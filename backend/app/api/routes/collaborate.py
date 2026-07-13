"""Real-time collaboration endpoints."""
import logging
from datetime import datetime, timezone
from uuid import UUID

from fastapi import APIRouter, Depends, Query, WebSocket, WebSocketDisconnect
from sqlalchemy import select

from app.core.permissions import authenticate_websocket, require_role
from app.core.websocket import manager
from app.db.database import async_session
from app.models.models import Layout, Project, User

logger = logging.getLogger(__name__)

router = APIRouter(tags=["collaboration"])


async def _user_owns_layout(db, user_id, layout_id: str) -> bool:
    """True if ``layout_id`` belongs to a project owned by ``user_id``."""
    try:
        lid = UUID(str(layout_id))
    except (ValueError, TypeError):
        return False
    row = await db.execute(
        select(Layout.id)
        .join(Project, Layout.project_id == Project.id)
        .where(Layout.id == lid, Project.user_id == user_id)
    )
    return row.scalar_one_or_none() is not None


@router.websocket("/ws/collaborate/{layout_id}")
async def collaborate_websocket(
    websocket: WebSocket,
    layout_id: str,
):
    """WebSocket endpoint for real-time layout collaboration.

    Requires authentication via ?token=<JWT> query parameter.
    """
    # Authenticate AND authorize before accepting the connection. Authentication
    # alone is not enough: without the ownership check any logged-in user could
    # join a stranger's private layout and read/inject live design data.
    async with async_session() as db:
        user = await authenticate_websocket(websocket, db)
        authorized = user is not None and await _user_owns_layout(db, user.id, layout_id)

    if user is None:
        await websocket.close(code=4001, reason="Nicht authentifiziert")
        return
    if not authorized:
        await websocket.close(code=4003, reason="Kein Zugriff auf dieses Layout")
        return

    user_info = {
        "user_id": str(user.id),
        "name": user.email,
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
                # Forward unknown message types
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
