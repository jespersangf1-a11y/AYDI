# backend/app/schemas/costs.py
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class CostItemCreate(BaseModel):
    category: str = Field(..., min_length=1, max_length=100)
    subcategory: str | None = Field(None, max_length=100)
    description: str | None = Field(None, max_length=1000)
    quantity: float = Field(1.0, ge=0)
    unit: str = Field("piece", min_length=1, max_length=50)
    unit_cost_eur: float = Field(..., ge=0)
    total_cost_eur: float = Field(..., ge=0)
    zone_name: str | None = Field(None, max_length=100)
    source: str = Field("estimate", max_length=50)
    notes: str | None = Field(None, max_length=2000)


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
