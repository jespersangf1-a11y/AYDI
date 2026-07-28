import logging
import math
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.api.routes import auth, benchmarks, collaborate, community, competitors, costs, images, import_cad, knowledge, layouts, materials, projects, quick_analysis, reports, service_reports, structural_items, versions
from app.core.config import settings
from app.core.middleware import register_middleware
from app.db.database import engine
from app.db.schema_sync import purge_orphans, repair_nonfinite_geometry, sync_schema
from app.models.models import Base

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables on startup
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        # create_all leaves existing tables untouched, so columns and indexes
        # added to a model after the database was first created never arrive.
        await conn.run_sync(sync_schema)
        # Foreign keys are enforced from now on; rows orphaned while they were
        # not would otherwise make every later integrity check fail.
        await conn.run_sync(purge_orphans)
        # Layouts, die vor der Eingabepruefung mit NaN/Infinity angelegt
        # wurden, liessen sich gar nicht mehr ausliefern — Starlette
        # serialisiert mit allow_nan=False. Einmalig entschaerfen.
        await conn.run_sync(repair_nonfinite_geometry)
    logger.info("Database tables created")

    # Seed data if empty
    from app.db.seed import seed
    await seed()

    yield


# The interactive documentation lists every route, every field and every
# validation rule of the API. That is a gift to an attacker and of no use to
# an end user, so outside development it is not served at all — including the
# raw schema at /openapi.json, which is what actually leaks the detail.
_docs_public = settings.docs_public
if not _docs_public:
    logger.info(
        "API-Dokumentation ist deaktiviert (ENVIRONMENT=%s). "
        "Zum Einschalten DOCS_ENABLED=true setzen.",
        settings.ENVIRONMENT,
    )

app = FastAPI(
    title="AYDI",
    description="AI Yacht Design Intelligence",
    version="0.2.0",
    lifespan=lifespan,
    docs_url="/docs" if _docs_public else None,
    redoc_url="/redoc" if _docs_public else None,
    openapi_url="/openapi.json" if _docs_public else None,
)

# CORS middleware (must be outermost for preflight handling)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type", "Accept-Language"],
)


def _ohne_unendlich(wert):
    """Ersetze NaN/Infinity rekursiv durch ihren Namen als Zeichenkette.

    FastAPI legt in eine Validierungsmeldung den beanstandeten Wert selbst mit
    hinein ("input"). Genau der ist bei diesen Faellen aber NaN oder Infinity —
    und Starlette serialisiert mit ``allow_nan=False``. Die Antwort liess sich
    deshalb nicht schreiben: statt der 422 mit der Begruendung bekam der
    Aufrufer einen Serverfehler und erfuhr nicht, was an seiner Eingabe falsch
    war. Die Schranke im Schema griff also, nur die Auskunft darueber ging
    verloren.
    """
    if isinstance(wert, float):
        if math.isnan(wert):
            return "NaN"
        if math.isinf(wert):
            return "Infinity" if wert > 0 else "-Infinity"
        return wert
    if isinstance(wert, dict):
        return {schluessel: _ohne_unendlich(w) for schluessel, w in wert.items()}
    if isinstance(wert, (list, tuple)):
        return [_ohne_unendlich(w) for w in wert]
    return wert


@app.exception_handler(RequestValidationError)
async def validierungsfehler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"detail": _ohne_unendlich(jsonable_encoder(exc.errors()))},
    )


# Register AYDI middleware: timing, error handling, rate limiting, locale
register_middleware(app)

# --- Routes ---
app.include_router(auth.router, prefix="/api/v1")
app.include_router(projects.router, prefix="/api/v1")
app.include_router(layouts.router, prefix="/api/v1")
app.include_router(materials.router, prefix="/api/v1")
app.include_router(service_reports.router, prefix="/api/v1")
app.include_router(costs.router, prefix="/api/v1")
app.include_router(structural_items.router, prefix="/api/v1")
app.include_router(competitors.router, prefix="/api/v1")
app.include_router(versions.router, prefix="/api/v1")
app.include_router(quick_analysis.router, prefix="/api/v1")
app.include_router(benchmarks.router, prefix="/api/v1")
app.include_router(reports.router, prefix="/api/v1")
app.include_router(collaborate.router, prefix="/api/v1")
app.include_router(images.router, prefix="/api/v1")
app.include_router(import_cad.router, prefix="/api/v1")
app.include_router(community.router, prefix="/api/v1")
app.include_router(knowledge.router, prefix="/api/v1")


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
