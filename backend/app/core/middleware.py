"""FastAPI middleware for AYDI.

Provides:
- Request-ID injection for log correlation
- Locale detection from Accept-Language header or query parameter
- Global error handling with user-facing messages
- CSRF protection (double-submit cookie pattern) for mutating endpoints
- Request timing and structured access logging
- Rate limiting (basic in-memory implementation)
"""

from __future__ import annotations

import asyncio
import logging
import time
import uuid
from collections import defaultdict
from typing import Any

from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

from app.core.config import settings
from app.core.errors import (
    AYDIError,
    CADImportError,
    DataValidationError,
    ModuleAnalysisError,
    VisualAnalysisError,
)
from app.core.i18n import Locale, set_locale, t

logger = logging.getLogger(__name__)
access_logger = logging.getLogger("aydi.access")


# ---------------------------------------------------------------------------
# Request-ID + structured access logging
# ---------------------------------------------------------------------------

class RequestContextMiddleware(BaseHTTPMiddleware):
    """Assign a request_id to every request and emit a structured access log.

    The request_id is propagated as ``X-Request-ID`` response header and
    attached to every log record made during the request (via the
    ``extra={"request_id": ...}`` mechanism — application code can opt in
    by reading ``request.state.request_id``).
    """

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        incoming = request.headers.get("x-request-id")
        request_id = incoming if incoming else uuid.uuid4().hex
        request.state.request_id = request_id

        start = time.perf_counter()
        try:
            response = await call_next(request)
            duration_ms = (time.perf_counter() - start) * 1000.0
            response.headers["X-Request-ID"] = request_id
            response.headers["X-Response-Time"] = f"{duration_ms:.1f}ms"
            access_logger.info(
                "request",
                extra={
                    "request_id": request_id,
                    "method": request.method,
                    "path": request.url.path,
                    "status": response.status_code,
                    "duration_ms": round(duration_ms, 2),
                    "client_ip": _client_ip(request),
                },
            )
            return response
        except Exception:
            duration_ms = (time.perf_counter() - start) * 1000.0
            access_logger.exception(
                "request-failed",
                extra={
                    "request_id": request_id,
                    "method": request.method,
                    "path": request.url.path,
                    "duration_ms": round(duration_ms, 2),
                },
            )
            raise


def _client_ip(request: Request) -> str:
    # Only trust X-Forwarded-For behind a configured trusted proxy; otherwise it
    # is attacker-controlled and could be spoofed to bypass rate limits or grow
    # the limiter's memory unbounded.
    if settings.TRUST_PROXY_HEADERS:
        forwarded = request.headers.get("x-forwarded-for")
        if forwarded:
            return forwarded.split(",")[0].strip()
    if request.client:
        return request.client.host
    return "unknown"


# ---------------------------------------------------------------------------
# CSRF Middleware (double-submit cookie)
# ---------------------------------------------------------------------------

class CSRFMiddleware(BaseHTTPMiddleware):
    """Reject state-changing requests whose X-CSRF-Token header doesn't
    match the aydi_csrf cookie.

    Strategy: double-submit cookie. The /auth/login endpoint sets two
    things — an httpOnly ``aydi_access`` cookie (the actual auth token)
    and a non-httpOnly ``aydi_csrf`` cookie that the browser's JS can
    read and echo back as the ``X-CSRF-Token`` header on mutating
    requests. An attacker controlling a malicious page cannot read the
    csrf cookie (same-origin policy), so they can't construct a request
    that satisfies both checks.

    Methods exempt: GET, HEAD, OPTIONS (no state change).
    Paths exempt: /auth/login, /auth/register, /auth/refresh (no
    pre-existing session to validate against).
    """

    EXEMPT_METHODS = {"GET", "HEAD", "OPTIONS"}
    EXEMPT_PATH_PREFIXES = (
        "/api/v1/auth/login",
        "/api/v1/auth/register",
        "/api/v1/auth/refresh",
        "/api/v1/auth/logout",
        "/api/v1/quick-analysis",  # public endpoint
        "/health",
        "/docs",
        "/openapi.json",
    )

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        if request.method in self.EXEMPT_METHODS:
            return await call_next(request)
        if any(request.url.path.startswith(p) for p in self.EXEMPT_PATH_PREFIXES):
            return await call_next(request)

        cookie_token = request.cookies.get("aydi_csrf")
        header_token = request.headers.get("x-csrf-token")

        # Only enforce CSRF when a session cookie is present (cookie auth in use).
        # Bearer-header-only clients are out of CSRF scope by definition.
        has_session = "aydi_access" in request.cookies
        if not has_session:
            return await call_next(request)

        if not cookie_token or not header_token or cookie_token != header_token:
            return JSONResponse(
                status_code=403,
                content={
                    "error": "csrf_failed",
                    "message": t("error.csrf_invalid"),
                },
            )

        return await call_next(request)


# ---------------------------------------------------------------------------
# Locale Middleware
# ---------------------------------------------------------------------------

class LocaleMiddleware(BaseHTTPMiddleware):
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
        lang = request.query_params.get("lang")
        if lang and lang.lower() in self.SUPPORTED:
            return lang.lower()
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
                },
            )
        except ModuleAnalysisError as exc:
            logger.error("Module analysis error: %s", exc, exc_info=True)
            return JSONResponse(
                status_code=500,
                content={
                    "error": "analysis_error",
                    "message": t("error.partial_failure"),
                },
            )
        except AYDIError as exc:
            logger.error("AYDI error: %s", exc, exc_info=True)
            return JSONResponse(
                status_code=500,
                content={
                    "error": "aydi_error",
                    "message": t("error.server_error"),
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
        self._requests: dict[str, dict[str, list[float]]] = defaultdict(
            lambda: defaultdict(list)
        )
        self._lock = asyncio.Lock()

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        if request.url.path in ("/health", "/health/live", "/health/ready", "/docs", "/openapi.json"):
            return await call_next(request)

        client_ip = _client_ip(request)
        route_prefix = self._match_route(request.url.path)
        max_requests, window = self.LIMITS.get(route_prefix, self.DEFAULT_LIMIT)

        allowed = await self._check_rate(client_ip, route_prefix, max_requests, window)
        if not allowed:
            logger.warning("Rate limit exceeded: %s on %s", client_ip, route_prefix)
            return JSONResponse(
                status_code=429,
                content={
                    "error": "rate_limited",
                    "message": t("error.rate_limited"),
                },
                headers={"Retry-After": str(window)},
            )

        return await call_next(request)

    def _match_route(self, path: str) -> str:
        for prefix in self.LIMITS:
            if path.startswith(prefix):
                return prefix
        return "default"

    async def _check_rate(
        self, ip: str, route: str, max_requests: int, window: int
    ) -> bool:
        now = time.monotonic()
        cutoff = now - window
        async with self._lock:
            routes = self._requests[ip]
            kept = [ts for ts in routes[route] if ts > cutoff]

            if len(kept) >= max_requests:
                routes[route] = kept
                return False

            kept.append(now)
            routes[route] = kept

            # Bound memory: drop this client's other buckets that have gone fully
            # stale so inactive routes do not accumulate unbounded.
            for r in [
                r for r, ts in list(routes.items())
                if r != route and not any(t > cutoff for t in ts)
            ]:
                del routes[r]
            return True


# ---------------------------------------------------------------------------
# Registration helper
# ---------------------------------------------------------------------------

def register_middleware(app: FastAPI) -> None:
    """Register all AYDI middleware.

    Order matters — outermost runs first (added last → outermost):
    1. RequestContext (assigns request_id, logs every request)
    2. ErrorHandling (catches anything below)
    3. RateLimit (enforced before any work)
    4. CSRF (only on mutating cookie-authenticated requests)
    5. Locale (sets request-scoped locale)
    """
    app.add_middleware(LocaleMiddleware)
    app.add_middleware(CSRFMiddleware)
    app.add_middleware(RateLimitMiddleware)
    app.add_middleware(ErrorHandlingMiddleware)
    app.add_middleware(RequestContextMiddleware)
    # Suppress access-log noise unless explicitly raised
    if not access_logger.handlers:
        access_logger.setLevel(settings.LOG_LEVEL)
