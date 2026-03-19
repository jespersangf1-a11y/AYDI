# backend/app/models/models.py
import uuid
from datetime import date, datetime, timezone

from sqlalchemy import Boolean, Date, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy import JSON, Uuid
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


class Base(DeclarativeBase):
    pass


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
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
    shipyard_id: Mapped[str | None] = mapped_column(String(255), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
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
