# backend/app/models/models.py
import uuid
from datetime import date, datetime, timezone

from sqlalchemy import Boolean, CheckConstraint, Date, DateTime, Float, ForeignKey, Index, Integer, String, Text, UniqueConstraint
from sqlalchemy import JSON, Uuid
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


class Base(DeclarativeBase):
    pass


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    # Organization ownership (pillar 4, stage 2). Nullable: private projects
    # stay private. SET NULL on org delete — a deleted org reverts its projects
    # to private, it never destroys members' work. Project.user_id owner always
    # wins; org membership adds a base access role (see get_accessible_project).
    org_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("organizations.id", ondelete="SET NULL"), nullable=True, index=True
    )
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    boat_class: Mapped[str] = mapped_column(String(20), nullable=False)
    length_m: Mapped[float] = mapped_column(Float, nullable=False)
    beam_m: Mapped[float] = mapped_column(Float, nullable=False)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="draft")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow, onupdate=_utcnow)

    layouts: Mapped[list["Layout"]] = relationship(back_populates="project", cascade="all, delete-orphan")
    analysis_results: Mapped[list["AnalysisResult"]] = relationship(
        back_populates="project", cascade="all, delete-orphan"
    )
    images: Mapped[list["ImageUpload"]] = relationship(back_populates="project", cascade="all, delete-orphan")


class ProjectMember(Base):
    """Project sharing (pillar 4, stage 1 — decision 'Option C').

    Grants a non-owner user access to a project with a role:
    viewer = read-only, editor = read/write. Owner-only operations
    (delete project, manage members) stay bound to Project.user_id.
    In stage 2 (organization model) this table remains the fine-grained
    per-project grant layer under org membership.
    """
    __tablename__ = "project_members"
    __table_args__ = (
        UniqueConstraint("project_id", "user_id", name="uq_project_member"),
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    project_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("projects.id", ondelete="CASCADE"), nullable=False, index=True
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    role: Mapped[str] = mapped_column(String(20), nullable=False, default="viewer")  # viewer, editor
    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow)


class Organization(Base):
    """Organization / shipyard (pillar 4, stage 2 — decision 'Option C' stage 2).

    A team entity that groups projects and members. Membership grants a base
    access role on the org's projects (see get_accessible_project); explicit
    ProjectMember grants still ADD access on top (external guests, extra
    grants) — GitHub org + repo-collaborators pattern.

    ``tier`` is the seat-licensing lever: a member's effective subscription
    tier is max(personal tier, org tier). It defaults to 'free' and may be
    raised ONLY by a platform admin (there is no billing system) — self-service
    would be a trivial privilege escalation (create org -> set enterprise).
    """
    __tablename__ = "organizations"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    tier: Mapped[str] = mapped_column(String(20), nullable=False, default="free")  # free, pro, enterprise
    created_by_user_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"), nullable=True
    )
    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow, onupdate=_utcnow)


class OrganizationMember(Base):
    """Membership in an organization with an org-level role.

    org_role: owner (full control, incl. tier is platform-admin-only), admin
    (manage members/invites, effective 'owner' on org projects), member
    (effective 'editor' on org projects). An org must always keep >= 1 owner.
    """
    __tablename__ = "organization_members"
    __table_args__ = (
        UniqueConstraint("organization_id", "user_id", name="uq_org_member"),
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    organization_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    org_role: Mapped[str] = mapped_column(String(20), nullable=False, default="member")  # owner, admin, member
    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow)


class Invitation(Base):
    """Unified invitation for project OR org access (pillar 4, stage 2).

    Exactly one of project_id / organization_id is set (CHECK). Keyed by
    normalized email — NOT a user FK — so an invite created before the invitee
    registers is picked up on their first login (GET /invitations/mine matches
    on the normalized email). Acceptance is always explicit (never auto-join
    on registration): membership requires the invitee's consent.

    The anti-enumeration property lives in the endpoints: creating an
    invitation returns an identical response whether or not the email has an
    account — it never performs a user lookup in the response path.
    """
    __tablename__ = "invitations"
    __table_args__ = (
        CheckConstraint(
            "(project_id IS NULL) <> (organization_id IS NULL)",
            name="ck_invitation_one_scope",
        ),
        Index("ix_invitations_email_status", "email", "status"),
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    email: Mapped[str] = mapped_column(String(255), nullable=False, index=True)  # normalized lower().strip()
    project_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("projects.id", ondelete="CASCADE"), nullable=True, index=True
    )
    organization_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("organizations.id", ondelete="CASCADE"), nullable=True, index=True
    )
    role: Mapped[str] = mapped_column(String(20), nullable=False)  # project: viewer|editor; org: member|admin
    invited_by_user_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"), nullable=True
    )
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="pending")  # pending|accepted|declined|revoked
    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow)
    expires_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    responded_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)


class Layout(Base):
    __tablename__ = "layouts"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    project_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("projects.id", ondelete="CASCADE"), nullable=False)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    version: Mapped[str] = mapped_column(String(50), default="v1.0")
    file_path: Mapped[str | None] = mapped_column(String, nullable=True)
    file_type: Mapped[str | None] = mapped_column(String(20), nullable=True)
    zones: Mapped[dict | list] = mapped_column(JSON, default=list)
    passages: Mapped[dict | list] = mapped_column(JSON, default=list)
    deck_height_mm: Mapped[int] = mapped_column(Integer, default=2100)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow, onupdate=_utcnow)

    project: Mapped["Project"] = relationship(back_populates="layouts")
    analysis_results: Mapped[list["AnalysisResult"]] = relationship(
        back_populates="layout", cascade="all, delete-orphan"
    )
    zone_materials: Mapped[list["ZoneMaterial"]] = relationship(
        back_populates="layout", cascade="all, delete-orphan"
    )
    cost_items: Mapped[list["CostItem"]] = relationship(
        back_populates="layout", cascade="all, delete-orphan"
    )
    structural_items: Mapped[list["StructuralItem"]] = relationship(
        back_populates="layout", cascade="all, delete-orphan"
    )
    versions: Mapped[list["LayoutVersion"]] = relationship(cascade="all, delete-orphan")
    decks: Mapped[list["Deck"]] = relationship(
        back_populates="layout", cascade="all, delete-orphan"
    )


class AnalysisResult(Base):
    __tablename__ = "analysis_results"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    project_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("projects.id", ondelete="CASCADE"), nullable=False)
    layout_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("layouts.id", ondelete="CASCADE"), nullable=False)
    # Links the 11 per-module rows of one Vollanalyse to a single run header so a
    # historical run (its overall score, which modules ran) is reconstructable
    # (H-3). Nullable/SET NULL: legacy rows and single-module analyses have none.
    run_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("analysis_runs.id", ondelete="SET NULL"), nullable=True, index=True
    )
    module: Mapped[str] = mapped_column(String(50), nullable=False)
    overall_score: Mapped[float] = mapped_column(Float, nullable=False)
    sub_scores: Mapped[dict] = mapped_column(JSON, default=dict)
    warnings: Mapped[list] = mapped_column(JSON, default=list)
    suggestions: Mapped[list] = mapped_column(JSON, default=list)
    metrics: Mapped[dict] = mapped_column(JSON, default=dict)
    config_used: Mapped[dict] = mapped_column(JSON, default=dict)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow)

    project: Mapped["Project"] = relationship(back_populates="analysis_results")
    layout: Mapped["Layout"] = relationship(back_populates="analysis_results")


class AnalysisRun(Base):
    """Header row for one full-analysis run (H-3).

    Groups the per-module AnalysisResult rows of a single Vollanalyse and stores
    the run-level outcome (overall score/confidence, module counts) so a past
    run is later attributable and reconstructable — previously the DB held only
    undifferentiated module rows with no run identity or overall score.
    """
    __tablename__ = "analysis_runs"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    project_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("projects.id", ondelete="CASCADE"), nullable=False, index=True
    )
    layout_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("layouts.id", ondelete="CASCADE"), nullable=False
    )
    overall_score: Mapped[float | None] = mapped_column(Float, nullable=True)
    overall_confidence: Mapped[str | None] = mapped_column(String(30), nullable=True)
    module_count: Mapped[int] = mapped_column(Integer, default=0)
    skipped_count: Mapped[int] = mapped_column(Integer, default=0)
    error_count: Mapped[int] = mapped_column(Integer, default=0)
    tier: Mapped[str | None] = mapped_column(String(20), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow)


# Future normalization models (not actively used in Phase 1)
class Zone(Base):
    __tablename__ = "zones"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    layout_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("layouts.id", ondelete="CASCADE"), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    zone_type: Mapped[str] = mapped_column(String(50), nullable=False)
    polygon: Mapped[list] = mapped_column(JSON, nullable=False)
    is_crew_area: Mapped[bool] = mapped_column(default=False)
    is_guest_area: Mapped[bool] = mapped_column(default=False)


class Passage(Base):
    __tablename__ = "passages"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    layout_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("layouts.id", ondelete="CASCADE"), nullable=False)
    from_zone: Mapped[str] = mapped_column(String(100), nullable=False)
    to_zone: Mapped[str] = mapped_column(String(100), nullable=False)
    width_mm: Mapped[float] = mapped_column(Float, nullable=False)
    is_primary: Mapped[bool] = mapped_column(default=True)


class Material(Base):
    __tablename__ = "materials"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    # Ownership guard: without it any logged-in user could PATCH/DELETE every
    # material — and DELETE cascades into FOREIGN projects' zone assignments.
    # Nullable for legacy/seed rows (admin-managed).
    created_by_user_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"), nullable=True
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(50), nullable=False)
    subcategory: Mapped[str] = mapped_column(String(50), nullable=False)
    manufacturer: Mapped[str | None] = mapped_column(String(255), nullable=True)
    properties: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    cost_per_unit: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    cost_unit: Mapped[str] = mapped_column(String(20), nullable=False, default="sqm")
    lifespan_years: Mapped[float | None] = mapped_column(Float, nullable=True)
    maintenance_interval_months: Mapped[int | None] = mapped_column(Integer, nullable=True)
    maintenance_cost_factor: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    known_issues: Mapped[list | None] = mapped_column(JSON, nullable=True)
    alternatives: Mapped[list | None] = mapped_column(JSON, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow, onupdate=_utcnow)


class ZoneMaterial(Base):
    __tablename__ = "zone_materials"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    layout_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("layouts.id", ondelete="CASCADE"), nullable=False)
    zone_name: Mapped[str] = mapped_column(String(100), nullable=False)
    surface_type: Mapped[str] = mapped_column(String(50), nullable=False)
    material_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("materials.id", ondelete="CASCADE"), nullable=False)
    area_sqm: Mapped[float] = mapped_column(Float, nullable=False)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow)

    material: Mapped["Material"] = relationship()
    layout: Mapped["Layout"] = relationship(back_populates="zone_materials")


class ServiceReport(Base):
    __tablename__ = "service_reports"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    # Owner of the report. Nullable only so the additive migration can backfill
    # legacy rows; new reports always set it. Access control keys on this
    # (see routes/service_reports.py) — these are the most confidential records
    # in the system (defect details, repair costs, shipyard internals).
    user_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=True, index=True
    )
    project_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("projects.id", ondelete="SET NULL"), nullable=True
    )
    boat_class: Mapped[str | None] = mapped_column(String(20), nullable=True)
    model_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    report_type: Mapped[str] = mapped_column(String(50), nullable=False)
    category: Mapped[str] = mapped_column(String(50), nullable=False)
    zone_type: Mapped[str | None] = mapped_column(String(50), nullable=True)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    severity: Mapped[str] = mapped_column(String(20), nullable=False, default="medium")
    root_cause: Mapped[str | None] = mapped_column(Text, nullable=True)
    resolution: Mapped[str | None] = mapped_column(Text, nullable=True)
    cost_eur: Mapped[float | None] = mapped_column(Float, nullable=True)
    hours_labor: Mapped[float | None] = mapped_column(Float, nullable=True)
    boat_age_months: Mapped[int | None] = mapped_column(Integer, nullable=True)
    materials_involved: Mapped[list | None] = mapped_column(JSON, nullable=True)
    images: Mapped[list | None] = mapped_column(JSON, nullable=True)
    reported_by: Mapped[str | None] = mapped_column(String(255), nullable=True)
    reported_at: Mapped[date | None] = mapped_column(Date, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow)
    metadata_extra: Mapped[dict | None] = mapped_column(JSON, nullable=True)

    project: Mapped["Project | None"] = relationship()


class CostItem(Base):
    __tablename__ = "cost_items"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    layout_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("layouts.id", ondelete="CASCADE"), nullable=False
    )
    category: Mapped[str] = mapped_column(String(50), nullable=False)
    subcategory: Mapped[str | None] = mapped_column(String(50), nullable=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    quantity: Mapped[float] = mapped_column(Float, nullable=False, default=1.0)
    unit: Mapped[str] = mapped_column(String(20), nullable=False, default="piece")
    unit_cost_eur: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    total_cost_eur: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    zone_name: Mapped[str | None] = mapped_column(String(100), nullable=True)
    source: Mapped[str] = mapped_column(String(50), nullable=False, default="estimate")
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow)

    layout: Mapped["Layout"] = relationship(back_populates="cost_items")


class StructuralItem(Base):
    __tablename__ = "structural_items"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    layout_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("layouts.id", ondelete="CASCADE"), nullable=False
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    item_type: Mapped[str] = mapped_column(String(50), nullable=False)
    zone_name: Mapped[str | None] = mapped_column(String(100), nullable=True)
    weight_kg: Mapped[float] = mapped_column(Float, nullable=False)
    position_x_mm: Mapped[float | None] = mapped_column(Float, nullable=True)
    position_y_mm: Mapped[float | None] = mapped_column(Float, nullable=True)
    position_z_mm: Mapped[float | None] = mapped_column(Float, nullable=True)
    dimensions: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    properties: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow)

    layout: Mapped["Layout"] = relationship(back_populates="structural_items")


class CompetitorModel(Base):
    __tablename__ = "competitor_models"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    # Ownership guard (same IDOR class as brand references/materials):
    # competitor data feeds EVERY user's market analysis. Nullable = legacy/
    # seed rows (admin-managed).
    created_by_user_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"), nullable=True
    )
    brand: Mapped[str] = mapped_column(String(255), nullable=False)
    model_name: Mapped[str] = mapped_column(String(255), nullable=False)
    boat_class: Mapped[str] = mapped_column(String(20), nullable=False)
    length_m: Mapped[float | None] = mapped_column(Float, nullable=True)
    beam_m: Mapped[float | None] = mapped_column(Float, nullable=True)
    year: Mapped[int | None] = mapped_column(Integer, nullable=True)
    price_range_eur: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    key_metrics: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    source: Mapped[str | None] = mapped_column(String(50), nullable=True)
    source_url: Mapped[str | None] = mapped_column(Text, nullable=True)
    images: Mapped[list | None] = mapped_column(JSON, nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow)


class BrandReferenceModel(Base):
    __tablename__ = "brand_reference_models"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    shipyard_id: Mapped[str | None] = mapped_column(String(255), nullable=True)
    # Ownership guard (audit: any logged-in user could delete ALL brand
    # references). Nullable for legacy rows.
    created_by_user_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"), nullable=True
    )
    # Org-scoped brand DNA (pillar 4, stage 2): org rows are private to the
    # org's members. NULL = personal (created_by) or legacy/seed (both NULL =
    # globally readable reference data).
    org_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("organizations.id", ondelete="SET NULL"), nullable=True, index=True
    )
    model_name: Mapped[str] = mapped_column(String(255), nullable=False)
    model_year: Mapped[int | None] = mapped_column(Integer, nullable=True)
    boat_class: Mapped[str] = mapped_column(String(20), nullable=False)
    layout_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("layouts.id", ondelete="SET NULL"), nullable=True
    )
    features: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    images: Mapped[list | None] = mapped_column(JSON, nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow)


class LayoutVersion(Base):
    __tablename__ = "layout_versions"
    __table_args__ = (
        # Guards the read-max-then-insert version numbering against concurrent
        # writers: a collision fails hard (handled as 409) instead of silently
        # producing two "Version N" rows.
        UniqueConstraint("layout_id", "version_number", name="uq_layout_version_number"),
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    layout_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("layouts.id", ondelete="CASCADE"), nullable=False
    )
    version_number: Mapped[int] = mapped_column(Integer, nullable=False)
    parent_version_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("layout_versions.id", ondelete="SET NULL"), nullable=True
    )
    zones_snapshot: Mapped[list | None] = mapped_column(JSON, nullable=True)
    passages_snapshot: Mapped[list | None] = mapped_column(JSON, nullable=True)
    # Non-geometry layout fields at snapshot time ({name, version,
    # deck_height_mm}) — without this, restoring a version could not bring
    # back an analysis-relevant deck_height change (destructive edit).
    layout_meta_snapshot: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    change_summary: Mapped[str | None] = mapped_column(Text, nullable=True)
    changed_by: Mapped[str | None] = mapped_column(String(255), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow)
    tags: Mapped[list | None] = mapped_column(JSON, nullable=True)


class Deck(Base):
    __tablename__ = "decks"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    layout_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("layouts.id", ondelete="CASCADE"), nullable=False
    )
    deck_number: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    z_offset_mm: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    height_mm: Mapped[float] = mapped_column(Float, nullable=False, default=2100.0)
    is_open: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    zones: Mapped[list | None] = mapped_column(JSON, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow)

    layout: Mapped["Layout"] = relationship(back_populates="decks")


class QuickAnalysisResult(Base):
    __tablename__ = "quick_analysis_results"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    boat_class: Mapped[str] = mapped_column(String(20), nullable=False)
    length_m: Mapped[float] = mapped_column(Float, nullable=False)
    specs_input: Mapped[dict] = mapped_column(JSON, nullable=False)
    overall_score: Mapped[float] = mapped_column(Float, nullable=False)
    module_results: Mapped[dict] = mapped_column(JSON, nullable=False)
    estimated_layout: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow)


class Report(Base):
    __tablename__ = "reports"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    project_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("projects.id", ondelete="CASCADE"), nullable=False)
    layout_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("layouts.id", ondelete="CASCADE"), nullable=False)
    report_type: Mapped[str] = mapped_column(String(20), nullable=False, default="full")
    report_data: Mapped[dict] = mapped_column(JSON, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow)

    project: Mapped["Project"] = relationship()


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[str] = mapped_column(String(20), nullable=False, default="user")  # admin, user, viewer
    tier: Mapped[str] = mapped_column(String(20), nullable=False, default="free")  # free, pro, enterprise
    shipyard_id: Mapped[str | None] = mapped_column(String(255), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    locale: Mapped[str] = mapped_column(String(5), nullable=False, default="de")  # de, en, es, fr
    unit_system: Mapped[str] = mapped_column(String(10), nullable=False, default="metric")  # metric, imperial
    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow, onupdate=_utcnow)


class ImageUpload(Base):
    __tablename__ = "image_uploads"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    project_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("projects.id", ondelete="SET NULL"), nullable=True
    )
    quick_analysis_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("quick_analysis_results.id", ondelete="SET NULL"), nullable=True
    )
    file_path: Mapped[str] = mapped_column(String(500), nullable=False)
    file_type: Mapped[str] = mapped_column(String(10), nullable=False)  # jpg, png, heic, webp
    file_size_bytes: Mapped[int] = mapped_column(Integer, nullable=False)
    image_type: Mapped[str] = mapped_column(String(30), nullable=False)
    # image_type values: interior_overview, interior_detail, exterior_overview, exterior_detail,
    #                    material_sample, rendering, floorplan_photo, cockpit, helm_station
    zone_name: Mapped[str | None] = mapped_column(String(100), nullable=True)
    deck_number: Mapped[int | None] = mapped_column(Integer, nullable=True)
    tags: Mapped[list | None] = mapped_column(JSON, nullable=True)
    ai_analysis: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    ai_analysis_version: Mapped[str | None] = mapped_column(String(20), nullable=True)
    uploaded_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow)
    metadata_extra: Mapped[dict | None] = mapped_column(JSON, nullable=True)  # EXIF, camera info

    project: Mapped["Project | None"] = relationship(back_populates="images")


class CommunityReport(Base):
    """Individual experience report from forum post or owner feedback."""
    __tablename__ = "community_reports"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow)
    updated_at: Mapped[datetime | None] = mapped_column(DateTime, onupdate=_utcnow)
    source_forum: Mapped[str] = mapped_column(String(100), nullable=False)
    source_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    source_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    boat_manufacturer: Mapped[str] = mapped_column(String(100), nullable=False)
    boat_model: Mapped[str | None] = mapped_column(String(100), nullable=True)
    boat_year: Mapped[int | None] = mapped_column(Integer, nullable=True)
    hull_material: Mapped[str | None] = mapped_column(String(50), nullable=True)
    hull_construction: Mapped[str | None] = mapped_column(String(50), nullable=True)
    propulsion: Mapped[str | None] = mapped_column(String(20), nullable=True)
    issues: Mapped[list] = mapped_column(JSON, nullable=False, default=list)
    positives: Mapped[list] = mapped_column(JSON, default=list)
    reliability: Mapped[float] = mapped_column(Float, nullable=False)
    raw_text: Mapped[str | None] = mapped_column(Text, nullable=True)

    __table_args__ = (
        Index("ix_community_reports_manufacturer_model", "boat_manufacturer", "boat_model"),
        Index("ix_community_reports_hull", "hull_material", "hull_construction"),
    )


class CommunityPattern(Base):
    """Aggregated pattern derived from ≥3 independent reports."""
    __tablename__ = "community_patterns"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow)
    updated_at: Mapped[datetime | None] = mapped_column(DateTime, onupdate=_utcnow)
    manufacturer: Mapped[str | None] = mapped_column(String(100), nullable=True)
    boat_model: Mapped[str | None] = mapped_column(String(100), nullable=True)
    issue_category: Mapped[str] = mapped_column(String(50), nullable=False)
    zone_type: Mapped[str | None] = mapped_column(String(50), nullable=True)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    report_count: Mapped[int] = mapped_column(Integer, nullable=False)
    severity_mode: Mapped[str] = mapped_column(String(20), nullable=False)
    typical_onset_years: Mapped[float | None] = mapped_column(Float, nullable=True)
    materials_involved: Mapped[list | None] = mapped_column(JSON, nullable=True)
    construction_methods_involved: Mapped[list | None] = mapped_column(JSON, nullable=True)
    confidence: Mapped[float] = mapped_column(Float, nullable=False)
    source_report_ids: Mapped[list] = mapped_column(JSON, nullable=False)
    is_positive: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    __table_args__ = (
        Index("ix_community_patterns_manufacturer_model", "manufacturer", "boat_model"),
        Index("ix_community_patterns_category", "issue_category"),
        Index("ix_community_patterns_zone", "zone_type"),
    )
