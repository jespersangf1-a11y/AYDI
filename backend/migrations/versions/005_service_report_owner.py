"""Service report ownership (access-control fix).

Revision ID: 005_service_report_owner
Revises: 004_organizations
Create Date: 2026-07-28

Adds ``service_reports.user_id`` (nullable FK -> users, CASCADE, indexed) so the
service-report routes can scope every read/write to the owner. Before this
column existed the routes had no ownership at all — any authenticated user could
list/read/modify/delete every other user's confidential service reports.

Additive-only, inspector-guarded (safe to re-run), SQLite batch-mode compatible.
Legacy rows keep user_id = NULL and are therefore invisible to the owner-scoped
routes (fail-closed): a NULL-owner report leaks to no one.
"""

from alembic import op
import sqlalchemy as sa


revision = "005_service_report_owner"
down_revision = "004_organizations"
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    if "service_reports" not in set(inspector.get_table_names()):
        return
    cols = {c["name"] for c in inspector.get_columns("service_reports")}
    if "user_id" not in cols:
        with op.batch_alter_table("service_reports") as batch:
            batch.add_column(sa.Column("user_id", sa.Uuid(), nullable=True))
            batch.create_foreign_key(
                "fk_service_report_user", "users", ["user_id"], ["id"], ondelete="CASCADE"
            )
            batch.create_index("ix_service_reports_user_id", ["user_id"])


def downgrade() -> None:
    with op.batch_alter_table("service_reports") as batch:
        batch.drop_index("ix_service_reports_user_id")
        batch.drop_constraint("fk_service_report_user", type_="foreignkey")
        batch.drop_column("user_id")
