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
import re
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
                    "client_ip": client_ip(request),
                },
            )
            if duration_ms > 5000:
                logger.warning(
                    "Slow request: %s %s took %.0fms",
                    request.method,
                    request.url.path,
                    duration_ms,
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


def client_ip(request: Request | None) -> str:
    """Die Absenderadresse einer Anfrage — die EINE Fassung.

    Only trust X-Forwarded-For behind a configured trusted proxy; otherwise it
    is attacker-controlled and could be spoofed to bypass rate limits or grow
    the limiter's memory unbounded.

    Es gab diese Funktion nach dem Zusammenfuehren zweimal: hier mit der
    Pruefung auf TRUST_PROXY_HEADERS, und in routes/auth.py ohne sie. Die
    zweite Fassung entschied ueber den Sperrzaehler der Anmeldung — ein
    beliebiger X-Forwarded-For-Wert verschaffte damit pro Versuch einen
    frischen Zaehler, und die Sperre nach fuenf Fehlversuchen je IP lief ins
    Leere. Beide Aufrufer nutzen jetzt diese Fassung.
    """
    if request is None:
        return "unknown"
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
        "/health",
        "/docs",
        "/openapi.json",
    )
    # Exakte Pfade statt Praefix: "/api/v1/quick-analysis" stand zuvor in der
    # Praefixliste und nahm damit auch die Unterrouten vom CSRF-Schutz aus —
    # insbesondere POST /api/v1/quick-analysis/{id}/images. Ausgenommen gehoert
    # nur der oeffentliche, unauthentifizierte Einstieg selbst.
    EXEMPT_PATHS = frozenset({"/api/v1/quick-analysis"})

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        if request.method in self.EXEMPT_METHODS:
            return await call_next(request)
        path = request.url.path.rstrip("/") or "/"
        if path in self.EXEMPT_PATHS:
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
        """Sprache aus ``?lang=`` oder ``Accept-Language`` bestimmen.

        Die Qualitaetswerte (``q=``) wurden zuvor ignoriert — es gewann schlicht
        der erste unterstuetzte Eintrag in der Kopfzeile. Bei
        ``Accept-Language: de;q=0.2, en;q=0.9`` kam damit Deutsch heraus, obwohl
        der Browser ausdruecklich Englisch bevorzugt. Ohne q-Angabe gilt laut
        RFC 9110 q=1.0.
        """
        lang = request.query_params.get("lang")
        if lang and lang.lower() in self.SUPPORTED:
            return lang.lower()

        candidates: list[tuple[float, int, str]] = []
        accept = request.headers.get("accept-language", "")
        for position, part in enumerate(accept.split(",")):
            token = part.strip()
            if not token:
                continue
            pieces = token.split(";")
            code = pieces[0].strip().split("-")[0].lower()
            if code not in self.SUPPORTED:
                continue
            quality = 1.0
            for parameter in pieces[1:]:
                name, _, value = parameter.partition("=")
                if name.strip().lower() == "q":
                    try:
                        quality = float(value.strip())
                    except ValueError:
                        quality = 0.0
                    break
            if quality <= 0.0:  # q=0 heisst ausdruecklich "nicht akzeptiert"
                continue
            # Bei gleichem q entscheidet die Reihenfolge in der Kopfzeile.
            candidates.append((-quality, position, code))

        if candidates:
            return min(candidates)[2]
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
    """Einfaches IP-Limit je Routengruppe.

    Die Zuordnung lief frueher ueber reine Praefixe und traf damit die teuersten
    Routen NICHT:

    * ``/api/v1/projects/{id}/images`` — die Route, die eine kostenpflichtige
      Claude-Vision-Analyse ausloest — beginnt mit ``/api/v1/projects`` und
      landete im 120/min-Eimer statt im 10/min-Eimer fuer Bilder.
    * ``/api/v1/import-cad`` existierte als Route ueberhaupt nicht; die echten
      Pfade sind ``/api/v1/projects/{id}/import/step|iges`` und
      ``/api/v1/projects/{id}/layouts/import-dxf`` — alle ebenfalls im
      120/min-Eimer. Der CAD-Eimer war also vollstaendig wirkungslos.

    Darum jetzt gemusterte Zuordnung statt Praefix, und die Reihenfolge
    entscheidet: **teuerste zuerst**. Ein Treffer weiter oben gewinnt, damit eine
    Unterroute nie in den grosszuegigeren Eimer ihres Elternpfads faellt.
    """

    # (Name, Muster, (max_requests, window_seconds)) — Reihenfolge = Vorrang.
    RULES: list[tuple[str, "re.Pattern[str]", tuple[int, int]]] = [
        # Bildanalyse: jeder Aufruf kann eine kostenpflichtige Vision-Anfrage
        # nach sich ziehen. Gilt fuer /images/analyze, /images/analyze-batch,
        # /projects/{id}/images und /quick-analysis/{id}/images.
        ("images", re.compile(r"^/api/v1/(?:.*/)?images(?:/|$)"), (10, 60)),
        # CAD-Import: Parsen grosser Dateien, CPU-intensiv.
        ("cad_import", re.compile(r"^/api/v1/.*/(?:import/|import-dxf)"), (10, 60)),
        # Anmeldung: Schutz gegen Passwort-Durchprobieren.
        ("auth", re.compile(r"^/api/v1/auth(?:/|$)"), (20, 60)),
        # Unauthentifizierte Schnellanalyse.
        ("quick_analysis", re.compile(r"^/api/v1/quick-analysis(?:/|$)"), (30, 60)),
        ("knowledge", re.compile(r"^/api/v1/knowledge(?:/|$)"), (60, 60)),
        ("projects", re.compile(r"^/api/v1/projects(?:/|$)"), (120, 60)),
        ("layouts", re.compile(r"^/api/v1/layouts(?:/|$)"), (120, 60)),
    ]
    DEFAULT_LIMIT = (120, 60)

    # Zaehlerstand modulweit statt je Instanz, damit er von aussen geleert werden
    # kann. Tests, die Autorisierung pruefen, teilen sich eine Client-IP und
    # laufen sonst gegen das Limit der Route, die sie gerade testen — sie wuerden
    # 429 statt 403/404 sehen und damit am eigentlichen Pruefgegenstand
    # vorbeimessen.
    _requests: dict[str, dict[str, list[float]]] = defaultdict(
        lambda: defaultdict(list)
    )

    def __init__(self, app: Any) -> None:
        super().__init__(app)
        self._lock = asyncio.Lock()

    @classmethod
    def reset(cls) -> None:
        """Alle Zaehler leeren (fuer Tests)."""
        cls._requests.clear()

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        if request.url.path in ("/health", "/health/live", "/health/ready", "/docs", "/openapi.json"):
            return await call_next(request)

        absender = client_ip(request)
        route_prefix = self._match_route(request.url.path)
        max_requests, window = self._limit_for(route_prefix)

        allowed = await self._check_rate(absender, route_prefix, max_requests, window)
        if not allowed:
            logger.warning("Rate limit exceeded: %s on %s", absender, route_prefix)
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
        """Name des Eimers fuer diesen Pfad — erste passende Regel gewinnt."""
        for name, pattern, _limit in self.RULES:
            if pattern.search(path):
                return name
        return "default"

    def _limit_for(self, route: str) -> tuple[int, int]:
        for name, _pattern, limit in self.RULES:
            if name == route:
                return limit
        return self.DEFAULT_LIMIT

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
# Security headers
# ---------------------------------------------------------------------------

class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    """Set the baseline browser-side security headers on every response.

    Bisher setzte die App keinen einzigen dieser Header. Der wichtigste ist
    ``X-Content-Type-Options: nosniff``: Nutzertext (z.B. ein ``model_name``
    mit ``<script>``) wird in JSON-Antworten zurueckgespiegelt, und ohne
    nosniff darf ein Browser eine solche Antwort als HTML interpretieren und
    das Skript ausfuehren. Die uebrigen Header schliessen Clickjacking und
    Referrer-Leaks aus.

    HSTS wird nur gesetzt, wenn die App ohnehin sichere Cookies verlangt
    (``COOKIE_SECURE``) — sonst wuerde eine lokale HTTP-Entwicklungsumgebung
    sich selbst aussperren.
    """

    #: Endpunkte, die HTML ausliefern und deshalb eine andere CSP brauchen.
    _HTML_PATHS = ("/docs", "/redoc")

    STATIC_HEADERS = {
        "X-Content-Type-Options": "nosniff",
        "X-Frame-Options": "DENY",
        "Referrer-Policy": "no-referrer",
        # Die API liefert ausschliesslich Daten, kein aktives Markup. base-uri
        # und form-action schliessen zusaetzlich aus, dass eingeschleustes
        # Markup das Basis-Ziel umbiegt oder ein Formular nach aussen sendet.
        "Content-Security-Policy": (
            "default-src 'none'; frame-ancestors 'none'; base-uri 'none'; "
            "form-action 'none'"
        ),
        "Cross-Origin-Resource-Policy": "same-site",
        # Die API braucht weder Kamera noch Mikrofon noch Standort.
        "Permissions-Policy": (
            "accelerometer=(), camera=(), geolocation=(), gyroscope=(), "
            "microphone=(), payment=(), usb=()"
        ),
        "X-Permitted-Cross-Domain-Policies": "none",
        "Cross-Origin-Opener-Policy": "same-origin",
    }

    #: CSP fuer die interaktive Dokumentation. Swagger UI und ReDoc laden ihre
    #: Bausteine von einem CDN; mit ``default-src 'none'`` blieben die Seiten
    #: leer. Sie sind ausserhalb der Entwicklung ohnehin abgeschaltet
    #: (``settings.docs_public``).
    _DOCS_CSP = (
        "default-src 'self'; img-src 'self' data: https:; "
        "script-src 'self' https://cdn.jsdelivr.net 'unsafe-inline'; "
        "style-src 'self' https://cdn.jsdelivr.net 'unsafe-inline'; "
        "font-src 'self' https://cdn.jsdelivr.net data:; "
        "frame-ancestors 'none'; base-uri 'none'"
    )

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        response = await call_next(request)
        # Die Dokumentationsseiten zuerst: ``setdefault`` unten laesst den hier
        # gesetzten Wert dann stehen.
        if request.url.path.startswith(self._HTML_PATHS):
            response.headers.setdefault("Content-Security-Policy", self._DOCS_CSP)
        for header, value in self.STATIC_HEADERS.items():
            response.headers.setdefault(header, value)
        if getattr(settings, "COOKIE_SECURE", False):
            response.headers.setdefault(
                "Strict-Transport-Security", "max-age=31536000; includeSubDomains"
            )
        # Zuweisung statt setdefault: uvicorn schreibt seine eigene Kennung an
        # der Transportschicht. Es laeuft deshalb mit --no-server-header
        # (siehe docker/entrypoint.sh), damit dieser Wert der einzige bleibt.
        response.headers["Server"] = "AYDI"
        return response


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

    SecurityHeaders wird zuletzt hinzugefuegt und laeuft damit weit aussen: die
    Header sollen auch auf Fehler- und Rate-Limit-Antworten stehen.
    """
    app.add_middleware(LocaleMiddleware)
    app.add_middleware(CSRFMiddleware)
    app.add_middleware(RateLimitMiddleware)
    app.add_middleware(ErrorHandlingMiddleware)
    app.add_middleware(RequestContextMiddleware)
    app.add_middleware(SecurityHeadersMiddleware)
    # Suppress access-log noise unless explicitly raised
    if not access_logger.handlers:
        access_logger.setLevel(settings.LOG_LEVEL)
