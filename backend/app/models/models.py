# backend/app/models/models.py
import uuid
from datetime import datetime

from sqlalchemy import DateTime, Enum, Float, ForeignKey, Integer, String, Text, func
from sqlalchemy.dialects.postgresql import JSON, UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    boat_class: Mapped[str] = mapped_column(
        Enum("small_sail", "cruising_sail", "large_motor", "superyacht", name="boat_class_enum"),
        nullable=False,
    )
    length_m: Mapped[float] = mapped_column(Float, nullable=False)
    beam_m: Mapped[float] = mapped_column(Float, nullable=False)
    status: Mapped[str] = mapped_column(
        Enum("draft", "active", "review", "archived", name="project_status_enum"),
        nullable=False,
        default="draft",
    )
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    layouts: Mapped[list["Layout"]] = relationship(back_populates="project", cascade="all, delete-orphan")
    analysis_results: Mapped[list["AnalysisResult"]] = relationship(
        back_populates="project", cascade="all, delete-orphan"
    )


class Layout(Base):
    __tablename__ = "layouts"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("projects.id", ondelete="CASCADE"), nullable=False)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    version: Mapped[str] = mapped_column(String(50), default="v1.0")
    file_path: Mapped[str | None] = mapped_column(String, nullable=True)
    file_type: Mapped[str | None] = mapped_column(String(20), nullable=True)
    zones: Mapped[dict | list] = mapped_column(JSON, default=list)
    passages: Mapped[dict | list] = mapped_column(JSON, default=list)
    deck_height_mm: Mapped[int] = mapped_column(Integer, default=2100)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    project: Mapped["Project"] = relationship(back_populates="layouts")
    analysis_results: Mapped[list["AnalysisResult"]] = relationship(
        back_populates="layout", cascade="all, delete-orphan"
    )


class AnalysisResult(Base):
    __tablename__ = "analysis_results"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("projects.id", ondelete="CASCADE"), nullable=False)
    layout_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("layouts.id", ondelete="CASCADE"), nullable=False)
    module: Mapped[str] = mapped_column(String(50), nullable=False)
    overall_score: Mapped[float] = mapped_column(Float, nullable=False)
    sub_scores: Mapped[dict] = mapped_column(JSON, default=dict)
    warnings: Mapped[list] = mapped_column(JSON, default=list)
    suggestions: Mapped[list] = mapped_column(JSON, default=list)
    metrics: Mapped[dict] = mapped_column(JSON, default=dict)
    config_used: Mapped[dict] = mapped_column(JSON, default=dict)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    project: Mapped["Project"] = relationship(back_populates="analysis_results")
    layout: Mapped["Layout"] = relationship(back_populates="analysis_results")


# Future normalization models (not actively used in Phase 1)
class Zone(Base):
    __tablename__ = "zones"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    layout_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("layouts.id", ondelete="CASCADE"), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    zone_type: Mapped[str] = mapped_column(String(50), nullable=False)
    polygon: Mapped[list] = mapped_column(JSON, nullable=False)
    is_crew_area: Mapped[bool] = mapped_column(default=False)
    is_guest_area: Mapped[bool] = mapped_column(default=False)


class Passage(Base):
    __tablename__ = "passages"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    layout_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("layouts.id", ondelete="CASCADE"), nullable=False)
    from_zone: Mapped[str] = mapped_column(String(100), nullable=False)
    to_zone: Mapped[str] = mapped_column(String(100), nullable=False)
    width_mm: Mapped[float] = mapped_column(Float, nullable=False)
    is_primary: Mapped[bool] = mapped_column(default=True)
