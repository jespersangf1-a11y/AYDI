"""Confidence gatekeeper for visual analysis results.

Ensures only reliable assessments reach users. Evaluates image quality,
content relevance, and AI self-reported certainty to determine whether
a visual analysis result is trustworthy enough to present.

Grundregel des Projekts: Unbekanntes wird IMMER konservativ nach unten
bewertet — lieber "nicht beurteilbar" als eine geratene Sicherheit.
"""
import logging
from dataclasses import dataclass, field
from enum import Enum

logger = logging.getLogger(__name__)

CONFIDENCE_WORD_MAP = {
    "hoch": 0.9,
    "high": 0.9,
    "mittel": 0.6,
    "medium": 0.6,
    "niedrig": 0.3,
    "low": 0.3,
    "sehr hoch": 0.95,
    "sehr niedrig": 0.15,
    # Der Materialprompt benutzt eine eigene Wortskala fuer Identifikationen
    "sicher": 0.9,
    "wahrscheinlich": 0.6,
    "vermutet": 0.3,
    # Explizite Nicht-Aussagen
    "nicht beurteilbar": 0.1,
    "unbekannt": 0.1,
    "keine angabe": 0.1,
}

# Top-Level-Keys, unter denen die Vision-Prompts ihre Selbsteinschaetzung
# zurueckgeben. Der Build-Quality-Prompt (prompts/quality.py, verwendet fuer
# image_type "interior_detail" und "exterior_detail") liefert
# "confidence_overall", alle uebrigen Prompts liefern "confidence".
# Die weiteren Aliase sind defensive Schreibvarianten des Modells.
CONFIDENCE_KEY_ALIASES = (
    "confidence",
    "confidence_overall",
    "overall_confidence",
    "confidence_level",
)

# Werte, mit denen das Modell "ja" bzw. "nein" auf assessable antwortet.
ASSESSABLE_TRUE_WORDS = {"true", "ja", "yes", "1"}
ASSESSABLE_FALSE_WORDS = {
    "false", "nein", "no", "0",
    "nicht beurteilbar", "unbeurteilbar", "nicht bewertbar",
}


class VisualConfidence(str, Enum):
    HIGH = "visual_high"
    MEDIUM = "visual_medium"
    LOW = "visual_low"
    INSUFFICIENT = "visual_insufficient"


@dataclass
class ConfidenceAssessment:
    """Result of confidence evaluation for a visual analysis."""
    level: VisualConfidence
    factors: list[str] = field(default_factory=list)
    image_quality: float = 0.0       # 0-1
    content_relevance: float = 0.0   # 0-1
    assessment_certainty: float = 0.0  # 0-1
    # None = Modell hat sich nicht geaeussert, False = explizit "nicht beurteilbar"
    model_assessable: bool | None = None
    # False = Bildguete nur aus Metadaten geschaetzt (keine Schaerfe-/Belichtungspruefung)
    image_quality_measured: bool = False

    @property
    def is_usable(self) -> bool:
        """Whether this assessment is reliable enough to show to the user."""
        if self.model_assessable is False:
            # Das Modell sagt ausdruecklich "kann ich nicht beurteilen" — das
            # schlaegt jede rechnerische Einstufung.
            return False
        return self.level in (VisualConfidence.HIGH, VisualConfidence.MEDIUM)


class ConfidenceGatekeeper:
    """Evaluates whether a visual analysis result is trustworthy."""

    MIN_IMAGE_QUALITY = 0.4
    MIN_CONTENT_RELEVANCE = 0.5
    MIN_ASSESSMENT_CERTAINTY = 0.5

    # Minimum resolution (width * height) for acceptable quality
    MIN_RESOLUTION = 640 * 480
    GOOD_RESOLUTION = 1920 * 1080

    # File size thresholds (bytes) as compression quality proxy
    MIN_FILE_SIZE = 50_000       # 50 KB
    GOOD_FILE_SIZE = 500_000     # 500 KB

    # Ohne echte Schaerfe-/Belichtungspruefung sagen Aufloesung und Dateigroesse
    # nichts darueber aus, ob ein Bild scharf, ausreichend belichtet und
    # sinnvoll ausgeschnitten ist. Die reine Metadaten-Bewertung ist deshalb
    # gedeckelt — sie darf nie "perfektes Bild" behaupten.
    METADATA_ONLY_QUALITY_CAP = 0.85

    # Sicherheit, wenn das Modell keine oder eine unverstaendliche
    # Selbsteinschaetzung liefert: bewusst unterhalb MIN_ASSESSMENT_CERTAINTY.
    UNKNOWN_CERTAINTY = 0.3

    def evaluate(self, ai_response: dict, image_metadata: dict) -> ConfidenceAssessment:
        """Evaluate the confidence of an AI visual analysis result.

        Args:
            ai_response: Parsed JSON response from the AI vision model.
            image_metadata: Dict with keys like width, height, file_size_bytes.
                Optionale Wahrnehmungsmetriken ("sharpness", "brightness",
                jeweils 0-1) werden verwendet, sobald der Aufrufer sie liefert.

        Returns:
            ConfidenceAssessment with level, factors, and component scores.
        """
        factors: list[str] = []

        image_quality, quality_measured = self._assess_image_quality_detail(image_metadata)
        if image_quality < self.MIN_IMAGE_QUALITY:
            factors.append(f"Bildqualitaet niedrig ({image_quality:.2f})")
        if not quality_measured:
            factors.append(
                "Bildguete nur aus Metadaten geschaetzt — Schaerfe, Belichtung "
                "und Bildausschnitt wurden nicht geprueft"
            )

        content_relevance = self._assess_content_relevance(ai_response)
        if content_relevance < self.MIN_CONTENT_RELEVANCE:
            factors.append(f"Inhaltliche Relevanz niedrig ({content_relevance:.2f})")

        assessment_certainty = self._assess_ai_certainty(ai_response)
        if assessment_certainty < self.MIN_ASSESSMENT_CERTAINTY:
            factors.append(f"KI-Sicherheit niedrig ({assessment_certainty:.2f})")
        if self._resolve_stated_certainty(ai_response) is None:
            factors.append("KI-Selbsteinschaetzung fehlt oder ist unverstaendlich")

        # Determine overall level
        avg = (image_quality + content_relevance + assessment_certainty) / 3.0

        if avg >= 0.75 and image_quality >= self.MIN_IMAGE_QUALITY:
            level = VisualConfidence.HIGH
        elif avg >= 0.55 and image_quality >= self.MIN_IMAGE_QUALITY:
            level = VisualConfidence.MEDIUM
        elif avg >= 0.35:
            level = VisualConfidence.LOW
            factors.append("Ergebnis mit Vorsicht zu interpretieren")
        else:
            level = VisualConfidence.INSUFFICIENT
            factors.append("Bewertung nicht zuverlaessig genug")

        # Die Selbsteinschaetzung muss auch wirken: liegt sie (oder ihr
        # konservativer Ersatzwert bei fehlender/unlesbarer Angabe) unter dem
        # Schwellenwert, darf das Ergebnis nicht als belastbar gelten — sonst
        # uebertoenen Aufloesung und Befundzahl ein "niedrig" des Modells.
        if assessment_certainty < self.MIN_ASSESSMENT_CERTAINTY and level in (
            VisualConfidence.HIGH,
            VisualConfidence.MEDIUM,
        ):
            level = VisualConfidence.LOW
            factors.append("Ergebnis mit Vorsicht zu interpretieren")

        # Hartes Veto: sagt das Modell selbst "nicht beurteilbar", wird das
        # Ergebnis nie als belastbar ausgewiesen — unabhaengig davon, was die
        # Rechnung ergibt.
        model_assessable = self._resolve_assessable(ai_response)
        if model_assessable is False:
            level = VisualConfidence.INSUFFICIENT
            factors.insert(0, "Modell hat das Bild als nicht beurteilbar markiert")

        if not factors:
            factors.append("Alle Qualitaetskriterien erfuellt")

        return ConfidenceAssessment(
            level=level,
            factors=factors,
            image_quality=round(image_quality, 3),
            content_relevance=round(content_relevance, 3),
            assessment_certainty=round(assessment_certainty, 3),
            model_assessable=model_assessable,
            image_quality_measured=quality_measured,
        )

    def _assess_image_quality(self, metadata: dict) -> float:
        """Assess image quality from resolution and file size.

        Returns a score between 0.0 and 1.0. Ohne Wahrnehmungsmetriken ist der
        Wert auf METADATA_ONLY_QUALITY_CAP gedeckelt.
        """
        score, _ = self._assess_image_quality_detail(metadata)
        return score

    def _assess_image_quality_detail(self, metadata: dict) -> tuple[float, bool]:
        """Assess image quality and report whether it was actually measured.

        Returns:
            (score 0.0-1.0, measured). "measured" ist nur True, wenn der
            Aufrufer Wahrnehmungsmetriken mitgeliefert hat. Sonst beruht der
            Wert allein auf Aufloesung und Dateigroesse und ist gedeckelt.
        """
        metadata = metadata or {}
        width = metadata.get("width", 0) or 0
        height = metadata.get("height", 0) or 0
        file_size = metadata.get("file_size_bytes", 0) or 0

        # Resolution score
        resolution = width * height
        if resolution <= 0:
            res_score = 0.2  # Unknown resolution, assume low
        elif resolution >= self.GOOD_RESOLUTION:
            res_score = 1.0
        elif resolution >= self.MIN_RESOLUTION:
            res_score = 0.5 + 0.5 * (resolution - self.MIN_RESOLUTION) / (self.GOOD_RESOLUTION - self.MIN_RESOLUTION)
        else:
            res_score = 0.5 * resolution / self.MIN_RESOLUTION

        # File size as compression quality proxy
        if file_size <= 0:
            size_score = 0.3  # Unknown size
        elif file_size >= self.GOOD_FILE_SIZE:
            size_score = 1.0
        elif file_size >= self.MIN_FILE_SIZE:
            size_score = 0.5 + 0.5 * (file_size - self.MIN_FILE_SIZE) / (self.GOOD_FILE_SIZE - self.MIN_FILE_SIZE)
        else:
            size_score = 0.5 * file_size / self.MIN_FILE_SIZE

        # Weighted combination: resolution matters more
        metadata_score = 0.7 * res_score + 0.3 * size_score

        perceptual = self._perceptual_score(metadata)
        if perceptual is None:
            # Ehrliche Deckelung: Aufloesung und Dateigroesse erkennen kein
            # unscharfes, dunkles oder falsch ausgeschnittenes Bild. Ohne diese
            # Pruefung gibt es kein "perfektes Bild".
            return min(metadata_score, self.METADATA_ONLY_QUALITY_CAP), False

        # Konservativ: der schlechtere der beiden Befunde entscheidet.
        return min(metadata_score, perceptual), True

    def _perceptual_score(self, metadata: dict) -> float | None:
        """Derive a score from optional perceptual metrics.

        Erkannte Keys (alle optional, 0-1): "sharpness" (1 = scharf),
        "brightness" (0 = schwarz, 0.5 = ideal belichtet, 1 = ausgebrannt).
        Returns None when no usable metric is present.
        """
        scores: list[float] = []

        sharpness = self._as_unit_float(metadata.get("sharpness"))
        if sharpness is not None:
            scores.append(sharpness)

        brightness = self._as_unit_float(metadata.get("brightness"))
        if brightness is not None:
            # Abweichung von der idealen Belichtung bestraft in beide Richtungen
            scores.append(max(0.0, 1.0 - 2.0 * abs(brightness - 0.5)))

        if not scores:
            return None
        return min(scores)

    @staticmethod
    def _as_unit_float(value) -> float | None:
        """Return value as float in [0,1], or None when unusable."""
        if value is None or isinstance(value, bool):
            return None
        if not isinstance(value, (int, float)):
            return None
        value = float(value)
        if value < 0.0 or value > 1.0:
            return None
        return value

    def _assess_content_relevance(self, ai_response: dict) -> float:
        """Assess whether the AI found meaningful yacht-related content.

        Returns a score between 0.0 and 1.0.
        """
        if not ai_response:
            return 0.0

        # Check if the AI explicitly flagged content as not assessable
        if self._resolve_assessable(ai_response) is False:
            return 0.2

        # Count cannot_assess items — more items = less relevance
        cannot_assess = ai_response.get("cannot_assess", [])
        if isinstance(cannot_assess, list) and len(cannot_assess) > 0:
            # Each cannot_assess item reduces relevance
            penalty = min(len(cannot_assess) * 0.1, 0.5)
            base = 0.8 - penalty
        else:
            base = 0.9

        # Check if findings exist. Der Build-Quality-Prompt nennt seine
        # Befundliste "overall_findings", die uebrigen Prompts "findings".
        for findings_key in ("findings", "overall_findings"):
            findings = ai_response.get(findings_key)
            if isinstance(findings, (list, dict)) and len(findings) > 0:
                base = min(1.0, base + 0.1)
                break

        return max(0.0, base)

    def _resolve_assessable(self, ai_response: dict) -> bool | None:
        """Resolve the model's explicit "assessable" statement.

        Returns True/False when the model made a statement, None when the field
        is absent. Unverstaendliche Werte gelten konservativ als "nicht
        beurteilbar".
        """
        if not ai_response or "assessable" not in ai_response:
            return None

        value = ai_response.get("assessable")
        if isinstance(value, bool):
            return value
        if value is None:
            return False
        if isinstance(value, (int, float)):
            return bool(value)
        if isinstance(value, str):
            normalized = value.strip().lower()
            if normalized in ASSESSABLE_TRUE_WORDS:
                return True
            if normalized in ASSESSABLE_FALSE_WORDS:
                return False
            logger.debug("Unbekannter assessable-Wert %r — konservativ als False gewertet", value)
            return False
        return False

    def _resolve_stated_certainty(self, ai_response: dict) -> float | None:
        """Resolve the AI's own confidence statement to a 0-1 score.

        Liest jeden bekannten Top-Level-Alias (CONFIDENCE_KEY_ALIASES) und nimmt
        — konservativ — den niedrigsten verwertbaren Wert. Returns None when the
        model stated nothing usable.
        """
        if not ai_response:
            return None

        resolved: list[float] = []
        for key in CONFIDENCE_KEY_ALIASES:
            if key not in ai_response:
                continue
            value = ai_response[key]

            if isinstance(value, bool):
                # "confidence: true" ist keine Sicherheitsangabe.
                logger.debug("Konfidenzfeld %s ist bool — nicht verwertbar", key)
                continue

            if isinstance(value, (int, float)):
                numeric = float(value)
                if 0.0 <= numeric <= 1.0:
                    resolved.append(numeric)
                elif 1.0 < numeric <= 100.0:
                    # Prozentangabe — nicht auf 1.0 hochklemmen
                    resolved.append(numeric / 100.0)
                else:
                    logger.debug("Konfidenzwert %r ausserhalb gueltiger Bereiche", value)
                continue

            if isinstance(value, str):
                normalized = value.strip().lower()
                if normalized in CONFIDENCE_WORD_MAP:
                    resolved.append(CONFIDENCE_WORD_MAP[normalized])
                else:
                    logger.debug("Unbekannter Konfidenzbegriff %r", value)

        if not resolved:
            return None
        return min(resolved)

    def _assess_ai_certainty(self, ai_response: dict) -> float:
        """Parse AI self-reported confidence from the response.

        The AI is instructed to include a confidence field with values like
        "hoch", "mittel", "niedrig" (Build-Quality-Prompt: "confidence_overall").
        This method converts that to a numeric score.

        Fehlende oder unverstaendliche Angaben werden nach UNTEN bewertet
        (UNKNOWN_CERTAINTY), nie nach oben — eine unlesbare Selbsteinschaetzung
        ist kein Qualitaetsbeleg.

        Returns a score between 0.0 and 1.0.
        """
        if not ai_response:
            return self.UNKNOWN_CERTAINTY

        stated = self._resolve_stated_certainty(ai_response)
        if stated is not None:
            return max(0.0, min(1.0, stated))

        return self.UNKNOWN_CERTAINTY
