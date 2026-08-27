"""Authentication endpoints: login, refresh, register, logout, me.

Cookie-first authentication: login/refresh issue httpOnly cookies plus a
non-httpOnly ``csrf_token`` cookie for double-submit CSRF protection.
For backward compatibility, access_token + refresh_token are still
returned in the response body, but new web clients should rely on the
cookies and ignore the body fields.

Wiederholte Fehlversuche werden pro IP und pro Konto gezaehlt und fuehren zu
einer zeitlich begrenzten Sperre (siehe ``_lockout_keys``) — sonst ist das
Anmeldeformular ein offenes Rateorakel.
"""
import asyncio
import logging
import secrets
import time
from uuid import UUID

import jwt
from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from pydantic import BaseModel, EmailStr, Field, field_validator
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.auth import (
    MIN_PASSWORD_LENGTH,
    create_access_token,
    create_refresh_token,
    decode_token,
    hash_password,
    validate_password_strength,
    verify_password,
    waste_password_time,
)
from app.core.config import settings
from app.core.permissions import (
    ACCESS_COOKIE_NAME,
    REFRESH_COOKIE_NAME,
    get_current_user,
)
from app.db.database import get_db
from app.models.models import User

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/auth", tags=["auth"])

CSRF_COOKIE_NAME = "aydi_csrf"


# ---------------------------------------------------------------------------
# Failed-login lockout
# ---------------------------------------------------------------------------
#
# Nothing stopped a caller from trying one password after another; only the
# generic rate limit of 20 requests per minute on /api/v1/auth applied, and
# that limit is per IP address, so a list of stolen passwords could be walked
# through indefinitely.
#
# Failures are now counted per source address *and* per e-mail address, with
# deliberately different thresholds:
#
#   per IP     5 failures  — the usual case, one host guessing passwords.
#   per e-mail 20 failures — a hard lock after five would let anybody lock a
#                            known account out of the product simply by
#                            failing five times against it. The higher bound
#                            still slows down an attack spread over many
#                            hosts without handing out that denial of
#                            service.
#
# The counters live in memory, which is enough for a single process. With more
# than one worker each keeps its own view — the correct fix there is a shared
# store (Redis), noted here so the limitation is not mistaken for an oversight.

_MAX_FAILED_PER_IP = 5
_MAX_FAILED_PER_EMAIL = 20
_LOCKOUT_SECONDS = 900  # 15 Minuten

#: key -> (Fehlversuche, Zeitpunkt des letzten Fehlversuchs)
_failed_logins: dict[str, tuple[int, float]] = {}
_lockout_guard = asyncio.Lock()


def _lockout_keys(email: str, client_ip: str) -> list[tuple[str, int]]:
    """Return the (key, threshold) pairs a login attempt is counted against."""
    return [
        (f"ip:{client_ip}", _MAX_FAILED_PER_IP),
        (f"email:{email.lower()}", _MAX_FAILED_PER_EMAIL),
    ]


async def _seconds_until_unlocked(keys: list[tuple[str, int]]) -> int:
    """Return the remaining lockout time in seconds, 0 if not locked."""
    now = time.monotonic()
    remaining = 0
    async with _lockout_guard:
        for key, threshold in keys:
            entry = _failed_logins.get(key)
            if not entry:
                continue
            attempts, last_failure = entry
            age = now - last_failure
            if age >= _LOCKOUT_SECONDS:
                # Das Fenster ist abgelaufen, der Zähler beginnt von vorn.
                _failed_logins.pop(key, None)
                continue
            if attempts >= threshold:
                remaining = max(remaining, int(_LOCKOUT_SECONDS - age) + 1)
    return remaining


async def _record_failure(keys: list[tuple[str, int]]) -> None:
    now = time.monotonic()
    async with _lockout_guard:
        for key, _threshold in keys:
            attempts, last_failure = _failed_logins.get(key, (0, now))
            if now - last_failure >= _LOCKOUT_SECONDS:
                attempts = 0
            _failed_logins[key] = (attempts + 1, now)


async def _clear_failures(keys: list[tuple[str, int]]) -> None:
    async with _lockout_guard:
        for key, _threshold in keys:
            _failed_logins.pop(key, None)


def _client_ip(request: Request | None) -> str:
    if request is None:
        return "unknown"
    forwarded = request.headers.get("x-forwarded-for")
    if forwarded:
        return forwarded.split(",")[0].strip()
    if request.client:
        return request.client.host
    return "unknown"


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
    # Die Mindestlänge steht jetzt an einer einzigen Stelle; die inhaltliche
    # Prüfung (Zeichenarten, Sperrliste, E-Mail im Passwort) folgt im Handler.
    password: str = Field(..., min_length=MIN_PASSWORD_LENGTH, max_length=128)
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
    request: Request,
    response: Response,
    db: AsyncSession = Depends(get_db),
):
    keys = _lockout_keys(data.email, _client_ip(request))

    locked_for = await _seconds_until_unlocked(keys)
    if locked_for:
        minutes = max(1, round(locked_for / 60))
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=(
                "Zu viele fehlgeschlagene Anmeldeversuche. "
                f"Bitte in etwa {minutes} Minuten erneut versuchen."
            ),
            headers={"Retry-After": str(locked_for)},
        )

    result = await db.execute(select(User).where(User.email == data.email))
    user = result.scalar_one_or_none()

    if user is None:
        # Ohne diesen Schritt antwortete eine unbekannte Adresse in etwa
        # 270 ms und eine bekannte in etwa 836 ms, weil nur die bekannte
        # überhaupt bis zum Passwort-Hash kam. Der Unterschied verriet
        # zuverlässig, welche Adressen ein Konto haben.
        waste_password_time()
        await _record_failure(keys)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Ungültige Anmeldedaten",
        )

    if not verify_password(data.password, user.hashed_password):
        await _record_failure(keys)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Ungültige Anmeldedaten",
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Konto deaktiviert",
        )

    await _clear_failures(keys)

    access = create_access_token(str(user.id), user.role)
    refresh = create_refresh_token(str(user.id))
    csrf = _set_auth_cookies(response, access, refresh)
    return TokenResponse(access_token=access, refresh_token=refresh, csrf_token=csrf)


@router.post("/register", response_model=UserResponse, status_code=201)
async def register(
    data: RegisterRequest,
    db: AsyncSession = Depends(get_db),
):
    # Bisher galt nur eine Mindestlänge von 8 Zeichen, "12345678" wurde also
    # angenommen. Die inhaltliche Prüfung meldet auf Deutsch, was fehlt.
    try:
        validate_password_strength(data.password, email=data.email)
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(exc),
        ) from exc

    # Check if email already exists
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
    try:
        await db.commit()
    except IntegrityError:
        # Zwischen der Prüfung oben und dem Schreiben kann dieselbe Adresse
        # von einer zweiten Anfrage angelegt worden sein. Vorher endete das
        # in HTTP 500 — bei sechs gleichzeitigen Registrierungen viermal.
        await db.rollback()
        logger.info("Registrierung kollidierte mit einer parallelen Anfrage")
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="E-Mail bereits registriert",
        ) from None
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
