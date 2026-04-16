# backend/app/api/routes/knowledge.py
"""
REST API router for the AYDI Knowledge System.

Exposes the comprehensive yacht design knowledge database via REST endpoints.
No authentication required - knowledge is public information.

Endpoints:
  GET /api/v1/knowledge/categories - List all knowledge categories
  GET /api/v1/knowledge/materials - Get material-specific knowledge
  GET /api/v1/knowledge/manufacturer/{name} - Get manufacturer profile
  GET /api/v1/knowledge/degradation - Get degradation patterns
  GET /api/v1/knowledge/compliance - Get compliance standards
  GET /api/v1/knowledge/systems - Get system-specific knowledge
  GET /api/v1/knowledge/search - Full-text search across databases
"""

import logging
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query

from app.core.permissions import get_current_user
from app.models.models import User

from app.services.knowledge.KNOWLEDGE_INDEX import KNOWLEDGE_INDEX
from app.services.knowledge.knowledge_retrieval import (
    get_knowledge_for_materials_analysis,
    get_knowledge_for_structural_analysis,
    get_knowledge_for_compliance,
    get_knowledge_for_service_patterns,
    get_manufacturer_knowledge,
    list_available_knowledge_databases,
    format_knowledge_for_prompt,
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
async def get_knowledge_categories(_user: User = Depends(get_current_user)):
    """
    Get the KNOWLEDGE_INDEX overview with all 21 categories and their status.

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
    _user: User = Depends(get_current_user),
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
async def get_manufacturer_profile(name: str, _user: User = Depends(get_current_user)):
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

        if not knowledge_data or not knowledge_data.get("found"):
            return ManufacturerResponse(
                manufacturer=None,
                message=f"No knowledge base entry found for manufacturer '{name}'",
            )

        profile_data = knowledge_data.get("profile", {})

        manufacturer = ManufacturerProfile(
            manufacturer_name=name,
            reputation_score=profile_data.get("reputation_score", 0.0),
            known_strengths=profile_data.get("known_strengths", []),
            known_weaknesses=profile_data.get("known_weaknesses", []),
            quality_tier=profile_data.get("quality_tier"),
            construction_methods=profile_data.get("construction_methods", []),
            material_preferences=profile_data.get("material_preferences", {}),
            production_type=profile_data.get("production_type"),
            typical_issues_by_age=profile_data.get("typical_issues_by_age", {}),
            expert_opinions=profile_data.get("expert_opinions", []),
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
    _user: User = Depends(get_current_user),
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
    _user: User = Depends(get_current_user),
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
    _user: User = Depends(get_current_user),
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
    _user: User = Depends(get_current_user),
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

        # Simple search implementation - in production would use full-text indexing
        search_query = q.lower().strip()
        matches: list[SearchMatch] = []

        # Search in KNOWLEDGE_INDEX
        for category_id, category_data in KNOWLEDGE_INDEX.items():
            title = category_data.get("title", "").lower()
            description = category_data.get("description", "").lower()

            # Check if search term matches title or description
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

        # Search in available databases list
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
            pass

        # Sort by relevance score
        matches.sort(key=lambda m: m.relevance_score, reverse=True)

        return SearchResponse(
            query=q,
            results_count=len(matches),
            matches=matches[:50],  # Limit to top 50 results
            search_time_ms=0.0,
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error("Error searching knowledge: %s", e)
        raise HTTPException(
            status_code=500,
            detail="Failed to search knowledge databases",
        )
