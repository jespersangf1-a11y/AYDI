"""Construction Weak-Points Knowledge Base for Yacht FMEA Analysis.

A comprehensive Failure Mode and Effects Analysis (FMEA) database for yacht
construction identifying critical weak points, failure modes, and prevention
strategies across all major zones and construction methods.

All user-facing strings in German, technical descriptions in English.
Pure function module — no database access.
"""

import logging
from typing import Dict, List, Optional, Any

logger = logging.getLogger(__name__)

# ============================================================================
# ZONE WEAKPOINTS - Critical areas organized by structural zone
# ============================================================================

ZONE_WEAKPOINTS = {
    "hull_below_waterline": {
        "critical_areas": [
            {
                "location": "Gelcoat-Laminate Interface",
                "failure_mode": "Osmotic blistering",
                "severity": "critical",
                "onset_years": 5,
                "symptoms": "Small blisters appear below waterline, white crystalline deposits",
                "root_cause": "Water permeation through gelcoat into epoxy pockets, hydrolysis",
                "affected_boat_classes": ["cruising_sail", "large_motor", "motorsailer"],
            },
            {
                "location": "Keel Root Fillet",
                "failure_mode": "Delamination under load",
                "severity": "critical",
                "onset_years": 8,
                "symptoms": "Cracking at root, hollow sound when tapped, visible gap",
                "root_cause": "Insufficient fillet radius, impact loads, resin starvation",
                "affected_boat_classes": ["racing_sail", "small_sail", "daysailer"],
            },
            {
                "location": "Bilge Area",
                "failure_mode": "Water staining, soft spot development",
                "severity": "major",
                "onset_years": 4,
                "symptoms": "Discoloration, soft laminate when pressed, mold growth",
                "root_cause": "Inadequate ventilation, standing water, poor drainage",
                "affected_boat_classes": ["all"],
            },
            {
                "location": "Through-hull fitting zones",
                "failure_mode": "Water ingress around penetration",
                "severity": "critical",
                "onset_years": 3,
                "symptoms": "Water weeping, corrosion rings, interior moisture damage",
                "root_cause": "Sealant degradation, micro-movement, poor bedding",
                "affected_boat_classes": ["all"],
            },
            {
                "location": "Rudder Post Bearing",
                "failure_mode": "Bearing wear, water intrusion",
                "severity": "major",
                "onset_years": 7,
                "symptoms": "Rudder play increases, water dripping in cabin",
                "root_cause": "Inadequate sealing, misalignment, bearing material degradation",
                "affected_boat_classes": ["cruising_sail", "motorsailer"],
            },
            {
                "location": "Propeller shaft sea tube",
                "failure_mode": "Bearing corrosion, seal failure",
                "severity": "critical",
                "onset_years": 6,
                "symptoms": "Engine room flood, oil leakage, excessive shaft runout",
                "root_cause": "Galvanic corrosion, inadequate sealing, bearing wear",
                "affected_boat_classes": ["large_motor", "motorsailer"],
            },
        ],
        "water_ingress_vectors": [
            {
                "entry_point": "Underwater fasteners",
                "mechanism": "Crevice corrosion around fasteners, seal degradation",
                "detection_method": "Infrared thermography, conductivity testing",
                "prevention": "Stainless passivation, silicone adhesive, regular inspection",
            },
            {
                "entry_point": "Haul-out damage zone",
                "mechanism": "Microcracks from cradle pressure, impact damage",
                "detection_method": "Ultrasonic testing, visual inspection at haulout",
                "prevention": "Proper cradle padding, care during haul/launch, repair schedule",
            },
            {
                "entry_point": "Running strut appendages",
                "mechanism": "Flow-induced vibration, fatigue cracking",
                "detection_method": "Dye penetrant, eddy current, ultrasonic inspection",
                "prevention": "Reinforced root design, proper bonding, anodes",
            },
        ],
        "chafing_zones": [
            {
                "location": "Keel cable ties",
                "rubbing_surfaces": "Cable against composite flange",
                "material_pairs_at_risk": ["polypropylene_cable", "carbon_fiber_weave"],
                "prevention": "Protective sleeves, edge rounding, cable routing optimization",
            },
        ],
    },
    "hull_above_waterline": {
        "critical_areas": [
            {
                "location": "Sheer line strakes",
                "failure_mode": "UV degradation, color fading, resin check",
                "severity": "minor",
                "onset_years": 4,
                "symptoms": "Color loss, dull appearance, hairline cracking in gelcoat",
                "root_cause": "UV radiation, inadequate UV inhibitors in gelcoat",
                "affected_boat_classes": ["all"],
            },
            {
                "location": "Hull-deck joint exterior",
                "failure_mode": "Caulk failure, water leakage into joint",
                "severity": "major",
                "onset_years": 5,
                "symptoms": "Water weeping, deck delamination, interior mold",
                "root_cause": "Polyurethane sealant shrinkage, movement, thermal cycling",
                "affected_boat_classes": ["all"],
            },
            {
                "location": "Drain hole corners",
                "failure_mode": "Resin pooling, micro-cracks",
                "severity": "minor",
                "onset_years": 6,
                "symptoms": "Cracks radiating from hole, cosmetic blistering",
                "root_cause": "Sharp corner stress concentration, incomplete drainage",
                "affected_boat_classes": ["all"],
            },
        ],
        "water_ingress_vectors": [
            {
                "entry_point": "Rain water on deck",
                "mechanism": "Flow under caulk, capillary action into laminate",
                "detection_method": "Water spray test, tracer dye injection",
                "prevention": "Proper slope design, quality caulking, sealant renewal",
            },
        ],
        "chafing_zones": [
            {
                "location": "Shroud attachment pads",
                "rubbing_surfaces": "Stainless plates against gelcoat",
                "material_pairs_at_risk": ["stainless_316", "gelcoat"],
                "prevention": "Anti-skid strips, bedding compound renewal, inspection",
            },
        ],
    },
    "deck": {
        "critical_areas": [
            {
                "location": "Mast step partner beams",
                "failure_mode": "Compression failure, splintering",
                "severity": "critical",
                "onset_years": 10,
                "symptoms": "Cracking around mast collar, mast moves side to side",
                "root_cause": "Overload from sail plan, inadequate beam sizing, impact loads",
                "affected_boat_classes": ["racing_sail", "cruising_sail"],
            },
            {
                "location": "Deck core interface",
                "failure_mode": "Delamination, water intrusion",
                "severity": "critical",
                "onset_years": 8,
                "symptoms": "Soft spots, water staining, hollow sound",
                "root_cause": "Resin starvation in sandwich, core saturation, impact damage",
                "affected_boat_classes": ["all"],
            },
            {
                "location": "Stanchion bases",
                "failure_mode": "Core crush, fastener pull-through",
                "severity": "major",
                "onset_years": 6,
                "symptoms": "Base loosens, cracks around fasteners",
                "root_cause": "Deck flexing, inadequate washers, creep in sandwich core",
                "affected_boat_classes": ["all"],
            },
            {
                "location": "Deck hatches",
                "failure_mode": "Seal degradation, water leakage",
                "severity": "major",
                "onset_years": 5,
                "symptoms": "Water dripping below hatch, condensation, mold",
                "root_cause": "UV aging of rubber gasket, sealant failure, misalignment",
                "affected_boat_classes": ["all"],
            },
            {
                "location": "Ventilation ducting terminations",
                "failure_mode": "Water siphoning during heavy weather",
                "severity": "major",
                "onset_years": 3,
                "symptoms": "Water entry during sailing, interior moisture",
                "root_cause": "Duct below deck level, inadequate baffles, wave washover",
                "affected_boat_classes": ["cruising_sail", "motorsailer"],
            },
        ],
        "water_ingress_vectors": [
            {
                "entry_point": "Teak deck seams",
                "mechanism": "Capillary action through wood grain, sealing compound loss",
                "detection_method": "Water spray test, core sampling",
                "prevention": "Regular sealing, proper drainage slope, underlayment",
            },
            {
                "entry_point": "Fastener holes",
                "mechanism": "Capillary leakage around stainless fasteners",
                "detection_method": "Tracer dye, borescope inspection",
                "prevention": "Adhesive sealing, sealant around bolts, regular inspection",
            },
        ],
        "chafing_zones": [
            {
                "location": "Genoa track under boom",
                "rubbing_surfaces": "Stainless track, sail batten, lazy jack lines",
                "material_pairs_at_risk": ["stainless_303", "polypropylene", "dacron"],
                "prevention": "Protective covers, proper track maintenance, line routing",
            },
            {
                "location": "Spinnaker pole rest points",
                "rubbing_surfaces": "Aluminum pole against deck edge reinforcement",
                "material_pairs_at_risk": ["aluminum_6061", "carbon_fiber_edge"],
                "prevention": "Padding, foam inserts, protective sleeves",
            },
        ],
    },
    "cabin_top": {
        "critical_areas": [
            {
                "location": "Cabin roof-coachroof joint",
                "failure_mode": "Caulk deterioration, interior water stains",
                "severity": "major",
                "onset_years": 6,
                "symptoms": "Water staining on interior, soft spots in cabin",
                "root_cause": "Polyurethane sealant aging, movement, improper slope",
                "affected_boat_classes": ["all"],
            },
            {
                "location": "Cabin trunk core saturation zone",
                "failure_mode": "Water absorption, delamination, mold",
                "severity": "major",
                "onset_years": 7,
                "symptoms": "Heavy cabin trunk, soft spots, musty odor",
                "root_cause": "Inadequate sealant, core exposed through cracks, poor ventilation",
                "affected_boat_classes": ["all"],
            },
        ],
        "water_ingress_vectors": [
            {
                "entry_point": "Companionway area",
                "mechanism": "Spray washover, improper slope directing water inboard",
                "detection_method": "Water spray test, tracer dye",
                "prevention": "Proper slope design, sill height optimization, drain channels",
            },
        ],
        "chafing_zones": [
            {
                "location": "Mainsheet traveler car channels",
                "rubbing_surfaces": "Nylon car wheels, stainless rail",
                "material_pairs_at_risk": ["acetal_copolymer", "stainless_304"],
                "prevention": "Regular lubrication, wheel replacement, channel cleaning",
            },
        ],
    },
    "cockpit": {
        "critical_areas": [
            {
                "location": "Cockpit locker seals",
                "failure_mode": "Gasket degradation, moisture ingress",
                "severity": "major",
                "onset_years": 5,
                "symptoms": "Mold growth inside lockers, musty odor",
                "root_cause": "UV aging of rubber, compression set, inadequate ventilation",
                "affected_boat_classes": ["all"],
            },
            {
                "location": "Cockpit floor drain system",
                "failure_mode": "Blockage, reverse siphon water entry",
                "severity": "major",
                "onset_years": 4,
                "symptoms": "Cockpit pooling, engine room flood, bilge overflow",
                "root_cause": "Debris accumulation, check valve failure, siphon conditions",
                "affected_boat_classes": ["all"],
            },
            {
                "location": "Wheel pedestal base",
                "failure_mode": "Corrosion, fastener failure, deck core crush",
                "severity": "major",
                "onset_years": 8,
                "symptoms": "Wheel wobbles, base corrosion visible, cracks around base",
                "root_cause": "Salt spray exposure, galvanic corrosion, inadequate washers",
                "affected_boat_classes": ["all"],
            },
        ],
        "water_ingress_vectors": [
            {
                "entry_point": "Steering cable exits",
                "mechanism": "Water seepage along cable conduit",
                "detection_method": "Visual inspection, moisture sensors below",
                "prevention": "Sealant compound, cable glands, regular inspection",
            },
        ],
        "chafing_zones": [
            {
                "location": "Winch drum",
                "rubbing_surfaces": "Rope against stainless drum edges",
                "material_pairs_at_risk": ["polyester_rope", "stainless_316"],
                "prevention": "Smooth drum edges, proper rope sizing, drum maintenance",
            },
        ],
    },
    "keel": {
        "critical_areas": [
            {
                "location": "Keel-hull junction laminate",
                "failure_mode": "Fatigue cracking, delamination",
                "severity": "critical",
                "onset_years": 6,
                "symptoms": "Cracks visible at root fillet, white stress lines",
                "root_cause": "Insufficient fillet radius, high stress concentration, impact",
                "affected_boat_classes": ["racing_sail", "small_sail"],
            },
            {
                "location": "Keel stub bonding plane",
                "failure_mode": "Separation, laminate spalling",
                "severity": "critical",
                "onset_years": 10,
                "symptoms": "Keel moves laterally, interior cabin cracking",
                "root_cause": "Inadequate surface preparation, poor bond line, cyclic loads",
                "affected_boat_classes": ["cruising_sail", "motorsailer"],
            },
            {
                "location": "Cast iron keel corrosion nodes",
                "failure_mode": "Rusting, weight loss, structural integrity loss",
                "severity": "critical",
                "onset_years": 5,
                "symptoms": "Rust staining on gelcoat, orange deposits underwater",
                "root_cause": "Poor coating, exposure through paint cracks, galvanic corrosion",
                "affected_boat_classes": ["all"],
            },
        ],
        "water_ingress_vectors": [
            {
                "entry_point": "Keel attachment bolt areas",
                "mechanism": "Crevice corrosion, seal degradation",
                "detection_method": "Dye penetrant, X-ray, ultrasonic thickness",
                "prevention": "Stainless fasteners, sealant application, cathodic protection",
            },
        ],
        "chafing_zones": [],
    },
    "rudder": {
        "critical_areas": [
            {
                "location": "Rudder blade root connection",
                "failure_mode": "Fatigue crack initiation",
                "severity": "critical",
                "onset_years": 8,
                "symptoms": "Cracks radiating from root, rudder play increases",
                "root_cause": "High bending stress, inadequate root radius, defects in laminate",
                "affected_boat_classes": ["racing_sail", "cruising_sail"],
            },
            {
                "location": "Rudder stock bearing in hull",
                "failure_mode": "Bearing wear, water seal failure",
                "severity": "major",
                "onset_years": 7,
                "symptoms": "Rudder hard to turn, water dripping, stainless corrosion",
                "root_cause": "Bearing material degradation, alignment issues, inadequate sealing",
                "affected_boat_classes": ["all"],
            },
            {
                "location": "Rudder post epoxy bushing",
                "failure_mode": "Delamination, movement in bore",
                "severity": "major",
                "onset_years": 6,
                "symptoms": "Rudder wobbles, clearance increases",
                "root_cause": "Resin starvation, inadequate cure, bearing loads",
                "affected_boat_classes": ["all"],
            },
        ],
        "water_ingress_vectors": [
            {
                "entry_point": "Rudder post gland packing",
                "mechanism": "Seal degradation, water weeping along shaft",
                "detection_method": "Visual inspection, water level monitoring",
                "prevention": "Regular packing replacement, shaft polishing, seal inspection",
            },
        ],
        "chafing_zones": [],
    },
    "mast_step": {
        "critical_areas": [
            {
                "location": "Mast step base laminate",
                "failure_mode": "Fatigue cracking around collar",
                "severity": "critical",
                "onset_years": 7,
                "symptoms": "Cracks radiating outward, white stress marks",
                "root_cause": "Mast flutter, inadequate collar reinforcement, impact loads",
                "affected_boat_classes": ["racing_sail", "small_sail"],
            },
            {
                "location": "Deck beam under mast",
                "failure_mode": "Compression failure, crushing",
                "severity": "critical",
                "onset_years": 9,
                "symptoms": "Visible compression lines, beam soft when pressed",
                "root_cause": "Inadequate beam sizing, core materials, structural loads",
                "affected_boat_classes": ["all"],
            },
        ],
        "water_ingress_vectors": [
            {
                "entry_point": "Mast collar around mast tube",
                "mechanism": "Capillary action up mast tube, spray washover",
                "detection_method": "Visual inspection, moisture detector inside tube",
                "prevention": "Sealant application, mast base drain, collar reinforcement",
            },
        ],
        "chafing_zones": [],
    },
    "chainplates": {
        "critical_areas": [
            {
                "location": "Chainplate-deck laminate interface",
                "failure_mode": "Delamination, core crush under load",
                "severity": "major",
                "onset_years": 6,
                "symptoms": "Chainplate loosens, cracks in laminate, water staining",
                "root_cause": "Inadequate backing plate size, load concentration, creep",
                "affected_boat_classes": ["all"],
            },
            {
                "location": "Stainless chainplate fastener holes",
                "failure_mode": "Crevice corrosion, fastener corrosion",
                "severity": "major",
                "onset_years": 5,
                "symptoms": "White corrosion deposits, fastener seizing, loosening",
                "root_cause": "Galvanic coupling, inadequate sealing, moisture trapping",
                "affected_boat_classes": ["all"],
            },
        ],
        "water_ingress_vectors": [
            {
                "entry_point": "Chainplate fastener area",
                "mechanism": "Crevice attack, sealant degradation",
                "detection_method": "Visual inspection, impedance spectroscopy",
                "prevention": "Sealant compound, stainless passivation, regular inspection",
            },
        ],
        "chafing_zones": [
            {
                "location": "Shroud-chainplate connection",
                "rubbing_surfaces": "Stainless wire, ss padeye, ss wire terminal",
                "material_pairs_at_risk": ["stainless_1x19_wire", "stainless_316"],
                "prevention": "Proper swaging, smooth edges, inspection schedule",
            },
        ],
    },
    "windows": {
        "critical_areas": [
            {
                "location": "Window frame elastomer seal",
                "failure_mode": "Seal degradation, water leakage",
                "severity": "major",
                "onset_years": 7,
                "symptoms": "Water dripping inside, mold on sill, fogging between panes",
                "root_cause": "UV aging, ozone attack, compression set, thermal cycling",
                "affected_boat_classes": ["all"],
            },
            {
                "location": "Window polycarbonate crazing",
                "failure_mode": "Stress cracking, UV degradation",
                "severity": "minor",
                "onset_years": 8,
                "symptoms": "Fine stress cracks, internal crazing, light scatter",
                "root_cause": "Stress concentration, UV radiation, organic solvent exposure",
                "affected_boat_classes": ["all"],
            },
            {
                "location": "Tempered glass edge spalling",
                "failure_mode": "Spontaneous fracture, edge chipping",
                "severity": "major",
                "onset_years": 5,
                "symptoms": "Chips on edges, radial cracks from impact, complete failure",
                "root_cause": "Edge damage from installation, thermal shock, impact",
                "affected_boat_classes": ["all"],
            },
        ],
        "water_ingress_vectors": [
            {
                "entry_point": "Window frame corners",
                "mechanism": "Sealant compound stress concentration, capillary action",
                "detection_method": "Water spray test, tracer dye injection",
                "prevention": "Fillet-radius sealant, quality glazing compounds, regular inspection",
            },
        ],
        "chafing_zones": [],
    },
    "hatches": {
        "critical_areas": [
            {
                "location": "Hatch gasket compression",
                "failure_mode": "Permanent set, seal failure",
                "severity": "major",
                "onset_years": 6,
                "symptoms": "Water entry during rain, hatch will not seal completely",
                "root_cause": "UV degradation, compression set in elastomer, thermal cycling",
                "affected_boat_classes": ["all"],
            },
            {
                "location": "Hatch frame delamination",
                "failure_mode": "Separation, warping, water entry",
                "severity": "major",
                "onset_years": 7,
                "symptoms": "Hatch flexes excessively, water weeping, interior damage",
                "root_cause": "UV exposure, core saturation, inadequate laminate thickness",
                "affected_boat_classes": ["all"],
            },
            {
                "location": "Hatch latch mechanism corrosion",
                "failure_mode": "Latch freezing, breakage",
                "severity": "minor",
                "onset_years": 4,
                "symptoms": "Latch difficult to operate, corrosion visible, eventual seizure",
                "root_cause": "Salt spray exposure, galvanic corrosion, inadequate coatings",
                "affected_boat_classes": ["all"],
            },
        ],
        "water_ingress_vectors": [
            {
                "entry_point": "Hatch frame overlap",
                "mechanism": "Capillary action under caulk, wave washover",
                "detection_method": "Water spray test, thermal imaging",
                "prevention": "Proper slope design, sealant renewal, hatch positioning",
            },
        ],
        "chafing_zones": [],
    },
    "through_hulls": {
        "critical_areas": [
            {
                "location": "Through-hull fitting bonding zone",
                "failure_mode": "Seal failure, water intrusion",
                "severity": "critical",
                "onset_years": 4,
                "symptoms": "Water seeping around fitting, corrosion deposits, staining",
                "root_cause": "Inadequate bedding compound, poor surface preparation, micro-movement",
                "affected_boat_classes": ["all"],
            },
            {
                "location": "Seacock internal lever corrosion",
                "failure_mode": "Valve sticking, inability to close",
                "severity": "critical",
                "onset_years": 5,
                "symptoms": "Valve hard to operate, lever stuck, corrosion inside valve",
                "root_cause": "Mineral deposits, seawater corrosion, inadequate maintenance",
                "affected_boat_classes": ["all"],
            },
            {
                "location": "Zinc anode pitting on through-hull",
                "failure_mode": "Anode dissolution, fastener exposure",
                "severity": "major",
                "onset_years": 3,
                "symptoms": "Anode thin, stainless fastener corrosion starting",
                "root_cause": "Inadequate anode sizing, stray current, high water resistance",
                "affected_boat_classes": ["all"],
            },
        ],
        "water_ingress_vectors": [
            {
                "entry_point": "Through-hull skin area",
                "mechanism": "Seal degradation, micro-movement under load",
                "detection_method": "Water spray test, conductivity probe, borescope",
                "prevention": "Quality bedding compound, regular inspection, seal replacement",
            },
        ],
        "chafing_zones": [],
    },
    "propeller_shaft": {
        "critical_areas": [
            {
                "location": "Shaft coupling misalignment",
                "failure_mode": "Bearing wear, vibration, alignment loss",
                "severity": "major",
                "onset_years": 6,
                "symptoms": "Propeller vibration, bearings overheat, shaft runout increases",
                "root_cause": "Engine settling, bearing wear, inadequate alignment procedure",
                "affected_boat_classes": ["large_motor", "motorsailer"],
            },
            {
                "location": "Propeller hub corrosion area",
                "failure_mode": "Key corrosion, hub loosening",
                "severity": "major",
                "onset_years": 4,
                "symptoms": "Propeller loosens, key corrodes, metallic clinking noise",
                "root_cause": "Galvanic corrosion, inadequate keyway sealing, sacrificial anode failure",
                "affected_boat_classes": ["all"],
            },
        ],
        "water_ingress_vectors": [],
        "chafing_zones": [],
    },
    "stern_tube": {
        "critical_areas": [
            {
                "location": "Stern tube bearing bronze corrosion",
                "failure_mode": "Bearing material loss, seal failure",
                "severity": "critical",
                "onset_years": 6,
                "symptoms": "Water seeping into engine room, bearing noise, shaft runout",
                "root_cause": "Galvanic corrosion, water chemistry, bearing wear",
                "affected_boat_classes": ["large_motor", "motorsailer"],
            },
            {
                "location": "Stern tube elastomer seal",
                "failure_mode": "Seal degradation, water entry",
                "severity": "critical",
                "onset_years": 5,
                "symptoms": "Water flooding engine room, oil mixing with water",
                "root_cause": "UV aging, thermal cycling, inadequate installation",
                "affected_boat_classes": ["all"],
            },
        ],
        "water_ingress_vectors": [
            {
                "entry_point": "Stern tube seal zone",
                "mechanism": "Seal degradation under pressure, shaft micro-movement",
                "detection_method": "Visual inspection, water level monitoring, pressure test",
                "prevention": "Regular seal replacement, shaft polishing, alignment check",
            },
        ],
        "chafing_zones": [],
    },
    "bow_thruster": {
        "critical_areas": [
            {
                "location": "Thruster through-hull seals",
                "failure_mode": "Seal failure, water ingress into engine room",
                "severity": "critical",
                "onset_years": 5,
                "symptoms": "Water flooding engine room, thruster leaking",
                "root_cause": "Seal degradation, inadequate bedding, installation error",
                "affected_boat_classes": ["large_motor"],
            },
            {
                "location": "Propeller blade fatigue zone",
                "failure_mode": "Blade cracking, spalling",
                "severity": "major",
                "onset_years": 8,
                "symptoms": "Vibration, cracks visible on blade, noise during operation",
                "root_cause": "Cavitation, inadequate blade material, impact damage",
                "affected_boat_classes": ["large_motor"],
            },
        ],
        "water_ingress_vectors": [
            {
                "entry_point": "Thruster tube penetration",
                "mechanism": "Seal degradation, pressure gradient",
                "detection_method": "Visual inspection, water sampling, pressure test",
                "prevention": "Seal maintenance, alignment verification, regular testing",
            },
        ],
        "chafing_zones": [],
    },
    "flybridge": {
        "critical_areas": [
            {
                "location": "Flybridge railing stanchion base",
                "failure_mode": "Base separation, core crush",
                "severity": "major",
                "onset_years": 6,
                "symptoms": "Stanchion becomes loose, cracking visible around base",
                "root_cause": "Inadequate backing plate, fastener pull-through, deck core creep",
                "affected_boat_classes": ["large_motor"],
            },
            {
                "location": "Soft top frame corners",
                "failure_mode": "Stress cracking in laminate",
                "severity": "minor",
                "onset_years": 5,
                "symptoms": "Fine cracks at stress points, white stress marks",
                "root_cause": "Flex concentration, inadequate corner radius, dynamic loading",
                "affected_boat_classes": ["large_motor"],
            },
        ],
        "water_ingress_vectors": [
            {
                "entry_point": "Soft top seams",
                "mechanism": "Sealant degradation, UV exposure",
                "detection_method": "Visual inspection, water spray test",
                "prevention": "Sealant renewal, UV protection, regular inspection",
            },
        ],
        "chafing_zones": [],
    },
    "transom": {
        "critical_areas": [
            {
                "location": "Transom laminate backing plate interface",
                "failure_mode": "Delamination, water intrusion",
                "severity": "critical",
                "onset_years": 7,
                "symptoms": "Transom flexes excessively, water staining, soft spots",
                "root_cause": "Inadequate laminate strength, backing plate insufficient, impact loads",
                "affected_boat_classes": ["all"],
            },
            {
                "location": "Engine mounting pad corrosion",
                "failure_mode": "Fastener corrosion, pad loosening",
                "severity": "major",
                "onset_years": 5,
                "symptoms": "Engine vibration increases, fasteners corrode, visual rust",
                "root_cause": "Galvanic corrosion, inadequate coating, salt spray exposure",
                "affected_boat_classes": ["all"],
            },
        ],
        "water_ingress_vectors": [
            {
                "entry_point": "Transom drain systems",
                "mechanism": "Siphoning during operation, blockage, check valve failure",
                "detection_method": "Water level monitoring, drain flushing",
                "prevention": "Check valve maintenance, drain slope optimization, regular cleaning",
            },
        ],
        "chafing_zones": [],
    },
    "anchor_locker": {
        "critical_areas": [
            {
                "location": "Anchor locker drain seal",
                "failure_mode": "Water trapping, corrosion of hardware",
                "severity": "minor",
                "onset_years": 4,
                "symptoms": "Standing water smell, chain corrosion, mold growth",
                "root_cause": "Inadequate drainage, clogged vent, poor ventilation",
                "affected_boat_classes": ["all"],
            },
        ],
        "water_ingress_vectors": [
            {
                "entry_point": "Anchor chain well",
                "mechanism": "Washover during heavy weather, inadequate drainage",
                "detection_method": "Visual inspection, water level check",
                "prevention": "Proper drain sizing, vent height optimization, regular cleaning",
            },
        ],
        "chafing_zones": [
            {
                "location": "Anchor chain against locker fiberglass",
                "rubbing_surfaces": "Galvanized chain, fiberglass gelcoat",
                "material_pairs_at_risk": ["galvanized_steel_chain", "polyester_gelcoat"],
                "prevention": "Chain netting, protective fabric lining, regular inspection",
            },
        ],
    },
    "engine_room": {
        "critical_areas": [
            {
                "location": "Engine mounting elastomer bushings",
                "failure_mode": "Rubber degradation, bushing failure",
                "severity": "major",
                "onset_years": 5,
                "symptoms": "Engine vibration increases, visible cracking in rubber",
                "root_cause": "Oil degradation of rubber, thermal cycling, age",
                "affected_boat_classes": ["all"],
            },
            {
                "location": "Stainless fastener crevice corrosion",
                "failure_mode": "Fastener stress corrosion cracking",
                "severity": "major",
                "onset_years": 6,
                "symptoms": "Fasteners corrode and break, visible cracks, corrosion deposits",
                "root_cause": "Crevice corrosion, chloride concentration, stress",
                "affected_boat_classes": ["all"],
            },
        ],
        "water_ingress_vectors": [
            {
                "entry_point": "Engine room through-hull fittings",
                "mechanism": "Seal failure, backing plate corrosion",
                "detection_method": "Visual inspection, water sampling",
                "prevention": "Regular seal replacement, fitting inspection, coating maintenance",
            },
        ],
        "chafing_zones": [],
    },
    "fuel_system": {
        "critical_areas": [
            {
                "location": "Fuel tank vent line corrosion zone",
                "failure_mode": "Vent blockage, fuel tank overflow",
                "severity": "major",
                "onset_years": 4,
                "symptoms": "Fuel overflow from vent, loss of fuel capacity, blockage",
                "root_cause": "Salt air corrosion, inadequate drain, internal rust",
                "affected_boat_classes": ["all"],
            },
            {
                "location": "Fuel line elastomer hose degradation",
                "failure_mode": "Hose cracking, fuel seepage",
                "severity": "critical",
                "onset_years": 8,
                "symptoms": "Fuel smell, leaking fuel, engine room contamination",
                "root_cause": "UV aging, ozone attack, ethanol fuel degradation",
                "affected_boat_classes": ["all"],
            },
        ],
        "water_ingress_vectors": [],
        "chafing_zones": [],
    },
    "electrical_system": {
        "critical_areas": [
            {
                "location": "Battery terminal corrosion zone",
                "failure_mode": "Terminal corrosion, resistance increase, poor connection",
                "severity": "minor",
                "onset_years": 3,
                "symptoms": "Corrosion deposits visible, hard starting, poor charging",
                "root_cause": "Galvanic corrosion, moisture, inadequate coating",
                "affected_boat_classes": ["all"],
            },
            {
                "location": "Stainless fastener in aluminum conductor lug",
                "failure_mode": "Galvanic corrosion, fastener seizure",
                "severity": "major",
                "onset_years": 4,
                "symptoms": "Connection loosens, fastener cannot be removed, corrosion visible",
                "root_cause": "Galvanic coupling, inadequate sealant, moisture ingress",
                "affected_boat_classes": ["all"],
            },
        ],
        "water_ingress_vectors": [],
        "chafing_zones": [],
    },
    "rigging": {
        "critical_areas": [
            {
                "location": "Stainless wire swage termination corrosion",
                "failure_mode": "Crevice corrosion initiation at swage",
                "severity": "major",
                "onset_years": 6,
                "symptoms": "Corrosion deposits visible at termination, wire weakening",
                "root_cause": "Moisture trapping in swage, inadequate sealing, pit initiation",
                "affected_boat_classes": ["all"],
            },
            {
                "location": "Mast extrusion crack initiation zones",
                "failure_mode": "Stress corrosion cracking",
                "severity": "critical",
                "onset_years": 7,
                "symptoms": "Cracks visible in extrusion profile, splintering, fracture risk",
                "root_cause": "Residual stress from extrusion, crevice corrosion, stress cycling",
                "affected_boat_classes": ["racing_sail", "cruising_sail"],
            },
        ],
        "water_ingress_vectors": [],
        "chafing_zones": [
            {
                "location": "Spreader tip wire contact",
                "rubbing_surfaces": "Stainless wire, aluminum spreader tip",
                "material_pairs_at_risk": ["stainless_1x19", "aluminum_6061_t6"],
                "prevention": "Wire guide installation, friction tape, inspection schedule",
            },
        ],
    },
    "stanchions": {
        "critical_areas": [
            {
                "location": "Stanchion base fastener holes",
                "failure_mode": "Fastener corrosion and pull-through",
                "severity": "major",
                "onset_years": 5,
                "symptoms": "Stanchion loosens, cracks around base, corrosion visible",
                "root_cause": "Crevice corrosion, inadequate washers, creep in sandwich",
                "affected_boat_classes": ["all"],
            },
            {
                "location": "Aluminum tube extrusion corrosion spots",
                "failure_mode": "Pitting corrosion, stress concentration",
                "severity": "minor",
                "onset_years": 4,
                "symptoms": "Corrosion pits visible, discoloration, corrosion staining",
                "root_cause": "Aluminum oxide breakdown, crevice conditions, salt exposure",
                "affected_boat_classes": ["all"],
            },
        ],
        "water_ingress_vectors": [],
        "chafing_zones": [
            {
                "location": "Stanchion wire intersection",
                "rubbing_surfaces": "Stainless wire, aluminum tube",
                "material_pairs_at_risk": ["stainless_316_wire", "aluminum_6061"],
                "prevention": "Wire routing optimization, protective sleeves, inspection",
            },
        ],
    },
    "pulpit": {
        "critical_areas": [
            {
                "location": "Pulpit base plate fasteners",
                "failure_mode": "Fastener corrosion, base loosening",
                "severity": "major",
                "onset_years": 5,
                "symptoms": "Pulpit wobbles, fasteners corrode, visible rust deposits",
                "root_cause": "Galvanic corrosion, crevice attack, inadequate sealing",
                "affected_boat_classes": ["all"],
            },
            {
                "location": "Pulpit rail intersection welds",
                "failure_mode": "Stress corrosion cracking in welds",
                "severity": "major",
                "onset_years": 8,
                "symptoms": "Cracks visible in weld HAZ, corrosion deposits, potential fracture",
                "root_cause": "Residual weld stress, crevice corrosion, cyclic loading",
                "affected_boat_classes": ["all"],
            },
        ],
        "water_ingress_vectors": [],
        "chafing_zones": [],
    },
}

# ============================================================================
# CONSTRUCTION METHOD RISKS
# ============================================================================

CONSTRUCTION_METHOD_RISKS = {
    "hand_layup": {
        "quality_risks": [
            {
                "defect": "Resin starvation",
                "cause": "Insufficient resin application, high fiber volume fraction",
                "detection": "Dry spots visible, high void content on cross-section",
                "severity": "critical",
            },
            {
                "defect": "Fiber waviness",
                "cause": "Poor laminate consolidation, manual placement technique",
                "detection": "Visual inspection under light, ultrasonic C-scan",
                "severity": "major",
            },
            {
                "defect": "Entrapped air voids",
                "cause": "Inadequate roller work, thick laminate buildup",
                "detection": "Ultrasonic testing, cross-section examination",
                "severity": "major",
            },
        ],
        "environmental_requirements": {
            "temperature_min_celsius": 15,
            "temperature_max_celsius": 30,
            "humidity_max_percent": 85,
            "cure_time_hours": 24,
            "post_cure_temperature_celsius": 60,
            "post_cure_time_hours": 4,
        },
        "common_mistakes": [
            "Applying resin before fiber saturation",
            "Using worn-out rollers, leaving patterns in surface",
            "Inadequate surface preparation of previous layer",
            "Laying fiber in same direction repeatedly (no cross-ply)",
            "Applying final layer too thick for proper consolidation",
        ],
        "inspection_points": [
            "Fiber alignment and waviness",
            "Void content (cross-section analysis, ultrasonic)",
            "Resin gel-time confirmation",
            "Surface finish (smoothness, no dry spots)",
            "Laminate thickness and fiber volume fraction",
        ],
    },
    "vacuum_infusion": {
        "quality_risks": [
            {
                "defect": "Dry fiber pockets",
                "cause": "Vacuum leak, incorrect fiber placement, inadequate vent location",
                "detection": "White dry spots visible, resin weight below specification",
                "severity": "critical",
            },
            {
                "defect": "Wrinkles in fiber reinforcement",
                "cause": "Bagging pressure too high, fiber movement during infusion",
                "detection": "Visual inspection, ultrasonic C-scan",
                "severity": "major",
            },
            {
                "defect": "Resin pool areas",
                "cause": "Vent location too high, fiber saturation incomplete",
                "detection": "Weight variation, resin-rich areas in sections",
                "severity": "major",
            },
        ],
        "environmental_requirements": {
            "temperature_min_celsius": 18,
            "temperature_max_celsius": 28,
            "humidity_max_percent": 80,
            "cure_time_hours": 16,
            "post_cure_temperature_celsius": 80,
            "post_cure_time_hours": 8,
        },
        "common_mistakes": [
            "Inadequate vacuum setup (slow pump, leaking fittings)",
            "Incorrect flow media arrangement (blocking resin flow)",
            "Fiber preform not properly secured (movement during infusion)",
            "Vent placement too close to inlet (premature resin exit)",
            "No backup vacuum system for power loss",
        ],
        "inspection_points": [
            "Vacuum integrity (no leaks at seams)",
            "Fiber/resin saturation (no dry spots)",
            "Resin flow pattern verification",
            "Laminate density and void content",
            "Surface finish consistency",
        ],
    },
    "prepreg_autoclave": {
        "quality_risks": [
            {
                "defect": "Fiber waviness in thick sections",
                "cause": "Inadequate vacuum bag consolidation, resin flow during cure",
                "detection": "Ultrasonic testing, cross-section analysis",
                "severity": "major",
            },
            {
                "defect": "Porosity in core bondline",
                "cause": "Volatiles trapped during cure, inadequate vacuum",
                "detection": "Ultrasonic C-scan, cross-sectioning",
                "severity": "critical",
            },
        ],
        "environmental_requirements": {
            "temperature_min_celsius": 20,
            "temperature_max_celsius": 25,
            "humidity_max_percent": 60,
            "cure_time_hours": 4,
            "post_cure_temperature_celsius": 120,
            "post_cure_time_hours": 2,
        },
        "common_mistakes": [
            "Storage temperature control inadequate (resin advance)",
            "Prepreg tack loss before bagging",
            "Unequal vacuum during autoclave cycle",
            "No thermocouples for temperature verification",
            "Incorrect pressure ramp rate",
        ],
        "inspection_points": [
            "Void content (ultrasonic, cross-section)",
            "Fiber volume fraction (ideal 60-65%)",
            "Dimensional accuracy and surface finish",
            "Laminate consolidation quality",
            "Bondline thickness (core sandwich)",
        ],
    },
    "resin_transfer_molding": {
        "quality_risks": [
            {
                "defect": "Weld line defects",
                "cause": "Inadequate mold design, resin flow meeting point weakness",
                "detection": "Visual inspection, ultrasonic testing across mold",
                "severity": "major",
            },
            {
                "defect": "Resin pockets and dead zones",
                "cause": "Inadequate vent location, fiber placement",
                "detection": "Visual inspection, weight analysis",
                "severity": "critical",
            },
        ],
        "environmental_requirements": {
            "temperature_min_celsius": 18,
            "temperature_max_celsius": 28,
            "humidity_max_percent": 75,
            "cure_time_hours": 8,
            "post_cure_temperature_celsius": 60,
            "post_cure_time_hours": 12,
        },
        "common_mistakes": [
            "Injection pressure too high (fiber movement, weld lines)",
            "Fiber architecture not optimized for mold geometry",
            "Inadequate fiber preform anchoring",
            "Poor vent design (low vacuum)",
            "Injector/vent gate pressure mismatch",
        ],
        "inspection_points": [
            "Fiber alignment and waviness",
            "Void and porosity (target <3%)",
            "Weld line strength (testing)",
            "Surface finish and dimensional accuracy",
            "Resin distribution uniformity",
        ],
    },
    "spray_layup": {
        "quality_risks": [
            {
                "defect": "High void content",
                "cause": "Inadequate consolidation, air entrapment during spraying",
                "detection": "Cross-sectioning, ultrasonic testing",
                "severity": "critical",
            },
            {
                "defect": "Fiber length reduction",
                "cause": "Roving shear in spray head, inadequate fiber",
                "detection": "Cross-section examination, mechanical testing",
                "severity": "major",
            },
        ],
        "environmental_requirements": {
            "temperature_min_celsius": 15,
            "temperature_max_celsius": 32,
            "humidity_max_percent": 80,
            "cure_time_hours": 24,
            "post_cure_temperature_celsius": 50,
            "post_cure_time_hours": 8,
        },
        "common_mistakes": [
            "Gun positioned too far from mold (fiber separation)",
            "Wrong spray viscosity (resin runs off, fiber dry)",
            "Inadequate rolling after spraying",
            "Uneven spray pattern (thickness variation)",
            "High humidity during cure (incompletely polymerized)",
        ],
        "inspection_points": [
            "Laminate thickness consistency",
            "Void content and porosity (ultrasonic)",
            "Fiber length and distribution",
            "Resin-to-fiber ratio",
            "Mechanical properties (coupon testing)",
        ],
    },
    "aluminum_welded": {
        "quality_risks": [
            {
                "defect": "HAZ stress corrosion cracking",
                "cause": "Residual stress, crevice corrosion in HAZ, high strength alloys",
                "detection": "Dye penetrant testing, visual inspection, pressure testing",
                "severity": "critical",
            },
            {
                "defect": "Porosity in weld",
                "cause": "Gas entrapment, inadequate shielding, contamination",
                "detection": "Radiography, ultrasonic testing, cross-section",
                "severity": "major",
            },
        ],
        "environmental_requirements": {
            "temperature_min_celsius": 5,
            "temperature_max_celsius": 35,
            "humidity_max_percent": 70,
            "cure_time_hours": 0,
            "post_cure_temperature_celsius": 150,
            "post_cure_time_hours": 2,
        },
        "common_mistakes": [
            "Inadequate surface cleaning before welding",
            "Using wrong filler alloy (zinc-containing can cause cracking)",
            "Inadequate shielding gas coverage",
            "Welding at wrong amperage (too hot or too cold)",
            "Distortion control inadequate (out-of-spec geometry)",
        ],
        "inspection_points": [
            "Visual inspection of weld bead (smooth, no cracks)",
            "Radiographic or ultrasonic testing for porosity",
            "Dye penetrant testing for surface cracks",
            "Hardness testing in HAZ",
            "Pressure test for leaks",
        ],
    },
    "steel_welded": {
        "quality_risks": [
            {
                "defect": "Hydrogen cracking in HAZ",
                "cause": "High carbon steel, inadequate preheat, restraint stress",
                "detection": "Ultrasonic testing (time-delay), visual inspection",
                "severity": "critical",
            },
            {
                "defect": "Lamellar tearing in thick sections",
                "cause": "Thick plate, high restraint, inadequate preheat",
                "detection": "Ultrasonic through-thickness testing, cross-section",
                "severity": "critical",
            },
        ],
        "environmental_requirements": {
            "temperature_min_celsius": 10,
            "temperature_max_celsius": 40,
            "humidity_max_percent": 75,
            "cure_time_hours": 0,
            "post_cure_temperature_celsius": 200,
            "post_cure_time_hours": 4,
        },
        "common_mistakes": [
            "Inadequate preheat for thicker plate",
            "PWHT (Post-Weld Heat Treatment) skipped or inadequate",
            "Wrong electrode type for application",
            "Too rapid cooling after welding",
            "Restraint design inadequate (excessive stress)",
        ],
        "inspection_points": [
            "Visual inspection (crack-free welds)",
            "Ultrasonic testing (internal defects, through-thickness)",
            "Radiography for porosity and inclusion",
            "Hardness profile across HAZ",
            "Hydrostatic pressure test",
        ],
    },
    "strip_plank_epoxy": {
        "quality_risks": [
            {
                "defect": "Plank cupping or warping",
                "cause": "Moisture uptake, inadequate epoxy seal, wood movement",
                "detection": "Visual inspection, moisture meter reading",
                "severity": "major",
            },
            {
                "defect": "Epoxy bond failure at plank interface",
                "cause": "Inadequate surface prep, wrong epoxy type, moisture",
                "detection": "Tap test (hollow sound), visual inspection, pull-off testing",
                "severity": "critical",
            },
        ],
        "environmental_requirements": {
            "temperature_min_celsius": 15,
            "temperature_max_celsius": 25,
            "humidity_max_percent": 65,
            "cure_time_hours": 24,
            "post_cure_temperature_celsius": None,
            "post_cure_time_hours": 0,
        },
        "common_mistakes": [
            "Planks with moisture content >12% before gluing",
            "Skipping or inadequate sanding between planks",
            "Using gap-filling epoxy on uneven surfaces",
            "Inadequate clamp pressure or uneven clamping",
            "Epoxy applied to only one mating surface",
        ],
        "inspection_points": [
            "Visual inspection of gaps (target <0.1mm)",
            "Bond line evaluation (no voids, solid color)",
            "Moisture meter verification on wood (target <12%)",
            "Tape test on epoxy (adhesion check)",
            "Cross-section examination of random planks",
        ],
    },
    "cold_molded": {
        "quality_risks": [
            {
                "defect": "Epoxy resin crack in outer laminate",
                "cause": "Shrinkage stress, UV exposure, inadequate fiber reinforcement",
                "detection": "Visual inspection, dye penetrant testing",
                "severity": "major",
            },
            {
                "defect": "Delamination between layers",
                "cause": "Inadequate epoxy application, moisture contamination",
                "detection": "Tap test, ultrasonic testing, cross-section",
                "severity": "critical",
            },
        ],
        "environmental_requirements": {
            "temperature_min_celsius": 15,
            "temperature_max_celsius": 25,
            "humidity_max_percent": 65,
            "cure_time_hours": 48,
            "post_cure_temperature_celsius": 60,
            "post_cure_time_hours": 8,
        },
        "common_mistakes": [
            "Epoxy ratio not precise (uncrosslinked resin)",
            "Core materials not properly saturated",
            "Inadequate compression of sandwich (voids remain)",
            "Applying outer laminate to uncured core",
            "No UV stabilization in outer layer (cracking)",
        ],
        "inspection_points": [
            "Visual inspection for cracks and delamination",
            "Tap test for void detection",
            "Cross-section analysis of layer bonding",
            "Laminate thickness and fiber volume fraction",
            "Mechanical testing of coupon samples",
        ],
    },
    "foam_sandwich": {
        "quality_risks": [
            {
                "defect": "Core crushing around fasteners",
                "cause": "Inadequate backing plates, high loads, inadequate core strength",
                "detection": "Visual inspection, pressure test, cross-section",
                "severity": "major",
            },
            {
                "defect": "Delamination at core-laminate interface",
                "cause": "Inadequate surface prep, resin starvation, core saturation",
                "detection": "Tap test, ultrasonic C-scan, pull-off testing",
                "severity": "critical",
            },
        ],
        "environmental_requirements": {
            "temperature_min_celsius": 18,
            "temperature_max_celsius": 28,
            "humidity_max_percent": 75,
            "cure_time_hours": 24,
            "post_cure_temperature_celsius": 60,
            "post_cure_time_hours": 12,
        },
        "common_mistakes": [
            "Core moisture content too high (>3% for PVC, >2% for PU)",
            "Resin application inadequate (starved bondline)",
            "Flat grain fabric on core surface (inadequate adhesion)",
            "Fastener backing plates too small or incompressible",
            "No vent holes for air escape during lamination",
        ],
        "inspection_points": [
            "Core moisture content verification",
            "Tap test over entire surface (no delamination)",
            "Pull-off test on core-to-laminate bond",
            "Cross-section of critical areas",
            "Fastener pull-out strength testing",
        ],
    },
}

# ============================================================================
# GALVANIC CORROSION TABLE
# ============================================================================

GALVANIC_CORROSION_TABLE = {
    "stainless_316_stainless_304": {"risk": "low", "voltage_diff_mv": 5, "notes": "Same passivation class, minimal risk in typical seawater"},
    "stainless_316_aluminum_5083": {"risk": "high", "voltage_diff_mv": 950, "notes": "One of worst pairs, avoid direct contact"},
    "stainless_316_aluminum_6082": {"risk": "high", "voltage_diff_mv": 960, "notes": "Extreme corrosion risk, use isolator"},
    "stainless_316_bronze": {"risk": "medium", "voltage_diff_mv": 120, "notes": "Manageable with isolators, typical through-hull design"},
    "stainless_316_brass": {"risk": "medium", "voltage_diff_mv": 140, "notes": "Dezincification possible, monitor for stress"},
    "stainless_316_carbon_fiber": {"risk": "high", "voltage_diff_mv": 800, "notes": "Composite cathode, rapid ss attack, avoid contact"},
    "stainless_316_copper": {"risk": "medium", "voltage_diff_mv": 280, "notes": "Moderate risk, use bedding compound isolation"},
    "stainless_316_zinc": {"risk": "high", "voltage_diff_mv": 1100, "notes": "Zinc sacrifices rapidly, design for replacement"},
    "stainless_316_mild_steel": {"risk": "high", "voltage_diff_mv": 500, "notes": "Steel corrodes rapidly, avoid any contact"},
    "stainless_316_titanium": {"risk": "none", "voltage_diff_mv": 50, "notes": "Noble passivation, minimal corrosion risk"},
    "stainless_316_lead": {"risk": "medium", "voltage_diff_mv": 250, "notes": "Rare pairing, moderate risk if present"},
    "stainless_316_monel": {"risk": "low", "voltage_diff_mv": 80, "notes": "Both noble, minimal electrochemical activity"},
    "aluminum_5083_zinc": {"risk": "high", "voltage_diff_mv": 200, "notes": "Aluminum becomes cathode, zinc sacrifices rapidly"},
    "aluminum_5083_bronze": {"risk": "high", "voltage_diff_mv": 1000, "notes": "One of worst combinations, extensive aluminum attack"},
    "aluminum_5083_carbon_fiber": {"risk": "high", "voltage_diff_mv": 1100, "notes": "Composite creates cathodic zone, severe attack"},
    "aluminum_5083_copper": {"risk": "high", "voltage_diff_mv": 1100, "notes": "Severe localized corrosion, use isolators"},
    "bronze_brass": {"risk": "medium", "voltage_diff_mv": 20, "notes": "Minor corrosion, usually acceptable"},
    "bronze_copper": {"risk": "low", "voltage_diff_mv": 50, "notes": "Similar potential, minimal risk"},
    "bronze_zinc": {"risk": "medium", "voltage_diff_mv": 1000, "notes": "Zinc sacrifices, useful for impressed current"},
    "brass_copper": {"risk": "low", "voltage_diff_mv": 30, "notes": "Similar passive films, low risk"},
    "brass_zinc": {"risk": "medium", "voltage_diff_mv": 1020, "notes": "Zinc becomes anode, useful in anodic protection"},
    "copper_carbon_fiber": {"risk": "high", "voltage_diff_mv": 850, "notes": "Carbon creates cathodic potential, copper attack"},
    "copper_zinc": {"risk": "medium", "voltage_diff_mv": 1050, "notes": "Zinc becomes anode, design consideration for propellers"},
    "carbon_fiber_aluminum_5083": {"risk": "high", "voltage_diff_mv": 1100, "notes": "Severe threat, avoid contact, use isolators"},
    "carbon_fiber_mild_steel": {"risk": "high", "voltage_diff_mv": 1000, "notes": "Rapid steel attack, requires complete isolation"},
    "carbon_fiber_stainless_316": {"risk": "high", "voltage_diff_mv": 800, "notes": "Stainless pitting risk, avoid direct contact"},
}

# ============================================================================
# JOINT FAILURE MODES
# ============================================================================

JOINT_FAILURE_MODES = {
    "hull_deck_joint": {
        "failure_modes": [
            {
                "mode": "Caulk deterioration and water leakage",
                "severity": "major",
                "onset_years": 5,
                "symptoms": "Water staining on cabin ceiling, musty smell, interior mold",
                "boat_classes_most_affected": ["all"],
            },
            {
                "mode": "Joint delamination from stress concentration",
                "severity": "critical",
                "onset_years": 8,
                "symptoms": "Visible separation at joint line, soft spots, large cracks",
                "boat_classes_most_affected": ["racing_sail", "small_sail"],
            },
        ],
        "inspection_protocol": "Annual visual inspection of entire joint line. Tracer dye testing every 3 years. Water spray testing before seasonal use. Sound bond line with borescope inspection every 5 years.",
        "recommended_materials": "Polyurethane adhesive sealant (3M 5200 or equivalent), fiberglass reinforced nylon backing, stainless fasteners with nylon washers",
    },
    "keel_hull_joint": {
        "failure_modes": [
            {
                "mode": "Fatigue cracking at fillet radius",
                "severity": "critical",
                "onset_years": 6,
                "symptoms": "Visible cracks radiating from junction, white stress marks",
                "boat_classes_most_affected": ["racing_sail", "small_sail", "daysailer"],
            },
            {
                "mode": "Keel movement and micro-fracture progression",
                "severity": "critical",
                "onset_years": 8,
                "symptoms": "Keel shifts laterally, interior ceiling cracks, water intrusion",
                "boat_classes_most_affected": ["cruising_sail", "motorsailer"],
            },
        ],
        "inspection_protocol": "Annual visual inspection of fillet radius. Ultrasonic thickness testing annually on older boats (>10 years). Dye penetrant testing every 3 years. Underwater video inspection every 5 years.",
        "recommended_materials": "High-strength structural epoxy (West System 105/209 or equivalent), extensive fillet radius (R≥30mm), multiple directional fiber lay-up",
    },
    "through_hull_fitting": {
        "failure_modes": [
            {
                "mode": "Sealant degradation and water intrusion",
                "severity": "critical",
                "onset_years": 4,
                "symptoms": "Water weeping around fitting, corrosion deposits, interior staining",
                "boat_classes_most_affected": ["all"],
            },
            {
                "mode": "Fitting corrosion and fastener seizure",
                "severity": "major",
                "onset_years": 5,
                "symptoms": "White corrosion deposits, fastener rust, difficult removal",
                "boat_classes_most_affected": ["all"],
            },
        ],
        "inspection_protocol": "Annual visual inspection for corrosion. Water spray test annually. Check seacock operation semi-annually. Valve removal and inspection every 5 years.",
        "recommended_materials": "Polysulfide or polyurethane bedding compound, stainless through-hull fittings, marine-grade sealant (3M 5200 or Sikaflex 291)",
    },
    "window_frame": {
        "failure_modes": [
            {
                "mode": "Elastomer gasket degradation and water leakage",
                "severity": "major",
                "onset_years": 7,
                "symptoms": "Water dripping, fogging between panes, interior moisture damage",
                "boat_classes_most_affected": ["all"],
            },
            {
                "mode": "Glass stress cracking and spontaneous fracture",
                "severity": "critical",
                "onset_years": 8,
                "symptoms": "Stress cracks visible, spontaneous breakage possible",
                "boat_classes_most_affected": ["all"],
            },
        ],
        "inspection_protocol": "Annual visual inspection for cracks and seal degradation. Water spray test every 2 years. Glass tap test for internal stress. Seal replacement every 7-10 years.",
        "recommended_materials": "EPDM or neoprene gasket (shore A 50-60), polyurethane glazing compound, tempered or laminated glass with protective edge",
    },
    "hatch_seal": {
        "failure_modes": [
            {
                "mode": "Gasket compression set and permanent deformation",
                "severity": "major",
                "onset_years": 6,
                "symptoms": "Hatch will not seal completely, water entry during rain",
                "boat_classes_most_affected": ["all"],
            },
            {
                "mode": "Hatch frame delamination from core saturation",
                "severity": "major",
                "onset_years": 7,
                "symptoms": "Hatch flexes excessively, water weeping, interior soft spots",
                "boat_classes_most_affected": ["all"],
            },
        ],
        "inspection_protocol": "Annual visual inspection of seal condition. Water spray test before season. Gasket replacement every 5-7 years. Frame integrity check every 3 years.",
        "recommended_materials": "EPDM gasket (shore A 40-50), polyurethane frame construction, aluminum frame with good UV protection",
    },
    "chainplate_bulkhead": {
        "failure_modes": [
            {
                "mode": "Core crush and delamination under load",
                "severity": "major",
                "onset_years": 6,
                "symptoms": "Chainplate loosens, cracks in surrounding laminate",
                "boat_classes_most_affected": ["racing_sail", "cruising_sail"],
            },
            {
                "mode": "Crevice corrosion at fastener-stainless interface",
                "severity": "major",
                "onset_years": 5,
                "symptoms": "White corrosion deposits, fastener seizure",
                "boat_classes_most_affected": ["all"],
            },
        ],
        "inspection_protocol": "Annual tightness check of all fasteners. Visual inspection for corrosion. Crevice corrosion monitoring with resistance measurement. Fastener removal and inspection every 3 years.",
        "recommended_materials": "Stainless 316 chainplate and fasteners, nylon washers and bushings, polyurethane or epoxy sealant compound",
    },
    "mast_step_beam": {
        "failure_modes": [
            {
                "mode": "Compression failure in beam under mast load",
                "severity": "critical",
                "onset_years": 9,
                "symptoms": "Visible compression lines in beam, soft spots when pressed",
                "boat_classes_most_affected": ["racing_sail", "cruising_sail"],
            },
            {
                "mode": "Fatigue cracking at collar interface",
                "severity": "critical",
                "onset_years": 7,
                "symptoms": "Visible cracks around mast collar, white stress marks",
                "boat_classes_most_affected": ["racing_sail"],
            },
        ],
        "inspection_protocol": "Annual visual inspection of collar interface. Ultrasonic testing of beam annually. Physical pressure test for soft spots. Detailed inspection every 3 years.",
        "recommended_materials": "High-density wood or carbon fiber reinforced composite, stainless mast collar, epoxy structural adhesive",
    },
    "rudder_bearing": {
        "failure_modes": [
            {
                "mode": "Bearing material corrosion and wear",
                "severity": "major",
                "onset_years": 7,
                "symptoms": "Rudder hard to turn, excessive play develops",
                "boat_classes_most_affected": ["all"],
            },
            {
                "mode": "Water seal failure and interior flooding",
                "severity": "critical",
                "onset_years": 6,
                "symptoms": "Water dripping into cabin, oil contamination",
                "boat_classes_most_affected": ["all"],
            },
        ],
        "inspection_protocol": "Annual rudder movement test. Visual inspection for water intrusion. Bearing wear measurement every 3 years. Seal replacement every 5-7 years.",
        "recommended_materials": "Bronze bearing material, stainless water seal, grease-packed design, regular lubrication schedule",
    },
    "propshaft_seal": {
        "failure_modes": [
            {
                "mode": "Seal degradation and water intrusion into engine room",
                "severity": "critical",
                "onset_years": 5,
                "symptoms": "Water pooling in engine room, oil leakage",
                "boat_classes_most_affected": ["large_motor", "motorsailer"],
            },
            {
                "mode": "Bearing corrosion from water ingress",
                "severity": "critical",
                "onset_years": 6,
                "symptoms": "Shaft runout increases, noise develops, bearing temperature rises",
                "boat_classes_most_affected": ["all"],
            },
        ],
        "inspection_protocol": "Monthly water level check in engine room. Annual seal inspection. Bearing noise monitoring during operation. Seal replacement every 5 years or as needed.",
        "recommended_materials": "PTFE and elastomer seal combination, stainless shaft, bronze bearing, regular lubrication",
    },
    "fuel_tank_mount": {
        "failure_modes": [
            {
                "mode": "Fastener corrosion and tank shift",
                "severity": "major",
                "onset_years": 4,
                "symptoms": "Tank vibrates, fasteners corrode, fuel smell increases",
                "boat_classes_most_affected": ["all"],
            },
            {
                "mode": "Elastomer mounting block degradation",
                "severity": "minor",
                "onset_years": 6,
                "symptoms": "Increased vibration, rubber hardened or cracked",
                "boat_classes_most_affected": ["all"],
            },
        ],
        "inspection_protocol": "Quarterly tightness check of all fasteners. Annual visual inspection for corrosion. Elastomer condition check every 3 years. Mounting block replacement every 7-10 years.",
        "recommended_materials": "Stainless fasteners with nylon bushings, neoprene elastomer blocks, stainless straps",
    },
    "battery_mount": {
        "failure_modes": [
            {
                "mode": "Fastener corrosion and battery shift",
                "severity": "minor",
                "onset_years": 3,
                "symptoms": "Corrosion deposits visible, battery moves slightly",
                "boat_classes_most_affected": ["all"],
            },
            {
                "mode": "Tray bottom erosion from acid spill",
                "severity": "minor",
                "onset_years": 5,
                "symptoms": "Tray material eroded, potential battery acid exposure",
                "boat_classes_most_affected": ["all"],
            },
        ],
        "inspection_protocol": "Quarterly fastener check and tightness. Annual acid spill inspection and neutralization. Battery area cleanliness monthly. Tray replacement every 10 years or as needed.",
        "recommended_materials": "Stainless fasteners, polypropylene or fiberglass tray, nylon bushings, anti-vibration rubber feet",
    },
}

# ============================================================================
# WEAR PATTERN DATABASE
# ============================================================================

WEAR_PATTERN_DATABASE = [
    {
        "zone": "hull_below_waterline",
        "component": "Gelcoat",
        "wear_type": "osmotic_blistering",
        "typical_lifespan_years": 8,
        "early_warning_signs": "Small pinpoint blisters appearing in clusters, white crystalline deposits",
        "affected_boat_classes": ["cruising_sail", "large_motor", "motorsailer"],
    },
    {
        "zone": "hull_below_waterline",
        "component": "Through-hull fitting seal",
        "wear_type": "corrosion",
        "typical_lifespan_years": 4,
        "early_warning_signs": "White corrosion deposits, staining around fitting, water weeping",
        "affected_boat_classes": ["all"],
    },
    {
        "zone": "hull_above_waterline",
        "component": "Sheer strake gelcoat",
        "wear_type": "UV_degradation",
        "typical_lifespan_years": 5,
        "early_warning_signs": "Color fading, dull appearance, fine hairline cracks in surface",
        "affected_boat_classes": ["all"],
    },
    {
        "zone": "deck",
        "component": "Stanchion base",
        "wear_type": "creep_and_corrosion",
        "typical_lifespan_years": 6,
        "early_warning_signs": "Base loosens gradually, cracks appear around fasteners",
        "affected_boat_classes": ["all"],
    },
    {
        "zone": "deck",
        "component": "Hatch gasket",
        "wear_type": "compression_set",
        "typical_lifespan_years": 7,
        "early_warning_signs": "Hatch seal becomes less tight, water entry during heavy rain",
        "affected_boat_classes": ["all"],
    },
    {
        "zone": "keel",
        "component": "Keel fillet radius",
        "wear_type": "fatigue",
        "typical_lifespan_years": 7,
        "early_warning_signs": "Stress cracks visible at fillet, white lines in gelcoat",
        "affected_boat_classes": ["racing_sail", "small_sail"],
    },
    {
        "zone": "rudder",
        "component": "Rudder bearing",
        "wear_type": "abrasion",
        "typical_lifespan_years": 8,
        "early_warning_signs": "Rudder becomes harder to turn, develops play side-to-side",
        "affected_boat_classes": ["all"],
    },
    {
        "zone": "window",
        "component": "Elastomer gasket",
        "wear_type": "UV_and_ozone",
        "typical_lifespan_years": 8,
        "early_warning_signs": "Rubber becomes stiff and brittle, loses grip on frame",
        "affected_boat_classes": ["all"],
    },
    {
        "zone": "rigging",
        "component": "Stainless swage termination",
        "wear_type": "crevice_corrosion",
        "typical_lifespan_years": 7,
        "early_warning_signs": "Corrosion deposits visible at swage, discoloration of wire",
        "affected_boat_classes": ["all"],
    },
    {
        "zone": "engine_room",
        "component": "Engine mount rubber",
        "wear_type": "chemical_degradation",
        "typical_lifespan_years": 6,
        "early_warning_signs": "Rubber hardens and cracks, vibration increases",
        "affected_boat_classes": ["all"],
    },
    {
        "zone": "hull_below_waterline",
        "component": "Propeller shaft bearing",
        "wear_type": "corrosion",
        "typical_lifespan_years": 7,
        "early_warning_signs": "Excessive shaft runout, bearing noise, water intrusion",
        "affected_boat_classes": ["all"],
    },
    {
        "zone": "cockpit",
        "component": "Winch drum",
        "wear_type": "abrasion",
        "typical_lifespan_years": 10,
        "early_warning_signs": "Groove development in drum, rope slipping",
        "affected_boat_classes": ["racing_sail", "cruising_sail"],
    },
    {
        "zone": "mast_step",
        "component": "Mast collar laminate",
        "wear_type": "fatigue",
        "typical_lifespan_years": 8,
        "early_warning_signs": "Cracks radiating from mast tube, mast side play develops",
        "affected_boat_classes": ["racing_sail", "cruising_sail"],
    },
    {
        "zone": "fuel_system",
        "component": "Fuel hose",
        "wear_type": "chemical_degradation",
        "typical_lifespan_years": 10,
        "early_warning_signs": "Hose becomes stiff, cracks develop, fuel smell increases",
        "affected_boat_classes": ["all"],
    },
    {
        "zone": "electrical",
        "component": "Battery terminal corrosion",
        "wear_type": "galvanic_corrosion",
        "typical_lifespan_years": 3,
        "early_warning_signs": "Green/white corrosion deposits on terminals, hard starting",
        "affected_boat_classes": ["all"],
    },
    {
        "zone": "chainplate",
        "component": "Fastener hole",
        "wear_type": "crevice_corrosion",
        "typical_lifespan_years": 5,
        "early_warning_signs": "White deposits around fasteners, fastener becomes hard to turn",
        "affected_boat_classes": ["all"],
    },
    {
        "zone": "hull_deck_joint",
        "component": "Polyurethane sealant",
        "wear_type": "UV_degradation",
        "typical_lifespan_years": 6,
        "early_warning_signs": "Sealant becomes hard and brittle, cracks appear, water leakage starts",
        "affected_boat_classes": ["all"],
    },
    {
        "zone": "transom",
        "component": "Engine mounting pad",
        "wear_type": "corrosion",
        "typical_lifespan_years": 5,
        "early_warning_signs": "Fasteners corrode, engine mounting becomes loose",
        "affected_boat_classes": ["all"],
    },
    {
        "zone": "anchor_locker",
        "component": "Anchor chain contact area",
        "wear_type": "abrasion",
        "typical_lifespan_years": 10,
        "early_warning_signs": "Gelcoat worn thin, exposed fibers visible",
        "affected_boat_classes": ["all"],
    },
    {
        "zone": "cabin_top",
        "component": "Caulk line",
        "wear_type": "UV_and_weathering",
        "typical_lifespan_years": 6,
        "early_warning_signs": "Caulk cracks and separates, water staining below visible",
        "affected_boat_classes": ["all"],
    },
]

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================


def get_weakpoints_for_boat(boat_class: str, zones: List[str]) -> Dict[str, Any]:
    """
    Filter construction weak points by boat class and present zones.

    Args:
        boat_class: Type of boat (e.g., 'cruising_sail', 'large_motor')
        zones: List of zone types present in the layout (e.g., ['hull_below_waterline', 'deck'])

    Returns:
        Dictionary containing filtered weak points relevant to the boat and zones
    """
    result = {
        "boat_class": boat_class,
        "zones_present": zones,
        "critical_areas": [],
        "water_ingress_vectors": [],
        "chafing_zones": [],
        "relevant_construction_methods": [],
        "material_pairing_risks": [],
        "wear_patterns": [],
        "summary": {},
    }

    # Filter critical areas by zone
    for zone in zones:
        if zone in ZONE_WEAKPOINTS:
            zone_data = ZONE_WEAKPOINTS[zone]

            # Filter critical areas by boat class
            for critical_area in zone_data.get("critical_areas", []):
                if boat_class in critical_area.get("affected_boat_classes", ["all"]) or \
                   "all" in critical_area.get("affected_boat_classes", []):
                    result["critical_areas"].append({
                        "zone": zone,
                        **critical_area,
                    })

            # Add water ingress vectors for this zone
            result["water_ingress_vectors"].extend([
                {"zone": zone, **vector}
                for vector in zone_data.get("water_ingress_vectors", [])
            ])

            # Add chafing zones for this zone
            result["chafing_zones"].extend([
                {"zone": zone, **chafe}
                for chafe in zone_data.get("chafing_zones", [])
            ])

    # Filter wear patterns by boat class
    for wear_pattern in WEAR_PATTERN_DATABASE:
        if any(z in [wear_pattern["zone"]] for z in zones):
            if boat_class in wear_pattern.get("affected_boat_classes", ["all"]) or \
               "all" in wear_pattern.get("affected_boat_classes", []):
                result["wear_patterns"].append(wear_pattern)

    # Generate summary statistics
    critical_count = sum(1 for ca in result["critical_areas"] if ca["severity"] == "critical")
    major_count = sum(1 for ca in result["critical_areas"] if ca["severity"] == "major")

    result["summary"] = {
        "total_critical_areas": len(result["critical_areas"]),
        "critical_severity_count": critical_count,
        "major_severity_count": major_count,
        "water_ingress_vectors_count": len(result["water_ingress_vectors"]),
        "chafing_zones_count": len(result["chafing_zones"]),
        "wear_patterns_count": len(result["wear_patterns"]),
        "priority_focus_areas": [
            ca for ca in result["critical_areas"]
            if ca["severity"] == "critical"
        ][:5],  # Top 5 critical areas
    }

    return result


def get_joint_inspection_schedule(joint_type: str, boat_class: str) -> Dict[str, Any]:
    """
    Get recommended inspection schedule for a specific joint type.

    Args:
        joint_type: Type of joint (e.g., 'hull_deck_joint')
        boat_class: Type of boat

    Returns:
        Dictionary with inspection schedule and protocols
    """
    if joint_type not in JOINT_FAILURE_MODES:
        return {"error": f"Unknown joint type: {joint_type}"}

    joint_data = JOINT_FAILURE_MODES[joint_type]

    return {
        "joint_type": joint_type,
        "boat_class": boat_class,
        "failure_modes": joint_data.get("failure_modes", []),
        "inspection_protocol": joint_data.get("inspection_protocol", ""),
        "recommended_materials": joint_data.get("recommended_materials", ""),
    }


def assess_galvanic_risk(material_1: str, material_2: str) -> Optional[Dict[str, Any]]:
    """
    Assess galvanic corrosion risk between two materials.

    Args:
        material_1: First material identifier
        material_2: Second material identifier

    Returns:
        Dictionary with risk assessment or None if pairing not found
    """
    # Try both orderings
    for pair_key in [f"{material_1}_{material_2}", f"{material_2}_{material_1}"]:
        if pair_key in GALVANIC_CORROSION_TABLE:
            return {
                "material_pair": pair_key,
                **GALVANIC_CORROSION_TABLE[pair_key],
            }

    return None


def get_construction_method_risks(method: str) -> Optional[Dict[str, Any]]:
    """
    Get quality risks and requirements for a specific construction method.

    Args:
        method: Construction method identifier

    Returns:
        Dictionary with method-specific risks and requirements
    """
    if method not in CONSTRUCTION_METHOD_RISKS:
        return None

    return {
        "construction_method": method,
        **CONSTRUCTION_METHOD_RISKS[method],
    }


__all__ = [
    "ZONE_WEAKPOINTS",
    "CONSTRUCTION_METHOD_RISKS",
    "GALVANIC_CORROSION_TABLE",
    "JOINT_FAILURE_MODES",
    "WEAR_PATTERN_DATABASE",
    "get_weakpoints_for_boat",
    "get_joint_inspection_schedule",
    "assess_galvanic_risk",
    "get_construction_method_risks",
]
