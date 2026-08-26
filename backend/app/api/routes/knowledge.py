# backend/app/api/routes/knowledge.py
"""
REST API router for the AYDI Knowledge System.

Exposes the comprehensive yacht design knowledge database via REST endpoints.
No authentication required — knowledge is public read-only information and the
Level-1 marketing funnel (product pillar 1: user-facing lexicon). Tiered depth
(`KNOWLEDGE_BASE_FULL`) is a deliberate follow-up product decision.

Endpoints:
  GET /api/v1/knowledge/categories - List all knowledge categories (legacy index)
  GET /api/v1/knowledge/corpus/categories - Browse the 31 research-corpus categories
  GET /api/v1/knowledge/corpus/documents/{key} - Read one full research document
  GET /api/v1/knowledge/materials - Get material-specific knowledge
  GET /api/v1/knowledge/manufacturer/{name} - Get manufacturer profile
  GET /api/v1/knowledge/degradation - Get degradation patterns
  GET /api/v1/knowledge/compliance - Get compliance standards
  GET /api/v1/knowledge/systems - Get system-specific knowledge
  GET /api/v1/knowledge/search - Full-text search across databases
"""

import asyncio
import logging
import re
from typing import Optional
from fastapi import APIRouter, HTTPException, Query

from app.services.knowledge.KNOWLEDGE_INDEX import KNOWLEDGE_INDEX
from app.services.knowledge.knowledge_retrieval import (
    get_knowledge_for_materials_analysis,
    get_knowledge_for_structural_analysis,
    get_knowledge_for_compliance,
    get_knowledge_for_service_patterns,
    get_manufacturer_knowledge,
    list_available_knowledge_databases,
    format_knowledge_for_prompt,
    # New markdown-powered retrieval functions
    get_all_faq_knowledge,
    get_all_glossary_knowledge,
    get_all_fehlerbilder_knowledge,
    get_all_fallstudien_knowledge,
    get_all_manufacturers_knowledge,
    get_all_expert_references_knowledge,
    search_knowledge as search_all_knowledge,
    MARKDOWN_LOADER_AVAILABLE,
)
from app.services.knowledge.markdown_knowledge_loader import (
    get_markdown_knowledge_summary,
    get_markdown_knowledge,
    get_knowledge_by_slug,
)
from app.schemas.knowledge import (
    KnowledgeIndexResponse,
    KnowledgeCategoryStatus,
    MaterialsKnowledgeResponse,
    MaterialKnowledge,
    ManufacturerResponse,
    ManufacturerProfile,
    DegradationResponse,
    DegradationCycle,
    LifespanData,
    ComplianceResponse,
    StandardRequirement,
    SystemsResponse,
    SystemKnowledge,
    SearchResponse,
    SearchMatch,
    KnowledgeErrorResponse,
    # New schemas for markdown knowledge
    FAQEntry,
    FAQResponse,
    GlossaryEntry,
    GlossaryResponse,
    FehlerbildEntry,
    FehlerbilderResponse,
    FallstudieEntry,
    FallstudienResponse,
    MarkdownManufacturerEntry,
    MarkdownManufacturersResponse,
    KnowledgeSummaryResponse,
    # Corpus browsing (user-facing lexicon)
    CorpusDocumentSummary,
    CorpusCategory,
    CorpusCategoriesResponse,
    CorpusTable,
    CorpusSection,
    CorpusDocumentResponse,
)

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/knowledge",
    tags=["knowledge"],
    responses={
        404: {"model": KnowledgeErrorResponse, "description": "Knowledge not found"},
        400: {"model": KnowledgeErrorResponse, "description": "Invalid parameters"},
    },
)


# ============================================================================
# KNOWLEDGE CATEGORIES ENDPOINT
# ============================================================================

@router.get("/categories", response_model=KnowledgeIndexResponse, status_code=200)
async def get_knowledge_categories():
    """
    Get the KNOWLEDGE_INDEX overview with all top-level categories and their status.

    Returns information about all knowledge categories, including implementation
    status (implemented/partial/missing), entry counts, and descriptions.

    Returns:
        KnowledgeIndexResponse: Complete knowledge system index
    """
    categories: list[KnowledgeCategoryStatus] = []
    implemented = 0
    partial = 0

    for category_id, category_data in KNOWLEDGE_INDEX.items():
        status = category_data.get("status", "missing")
        if status == "implemented":
            implemented += 1
        elif status == "partial":
            partial += 1

        categories.append(
            KnowledgeCategoryStatus(
                category_id=category_id,
                title=category_data.get("title", category_id),
                status=status,
                description=category_data.get("description"),
                entry_count=category_data.get("entries", 0),
            )
        )

    return KnowledgeIndexResponse(
        total_categories=len(KNOWLEDGE_INDEX),
        implemented_count=implemented,
        partial_count=partial,
        categories=sorted(categories, key=lambda c: c.category_id),
    )


# ============================================================================
# MATERIALS KNOWLEDGE ENDPOINT
# ============================================================================

@router.get(
    "/materials",
    response_model=MaterialsKnowledgeResponse,
    status_code=200,
)
async def get_materials_knowledge(
    hull_material: Optional[str] = Query(
        None,
        description="Hull material (e.g., grp, carbon, wood, aluminum, steel)",
    ),
    hull_construction: Optional[str] = Query(
        None,
        description="Hull construction method (e.g., resin_infusion, hand_layup, vacuum_infusion)",
    ),
    core_material: Optional[str] = Query(
        None,
        description="Core material for sandwich construction (e.g., pvc_foam, balsa, airex)",
    ),
):
    """
    Get material-specific knowledge for a given composition.

    Retrieves technical data about resins, fibers, gelcoats, core materials,
    and their interactions. Returns material properties, lifespan, failure modes,
    and recommendations.

    Query Parameters:
        hull_material: Primary hull material type
        hull_construction: Construction method used
        core_material: Core material if sandwich construction

    Returns:
        MaterialsKnowledgeResponse: Material technical knowledge and recommendations
    """
    try:
        # Retrieve material knowledge from the service
        knowledge_data = get_knowledge_for_materials_analysis(
            hull_material=hull_material,
            hull_construction=hull_construction,
            core_material=core_material,
        )

        # Extract and structure the response
        materials_list: list[MaterialKnowledge] = []

        # Process resin data if available
        if "resins" in knowledge_data:
            for resin in knowledge_data["resins"]:
                if isinstance(resin, dict):
                    materials_list.append(
                        MaterialKnowledge(
                            material_type="resin",
                            name=resin.get("name", "Unknown"),
                            properties=resin.get("properties", {}),
                            lifespan_years=resin.get("lifespan_years"),
                            failure_modes=resin.get("failure_modes", []),
                            maintenance_notes=resin.get("maintenance_notes"),
                            common_issues=resin.get("common_issues", []),
                        )
                    )

        # Process fiber data if available
        if "fibers" in knowledge_data:
            for fiber in knowledge_data["fibers"]:
                if isinstance(fiber, dict):
                    materials_list.append(
                        MaterialKnowledge(
                            material_type="fiber",
                            name=fiber.get("name", "Unknown"),
                            properties=fiber.get("properties", {}),
                            lifespan_years=fiber.get("lifespan_years"),
                            failure_modes=fiber.get("failure_modes", []),
                            maintenance_notes=fiber.get("maintenance_notes"),
                            common_issues=fiber.get("common_issues", []),
                        )
                    )

        # Process core material data if available
        if "core_materials" in knowledge_data:
            for core in knowledge_data["core_materials"]:
                if isinstance(core, dict):
                    materials_list.append(
                        MaterialKnowledge(
                            material_type="core",
                            name=core.get("name", "Unknown"),
                            properties=core.get("properties", {}),
                            lifespan_years=core.get("lifespan_years"),
                            failure_modes=core.get("failure_modes", []),
                            maintenance_notes=core.get("maintenance_notes"),
                            common_issues=core.get("common_issues", []),
                        )
                    )

        return MaterialsKnowledgeResponse(
            hull_material=hull_material,
            hull_construction=hull_construction,
            core_material=core_material,
            materials=materials_list,
            recommendations=knowledge_data.get("recommendations", []),
            warnings=knowledge_data.get("warnings", []),
        )

    except Exception as e:
        logger.error("Error retrieving materials knowledge: %s", e)
        raise HTTPException(
            status_code=500,
            detail="Failed to retrieve materials knowledge",
        )


# ============================================================================
# MANUFACTURER KNOWLEDGE ENDPOINT
# ============================================================================

@router.get(
    "/manufacturer/{name}",
    response_model=ManufacturerResponse,
    status_code=200,
)
async def get_manufacturer_profile(name: str):
    """
    Get manufacturer profile from the knowledge databases.

    Retrieves known patterns, reputation, strengths, weaknesses, and typical
    issues for a specific yacht manufacturer.

    Path Parameters:
        name: Manufacturer name or brand

    Returns:
        ManufacturerResponse: Manufacturer profile with historical patterns
    """
    try:
        if not name or len(name.strip()) < 2:
            raise HTTPException(
                status_code=400,
                detail="Manufacturer name must be at least 2 characters",
            )

        knowledge_data = get_manufacturer_knowledge(builder_name=name)

        # get_manufacturer_knowledge() returns the profile dict DIRECTLY (or {}
        # / only markdown_matches) — there is no 'found'/'profile' wrapper.
        # The previous wrapper check made every real match report "not found".
        markdown_matches = knowledge_data.get("markdown_matches") or []
        profile_data = {
            k: v for k, v in knowledge_data.items() if k != "markdown_matches"
        }

        if not profile_data and not markdown_matches:
            return ManufacturerResponse(
                manufacturer=None,
                message=f"No knowledge base entry found for manufacturer '{name}'",
            )

        # Map the real DB field names (aging_lifecycle_manufacturers_deep.py:
        # key_de, business_model, build_quality_assessment, known_problems,
        # notes) defensively onto the response schema.
        quality_assessment = profile_data.get("build_quality_assessment")
        if not isinstance(quality_assessment, dict):
            quality_assessment = {}

        raw_problems = profile_data.get("known_problems") or []
        if isinstance(raw_problems, str):
            # Some profiles carry a single string here (e.g. Dehler:
            # "virtually_none_documented_...") — iterating it directly would
            # char-split it into 48 one-letter "weaknesses".
            raw_problems = [raw_problems]
        known_weaknesses = profile_data.get("known_weaknesses") or [
            str(p.get("issue", p)) if isinstance(p, dict) else str(p)
            for p in raw_problems
        ]

        expert_opinions = [str(o) for o in profile_data.get("expert_opinions", [])]
        if profile_data.get("notes"):
            expert_opinions.append(str(profile_data["notes"]))
        for match in markdown_matches:
            expert_opinions.append(
                f"{match.get('name', '')} — {match.get('specialization', '')} "
                f"(Quelle: {match.get('source', '')})".strip()
            )

        try:
            reputation_score = float(profile_data.get("reputation_score", 0.0))
        except (TypeError, ValueError):
            reputation_score = 0.0

        manufacturer = ManufacturerProfile(
            manufacturer_name=str(profile_data.get("key_de") or name),
            reputation_score=max(0.0, min(100.0, reputation_score)),
            known_strengths=[str(s) for s in profile_data.get("known_strengths", [])],
            known_weaknesses=[str(w) for w in known_weaknesses],
            quality_tier=profile_data.get("quality_tier")
            or quality_assessment.get("current_reputation")
            or quality_assessment.get("general"),
            construction_methods=[
                str(c) for c in profile_data.get("construction_methods", [])
            ],
            material_preferences=profile_data.get("material_preferences") or {},
            production_type=profile_data.get("production_type")
            or profile_data.get("business_model"),
            typical_issues_by_age=profile_data.get("typical_issues_by_age")
            or quality_assessment,
            expert_opinions=expert_opinions,
        )

        return ManufacturerResponse(
            manufacturer=manufacturer,
            message=f"Knowledge base profile for {name}",
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error("Error retrieving manufacturer knowledge: %s", e)
        raise HTTPException(
            status_code=500,
            detail="Failed to retrieve manufacturer knowledge",
        )


# ============================================================================
# DEGRADATION & LIFECYCLE ENDPOINT
# ============================================================================

@router.get(
    "/degradation",
    response_model=DegradationResponse,
    status_code=200,
)
async def get_degradation_knowledge(
    hull_material: Optional[str] = Query(None, description="Hull material (e.g., grp, carbon)"),
    core_material: Optional[str] = Query(None, description="Core material (e.g., balsa, pvc_foam)"),
):
    """
    Get degradation patterns, cycles, and material lifespans.

    Returns information about how materials degrade over time, typical onset
    of degradation, failure probabilities, and prevention measures.

    Query Parameters:
        hull_material: Hull material to analyze
        core_material: Core material to analyze

    Returns:
        DegradationResponse: Degradation cycles, lifespans, and risk factors
    """
    try:
        # For now, return a comprehensive but generic response
        # In production, this would pull from aging_lifecycle_manufacturers_deep.py
        degradation_cycles: list[DegradationCycle] = [
            DegradationCycle(
                name="Osmotic Blistering (GFK)",
                description="Water absorption causing blisters in polyester/vinylester hulls",
                onset_years=5.0,
                duration_years=10.0,
                severity="moderate",
            ),
            DegradationCycle(
                name="Gelcoat Crazing",
                description="Fine cracks in gelcoat surface from UV and stress",
                onset_years=3.0,
                duration_years=15.0,
                severity="mild",
            ),
            DegradationCycle(
                name="Core Delamination",
                description="Separation between skin and core material",
                onset_years=8.0,
                duration_years=5.0,
                severity="severe",
            ),
        ]

        lifespan_data: list[LifespanData] = [
            LifespanData(
                component="GFK Hull (Polyester)",
                lifespan_years=30.0,
                maintenance_intervals_months=[12, 24, 36],
                failure_probability_percent=15.0,
            ),
            LifespanData(
                component="PVC Foam Core",
                lifespan_years=25.0,
                maintenance_intervals_months=[24, 48],
                failure_probability_percent=20.0,
            ),
        ]

        return DegradationResponse(
            hull_material=hull_material,
            core_material=core_material,
            degradation_cycles=degradation_cycles,
            lifespan_data=lifespan_data,
            risk_factors=[
                "UV exposure",
                "Water immersion cycles",
                "Temperature fluctuations",
                "Poor maintenance",
                "Manufacturing defects",
            ],
            prevention_measures=[
                "Regular UV protection (waxing/varnish)",
                "Proper ventilation to prevent moisture",
                "Annual bottom inspection",
                "Preventive maintenance on seals",
                "Climate-controlled storage when possible",
            ],
        )

    except Exception as e:
        logger.error("Error retrieving degradation knowledge: %s", e)
        raise HTTPException(
            status_code=500,
            detail="Failed to retrieve degradation knowledge",
        )


# ============================================================================
# COMPLIANCE & STANDARDS ENDPOINT
# ============================================================================

@router.get(
    "/compliance",
    response_model=ComplianceResponse,
    status_code=200,
)
async def get_compliance_standards(
    propulsion: Optional[str] = Query(
        None,
        description="Propulsion type: sail, motor, hybrid, trawler",
    ),
    length_m: Optional[float] = Query(
        None,
        ge=5.0,
        le=500.0,
        description="Vessel length in meters",
    ),
    operating_waters: Optional[str] = Query(
        None,
        description="Operating waters: inland, coastal, offshore",
    ),
):
    """
    Get applicable compliance standards and safety requirements.

    Returns standards that apply based on vessel type, size, and operating
    area. Includes structural, safety, and electrical requirements.

    Query Parameters:
        propulsion: Type of propulsion
        length_m: Vessel length in meters
        operating_waters: Typical operating area

    Returns:
        ComplianceResponse: Applicable standards and requirements
    """
    try:
        # Retrieve compliance knowledge
        compliance_data = get_knowledge_for_compliance(
            propulsion=propulsion,
            length_m=length_m,
            operating_waters=operating_waters,
        )

        standards: list[StandardRequirement] = [
            StandardRequirement(
                standard_code="ISO 12215",
                description="Small craft stability and buoyancy",
                applies=True if length_m and length_m <= 24 else False,
                risk_if_not_met="Capsizing or sinking in rough conditions",
            ),
            StandardRequirement(
                standard_code="ISO 9650",
                description="Inflatable life jackets and buoyancy aids",
                applies=True,
                risk_if_not_met="Inability to rescue persons from water",
            ),
            StandardRequirement(
                standard_code="IEC 60092",
                description="Electrical installations in ships",
                applies=bool(propulsion and "motor" in propulsion.lower()),
                risk_if_not_met="Electrical fire, electrocution",
            ),
        ]

        safety_reqs = [
            "Life jackets for all crew",
            "First aid kit",
            "Fire extinguishers appropriate for vessel class",
            "Safety harnesses and deck safety equipment",
        ]

        structural_reqs = [
            "Hull certification for vessel class",
            "Proper scantlings for hull, deck, and keel",
            "Stress analysis for major structural components",
        ]

        return ComplianceResponse(
            propulsion=propulsion,
            length_m=length_m,
            operating_waters=operating_waters,
            applicable_standards=standards,
            safety_requirements=safety_reqs,
            structural_requirements=structural_reqs,
            notes=compliance_data.get("notes", ""),
        )

    except Exception as e:
        logger.error("Error retrieving compliance knowledge: %s", e)
        raise HTTPException(
            status_code=500,
            detail="Failed to retrieve compliance knowledge",
        )


# ============================================================================
# SYSTEMS KNOWLEDGE ENDPOINT
# ============================================================================

@router.get(
    "/systems",
    response_model=SystemsResponse,
    status_code=200,
)
async def get_systems_knowledge(
    system_type: Optional[str] = Query(
        None,
        description="System type: engine, electrical, sanitary, rigging, steering, cooling, fuel",
    ),
):
    """
    Get system-specific knowledge for maintenance and troubleshooting.

    Returns detailed information about yacht systems, including components,
    common issues, maintenance schedules, and failure modes.

    Query Parameters:
        system_type: Type of system to retrieve knowledge for

    Returns:
        SystemsResponse: System-specific knowledge and recommendations
    """
    try:
        if not system_type:
            return SystemsResponse(
                system_type=None,
                systems=[],
                general_notes="Specify system_type parameter to retrieve knowledge",
            )

        system_type_lower = system_type.lower().strip()

        # Build system knowledge based on type
        systems_list: list[SystemKnowledge] = []

        if system_type_lower in ["engine", "motor", "diesel"]:
            systems_list.append(
                SystemKnowledge(
                    system_type="engine",
                    components=[
                        "Engine block",
                        "Cylinder head",
                        "Fuel injectors",
                        "Turbocharger (if equipped)",
                        "Cooling system",
                        "Exhaust manifold",
                    ],
                    common_issues=[
                        "Fuel injector fouling",
                        "Turbo wastegate sticking",
                        "Coolant leaks at hose connections",
                        "Carbon buildup in combustion chambers",
                    ],
                    maintenance_schedule={
                        "oil_change_hours": 500,
                        "fuel_filter_hours": 500,
                        "coolant_flush_months": 24,
                        "impeller_inspection_months": 12,
                    },
                    failure_modes=[
                        "Cavitation erosion in cooling passages",
                        "Fuel line corrosion",
                        "Bearing wear",
                    ],
                    upgrade_considerations=[
                        "High-capacity fuel filter upgrade",
                        "Secondary oil filter system",
                        "Engine monitoring system",
                    ],
                    expert_recommendations=[
                        "Use stabilized fuel for seasonal storage",
                        "Run engine under load monthly to prevent carbon",
                        "Monitor coolant condition quarterly",
                    ],
                )
            )

        elif system_type_lower in ["electrical", "electric", "battery"]:
            systems_list.append(
                SystemKnowledge(
                    system_type="electrical",
                    components=[
                        "Battery banks",
                        "Alternator",
                        "Shore power converter",
                        "Main distribution panel",
                        "Wiring and connections",
                        "Corrosion protection",
                    ],
                    common_issues=[
                        "Corroded terminals",
                        "Undersized cables",
                        "Shore power contactor failure",
                        "Alternator output issues",
                    ],
                    maintenance_schedule={
                        "terminal_inspection_months": 3,
                        "battery_specific_gravity_months": 6,
                        "wiring_insulation_test_months": 24,
                    },
                    failure_modes=[
                        "Galvanic corrosion at copper/aluminum junction",
                        "Battery stratification",
                        "Reverse polarity damage",
                    ],
                    upgrade_considerations=[
                        "Lithium battery systems",
                        "MPPT solar charge controller",
                        "Battery monitoring system",
                    ],
                    expert_recommendations=[
                        "Use tinned copper wire only",
                        "Install isolation switches on all major circuits",
                        "Use hot-shrink tubing on all exposed connections",
                    ],
                )
            )

        elif system_type_lower in ["sanitary", "plumbing", "water"]:
            systems_list.append(
                SystemKnowledge(
                    system_type="sanitary",
                    components=[
                        "Through-hulls and seacocks",
                        "Toilet systems",
                        "Holding tanks",
                        "Water tanks",
                        "Piping and hoses",
                    ],
                    common_issues=[
                        "Seacock deterioration",
                        "Hose cracking and splitting",
                        "Holding tank odors",
                        "Through-hull failure",
                    ],
                    maintenance_schedule={
                        "seacock_operation_months": 3,
                        "hose_visual_inspection_months": 6,
                        "tank_inspection_months": 12,
                    },
                    failure_modes=[
                        "Dezincification of brass seacocks",
                        "Saltwater corrosion of valves",
                        "Hose burst from pressure or age",
                    ],
                    upgrade_considerations=[
                        "Chrome-plated bronze seacocks",
                        "Antimicrobial piping",
                        "Integrated shutoff valves",
                    ],
                    expert_recommendations=[
                        "Open and close all seacocks monthly",
                        "Keep backup through-hull plugs onboard",
                        "Inspect all hose clips for corrosion",
                    ],
                )
            )

        return SystemsResponse(
            system_type=system_type,
            systems=systems_list,
            general_notes=f"Knowledge for {system_type} systems" if systems_list else f"No knowledge available for system type: {system_type}",
        )

    except Exception as e:
        logger.error("Error retrieving systems knowledge: %s", e)
        raise HTTPException(
            status_code=500,
            detail="Failed to retrieve systems knowledge",
        )


# ============================================================================
# FULL-TEXT SEARCH ENDPOINT
# ============================================================================

@router.get(
    "/search",
    response_model=SearchResponse,
    status_code=200,
)
async def search_knowledge(
    q: str = Query(..., min_length=2, max_length=200, description="Search query"),
):
    """
    Full-text search across all knowledge databases.

    Searches for matching entries in all knowledge modules and returns
    relevant results with relevance scores.

    Query Parameters:
        q: Search query (minimum 2 characters)

    Returns:
        SearchResponse: Matching knowledge entries with relevance scores
    """
    try:
        if not q or len(q.strip()) < 2:
            raise HTTPException(
                status_code=400,
                detail="Search query must be at least 2 characters",
            )

        import time
        start_time = time.time()

        # Warm the corpus cache off the event loop (cold-start parse ~15s)
        if MARKDOWN_LOADER_AVAILABLE:
            await asyncio.to_thread(get_markdown_knowledge)

        search_query = q.lower().strip()
        matches: list[SearchMatch] = []

        # Search in KNOWLEDGE_INDEX
        for category_id, category_data in KNOWLEDGE_INDEX.items():
            title = category_data.get("title", "").lower()
            description = category_data.get("description", "").lower()

            if search_query in title or search_query in description:
                matches.append(
                    SearchMatch(
                        category=category_id,
                        database="KNOWLEDGE_INDEX",
                        entry_name=category_data.get("title", category_id),
                        excerpt=category_data.get("description", "")[:200],
                        relevance_score=1.0 if search_query in title else 0.7,
                    )
                )

        # Search corpus document titles — these open as full articles in the UI
        # (database="markdown_document", category=<document key>)
        if MARKDOWN_LOADER_AVAILABLE:
            try:
                cat_titles = _corpus_category_titles()
                for doc_key, doc in get_markdown_knowledge().items():
                    doc_title = (doc.get("title") or "").lower()
                    if search_query in doc_title or search_query in doc_key.lower():
                        cat_name = cat_titles.get(
                            doc["category"], f"Kategorie {doc['category']}"
                        )
                        matches.append(
                            SearchMatch(
                                category=doc_key,
                                database="markdown_document",
                                entry_name=doc.get("title") or doc_key,
                                excerpt=(
                                    f"Fachartikel · {cat_name} · "
                                    f"{doc.get('line_count', 0)} Zeilen"
                                ),
                                relevance_score=0.95,
                            )
                        )
            except Exception:
                logger.exception("Error searching corpus document titles")

        # Search in markdown knowledge (FAQ, Glossar, Fehlerbilder, Erfahrungsberichte)
        if MARKDOWN_LOADER_AVAILABLE:
            try:
                md_results = search_all_knowledge(q, max_results=30)
                for md_result in md_results:
                    result_type = md_result.get("type", "unknown")
                    if result_type == "faq":
                        matches.append(SearchMatch(
                            category=md_result.get("source", ""),
                            database="markdown_faq",
                            entry_name=md_result.get("question_de", "")[:100],
                            excerpt=md_result.get("answer_de", "")[:200],
                            relevance_score=0.9,
                            full_content=md_result,
                        ))
                    elif result_type == "glossary":
                        matches.append(SearchMatch(
                            category=md_result.get("source", ""),
                            database="markdown_glossary",
                            entry_name=md_result.get("term_de", "")[:100],
                            excerpt=md_result.get("definition", "")[:200],
                            relevance_score=0.85,
                            full_content=md_result,
                        ))
                    elif result_type == "fehlerbild":
                        matches.append(SearchMatch(
                            category=md_result.get("source", ""),
                            database="markdown_fehlerbilder",
                            entry_name=md_result.get("fehlerbild_title", "")[:100],
                            excerpt=md_result.get("symptom_de", "")[:200],
                            relevance_score=0.88,
                            full_content=md_result,
                        ))
                    elif result_type == "erfahrungsbericht":
                        matches.append(SearchMatch(
                            category=md_result.get("source", ""),
                            database="markdown_erfahrungsberichte",
                            entry_name=md_result.get("forum", "Forum"),
                            excerpt=md_result.get("text", "")[:200],
                            relevance_score=0.75,
                            full_content=md_result,
                        ))
            except Exception:
                logger.exception("Error searching markdown knowledge")

        # Search in legacy databases
        try:
            databases = list_available_knowledge_databases()
            for db_name, count in databases.items():
                if search_query in db_name.lower():
                    matches.append(
                        SearchMatch(
                            category="databases",
                            database="knowledge_retrieval",
                            entry_name=db_name,
                            excerpt=f"Database with {count} entries",
                            relevance_score=0.8,
                        )
                    )
        except Exception:
            # Die Korpus-Suche ist Anreicherung — ein Fehler darf die uebrigen
            # Treffer nicht kosten. Er darf aber auch nicht spurlos verschwinden:
            # Zuvor stand hier ein nacktes `pass`, wodurch eine dauerhaft
            # kaputte Suche als "keine Treffer" erschien und in keinem Log auftauchte.
            logger.exception("Korpus-Suche fehlgeschlagen; liefere die uebrigen Treffer")

        elapsed_ms = (time.time() - start_time) * 1000
        matches.sort(key=lambda m: m.relevance_score, reverse=True)

        return SearchResponse(
            query=q,
            results_count=len(matches),
            matches=matches[:50],
            search_time_ms=round(elapsed_ms, 2),
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error("Error searching knowledge: %s", e)
        raise HTTPException(
            status_code=500,
            detail="Failed to search knowledge databases",
        )


# ============================================================================
# MARKDOWN KNOWLEDGE ENDPOINTS — FAQ, Glossar, Fehlerbilder, Fallstudien
# ============================================================================


@router.get("/faq", response_model=FAQResponse, status_code=200)
async def get_faq_entries(
    category: Optional[str] = Query(
        None,
        description="Filter by category (e.g. '01', '02', '03', '04', '05', '06')",
    ),
    q: Optional[str] = Query(
        None,
        min_length=2,
        max_length=200,
        description="Search in questions and answers",
    ),
    max_results: int = Query(50, ge=1, le=500, description="Max results"),
):
    """
    Get FAQ entries from the markdown knowledge database.

    Searches across all 72 knowledge files and returns matching FAQ entries.
    Supports filtering by category and keyword search.

    Returns:
        FAQResponse: List of FAQ entries with source attribution
    """
    try:
        entries = get_all_faq_knowledge(
            category=category,
            search_query=q,
            max_results=max_results,
        )
        return FAQResponse(
            total_count=len(entries),
            category=category,
            search_query=q,
            entries=[
                FAQEntry(
                    question_de=e.get("question_de", ""),
                    answer_de=e.get("answer_de", ""),
                    confidence=e.get("confidence", "documented"),
                    knowledge_source=e.get("knowledge_source"),
                )
                for e in entries
            ],
        )
    except Exception as e:
        logger.error("Error retrieving FAQ knowledge: %s", e)
        raise HTTPException(status_code=500, detail="Failed to retrieve FAQ entries")


@router.get("/glossar", response_model=GlossaryResponse, status_code=200)
async def get_glossary_entries(
    category: Optional[str] = Query(None, description="Filter by category"),
    q: Optional[str] = Query(None, min_length=2, max_length=200, description="Search term"),
    max_results: int = Query(100, ge=1, le=1000),
):
    """
    Get glossary entries from the markdown knowledge database.

    Returns all glossary terms with German and English translations and definitions.
    """
    try:
        entries = get_all_glossary_knowledge(
            category=category,
            search_query=q,
            max_results=max_results,
        )
        return GlossaryResponse(
            total_count=len(entries),
            category=category,
            search_query=q,
            entries=[
                GlossaryEntry(
                    term_de=e.get("term_de"),
                    term_en=e.get("term_en"),
                    definition=e.get("definition"),
                    knowledge_source=e.get("knowledge_source"),
                )
                for e in entries
            ],
        )
    except Exception as e:
        logger.error("Error retrieving glossary: %s", e)
        raise HTTPException(status_code=500, detail="Failed to retrieve glossary entries")


@router.get("/fehlerbilder", response_model=FehlerbilderResponse, status_code=200)
async def get_fehlerbilder(
    category: Optional[str] = Query(None, description="Filter by category"),
    q: Optional[str] = Query(None, min_length=2, max_length=200, description="Search in title/text"),
    max_results: int = Query(50, ge=1, le=500),
):
    """
    Get failure pattern entries (Fehlerbilder) from the markdown knowledge database.

    Returns structured failure patterns with symptoms, causes, and corrective actions.
    """
    try:
        entries = get_all_fehlerbilder_knowledge(
            category=category,
            search_query=q,
            max_results=max_results,
        )
        return FehlerbilderResponse(
            total_count=len(entries),
            category=category,
            search_query=q,
            entries=[
                FehlerbildEntry(
                    title_de=e.get("title_de", ""),
                    symptom_de=e.get("symptom_de"),
                    ursache_de=e.get("ursache_de"),
                    massnahme_de=e.get("massnahme_de"),
                    haeufigkeit_de=e.get("haeufigkeit_de"),
                    confidence=e.get("confidence"),
                    knowledge_source=e.get("knowledge_source"),
                )
                for e in entries
            ],
        )
    except Exception as e:
        logger.error("Error retrieving fehlerbilder: %s", e)
        raise HTTPException(status_code=500, detail="Failed to retrieve failure patterns")


@router.get("/fallstudien", response_model=FallstudienResponse, status_code=200)
async def get_fallstudien(
    category: Optional[str] = Query(None, description="Filter by category"),
    q: Optional[str] = Query(None, min_length=2, max_length=200, description="Search in title/text"),
    max_results: int = Query(50, ge=1, le=500),
):
    """
    Get case studies (Fallstudien) from the markdown knowledge database.

    Returns real-world case studies with situation, diagnosis, result, and lessons learned.
    """
    try:
        entries = get_all_fallstudien_knowledge(
            category=category,
            search_query=q,
            max_results=max_results,
        )
        return FallstudienResponse(
            total_count=len(entries),
            category=category,
            search_query=q,
            entries=[
                FallstudieEntry(
                    title_de=e.get("title_de", ""),
                    situation_de=e.get("situation_de"),
                    diagnose_de=e.get("diagnose_de"),
                    ursache_de=e.get("ursache_de"),
                    ergebnis_de=e.get("ergebnis_de"),
                    kosten_de=e.get("kosten_de"),
                    lehre_de=e.get("lehre_de"),
                    confidence=e.get("confidence"),
                    knowledge_source=e.get("knowledge_source"),
                )
                for e in entries
            ],
        )
    except Exception as e:
        logger.error("Error retrieving fallstudien: %s", e)
        raise HTTPException(status_code=500, detail="Failed to retrieve case studies")


@router.get("/manufacturers/markdown", response_model=MarkdownManufacturersResponse, status_code=200)
async def get_markdown_manufacturers(
    category: Optional[str] = Query(None, description="Filter by category"),
    q: Optional[str] = Query(None, min_length=2, max_length=200, description="Search by name"),
    max_results: int = Query(100, ge=1, le=1000),
):
    """
    Get manufacturer profiles from the markdown knowledge database.

    Returns manufacturers extracted from all 72 knowledge files with specializations,
    origins, and certifications.
    """
    try:
        entries = get_all_manufacturers_knowledge(
            category=category,
            search_query=q,
            max_results=max_results,
        )
        return MarkdownManufacturersResponse(
            total_count=len(entries),
            category=category,
            search_query=q,
            entries=[
                MarkdownManufacturerEntry(
                    name=e.get("name", ""),
                    origin=e.get("origin"),
                    specialization=e.get("specialization"),
                    website=e.get("website"),
                    founded=e.get("founded"),
                    certifications=e.get("certifications"),
                    knowledge_source=e.get("knowledge_source"),
                )
                for e in entries
            ],
        )
    except Exception as e:
        logger.error("Error retrieving markdown manufacturers: %s", e)
        raise HTTPException(status_code=500, detail="Failed to retrieve manufacturer data")


@router.get("/summary", response_model=KnowledgeSummaryResponse, status_code=200)
async def get_knowledge_summary():
    """
    Get a complete summary of all loaded knowledge — both legacy databases
    and the 72 markdown knowledge files.

    Returns counts for files, lines, tables, FAQ, glossary, fehlerbilder,
    fallstudien, manufacturers, and expert references.
    """
    try:
        md_summary = get_markdown_knowledge_summary()
        legacy_dbs = list_available_knowledge_databases()

        # Filter legacy-only keys
        legacy_only = {
            k: v for k, v in legacy_dbs.items()
            if not k.startswith("MARKDOWN")
        }

        return KnowledgeSummaryResponse(
            total_files=md_summary.get("total_files", 0),
            total_lines=md_summary.get("total_lines", 0),
            total_tables=md_summary.get("total_tables", 0),
            total_manufacturers=md_summary.get("total_manufacturers", 0),
            total_erfahrungsberichte=md_summary.get("total_erfahrungsberichte", 0),
            total_faq=md_summary.get("total_faq", 0),
            total_glossary=md_summary.get("total_glossary", 0),
            total_fehlerbilder=md_summary.get("total_fehlerbilder", 0),
            total_fallstudien=md_summary.get("total_fallstudien", 0),
            total_expert_references=md_summary.get("total_expert_references", 0),
            legacy_databases=legacy_only,
        )
    except Exception as e:
        logger.error("Error retrieving knowledge summary: %s", e)
        raise HTTPException(status_code=500, detail="Failed to retrieve knowledge summary")


# ============================================================================
# CORPUS BROWSING ENDPOINTS — the research corpus as a user-facing lexicon
# ============================================================================

# Cached '01' -> 'Dichtungen und Profile' mapping, derived from the
# KNOWLEDGE_INDEX markdown section (single source of truth for naming).
_CORPUS_CATEGORY_TITLES: Optional[dict[str, str]] = None


def _corpus_category_titles() -> dict[str, str]:
    """Parse category names from KNOWLEDGE_INDEX['22_markdown_knowledge']."""
    global _CORPUS_CATEGORY_TITLES
    if _CORPUS_CATEGORY_TITLES is None:
        titles: dict[str, str] = {}
        md_section = KNOWLEDGE_INDEX.get("22_markdown_knowledge", {})
        for sub in md_section.get("subcategories", {}).values():
            title = sub.get("title", "")
            match = re.match(r"^(\d{2})\s*[—–-]\s*(.+)$", title)
            if match:
                titles[match.group(1)] = match.group(2).strip()
        _CORPUS_CATEGORY_TITLES = titles
    return _CORPUS_CATEGORY_TITLES


@router.get(
    "/corpus/categories",
    response_model=CorpusCategoriesResponse,
    status_code=200,
)
async def get_corpus_categories():
    """
    Browse structure of the full research corpus: all categories (01-31)
    with their documents, ready for the lexicon UI.

    Returns:
        CorpusCategoriesResponse: Categories with document summaries; each
        document's `key` can be resolved via GET /corpus/documents/{key}.
    """
    if not MARKDOWN_LOADER_AVAILABLE:
        raise HTTPException(status_code=503, detail="Knowledge corpus not available")

    try:
        # First call parses ~840K lines (~15s) — keep that off the event loop
        # (cold start would otherwise freeze /health and every other request).
        docs = await asyncio.to_thread(get_markdown_knowledge)
        titles = _corpus_category_titles()

        by_category: dict[str, list[tuple[str, dict]]] = {}
        for doc_key, doc in docs.items():
            by_category.setdefault(doc.get("category", "??"), []).append((doc_key, doc))

        categories: list[CorpusCategory] = []
        for cat_id in sorted(by_category):
            entries = sorted(
                by_category[cat_id],
                key=lambda kv: (kv[1].get("subcategory", ""), kv[0]),
            )
            documents = [
                CorpusDocumentSummary(
                    key=doc_key,
                    title=doc.get("title") or doc_key,
                    category=doc.get("category", ""),
                    subcategory=doc.get("subcategory", ""),
                    line_count=doc.get("line_count", 0),
                    table_count=len(doc.get("tables", [])),
                    faq_count=len(doc.get("faq", [])),
                    fehlerbilder_count=len(doc.get("fehlerbilder", [])),
                    fallstudien_count=len(doc.get("fallstudien", [])),
                )
                for doc_key, doc in entries
            ]
            categories.append(
                CorpusCategory(
                    id=cat_id,
                    name=titles.get(cat_id, f"Kategorie {cat_id}"),
                    document_count=len(documents),
                    documents=documents,
                )
            )

        return CorpusCategoriesResponse(
            total_categories=len(categories),
            total_documents=len(docs),
            categories=categories,
        )
    except Exception as e:
        logger.error("Error building corpus categories: %s", e)
        raise HTTPException(status_code=500, detail="Failed to load knowledge corpus")


def _table_to_schema(table: list) -> CorpusTable:
    """Convert loader row-dicts into an order-preserving columns/rows table."""
    if not table:
        return CorpusTable(columns=[], rows=[])
    columns = list(table[0].keys())  # Python dicts preserve insertion order
    rows = [[str(row.get(col, "")) for col in columns] for row in table]
    return CorpusTable(columns=columns, rows=rows)


def _section_to_schema(section: dict) -> CorpusSection:
    """Convert the loader's section dict into the response schema."""
    return CorpusSection(
        title=section.get("title", ""),
        level=section.get("level", 0),
        text="\n".join(section.get("content_lines", [])).strip(),
        tables=[_table_to_schema(t) for t in section.get("tables", [])],
        subsections=[
            _section_to_schema(sub) for sub in section.get("subsections", [])
        ],
    )


@router.get(
    "/corpus/documents/{key}",
    response_model=CorpusDocumentResponse,
    status_code=200,
)
async def get_corpus_document(key: str):
    """
    Read one full research document as a structured article (section
    hierarchy with text and tables) — the lexicon article view.

    Path Parameters:
        key: Document key from /corpus/categories (slug or composite key)

    Returns:
        CorpusDocumentResponse: Fully parsed document
    """
    if not MARKDOWN_LOADER_AVAILABLE:
        raise HTTPException(status_code=503, detail="Knowledge corpus not available")

    # Cold-start parse must not block the event loop (see corpus/categories).
    doc = await asyncio.to_thread(get_knowledge_by_slug, key)
    if doc is None:
        raise HTTPException(
            status_code=404,
            detail=f"Knowledge document '{key}' not found",
        )

    try:
        titles = _corpus_category_titles()
        return CorpusDocumentResponse(
            key=key,
            file=doc.get("file", ""),
            category=doc.get("category", ""),
            category_name=titles.get(
                doc.get("category", ""), f"Kategorie {doc.get('category', '')}"
            ),
            subcategory=doc.get("subcategory", ""),
            slug=doc.get("slug", key),
            title=doc.get("title") or key,
            line_count=doc.get("line_count", 0),
            sections=_section_to_schema(doc.get("sections", {})),
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.error("Error serializing corpus document '%s': %s", key, e)
        raise HTTPException(status_code=500, detail="Failed to load knowledge document")
