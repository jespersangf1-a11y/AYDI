import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import (
    auth,
    benchmarks,
    collaborate,
    community,
    competitors,
    costs,
    images,
    import_cad,
    knowledge,
    layouts,
    materials,
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
    logger.info("AYDI starting up (json_logs=%s)", settings.LOG_JSON)

    # Loud warning if the app is running with the repo-public default signing key.
    # In ENVIRONMENT=production this is already a hard boot failure (see config.py);
    # here we surface it for dev/staging so it never silently reaches production.
    if settings.uses_default_secret:
        logger.warning(
            "SECRET_KEY is the built-in default — auth tokens are forgeable with the "
            "public repo value. Set a strong SECRET_KEY before any real deployment."
        )

    # Seed reference data if tables are empty
    from app.db.seed import seed
    await seed()

    yield
    logger.info("AYDI shutting down")


app = FastAPI(
    title="AYDI",
    description="AI Yacht Design Intelligence",
    version="0.2.0",
    lifespan=lifespan,
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
