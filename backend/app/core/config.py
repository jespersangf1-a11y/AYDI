# backend/app/core/config.py
from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite+aiosqlite:///./aydi.db"
    # Origins allowed to call the API with credentials. Keep this to the exact
    # origins that actually serve the app — "*" is rejected outright below,
    # because combining it with allow_credentials is both forbidden by the
    # CORS spec and a genuine cross-site risk.
    CORS_ORIGINS: list[str] = [
        "http://localhost:5173",
        "http://localhost:4173",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:4173",
    ]
    # "development" keeps /docs open and CSP lenient. Anything else is treated
    # as production: interactive docs and the OpenAPI schema are closed unless
    # DOCS_ENABLED is set explicitly.
    ENVIRONMENT: str = "development"
    DOCS_ENABLED: bool | None = None
    ANTHROPIC_API_KEY: str | None = None
    ANTHROPIC_MODEL: str = "claude-sonnet-4-20250514"
    VISUAL_ANALYSIS_TIMEOUT_SEC: int = 30
    DATABASE_POOL_SIZE: int = 10
    LOG_LEVEL: str = "INFO"
    MAX_IMAGE_SIZE_MB: int = 20
    UPLOAD_DIR: str = "uploads"
    SECRET_KEY: str = "aydi-secret-key-change-in-production"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    model_config = SettingsConfigDict(env_file=".env")

    @property
    def is_production(self) -> bool:
        return self.ENVIRONMENT.lower() not in ("development", "dev", "local", "test")

    @property
    def docs_public(self) -> bool:
        """Whether /docs, /redoc and /openapi.json are served at all."""
        if self.DOCS_ENABLED is not None:
            return self.DOCS_ENABLED
        return not self.is_production

    @field_validator("CORS_ORIGINS")
    @classmethod
    def reject_wildcard_origin(cls, origins: list[str]) -> list[str]:
        if "*" in origins:
            raise ValueError(
                "CORS_ORIGINS darf kein '*' enthalten: Die API sendet Anmeldedaten, "
                "und ein Platzhalter wuerde jeder fremden Seite Zugriff geben."
            )
        return origins


settings = Settings()
