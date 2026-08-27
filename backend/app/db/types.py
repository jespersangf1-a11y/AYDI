"""Custom SQLAlchemy column types."""
from datetime import UTC, datetime

from sqlalchemy import DateTime
from sqlalchemy.types import TypeDecorator


class UtcDateTime(TypeDecorator):
    """A timestamp that is always UTC and always timezone-aware in Python.

    Two problems this solves:

    1. SQLite's ``DATETIME`` silently discards the offset of an aware value
       and hands back a naive one, so ``DateTime(timezone=True)`` alone buys
       nothing there. Timestamps were therefore leaving the API as
       ``2026-07-20T09:12:33`` with no zone at all — a client had to guess.
    2. Rows written before this change are naive but were produced by
       ``datetime.now(timezone.utc)``, i.e. they *are* UTC. Reading them back
       as UTC is correct, not an assumption made for convenience.

    On PostgreSQL the underlying ``TIMESTAMP WITH TIME ZONE`` does the real
    work; this decorator then only normalises to UTC.
    """

    impl = DateTime(timezone=True)
    cache_ok = True

    def process_bind_param(self, value: datetime | None, dialect) -> datetime | None:  # noqa: ANN001
        if value is None:
            return None
        if value.tzinfo is None:
            value = value.replace(tzinfo=UTC)
        return value.astimezone(UTC)

    def process_result_value(self, value: datetime | None, dialect) -> datetime | None:  # noqa: ANN001
        if value is None:
            return None
        if value.tzinfo is None:
            return value.replace(tzinfo=UTC)
        return value.astimezone(UTC)
