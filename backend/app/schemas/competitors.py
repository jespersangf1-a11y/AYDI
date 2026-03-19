# backend/app/schemas/competitors.py
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


# --- Competitor models ---


class CompetitorCreate(BaseModel):
    brand: str
    model_name: str
    boat_class: str
    length_m: float | None = None
    beam_m: float | None = None
    year: int | None = None
    price_range_eur: dict | None = None
    key_metrics: dict | None = None
    source: str | None = None
    source_url: str | None = None
    images: list[str] | None = None
    notes: str | None = None


class CompetitorUpdate(BaseModel):
    brand: str | None = None
    model_name: str | None = None
    boat_class: str | None = None
    length_m: float | None = None
    beam_m: float | None = None
    year: int | None = None
    price_range_eur: dict | None = None
    key_metrics: dict | None = None
    source: str | None = None
    source_url: str | None = None
    images: list[str] | None = None
    notes: str | None = None


class CompetitorResponse(BaseModel):
    id: UUID
    brand: str
    model_name: str
    boat_class: str
    length_m: float | None
    beam_m: float | None
    year: int | None
    price_range_eur: dict | None
    key_metrics: dict | None
    source: str | None
    source_url: str | None
    images: list | None
    notes: str | None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


# --- Brand reference models ---


class BrandReferenceCreate(BaseModel):
    shipyard_id: str | None = None
    model_name: str
    model_year: int | None = None
    boat_class: str
    layout_id: UUID | None = None
    features: dict | None = None
    images: list[str] | None = None
    notes: str | None = None


class BrandReferenceResponse(BaseModel):
    id: UUID
    shipyard_id: str | None
    model_name: str
    model_year: int | None
    boat_class: str
    layout_id: UUID | None
    features: dict | None
    images: list | None
    notes: str | None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
