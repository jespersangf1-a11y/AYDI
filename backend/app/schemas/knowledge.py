# backend/app/schemas/knowledge.py
"""Pydantic schemas for Knowledge API endpoints."""

from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


# ============================================================================
# CATEGORY & INDEX RESPONSES
# ============================================================================

class KnowledgeCategoryStatus(BaseModel):
    """Status of a single knowledge category."""
    category_id: str = Field(..., description="Unique identifier for the category")
    title: str = Field(..., description="Display title of the category")
    status: str = Field(..., description="Implementation status: implemented/partial/missing")
    description: str | None = Field(None, description="Category description")
    entry_count: int = Field(0, description="Number of entries in this category")


class KnowledgeIndexResponse(BaseModel):
    """Complete knowledge system index with all categories."""
    total_categories: int = Field(..., description="Total number of categories")
    implemented_count: int = Field(..., description="Number of fully implemented categories")
    partial_count: int = Field(..., description="Number of partially implemented categories")
    categories: list[KnowledgeCategoryStatus] = Field(..., description="List of all categories")

    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# MATERIALS KNOWLEDGE
# ============================================================================

class MaterialKnowledge(BaseModel):
    """Material-specific knowledge data."""
    material_type: str = Field(..., description="Type of material (resin/fiber/gelcoat/core)")
    name: str = Field(..., description="Material name or designation")
    properties: dict = Field(default_factory=dict, description="Technical properties")
    lifespan_years: float | None = Field(None, description="Typical lifespan in years")
    failure_modes: list[str] = Field(default_factory=list, description="Known failure modes")
    maintenance_notes: str | None = Field(None, description="Maintenance recommendations")
    common_issues: list[str] = Field(default_factory=list, description="Common issues observed")


class MaterialsKnowledgeResponse(BaseModel):
    """Knowledge response for material compositions."""
    hull_material: str | None = Field(None, description="Hull material specified")
    hull_construction: str | None = Field(None, description="Hull construction method")
    core_material: str | None = Field(None, description="Core material specified")
    materials: list[MaterialKnowledge] = Field(default_factory=list, description="Material knowledge entries")
    recommendations: list[str] = Field(default_factory=list, description="Recommendations based on materials")
    warnings: list[str] = Field(default_factory=list, description="Warnings for this material combination")

    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# DEGRADATION & LIFECYCLE KNOWLEDGE
# ============================================================================

class DegradationCycle(BaseModel):
    """Degradation cycle for a material or system."""
    name: str = Field(..., description="Degradation cycle name")
    description: str = Field(..., description="Description of the cycle")
    onset_years: float = Field(..., description="Typical onset in years")
    duration_years: float = Field(..., description="Typical duration in years")
    severity: str = Field(..., description="Severity: mild/moderate/severe")


class LifespanData(BaseModel):
    """Lifespan information for materials and systems."""
    component: str = Field(..., description="Component or material name")
    lifespan_years: float = Field(..., description="Typical lifespan in years")
    maintenance_intervals_months: list[int] = Field(default_factory=list)
    failure_probability_percent: float | None = Field(None, description="Failure probability at lifespan")


class DegradationResponse(BaseModel):
    """Knowledge response for degradation patterns."""
    hull_material: str | None = Field(None)
    core_material: str | None = Field(None)
    degradation_cycles: list[DegradationCycle] = Field(default_factory=list)
    lifespan_data: list[LifespanData] = Field(default_factory=list)
    risk_factors: list[str] = Field(default_factory=list, description="Risk factors for degradation")
    prevention_measures: list[str] = Field(default_factory=list)

    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# MANUFACTURER KNOWLEDGE
# ============================================================================

class ManufacturerProfile(BaseModel):
    """Manufacturer-specific knowledge profile."""
    manufacturer_name: str = Field(..., description="Name of the manufacturer")
    reputation_score: float = Field(0.0, ge=0, le=100, description="Reputation score 0-100")
    known_strengths: list[str] = Field(default_factory=list)
    known_weaknesses: list[str] = Field(default_factory=list)
    quality_tier: str | None = Field(None, description="Quality tier: budget/economy/mid-range/premium/luxury")
    construction_methods: list[str] = Field(default_factory=list)
    material_preferences: dict = Field(default_factory=dict)
    production_type: str | None = Field(None, description="Production type: production/semi-custom/custom")
    typical_issues_by_age: dict = Field(default_factory=dict, description="Issues by boat age in years")
    expert_opinions: list[str] = Field(default_factory=list)


class ManufacturerResponse(BaseModel):
    """Knowledge response for manufacturer information."""
    manufacturer: ManufacturerProfile | None = Field(None)
    message: str = Field(..., description="Response message")

    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# COMPLIANCE & STANDARDS KNOWLEDGE
# ============================================================================

class StandardRequirement(BaseModel):
    """A single compliance requirement."""
    standard_code: str = Field(..., description="Standard code (e.g., ISO 12215)")
    description: str = Field(..., description="What this standard requires")
    applies: bool = Field(..., description="Whether this applies to the vessel")
    risk_if_not_met: str | None = Field(None, description="Risk if requirement not met")


class ComplianceResponse(BaseModel):
    """Knowledge response for compliance and standards."""
    propulsion: str | None = Field(None, description="Propulsion type (sail/motor/hybrid)")
    length_m: float | None = Field(None, description="Vessel length in meters")
    operating_waters: str | None = Field(None, description="Operating waters (inland/coastal/offshore)")
    applicable_standards: list[StandardRequirement] = Field(default_factory=list)
    safety_requirements: list[str] = Field(default_factory=list, description="Safety-specific requirements")
    structural_requirements: list[str] = Field(default_factory=list)
    notes: str | None = Field(None, description="Additional compliance notes")

    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# SYSTEMS KNOWLEDGE
# ============================================================================

class SystemKnowledge(BaseModel):
    """Knowledge about a specific system type."""
    system_type: str = Field(..., description="Type of system (engine/electrical/sanitary/rigging)")
    components: list[str] = Field(default_factory=list, description="Main components of this system")
    common_issues: list[str] = Field(default_factory=list, description="Common issues with this system")
    maintenance_schedule: dict = Field(default_factory=dict, description="Maintenance schedule in months")
    failure_modes: list[str] = Field(default_factory=list, description="Known failure modes")
    upgrade_considerations: list[str] = Field(default_factory=list)
    expert_recommendations: list[str] = Field(default_factory=list)


class SystemsResponse(BaseModel):
    """Knowledge response for system-specific information."""
    system_type: str | None = Field(None)
    systems: list[SystemKnowledge] = Field(default_factory=list)
    general_notes: str | None = Field(None)

    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# SEARCH RESULTS
# ============================================================================

class SearchMatch(BaseModel):
    """A single search result match."""
    category: str = Field(..., description="Knowledge category where match was found")
    database: str = Field(..., description="Database within the category")
    entry_name: str = Field(..., description="Name of the matched entry")
    excerpt: str = Field(..., description="Excerpt of matching content")
    relevance_score: float = Field(0.0, ge=0, le=1.0, description="Relevance score 0-1")
    full_content: dict | None = Field(None, description="Full content of the match if available")


class SearchResponse(BaseModel):
    """Full-text search response across knowledge databases."""
    query: str = Field(..., description="The search query")
    results_count: int = Field(0, description="Total number of matches")
    matches: list[SearchMatch] = Field(default_factory=list, description="Matching entries")
    search_time_ms: float = Field(0.0, description="Time to execute search in milliseconds")

    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# FAQ KNOWLEDGE
# ============================================================================

class FAQEntry(BaseModel):
    """A single FAQ entry from markdown knowledge."""
    question_de: str = Field(..., description="Question in German")
    answer_de: str = Field(..., description="Answer in German")
    confidence: str = Field("documented", description="Confidence level")
    knowledge_source: str | None = Field(None, description="Source knowledge file slug")


class FAQResponse(BaseModel):
    """Response for FAQ knowledge queries."""
    total_count: int = Field(0, description="Total FAQ entries matching")
    category: str | None = Field(None, description="Category filter applied")
    search_query: str | None = Field(None, description="Search filter applied")
    entries: list[FAQEntry] = Field(default_factory=list)

    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# GLOSSARY KNOWLEDGE
# ============================================================================

class GlossaryEntry(BaseModel):
    """A single glossary entry from markdown knowledge."""
    term_de: str | None = Field(None, description="German term")
    term_en: str | None = Field(None, description="English term")
    definition: str | None = Field(None, description="Definition")
    knowledge_source: str | None = Field(None, description="Source knowledge file slug")


class GlossaryResponse(BaseModel):
    """Response for glossary knowledge queries."""
    total_count: int = Field(0)
    category: str | None = Field(None)
    search_query: str | None = Field(None)
    entries: list[GlossaryEntry] = Field(default_factory=list)

    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# FEHLERBILDER (FAILURE PATTERNS)
# ============================================================================

class FehlerbildEntry(BaseModel):
    """A single failure pattern from markdown knowledge."""
    title_de: str = Field(..., description="Fehlerbild title in German")
    symptom_de: str | None = Field(None, description="Symptoms")
    ursache_de: str | None = Field(None, description="Root cause")
    massnahme_de: str | None = Field(None, description="Corrective action")
    haeufigkeit_de: str | None = Field(None, description="Frequency")
    confidence: str | None = Field(None, description="Confidence level")
    knowledge_source: str | None = Field(None, description="Source knowledge file slug")


class FehlerbilderResponse(BaseModel):
    """Response for failure pattern queries."""
    total_count: int = Field(0)
    category: str | None = Field(None)
    search_query: str | None = Field(None)
    entries: list[FehlerbildEntry] = Field(default_factory=list)

    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# FALLSTUDIEN (CASE STUDIES)
# ============================================================================

class FallstudieEntry(BaseModel):
    """A single case study from markdown knowledge."""
    title_de: str = Field(..., description="Case study title")
    situation_de: str | None = Field(None, description="Initial situation")
    diagnose_de: str | None = Field(None, description="Diagnosis")
    ursache_de: str | None = Field(None, description="Root cause")
    ergebnis_de: str | None = Field(None, description="Result")
    kosten_de: str | None = Field(None, description="Cost info")
    lehre_de: str | None = Field(None, description="Lesson learned")
    confidence: str | None = Field(None, description="Confidence level")
    knowledge_source: str | None = Field(None, description="Source knowledge file slug")


class FallstudienResponse(BaseModel):
    """Response for case study queries."""
    total_count: int = Field(0)
    category: str | None = Field(None)
    search_query: str | None = Field(None)
    entries: list[FallstudieEntry] = Field(default_factory=list)

    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# MANUFACTURERS (from markdown knowledge)
# ============================================================================

class MarkdownManufacturerEntry(BaseModel):
    """A manufacturer entry parsed from markdown knowledge files."""
    name: str = Field(..., description="Manufacturer name")
    origin: str | None = Field(None, description="Country/origin")
    specialization: str | None = Field(None, description="Main specialization")
    website: str | None = Field(None, description="Website URL")
    founded: str | None = Field(None, description="Year founded")
    certifications: str | None = Field(None, description="Certifications held")
    knowledge_source: str | None = Field(None, description="Source knowledge file slug")


class MarkdownManufacturersResponse(BaseModel):
    """Response for markdown manufacturer queries."""
    total_count: int = Field(0)
    category: str | None = Field(None)
    search_query: str | None = Field(None)
    entries: list[MarkdownManufacturerEntry] = Field(default_factory=list)

    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# KNOWLEDGE SUMMARY
# ============================================================================

class KnowledgeSummaryResponse(BaseModel):
    """Summary of all loaded markdown knowledge."""
    total_files: int = Field(0)
    total_lines: int = Field(0)
    total_tables: int = Field(0)
    total_manufacturers: int = Field(0)
    total_erfahrungsberichte: int = Field(0)
    total_faq: int = Field(0)
    total_glossary: int = Field(0)
    total_fehlerbilder: int = Field(0)
    total_fallstudien: int = Field(0)
    total_expert_references: int = Field(0)
    legacy_databases: dict = Field(default_factory=dict, description="Legacy deep_*.py database counts")

    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# CORPUS BROWSING — the 252 research documents as a user-facing lexicon
# ============================================================================

class CorpusDocumentSummary(BaseModel):
    """Summary of one research document for the category browse view."""
    key: str = Field(..., description="Lookup key for /corpus/documents/{key} (slug or composite key)")
    title: str = Field(..., description="Document title (from first H1)")
    category: str = Field(..., description="Corpus category number, e.g. '01'")
    subcategory: str = Field(..., description="Document number within the category, e.g. '05'")
    line_count: int = Field(0)
    table_count: int = Field(0)
    faq_count: int = Field(0)
    fehlerbilder_count: int = Field(0)
    fallstudien_count: int = Field(0)


class CorpusCategory(BaseModel):
    """One of the corpus categories (01-31) with its documents."""
    id: str = Field(..., description="Category number, e.g. '01'")
    name: str = Field(..., description="German category name, e.g. 'Dichtungen und Profile'")
    document_count: int = Field(0)
    documents: list[CorpusDocumentSummary] = Field(default_factory=list)


class CorpusCategoriesResponse(BaseModel):
    """Browse structure of the full research corpus."""
    total_categories: int = Field(0)
    total_documents: int = Field(0)
    categories: list[CorpusCategory] = Field(default_factory=list)

    model_config = ConfigDict(from_attributes=True)


class CorpusTable(BaseModel):
    """A parsed markdown table with explicit column order.

    Explicit `columns` (instead of row dicts) because JS object-key iteration
    reorders integer-like keys (e.g. engine-model headers like "2003"),
    which would scramble comparison tables in the article view.
    """
    columns: list[str] = Field(default_factory=list)
    rows: list[list[str]] = Field(default_factory=list)


class CorpusSection(BaseModel):
    """Recursive section of a parsed research document."""
    title: str = Field("")
    level: int = Field(0)
    text: str = Field("", description="Section body text (markdown source, tables extracted)")
    tables: list[CorpusTable] = Field(default_factory=list)
    subsections: list["CorpusSection"] = Field(default_factory=list)


CorpusSection.model_rebuild()


class CorpusDocumentResponse(BaseModel):
    """A full research document, parsed into a section hierarchy."""
    key: str = Field(...)
    file: str = Field(..., description="Source filename, e.g. '01_02_fenster_dichtungen.md'")
    category: str = Field(...)
    category_name: str = Field(...)
    subcategory: str = Field(...)
    slug: str = Field(...)
    title: str = Field(...)
    line_count: int = Field(0)
    sections: CorpusSection = Field(..., description="Root section containing the full hierarchy")

    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# ERROR RESPONSES
# ============================================================================

class KnowledgeErrorResponse(BaseModel):
    """Error response for knowledge API."""
    detail: str = Field(..., description="Error message")
    error_code: str | None = Field(None, description="Machine-readable error code")
    parameters_received: dict | None = Field(None, description="Parameters that were received")
