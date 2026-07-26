# backend/app/schemas/materials.py
from datetime import datetime
from typing import Literal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class MaterialCreate(BaseModel):
    name: str
    category: str
    subcategory: str
    manufacturer: str | None = None
    properties: dict | None = None
    cost_per_unit: float = 0.0
    cost_unit: str = "sqm"
    lifespan_years: float | None = None
    maintenance_interval_months: int | None = None
    maintenance_cost_factor: float = 0.0
    known_issues: list | None = None
    alternatives: list[str] | None = None


class MaterialUpdate(BaseModel):
    name: str | None = None
    category: str | None = None
    subcategory: str | None = None
    manufacturer: str | None = None
    properties: dict | None = None
    cost_per_unit: float | None = None
    cost_unit: str | None = None
    lifespan_years: float | None = None
    maintenance_interval_months: int | None = None
    maintenance_cost_factor: float | None = None
    known_issues: list | None = None
    alternatives: list[str] | None = None


class MaterialResponse(BaseModel):
    id: UUID
    name: str
    category: str
    subcategory: str
    manufacturer: str | None
    properties: dict | None
    cost_per_unit: float
    cost_unit: str
    lifespan_years: float | None
    maintenance_interval_months: int | None
    maintenance_cost_factor: float
    known_issues: list | None
    alternatives: list[str] | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ZoneMaterialCreate(BaseModel):
    zone_name: str = Field(..., min_length=1, max_length=100)
    # Closed set: free strings would silently bypass the materials analysis'
    # surface handling; area must be positive — negative areas would let an
    # API client subtract lifecycle cost/weight and inflate the score.
    surface_type: Literal[
        "floor", "wall", "ceiling", "countertop", "upholstery", "deck"
    ]
    material_id: UUID
    area_sqm: float = Field(..., gt=0, le=10000)
    notes: str | None = Field(None, max_length=1000)


class ZoneMaterialResponse(BaseModel):
    id: UUID
    layout_id: UUID
    zone_name: str
    surface_type: str
    material_id: UUID
    area_sqm: float
    notes: str | None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
