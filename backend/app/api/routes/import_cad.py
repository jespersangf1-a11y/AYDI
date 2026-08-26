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

from app.core.permissions import get_accessible_project, get_current_user
from app.db.database import get_db
from app.models.models import Project, User
from app.schemas.schemas import CadImportResponse
from app.services.cad_import.step_parser import parse_step, parse_iges

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/projects/{project_id}", tags=["import"])

STEP_EXTENSIONS = {".step", ".stp"}
IGES_EXTENSIONS = {".iges", ".igs"}

# Upload-Obergrenze fuer CAD-Dateien — identisch zum DXF-Pfad
# (layouts.import_dxf), damit alle Import-Endpunkte dieselbe Grenze,
# denselben Statuscode (413) und dieselbe deutsche Meldung liefern.
MAX_CAD_UPLOAD_BYTES = 25 * 1024 * 1024  # 25 MB
_UPLOAD_CHUNK_BYTES = 1 * 1024 * 1024  # 1 MB


async def _read_upload_limited(file: UploadFile, max_bytes: int = MAX_CAD_UPLOAD_BYTES) -> bytes:
    """Read an upload in chunks and abort as soon as the limit is exceeded.

    Never buffers more than ``max_bytes`` + one chunk, so an oversized upload
    cannot exhaust memory before the size check runs (im Gegensatz zu einem
    unbegrenzten ``await file.read()``).
    """
    buffer = bytearray()
    while True:
        chunk = await file.read(_UPLOAD_CHUNK_BYTES)
        if not chunk:
            break
        buffer.extend(chunk)
        if len(buffer) > max_bytes:
            raise HTTPException(
                status_code=413,
                detail=f"Datei zu gross. Maximal {max_bytes // (1024 * 1024)} MB erlaubt.",
            )
    return bytes(buffer)


async def _get_project(
    project_id: UUID, user: User, db: AsyncSession, min_role: str = "editor"
) -> Project:
    """Access-checked fetch: owner or shared member with >= min_role
    (pillar 4, stage 1 — see core.permissions.get_accessible_project)."""
    return await get_accessible_project(project_id, user, db, min_role)


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
    _user: User = Depends(get_current_user),
):
    """Import a STEP file and return parsed zones/passages for review.

    The returned preview is not saved automatically. The user reviews
    and corrects zones, then confirms via POST to /layouts.
    """
    await _get_project(project_id, _user, db)
    _validate_file_extension(file.filename, STEP_EXTENSIONS, "STEP")

    content = await _read_upload_limited(file)
    if not content:
        raise HTTPException(
            status_code=400,
            detail="Leere Datei hochgeladen.",
        )

    try:
        result = parse_step(content, filename=file.filename or "model.step")
    except ValueError as e:
        logger.warning("STEP parse validation error: %s", e)
        raise HTTPException(status_code=400, detail="Ungültige STEP-Datei. Bitte Format prüfen.")
    except Exception:
        logger.exception("Unexpected error parsing STEP file")
        raise HTTPException(
            status_code=500,
            detail="Interner Fehler beim Parsen der STEP-Datei. Bitte erneut versuchen.",
        )

    return result


@router.post("/import/iges", response_model=CadImportResponse)
async def import_iges_file(
    project_id: UUID,
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    """Import an IGES file and return parsed zones/passages for review.

    The returned preview is not saved automatically. The user reviews
    and corrects zones, then confirms via POST to /layouts.
    """
    await _get_project(project_id, _user, db)
    _validate_file_extension(file.filename, IGES_EXTENSIONS, "IGES")

    content = await _read_upload_limited(file)
    if not content:
        raise HTTPException(
            status_code=400,
            detail="Leere Datei hochgeladen.",
        )

    try:
        result = parse_iges(content, filename=file.filename or "model.iges")
    except ValueError as e:
        logger.warning("IGES parse validation error: %s", e)
        raise HTTPException(status_code=400, detail="Ungültige IGES-Datei. Bitte Format prüfen.")
    except Exception:
        logger.exception("Unexpected error parsing IGES file")
        raise HTTPException(
            status_code=500,
            detail="Interner Fehler beim Parsen der IGES-Datei. Bitte erneut versuchen.",
        )

    return result
