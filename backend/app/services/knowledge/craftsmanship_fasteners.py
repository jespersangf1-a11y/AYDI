"""
Exhaustive fastener, hardware, and mechanical connection knowledge base
for marine/yacht applications. Master yacht rigger and marine engineer perspective.

Alle Datenstrukturen in Deutsch für AYDI-System.
Code comments in English.
"""

# ==============================================================================
# 1. MARINE_FASTENERS - Comprehensive fastener specifications
# ==============================================================================

MARINE_FASTENERS = {
    "machine_screw_316": {
        "name": "Maschinengewinde-Schraube 316er Edelstahl",
        "material": "Stainless Steel 316",
        "grade_standard": "A4-70 / DIN 912",
        "sizes_available": ["M3", "M4", "M5", "M6", "M8", "M10", "M12", "M16"],
        "tensile_strength_mpa": 700,
        "shear_strength_mpa": 560,
        "suitable_for": [
            "deck_hardware_fastening",
            "portlight_frames",
            "interior_cabinetry",
            "electrical_terminal_blocks",
            "small_hardware_assembly",
            "teak_rail_attachment",
            "window_frame_assembly"
        ],
        "not_suitable_for": [
            "main_structural_loads",
            "mast_attachment",
            "keel_bolts",
            "rudder_bearing_plates",
            "high_vibration_areas"
        ],
        "galvanic_compatibility": {
            "copper_alloys": "excellent",
            "aluminium": "use_isolation",
            "carbon_steel": "excellent",
            "bronze": "excellent",
            "nickel_alloys": "excellent"
        },
        "torque_values_nm": {
            "M3": 0.6,
            "M4": 1.3,
            "M5": 2.5,
            "M6": 4.2,
            "M8": 10.0,
            "M10": 19.5,
            "M12": 34.0,
            "M16": 76.0
        },
        "pre_drill_sizes_mm": {
            "M3": 2.5,
            "M4": 3.3,
            "M5": 4.2,
            "M6": 5.0,
            "M8": 6.8,
            "M10": 8.5,
            "M12": 10.0,
            "M16": 14.0
        },
        "quality_criteria": {
            "head_seating": "must_be_flush",
            "thread_engagement_min_mm": 1.5,
            "washer_requirement": "optional_316_stainless",
            "sealant_requirement": "not_required",
            "galvanic_isolation": "recommended"
        },
        "common_failures": [
            "galling_under_assembly",
            "crevice_corrosion_in_clogged_threads",
            "hydrogen_embrittlement_rare",
            "fastener_loosening_vibration"
        ],
        "inspection_interval_months": 24
    },

    "self_tapping_316": {
        "name": "Selbstschneidende Schraube 316er Edelstahl",
        "material": "Stainless Steel 316",
        "grade_standard": "A4 / DIN 7981",
        "sizes_available": ["#10", "#12", "M4", "M5", "M6", "M8"],
        "tensile_strength_mpa": 650,
        "shear_strength_mpa": 520,
        "suitable_for": [
            "GRP_deck_fastening",
            "aluminium_trim_attachment",
            "thin_gauge_stainless_panels",
            "cabin_interior_assembly",
            "electrical_panel_mounting"
        ],
        "not_suitable_for": [
            "highly_stressed_structural_joints",
            "wooden_deck_primary_fastening",
            "repeated_assembly_disassembly",
            "high_vibration_environments"
        ],
        "galvanic_compatibility": {
            "GRP": "excellent",
            "aluminium": "use_isolation",
            "stainless_steel": "excellent",
            "bronze": "excellent"
        },
        "torque_values_nm": {
            "#10": 0.8,
            "#12": 1.2,
            "M4": 1.5,
            "M5": 2.3,
            "M6": 3.8,
            "M8": 8.5
        },
        "pre_drill_sizes_mm": {
            "#10": 2.4,
            "#12": 2.8,
            "M4": 3.0,
            "M5": 3.8,
            "M6": 4.5,
            "M8": 6.0
        },
        "quality_criteria": {
            "head_seating": "flat_washered",
            "thread_engagement_min_mm": 2.0,
            "washer_requirement": "required_stainless",
            "sealant_requirement": "optional_in_deck_applications",
            "substrate_thickness_min_mm": 1.5
        },
        "common_failures": [
            "stripping_in_soft_GRP",
            "corrosion_at_washline",
            "vibration_loosening",
            "galling_with_stainless_steel"
        ],
        "inspection_interval_months": 12
    },

    "wood_screw_316": {
        "name": "Holzschraube 316er Edelstahl",
        "material": "Stainless Steel 316",
        "grade_standard": "A4 / DIN 571",
        "sizes_available": ["#8", "#10", "#12", "5x50", "5x75", "6x80", "8x100"],
        "tensile_strength_mpa": 700,
        "shear_strength_mpa": 560,
        "suitable_for": [
            "teak_deck_fastening",
            "wooden_rail_mounting",
            "cabin_sole_fastening",
            "wooden_structural_members",
            "companionway_steps",
            "wooden_door_frame_assembly",
            "timber_stringer_attachment"
        ],
        "not_suitable_for": [
            "GRP_laminate_fastening",
            "aluminium_attachment",
            "high_vibration_areas",
            "moisture_sensitive_wood"
        ],
        "galvanic_compatibility": {
            "teak": "excellent",
            "oak": "excellent",
            "spruce": "excellent",
            "mahogany": "excellent",
            "iroko": "excellent"
        },
        "torque_values_nm": {
            "#8": 3.5,
            "#10": 5.5,
            "#12": 8.0,
            "5x50": 2.0,
            "5x75": 2.5,
            "6x80": 3.5,
            "8x100": 6.0
        },
        "pre_drill_sizes_mm": {
            "#8": 3.2,
            "#10": 4.0,
            "#12": 5.0,
            "5x50": 2.5,
            "5x75": 2.5,
            "6x80": 3.2,
            "8x100": 4.0
        },
        "quality_criteria": {
            "head_seating": "countersunk_flush",
            "thread_engagement_min_mm": 25,
            "washer_requirement": "not_required",
            "sealant_requirement": "optional_teak_sealing_compound",
            "wood_moisture_content": "8_to_12_percent"
        },
        "common_failures": [
            "wood_splitting_at_fastening",
            "fastener_loosening_wood_shrinkage",
            "corrosion_in_teak_tannic_acid",
            "head_stripping_over_torque"
        ],
        "inspection_interval_months": 6
    },

    "wood_screw_bronze": {
        "name": "Holzschraube Bronze",
        "material": "Bronze (Cu-Sn-Al)",
        "grade_standard": "Naval brass / DIN 1052",
        "sizes_available": ["#8", "#10", "#12", "5x50", "5x75", "6x80", "8x100"],
        "tensile_strength_mpa": 450,
        "shear_strength_mpa": 360,
        "suitable_for": [
            "wooden_deck_fastening_heritage",
            "teak_trim_assembly",
            "wooden_structural_fastening",
            "traditional_yacht_construction",
            "high_corrosion_environments",
            "traditional_cabin_assembly"
        ],
        "not_suitable_for": [
            "high_load_structures",
            "GRP_composite_fastening",
            "stainless_steel_adjacent"
        ],
        "galvanic_compatibility": {
            "teak": "excellent",
            "oak": "excellent",
            "copper_alloys": "excellent",
            "stainless_steel": "excellent",
            "aluminium": "avoid"
        },
        "torque_values_nm": {
            "#8": 2.5,
            "#10": 4.0,
            "#12": 6.0,
            "5x50": 1.5,
            "5x75": 2.0,
            "6x80": 2.8,
            "8x100": 4.5
        },
        "pre_drill_sizes_mm": {
            "#8": 3.2,
            "#10": 4.0,
            "#12": 5.0,
            "5x50": 2.5,
            "5x75": 2.5,
            "6x80": 3.2,
            "8x100": 4.0
        },
        "quality_criteria": {
            "head_seating": "countersunk_flush",
            "thread_engagement_min_mm": 25,
            "washer_requirement": "optional_bronze",
            "sealant_requirement": "teak_sealing_compound_recommended",
            "wood_moisture_content": "8_to_12_percent"
        },
        "common_failures": [
            "fastener_relaxation_bronze_creep",
            "head_corrosion_wood_acids",
            "wood_splitting",
            "lower_holding_force_than_stainless"
        ],
        "inspection_interval_months": 6
    },

    "through_bolt_316": {
        "name": "Durchgangsschraube 316er Edelstahl",
        "material": "Stainless Steel 316",
        "grade_standard": "A4-70 / DIN 933",
        "sizes_available": ["M6", "M8", "M10", "M12", "M16", "M20"],
        "tensile_strength_mpa": 700,
        "shear_strength_mpa": 560,
        "suitable_for": [
            "through_deck_fastening",
            "deck_hardware_major",
            "mast_step_mounting",
            "keel_bollard_attachment",
            "structural_member_connection",
            "chainplate_assembly",
            "pushpit_stanchion"
        ],
        "not_suitable_for": [
            "keel_bolts_primary",
            "rudder_shaft_coupling",
            "high_vibration_without_locking"
        ],
        "galvanic_compatibility": {
            "stainless_steel": "excellent",
            "bronze": "excellent",
            "copper_alloys": "excellent",
            "aluminium": "use_isolation",
            "mild_steel": "excellent"
        },
        "torque_values_nm": {
            "M6": 13.5,
            "M8": 32.0,
            "M10": 63.0,
            "M12": 110.0,
            "M16": 245.0,
            "M20": 475.0
        },
        "pre_drill_sizes_mm": {
            "M6": 6.5,
            "M8": 8.5,
            "M10": 10.5,
            "M12": 13.0,
            "M16": 17.0,
            "M20": 21.0
        },
        "quality_criteria": {
            "head_seating": "washer_required",
            "thread_engagement_min_mm": 1.5,
            "washer_requirement": "required_under_and_over",
            "sealant_requirement": "marine_sealant_deck_penetrations",
            "nut_locking": "nylon_insert_lock_nut_or_mechanical"
        },
        "common_failures": [
            "fastener_loosening_vibration",
            "crevice_corrosion_under_washer",
            "galvanic_corrosion_mixed_metals",
            "nut_backing_off"
        ],
        "inspection_interval_months": 12
    },

    "carriage_bolt_316": {
        "name": "Kutschenschraube 316er Edelstahl",
        "material": "Stainless Steel 316",
        "grade_standard": "A4 / DIN 603",
        "sizes_available": ["M6", "M8", "M10", "M12", "M16"],
        "tensile_strength_mpa": 700,
        "shear_strength_mpa": 560,
        "suitable_for": [
            "wooden_structure_fastening",
            "deck_rail_base_mounting",
            "coaming_attachment",
            "wooden_hatch_frame_assembly",
            "timber_structural_connection",
            "companionway_mounting"
        ],
        "not_suitable_for": [
            "GRP_laminate_fastening",
            "high_vibration_without_lock_washer",
            "highly_corrosive_bilge_areas"
        ],
        "galvanic_compatibility": {
            "wood": "excellent",
            "bronze": "excellent",
            "copper_alloys": "excellent",
            "stainless_steel": "excellent"
        },
        "torque_values_nm": {
            "M6": 12.0,
            "M8": 28.0,
            "M10": 55.0,
            "M12": 95.0,
            "M16": 220.0
        },
        "pre_drill_sizes_mm": {
            "M6": 6.5,
            "M8": 8.5,
            "M10": 10.5,
            "M12": 13.0,
            "M16": 17.0
        },
        "quality_criteria": {
            "head_seating": "flush_in_wood",
            "thread_engagement_min_mm": 25,
            "washer_requirement": "under_nut_only",
            "sealant_requirement": "optional_wood_sealing",
            "head_rotation_prevention": "square_neck_prevents_rotation"
        },
        "common_failures": [
            "nut_backing_off_vibration",
            "wood_swelling_loosening",
            "head_corrosion_wood_acids",
            "wood_splitting_at_head"
        ],
        "inspection_interval_months": 12
    },

    "u_bolt_316": {
        "name": "U-Schraube 316er Edelstahl",
        "material": "Stainless Steel 316",
        "grade_standard": "A4 / DIN 3570",
        "sizes_available": ["M8", "M10", "M12", "M16", "M20"],
        "tensile_strength_mpa": 700,
        "shear_strength_mpa": 560,
        "suitable_for": [
            "pulpit_stanchion_mounting",
            "pushpit_rail_attachment",
            "deck_tube_clamping",
            "pipe_clamp_fastening",
            "rigging_wire_clamp",
            "through_deck_cleat_mounting"
        ],
        "not_suitable_for": [
            "high_tension_rigging",
            "keel_bolts",
            "primary_structural_loads"
        ],
        "galvanic_compatibility": {
            "stainless_steel": "excellent",
            "bronze": "excellent",
            "mild_steel": "excellent"
        },
        "torque_values_nm": {
            "M8": 24.0,
            "M10": 48.0,
            "M12": 84.0,
            "M16": 189.0,
            "M20": 365.0
        },
        "pre_drill_sizes_mm": {
            "M8": 8.5,
            "M10": 10.5,
            "M12": 13.0,
            "M16": 17.0,
            "M20": 21.0
        },
        "quality_criteria": {
            "head_seating": "washer_required_both_sides",
            "thread_engagement_min_mm": 1.5,
            "washer_requirement": "required_under_nut",
            "sealant_requirement": "deck_penetration_sealant",
            "u_bolt_bend_radius": "must_be_smooth"
        },
        "common_failures": [
            "nut_loosening_vibration",
            "crevice_corrosion_under_washers",
            "bend_fracture_sharp_radius",
            "oversizing_clamped_tube"
        ],
        "inspection_interval_months": 6
    },

    "eye_bolt_316": {
        "name": "Augenschraube 316er Edelstahl",
        "material": "Stainless Steel 316",
        "grade_standard": "A4 / DIN 580",
        "sizes_available": ["M6", "M8", "M10", "M12", "M16"],
        "tensile_strength_mpa": 700,
        "shear_strength_mpa": 560,
        "suitable_for": [
            "deck_lifting_eye",
            "rigging_attachment_point",
            "halyards_hook_attachment",
            "pulley_mounting",
            "safety_line_attachment",
            "deck_pad_eye_assembly"
        ],
        "not_suitable_for": [
            "rotating_under_load",
            "primary_sail_control",
            "mast_attachment"
        ],
        "galvanic_compatibility": {
            "bronze": "excellent",
            "stainless_steel": "excellent",
            "copper_alloys": "excellent"
        },
        "torque_values_nm": {
            "M6": 13.5,
            "M8": 32.0,
            "M10": 63.0,
            "M12": 110.0,
            "M16": 245.0
        },
        "pre_drill_sizes_mm": {
            "M6": 6.5,
            "M8": 8.5,
            "M10": 10.5,
            "M12": 13.0,
            "M16": 17.0
        },
        "quality_criteria": {
            "head_seating": "washer_required",
            "thread_engagement_min_mm": 1.5,
            "washer_requirement": "required_under_eye",
            "sealant_requirement": "deck_penetration_sealant",
            "eye_alignment": "load_direction_verified"
        },
        "common_failures": [
            "eye_bending_overload",
            "fastener_loosening_cyclic_load",
            "crevice_corrosion",
            "eye_rotation_under_load"
        ],
        "inspection_interval_months": 6
    },

    "hanger_bolt": {
        "name": "Hängerschraube",
        "material": "Stainless Steel 316 or Zinc Plated",
        "grade_standard": "A4 or DIN 3573",
        "sizes_available": ["M8", "M10", "M12", "M16"],
        "tensile_strength_mpa": 700,
        "shear_strength_mpa": 560,
        "suitable_for": [
            "suspended_cabin_equipment",
            "engine_mount_anchor",
            "through_deck_heavy_item_mounting",
            "bilge_pump_mounting",
            "tankage_suspension"
        ],
        "not_suitable_for": [
            "primary_structural_bearing",
            "repeated_assembly_disassembly"
        ],
        "galvanic_compatibility": {
            "stainless_steel": "excellent",
            "bronze": "excellent"
        },
        "torque_values_nm": {
            "M8": 32.0,
            "M10": 63.0,
            "M12": 110.0,
            "M16": 245.0
        },
        "pre_drill_sizes_mm": {
            "M8": 8.5,
            "M10": 10.5,
            "M12": 13.0,
            "M16": 17.0
        },
        "quality_criteria": {
            "head_seating": "washer_required",
            "thread_engagement_min_mm": 2.0,
            "washer_requirement": "required_above_and_below",
            "sealant_requirement": "optional_thread_sealant",
            "suspension_bracket_contact": "full_bearing_surface"
        },
        "common_failures": [
            "nut_backing_off_vibration",
            "shank_bending_dynamic_load",
            "crevice_corrosion"
        ],
        "inspection_interval_months": 6
    },

    "lag_bolt_316": {
        "name": "Lagerschraube 316er Edelstahl",
        "material": "Stainless Steel 316",
        "grade_standard": "A4 / DIN 571",
        "sizes_available": ["6x60", "8x80", "10x100", "12x120", "16x160"],
        "tensile_strength_mpa": 700,
        "shear_strength_mpa": 560,
        "suitable_for": [
            "through_deck_structural_fastening",
            "mast_step_mounting",
            "keel_structure_attachment",
            "cabin_sole_main_fastening",
            "timber_to_timber_structural_connection"
        ],
        "not_suitable_for": [
            "primary_keel_bolts",
            "rudder_assembly",
            "high_vibration_areas"
        ],
        "galvanic_compatibility": {
            "wood": "excellent",
            "bronze": "excellent",
            "stainless_steel": "excellent"
        },
        "torque_values_nm": {
            "6x60": 4.0,
            "8x80": 8.0,
            "10x100": 14.0,
            "12x120": 22.0,
            "16x160": 48.0
        },
        "pre_drill_sizes_mm": {
            "6x60": 4.0,
            "8x80": 5.5,
            "10x100": 7.0,
            "12x120": 8.5,
            "16x160": 11.0
        },
        "quality_criteria": {
            "head_seating": "washer_required_penetration",
            "thread_engagement_min_mm": 30,
            "washer_requirement": "required_large_diameter",
            "sealant_requirement": "teak_sealing_compound",
            "wood_fiber_direction": "perpendicular_optimal"
        },
        "common_failures": [
            "fastener_loosening_wood_shrinkage",
            "head_corrosion_wood_acids",
            "wood_splitting_installation",
            "washout_under_head"
        ],
        "inspection_interval_months": 6
    },

    "rivets_monel_blind": {
        "name": "Blindniete Monel",
        "material": "Monel 400 (Ni-Cu)",
        "grade_standard": "ASTM B 316",
        "sizes_available": ["3.2x6", "3.2x9", "4.0x10", "4.0x12", "5.0x14", "5.0x16"],
        "tensile_strength_mpa": 580,
        "shear_strength_mpa": 465,
        "suitable_for": [
            "aluminium_hull_fastening",
            "GRP_sandwich_core_fastening",
            "trim_fastening_aluminium_spars",
            "deck_hardware_light_fastening",
            "non_removable_permanent_joints"
        ],
        "not_suitable_for": [
            "high_load_structural_joints",
            "removable_disassembly_applications",
            "primary_rigging_attachment"
        ],
        "galvanic_compatibility": {
            "aluminium": "excellent",
            "GRP": "excellent",
            "stainless_steel": "excellent",
            "bronze": "excellent"
        },
        "torque_values_nm": {
            "blind_rivet": "not_applicable_permanent"
        },
        "pre_drill_sizes_mm": {
            "3.2x6": 3.3,
            "3.2x9": 3.3,
            "4.0x10": 4.1,
            "4.0x12": 4.1,
            "5.0x14": 5.1,
            "5.0x16": 5.1
        },
        "quality_criteria": {
            "installation_tool": "pneumatic_hand_riveter_required",
            "mandrel_break_point": "verified_break",
            "shop_head_formation": "1.5x_to_2x_original_diameter",
            "sealant_requirement": "sealant_in_hole_before_installation",
            "no_re_fastening": "permanent_assembly"
        },
        "common_failures": [
            "insufficient_mandrel_closure",
            "hole_enlargement_vibration",
            "corrosion_around_blind_section",
            "pull_out_under_shear_load"
        ],
        "inspection_interval_months": 36
    },

    "rivets_aluminium": {
        "name": "Blindniete Aluminium",
        "material": "Aluminium 1100 or 5005",
        "grade_standard": "ASTM B 316",
        "sizes_available": ["2.4x6", "3.2x6", "3.2x9", "4.0x10", "4.0x12"],
        "tensile_strength_mpa": 220,
        "shear_strength_mpa": 180,
        "suitable_for": [
            "light_interior_trim_fastening",
            "non_structural_GRP_fastening",
            "cabin_panel_attachment_light",
            "non_load_bearing_joints"
        ],
        "not_suitable_for": [
            "deck_fastening",
            "structural_connections",
            "any_high_load_application",
            "marine_corrosive_environments"
        ],
        "galvanic_compatibility": {
            "aluminium": "excellent",
            "GRP": "acceptable"
        },
        "torque_values_nm": {
            "blind_rivet": "not_applicable_permanent"
        },
        "pre_drill_sizes_mm": {
            "2.4x6": 2.5,
            "3.2x6": 3.3,
            "3.2x9": 3.3,
            "4.0x10": 4.1,
            "4.0x12": 4.1
        },
        "quality_criteria": {
            "installation_tool": "hand_rivet_tool_acceptable",
            "mandrel_break_point": "verified_break",
            "shop_head_formation": "1.5x_to_2x_original_diameter",
            "sealant_requirement": "sealant_below_waterline_critical",
            "no_re_fastening": "permanent_assembly"
        },
        "common_failures": [
            "rivet_fracture_excessive_force",
            "insufficient_grip_length",
            "corrosion_perforation",
            "pull_out_underload"
        ],
        "inspection_interval_months": 24
    },

    "rivets_stainless": {
        "name": "Blindniete Edelstahl 316",
        "material": "Stainless Steel 316",
        "grade_standard": "ASTM B 565",
        "sizes_available": ["3.2x9", "4.0x10", "4.0x12", "5.0x14", "5.0x16"],
        "tensile_strength_mpa": 620,
        "shear_strength_mpa": 495,
        "suitable_for": [
            "deck_trim_fastening",
            "stainless_structural_riveting",
            "high_visibility_deck_hardware",
            "GRP_deck_fastening",
            "trim_fastening_permanent"
        ],
        "not_suitable_for": [
            "removable_disassembly_applications",
            "primary_load_bearing_structure",
            "mast_attachment"
        ],
        "galvanic_compatibility": {
            "stainless_steel": "excellent",
            "bronze": "excellent",
            "GRP": "excellent"
        },
        "torque_values_nm": {
            "blind_rivet": "not_applicable_permanent"
        },
        "pre_drill_sizes_mm": {
            "3.2x9": 3.3,
            "4.0x10": 4.1,
            "4.0x12": 4.1,
            "5.0x14": 5.1,
            "5.0x16": 5.1
        },
        "quality_criteria": {
            "installation_tool": "pneumatic_riveter_required",
            "mandrel_break_point": "verified_break",
            "shop_head_formation": "1.5x_to_2x_original_diameter",
            "sealant_requirement": "marine_sealant_critical",
            "corrosion_resistance": "superior_to_monel"
        },
        "common_failures": [
            "mandrel_pull_out_insufficient_force",
            "hole_enlargement",
            "crevice_corrosion_rare",
            "brittle_failure_cold_working"
        ],
        "inspection_interval_months": 36
    },

    "threaded_insert_helicoil": {
        "name": "Gewindeinsatz Helicoil 316er",
        "material": "Stainless Steel 316 Helical Insert",
        "grade_standard": "DIN 910 / ISO 13753",
        "sizes_available": ["M3", "M4", "M5", "M6", "M8", "M10", "M12", "M16"],
        "tensile_strength_mpa": 700,
        "shear_strength_mpa": 560,
        "suitable_for": [
            "stripped_GRP_thread_repair",
            "aluminium_thread_reinforcement",
            "high_removal_frequency_applications",
            "cabin_hardware_repeated_assembly",
            "trim_fastening_repair"
        ],
        "not_suitable_for": [
            "one_time_fastening",
            "primary_structural_loads",
            "safety_critical_rigging"
        ],
        "galvanic_compatibility": {
            "stainless_steel": "excellent",
            "aluminium": "excellent",
            "bronze": "excellent",
            "GRP": "excellent"
        },
        "torque_values_nm": {
            "M3": 0.6,
            "M4": 1.3,
            "M5": 2.5,
            "M6": 4.2,
            "M8": 10.0,
            "M10": 19.5,
            "M12": 34.0,
            "M16": 76.0
        },
        "pre_drill_sizes_mm": {
            "M3": 3.4,
            "M4": 4.5,
            "M5": 5.5,
            "M6": 6.8,
            "M8": 9.3,
            "M10": 11.5,
            "M12": 13.5,
            "M16": 18.0
        },
        "quality_criteria": {
            "installation_tool": "helicoil_insertion_tool_required",
            "insert_seating": "flush_or_recessed",
            "hole_depth": "exact_per_specification",
            "sealant_requirement": "optional_thread_sealant",
            "insert_integrity": "no_visible_damage"
        },
        "common_failures": [
            "insert_stripping_over_torque",
            "incomplete_installation_holes",
            "loose_helicoil_rotating_out",
            "fastener_thread_stripping_helicoil"
        ],
        "inspection_interval_months": 12
    },

    "toggle_bolt_grp": {
        "name": "Flügeldübel GRP-Anwendung",
        "material": "Stainless Steel 316 Screw / Brass Toggle",
        "grade_standard": "DIN 65151",
        "sizes_available": ["M6", "M8", "M10"],
        "tensile_strength_mpa": 700,
        "shear_strength_mpa": 560,
        "suitable_for": [
            "GRP_cabin_interior_fastening",
            "hollow_GRP_panel_mounting",
            "interior_hardware_installation",
            "shelving_mounting",
            "light_fixture_attachment"
        ],
        "not_suitable_for": [
            "exterior_deck_fastening",
            "high_load_fastening",
            "structural_attachment",
            "waterline_penetrations"
        ],
        "galvanic_compatibility": {
            "GRP": "excellent",
            "stainless_steel": "excellent"
        },
        "torque_values_nm": {
            "M6": 4.0,
            "M8": 8.0,
            "M10": 14.0
        },
        "pre_drill_sizes_mm": {
            "M6": 6.5,
            "M8": 8.5,
            "M10": 10.5
        },
        "quality_criteria": {
            "hole_size": "exact_per_toggle_specification",
            "toggle_wing_clearance": "unobstructed_rotation",
            "fastener_torque": "snug_not_over_tight",
            "sealant_requirement": "sealant_around_perimeter_optional"
        },
        "common_failures": [
            "toggle_rotation_in_hole",
            "fastener_loosening_vibration",
            "fastener_pull_through",
            "GRP_cracking_around_fastening"
        ],
        "inspection_interval_months": 12
    },

    "backing_plate_assembly": {
        "name": "Unterlegplatte-Baugruppe",
        "material": "Stainless Steel 316 or Bronze",
        "grade_standard": "Custom Engineered per Load",
        "sizes_available": ["Custom", "50x50x6", "75x75x8", "100x100x10", "150x150x12"],
        "tensile_strength_mpa": 700,
        "shear_strength_mpa": 560,
        "suitable_for": [
            "deck_hardware_spreading_loads",
            "through_deck_fastening_structural",
            "chainplate_backing",
            "mast_step_base",
            "stanchion_base_support",
            "heavy_equipment_mounting"
        ],
        "not_suitable_for": [
            "non_load_fastening",
            "interior_light_hardware"
        ],
        "galvanic_compatibility": {
            "stainless_steel": "excellent",
            "bronze": "excellent",
            "GRP": "excellent"
        },
        "torque_values_nm": {
            "backing_plate": "per_fastener_specification"
        },
        "pre_drill_sizes_mm": {
            "backing_plate": "per_fastener_specification"
        },
        "quality_criteria": {
            "plate_thickness_min_mm": "calculated_load_spread",
            "plate_bearing_surface": "100_pct_contact_deck",
            "fastener_spacing": "load_distribution_verified",
            "sealant_bed": "continuous_under_plate",
            "hole_alignment": "no_deviation_perpendicular"
        },
        "common_failures": [
            "insufficient_plate_thickness",
            "poor_deck_contact",
            "sealant_washout",
            "fastener_bearing_failure"
        ],
        "inspection_interval_months": 12
    }
}

# ==============================================================================
# 2. DECK_HARDWARE_MOUNTING - Installation procedures and requirements
# ==============================================================================

DECK_HARDWARE_MOUNTING = {
    "cleat_mounting": {
        "name": "Klampe Montage",
        "typical_fasteners": ["through_bolt_316", "backing_plate_assembly"],
        "backing_plate_required": True,
        "backing_plate_spec": {
            "material": "Stainless Steel 316 or Bronze",
            "thickness_mm": 8,
            "bearing_area_multiplier": 2.5,
            "fastener_spacing_mm": 80
        },
        "sealant_type": "polyurethane_marine_sealant",
        "sealant_application_method": "continuous_bead_under_plate_around_base",
        "torque_sequence": ["star_pattern_4bolt"],
        "load_type": "combined_shear_tension",
        "typical_load_kn": 15.0,
        "safety_factor": 4.0,
        "quality_criteria": {
            "alignment": "base_parallel_deck_surface",
            "sealant_bed": "minimum_5mm_continuous",
            "backing_plate_contact_pct": 100,
            "torque_verification": "each_fastener_verified_final"
        },
        "common_failures": [
            "fastener_loosening_wind_load",
            "sealant_washout_marine_environment",
            "backing_plate_contact_loss",
            "deck_cracking_load_concentration"
        ],
        "inspection_interval_months": 6
    },

    "winch_mounting": {
        "name": "Winsch Montage",
        "typical_fasteners": ["through_bolt_316", "backing_plate_assembly"],
        "backing_plate_required": True,
        "backing_plate_spec": {
            "material": "Stainless Steel 316",
            "thickness_mm": 12,
            "bearing_area_multiplier": 3.0,
            "fastener_spacing_mm": 100
        },
        "sealant_type": "polyurethane_marine_sealant",
        "sealant_application_method": "continuous_bed_under_base_plate",
        "torque_sequence": ["star_pattern_6bolt"],
        "load_type": "high_shear_tension",
        "typical_load_kn": 25.0,
        "safety_factor": 5.0,
        "quality_criteria": {
            "alignment": "level_all_planes",
            "sealant_bed": "minimum_6mm_continuous",
            "backing_plate_contact_pct": 100,
            "torque_verification": "cross_check_after_24h"
        },
        "common_failures": [
            "fastener_loosening_repeated_loads",
            "deck_cracking_around_plate",
            "backing_plate_fracture_overload",
            "bearing_surface_corrosion"
        ],
        "inspection_interval_months": 3
    },

    "stanchion_base": {
        "name": "Stütze Basis Montage",
        "typical_fasteners": ["u_bolt_316", "through_bolt_316"],
        "backing_plate_required": True,
        "backing_plate_spec": {
            "material": "Stainless Steel 316",
            "thickness_mm": 6,
            "bearing_area_multiplier": 2.0,
            "fastener_spacing_mm": 60
        },
        "sealant_type": "polyurethane_marine_sealant",
        "sealant_application_method": "continuous_bead_perimeter",
        "torque_sequence": ["star_pattern_4bolt"],
        "load_type": "shear_dominant",
        "typical_load_kn": 8.0,
        "safety_factor": 6.0,
        "quality_criteria": {
            "alignment": "vertical_tolerance_5mm_height",
            "sealant_bed": "minimum_4mm_continuous",
            "backing_plate_contact_pct": 95,
            "torque_verification": "initial_then_monthly"
        },
        "common_failures": [
            "stanchion_bending_impact_load",
            "fastener_loosening_fatigue",
            "corrosion_at_deck_penetration",
            "deck_cracking_impact_stress"
        ],
        "inspection_interval_months": 6
    },

    "chainplate": {
        "name": "Kettenpfanne Montage",
        "typical_fasteners": ["through_bolt_316", "backing_plate_assembly"],
        "backing_plate_required": True,
        "backing_plate_spec": {
            "material": "Stainless Steel 316 or Bronze",
            "thickness_mm": 10,
            "bearing_area_multiplier": 2.5,
            "fastener_spacing_mm": 75
        },
        "sealant_type": "polyurethane_marine_sealant",
        "sealant_application_method": "continuous_bed_with_fillet",
        "torque_sequence": ["star_pattern_6bolt"],
        "load_type": "tension_dominant",
        "typical_load_kn": 40.0,
        "safety_factor": 5.0,
        "quality_criteria": {
            "alignment": "load_vector_verified",
            "sealant_bed": "minimum_6mm_fillet",
            "backing_plate_contact_pct": 100,
            "torque_verification": "cross_check_load_test"
        },
        "common_failures": [
            "fastener_loosening_cyclic_load",
            "backing_plate_rotation",
            "deck_fracture_through_fastener",
            "sealant_failure_dynamic_movement"
        ],
        "inspection_interval_months": 3
    },

    "pad_eye": {
        "name": "Augenplatte Montage",
        "typical_fasteners": ["eye_bolt_316", "backing_plate_assembly"],
        "backing_plate_required": True,
        "backing_plate_spec": {
            "material": "Stainless Steel 316",
            "thickness_mm": 8,
            "bearing_area_multiplier": 2.0,
            "fastener_spacing_mm": 70
        },
        "sealant_type": "polyurethane_marine_sealant",
        "sealant_application_method": "continuous_perimeter_bead",
        "torque_sequence": ["star_pattern_4bolt"],
        "load_type": "tension_shear_combined",
        "typical_load_kn": 20.0,
        "safety_factor": 5.0,
        "quality_criteria": {
            "alignment": "load_axis_perpendicular_deck",
            "sealant_bed": "minimum_5mm_continuous",
            "backing_plate_contact_pct": 100,
            "torque_verification": "final_verification"
        },
        "common_failures": [
            "pad_eye_bending_overload",
            "fastener_loosening",
            "sealant_separation_dynamic_load",
            "eye_corrosion_crevice"
        ],
        "inspection_interval_months": 6
    },

    "turning_block": {
        "name": "Umlenkblock Montage",
        "typical_fasteners": ["eye_bolt_316", "backing_plate_assembly"],
        "backing_plate_required": True,
        "backing_plate_spec": {
            "material": "Stainless Steel 316",
            "thickness_mm": 6,
            "bearing_area_multiplier": 1.8,
            "fastener_spacing_mm": 60
        },
        "sealant_type": "polyurethane_marine_sealant",
        "sealant_application_method": "continuous_bed",
        "torque_sequence": ["star_pattern_4bolt"],
        "load_type": "shear_dominant",
        "typical_load_kn": 10.0,
        "safety_factor": 5.0,
        "quality_criteria": {
            "alignment": "block_rotates_freely_unloaded",
            "sealant_bed": "minimum_4mm",
            "backing_plate_contact_pct": 95,
            "torque_verification": "no_over_constraint"
        },
        "common_failures": [
            "block_bearing_failure",
            "fastener_loosening_pulley_rotation",
            "deck_cracking",
            "sealant_washout"
        ],
        "inspection_interval_months": 6
    },

    "jammer": {
        "name": "Klemme Montage",
        "typical_fasteners": ["self_tapping_316", "eye_bolt_316"],
        "backing_plate_required": False,
        "backing_plate_spec": None,
        "sealant_type": "polyurethane_marine_sealant",
        "sealant_application_method": "bead_around_base",
        "torque_sequence": ["star_pattern_4bolt"],
        "load_type": "shear_dominant",
        "typical_load_kn": 5.0,
        "safety_factor": 3.0,
        "quality_criteria": {
            "alignment": "rope_slot_parallel_deck",
            "sealant_bed": "minimum_3mm_bead",
            "backing_plate_contact_pct": "n_a",
            "torque_verification": "snug_no_over_tightening"
        },
        "common_failures": [
            "fastener_loosening_vibration",
            "rope_slippage_inadequate_clamp",
            "corrosion_crevice",
            "fastener_pull_through"
        ],
        "inspection_interval_months": 12
    },

    "furler_base": {
        "name": "Rollanlage Basis Montage",
        "typical_fasteners": ["through_bolt_316", "backing_plate_assembly"],
        "backing_plate_required": True,
        "backing_plate_spec": {
            "material": "Stainless Steel 316",
            "thickness_mm": 10,
            "bearing_area_multiplier": 2.5,
            "fastener_spacing_mm": 85
        },
        "sealant_type": "polyurethane_marine_sealant",
        "sealant_application_method": "continuous_bed_with_fillet",
        "torque_sequence": ["star_pattern_8bolt"],
        "load_type": "tension_shear",
        "typical_load_kn": 35.0,
        "safety_factor": 5.0,
        "quality_criteria": {
            "alignment": "furler_axis_vertical",
            "sealant_bed": "minimum_6mm_continuous",
            "backing_plate_contact_pct": 100,
            "torque_verification": "load_test_before_use"
        },
        "common_failures": [
            "fastener_loosening_sail_load",
            "backing_plate_bearing_failure",
            "furler_misalignment",
            "sealant_failure_thermal_cycling"
        ],
        "inspection_interval_months": 3
    },

    "anchor_windlass": {
        "name": "Ankerwinsch Montage",
        "typical_fasteners": ["through_bolt_316", "backing_plate_assembly"],
        "backing_plate_required": True,
        "backing_plate_spec": {
            "material": "Stainless Steel 316",
            "thickness_mm": 12,
            "bearing_area_multiplier": 3.0,
            "fastener_spacing_mm": 100
        },
        "sealant_type": "polyurethane_marine_sealant",
        "sealant_application_method": "continuous_bed_perimeter_fillet",
        "torque_sequence": ["star_pattern_8bolt"],
        "load_type": "high_shear_tension",
        "typical_load_kn": 50.0,
        "safety_factor": 5.0,
        "quality_criteria": {
            "alignment": "winch_axis_perpendicular_deck",
            "sealant_bed": "minimum_7mm_continuous",
            "backing_plate_contact_pct": 100,
            "torque_verification": "load_test_verification"
        },
        "common_failures": [
            "fastener_failure_shock_load",
            "deck_cracking_stress_concentration",
            "backing_plate_fracture",
            "sealant_washout_moisture_penetration"
        ],
        "inspection_interval_months": 6
    },

    "solar_panel_mount": {
        "name": "Solarpanel Montage",
        "typical_fasteners": ["self_tapping_316", "eye_bolt_316"],
        "backing_plate_required": False,
        "backing_plate_spec": None,
        "sealant_type": "polyurethane_marine_sealant",
        "sealant_application_method": "bead_under_clamp_feet",
        "torque_sequence": ["star_pattern_4bolt"],
        "load_type": "shear_dominant_wind",
        "typical_load_kn": 5.0,
        "safety_factor": 4.0,
        "quality_criteria": {
            "alignment": "panel_level_wind_load_verified",
            "sealant_bed": "minimum_3mm_bead",
            "backing_plate_contact_pct": "n_a",
            "torque_verification": "snug_not_over_tight_brittle_panel"
        },
        "common_failures": [
            "panel_cracking_over_tightening",
            "fastener_loosening_vibration",
            "sealant_failure_thermal_stress",
            "corrosion_at_fastener_panel_interface"
        ],
        "inspection_interval_months": 12
    },

    "radar_mount": {
        "name": "Radarmast Montage",
        "typical_fasteners": ["through_bolt_316", "backing_plate_assembly"],
        "backing_plate_required": True,
        "backing_plate_spec": {
            "material": "Stainless Steel 316",
            "thickness_mm": 8,
            "bearing_area_multiplier": 2.5,
            "fastener_spacing_mm": 80
        },
        "sealant_type": "polyurethane_marine_sealant",
        "sealant_application_method": "continuous_bed_with_fillet",
        "torque_sequence": ["star_pattern_4bolt"],
        "load_type": "shear_dominant_wind",
        "typical_load_kn": 12.0,
        "safety_factor": 4.0,
        "quality_criteria": {
            "alignment": "mast_vertical_tolerance_5mm_height",
            "sealant_bed": "minimum_5mm_continuous",
            "backing_plate_contact_pct": 100,
            "torque_verification": "after_24h_and_monthly"
        },
        "common_failures": [
            "fastener_loosening_wind_vibration",
            "mast_bending_fatigue",
            "sealant_failure_salt_water_penetration",
            "backing_plate_corrosion"
        ],
        "inspection_interval_months": 6
    },

    "pushpit_pulpit": {
        "name": "Rehling Montage",
        "typical_fasteners": ["through_bolt_316", "backing_plate_assembly"],
        "backing_plate_required": True,
        "backing_plate_spec": {
            "material": "Stainless Steel 316",
            "thickness_mm": 6,
            "bearing_area_multiplier": 2.0,
            "fastener_spacing_mm": 70
        },
        "sealant_type": "polyurethane_marine_sealant",
        "sealant_application_method": "continuous_perimeter_bead",
        "torque_sequence": ["star_pattern_4bolt"],
        "load_type": "combined_shear_tension",
        "typical_load_kn": 10.0,
        "safety_factor": 6.0,
        "quality_criteria": {
            "alignment": "rail_straight_tolerance_3mm_span",
            "sealant_bed": "minimum_4mm_continuous",
            "backing_plate_contact_pct": 95,
            "torque_verification": "initial_then_quarterly"
        },
        "common_failures": [
            "rail_bending_impact",
            "fastener_loosening_impact_loads",
            "deck_cracking_impact_stress",
            "sealant_failure_foot_traffic"
        ],
        "inspection_interval_months": 6
    },

    "track_mounting": {
        "name": "Schiene Montage",
        "typical_fasteners": ["self_tapping_316", "machine_screw_316"],
        "backing_plate_required": False,
        "backing_plate_spec": None,
        "sealant_type": "polyurethane_marine_sealant",
        "sealant_application_method": "bead_under_track_profile",
        "torque_sequence": ["sequential_line"],
        "load_type": "shear_dominant",
        "typical_load_kn": 3.0,
        "safety_factor": 3.0,
        "quality_criteria": {
            "alignment": "track_straight_fairlead_smooth",
            "sealant_bed": "continuous_under_track",
            "backing_plate_contact_pct": "n_a",
            "torque_verification": "final_and_after_sail_load"
        },
        "common_failures": [
            "track_distortion_fastener_over_tightening",
            "fastener_loosening_repeat_load",
            "sealant_failure_weather_exposure",
            "fastener_corrosion_crevice"
        ],
        "inspection_interval_months": 12
    }
}

# ==============================================================================
# 3. THROUGH_HULL_FITTINGS - Underwater fitting specifications
# ==============================================================================

THROUGH_HULL_FITTINGS = {
    "seacock_bronze": {
        "name": "Seehahn Bronze",
        "material": "Naval Bronze (Cu-Sn-Pb)",
        "suitable_below_waterline": True,
        "installation_procedure": [
            "1_measure_hull_thickness_at_location",
            "2_prepare_hole_diameter_per_seacock_spec",
            "3_install_through_hull_fitting_with_rubber_washer",
            "4_apply_bedding_compound_to_flange",
            "5_install_seacock_from_inside_hull",
            "6_secure_fasteners_in_star_pattern",
            "7_allow_bedding_compound_24h_cure",
            "8_test_for_leaks_under_load",
            "9_wire_lock_fasteners_if_required"
        ],
        "sealant": "marine_polysulfide_or_polyurethane",
        "backing_block_required": True,
        "quality_criteria": {
            "fastener_type": "bronze_or_stainless_316",
            "backing_block_material": "hardwood_or_marine_plywood",
            "backing_block_dimensions": "min_2x_opening_size",
            "sealing_surface": "no_visible_gaps_in_sealant",
            "valve_operation": "smooth_no_binding",
            "corrosion_appearance": "expected_patina_only"
        },
        "failure_modes": [
            "valve_corrosion_dezincification",
            "fastener_loosening_water_entry",
            "sealant_failure_salt_water_attack",
            "backing_block_rot_moisture",
            "valve_handle_corrosion"
        ],
        "inspection_interval_months": 12,
        "replacement_interval_years": 15
    },

    "seacock_marelon": {
        "name": "Seehahn Marelon",
        "material": "Marelon Composite (Resin + Reinforcement)",
        "suitable_below_waterline": True,
        "installation_procedure": [
            "1_check_marelon_compatibility_saltwater",
            "2_measure_hull_thickness_and_prepare_hole",
            "3_install_through_hull_with_rubber_washer",
            "4_apply_bedding_compound_non_aggressive",
            "5_install_seacock_from_inside_with_stainless_fasteners",
            "6_torque_fasteners_carefully_no_over_tightening",
            "7_allow_24h_cure_minimum",
            "8_test_valve_operation_no_binding",
            "9_inspect_backing_block_integrity"
        ],
        "sealant": "marine_polyurethane_polysulfide",
        "backing_block_required": True,
        "quality_criteria": {
            "fastener_type": "stainless_steel_316_only",
            "backing_block_material": "marine_plywood_or_hardwood",
            "backing_block_dimensions": "min_2x_opening_size",
            "sealing_surface": "continuous_bead_no_gaps",
            "valve_operation": "smooth_easy_full_range",
            "no_galvanic_corrosion": "stainless_fasteners_critical"
        },
        "failure_modes": [
            "fastener_corrosion_galvanic",
            "sealant_failure_aggressive_chemistry",
            "backing_block_rot",
            "valve_fracture_brittle_material",
            "thread_stripping_over_tightening"
        ],
        "inspection_interval_months": 12,
        "replacement_interval_years": 20
    },

    "skin_fitting_316": {
        "name": "Anschluss Fitting 316er Edelstahl",
        "material": "Stainless Steel 316",
        "suitable_below_waterline": True,
        "installation_procedure": [
            "1_verify_hull_material_compatibility",
            "2_prepare_hole_per_fitting_specification",
            "3_install_rubber_sealing_washer",
            "4_apply_marine_sealant_to_flange",
            "5_secure_fitting_fasteners_star_pattern",
            "6_install_strainer_basket_if_applicable",
            "7_cure_sealant_24h_before_use",
            "8_pressure_test_if_required",
            "9_apply_protective_coating_if_needed"
        ],
        "sealant": "polyurethane_marine_sealant_or_polysulfide",
        "backing_block_required": True,
        "quality_criteria": {
            "fastener_type": "stainless_steel_316",
            "backing_block_material": "hardwood_or_marine_plywood",
            "backing_block_dimensions": "min_2x_opening_size_rounded_edges",
            "sealing_surface": "no_visible_gaps_sealant",
            "strainer_access": "cleanable_under_load",
            "corrosion_resistance": "stainless_surface_condition"
        },
        "failure_modes": [
            "crevice_corrosion_under_fitting",
            "sealant_failure_thermal_cycling",
            "fastener_loosening_pressure_variation",
            "backing_block_failure_moisture",
            "fitting_erosion_high_flow"
        ],
        "inspection_interval_months": 12,
        "replacement_interval_years": 20
    },

    "transducer_fitting": {
        "name": "Geber Durchführung",
        "material": "Bronze or Stainless Steel 316",
        "suitable_below_waterline": True,
        "installation_procedure": [
            "1_select_location_clear_of_turbulence",
            "2_prepare_hole_perpendicular_to_hull",
            "3_install_rubber_grommet_seal",
            "4_apply_bedding_compound_perimeter",
            "5_secure_fitting_fasteners_symmetrically",
            "6_connect_electrical_waterproof_connector",
            "7_test_transducer_signal_quality",
            "8_allow_24h_cure",
            "9_verify_no_water_ingress_at_fastener"
        ],
        "sealant": "marine_polyurethane_or_polysulfide",
        "backing_block_required": True,
        "quality_criteria": {
            "fastener_type": "stainless_steel_316",
            "backing_block_material": "marine_plywood_or_plastic_plate",
            "backing_block_dimensions": "min_1.5x_opening_size",
            "sealing_surface": "waterproof_grommet_compression",
            "electrical_sealing": "waterproof_connector_required",
            "transducer_signal": "verified_before_closure"
        },
        "failure_modes": [
            "electrical_water_ingress",
            "fastener_corrosion_galvanic",
            "transducer_cable_abrasion",
            "sealant_failure_vibration",
            "backing_block_degradation"
        ],
        "inspection_interval_months": 12,
        "replacement_interval_years": 10
    },

    "shaft_seal_pss": {
        "name": "Wellendichtung PSS",
        "material": "PSS Dichtung (Polymer)",
        "suitable_below_waterline": True,
        "installation_procedure": [
            "1_measure_shaft_diameter_runout",
            "2_prepare_shaft_surface_smooth",
            "3_slide_pss_seal_on_shaft",
            "4_position_seal_at_correct_depth",
            "5_install_hose_clamps_properly_spaced",
            "6_tighten_clamps_evenly_no_over_tightening",
            "7_check_shaft_rotation_smooth",
            "8_apply_sealant_around_hull_penetration",
            "9_monitor_for_weeping_first_24h"
        ],
        "sealant": "polyurethane_marine_sealant",
        "backing_block_required": False,
        "quality_criteria": {
            "fastener_type": "stainless_steel_hose_clamp",
            "shaft_condition": "smooth_no_corrosion_pits",
            "seal_compression": "even_around_shaft",
            "clamp_tightness": "snug_no_over_constraint",
            "weeping_acceptable": "minimal_first_week",
            "no_shaft_wobble": "runout_less_than_1mm"
        },
        "failure_modes": [
            "weeping_excessive_pressure_build",
            "shaft_corrosion_pitting",
            "seal_material_degradation",
            "clamp_corrosion_loosening",
            "shaft_bearing_overheating_seal_drag"
        ],
        "inspection_interval_months": 6,
        "replacement_interval_years": 5
    },

    "shaft_seal_traditional": {
        "name": "Wellendichtung Traditional",
        "material": "Stuffing Box with Packing",
        "suitable_below_waterline": True,
        "installation_procedure": [
            "1_prepare_shaft_clean_smooth_surface",
            "2_install_packing_gland_if_missing",
            "3_cut_packing_material_size",
            "4_wrap_packing_evenly_around_shaft",
            "5_slide_gland_over_packing",
            "6_hand_tighten_gland_fasteners",
            "7_rotate_shaft_check_smooth",
            "8_gradually_tighten_fasteners_even_pressure",
            "9_monitor_weeping_establish_drip_rate"
        ],
        "sealant": "packing_material_graphite_impregnated",
        "backing_block_required": False,
        "quality_criteria": {
            "fastener_type": "stainless_or_bronze",
            "packing_material": "graphite_impregnated_polyester",
            "packing_wrap": "uniform_even_gaps",
            "gland_compression": "hand_tight_plus_1_4_turn",
            "weeping_rate": "one_drop_per_minute_at_speed",
            "shaft_condition": "smooth_no_scoring"
        },
        "failure_modes": [
            "packing_degradation_heat",
            "shaft_scoring_excessive_tightening",
            "gland_fastener_loosening",
            "weeping_excessive_or_dry_running",
            "gland_breakage_over_tightening"
        ],
        "inspection_interval_months": 3,
        "replacement_interval_years": 3
    },

    "rudder_bearing": {
        "name": "Ruderanlage Lagerung",
        "material": "Bronze Bush or Polymer Bearing",
        "suitable_below_waterline": True,
        "installation_procedure": [
            "1_remove_rudder_shaft_if_serviceable",
            "2_inspect_bearing_material_condition",
            "3_measure_shaft_diameter_wear",
            "4_prepare_installation_location",
            "5_press_bearing_into_location_if_required",
            "6_align_shaft_perpendicular_deck",
            "7_check_shaft_rotation_smooth_no_binding",
            "8_install_bearing_cover_sealing",
            "9_grease_bearing_per_specification"
        ],
        "sealant": "marine_grease_or_bearing_sealing",
        "backing_block_required": False,
        "quality_criteria": {
            "fastener_type": "stainless_bronze_fasteners",
            "bearing_material": "no_cracks_corrosion",
            "shaft_clearance": "minimum_radial_play",
            "alignment": "shaft_vertical_tolerance_5mm",
            "rotation_quality": "smooth_minimal_friction",
            "sealing_cover": "no_water_ingress"
        },
        "failure_modes": [
            "bearing_material_erosion",
            "shaft_corrosion_pitting",
            "bearing_seizure_inadequate_lubrication",
            "alignment_loss_binding",
            "seal_failure_water_ingress"
        ],
        "inspection_interval_months": 12,
        "replacement_interval_years": 10
    },

    "keel_bolt_assembly": {
        "name": "Kielbeschlag Baugruppe",
        "material": "Stainless Steel 316 or High Strength Steel",
        "suitable_below_waterline": True,
        "installation_procedure": [
            "1_verify_keel_structure_integrity",
            "2_prepare_bolt_holes_exact_diameter",
            "3_measure_hull_thickness_at_installation",
            "4_install_internal_backing_plate_assembly",
            "5_apply_bedding_compound_bolt_penetration",
            "6_install_bolts_with_washers_large_bearing",
            "7_install_external_backing_plates_if_required",
            "8_torque_bolts_star_pattern_precise_values",
            "9_verify_structural_loads_aligned",
            "10_apply_protective_coating_underwater_section"
        ],
        "sealant": "marine_polyurethane_bedding_compound",
        "backing_block_required": True,
        "quality_criteria": {
            "fastener_type": "A4_stainless_or_high_strength_steel",
            "backing_plate_material": "stainless_bronze_or_steel",
            "backing_plate_dimensions": "min_3x_bolt_circle",
            "torque_verification": "each_bolt_load_measured",
            "seal_integrity": "no_seepage_under_load",
            "alignment": "load_path_verified_structural"
        },
        "failure_modes": [
            "fastener_corrosion_galvanic_attack",
            "backing_plate_failure_overload",
            "sealant_degradation_salt_water",
            "bolt_loosening_dynamic_loads",
            "keel_structural_failure_concentration"
        ],
        "inspection_interval_months": 12,
        "replacement_interval_years": 20
    }
}

# Continuation in next part due to token limits...
# File continues with remaining sections below

# ==============================================================================
# 4. RIGGING_HARDWARE - Rigging and tensioning equipment specifications
# ==============================================================================

RIGGING_HARDWARE = {
    "turnbuckle_open": {
        "name": "Wantenspanner offen",
        "material": "Stainless Steel 316 or Bronze",
        "swl_to_break_ratio": 5.0,
        "inspection_criteria": [
            "visible_corrosion_or_pitting",
            "thread_damage_or_galling",
            "missing_or_damaged_cotter_pin",
            "barrel_straightness_not_bent",
            "body_cracks_fractures",
            "swivel_joint_freedom_of_rotation"
        ],
        "wear_indicators": [
            "thread_stripping_resistance",
            "cotter_pin_hole_enlargement",
            "barrel_thread_engagement_loss",
            "swivel_corrosion_staining"
        ],
        "replacement_criteria": [
            "visible_thread_damage",
            "cotter_pin_hole_stripped",
            "barrel_bent_or_corroded_through",
            "swivel_stuck_or_binding",
            "safety_load_test_failure",
            "operating_beyond_swl_history"
        ],
        "quality_criteria": {
            "thread_pitch": "metric_or_british_consistent",
            "cotter_pin": "split_pin_required_always",
            "swivel_function": "full_free_rotation",
            "surface_finish": "no_seizing_corrosion",
            "barrel_thread_engagement": "minimum_3_full_turns"
        },
        "common_failures": [
            "thread_stripping_over_tightening",
            "barrel_separation_shock_load",
            "cotter_pin_loss_vibration",
            "corrosion_saltwater_exposure",
            "swivel_corrosion_stiffening"
        ]
    },

    "turnbuckle_toggle": {
        "name": "Wantenspanner Scharnierausführung",
        "material": "Stainless Steel 316",
        "swl_to_break_ratio": 5.0,
        "inspection_criteria": [
            "toggle_pin_straightness",
            "pin_hole_wear_enlargement",
            "body_thread_integrity",
            "corrosion_pitting_appearance",
            "toggle_movement_free",
            "barrel_alignment"
        ],
        "wear_indicators": [
            "pin_bending_slight",
            "pin_hole_oval_deformation",
            "barrel_thread_wear",
            "corrosion_staining_salt_encrustation"
        ],
        "replacement_criteria": [
            "pin_bent_or_broken",
            "pin_hole_stripped",
            "thread_damage_stripping",
            "barrel_bent_beyond_tolerance",
            "safety_load_test_failure"
        ],
        "quality_criteria": {
            "toggle_pin": "stainless_steel_smooth",
            "pin_diameter": "no_deviation_tolerance",
            "body_threads": "clean_no_corrosion_debris",
            "surface_finish": "polished_or_bright",
            "toggle_movement": "free_full_range"
        },
        "common_failures": [
            "pin_bending_shock_load",
            "pin_hole_wear_movement",
            "thread_stripping_vibration",
            "corrosion_salt_encrustation",
            "barrel_bending_side_load"
        ]
    },

    "clevis_pin": {
        "name": "Bolzenausführung Spaltklinke",
        "material": "Stainless Steel 316",
        "swl_to_break_ratio": 4.0,
        "inspection_criteria": [
            "pin_straightness",
            "pin_surface_corrosion_pitting",
            "cotter_pin_presence_integrity",
            "hole_wear_enlargement",
            "body_cracks_fractures",
            "swivel_movement_smooth"
        ],
        "wear_indicators": [
            "pin_slight_bending",
            "hole_oval_deformation",
            "cotter_pin_fatigue_fracture",
            "surface_corrosion_salt_staining"
        ],
        "replacement_criteria": [
            "pin_bent_or_broken",
            "hole_stripped_enlarged",
            "cotter_pin_missing",
            "body_cracked",
            "safety_load_test_failure"
        ],
        "quality_criteria": {
            "pin_material": "stainless_steel_316",
            "pin_diameter": "snug_fit_no_play",
            "cotter_pin": "stainless_split_pin_required",
            "surface_finish": "smooth_no_sharp_edges",
            "body_holes": "aligned_no_deformation"
        },
        "common_failures": [
            "cotter_pin_loss_vibration",
            "pin_bending_cyclic_load",
            "hole_wear_enlargement",
            "corrosion_surface_pitting",
            "body_fracture_brittle"
        ]
    },

    "split_pin_cotter": {
        "name": "Splint",
        "material": "Stainless Steel 316",
        "swl_to_break_ratio": 2.0,
        "inspection_criteria": [
            "pin_straightness_before_installation",
            "pin_diameter_no_corrosion",
            "pin_leg_length_symmetrical",
            "corrosion_appearance_staining"
        ],
        "wear_indicators": [
            "pin_fracture_fatigue_cracks",
            "pin_corrosion_pitting_appearance",
            "pin_bending_loss_of_security"
        ],
        "replacement_criteria": [
            "pin_fractured_broken",
            "pin_corroded_weakened",
            "pin_bent_insufficient_tension",
            "pin_missing_lost"
        ],
        "quality_criteria": {
            "material": "stainless_steel_316",
            "diameter": "exact_per_hole_specification",
            "straightness": "within_tolerance",
            "surface_finish": "bright_no_defects",
            "leg_formation": "symmetrical_bent_proper_angle"
        },
        "common_failures": [
            "pin_loss_vibration_loosening",
            "pin_fracture_fatigue",
            "pin_bending_impact",
            "corrosion_pitting_stress_concentration",
            "inadequate_security_loose_fit"
        ]
    },

    "shackle_d": {
        "name": "D-Schäkel",
        "material": "Stainless Steel 316 or Forged Steel",
        "swl_to_break_ratio": 5.0,
        "inspection_criteria": [
            "body_cracks_fractures",
            "pin_straightness_bearing",
            "pin_corrosion_pitting",
            "pin_hole_wear_enlargement",
            "shackle_dimensional_no_distortion",
            "cotter_pin_presence_integrity"
        ],
        "wear_indicators": [
            "pin_slight_bending",
            "pin_hole_deformation_ovality",
            "surface_corrosion_staining",
            "cotter_pin_fatigue_micro_cracks"
        ],
        "replacement_criteria": [
            "body_crack_fracture",
            "pin_bent_or_broken",
            "pin_hole_enlarged_stripped",
            "shackle_bent_distorted",
            "safety_load_test_failure"
        ],
        "quality_criteria": {
            "material": "stainless_or_high_strength_steel",
            "body_finish": "smooth_no_stress_concentrations",
            "pin": "stainless_steel_tight_fit",
            "cotter_pin": "split_pin_required",
            "weight_rating": "marked_clearly_visible"
        },
        "common_failures": [
            "body_fracture_overload_fatigue",
            "pin_bending_shock_load",
            "pin_hole_wear_movement",
            "cotter_pin_loss_vibration",
            "corrosion_crevice_fatigue"
        ]
    },

    "shackle_snap": {
        "name": "Schnappschäkel",
        "material": "Stainless Steel 316",
        "swl_to_break_ratio": 4.0,
        "inspection_criteria": [
            "snap_mechanism_smoothness",
            "snap_latch_security",
            "body_cracks_fractures",
            "pin_straightness",
            "corrosion_pitting_appearance",
            "snap_return_spring_function"
        ],
        "wear_indicators": [
            "snap_latching_stiffness_increase",
            "snap_spring_weakening",
            "pin_slight_bending",
            "corrosion_surface_staining"
        ],
        "replacement_criteria": [
            "snap_mechanism_broken_stuck",
            "spring_failure_no_return",
            "body_cracked",
            "safety_load_test_failure"
        ],
        "quality_criteria": {
            "material": "stainless_steel_316",
            "snap_mechanism": "smooth_effortless_operation",
            "spring_tension": "positive_return_force",
            "body_finish": "smooth_no_sharp_edges",
            "pin_fit": "snug_no_play"
        },
        "common_failures": [
            "snap_mechanism_corrosion_seizing",
            "spring_fatigue_failure",
            "snap_unlatching_impact_load",
            "pin_bending_shock",
            "body_fracture_overload"
        ]
    },

    "thimble": {
        "name": "Kausche",
        "material": "Stainless Steel 316 or Bronze",
        "swl_to_break_ratio": 5.0,
        "inspection_criteria": [
            "outer_surface_corrosion_pitting",
            "inner_groove_wear_rope_indent",
            "rope_lay_security_whipping",
            "thimble_shape_distortion",
            "fastener_integrity_if_swaged"
        ],
        "wear_indicators": [
            "inner_groove_indentation_deepening",
            "surface_corrosion_staining",
            "rope_movement_in_eye",
            "thimble_denting_deformation"
        ],
        "replacement_criteria": [
            "inner_groove_worn_1_2_diameter",
            "thimble_distorted_oval",
            "rope_slipping_in_eye",
            "corrosion_perforation_through_wall",
            "safety_load_test_failure"
        ],
        "quality_criteria": {
            "material": "stainless_or_bronze",
            "inner_radius": "matches_rope_diameter",
            "surface_finish": "smooth_no_burrs",
            "rope_seating": "rope_lies_evenly",
            "fastening": "secure_no_loosening"
        },
        "common_failures": [
            "rope_slipping_inadequate_whipping",
            "groove_wear_rope_cutting",
            "thimble_distortion_side_load",
            "corrosion_surface_pitting",
            "fastener_loosening_vibration"
        ]
    },

    "swage_terminal": {
        "name": "Pressklemme Endverbindung",
        "material": "Aluminium or Stainless Steel",
        "swl_to_break_ratio": 5.0,
        "inspection_criteria": [
            "swage_integrity_no_cracks",
            "rope_seating_firm_secure",
            "rope_lay_whipping_security",
            "swage_dimensional_no_distortion",
            "fastener_security_if_crimped"
        ],
        "wear_indicators": [
            "surface_corrosion_staining",
            "micro_cracks_stress_concentration",
            "rope_slipping_movement",
            "swage_denting_deformation"
        ],
        "replacement_criteria": [
            "swage_fractured_split",
            "rope_slipping_in_swage",
            "corrosion_perforation_through_wall",
            "swage_deformed_distorted",
            "safety_load_test_failure"
        ],
        "quality_criteria": {
            "material": "aluminium_or_stainless",
            "swage_integrity": "no_visible_cracks",
            "rope_fit": "snug_firm_seating",
            "surface_finish": "smooth_consistent",
            "pressing_force": "per_specification_verified"
        },
        "common_failures": [
            "swage_fracture_fatigue",
            "rope_slipping_inadequate_compression",
            "corrosion_crevice_fatigue",
            "distortion_bending_load",
            "rope_strand_breakage_under_load"
        ]
    },

    "mechanical_terminal_sta_lok": {
        "name": "Mechanische Endverbindung Sta-Lok",
        "material": "Stainless Steel 316",
        "swl_to_break_ratio": 5.0,
        "inspection_criteria": [
            "cone_seating_security_visual",
            "mandrel_straightness_alignment",
            "rope_strands_secure_in_cone",
            "fastener_torque_verified",
            "corrosion_pitting_appearance",
            "mechanical_integrity_smooth"
        ],
        "wear_indicators": [
            "cone_loosening_rotation",
            "rope_strand_slipping_movement",
            "fastener_corrosion_staining",
            "micro_movement_cone_mandrel"
        ],
        "replacement_criteria": [
            "cone_loosened_rotated",
            "rope_strands_slipping_pulling_out",
            "fastener_stripped_damaged",
            "mandrel_bent_or_damaged",
            "safety_load_test_failure"
        ],
        "quality_criteria": {
            "material": "stainless_steel_316",
            "cone_seating": "uniform_contact_no_gaps",
            "rope_strand_distribution": "even_no_bundling",
            "fastener_torque": "per_specification_locked",
            "mechanical_engagement": "confirmed_visual"
        },
        "common_failures": [
            "cone_loosening_vibration",
            "rope_strand_slipping_tension_load",
            "fastener_loosening_vibration",
            "mandrel_bending_shock_load",
            "corrosion_cone_mandrel_interface"
        ]
    },

    "wire_rope_clip": {
        "name": "Drahtseilklemme",
        "material": "Stainless Steel 316 or Malleable Iron",
        "swl_to_break_ratio": 5.0,
        "inspection_criteria": [
            "clamp_bolt_torque_verification",
            "clamp_base_straightness",
            "rope_seating_groove_contact",
            "rope_strand_secure_not_slipping",
            "corrosion_pitting_appearance",
            "clamp_movement_bolt_tightness"
        ],
        "wear_indicators": [
            "bolt_loosening_vibration",
            "rope_slipping_movement_subtle",
            "clamp_base_bending_deformation",
            "surface_corrosion_staining"
        ],
        "replacement_criteria": [
            "bolt_loosened_fastener",
            "rope_slipping_pulling_through",
            "clamp_base_cracked_fractured",
            "corrosion_weakness_pitting",
            "safety_load_test_failure"
        ],
        "quality_criteria": {
            "material": "stainless_or_malleable_iron",
            "bolt": "stainless_steel_snug_fit",
            "rope_groove": "matches_rope_diameter",
            "clamp_base": "straight_no_distortion",
            "fastener_security": "lock_nut_or_thread_sealant"
        },
        "common_failures": [
            "bolt_loosening_vibration",
            "rope_slipping_inadequate_grip",
            "clamp_base_bending_side_load",
            "corrosion_surface_weakness",
            "fastener_pullout_overload"
        ]
    },

    "halyard_sheave": {
        "name": "Nocke Umlenkrolle",
        "material": "Stainless Steel or Composite Bearing",
        "swl_to_break_ratio": 5.0,
        "inspection_criteria": [
            "sheave_rotation_smooth_no_binding",
            "bearing_surface_corrosion",
            "pin_straightness_alignment",
            "pin_hole_wear_enlargement",
            "sheave_groove_wear_rope_indent",
            "fastener_security_bolt_integrity"
        ],
        "wear_indicators": [
            "sheave_rotation_stiffening",
            "bearing_surface_corrosion_staining",
            "pin_slight_bending",
            "groove_indentation_deepening"
        ],
        "replacement_criteria": [
            "sheave_binding_stiff_rotation",
            "bearing_seized_frozen",
            "pin_bent_or_broken",
            "groove_worn_rope_cutting",
            "safety_load_test_failure"
        ],
        "quality_criteria": {
            "sheave_material": "stainless_or_nylon_bearing",
            "rotation": "smooth_free_minimal_friction",
            "pin": "stainless_steel_tight_fit",
            "groove_radius": "matches_rope_diameter",
            "fastener": "secure_lock_nut_required"
        },
        "common_failures": [
            "bearing_corrosion_seizing",
            "pin_bending_shock_load",
            "groove_wear_rope_cutting",
            "fastener_loosening_vibration",
            "sheave_distortion_deformation"
        ]
    },

    "mast_step": {
        "name": "Mastfuß",
        "material": "Stainless Steel 316 or Aluminum Alloy",
        "swl_to_break_ratio": 5.0,
        "inspection_criteria": [
            "fastener_security_bolt_torque",
            "step_flatness_contact_surface",
            "corrosion_pitting_appearance",
            "bearing_surface_wear",
            "mast_tube_straightness_alignment",
            "ball_bearing_if_rotating_smooth"
        ],
        "wear_indicators": [
            "fastener_loosening_vibration",
            "bearing_surface_corrosion",
            "step_bending_deformation",
            "mast_movement_slight_rotation"
        ],
        "replacement_criteria": [
            "fastener_loosened_stripped",
            "step_cracked_fractured",
            "bearing_seized_damaged",
            "mast_bending_side_play",
            "safety_load_test_failure"
        ],
        "quality_criteria": {
            "material": "stainless_or_aluminium_alloy",
            "fastener": "stainless_steel_lock_nut",
            "bearing_surface": "smooth_even_contact",
            "step_flatness": "perpendicular_mast_axis",
            "installation": "verified_vertical_alignment"
        },
        "common_failures": [
            "fastener_loosening_vibration",
            "step_cracking_overload",
            "bearing_corrosion_seizing",
            "mast_misalignment_side_load",
            "step_bending_lateral_force"
        ]
    },

    "gooseneck": {
        "name": "Gänsefuß Begummung",
        "material": "Stainless Steel 316",
        "swl_to_break_ratio": 4.0,
        "inspection_criteria": [
            "fastener_security_bolt_torque",
            "gooseneck_straightness_alignment",
            "bolt_holes_condition_no_stripping",
            "corrosion_pitting_appearance",
            "boom_fitting_interface_wear",
            "mechanical_locking_security"
        ],
        "wear_indicators": [
            "fastener_loosening_movement",
            "gooseneck_slight_bending",
            "bolt_corrosion_staining",
            "boom_connector_wear_looseness"
        ],
        "replacement_criteria": [
            "fastener_loosened_stripped",
            "gooseneck_bent_or_cracked",
            "bolt_holes_enlarged_damaged",
            "mechanical_locking_failure",
            "safety_load_test_failure"
        ],
        "quality_criteria": {
            "material": "stainless_steel_316",
            "fastener": "stainless_lock_nut_required",
            "alignment": "boom_axis_perpendicular_mast",
            "bolt_holes": "no_cross_threading",
            "mechanical_locking": "security_verified"
        },
        "common_failures": [
            "fastener_loosening_boom_motion",
            "gooseneck_bending_sail_load",
            "bolt_hole_stripping_vibration",
            "corrosion_mechanical_weakness",
            "boom_connector_looseness_play"
        ]
    },

    "spreader_bracket": {
        "name": "Ausleger Befestigung",
        "material": "Stainless Steel 316 or Aluminum",
        "swl_to_break_ratio": 4.0,
        "inspection_criteria": [
            "fastener_torque_verification",
            "bracket_straightness_alignment",
            "spreader_hole_wear_enlargement",
            "corrosion_pitting_appearance",
            "mast_interface_contact",
            "lateral_movement_security"
        ],
        "wear_indicators": [
            "fastener_loosening_vibration",
            "bracket_slight_bending",
            "spreader_hole_deformation",
            "corrosion_surface_staining"
        ],
        "replacement_criteria": [
            "fastener_loosened_stripped",
            "bracket_bent_or_cracked",
            "spreader_hole_enlarged_damaged",
            "mast_contact_lost_separation",
            "safety_load_test_failure"
        ],
        "quality_criteria": {
            "material": "stainless_or_aluminium_alloy",
            "fastener": "stainless_lock_nut_required",
            "bracket_straightness": "within_tolerance",
            "mast_contact": "full_bearing_surface",
            "lateral_security": "no_side_play_movement"
        },
        "common_failures": [
            "fastener_loosening_vibration",
            "bracket_bending_spreader_tension",
            "spreader_hole_wear_movement",
            "mast_contact_loss_separation",
            "corrosion_fatigue_weakness"
        ]
    },

    "chainplate_tang": {
        "name": "Kettenpfanne Bolzen",
        "material": "Stainless Steel 316 or Bronze",
        "swl_to_break_ratio": 5.0,
        "inspection_criteria": [
            "fastener_torque_security",
            "tang_straightness_alignment",
            "tang_hole_wear_enlargement",
            "corrosion_pitting_appearance",
            "deck_interface_sealing",
            "mechanical_load_verification"
        ],
        "wear_indicators": [
            "fastener_loosening_vibration",
            "tang_slight_bending_deformation",
            "tang_hole_deformation_ovality",
            "corrosion_staining_salt_encrustation"
        ],
        "replacement_criteria": [
            "fastener_loosened_stripped",
            "tang_bent_or_broken",
            "tang_hole_enlarged_damaged",
            "corrosion_perforation_weakness",
            "safety_load_test_failure"
        ],
        "quality_criteria": {
            "material": "stainless_or_bronze",
            "fastener": "stainless_lock_nut_required",
            "tang_alignment": "load_axis_verified",
            "deck_sealing": "sealant_bed_continuous",
            "mechanical_integrity": "no_movement_or_play"
        },
        "common_failures": [
            "fastener_loosening_cyclic_tension",
            "tang_bending_overload_fatigue",
            "tang_hole_wear_enlargement",
            "corrosion_crevice_fatigue",
            "deck_cracking_stress_concentration"
        ]
    }
}

# ==============================================================================
# 5. SEALANT_SELECTION_MATRIX - Application-specific sealant recommendations
# ==============================================================================

SEALANT_SELECTION_MATRIX = {
    "deck_hardware": {
        "recommended_sealant": "polyurethane_marine_sealant_3M_5200_or_similar",
        "alternative": "polysulfide_marine_sealant",
        "NOT_to_use": ["silicone_general_purpose", "acrylic_caulk", "oil_based_putty"],
        "primer_required": False,
        "surface_prep": "clean_dry_dust_free_degrease_with_solvent",
        "cure_time_days": 7,
        "life_expectancy_years": 10,
        "quality_criteria": {
            "application_depth_mm": "6_to_8",
            "bead_width_mm": "minimum_8",
            "no_voids": "continuous_full_depth",
            "surface_finish": "smooth_no_skin_formation",
            "adhesion": "no_separation_perimeter"
        }
    },

    "window_portlight": {
        "recommended_sealant": "polyurethane_marine_sealant",
        "alternative": "polysulfide_marine_sealant",
        "NOT_to_use": ["silicone", "acrylic", "butyl_tape"],
        "primer_required": True,
        "surface_prep": "clean_glass_frame_with_degreaser_sand_surface_lightly",
        "cure_time_days": 7,
        "life_expectancy_years": 8,
        "quality_criteria": {
            "application_depth_mm": "4_to_6",
            "bead_width_mm": "8_to_10",
            "glass_contact": "3mm_minimum_all_sides",
            "frame_contact": "continuous_no_gaps",
            "surface_finish": "smooth_no_bubbles"
        }
    },

    "hull_deck_joint": {
        "recommended_sealant": "polyurethane_marine_sealant_high_strength",
        "alternative": "polysulfide_marine_sealant",
        "NOT_to_use": ["silicone", "acrylic", "temporary_sealant"],
        "primer_required": True,
        "surface_prep": "sand_clean_remove_all_old_sealant_degrease",
        "cure_time_days": 14,
        "life_expectancy_years": 12,
        "quality_criteria": {
            "application_depth_mm": "8_to_10",
            "bead_width_mm": "10_to_15",
            "void_free": "no_air_pockets_full_depth",
            "hull_contact": "continuous_even_pressure",
            "deck_contact": "continuous_sealed_edge"
        }
    },

    "underwater_fitting": {
        "recommended_sealant": "polysulfide_marine_sealant_submerged_rated",
        "alternative": "polyurethane_marine_sealant_submerged",
        "NOT_to_use": ["silicone_any_type", "acrylic", "vinyl_latex"],
        "primer_required": True,
        "surface_prep": "sand_smooth_clean_degrease_dry_completely",
        "cure_time_days": 21,
        "life_expectancy_years": 15,
        "quality_criteria": {
            "application_depth_mm": "6_to_8",
            "bead_width_mm": "8_to_12",
            "fitting_contact": "continuous_no_gaps",
            "hull_contact": "even_pressure",
            "submerged_integrity": "verified_test_tank"
        }
    },

    "keel_attachment": {
        "recommended_sealant": "polyurethane_marine_sealant_high_strength",
        "alternative": "polysulfide_marine_sealant",
        "NOT_to_use": ["silicone", "acrylic", "flexible_caulk"],
        "primer_required": True,
        "surface_prep": "sand_clean_remove_moisture_completely_degrease",
        "cure_time_days": 21,
        "life_expectancy_years": 15,
        "quality_criteria": {
            "application_depth_mm": "10_to_12",
            "bead_width_mm": "12_to_15",
            "keel_contact": "continuous_full_length",
            "hull_contact": "continuous_full_bearing",
            "void_free": "structural_integrity_verified"
        }
    },

    "teak_deck": {
        "recommended_sealant": "teak_sealing_compound_or_polyurethane",
        "alternative": "marine_epoxy_sealant",
        "NOT_to_use": ["silicone_stains_teak", "water_based_latex"],
        "primer_required": False,
        "surface_prep": "clean_teak_dry_remove_sand_dust_degrease",
        "cure_time_days": 7,
        "life_expectancy_years": 3,
        "quality_criteria": {
            "application_depth_mm": "2_to_4",
            "bead_width_mm": "3_to_5",
            "teak_contact": "continuous_even",
            "no_staining": "compatible_teak_wood",
            "appearance": "natural_teak_color_preserved"
        }
    },

    "portlight_framing": {
        "recommended_sealant": "polyurethane_marine_sealant",
        "alternative": "polysulfide_marine_sealant",
        "NOT_to_use": ["silicone_gas_escape", "acrylic", "butyl_inadequate"],
        "primer_required": True,
        "surface_prep": "clean_frame_glass_sand_lightly_degrease",
        "cure_time_days": 7,
        "life_expectancy_years": 8,
        "quality_criteria": {
            "application_depth_mm": "4_to_6",
            "bead_width_mm": "6_to_8",
            "frame_contact": "continuous_all_edges",
            "glass_contact": "minimum_2mm_all_sides",
            "surface_finish": "smooth_professional_appearance"
        }
    },

    "chainplate_base": {
        "recommended_sealant": "polyurethane_marine_sealant",
        "alternative": "polysulfide_marine_sealant",
        "NOT_to_use": ["silicone", "acrylic", "weak_adhesion_sealant"],
        "primer_required": True,
        "surface_prep": "sand_deck_surface_clean_remove_old_sealant_degrease",
        "cure_time_days": 7,
        "life_expectancy_years": 10,
        "quality_criteria": {
            "application_depth_mm": "6_to_8",
            "bead_width_mm": "8_to_10",
            "deck_contact": "continuous_under_plate",
            "plate_contact": "full_perimeter_sealed",
            "fillet": "smooth_no_sharp_edge"
        }
    },

    "through_hull_fitting": {
        "recommended_sealant": "polysulfide_marine_sealant",
        "alternative": "polyurethane_marine_sealant",
        "NOT_to_use": ["silicone_gas_escape", "acrylic", "temporary_sealant"],
        "primer_required": True,
        "surface_prep": "sand_hull_clean_remove_moisture_degrease_thoroughly",
        "cure_time_days": 14,
        "life_expectancy_years": 12,
        "quality_criteria": {
            "application_depth_mm": "6_to_8",
            "bead_width_mm": "8_to_12",
            "fitting_contact": "continuous_no_voids",
            "hull_contact": "full_bearing_surface",
            "backing_block": "full_contact_under_plate"
        }
    },

    "engine_mount_isolation": {
        "recommended_sealant": "marine_polyurethane_vibration_rated",
        "alternative": "polysulfide_marine_sealant",
        "NOT_to_use": ["general_purpose_silicone", "acrylic", "water_based"],
        "primer_required": True,
        "surface_prep": "clean_mount_surface_degrease_remove_old_sealant",
        "cure_time_days": 7,
        "life_expectancy_years": 5,
        "quality_criteria": {
            "application_depth_mm": "4_to_6",
            "bead_width_mm": "6_to_8",
            "mount_contact": "continuous_even_pressure",
            "no_voids": "full_depth_application",
            "elasticity": "flexible_accommodate_vibration"
        }
    }
}

# ==============================================================================
# 6. TORQUE_PATTERNS - Fastener tightening sequences and procedures
# ==============================================================================

TORQUE_PATTERNS = {
    "star_pattern_4bolt": {
        "description": "Cross-pattern four-bolt torque sequence for even load distribution",
        "sequence": [1, 3, 2, 4],
        "first_pass_pct": 50,
        "second_pass_pct": 75,
        "final_pass_pct": 100,
        "wait_between_passes_minutes": 15
    },

    "star_pattern_6bolt": {
        "description": "Six-bolt star pattern for even circular load distribution",
        "sequence": [1, 4, 2, 5, 3, 6],
        "first_pass_pct": 40,
        "second_pass_pct": 70,
        "final_pass_pct": 100,
        "wait_between_passes_minutes": 15
    },

    "star_pattern_8bolt": {
        "description": "Eight-bolt star pattern for large mounted equipment",
        "sequence": [1, 5, 2, 6, 3, 7, 4, 8],
        "first_pass_pct": 35,
        "second_pass_pct": 65,
        "final_pass_pct": 100,
        "wait_between_passes_minutes": 15
    },

    "sequential_line": {
        "description": "Sequential tightening along a line for track or rail mounting",
        "sequence": [1, 2, 3, 4, 5],
        "first_pass_pct": 50,
        "second_pass_pct": 75,
        "final_pass_pct": 100,
        "wait_between_passes_minutes": 10
    },

    "three_pass_method": {
        "description": "Three-pass method for critical structural fastening",
        "sequence": ["all_fasteners_sequentially"],
        "first_pass_pct": 30,
        "second_pass_pct": 60,
        "final_pass_pct": 100,
        "wait_between_passes_minutes": 20
    }
}

# ============================================================================
# THREAD TYPES MARINE — Gewindearten im Detail
# ============================================================================

THREAD_TYPES_MARINE = {
    "metric_coarse": {
        "name_de": "Metrisches Regelgewinde (ISO)",
        "standard": "ISO 261 / DIN 13",
        "sizes_common": ["M4", "M5", "M6", "M8", "M10", "M12", "M16", "M20"],
        "use": "Standard im europäischen Bootsbau, Deckshardware",
        "note": "Bevorzugt in Europa — bei Nachrüstung immer prüfen ob metrisch oder zöllig",
    },
    "metric_fine": {
        "name_de": "Metrisches Feingewinde",
        "standard": "ISO 261 / DIN 13",
        "advantage": "Höhere Vorspannkraft, geringere Lockerungstendenz",
        "use": "Motorenbefestigung, Rigg-Spanner, hoch belastete Verbindungen",
    },
    "unc": {
        "name_de": "UNC (Unified Coarse — US-Grobgewinde)",
        "standard": "ANSI/ASME B1.1",
        "sizes_common": ["1/4-20", "5/16-18", "3/8-16", "1/2-13", "5/8-11"],
        "use": "US-Boote, Harken/Lewmar-Beschläge teilweise UNC",
        "warning": "NICHT mit metrisch verwechseln — M6 ≠ 1/4 UNC!",
    },
    "unf": {
        "name_de": "UNF (Unified Fine — US-Feingewinde)",
        "standard": "ANSI/ASME B1.1",
        "use": "Hochbelastete Verbindungen, Rigg-Beschläge, Propellermuttern",
        "advantage": "Höhere Klemmkraft als UNC bei gleichem Durchmesser",
    },
    "bsp_pipe": {
        "name_de": "BSP (British Standard Pipe) / G-Gewinde",
        "standard": "ISO 228 (parallel) / ISO 7 (konisch)",
        "use": "Rohrverschraubungen, Seeventile, Schlauchstutzen",
        "sealing": {
            "parallel_bspp": "Dichtung durch O-Ring oder Flachdichtung",
            "taper_bspt": "Dichtung durch Gewindeform + Teflonband oder Hanf/Loctite 577",
        },
        "sizes_common": ["1/4 BSP", "3/8 BSP", "1/2 BSP", "3/4 BSP", "1 BSP", "1-1/2 BSP"],
    },
    "whitworth": {
        "name_de": "Whitworth (BSW/BSF)",
        "note": "Veraltet, aber auf älteren englischen Booten zu finden",
        "recognition": "55° Flankenwinkel (metrisch = 60°, UNC = 60°)",
        "use": "Restauration klassischer Yachten, Vintage-Beschläge",
    },
}

# ============================================================================
# THREAD LOCKING — Gewindesicherung (Loctite-Typen)
# ============================================================================

THREAD_LOCKING = {
    "loctite_222": {
        "name_de": "Loctite 222 (lila — niedrigfest)",
        "strength": "niedrig",
        "breakaway_torque_nm": 3,
        "use": "Kleine Schrauben (M2-M6), Einstellschrauben, Instrumenten-Befestigung",
        "disassembly": "Mit Handwerkzeug lösbar",
        "temperature_max_c": 150,
    },
    "loctite_243": {
        "name_de": "Loctite 243 (blau — mittelfest)",
        "strength": "mittel",
        "breakaway_torque_nm": 15,
        "use": "Standard-Sicherung M6-M20, Decksbeschläge, Klampen",
        "disassembly": "Mit Handwerkzeug lösbar (bei Bedarf erwärmen)",
        "temperature_max_c": 180,
        "oil_tolerant": True,
        "note": "STANDARD für die meisten Marine-Anwendungen",
    },
    "loctite_271": {
        "name_de": "Loctite 271 (rot — hochfest)",
        "strength": "hoch",
        "breakaway_torque_nm": 30,
        "use": "Dauerhafte Verbindungen: Stevenrohr, Wellenanlage, Kielbolzen-Muttern",
        "disassembly": "Nur mit Erwärmung >250°C lösbar",
        "temperature_max_c": 230,
        "warning": "Nur verwenden wenn KEINE Demontage geplant — sonst 243 nehmen!",
    },
    "loctite_638": {
        "name_de": "Loctite 638 (grün — Buchsen/Lagersicherung)",
        "strength": "hoch",
        "type": "Fügeprodukt für zylindrische Teile",
        "use": "Buchsen einkleben, Lagersitze sichern, Ruderkoker-Buchse",
        "gap_fill_mm": 0.25,
    },
    "loctite_577": {
        "name_de": "Loctite 577 (gelb — Gewindedichtung)",
        "type": "Rohrgewinde-Dichtmittel",
        "use": "BSP-Gewinde, Seeventile, Rohrverschraubungen",
        "pressure_max_bar": 10,
        "temperature_max_c": 150,
        "advantage": "Ersetzt Teflonband und Hanf — einstellbar nach Aushärtung",
    },
}

# ============================================================================
# WELDING MARINE — Schweißverbindungen (WIG/TIG Parameter)
# ============================================================================

WELDING_MARINE = {
    "tig_stainless_316": {
        "name_de": "WIG/TIG Edelstahl AISI 316",
        "process": "WIG (Wolfram-Inertgas) / TIG",
        "filler_wire": "ER316L (niedrig-Kohlenstoff)",
        "shielding_gas": "Argon 99.99%",
        "back_purge": "PFLICHT — Formiergas (Argon/N2 95/5) auf Rückseite",
        "amperage_range_a": {"1mm": "30-50", "2mm": "50-80", "3mm": "80-120"},
        "interpass_temp_max_c": 150,
        "post_weld": "Beizen mit Beizpaste (HF/HNO3) + Passivieren",
        "common_defects": [
            "Anlauffarben (>350°C = Chromverarmung → Korrosion)",
            "Schweißverzug (dünne Bleche!)",
            "Heißrisse bei zu hoher Schweißgeschwindigkeit",
        ],
    },
    "tig_aluminium_5083": {
        "name_de": "WIG/TIG Aluminium 5083 (Marine-Alu)",
        "process": "WIG AC (Wechselstrom)",
        "filler_wire": "ER5356 oder ER5183",
        "shielding_gas": "Argon 99.99%",
        "amperage_range_a": {"2mm": "60-90", "3mm": "90-130", "5mm": "130-200"},
        "preheat": "Nicht nötig bis 6mm, ab 6mm: 50-80°C",
        "post_weld": "Keine Wärmebehandlung bei 5083 (würde Korrosionsbeständigkeit senken)",
        "cleaning": "Oxidschicht entfernen mit Edelstahl-Drahtbürste (NUR für Alu reserviert!)",
        "common_defects": [
            "Porosität (Feuchtigkeit, Verschmutzung)",
            "Fehlende Durchschweißung (Oxide nicht entfernt)",
            "Risse in Wärmeeinflusszone (HAZ)",
        ],
    },
    "tig_bronze_silicon": {
        "name_de": "WIG/TIG Siliziumbronze",
        "process": "WIG DC (Gleichstrom, Elektrode minus)",
        "filler_wire": "ERCuSi-A",
        "shielding_gas": "Argon",
        "use": "Reparatur von Bronze-Beschlägen, Seeventile, Propeller",
        "note": "Siliziumbronze zum Löt-Schweißen von Stahl/GFK-Verbindungen",
    },
}

# ==============================================================================
# 7. ASSESSMENT FUNCTION - Evaluate fastener installations
# ==============================================================================

def assess_fastener_installation(
    fastener_type: str,
    hardware: str,
    material_substrate: str,
    location: str,
    torque_applied_nm: float = None,
    sealant_used: str = None,
    backing_plate_present: bool = None
) -> dict:
    """
    Comprehensive assessment of fastener installation quality and compliance.
    
    Args:
        fastener_type: Key from MARINE_FASTENERS dict
        hardware: Key from DECK_HARDWARE_MOUNTING dict
        material_substrate: "GRP" | "aluminum" | "wood_teak" | "wood_oak" | "carbon_steel"
        location: "deck" | "hull" | "underwater" | "mast" | "cabin"
        torque_applied_nm: Actual torque applied (for verification)
        sealant_used: Type of sealant applied
        backing_plate_present: Whether backing plate was installed
    
    Returns:
        dict with keys: score (0-100), findings (list), critical_issues (list),
                       recommendations (list), compliance_status (str)
    """
    
    findings = []
    critical_issues = []
    recommendations = []
    score = 100
    
    # Validate inputs
    if fastener_type not in MARINE_FASTENERS:
        return {
            "score": 0,
            "findings": [f"Unknown fastener type: {fastener_type}"],
            "critical_issues": ["Invalid fastener specification"],
            "recommendations": ["Select fastener from MARINE_FASTENERS dict"],
            "compliance_status": "INVALID"
        }
    
    fastener_spec = MARINE_FASTENERS[fastener_type]
    
    # Check fastener suitability for location
    if location not in fastener_spec.get("suitable_for", []):
        if location in fastener_spec.get("not_suitable_for", []):
            critical_issues.append(
                f"Fastener {fastener_type} explicitly NOT suitable for {location}"
            )
            score -= 30
        else:
            findings.append(
                f"Fastener {fastener_type} application at {location} not explicitly listed"
            )
            score -= 10
    
    # Check substrate compatibility
    galvanic_compat = fastener_spec.get("galvanic_compatibility", {})
    substrate_compat_map = {
        "GRP": "GRP",
        "aluminum": "aluminium",
        "wood_teak": "teak",
        "wood_oak": "oak",
        "carbon_steel": "carbon_steel",
        "bronze": "bronze",
        "stainless_steel": "stainless_steel"
    }
    
    substrate_key = substrate_compat_map.get(material_substrate)
    if substrate_key and substrate_key in galvanic_compat:
        compat = galvanic_compat[substrate_key]
        if "isolation" in compat.lower():
            recommendations.append(
                f"Install galvanic isolation washer between {fastener_type} and {material_substrate}"
            )
            score -= 5
        elif "avoid" in compat.lower():
            critical_issues.append(
                f"Galvanic incompatibility: {fastener_type} on {material_substrate}"
            )
            score -= 25
        else:
            findings.append(
                f"Galvanic compatibility {fastener_type} / {material_substrate}: {compat}"
            )
    
    # Verify backing plate requirement
    if hardware in DECK_HARDWARE_MOUNTING:
        hardware_spec = DECK_HARDWARE_MOUNTING[hardware]
        
        if hardware_spec.get("backing_plate_required") and not backing_plate_present:
            critical_issues.append(
                f"Backing plate required for {hardware} but not installed"
            )
            score -= 20
            
        if backing_plate_present:
            findings.append("Backing plate installed as required")
        
        # Check typical fasteners compatibility
        typical = hardware_spec.get("typical_fasteners", [])
        if fastener_type not in typical:
            findings.append(
                f"Fastener {fastener_type} not in typical list for {hardware}: {typical}"
            )
            score -= 5
    
    # Verify torque value if provided
    if torque_applied_nm is not None:
        torque_spec = fastener_spec.get("torque_values_nm", {})
        # For simplicity, check if torque is in reasonable range (allow 10% tolerance)
        if torque_spec:
            avg_torque = sum(torque_spec.values()) / len(torque_spec)
            if abs(torque_applied_nm - avg_torque) / avg_torque > 0.20:
                recommendations.append(
                    f"Verify torque {torque_applied_nm}Nm is correct for fastener size "
                    f"(typical range {min(torque_spec.values())}-{max(torque_spec.values())}Nm)"
                )
                score -= 10
    
    # Verify sealant if in marine environment
    if location in ["deck", "underwater", "hull"]:
        if sealant_used:
            finding_msg = f"Sealant {sealant_used} applied"
            if "polyurethane" in sealant_used.lower() or "polysulfide" in sealant_used.lower():
                finding_msg += " - marine-grade sealant confirmed"
            else:
                recommendations.append(
                    f"Consider marine-grade polyurethane or polysulfide sealant "
                    f"instead of {sealant_used}"
                )
                score -= 10
            findings.append(finding_msg)
        elif fastener_spec.get("quality_criteria", {}).get("sealant_requirement") != "not_required":
            critical_issues.append(
                f"Sealant required for {fastener_type} in {location} but not applied"
            )
            score -= 15
    
    # Inspection interval recommendation
    inspection_months = fastener_spec.get("inspection_interval_months", 12)
    recommendations.append(
        f"Schedule inspection every {inspection_months} months "
        f"(next due in {inspection_months} months from installation)"
    )
    
    # Compile compliance status
    if critical_issues:
        compliance_status = "NON-COMPLIANT"
    elif score >= 90:
        compliance_status = "COMPLIANT"
    elif score >= 75:
        compliance_status = "ACCEPTABLE_WITH_NOTES"
    else:
        compliance_status = "REQUIRES_REVIEW"
    
    return {
        "score": max(0, score),
        "findings": findings,
        "critical_issues": critical_issues,
        "recommendations": recommendations,
        "compliance_status": compliance_status,
        "fastener_details": fastener_spec.get("name"),
        "inspection_interval_months": inspection_months
    }


# ==============================================================================
# Example usage and verification
# ==============================================================================

if __name__ == "__main__":
    # Example: Assess chainplate installation
    result = assess_fastener_installation(
        fastener_type="through_bolt_316",
        hardware="chainplate",
        material_substrate="GRP",
        location="deck",
        torque_applied_nm=63.0,
        sealant_used="polyurethane_marine_sealant",
        backing_plate_present=True
    )
    
    print("=" * 70)
    print("FASTENER INSTALLATION ASSESSMENT")
    print("=" * 70)
    print(f"Compliance Status: {result['compliance_status']}")
    print(f"Assessment Score: {result['score']}/100")
    print(f"\nFastener: {result['fastener_details']}")
    print(f"Inspection Interval: Every {result['inspection_interval_months']} months")
    print(f"\nFindings:")
    for finding in result['findings']:
        print(f"  ✓ {finding}")
    if result['critical_issues']:
        print(f"\nCritical Issues:")
        for issue in result['critical_issues']:
            print(f"  ✗ {issue}")
    print(f"\nRecommendations:")
    for rec in result['recommendations']:
        print(f"  → {rec}")
    print("=" * 70)
