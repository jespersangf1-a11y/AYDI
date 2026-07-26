"""Initial schema — bootstraps all AYDI tables from SQLAlchemy models.

Revision ID: 000_initial
Revises:
Create Date: 2026-05-21

This migration is the "squashed initial" — before its introduction the
application called ``Base.metadata.create_all`` on every startup, which
left no migration history and made schema drift untraceable. From this
revision onward, all schema changes flow through Alembic.

Rather than enumerating ~20 tables verbatim (which would diverge from
the SQLAlchemy models the moment they evolve), this migration delegates
to ``Base.metadata.create_all`` against the bound connection. Future
migrations (revision 002+) are expected to use explicit ``op.add_column``,
``op.create_index`` and friends.

For a fresh database:

    alembic upgrade head

For an existing database that was previously bootstrapped via
``Base.metadata.create_all``:

    alembic stamp 001_user_prefs

(marks the DB as already migrated to the head of the pre-Alembic state).
"""
from alembic import op

from app.models.models import Base


revision = "000_initial"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    # Idempotent: create_all only creates missing tables.
    Base.metadata.create_all(bind=bind)


def downgrade() -> None:
    bind = op.get_bind()
    Base.metadata.drop_all(bind=bind)
