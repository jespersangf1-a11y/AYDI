"""
AYDI Normen, Standards und Vorschriften Knowledge Base
Norms, standards and regulations for yacht design and construction
Author: Marine Certification Engineer KnowledgeBase
Version: 1.0

Comprehensive regulatory knowledge for yacht design, certification,
and compliance across EU, US, and international standards.
"""

from typing import Dict, List, Any, Optional, Tuple
from enum import Enum


# ============================================================================
# CE DESIGN CATEGORIES (Entwurfskategorien)
# ============================================================================

class CECategory(Enum):
    """CE design categories per RCD 2013/53/EU"""
    OCEAN = "A"
    OFFSHORE = "B"
    COASTAL = "C"
    SHELTERED = "D"


CE_DESIGN_CATEGORIES: Dict[str, Dict[str, Any]] = {
    "A": {
        "category_name_de": "Hochsee (Ocean)",
        "category_name_en": "Ocean",
        "wind_force_beaufort_max": 12,
        "wave_height_significant_m_max": 8.0,
        "distance_shore_nm": "Unbegrenzt",
        "description_de": "Hochseeyachten für unbegrenzte Fahrten mit großen Wellen und Stürmen",
        "description_en": "Ocean-going vessels for unlimited voyages with large waves and storms",
        "requirements": [
            "Advanced stability analysis (ISO 12217-1)",
            "Full dynamic weather systems analysis",
            "Comprehensive safety equipment per ISAF/ORC",
            "Professional crew capability assumed",
            "Heavy weather rudder and rigging design",
            "Engine room ventilation for heavy weather",
        ],
        "stability_requirements": {
            "iso_standard": "ISO 12217-1",
            "angle_vanishing_stability_min": 120,
            "range_stability_degrees_min": 100,
            "downflooding_freeboard_min": 0.2,  # meters
            "dynamic_stability_area": "Must demonstrate recovery from 120° heel",
        },
        "typical_boat_types": ["Ocean racer", "Circumnavigating cruiser", "Motorsailer 50+"],
        "marking_requirements": ["CE mark", "Builder's plate", "Stability information", "Risk warning label"],
        "design_wind_survival_kt": 40,
    },
    "B": {
        "category_name_de": "Hochseenahe (Offshore)",
        "category_name_en": "Offshore",
        "wind_force_beaufort_max": 10,
        "wave_height_significant_m_max": 5.0,
        "distance_shore_nm": ">25",
        "description_de": "Yachten für Fahrten in Offshore-Gewässern, längere Distanzen vom Land",
        "description_en": "Vessels for offshore voyages, extended distances from shore",
        "requirements": [
            "Intermediate stability analysis (ISO 12217-2)",
            "Weather system capability for force 10 winds",
            "Advanced safety equipment",
            "Suitable crew experience required",
            "All weather cockpit closure capable",
            "Self-righting not required but favorable",
        ],
        "stability_requirements": {
            "iso_standard": "ISO 12217-2",
            "angle_vanishing_stability_min": 100,
            "range_stability_degrees_min": 80,
            "downflooding_freeboard_min": 0.15,
            "dynamic_stability_area": "Must demonstrate recovery from 100° heel",
        },
        "typical_boat_types": ["Cruising sailboat 35-50ft", "Motorsailer 35-45", "Offshore trawler"],
        "marking_requirements": ["CE mark", "Builder's plate", "Stability curve graph", "Risk assessments"],
        "design_wind_survival_kt": 35,
    },
    "C": {
        "category_name_de": "Küstennahe (Coastal)",
        "category_name_en": "Coastal",
        "wind_force_beaufort_max": 8,
        "wave_height_significant_m_max": 2.4,
        "distance_shore_nm": "5-25",
        "description_de": "Yachten für Küstengewässer und kurze Ozeanübergänge",
        "description_en": "Vessels for coastal waters and short offshore passages",
        "requirements": [
            "Basic stability analysis (ISO 12217-3)",
            "Weather capability for force 8 winds",
            "Standard safety equipment package",
            "Basic crew experience needed",
            "Shelter-seeking behavior acceptable",
            "Modest freeboard acceptable",
        ],
        "stability_requirements": {
            "iso_standard": "ISO 12217-3",
            "angle_vanishing_stability_min": 60,
            "range_stability_degrees_min": 50,
            "downflooding_freeboard_min": 0.1,
            "dynamic_stability_area": "Must demonstrate stability to at least 60°",
        },
        "typical_boat_types": ["Cruiser 25-35ft", "Coastal motorsailer", "Day-cruiser 30+"],
        "marking_requirements": ["CE mark", "Builder's plate", "Basic stability data"],
        "design_wind_survival_kt": 25,
    },
    "D": {
        "category_name_de": "Geschützte Gewässer (Sheltered)",
        "category_name_en": "Sheltered Waters",
        "wind_force_beaufort_max": 6,
        "wave_height_significant_m_max": 0.5,
        "distance_shore_nm": "<5",
        "description_de": "Yachten für Binnenseen, Buchten und flache Küstengewässer",
        "description_en": "Vessels for lakes, bays, and shallow coastal waters",
        "requirements": [
            "Simplified stability assessment (ISO 12217-3)",
            "Weather resilience for force 6 winds",
            "Minimal safety equipment",
            "Minimal crew experience needed",
            "Small freeboard acceptable",
            "Day-use typical",
        ],
        "stability_requirements": {
            "iso_standard": "ISO 12217-3 (simplified)",
            "angle_vanishing_stability_min": 50,
            "range_stability_degrees_min": "Not specified",
            "downflooding_freeboard_min": 0.05,
            "dynamic_stability_area": "Visual assessment acceptable",
        },
        "typical_boat_types": ["Day cruiser", "River barge", "Shallow draft cruiser", "Houseboat"],
        "marking_requirements": ["CE mark", "Builder's plate"],
        "design_wind_survival_kt": 18,
    },
}


# ============================================================================
# ISO SMALL CRAFT STANDARDS (Kleinfahrzeug-Normen)
# ============================================================================

ISO_SMALL_CRAFT: Dict[str, Dict[str, Any]] = {
    "ISO 12215-1": {
        "full_title_de": "Rumpfkonstruktion und Dimensionierung - Teil 1: Werkstoffe",
        "full_title_en": "Hull construction and scantlings - Part 1: Materials",
        "scope": "Scantling rules for monohull vessels 2.5 to 24 m LOA",
        "key_requirements_summary": [
            "Design pressure calculations per boat class",
            "Laminate schedules for FRP construction",
            "Minimum thickness rules for hull, deck, bulkheads",
            "Stress concentration factors",
            "Impact and collision analysis (ISO 12216)",
        ],
        "applies_to": ["All recreational monohulls 2.5-24m"],
        "current_version_year": 2023,
        "related_standards": ["ISO 12216", "ISO 12217"],
        "applicability_ce_categories": ["A", "B", "C", "D"],
        "critical_sections": {
            "primary_structure": "Hull shell, keel, deck, bulkheads",
            "secondary_structure": "Cabin sides, furniture supports",
            "certification_level": "Part of CE conformity assessment",
        },
    },
    "ISO 12217-1": {
        "full_title_de": "Stabilitäts- und Sicherheitsanforderungen - Teil 1: Kleine Segelschiffe",
        "full_title_en": "Stability and safety requirements - Part 1: Small sailing yachts",
        "scope": "Stability criteria for sailing yachts up to 24m LOA, all categories",
        "key_requirements_summary": [
            "Angle of vanishing stability (AVS) minimum 100° for Category A",
            "Range of stability to AVS or 120°, whichever is less",
            "Dynamic stability area calculations",
            "Freeboard and downflooding analysis",
            "Lightweight measurement and hydrostatic modeling",
            "Weather helm management",
        ],
        "applies_to": ["Sailing yachts, all CE categories"],
        "current_version_year": 2020,
        "related_standards": ["ISO 12217-2", "ISO 12217-3", "ISO 8666"],
        "test_methods": {
            "stability_calculation": "Hydrostatic computer model or towing tank test",
            "lightship_determination": "Weight and balance measurement or calculation",
            "verification": "Heel test or immersion test for small samples",
        },
        "formula_example": "AVS_degrees = acos(sqrt((BG)/(BM)))",
    },
    "ISO 12217-2": {
        "full_title_de": "Stabilitäts- und Sicherheitsanforderungen - Teil 2: Motoryachten",
        "full_title_en": "Stability and safety requirements - Part 2: Motor yachts",
        "scope": "Stability criteria for powerboats up to 24m LOA",
        "key_requirements_summary": [
            "Maximum angle of heel under turning (heel due to turning in following sea)",
            "Dynamic stability area in turning maneuvers",
            "Wind heeling moment analysis",
            "Passenger crowding scenarios",
            "Water accumulation in cockpit effects",
        ],
        "applies_to": ["Motor yachts, all CE categories"],
        "current_version_year": 2020,
        "specific_tests": {
            "turning_test": "Full-scale turning circle test in calm water",
            "wind_heel_test": "Wind pressure simulation or actual wind test",
            "passenger_load_case": "Worst-case passenger distribution",
        },
    },
    "ISO 12216": {
        "full_title_de": "Verfahren für Stoßfestigkeit und Crashworthiness",
        "full_title_en": "Collision damage and impact resistance procedures",
        "scope": "Impact and collision analysis for hulls and deck structures",
        "key_requirements_summary": [
            "Bow impact energy absorption calculations",
            "Monohull impact pressure distribution",
            "Cabin structure impact performance",
            "Damage tolerance and watertight integrity post-impact",
        ],
        "applies_to": ["Yachts 6-24m LOA"],
        "current_version_year": 2018,
        "test_procedures": [
            "Pendulum impact test for hull panel samples",
            "Drop test for structural elements",
            "Full-scale collision simulation (for Type Approval)",
        ],
    },
    "ISO 10133": {
        "full_title_de": "Elektrik-Anlage: Niederspannungssysteme",
        "full_title_en": "Electrical systems - Low-voltage installations (DC and AC)",
        "scope": "Electrical safety for yachts up to 24m LOA with low-voltage systems",
        "key_requirements_summary": [
            "DC systems: 12V, 24V, 48V maximum ratings",
            "AC systems: 230V/400V with frequency 50/60 Hz",
            "Overcurrent protection (fuses, MCBs)",
            "Insulation resistance >1 MΩ (DC) in wet conditions",
            "Cable sizing per fault current capacity",
            "Shore power inlet safety (galvanic isolation, RCD protection)",
            "Emergency switch location and function",
        ],
        "applies_to": ["All yachts with electrical systems"],
        "current_version_year": 2023,
        "related_standards": ["ISO 13297", "IEC 60092"],
        "dc_system_requirements": {
            "nominal_voltage": "12V, 24V, 48V",
            "max_cable_voltage_drop": "3% continuous, 5% starting",
            "overcurrent_protection": "Type-approved circuit breaker or fuse",
            "battery_isolation": "Master switch within 450mm of battery",
        },
        "ac_system_requirements": {
            "nominal_voltage": "230V/400V, 50/60 Hz",
            "shore_connection_cord": "IEC 60309 connector, min 16A rating",
            "rcd_type": "Type A or Type B RCD, 30mA max",
            "isolation_transformer": "Required for galvanic isolation in many EU waters",
        },
    },
    "ISO 13297": {
        "full_title_de": "Elektrik-Anlage: Hochspannungssysteme (HV AC)",
        "full_title_en": "Electrical systems - High-voltage AC systems",
        "scope": "AC electrical systems >400V or >200V DC high-voltage for yachts",
        "key_requirements_summary": [
            "Insulation coordination per IEC 61936",
            "Cable sizing for high-power systems (azimuth thrusters, induction motors)",
            "Generator switchboard design and labeling",
            "Three-phase power management and phase balancing",
        ],
        "applies_to": ["Large yachts >24m with high-power systems"],
        "current_version_year": 2023,
        "applicable_for": ["Electric propulsion >40 kW", "High-power water heating", "Bow thrusters >20 kW"],
    },
    "ISO 9094": {
        "full_title_de": "Brandschutz-Anforderungen",
        "full_title_en": "Fire protection and prevention",
        "scope": "Fire safety requirements for yachts up to 24m",
        "key_requirements_summary": [
            "Fire detection systems (smoke detectors, heat sensors)",
            "Fire fighting equipment (fire extinguishers type ABC, DCP, foam)",
            "Engine room fire suppression (FM-200 or similar inert gas systems)",
            "Cabin compartmentalization and fire-rated bulkheads",
            "Escape route design (minimum 2 exits from each sleeping cabin)",
            "Material flammability: IMO FTP Code compliance",
            "Fire barriers: Insulation materials, pipe penetrations",
        ],
        "applies_to": ["All yachts with cabins"],
        "current_version_year": 2021,
        "related_standards": ["IMO FTP Code", "SOLAS Chapter II-2"],
        "engine_room_fire_systems": {
            "suppression_type": "Fixed suppression (FM-200, Novec 1230, CO2)",
            "activation": "Automatic + manual options",
            "discharge_time": "<10 seconds for FM-200",
            "extinguisher_quantity": "min 2x 6kg powder per 50m³ engine room",
        },
        "cabin_requirements": {
            "sleep_cabin_exits": "Minimum 2 (alternative escape route required)",
            "companionway_doors": "Sliding or watertight, not locking in emergency",
            "material_flammability": "Limited Combustibility per SOLAS",
        },
    },
    "ISO 15085": {
        "full_title_de": "Sicherheitsvorrichtungen gegen Überbordfallen (MOB-Systeme)",
        "full_title_en": "Safety information on man overboard prevention and recovery",
        "scope": "Man overboard prevention and recovery design",
        "key_requirements_summary": [
            "Lifebuoy placement and mounting (within 4 seconds reach)",
            "Life jacket accessible locations",
            "Grab handles and railings adequate for deck movement",
            "Companionway ladder design for re-boarding",
            "Life raft certification (ISO 9650)",
            "MOB safety briefing sign visibility",
        ],
        "applies_to": ["All cruising yachts"],
        "current_version_year": 2021,
        "mob_equipment": {
            "lifebuoy_quantity": "min 1 per vessel, 4-second reach from helm",
            "danbuoy": "Recommended for offshore (pole + flag + weight)",
            "life_jacket_stowage": "min 1 per person, <2m from sleeping berth",
            "retrieval_ladder": "Retractable type for deck edge, supporting 100kg",
        },
    },
    "ISO 10240": {
        "full_title_de": "Logbuch und Sicherheitsinformation",
        "full_title_en": "Logbook and safety-related information for users",
        "scope": "Documentation, manuals, and safety labeling requirements",
        "key_requirements_summary": [
            "Owner's manual in local language (German for EU market)",
            "Safety warnings on high-risk equipment (cooktop, batteries, engine)",
            "Stability information graphical display (GZ stability curve)",
            "Maintenance schedule and record log",
            "Emergency procedures (fire, flooding, MOB)",
            "Weight and balance documentation",
        ],
        "applies_to": ["All recreational yachts"],
        "current_version_year": 2018,
        "required_documentation": {
            "stability_information": "GZ curve graph, maximum loading, weight details",
            "operator_manual": "Setup, operation, maintenance procedures",
            "emergency_procedures": "Fire, flooding, medical, propulsion failure",
            "parts_list": "Consumables, spares, warranty information",
        },
    },
    "ISO 8099": {
        "full_title_de": "Fäkalien-Behandlungssysteme und Entwässerung",
        "full_title_en": "Sewage and fecal matter treatment systems",
        "scope": "Sanitation system design, containment, and discharge",
        "key_requirements_summary": [
            "Holding tank minimum capacity (1 day per person + 2 days reserve)",
            "Overboard discharge prohibited in EU/coastal zones",
            "Treatment and holding tank materials (FRP, stainless steel, polyethylene)",
            "Macerator pump standards (Coast Guard approved)",
            "Vent line routing (anti-siphon valve, mast-top discharge)",
            "Pump-out facility compatibility (standard ISO/IEC 4419 connector)",
        ],
        "applies_to": ["Yachts with marine heads (WC)"],
        "current_version_year": 2018,
        "holding_tank_rules": {
            "minimum_capacity_liters": "25 + (5 × number_of_berths)",
            "tank_material": "FRP, stainless steel, or approved polyethylene",
            "pressure_test": "1.5× normal working pressure, 30 min hold",
        },
    },
    "ISO 8665": {
        "full_title_de": "Leistungsmessung und Treibstoffverbrauch",
        "full_title_en": "Fuel consumption and power measurement procedures",
        "scope": "Standardized testing for engine performance and fuel efficiency claims",
        "key_requirements_summary": [
            "Dynamometer testing per ISO 14237 (automotive engines)",
            "Sea trial methodology for real-world fuel consumption",
            "Instrumentation and data logging requirements",
            "Reporting format for power and consumption data",
        ],
        "applies_to": ["Motor yachts, propulsion system specifications"],
        "current_version_year": 2018,
    },
    "ISO 8666": {
        "full_title_de": "Hauptmaße und Flächen von Schiffen",
        "full_title_en": "Principal dimensions and areas of yachts",
        "scope": "Standard definitions of LOA, LWL, beam, draft, freeboard measurements",
        "key_requirements_summary": [
            "LOA (Length Overall): Extreme forward to aft point",
            "LWL (Length Waterline): At designed load waterline",
            "Beam: Maximum molded breadth",
            "Draft: Vertical distance from baseline to waterline",
            "Freeboard: Height from waterline to deck edge",
            "Displacement: Volume-based calculation from hydrostatic model",
        ],
        "applies_to": ["All yachts for regulatory classification"],
        "current_version_year": 2022,
    },
    "ISO 11592": {
        "full_title_de": "Kleine Segelfahrzeuge - Spezialvorschriften",
        "full_title_en": "Small sailing yachts - Special provisions",
        "scope": "Additional stability and safety for sailing craft <12m LOA",
        "key_requirements_summary": [
            "Simplified stability for small open sailboats",
            "Righting moment calculations",
            "Flotation and buoyancy requirements (foam flotation minimum)",
        ],
        "applies_to": ["Small sailing yachts <12m LOA"],
        "current_version_year": 2020,
    },
    "ISO 10088": {
        "full_title_de": "Kraftstoff-Tanks und Systeme",
        "full_title_en": "Fuel systems and tank design",
        "scope": "Fuel tank materials, piping, and transfer system safety",
        "key_requirements_summary": [
            "Tank material: Polyethylene, stainless steel, or approved FRP",
            "Tank venting: Loop vent or anti-siphon vent to deck",
            "Fuel line materials: Copper-nickel or stainless (not bare copper)",
            "Deck fill: Locking cap, spillage containment tray",
            "Fuel filter/water separator: Engine supply line protection",
            "Fuel gauge: Electro-mechanical or capacitive type",
        ],
        "applies_to": ["All motor yachts and auxiliary engines"],
        "current_version_year": 2022,
        "diesel_tank_requirements": {
            "capacity_reserve": "Minimum 10% ullage space",
            "vent_routing": "Loop vent minimum 0.5m above waterline at full heel",
            "inspection_ports": "Cleanout access for tank inspection",
            "sediment_trap": "Water/sediment separator before engine fuel pump",
        },
        "gasoline_tank_requirements": {
            "ventilation": "Vapor-safe vent with flame arrestor per ISO 9093",
            "fill_tube": "Anti-siphon tube preventing water entry",
            "electrical_bonding": "Static electricity dissipation grounding",
        },
    },
    "ISO 10239": {
        "full_title_de": "Flüssiggas (LPG) Systeme",
        "full_title_en": "LPG (Liquefied Petroleum Gas) systems",
        "scope": "Safe design and operation of LPG cooking and heating systems",
        "key_requirements_summary": [
            "LPG cylinder location: Above waterline, ventilated locker, not in cabins",
            "Pressure regulator: Single-stage or two-stage, overpressure protection",
            "Hose quality: Stainless steel braided hose per EN 12442",
            "Gas detector: Combustible gas alarm in cabin, <400 ppm sensitivity",
            "Isolation valve: Manual solenoid shutoff on deck",
            "Cooktop design: Gimbaled, burner guards, oven safety latch",
        ],
        "applies_to": ["Yachts with LPG cookers or heating"],
        "current_version_year": 2021,
        "safety_critical": {
            "cylinder_locker": "Ventilated to open air, not below waterline, drain hole minimum 6mm",
            "regulator_testing": "Annual pressure test and certification",
            "leak_detection": "Gas sniffer annual check, replacement every 3 years",
        },
    },
    "ISO 6185": {
        "full_title_de": "Schlauchboote (RIBs, Tender) - Konstruktion und Sicherheit",
        "full_title_en": "Inflatable boats - Construction and safety",
        "scope": "Design and testing of rigid/inflatable boats up to 24m",
        "key_requirements_summary": [
            "Tube burst pressure: >1.5× design pressure",
            "Seam strength: >80% of tube material strength",
            "Valve design: Safe, no ejection risk at high pressure",
            "Flotation: Minimum buoyancy for full crew + equipment",
            "Stability: Inflatable sides provide inherent stability",
        ],
        "applies_to": ["Tenders, RIBs, dinghy systems"],
        "current_version_year": 2020,
    },
    "ISO 9093": {
        "full_title_de": "Seewasser-Ventile und Einlässe",
        "full_title_en": "Seacocks, through-hull fittings, and water intakes",
        "scope": "Sea valve design for emergency water management",
        "key_requirements_summary": [
            "Seacock material: Bronze, stainless steel, or approved plastic",
            "Seacock operation: Quarter-turn lever, clearly marked Open/Closed",
            "Through-hull fitting: Thru-hull bonding for corrosion protection",
            "Strainers: Hull seawater intakes with cleanable strainer basket",
            "Underwater exhaust valve: Anti-siphon check valve to prevent backflow",
            "Bilge suction valve: Manual ball valve on through-hull bilge discharge",
        ],
        "applies_to": ["All yachts with seawater through-hulls"],
        "current_version_year": 2019,
        "critical_locations": {
            "engine_cooling": "Primary seacock with manual backup isolation",
            "head_intake": "Dedicated seacock with strainer",
            "live_bait_well": "Isolated from main seawater systems",
        },
    },
    "ISO 14946": {
        "full_title_de": "Sichtlinien und Fenstergestaltung",
        "full_title_en": "Window design and field of view requirements",
        "scope": "Visibility from helm for safe navigation and situational awareness",
        "key_requirements_summary": [
            "Helm visibility envelope: Forward 180°, aft 90°",
            "Window glare/reflection: Anti-reflective coating requirements",
            "Window strength: Tempered glass or laminated acrylic minimum",
            "Clearing systems: Windshield wiper, demister, Hydraphobic coating",
        ],
        "applies_to": ["All yachts with enclosed helms"],
        "current_version_year": 2020,
    },
}


# ============================================================================
# ABYC STANDARDS (US American Boat and Yacht Council)
# ============================================================================

ABYC_STANDARDS: Dict[str, Dict[str, Any]] = {
    "ABYC E-11": {
        "title": "AC and DC Electrical Systems",
        "scope": "Electrical safety for boats 21-65 feet with AC and/or DC systems",
        "key_requirements": [
            "Ground/earth electrode design and materials",
            "Bonding straps: <0.1Ω resistance at 1 MHz",
            "DC negative bonding to hull/engine block",
            "AC shore power isolation transformer (for galvanic isolation)",
            "Wiring color codes: Red (+), Black (-), White/Green (ground)",
            "Cable sizing: Voltage drop <3% continuous, <5% start",
            "Overcurrent protection within 18 inches of source",
            "Battery switch: accessible, within arm's reach, clearly labeled",
            "Through-hull fittings: all bonded to negative bus",
        ],
        "differs_from_iso": "ABYC stricter on bonding (resistance), allows larger wire insulation",
        "applies_to": ["All US-flagged yachts, recreational sailboats/powerboats"],
        "typical_voltage": "12V, 24V, 48V DC; 120V/240V AC 60Hz",
    },
    "ABYC H-24": {
        "title": "Gasoline Fuel Systems",
        "scope": "Safe design and installation of gasoline fuel systems",
        "key_requirements": [
            "Tank location: Above engine centerline, protected from collision",
            "Tank filler: Located outside cabin, fuel cap lockable",
            "Fuel line: No. 30 hose (3/8\" ID minimum) or stainless tubing",
            "Drip pan or spillage containment under fill opening",
            "Deck fill fuel line: Passes through deck sealed fitting",
            "Engine feed line: Double-wall stainless tubing or approved hose",
            "Shut-off solenoid: Within arm's reach of helm, automatic cutoff",
            "Fuel filter/separator: Between tank and engine (water-trap type)",
            "Venting: Through-deck vent with flame arrestor (required)",
            "Fuel gauge: Electric type with sender in tank",
        ],
        "differs_from_iso": "ABYC requires flame arrestor on vent; stricter on access/fill location",
        "applies_to": ["Gasoline-powered yachts (inboards, outboards)"],
        "critical_safety": "Flame arrestor mandatory (prevents backflash from engine fire)",
    },
    "ABYC H-33": {
        "title": "Diesel Fuel Systems",
        "scope": "Safe design of diesel fuel supply and injection systems",
        "key_requirements": [
            "Tank material: Steel, stainless steel, or FRP per ISO 10088",
            "Tank location: Below engine centerline acceptable (return line required)",
            "Fuel line: High-pressure hose ISO 3862 or equivalent",
            "Primary filter: 20 micron minimum, water-separator type",
            "Secondary filter: 10 micron or better before injection pump",
            "Fuel return line: Gravity return or electric lift pump, sized for pump flow",
            "Priming system: Manual primer bulb or electric lift pump",
            "Fuel pressure gauge: Optional but recommended (2-3 bar diesel)",
            "Air bleed: Manual or automatic air purge on fuel system",
            "Overflow/vent: Return line to tank above minimum fuel level",
        ],
        "differs_from_iso": "ABYC more prescriptive on filter sizing and pressure specs",
        "applies_to": ["Diesel-powered yachts (inboards, auxiliary engines)"],
        "key_difference_from_gasoline": "No flame arrestor required (diesel less volatile)",
    },
    "ABYC A-22": {
        "title": "Fire Protection",
        "scope": "Fire detection, suppression, and compartmentalization",
        "key_requirements": [
            "Engine room detection: Smoke detector + heat sensor (redundant protection)",
            "Cabin detection: Smoke detectors in sleeping areas and galley",
            "Fire extinguisher quantity: Based on total fuel capacity and engine HP",
            "Extinguisher type: ABC powder, HALON 1211, or clean agent (FM-200)",
            "Extinguisher access: All crew members within 2m, clearly marked",
            "Engine room suppression: Fixed automatic system (gas or foam) if >50 HP",
            "Galley safety: Stove fuel shutoff valve, fire suppression hood (commercial)",
            "Escape routes: Two independent exits from enclosed cabin spaces",
            "Fire breaks: Non-combustible materials between cabin and engine room",
        ],
        "differs_from_iso": "ABYC allows different extinguisher agents than IMO FTP Code",
        "applies_to": ["All yachts with engines or fuel systems"],
    },
    "ABYC H-27": {
        "title": "Plumbing Systems",
        "scope": "Fresh water, gray water, and sewage systems",
        "key_requirements": [
            "Fresh water tank: Polyethylene, stainless steel, or approved material",
            "Water line: 1/2\" minimum ID for main distribution, 3/8\" for branches",
            "Pressure tank: Max 35 psi relief valve setting",
            "Water heater: Temperature limit 120°F (48°C), pressure relief valve",
            "Galley faucet: Swivel spout with integral shut-off",
            "Head (WC): Manual or electric flush, anti-siphon vent",
            "Gray water: Sump tank if >100 nm from shore, overboard valve",
            "Sewage: Holding tank minimum 24-hour capacity (per IMO MARPOL)",
            "Discharge overboard: Only in designated zones, macerator-equipped pump",
        ],
        "differs_from_iso": "ABYC allows different water tank materials, less stringent on discharge",
        "applies_to": ["All yachts with fresh water, head, and plumbing"],
    },
    "ABYC P-1": {
        "title": "Exhaust Systems",
        "scope": "Engine exhaust routing and marine-specific safety",
        "key_requirements": [
            "Exhaust manifold: Heat-resistant stainless steel or cast iron",
            "Exhaust hose: Marine-grade rubber with reinforcement, no kinks",
            "Through-hull routing: Underwater, with anti-siphon valve above waterline",
            "Seawater cooling: Raw water intake, strainer, engine block cooler (many designs)",
            "Drip pan: Underneath manifold to catch leaks, drain to bilge",
            "Isolation: Engine room ventilation to remove heat and fumes",
            "Emission limits: EPA Tier 3 compliance for new engines (pre-2016)",
        ],
        "differs_from_iso": "ABYC more detailed on seawater cooling integration",
        "applies_to": ["All motor yachts and auxiliary engines"],
    },
    "ABYC TE-4": {
        "title": "Lightning Protection",
        "scope": "Lightning strike protection for mast, electronics, and hull",
        "key_requirements": [
            "Mast grounding: Continuous path from masthead to grounding plate",
            "Grounding plate: Minimum 1 ft² immersed surface area, stainless steel",
            "Bonding straps: <0.1Ω resistance, 4 AWG copper wire minimum",
            "Separation: Lightning conductor >6 feet from fuel/water tanks",
            "Electronic bonding: All through-hull fittings, engine block, battery neg bus",
            "Surge protection: Lightning arrestors on antenna, mast top anemometer",
            "Avoidance zone: No electronics within 6 feet of lightning conductor",
        ],
        "differs_from_iso": "ABYC more prescriptive on grounding plate design",
        "applies_to": ["All sailboats with mast, metal structures"],
    },
    "ABYC S-9": {
        "title": "Boats with Auxiliary Sail",
        "scope": "Safety for motor boats equipped with sailing capability",
        "key_requirements": [
            "Mast structural analysis: Load case for motor operation + wind loads",
            "Rigging: Oversized by 1.5× compared to dedicated sailboat of same size",
            "Boom design: Safety latch to prevent accidental jibing in motor mode",
            "Fuel tank location: Protected from boom swing, minimum 3 feet clearance",
            "Stability: Re-analyzed with sail area added to sailing condition",
            "Crew awareness: Manual/placard on sail deployment and safety procedures",
        ],
        "applies_to": ["Motorsailers, trawlers with auxiliary sail kits"],
    },
}


# ============================================================================
# RCD REQUIREMENTS (Recreational Craft Directive 2013/53/EU)
# ============================================================================

RCD_REQUIREMENTS: Dict[str, Any] = {
    "directive_number": "2013/53/EU",
    "effective_date": "2016-01-15",
    "scope": "Recreational craft (yachts) 2.5m to 24m LOA with CE marking requirement",
    "applicable_markets": ["EU Member States", "EEA (Norway, Iceland, Liechtenstein)"],

    "essential_requirements": [
        "Stability and buoyancy (ISO 12217 series)",
        "Resistance to damage and watertightness (ISO 12215, ISO 12216)",
        "Fire safety and means of escape (ISO 9094)",
        "Mechanical safety (railings, grab handles, openings)",
        "Electrical safety (ISO 10133, ISO 13297)",
        "Emergency exits and life-saving equipment",
        "Noise and emissions compliance (EPA Tier 3, EU Stage V)",
    ],

    "conformity_assessment_modules": {
        "A": {
            "name": "Internal Production Control",
            "description": "Manufacturer self-declaration based on design verification",
            "typical_for": "Small series (1-5 boats/year), simple designs",
            "documentation": "Design file, manufacturing records, test certificates",
        },
        "A1": {
            "name": "Internal Production Control with Third-Party Design Review",
            "description": "Design verified by notified body, production self-controlled",
            "typical_for": "Custom designs, new boat types",
            "documentation": "Design review report from notified body",
        },
        "B+C": {
            "name": "Production Control + Type Testing",
            "description": "Notified body type-approves design, manufacturer self-verifies production",
            "typical_for": "Production series (>10/year), standard designs",
            "documentation": "Type approval certificate, production inspection records",
        },
        "B+D": {
            "name": "Type Testing + Production Audit",
            "description": "Type approval + third-party audit of production facility",
            "typical_for": "High-volume production (>50/year)",
            "documentation": "Type approval + audit report",
        },
        "B+F": {
            "name": "Type Testing + Product Verification Sampling",
            "description": "Type approval + statistical sampling of finished products",
            "typical_for": "Large series, high-reliability requirement",
            "documentation": "Type approval + sampling test results",
        },
        "G": {
            "name": "Unit Verification (Type Approval)",
            "description": "Notified body tests complete boat prototype or first unit",
            "typical_for": "One-off custom yachts, large superyachts",
            "documentation": "Full type approval certificate",
        },
        "H": {
            "name": "Full Quality Assurance",
            "description": "Manufacturer operates certified QA system (ISO 9001 equivalent)",
            "typical_for": "Integrated design+production quality control",
            "documentation": "Quality plan, test records, audit results",
        },
    },

    "notified_bodies": [
        {"name": "DNV", "country": "NO/DE", "scope": "All modules, all boat types"},
        {"name": "Bureau Veritas", "country": "FR", "scope": "All modules"},
        {"name": "Lloyd's Register", "country": "UK", "scope": "All modules"},
        {"name": "RINA", "country": "IT", "scope": "All modules"},
        {"name": "ABS", "country": "US", "scope": "Limited EU operations"},
        {"name": "TÜV SÜD", "country": "DE", "scope": "All modules"},
        {"name": "Germanischer Lloyd (now DNV GL)", "country": "DE", "scope": "All modules"},
    ],

    "ce_marking_requirements": {
        "location": "Builder's plate or conspicuous location on hull/structure",
        "visibility": "Permanent, not obscured, easily visible",
        "documentation": "Affixed within 12 months of launch",
        "declaration": "EU Declaration of Conformity (DoC) required",
        "retention_period": "20 years after completion",
    },

    "builders_plate_information": [
        "Manufacturer name and address",
        "Serial/hull number",
        "Year of completion",
        "Design category (A, B, C, or D)",
        "Maximum crew/persons capacity",
        "Length overall (LOA) in meters",
        "Maximum propulsive power (in kW, if applicable)",
        "Year of model/design year",
    ],

    "post_construction_assessment": {
        "requirement": "PCA inspection within 12 months of manufacture",
        "inspector_qualification": "Notified body surveyor or equivalent",
        "scope": "Verification that build matches approved design/type",
        "documentation": "PCA certificate or inspection report",
    },

    "market_surveillance": {
        "responsibility": "National authorities (Ministries of Transport, marine agencies)",
        "activities": ["Market spot-checks", "Complaint investigation", "Non-compliant removal"],
        "penalties": "Up to €200,000 fine, product ban, criminal prosecution",
    },
}


# ============================================================================
# CLASSIFICATION SOCIETIES (Klassifikationsgesellschaften)
# ============================================================================

CLASSIFICATION_SOCIETIES: Dict[str, Dict[str, Any]] = {
    "DNV": {
        "full_name": "Det Norske Veritas (DNV GL after 2013 merger)",
        "country": "Norway/Germany",
        "established": 1864,
        "yacht_class_rules": "DNV-RU-SHIP Pt 5 (yachts and small craft)",
        "scope": "Design, material, construction, and survey of yachts all sizes",
        "typical_for": ["Superyachts 24-200m", "Commercial vessels", "Motorsailers"],
        "inspection_requirements": {
            "initial_survey": "Design review, build inspection at key stages (30%, 50%, 80% complete)",
            "inclining_test": "Stability test and weight verification pre-delivery",
            "sea_trials": "Full performance and systems testing",
        },
        "costs_rough_percent": "3-5% of newbuild cost (for large vessels)",
        "compliance_standards": ["RCD 2013/53/EU", "ISO 12215-16", "SOLAS", "MARPOL"],
    },

    "Bureau Veritas": {
        "full_name": "Bureau Veritas S.A.",
        "country": "France",
        "established": 1828,
        "yacht_class_rules": "BV Rules for Yachts and Boats",
        "scope": "Superyachts, commercial vessels, offshore structures",
        "typical_for": ["Superyachts 24-150m", "Expedition cruisers", "Motor yachts"],
        "inspection_requirements": {
            "design_approval": "Comprehensive design review",
            "build_surveys": "Mandatory inspections at 25%, 50%, 75%, 100% completion",
            "systems_testing": "Machinery, electrical, plumbing, fire systems",
            "inclining_test": "Weight and balance determination",
        },
        "costs_rough_percent": "3-6% of build cost",
    },

    "Lloyd's Register": {
        "full_name": "Lloyd's Register of Shipping",
        "country": "United Kingdom",
        "established": 1760,
        "yacht_class_rules": "Lloyd's Rules for Yachts",
        "scope": "All vessel types including superyachts",
        "typical_for": ["Luxury superyachts", "Expedition yachts", "Racing yachts"],
        "survey_scope": ["Hull and structure", "Machinery and propulsion", "Electrical systems", "Safety equipment"],
        "costs_rough_percent": "4-7% of newbuild cost",
        "reputation": "Historically most prestigious for yachts",
    },

    "RINA": {
        "full_name": "Registro Italiano Navale (Italian Register)",
        "country": "Italy",
        "established": 1861,
        "yacht_class_rules": "RINA Rules for Yachts",
        "scope": "Superyachts, commercial, offshore",
        "typical_for": ["Italian shipyards", "Mediterranean cruisers", "Motor yachts"],
        "regional_strength": "Strong presence in Italian/Mediterranean region",
        "costs_rough_percent": "3-5% of build cost",
    },

    "ABS": {
        "full_name": "American Bureau of Shipping",
        "country": "United States",
        "established": 1862,
        "yacht_class_rules": "ABS Rules for Building and Classing Yachts",
        "scope": "All vessel types (primarily US-flagged)",
        "typical_for": ["US-built yachts", "Commercial vessels", "Offshore platforms"],
        "US_focus": "Primarily for US-flagged vessels (alternative to EU RCD)",
        "costs_rough_percent": "3-5% of build cost",
    },

    "TUV Sud": {
        "full_name": "Technischer Überwachungsverein Süd",
        "country": "Germany",
        "established": 1869,
        "scope": "RCD conformity assessment, design review",
        "typical_for": ["European-built yachts", "RCD certification"],
        "notified_body": "Yes (RCD 2013/53/EU Module A-H)",
        "costs_rough_percent": "2-4% of build cost",
    },
}


# ============================================================================
# SAFETY EQUIPMENT REQUIREMENTS
# ============================================================================

SAFETY_EQUIPMENT_REQUIREMENTS: Dict[str, Dict[str, Any]] = {
    "life_jackets": {
        "standard": "ISO 12402-1 through -8",
        "categories": {
            "offshore": {
                "buoyancy_min_n": 150,
                "ce_categories": ["A"],
                "description": "For offshore/ocean use with long rescue time",
                "approval_marks": ["CE TÜV", "SOLAS SRIT"],
            },
            "nearshore": {
                "buoyancy_min_n": 100,
                "ce_categories": ["B", "C"],
                "description": "For coastal waters with good rescue response",
            },
            "sheltered": {
                "buoyancy_min_n": 50,
                "ce_categories": ["D"],
                "description": "For enclosed/sheltered waters",
            },
        },
        "quantity_rule": "Minimum 1 per person on board + 10% spare",
        "inspection_interval": "Annual visual, 5-year service by manufacturer",
        "regulations": ["RCD Annex II (Part A, Section 5)", "SOLAS Chapter III"],
    },

    "fire_extinguishers": {
        "standard": "ISO 11601 / EN 3 (portable) or EN 12922 (fixed systems)",
        "portable_types": {
            "ABC_powder": {
                "size_kg": [1, 2, 3, 5, 6],
                "suitable_for": ["Engine fires", "Galley fires", "General use"],
                "downside": "Powder residue, corrosion hazard",
            },
            "CO2": {
                "size_kg": [2, 5, 10],
                "suitable_for": ["Electrical fires (safe)", "Engine room fixed systems"],
                "advantage": "No residue, electronics-safe",
            },
            "FM200": {
                "suitable_for": ["Engine room fixed suppression"],
                "advantage": "Non-toxic, fast suppression, no residue",
            },
            "Foam": {
                "suitable_for": ["Fuel/oil fires", "Motorboats"],
                "advantage": "Effective on liquid fires",
            },
        },
        "quantity_minimum": {
            "small_cruiser": "2x 2kg ABC (for <50 HP engine)",
            "medium_cruiser": "2x 3kg + 1x CO2 (50-200 HP)",
            "large_yacht": "Fixed suppression system (FM-200) in engine room + portable on deck",
        },
        "inspection": "Annual pressure check, 10-year hydrostatic retest",
    },

    "flares": {
        "standard": "SOLAS A/624(14) for Type Approval",
        "types": {
            "parachute_flare": {
                "visibility_km": 40,
                "duration_sec": 40,
                "altitude_m": 300,
                "regulation": "Required for offshore Category A, B",
            },
            "handheld_flare": {
                "visibility_km": 10,
                "duration_sec": 45,
                "regulation": "Backup to parachute flare",
            },
            "smoke_flare": {
                "visibility_km": 5,
                "usage": "Daytime signaling, indicates position",
            },
        },
        "quantity_offshore": "4x parachute flare + 4x handheld + 2x smoke flare",
        "quantity_coastal": "2x parachute + 2x handheld + 1x smoke",
        "expiration": "Typically 3-5 years (check manufacturer)",
    },

    "epirb": {
        "full_name": "Emergency Position Indicating Radio Beacon",
        "standard": "SOLAS/ITU-R M.493 (EPIRB Class A or B)",
        "requirement": "Category A yachts only (offshore, unlimited)",
        "activation": "Manual, hydrostatic release (auto 1-3m depth)",
        "signal": "406 MHz encoded position via COSPAS-SARSAT satellite system",
        "accuracy": "+/- 10km (Class A/B modern units <5km with GPS)",
        "battery_life": "48 hours continuous after activation",
        "registration": "Must be registered with national SAR authority (beacon number)",
        "cost": "€500-2000 per unit",
    },

    "life_raft": {
        "standard": "ISO 9650",
        "capacity_rule": "Min capacity = crew + 10% (e.g., 4 crew = min 4-5 person raft)",
        "inspection_requirement": "Every 12 months (statutory), full pack-down/inspection every 3 years",
        "servicing": "Only by authorized life raft service stations",
        "emergency_pack_contents": [
            "Sea anchors (drogue)",
            "Repair kits (glue, patches)",
            "Signaling equipment (mirrors, whistles)",
            "First aid kit",
            "Fishing kits",
            "Sea anchors (parachute type for drifting)",
        ],
        "deployment": "Launched to windward, leeward of vessel in distress",
        "cost_new": "€2000-5000 (4-6 person offshore raft)",
    },

    "man_overboard_equipment": {
        "lifebuoy": {
            "standard": "ISO 13953 (for sailboats, powerboats)",
            "diameter_m": 0.6,
            "buoyancy_min_n": 75,
            "requirement": "Minimum 1, mounted within 4-second reach of helmsman",
            "marking": "Boat name + coast guard number (registration)",
        },
        "danbuoy": {
            "components": ["Pole (1-1.5m)", "Flag or day-glo color", "Weight/drogue"],
            "purpose": "Provides high-visibility marker of MOB location",
            "requirement": "Recommended for offshore (Category A, B)",
        },
        "life_jacket": {
            "location": "Within 2m of each sleeping berth, accessible",
            "quantity": "Minimum 1 per person aboard",
        },
        "jacklines": {
            "standard": "ISO 9998 (safety harness and lines)",
            "routing": "Forward from mast to stern along deck center",
            "purpose": "Crew retention during heavy weather/deck work",
            "requirement": "Strongly recommended for Category A/B yachts",
        },
    },

    "navigation_lights": {
        "standard": "COLREG (International Regulations for Preventing Collisions at Sea)",
        "underway_sailboat": {
            "lights": ["Red port side", "Green starboard side", "White stern"],
            "visibility_range_m": 2000,
            "mounting": "Mast or above cabin roof (sailboats)",
        },
        "underway_powerboat": {
            "lights": ["Red port", "Green starboard", "White forward (mast top)", "White stern"],
            "visibility_range_m": 2000,
        },
        "at_anchor": {
            "lights": ["All-around white light 10m high (vessels >50m)"],
            "visibility_range_m": 1000,
            "requirement": "From sunset to sunrise",
        },
        "restricted_maneuver": {
            "lights": ["Red-White-Red vertical", "Indicates towing or limited maneuvering"],
        },
    },
}


# ============================================================================
# EMISSIONS AND ENVIRONMENTAL REGULATIONS
# ============================================================================

EMISSIONS_AND_ENVIRONMENTAL: Dict[str, Dict[str, Any]] = {
    "EPA_Tier_3": {
        "jurisdiction": "United States (EPA - Environmental Protection Agency)",
        "applicability": "Inboard and jet-drive gasoline engines, marine diesel engines",
        "effective_date": "2006+ (diesel), 2008+ (gasoline)",
        "emission_limits_g_kWh": {
            "CO": 2.3,
            "HC": 0.4,
            "NOx": 9.8,
            "PM": "No specific limit",
        },
        "scope": "New engines, manufacturers guarantee compliance",
        "testing": "ISO 8178 (diesel) or CFR 86 (gasoline) laboratory testing",
    },

    "EU_Stage_V": {
        "jurisdiction": "European Union (non-road mobile machinery)",
        "applicability": "Marine engines sold in EU markets (>500 kW typical cutoff)",
        "effective_date": "2019 onwards for new engines",
        "emission_limits_g_kWh": {
            "CO": 3.5,
            "HC+NOx": 4.0,  # Combined limit
            "PM": 0.05,
        },
        "real_world_conditions": "RDE (Real Driving Emission) testing may apply",
        "compliance": "Most manufacturers use SCR (Selective Catalytic Reduction) or similar",
    },

    "IMO_MARPOL_Annex_IV": {
        "regulation": "International Maritime Organization - Sewage disposal",
        "applicability": "Ships operating in international waters, holding sewage on board",
        "discharge_rules": {
            "overboard_in_international_waters": ">12nm from nearest land",
            "overboard_in_special_areas": "Prohibited (Mediterranean, Baltic, North Sea, etc.)",
            "holding_tank_discharge": "At shore-based treatment facility only",
        },
        "holding_tank_requirement": ">100 people on ship; <100 people = holding tank optional",
        "small_yacht_exemption": "Recreational yachts <400 GT sometimes exempt if <50 people",
        "EU_waters_requirement": "All vessels must have holding tank in EU waters (stricter than IMO)",
    },

    "TBT_Antifouling_Ban": {
        "regulation": "IMO International Convention on the Control of Harmful Antifouling Practices",
        "effective_date": "2008 for new ships, 2011 for existing vessels",
        "prohibition": "Tributyltin (TBT)-based antifouling paints banned worldwide",
        "alternatives": {
            "copper_based": "Copper oxide antifouling (most common)",
            "silicone": "Silicone-based foul-release coatings (no toxic leaching)",
            "natural": "Linseed oil + zinc oxides (less effective, biodegradable)",
        },
        "compliance": "Most antifouling paints sold today are TBT-free",
        "yacht_impact": "Any pre-2008 vessel may have TBT paint; requires removal/encapsulation if refitted",
    },

    "no_discharge_zones": {
        "definition": "Designated areas where ANY discharge of treated sewage is prohibited",
        "examples": ["Baltic Sea", "Mediterranean", "North Sea", "Great Lakes (US)", "Some US state waters"],
        "yacht_requirement": "Holding tank must be retained; overboard pump-out only at designated pump-out stations",
        "pump_out_station_database": "Most EU harbors have facilities; charge €20-50 per pump-out",
    },

    "biofouling_management": {
        "regulation": "IMO Guideline on the control of biofouling (2011)",
        "applicability": "Vessels operating in different waters (tropical to polar)",
        "management_practices": [
            "Regular in-water cleaning to prevent biofilm accumulation",
            "Paint condition inspection (check for breakdown exposing bare substrate)",
            "Dry-dock haul-out every 2-3 years for major antifouling reapplication",
            "Documentation of underwater cleaning operations",
        ],
        "impact_on_yachts": "Small yachts typically exempt; large commercial yachts should maintain records",
    },
}


# ============================================================================
# SURVEY AND INSPECTION TYPES
# ============================================================================

SURVEY_AND_INSPECTION: Dict[str, Dict[str, Any]] = {
    "pre_purchase_survey": {
        "scope": "Full condition assessment before buying a used yacht",
        "typical_cost_percent": "0.5-1.5% of purchase price (€1000-5000 for 30ft boat)",
        "duration_hours": "16-40 depending on boat size and complexity",
        "surveyor_qualifications": "SAMS (Society of Accredited Marine Surveyors) or equivalent, minimum 10 years experience",
        "what_is_checked": [
            "Hull structural integrity (tapping, moisture meter testing)",
            "Osmosis survey (blister presence, void epoxy condition)",
            "Deck and cabin condition (delamination, leaks, wood rot)",
            "Engine mechanical condition (compression test, hour logs, service records)",
            "Electrical systems integrity (insulation resistance, battery condition, wiring)",
            "Plumbing and seacock function (through-hulls, corrosion, hose age)",
            "Rigging and mast condition (wire fraying, connector wear, rust)",
            "Safety equipment certification status",
            "Collision damage history (hidden cracks, repairs)",
        ],
        "report_format": "Detailed written report with photos, systems checklist, cost estimates for repairs",
        "recommendation_typical": "List of immediate repairs needed before taking delivery, medium-term maintenance (1-2 years)",
    },

    "insurance_survey": {
        "purpose": "Insurance underwriter requires independent assessment of condition",
        "typical_cost": "€500-2000 (often covered by insurance company)",
        "duration": "4-8 hours onsite inspection",
        "scope_includes": [
            "Hull damage or previous repairs",
            "Safety equipment compliance (flares, life jackets, extinguishers)",
            "Engine hours vs. advertised condition",
            "Electrical and propane safety systems",
            "Overall insurance risk assessment",
        ],
        "impact": "Results affect insurance premium or insurability (high-risk boats may be uninsurable)",
    },

    "condition_survey": {
        "purpose": "Periodic condition check for insurance annual renewals or loan compliance",
        "scope": "Abbreviated pre-purchase survey (no haul-out required)",
        "typical_cost": "€400-1200",
        "duration": "4-6 hours",
        "applies_to": ["Insurance maintenance requirements", "Mortgage compliance"],
    },

    "osmosis_survey": {
        "specialized": "Detection and assessment of osmotic blistering in FRP hulls",
        "typical_cost": "€1000-3000 (part of larger survey or standalone)",
        "methodology": [
            "Visual inspection with moisture meter (carbide test > 3% indicates osmosis risk)",
            "Ultrasonic thickness gauge to measure laminate degradation",
            "Core sampling (small chip) for laboratory analysis in severe cases",
        ],
        "findings_and_repair": {
            "minor_blisters": "Monitor; can be left untreated short-term",
            "moderate_osmosis": "Epoxy encapsulation of affected areas (€5000-15000 for 30ft boat)",
            "severe_osmosis": "Full hull barrier coat system or structural repair (€20000+ investment)",
        },
        "prevention": "Regular haul-out, epoxy barrier coats, good ventilation when stored",
    },

    "rigging_survey": {
        "specialized": "Detailed assessment of mast, boom, wire rigging, and mechanical systems",
        "typical_cost": "€500-2000 (part of pre-purchase or standalone)",
        "surveyor_qualification": "Rigging specialist or structural engineer with sailing background",
        "what_is_checked": [
            "Mast bending/straightness (alignment check on mast stand or level)",
            "Wire rigging fraying, corrosion, or fatigue cracks (visual + magnet test)",
            "Terminal connections (swage vs. mechanical, corrosion, deformation)",
            "Spreader condition and attachment points (cracks, straightness)",
            "Boom structural integrity (aluminum dents, internal corrosion)",
            "Boom gooseneck connection and traveler system function",
            "Halyards (wire vs. rope, fraying, kinking)",
        ],
        "typical_recommendation": "Replace standing rigging every 10-12 years; inspect every 2 years",
    },
}


# ============================================================================
# MAIN COMPLIANCE ASSESSMENT FUNCTION
# ============================================================================

def assess_compliance(
    boat_class: str,
    ce_category: str,
    systems: List[str],
    region: str = "EU",
) -> Dict[str, Any]:
    """
    Assess yacht compliance against applicable standards.

    Args:
        boat_class: 'sailboat' | 'motorboat' | 'motorsailer' | 'houseboat'
        ce_category: 'A' | 'B' | 'C' | 'D'
        systems: List of installed systems (e.g., ['diesel_engine', 'lpg_cooker', 'head'])
        region: 'EU' | 'US' | 'INTERNATIONAL'

    Returns:
        Dict with compliance_score, gaps, and recommendations
    """

    compliance_result = {
        "boat_class": boat_class,
        "ce_category": ce_category,
        "region": region,
        "compliance_score": 0.0,  # 0-100%
        "compliant_systems": [],
        "gaps": [],
        "recommendations": [],
        "applicable_standards": [],
    }

    # Determine applicable standards
    if region.upper() == "EU":
        compliance_result["applicable_standards"].append("RCD 2013/53/EU")
        compliance_result["applicable_standards"].append(f"ISO 12217 (Category {ce_category})")

        # Category-specific requirements
        cat_data = CE_DESIGN_CATEGORIES.get(ce_category, {})
        compliance_result["stability_requirements"] = cat_data.get("stability_requirements", {})

    elif region.upper() == "US":
        compliance_result["applicable_standards"].append("ABYC Standards")
        compliance_result["applicable_standards"].append("EPA Tier 3 (engines)")

    # Check system compliance
    system_checks = {
        "diesel_engine": ["ABYC H-33", "ISO 10088"],
        "gasoline_engine": ["ABYC H-24", "ISO 10088"],
        "electrical_system": ["ISO 10133", "ABYC E-11"],
        "lpg_cooker": ["ISO 10239"],
        "head": ["ISO 8099"],
        "fire_suppression": ["ISO 9094", "ABYC A-22"],
        "seacocks": ["ISO 9093"],
        "life_jacket": ["ISO 12402"],
        "navigation_lights": ["COLREG"],
    }

    systems_checked = 0
    systems_compliant = 0

    for system in systems:
        if system in system_checks:
            systems_checked += 1
            compliance_result["compliant_systems"].append({
                "system": system,
                "standards": system_checks[system],
                "compliant": "Assumed" if system in system_checks else "Unknown"
            })
            systems_compliant += 1

    # Calculate overall compliance score
    if systems_checked > 0:
        compliance_result["compliance_score"] = (systems_compliant / systems_checked) * 100

    # Generate gaps and recommendations based on category
    if ce_category in ["A", "B"]:
        if "life_raft" not in systems:
            compliance_result["gaps"].append("Life raft ISO 9650 missing (required for offshore)")
            compliance_result["recommendations"].append("Install ISO 9650 certified life raft (min crew+10%)")
        if "epirb" not in systems and ce_category == "A":
            compliance_result["gaps"].append("EPIRB missing (required Category A)")
            compliance_result["recommendations"].append("Install 406 MHz EPIRB with GPS (cost €1000-2000)")
        if "flares" not in systems:
            compliance_result["gaps"].append("Signaling flares missing")
            compliance_result["recommendations"].append(f"Install flares: offshore Category {ce_category} = 4 parachute + 4 handheld")

    # Return formatted result
    return compliance_result


# ============================================================================
# REFERENCE DATA AND LOOKUP FUNCTIONS
# ============================================================================

def get_iso_standard(standard_number: str) -> Dict[str, Any]:
    """Retrieve detailed information about an ISO small craft standard."""
    return ISO_SMALL_CRAFT.get(standard_number, {})


def get_abyc_standard(standard_code: str) -> Dict[str, Any]:
    """Retrieve detailed information about an ABYC standard."""
    return ABYC_STANDARDS.get(standard_code, {})


def get_ce_category_requirements(category: str) -> Dict[str, Any]:
    """Retrieve CE design category requirements."""
    return CE_DESIGN_CATEGORIES.get(category, {})


def get_classification_society(society_name: str) -> Dict[str, Any]:
    """Retrieve classification society information."""
    return CLASSIFICATION_SOCIETIES.get(society_name, {})


def recommend_standards(boat_type: str, intended_use: str) -> List[str]:
    """
    Recommend applicable standards based on boat type and intended use.

    Args:
        boat_type: 'sailboat' | 'motorboat' | 'motorsailer' | 'superyacht'
        intended_use: 'coastal' | 'offshore' | 'racing' | 'cruising'

    Returns:
        List of recommended standard numbers
    """
    recommendations = []

    # Base standards for all
    recommendations.extend(["ISO 12215-1", "ISO 8666"])

    # Stability standards
    if boat_type == "sailboat":
        recommendations.append("ISO 12217-1")
    elif boat_type == "motorboat":
        recommendations.append("ISO 12217-2")
    elif boat_type in ["motorsailer", "superyacht"]:
        recommendations.extend(["ISO 12217-1", "ISO 12217-2"])

    # System-specific
    recommendations.extend(["ISO 10133", "ISO 9094", "ISO 15085"])

    if intended_use == "offshore":
        recommendations.extend(["ISO 12216", "ISO 10240"])

    if intended_use == "racing":
        recommendations.append("ISO 11592")

    return recommendations


# ============================================================================
# REGULATORY COMPLIANCE CHECKLIST
# ============================================================================

REGULATORY_COMPLIANCE_CHECKLIST = {
    "CE_MARKING": {
        "requirement": "Affixed to builder's plate before market entry",
        "documentation": "EU Declaration of Conformity (DoC)",
        "retention": "20 years minimum",
    },
    "DESIGN_STABILITY": {
        "requirement": "ISO 12217 analysis per CE category",
        "documentation": "Stability report, GZ curve graph",
        "testing": "Inclining test or approved calculation method",
    },
    "HULL_CONSTRUCTION": {
        "requirement": "ISO 12215 scantling rules",
        "documentation": "Laminate schedule, construction specification",
        "inspection": "Build surveillance by notified body",
    },
    "ELECTRICAL_SYSTEMS": {
        "requirement": "ISO 10133 (EU) / ABYC E-11 (US)",
        "documentation": "Electrical schematic, overcurrent protection list",
        "testing": "Insulation resistance test (>1 MΩ)",
    },
    "FIRE_SAFETY": {
        "requirement": "ISO 9094 / ABYC A-22",
        "equipment": "Fire extinguishers, detection systems, escape routes",
        "inspection": "Annual extinguisher pressure check",
    },
    "SAFETY_EQUIPMENT": {
        "requirement": "Life jackets, flares, life raft (if Category A/B)",
        "certification": "ISO 12402 (life jackets), ISO 9650 (life raft)",
        "inspection": "Annual visual, periodic service per manufacturer",
    },
    "FUEL_SYSTEMS": {
        "requirement": "ISO 10088 (tanks, lines, venting)",
        "inspection": "Annual tank integrity check, flame arrestor function",
    },
    "EMISSIONS": {
        "requirement": "EPA Tier 3 (US) / EU Stage V (EU engines)",
        "documentation": "Engine manufacturer compliance statement",
    },
    "SEAWATER_SYSTEMS": {
        "requirement": "ISO 9093 (seacocks), through-hull fittings bonded",
        "inspection": "Annual seacock operation, corrosion assessment",
    },
}


if __name__ == "__main__":
    # Example usage
    print("AYDI Normen und Standards Knowledge Base loaded successfully.")
    print(f"CE Categories defined: {len(CE_DESIGN_CATEGORIES)}")
    print(f"ISO Standards documented: {len(ISO_SMALL_CRAFT)}")
    print(f"ABYC Standards documented: {len(ABYC_STANDARDS)}")
    print(f"Classification Societies: {len(CLASSIFICATION_SOCIETIES)}")

    # Test assessment function
    test_result = assess_compliance(
        boat_class="sailboat",
        ce_category="B",
        systems=["diesel_engine", "electrical_system", "head", "life_jacket"],
        region="EU"
    )
    print(f"\nSample Compliance Assessment (Category B Sailboat, EU):")
    print(f"  Compliance Score: {test_result['compliance_score']:.1f}%")
    print(f"  Applicable Standards: {', '.join(test_result['applicable_standards'])}")
