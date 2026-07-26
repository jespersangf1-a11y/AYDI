"""Migration 004 (organizations) round-trip on SQLite.

Drives the migration's own upgrade()/downgrade() through Alembic's Operations
against a real sync SQLite engine — the same batch_alter + inspector-guard
pattern proven in 003. Verifies: additive tables/columns appear on upgrade,
disappear on downgrade, and the migration is idempotent (re-run safe).
"""

import importlib.util
from pathlib import Path

import pytest
import sqlalchemy as sa

# Alembic is a production dependency; skip cleanly where it isn't installed.
pytest.importorskip("alembic")
from alembic.migration import MigrationContext  # noqa: E402
from alembic.operations import Operations  # noqa: E402


def _load_migration():
    path = Path(__file__).resolve().parents[1] / "migrations" / "versions" / "004_organizations.py"
    spec = importlib.util.spec_from_file_location("mig004", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _prerequisite_schema(engine):
    """Create the minimal pre-004 tables the migration's FKs/batch_alter need."""
    meta = sa.MetaData()
    sa.Table(
        "users", meta,
        sa.Column("id", sa.Uuid(), primary_key=True),
    )
    sa.Table(
        "projects", meta,
        sa.Column("id", sa.Uuid(), primary_key=True),
        sa.Column("user_id", sa.Uuid()),
    )
    sa.Table(
        "brand_reference_models", meta,
        sa.Column("id", sa.Uuid(), primary_key=True),
        sa.Column("model_name", sa.String(255)),
    )
    meta.create_all(engine)


def test_migration_004_round_trip(tmp_path):
    db = tmp_path / "mig004.db"
    engine = sa.create_engine(f"sqlite:///{db}")
    _prerequisite_schema(engine)
    mig = _load_migration()

    with engine.connect() as conn:
        ctx = MigrationContext.configure(conn)
        with Operations.context(ctx):
            mig.upgrade()
            # Idempotent: inspector guards make a re-run a no-op, not an error.
            mig.upgrade()
        conn.commit()

        inspector = sa.inspect(conn)
        tables = set(inspector.get_table_names())
        assert {"organizations", "organization_members", "invitations"} <= tables
        proj_cols = {c["name"] for c in inspector.get_columns("projects")}
        assert "org_id" in proj_cols
        bref_cols = {c["name"] for c in inspector.get_columns("brand_reference_models")}
        assert "org_id" in bref_cols

    with engine.connect() as conn:
        ctx = MigrationContext.configure(conn)
        with Operations.context(ctx):
            mig.downgrade()
        conn.commit()

        inspector = sa.inspect(conn)
        tables = set(inspector.get_table_names())
        assert "organizations" not in tables
        assert "organization_members" not in tables
        assert "invitations" not in tables
        assert "org_id" not in {c["name"] for c in inspector.get_columns("projects")}
        assert "org_id" not in {c["name"] for c in inspector.get_columns("brand_reference_models")}
