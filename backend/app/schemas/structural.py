# backend/app/schemas/structural.py
from datetime import datetime
from typing import Literal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


# Closed type set: the analysis' tank/heavy heuristics key on these values;
# free strings would silently bypass them.
StructuralItemType = Literal[
    "engine", "ballast", "fuel_tank", "water_tank",
    "battery", "anchor_chain", "rigging", "other",
]

# Positions are millimetres within/near the boat frame; weights must be
# positive finite kg — negative/NaN values would subtract mass from the CG
# model or corrupt persisted metrics.
_WEIGHT_FIELD = Field(gt=0, le=100_000, allow_inf_nan=False)
_POSITION_FIELD = Field(default=None, ge=-200_000, le=200_000, allow_inf_nan=False)


class StructuralItemCreate(BaseModel):
    name: str = Field(min_length=1, max_length=200)
    item_type: StructuralItemType
    zone_name: str | None = Field(default=None, max_length=100)
    weight_kg: float = _WEIGHT_FIELD
    position_x_mm: float | None = _POSITION_FIELD
    position_y_mm: float | None = _POSITION_FIELD
    position_z_mm: float | None = _POSITION_FIELD
    dimensions: dict | None = None
    properties: dict | None = None


class StructuralItemUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=200)
    item_type: StructuralItemType | None = None
    zone_name: str | None = Field(default=None, max_length=100)
    weight_kg: float | None = Field(
        default=None, gt=0, le=100_000, allow_inf_nan=False
    )
    position_x_mm: float | None = _POSITION_FIELD
    position_y_mm: float | None = _POSITION_FIELD
    position_z_mm: float | None = _POSITION_FIELD
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
