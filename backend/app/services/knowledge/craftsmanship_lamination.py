"""
AYDI Composite Lamination & GFK/CFK Processing Knowledge Base
Master Craftsman Technical Reference for Yacht Composite Manufacturing

This module contains exhaustive technical specifications for lamination techniques,
fiber types, resin systems, and quality criteria used in professional yacht yard environments.
All descriptions are in German; all code comments in English.
"""

# ============================================================================
# 1. LAMINATION TECHNIQUES - All methods used in yacht building
# ============================================================================

LAMINATION_TECHNIQUES = {
    "hand_layup_polyester": {
        "name": "Handlaminierung mit Polyesterharz",
        "description": "Traditionelle Schichtweise Verlegung von Glasfasern mit Polyesterharz-Tränkung. Einfache manuelle Verdichtung mit Walzen oder Bürsten.",
        "fiber_volume_pct": {"min": 25, "max": 35, "optimal": 30},
        "void_content_pct": {"target": 4.5, "max_acceptable": 6.0},
        "strength_rating": {"tensile_mpa": 120, "flexural_mpa": 180, "shear_mpa": 8},
        "reproducibility_rating": 2.5,  # 0-5 scale
        "cost_rating": 1.0,  # 0-5 scale (lowest cost)
        "suitable_for": [
            "hull_below_waterline",
            "keel_area",
            "structural_bulkheads",
            "non_critical_secondary_structure"
        ],
        "environmental_requirements": {
            "temperature_c": 15,
            "humidity_pct_max": 75,
            "dust_level_pct_max": 0.2,
            "wind_speed_kts_max": 2
        },
        "equipment_list": [
            "gelcoat_spray_gun",
            "brushes_synthetic",
            "rollers_50mm_diameter",
            "squeegees_polyurethane",
            "catalyst_dispenser",
            "mixing_containers_calibrated",
            "thermometer_mercury_or_digital",
            "hygrometer",
            "ppk_protective_equipment"
        ],
        "layup_sequence_rules": [
            "Gelcoatschicht 0.5-0.8mm zuerst auftragen",
            "Nach 30-45 Min Gelcoat antrocknen lassen (abhängig von Katalysator und Temperatur)",
            "Erste Faserschicht (CSM 450gsm) mit Harzrolle einarbeiten",
            "Mit Laminierbürste oder Walze Blasen entfernen",
            "Jede Faserschicht vollständig durchfeuchten vor nächster Schicht",
            "Orientierung der Schichten: ±45° für Schub, 0° für Längsfestigkeit, 90° für Querkraft",
            "Wartezeit zwischen Schichten: 20-30 Min bei 20°C (abhängig von Exotherm)",
            "Endkontrolle auf Volllaminierung und Blasenfreiheit"
        ],
        "quality_criteria": {
            "excellent": {
                "fiber_volume_pct": {"min": 32, "max": 35},
                "void_content_pct": {"max": 2.0},
                "gelcoat_thickness_mm": {"min": 0.6, "max": 0.8},
                "surface_finish": "High-gloss, no brush marks, no voids",
                "weight_tolerance_pct": 2.0,
                "tensile_strength_mpa": {"min": 130}
            },
            "good": {
                "fiber_volume_pct": {"min": 29, "max": 35},
                "void_content_pct": {"max": 3.5},
                "gelcoat_thickness_mm": {"min": 0.5, "max": 0.9},
                "surface_finish": "Glossy, minor brush marks acceptable",
                "weight_tolerance_pct": 3.0,
                "tensile_strength_mpa": {"min": 120}
            },
            "acceptable": {
                "fiber_volume_pct": {"min": 27, "max": 36},
                "void_content_pct": {"max": 5.0},
                "gelcoat_thickness_mm": {"min": 0.4, "max": 1.0},
                "surface_finish": "Visible brush marks, minor voids in secondary areas",
                "weight_tolerance_pct": 4.0,
                "tensile_strength_mpa": {"min": 110}
            },
            "poor": {
                "fiber_volume_pct": {"min": 0, "max": 26},
                "void_content_pct": {"max": 6.1},
                "gelcoat_thickness_mm": {"min": 0, "max": 1.5},
                "surface_finish": "Rough, uneven, major voids",
                "weight_tolerance_pct": 5.1,
                "tensile_strength_mpa": {"min": 0}
            }
        },
        "common_defects": [
            {
                "defect": "Blasen und Poren in der Matrix",
                "cause": "Unzureichendes Ausrollen, zu schnelles Laminieren bei hoher Temperatur, falsche Katalysatorkonzentration",
                "detection_method": "Visuelle Inspektion, Schallprüfung (Ultraschall), Röntgenfluoreszenz",
                "repair_possible": True,
                "prevention": [
                    "Systematisches Ausrollen mit Laminierbürste nach jeder Schicht",
                    "Exothermische Temperatur überwachen (max 40°C)",
                    "Katalysator korrekt dosieren (0.5-1.0% abhängig von Temperatur)",
                    "Luftfeuchtigkeit unter 75% halten"
                ]
            },
            {
                "defect": "Glasfaserablösungen (Fiber Floating)",
                "cause": "Zu wenig Harz, Faserorientierung falsch, Walzenübertritt falsch",
                "detection_method": "Visuelle Inspektation Lupe 10x, Druckprobe mit Fingernagel",
                "repair_possible": True,
                "prevention": [
                    "Harzgehalt korrekt einstellen (Richtlinie: 70% Harz / 30% Faser für Hand-Layup)",
                    "Jede Schicht vollständig durchfeuchten",
                    "Walzenübertritt mehrfach durchführen",
                    "Faserschicht mit Harzwalze vor dem Ausrollen anfeuchten"
                ]
            },
            {
                "defect": "Gelcoat-Risse und Spannungsrisse",
                "cause": "Zu dicke Gelcoatschicht, unzureichende Schrumpfungsausgleich, Temperaturgradienten",
                "detection_method": "Visuelle Kontrolle, Durchlicht-Inspektion",
                "repair_possible": True,
                "prevention": [
                    "Gelcoat-Schichtdicke 0.5-0.8mm einhalten",
                    "Gelcoat mit Faser-Oberflächenschicht direkt abdecken",
                    "Temperaturgradienten minimieren (konstante 18-25°C)",
                    "Gehärter-Cure-Zeit respektieren, nicht vorab abschleifen"
                ]
            },
            {
                "defect": "Schichthaftungsfehlstellen zwischen Lagen",
                "cause": "Zu lange Wartezeiten zwischen Schichten, Verschmutzung Oberfläche, unzureichende Haft",
                "detection_method": "Ultraschallprüfung, Tap-Test mit Hammer und Stethoskop",
                "repair_possible": True,
                "prevention": [
                    "Wartezeit 20-30 Min optimal (nicht mehr als 2h ohne Oberflächenrauheit)",
                    "Oberfläche vor nächster Schicht absaugen/abbürsten (kein Wasser!)",
                    "Bei langer Wartezeit: Oberfläche mit 40er Schleifer anrauen",
                    "Oberflächenfeuchte kontrollieren (nicht über 75% rel. Feuchte)"
                ]
            }
        ],
        "cure_schedule": {
            "room_temperature_20c": {
                "gelcoat_handling_min": 45,
                "first_fiber_layup_min": 60,
                "full_cure_hours": 16,
                "mold_demold_hours": 24,
                "post_cure_recommended_c": "None (optional room temp cure only)"
            },
            "elevated_temperature_40c": {
                "gelcoat_handling_min": 15,
                "first_fiber_layup_min": 25,
                "full_cure_hours": 4,
                "mold_demold_hours": 8,
                "post_cure_recommended_c": "Optional: 2h at 40°C"
            }
        }
    },

    "hand_layup_vinylester": {
        "name": "Handlaminierung mit Vinylesterharz",
        "description": "Handlaminierung mit fortgeschrittenem Vinylesterharz. Bessere Feuchtigkeitsbeständigkeit und Chemikalienresistenz als Polyester. Höhere Kosten.",
        "fiber_volume_pct": {"min": 28, "max": 38, "optimal": 32},
        "void_content_pct": {"target": 3.5, "max_acceptable": 5.0},
        "strength_rating": {"tensile_mpa": 150, "flexural_mpa": 210, "shear_mpa": 10},
        "reproducibility_rating": 3.0,
        "cost_rating": 2.5,
        "suitable_for": [
            "hull_below_waterline",
            "water_tanks",
            "corrosive_environment_areas",
            "high_durability_sections"
        ],
        "environmental_requirements": {
            "temperature_c": 18,
            "humidity_pct_max": 70,
            "dust_level_pct_max": 0.15,
            "wind_speed_kts_max": 1.5
        },
        "equipment_list": [
            "gelcoat_spray_gun_HVLP",
            "brushes_natural_hair",
            "rollers_50-75mm",
            "squeegees_polyurethane",
            "catalyst_dispenser_2_part",
            "accelerator_dispenser_optional",
            "thermometer_digital",
            "hygrometer",
            "exotherm_monitor",
            "ventilation_system"
        ],
        "layup_sequence_rules": [
            "Gelcoat (Vinylester matched) 0.6-0.9mm auftragen",
            "Gelcoat-Antrocknung 45-60 Min bei 20°C",
            "Erste Faserschicht (biaxiale 450gsm) mit spezieller Harzwalze einarbeiten",
            "Vinylesterharz durchfeuchten - höherer Harzgehalt nötig (35-38% Faser)",
            "Schichtaufbau: CSM 450gsm → Biax 450gsm (±45°) → UD 600gsm (0°) → Biax 450gsm (±45°)",
            "Mit Laminierbürste oder Stahlwalze komprimieren (nicht zu aggressive)",
            "Wartezeit: 15-25 Min bei 20°C (kürzere Gel-Zeit als Polyester)",
            "Exotherme Temperatur überwachen - Vinylester reagiert schneller"
        ],
        "quality_criteria": {
            "excellent": {
                "fiber_volume_pct": {"min": 34, "max": 38},
                "void_content_pct": {"max": 1.5},
                "gelcoat_thickness_mm": {"min": 0.7, "max": 0.9},
                "surface_finish": "Mirror-gloss finish, no orange peel",
                "weight_tolerance_pct": 1.5,
                "water_absorption_24h_pct": {"max": 0.3}
            },
            "good": {
                "fiber_volume_pct": {"min": 31, "max": 38},
                "void_content_pct": {"max": 2.5},
                "gelcoat_thickness_mm": {"min": 0.6, "max": 1.0},
                "surface_finish": "Glossy, minor imperfections acceptable",
                "weight_tolerance_pct": 2.0,
                "water_absorption_24h_pct": {"max": 0.5}
            },
            "acceptable": {
                "fiber_volume_pct": {"min": 29, "max": 39},
                "void_content_pct": {"max": 4.0},
                "gelcoat_thickness_mm": {"min": 0.5, "max": 1.1},
                "surface_finish": "Acceptable gloss, visible brush strokes",
                "weight_tolerance_pct": 3.0,
                "water_absorption_24h_pct": {"max": 0.8}
            }
        },
        "common_defects": [
            {
                "defect": "Schnelle Gelierzeit - unvollständige Laminierung",
                "cause": "Zu viel Katalysator, zu warme Umgebung (>25°C), alte Harzcharge",
                "detection_method": "Visuelle Kontrolle während Laminierung, Viskositätsprobe",
                "repair_possible": False,
                "prevention": [
                    "Katalysator genau nach Datenblatt dosieren (0.5-1.0% max)",
                    "Temperatur 18-22°C halten",
                    "Frisches Harz verwenden (Verfallsdatum prüfen)",
                    "Kleine Chargen arbeiten bei warmer Jahreszeit"
                ]
            },
            {
                "defect": "Schichtrisse durch schnelle Härtung",
                "cause": "Exotherme Spitzentemperatur zu hoch (>60°C), dicke Schicht auf einmal",
                "detection_method": "Oberflächenrisse sichtbar, Thermografie, Ultraschall",
                "repair_possible": True,
                "prevention": [
                    "Dünnere Schichten pro Lage (max 2mm pro Laminiervorgang)",
                    "Exothermische Temperatur mit Thermofühlern überwachen",
                    "Belüftung zur Wärmeverbreitung nutzen",
                    "Wartezeit zwischen dicken Schichten erhöhen"
                ]
            }
        ],
        "cure_schedule": {
            "room_temperature_20c": {
                "gelcoat_handling_min": 60,
                "first_fiber_layup_min": 75,
                "full_cure_hours": 20,
                "mold_demold_hours": 28,
                "post_cure_recommended_c": "Post-cure 2h at 60°C improves properties by 10-15%"
            },
            "elevated_temperature_40c": {
                "gelcoat_handling_min": 20,
                "first_fiber_layup_min": 30,
                "full_cure_hours": 6,
                "mold_demold_hours": 12,
                "post_cure_recommended_c": "2h at 60°C highly recommended"
            }
        }
    },

    "hand_layup_epoxy": {
        "name": "Handlaminierung mit Epoxidharz",
        "description": "Premium Hand-Layup mit Zweikomponenten-Epoxid. Höchste Festigkeit, beste Feuchtigkeitsbeständigkeit, aber schwierig zu verarbeiten und teuer.",
        "fiber_volume_pct": {"min": 32, "max": 42, "optimal": 38},
        "void_content_pct": {"target": 2.0, "max_acceptable": 3.5},
        "strength_rating": {"tensile_mpa": 180, "flexural_mpa": 260, "shear_mpa": 12},
        "reproducibility_rating": 2.0,  # schwierig
        "cost_rating": 4.0,
        "suitable_for": [
            "racing_hull",
            "high_load_structural_areas",
            "custom_composite_parts",
            "repair_high_performance"
        ],
        "environmental_requirements": {
            "temperature_c": 20,
            "humidity_pct_max": 60,
            "dust_level_pct_max": 0.1,
            "wind_speed_kts_max": 0
        },
        "equipment_list": [
            "scales_gram_precision_0_1g",
            "mixing_pot_aluminum",
            "stirrer_wooden_or_glass",
            "brushes_natural_hair",
            "rollers_glass_fiber",
            "squeegees_hard_plastic",
            "thermometer_infrared",
            "timer_countdown",
            "ventilation_hood",
            "personal_protective_equipment_heavy"
        ],
        "layup_sequence_rules": [
            "Epoxid und Härter exakt nach Gewicht mischen (nicht nach Volumen)",
            "Mischung 2-3 Min ruhig in Behälter stehen lassen (Luftblasen absetzen)",
            "Gelcoat auftragen (epoxy-matched, 0.7-1.0mm)",
            "Gelcoat antrocknen 90-120 Min (länger als Polyester/Vinylester)",
            "Erste Schicht: CSM 450gsm oder Biax 0°/90°",
            "Mit spezieller Epoxid-Walze einarbeiten (weniger aggressiv als Polyester)",
            "Jede Schicht: 0°/±45°/90°/±45° Orientierungsmuster",
            "Wartezeit 30-45 Min zwischen Schichten (abhängig von Härter)",
            "Nach letzter Schicht: Oberfläche mit Peel-Ply abdecken oder Wachs auftragen (verhindert Luft-Härtung)",
            "Volle Härtung: 7 Tage bei 20°C oder 8-16h bei 60°C Post-Cure"
        ],
        "quality_criteria": {
            "excellent": {
                "fiber_volume_pct": {"min": 39, "max": 42},
                "void_content_pct": {"max": 1.0},
                "gelcoat_thickness_mm": {"min": 0.8, "max": 1.0},
                "surface_finish": "Flawless gloss, no ripple",
                "weight_tolerance_pct": 1.0,
                "tensile_strength_mpa": {"min": 190},
                "water_absorption_24h_pct": {"max": 0.15}
            },
            "good": {
                "fiber_volume_pct": {"min": 36, "max": 42},
                "void_content_pct": {"max": 1.5},
                "gelcoat_thickness_mm": {"min": 0.7, "max": 1.1},
                "surface_finish": "High gloss, minor marks acceptable",
                "weight_tolerance_pct": 1.5,
                "tensile_strength_mpa": {"min": 175},
                "water_absorption_24h_pct": {"max": 0.25}
            },
            "acceptable": {
                "fiber_volume_pct": {"min": 33, "max": 43},
                "void_content_pct": {"max": 2.5},
                "gelcoat_thickness_mm": {"min": 0.6, "max": 1.2},
                "surface_finish": "Good gloss, visible texture",
                "weight_tolerance_pct": 2.0,
                "tensile_strength_mpa": {"min": 160},
                "water_absorption_24h_pct": {"max": 0.4}
            }
        },
        "common_defects": [
            {
                "defect": "Unvollständige Härtung - klebrig bleiben",
                "cause": "Falsches Mischverhältnis (±5% kritisch), alte Komponenten, zu niedrige Temperatur",
                "detection_method": "Oberflächentest (Fingernagel), Viscosity check, DSC Analyse",
                "repair_possible": False,
                "prevention": [
                    "Komponenten genau nach Gewicht mischen (Digitalwaage ±0.1g)",
                    "Verfallsdatum prüfen - Epoxid altert schneller als Härter",
                    "Nach Mischung rühren und 2min ruhen lassen",
                    "Mindesttemperatur 18°C einhalten (besser 20-25°C)"
                ]
            },
            {
                "defect": "Blasenbildung während Härtung",
                "cause": "Luftblasen beim Mischen eingerührt, nicht genug Komprimierung, falsche Härterdosierung",
                "detection_method": "Röntgenfluoreszenz, Ultraschallprüfung, Tapy-Test",
                "repair_possible": True,
                "prevention": [
                    "Mischung vor Gebrauch 2-3 Min stehen lassen (Blasen setzen ab)",
                    "Mit spezieller Walze oder Bürste sanft komprimieren",
                    "Luftfeuchte unter 60% halten",
                    "Belüftung während Härtung (aber nicht direkt Wind)"
                ]
            },
            {
                "defect": "Gelbfärbung oder Verfärbung nach UV-Exposition",
                "cause": "UV-sensible Härter, schlechte Gelcoat-UV-Stabilität, falsche Lagerung vor Verarbeitung",
                "detection_method": "Visuelle Kontrolle nach 3-6 Monaten UV-Exposition",
                "repair_possible": True,
                "prevention": [
                    "UV-stabile Epoxid-Härter wählen (z.B. cycloaliphatic)",
                    "Gelcoat mit UV-Blocker wählen",
                    "Verarbeitete Teile vor Sonnenlicht geschützt lagern",
                    "Mit UV-Klarlack (2 Schichten) schützen"
                ]
            }
        ],
        "cure_schedule": {
            "room_temperature_20c": {
                "gelcoat_handling_min": 120,
                "first_fiber_layup_min": 150,
                "full_cure_hours": 168,  # 7 days
                "mold_demold_hours": 48,
                "post_cure_recommended_c": "Post-cure 16h at 60°C or 8h at 80°C highly recommended (increases Tg)"
            },
            "elevated_temperature_40c": {
                "gelcoat_handling_min": 45,
                "first_fiber_layup_min": 60,
                "full_cure_hours": 36,
                "mold_demold_hours": 18,
                "post_cure_recommended_c": "8h at 80°C mandatory for full strength development"
            }
        }
    },

    "vacuum_bag": {
        "name": "Vakuumsack-Verdichtung (Vacuum Bagging)",
        "description": "Handlaminierung mit nachgelagerter Vakuumsack-Verdichtung. Senkung der Porengehalte, Erhöhung der Fasernvolumenanteil auf 40-45%.",
        "fiber_volume_pct": {"min": 40, "max": 46, "optimal": 43},
        "void_content_pct": {"target": 1.5, "max_acceptable": 2.5},
        "strength_rating": {"tensile_mpa": 210, "flexural_mpa": 300, "shear_mpa": 14},
        "reproducibility_rating": 3.5,
        "cost_rating": 2.8,
        "suitable_for": [
            "hull_cruiser_production",
            "deck_structures",
            "bulkheads_high_load",
            "keel_area"
        ],
        "environmental_requirements": {
            "temperature_c": 20,
            "humidity_pct_max": 70,
            "dust_level_pct_max": 0.15,
            "wind_speed_kts_max": 1.0,
            "vacuum_pump_availability": "Essential"
        },
        "equipment_list": [
            "vacuum_pump_3_5_5_6_cfm",
            "vacuum_gauge_0_to_1bar",
            "vacuum_hose_nylon_reinforced",
            "peel_ply_fabric",
            "breather_fabric_nonwoven",
            "sealant_tape_butyl",
            "vacuum_port_fittings",
            "release_film_or_tape",
            "roller_hand_or_pneumatic",
            "thermometer_ir",
            "humidity_monitor"
        ],
        "layup_sequence_rules": [
            "Standard Hand-Layup durchführen (Gelcoat + erste Faserlagen)",
            "Nach Gelcoat-Härtung und ersten 2-3 Faserlagen Vakuumsack aufbauen",
            "Vakuumsack-Komponenten: Release Film → Peel Ply → Breather Fabric → Sealant Tape",
            "Sealant Tape an Moldenrand und Vakuumport anbringen",
            "Vakuum schrittweise aufbauen: 0.2 bar → 0.5 bar → 0.8 bar (nicht schlagartig)",
            "Vakuum-Druck: 0.8-0.9 bar halten während restlichen Laminierung (8-12 Stunden)",
            "Nach Laminierung: Vakuum halten bis Harz vollständig gehärtet (24-48 Stunden)",
            "Vakuum-Überwachung: Druckänderung <0.05 bar/Stunde erlaubt (Test auf Lecks)",
            "Sealant Tape und Breather nach Härtung entfernen"
        ],
        "quality_criteria": {
            "excellent": {
                "fiber_volume_pct": {"min": 44, "max": 46},
                "void_content_pct": {"max": 1.0},
                "gelcoat_thickness_mm": {"min": 0.7, "max": 0.9},
                "surface_finish": "High-gloss, flawless",
                "weight_tolerance_pct": 1.0,
                "tensile_strength_mpa": {"min": 225},
                "vacuum_stability_bar_min": 0.85
            },
            "good": {
                "fiber_volume_pct": {"min": 41, "max": 46},
                "void_content_pct": {"max": 1.5},
                "gelcoat_thickness_mm": {"min": 0.6, "max": 1.0},
                "surface_finish": "Gloss, minor imperfections",
                "weight_tolerance_pct": 1.5,
                "tensile_strength_mpa": {"min": 210},
                "vacuum_stability_bar_min": 0.80
            },
            "acceptable": {
                "fiber_volume_pct": {"min": 39, "max": 47},
                "void_content_pct": {"max": 2.5},
                "gelcoat_thickness_mm": {"min": 0.5, "max": 1.1},
                "surface_finish": "Good, visible pores acceptable",
                "weight_tolerance_pct": 2.0,
                "tensile_strength_mpa": {"min": 195},
                "vacuum_stability_bar_min": 0.70
            }
        },
        "common_defects": [
            {
                "defect": "Vakuum-Leck und Druckabfall",
                "cause": "Sealant Tape nicht ordnungsgemäß angebracht, Schlauchbeschädigung, Ventil undicht, Peel-Ply beschädigt",
                "detection_method": "Drucküberwachung (sollte <0.05 bar/Stunde abfallen), Seifenwasser-Test an Nähten",
                "repair_possible": True,
                "prevention": [
                    "Sealant Tape glatt und ohne Falten anbringen (doppelt ankleben)",
                    "Schläuche täglich vor Gebrauch auf Risse prüfen",
                    "Vakuumport korrekt positionieren (nicht unter Harz-Level)",
                    "Peel-Ply vor Verwendung auf Beschädigungen prüfen"
                ]
            },
            {
                "defect": "Ungleichmäßige Harz-Verteilung",
                "cause": "Breather Fabric falsch platziert, zu viel/zu wenig Harz, Vakuum zu früh angewendet",
                "detection_method": "Oberflächenrauheit unterschiedlich, Ultraschall zeigt Dünnstellen",
                "repair_possible": False,
                "prevention": [
                    "Breather Fabric glatt auflegen, keine Falten",
                    "Harzgehalt vor Vakuum optimieren (Hand-Layup gut durchlaminieren)",
                    "Vakuum schrittweise (nicht schlagartig) aufbauen",
                    "Thermografie zur Kontrolle der Harz-Verteilung einsetzen"
                ]
            }
        ],
        "cure_schedule": {
            "room_temperature_20c": {
                "initial_hand_layup_hours": 2,
                "vacuum_application_min": 120,
                "vacuum_maintenance_hours": 12,
                "full_cure_with_vacuum_hours": 24,
                "vacuum_release_hours": 24,
                "demold_hours": 48,
                "post_cure_optional_c": "2-4h at 50°C optional"
            }
        }
    },

    "vacuum_infusion_rtm_light": {
        "name": "Vakuum-Infusion (RTM-Light)",
        "description": "Trockene Faser wird mit Vakuum durchgetränkt. Minimal Porengehalt, hoher Faseranteil (45-50%), aber komplexe Prozesssteuerung.",
        "fiber_volume_pct": {"min": 45, "max": 52, "optimal": 48},
        "void_content_pct": {"target": 1.0, "max_acceptable": 2.0},
        "strength_rating": {"tensile_mpa": 250, "flexural_mpa": 360, "shear_mpa": 16},
        "reproducibility_rating": 3.0,
        "cost_rating": 3.2,
        "suitable_for": [
            "racing_yacht_hull",
            "performance_structural",
            "high_load_compression_areas",
            "premium_production"
        ],
        "environmental_requirements": {
            "temperature_c": 22,
            "humidity_pct_max": 60,
            "dust_level_pct_max": 0.1,
            "wind_speed_kts_max": 0,
            "vacuum_system_robustness": "Industrial-grade required"
        },
        "equipment_list": [
            "vacuum_pump_5_cfm_minimum",
            "vacuum_gauge_high_precision_0_01bar",
            "heater_space_or_infrared",
            "infusion_resin_degassed",
            "infusion_lines_spiral_plastic",
            "distribution_media_mesh",
            "release_film",
            "peel_ply",
            "bleeder_fabric",
            "sealant_tape_premium",
            "vacuum_ports_multiple",
            "thermocouples_rtd",
            "data_logger_temperature",
            "infusion_pot_vacuum_equipped"
        ],
        "layup_sequence_rules": [
            "Alle Faserlagen trocken in Form einlegen (kein Harz vorab)",
            "Faser-Schichtfolge optimieren für Infusionsfluss: 0° UD zuerst (guter Flow) → ±45° Biax (Schub) → 90° oder CSM (abschließend)",
            "Distribution Media (Mesh) auf oberste Faser legen - führt Harz über ganze Breite",
            "Peel-Ply auf Distribution Media auflegen",
            "Breather Fabric auf ganzer Fläche auflegen (Harz-Transpiration)",
            "Vakuum-Schema: 2-4 Infusions-Resin-Einleitungspunkte, 1-2 Vakuum-Abluftpunkte",
            "Vakuum aufbauen auf 0.8-0.9 bar, halten >30 min (Faser Entlüftung, Feuchtigkeitsentfernung)",
            "Infusions-Pot mit Harz füllen (Harz auch vakuumbehandelt sein sollte >30 min)",
            "Harz-Injektion starten - Vakuum nicht unterbrechen während Infusion (30-90 min je nach Größe)",
            "Infusions-Ende: Frontline der Harz-Permeation beobachten, nicht über Abluftpunkt hinaus laufen lassen",
            "Nach Infusion: Infusions-Linien versperren, Vakuum weitere 2-4h halten (Nachverdichtung, Volatile-Abbau)",
            "Härtung unter Vakuum bis zur Gelzeit, dann Sack entfernen"
        ],
        "quality_criteria": {
            "excellent": {
                "fiber_volume_pct": {"min": 50, "max": 52},
                "void_content_pct": {"max": 0.5},
                "surface_finish": "Mirror-gloss, no ripple",
                "weight_tolerance_pct": 0.8,
                "tensile_strength_mpa": {"min": 270},
                "fiber_waviness_mm": {"max": 1.0},
                "resin_bank_mm": {"max": 2.0}
            },
            "good": {
                "fiber_volume_pct": {"min": 47, "max": 52},
                "void_content_pct": {"max": 1.0},
                "surface_finish": "High gloss, minor imperfections",
                "weight_tolerance_pct": 1.0,
                "tensile_strength_mpa": {"min": 255},
                "fiber_waviness_mm": {"max": 2.0},
                "resin_bank_mm": {"max": 3.0}
            },
            "acceptable": {
                "fiber_volume_pct": {"min": 45, "max": 53},
                "void_content_pct": {"max": 2.0},
                "surface_finish": "Good gloss, visible imperfections",
                "weight_tolerance_pct": 1.5,
                "tensile_strength_mpa": {"min": 240},
                "fiber_waviness_mm": {"max": 3.0},
                "resin_bank_mm": {"max": 5.0}
            }
        },
        "common_defects": [
            {
                "defect": "Trockenstellen - unvollständige Infusion",
                "cause": "Falsche Infusions-Port-Platzierung, zu hohe Viskosität (Temperatur zu niedrig), Fasern zu dicht",
                "detection_method": "Oberflächenoptik, Ultraschallprüfung C-Scan, Thermografie während Infusion",
                "repair_possible": False,
                "prevention": [
                    "Infusions-Pad-Ort berechnen (1/4 bis 1/3 von Kante, optimal zentral)",
                    "Harz-Viskosität optimieren (30-50 cps optimal) - Temperatur kontrollieren",
                    "Distribution Media Ausdehnung nutzen - Harz-Fluss über ganze Breite",
                    "Vakuum-Port am höchsten Punkt (Luft-Entfernung)",
                    "Probe-Infusion mit Tracer durchführen"
                ]
            },
            {
                "defect": "Mehrschichtigkeit - Harz läuft zu schnell",
                "cause": "Verteilungs-Media falsch orientiert, Vakuum zu hoch, Fiber-Volumengehalt zu niedrig",
                "detection_method": "Beobachtung während Infusion, Oberflächenfinish, Röntgen",
                "repair_possible": False,
                "prevention": [
                    "Distribution Media mit niedriger Permeabilität wählen",
                    "Vakuum graduell aufbauen (nicht schlagartig auf 0.9 bar)",
                    "Faserdichte überprüfen - zu lockere Struktur vermeiden",
                    "Harz-Injektion an mehreren Punkten (nicht nur einen)"
                ]
            },
            {
                "defect": "Resin-Bank (Harz-Ansammlung)",
                "cause": "Zu viel Harz in Pot, Abluftschacht falsch positioniert, Infusion-Ende nicht kontrolliert",
                "detection_method": "Sichtbar nach Sack-Entfernung, Gewicht zu schwer",
                "repair_possible": True,
                "prevention": [
                    "Harz-Volumen genau berechnen (Faserabsorption + 10% Reserve)",
                    "Abluftschacht an Infusions-Laufkante positionieren",
                    "Infusions-Front beobachten, Zufuhr stoppen wenn Front Abluft erreicht",
                    "Mehrfache kleine Abluftpunkte statt ein großer Punkt"
                ]
            }
        ],
        "cure_schedule": {
            "room_temperature_22c": {
                "fiber_degassing_min": 30,
                "harz_degassing_min": 45,
                "infusion_time_min": "30-90 (size dependent)",
                "post_infusion_vacuum_hours": 4,
                "gelation_time_hours": 8,
                "full_cure_hours": 48,
                "demold_hours": 72,
                "post_cure_recommended_c": "Optional: 4h at 60°C"
            }
        }
    },

    "resin_transfer_molding": {
        "name": "Resin Transfer Molding (RTM)",
        "description": "Zwei-Schalen-Formwerkzeug mit Druckinfusion. Beidseitig glatte Oberfläche, hohe Qualität und Reproduzierbarkeit.",
        "fiber_volume_pct": {"min": 46, "max": 54, "optimal": 50},
        "void_content_pct": {"target": 0.8, "max_acceptable": 1.5},
        "strength_rating": {"tensile_mpa": 280, "flexural_mpa": 400, "shear_mpa": 18},
        "reproducibility_rating": 4.5,
        "cost_rating": 3.8,
        "suitable_for": [
            "production_series_hull",
            "production_deck",
            "high_precision_structural",
            "performance_racing"
        ],
        "environmental_requirements": {
            "temperature_c": 22,
            "humidity_pct_max": 55,
            "dust_level_pct_max": 0.05,
            "wind_speed_kts_max": 0
        },
        "equipment_list": [
            "rtm_tool_split_mold",
            "pressure_injection_pump_2_8_bar",
            "pressure_gauge_0_10bar",
            "harz_pot_heater_equipped",
            "resin_manifold_multi_port",
            "clamp_system_pneumatic_or_hydraulic",
            "thermocouples_multiple",
            "data_acquisition_system",
            "vacuum_assist_pump"
        ],
        "layup_sequence_rules": [
            "Beide Form-Schalen vorbereiten: Release-Agent auftragen, Fasern korrekt platzieren",
            "Faser-Orientierung: 0° UD (Längsfestigkeit) → ±45° Biax (Schub) → 0° UD → ±45° Biax (abschließend)",
            "Für kritische Zonen: Mehrlagiges Design mit lokaler Faserverstärkung",
            "Beide Schalen zusammenspannen: Druckverteilung über Randclips/Klammern",
            "Harz auf Prozess-Temperatur (50-60°C) und Zielzähigkeit (30-50 cps) einstellen",
            "Druck-Infusion starten: 2-4 bar (abhängig von Faserdichte und Harz-Viskosität)",
            "Druck-Verteilung: Mehrere Einleitungs-Punkte, 2-4 Abluftpunkte an höchsten Stellen",
            "Während Infusion: Druck konstant halten ±0.2 bar, Temperatur ±2°C, Abluftbeobachtung",
            "Infusions-Ende erkannt: Harz-Front erreicht alle Abluftpunkte, Widerstand-Anstieg messbar",
            "Nach Gelation: Druck weitere 30 min halten (Nachverdichtung, Porenabbau)",
            "Sealant versetzen (wenn nötig), Harze aushärten - ohne Druckfreigabe",
            "Nach Härtung: Werkzeug öffnen, Gussteil demoldieren"
        ],
        "quality_criteria": {
            "excellent": {
                "fiber_volume_pct": {"min": 51, "max": 54},
                "void_content_pct": {"max": 0.5},
                "surface_finish_both_sides": "Flawless gloss on both surfaces",
                "weight_tolerance_pct": 0.5,
                "tensile_strength_mpa": {"min": 295},
                "dimensional_tolerance_mm": {"max": 0.3},
                "pressure_during_cure_bar": {"min": 1.5, "max": 4.0}
            },
            "good": {
                "fiber_volume_pct": {"min": 48, "max": 54},
                "void_content_pct": {"max": 1.0},
                "surface_finish_both_sides": "High gloss, minor imperfections acceptable",
                "weight_tolerance_pct": 0.8,
                "tensile_strength_mpa": {"min": 280},
                "dimensional_tolerance_mm": {"max": 0.5},
                "pressure_during_cure_bar": {"min": 1.5, "max": 4.0}
            },
            "acceptable": {
                "fiber_volume_pct": {"min": 46, "max": 55},
                "void_content_pct": {"max": 1.5},
                "surface_finish_both_sides": "Good gloss, visible marks acceptable",
                "weight_tolerance_pct": 1.0,
                "tensile_strength_mpa": {"min": 265},
                "dimensional_tolerance_mm": {"max": 0.8},
                "pressure_during_cure_bar": {"min": 1.0, "max": 4.5}
            }
        },
        "common_defects": [
            {
                "defect": "Harz-Front-Verzögerung - verzögerte Infusion",
                "cause": "Faser-Dichte zu hoch, Druck zu niedrig, Harz-Viskosität zu hoch, Durchlüftungs-Blockade",
                "detection_method": "Infusions-Dauer länger als erwartet, Druckzuwachs gemessen",
                "repair_possible": False,
                "prevention": [
                    "Druck erhöhen (2-4 bar berechtigt, abhängig von Faserdichte)",
                    "Harz-Temperatur auf 55-60°C erhöhen (Viskosität senkend)",
                    "Faser-Dichte im Design überprüfen",
                    "Abluftpunkte optimieren (mehrere kleine statt ein großer)"
                ]
            },
            {
                "defect": "Druck-Undichtheiten - Harz-Auslauf",
                "cause": "Schalen nicht optimal gespannt, Versiegelung unzureichend, Formwerkzeug-Verschleiß",
                "detection_method": "Sichtbarer Harz-Austritt, Gewichtsverlust, Druck-Abfall",
                "repair_possible": False,
                "prevention": [
                    "Schalen-Spannkraft überprüfen (Herstellerangaben + 10% Reserve)",
                    "Versiegelung (Ton/Latex) täglich überprüfen und erneuern",
                    "Formwerkzeug-Wartung: Oberfläche polieren, Verschleiß ausgleichen",
                    "Druck-Probe ohne Fasern durchführen (Funktionsprüfung)"
                ]
            }
        ],
        "cure_schedule": {
            "room_temperature_22c": {
                "clamp_setup_min": 15,
                "pressure_infusion_min": "10-30",
                "pressure_maintenance_post_gelation_min": 30,
                "demold_hours": 24,
                "full_cure_hours": 72,
                "post_cure_recommended_c": "4-8h at 80°C for optimal Tg"
            },
            "hot_mold_60c": {
                "clamp_setup_min": 10,
                "pressure_infusion_min": "5-15",
                "pressure_maintenance_post_gelation_min": 20,
                "demold_hours": 8,
                "full_cure_hours": 16,
                "post_cure_recommended_c": "Not needed - Tg already achieved"
            }
        }
    },

    "prepreg_oven": {
        "name": "Prepreg-Oven-Verarbeitung",
        "description": "Vorgefertigte Prepreg-Schichten (Faser + teilweise ausgehärtetes Harz) in Heißluft-Ofen verarbeitet. Höchste Qualität, höchste Kosten.",
        "fiber_volume_pct": {"min": 55, "max": 62, "optimal": 58},
        "void_content_pct": {"target": 0.5, "max_acceptable": 1.0},
        "strength_rating": {"tensile_mpa": 320, "flexural_mpa": 480, "shear_mpa": 21},
        "reproducibility_rating": 4.8,
        "cost_rating": 4.5,
        "suitable_for": [
            "racing_yacht_ultimate",
            "structural_aerospace_standard",
            "ultra_light_performance",
            "military_spec"
        ],
        "environmental_requirements": {
            "temperature_c": 20,
            "humidity_pct_max": 50,
            "dust_level_pct_max": 0.02,
            "wind_speed_kts_max": 0,
            "prepreg_storage_temp_c": "15-25",
            "prepreg_storage_humidity_pct_max": 45
        },
        "equipment_list": [
            "prepreg_rolls_storage_freezer_minus_18",
            "vacuum_oven_0_1_to_1_bar",
            "tool_heating_system_cartridge_or_oil",
            "temperature_controller_pid",
            "vacuum_pump_industrial",
            "vacuum_gauge_high_precision",
            "bleeder_fabric",
            "peel_ply",
            "release_film",
            "caul_sheet_metal_or_ptfe"
        ],
        "layup_sequence_rules": [
            "Prepreg-Rollen aus Gefrierschrank (-18°C) 1h vor Verarbeitung auf Raumtemperatur bringen (Kondenswasser-Vermeidung)",
            "Jedes Prepreg-Blatt aus Backpapier vorsichtig schälen (vor Verarbeitung, nicht frühzeitig)",
            "Erste Schicht auf trockener, heißer Form (nicht unter 50°C) auflegen",
            "Jede Schicht mit Walze fest ankleiben (Luft-Austritt, Schichthaftung)",
            "Schichtfolge optimieren: UD 0° → Woven Biax ±45° → UD 0° → Woven ±45° → UD 0° (Ende)",
            "Jede 4-5 Schichten: Peel-Ply-Schicht einfügen (Oberfläche für Sekundärwerk-Bonding)",
            "Nach vollständiger Schichtung: Peel-Ply auf Oberseite, Release-Film, Bleeder-Fabric",
            "Vakuum-Sack aufbauen (analog Vacuum-Bag-Prozess)",
            "Werkzeug zusammenfügen mit Pressdruck (wenn geformt)",
            "Vakuum aufbauen auf 0.8-0.9 bar - halten während ganzer Härtung",
            "Temperatur-Profil einfahren (siehe Cure Schedule) - ramp rate nicht >2-3°C/min"
        ],
        "quality_criteria": {
            "excellent": {
                "fiber_volume_pct": {"min": 59, "max": 62},
                "void_content_pct": {"max": 0.3},
                "surface_finish": "Mirror-gloss, aerospace grade",
                "weight_tolerance_pct": 0.3,
                "tensile_strength_mpa": {"min": 340},
                "ply_continuity": "100% (no wrinkles or gaps)",
                "dimensional_tolerance_mm": {"max": 0.2}
            },
            "good": {
                "fiber_volume_pct": {"min": 56, "max": 62},
                "void_content_pct": {"max": 0.7},
                "surface_finish": "High-gloss, excellent",
                "weight_tolerance_pct": 0.5,
                "tensile_strength_mpa": {"min": 325},
                "ply_continuity": ">98% (minor wrinkles acceptable)",
                "dimensional_tolerance_mm": {"max": 0.3}
            },
            "acceptable": {
                "fiber_volume_pct": {"min": 55, "max": 63},
                "void_content_pct": {"max": 1.0},
                "surface_finish": "Good gloss, minor imperfections",
                "weight_tolerance_pct": 0.8,
                "tensile_strength_mpa": {"min": 310},
                "ply_continuity": ">95% (wrinkles <2mm depth)",
                "dimensional_tolerance_mm": {"max": 0.5}
            }
        },
        "common_defects": [
            {
                "defect": "Prepreg-Trockenheit - Harzgehalt zu niedrig",
                "cause": "Gefrierschrank-Lagerung zu alt, Prepreg-Verfallsdatum überschritten, unsachgemäße Handhabung (Wärmeeintrag)",
                "detection_method": "Prepreg fühlt sich spröde an, Faltenbildung während Layup, Poren in Endteil",
                "repair_possible": False,
                "prevention": [
                    "Gefrierschrank-Lagerdatum streng kontrollieren (max 12 Monate, abhängig von Harz-Typ)",
                    "Verfallsdatum Prepreg überprüfen (meist 12-18 Monate ab Fabrikation)",
                    "Lagerbedinungen: -18°C ±3°C, 50% Luftfeuchte max",
                    "Benutztes Prepreg sofort in Gefrierschrank zurück (nicht länger als 30 min Raumtemp)"
                ]
            },
            {
                "defect": "Faltenbildung und Faser-Welligkeit",
                "cause": "Prepreg zu kalt beim Layup, falsche Temperatur-Ramprate (zu schnell), Prepreg zu steif",
                "detection_method": "Sichtbare Falten auf Oberfläche, Ultraschall zeigt Unregelmäßigkeiten, Dehnung sichtbar",
                "repair_possible": False,
                "prevention": [
                    "Werkzeug-Temperatur vor Layup auf 50-60°C vorheizen",
                    "Prepreg auf Raumtemperatur bringen (20-25°C) vor Verarbeitung",
                    "Temperatur-Ramprate: max 2°C/min (besonders bei dicken Teilen)",
                    "Druck während Härtung auf Form halten (Falten-Reduktion)"
                ]
            }
        ],
        "cure_schedule": {
            "standard_epoxy_prepreg": {
                "room_temperature_conditioning_min": 60,
                "vacuum_application": "Before heating",
                "temperature_ramp_c_per_min": 2,
                "dwell_at_80c_min": 30,
                "ramp_to_120c_c_per_min": 2,
                "dwell_at_120c_min": 120,
                "cool_down_ramp_c_per_min": 2,
                "total_cycle_hours": 6,
                "vacuum_release_after_gelation_min": 90
            },
            "fast_epoxy_prepreg": {
                "room_temperature_conditioning_min": 30,
                "vacuum_application": "Before heating",
                "temperature_ramp_c_per_min": 3,
                "dwell_at_130c_min": 60,
                "cool_down_ramp_c_per_min": 2,
                "total_cycle_hours": 2.5,
                "vacuum_release_after_gelation_min": 60
            }
        }
    },

    "prepreg_autoclave": {
        "name": "Prepreg-Autoklav-Verarbeitung",
        "description": "Prepreg-Verarbeitung in Druckautoklav unter Vakuum + Über-Druck. Optimale Fiber-Volumen (60%+), minimale Poren, Militär/Luft- und Raumfahrt-Standard.",
        "fiber_volume_pct": {"min": 58, "max": 65, "optimal": 62},
        "void_content_pct": {"target": 0.3, "max_acceptable": 0.5},
        "strength_rating": {"tensile_mpa": 360, "flexural_mpa": 530, "shear_mpa": 23},
        "reproducibility_rating": 5.0,
        "cost_rating": 5.0,
        "suitable_for": [
            "ultra_performance_racing",
            "military_applications",
            "aerospace_derivative",
            "state_of_art_custom"
        ],
        "environmental_requirements": {
            "temperature_c": 21,
            "humidity_pct_max": 50,
            "dust_level_pct_max": 0.01,
            "wind_speed_kts_max": 0,
            "autoclave_availability": "Required"
        },
        "equipment_list": [
            "prepreg_rolls_freezer_minus_18",
            "vacuum_oven_preparation",
            "autoclave_chamber_3_7_bar",
            "thermal_profiler_10_channel",
            "bleeder_fabric",
            "peel_ply",
            "release_film_ptfe",
            "caul_sheet_aluminum",
            "breather_fabric_nonwoven"
        ],
        "layup_sequence_rules": [
            "Prepreg-Vorbereitung identisch zu Oven-Prozess",
            "Schichtaufbau: UD 0° → Biax ±45° → UD 90° → Biax ±45° → UD 0° (optimiert für Autoklav)",
            "Multi-Directional (MD) oder Quasi-Isotropic (QI) Aufbauten bevorzugt",
            "Peel-Ply alle 5-8 Lagen",
            "Tool-Vorbereitung: Aluminiumkaul-Blech auf Tool (Druckverteilung), Release-Agent großzügig",
            "Komplettes Vakuum-Sack-System aufbauen (identisch zu Prepreg-Oven)",
            "Vakuum vor Autoklav-Druck aufbauen (0.8 bar minimum)",
            "Teil in Autoklav-Kammer einfahren",
            "Autoklav-Programm starten: Vakuum halten + Druck aufbauen nach Temperatur-Profil",
            "Druck-Profil: Ramp mit 2-3 bar/min zu 3.5-7 bar (abhängig von Prepreg-Typ), halten bis Härtung abgeschlossen"
        ],
        "quality_criteria": {
            "excellent": {
                "fiber_volume_pct": {"min": 62, "max": 65},
                "void_content_pct": {"max": 0.2},
                "surface_finish": "Military-spec gloss, flawless",
                "weight_tolerance_pct": 0.2,
                "tensile_strength_mpa": {"min": 375},
                "matrix_cracking": "0% detectable",
                "ply_waviness": "0%",
                "dimensional_tolerance_mm": {"max": 0.1}
            },
            "good": {
                "fiber_volume_pct": {"min": 60, "max": 65},
                "void_content_pct": {"max": 0.4},
                "surface_finish": "Excellent gloss, aerospace grade",
                "weight_tolerance_pct": 0.3,
                "tensile_strength_mpa": {"min": 360},
                "matrix_cracking": "<0.1% area",
                "ply_waviness": "<0.5%",
                "dimensional_tolerance_mm": {"max": 0.2}
            },
            "acceptable": {
                "fiber_volume_pct": {"min": 58, "max": 66},
                "void_content_pct": {"max": 0.5},
                "surface_finish": "Good gloss, minor imperfections acceptable",
                "weight_tolerance_pct": 0.5,
                "tensile_strength_mpa": {"min": 345},
                "matrix_cracking": "<1% area",
                "ply_waviness": "<2%",
                "dimensional_tolerance_mm": {"max": 0.3}
            }
        },
        "common_defects": [
            {
                "defect": "Matrix-Risse durch Über-Druck",
                "cause": "Druck zu schnell aufgebracht (>3 bar/min), Temperatur-Synchronisation unzureichend, Matrix zu spröde",
                "detection_method": "Akustische Emissionsprüfung während Prozess, Oberflächenrisse, Ultraschall post-cure",
                "repair_possible": False,
                "prevention": [
                    "Druck-Ramprate langsam: 1-2 bar/min",
                    "Temperatur-Profil streng einhalten (Heiße-Phase vor Druck-Anstieg)",
                    "Prepreg-Typ mit höherer Bruchzähigkeit wählen",
                    "Vakuum während ganzer Härtung + Abkühlung halten"
                ]
            }
        ],
        "cure_schedule": {
            "standard_aerospace_epoxy": {
                "vacuum_prebag_min": 30,
                "autoclave_chamber_entry_min": 10,
                "temperature_ramp_c_per_min": 2,
                "dwell_at_120c_min": 120,
                "pressure_ramp_bar_per_min": 1,
                "dwell_at_pressure_5bar_min": 120,
                "cool_under_pressure_c_per_min": 2,
                "pressure_release_at_temp_c": 60,
                "total_cycle_hours": 8,
                "post_cure_not_needed": True
            }
        }
    },

    "filament_winding": {
        "name": "Filament Winding",
        "description": "Faserrollen auf rotierendes Formkern aufgewickelt. Höchste Faserorientierungs-Genauigkeit, optimal für zylindrische Strukturen (Rumpf, Rohre).",
        "fiber_volume_pct": {"min": 50, "max": 60, "optimal": 55},
        "void_content_pct": {"target": 1.0, "max_acceptable": 2.0},
        "strength_rating": {"tensile_mpa": 270, "flexural_mpa": 350, "shear_mpa": 15},
        "reproducibility_rating": 4.2,
        "cost_rating": 3.5,
        "suitable_for": [
            "hull_cylinder_section",
            "mast_tube",
            "boom_tube",
            "pressure_vessel",
            "ballast_tank"
        ],
        "environmental_requirements": {
            "temperature_c": 22,
            "humidity_pct_max": 65,
            "dust_level_pct_max": 0.2,
            "wind_speed_kts_max": 1.0
        },
        "equipment_list": [
            "filament_winding_machine",
            "rotating_mandrel",
            "harz_pot_with_immersion_bath",
            "tension_controller",
            "degree_counter",
            "thermometer",
            "release_agent_mandrel"
        ],
        "layup_sequence_rules": [
            "Mandrel (Formkern) mit Release-Agent (Wachs oder spezial Coating) vorbereiten",
            "Fadenzahl (Roving) nach Festigkeits-Anforderung wählen (größere Rohre: 12-50 Roving)",
            "Spulen-Anordnung: Hauptspulen für Längsfasern (0°), Wickelspulen für Wickelwinkel (±45°-80°)",
            "Wickelwinkel berechnen nach Anforderung: 45° für Schub/Torsion, 80-90° für axiale Last",
            "Harz-Tränkung: Fasern durch Harz-Bad führen (Harz-Gehalt 50-60%)",
            "Wickel-Sequenz: Erste Schicht radial (0°/axial) → dann Wickelwinkel-Schichten",
            "Rotations-Geschwindigkeit: 20-50 RPM (langsamer = bessere Harz-Tränkung, schneller = höhere Produktion)",
            "Nach letzter Schicht: Mandrel weiter drehen zum Trocknen (10-20 Umdrehungen)",
            "Harz-Aushärtung im Wickel (RT oder erhitzt Ofen/Autoklav)"
        ],
        "quality_criteria": {
            "excellent": {
                "fiber_volume_pct": {"min": 56, "max": 60},
                "void_content_pct": {"max": 1.0},
                "fiber_alignment_deg": {"max": 1.0},
                "fiber_waviness": "None detectable",
                "wall_thickness_tolerance_mm": {"max": 0.2},
                "hoop_strength_mpa": {"min": 300},
                "axial_strength_mpa": {"min": 200}
            },
            "good": {
                "fiber_volume_pct": {"min": 52, "max": 60},
                "void_content_pct": {"max": 1.5},
                "fiber_alignment_deg": {"max": 2.0},
                "fiber_waviness": "<1mm",
                "wall_thickness_tolerance_mm": {"max": 0.3},
                "hoop_strength_mpa": {"min": 280},
                "axial_strength_mpa": {"min": 180}
            },
            "acceptable": {
                "fiber_volume_pct": {"min": 50, "max": 61},
                "void_content_pct": {"max": 2.0},
                "fiber_alignment_deg": {"max": 3.0},
                "fiber_waviness": "<2mm",
                "wall_thickness_tolerance_mm": {"max": 0.5},
                "hoop_strength_mpa": {"min": 260},
                "axial_strength_mpa": {"min": 160}
            }
        },
        "common_defects": [
            {
                "defect": "Luftblasen und Poren",
                "cause": "Langsame Harz-Tränkung, Rotations-Geschwindigkeit zu schnell, trockene Fasern",
                "detection_method": "Röntgenfluoreszenz, Ultraschall, Oberflächenrauheit",
                "repair_possible": False,
                "prevention": [
                    "Rotations-Geschwindigkeit optimieren (20-35 RPM)",
                    "Harz-Bad Tiefe ausreichend (Fasern vollständig eintauchen)",
                    "Harz-Viskosität optimieren (30-50 cps)",
                    "Spulen-Spannung richtig einstellen (Fasern nicht zu locker)"
                ]
            },
            {
                "defect": "Faser-Verzögerung (Wrinkles)",
                "cause": "Zu hohe Spulen-Spannung, unzureichend Harz, Wickelwinkel falsch",
                "detection_method": "Sichtbare Falten, Muster ungleichmäßig, Ultraschall",
                "repair_possible": False,
                "prevention": [
                    "Spulen-Spannung reduzieren (zu Beginn niedrig, später erhöhen)",
                    "Harz-Gehalt überprüfen (mindestens 50%)",
                    "Wickelwinkel nach Entwurf überprüfen (zu steile Winkel anfälliger)"
                ]
            }
        ],
        "cure_schedule": {
            "room_temperature_22c": {
                "initial_harz_tack_hours": 1,
                "mandrel_still_time_hours": 4,
                "full_cure_hours": 24,
                "demold_hours": 48,
                "post_cure_optional_c": "Optional: 2-4h at 60°C"
            },
            "oven_cure_50c": {
                "initial_harz_tack_hours": 0.5,
                "mandrel_still_time_hours": 2,
                "full_cure_hours": 4,
                "demold_hours": 8,
                "post_cure_optional_c": "Optional: 2h at 70°C"
            }
        }
    },

    "spray_layup": {
        "name": "Spray-up Laminierung (Resin Transfer Spraying)",
        "description": "Gehackte Faser und Harz werden mit Spritzpistole aufgesprüht. Schnell und einfach, aber niedrigste Qualität aller Methoden.",
        "fiber_volume_pct": {"min": 15, "max": 25, "optimal": 20},
        "void_content_pct": {"target": 7.0, "max_acceptable": 9.0},
        "strength_rating": {"tensile_mpa": 80, "flexural_mpa": 120, "shear_mpa": 5},
        "reproducibility_rating": 1.5,
        "cost_rating": 1.5,
        "suitable_for": [
            "non_structural_parts",
            "secondary_cabin_parts",
            "cosmetic_covers",
            "lightweight_non_critical"
        ],
        "environmental_requirements": {
            "temperature_c": 18,
            "humidity_pct_max": 80,
            "dust_level_pct_max": 0.3,
            "wind_speed_kts_max": 3.0,
            "spray_ventilation": "Essential (fume extraction required)"
        },
        "equipment_list": [
            "spray_gun_chopper_resin",
            "air_compressor_8_bar",
            "harz_pot_resin_feed",
            "catalyst_dispenser",
            "abrasive_blower",
            "respiratory_protection_cartridge",
            "ventilation_hood",
            "roller_hand_for_consolidation"
        ],
        "layup_sequence_rules": [
            "Gelcoat auftragen (0.8-1.5mm dicke - höher als Hand-Layup wegen niedriger Qualität)",
            "Nach Gelcoat-Antrocknung (45-60 min): Erste Spritzschicht",
            "Spray-Pistole mit gehackter Faser (25mm Länge) und Harz kombiniert auftragen",
            "Spritz-Dicke pro Schicht: 3-5mm (schneller als Hand-Layup)",
            "Nach jeder Schicht: Mit Hand-Walze verdichten und komprimieren (Blasen-Reduktion)",
            "Schichten schnell hintereinander auftragen (Haft-Zeiten kurz: 10-15 min)",
            "Gesamt-Schichtdicke: 8-12mm (bei Bedarf mehrere Schichten)",
            "Nach letzter Schicht: Oberfläche überschleifen oder mit Finish-Gel versiegeln"
        ],
        "quality_criteria": {
            "excellent": {
                "fiber_volume_pct": {"min": 22, "max": 25},
                "void_content_pct": {"max": 6.0},
                "gelcoat_thickness_mm": {"min": 1.0, "max": 1.5},
                "surface_finish": "Reasonably smooth, acceptable gloss",
                "weight_tolerance_pct": 5.0,
                "tensile_strength_mpa": {"min": 90}
            },
            "good": {
                "fiber_volume_pct": {"min": 19, "max": 25},
                "void_content_pct": {"max": 7.5},
                "gelcoat_thickness_mm": {"min": 0.9, "max": 1.6},
                "surface_finish": "Rough texture visible, gloss acceptable",
                "weight_tolerance_pct": 6.0,
                "tensile_strength_mpa": {"min": 80}
            },
            "acceptable": {
                "fiber_volume_pct": {"min": 16, "max": 26},
                "void_content_pct": {"max": 9.0},
                "gelcoat_thickness_mm": {"min": 0.8, "max": 1.8},
                "surface_finish": "Rough, acceptable for non-critical",
                "weight_tolerance_pct": 8.0,
                "tensile_strength_mpa": {"min": 70}
            }
        },
        "common_defects": [
            {
                "defect": "Unvollständige Faser-Tränkung",
                "cause": "Zu schnell spritzen (Faser zu trocken), unzureichende Walzen-Verdichtung, schlechte Harz-Zufuhr",
                "detection_method": "Oberflächenrauhheit, Ultraschall zeigt Hohlräume, Bruch-Test zeigt trockene Faser",
                "repair_possible": True,
                "prevention": [
                    "Spritz-Geschwindigkeit moderat (nicht zu schnell)",
                    "Nach jeder Schicht gründlich walzen (mindestens 3 Walzen-Durchgänge)",
                    "Harz-Zufuhr überprüfen (kontinuierlich)",
                    "Faser-Länge anpassen (zu kurz = trockene Bereiche)"
                ]
            },
            {
                "defect": "Starke Blasenbildung",
                "cause": "Spritzdruck zu hoch, Luft aus Harz entweicht, schlechte Verdichtung",
                "detection_method": "Oberflächenporengehalt sichtbar, Oberflächenrauhheit gemessen",
                "repair_possible": True,
                "prevention": [
                    "Spritzdruck reduzieren (3-5 bar optimal)",
                    "Harz vor Gebrauch entlüften (Vakuum 30 min)",
                    "Gründliches Walzen nach jeder Schicht",
                    "Umgebungsfeuchte gering halten (<70%)"
                ]
            }
        ],
        "cure_schedule": {
            "room_temperature_20c": {
                "gelcoat_handling_min": 45,
                "first_spray_min": 60,
                "between_layers_min": 15,
                "full_cure_hours": 20,
                "demold_hours": 24,
                "post_cure_not_recommended": True
            }
        }
    }
}

# ============================================================================
# 2. FIBER TYPES - All reinforcement fibers used in yacht building
# ============================================================================

FIBER_TYPES = {
    "e_glass_woven": {
        "name": "E-Glas Gewebe (2/2 Köper)",
        "description": "Elektrizitätsglas gewebte Fasern, Standard-Armierung für Yacht-Rümpfe. Sehr günstig, gute Festigkeit, niedriges spezifisches Gewicht.",
        "weight_gsm_range": {"min": 180, "max": 600},
        "common_weights_gsm": [200, 300, 450, 600],
        "tensile_strength_mpa": 1200,  # woven fiber bundle
        "tensile_modulus_gpa": 36,
        "cost_per_sqm_usd": 2.5,
        "density_g_per_cm3": 2.55,
        "drapeability": 0.65,
        "impact_resistance": 0.6,
        "suitable_resin_systems": [
            "polyester_ortho",
            "polyester_iso_npg",
            "vinylester",
            "epoxy_standard",
            "epoxy_infusion",
            "phenolic"
        ],
        "orientation_rules": [
            "Für Längsfestigkeit: 0° ausrichten",
            "Für Querkraft/Schub: ±45° oder ±60°",
            "Für 2D-Last-Fall: 0°/90° oder ±45°"
        ],
        "cutting_notes": "Fasern können mit scharfem Messer geschnitten werden. Keine speziellen Werkzeuge nötig. Nach Schnitt keine Fransen-Verschärfung nötig.",
        "quality_criteria": {
            "fiber_alignment_tolerance_deg": 2.0,
            "no_wrinkles": True,
            "no_damage_edges": True,
            "weight_tolerance_pct": 3.0,
            "burst_strength_kpa": {"min": 800}
        }
    },

    "e_glass_csm": {
        "name": "E-Glas CSM (Chopped Strand Mat)",
        "description": "Gehackte Glasfaser-Strähne, zufällig orientiert. Für schnelle Hand-Layup und Spray-up. Gute Oberflächen-Eigenschaften.",
        "weight_gsm_range": {"min": 300, "max": 900},
        "common_weights_gsm": [300, 450, 600, 750, 900],
        "tensile_strength_mpa": 800,
        "tensile_modulus_gpa": 20,
        "cost_per_sqm_usd": 1.8,
        "density_g_per_cm3": 2.55,
        "drapeability": 1.0,  # drapes perfectly, random orientation
        "impact_resistance": 0.75,
        "suitable_resin_systems": [
            "polyester_ortho",
            "polyester_iso_npg",
            "vinylester",
            "epoxy_standard"
        ],
        "orientation_rules": [
            "Zufällig orientiert - Verwendung für isotrope Eigenschaften",
            "Oft als erste Schicht nach Gelcoat (Haftung, Oberflächenqualität)",
            "Für Oberflächenschicht oder zwischen strukturellen Lagen"
        ],
        "cutting_notes": "Mit Schere leicht zu schneiden. Keine Fransen-Bildung. Kann beliebig zerteilt werden.",
        "quality_criteria": {
            "binder_quality": "Guter Zusammenhalt, keine Faserflocken beim Handling",
            "weight_tolerance_pct": 5.0,
            "no_powder_residue": True
        }
    },

    "e_glass_biax": {
        "name": "E-Glas Biaxial (0°/90° oder ±45°)",
        "description": "Gewebe mit zwei Orientierungen in einer Schicht. Kombiniert Festigkeit in zwei Richtungen. Häufiger als einzelnes Gewebe.",
        "weight_gsm_range": {"min": 300, "max": 600},
        "common_weights_gsm": [300, 450, 600],
        "common_orientations_deg": [[0, 90], [45, -45]],
        "tensile_strength_mpa": 1100,  # in primary direction
        "tensile_modulus_gpa": 32,
        "cost_per_sqm_usd": 3.2,
        "density_g_per_cm3": 2.55,
        "drapeability": 0.72,
        "impact_resistance": 0.7,
        "suitable_resin_systems": [
            "polyester_ortho",
            "polyester_iso_npg",
            "vinylester",
            "epoxy_standard",
            "epoxy_infusion"
        ],
        "orientation_rules": [
            "0°/90° Biax: Längsfestigkeit (0°) + Querfestigkeit (90°)",
            "±45° Biax: Schubfestigkeit und Torsions-Steifigkeit",
            "Typisches Aufbau-Schema: [0°/90°] → [±45°] → [0°/90°]"
        ],
        "cutting_notes": "Webabriss entlang Kette oder Schuss möglich. Fasern fallen nicht leicht auf.",
        "quality_criteria": {
            "fiber_alignment_tolerance_deg": 1.5,
            "no_wrinkles": True,
            "weight_tolerance_pct": 2.5,
            "ply_bond_strength": "Guter Zusammenhalt"
        }
    },

    "e_glass_triax": {
        "name": "E-Glas Triaxial (0°/±45° oder variabel)",
        "description": "Gewebe mit drei Orientierungen in einer Schicht. Bessere Multi-Direktional-Eigenschaften, weniger Schichten nötig.",
        "weight_gsm_range": {"min": 300, "max": 700},
        "common_weights_gsm": [300, 450, 600, 700],
        "common_orientations_deg": [[0, 45, -45], [0, 60, -60]],
        "tensile_strength_mpa": 1050,
        "tensile_modulus_gpa": 28,
        "cost_per_sqm_usd": 4.0,
        "density_g_per_cm3": 2.55,
        "drapeability": 0.68,
        "impact_resistance": 0.75,
        "suitable_resin_systems": [
            "polyester_ortho",
            "polyester_iso_npg",
            "vinylester",
            "epoxy_standard"
        ],
        "orientation_rules": [
            "Reduziert Lagen-Anzahl verglichen zu Biax (3 Richtungen statt 2)",
            "Wird oft allein verwendet oder mit UD-Lagen kombiniert",
            "Triax + UD 0°: Quasi-Isotropes Laminat mit guter Längsfestigkeit"
        ],
        "cutting_notes": "Kann entlang Kette oder Schuss geschnitten werden, aber Vorsicht: Diagonale Fasern können ausfasern.",
        "quality_criteria": {
            "fiber_alignment_tolerance_deg": 2.0,
            "ply_separation": "Kein Verrutschen zwischen Orientierungen",
            "weight_tolerance_pct": 3.0
        }
    },

    "e_glass_quadrax": {
        "name": "E-Glas Quadraxial (0°/90°/±45°)",
        "description": "Vier Orientierungen in einer Schicht. Maximale Flexibilität Multi-Direktional. Seltener verwendet, höhere Kosten.",
        "weight_gsm_range": {"min": 400, "max": 800},
        "common_weights_gsm": [450, 600, 750, 800],
        "tensile_strength_mpa": 1000,
        "tensile_modulus_gpa": 26,
        "cost_per_sqm_usd": 5.0,
        "density_g_per_cm3": 2.55,
        "drapeability": 0.60,
        "impact_resistance": 0.78,
        "suitable_resin_systems": [
            "epoxy_standard",
            "epoxy_infusion",
            "polyester_iso_npg",
            "vinylester"
        ],
        "orientation_rules": [
            "Verwendung in Konstruktionen mit komplexen Multi-Richtungs-Lasten",
            "Häufig in Racing-Yachten für optimales Gewicht/Steifigkeit-Verhältnis"
        ],
        "cutting_notes": "Schwierig zu schneiden ohne Beschädigungen. Spezialisiertes Schneid-Werkzeug empfohlen.",
        "quality_criteria": {
            "fiber_alignment_tolerance_deg": 2.5,
            "crimp_factor_pct": {"max": 10},
            "weight_tolerance_pct": 3.5
        }
    },

    "s_glass": {
        "name": "S-Glas Gewebe",
        "description": "High-Strength Glass. Höhere Zugfestigkeit und -Steifigkeit als E-Glas. Teuer, aber optimale Performance.",
        "weight_gsm_range": {"min": 200, "max": 600},
        "common_weights_gsm": [200, 300, 450, 600],
        "tensile_strength_mpa": 1400,  # ca. 15% höher als E-Glas
        "tensile_modulus_gpa": 42,  # ca. 15% höher als E-Glas
        "cost_per_sqm_usd": 6.0,
        "density_g_per_cm3": 2.48,
        "drapeability": 0.65,
        "impact_resistance": 0.65,
        "suitable_resin_systems": [
            "epoxy_standard",
            "epoxy_infusion",
            "epoxy_prepreg",
            "vinylester"
        ],
        "orientation_rules": [
            "Optimum für kritische Zonen: Mast-Basis, Kielschuh, Crash-Zone",
            "Mischung mit Carbon 50/50 für Performance-Optimierung (Kosten/Gewicht)"
        ],
        "cutting_notes": "Wie E-Glas - mit Messer leicht zu schneiden. Fasern sind etwas feiner.",
        "quality_criteria": {
            "fiber_alignment_tolerance_deg": 1.5,
            "no_fiber_damage": True,
            "weight_tolerance_pct": 2.5,
            "tensile_strength_min_mpa": 1350
        }
    },

    "carbon_ud": {
        "name": "Carbon UD (Unidirektional)",
        "description": "Durchgehende Carbonfasern in einer Richtung. Höchste Zugfestigkeit und Steifigkeit in Faser-Richtung. Teuer, niedrig Schub-Festigkeit.",
        "weight_gsm_range": {"min": 200, "max": 600},
        "common_weights_gsm": [200, 300, 400, 600],
        "tensile_strength_mpa": 2100,
        "tensile_modulus_gpa": 110,
        "cost_per_sqm_usd": 15.0,
        "density_g_per_cm3": 1.60,
        "drapeability": 0.5,  # Schwierig zu drapieren
        "impact_resistance": 0.3,  # Niedrig - bruchempfindlich
        "suitable_resin_systems": [
            "epoxy_standard",
            "epoxy_infusion",
            "epoxy_prepreg",
            "epoxy_autoclave"
        ],
        "orientation_rules": [
            "Nur in Längsrichtung verwenden (0°) für maximale Längsfestigkeit",
            "Immer kombiniert mit Biax oder CSM für Schub/Impact",
            "Typisches Schema: [UD 0°] + [Biax ±45°] für Multi-Direktional-Eigenschaften",
            "Lokale Verstärkungen in kritischen Bereichen (Mast, Kiel, Rumpf-Spannen)"
        ],
        "cutting_notes": "Carbon-Fasern sind elektrisch leitfähig - kann ESD-Schäden verursachen. Mit spezialisiertem Schneid-Werkzeug oder Schere schneiden.",
        "quality_criteria": {
            "fiber_alignment_tolerance_deg": 1.0,
            "no_waviness": True,
            "fiber_splitting": "Minimal",
            "weight_tolerance_pct": 1.5,
            "tensile_strength_min_mpa": 2050
        }
    },

    "carbon_twill": {
        "name": "Carbon Twill (2/2 Köper)",
        "description": "Carbon-Gewebe mit 2D-Köper-Bindung. Bessere Drapeierbarkeit als UD, anisotrope Eigenschaften.",
        "weight_gsm_range": {"min": 200, "max": 500},
        "common_weights_gsm": [200, 300, 400, 500],
        "tensile_strength_mpa": 1500,  # reduziert durch Webaltern
        "tensile_modulus_gpa": 70,
        "cost_per_sqm_usd": 18.0,
        "density_g_per_cm3": 1.60,
        "drapeability": 0.75,  # Besser als UD
        "impact_resistance": 0.4,
        "suitable_resin_systems": [
            "epoxy_standard",
            "epoxy_infusion",
            "epoxy_prepreg",
            "epoxy_autoclave"
        ],
        "orientation_rules": [
            "Für sichtbare Oberflächen (Twill-Muster sieht gut aus)",
            "Combination mit UD: [Twill 0/90°] + [UD 0°]",
            "Höhere Schubfestigkeit als UD allein"
        ],
        "cutting_notes": "Kann leicht entlang Kette/Schuss geschnitten werden. Webabriss ohne Fransen möglich.",
        "quality_criteria": {
            "fiber_alignment_tolerance_deg": 2.0,
            "weave_pattern_symmetry": "Perfekt symmetrisch",
            "weight_tolerance_pct": 2.0
        }
    },

    "carbon_biax": {
        "name": "Carbon Biaxial (0°/90° oder ±45°)",
        "description": "Carbon-Gewebe mit zwei Orientierungen. Balancierte 2D-Eigenschaften, gute Drapeierbarkeit.",
        "weight_gsm_range": {"min": 250, "max": 500},
        "common_weights_gsm": [300, 400, 500],
        "common_orientations_deg": [[0, 90], [45, -45]],
        "tensile_strength_mpa": 1200,
        "tensile_modulus_gpa": 65,
        "cost_per_sqm_usd": 20.0,
        "density_g_per_cm3": 1.60,
        "drapeability": 0.70,
        "impact_resistance": 0.45,
        "suitable_resin_systems": [
            "epoxy_standard",
            "epoxy_infusion",
            "epoxy_prepreg",
            "epoxy_autoclave"
        ],
        "orientation_rules": [
            "0°/90° Biax: Längsfestigkeit + Querfestigkeit (balanced)",
            "±45° Biax: Schubfestigkeit, Torsions-Steifigkeit",
            "Typisches Racing-Aufbau: [Carbon UD 0°] + [Carbon Biax ±45°] + [Glass Biax 0°/90°]"
        ],
        "cutting_notes": "Webabriss möglich entlang Kette. Fasern fallen nicht auf.",
        "quality_criteria": {
            "fiber_alignment_tolerance_deg": 1.5,
            "weight_tolerance_pct": 1.5,
            "ply_bond": "Gut"
        }
    },

    "aramid_plain": {
        "name": "Aramid Gewebe (Kevlar, Plain Weave)",
        "description": "Hochleistungs-Polymer-Fasern. Sehr hohe Zugfestigkeit, gute Schlag-Beständigkeit, gutes spezifisches Gewicht. Teuer.",
        "weight_gsm_range": {"min": 150, "max": 400},
        "common_weights_gsm": [160, 200, 300, 400],
        "tensile_strength_mpa": 1550,
        "tensile_modulus_gpa": 75,
        "cost_per_sqm_usd": 20.0,
        "density_g_per_cm3": 1.45,
        "drapeability": 0.78,
        "impact_resistance": 0.9,  # Ausgezeichnet - Impact-resistent
        "suitable_resin_systems": [
            "epoxy_standard",
            "epoxy_infusion",
            "epoxy_prepreg",
            "epoxy_autoclave"
        ],
        "orientation_rules": [
            "Für Schlag-kritische Zonen: Cockpit, Fender, Bug-Bereich",
            "Hybrid: [Carbon UD 0°] + [Aramid Biax ±45°] + [Glass CSM]",
            "Nicht für reine Längsfestigkeit (zu teuer) - nur für Impact/Energie-Absorb"
        ],
        "cutting_notes": "Schwer zu schneiden - Schere oder Spezial-Messer empfohlen. Fasern reißen leicht.",
        "quality_criteria": {
            "fiber_alignment_tolerance_deg": 2.0,
            "no_fiber_fraying": True,
            "weight_tolerance_pct": 2.5,
            "impact_strength_kj_per_m2": {"min": 80}
        }
    },

    "aramid_ud": {
        "name": "Aramid UD (Kevlar UD)",
        "description": "Unidirektionale Aramid-Fasern. Höchste Zugfestigkeit in Längsrichtung unter allen organischen Fasern.",
        "weight_gsm_range": {"min": 150, "max": 400},
        "common_weights_gsm": [160, 200, 300, 400],
        "tensile_strength_mpa": 1600,
        "tensile_modulus_gpa": 82,
        "cost_per_sqm_usd": 22.0,
        "density_g_per_cm3": 1.45,
        "drapeability": 0.45,
        "impact_resistance": 0.95,
        "suitable_resin_systems": [
            "epoxy_standard",
            "epoxy_infusion",
            "epoxy_prepreg",
            "epoxy_autoclave"
        ],
        "orientation_rules": [
            "Hochperformance-Racing-Struktur kombiniert mit Carbon",
            "[Aramid UD 0°] + [Carbon Biax ±45°] für leichte, starke Rümpfe"
        ],
        "cutting_notes": "Sehr schwer zu schneiden. Spezial-Werkzeuge notwendig. Fasern reißen.",
        "quality_criteria": {
            "fiber_alignment_tolerance_deg": 1.0,
            "no_waviness": True,
            "weight_tolerance_pct": 1.5
        }
    },

    "basalt_woven": {
        "name": "Basalt-Gewebe",
        "description": "Natürliches vulkanisches Mineral-Gewebe. Günstig wie Glass, höhere Eigenschaften, bessere Wärmebeständigkeit. Neuere Alternative.",
        "weight_gsm_range": {"min": 200, "max": 600},
        "common_weights_gsm": [200, 300, 450, 600],
        "tensile_strength_mpa": 1300,  # Zwischen Glass und Carbon
        "tensile_modulus_gpa": 45,
        "cost_per_sqm_usd": 3.5,
        "density_g_per_cm3": 2.70,
        "drapeability": 0.65,
        "impact_resistance": 0.70,
        "suitable_resin_systems": [
            "polyester_ortho",
            "polyester_iso_npg",
            "vinylester",
            "epoxy_standard",
            "epoxy_infusion"
        ],
        "orientation_rules": [
            "Ähnlich wie E-Glass - beliebig einsetzbar",
            "Basalt + Carbon Hybrid: [Basalt 0°/90°] + [Carbon UD 0°]",
            "Kostengünstigere Alternative zu Carbon-Hybrid"
        ],
        "cutting_notes": "Wie Glass - einfach mit Messer schneidbar. Keine speziellen Anforderungen.",
        "quality_criteria": {
            "fiber_alignment_tolerance_deg": 2.0,
            "weight_tolerance_pct": 3.0,
            "color_consistency": "Dunkelbraun/Schwarz gleichmäßig"
        }
    },

    "hybrid_carbon_aramid": {
        "name": "Carbon/Aramid Hybrid-Gewebe",
        "description": "Carbon und Aramid Fasern kombiniert in einer Schicht. Optimale Balance: Carbon-Steifigkeit + Aramid-Schlag-Beständigkeit.",
        "weight_gsm_range": {"min": 300, "max": 500},
        "common_weights_gsm": [300, 400, 500],
        "tensile_strength_mpa": 1750,  # Zwischen reiner Carbon/Aramid
        "tensile_modulus_gpa": 85,
        "cost_per_sqm_usd": 24.0,
        "density_g_per_cm3": 1.55,
        "drapeability": 0.70,
        "impact_resistance": 0.85,
        "suitable_resin_systems": [
            "epoxy_standard",
            "epoxy_infusion",
            "epoxy_prepreg",
            "epoxy_autoclave"
        ],
        "orientation_rules": [
            "Premium-Racing-Struktur",
            "Typisches Aufbau: [Carbon UD 0°] + [Carbon/Aramid Hybrid Biax ±45°]",
            "Kostet weniger als rein Carbon, besser Impact-Schutz"
        ],
        "cutting_notes": "Schwer zu schneiden. Spezial-Messer empfohlen. Carbon- und Aramid-Fasern haben unterschiedliche Schneidverhalten.",
        "quality_criteria": {
            "carbon_aramid_ratio": "Spezifiziert (z.B. 50/50)",
            "fiber_alignment_tolerance_deg": 1.5,
            "weight_tolerance_pct": 2.0
        }
    },

    "hybrid_carbon_glass": {
        "name": "Carbon/Glass Hybrid-Gewebe",
        "description": "Carbon und Glas-Fasern kombiniert. Kostengünstige Alternative zu reiner Carbon. Bessere Impact-Beständigkeit als reines Carbon.",
        "weight_gsm_range": {"min": 300, "max": 600},
        "common_weights_gsm": [300, 400, 500, 600],
        "tensile_strength_mpa": 1300,
        "tensile_modulus_gpa": 60,
        "cost_per_sqm_usd": 12.0,
        "density_g_per_cm3": 1.85,
        "drapeability": 0.70,
        "impact_resistance": 0.65,
        "suitable_resin_systems": [
            "epoxy_standard",
            "epoxy_infusion",
            "polyester_iso_npg",
            "vinylester"
        ],
        "orientation_rules": [
            "Wirtschaftliche Wahl für Performance-Cruiser",
            "Mischung: [Carbon/Glass Biax 0°/90°] + [Glass CSM]",
            "Reduziert Kosten ohne dramatische Festigkeits-Einbußen"
        ],
        "cutting_notes": "Wie Glass - mit Messer leicht schneidbar.",
        "quality_criteria": {
            "carbon_glass_ratio": "Typisch 40/60 bis 50/50",
            "fiber_alignment_tolerance_deg": 2.0,
            "weight_tolerance_pct": 2.5
        }
    }
}

# ============================================================================
# 3. RESIN SYSTEMS - Binding matrices for composite structures
# ============================================================================

RESIN_SYSTEMS = {
    "polyester_ortho": {
        "name": "Orthophthalisches Polyesterharz",
        "description": "Wirtschaftliches Standard-Harz für Hand-Layup. Niedrige Kosten, akzeptable Eigenschaften, schnelle Aushärtung.",
        "mix_ratio": "100:1 bis 2 (Harz:Katalysator MEK-PO, abhängig von Temperatur)",
        "pot_life_min_at_20c": 30,
        "pot_life_min_at_30c": 15,
        "gel_time_min_at_20c": 45,
        "gel_time_min_at_30c": 25,
        "peak_exotherm_c": 120,
        "shrinkage_pct": 7.5,
        "water_absorption_24h_pct": 0.8,
        "cost_per_kg_usd": 2.0,
        "suitable_for": [
            "hull_cruiser",
            "deck_structures",
            "non_critical_secondary",
            "production_standard"
        ],
        "quality_criteria": {
            "mix_accuracy_pct": 5.0,
            "gel_time_monitoring": "Kritisch - Katalysator-Genauigkeit ±10% erlaubt",
            "exotherm_control": "Max 40°C bei dicken Laminierungen (>3mm), Belüftung notwendig",
            "cure_completeness": "Voll durchgehärtet nach 24h bei 20°C"
        },
        "common_defects": [
            "Zu schnelle Gelierung (falscher Katalysator-Gehalt)",
            "Unvollständige Härtung bei niedrigen Temperaturen",
            "Starke Schrumpfung - Rissbildung",
            "Schlechte Feuchtigkeits-Beständigkeit (Wasser-Aufnahme)"
        ],
        "density_g_per_cm3": 1.12,
        "tensile_strength_mpa": 70,
        "tensile_modulus_gpa": 3.2,
        "flexural_strength_mpa": 110,
        "glass_transition_temp_c": 85
    },

    "polyester_iso_npg": {
        "name": "Isophthalsäure Polyesterharz mit NPG (Neopentylglykol)",
        "description": "Verbessertes Polyesterharz mit besserer Feuchtigkeits-Beständigkeit und Chemikalien-Resistenz. Bevorzugt für Wasseranlage-Teile.",
        "mix_ratio": "100:0.8 bis 1.5 (Harz:Katalysator)",
        "pot_life_min_at_20c": 35,
        "pot_life_min_at_30c": 18,
        "gel_time_min_at_20c": 50,
        "gel_time_min_at_30c": 28,
        "peak_exotherm_c": 115,
        "shrinkage_pct": 6.0,
        "water_absorption_24h_pct": 0.4,  # Besser als Ortho
        "cost_per_kg_usd": 2.3,
        "suitable_for": [
            "hull_below_waterline",
            "water_tanks_potable",
            "bilge_tanks",
            "areas_chemical_exposure"
        ],
        "quality_criteria": {
            "mix_accuracy_pct": 3.0,
            "water_absorption_resistance": "Sehr wichtig - max 0.4% in 24h",
            "exotherm_control": "Max 35°C empfohlen (niedriger als Ortho)",
            "cure_schedule_compliance": "Streng einhalten für optimale Feuchtigkeits-Beständigkeit"
        },
        "common_defects": [
            "Feuchtigkeits-assoziierte Quellung (bei zu hoher Feuchte während Laminierung)",
            "Osmose (Wasser-Blasen, späte Symptome nach 2-3 Jahren)"
        ],
        "density_g_per_cm3": 1.10,
        "tensile_strength_mpa": 85,
        "tensile_modulus_gpa": 3.4,
        "flexural_strength_mpa": 125,
        "glass_transition_temp_c": 95
    },

    "vinylester": {
        "name": "Vinylesterharz",
        "description": "Premium-Polyester mit Vinyl-Endgruppen. Bessere Feuchtigkeits-Beständigkeit, höhere Festigkeit und Chemikalien-Resistenz. Höhere Kosten.",
        "mix_ratio": "100:1 (Harz:Katalysator MEK-PO)",
        "pot_life_min_at_20c": 40,
        "pot_life_min_at_30c": 20,
        "gel_time_min_at_20c": 50,
        "gel_time_min_at_30c": 30,
        "peak_exotherm_c": 130,
        "shrinkage_pct": 5.0,
        "water_absorption_24h_pct": 0.2,
        "cost_per_kg_usd": 3.5,
        "suitable_for": [
            "hull_performance",
            "structural_bulkheads",
            "high_durability_zones",
            "racing_epoxy_alternative"
        ],
        "quality_criteria": {
            "mix_accuracy_pct": 2.0,
            "exotherm_control": "Kritisch - schnellere Exotherm-Reaktion als Polyester",
            "cure_schedule": "Kürzere Wartezeiten zwischen Schichten (15-25 min)",
            "post_cure_optional": "2-4h bei 60°C verbessert Eigenschaften um 5-10%"
        },
        "common_defects": [
            "Zu schnelle Gelierung bei hoher Temperatur",
            "Rissbildung durch zu dicke Schichten-auf-einmal",
            "Mangel-Härtung bei falscher Katalysatoren-Dosierung"
        ],
        "density_g_per_cm3": 1.06,
        "tensile_strength_mpa": 110,
        "tensile_modulus_gpa": 3.8,
        "flexural_strength_mpa": 160,
        "glass_transition_temp_c": 110,
        "chemical_resistance": "Ausgezeichnet - säure/base beständig"
    },

    "epoxy_standard": {
        "name": "Zweikomponenten-Epoxidharz (Bisphenol-A-Typ)",
        "description": "Premium-Harz mit höchster Festigkeit, ausgezeichnete Feuchtigkeits-Beständigkeit, schwierig zu verarbeiten, sehr teuer.",
        "mix_ratio": "100:35 bis 50 (Harz:Härter, variiert je nach Formulierung - exakt nach Datenblatt mischen!)",
        "pot_life_min_at_20c": 60,
        "pot_life_min_at_30c": 30,
        "gel_time_min_at_20c": 150,
        "gel_time_min_at_30c": 80,
        "peak_exotherm_c": 160,
        "shrinkage_pct": 2.0,
        "water_absorption_24h_pct": 0.1,
        "cost_per_kg_usd": 8.0,
        "suitable_for": [
            "racing_yachts",
            "structural_critical",
            "high_load_areas",
            "repair_premium"
        ],
        "quality_criteria": {
            "mix_accuracy_pct": 0.5,  # Kritisch! ±5% Fehler = Unterhärtung
            "mixing_procedure": "Langsam rühren, 2-3 min ruhen lassen (Blasen entlüften)",
            "temperature_stability": "Konstant 20-25°C während Verarbeitung",
            "exotherm_control": "Moderate Exotherm, aber langsam Temperatur anpassen",
            "post_cure_mandatory": "8-16h bei 80°C zur vollständigen Härtung / Tg-Erreichung"
        },
        "common_defects": [
            "Unterhärtung durch falsches Misch-Verhältnis",
            "Gelbfärbung durch UV-Eintrag (vor Post-Cure schützen)",
            "Blasenbildung durch unsachgemäße Mischung",
            "Temperatur-Empfindlichkeit während Verarbeitung"
        ],
        "density_g_per_cm3": 1.16,
        "tensile_strength_mpa": 80,  # Resin allein, mit Fasern: +120%)
        "tensile_modulus_gpa": 3.2,
        "flexural_strength_mpa": 140,
        "glass_transition_temp_c": 120,  # Nach Post-Cure: 130+
        "water_absorption_resistance": "Ausgezeichnet"
    },

    "epoxy_infusion": {
        "name": "Infusions-Epoxidharz (low-viscosity)",
        "description": "Speziell für Vakuum-Infusions-Prozess optimiert. Niedrige Viskosität für guten Harz-Fluss, optimierte Gel-Zeit.",
        "mix_ratio": "100:30 bis 45 (abhängig von Infusions-Geschwindigkeit)",
        "pot_life_min_at_20c": 120,
        "pot_life_min_at_30c": 60,
        "gel_time_min_at_20c": 200,
        "gel_time_min_at_30c": 100,
        "peak_exotherm_c": 140,
        "shrinkage_pct": 2.5,
        "water_absorption_24h_pct": 0.12,
        "viscosity_cps_at_20c": 250,  # Niedrig - für Durchfluss-Optimierung
        "cost_per_kg_usd": 9.0,
        "suitable_for": [
            "vacuum_infusion_rtm_light",
            "resin_transfer_molding",
            "large_composite_structures",
            "production_efficiency"
        ],
        "quality_criteria": {
            "mix_accuracy_pct": 0.5,
            "viscosity_stability": "Während Infusion konstant (Temperatur ±2°C)",
            "harz_degassing": "Minimal 30 min Vakuum vor Infusion",
            "infusion_flow_rate": "Überwachen - sollte konstant sein",
            "gel_time_achievement": "Nicht vor Infusions-Ende gelieren"
        },
        "common_defects": [
            "Trockenstellen - Infusion zu schnell beendet",
            "Harz-Bank durch zu viel Material",
            "Vorzeitige Gelierung bei zu hoher Temperatur"
        ],
        "density_g_per_cm3": 1.15,
        "tensile_strength_mpa": 75,
        "glass_transition_temp_c": 115
    },

    "epoxy_prepreg": {
        "name": "Prepreg-Epoxidharz (Oven/Autoclave-Grade)",
        "description": "Vorgefertigte Harzbeschichtung auf Fasern. Optimiert für Oven- oder Autoklav-Verarbeitung. Höchste Kontrolle über Eigenschaften.",
        "mix_ratio": "Nicht zutreffend (vorgefertigt)",
        "pot_life_not_applicable": True,
        "gel_time_not_applicable": True,
        "process_temperature_c": "80-140 (abhängig von Grade)",
        "shrinkage_pct": 1.5,
        "water_absorption_24h_pct": 0.08,
        "cost_per_kg_usd": 12.0,
        "suitable_for": [
            "prepreg_oven",
            "prepreg_autoclave",
            "aerospace_derivative",
            "high_precision_structures"
        ],
        "quality_criteria": {
            "storage_condition": "Gefrierschrank -18°C ±3°C, max 18 Monate",
            "room_temperature_acclimation": "60 min vor Verwendung (Kondenswasser-Vermeidung)",
            "layup_temperature": "18-25°C (zu warm = vorzeitige Gelierung)",
            "hand_peel_effort": "Sollte leicht schälen ohne Faseraufzug",
            "tack_level": "Moderat - hält Schichten zusammen ohne zu kleben",
            "fiber_volume_pct": "55-65% (bereits vorgestellt)"
        },
        "common_defects": [
            "Gelierung vor Verarbeitung (alte Charge oder zu warm gelagert)",
            "Zu trockenes Prepreg (Harz verdunstet)",
            "Faltenbildung während Layup",
            "Feuchtigkeits-Aufnahme (Kondensation auf kaltem Prepreg)"
        ],
        "density_g_per_cm3": 1.14,
        "tensile_strength_mpa": 85,
        "glass_transition_temp_c": 140  # Nach Härtung
    },

    "phenolic": {
        "name": "Phenolisches Harz (Heat-Resistant)",
        "description": "Spezial-Harz für höchste Temperatur-Beständigkeit. Seltener in Yachten, verwendet für Engine-Compartments oder Ballast-Strukturen.",
        "mix_ratio": "100:40 bis 60 (abhängig von Formulierung)",
        "pot_life_min_at_20c": 20,
        "gel_time_min_at_20c": 30,
        "peak_exotherm_c": 150,
        "shrinkage_pct": 4.0,
        "water_absorption_24h_pct": 0.15,
        "cost_per_kg_usd": 15.0,
        "suitable_for": [
            "engine_room_structures",
            "high_temperature_zones",
            "ballast_tank_critical",
            "specialty_applications"
        ],
        "quality_criteria": {
            "temperature_rating": "Kontinuierliche Anwendung bis 200°C",
            "fire_resistance": "Self-extinguishing, sehr gute Flammschutz-Eigenschaften",
            "exotherm_control": "Höher als Epoxid - Vorsicht bei dicken Schichten"
        },
        "common_defects": [
            "Brittle-Versagen bei Raumtemperatur (niedrige Schlag-Festigkeit)",
            "Formaldehyd-Abgasung während Laminierung (Sicherheit!)"
        ],
        "density_g_per_cm3": 1.30,
        "tensile_strength_mpa": 60,
        "glass_transition_temp_c": 200
    }
}

# ============================================================================
# 4. LAMINATE_SCHEDULES - Typical layup sequences for yacht zones
# ============================================================================

LAMINATE_SCHEDULES = {
    "hull_below_waterline_cruiser": {
        "description": "Standard Cruising-Rumpf unter Wasserlinie - ausreichend für 30+ Knoten-Segeln",
        "design_pressure_kpa": 35,
        "safety_factor": 3.5,
        "layers": [
            {"fiber_type": "e_glass_csm", "weight_gsm": 450, "orientation_deg": 0, "purpose": "Gelcoat-Haftung, Oberflächenschutz"},
            {"fiber_type": "e_glass_woven", "weight_gsm": 450, "orientation_deg": 0, "purpose": "Längsfestigkeit, Grundlage"},
            {"fiber_type": "e_glass_biax", "weight_gsm": 450, "orientation_deg": [0, 90], "purpose": "Biaxiale Festigkeit"},
            {"fiber_type": "e_glass_biax", "weight_gsm": 450, "orientation_deg": [45, -45], "purpose": "Schubfestigkeit, Torsion"},
            {"fiber_type": "e_glass_biax", "weight_gsm": 450, "orientation_deg": [0, 90], "purpose": "Querfestigkeit"},
            {"fiber_type": "e_glass_woven", "weight_gsm": 450, "orientation_deg": 90, "purpose": "Querfestigkeit"},
            {"fiber_type": "e_glass_biax", "weight_gsm": 450, "orientation_deg": [45, -45], "purpose": "Schubfestigkeit"},
            {"fiber_type": "e_glass_biax", "weight_gsm": 450, "orientation_deg": [0, 90], "purpose": "Symmetrie, Ausgleich"}
        ],
        "total_thickness_mm": 5.5,
        "expected_weight_kg_per_m2": 28,
        "tensile_strength_mpa": 280,
        "flexural_strength_mpa": 380,
        "shear_strength_mpa": 14,
        "notes": "Klassischer Aufbau mit E-Glas und Polyester/Vinylester. Bewährt über 30 Jahre Bootslegung."
    },

    "hull_above_waterline_cruiser": {
        "description": "Rumpf über Wasserlinie - weniger Druck, aber UV-Belastung",
        "design_pressure_kpa": 15,
        "safety_factor": 4.0,
        "layers": [
            {"fiber_type": "e_glass_csm", "weight_gsm": 450, "orientation_deg": 0, "purpose": "Gelcoat-Haftung"},
            {"fiber_type": "e_glass_woven", "weight_gsm": 300, "orientation_deg": 0, "purpose": "Längsfestigkeit"},
            {"fiber_type": "e_glass_biax", "weight_gsm": 450, "orientation_deg": [0, 90], "purpose": "Biaxiale Grundlage"},
            {"fiber_type": "e_glass_biax", "weight_gsm": 300, "orientation_deg": [45, -45], "purpose": "Schubfestigkeit"},
            {"fiber_type": "e_glass_biax", "weight_gsm": 300, "orientation_deg": [0, 90], "purpose": "Querfestigkeit"},
            {"fiber_type": "e_glass_woven", "weight_gsm": 300, "orientation_deg": 90, "purpose": "Oberflächenschutz"}
        ],
        "total_thickness_mm": 3.8,
        "expected_weight_kg_per_m2": 20,
        "tensile_strength_mpa": 220,
        "flexural_strength_mpa": 300,
        "shear_strength_mpa": 10,
        "notes": "Dünnere Lage möglich da weniger Wasserdruck. Aber UV-Schutz durch Gelcoat wichtig."
    },

    "deck_cruiser": {
        "description": "Deck-Struktur - kombiniert strukturelle Anforderungen mit Walking-Sicherheit",
        "design_pressure_kpa": 12,
        "safety_factor": 4.5,
        "layers": [
            {"fiber_type": "e_glass_csm", "weight_gsm": 300, "orientation_deg": 0, "purpose": "Oberflächenschutz, Rutsch-Beständigkeit"},
            {"fiber_type": "e_glass_woven", "weight_gsm": 300, "orientation_deg": 0, "purpose": "Längsfestigkeit"},
            {"fiber_type": "e_glass_biax", "weight_gsm": 300, "orientation_deg": [45, -45], "purpose": "Schubfestigkeit, Torsions-Steifigkeit"},
            {"fiber_type": "e_glass_biax", "weight_gsm": 300, "orientation_deg": [0, 90], "purpose": "Biaxiale Ausgleich"},
            {"fiber_type": "e_glass_woven", "weight_gsm": 300, "orientation_deg": 90, "purpose": "Querfestigkeit"}
        ],
        "total_thickness_mm": 3.2,
        "expected_weight_kg_per_m2": 17,
        "tensile_strength_mpa": 190,
        "flexural_strength_mpa": 260,
        "shear_strength_mpa": 8,
        "notes": "CSM-Oberflächenschicht für bessere Rutsch-Beständigkeit. Durchtritt-Verstärkungen um Mastten nötig."
    },

    "hull_racing": {
        "description": "Racing-Rumpf - Maximum Leistung/Gewicht, höhere Kosten, kritische Qualität",
        "design_pressure_kpa": 50,
        "safety_factor": 2.5,
        "layers": [
            {"fiber_type": "e_glass_csm", "weight_gsm": 300, "orientation_deg": 0, "purpose": "Gelcoat-Haftung"},
            {"fiber_type": "carbon_ud", "weight_gsm": 300, "orientation_deg": 0, "purpose": "Längsfestigkeit - höchste"},
            {"fiber_type": "carbon_biax", "weight_gsm": 300, "orientation_deg": [45, -45], "purpose": "Schubfestigkeit, Torsion"},
            {"fiber_type": "carbon_ud", "weight_gsm": 300, "orientation_deg": 0, "purpose": "Längsfestigkeit-Verstärkung"},
            {"fiber_type": "carbon_biax", "weight_gsm": 300, "orientation_deg": [45, -45], "purpose": "Schub/Torsion"},
            {"fiber_type": "e_glass_biax", "weight_gsm": 450, "orientation_deg": [0, 90], "purpose": "Schutz vor Impact, Haftung"}
        ],
        "total_thickness_mm": 4.2,
        "expected_weight_kg_per_m2": 24,
        "tensile_strength_mpa": 420,
        "flexural_strength_mpa": 550,
        "shear_strength_mpa": 18,
        "notes": "Carbon UD + Biax Hybrid. Letzte Schicht Glass für Schlag-Schutz und Haftung. Vacuum-Infusion oder RTM notwendig."
    },

    "bulkhead_structural": {
        "description": "Struktur-Schotte für Wasserdichtigkeit und Lasten-Übertragung",
        "design_pressure_kpa": 40,
        "safety_factor": 3.0,
        "layers": [
            {"fiber_type": "e_glass_woven", "weight_gsm": 450, "orientation_deg": 0, "purpose": "Längsfestigkeit"},
            {"fiber_type": "e_glass_biax", "weight_gsm": 600, "orientation_deg": [45, -45], "purpose": "Schubfestigkeit - kritisch"},
            {"fiber_type": "e_glass_woven", "weight_gsm": 450, "orientation_deg": 90, "purpose": "Querfestigkeit"},
            {"fiber_type": "e_glass_biax", "weight_gsm": 600, "orientation_deg": [45, -45], "purpose": "Schubfestigkeit (Mitte)"},
            {"fiber_type": "e_glass_woven", "weight_gsm": 450, "orientation_deg": 0, "purpose": "Längsfestigkeit (Gegenseite)"}
        ],
        "total_thickness_mm": 6.0,
        "expected_weight_kg_per_m2": 32,
        "tensile_strength_mpa": 300,
        "flexural_strength_mpa": 400,
        "shear_strength_mpa": 16,
        "notes": "Symmetrischer Aufbau. Hohe Schubfestigkeit durch ±45°-Betonung. Laminierung muss fehlerfrei sein (Wasserdichtigkeit)."
    },

    "cabin_top": {
        "description": "Kabinen-Dachabdeckung - niedrige Lasten, aber Langlebigkeit kritisch",
        "design_pressure_kpa": 8,
        "safety_factor": 5.0,
        "layers": [
            {"fiber_type": "e_glass_csm", "weight_gsm": 300, "orientation_deg": 0, "purpose": "Oberflächenschutz, UV-Stabilität"},
            {"fiber_type": "e_glass_woven", "weight_gsm": 300, "orientation_deg": 0, "purpose": "Grundlage"},
            {"fiber_type": "e_glass_biax", "weight_gsm": 300, "orientation_deg": [45, -45], "purpose": "Schubfestigkeit"},
            {"fiber_type": "e_glass_woven", "weight_gsm": 300, "orientation_deg": 90, "purpose": "Querfestigkeit"}
        ],
        "total_thickness_mm": 2.5,
        "expected_weight_kg_per_m2": 14,
        "tensile_strength_mpa": 160,
        "flexural_strength_mpa": 220,
        "shear_strength_mpa": 6,
        "notes": "Gewichtseinsparung möglich (dünn). CSM-Oberseite für guten Sonnenschutz und UV-Beständigkeit."
    },

    "transom": {
        "description": "Motor-Transom / Heck-Schott - hohe lokalisierte Lasten vom Motor",
        "design_pressure_kpa": 80,
        "safety_factor": 2.5,
        "layers": [
            {"fiber_type": "e_glass_csm", "weight_gsm": 450, "orientation_deg": 0, "purpose": "Haftung, Oberflächenschutz"},
            {"fiber_type": "e_glass_woven", "weight_gsm": 600, "orientation_deg": 0, "purpose": "Längsfestigkeit - höchste (senkrecht)"},
            {"fiber_type": "e_glass_biax", "weight_gsm": 600, "orientation_deg": [45, -45], "purpose": "Schubfestigkeit"},
            {"fiber_type": "e_glass_woven", "weight_gsm": 600, "orientation_deg": 90, "purpose": "Querfestigkeit"},
            {"fiber_type": "e_glass_biax", "weight_gsm": 600, "orientation_deg": [45, -45], "purpose": "Schubfestigkeit (Gegenseite)"},
            {"fiber_type": "e_glass_woven", "weight_gsm": 600, "orientation_deg": 0, "purpose": "Längsfestigkeit-Verstärkung"}
        ],
        "total_thickness_mm": 7.5,
        "expected_weight_kg_per_m2": 38,
        "tensile_strength_mpa": 350,
        "flexural_strength_mpa": 480,
        "shear_strength_mpa": 20,
        "notes": "Dickste Standardlage. Lokale Verstärkungen unter Motor-Halterungen. Potting von Befestigungs-Inserts essentiell."
    },

    "keel_area": {
        "description": "Kielschuh / Unterwasser-Verstärkung - abrasion-resistant, hohe Dauerlasten",
        "design_pressure_kpa": 60,
        "safety_factor": 2.5,
        "layers": [
            {"fiber_type": "s_glass_woven", "weight_gsm": 450, "orientation_deg": 0, "purpose": "Höhere Festigkeit als E-Glas"},
            {"fiber_type": "carbon_ud", "weight_gsm": 300, "orientation_deg": 0, "purpose": "Längsfestigkeit-Maximierung"},
            {"fiber_type": "carbon_biax", "weight_gsm": 300, "orientation_deg": [45, -45], "purpose": "Schubfestigkeit"},
            {"fiber_type": "s_glass_woven", "weight_gsm": 450, "orientation_deg": 90, "purpose": "Querfestigkeit, Dauer-Beständigkeit"},
            {"fiber_type": "carbon_ud", "weight_gsm": 300, "orientation_deg": 0, "purpose": "Längsfestigkeit (Verstärkung)"},
            {"fiber_type": "carbon_biax", "weight_gsm": 300, "orientation_deg": [45, -45], "purpose": "Schubfestigkeit (Gegenseite)"}
        ],
        "total_thickness_mm": 5.8,
        "expected_weight_kg_per_m2": 32,
        "tensile_strength_mpa": 480,
        "flexural_strength_mpa": 620,
        "shear_strength_mpa": 22,
        "notes": "Hybrid Carbon/S-Glass für optimale Kosten/Leistung. Externe Schutz-Coating (Epoxy + Antifouling) essentiell."
    }
}

# ============================================================================
# 5. SANDWICH_CORE_PROCESSING - Sandwich-Struktur Verarbeitung
# ============================================================================

SANDWICH_CORE_PROCESSING = {
    "contour_cutting": {
        "description": "Präzisions-Schneiden von Kern-Material (Schaumstoff, Holz) in Formen",
        "materials_applicable": ["PVC_foam", "PET_foam", "Balsa", "Rohacell", "Core_materials"],
        "quality_criteria": {
            "cut_tolerance_mm": {"max": 1.0},
            "edge_smoothness": "Keine scharfen Kanten - mit Schleifen nacharbeiten",
            "no_core_crushing": True,
            "surface_contamination_free": True
        },
        "best_practices": [
            "Heizbrett-Schneiden für Schaumstoff (schmilzt sauberer als Säge)",
            "Säge oder Messer für Balsa (trocken, keine Hitze)",
            "Schleif-Nachbearbeitung mit 80er-Körnung für glatte Kanten",
            "Staub vollständig absaugen - Kontamination verhindert spätere Haft",
            "Größe-Toleranz: ±0.5mm anstreben (nicht ±1mm!)",
            "Ecken-Radien wo möglich (verhindert Spannungs-Konzentration)"
        ],
        "common_failures": [
            "Quetschungen durch zu scharfe Werkzeuge",
            "Ungleichmäßige Schnittflächen (Oberflächen-Rauheit)",
            "Kern-Beschädigungen - später Wasser-Eindringung",
            "Staub-Verschmutzung - schlechte Haft zwischen Kern und Fasern"
        ]
    },

    "scarf_joining": {
        "description": "Schräg-Verbindung von zwei Kern-Stücken - minimiert Stufen",
        "scarf_ratio": {"min": 8, "optimal": 12, "description": "Verhältnis Länge:Dicke"},
        "quality_criteria": {
            "scarf_angle_deg": {"optimal": 6, "tolerance": "±0.5"},
            "surface_smoothness_ra_um": {"max": 1.6},
            "scarf_alignment": "Keine Höhen-Unterschiede >0.1mm",
            "joint_strength_pct_of_core": {"min": 90}
        },
        "best_practices": [
            "Schleif-Maschine oder CNC-Schleifer für Genauigkeit (besser als Handwerk)",
            "Schräg-Winkel langsam anfahren - gleichmäßiger Satz",
            "Nach Schleif-Prozess: Oberflächenrauheit <1.6µm Ra (glatte Haftung)",
            "Kern-Stücke vor Verklebung trocknen (Feuchte <5% für PVC-Schaumstoff)",
            "Verklebung mit Kern-spezifischem Harz durchführen (z.B. Epoxy)",
            "Verklebung mit leichtem Druck komprimieren (nicht quetschen!)",
            "Aushärtung >24h vor Faseraufbau"
        ],
        "common_failures": [
            "Zu kurzer Scarf-Ratio (<8:1) - Scherkräfte konzentriert",
            "Rauhe Schräg-Flächen - schlechte Haft",
            "Falsche Höhen-Ausrichtung - Spannungs-Spitzen",
            "Falsche Klebstoff - zu spröde oder zu duktil"
        ]
    },

    "potting_inserts": {
        "description": "Einbettung von Gewindeinserts, Bolzen, Fittings in Kern-Material",
        "insert_types": ["threaded_inserts", "eyebolts", "chain_plates", "fitting_bosses"],
        "quality_criteria": {
            "insert_alignment_deg": {"max": 2.0},
            "potting_material_coverage_mm": {"min": 10},
            "no_air_voids": True,
            "material_connection_strength": "Insert reißt nicht aus unter Last"
        },
        "best_practices": [
            "Insert-Position vor Kern-Aufbau festlegen (nicht nachträglich bohren!)",
            "Bohrung in Kern-Material 1-2mm größer als Insert-Durchmesser",
            "Kern-Bohrung mit Epoxy-Harz ausfüllen (dünnflüssig für gute Durchdringung)",
            "Insert einpress mit korrrekter Tiefe (ganz durchdringen, nicht zu tief)",
            "Harz aushärten >24h vor weiterer Bearbeitung",
            "Nach Härtung: Oberfläche eben schleifen (Insert-Kopf bündig)"
        ],
        "installation_procedure": [
            "1. Kern-Material mit Harz-Bett vorbereiten",
            "2. Bohrung nach exaktem Plan durchführen",
            "3. Bohrung mit Epoxy fluten (Harz füllt Kern-Porenraum)",
            "4. Insert einpressen mit leichtem Drehmoment-Kontakt",
            "5. Überschüssiges Harz abwischen",
            "6. Aushärtung 24-48h",
            "7. Test-Torsion: Insert-Festigkeit prüfen"
        ],
        "common_failures": [
            "Luftblasen unter Insert - Insert-Lockering später",
            "Zu geringe Harz-Durchdringung - Wasser-Eindringung bei Salzwasser-Kontakt",
            "Falsche Insert-Tiefe - Gewindeschäden",
            "Korrosion von Metall-Insert (Edelstahl empfohlen)"
        ]
    },

    "core_bonding": {
        "description": "Haftung von Kern zwischen oberer und unterer Faser-Schale",
        "bonding_approaches": ["wet_layup_direct", "adhesive_film", "adhesive_paste"],
        "quality_criteria": {
            "bond_line_thickness_mm": {"optimal": 0.5, "max": 2.0},
            "void_content_pct": {"max": 2.0},
            "delamination_risk": "Null - vollständige Haft erforderlich",
            "bond_strength_mpa": {"min": 5.0}
        },
        "wet_layup_direct": {
            "description": "Kern direkt auf feuchter Faser-Unterschicht aufbringen",
            "procedure": [
                "1. Faser-Unterschicht bis zur Gele-Zeit durchlaminieren",
                "2. Kern-Material auf feuchte Oberfläche auflegen",
                "3. Mit Walze oder Pressdruck verdichten (keine Lufttaschen)",
                "4. Oberfaser-Schicht sofort aufbringen",
                "5. Gesamte Sandwich-Struktur vollständig durchwalzen"
            ],
            "best_practices": [
                "Unterschicht sollte noch klebrig sein (15-45 min nach Laminierung)",
                "Kern-Material trocken und staub-frei",
                "Walzendruck moderat - Kern nicht quetschen/komprimieren",
                "Oberflächenfinish nach Verdichtung: glatte Wellen, keine Lücken",
                "Aushärtung unter ständigem Druck (vakuum-bag optional)"
            ]
        },
        "adhesive_film": {
            "description": "Spezial-Harz-Film zwischen Kern und Faserschale (meist Prepreg-Systeme)",
            "procedure": [
                "1. Harz-Film auf Faser-Unterschicht auflegen",
                "2. Kern auf Film platzieren",
                "3. Oberfaser-Schicht aufbringen",
                "4. Während Härtung erhitzen (aktiviert Harz-Film-Klebrigkeit)"
            ],
            "best_practices": [
                "Film-Temperatur: meist 80-120°C zum Aktivieren",
                "Druck während Härtung: vakuum + Oven oder Autoklav",
                "Film-Dicke: 50-200µm (abhängig von Harz-Type)",
                "Komplette Kern-Abdeckung - keine freien Stellen"
            ]
        },
        "adhesive_paste": {
            "description": "Paste-Klebstoff (z.B. Epoxy-Paste) zwischen Kern und Faserschale",
            "procedure": [
                "1. Paste auf Kern-Oberfläche auftragen (dünne Schicht ~0.5mm)",
                "2. Kern auf Unterschicht auflegen",
                "3. Oberfasern aufbringen und walzen",
                "4. Aushärtung unter Druck (vakuum empfohlen)"
            ],
            "best_practices": [
                "Paste-Auftrag: Walze oder Sprayer für gleichmäßige Schicht",
                "Kern-Auflage: Mit Walze verdichten bis Harz-Überschuss sichtbar",
                "Druck-Haltung: 12-24h für vollständige Haft",
                "Harz-Auswahl: Kompatibel mit Faserschale-Harz"
            ]
        },
        "common_failures": [
            "Kern-Delaminierung später durch Wassereindringung (Haftungsverlust)",
            "Trockene Stellen - fehlende Haftung in Zonen",
            "Harz-Bluten (zu viel Haft-Schicht) - spätere Risse",
            "Kern-Quetschung durch zu hohen Druck"
        ]
    },

    "edge_closeout": {
        "description": "Versiegelung von freiliegenden Kern-Kanten (Wasser-Eindringung verhindern)",
        "closeout_methods": ["folded_laminate", "cap_strip", "resin_fillet"],
        "quality_criteria": {
            "edge_seal_completeness_pct": 100,
            "resin_penetration_mm": {"min": 5},
            "no_exposed_core": True,
            "water_ingress_rate_ml_per_year": {"max": 0}
        },
        "folded_laminate": {
            "description": "Oberfaser um Kern-Kante herum falten (einfach, effektiv)",
            "procedure": [
                "1. Oberfaserschale 50-100mm über Kern-Kante hinaus laminieren",
                "2. Am Kant-Ende: Fasern nach unten / innen falten",
                "3. Zusätzlich CSM oder Biax auf Innenfläche auftragen",
                "4. Festwalzen und aushärten"
            ],
            "advantages": [
                "Einfaches Verfahren, keine Zusatzteile",
                "Hohe Festigkeit durch durchgehende Fasern",
                "Kostengünstig"
            ]
        },
        "cap_strip": {
            "description": "Spezial-Kappe oder Deckel auf Kern-Kante aufgeklebt",
            "procedure": [
                "1. Kern-Kante glatt schleifen / vorbereiten",
                "2. Kappe (Kunststoff, Laminated-Streifen) mit Epoxy kleben",
                "3. Mit Druck verdichten bis Harz vollständig durchdringt",
                "4. Aushärtung >24h"
            ],
            "materials": [
                "Aluminum-Kappe (leicht, dauerhaft)",
                "HDPE-Kappe (günstig, UV-empfindlich)",
                "Laminat-Kappe (beste Haftung zu Composites)"
            ]
        },
        "resin_fillet": {
            "description": "Dicke Harz-Ausfüllung mit oder ohne Fasern an Kern-Kanten",
            "procedure": [
                "1. Kern-Kante glätten",
                "2. Harz-Paste + Füllstoff (z.B. Hollow Microspheres) anmischen",
                "3. Auf Kern-Kante aufbringen, glätten",
                "4. Optional: CSM-Streifen auf feuchte Paste auftragen",
                "5. Aushärtung >24h, dann überschleifen"
            ],
            "best_practices": [
                "Fillet-Radius: 10-20mm (verhindert Spannungs-Spitzen)",
                "Harz-Konsistenz: Peanut-Butter-artig (nicht zu flüssig)",
                "Füllstoff-Anteil: 30-50% (leicht, aber stabil)",
                "Aushärtung: Schutz vor Wasser während Härtung"
            ]
        },
        "common_failures": [
            "Unvollständige Versiegelung - Wasser dringt in Kern-Porenraum",
            "Spröde Harz-Füllung - Risse unter mechanischer Last",
            "Falscher Fillet-Radius - Spannungs-Konzentration",
            "Unzureichende Haft zwischen Cap und Kern"
        ]
    }
}

# ============================================================================
# 6. REPAIR_TECHNIQUES - Composite repair procedures
# ============================================================================

REPAIR_TECHNIQUES = {
    "gelcoat_scratch": {
        "description": "Oberflächenabschabung in Gelcoat (keine Faser sichtbar)",
        "severity": "Kosmetisch - keine strukturellen Auswirkungen",
        "procedure_steps": [
            "1. Kratzer mit 80er-Schleifer vergrößern (V-Nute, Haftung verbessern)",
            "2. Bereich mit 120er nachschleifen - raue Oberfläche",
            "3. Mit feuchtem Tuch abwischen, trocknen lassen",
            "4. Neu angemischtes Gelcoat auftragen (matched color)",
            "5. 30-60 min aushärten lassen",
            "6. Mit 120er schleifen (glätten), dann 400er Finish-Schliff",
            "7. Mit feinem Poliertuch und Poliercompound polieren"
        ],
        "material_list": [
            "Gelcoat (farbabgestimmt)",
            "Katalysator (0.5-1.0%)",
            "Schleifpapier (80, 120, 400er Körnung)",
            "Poliercompound und Tuch",
            "Sicherheitsausrüstung (Maske, Schutzbrille)"
        ],
        "cure_time_hours": 0.5,
        "quality_criteria": {
            "gloss_match_to_original": "Mindestens 85% (hochglanz Material)",
            "no_color_mismatch": "Farbton innerhalb 3 Delta-E",
            "smooth_finish": "Keine Kratzer oder Unebenheiten sichtbar"
        },
        "common_mistakes": [
            "Zu tiefes Abschleifen - Faser sichtbar (wird zu Crack-Repair)",
            "Falsches Gelcoat-Tintung - Farbmismatch",
            "Unzureichende Oberflächen-Rauhheit - Gelcoat haftet nicht",
            "Zu schnelle oder zu langsame Härtung (Temperatur-abhängig)"
        ]
    },

    "gelcoat_crack": {
        "description": "Riss im Gelcoat (Faser sichtbar oder drohend)",
        "severity": "Minor - aber verhindert Wasser-Eindringung",
        "procedure_steps": [
            "1. Riss mit Winkelschleifer (2-3mm breit) aufschneiden - V-Nute bilden",
            "2. Mit 120er-Schleifer ausschleifen, danach 200er glätten",
            "3. Staub und Verschmutzung absaugen/wegwischen",
            "4. Epoxy-Grundierung dünn auftragen (optional, aber empfohlen)",
            "5. Riss mit angemischtem Gelcoat füllen (etwas über Oberflächenniveau)",
            "6. Mit Plastik-Spatel glätten, Überschuss entfernen",
            "7. 60-90 min aushärten (abhängig von Katalysator-Dosierung)",
            "8. Mit 120er schleifen, dann 400er Finish-Schliff",
            "9. Mit Poliercompound polieren"
        ],
        "material_list": [
            "Epoxy-Epoxi 2-K (optional, für Haftung)",
            "Gelcoat (farbabgestimmt)",
            "Katalysator (0.5-1.0%)",
            "Schleifpapier (80, 120, 200, 400er)",
            "Plastik-Spatel",
            "Poliercompound"
        ],
        "cure_time_hours": 1.5,
        "quality_criteria": {
            "riss_fullness": "Komplett gefüllt - keine Lufttaschen",
            "surface_level_match": "Glatt, keine Unebenheiten",
            "gloss_match": "Mindestens 90% Original"
        },
        "common_mistakes": [
            "Riss nicht ausreichend aufgeweitet - Gelcoat reißt nach",
            "Luft in Gelcoat-Füllung (unter Oberflächenspannung)",
            "Falsche Katalysator-Dosierung - Unterhärtung",
            "Zu feuchte Reparatur-Stelle - Wasserdampf-Blasen"
        ]
    },

    "delamination_small": {
        "description": "Lokale Schichthaftungsfehlstelle ohne strukturelle Bedeutung (<500cm²)",
        "severity": "Minor - aber weitet sich aus wenn nicht repariert",
        "procedure_steps": [
            "1. Delaminiertes Gebiet markieren (mit Marker von unten sichtbar machen)",
            "2. Mit Lochsäge oder Winkelschleifer Loch in Oberfläche schneiden (5-10cm über Delaminierung)",
            "3. Mit Druckluft oder Spritze Epoxy-Harz in Hohlraum injizieren (unter Druck)",
            "4. Harz mit Schaumstoff-Plugger verteilen, austreiben von Luft",
            "5. Loch mit Epoxy-Spachtelmasse verschließen und glatt abziehen",
            "6. 24h aushärten",
            "7. Mit 120er-400er Körnung schleifen, polieren"
        ],
        "material_list": [
            "Low-Viscosity Epoxy (für Injektionen)",
            "Epoxy-Spachtelmasse (für Verschluss)",
            "Injektions-Nadelspritze oder -Pumpe",
            "Schaumstoff-Spreizer",
            "Schleifpapier und Poliercompound"
        ],
        "cure_time_hours": 24,
        "quality_criteria": {
            "adhesive_penetration_pct": 100,
            "no_remaining_voids": True,
            "surface_smoothness": "Glatt nach Schliff",
            "delamination_recurrence_probability": "Minimal (<5%)"
        },
        "common_mistakes": [
            "Nicht genug Harz injiziert - Luft bleibt",
            "Druck zu hoch - Matrix-Risse entstehen",
            "Falscher Epoxy-Typ (zu hochviskos) - blockiert",
            "Zu tiefes Schleifen nach Repair - Material-Entfernung"
        ]
    },

    "delamination_large": {
        "description": "Großflächige Schichthaftungsfehlstelle (>500cm²) - strukturelle Integrität betroffen",
        "severity": "Major - Boot nicht fahrsicher",
        "procedure_steps": [
            "1. Delaminiertes Gebiet exakt kartographieren (mit Tap-Test Oberflächengeometrie feststellen)",
            "2. Rechteckiges Reparatur-Feld zuschneiden (20-30mm Sicherheits-Rand außerhalb Delaminierung)",
            "3. Mit Winkelschleifer bis auf strukturelle Faserschicht ausschleifen (inklusive aller Gelcoat/oberflächlicher Lagen)",
            "4. Unterseite (wenn zugänglich) analog ausschleifen",
            "5. Alle Oberflächen mit 120er-Körnung rauh machen - Staub absaugen",
            "6. Epoxy-Harz mit Pinsel großzügig auftragen (1-2 Schichten)",
            "7. Neue Faserschichten aufbauen (identisch zur Original-Schichtfolge)",
            "8. Erste Schicht: CSM oder Gewebe (Haftung zu alter Struktur)",
            "9. Dann: Fiberglas-Schichten analog Original (Dicke aufbauen)",
            "10. Mit Vakuum-Bag verdichten (bevorzugt für großflächige Reparatur)",
            "11. Aushärtung 24-48h",
            "12. Oberflächenfinish: Schleifen und polieren (inkl. Gelcoat neu auftragen)"
        ],
        "material_list": [
            "Epoxy-Harz (bulk)",
            "Glasfaser-Schichten (CSM, Gewebe, ggf. Biax - identisch zu Original)",
            "Vakuum-Bag-System (optional aber empfohlen)",
            "Winkelschleifer, Schleifpapier",
            "Wälzen/Bürsten für Laminierung",
            "Gelcoat zur Oberflächenfinish"
        ],
        "cure_time_hours": 48,
        "quality_criteria": {
            "layer_integrity": "Neue Schichten vollständig durchlaminiert, blasenfrei",
            "adhesion_to_original": "Fest, keine neuen Delaminierungen",
            "structural_strength_recovery_pct": 95,
            "visual_finish_match": "Gloss und Oberflächenfinish vergleichbar zu Original"
        },
        "common_mistakes": [
            "Reparatur-Feld zu klein - Delaminierung schreitet außer den Grenzen fort",
            "Unzureichende Rauhheit alter Oberfläche - neue Schichten haften nicht",
            "Falsche Schichtfolge - Eigenschaften nicht wiederhergestellt",
            "Zu dicke neue Laminierung auf einmal - Exotherm-Risse",
            "Vakuum nicht gehalten während Härtung - wieder Blasen"
        ]
    },

    "osmosis_treatment": {
        "description": "Behandlung von Osmose (Wasser-eindringung + Blasenbildung im Rumpf)",
        "severity": "Major - Boot unverwendbar bis behandelt",
        "procedure_steps": [
            "1. Diagnose: Mit Holzfeuchte-Messgerät Wasser-Gehalt in Laminate prüfen (>3-4% kritisch)",
            "2. Blasen markieren - Tap-Test oder Infrarot-Thermografie",
            "3. Mit Winkelschleifer oben: Gelcoat + oberflächliche Faserschicht entfernen (bis auf feste Struktur)",
            "4. Wenn möglich: Unterseite auch entfernen (Vollständigkeit)",
            "5. Exponierte Struktur mehrere Wochen trocknen lassen (bei warmer/trockener Umgebung, ggf. mit Wärmeleitung)",
            "6. Nach Trocknung: Feuchte-Test wiederholen (sollte <2% sein)",
            "7. Trockene Oberfläche rauh machen (Körnung 80-120)",
            "8. Epoxy-Barrier-Coat auftragen (2-3 Schichten, je 0.5-1mm)",
            "9. Oberflächenfinish: Neues Gelcoat oder Farbe",
            "10. Nach Repair: Belüftung sicherstellen (Rumpf-Entlüftung) für langfristigen Erfolg"
        ],
        "material_list": [
            "Barrier-Epoxy-Harz (spezial für Osmose-Behandlung)",
            "Glasfaser-Mesh zum Verstärken (optional)",
            "Gelcoat (neuer, hochqualitativ mit UV-Schutz)",
            "Hygrometer und Holz-Feuchte-Messgerät",
            "Schleifausrüstung, Wärme-Quelle zum Trocknen"
        ],
        "cure_time_days": 10,
        "drying_time_days": 14,
        "quality_criteria": {
            "moisture_content_final_pct": {"max": 2.0},
            "barrier_coat_thickness_mm": {"min": 1.5},
            "no_new_blisters_after_1_year": True,
            "warranty_period_years": 2
        },
        "prevention": [
            "Original Gelcoat von hoher Qualität wählen (dicke, mit UV-Stabilisatoren)",
            "Wasserdichte Rumpf-Oberfläche - keine Risse/Beschädigungen",
            "Gute Belüftung unten (Keel-Ventile, Durchlüftungsöffnungen)",
            "Rumpf regelmäßig auf Wasser-Eindringung prüfen",
            "Häufig trocknen (Boot im Freien lagern, nicht im feuchten Schuppen)"
        ],
        "common_mistakes": [
            "Nur oberflächliche Behandlung - Osmose kehrt zurück",
            "Zu kurze Trocknungszeit - Wasser bleibt in Laminate",
            "Barrier-Coat zu dünn - Wasser dringt später wieder ein",
            "Keine Verbesserung der Belüftung - gleiche Bedingungen entstehen wieder"
        ]
    },

    "impact_damage": {
        "description": "Schlag-Beschädigungen (Kratzer, Dellen, kleine Risse in Laminate)",
        "severity": "Variable - von kosmetisch bis strukturell",
        "procedure_steps": [
            "1. Schadensgebiet bewerten: Nur Oberflächenschaden vs. tiefere Delaminierung",
            "2. Mit Tap-Test Delaminierungs-Grenzen feststellen",
            "3. Oberflächliches Schleifen: Mit 80er-Körnung Gelcoat + oberflächliche Faser entfernen",
            "4. Wenn tiefe Kratzer: Mit 120er nachschleifen in V-Nute-Form",
            "5. Oberflächenrauhung: Mit 200er-Körnung finishing schleifen",
            "6. Wenn Delaminierung: Mit Injektions-Epoxi-Harz unter Druck füllen (siehe delamination_small)",
            "7. Oberflächliche Kratzer: Mit angemischtem Gelcoat füllen",
            "8. Tiefere Kratzer: Mit Epoxy-Spachtelmasse + ggf. kleine Faser-Einlagen füllen",
            "9. Aushärtung 24-48h",
            "10. Oberflächenfinish: Glatt schleifen (80-400er Körnung), polieren"
        ],
        "material_list": [
            "Gelcoat (farbabgestimmt)",
            "Epoxy-Spachtelmasse",
            "Injektions-Epoxi (falls Delaminierung)",
            "Schleifpapier (80, 120, 200, 400er)",
            "Poliercompound",
            "Kleine Glasfaser-Streifen (optional)"
        ],
        "cure_time_hours": 2,
        "quality_criteria": {
            "surface_completeness": "Vollständig gefüllt, keine Lücken",
            "color_match": "Mindestens 90% Original-Farbton",
            "structural_integrity": "Keine erkannten Risse, Delaminierungen"
        },
        "common_mistakes": [
            "Delaminierung übersehen - nur Oberflächenkratzer repariert",
            "Zu tiefes Abschleifen - zu viel Material entfernt",
            "Falsche Spachtelmasse - zu spröde, später rissig",
            "Unzureichende Rauhheit - Gelcoat oder Spachtel haftet nicht"
        ]
    },

    "through_hull_repair": {
        "description": "Lochschaden mit Durchbruch (Wasser-eindringung, strukturelle Integrität betroffen)",
        "severity": "Critical - Boot muss sofort repariert werden",
        "procedure_steps": [
            "1. Leck zunächst temporär abdichten (Tuch + Epoxy-Notfalllösung oder Patch)",
            "2. Wasser absaugen, betroffenes Gebiet trocknen",
            "3. Mit Winkelschleifer ringförmig um Loch aufschleifen (25-50mm Rand, bis Faserschicht sichtbar)",
            "4. Alle beschädigten Faserschichten entfernen (auch innen wenn zugänglich)",
            "5. Mit 120er-Körnung rauh machen",
            "6. Epoxy-Harz auftragen (1-2 Schichten mit Pinsel)",
            "7. Neue Faser-Schichten aufbauen in radialer Form (Loch von innen + außen)",
            "   - Erste Schicht: CSM oder Gewebe (Haftung)",
            "   - Dann: Biax 0°/90°, Biax ±45°, UD 0° in ringförmiger Anordnung",
            "   - Gesamtdicke: Original-Laminate-Dicke + 50%",
            "8. Mit Vakuum-Bag verdichten (essentiell)",
            "9. Aushärtung 24-48h",
            "10. Oberflächenfinish: Gelcoat neu aufbringen, schleifen und polieren"
        ],
        "material_list": [
            "Epoxy-Harz (bulk, für Reparatur-Größe ausreichend)",
            "Verschiedene Glasfaser-Typen (CSM, Gewebe, Biax, UD)",
            "Vakuum-Bag-System (essentiell)",
            "Winkelschleifer, Schleifpapier",
            "Wälzen/Bürsten für Laminierung",
            "Gelcoat"
        ],
        "cure_time_hours": 48,
        "quality_criteria": {
            "watertightness": "0% Wasserfluss bei Druck-Test (5kpa)",
            "structural_strength_recovery_pct": 110,
            "no_delamination_visible": True,
            "visual_finish_match": "Gut - akzeptabel für Reparatur"
        },
        "common_mistakes": [
            "Nicht alle beschädigten Fasern entfernt - Reparatur schwach",
            "Zu wenig neue Faser-Schichten - nicht stabil",
            "Vakuum nicht gehalten - Blasen und Porengehalt zu hoch",
            "Gelcoat nicht vollständig - Wasser-Eindringung möglich"
        ]
    },

    "core_rot_repair": {
        "description": "Behandlung von verrottetem Kern-Material in Sandwich-Struktur",
        "severity": "Major - strukturelle Stabilität betroffen",
        "procedure_steps": [
            "1. Diagnose: Mit Schlag-Hammer / Tap-Test faulen Kern lokalisieren",
            "2. Mit Infrarot-Thermografie oder Röntgen Ausmaß der Zerstörung prüfen",
            "3. Mit Winkelschleifer rechteckiges Reparatur-Feld ausschneiden (50mm Sicherheits-Rand um Fäulnis)",
            "4. Obere Faserschale wegschleifen (bis Kern sichtbar)",
            "5. Faulen Kern-Material komplett ausräumen (mit Flachmeißel oder Schleifer)",
            "6. Innenflächen glatt schleifen, Staub absaugen",
            "7. Neues Kern-Material zuschneiden (identisches Material - PVC, Balsa, etc.)",
            "8. Kern-Oberfläche mit Epoxy-Klebstoff versehen",
            "9. Neuen Kern einsetzen (mit Holzkeilen Druckverteilung)",
            "10. Epoxy überschüssig abwischen",
            "11. Aushärtung 24h unter Druck halten",
            "12. Oberfläche rauh machen (80-120er Körnung)",
            "13. Neue Faserschicht aufbauen (mindestens 2 Schichten CSM/Gewebe für Haftung, dann Original-Aufbau)",
            "14. Mit Vakuum-Bag verdichten",
            "15. Aushärtung 24-48h",
            "16. Oberflächenfinish: Gelcoat auftragen, schleifen, polieren"
        ],
        "material_list": [
            "Neues Kern-Material (PVC-Schaumstoff, Balsa, etc. - identisch zu Original)",
            "Epoxy-Klebstoff (für Kern-Bonding)",
            "Glasfaser-Schichten (CSM, Gewebe, Biax - nach Original-Plan)",
            "Epoxy-Harz (bulk)",
            "Vakuum-Bag-System",
            "Holzkeile für Druckverteilung",
            "Schleifausrüstung",
            "Gelcoat"
        ],
        "cure_time_days": 3,
        "quality_criteria": {
            "new_core_bond_strength_mpa": {"min": 5.0},
            "fiber_to_core_adhesion": "Vollständig, keine Delaminierung",
            "structural_stiffness_recovery_pct": 100,
            "no_water_ingress_after_6_months": True
        },
        "prevention": [
            "Original Sandwich-Struktur mit gutem Edge-Closeout (Wasser-Schutz)",
            "Belüftung unter Deck/Kabine (verhindert Kondensation auf Kern)",
            "Regelmäßige Inspektionen auf Wasser-Flecken",
            "Sofortige Reparatur von Rissen / Beschädigungen in Außenschale",
            "Drainage-Öffnungen in kritischen Zonen (z.B. Kajüteneingänge)"
        ],
        "common_mistakes": [
            "Faulen Kern nicht vollständig entfernt - Fäulnis breitet sich aus",
            "Neuer Kern nicht gut geklebt - später wieder Delaminierung",
            "Keine Belüftungs-Verbesserung - gleiche Feuchte-Bedingungen entstehen",
            "Zu dünn neue Faserschichten - strukturelle Schwachstelle"
        ]
    }
}

# ============================================================================
# 7. QUALITY ASSESSMENT FUNCTION
# ============================================================================

def assess_laminate_quality(technique, fiber_type, resin_system, yacht_zone):
    """
    Bewertungsfunktion für Laminat-Qualität basierend auf Prozess-Parametern.

    Args:
        technique (str): Name der Laminations-Technik (z.B. "hand_layup_polyester")
        fiber_type (str): Faser-Typ (z.B. "e_glass_woven")
        resin_system (str): Harz-System (z.B. "polyester_ortho")
        yacht_zone (str): Rumpf-Zone (z.B. "hull_below_waterline_cruiser")

    Returns:
        dict: {
            "overall_score": 0-100,
            "quality_rating": "excellent"/"good"/"acceptable"/"poor",
            "findings": [list of observations],
            "strengths": [list of strong points],
            "weaknesses": [list of concerns],
            "recommended_actions": [list of improvements]
        }
    """

    score = 50  # Starting score
    findings = []
    strengths = []
    weaknesses = []
    recommended_actions = []

    # Validate inputs
    if technique not in LAMINATION_TECHNIQUES:
        return {"error": f"Unknown lamination technique: {technique}"}

    if fiber_type not in FIBER_TYPES:
        return {"error": f"Unknown fiber type: {fiber_type}"}

    if resin_system not in RESIN_SYSTEMS:
        return {"error": f"Unknown resin system: {resin_system}"}

    if yacht_zone not in LAMINATE_SCHEDULES:
        return {"error": f"Unknown yacht zone: {yacht_zone}"}

    tech_data = LAMINATION_TECHNIQUES[technique]
    fiber_data = FIBER_TYPES[fiber_type]
    resin_data = RESIN_SYSTEMS[resin_system]
    zone_data = LAMINATE_SCHEDULES[yacht_zone]

    # 1. Technique appropriateness for yacht zone
    if yacht_zone in tech_data["suitable_for"]:
        score += 10
        strengths.append(f"Technique '{technique}' is well-suited for zone '{yacht_zone}'")
    else:
        score -= 15
        weaknesses.append(f"Technique '{technique}' is NOT typically used for '{yacht_zone}'")
        recommended_actions.append(f"Consider alternative technique from: {tech_data['suitable_for']}")

    # 2. Fiber type suitability for resin
    if resin_system in fiber_data["suitable_resin_systems"]:
        score += 8
        strengths.append(f"Fiber '{fiber_type}' is compatible with resin '{resin_system}'")
    else:
        score -= 20
        weaknesses.append(f"Fiber '{fiber_type}' is NOT compatible with resin '{resin_system}'")
        recommended_actions.append(f"Choose compatible resin: {fiber_data['suitable_resin_systems'][0]}")

    # 3. Reproducibility assessment
    reproducibility = tech_data["reproducibility_rating"]
    if reproducibility >= 4.0:
        score += 12
        strengths.append(f"High reproducibility rating ({reproducibility}/5.0) ensures consistent quality")
    elif reproducibility >= 3.0:
        score += 5
        findings.append(f"Moderate reproducibility ({reproducibility}/5.0) - quality control important")
    else:
        score -= 10
        weaknesses.append(f"Low reproducibility ({reproducibility}/5.0) - challenging for consistent results")
        recommended_actions.append("Implement strict quality control procedures and skilled technician training")

    # 4. Cost efficiency
    tech_cost = tech_data["cost_rating"]
    resin_cost = resin_data["cost_per_kg_usd"]
    if tech_cost <= 2.0 and resin_cost <= 3.0:
        score += 5
        strengths.append("Cost-effective process and materials")
    elif tech_cost > 4.0 or resin_cost > 8.0:
        findings.append("Premium technique/materials chosen - cost higher but quality potential enhanced")

    # 5. Fiber volume % achievement
    expected_fiber_vol = (tech_data["fiber_volume_pct"]["min"] + tech_data["fiber_volume_pct"]["max"]) / 2
    zone_fiber_vol = 32  # typical cruise laminate
    if abs(expected_fiber_vol - zone_fiber_vol) < 5:
        score += 8
        strengths.append(f"Expected fiber volume (~{expected_fiber_vol:.0f}%) aligned with zone requirements")
    elif expected_fiber_vol > zone_fiber_vol:
        score += 10
        strengths.append(f"Technique yields higher fiber volume ({expected_fiber_vol:.0f}%) - increased strength")
    else:
        score -= 5
        weaknesses.append(f"Technique yields lower fiber volume ({expected_fiber_vol:.0f}%) - monitor void content")

    # 6. Void content management
    target_void = tech_data["void_content_pct"]["target"]
    if target_void <= 1.0:
        score += 12
        strengths.append(f"Excellent void control (target {target_void}%) - high quality assured")
    elif target_void <= 3.0:
        score += 6
        findings.append(f"Good void control (target {target_void}%) - standard industry practice")
    else:
        score -= 8
        weaknesses.append(f"High void content (target {target_void}%) - quality risks")
        recommended_actions.append("Implement vacuum bagging or pressure application to reduce voids")

    # 7. Strength rating vs. zone requirements
    technique_strength = tech_data["strength_rating"]["tensile_mpa"]
    zone_strength = zone_data["tensile_strength_mpa"]
    strength_ratio = technique_strength / zone_strength

    if strength_ratio >= 1.5:
        score += 15
        strengths.append(f"Technique provides {strength_ratio:.1f}x required strength - high safety margin")
    elif strength_ratio >= 1.0:
        score += 8
        strengths.append(f"Technique meets strength requirement ({strength_ratio:.1f}x ratio)")
    elif strength_ratio >= 0.8:
        score -= 5
        findings.append(f"Strength barely adequate ({strength_ratio:.1f}x ratio) - limited margin")
    else:
        score -= 20
        weaknesses.append(f"Technique insufficient for zone (only {strength_ratio:.1f}x required strength)")
        recommended_actions.append("Select higher-performance technique or additional laminate plies")

    # 8. Environmental control requirements
    env_score = 0
    if tech_data["environmental_requirements"]["temperature_c"] >= 20:
        env_score += 5
    else:
        env_score -= 3

    if tech_data["environmental_requirements"]["humidity_pct_max"] >= 70:
        env_score += 5
    else:
        env_score -= 3
        weaknesses.append("Low humidity requirement (<70%) - challenging in shipyard")
        recommended_actions.append("Consider climatic control or technique adjustment")

    score += env_score

    # 9. Cure schedule complexity
    cure_schedule = tech_data.get("cure_schedule", {})
    if "room_temperature_20c" in cure_schedule:
        room_temp_hours = cure_schedule["room_temperature_20c"].get("full_cure_hours", 24)
        if room_temp_hours <= 24:
            score += 5
            strengths.append("Fast cure schedule - quick production cycle")
        elif room_temp_hours > 168:
            weaknesses.append("Very slow cure (>7 days) - production impact")
            recommended_actions.append("Plan extended cure schedule or use post-cure heating")

    # 10. Repairability
    repairable_systems = ["hand_layup_polyester", "hand_layup_vinylester", "hand_layup_epoxy"]
    if technique in repairable_systems:
        score += 8
        strengths.append("Technique is easily repairable in field conditions")
    else:
        findings.append("Technique requires specialized equipment/expertise for repairs")

    # Final score bounds
    score = max(0, min(100, score))

    # Determine quality rating
    if score >= 85:
        rating = "excellent"
    elif score >= 70:
        rating = "good"
    elif score >= 50:
        rating = "acceptable"
    else:
        rating = "poor"

    # Compile findings summary
    findings.append(f"Overall assessment: {rating.upper()} quality achievable with '{technique}'")
    findings.append(f"Zone: {yacht_zone}")
    findings.append(f"Expected tensile strength: {technique_strength}MPa (required: {zone_strength}MPa)")

    return {
        "overall_score": score,
        "quality_rating": rating,
        "technique": technique,
        "fiber_type": fiber_type,
        "resin_system": resin_system,
        "yacht_zone": yacht_zone,
        "findings": findings,
        "strengths": strengths,
        "weaknesses": weaknesses,
        "recommended_actions": recommended_actions,
        "expected_properties": {
            "tensile_strength_mpa": technique_strength,
            "flexural_strength_mpa": tech_data["strength_rating"]["flexural_mpa"],
            "shear_strength_mpa": tech_data["strength_rating"]["shear_mpa"],
            "fiber_volume_pct_expected": (tech_data["fiber_volume_pct"]["min"] + tech_data["fiber_volume_pct"]["max"]) / 2,
            "void_content_pct_target": target_void,
            "cure_time_hours": cure_schedule.get("room_temperature_20c", {}).get("full_cure_hours", "N/A")
        }
    }

