# backend/app/schemas/schemas.py
from datetime import datetime
from enum import Enum
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class BoatClass(str, Enum):
    small_sail = "small_sail"
    cruising_sail = "cruising_sail"
    large_motor = "large_motor"
    superyacht = "superyacht"


class ProjectStatus(str, Enum):
    draft = "draft"
    active = "active"
    review = "review"
    archived = "archived"


# Zone / Passage data (JSON within Layout)
class ZoneData(BaseModel):
    name: str
    zone_type: str
    polygon: list[list[float]]
    is_crew_area: bool = False
    is_guest_area: bool = False
    visibility_angle: float | None = None


class PassageData(BaseModel):
    from_zone: str
    to_zone: str
    width_mm: float
    is_primary: bool = True


# Project schemas
class ProjectCreate(BaseModel):
    name: str
    description: str | None = None
    boat_class: BoatClass
    length_m: float
    beam_m: float


class ProjectUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    boat_class: BoatClass | None = None
    length_m: float | None = None
    beam_m: float | None = None
    status: ProjectStatus | None = None


class ProjectResponse(BaseModel):
    id: UUID
    name: str
    description: str | None
    boat_class: BoatClass
    length_m: float
    beam_m: float
    status: ProjectStatus
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


# Layout schemas
class LayoutCreate(BaseModel):
    name: str
    version: str = "v1.0"
    zones: list[ZoneData]
    passages: list[PassageData]
    deck_height_mm: int = 2100


class LayoutResponse(BaseModel):
    id: UUID
    project_id: UUID
    name: str
    version: str
    file_path: str | None
    file_type: str | None
    zones: list[ZoneData]
    passages: list[PassageData]
    deck_height_mm: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


# Analysis schemas
class AnalysisRequest(BaseModel):
    layout_id: UUID
    module: str


class WarningData(BaseModel):
    severity: str
    message: str
    suggestion: str


class AnalysisResponse(BaseModel):
    id: UUID
    project_id: UUID
    layout_id: UUID
    module: str
    overall_score: float
    sub_scores: dict[str, float]
    warnings: list[WarningData]
    suggestions: list[str]
    metrics: dict
    config_used: dict
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


# DXF Import
class DxfImportResponse(BaseModel):
    zones: list[ZoneData]
    passages: list[PassageData]
    warnings: list[str]


# Error
class ErrorResponse(BaseModel):
    detail: str
    errors: list[str] | None = None
