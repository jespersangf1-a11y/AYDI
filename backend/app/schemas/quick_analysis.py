from datetime import datetime
from enum import Enum
from uuid import UUID
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator


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
    draft_m: Optional[float] = None
    displacement_kg: Optional[float] = None
    cabin_count: Optional[int] = None
    berth_count: Optional[int] = None
    head_count: Optional[int] = None

    # Layout hints
    cockpit_area_sqm: Optional[float] = None
    salon_area_sqm: Optional[float] = None
    pantry_type: Optional[str] = None
    helm_position: Optional[str] = None
    has_flybridge: Optional[bool] = None
    has_crew_quarters: Optional[bool] = None

    # Performance
    engine_hp: Optional[float] = None
    engine_count: Optional[int] = None
    fuel_capacity_l: Optional[float] = None
    water_capacity_l: Optional[float] = None
    sail_area_sqm: Optional[float] = None
    max_speed_kn: Optional[float] = None

    # Commercial
    price_eur: Optional[float] = None
    year: Optional[int] = None
    brand: Optional[str] = None
    model_name: Optional[str] = None

    deck_height_mm: Optional[float] = None
    storage_volume_l: Optional[float] = None

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
