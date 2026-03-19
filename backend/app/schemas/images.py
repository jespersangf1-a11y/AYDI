from datetime import datetime
from enum import Enum
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ImageType(str, Enum):
    interior_overview = "interior_overview"
    interior_detail = "interior_detail"
    exterior_overview = "exterior_overview"
    exterior_detail = "exterior_detail"
    material_sample = "material_sample"
    rendering = "rendering"
    floorplan_photo = "floorplan_photo"
    cockpit = "cockpit"
    helm_station = "helm_station"


class VisualConfidence(str, Enum):
    high = "high"
    medium = "medium"
    low = "low"
    insufficient = "insufficient"


class VisualFinding(BaseModel):
    category: str
    observation: str
    assessment: str  # gut, akzeptabel, mangelhaft, kritisch
    confidence: str  # hoch, mittel, niedrig
    location_in_image: str | None = None
    detail: str | None = None
    severity: str | None = None
    suggestion: str | None = None


class ImageUploadResponse(BaseModel):
    id: UUID
    project_id: UUID | None
    quick_analysis_id: UUID | None
    file_path: str
    file_type: str
    file_size_bytes: int
    image_type: str
    zone_name: str | None
    deck_number: int | None
    tags: list[str] | None
    ai_analysis: dict | None
    ai_analysis_version: str | None
    uploaded_at: datetime
    metadata_extra: dict | None

    model_config = ConfigDict(from_attributes=True)


class ImageAnalysisRequest(BaseModel):
    image_type: ImageType
    boat_class: str
    zone_type: str | None = None
    analysis_depth: str = "standard"  # quick, standard, detailed


class ImageAnalysisResponse(BaseModel):
    image_id: UUID
    scores: dict[str, float]
    findings: list[VisualFinding]
    positive_aspects: list[str]
    concerns: list[str]
    cannot_assess: list[str]
    recommendations: list[str]
    confidence: VisualConfidence
    confidence_factors: list[str]
    image_quality_sufficient: bool


class BatchAnalysisRequest(BaseModel):
    boat_class: str
    zone_type: str | None = None
    analysis_depth: str = "standard"


class BatchAnalysisResponse(BaseModel):
    images_analyzed: int
    images_rejected: int
    fused_score: float | None
    confidence: VisualConfidence
    findings: list[VisualFinding]
    positive_aspects: list[str]
    concerns: list[str]
    recommendations: list[str]
