# backend/app/db/database.py
from collections.abc import AsyncGenerator

from sqlalchemy import event
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.core.config import settings

engine = create_async_engine(settings.DATABASE_URL, echo=False)
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
