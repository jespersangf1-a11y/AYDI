"""Centralized logging configuration for AYDI.

Provides ``setup_logging`` which configures the root logger with either
plain or JSON formatting depending on the environment. JSON formatting
is required for production observability tools (Datadog, Grafana Loki,
ELK, etc.) that index structured fields like ``request_id``, ``path``,
``status``, ``duration_ms``.

Usage:

    from app.core.logging import setup_logging
    from app.core.config import settings

    setup_logging(level=settings.LOG_LEVEL, json_format=settings.LOG_JSON)

After this call, modules can use ``logging.getLogger(__name__)`` as
normal and inherit the configuration.
"""
from __future__ import annotations

import json
import logging
import logging.config
import sys
from datetime import datetime, timezone
from typing import Any


# Fields produced by app middleware are surfaced as MDC-like attributes on
# log records via LoggerAdapter or `extra=` on log calls. We pass them
# through to JSON output when present.
_EXTRA_FIELDS = (
    "request_id",
    "user_id",
    "path",
    "method",
    "status",
    "duration_ms",
    "client_ip",
)


class JsonFormatter(logging.Formatter):
    """Minimal JSON formatter — no external dependencies.

    Emits one JSON object per log record. Includes standard fields
    (timestamp, level, name, message) plus any extras attached by the
    middleware (request_id, etc.) plus stack traces for exceptions.
    """

    def format(self, record: logging.LogRecord) -> str:
        payload: dict[str, Any] = {
            "ts": datetime.fromtimestamp(record.created, tz=timezone.utc).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "msg": record.getMessage(),
        }
        for field in _EXTRA_FIELDS:
            value = getattr(record, field, None)
            if value is not None:
                payload[field] = value
        if record.exc_info:
            payload["exc"] = self.formatException(record.exc_info)
        if record.stack_info:
            payload["stack"] = self.formatStack(record.stack_info)
        return json.dumps(payload, ensure_ascii=False, default=str)


_PLAIN_FORMAT = "%(asctime)s %(levelname)-7s %(name)s :: %(message)s"


def setup_logging(level: str = "INFO", json_format: bool = False) -> None:
    """Configure the root logger.

    Called once during FastAPI lifespan startup. Idempotent — safe to
    call multiple times (uvicorn reload triggers reimports).
    """
    handler = logging.StreamHandler(sys.stdout)
    if json_format:
        handler.setFormatter(JsonFormatter())
    else:
        handler.setFormatter(logging.Formatter(_PLAIN_FORMAT, datefmt="%H:%M:%S"))

    root = logging.getLogger()
    # Replace existing handlers cleanly to avoid duplicate log lines under reload
    for existing in list(root.handlers):
        root.removeHandler(existing)
    root.addHandler(handler)
    root.setLevel(level.upper())

    # Tone down noisy libraries
    logging.getLogger("uvicorn.access").setLevel("WARNING")
    logging.getLogger("sqlalchemy.engine").setLevel("WARNING")
    logging.getLogger("httpx").setLevel("WARNING")
    logging.getLogger("httpcore").setLevel("WARNING")
