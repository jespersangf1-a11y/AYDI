"""Organization (team / shipyard) endpoints — pillar 4, stage 2.

Access model:
- Org roles: owner (full control), admin (manage members/invites), member.
- Org membership grants a base access role on the org's projects (owner/admin
  -> effective 'owner', member -> 'editor'); see permissions.get_accessible_project.
- org.tier is the seat-licensing lever (effective tier = max(personal, org));
  it is platform-admin-only — never self-service (that would be a privilege
  escalation: create org -> set enterprise -> free access to everything).
"""
import logging
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.invitations import (
    MAX_PENDING_PER_INVITER,
    build_invitation_response,
    count_pending_from_inviter,
    invitation_expiry,
    normalize_email,
)
from app.core.permissions import (
    get_current_user,
    get_org_role,
    require_org,
    require_role,
)
from app.core.subscription import Feature, has_feature
from app.core.permissions import effective_tier
from app.db.database import get_db
from app.models.models import (
    Invitation,
    Organization,
    OrganizationMember,
    Project,
    User,
)
from app.schemas.schemas import (
    InvitationResponse,
    OrganizationCreate,
    OrganizationResponse,
    OrganizationUpdate,
    OrgInvitationCreate,
    OrgMemberResponse,
    OrgMemberRoleUpdate,
    OrgTierUpdate,
    ProjectResponse,
)

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/orgs", tags=["organizations"])

# Cap owned orgs per user to bound abuse (org creation is open to everyone).
_MAX_OWNED_ORGS = 5


async def _member_count(org_id: UUID, db: AsyncSession) -> int:
    result = await db.execute(
        select(func.count(OrganizationMember.id)).where(
            OrganizationMember.organization_id == org_id
        )
    )
    return result.scalar_one() or 0


async def _locked_owner_count(org_id: UUID, db: AsyncSession) -> int:
    """Count owners while holding a row lock on the owner rows, so a concurrent
    demote/remove cannot race the last-owner guard down to zero. On PostgreSQL
    FOR UPDATE serializes the check-and-mutate; on SQLite writes serialize
    anyway. Must be called inside the same transaction as the mutation."""
    result = await db.execute(
        select(OrganizationMember.id)
        .where(
            OrganizationMember.organization_id == org_id,
            OrganizationMember.org_role == "owner",
        )
        .with_for_update()
    )
    return len(result.scalars().all())


@router.post("", response_model=OrganizationResponse, status_code=201)
async def create_organization(
    data: OrganizationCreate,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Create an organization. Open to any authenticated user; the creator
    becomes org owner. tier defaults to 'free' (raised only by platform admins)."""
    owned = await db.execute(
        select(func.count(Organization.id)).where(
            Organization.created_by_user_id == _user.id
        )
    )
    if (owned.scalar_one() or 0) >= _MAX_OWNED_ORGS:
        raise HTTPException(
            status_code=409,
            detail="Maximale Anzahl eigener Organisationen erreicht.",
        )

    org = Organization(name=data.name, tier="free", created_by_user_id=_user.id)
    db.add(org)
    await db.flush()
    db.add(
        OrganizationMember(organization_id=org.id, user_id=_user.id, org_role="owner")
    )
    await db.commit()
    await db.refresh(org)
    logger.info("User %s created organization %s", _user.id, org.id)
    return OrganizationResponse(
        id=org.id, name=org.name, tier=org.tier, created_at=org.created_at,
        org_role="owner", member_count=1,
    )


@router.get("", response_model=list[OrganizationResponse])
async def list_my_organizations(
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Organizations the caller is a member of (never global)."""
    result = await db.execute(
        select(Organization, OrganizationMember.org_role)
        .join(
            OrganizationMember,
            OrganizationMember.organization_id == Organization.id,
        )
        .where(OrganizationMember.user_id == _user.id)
        .order_by(Organization.created_at)
    )
    orgs = []
    for org, org_role in result.all():
        orgs.append(
            OrganizationResponse(
                id=org.id, name=org.name, tier=org.tier, created_at=org.created_at,
                org_role=org_role, member_count=await _member_count(org.id, db),
            )
        )
    return orgs


@router.get("/{org_id}", response_model=OrganizationResponse)
async def get_organization(
    org_id: UUID,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    org = await require_org(org_id, _user, db, min_role="member")
    role = await get_org_role(org_id, _user, db)
    return OrganizationResponse(
        id=org.id, name=org.name, tier=org.tier, created_at=org.created_at,
        org_role=role, member_count=await _member_count(org.id, db),
    )


@router.patch("/{org_id}", response_model=OrganizationResponse)
async def update_organization(
    org_id: UUID,
    data: OrganizationUpdate,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Rename an organization (owner/admin). tier is NOT changeable here."""
    org = await require_org(org_id, _user, db, min_role="admin")
    org.name = data.name
    await db.commit()
    await db.refresh(org)
    role = await get_org_role(org_id, _user, db)
    return OrganizationResponse(
        id=org.id, name=org.name, tier=org.tier, created_at=org.created_at,
        org_role=role, member_count=await _member_count(org.id, db),
    )


@router.delete("/{org_id}", status_code=204)
async def delete_organization(
    org_id: UUID,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Delete an org (owner only). Projects and brand references revert to
    private (org_id -> NULL); members and invitations are removed. No member
    work is destroyed.

    The cleanup is done EXPLICITLY rather than relying on DB-level FK cascade:
    SQLite does not enforce FK actions unless PRAGMA foreign_keys=ON, so an
    implicit `delete(org)` would leave dangling org_id / orphaned members in
    dev and test. Doing it in code guarantees identical behavior on every DB.
    """
    from sqlalchemy import update as _update

    org = await require_org(org_id, _user, db, min_role="owner")

    await db.execute(
        _update(Project).where(Project.org_id == org_id).values(org_id=None)
    )
    from app.models.models import BrandReferenceModel, Invitation

    await db.execute(
        _update(BrandReferenceModel)
        .where(BrandReferenceModel.org_id == org_id)
        .values(org_id=None)
    )
    await db.execute(
        Invitation.__table__.delete().where(Invitation.organization_id == org_id)
    )
    await db.execute(
        OrganizationMember.__table__.delete().where(
            OrganizationMember.organization_id == org_id
        )
    )
    await db.delete(org)
    await db.commit()
    logger.info("User %s deleted organization %s", _user.id, org_id)


# ---------------------------------------------------------------------------
# Members
# ---------------------------------------------------------------------------


@router.get("/{org_id}/members", response_model=list[OrgMemberResponse])
async def list_org_members(
    org_id: UUID,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    await require_org(org_id, _user, db, min_role="member")
    result = await db.execute(
        select(OrganizationMember, User)
        .join(User, OrganizationMember.user_id == User.id)
        .where(OrganizationMember.organization_id == org_id)
        .order_by(OrganizationMember.created_at)
    )
    return [
        OrgMemberResponse(
            user_id=user.id, email=user.email, full_name=user.full_name,
            org_role=member.org_role,
        )
        for member, user in result.all()
    ]


@router.patch("/{org_id}/members/{member_user_id}", response_model=OrgMemberResponse)
async def update_org_member_role(
    org_id: UUID,
    member_user_id: UUID,
    data: OrgMemberRoleUpdate,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Change a member's org role — OWNER ONLY (admins cannot mint admins;
    role administration is the highest-value takeover primitive)."""
    await require_org(org_id, _user, db, min_role="owner")

    result = await db.execute(
        select(OrganizationMember, User)
        .join(User, OrganizationMember.user_id == User.id)
        .where(
            OrganizationMember.organization_id == org_id,
            OrganizationMember.user_id == member_user_id,
        )
    )
    row = result.first()
    if not row:
        raise HTTPException(status_code=404, detail="Mitglied nicht gefunden")
    member, target = row

    # Last-owner protection: demoting the only owner would orphan the org.
    # Row-locked count serializes concurrent demote/remove (no race to zero).
    if member.org_role == "owner" and data.org_role != "owner":
        if await _locked_owner_count(org_id, db) <= 1:
            raise HTTPException(
                status_code=409,
                detail=(
                    "Die Organisation benötigt mindestens einen Eigentümer — "
                    "übertragen Sie zuerst die Eigentümerschaft."
                ),
            )

    member.org_role = data.org_role
    await db.commit()
    logger.info(
        "User %s set org %s member %s role=%s",
        _user.id, org_id, member_user_id, data.org_role,
    )
    return OrgMemberResponse(
        user_id=target.id, email=target.email, full_name=target.full_name,
        org_role=member.org_role,
    )


@router.delete("/{org_id}/members/{member_user_id}", status_code=204)
async def remove_org_member(
    org_id: UUID,
    member_user_id: UUID,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Remove a member.

    - Anyone may leave themselves (except the last owner).
    - Removing OTHERS requires the caller to strictly outrank the target, with
      owners as peers: an owner may remove anyone, but an admin may remove only
      members — NOT other admins or owners. This mirrors the owner-only rule
      for role changes (an admin must not evict a co-owner via the delete path).
    """
    if member_user_id == _user.id:
        await require_org(org_id, _user, db, min_role="member")
    else:
        await require_org(org_id, _user, db, min_role="admin")

    result = await db.execute(
        select(OrganizationMember).where(
            OrganizationMember.organization_id == org_id,
            OrganizationMember.user_id == member_user_id,
        )
    )
    member = result.scalar_one_or_none()
    if not member:
        raise HTTPException(status_code=404, detail="Mitglied nicht gefunden")

    if member_user_id != _user.id:
        caller_role = await get_org_role(org_id, _user, db)
        order = {"member": 0, "admin": 1, "owner": 2}
        # Owners may remove anyone (peers included); everyone else must strictly
        # outrank the target.
        if caller_role != "owner" and order.get(member.org_role, 0) >= order.get(caller_role, 0):
            raise HTTPException(
                status_code=403,
                detail="Sie können nur Mitglieder mit niedrigerer Rolle entfernen.",
            )

    if member.org_role == "owner" and await _locked_owner_count(org_id, db) <= 1:
        raise HTTPException(
            status_code=409,
            detail=(
                "Die Organisation benötigt mindestens einen Eigentümer — "
                "übertragen Sie zuerst die Eigentümerschaft."
            ),
        )

    await db.delete(member)
    await db.commit()
    logger.info("User %s removed member %s from org %s", _user.id, member_user_id, org_id)


# ---------------------------------------------------------------------------
# Fleet view
# ---------------------------------------------------------------------------


@router.get("/{org_id}/projects", response_model=list[ProjectResponse])
async def list_org_projects(
    org_id: UUID,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Fleet view: all projects owned by the org. ENTERPRISE feature."""
    await require_org(org_id, _user, db, min_role="member")
    if not has_feature(effective_tier(_user), Feature.FLEET_MANAGEMENT):
        raise HTTPException(
            status_code=403,
            detail="Die Flottenübersicht erfordert den ENTERPRISE-Tarif.",
        )
    role = await get_org_role(org_id, _user, db)
    # org owner/admin -> 'owner' on every org project; member -> 'editor'
    derived = "owner" if role in ("owner", "admin") else "editor"
    result = await db.execute(
        select(Project).where(Project.org_id == org_id).order_by(Project.created_at.desc())
    )
    projects = result.scalars().all()
    for p in projects:
        p.access_role = "owner" if p.user_id == _user.id else derived  # type: ignore[attr-defined]
    return projects


# ---------------------------------------------------------------------------
# Org invitations
# ---------------------------------------------------------------------------


@router.post("/{org_id}/invitations", response_model=InvitationResponse, status_code=201)
async def create_org_invitation(
    org_id: UUID,
    data: OrgInvitationCreate,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Invite a user to the org by email. Admins may invite members; only the
    OWNER may invite admins. Response is identical whether or not the email has
    an account (anti-enumeration) — no user lookup in the response path."""
    await require_org(org_id, _user, db, min_role="admin")
    if data.role == "admin":
        caller_role = await get_org_role(org_id, _user, db)
        if caller_role != "owner":
            raise HTTPException(
                status_code=403,
                detail="Nur der Organisations-Eigentümer kann Administratoren einladen.",
            )

    email = normalize_email(data.email)

    # Abuse cap
    if await count_pending_from_inviter(db, _user.id) >= MAX_PENDING_PER_INVITER:
        raise HTTPException(
            status_code=429,
            detail=(
                "Zu viele offene Einladungen — bitte warten Sie, bis "
                "bestehende angenommen wurden oder ablaufen."
            ),
        )

    # Conflicts the inviter can already see (member/invite lists) — no new leak:
    existing_member = await db.execute(
        select(OrganizationMember)
        .join(User, OrganizationMember.user_id == User.id)
        .where(
            OrganizationMember.organization_id == org_id,
            func.lower(User.email) == email,
        )
    )
    if existing_member.first():
        raise HTTPException(
            status_code=409, detail="Diese E-Mail ist bereits Mitglied der Organisation."
        )

    dup = await db.execute(
        select(Invitation).where(
            Invitation.organization_id == org_id,
            Invitation.email == email,
            Invitation.status == "pending",
        )
    )
    if dup.first():
        raise HTTPException(
            status_code=409,
            detail="Für diese E-Mail liegt bereits eine offene Einladung vor.",
        )

    inv = Invitation(
        email=email, organization_id=org_id, role=data.role,
        invited_by_user_id=_user.id, status="pending", expires_at=invitation_expiry(),
    )
    db.add(inv)
    await db.commit()
    await db.refresh(inv)
    logger.info("User %s invited %s to org %s (role=%s)", _user.id, email, org_id, data.role)
    return InvitationResponse(**await build_invitation_response(inv, db))


@router.get("/{org_id}/invitations", response_model=list[InvitationResponse])
async def list_org_invitations(
    org_id: UUID,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    await require_org(org_id, _user, db, min_role="admin")
    result = await db.execute(
        select(Invitation)
        .where(Invitation.organization_id == org_id, Invitation.status == "pending")
        .order_by(Invitation.created_at.desc())
    )
    return [
        InvitationResponse(**await build_invitation_response(inv, db))
        for inv in result.scalars().all()
    ]


@router.delete("/{org_id}/invitations/{invitation_id}", status_code=204)
async def revoke_org_invitation(
    org_id: UUID,
    invitation_id: UUID,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    await require_org(org_id, _user, db, min_role="admin")
    result = await db.execute(
        select(Invitation).where(
            Invitation.id == invitation_id,
            Invitation.organization_id == org_id,
        )
    )
    inv = result.scalar_one_or_none()
    if not inv:
        raise HTTPException(status_code=404, detail="Einladung nicht gefunden")
    inv.status = "revoked"
    await db.commit()


# ---------------------------------------------------------------------------
# Platform-admin tier control (the ONLY way org.tier changes)
# ---------------------------------------------------------------------------

admin_router = APIRouter(prefix="/admin/orgs", tags=["organizations"])


@admin_router.post("/{org_id}/tier", response_model=OrganizationResponse)
async def set_org_tier(
    org_id: UUID,
    data: OrgTierUpdate,
    _user: User = Depends(require_role("admin")),
    db: AsyncSession = Depends(get_db),
):
    """Set an organization's tier — PLATFORM ADMIN ONLY.

    This is the sole path that changes org.tier (no billing system). Making it
    self-service would let any user create an org and grant themselves
    enterprise (privilege escalation)."""
    result = await db.execute(select(Organization).where(Organization.id == org_id))
    org = result.scalar_one_or_none()
    if not org:
        raise HTTPException(status_code=404, detail="Organisation nicht gefunden")
    org.tier = data.tier
    await db.commit()
    await db.refresh(org)
    logger.info("Admin %s set org %s tier=%s", _user.id, org_id, data.tier)
    return OrganizationResponse(
        id=org.id, name=org.name, tier=org.tier, created_at=org.created_at,
        member_count=await _member_count(org.id, db),
    )
