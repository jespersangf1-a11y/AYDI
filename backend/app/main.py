import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import auth, benchmarks, collaborate, community, competitors, costs, images, import_cad, layouts, materials, projects, quick_analysis, reports, service_reports, structural_items, versions
from app.core.config import settings
from app.db.database import engine
from app.models.models import Base

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables on startup
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("Database tables created")

    # Seed data if empty
    from app.db.seed import seed
    await seed()

    yield


app = FastAPI(
    title="AYDI",
    description="AI Yacht Design Intelligence",
    version="0.1.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
