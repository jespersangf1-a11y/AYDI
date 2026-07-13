# backend/app/core/config.py
from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

# The built-in fallback signing key. It is intentionally recognisable so that
# both the production guard below and the startup warning can detect it. Any
# real deployment MUST override SECRET_KEY via environment/.env.
DEFAULT_SECRET_KEY = "aydi-secret-key-change-in-production"


class Settings(BaseSettings):
    # "development" | "production" — production activates hard security guards.
    ENVIRONMENT: str = "development"
    DATABASE_URL: str = "sqlite+aiosqlite:///./aydi.db"
    CORS_ORIGINS: list[str] = ["http://localhost:5173"]
    ANTHROPIC_API_KEY: str | None = None
    ANTHROPIC_MODEL: str = "claude-sonnet-4-20250514"
    VISUAL_ANALYSIS_TIMEOUT_SEC: int = 30
    DATABASE_POOL_SIZE: int = 10
    LOG_LEVEL: str = "INFO"
    LOG_JSON: bool = False  # production: structured JSON for log aggregators
    MAX_IMAGE_SIZE_MB: int = 20
    UPLOAD_DIR: str = "uploads"
    SECRET_KEY: str = DEFAULT_SECRET_KEY
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    # When True, cookie auth is the only accepted credential source
    # (Authorization-header fallback disabled). Leave False during
    # transition to keep existing bearer-token clients working.
    AUTH_COOKIE_ONLY: bool = False
    COOKIE_SECURE: bool = False  # set True in production (requires HTTPS)
    COOKIE_DOMAIN: str | None = None
    # Only honour X-Forwarded-For for the client IP when set True — enable ONLY
    # when behind a trusted proxy/load balancer that sets it. Default False so
    # the header cannot be spoofed to bypass rate limits / grow memory.
    TRUST_PROXY_HEADERS: bool = False

    model_config = SettingsConfigDict(env_file=".env")

    @property
    def uses_default_secret(self) -> bool:
        return self.SECRET_KEY == DEFAULT_SECRET_KEY

    @model_validator(mode="after")
    def _enforce_production_security(self) -> "Settings":
        """Refuse to boot with insecure defaults when ENVIRONMENT=production.

        Prevents the silent fallback to the repo-public default signing key
        (which would allow anyone to forge auth tokens) and to non-HTTPS cookies.
        """
        if self.ENVIRONMENT.strip().lower() == "production":
            problems: list[str] = []
            if self.uses_default_secret:
                problems.append(
                    'SECRET_KEY is the built-in default — set a strong random value, e.g. '
                    'python -c "import secrets; print(secrets.token_urlsafe(64))"'
                )
            if not self.COOKIE_SECURE:
                problems.append("COOKIE_SECURE must be True in production (HTTPS-only cookies).")
            if problems:
                raise ValueError(
                    "Insecure configuration for ENVIRONMENT=production:\n  - "
                    + "\n  - ".join(problems)
                )
        return self


settings = Settings()
