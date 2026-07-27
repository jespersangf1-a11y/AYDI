# backend/app/schemas/schemas.py
from datetime import date, datetime
from enum import Enum
from typing import Literal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field


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
    name: str = Field(..., min_length=1, max_length=100)
    zone_type: str = Field(..., min_length=1, max_length=50)
    polygon: list[list[float]]
    height_mm: float | None = Field(None, ge=0, le=10000)
    is_crew_area: bool = False
    is_guest_area: bool = False
    visibility_angle: float | None = Field(None, ge=0, le=360)
    properties: dict | None = None


class PassageData(BaseModel):
    from_zone: str
    to_zone: str
    width_mm: float
    length_mm: float | None = None
    points: list[list[float]] | None = None
    is_primary: bool = True
    # Passage-level attributes (e.g. sill_height_mm for the CE companionway-sill
    # check). Without this, Pydantic silently dropped the field and
    # CE_NO_SILL_DATA fired permanently — the check was unreachable via the API.
    properties: dict | None = None


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
    name: str = Field(..., min_length=1, max_length=200)
    description: str | None = Field(None, max_length=2000)
    boat_class: BoatClass
    length_m: float = Field(..., gt=0, le=300, description="Bootslänge in Metern")
    beam_m: float = Field(..., gt=0, le=50, description="Bootsbreite in Metern")


class ProjectUpdate(BaseModel):
    name: str | None = Field(None, min_length=1, max_length=200)
    description: str | None = Field(None, max_length=2000)
    boat_class: BoatClass | None = None
    length_m: float | None = Field(None, gt=0, le=300)
    beam_m: float | None = Field(None, gt=0, le=50)
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
    # Organization ownership (pillar 4, stage 2), None for private projects.
    org_id: UUID | None = None
    # Caller's relationship to the project: "owner" / "editor" / "viewer".
    # Drives the "geteilt"-badge and owner-only UI (sharing dialog).
    access_role: str | None = None

    model_config = ConfigDict(from_attributes=True)


# Project sharing (pillar 4, stage 1)
class ProjectMemberCreate(BaseModel):
    email: EmailStr
    role: Literal["viewer", "editor"] = "viewer"


class ProjectMemberRoleUpdate(BaseModel):
    role: Literal["viewer", "editor"]


class ProjectMemberResponse(BaseModel):
    user_id: UUID
    email: str
    full_name: str
    role: str  # owner, editor, viewer

    model_config = ConfigDict(from_attributes=True)


# Project org attachment (pillar 4, stage 2)
class ProjectOrgUpdate(BaseModel):
    # None = detach the project back to private
    org_id: UUID | None = None


# ---------------------------------------------------------------------------
# Organizations (pillar 4, stage 2)
# ---------------------------------------------------------------------------

class OrganizationCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)


class OrganizationUpdate(BaseModel):
    # Rename only. tier is deliberately NOT here — it is platform-admin-only
    # (self-service tier changes would be a privilege escalation).
    name: str = Field(..., min_length=1, max_length=200)


class OrganizationResponse(BaseModel):
    id: UUID
    name: str
    tier: str
    created_at: datetime
    # Caller's org_role ("owner"/"admin"/"member") — for UI gating.
    org_role: str | None = None
    member_count: int | None = None

    model_config = ConfigDict(from_attributes=True)


class OrgMemberResponse(BaseModel):
    user_id: UUID
    email: str
    full_name: str
    org_role: str  # owner, admin, member

    model_config = ConfigDict(from_attributes=True)


class OrgMemberRoleUpdate(BaseModel):
    org_role: Literal["owner", "admin", "member"]


class OrgTierUpdate(BaseModel):
    # Platform-admin-only endpoint payload.
    tier: Literal["free", "pro", "enterprise"]


# ---------------------------------------------------------------------------
# Invitations (pillar 4, stage 2)
# ---------------------------------------------------------------------------

class ProjectInvitationCreate(BaseModel):
    email: EmailStr
    role: Literal["viewer", "editor"] = "viewer"


class OrgInvitationCreate(BaseModel):
    email: EmailStr
    role: Literal["member", "admin"] = "member"


class InvitationResponse(BaseModel):
    id: UUID
    email: str
    role: str
    status: str
    scope: str  # "project" | "org"
    project_id: UUID | None = None
    organization_id: UUID | None = None
    # Human-readable target name, filled by the endpoint (project/org name).
    target_name: str | None = None
    invited_by_email: str | None = None
    created_at: datetime
    expires_at: datetime

    model_config = ConfigDict(from_attributes=True)


# Layout schemas
class LayoutCreate(BaseModel):
    name: str
    version: str = "v1.0"
    zones: list[ZoneData]
    passages: list[PassageData]
    deck_height_mm: int = 2100


class LayoutUpdate(BaseModel):
    """Partial layout update (pillar 3: owner refit loop).

    Every applied update auto-snapshots the PREVIOUS state as a LayoutVersion,
    so edits are never destructive and before/after comparison always works.
    """
    name: str | None = Field(None, min_length=1, max_length=200)
    version: str | None = Field(None, min_length=1, max_length=50)
    # min_length=1: emptying a layout is not a refit operation — a bare
    # zones=[] would only ever appear by accident (e.g. missing snapshot)
    # and every following analysis would fail on empty geometry.
    zones: list[ZoneData] | None = Field(None, min_length=1)
    passages: list[PassageData] | None = None
    deck_height_mm: int | None = Field(None, ge=1000, le=5000)
    # Zone renames performed in this update ({old_name: new_name}) — the
    # server cascades them to ZoneMaterial/StructuralItem/CostItem rows,
    # which reference zones BY NAME and would otherwise be orphaned.
    zone_renames: dict[str, str] | None = None
    # Recorded on the auto-created version snapshot
    change_summary: str | None = Field(None, max_length=500)


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
    source_forum: str = Field(..., min_length=1, max_length=100)
    source_url: str | None = Field(None, max_length=2000)
    source_date: date | None = None
    boat_manufacturer: str = Field(..., min_length=1, max_length=200)
    boat_model: str | None = Field(None, max_length=200)
    boat_year: int | None = Field(None, ge=1900, le=2100)
    hull_material: str | None = Field(None, max_length=100)
    hull_construction: str | None = Field(None, max_length=100)
    propulsion: str | None = Field(None, max_length=100)
    issues: list[CommunityIssue] = []
    positives: list[CommunityPositive] = []
    reliability: float = Field(..., ge=0.0, le=1.0)
    raw_text: str | None = Field(None, max_length=50000)


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
