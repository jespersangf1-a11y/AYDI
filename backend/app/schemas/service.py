# backend/app/schemas/service.py
from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ServiceReportCreate(BaseModel):
    report_type: str
    category: str
    zone_type: str | None = None
    description: str
    severity: str = "medium"
    root_cause: str | None = None
    resolution: str | None = None
    cost_eur: float | None = None
    hours_labor: float | None = None
    boat_age_months: int | None = None
    materials_involved: list | None = None
    reported_by: str | None = None
    reported_at: date | None = None
    project_id: UUID | None = None
    boat_class: str | None = None
    model_name: str | None = None
    metadata_extra: dict | None = None


class ServiceReportUpdate(BaseModel):
    report_type: str | None = None
    category: str | None = None
    zone_type: str | None = None
    description: str | None = None
    severity: str | None = None
    root_cause: str | None = None
    resolution: str | None = None
    cost_eur: float | None = None
    hours_labor: float | None = None
    boat_age_months: int | None = None
    materials_involved: list | None = None
    reported_by: str | None = None
    reported_at: date | None = None
    project_id: UUID | None = None
    boat_class: str | None = None
    model_name: str | None = None
    metadata_extra: dict | None = None


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
