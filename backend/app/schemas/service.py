# backend/app/schemas/service.py
from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator

# Severity drives the analysis weighting — normalise German/English spellings to
# a small closed set and reject anything else (L-8).
_SEVERITY_MAP = {
    "critical": "critical", "high": "high", "medium": "medium", "low": "low", "none": "low",
    "kritisch": "critical", "hoch": "high", "mittel": "medium", "gering": "low", "niedrig": "low",
}
# Generous superset of the report types used across the UI, analysis and tests.
_REPORT_TYPES = {
    "repair", "inspection", "maintenance", "warranty", "refit",
    "complaint", "feedback", "incident", "service",
}


def _normalize_severity(v):
    if v is None:
        return v
    key = str(v).strip().lower()
    if key not in _SEVERITY_MAP:
        raise ValueError(f"Ungültiger Schweregrad: {v!r}. Erlaubt: critical, high, medium, low.")
    return _SEVERITY_MAP[key]


def _validate_report_type(v):
    if v is None:
        return v
    key = str(v).strip().lower()
    if key not in _REPORT_TYPES:
        raise ValueError(
            f"Ungültiger Berichtstyp: {v!r}. Erlaubt: {', '.join(sorted(_REPORT_TYPES))}."
        )
    return key


def _validate_materials(v):
    if v is None:
        return v
    if not isinstance(v, list) or not all(isinstance(m, str) for m in v):
        raise ValueError("materials_involved muss eine Liste von Zeichenketten sein.")
    return v


class ServiceReportCreate(BaseModel):
    report_type: str
    category: str = Field(..., min_length=1, max_length=100)
    zone_type: str | None = Field(None, max_length=50)
    description: str = Field(..., min_length=1, max_length=20000)
    severity: str = "medium"
    root_cause: str | None = Field(None, max_length=20000)
    resolution: str | None = Field(None, max_length=20000)
    cost_eur: float | None = Field(None, ge=0, le=1_000_000_000)
    hours_labor: float | None = Field(None, ge=0, le=100_000)
    boat_age_months: int | None = Field(None, ge=0, le=1200)
    materials_involved: list | None = None
    reported_by: str | None = Field(None, max_length=255)
    reported_at: date | None = None
    project_id: UUID | None = None
    boat_class: str | None = Field(None, max_length=50)
    model_name: str | None = Field(None, max_length=255)
    metadata_extra: dict | None = None

    _norm_severity = field_validator("severity")(_normalize_severity)
    _val_report_type = field_validator("report_type")(_validate_report_type)
    _val_materials = field_validator("materials_involved")(_validate_materials)


class ServiceReportUpdate(BaseModel):
    report_type: str | None = None
    category: str | None = Field(None, min_length=1, max_length=100)
    zone_type: str | None = Field(None, max_length=50)
    description: str | None = Field(None, min_length=1, max_length=20000)
    severity: str | None = None
    root_cause: str | None = Field(None, max_length=20000)
    resolution: str | None = Field(None, max_length=20000)
    cost_eur: float | None = Field(None, ge=0, le=1_000_000_000)
    hours_labor: float | None = Field(None, ge=0, le=100_000)
    boat_age_months: int | None = Field(None, ge=0, le=1200)
    materials_involved: list | None = None
    reported_by: str | None = Field(None, max_length=255)
    reported_at: date | None = None
    project_id: UUID | None = None
    boat_class: str | None = Field(None, max_length=50)
    model_name: str | None = Field(None, max_length=255)
    metadata_extra: dict | None = None

    _norm_severity = field_validator("severity")(_normalize_severity)
    _val_report_type = field_validator("report_type")(_validate_report_type)
    _val_materials = field_validator("materials_involved")(_validate_materials)


class ServiceReportResponse(BaseModel):
    id: UUID
    report_type: str
    category: str
    zone_type: str | None
    description: str
    severity: str
    root_cause: str | None
    resolution: str | None
    cost_eur: float | None
    hours_labor: float | None
    boat_age_months: int | None
    materials_involved: list | None
    reported_by: str | None
    reported_at: date | None
    project_id: UUID | None
    boat_class: str | None
    model_name: str | None
    metadata_extra: dict | None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
