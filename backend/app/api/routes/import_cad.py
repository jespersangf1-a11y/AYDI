"""Routes for STEP/IGES CAD file import.

Provides endpoints to upload STEP (.step/.stp) and IGES (.iges/.igs) files,
parse them into zones and passages, and return a preview for user review.
The user confirms via POST to /layouts with corrected data.
"""
import logging
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.models.models import Project
from app.schemas.schemas import CadImportResponse
from app.services.cad_import.step_parser import parse_step, parse_iges

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/projects/{project_id}", tags=["import"])

STEP_EXTENSIONS = {".step", ".stp"}
IGES_EXTENSIONS = {".iges", ".igs"}


async def _get_project(project_id: UUID, db: AsyncSession) -> Project:
    """Load and validate project existence."""
    result = await db.execute(select(Project).where(Project.id == project_id))
    project = result.scalar_one_or_none()
    if not project:
        raise HTTPException(status_code=404, detail="Projekt nicht gefunden")
    return project


def _validate_file_extension(filename: str | None, allowed: set[str], format_name: str) -> None:
    """Validate file extension against allowed set."""
    if not filename:
        raise HTTPException(
            status_code=400,
            detail=f"Dateiname fehlt. Nur {format_name}-Dateien werden unterstützt.",
        )
    ext = "." + filename.rsplit(".", 1)[-1].lower() if "." in filename else ""
    if ext not in allowed:
        raise HTTPException(
            status_code=400,
            detail=(
                f"Ungültige Dateiendung '{ext}'. "
                f"Nur {', '.join(sorted(allowed))} Dateien werden unterstützt."
            ),
        )


@router.post("/import/step", response_model=CadImportResponse)
async def import_step_file(
    project_id: UUID,
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
):
    """Import a STEP file and return parsed zones/passages for review.

    The returned preview is not saved automatically. The user reviews
    and corrects zones, then confirms via POST to /layouts.
    """
    await _get_project(project_id, db)
    _validate_file_extension(file.filename, STEP_EXTENSIONS, "STEP")

    content = await file.read()
    if not content:
        raise HTTPException(
            status_code=400,
            detail="Leere Datei hochgeladen.",
        )

    try:
        result = parse_step(content, filename=file.filename or "model.step")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.exception("Unexpected error parsing STEP file")
        raise HTTPException(
            status_code=500,
            detail=f"Fehler beim Parsen der STEP-Datei: {e}",
        )

    return result


@router.post("/import/iges", response_model=CadImportResponse)
async def import_iges_file(
    project_id: UUID,
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
):
    """Import an IGES file and return parsed zones/passages for review.

    The returned preview is not saved automatically. The user reviews
    and corrects zones, then confirms via POST to /layouts.
    """
    await _get_project(project_id, db)
    _validate_file_extension(file.filename, IGES_EXTENSIONS, "IGES")

    content = await file.read()
    if not content:
        raise HTTPException(
            status_code=400,
            detail="Leere Datei hochgeladen.",
        )

    try:
        result = parse_iges(content, filename=file.filename or "model.iges")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.exception("Unexpected error parsing IGES file")
        raise HTTPException(
            status_code=500,
            detail=f"Fehler beim Parsen der IGES-Datei: {e}",
        )

    return result
