import asyncio
import json
import logging
import os
import uuid as uuid_mod
from pathlib import Path
from uuid import UUID

from fastapi import APIRouter, BackgroundTasks, Depends, File, Form, HTTPException, UploadFile
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.permissions import effective_tier, get_accessible_project, get_current_user
from app.core.subscription import Feature, has_feature
from app.db.database import get_db
from app.models.models import ImageUpload, Project, QuickAnalysisResult, User
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
# heic dropped: unsupported downstream (analyzer MEDIA_TYPE_MAP + Claude Vision).
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "webp"}
# Aus der Konfiguration statt fest verdrahtet: MAX_IMAGE_SIZE_MB war als
# Einstellung deklariert, wurde aber nirgends gelesen — wer sie setzte,
# aenderte nichts. Eine Konfiguration, die nichts bewirkt, ist irrefuehrender
# als gar keine.
MAX_FILE_SIZE = settings.MAX_IMAGE_SIZE_MB * 1024 * 1024
MAX_BATCH_FILES = 20
# Authoritative content-based format -> stored extension (defends against
# polyglot / disguised non-image uploads that pass the filename-extension check).
_PIL_FORMAT_TO_EXT = {"JPEG": "jpg", "PNG": "png", "WEBP": "webp"}

# Version der Bildanalyse-Pipeline (Prompts + Auswertung). Wird NUR gesetzt,
# wenn tatsächlich ein Modell gelaufen ist. Das konkrete Modell steht im
# Ergebnis selbst unter ``ai_analysis["model_used"]`` — die Spalte ist auf
# 20 Zeichen begrenzt und kann eine Modell-ID nicht aufnehmen.
AI_ANALYSIS_VERSION = "1.0"

# Provenienz-Schlüssel in ``ImageUpload.metadata_extra``: wer das Bild
# hochgeladen hat. Trägt bei Schnellanalysen zusätzlich die Zugriffsprüfung.
UPLOADER_META_KEY = "uploaded_by_user_id"

# Nutzertext für das Tarif-Gate der visuellen Analyse (PRO-Feature
# VISUAL_ANALYSIS). Bewusst erklärend statt nacktem 403.
VISUAL_TIER_MESSAGE = (
    "KI-Bildanalyse ist im PRO-Tarif enthalten. Bilder lassen sich weiterhin "
    "hochladen und speichern — für die visuelle Auswertung (Pipeline B) ist "
    "ein Upgrade auf PRO erforderlich."
)


def _ensure_upload_dir() -> None:
    """Create upload directory if it does not exist."""
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


def _validate_boat_class(boat_class: str) -> None:
    """Reject unknown boat classes (mirrors the image_type validation).

    Without this an unknown class (e.g. 'u_boot') was accepted and silently
    calibrated the visual prompt against a non-existent class.
    """
    from app.schemas.schemas import BoatClass

    try:
        BoatClass(boat_class)
    except ValueError:
        valid = [c.value for c in BoatClass]
        raise HTTPException(
            status_code=400,
            detail=f"Ungültige Bootsklasse: {boat_class}. Erlaubt: {', '.join(valid)}",
        )


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


def _validate_image_bytes(content: bytes) -> str:
    """Verify the bytes decode as a supported image; return the canonical ext.

    Content-based check (structural decode via Pillow) so a non-image payload
    disguised with an image extension cannot be stored and later served
    (stored-XSS / content-sniffing). Raises 400 on failure.
    """
    from io import BytesIO

    try:
        from PIL import Image

        with Image.open(BytesIO(content)) as img:
            img.verify()  # structural validation (leaves img unusable afterwards)
        with Image.open(BytesIO(content)) as img2:
            fmt = (img2.format or "").upper()
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code=400, detail="Datei ist kein gültiges Bild.")

    ext = _PIL_FORMAT_TO_EXT.get(fmt)
    if ext is None:
        raise HTTPException(
            status_code=400,
            detail=f"Nicht unterstütztes Bildformat: {fmt or 'unbekannt'}. Erlaubt: JPEG, PNG, WEBP.",
        )
    return ext


async def _save_file(file: UploadFile) -> tuple[str, str, int]:
    """Save uploaded file and return (file_path, file_type, file_size_bytes)."""
    # Cheap early reject by filename extension.
    _extract_extension(file.filename)

    # Bounded read: never buffer more than the limit (+1 byte to detect overflow),
    # so an oversized upload cannot exhaust memory before the size check runs.
    content = await file.read(MAX_FILE_SIZE + 1)
    file_size = len(content)
    if file_size > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413,
            detail=f"Datei zu gross. Maximal {MAX_FILE_SIZE // (1024 * 1024)} MB erlaubt.",
        )
    if file_size == 0:
        raise HTTPException(status_code=400, detail="Leere Datei hochgeladen.")

    # Content is authoritative for the stored extension.
    file_type = _validate_image_bytes(content)

    _ensure_upload_dir()
    unique_name = f"{uuid_mod.uuid4()}.{file_type}"
    dest = UPLOAD_DIR / unique_name
    await asyncio.to_thread(dest.write_bytes, content)

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


def _analysis_succeeded(result: dict | None) -> bool:
    """True only when a real visual analysis ran and produced a parsed result.

    Unavailable/error results (SDK missing, API failure, unparseable response)
    carry ``analysis=None`` plus an ``error`` key. They must NOT be counted as
    successful analyses — otherwise confidence would be reported for work that
    never happened (Reliability rule: "never present uncertain results as facts").
    """
    return bool(result) and result.get("analysis") is not None and not result.get("error")


def _visual_analysis_allowed(user: User | None) -> bool:
    """Server-seitiges Tarif-Gate für Pipeline B (CLAUDE.md: require_feature an
    der Route-Grenze).

    ``None`` = anonymer Level-1-Aufruf. Anonym bedeutet kein PRO, also auch
    kein (kostenpflichtiger) Claude-Vision-Aufruf — das ist die sichere
    Auslegung. Der effektive Tarif wird gelesen, damit eine ENTERPRISE-Org die
    Analyse für ihre Mitglieder freischaltet.
    """
    if user is None:
        return False
    return has_feature(effective_tier(user), Feature.VISUAL_ANALYSIS)


def _require_visual_analysis(user: User | None) -> None:
    """Harte Sperre für Routen, deren einziger Zweck die Analyse ist."""
    if not _visual_analysis_allowed(user):
        raise HTTPException(status_code=403, detail=VISUAL_TIER_MESSAGE)


def _tier_skipped_analysis() -> dict:
    """Modul-Skip-Ergebnis für Upload-Routen: Bild wird gespeichert, die
    Analyse unterbleibt tarifbedingt — sichtbar statt stillschweigend."""
    return {"available": False, "reason": VISUAL_TIER_MESSAGE}


async def _run_visual_analysis_if_allowed(
    user: User | None,
    *,
    file_path: str,
    image_type: str,
    boat_class: str,
    zone_type: str | None = None,
    analysis_depth: str = "standard",
) -> dict | None:
    """Analyse im Thread-Pool ausführen — nie im laufenden Event-Loop.

    ``analyze_image`` ist ein synchroner Wrapper um eine Coroutine und nutzt
    intern ``asyncio.run``; direkt aufgerufen wirft er im laufenden Loop einen
    RuntimeError, der als "Analyse fehlgeschlagen" verschluckt würde.
    """
    if not _visual_analysis_allowed(user):
        return _tier_skipped_analysis()
    return await asyncio.to_thread(
        _try_visual_analysis,
        file_path=file_path,
        image_type=image_type,
        boat_class=boat_class,
        zone_type=zone_type,
        analysis_depth=analysis_depth,
    )



# ---------------------------------------------------------------------------
# Bildanalyse als Hintergrundauftrag
#
# Ein Vision-Aufruf dauert gemessen rund 60 s. Inline in der HTTP-Anfrage
# ausgefuehrt scheitert er an den ueblichen Zeitgrenzen: nginx bricht per
# Default nach 60 s ab, Browser und die PaaS-Proxys aehnlich. Der Pfad
# funktionierte lokal und waere in Produktion sporadisch umgefallen — mit einem
# Fehlerbild, das nach "API kaputt" aussieht statt nach "zu lang gewartet".
#
# Der Upload antwortet deshalb sofort; die Analyse laeuft danach weiter und
# traegt ihr Ergebnis nach. Der Zustand ist ueber ``ai_analysis_status``
# abfragbar.
# ---------------------------------------------------------------------------

ANALYSIS_PENDING = "pending"
ANALYSIS_RUNNING = "running"
ANALYSIS_DONE = "done"
ANALYSIS_FAILED = "failed"
ANALYSIS_SKIPPED_TIER = "skipped_tier"



def background_session_factory():
    """Sitzungsquelle fuer Hintergrundauftraege.

    Bewusst als Funktion und nicht als Direktimport: Der Auftrag laeuft NACH der
    Antwort, kann also nicht die Sitzung der Anfrage benutzen — und Tests, die
    ``get_db`` ueberschreiben, muessen den Hintergrundpfad auf dieselbe Datenbank
    lenken koennen. Ohne diese Indirektion schriebe der Auftrag in die real
    konfigurierte DB, waehrend der Test in einer anderen liest.
    """
    from app.db.database import async_session

    return async_session



async def _analyse_image_in_background(
    image_id: UUID,
    file_path: str,
    image_type: str,
    boat_class: str,
    zone_type: str | None,
    analysis_depth: str,
    tier_allowed: bool,
) -> None:
    """Die Analyse nachziehen, nachdem die Antwort schon raus ist.

    Nutzt eine EIGENE Datenbanksitzung: Die der Anfrage ist geschlossen, sobald
    die Antwort gesendet wurde.

    Faellt hier etwas um, darf es den Serverprozess nicht mitnehmen — der
    Nutzer hat seine Antwort bereits. Der Fehler landet im Log und als
    ``failed`` am Datensatz, damit die Oberflaeche ihn zeigen kann, statt
    ewig "laeuft noch" anzuzeigen.
    """
    async def _store(status: str, result: dict | None) -> None:
        try:
            async with background_session_factory()() as session:
                image = await session.get(ImageUpload, image_id)
                if image is None:  # zwischenzeitlich geloescht
                    return
                image.ai_analysis_status = status
                if result is not None:
                    image.ai_analysis = result
                    image.ai_analysis_version = (
                        AI_ANALYSIS_VERSION if _analysis_succeeded(result) else None
                    )
                await session.commit()
        except Exception:
            logger.exception("Bildanalyse-Status fuer %s nicht speicherbar", image_id)

    if not tier_allowed:
        await _store(ANALYSIS_SKIPPED_TIER, _tier_skipped_analysis())
        return

    await _store(ANALYSIS_RUNNING, None)
    try:
        result = await asyncio.to_thread(
            _try_visual_analysis,
            file_path=file_path,
            image_type=image_type,
            boat_class=boat_class,
            zone_type=zone_type,
            analysis_depth=analysis_depth,
        )
    except Exception:
        logger.exception("Bildanalyse fuer %s fehlgeschlagen", image_id)
        await _store(ANALYSIS_FAILED, None)
        return

    await _store(
        ANALYSIS_DONE if _analysis_succeeded(result) else ANALYSIS_FAILED,
        result,
    )


async def _assert_quick_analysis_claim(
    quick_analysis_id: UUID, user: User, db: AsyncSession
) -> None:
    """SEC-12: Bezug zwischen Aufrufer und Schnellanalyse prüfen.

    ``quick_analysis_results`` trägt keine Nutzer-Spalte — Level 1 ist bewusst
    anonym. Ein echter Eigentümer-Bezug ist ohne Schema-Erweiterung nicht
    möglich, deshalb gilt Erst-Beanspruchung: der erste Upload hinterlegt die
    Nutzer-ID in der Bild-Provenienz; danach dürfen nur noch dieselben
    Nutzer:innen Bilder an diese Schnellanalyse hängen. Fremde Konten mit
    Kenntnis der ID können so keine Bilder mehr unterschieben.
    """
    result = await db.execute(
        select(ImageUpload.metadata_extra)
        .where(ImageUpload.quick_analysis_id == quick_analysis_id)
        .order_by(ImageUpload.uploaded_at.asc())
    )
    for (meta,) in result.all():
        claimant = (meta or {}).get(UPLOADER_META_KEY)
        if not claimant:
            continue
        if claimant != str(user.id):
            raise HTTPException(
                status_code=403,
                detail=(
                    "Diese Schnellanalyse ist bereits einem anderen Konto "
                    "zugeordnet. Bilder lassen sich nur an eigene "
                    "Schnellanalysen anhängen."
                ),
            )
        return


async def _get_project(
    project_id: UUID, user: User, db: AsyncSession, min_role: str = "editor"
) -> Project:
    """Access-checked fetch: owner or shared member with >= min_role
    (pillar 4, stage 1 — see core.permissions.get_accessible_project)."""
    return await get_accessible_project(project_id, user, db, min_role)


# ---------------------------------------------------------------------------
# POST /images/analyze — standalone image analysis
# ---------------------------------------------------------------------------


@router.post("/images/analyze", response_model=ImageUploadResponse, status_code=201)
async def analyze_image_standalone(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    image_type: str = Form(...),
    boat_class: str = Form(...),
    zone_type: str | None = Form(None),
    analysis_depth: str = Form("standard"),
    tags: str | None = Form(None),
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Upload a single image, run visual analysis, return results."""
    # Diese Route existiert nur zur Analyse -> harte Tarif-Sperre VOR dem
    # Upload (SEC-4). Ohne sie lösen FREE-Konten unbegrenzt kostenpflichtige
    # Claude-Vision-Aufrufe aus.
    _require_visual_analysis(_user)

    # Validate image_type enum
    try:
        ImageType(image_type)
    except ValueError:
        valid = [t.value for t in ImageType]
        raise HTTPException(
            status_code=400,
            detail=f"Ungültiger Bildtyp: {image_type}. Erlaubt: {', '.join(valid)}",
        )
    _validate_boat_class(boat_class)

    file_path, file_type, file_size = await _save_file(file)

    metadata = await asyncio.to_thread(_extract_image_metadata, file_path)

    # Die Analyse laeuft NACH der Antwort (siehe _analyse_image_in_background).
    tier_allowed = _visual_analysis_allowed(_user)

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
        ai_analysis=None,
        # Erst die fertige Analyse bekommt Ergebnis und Version (ROB-8).
        ai_analysis_version=None,
        ai_analysis_status=ANALYSIS_PENDING if tier_allowed else ANALYSIS_SKIPPED_TIER,
        metadata_extra={**(metadata or {}), UPLOADER_META_KEY: str(_user.id)},
    )
    db.add(image)
    await db.commit()
    await db.refresh(image)
    background_tasks.add_task(
        _analyse_image_in_background,
        image_id=image.id,
        file_path=file_path,
        image_type=image_type,
        boat_class=boat_class,
        zone_type=zone_type,
        analysis_depth=analysis_depth,
        tier_allowed=tier_allowed,
    )
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
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    image_type: str = Form(...),
    zone_name: str | None = Form(None),
    deck_number: int | None = Form(None),
    tags: str | None = Form(None),
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Upload an image linked to a specific project."""
    project = await _get_project(project_id, _user, db)

    try:
        ImageType(image_type)
    except ValueError:
        valid = [t.value for t in ImageType]
        raise HTTPException(
            status_code=400,
            detail=f"Ungültiger Bildtyp: {image_type}. Erlaubt: {', '.join(valid)}",
        )

    file_path, file_type, file_size = await _save_file(file)
    metadata = await asyncio.to_thread(_extract_image_metadata, file_path)

    # Zweck dieser Route ist die Ablage am Projekt; die Analyse ist Zugabe.
    # Deshalb weiches Gate: FREE darf hochladen, die kostenpflichtige Analyse
    # unterbleibt aber sichtbar (SEC-4).
    # Die Analyse laeuft NACH der Antwort (siehe _analyse_image_in_background).
    tier_allowed = _visual_analysis_allowed(_user)

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
        ai_analysis=None,
        ai_analysis_version=None,
        ai_analysis_status=ANALYSIS_PENDING if tier_allowed else ANALYSIS_SKIPPED_TIER,
        metadata_extra={**(metadata or {}), UPLOADER_META_KEY: str(_user.id)},
    )
    db.add(image)
    await db.commit()
    await db.refresh(image)
    background_tasks.add_task(
        _analyse_image_in_background,
        image_id=image.id,
        file_path=file_path,
        image_type=image_type,
        boat_class=project.boat_class,
        zone_type=zone_name,
        analysis_depth="standard",
        tier_allowed=tier_allowed,
    )
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
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """List all images for a project, optionally filtered by image_type."""
    await _get_project(project_id, _user, db, min_role="viewer")

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
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Upload multiple images and get a combined visual assessment."""
    # Reine Analyse-Route -> harte Tarif-Sperre vor jedem Upload (SEC-4).
    _require_visual_analysis(_user)
    _validate_boat_class(boat_class)
    if not files:
        raise HTTPException(status_code=400, detail="Keine Dateien hochgeladen.")
    if len(files) > MAX_BATCH_FILES:
        raise HTTPException(
            status_code=400,
            detail=f"Zu viele Dateien. Maximal {MAX_BATCH_FILES} pro Batch.",
        )

    all_findings = []
    all_positives = []
    all_concerns = []
    all_recommendations = []
    images_saved = 0
    images_analyzed = 0
    images_rejected = 0
    scores_sum: dict[str, list[float]] = {}

    for file in files:
        try:
            file_path, file_type, file_size = await _save_file(file)
        except HTTPException:
            images_rejected += 1
            continue

        metadata = await asyncio.to_thread(_extract_image_metadata, file_path)

        ai_result = await asyncio.to_thread(
            _try_visual_analysis,
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
            ai_analysis_version=AI_ANALYSIS_VERSION if _analysis_succeeded(ai_result) else None,
            metadata_extra={**(metadata or {}), UPLOADER_META_KEY: str(_user.id)},
        )
        db.add(image)
        images_saved += 1

        # Only a real, parsed analysis counts toward the reported confidence.
        # A saved-but-unanalyzed image (SDK unavailable / API error) must never
        # inflate the confidence tier.
        if _analysis_succeeded(ai_result):
            images_analyzed += 1
            analysis = ai_result.get("analysis") or {}
            score = ai_result.get("score")
            if isinstance(score, (int, float)):
                scores_sum.setdefault("overall", []).append(float(score))
            all_findings.extend(analysis.get("findings", []) or [])
            all_positives.extend(analysis.get("positive_aspects", []) or [])
            all_concerns.extend(analysis.get("concerns", []) or [])
            all_recommendations.extend(analysis.get("recommendations", []) or [])

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
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Upload an image linked to a quick analysis result."""
    result = await db.execute(
        select(QuickAnalysisResult).where(QuickAnalysisResult.id == quick_analysis_id)
    )
    qa = result.scalar_one_or_none()
    if not qa:
        raise HTTPException(status_code=404, detail="Schnellanalyse nicht gefunden")

    # SEC-12: nur der Erst-Uploader darf weitere Bilder anhängen.
    await _assert_quick_analysis_claim(quick_analysis_id, _user, db)

    try:
        ImageType(image_type)
    except ValueError:
        valid = [t.value for t in ImageType]
        raise HTTPException(
            status_code=400,
            detail=f"Ungültiger Bildtyp: {image_type}. Erlaubt: {', '.join(valid)}",
        )

    file_path, file_type, file_size = await _save_file(file)
    metadata = await asyncio.to_thread(_extract_image_metadata, file_path)

    # ROB-7: der synchrone Analyzer-Wrapper MUSS in einen Thread — direkt im
    # laufenden Event-Loop scheiterte er bisher an ``asyncio.run`` und die
    # Route meldete trotzdem 201, ohne dass Pipeline B je gelaufen wäre.
    ai_result = await _run_visual_analysis_if_allowed(
        _user,
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
        ai_analysis_version=AI_ANALYSIS_VERSION if _analysis_succeeded(ai_result) else None,
        # Provenienz + Erst-Beanspruchung dieser Schnellanalyse (SEC-12).
        metadata_extra={**(metadata or {}), UPLOADER_META_KEY: str(_user.id)},
    )
    db.add(image)
    await db.commit()
    await db.refresh(image)
    return image
