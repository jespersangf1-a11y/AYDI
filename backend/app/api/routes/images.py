import json
import logging
import os
import uuid as uuid_mod
from pathlib import Path
from uuid import UUID

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.models.models import ImageUpload, Project, QuickAnalysisResult
from app.schemas.images import (
    BatchAnalysisRequest,
    BatchAnalysisResponse,
    ImageAnalysisResponse,
    ImageType,
    ImageUploadResponse,
    VisualConfidence,
)

logger = logging.getLogger(__name__)

router = APIRouter(tags=["images"])

UPLOAD_DIR = Path(__file__).resolve().parents[3] / "uploads" / "images"
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "heic", "webp"}
MAX_FILE_SIZE = 20 * 1024 * 1024  # 20 MB


def _ensure_upload_dir() -> None:
    """Create upload directory if it does not exist."""
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


def _extract_extension(filename: str | None) -> str:
    """Extract and validate file extension."""
    if not filename:
        raise HTTPException(
            status_code=400,
            detail="Dateiname fehlt.",
        )
    ext = filename.rsplit(".", 1)[-1].lower() if "." in filename else ""
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Nicht unterstütztes Dateiformat: .{ext}. Erlaubt: {', '.join(sorted(ALLOWED_EXTENSIONS))}",
        )
    return ext


def _normalise_extension(ext: str) -> str:
    """Normalise jpeg -> jpg for consistency."""
    return "jpg" if ext == "jpeg" else ext


async def _save_file(file: UploadFile) -> tuple[str, str, int]:
    """Save uploaded file and return (file_path, file_type, file_size_bytes)."""
    ext = _extract_extension(file.filename)
    file_type = _normalise_extension(ext)

    content = await file.read()
    file_size = len(content)

    if file_size > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail=f"Datei zu gross. Maximal {MAX_FILE_SIZE // (1024 * 1024)} MB erlaubt.",
        )
    if file_size == 0:
        raise HTTPException(status_code=400, detail="Leere Datei hochgeladen.")

    _ensure_upload_dir()
    unique_name = f"{uuid_mod.uuid4()}.{file_type}"
    dest = UPLOAD_DIR / unique_name
    dest.write_bytes(content)

    return str(dest), file_type, file_size


def _extract_image_metadata(file_path: str) -> dict | None:
    """Try to extract basic image metadata via Pillow. Returns None on failure."""
    try:
        from PIL import Image

        with Image.open(file_path) as img:
            meta: dict = {
                "width": img.width,
                "height": img.height,
                "format": img.format,
                "mode": img.mode,
            }
            # Try to get EXIF data
            exif = img.getexif()
            if exif:
                exif_data = {}
                for tag_id, value in exif.items():
                    try:
                        exif_data[str(tag_id)] = str(value)
                    except Exception:
                        pass
                if exif_data:
                    meta["exif"] = exif_data
            return meta
    except Exception as exc:
        logger.debug("Bild-Metadaten konnten nicht extrahiert werden: %s", exc)
        return None


def _try_visual_analysis(
    file_path: str,
    image_type: str,
    boat_class: str,
    zone_type: str | None = None,
    analysis_depth: str = "standard",
) -> dict | None:
    """Attempt to run visual analysis. Returns None if analyzer is not available."""
    try:
        from app.services.visual.analyzer import analyze_image

        return analyze_image(
            file_path=file_path,
            image_type=image_type,
            boat_class=boat_class,
            zone_type=zone_type,
            analysis_depth=analysis_depth,
        )
    except ImportError:
        logger.info("Visual-Analyse-Modul nicht verfügbar, Bild wird ohne Analyse gespeichert.")
        return None
    except Exception as exc:
        logger.warning("Visual-Analyse fehlgeschlagen: %s", exc)
        return None


async def _get_project(project_id: UUID, db: AsyncSession) -> Project:
    result = await db.execute(select(Project).where(Project.id == project_id))
    project = result.scalar_one_or_none()
    if not project:
        raise HTTPException(status_code=404, detail="Projekt nicht gefunden")
    return project


# ---------------------------------------------------------------------------
# POST /images/analyze — standalone image analysis
# ---------------------------------------------------------------------------


@router.post("/images/analyze", response_model=ImageUploadResponse, status_code=201)
async def analyze_image_standalone(
    file: UploadFile = File(...),
    image_type: str = Form(...),
    boat_class: str = Form(...),
    zone_type: str | None = Form(None),
    analysis_depth: str = Form("standard"),
    tags: str | None = Form(None),
    db: AsyncSession = Depends(get_db),
):
    """Upload a single image, run visual analysis, return results."""
    # Validate image_type enum
    try:
        ImageType(image_type)
    except ValueError:
        valid = [t.value for t in ImageType]
        raise HTTPException(
            status_code=400,
            detail=f"Ungültiger Bildtyp: {image_type}. Erlaubt: {', '.join(valid)}",
        )

    file_path, file_type, file_size = await _save_file(file)

    metadata = _extract_image_metadata(file_path)

    ai_result = _try_visual_analysis(
        file_path=file_path,
        image_type=image_type,
        boat_class=boat_class,
        zone_type=zone_type,
        analysis_depth=analysis_depth,
    )

    parsed_tags = None
    if tags:
        try:
            parsed_tags = json.loads(tags)
        except json.JSONDecodeError:
            parsed_tags = [t.strip() for t in tags.split(",") if t.strip()]

    image = ImageUpload(
        file_path=file_path,
        file_type=file_type,
        file_size_bytes=file_size,
        image_type=image_type,
        zone_name=zone_type,
        tags=parsed_tags,
        ai_analysis=ai_result,
        ai_analysis_version="1.0" if ai_result else None,
        metadata_extra=metadata,
    )
    db.add(image)
    await db.commit()
    await db.refresh(image)
    return image


# ---------------------------------------------------------------------------
# POST /projects/{pid}/images — upload image linked to project
# ---------------------------------------------------------------------------


@router.post(
    "/projects/{project_id}/images",
    response_model=ImageUploadResponse,
    status_code=201,
)
async def upload_project_image(
    project_id: UUID,
    file: UploadFile = File(...),
    image_type: str = Form(...),
    zone_name: str | None = Form(None),
    deck_number: int | None = Form(None),
    tags: str | None = Form(None),
    db: AsyncSession = Depends(get_db),
):
    """Upload an image linked to a specific project."""
    project = await _get_project(project_id, db)

    try:
        ImageType(image_type)
    except ValueError:
        valid = [t.value for t in ImageType]
        raise HTTPException(
            status_code=400,
            detail=f"Ungültiger Bildtyp: {image_type}. Erlaubt: {', '.join(valid)}",
        )

    file_path, file_type, file_size = await _save_file(file)
    metadata = _extract_image_metadata(file_path)

    ai_result = _try_visual_analysis(
        file_path=file_path,
        image_type=image_type,
        boat_class=project.boat_class,
        zone_type=zone_name,
    )

    parsed_tags = None
    if tags:
        try:
            parsed_tags = json.loads(tags)
        except json.JSONDecodeError:
            parsed_tags = [t.strip() for t in tags.split(",") if t.strip()]

    image = ImageUpload(
        project_id=project_id,
        file_path=file_path,
        file_type=file_type,
        file_size_bytes=file_size,
        image_type=image_type,
        zone_name=zone_name,
        deck_number=deck_number,
        tags=parsed_tags,
        ai_analysis=ai_result,
        ai_analysis_version="1.0" if ai_result else None,
        metadata_extra=metadata,
    )
    db.add(image)
    await db.commit()
    await db.refresh(image)
    return image


# ---------------------------------------------------------------------------
# GET /projects/{pid}/images — list project images
# ---------------------------------------------------------------------------


@router.get(
    "/projects/{project_id}/images",
    response_model=list[ImageUploadResponse],
)
async def list_project_images(
    project_id: UUID,
    image_type: str | None = None,
    db: AsyncSession = Depends(get_db),
):
    """List all images for a project, optionally filtered by image_type."""
    await _get_project(project_id, db)

    query = select(ImageUpload).where(ImageUpload.project_id == project_id)
    if image_type:
        query = query.where(ImageUpload.image_type == image_type)
    query = query.order_by(ImageUpload.uploaded_at.desc())

    result = await db.execute(query)
    return result.scalars().all()


# ---------------------------------------------------------------------------
# POST /images/analyze-batch — multi-image batch analysis
# ---------------------------------------------------------------------------


@router.post("/images/analyze-batch", response_model=BatchAnalysisResponse, status_code=201)
async def analyze_batch(
    files: list[UploadFile] = File(...),
    boat_class: str = Form(...),
    zone_type: str | None = Form(None),
    analysis_depth: str = Form("standard"),
    db: AsyncSession = Depends(get_db),
):
    """Upload multiple images and get a combined visual assessment."""
    if not files:
        raise HTTPException(status_code=400, detail="Keine Dateien hochgeladen.")

    all_findings = []
    all_positives = []
    all_concerns = []
    all_recommendations = []
    images_analyzed = 0
    images_rejected = 0
    scores_sum: dict[str, list[float]] = {}

    for file in files:
        try:
            file_path, file_type, file_size = await _save_file(file)
        except HTTPException:
            images_rejected += 1
            continue

        metadata = _extract_image_metadata(file_path)

        ai_result = _try_visual_analysis(
            file_path=file_path,
            image_type="interior_overview",
            boat_class=boat_class,
            zone_type=zone_type,
            analysis_depth=analysis_depth,
        )

        image = ImageUpload(
            file_path=file_path,
            file_type=file_type,
            file_size_bytes=file_size,
            image_type="interior_overview",
            zone_name=zone_type,
            ai_analysis=ai_result,
            ai_analysis_version="1.0" if ai_result else None,
            metadata_extra=metadata,
        )
        db.add(image)

        if ai_result:
            images_analyzed += 1
            for key, val in ai_result.get("scores", {}).items():
                scores_sum.setdefault(key, []).append(val)
            all_findings.extend(ai_result.get("findings", []))
            all_positives.extend(ai_result.get("positive_aspects", []))
            all_concerns.extend(ai_result.get("concerns", []))
            all_recommendations.extend(ai_result.get("recommendations", []))
        else:
            images_analyzed += 1  # File saved successfully even without analysis

    await db.commit()

    # Compute fused scores
    fused_score = None
    if scores_sum:
        all_vals = [v for vals in scores_sum.values() for v in vals]
        fused_score = round(sum(all_vals) / len(all_vals), 1) if all_vals else None

    # Determine overall confidence
    if images_analyzed == 0:
        confidence = VisualConfidence.insufficient
    elif images_analyzed <= 2:
        confidence = VisualConfidence.low
    elif images_analyzed <= 5:
        confidence = VisualConfidence.medium
    else:
        confidence = VisualConfidence.high

    return BatchAnalysisResponse(
        images_analyzed=images_analyzed,
        images_rejected=images_rejected,
        fused_score=fused_score,
        confidence=confidence,
        findings=all_findings,
        positive_aspects=list(dict.fromkeys(all_positives)),  # deduplicate preserving order
        concerns=list(dict.fromkeys(all_concerns)),
        recommendations=list(dict.fromkeys(all_recommendations)),
    )


# ---------------------------------------------------------------------------
# POST /quick-analysis/{id}/images — upload image to quick analysis
# ---------------------------------------------------------------------------


@router.post(
    "/quick-analysis/{quick_analysis_id}/images",
    response_model=ImageUploadResponse,
    status_code=201,
)
async def upload_quick_analysis_image(
    quick_analysis_id: UUID,
    file: UploadFile = File(...),
    image_type: str = Form(...),
    zone_name: str | None = Form(None),
    tags: str | None = Form(None),
    db: AsyncSession = Depends(get_db),
):
    """Upload an image linked to a quick analysis result."""
    result = await db.execute(
        select(QuickAnalysisResult).where(QuickAnalysisResult.id == quick_analysis_id)
    )
    qa = result.scalar_one_or_none()
    if not qa:
        raise HTTPException(status_code=404, detail="Schnellanalyse nicht gefunden")

    try:
        ImageType(image_type)
    except ValueError:
        valid = [t.value for t in ImageType]
        raise HTTPException(
            status_code=400,
            detail=f"Ungültiger Bildtyp: {image_type}. Erlaubt: {', '.join(valid)}",
        )

    file_path, file_type, file_size = await _save_file(file)
    metadata = _extract_image_metadata(file_path)

    ai_result = _try_visual_analysis(
        file_path=file_path,
        image_type=image_type,
        boat_class=qa.boat_class,
        zone_type=zone_name,
    )

    parsed_tags = None
    if tags:
        try:
            parsed_tags = json.loads(tags)
        except json.JSONDecodeError:
            parsed_tags = [t.strip() for t in tags.split(",") if t.strip()]

    image = ImageUpload(
        quick_analysis_id=quick_analysis_id,
        file_path=file_path,
        file_type=file_type,
        file_size_bytes=file_size,
        image_type=image_type,
        zone_name=zone_name,
        tags=parsed_tags,
        ai_analysis=ai_result,
        ai_analysis_version="1.0" if ai_result else None,
        metadata_extra=metadata,
    )
    db.add(image)
    await db.commit()
    await db.refresh(image)
    return image
