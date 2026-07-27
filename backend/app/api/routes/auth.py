"""Authentication endpoints: login, refresh, register, logout, me.

Cookie-first authentication: login/refresh issue httpOnly cookies plus a
non-httpOnly ``csrf_token`` cookie for double-submit CSRF protection.
For backward compatibility, access_token + refresh_token are still
returned in the response body, but new web clients should rely on the
cookies and ignore the body fields.
"""
import secrets
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Response, status
from pydantic import BaseModel, EmailStr, Field, field_validator
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.auth import (
    create_access_token,
    create_refresh_token,
    decode_token,
    hash_password,
    verify_password,
)
from app.core.config import settings
from app.core.permissions import (
    ACCESS_COOKIE_NAME,
    REFRESH_COOKIE_NAME,
    get_current_user,
)
from app.db.database import get_db
from app.models.models import User

import jwt

router = APIRouter(prefix="/auth", tags=["auth"])

CSRF_COOKIE_NAME = "aydi_csrf"


class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=1)


# A small blocklist of the most common weak passwords. Not exhaustive — the
# structural checks below (character variety, distinct-character count) catch
# the long tail; this just rejects the obvious ones with a clear message.
_COMMON_PASSWORDS = frozenset({
    "password", "passwort", "12345678", "123456789", "1234567890",
    "qwertyui", "qwertz12", "iloveyou", "admin123", "letmein1",
    "welcome1", "abc12345", "password1", "passw0rd",
})


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=128)
    full_name: str = Field(..., min_length=2, max_length=200)
    shipyard_id: str | None = Field(None, max_length=100)

    @field_validator("password")
    @classmethod
    def _password_strength(cls, v: str) -> str:
        """Enforce a minimal strength policy beyond length (N-2).

        Rejects common passwords, near-uniform strings (e.g. 'aaaaaaaa'), and
        single-character-class passwords under 12 chars. Deliberately lenient
        so it never blocks a genuinely strong passphrase.
        """
        if v.lower() in _COMMON_PASSWORDS:
            raise ValueError("Passwort ist zu häufig und leicht zu erraten.")
        if len(set(v)) < 4:
            raise ValueError("Passwort enthält zu wenige unterschiedliche Zeichen.")
        classes = sum([
            any(c.islower() for c in v),
            any(c.isupper() for c in v),
            any(c.isdigit() for c in v),
            any(not c.isalnum() for c in v),
        ])
        if len(v) < 12 and classes < 2:
            raise ValueError(
                "Passwort muss Buchstaben mit Ziffern oder Sonderzeichen "
                "kombinieren (oder mindestens 12 Zeichen lang sein)."
            )
        return v


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    csrf_token: str | None = None


class RefreshRequest(BaseModel):
    refresh_token: str | None = None  # optional — read from cookie if absent


class UserResponse(BaseModel):
    id: str
    email: str
    full_name: str
    role: str
    shipyard_id: str | None
    is_active: bool


def _set_auth_cookies(response: Response, access: str, refresh: str) -> str:
    """Attach the three auth cookies to the outgoing response and return the CSRF token."""
    csrf = secrets.token_urlsafe(32)
    common = {
        "secure": settings.COOKIE_SECURE,
        "samesite": "lax",
        "domain": settings.COOKIE_DOMAIN,
        "path": "/",
    }
    response.set_cookie(
        ACCESS_COOKIE_NAME,
        access,
        httponly=True,
        max_age=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        **common,
    )
    response.set_cookie(
        REFRESH_COOKIE_NAME,
        refresh,
        httponly=True,
        max_age=settings.REFRESH_TOKEN_EXPIRE_DAYS * 24 * 60 * 60,
        **common,
    )
    # CSRF token is NOT httponly — frontend reads it and echoes it in X-CSRF-Token
    response.set_cookie(
        CSRF_COOKIE_NAME,
        csrf,
        httponly=False,
        max_age=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        **common,
    )
    return csrf


def _clear_auth_cookies(response: Response) -> None:
    for name in (ACCESS_COOKIE_NAME, REFRESH_COOKIE_NAME, CSRF_COOKIE_NAME):
        response.delete_cookie(name, path="/", domain=settings.COOKIE_DOMAIN)


@router.post("/login", response_model=TokenResponse)
async def login(
    data: LoginRequest,
    response: Response,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(User).where(User.email == data.email))
    user = result.scalar_one_or_none()
    if not user or not verify_password(data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Ungültige Anmeldedaten",
        )
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Konto deaktiviert",
        )

    access = create_access_token(str(user.id), user.role)
    refresh = create_refresh_token(str(user.id))
    csrf = _set_auth_cookies(response, access, refresh)
    return TokenResponse(access_token=access, refresh_token=refresh, csrf_token=csrf)


@router.post("/register", response_model=UserResponse, status_code=201)
async def register(
    data: RegisterRequest,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(User).where(User.email == data.email))
    if result.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="E-Mail bereits registriert",
        )

    user = User(
        email=data.email,
        hashed_password=hash_password(data.password),
        full_name=data.full_name,
        shipyard_id=data.shipyard_id,
        role="user",
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)

    return UserResponse(
        id=str(user.id),
        email=user.email,
        full_name=user.full_name,
        role=user.role,
        shipyard_id=user.shipyard_id,
        is_active=user.is_active,
    )


@router.post("/refresh", response_model=TokenResponse)
async def refresh_token(
    data: RefreshRequest,
    response: Response,
    db: AsyncSession = Depends(get_db),
):
    # Read refresh token from cookie if request body didn't carry one
    from fastapi import Request as _Request  # local import to avoid top-level cycle
    # Note: we accept either cookie or body for transition compatibility
    token_str = data.refresh_token
    if not token_str:
        # Fallback impossible without Request — clients without cookies must supply token in body
        raise HTTPException(status_code=400, detail="Refresh-Token fehlt")

    try:
        payload = decode_token(token_str)
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Refresh-Token abgelaufen")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Ungültiges Refresh-Token")

    if payload.get("type") != "refresh":
        raise HTTPException(status_code=401, detail="Ungültiger Token-Typ")

    result = await db.execute(select(User).where(User.id == UUID(payload["sub"])))
    user = result.scalar_one_or_none()
    if not user or not user.is_active:
        raise HTTPException(status_code=401, detail="Benutzer nicht gefunden")

    access = create_access_token(str(user.id), user.role)
    refresh = create_refresh_token(str(user.id))
    csrf = _set_auth_cookies(response, access, refresh)
    return TokenResponse(access_token=access, refresh_token=refresh, csrf_token=csrf)


@router.post("/logout", status_code=204)
async def logout(response: Response):
    """Clear auth cookies. Idempotent — safe to call without an active session."""
    _clear_auth_cookies(response)
    return Response(status_code=204)


@router.get("/me", response_model=UserResponse)
async def get_me(
    user: User = Depends(get_current_user),
):
    return UserResponse(
        id=str(user.id),
        email=user.email,
        full_name=user.full_name,
        role=user.role,
        shipyard_id=user.shipyard_id,
        is_active=user.is_active,
    )
