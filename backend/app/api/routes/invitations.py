"""Recipient-side invitation endpoints — pillar 4, stage 2.

The invitee's inbox and accept/decline. This is the ONLY place that matches an
account against an invitation (by normalized email), which is what keeps
invitation *creation* free of account-existence leaks. Acceptance is always
explicit — membership is never granted silently on registration.
"""
import logging
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.invitations import build_invitation_response, is_expired, normalize_email
from app.core.permissions import get_current_user
from app.db.database import get_db
from app.models.models import (
    Invitation,
    OrganizationMember,
    ProjectMember,
    User,
)
from app.schemas.schemas import InvitationResponse

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/invitations", tags=["invitations"])


@router.get("/mine", response_model=list[InvitationResponse])
async def list_my_invitations(
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Pending, unexpired invitations addressed to my email. Matches on the
    normalized email, so invites sent before I registered show up now."""
    email = normalize_email(_user.email)
    result = await db.execute(
        select(Invitation)
        .where(Invitation.email == email, Invitation.status == "pending")
        .order_by(Invitation.created_at.desc())
    )
    out = []
    for inv in result.scalars().all():
        if is_expired(inv):
            continue
        out.append(InvitationResponse(**await build_invitation_response(inv, db)))
    return out


async def _load_recipient_invitation(
    invitation_id: UUID, user: User, db: AsyncSession
) -> Invitation:
    """Load an invitation addressed to the caller — 404 for anyone else, so
    invitation IDs are not probeable by non-recipients."""
    result = await db.execute(
        select(Invitation).where(Invitation.id == invitation_id)
    )
    inv = result.scalar_one_or_none()
    if not inv or inv.email != normalize_email(user.email):
        raise HTTPException(status_code=404, detail="Einladung nicht gefunden")
    return inv


@router.post("/{invitation_id}/accept", response_model=InvitationResponse)
async def accept_invitation(
    invitation_id: UUID,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Accept an invitation → creates the membership. Idempotent if already a
    member. 410 for expired/revoked."""
    from datetime import datetime, timezone

    inv = await _load_recipient_invitation(invitation_id, _user, db)

    if inv.status != "pending":
        raise HTTPException(
            status_code=410,
            detail="Diese Einladung ist abgelaufen oder wurde zurückgezogen.",
        )
    if is_expired(inv):
        inv.status = "expired"
        await db.commit()
        raise HTTPException(status_code=410, detail="Diese Einladung ist abgelaufen.")

    if inv.project_id is not None:
        existing = await db.execute(
            select(ProjectMember).where(
                ProjectMember.project_id == inv.project_id,
                ProjectMember.user_id == _user.id,
            )
        )
        member = existing.scalar_one_or_none()
        if member is None:
            db.add(
                ProjectMember(
                    project_id=inv.project_id, user_id=_user.id, role=inv.role
                )
            )
        else:
            member.role = inv.role  # accepting a fresh invite updates the grant
    else:
        existing = await db.execute(
            select(OrganizationMember).where(
                OrganizationMember.organization_id == inv.organization_id,
                OrganizationMember.user_id == _user.id,
            )
        )
        om = existing.scalar_one_or_none()
        if om is None:
            db.add(
                OrganizationMember(
                    organization_id=inv.organization_id,
                    user_id=_user.id,
                    org_role=inv.role,
                )
            )
        else:
            om.org_role = inv.role

    inv.status = "accepted"
    inv.responded_at = datetime.now(timezone.utc)
    await db.commit()
    await db.refresh(inv)
    logger.info("User %s accepted invitation %s", _user.id, invitation_id)
    return InvitationResponse(**await build_invitation_response(inv, db))


@router.post("/{invitation_id}/decline", status_code=204)
async def decline_invitation(
    invitation_id: UUID,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    from datetime import datetime, timezone

    inv = await _load_recipient_invitation(invitation_id, _user, db)
    if inv.status == "pending":
        inv.status = "declined"
        inv.responded_at = datetime.now(timezone.utc)
        await db.commit()
