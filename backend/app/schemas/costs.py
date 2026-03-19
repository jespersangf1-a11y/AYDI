# backend/app/schemas/costs.py
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class CostItemCreate(BaseModel):
    category: str
    subcategory: str | None = None
    description: str | None = None
    quantity: float = 1.0
    unit: str = "piece"
    unit_cost_eur: float
    total_cost_eur: float
    zone_name: str | None = None
    source: str = "estimate"
    notes: str | None = None


class CostItemUpdate(BaseModel):
    category: str | None = None
    subcategory: str | None = None
    description: str | None = None
    quantity: float | None = None
    unit: str | None = None
    unit_cost_eur: float | None = None
    total_cost_eur: float | None = None
    zone_name: str | None = None
    source: str | None = None
    notes: str | None = None


class CostItemResponse(BaseModel):
    id: UUID
    layout_id: UUID
    category: str
    subcategory: str | None
    description: str | None
    quantity: float
    unit: str
    unit_cost_eur: float
    total_cost_eur: float
    zone_name: str | None
    source: str
    notes: str | None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
