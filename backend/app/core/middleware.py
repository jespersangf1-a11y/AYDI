"""FastAPI middleware for AYDI.

Provides:
- Locale detection from Accept-Language header or query parameter
- Global error handling with user-facing messages
- Request timing and logging
- Rate limiting (basic in-memory implementation)
"""

from __future__ import annotations

import asyncio
import logging
import time
from collections import defaultdict
from typing import Any

from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from app.core.errors import (
    AYDIError,
    CADImportError,
    DataValidationError,
    ModuleAnalysisError,
    VisualAnalysisError,
)
from app.core.i18n import Locale, set_locale, t

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Locale Middleware
# ---------------------------------------------------------------------------

class LocaleMiddleware(BaseHTTPMiddleware):
    """Detect locale from request and set it for the async context.

    Priority:
    1. Query parameter: ?lang=en
    2. Accept-Language header
    3. Default: de
    """

    SUPPORTED = {l.value for l in Locale}

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        locale = self._detect_locale(request)
        set_locale(locale)
        response = await call_next(request)
        response.headers["Content-Language"] = locale
        return response

    def _detect_locale(self, request: Request) -> str:
        # 1. Query parameter
        lang = request.query_params.get("lang")
        if lang and lang.lower() in self.SUPPORTED:
            return lang.lower()

        # 2. Accept-Language header
        accept = request.headers.get("accept-language", "")
        for part in accept.split(","):
            code = part.strip().split(";")[0].strip().split("-")[0].lower()
            if code in self.SUPPORTED:
                return code

        return "de"


# ---------------------------------------------------------------------------
# Error Handling Middleware
# ---------------------------------------------------------------------------

class ErrorHandlingMiddleware(BaseHTTPMiddleware):
    """Global error handler that returns user-facing error messages.

    Catches AYDI domain exceptions and returns appropriate HTTP responses
    with localized error messages. Unknown errors get a generic 500 response.
    """

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        try:
            return await call_next(request)
        except DataValidationError as exc:
            logger.warning("Validation error: %s", exc, exc_info=False)
            return JSONResponse(
                status_code=422,
                content={
                    "error": "validation_error",
                    "message": t("error.validation_failed", details=str(exc)),
                    "details": str(exc),
                },
            )
        except CADImportError as exc:
            logger.warning("CAD import error: %s", exc, exc_info=False)
            return JSONResponse(
                status_code=422,
                content={
                    "error": "cad_import_error",
                    "message": t("error.cad_parse_failed"),
                    "details": str(exc),
                },
            )
        except VisualAnalysisError as exc:
            logger.warning("Visual analysis error: %s", exc, exc_info=False)
            return JSONResponse(
                status_code=502,
                content={
                    "error": "visual_analysis_error",
                    "message": t("error.api_unavailable"),
                    "details": str(exc),
                },
            )
        except ModuleAnalysisError as exc:
            logger.error("Module analysis error: %s", exc, exc_info=True)
            return JSONResponse(
                status_code=500,
                content={
                    "error": "analysis_error",
                    "message": t("error.partial_failure"),
                    "details": str(exc),
                },
            )
        except AYDIError as exc:
            logger.error("AYDI error: %s", exc, exc_info=True)
            return JSONResponse(
                status_code=500,
                content={
                    "error": "aydi_error",
                    "message": t("error.server_error"),
                    "details": str(exc),
                },
            )
        except asyncio.TimeoutError:
            logger.warning("Request timeout for %s", request.url.path)
            return JSONResponse(
                status_code=504,
                content={
                    "error": "timeout",
                    "message": t("error.timeout"),
                },
            )
        except Exception:
            logger.exception("Unhandled error for %s", request.url.path)
            return JSONResponse(
                status_code=500,
                content={
                    "error": "internal_error",
                    "message": t("error.server_error"),
                },
            )


# ---------------------------------------------------------------------------
# Rate Limiting Middleware
# ---------------------------------------------------------------------------

class RateLimitMiddleware(BaseHTTPMiddleware):
    """Basic in-memory rate limiting.

    Limits requests per IP address. Different limits for:
    - Public endpoints (quick_analysis, auth): 30 req/min
    - Authenticated endpoints: 120 req/min
    - Heavy endpoints (analysis, image upload): 10 req/min

    Note: For production, use Redis-backed rate limiting.
    """

    # Route prefix -> (max_requests, window_seconds)
    LIMITS: dict[str, tuple[int, int]] = {
        "/api/v1/quick-analysis": (30, 60),
        "/api/v1/auth": (20, 60),
        "/api/v1/images": (10, 60),
        "/api/v1/import-cad": (10, 60),
        "/api/v1/projects": (120, 60),
        "/api/v1/layouts": (120, 60),
        "/api/v1/knowledge": (60, 60),
    }
    DEFAULT_LIMIT = (120, 60)

    def __init__(self, app: Any) -> None:
        super().__init__(app)
        # {ip: {route_prefix: [(timestamp, ...)]}}
        self._requests: dict[str, dict[str, list[float]]] = defaultdict(
            lambda: defaultdict(list)
        )
        self._lock = asyncio.Lock()

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        # Skip rate limiting for health checks
        if request.url.path in ("/health", "/docs", "/openapi.json"):
            return await call_next(request)

        client_ip = self._get_client_ip(request)
        route_prefix = self._match_route(request.url.path)
        max_requests, window = self.LIMITS.get(route_prefix, self.DEFAULT_LIMIT)

        allowed = await self._check_rate(client_ip, route_prefix, max_requests, window)
        if not allowed:
            logger.warning(
                "Rate limit exceeded: %s on %s", client_ip, route_prefix
            )
            return JSONResponse(
                status_code=429,
                content={
                    "error": "rate_limited",
                    "message": t("error.rate_limited"),
                },
                headers={"Retry-After": str(window)},
            )

        return await call_next(request)

    def _get_client_ip(self, request: Request) -> str:
        forwarded = request.headers.get("x-forwarded-for")
        if forwarded:
            return forwarded.split(",")[0].strip()
        if request.client:
            return request.client.host
        return "unknown"

    def _match_route(self, path: str) -> str:
        for prefix in self.LIMITS:
            if path.startswith(prefix):
                return prefix
        return "default"

    async def _check_rate(
        self, ip: str, route: str, max_requests: int, window: int
    ) -> bool:
        now = time.monotonic()
        async with self._lock:
            timestamps = self._requests[ip][route]
            # Remove expired entries
            cutoff = now - window
            self._requests[ip][route] = [ts for ts in timestamps if ts > cutoff]
            timestamps = self._requests[ip][route]

            if len(timestamps) >= max_requests:
                return False

            timestamps.append(now)
            return True


# ---------------------------------------------------------------------------
# Security Headers Middleware
# ---------------------------------------------------------------------------

class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    """Set the response headers a browser needs to defend the app.

    None of these were being sent. Each one closes a specific hole:

    ``X-Content-Type-Options``    stops a JSON response being sniffed as HTML
                                  or script.
    ``X-Frame-Options`` /
    ``frame-ancestors``           stops the app being framed for clickjacking.
    ``Referrer-Policy``           keeps project identifiers out of the
                                  Referer header sent to third parties.
    ``Content-Security-Policy``   limits what an injected string could load;
                                  API responses need nothing at all, so the
                                  policy denies everything by default.
    ``Permissions-Policy``        the API has no use for camera, microphone
                                  or geolocation.
    ``Strict-Transport-Security`` only over HTTPS, and only in production —
                                  sending it from a local HTTP server would
                                  pin the developer's browser to HTTPS on
                                  localhost.
    ``Server``                    overwritten so the exact server software is
                                  no longer advertised.

    One caveat on ``Server``: uvicorn writes its own value at the transport
    layer, *before* the application's headers, and does not check whether the
    app already set one — a middleware alone therefore produces the header
    twice, and a proxy reads the first. Uvicorn must be started with
    ``--no-server-header`` (or ``server_header=False``) for the override to
    be the only value. This was verified against the running server rather
    than assumed.
    """

    #: Endpoints that render HTML and therefore need a workable policy.
    _HTML_PATHS = ("/docs", "/redoc")

    def __init__(self, app: Any, *, production: bool = False) -> None:
        super().__init__(app)
        self._production = production

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        response = await call_next(request)
        headers = response.headers

        headers.setdefault("X-Content-Type-Options", "nosniff")
        headers.setdefault("X-Frame-Options", "DENY")
        headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
        headers.setdefault(
            "Permissions-Policy",
            "accelerometer=(), camera=(), geolocation=(), gyroscope=(), "
            "microphone=(), payment=(), usb=()",
        )
        headers.setdefault("X-Permitted-Cross-Domain-Policies", "none")
        headers.setdefault("Cross-Origin-Opener-Policy", "same-origin")
        headers.setdefault("Cross-Origin-Resource-Policy", "same-site")

        if request.url.path.startswith(self._HTML_PATHS):
            # Swagger UI / ReDoc load their assets from a CDN.
            headers.setdefault(
                "Content-Security-Policy",
                "default-src 'self'; img-src 'self' data: https:; "
                "script-src 'self' https://cdn.jsdelivr.net 'unsafe-inline'; "
                "style-src 'self' https://cdn.jsdelivr.net 'unsafe-inline'; "
                "font-src 'self' https://cdn.jsdelivr.net data:; "
                "frame-ancestors 'none'; base-uri 'none'",
            )
        else:
            headers.setdefault(
                "Content-Security-Policy",
                "default-src 'none'; frame-ancestors 'none'; base-uri 'none'; "
                "form-action 'none'",
            )

        if self._production:
            headers.setdefault(
                "Strict-Transport-Security",
                "max-age=31536000; includeSubDomains",
            )

        headers["Server"] = "AYDI"
        return response


# ---------------------------------------------------------------------------
# Request Timing Middleware
# ---------------------------------------------------------------------------

class TimingMiddleware(BaseHTTPMiddleware):
    """Add X-Response-Time header to all responses."""

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        start = time.perf_counter()
        response = await call_next(request)
        elapsed_ms = (time.perf_counter() - start) * 1000
        response.headers["X-Response-Time"] = f"{elapsed_ms:.1f}ms"
        if elapsed_ms > 5000:
            logger.warning(
                "Slow request: %s %s took %.0fms",
                request.method,
                request.url.path,
                elapsed_ms,
            )
        return response


# ---------------------------------------------------------------------------
# Registration helper
# ---------------------------------------------------------------------------

def register_middleware(app: FastAPI) -> None:
    """Register all AYDI middleware on a FastAPI app.

    Order matters — outermost middleware runs first:
    1. Security headers (must also cover error responses, so it wraps them)
    2. Timing
    3. Error handling (catches all exceptions)
    4. Rate limiting (before any processing)
    5. Locale detection (available to all handlers)
    """
    from app.core.config import settings

    # Added in reverse order (last added = outermost)
    app.add_middleware(LocaleMiddleware)
    app.add_middleware(RateLimitMiddleware)
    app.add_middleware(ErrorHandlingMiddleware)
    app.add_middleware(TimingMiddleware)
    app.add_middleware(SecurityHeadersMiddleware, production=settings.is_production)
