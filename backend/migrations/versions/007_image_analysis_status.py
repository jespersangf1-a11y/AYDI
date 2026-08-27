"""Statusfeld fuer die asynchrone Bildanalyse.

Die visuelle Analyse dauert gemessen rund 60 s und lief bisher INLINE in der
HTTP-Anfrage. Browser und Reverse-Proxys brechen in dieser Groessenordnung ab
(nginx: 60 s Default) — der Pfad funktionierte lokal und waere in Produktion
sporadisch gescheitert. Sie laeuft jetzt als Hintergrundauftrag.

Damit braucht es einen Zustand: Ohne ihn waere "laeuft noch" nicht von
"gescheitert" zu unterscheiden, beide haetten ai_analysis = NULL.

IDEMPOTENT, wie alle Migrationen ab 001: Revision 000 baut das Schema per
``Base.metadata.create_all`` aus den LIVE-Modellen. Eine frische Datenbank hat
die Spalte deshalb schon bei 000 — ein blindes ``add_column`` liefe hier in
"duplicate column name".

Revision ID: 007_image_analysis_status
Revises: 006_analysis_run
"""
import sqlalchemy as sa
from alembic import op

revision = "007_image_analysis_status"
down_revision = "006_analysis_run"
branch_labels = None
depends_on = None

TABLE = "image_uploads"
COLUMN = "ai_analysis_status"


def _columns(bind) -> set[str]:
    return {col["name"] for col in sa.inspect(bind).get_columns(TABLE)}


def upgrade() -> None:
    bind = op.get_bind()
    if COLUMN not in _columns(bind):
        op.add_column(TABLE, sa.Column(COLUMN, sa.String(length=20), nullable=True))

    # Bestandsdaten sinnvoll vorbelegen: Wo bereits ein Ergebnis vorliegt, ist
    # die Analyse fertig; alles andere gilt als nie gelaufen.
    op.execute(
        f"UPDATE {TABLE} SET {COLUMN} = 'done' "
        f"WHERE {COLUMN} IS NULL AND ai_analysis IS NOT NULL"
    )


def downgrade() -> None:
    bind = op.get_bind()
    if COLUMN in _columns(bind):
        op.drop_column(TABLE, COLUMN)
