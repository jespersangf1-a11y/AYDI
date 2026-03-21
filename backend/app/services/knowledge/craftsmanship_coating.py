"""
AYDI Coating & Surface Finishing Knowledge Base
Marine painting and coatings for yacht design analysis
Author: Master Marine Painter/Coater KnowledgeBase
Version: 1.0

Umfassendes Wissen über Anstrichsysteme, Oberflächenvorbereitung und Beschichtungstechniken
für marine Anwendungen im Yachtbau. Basiert auf Jahrzehnten praktischer Erfahrung.
"""

# ============================================================================
# PAINT SYSTEMS - Vollständige Anstrichsysteme von Grundierung bis Decklack
# ============================================================================

PAINT_SYSTEMS = {
    # OBERDECKSSYSTEME - Above Waterline

    "two_pack_polyurethane_above_wl": {
        "name": "Zweikomponenten-Polyurethan Überwasser",
        "name_de": "2K-PU Oberdeckssystem",
        "application_zone": ["above_waterline", "cabin_sides", "superstructure"],
        "boat_class_suitable": ["dinghy", "cruiser", "racing", "superyacht"],
        "total_dft_micron": 180,
        "durability_years": 5,
        "cost_rating": 4,
        "description": "Premium 2K polyurethane system offering excellent UV resistance, durability and aesthetics",
        "layers": [
            {
                "layer_number": 1,
                "product_type": "epoxy_primer",
                "coats": 1,
                "wet_film_thickness_micron": 150,
                "dry_film_thickness_micron": 75,
                "recoat_window_hours_min": 4,
                "recoat_window_hours_max": 16,
            },
            {
                "layer_number": 2,
                "product_type": "polyurethane_intermediate",
                "coats": 1,
                "wet_film_thickness_micron": 120,
                "dry_film_thickness_micron": 60,
                "recoat_window_hours_min": 6,
                "recoat_window_hours_max": 24,
            },
            {
                "layer_number": 3,
                "product_type": "polyurethane_topcoat",
                "coats": 2,
                "wet_film_thickness_micron": 90,
                "dry_film_thickness_micron": 45,
                "recoat_window_hours_min": 8,
                "recoat_window_hours_max": 48,
            },
        ],
        "surface_prep": [
            "Power wash with 80-100 bar, allow 24h drying",
            "Sand with P120 to P180 to remove gloss and contaminants",
            "Vacuum clean all dust",
            "Final tack rag wipe immediately before application",
        ],
        "application_method": {
            "primary": "hvlp_spray",
            "secondary": "airless_spray",
            "description": "HVLP spray for finish quality, 50% overlap, 2-3 mm fan width. Thin coats prevent runs.",
            "gun_pressure_bar": 1.2,
            "nozzle_size_mm": 1.4,
            "spray_distance_cm": 25,
        },
        "temperature_range_c": [15, 25],
        "humidity_max_pct": 85,
        "dew_point_margin_c": 3,
        "pot_life_minutes": 4,
        "working_time_minutes": 120,
        "quality_criteria": {
            "gloss_level": "high",
            "gloss_60_min": 70,
            "surface_smoothness": "mirror-like",
            "color_match": "exact_match_to_reference",
            "adhesion": "excellent",
            "hardness": "pencil_2H",
            "water_resistance": "excellent",
        },
        "common_defects": [
            "runs_sags",
            "orange_peel",
            "fish_eyes",
            "solvent_popping",
            "color_mismatch",
        ],
        "preparation_days_needed": 3,
        "application_days_per_coat": 1,
        "curing_days": 7,
    },

    "one_pack_polyurethane_above_wl": {
        "name": "Einkomponenten-Polyurethan Überwasser",
        "name_de": "1K-PU Oberdeckssystem",
        "application_zone": ["above_waterline", "trim_work"],
        "boat_class_suitable": ["dinghy", "cruiser", "fishing_boat"],
        "total_dft_micron": 160,
        "durability_years": 4,
        "cost_rating": 3,
        "description": "Single-component polyurethane, easy to apply, good UV resistance, limited pot life",
        "layers": [
            {
                "layer_number": 1,
                "product_type": "alkyd_primer",
                "coats": 1,
                "wet_film_thickness_micron": 120,
                "dry_film_thickness_micron": 60,
                "recoat_window_hours_min": 12,
                "recoat_window_hours_max": 48,
            },
            {
                "layer_number": 2,
                "product_type": "polyurethane_topcoat_1k",
                "coats": 2,
                "wet_film_thickness_micron": 100,
                "dry_film_thickness_micron": 50,
                "recoat_window_hours_min": 6,
                "recoat_window_hours_max": 24,
            },
        ],
        "surface_prep": [
            "Sand with P120-P150 to remove old coating",
            "Clean with tack rag",
            "Allow 2h before painting in cool/dry conditions",
        ],
        "application_method": {
            "primary": "brush_synthetic",
            "secondary": "foam_roller",
            "description": "Apply with quality synthetic brush in thin, even coats. Maintain wet edge.",
            "film_build_per_coat_micron": 50,
        },
        "temperature_range_c": [10, 28],
        "humidity_max_pct": 80,
        "dew_point_margin_c": 3,
        "pot_life_minutes": 6,
        "quality_criteria": {
            "gloss_level": "medium-high",
            "adhesion": "good",
            "hardness": "pencil_H",
            "drying_time_hours": 4,
        },
        "common_defects": [
            "brush_marks",
            "runs_sags",
            "color_variation",
        ],
        "curing_days": 5,
    },

    "alkyd_enamel_traditional": {
        "name": "Alkyd-Emaillelack traditionell",
        "name_de": "Alkyd-Email traditionell",
        "application_zone": ["above_waterline", "trim_work", "cabin_exterior"],
        "boat_class_suitable": ["classic_yacht", "restoration", "wooden_boat"],
        "total_dft_micron": 140,
        "durability_years": 3,
        "cost_rating": 2,
        "description": "Classic alkyd enamel for traditional yacht restoration, excellent working properties",
        "layers": [
            {
                "layer_number": 1,
                "product_type": "oil_primer",
                "coats": 1,
                "wet_film_thickness_micron": 100,
                "dry_film_thickness_micron": 50,
                "recoat_window_hours_min": 16,
                "recoat_window_hours_max": 72,
            },
            {
                "layer_number": 2,
                "product_type": "alkyd_enamel",
                "coats": 2,
                "wet_film_thickness_micron": 90,
                "dry_film_thickness_micron": 45,
                "recoat_window_hours_min": 12,
                "recoat_window_hours_max": 48,
            },
        ],
        "surface_prep": [
            "Scrape off old loose paint",
            "Sand smooth with P100-P120",
            "Wipe clean, allow dust to settle",
        ],
        "application_method": {
            "primary": "brush_natural",
            "description": "Traditional natural bristle brush, long flowing strokes, maintain wet edge carefully",
            "brush_size_mm": 50,
        },
        "temperature_range_c": [8, 30],
        "humidity_max_pct": 85,
        "dew_point_margin_c": 2,
        "pot_life_minutes": 240,
        "quality_criteria": {
            "gloss_level": "semi-gloss",
            "surface_finish": "smooth",
            "traditional_appearance": True,
        },
        "common_defects": [
            "brush_marks",
            "sagging_in_thick_application",
        ],
        "curing_days": 10,
    },

    # UNTERWASSERSYSTEME - Below Waterline

    "epoxy_below_waterline": {
        "name": "Epoxid-Schutzsystem Unterwasser",
        "name_de": "Epoxid Unterwassersystem",
        "application_zone": ["below_waterline", "waterline", "rudder"],
        "boat_class_suitable": ["dinghy", "cruiser", "racing", "superyacht"],
        "total_dft_micron": 220,
        "durability_years": 6,
        "cost_rating": 4,
        "description": "High-build epoxy system providing excellent moisture barrier and corrosion protection",
        "layers": [
            {
                "layer_number": 1,
                "product_type": "epoxy_primer_high_build",
                "coats": 1,
                "wet_film_thickness_micron": 200,
                "dry_film_thickness_micron": 100,
                "recoat_window_hours_min": 4,
                "recoat_window_hours_max": 16,
            },
            {
                "layer_number": 2,
                "product_type": "epoxy_midcoat",
                "coats": 1,
                "wet_film_thickness_micron": 150,
                "dry_film_thickness_micron": 75,
                "recoat_window_hours_min": 6,
                "recoat_window_hours_max": 24,
            },
            {
                "layer_number": 3,
                "product_type": "epoxy_topcoat",
                "coats": 1,
                "wet_film_thickness_micron": 90,
                "dry_film_thickness_micron": 45,
                "recoat_window_hours_min": 8,
                "recoat_window_hours_max": 72,
            },
        ],
        "surface_prep": [
            "Abrasive blast SA 2.5 (80-90% white metal)",
            "Achieve surface profile Ra 2.5-3.5 micron",
            "Remove all salt and contamination",
            "Apply within 8 hours of blasting (flash rust prevention)",
        ],
        "application_method": {
            "primary": "airless_spray",
            "secondary": "hvlp_spray",
            "description": "Airless spray 2-3 bar, thick coats, prevent sags through horizontal application",
            "spray_distance_cm": 30,
            "nozzle_size_mm": 1.8,
        },
        "temperature_range_c": [10, 30],
        "humidity_max_pct": 75,
        "dew_point_margin_c": 4,
        "pot_life_minutes": 8,
        "working_time_minutes": 180,
        "quality_criteria": {
            "adhesion": "excellent_to_substrate",
            "hardness": "pencil_3H",
            "impact_resistance": "good",
            "water_absorption": "minimal",
            "salt_spray_resistance": "500_hours",
        },
        "common_defects": [
            "pinholes",
            "blistering",
            "water_ingress",
        ],
        "preparation_days_needed": 2,
        "curing_days": 14,
    },

    # ANTIFOULING-SYSTEME

    "antifouling_copper_selfpolishing": {
        "name": "Selbstpolierendes Kupfer-Antifouling (ESPC)",
        "name_de": "Kupfer ESPC Antifouling",
        "application_zone": ["below_waterline", "rudder", "propeller_shaft"],
        "boat_class_suitable": ["cruiser", "racing", "fishing_boat", "superyacht"],
        "total_dft_micron": 200,
        "durability_years": 4,
        "cost_rating": 3,
        "description": "Eco-friendly self-polishing copper antifouling with gradual wear pattern",
        "layers": [
            {
                "layer_number": 1,
                "product_type": "epoxy_barrier_coat",
                "coats": 1,
                "wet_film_thickness_micron": 150,
                "dry_film_thickness_micron": 75,
                "recoat_window_hours_min": 4,
                "recoat_window_hours_max": 16,
            },
            {
                "layer_number": 2,
                "product_type": "antifouling_copper_espc",
                "coats": 2,
                "wet_film_thickness_micron": 100,
                "dry_film_thickness_micron": 50,
                "recoat_window_hours_min": 6,
                "recoat_window_hours_max": 48,
            },
        ],
        "surface_prep": [
            "Remove existing AF with sander or scraper (P60-P80)",
            "Abrasive blast to SA 2.5 if bare metal exposed",
            "Wash with freshwater, allow to dry completely",
        ],
        "application_method": {
            "primary": "airless_spray",
            "description": "Apply in vertical passes, avoid excessive thickness which reduces effectiveness",
            "nozzle_size_mm": 1.6,
            "pressure_bar": 2.5,
        },
        "temperature_range_c": [15, 28],
        "humidity_max_pct": 80,
        "dew_point_margin_c": 3,
        "pot_life_minutes": 4,
        "quality_criteria": {
            "copper_content_pct": 28,
            "polishing_rate_micron_per_month": 15,
            "adhesion": "excellent",
            "coverage": "complete_no_holidays",
        },
        "environmental_rating": "IMO approved ESPC",
        "common_defects": [
            "insufficient_coverage",
            "delamination_from_barrier",
        ],
        "application_months": "spring_maintenance",
        "curing_days": 3,
    },

    "antifouling_hard": {
        "name": "Hartantifouling",
        "name_de": "Hard-Antifouling",
        "application_zone": ["below_waterline", "keel", "rudder"],
        "boat_class_suitable": ["fishing_boat", "workboat", "motorsailer"],
        "total_dft_micron": 250,
        "durability_years": 5,
        "cost_rating": 2,
        "description": "Durable hard antifouling with high copper oxide content, excellent protection",
        "layers": [
            {
                "layer_number": 1,
                "product_type": "epoxy_barrier_coat",
                "coats": 1,
                "wet_film_thickness_micron": 150,
                "dry_film_thickness_micron": 75,
                "recoat_window_hours_min": 4,
                "recoat_window_hours_max": 16,
            },
            {
                "layer_number": 2,
                "product_type": "antifouling_hard_ablative",
                "coats": 2,
                "wet_film_thickness_micron": 125,
                "dry_film_thickness_micron": 62,
                "recoat_window_hours_min": 6,
                "recoat_window_hours_max": 36,
            },
        ],
        "surface_prep": [
            "Mechanical removal of old AF coating",
            "Sand to P80-P120 for texture",
            "Clean with tack rag",
        ],
        "application_method": {
            "primary": "airless_spray",
            "secondary": "roller",
            "description": "Airless spray or 10mm nap roller, allow proper leveling between coats",
            "roller_nap_mm": 10,
        },
        "temperature_range_c": [10, 30],
        "humidity_max_pct": 85,
        "dew_point_margin_c": 2,
        "pot_life_minutes": 120,
        "quality_criteria": {
            "hardness": "pencil_HB",
            "adhesion": "excellent",
            "abrasion_resistance": "high",
            "copper_oxide_content_pct": 50,
        },
        "common_defects": [
            "rough_application",
            "incomplete_coverage",
        ],
        "curing_days": 7,
    },

    "antifouling_silicone": {
        "name": "Silikon-Antifouling eco",
        "name_de": "Silikon-Antifouling ökologisch",
        "application_zone": ["below_waterline"],
        "boat_class_suitable": ["dinghy", "cruiser", "superyacht"],
        "total_dft_micron": 180,
        "durability_years": 3,
        "cost_rating": 5,
        "description": "Premium eco-friendly silicon-based AF, no biocide leaching, excellent foul release",
        "layers": [
            {
                "layer_number": 1,
                "product_type": "epoxy_primer",
                "coats": 1,
                "wet_film_thickness_micron": 150,
                "dry_film_thickness_micron": 75,
                "recoat_window_hours_min": 4,
                "recoat_window_hours_max": 16,
            },
            {
                "layer_number": 2,
                "product_type": "antifouling_silicone",
                "coats": 2,
                "wet_film_thickness_micron": 90,
                "dry_film_thickness_micron": 45,
                "recoat_window_hours_min": 8,
                "recoat_window_hours_max": 24,
            },
        ],
        "surface_prep": [
            "Remove old AF with soft scraper, avoid substrate damage",
            "Sand lightly with P150 for adhesion",
            "Clean thoroughly",
        ],
        "application_method": {
            "primary": "hvlp_spray",
            "description": "HVLP spray for smooth finish, silicon coatings require careful technique",
            "pressure_bar": 1.5,
        },
        "temperature_range_c": [12, 25],
        "humidity_max_pct": 80,
        "dew_point_margin_c": 4,
        "pot_life_minutes": 6,
        "eco_rating": "biocide_free",
        "quality_criteria": {
            "surface_slip_coefficient": 0.1,
            "foul_release_performance": "excellent",
            "environmental_compliance": "IMO_approved",
        },
        "common_defects": [
            "poor_adhesion_if_contaminated",
            "application_over_copper_af_issues",
        ],
        "curing_days": 5,
    },

    # SPEZIALCOATINGS

    "bilge_paint_epoxy": {
        "name": "Bilgenfarbe Epoxid",
        "name_de": "Epoxid-Bilgenfarbe",
        "application_zone": ["bilge", "engine_compartment_lower"],
        "boat_class_suitable": ["all_classes"],
        "total_dft_micron": 250,
        "durability_years": 4,
        "cost_rating": 3,
        "description": "Heavy-duty epoxy for bilge areas, excellent fuel and water resistance",
        "layers": [
            {
                "layer_number": 1,
                "product_type": "epoxy_primer_bilge",
                "coats": 1,
                "wet_film_thickness_micron": 200,
                "dry_film_thickness_micron": 100,
                "recoat_window_hours_min": 4,
                "recoat_window_hours_max": 16,
            },
            {
                "layer_number": 2,
                "product_type": "epoxy_topcoat_bilge",
                "coats": 1,
                "wet_film_thickness_micron": 150,
                "dry_film_thickness_micron": 75,
                "recoat_window_hours_min": 6,
                "recoat_window_hours_max": 24,
            },
        ],
        "surface_prep": [
            "Degrease with solvent wipe or alkaline cleaner",
            "Sand with P100-P120",
            "Abrasive blast SA 2 for severe contamination",
            "Remove all oil, fuel, and water residue",
        ],
        "application_method": {
            "primary": "airless_spray",
            "secondary": "roller",
            "description": "Airless spray 2-3 bar, achieve full coverage with 30% overlap",
            "nozzle_size_mm": 1.8,
        },
        "temperature_range_c": [15, 28],
        "humidity_max_pct": 75,
        "dew_point_margin_c": 4,
        "pot_life_minutes": 8,
        "quality_criteria": {
            "fuel_resistance": "excellent",
            "water_absorption": "minimal",
            "salt_spray_500h": "minimal_corrosion",
            "adhesion": "excellent",
        },
        "common_defects": [
            "adhesion_failure_from_oil",
            "blistering_from_moisture",
        ],
        "curing_days": 10,
    },

    "engine_room_paint": {
        "name": "Maschinenraumfarbe",
        "name_de": "Engine Room Beschichtung",
        "application_zone": ["engine_room", "machinery_space"],
        "boat_class_suitable": ["all_classes"],
        "total_dft_micron": 200,
        "durability_years": 3,
        "cost_rating": 3,
        "description": "Heat-resistant coating for engine rooms, handles thermal cycling and vibration",
        "layers": [
            {
                "layer_number": 1,
                "product_type": "epoxy_primer_heat_resistant",
                "coats": 1,
                "wet_film_thickness_micron": 150,
                "dry_film_thickness_micron": 75,
                "recoat_window_hours_min": 4,
                "recoat_window_hours_max": 16,
            },
            {
                "layer_number": 2,
                "product_type": "polyurethane_topcoat_heat_resistant",
                "coats": 1,
                "wet_film_thickness_micron": 125,
                "dry_film_thickness_micron": 62,
                "recoat_window_hours_min": 6,
                "recoat_window_hours_max": 24,
            },
        ],
        "surface_prep": [
            "Solvent clean to remove oil and grease",
            "Sand with P80-P120",
            "Vacuum clean thoroughly",
        ],
        "application_method": {
            "primary": "brush_synthetic",
            "secondary": "roller",
            "description": "Brush or roller application, ensure complete coverage of edges",
        },
        "temperature_range_c": [10, 30],
        "humidity_max_pct": 80,
        "dew_point_margin_c": 3,
        "heat_resistance_celsius": 60,
        "quality_criteria": {
            "heat_resistance": "60C_continuous",
            "adhesion": "good",
            "resistance_to_oils": "excellent",
            "vibration_resistance": "good",
        },
        "common_defects": [
            "adhesion_loss_thermal_cycling",
            "blistering_high_humidity",
        ],
        "curing_days": 7,
    },

    "nonskid_deck_coating": {
        "name": "Rutschfeste Decksbeschichtung",
        "name_de": "Antirutsch-Decksbeschichtung",
        "application_zone": ["deck", "cabin_top", "walkway"],
        "boat_class_suitable": ["all_classes"],
        "total_dft_micron": 300,
        "durability_years": 3,
        "cost_rating": 3,
        "description": "Textured non-skid coating with excellent grip and UV resistance",
        "layers": [
            {
                "layer_number": 1,
                "product_type": "polyurethane_primer_deck",
                "coats": 1,
                "wet_film_thickness_micron": 150,
                "dry_film_thickness_micron": 75,
                "recoat_window_hours_min": 6,
                "recoat_window_hours_max": 24,
            },
            {
                "layer_number": 2,
                "product_type": "polyurethane_nonskid",
                "coats": 2,
                "wet_film_thickness_micron": 125,
                "dry_film_thickness_micron": 62,
                "recoat_window_hours_min": 8,
                "recoat_window_hours_max": 48,
                "aggregate_type": "silica_sand",
                "aggregate_size_micron": 100,
                "aggregate_content_pct": 40,
            },
        ],
        "surface_prep": [
            "Power wash deck thoroughly",
            "Sand with P120-P150 to improve adhesion",
            "Clean all salt residue",
            "Allow 48h drying in dry conditions",
        ],
        "application_method": {
            "primary": "roller",
            "secondary": "brush_for_edges",
            "description": "10mm nap roller with continuous stirring to keep aggregate suspended",
            "roller_nap_mm": 10,
        },
        "temperature_range_c": [15, 25],
        "humidity_max_pct": 75,
        "dew_point_margin_c": 4,
        "pot_life_minutes": 6,
        "quality_criteria": {
            "slip_resistance_coefficient": 0.6,
            "texture_uniformity": "consistent_throughout",
            "aggregate_embedding": "fully_embedded",
            "uv_resistance": "excellent",
        },
        "common_defects": [
            "aggregate_settling",
            "uneven_texture",
            "aggregate_loss",
        ],
        "curing_days": 14,
    },

    "teak_deck_sealer": {
        "name": "Teak-Deck Versiegelung",
        "name_de": "Teak-Deck Schutz",
        "application_zone": ["teak_deck", "teak_trim"],
        "boat_class_suitable": ["classic_yacht", "superyacht", "cruiser"],
        "total_dft_micron": 80,
        "durability_years": 2,
        "cost_rating": 4,
        "description": "Transparent protective sealer for teak wood, maintains natural grain appearance",
        "layers": [
            {
                "layer_number": 1,
                "product_type": "teak_oil_sealer",
                "coats": 2,
                "wet_film_thickness_micron": 50,
                "dry_film_thickness_micron": 25,
                "recoat_window_hours_min": 4,
                "recoat_window_hours_max": 24,
            },
        ],
        "surface_prep": [
            "Clean teak with specialized teak cleaner",
            "Sand lightly with P150-P180 if weathered",
            "Remove all dust and dirt",
            "Allow wood to dry 24h minimum",
        ],
        "application_method": {
            "primary": "brush_natural",
            "secondary": "cotton_cloth",
            "description": "Apply with grain, use lint-free cloth for final wipe-down immediately",
            "wipe_down_minutes": 10,
        },
        "temperature_range_c": [15, 25],
        "humidity_max_pct": 60,
        "dew_point_margin_c": 5,
        "pot_life_minutes": 480,
        "quality_criteria": {
            "wood_appearance": "natural_grain_visible",
            "water_beading": "good",
            "surface_feel": "smooth_natural",
            "color_retention": "maintains_warm_tone",
        },
        "common_defects": [
            "sticky_residue_poor_wiping",
            "white_haze_dust",
        ],
        "maintenance_months": 12,
        "curing_days": 3,
    },

    # KLARLACK-SYSTEME

    "varnish_spar_traditional": {
        "name": "Bootslack Spar traditionell",
        "name_de": "Spar-Bootslack traditionell",
        "application_zone": ["bright_work", "trim", "cabin_sides"],
        "boat_class_suitable": ["classic_yacht", "wooden_boat", "restoration"],
        "total_dft_micron": 100,
        "durability_years": 2,
        "cost_rating": 4,
        "description": "Traditional flexible spar varnish, maintains appearance with proper maintenance",
        "layers": [
            {
                "layer_number": 1,
                "product_type": "spar_varnish_sealer",
                "coats": 1,
                "wet_film_thickness_micron": 80,
                "dry_film_thickness_micron": 40,
                "recoat_window_hours_min": 12,
                "recoat_window_hours_max": 48,
            },
            {
                "layer_number": 2,
                "product_type": "spar_varnish",
                "coats": 3,
                "wet_film_thickness_micron": 60,
                "dry_film_thickness_micron": 30,
                "recoat_window_hours_min": 16,
                "recoat_window_hours_max": 48,
            },
        ],
        "surface_prep": [
            "Strip old varnish with chemical stripper or sander P80-P120",
            "Sand bare wood with P150-P220",
            "Stain if desired",
            "Final sand with P220 before first coat",
            "Tack rag wipe",
        ],
        "application_method": {
            "primary": "brush_natural",
            "description": "High-quality natural bristle brush, long smooth strokes, maintain wet edge",
            "brush_size_mm": 50,
            "stroke_direction": "with_grain",
        },
        "temperature_range_c": [15, 25],
        "humidity_max_pct": 70,
        "dew_point_margin_c": 4,
        "pot_life_minutes": 480,
        "quality_criteria": {
            "gloss_level": "high",
            "clarity": "crystal_clear",
            "wood_grain_visibility": "excellent",
            "flexibility": "excellent",
        },
        "common_defects": [
            "brush_marks",
            "dust_inclusions",
            "hazy_appearance",
        ],
        "maintenance_frequency_months": 6,
        "curing_days": 14,
    },

    "varnish_2k_polyurethane": {
        "name": "2K-Polyurethan-Klarlack",
        "name_de": "2K-PU Klarlack hochglanz",
        "application_zone": ["bright_work", "trim", "cabin_detail"],
        "boat_class_suitable": ["modern_yacht", "superyacht", "cruiser"],
        "total_dft_micron": 120,
        "durability_years": 4,
        "cost_rating": 5,
        "description": "Premium 2K polyurethane clear coat, superior durability and UV resistance",
        "layers": [
            {
                "layer_number": 1,
                "product_type": "primer_for_varnish",
                "coats": 1,
                "wet_film_thickness_micron": 100,
                "dry_film_thickness_micron": 50,
                "recoat_window_hours_min": 4,
                "recoat_window_hours_max": 16,
            },
            {
                "layer_number": 2,
                "product_type": "polyurethane_clear_coat_2k",
                "coats": 2,
                "wet_film_thickness_micron": 90,
                "dry_film_thickness_micron": 45,
                "recoat_window_hours_min": 6,
                "recoat_window_hours_max": 24,
            },
        ],
        "surface_prep": [
            "Sand substrate with P150-P180",
            "Vacuum clean all dust",
            "Tack rag wipe immediately before application",
        ],
        "application_method": {
            "primary": "hvlp_spray",
            "description": "HVLP spray for flawless finish, thin coats to prevent runs",
            "pressure_bar": 1.2,
            "nozzle_size_mm": 1.4,
        },
        "temperature_range_c": [18, 25],
        "humidity_max_pct": 75,
        "dew_point_margin_c": 4,
        "pot_life_minutes": 4,
        "quality_criteria": {
            "gloss_60_degree": 90,
            "clarity": "crystal_clear_no_bubbles",
            "hardness": "pencil_2H",
            "uv_resistance": "excellent",
        },
        "common_defects": [
            "runs_sags",
            "orange_peel",
            "dust_nibs",
        ],
        "curing_days": 7,
    },

    # REPARATUR-SYSTEME

    "gelcoat_repair_system": {
        "name": "Gelcoat-Reparatursystem",
        "name_de": "Gelcoat Reparatur",
        "application_zone": ["fiberglass_hull", "damage_repair"],
        "boat_class_suitable": ["fiberglass_boat", "all_modern_boats"],
        "total_dft_micron": 250,
        "durability_years": 7,
        "cost_rating": 2,
        "description": "Color-matched gelcoat repair system for fiberglass damage restoration",
        "layers": [
            {
                "layer_number": 1,
                "product_type": "polyester_resin_fill",
                "coats": 1,
                "wet_film_thickness_micron": 0,
                "dry_film_thickness_micron": 0,
                "application_note": "Build up with resin before gelcoat application",
            },
            {
                "layer_number": 2,
                "product_type": "gelcoat_matched",
                "coats": 1,
                "wet_film_thickness_micron": 250,
                "dry_film_thickness_micron": 200,
                "recoat_window_hours_min": 24,
                "recoat_window_hours_max": 72,
            },
        ],
        "surface_prep": [
            "Grind out damage with P40-P80 to sound substrate",
            "Create tapered edges 1:10 ratio minimum",
            "Vacuum clean all dust and debris",
            "Wipe with acetone to remove contamination",
        ],
        "application_method": {
            "primary": "spray_gun",
            "secondary": "brush",
            "description": "Spray application for best color match and finish, small repairs can be brush applied",
            "spray_pressure_bar": 2.0,
        },
        "temperature_range_c": [18, 28],
        "humidity_max_pct": 80,
        "dew_point_margin_c": 3,
        "pot_life_minutes": 20,
        "quality_criteria": {
            "color_match": "exact_match_to_hull",
            "gloss_match": "exactly_blends_with_surrounding",
            "gap_filling": "no_micro_voids",
            "surface_profile": "feathered_blend",
        },
        "common_defects": [
            "color_mismatch",
            "gloss_mismatch",
            "visible_repair_edge",
            "shrinkage_during_cure",
        ],
        "curing_days": 7,
    },

    "barrier_coat_osmosis": {
        "name": "Barrier-Coat Osmoseschutz",
        "name_de": "Osmose-Barrier-Coat",
        "application_zone": ["below_waterline", "osmosis_prevention"],
        "boat_class_suitable": ["fiberglass_boat", "older_construction"],
        "total_dft_micron": 300,
        "durability_years": 5,
        "cost_rating": 4,
        "description": "High-build barrier coat to prevent water ingress and osmotic blister formation",
        "layers": [
            {
                "layer_number": 1,
                "product_type": "epoxy_primer_osmosis",
                "coats": 1,
                "wet_film_thickness_micron": 200,
                "dry_film_thickness_micron": 100,
                "recoat_window_hours_min": 4,
                "recoat_window_hours_max": 16,
            },
            {
                "layer_number": 2,
                "product_type": "epoxy_barrier_coat_high_build",
                "coats": 2,
                "wet_film_thickness_micron": 150,
                "dry_film_thickness_micron": 100,
                "recoat_window_hours_min": 6,
                "recoat_window_hours_max": 24,
            },
        ],
        "surface_prep": [
            "Fair out blistered areas, sand smooth",
            "Abrasive blast SA 2.5 for optimal adhesion",
            "Achieve surface profile Ra 2.5-3.5 micron",
            "Dry thoroughly before application (moisture meter check)",
        ],
        "application_method": {
            "primary": "airless_spray",
            "secondary": "roller",
            "description": "Airless spray 2.5-3.0 bar, multiple thin coats better than one thick coat",
            "spray_pattern": "50_percent_overlap",
        },
        "temperature_range_c": [10, 30],
        "humidity_max_pct": 75,
        "dew_point_margin_c": 4,
        "moisture_content_max_pct": 12,
        "pot_life_minutes": 8,
        "quality_criteria": {
            "water_permeability": "minimal",
            "adhesion": "excellent_to_fiberglass",
            "impact_resistance": "excellent",
            "salt_spray_resistance": "1000_hours_minimum",
            "void_filling": "complete",
        },
        "common_defects": [
            "pinholes_poor_adhesion",
            "blistering_from_moisture",
            "delamination",
        ],
        "curing_days": 14,
        "moisture_check_required": True,
    },
}

# ============================================================================
# SURFACE PREPARATION METHODS
# ============================================================================

SURFACE_PREPARATION = {
    "sanding_grades": {
        "name": "Schleifen - Körnungsgrade",
        "description": "Standard abrasive sanding grades from coarse to ultra-fine",
        "grades": {
            "P40": {
                "grit_size_micron": 425,
                "use_case": "Aggressive removal, rough surfaces, old paint stripping",
                "substrate": "metal",
                "finish": "very_rough",
                "typical_application": "First stage in heavy restoration",
            },
            "P60": {
                "grit_size_micron": 250,
                "use_case": "Paint removal, fiberglass fairing",
                "substrate": ["metal", "fiberglass"],
                "finish": "rough",
            },
            "P80": {
                "grit_size_micron": 180,
                "use_case": "General surface preparation, removing old coatings",
                "substrate": ["metal", "fiberglass", "wood"],
                "finish": "semi-rough",
            },
            "P100": {
                "grit_size_micron": 150,
                "use_case": "Intermediate sanding, primer sanding",
                "substrate": ["all"],
                "finish": "medium",
            },
            "P120": {
                "grit_size_micron": 125,
                "use_case": "Most common preparation grade before paint",
                "substrate": ["all"],
                "finish": "medium",
                "industry_standard": True,
            },
            "P150": {
                "grit_size_micron": 106,
                "use_case": "Fine preparation, between coats sanding",
                "substrate": ["all"],
                "finish": "fine",
            },
            "P180": {
                "grit_size_micron": 90,
                "use_case": "Fine sanding, preparation for topcoat",
                "substrate": ["all"],
                "finish": "fine",
            },
            "P220": {
                "grit_size_micron": 75,
                "use_case": "Very fine finish sanding, between varnish coats",
                "substrate": ["wood", "previous_coating"],
                "finish": "very_fine",
            },
            "P320": {
                "grit_size_micron": 46,
                "use_case": "Ultra-fine sanding for varnish",
                "substrate": ["wood", "varnish"],
                "finish": "ultra_fine",
            },
            "P500": {
                "grit_size_micron": 30,
                "use_case": "Final sanding before clear coat",
                "substrate": ["fine_surfaces"],
                "finish": "ultra_fine",
            },
            "P1000": {
                "grit_size_micron": 15,
                "use_case": "Wet sanding, final finish preparation",
                "substrate": ["clear_coat_work"],
                "finish": "mirror_preparation",
            },
            "P2000": {
                "grit_size_micron": 8,
                "use_case": "Wet sanding, super fine final finish",
                "substrate": ["clear_coat_repair"],
                "finish": "ultra_mirror",
            },
        },
    },

    "degreasing": {
        "name": "Entfettung",
        "description": "Removal of oil, grease, wax, and contamination",
        "methods": {
            "solvent_wipe": {
                "type": "chemical_solvent",
                "solvents": ["mineral_spirits", "acetone", "degreaser_cleaner"],
                "use_case": "Quick contamination removal, oil and grease",
                "when_to_use": "Before sanding or primer application",
                "equipment": "lint-free cloth, solvent",
                "quality_criteria": {
                    "cloth_residue": "none_white_cloth_stays_clean",
                    "surface_shine": "removed",
                    "contamination": "none_visible",
                },
                "common_mistakes": [
                    "Using tap water that leaves minerals",
                    "Insufficient wipe-down time",
                    "Recontamination from dirty cloth",
                ],
            },
            "water_based_cleaner": {
                "type": "alkaline_detergent",
                "cleaners": ["marine_boat_soap", "alkaline_cleaner", "pressure_wash"],
                "use_case": "Salt removal, water-soluble contamination",
                "when_to_use": "After power washing, before painting",
                "equipment": "soft brush, clean water, drying time",
                "drying_time_hours": 24,
                "quality_criteria": {
                    "salt_residue": "none_salinity_test_zero",
                    "surface": "clean_matte_finish",
                },
                "common_mistakes": [
                    "Insufficient drying time",
                    "Recontamination from rain",
                    "Not removing all salt deposits",
                ],
            },
            "power_wash_degreasing": {
                "type": "pressure_cleaning",
                "pressure_bar": 80,
                "temperature_celsius": 60,
                "use_case": "Marine growth removal, salt contamination",
                "when_to_use": "Before recoating bottom paint",
                "equipment": "pressure washer, nozzle 25 degrees",
                "distance_cm": 30,
                "quality_criteria": {
                    "surface_cleanliness": "white_rag_stays_white",
                    "growth_removal": "complete",
                },
                "common_mistakes": [
                    "Nozzle too close causing substrate damage",
                    "Insufficient drying time afterward",
                ],
            },
        },
    },

    "abrasive_blasting": {
        "name": "Strahltechnik - Strahlvorbereitung",
        "description": "Industrial abrasive blasting for metal preparation",
        "grades": {
            "SA_1": {
                "name": "Light blast cleaning",
                "coverage_pct": 25,
                "use_case": "Minimal preparation, old paint removed",
                "when_to_use": "Not typical for marine applications",
                "surface_cleanliness": "poor",
                "typical_application": "Not recommended",
            },
            "SA_2": {
                "name": "Hand tool cleaning",
                "coverage_pct": 50,
                "use_case": "Remove rust, loose scale, loose paint",
                "when_to_use": "Quick marine maintenance",
                "surface_cleanliness": "moderate",
                "surface_profile_micron": 1.5,
            },
            "SA_2_5": {
                "name": "Very thorough blast cleaning",
                "coverage_pct": 90,
                "use_case": "Industrial marine standard preparation",
                "when_to_use": "New build, major repaints, epoxy systems",
                "surface_cleanliness": "excellent",
                "surface_profile_micron": 2.5,
                "industry_standard": True,
            },
            "SA_3": {
                "name": "White metal blast cleaning",
                "coverage_pct": 98,
                "use_case": "Complete rust and paint removal",
                "when_to_use": "Naval vessels, high-performance coatings",
                "surface_cleanliness": "excellent_white_metal_appearance",
                "surface_profile_micron": 3.5,
                "flash_rust_time_hours": 4,
            },
        },
    },

    "chemical_etching": {
        "name": "Chemische Vorbehandlung",
        "description": "Chemical surface preparation for enhanced adhesion",
        "methods": {
            "phosphatization": {
                "name_de": "Phosphatierung",
                "purpose": "Create phosphate layer for corrosion protection and paint adhesion",
                "when_to_use": "Steel substrates before primer",
                "process_steps": [
                    "Degrease with alkaline cleaner",
                    "Apply phosphate solution (iron or zinc based)",
                    "Reaction time 5-15 minutes",
                    "Rinse with deionized water",
                    "Air dry thoroughly",
                ],
                "coating_thickness_micron": 2,
                "effectiveness": "good_adhesion_improvement",
            },
            "chromate_conversion": {
                "name_de": "Chromat-Konvertierung",
                "purpose": "Corrosion inhibitor layer, improves adhesion",
                "when_to_use": "Aluminum substrates, aerospace standard",
                "color": "golden_iridescent",
                "coating_thickness_micron": 1.5,
                "toxicity_note": "Hexavalent chromium, environmental restrictions apply",
            },
        },
    },

    "power_washing": {
        "name": "Hochdruckreinigung",
        "description": "Pressure washing for contamination removal",
        "parameters": {
            "pressure_bar": 80,
            "temperature_celsius": 40,
            "nozzle_angle_degrees": 25,
            "distance_cm": 30,
            "when_to_use": "Salt spray removal, marine growth cleaning",
            "substrate_cautions": [
                "Avoid damaging soft substrates",
                "Keep distance from electronics",
                "Not suitable for fiberglass above 100 bar",
            ],
            "drying_time_hours": 24,
            "quality_criteria": {
                "surface_cleanliness": "white_cloth_clean",
                "salt_residue": "zero",
            },
        },
    },

    "dewaxing": {
        "name": "Entwachsen",
        "description": "Removal of wax, mold release, or release agent",
        "when_to_use": "Fiberglass surfaces, newly molded parts, repairs",
        "methods": [
            "Solvent wipe with acetone or specialized remover",
            "Mechanical sanding P80-P120",
            "Chemical dewaxer product application",
        ],
        "quality_criteria": {
            "wax_removal": "complete_no_white_residue",
            "water_beading": "none_water_absorbs",
        },
    },

    "tack_rag": {
        "name": "Haftgrund-Tuch / Tack Rag",
        "description": "Final dust removal before coating application",
        "when_to_use": "Immediately before any paint or varnish application",
        "technique": [
            "Wipe in one direction to gather dust",
            "Change area of rag frequently",
            "Apply light pressure, do not rub vigorously",
            "Final wipe within 30 minutes of application start",
        ],
        "quality_criteria": {
            "dust_particles": "none_visible",
            "surface_cleanliness": "ready_for_paint",
        },
        "common_mistakes": [
            "Tack rag too wet causing adhesion issues",
            "Applied too far in advance before painting",
            "Inadequate coverage of entire surface",
        ],
    },
}

# ============================================================================
# APPLICATION METHODS
# ============================================================================

APPLICATION_METHODS = {
    "brush_natural": {
        "name": "Natural Bristle Brush",
        "name_de": "Naturborstenpinsel",
        "suitable_for": [
            "alkyd_enamel",
            "spar_varnish",
            "spar_varnish_traditional",
            "oil_based_primers",
        ],
        "technique_description": "Long, smooth strokes, maintain wet edge, blend edges of new passes",
        "film_build_per_coat_micron": 40,
        "finish_quality": 0.85,
        "speed_sqm_per_hour": 10,
        "brush_types": {
            "filbert": "General purpose, good for varnish",
            "flat": "Large surfaces, wide strokes",
            "angled": "Edges and trim work",
        },
        "quality_criteria": {
            "brush_marks": "minimal_flow_out",
            "drips_runs": "none",
            "edge_definition": "clean",
        },
        "common_defects": {
            "brush_marks": {
                "cause": "Brush not fully wet, stroking too much",
                "fix": "More frequent brush dipping, long smooth strokes",
            },
            "bristle_shedding": {
                "cause": "Low-quality brush, not pre-wetted",
                "fix": "Use quality marine-grade brush, pre-wet bristles",
            },
            "dust_in_finish": {
                "cause": "Not wiping with tack rag, drafts",
                "fix": "Final tack rag wipe, block off area from air flow",
            },
        },
        "maintenance": "Soak in appropriate solvent, clean thoroughly after use",
    },

    "brush_synthetic": {
        "name": "Synthetic Bristle Brush",
        "name_de": "Kunststoffborstenpinsel",
        "suitable_for": [
            "water_based_paint",
            "one_pack_polyurethane",
            "polyurethane_primers",
            "acrylic_coatings",
        ],
        "technique_description": "Similar to natural bristle, works well with water-based products",
        "film_build_per_coat_micron": 45,
        "finish_quality": 0.80,
        "speed_sqm_per_hour": 12,
        "quality_criteria": {
            "bristle_loss": "minimal",
            "surface_finish": "smooth",
        },
        "common_defects": {
            "bristle_shedding": {
                "cause": "Low quality synthetic fibers",
                "fix": "Invest in quality marine-grade synthetic brushes",
            },
        },
    },

    "foam_roller": {
        "name": "Foam Roller",
        "name_de": "Schaumstoffwalze",
        "suitable_for": [
            "primers",
            "alkyd_enamel",
            "polyurethane_topcoats",
            "acrylic_paints",
        ],
        "technique_description": "Roll in W or M pattern, maintain consistent pressure, slight overlap",
        "nap_mm": 5,
        "film_build_per_coat_micron": 50,
        "finish_quality": 0.75,
        "speed_sqm_per_hour": 20,
        "quality_criteria": {
            "uniformity": "even_coverage",
            "stippling": "minimal_orange_peel_texture",
        },
        "common_defects": {
            "orange_peel": {
                "cause": "Foam roller characteristics, thick application",
                "fix": "Thin coats, blend with brush immediately",
            },
        },
    },

    "mohair_roller": {
        "name": "Mohair Roller",
        "name_de": "Mohair-Walze",
        "suitable_for": [
            "high_gloss_topcoats",
            "polyurethane_paint",
            "enamel",
        ],
        "technique_description": "Fine nap gives excellent finish, slow roll for quality",
        "nap_mm": 8,
        "film_build_per_coat_micron": 55,
        "finish_quality": 0.90,
        "speed_sqm_per_hour": 8,
        "quality_criteria": {
            "finish": "very_smooth",
            "stipple": "minimal",
        },
        "common_defects": {
            "slow_coverage": {
                "cause": "Fine nap requires care",
                "fix": "Accept slower application rate for quality",
            },
        },
    },

    "hvlp_spray": {
        "name": "HVLP Spray (High Volume Low Pressure)",
        "name_de": "HVLP Spritzanlage",
        "suitable_for": [
            "two_pack_polyurethane",
            "polyurethane_topcoats",
            "2k_clear_coat",
            "varnish_2k",
            "antifouling_silicone",
        ],
        "technique_description": "Trigger pulls back for paint flow, maintain 25cm distance, 50% overlap pattern",
        "pressure_bar": 1.2,
        "nozzle_size_mm": 1.4,
        "film_build_per_coat_micron": 45,
        "finish_quality": 0.95,
        "speed_sqm_per_hour": 15,
        "gun_technique": {
            "stroke": "Horizontal or vertical passes at constant speed",
            "overlap": "50 percent of fan width",
            "angle": "90 degrees perpendicular to surface",
            "distance": "25 centimeters optimal",
        },
        "quality_criteria": {
            "finish": "glass_smooth",
            "orange_peel": "minimal_excellent_flow",
            "runs_sags": "none_with_proper_technique",
            "spray_pattern": "even_rectangular",
        },
        "common_defects": {
            "orange_peel": {
                "cause": "Pressure too high, nozzle too far",
                "fix": "Reduce pressure, move closer, slower passes",
            },
            "runs_sags": {
                "cause": "Too much material in one pass, application angle wrong",
                "fix": "Thin coats, proper technique, ensure surface level",
            },
            "dry_spray": {
                "cause": "Air flow separating atomized paint, solvent evaporation",
                "fix": "Reduce air flow, check fluid nozzle setup, increase humidity",
            },
            "fish_eyes": {
                "cause": "Silicone or wax contamination",
                "fix": "Clean gun thoroughly, check for silicone products nearby",
            },
        },
        "setup_notes": "Requires 2 CFM compressor minimum, HVLP conversion kits available",
    },

    "airless_spray": {
        "name": "Airless Spray",
        "name_de": "Airless-Spritzanlage",
        "suitable_for": [
            "epoxy_systems",
            "high_build_primers",
            "bilge_paint",
            "antifouling_copper",
            "barrier_coat",
        ],
        "technique_description": "Pump delivers pressurized paint directly, fast coverage, thicker films",
        "pressure_bar": 2.5,
        "nozzle_size_mm": 1.8,
        "film_build_per_coat_micron": 75,
        "finish_quality": 0.75,
        "speed_sqm_per_hour": 30,
        "gun_technique": {
            "distance": "30 centimeters from surface",
            "overlap": "50 percent fan width",
            "speed": "Constant speed passes",
            "pattern": "Vertical or horizontal sweeps",
        },
        "quality_criteria": {
            "coverage": "complete_no_holidays",
            "buildup": "thick_durable_films",
        },
        "common_defects": {
            "runs_sags": {
                "cause": "Application angle wrong, too much material, surface not level",
                "fix": "Ensure surface level, slower passes, proper gun angle",
            },
            "orange_peel": {
                "cause": "Excessive pressure, viscosity too low",
                "fix": "Reduce pressure slightly, check material viscosity",
            },
        },
        "equipment_notes": "High pressure pump system, tip sizes critical for material type",
    },

    "conventional_spray": {
        "name": "Conventional Spray Gun",
        "name_de": "Konventionelle Spritzanlage",
        "suitable_for": [
            "all_coating_types",
        ],
        "technique_description": "Professional spray method, air atomizes paint, requires skilled operator",
        "air_pressure_bar": 3.0,
        "nozzle_size_mm": 1.8,
        "film_build_per_coat_micron": 60,
        "finish_quality": 0.85,
        "speed_sqm_per_hour": 20,
        "quality_criteria": {
            "finish": "professional_smooth",
        },
        "common_defects": {
            "overspray": {
                "cause": "Air pressure too high, nozzle tip size, spray pattern",
                "fix": "Reduce air pressure, check nozzle setup",
            },
        },
    },

    "roll_and_tip": {
        "name": "Roll and Tip Application",
        "name_de": "Walze mit Pinsel-Finish",
        "suitable_for": [
            "primers",
            "topcoats",
            "high_gloss_finishes",
        ],
        "technique_description": "Apply with roller, immediately tip with brush to remove stipple",
        "film_build_per_coat_micron": 50,
        "finish_quality": 0.88,
        "speed_sqm_per_hour": 15,
        "process": [
            "Roll W or M pattern with roller",
            "Immediately follow with brush tips (light pressure)",
            "Blend edges while coating still wet",
        ],
        "quality_criteria": {
            "finish": "smooth_no_stipple",
            "uniformity": "excellent",
        },
        "common_defects": {
            "brush_marks": {
                "cause": "Tipping too much or paint too viscous",
                "fix": "Light tipping passes, proper viscosity",
            },
        },
    },
}

# ============================================================================
# DEFECT DIAGNOSIS
# ============================================================================

DEFECT_DIAGNOSIS = {
    "runs_sags": {
        "name": "Lackläufer und Durchhänger",
        "name_de": "Runs und Sags",
        "description": "Paint flows downward before curing, creating vertical streaks",
        "cause": [
            "Excessive film thickness in single pass",
            "Paint too thin (low viscosity)",
            "Application at excessive angle",
            "Temperature too low (slow cure, paint flows)",
            "Humidity too high (extends working time)",
            "Applying over slick/non-absorbent surface",
        ],
        "prevention": [
            "Apply thin coats, 2-3 thin better than 1 thick",
            "Maintain proper viscosity per manufacturer",
            "Keep surface level when possible",
            "Paint vertical surfaces from top to bottom",
            "Maintain proper temperature and humidity",
            "Ensure adequate surface preparation for adhesion",
        ],
        "repair_method": [
            "Light sanding with P120-P150 while wet, feather runs",
            "If cured, sand smooth with P220, reapply thin coat",
            "Sand affected area and adjacent zone, blend coat",
            "For severe defects, remove coating, start fresh",
        ],
        "severity": "cosmetic_or_structural_if_very_thick",
        "prevention_temperature_c": [18, 25],
        "prevention_humidity_pct": [50, 75],
    },

    "orange_peel": {
        "name": "Orangenschale",
        "name_de": "Orange Peel Textur",
        "description": "Surface texture resembles orange skin, uneven stippled finish",
        "cause": [
            "Solvent evaporation too fast",
            "Spray pressure too high",
            "Gun too far from surface",
            "Paint too thick (poor leveling)",
            "Inadequate thinning with reducer",
            "Environmental conditions (temperature, humidity)",
            "Roller application without tipping",
        ],
        "prevention": [
            "Use proper spray gun distance (25cm HVLP, 30cm airless)",
            "Reduce spray pressure if possible",
            "Proper viscosity and reducer ratio",
            "Maintain optimal temperature (18-25°C) and humidity (50-75%)",
            "Consider spray booth for humidity control",
            "Use mohair roller with light tipping if rolling",
        ],
        "repair_method": [
            "Fine wet sanding P1000-P2000 to smooth texture",
            "Compound and polish for light orange peel",
            "Recoat with proper technique if severe",
            "Sand smooth, reapply with corrected technique",
        ],
        "severity": "cosmetic",
        "visual_inspection": "Light reflection shows texture, not smooth mirror",
    },

    "fish_eyes": {
        "name": "Fischaugen",
        "name_de": "Fish Eyes (Kraterbildung)",
        "description": "Small circular cratering in paint film, paint crawls away from spots",
        "cause": [
            "Silicone contamination on surface",
            "Wax mold release not removed",
            "Polishing compound residue",
            "Incompatible previous coating",
            "Contaminants in spray gun",
            "Metallic particles or foreign matter",
        ],
        "prevention": [
            "Thorough surface degreasing and cleaning",
            "Use fish eye eliminator in paint if needed",
            "Clean spray gun and all equipment thoroughly",
            "Use lint-free cloth for final wiping",
            "Check for silicone products nearby (polish, release agent)",
            "Adequate surface preparation (sanding, dewaxing)",
        ],
        "repair_method": [
            "Add fish eye eliminator to remaining paint (follow ratio)",
            "Sand affected area smooth, reapply with fish eye eliminator",
            "If severe: Strip coating, thorough cleaning, prime and paint",
            "Test on sample first before adding fish eye reducer",
        ],
        "severity": "cosmetic_but_indicates_contamination",
        "diagnostic_tip": "Forms at same locations repeatedly if persistent contamination",
    },

    "pinholes": {
        "name": "Poren und Pinholes",
        "name_de": "Pinholes und Porenbildung",
        "description": "Small holes or voids in paint film, substrate visible",
        "cause": [
            "Trapped air in porous substrate",
            "Solvent popping during cure",
            "Contamination in spray booth",
            "Application over damp surface",
            "Application over glossy non-absorbent surface",
            "Fiberglass void or cavity bubbles",
        ],
        "prevention": [
            "Ensure substrate fully dry (moisture meter check)",
            "Sand substrate for absorption (P80-P120)",
            "Use primer suited to substrate (bridges voids)",
            "Apply in dust-free environment",
            "Avoid painting over damp or glossy surfaces",
            "High-build primers fill voids better",
        ],
        "repair_method": [
            "Fill small pinholes with putty after prime coat",
            "Sand smooth, apply additional primer and topcoat",
            "For epoxy, apply additional thin coat (self-bridging)",
            "Severe cases: Sand off, restart with proper prep",
        ],
        "severity": "structural_if_deep_voids_reach_substrate",
        "preventive_measure": "Use barrier coat or high-build epoxy on porous surfaces",
    },

    "blistering": {
        "name": "Blasenbildung",
        "name_de": "Blistering",
        "description": "Bubbles or blisters form in paint film, paint separates from substrate",
        "cause": [
            "Water or moisture trapped under coating",
            "Osmotic pressure (salt/moisture ingress in fiberglass)",
            "Application over damp substrate",
            "Inadequate surface preparation",
            "Poor adhesion from contaminants",
            "Exposure to wet conditions too soon after painting",
            "Thermal expansion/contraction cycling",
        ],
        "prevention": [
            "Ensure substrate completely dry (moisture meter <12%)",
            "Allow proper drying time before exposure to water",
            "Proper surface preparation (degreasing, sanding)",
            "High-quality barrier coat for osmosis protection",
            "Adequate recoat windows (avoid trapping solvents)",
            "Proper ventilation during cure",
        ],
        "repair_method": [
            "Small blisters: Sand flat, recoat affected area",
            "Large blisters: Remove paint from blister area, allow dry, prime/paint",
            "Extensive blistering: Strip coating, allow drying, apply barrier coat, repaint",
            "For osmosis: Apply high-build epoxy barrier coat",
        ],
        "severity": "structural_affects_protection",
        "prevention_moisture_content": "Substrate <12% moisture content",
        "prevention_drying_time_before_water": 7,
    },

    "chalking": {
        "name": "Kreidebildung",
        "name_de": "Chalking",
        "description": "Powdery surface deposit, paint appears to chalk when rubbed",
        "cause": [
            "UV degradation of topcoat",
            "Poor UV protection (insufficient binder)",
            "Excessive exposure to weathering",
            "Wrong paint system for exposure (non-UV resistant)",
            "Age/lifespan exceeded",
            "Lack of adequate topcoat",
        ],
        "prevention": [
            "Use UV-resistant topcoats (2K polyurethane, epoxy)",
            "Avoid single-coat systems in high-UV areas",
            "Maintain proper film thickness (minimum DFT)",
            "Schedule repainting within expected durability",
            "Regular maintenance and touch-up",
        ],
        "repair_method": [
            "Wash off chalky residue with water and mild detergent",
            "Light sanding P150-P220",
            "Apply UV-resistant topcoat",
            "For widespread: Strip old paint, apply new system",
        ],
        "severity": "cosmetic_but_indicates_coating_failure",
        "expected_lifespan": "Indicates end of coating life",
    },

    "cracking_checking": {
        "name": "Rissbildung",
        "name_de": "Cracking und Checking",
        "description": "Fine cracks or checks form in paint film, often in pattern",
        "cause": [
            "Excessive film thickness (brittleness)",
            "Substrate movement (flex, vibration)",
            "Temperature cycling stress",
            "UV degradation over time",
            "Incompatible coating over previous paint",
            "Loss of flexibility in aging paint",
        ],
        "prevention": [
            "Apply proper film thickness (multiple thin coats)",
            "Use flexible primers and topcoats",
            "Account for substrate movement in design",
            "Maintain surface flexibility (flexible epoxy)",
            "Use spar varnish with flexibility for bright work",
            "Match paint system to substrate flexibility needs",
        ],
        "repair_method": [
            "Sand smooth with P120-P150",
            "Apply flexible primer if substrate movement expected",
            "Recoat with flexible paint system",
            "For severe cracking: Strip entire area, start fresh",
        ],
        "severity": "structural_if_deep_water_ingress_risk",
        "substrate_movement_tolerance": "Flexible paints required for moving substrates",
    },

    "delamination_peeling": {
        "name": "Ablösung und Abblätterung",
        "name_de": "Delamination und Peeling",
        "description": "Paint lifts away from substrate or previous coat, flaking or peeling",
        "cause": [
            "Poor surface preparation (glossy surface not keyed)",
            "Incompatible paint systems",
            "Water or moisture behind coating",
            "Inadequate adhesion promoter",
            "Dirty or contaminated surface",
            "Substrate movement exceeds paint flexibility",
            "Poor primer adhesion",
        ],
        "prevention": [
            "Thorough sanding of old surface (P120 minimum)",
            "Degreasing and cleaning before painting",
            "Use primer compatible with both substrate and topcoat",
            "Allow proper curing between coats",
            "Moisture-free substrate before painting",
            "Test adhesion if uncertain (cross-cut adhesion test)",
        ],
        "repair_method": [
            "Remove all peeling paint (scrape or sand)",
            "Sand substrate smooth",
            "Apply primer to bare substrate",
            "Recoat with compatible paint system",
            "Feather edges of remaining good paint",
        ],
        "severity": "structural_affects_all_protection",
        "diagnostic_method": "Cross-cut adhesion test, pull-off adhesion test",
    },

    "wrinkling": {
        "name": "Faltenbildung",
        "name_de": "Wrinkling",
        "description": "Wrinkled or corrugated surface pattern appears during or after cure",
        "cause": [
            "Excessive film thickness (outer surface skins over while wet interior)",
            "Too much heat applied during cure",
            "Rapid surface cure with slow inner cure",
            "Incompatible reducer or thinner",
            "Applying over oily or waxed surface",
            "Reactive coatings applied too thick (2K epoxy, PU)",
        ],
        "prevention": [
            "Apply thin coats (multiple coats rather than thick single coat)",
            "Follow pot life and recoat windows",
            "Use proper reducer for temperature conditions",
            "Adequate surface preparation and degreasing",
            "Avoid excessive heat (oven cure)",
            "Stir 2K products thoroughly for even reaction",
        ],
        "repair_method": [
            "Sand wrinkled surface smooth (P120-P150)",
            "Remove worst wrinkles if severe",
            "Recoat with thin proper-viscosity coat",
            "Complete removal if severe throughout",
        ],
        "severity": "cosmetic_unless_structural_voids",
        "prevention_film_thickness_micron": 80,
    },

    "color_mismatch": {
        "name": "Farbabweichung",
        "name_de": "Color Mismatch",
        "description": "Applied color does not match reference or previous coat",
        "cause": [
            "Wrong paint code or batch",
            "Inadequate mixing (pigment settling)",
            "Tinting error (wrong pigment amount)",
            "Paint age degradation",
            "Application technique effects (spray vs brush)",
            "Lighting conditions at comparison",
            "Absorption differences in substrate",
        ],
        "prevention": [
            "Verify paint code before opening container",
            "Mix paint thoroughly before application",
            "Apply test coat on scrap or inconspicuous area",
            "Compare under consistent lighting",
            "Use same application method as reference",
            "Maintain consistent film thickness",
            "Request certified color match if custom tint",
        ],
        "repair_method": [
            "Light: Blend area by extending adjacent coat",
            "Moderate: Sand and recoat affected zone",
            "Severe: Strip color coat, repaint entire visible surface",
            "For metallic: Adjust angle viewing for best match",
        ],
        "severity": "cosmetic",
        "quality_assurance": "Color matching standard: Delta E < 2",
    },

    "dust_inclusions": {
        "name": "Staubeinschlüsse",
        "name_de": "Dust Inclusions",
        "description": "Dust particles embedded in wet paint film",
        "cause": [
            "Inadequate surface cleaning before painting",
            "Tack rag not used before application",
            "Dust in spray booth or application area",
            "Poor ventilation causing dust circulation",
            "Painting on windy day outdoors",
            "Inadequate drying/curing environment",
        ],
        "prevention": [
            "Final tack rag wipe immediately before painting",
            "Clean spray booth before use",
            "Block area from air flow during curing",
            "Paint in calm, low-dust environment",
            "Vacuum surface thoroughly before tacking",
            "Use air-curtained booth if available",
        ],
        "repair_method": [
            "Remove visible dust while paint wet (pick out with tweezers)",
            "Light sanding (P320-P500) if cured, seal with topcoat",
            "Sand smooth (P180), apply fresh coat if severe",
            "Multiple small dust inclusions: Polish and buff after cure",
        ],
        "severity": "cosmetic",
        "detectability": "Visible under raking light, tactile roughness",
    },

    "solvent_popping": {
        "name": "Lösemittelpopping",
        "name_de": "Solvent Popping",
        "description": "Bubbles or voids form during cure as trapped solvent escapes",
        "cause": [
            "Paint applied too thick (solvent can't escape)",
            "Excessive reducer/thinner",
            "Solvent evaporation trapped by skin forming",
            "High temperature accelerating evaporation",
            "Low humidity preventing slow evaporation",
            "Second coat applied over uncured first coat",
        ],
        "prevention": [
            "Apply thin coats with adequate recoat window",
            "Use proper reducer ratio (follow label)",
            "Paint in temperature range 18-25°C",
            "Maintain humidity 50-75%",
            "Allow full cure between coats",
            "Avoid excessive airflow during initial cure",
        ],
        "repair_method": [
            "Sand affected area smooth (P150-P220)",
            "Fill pops if deep with primer",
            "Recoat with thin proper-viscosity coat",
            "If widespread: Remove and restart",
        ],
        "severity": "cosmetic_unless_deep_voids",
    },

    "overspray": {
        "name": "Sprühnebel",
        "name_de": "Overspray",
        "description": "Fine paint mist lands on unintended areas",
        "cause": [
            "Inadequate masking or protection",
            "Spray gun angle too wide",
            "Spray pressure too high",
            "Application distance too far",
            "Wind or air movement spreading mist",
        ],
        "prevention": [
            "Proper masking with tape and protective sheeting",
            "Adjust spray gun for narrow precise pattern",
            "Reduce pressure if overspray excessive",
            "Maintain proper gun distance (25cm HVLP, 30cm airless)",
            "Paint in still air conditions",
        ],
        "repair_method": [
            "Dry overspray: Brush or wipe off before dry",
            "Cured overspray: Wet sand with fine paper, compound and polish",
            "Extensive: Strip area and repaint",
        ],
        "severity": "cosmetic",
    },

    "curtaining": {
        "name": "Vorhangbildung",
        "name_de": "Curtaining",
        "description": "Paint hangs down in curtain-like waves on vertical surfaces",
        "cause": [
            "Excessive paint application",
            "Gun too close, too slow, or too much trigger",
            "Paint too thin viscosity",
            "Vertical surface application",
            "Temperature too low (slow cure)",
        ],
        "prevention": [
            "Apply thin coats",
            "Proper spray technique (trigger control)",
            "Maintain proper gun distance",
            "Correct viscosity for conditions",
            "Paint near-horizontal surfaces before vertical",
            "Adequate temperature and airflow",
        ],
        "repair_method": [
            "While wet: Feather with brush or solvent wipe",
            "Cured: Sand smooth, reapply thin coat",
            "Severe: Strip section and restart",
        ],
        "severity": "cosmetic_or_structural_if_very_thick",
    },

    "crazing": {
        "name": "Netzrissbildung",
        "name_de": "Crazing",
        "description": "Fine network cracks appear, resembling alligator skin (but finer)",
        "cause": [
            "Incompatible paint layers (different chemistry)",
            "Old brittlε paint under flexible new paint",
            "Stress and substrate movement",
            "Age-related embrittlement",
        ],
        "prevention": [
            "Sand old paint thoroughly before recoating",
            "Use compatible paint systems",
            "Provide flexibility with primers designed for adhesion",
            "Replace old brittle paint with modern flexible systems",
        ],
        "repair_method": [
            "Complete removal of old paint if underlying cause",
            "Apply flexible primer before new topcoat",
            "Sand smooth and recoat",
        ],
        "severity": "structural_indicates_adhesion_failure",
    },

    "rust_bleed_through": {
        "name": "Rostdurchschlag",
        "name_de": "Rust Bleed Through",
        "description": "Rust staining appears through paint film",
        "cause": [
            "Inadequate rust removal before painting",
            "Rust continues under coating (moisture ingress)",
            "No primer or rust converter applied",
            "Moisture reaching unprotected substrate",
            "Flash rust during/after surface prep",
        ],
        "prevention": [
            "Complete rust removal (SA 2.5 blast ideal)",
            "Apply epoxy primer immediately after prep",
            "Use rust converter on pitted surface",
            "Avoid moisture exposure during application",
            "High-build epoxy as barrier coat",
            "Adequate topcoat coverage",
        ],
        "repair_method": [
            "Sand to reveal rust extent",
            "Remove rust (grinding, blasting, rust converter)",
            "Apply epoxy primer",
            "Recoat with topcoat",
            "For extensive rust: Strip entire area, restart with rust removal",
        ],
        "severity": "structural_affects_corrosion_protection",
    },
}

# ============================================================================
# MEASUREMENT METHODS
# ============================================================================

MEASUREMENT_METHODS = {
    "wet_film_gauge": {
        "name": "Wet Film Thickness Gauge",
        "name_de": "Nassfilm-Dickenmesser",
        "standard": "ISO 2808:2007",
        "description": "Measures coating thickness immediately after application, before drying",
        "how_to_use": [
            "Apply paint to surface",
            "Before paint skins over or flows, press gauge into wet film",
            "Read measurement directly on gauge scale",
            "Record multiple measurements across surface",
            "Typical 5-10 measurements per area",
        ],
        "gauge_types": [
            "Comb gauge: Teeth of different lengths, visual match",
            "Wheel gauge: Rolling wheel with notches, feel and visual",
        ],
        "pass_fail_criteria": {
            "wet_film_requirement": "Maintain target wet film +/- 10%",
            "example_target": "150 micron ± 15 micron WFT range = 135-165 micron",
        },
        "frequency": "Every coat application",
        "accuracy_micron": 5,
        "limitations": "Can only measure until paint becomes tacky, not after skin-over",
    },

    "dry_film_gauge": {
        "name": "Dry Film Thickness Gauge",
        "name_de": "Trockenfilm-Dickenmesser",
        "standard": "ISO 2808:2007",
        "description": "Measures cured paint thickness using magnetic or electronic methods",
        "gauge_types": {
            "magnetic_induction": {
                "method": "Magnetic probe attracts to steel substrate",
                "suitable_for": "Steel substrates, ferrous metals",
                "accuracy_micron": 5,
            },
            "electronic_eddy_current": {
                "method": "Eddy current probe, electromagnetic induction",
                "suitable_for": "All substrates (aluminum, fiberglass, stainless)",
                "accuracy_micron": 3,
            },
        },
        "how_to_use": [
            "Ensure coating fully cured",
            "Place gauge probe perpendicular to surface",
            "Press firmly until reading stabilizes",
            "Record measurement on display",
            "Typical 10-20 measurements per 10 sqm",
        ],
        "pass_fail_criteria": {
            "minimum_dft": "Achieve target minimum (system dependent)",
            "maximum_dft": "Not exceed manufacturer maximum",
            "uniformity": "DFT variation < 20% across surface",
            "example": "Target 180 micron ±10% = 162-198 micron acceptable",
        },
        "frequency": "After each coat cures, final inspection",
        "measurement_locations": [
            "High points (peaks)",
            "Low points (valleys)",
            "Representative average areas",
        ],
        "common_errors": [
            "Measuring while paint still curing (false readings)",
            "Not perpendicular probe placement",
            "Substrate thickness variation affecting reading",
        ],
    },

    "adhesion_cross_cut": {
        "name": "Adhesion Cross-Cut Test",
        "name_de": "Kreuzhaftungsprüfung",
        "standard": "ISO 2409",
        "description": "Mechanical adhesion test by making cross-cuts and tape pull",
        "equipment": [
            "Cross-cut tool (6 cuts vertical, 6 cuts horizontal, 1mm spacing)",
            "Adhesive tape (standard test tape)",
        ],
        "how_to_use": [
            "Make vertical cuts with cross-cut tool across coating",
            "Make horizontal cuts perpendicular at same spacing",
            "Ensure cuts reach substrate",
            "Apply adhesive tape over cross-cut pattern",
            "Press tape firmly with rigid blade",
            "Pull tape at 180 degrees briskly",
            "Examine pattern for coating removal",
        ],
        "pass_fail_criteria": {
            "rating_scale": "0-5",
            "5": "No removal of coating (excellent adhesion)",
            "4": "Small flakes removed at intersections only",
            "3": "Strips of coating lifted (acceptable for primers)",
            "2": "Multiple strips removed (poor adhesion)",
            "1": "Majority of coating removed (failure)",
            "0": "Complete removal (complete failure)",
            "acceptable_minimum_topcoat": "Rating 4 minimum",
            "acceptable_minimum_primer": "Rating 3 minimum",
        },
        "frequency": "Every coat application, final inspection",
        "standard_reference": "ISO 2409:2020",
    },

    "adhesion_pull_off": {
        "name": "Pull-Off Adhesion Test",
        "name_de": "Reißfestigkeitsprüfung",
        "standard": "ISO 4624",
        "description": "Destructive test measuring adhesion force by pulling dolly from surface",
        "equipment": [
            "Pull-off adhesion tester (mechanical or digital)",
            "Test dollies (metal cylinders, typically 20-50mm diameter)",
            "Epoxy adhesive (to bond dolly to coating)",
        ],
        "how_to_use": [
            "Glue test dolly to coating surface with epoxy",
            "Allow epoxy to cure (typically 24 hours)",
            "Mount dolly in pull-off tester",
            "Apply perpendicular pulling load at controlled rate",
            "Record maximum force at failure",
            "Calculate adhesion value: Force (N) / Dolly area (mm²) = MPa",
        ],
        "pass_fail_criteria": {
            "minimum_adhesion_mpa": 1.5,
            "excellent_adhesion": "> 3.0 MPa",
            "good_adhesion": "1.5 - 3.0 MPa",
            "poor_adhesion": "< 1.5 MPa",
        },
        "frequency": "Quality control, problem diagnosis, acceptance testing",
        "standard_reference": "ISO 4624:2016",
        "measurement_locations": "Minimum 3 test points per area",
    },

    "gloss_meter": {
        "name": "Gloss Meter",
        "name_de": "Glanzmeßgerät",
        "standard": "ISO 2813",
        "description": "Measures surface gloss by specular reflection",
        "gloss_scale": {
            "60_degree": "Standard measurement angle for most surfaces",
            "20_degree": "High-gloss surfaces (>70 gloss units)",
            "85_degree": "Low-gloss surfaces (<10 gloss units)",
        },
        "how_to_use": [
            "Calibrate meter on standard black glass reference",
            "Place meter perpendicular to surface",
            "Hold firmly without pressing hard",
            "Trigger measurement",
            "Record gloss units",
            "Take 3-5 measurements per area",
        ],
        "pass_fail_criteria": {
            "high_gloss": "> 70 gloss units at 60 degrees",
            "medium_gloss": "30-70 gloss units",
            "low_gloss_satin": "10-30 gloss units",
            "matte": "< 10 gloss units",
            "typical_specification": "70 ± 5 gloss units for marine topcoat",
        },
        "frequency": "Quality acceptance, specification compliance",
        "standard_reference": "ISO 2813:2014",
    },

    "dew_point_calculator": {
        "name": "Dew Point Calculator / Meter",
        "name_de": "Taupunkt-Hygrometer",
        "standard": "ISO 8502-2",
        "description": "Measures surface temperature vs air temperature/humidity to determine condensation risk",
        "critical_parameter": "Substrate must be 3-5°C warmer than dew point to prevent moisture condensation",
        "how_to_use": [
            "Measure ambient temperature and humidity",
            "Measure substrate surface temperature",
            "Calculate dew point using psychrometric chart or calculator",
            "Verify substrate temperature > dew point + 3°C minimum",
            "Delay painting if substrate too cold",
        ],
        "example": {
            "ambient_temperature_c": 20,
            "ambient_humidity_pct": 75,
            "dew_point_calculated_c": 15,
            "substrate_required_minimum_c": 18,
            "substrate_actual_c": 14,
            "result": "DO NOT PAINT - substrate below minimum, risk of moisture condensation",
        },
        "critical_importance": "Most common cause of coating failure in marine applications",
        "frequency": "Before every application, continuous during application",
        "standard_reference": "ISO 8502-2:2005",
    },

    "surface_profile_measurement": {
        "name": "Surface Profile / Roughness Measurement",
        "name_de": "Oberflächenrauheit / Rauhtiefe",
        "standard": "ISO 19927-2",
        "description": "Measures peak-to-valley height of blasted surface profile",
        "purpose": "Ensures adequate surface anchoring for adhesion",
        "measurement_methods": {
            "replica_tape": {
                "method": "Press profile replica tape to blasted surface, measure tape thickness increase",
                "accuracy": "Moderate",
                "cost": "Low",
            },
            "stylus_profilometer": {
                "method": "Electronic device draws stylus across surface measuring peaks and valleys",
                "accuracy": "High",
                "cost": "High",
            },
        },
        "target_values": {
            "abrasive_blast_sa25": "2.5 micron Ra",
            "abrasive_blast_sa3": "3.5 micron Ra",
            "acceptable_range": "+/- 0.5 micron",
        },
        "why_important": "Rough profile anchors paint, prevents peeling and adhesion failure",
        "too_smooth_problem": "Glossy blasted surface may have poor adhesion",
        "too_rough_problem": "Excessive roughness may trap air (pinhole defects)",
        "frequency": "After blasting, before priming",
        "standard_reference": "ISO 19927-2:2018",
    },
}

# ============================================================================
# POLISHING AND COMPOUNDING — Polieren und Compoundieren
# ============================================================================

POLISHING_SYSTEMS = {
    "compound_heavy_cut": {
        "name_de": "Schleifpaste grob (Heavy Cut)",
        "abrasive_grade": "P1000-P1500 Äquivalent",
        "use": "Entfernung von Kratzern, Orangenhaut, Läufer nach Lackierung",
        "application": "Exzenter-Poliermaschine, 1000-1500 U/min",
        "brands": ["Menzerna 400 Heavy Cut", "3M Perfect-It III Rubbing Compound"],
        "pad": "Wollpad oder Schaumpad (gelb/orange)",
    },
    "compound_medium_cut": {
        "name_de": "Polierpaste mittel (Medium Cut)",
        "abrasive_grade": "P2000-P3000 Äquivalent",
        "use": "Hologramm-Entfernung nach Grobpolitur, mittlere Kratzer",
        "application": "Exzenter-Poliermaschine, 800-1200 U/min",
        "pad": "Schaumpad (weiß)",
    },
    "finish_polish": {
        "name_de": "Hochglanzpolitur (Finish)",
        "abrasive_grade": "Ultra-fein, keine sichtbaren Kratzer",
        "use": "Spiegelglanz-Finish auf 2K-PU-Lack",
        "brands": ["Menzerna Super Finish 3500", "3M Ultrafina SE"],
        "pad": "Schwarzer Schaumpad (ultra-weich)",
    },
    "wax_protection": {
        "name_de": "Bootsschutzwachs",
        "types": {
            "carnauba": "Natürliches Hartwachs — höchster Glanz, 2-3 Monate Haltbarkeit",
            "polymer_sealant": "Synthetischer Versiegeler — 4-6 Monate Haltbarkeit",
            "ceramic_coating": "Keramikversiegelung (SiO2) — 1-2 Jahre, hydrophob",
        },
        "application_sequence": "Nach Politur: Wachs/Versiegelung innerhalb 24h auftragen",
    },
}

# ============================================================================
# WRAPPING / FOLIENBESCHICHTUNG
# ============================================================================

FOIL_WRAPPING = {
    "cast_vinyl": {
        "name_de": "Gegossene Vinylfolie (Cast)",
        "thickness_um": 50,
        "conformability": "hoch — passt sich Wölbungen und Sicken an",
        "durability_years": "5-7 (Marinebereich: 3-5)",
        "brands": ["3M 1080/2080 Marine", "Avery Supreme Wrapping Film"],
        "surface_prep": "Reinigen, Entfetten (IPA), bei Bedarf Primer auf schwierigen Stellen",
        "temperature_application_c": "18-25 (nicht unter 15°C)",
        "post_heat_c": 90,
        "use": "Rumpf-Folierung als Lack-Alternative, Akzentstreifen, Wasserpass",
    },
    "print_wrap": {
        "name_de": "Bedruckte Bootsbeschriftung",
        "material": "Gegossene Vinylfolie mit UV-Tintendruck",
        "laminate": "Klarlaminat zum Schutz des Druckbilds (Matt oder Glanz)",
        "use": "Bootsnamen, Registrierung, Werbung, Dekor",
    },
}

# ============================================================================
# ANODIZING AND GALVANIZING — Anodisierung, Verzinkung
# ============================================================================

METAL_SURFACE_TREATMENTS = {
    "anodizing_aluminium": {
        "name_de": "Eloxierung (Anodisierung) Aluminium",
        "process": "Elektrolytische Oxidation in Schwefelsäure",
        "layer_thickness_um": {"standard": 15, "hard_anodize": 50},
        "color_options": ["natur (silber)", "schwarz", "bronze", "blau", "rot"],
        "marine_note": "Standard-Eloxal ist NICHT seewasserfest — Hart-Eloxal (Typ III) oder Versiegeln mit heißem Wasser",
        "typical_parts": ["Mastprofil", "Baumprofil", "Beschläge", "Lüftergitter"],
    },
    "hot_dip_galvanizing": {
        "name_de": "Feuerverzinkung",
        "process": "Eintauchen in Zinkschmelze bei 450°C",
        "layer_thickness_um": "50-100",
        "durability_years_marine": "5-15 (Seewasser), 20-40 (Süßwasser)",
        "typical_parts": ["Ankerketten", "Anker", "Bugbeschläge (einfache Boote)", "Trailer-Teile"],
        "warning": "Verzinkter Stahl + Edelstahl = galvanische Korrosion! Nicht kombinieren.",
    },
    "powder_coating": {
        "name_de": "Pulverbeschichtung",
        "process": "Elektrostatisch aufgeladenes Pulver, eingebrannt bei 160-200°C",
        "layer_thickness_um": "60-120",
        "typical_parts": ["Bimini-Rahmen", "Geräteträger", "Davits", "Relingsstützen (einfache Boote)"],
        "marine_suitability": "Gut als UV-Schutz, aber bei Beschädigung lokale Korrosion unter Schicht",
        "note": "Nur auf Aluminium oder Stahl — nicht auf GFK",
    },
}

# ============================================================================
# ASSESSMENT FUNCTION
# ============================================================================

def assess_coating_system(system_id, zone, boat_class, environmental_conditions=None):
    """
    Assess suitability of coating system for specific application.

    Args:
        system_id: Key from PAINT_SYSTEMS dict
        zone: Application zone ('above_waterline', 'below_waterline', etc.)
        boat_class: Boat classification ('cruiser', 'racing', 'superyacht', etc.)
        environmental_conditions: Optional dict with exposure data
            - climate: 'temperate', 'tropical', 'arctic'
            - uv_exposure: 'high', 'moderate', 'low'
            - salt_spray: True/False
            - freshwater: True/False

    Returns:
        dict with:
            - suitability_score: 0-100
            - findings: list of assessment points
            - recommendations: list of recommendations
            - warnings: list of cautions
            - alternate_systems: list of alternative system IDs
    """

    if system_id not in PAINT_SYSTEMS:
        return {
            "error": f"System {system_id} not found",
            "suitability_score": 0,
        }

    system = PAINT_SYSTEMS[system_id]
    score = 100
    findings = []
    warnings = []
    recommendations = []

    # Check zone compatibility
    if zone in system.get("application_zone", []):
        findings.append(f"System approved for {zone} application")
    else:
        score -= 30
        warnings.append(f"System not recommended for {zone} - designed for {system['application_zone']}")

    # Check boat class compatibility
    if boat_class in system.get("boat_class_suitable", []):
        findings.append(f"Suitable for {boat_class} class vessels")
    else:
        score -= 20
        warnings.append(f"System not tested for {boat_class} class")

    # Environmental assessment
    if environmental_conditions:
        if environmental_conditions.get("uv_exposure") == "high":
            if system_id in ["two_pack_polyurethane_above_wl", "varnish_2k_polyurethane"]:
                findings.append("Excellent UV resistance for high-exposure areas")
            elif system_id in ["alkyd_enamel_traditional"]:
                score -= 15
                warnings.append("Alkyd enamel limited UV resistance - consider 2K PU")

        if environmental_conditions.get("salt_spray"):
            if "epoxy" in system_id or "barrier" in system_id:
                findings.append("Excellent salt spray protection with epoxy base")
            elif "antifouling" in system_id:
                findings.append("Biocide protection against marine organisms")

        climate = environmental_conditions.get("climate", "temperate")
        if climate == "tropical" and system.get("temperature_range_c"):
            if system["temperature_range_c"][1] < 30:
                score -= 10
                warnings.append(f"Temperature range {system['temperature_range_c']}°C may be marginal for tropical")

    # Cost vs durability analysis
    durability = system.get("durability_years", 0)
    cost_rating = system.get("cost_rating", 3)
    value_ratio = durability / cost_rating if cost_rating > 0 else 0

    if value_ratio > 1.5:
        findings.append(f"Good value: {durability} years durability at cost rating {cost_rating}/5")
    elif value_ratio < 0.7:
        findings.append(f"Premium cost: {durability} years durability at cost rating {cost_rating}/5")

    # Durability recommendation
    if durability < 3:
        recommendations.append("Consider higher-durability system for critical applications")
    elif durability >= 5:
        findings.append(f"Long-term protection ({durability} years expected lifespan)")

    # Surface prep complexity
    surface_prep_steps = len(system.get("surface_prep", []))
    if surface_prep_steps > 5:
        recommendations.append("Extensive surface preparation required - allocate adequate time and labor")

    # Application method notes
    app_method = system.get("application_method", {}).get("primary")
    if app_method == "airless_spray":
        recommendations.append("Airless spray equipment required - ensure proper setup and operator training")
    elif app_method == "hvlp_spray":
        recommendations.append("HVLP spray system needed for quality finish - ensure adequate air supply")
    elif app_method == "brush_natural":
        recommendations.append("Requires skill with natural bristle brush technique for quality result")

    # Ensure score stays 0-100
    score = max(0, min(100, score))

    return {
        "system_id": system_id,
        "system_name": system.get("name", system_id),
        "zone": zone,
        "boat_class": boat_class,
        "suitability_score": score,
        "durability_years": durability,
        "cost_rating": cost_rating,
        "total_dft_micron": system.get("total_dft_micron"),
        "findings": findings,
        "recommendations": recommendations,
        "warnings": warnings,
        "critical_factors": {
            "temperature_range_c": system.get("temperature_range_c"),
            "humidity_max_pct": system.get("humidity_max_pct"),
            "dew_point_margin_c": system.get("dew_point_margin_c"),
        },
    }
