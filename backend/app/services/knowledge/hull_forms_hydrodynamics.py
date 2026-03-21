"""
AYDI Rumpfformen und Hydrodynamik Knowledge Base
Hull forms, keels, rudders and hydrodynamic concepts for yacht design analysis
Author: Naval Architecture KnowledgeBase
Version: 1.0
"""

from typing import Dict, List, Any, Tuple
from dataclasses import dataclass
import math


@dataclass
class HullType:
    """Hull form classification with hydrodynamic characteristics"""
    name_de: str
    name_en: str
    speed_range_knots: Tuple[float, float]
    froude_number_range: Tuple[float, float]
    displacement_to_length_ratio: Tuple[float, float]
    prismatic_coefficient_range: Tuple[float, float]
    stability_characteristics: str
    typical_boat_class: str
    sea_state_capability: str
    advantages: List[str]
    disadvantages: List[str]


@dataclass
class KeelType:
    """Keel configuration with performance characteristics"""
    name_de: str
    name_en: str
    draft_range_m: Tuple[float, float]
    ballast_ratio_range: Tuple[float, float]
    righting_moment_characteristics: str
    windward_performance: str
    structural_requirements: str
    grounding_behavior: str
    typical_boat_class: str
    maintenance_level: str
    failure_modes: List[str]


@dataclass
class RudderType:
    """Rudder design with control and structural properties"""
    name_de: str
    name_en: str
    efficiency_rating: str
    control_authority: str
    structural_vulnerability: str
    bearing_types: List[str]
    typical_boat_class: str
    failure_modes: List[str]


HULL_TYPES: Dict[str, HullType] = {
    "displacement": HullType(
        name_de="Verdränger (Langkiel)",
        name_en="Displacement (Full-Keel)",
        speed_range_knots=(6.0, 12.0),
        froude_number_range=(0.15, 0.35),
        displacement_to_length_ratio=(150.0, 350.0),
        prismatic_coefficient_range=(0.55, 0.62),
        stability_characteristics="High stability, stiff, low heel angles, high righting moment",
        typical_boat_class="Cruising sailboats, full-keel offshore, traditional designs",
        sea_state_capability="Excellent in rough seas, slow rolling, comfortable motion",
        advantages=[
            "Excellent rough-water performance",
            "High initial and ultimate stability",
            "Good load-carrying capacity",
            "Predictable, forgiving behavior",
            "Low dynamic loads",
            "Excellent seaworthiness"
        ],
        disadvantages=[
            "Lower speed potential",
            "Higher wetted surface drag",
            "Poor windward performance in light air",
            "Higher running costs",
            "Larger turning radius"
        ]
    ),
    "semi_displacement": HullType(
        name_de="Semi-Verdränger",
        name_en="Semi-Displacement Hull",
        speed_range_knots=(10.0, 20.0),
        froude_number_range=(0.35, 0.50),
        displacement_to_length_ratio=(100.0, 200.0),
        prismatic_coefficient_range=(0.58, 0.68),
        stability_characteristics="Moderate stability, dynamic heel, moderate righting moment",
        typical_boat_class="Fast cruisers, motorsailers, performance yachts",
        sea_state_capability="Good in moderate seas, can be lively in rough water",
        advantages=[
            "Better speed than displacement",
            "Efficient power plant utilization",
            "Practical load capacity",
            "Compromise between comfort and speed",
            "Good fuel efficiency"
        ],
        disadvantages=[
            "Trim sensitive",
            "Wave-making resistance increases significantly",
            "Moderate heel in sailing",
            "Can be wet in rough seas"
        ]
    ),
    "planing": HullType(
        name_de="Gleitfähiger Rumpf (Gleiter)",
        name_en="Planing Hull",
        speed_range_knots=(15.0, 40.0),
        froude_number_range=(0.50, 2.50),
        displacement_to_length_ratio=(40.0, 120.0),
        prismatic_coefficient_range=(0.50, 0.60),
        stability_characteristics="Dynamic stability, high heel angles, transverse instability in light air",
        typical_boat_class="Performance yachts, speedboats, high-speed cruisers",
        sea_state_capability="Moderate to good at speed, rough when slow",
        advantages=[
            "High speed capability",
            "Minimal wave-making resistance at speed",
            "Shallow draft options available",
            "Good acceleration and maneuverability",
            "Excellent light-air performance potential"
        ],
        disadvantages=[
            "Sensitive to trim and load distribution",
            "Poor slow-speed efficiency",
            "High lateral forces when sailing",
            "Requires strong build for high speeds",
            "Uncomfortable in seaway at slow speeds"
        ]
    ),
    "swath": HullType(
        name_de="SWATH (Small Waterplane Area Twin Hull)",
        name_en="SWATH (Small Waterplane Area Twin Hull)",
        speed_range_knots=(12.0, 25.0),
        froude_number_range=(0.25, 0.50),
        displacement_to_length_ratio=(180.0, 400.0),
        prismatic_coefficient_range=(0.70, 0.85),
        stability_characteristics="Exceptional stability, minimal heel, large righting moment",
        typical_boat_class="Expedition vessels, research ships, comfort-focused yachts",
        sea_state_capability="Outstanding in rough seas, minimal motion",
        advantages=[
            "Exceptional seaworthiness and motion",
            "Very large internal volume",
            "Minimal heeling in strong wind",
            "Excellent wave-piercing capability",
            "Very stable in all conditions"
        ],
        disadvantages=[
            "Complex structure and construction",
            "High drag at displacement speeds",
            "Difficulty with shallow water",
            "Expensive to build and maintain",
            "Symmetrical performance only"
        ]
    ),
    "catamaran": HullType(
        name_de="Katamaran",
        name_en="Catamaran",
        speed_range_knots=(10.0, 30.0),
        froude_number_range=(0.30, 0.70),
        displacement_to_length_ratio=(80.0, 250.0),
        prismatic_coefficient_range=(0.60, 0.72),
        stability_characteristics="Excellent transverse stability, minimal heel, stiff platform",
        typical_boat_class="Cruising cats, fast ferries, motorsailers, performance racing",
        sea_state_capability="Good in most conditions, some pitching in head seas",
        advantages=[
            "Large deck and cabin space for displacement",
            "Excellent stability and motion control",
            "Shallow draft available",
            "Good speed efficiency",
            "Excellent living space"
        ],
        disadvantages=[
            "Complex structure",
            "Increased windage",
            "Poor pointing ability under sail",
            "Reduced maneuverability",
            "Higher construction and maintenance cost"
        ]
    ),
    "trimaran": HullType(
        name_de="Trimaran",
        name_en="Trimaran",
        speed_range_knots=(12.0, 35.0),
        froude_number_range=(0.35, 0.80),
        displacement_to_length_ratio=(60.0, 180.0),
        prismatic_coefficient_range=(0.58, 0.68),
        stability_characteristics="Good stability from outrigger floats, heel limited by float immersion",
        typical_boat_class="Performance cruisers, offshore racers, fast expedition vessels",
        sea_state_capability="Good to excellent, floats provide motion damping",
        advantages=[
            "High-speed potential with reasonable load",
            "Good stability from floats",
            "Lighter than equivalent catamaran",
            "Better pointing than catamaran",
            "Excellent rough-water performance"
        ],
        disadvantages=[
            "Float immersion limits heel range",
            "Complex structure",
            "Potential capsize risk if improperly designed",
            "Maintenance of three hulls",
            "Difficult maneuvering and anchoring"
        ]
    ),
    "round_bilge": HullType(
        name_de="Rundbug-Rumpf",
        name_en="Round-Bilge Hull",
        speed_range_knots=(8.0, 16.0),
        froude_number_range=(0.20, 0.42),
        displacement_to_length_ratio=(120.0, 300.0),
        prismatic_coefficient_range=(0.54, 0.65),
        stability_characteristics="Good stability, natural heel damping, smooth motion",
        typical_boat_class="Cruising sailboats, traditional designs, comfortable yachts",
        sea_state_capability="Excellent seakeeping, forgiving in heavy weather",
        advantages=[
            "Excellent form stability",
            "Good structural efficiency",
            "Smooth motion through seaways",
            "Natural heel damping",
            "Good dynamic stability"
        ],
        disadvantages=[
            "Higher construction complexity than hard-chine",
            "Slightly lower speed potential",
            "More difficult to repair",
            "Less usable bilge space"
        ]
    ),
    "hard_chine": HullType(
        name_de="Knickspant (Hart-Kante)",
        name_en="Hard-Chine Hull",
        speed_range_knots=(8.0, 20.0),
        froude_number_range=(0.25, 0.55),
        displacement_to_length_ratio=(80.0, 250.0),
        prismatic_coefficient_range=(0.55, 0.65),
        stability_characteristics="Form stability dependent on tumblehome design, angular motion",
        typical_boat_class="Fishing vessels, work boats, some cruisers, trailer-able designs",
        sea_state_capability="Acceptable in moderate seas, can be wet at high speeds",
        advantages=[
            "Simpler, faster construction",
            "Good structural efficiency",
            "More usable interior volume",
            "Easy to repair",
            "Lower construction cost"
        ],
        disadvantages=[
            "Less refined motion characteristics",
            "Poor form stability unless designed carefully",
            "Can be wet in rough seas",
            "Higher dynamic loads on structure",
            "Less comfortable motion"
        ]
    ),
    "multichine": HullType(
        name_de="Mehrspant",
        name_en="Multi-Chine Hull",
        speed_range_knots=(8.0, 18.0),
        froude_number_range=(0.22, 0.50),
        displacement_to_length_ratio=(100.0, 280.0),
        prismatic_coefficient_range=(0.56, 0.66),
        stability_characteristics="Good stability, improved seakeeping vs hard-chine, angular motion",
        typical_boat_class="Cruisers, fishing boats, performance work boats",
        sea_state_capability="Good in moderate seas, improved over single hard-chine",
        advantages=[
            "Better form stability than hard-chine",
            "Reasonable construction complexity",
            "Good speed potential",
            "Better motion than hard-chine",
            "Practical construction methods"
        ],
        disadvantages=[
            "More complex than single hard-chine",
            "Still less refined than round-bilge",
            "Multiple chine lines add construction time"
        ]
    )
}


KEEL_TYPES: Dict[str, KeelType] = {
    "full_keel": KeelType(
        name_de="Langkiel",
        name_en="Full Keel",
        draft_range_m=(1.2, 3.0),
        ballast_ratio_range=(0.30, 0.50),
        righting_moment_characteristics="High, progressive, stable at all heel angles",
        windward_performance="Moderate, good tracking, weatherly in rough conditions",
        structural_requirements="Minimal bending loads, simple attachment, forgiving to grounding",
        grounding_behavior="Contacts bottom progressively, generally safe, minimal damage potential",
        typical_boat_class="Cruising sailboats, offshore vessels, traditional designs, heavy displacement",
        maintenance_level="Low maintenance, easily inspected, simple repair",
        failure_modes=["Galvanic corrosion at ballast interface", "Paint breakdown in high-flow areas"]
    ),
    "fin_keel": KeelType(
        name_de="Kurzkiel (Fin)",
        name_en="Fin Keel",
        draft_range_m=(1.5, 3.5),
        ballast_ratio_range=(0.40, 0.65),
        righting_moment_characteristics="High at moderate heel, progressive to 25-30 degrees",
        windward_performance="Excellent, reduces leeway, high pointing ability",
        structural_requirements="High bending loads, requires strong attachment, stiff design",
        grounding_behavior="Abrupt, can cause significant damage, load concentration",
        typical_boat_class="Performance cruisers, racing yachts, modern designs",
        maintenance_level="Medium maintenance, regular inspection of root fillet",
        failure_modes=["Root fillet cracking under extreme loads", "Deflection at deep heel angles", "Keel-hull bond failure"]
    ),
    "bulb_keel": KeelType(
        name_de="Ansatzstabkiel (Bulb)",
        name_en="Bulb Keel",
        draft_range_m=(1.8, 3.8),
        ballast_ratio_range=(0.45, 0.70),
        righting_moment_characteristics="Very high at all heel angles due to bulb moment",
        windward_performance="Excellent, outstanding pointing, low leeway",
        structural_requirements="Very high bending loads, reinforced root, complex internal structure",
        grounding_behavior="Catastrophic risk, bulb impact can compromise hull integrity",
        typical_boat_class="High-performance racing yachts, offshore racing, light-displacement cruisers",
        maintenance_level="High maintenance, regular ultrasonic inspection required",
        failure_modes=["Bulb separation from keel shaft", "Internal casting defects", "Root failure under extreme conditions", "Water infiltration into hollow bulb"]
    ),
    "t_keel": KeelType(
        name_de="T-Kiel",
        name_en="T-Keel",
        draft_range_m=(1.6, 3.5),
        ballast_ratio_range=(0.42, 0.62),
        righting_moment_characteristics="High, optimized for offshore racing, powerful at heel",
        windward_performance="Excellent, very good pointing, low drag configuration",
        structural_requirements="High bending and torsional loads, requires reinforced root",
        grounding_behavior="Abrupt contact, potential for significant keel damage",
        typical_boat_class="Offshore racing yachts, performance cruisers, IMS/ORC designs",
        maintenance_level="High maintenance, regular inspection of winglet attachment",
        failure_modes=["Winglet failure under extreme conditions", "Root fillet cracking", "Keel-hull separation", "Steering loads via rudder attachment"]
    ),
    "swing_keel": KeelType(
        name_de="Schwenkkiel",
        name_en="Swing Keel",
        draft_range_m=(0.4, 2.5),
        ballast_ratio_range=(0.25, 0.45),
        righting_moment_characteristics="Moderate to good depending on ballast, less stable when retracted",
        windward_performance="Good when deployed, reduced when partially retracted",
        structural_requirements="Requires strong pivot and hinge structure, wear-resistant materials",
        grounding_behavior="Can absorb some impact by swinging, reduced damage risk",
        typical_boat_class="Shoal-draft cruisers, trailerable designs, shallow-water boats",
        maintenance_level="Medium-high maintenance, regular inspection of hinge and pivot bearings",
        failure_modes=["Corrosion of hinge mechanism", "Wear in pivot bearing", "Hydraulic/manual system failure", "Water ingress into pivot area", "Loss of keel during operation"]
    ),
    "lifting_keel": KeelType(
        name_de="Hubkiel",
        name_en="Lifting Keel",
        draft_range_m=(0.35, 2.5),
        ballast_ratio_range=(0.30, 0.50),
        righting_moment_characteristics="Good when deployed, compromised when partially raised",
        windward_performance="Excellent when fully deployed, acceptable partially raised",
        structural_requirements="Vertical load path, strong guide rails, smooth operation essential",
        grounding_behavior="Can be retracted to minimize damage, flexible shallow-water capability",
        typical_boat_class="Shallow-draft cruisers, expedition vessels, variable-draft designs",
        maintenance_level="High maintenance, rail corrosion, seal degradation common",
        failure_modes=["Guide rail corrosion and jamming", "Seal failure and water ingress", "Hydraulic system malfunction", "Keel dropping while operating", "Lateral movement in seaway"]
    ),
    "bilge_keel": KeelType(
        name_de="Kimmkiel",
        name_en="Bilge Keel",
        draft_range_m=(0.6, 1.5),
        ballast_ratio_range=(0.15, 0.30),
        righting_moment_characteristics="Low, provides form stability primarily, heel-dependent",
        windward_performance="Reduced leeway vs no keel, but inferior to centralized keels",
        structural_requirements="Minimal bending loads, simple bolted attachment",
        grounding_behavior="Very forgiving, minimal damage, easily repaired",
        typical_boat_class="Shoal-draft cruisers, fishing vessels, beachable designs, canoe sterns",
        maintenance_level="Low maintenance, easy repair and replacement",
        failure_modes=["Bolt corrosion and loosening", "Local hull stressing at attachment points"]
    ),
    "centerboard": KeelType(
        name_de="Schwertbrett (Centerboard)",
        name_en="Centerboard / Daggerboard",
        draft_range_m=(0.3, 1.8),
        ballast_ratio_range=(0.10, 0.25),
        righting_moment_characteristics="Form stability primary, ballast minimal, heel sensitive",
        windward_performance="Good when deployed, excellent pointing in light air",
        structural_requirements="Pivot bearing wear resistance, smooth operation critical",
        grounding_behavior="Fully retracts, minimal damage possible",
        typical_boat_class="Dinghy sailing, small cruisers, training vessels, racing classes",
        maintenance_level="Medium maintenance, wear in bearings increases gradually",
        failure_modes=["Bearing wear and binding", "Water ingress around pivot", "Pendant line failure", "Emergency retraction jamming"]
    ),
    "canting_keel": KeelType(
        name_de="Schwenkbarer Bulbkiel",
        name_en="Canting Keel",
        draft_range_m=(1.8, 4.0),
        ballast_ratio_range=(0.50, 0.75),
        righting_moment_characteristics="Exceptional righting moment, adjustable by canting angle",
        windward_performance="Outstanding, zero heel potential in optimized configuration",
        structural_requirements="Extreme bending loads, hydraulic system critical, robust design mandatory",
        grounding_behavior="Very high risk of catastrophic failure, expensive damage",
        typical_boat_class="High-performance racing yachts, America's Cup class, VO70 class",
        maintenance_level="Very high maintenance, complex hydraulic and structural inspection",
        failure_modes=["Hydraulic system failure", "Keel separation at extreme canting angles", "Structural fatigue at bearing", "Loss of sail-carrying ability if system fails"]
    )
}


RUDDER_TYPES: Dict[str, RudderType] = {
    "spade_rudder": RudderType(
        name_de="Spatenruder",
        name_en="Spade Rudder",
        efficiency_rating="Excellent, high control authority, minimal drag",
        control_authority="Very high, responsive steering, direct feedback",
        structural_vulnerability="High, exposed to impacts and cavitation, root cracking common",
        bearing_types=["Pintle and gudgeon", "Upper and lower skeg bearing", "Flange bearing at hull"],
        typical_boat_class="Performance yachts, racing designs, modern cruisers",
        failure_modes=["Root fillet cracking under hard steering loads", "Cavitation erosion at aft edge", "Bearing failure and uncontrolled movement", "Rudder-hull separation under impact"]
    ),
    "skeg_hung": RudderType(
        name_de="Skeggehenkt",
        name_en="Skeg-Hung Rudder",
        efficiency_rating="Very good, supported by skeg, reasonable control authority",
        control_authority="Good, slightly reduced vs spade due to skeg influence",
        structural_vulnerability="Lower than spade, skeg provides impact protection",
        bearing_types=["Pintle/gudgeon at skeg", "Upper bearing in hull", "Flange mount at skeg head"],
        typical_boat_class="Cruising sailboats, offshore yachts, traditional designs",
        failure_modes=["Skeg attachment failure", "Rudder-skeg separation", "Bearing corrosion at skeg junction", "Structural fatigue in skeg"]
    ),
    "full_keel_attached": RudderType(
        name_de="Langkielgehenkt",
        name_en="Full-Keel Attached Rudder",
        efficiency_rating="Good, integrated with keel, reduced total drag",
        control_authority="Adequate, limited by integrated design, slightly over-balanced naturally",
        structural_vulnerability="Low, well-protected by keel, robust configuration",
        bearing_types=["Integral to keel structure", "Single pivot bearing", "Rudder horn attachment"],
        typical_boat_class="Traditional cruisers, heavy-displacement vessels, comfortable offshore yachts",
        failure_modes=["Keel-rudder bond failure", "Bearing wear over time", "Unbalanced forces causing helm changes"]
    ),
    "balanced_spade": RudderType(
        name_de="Balanciertes Spatenruder",
        name_en="Balanced Spade Rudder",
        efficiency_rating="Excellent, reduced steering effort, high control authority",
        control_authority="Very high, self-centering characteristics reduce fatigue",
        structural_vulnerability="High at pivot, balanced design reduces root loads slightly",
        bearing_types=["Upper and lower bearings", "Flange mount at pivot", "Roller bearing typical"],
        typical_boat_class="Cruising yachts, high-displacement vessels, motorsailers",
        failure_modes=["Over-balancing in extreme conditions", "Bearing failure from balance loads", "Torque-steering effects"]
    ),
    "twin_rudders": RudderType(
        name_de="Zwillingsruder",
        name_en="Twin Rudders",
        efficiency_rating="Good total, distributed loading, differential steering possible",
        control_authority="Very good, each rudder independently effective",
        structural_vulnerability="Lower per rudder, but doubled complexity and cost",
        bearing_types=["Individual rudder bearings", "Each requires independent support", "Typical on wide sterns"],
        typical_boat_class="Catamarans, wide-sterned powerboats, some trimarans",
        failure_modes=["Imbalanced steering if one rudder fails", "Complex plumbing and mechanics", "Cavitation on inside rudder at high speeds"]
    ),
    "transom_hung": RudderType(
        name_de="Spiegel-gehenkt",
        name_en="Transom-Hung Rudder",
        efficiency_rating="Acceptable, simple integration, adequate control",
        control_authority="Moderate, practical for smaller vessels",
        structural_vulnerability="Moderate, transom loading, pintle stress concentration",
        bearing_types=["Pintle and gudgeon set", "Flange mount at transom", "May use tiller or quadrant"],
        typical_boat_class="Trawlers, workboats, small outboard cruisers",
        failure_modes=["Transom cracking under steering loads", "Pintle corrosion", "Rudder loss if pintles fail"]
    )
}


PROPELLER_CONFIGURATIONS: Dict[str, Dict[str, Any]] = {
    "single_screw_center": {
        "name_de": "Einzelschraube mittig",
        "name_en": "Single Screw Centerline",
        "aperture_requirements": "Clean flow, minimal hull obstruction, 1.1-1.2x prop diameter forward clearance",
        "shaft_angle": "Typically 2-5 degrees downward inclination for torpedo launch",
        "efficiency_factors": {
            "ideal_efficiency": 0.70,
            "real_efficiency": 0.55,
            "hull_coefficient": 0.80,
            "relative_rotative_efficiency": 1.05,
            "shaft_efficiency": 0.98
        },
        "typical_boat_class": "Sailboat auxiliary, motorsailers, many cruising yachts",
        "advantages": ["Simple mechanics", "Good efficiency", "Minimal drag", "Symmetrical thrust"]
    },
    "twin_screw": {
        "name_de": "Doppelschraube",
        "name_en": "Twin Screw",
        "aperture_requirements": "Spaced apertures, 1.2-1.5x prop diameter between centerlines",
        "shaft_angle": "Each typically 2-5 degrees, counter-rotating common for reduction in torque effect",
        "efficiency_factors": {
            "ideal_efficiency": 0.68,
            "real_efficiency": 0.52,
            "hull_coefficient": 0.78,
            "relative_rotative_efficiency": 1.03,
            "shaft_efficiency": 0.97
        },
        "typical_boat_class": "Trawlers, ferries, powerboats, motorsailers",
        "advantages": ["Excellent maneuvering", "Independent thrust control", "Better backing power"]
    },
    "saildrive": {
        "name_de": "Antriebswelle (Saildrive)",
        "name_en": "Saildrive / Z-Drive",
        "aperture_requirements": "Minimal hull penetration, compact, typically 0.8-1.2m draft adjustment",
        "shaft_angle": "Flexible, can vary from 0-45 degrees via universal joint",
        "efficiency_factors": {
            "ideal_efficiency": 0.65,
            "real_efficiency": 0.50,
            "hull_coefficient": 0.76,
            "relative_rotative_efficiency": 1.02,
            "shaft_efficiency": 0.95
        },
        "typical_boat_class": "Modern cruising yachts, motorsailers, performance sailboats",
        "advantages": ["Variable shaft angle", "Compact installation", "Reduced prop damage risk"]
    },
    "sailboat_folding": {
        "name_de": "Klappschraube (Segelboot)",
        "name_en": "Sailboat Folding Propeller",
        "aperture_requirements": "Standard shaft through hull, folds when not in use",
        "shaft_angle": "Standard shaft angle, prop retracts behind deadwood",
        "efficiency_factors": {
            "ideal_efficiency": 0.62,
            "real_efficiency": 0.48,
            "hull_coefficient": 0.74,
            "relative_rotative_efficiency": 1.00,
            "shaft_efficiency": 0.96
        },
        "typical_boat_class": "Cruising sailboats, ocean-going yachts, fuel-efficiency focused",
        "advantages": ["Minimal drag when folded", "Simple mechanical operation", "Easy maintenance"]
    }
}


HYDRODYNAMIC_COEFFICIENTS: Dict[str, Dict[str, Any]] = {
    "prismatic_coefficient": {
        "name_de": "Prismatischer Koeffizient (Cp)",
        "name_en": "Prismatic Coefficient (Cp)",
        "definition": "Ratio of displaced volume to volume of prism with same length and midship section area",
        "formula": "Cp = Displacement / (L_pp × A_m × ρ)",
        "typical_ranges": {
            "displacement_slow": (0.55, 0.62),
            "semi_displacement": (0.58, 0.68),
            "planning": (0.50, 0.60),
            "high_speed_planing": (0.45, 0.55)
        },
        "what_it_tells": "Distribution of volume along hull length; high Cp = full sections throughout, low Cp = concentrated sections",
        "typical_values": {
            "full_keel_cruiser": 0.59,
            "fin_keel_racer": 0.56,
            "planing_hull": 0.53,
            "motorsailer": 0.65
        }
    },
    "block_coefficient": {
        "name_de": "Völligkeitsgrad (Cb)",
        "name_en": "Block Coefficient (Cb)",
        "definition": "Ratio of displaced volume to volume of circumscribed rectangular box",
        "formula": "Cb = Displacement / (L_pp × B × T × ρ)",
        "typical_ranges": {
            "light_displacement": (0.45, 0.55),
            "moderate_displacement": (0.55, 0.65),
            "heavy_displacement": (0.65, 0.75),
            "planning": (0.35, 0.50)
        },
        "what_it_tells": "Overall 'fullness' of hull; higher Cb indicates fatter hull form with less fine underwater shape",
        "typical_values": {
            "IMS_racer": 0.48,
            "cruiser_40ft": 0.56,
            "heavy_displacement": 0.68,
            "motorsailer": 0.62
        }
    },
    "waterplane_coefficient": {
        "name_de": "Wasserlinienkoeffizient (Cwp)",
        "name_en": "Waterplane Coefficient (Cwp)",
        "definition": "Ratio of actual waterplane area to area of circumscribed rectangle",
        "formula": "Cwp = A_wp / (L_pp × B)",
        "typical_ranges": {
            "fine_bow_stern": (0.60, 0.70),
            "moderate": (0.70, 0.78),
            "full": (0.78, 0.85)
        },
        "what_it_tells": "Shape of waterplane; affects buoyancy distribution and dynamic stability",
        "typical_values": {
            "racing_yacht": 0.65,
            "cruising_yacht": 0.72,
            "trawler": 0.80
        }
    },
    "midship_coefficient": {
        "name_de": "Spantenquerschnittskoeffizient (Cm)",
        "name_en": "Midship Section Coefficient (Cm)",
        "definition": "Ratio of actual midship section area to area of circumscribed rectangle",
        "formula": "Cm = A_m / (B × T)",
        "typical_ranges": {
            "fine_sections": (0.70, 0.80),
            "moderate": (0.80, 0.90),
            "full_sections": (0.90, 0.98)
        },
        "what_it_tells": "Cross-sectional fullness at midships; lower values indicate finer, more V-shaped sections",
        "typical_values": {
            "IMS_racer": 0.73,
            "cruiser": 0.82,
            "motorsailer": 0.88
        }
    },
    "displacement_length_ratio": {
        "name_de": "Gewichtslänge-Verhältnis (D/L)",
        "name_en": "Displacement/Length Ratio (D/L)",
        "definition": "Displacement in tons divided by (L_wl/100)^3",
        "formula": "D/L = Displacement / ((L_wl/100)^3)",
        "typical_ranges": {
            "light": (0, 100),
            "moderate": (100, 200),
            "heavy": (200, 350),
            "very_heavy": (350, 600)
        },
        "what_it_tells": "Heavy displacement yachts relative to length carry more weight, slower but more stable",
        "typical_values": {
            "modern_racer": 85,
            "cruiser_cruiser": 180,
            "full_keel_cruiser": 280,
            "offshore_heavy": 350
        }
    },
    "sail_area_displacement_ratio": {
        "name_de": "Segelfläche-Gewicht-Verhältnis (SA/D)",
        "name_en": "Sail Area / Displacement Ratio (SA/D)",
        "definition": "Total sail area in sq-ft divided by displacement in tons (or normalized to volume)",
        "formula": "SA/D = Total_Sail_Area / Displacement (various normalizations exist)",
        "typical_ranges": {
            "heavy_cruiser": (14, 18),
            "cruiser": (18, 22),
            "performance_cruiser": (22, 26),
            "racer": (26, 32),
            "extreme_racer": (32, 40)
        },
        "what_it_tells": "Power available for sailing relative to weight; higher ratios indicate light-air potential",
        "typical_values": {
            "cruiser": 19.5,
            "cruiser_racer": 23.0,
            "IMS_racer": 27.5,
            "doublehanded_racer": 31.0
        }
    },
    "speed_length_ratio": {
        "name_de": "Geschwindigkeit-Länge-Verhältnis",
        "name_en": "Speed/Length Ratio",
        "definition": "Actual speed (knots) divided by square root of waterline length (feet)",
        "formula": "Speed/Length = V / sqrt(L_wl)",
        "typical_ranges": {
            "displacement_sailboat": (0.9, 1.3),
            "cruiser_sailboat": (1.1, 1.5),
            "performance_sailboat": (1.3, 1.8),
            "powerboat_cruiser": (1.5, 2.2),
            "planning_powerboat": (2.5, 4.0)
        },
        "what_it_tells": "Speed relative to hull length; higher ratios indicate faster, potentially less efficient designs",
        "typical_values": {
            "full_keel_sailer": 1.1,
            "modern_racer": 1.6,
            "motorsailer": 1.8,
            "fast_cruiser": 2.1
        }
    },
    "froude_number": {
        "name_de": "Froude-Zahl (Fn)",
        "name_en": "Froude Number (Fn)",
        "definition": "Speed divided by square root of (gravity × waterline length), dimensionless velocity metric",
        "formula": "Fn = V / sqrt(g × L_wl)",
        "typical_ranges": {
            "displacement": (0.15, 0.35),
            "semi_displacement": (0.35, 0.55),
            "semi_planning": (0.55, 0.85),
            "planning": (0.85, 2.50)
        },
        "what_it_tells": "Governs wave-making characteristics and resistance components; critical for resistance prediction",
        "typical_values": {
            "cruising_sailboat_6kt": 0.18,
            "motorsailer_10kt": 0.33,
            "performance_cruiser_12kt": 0.42,
            "planning_hull_20kt": 1.85
        }
    }
}


STABILITY_CONCEPTS: Dict[str, Dict[str, Any]] = {
    "gz_curve": {
        "name_de": "GZ-Kurve (Hebelarmkurve)",
        "name_en": "GZ Curve (Righting Arm Curve)",
        "definition": "Graphical representation of righting moment arm vs. heel angle",
        "measurement_method": "Hydrostatic calculations or physical inclining experiment",
        "typical_ranges_by_class": {
            "ims_yacht": "GZ_max at 35-45°, AVS > 130°",
            "cruiser": "GZ_max at 30-40°, AVS > 120°",
            "heavy_displacement": "GZ_max at 25-35°, AVS > 110°",
            "racer": "GZ_max at 40-50°, AVS > 140°"
        },
        "regulatory_requirements": "ISO 12217-1 and -2 specify minimum GZ values at standard heel angles",
        "key_parameters": {
            "gz_maximum": "Peak of curve indicates maximum righting moment",
            "angle_at_maximum": "Heel angle where maximum righting moment occurs",
            "ave_stability": "Area under curve to 30° or AVS",
            "initial_stability_gm": "Slope at zero heel, related to metacentric height"
        }
    },
    "metacentric_height": {
        "name_de": "Metazentrische Höhe (GM)",
        "name_en": "Metacentric Height (GM)",
        "definition": "Vertical distance between center of gravity (G) and metacenter (M) of vessel",
        "measurement_method": "Hydrostatic calculations from hull form and weight distribution",
        "typical_ranges_by_class": {
            "ims_racer": (0.8, 1.2),
            "performance_cruiser": (1.0, 1.5),
            "cruiser": (1.2, 1.8),
            "motorsailer": (1.5, 2.2),
            "heavy_displacement": (2.0, 3.0)
        },
        "formula": "GM = BM - BG where BM = I/V (second moment / displaced volume)",
        "what_indicates": "Initial stability; higher GM = stiffer boat with quick heel response, lower GM = easier sail carrying",
        "practical_implications": {
            "gm_too_low": "Tender feel, gentle heel, slow return, potential capsize risk",
            "gm_too_high": "Very stiff, rapid heel, jerky motion, difficult to sail, crew discomfort",
            "gm_sweet_spot": "1.2-1.8m for cruiser represents good balance of comfort and stability"
        }
    },
    "angle_vanishing_stability": {
        "name_de": "Winkel des verschwindenden Stabilitätsmoments (AVS)",
        "name_en": "Angle of Vanishing Stability (AVS)",
        "definition": "Heel angle at which GZ curve returns to zero; beyond this angle vessel cannot self-right",
        "measurement_method": "Read from GZ curve where righting moment arm returns to zero",
        "typical_ranges_by_class": {
            "ims_racer": (130, 150),
            "performance_cruiser": (120, 140),
            "cruiser": (110, 130),
            "motorsailer": (105, 125),
            "heavy_displacement": (100, 120)
        },
        "regulatory_minimum_iso_12217": "> 90° for Category A vessels; > 80° for Categories B/C/D",
        "what_indicates": "Margin to capsize; larger AVS provides more safety buffer in extreme conditions",
        "critical_note": "AVS alone insufficient for safety assessment; GZ curve shape and GZ values at intermediate angles also crucial"
    },
    "stix_index": {
        "name_de": "STIX-Index",
        "name_en": "STIX Index (Stability Index)",
        "definition": "Numeric stability predictor: STIX = (GZ_30 + GZ_40 + GZ_50) / 3 × (GZ_max_heel) × (AVS - 90)",
        "measurement_method": "Calculated from GZ curve values at three standard heel angles",
        "typical_ranges": {
            "marginal": (1.0, 2.0),
            "acceptable": (2.0, 3.5),
            "good": (3.5, 6.0),
            "excellent": (6.0, 10.0)
        },
        "what_indicates": "Combined stability metric easier to communicate than full GZ curve, useful for quick assessment",
        "limitations": "STIX simplified metric; cannot replace full GZ curve analysis for design decisions"
    },
    "iso_categories": {
        "name_de": "ISO 12217 Kategorien",
        "name_en": "ISO 12217 Stability Categories",
        "category_a": {
            "description": "Ocean, exposure to waves with significant height > 4m, remote from shelter",
            "typical_use": "Offshore racing, long-distance cruising",
            "min_avs": 130,
            "min_gz_values": "GZ_30 >= 0.20m, GZ_40 >= 0.35m, GZ_50 >= 0.40m or AVS"
        },
        "category_b": {
            "description": "Coastal, significant wave height 2-4m, shelter available within distance",
            "typical_use": "Cruising within reasonable distance of land",
            "min_avs": 120,
            "min_gz_values": "GZ_30 >= 0.17m, GZ_40 >= 0.30m"
        },
        "category_c": {
            "description": "Sheltered waters, significant wave height < 2m, rapid access to shelter",
            "typical_use": "Day sailing, inland cruising",
            "min_avs": 110,
            "min_gz_values": "GZ_30 >= 0.12m, GZ_40 >= 0.24m"
        },
        "category_d": {
            "description": "Small lakes/rivers, protected bays, significant wave height < 0.5m",
            "typical_use": "Training, small day boats",
            "min_avs": 90,
            "min_gz_values": "GZ_30 >= 0.09m"
        }
    },
    "downflooding_angle": {
        "name_de": "Flutungswinkel",
        "name_en": "Downflooding Angle",
        "definition": "Heel angle at which water first enters hull via openings (windows, companionways, vents)",
        "measurement_method": "Identified from hull plans; lowest opening point that could allow water ingress",
        "typical_values": {
            "modern_yacht": (40, 60),
            "cruising_yacht": (30, 50),
            "racing_yacht": (45, 70),
            "motorsailer": (25, 40)
        },
        "regulatory_requirement": "ISO 12217 requires downflooding angle > AVS or at least 10° greater",
        "design_implication": "Critical for vessel seaworthiness; limits effective useful sailing range and safety",
        "practical_consideration": "Downflooding angle often limit factor for traditional yacht heel angles"
    }
}


RESISTANCE_COMPONENTS: Dict[str, Dict[str, Any]] = {
    "friction_resistance": {
        "name_de": "Reibungswiderstand",
        "name_en": "Friction Resistance",
        "definition": "Viscous drag acting on hull surface due to fluid friction; largest component at low speeds",
        "percentage_of_total": {
            "displacement_6kts": 0.75,
            "displacement_10kts": 0.65,
            "semi_displacement_15kts": 0.55,
            "planing_20kts": 0.25
        },
        "estimation_formula": "Rf = 0.5 × ρ × V^2 × S × Cf where Cf from ITTC line or similar",
        "variables": {
            "rho": "Water density (1025 kg/m³ seawater)",
            "V": "Vessel speed m/s",
            "S": "Wetted surface area m²",
            "Cf": "Friction coefficient from ITTC 1957 line or Schoenherr line"
        },
        "reduction_factors": {
            "hull_roughness": -0.02,
            "biofouling": -0.05,
            "low_speed": 0.03
        }
    },
    "wave_making_resistance": {
        "name_de": "Wellenerzeugungswiderstand",
        "name_en": "Wave-Making Resistance",
        "definition": "Energy-dissipation resistance due to generation of waves by hull moving through water",
        "percentage_of_total": {
            "displacement_low_fn": 0.15,
            "displacement_high_fn": 0.30,
            "semi_displacement": 0.35,
            "planing": 0.30
        },
        "froude_number_dependence": "Rw ∝ (Fn)^n where n varies with speed range, dramatically increases near Fn=0.55",
        "estimation_methods": ["Michell integral", "Havelock curves", "Delft series regression"],
        "hump_speed": "Near Fn=0.35-0.45 for many hulls, pronounced wave resistance increase",
        "design_consideration": "Critical factor limiting speed-to-length ratios for displacement hulls"
    },
    "form_resistance": {
        "name_de": "Formwiderstand",
        "name_en": "Form Resistance / Pressure Drag",
        "definition": "Viscous pressure drag from flow separation and adverse pressure gradients",
        "percentage_of_total": {
            "fine_hull": 0.05,
            "moderate_hull": 0.10,
            "full_hull": 0.15
        },
        "typically_modeled_as": "Form drag coefficient multiplied by dynamic pressure and reference area",
        "reduction_strategy": "Fair hull lines, avoid abrupt shape changes, optimize forebody design",
        "estimation": "Often grouped with friction resistance in simplified methods; separate in CFD"
    },
    "appendage_resistance": {
        "name_de": "Zusatzwiderstand (Kiel, Ruder, etc.)",
        "name_en": "Appendage Resistance",
        "definition": "Drag from keel, rudder, shaft, struts and other underwater appendages",
        "percentage_of_total": {
            "sailboat_with_keel": 0.15,
            "sailboat_with_bulb": 0.18,
            "motorboat": 0.10
        },
        "components": {
            "keel_drag": "Skin friction + form drag + induced drag from lift generation",
            "rudder_drag": "Typically 3-5% of total when neutral",
            "shaft_strut_drag": "Minor but measurable",
            "through_hull_fittings": "Minor contributor"
        },
        "estimation": "Separate drag coefficients for each appendage from NACA or empirical data"
    },
    "wind_resistance": {
        "name_de": "Luftwiderstand",
        "name_en": "Wind Resistance / Air Drag",
        "definition": "Aerodynamic drag on hull, superstructure, rigging and crew/contents above waterline",
        "percentage_of_total": {
            "displacement_sailboat": 0.02,
            "cruiser_motorsailer": 0.03,
            "motor_yacht": 0.05,
            "high_freeboard_ferry": 0.10
        },
        "formula": "Rair = 0.5 × ρ_air × V_rel^2 × A_proj × Cd",
        "typical_drag_coefficients": {
            "modern_hull_form": 0.50,
            "traditional_hull": 0.65,
            "with_standing_rigging": 0.70,
            "with_sails_deployed": 1.10
        }
    },
    "added_resistance_waves": {
        "name_de": "Zusatzwiderstand in See",
        "name_en": "Added Resistance in Waves",
        "definition": "Additional resistance due to sea state; hull must continually generate waves in seaway",
        "percentage_of_total": {
            "calm_water": 0.0,
            "moderate_sea": 0.15,
            "heavy_sea": 0.50,
            "extreme_sea": 1.50
        },
        "estimation_methods": ["Faltinsen approach", "Regression models", "CFD with dynamic mesh"],
        "weather_routing_implication": "Can increase fuel consumption 20-50% in actual sea conditions vs calm-water predictions",
        "practical_note": "Most complex resistance component; requires specialized tools for accurate prediction"
    }
}


HULL_CONSTRUCTION_METHODS: Dict[str, Dict[str, Any]] = {
    "grp_hand_laminate": {
        "name_de": "GFK Handlaminat",
        "name_en": "GRP Hand Laminate",
        "weight_factor": 1.0,
        "stiffness": "Moderate to high with core material; lower with solid laminate",
        "maintenance": "Regular repainting, osmotic blister risk, UV degradation of gelcoat",
        "repairability": "Excellent, can repair with overlapping patches",
        "cost_factor": 1.0,
        "typical_boat_class": "Most cruising yachts, traditional production boats, entry-level cruisers",
        "minimum_wall_thickness_ranges": {
            "small_yacht_24ft": (3.5, 4.5),
            "cruiser_40ft": (5.0, 6.5),
            "large_cruiser_60ft": (7.0, 9.0),
            "units": "mm"
        },
        "advantages": [
            "Proven track record 50+ years",
            "Relatively simple production process",
            "Good repairability",
            "Lower tooling cost",
            "Good sea-worthiness"
        ],
        "disadvantages": [
            "Labor-intensive lamination",
            "Osmotic blistering risk",
            "Higher voids and variability",
            "Heavier per stiffness",
            "Gelcoat degradation in tropical UV"
        ]
    },
    "grp_vacuum_infusion": {
        "name_de": "GFK Vakuuminfusion",
        "name_en": "GRP Vacuum Infusion",
        "weight_factor": 0.85,
        "stiffness": "High, precise fiber control, minimal voids",
        "maintenance": "Paint system, better osmotic protection, careful gelcoat handling",
        "repairability": "Good with specialized tools, more complex than laminate",
        "cost_factor": 1.3,
        "typical_boat_class": "High-performance yachts, racing boats, premium cruisers",
        "minimum_wall_thickness_ranges": {
            "small_yacht_24ft": (2.8, 3.5),
            "cruiser_40ft": (3.8, 4.8),
            "large_cruiser_60ft": (5.0, 6.5),
            "units": "mm"
        },
        "advantages": [
            "15-20% weight reduction",
            "Lower void content (< 2%)",
            "Better fiber wet-out",
            "Reduced styrene emissions",
            "Better gelcoat adhesion"
        ],
        "disadvantages": [
            "Complex process requiring skilled labor",
            "Higher equipment cost",
            "Longer production time",
            "Quality dependent on tool design",
            "Repair more difficult than laminate"
        ]
    },
    "sandwich": {
        "name_de": "Sandwich-Konstruktion",
        "name_en": "Sandwich Construction",
        "weight_factor": 0.65,
        "stiffness": "Very high for weight; moment of inertia advantage",
        "maintenance": "Paint, edge protection critical, delamination risk if damaged",
        "repairability": "Difficult, requires rebuild of core section",
        "cost_factor": 1.6,
        "typical_boat_class": "Performance cruisers, racing yachts, large displacement cruisers",
        "minimum_wall_thickness_ranges": {
            "small_yacht_24ft": (4.0, 5.0),
            "cruiser_40ft": (5.5, 7.0),
            "large_cruiser_60ft": (7.5, 9.5),
            "units": "mm total thickness"
        },
        "core_materials": {
            "PVC_foam": {"density": (60, 100), "cost": 1.0, "durability": "Good"},
            "polyurethane": {"density": (30, 60), "cost": 1.1, "durability": "Excellent"},
            "balsa": {"density": (100, 150), "cost": 1.3, "durability": "Good if sealed"},
            "aramid": {"density": (50, 90), "cost": 2.0, "durability": "Excellent"}
        },
        "advantages": [
            "Excellent stiffness-to-weight",
            "Superior damping characteristics",
            "Impact energy absorption",
            "Good insulation properties",
            "Reduced fatigue stress"
        ],
        "disadvantages": [
            "Highest material cost",
            "Delamination risk if water infiltrates",
            "Core compression under point loads",
            "Difficult repairs",
            "Weight gain if delamination occurs"
        ]
    },
    "aluminum": {
        "name_de": "Aluminium",
        "name_en": "Aluminum",
        "weight_factor": 1.35,
        "stiffness": "Very high; requires less thickness than composite",
        "maintenance": "Anodizing degradation, galvanic corrosion in seawater, frequent repainting",
        "repairability": "Moderate, requires welding expertise",
        "cost_factor": 1.2,
        "typical_boat_class": "Working vessels, expedition yachts, fast ferries, commercial vessels",
        "minimum_wall_thickness_ranges": {
            "small_yacht_24ft": (2.5, 3.5),
            "cruiser_40ft": (3.5, 5.0),
            "large_cruiser_60ft": (5.0, 7.0),
            "units": "mm"
        },
        "alloys_common": {
            "5083_h321": {"corrosion_resistance": "Good", "weldability": "Excellent", "strength": "Moderate"},
            "6061_t6": {"corrosion_resistance": "Moderate", "weldability": "Good", "strength": "Moderate"},
            "7075": {"corrosion_resistance": "Poor", "weldability": "Fair", "strength": "Excellent"}
        },
        "advantages": [
            "Very high stiffness",
            "Proven durability 40+ years",
            "High strength-to-weight for large vessels",
            "Weldable, good for custom builds",
            "Excellent for expedition vessels"
        ],
        "disadvantages": [
            "Heavier than modern composites",
            "Galvanic corrosion risk without cathodic protection",
            "Labor-intensive surface preparation",
            "Higher maintenance costs",
            "Difficult to repair in remote locations"
        ]
    },
    "steel": {
        "name_de": "Stahl",
        "name_en": "Steel",
        "weight_factor": 1.85,
        "stiffness": "Very high; allows thin plating",
        "maintenance": "Continuous paint maintenance, corrosion risk in bilges, coating critical",
        "repairability": "Excellent, welding straightforward, repairs easy anywhere",
        "cost_factor": 0.9,
        "typical_boat_class": "Working boats, commercial vessels, some expedition yachts, superyachts",
        "minimum_wall_thickness_ranges": {
            "small_yacht_24ft": (1.5, 2.0),
            "cruiser_40ft": (2.0, 3.0),
            "large_cruiser_60ft": (3.0, 4.5),
            "units": "mm"
        },
        "steel_grades": {
            "mild_steel": {"strength": "Moderate", "corrosion_rate": "High", "weldability": "Excellent"},
            "ab_cd_grade": {"strength": "Moderate", "corrosion_rate": "High", "weldability": "Excellent"},
            "weathering_steel": {"strength": "Moderate", "corrosion_rate": "Very low", "weldability": "Good"}
        },
        "advantages": [
            "Lowest material cost",
            "Excellent weldability",
            "Easiest to repair anywhere",
            "High strength allows thin sections",
            "Excellent for welded custom builds"
        ],
        "disadvantages": [
            "Heaviest construction material",
            "Continuous corrosion risk",
            "High maintenance painting required",
            "Interior rust if moisture management poor",
            "Limited lifespan without active corrosion control (30-40 years typical)"
        ]
    },
    "wood_epoxy": {
        "name_de": "Holz-Epoxid (WEST)",
        "name_en": "Wood-Epoxy (WEST System)",
        "weight_factor": 0.95,
        "stiffness": "Moderate to high depending on wood selection",
        "maintenance": "Varnish refinishing, moisture protection, wood checking",
        "repairability": "Excellent, traditional woodworking repairs possible",
        "cost_factor": 1.4,
        "typical_boat_class": "Classic yachts, cruising yachts, cold-water expedition vessels",
        "minimum_wall_thickness_ranges": {
            "small_yacht_24ft": (20, 30),
            "cruiser_40ft": (30, 40),
            "large_cruiser_60ft": (40, 60),
            "units": "mm planking"
        },
        "wood_selections": {
            "spruce": {"strength": "Good", "durability": "Poor", "weight": "Light"},
            "oak": {"strength": "Excellent", "durability": "Good", "weight": "Heavy"},
            "mahogany": {"strength": "Good", "durability": "Excellent", "weight": "Heavy"},
            "teak": {"strength": "Excellent", "durability": "Excellent", "weight": "Heavy"}
        },
        "advantages": [
            "Classic aesthetic",
            "Excellent workability",
            "Easy repairs in field",
            "Good tactile qualities",
            "Low environmental impact if properly sourced"
        ],
        "disadvantages": [
            "High labor cost for construction",
            "Continuous maintenance required",
            "Shorter lifespan than composite/aluminum",
            "Moisture sensitivity",
            "Requires expertise for proper epoxy application",
            "Limited availability of quality timber"
        ]
    },
    "ferrocement": {
        "name_de": "Ferrozement",
        "name_en": "Ferrocement",
        "weight_factor": 1.65,
        "stiffness": "Very high but brittle",
        "maintenance": "Paint maintenance, corrosion risk if cement fails, crack monitoring",
        "repairability": "Difficult, requires patch welding and relining",
        "cost_factor": 0.85,
        "typical_boat_class": "Fishing boats, working vessels, some cruising yachts (older designs)",
        "minimum_wall_thickness_ranges": {
            "small_yacht_24ft": (12, 16),
            "cruiser_40ft": (16, 20),
            "large_cruiser_60ft": (20, 30),
            "units": "mm"
        },
        "construction_method": "Steel wire mesh encased in cement mortar; traditional development no longer common",
        "advantages": [
            "Very low material cost",
            "Good compressive strength",
            "Can be built with basic tools",
            "Suitable for developing countries",
            "Reasonable strength for displacement hulls"
        ],
        "disadvantages": [
            "Very heavy for performance",
            "Brittle, poor impact resistance",
            "Difficult to repair cracks",
            "Water ingress through cracks common",
            "Labor-intensive construction",
            "No longer commonly built; support limited"
        ]
    }
}


def calculate_cp_range(hull_type_key: str) -> Tuple[float, float]:
    """
    Return typical prismatic coefficient range for given hull type.
    """
    if hull_type_key not in HULL_TYPES:
        return (0.55, 0.65)
    return HULL_TYPES[hull_type_key].prismatic_coefficient_range


def calculate_fn_at_speed(speed_knots: float, length_wl_m: float) -> float:
    """
    Calculate Froude number from speed and waterline length.
    Fn = V / sqrt(g * L_wl) where V in m/s, g = 9.81 m/s²
    """
    speed_ms = speed_knots * 0.51444
    g = 9.81
    if length_wl_m <= 0:
        return 0.0
    fn = speed_ms / math.sqrt(g * length_wl_m)
    return round(fn, 3)


def assess_stability_iso_category(gz_max_m: float, avs_deg: float,
                                   gz_30_m: float = None, gz_40_m: float = None) -> Dict[str, Any]:
    """
    Assess which ISO 12217 category vessel meets based on stability parameters.
    Returns category recommendation and compliance details.
    """
    compliant_categories = []

    # Category A: AVS >= 130, GZ_30 >= 0.20, GZ_40 >= 0.35
    if avs_deg >= 130 and (gz_30_m is None or gz_30_m >= 0.20) and (gz_40_m is None or gz_40_m >= 0.35):
        compliant_categories.append("A")

    # Category B: AVS >= 120, GZ_30 >= 0.17, GZ_40 >= 0.30
    if avs_deg >= 120 and (gz_30_m is None or gz_30_m >= 0.17) and (gz_40_m is None or gz_40_m >= 0.30):
        compliant_categories.append("B")

    # Category C: AVS >= 110, GZ_30 >= 0.12, GZ_40 >= 0.24
    if avs_deg >= 110 and (gz_30_m is None or gz_30_m >= 0.12) and (gz_40_m is None or gz_40_m >= 0.24):
        compliant_categories.append("C")

    # Category D: AVS >= 90, GZ_30 >= 0.09
    if avs_deg >= 90 and (gz_30_m is None or gz_30_m >= 0.09):
        compliant_categories.append("D")

    highest_category = compliant_categories[0] if compliant_categories else "Non-compliant"

    return {
        "highest_category": highest_category,
        "compliant_categories": compliant_categories,
        "gz_max_m": gz_max_m,
        "avs_deg": avs_deg,
        "assessment": f"Vessel meets minimum ISO 12217-{highest_category} requirements"
    }


def estimate_froude_resistance_regime(fn: float) -> Dict[str, Any]:
    """
    Classify Froude number and describe resistance characteristics and design implications.
    """
    if fn < 0.25:
        regime = "Displacement (Low Speed)"
        dominant_resistance = "Friction dominant, wave-making secondary"
        hull_type_suitable = ["Full keel displacement", "Langkiel", "Heavy cruiser"]
    elif fn < 0.45:
        regime = "Displacement (Moderate Speed)"
        dominant_resistance = "Friction and wave-making balanced; hump region possible"
        hull_type_suitable = ["Fin keel cruiser", "Semi-displacement", "Performance cruiser"]
    elif fn < 0.65:
        regime = "Semi-Displacement"
        dominant_resistance = "Wave-making peak; trim very sensitive; resistance spike likely"
        hull_type_suitable = ["Semi-displacement", "Motorsailer", "Light displacement racer"]
    elif fn < 1.0:
        regime = "Early Planing"
        dominant_resistance = "Wave-making reducing, induced drag increasing"
        hull_type_suitable = ["Planing hull", "Fast cruiser", "Performance speedboat"]
    else:
        regime = "Full Planing"
        dominant_resistance = "Dynamic lift supports hull; wave-making minimal"
        hull_type_suitable = ["Fast planing", "Speedboat", "Performance yacht"]

    return {
        "froude_number": fn,
        "regime": regime,
        "dominant_resistance": dominant_resistance,
        "suitable_hull_types": hull_type_suitable
    }


def assess_hull_design(hull_type_key: str, length_wl_m: float, beam_m: float,
                       draft_m: float, displacement_tonnes: float,
                       sailing_speed_knots: float = None) -> Dict[str, Any]:
    """
    Comprehensive assessment of hull design, returning hydrodynamic predictions,
    stability implications, and design recommendations.

    Args:
        hull_type_key: Key from HULL_TYPES dict
        length_wl_m: Waterline length in meters
        beam_m: Beam in meters
        draft_m: Draft in meters
        displacement_tonnes: Displacement in metric tonnes
        sailing_speed_knots: Typical sailing speed for assessment

    Returns:
        Dictionary with findings, recommendations, performance assessment
    """
    if hull_type_key not in HULL_TYPES:
        return {"error": f"Hull type '{hull_type_key}' not found"}

    hull = HULL_TYPES[hull_type_key]
    findings = {
        "hull_type": hull.name_en,
        "hull_type_de": hull.name_de,
        "design_parameters": {
            "length_wl_m": length_wl_m,
            "beam_m": beam_m,
            "draft_m": draft_m,
            "displacement_tonnes": displacement_tonnes
        }
    }

    # Calculate key ratios
    if length_wl_m > 0 and beam_m > 0 and draft_m > 0:
        length_beam_ratio = length_wl_m / beam_m
        beam_draft_ratio = beam_m / draft_m
        displaced_volume_m3 = displacement_tonnes / 1.025  # seawater density
        disp_length_ratio = displacement_tonnes / ((length_wl_m / 100) ** 3)

        findings["calculated_ratios"] = {
            "length_beam_ratio": round(length_beam_ratio, 2),
            "beam_draft_ratio": round(beam_draft_ratio, 2),
            "displaced_volume_m3": round(displaced_volume_m3, 2),
            "displacement_length_ratio": round(disp_length_ratio, 1)
        }

    # Froude number assessment if speed provided
    recommendations = []
    if sailing_speed_knots:
        fn = calculate_fn_at_speed(sailing_speed_knots, length_wl_m)
        findings["froude_number"] = fn
        findings["froude_analysis"] = estimate_froude_resistance_regime(fn)

        if fn not in hull.froude_number_range:
            recommendations.append(
                f"Design Froude number {fn} slightly outside typical range "
                f"{hull.froude_number_range}; consider hull form optimization"
            )

    # Design consistency check
    if hull_type_key == "displacement" and disp_length_ratio < hull.displacement_to_length_ratio[0]:
        recommendations.append(
            "Displacement-length ratio below typical for this hull type; "
            "verify form stability and weight distribution"
        )

    findings["stability_characteristics"] = hull.stability_characteristics
    findings["sea_state_capability"] = hull.sea_state_capability
    findings["typical_boat_class"] = hull.typical_boat_class
    findings["advantages"] = hull.advantages
    findings["disadvantages"] = hull.disadvantages
    findings["recommendations"] = recommendations if recommendations else ["Design appears consistent with hull type characteristics"]

    return findings


# Verification constant for knowledge base integrity
KNOWLEDGE_BASE_VERSION = "1.0-2026-03"
NAVAL_ARCHITECTURE_REFERENCE = "ISO 12217, Delft Series, Holtrop-Mennen, ITTC Guidelines"
