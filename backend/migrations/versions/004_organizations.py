"""Organizations / team model (pillar 4, stage 2 — decision 'Option C' stage 2).

Revision ID: 004_organizations
Revises: 003_project_sharing
Create Date: 2026-07-26

Additive-only, inspector-guarded (safe to re-run), SQLite batch-mode compatible.

1. organizations: the team/shipyard entity. ``tier`` is the seat-licensing
   lever (effective tier = max(personal, org)); it stays platform-admin-only.
2. organization_members: per-org role (owner/admin/member).
3. invitations: unified project OR org invitation, keyed by normalized email
   (works for not-yet-registered invitees). CHECK enforces exactly one scope.
4. projects.org_id / brand_reference_models.org_id: nullable FK, SET NULL on
   org delete (a deleted org reverts its projects to private — never destroys
   member work).

No data migration of the freetext ``shipyard_id`` columns: freetext cannot be
mapped to a tenancy boundary without fabricating certainty, and a wrong match
is a cross-tenant data leak. They are deprecated in place; org assignment of
legacy brand references is a deliberate, admin-executed action only.
"""

from alembic import op
import sqlalchemy as sa


revision = "004_organizations"
down_revision = "003_project_sharing"
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    tables = set(inspector.get_table_names())

    if "organizations" not in tables:
        op.create_table(
            "organizations",
            sa.Column("id", sa.Uuid(), primary_key=True),
            sa.Column("name", sa.String(200), nullable=False),
            sa.Column("tier", sa.String(20), nullable=False, server_default="free"),
            sa.Column(
                "created_by_user_id",
                sa.Uuid(),
                sa.ForeignKey("users.id", ondelete="SET NULL"),
                nullable=True,
            ),
            sa.Column("created_at", sa.DateTime(), nullable=True),
            sa.Column("updated_at", sa.DateTime(), nullable=True),
        )

    if "organization_members" not in tables:
        op.create_table(
            "organization_members",
            sa.Column("id", sa.Uuid(), primary_key=True),
            sa.Column(
                "organization_id",
                sa.Uuid(),
                sa.ForeignKey("organizations.id", ondelete="CASCADE"),
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
            sa.Column("org_role", sa.String(20), nullable=False, server_default="member"),
            sa.Column("created_at", sa.DateTime(), nullable=True),
            sa.UniqueConstraint("organization_id", "user_id", name="uq_org_member"),
        )

    if "invitations" not in tables:
        op.create_table(
            "invitations",
            sa.Column("id", sa.Uuid(), primary_key=True),
            sa.Column("email", sa.String(255), nullable=False, index=True),
            sa.Column(
                "project_id",
                sa.Uuid(),
                sa.ForeignKey("projects.id", ondelete="CASCADE"),
                nullable=True,
                index=True,
            ),
            sa.Column(
                "organization_id",
                sa.Uuid(),
                sa.ForeignKey("organizations.id", ondelete="CASCADE"),
                nullable=True,
                index=True,
            ),
            sa.Column("role", sa.String(20), nullable=False),
            sa.Column(
                "invited_by_user_id",
                sa.Uuid(),
                sa.ForeignKey("users.id", ondelete="SET NULL"),
                nullable=True,
            ),
            sa.Column("status", sa.String(20), nullable=False, server_default="pending"),
            sa.Column("created_at", sa.DateTime(), nullable=True),
            sa.Column("expires_at", sa.DateTime(), nullable=False),
            sa.Column("responded_at", sa.DateTime(), nullable=True),
            sa.CheckConstraint(
                "(project_id IS NULL) <> (organization_id IS NULL)",
                name="ck_invitation_one_scope",
            ),
            sa.Index("ix_invitations_email_status", "email", "status"),
        )

    # Nullable org_id FKs on projects and brand_reference_models
    for table, fk_name in (
        ("projects", "fk_project_org"),
        ("brand_reference_models", "fk_brand_ref_org"),
    ):
        cols = {c["name"] for c in inspector.get_columns(table)}
        if "org_id" not in cols:
            with op.batch_alter_table(table) as batch:
                batch.add_column(sa.Column("org_id", sa.Uuid(), nullable=True))
                batch.create_foreign_key(
                    fk_name, "organizations", ["org_id"], ["id"], ondelete="SET NULL"
                )
                batch.create_index(f"ix_{table}_org_id", ["org_id"])


def downgrade() -> None:
    for table, fk_name in (
        ("projects", "fk_project_org"),
        ("brand_reference_models", "fk_brand_ref_org"),
    ):
        with op.batch_alter_table(table) as batch:
            batch.drop_index(f"ix_{table}_org_id")
            batch.drop_constraint(fk_name, type_="foreignkey")
            batch.drop_column("org_id")
    op.drop_table("invitations")
    op.drop_table("organization_members")
    op.drop_table("organizations")
