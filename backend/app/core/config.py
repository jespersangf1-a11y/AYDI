# backend/app/core/config.py
from pydantic import field_validator, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

# The built-in fallback signing key. It is intentionally recognisable so that
# both the production guard below and the startup warning can detect it. Any
# real deployment MUST override SECRET_KEY via environment/.env.
DEFAULT_SECRET_KEY = "aydi-secret-key-change-in-production"


class Settings(BaseSettings):
    # "development" | "production" — production activates hard security guards,
    # closes the interactive docs and tightens the CSP.
    ENVIRONMENT: str = "development"
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
    # None → docs follow ENVIRONMENT (open in development, closed otherwise).
    DOCS_ENABLED: bool | None = None
    ANTHROPIC_API_KEY: str | None = None
    # claude-sonnet-4-20250514 war zurückgezogen: Die API antwortete mit
    # 404 not_found_error, die visuelle Analyse schlug dadurch bei JEDEM
    # Bild fehl. Aktuelle Modell-IDs tragen kein Datumssuffix.
    ANTHROPIC_MODEL: str = "claude-opus-5"
    # Gemessen: Ein Bild mit dem Standardprompt braucht auf claude-opus-5 rund
    # 57 s (4.970 Eingabe-, 3.363 Ausgabe-Tokens). Mit 30 s lief JEDER Aufruf
    # in den Timeout. 120 s lassen Luft für größere Bilder und Lastspitzen,
    # ohne einen hängenden Aufruf unbegrenzt offen zu halten.
    VISUAL_ANALYSIS_TIMEOUT_SEC: int = 120
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
                "und ein Platzhalter würde jeder fremden Seite Zugriff geben."
            )
        return origins

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
                    "Insecure configuration for ENVIRONMENT=production:" + chr(10) + "  - "
                    + (chr(10) + "  - ").join(problems)
                )
        return self


settings = Settings()
