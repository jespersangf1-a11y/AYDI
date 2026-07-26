# backend/app/schemas/versions.py
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from app.schemas.schemas import PassageData, ZoneData


class LayoutVersionCreate(BaseModel):
    # Typed snapshots: restore sends them back through PATCH /layouts, which
    # validates list[ZoneData] — accepting arbitrary lists here would create
    # versions the API can never restore by its own contract.
    zones_snapshot: list[ZoneData] | None = None
    passages_snapshot: list[PassageData] | None = None
    change_summary: str | None = None
    # NOTE: no changed_by field — the audit trail is server-authoritative
    # (set from the authenticated user; client-supplied values allowed
    # spoofing the history in shared projects).
    parent_version_id: UUID | None = None
    tags: list | None = None


class LayoutVersionResponse(BaseModel):
    id: UUID
    layout_id: UUID
    version_number: int
    parent_version_id: UUID | None
    zones_snapshot: list | None
    passages_snapshot: list | None
    layout_meta_snapshot: dict | None = None
    change_summary: str | None
    changed_by: str | None
    tags: list | None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
