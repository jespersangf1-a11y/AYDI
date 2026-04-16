# backend/app/api/routes/versions.py
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.permissions import get_current_user
from app.db.database import get_db
from app.models.models import Layout, LayoutVersion, Project, User
from app.schemas.versions import LayoutVersionCreate, LayoutVersionResponse
from app.services.diff.layout_diff import compute_layout_diff

router = APIRouter(prefix="/projects/{project_id}", tags=["versions"])


async def _verify_project_ownership(
    project_id: UUID,
    user: User,
    db: AsyncSession,
) -> None:
    """Verify the project exists and belongs to the given user."""
    result = await db.execute(
        select(Project).where(Project.id == project_id, Project.user_id == user.id)
    )
    if not result.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="Projekt nicht gefunden")


async def _get_layout_or_404(
    project_id: UUID,
    layout_id: UUID,
    db: AsyncSession,
) -> Layout:
    """Verify layout exists and belongs to the given project."""
    result = await db.execute(
        select(Layout).where(Layout.id == layout_id, Layout.project_id == project_id)
    )
    layout = result.scalar_one_or_none()
    if not layout:
        raise HTTPException(status_code=404, detail="Layout nicht gefunden")
    return layout


@router.get(
    "/layouts/{layout_id}/versions",
    response_model=list[LayoutVersionResponse],
)
async def list_versions(
    project_id: UUID,
    layout_id: UUID,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    await _verify_project_ownership(project_id, _user, db)
    await _get_layout_or_404(project_id, layout_id, db)

    result = await db.execute(
        select(LayoutVersion)
        .where(LayoutVersion.layout_id == layout_id)
        .order_by(LayoutVersion.version_number.desc())
    )
    return result.scalars().all()


@router.post(
    "/layouts/{layout_id}/versions",
    response_model=LayoutVersionResponse,
    status_code=201,
)
async def create_version(
    project_id: UUID,
    layout_id: UUID,
    data: LayoutVersionCreate,
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    await _verify_project_ownership(project_id, _user, db)
    await _get_layout_or_404(project_id, layout_id, db)

    # Auto-increment version_number: max existing + 1, default 1
    result = await db.execute(
        select(func.max(LayoutVersion.version_number)).where(
            LayoutVersion.layout_id == layout_id
        )
    )
    max_version = result.scalar_one_or_none()
    next_version_number = (max_version or 0) + 1

    version = LayoutVersion(
        layout_id=layout_id,
        version_number=next_version_number,
        **data.model_dump(),
    )
    db.add(version)
    await db.commit()
    await db.refresh(version)
    return version


@router.get(
    "/layouts/{layout_id}/versions/{version_id}",
    response_model=LayoutVersionResponse,
)
async def get_version(
    project_id: UUID,
    layout_id: UUID,
    version_id: UUID,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    await _verify_project_ownership(project_id, _user, db)
    await _get_layout_or_404(project_id, layout_id, db)

    result = await db.execute(
        select(LayoutVersion).where(
            LayoutVersion.id == version_id,
            LayoutVersion.layout_id == layout_id,
        )
    )
    version = result.scalar_one_or_none()
    if not version:
        raise HTTPException(status_code=404, detail="Version nicht gefunden")
    return version


@router.get("/layouts/{layout_id}/diff")
async def diff_versions(
    project_id: UUID,
    layout_id: UUID,
    a: UUID = Query(..., description="Version A (Basis)"),
    b: UUID = Query(..., description="Version B (Neu)"),
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Compute a structured diff between two layout versions."""
    await _verify_project_ownership(project_id, _user, db)
    await _get_layout_or_404(project_id, layout_id, db)

    result_a = await db.execute(
        select(LayoutVersion).where(
            LayoutVersion.id == a, LayoutVersion.layout_id == layout_id
        )
    )
    version_a = result_a.scalar_one_or_none()
    if not version_a:
        raise HTTPException(status_code=404, detail="Version A nicht gefunden")

    result_b = await db.execute(
        select(LayoutVersion).where(
            LayoutVersion.id == b, LayoutVersion.layout_id == layout_id
        )
    )
    version_b = result_b.scalar_one_or_none()
    if not version_b:
        raise HTTPException(status_code=404, detail="Version B nicht gefunden")

    diff = compute_layout_diff(
        {"zones": version_a.zones_snapshot or [], "passages": version_a.passages_snapshot or []},
        {"zones": version_b.zones_snapshot or [], "passages": version_b.passages_snapshot or []},
    )
    return diff
