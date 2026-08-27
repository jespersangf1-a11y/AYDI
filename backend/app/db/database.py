# backend/app/db/database.py
from collections.abc import AsyncGenerator

from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.core.config import settings


# SQLite ignores FK ON DELETE actions (SET NULL / CASCADE) unless foreign-key
# enforcement is switched on per connection. Production runs PostgreSQL (which
# always enforces them), but dev and the whole test suite run on SQLite — so
# without this, org-delete SET NULL and other FK actions silently no-op and the
# tests would validate tenancy against an engine that doesn't enforce it. This
# global listener turns it on for every SQLite connection (app + tests).
@event.listens_for(Engine, "connect")
def _enable_sqlite_fk(dbapi_connection, _connection_record):  # pragma: no cover
    module = type(dbapi_connection).__module__
    if "sqlite" in module:
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()


# pool_size gilt nur fuer Pools, die eine Groesse kennen. SQLite laeuft hier ueber
# NullPool/SingletonThreadPool und lehnt das Argument ab — darum nur fuer echte
# Server-Datenbanken setzen. DATABASE_POOL_SIZE war zuvor deklariert, aber
# nirgends gelesen.
_engine_kwargs: dict = {"echo": False}
if not settings.DATABASE_URL.startswith("sqlite"):
    _engine_kwargs["pool_size"] = settings.DATABASE_POOL_SIZE

engine = create_async_engine(settings.DATABASE_URL, **_engine_kwargs)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


_IS_SQLITE = settings.DATABASE_URL.startswith("sqlite")

if _IS_SQLITE:

    @event.listens_for(engine.sync_engine, "connect")
    def _sqlite_pragmas(dbapi_connection, connection_record) -> None:  # noqa: ANN001
        """Apply the pragmas SQLite needs but does not default to.

        ``foreign_keys`` is OFF by default in SQLite, per connection. Without
        it every ``ForeignKey`` in the models is decorative: rows referencing a
        deleted parent survive, and ``ON DELETE CASCADE`` never fires. A real
        orphan had already accumulated in the live database because of this.

        ``journal_mode=WAL`` lets readers work while a writer holds the
        database, which is what the concurrent-request tests were tripping on
        under the default ``delete`` journal.

        ``busy_timeout`` makes a competing writer wait instead of failing
        immediately with "database is locked".
        """
        cursor = dbapi_connection.cursor()
        try:
            cursor.execute("PRAGMA foreign_keys=ON")
            cursor.execute("PRAGMA journal_mode=WAL")
            cursor.execute("PRAGMA busy_timeout=5000")
            cursor.execute("PRAGMA synchronous=NORMAL")
        finally:
            cursor.close()


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
