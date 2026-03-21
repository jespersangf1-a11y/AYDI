"""
AYDI Yacht Rigg- und Segelsysteme Knowledge Base
Rigging, standing rigging, running rigging and sail systems

Rigging ist das Skelett eines Segelschiffes.
Standing rigging (stehendes Gut) trägt Mast- und Baumlasten.
Running rigging (laufendes Gut) kontrolliert Segel.

Master Marine Rigger KnowledgeBase
Version: 1.0
Scope: Racing/Cruising Sailyachts 30-100ft
Author: AYDI Marine Engineering
"""

from typing import Dict, List, Any, Tuple

# ============================================================================
# STANDING_RIGGING — Stehendes Gut (statische Rigg-Komponenten)
# ============================================================================

STANDING_RIGGING: Dict[str, Dict[str, Any]] = {
    "1x19_stainless_wire": {
        "name": "1x19 Stainless Steel Wire",
        "german_name": "1x19 Edelstahl Drahtseil",
        "material_spec": "AISI 316L stainless steel, non-rotating",
        "construction": "7 strands around a rope core",
        "breaking_load_table_mm": {
            "3.2": 1580,      # kg
            "4.0": 2480,
            "5.0": 3880,
            "6.0": 5600,
            "8.0": 9900,
            "10.0": 15500,
            "12.0": 22400,
        },
        "stretch_percent": 3.5,
        "weight_per_meter_kg": {
            "4.0": 0.043,
            "5.0": 0.067,
            "6.0": 0.096,
            "8.0": 0.171,
            "10.0": 0.268,
        },
        "uv_resistance": "Excellent (stainless)",
        "fatigue_life_cycles": 100000,
        "inspection_method": "Visual for rust/corrosion, wire pulls at swage points",
        "typical_replacement_interval_years": 15,
        "terminal_types": ["Swage fitting 1/4\" cone", "T-ball", "Eye"],
        "cost_factor": 1.0,
        "failure_modes": [
            "Crevice corrosion at swage (poor drainage)",
            "Stress concentration at ball/eye junction",
            "Fatigue at spreader brackets",
            "Galvanic corrosion if mixed with aluminum",
        ],
        "notes": "Industry standard. Cost-effective. Highly reliable. Subject to crevice corrosion if not well-sealed.",
    },

    "rod_rigging_navtec": {
        "name": "Rod Rigging (Navtec Nitronic 50)",
        "german_name": "Stabrgg (Navtec Nitronic 50)",
        "material_spec": "Nitronic 50 (25Mn-5Cr-2Ni-0.32N stainless alloy)",
        "construction": "Solid bar, 0.75-1.50\" OD, threaded ends",
        "breaking_load_table_diameter": {
            "0.75_inch": 6200,  # kg
            "1.0_inch": 11000,
            "1.25_inch": 17200,
            "1.5_inch": 24800,
        },
        "stretch_percent": 0.8,
        "weight_per_meter_kg": {
            "0.75_inch": 0.35,
            "1.0_inch": 0.63,
            "1.25_inch": 0.98,
            "1.5_inch": 1.41,
        },
        "uv_resistance": "N/A (internal component)",
        "fatigue_life_cycles": 500000,
        "inspection_method": "Thread inspection, magnetic particle testing for micro-cracks",
        "typical_replacement_interval_years": 20,
        "terminal_types": ["Norseman fitting", "Sta-Lok", "Hi-Mod fork"],
        "cost_factor": 3.5,
        "failure_modes": [
            "Thread galling during installation (requires anti-seize)",
            "Corrosion pitting under terminals if not sealed",
            "Fatigue failure at thread runout",
            "Galvanic reaction with aluminum mast",
        ],
        "brands": ["Navtec", "Schaefer", "Southern Spars"],
        "notes": "Premium choice. Zero stretch (maintains mast shape). Requires careful installation. Excellent for racing.",
    },

    "dyform_wire": {
        "name": "Dyform Stainless Wire",
        "german_name": "Dyform Draht (gepresst)",
        "material_spec": "AISI 316 stainless, mechanically formed",
        "construction": "7x7 or 7x19 compacted, elliptical/round shaped wires",
        "breaking_load_table_mm": {
            "5.0": 4200,
            "6.0": 6000,
            "8.0": 10700,
            "10.0": 16700,
        },
        "stretch_percent": 2.5,
        "weight_per_meter_kg": {
            "5.0": 0.085,
            "6.0": 0.122,
            "8.0": 0.217,
            "10.0": 0.340,
        },
        "uv_resistance": "Excellent",
        "fatigue_life_cycles": 150000,
        "inspection_method": "Visual kinking, pull test at terminals",
        "typical_replacement_interval_years": 12,
        "terminal_types": ["Sta-Lok", "Norseman", "Swage"],
        "cost_factor": 1.8,
        "failure_modes": [
            "Kinking under lateral load",
            "Creep under sustained tension",
            "Lower fatigue tolerance than rod",
        ],
        "brands": ["Wirerope Works", "English Braiding"],
        "notes": "Better than 1x19 in fatigue. Lower stretch than wire. Intermediate cost/performance.",
    },

    "pbo_zylon_wire": {
        "name": "PBO (Zylon) Rigging Wire",
        "german_name": "PBO (Zylon) Rigg",
        "material_spec": "Para-phenylene benzobisoxazole fiber in aramid yarn matrix",
        "construction": "High-modulus fiber cables, 6-8mm diameter",
        "breaking_load_table_mm": {
            "6.0": 3500,
            "8.0": 6200,
            "10.0": 9700,
        },
        "stretch_percent": 1.8,
        "weight_per_meter_kg": {
            "6.0": 0.032,
            "8.0": 0.057,
            "10.0": 0.089,
        },
        "uv_resistance": "Poor (requires UV sleeve or cover)",
        "fatigue_life_cycles": 80000,
        "inspection_method": "Fiber crimp inspection, strength test",
        "typical_replacement_interval_years": 8,
        "terminal_types": ["Adhesive-bonded swage", "Hi-Mod eye"],
        "cost_factor": 5.2,
        "failure_modes": [
            "UV degradation (critical: needs full UV protection)",
            "Moisture absorption reduces strength 20%",
            "Abrasion at spreaders and mast contact",
            "Stress concentration at adhesive layer",
        ],
        "brands": ["Pinnell & Bax", "Hydra Sports"],
        "notes": "Ultra-lightweight, high-modulus. Requires disciplined maintenance. Racing only. Performance degrades rapidly without UV protection.",
    },

    "dynex_dux_dyneema": {
        "name": "Dynex Dux (Dyneema SK99) Synthetic Rigging",
        "german_name": "Dynex Dux (HMPE Rigg)",
        "material_spec": "Ultra-high-molecular-weight polyethylene (Dyneema SK99)",
        "construction": "Braided synthetic yarn, 10-15mm diameter",
        "breaking_load_table_mm": {
            "8.0": 2800,
            "10.0": 4400,
            "12.0": 6300,
            "14.0": 8600,
        },
        "stretch_percent": 2.2,
        "weight_per_meter_kg": {
            "8.0": 0.028,
            "10.0": 0.043,
            "12.0": 0.062,
        },
        "uv_resistance": "Moderate (carbon black additives help)",
        "fatigue_life_cycles": 120000,
        "inspection_method": "Visual fiber crimp, pull-through test at sheaves",
        "typical_replacement_interval_years": 10,
        "terminal_types": ["Hi-Mod eye", "Adhesive swage", "Spliced eye"],
        "cost_factor": 4.8,
        "failure_modes": [
            "Creep under sustained load (5-10% over 5 years)",
            "Melting point only 150°C (chafe risk)",
            "Poor fatigue under bending loads",
            "Knots reduce strength 50%",
        ],
        "brands": ["Hall Spars", "Southern Spars"],
        "notes": "1/3 weight of wire equivalent. Good for cruising/light racing. Creep requires periodic tensioning. Avoid high-load halyards.",
    },

    "carbon_fiber_rigging": {
        "name": "Carbon Fiber Rod Rigging",
        "german_name": "Kohlefaser-Stabrgg",
        "material_spec": "Carbon fiber epoxy composite, hollow or solid",
        "construction": "Pultruded rod, 12-25mm diameter",
        "breaking_load_table_mm": {
            "12.0": 4200,
            "14.0": 5700,
            "16.0": 7500,
            "18.0": 9600,
        },
        "stretch_percent": 0.3,
        "weight_per_meter_kg": {
            "12.0": 0.11,
            "14.0": 0.15,
            "16.0": 0.19,
            "18.0": 0.25,
        },
        "uv_resistance": "Poor (requires epoxy protection)",
        "fatigue_life_cycles": 200000,
        "inspection_method": "Ultrasonic for delamination, visual for cracking",
        "typical_replacement_interval_years": 18,
        "terminal_types": ["Carbon compression fittings", "Fork/eye adhesive"],
        "cost_factor": 8.0,
        "failure_modes": [
            "Delamination from impact or fatigue",
            "Moisture ingress at terminal interfaces",
            "Buckling under compression (limited diagonal stays)",
            "High cost of replacement after damage",
        ],
        "brands": ["Hall Spars", "Sparcraft"],
        "notes": "Ultimate performance. Lowest weight. Highest cost. Brittle—requires careful handling. Reserved for racing machines.",
    },

    "galvanized_wire_traditional": {
        "name": "Galvanized Steel Wire (Traditional)",
        "german_name": "Verzinkt Stahldraht",
        "material_spec": "ASTM A363 galvanized steel, hot-dip or electro-plated",
        "construction": "6x19 IWRC or 7x19 construction",
        "breaking_load_table_mm": {
            "6.0": 4800,
            "8.0": 8500,
            "10.0": 13300,
            "12.0": 19200,
        },
        "stretch_percent": 5.0,
        "weight_per_meter_kg": {
            "6.0": 0.105,
            "8.0": 0.186,
            "10.0": 0.291,
            "12.0": 0.419,
        },
        "uv_resistance": "Good (zinc coating)",
        "fatigue_life_cycles": 60000,
        "inspection_method": "Corrosion assessment, strand count check",
        "typical_replacement_interval_years": 8,
        "terminal_types": ["Thimble + clamp", "Swaged Monel", "Loop splice"],
        "cost_factor": 0.4,
        "failure_modes": [
            "Rust at strand ends",
            "Fatigue at clamp transitions",
            "Galvanic corrosion with stainless fittings",
            "High weight",
        ],
        "notes": "Budget option. Heavy. Higher stretch. Suitable for cruising/traditional vessels. Proven reliability over decades.",
    },

    "discontinuous_rod_rigging": {
        "name": "Discontinuous Rod Rigging System",
        "german_name": "Diskontinuierliche Stabrgg",
        "material_spec": "Nitronic 50 rod segments connected with mechanical couplers",
        "construction": "1.0-1.25\" rod sections (3-5ft each) with fork/eye couplers",
        "breaking_load_table_section": {
            "1.0_inch": 11000,  # kg per section
            "1.25_inch": 17200,
        },
        "stretch_percent": 1.2,
        "weight_per_meter_kg": {
            "1.0_inch": 0.63,
            "1.25_inch": 0.98,
        },
        "uv_resistance": "N/A",
        "fatigue_life_cycles": 250000,
        "inspection_method": "Coupler tightness, thread inspection",
        "typical_replacement_interval_years": 15,
        "terminal_types": ["Fork coupler", "Toggle link"],
        "cost_factor": 2.8,
        "failure_modes": [
            "Coupler loosening due to vibration",
            "Corrosion pitting at coupler junctions",
            "Unequal load distribution between sections",
        ],
        "brands": ["Southern Spars", "Selden"],
        "notes": "Allows individual section replacement. Modular approach. Easier handling than full-length rod. Slight weight/cost premium.",
    },
}

# ============================================================================
# TERMINALS_AND_FITTINGS — Endverbindungen
# ============================================================================

TERMINALS_AND_FITTINGS: Dict[str, Dict[str, Any]] = {
    "swage_fitting": {
        "name": "Swage Fitting (Compression Terminal)",
        "german_name": "Pressklemmen-Endverbindung",
        "material": "17-4PH stainless steel or Monel alloy",
        "types": ["1/4\"-cone fork", "T-ball", "Open barrel eye"],
        "load_rating_percent": 100,
        "installation_method": "Hydraulic press (7-ton or 10-ton die set)",
        "installation_notes": "Permanent. No disassembly. Requires calibrated equipment.",
        "inspection_criteria": [
            "No visible gaps between cone and barrel",
            "Uniform radial compression (no flat spots)",
            "Wire protrusion: 0-3mm (measure flush)",
            "Pull-test minimum: 90% of wire breaking load",
        ],
        "failure_modes": [
            "Under-swaging: cone slips out under load",
            "Over-swaging: barrel splits, cone crushes wire",
            "Crevice corrosion inside terminal (stainless/saltwater)",
            "Stress riser: fatigue crack initiates at cone/barrel junction",
        ],
        "brands": ["Petro Industrial", "Nicopress", "Thomas & Betts"],
        "cost_per_terminal_usd": 12,
        "notes": "Industry standard for 1x19 wire. Irreversible. Must have correct press setting.",
    },

    "t_ball_terminal": {
        "name": "T-Ball Fitting (Navtec)",
        "german_name": "T-Kugel Endverbindung",
        "material": "316 stainless steel ball, 316 stainless body",
        "load_rating_percent": 95,
        "installation_method": "Swage or adhesive bond (epoxy)",
        "installation_notes": "Available for 4-10mm wire. Fits universal mast hardware.",
        "inspection_criteria": [
            "Ball rotation smooth but not loose",
            "No cracks in mounting barrel",
            "Visual wire compression (no gaps)",
        ],
        "failure_modes": [
            "Ball spins off under load (inadequate swage)",
            "Corrosion between ball and body",
            "Wire slips due to low barrel compression",
        ],
        "brands": ["Navtec", "Schaefer"],
        "cost_per_terminal_usd": 18,
        "notes": "Requires matching T-ball hardware (chainplates, spreader blocks). Quick/easy replacement.",
    },

    "sta_lok_mechanical": {
        "name": "Sta-Lok Mechanical Terminal",
        "german_name": "Sta-Lok Mechanische Endverbindung",
        "material": "316 stainless steel cone/wedge/body",
        "load_rating_percent": 95,
        "installation_method": "Manual assembly (hand tools, special tool required)",
        "installation_notes": "Tool: Sta-Lok installation wrench. Reusable/removable.",
        "assembly_steps": [
            "1. Strand the wire into die (6 strands per side for rod)",
            "2. Compress cone onto strands (hand tightening)",
            "3. Fit body over cone and threads",
            "4. Tighten to specified torque (typically 15-25 Nm)",
        ],
        "inspection_criteria": [
            "Cone sits flush in body (no gaps)",
            "Wire strands visible, compressed evenly",
            "Torque wrench confirmation: spec torque ±2 Nm",
            "Pull-test: 90%+ wire strength",
        ],
        "failure_modes": [
            "Under-tightening: cone pulls loose under load",
            "Over-tightening: body threads strip, cone crushes wire",
            "Corrosion (saltwater): wedge seizes, cannot remove",
            "Lateral load (sidestay): wedge shears under compression",
        ],
        "brands": ["Sta-Lok (UK)", "Breithorn"],
        "cost_per_terminal_usd": 35,
        "notes": "Reusable. Allows mid-season adjustments. Popular for DIY riggers. Requires discipline (torque spec critical).",
    },

    "norseman_terminal": {
        "name": "Norseman Mechanical Terminal",
        "german_name": "Norseman Mechanische Endverbindung",
        "material": "316/A4 stainless steel (cone, collet, body)",
        "load_rating_percent": 98,
        "installation_method": "Manual assembly with collet and cone",
        "installation_notes": "Removable/reusable. Works with rod or wire.",
        "assembly_steps": [
            "1. Thread rod/wire into body (hand-tight)",
            "2. Slide collet and cone assembly",
            "3. Tighten cap/cone using 2x wrench (body + cap)",
            "4. Full tightening: ~2-3 full turns after hand-tight",
        ],
        "inspection_criteria": [
            "Collet centered in body (no offset)",
            "Cone seated flush",
            "Wrench-tight confirmation (no slippage under load)",
            "Pull-test: 95%+ wire strength",
        ],
        "failure_modes": [
            "Under-tightening (most common): collet doesn't grip, terminal spins",
            "Over-tightening: collet splits, loses grip",
            "Saltwater corrosion: collet seizes",
            "Vibration: cap unscrews under motion",
        ],
        "brands": ["Norseman (Sweden/UK)", "Breithorn"],
        "cost_per_terminal_usd": 40,
        "notes": "Premium mechanical terminal. Superior fatigue tolerance. Requires wrench discipline and periodic re-tightening.",
    },

    "hi_mod_fork_terminal": {
        "name": "Hi-Mod Fork/Eye Terminal",
        "german_name": "Hi-Mod Gabel/Öse Endverbindung",
        "material": "Aluminum alloy or stainless steel body, various pin options",
        "load_rating_percent": 92,
        "installation_method": "Adhesive epoxy or mechanical swage hybrid",
        "installation_notes": "Compatible with rod, wire, and synthetic. Accepts clevis pins.",
        "pin_types": ["Stainless steel 1/4\" pin", "Toggle pins", "Spring-loaded pins"],
        "inspection_criteria": [
            "Adhesive fully cured (7 days): no movement under hand force",
            "Pin in place with cotter pin/lock washer",
            "No cracks in arms",
            "Bend/torque test: no deformation",
        ],
        "failure_modes": [
            "Adhesive bond failure (insufficient cure, contamination)",
            "Pin shear under lateral load (single-shear design)",
            "Crack propagation from pin hole radius",
            "Corrosion at epoxy/metal interface",
        ],
        "brands": ["Samson", "Admiral", "Ronstan"],
        "cost_per_terminal_usd": 28,
        "notes": "Hybrid design. Removable. Excellent for mixed rigging. Pin failure is limiting factor (single-shear).",
    },

    "rigging_screw_turnbuckle": {
        "name": "Rigging Screw / Turnbuckle",
        "german_name": "Riggschraube / Spannschraube",
        "material": "316 stainless steel (body, screws, clevis pin)",
        "load_rating_table_inch": {
            "1/4\"": 2200,  # kg safe working load
            "5/16\"": 3500,
            "3/8\"": 5000,
            "1/2\"": 8800,
        },
        "installation_method": "Threaded eyes or forks onto both ends",
        "installation_notes": "Typical preload (shrouds): 15-25% of breaking load",
        "adjustment_procedure": [
            "1. Measure baseline length (mast vertical, no trim)",
            "2. Adjust 1/4 turn at a time",
            "3. Retension: check mast straightness with level",
            "4. Lock clevis pin with cotter pin or wire (essential)",
        ],
        "inspection_criteria": [
            "Cotter pin in place and spread",
            "No rotation under hand pressure",
            "Screw threads clean (no corrosion lock-up)",
            "Eye/fork pins free of play",
        ],
        "failure_modes": [
            "Lost cotter pin: screw unscrews under vibration",
            "Thread seizing (galvanic corrosion)",
            "Clevis pin shear under cyclic load",
            "Body cracking from over-tension",
        ],
        "brands": ["Schaefer", "Harken", "Lewmar"],
        "cost_per_unit_usd": 45,
        "notes": "Adjustable. Allows in-season trim refinement. Cotter pin discipline critical. Inspect quarterly.",
    },

    "toggle_link": {
        "name": "Toggle Link (Articulated Joint)",
        "german_name": "Gelenkverbindung / Toggle",
        "material": "316 stainless steel (2x articulated links)",
        "load_rating": "Rated for rope eye or terminal pin",
        "installation_method": "Pins/fasteners at each joint",
        "installation_notes": "Reduces bending loads on adjacent fittings",
        "function": "Absorbs misalignment, converts bending moment to axial load",
        "inspection_criteria": [
            "Pin rotation smooth (lubricate if stiff)",
            "No visible cracks at pin holes",
            "Wire protection: edges chamfered",
        ],
        "failure_modes": [
            "Pin seizing under corrosion",
            "Crack initiation at pin hole stress concentration",
            "Loss of articulation (rigidity increases bending load)",
        ],
        "brands": ["Schaefer", "Antal"],
        "cost_per_unit_usd": 22,
        "notes": "Used on diagonals, lower caps. Prolongs rigging life by reducing secondary bending.",
    },

    "clevis_pin": {
        "name": "Clevis Pin (Fastener)",
        "german_name": "Splintstift / Klappsplint",
        "material": "316 stainless steel, NACA standard shank",
        "diameter_options": ["1/4\"", "5/16\"", "3/8\""],
        "installation_notes": "Requires cotter pin or lock washer as retainer",
        "inspection_criteria": [
            "Cotter pin fully spread and visible",
            "Pin shank free of corrosion/galling",
            "No movement when hand-shaken",
        ],
        "failure_modes": [
            "Cotter pin lost: pin backs out",
            "Shear failure under shock load",
            "Corrosion seizing (saltwater without O-ring)",
        ],
        "cost_per_pin_usd": 3,
        "notes": "Critical item—carry spares. Single-shear design limits load. Check weekly.",
    },

    "split_pin_cotter_pin": {
        "name": "Split Pin / Cotter Pin (Retainer)",
        "german_name": "Splintsicherung / Splint",
        "material": "316 stainless steel, wire diameter 1.2-2.4mm",
        "standard": "DIN 94 or ISO 1234",
        "installation_procedure": [
            "1. Insert through clevis pin hole",
            "2. Spread legs 45° apart (even pressure)",
            "3. Trim excess (1-2mm beyond pin eye)",
            "4. Tap flat with hammer to prevent snagging",
        ],
        "inspection_criteria": [
            "Legs fully spread and separated",
            "No corrosion at fold point (stress concentration)",
            "Seated flush in pin eye",
        ],
        "failure_modes": [
            "Insufficient spread: pin backs out under vibration",
            "Over-trimming: pin falls out of hole",
            "Corrosion at fold: leg breaks, pin lost",
        ],
        "cost_per_pin_usd": 0.25,
        "notes": "Consumable item. Carry 20+ spares. Critical safety item. Inspect before every passage.",
    },
}

# ============================================================================
# RUNNING_RIGGING — Laufendes Gut (dynamische Rigg-Komponenten)
# ============================================================================

RUNNING_RIGGING: Dict[str, Dict[str, Any]] = {
    "main_halyard": {
        "name": "Main Halyard",
        "german_name": "Großfall",
        "function": "Raises main sail (static vertical load + swinging moment at hoist)",
        "material_recommendation": ["Dyneema SK75 braid", "Vectran", "High-modulus polyester"],
        "diameter_by_boat_length": {
            "30ft": "8-10mm",
            "40ft": "10-12mm",
            "50ft": "12-14mm",
            "65ft": "14-16mm",
        },
        "construction": "Single braid (less stretch) or braid-on-braid (easier handling)",
        "breaking_load_target": "2x sail area × 10 kg/m² (racing) to 1.5x (cruising)",
        "clutch_compatibility": "Spinlock HS 10-16 or Antal HT winch cleat",
        "winch_sizing": "Halyard winch: power ratio 6:1 minimum",
        "chafe_points": [
            "Mast cap sheave (wrap with batten tape)",
            "Upper spreader contact (avoid if possible)",
            "Cleat exit (edge radius >10mm required)",
        ],
        "replacement_signs": [
            "Fuzz/fluffing on surface (UV damage)",
            "Loss of gloss/sheen (oxidation)",
            "Reduced holding power in cleat (fiber compression)",
            "Stretch > original length by 2%",
        ],
        "typical_service_life_hours": 800,
        "maintenance": "Rinse with fresh water weekly (saltwater deposits weaken braid)",
        "notes": "Failure results in sail collapse. Inspect before every heavy wind sailing. Replace annually in racing.",
    },

    "genoa_halyard": {
        "name": "Genoa / Jib Halyard",
        "german_name": "Fockfall",
        "function": "Raises headsail (lower load than main, higher fatigue from frequent changes)",
        "material_recommendation": ["Dyneema SK75", "Polyester blend", "Vectran"],
        "diameter_by_boat_length": {
            "30ft": "6-8mm",
            "40ft": "8-10mm",
            "50ft": "10-12mm",
        },
        "construction": "Braid-on-braid preferred (stretch management, easier splicing)",
        "breaking_load_target": "1.5x jib area × 8 kg/m²",
        "clutch_compatibility": "Spinlock HS 8-10 or Antal HT",
        "winch_sizing": "Same halyard winch as main (if separate, 4:1 gear ratio)",
        "chafe_points": [
            "Mast cap sheave (primary wear point)",
            "Foil slot or extrusion (if roller furling)",
            "Deck lead blocks (fairlead edge radius critical)",
        ],
        "replacement_signs": [
            "Seizing strength reduced (cleat slips under light load)",
            "Visible degradation in 100mm hoist section",
            "Knots in braid fiber (UV damage)",
        ],
        "typical_service_life_hours": 600,
        "maintenance": "Wash under freshwater every 10 hours sailing",
        "notes": "Frequent hoist/lower cycles. UV exposure at deck. Replace every season (racing) to every 2 years (cruising).",
    },

    "spinnaker_halyard": {
        "name": "Spinnaker Halyard",
        "german_name": "Spinnakerfall",
        "function": "Raises spinnaker/gennaker (high moment + sideways swing)",
        "material_recommendation": ["Dyneema SK99 (ultra-light, critical if high pole)", "Vectran"],
        "diameter_by_boat_length": {
            "40ft": "8-10mm",
            "50ft": "10-12mm",
            "65ft": "12-14mm",
        },
        "construction": "Single braid (lower stretch = more stable hoist)",
        "breaking_load_target": "2.5x spinnaker area × 6 kg/m² (asymmetric harder on rigging)",
        "clutch_compatibility": "Dedicated spinnaker cleat, OR floating block + jib halyard winch",
        "winch_sizing": "Can share halyard winch if dedicated clutch prevents roll-over",
        "chafe_points": [
            "Mast hoist foil (primary: tape with leather/Toughlon)",
            "Halyard snap shackle (articulated design required)",
            "Floating block swivel (must articulate freely)",
        ],
        "replacement_signs": [
            "Fading/UV bleaching (spinnaker pole area, unshaded)",
            "Stiffness (fiber fatigue from dynamic load)",
            "Knot formation (incompletely untwisted)",
        ],
        "typical_service_life_hours": 300,
        "maintenance": "Dedicated use (don't use for main sail substitute). Dry thoroughly after rain.",
        "notes": "Highest failure rate among halyards. Frequent dynamic loads. Inspect before every downwind session.",
    },

    "mainsheet": {
        "name": "Mainsheet",
        "german_name": "Großschot",
        "function": "Controls main sail trim (continuous dynamic load, most-used line)",
        "material_recommendation": ["Dyneema SK75/SK99 (racing)", "Vectran", "Premium polyester"],
        "diameter_by_boat_length": {
            "30ft": "10-12mm",
            "40ft": "12-14mm",
            "50ft": "14-16mm",
            "65ft": "16-18mm",
        },
        "construction": "Double braid preferred (durability, hand comfort, easy splicing)",
        "breaking_load_target": "3x GZ (righting moment) / 100 kg minimum",
        "clutch_compatibility": "Mainsheet cleat (self-tailing winch standard)",
        "winch_sizing": "Power ratio: 4:1 minimum (standard cruising)",
        "typical_purchase_length": "100-120ft",
        "chafe_points": [
            "Boom gooseneck (3-4 feet of primary wear)",
            "Boom end (if traveler car is aft)",
            "Deck block exits (wrap blocks with leather)",
            "Hand grip area (where trimmed by crew)",
        ],
        "replacement_signs": [
            "Loss of gloss, fuzzy appearance (normal wear)",
            "Diameter reduction > 1mm (significant fiber loss)",
            "Cleat slippage under moderate load (compression failure)",
            "Visible mold/discoloration (moisture damage, requires washing)",
        ],
        "typical_service_life_hours": 1200,
        "maintenance": "Wash weekly (salt deposits attract moisture). Dry thoroughly. UV cover if stored.",
        "notes": "Most-abused line on boat. Budget for replacement every 18 months (racing) to 4 years (cruising).",
    },

    "genoa_sheets": {
        "name": "Genoa / Jib Sheets (Pair)",
        "german_name": "Fockschoten",
        "function": "Controls headsail trim (symmetric port/starboard load, frequent tacking)",
        "material_recommendation": ["Dyneema SK75", "Vectran", "Polyester blend"],
        "diameter_by_boat_length": {
            "30ft": "8-10mm",
            "40ft": "10-12mm",
            "50ft": "12-14mm",
        },
        "construction": "Double braid (standard) or single braid (lighter, less stretch)",
        "breaking_load_target": "1.5x GZ / 80 kg minimum",
        "clutch_compatibility": "Self-tailing winches (one per side) or floating blocks + primary winch",
        "winch_sizing": "Power ratio: 4:1 minimum",
        "typical_purchase_length": "60-80ft per side",
        "chafe_points": [
            "Fairlead block (highest wear during upwind)",
            "Spreader contact (if overlapping genoa)",
            "Cleat/winch exit (rope tape recommended)",
            "Pulpit/stanchion (prevent during maneuvers)",
        ],
        "replacement_signs": [
            "Fuzzing at fairlead (indicates wear rate)",
            "Slipping in cleat under full trim (fiber compression)",
            "Mold/staining (wash and dry immediately)",
            "Knots in braid (damaged, replace that section)",
        ],
        "typical_service_life_hours": 900,
        "maintenance": "Wash monthly. Dry before storage. Rotate port/starboard seasonally if unequal wear.",
        "notes": "Pair must be identical length/construction. Tacking loads are cyclic (fatigue critical). Replace together.",
    },

    "spinnaker_sheets": {
        "name": "Spinnaker Sheets (Pair)",
        "german_name": "Spinnakerführungen",
        "function": "Controls spinnaker lateral position (low bending stiffness, easy easing)",
        "material_recommendation": ["Dyneema SK75 (light, runs easy)", "Vectran", "Polyester"],
        "diameter_by_boat_length": {
            "40ft": "8-10mm",
            "50ft": "10-12mm",
            "65ft": "12-14mm",
        },
        "construction": "Single braid preferred (less weight aloft, easier to handle)",
        "breaking_load_target": "1.2x spinnaker area × 6 kg/m²",
        "clutch_compatibility": "Floating block or low-friction snatch block (spinnaker can swing)",
        "winch_sizing": "Can use jib sheet winch if secondary line has independent control",
        "typical_purchase_length": "80-100ft per side",
        "chafe_points": [
            "Snatch block shackle (protect with leather tape)",
            "Deck blocks (fairlead angles > 45° cause friction)",
            "Cleat/winch exit",
        ],
        "replacement_signs": [
            "Stiffness (fatigue from load cycling)",
            "Loss of gloss (UV damage from continuous deck exposure)",
            "Slippage in cleat (compression failure)",
        ],
        "typical_service_life_hours": 400,
        "maintenance": "Store out of sunlight. Rinse after salt exposure. Keep supple.",
        "notes": "Lower loads than genoa sheets. Lighter material acceptable. Must pay out smoothly (inspect cleat weekly).",
    },

    "reefing_lines": {
        "name": "Reef Points / Reefing Line",
        "german_name": "Reffschnüre",
        "function": "Controls deployed reefs (pendant pulls leech down, line controls/secures)",
        "material_recommendation": ["Polyester (less critical)", "Dyneema (faster reef)", "Braided 3-strand"],
        "diameter_by_boat_length": {
            "30ft": "5-6mm",
            "40ft": "6-8mm",
            "50ft": "8-10mm",
        },
        "construction": "Single braid or 3-strand (sufficient breaking load, cost-effective)",
        "breaking_load_target": "0.8x main sail area × 10 kg/m²",
        "clutch_compatibility": "Dedicated reefing cleat (low-friction) or jib halyard winch",
        "winch_sizing": "Jib halyard winch acceptable (lower torque than main sail hoist)",
        "typical_purchase_length": "40-60ft",
        "chafe_points": [
            "Mast channel or slide (if in-mast furling)",
            "Boom cringle hardware (pad with leather)",
            "Cleat exit (smooth radius)",
        ],
        "replacement_signs": [
            "Increased friction in cleat (fiber fraying)",
            "Loss of gloss (age-related, still safe if diameter OK)",
            "Visible cuts/damage (safety issue—replace immediately)",
        ],
        "typical_service_life_hours": 600,
        "notes": "Reefing is frequent operation (affects fatigue life). Test reefing monthly in season.",
    },

    "vang_kicker": {
        "name": "Boom Vang / Kicker",
        "german_name": "Baum-Vang / Topnant",
        "function": "Controls boom twist and vertical rise (dynamic load varies with point of sail)",
        "material_recommendation": ["Dyneema SK75", "Vectran", "Premium polyester"],
        "diameter_by_boat_length": {
            "30ft": "8-10mm",
            "40ft": "10-12mm",
            "50ft": "12-14mm",
        },
        "construction": "Single braid (low-stretch critical for sail shape control)",
        "breaking_load_target": "1.5x main area × 8 kg/m²",
        "clutch_compatibility": "Block + cleat system (not typically winched)",
        "typical_purchase_length": "30-40ft",
        "chafe_points": [
            "Boom attachment (leather pad on boom)",
            "Block sheaves (fairlead angle critical, > 45° causes friction)",
            "Cleat exit (smooth edges)",
        ],
        "replacement_signs": [
            "Twist control loss (sail shape deteriorates when hard on wind)",
            "Visible fraying/degradation at boom attachment",
            "Creep (vang stretches, boom rises uncontrollably)",
        ],
        "typical_service_life_hours": 800,
        "notes": "Directly affects sail efficiency. Inspect trim monthly. Rerig if any slippage.",
    },

    "cunningham": {
        "name": "Cunningham / Downhaul",
        "german_name": "Unterholer / Niederholer",
        "function": "Controls main sail draft/flatten (fine-tuning luff tension)",
        "material_recommendation": ["Light polyester", "Dyneema SK75"],
        "diameter_by_boat_length": {
            "30ft": "4-5mm",
            "40ft": "5-6mm",
            "50ft": "6-8mm",
        },
        "construction": "Single braid or 3-strand (low loads, cost is secondary)",
        "breaking_load_target": "0.3x main area × 5 kg/m²",
        "clutch_compatibility": "Low-friction cleat (e.g., Harken 40.5 or Antal XT) or small winch",
        "typical_purchase_length": "20-30ft",
        "chafe_points": [
            "Mast grommet (pad with leather if high-load racing)",
            "Block exit fairlead",
        ],
        "replacement_signs": [
            "Difficult to tension (compression failure)",
            "Loses shape when released (creep)",
        ],
        "typical_service_life_hours": 1000,
        "notes": "Racing-critical. Cruising boats may omit. Tension changes with wind strength.",
    },

    "outhaul": {
        "name": "Outhaul",
        "german_name": "Baum-Aussteller",
        "function": "Controls main sail foot shape/tension (flatten in heavy, ease in light)",
        "material_recommendation": ["Light polyester", "Dyneema SK75"],
        "diameter_by_boat_length": {
            "30ft": "4-5mm",
            "40ft": "5-6mm",
            "50ft": "6-8mm",
        },
        "construction": "Single braid or 3-strand",
        "breaking_load_target": "0.3x main area × 5 kg/m²",
        "clutch_compatibility": "Low-friction cleat or block + line system",
        "typical_purchase_length": "20-30ft",
        "chafe_points": [
            "Boom end cringle (pad with leather)",
            "Block fairleads (angle > 45° increases friction)",
        ],
        "replacement_signs": [
            "Fraying at boom end cringle",
            "Loss of adjustment range (creep stretched line)",
        ],
        "typical_service_life_hours": 1000,
        "notes": "Constant adjustment during sailing. Cruising boats often use fixed eye (not adjustable).",
    },

    "topping_lift": {
        "name": "Topping Lift",
        "german_name": "Topnant / Brassen",
        "function": "Supports boom when sail is lowered (prevents accidental jibe/boom drop)",
        "material_recommendation": ["Polyester (low cost)", "Dyneema (low-weight option)"],
        "diameter_by_boat_length": {
            "30ft": "6-8mm",
            "40ft": "8-10mm",
            "50ft": "10-12mm",
        },
        "construction": "Single braid or 3-strand (load is static when sail is down)",
        "breaking_load_target": "1.5x boom weight",
        "clutch_compatibility": "Cleat or block + rope stopper",
        "typical_purchase_length": "40-50ft",
        "chafe_points": [
            "Boom end fitting (pad with leather)",
            "Upper block/sheave at mast (fairlead angle)",
        ],
        "replacement_signs": [
            "Boom sags when sail is lowered (excessive creep)",
            "Visible rot/mold (indicates moisture, must dry immediately)",
        ],
        "typical_service_life_hours": 500,
        "notes": "Lower priority for replacement (limited dynamic loading). Inspect for mold/mildew monthly.",
    },
}

# ============================================================================
# ROPE_MATERIALS — Tauwerk-Materialien
# ============================================================================

ROPE_MATERIALS: Dict[str, Dict[str, Any]] = {
    "polyester_dacron": {
        "name": "Polyester (Dacron)",
        "german_name": "Polyester (Dacron)",
        "fiber_type": "Polyethylene terephthalate, synthetic filament",
        "density_g_cm3": 1.38,
        "breaking_strength_ratio_vs_nylon": 0.92,
        "elongation_percent": 14,
        "uv_resistance": "Good (5-10 year lifespan with cover)",
        "creep_percent_at_50pct_load_1yr": 2.5,
        "melting_point_celsius": 254,
        "water_absorption_percent": 0.4,
        "cost_factor": 1.0,
        "typical_use": ["Mainsheet", "Genoa sheets", "Cruising halyards"],
        "advantages": [
            "Good UV resistance (can weather sun)",
            "Low creep (stable shape retention)",
            "Cost-effective",
            "Comfortable hand feel (not slippery)",
            "Easy splicing",
        ],
        "disadvantages": [
            "Heavier than Dyneema (10x for same breaking load)",
            "Larger diameter needed (rigging weight increases)",
            "Moderate stretch (2-3% over load life)",
        ],
        "typical_brands": ["Samson", "New England Rope", "Marlow"],
        "notes": "Industry standard for cruising boats. Tried-and-tested for 50+ years. Suitable for boats without racing ambitions.",
    },

    "dyneema_hmpe_sk75": {
        "name": "Dyneema / HMPE (SK75)",
        "german_name": "Dyneema SK75 (UHMWPE)",
        "fiber_type": "Ultra-high-molecular-weight polyethylene",
        "density_g_cm3": 0.98,
        "breaking_strength_ratio_vs_nylon": 1.15,
        "elongation_percent": 3.5,
        "uv_resistance": "Moderate (requires UV protection or cover)",
        "creep_percent_at_50pct_load_1yr": 5.0,
        "melting_point_celsius": 147,
        "water_absorption_percent": 0.05,
        "cost_factor": 3.2,
        "typical_use": ["Halyards (best choice)", "Cruising mainsheets", "Control lines"],
        "advantages": [
            "1/3 weight of polyester (halyard loads on crew reduced)",
            "Low stretch (4-6mm loss per 30ft halyard over 5 years)",
            "High breaking strength (smaller diameter possible)",
            "Excellent water shedding (floats, doesn't absorb)",
            "Long service life (if protected from UV)",
        ],
        "disadvantages": [
            "Critical UV sensitivity (bleaches/weakens in 6 months if exposed)",
            "Creep under load (5-10% permanent stretch at 50% load)",
            "Slippery (difficult hand feel, requires careful cleat design)",
            "Low melting point (135-147°C) — friction can cause damage",
            "Knots reduce strength 50% (never knot, always splice)",
            "Expensive (4-5x polyester)",
        ],
        "typical_brands": ["Samson", "New England Rope", "Yale", "Marlow"],
        "care_instructions": [
            "Store in UV-protected bag (blue/dark sail bag)",
            "Cover exposed halyards with stretch tape or lazy jack",
            "Inspect quarterly for bleaching/fuzz",
            "Replace if strength loss suspected (pull-test recommended)",
        ],
        "notes": "Best halyard material. Requires discipline (UV cover, storage). Recommended for all modern boats.",
    },

    "dyneema_hmpe_sk99": {
        "name": "Dyneema / HMPE (SK99)",
        "german_name": "Dyneema SK99 (Ultra-modulus)",
        "fiber_type": "Ultra-high-molecular-weight polyethylene, cross-linked",
        "density_g_cm3": 0.99,
        "breaking_strength_ratio_vs_nylon": 1.40,
        "elongation_percent": 3.0,
        "uv_resistance": "Moderate (same as SK75 — requires protection)",
        "creep_percent_at_50pct_load_1yr": 3.0,
        "melting_point_celsius": 145,
        "water_absorption_percent": 0.05,
        "cost_factor": 4.8,
        "typical_use": ["Racing halyards (best choice)", "Spinnaker halyards", "High-load control lines"],
        "advantages": [
            "Highest breaking strength of any rope (finest diameter possible)",
            "Lower creep than SK75 (more stable shape retention)",
            "Extreme lightweight (critical for high pole loads)",
            "Proven in America's Cup and Olympic racing",
        ],
        "disadvantages": [
            "Severe UV sensitivity (even more critical than SK75)",
            "Highest cost (6-8x polyester)",
            "Extreme slipperiness (cleat selection critical: self-tailing mandatory)",
            "Knots fail — splicing only option",
            "Creep still occurs (3% over 5 years under load)",
        ],
        "typical_brands": ["Samson", "Marlow", "Yale"],
        "care_instructions": [
            "UV cover is non-negotiable (lazy jacks or stretch tape)",
            "Store in sealed bag between seasons",
            "Inspect for bleaching monthly during season",
            "Replace annually (racing)" ,
        ],
        "notes": "Reserved for racing boats. Marginal durability if UV not strictly managed. Not recommended for cruising.",
    },

    "vectran": {
        "name": "Vectran (LCPP — Liquid Crystal Polymer)",
        "german_name": "Vectran (Flüssigkristallpolymer)",
        "fiber_type": "Liquid crystal polymer, aramid-like structure",
        "density_g_cm3": 1.40,
        "breaking_strength_ratio_vs_nylon": 1.22,
        "elongation_percent": 2.5,
        "uv_resistance": "Very good (10+ years with care)",
        "creep_percent_at_50pct_load_1yr": 1.5,
        "melting_point_celsius": 320,
        "water_absorption_percent": 0.05,
        "cost_factor": 3.8,
        "typical_use": ["Mainsheets (premium)", "Halyards (alternative to Dyneema)", "Control lines"],
        "advantages": [
            "Excellent UV resistance (can be exposed without cover)",
            "Very low creep (maintains shape over years)",
            "Higher melting point (resistant to friction/chafe)",
            "Friendly hand feel (less slippery than Dyneema)",
            "Excellent fatigue resistance",
        ],
        "disadvantages": [
            "Slightly heavier than Dyneema SK99",
            "Higher cost than polyester",
            "More sensitive to bending stiffness (requires careful block sizing)",
            "Less universal brand recognition (fewer suppliers)",
        ],
        "typical_brands": ["Cortland", "Marlow"],
        "care_instructions": [
            "Rinse with fresh water weekly",
            "Dry before storage",
            "No special UV protection required (unlike Dyneema)",
        ],
        "notes": "Excellent all-around rope for mixed-use lines. Balance of performance and durability. Recommended for cruising/club racing.",
    },

    "technora": {
        "name": "Technora (Aramid Polyamide)",
        "german_name": "Technora (Aramid-Polyamid-Mix)",
        "fiber_type": "Aromatic polyamide (aramid) + polyamide blend",
        "density_g_cm3": 1.39,
        "breaking_strength_ratio_vs_nylon": 1.05,
        "elongation_percent": 3.5,
        "uv_resistance": "Good (5-8 years with cover)",
        "creep_percent_at_50pct_load_1yr": 2.0,
        "melting_point_celsius": 370,
        "water_absorption_percent": 1.5,
        "cost_factor": 2.5,
        "typical_use": ["Control lines", "Reefing lines", "Secondary halyards"],
        "advantages": [
            "Very high melting point (excellent chafe resistance)",
            "Low creep",
            "Good UV resistance",
            "Higher breaking strength than polyester",
        ],
        "disadvantages": [
            "Water absorption (loses 15-20% strength when wet)",
            "Less common (limited supplier base)",
            "Requires UV cover for extended storage",
            "Higher cost than polyester",
        ],
        "typical_brands": ["New England Rope", "Bridon"],
        "notes": "Specialty material. Good for high-chafe areas. Rare in modern rigging (replaced by Vectran).",
    },

    "pbo_zylon_fiber": {
        "name": "PBO (Zylon) Fiber",
        "german_name": "PBO/Zylon (Para-Phenylene Benzobisoxazol)",
        "fiber_type": "Rigid aromatic heterocyclic polymer",
        "density_g_cm3": 1.56,
        "breaking_strength_ratio_vs_nylon": 1.60,
        "elongation_percent": 2.0,
        "uv_resistance": "Very poor (6-12 months without cover, then loses 50% strength)",
        "creep_percent_at_50pct_load_1yr": 0.5,
        "melting_point_celsius": 650,
        "water_absorption_percent": 4.0,
        "cost_factor": 6.0,
        "typical_use": ["Racing halyards only", "Extreme racing applications"],
        "advantages": [
            "Highest breaking strength of any fiber (ultra-fine diameter)",
            "Virtually no creep (constant mast geometry under load)",
            "Extremely low elongation (0.3-0.5% typical)",
        ],
        "disadvantages": [
            "Catastrophic UV degradation (color fade = strength loss)",
            "Water absorption (strength loss 20-30% when wet)",
            "Brittle (low impact resistance, prone to kinking)",
            "Extreme cost (8-10x polyester)",
            "Difficult to splice (requires epoxy/mechanical terminals only)",
            "Short lifespan (1-2 years racing, then must replace)",
        ],
        "typical_brands": ["Pinnell & Bax", "Hydra Sports"],
        "care_instructions": [
            "Full UV cover is mandatory (no exceptions)",
            "Store in sealed UV-proof bag between seasons",
            "Dry immediately after rain/spray (moisture weakens)",
            "Inspect monthly — replace if color fades",
        ],
        "notes": "Racing-only material. High performance at very high cost/risk. Not suitable for cruising or casual racing.",
    },

    "aramid_kevlar": {
        "name": "Aramid (Kevlar)",
        "german_name": "Aramid (Kevlar)",
        "fiber_type": "Para-aramid polyamide (Kevlar is DuPont trademark)",
        "density_g_cm3": 1.44,
        "breaking_strength_ratio_vs_nylon": 1.30,
        "elongation_percent": 2.0,
        "uv_resistance": "Good (5+ years with care)",
        "creep_percent_at_50pct_load_1yr": 1.0,
        "melting_point_celsius": 370,
        "water_absorption_percent": 3.0,
        "cost_factor": 3.5,
        "typical_use": ["Control lines", "Racing applications"],
        "advantages": [
            "Very high breaking strength",
            "Low creep",
            "Good cut/chafe resistance",
        ],
        "disadvantages": [
            "Water absorption (loses 15-20% strength when saturated)",
            "UV sensitivity (yellow after 2-3 years)",
            "Expensive",
            "Less common than modern alternatives",
        ],
        "typical_brands": ["DuPont Kevlar"],
        "notes": "Largely superseded by Vectran and Dyneema. Historical significance in 1980s-1990s racing.",
    },

    "nylon_polyamide": {
        "name": "Nylon (Polyamide)",
        "german_name": "Nylon (Polyamid)",
        "fiber_type": "Polyamide synthetic filament",
        "density_g_cm3": 1.14,
        "breaking_strength_ratio_vs_nylon": 1.0,
        "elongation_percent": 20,
        "uv_resistance": "Poor (1-2 years unprotected)",
        "creep_percent_at_50pct_load_1yr": 8.0,
        "melting_point_celsius": 215,
        "water_absorption_percent": 3.5,
        "cost_factor": 0.6,
        "typical_use": ["Mooring/dock lines only", "NOT for rigging"],
        "advantages": [
            "Very low cost",
            "Excellent elasticity (shock absorption)",
            "Abrasion resistant",
        ],
        "disadvantages": [
            "High creep (not suitable for sail rigging)",
            "Poor UV resistance",
            "Heavy (7x weight for same strength as Dyneema)",
            "Water absorption affects strength",
        ],
        "notes": "Mooring line material only. Never use for halyards/sheets (excessive stretch).",
    },

    "polypropylene": {
        "name": "Polypropylene",
        "german_name": "Polypropylen",
        "fiber_type": "Polypropylene thermoplastic polymer",
        "density_g_cm3": 0.90,
        "breaking_strength_ratio_vs_nylon": 0.65,
        "elongation_percent": 16,
        "uv_resistance": "Very poor (6-12 months)",
        "creep_percent_at_50pct_load_1yr": 12,
        "melting_point_celsius": 165,
        "water_absorption_percent": 0.0,
        "cost_factor": 0.3,
        "typical_use": ["Temporary lines", "NOT suitable for rigging"],
        "advantages": [
            "Lowest cost",
            "Floats (rescue lines)",
            "No water absorption",
        ],
        "disadvantages": [
            "Very low UV resistance (disintegrates quickly)",
            "High creep",
            "Weak (low breaking strength)",
            "Low melting point (risk of fusion damage)",
        ],
        "notes": "Emergency/temporary use only. Not suitable for any permanent rigging application.",
    },
}

# ============================================================================
# WINCHES_AND_HARDWARE — Winschen und Decksbeschläge
# ============================================================================

WINCHES_AND_HARDWARE: Dict[str, Dict[str, Any]] = {
    "self_tailing_winch": {
        "name": "Self-Tailing Winch",
        "german_name": "Selbstholende Winde",
        "function": "Hauls line and grips automatically (eliminates need for crew on tail)",
        "load_ratings_kg": {
            "10": 1600,
            "16": 3500,
            "25": 6200,
            "40": 11000,
        },
        "gear_ratio_options": [
            "2-speed: 4:1 low / 16:1 high",
            "3-speed: 4:1 / 16:1 / 64:1 (rare)",
        ],
        "power_ratio": "16:1 (winch mechanical advantage × handle length)",
        "sizing_by_boat_length": {
            "30ft": "10/16 kg rating",
            "40ft": "16/25 kg rating",
            "50ft": "25/40 kg rating",
            "65ft": "40+ kg rating",
        },
        "self_tailing_jaw": {
            "mechanism": "Elastomer-lined upper jaw, fixed lower drum",
            "function": "Grips rope and prevents backslip",
            "maintenance_interval_hours": 200,
            "wear_pattern": "Jaw wears unevenly (rotate positions seasonally)",
            "replacement_signs": [
                "Rope slips under load (jaw is glazed/worn)",
                "Rough texture indicates deep wear (replace immediately)",
            ],
            "jaw_replacement_cost_usd": 120,
        },
        "maintenance": [
            "Weekly rinse with freshwater (salt deposits cause friction loss)",
            "Monthly lubrication with light machine oil (sparingly — excess attracts dirt)",
            "Quarterly jaw inspection (compare left vs right wear)",
            "Annual overhaul (disassemble, clean ratchet, inspect bearings)",
        ],
        "failure_modes": [
            "Jaw wear (most common): jaw becomes smooth, cannot grip rope",
            "Ratchet slippage: worn pawl or worn ratchet gear (catastrophic)",
            "Bearing wear: increased friction, rough turning",
            "Handle breaking: metal fatigue at base (rare on quality models)",
        ],
        "brands": [
            "Harken (best—world standard)",
            "Lewmar (good, less expensive)",
            "Andersen (excellent, Swedish)",
            "Antal (Spanish, economical)",
        ],
        "cost_installed_usd": 800,
        "notes": "Standard on all modern sailboats > 30ft. Indispensable for crew management.",
    },

    "powered_winch": {
        "name": "Powered Winch (Electric Motor)",
        "german_name": "Motor-Winde",
        "function": "Electric motor drives winch (for cruising/large boats/accessibility)",
        "motor_power_options": ["1 hp", "2 hp", "3 hp"],
        "voltage_options": ["12V DC (cruising)", "24V DC (larger boats)", "110V AC (large yachts)"],
        "load_ratings_kg": {
            "1 hp": 3000,
            "2 hp": 6000,
            "3 hp": 9000,
        },
        "speed_control": "Proportional foot pedal (variable load)",
        "installation_notes": "Requires dedicated circuit breaker (50A minimum), wiring, foot switch",
        "maintenance": [
            "Motor brushes: inspect annually, replace every 500 hours",
            "Gearbox oil: change annually (mineral oil 80W-90)",
            "Electrical: clean contacts quarterly, protect from corrosion",
        ],
        "failure_modes": [
            "Motor brush wear (loss of power, arcing)",
            "Gearbox oil degradation (noise, slipping)",
            "Electrical corrosion (moisture inside motor)",
            "Foot switch failure (most common failure point)",
        ],
        "brands": ["Lewmar", "Andersen", "Harken", "Maxwell"],
        "cost_installed_usd": 2500,
        "notes": "Luxurious for cruising. Adds weight, complexity, cost. Not used in racing.",
    },

    "halyard_winch": {
        "name": "Halyard Winch (Dedicated)",
        "german_name": "Fallwinde",
        "function": "Specialized winch for halyards (higher power ratio than sheet winch)",
        "load_ratings_kg": {
            "10": 1600,
            "16": 3500,
            "25": 6200,
        },
        "gear_ratio": "16:1 (halyard loads are sustained, not cyclic)",
        "mounting_location": "Mast base or cabin top (accessible to crew)",
        "self_tailing": "Yes (essential for halyard use)",
        "sizing_by_boat_length": {
            "30ft": "16 kg",
            "40ft": "25 kg",
            "50ft": "40 kg",
        },
        "maintenance": [
            "Monthly jaw inspection (halyard use causes rapid wear)",
            "Quarterly replacement if rope fuzzes (sign of jaw glazing)",
            "Annual complete overhaul (disassembly, cleaning, reassembly)",
        ],
        "failure_modes": [
            "Jaw glazing (most common — rope slips when hauling)",
            "Ratchet slippage (catastrophic — sail falls)",
        ],
        "brands": ["Harken", "Lewmar", "Andersen", "Antal"],
        "cost_installed_usd": 600,
        "notes": "Twin halyards (port/starboard) require separate winches or single winch with careful fairleading.",
    },

    "sheet_winch": {
        "name": "Sheet Winch",
        "german_name": "Schot-Winde",
        "function": "Trims genoa/jib sheets (cyclic loading, requires higher speed than halyard)",
        "load_ratings_kg": {
            "16": 3500,
            "25": 6200,
            "40": 11000,
        },
        "gear_ratio": "4:1 low / 16:1 high (sheet winches prioritize speed over power)",
        "typical_count": "2 (one per side for genoa), plus 1 main sheet",
        "mounting_location": "Cockpit aft corners (easy access)",
        "self_tailing": "Yes (reduces crew requirement)",
        "power_applications": "Trimming, not hauling (lower sustained load than halyards)",
        "failure_modes": [
            "Jaw wear (rapid from repeated load cycles)",
            "Ratchet failure (catastrophic)",
        ],
        "maintenance": [
            "Weekly rinse (heavy use in salt environment)",
            "Monthly jaw inspection",
            "Quarterly jaw replacement (sheet use causes rapid wear)",
        ],
        "brands": ["Harken", "Lewmar", "Andersen"],
        "cost_installed_usd": 500,
        "notes": "Typically 1-2 sizes smaller than halyard winch. Replaceable jaw covers critical maintenance interval.",
    },

    "fixed_block": {
        "name": "Fixed Block (Non-Articulated)",
        "german_name": "Feste Rolle",
        "function": "Changes rope direction (sheave doesn't rotate with load)",
        "load_ratings_kg": {
            "small": 500,
            "medium": 1000,
            "large": 2000,
        },
        "sheave_material": ["Stainless steel (best)", "Plastic (budget)"],
        "sheave_bearing": "Stainless bushing or ball bearing (ball bearing preferred)",
        "fairlead_angle_limit": "45° maximum (above 45° causes line friction/heat)",
        "inspection_criteria": [
            "Sheave rotates freely (hand test: 1-2 second coast)",
            "No visible corrosion on pin/bearing",
            "Line sits centered on sheave groove",
        ],
        "failure_modes": [
            "Seized sheave (rust, salt intrusion)",
            "Cracked body (impact damage)",
            "Bent pin (causes misalignment, line abrasion)",
        ],
        "brands": ["Harken", "Ronstan", "Schaefer"],
        "cost_per_block_usd": 30,
        "notes": "Maintenance-free if rinsed monthly. Proper fairlead angle critical (inspect quarterly).",
    },

    "ratchet_block": {
        "name": "Ratchet Block",
        "german_name": "Sperre-Rolle mit Ratschenfunktion",
        "function": "Prevents backslip under load (one-way holding)",
        "load_ratings_kg": {
            "small": 800,
            "medium": 1500,
            "large": 2500,
        },
        "ratchet_mechanism": "Pawl + ratchet gear (similar to winch)",
        "typical_use": ["Mainsheet", "Spinnaker guy"],
        "activation": "Rope tension > threshold (typically 200-300 kg) engages ratchet",
        "disengagement": "Crew must disengage by lifting rope out of gear",
        "inspection_criteria": [
            "Ratchet engages smoothly at moderate load",
            "No grinding/slipping when disengaged",
            "Pawl spring returns immediately (manual test)",
        ],
        "failure_modes": [
            "Pawl sticking (corrosion, dirt)",
            "Ratchet gear wear (slipping under load)",
            "Spring fatigue (pawl doesn't return)",
        ],
        "brands": ["Harken", "Ronstan", "Antal"],
        "cost_per_block_usd": 85,
        "maintenance": [
            "Rinse monthly (salt deposits prevent smooth engagement)",
            "Quarterly inspection of pawl movement",
            "Annual overhaul (disassemble, clean ratchet mechanism)",
        ],
        "notes": "Useful for single-handed sailing. Can cause rope wear if engaged too aggressively.",
    },

    "fiddle_block": {
        "name": "Fiddle Block (Multi-Sheave)",
        "german_name": "Zweifach-Rolle",
        "function": "Two sheaves (one above other) for rope changes or mechanical advantage",
        "sheave_count": 2,
        "mechanical_advantage": "1:2 (single block with hauling/standing parts from same block)",
        "typical_use": ["Mainsheet setup", "Jib sheet block"],
        "load_ratings_kg": {
            "small": 600,
            "medium": 1200,
            "large": 2000,
        },
        "inspection_criteria": [
            "Both sheaves rotate independently and smoothly",
            "No side-play on pins",
            "Body alignment (sheaves parallel to rope)",
        ],
        "failure_modes": [
            "Sheave misalignment (causes line abrasion)",
            "Pin bent (loss of sheave rotation)",
            "Separator cracked (sheaves touch, jam)",
        ],
        "brands": ["Harken", "Ronstan"],
        "cost_per_block_usd": 120,
        "notes": "Compact way to achieve mechanical advantage. Adds weight vs two single blocks. Requires careful alignment.",
    },

    "spinlock_cleat": {
        "name": "Spinlock Cleat (Self-Tailing Cam)",
        "german_name": "Spinlock Klemme / Selbstholende Klemme",
        "function": "Jammer cleat that holds rope and prevents backslip (no hand-tailing required)",
        "typical_sizes": ["HS10", "HS16", "HS20"],
        "load_ratings_kg": {
            "HS10": 1000,
            "HS16": 1600,
            "HS20": 2000,
        },
        "mechanism": "Cam lever + elastomer friction pads",
        "operation": "1. Wrap rope around cleat. 2. Lever down to engage. 3. Rope holds automatically.",
        "disengagement": "Lift lever to release (requires upward force)",
        "installation_angle": "30-45° to rope direction (fairlead critical)",
        "inspection_criteria": [
            "Cam lever moves smoothly (no friction)",
            "Friction pads not glazed (rough surface required)",
            "Rope sits centered between pads",
        ],
        "pad_wear_signs": [
            "Rope slides when lever is engaged (glazed pads)",
            "Permanent rope marks in pads (sign of replacement needed)",
        ],
        "maintenance": [
            "Rinse monthly (prevent salt deposit buildup)",
            "Quarterly friction pad inspection",
            "Annual pad replacement if glazed (cost: $25)",
        ],
        "failure_modes": [
            "Glazed pads (most common): cannot grip rope",
            "Broken lever (metal fatigue from repeated jamming)",
            "Crack in body from side-loading",
        ],
        "brands": ["Spinlock (market leader)", "Antal", "Ronstan"],
        "cost_per_cleat_usd": 60,
        "notes": "Industry standard for halyards/control lines. Requires proper fairlead angle (critical). Pads are consumable (annual replacement in heavy use).",
    },

    "antal_ht_cleat": {
        "name": "Antal HT Cleat (Low-Friction Cam)",
        "german_name": "Antal HT Klemme",
        "function": "High-friction alternative to Spinlock (less aggressive, easier easing)",
        "load_ratings_kg": {
            "HT10": 1000,
            "HT16": 1600,
            "HT20": 2000,
        },
        "mechanism": "Aluminum cam + composite pads (lower friction coefficient than Spinlock)",
        "advantage_over_spinlock": "Easier easing without dramatic jamming (better for reefing lines)",
        "installation_angle": "25-40° to rope direction",
        "maintenance": [
            "Monthly rinse",
            "Quarterly pad inspection",
            "Annual pad replacement",
        ],
        "brands": ["Antal (Spanish company)"],
        "cost_per_cleat_usd": 50,
        "notes": "Gentler than Spinlock. Good choice for reefing lines, light sheets. Less secure than Spinlock under extreme load.",
    },

    "cam_cleat": {
        "name": "Standard Cam Cleat (Basic Jammer)",
        "german_name": "Einfache Cam-Klemme",
        "function": "Basic rope holder (no self-tailing — requires hand for backup)",
        "load_ratings_kg": {
            "small": 500,
            "medium": 1000,
            "large": 1500,
        },
        "mechanism": "Single aluminum cam + elastomer pads",
        "operation": "Press rope down, cam jams. Pull up to release.",
        "fairlead_angle": "Typically mounted at 30-60° to rope",
        "installation_notes": "Bolt-down with SS fasteners, cleats should be flush to deck",
        "maintenance": [
            "Rinse with freshwater weekly",
            "Pads wear quickly (every season or 200+ hours)",
            "Quarterly pad replacement if glazed",
        ],
        "failure_modes": [
            "Glazed pads (cannot hold rope)",
            "Cracked cam from impact",
            "Fasteners corrode/loosen",
        ],
        "cost_per_cleat_usd": 20,
        "notes": "Economy choice. Acceptable for low-load control lines. Not suitable for halyards (continuous tailing required).",
    },

    "track_and_car_system": {
        "name": "Track and Car System (Traveler)",
        "german_name": "Schiene und Laufkatze",
        "function": "Allows rope eye/block to slide along track (mainsheet trimming)",
        "track_length_options": ["2ft", "3ft", "4ft", "6ft"],
        "load_ratings_kg": {
            "small_car": 1500,
            "medium_car": 2500,
            "large_car": 4000,
        },
        "materials": [
            "Track: aluminum extrusion (anodized)",
            "Car: nylon/acetal polymer (low friction)",
            "Ball bearings: stainless steel",
        ],
        "typical_location": "Boom end, cabin top (mainsheet), genoa lead block positions",
        "installation": "Deck-bolted track, car rides on ball-bearing rollers",
        "maintenance": [
            "Monthly rinse (salt deposits cause friction increase)",
            "Quarterly inspection of ball bearings (replace if rough)",
            "Annual re-anodizing of track if corrosion appears (rare)",
            "Car seal replacement annually (dust cap keeps debris out)",
        ],
        "failure_modes": [
            "Bearing corrosion (track becomes stiff)",
            "Car derailment (excessive side load, improper fastening)",
            "Track wear (rarely, usually track outlasts car)",
            "Fastener corrosion (loosen track from mounting)",
        ],
        "brands": ["Harken", "Lewmar", "Ronstan", "Andersen"],
        "cost_for_4ft_system_usd": 400,
        "notes": "Critical for mainsheet trim control. Ball bearing maintenance essential (quarterly inspection recommended).",
    },

    "mast_hardware_sheave_boxes": {
        "name": "Mast Hardware / Sheave Boxes",
        "german_name": "Mast-Hardware / Scheibenbox",
        "function": "Houses halyard sheaves at mast top, supports rigging loads",
        "typical_sheave_count": [1, 2, 3, 4],
        "sheave_materials": ["Stainless steel", "Acetal polymer"],
        "sheave_diameter_options": ["25mm", "30mm", "35mm", "40mm"],
        "installation_method": "Bolted or riveted to mast extrusion",
        "failure_modes": [
            "Sheave seizure (rust, salt intrusion) — most common",
            "Cracked box body (impact during mast step)",
            "Loose bolts (vibration causes loosening)",
            "Halyard chafe on box edge (poor radius)",
        ],
        "inspection_checklist": [
            "Each sheave rotates smoothly (hand test: coast for 2+ seconds)",
            "No groove wear on sheave (indicates halyard rubbing)",
            "Bolts tight (wrench check, no hand-tightening)",
            "No visible corrosion (salt deposits indicate poor drainage)",
        ],
        "maintenance": [
            "Monthly mast cleaning (remove salt deposits)",
            "Quarterly sheave rotation check (by hand, spinning test)",
            "Annual lubrication (light oil on sheave pin, sparingly)",
            "Post-season: hose down mast top with freshwater (critical)",
        ],
        "typical_sheave_box_types": [
            "Single sheave (spinnaker halyard)",
            "Dual sheave (main + jib halyard)",
            "Triple sheave (main + jib + spinnaker)",
        ],
        "cost_per_box_usd": 150,
        "notes": "Mast-top hardware is exposed to harshest environment. Quarterly inspection critical. Seized sheave = halyard failure.",
    },
}

# ============================================================================
# MAST_AND_BOOM — Mast und Baum
# ============================================================================

MAST_AND_BOOM: Dict[str, Dict[str, Any]] = {
    "aluminum_extruded_mast": {
        "name": "Aluminum Extruded Mast",
        "german_name": "Aluminium Strangpressmast",
        "material_grade": "6061-T6 (standard), 7075-T6 (racing)",
        "section_profiles": [
            "Vertical extrusion (main spar)",
            "Full-batten grooves",
            "Spreader pad attachment points",
            "Halyard slots or external halyards",
        ],
        "wall_thickness_ranges_mm": [2.0, 2.5, 3.0, 3.5, 4.0],
        "corrosion_issues": [
            "Pitting corrosion (saltwater + crevices at rigging terminals)",
            "Galvanic corrosion (dissimilar metals: aluminum mast + stainless rigging)",
            "Exfoliation (subsurface corrosion, causes internal delamination)",
        ],
        "typical_defects": [
            "Corrosion staining (white/gray powder on surface — cosmetic or serious?)",
            "Cracking at spreader pad welds (stress concentration)",
            "Dent/ding (can initiate fatigue crack)",
            "Delamination (separation of extrusion layers, serious structural failure)",
        ],
        "inspection_points": [
            "Spreader pad area (weld quality, cracking)",
            "Upper extrusion (spreader attachment loads)",
            "Lower extrusion (mast step connection, bending stresses)",
            "Halyard exit areas (chafe, corrosion)",
            "External surface (corrosion pitting depth)",
        ],
        "fatigue_life": "100,000+ cycles (with proper rigging tension and tuning)",
        "maintenance": [
            "Post-season: thorough freshwater wash",
            "Annual: sand-blast + re-anodize corroded areas",
            "Quarterly: visual inspection for new corrosion",
        ],
        "cost_factor": 1.0,
        "notes": "Industry standard for cruising/racing. 50-year+ lifespan if well-maintained. Rigging mis-tuning causes premature failure.",
    },

    "carbon_fiber_mast": {
        "name": "Carbon Fiber Mast (Pultruded)",
        "german_name": "Kohlefaser-Mast",
        "material_spec": "Carbon fiber/epoxy composite, pultruded tube",
        "section_profiles": ["Streamlined airfoil shape", "Grooves for battens/halyards"],
        "wall_thickness_ranges_mm": [2.0, 2.5, 3.0],
        "advantages": [
            "1/3 weight of aluminum (mast weight = 10% of total rig weight reduction)",
            "Excellent stiffness (minimal sag, better sail shape)",
            "No corrosion (epoxy barrier)",
            "Better fatigue resistance (composite dampening)",
        ],
        "disadvantages": [
            "Extreme cost (2-4x aluminum)",
            "Brittle (prone to cracking from impact)",
            "Repair is complex/expensive (cannot weld, requires epoxy)",
            "Poor UV resistance (epoxy yellows/degrades, must protect)",
            "Galvanic issues less problematic (epoxy isolates)",
        ],
        "typical_defects": [
            "Delamination (separation of carbon fiber layers from epoxy)",
            "Micro-cracks (can propagate rapidly under load)",
            "Impact damage (keel strike, boom contact)",
            "Moisture ingress at terminal ends",
        ],
        "inspection_method": [
            "Visual: look for white stress marks (indicates delamination)",
            "Tap test: sound changes if delamination present",
            "Ultrasonic NDT: detects internal delamination (professional required)",
            "Dye penetrant: finds surface cracks (professional required)",
        ],
        "maintenance": [
            "UV cover when stored (essential, apply shade cloth or lazy jacks)",
            "Avoid impact (cannot tolerate boom contact, keel strike)",
            "Annual visual inspection for delamination",
            "Professional NDT every 5 years (racing) or 10 years (cruising)",
        ],
        "lifespan": "20+ years (if protected from UV and impact)",
        "cost_factor": 3.5,
        "notes": "Racing only. Weight savings are marginal on cruising boats. High cost limits use to high-performance racing.",
    },

    "wooden_mast_traditional": {
        "name": "Wooden Mast (Traditional)",
        "german_name": "Holzmast (Klassisch)",
        "material_spec": "Sitka spruce or Douglas fir, laminated or solid",
        "construction": [
            "Solid spar (traditional, single piece timber)",
            "Laminated (strips glued together for strength, flexibility)",
        ],
        "typical_dimensions": "Hollow box section, 40-80mm² cross-section",
        "corrosion_issues": [
            "Rot (fungal decay, occurs in damp areas without ventilation)",
            "Insect damage (termites, powder post beetles in tropical climates)",
            "Wood splitting (seasonal movement, shrinkage/expansion)",
        ],
        "typical_defects": [
            "Soft wood (rot from water intrusion at upper end)",
            "Crack propagation (shakes along grain, difficult to stop)",
            "Hardware corrosion (stainless bolts corrode wood underneath)",
            "Bent mast (overloaded or impact damage, permanent deformation)",
        ],
        "inspection_points": [
            "Upper extrusion (check for water staining, rot)",
            "Spreader pad area (moisture traps, rot starting point)",
            "Mast step connection (water pool, rot habitat)",
            "Hardware bolts (corrosion halo, wood staining beneath)",
            "Butt joint (laminated masts): check for glue line separation",
        ],
        "maintenance_critical": [
            "Varnish finish: sand + re-varnish annually (prevents rot)",
            "Drainage: ensure water does not pool at upper end",
            "Hardware: stainless only (remove all steel fasteners)",
            "Ventilation: circulate air inside hollow sections",
        ],
        "lifespan": "15-40 years (depends entirely on maintenance discipline)",
        "cost_factor": 1.2,
        "notes": "Requires discipline. Can last decades with meticulous care. Often seen on classic/traditional boats. Amateur maintenance = early failure.",
    },

    "aluminum_boom": {
        "name": "Aluminum Boom",
        "german_name": "Aluminium Baum",
        "material_grade": "6061-T6 (same as mast)",
        "section_profiles": ["Oval or round tube", "Clew attachment", "Outhaul attachment points"],
        "wall_thickness_mm": [2.0, 2.5, 3.0],
        "corrosion_issues": "Same as mast: pitting, galvanic corrosion with stainless fittings",
        "typical_defects": [
            "Corrosion pitting at gooseneck (splash zone)",
            "Bending (impact or excessive vang tension)",
            "Cracking at clew reinforcement (rigging loads)",
        ],
        "inspection_points": [
            "Gooseneck attachment (corrosion, cracking)",
            "Clew reinforcement (weld quality, cracking under load)",
            "Outhaul track (corrosion, stiffness)",
            "External surface (pitting depth)",
        ],
        "maintenance": [
            "Post-season: freshwater wash",
            "Annual: inspect for new corrosion",
            "Quarterly: visual check for bending",
        ],
        "lifespan": "30+ years (if maintained)",
        "cost_factor": 0.8,
        "notes": "Similar durability to mast. Lower loads make failure less common.",
    },

    "carbon_boom": {
        "name": "Carbon Boom",
        "german_name": "Kohlefaser-Baum",
        "material_spec": "Carbon fiber/epoxy composite",
        "section_profiles": ["Teardrop or round shape", "Lower weight than aluminum"],
        "advantages": [
            "Minimal weight (reduces imbalance aloft)",
            "Excellent stiffness (maintains mainsail shape)",
            "No corrosion",
        ],
        "disadvantages": [
            "High cost (2-3x aluminum)",
            "Brittleness (impact damage severe)",
            "Repair complexity",
        ],
        "typical_defects": [
            "Delamination (from impact or overload)",
            "Cracking at attachment points (stress concentration)",
            "Moisture ingress",
        ],
        "inspection_method": [
            "Visual: stress marks or color change",
            "Tap test: hollow sound indicates delamination",
            "Professional NDT (ultrasonic) for internal damage",
        ],
        "maintenance": [
            "UV protection (cover when stored)",
            "Avoid impact (keel strike, boom contact)",
            "Annual visual inspection",
        ],
        "lifespan": "20+ years",
        "cost_factor": 3.0,
        "notes": "Racing only. Weight savings marginal on cruising boats. Cost-benefit poor for most applications.",
    },

    "bowsprit_bugspriet": {
        "name": "Bowsprit / Bugspriet",
        "german_name": "Bugspriet / Bugspriet",
        "function": "Extends mast forward (increases sail area, lowers center of effort)",
        "material_options": ["Aluminum extrusion", "Carbon fiber", "Wood (rare)"],
        "length_options": ["1-2x foretriangle height"],
        "rigging_connections": [
            "Stay (forestay extension)",
            "Lower shrouds (diagonal stays)",
            "Gybe lines (control boom swing on downwind)",
        ],
        "typical_defects": [
            "Corrosion at outboard end (exposed to spray)",
            "Cracking at deck/bulwark penetration (stress concentration)",
            "Withdrawal from deck (fastening failure — dangerous)",
            "Bending from shock loads (jibe impact)",
        ],
        "inspection_points": [
            "Deck attachment bolts (must be tight, check monthly)",
            "Root area (cracking from bending loads)",
            "Outboard end (corrosion, wear at fairlead)",
            "Stay attachment points (corrosion, cracking)",
        ],
        "maintenance": [
            "Monthly: check bolt tightness (vibration can loosen)",
            "Quarterly: visual inspection for cracks",
            "Annual: re-seal if aluminum (protective coating)",
        ],
        "failure_consequence": "Catastrophic if separation occurs (mast loss likely)",
        "notes": "Critical safety item. Bolt failure = mast loss. Monthly inspection mandatory.",
    },
}

# ============================================================================
# SAIL_TYPES_AND_SYSTEMS — Segeltypen und Systeme
# ============================================================================

SAIL_TYPES_AND_SYSTEMS: Dict[str, Dict[str, Any]] = {
    "mainsail_full_batten": {
        "name": "Mainsail (Full-Batten Configuration)",
        "german_name": "Großsegel (Vollbattens)",
        "construction": "Full-length battens (7-9 batten pockets) + roach",
        "material_options": ["Dacron (cruising)", "Laminate (racing)", "Tri-radial weave"],
        "weight_oz_per_sqft": [4.5, 5.0, 5.5],
        "reef_system": ["Standard reef points (2-3 reefs)", "Slab reefing", "In-boom furling"],
        "furling_system_options": [
            "In-mast furling (vertical roller behind mast)",
            "In-boom furling (horizontal roller in boom)",
            "Traditional hanked sail (no furling)",
        ],
        "expected_lifespan_hours": {
            "racing": 300,
            "cruising": 1000,
        },
        "care_instructions": [
            "Dry before stowing (mildew risk if wet)",
            "Shade from sun when stored (UV fades/weakens)",
            "Inspect batten pockets monthly (stitching wear)",
            "Wash in saltwater rinse, dry thoroughly",
        ],
        "typical_defects": [
            "Batten pocket failure (stitching comes undone, batten falls out)",
            "Clew cringle separation (high-load point, stitching failure)",
            "Leech flutter (loss of roach shape, aerodynamic loss)",
            "Mildew (dark spots, indicates moisture + mold growth)",
            "UV damage (color fade = strength loss, superficial or deep?)",
        ],
        "notes": "Full battens increase sail longevity (10-20% longer life). Reefing is frequent operation (fatigue critical).",
    },

    "mainsail_in_mast_furling": {
        "name": "Mainsail (In-Mast Furling System)",
        "german_name": "Großsegel (Mast-Rollsystem)",
        "mechanism": "Vertical roller mechanism inside/behind mast, furls sail by rotating mast",
        "advantages": [
            "One-handed reefing (no boom jibing risk)",
            "Excellent for short-handed sailing",
            "Faster reefing (seconds vs minutes for traditional)",
        ],
        "disadvantages": [
            "Loss of roach (sail shape compromised when partial-furled)",
            "Batten pocket stress (battens bend sharply during furling)",
            "System complexity (more things to break)",
            "Mast rotation tolerance required (can induce vibration)",
        ],
        "typical_defects": [
            "Furling line jam (salt/sand intrusion in roller)",
            "Batten pocket cracking (repeated sharp bends)",
            "Mast bearing wear (rotation axis becomes rough)",
            "Leech flutter (seal strips wear, sail ruffles)",
        ],
        "maintenance": [
            "Monthly: test furling/unfurling (identify binding points)",
            "Quarterly: rinse furling mechanism with freshwater",
            "Annual: bearing inspection (replace if rough/noisy)",
            "Post-season: lubricate bearings (light machine oil only)",
        ],
        "expected_lifespan_hours": 800,
        "notes": "Convenient but mechanically complex. Batten pocket failure is common (10-20% shorter sail life vs traditional).",
    },

    "mainsail_in_boom_furling": {
        "name": "Mainsail (In-Boom Furling System)",
        "german_name": "Großsegel (Baum-Rollsystem)",
        "mechanism": "Horizontal roller inside boom, furls sail by rotating boom",
        "advantages": [
            "Safer than in-mast (boom-end visibility maintained)",
            "Better sail shape at partial reefing",
            "Lower aspect ratio roller (less stress than vertical)",
        ],
        "disadvantages": [
            "Boom must rotate 360° (higher bearing wear)",
            "Gooseneck stiffness (roller friction opposes boom movement)",
            "More complex rigging than traditional",
            "System weight (roller mechanism adds 20-30 lbs)",
        ],
        "typical_defects": [
            "Roller bearing wear (boom rotation becomes stiff)",
            "Sail shape loss (seal strips fail, wrinkles form)",
            "Furling line jam (salt intrusion in roller)",
            "Boom stiffness (crew struggles to trim mainsheet)",
        ],
        "maintenance": [
            "Monthly: furling test + lubrication",
            "Quarterly: bearing inspection",
            "Annual: seal strip replacement (critical for shape)",
        ],
        "expected_lifespan_hours": 900,
        "notes": "Better compromise between convenience and sail shape. More reliable than in-mast but still complex.",
    },

    "genoa_jib_sail": {
        "name": "Genoa / Jib Sail",
        "german_name": "Fock / Jib",
        "construction": "Hanked to foil or furler, batten-less (in most cases)",
        "material_options": ["Dacron (cruising)", "Laminate (racing)"],
        "overlap_percent": ["100% (jib, no overlap)", "120-150% (genoa, overlaps main)"],
        "expected_lifespan_hours": [600, 1000],
        "furling_system_options": [
            "Manual hank-on (hanks attach to stay, removable)",
            "Roller furler (mechanical or manual)",
            "Rod furler (high-tech racing)",
        ],
        "care_instructions": [
            "Dry completely before stowing (mildew risk critical)",
            "Inspect hanks/furler hardware monthly",
            "Wash with freshwater rinse (salt deposits weaken)",
            "UV protection (blue shade cloth when stored)",
        ],
        "typical_defects": [
            "Hank failure (spring hank cracks or opens)",
            "Leech flutter (loss of tension, aerodynamic loss)",
            "Clew cringle separation (stitching failure from load cycling)",
            "UV fading (coloration fade = strength loss in Dacron)",
            "Luff groove wear (from furler or hanks rubbing)",
        ],
        "notes": "Frequently changed sail (affects fatigue life). Hank quality critical.",
    },

    "code_0_sail": {
        "name": "Code 0 / Light-Air Reaching Sail",
        "german_name": "Code 0 / Leichtwind-Segel",
        "construction": "High-aspect-ratio, overlapping, batten-less",
        "material": "Light laminate (2-3 oz) or Dacron (2.5-3.5 oz)",
        "function": "Light-air reaching (5-12 knots apparent wind, 40-150° angle)",
        "expected_lifespan_hours": 200,
        "deployment": [
            "Hanked to foil (traditional)",
            "Furler on existing headstay (common)",
        ],
        "care_instructions": [
            "Store with shade protection (UV critical, 2-3x faster degradation)",
            "Dry completely (laminate delaminates if stored wet)",
            "Inspect stitching quarterly (light materials are vulnerable)",
        ],
        "typical_defects": [
            "Laminate delamination (moisture ingress, stitching leaks water)",
            "UV degradation (severe, fabric becomes brittle)",
            "Leech flutter (loose leech under weak wind)",
            "Batten pocket failure (if battened version)",
        ],
        "lifespan_racing": "1-2 seasons",
        "lifespan_cruising": "2-4 years",
        "notes": "Specialty sail. Fragile. High cost limits to racing boats. UV protection is critical.",
    },

    "gennaker_sail": {
        "name": "Gennaker (Asymmetric Hybrid)",
        "german_name": "Gennaker / Asym-Hybrid",
        "construction": "Hybrid of genoa + spinnaker, batten-less",
        "material": "Medium laminate or Dacron",
        "function": "Reaching sail (alternative to Code 0), easier to handle than spinnaker",
        "expected_lifespan_hours": 300,
        "advantages_over_spinnaker": [
            "One-person launch (pole not required)",
            "Easier trim (controls via sheets only)",
            "Safer downwind (less swing risk)",
        ],
        "disadvantages": [
            "Not as efficient as spinnaker downwind",
            "Can collapse in light/heavy wind",
            "Requires dedicated furler/snuffer system",
        ],
        "care_instructions": [
            "UV protection essential (store in shade)",
            "Dry before stowing",
            "Inspect sheet attachment points monthly",
        ],
        "typical_defects": [
            "Leech flutter",
            "UV fading (strength loss)",
            "Sheet attachment failure",
        ],
        "notes": "Growing in popularity. Good compromise for cruising boats avoiding full spinnaker complexity.",
    },

    "spinnaker_symmetric": {
        "name": "Spinnaker (Symmetric Pole)",
        "german_name": "Spinnaker (symmetrisch mit Paal)",
        "construction": "Balanced design, requires pole + guy for downwind flight",
        "material_options": ["Nylon (cruising, light)", "Laminate (racing)"],
        "weight_oz_per_sqft": [0.75, 1.0, 1.25],
        "pole_length": "Typically 70-100% of boom length",
        "expected_lifespan_hours": [200, 400],
        "deployment": [
            "Turtle bag (pack kept ready, quick launch)",
            "Pole trip (automatic release system for jibing)",
        ],
        "care_instructions": [
            "Dry immediately after use (nylon absorbs moisture)",
            "UV protection critical (store inside, away from sun)",
            "Patch any holes immediately (nylon rips propagate)",
            "Never allow to drag in water (salt intrusion damages nylon)",
        ],
        "typical_defects": [
            "Leech leak (stitching separates, sail fills with air incorrectly)",
            "Pole fittings corrode (stainless only)",
            "Rip propagation (small hole becomes large tear quickly)",
            "Shrinking (nylon shrinks if stored wet)",
        ],
        "lifespan_racing": "1-2 seasons (frequent use = fatigue)",
        "lifespan_cruising": "3-5 years (occasional use)",
        "notes": "Specialized sail. Requires pole + rigging knowledge. Expensive (often cheapest new purchase option).",
    },

    "spinnaker_asymmetric": {
        "name": "Spinnaker (Asymmetric / Free-Flying)",
        "german_name": "Spinnaker (asymmetrisch / Freiliegend)",
        "construction": "Asymmetric design, hanked to foil or furler, no pole",
        "material_options": ["Nylon (cruising)", "Laminate (racing)"],
        "advantages": [
            "No pole required (easier launch/jibe)",
            "Hanked to foil (reusable furler)",
            "Single-handed deployment possible",
        ],
        "disadvantages": [
            "Less efficient downwind than symmetric (lower sail area)",
            "More complex trimming (2x halyards/guys typically)",
            "Not suitable for very deep downwind (200°+)",
        ],
        "expected_lifespan_hours": [250, 500],
        "care_instructions": [
            "Dry immediately (nylon moisture = shrinking + rot)",
            "UV protection (critical, same as symmetric)",
            "Inspect foil/furler hardware monthly",
        ],
        "typical_defects": [
            "Leech leak",
            "Furler/hanks corrosion",
            "Rip propagation",
            "Luff tape wear (from furler sliding)",
        ],
        "notes": "Growing in popularity. Easier than symmetric pole-based system. Good for cruising.",
    },

    "storm_jib": {
        "name": "Storm Jib (Heavy-Air Escape Sail)",
        "german_name": "Sturmsegel / Notfock",
        "construction": "Very small, heavily-reinforced jib (typically 3-5% of mainsail area)",
        "material": "Heavy Dacron (6-8 oz) or aramid laminate",
        "typical_size": "60-150 sq ft (varies by boat)",
        "function": "Emergency heavy-air sail when main + genoa become unmanageable",
        "deployment": [
            "Hanked to inner stay (if installed)",
            "Furled on forestay behind working genoa",
        ],
        "care_instructions": [
            "Inspect annually (stored most of season)",
            "Keep dry (mildew risk is high with infrequent use)",
            "UV protection essential (sits folded, one side exposed)",
        ],
        "typical_defects": [
            "Mildew (from storage moisture)",
            "Hank corrosion (sitting in storage, salt residue)",
            "Batten pocket stitching failure (rarely used, stitching weakens)",
        ],
        "replacement_interval": "5-10 years (infrequent use = slow aging)",
        "notes": "Insurance policy. Rarely needed. Proper storage critical (dry, shaded, ventilated).",
    },

    "trysail": {
        "name": "Trysail (Heavy-Air Fore-and-Aft Sail)",
        "german_name": "Besan / Sturmsegel",
        "construction": "Small sail set on independent track/boom, not in mast",
        "material": "Heavy Dacron (7-9 oz)",
        "function": "Ultra-heavy-air storm sail (deployed when storm jib + reefed main inadequate)",
        "typical_area": "10-20% of mainsail area",
        "deployment": [
            "Separate track on mast (racing boats, high-end cruising)",
            "Rigged independently, independent boom or mast track",
        ],
        "care_instructions": [
            "Stored folded (minimal handling)",
            "Dry, shaded storage (mildew/UV risk)",
            "Annual visual inspection",
        ],
        "typical_defects": [
            "Mildew (storage moisture)",
            "Track corrosion (salt deposits)",
        ],
        "replacement_interval": "10+ years (very infrequent use)",
        "notes": "Specialized sail. Found mainly on larger offshore cruising or racing boats. Rarely deployed.",
    },
}

# ============================================================================
# RIGGING_INSPECTION — Rigg-Inspektion und Zustand
# ============================================================================

RIGGING_INSPECTION: Dict[str, Any] = {
    "visual_inspection_checklist": {
        "masthead_area": [
            "Sheave box: sheaves rotate freely (hand test, 2+ second coast)",
            "Sheave box bolts: tight (wrench-test, no hand tightening allowed)",
            "Upper spreader pad: cracks visible? weld quality?",
            "Standing rigging terminals: gaps at swage? corrosion?",
        ],
        "spreader_inspection": [
            "Spreader straightness: sight along spar from mast",
            "Spreader hardware: tight bolts, no cracks at pad",
            "Spreader tips: leather pads intact (prevent rigging chafe)",
            "Diagonal stays: no kinks or bends visible",
        ],
        "chainplate_area": [
            "Stainless bolts: corrosion-free (white corrosion = problem)",
            "Body hardware: cracks or deformation visible?",
            "Sealant: cracked or missing (water intrusion risk)",
            "Turnbuckle cotter pins: in place, fully spread",
        ],
        "swage_terminal_ends": [
            "Cone/barrel: gaps between pieces? (indicates under-swaging)",
            "Corrosion: pitting under terminal (crevice corrosion)",
            "Wire strands: any pulled/loose? (indicates movement)",
            "Termination finish: smooth or rough transitions (stress riser)?",
        ],
        "mast_condition": [
            "Corrosion: white/gray powder visible? depth?",
            "Dents: presence, depth, sharp vs rounded edges",
            "Bending: sight along full length (compare to baseline)",
            "Cracking: any visible cracks (major red flag)",
        ],
        "boom_condition": [
            "Corrosion: pitting at gooseneck (splash zone)",
            "Bend: sight along full length",
            "Clew reinforcement: any cracking visible?",
            "Hardware attachment: bolts tight, no movement",
        ],
    },

    "ndt_methods": {
        "dye_penetrant": {
            "principle": "Colored dye enters surface cracks, reveals flaws via washoff",
            "application": "Swage terminals, rod rigging, mast welds",
            "procedure": [
                "1. Clean surface thoroughly (degreaser, wire brush)",
                "2. Apply red penetrant dye (wait 10-30 min)",
                "3. Wipe excess dye off",
                "4. Apply white developer powder",
                "5. Cracks appear as red lines on white background",
            ],
            "sensitivity": "Detects surface cracks > 0.5mm",
            "cost_per_inspection_usd": 150,
            "limitation": "Cannot detect subsurface defects (below surface)",
        },

        "magnetic_particle": {
            "principle": "Magnetic field attracts iron particles to surface flaws",
            "application": "Steel rigging (galvanized wire), magnetic materials only",
            "procedure": [
                "1. Magnetize component (permanent magnet or electromagnet)",
                "2. Dust with ferrous particles (iron powder)",
                "3. Particles cluster at cracks/defects",
                "4. Photograph or document findings",
            ],
            "sensitivity": "Detects cracks, subsurface inclusions",
            "cost_per_inspection_usd": 120,
            "limitation": "Cannot be used on non-magnetic stainless steel (majority of modern rigging)",
        },

        "ultrasonic_testing": {
            "principle": "Sound waves detect internal material discontinuities",
            "application": "Rod rigging (Nitronic 50), carbon fiber masts, aluminum spars",
            "procedure": [
                "1. Couple transducer to material (ultrasonic gel)",
                "2. Send ultrasonic pulse through material",
                "3. Measure return reflections (flaws show as echoes)",
                "4. Compare to baseline (healthy material signature)",
            ],
            "detects": ["Delamination", "Cracks", "Corrosion pitting depth", "Voids"],
            "cost_per_inspection_usd": 250,
            "limitation": "Requires calibration/comparison baseline, expensive equipment",
        },

        "thermal_imaging": {
            "principle": "Infrared detects temperature differences (cracks/voids show as hot/cold spots)",
            "application": "Carbon fiber structures, composite masts",
            "procedure": [
                "1. Heat material (sun exposure or heat gun)",
                "2. Scan with thermal camera",
                "3. Delaminated areas show as cooler regions",
            ],
            "sensitivity": "Detects subsurface delamination, voids",
            "cost_per_inspection_usd": 180,
        },
    },

    "load_testing_procedure": {
        "purpose": "Verify rigging breaking load & identify marginal components",
        "procedure": [
            "1. Select load cell (0-10 ton rating typical)",
            "2. Rig load cell between component and anchor point",
            "3. Apply increasing load (50% → 75% → 90% → 100% MWL)",
            "4. Hold at each level, monitor for movement/creep",
            "5. Photograph any visible deformation or slipping",
        ],
        "acceptance_criteria": [
            "No visible movement (terminal doesn't slip/rotate)",
            "No permanent elongation (component returns to length after load release)",
            "Load reaches 90% of wire breaking load without failure",
        ],
        "failure_indicators": [
            "Terminal slips out of swage (under-swaging)",
            "Rod threads strip (over-torqued)",
            "Mechanical terminal loosens (under-tightened)",
        ],
        "cost_per_test_usd": 300,
        "typical_scope": "Test 2-3 critical terminals per inspection (total: $600-900)",
    },

    "failure_warning_signs": {
        "imminent_failure": [
            "Terminal pulling out of swage (white/shiny wire core visible, >2mm protrusion)",
            "Visible crack at terminal (NDT-confirmed crack)",
            "Rod rigging thread stripping (cannot tighten, spinning freely)",
            "Mast buckle (S-curve visible when sighting along spar)",
            "Spreader crack at base (>50% through wall thickness)",
            "Shroud/stay bent at acute angle (kink visible, not gradual curve)",
        ],
        "action_required": "Do not sail. Rig temporary support. Replace immediately.",

        "significant_concern": [
            "Terminal corrosion with pitting (white powder visible under fitting)",
            "Wire fuzz/fraying (indicating UV damage or mechanical abrasion)",
            "Stretch/creep (rigging tension drops between tuning intervals)",
            "Loose turnbuckle cotter pin (missing, unspreads)",
            "Mast bending (>1% curvature, increases with load)",
        ],
        "action_required": "Inspect under load. Plan replacement. Do not sail hard.",

        "monitor": [
            "Minor corrosion staining (cosmetic, no depth)",
            "Small dent in mast (no crack, aluminum only)",
            "Slightly fuzzy halyard (minor UV, still functional)",
            "Turnbuckle tension drift (normal, retension needed)",
        ],
        "action_required": "Document, monitor, plan maintenance.",
    },

    "inspection_frequency_schedule": {
        "daily_before_sailing": [
            "Mast straightness (sight along from cabin)",
            "Visible cracks or bends (quick visual scan)",
            "Cotter pins in place (spreader shroud pins, turnbuckles)",
        ],

        "weekly": [
            "Sheave rotation test (mast top accessible, hand-spin each)",
            "Cleat/winch jaw condition (visual, is rope fuzzing?)",
            "Halyard/sheet wear assessment (fuzzing, diameter loss)",
            "Mast cleanliness (rinse mast top to remove salt)",
        ],

        "monthly": [
            "Complete rig walkabout (deck circuit + aloft inspection)",
            "Turnbuckle cotter pin count (each should be in place)",
            "Swage terminal pull-test (gentle hand pull, verify no slipping)",
            "Track/car system inspection (blocks rotate freely?)",
            "Boom gooseneck bolt tightness (wrench test)",
        ],

        "quarterly": [
            "Spreader pad weld inspection (crack emergence early detection)",
            "Chainplate area corrosion assessment (white staining = pitting?)",
            "Rod rigging thread inspection (visual, no corrosion seizing)",
            "Sail damage assessment (holes, stitching, batten pocket condition)",
            "Halyard/sheet condition decision (replace now? next season?)",
        ],

        "annually_post_season": [
            "Professional full rig inspection (NDT recommended every 3-5 years)",
            "Mast removal & detailed inspection (best access for damage detection)",
            "Terminal replacement assessment (5-10 year intervals typical)",
            "Standing rigging strength evaluation (load test, NDT)",
            "Mast/boom finish restoration (anodizing, varnish, epoxy)",
        ],
    },
}

# ============================================================================
# ASSESSMENT FUNCTION
# ============================================================================

def assess_rigging_condition(
    observations: Dict[str, Any],
    boat_age_years: int = 10,
    sailing_intensity: str = "cruising",  # "racing" or "cruising"
) -> Dict[str, Any]:
    """
    Comprehensive rigging condition assessment.

    observations: Dict with keys like "mast_corrosion", "spreader_crack", etc.
    boat_age_years: Age of vessel (context for component life)
    sailing_intensity: "racing" (frequent, hard) or "cruising" (occasional)

    Returns: Dict with score (0-100), findings, recommendations
    """

    score = 100
    findings = []
    recommendations = []
    urgency = "green"  # "green" (monitor), "yellow" (plan), "red" (immediate action)

    # Standing rigging assessment
    if "terminal_corrosion" in observations and observations["terminal_corrosion"]:
        score -= 15
        findings.append("Terminal corrosion detected (pitting). Indicates poor drainage/sealing.")
        recommendations.append("Inspect under load. Plan replacement in 6-12 months.")
        urgency = "yellow"

    if "terminal_pulling" in observations and observations["terminal_pulling"]:
        score -= 40
        findings.append("CRITICAL: Terminal pulling out of swage. Imminent failure risk.")
        recommendations.append("DO NOT SAIL. Replace wire immediately.")
        urgency = "red"

    if "mast_crack" in observations and observations["mast_crack"]:
        score -= 50
        findings.append("CRITICAL: Mast crack detected. Structural failure risk.")
        recommendations.append("DO NOT SAIL. Professional repair or replacement required.")
        urgency = "red"

    if "mast_bending" in observations and observations["mast_bending"] > 1.0:
        score -= 20
        findings.append(f"Mast bending: {observations['mast_bending']}% curvature. Indicates rig mis-tune or overload.")
        recommendations.append("Check shroud tension. Verify spreader geometry.")
        urgency = "yellow"

    if "spreader_crack" in observations and observations["spreader_crack"]:
        score -= 25
        findings.append("Spreader pad crack. Load concentration point.")
        recommendations.append("Monitor closely. Replace spreader at next maintenance window.")
        urgency = "yellow"

    if "halyard_fuzz" in observations and observations["halyard_fuzz"]:
        score -= 10
        findings.append("Halyard fuzz detected. UV damage or mechanical abrasion.")
        recommendations.append("Replace halyard at end of season.")
        urgency = "green"

    if "cleat_slipping" in observations and observations["cleat_slipping"]:
        score -= 15
        findings.append("Cleat/winch jaw slipping. Jaw is glazed.")
        recommendations.append("Replace cleat pads immediately (safety-critical item).")
        urgency = "yellow"

    # Age-based score adjustment
    if boat_age_years > 20 and sailing_intensity == "racing":
        score -= 10
        findings.append(f"Boat age {boat_age_years} years + racing use. Risk of fatigue cracks increased.")
        recommendations.append("Professional NDT inspection recommended (rod rigging, mast welds).")

    if boat_age_years > 30:
        score -= 15
        findings.append("Boat age > 30 years. Major component replacement may be overdue.")
        recommendations.append("Full rig inspection and life assessment recommended.")

    return {
        "overall_score": max(0, score),
        "condition_rating": "Excellent" if score >= 90 else "Good" if score >= 75 else "Fair" if score >= 50 else "Poor",
        "urgency": urgency,
        "findings": findings,
        "recommendations": recommendations,
        "next_inspection_months": 12 if urgency == "green" else 6 if urgency == "yellow" else 0,
    }


# ============================================================================
# END OF FILE
# ============================================================================
