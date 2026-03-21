"""
AYDI Yacht Sanitär- und Rohrleitungssysteme Knowledge Base
Plumbing and fluid systems for yacht design analysis
Author: Master Marine Plumber KnowledgeBase
Version: 1.0
"""

from typing import Dict, List, Any


PIPE_MATERIALS: Dict[str, Dict[str, Any]] = {
    "PVC": {
        "deutscher_name": "PVC-Rohre",
        "diameter_range_mm": (6, 50),
        "pressure_rating_bar": 10,
        "temperature_range_c": (-5, 40),
        "media_compatibility": ["freshwater", "coolant", "bilge"],
        "joining_methods": ["solvent_cement", "push_fit_connector", "hose_clamp"],
        "standards": ["ISO 1452", "ABYC H-27"],
        "failure_modes": ["UV_degradation_above_deck", "stress_cracking_chlorine", "freeze_burst"],
        "brands": ["Schedule_40_Marine_Grade", "Spears"],
        "notes": "Nicht für Salzwasser oder hohe Temperatur. Hält lange unter Deck."
    },
    "HDPE": {
        "deutscher_name": "Hochdruck-Polyethylen",
        "diameter_range_mm": (10, 63),
        "pressure_rating_bar": 16,
        "temperature_range_c": (-20, 50),
        "media_compatibility": ["freshwater", "fuel", "bilge", "coolant"],
        "joining_methods": ["heat_fusion", "insert_fitting", "compression"],
        "standards": ["ISO 4427", "ABYC H-27"],
        "failure_modes": ["fatigue_at_fittings", "creep_under_pressure", "rodent_gnaw"],
        "brands": ["Fafnir", "Logtis_Marine"],
        "notes": "Flexibel, rutschenproben, für Kälte ideal. Benzinverträglich."
    },
    "PEX": {
        "deutscher_name": "Vernetztes Polyethylen",
        "diameter_range_mm": (6, 28),
        "pressure_rating_bar": 10,
        "temperature_range_c": (-10, 85),
        "media_compatibility": ["freshwater", "hot_water", "heating"],
        "joining_methods": ["crimp_fitting", "push_fit", "compression"],
        "standards": ["ISO 18726", "ABYC H-27"],
        "failure_modes": ["oxidation_above_deck", "UV_breakdown", "compression_nut_loosening"],
        "brands": ["Helicoil_Marine", "Speedfit"],
        "notes": "Beste Flexibilität, ideal für Warmwasser. Muss UV-geschützt sein."
    },
    "Copper": {
        "deutscher_name": "Kupferrohre",
        "diameter_range_mm": (6, 38),
        "pressure_rating_bar": 20,
        "temperature_range_c": (-40, 120),
        "media_compatibility": ["freshwater", "hot_water", "engine_cooling"],
        "joining_methods": ["brazing", "solder", "compression_fitting"],
        "standards": ["ISO 1057", "ASTM B88"],
        "failure_modes": ["dezincification_in_brass_fittings", "corrosion_in_acidic_water", "work_hardening_rupture"],
        "brands": ["Mueller_Streamline", "Viega"],
        "notes": "Klassisch, thermisch leistungsfähig. Dezinkung durch silbergelötet oder Zinn-Zink-Legierungen vermeiden."
    },
    "CuNi_90_10": {
        "deutscher_name": "Kupfer-Nickel Seewasserleitungen",
        "diameter_range_mm": (16, 63),
        "pressure_rating_bar": 25,
        "temperature_range_c": (-20, 60),
        "media_compatibility": ["seawater", "raw_water_cooling"],
        "joining_methods": ["brazing", "TIG_welding", "compression_fitting"],
        "standards": ["ISO 6722", "ASTM B111"],
        "failure_modes": ["impingement_attack_at_elbows", "velocity_erosion_above_2_5_mps", "crevice_corrosion"],
        "brands": ["Outboard_Marine_Grade", "Cupro_Nickel_Suppliers"],
        "notes": "Marine-Standard für Rohwasser. Langsam laufend (<2,5 m/s). Biozidarm nötig."
    },
    "Stainless_316L": {
        "deutscher_name": "Edelstahl 316L Rohre",
        "diameter_range_mm": (6, 50),
        "pressure_rating_bar": 32,
        "temperature_range_c": (-50, 150),
        "media_compatibility": ["seawater", "fuel", "freshwater", "hot_water"],
        "joining_methods": ["welding", "compression_fitting", "o_ring_face_seal"],
        "standards": ["ISO 1312", "NORSOK M-630"],
        "failure_modes": ["pitting_in_chloride_environments", "stress_corrosion_cracking", "crevice_corrosion"],
        "brands": ["AMTROL", "Hydro_Systems"],
        "notes": "Beste Korrosionsbeständigkeit. Teueste Option aber beständig 20+ Jahre."
    },
    "Reinforced_Rubber_Hose": {
        "deutscher_name": "Verstärkte Gummischläuche",
        "diameter_range_mm": (8, 63),
        "pressure_rating_bar": 10,
        "temperature_range_c": (-30, 65),
        "media_compatibility": ["raw_water", "bilge", "engine_cooling", "exhaust_wet"],
        "joining_methods": ["hose_clamp_stainless", "JIC_fitting", "swaged_fitting"],
        "standards": ["ISO 1402", "SAE J20R13"],
        "failure_modes": ["aging_and_cracking", "hose_burst_overpressure", "internal_collapse_vacuum"],
        "brands": ["Jabsco", "Permatex_Hose"],
        "notes": "Vielseitig, günstig. Alle 5-7 Jahre ersetzen (Alterung unter UV)."
    },
    "Sanitation_Hose_Reinforced": {
        "deutscher_name": "Spezial-Fäkalienschläuche",
        "diameter_range_mm": (25, 50),
        "pressure_rating_bar": 0.5,
        "temperature_range_c": (0, 50),
        "media_compatibility": ["blackwater", "sewage"],
        "joining_methods": ["hose_clamp_marine_grade", "hose_barb_fitting"],
        "standards": ["ISO 8099", "MARPOL"],
        "failure_modes": ["permeation_odor_leakage", "splitting_age", "bacterial_biofilm_inside"],
        "brands": ["Taitra", "Groco_Sanitation_Hose", "Trident_Black_Water"],
        "notes": "MUSS ISO 8099 sein! Laminat-Barrierschicht gegen Permeation. Alt = Gestank!"
    }
}


HOSE_TYPES: Dict[str, Dict[str, Any]] = {
    "Raw_Water_Cooling": {
        "deutscher_name": "Rohwasser-Kühlerschläuche",
        "construction_layers": ["inner_EPDM", "textile_reinforcement", "outer_synthetic_rubber"],
        "temperature_max_c": 60,
        "pressure_max_bar": 2.5,
        "media_compatibility": ["seawater", "brackish_water"],
        "clamp_requirements": "double_stainless_steel_hose_clamp",
        "diameter_mm": [16, 19, 25, 32, 38, 50],
        "brands": ["Goodyear_Marine", "Parker_Marine", "Jabsco"],
        "replacement_interval_years": 7,
        "notes": "Muss alle 7 Jahre inspiziert werden wegen Alterung. Druckseite kritisch."
    },
    "Exhaust_Wet_Hose": {
        "deutscher_name": "Nass-Auspuffschläuche",
        "construction_layers": ["silicone_inner", "steel_wire_reinforcement", "silicone_outer"],
        "temperature_max_c": 120,
        "pressure_max_bar": 3.0,
        "media_compatibility": ["hot_exhaust_water_mix"],
        "clamp_requirements": "double_stainless_hose_clamp_high_temp",
        "diameter_mm": [25, 32, 38, 50],
        "brands": ["Permatex", "Trident", "Bisco"],
        "replacement_interval_years": 5,
        "notes": "Silikon-Kern für Hitze. Thermische Ausdehnung kalkulieren!"
    },
    "Fuel_Line_Marine": {
        "deutscher_name": "Benzin-/Dieselschläuche",
        "construction_layers": ["ethylene_propylene_inner", "textile_braid", "nitrile_outer"],
        "temperature_max_c": 50,
        "pressure_max_bar": 3.4,
        "media_compatibility": ["gasoline", "diesel", "biodiesel_up_to_10pct"],
        "clamp_requirements": "double_stainless_fuel_hose_clamp",
        "diameter_mm": [6, 8, 10, 13, 16],
        "brands": ["Teleflex", "Volvo_Penta", "Sherwood_Fuel_Hose"],
        "replacement_interval_years": 10,
        "standards": ["ABYC_H-24", "ISO_8469"],
        "notes": "Fungizidbelasteter Diesel > jährliche Filterung nötig. Keine PVC!"
    },
    "Sanitation_Hose": {
        "deutscher_name": "Fäkalienschläuche",
        "construction_layers": ["nylon_barrier_film", "rubber_middle", "nylon_outer"],
        "temperature_max_c": 45,
        "pressure_max_bar": 0.8,
        "media_compatibility": ["blackwater", "sewage"],
        "clamp_requirements": "stainless_marine_grade_full_turn",
        "diameter_mm": [25, 32, 38, 50],
        "brands": ["Taitra_Sanitaire", "Raritan_Sanitation_Hose", "Groco"],
        "replacement_interval_years": 8,
        "standards": ["ISO_8099"],
        "notes": "Permeations-Test kritisch! Laminat muss intakt sein sonst Geruchentwicklung."
    },
    "Bilge_Suction": {
        "deutscher_name": "Bilgenwassr-Saugschläuche",
        "construction_layers": ["smooth_nitrile_inner", "wire_spiral", "synthetic_rubber"],
        "temperature_max_c": 50,
        "pressure_max_bar": -0.9,
        "media_compatibility": ["bilge_water", "oily_water"],
        "clamp_requirements": "double_stainless_clamp_minimum",
        "diameter_mm": [25, 32, 38, 50],
        "brands": ["Trident_Bilge", "Flexfab"],
        "replacement_interval_years": 6,
        "notes": "Spirale gegen Vakuumkollaps. Innenoberfläche glatt (Verschlammung minimieren)."
    },
    "Freshwater_Pressure": {
        "deutscher_name": "Frischwasser-Druckschläuche",
        "construction_layers": ["NSF_inner", "polyester_braid", "synthetic_rubber"],
        "temperature_max_c": 65,
        "pressure_max_bar": 4.0,
        "media_compatibility": ["freshwater", "hot_freshwater"],
        "clamp_requirements": "single_stainless_hose_clamp_sufficient",
        "diameter_mm": [6, 8, 10, 13, 16, 19],
        "brands": ["SharkBite_Marine", "Goodyear_Potable"],
        "replacement_interval_years": 8,
        "standards": ["NSF_61", "ABYC_H-27"],
        "notes": "NSF 61 für Trinkwasser kritisch! FDA-Zertifikat prüfen."
    },
    "Deckwash": {
        "deutscher_name": "Deckwaschen-Schläuche",
        "construction_layers": ["EPDM_inner", "synthetic_fiber_braid", "cover"],
        "temperature_max_c": 50,
        "pressure_max_bar": 10.0,
        "media_compatibility": ["freshwater", "saltwater"],
        "clamp_requirements": "stainless_clamp_two_recommended",
        "diameter_mm": [13, 16, 19, 25],
        "brands": ["Jabsco", "Gardena_Marine_Connector"],
        "replacement_interval_years": 7,
        "notes": "Oft in Sonne > UV-Schutz oder Schlauchkanal! Hochdruck."
    },
    "LPG_Propane_Tubing": {
        "deutscher_name": "Propan-Gaszuleitungen",
        "construction_layers": ["seamless_copper", "or_stainless_braid"],
        "temperature_max_c": 50,
        "pressure_max_bar": 2.0,
        "media_compatibility": ["propane", "butane"],
        "clamp_requirements": "none_rigid_tubing_with_compression_fitting",
        "diameter_mm": [3.2, 4.8, 6.4, 9.5],
        "brands": ["Coppergas_Marine", "Stainless_Marine_Fittings"],
        "replacement_interval_years": 10,
        "standards": ["ISO_10239", "EN_15609"],
        "notes": "Kupfer oder V4A Edelstahl. Gummigas-Schlauch verboten (Permeation)!"
    }
}


SEACOCKS_AND_VALVES: Dict[str, Dict[str, Any]] = {
    "Bronze_Seacock": {
        "deutscher_name": "Bronze Seeventil",
        "material": "Cast_Bronze_Gunmetal",
        "pressure_rating_bar": 2.5,
        "temperature_range_c": (-20, 50),
        "connection_type": "hose_barb_and_flanged",
        "maintenance_interval_months": 12,
        "failure_modes": ["dezincification_of_brass_components", "internal_corrosion_pitting", "handle_seizing"],
        "installation_rules": "below_waterline_only_with_tapered_wood_plug",
        "standards": ["ISO_9093", "ABYC_E-8"],
        "brands": ["Groco", "Perko", "Forespar"],
        "notes": "Klassiker, langlebig >15 Jahre. Handle regelmäßig dreißen (nicht einfaul werden lassen)."
    },
    "Composite_Marelon_Seacock": {
        "deutscher_name": "Kunststoff Seeventil (Marelon)",
        "material": "Reinforced_Nylon_Composite",
        "pressure_rating_bar": 1.7,
        "temperature_range_c": (-10, 40),
        "connection_type": "hose_barb_and_flanged",
        "maintenance_interval_months": 24,
        "failure_modes": ["stress_cracking_over_tightening", "UV_degradation_exterior", "internal_galvanic_current_when_bronze_nearby"],
        "installation_rules": "below_waterline_above_waterline_acceptable",
        "standards": ["ABYC_E-8"],
        "brands": ["Forespar_Marelon", "Groco_Plastic_Series"],
        "notes": "Leichter, kostengünstiger, aber < Druck als Bronze. Gutes Preis/Leistungs-Verhältnis."
    },
    "Ball_Valve_Stainless": {
        "deutscher_name": "Kugelhahn Edelstahl",
        "material": "Stainless_316L_Body",
        "pressure_rating_bar": 20.0,
        "temperature_range_c": (-20, 100),
        "connection_type": "threaded_or_flanged",
        "maintenance_interval_months": 24,
        "failure_modes": ["handle_breakage_plastic_handle", "internal_deposit_scaling", "seal_degradation_high_temp"],
        "installation_rules": "above_waterline_general_isolation",
        "standards": ["ISO_17292"],
        "brands": ["Hydro_Systems", "Viega", "Belimo"],
        "notes": "Vielseitiger Absperrhahn. Höchste Zuverlässigkeit. Vollevollwertiger Ersatz für Seeventile nicht geeignet."
    },
    "Gate_Valve_Brass": {
        "deutscher_name": "Schieberventil",
        "material": "Brass_Body_Bronze_Internal",
        "pressure_rating_bar": 10.0,
        "temperature_range_c": (-10, 65),
        "connection_type": "threaded",
        "maintenance_interval_months": 36,
        "failure_modes": ["stem_seizing", "internal_corrosion", "wedging_particles"],
        "installation_rules": "above_waterline_isolation",
        "standards": ["ISO_1211"],
        "brands": ["Mueller", "Nibco"],
        "notes": "Langsam betätigen (Wasserschlag vermeiden). Weniger zuverlässig als Kugelhahn."
    },
    "Check_Valve_Bronze": {
        "deutscher_name": "Rückschlagventil",
        "material": "Bronze_Gunmetal_Spring",
        "pressure_rating_bar": 4.0,
        "temperature_range_c": (-20, 60),
        "connection_type": "hose_barb_or_threaded",
        "maintenance_interval_months": 24,
        "failure_modes": ["spring_corrosion", "internal_particle_jamming", "flapper_sticking"],
        "installation_rules": "raw_water_bilge_freshwater_outlet_lines",
        "standards": ["ISO_27541"],
        "brands": ["Groco", "Flojet"],
        "notes": "Schutz gegen Rückfluss (besonders Seewasser-Rücksog bei Motor aus). Regelmäßig betätigen."
    },
    "Y_Valve_Sanitation": {
        "deutscher_name": "Y-Ventil für Toilette (3-Weg)",
        "material": "Brass_or_Bronze",
        "pressure_rating_bar": 0.8,
        "temperature_range_c": (0, 45),
        "connection_type": "hose_barb",
        "maintenance_interval_months": 12,
        "failure_modes": ["seal_degradation", "handle_corrosion", "internal_blockage_sewage"],
        "installation_rules": "between_toilet_and_holding_tank",
        "standards": ["ISO_8099"],
        "brands": ["Raritan", "Groco", "Osculati"],
        "notes": "Ermöglicht Umschaltung Seewasser/Holding-Tank. Dichtsitze sind kritisch (leckt leicht)."
    },
    "Pressure_Relief_Valve": {
        "deutscher_name": "Überdruckventil",
        "material": "Stainless_or_Bronze",
        "pressure_rating_bar": "adjustable_0_5_to_5",
        "temperature_range_c": (-10, 80),
        "connection_type": "threaded",
        "maintenance_interval_months": 12,
        "failure_modes": ["spring_fatigue", "seat_erosion_hammering", "adjustment_drift"],
        "installation_rules": "freshwater_system_after_accumulator",
        "standards": ["ISO_4413"],
        "brands": ["Flojet", "Jabsco"],
        "notes": "Schützt Druckanlage vor Über-Überdruck (z.B. bei Sonneneinstrahlung Speicher)."
    },
    "Anti_Siphon_Valve": {
        "deutscher_name": "Anti-Siphon-Ventil",
        "material": "Brass_Reinforced",
        "pressure_rating_bar": 1.0,
        "temperature_range_c": (5, 50),
        "connection_type": "threaded_intake",
        "maintenance_interval_months": 36,
        "failure_modes": ["internal_blockage", "spring_corrosion", "seal_failure"],
        "installation_rules": "fuel_tank_or_holding_tank_vent",
        "standards": ["ABYC_H-24"],
        "brands": ["Groco", "Forespar"],
        "notes": "Verhindert Tankentleerung durch Siphoning, wenn Schlauch bricht. Kritisch für Sicherheit!"
    }
}


PUMPS: Dict[str, Dict[str, Any]] = {
    "Bilge_Pump_Manual": {
        "deutscher_name": "Handbilgepumpe",
        "flow_rate_lpm": 15,
        "pressure_bar": 0.5,
        "power_w": 0,
        "priming": "self_priming",
        "maintenance": ["check_flapper_valve_annually", "test_monthly", "replace_seals_5_years"],
        "brands": ["Pompanella", "Flojet_Hand_Bilge"],
        "installation": "cockpit_or_cabin_accessible",
        "notes": "Notfallanlage. Alle sollten bedienbar sein. Nach Havarie sofort prüfen!"
    },
    "Bilge_Pump_Electric_Submersible": {
        "deutscher_name": "Tauch-Elektrobilgepumpe",
        "flow_rate_lpm": 40,
        "pressure_bar": 0.3,
        "power_w": 600,
        "priming": "submersible_no_priming",
        "maintenance": ["check_float_switch_monthly", "test_monthly", "impeller_replacement_2_years"],
        "brands": ["Rule_2000", "Jabsco_Cartridge_Bilge", "Johnson_F5B-24"],
        "installation": "direct_sump_mounted",
        "notes": "Standard moderner Yachten. Float-Schalter oft ausfallend > manueller Überschreibung nötig."
    },
    "Bilge_Pump_High_Capacity": {
        "deutscher_name": "Hochleistungs-Bilgepumpe",
        "flow_rate_lpm": 100,
        "pressure_bar": 1.0,
        "power_w": 1200,
        "priming": "self_priming_with_prime_pump",
        "maintenance": ["impeller_replacement_annually", "pressure_relief_valve_check", "line_flush_monthly"],
        "brands": ["March_AC", "Flojet_Pump_Centrifugal"],
        "installation": "external_pumped_to_through_hull_or_deck",
        "notes": "Großsegler oder Notfall-Setup. Zentrifugalpumpen benötigen Ansauganlage mit Primer."
    },
    "Freshwater_Pressure_Pump": {
        "deutscher_name": "Frischwasser-Druckpumpe",
        "flow_rate_lpm": 20,
        "pressure_bar": 3.5,
        "power_w": 500,
        "priming": "self_priming",
        "maintenance": ["pressure_switch_adjustment_biennial", "accumulator_tank_precharge_annually", "impeller_3_years"],
        "brands": ["Jabsco_Water_Puppy", "Flojet_Automatik", "Shurflo_High_Pressure"],
        "installation": "tank_mounted_or_inline",
        "notes": "Automatisch (Druckschalter). Druckkessel (Akkumulator) reduziiert Startzyklen (Motor-Verschleiß)."
    },
    "Macerator_Pump": {
        "deutscher_name": "Zerhacker-Pumpe",
        "flow_rate_lpm": 15,
        "pressure_bar": 2.5,
        "power_w": 800,
        "priming": "self_priming",
        "maintenance": ["blade_sharpness_check_6_months", "fine_mesh_screen_cleaning", "electric_motor_bearing_annually"],
        "brands": ["Raritan_Electroscan", "Groco_Macerator"],
        "installation": "holding_tank_outlet_high_position",
        "notes": "Zerkleiner Fäkalien für Überboard-Pumping oder Pumpentoilette. Rostige Blätter = Verlust Förderung."
    },
    "Deckwash_Pump": {
        "deutscher_name": "Deckwaschen-Pumpe",
        "flow_rate_lpm": 60,
        "pressure_bar": 4.0,
        "power_w": 1100,
        "priming": "not_self_priming_foot_valve_required",
        "maintenance": ["foot_valve_screen_monthly", "seal_pack_replacement_2_years", "impeller_3_years"],
        "brands": ["Johnson_Pump_Deckwash", "Flojet_Deckwascher"],
        "installation": "deck_outlet_manifold_with_multiple_hose_connections",
        "notes": "Große Durchsätze möglich. Foot-Ventil vor Ansaugung unverzichtbar (Selbstansaugung sonst fehlgeschlagen)."
    },
    "Raw_Water_Impeller_Pump": {
        "deutscher_name": "Rohwasser-Kreiselpumpe (Impeller)",
        "flow_rate_lpm": 80,
        "pressure_bar": 0.4,
        "power_w": 750,
        "priming": "must_be_self_priming",
        "maintenance": ["impeller_replacement_annually", "housing_gasket_biennial", "screen_clean_monthly"],
        "brands": ["Sherwood_Impeller", "Jabsco_Impeller_Pump"],
        "installation": "engine_inlet_manifold_or_standalone_cooling_loop",
        "notes": "Impeller-Pumpen sind empfindlich. Sandpartikel = Verschleiß. Immer Sieb verwenden!"
    },
    "Centrifugal_Pump": {
        "deutscher_name": "Zentrifugal-Pumpe",
        "flow_rate_lpm": 150,
        "pressure_bar": 1.5,
        "power_w": 1500,
        "priming": "requires_priming_reservoir_or_pump",
        "maintenance": ["mechanical_seal_annually", "bearing_lubrication_biennial", "turbine_wear_ring_3_years"],
        "brands": ["March_AC_Magnetic_Drive", "Flojet_Centrifugal"],
        "installation": "external_line_priming_foot_valve",
        "notes": "Beste für große Durchsätze / Abwasser. Aber Ansauganlage notwendig (Priming-Tank)."
    },
    "Diaphragm_Pump_Manual": {
        "deutscher_name": "Membran-Handpumpe",
        "flow_rate_lpm": 8,
        "pressure_bar": 2.0,
        "power_w": 0,
        "priming": "self_priming",
        "maintenance": ["diaphragm_replacement_3_years", "check_valve_flapper_annually"],
        "brands": ["Whale_Gusher_Galley", "ITT_Flojet_Manual"],
        "installation": "galley_or_emergency_water_supply",
        "notes": "Klassisch für Schiff-Galerien. Langlebig > 10 Jahre mit Wartung."
    },
    "WC_Hand_Pump": {
        "deutscher_name": "Toiletten-Handpumpe",
        "flow_rate_lpm": 5,
        "pressure_bar": 0.3,
        "power_w": 0,
        "priming": "not_required_water_seated_in_bowl",
        "maintenance": ["flapper_valve_check_annually", "rod_corrosion_inspection", "full_unit_replacement_10_years"],
        "brands": ["Raritan_Manual_WC", "Groco_Piston_Pump"],
        "installation": "integrated_into_toilet_bowl_base",
        "notes": "Zuverlässig. Verstopfung häufig bei schlechter Wartung (Kalkablagerung)."
    }
}


FRESHWATER_SYSTEM: Dict[str, Any] = {
    "tank_materials": {
        "Polyethylen_Food_Grade": {
            "capacity_liters": [50, 100, 150, 200, 300, 500],
            "lifespan_years": 20,
            "temperature_max_c": 50,
            "brands": ["Freudenberg", "Plastex_Marine"],
            "notes": "Standard. FDA-gekennzeichnet für Trinkwasser. UV-Schutz erforderlich."
        },
        "Stainless_Steel_304_or_316": {
            "capacity_liters": [100, 200, 300, 500, 1000],
            "lifespan_years": 25,
            "temperature_max_c": 80,
            "brands": ["Freudenberg_Stainless", "AMTROL"],
            "notes": "Höchste Hygiene, aber teuer. Schweißnähte müssen passiviert sein."
        },
        "Aluminum_with_Epoxy_Liner": {
            "capacity_liters": [200, 300, 500, 1000],
            "lifespan_years": 15,
            "temperature_max_c": 50,
            "brands": ["Empiris", "Aqua_Tank"],
            "notes": "Leicht, korrosionsbeständig wenn Beschichtung intakt. Langsameres Altern als PE."
        }
    },
    "watermaker_desalination": {
        "reverse_osmosis_marine": {
            "flow_rate_lph": [100, 200, 400],
            "power_consumption_w": [800, 1200, 1800],
            "recovery_rate_pct": 50,
            "salinity_output_ppm": "< 50",
            "brands": ["HyDra_Aqua", "Sea_Recovery", "Force_10"],
            "maintenance": ["pre_filter_cartridge_3_months", "membrane_replacement_3_to_5_years"],
            "notes": "Druck 55-60 bar erforderlich. Hochdruckpumpe mit Motor oder PTO-Antrieb."
        }
    },
    "uv_sterilizer": {
        "ultraviolet_lamp_system": {
            "flow_rate_lph": [100, 200],
            "power_w": [20, 40],
            "lamp_replacement_months": 12,
            "brands": ["Sterilite", "UV_Purification_Marine"],
            "application": "final_stage_after_filters",
            "notes": "Nicht gegen Salz wirksam (nur photosynthetic_bacteria). Nach RO optional."
        }
    },
    "filters": {
        "sediment_pre_filter": {
            "micron_rating": "20_to_100_micron",
            "cartridge_replacement_months": 3,
            "brands": ["Pentek", "Aqua_Pure"],
            "installation": "tank_outlet_before_all_other_systems"
        },
        "activated_carbon_filter": {
            "micron_rating": "5_micron",
            "cartridge_replacement_months": 6,
            "brands": ["Aqua_Pure_Taste", "Omnipure"],
            "removes": ["chlorine", "taste", "odor", "pesticides"]
        }
    },
    "accumulator_tank": {
        "volume_liters": [2, 5, 10, 20],
        "type": "bladder_accumulator",
        "precharge_bar": "usually_0_7x_pump_pressure",
        "brands": ["Amtrol", "Zilmet"],
        "function": "dampen_pump_cycling_reduce_motor_starts",
        "maintenance": ["precharge_check_annually", "gas_valve_inspection_3_years"]
    },
    "hot_water_system": {
        "engine_heat_exchanger": {
            "capacity_liters": [10, 20, 30],
            "material": "stainless_or_copper_brazed",
            "brands": ["Isotemp", "Nibe"],
            "function": "waste_heat_from_engine_cooling_loop"
        },
        "electric_heater": {
            "power_w": [2000, 3000, 4000],
            "voltage": "12V_or_24V_DC_or_110_220V_AC",
            "thermostat_setpoint_c": [40, 45, 50],
            "brands": ["Isotemp", "Xylem_Quick"],
            "installation": "inline_or_tank_immersion"
        },
        "instant_gas_heater": {
            "power_kw": [6, 8, 10],
            "fuel": "LPG",
            "brands": ["Force_10", "Webasto"],
            "advantage": "space_saving_rapid_hot_water"
        }
    },
    "sizing_by_boat_class": {
        "cruiser_30_40ft": "tank_150_200L, pump_15lpm, heater_2kW",
        "cruiser_40_50ft": "tank_250_400L, pump_20lpm, heater_3kW",
        "offshore_50_60ft": "tank_400_600L, pump_25lpm, heater_4kW_plus_engine_exchanger",
        "guidelines": "min_10L_per_person_per_day_consumption"
    },
    "winterization_freshwater": {
        "steps": [
            "turn_off_water_heater",
            "drain_all_tanks_completely",
            "drain_pump_lines_and_pressure_vessel",
            "add_RV_antifreeze_propylene_glycol_food_grade_to_system",
            "run_pump_until_pink_liquid_at_all_faucets",
            "cap_all_through_hulls_and_deck_drains",
            "store_tanks_dry_or_filled_with_stabilized_water"
        ],
        "antifreeze_type": "propylene_glycol_NOT_ethylene_glycol",
        "drain_points": ["lowest_cabin_faucet", "galley_sink", "head_washbasin", "shower", "holding_tank_pump"]
    }
}


SANITATION_SYSTEM: Dict[str, Any] = {
    "manual_wc": {
        "deutscher_name": "Handtoilette",
        "flushing_mechanism": "manual_pump",
        "water_per_flush_liters": 2,
        "brands": ["Raritan_Compact", "Groco_Manual_WC"],
        "advantages": ["simple", "reliable", "no_electric_power", "user_aware_of_usage"],
        "disadvantages": ["labor_intensive", "user_dependent_quality"],
        "maintenance": ["annual_pump_seal_inspection", "corrosion_protection_zinc"]
    },
    "electric_wc": {
        "deutscher_name": "Elektrische Toilette",
        "flushing_mechanism": "electric_pump_12V_24V_or_110_220V_AC",
        "water_per_flush_liters": 1.5,
        "brands": ["Raritan_Electra", "Groco_Deluxe_Electric"],
        "power_consumption_w": [150, 300],
        "advantages": ["ease_of_use", "low_water_consumption"],
        "disadvantages": ["electric_power_required", "more_complex_plumbing"],
        "maintenance": ["seal_pack_annually", "flapper_inspection"]
    },
    "vacuum_wc": {
        "deutscher_name": "Vakuum-Toilette",
        "flushing_mechanism": "vacuum_line_low_pressure",
        "water_per_flush_liters": 0.5,
        "brands": ["Electrolux_Aqualux", "VacuFlush"],
        "power_consumption_w": [600],
        "advantages": ["very_low_water_consumption", "compact_design"],
        "disadvantages": ["complex_service", "expensive", "vacuum_pump_reliability"],
        "maintenance": ["vacuum_pump_seal_annually", "line_deodorizing_biannual"]
    },
    "holding_tank": {
        "volume_sizing_rule": "3_to_7_days_offshore_or_7_to_14_days_cruising",
        "materials": ["polyethylene_food_grade", "stainless_steel", "fiberglass"],
        "capacity_liters": [50, 100, 150, 200, 300],
        "brands": ["Raritan_Flexflo", "Groco_Holding_Tank"],
        "pumpout_connection": "deck_through_hull_with_cap",
        "vent_requirements": "carbon_filter_vent_to_prevent_odor",
        "monitoring": ["level_gauge_manual_sight_glass", "electrical_level_sensor"],
        "notes": "Größter Übelgeruchs-Falle am Schiff. Lüftung und Dichtheit kritisch!"
    },
    "y_valve_toilet": {
        "function": "selectable_seawater_flushing_or_holding_tank_discharge",
        "material": "brass_or_bronze",
        "brands": ["Raritan", "Groco"],
        "installation": "between_toilet_and_sea_thru_hull",
        "maintenance": ["handle_actuation_monthly", "seal_inspection_annually"],
        "notes": "Ermöglicht Flexibilität. Aber Dichtheit ist kritisch (Lecks häufig)."
    },
    "macerator_sewage": {
        "function": "finely_chop_solids_for_overboard_discharge",
        "brands": ["Raritan_Electroscan", "Groco_Macerator"],
        "power_consumption_w": [800, 1000],
        "maintenance": ["blade_wear_inspection_6_months", "motor_bearing_annually"],
        "pressure_output_bar": 2.5,
        "notes": "Nur in Küstenwasser oder mit Genehmigung > weite Seereisen benötigen Holding-Tank."
    },
    "deck_pumpout_fitting": {
        "standard": "ISO_8099_compliant_deck_plate",
        "material": "stainless_or_bronze",
        "mounting": "accessible_location_not_over_teak_or_cabin",
        "brands": ["Groco", "Forespar"],
        "cap": "stainless_steel_hinged_with_lanyard",
        "notes": "Muss schnell und sauber austauschbar sein (kein Herum-Tropfen)."
    },
    "blackwater_treatment": {
        "electroscan_additive": {
            "product": "Raritan_Electroscan_NE_Tablets",
            "function": "deodorizing_and_bacteria_suppression",
            "frequency": "weekly_or_per_manual"
        },
        "enzyme_treatment": {
            "product": "biological_enzyme_additive",
            "function": "natural_decomposition",
            "frequency": "weekly"
        }
    },
    "standards_regulations": {
        "ISO_8099": "Sanitation_Hose_Permeation_Testing",
        "MARPOL": "International_Maritime_Pollution_Convention",
        "no_discharge_zones": "restricted_areas_must_use_holding_tank"
    },
    "hose_permeation_problem": {
        "description": "Old_sanitation_hose_develops_odor_from_bacteria_through_aging_hose_walls",
        "solution": "Replace_hose_every_8_to_10_years_minimum",
        "brands_with_barrier_layer": ["Taitra_with_Nylon_Barrier", "Trident_Sanitation"],
        "test_method": "Immerse_hose_in_methylene_chloride_check_for_seepage"
    }
}


FUEL_SYSTEM: Dict[str, Any] = {
    "tank_materials": {
        "aluminum_marine_grade": {
            "capacity_liters": [100, 200, 300, 500],
            "lifespan_years": 20,
            "temperature_max_c": 50,
            "brands": ["Empiris", "Freudenberg_Aluminum"],
            "notes": "Standard. Muss innen passiviert sein (Korrosion vermeiden)."
        },
        "stainless_steel_304_316": {
            "capacity_liters": [100, 200, 300, 500],
            "lifespan_years": 25,
            "temperature_max_c": 60,
            "brands": ["AMTROL", "Empiris_Stainless"],
            "notes": "Beste Option. Schweißqualität kritisch."
        },
        "polyethylene_diesel_rated": {
            "capacity_liters": [50, 100, 150],
            "lifespan_years": 15,
            "temperature_max_c": 50,
            "brands": ["Nauta_Plastics"],
            "notes": "Nur Diesel, nicht Benzin! Fungizid-resistent Typ."
        }
    },
    "fuel_lines": {
        "material": "ABYC_H-24_compliant_hose",
        "diameter_mm": [6, 8, 10, 13, 16],
        "pressure_rating_bar": 3.4,
        "temperature_max_c": 50,
        "brands": ["Teleflex_Marine_Fuel", "Volvo_Penta_Fuel_Hose"],
        "joining": "hose_clamp_double_stainless",
        "inspection_interval_months": 12,
        "notes": "Keine PVC! Benzin zersetzt PVC. Doppel-Schellenbands für Sicherheit."
    },
    "fuel_filter": {
        "racor_water_separator": {
            "flow_capacity_lph": [100, 200, 300],
            "brands": ["Racor_500FG", "Racor_1000FG"],
            "maintenance": ["water_drain_valve_monthly", "cartridge_replacement_annually"],
            "function": "Catches_free_water_and_sediment",
            "notes": "Kritisch für Diesel! Wasser = Korrosion, Mikroben, Startprobleme."
        }
    },
    "fuel_deck_fills": {
        "material": "stainless_or_bronze",
        "cap": "stainless_hinged_self_closing",
        "strainer_screen": "100_micron_mesh",
        "brands": ["Groco", "Forespar"],
        "installation": "easily_accessible_away_from_cabin",
        "notes": "Muss tropffrei sein. Stabil gegen Verschmutzung."
    },
    "fuel_vents": {
        "vent_material": "stainless_loop_or_carbon_filter_vent",
        "brands": ["Forespar_Fuel_Vent", "Groco_Vent_Loop"],
        "function": "prevents_tank_vacuum_during_fuel_draw",
        "antibackflow": "check_valve_built_in",
        "notes": "Vent-Schleifen verhindern Luftsack. Schlauch muss über Rumpfspitze austreten (Kein Rückfluss bei Wellenschlag)."
    },
    "fuel_shutoff_valve": {
        "type": "ball_valve_stainless",
        "installation": "tank_outlet_below_tank_level",
        "pressure_rating_bar": 3.4,
        "brands": ["Groco", "Viega"],
        "function": "emergency_fuel_isolation",
        "operation": "accessible_from_cockpit_preferred"
    },
    "anti_siphon_valve": {
        "requirement": "ABYC_H-24_mandatory",
        "location": "fuel_tank_vent_or_deck_fill",
        "material": "brass_reinforced",
        "function": "prevents_tank_emptying_if_hose_ruptures",
        "brands": ["Groco", "Forespar"],
        "notes": "Kritisch für Sicherheit! Schlauch-Risse führen zu Brandgefahr wenn kein Anti-Siphon."
    },
    "standards_regulations": {
        "ABYC_H-24": "Fuel_System_Installation",
        "ISO_10088": "Onboard_Fuel_Systems",
        "fire_safety": "All_components_rated_for_fuel_service"
    },
    "fungal_contamination_diesel": {
        "problem": "Microbial_growth_in_diesel_tanks_causes_filter_clogging_and_corrosion",
        "prevention": ["keep_tank_topped_up_minimize_condensation", "fuel_polishing_service_annually"],
        "treatment": ["diesel_biocide_additive_Biobor_JF", "professional_tank_cleaning"],
        "notes": "Häufiges Problem in tropischen Klimazonen und älteren Schiffen."
    }
}


GAS_SYSTEM_LPG: Dict[str, Any] = {
    "propane_storage": {
        "tank_material": "stainless_steel_316L",
        "capacity_kg": [2, 5, 10, 20, 30],
        "brands": ["Worthington", "Manchester"],
        "locker_requirements": "ventilated_overboard_drain_no_bilge_water_pooling",
        "locker_size_minimum": "volume_3x_tank_volume",
        "drain_orifice_diameter_mm": 3,
        "installation_rules": [
            "above_waterline",
            "fully_ventilated_at_deck_level",
            "dedicated_through_hull_drain",
            "lightning_protection",
            "no_ignition_sources_nearby"
        ]
    },
    "solenoid_valve": {
        "function": "automatic_fuel_shutoff_when_stove_or_heater_off",
        "voltage": ["12V_DC", "24V_DC"],
        "brands": ["Honeywell_Solenoid", "Emerson"],
        "installation": "tank_outlet_before_regulator",
        "safety_feature": "failsafe_springs_to_closed_position",
        "maintenance": ["coil_inspection_annually"]
    },
    "regulator": {
        "type": "two_stage_marine_grade",
        "first_stage": "high_pressure_to_intermediate",
        "second_stage": "intermediate_to_final_pressure",
        "outlet_pressure_bar": 0.025,
        "brands": ["Cavagna_Marine", "Victaulic"],
        "installation": "shortly_downstream_of_tank"
    },
    "tubing": {
        "material_option_1": "seamless_copper_tubing",
        "material_option_2": "stainless_steel_braid_tube",
        "diameter_mm": [3.2, 4.8, 6.4, 9.5],
        "pressure_rating_bar": 20,
        "standards": ["ISO_10239", "EN_15609"],
        "bending_radius_minimum": "10x_tube_outer_diameter",
        "joinery": "compression_fitting_or_flared_fitting",
        "brands": ["Coppergas", "Stainless_Marine_Fittings"],
        "notes": "Gummigas-Schläuche verboten! Bleibt unzulässig durch Permeation."
    },
    "connections_and_joints": {
        "flared_fitting": "double_flare_brass_on_copper",
        "compression_fitting": "olive_and_ferrule_stainless",
        "standards": ["ISO_6149", "ISO_10239"],
        "torque_spec_nm": "follow_equipment_manual",
        "brands": ["Swagelok", "Hydraflow"],
        "inspection": "annual_tightness_check_with_soapy_water"
    },
    "leak_detection": {
        "test_method_1": "soapy_water_bubble_test_at_all_joints",
        "test_method_2": "electronic_gas_detector_portable",
        "test_frequency": "before_season_and_after_modifications",
        "brands": ["BW_Technologies_GasAlert", "Dräger_Polytron"],
        "notes": "Niemals Feuer verwenden! Seifen-Lösung überall auftragen."
    },
    "installation_rules": {
        "tank_locker": "ventilated_gas_locker_overboard_drain",
        "solenoid_valve": "tank_isolation_automatic",
        "service_valve": "manual_shutoff_accessible",
        "pressure_relief": "tank_fitted_with_relief_valve",
        "electrical": "shore_power_disconnect_if_LPG_detected",
        "warning_labels": "flame_and_pressure_danger_in_multiple_languages"
    },
    "standards_regulations": {
        "ISO_10239": "LPG_Onboard_Installation",
        "EN_15609": "Gas_Appliance_Installation",
        "LPG_Code_Germany": "DVGW_G600_Technical_Rules"
    }
}


THROUGH_HULL_SCHEDULE: Dict[str, Any] = {
    "yacht_35ft_cruiser": {
        "total_through_hulls": 12,
        "below_waterline": [
            {"name": "raw_water_cooling_inlet", "diameter_mm": 25, "material": "bronze_seacock"},
            {"name": "raw_water_cooling_outlet", "diameter_mm": 32, "material": "bronze_seacock"},
            {"name": "bilge_suction", "diameter_mm": 25, "material": "bronze_seacock"},
            {"name": "toilet_inlet_Y_valve", "diameter_mm": 19, "material": "bronze_seacock"},
            {"name": "toilet_overboard_discharge_macerator", "diameter_mm": 32, "material": "bronze_seacock"},
            {"name": "speedlog_transducer", "diameter_mm": 13, "material": "bronze_fitting"}
        ],
        "above_waterline": [
            {"name": "freshwater_pressure_outlet", "diameter_mm": 16, "material": "stainless_deck_plate"},
            {"name": "deckwash_inlet", "diameter_mm": 19, "material": "stainless_deck_plate"},
            {"name": "fuel_deck_fill", "diameter_mm": 35, "material": "stainless_with_cap"},
            {"name": "holding_tank_pumpout", "diameter_mm": 38, "material": "stainless_with_cap"},
            {"name": "exhaust_hose_exit", "diameter_mm": 38, "material": "marine_plastic"},
            {"name": "ventilation_through_hull", "diameter_mm": 75, "material": "stainless_louvre"}
        ]
    },
    "general_rules": {
        "below_waterline": "all_fitted_with_seacocks_and_tapered_wooden_emergency_plugs",
        "above_waterline": "deck_plates_or_flanges_with_hinged_caps",
        "emergency_plug_location": "visibly_marked_near_each_through_hull",
        "plug_diameter_mm": "one_size_up_from_through_hull",
        "material_plug": "tapered_wooden_dowel_with_lanyard"
    },
    "installation_standards": {
        "ISO_9093": "Seacock_Standards",
        "ABYC_E_8": "Through_Hull_Fittings",
        "BVQtry": "Bureau_Veritas_Classed_Requirements"
    }
}


WINTERIZATION_PROCEDURES: Dict[str, Any] = {
    "freshwater_system_winter": {
        "steps": [
            "Isolate_water_heater_via_valve",
            "Drain_all_tanks_and_lines_completely",
            "Add_RV_antifreeze_propylene_glycol_food_grade_minimum_2_percent_concentration",
            "Run_pump_until_pink_liquid_at_all_outlets",
            "Leave_system_pressurized_with_antifreeze",
            "Drain_and_refill_holding_tank_or_leave_empty",
            "Close_seacocks"
        ],
        "antifreeze_type": "propylene_glycol_NOT_ethylene_glycol_toxic",
        "temperature_protection_c": -20,
        "brands": ["Flojet_RV_Antifreeze", "Thetford_Marine_Antifreeze"]
    },
    "engine_cooling_system": {
        "preparation": [
            "Check_antifreeze_concentration_with_hydrometer",
            "Top_up_coolant_to_spec",
            "Run_engine_until_warm_to_distribute",
            "Install_frost_plugs_if_engine_has_block_drains"
        ],
        "coolant_type": "marine_blue_antifreeze_with_corrosion_inhibitors",
        "brands": ["Volvo_Penta_Coolant", "Cummins_DCA"]
    },
    "head_toilet_winterization": {
        "manual_wc": [
            "Drain_pump_lines",
            "Add_antifreeze_to_bowl_and_pump_until_exits_outlet",
            "Leave_small_amount_in_bowl_for_seal_protection"
        ],
        "holding_tank": [
            "Empty_completely_if_macerator_pump",
            "Or_fill_with_antifreeze_solution_if_holding_tank_only",
            "Leave_vent_carbon_filter_open"
        ]
    },
    "gas_system_lpg": {
        "steps": [
            "Verify_solenoid_valve_functioning",
            "Pressure_test_all_connections_with_soapy_water",
            "Turn_off_main_tank_valve",
            "Leave_system_isolated_until_spring"
        ]
    },
    "fuel_system_diesel": {
        "steps": [
            "Top_tank_to_prevent_condensation",
            "Add_diesel_biocide_Biobor_JF_per_instructions",
            "Run_engine_to_distribute_additive",
            "Shut_fuel_shutoff_valve"
        ],
        "concern": "Water_condensation_in_tank_causes_microbial_growth",
        "fuel_polishing": "consider_professional_polishing_service"
    },
    "heating_system": {
        "cabin_heat": [
            "Drain_if_forced_air_water_heated_system",
            "Or_flush_with_antifreeze_if_retaining_heat"
        ],
        "fireplace_or_diesel_heater": [
            "Service_inspection_pre_season",
            "Clean_heat_exchanger",
            "Check_fuel_line_connections"
        ]
    },
    "drain_points_checklist": [
        "Lowest_cabin_faucet",
        "Head_sink_and_shower",
        "Galley_sink",
        "Engine_block_drain_plugs",
        "Pressure_accumulator_tank_drain",
        "Bilge_sump"
    ]
}


def assess_plumbing_installation(
    boat_length_ft: float,
    boat_type: str,
    fuel_type: str,
    systems_installed: List[str]
) -> Dict[str, Any]:
    """
    Comprehensive plumbing system assessment for yacht design analysis.

    Args:
        boat_length_ft: Overall length of vessel (feet)
        boat_type: 'cruiser', 'motorsailer', 'offshore', 'dayboat'
        fuel_type: 'diesel', 'gasoline', 'both'
        systems_installed: List of systems ['freshwater', 'sanitation', 'fuel', 'gas_lpg']

    Returns:
        Dict with assessment score (0-100), findings, and recommendations.
    """

    findings = []
    recommendations = []
    score = 100

    # Base assessment by boat type
    if boat_type == "offshore" and boat_length_ft >= 40:
        findings.append("Offshore yacht configuration detected: recommend full redundancy.")
        recommendations.append("Install backup bilge pump (manual + electric).")
        recommendations.append("Dual independent freshwater tanks recommended.")
    elif boat_type == "cruiser" and boat_length_ft < 35:
        findings.append("Coastal cruiser: standard single-system installation acceptable.")

    # Fuel system checks
    if "fuel" in systems_installed:
        if fuel_type == "diesel":
            findings.append("Diesel fuel selected: water separator and biocide critical.")
            recommendations.append("Install Racor-type water separator with annual maintenance.")
            recommendations.append("Annual fuel polishing service or biocide treatment.")
        elif fuel_type == "gasoline":
            findings.append("Gasoline fuel: anti-siphon valve mandatory for safety.")
            recommendations.append("ABYC H-24 compliant fuel hose required (not PVC).")
            score -= 10 if boat_length_ft > 45 else 0

    # Sanitation checks
    if "sanitation" in systems_installed:
        findings.append("Sanitation system installed: holding tank and venting critical.")
        if boat_length_ft >= 35:
            recommendations.append("Consider dual-function Y-valve (seawater and holding tank).")
        recommendations.append("Replace sanitation hose every 8-10 years (permeation risk).")
        recommendations.append("Install carbon-filter holding tank vent to minimize odor.")

    # Gas LPG checks
    if "gas_lpg" in systems_installed:
        findings.append("LPG propane system: locker and safety valve compliance essential.")
        recommendations.append("Dedicated gas locker with overboard drain required.")
        recommendations.append("Annual bubble test at all connections (soapy water).")
        recommendations.append("Solenoid shutoff valve with manual backup.")

    # Freshwater checks
    if "freshwater" in systems_installed:
        tank_capacity = 150 + (boat_length_ft / 5)
        findings.append(f"Recommended freshwater tank capacity: {tank_capacity:.0f} liters.")
        recommendations.append("Accumulator tank for pressure system (reduces pump cycling).")
        if boat_length_ft > 50:
            recommendations.append("Consider watermaker desalination system for extended cruising.")

    # General recommendations
    recommendations.append("All seacocks below waterline must include tapered wooden emergency plugs.")
    recommendations.append("Through-hull inspection: annually before season, post-grounding.")
    recommendations.append("Winter preparation: antifreeze systems (propylene glycol food-grade).")
    recommendations.append("Hose aging: visually inspect annually, replace if cracked or soft.")

    return {
        "assessment_score": max(0, score),
        "boat_classification": boat_type,
        "findings": findings,
        "recommendations": recommendations,
        "critical_items": [
            "Bilge pump functionality and float switch operation",
            "All below-waterline seacocks and emergency plugs",
            "Sanitation hose permeation (age and integrity)",
            "Fuel system anti-siphon protection",
            "LPG gas locker ventilation and solenoid shutoff"
        ],
        "maintenance_frequency_summary": {
            "weekly": ["test_bilge_pump_float_switch", "monitor_fuel_water_separator"],
            "monthly": ["check_through_hull_integrity", "visual_hose_inspection"],
            "quarterly": ["pressure_test_fuel_system", "sanitize_freshwater_tank"],
            "annually": ["replace_fuel_racor_cartridge", "professional_through_hull_haul_out_inspection"],
            "5_years": ["replace_bilge_hose", "recharge_accumulator_tank"],
            "7_years": ["replace_raw_water_cooling_hose", "replace_sanitation_hose"],
            "10_years": ["full_system_overhaul_assessment", "through_hull_fitting_replacement"]
        }
    }
