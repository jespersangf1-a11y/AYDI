"""(Historical) Add tier, locale, unit_system to users table.

Revision ID: 001_user_prefs
Revises: 000_initial
Create Date: 2026-04-16

NOTE: As of revision 000_initial (May 2026), these columns are part of
the initial squashed schema, so the upgrade is now a no-op on fresh
databases. Kept as a placeholder revision to preserve history for any
deployment that already stamped 001_user_prefs as head.
"""

from alembic import op
import sqlalchemy as sa


revision = "001_user_prefs"
down_revision = "000_initial"
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    existing_cols = {col["name"] for col in inspector.get_columns("users")}
    if "tier" not in existing_cols:
        op.add_column("users", sa.Column("tier", sa.String(20), nullable=False, server_default="free"))
    if "locale" not in existing_cols:
        op.add_column("users", sa.Column("locale", sa.String(5), nullable=False, server_default="de"))
    if "unit_system" not in existing_cols:
        op.add_column("users", sa.Column("unit_system", sa.String(10), nullable=False, server_default="metric"))


def downgrade() -> None:
    # Reverse only what this revision added; if 000_initial built the schema,
    # downgrading 001 in isolation should not drop user-preference columns.
    pass
