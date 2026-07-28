"""Bring an existing database up to the current model definition.

``Base.metadata.create_all`` only creates *missing tables*. It does not touch a
table that already exists, so an index or a column added to a model later never
reaches a database that was created before the change — which is exactly the
situation the deployed SQLite file was in: eighteen foreign-key columns without
an index, and no owner column on the tables that later grew one.

This module closes that gap with the two operations SQLite can perform in
place: ``CREATE INDEX IF NOT EXISTS`` and ``ALTER TABLE ... ADD COLUMN``. Both
are idempotent, so this runs on every startup. Anything more involved (dropping
a column, changing a type) is deliberately out of scope and would need a real
migration.
"""
from __future__ import annotations

import logging

from sqlalchemy import inspect, text
from sqlalchemy.engine import Connection
from sqlalchemy.schema import CreateIndex

from app.models.models import Base

logger = logging.getLogger(__name__)


def _existing_columns(conn: Connection, table_name: str) -> set[str]:
    return {c["name"] for c in inspect(conn).get_columns(table_name)}


def _existing_indexes(conn: Connection, table_name: str) -> set[str]:
    return {i["name"] for i in inspect(conn).get_indexes(table_name)}


def sync_schema(conn: Connection) -> dict[str, list[str]]:
    """Add missing columns and indexes. Returns what was changed."""
    added_columns: list[str] = []
    added_indexes: list[str] = []

    inspector = inspect(conn)
    present_tables = set(inspector.get_table_names())
    dialect = conn.dialect

    for table in Base.metadata.sorted_tables:
        if table.name not in present_tables:
            continue  # create_all already made it, with everything on it

        have_columns = _existing_columns(conn, table.name)
        for column in table.columns:
            if column.name in have_columns:
                continue
            # A new column can only be added if existing rows can be filled.
            if not column.nullable and column.server_default is None and column.default is None:
                logger.warning(
                    "Spalte %s.%s fehlt, kann aber nicht nachtraeglich angelegt "
                    "werden (NOT NULL ohne Standardwert).",
                    table.name,
                    column.name,
                )
                continue
            column_type = column.type.compile(dialect=dialect)
            ddl = f'ALTER TABLE "{table.name}" ADD COLUMN "{column.name}" {column_type}'
            if not column.nullable:
                default = column.server_default
                if default is not None:
                    ddl += f" NOT NULL DEFAULT {default.arg.text}"  # type: ignore[union-attr]
            conn.execute(text(ddl))
            added_columns.append(f"{table.name}.{column.name}")

        have_indexes = _existing_indexes(conn, table.name)
        for index in table.indexes:
            if index.name in have_indexes:
                continue
            # Re-check the columns: an index over a column we just refused to
            # add would fail the whole startup.
            index_columns = {c.name for c in index.columns}
            if not index_columns <= _existing_columns(conn, table.name):
                continue
            conn.execute(CreateIndex(index, if_not_exists=True))
            added_indexes.append(index.name or "?")

    if added_columns or added_indexes:
        logger.info(
            "Schema angeglichen: %d Spalten, %d Indizes ergaenzt (%s | %s)",
            len(added_columns),
            len(added_indexes),
            ", ".join(added_columns) or "-",
            ", ".join(added_indexes) or "-",
        )

    return {"columns": added_columns, "indexes": added_indexes}


def purge_orphans(conn: Connection) -> dict[str, int]:
    """Delete rows whose mandatory parent no longer exists.

    With ``PRAGMA foreign_keys`` off — SQLite's default, and how this database
    ran until now — a parent could be deleted while its children stayed behind.
    Those children are unreachable through the API but block the foreign-key
    checks now that the pragma is on. They are removed once, at startup.
    """
    removed: dict[str, int] = {}

    for table in Base.metadata.sorted_tables:
        for fk in table.foreign_keys:
            column = fk.parent
            if column.nullable:
                continue  # SET NULL / optional link, an orphan is legitimate
            target = fk.column
            statement = text(
                f'DELETE FROM "{table.name}" WHERE "{column.name}" IS NOT NULL '
                f'AND "{column.name}" NOT IN (SELECT "{target.name}" FROM "{target.table.name}")'
            )
            result = conn.execute(statement)
            if result.rowcount:
                removed[f"{table.name}.{column.name}"] = result.rowcount

    if removed:
        logger.warning("Verwaiste Zeilen entfernt: %s", removed)

    return removed
