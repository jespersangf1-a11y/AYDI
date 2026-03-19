# backend/app/schemas/versions.py
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class LayoutVersionCreate(BaseModel):
    zones_snapshot: list | None = None
    passages_snapshot: list | None = None
    change_summary: str | None = None
    changed_by: str | None = None
    parent_version_id: UUID | None = None
    tags: list | None = None


class LayoutVersionResponse(BaseModel):
    id: UUID
    layout_id: UUID
    version_number: int
    parent_version_id: UUID | None
    zones_snapshot: list | None
    passages_snapshot: list | None
    change_summary: str | None
    changed_by: str | None
    tags: list | None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
