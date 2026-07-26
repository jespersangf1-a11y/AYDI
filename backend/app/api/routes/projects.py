import logging
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import or_, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.invitations import (
    MAX_PENDING_PER_INVITER,
    build_invitation_response,
    count_pending_from_inviter,
    invitation_expiry,
    normalize_email,
)
from app.core.permissions import get_accessible_project, get_current_user, get_org_role
from app.db.database import get_db
from app.models.models import Invitation, Organization, Project, ProjectMember, User
from app.schemas.schemas import (
    InvitationResponse,
    ProjectCreate,
    ProjectInvitationCreate,
    ProjectMemberCreate,
    ProjectMemberResponse,
    ProjectMemberRoleUpdate,
    ProjectOrgUpdate,
    ProjectResponse,
    ProjectStatus,
    ProjectUpdate,
)
from sqlalchemy import func

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/projects", tags=["projects"])


async def _get_user_project(
    project_id: UUID, user: User, db: AsyncSession, min_role: str = "editor"
) -> Project:
    """Access-checked project fetch (owner or shared member per role)."""
    return await get_accessible_project(project_id, user, db, min_role)


async def _attach_access_role(project: Project, user: User, db: AsyncSession) -> None:
    """Populate the transient access_role attribute for the response —
    ALL ProjectResponse-returning endpoints must do this consistently.
    Delegates to the central effective-role resolver (owner / project_member /
    org-derived role — pillar 4, stage 2)."""
    from app.core.permissions import _effective_project_role

    project.access_role = await _effective_project_role(project, user, db)  # type: ignore[attr-defined]


@router.get("", response_model=list[ProjectResponse])
async def list_projects(
    status: ProjectStatus | None = None,
    limit: int = Query(50, ge=1, le=200),
    offset: int = Query(0, ge=0),
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    # Projects I can see: owned OR shared with me (project_members, stage 1)
    # OR belonging to an org I am a member of (pillar 4, stage 2).
    from app.models.models import OrganizationMember

    membership_subquery = select(ProjectMember.project_id).where(
        ProjectMember.user_id == _user.id
    )
    my_orgs_subquery = select(OrganizationMember.organization_id).where(
        OrganizationMember.user_id == _user.id
    )
    query = select(Project).where(
        or_(
            Project.user_id == _user.id,
            Project.id.in_(membership_subquery),
            Project.org_id.in_(my_orgs_subquery),
        )
    )
    if status:
        query = query.where(Project.status == status.value)
    query = query.order_by(Project.created_at.desc()).limit(limit).offset(offset)
    result = await db.execute(query)
    projects = result.scalars().all()

    # Attach the caller's effective access role for UI badges ("geteilt").
    # Precompute the two membership maps to avoid a per-project query.
    member_roles = dict(
        (
            await db.execute(
                select(ProjectMember.project_id, ProjectMember.role).where(
                    ProjectMember.user_id == _user.id
                )
            )
        ).all()
    )
    org_roles = dict(
        (
            await db.execute(
                select(OrganizationMember.organization_id, OrganizationMember.org_role).where(
                    OrganizationMember.user_id == _user.id
                )
            )
        ).all()
    )
    _order = {"viewer": 0, "editor": 1, "owner": 2}
    _rank_role = {0: "viewer", 1: "editor", 2: "owner"}
    for project in projects:
        if project.user_id == _user.id:
            project.access_role = "owner"  # type: ignore[attr-defined]
            continue
        best = -1
        pm = member_roles.get(project.id)
        if pm is not None:
            best = max(best, _order.get(pm, -1))
        if project.org_id is not None and project.org_id in org_roles:
            mapped = "owner" if org_roles[project.org_id] in ("owner", "admin") else "editor"
            best = max(best, _order[mapped])
        project.access_role = _rank_role.get(best)  # type: ignore[attr-defined]
    return projects


@router.post("", response_model=ProjectResponse, status_code=201)
async def create_project(
    data: ProjectCreate,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    project = Project(**data.model_dump(), user_id=_user.id)
    db.add(project)
    await db.commit()
    await db.refresh(project)
    project.access_role = "owner"  # type: ignore[attr-defined]
    logger.info("User %s created project %s (%s)", _user.id, project.id, data.name)
    return project


@router.get("/{project_id}", response_model=ProjectResponse)
async def get_project(
    project_id: UUID,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    project = await _get_user_project(project_id, _user, db, min_role="viewer")
    await _attach_access_role(project, _user, db)
    return project


@router.patch("/{project_id}", response_model=ProjectResponse)
async def update_project(
    project_id: UUID,
    data: ProjectUpdate,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    project = await _get_user_project(project_id, _user, db, min_role="editor")

    update_data = data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        if isinstance(value, ProjectStatus):
            value = value.value
        setattr(project, field, value)

    await db.commit()
    await db.refresh(project)
    await _attach_access_role(project, _user, db)
    logger.info("User %s updated project %s (fields: %s)", _user.id, project_id, list(update_data.keys()))
    return project


@router.delete("/{project_id}", status_code=204)
async def delete_project(
    project_id: UUID,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    # Deleting a project stays owner-only
    project = await _get_user_project(project_id, _user, db, min_role="owner")
    await db.delete(project)
    await db.commit()
    logger.info("User %s deleted project %s", _user.id, project_id)


# ---------------------------------------------------------------------------
# Project members (pillar 4, stage 1: sharing)
# ---------------------------------------------------------------------------


@router.get("/{project_id}/members", response_model=list[ProjectMemberResponse])
async def list_members(
    project_id: UUID,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Members of a project — visible to owner and members."""
    project = await _get_user_project(project_id, _user, db, min_role="viewer")

    owner_result = await db.execute(select(User).where(User.id == project.user_id))
    owner = owner_result.scalar_one_or_none()

    members_result = await db.execute(
        select(ProjectMember, User)
        .join(User, ProjectMember.user_id == User.id)
        .where(ProjectMember.project_id == project_id)
        .order_by(ProjectMember.created_at)
    )
    entries: list[ProjectMemberResponse] = []
    if owner:
        entries.append(
            ProjectMemberResponse(
                user_id=owner.id,
                email=owner.email,
                full_name=owner.full_name,
                role="owner",
            )
        )
    for member, user in members_result.all():
        entries.append(
            ProjectMemberResponse(
                user_id=user.id,
                email=user.email,
                full_name=user.full_name,
                role=member.role,
            )
        )
    return entries


@router.post(
    "/{project_id}/members",
    response_model=ProjectMemberResponse,
    status_code=201,
)
async def add_member(
    project_id: UUID,
    data: ProjectMemberCreate,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Share the project with another user (owner-only)."""
    project = await _get_user_project(project_id, _user, db, min_role="owner")

    user_result = await db.execute(select(User).where(User.email == data.email))
    target = user_result.scalar_one_or_none()
    if not target:
        raise HTTPException(
            status_code=404,
            detail=f"Kein Nutzer mit der E-Mail '{data.email}' gefunden.",
        )
    if target.id == project.user_id:
        raise HTTPException(
            status_code=409,
            detail="Der Eigentümer ist bereits Mitglied des Projekts.",
        )

    member = ProjectMember(project_id=project_id, user_id=target.id, role=data.role)
    db.add(member)
    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=409,
            detail=(
                f"'{data.email}' ist bereits Mitglied dieses Projekts. "
                "Die Rolle lässt sich im Teilen-Dialog direkt ändern."
            ),
        )
    logger.info(
        "User %s shared project %s with %s (role=%s)",
        _user.id, project_id, target.id, data.role,
    )
    return ProjectMemberResponse(
        user_id=target.id,
        email=target.email,
        full_name=target.full_name,
        role=member.role,
    )


@router.patch(
    "/{project_id}/members/{member_user_id}",
    response_model=ProjectMemberResponse,
)
async def update_member_role(
    project_id: UUID,
    member_user_id: UUID,
    data: ProjectMemberRoleUpdate,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Change a member's role in place (owner-only) — stage 2 replaces the
    stage-1 workaround of remove-then-reshare."""
    await _get_user_project(project_id, _user, db, min_role="owner")

    result = await db.execute(
        select(ProjectMember, User)
        .join(User, ProjectMember.user_id == User.id)
        .where(
            ProjectMember.project_id == project_id,
            ProjectMember.user_id == member_user_id,
        )
    )
    row = result.first()
    if not row:
        raise HTTPException(status_code=404, detail="Mitglied nicht gefunden")
    member, target = row
    member.role = data.role
    await db.commit()
    logger.info(
        "User %s changed role of member %s in project %s to %s",
        _user.id, member_user_id, project_id, data.role,
    )
    return ProjectMemberResponse(
        user_id=target.id,
        email=target.email,
        full_name=target.full_name,
        role=member.role,
    )


@router.delete("/{project_id}/members/{member_user_id}", status_code=204)
async def remove_member(
    project_id: UUID,
    member_user_id: UUID,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Revoke a member's access. Owner-only — except members may remove
    THEMSELVES (leave a shared project)."""
    if member_user_id == _user.id:
        await _get_user_project(project_id, _user, db, min_role="viewer")
    else:
        await _get_user_project(project_id, _user, db, min_role="owner")

    result = await db.execute(
        select(ProjectMember).where(
            ProjectMember.project_id == project_id,
            ProjectMember.user_id == member_user_id,
        )
    )
    member = result.scalar_one_or_none()
    if not member:
        raise HTTPException(status_code=404, detail="Mitglied nicht gefunden")
    await db.delete(member)
    await db.commit()
    logger.info("User %s removed member %s from project %s", _user.id, member_user_id, project_id)


# ---------------------------------------------------------------------------
# Organization attachment (pillar 4, stage 2)
# ---------------------------------------------------------------------------


@router.patch("/{project_id}/org", response_model=ProjectResponse)
async def set_project_org(
    project_id: UUID,
    data: ProjectOrgUpdate,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Attach a project to an org (org_id set) or detach it back to private
    (org_id null).

    Attach: only the project OWNER may donate their project, and only to an org
    they are a member of (unknown/foreign org -> 404, no org enumeration);
    already attached -> 409.
    Detach: project owner OR org owner/admin (offboarding / cleanup).
    """
    # Fetch the project directly — attach/detach has bespoke ownership rules
    # that don't map onto get_accessible_project's role ladder.
    result = await db.execute(select(Project).where(Project.id == project_id))
    project = result.scalar_one_or_none()
    if not project:
        raise HTTPException(status_code=404, detail="Projekt nicht gefunden")

    is_project_owner = project.user_id == _user.id

    if data.org_id is None:
        # Detach: project owner, or an owner/admin of the org it belongs to.
        allowed = is_project_owner
        if not allowed and project.org_id is not None:
            role = await get_org_role(project.org_id, _user, db)
            allowed = role in ("owner", "admin")
        if not allowed:
            raise HTTPException(
                status_code=403,
                detail="Nur der Projekt-Eigentümer oder eine Org-Leitung kann das Projekt lösen.",
            )
        project.org_id = None
    else:
        if not is_project_owner:
            raise HTTPException(
                status_code=403,
                detail="Nur der Projekt-Eigentümer kann das Projekt einer Organisation zuordnen.",
            )
        if project.org_id is not None:
            raise HTTPException(
                status_code=409,
                detail="Projekt gehört bereits einer Organisation — zuerst lösen.",
            )
        # Caller must be a member of the target org (any role) — else 404 so
        # org existence is not probeable.
        role = await get_org_role(data.org_id, _user, db)
        if role is None:
            raise HTTPException(status_code=404, detail="Organisation nicht gefunden")
        project.org_id = data.org_id

    await db.commit()
    await db.refresh(project)
    await _attach_access_role(project, _user, db)
    logger.info("User %s set project %s org_id=%s", _user.id, project_id, data.org_id)
    return project


# ---------------------------------------------------------------------------
# Project invitations (pillar 4, stage 2) — the anti-enumeration sharing path
# ---------------------------------------------------------------------------


@router.post("/{project_id}/invitations", response_model=InvitationResponse, status_code=201)
async def create_project_invitation(
    project_id: UUID,
    data: ProjectInvitationCreate,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Invite a user to a project by email (owner-only). The response is
    identical whether or not the email has an account — no user lookup happens
    in the response path (fixes the enumeration leak of the legacy direct-add
    endpoint). The invite is picked up by the recipient under /invitations/mine
    and takes effect only when they explicitly accept."""
    await _get_user_project(project_id, _user, db, min_role="owner")
    email = normalize_email(data.email)

    if await count_pending_from_inviter(db, _user.id) >= MAX_PENDING_PER_INVITER:
        raise HTTPException(
            status_code=429,
            detail=(
                "Zu viele offene Einladungen — bitte warten Sie, bis "
                "bestehende angenommen wurden oder ablaufen."
            ),
        )

    # Conflicts the owner can already see in the member/invite lists (no leak):
    existing_member = await db.execute(
        select(ProjectMember)
        .join(User, ProjectMember.user_id == User.id)
        .where(ProjectMember.project_id == project_id, func.lower(User.email) == email)
    )
    if existing_member.first():
        raise HTTPException(
            status_code=409, detail="Diese E-Mail hat bereits Zugriff auf dieses Projekt."
        )
    # Owner's own email
    owner_email = await db.execute(select(User.email).where(User.id == _user.id))
    if normalize_email(owner_email.scalar_one()) == email:
        raise HTTPException(
            status_code=409, detail="Der Eigentümer benötigt keine Einladung."
        )
    dup = await db.execute(
        select(Invitation).where(
            Invitation.project_id == project_id,
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
        email=email, project_id=project_id, role=data.role,
        invited_by_user_id=_user.id, status="pending", expires_at=invitation_expiry(),
    )
    db.add(inv)
    await db.commit()
    await db.refresh(inv)
    logger.info("User %s invited %s to project %s (role=%s)", _user.id, email, project_id, data.role)
    return InvitationResponse(**await build_invitation_response(inv, db))


@router.get("/{project_id}/invitations", response_model=list[InvitationResponse])
async def list_project_invitations(
    project_id: UUID,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    await _get_user_project(project_id, _user, db, min_role="owner")
    result = await db.execute(
        select(Invitation)
        .where(Invitation.project_id == project_id, Invitation.status == "pending")
        .order_by(Invitation.created_at.desc())
    )
    return [
        InvitationResponse(**await build_invitation_response(inv, db))
        for inv in result.scalars().all()
    ]


@router.delete("/{project_id}/invitations/{invitation_id}", status_code=204)
async def revoke_project_invitation(
    project_id: UUID,
    invitation_id: UUID,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    await _get_user_project(project_id, _user, db, min_role="owner")
    result = await db.execute(
        select(Invitation).where(
            Invitation.id == invitation_id,
            Invitation.project_id == project_id,
        )
    )
    inv = result.scalar_one_or_none()
    if not inv:
        raise HTTPException(status_code=404, detail="Einladung nicht gefunden")
    inv.status = "revoked"
    await db.commit()
