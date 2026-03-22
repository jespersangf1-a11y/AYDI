"""Main visual analysis orchestrator for yacht image assessment.

Uses Claude's vision API to analyze yacht photos for spatial quality,
craftsmanship, materials, emotional impact, exterior design, and helm
ergonomics. Pure service — no database access.
"""
import base64
import json
import logging
import os
import re
from pathlib import Path

from app.core.config import settings

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


class VisualAnalyzer:
    """Orchestrates image analysis via Claude's vision API.

    Handles image loading, prompt selection, API calls, response parsing,
    confidence gating, and result caching. Gracefully degrades when the
    anthropic SDK is not installed.
    """

    MODEL = settings.ANTHROPIC_MODEL
    MODEL_DETAILED = "claude-opus-4-20250514"
    MAX_TOKENS = 4096
    MAX_TOKENS_DETAILED = 8192

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
                self._client = anthropic.Anthropic()
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

        # Check cache
        cache_key = self.cache.get_cache_key(image_path, image_type, boat_class, analysis_depth)
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

        # Call Claude vision API
        try:
            response = self.client.messages.create(
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
            )
        except Exception:
            logger.exception("Claude API call failed for %s", image_path)
            return self._error_result(image_path, image_type, "API-Aufruf fehlgeschlagen")

        # Extract text from response
        response_text = ""
        for block in response.content:
            if hasattr(block, "text"):
                response_text += block.text

        # Parse JSON
        parsed = self._parse_json_response(response_text)
        if parsed is None:
            logger.warning("Could not parse JSON from API response for %s", image_path)
            return self._error_result(
                image_path, image_type,
                "KI-Antwort konnte nicht verarbeitet werden",
                raw_response=response_text,
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
            analysis = r.get("analysis", {})
            findings = analysis.get("findings", [])
            if isinstance(findings, list):
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

        return base64.b64encode(data).decode("utf-8"), media_type

    def _parse_json_response(self, response_text: str) -> dict | None:
        """Parse JSON from AI response, handling markdown code blocks.

        The AI may wrap its JSON in ```json ... ``` blocks or include
        leading/trailing text. This method extracts and parses the JSON.

        Args:
            response_text: Raw text response from the AI.

        Returns:
            Parsed dict, or None if parsing fails.
        """
        if not response_text:
            return None

        text = response_text.strip()

        # Try direct parse first
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            pass

        # Strip markdown code block fences
        code_block_pattern = r"```(?:json)?\s*\n?(.*?)\n?\s*```"
        match = re.search(code_block_pattern, text, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(1).strip())
            except json.JSONDecodeError:
                pass

        # Try to find JSON object boundaries
        first_brace = text.find("{")
        last_brace = text.rfind("}")
        if first_brace >= 0 and last_brace > first_brace:
            try:
                return json.loads(text[first_brace:last_brace + 1])
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
        Returns the first matching score found, or None.
        """
        for key in SCORE_KEYS:
            if key in parsed:
                try:
                    return float(parsed[key])
                except (TypeError, ValueError):
                    pass
        return None

    def _unavailable_result(self, image_path: str, image_type: str, boat_class: str) -> dict:
        """Return a structured result when the anthropic SDK is not available."""
        return {
            "image_path": image_path,
            "image_type": image_type,
            "boat_class": boat_class,
            "analysis": None,
            "confidence": {
                "level": "insufficient",
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
        raw_response: str | None = None,
    ) -> dict:
        """Return a structured error result."""
        result = {
            "image_path": image_path,
            "image_type": image_type,
            "analysis": None,
            "confidence": {
                "level": "insufficient",
                "is_usable": False,
                "factors": [error_message],
                "image_quality": 0.0,
                "content_relevance": 0.0,
                "assessment_certainty": 0.0,
            },
            "score": None,
            "error": error_message,
        }
        if raw_response is not None:
            result["raw_response"] = raw_response[:2000]  # Truncate for safety
        return result
