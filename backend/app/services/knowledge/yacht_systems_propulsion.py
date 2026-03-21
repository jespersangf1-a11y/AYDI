"""
AYDI Yacht Antriebs- und Motorsysteme Knowledge Base
Propulsion, engine systems and drive trains for yacht design analysis
Author: Master Marine Engineer KnowledgeBase
Version: 1.0

Encyclopedic reference for marine propulsion engineering with specifications
for diesel inboards, electric drives, saildrives, and hybrid systems.
"""

from typing import Dict, List, Any, Tuple
from enum import Enum
from dataclasses import dataclass


# ============================================================================
# ENGINE TYPES — Motortypen Marine
# ============================================================================

@dataclass
class EngineSpecification:
    """Marine engine technical specification"""
    type_name: str
    manufacturer: str
    model: str
    power_hp: int
    rpm_range: Tuple[int, int]
    fuel_consumption_l_per_h_per_hp: float
    weight_kg_per_hp: float
    cooling_system: str
    typical_boat_class: str
    displacement_cc: int
    cylinders: int
    maintenance_schedule_hours: Dict[int, List[str]]
    common_failures: List[str]
    lifespan_hours: int
    emissions_tier: str


# Inboard Diesel Naturally Aspirated
YANMAR_3JH40_SAILDRIVE = {
    "type_name": "Inboard Diesel Saildrive (Naturally Aspirated)",
    "manufacturer": "Yanmar",
    "model": "3JH40",
    "power_hp": 40,
    "rpm_range": (800, 3600),
    "fuel_consumption_l_per_h_per_hp": 0.185,
    "weight_kg_per_hp": 1.85,
    "cooling_system": "Raw water with heat exchanger indirect",
    "typical_boat_class": "Cruising sailboat 35-45ft",
    "displacement_cc": 1077,
    "cylinders": 3,
    "maintenance_schedule_hours": {
        100: ["Check fuel filter water separator", "Check impeller condition"],
        200: ["Replace fuel filter element", "Inspect raw water strainer"],
        500: ["Change engine oil and filter", "Check zinc anodes"],
        1000: ["Replace impeller", "Inspect cooling system heat exchanger"],
        2000: ["Complete overhaul inspection", "Transmission fluid change"],
    },
    "common_failures": [
        "Impeller failure (200 hour intervals critical)",
        "Raw water strainer blockage from debris",
        "Zinc anode erosion in seawater cooling",
        "Saildrive coupling corrosion",
        "Thermostat sticking (trapped air in cooling)",
    ],
    "lifespan_hours": 10000,
    "emissions_tier": "IMO Tier II",
    "gearbox": {"type": "Saildrive integrated", "ratio": 2.03},
}

VOLVO_PENTA_D2_40_SAILDRIVE = {
    "type_name": "Inboard Diesel Saildrive (Naturally Aspirated)",
    "manufacturer": "Volvo Penta",
    "model": "D2-40",
    "power_hp": 40,
    "rpm_range": (800, 3600),
    "fuel_consumption_l_per_h_per_hp": 0.190,
    "weight_kg_per_hp": 1.95,
    "cooling_system": "Keel cooler + raw water",
    "typical_boat_class": "Cruising sailboat 35-45ft",
    "displacement_cc": 1171,
    "cylinders": 3,
    "maintenance_schedule_hours": {
        100: ["Inspect fuel filter condition"],
        200: ["Replace fuel filter", "Inspect impeller"],
        500: ["Change engine oil", "Check sacrificial anodes"],
        1000: ["Replace impeller (mandatory)", "Saildrive coupling inspection"],
        2000: ["Major service: transmission oil, seals"],
    },
    "common_failures": [
        "Saildrive seal leakage (normal wear, replace every 2000h)",
        "Propeller cavitation damage (pitch too aggressive)",
        "Cooling water blockage from biofouling",
        "Corrosion in keel cooling tube",
    ],
    "lifespan_hours": 12000,
    "emissions_tier": "IMO Tier II",
    "gearbox": {"type": "Saildrive integrated", "ratio": 2.00},
}

# Inboard Diesel Turbocharged
BETA_50_TURBO = {
    "type_name": "Inboard Diesel Turbocharged",
    "manufacturer": "Beta Marine",
    "model": "50 Turbo (Cummins 3B3.8)",
    "power_hp": 50,
    "rpm_range": (1200, 3200),
    "fuel_consumption_l_per_h_per_hp": 0.195,
    "weight_kg_per_hp": 1.60,
    "cooling_system": "Indirect closed-loop with keel cooling option",
    "typical_boat_class": "Motorsailer 40-50ft",
    "displacement_cc": 3800,
    "cylinders": 3,
    "maintenance_schedule_hours": {
        100: ["Monitor boost pressure (3.0-3.5 bar normal)"],
        200: ["Replace engine oil and oil filter"],
        500: ["Inspect turbo lubrication lines for sludge"],
        1000: ["Replace fuel filter element", "Check intercooler fins"],
        2000: ["Turbo inspection by specialist"],
    },
    "common_failures": [
        "Turbocharger bearing wear (lack of cooldown after high load)",
        "Carbon buildup in EGR system (poor fuel quality)",
        "Intercooler blockage from salt corrosion",
        "Wastegate sticking (carbon deposits)",
    ],
    "lifespan_hours": 8000,
    "emissions_tier": "IMO Tier II (with EGR)",
    "gearbox": {"type": "ZF Marine 25M", "ratio": 2.17},
}

NANNI_N2_14_TURBO = {
    "type_name": "Inboard Diesel Turbocharged",
    "manufacturer": "Nanni",
    "model": "N2.14 Turbo",
    "power_hp": 14,
    "rpm_range": (2200, 3600),
    "fuel_consumption_l_per_h_per_hp": 0.210,
    "weight_kg_per_hp": 2.1,
    "cooling_system": "Raw water with keel cooler",
    "typical_boat_class": "Cruising sailboat 30-35ft",
    "displacement_cc": 1432,
    "cylinders": 2,
    "maintenance_schedule_hours": {
        100: ["Check turbo boost gauge"],
        200: ["Fuel filter inspection and drain water"],
        500: ["Engine oil change"],
        1000: ["Turbo cooling line inspection"],
    },
    "common_failures": [
        "Turbo seal degradation in salty environment",
        "Heat exchanger scaling from poor water treatment",
        "Prop shaft misalignment causing vibration stress",
    ],
    "lifespan_hours": 7000,
    "emissions_tier": "IMO Tier I",
    "gearbox": {"type": "Saildrive integrated", "ratio": 2.38},
}

# Outboard Engines
YAMAHA_F250_OUTBOARD = {
    "type_name": "Outboard 4-Stroke High Performance",
    "manufacturer": "Yamaha",
    "model": "F250 VMAX SHO",
    "power_hp": 250,
    "rpm_range": (5000, 6100),
    "fuel_consumption_l_per_h_per_hp": 0.280,
    "weight_kg": 280,
    "cooling_system": "Thermostat raw water circulation",
    "typical_boat_class": "Performance planing boat 30-45ft",
    "displacement_cc": 2494,
    "cylinders": 4,
    "maintenance_schedule_hours": {
        50: ["Check lower unit oil", "Inspect anodes"],
        100: ["Spark plug inspection"],
        200: ["Change engine oil", "Inspect water pump impeller"],
        500: ["Complete lower unit service"],
    },
    "common_failures": [
        "Water pump impeller wear (saltwater, 200h intervals)",
        "Lower unit seal failure causing oil loss",
        "Fuel injector clogging from ethanol fuel",
    ],
    "lifespan_hours": 2000,
    "emissions_tier": "EPA Tier 3",
    "gearbox": {"type": "Shift integrated", "ratio": 1.85},
}

MERCURY_90_HP_4STROKE = {
    "type_name": "Outboard 4-Stroke Mid-Range",
    "manufacturer": "Mercury Marine",
    "model": "90 ELPT EFI",
    "power_hp": 90,
    "rpm_range": (4750, 6050),
    "fuel_consumption_l_per_h_per_hp": 0.265,
    "weight_kg": 120,
    "cooling_system": "Raw water with anode protection",
    "typical_boat_class": "Center console 25-35ft",
    "displacement_cc": 1496,
    "cylinders": 4,
    "maintenance_schedule_hours": {
        100: ["Check water pump output", "Zinc anode inspection"],
        200: ["Oil and filter change"],
        500: ["Impeller replacement (critical)"],
    },
    "common_failures": [
        "Corrosion in cooling passages (inadequate anode)",
        "Impeller degradation in debris-filled water",
    ],
    "lifespan_hours": 2500,
    "emissions_tier": "EPA Tier 3",
    "gearbox": {"type": "Shift integrated", "ratio": 1.98},
}


# ============================================================================
# ELECTRIC PROPULSION — Elektrischer Antrieb
# ============================================================================

TORQEEDO_DEEP_SKY_50KW = {
    "type_name": "Electric Pod Motor",
    "manufacturer": "Torqeedo",
    "model": "Deep Sky 50kW",
    "power_kw": 50,
    "power_hp": 67,
    "rpm_range": (0, 4500),
    "motor_type": "Brushless AC induction",
    "weight_kg": 180,
    "cooling_system": "Integrated water cooling",
    "typical_boat_class": "Motorsailer or trawler 40-55ft",
    "battery_requirement_kwh": 150,
    "range_nm_at_hull_speed": 45,
    "regeneration_capable": True,
    "maintenance_schedule_hours": {
        500: ["Battery health check via BMS"],
        1000: ["Motor bearing inspection (no wear typical)"],
        2000: ["Propeller inspection and cleaning"],
    },
    "common_failures": [
        "Battery capacity degradation (80% at 2000 cycle)",
        "Propeller fouling (weeds, rope)",
        "Water ingress seal failure (rare, rated IP67)",
    ],
    "lifespan_hours": 5000,
    "cost_usd": 85000,
    "efficiency_percent": 92,
}

EPROPULSION_AQUA40 = {
    "type_name": "Electric Pod Motor Compact",
    "manufacturer": "ePropulsion",
    "model": "Aqua 40 Plus",
    "power_kw": 40,
    "power_hp": 54,
    "rpm_range": (0, 4500),
    "motor_type": "Brushless AC permanent magnet",
    "weight_kg": 65,
    "cooling_system": "Passive water cooling fins",
    "typical_boat_class": "Cruising sailboat 35-45ft",
    "battery_requirement_kwh": 75,
    "range_nm_at_hull_speed": 35,
    "regeneration_capable": False,
    "maintenance_schedule_hours": {
        500: ["Battery voltage equilibrium check"],
        1000: ["Motor temp sensor calibration"],
    },
    "common_failures": [
        "Battery overheating in tropical waters",
        "Firmware update requirement for battery compatibility",
    ],
    "lifespan_hours": 4000,
    "cost_usd": 42000,
    "efficiency_percent": 91,
}

FISCHER_PANDA_HYBRID_GENSET = {
    "type_name": "Hybrid Diesel-Electric Genset",
    "manufacturer": "Fischer Panda",
    "model": "Greenline 32 (Hybrid)",
    "power_kw_diesel": 32,
    "power_kw_electric": 15,
    "diesel_fuel_consumption_l_per_h": 7.5,
    "electric_battery_kwh": 50,
    "motor_type": "Brushless AC",
    "weight_kg": 450,
    "cooling_system": "Closed-loop with waste heat recovery",
    "typical_boat_class": "Trawler or motorsailer 45-65ft",
    "range_nm_pure_electric": 25,
    "regeneration_capable": True,
    "maintenance_schedule_hours": {
        100: ["Diesel fuel quality check", "Battery state of charge"],
        500: ["Genset service interval", "Cooling system flush"],
        1000: ["Motor and alternator bearing inspection"],
    },
    "common_failures": [
        "Inverter overheating (poor ventilation)",
        "Battery management system communication loss",
        "Diesel fuel degradation if not run monthly",
    ],
    "lifespan_hours": 8000,
    "cost_usd": 95000,
}


# ============================================================================
# DRIVE TRAINS — Antriebsstrang
# ============================================================================

DRIVE_TRAIN_TYPES = {
    "saildrive_volvo_sd130": {
        "name": "Saildrive Volvo SD130",
        "type": "Through-keel saildrive",
        "shaft_diameter_mm": 24,
        "alignment_tolerance_mm": 0.5,
        "bearing_types": ["Rubber bushing forward", "Oil-lubricated shaft bearing"],
        "coupling_type": "Integral flexible coupling",
        "propeller_mounting": "Internal saildrive prop cone",
        "efficiency_percent": 88,
        "typical_power_hp": 30,
        "gearbox_integrated": True,
        "maintenance_interval_hours": 1000,
        "seal_replacement_hours": 2000,
        "common_wear": ["Propeller cone slip", "Seal leakage normal aging"],
        "noise_db_at_full_rpm": 82,
        "vibration_rating": "Very low (0.5mm/s)",
        "cost_usd": 6500,
    },
    "saildrive_volvo_sd150": {
        "name": "Saildrive Volvo SD150",
        "type": "Through-keel saildrive heavy duty",
        "shaft_diameter_mm": 28,
        "alignment_tolerance_mm": 0.4,
        "bearing_types": ["Composite forward bearing", "Oil-lubricated rear"],
        "coupling_type": "Rigid coupling with damper",
        "propeller_mounting": "External prop cone for larger props",
        "efficiency_percent": 89,
        "typical_power_hp": 55,
        "gearbox_integrated": True,
        "maintenance_interval_hours": 1000,
        "seal_replacement_hours": 2500,
        "common_wear": ["Bearing pocket erosion in heavy seas"],
        "noise_db_at_full_rpm": 80,
        "vibration_rating": "Very low (0.4mm/s)",
        "cost_usd": 8200,
    },
    "saildrive_yanmar_sd60": {
        "name": "Saildrive Yanmar SD60",
        "type": "Through-keel saildrive universal",
        "shaft_diameter_mm": 22,
        "alignment_tolerance_mm": 0.6,
        "bearing_types": ["Rubber composite bearing"],
        "coupling_type": "Flexible rubber coupling",
        "propeller_mounting": "Integral saildrive cone",
        "efficiency_percent": 86,
        "typical_power_hp": 40,
        "gearbox_integrated": True,
        "maintenance_interval_hours": 500,
        "seal_replacement_hours": 1500,
        "common_wear": ["Rubber bearing degradation in tropics"],
        "noise_db_at_full_rpm": 84,
        "vibration_rating": "Low (0.8mm/s)",
        "cost_usd": 5800,
    },
    "conventional_shaft_drive": {
        "name": "Conventional Shaft Drive",
        "type": "Through-stern shaft with external rudder",
        "shaft_diameter_mm": 30,
        "alignment_tolerance_mm": 0.25,
        "bearing_types": ["Cutless rubber bearing (keel)", "Stern tube bearing"],
        "coupling_type": "Flexible shaft coupling (rubber insert)",
        "propeller_mounting": "Direct on shaft (nut/key)",
        "efficiency_percent": 92,
        "typical_power_hp": 75,
        "gearbox_integrated": False,
        "maintenance_interval_hours": 500,
        "seal_replacement_hours": 3000,
        "common_wear": ["Cutless bearing erosion (sailboat vibration)", "Stern tube seal leakage"],
        "noise_db_at_full_rpm": 86,
        "vibration_rating": "Moderate (1.2mm/s)",
        "cost_usd": 7500,
        "requires_separate_gearbox": True,
    },
    "v_drive_inboard": {
        "name": "V-Drive Inboard",
        "type": "Engine forward, drive aft (reverse through transom)",
        "shaft_diameter_mm": 32,
        "alignment_tolerance_mm": 0.3,
        "bearing_types": ["Main engine rubber mounts", "Thrust bearing in gearbox"],
        "coupling_type": "Rigid with vibration damper",
        "propeller_mounting": "Vertical shaft cone",
        "efficiency_percent": 87,
        "typical_power_hp": 200,
        "gearbox_integrated": True,
        "maintenance_interval_hours": 100,
        "seal_replacement_hours": 1000,
        "common_wear": ["Engine mount failure (high thrust)", "Transmission overheating"],
        "noise_db_at_full_rpm": 88,
        "vibration_rating": "Moderate-high (1.5mm/s)",
        "cost_usd": 12000,
    },
    "pod_drive_volvo_ips": {
        "name": "Pod Drive Volvo IPS (Inboard Performance System)",
        "type": "Submerged pod with dual propellers",
        "shaft_diameter_mm": "Integrated",
        "alignment_tolerance_mm": 0.1,
        "bearing_types": ["Sealed spherical bearing", "Integrated thrust assembly"],
        "coupling_type": "Integral flexible joint",
        "propeller_mounting": "Dual counter-rotating props",
        "efficiency_percent": 95,
        "typical_power_hp": 370,
        "gearbox_integrated": True,
        "maintenance_interval_hours": 500,
        "seal_replacement_hours": 2000,
        "common_wear": ["Propeller cavitation (speed tuning critical)"],
        "noise_db_at_full_rpm": 79,
        "vibration_rating": "Very low (0.2mm/s)",
        "cost_usd": 45000,
    },
    "jet_drive": {
        "name": "Jet Drive (Water Jet)",
        "type": "Submerged intake, high-speed discharge",
        "shaft_diameter_mm": "Integrated pump",
        "alignment_tolerance_mm": 0.2,
        "bearing_types": ["Sealed pump bearings"],
        "coupling_type": "Direct flexible drive",
        "propeller_mounting": "Impeller internal",
        "efficiency_percent": 78,
        "typical_power_hp": 350,
        "gearbox_integrated": True,
        "maintenance_interval_hours": 200,
        "seal_replacement_hours": 1500,
        "common_wear": ["Impeller erosion (sand/debris)", "Intake grate blockage"],
        "noise_db_at_full_rpm": 92,
        "vibration_rating": "Low (0.6mm/s)",
        "cost_usd": 38000,
    },
}


# ============================================================================
# PROPELLERS — Propeller
# ============================================================================

PROPELLER_TYPES = {
    "fixed_2blade_bronze": {
        "name": "Fixed 2-Blade Bronze Propeller",
        "type": "Fixed pitch, 2 blade",
        "material": "Manganese bronze (CuZnNi)",
        "typical_diameter_inches": (12, 14, 16, 18),
        "pitch_range_inches": (10, 12, 14, 16),
        "efficiency_percent": 55,
        "drag_when_sailing_percent_extra_resistance": 8,
        "cavitation_resistance": "Good (low speed)",
        "common_failures": [
            "Hub corrosion (inadequate zinc)",
            "Blade erosion from cavitation (high-speed boats)",
            "Root crack from cyclic stress",
        ],
        "maintenance": [
            "Zinc anodes replacement yearly (seasonal)",
            "Antifouling paint every season",
            "Balance check if vibration increases",
        ],
        "brands": ["Bruntons", "Martyr", "Automat"],
        "cost_usd": 400,
    },
    "fixed_3blade_nibral": {
        "name": "Fixed 3-Blade Nibral Propeller",
        "type": "Fixed pitch, 3 blade",
        "material": "Nickel-Aluminum-Bronze (Nibral)",
        "typical_diameter_inches": (12, 14, 16, 18, 20),
        "pitch_range_inches": (10, 12, 14, 16, 18),
        "efficiency_percent": 62,
        "drag_when_sailing_percent_extra_resistance": 12,
        "cavitation_resistance": "Excellent (high speed)",
        "common_failures": [
            "Hub corrosion (even with zincs in contaminated water)",
            "Dezincification in Cu-based alloys",
        ],
        "maintenance": [
            "Zinc anode replacement every 6-12 months (depends on location)",
            "Polish and antifouling paint seasonally",
            "Dynamic balancing after damage",
        ],
        "brands": ["MAX-PROP", "Gori", "Flex-O-Fold", "Automat"],
        "cost_usd": 650,
    },
    "folding_2blade": {
        "name": "Folding 2-Blade Propeller",
        "type": "Folding, reduces drag sailing",
        "material": "Stainless steel or bronze blades, steel hub",
        "typical_diameter_inches": (10, 12, 14),
        "pitch_range_inches": (8, 10, 12, 14),
        "efficiency_percent": 50,
        "drag_when_sailing_percent_extra_resistance": 2,
        "cavitation_resistance": "Poor (high speed not suitable)",
        "common_failures": [
            "Hinge pin corrosion or seizing",
            "Blade spring stiffness loss after years",
            "Hub binding from marine growth",
        ],
        "maintenance": [
            "Hinge joint lubrication (synthetic grease, saltwater rated)",
            "Zinc anode on hub (if bronze)",
            "Test fold/unfold mechanism monthly",
        ],
        "brands": ["Flex-O-Fold", "Martyr Folding", "Automat Folding"],
        "cost_usd": 750,
    },
    "feathering_maxprop": {
        "name": "Feathering Propeller MAX-PROP",
        "type": "Feathering (variable pitch mechanically)",
        "material": "Nibral blades, stainless steel shaft",
        "typical_diameter_inches": (12, 14, 16),
        "pitch_range_inches": (10, 12, 14, 16),
        "efficiency_percent": 58,
        "drag_when_sailing_percent_extra_resistance": 0.5,
        "cavitation_resistance": "Good",
        "common_failures": [
            "Mechanical linkage wear (high cycles)",
            "Oil seal leakage from prop shaft",
            "Blade pitch lag under acceleration",
        ],
        "maintenance": [
            "Oil change every 500 engine hours",
            "Mechanical assembly inspection yearly",
            "Pitch control cable tension check",
        ],
        "brands": ["MAX-PROP (Gori)", "Gori Feathering"],
        "cost_usd": 2800,
    },
    "feathering_gori": {
        "name": "Feathering Propeller Gori 4D",
        "type": "Feathering (4-blade option)",
        "material": "Nibral/stainless composite",
        "typical_diameter_inches": (14, 16, 18),
        "pitch_range_inches": (12, 14, 16, 18),
        "efficiency_percent": 64,
        "drag_when_sailing_percent_extra_resistance": 0.3,
        "cavitation_resistance": "Excellent",
        "common_failures": [
            "Hydraulic seal degradation (saltwater)",
            "Control solenoid valve sticking",
        ],
        "maintenance": [
            "Hydraulic fluid check (special marine ISO VG 46)",
            "Solenoid valve cleaning/replacement every 2-3 years",
            "Annual blade angle verification",
        ],
        "brands": ["Gori (Italian premium)"],
        "cost_usd": 3500,
    },
    "variable_pitch_merchant": {
        "name": "Variable Pitch Propeller (Commercial Type)",
        "type": "Fully variable pitch (hydraulic)",
        "material": "Stainless steel hub, bronze blades",
        "typical_diameter_inches": (16, 18, 20, 24),
        "pitch_range_inches": (12, 14, 16, 18, 20),
        "efficiency_percent": 68,
        "drag_when_sailing_percent_extra_resistance": 5,
        "cavitation_resistance": "Excellent",
        "common_failures": [
            "Pitching oil pump wear",
            "Actuator cylinder seal failure",
            "Blade root stress fracture",
        ],
        "maintenance": [
            "Hydraulic system overhaul every 1000 hours",
            "Oil analysis for metal content",
            "Annual shaft bearing inspection",
        ],
        "brands": ["Rolls-Royce (formerly Kamewa)", "ZF"],
        "cost_usd": 8500,
    },
    "bow_thruster_prop": {
        "name": "Bow Thruster Propeller",
        "type": "Tunnel propeller (horizontal axis)",
        "material": "Bronze or Nibral",
        "typical_diameter_inches": (8, 10, 12),
        "pitch_range_inches": (6, 8, 10),
        "efficiency_percent": 45,
        "drag_when_sailing_percent_extra_resistance": 15,
        "cavitation_resistance": "Poor (confined space)",
        "common_failures": [
            "Cavitation erosion from confined tunnel",
            "Bearing wear from lateral thrust loads",
        ],
        "maintenance": [
            "Annual tunnel inspection for marine growth",
            "Bearing grease replenishment",
            "Zinc anode replacement yearly",
        ],
        "brands": ["Kobelt", "Side Power", "Sleipner"],
        "cost_usd": 1200,
    },
}


# ============================================================================
# COOLING SYSTEMS — Kühlsysteme
# ============================================================================

COOLING_SYSTEMS = {
    "raw_water_direct": {
        "name": "Raw Water Cooling (Direct)",
        "type": "Seawater directly through engine",
        "components": {
            "through_hull": "Bronze or plastic through-hull fitting (intake)",
            "raw_water_strainer": "Spin-on or cartridge type, mesh 100-200 micron",
            "impeller_pump": "Rubber or composite impeller",
            "engine_block_passages": "Cast passages subject to corrosion",
            "thermostat": "Wax type, typically 70-82°C setpoint",
            "discharge_hose": "Heavy reinforced rubber EPDM, 1-2 inch diameter",
            "anode": "Sacrificial zinc, aluminum, or magnesium rod",
        },
        "advantages": ["Low cost", "Reliable at low RPM"],
        "disadvantages": [
            "Corrosion in engine block inevitable",
            "Frequent impeller replacement (200 hour mandatory)",
            "Strainer blockage from debris/seaweed",
            "Zinc anode erosion in high-salinity water",
        ],
        "maintenance_schedule_hours": {
            50: ["Visual inspection discharge flow (good stream expected)"],
            100: ["Clean raw water strainer bowl", "Check anode erosion"],
            200: ["Replace impeller (CRITICAL - failure causes overheating)"],
            500: ["Replace raw water strainer element"],
            1000: ["Replace zinc anode", "Flush passages with vinegar/acid if gunked"],
        },
        "failure_modes": [
            "Impeller disintegration -> engine overheat -> seizure (catastrophic)",
            "Strainer blockage -> pressure rise -> thermostat stuck -> overheat",
            "Zinc anode depletion -> rapid engine corrosion, white deposits",
        ],
        "cost_usd": 150,
    },
    "indirect_heat_exchanger": {
        "name": "Indirect Cooling (Heat Exchanger)",
        "type": "Freshwater loop with raw water heat exchanger",
        "components": {
            "freshwater_circuit": ["Closed loop: engine -> radiator -> thermostat"],
            "heat_exchanger": "Brazed plate-frame or tube-in-shell, copper alloy",
            "raw_water_strainer": "Mesh 100 micron, critical for heat exchanger longevity",
            "impeller_pump": "Mounted on raw water inlet",
            "thermostat": "Dual setpoint (engine coolant and raw water sides)",
            "expansion_tank": "Pressurized, holds 5-10% engine coolant volume",
            "raw_water_zinc": "Sacrificial anode in heat exchanger or line",
        },
        "advantages": [
            "Engine block protected from saltwater (much longer life)",
            "More consistent engine temperature",
            "Impeller still critical but slightly less stress",
        ],
        "disadvantages": [
            "More complex system (more failure points)",
            "Heat exchanger core blockage risk",
            "Freshwater coolant requires maintenance (inhibitor refresh)",
        ],
        "maintenance_schedule_hours": {
            100: ["Check coolant level and condition (pink = good, brown = oxidized)"],
            200: ["Inspect raw water strainer (blockage here = heat exchanger damage risk)"],
            500: ["Replace impeller", "Top-up or replace engine coolant"],
            1000: ["Reverse-flush heat exchanger if performance drops"],
            2000: ["Pull and inspect heat exchanger (descale if needed)"],
        },
        "failure_modes": [
            "Heat exchanger core corrosion (raw water side) -> pin-hole leaks -> engine overheat",
            "Freshwater coolant inhibitor depletion -> internal engine rust",
            "Thermostat sticking (especially if air trapped in system)",
        ],
        "cost_usd": 1200,
    },
    "keel_cooler": {
        "name": "Keel Cooler (Passive Immersion)",
        "type": "Copper tubing welded to keel external surface",
        "components": {
            "external_tubing": "Copper tube, 1-2 inch diameter, runs along keel",
            "internal_circulation": "Freshwater engine coolant loops through tube",
            "seawater_exposure": "Direct contact with hull bottom (subject to barnacles/fouling)",
            "thermostat": "Engine coolant side, sets flow rate based on temp",
        },
        "advantages": [
            "Passive (no impeller = no 200-hour wear item)",
            "Large surface area gives predictable cooling",
            "Silent operation",
        ],
        "disadvantages": [
            "Fouling reduces effectiveness (biofouling, barnacles)",
            "Requires good ventilation around keel (poor in motoring hard)",
            "Not suitable for high-power engines without supplementary cooling",
            "Difficult to service (external)",
        ],
        "maintenance_schedule_hours": {
            500: ["Haul-out inspection of external tubing for fouling/corrosion"],
            1000: ["Anti-fouling paint refresh on keel cooler tubes"],
            2000: ["Descale internal tubes if marine growth detected"],
        },
        "failure_modes": [
            "Tube rupture from external impact (grounding, collision)",
            "Biofouling blockage (algae/barnacles prevent heat transfer)",
            "Copper corrosion in certain seawater chemistries",
        ],
        "cost_usd": 800,
    },
    "dry_exhaust_cooling": {
        "name": "Dry Exhaust (Insulated, No Cooling)",
        "type": "Insulated exhaust pipe, minimal cooling",
        "components": {
            "insulation": "Fiberglass or ceramic wrap around exhaust",
            "exhaust_hose": "High-temp rated, 2-4 inch diameter",
            "muffler": "Optional, usually bypassed on marine engines",
        },
        "advantages": [
            "No raw water involvement -> no impeller",
            "Higher fuel efficiency (heat retention)",
            "Corrosion-free operation",
        ],
        "disadvantages": [
            "Very hot in engine compartment (fire risk)",
            "Noise (loud exhaust)",
            "Not common for marine (requires special engine mods)",
        ],
        "maintenance_schedule_hours": {
            500: ["Visual inspection for insulation integrity"],
            2000: ["Re-wrap insulation if degraded"],
        },
        "failure_modes": [
            "Insulation failure -> rapid rusting of exhaust pipe",
            "Heat damage to adjacent hoses/wiring",
        ],
        "cost_usd": 600,
    },
}


# ============================================================================
# EXHAUST SYSTEMS — Abgassysteme
# ============================================================================

EXHAUST_SYSTEMS = {
    "wet_exhaust_waterlock": {
        "name": "Wet Exhaust with Waterlock Muffler",
        "type": "Sea water mixed with exhaust, muffled",
        "components": {
            "exit_elbow": "Bronze or stainless steel 90° elbow from engine",
            "waterlock_muffler": "Submerged chamber with U-bend (holds water seal)",
            "discharge_hose": "Large diameter EPDM rubber (1.5-2.5 inch typical)",
            "siphon_break": "Optional check valve to prevent back-siphoning",
            "exhaust_outlet": "Through transom or hull, above waterline when anchored",
        },
        "advantages": ["Quiet operation", "Cools exhaust naturally"],
        "disadvantages": [
            "Raw water side of system needs strainer maintenance",
            "Waterlock muffler can fill with water (improper pitch of hose)",
            "Salt deposits accumulate in waterlock",
        ],
        "materials": {
            "waterlock_body": "Stainless steel or fiberglass",
            "hose": "Reinforced EPDM (min 2 wire braid), not PVC",
            "clamps": "Stainless steel worm-drive",
        },
        "sizing_rules": {
            "hose_diameter_rule": "Minimum 1.5x engine exhaust port diameter",
            "rise_to_transom": "Must rise 18+ inches above waterline for siphon protection",
            "hose_slope": "Continuous gentle rise, no low spots",
        },
        "maintenance_schedule_hours": {
            200: ["Inspect hose for internal salt deposits"],
            500: ["Drain waterlock muffler, flush with freshwater"],
            1000: ["Replace waterlock internal baffle if eroded"],
            2000: ["Full exhaust hose inspection/replacement if deteriorated"],
        },
        "failure_modes": [
            "Back-siphoning (swamp in engine if hose lower than waterline overnight)",
            "Waterlock overfilling -> salt water back into engine",
            "Hose collapse/blockage -> exhaust backpressure -> poor running",
        ],
        "cost_usd": 800,
    },
    "dry_exhaust_insulated": {
        "name": "Dry Exhaust (Insulated Pipe, No Water Injection)",
        "type": "High-temperature insulated pipe",
        "components": {
            "exhaust_pipe": "Stainless steel or mild steel tube",
            "insulation": "Fiberglass or ceramic fiber wrap",
            "flexible_section": "Corrugated stainless tube near engine",
            "muffler_optional": "Usually deleted for marine (too much backpressure)",
        },
        "advantages": [
            "No raw water involvement -> inherently reliable",
            "High fuel efficiency (heat not dissipated)",
        ],
        "disadvantages": [
            "Extreme heat in engine compartment (fire hazard)",
            "Insulation must remain intact (degradation = rust/corrosion)",
            "Rare in sailboats (not enough cooling for idle)",
        ],
        "materials": {
            "pipe": "Stainless steel 304 or 316",
            "insulation": "Ceramic fiber or marine fiberglass wrap",
            "outlet": "High-temp silicone hose final leg to transom",
        },
        "backpressure_limit": "< 15 cm water column at full RPM",
        "maintenance_schedule_hours": {
            500: ["Visual inspection of insulation integrity"],
            2000: ["Replace degraded insulation wrap"],
        },
        "failure_modes": [
            "Insulation failure -> rapid rust -> perforation",
            "Heat damage to nearby hoses/electrical",
            "Inadequate ventilation in engine compartment",
        ],
        "cost_usd": 1500,
    },
    "semi_dry_exhaust": {
        "name": "Semi-Dry Exhaust (Water Cooled Pipe)",
        "type": "Cooling jacket around exhaust pipe",
        "components": {
            "jacketed_exhaust_pipe": "Double-wall pipe with cooling water path",
            "raw_water_inlet": "From main engine cooling circuit",
            "thermostat_bypass": "Water diverts around jacket at low RPM",
        },
        "advantages": [
            "Cooler temperatures than dry exhaust",
            "Quieter than wet exhaust",
        ],
        "disadvantages": [
            "Complex plumbing (adds cost)",
            "Scale buildup in cooling jacket (hard water)",
            "Still vulnerable to saltwater corrosion on exterior",
        ],
        "maintenance_schedule_hours": {
            500: ["Flush jacket with vinegar to remove scale"],
            1000: ["Inspect for leaks in cooling jacket welds"],
        },
        "cost_usd": 2200,
    },
    "generator_exhaust": {
        "name": "Generator Set Exhaust",
        "type": "Typically wet exhaust on genset",
        "components": {
            "genset_exhaust_manifold": "Cast iron or stainless steel",
            "waterlock_muffler_small": "Compact size for genset (200-400W)",
            "discharge_line": "Separate from main engine exhaust",
        },
        "special_considerations": [
            "Generator exhaust valves run cooler than main engine",
            "Separate exhaust line prevents back-pressure on main engine",
            "Water injection in genset exhaust reduces noise further",
        ],
        "maintenance_schedule_hours": {
            100: ["Inspect genset exhaust temperature (should be tepid)"],
            500: ["Drain and flush genset waterlock"],
        },
        "cost_usd": 450,
    },
}


# ============================================================================
# FUEL MANAGEMENT — Kraftstoffmanagement
# ============================================================================

FUEL_CONSUMPTION_DATABASE = {
    "slow_cruising_hull_speed": {
        "hull_type": "Displacement sailboat cruising speed (1.3x sqrt(LWL) knots)",
        "consumption_rule": "0.150 to 0.200 l/h per hp (diesels)",
        "example_40ft_sailboat": {
            "hull_speed_knots": 6.8,
            "engine_hp": 40,
            "fuel_consumption_l_per_h": 6,
            "range_hours_at_60L_tank": 10,
            "range_nm": 68,
        },
    },
    "medium_cruising_planing": {
        "hull_type": "Light displacement or planing hull",
        "consumption_rule": "0.200 to 0.280 l/h per hp (depends on displacement)",
        "example_30ft_planing": {
            "speed_knots": 12,
            "engine_hp": 200,
            "fuel_consumption_l_per_h": 45,
            "range_hours_at_300L_tank": 6.7,
            "range_nm": 80,
        },
    },
    "full_speed_planing": {
        "hull_type": "Performance planing boat",
        "consumption_rule": "0.300 to 0.400 l/h per hp",
        "example_35ft_planing_full_speed": {
            "speed_knots": 28,
            "engine_hp_twin": 350,
            "fuel_consumption_l_per_h": 140,
            "range_hours_at_400L_tank": 2.9,
            "range_nm": 81,
        },
    },
}

FUEL_QUALITY_MANAGEMENT = {
    "diesel_fuel_characteristics": {
        "cetane_index": "Min 40 for marine diesel (ASTM D2699)",
        "sulfur_content": "Max 0.001% (IMO 2020 regulation)",
        "water_content": "Max 200 ppm (parts per million)",
        "cloud_point": "Dependent on climate (-5 to +15°C typical)",
        "pour_point": "Dependent on climate (-20 to 0°C tropical)",
    },
    "diesel_bug_biofouling": {
        "cause": "Bacterium Pseudomonas aeruginosa + fungus growth at fuel-water interface",
        "environment": "Warm fuel tanks (tropical) with water contamination",
        "signs": [
            "Dark sludge at tank bottom",
            "Clogged fuel filter (rapid)",
            "Engine knocking/poor starting",
            "Visible water in fuel",
        ],
        "prevention": [
            "Keep fuel tank full (minimize air/water)",
            "Add biocide annually in warm waters (e.g., Biobor JF)",
            "Use fuel filter bowl with water separator",
            "Drain water from filter regularly",
        ],
        "treatment": [
            "Drain tank completely",
            "Flush with fresh clean diesel",
            "Add strong biocide (Kathon FP1.5 or equivalent)",
            "Run engine for 2-3 hours to circulate",
            "Monitor fuel filter pressure",
        ],
    },
    "fuel_filter_water_separator": {
        "function": "Removes water and particulates before engine",
        "types": [
            "Simple spin-on cartridge filter (10-30 micron)",
            "Coalescent separator (combines fine water droplets)",
            "Bypass water ejection (electric pump drains collected water)",
        ],
        "maintenance_schedule_hours": {
            100: ["Check water separator bowl for free water", "Drain if present"],
            200: ["Visual inspection of filter element (check for darkening)"],
            500: ["Replace fuel filter element (max 500h or annually)"],
            1000: ["Full fuel system inspection including lines"],
        },
        "recommended_brands": ["Racor", "Separ", "Mann+Hummel"],
    },
    "fuel_tank_monitoring": {
        "capacity_selection_rule": "1.5 to 2.0 x estimated fuel burn for intended cruise distance",
        "gauging_options": [
            "Simple float gauge (unreliable in rough seas)",
            "Capacitive sender (more reliable, requires calibration)",
            "Flow meter (tracks actual consumption real-time)",
        ],
        "tank_material": ["Aluminum (lightest)", "Steel (most durable)", "Polyethylene (corrosion-free)"],
        "baffles": "Internal baffles reduce fuel surge in rough seas",
        "vent_breather": "Prevents pressure buildup (breather loop to deck level)",
    },
}


# ============================================================================
# TRANSMISSION — Getriebe
# ============================================================================

TRANSMISSION_TYPES = {
    "zf_marine_25m": {
        "name": "ZF Marine 25M",
        "manufacturer": "ZF (formerly Hurth)",
        "type": "Mechanical constant-mesh gearbox",
        "power_rating_kw": 55,
        "power_rating_hp": 75,
        "gear_ratio_forward": 2.17,
        "gear_ratio_reverse": 2.17,
        "input_rpm_max": 3200,
        "output_rpm_max": 1475,
        "reduction_ratio": 2.17,
        "oil_type": "Marine ISO VG 46 (Mobil Pyrogard SHC or equivalent)",
        "oil_change_interval_hours": 500,
        "operating_temperature": "80-90°C normal, max 110°C",
        "maintenance_schedule_hours": {
            100: ["Check oil level (dipstick) - critical before long passage"],
            250: ["Inspect oil for metal debris (indicator of wear)"],
            500: ["Oil and filter change (marine gear oil, not automotive)"],
            1000: ["Complete overhaul by specialist (check bearings, seals)"],
        },
        "failure_modes": [
            "Syncro ring wear -> difficult gear engagement",
            "Thrust bearing failure -> shaft play/vibration",
            "Oil seal leakage -> external drip",
        ],
        "common_issues": [
            "Operator abuse (slamming into reverse while moving forward)",
            "Overspeed (exceeding max input RPM) -> bearing stress",
            "Oil contamination from water ingress (seal failure)",
        ],
        "cost_usd": 3500,
        "compatible_engines": ["Volvo Penta D2", "Yanmar 3JH", "Beta 38, 50"],
    },
    "zf_hurth_650": {
        "name": "ZF Hurth 650",
        "manufacturer": "ZF Friedrichshafen",
        "type": "Mechanical constant-mesh gearbox",
        "power_rating_kw": 110,
        "power_rating_hp": 150,
        "gear_ratio_forward": 1.86,
        "gear_ratio_reverse": 1.86,
        "input_rpm_max": 3600,
        "output_rpm_max": 1935,
        "reduction_ratio": 1.86,
        "oil_type": "Marine ISO VG 46",
        "oil_change_interval_hours": 500,
        "operating_temperature": "85-95°C normal",
        "maintenance_schedule_hours": {
            250: ["Oil level check + smell test (burnt smell = trouble)"],
            500: ["Oil and filter change"],
            1000: ["Inspect for oil leaks, check seal condition"],
        },
        "failure_modes": [
            "Bearing race spalling (high-load operation)",
            "Seal degradation in hot engine rooms",
        ],
        "cost_usd": 5200,
    },
    "saildrive_integrated_gearbox": {
        "name": "Saildrive Integrated Transmission",
        "type": "Built-in reduction gearbox (Volvo SD130, Yanmar SD60)",
        "power_handling_kw": 30,
        "typical_reduction_ratio": 2.0,
        "input_rpm": 3600,
        "output_rpm": 1800,
        "oil_type": "Saildrive-specific synthetic (not standard marine oil)",
        "oil_change_interval_hours": 1000,
        "seal_replacement_interval_hours": 2000,
        "operating_temperature": "70-85°C (water-cooled)",
        "maintenance": [
            "Oil level check via dipstick on gearbox",
            "Oil must match OEM spec (wrong oil = seal failure)",
            "Seal replacement is major service (requires haul-out)",
        ],
        "failure_modes": [
            "Oil seal leakage (normal aging, 2000h replacement)",
            "Coupling wear (propeller cone slips on shaft)",
        ],
        "cost_included_in_saildrive": 2800,
    },
    "hydraulic_transmission": {
        "name": "Hydraulic Transmission (Variable Displacement)",
        "type": "Pump + motor system (rare in small yachts)",
        "power_rating_kw": 150,
        "characteristics": [
            "Infinite variable speed (no discrete gears)",
            "Smooth acceleration/deceleration",
            "Reverse integral to design",
        ],
        "disadvantages": [
            "Complex maintenance (hydraulic seals, filters)",
            "Heat generation (requires cooling loop)",
            "High cost relative to mechanical transmission",
        ],
        "oil_type": "ISO VG 46 hydraulic fluid (fire-resistant types available)",
        "oil_change_interval_hours": 250,
        "filter_change_interval_hours": 100,
        "cost_usd": 18000,
    },
    "pod_drive_transmission": {
        "name": "Pod Drive Integrated (Volvo IPS, ZF POD)",
        "type": "High-performance submerged drive with integral transmission",
        "power_rating_kw": 280,
        "input_rpm_max": 3600,
        "output_configuration": "Dual counter-rotating props (IPS system)",
        "efficiency_percent": 95,
        "maintenance_schedule_hours": {
            500: ["Bearing grease levels (sealed unit, minimal service)"],
            1000: ["Electronic trim system test (reversibility)"],
            2000: ["Full seal inspection by authorized service"],
        },
        "failure_modes": [
            "Seal failure (rare, fully sealed unit)",
            "Propeller cavitation damage (rare in IPS design)",
        ],
        "cost_usd": 45000,
    },
}


# ============================================================================
# MAINTENANCE SCHEDULE — Wartungsplan
# ============================================================================

ENGINE_MAINTENANCE_SCHEDULE = {
    "100_hours": [
        "Check fuel filter water separator bowl (drain if water present)",
        "Inspect raw water strainer basket (clean if debris visible)",
        "Check cooling system temperature gauge (should reach 75-85°C)",
        "Visual inspection of hoses (look for weeping, salt deposits)",
        "Check engine oil level (cold engine, on level surface)",
        "Inspect battery terminals for corrosion",
        "Listen for unusual noises (knocking, grinding indicate problems)",
        "Check transmission/gearbox oil level",
    ],
    "200_hours": [
        "Replace engine oil and filter",
        "Drain and flush water separator fuel filter",
        "Inspect and possibly replace impeller if engine is > 5 years old",
        "Check zinc anode (should show active corrosion, replace if < 50% left)",
        "Inspect propeller for cavitation damage, weed/fishing line wrap",
        "Check propeller shaft alignment (vibration at RPM indicates misalignment)",
        "Flush raw water cooling system with vinegar to remove scale",
    ],
    "500_hours": [
        "Replace raw water strainer cartridge",
        "Complete cooling system inspection (heat exchanger internal flush)",
        "Check gearbox oil color/condition (dark brown = wear, replace)",
        "Transmission oil change (if not recently done)",
        "Impeller replacement (MANDATORY - failure catastrophic)",
        "Propeller removal and inspection (check for micro-fractures)",
        "Battery load test (should hold 12.5V+ under 100A draw for 10 sec)",
        "Engine exhaust system inspection (listen for new leaks/weakness)",
        "Full engine external inspection (bolts, mounts, seals)",
    ],
    "1000_hours": [
        "Transmission seal and bearing inspection (may require specialist)",
        "Saildrive coupling mechanical check (test with light load reverse)",
        "Replace engine coolant if indirect cooling system (inhibitor depletes)",
        "Shaft and cutless bearing wear check (haul-out visual inspection)",
        "Propeller shaft coupling inspection for corrosion/misalignment",
        "Heat exchanger external inspection and cleaning (remove growth)",
        "Fuel tank inspection for water/sludge (drain tank sediment)",
        "All hoses: age check (rubber becomes brittle > 5-7 years old)",
    ],
    "2000_hours": [
        "Major engine overhaul review (consider piston/ring inspection)",
        "Transmission internal overhaul or rebuild (specialist service)",
        "Saildrive seal replacement (normal scheduled maintenance)",
        "Hull anode inspection and replacement (significant corrosion expected)",
        "Exhaust system replacement (hose and components typically worn)",
        "Full shaft alignment verification with laser alignment tool",
        "Replace all through-hull seacocks with grease (prevent sticking)",
        "Engine mount inspection (rubber degrades, replace if cracked)",
    ],
}


# ============================================================================
# ASSESSMENT FUNCTION
# ============================================================================

def assess_propulsion_system(
    engine_type: str,
    hours_on_engine: int,
    cooling_system: str,
    hull_type: str,
    fuel_tank_capacity_liters: int,
    last_maintenance_date: str,
    observed_symptoms: List[str]
) -> Dict[str, Any]:
    """
    Comprehensive propulsion system assessment for AYDI yacht design.

    Args:
        engine_type: Engine model identifier
        hours_on_engine: Total running hours accumulated
        cooling_system: Type of cooling (raw_water, indirect, keel_cooler, etc.)
        hull_type: sailboat, motorsailer, planing, trawler, etc.
        fuel_tank_capacity_liters: Available fuel range capacity
        last_maintenance_date: ISO format date (YYYY-MM-DD)
        observed_symptoms: List of current operational issues

    Returns:
        Dictionary containing:
        - assessment_score (0-100): System health rating
        - critical_findings: List of immediate action items
        - recommendations: Prioritized list of maintenance/upgrades
        - fuel_range_estimate_nm: Distance capability on full tank
        - next_scheduled_maintenance: Hours/date of next service
        - risk_level: "green", "yellow", "red"
    """

    assessment_score = 100
    critical_findings = []
    recommendations = []
    risk_level = "green"

    # Check engine age/hours
    if hours_on_engine > 5000:
        assessment_score -= 15
        recommendations.append("Engine approaching mid-life: plan for overhaul at 8000-10000 hours")

    if hours_on_engine % 200 != 0 and hours_on_engine > 100:
        next_maintenance_hours = ((hours_on_engine // 200) + 1) * 200
        recommendations.append(f"Impeller replacement due: next service at {next_maintenance_hours}h")

    # Cooling system checks
    if cooling_system == "raw_water_direct" and hours_on_engine > 200:
        if hours_on_engine % 200 > 50:
            critical_findings.append("Raw water cooling: impeller replacement OVERDUE (every 200h mandatory)")
            risk_level = "red"
            assessment_score -= 30

    # Symptom evaluation
    symptom_severity = {
        "overheating": {"score_penalty": 20, "finding": "Cooling system failure imminent"},
        "loss_of_power": {"score_penalty": 25, "finding": "Engine degradation or fuel contamination"},
        "excessive_vibration": {"score_penalty": 15, "finding": "Propeller damage or shaft misalignment"},
        "fuel_smell": {"score_penalty": 10, "finding": "Potential fuel leak in bilge"},
        "white_deposits": {"score_penalty": 18, "finding": "Saltwater corrosion: zinc anode depleted"},
    }

    for symptom in observed_symptoms:
        if symptom in symptom_severity:
            assessment_score -= symptom_severity[symptom]["score_penalty"]
            critical_findings.append(symptom_severity[symptom]["finding"])
            if symptom_severity[symptom]["score_penalty"] >= 20:
                risk_level = "red"
            elif risk_level != "red":
                risk_level = "yellow"

    # Fuel range estimation (simplified)
    # Assumes typical displacement sailboat consumption
    fuel_consumption_l_per_h = 6.0  # Nominal cruising consumption
    endurance_hours = fuel_tank_capacity_liters / fuel_consumption_l_per_h
    hull_speed_knots = 6.8  # Typical for 40ft sailboat
    fuel_range_estimate_nm = int(endurance_hours * hull_speed_knots)

    # Determine next maintenance milestone
    maintenance_milestones = [100, 200, 500, 1000, 2000]
    next_milestone = next((m for m in maintenance_milestones if m > hours_on_engine), 2000)

    # Assemble assessment
    return {
        "assessment_score": max(0, min(100, assessment_score)),
        "risk_level": risk_level,
        "critical_findings": critical_findings,
        "recommendations": recommendations,
        "fuel_range_estimate_nm": fuel_range_estimate_nm,
        "endurance_hours": round(endurance_hours, 1),
        "next_scheduled_maintenance_hours": next_milestone,
        "hours_until_next_service": next_milestone - hours_on_engine,
        "assessment_timestamp": "2026-03-21T00:00:00Z",
    }


# ============================================================================
# PROPULSION SELECTION MATRIX
# ============================================================================

PROPULSION_SELECTION_MATRIX = {
    "sailboat_cruiser_30_40ft": {
        "recommended_engines": [
            "Yanmar 3JH40 saildrive (simplicity, reliability)",
            "Volvo Penta D2-40 saildrive (features, cost)",
        ],
        "cooling_system": "Raw water indirect heat exchanger (good balance)",
        "propeller": "3-blade Nibral fixed pitch, feathering optional",
        "fuel_tank": "50-80 liters (200 nm range at 6 knots)",
        "transmission": "Saildrive integrated 2.0-2.1 reduction",
    },
    "motorsailer_45_55ft": {
        "recommended_engines": [
            "Beta 50 turbo (good fuel economy)",
            "Volvo Penta D3 55-75hp saildrive",
        ],
        "cooling_system": "Indirect with optional keel cooler",
        "propeller": "Feathering MAX-PROP or Gori 4-blade",
        "fuel_tank": "150-250 liters (400+ nm range)",
        "transmission": "Separate ZF 25M gearbox or saildrive integrated",
    },
    "trawler_40_60ft": {
        "recommended_engines": [
            "Cummins B series turbocharged (heavy duty)",
            "Yanmar 6LY turbocharged",
        ],
        "cooling_system": "Indirect with large heat exchanger + keel cooler",
        "propeller": "3-blade Nibral or 4-blade variable pitch",
        "fuel_tank": "300-600 liters (1000+ nm range)",
        "transmission": "ZF 650 or marine reduction gearbox",
    },
    "performance_planing_boat_25_40ft": {
        "recommended_engines": [
            "Twin Mercury/Yamaha 250-350hp outboards",
            "Twin Volvo Penta V8 inboards (IPS pod drive)",
        ],
        "cooling_system": "Integral outboard cooling (raw water)",
        "propeller": "3-blade stainless, high-speed design",
        "fuel_tank": "200-400 liters (max range 150 nm at full speed)",
        "transmission": "Outboard integral or Pod drive automatic",
    },
}


if __name__ == "__main__":
    # Example usage of assessment function
    assessment = assess_propulsion_system(
        engine_type="Yanmar 3JH40",
        hours_on_engine=450,
        cooling_system="raw_water_direct",
        hull_type="sailboat",
        fuel_tank_capacity_liters=60,
        last_maintenance_date="2026-01-15",
        observed_symptoms=["white_deposits", "overheating"]
    )

    print("AYDI Propulsion System Assessment")
    print("=" * 60)
    print(f"Risk Level: {assessment['risk_level'].upper()}")
    print(f"System Health Score: {assessment['assessment_score']}/100")
    print(f"Fuel Range: {assessment['fuel_range_estimate_nm']} nm")
    print(f"\nCritical Findings:")
    for finding in assessment['critical_findings']:
        print(f"  - {finding}")
    print(f"\nRecommendations:")
    for rec in assessment['recommendations']:
        print(f"  - {rec}")
