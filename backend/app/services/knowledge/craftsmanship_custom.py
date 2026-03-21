"""
AYDI Custom Fitting and Adaptation Knowledge Base
Master yacht interior fitting and custom fabrication reference
German language knowledge bases with English code comments
"""

# ==============================================================================
# CUSTOM FITTING TECHNIQUES
# Specialized methods for measuring, templating, and adapting components
# ==============================================================================

CUSTOM_FIT_TECHNIQUES = {
    "template_making_cardboard": {
        "name": "Kartonschablonenherstellung",
        "description": "Einfache Kartonschablone für Grundform und Passung",
        "accuracy_mm": 3,  # Standard tolerance for cardboard templates
        "suitable_for": [
            "bulkhead_liner_rough_fit",
            "sole_panel_outline",
            "companionway_steps_profile",
            "initial_measurement",
            "complex_curved_surfaces"
        ],
        "tools_required": [
            "corrugated_cardboard",
            "kraft_paper",
            "marker",
            "scissors",
            "flexible_curve",
            "straightedge"
        ],
        "time_factor": 1.0,  # Baseline time = 100%
        "quality_criteria": {
            "outline_clarity": "sharp, well-marked edges",
            "contour_matching": "follows hull/deck curves within 5mm",
            "hole_positioning": "accuracy ±5mm",
            "repeatability": "consistent when transferred"
        },
        "common_mistakes": [
            "template_deformation_during_storage",
            "inaccurate_edge_marking",
            "poor_cutout_for_obstructions",
            "not_accounting_for_material_thickness",
            "cardboard_shifting_during_tracing"
        ],
        "when_preferred": {
            "boat_types": ["traditional_wooden", "custom_build", "retrofit"],
            "situations": [
                "first_prototype_fit",
                "complex_irregular_shapes",
                "budget_conscious_work",
                "onsite_unavailable_fabrication",
                "learning_and_verification"
            ],
            "hull_materials": ["wood", "fiberglass", "epoxy"]
        }
    },

    "template_making_plywood": {
        "name": "Sperrholzschablonenherstellung",
        "description": "Präzise Sperrholzschablone für Serienfertigung",
        "accuracy_mm": 1.5,  # Higher precision than cardboard
        "suitable_for": [
            "multiple_identical_components",
            "permanent_template_storage",
            "high_precision_fitting",
            "cabinet_doors",
            "berth_platforms",
            "structural_components"
        ],
        "tools_required": [
            "birch_plywood_6mm",
            "jigsaw_or_circular_saw",
            "rasp",
            "sandpaper_80_120_grit",
            "measuring_tape",
            "pencil",
            "carpenter_square"
        ],
        "time_factor": 2.0,  # 200% longer than cardboard
        "quality_criteria": {
            "dimensional_accuracy": "within 1.5mm",
            "surface_smoothness": "rasped and sanded clean",
            "edge_clarity": "sharp, well-defined",
            "durability": "resistant to warping and damage",
            "label_clarity": "clearly marked for orientation and reuse"
        },
        "common_mistakes": [
            "plywood_warping_after_cutting",
            "inexact_saw_cuts",
            "not_leaving_witness_marks",
            "template_thickness_not_accounted_for",
            "edge_splintering"
        ],
        "when_preferred": {
            "boat_types": ["production", "semi_custom", "large_fleets"],
            "situations": [
                "production_run_of_5_or_more",
                "long_term_storage_needed",
                "high_precision_critical",
                "wear_resistant_template_needed",
                "CNC_machine_template_input"
            ],
            "hull_materials": ["fiberglass", "aluminum", "composite"]
        }
    },

    "digital_templating_laser": {
        "name": "Digitale Vorlagenerstellung mit Laser-Scanning",
        "description": "3D-Laserscanning und CNC-Fertigung",
        "accuracy_mm": 0.5,  # Professional laser accuracy
        "suitable_for": [
            "complex_3D_shapes",
            "engine_room_components",
            "high_precision_metalwork",
            "dashboard_bezels",
            "solar_panel_mounts",
            "electronic_integration"
        ],
        "tools_required": [
            "laser_scanner_3D",
            "CAD_software",
            "CNC_router_or_waterjet",
            "measurement_calibration_block",
            "point_cloud_processing_software"
        ],
        "time_factor": 3.5,  # 350% - includes scanning, processing, CAM
        "quality_criteria": {
            "point_cloud_density": "minimum_10_points_per_cm2",
            "data_alignment": "scanner_calibration_<0.3mm",
            "component_fit": "first_trial_fit_acceptable",
            "repeatability": "100%_consistent_across_batches",
            "delivery_time": "CAD_data_same_day_possible"
        },
        "common_mistakes": [
            "poor_scanner_calibration",
            "inadequate_point_cloud_filtering",
            "material_reflectivity_issues",
            "CAM_tool_path_interference",
            "alignment_reference_marker_placement"
        ],
        "when_preferred": {
            "boat_types": ["large_yacht", "production", "technical_custom"],
            "situations": [
                "production_series_50_plus",
                "sub_0.5mm_tolerance_required",
                "retrofit_matching_existing_shape",
                "engine_room_tight_fit",
                "performance_critical_aerodynamic",
                "digital_archive_needed"
            ],
            "hull_materials": ["any_material", "mixed_materials"]
        }
    },

    "spiling_board": {
        "name": "Spilling-Board (Messlehre mit beweglichen Stiften)",
        "description": "Traditionelle Methode mit einstellbaren Messstiften",
        "accuracy_mm": 2.0,
        "suitable_for": [
            "complex_irregular_shaping",
            "hull_fairing_measurement",
            "planking_profile",
            "cabin_top_intersection",
            "keel_to_hull_interface"
        ],
        "tools_required": [
            "spiling_board_frame",
            "adjustable_pins_or_sliding_needles",
            "reference_baseline",
            "marking_surface",
            "measurement_transfer_device"
        ],
        "time_factor": 2.5,  # Slower than templates but captures nuance
        "quality_criteria": {
            "pin_registration": "smooth, repeatable movement",
            "baseline_accuracy": "established with tolerance ±1mm",
            "profile_smoothness": "continuous curve without steps",
            "transferability": "profile can be reproduced accurately"
        },
        "common_mistakes": [
            "pins_not_perpendicular_to_baseline",
            "baseline_not_truly_straight",
            "pin_friction_causing_binding",
            "baseline_reference_shift",
            "measuring_without_steady_technique"
        ],
        "when_preferred": {
            "boat_types": ["traditional_wood", "custom_fit"],
            "situations": [
                "highly_curved_surfaces",
                "single_item_fitting",
                "master_craftsman_verification",
                "traditional_boat_building_methods",
                "documentation_and_archive"
            ],
            "hull_materials": ["wood", "fiberglass", "epoxy"]
        }
    },

    "tick_stick_method": {
        "name": "Tick-Stick-Methode (Kerbstab-Messung)",
        "description": "Messkern mit Markierungen für Abstandsmessung",
        "accuracy_mm": 1.0,
        "suitable_for": [
            "gap_measurement_fitting",
            "bulkhead_hull_interface",
            "deck_edge_offset",
            "sole_panel_edge_fit",
            "locker_frame_fit",
            "door_frame_gaps"
        ],
        "tools_required": [
            "hardwood_stick_10x10mm",
            "sharp_pencil_or_marking_knife",
            "dividers_or_calipers",
            "straightedge_reference"
        ],
        "time_factor": 0.7,  # Quick and efficient
        "quality_criteria": {
            "mark_clarity": "sharp, deep marks visible",
            "measurement_accuracy": "repeatable within 0.5mm",
            "transfer_accuracy": "marks reproduce shape correctly",
            "durability": "marks persist through handling"
        },
        "common_mistakes": [
            "stick_not_held_perpendicular",
            "marks_too_shallow_or_unclear",
            "reference_surface_not_truly_flat",
            "stick_bending_during_measurement",
            "marks_bleeding_or_running"
        ],
        "when_preferred": {
            "boat_types": ["all_types"],
            "situations": [
                "continuous_irregular_edges",
                "quick_field_measurement",
                "small_adjustments_and_fitting",
                "gap_profiling",
                "integration_with_existing_structure"
            ],
            "hull_materials": ["any"]
        }
    },

    "direct_scribing": {
        "name": "Direktes Anreißen (Scribe-Fit-Methode)",
        "description": "Direktes Anzeichnen auf dem Werkstoff mit Messwerkzeugen",
        "accuracy_mm": 1.5,
        "suitable_for": [
            "trim_and_fit_carpentry",
            "panel_edge_scribing",
            "joint_interface_marking",
            "frame_integration"
        ],
        "tools_required": [
            "scribe_tool_spring_loaded",
            "marking_gauge",
            "dividers",
            "sharp_pencil",
            "reference_straight_edge"
        ],
        "time_factor": 1.0,
        "quality_criteria": {
            "scribe_line_consistency": "continuous, fine line",
            "line_clarity": "easily followed for cutting",
            "accuracy": "within ±1.5mm of intended fit",
            "surface_marking": "marks cleanly without tearing grain"
        },
        "common_mistakes": [
            "tool_pressure_too_heavy_causing_gouges",
            "tool_angle_inconsistent",
            "reference_surface_not_flat",
            "line_breaks_in_tight_areas",
            "removing_reference_before_cutting"
        ],
        "when_preferred": {
            "boat_types": ["wood", "custom_build"],
            "situations": [
                "timber_or_plywood_components",
                "close_fit_to_curved_hull",
                "fast_field_adaptation",
                "no_power_tools_available",
                "craftsman_preference"
            ],
            "hull_materials": ["wood", "fiberglass"]
        }
    },

    "contour_gauge_transfer": {
        "name": "Konturlehre-Übertragung (Formenlehre)",
        "description": "Flexible Schablone für komplexe Konturen",
        "accuracy_mm": 2.0,
        "suitable_for": [
            "complex_profiles",
            "curved_surface_matching",
            "irregular_shaping",
            "edge_fitting",
            "interface_profiling"
        ],
        "tools_required": [
            "contour_gauge_25_or_40cm",
            "marking_surface",
            "pencil",
            "coping_saw_or_jigsaw",
            "rasp_and_file"
        ],
        "time_factor": 1.2,
        "quality_criteria": {
            "profile_flexibility": "holds shape without drift",
            "pin_stability": "pins don't slip or shift",
            "transfer_accuracy": "reproduced profile matches within 2mm",
            "edge_definition": "clear profile line for cutting"
        },
        "common_mistakes": [
            "gauge_not_held_perpendicular",
            "pins_not_flush_with_surface",
            "gauge_deformation_during_storage",
            "transferring_to_wrong_orientation",
            "not_securing_gauge_during_transfer"
        ],
        "when_preferred": {
            "boat_types": ["retrofit", "custom_fit"],
            "situations": [
                "field_adaptation_measurement",
                "quick_profile_capture",
                "single_item_fitting",
                "irregular_surface_matching",
                "non_contact_measurement"
            ],
            "hull_materials": ["any"]
        }
    },

    "pattern_projection": {
        "name": "Musterprojektion (Digitale Projektion auf Bauteil)",
        "description": "Digitale Lichtprojektion des geplanten Musters auf Komponente",
        "accuracy_mm": 3.0,  # Accuracy depends on projector and surface
        "suitable_for": [
            "large_panel_marking",
            "dashboard_layout_visualization",
            "interior_design_preview",
            "joinery_layout",
            "complex_multi_part_assembly"
        ],
        "tools_required": [
            "projector_1000_lumens_minimum",
            "CAD_software_export",
            "darkened_work_space",
            "laser_distance_measurement",
            "marking_tools_pen_chalk"
        ],
        "time_factor": 2.0,  # Setup and alignment time
        "quality_criteria": {
            "projection_focus": "sharp lines within 3mm",
            "color_contrast": "visible on component material",
            "alignment_accuracy": "projection matches component within 3mm",
            "image_stability": "no drift during marking"
        },
        "common_mistakes": [
            "projector_not_perpendicular_to_surface",
            "inadequate_workspace_lighting_control",
            "CAD_model_scale_error",
            "projector_heat_causing_shutdown",
            "surface_texture_reducing_contrast"
        ],
        "when_preferred": {
            "boat_types": ["modern_custom", "large_yacht", "technical_fit"],
            "situations": [
                "full_interior_layout_preview",
                "multi_component_assembly_planning",
                "client_approval_visualization",
                "complex_joinery_coordination",
                "error_verification_before_cutting"
            ],
            "hull_materials": ["any"]
        }
    }
}


# ==============================================================================
# INTERIOR FITTING COMPONENTS
# Detailed specifications for custom yacht interior work
# ==============================================================================

INTERIOR_FITTING = {
    "companionway_steps": {
        "name": "Niedergang/Treppenstufen",
        "description": "Maßgeschneiderte Stufen mit Passform zur Rumpfkrümmung",
        "materials_typical": [
            "teak_planking_25-35mm",
            "mahogany_solid_or_veneer",
            "coated_plywood",
            "stainless_steel_edge_protection",
            "non_slip_tape_or_finish"
        ],
        "fit_tolerance_mm": 2.0,  # Structural fit tolerance
        "expansion_gap_mm": 0.5,  # Teak expansion coefficient: 0.001 per °C per 100mm width
        "fastening_method": [
            "stainless_steel_screws_countersunk",
            "epoxy_adhesive_backup",
            "deck_cleat_mounting",
            "structural_core_integration"
        ],
        "moisture_considerations": {
            "annual_movement": "±2-3mm depending on width and humidity",
            "equilibrium_moisture_content": "12% for teak, 10-15% for plywood core",
            "ventilation_critical": True,
            "protective_finish": "polyurethane_or_epoxy_3coats_minimum"
        },
        "quality_criteria": {
            "fit": "snug integration with deck edge, no rocking",
            "finish": "smooth tread surface, clean joinery",
            "function": "safe grip, minimum 150mm tread width, 200mm rise typical"
        },
        "common_problems": [
            "crown_warping_from_humidity_cycling",
            "loose_edge_trim_due_to_expansion",
            "slippery_tread_surface_in_wet_conditions",
            "fastener_corrosion_and_staining",
            "misalignment_with_deck_slope"
        ],
        "assessment_checklist": [
            "tread_surface_flatness_check_straightedge",
            "fastener_integrity_visual_and_torque",
            "edge_trim_adhesion_tap_test",
            "non_slip_surface_condition",
            "no_visible_gaps_or_cracks",
            "expansion_gap_measurement",
            "color_and_finish_consistency",
            "hardware_corrosion_inspection"
        ]
    },

    "galley_countertop": {
        "name": "Kombüsen-Arbeitsfläche",
        "description": "Robuste Arbeitsfläche mit Wasser- und Stoßfestigkeit",
        "materials_typical": [
            "teak_endgrain_25mm",
            "coated_plywood_15+15mm",
            "stainless_steel_inlay_sections",
            "solid_surface_material",
            "epoxy_composite"
        ],
        "fit_tolerance_mm": 3.0,  # Allows for deck curvature integration
        "expansion_gap_mm": 1.0,  # For teak movement in high-moisture environment
        "fastening_method": [
            "tabletop_fasteners_wooden_buttons",
            "stainless_epoxy_adhesive",
            "structural_mounting_cleats",
            "shimmed_support_blocking"
        ],
        "moisture_considerations": {
            "galley_humidity": "80-95% typical operational humidity",
            "moisture_protection": "epoxy_sealer_underside_critical",
            "edge_sealing": "essential_to_prevent_core_delamination",
            "ventilation": "promote_air_circulation_beneath_counter",
            "maintenance": "regular_drying_and_inspection_required"
        },
        "quality_criteria": {
            "fit": "level surface within 2mm over 1m, aligned with sink and stove",
            "finish": "durable, non-slip when wet, easy to clean",
            "function": "adequate_workspace_min_600mm_depth, heat_resistant"
        },
        "common_problems": [
            "core_delamination_from_sink_splashing",
            "edge_swelling_and_cupping",
            "fastener_corrosion_staining_wood",
            "surface_wear_and_finish_breakdown",
            "unsealed_edges_allowing_water_ingress",
            "movement_causing_tile_or_edge_cracking"
        ],
        "assessment_checklist": [
            "surface_level_check_straightedge_and_level",
            "deck_integration_gap_measurement",
            "fastener_condition_and_tightness",
            "underside_moisture_and_mold_inspection",
            "edge_banding_integrity_and_adhesion",
            "sink_integration_and_sealing",
            "stove_integration_and_clearance",
            "overall_finish_condition",
            "movement_indicators_cracks_or_gaps"
        ]
    },

    "nav_station_desk": {
        "name": "Navigationstisch/Kartentisch",
        "description": "Ebene, robuste Arbeitsfläche für Seekarten und Navigation",
        "materials_typical": [
            "teak_plywood_21mm",
            "marine_grade_plywood_core",
            "stainless_steel_edge_trim",
            "non_slip_surface_coat"
        ],
        "fit_tolerance_mm": 1.5,  # Navigation precision requires flatness
        "expansion_gap_mm": 0.5,
        "fastening_method": [
            "stainless_bolts_through_structural_support",
            "epoxy_adhesive_reinforcement",
            "vibration_damping_rubber_isolators"
        ],
        "moisture_considerations": {
            "typical_moisture_level": "electronics_cool_zone_generally_lower_humidity",
            "equipment_ventilation": "ensure_airflow_around_electronics",
            "surface_protection": "prevent_condensation_buildup",
            "cable_management": "moisture_resistant_routing"
        },
        "quality_criteria": {
            "fit": "perfectly level surface, flatness ±1mm/meter critical",
            "finish": "smooth, anti_glare, non_slip surface",
            "function": "stable platform, min_600x800mm for chart work, adequate lighting"
        },
        "common_problems": [
            "sagging_or_flex_under_equipment_weight",
            "surface_reflection_issues_with_electronics",
            "cable_interference_with_movement",
            "inadequate_equipment_cooling",
            "electronic_interference_from_metal_trim"
        ],
        "assessment_checklist": [
            "flatness_measurement_with_straightedge_and_laser_level",
            "surface_level_X_and_Y_directions",
            "structural_support_deflection_under_load",
            "equipment_mounting_vibration_check",
            "cable_routing_and_strain_relief",
            "finish_condition_wear_and_damage",
            "electronic_grounding_and_shielding",
            "lighting_adequacy_and_glare_assessment"
        ]
    },

    "berth_cushion_platform": {
        "name": "Schlafplatz-Polsterung/Mattform",
        "description": "Strukturierte Plattform für Matratzenlagerung und Komfort",
        "materials_typical": [
            "marine_plywood_18_21mm",
            "epoxy_sealed_wood_framing",
            "closed_cell_foam_core",
            "high_resilience_polyurethane_foam",
            "fabric_covering_solution_dyed"
        ],
        "fit_tolerance_mm": 5.0,  # Comfort fit allows more tolerance
        "expansion_gap_mm": 2.0,  # Berth areas subject to condensation
        "fastening_method": [
            "structural_frame_bolts_and_brackets",
            "elastic_straps_for_movement_absorption",
            "ventilation_slats_for_air_circulation",
            "stapled_fabric_attachment"
        ],
        "moisture_considerations": {
            "condensation_risk": "very_high_at_hull_side_berths",
            "ventilation": "critical_beneath_berth_essential",
            "moisture_barrier": "vapor_barrier_on_hull_contact_side",
            "air_circulation": "slats_or_spacers_minimum_10mm",
            "regular_inspection": "mold_and_moisture_checking_essential"
        },
        "quality_criteria": {
            "fit": "snug hull integration, even weight distribution",
            "finish": "clean fabric, no_wrinkles or sags, professional_seaming",
            "function": "comfortable_sleep_support, ergonomic_positioning, min_600mm_width"
        },
        "common_problems": [
            "mold_growth_from_condensation_and_poor_ventilation",
            "delamination_of_plywood_from_moisture",
            "sagging_or_permanent_deformation",
            "inadequate_cushion_support_or_comfort",
            "fabric_deterioration_from_mildew",
            "hull_contact_creating_cold_spots"
        ],
        "assessment_checklist": [
            "hull_contact_surface_dry_and_clean",
            "ventilation_space_verified_beneath_platform",
            "plywood_structural_integrity_no_soft_spots",
            "cushion_condition_and_compression",
            "fabric_seams_integrity_and_covering_quality",
            "no_moisture_stains_or_discoloration",
            "ventilation_slat_clearance_adequate",
            "anti_mold_treatment_applied_or_needed",
            "weight_distribution_and_frame_deflection",
            "comfort_level_assessment_body_pressure_points"
        ]
    },

    "locker_doors_frames": {
        "name": "Spindtüren und Rahmenkonstruktion",
        "description": "Rahmen und Türen für Stauräume mit korrosionsfreier Konstruktion",
        "materials_typical": [
            "teak_or_mahogany_frame_20x20mm",
            "teak_plywood_panels_9_12mm",
            "marine_grade_hinges_stainless_or_bronze",
            "magnetic_catches_or_friction_hinges",
            "stainless_steel_handle_and_knob"
        ],
        "fit_tolerance_mm": 2.5,  # Door alignment critical for function
        "expansion_gap_mm": 1.0,  # Teak/mahogany movement accommodation
        "fastening_method": [
            "mortise_and_tenon_frame_joinery",
            "stainless_screws_countersunk_and_plugged",
            "epoxy_adhesive_joint_reinforcement",
            "hinge_mounting_with_through_bolts"
        ],
        "moisture_considerations": {
            "interior_storage_environment": "moderate_humidity_usually_interior_locker",
            "frame_construction": "solid_hardwood_preferred_for_stability",
            "joint_sealing": "epoxy_fill_exterior_joints",
            "door_sealing": "optional_weather_sealing_for_exposed_locker",
            "ventilation": "ensure_air_circulation_inside_locker"
        },
        "quality_criteria": {
            "fit": "frame integrates flush with adjacent structure, door closes smoothly",
            "finish": "clean_grain_exposed_wood, consistent_color_and_depth",
            "function": "doors operate smoothly, latches_securely, hinges_silent"
        },
        "common_problems": [
            "door_sag_over_time_from_weight",
            "hinge_corrosion_causing_binding",
            "wood_splitting_at_screw_penetration",
            "door_gap_increasing_from_frame_deflection",
            "latch_failure_from_vibration_loosening",
            "moisture_infiltration_at_edge_joints"
        ],
        "assessment_checklist": [
            "frame_plumb_check_both_directions",
            "door_alignment_gap_measurement_all_sides",
            "hinge_operation_smooth_no_binding",
            "latch_engagement_and_function",
            "wood_condition_cracks_or_soft_spots",
            "fastener_tightness_visual_and_torque",
            "finish_condition_wear_or_damage",
            "moisture_stains_or_mold_indicators",
            "hardware_corrosion_inspection"
        ]
    },

    "sole_panels": {
        "name": "Bootsdeckel/Soleplatten (Fußboden)",
        "description": "Einzelne Paneele für angepassten Kabinensollerfußboden",
        "materials_typical": [
            "teak_planking_solid_20_28mm",
            "teak_plywood_12_15mm",
            "holly_accents_or_contrast_stringing",
            "epoxy_sealed_plywood_core",
            "non_slip_surface_treatment"
        ],
        "fit_tolerance_mm": 3.0,  # Slight gaps acceptable between planks
        "expansion_gap_mm": 1.5,  # Teak movement in high-traffic moist area
        "fastening_method": [
            "stainless_steel_screws_blind_fastened",
            "epoxy_adhesive_bed_and_backup",
            "wooden_or_composite_support_battens",
            "elastic_mounting_isolators"
        ],
        "moisture_considerations": {
            "foot_traffic_moisture": "constant_wet_conditions_cabin_sole",
            "drainage_and_drying": "must_allow_water_flow_to_bilge",
            "underside_ventilation": "critical_for_mold_prevention",
            "seasonal_movement": "±2-3mm width movement typical",
            "finish_durability": "UV_and_moisture_resistant_coating_essential"
        },
        "quality_criteria": {
            "fit": "tight_joints_between_planks_no_gaps_greater_than_1mm",
            "finish": "smooth_surface_splinter_free_uniform_color",
            "function": "safe_non_slip_surface_proper_drainage_water_flow"
        },
        "common_problems": [
            "warping_and_cupping_from_moisture_cycling",
            "water_pooling_and_rotting_if_drainage_blocked",
            "loose_or_squeaky_planks_from_fastener_failure",
            "slippery_surface_in_wet_conditions",
            "edge_splinter_and_deterioration",
            "mold_and_mildew_growth_on_underside"
        ],
        "assessment_checklist": [
            "surface_level_check_with_straightedge",
            "plank_joint_gaps_measurement_all_seams",
            "fastener_tightness_no_squeaks_or_movement",
            "water_drainage_path_verification",
            "underside_moisture_inspection_ventilation_check",
            "surface_finish_condition_non_slip_treatment",
            "wood_condition_no_soft_spots_or_rot",
            "color_consistency_and_grain_match",
            "edge_condition_no_splinters_or_cracks",
            "secure_support_underneath_no_deflection"
        ]
    },

    "headliner_panels": {
        "name": "Kopfdeckel/Überkopf-Verkleidung",
        "description": "Deckenverkleidung für Kabineninnenseite mit Wärme- und Feuchtigkeitsschutz",
        "materials_typical": [
            "marine_plywood_6_9mm",
            "fiberglass_cloth_reinforced_panels",
            "closed_cell_foam_backing",
            "fabric_covering_flame_retardant",
            "epoxy_edge_banding"
        ],
        "fit_tolerance_mm": 5.0,  # Structural fit less critical than aesthetic
        "expansion_gap_mm": 2.0,  # Foam and fabric will compress slightly
        "fastening_method": [
            "lightweight_stainless_fasteners_discrete_mounting",
            "trim_molding_conceals_fasteners",
            "adhesive_plus_fastener_combined_approach",
            "tension_straps_for_large_panels"
        ],
        "moisture_considerations": {
            "condensation_risk": "high_especially_cold_weather",
            "ventilation_space": "minimum_10mm_air_gap_to_deck_structure",
            "foam_backing": "closed_cell_preferred_moisture_resistant",
            "vapor_barrier": "optional_depending_on_climate_zone",
            "mold_prevention": "dark_color_fabric_shows_less_mold"
        },
        "quality_criteria": {
            "fit": "smooth_continuous_surface_no_sagging_or_bulges",
            "finish": "even_color_professional_seaming_clean_edge_molding",
            "function": "light_diffusion_sound_absorption_thermal_insulation"
        },
        "common_problems": [
            "sagging_from_inadequate_support_or_foam_compression",
            "condensation_and_mold_at_fabric_interface",
            "water_staining_from_deck_leaks_above",
            "fastener_showing_and_degrading_appearance",
            "fabric_deterioration_from_UV_exposure",
            "sound_echo_if_insufficient_absorption"
        ],
        "assessment_checklist": [
            "visual_inspection_for_sagging_or_bulges",
            "moisture_stains_or_discoloration_check",
            "fastener_concealment_and_finish_quality",
            "edge_molding_fit_and_condition",
            "fabric_seam_integrity_and_appearance",
            "no_visible_creases_or_wrinkles",
            "ventilation_space_verification_if_accessible",
            "attachment_tightness_gentle_push_test",
            "overall_color_uniformity_and_condition",
            "acoustic_quality_basic_sound_test"
        ]
    },

    "bulkhead_liners": {
        "name": "Schottverkleidung/Schott-Innenseite",
        "description": "Verkleidete Schotten mit Wärmeschutz und Optik",
        "materials_typical": [
            "thin_marine_plywood_3_6mm",
            "teak_veneer_or_mahogany_veneer",
            "closed_cell_foam_insulation_backing",
            "stainless_steel_trim_and_edge_banding",
            "epoxy_sealed_joints"
        ],
        "fit_tolerance_mm": 2.0,  # Visible surface requires good fit
        "expansion_gap_mm": 0.5,  # Veneer panels have minimal movement
        "fastening_method": [
            "stainless_screws_countersunk_and_plugged",
            "contact_adhesive_plus_fasteners",
            "wooden_trim_conceals_fastener_heads",
            "edge_molding_aluminum_or_stainless"
        ],
        "moisture_considerations": {
            "structural_bulkhead": "behind_liner_must_remain_dry",
            "ventilation": "air_gap_critical_behind_panel",
            "vapor_barrier": "may_be_integrated_into_foam_backing",
            "inspection_access": "ensure_ability_to_inspect_structure_behind",
            "condensation": "monitor_for_moisture_at_interface"
        },
        "quality_criteria": {
            "fit": "panels_seam_cleanly_at_joints_no_gaps_visible",
            "finish": "uniform_grain_and_color_professional_seaming",
            "function": "contributes_to_interior_insulation_and_appearance"
        },
        "common_problems": [
            "veneer_delamination_from_moisture_or_impact",
            "visible_fastener_marks_reducing_appearance",
            "edge_splitting_at_fastener_penetration",
            "seam_opening_from_movement_or_impact",
            "moisture_accumulation_behind_panel",
            "color_fading_from_sun_exposure",
            "impact_cracking_or_puncture_of_thin_material"
        ],
        "assessment_checklist": [
            "visual_surface_condition_scratches_cracks_damage",
            "fastener_condition_and_concealment_quality",
            "seam_tightness_and_alignment",
            "edge_molding_fit_and_condition",
            "color_and_grain_consistency",
            "veneer_adhesion_tap_test_hollow_sound_indicates_failure",
            "structural_bulkhead_behind_dry_check_if_accessible",
            "trim_molding_tight_and_secure",
            "corner_detail_and_protection",
            "overall_cleanliness_and_finish_quality"
        ]
    },

    "fiddle_rails": {
        "name": "Falltische/Fiddlebrettnachhalter (Reling auf Möbeln)",
        "description": "Rahmen zum Sichern von Gegenständen gegen Verschieben in Seegängen",
        "materials_typical": [
            "teak_or_mahogany_hardwood_25mm_diameter",
            "stainless_steel_hinges_and_brackets",
            "polyurethane_or_leather_bumpers",
            "stainless_or_bronze_fasteners"
        ],
        "fit_tolerance_mm": 2.0,
        "expansion_gap_mm": 0.0,  # Rail fixed position, no movement
        "fastening_method": [
            "stainless_steel_bolts_through_structure",
            "structural_epoxy_adhesive_backup",
            "hinge_pins_installed_last_for_easy_removal"
        ],
        "moisture_considerations": {
            "exterior_rail_exposure": "if_on_deck_full_UV_and_salt_exposure",
            "interior_rail_lower_moisture": "protected_from_direct_spray",
            "finish_protection": "UV_resistant_seal_annual_maintenance",
            "fastener_corrosion": "stainless_essential_no_mild_steel"
        },
        "quality_criteria": {
            "fit": "secure_attachment_no_rocking_smooth_operation",
            "finish": "smooth_wood_comfortable_grip_no_splinters",
            "function": "effective_retention_of_tableware_objects_stable_when_flipped"
        },
        "common_problems": [
            "loose_fasteners_from_vibration_and_movement",
            "wood_splitting_at_fastener_penetration",
            "hinge_corrosion_binding_motion",
            "inadequate_retention_in_heavy_seas",
            "fastener_corrosion_staining_wood"
        ],
        "assessment_checklist": [
            "attachment_tightness_no_movement",
            "hinge_operation_smooth_silent",
            "fastener_corrosion_inspection",
            "wood_surface_smooth_no_splinters",
            "bumper_pads_intact_and_functional",
            "structural_backing_intact_no_cracking",
            "movement_range_adequate_and_smooth",
            "finish_condition_and_sealing"
        ]
    },

    "handrail_custom": {
        "name": "Handgriff/Reling (maßgefertigt)",
        "description": "Strukturelle Sicherheitsreling für Bewegung an Bord",
        "materials_typical": [
            "teak_hardwood_solid_30-40mm_diameter",
            "stainless_steel_core_option",
            "stainless_steel_brackets_heavy_duty",
            "teak_or_stainless_finish"
        ],
        "fit_tolerance_mm": 1.0,  # Safety critical, close fit required
        "expansion_gap_mm": 0.0,  # Fixed installation
        "fastening_method": [
            "stainless_steel_through_bolts_structural",
            "epoxy_bedding_and_fastener_combination",
            "fiberglass_reinforced_mounting_blocks",
            "vibration_damping_washers"
        ],
        "moisture_considerations": {
            "exposed_location": "high_moisture_constant_salt_spray",
            "wood_protection": "epoxy_end_sealing_critical",
            "fastener_isolation": "stainless_essential_no_dissimilar_metals",
            "maintenance": "regular_inspection_and_reoiling_needed",
            "finish_durability": "annual_refinishing_recommended"
        },
        "quality_criteria": {
            "fit": "firmly_attached_no_movement_or_flex_structural_load_rated",
            "finish": "smooth_tactile_comfortable_grip",
            "function": "capable_of_supporting_person_full_body_weight_safely"
        },
        "common_problems": [
            "loose_bolts_from_vibration_and_ship_motion",
            "through_bolt_corrosion_weakening_attachment",
            "wood_splitting_at_fastener_concentration",
            "salt_spray_damage_even_on_stainless",
            "inadequate_bracket_design_for_structural_load",
            "water_intrusion_at_fastener_penetration"
        ],
        "assessment_checklist": [
            "attachment_security_firm_no_movement",
            "through_bolt_condition_torque_spec_verification",
            "wood_condition_no_cracks_or_soft_spots",
            "finish_sealing_adequate_no_exposure",
            "fastener_corrosion_inspection",
            "bracket_structural_integrity_no_cracks",
            "load_test_if_accessible_full_body_weight",
            "diameter_and_grip_ergonomic",
            "surface_finish_smooth_no_splinters",
            "drainage_and_ventilation_around_mounting"
        ]
    },

    "trim_moldings": {
        "name": "Zierleisten/Kantenschutz (Profilleisten)",
        "description": "Dekorative und funktionale Kantenabdeckung und Übergänge",
        "materials_typical": [
            "teak_or_mahogany_solid_or_veneer",
            "stainless_steel_angle_or_trim",
            "aluminum_anodized_finish",
            "rubber_or_PVC_profile_bumper",
            "composite_synthetic_trim"
        ],
        "fit_tolerance_mm": 1.5,  # Visible detail requires good fit
        "expansion_gap_mm": 0.5,  # Minimal movement for trim
        "fastening_method": [
            "stainless_fasteners_countersunk_plugged",
            "contact_adhesive_plus_fastener_backup",
            "crimp_or_adhesive_only_for_metal_trim",
            "trim_screws_every_150-200mm"
        ],
        "moisture_considerations": {
            "edge_protection": "shields_underlying_material_from_water_ingress",
            "joint_sealing": "caulk_as_needed_to_prevent_water_penetration",
            "finish_maintenance": "same_as_underlying_component_typically",
            "impact_resistance": "absorbs_minor_impacts_protecting_structure"
        },
        "quality_criteria": {
            "fit": "tight_joints_at_corners_and_seams_no_gaps",
            "finish": "clean_lines_professional_appearance_consistent_color",
            "function": "protects_edges_provides_visual_break_and_safety"
        },
        "common_problems": [
            "loose_trim_from_fastener_failure",
            "corner_separation_from_expansion_contraction",
            "paint_or_finish_failure_along_edge",
            "water_intrusion_behind_trim_if_caulking_fails",
            "mechanical_damage_to_trim_from_impact"
        ],
        "assessment_checklist": [
            "fastener_tightness_and_corrosion_check",
            "corner_joint_fit_and_adhesion",
            "caulking_integrity_if_present",
            "color_and_finish_consistency",
            "no_gaps_at_seams_or_transitions",
            "surface_condition_scratches_damage",
            "adhesion_tap_test_for_delamination",
            "water_penetration_check_behind_trim",
            "protective_function_adequate_edge_protection"
        ]
    },

    "cabinet_hardware": {
        "name": "Möbelbeschlag/Verschlüsse",
        "description": "Schlösser, Griffe, Scharniere für Schränke und Luken",
        "materials_typical": [
            "stainless_steel_grade_marine_316",
            "bronze_or_brass_traditional",
            "polymer_composite_handles",
            "marine_grade_fasteners",
            "cushioned_catches_magnetic_or_friction"
        ],
        "fit_tolerance_mm": 1.0,  # Functional hardware requires precision
        "expansion_gap_mm": 0.0,  # Fixed mounting
        "fastening_method": [
            "stainless_steel_screws_countersunk",
            "machine_bolts_through_fastened_preferred",
            "epoxy_adhesive_backup_reinforcement",
            "lock_washers_against_vibration_loosening"
        ],
        "moisture_considerations": {
            "salt_spray_environment": "stainless_316_essential_no_substitutes",
            "fastener_isolation": "stainless_only_with_stainless_wood",
            "drainage": "ensure_water_drainage_paths_around_hardware",
            "corrosion_monitoring": "regular_inspection_replacement_as_needed",
            "lubrication": "marine_grade_lubricant_for_hinges_and_locks"
        },
        "quality_criteria": {
            "fit": "precise_installation_no_movement_smooth_operation",
            "finish": "corrosion_free_polished_or_brushed_consistently",
            "function": "reliable_latching_smooth_motion_no_binding"
        },
        "common_problems": [
            "corrosion_and_rust_staining_on_fasteners",
            "loose_screws_from_vibration_and_motion",
            "handle_pull_stress_concentrations_causing_failure",
            "hinge_pin_corrosion_binding_door_motion",
            "lock_mechanism_salt_spray_damage",
            "dissimilar_metal_galvanic_corrosion"
        ],
        "assessment_checklist": [
            "fastener_condition_no_corrosion_staining",
            "hinge_operation_smooth_no_binding",
            "handle_pull_test_secure_no_movement",
            "latch_engagement_proper_closure",
            "lock_mechanism_operation_if_present",
            "fastener_tightness_torque_spec_check",
            "corrosion_or_salt_spray_damage",
            "finish_consistency_and_appearance",
            "wear_patterns_and_surface_condition",
            "vibration_loosening_visual_indicators"
        ]
    }
}


# ==============================================================================
# HULL AND STRUCTURAL FAIRING
# Surface preparation and alignment standards
# ==============================================================================

ALIGNMENT_AND_FAIRNESS = {
    "hull_fairing": {
        "name": "Rumpf-Spachtelung/Rumpfoberflächen-Ausgleich",
        "description": "Flächung und Ausgleich der äußeren Rumpfoberfläche",
        "filler_material": [
            "epoxy_polyester_filler_two_part",
            "high_build_polyester_putty",
            "fairing_compound_low_shrinkage",
            "fiberglass_reinforced_epoxy_heavy_repairs",
            "microballoon_epoxy_lightweight"
        ],
        "application_method": [
            "hand_trowel_small_areas",
            "pneumatic_spray_application_large_areas",
            "wet_on_wet_layup_technique",
            "block_fill_followed_by_sanding",
            "vacuum_injection_high_quality"
        ],
        "sanding_sequence": [
            "initial_80_grit_cutting_level",
            "progression_120_150_grit_shape",
            "finish_180_220_grit_surface_prep",
            "wet_sanding_final_400_600_grit_optional"
        ],
        "straightedge_tolerance_mm_per_m": 2.0,  # Typical fair curve tolerance
        "quality_criteria": {
            "visual": "continuous_fair_surface_no_depressions_or_high_spots",
            "measurement": "straightedge_check_fairness_within_2mm/meter",
            "finish": "smooth_surface_ready_for_paint_no_orange_peel_texture"
        },
        "common_defects": [
            "shrinkage_void_and_depression_formation",
            "sand_through_to_substrate_exposing_fiberglass",
            "wavy_surface_from_improper_troweling_technique",
            "hard_edge_at_repair_boundary_not_feathered",
            "filler_adhesion_failure_and_popping",
            "improper_filler_hardness_too_soft_or_brittle"
        ]
    },

    "deck_fairing": {
        "name": "Deck-Spachtelung/Deckenausgleich",
        "description": "Oberflächenausgleich und Spachtelung des Decks",
        "filler_material": [
            "epoxy_polyester_filler",
            "teak_color_filler_teak_deck",
            "white_polyester_filler_non_skid_deck",
            "flexible_polyurethane_filler_joint_sealing"
        ],
        "application_method": [
            "hand_trowel_teak_deck_application",
            "block_fill_large_deck_areas",
            "joint_injection_for_inter_plank_gaps",
            "spray_application_polyester_filler_large_area"
        ],
        "sanding_sequence": [
            "80_grit_initial_cutting_level",
            "120_grit_shape_and_surface_prep",
            "150_220_grit_final_finish",
            "non_skid_texture_maintained_if_required"
        ],
        "straightedge_tolerance_mm_per_m": 3.0,  # Deck can be less fair than hull
        "quality_criteria": {
            "visual": "smooth_integrated_surface_color_matched_to_deck",
            "measurement": "walkway_flatness_3mm_tolerance_per_meter",
            "finish": "ready_for_paint_non_skid_pattern_if_required"
        },
        "common_defects": [
            "color_mismatch_filler_visible_after_paint",
            "delamination_between_filler_and_teak_deck",
            "soft_filler_material_continued_movement",
            "low_spot_retention_water_pooling",
            "expansion_gap_closure_preventing_deck_movement"
        ]
    },

    "cabin_top_fairing": {
        "name": "Aufbauten-/Kabinendach-Spachtelung",
        "description": "Oberflächenausgleich und Nahtabdeckung an Aufbauten",
        "filler_material": [
            "epoxy_polyester_filler_standard",
            "adhesive_sealant_polyurethane_joint",
            "flexible_polyurethane_high_movement_areas",
            "fairing_compound_sandwich_core_integration"
        ],
        "application_method": [
            "injection_for_sandwich_core_sealing",
            "hand_trowel_edge_transitions",
            "spray_application_large_smooth_areas",
            "caulk_extrusion_flex_joint_integration"
        ],
        "sanding_sequence": [
            "80_grit_initial_core_preparation",
            "120_grit_level_and_shape",
            "180_220_grit_final_surface_prep",
            "wet_sanding_400_grit_optional_premium_finish"
        ],
        "straightedge_tolerance_mm_per_m": 2.5,  # Between deck and hull
        "quality_criteria": {
            "visual": "smooth_fair_transition_between_deck_and_cabin",
            "measurement": "cabin_top_fairness_2.5mm_tolerance_per_meter",
            "finish": "ready_for_gel_coat_paint_no_defects"
        },
        "common_defects": [
            "core_material_exposure_from_through_breach",
            "moisture_in_sandwich_core_delamination_risk",
            "hard_edge_at_original_mold_line_not_feathered",
            "filler_color_mismatch_with_final_finish",
            "inadequate_core_integration_point_loads"
        ]
    },

    "keel_hull_fairing": {
        "name": "Kielbereiche-Spachtelung (Hull-Keel-Übergang)",
        "description": "Präzisions-Spachtelung im kritischen Kielstoß",
        "filler_material": [
            "epoxy_filler_high_strength",
            "fiberglass_epoxy_structural_fill",
            "fairing_putty_low_shrinkage",
            "ceramic_filled_epoxy_ultra_hard"
        ],
        "application_method": [
            "wet_layup_structural_repair_major",
            "hand_application_small_defects",
            "vacuum_injection_core_sealing",
            "pressure_injection_void_elimination"
        ],
        "sanding_sequence": [
            "36_60_grit_aggressive_material_removal",
            "80_grit_shaping_and_leveling",
            "120_150_grit_surface_prep",
            "220_400_grit_final_finish_critical_area"
        ],
        "straightedge_tolerance_mm_per_m": 1.5,  # Strictest tolerance - performance critical
        "quality_criteria": {
            "visual": "invisible_repair_seamless_integration",
            "measurement": "keel_joint_fairness_1.5mm_per_meter_performance_critical",
            "strength": "filler_hardness_equal_or_greater_substrate"
        },
        "common_defects": [
            "structural_void_from_incomplete_fill",
            "filler_brittle_fracture_impact_or_flex",
            "moisture_intrusion_from_poor_sealing",
            "hydrodynamic_defect_from_fairness_variation",
            "paint_buildup_increasing_underwater_drag"
        ]
    },

    "rudder_fairing": {
        "name": "Ruder-Spachtelung/Ruder-Oberflächenausgleich",
        "description": "Präzisions-Spachtelung des Ruderprofiles (Hydrodynamik-kritisch)",
        "filler_material": [
            "epoxy_filler_ultra_smooth_low_shrinkage",
            "ceramic_filled_epoxy_exceptional_hardness",
            "polyurethane_filler_flexible_movement",
            "aerospace_grade_epoxy_critical_profiles"
        ],
        "application_method": [
            "hand_sculpting_small_areas",
            "spray_application_uniform_buildup",
            "block_filling_layering_technique",
            "CNC_profile_verification_after_fill"
        ],
        "sanding_sequence": [
            "60_80_grit_initial_sculpting",
            "120_150_grit_profile_shape_refinement",
            "220_grit_smooth_surface",
            "400_600_grit_wet_sand_final_polish_critical"
        ],
        "straightedge_tolerance_mm_per_m": 0.5,  # Ultra-precise - hydrodynamic performance critical
        "quality_criteria": {
            "visual": "mirror_smooth_surface_no_texture",
            "measurement": "rudder_profile_tolerance_0.5mm_per_meter_hydrodynamic_critical",
            "hydrodynamic": "profile_accuracy_impacts_handling_and_performance"
        },
        "common_defects": [
            "profile_distortion_changing_hydrodynamic_properties",
            "waviness_in_chord_profile_increasing_drag",
            "trailing_edge_thickness_variance",
            "excessive_paint_buildup_destroying_profile",
            "moisture_core_damage_weakening_structure"
        ]
    }
}


# ==============================================================================
# GAP AND TOLERANCE STANDARDS
# Acceptable spacing between components and materials
# ==============================================================================

GAP_AND_TOLERANCE_STANDARDS = {
    "teak_plank_gap": {
        "name": "Teakplanken-Fuge (Teak Decking Gap)",
        "target_gap_mm": 3,
        "acceptable_range_mm": [2, 4],  # Min-max acceptable
        "material_for_shimming": [
            "teak_shim_stock",
            "marine_plywood_spacer",
            "composite_deck_spacer"
        ],
        "filler_if_oversize": [
            "polyurethane_caulk_flexible",
            "polysulfide_sealant",
            "epoxy_teak_filler_if_gap_<5mm"
        ],
        "quality_criteria": {
            "visual": "uniform_gap_consistent_full_length_plank",
            "structural": "no_moisture_pooling_adequate_drainage",
            "expansion": "accounts_for_seasonal_teak_movement"
        }
    },

    "locker_door_gap": {
        "name": "Spindtür-Spalt (Locker Door Gap)",
        "target_gap_mm": 2.5,
        "acceptable_range_mm": [1.5, 3.5],
        "material_for_shimming": [
            "hardwood_shim_teak_mahogany",
            "composite_shim_plastic",
            "brass_shim_precision_fit"
        ],
        "filler_if_oversize": [
            "edge_banding_teak_or_mahogany",
            "epoxy_filler_final_sanding",
            "trim_molding_conceals_oversize_gap"
        ],
        "quality_criteria": {
            "visual": "consistent_gap_all_around_door_edge",
            "functional": "door_operates_smoothly_no_binding",
            "aesthetic": "uniform_appearance_all_edges"
        }
    },

    "companionway_hatch": {
        "name": "Niedergangs-Luken-Spalt",
        "target_gap_mm": 1.5,
        "acceptable_range_mm": [0.5, 2.5],
        "material_for_shimming": [
            "anodized_aluminum_shim",
            "stainless_steel_shim",
            "composite_threshold_spacer"
        ],
        "filler_if_oversize": [
            "polyurethane_threshold_seal",
            "neoprene_bulb_seal",
            "silicone_weather_seal"
        ],
        "quality_criteria": {
            "visual": "tight_seam_minimal_light_showing",
            "functional": "weather_tight_no_water_entry_in_seas",
            "safety": "no_tripping_hazard_smooth_threshold"
        }
    },

    "drawer_gap": {
        "name": "Schublade-Spalt (Galley Drawer Gap)",
        "target_gap_mm": 3,
        "acceptable_range_mm": [2, 4],
        "material_for_shimming": [
            "hardwood_frame_adjustment",
            "adjustable_slides_fine_tuning",
            "spacer_shim_behind_frame"
        ],
        "filler_if_oversize": [
            "edge_trim_frame_edge",
            "drawer_slide_shimming",
            "frame_dimension_enlargement"
        ],
        "quality_criteria": {
            "visual": "uniform_gaps_all_sides",
            "functional": "drawer_slides_smoothly_easy_operation",
            "content_security": "no_excessive_gap_allowing_spillage"
        }
    },

    "sole_panel_gap": {
        "name": "Bodenpaneel-Spalt (Sole Panel Gap)",
        "target_gap_mm": 1,
        "acceptable_range_mm": [0.5, 1.5],
        "material_for_shimming": [
            "teak_wedge_shim",
            "marine_plywood_spacer",
            "epoxy_adjustment_filler"
        ],
        "filler_if_oversize": [
            "epoxy_teak_dust_mixture",
            "polyurethane_caulk_flexible",
            "teak_edge_molding_conceals_gap"
        ],
        "quality_criteria": {
            "visual": "tight_seamless_joint",
            "functional": "no_water_pooling_drainage_path",
            "safety": "no_trip_hazard_smooth_transition"
        }
    },

    "portlight_frame": {
        "name": "Bullauge-Fassung (Portlight Frame Gap)",
        "target_gap_mm": 2,
        "acceptable_range_mm": [1, 3],
        "material_for_shimming": [
            "stainless_steel_shim",
            "aluminum_shim_anodized",
            "neoprene_gasket_spacer"
        ],
        "filler_if_oversize": [
            "polyurethane_sealant_exterior",
            "silicone_sealant_weatherproof",
            "neoprene_bulb_seal_compression"
        ],
        "quality_criteria": {
            "visual": "uniform_sealing_gap_all_around",
            "functional": "watertight_no_weeping_or_seepage",
            "structural": "proper_compression_gasket_contact"
        }
    },

    "window_frame": {
        "name": "Fenster-Fassung (Window Frame Gap)",
        "target_gap_mm": 1.5,
        "acceptable_range_mm": [0.5, 2.5],
        "material_for_shimming": [
            "stainless_steel_shim",
            "marine_grade_plastic_shim",
            "neoprene_gasket"
        ],
        "filler_if_oversize": [
            "silicone_sealant_clear",
            "polyurethane_sealant_colored",
            "compression_gasket_seal"
        ],
        "quality_criteria": {
            "visual": "consistent_gap_professional_appearance",
            "functional": "watertight_seal_no_fogging_interior",
            "structural": "proper_compression_gasket_seating"
        }
    },

    "hull_deck_joint": {
        "name": "Rumpf-Deck-Kante (Hull-Deck Joint)",
        "target_gap_mm": 2,
        "acceptable_range_mm": [1, 3],
        "material_for_shimming": [
            "stainless_steel_angle_spacer",
            "molded_composite_spacer",
            "adjustable_mounting_bracket"
        ],
        "filler_if_oversize": [
            "polyurethane_sealant_structural",
            "polysulfide_sealant_flexible",
            "epoxy_adhesive_sealant_rigid"
        ],
        "quality_criteria": {
            "visual": "uniform_gap_clean_line_no_steps",
            "structural": "no_water_intrusion_fully_sealed",
            "functional": "alignment_true_no_sag_or_deflection"
        }
    },

    "bulkhead_to_hull": {
        "name": "Schott-Rumpf-Verbindung (Bulkhead-Hull Interface)",
        "target_gap_mm": 0.5,
        "acceptable_range_mm": [0, 1],
        "material_for_shimming": [
            "epoxy_adhesive_bedding",
            "thin_composite_shim",
            "molded_epoxy_spacer"
        ],
        "filler_if_oversize": [
            "epoxy_filler_structural",
            "fiberglass_epoxy_tape_reinforced",
            "polyurethane_sealant_flexible"
        ],
        "quality_criteria": {
            "visual": "gap_barely_visible_structural_appearance",
            "structural": "full_contact_epoxy_bedding_complete",
            "functional": "no_movement_rigid_bulkhead_support"
        }
    },

    "engine_alignment": {
        "name": "Motor-Ausrichtung (Engine Alignment Tolerance)",
        "target_gap_mm": 0.0,  # Zero gap for mechanical fit
        "acceptable_range_mm": [-0.5, 0.5],  # Coupler flex tolerance
        "material_for_shimming": [
            "stainless_steel_shim_engine_bed",
            "brass_shim_precision_ground",
            "adjustable_engine_mounts"
        ],
        "filler_if_oversize": [
            "flexible_coupling_absorption",
            "vibration_isolator_damping",
            "re_machining_engine_bed_surface"
        ],
        "quality_criteria": {
            "visual": "no_visible_offset_prop_shaft_alignment",
            "functional": "smooth_propeller_rotation_no_vibration",
            "performance": "minimal_vibration_smooth_acceleration"
        }
    }
}


# ==============================================================================
# CUSTOM METALWORK FOR YACHTS
# Fabrication and finishing specifications for marine metalwork
# ==============================================================================

CUSTOM_METALWORK = {
    "stainless_fabrication": {
        "name": "Edelstahl-Fertigung (Stainless Steel Fabrication)",
        "material": "ASTM_A276_Type_316_or_higher",  # Marine grade essential
        "welding_method": [
            "TIG_tungsten_inert_gas_preferred",
            "MIG_metal_inert_gas_secondary",
            "manual_stick_welding_structural_heavy"
        ],
        "finish_requirement": [
            "mill_finish_standard",
            "brushed_#4_polish_common",
            "mirror_polish_premium_bright_work",
            "satin_finish_modern_aesthetic"
        ],
        "passivation": {
            "critical_for_marine": True,
            "specification": "ASTM_A967_passivation",
            "citric_acid_method": "preferred_non_toxic",
            "nitric_acid_method": "standard_harsh_chemical",
            "minimum_soak_time_hours": 24,
            "post_passivation_rinse": "critical_remove_residuals"
        },
        "quality_criteria": {
            "weld_appearance": "smooth_consistent_bead_no_spatter",
            "corrosion_resistance": "no_rust_staining_after_passivation",
            "dimensional_accuracy": "within_1mm_tolerance_functional_fit",
            "finish_consistency": "uniform_polish_or_brush_pattern"
        },
        "common_failures": [
            "sensitization_from_improper_heat_treatment",
            "stress_corrosion_cracking_high_tensile_stress",
            "crevice_corrosion_galvanic_couples_wrong_fasteners",
            "chloride_pitting_insufficient_passivation",
            "weld_porosity_weak_structural_joint",
            "dissimilar_metal_coupling_galvanic_corrosion"
        ]
    },

    "aluminum_fabrication": {
        "name": "Aluminium-Fertigung (Aluminum Fabrication)",
        "material": "6061_T6_or_5083_marine_grade",
        "welding_method": [
            "TIG_tungsten_inert_gas_only_method",
            "MIG_metal_inert_gas_secondary_acceptable"
        ],
        "finish_requirement": [
            "anodize_Type_II_12_25_microns_standard",
            "anodize_Type_III_25_50_microns_hard_coat",
            "clear_anodize_natural_aluminum_color",
            "colored_anodize_black_bronze_available"
        ],
        "passivation": {
            "not_used": "aluminum_uses_anodizing_not_passivation",
            "anodize_critical": True,
            "anodize_thickness": "20_microns_minimum_marine",
            "seal_after_anodize": "essential_corrosion_protection"
        },
        "quality_criteria": {
            "weld_quality": "consistent_smooth_bead_full_penetration",
            "anodize_uniformity": "consistent_color_thickness_all_surfaces",
            "finish_appearance": "smooth_no_pitting_or_white_oxide",
            "dimensional_accuracy": "within_1.5mm_functional_tolerance"
        },
        "common_failures": [
            "galvanic_corrosion_aluminum_with_stainless_fasteners",
            "inadequate_anodize_thickness_corrosion_breakthrough",
            "pitting_in_anodize_layer_allowing_base_corrosion",
            "weld_heat_affected_zone_strength_reduction",
            "salt_spray_corrosion_inadequate_coating",
            "fastener_corrosion_dissimilar_metal_contact"
        ]
    },

    "bronze_casting_repair": {
        "name": "Bronze-Guss/Reparatur (Bronze Casting Repair)",
        "material": "manganese_bronze_silicon_bronze_marine",
        "welding_method": [
            "bronze_welding_rod_lower_temperature",
            "tig_for_thin_section_repair",
            "gas_torch_small_repairs",
            "re_casting_for_major_damage"
        ],
        "finish_requirement": [
            "as_cast_traditional_appearance",
            "polished_bright_bright_work",
            "varnished_protective_clear_coat",
            "oil_finish_traditional_method"
        ],
        "passivation": {
            "not_applicable": "bronze_inherently_corrosion_resistant",
            "cleaning": "remove_scale_and_flux_residue_essential",
            "oil_protection": "light_oil_coating_maintenance"
        },
        "quality_criteria": {
            "weld_strength": "equal_or_greater_than_base_metal",
            "surface_finish": "smooth_no_porosity_or_inclusions",
            "appearance": "consistent_color_finish_appropriate_style",
            "fit_function": "repairs_restore_original_specification"
        },
        "common_failures": [
            "dezincification_loss_of_zinc_in_brass_alloys",
            "segregation_in_cast_section_porosity",
            "weld_porosity_weak_repair_points",
            "improper_heat_treatment_brittleness",
            "corrosion_at_weld_interface_dissimilar_alloy"
        ]
    },

    "custom_brackets": {
        "name": "Maßgefertigte Halterungen (Custom Brackets)",
        "material": "stainless_316_aluminum_6061_or_bronze",
        "welding_method": [
            "TIG_preferred_stainless",
            "MIG_aluminum",
            "bronze_welding_or_mechanical_fastening_bronze"
        ],
        "finish_requirement": [
            "mill_finish_functional_aesthetic",
            "polished_bright_work",
            "painted_protective_coating_color_match"
        ],
        "passivation": {
            "stainless_critical": True,
            "aluminum_anodize_essential": True,
            "bronze_minimal": "cleaning_only"
        },
        "quality_criteria": {
            "dimensional_accuracy": "within_1mm_assembly_fit",
            "structural_strength": "load_rating_documented",
            "installation_fit": "fastener_holes_accurate_alignment",
            "appearance": "consistent_finish_clean_lines"
        },
        "common_failures": [
            "corrosion_from_dissimilar_metals_poor_isolation",
            "stress_concentration_sharp_corners",
            "loose_fasteners_vibration_induced",
            "weld_cracks_thermal_stress",
            "inadequate_load_bearing_capacity_thin_stock"
        ]
    },

    "pulpit_modification": {
        "name": "Reling-Modifikation (Pulpit Modification)",
        "material": "stainless_316_tubing_32_38mm_dia",
        "welding_method": [
            "TIG_tungsten_inert_gas_primary",
            "structural_full_penetration_welds"
        ],
        "finish_requirement": [
            "polished_bright_work_standard",
            "brushed_matte_finish_alternative"
        ],
        "passivation": {
            "critical_safety_component": True,
            "ASTM_A967_essential": True,
            "full_coverage_passivation": "all_welds_and_surfaces"
        },
        "quality_criteria": {
            "weld_quality": "consistent_smooth_full_penetration",
            "structural_integrity": "no_cracks_no_porosity",
            "finish_corrosion_resistance": "bright_and_clean_no_discoloration",
            "safety_load_rating": "documented_certification"
        },
        "common_failures": [
            "weld_cracking_thermal_cycling",
            "corrosion_at_weld_HAZ_sensitization",
            "loose_fasteners_impact_vibration",
            "fatigue_failure_stress_concentration",
            "inadequate_structural_strength_design"
        ]
    },

    "solar_arch": {
        "name": "Sonnenkollektor-Bügel/Solaranlage-Struktur (Solar Arch)",
        "material": "anodized_aluminum_6061_T6_or_stainless_316",
        "welding_method": [
            "TIG_aluminum_preferred",
            "mechanical_fastening_composite_alternative"
        ],
        "finish_requirement": [
            "anodize_Type_II_clear_or_colored",
            "polished_stainless_bright_work",
            "powder_coat_color_match_hull"
        ],
        "passivation": {
            "aluminum_anodize_critical": True,
            "stainless_passivation_if_used": True,
            "UV_protection_essential": "UV_resistant_anodize_or_paint"
        },
        "quality_criteria": {
            "structural_load_capacity": "designed_wind_load_specifications",
            "electrical_isolation": "no_galvanic_coupling_to_hull",
            "finish_durability": "UV_resistant_5_year_minimum",
            "installation_accuracy": "true_alignment_smooth_operation"
        },
        "common_failures": [
            "galvanic_corrosion_dissimilar_metals",
            "inadequate_wind_load_design",
            "UV_degradation_finish_breakdown",
            "loose_fasteners_vibration_induced",
            "electrical_grounding_interference_electronics"
        ]
    },

    "davit_fabrication": {
        "name": "Bootskran-Fertigung (Davit Fabrication)",
        "material": "stainless_316_tubing_or_aluminum_6061",
        "welding_method": [
            "TIG_full_penetration_critical",
            "structural_welding_specifications_ABS_or_DNV"
        ],
        "finish_requirement": [
            "polished_stainless_bright_work",
            "anodize_aluminum_protection",
            "paint_protective_coating_color"
        ],
        "passivation": {
            "critical_safety_equipment": True,
            "full_structural_passivation_required": True,
            "periodic_inspection_recommended": "annually"
        },
        "quality_criteria": {
            "structural_strength": "certified_load_capacity_documentation",
            "weld_integrity": "radiographic_testing_if_required",
            "corrosion_resistance": "full_passivation_no_staining",
            "mechanical_function": "smooth_operation_locking_mechanisms"
        },
        "common_failures": [
            "stress_corrosion_cracking_service_history",
            "weld_cracks_fatigue_cycle_load",
            "corrosion_pitting_inadequate_finish",
            "mechanical_wear_fastener_seizure",
            "structural_failure_overload_or_impact"
        ]
    },

    "custom_tankage": {
        "name": "Maßgefertigte Tanks (Custom Tankage)",
        "material": "stainless_316_aluminum_5083_or_composite",
        "welding_method": [
            "TIG_full_penetration_internal_fillet_critical",
            "pressure_vessel_standards_ASME_or_equivalent"
        ],
        "finish_requirement": [
            "internal_smooth_weld_passivation_critical",
            "external_protective_paint_or_anodize",
            "epoxy_internal_coating_fuel_tanks_optional"
        ],
        "passivation": {
            "internal_passivation_critical": True,
            "electropolish_option_superior_quality": True,
            "contamination_testing_required": "post_passivation"
        },
        "quality_criteria": {
            "pressure_integrity": "hydrostatic_test_no_leaks",
            "weld_quality": "internal_fillet_smooth_continuous",
            "internal_cleanliness": "no_contamination_particles",
            "structural_certification": "compliance_standards_documentation"
        },
        "common_failures": [
            "weld_porosity_causing_slow_weep",
            "internal_corrosion_inadequate_passivation",
            "tank_stress_corrosion_cracking_service",
            "fastener_corrosion_water_tank_discoloration",
            "contamination_particulate_clogging_systems"
        ]
    }
}


# ==============================================================================
# SYSTEMS INTEGRATION
# Standards and routing guidelines for ship systems
# ==============================================================================

SYSTEMS_INTEGRATION = {
    "plumbing_routing": {
        "name": "Rohrleitungs-Verlegung (Plumbing Routing)",
        "standards": [
            "ISO_10856_marine_hose_specification",
            "ABYC_E11_marine_standards_compliance",
            "ABS_American_Bureau_Shipping_if_classed"
        ],
        "routing_rules": [
            "avoid_routing_above_electronics_or_navigation_systems",
            "support_hose_every_300_400mm_vibration_damping",
            "loop_rise_prevent_siphoning_through_seacock",
            "bilge_line_drain_lowest_point_complete_evacuation",
            "isolation_valves_each_through_hull_fitting_safety",
            "through_hull_fittings_2x_hose_diameter_minimum_clearance",
            "no_sharp_bends_minimum_10x_hose_diameter_radius",
            "separation_freshwater_and_greywater_different_colors"
        ],
        "quality_criteria": {
            "structural": "no_chafing_or_abrasion_points_protective_sleeves",
            "functional": "flow_rates_meet_system_demand_no_restriction",
            "safety": "no_siphon_risk_isolation_valves_functional",
            "longevity": "hose_replaced_per_manufacturer_lifespan_typically_10_years"
        },
        "inspection_checklist": [
            "through_hull_fitting_secure_no_weeping",
            "isolation_valve_operation_smooth_turnkey",
            "hose_clamps_tight_no_corrosion_or_separation",
            "chafe_protection_intact_no_hose_wear",
            "drain_loops_present_proper_loop_height",
            "separation_of_systems_visual_color_coding",
            "cleat_or_loop_spacing_adequate_no_vibration",
            "pressure_test_if_installed_no_leaks_under_load"
        ],
        "common_mistakes": [
            "using_non_marine_hose_inadequate_UV_resistance",
            "undersized_hose_flow_restriction_pump_cavitation",
            "routing_above_seacock_siphon_risk_water_intrusion",
            "missing_isolation_valves_difficult_maintenance",
            "inadequate_support_vibration_failure_hose_clamps",
            "sharp_bends_hose_cracking_blockage_risk",
            "wrong_hose_color_cross_contamination_risk"
        ]
    },

    "electrical_routing": {
        "name": "Elektroleitungs-Verlegung (Electrical Routing)",
        "standards": [
            "ABYC_E11_marine_electrical_standards",
            "ISO_13297_marine_electrical_safety",
            "NFPA_70_National_Electrical_Code_marine_supplement"
        ],
        "routing_rules": [
            "separate_power_and_signal_cables_minimum_50mm_distance",
            "use_marine_grade_tinned_copper_wire_corrosion_resistance",
            "cable_gauge_sized_for_circuit_amperage_voltage_drop_<3_percent",
            "bundle_cables_with_marine_grade_adhesive_lined_tubing",
            "through_deck_penetration_sealed_epoxy_or_stainless_glands",
            "circuit_protection_breaker_every_circuit_isolation",
            "no_routing_above_navigational_electronics",
            "strain_relief_all_connectors_secure_positions",
            "color_coding_red_positive_black_negative_yellow_switch_green_ground"
        ],
        "quality_criteria": {
            "insulation": "marine_grade_UV_resistant_no_cracks",
            "connections": "crimped_soldered_corrosion_free_no_corrosion_bloom",
            "routing": "supported_and_protected_no_sharp_bends",
            "labeling": "all_circuits_labeled_at_panel_and_termination"
        },
        "inspection_checklist": [
            "wire_gauge_adequate_per_circuit_amperage",
            "circuit_breaker_or_fuse_per_circuit_overload_protection",
            "main_battery_disconnect_accessible_safety_critical",
            "ground_straps_battery_to_engine_and_hull_secure",
            "no_visible_corrosion_or_oxidation_connectors",
            "cable_support_clamps_secure_no_vibration_damage",
            "through_hull_penetration_sealed_no_water_intrusion",
            "connector_sealed_covers_moisture_protection",
            "voltage_drop_test_if_circuits_<5_watts_loss",
            "continuity_test_all_circuits_proper_operation"
        ],
        "common_mistakes": [
            "undersized_wire_voltage_drop_dim_lights_slow_motor",
            "mixing_power_and_signal_cables_electromagnetic_interference",
            "corroded_connectors_poor_contact_intermittent_failure",
            "inadequate_circuit_protection_fire_risk",
            "poor_grounding_safety_hazard_electric_shock_risk",
            "routing_above_navigation_systems_interference",
            "missing_strain_relief_fatigue_wire_failure"
        ]
    },

    "cable_management": {
        "name": "Kabelführungs-Management (Cable Management)",
        "standards": [
            "marine_grade_cable_tray_stainless_or_coated",
            "separation_power_signal_data_physical_segregation"
        ],
        "routing_rules": [
            "use_labeled_cable_ties_marine_grade_UV_resistant",
            "avoid_cable_routing_engine_high_temperature_zones",
            "run_power_and_signal_in_separate_conduit_1mm_minimum_separation",
            "secure_cable_every_300mm_support_cleat_or_tie",
            "avoid_moisture_traps_secure_cable_above_water_level_when_possible",
            "connector_locations_accessible_maintenance_service",
            "color_coding_cables_functional_identification_at_glance"
        ],
        "quality_criteria": {
            "organization": "cables_neat_identified_organized_logical_paths",
            "protection": "cables_protected_abrasion_damage_pressure",
            "accessibility": "maintainable_serviceable_without_major_disassembly",
            "documentation": "diagram_updated_current_reality_actual_installation"
        },
        "inspection_checklist": [
            "cable_ties_secure_no_loose_or_missing_ties",
            "documentation_current_matches_physical_installation",
            "no_pinched_cables_or_visible_damage",
            "connector_accessible_replaceable_without_major_work",
            "separation_power_signal_visually_distinct_paths",
            "cable_support_spacing_adequate_no_sag",
            "grounding_continuity_hull_bonding_verified",
            "moisture_protection_no_water_pooling_cable_trays"
        ],
        "common_mistakes": [
            "poor_documentation_technician_confusion_troubleshooting_difficulty",
            "mixed_power_signal_cables_interference_noise",
            "inadequate_support_cable_chafing_failure",
            "hard_to_access_connections_maintenance_difficulty",
            "oversized_cable_bundle_difficult_routing_weight",
            "missing_cable_identification_confusion_troubleshooting"
        ]
    },

    "bilge_pump_installation": {
        "name": "Bilgenpumpen-Installation (Bilge Pump Installation)",
        "standards": [
            "ABYC_E11_bilge_system_safety",
            "ISO_10856_marine_pump_hose_specification"
        ],
        "routing_rules": [
            "suction_intake_lowest_bilge_point_full_evacuation",
            "discharge_above_waterline_prevent_siphon_back",
            "isolation_valves_suction_and_discharge_maintenance",
            "strainer_intake_prevent_blockage_25_mesh_recommended",
            "anti_siphon_hole_discharge_line_above_waterline",
            "backup_pump_manual_or_secondary_electric_safety",
            "shower_drain_greywater_to_holding_tank_separate_system"
        ],
        "quality_criteria": {
            "capacity": "pump_capacity_adequate_water_ingress_rate_plus_margin",
            "reliability": "dual_pump_system_or_manual_backup_safety_critical",
            "ease_of_use": "manual_pump_operable_from_cockpit_emergency_access",
            "maintenance": "filter_strainer_accessible_regular_cleaning"
        },
        "inspection_checklist": [
            "intake_strainer_clean_no_blockage",
            "suction_hose_intact_no_cracks_or_leaks",
            "discharge_through_hull_fitting_secure",
            "anti_siphon_hole_clear_no_blockage",
            "isolation_valves_operate_smoothly",
            "manual_pump_operation_accessible_clear",
            "backup_system_present_and_functional",
            "bilge_area_clean_regular_maintenance",
            "electrical_connections_secure_no_corrosion"
        ],
        "common_mistakes": [
            "single_pump_system_no_backup_catastrophic_failure_risk",
            "intake_too_high_pump_unable_to_evacuate_bilge",
            "discharge_below_waterline_siphon_water_intrusion_risk",
            "missing_anti_siphon_hole_water_backflow_damage",
            "inadequate_pump_capacity_water_accumulation",
            "blocked_strainer_pump_cavitation_failure"
        ]
    },

    "fuel_system": {
        "name": "Treibstoff-System (Fuel System)",
        "standards": [
            "ABYC_E09_fuel_system_safety_critical",
            "ISO_10856_marine_hose_fuel_specification"
        ],
        "routing_rules": [
            "fuel_tank_baffled_prevent_sloshing_fuel_starvation",
            "fill_deck_fitting_through_deck_remote_from_cabin",
            "fuel_line_stainless_steel_or_copper_not_aluminum",
            "isolation_valve_tank_outlet_maintenance_safety",
            "fuel_filter_accessible_regular_inspection",
            "vent_line_above_waterline_prevent_water_intrusion",
            "no_fuel_line_routing_through_cabin_fire_risk",
            "fuel_gauge_sender_tank_mounted_corrosion_resistant"
        ],
        "quality_criteria": {
            "safety": "no_fuel_fumes_in_cabin_ventilation_critical",
            "reliability": "fuel_delivery_consistent_no_starvation_in_rough_seas",
            "maintenance": "components_accessible_inspection_and_service",
            "longevity": "system_tested_no_leaks_under_operating_conditions"
        },
        "inspection_checklist": [
            "tank_secure_no_movement_or_vibration",
            "fuel_line_intact_no_cracks_weeping",
            "isolation_valve_function_security_check",
            "fuel_filter_condition_water_content_test",
            "vent_line_patent_not_blocked_no_vacuum",
            "deck_fill_cap_secure_tight_seal",
            "fuel_gauge_accuracy_verification",
            "no_visible_leaks_joints_or_connections",
            "ventilation_effective_no_fuel_odor_cabin"
        ],
        "common_mistakes": [
            "fuel_line_plastic_hose_inadequate_marine_specification",
            "missing_isolation_valve_maintenance_difficulty",
            "vent_line_inadequate_sizing_tank_vacuum",
            "fuel_line_routed_through_cabin_fire_hazard",
            "inadequate_filtration_water_contamination_engine_damage",
            "fuel_tank_unbaffle_fuel_starvation_rough_seas"
        ]
    },

    "water_system": {
        "name": "Frischwasser-System (Fresh Water System)",
        "standards": [
            "ABYC_E12_water_system_safety",
            "ISO_10856_marine_hose_water_specification"
        ],
        "routing_rules": [
            "water_tank_food_grade_plastic_or_stainless_internal_coating",
            "fill_deck_fitting_remote_from_fuel_and_sewage",
            "isolation_valve_tank_outlet_maintenance_flexibility",
            "water_heater_sized_galley_and_head_adequate_hot_water",
            "pressure_pump_maintain_15_20_psi_normal_operation",
            "check_valve_tank_inlet_prevent_backflow",
            "pressure_relief_valve_20_psi_pump_protection",
            "through_hull_fitting_metal_stainless_seacock_isolation"
        ],
        "quality_criteria": {
            "potability": "water_taste_odor_free_regular_inspection",
            "pressure": "consistent_flow_all_fixtures_no_restriction",
            "maintenance": "tanks_accessible_cleaning_regular_inspection",
            "reliability": "system_tested_no_leaks_normal_operation"
        },
        "inspection_checklist": [
            "tank_fill_level_gauge_accurate_functioning",
            "isolation_valve_operation_smooth_and_secure",
            "through_hull_fitting_secure_seacock_operation",
            "water_hose_intact_no_cracks_or_leaks",
            "pressure_pump_operation_normal_quiet_even_pressure",
            "water_heater_function_hot_water_adequate_temperature",
            "check_valve_function_no_backflow_contamination",
            "no_leaks_at_connections_joints_or_fittings",
            "water_taste_test_if_concern_contamination_check"
        ],
        "common_mistakes": [
            "water_tank_inadequate_size_frequent_refill_requirement",
            "missing_isolation_valve_maintenance_difficulty",
            "inadequate_pressure_pump_weak_flow_all_fixtures",
            "contamination_cross_connection_with_seawater_system",
            "inadequate_hot_water_capacity_poor_shower_experience",
            "pressure_pump_damage_over_pressurization_no_relief_valve"
        ]
    },

    "black_water_system": {
        "name": "Abwasser-System (Black Water/Sewage System)",
        "standards": [
            "ABYC_E13_marine_sanitation_device_standards",
            "ISO_10856_marine_hose_black_water_specification"
        ],
        "routing_rules": [
            "through_hull_fitting_minimum_500mm_above_waterline",
            "isolation_valve_discharge_through_hull_maintenance_and_storage",
            "holding_tank_sized_typical_usage_5_7_day_capacity",
            "deck_fitting_through_deck_remote_from_water_tank",
            "discharge_line_above_waterline_prevent_backflow",
            "vent_line_above_cabin_prevent_odor_intrusion",
            "macerator_pump_grind_solids_soft_discharge_lines",
            "marine_sanitation_device_proper_operation_legal_compliance"
        ],
        "quality_criteria": {
            "compliance": "system_meets_marine_sanitation_device_standards",
            "odor_control": "no_unpleasant_odor_deck_cabin_ventilation",
            "reliability": "tank_and_system_functioning_no_backup_or_overflow",
            "maintenance": "components_accessible_service_and_pump_out"
        },
        "inspection_checklist": [
            "holding_tank_secure_no_leaks_or_cracks",
            "isolation_valve_function_secure_operation",
            "through_hull_fitting_above_waterline_proper_height",
            "discharge_hose_intact_no_cracks_or_separation",
            "vent_line_above_cabin_patent_not_blocked",
            "tank_level_gauge_accuracy_functioning",
            "marine_sanitation_device_operation_proper_treatment",
            "no_odor_or_evidence_leakage_structural_cleanliness",
            "electrical_connections_secure_no_corrosion"
        ],
        "common_mistakes": [
            "through_hull_fitting_too_low_water_intrusion_risk",
            "inadequate_tank_size_frequent_pump_out_inconvenience",
            "missing_marine_sanitation_device_legal_non_compliance",
            "discharge_line_below_waterline_backflow_contamination_risk",
            "inadequate_ventilation_odor_cabin_intrusion",
            "blockage_macerator_pump_overflow_backup_damage"
        ]
    },

    "ventilation_system": {
        "name": "Lüftungs-System (Ventilation System)",
        "standards": [
            "ABYC_E10_ventilation_standards_safety",
            "ISO_maritime_safety_regulations"
        ],
        "routing_rules": [
            "cabin_air_intake_high_side_free_from_exhaust_odor",
            "engine_room_exhaust_above_cabin_no_fume_intrusion",
            "head_compartment_dedicated_exhaust_odor_control",
            "galley_exhaust_hood_grease_filter_replaceable",
            "through_deck_penetration_sealed_epoxy_or_stainless_glands",
            "ductwork_sized_adequate_air_exchange_rate_minimum_4_air_changes_hour",
            "dampers_deck_fitting_prevent_rain_seawater_intrusion",
            "fan_motor_marine_grade_sealed_corrosion_resistant"
        ],
        "quality_criteria": {
            "airflow": "adequate_circulation_all_compartments_no_stagnant_air",
            "odor_control": "effective_head_and_galley_odor_control",
            "moisture": "reduced_condensation_mold_prevention",
            "noise": "quiet_operation_minimal_vibration_sound"
        },
        "inspection_checklist": [
            "intake_ductwork_patent_not_blocked_clear_flow",
            "exhaust_damper_function_seals_properly_closed",
            "fan_motor_operation_smooth_quiet_full_speed",
            "ductwork_secure_no_vibration_or_separation",
            "through_deck_penetration_sealed_no_water_intrusion",
            "galley_hood_grease_filter_clean_replaceable",
            "head_ventilation_adequate_rapid_odor_elimination",
            "cabin_circulation_no_stagnant_areas_draft_free",
            "motor_corrosion_protection_intact_no_rust"
        ],
        "common_mistakes": [
            "inadequate_intake_ductwork_poor_circulation",
            "exhaust_damper_failure_water_intrusion_damage",
            "inadequate_head_ventilation_odor_problems",
            "grease_filter_blockage_reduced_galley_exhaust",
            "inadequate_ductwork_sizing_poor_airflow",
            "through_deck_penetration_not_sealed_water_intrusion"
        ]
    }
}


# ==============================================================================
# ASSESSMENT FUNCTION
# Evaluate custom fitting quality based on component properties
# ==============================================================================

def assess_custom_fit(component: str, material: str, location: str, tolerance_mm: float) -> dict:
    """
    Evaluate the quality of a custom fitted component.

    Parameters:
    - component: Name of component being fitted (e.g., "companionway_steps")
    - material: Material specification (e.g., "teak_25mm_solid")
    - location: Installation location (e.g., "deck_to_cabin_interface")
    - tolerance_mm: Measured fit tolerance in millimeters

    Returns:
    - Dictionary with assessment results including score (0-100), findings, and recommendations

    Assessment Criteria:
    - Tolerance fit: ±2mm for structural, ±1.5mm for visible surfaces
    - Material suitability: Marine-grade, corrosion resistance, dimensional stability
    - Installation location: Moisture exposure, accessibility, functional requirements
    - Quality indicators: Seamless joints, no gaps, proper fastening, protective finishes
    """

    # Base assessment score
    assessment_score = 100
    findings = []
    recommendations = []

    # Tolerance evaluation
    if tolerance_mm <= 1.0:
        findings.append("Toleranz ausgezeichnet - Präzisions-Handwerk erkennbar")
        assessment_score += 5
    elif tolerance_mm <= 2.0:
        findings.append("Toleranz gut - Standard Handwerk-Qualität")
        assessment_score += 0
    elif tolerance_mm <= 3.0:
        findings.append("Toleranz akzeptabel - Funktional aber nicht optimal")
        assessment_score -= 10
        recommendations.append("Nacharbeit erwägen für visuelle Komponenten")
    else:
        findings.append("Toleranz unzureichend - Nacharbeiten erforderlich")
        assessment_score -= 25
        recommendations.append("Komponente überarbeiten oder Spalt mit Zierleiste verdecken")

    # Material suitability evaluation
    marine_materials = ["teak", "mahogany", "stainless", "bronze", "aluminum_anodized"]
    if any(mat in material.lower() for mat in marine_materials):
        findings.append("Material marine-geeignet - Korrosionsbeständigkeit gegeben")
        assessment_score += 5
    else:
        findings.append("Material möglicherweise nicht marine-geeignet")
        assessment_score -= 15
        recommendations.append("Material-Eignung überprüfen - Salzwasser-Belastung berücksichtigen")

    # Location-specific moisture considerations
    moisture_prone_locations = ["hull_interface", "below_waterline", "engine_room", "head", "galley"]
    if any(loc in location.lower() for loc in moisture_prone_locations):
        findings.append("Feuchtigkeitsexposition hoch - Schutzmaßnahmen kritisch")
        assessment_score -= 5
        recommendations.append("Epoxy-Siegelung und Entwässerung überprüfen")

    # Visibility impact
    visible_locations = ["companionway", "cabin", "saloon", "deck_surface"]
    if any(vis in location.lower() for vis in visible_locations):
        if tolerance_mm > 1.5:
            findings.append("Sichtbare Komponente mit höherer Toleranz - ästhetische Bedenken")
            assessment_score -= 10
            recommendations.append("Fugen mit Zierleisten oder Spachtelung abdecken")

    # Expansion coefficient assessment for wood materials
    if "wood" in material.lower() or "teak" in material.lower():
        recommendations.append("Holz-Ausdehnungsspalt (0.5-1.5mm) überprüfen - saisonale Bewegung erwarten")

    # Generate quality rating
    if assessment_score >= 90:
        quality_rating = "Hervorragend"
    elif assessment_score >= 80:
        quality_rating = "Gut"
    elif assessment_score >= 70:
        quality_rating = "Befriedigend"
    elif assessment_score >= 60:
        quality_rating = "Ausreichend"
    else:
        quality_rating = "Mangelhaft"

    return {
        "component": component,
        "material": material,
        "location": location,
        "measured_tolerance_mm": tolerance_mm,
        "assessment_score": min(100, max(0, assessment_score)),  # Clamp 0-100
        "quality_rating": quality_rating,
        "findings": findings,
        "recommendations": recommendations,
        "assessment_note": "Bewertung basiert auf Toleranzpassung, Material-Eignung, und Standort-Faktoren"
    }
