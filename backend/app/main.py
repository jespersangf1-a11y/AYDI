from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import layouts, projects
from app.core.config import settings

app = FastAPI(title="AYDI", description="AI Yacht Design Intelligence", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(projects.router, prefix="/api/v1")
app.include_router(layouts.router, prefix="/api/v1")


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
