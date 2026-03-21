# backend/app/schemas/schemas.py
from datetime import date, datetime
from enum import Enum
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class BoatClass(str, Enum):
    small_sail = "small_sail"
    cruising_sail = "cruising_sail"
    racing_sail = "racing_sail"
    daysailer = "daysailer"
    motorsailer = "motorsailer"
    catamaran_sail = "catamaran_sail"
    catamaran_motor = "catamaran_motor"
    small_motor = "small_motor"
    large_motor = "large_motor"
    sport_cruiser = "sport_cruiser"
    trawler = "trawler"
    explorer = "explorer"
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
    height_mm: float | None = None
    is_crew_area: bool = False
    is_guest_area: bool = False
    visibility_angle: float | None = None
    properties: dict | None = None


class PassageData(BaseModel):
    from_zone: str
    to_zone: str
    width_mm: float
    length_mm: float | None = None
    points: list[list[float]] | None = None
    is_primary: bool = True


# Pydantic v2 validation schemas for zones and passages
class ZoneSchema(BaseModel):
    name: str
    zone_type: str
    area_m2: float | None = None
    polygon: list | None = None
    properties: dict | None = None

    model_config = ConfigDict(from_attributes=True)


class PassageSchema(BaseModel):
    from_zone: str
    to_zone: str
    width_mm: float
    type: str
    properties: dict | None = None

    model_config = ConfigDict(from_attributes=True)


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
    config_overrides: dict | None = None


class FullAnalysisRequest(BaseModel):
    """Request body for running all analysis modules on a layout."""
    layout_id: UUID
    config_overrides: dict | None = None


class WarningData(BaseModel):
    code: str | None = None
    severity: str
    message: str
    location: str | None = None
    value: float | None = None
    threshold: float | None = None
    suggestion: str
    norm: str | None = None


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


# Report schemas
class ReportRequest(BaseModel):
    layout_id: UUID
    report_type: str = "full"  # full, summary, executive


class ReportResponse(BaseModel):
    id: UUID
    project_id: UUID
    layout_id: UUID
    report_type: str
    report_data: dict
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


# CAD Import (STEP/IGES)
class DeckInfo(BaseModel):
    z_mm: float
    name: str
    face_count: int = 0


class CadImportResponse(BaseModel):
    zones: list[ZoneData]
    passages: list[PassageData]
    warnings: list[str]
    decks: list[DeckInfo] = []


# Error
class ErrorResponse(BaseModel):
    detail: str
    errors: list[str] | None = None


# Community Intelligence schemas
class CommunityIssue(BaseModel):
    category: str
    zone_type: str
    description: str
    severity: str
    boat_age_months: int | None = None


class CommunityPositive(BaseModel):
    category: str
    zone_type: str
    description: str


class CommunityReportCreate(BaseModel):
    source_forum: str
    source_url: str | None = None
    source_date: date | None = None
    boat_manufacturer: str
    boat_model: str | None = None
    boat_year: int | None = None
    hull_material: str | None = None
    hull_construction: str | None = None
    propulsion: str | None = None
    issues: list[CommunityIssue] = []
    positives: list[CommunityPositive] = []
    reliability: float
    raw_text: str | None = None


class CommunityReportResponse(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime | None = None
    source_forum: str
    source_url: str | None = None
    source_date: date | None = None
    boat_manufacturer: str
    boat_model: str | None = None
    boat_year: int | None = None
    hull_material: str | None = None
    hull_construction: str | None = None
    propulsion: str | None = None
    issues: list[dict] = []
    positives: list[dict] = []
    reliability: float
    raw_text: str | None = None
    model_config = ConfigDict(from_attributes=True)


class CommunityPatternResponse(BaseModel):
    id: int
    created_at: datetime
    manufacturer: str | None = None
    boat_model: str | None = None
    issue_category: str
    zone_type: str | None = None
    description: str
    report_count: int
    severity_mode: str
    typical_onset_years: float | None = None
    materials_involved: list[str] | None = None
    construction_methods_involved: list[str] | None = None
    confidence: float
    source_report_ids: list[int]
    is_positive: bool
    model_config = ConfigDict(from_attributes=True)


class AggregationResultResponse(BaseModel):
    patterns_created: int
    reports_processed: int
    reports_skipped: int
    groups_below_threshold: int
