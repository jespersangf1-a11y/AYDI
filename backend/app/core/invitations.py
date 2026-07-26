"""Shared invitation helpers (pillar 4, stage 2).

The security-relevant invariants live here so project and org invitation
endpoints cannot drift apart:
- email normalization (one function, used at write, at /mine matching, and
  would be used by any registration hook) — lower()+strip() only, NEVER
  alias/dot folding (over-normalization could deliver a grant to the wrong
  account).
- a fixed TTL so stale grants expire.
- one response builder so scope/target/inviter are derived consistently.
"""
from datetime import datetime, timedelta, timezone

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.models import Invitation, Organization, Project, User

INVITATION_TTL_DAYS = 14
# Abuse cap: max pending invitations a single user may have outstanding.
MAX_PENDING_PER_INVITER = 50


def normalize_email(email: str) -> str:
    """The one normalization applied everywhere an email is an auth boundary."""
    return (email or "").strip().lower()


def invitation_expiry() -> datetime:
    return datetime.now(timezone.utc) + timedelta(days=INVITATION_TTL_DAYS)


def _aware(dt: datetime) -> datetime:
    """SQLite returns naive datetimes; compare in UTC."""
    return dt if dt.tzinfo is not None else dt.replace(tzinfo=timezone.utc)


def is_expired(inv: Invitation) -> bool:
    return _aware(inv.expires_at) < datetime.now(timezone.utc)


async def build_invitation_response(inv: Invitation, db: AsyncSession) -> dict:
    """Assemble the InvitationResponse dict (scope, target name, inviter)."""
    scope = "project" if inv.project_id is not None else "org"
    target_name: str | None = None
    if inv.project_id is not None:
        proj = await db.execute(select(Project.name).where(Project.id == inv.project_id))
        target_name = proj.scalar_one_or_none()
    elif inv.organization_id is not None:
        org = await db.execute(
            select(Organization.name).where(Organization.id == inv.organization_id)
        )
        target_name = org.scalar_one_or_none()

    invited_by_email: str | None = None
    if inv.invited_by_user_id is not None:
        inviter = await db.execute(
            select(User.email).where(User.id == inv.invited_by_user_id)
        )
        invited_by_email = inviter.scalar_one_or_none()

    return {
        "id": inv.id,
        "email": inv.email,
        "role": inv.role,
        "status": inv.status,
        "scope": scope,
        "project_id": inv.project_id,
        "organization_id": inv.organization_id,
        "target_name": target_name,
        "invited_by_email": invited_by_email,
        "created_at": inv.created_at,
        "expires_at": inv.expires_at,
    }


async def count_pending_from_inviter(db: AsyncSession, user_id) -> int:
    from sqlalchemy import func

    result = await db.execute(
        select(func.count(Invitation.id)).where(
            Invitation.invited_by_user_id == user_id,
            Invitation.status == "pending",
        )
    )
    return result.scalar_one() or 0
