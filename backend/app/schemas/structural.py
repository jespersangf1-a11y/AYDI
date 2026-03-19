# backend/app/schemas/structural.py
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class StructuralItemCreate(BaseModel):
    name: str
    item_type: str
    zone_name: str | None = None
    weight_kg: float
    position_x_mm: float | None = None
    position_y_mm: float | None = None
    position_z_mm: float | None = None
    dimensions: dict | None = None
    properties: dict | None = None


class StructuralItemUpdate(BaseModel):
    name: str | None = None
    item_type: str | None = None
    zone_name: str | None = None
    weight_kg: float | None = None
    position_x_mm: float | None = None
    position_y_mm: float | None = None
    position_z_mm: float | None = None
    dimensions: dict | None = None
    properties: dict | None = None


class StructuralItemResponse(BaseModel):
    id: UUID
    layout_id: UUID
    name: str
    item_type: str
    zone_name: str | None
    weight_kg: float
    position_x_mm: float | None
    position_y_mm: float | None
    position_z_mm: float | None
    dimensions: dict | None
    properties: dict | None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
