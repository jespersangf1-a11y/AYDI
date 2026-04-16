"""Add tier, locale, and unit_system columns to users table.

Revision ID: 001_user_prefs
Revises:
Create Date: 2026-04-16

"""

from alembic import op
import sqlalchemy as sa

revision = "001_user_prefs"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column("tier", sa.String(20), nullable=False, server_default="free"),
    )
    op.add_column(
        "users",
        sa.Column("locale", sa.String(5), nullable=False, server_default="de"),
    )
    op.add_column(
        "users",
        sa.Column("unit_system", sa.String(10), nullable=False, server_default="metric"),
    )


def downgrade() -> None:
    op.drop_column("users", "unit_system")
    op.drop_column("users", "locale")
    op.drop_column("users", "tier")
