"""WebSocket connection manager for real-time collaboration."""
import logging
from datetime import datetime, timezone
from typing import Optional

from fastapi import WebSocket

logger = logging.getLogger(__name__)


class ConnectionManager:
    """Manages WebSocket connections for layout collaboration sessions."""

    def __init__(self):
        # layout_id → list of (websocket, user_info)
        self._connections: dict[str, list[tuple[WebSocket, dict]]] = {}

    async def connect(self, websocket: WebSocket, layout_id: str, user_info: dict):
        """Accept a new WebSocket connection and add to the layout's room."""
        await websocket.accept()
        if layout_id not in self._connections:
            self._connections[layout_id] = []
        self._connections[layout_id].append((websocket, user_info))
        logger.info(f"User {user_info.get('name', 'unknown')} connected to layout {layout_id}")

        # Notify others
        await self.broadcast(layout_id, {
            "type": "user_joined",
            "user": user_info,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }, exclude=websocket)

        # Send current participants to the new connection
        participants = self.get_participants(layout_id)
        await websocket.send_json({
            "type": "participants",
            "participants": participants,
        })

    def disconnect(self, websocket: WebSocket, layout_id: str) -> Optional[dict]:
        """Remove a WebSocket connection from the layout's room."""
        if layout_id not in self._connections:
            return None

        removed_info: Optional[dict] = None
        remaining: list[tuple[WebSocket, dict]] = []

        for ws, info in self._connections[layout_id]:
            if ws == websocket:
                removed_info = info
            else:
                remaining.append((ws, info))

        if remaining:
            self._connections[layout_id] = remaining
        else:
            del self._connections[layout_id]

        if removed_info:
            logger.info(f"User {removed_info.get('name', 'unknown')} disconnected from layout {layout_id}")

        return removed_info

    def get_participants(self, layout_id: str) -> list[dict]:
        """Get list of current participants in a layout session."""
        if layout_id not in self._connections:
            return []
        return [info for _, info in self._connections[layout_id]]

    async def broadcast(self, layout_id: str, message: dict, exclude: Optional[WebSocket] = None):
        """Send a message to all connections in a layout room."""
        if layout_id not in self._connections:
            return
        disconnected: list[WebSocket] = []
        for ws, info in self._connections[layout_id]:
            if ws == exclude:
                continue
            try:
                await ws.send_json(message)
            except Exception:
                disconnected.append(ws)
        # Clean up dead connections
        if disconnected:
            self._connections[layout_id] = [
                (ws, info) for ws, info in self._connections[layout_id]
                if ws not in disconnected
            ]

    def active_sessions(self) -> list[dict]:
        """Return info about all active collaboration sessions."""
        sessions = []
        for layout_id, connections in self._connections.items():
            sessions.append({
                "layout_id": layout_id,
                "participant_count": len(connections),
                "participants": [info for _, info in connections],
            })
        return sessions


# Singleton instance
manager = ConnectionManager()
