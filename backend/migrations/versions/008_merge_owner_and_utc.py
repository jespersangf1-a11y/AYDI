"""Besitzer der Schnellanalyse, Fremdschluessel-Indizes, UTC-Zeitstempel.

Entstanden beim Zusammenfuehren von ``audit/fixes-checkpoint`` und ``main``.
Drei Dinge kamen von ``main`` und brauchen fuer bestehende Datenbanken einen
Schritt, den eine frische Datenbank durch Revision 000 schon hat:

1. ``quick_analysis_results.owner_id`` — eine gespeicherte Schnellanalyse
   konnte bisher von jedem abgerufen werden, der ihre Kennung kannte. Mit
   Besitzer gilt: gehoert sie einem Konto, sieht nur dieses Konto sie; eine
   anonyme (Level 1, nicht angemeldet) bleibt ohne Besitzer und damit
   abrufbar, so wie der oeffentliche Trichter es braucht.

   Die uebrigen Besitzerspalten kommen NICHT hinzu: Material,
   CompetitorModel, BrandReferenceModel und ServiceReport fuehren sie auf
   diesem Zweig bereits als ``created_by_user_id`` bzw. ``user_id`` (siehe
   Revisionen 003–005). ``main`` hatte dieselbe Sache ``owner_id`` genannt;
   beide anzulegen haette jeder dieser Tabellen ZWEI Besitzerspalten gegeben.

2. Indizes auf haeufig gefilterte Fremdschluessel. Ohne sie liest jede
   Layout-, Zonen- oder Berichtsabfrage die ganze Tabelle.

3. Zeitstempel als ``TIMESTAMP WITH TIME ZONE``. Nur auf PostgreSQL eine
   echte Aenderung: SQLite legt beides gleich ab, dort ist der Unterschied
   allein die Python-seitige Normalisierung in ``app/db/types.py``.

IDEMPOTENT, wie alle Migrationen ab 001: Revision 000 baut das Schema per
``Base.metadata.create_all`` aus den LIVE-Modellen, eine frische Datenbank hat
Spalte und Indizes deshalb schon bei 000.

Revision ID: 008_merge_owner_and_utc
Revises: 007_image_analysis_status
"""
import sqlalchemy as sa
from alembic import op

revision = "008_merge_owner_and_utc"
down_revision = "007_image_analysis_status"
branch_labels = None
depends_on = None

OWNER_TABLE = "quick_analysis_results"
OWNER_COLUMN = "owner_id"

#: (Index, Tabelle, Spalte) — dieselben, die die Modelle als index=True fuehren.
INDEXES: tuple[tuple[str, str, str], ...] = (
    ("ix_analysis_results_layout_id", "analysis_results", "layout_id"),
    ("ix_analysis_results_project_id", "analysis_results", "project_id"),
    ("ix_layouts_project_id", "layouts", "project_id"),
    ("ix_passages_layout_id", "passages", "layout_id"),
    ("ix_reports_layout_id", "reports", "layout_id"),
    ("ix_reports_project_id", "reports", "project_id"),
    ("ix_zones_layout_id", "zones", "layout_id"),
    ("ix_zone_materials_layout_id", "zone_materials", "layout_id"),
    ("ix_zone_materials_material_id", "zone_materials", "material_id"),
    (f"ix_{OWNER_TABLE}_{OWNER_COLUMN}", OWNER_TABLE, OWNER_COLUMN),
)

#: Tabelle -> Zeitstempelspalten, die auf timestamptz gehoben werden.
UTC_COLUMNS: dict[str, tuple[str, ...]] = {
    "users": ("created_at", "updated_at"),
    "projects": ("created_at", "updated_at"),
    "layouts": ("created_at", "updated_at"),
    "layout_versions": ("created_at",),
    "materials": ("created_at", "updated_at"),
    "zone_materials": ("created_at",),
    "decks": ("created_at",),
    "cost_items": ("created_at",),
    "structural_items": ("created_at",),
    "service_reports": ("created_at",),
    "competitor_models": ("created_at",),
    "brand_reference_models": ("created_at",),
    "community_reports": ("created_at", "updated_at"),
    "community_patterns": ("created_at", "updated_at"),
    "analysis_results": ("created_at",),
    "quick_analysis_results": ("created_at",),
    "reports": ("created_at",),
    "image_uploads": ("uploaded_at",),
}


def _tables(bind) -> set[str]:
    return set(sa.inspect(bind).get_table_names())


def _columns(bind, table: str) -> set[str]:
    return {col["name"] for col in sa.inspect(bind).get_columns(table)}


def _indexes(bind, table: str) -> set[str]:
    return {ix["name"] for ix in sa.inspect(bind).get_indexes(table)}


def upgrade() -> None:
    bind = op.get_bind()
    vorhandene_tabellen = _tables(bind)

    # --- 1. Besitzer der Schnellanalyse ---
    if OWNER_TABLE in vorhandene_tabellen and OWNER_COLUMN not in _columns(bind, OWNER_TABLE):
        # Bewusst OHNE Fremdschluessel-Constraint im ALTER: SQLite kann einen
        # solchen nachtraeglich nicht anlegen, und ein Batch-Umbau der Tabelle
        # waere fuer eine nullbare Spalte unverhaeltnismaessig. Auf PostgreSQL
        # traegt eine frische Datenbank den Constraint aus Revision 000.
        op.add_column(
            OWNER_TABLE, sa.Column(OWNER_COLUMN, sa.Uuid(), nullable=True)
        )

    # --- 2. Fremdschluessel-Indizes ---
    for name, table, column in INDEXES:
        if table not in vorhandene_tabellen:
            continue
        if column not in _columns(bind, table):
            continue
        if name in _indexes(bind, table):
            continue
        op.create_index(name, table, [column])

    # --- 3. Zeitstempel mit Zeitzone (nur PostgreSQL) ---
    if bind.dialect.name != "postgresql":
        return
    for table, columns in UTC_COLUMNS.items():
        if table not in vorhandene_tabellen:
            continue
        vorhanden = _columns(bind, table)
        for column in columns:
            if column not in vorhanden:
                continue
            # Bestandswerte wurden mit datetime.now(timezone.utc) geschrieben,
            # sind also UTC — genau das sagt das USING dem Server.
            op.execute(
                f'ALTER TABLE "{table}" ALTER COLUMN "{column}" '
                f'TYPE TIMESTAMP WITH TIME ZONE '
                f'USING "{column}" AT TIME ZONE \'UTC\''
            )


def downgrade() -> None:
    bind = op.get_bind()
    vorhandene_tabellen = _tables(bind)

    if bind.dialect.name == "postgresql":
        for table, columns in UTC_COLUMNS.items():
            if table not in vorhandene_tabellen:
                continue
            vorhanden = _columns(bind, table)
            for column in columns:
                if column in vorhanden:
                    op.execute(
                        f'ALTER TABLE "{table}" ALTER COLUMN "{column}" '
                        f'TYPE TIMESTAMP WITHOUT TIME ZONE'
                    )

    for name, table, column in INDEXES:
        if table in vorhandene_tabellen and name in _indexes(bind, table):
            op.drop_index(name, table_name=table)

    if OWNER_TABLE in vorhandene_tabellen and OWNER_COLUMN in _columns(bind, OWNER_TABLE):
        op.drop_column(OWNER_TABLE, OWNER_COLUMN)
