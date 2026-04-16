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
    1. Timing (wraps everything)
    2. Error handling (catches all exceptions)
    3. Rate limiting (before any processing)
    4. Locale detection (available to all handlers)
    """
    # Added in reverse order (last added = outermost)
    app.add_middleware(LocaleMiddleware)
    app.add_middleware(RateLimitMiddleware)
    app.add_middleware(ErrorHandlingMiddleware)
    app.add_middleware(TimingMiddleware)
