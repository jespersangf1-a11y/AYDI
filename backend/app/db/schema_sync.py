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

import json
import logging
import math

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


# --- Geometrie mit NaN/Infinity ---------------------------------------------
#
# Bis die Eingabepruefung in schemas.py stand, konnte ein Layout mit den
# JSON-Literalen ``NaN`` oder ``Infinity`` angelegt werden: Pythons json-Modul
# liest sie, und die Geometriefelder hatten keine Schranke, an der ein
# Vergleich mit NaN haette scheitern koennen. Beim Ausliefern schreibt
# Starlette dagegen mit ``allow_nan=False`` — jede Anfrage auf die Layout-Liste
# des betroffenen Projekts endete danach in einem Serverfehler, nicht nur die
# auf das eine kaputte Layout.
#
# Neue Datensaetze koennen so nicht mehr entstehen. Vorhandene werden hier
# einmalig entschaerft, damit die Liste wieder lesbar wird.

_GEOMETRIE_TABELLEN = (
    ("layouts", "zones", "passages"),
    ("layout_versions", "zones_snapshot", "passages_snapshot"),
)

# Grobfilter auf dem rohen JSON-Text, damit nicht jede Zeile geparst werden
# muss. Gross-/Kleinschreibung ist bedeutsam: json.dumps schreibt genau diese
# Schreibweise, und "-Infinity" enthaelt "Infinity" bereits.
_LITERALE = ("NaN", "Infinity")


def _ist_nicht_endlich(wert: object) -> bool:
    return isinstance(wert, float) and (math.isnan(wert) or math.isinf(wert))


def _zonen_bereinigen(zonen: list) -> tuple[list, int]:
    """Zonen mit unbrauchbarer Geometrie wieder lesbar machen.

    Das Polygon wird geleert statt korrigiert. Ein NaN laesst sich nicht durch
    eine plausible Zahl ersetzen, ohne Geometrie zu erfinden, und die
    Auswertungsmodule behandeln ein leeres Polygon bereits als "keine Flaeche
    bekannt" (``z.get("polygon") or []``, dann ``len(polygon) < 3``). Name, Typ
    und Eigenschaften der Zone bleiben erhalten.
    """
    bereinigt: list = []
    treffer = 0
    for zone in zonen:
        if not isinstance(zone, dict):
            bereinigt.append(zone)
            continue
        neu = dict(zone)
        polygon = neu.get("polygon")
        if isinstance(polygon, list) and any(
            _ist_nicht_endlich(koordinate)
            for punkt in polygon
            if isinstance(punkt, list)
            for koordinate in punkt
        ):
            neu["polygon"] = []
            treffer += 1
        for feld in ("height_mm", "visibility_angle"):
            if _ist_nicht_endlich(neu.get(feld)):
                neu[feld] = None
                treffer += 1
        bereinigt.append(neu)
    return bereinigt, treffer


def _durchgaenge_bereinigen(durchgaenge: list) -> tuple[list, int]:
    """Durchgaenge ohne brauchbares Mass entfernen.

    Anders als bei einer Zone gibt es hier nichts zu erhalten: die Breite ist
    das Mass, das die Ergonomie auswertet, und ein Durchgang ohne sie wuerde je
    nach Modul als unendlich breit oder als Sperre gelesen — beides falsch.
    """
    behalten: list = []
    entfernt = 0
    for durchgang in durchgaenge:
        if not isinstance(durchgang, dict):
            behalten.append(durchgang)
            continue
        zahlen: list = [durchgang.get("width_mm"), durchgang.get("length_mm")]
        punkte = durchgang.get("points")
        if isinstance(punkte, list):
            zahlen += [
                koordinate
                for punkt in punkte
                if isinstance(punkt, list)
                for koordinate in punkt
            ]
        if any(_ist_nicht_endlich(zahl) for zahl in zahlen):
            entfernt += 1
            continue
        behalten.append(durchgang)
    return behalten, entfernt


def repair_nonfinite_geometry(conn: Connection) -> dict[str, int]:
    """Entschaerfe gespeicherte Layouts, die NaN oder Infinity enthalten.

    Laeuft bei jedem Start und ist damit auch die Reparatur fuer eine
    Datenbank, die vor der Eingabepruefung befuellt wurde. Ist nichts zu tun,
    kostet es einen Tabellendurchlauf ohne Schreibzugriff.
    """
    bilanz: dict[str, int] = {}
    vorhandene_tabellen = set(inspect(conn).get_table_names())

    for tabelle, zonen_spalte, durchgangs_spalte in _GEOMETRIE_TABELLEN:
        if tabelle not in vorhandene_tabellen:
            continue

        zeilen = conn.execute(
            text(
                f'SELECT "id", "{zonen_spalte}", "{durchgangs_spalte}" '
                f'FROM "{tabelle}"'
            )
        ).fetchall()

        for kennung, zonen_roh, durchgaenge_roh in zeilen:
            verdaechtig = any(
                isinstance(roh, str) and any(lit in roh for lit in _LITERALE)
                for roh in (zonen_roh, durchgaenge_roh)
            )
            if not verdaechtig:
                continue

            try:
                zonen = json.loads(zonen_roh) if isinstance(zonen_roh, str) else zonen_roh
                durchgaenge = (
                    json.loads(durchgaenge_roh)
                    if isinstance(durchgaenge_roh, str)
                    else durchgaenge_roh
                )
            except (TypeError, ValueError):
                logger.warning(
                    "Geometrie von %s.%s ist kein lesbares JSON, uebersprungen.",
                    tabelle,
                    kennung,
                )
                continue

            zonen_neu, zonen_treffer = (
                _zonen_bereinigen(zonen) if isinstance(zonen, list) else (zonen, 0)
            )
            durchgaenge_neu, durchgangs_treffer = (
                _durchgaenge_bereinigen(durchgaenge)
                if isinstance(durchgaenge, list)
                else (durchgaenge, 0)
            )
            if not zonen_treffer and not durchgangs_treffer:
                continue

            conn.execute(
                text(
                    f'UPDATE "{tabelle}" SET "{zonen_spalte}" = :zonen, '
                    f'"{durchgangs_spalte}" = :durchgaenge WHERE "id" = :kennung'
                ),
                {
                    # allow_nan=False sichert ab, dass wir nicht selbst wieder
                    # ein ungueltiges Literal zurueckschreiben.
                    "zonen": json.dumps(zonen_neu, allow_nan=False),
                    "durchgaenge": json.dumps(durchgaenge_neu, allow_nan=False),
                    "kennung": kennung,
                },
            )
            bilanz[f"{tabelle}.{kennung}"] = zonen_treffer + durchgangs_treffer

    if bilanz:
        logger.warning(
            "Geometrie mit NaN/Infinity bereinigt: %d Datensaetze (%s)",
            len(bilanz),
            ", ".join(sorted(bilanz)),
        )

    return bilanz
