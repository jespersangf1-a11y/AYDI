"""Real-time collaboration endpoints."""
import logging
from datetime import datetime, timezone
from uuid import UUID

from fastapi import APIRouter, Depends, Query, WebSocket, WebSocketDisconnect
from sqlalchemy import select

from app.core.permissions import authenticate_websocket, effective_tier, require_role
from app.core.subscription import Feature, has_feature
from app.core.websocket import manager
from app.db.database import async_session
from app.models.models import Layout, OrganizationMember, Project, ProjectMember, User

logger = logging.getLogger(__name__)

router = APIRouter(tags=["collaboration"])


async def _layout_access_role(db, user_id, layout_id: str) -> str | None:
    """'owner' / member role / None for the layout's project.

    Pillar 4, stage 1: the owner-only gate made the multi-participant
    WebSocket unusable — a second team member could never join. Any member
    role may JOIN the session; the role decides write semantics inside the
    channel (viewers must not broadcast edits).
    """
    try:
        lid = UUID(str(layout_id))
    except (ValueError, TypeError):
        return None
    row = await db.execute(
        select(Layout.id, Project.id, Project.user_id, Project.org_id)
        .join(Project, Layout.project_id == Project.id)
        .where(Layout.id == lid)
    )
    hit = row.first()
    if hit is None:
        return None
    _, project_id, owner_id, org_id = hit
    if owner_id == user_id:
        return "owner"

    # Explicit project membership (stage 1) OR org-derived role (stage 2) —
    # highest wins. viewer < editor < owner.
    order = {"viewer": 0, "editor": 1, "owner": 2}
    best = -1
    member = await db.execute(
        select(ProjectMember.role).where(
            ProjectMember.project_id == project_id,
            ProjectMember.user_id == user_id,
        )
    )
    prole = member.scalar_one_or_none()
    if prole is not None:
        best = max(best, order.get(prole, -1))

    if org_id is not None:
        org = await db.execute(
            select(OrganizationMember.org_role).where(
                OrganizationMember.organization_id == org_id,
                OrganizationMember.user_id == user_id,
            )
        )
        org_role = org.scalar_one_or_none()
        if org_role is not None:
            mapped = "owner" if org_role in ("owner", "admin") else "editor"
            best = max(best, order[mapped])

    if best < 0:
        return None
    return {0: "viewer", 1: "editor", 2: "owner"}[best]


@router.websocket("/ws/collaborate/{layout_id}")
async def collaborate_websocket(
    websocket: WebSocket,
    layout_id: str,
):
    """WebSocket endpoint for real-time layout collaboration.

    Requires authentication via ?token=<JWT> query parameter.
    """
    # Authenticate AND authorize before accepting the connection. Authentication
    # alone is not enough: without the access check any logged-in user could
    # join a stranger's private layout and read/inject live design data.
    async with async_session() as db:
        user = await authenticate_websocket(websocket, db)
        access_role = (
            await _layout_access_role(db, user.id, layout_id) if user else None
        )

    # A custom close code (4001/4003) is only delivered to the browser as a
    # WebSocket close frame if the handshake was ACCEPTED first. Closing before
    # accept() rejects at the HTTP layer and the client sees a generic 1006 —
    # which its no-retry logic can't distinguish, so it would reconnect forever.
    # Accept, then close with the real reason on every denial path.
    if user is None:
        await websocket.accept()
        await websocket.close(code=4001, reason="Nicht authentifiziert")
        return
    # Server-side tier gate (CLAUDE.md: enforce features at route boundaries).
    # Effective tier so an enterprise org unlocks collaboration for members.
    if not has_feature(effective_tier(user), Feature.COLLABORATION):
        await websocket.accept()
        await websocket.close(
            code=4003, reason="Collaboration erfordert den PRO-Tarif"
        )
        return
    if access_role is None:
        await websocket.accept()
        await websocket.close(code=4003, reason="Kein Zugriff auf dieses Layout")
        return

    user_info = {
        "user_id": str(user.id),
        "name": user.email,
        "role": access_role,
        "joined_at": datetime.now(timezone.utc).isoformat(),
    }

    await manager.connect(websocket, layout_id, user_info)

    try:
        while True:
            data = await websocket.receive_json()
            message_type = data.get("type", "unknown")

            if message_type == "cursor_move":
                # Broadcast cursor position to others
                await manager.broadcast(layout_id, {
                    "type": "cursor_move",
                    "user": user_info,
                    "position": data.get("position", {}),
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                }, exclude=websocket)

            elif message_type == "zone_select":
                # Broadcast zone selection
                await manager.broadcast(layout_id, {
                    "type": "zone_select",
                    "user": user_info,
                    "zone_name": data.get("zone_name"),
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                }, exclude=websocket)

            elif message_type == "zone_edit":
                # Write semantics respect the sharing role: a read-only viewer
                # must not broadcast edits into everyone's live view.
                if access_role == "viewer":
                    await websocket.send_json({
                        "type": "error",
                        "message": "Nur-Lesen-Zugriff — Änderungen sind nicht erlaubt.",
                    })
                    continue
                # Broadcast zone edit (optimistic: client applies locally, server broadcasts)
                await manager.broadcast(layout_id, {
                    "type": "zone_edit",
                    "user": user_info,
                    "zone_name": data.get("zone_name"),
                    "changes": data.get("changes", {}),
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                }, exclude=websocket)

            elif message_type == "comment":
                # Broadcast comment/annotation
                await manager.broadcast(layout_id, {
                    "type": "comment",
                    "user": user_info,
                    "text": data.get("text", ""),
                    "position": data.get("position"),
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                }, exclude=websocket)

            elif message_type == "ping":
                await websocket.send_json({"type": "pong"})

            else:
                # Forward unknown message types — but never from viewers
                # (arbitrary payloads are potential write/injection channels)
                if access_role == "viewer":
                    await websocket.send_json({
                        "type": "error",
                        "message": "Nur-Lesen-Zugriff — dieser Nachrichtentyp ist nicht erlaubt.",
                    })
                    continue
                await manager.broadcast(layout_id, {
                    "type": message_type,
                    "user": user_info,
                    "data": data,
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                }, exclude=websocket)

    except WebSocketDisconnect:
        disconnected_user = manager.disconnect(websocket, layout_id)
        if disconnected_user:
            await manager.broadcast(layout_id, {
                "type": "user_left",
                "user": disconnected_user,
                "timestamp": datetime.now(timezone.utc).isoformat(),
            })
    except Exception as e:
        logger.error("WebSocket error for layout %s: %s", layout_id, e)
        manager.disconnect(websocket, layout_id)


@router.get("/collaborate/sessions")
async def list_active_sessions(_user: User = Depends(require_role("admin"))):
    """List all currently active collaboration sessions — admin only.

    This exposes every active layout_id plus participant emails across tenants,
    so it is restricted to admins. Regular users receive their own per-layout
    presence over the WebSocket instead.
    """
    return {"sessions": manager.active_sessions()}
