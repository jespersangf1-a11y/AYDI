# backend/app/core/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite+aiosqlite:///./aydi.db"
    CORS_ORIGINS: list[str] = ["http://localhost:5173"]
    ANTHROPIC_API_KEY: str | None = None
    ANTHROPIC_MODEL: str = "claude-sonnet-4-20250514"
    VISUAL_ANALYSIS_TIMEOUT_SEC: int = 30
    DATABASE_POOL_SIZE: int = 10
    LOG_LEVEL: str = "INFO"
    MAX_IMAGE_SIZE_MB: int = 20
    UPLOAD_DIR: str = "uploads"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
