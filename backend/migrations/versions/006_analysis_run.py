"""Analysis run header (H-3 — reconstructable analysis history).

Revision ID: 006_analysis_run
Revises: 005_service_report_owner
Create Date: 2026-08-10

A full analysis previously persisted only its per-module rows, with no run
identity or overall score — so a past run ("our March analysis scored 71.4")
could not be reconstructed. This adds:

1. analysis_runs: one header row per full-analysis run (overall score/
   confidence, module/skip/error counts, tier).
2. analysis_results.run_id: nullable FK -> analysis_runs (SET NULL), so the 11
   module rows of a run link back to it. Legacy rows and single-module
   analyses keep run_id = NULL.

Additive-only, inspector-guarded (safe to re-run), SQLite batch-mode compatible.
"""

from alembic import op
import sqlalchemy as sa


revision = "006_analysis_run"
down_revision = "005_service_report_owner"
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    tables = set(inspector.get_table_names())

    if "analysis_runs" not in tables:
        op.create_table(
            "analysis_runs",
            sa.Column("id", sa.Uuid(), primary_key=True),
            sa.Column("project_id", sa.Uuid(), nullable=False, index=True),
            sa.Column("layout_id", sa.Uuid(), nullable=False),
            sa.Column("overall_score", sa.Float(), nullable=True),
            sa.Column("overall_confidence", sa.String(30), nullable=True),
            sa.Column("module_count", sa.Integer(), server_default="0"),
            sa.Column("skipped_count", sa.Integer(), server_default="0"),
            sa.Column("error_count", sa.Integer(), server_default="0"),
            sa.Column("tier", sa.String(20), nullable=True),
            sa.Column("created_at", sa.DateTime(), nullable=True),
            sa.ForeignKeyConstraint(["project_id"], ["projects.id"], ondelete="CASCADE"),
            sa.ForeignKeyConstraint(["layout_id"], ["layouts.id"], ondelete="CASCADE"),
        )

    if "analysis_results" in tables:
        cols = {c["name"] for c in inspector.get_columns("analysis_results")}
        if "run_id" not in cols:
            with op.batch_alter_table("analysis_results") as batch:
                batch.add_column(sa.Column("run_id", sa.Uuid(), nullable=True))
                batch.create_foreign_key(
                    "fk_analysis_result_run", "analysis_runs", ["run_id"], ["id"],
                    ondelete="SET NULL",
                )
                batch.create_index("ix_analysis_results_run_id", ["run_id"])


def downgrade() -> None:
    with op.batch_alter_table("analysis_results") as batch:
        batch.drop_index("ix_analysis_results_run_id")
        batch.drop_constraint("fk_analysis_result_run", type_="foreignkey")
        batch.drop_column("run_id")
    op.drop_table("analysis_runs")
