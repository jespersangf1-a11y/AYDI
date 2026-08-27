import logging
import math
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.api.routes import (
    auth,
    benchmarks,
    collaborate,
    community,
    competitors,
    costs,
    images,
    import_cad,
    invitations,
    knowledge,
    layouts,
    materials,
    organizations,
    projects,
    quick_analysis,
    reports,
    service_reports,
    structural_items,
    versions,
)
from app.core.config import settings
from app.core.logging import setup_logging
from app.core.middleware import register_middleware

# Initialize logging FIRST so subsequent module imports inherit handlers.
setup_logging(level=settings.LOG_LEVEL, json_format=settings.LOG_JSON)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Schema is managed by Alembic — see backend/migrations/.
    # Dev: `alembic upgrade head` before starting uvicorn.
    # Docker: docker/entrypoint.sh runs it automatically.
    #
    # Bewusst KEIN Base.metadata.create_all und kein sync_schema hier: Alembic
    # ist die eine Quelle für das Schema. Ein zweiter Weg, der Tabellen und
    # Spalten anlegt, lässt beide auseinanderlaufen — genau die Doppelung,
    # die diese Zusammenführung sonst neu entstehen liesse.
    logger.info("AYDI starting up (json_logs=%s)", settings.LOG_JSON)

    # Loud warning if the app is running with the repo-public default signing key.
    # In ENVIRONMENT=production this is already a hard boot failure (see config.py);
    # here we surface it for dev/staging so it never silently reaches production.
    if settings.uses_default_secret:
        logger.warning(
            "SECRET_KEY is the built-in default — auth tokens are forgeable with the "
            "public repo value. Set a strong SECRET_KEY before any real deployment."
        )

    # Einmalige Datenreparaturen. Sie betreffen Zeilen, nicht das Schema, und
    # sind unabhängig davon, wie das Schema entstanden ist:
    #   * Zeilen, die verwaist zurückblieben, solange SQLite die Fremdschlüssel
    #     noch nicht durchsetzte. Sie sind über die API ohnehin unerreichbar,
    #     blockieren aber jede spätere Integritätsprüfung.
    #   * Geometrie mit NaN/Infinity aus der Zeit vor der Eingabeprüfung:
    #     Starlette schreibt mit allow_nan=False, eine einzige solche Zeile
    #     liess die ganze Layout-Liste des Projekts im Serverfehler enden.
    # Beide sind idempotent und danach ein No-op.
    from app.db.database import engine
    from app.db.schema_sync import purge_orphans, repair_nonfinite_geometry

    async with engine.begin() as conn:
        await conn.run_sync(purge_orphans)
        await conn.run_sync(repair_nonfinite_geometry)

    # Seed reference data if tables are empty
    from app.db.seed import seed
    await seed()

    # Warm the markdown knowledge corpus BEFORE serving traffic: the lazy
    # first parse takes ~15s for ~840K lines and would otherwise run inside
    # the first (now public) knowledge request, freezing the event loop —
    # including /health — right after every restart.
    import asyncio as _asyncio
    from app.services.knowledge.markdown_knowledge_loader import (
        get_markdown_knowledge as _warm_corpus,
    )
    docs = await _asyncio.to_thread(_warm_corpus)
    logger.info("Knowledge corpus warmed: %d documents", len(docs))

    yield
    logger.info("AYDI shutting down")


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

# CORS middleware (must be outermost for preflight handling).
# With cookie auth, allow_credentials=True and allow_origins must NOT be ["*"];
# X-CSRF-Token must be in the allow_headers list so the frontend can echo
# back the double-submit token on mutating requests.
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type", "Accept-Language", "X-CSRF-Token", "X-Request-ID"],
    expose_headers=["X-Request-ID", "X-Response-Time"],
)


def _ohne_unendlich(wert):
    """Ersetze NaN/Infinity rekursiv durch ihren Namen als Zeichenkette.

    FastAPI legt in eine Validierungsmeldung den beanstandeten Wert selbst mit
    hinein ("input"). Genau der ist bei diesen Fällen aber NaN oder Infinity —
    und Starlette serialisiert mit ``allow_nan=False``. Die Antwort liess sich
    deshalb nicht schreiben: statt der 422 mit der Begründung bekam der
    Aufrufer einen Serverfehler und erfuhr nicht, was an seiner Eingabe falsch
    war. Die Schranke im Schema griff also, nur die Auskunft darüber ging
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


# Register AYDI middleware: request-id, timing, error handling, rate limit, csrf, locale
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
app.include_router(organizations.router, prefix="/api/v1")
app.include_router(organizations.admin_router, prefix="/api/v1")
app.include_router(invitations.router, prefix="/api/v1")


@app.get("/health/live")
async def health_live():
    """Liveness probe — process is up. No external dependencies checked."""
    return {"status": "alive"}


@app.get("/health/ready")
async def health_ready():
    """Readiness probe — process is up AND able to reach the database."""
    from sqlalchemy import text
    from app.db.database import engine
    try:
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
        return {"status": "ready", "db": "ok"}
    except Exception as exc:  # noqa: BLE001
        # Detail stays in the logs — an unauthenticated probe must not receive
        # raw DB/driver error text (host/port/driver internals).
        logger.warning("Readiness check failed: %s", exc)
        return {"status": "not_ready", "db": "error"}


# Backward-compatible alias for legacy probes / load balancers
@app.get("/health")
async def health_check():
    return {"status": "healthy"}
