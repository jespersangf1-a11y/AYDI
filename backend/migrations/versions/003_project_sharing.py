"""Project sharing (pillar 4, stage 1 — decision 'Option C').

Revision ID: 003_project_sharing
Revises: 002_layout_version_integrity
Create Date: 2026-07-26

1. project_members: per-project grants (viewer/editor). Owner-only operations
   stay bound to projects.user_id. Unlocks the already multi-participant
   collaboration WebSocket that was gated owner-only.
2. brand_reference_models.created_by_user_id: closes the audit finding that
   any logged-in user could delete ALL brand references (nullable for legacy
   rows; stage 2 migrates ownership to organizations).
"""

from alembic import op
import sqlalchemy as sa


revision = "003_project_sharing"
down_revision = "002_layout_version_integrity"
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)

    if "project_members" not in inspector.get_table_names():
        op.create_table(
            "project_members",
            sa.Column("id", sa.Uuid(), primary_key=True),
            sa.Column(
                "project_id",
                sa.Uuid(),
                sa.ForeignKey("projects.id", ondelete="CASCADE"),
                nullable=False,
                index=True,
            ),
            sa.Column(
                "user_id",
                sa.Uuid(),
                sa.ForeignKey("users.id", ondelete="CASCADE"),
                nullable=False,
                index=True,
            ),
            sa.Column("role", sa.String(20), nullable=False, server_default="viewer"),
            sa.Column("created_at", sa.DateTime(), nullable=True),
            sa.UniqueConstraint("project_id", "user_id", name="uq_project_member"),
        )

    # Ownership columns for globally shared resources (same IDOR class):
    # brand references, materials, competitor models all feed other users'
    # analyses and were mutable/deletable by ANY logged-in user.
    for table, fk_name in (
        ("brand_reference_models", "fk_brand_ref_created_by"),
        ("materials", "fk_material_created_by"),
        ("competitor_models", "fk_competitor_created_by"),
    ):
        cols = {c["name"] for c in inspector.get_columns(table)}
        if "created_by_user_id" not in cols:
            with op.batch_alter_table(table) as batch:
                batch.add_column(
                    sa.Column("created_by_user_id", sa.Uuid(), nullable=True)
                )
                batch.create_foreign_key(
                    fk_name,
                    "users",
                    ["created_by_user_id"],
                    ["id"],
                    ondelete="SET NULL",
                )


def downgrade() -> None:
    for table, fk_name in (
        ("brand_reference_models", "fk_brand_ref_created_by"),
        ("materials", "fk_material_created_by"),
        ("competitor_models", "fk_competitor_created_by"),
    ):
        with op.batch_alter_table(table) as batch:
            batch.drop_constraint(fk_name, type_="foreignkey")
            batch.drop_column("created_by_user_id")
    op.drop_table("project_members")
