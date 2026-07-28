from datetime import datetime
from enum import Enum
from uuid import UUID
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator

from app.core.boat_classes import BOAT_CLASSES, is_known


class ConfidenceLevel(str, Enum):
    measured = "measured"
    calculated = "calculated"
    estimated = "estimated"
    benchmark = "benchmark"


class PublicSpecs(BaseModel):
    """What someone can enter from a brochure or website."""
    # Required
    # Accepted classes: small_sail, cruising_sail, racing_sail, daysailer, motorsailer,
    # catamaran_sail, catamaran_motor, small_motor, large_motor, sport_cruiser, trawler,
    # explorer, superyacht
    boat_class: str
    length_m: float = Field(..., gt=0, lt=200)

    # Optional — each additional field improves analysis quality
    beam_m: Optional[float] = Field(None, gt=0, lt=200)
    draft_m: Optional[float] = Field(None, gt=0, le=20)
    displacement_kg: Optional[float] = Field(None, gt=0, le=5_000_000)
    cabin_count: Optional[int] = Field(None, ge=0, le=60)
    berth_count: Optional[int] = Field(None, ge=0, le=200)
    head_count: Optional[int] = Field(None, ge=0, le=60)

    # Layout hints
    cockpit_area_sqm: Optional[float] = Field(None, gt=0, le=2000)
    salon_area_sqm: Optional[float] = Field(None, gt=0, le=2000)
    pantry_type: Optional[str] = Field(None, max_length=60)
    helm_position: Optional[str] = Field(None, max_length=60)
    has_flybridge: Optional[bool] = None
    has_crew_quarters: Optional[bool] = None

    # Performance
    engine_hp: Optional[float] = Field(None, ge=0, le=50_000)
    engine_count: Optional[int] = Field(None, ge=0, le=12)
    fuel_capacity_l: Optional[float] = Field(None, ge=0, le=1_000_000)
    water_capacity_l: Optional[float] = Field(None, ge=0, le=1_000_000)
    sail_area_sqm: Optional[float] = Field(None, ge=0, le=20_000)
    max_speed_kn: Optional[float] = Field(None, ge=0, le=150)

    # Commercial
    price_eur: Optional[float] = Field(None, ge=0, le=1_000_000_000)
    year: Optional[int] = Field(None, ge=1850, le=2100)
    brand: Optional[str] = Field(None, max_length=120)
    model_name: Optional[str] = Field(None, max_length=120)

    deck_height_mm: Optional[float] = Field(None, gt=0, le=10_000)
    storage_volume_l: Optional[float] = Field(None, ge=0, le=1_000_000)

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

    model_config = ConfigDict(from_attributes=True)
