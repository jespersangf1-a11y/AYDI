"""FastAPI dependencies for authentication and authorization.

Provides:
- JWT-based user authentication
- Role-based access control (admin, user, viewer)
- Subscription tier gating (free, pro, enterprise)
- Optional auth for public endpoints
"""
from uuid import UUID

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.auth import decode_token
from app.core.i18n import t
from app.core.subscription import Feature, require_feature as _require_feature
from app.db.database import get_db
from app.models.models import User

import jwt

security = HTTPBearer(auto_error=False)


async def get_current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(security),
    db: AsyncSession = Depends(get_db),
) -> User:
    """Extract and validate the current user from the JWT bearer token."""
    if credentials is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=t("auth.login_required"),
        )

    try:
        payload = decode_token(credentials.credentials)
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=t("auth.token_expired"),
        )
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=t("auth.invalid_credentials"),
        )

    if payload.get("type") != "access":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=t("auth.invalid_credentials"),
        )

    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=t("auth.invalid_credentials"),
        )

    result = await db.execute(select(User).where(User.id == UUID(user_id)))
    user = result.scalar_one_or_none()
    if not user or not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=t("auth.invalid_credentials"),
        )

    return user


def require_role(*roles: str):
    """Dependency factory that checks if the current user has one of the required roles."""
    async def _check_role(user: User = Depends(get_current_user)) -> User:
        if user.role not in roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=t("auth.insufficient_permissions"),
            )
        return user
    return _check_role


def require_tier(*features: Feature):
    """Dependency factory that checks if the user's subscription tier allows a feature.

    Usage:
        @router.get("/data", dependencies=[Depends(require_tier(Feature.FULL_ANALYSIS))])
        async def get_data(...):
            ...
    """
    async def _check_tier(user: User = Depends(get_current_user)) -> User:
        for feature in features:
            _require_feature(user.tier, feature)
        return user
    return _check_tier


async def authenticate_websocket(
    websocket,
    db: AsyncSession,
) -> User | None:
    """Authenticate a WebSocket connection via token query parameter.

    Usage in WebSocket endpoint:
        db = async_session()  # or however you get a session
        user = await authenticate_websocket(websocket, db)
        if user is None:
            await websocket.close(code=4001, reason="Nicht authentifiziert")
            return
    """
    token = websocket.query_params.get("token")
    if not token:
        return None
    try:
        payload = decode_token(token)
    except (jwt.ExpiredSignatureError, jwt.PyJWTError):
        return None

    if payload.get("type") != "access":
        return None

    user_id = payload.get("sub")
    if not user_id:
        return None

    result = await db.execute(select(User).where(User.id == UUID(user_id)))
    user = result.scalar_one_or_none()
    if not user or not user.is_active:
        return None
    return user


# Convenience: optional auth (returns None if no token)
async def get_optional_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(security),
    db: AsyncSession = Depends(get_db),
) -> User | None:
    """Like get_current_user but returns None instead of raising if no token."""
    if credentials is None:
        return None
    try:
        return await get_current_user(credentials, db)
    except HTTPException:
        return None
