"""Confidence gatekeeper for visual analysis results.

Ensures only reliable assessments reach users. Evaluates image quality,
content relevance, and AI self-reported certainty to determine whether
a visual analysis result is trustworthy enough to present.
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

    @property
    def is_usable(self) -> bool:
        """Whether this assessment is reliable enough to show to the user."""
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

    def evaluate(self, ai_response: dict, image_metadata: dict) -> ConfidenceAssessment:
        """Evaluate the confidence of an AI visual analysis result.

        Args:
            ai_response: Parsed JSON response from the AI vision model.
            image_metadata: Dict with keys like width, height, file_size_bytes.

        Returns:
            ConfidenceAssessment with level, factors, and component scores.
        """
        factors: list[str] = []

        image_quality = self._assess_image_quality(image_metadata)
        if image_quality < self.MIN_IMAGE_QUALITY:
            factors.append(f"Bildqualitaet niedrig ({image_quality:.2f})")

        content_relevance = self._assess_content_relevance(ai_response)
        if content_relevance < self.MIN_CONTENT_RELEVANCE:
            factors.append(f"Inhaltliche Relevanz niedrig ({content_relevance:.2f})")

        assessment_certainty = self._assess_ai_certainty(ai_response)
        if assessment_certainty < self.MIN_ASSESSMENT_CERTAINTY:
            factors.append(f"KI-Sicherheit niedrig ({assessment_certainty:.2f})")

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

        if not factors:
            factors.append("Alle Qualitaetskriterien erfuellt")

        return ConfidenceAssessment(
            level=level,
            factors=factors,
            image_quality=round(image_quality, 3),
            content_relevance=round(content_relevance, 3),
            assessment_certainty=round(assessment_certainty, 3),
        )

    def _assess_image_quality(self, metadata: dict) -> float:
        """Assess image quality from resolution and file size.

        Returns a score between 0.0 and 1.0.
        """
        width = metadata.get("width", 0)
        height = metadata.get("height", 0)
        file_size = metadata.get("file_size_bytes", 0)

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
        return 0.7 * res_score + 0.3 * size_score

    def _assess_content_relevance(self, ai_response: dict) -> float:
        """Assess whether the AI found meaningful yacht-related content.

        Returns a score between 0.0 and 1.0.
        """
        if not ai_response:
            return 0.0

        # Check if the AI explicitly flagged content as not assessable
        assessable = ai_response.get("assessable", True)
        if assessable is False:
            return 0.2

        # Count cannot_assess items — more items = less relevance
        cannot_assess = ai_response.get("cannot_assess", [])
        if isinstance(cannot_assess, list) and len(cannot_assess) > 0:
            # Each cannot_assess item reduces relevance
            penalty = min(len(cannot_assess) * 0.1, 0.5)
            base = 0.8 - penalty
        else:
            base = 0.9

        # Check if findings exist
        findings = ai_response.get("findings", [])
        if isinstance(findings, list) and len(findings) > 0:
            base = min(1.0, base + 0.1)
        elif isinstance(findings, dict) and len(findings) > 0:
            base = min(1.0, base + 0.1)

        return max(0.0, base)

    def _assess_ai_certainty(self, ai_response: dict) -> float:
        """Parse AI self-reported confidence from the response.

        The AI is instructed to include a confidence field with values
        like 'hoch', 'mittel', 'niedrig'. This method converts that
        to a numeric score.

        Returns a score between 0.0 and 1.0.
        """
        if not ai_response:
            return 0.3

        confidence_raw = ai_response.get("confidence", "")

        if isinstance(confidence_raw, (int, float)):
            return max(0.0, min(1.0, float(confidence_raw)))

        if isinstance(confidence_raw, str):
            normalized = confidence_raw.strip().lower()
            if normalized in CONFIDENCE_WORD_MAP:
                return CONFIDENCE_WORD_MAP[normalized]

        # If no confidence field, infer from response quality
        has_score = any(
            key in ai_response
            for key in ("spatial_score", "overall_quality_score", "material_score",
                        "emotional_score", "exterior_score", "helm_score")
        )
        if has_score:
            return 0.6  # AI produced scores, moderate confidence assumed

        return 0.3
