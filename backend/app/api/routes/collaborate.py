"""Real-time collaboration endpoints."""
import logging
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, Query, WebSocket, WebSocketDisconnect

from app.core.permissions import authenticate_websocket, get_current_user
from app.core.websocket import manager
from app.db.database import async_session
from app.models.models import User

logger = logging.getLogger(__name__)

router = APIRouter(tags=["collaboration"])


@router.websocket("/ws/collaborate/{layout_id}")
async def collaborate_websocket(
    websocket: WebSocket,
    layout_id: str,
):
    """WebSocket endpoint for real-time layout collaboration.

    Requires authentication via ?token=<JWT> query parameter.
    """
    # Authenticate before accepting the connection
    async with async_session() as db:
        user = await authenticate_websocket(websocket, db)

    if user is None:
        await websocket.close(code=4001, reason="Nicht authentifiziert")
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
async def list_active_sessions(_user: User = Depends(get_current_user)):
    """List all currently active collaboration sessions."""
    return {"sessions": manager.active_sessions()}
