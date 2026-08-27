from datetime import datetime
from enum import Enum
from uuid import UUID
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator

from app.core.boat_classes import BOAT_CLASSES, is_known
from app.schemas.schemas import FiniteNumbersMixin, require_finite

# ---------------------------------------------------------------------------
# Schranken der öffentlichen Schnellanalyse (ROB-2, ROB-3)
#
# Dieser Endpunkt ist UNAUTHENTIFIZIERT. Alles, was hier hereinkommt, geht ohne
# weitere Prüfung in `estimate_layout_from_specs()` und von dort in die
# Analysemodule. Zwei Klassen von Eingaben sind gefährlich:
#
#  * NaN/Infinity — die Module rechnen still weiter, das Ergebnis ist NaN, und
#    spätestens die JSON-Serialisierung der Response bricht (JSON kennt kein
#    NaN). ROB-2.
#  * Unbegrenzte Zähler — `cabin_count`/`head_count` erzeugen je eine Zone; die
#    Ergonomie-Analyse ist quadratisch in der Zonenzahl. Gemessen: 5.000 Kabinen
#    = 75 s in EINEM Modul, 500.000 blockieren den Event-Loop praktisch
#    unbegrenzt. ROB-3.
#
# Die Grenzen sind an den 13 Bootsklassen ausgerichtet (bis > 100 m Superyacht)
# und großzügig gewählt: 100 Kabinen und 400 Kojen liegen deutlich über allem,
# was real gebaut wird, kappen die Laufzeit aber auf Millisekunden.
# ---------------------------------------------------------------------------

MAX_CABIN_COUNT = 100
MAX_HEAD_COUNT = 100
MAX_BERTH_COUNT = 400
MAX_ENGINE_COUNT = 12


class ConfidenceLevel(str, Enum):
    measured = "measured"
    calculated = "calculated"
    estimated = "estimated"
    benchmark = "benchmark"


class PublicSpecs(FiniteNumbersMixin):
    """What someone can enter from a brochure or website."""
    # Required
    # Accepted classes: small_sail, cruising_sail, racing_sail, daysailer, motorsailer,
    # catamaran_sail, catamaran_motor, small_motor, large_motor, sport_cruiser, trawler,
    # explorer, superyacht
    # allow_inf_nan=False riegelt NaN/Infinity maschinell ab; der Validator
    # darunter liefert zusätzlich die deutsche Fehlermeldung (ROB-2).
    model_config = ConfigDict(allow_inf_nan=False)

    boat_class: str = Field(..., min_length=1, max_length=50)
    length_m: float = Field(..., gt=0, lt=200)

    # Optional — each additional field improves analysis quality
    beam_m: Optional[float] = Field(None, gt=0, le=80)
    draft_m: Optional[float] = Field(None, ge=0, le=30)
    displacement_kg: Optional[float] = Field(None, ge=0, le=50_000_000)
    cabin_count: Optional[int] = Field(None, ge=0, le=MAX_CABIN_COUNT)
    berth_count: Optional[int] = Field(None, ge=0, le=MAX_BERTH_COUNT)
    head_count: Optional[int] = Field(None, ge=0, le=MAX_HEAD_COUNT)

    # Layout hints
    cockpit_area_sqm: Optional[float] = Field(None, ge=0, le=10_000)
    salon_area_sqm: Optional[float] = Field(None, ge=0, le=10_000)
    pantry_type: Optional[str] = Field(None, max_length=50)
    helm_position: Optional[str] = Field(None, max_length=50)
    has_flybridge: Optional[bool] = None
    has_crew_quarters: Optional[bool] = None

    # Performance
    engine_hp: Optional[float] = Field(None, ge=0, le=200_000)
    engine_count: Optional[int] = Field(None, ge=0, le=MAX_ENGINE_COUNT)
    fuel_capacity_l: Optional[float] = Field(None, ge=0, le=5_000_000)
    water_capacity_l: Optional[float] = Field(None, ge=0, le=5_000_000)
    sail_area_sqm: Optional[float] = Field(None, ge=0, le=50_000)
    max_speed_kn: Optional[float] = Field(None, ge=0, le=200)

    # Commercial
    price_eur: Optional[float] = Field(None, ge=0, le=10_000_000_000)
    # Bounded: an unchecked typo ("202") would otherwise drive the buyer
    # report's age logic into an "1824 Jahre alt" analysis presented as real.
    year: Optional[int] = Field(None, ge=1900, le=2100)
    brand: Optional[str] = Field(None, max_length=100)
    model_name: Optional[str] = Field(None, max_length=100)

    deck_height_mm: Optional[float] = Field(None, gt=0, le=10_000)
    storage_volume_l: Optional[float] = Field(None, ge=0, le=5_000_000)

    @field_validator('*', mode='before')
    @classmethod
    def _reject_non_finite(cls, value, info):
        """NaN/Infinity in JEDEM Zahlenfeld abweisen — mit deutscher Meldung.

        Läuft als before-Validator, damit die verständliche Meldung vor den
        generischen ge/le-Meldungen von Pydantic greift.
        """
        return require_finite(value, info.field_name)

    @field_validator('boat_class')
    @classmethod
    def boat_class_must_be_known(cls, boat_class: str) -> str:
        """Reject unknown classes instead of silently scoring them 50.0.

        Previously any string was accepted: the analysis modules correctly
        refused with ``available: false``, but the route turned that refusal
        back into an invented result and echoed the raw input into German
        prose. Refusing at the edge removes both problems at once.
        """
        if not is_known(boat_class):
            raise ValueError(
                "Unbekannte Bootsklasse. Zulässig sind: " + ", ".join(BOAT_CLASSES)
            )
        return boat_class

    @field_validator('beam_m')
    @classmethod
    def beam_must_be_less_than_length(cls, beam_m: Optional[float], info) -> Optional[float]:
        """Validate that beam is less than length when both are provided."""
        if beam_m is not None and info.data.get('length_m'):
            if beam_m >= info.data['length_m']:
                raise ValueError(f'beam_m ({beam_m}m) must be less than length_m ({info.data["length_m"]}m)')
        return beam_m


class QuickModuleResult(BaseModel):
    available: bool
    score: Optional[float] = None
    confidence: Optional[ConfidenceLevel] = None
    key_findings: Optional[list[dict]] = None
    competitors_compared: Optional[int] = None
    strengths: Optional[list[str]] = None
    weaknesses: Optional[list[str]] = None
    reason: Optional[str] = None  # why unavailable


class QuickAnalysisResponse(BaseModel):
    id: UUID
    analysis_level: str = "public_specs"
    confidence: ConfidenceLevel = ConfidenceLevel.estimated
    specs_provided: int
    specs_inferred: int
    overall_assessment: dict  # {score, confidence, summary}
    modules: dict[str, QuickModuleResult]
    upgrade_prompt: dict  # {message, additional_modules}
    specs_used: dict  # the input specs for reference
    created_at: datetime
    # Pillar 2 (Kaufberatung): filled when the user supplied boat identity
    # (brand / model_name / year); None otherwise.
    buyer_insights: Optional[dict] = None

    model_config = ConfigDict(from_attributes=True)


class BuyerInsightsResponse(BaseModel):
    """Boat-specific buyer report (pillar 2 — Kaufberatung, Level 1/public).

    Sections keep their own confidence labels: manufacturer/community data is
    "documented" (curated knowledge / aggregated reports), age expectations
    are "estimated" (statistical lifespans, not findings on the actual boat).
    """
    available: bool
    reason: Optional[str] = None
    boat_identity: Optional[dict] = None
    manufacturer: Optional[dict] = None
    age_expectations: Optional[dict] = None
    community: Optional[dict] = None
    summary_de: Optional[str] = None
    disclaimer_de: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
