"""Layout-version integrity: unique (layout_id, version_number) + meta snapshot.

Revision ID: 002_layout_version_integrity
Revises: 001_user_prefs
Create Date: 2026-07-21

Two fixes for the refit loop (pillar 3):
1. Unique constraint on (layout_id, version_number) — the read-max-then-insert
   numbering in PATCH /layouts and POST /versions could otherwise produce two
   "Version N" rows under concurrency (silent history corruption).
2. layout_meta_snapshot JSON column — snapshots previously stored only
   zones/passages, so deck_height_mm/name changes were destructive
   (unrestorable) despite the "edits are never destructive" contract.
"""

from alembic import op
import sqlalchemy as sa


revision = "002_layout_version_integrity"
down_revision = "001_user_prefs"
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)

    existing_cols = {c["name"] for c in inspector.get_columns("layout_versions")}
    if "layout_meta_snapshot" not in existing_cols:
        op.add_column(
            "layout_versions",
            sa.Column("layout_meta_snapshot", sa.JSON(), nullable=True),
        )

    existing_uniques = {
        uc["name"] for uc in inspector.get_unique_constraints("layout_versions")
    }
    if "uq_layout_version_number" not in existing_uniques:
        # batch_alter_table so SQLite (dev) handles the table rebuild;
        # on PostgreSQL this emits a plain ALTER TABLE ADD CONSTRAINT.
        with op.batch_alter_table("layout_versions") as batch:
            batch.create_unique_constraint(
                "uq_layout_version_number", ["layout_id", "version_number"]
            )


def downgrade() -> None:
    with op.batch_alter_table("layout_versions") as batch:
        batch.drop_constraint("uq_layout_version_number", type_="unique")
    op.drop_column("layout_versions", "layout_meta_snapshot")
