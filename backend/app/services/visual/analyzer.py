"""Main visual analysis orchestrator for yacht image assessment.

Uses Claude's vision API to analyze yacht photos for spatial quality,
craftsmanship, materials, emotional impact, exterior design, and helm
ergonomics. Pure service — no database access.
"""
import asyncio
import base64
import io
import json
import logging
import math
import os
import re
from pathlib import Path

from app.core.config import settings
from app.core.retry import retry_async, get_circuit_breaker, NonRetryableError, RetryableError

logger = logging.getLogger(__name__)

MEDIA_TYPE_MAP = {
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".gif": "image/gif",
    ".webp": "image/webp",
}

# Score keys used by different prompt types
SCORE_KEYS = (
    "spatial_score",
    "overall_quality_score",
    "material_score",
    "emotional_score",
    "exterior_score",
    "helm_score",
)

# Gueltiger Score-Bereich (siehe CLAUDE.md: Scores sind immer 0-100)
SCORE_MIN = 0.0
SCORE_MAX = 100.0

# Keys, unter denen die Prompts ihre Einzelbefunde liefern. Der
# Build-Quality-Prompt (quality.py) verwendet "overall_findings", alle
# anderen "findings" — die Aggregation muss BEIDE einsammeln, sonst sieht
# der Nutzer die Verarbeitungsbefunde nie.
FINDING_KEYS = ("findings", "overall_findings")

# --- Bildvorbereitung ------------------------------------------------------
# Die Vision-API rechnet Bilder intern ohnehin auf ~1568 px laengste Kante
# herunter. Alles darueber kostet nur Upload-Zeit, Latenz und Tokens.
MAX_IMAGE_EDGE_PX = 1568
# Rohbytes, ab denen auch ein masshaltiges Bild neu komprimiert wird.
MAX_IMAGE_BYTES = 3_000_000
JPEG_QUALITY = 85


class VisualAnalyzer:
    """Orchestrates image analysis via Claude's vision API.

    Handles image loading, prompt selection, API calls, response parsing,
    confidence gating, and result caching. Gracefully degrades when the
    anthropic SDK is not installed.
    """

    MODEL = settings.ANTHROPIC_MODEL
    # Ebenfalls zurueckgezogen (siehe config.py). Fuer die Tiefenanalyse
    # dasselbe aktuelle Modell wie im Standardfall.
    MODEL_DETAILED = settings.ANTHROPIC_MODEL
    MAX_TOKENS = 4096
    MAX_TOKENS_DETAILED = 8192
    # Wartezeit-Obergrenze pro API-Versuch (Sekunden).
    # Aus der Konfiguration: VISUAL_ANALYSIS_TIMEOUT_SEC war deklariert, wurde
    # aber nirgends gelesen.
    API_TIMEOUT_S = float(settings.VISUAL_ANALYSIS_TIMEOUT_SEC)

    def __init__(self):
        self._client = None
        self._cache = None
        self._gatekeeper = None

    @property
    def client(self):
        """Lazy-initialize Anthropic client. Returns None if SDK unavailable."""
        if self._client is None:
            try:
                import anthropic
                # Pass the configured key explicitly; if None the SDK falls back
                # to the ANTHROPIC_API_KEY env var (so .env config is honoured).
                self._client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)
            except ImportError:
                logger.warning("anthropic SDK not installed — visual analysis unavailable")
                self._client = None
            except Exception:
                logger.exception("Failed to initialize Anthropic client")
                self._client = None
        return self._client

    @property
    def cache(self):
        """Lazy-initialize analysis cache."""
        if self._cache is None:
            from app.services.visual.cache import AnalysisCache
            self._cache = AnalysisCache()
        return self._cache

    @property
    def gatekeeper(self):
        """Lazy-initialize confidence gatekeeper."""
        if self._gatekeeper is None:
            from app.services.visual.confidence import ConfidenceGatekeeper
            self._gatekeeper = ConfidenceGatekeeper()
        return self._gatekeeper

    async def analyze_image(
        self,
        image_path: str,
        image_type: str,
        boat_class: str,
        zone_type: str | None = None,
        analysis_depth: str = "standard",
        context: dict | None = None,
        boat_dna: object | None = None,
    ) -> dict:
        """Analyze a single yacht image.

        Args:
            image_path: Path to the image file on disk.
            image_type: Image category (e.g. 'interior_overview', 'helm_station').
            boat_class: Yacht class for calibrated evaluation.
            zone_type: Optional zone type for focused analysis.
            analysis_depth: 'standard' or 'detailed' (uses stronger model).
            context: Optional extra context (length_m, beam_m, etc.).
            boat_dna: Optional BoatDNA object for expert knowledge injection.

        Returns:
            Structured analysis result dict with score, findings,
            confidence assessment, and metadata.
        """
        # Check SDK availability
        if self.client is None:
            return self._unavailable_result(image_path, image_type, boat_class)

        # Check cache — zone_type and context change the prompt, so include them.
        cache_key = self.cache.get_cache_key(
            image_path, image_type, boat_class, analysis_depth,
            zone_type=zone_type, context=context,
        )
        cached = self.cache.get(cache_key)
        if cached is not None:
            logger.info("Cache hit for %s (%s)", image_path, image_type)
            return cached

        # Load image
        try:
            image_data, media_type = self._load_image_base64(image_path)
        except FileNotFoundError:
            logger.error("Image file not found: %s", image_path)
            return self._error_result(image_path, image_type, "Bilddatei nicht gefunden")
        except ValueError as e:
            logger.error("Unsupported image format: %s", e)
            return self._error_result(image_path, image_type, str(e))

        # Build visual context if boat_dna provided
        visual_context = None
        if boat_dna is not None:
            try:
                from app.services.visual.prompt_context import build_visual_context
                visual_context = build_visual_context(boat_dna)
            except Exception:
                logger.warning("Failed to build visual context from boat_dna", exc_info=True)

        # Get prompt
        from app.services.visual.prompts import get_prompt
        prompt = get_prompt(image_type, boat_class, zone_type, context, visual_context)

        # Select model
        model = self.MODEL_DETAILED if analysis_depth == "detailed" else self.MODEL
        max_tokens = self.MAX_TOKENS_DETAILED if analysis_depth == "detailed" else self.MAX_TOKENS

        # Call Claude vision API with retry + circuit breaker
        breaker = get_circuit_breaker(
            "anthropic_vision_api", failure_threshold=5, recovery_timeout=60.0
        )
        if not breaker.allow_request():
            logger.warning("Circuit breaker not admitting calls for Anthropic Vision API — skipping")
            return self._error_result(
                image_path, image_type,
                "API vorübergehend nicht verfügbar (Circuit Breaker offen). Bitte später erneut versuchen.",
            )

        def _blocking_create():
            """Der eigentliche — synchrone und blockierende — SDK-Aufruf."""
            return self.client.messages.create(
                model=model,
                max_tokens=max_tokens,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "image",
                                "source": {
                                    "type": "base64",
                                    "media_type": media_type,
                                    "data": image_data,
                                },
                            },
                            {
                                "type": "text",
                                "text": prompt,
                            },
                        ],
                    }
                ],
                # Eigenes SDK-Timeout: begrenzt die Lebensdauer des
                # Worker-Threads, den wait_for nicht abbrechen kann.
                timeout=self.API_TIMEOUT_S,
            )

        async def _call_claude_api():
            """Wrapper for the synchronous Anthropic SDK call.

            Der SDK-Aufruf ist blockierend und laeuft deshalb via
            ``asyncio.to_thread`` in einem Worker-Thread. Nur so bleibt der
            Event-Loop frei und das in ``retry_async`` gesetzte
            ``asyncio.wait_for``-Timeout kann ueberhaupt greifen: Stuende der
            blockierende Aufruf direkt unter ``wait_for``, kaeme der Loop
            waehrend des Aufrufs nie zum Zug und das Timeout waere wirkungslos.

            WICHTIG: Ein ``wait_for``-Timeout beendet den Worker-Thread NICHT —
            Python kann einen laufenden Thread nicht abbrechen. Es begrenzt
            ausschliesslich unsere Wartezeit; der Thread laeuft im Hintergrund
            weiter, bis der SDK-Aufruf selbst zurueckkehrt. Deshalb bekommt der
            SDK zusaetzlich sein eigenes Client-Timeout mit (siehe _blocking_create).
            """
            try:
                return await asyncio.to_thread(_blocking_create)
            except Exception as e:
                # Classify so the retry layer actually acts: permanent errors
                # (auth, 400 bad request) must NOT be retried; transient ones
                # (429 rate limit, 5xx, timeouts, connection) MUST be re-raised
                # as RetryableError — otherwise retry_async treats the raw SDK
                # exception as non-retryable and aborts on the first failure.
                error_str = str(e).lower()
                status_code = getattr(e, "status_code", None)
                if status_code in (401, 403) or "invalid_api_key" in error_str or "authentication" in error_str:
                    raise NonRetryableError(f"Authentication error: {e}") from e
                if status_code == 400 or "invalid_request" in error_str:
                    raise NonRetryableError(f"Invalid request: {e}") from e
                # 404 heisst hier praktisch immer: die konfigurierte Modell-ID gibt
                # es nicht (mehr). Das wird beim naechsten Versuch nicht anders —
                # zuvor galt es als "voruebergehend" und wurde viermal mit Backoff
                # wiederholt: 7 Sekunden und 4 API-Anfragen pro Bild, jedes Mal
                # vergeblich, und in den Logs sah es nach einer Stoerung aus statt
                # nach einer Fehlkonfiguration.
                if status_code == 404 or "not_found" in error_str:
                    raise NonRetryableError(
                        f"Modell oder Endpunkt nicht gefunden (ANTHROPIC_MODEL pruefen): {e}"
                    ) from e
                # Everything else (429, 5xx, timeouts, connection resets) is transient.
                raise RetryableError(f"Transient API error: {e}") from e

        retry_result = await retry_async(
            _call_claude_api,
            max_retries=3,
            base_delay=1.0,
            max_delay=15.0,
            timeout=self.API_TIMEOUT_S,
            context=f"vision_api:{image_type}:{Path(image_path).name}",
        )

        if not retry_result.success:
            breaker.record_failure()
            logger.error(
                "Claude API call failed for %s after %d attempts (%.0fms): %s",
                image_path, retry_result.attempts, retry_result.total_time_ms, retry_result.error,
            )
            # Generic client-facing message — internal error details stay in logs.
            return self._error_result(
                image_path, image_type,
                "Die visuelle Analyse ist fehlgeschlagen. Bitte später erneut versuchen.",
            )

        breaker.record_success()
        response = retry_result.value

        # Extract text from response
        response_text = ""
        for block in response.content:
            if hasattr(block, "text"):
                response_text += block.text

        # Parse JSON
        parsed = self._parse_json_response(response_text)
        if parsed is None:
            # Log the raw response for debugging but never return it to the client.
            logger.warning(
                "Could not parse JSON from API response for %s: %s",
                image_path, response_text[:500],
            )
            return self._error_result(
                image_path, image_type,
                "KI-Antwort konnte nicht verarbeitet werden",
            )

        # Get image metadata for confidence assessment
        image_metadata = self._get_image_metadata(image_path)

        # Run confidence gatekeeper
        confidence = self.gatekeeper.evaluate(parsed, image_metadata)

        # Build result
        result = {
            "image_path": image_path,
            "image_type": image_type,
            "boat_class": boat_class,
            "zone_type": zone_type,
            "analysis_depth": analysis_depth,
            "model_used": model,
            "analysis": parsed,
            "confidence": {
                "level": confidence.level.value,
                "is_usable": confidence.is_usable,
                "factors": confidence.factors,
                "image_quality": confidence.image_quality,
                "content_relevance": confidence.content_relevance,
                "assessment_certainty": confidence.assessment_certainty,
            },
            "score": self._extract_score(parsed),
        }

        # Cache result
        self.cache.set(cache_key, result)
        logger.info(
            "Analyzed %s (%s): score=%.1f, confidence=%s",
            image_path, image_type,
            result["score"] or 0.0,
            confidence.level.value,
        )

        return result

    async def analyze_batch(
        self,
        images: list[dict],
        boat_class: str,
        zone_type: str | None = None,
        analysis_depth: str = "standard",
        boat_dna: object | None = None,
    ) -> dict:
        """Analyze multiple images and fuse results.

        Args:
            images: List of dicts with keys: path, image_type, zone_name (optional).
            boat_class: Yacht class for calibrated evaluation.
            zone_type: Optional zone type for focused analysis.
            analysis_depth: 'standard' or 'detailed'.
            boat_dna: Optional BoatDNA object for expert knowledge injection.

        Returns:
            Fused result dict with weighted scores, deduplicated findings,
            and per-image results.
        """
        individual_results = []
        for img in images:
            result = await self.analyze_image(
                image_path=img["path"],
                image_type=img.get("image_type", "interior_overview"),
                boat_class=boat_class,
                zone_type=img.get("zone_name") or zone_type,
                analysis_depth=analysis_depth,
                boat_dna=boat_dna,
            )
            individual_results.append(result)

        # Filter usable results
        usable = [r for r in individual_results if r.get("confidence", {}).get("is_usable", False)]
        unusable_count = len(individual_results) - len(usable)

        if not usable:
            return {
                "total_images": len(images),
                "usable_images": 0,
                "unusable_images": unusable_count,
                "fused_score": None,
                "findings": [],
                "warnings": [
                    "Keine Bilder mit ausreichender Qualitaet fuer zuverlaessige Analyse."
                ],
                "individual_results": individual_results,
            }

        # Weighted average score (weight by confidence certainty)
        scores = []
        weights = []
        for r in usable:
            score = r.get("score")
            certainty = r.get("confidence", {}).get("assessment_certainty", 0.5)
            if score is not None:
                scores.append(score)
                weights.append(certainty)

        if scores and weights:
            total_weight = sum(weights)
            fused_score = sum(s * w for s, w in zip(scores, weights)) / total_weight if total_weight > 0 else None
        else:
            fused_score = None

        # Collect and deduplicate findings
        all_findings = []
        seen_observations = set()
        for r in usable:
            analysis = r.get("analysis")
            if not isinstance(analysis, dict):
                continue
            # Beide Befund-Keys beruecksichtigen: der Build-Quality-Prompt
            # liefert "overall_findings" — diese Befunde wurden bisher
            # stillschweigend verworfen und erreichten den Nutzer nie.
            for findings_key in FINDING_KEYS:
                findings = analysis.get(findings_key)
                if not isinstance(findings, list):
                    continue
                for f in findings:
                    obs = f.get("observation", "") if isinstance(f, dict) else str(f)
                    if obs and obs not in seen_observations:
                        seen_observations.add(obs)
                        all_findings.append(f)

        # Cross-validate: flag high variance
        cross_validation_warnings = []
        if len(scores) >= 2:
            score_range = max(scores) - min(scores)
            if score_range > 30:
                cross_validation_warnings.append(
                    f"Hohe Bewertungsvarianz zwischen Bildern (Spanne: {score_range:.0f} Punkte). "
                    "Ergebnisse mit Vorsicht interpretieren."
                )

        return {
            "total_images": len(images),
            "usable_images": len(usable),
            "unusable_images": unusable_count,
            "fused_score": round(fused_score, 1) if fused_score is not None else None,
            "findings": all_findings,
            "cross_validation_warnings": cross_validation_warnings,
            "individual_results": individual_results,
        }

    def _load_image_base64(self, image_path: str) -> tuple[str, str]:
        """Load an image file and return base64-encoded data with media type.

        Args:
            image_path: Path to the image file.

        Returns:
            Tuple of (base64_data_string, media_type_string).

        Raises:
            FileNotFoundError: If the image file does not exist.
            ValueError: If the image format is not supported.
        """
        path = Path(image_path)
        if not path.exists():
            raise FileNotFoundError(f"Image not found: {image_path}")

        suffix = path.suffix.lower()
        media_type = MEDIA_TYPE_MAP.get(suffix)
        if media_type is None:
            raise ValueError(
                f"Nicht unterstuetztes Bildformat: {suffix}. "
                f"Unterstuetzt: {', '.join(MEDIA_TYPE_MAP.keys())}"
            )

        with open(path, "rb") as f:
            data = f.read()

        # Grosse Fotos (Handy-Aufnahmen: 10-20 MB) vor dem Kodieren
        # herunterrechnen — spart Upload-Zeit, Latenz und Token-Kosten.
        data, media_type = self._prepare_image_bytes(data, media_type)

        return base64.b64encode(data).decode("utf-8"), media_type

    def _prepare_image_bytes(self, raw: bytes, media_type: str) -> tuple[bytes, str]:
        """Skaliere/komprimiere ein Bild vor der base64-Kodierung.

        Die Vision-API rechnet Bilder ohnehin auf ~1568 px laengste Kante
        herunter; alles darueber ist reine Upload-, Latenz- und Token-
        Verschwendung. Bilder innerhalb der Grenzen werden unveraendert
        durchgereicht (kein unnoetiger Qualitaetsverlust durch Re-Encoding).

        Faellt Pillow aus (nicht installiert, defekte oder unlesbare Datei),
        werden die Originalbytes unveraendert zurueckgegeben — die Analyse
        laeuft dann wie bisher, nur eben ungeskaliert.

        Args:
            raw: Originalbytes der Bilddatei.
            media_type: Media-Type aus der Dateiendung.

        Returns:
            Tuple (bytes, media_type) — der Media-Type kann sich beim
            Re-Encoding aendern (z.B. GIF/WebP -> JPEG).
        """
        try:
            from PIL import Image
        except ImportError:
            logger.debug("Pillow nicht installiert — Bild wird ungeskaliert gesendet")
            return raw, media_type

        try:
            with Image.open(io.BytesIO(raw)) as img:
                img.load()
                width, height = img.size
                longest = max(width, height)
                needs_resize = longest > MAX_IMAGE_EDGE_PX
                if not needs_resize and len(raw) <= MAX_IMAGE_BYTES:
                    return raw, media_type

                if needs_resize:
                    scale = MAX_IMAGE_EDGE_PX / longest
                    img = img.resize(
                        (max(1, round(width * scale)), max(1, round(height * scale))),
                        Image.LANCZOS,
                    )

                has_alpha = img.mode in ("RGBA", "LA") or (
                    img.mode == "P" and "transparency" in img.info
                )
                buffer = io.BytesIO()
                if has_alpha:
                    out_media_type = "image/png"
                    img.convert("RGBA").save(buffer, format="PNG", optimize=True)
                else:
                    out_media_type = "image/jpeg"
                    img.convert("RGB").save(
                        buffer, format="JPEG", quality=JPEG_QUALITY, optimize=True
                    )
                prepared = buffer.getvalue()
        except Exception:
            logger.warning(
                "Bild konnte nicht skaliert werden — sende Originalbytes",
                exc_info=True,
            )
            return raw, media_type

        # Re-Encoding ohne Groessengewinn: Original behalten.
        if not needs_resize and len(prepared) >= len(raw):
            return raw, media_type

        logger.info(
            "Bild fuer Vision-API aufbereitet: %dx%d, %.2f MB -> %.2f MB (%s)",
            width, height, len(raw) / 1e6, len(prepared) / 1e6, out_media_type,
        )
        return prepared, out_media_type

    def _parse_json_response(self, response_text: str) -> dict | None:
        """Parse JSON from AI response, handling markdown code blocks.

        The AI may wrap its JSON in ```json ... ``` blocks or include
        leading/trailing text. This method extracts and parses the JSON.

        Schema-Guard: Akzeptiert wird ausschliesslich ein JSON-OBJEKT. Liefert
        das Modell eine Liste, eine Zahl oder einen String — auch innerhalb von
        Markdown-Fences —, wird das Ergebnis verworfen und None zurueckgegeben.
        Sonst schlaegt die Weiterverarbeitung mit AttributeError fehl, weil auf
        dem Resultat ``.get()`` aufgerufen wird.

        Args:
            response_text: Raw text response from the AI.

        Returns:
            Parsed dict, or None if parsing fails or the JSON is not an object.
        """
        if not response_text:
            return None

        text = response_text.strip()

        def _as_object(candidate: object) -> dict | None:
            """Nur Objekte durchlassen — alles andere ist Schema-Verletzung."""
            if isinstance(candidate, dict):
                return candidate
            logger.warning(
                "KI-Antwort ist kein JSON-Objekt, sondern %s — verworfen",
                type(candidate).__name__,
            )
            return None

        # Try direct parse first
        try:
            return _as_object(json.loads(text))
        except json.JSONDecodeError:
            pass

        # Strip markdown code block fences
        code_block_pattern = r"```(?:json)?\s*\n?(.*?)\n?\s*```"
        match = re.search(code_block_pattern, text, re.DOTALL)
        if match:
            try:
                return _as_object(json.loads(match.group(1).strip()))
            except json.JSONDecodeError:
                pass

        # Try to find JSON object boundaries
        first_brace = text.find("{")
        last_brace = text.rfind("}")
        if first_brace >= 0 and last_brace > first_brace:
            try:
                return _as_object(json.loads(text[first_brace:last_brace + 1]))
            except json.JSONDecodeError:
                pass

        logger.warning("All JSON parsing strategies failed")
        return None

    def _get_image_metadata(self, image_path: str) -> dict:
        """Extract basic image metadata (dimensions, file size).

        Args:
            image_path: Path to the image file.

        Returns:
            Dict with width, height, file_size_bytes. Values may be 0
            if metadata cannot be extracted.
        """
        metadata = {"width": 0, "height": 0, "file_size_bytes": 0}

        try:
            metadata["file_size_bytes"] = os.path.getsize(image_path)
        except OSError:
            pass

        # Try PIL/Pillow for dimensions
        try:
            from PIL import Image
            with Image.open(image_path) as img:
                metadata["width"], metadata["height"] = img.size
        except ImportError:
            logger.debug("Pillow not installed — image dimensions unavailable")
        except Exception:
            logger.debug("Could not read image dimensions from %s", image_path)

        return metadata

    def _extract_score(self, parsed: dict) -> float | None:
        """Extract the primary score from a parsed analysis result.

        Different prompt types use different score key names.
        Returns the first VALID score found, or None.

        Validierung (B-11): ``True`` ist in Python ein ``int`` und wuerde
        stillschweigend zu 1.0 — ein erfundener Score. Ebenso werden NaN/Inf
        und Werte ausserhalb 0-100 verworfen. In all diesen Faellen liefern wir
        lieber None ("nicht beurteilbar") als eine erfundene Zahl.
        """
        if not isinstance(parsed, dict):
            return None

        for key in SCORE_KEYS:
            if key not in parsed:
                continue
            raw = parsed[key]

            # bool ist Subklasse von int: True -> 1.0 waere ein Fantasie-Score.
            if isinstance(raw, bool):
                logger.warning("Score '%s' ist ein Boolean (%r) — verworfen", key, raw)
                continue

            try:
                value = float(raw)
            except (TypeError, ValueError):
                continue

            if not math.isfinite(value):
                logger.warning("Score '%s' ist nicht endlich (%r) — verworfen", key, raw)
                continue

            if not SCORE_MIN <= value <= SCORE_MAX:
                logger.warning(
                    "Score '%s' ausserhalb des gueltigen Bereichs 0-100 (%r) — verworfen",
                    key, value,
                )
                continue

            return value

        return None

    def _unavailable_result(self, image_path: str, image_type: str, boat_class: str) -> dict:
        """Return a structured result when the anthropic SDK is not available."""
        return {
            "image_path": image_path,
            "image_type": image_type,
            "boat_class": boat_class,
            "analysis": None,
            "confidence": {
                "level": "visual_insufficient",
                "is_usable": False,
                "factors": ["Anthropic SDK nicht installiert — visuelle Analyse nicht verfuegbar"],
                "image_quality": 0.0,
                "content_relevance": 0.0,
                "assessment_certainty": 0.0,
            },
            "score": None,
            "error": "Anthropic SDK nicht installiert. Bitte 'pip install anthropic' ausfuehren.",
        }

    def _error_result(
        self,
        image_path: str,
        image_type: str,
        error_message: str,
    ) -> dict:
        """Return a structured error result.

        ``error_message`` must be a generic, client-safe string — raw model
        output and internal exception text are logged, never returned here.
        """
        return {
            "image_path": image_path,
            "image_type": image_type,
            "analysis": None,
            "confidence": {
                "level": "visual_insufficient",
                "is_usable": False,
                "factors": [error_message],
                "image_quality": 0.0,
                "content_relevance": 0.0,
                "assessment_certainty": 0.0,
            },
            "score": None,
            "error": error_message,
        }


# ---------------------------------------------------------------------------
# Module-level convenience wrapper
#
# Routes import `analyze_image` from this module (a plain function), while the
# real logic lives on the async `VisualAnalyzer.analyze_image` method. This
# wrapper bridges the two: it maps the route-facing `file_path` argument to the
# analyzer's `image_path` parameter and drives the coroutine to completion.
# ---------------------------------------------------------------------------

_default_analyzer: "VisualAnalyzer | None" = None


def _get_default_analyzer() -> "VisualAnalyzer":
    """Return a process-wide shared VisualAnalyzer instance."""
    global _default_analyzer
    if _default_analyzer is None:
        _default_analyzer = VisualAnalyzer()
    return _default_analyzer


def analyze_image(
    file_path: str,
    image_type: str,
    boat_class: str,
    zone_type: str | None = None,
    analysis_depth: str = "standard",
    context: dict | None = None,
    boat_dna: object | None = None,
) -> dict:
    """Synchronous wrapper around ``VisualAnalyzer.analyze_image``.

    IMPORTANT: must be called OFF the event loop (e.g. via ``asyncio.to_thread``)
    — it uses ``asyncio.run`` and would raise inside an already-running loop.
    This also keeps the blocking Anthropic SDK call off the main event loop.
    """
    import asyncio

    return asyncio.run(
        _get_default_analyzer().analyze_image(
            image_path=file_path,
            image_type=image_type,
            boat_class=boat_class,
            zone_type=zone_type,
            analysis_depth=analysis_depth,
            context=context,
            boat_dna=boat_dna,
        )
    )
