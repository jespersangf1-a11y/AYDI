"""
AYDI Sanitär, Interieur, Sicherheit & Normen — Tiefenwissen
Comprehensive technical knowledge on marine sanitary systems, gas installations,
interior construction, safety systems, and international standards.

Author: AYDI Research Team
Version: 1.0
"""
from typing import Dict, Any


# ============================================================================
# SEACOCK DATABASE: Material Selection & Corrosion Protection
# ============================================================================

SEACOCK_DATABASE: Dict[str, Any] = {
    "material_comparison": {
        "bronze_rotguss": {
            "key_de": "Rotguss (dezinkierungsresistent)",
            "standard": "DZR dezincification-resistant standard",
            "composition": "Copper-Tin-Zinc alloy with inhibitor elements",
            "dezincification_risk": "Minimized through DZR treatment",
            "typical_life": "15-20 years in salt water",
            "corrosion_rate": "Minimal under DZR specification",
            "cost": "Moderate",
            "reliability": "High",
            "critical_note": "Must be certified DZR for marine use",
            "standards_compliance": "ISO 1086, EN 12163",
        },
        "messing_brass": {
            "key_de": "Messing (nicht für Marine)",
            "type": "Copper-Zinc alloy without dezincification protection",
            "dezincification_mechanism": "Zinc leaches from crystal structure leaving porous copper",
            "visual_failure": "Pink/copper discoloration indicates failure",
            "case_study": "Random Harvest case: 25mm fitting complete failure",
            "failure_timeline": "16 months in service",
            "corrosion_rate": "1.275mm per year observed",
            "failure_mode": "Structural collapse and uncontrolled flooding",
            "risk_level": "CRITICAL - DO NOT USE",
            "why_failure": "Zinc preferentially corrodes, leaving brittle copper matrix",
            "indicator": "Pink staining on seacock indicates dezincification",
        },
        "marelon_composite": {
            "key_de": "Marelon Kunststoffkomposit",
            "material": "Composite plastic (acetyl copolymer)",
            "corrosion_proof": True,
            "galvanic_immunity": True,
            "typical_life": "20+ years documented service",
            "abyc_certification": "ABYC H-27 compliant",
            "temperature_range": "-20°C to +60°C",
            "advantages": [
                "Zero galvanic corrosion",
                "No dezincification risk",
                "Lighter weight",
                "Easier to work with",
                "Better for isolated through-hulls"
            ],
            "limitations": [
                "Less rigid than bronze",
                "Not suitable for high-pressure applications",
                "Operating temperature limits",
                "Potential for creep under stress"
            ],
            "cost": "Higher than brass, comparable to DZR bronze",
            "manufacturer": "Sparton Corporation",
        },
        "stainless_steel": {
            "key_de": "Edelstahl (nicht empfohlen)",
            "type": "316L or higher grade",
            "concern": "Crevice corrosion in marine environment",
            "failure_mode": "Pitting and localized corrosion",
            "risk_context": "Salt water chloride concentration activates crevices",
            "protective_film": "Passivation layer vulnerable under oxygen-depleted conditions",
            "recommendation": "NOT recommended for seacocks",
            "potential_use": "Only with active cathodic protection and maintenance",
            "inspection_requirement": "Mandatory regular inspection if used",
        },
    },
    "hose_connections": {
        "key_de": "Schlauchanschlüsse für Seecocks",
        "clamp_standard": "Double 316SS clamps mandatory below waterline",
        "clamp_specification": {
            "material": "316 Stainless Steel worm drive",
            "quantity": "Minimum 2 per connection below waterline",
            "band_width": "9mm minimum",
            "torque": "6-7 Nm for 9mm band",
            "inspection": "Tighten quarterly, replace annually",
        },
        "hose_aging": {
            "key_de": "Schlauchalterung",
            "embrittlement_timeline": "7-10 years typical service life",
            "failure_mechanism": "Plasticizer migration, UV degradation, ozone attack",
            "flexibility_loss": "Gradual stiffening makes failure more likely",
            "inspection_frequency": "Annual visual and tactile inspection",
            "replacement_schedule": "Every 10 years mandatory",
            "failure_consequence": "Rapid flooding if hose fails below waterline",
        },
        "clamp_failure_cascade": {
            "key_de": "Versagenskaskade",
            "initial_failure": "Single clamp corrosion or loosening",
            "water_egress": "Micro-leaking begins",
            "timeline": "Hours to minutes for catastrophic failure",
            "damage_rate": "Flooding possible within minutes",
            "prevention": "Redundant clamps, annual inspection, spare clamps aboard",
            "emergency_response": "Wooden plugs tapered to fit hose diameter",
        },
        "hose_material_options": {
            "nitrile_rubber": {
                "standard": "SAE J30R9 (ISO 1402)",
                "salt_water_rating": "Good",
                "flexibility": "Excellent at low temperatures",
                "UV_resistance": "Moderate - needs protection",
                "cost": "Low to moderate",
                "lifespan": "8-10 years",
            },
            "epdm_rubber": {
                "standard": "ISO 6072",
                "salt_water_rating": "Excellent",
                "flexibility": "Good",
                "UV_resistance": "Superior",
                "cost": "Moderate",
                "lifespan": "10-15 years",
            },
            "reinforced_pvc": {
                "standard": "Various manufacturers",
                "salt_water_rating": "Fair to good",
                "permeability": "Allows odor penetration",
                "UV_resistance": "Moderate",
                "cost": "Low",
                "lifespan": "5-8 years",
                "note": "Avoid for sanitation hoses"
            },
        },
    },
}


# ============================================================================
# TOILET DATABASE: Types, Systems, & Maintenance
# ============================================================================

TOILET_DATABASE: Dict[str, Any] = {
    "types": {
        "manual_simple": {
            "key_de": "Manuelle einfache Toilette",
            "mechanism": "Mechanical pump with seacock valve",
            "power_requirement": "Zero - human-powered",
            "water_usage": "3-5 gallons per flush",
            "advantages": [
                "Ultra-reliable",
                "No electrical dependency",
                "Simple maintenance",
                "Inexpensive"
            ],
            "disadvantages": [
                "Physical effort required",
                "Single point failure: siphon break valve",
                "Slower than powered options"
            ],
            "manufacturers": ["Jabsco", "Taylor Made", "ITT"],
            "typical_cost": "$300-$600",
        },
        "electric_macerating": {
            "key_de": "Elektrische Zerkleinerungtoilette",
            "mechanism": "Electric pump pulverizes waste before pumping",
            "power_consumption": "3-7 amperes at 12V DC",
            "water_usage": "0.5-1.5 gallons per flush (energy efficient)",
            "advantages": [
                "Low water consumption",
                "Quiet operation",
                "Can run through smaller hoses",
                "Automatic operation",
                "Good for multiple heads"
            ],
            "disadvantages": [
                "Electrical dependency",
                "More complex mechanism",
                "Potential clogging from non-biodegradable materials",
                "Noxious fumes if clogged"
            ],
            "critical_wire_gauge": {
                "description": "Wire sizing critical due to 3-7A draw",
                "rule": "ABYC E-11 guidance: <10ft = 10 AWG, 10-15ft = 8 AWG, >15ft = 6 AWG",
                "voltage_drop": "3% maximum for critical circuits",
            },
            "manufacturers": ["Raritan", "Dometic", "SPX Johnson"],
            "typical_cost": "$1,200-$2,500",
            "experience_note": "Macerating systems work well for boats with multiple heads and limited water"
        },
        "vacuum_system": {
            "key_de": "Vakuumtoilette",
            "mechanism": "Vacuum pulls waste through system using only 2 pints per flush",
            "power_requirement": "Central vacuum pump (5-10A)",
            "water_usage": "1 pint fresh + 1 pint sea water per flush",
            "advantages": [
                "Minimal water consumption ideal for cruising",
                "Compact holding tank requirements",
                "Excellent for extended passages",
                "Odor-free operation when functioning correctly",
                "EPA compliant"
            ],
            "disadvantages": [
                "Complex system requiring maintenance expertise",
                "Central pump failure disables all heads",
                "Higher initial cost",
                "Requires sealed plumbing system"
            ],
            "manufacturers": ["Dometic Vacu-Flush", "SPX Johnson"],
            "typical_cost": "$3,500-$6,000 (full system)",
            "maintenance_requirement": "Annual professional servicing recommended",
        },
        "composting_toilet": {
            "key_de": "Komposttoilette",
            "mechanism": "Separates liquid and solid waste, biological decomposition",
            "power_requirement": "Optional fan (low draw), zero required",
            "water_usage": "None",
            "advantages": [
                "Zero plumbing requirements",
                "Ecological - no discharge",
                "Works when sitting idle",
                "Low maintenance",
                "Suitable for anchoring indefinitely"
            ],
            "disadvantages": [
                "Requires manual emptying of solids",
                "Limited to small crews",
                "Not suitable for high-traffic situations",
                "Social acceptance issues"
            ],
            "manufacturers": ["Nature's Head", "Separett", "Biolet"],
            "typical_cost": "$1,000-$2,000",
            "use_case": "Solo sailors, minimal crew, extended anchoring",
            "notes": "Nature's Head has excellent reviews for reliability and ease of use"
        },
    },
    "sanitation_hose": {
        "key_de": "Abwasserschlauch",
        "pvc_standard": {
            "description": "Standard reinforced PVC hose",
            "permeability_issue": "PVC permeates odor molecules through wall material",
            "smell_problem": "Odor permeation increases with temperature and age",
            "cost": "Low (~$2/foot)",
            "recommended_use": "Suction lines only, NOT discharge lines",
            "warning": "Causes persistent galley/cabin odors on sailboats"
        },
        "saniflex_advanced": {
            "key_de": "Saniflex Premium Schlauch",
            "manufacturer": "Raritan",
            "odor_resistance": "15x more resistant than standard PVC",
            "barrier_layer": "Multi-wall construction with odor barrier",
            "flexibility": "Remains flexible throughout service life",
            "temperature_range": "-10°C to +60°C",
            "advantages": [
                "Minimal odor permeation",
                "Superior durability",
                "Better resistance to waste degradation",
                "Maintains flexibility"
            ],
            "cost": "Premium (~$8-12/foot)",
            "lifespan": "12-15 years typical",
            "recommended": "All discharge lines, especially in galley area",
            "notes": "Worth premium cost for cruising comfort"
        },
        "replacement_schedule": {
            "key_de": "Austauschplan",
            "interval": "8-10 years for discharge hoses",
            "accelerators": [
                "High ambient temperature",
                "Direct sunlight exposure",
                "Biological growth inside hose",
                "Chemical incompatibility with waste"
            ],
            "inspection_test": "Wrap hot damp cloth around hose, smell after 30 seconds",
            "positive_test": "If odor noticeably increases through hose wall, replacement needed",
        },
    },
    "manufacturers": {
        "jabsco": {
            "key_de": "Jabsco",
            "known_for": "Reliable manual and electric toilets",
            "reputation": "Industry standard for marine sanitation",
            "product_range": "Manual, electric, vacuum, diaphragm pumps",
            "reliability": "High",
            "spare_parts_availability": "Excellent globally",
            "typical_models": ["Quiet Flush", "Cruise Air", "Electra Flush"]
        },
        "raritan": {
            "key_de": "Raritan",
            "known_for": "Premium sanitation systems and hoses",
            "reputation": "High-end marine toilets and waste systems",
            "product_range": "Macerating, vacuum, holding tanks, treatment chemicals",
            "innovation": "Saniflex hose technology, advanced waste treatment",
            "reliability": "High",
            "typical_models": ["Atlantes", "PH", "PhII", "Crown"]
        },
        "nature_s_head": {
            "key_de": "Nature's Head",
            "known_for": "Composting toilet",
            "reputation": "Excellent reliability and user satisfaction",
            "user_experience": "Low odor, simple operation, easy maintenance",
            "lifespan": "20+ years with proper care",
            "support": "Good community, excellent documentation",
            "cost_effectiveness": "High - no plumbing required"
        },
    },
}


# ============================================================================
# GAS INSTALLATION DATABASE: LPG/CNG Systems & Safety
# ============================================================================

GAS_INSTALLATION_DATABASE: Dict[str, Any] = {
    "locker": {
        "key_de": "Gasflaschenschrank",
        "primary_requirement": "Vapor-tight enclosure to prevent interior contamination",
        "secondary_requirement": "Ventilation to exterior to prevent vapor buildup",
        "location_specification": "Lowest point of locker must be able to drain overboard",
        "drain_requirement": "Above waterline, minimum 1/4 inch diameter",
        "construction": {
            "material": "Marine plywood or fiberglass",
            "seal_standard": "Vapor-tight - no gaps larger than 1mm",
            "door": "Self-closing, latch-securing",
            "ventilation_port": "Deck-stepped, through hull, screened"
        },
        "ventilation_system": {
            "description": "Natural convection ventilation outboard",
            "intake": "Below deck mounted locker",
            "exhaust": "Above deck through through-hull",
            "diameter": "Minimum 1.5 inch hose",
            "protection": "Screen to prevent insect/debris entry"
        },
        "safety_features": {
            "isolation_valve": "Solenoid shutoff accessible from galley",
            "manual_shutoff": "Separate manual ball valve for isolation",
            "pressure_relief": "Built into regulator assembly",
            "redundancy": "Two independent shut-off methods"
        },
        "regulatory_compliance": {
            "standard": "ISO 9094 Part 1 (vessels ≤15m)",
            "reference": "ABYC H-33 (LPG systems)",
            "ce_directive": "2013/53/EU Recreational Craft"
        },
    },
    "piping": {
        "key_de": "Gasleitungen",
        "material_requirements": {
            "copper": {
                "specification": "Soft copper tubing, UN 12285",
                "diameter": "Properly sized for flow rate",
                "advantages": ["Corrosion resistant", "Easy to bend", "Standard practice"],
                "installation": "Must be protected from mechanical damage"
            },
            "stainless_steel": {
                "specification": "316 seamless tubing",
                "advantages": ["Superior corrosion resistance", "Strong"],
                "difficulty": "Harder to work with, requires special tools",
                "cost": "More expensive than copper"
            },
            "prohibited_materials": {
                "rubber": {
                    "reason": "NEVER use rubber hose for LPG lines",
                    "risk": "Gas permeates through rubber over time",
                    "consequence": "Uncontrolled gas leakage into cabin",
                    "exception": "Short flex connections with integral fittings only"
                },
                "aluminum": {
                    "reason": "Reacts with LPG and moisture",
                    "risk": "Corrosion and structural failure"
                }
            }
        },
        "routing_requirements": {
            "run_high_above_bilge": {
                "rule": "All piping runs must be well above bilge water level",
                "reason": "Prevents water accumulation and corrosion",
                "minimum_height": "Highest anticipated bilge water level + 6 inches"
            },
            "protection": "All piping runs protected from mechanical damage",
            "support": "Secured with clips every 12-18 inches",
            "installation": "No sharp bends, minimum bend radius 3x tubing diameter",
            "valve_access": "All shutoff valves easily accessible for emergency operation"
        },
        "connections": {
            "flare_fittings": {
                "type": "37-degree flare fitting (SAE J518)",
                "sealing": "Metal-to-metal seal, no thread sealant needed",
                "torque": "12-18 Nm depending on size",
                "inspection": "Check quarterly for weeping"
            },
            "integral_fittings": {
                "type": "Soldered or welded connections",
                "strength": "Superior to flare fittings",
                "requirement": "Professional installation mandatory"
            }
        },
    },
    "detector": {
        "key_de": "Gasdetektor",
        "location_critical": "Must be mounted at lowest bilge point",
        "reason_lpg_heavy": "LPG is heavier than air and pools in lowest areas",
        "consequence_wrong_location": "Ceiling-mounted detector will miss dangerous vapor buildup",
        "detector_type": "Catalytic bead sensor for LPG vapor",
        "specifications": {
            "sensitivity": "Alarm threshold typically 25% LEL (Lower Explosive Limit)",
            "response_time": "30 seconds or less to 50% LEL",
            "power": "Hardwired to 12V DC with battery backup",
            "alarm": "Audible alarm minimum 85 dB at 1 meter"
        },
        "wiring": {
            "wire_gauge": "ABYC E-11 sizing (12V DC, 3% voltage drop)",
            "circuit_protection": "2A fuse in dedicated circuit",
            "installation": "Professional electrician recommended"
        },
        "maintenance": {
            "calibration": "Annual by manufacturer or certified technician",
            "sensor_life": "3-5 years typical, replace per manufacturer",
            "test_function": "Monthly functional test with test gas"
        },
        "integration": {
            "safety_solenoid": "Detector should trigger solenoid shutoff on high alarm",
            "backup_alarm": "Independent audible alarm with battery backup"
        },
    },
    "thermoelectric_safety": {
        "key_de": "Thermoelement Sicherheit",
        "critical_importance": "Thermocouple stops gas flow if burner flame is extinguished",
        "function": {
            "principle": "Flame heats thermocouple generating micro-voltage",
            "voltage_generation": "Approximately 25mV when properly heated",
            "solenoid_operation": "Micro-voltage holds solenoid valve open",
            "failure_mode": "Flame out = no voltage = solenoid closes = gas shutoff"
        },
        "safety_significance": {
            "risk_prevented": "Unburned gas escaping into cabin if burner blows out",
            "scenarios": ["Wave knockdown extinguishing stove", "Wind blowing out pilot light", "Burner clogging"]
        },
        "maintenance_critical": {
            "inspection": "Monthly - verify flame reaches thermocouple",
            "cleaning": "Remove carbon buildup from thermocouple tip",
            "testing": "Light burner, blow out flame, verify solenoid closes",
            "replacement": "If solenoid doesn't close within 30 seconds, replace thermocouple"
        },
        "gimbal_stove_consideration": {
            "note": "Gimbaled stoves require special attention",
            "risk": "Flexible connections can kink, restricting gas flow",
            "mitigation": "Use reinforced flex tubing, minimize bends",
            "maintenance": "More frequent inspection of flex connections"
        },
    },
    "solenoid_shutoff": {
        "key_de": "Magnetventil Abschaltung",
        "manual_control": "Accessible button/switch in galley for emergency shutoff",
        "automatic_triggers": [
            "High LPG detection alarm",
            "Thermocouple flame-out signal from stove",
            "Optional: Timer for unattended operation"
        ],
        "specifications": {
            "response_time": "Less than 100 milliseconds",
            "seal_quality": "Must shut off completely with zero leakage",
            "power_requirement": "12V DC nominal, 1 amp coil draw"
        },
        "testing": {
            "frequency": "Monthly",
            "procedure": "Activate shutoff, verify gas supply stops at stove",
            "restoration": "Manual reset after alarm event"
        },
    },
}


# ============================================================================
# INTERIOR DATABASE: Wood, Materials, Joinery, Upholstery
# ============================================================================

INTERIOR_DATABASE: Dict[str, Any] = {
    "wood_materials": {
        "key_de": "Holzmaterialien",
        "teak": {
            "key_de": "Teakholz",
            "botanical_name": "Tectona grandis",
            "origin": "Tropical hardwood from Southeast Asia",
            "characteristics": {
                "hardness": "Janka hardness 1000-1280",
                "density": "0.6-0.75 g/cm³",
                "color": "Golden brown maturing to silver-grey",
                "grain": "Straight to wavy, distinctive appearance"
            },
            "marine_properties": {
                "durability": "Exceptional 20-30+ years exterior",
                "rot_resistance": "Natural oils provide excellent rot protection",
                "water_repellent": "High natural oil content minimizes absorption",
                "workability": "Easy to work, bends well, glues easily"
            },
            "applications": ["Trim", "Cabin sole", "Exterior rails", "Deck covering"],
            "maintenance": {
                "frequency": "Annual to bi-annual brightening",
                "process": "Clean, lightly sand, apply teak oil or finish",
                "labor_intensive": "Significant ongoing maintenance required",
                "cost": "Moderate maintenance, high material cost"
            },
            "drawback": "Tropical timber sustainability concerns",
            "cost_classification": "Premium",
        },
        "oak": {
            "key_de": "Eichenholz",
            "type": "Hardwood from temperate regions",
            "characteristics": {
                "hardness": "Janka hardness 1290",
                "density": "0.75-0.9 g/cm³",
                "color": "Light tan to medium brown",
                "grain": "Bold ray fleck pattern"
            },
            "marine_issues": {
                "tannin_content": "High tannins can react with moisture and metal fittings",
                "water_absorption": "Higher than teak, requires protection",
                "galvanic_reaction": "Tannins accelerate corrosion of steel fasteners",
                "rot_susceptibility": "More vulnerable than teak without protection"
            },
            "applications": [
                "Structural beams",
                "Cabin joinery",
                "Furniture frames",
                "High-visibility trim"
            ],
            "requirements": [
                "Excellent finish maintenance",
                "Stainless steel fasteners mandatory",
                "Regular oil/varnish reapplication",
                "Elevated bilge monitoring"
            ],
            "cost_classification": "Moderate to premium",
        },
        "mahogany": {
            "key_de": "Mahagoniholz",
            "botanical_name": "Swietenia macrophylla (true mahogany)",
            "characteristics": {
                "hardness": "Janka hardness 800-900",
                "density": "0.55-0.65 g/cm³",
                "color": "Reddish-brown, darkens with age",
                "grain": "Straight, uniform, attractive appearance"
            },
            "marine_advantages": {
                "durability": "15-20+ years with maintenance",
                "workability": "Excellent, machines cleanly",
                "appearance": "Highly valued for traditional yacht interiors",
                "stability": "Good dimensional stability"
            },
            "maintenance": [
                "Annual brightening and oiling",
                "Varnish recoating every 2-3 years",
                "More moderate than teak"
            ],
            "applications": [
                "Cabin paneling",
                "Cabin joinery",
                "Doors and trim",
                "Furniture construction"
            ],
            "cost_classification": "Premium",
            "sustainability_note": "Prefer sustainably harvested sources"
        },
        "marine_plywood": {
            "key_de": "Marinesperrholz",
            "standard_bs_1088": {
                "specification": "British Standard 1088 - marine grade plywood",
                "face_veneer": "Minimum 1mm thickness for durability",
                "core_veneers": "Hardwood species with specified gap limits",
                "adhesive": "Exterior-grade phenol-formaldehyde (phenolic)",
                "void_limitation": "Maximum gap specification between core veneers"
            },
            "preferred_species": [
                "Okoume (African hardwood, excellent rot resistance)",
                "Meranti (Southeast Asian, good durability)",
                "Avoid: Softwood cores which delaminate easily"
            ],
            "quality_grading": {
                "bruynzeel_premium": {
                    "description": "Dutch manufacturer producing premium marine plywood",
                    "face_veneer": ">1mm thickness for maximum durability",
                    "core_quality": "Strict void control, hardwood only",
                    "adhesive": "Waterproof phenolic glue",
                    "reputation": "Industry standard for high-quality yacht interiors",
                    "cost": "Premium but justified for longevity"
                },
                "standard_bs1088": {
                    "meets_specification": "Acceptable for marine use",
                    "cost": "Lower than premium brands",
                    "caution": "Verify core species and veneer thickness"
                }
            },
            "applications": [
                "Cabin sole underlayment",
                "Structural bulkheads",
                "Joinery backing",
                "High-quality interior construction"
            ],
            "installation": "Seal all edges with epoxy or waterproof finish",
        },
        "mdf_disaster": {
            "key_de": "MDF - Katastrophe",
            "material": "Medium Density Fiberboard",
            "marine_catastrophe": "IRREVERSIBLE SWELLING when exposed to moisture",
            "failure_mechanism": {
                "water_absorption": "Wood fibers absorb water and swell permanently",
                "adhesive_failure": "Glue between fibers breaks down in salt/moisture environment",
                "delamination": "Fibers separate, creating gaps and weakness",
                "structural_collapse": "Loses all structural integrity"
            },
            "timeline": {
                "condensation_exposure": "Visible swelling within weeks",
                "high_humidity": "Damage accelerates with elevated moisture",
                "bilge_water": "Complete structural failure within months"
            },
            "consequences": [
                "Distorted joinery",
                "Weakened structural elements",
                "Cabinet failures",
                "Mold proliferation in swollen material",
                "Toxic off-gassing as glues fail"
            ],
            "recommendation": "NEVER use MDF in marine environments",
            "if_encountered": "Plan replacement with proper marine plywood",
        },
        "chipboard_builders_mistake": {
            "key_de": "Sperrholzfehlgriff",
            "material": "Particle board / chip board",
            "builder_justification": "Low cost, easy to work with",
            "marine_reality": "Unsuitable despite continued use by serial builders",
            "failure_characteristics": {
                "water_sensitivity": "Extreme water absorption",
                "strength_loss": "Loses structural strength when wet",
                "particle_separation": "Particles separate in moisture",
                "irreversible": "Swelling and degradation are permanent"
            },
            "problem_timeline": {
                "initial": "Hidden interior use by cost-conscious builders",
                "discovery": "Problems emerge after first year of tropical cruising",
                "consequence": "Significant repair costs during warranty period"
            },
            "inspection_points": [
                "Check under cabin sole cushions",
                "Inspect interior wall backing",
                "Look behind galley and cabin furniture",
                "Check structural bulkhead cores"
            ],
            "warranty_issue": "Many builders deny this is their fault",
            "replacement_cost": "Significant - budget $5,000+ for major replacement",
        },
    },
    "joinery": {
        "key_de": "Zimmerei und Verbindungen",
        "dowel_joints": {
            "key_de": "Dübel Verbindungen",
            "strength": "Strongest wood-to-wood joinery method",
            "mechanism": "Dowels cross-grain, creating primary shear resistance",
            "sizing": {
                "diameter": "1/3 material thickness typical",
                "length": "1.5x diameter, minimum 1 inch",
                "spacing": "3-4 inches center-to-center"
            },
            "advantages": [
                "Excellent strength",
                "Water-resistant when glued properly",
                "Works with all wood species",
                "Hidden within joint"
            ],
            "disadvantages": [
                "Time-consuming to drill accurately",
                "Requires precision jigs",
                "Difficult to adjust if holes are slightly off"
            ],
            "marine_suitability": "Excellent for structural joinery",
            "adhesive": "Epoxy or waterproof polyurethane",
        },
        "biscuit_joints": {
            "key_de": "Feder Verbindungen",
            "strength": "Moderate - primarily for alignment",
            "mechanism": "Compressed hardwood biscuits align two pieces during glue-up",
            "biscuit_types": {
                "size_0": "0.75 x 1.125 x 2.125 inches",
                "size_10": "1 x 1.625 x 2.375 inches (most common)",
                "size_20": "1.25 x 1.875 x 2.75 inches (cabinetry)"
            },
            "primary_purpose": "Alignment only - not primary load-bearing",
            "advantages": [
                "Quick alignment during assembly",
                "Minimal setup time",
                "Easy to execute"
            ],
            "disadvantages": [
                "Cannot carry heavy loads",
                "Biscuits expand/contract with moisture",
                "Not suitable for primary structural joinery"
            ],
            "marine_limitation": "Use only for non-critical joinery",
            "adhesive": "Must be waterproof when used in marine environment",
        },
        "pocket_screws": {
            "key_de": "Tasche Schraubenverbindungen",
            "mechanism": "Screws driven at angle from pocket hole into edge of adjoining piece",
            "strength": "Good for cabinet construction, adequate for interior furniture",
            "advantages": [
                "Fast assembly (ikea-style furniture)",
                "No visible fasteners on face",
                "Allows disassembly for service",
                "Works with various wood species"
            ],
            "disadvantages": [
                "Lower strength than dowels",
                "Requires pocket hole jig",
                "Screws can loosen over time with vibration",
                "Not suitable for structural elements"
            ],
            "marine_considerations": {
                "fasteners": "Stainless steel pan-head screws mandatory",
                "tightening": "Check quarterly for loosening",
                "moisture": "Holes can accumulate bilge water if not sealed"
            },
            "applications": ["Cabinet construction", "Furniture frames", "Non-structural trim"],
        },
        "adhesives": {
            "key_de": "Holzklebstoffe",
            "epoxy": {
                "type": "Two-part epoxy resin + hardener",
                "waterproofing": "Excellent - fully waterproof joint",
                "rigidity": "Creates rigid joint, minimal flex",
                "gap_filling": "Good gap-filling properties (up to 1/8 inch)",
                "cure_time": "Slow - 24 hours typical",
                "mixing": "Must follow exact ratio for proper cure",
                "advantages": [
                    "Superior waterproofing",
                    "Excellent strength",
                    "Works on oily woods (teak)",
                    "Gap-filling ability"
                ],
                "disadvantages": [
                    "Slow cure time",
                    "Requires careful mixing",
                    "Difficult to remove excess",
                    "Can crack under extreme stress"
                ],
                "marine_recommendation": "Best choice for structural joinery",
            },
            "polyurethane": {
                "type": "Moisture-cured polyurethane",
                "waterproofing": "Excellent - fully waterproof",
                "flexibility": "Creates slightly flexible joint (better for movement)",
                "cure_time": "24-48 hours",
                "application": "Requires slightly damp surfaces for activation",
                "advantages": [
                    "Superior waterproofing",
                    "Better flex than epoxy",
                    "Excellent for teak",
                    "Automatic activation (no mixing)"
                ],
                "disadvantages": [
                    "Messier application (foams slightly)",
                    "Requires moisture to cure properly",
                    "More expensive than epoxy"
                ],
                "marine_ideal_use": "Best for flexible joinery in high-movement areas",
            },
            "pva_polyvinyl_acetate": {
                "type": "Common yellow wood glue (Titebond, Elmer's)",
                "waterproofing": "NOT waterproof - dissolves in standing water",
                "marine_suitability": "Inadequate for marine joinery",
                "consequence": "Joint failure when exposed to moisture/humidity",
                "use_case": "Interior furniture only - not recommended for boats",
                "failure_timeline": "6-12 months in marine environment",
            },
        },
    },
    "furniture_attachment": {
        "key_de": "Möbelbefestigung",
        "flexible_interface": {
            "concept": "Furniture must flex independently from hull structure",
            "reason": "Hull moves/flexes in waves, rigid furniture amplifies stress",
            "consequence": "Rigid attachment = accelerated failure and cracking"
        },
        "tabbing_method": {
            "key_de": "Glasfaser Tabbing",
            "technique": "Glass tape/cloth strips create flexible bond between furniture and hull",
            "material": "Fiberglass tape or cloth in resin",
            "application": {
                "width": "Laminate width 3-6 inches typical",
                "layers": "3-5 layers of tape for strength",
                "resin": "Epoxy or polyester resin system"
            },
            "flexibility": "Allows furniture to move slightly relative to hull",
            "strength": "Adequate for holding furniture in place",
            "reliability": "Proven method in yacht construction",
            "advantages": [
                "Distributes loads over wide area",
                "Allows micro-movement",
                "No hard attachment points",
                "Prevents stress concentration"
            ],
        },
        "fastener_approach": {
            "option": "Mechanical fastening through bulkheads to hull stringers",
            "materials": [
                "Stainless steel bolts with washers",
                "Backing plates to distribute load",
                "Bedding compound under all fasteners"
            ],
            "limitation": "Creates rigid connection - must allow some flex",
            "mitigation": "Use rubber isolation pads under fasteners",
        },
    },
    "upholstery": {
        "key_de": "Polsterung",
        "foam_types": {
            "cold_foam_marine": {
                "grades": "RG35 (light), RG40 (medium), RG50 (firm)",
                "description": "Open-cell polyurethane foam, marine-grade",
                "density": "35-50 kg/m³",
                "characteristics": {
                    "breathability": "Allows air circulation (prevents mold)",
                    "water_absorption": "Absorbs water but dries quickly",
                    "resilience": "Good recovery and comfort",
                    "durability": "8-10 years in marine environment"
                },
                "marine_advantages": [
                    "Breathable, prevents condensation buildup",
                    "Mold-resistant compared to closed-cell",
                    "Comfortable seating",
                    "Standard marine choice"
                ],
                "cleaning": "Sponge with fresh water, air dry thoroughly",
                "replacement_schedule": "Every 8-10 years for original comfort"
            },
            "closed_cell_issues": {
                "problem": "Traps moisture, promotes mold growth",
                "application": "Not recommended for cabin upholstery",
                "exception": "Okay for flotation (requires drainage/ventilation)"
            }
        },
        "mattress_ventilation": {
            "key_de": "Matratzen Belüftung",
            "critical_importance": "CRITICAL for mold prevention",
            "mechanism": {
                "issue": "Mattress between hull and cabin air traps condensation",
                "mold_risk": "High - perfect environment for biological growth",
                "consequence": "Mold odor, respiratory issues, material degradation"
            },
            "ventilation_solutions": [
                "Slatted mattress platform (improves airflow)",
                "Portable mattress vents (remove when sitting)",
                "Lifting/airing mattresses weekly on sunny days",
                "Running ventilation fans nightly if anchored",
                "Dehumidifier operation in high-humidity areas"
            ],
            "prevention_strategy": [
                "Ensure cabin air circulation",
                "Monitor humidity levels (maintain <60%)",
                "Allow mattress to air regularly",
                "Use moisture-absorbing products beneath mattress"
            ],
        },
        "fabric_selection": {
            "sunbrella": {
                "key_de": "Sunbrella Gewebe",
                "type": "Solution-dyed acrylic fiber",
                "characteristics": [
                    "Excellent UV resistance",
                    "High colorfastness",
                    "Mildew-resistant treatment",
                    "Water-resistant coating"
                ],
                "applications": ["Cushions", "Upholstery", "Exterior covers"],
                "durability": "10+ years outdoor service",
                "maintenance": "Soap/water cleaning",
                "cost": "Premium but justified",
            },
            "marine_vinyl": {
                "type": "PVC-based fabric with UV protection",
                "characteristics": [
                    "Waterproof surface",
                    "Easy to clean",
                    "Mildew resistant",
                    "Various colors/textures"
                ],
                "applications": ["Cabin cushions", "Bench seats", "High-moisture areas"],
                "durability": "7-10 years typical",
                "cleaning": "Wipe with damp cloth",
                "consideration": "Can feel clammy in humid conditions",
            },
            "natural_canvas": {
                "characteristic": "Absorbs moisture and mildew",
                "recommendation": "Not ideal for marine environments",
                "alternative": "Use Sunbrella or marine vinyl instead"
            }
        },
        "thread_specifications": {
            "v_92": {
                "specification": "Standard polyester thread",
                "strength": "Adequate for most upholstery",
                "uv_resistance": "Moderate",
                "application": "Interior cushions"
            },
            "v_138_heavy": {
                "specification": "Heavy-duty UV-resistant polyester",
                "strength": "Superior strength",
                "uv_resistance": "High - resists fading",
                "application": "Exterior cushions, exposed stitching",
                "recommendation": "Best for marine use"
            }
        },
    },
    "surfaces": {
        "key_de": "Oberflächenmaterialien",
        "corian_acrylic": {
            "type": "Solid surface acrylic composite",
            "characteristics": [
                "Seamless installation",
                "Wide color selection",
                "Warm to touch (unlike stone)",
                "Stain resistant"
            ],
            "advantage": "Repairable - small chips/scratches can be sanded out",
            "disadvantages": [
                "Can scorch from hot objects",
                "Scratches from sharp objects",
                "More expensive than laminate"
            ],
            "marine_suitability": "Good - especially for galley counters",
            "maintenance": "Clean with mild soap, avoid abrasive scrubbers",
            "repair": "Professional sanding restores minor damage"
        },
        "marine_plywood_surfaces": {
            "specification": "BS 1088 marine plywood for backing",
            "finish_options": [
                "Epoxy primer + polyurethane topcoat",
                "Bright varnish (6+ coats)",
                "Two-part polyurethane system"
            ],
            "durability": "15+ years with proper maintenance",
            "reparability": "Can refinish if damaged",
            "cost": "Moderate to high"
        },
        "hpl_laminate": {
            "type": "High-Pressure Laminate (Formica, Wilsonart)",
            "advantages": [
                "Inexpensive",
                "Wide design options",
                "Easy to clean",
                "Durable surface"
            ],
            "edge_problems": {
                "issue": "Unprotected edges absorb moisture",
                "consequence": "Core swelling and delamination",
                "solution": "All edges must have edge banding or trim"
            },
            "marine_consideration": "Acceptable if edges properly protected",
            "lifespan": "10-12 years with edge protection",
        },
        "teak_traditional": {
            "characteristic": "Classic marine interior finish",
            "appearance": "Golden brown, distinctive grain",
            "maintenance": [
                "Annual oiling or varnishing",
                "Labor-intensive upkeep",
                "Matures to silver-grey if untreated"
            ],
            "cost": "High material + high maintenance labor",
            "sustainability": "Consider FSC-certified sources"
        },
    },
}


# ============================================================================
# MOISTURE DATABASE: Condensation Control & Ventilation
# ============================================================================

MOISTURE_DATABASE: Dict[str, Any] = {
    "condensation": {
        "key_de": "Kondensation Kontrolle",
        "three_pillars": [
            "Heating - raise interior temperature above dew point",
            "Insulation - reduce cold surfaces where condensation occurs",
            "Ventilation - exchange moist interior air with drier exterior air"
        ],
        "root_cause": {
            "mechanism": "Warm moist interior air contacts cold hull surface",
            "dew_point": "Water vapor condenses when surface temperature drops below dew point",
            "tropical_risk": "High humidity + cool hull = severe condensation risk",
            "winter_risk": "Heating interior while hull remains cold creates differential"
        },
        "hull_insulation": {
            "key_de": "Rumpfisolation",
            "pu_foam_insulation": {
                "material": "Polyurethane foam spray or board",
                "thickness_thermal": "2cm thickness minimal thermal resistance",
                "thickness_condensation": "6-7cm optimal to prevent condensation",
                "advantage": "Superior insulation value per thickness",
                "disadvantage": "Difficult to repair if damaged",
                "installation": "Factory spray or fitted boards"
            },
            "armaflex_self_adhering": {
                "material": "Closed-cell elastomeric foam",
                "characteristics": [
                    "Self-adhering - no fasteners needed",
                    "Flexible - follows curves easily",
                    "Low thermal conductivity",
                    "Vapor barrier included"
                ],
                "thickness": "12-19mm typical",
                "advantages": [
                    "Retrofit-friendly",
                    "Works on existing hulls",
                    "Easy installation"
                ],
                "cost": "Moderate",
                "application": "Bilge area, engine room, high-moisture zones"
            },
            "mineral_wool": {
                "material": "Glass or rock wool batts",
                "fire_resistance": "Excellent - non-flammable",
                "thermal_performance": "Good insulation value",
                "moisture_issue": "Absorbs water if exposed to bilge water",
                "requirement": "Waterproof vapor barrier essential",
                "application": "Structural bulkheads, fire protection",
                "disadvantage": "Must never be exposed to bilge water"
            },
            "insulation_strategy": {
                "principle": "Insulate hull to keep interior surfaces warmer",
                "result": "Reduces condensation formation on surfaces",
                "supplementary": "Combined with heating and ventilation"
            }
        },
    },
    "ventilation": {
        "key_de": "Belüftung",
        "dorade_water_trap": {
            "key_de": "Dorade Wasserfalle",
            "design": "Cowl vent with internal baffle that traps water while allowing air passage",
            "function": [
                "Allows fresh air into cabin",
                "Prevents water entry in rough seas",
                "Allows air to exit cabin ventilation"
            ],
            "principle": "Water drops are heavier than air and fall to bottom of baffle",
            "dimensions": "Standard 3 inch, 4 inch, or 5 inch diameters",
            "placement": "Foredeck and aft cabin areas for cross-ventilation",
            "maintenance": [
                "Check for clogs (algae, spider webs)",
                "Rinse with fresh water annually",
                "Ensure internal baffle is intact"
            ],
            "effectiveness": "90%+ protection in normal conditions",
            "limitation": "Continuous boarding seas can overcome any vent",
        },
        "solar_ventilation_fans": {
            "key_de": "Solarbelüftungsventilatoren",
            "purpose": "Maintain air circulation when boat is unattended",
            "power_source": "Small solar panel with battery or direct DC",
            "operation": "Runs continuously during daylight hours",
            "benefit": "Prevents moisture accumulation in unoccupied boat",
            "effectiveness": "Reduces mold, mildew, and odor significantly",
            "installation": [
                "Cabin top mounted",
                "Through-hull with duct",
                "Battery-powered option available"
            ],
            "cost": "$200-$400 installed",
            "maintenance": "Annual inspection, clean solar panel",
            "value": "Highly recommended for boats that sit unoccupied"
        },
        "forced_ventilation": {
            "key_de": "Erzwungene Belüftung",
            "application": "Engine room, galley, head areas",
            "exhaust_fans": {
                "location": "Mount in cabin top or through hull",
                "function": "Extract moist/odorous air from interior",
                "power": "12V DC or 110V AC depending on installation",
                "capacity": "Sized based on cabin volume",
                "control": "Manual switch or auto humidity sensor"
            },
            "intake_fans": {
                "location": "Opposite side of cabin from exhaust",
                "function": "Positive pressure pulls fresh air inboard",
                "balance": "Supply = exhaust for stable pressure"
            },
            "timing": "Run nightly while anchored to exchange interior air",
            "desiccant_system": {
                "alternative": "Rechargeable desiccant canisters in cabin",
                "use_case": "Supplement mechanical ventilation",
                "maintenance": "Recharge weekly by solar heat or oven"
            }
        },
    },
}


# ============================================================================
# FIRE SAFETY DATABASE: Extinguishers, Suppression, Standards
# ============================================================================

FIRE_SAFETY_DATABASE: Dict[str, Any] = {
    "extinguishers": {
        "key_de": "Feuerlöscher",
        "fire_classes": {
            "class_a": "Ordinary combustibles (wood, paper, fabric)",
            "class_b": "Flammable liquids (fuel, oil, paint)",
            "class_c": "Electrical equipment fires",
            "class_d": "Combustible metals (rare on boats)",
            "class_k": "Commercial cooking oil (galley fires)"
        },
        "dry_chemical_multiclass": {
            "key_de": "Trockenlöschmittel",
            "type": "Dry chemical powder (ABC or B+C rating)",
            "composition": [
                "Monoammonium phosphate (ABC multi-purpose)",
                "Potassium chloride (B+C marine standard)"
            ],
            "marine_standard": "Class B+C dry chemical most common",
            "fire_suppression": "Interrupts combustion chain reaction",
            "effectiveness": "Excellent for fuel/electrical fires",
            "disadvantages": [
                "Corrosive powder residue",
                "Requires cleanup after use",
                "Visibility reduced by powder cloud",
                "Not for lithium battery fires"
            ],
            "capacity": "2-5 lb canisters typical on boats",
            "placement": "Galley, engine room, electrical panel areas",
            "inspection": "Monthly pressure check, replace if needle drops",
            "expiration": "10-12 years typical service life",
        },
        "abc_multipurpose": {
            "type": "Multi-purpose dry chemical",
            "rating": "Effective on A, B, and C fires",
            "composition": "Ammonium polyphosphate-based",
            "advantage": "Single extinguisher covers most shipboard fires",
            "disadvantage": "Slightly less effective on pure B fires than specialized B+C",
            "cost": "Lower than specialized types",
        },
        "lithium_fire_crisis": {
            "key_de": "Lithium-Batterie Brände",
            "crisis": "Lithium battery fires are revolution in marine safety",
            "conventional_ineffective": "Standard dry chemical extinguishers FAIL on lithium fires",
            "mechanism": [
                "Lithium fires reach extreme temperatures (1000°C+)",
                "Lithium compounds are oxidizers - burn without oxygen",
                "Standard extinguishers cannot suppress the reaction",
                "Fire reignites after apparent suppression"
            ],
            "required_technology": "AVD (Aqueous Vermiculite Dispersion)",
            "avd_mechanism": {
                "principle": "Vermiculite particles coat lithium battery and cool effectively",
                "cooling": "Massive heat absorption cools below lithium ignition temperature",
                "oxygen_exclusion": "Particles coat battery excluding residual oxygen",
                "success_rate": "95%+ suppression of lithium fires"
            },
            "lith_ex_brand": {
                "manufacturer": "Lith-Ex Ltd (UK)",
                "product": "Lith-Ex fire suppressant aerosol",
                "size": "300ml aerosol can",
                "effectiveness": "Proven suppression of large lithium battery fires",
                "cost": "$200-$300 per can",
                "requirement": "At least one per major lithium battery installation"
            },
            "installation": "Near all lithium battery banks",
            "crew_training": "Everyone must understand lithium fire risks",
            "emergency_procedure": [
                "Identify lithium fire (unusual color, extreme heat)",
                "Evacuate non-essential crew",
                "Use Lith-Ex AVD product",
                "If ineffective, abandon and alert rescue services"
            ],
            "monitoring": "Lithium battery BMS should prevent fires through temperature/voltage management"
        },
        "automatic_engine_room": {
            "key_de": "Automatische Motorraum Suppression",
            "system_type": "Fixed gaseous suppression system (CO2 or Halon replacement)",
            "function": "Automatically detects engine room fire and discharges suppressant",
            "detection_methods": [
                "Flame detector (optical sensor)",
                "Smoke detector (ionization/photoelectric)",
                "Temperature switch (thermal release)"
            ],
            "suppressants": {
                "co2": {
                    "type": "Carbon dioxide gas",
                    "effectiveness": "Excellent engine room suppression",
                    "risk": "Asphyxiation hazard - crew evacuation required",
                    "warning": "Loud alarm and solenoid activation before discharge"
                },
                "novec_1230": {
                    "type": "Hydrofluoroolefin (EPA approved Halon replacement)",
                    "effectiveness": "Excellent suppression with low residue",
                    "risk": "Much safer than CO2 - lower toxicity",
                    "application": "Modern luxury yachts standard"
                }
            },
            "automatic_shutdown": {
                "integration": "Fire detection triggers engine fuel shutoff",
                "manual_override": "Crew can shut down manually if early detection"
            },
            "discharge_zones": "Engine room sealed, crew evacuated before discharge",
            "maintenance": "Annual professional inspection and certification",
            "regulatory": "Mandatory on yachts >15m with enclosed engine rooms"
        },
    },
    "iso_9094": {
        "key_de": "ISO 9094 Brandschutz",
        "scope": "Fire protection requirements for recreational craft",
        "parts": {
            "part_1": {
                "title": "Fire Protection for Small Boats ≤15m",
                "requirements": [
                    "Fire extinguisher minimum 2x 2kg or 1x 4kg",
                    "Fire-retardant materials in cabin",
                    "Fuel system safety",
                    "Stove installation and testing"
                ],
                "enforcement": "CE marking requirement"
            },
            "part_2": {
                "title": "Fire Protection for Large Boats >15m",
                "requirements": [
                    "Multiple fire extinguishers (based on vessel size/layout)",
                    "Automatic sprinkler system or fire detection in accommodation",
                    "Mandatory fixed fire suppression in engine room",
                    "Fire-retardant materials specification",
                    "High-standard fuel/stove installation",
                    "Structural fire protection (bulkheads, ceiling)"
                ],
                "engine_room": "Fixed suppression system mandatory (CO2 or alternative)",
                "accommodation": "Either auto sprinklers or detection + manual extinguishers",
                "enforcement": "CE marking requirement"
            }
        },
        "ce_directive_2013_53_eu": {
            "applicability": "Recreational Craft Directive for EU-built/imported boats",
            "categories": {
                "category_a": "Ocean - unlimited range",
                "category_b": "Offshore - limited range in restricted waters",
                "category_c": "Inshore - protected waters within 20nm of shore",
                "category_d": "Sheltered - lakes, rivers, protected harbors"
            },
            "fire_requirements": "ISO 9094 Part 1 or Part 2 depending on size",
            "compliance_documentation": "Technical file must be maintained",
            "enforcement": "Port state control inspections"
        }
    },
}


# ============================================================================
# LEAK DEFENSE DATABASE: Bilge Pumps, Plugs, Emergency Systems
# ============================================================================

LEAK_DEFENSE_DATABASE: Dict[str, Any] = {
    "bilge_pumps": {
        "key_de": "Lenzpumpen",
        "derating_factors": {
            "principle": "Stated GPH rating assumes ideal conditions",
            "real_world": "Field installation reduces capacity significantly",
            "hose_length": {
                "factor": "Each foot of hose reduces capacity 2-3%",
                "example": "30 feet of hose = 60-90% capacity loss"
            },
            "hose_diameter": {
                "factor": "Undersized hose creates severe restriction",
                "rule": "Use hose diameter no smaller than pump outlet",
                "pressure_drop": "Exponential increase with restriction"
            },
            "fittings": {
                "factor": "Each 90-degree elbow = 5-10% loss",
                "rule": "Use long-radius fittings, minimize elbows",
                "strainer": "Inlet strainer can cut capacity 30-40%"
            },
            "lift": {
                "factor": "Vertical rise reduces capacity significantly",
                "example": "6ft lift = 20% capacity reduction",
                "principle": "Pump must overcome water column weight"
            },
            "voltage_drop": {
                "factor": "Undersized wiring reduces motor voltage",
                "rule": "ABYC E-11: 3% voltage drop maximum",
                "consequence": "Motor draws more current at reduced voltage = stalling risk"
            },
            "calculation_example": {
                "rated": "2000 GPH at optimal conditions",
                "30ft_hose": "2000 - 600 (30% loss) = 1400 GPH",
                "elbows_4x": "1400 - 400 (10% loss) = 1000 GPH",
                "strainer": "1000 - 300 (30% loss) = 700 GPH",
                "reality": "700 GPH vs 2000 rated = 65% penalty"
            }
        },
        "staged_redundancy": {
            "principle": "Multiple independent pumps provide failsafe protection",
            "capacity_split": {
                "primary": "1000-2000 GPH electric pump",
                "secondary": "500-1000 GPH backup electric pump",
                "manual": "Manual diaphragm pump for emergency"
            },
            "independence": [
                "Separate through-hull strainers",
                "Independent discharge hoses",
                "Separate electrical circuits and switches",
                "Non-interconnected systems"
            ],
            "activation": {
                "primary": "Auto float switch activates when level rises",
                "secondary": "Manual operation or separate float switch",
                "manual": "Crew-operated for emergency backup"
            },
            "philosophy": "If one system fails, others continue protecting boat"
        },
        "independent_wiring": {
            "key_de": "Unabhängige Verdrahtung",
            "circuit_isolation": "Each pump on separate circuit with dedicated breaker",
            "battery_connection": "Direct connection to battery bypasses main switch",
            "wire_sizing": "ABYC E-11: 3% voltage drop for critical circuits",
            "switches": "Separate switches for each pump, all accessible",
            "consequence": "Single electrical failure cannot disable all pumping"
        },
        "independent_hoses": {
            "principle": "Separate intake/discharge prevents single point failure",
            "intake": "Each pump draws from lowest bilge point",
            "discharge": "Dedicated through-hull for each pump system",
            "advantage": "Single hose blockage doesn't affect other systems"
        },
        "abyc_dry_running": {
            "requirement": "Pump must run dry for 7+ hours without damage",
            "principle": "Bilge may empty with pump continuing operation",
            "pump_selection": "Specified marine pumps designed for dry running",
            "consequence": "Consumer-grade pumps fail with air induction"
        }
    },
    "float_switches": {
        "key_de": "Schwimmerventile",
        "automatic_activation": {
            "principle": "Float rises with water level, triggering switch at preset depth",
            "sensitivity": "Typically activates at 6-8 inches of bilge water",
            "advantage": "Removes human oversight - automatic protection 24/7"
        },
        "ultra_pumpswitch": {
            "manufacturer": "Ultra Industries (marine specialist)",
            "reliability": "Excellent track record for marine service",
            "design": "Sealed mercury switch (or modern solid-state) in float chamber",
            "activation": "Float mechanism operates mercury switch as water rises",
            "maintenance": "Minimal - check for debris/corrosion annually",
            "cost": "$50-$100 per switch"
        },
        "switch_reliability": {
            "failure_modes": [
                "Corrosion of switch contacts",
                "Float chamber leakage",
                "Debris jamming float movement",
                "Electrical contact failure"
            ],
            "mitigation": [
                "Stainless steel construction preference",
                "Annual inspection and cleaning",
                "Protection from debris (strainer)",
                "Testing by manual triggering monthly"
            ]
        }
    },
    "wooden_plugs": {
        "key_de": "Holzstöpsel Notfall",
        "construction": {
            "material": "Tapered softwood (pine or fir preferred)",
            "taper": "Gradual increase in diameter along length",
            "diameter": "Ranges 3/4 inch to 1.5 inches diameter",
            "length": "2-4 inches long",
            "edge": "Rounded - never sharp"
        },
        "operation": {
            "principle": "Wood swells when wet, creating watertight seal",
            "application": "Hammered into through-hull opening",
            "force": "Gentle to moderate - do not split wood",
            "seal_quality": "Effective for permanent emergency sealing",
            "durability": "Holds indefinitely until professional repair"
        },
        "quantity_rule": {
            "principle": "One plug per 10 feet of boat length",
            "example": "40ft boat = 4 plugs minimum",
            "location": "Taped near relevant through-hulls",
            "identification": "Label each plug with diameter to match through-hull"
        },
        "emergency_use": {
            "procedure": [
                "Identify leaking through-hull",
                "Match plug diameter to hole",
                "Place wooden plug over hole",
                "Hammer gently until water flow stops",
                "Monitor seal for stability",
                "Plan permanent repair within days"
            ]
        }
    },
    "emergency_crash_pump": {
        "key_de": "Notfall Crashpumpe",
        "principle": "Use engine seawater cooling pump as bilge pump in emergency",
        "procedure": [
            "Close seacock shutoff at through-hull inlet",
            "Disconnect seawater intake hose",
            "Lower free end of hose into bilge",
            "Restart engine to circulate seawater from bilge overboard",
            "Monitor bilge level until stable"
        ],
        "effectiveness": {
            "flow_rate": "Typical engine cooling pump 30-60 GPM",
            "duration": "Can run indefinitely while engine operates",
            "limitation": "Requires engine function - not option with engine failure"
        },
        "groco_safety_seacock": {
            "product": "Groco Safety Seacock Converter Kit",
            "function": "Allows isolation valve to select bilge or normal cooling flow",
            "valve_mechanism": "Three-way shutoff integrated in seacock",
            "operation": [
                "Normal position: engine cooling draw",
                "Bilge emergency: toggle valve to draw from bilge instead",
                "Both off: isolates sea from engine/bilge"
            ],
            "advantage": "Pre-configured system - faster deployment in emergency",
            "cost": "$200-$300 including installation"
        }
    },
}


# ============================================================================
# STABILITY DATABASE: CE Categories & Standards
# ============================================================================

STABILITY_DATABASE: Dict[str, Any] = {
    "ce_categories": {
        "key_de": "CE Kategorien",
        "category_a": {
            "key_de": "Ozean",
            "description": "Unlimited oceanic range",
            "sea_state": "Design conditions: severe and strong winds, high waves",
            "distance": "No distance restrictions",
            "typical_vessels": "Offshore cruising yachts, commercial vessels",
            "stability_requirement": "AVS minimum 100°",
        },
        "category_b": {
            "key_de": "Offshore",
            "description": "Offshore sheltered waters with limited range",
            "sea_state": "Design conditions: strong winds, high waves",
            "distance": "Typically 50-200nm from shelter",
            "typical_vessels": "Mediterranean cruisers, Caribbean offshore",
            "stability_requirement": "AVS minimum 95°"
        },
        "category_c": {
            "key_de": "Inshore",
            "description": "Inshore waters within proximity to shelter",
            "sea_state": "Moderate to strong winds, moderate waves",
            "distance": "Typically within 20nm of shelter",
            "typical_vessels": "Daysailers, weekend cruisers",
            "stability_requirement": "AVS minimum 90°"
        },
        "category_d": {
            "key_de": "Geschützt",
            "description": "Sheltered inland/coastal waters",
            "sea_state": "Light to moderate winds, small waves",
            "typical_waters": "Lakes, rivers, protected bays",
            "typical_vessels": "Pontoons, protected water boats",
            "stability_requirement": "AVS minimum 80°"
        }
    },
    "avs_angle_vanishing_stability": {
        "key_de": "AVS Winkel",
        "definition": "Angle at which boat loses ability to right itself",
        "measurement": "Heel angle where stability curve becomes negative",
        "category_minimums": {
            "category_a": "100 degrees minimum",
            "category_b": "95 degrees minimum",
            "category_c": "90 degrees minimum",
            "category_d": "80 degrees minimum"
        },
        "significance": {
            "principle": "Larger AVS = boat more resistant to capsize",
            "safety_margin": "Category A boats can tolerate 100° heel without capsizing",
            "design_challenge": "Wide, light boats have smaller AVS"
        },
        "testing": {
            "method": "Inclination experiment measuring righting moment at various angles",
            "procedure": "Weights moved across beam, heel angle measured",
            "calculation": "Righting moment plotted against heel angle",
            "failure_point": "Angle where righting moment becomes negative"
        }
    },
    "stix_stability_index": {
        "key_de": "STIX Stabilitätsindex",
        "scale": "0-50 scale, higher is better",
        "interpretation": [
            "STIX 5-10: Very beamy, stiff boats (trawler-style)",
            "STIX 15-25: Moderate stability (typical cruisers)",
            "STIX 25-40: Good stability (traditional designs)",
            "STIX 40-50: Exceptional stability (narrow, deep designs)"
        ],
        "designer_tool": "Used early in design to evaluate concept stability",
        "simplicity": "Quick calculation without full inclination testing",
        "accuracy": "Approximate - full stability analysis required for certification"
    },
    "iso_12217": {
        "key_de": "ISO 12217 Stabilitätsnorm",
        "standard": "Small craft stability and buoyancy assessment",
        "parts": {
            "part_1": {
                "title": "Non-planning mono-hull and multi-hull boats",
                "method": "Inclination test for stability curve",
                "applicability": "Most sailing yachts and cruising motor yachts"
            },
            "part_2": {
                "title": "Calculation of stability categories for displacement boats",
                "method": "Mathematical modeling instead of testing",
                "applicability": "Design phase assessment and boats under development"
            },
            "part_3": {
                "title": "Wind and water heel calculations",
                "method": "Dynamic stability assessment",
                "applicability": "Sailing yachts in realistic conditions"
            }
        },
        "boat_length": "Applies to boats typically 6-24 meters (some parts larger)",
        "regulatory_requirement": "Mandatory for CE marking compliance"
    }
}


# ============================================================================
# STANDARDS DATABASE: Comprehensive Marine Standards
# ============================================================================

STANDARDS_DATABASE: Dict[str, Any] = {
    "iso_standards": {
        "key_de": "ISO Normen",
        "iso_12215": {
            "number": "ISO 12215",
            "title": "Small craft - Hull construction and scantling",
            "scope": "Design and construction of hulls for boats ≤24m",
            "coverage": [
                "Hull material specifications (composite, wood, metal)",
                "Scantling (structural member sizing) rules",
                "Design loads (wave impact, slamming)",
                "Construction methodology"
            ],
            "part_1": "Composite/aluminum boats",
            "part_2": "Fiberglass reinforced plastic boats",
            "part_3": "Steel boats",
            "part_4": "Wooden boats"
        },
        "iso_12217": {
            "number": "ISO 12217",
            "title": "Small craft - Stability and buoyancy assessment",
            "scope": "Safety evaluation of boat stability",
            "category_coverage": "A, B, C, D category definition and requirements",
            "testing": "Inclination test, calculation methods, wind heel assessment",
            "regulatory": "Mandatory for CE certification"
        },
        "iso_9094": {
            "number": "ISO 9094",
            "title": "Small craft - Fire protection",
            "part_1": "Boats ≤15m - fire extinguisher and materials",
            "part_2": "Boats >15m - fixed suppression systems, more stringent requirements"
        },
        "iso_15085": {
            "number": "ISO 15085",
            "title": "Small craft - Man overboard prevention and recovery",
            "recent_update": "Updated 2024",
            "coverage": [
                "Design to prevent person-overboard situations",
                "Recovery equipment (ladders, lines)",
                "Training requirements",
                "Vessel design modifications"
            ]
        },
        "iso_12216": {
            "number": "ISO 12216",
            "title": "Small craft - Windows, hatches, doors and associated structures",
            "requirements": [
                "Strength of windows/hatches",
                "Watertightness verification",
                "Installation standards",
                "Testing procedures"
            ]
        },
        "iso_10133": {
            "number": "ISO 10133",
            "title": "Small craft electrical systems - Direct current",
            "scope": "DC electrical installation safety",
            "coverage": "12V/24V/48V systems, wiring, switches, protection"
        },
        "iso_13297": {
            "number": "ISO 13297",
            "title": "Small craft electrical systems - Alternating current",
            "scope": "110V/220V/240V AC electrical systems",
            "coverage": "Shore power, generators, wiring, grounding"
        },
        "iso_11105": {
            "number": "ISO 11105",
            "title": "Engine room ventilation for small craft",
            "requirements": [
                "Air flow rates for engine operation",
                "Fresh air intake sizing",
                "Exhaust duct specification",
                "Safety for gasoline/diesel engines"
            ]
        },
        "iso_8666": {
            "number": "ISO 8666",
            "title": "Small craft - Principal dimensions",
            "scope": "Definition of hull dimensions for vessel classification",
            "coverage": "LOA, LWL, beam, draft, freeboard measurement standardization"
        },
        "iso_10087": {
            "number": "ISO 10087",
            "title": "Small craft - Boat identification and record",
            "scope": "Hull Identification Number (HIN) assignment",
            "requirement": "Mandatory HIN on all recreational craft",
            "format": "12-character code identifying manufacturer, model, year"
        }
    },
    "regulatory_frameworks": {
        "key_de": "Regulatorische Rahmenbedingungen",
        "ce_directive_2013_53_eu": {
            "full_name": "Directive 2013/53/EU - Recreational Craft Directive",
            "applicability": "All recreational boats sold or built in EU",
            "effective_date": "Since 1998 (original), 2013 major revision",
            "boat_categories": "A, B, C, D based on operation design",
            "compliance": [
                "CE marking required on hull or construction record",
                "Technical documentation must be maintained",
                "Port state control inspections",
                "Manufacturer liable for compliance"
            ],
            "standards_referenced": [
                "ISO 12217 (stability)",
                "ISO 9094 (fire protection)",
                "ISO 12215 (hull construction)",
                "ISO 12216 (windows/hatches)",
                "ISO 10133/13297 (electrical)",
                "Other ISO standards as referenced"
            ]
        }
    },
    "abyc_standards": {
        "key_de": "ABYC Normen (USA)",
        "organization": "American Boat and Yacht Council",
        "regulatory_status": "Not law but industry standard, sometimes mandated by insurance",
        "abyc_e_11": {
            "title": "Electrical - General",
            "coverage": [
                "Wire sizing for 3% critical / 10% non-critical voltage drop",
                "Color coding standardization",
                "Circuit protection (breakers, fuses)",
                "DC battery systems",
                "Grounding and bonding"
            ],
            "voltage_drop_calculation": "For 12V system: use voltage drop tables based on amperage and distance"
        },
        "abyc_e_13": {
            "title": "Electrical - Lithium Battery Systems",
            "coverage": [
                "Battery Management System (BMS) requirements",
                "Thermal management and temperature monitoring",
                "Isolation of lithium banks from traditional lead-acid systems",
                "Fire detection and suppression for lithium banks"
            ],
            "critical": "Lithium battery systems must meet stringent BMS and thermal protection requirements"
        },
        "abyc_h_24": {
            "title": "Fuel Systems",
            "coverage": [
                "Fuel tank material and construction",
                "Fuel line routing and material specification",
                "Filler and vent specification",
                "Carburetor/fuel injection system safety",
                "Ventilation of fuel vapors"
            ]
        },
        "abyc_h_27": {
            "title": "Seacocks and Through-hulls",
            "requirement": "Through-hull fittings must be DZR bronze or Marelon composite",
            "installation": "All below-waterline fittings must have accessible seacocks",
            "emergency": "Wooden plugs and wrenches available for seacock operation"
        },
        "abyc_h_33": {
            "title": "Liquified Petroleum Gas Systems",
            "coverage": [
                "Locker design and ventilation",
                "Gas line routing and material",
                "Solenoid shutoff valve requirements",
                "Vapor detection and alarm",
                "Thermocouple safety on stoves",
                "System testing and maintenance"
            ],
            "standard_compliance": "Mandatory for LPG systems on US-registered vessels"
        }
    },
    "classification_societies": {
        "key_de": "Klassifizierstellen",
        "lloyds_register": {
            "name": "Lloyd's Register of Shipping",
            "focus": "Yacht classification and survey",
            "products": [
                "Lloyd's Register Class notation for yachts",
                "Design review and certification",
                "Construction survey and oversight",
                "Periodic class renewal surveys",
                "Special service notations (expedition, research, etc.)"
            ],
            "prestige": "World's oldest classification society, high prestige",
            "cost": "Premium but provides independent verification"
        },
        "abs_american": {
            "name": "American Bureau of Shipping (ABS)",
            "focus": "Yacht rules and classification",
            "products": [
                "ABS yacht classification rules",
                "Design assessment and approval",
                "Construction oversight",
                "Class maintenance",
                "Alternative notation system"
            ],
            "scope": "Primarily US/Americas but global operation"
        },
        "dnv_gl": {
            "name": "DNV GL (Det Norske Veritas)",
            "focus": "Yacht notation and design review",
            "service": "Comprehensive yacht classification services",
            "regions": "Strong in Northern Europe, Scandinavia"
        }
    },
    "standards_summary_table": {
        "key_de": "Normen Übersicht",
        "design_phase": [
            "ISO 12215 (scantling/hull design)",
            "ISO 12217 (stability assessment)",
            "ISO 8666 (principal dimensions)"
        ],
        "construction": [
            "ISO 12215 (construction standards)",
            "ISO 12216 (windows/hatches/doors)",
            "ABYC standards for systems"
        ],
        "equipment": [
            "ISO 9094 (fire protection)",
            "ISO 10133 (DC electrical)",
            "ISO 13297 (AC electrical)",
            "ABYC H-24 (fuel systems)",
            "ABYC H-27 (seacocks)",
            "ABYC H-33 (LPG systems)",
            "ISO 11105 (engine ventilation)"
        ],
        "certification": [
            "CE Directive 2013/53/EU (EU requirement)",
            "Lloyd's Register Class (optional prestige)",
            "ABS Notation (optional prestige)",
            "ISO 10087 (HIN identification)"
        ]
    }
}


# ============================================================================
# Module Summary & Integration
# ============================================================================

MODULE_METADATA: Dict[str, Any] = {
    "module_name": "sanitary_interior_safety_deep",
    "version": "1.0",
    "description": "Comprehensive marine systems knowledge covering sanitary installations, interior construction, gas systems, fire safety, leak defense, and regulatory standards",
    "coverage": {
        "seacock_materials": "Material selection for corrosion resistance and safety",
        "toilets": "Types, sanitation hose selection, manufacturers",
        "gas_systems": "LPG installation, safety devices, hazard prevention",
        "interior_materials": "Wood species, plywood grades, joinery techniques",
        "upholstery": "Foam types, fabric selection, ventilation",
        "moisture_control": "Condensation prevention, insulation, ventilation",
        "fire_safety": "Extinguishers, suppression systems, standards",
        "leak_defense": "Bilge pumps, plugs, emergency systems",
        "stability": "Stability indices, testing methods, regulatory categories",
        "standards": "ISO, ABYC, classification societies, CE requirements"
    },
    "language": "German annotations for key technical terms (key_de)",
    "data_structure": "Dict[str, Any] throughout for maximum flexibility",
    "real_world_focus": "Practical experience-based information with real standards",
    "estimated_size": "Exceeds 1800 lines of comprehensive technical content"
}


if __name__ == "__main__":
    print("AYDI Sanitär, Interieur, Sicherheit & Normen — Tiefenwissen")
    print("=" * 80)
    print(f"Module: {MODULE_METADATA['module_name']}")
    print(f"Version: {MODULE_METADATA['version']}")
    print(f"\nDatabases loaded:")
    print(f"  - SEACOCK_DATABASE: {len(SEACOCK_DATABASE)} sections")
    print(f"  - TOILET_DATABASE: {len(TOILET_DATABASE)} sections")
    print(f"  - GAS_INSTALLATION_DATABASE: {len(GAS_INSTALLATION_DATABASE)} sections")
    print(f"  - INTERIOR_DATABASE: {len(INTERIOR_DATABASE)} sections")
    print(f"  - MOISTURE_DATABASE: {len(MOISTURE_DATABASE)} sections")
    print(f"  - FIRE_SAFETY_DATABASE: {len(FIRE_SAFETY_DATABASE)} sections")
    print(f"  - LEAK_DEFENSE_DATABASE: {len(LEAK_DEFENSE_DATABASE)} sections")
    print(f"  - STABILITY_DATABASE: {len(STABILITY_DATABASE)} sections")
    print(f"  - STANDARDS_DATABASE: {len(STANDARDS_DATABASE)} sections")
    print("\nAll knowledge bases initialized successfully.")
