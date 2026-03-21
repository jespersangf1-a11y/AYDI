"""
AYDI Yacht Elektrik und Elektronik Knowledge Base
Electrical and Electronics Systems for yacht design analysis
Author: Master Marine Electrician KnowledgeBase
Version: 1.0

Umfassendes Wissen über marine Elektrik, Verkabelung, Energieerzeugung,
Speicherung und Verteilung auf Yachten. Expertenwissen auf Handwerksmästerniveau
mit Standards (ISO 10133, ABYC E-11), Fehlermodi und Diagnose.
"""

from typing import Dict, List, Any, Tuple


# ============================================================================
# CABLE_TYPES — Kabeltypen Marine
# ============================================================================
CABLE_TYPES: Dict[str, Dict[str, Any]] = {
    "UMS_Tinned_Copper_Marine": {
        "name": "Tinned Copper Marine Cable (UMS)",
        "cross_section_mm2": [0.5, 1.0, 1.5, 2.5, 4.0, 6.0, 10.0, 16.0, 25.0, 35.0, 50.0, 70.0],
        "insulation_type": "PVC (Polyvinyl Chloride) - halogen-free ISO 7072",
        "voltage_rating_vdc": 50,
        "voltage_rating_vac": 250,
        "temperature_rating_celsius": (-20, 60),
        "standard": "ISO 10133, ABYC E-11, IEC 60227",
        "color_code": "Red (positive), Black (negative), Yellow (AC), Green (ground)",
        "bending_radius_mm": 10,  # 10x conductor diameter
        "typical_use": "General 12/24/48V DC wiring, battery interconnects, house loads",
        "brands": ["Ancor", "Belden", "Pacer Group", "Marine Products Ltd"],
        "current_capacity_12v_amps": {
            "1.0": 15, "1.5": 20, "2.5": 30, "4.0": 40, "6.0": 55,
            "10.0": 85, "16.0": 120, "25.0": 170, "35.0": 230, "50.0": 310
        },
        "cost_per_meter_eur": 0.35,
        "notes": "Tinned copper resists corrosion in marine saltwater environment better than bare copper"
    },

    "Battery_Cable_Heavy_Gauge": {
        "name": "Heavy Gauge Battery Cable (Tinned, 60% Copper)",
        "cross_section_mm2": [4.0, 6.0, 10.0, 16.0, 25.0, 35.0, 50.0, 70.0, 95.0, 120.0, 150.0],
        "insulation_type": "Flexible PVC, 3mm thick",
        "voltage_rating_vdc": 50,
        "temperature_rating_celsius": (-30, 80),
        "standard": "ABYC E-11, IEC 60227",
        "color_code": "Red (positive), Black (negative)",
        "bending_radius_mm": 60,
        "typical_use": "Main battery interconnects, alternator output, large load distribution",
        "brands": ["East Penn Deka", "Ancor", "Belden", "Maretron"],
        "current_capacity_12v_amps": {
            "10.0": 95, "16.0": 135, "25.0": 190, "35.0": 260,
            "50.0": 355, "70.0": 480, "95.0": 630, "120.0": 760
        },
        "stranding": "19x3.45 mm (stranded for flexibility)",
        "resistance_per_meter": 0.0018,  # ohms/meter at 20°C
        "cost_per_meter_eur": 0.85,
        "notes": "Lower resistance than standard cable; critical for high-current paths"
    },

    "Coaxial_RG_213": {
        "name": "Coaxial Cable RG-213 (VHF/HF Radio)",
        "impedance_ohm": 50,
        "velocity_factor": 0.66,
        "outer_diameter_mm": 10.8,
        "inner_conductor_mm": 2.26,
        "insulation_type": "Polyethylene core + tinned copper shield",
        "voltage_rating_vrms": 3000,
        "temperature_rating_celsius": (-55, 80),
        "standard": "MIL-C-17, IEC 61917",
        "bending_radius_mm": 100,
        "typical_use": "VHF radio antenna feeder, HF SSB antenna, GPS antenna",
        "brands": ["Radiall", "Times Microwave", "Belden"],
        "attenuation_db_per_100m_at_1ghz": 3.0,
        "cost_per_meter_eur": 0.55,
        "notes": "Shielding prevents EMI interference; requires proper grounding at radio end"
    },

    "Data_Cable_Cat5e_Shielded": {
        "name": "Shielded Category 5e Data Cable (NMEA 2000, Networking)",
        "conductor_count": 4,  # twisted pairs
        "impedance_ohm": 100,
        "outer_diameter_mm": 7.5,
        "insulation_type": "Polyethylene + aluminum foil + drain wire shield",
        "voltage_rating_v": 100,
        "temperature_rating_celsius": (-20, 70),
        "standard": "IEC 61076, ISO 10133",
        "bending_radius_mm": 40,
        "max_segment_length_m": 100,
        "typical_use": "NMEA 2000 network backbone, Ethernet LAN, instrument wiring",
        "brands": ["Belden", "Anixter", "Reichle & De-Massari"],
        "bandwidth_mhz": 100,
        "cost_per_meter_eur": 0.25,
        "notes": "Twisted pair reduces crosstalk; foil shield provides EMI rejection"
    },

    "Shore_Power_Cable_3x_2_5": {
        "name": "Shore Power Cable 230V AC (3x2.5 mm²)",
        "cross_section_mm2": 2.5,
        "conductor_count": 3,  # L, N, PE
        "insulation_type": "Rubber/PVC halogen-free",
        "voltage_rating_vac": 400,
        "temperature_rating_celsius": (-20, 60),
        "standard": "IEC 60227 RV-K, ABYC E-11",
        "color_code": "Brown (L), Blue (N), Green/Yellow (PE)",
        "bending_radius_mm": 80,
        "typical_use": "Shore connection 230V AC single-phase, 16A max",
        "brands": ["Lappkabel", "Sensormatic", "Nexans"],
        "current_capacity_amps": 16,
        "cost_per_meter_eur": 1.20,
        "notes": "Must include RCD (residual current device) protection; typically 30mA"
    },

    "Twin_Core_Shielded_Instrument": {
        "name": "Twin Core Shielded Twisted Pair (Analog Sensors)",
        "conductor_count": 2,
        "cross_section_mm2": 0.5,
        "shield_type": "Tinned copper braid 80% coverage",
        "insulation_type": "PVC",
        "voltage_rating_v": 50,
        "temperature_rating_celsius": (-20, 80),
        "standard": "ISO 10133, ABYC E-11",
        "bending_radius_mm": 30,
        "typical_use": "Temperature sensors, pressure transducers, analog sensor wiring",
        "brands": ["Ancor", "Belden", "Pacer"],
        "capacitance_pf_per_meter": 120,
        "cost_per_meter_eur": 0.18,
        "notes": "Shield must be grounded at one end only to prevent ground loops"
    },

    "Flat_Ribbon_Automotive_Style": {
        "name": "Flat Ribbon Cable (Automotive Multi-conductor)",
        "conductor_count": [2, 4, 6, 8, 10, 12, 16],
        "cross_section_per_conductor_mm2": 1.0,
        "insulation_type": "Polyethylene",
        "voltage_rating_v": 50,
        "temperature_rating_celsius": (-20, 80),
        "standard": "SAE J1211",
        "bending_radius_mm": 40,
        "typical_use": "Wiring harnesses, backplane connections, distribution panels",
        "brands": ["3M", "Delphi", "TE Connectivity"],
        "cost_per_meter_eur": 0.12,
        "notes": "Compact; good for bundled installations but harder to repair individually"
    },

    "Fiber_Optic_NMEA_2000_Isolated": {
        "name": "Fiber Optic Isolated Network Cable",
        "core_diameter_micron": 50,
        "cladding_diameter_micron": 125,
        "jacket_diameter_mm": 4.0,
        "insulation_type": "Acrylic/Polyimide",
        "voltage_rating": "N/A - optical",
        "temperature_rating_celsius": (-40, 85),
        "standard": "IEC 60793, ABYC E-11",
        "bending_radius_mm": 50,
        "typical_use": "EMI-sensitive installations, galvanic isolation between system segments",
        "brands": ["Corning", "Prysmian", "Nexans"],
        "attenuation_db_per_km_at_850nm": 3.5,
        "cost_per_meter_eur": 2.50,
        "notes": "Eliminates ground loops completely; requires opto-isolator transceivers"
    },

    "Armored_Tray_Cable_Marine_Grade": {
        "name": "Armored Tray Cable (Flex Armor, 3-conductor)",
        "conductor_count": 3,
        "cross_section_mm2": [2.5, 4.0, 6.0, 10.0],
        "armor_type": "Flexible steel braid, tinned",
        "insulation_type": "PVC + LSZH (Low Smoke Zero Halogen)",
        "voltage_rating_vdc": 50,
        "temperature_rating_celsius": (-20, 70),
        "standard": "ISO 10133, ABYC E-11",
        "bending_radius_mm": 120,
        "typical_use": "Through-deck penetrations, high-abuse areas, mechanical protection",
        "brands": ["Ancor", "West Marine", "Belden"],
        "crush_resistance_lbs": 1200,
        "cost_per_meter_eur": 2.10,
        "notes": "Armor adds weight and stiffness; excellent for harsh environments"
    },

    "Subsea_ROV_Cable_Polyurethane": {
        "name": "Subsea Cable (Polyurethane, Antifouling)",
        "conductor_count": 2,
        "cross_section_mm2": 1.5,
        "insulation_type": "Polyurethane, UV/ozone resistant",
        "voltage_rating_vdc": 100,
        "temperature_rating_celsius": (-40, 90),
        "standard": "ISO 10133, DNV GL",
        "bending_radius_mm": 50,
        "typical_use": "Through-hull penetrations, underwater sensors, thruster controls",
        "brands": ["SubConn", "Teledyne", "SAM Electronics"],
        "saltwater_immersion_rated": True,
        "antifouling_coating": "Polyurethane elastomer",
        "cost_per_meter_eur": 4.50,
        "notes": "Rated for full saltwater immersion; excellent flex life and abrasion resistance"
    },
}


# ============================================================================
# BATTERY_SYSTEMS — Batteriesysteme
# ============================================================================
BATTERY_SYSTEMS: Dict[str, Dict[str, Any]] = {
    "AGM_Lead_Acid": {
        "chemistry": "Lead-acid with Absorbed Glass Mat separator",
        "name_common": "AGM (Absorbed Glass Mat) Battery",
        "voltage_nominal_v": 12,
        "capacity_ranges_ah": [40, 70, 100, 140, 200, 300],
        "cycle_life": 800,
        "depth_of_discharge_percent": 80,
        "recharge_voltage_v": 14.4,
        "max_charge_current_a": "0.2C to 0.3C (per capacity)",
        "float_voltage_v": 13.2,
        "temperature_range_celsius": (-20, 50),
        "self_discharge_percent_per_month": 3,
        "weight_per_kwh_kg": 25,
        "bms_required": False,
        "ventilation_required": False,
        "internal_resistance_mohm": 2.5,
        "cost_per_kwh_eur": 80,
        "pros": [
            "Robust, proven technology",
            "Works in all temperatures",
            "Low cost",
            "Tolerates overcharging"
        ],
        "cons": [
            "Acid can spill",
            "Sulfation if discharged fully",
            "Lower energy density",
            "Gassing during charge (ventilation needed)"
        ],
        "typical_brands": ["Victron Energy (Lifepo4), Rolls-Royce, Trojan, East Penn Deka"],
        "maintenance": "Water topping, terminal corrosion cleaning",
        "failure_modes": ["Sulfation from deep discharge", "Corrosion", "Grid degradation"]
    },

    "Gel_Lead_Acid": {
        "chemistry": "Lead-acid with Silica Gel electrolyte",
        "name_common": "Gel Battery",
        "voltage_nominal_v": 12,
        "capacity_ranges_ah": [50, 80, 100, 150, 200, 250],
        "cycle_life": 1200,
        "depth_of_discharge_percent": 70,
        "recharge_voltage_v": 14.1,
        "max_charge_current_a": "0.15C",
        "float_voltage_v": 13.0,
        "temperature_range_celsius": (-20, 50),
        "self_discharge_percent_per_month": 2,
        "weight_per_kwh_kg": 28,
        "bms_required": False,
        "ventilation_required": False,
        "sealed_acid_safe": True,
        "cost_per_kwh_eur": 100,
        "pros": [
            "Sealed (no spill risk)",
            "Good cycle life",
            "No maintenance",
            "Tolerates tilt/motion"
        ],
        "cons": [
            "Charging must be precise",
            "Slower charge acceptance",
            "Higher cost than AGM",
            "Lower energy density"
        ],
        "typical_brands": ["Victron, Sonnenschein, Exell, Hoppecke"],
        "charge_controller_requirement": "Dedicated gel-mode charger recommended",
        "failure_modes": ["Gassing if overcharged", "Slow recharge acceptance"]
    },

    "Lithium_LiFePO4": {
        "chemistry": "Lithium Iron Phosphate (Lifepo4)",
        "name_common": "LiFePO4 (LFP) Battery",
        "voltage_nominal_v": 12.8,  # or 25.6V for 2S, 38.4V for 3S, 51.2V for 4S
        "capacity_ranges_ah": [50, 100, 150, 200, 300, 400],
        "cycle_life": 5000,
        "depth_of_discharge_percent": 95,
        "recharge_voltage_v": 14.6,
        "max_charge_current_a": "1.0C",
        "float_voltage_v": 13.4,
        "temperature_range_celsius": (-20, 60),
        "self_discharge_percent_per_month": 0.2,
        "weight_per_kwh_kg": 8,
        "bms_required": True,
        "bms_type": "Integrated BMS with cell balancing, low-temp cutoff, overload protection",
        "ventilation_required": False,
        "internal_resistance_mohm": 0.15,
        "energy_density_wh_per_kg": 125,
        "cost_per_kwh_eur": 220,
        "pros": [
            "Longest lifespan (5000+ cycles)",
            "Highest energy density",
            "Fast charge/discharge",
            "No maintenance",
            "Thermal stable, safe chemistry"
        ],
        "cons": [
            "High initial cost",
            "Requires BMS",
            "Temperature sensitive at low temps",
            "Needs matching charger"
        ],
        "typical_brands": ["Victron LiFePO4 Smart", "Battle Born", "RELiON", "Relion"],
        "low_temp_charge_cutoff_celsius": 0,
        "bms_features": "Cell balancing, heater control, CAN/Modbus interface",
        "compatible_alternator_regulators": ["Balmar Max Charge", "Blue Sea Mega Charge"],
        "failure_modes": ["BMS failure stops all current", "Cell imbalance over time"]
    },

    "Lithium_NMC_High_Energy": {
        "chemistry": "Lithium Nickel Manganese Cobalt Oxide (NMC)",
        "name_common": "NMC Lithium Battery",
        "voltage_nominal_v": 11.1,  # 3.7V per cell x 3
        "capacity_ranges_ah": [100, 200, 300, 400],
        "cycle_life": 3000,
        "depth_of_discharge_percent": 90,
        "recharge_voltage_v": 12.6,
        "max_charge_current_a": "1.0C",
        "temperature_range_celsius": (-10, 55),
        "self_discharge_percent_per_month": 0.5,
        "weight_per_kwh_kg": 6,
        "bms_required": True,
        "energy_density_wh_per_kg": 167,
        "cost_per_kwh_eur": 240,
        "pros": [
            "Highest energy density",
            "Lighter weight",
            "Good power delivery"
        ],
        "cons": [
            "Lower thermal stability than LFP",
            "Shorter cycle life",
            "More expensive than LFP",
            "Cold weather issues"
        ],
        "typical_brands": ["Relion, Epoch Batteries"],
        "thermal_runaway_risk": "Moderate - requires BMS temperature monitoring",
        "failure_modes": ["Thermal runaway if damaged", "Faster capacity fade"]
    },

    "Supercapacitor_Ultracap": {
        "chemistry": "Double-layer capacitor (electric field, no chemical reaction)",
        "name_common": "Supercapacitor / Ultracap",
        "voltage_nominal_v": 2.7,
        "cell_capacity_farad": [100, 500, 1000, 3000],
        "energy_density_wh_per_kg": 5,
        "power_density_w_per_kg": 5000,
        "cycle_life": 500000,
        "temperature_range_celsius": (-40, 65),
        "self_discharge_percent_per_month": 20,
        "charge_time_seconds": 1,
        "discharge_time_seconds": 1,
        "bms_required": False,
        "internal_resistance_mohm": 0.1,
        "cost_per_kwh_eur": 5000,
        "pros": [
            "Unlimited charge cycles",
            "Ultra-fast charge/discharge",
            "No thermal runaway",
            "Excellent for peak power",
            "Works at any temperature"
        ],
        "cons": [
            "Extremely low energy capacity (Wh)",
            "Prohibitive cost per kWh",
            "High self-discharge",
            "Voltage varies with state of charge"
        ],
        "typical_brands": ["Maxwell, Ioxus, Skeleton"],
        "typical_use": "Peak power shaving, engine starting assist, momentary power backup",
        "modules_in_series": "Required to reach 12/24/48V (cell voltage 2.7V only)"
    },

    "Wet_Cell_Flooded_Lead_Acid": {
        "chemistry": "Lead-acid with liquid sulfuric acid electrolyte",
        "name_common": "Wet Cell / Flooded Battery",
        "voltage_nominal_v": 12,
        "capacity_ranges_ah": [50, 75, 100, 150, 200, 300],
        "cycle_life": 500,
        "depth_of_discharge_percent": 50,
        "recharge_voltage_v": 14.4,
        "max_charge_current_a": "0.1C",
        "float_voltage_v": 13.2,
        "temperature_range_celsius": (-20, 50),
        "self_discharge_percent_per_month": 5,
        "weight_per_kwh_kg": 30,
        "bms_required": False,
        "ventilation_required": True,  # Hydrogen/oxygen venting
        "gassing_during_charge": True,
        "cost_per_kwh_eur": 60,
        "pros": [
            "Cheapest option",
            "Robust, tolerant of abuse",
            "Replaceable electrolyte if damaged"
        ],
        "cons": [
            "Heavy and bulky",
            "Requires ventilation (safety hazard)",
            "Acid corrosion risk",
            "Water loss during charging",
            "Explosive hydrogen gas"
        ],
        "typical_brands": ["Interstate, Exell, Deka"],
        "typical_use": "Engine starting battery (not recommended for house bank)",
        "ventilation_requirement": "Direct vent to outside; 1 in² per battery recommended",
        "failure_modes": ["Sulfation, electrolyte loss, acid corrosion"]
    },

    "Lead_Carbon_Hybrid": {
        "chemistry": "Lead-acid hybrid with carbon additive to negative plate",
        "name_common": "Lead-Carbon Hybrid",
        "voltage_nominal_v": 12,
        "capacity_ranges_ah": [100, 150, 200],
        "cycle_life": 2500,
        "depth_of_discharge_percent": 60,
        "recharge_voltage_v": 14.4,
        "max_charge_current_a": "0.2C",
        "temperature_range_celsius": (-20, 50),
        "cost_per_kwh_eur": 110,
        "pros": [
            "Better cycle life than wet cell",
            "Better sulfation resistance",
            "Lower cost than lithium",
            "Mature technology"
        ],
        "cons": [
            "Not sealed (hybrid advantage less than AGM)",
            "Gassing still possible",
            "Heavier than LFP"
        ],
        "typical_brands": ["Victron, Enersys Odyssey"],
        "failure_modes": ["Carbon shedding over time", "Sulfation possible"]
    },

    "Starter_vs_House_Bank": {
        "starter_battery": {
            "purpose": "High current pulse for engine cranking",
            "chemistry_typical": "Lead-acid (wet or AGM)",
            "cca_rating": 500,  # Cold Cranking Amps
            "capacity_ah_typical": 100,
            "discharge_profile": "High current (500A+), short duration (10 sec)",
            "depth_of_discharge_typical": 0,  # Recharged by alternator immediately
            "isolation": "Via battery switch or VSR (Voltage Sensitive Relay)"
        },
        "house_bank": {
            "purpose": "Deep cycling for DC loads, inverter, etc.",
            "chemistry_typical": "AGM, Gel, or LiFePO4",
            "capacity_ah_typical": 200,
            "discharge_profile": "Moderate current (20-50A), long duration (hours/days)",
            "depth_of_discharge_safe": 80,
            "isolation": "From starter via VSR or manual switch"
        },
        "isolation_method": "VSR senses alternator output; disconnects when below 12.8V",
        "warning": "Mixing starter and house bank without isolation causes premature failure"
    }
}


# ============================================================================
# CHARGING_SYSTEMS — Ladesysteme
# ============================================================================
CHARGING_SYSTEMS: Dict[str, Dict[str, Any]] = {
    "Diesel_Alternator_Standard": {
        "name": "Engine Alternator (Diesel 12V / 24V)",
        "alternator_type": "3-phase brushless automotive-marine hybrid",
        "output_range_amps": [60, 80, 100, 120, 150],
        "voltage_output_v": 14.4,
        "efficiency_percent": 85,
        "typical_engine_rpm": 1500,
        "output_amps_at_1500_rpm": {
            "60A_unit": 55,
            "100A_unit": 95,
            "150A_unit": 140
        },
        "startup_current_inrush_a": 200,
        "regulation_type": "1-wire or 3-wire external regulator",
        "brands": ["Balmar, Leece-Neville, Hitachi, Bosch"],
        "pulley_ratio": 1.8,  # engine rpm / alternator rpm multiplier
        "installation_note": "Engine rpm 1200+ for alternator output; idles poorly",
        "typical_sizing": "50-100A for cruising sailboats, 100-150A for powerboats",
        "cost_eur": 400,
        "failure_modes": ["Diode failure (warm weather)", "Regulator failure", "Belt slip"]
    },

    "Alternator_High_Output_Regulator": {
        "name": "Smart Regulator + Standard Alternator (Balmar Max Charge, etc.)",
        "alternator": "3-phase (60-150A stock unit)",
        "regulator_type": "External PWM 3-stage smart regulator",
        "voltage_setpoint_bulk_v": 14.4,
        "voltage_setpoint_absorption_v": 14.4,
        "voltage_setpoint_float_v": 13.2,
        "temperature_compensated": True,
        "remote_sensing": "Senses battery voltage directly, compensates for wire loss",
        "multi_battery_capable": True,
        "cost_regulator_eur": 350,
        "output_boost_percent": 10,  # over stock alternator
        "typical_system_output_amps": 130,
        "brands": ["Balmar Max Charge, Ample Power, Blue Sea Mega Charge"],
        "advantages": [
            "Improves charging from stock alternator",
            "Three-stage charge algorithm",
            "Remote sensing minimizes voltage drop effect",
            "Can manage multiple battery banks"
        ]
    },

    "Solar_Panel_Monocrystalline": {
        "name": "Monocrystalline Solar Panel (High Efficiency)",
        "panel_type": "Monocrystalline silicon cells",
        "efficiency_percent": 18,
        "power_per_m2_watts": 200,
        "typical_sizes_watts": [50, 100, 150, 200, 250, 300],
        "voltage_voc": 37,  # Open circuit voltage
        "voltage_mpp_v": 30,  # Voltage at max power point
        "current_mpp_a": {
            "100W": 3.3,
            "200W": 6.6,
            "300W": 10.0
        },
        "temperature_coefficient_percent_per_c": -0.4,
        "output_at_25c_sun": "Rated power (100W panel = 100W in full sun)",
        "output_at_50_percent_cloud": "50W (linear with irradiance)",
        "installation": "Rigid mounting on hardtop, bimini, stanchion, or flexible deck panels",
        "brands": ["Victron, Renogy, Rich Solar, Solargrid"],
        "typical_daily_yield_summer_ah": {
            "100W_panel_in_mediterranean": 15,
            "200W_panel_in_mediterranean": 30
        },
        "typical_daily_yield_winter_ah": {
            "100W_panel_in_northern": 5,
            "200W_panel_in_northern": 10
        },
        "cost_per_watt_eur": 0.8,
        "lifespan_years": 25,
        "degradation_percent_per_year": 0.8,
        "advantages": [
            "Highest efficiency",
            "Best in partial shade",
            "Space efficient"
        ],
        "disadvantages": [
            "Highest cost",
            "Heat buildup reduces efficiency",
            "Bird droppings impact critical"
        ]
    },

    "Solar_Panel_Polycrystalline": {
        "name": "Polycrystalline Solar Panel (Cost-Effective)",
        "panel_type": "Polycrystalline silicon cells",
        "efficiency_percent": 15,
        "power_per_m2_watts": 170,
        "typical_sizes_watts": [50, 100, 150, 200, 250],
        "voltage_voc": 36,
        "temperature_coefficient_percent_per_c": -0.45,
        "cost_per_watt_eur": 0.5,
        "advantages": [
            "Lower cost than monocrystalline",
            "Adequate efficiency",
            "Proven reliability"
        ],
        "disadvantages": [
            "Slightly lower efficiency",
            "More temperature sensitive"
        ],
        "typical_brands": ["Victron, Renogy"]
    },

    "Solar_Panel_Flexible_ETFE": {
        "name": "Flexible ETFE Solar Panel (Deck-Mount, Lightweight)",
        "panel_type": "Thin-film monocrystalline on flexible substrate",
        "efficiency_percent": 17,
        "weight_per_watt_grams": 2,
        "thickness_mm": 2.5,
        "typical_sizes_watts": [50, 100, 150, 200],
        "mounting": "Adhesive backing (3M tape) or mechanically fastened",
        "flexibility": "Bends up to 30 degrees radius",
        "cost_per_watt_eur": 1.2,
        "advantages": [
            "Lightweight (1/10 rigid panel)",
            "Flexible mounting options",
            "Less wind loading",
            "Suitable for canvas hardtop"
        ],
        "disadvantages": [
            "Higher cost per watt",
            "Less durable than rigid",
            "Adhesive can fail in marine environment"
        ],
        "typical_brands": ["Solara, Sunpower, Victron"]
    },

    "Wind_Generator_Vertical_Axis": {
        "name": "Vertical-Axis Wind Generator (VAWT)",
        "rotor_type": "Vertical-axis (Savonius, Darrieus, hybrid)",
        "power_range_watts": [200, 400, 600, 1000],
        "cut_in_speed_knots": 5,
        "rated_speed_knots": 12,
        "survival_speed_knots": 30,
        "output_voltage_v": 24,
        "output_at_10_knots_watts": {
            "400W_unit": 150,
            "1000W_unit": 400
        },
        "mounting": "Masthead, pole, or davit",
        "noise_db_at_10m": 65,
        "rotor_diameter_m": [1.0, 1.2, 1.5],
        "brands": ["Air-X, Proven, Southwest Windpower"],
        "advantage_vawt": [
            "Accepts wind from any direction",
            "Lower cut-in speed",
            "Self-starting"
        ],
        "disadvantage_vawt": [
            "Less efficient than HAWT",
            "Vibration and noise",
            "Not suitable in light winds <8 knots"
        ],
        "maintenance": "Bearing check annually, brush inspection",
        "cost_eur": 1500,
        "lifespan_years": 15
    },

    "Wind_Generator_Horizontal_Axis": {
        "name": "Horizontal-Axis Wind Generator (HAWT)",
        "rotor_type": "Horizontal-axis (propeller-style)",
        "power_range_watts": [100, 200, 400, 600],
        "cut_in_speed_knots": 6,
        "rated_speed_knots": 13,
        "survival_speed_knots": 35,
        "output_voltage_v": 12,
        "output_at_12_knots_watts": {
            "200W_unit": 180,
            "400W_unit": 350
        },
        "rotor_diameter_m": [1.2, 1.8, 2.1],
        "furling_speed_knots": 14,
        "brands": ["Air-X, Marlec, Southwest Windpower"],
        "advantage_hawt": [
            "More efficient than VAWT",
            "Lower noise",
            "Better in moderate winds"
        ],
        "disadvantage_hawt": [
            "Must face into wind (requires tail vane)",
            "Requires minimum wind direction alignment",
            "Higher vibration in gusts"
        ],
        "cost_eur": 1200,
        "mounting_restriction": "Minimum 10 feet above deck for safety/efficiency"
    },

    "Hydro_Generator_Trailing_Log": {
        "name": "Trailing Hydro-Generator (Speed Log Driven)",
        "generator_type": "Permanent magnet alternator, paddle-driven",
        "mounting": "Towed behind vessel on 50-100m line",
        "output_voltage_v": 12,
        "output_at_5_knots_watts": 40,
        "output_at_7_knots_watts": 80,
        "output_at_10_knots_watts": 180,
        "propeller_diameter_mm": 75,
        "efficiency_percent": 50,
        "brands": ["Ampair HydroGen, Marlec, Aquair"],
        "advantages": [
            "Works 24/7 underway",
            "No deck installation needed",
            "Quiet operation"
        ],
        "disadvantages": [
            "Drag increases fuel consumption (0.5-1 knot speed loss)",
            "Tether management complexity",
            "Weather-dependent (must be towed in rough seas)"
        ],
        "maintenance": "Annual propeller inspection, bearing grease",
        "cost_eur": 800,
        "typical_daily_output_ah": 20,  # 5-knot passage
        "installation": "Through-transom fairlead, snubber pulley"
    },

    "Shore_Power_Charger_30A": {
        "name": "Shore Power Charger (230V AC to 12V/24V DC)",
        "input_voltage_vac": 230,
        "input_frequency_hz": 50,
        "input_connector": "Type E (CEE 7/4) European standard",
        "max_input_current_a": 16,
        "output_voltage_v": 14.4,
        "output_current_max_a": 30,
        "charge_stages": ["Bulk (14.4V)", "Absorption (14.4V, decreasing current)", "Float (13.2V)"],
        "temperature_compensated": True,
        "output_capacity_rating_ah": "Up to 300Ah (typical 100Ah system)",
        "brands": ["Victron Skylla-TG, Xantrex, Meanwell"],
        "efficiency_percent": 88,
        "rcd_protection": "30mA RCD (Residual Current Device) required by standard",
        "power_consumption_idle_w": 5,
        "cost_eur": 180,
        "installation": "Shore inlet via RCD breaker → charger → battery bank",
        "advantage": [
            "Most efficient DC charging",
            "Silent operation",
            "Multi-stage charge profile"
        ],
        "failure_modes": ["Transformer burnout (polarity reverse)", "Rectifier diode failure"]
    },

    "Fuel_Cell_Hydrogen": {
        "name": "Proton Exchange Membrane (PEM) Fuel Cell",
        "technology": "Hydrogen fuel cell with water emission",
        "output_power_range_watts": [100, 500, 1000, 5000],
        "output_voltage_vdc": 12,  # or stackable modules
        "hydrogen_input_psi": 3,
        "efficiency_percent": 55,
        "stack_lifespan_hours": 10000,
        "startup_time_seconds": 5,
        "noise_db": 65,
        "brands": ["Ballard, GenCell, Intelligent Energy"],
        "cost_per_watt_eur": 5,
        "major_limitation": "No hydrogen infrastructure on most cruising routes",
        "hydrogen_storage": "High-pressure tank (350-700 bar), very heavy/bulky",
        "advantage": [
            "Zero emissions (only water)",
            "High efficiency",
            "Quiet"
        ],
        "disadvantage": [
            "Prohibitive cost",
            "No hydrogen refueling network",
            "Complex safety system",
            "Not practical for current cruising"
        ],
        "status": "Experimental for yachts; not production-ready (as of 2026)"
    },

    "DC_DC_Converter_Buck": {
        "name": "DC-DC Converter (Buck: 48V input → 12V output)",
        "converter_type": "Isolated or non-isolated buck converter",
        "input_range_v": [40, 60],
        "input_voltage_nominal": 48,
        "output_voltage_v": 12,
        "output_current_max_a": 60,
        "output_power_max_watts": 720,
        "efficiency_percent": 92,
        "isolation": "Optional galvanic isolation 3000Vac",
        "thermal_management": "Convection or fan-cooled",
        "brands": ["Victron, Meanwell, RECOM"],
        "cost_eur": 250,
        "typical_use": "Stepping down 48V house bank to 12V for legacy loads/starting",
        "failure_modes": ["Input filter capacitor failure under ripple current"]
    }
}


# ============================================================================
# DISTRIBUTION — Verteilung und Sicherung
# ============================================================================
DISTRIBUTION: Dict[str, Dict[str, Any]] = {
    "Main_Battery_Switch_VSR": {
        "name": "Voltage Sensitive Relay (VSR) / Battery Isolator",
        "function": "Automatically isolates starter battery from house bank based on voltage",
        "isolation_threshold_v": 12.8,
        "reconnect_threshold_v": 12.5,
        "max_current_rating_a": 200,
        "relay_type": "Normally-open solenoid with voltage sensing",
        "brands": ["Blue Sea M-series, Balmar, Littelfuse"],
        "installation": "Positive cable from alternator → VSR → starter battery and house bank",
        "time_delay_seconds": 0.5,  # Prevents chatter during transient voltage dips",
        "cost_eur": 45,
        "advantage": [
            "Automatic isolation/connection",
            "No manual switching needed",
            "Protects house bank from starter drain"
        ],
        "failure_modes": ["Relay contacts corrode (no isolation)", "Sense wire corrosion"]
    },

    "Manual_Battery_Switch_1_2_Both_Off": {
        "name": "Manual Battery Switch (3-position: 1, 2, Both, Off)",
        "switch_type": "Heavy-duty selector switch, 4-position",
        "max_current_continuous_a": 200,
        "inrush_current_a": 500,
        "contact_material": "Silver-plated copper",
        "positions": {
            "1": "Starter battery only (engine start)",
            "2": "House battery only (DC loads)",
            "Both": "Both batteries in parallel (emergency, high current)",
            "Off": "All batteries disconnected"
        },
        "brands": ["Blue Sea Battery Switch, Newmar"],
        "installation": "Between batteries and main positive distribution",
        "cost_eur": 25,
        "usage_caution": "Position 'Both' only in emergency (different SOC can cause damage)"
    },

    "Distribution_Bus_Bar_Multi_Terminal": {
        "name": "Tinned Copper Multi-Terminal Bus Bar (12-terminal)",
        "material": "Tinned copper rod, 10mm diameter",
        "terminal_count": [6, 9, 12, 16, 20],
        "max_current_per_terminal_a": 300,
        "voltage_rating_v": 60,
        "insulation": "Polycarbonate standoffs, UL-rated",
        "terminal_hole_size_mm": 8,
        "terminal_stud_length_mm": 10,
        "brands": ["Bussman, Littelfuse, Ancor"],
        "cost_eur": 15,
        "typical_use": "Primary positive distribution for 12V systems",
        "installation": "Mounted on battery box or bulkhead, main cable → bus bar → circuit protection",
        "connection": "Ring terminals (8mm) under M8 stainless studs",
        "failure_modes": ["Terminal corrosion/arcing if not tinned properly"]
    },

    "Fuse_ANL_High_Capacity": {
        "name": "ANL Fuse (Audible Notification Level - High Current)",
        "fuse_type": "Bolt-down cartridge fuse, silver-plated copper",
        "ratings_amps": [40, 80, 100, 125, 150, 200, 250, 300],
        "voltage_rating_v": 48,
        "melting_current_percent_over_rating": 135,  # Blows at 135% rated (5 sec typical)",
        "breaking_capacity_amps": 5000,  # Max short-circuit current it can safely interrupt",
        "response_time_seconds_at_2x_rating": 5,
        "response_time_seconds_at_5x_rating": 0.1,
        "holder_material": "Composite (thermoplastic)",
        "brands": ["Littelfuse, Bussman, MRBF"],
        "typical_use": "Main battery → distribution (high current main fuse)",
        "cost_per_fuse_eur": 3,
        "installation": "Directly on positive battery terminal, within 18 inches (45cm)",
        "standard": "ABYC E-11, UL 248",
        "failure_modes": ["Corrosion of silver plate reduces contact", "Holder melting in high-temp"]
    },

    "Fuse_MRBF_Marine_Rated": {
        "name": "MRBF Fuse (Marine-Rated Blade Fuse)",
        "fuse_type": "Blade-type, plastic case with color coding",
        "ratings_amps": [5, 7.5, 10, 15, 20, 25, 30, 40],
        "voltage_rating_v": 32,
        "nominal_melting_time_seconds_at_2x_rating": 30,
        "color_codes": {
            "5A": "Tan",
            "10A": "Red",
            "15A": "Blue",
            "20A": "Yellow",
            "25A": "Clear",
            "30A": "Green",
            "40A": "Orange"
        },
        "brands": ["Littelfuse, Blue Sea"],
        "cost_per_fuse_eur": 1,
        "installation": "Branch circuits via fuse block (individual circuit protection)",
        "standard": "ABYC E-11",
        "circuit_naming": "Each circuit labeled on block (e.g., 'Nav Lights 10A')",
        "failure_modes": ["False trips on inductive surge", "Slow response in marginal current"]
    },

    "Circuit_Breaker_Manual_Reset_20A": {
        "name": "Circuit Breaker (Manual Reset, 20A)",
        "breaker_type": "Magnetic circuit breaker (no thermal lag)",
        "ratings_amps": [2, 5, 10, 15, 20, 30, 50],
        "voltage_rating_v": 48,
        "trip_current_percent_over_rating": 125,  # Trips at 125% (2.5x = 50A)",
        "trip_response_time_ms": 50,  # Faster than fuse",
        "reset_method": "Manual push-button (no automatic)",
        "brands": ["Blue Sea Systems, Eaton Cutler-Hammer"],
        "cost_eur": 8,
        "advantage": [
            "Reusable (no spare cartridges needed)",
            "Faster response than fuse",
            "Visual trip indication"
        ],
        "disadvantage": [
            "Must reset manually (inconvenient)",
            "More expensive than fuses"
        ],
        "typical_use": "Branch circuits where nuisance trips unlikely",
        "failure_modes": ["Contact erosion causes erratic trips", "Spring fatigue"]
    },

    "Voltage_Regulator_PWM_Alternator": {
        "name": "PWM Voltage Regulator (Alternator Control)",
        "regulator_type": "Pulse-width-modulation external regulator",
        "input_voltage_range_v": [10, 16],  # Alternator unregulated output",
        "output_voltage_setpoint_v": 14.4,  # Bulk/absorption",
        "output_voltage_float_v": 13.2,  # Float (no load)",
        "temperature_compensation": True,  # -0.03V per degree C",
        "three_stage_charging": ["Bulk (14.4V full current)", "Absorption (14.4V decreasing)", "Float (13.2V)"],
        "switching_frequency_khz": 15,
        "efficiency_percent": 98,
        "brands": ["Balmar Max Charge, Ample Power, Motorola"],
        "cost_eur": 350,
        "heat_dissipation_watts": 200,  # At 200A difference input-output",
        "mounting": "Close to alternator (minimizes wiring)",
        "remote_sensing_wire": "Senses battery voltage directly (not alternator terminal)",
        "failure_modes": ["FET (field effect transistor) burnout from voltage spike"]
    },

    "Inverter_2000W_Pure_Sine": {
        "name": "Inverter (2000W Pure Sine Wave, 12V input)",
        "inverter_type": "Pure sine wave (clean AC, runs sensitive electronics)",
        "input_voltage_v": 12,  # or 24V, 48V variants",
        "input_voltage_range_v": [10, 15],
        "output_voltage_vac": 230,
        "output_frequency_hz": 50,
        "continuous_power_watts": 2000,
        "peak_power_watts": 4000,  # For 5 seconds (motor inrush)",
        "efficiency_percent": 92,
        "transfer_time_ms": 4,  # Switching to generator",
        "idle_power_draw_watts": 40,
        "brands": ["Victron Multiplus, Xantrex ProWatt, Mastervolt"],
        "cost_eur": 1200,
        "advantages": [
            "Quieter than generator",
            "No fuel consumption",
            "Clean power for microwave, fridge"
        ],
        "disadvantages": [
            "Draws heavy current from batteries (limits runtime)",
            "Idle load drains house bank continuously",
            "Cannot run continuous 2000W for >1 hour without recharge"
        ],
        "typical_use": "Microwave 5min, coffee maker, laptop charging, fridge during quiet hours",
        "failure_modes": ["Electrolytic capacitor failure in tropical heat"]
    },

    "Combiner_Four_String_PV": {
        "name": "Solar Combiner Box (4-String PV Array)",
        "function": "Combines multiple solar panel strings into single main breaker",
        "input_strings": 4,
        "fuse_per_string_amps": 20,
        "main_breaker_amps": 80,
        "fuse_type": "MRBF blade or ANL cartridge",
        "blocking_diode_per_string": True,  # Prevents back-current at night",
        "diode_type": "Schottky, 40A rated",
        "voltage_input_max_vdc": 600,
        "brands": ["Xantrex, Morningstar, Victron"],
        "cost_eur": 150,
        "installation": "On roof / hardtop near array, short feeder to charge controller",
        "bypass_diode_prevention": "Blocking diode essential (prevents reverse current through dark panels)",
        "failure_modes": ["Blocking diode failure causes array discharge at night"]
    }
}


# ============================================================================
# BONDING_AND_GROUNDING — Erdung und Potentialausgleich
# ============================================================================
BONDING_AND_GROUNDING: Dict[str, Dict[str, Any]] = {
    "DC_Negative_Bonding_System": {
        "name": "DC Negative Bonding System (Common Ground)",
        "standard": "ABYC E-11, ISO 10133",
        "function": "All DC negative circuits return to battery negative terminal through bonding",
        "main_negative_busbar": "Tinned copper, directly to battery negative",
        "conductor_sizing_rule": "Same gauge as positive conductor carrying same current",
        "color_code": "Black insulation (DC negative)",
        "splitters_branching": "Use tinned copper terminals or bus bar, avoid aluminum",
        "through_hull_bonding": "Engine negative, thruster negative, water heater case bonded",
        "star_point_grounding": "Single point of DC negative return (battery terminal)",
        "failure_mode": "Parallel ground paths (at engine, mast, hull) cause ground loops",
        "best_practice": "All negatives → main bus → battery negative; never split mid-circuit"
    },

    "AC_Shore_Power_Grounding": {
        "name": "AC Shore Power Grounding (230V Single Phase)",
        "standard": "IEC 60364, ABYC E-11, EN 61936",
        "grounding_system_type": "TT (Earthed neutral, local earth electrode)",
        "neutral_color": "Blue",
        "earth_ground_color": "Green/Yellow striped",
        "shore_pedestal_earth_conductor": "20mm² or larger (European standard)",
        "boat_earth_conductor_size_mm2": 10,
        "earth_electrode_method": "Zinc plate ~1m² in seawater, or copper rod",
        "earth_resistance_target_ohms": 8,  # Max per IEC 61936",
        "rcd_protection_ma": 30,  # 30mA Residual Current Device (breaker)",
        "brands_rcd": ["Schneider Electric, ABB, Siemens"],
        "failure_mode": "RCD malfunction leaves crew unprotected from electrocution",
        "testing": "Annual RCD test button press (simulates ground fault)"
    },

    "Bonding_System_Through_Hull_Zincs": {
        "name": "Through-Hull Hardware Bonding (Sacrificial Anode Protection)",
        "purpose": "Prevent galvanic corrosion of underwater metals",
        "through_hull_items": [
            "Seacock intakes", "Thru-hull rudder post", "Propeller shaft",
            "Transducers", "Anodes", "Keel attachment points"
        ],
        "bonding_conductor_gauge_awg": 8,  # #8 AWG minimum",
        "bonding_bus_location": "Inside hull, accessible for inspection",
        "anode_type": "Zinc (primary - high activity metal)",
        "anode_mass_per_boat_size": {
            "25_feet": 1.5,  # kg",
            "35_feet": 3.0,
            "50_feet": 5.0
        },
        "anode_replacement_interval_years": 2,
        "standard": "ABYC E-2, ISO 10133",
        "failure_mode": "Corrosion of thru-hull fittings, hull penetration leaks",
        "inspection": "Annual zincs inspection; replace if <50% remaining"
    },

    "Galvanic_Isolator_Isolation_Transformer": {
        "name": "Galvanic Isolator (Shore Power AC Isolation)",
        "function": "Breaks DC path between shore and boat, preventing stray current corrosion",
        "technology": "Transformer (1:1 isolation + 3% impedance) or diode-based isolator",
        "isolation_voltage_breakdown_v": 4000,
        "insertion_loss_percent": 0.5,
        "brands": ["Newmar Isolation Transformer, Blue Sea M-20X, Victron"],
        "cost_eur": 250,
        "installation": "Shore connector → isolator → boat distribution",
        "typical_application": "Mediterranean/crowded mooring (high stray current risk)",
        "leakage_current_test": "Annual insulation resistance test (>100 Megohms)",
        "failure_modes": ["Core saturation (transformer burnout)", "Diode short-circuit"]
    },

    "Isolation_Transformer_AC_Galvanic": {
        "name": "Isolation Transformer (High-Power AC Isolation, 16A)",
        "transformer_type": "Toroidal ferrite core, 1:1 turns ratio, 3% inductance",
        "input_voltage_vac": 230,
        "output_voltage_vac": 230,
        "max_output_current_amps": 16,
        "max_power_va": 3700,
        "insulation_class": "Class H (180°C wire insulation)",
        "isolation_impedance_ohms": 4000,
        "leakage_current_source_ma": 3.5,  # <3.5 spec maximum
        "brands": ["Newmar, Victron, Avel Lindberg"],
        "cost_eur": 350,
        "advantage": [
            "Breaks AC ground loop (stray current protection)",
            "EMI filtering benefit",
            "Isolation proven technology"
        ],
        "disadvantage": [
            "Weight (8-10 kg)",
            "Heat dissipation (mount in engine room)",
            "Cost vs. newer isolator tech"
        ],
        "maintenance": "Cooling fan check annually, insulation test 5-yearly"
    }
}


# ============================================================================
# MARINE_CONNECTORS — Steckverbinder Marine
# ============================================================================
MARINE_CONNECTORS: Dict[str, Dict[str, Any]] = {
    "Deutsch_DT_Connector_Series": {
        "name": "Deutsch DT Series Connector (IP67, Wet Matable)",
        "type": "Circular multi-pin connector, 2-12 pins",
        "housing_material": "Thermoplastic polyamide (Polyamide 46)",
        "pin_material": "Tin-plated copper, 20µm minimum",
        "waterproof_rating": "IP67 (1m immersion, 30 min)",
        "voltage_rating_v": 600,
        "current_per_pin_amps": 13,  # 0.5mm² contact max 13A",
        "contact_style": "Solid (not stranded wire)",
        "mating_cycles": 500,
        "insertion_force_n": 45,
        "retention_latch": "Locking keyed latch (prevents wrong orientation)",
        "cost_per_connector_eur": 8,
        "crimping_tool_required": "Yes, specific to contact type",
        "typical_use": "Thru-hull transducers, multipin underwater sensors, SCUBA rebreather comms",
        "brands": ["Deutsch, Phoenix Contact, Tyco"],
        "failure_modes": ["Pin corrosion in salt spray (needs sealing compound)", "Contact separation under vibration"]
    },

    "Terminal_Block_Screw_16A": {
        "name": "Terminal Block (Screw-Down, 16A Single)",
        "mounting": "DIN rail or bulkhead",
        "capacity_amps": 16,
        "voltage_rating_v": 250,
        "wire_gauge_range_awg": [12, 10, 8],  # Maximum #8 AWG per terminal",
        "conductor_type": "Solid or stranded (tinned preferred)",
        "spring_rating_n": 20,  # Contact spring force",
        "pitch_mm": 7.5,  # Distance between terminals",
        "material": "Polyamide 6.6, copper alloy contacts",
        "brands": ["Phoenix Contact, Weidmüller, Buchanan"],
        "cost_per_terminal_eur": 0.40,
        "typical_use": "Shore power inlet, main AC distribution, fused breaker outputs",
        "crimping": "No crimping required; direct wire insertion under screw",
        "failure_modes": ["Screw loosening under vibration (periodically retorque)"]
    },

    "Ring_Terminal_Tinned_8mm": {
        "name": "Ring Terminal (Tinned Copper, 8mm stud)",
        "stud_diameter_mm": 8,
        "wire_gauge_range_awg": [10, 8, 6],  # UMS cable primarily",
        "material": "Tinned copper (not aluminum)",
        "insulation_type": "Polyolefin (heat-shrink recommended)",
        "voltage_rating_v": 600,
        "current_capacity_amps": 40,  # Per 6mm² wire",
        "crimping_method": "Hydraulic or hand crimper (requires proper tool)",
        "pull-off_force_lbs": 100,  # Proper crimp minimum",
        "brands": ["Ancor, Littelfuse, Panduit"],
        "cost_per_terminal_eur": 0.08,
        "installation": "Crimp → slide onto M8 stud → tighten nut (80 Nm)",
        "failure_modes": ["Poor crimp (insufficient pressure) → oxidation", "Corrosion if bare copper used"]
    },

    "Butt_Connector_Tinned_4mm2": {
        "name": "Butt Connector (Tinned, 4mm² wire)",
        "splice_method": "Crimped connector joins two wire ends",
        "wire_gauge_range_mm2": [1.5, 2.5, 4.0, 6.0],
        "material": "Tinned copper (marine-grade)",
        "insulation": "Polyolefin heat-shrink",
        "voltage_rating_v": 600,
        "pull_strength_lbs": 200,
        "brands": ["Ancor, Littelfuse, Phoenix"],
        "cost_per_connector_eur": 0.06,
        "installation_note": "Never use solder joints on marine DC circuits (risk of cold solder)",
        "best_practice": "Crimp connections only; no soldering on power circuits",
        "failure_modes": ["Corroded connector joint (oxidation over months)"]
    },

    "Shore_Power_Connector_Mennekes_16A": {
        "name": "Mennekes Shore Power Connector (230V 16A, IP67)",
        "standard": "IEC 60309-2, EN 60309-2",
        "connector_type": "Industrial circular connector, 5-pin (L, N, E, two unused)",
        "voltage_rating_vac": 250,
        "current_rating_amps": 16,
        "frequency_hz": 50,
        "waterproof_rating": "IP67",
        "mating_cycles": 2000,
        "contact_material": "Silver-plated copper",
        "locking_mechanism": "Twist-lock cam (prevents accidental disconnect)",
        "inlet_installation": "Through-transom or cabin wall penetration",
        "shore_pedestal_connector": "Matching male receptacle (CEE 7/4 standard)",
        "cost_inlet_eur": 35,
        "cost_shore_cord_eur": 25,  # Per 25m cable",
        "typical_use": "European and Asian marinas (standard everywhere except N. America)",
        "failure_modes": ["Contact oxidation (green corrosion on copper)", "Locking mechanism crack"]
    },

    "NMEA_2000_Backbone_Connector": {
        "name": "NMEA 2000 M12 X-Code Connector (5-pin)",
        "standard": "IEC 61076-2-109, NMEA 2000 compatible",
        "pin_count": 5,
        "voltage_rating_v": 250,
        "current_per_pin_a": 4,
        "coding": "X-code (prevents wrong insertion)",
        "waterproof_rating": "IP67 (female receptacle)",
        "mating_cycles": 500,
        "connector_type": "M12 circular (8mm diameter)",
        "shielded_cable": "Yes, twisted pair with aluminum foil shield",
        "cable_impedance_ohm": 120,
        "brands": ["Raymarine, Garmin, Navico, Simrad"],
        "cost_t-connector_eur": 12,
        "cost_backbone_cable_per_meter_eur": 0.35,
        "backbone_max_length_m": 200,  # Theoretical; typically <100m practical",
        "termination_resistor": "120 Ohm at each end (critical for signal integrity)",
        "failure_modes": ["Backbone overcurrent (daisy-chain adds loads)", "Corroded shield (EMI interference)"]
    }
}


# ============================================================================
# NAVIGATION_ELECTRONICS — Navigationselektronik
# ============================================================================
NAVIGATION_ELECTRONICS: Dict[str, Dict[str, Any]] = {
    "Chartplotter_MFD_7_inch": {
        "name": "Multi-Function Display (MFD) 7-inch Chartplotter",
        "screen_size_inches": 7,
        "screen_type": "IPS LCD, 1024x600 pixels",
        "brightness_nits": 800,
        "viewing_angle_degrees": 170,
        "power_consumption_watts": 12,
        "operating_voltage_vdc": 12,
        "operating_temperature_celsius": (-20, 55),
        "waterproof_rating": "IP67",
        "gps_accuracy_meters": 5,
        "update_rate_hz": 10,  # Position fix",
        "integration": "NMEA 2000, NMEA 0183, Ethernet",
        "chart_source": "Pre-loaded (OpenCPN, Garmin) or SD card (Navionics+)",
        "brands": ["Garmin GPSMAP, Simrad GO series, Lowrance HDS Live"],
        "cost_eur": 400,
        "typical_use": "Navigation underway, anchor alert, route planning",
        "mounting": "Bracket on hardtop, pedestal, or cabin table",
        "failure_modes": [
            "GPS loss under metal hardtop",
            "LCD screen bleaching (UV damage)",
            "Saltwater spray corrosion of connectors"
        ]
    },

    "Radar_4kW_Radome": {
        "name": "Marine Radar (4kW Radome, S-band 3cm)",
        "radar_type": "Solid-state phased array (no rotating antenna)",
        "transmit_power_watts": 4000,
        "frequency_mhz": 9375,  # S-band (3cm wavelength)",
        "pulse_duration_microseconds": 0.3,  # Short pulse for close targets",
        "range_max_nm": 48,
        "range_resolution_meters": 20,
        "power_consumption_watts": 100,
        "operating_voltage_vdc": 24,
        "antenna_dimensions_m": [0.6, 0.4],  # Width × height",
        "integration": "NMEA 2000, Ethernet",
        "brands": ["Garmin GMR Fantom", "Navico Broadband 4G"],
        "cost_eur": 3000,
        "mounting": "Hardtop pole (1.5m minimum height for rain avoidance)",
        "typical_use": "Night navigation, fog detection, rain detection (green echo)",
        "maintenance": "Annual antenna alignment check",
        "failure_modes": [
            "Saltwater spray into radome",
            "Bearing misalignment (improper mounting)",
            "Magnetron tube failure (older tube radars)"
        ]
    },

    "AIS_Receiver_Transceiver_Class_B": {
        "name": "AIS (Automatic Identification System) Class B Transceiver",
        "ais_class": "Class B (receive + transmit, <25W)",
        "transmit_power_watts": 2,
        "frequency_mhz": 161.975 and 162.025,  # Two VHF channels",
        "update_rate_seconds": 30,  # Own-ship position broadcast interval",
        "receiver_range_nm": 20,  # Typical coastline",
        "integration": "NMEA 0183, NMEA 2000",
        "power_consumption_watts": 5,
        "operating_voltage_vdc": 12,
        "antenna_type": "Stainless steel whip, 0.6m",
        "brands": ["Garmin AIS 5, Simrad HALO, SRT Black Box"],
        "cost_eur": 180,
        "typical_use": "See other vessels on MFD, avoid collision, port tracking",
        "failure_modes": [
            "Antenna corrosion (salt spray)",
            "Receiver overload near ships (AGC malfunction)",
            "VHF interference (nearby radio transmission)"
        ],
        "regulation": "Some regions mandate AIS for vessels >300GT or commercial traffic"
    },

    "VHF_Radio_Handheld": {
        "name": "Handheld VHF Radio (12W, IPX7 Waterproof)",
        "vhf_channels": 88,  # International marine bands",
        "transmit_power_watts": [1, 5, 12],  # Switchable",
        "frequency_range_mhz": [156.0, 163.0],
        "channel_spacing_khz": 12.5,
        "squelch_threshold_dbm": -107,  # Sensitivity",
        "operating_time_hours": 8,  # Per charge",
        "battery_capacity_mah": 1800,
        "waterproof_rating": "IPX7 (floats, 1m submersion 30 min)",
        "temperature_range_celsius": (-10, 60),
        "power_consumption_standby_mw": 100,
        "power_consumption_transmit_w": 6,
        "antenna_length_mm": 150,
        "brands": ["Icom IC-M24, Standard Horizon HX890, Kenwood"],
        "cost_eur": 150,
        "typical_use": "Mayday distress, local communication <10nm",
        "sos_button": "Automated DSC distress message with GPS position",
        "failure_modes": [
            "Battery corrosion (never leave in radio overnight)",
            "Water intrusion seal failure"
        ]
    },

    "Depth_Sounder_Transducer": {
        "name": "Depth Sounder (Transducer + Display)",
        "frequency_khz": [50, 200],  # Dual frequency",
        "transducer_type": "Hull-mounted bronze or plastic",
        "operating_depth_max_m": 300,
        "accuracy_percent_of_reading": 5,
        "update_rate_hz": 10,
        "power_consumption_watts": 2,
        "operating_voltage_vdc": 12,
        "display_type": "LCD, 3-4 digits",
        "integration": "NMEA 0183",
        "brands": ["Garmin, Lowrance, Navico Simrad"],
        "cost_eur": 50,
        "installation": "Through-hull transducer (critical: no air bubbles under it)",
        "typical_use": "Anchor monitoring (audible alert at anchor watch depth)",
        "failure_modes": [
            "Air bubble accumulation under transducer (false shallow reading)",
            "Transducer fouling (seaweed, barnacle)",
            "Cable corrosion at connector"
        ]
    },

    "Wind_Instruments_Masthead": {
        "name": "Wind Instruments (Masthead Wind Speed + Direction)",
        "wind_speed_range_knots": [0, 80],
        "wind_speed_accuracy_percent": 5,
        "wind_direction_accuracy_degrees": 5,
        "sensor_type": "Propeller cups (speed) + vane (direction)",
        "propeller_diameter_mm": 30,
        "operating_temperature_celsius": (-40, 80),
        "power_consumption_ma": 50,
        "operating_voltage_vdc": 12,
        "cable_type": "2-conductor twisted pair (sometimes 4-conductor for redundancy)",
        "cable_length_limit_m": 100,
        "integration": "NMEA 0183",
        "brands": ["Garmin, Simrad, Raymarine"],
        "cost_eur": 200,
        "mounting": "Top of mast (most critical height for accurate measurement)",
        "typical_use": "Real-time wind display for sail trim, autopilot input",
        "failure_modes": [
            "Propeller degradation (UV, saltwater oxidation)",
            "Vane bearing wear (oscillation, sluggish response)",
            "Connector corrosion at mast-to-cabin transition"
        ]
    },

    "Autopilot_Course_Computer": {
        "name": "Autopilot (Compass-Based Steering Computer)",
        "autopilot_type": "Flux-gate compass with rudder servo control",
        "steering_range_degrees": [0, 360],
        "heading_accuracy_degrees": 2,
        "compass_deviation_compass_calibration": "Required before first use",
        "rudder_servo_type": "Linear hydraulic or electric",
        "servo_response_time_seconds": 3,
        "power_consumption_watts": 20,
        "operating_voltage_vdc": 12,
        "control_interface": ["Physical buttons", "NMEA 2000"],
        "integration": "Chartplotter input for waypoint steering",
        "brands": ["Garmin GHP Compact, Simrad OP25, Raymarine EV-200"],
        "cost_eur": 600,
        "typical_use": "Hands-free steering underway, reduces crew fatigue",
        "installation": "Compass mounted on binnacle or hardtop; servo in steering system",
        "failure_modes": [
            "Compass deviation calibration error (oscillating course)",
            "Servo stiction (stuck, jerky response)",
            "Rudder feedback cable corrosion"
        ]
    },

    "Satellite_Communication_SSB_Radio": {
        "name": "Satellite Communication (Iridium Handset or SSB HF Radio)",
        "technology": "Iridium LEO constellation (SSB = deprecated Single Sideband)",
        "coverage": "Global ocean (Iridium complete, SSB skip-dependent)",
        "latency_seconds": 2,  # Iridium latency <2 seconds typical
        "data_speed_kbps": [2.4, 10],  # Voice / data variant",
        "handset_battery_hours": 5,
        "typical_cost_iridium_handset_eur": 600,
        "typical_cost_ssb_radio_eur": 2000,
        "brands": ["Iridium GO!, Isatphone, Collins SSB"],
        "power_consumption_transmit_watts": [5, 50],  # Handheld vs. ship system",
        "operating_voltage": [12, 24],
        "typical_use": "Emergency distress (EPIRB backup), crew check-ins, weather routing",
        "failure_modes": [
            "Handset satellite lock loss (in cabin/below deck)",
            "SIM card lockout after failed login",
            "Antenna corrosion (SSB system)"
        ],
        "cost_monthly_plan_eur": 20,  # Iridium $0.15/min = ~€100 typical use"
    }
}


# ============================================================================
# LIGHTING_SYSTEMS — Beleuchtungssysteme
# ============================================================================
LIGHTING_SYSTEMS: Dict[str, Dict[str, Any]] = {
    "Navigation_Light_Port_Starboard_Red_Green": {
        "name": "Navigation Light (Port Red, Starboard Green)",
        "regulation": "COLREG International Rules of the Road",
        "light_type": "LED 0.5W or incandescent 10W",
        "visible_range_nm": 1,  # Minimum COLREG requirement",
        "color_specification": "Port: Red 630nm, Starboard: Green 500nm",
        "light_coverage_arc_degrees": 112.5,  # Port light looks across bow and port quarter",
        "mounting": "Port and starboard rails/stanchions, 1m+ above deck",
        "power_consumption_led_watts": 0.5,
        "power_consumption_incandescent_watts": 10,
        "operating_voltage_vdc": 12,
        "ip_rating": "IP66",
        "brands": ["Perko, Aqua Signal, Hella"],
        "cost_per_light_eur": 40,
        "failure_mode": "Lens clouding (oxidation) reduces effective range below 1nm",
        "maintenance": "Annual lens cleaning (saltwater deposits)"
    },

    "Anchor_Light_All_Round_White": {
        "name": "Anchor Light (All-Round White Light, 20W equivalent LED)",
        "regulation": "COLREG Rule 30 (at anchor)",
        "light_type": "LED 2W (equivalent 20W incandescent)",
        "visible_range_nm": 2,
        "color": "White 4000K or 5600K",
        "light_coverage_arc_degrees": 360,  # Omnidirectional",
        "mounting": "Masthead or upper rigging (highest point)",
        "power_consumption_watts": 2,
        "power_consumption_incandescent_old_watts": 20,
        "operating_voltage_vdc": 12,
        "flash_rate_flashes_per_minute": 10,  # Typical",
        "ip_rating": "IP67",
        "brands": ["Aqua Signal, Perko, Signalmaster"],
        "cost_eur": 60,
        "typical_use": "Overnight at anchor in traffic areas (mandatory if within 1nm of shipping lane)",
        "failure_modes": [
            "Mast vibration loosens fixture",
            "LED driver failure (no flash)",
            "Wire corrosion at mast connection"
        ]
    },

    "Interior_LED_Cabin_Lighting": {
        "name": "Interior LED Cabin Light (3W, Cool White)",
        "light_type": "SMD (surface-mount) LED module",
        "power_consumption_watts": 3,
        "color_temperature_k": 4000,  # Cool white; 3000K warm not recommended (eyes)",
        "brightness_lumens": 250,
        "equivalent_incandescent_watts": 25,
        "operating_voltage_vdc": 12,
        "ip_rating": "IP65 (splash-proof)",
        "mounting": "Ceiling or cabin sole recessed fixture",
        "heat_dissipation": "Passive (no fan, silent)",
        "cost_per_fixture_eur": 15,
        "typical_circuit": "12V positive through switch; negative to DC return bus",
        "common_error": "Using 230V AC fixtures below deck (fire/shock hazard)",
        "brands": ["Lumitec, AAA Lighting, Hella"],
        "failure_modes": [
            "Cold solder joints (vibration)",
            "Driver electrolytic capacitor failure in heat"
        ]
    },

    "Cockpit_Spotlight_LED_20W": {
        "name": "Cockpit Spotlight (LED 20W equivalent, Steerable)",
        "light_type": "CREE or Philips LED, 10°–30° beam angle",
        "power_consumption_watts": 2.5,
        "light_output_lumens": 1400,
        "equivalent_incandescent_watts": 20,
        "beam_angle_degrees": [10, 20, 30],
        "color_temperature_k": 6500,  # Daylight (for night vision compatibility)",
        "operating_voltage_vdc": 12,
        "mounting": "Hardtop forward-facing, motorized pan/tilt",
        "ip_rating": "IP67",
        "brands": ["OSRAM, Lumitec, Attwood"],
        "cost_eur": 80,
        "typical_use": "Navigating narrow channels at night, anchoring out",
        "failure_modes": [
            "Motor failure (pan/tilt jam)",
            "Lens hazing (salt spray film)"
        ],
        "power_note": "20W incandescent draws 20A @ 12V; 2.5W LED draws 0.2A (huge savings)"
    },

    "Underwater_Hull_Light_LED_Green": {
        "name": "Underwater Hull Light (LED Green, 9W)",
        "mounting_location": "Through-hull underwater on port/starboard sides",
        "light_type": "High-power LED, 520nm green (fish attraction, also mooring light)",
        "power_consumption_watts": 9,
        "light_output_lumens": 600,
        "beam_angle_degrees": 120,
        "depth_rating_meters": 10,  # Operating depth",
        "pressure_rating_bar": 2,
        "waterproof_rating": "IP68 fully submersed",
        "saltwater_immersion": True,
        "operating_voltage_vdc": 12,
        "control": "Manual switch or timer (3hr auto-off typical)",
        "brands": ["Lumitec, Attwood, Seadog"],
        "cost_eur": 120,
        "typical_use": "Fish attraction while at anchor (evening entertainment), mooring visibility",
        "failure_modes": [
            "Saltwater corrosion (requires annual disassembly/regrease)",
            "Thermal runaway (LED overheating under prolonged use)"
        ],
        "color_options": ["Green (fish attraction)", "Blue (mooring)", "Warm white (deck work)"]
    },

    "Searchlight_Spotlight_Halogen_500W": {
        "name": "Searchlight (Halogen Remote Control, 500W)",
        "light_source": "Halogen 500W (or LED 30W equivalent)",
        "color_temperature_k": 3200,  # Warm white",
        "beam_angle_degrees": [8, 12, 20],
        "light_output_lumens": [5000, 3500, 2500],
        "visible_range_meters": [200, 150, 100],
        "mounting": "Remote control motorized pan/tilt, hardtop or mast",
        "power_consumption_watts": 500,  # Halogen; 30W LED version common",
        "operating_voltage_vdc": 12,
        "color_temperature_led_k": 5600,  # If LED variant",
        "power_led_variant_watts": 30,
        "ip_rating": "IP65",
        "brands": ["OSRAM, Hella, Jabsco"],
        "cost_halogen_eur": 300,
        "cost_led_eur": 150,
        "typical_use": "Night navigation (large rivers, narrow channels), docking large boats",
        "failure_modes": [
            "Halogen bulb burnout (cannot touch with bare hands; skin oil causes failure)",
            "Motor failure (pivot shaft wear)",
            "Remote control receiver loss"
        ],
        "note": "LED searchlight trend (lower power, no heat, longer life)"
    }
}


# ============================================================================
# CABLE_SIZING_RULES — Kabelquerschnitt-Berechnung
# ============================================================================
def calculate_cable_size(
    current_amps: float,
    circuit_length_meters: float,
    voltage_system: int = 12,
    max_voltage_drop_percent: float = 3.0
) -> Dict[str, Any]:
    """
    Calculate required cable cross-section per ABYC E-11 voltage drop rule.

    Args:
        current_amps: Maximum continuous circuit current
        circuit_length_meters: Length from battery to load (one-way)
        voltage_system: 12, 24, or 48 voltage
        max_voltage_drop_percent: Typical 3% (power circuits), 10% (lighting)

    Returns:
        Dict with cable_mm2, voltage_drop_v, loss_watts, recommendation

    Formula: V_drop = (2 × L × I × R) / 1000
        where L = length (m), I = current (A), R = resistance (ohm/1000m)
    """
    # Tinned copper marine cable resistance (ohm per 1000m)
    copper_resistance_per_1000m = {
        0.5: 42.0,
        1.0: 21.0,
        1.5: 14.0,
        2.5: 8.4,
        4.0: 5.3,
        6.0: 3.5,
        10.0: 2.1,
        16.0: 1.3,
        25.0: 0.83,
        35.0: 0.59,
        50.0: 0.42,
        70.0: 0.30
    }

    max_allowable_drop_v = (voltage_system * max_voltage_drop_percent) / 100

    # Find minimum cable size
    selected_mm2 = None
    for mm2, resistance in sorted(copper_resistance_per_1000m.items()):
        voltage_drop_v = (2 * circuit_length_meters * current_amps * resistance) / 1000000
        if voltage_drop_v <= max_allowable_drop_v:
            selected_mm2 = mm2
            selected_resistance = resistance
            selected_drop = voltage_drop_v
            break

    if selected_mm2 is None:
        # No suitable size found; use largest and flag warning
        selected_mm2 = max(copper_resistance_per_1000m.keys())
        selected_resistance = copper_resistance_per_1000m[selected_mm2]
        selected_drop = (2 * circuit_length_meters * current_amps * selected_resistance) / 1000000
        warning = "UNDERSIZED (exceeds max voltage drop)"
    else:
        warning = None

    loss_watts = (selected_drop * selected_drop * 1000) / (voltage_system * current_amps)

    return {
        "cable_cross_section_mm2": selected_mm2,
        "voltage_drop_v": round(selected_drop, 3),
        "voltage_drop_percent": round((selected_drop / voltage_system) * 100, 2),
        "power_loss_watts": round(loss_watts, 2),
        "copper_resistance_per_km_ohm": copper_resistance_per_1000m[selected_mm2] / 1000,
        "recommendation": f"Use {selected_mm2}mm² cable ({selected_mm2 / 1.27:.0f} AWG equivalent)",
        "warning": warning,
        "standard": "ABYC E-11 (3% for power, 10% for lighting)"
    }


# ============================================================================
# ELECTRICAL_FAILURE_MODES — Häufige Fehler und Diagnose
# ============================================================================
ELECTRICAL_FAILURE_MODES: Dict[str, Dict[str, Any]] = {
    "Terminal_Corrosion_Green_Oxide": {
        "name": "Terminal Corrosion (Green Copper Oxide)",
        "symptom": [
            "Voltage drop across connection",
            "Battery doesn't charge fully",
            "Dim cabin lights under load",
            "Slow engine starter cranking",
            "Radio shuts down under load"
        ],
        "visible_signs": "Green or white crust on battery posts and connectors",
        "root_cause": [
            "Dissimilar metals (copper + lead + steel)",
            "Saltwater spray exposure",
            "Moisture inside terminal",
            "Acid vapor from wet-cell batteries"
        ],
        "diagnosis_method": [
            "Voltage test: Battery 12.5V, but only 11.8V at load",
            "Resistance test: Measure with multimeter across corroded connection (should be <0.01 ohm, bad is >0.1)",
            "Visual inspection: Look for oxidation color (green = copper oxide, white = lead corrosion)"
        ],
        "repair": [
            "Disconnect battery (safety!)",
            "Remove terminal and scrub with wire brush or sandpaper",
            "Clean post with baking soda + water (neutralizes acid)",
            "Reinstall terminal with thin anti-corrosion grease layer",
            "Retorque stud (battery post: 80 Nm, buss bar: 60 Nm)"
        ],
        "prevention": [
            "Coat battery terminals with dielectric grease annually",
            "Ensure sealed/AGM batteries (no acid vapor)",
            "Keep electrical areas ventilated and dry",
            "Use tinned copper connectors (resist oxidation)"
        ],
        "diagnosis_time_minutes": 5
    },

    "Voltage_Drop_Undersized_Cable": {
        "name": "Voltage Drop (Excessive, Undersized Cable)",
        "symptom": [
            "Engine starter barely cranks (11V at starter, should be 10.5V minimum)",
            "Cabin lights dim when thruster operates",
            "Battery charges slowly (alternator regulation confused)",
            "Navigation light flicker underway"
        ],
        "root_cause": [
            "Cable too small for circuit current",
            "Circuit too long (distance from battery >10m)",
            "Poor connections adding series resistance",
            "Corroded terminals (see Corrosion failure mode)"
        ],
        "diagnosis_method": [
            "Voltage test: Measure at battery (e.g., 14.2V), then at load (e.g., 13.1V). Drop = 1.1V = 7.7% (bad!)",
            "Current test: Measure circuit current under load with clamp meter",
            "Use formula: V_drop = (2 × L × I × R) / 1000; L = length, I = amps, R = cable resistance"
        ],
        "repair": [
            "Upgrade cable to larger cross-section (see CABLE_SIZING_RULES function)",
            "Example: 4mm² to 6mm² or 10mm²",
            "Minimize circuit length if possible",
            "Clean all connections"
        ],
        "prevention": [
            "Size cable correctly at design (use 3% rule for power, 10% for lighting)",
            "Use multiple smaller diameter runs instead of single long run (reduce inductance)"
        ],
        "common_error": "Using automotive cable (0.5mm²) for yacht 50A main circuit (dangerously undersized)"
    },

    "Battery_Sulfation_Deep_Discharge": {
        "name": "Battery Sulfation (Lead-Acid Type)",
        "symptom": [
            "Battery won't hold charge",
            "Cranking amps low",
            "High internal resistance",
            "Charger shuts off early (thinks battery is full)"
        ],
        "root_cause": [
            "Deep discharge below 10.5V (Lead-Acid) for extended period",
            "Left uncharged for weeks",
            "Repetitive partial discharge without full recharge (golf-cart pattern)",
            "High ambient temperature accelerating chemical degradation"
        ],
        "diagnosis_method": [
            "Voltage test: Resting battery at 12.2V instead of normal 12.7V",
            "Charge test: After charging, battery voltage drops quickly (e.g., 12.9V → 12.0V in 2 hours)",
            "Internal resistance: High resistance indicates sulfation"
        ],
        "repair": [
            "Slow charge (0.1C rate) for 12+ hours (50Ah battery = 5A charge current)",
            "Pulse charger can sometimes recover sulfation (e.g., Optima chargers)",
            "If unrecoverable: Replace battery (cost ~€100-200)"
        ],
        "prevention": [
            "Never allow discharge below 50% DoD for lead-acid (depth of discharge)",
            "Charge weekly during off-season",
            "Install solar trickle charger (5-10W) for monthly discharge",
            "Keep batteries in cool location (<20°C) when not in use"
        ],
        "lifespan_impact": "Single deep discharge reduces remaining cycle life by ~10-20%"
    },

    "Alternator_Diode_Failure_No_Charging": {
        "name": "Alternator Diode Failure (No Charging Output)",
        "symptom": [
            "Battery not charging underway",
            "Dashboard ammeter shows zero (or negative discharge)",
            "Charging light stays on (no regulation feedback)",
            "Battery voltage drops slowly despite running engine"
        ],
        "root_cause": [
            "One or more of 6 alternator rectifier diodes failed (heat stress, saltwater corrosion, water intrusion)",
            "Diode short-circuit draws current in wrong direction",
            "Wet-salt environment (120°F+ in engine room) accelerates failure"
        ],
        "diagnosis_method": [
            "Voltage test: Engine off = 12.7V, engine at 1500 rpm = 12.7V (no increase = no charging)",
            "Ammeter test: Clamp meter on positive alternator output = 0A",
            "Resistance test: Multimeter across alternator output = low resistance (should be high when off)",
            "Visual inspection: Moisture or saltwater inside alternator connector"
        ],
        "repair": [
            "Replace alternator (cost €200-400 depending on size/brand)",
            "Or replace rectifier diode set (DIY for skilled mechanic, €50-80)",
            "Have alternator tested by auto electrician (€20 bench charge)"
        ],
        "prevention": [
            "Install sealed alternator connector to keep salt spray out",
            "Ensure engine room ventilation (reduces temperature)",
            "Use dielectric grease on alternator housing to shed water",
            "Annual alternator output check (should be >13.5V at idle)"
        ],
        "failure_rate": "Most common alternator failure in marine environments (hot + salty)"
    },

    "Ground_Fault_Leakage_to_Hull": {
        "name": "Ground Fault (Unintended Current Path to Hull)",
        "symptom": [
            "Crew feels mild electric shock when touching railings or metal fixtures",
            "Battery discharges fast even with no loads on",
            "RCD (residual current device) trips when shower runs",
            "Corrosion appears on underwater metal fittings (electrolysis)"
        ],
        "root_cause": [
            "Water intrusion into submerged electrical box (thru-hull penetration)",
            "Damaged cable insulation (chafe against metal edge)",
            "Corroded connector underwater (transducer, thruster)",
            "AC leakage from shore power through isolation transformer failure"
        ],
        "diagnosis_method": [
            "Megohm test: Multimeter resistance test from all circuits to hull = should be >1 Megohm",
            "If <100 Kohm = definite ground fault",
            "Insulation tester (hipot): Apply 500V DC, measure leakage current (<1mA = safe)",
            "Visual inspection: Look for pinhole corrosion on connectors or cable"
        ],
        "repair": [
            "Isolate faulty circuit (disconnect at main switch)",
            "Inspect for water/corrosion and dry out (hair dryer)",
            "Replace damaged insulation or connector",
            "Reinstall and test"
        ],
        "prevention": [
            "Seal all through-hull electrical penetrations with potting compound",
            "Route cables away from chafe points",
            "Annual megohm test (part of surveyor's electrical survey)"
        ],
        "health_risk": "Chronic exposure to ground faults can cause fibrillation (dangerous)"
    },

    "Reverse_Polarity_DC_Damage": {
        "name": "Reverse Polarity (Positive to Negative Terminal)",
        "symptom": [
            "Instant circuit breaker trip or fuse blow (on reconnection)",
            "Electrical equipment doesn't turn on",
            "Smoke/fire if polarity held for >5 seconds",
            "Alternator/charger destroyed immediately"
        ],
        "root_cause": [
            "Shore charger or second battery connected backwards (positive to negative)",
            "Crew confusion during emergency starting procedure (jump-start)",
            "Defective VSR relay (connects reversed polarity)"
        ],
        "diagnosis_method": [
            "Visual inspection: Check polarity before connecting any source (RED = +, BLACK = −)",
            "Ohm test: Never apply power until verified (multimeter on positive cable to ground = open circuit)"
        ],
        "repair": [
            "Do NOT apply power; immediately disconnect source",
            "Check all electrical devices (charger, inverter, alternator regulator likely destroyed)",
            "Replace damaged components"
        ],
        "prevention": [
            "Color-code cables clearly (red shrink-wrap on positive, black on negative)",
            "Label battery terminal posts: +12V and GND (ground)",
            "Use polarity-proof connectors (Deutsch DT coding prevents wrong insertion)",
            "Procedure check: Always verify polarity with multimeter before jump-start or shore charger connection"
        ],
        "cost_impact": "Alternator regulator (~€300) + charger (~€200) destruction = €500+ repair"
    },

    "Overloaded_Circuit_Nuisance_Trip": {
        "name": "Overloaded Circuit (Continuous Trip or Slow Burnout)",
        "symptom": [
            "Circuit breaker trips repeatedly",
            "Fuse blows immediately after replacement",
            "Cable feels warm to touch",
            "Smell of burning insulation"
        ],
        "root_cause": [
            "Too many devices on single circuit (aggregated load exceeds fuse/breaker rating)",
            "Load larger than circuit designed for (e.g., large air-conditioner on 15A circuit)",
            "Ground fault causing high inrush current (masked by high-impedance short)",
            "Faulty device drawing excessive current (motor stalled, heater element failed)"
        ],
        "diagnosis_method": [
            "Load audit: Add up all loads on circuit (amps) and compare to breaker/fuse rating",
            "Ammeter clamp test: Measure actual current on circuit at full load",
            "Thermal camera: Aim at cable during operation; hot spot = overload location",
            "Voltage drop: Excessive drop during load indicates high current × resistance"
        ],
        "repair": [
            "Identify offending load and isolate (remove device or move to different circuit)",
            "Install larger breaker/fuse ONLY if cable can handle increased current (upgrade cable if needed)",
            "Never bypass breaker/fuse with heavier rating without upgrading cable"
        ],
        "prevention": [
            "Plan circuits: 15A circuit × 230V AC = 3.4 kW max (microwave + kettle = overload!)",
            "Use load management: Don't run multiple high-load devices simultaneously",
            "Dedicate circuits for high-power loads (thruster, heater, air-con)"
        ],
        "dangerous_error": "Bypassing 15A fuse with 20A fuse to solve nuisance trips = Fire hazard!"
    },

    "Chafe_Damage_Wire_Insulation": {
        "name": "Chafe Damage (Cable Insulation Worn Through)",
        "symptom": [
            "Short circuit or ground fault if wire touches metal",
            "Intermittent function (chafe alternates between contact and gap)",
            "Voltage loss if chafed area has high resistance"
        ],
        "root_cause": [
            "Cable routed over sharp edge (pulpit corner, through rigging hole)",
            "Cable not secured; moves during motion and rubs fixture",
            "Inadequate conduit or protective sleeving",
            "UV degradation of insulation (exposed topside cable)"
        ],
        "diagnosis_method": [
            "Visual inspection: Follow cable path and look for thin spots or exposed copper",
            "Hand feel: Gently rub along insulation looking for rough spots or cuts",
            "Megohm test: Low resistance to hull suggests chafe-to-ground"
        ],
        "repair": [
            "Short-term (temporary): Wrap damaged section with electrical tape or heat-shrink tubing",
            "Permanent: Replace entire cable run with new one, routed away from sharp edges",
            "Protective: Sleeve cable through marine-grade conduit (Ancor Adhesive-Lined Shrink Tubing)"
        ],
        "prevention": [
            "Route cables through existing cable trays or conduit",
            "Use cable clips every 12 inches (30cm) to prevent movement",
            "Seal cable penetrations with potting compound (prevents water + chafe)",
            "Use armored cable (Flex Armor) in high-motion areas"
        ],
        "high_risk": "Chafe in engine room = potential fire hazard; inspect monthly"
    },

    "Electrolysis_Underwater_Metal_Corrosion": {
        "name": "Electrolysis (Stray Current Corrosion of Underwater Metals)",
        "symptom": [
            "Propeller loses coating (bare bronze exposed)",
            "Through-hull fittings pit and deteriorate",
            "Fasteners around hull corrode rapidly (SS bolts turn black)",
            "Zinc anodes dissolve in weeks instead of years"
        ],
        "root_cause": [
            "Stray DC current from improperly grounded AC shore power",
            "Galvanic coupling between different metals (aluminum and bronze)",
            "Failed isolation transformer (AC leakage path to hull)",
            "Inadequate bonding system (underwater metals not connected to negative return)"
        ],
        "diagnosis_method": [
            "Potential test: Measure voltage between propeller and remote seawater reference electrode",
            "Should be -0.8V to -1.0V (cathodic protection range)",
            "If >-1.2V = electrolysis risk; if 0V (anodic) = severe corrosion underway",
            "Zinc inspection: Consume only 10-15% per season; rapid loss = electrolysis"
        ],
        "repair": [
            "Trace and eliminate stray current source (typically shore charger or AC leakage)",
            "Install/upgrade bonding system connecting all underwater metals",
            "Install sacrificial zinc anodes if not present (propeller, keel, rudder)"
        ],
        "prevention": [
            "Use isolation transformer on shore power (breaks AC galvanic path)",
            "Bond all underwater hardware to single negative bus",
            "Annual zinc inspection and replacement",
            "Install stray current meter for early warning"
        ],
        "risk_level": "High; propeller corrosion = €2000+ repair cost"
    },

    "Water_Intrusion_Connector_Corrosion": {
        "name": "Water Intrusion into Electrical Connector",
        "symptom": [
            "Equipment intermittently loses power or function",
            "Connector pins turn green/white with corrosion",
            "High resistance connection (voltage drop, heating)",
            "Burning smell near connector"
        ],
        "root_cause": [
            "Damaged connector seal (o-ring degraded or missing)",
            "Cable pulled through water during operation (e.g., engine exhaust water)",
            "Improper storage (submerged battery box during winter)"
        ],
        "diagnosis_method": [
            "Visual: Disconnect and inspect pins for corrosion (green = copper oxide)",
            "Resistance: Measure across connector pins (bad: >0.1 ohm, good: <0.01 ohm)",
            "Time-of-failure correlation: Intermittent faults after wet weather = water intrusion"
        ],
        "repair": [
            "Dry out completely (hair dryer on low heat, silica packets overnight)",
            "Clean pins with electrical contact cleaner (Isopropanol-based)",
            "Wipe with small brass brush to remove oxide",
            "Apply thin layer of dielectric grease before reassembly"
        ],
        "prevention": [
            "Use marine-grade IP67 connectors for below-deck applications",
            "Coat connector entry points with potting compound (flexible epoxy)",
            "Annual connector inspection and grease reapplication",
            "Route cables to avoid standing water or splash zones"
        ],
        "failure_mode_consequence": "Intermittent connection can cause battery overcharge (regulator confused by voltage drop)"
    }
}


# ============================================================================
# ASSESSMENT FUNCTION
# ============================================================================
def assess_electrical_installation(
    system_type: str,
    cable_type: str,
    cross_section_mm2: float,
    circuit_length_m: float,
    current_a: float,
    voltage_system: int = 12,
    fuse_rating_a: float = 20,
    connection_type: str = "ring_terminal",
    age_years: int = 3
) -> Dict[str, Any]:
    """
    Assess electrical installation for safety and performance.

    Args:
        system_type: "DC_main", "AC_shore", "solar_charging", "alternator"
        cable_type: Type from CABLE_TYPES dict keys
        cross_section_mm2: Actual cable cross-section installed
        circuit_length_m: Distance from battery/source to load
        current_a: Maximum continuous current
        voltage_system: 12, 24, or 48
        fuse_rating_a: Installed fuse/breaker amperage
        connection_type: "ring_terminal", "butt_connector", "soldered", etc.
        age_years: Years since installation

    Returns:
        Comprehensive assessment with score (0-100), findings, recommendations
    """
    findings = []
    score = 100

    # ---- CABLE SIZING CHECK
    result_cable = calculate_cable_size(current_a, circuit_length_m, voltage_system, max_voltage_drop_percent=3.0)
    required_mm2 = result_cable["cable_cross_section_mm2"]

    if cross_section_mm2 < required_mm2:
        score -= 25
        findings.append(f"CRITICAL: Cable undersized. Installed: {cross_section_mm2}mm², Required: {required_mm2}mm². Voltage drop: {result_cable['voltage_drop_percent']:.2f}%")
    elif cross_section_mm2 == required_mm2:
        findings.append(f"Cable sizing adequate ({cross_section_mm2}mm²). Voltage drop: {result_cable['voltage_drop_percent']:.2f}%")
    else:
        findings.append(f"Cable oversized (acceptable safety margin). {cross_section_mm2}mm² > required {required_mm2}mm². Voltage drop: {result_cable['voltage_drop_percent']:.2f}%")

    # ---- FUSE SIZING CHECK
    # Rule: Fuse should be ~125% of maximum continuous current for protective coordination
    min_fuse_a = current_a * 1.25
    max_fuse_a = current_a * 1.5

    if fuse_rating_a < min_fuse_a:
        score -= 15
        findings.append(f"WARNING: Fuse rating too low. Installed: {fuse_rating_a}A, Recommended: {min_fuse_a:.0f}A–{max_fuse_a:.0f}A (high nuisance trip risk)")
    elif fuse_rating_a > max_fuse_a * 2:
        score -= 20
        findings.append(f"CRITICAL: Fuse rating too high. Installed: {fuse_rating_a}A, Max acceptable: {max_fuse_a:.0f}A (fire hazard if cable overload)")
    else:
        findings.append(f"Fuse rating appropriate ({fuse_rating_a}A for {current_a}A circuit)")

    # ---- CONNECTION TYPE CHECK
    if connection_type == "soldered":
        score -= 10
        findings.append("WARNING: Soldered connections detected. ABYC E-11 recommends crimped terminals only for DC power circuits (solder joint corrosion risk in marine)")
    elif connection_type == "butt_connector":
        findings.append("Connection type acceptable (butt connector with marine-grade tinning)")
    elif connection_type == "ring_terminal":
        findings.append("Connection type excellent (ring terminal, standard marine practice)")
    else:
        findings.append(f"Connection type: {connection_type}")

    # ---- CABLE AGE CHECK
    if age_years > 10:
        score -= 5
        findings.append("INFO: Cable age >10 years. Consider replacement after next haul-out (insulation degradation possible)")
    elif age_years > 5:
        findings.append("INFO: Cable age >5 years. Schedule inspection for UV damage and corrosion")

    # ---- SYSTEM-SPECIFIC CHECKS
    if system_type == "AC_shore":
        # AC-specific: phase, neutral, earth all present?
        findings.append("AC shore power system: Verify RCD (30mA residual current device) installed in breaker panel")
        score -= 5 if age_years > 5 else 0

    elif system_type == "solar_charging":
        findings.append("Solar charging: Verify blocking diodes present in combiner box (prevents night-time array discharge)")

    elif system_type == "alternator":
        findings.append("Alternator output: Verify voltage regulator set to 14.4V bulk / 13.2V float. Temperature compensation enabled?")

    # ---- FINAL SCORE AND RECOMMENDATION
    if score >= 90:
        status = "EXCELLENT"
        action = "No immediate action required. Continue annual inspections."
    elif score >= 75:
        status = "ACCEPTABLE"
        action = "Schedule service within 12 months. Address warnings listed above."
    elif score >= 50:
        status = "POOR"
        action = "Electrical system requires immediate attention. Do not operate vessel until corrected."
    else:
        status = "CRITICAL"
        action = "HAZARD: Electrical system unsafe. Consult marine electrician immediately. Do not operate."

    return {
        "assessment_status": status,
        "score_0_to_100": score,
        "findings": findings,
        "required_actions": action,
        "cable_voltage_drop_percent": result_cable["voltage_drop_percent"],
        "power_loss_watts": result_cable["power_loss_watts"],
        "fuse_current_check_a": (min_fuse_a, max_fuse_a),
        "standard_reference": "ABYC E-11 / ISO 10133"
    }


if __name__ == "__main__":
    # Example assessment
    result = assess_electrical_installation(
        system_type="DC_main",
        cable_type="UMS_Tinned_Copper_Marine",
        cross_section_mm2=4.0,
        circuit_length_m=15,
        current_a=30,
        voltage_system=12,
        fuse_rating_a=40,
        connection_type="ring_terminal",
        age_years=2
    )

    print("=" * 70)
    print("ELECTRICAL INSTALLATION ASSESSMENT")
    print("=" * 70)
    print(f"Status: {result['assessment_status']}")
    print(f"Score: {result['score_0_to_100']}/100")
    print(f"\nVoltage Drop: {result['cable_voltage_drop_percent']:.2f}%")
    print(f"Power Loss: {result['power_loss_watts']:.2f}W")
    print(f"\nFindings:")
    for finding in result['findings']:
        print(f"  • {finding}")
    print(f"\nRecommended Action:\n  {result['required_actions']}")
    print(f"\nStandard: {result['standard_reference']}")
    print("=" * 70)
