"""FastAPI dependencies for authentication and authorization.

Provides:
- Cookie-first JWT authentication with header fallback (controlled by
  settings.AUTH_COOKIE_ONLY)
- Role-based access control (admin, user, viewer)
- Subscription tier gating (free, pro, enterprise)
- Optional auth for public endpoints

Authentication source priority:
  1. ``aydi_access`` httpOnly cookie (preferred — set by /auth/login)
  2. ``Authorization: Bearer <token>`` header (fallback for API clients
     and tests, unless settings.AUTH_COOKIE_ONLY is True)
"""
from uuid import UUID

from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.auth import decode_token
from app.core.config import settings
from app.core.i18n import t
from app.core.subscription import Feature, _tier_rank, require_feature as _require_feature
from app.db.database import get_db
from app.models.models import User

import jwt

# auto_error=False so that we can fall through to cookie lookup when no
# Authorization header is present.
security = HTTPBearer(auto_error=False)

ACCESS_COOKIE_NAME = "aydi_access"
REFRESH_COOKIE_NAME = "aydi_refresh"


def _extract_token(
    request: Request,
    credentials: HTTPAuthorizationCredentials | None,
) -> str | None:
    """Extract a JWT access token from cookie (preferred) or Authorization header.

    Returns None if neither is present, or if AUTH_COOKIE_ONLY is set and
    only the header is present.
    """
    cookie_token = request.cookies.get(ACCESS_COOKIE_NAME)
    if cookie_token:
        return cookie_token
    if settings.AUTH_COOKIE_ONLY:
        return None
    if credentials is not None:
        return credentials.credentials
    return None


# ---------------------------------------------------------------------------
# Effective subscription tier (pillar 4, stage 2)
# ---------------------------------------------------------------------------

async def resolve_effective_tier(user: User, db: AsyncSession) -> str:
    """The tier that actually governs a user = max(personal, org tiers).

    Organization membership grants the org's tier to every member (the
    seat-licensing story) — resolved per request, never persisted, so leaving
    an org or an org downgrade takes effect on the next request.
    """
    from app.models.models import Organization, OrganizationMember

    result = await db.execute(
        select(Organization.tier)
        .join(OrganizationMember, OrganizationMember.organization_id == Organization.id)
        .where(OrganizationMember.user_id == user.id)
    )
    best = user.tier
    for (org_tier,) in result.all():
        if _tier_rank(org_tier) > _tier_rank(best):
            best = org_tier
    return best


def effective_tier(user: User) -> str:
    """Read the effective tier attached by get_current_user /
    authenticate_websocket. Falls back to the personal tier when the attr is
    absent — which keeps tests that inject bare User objects via
    dependency_overrides gating on the personal tier, exactly as before."""
    return getattr(user, "effective_tier", None) or user.tier


async def get_current_user(
    request: Request,
    credentials: HTTPAuthorizationCredentials | None = Depends(security),
    db: AsyncSession = Depends(get_db),
) -> User:
    """Extract and validate the current user from cookie or bearer token."""
    token = _extract_token(request, credentials)
    if token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=t("auth.login_required"),
        )

    try:
        payload = decode_token(token)
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

    # Attach the effective tier (personal ⊔ org tiers) for all downstream gates
    user.effective_tier = await resolve_effective_tier(user, db)  # type: ignore[attr-defined]
    return user


def require_role(*roles: str):
    """Dependency factory: only users with one of the listed roles pass."""
    async def _check_role(user: User = Depends(get_current_user)) -> User:
        if user.role not in roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=t("auth.insufficient_permissions"),
            )
        return user
    return _check_role


def require_tier(*features: Feature):
    """Dependency factory: gate behind subscription feature flags.

    Reads the EFFECTIVE tier (personal ⊔ org), so an enterprise org unlocks
    its features for every member."""
    async def _check_tier(user: User = Depends(get_current_user)) -> User:
        for feature in features:
            _require_feature(effective_tier(user), feature)
        return user
    return _check_tier


async def authenticate_websocket(
    websocket,
    db: AsyncSession,
) -> User | None:
    """Authenticate a WebSocket connection via token query parameter or cookie."""
    token = websocket.query_params.get("token")
    if not token:
        # Fallback: cookies are sent on the upgrade request too
        token = websocket.cookies.get(ACCESS_COOKIE_NAME)
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
    user.effective_tier = await resolve_effective_tier(user, db)  # type: ignore[attr-defined]
    return user


async def get_optional_user(
    request: Request,
    credentials: HTTPAuthorizationCredentials | None = Depends(security),
    db: AsyncSession = Depends(get_db),
) -> User | None:
    """Like get_current_user but returns None instead of raising if no token."""
    if _extract_token(request, credentials) is None:
        return None
    try:
        return await get_current_user(request, credentials, db)
    except HTTPException:
        return None


# ---------------------------------------------------------------------------
# Project access (pillar 4, stage 1: sharing with roles)
# ---------------------------------------------------------------------------

# Role hierarchy for shared projects. "owner" is not a member role — it is
# derived from Project.user_id and always wins.
_PROJECT_ROLE_ORDER: dict[str, int] = {"viewer": 0, "editor": 1, "owner": 2}
_RANK_TO_ROLE: dict[int, str] = {v: k for k, v in _PROJECT_ROLE_ORDER.items()}

# Organization role -> effective project role (pillar 4, stage 2).
# Members can edit fleet projects (editing is the job inside a Werft);
# org owners/admins get full control (offboarding a departed employee's work).
_ORG_ROLE_TO_PROJECT_ROLE: dict[str, str] = {
    "owner": "owner",
    "admin": "owner",
    "member": "editor",
}


async def _effective_project_role(project, user: User, db: AsyncSession) -> str | None:
    """Highest role the user holds on a project, or None for no access.

    Combines three sources (max wins):
      1. Project.user_id  -> 'owner' (always wins)
      2. ProjectMember.role (explicit per-project grant, incl. external guests)
      3. org membership on Project.org_id, mapped via _ORG_ROLE_TO_PROJECT_ROLE
    project_members only ever ADD access; the org never restricts an explicit
    grant, and an explicit grant never restricts org access.
    """
    from app.models.models import OrganizationMember, ProjectMember

    if project.user_id == user.id:
        return "owner"

    best = -1
    member = await db.execute(
        select(ProjectMember.role).where(
            ProjectMember.project_id == project.id,
            ProjectMember.user_id == user.id,
        )
    )
    row = member.scalar_one_or_none()
    if row is not None:
        best = max(best, _PROJECT_ROLE_ORDER.get(row, -1))

    if project.org_id is not None:
        org = await db.execute(
            select(OrganizationMember.org_role).where(
                OrganizationMember.organization_id == project.org_id,
                OrganizationMember.user_id == user.id,
            )
        )
        org_role = org.scalar_one_or_none()
        if org_role is not None:
            mapped = _ORG_ROLE_TO_PROJECT_ROLE.get(org_role)
            if mapped is not None:
                best = max(best, _PROJECT_ROLE_ORDER[mapped])

    return _RANK_TO_ROLE.get(best)


async def get_accessible_project(
    project_id: UUID,
    user: User,
    db: AsyncSession,
    min_role: str = "editor",
):
    """Resolve a project the user may access with at least ``min_role``.

    Access = max(owner-if-creator, explicit ProjectMember role, org-derived
    role for Project.org_id). 404 when the project does not exist OR the user
    has no access at all (no existence leak). 403 when the user has access but
    an insufficient role — a German, actionable message.

    Defaulting to "editor" is deliberate: a missed read-callsite then
    over-restricts a viewer instead of silently allowing writes.
    """
    from app.models.models import Project

    result = await db.execute(select(Project).where(Project.id == project_id))
    project = result.scalar_one_or_none()
    if not project:
        raise HTTPException(status_code=404, detail="Projekt nicht gefunden")

    role = await _effective_project_role(project, user, db)
    if role is None:
        raise HTTPException(status_code=404, detail="Projekt nicht gefunden")

    if _PROJECT_ROLE_ORDER[role] >= _PROJECT_ROLE_ORDER.get(min_role, 99):
        return project

    if min_role == "owner":
        raise HTTPException(
            status_code=403,
            detail="Nur der Eigentümer (bzw. Org-Eigentümer/Admin) kann diese Aktion ausführen.",
        )
    raise HTTPException(
        status_code=403,
        detail=(
            f"Diese Aktion erfordert die Rolle '{min_role}' — "
            f"Ihre Rolle in diesem Projekt: '{role}'."
        ),
    )


async def get_project_access_role(
    project_id: UUID,
    user: User,
    db: AsyncSession,
) -> str | None:
    """'owner' / 'editor' / 'viewer' / None — effective role for display."""
    from app.models.models import Project

    result = await db.execute(select(Project).where(Project.id == project_id))
    project = result.scalar_one_or_none()
    if not project:
        return None
    return await _effective_project_role(project, user, db)


# ---------------------------------------------------------------------------
# Organization access (pillar 4, stage 2)
# ---------------------------------------------------------------------------

_ORG_ROLE_ORDER: dict[str, int] = {"member": 0, "admin": 1, "owner": 2}


async def get_org_role(org_id: UUID, user: User, db: AsyncSession) -> str | None:
    """The caller's org_role, or None if not a member."""
    from app.models.models import OrganizationMember

    result = await db.execute(
        select(OrganizationMember.org_role).where(
            OrganizationMember.organization_id == org_id,
            OrganizationMember.user_id == user.id,
        )
    )
    return result.scalar_one_or_none()


async def require_org(
    org_id: UUID,
    user: User,
    db: AsyncSession,
    min_role: str = "member",
):
    """Resolve an organization the caller may access with at least ``min_role``.

    404 for unknown org OR non-members (no existence leak / no org
    enumeration); 403 for members with an insufficient org_role.
    """
    from app.models.models import Organization

    result = await db.execute(select(Organization).where(Organization.id == org_id))
    org = result.scalar_one_or_none()
    if not org:
        raise HTTPException(status_code=404, detail="Organisation nicht gefunden")

    role = await get_org_role(org_id, user, db)
    if role is None:
        raise HTTPException(status_code=404, detail="Organisation nicht gefunden")

    if _ORG_ROLE_ORDER.get(role, -1) >= _ORG_ROLE_ORDER.get(min_role, 99):
        return org

    raise HTTPException(
        status_code=403,
        detail=(
            f"Diese Aktion erfordert die Organisationsrolle '{min_role}' — "
            f"Ihre Rolle: '{role}'."
        ),
    )
