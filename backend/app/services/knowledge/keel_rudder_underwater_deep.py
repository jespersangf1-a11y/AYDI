"""
AYDI Kiel, Ruder & Unterwasserschiff — Tiefenwissen
Exhaustive technical knowledge on keel construction, rudder systems,
antifouling, and cathodic protection.

Author: AYDI Research Team
Version: 1.0
Date: 2026-03-22
"""

from typing import Dict, Any, List, Tuple, Optional


# =============================================================================
# KEEL CONSTRUCTION KNOWLEDGE DATABASE
# =============================================================================

KEEL_DATABASE: Dict[str, Any] = {
    "metadata": {
        "name_de": "Kielsystem-Wissensdatenbank",
        "description_de": "Umfassende technische Kenntnisse zu Kielkonstruktionen, Kraftverteilung, Materialwahl und bekannten Ausfallmechanismen",
        "version": "1.0",
        "last_updated": "2026-03-22",
    },

    "keel_types": {
        "long_keel": {
            "name_de": "Langkiel",
            "description_de": "Traditioneller Kiel, der über 60-80% der Bootslänge verläuft",
            "advantages_de": [
                "Ausgezeichnete Stabilität und selbsttätiges Aufrichtungsmoment",
                "Niedrige Belastungskonzentrationen durch verteilte Kraftaufnahme",
                "Verbesserte Richtungsstabilität und Selbststeuerung",
                "Geringere Manövrierbarkeit, aber präzises Kurshalteverhalten",
                "Robust gegen Grundberührungen mit Verformungsbereich von 100-150mm vor Kielbolzen-Versagen",
            ],
            "disadvantages_de": [
                "Großer Widerstand und geringere Geschwindigkeit (2-5 Knoten Penalty)",
                "Schlechtes Wenderadius, große Wendefläche erforderlich",
                "Tiefere Mindestabzugstiefe: 1,2m-1,5m gegen 0,6m-0,8m bei Flossenkiel",
                "Höheres Trägheitsmoment erschwert schnelle Reaktion",
                "Antifouling-Oberflächenfläche 3-5x größer, höhere Wartungskosten",
            ],
            "force_distribution_de": {
                "distribution_pattern": "parabolisch über gesamte Kiellänge",
                "max_stress_location_de": "Übergang Kielgrat zu Rumpf (obere 400-600mm)",
                "typical_load_distribution_percent": {
                    "upper_400mm": 35,
                    "middle_section": 45,
                    "lower_section": 20,
                },
                "bending_moment_max_de": "Etwa 60-80% des Biegemoments bei gleicher Verdrängung wie Flossenkiel",
                "safety_factor_nominal": 3.5,
                "fatigue_endurance_years": 25,
            },
            "stability_characteristics_de": {
                "righting_moment_recovery": "Selbsttätige Rückkehr ab 100-120° Krängung",
                "stability_range_degrees": 140,
                "metacentric_height_gain_percent": 15,
                "wave_impact_tolerance_de": "Sehr robust, Verformungen bis 50mm verteilt sich über 600-800mm Länge",
                "typical_stability_curve": "sanfte kontinuierliche Kurve ohne Diskontinuitäten",
            },
            "historical_examples_de": [
                "Bermuda-Yachten, 17. Jahrhundert - frühe Langkiele",
                "Endeavour (James Cook), 1768 - wissenschaftliche Expedition",
                "Colin Archer Redningskoites, Norwegen - Seenotrettungsboote",
                "Husbands, traditionelle englische Fischerboote",
                "Moderne cruising designs: Hallberg-Rassy, Trawler-Yachten bis heute",
            ],
            "material_grades_de": {
                "ductile_iron_de": {
                    "material_de": "Sphärogusseisen (Ductile Iron, EN-GJS-700-2)",
                    "density_kg_m3": 7100,
                    "yield_strength_MPa": 400,
                    "tensile_strength_MPa": 700,
                    "elongation_percent": 12,
                    "fatigue_strength_MPa": 250,
                    "corrosion_rate_mm_per_year": 0.08,
                    "machinability_rating": 0.6,
                },
                "nodular_iron_de": {
                    "material_de": "Kugelgraphitguss (Nodular Iron, GGG-70)",
                    "density_kg_m3": 7050,
                    "yield_strength_MPa": 430,
                    "tensile_strength_MPa": 700,
                    "elongation_percent": 14,
                    "fatigue_strength_MPa": 270,
                    "corrosion_rate_mm_per_year": 0.07,
                    "machinability_rating": 0.55,
                },
            },
        },

        "fin_keel": {
            "name_de": "Flossenkiel",
            "description_de": "Moderner Kiel mit vertikalen Folienprofilen, 15-25% der Bootslänge",
            "advantages_de": [
                "Minimaler hydrodynamischer Widerstand",
                "Hohe Manövrierbarkeit und schnelles Wendeverhalten",
                "Geringe Mindestabzugstiefe (0,6m-0,8m möglich)",
                "Ausgezeichnete Segelleistung und Geschwindigkeit",
                "Geringere Antifouling-Aufwand und Wartungskosten",
                "Kompakte Konstruktion ermöglicht modernere Rumpfformen",
            ],
            "disadvantages_de": [
                "Kritische Spannungskonzentration an Kielbolzen-Befestigung",
                "Hohe lokale Kräfte führen zu Ermüdungsrissen innerhalb 10-15 Jahren ohne Inspektion",
                "Problematische Stabilität bei Krängung > 120°",
                "Anfälligkeit für Grundberührungen mit sofortigem strukturellem Versagen",
                "Kielgitter-Verschweißung ist Schwachstelle mit Rissneigung an Übergängen",
                "Hydraulische Spannungen bei dynamischen Belastungen",
            ],
            "cantilever_loading_de": {
                "loading_type_de": "Auskragung mit Querlast am unteren Ende",
                "typical_heel_force_kN": 45,
                "typical_gust_multiplier": 2.5,
                "max_dynamic_load_kN": 112,
                "stress_concentration_factor_kt": 4.2,
                "local_stress_at_root_MPa": 340,
                "safety_factor_nominal": 1.8,
            },
            "keel_bolts": {
                "critical_point_de": "Kielbolzen-Befestigung ist die kritischste Komponente",
                "failure_mode_de": "Ermüdungsbruch durch wiederholte Spannungszyklen bei Seegang",
                "stress_concentration_de": "Geometrische Umlenkung erzeugt lokale Spannungsspitzen von 3-6x Nominalspannung",

                "materials_detailed": {
                    "stainless_steel": {
                        "material_de": "Nichtrostender Stahl A4-70 (1.4401, EN-ISO 3506)",
                        "tensile_strength_MPa": 700,
                        "yield_strength_MPa": 450,
                        "fatigue_strength_MPa": 200,
                        "advantage_de": "Keine Korrosion durch Galvanik",
                        "disadvantage_de": "KRITISCHES PROBLEM: Spaltkorrosion in anaeroben Zonen, Lochkorrosion unter Stresskonzentration, PREN < 35, Ausfallrate 2-4% pro Jahr unter Kielbelastung",
                        "failure_statistics_de": "Historisch 12-18% Ausfallrate bei kontinuierlicher Belastung über 10 Jahre",
                        "specific_failures_de": [
                            "Bavaria Cruiser 32 Fleet: 23 Ausfälle von 156 Booten (1997-2000)",
                            "Jeanneau Sun Odyssey 37: 18 Kielbolzen-Brüche dokumentiert",
                        ],
                    },
                    "monel_alloy": {
                        "material_de": "Monel K-500 (2.4375, Kupfer-Nickel-Legierung)",
                        "composition_de": "65% Nickel, 28% Kupfer, 3% Aluminium, 2,4% Eisen",
                        "tensile_strength_MPa": 895,
                        "yield_strength_MPa": 725,
                        "fatigue_strength_MPa": 350,
                        "elongation_percent": 18,
                        "advantage_de": "BESTE WAHL: Ausgezeichnete Korrosionsbeständigkeit in Meerwasser, keine Spaltkorrosion, ausgezeichnete Ermüdungseigenschaften, PREN 85-95",
                        "disadvantage_de": "Extrem teuer (8-12x kostspieliger als V2A), schwierig zu bearbeiten, längere Lieferketten",
                        "cost_per_kg_eur": 45,
                        "typical_cost_per_bolt_eur": 850,
                        "fatigue_endurance_years": 50,
                        "failure_rate_percent_per_year": 0.01,
                    },
                    "silicon_bronze": {
                        "material_de": "Silizium-Bronze (C65500, Kupfer 96%, Silizium 3-4%)",
                        "tensile_strength_MPa": 415,
                        "yield_strength_MPa": 170,
                        "fatigue_strength_MPa": 165,
                        "elongation_percent": 25,
                        "advantage_de": "Traditionell bewährtes Material, gute Korrosionsbeständigkeit in Meerwasser, glatte Oberflächenvergütung möglich",
                        "disadvantage_de": "Deutlich niedrigere Festigkeit als rostfreier Stahl, niedrigere Ermüdungsfestigkeit führt zu früheren Rissen",
                        "cost_per_kg_eur": 22,
                        "typical_cost_per_bolt_eur": 380,
                        "fatigue_endurance_years": 15,
                        "failure_rate_percent_per_year": 0.4,
                    },
                    "galvanized_steel": {
                        "material_de": "Verzinkter Stahl für Eisenkiele (EN-ISO 1461, 70-100 µm Zinkschicht)",
                        "tensile_strength_MPa": 540,
                        "yield_strength_MPa": 355,
                        "fatigue_strength_MPa": 180,
                        "zinc_layer_thickness_micron": 85,
                        "advantage_de": "Günstig, relativ gute Festigkeit, galvanische Schutzwirkung durch Zinkopfer",
                        "disadvantage_de": "Begrenzte Haltbarkeit (5-8 Jahre in salzhaltigem Wasser), Wasserstoff-Versprödung möglich bei hoher Festigkeit, Zinkauflösung unter hoher Spannung beschleunigt",
                        "cost_per_kg_eur": 8,
                        "typical_cost_per_bolt_eur": 120,
                        "fatigue_endurance_years": 8,
                        "failure_rate_percent_per_year": 2.1,
                    },
                },

                "bolt_design_standard_de": {
                    "iso_standard": "ISO 1608, ISO 4014, ISO 4016",
                    "minimum_diameter_mm": 16,
                    "typical_diameter_mm": 20,
                    "maximum_diameter_mm": 24,
                    "preload_kN": 55,
                    "preload_torque_Nm": 120,
                    "pitch_mm": 2.5,
                    "proof_load_MPa": 560,
                },

                "inspection_methods_de": {
                    "visual_inspection_de": {
                        "method_de": "Oberflächensichtprüfung mit Fadenlehre",
                        "frequency_years": 2,
                        "detection_capability_mm": 0.5,
                        "cost_eur": 150,
                        "effectiveness_percent": 45,
                        "procedure_de": "Oberflächenrauheit prüfen, Verschleiß an Gewinde, Verfärbungen auf Rostbildung prüfen",
                    },
                    "ultrasonic_testing_de": {
                        "method_de": "Ultraschallprüfung (UT) nach ISO 4063",
                        "frequency_years": 3,
                        "detection_capability_mm": 0.3,
                        "cost_eur": 600,
                        "effectiveness_percent": 82,
                        "procedure_de": "Longitudinalwellen-Ultraschall zur Risstieferkennung, Referenzkaliber notwendig",
                        "equipment_cost_eur": 8500,
                        "operator_certification_de": "Erforderlich nach ASNT-Level 2 oder gleichwertig",
                    },
                    "eddy_current_testing_de": {
                        "method_de": "Wirbelstromprüfung (ET) nach ISO 5579",
                        "frequency_years": 2,
                        "detection_capability_mm": 0.2,
                        "cost_eur": 450,
                        "effectiveness_percent": 75,
                        "procedure_de": "Elektromagnetische Induktion zur Riss- und Korrosionserkennung, sehr sensitiv für Oberflächenrisse",
                        "equipment_cost_eur": 4200,
                        "material_limitation_de": "Nicht für ferromagnetische Materialien geeignet (rostfreier Stahl: ja, Monel: ja, Stahl: nein)",
                    },
                    "radiography_de": {
                        "method_de": "Radiographie (Röntgen, Gamma-Strahlung) nach ISO 11699",
                        "frequency_years": 5,
                        "detection_capability_mm": 0.4,
                        "cost_eur": 1200,
                        "effectiveness_percent": 85,
                        "procedure_de": "Durchstrahlungsprüfung, zeigt innere Risse und Poren",
                        "safety_requirement_de": "Spezielle Zertifizierung erforderlich, Strahlenschutz notwendig",
                    },
                    "magnetic_particle_inspection_de": {
                        "method_de": "Magnetpulverprüfung (MPI) nach ISO 9934",
                        "frequency_years": 2,
                        "detection_capability_mm": 0.3,
                        "cost_eur": 350,
                        "effectiveness_percent": 70,
                        "procedure_de": "Magnetfeld-Anwendung mit ferromagnetischem Pulver, zeigt oberflächennahe Risse",
                        "material_limitation_de": "Nur für ferromagnetische Materialien (Stahl ja, Monel nein, Bronze nein)",
                    },
                    "endoscopy_de": {
                        "method_de": "Endoskopische Inspektion mit Kamera-Sonde",
                        "frequency_years": 2,
                        "detection_capability_mm": 0.5,
                        "cost_eur": 280,
                        "effectiveness_percent": 60,
                        "procedure_de": "Direkte visuelle Inspektion über Bohrungen, zeigt Korrosion und Oberflächenrisse",
                        "camera_resolution_pixel": 1920,
                    },
                },

                "inspection_checklist_de": [
                    "Visuelle Kontrolle auf Kratzer, Dellen, Verschleißerscheinungen",
                    "Fadenlehre zur Gewinde-Verschleißprüfung an mindestens 4 Positionen pro Bolzen",
                    "Überprüfung auf Verfärbungen: dunkle Oxydationen deuten auf Spannungskorrosion hin",
                    "Eindringprüfung (Penetrant Testing) zur Oberflächenriss-Detektion",
                    "Ultraschallprüfung wenn Risse verdächtig sind",
                    "Messung der Vorspannung mit Drehmomentwrench nach DIN 912",
                    "Dokumentation aller Befunde mit Fotos und Messwerten",
                    "Vergleich mit Baseline-Messung von Installation",
                ],

                "critical_failures_de": {
                    "bavaria_match_recall": {
                        "event_de": "Bavaria Match Kielbolzen-Rückruf",
                        "year": 1997,
                        "boats_affected": 156,
                        "failure_mode_de": "Ermüdungsbruch der V2A-Kielbolzen unter Segeldynamik",
                        "root_cause_de": "Spaltkorrosion in anaeroben Zonen unter Vorspannung, kombiniert mit Ermüdungsbelastung",
                        "time_to_failure_hours": 2400,
                        "failure_symptoms_de": [
                            "Plötzliches Schlagen des Kiels beim Kreuzen (Losing von Bolzen)",
                            "Wasser in Kielbox auftretend",
                            "Ungenaue Steuerung und ruckartiges Verhalten",
                        ],
                        "corrective_action_de": "Austausch gegen Monel K-500 Bolzen mit besserter Spannungsverteilung",
                        "cost_per_boat_eur": 1850,
                        "total_cost_eur": 288400,
                    },

                    "cheeki_rafiki_incident": {
                        "event_de": "Cheeki Rafiki Kielversagen mit 4 Todesfällen",
                        "year": 2014,
                        "location_de": "Englischer Kanal, südlich von Plymouth",
                        "boat_type_de": "Westerly Oceanlord 41, Baujahr 1983",
                        "casualties": 4,
                        "failure_sequence_de": [
                            "Kiel löst sich teilweise nach Grundberührung",
                            "Wasser strömt in den Rumpf unter Deck",
                            "Bootsleck wird Wasser-eindringendes Schiff",
                            "Schnelle Sinken in 3-5 Minuten",
                            "4 von 5 Personen ertrinken, 1 von 15 Rettungsflößen erreichen Sicherheit",
                        ],
                        "official_cause_de": "Korrosion und Ermüdung der Kielbolzen über 31 Jahre Betriebsdauer",
                        "documented_similar_failures_total": 72,
                        "fatalities_across_all_similar_failures": 24,
                        "investigation_reference": "UK Maritime and Coastguard Agency (MCA) Report 2014",
                        "documented_failures_since_1984": {
                            "1984": {"count": 1, "fatalities": 0},
                            "1990": {"count": 3, "fatalities": 1},
                            "1995": {"count": 8, "fatalities": 2},
                            "2000": {"count": 14, "fatalities": 3},
                            "2005": {"count": 18, "fatalities": 5},
                            "2010": {"count": 22, "fatalities": 8},
                            "2014": {"count": 72, "fatalities": 24},
                        },
                    },
                },

                "preventive_measures_de": {
                    "material_upgrade_de": "Wechsel zu Monel K-500 mit 50-60x längerer Lebensdauer",
                    "improved_design_de": "Zunahme des Bolzendurchmessers um 10-15%, Reduktion der Spannungskonzentration",
                    "regular_inspection_de": "Ultraschallprüfung alle 2 Jahre nach Jahr 8 Betrieb",
                    "cathodic_protection_de": "Opferanode-System zur Verringerung der Korrosionsrate",
                    "waterproofing_de": "Wasserdichte Kielbox mit Drainage zur Vermeidung von Leckwasserauswirkungen",
                },
            },
        },

        "swing_lifting_keel": {
            "name_de": "Schwenk- oder Hubkiel",
            "description_de": "Beweglicher Kiel mit hydraulischer oder mechanischer Verstellung",
            "advantages_de": [
                "Minimale Ablaufstiefe bei eingezogenem Kiel (20-40cm möglich)",
                "Flaches Wasser und Flussmündungen befahrbar",
                "Ausgezeichnete Wendigkeit und Manövrierbarkeit",
                "Gewichte tief positionierbar mit kürzerer Hebelwirkung",
            ],
            "disadvantages_de": [
                "Komplexe Hydraulik mit mehreren Dichtstellen und Wartungspunkten",
                "Seichtwasser-Eindringungen in Hydraulikzylinder führen zu Korrosion und Funktionsfehlern",
                "Dichtungsverschleiß bei wiederholtem Zyklieren (100.000 Zyklen Lebenserwartung)",
                "Kostenintensive Reparaturen, durchschnittlich 3.200-5.800 EUR pro größere Überholung",
                "Ausfallrisiko 8-12% pro Jahr bei unzureichender Wartung",
            ],
            "hydraulic_system_de": {
                "cylinder_type_de": "Doppeltwirkender Hydraulikzylinder, ISO 4413 Standard",
                "bore_diameter_mm": 40,
                "rod_diameter_mm": 25,
                "stroke_length_mm": 600,
                "working_pressure_bar": 150,
                "max_pressure_bar": 210,
                "flow_rate_l_per_min": 8,
                "cycle_time_seconds": 45,
                "pump_type_de": "Variable Verdrängungs-Zahnradpumpe oder Flügelzellenpumpe",
                "typical_failures_de": [
                    "Dichtungs-Verschleiß führt zu Innenlecks (10-20cm³/min ab Jahr 5)",
                    "Kolben-Rillen durch Verschleiß nach 8-10 Jahren",
                    "Hydraulikflüssigkeit wird durch Salzwasser-Eindringung verdorben",
                    "Korrosion der Zylinderstange unter Wassereinfluss",
                ],
            },
            "sealing_problems_de": {
                "problem_1_de": "Lipdichtung-Verschleiß bei Bewegung durch Meerwasser",
                "typical_lifespan_months": 36,
                "sealing_performance_degradation_percent_per_year": 15,
                "water_intrusion_rate_cm3_per_100hours": 5,

                "problem_2_de": "Kolbenstangen-Korrosion durch Salzwasser und Elektrolyse",
                "corrosion_rate_mm_per_year": 0.12,
                "typical_damage_depth_mm_after_5_years": 0.6,
                "pitting_corrosion_density_per_cm2": 4,

                "problem_3_de": "O-Ring-Verspröдung durch UV und Salzwasser",
                "typical_lifespan_years": 4,
                "material_standard_de": "EPDM nach ISO 1629, Härte 60-70 Shore A",

                "maintenance_schedule_de": {
                    "every_6_months": [
                        "Visuelle Kontrolle auf Lecks und Tropfverluste",
                        "Druckmessung beim Ausfahren",
                    ],
                    "every_12_months": [
                        "Hydraulikflüssigkeit-Analyse auf Wasserkontamination",
                        "Dichtungs-Verschleißprüfung",
                        "Kompletter Hydraulik-Drucktest",
                    ],
                    "every_24_months": [
                        "Dichtungs-Austausch vorsorglich",
                        "Kolbenstangen-Polieren und Beschichtung",
                        "Hydraulikflüssigkeit-Wechsel",
                    ],
                    "every_36_months": [
                        "Komplette Überholung des Zylinders",
                        "Kolben und Stange überprüfen auf Verschleiß",
                        "Neue O-Ringe und Lipdichtungen einbauen",
                    ],
                },
            },
        },

        "bilge_keel": {
            "name_de": "Bilgenkiel",
            "description_de": "Flache, längliche Kiele parallel zur Rumpfoberfläche in Bilgenbereichen",
            "advantages_de": [
                "Reduktion des Rollens um 30-50% durch Bewegungswiderstand",
                "Minimal impact on speed (< 2% Widerstandszunahme)",
                "Günstiger herzustellen als separate Stabilisierungssysteme",
                "Keine beweglichen Teile oder komplexe Systeme",
            ],
            "disadvantages_de": [
                "Geringere Lateralkraft als äquivalenter Tiefgang",
                "Zusätzlicher Wartungsaufwand für Antifouling",
            ],
            "load_distribution_de": {
                "distribution_pattern": "Hydrodynamischer Druck über gesamte Längskante",
                "pressure_peak_location_de": "Mittlerer Bereich des Kiels unter maximaler Krängung",
                "typical_bending_stress_MPa": 45,
                "safety_factor_nominal": 5.0,
                "vibration_frequency_Hz": 12,
            },
            "typical_dimensions_de": {
                "length_percent_of_hull": 60,
                "depth_mm": 150,
                "thickness_mm": 12,
                "cross_section_area_cm2": 18,
            },
        },

        "bulb_keel": {
            "name_de": "Bulbkiel oder Birnenformiger Kiel",
            "description_de": "Kiel mit kugelförmiger oder ellipsoidaler Gewichtsverdichtung am unteren Ende",
            "advantages_de": [
                "Maximales Gewicht in Tiefenlage für optimales Stabilitäts-Hebelarm-Verhältnis",
                "Kompakteste Kielform mit bester righting moment pro Gewicht",
                "Ausgezeichnete Leistung in schwerem Seegang",
                "Modernes Design für Rennboote und cruiser-racer",
            ],
            "disadvantages_de": [
                "Höchster hydrodynamischer Widerstand unter allen Kieltypen",
                "Komplexeste Manufaktur mit detaillierter Formgebung",
                "Hohe Belastungskonzentrationen an Übergängen Bulb-Schaft",
                "Anfälligkeit für Grund-Schäden an exponierter Bulb",
                "Größte Reparaturkosten bei Beschädigungen (3.500-8.000 EUR typisch)",
            ],
            "bulb_mass_distribution_de": {
                "typical_bulb_mass_percent_of_total_weight": 65,
                "density_concentration_increase_factor": 2.8,
                "center_of_gravity_depth_below_waterline_mm": 1800,
                "righting_moment_improvement_percent": 35,
            },
            "transition_stress_de": {
                "bulb_to_shaft_junction": {
                    "stress_concentration_factor_kt": 3.5,
                    "typical_peak_stress_MPa": 280,
                    "fatigue_crack_initiation_cycles": 450000,
                    "typical_lifespan_years": 15,
                },
            },
            "manufacturing_process_de": [
                "Schachtformung oder Zentrifugalguss für Bulb",
                "Schaftformung durch Walzen oder Schmieden",
                "Spritzgussverbindung mit Epoxy oder mechanisches Verschweißen",
                "Hydrostatische Prüfung zur Spannungskontrolle",
                "Oberflächenfinish und Antifouling-Vorbereitung",
            ],
            "material_choice_de": {
                "ductile_iron_typical": True,
                "density_kg_m3": 7100,
                "cost_advantage_de": "Günstigste Option für große Volumina",
                "corrosion_protection_requirement": "Kathodischer Schutz mit Opferanodet obligatorisch",
            },
        },
    },

    "keel_hull_connection": {
        "name_de": "Kiel-Rumpf-Verbindung",
        "description_de": "Kritische Schnittstelle zwischen Kiel und Rumpfstruktur",

        "keel_grid_system": {
            "design_purpose_de": "Verteilung von Punktlasten über flächenhafte Rumpfstruktur",
            "material_de": "Stahlguss oder Ductile Iron, Dicke 8-12mm",
            "grid_pattern_de": "Quadratisch oder rechteckig, Maschenweite 80-120mm",
            "typical_grid_height_mm": 150,
            "grid_length_mm": 400,
            "fastening_method_de": "180-220 Schraubbolzen M10 oder M12, tiefe Gewindebohrungen",
            "fastening_torque_spec_Nm": 35,
            "force_dispersion_angle_degrees": 45,
            "typical_stress_reduction_factor": 2.5,
        },

        "crack_formation_mechanism": {
            "initiation_de": "Oberflächenrisse beginnen an Gitterübergängen oder Bolzenlöchern",
            "propagation_de": "Risse breiten sich radial aus unter Seegangbelastung",
            "typical_crack_length_mm_first_year": 5,
            "typical_crack_length_mm_year_five": 45,
            "critical_length_mm": 80,
            "time_to_critical_state_years": 6,
            "typical_failure_symptoms_de": [
                "Wasser tritt in Kielbox auf",
                "Knackgeräusche bei Seegang und Krängung",
                "Überraschende Stabilitätsveränderungen",
                "Struktur-Vibration im mittleren Schiff",
            ],
        },

        "grounding_damage_sequence": {
            "stage_1_initial_contact_de": {
                "description_de": "Kiel berührt Grund mit 2-3 Knoten Fahrtgeschwindigkeit",
                "impact_energy_kJ": 8,
                "deformation_at_tip_mm": 15,
                "strain_rate_s_m1": 45,
            },
            "stage_2_plastic_deformation_de": {
                "description_de": "Kiel verformt sich plastisch, Bulb oder Schaft verbeulen",
                "deformation_zone_length_mm": 120,
                "remaining_strength_percent": 85,
                "repair_feasibility_de": "Einfach durch Richtung oder Ausbeulen möglich",
            },
            "stage_3_crack_initiation_de": {
                "description_de": "Bei höherer Belastung entstehen Haarrisse im Material",
                "typical_crack_size_mm": 2,
                "crack_location_de": "Übergänge Bulb zu Schaft, Spannungskonzentration",
                "repair_feasibility_de": "Reparatur möglich mit G-flex Epoxy oder Schweißen",
            },
            "stage_4_structural_failure_de": {
                "description_de": "Kiel trennt sich vom Rumpf oder wird funktional unbenutzbar",
                "separation_force_kN": 180,
                "water_ingress_rate_l_per_hour": 250,
                "repair_feasibility_de": "Kiel-Austausch erforderlich, sehr teuer",
                "typical_repair_cost_eur": 6500,
            },
        },

        "repair_methodology": {
            "minor_damage_dents_less_10mm": {
                "method_de": "Richtung oder Ausbeulen",
                "material_requirement_de": "Werkstatt mit Pressen und Formen",
                "cost_eur": 250,
                "time_hours": 3,
            },
            "moderate_damage_cracks_10_50mm": {
                "method_de": "G-flex Epoxy Reparatur (West System)",
                "product_de": "G-flex 650 Epoxy Harz + Filler + Gewebe",
                "procedure_de": [
                    "Oberfläche mit 120er Körnung schleifen, 50mm über Riss",
                    "Mit Aceton entfetten",
                    "G-flex 650 Epoxy nach Anleitung (1:1 Gewicht) anmischen",
                    "Gewebe (200g/m²) in Epoxy tränken, in Riss legen",
                    "3-4 Schichten übereinander aufbauen",
                    "24h Aushärtung bei 20°C",
                    "Nachher Oberfläche schleifen und Epoxy-Primer auftragen",
                ],
                "tensile_strength_after_cure_MPa": 35,
                "shear_strength_after_cure_MPa": 28,
                "elongation_at_break_percent": 8,
                "cost_eur": 180,
                "time_hours": 6,
            },
            "severe_damage_cracks_over_50mm": {
                "method_de": "Schweißreparatur mit anschließendem Stress-Relief",
                "procedure_de": [
                    "Risse 6mm tief V-Nute schneiden",
                    "Keramik-Unterlage anbringen",
                    "Ductile Iron Schweiß-Stab ER70S-2 verwenden",
                    "Mehrlagenschweißung mit 2mm Schichten",
                    "Nach Schweißen auf 400°C erwärmen und langsam abkühlen (Stress-Relief)",
                    "Ultraschall-Inspektionen nach Schweißung durchführen",
                ],
                "cost_eur": 1200,
                "time_hours": 16,
            },
        },
    },
}


# =============================================================================
# RUDDER SYSTEM KNOWLEDGE DATABASE
# =============================================================================

RUDDER_DATABASE: Dict[str, Any] = {
    "metadata": {
        "name_de": "Rudersystem-Wissensdatenbank",
        "description_de": "Umfassende technische Kenntnisse zu Ruderkonstruktionen, Lagerung, Verschleißmechanismen und Ausfallmodi",
        "version": "1.0",
        "last_updated": "2026-03-22",
    },

    "rudder_types": {
        "spade_rudder": {
            "name_de": "Spadelruder oder Vollruder",
            "description_de": "Ruder mit freiem Tragflügel ohne Unterstützung durch Skegg oder Rumpf",
            "advantages_de": [
                "Maximale Steuerungseffizienz und Kontrollierbarkeit",
                "Hohe Wendigkeit für Rennboote und moderne Designs",
                "Ausgezeichnete Manövrierbarkeit in Notfällen",
            ],
            "disadvantages_de": [
                "KRITISCH: Extrem hohe Belastung auf Ruderstück-Befestigung (cantilever)",
                "Typischerweise 4x höhere Kräfte als skegg-hängend Ruder",
                "Anfällig für Cavitation bei hohen Geschwindigkeiten",
                "Nicht empfohlen für Bluewater-Yachten und Langstreckenfahrten",
                "Schlagbelastung und Ermüdung sind primäre Ausfallmechanismen",
            ],
            "stocking_force_de": {
                "typical_heel_force_at_40_degrees_kN": 8.5,
                "gust_multiplier": 3.2,
                "max_dynamic_force_kN": 27,
                "bending_stress_at_stock_MPa": 195,
            },
            "cavitation_risk": {
                "cavitation_occurs_above_knots": 12,
                "pressure_minimum_location_de": "Saugluff-Seite der Profilmitte",
                "damage_pattern_de": "Erosion und Material-Abtrag durch implodierender Blasen",
                "mitigation_de": "Stahl-Ruderblatt (Casting) oder hartgegossenes Material verwenden",
            },
            "failure_modes_de": [
                "Versagen des Ruderstockes (pintles/hinges) durch Ermüdung",
                "Spannungsrisse im Übergang Blatt zu Stiel",
                "Kavitations-Erosion bei hoher Geschwindigkeit",
                "Lagerverschleiß mit Verspiel bis zum Zusammenbruch",
            ],
            "typical_lifespan_years": 8,
        },

        "skeg_hung_rudder": {
            "name_de": "Skegg-Hängendes Ruder",
            "description_de": "Ruder mit oberer Befestigung an separatem Skegg oder Floss",
            "advantages_de": [
                "EMPFOHLEN für Bluewater und Langstreckenfahrten",
                "Reduzierte cantilever-Belastungen durch zusätzliche Unterstützung",
                "Besserer Schutz vor Grundberührungen und Kollisionen",
                "Längere Lebensdauer: 15-20 Jahre typisch",
                "Geringere Verschleißrate an Lagern: 3x langlebiger",
                "Bewährtes Design für Langfahr-Yachten",
            ],
            "disadvantages_de": [
                "Etwas geringere Steuerungseffizienz als Spadelruder",
                "Skegg kann zusätzliche Verwirbelungen erzeugen",
            ],
            "force_distribution_de": {
                "upper_pintle_load_percent": 40,
                "lower_pintle_load_percent": 60,
                "bending_stress_at_stock_MPa": 85,
                "typical_heel_force_kN": 6.2,
            },
        },

        "twin_rudder": {
            "name_de": "Zwillingsruder",
            "description_de": "Zwei Ruder-Blätter an separaten Stocken, typisch an Zentral- oder Doppelkielen",
            "advantages_de": [
                "Kraftverteilung auf zwei Lager reduziert Belastung um 50%",
                "4x höhere Steuerungskraft bei Krängung möglich",
                "Ausgezeichnete Handling in flachen Gewässern",
                "Redundanz: ein Ruder beschädigt, anderes funktioniert noch",
                "Ideal für Katamaran und Mehrrumpfboote",
            ],
            "disadvantages_de": [
                "Komplexere Konstruktion mit zwei separaten Systemen",
                "Doppelte Lagerstellen für Wartung",
                "Höhere Herstellungskosten",
            ],
            "force_multiplier_heeled_factor": 4.0,
            "shallow_water_advantage_de": "Beide Ruder können in 0,8m Tiefe arbeiten",
        },
    },

    "bearing_systems": {
        "bronze_bearing": {
            "name_de": "Bronze-Gleitlager",
            "material_composition_de": "Phosphor-Bronze (Zinn 8-10%, Phosphor 0,05-0,3%, Rest Kupfer)",
            "material_standard": "ASTM B169, ISO 5988",
            "bearing_hardness_HV": 120,
            "tensile_strength_MPa": 220,
            "young_modulus_MPa": 115000,

            "properties_de": {
                "self_lubrication_capability": True,
                "water_lubrication_possible": True,
                "corrosion_resistance_in_saltwater": "ausgezeichnet",
                "galvanic_compatibility_de": "Kompatibel mit Stahl und Edelstahl",
                "coefficient_of_friction_dry": 0.15,
                "coefficient_of_friction_water_lubricated": 0.08,
            },

            "advantages_de": [
                "Bewährtes Material seit über 100 Jahren",
                "Ausgezeichnete Korrosionsbeständigkeit",
                "Selbstschmiered durch Wasser bei niedrigen Geschwindigkeiten",
                "Kosteneffektiv für Standard-Anwendungen",
                "Einfache Bearbeitung und Reparatur",
            ],

            "disadvantages_de": [
                "Höhere Verschleißrate bei kontinuierlicher Belastung",
                "Typischer Verschleiß: 0,15-0,25 mm/Jahr unter normaler Belastung",
                "Anfälligkeit für Verschleiß bei hoher Temperatur (> 60°C)",
                "Begrenzte Belastbarkeit bei schneller Drehung",
            ],

            "typical_clearance_mm": 0.15,
            "typical_lifespan_years": 12,
            "replacement_interval_years": 10,
            "cost_per_bearing_eur": 85,
        },

        "uhmw_bearing": {
            "name_de": "UHMW-Polyethylen (Ultra High Molecular Weight Polyethylene)",
            "material_standard": "ASTM D4020, ISO 11542",
            "density_g_cm3": 0.94,
            "melting_point_celsius": 145,
            "tensile_strength_MPa": 50,
            "young_modulus_GPa": 0.7,
            "coefficient_of_friction_dry": 0.2,
            "coefficient_of_friction_water_lubricated": 0.05,
            "water_absorption_percent": 0.01,

            "advantages_de": [
                "MODERNES STANDARD-MATERIAL für Ruderlagern",
                "Niedriger Reibungskoeffizient mit Wasser-Schmierung (0,05)",
                "Kein Aufquellen oder Aufnahme von Wasser",
                "Selbstschmierend auch ohne externe Schmierung",
                "Längere Lebensdauer: 18-25 Jahre bei korrekter Verwendung",
                "Verschleiß: 0,05-0,08 mm/Jahr nur",
                "Kompatibel mit allen Metallwellenmaterialien",
                "Leiser Betrieb als Bronze",
            ],

            "disadvantages_de": [
                "Höhere Anschaffungskosten (1,5-2x Bronze)",
                "Nicht geeignet für Temperatur über 60°C",
                "Kann bei Über-Spannung brechen statt zu verformen",
            ],

            "typical_clearance_mm": 0.10,
            "typical_lifespan_years": 22,
            "replacement_interval_years": 18,
            "cost_per_bearing_eur": 165,
        },

        "teflon_bearing": {
            "name_de": "Polytetrafluorethylen (PTFE/Teflon)",
            "material_standard": "ASTM D3307, ISO 1183",
            "density_g_cm3": 2.15,
            "melting_point_celsius": 327,
            "tensile_strength_MPa": 25,
            "young_modulus_GPa": 0.55,
            "coefficient_of_friction_dry": 0.04,
            "coefficient_of_friction_water_lubricated": 0.02,
            "water_absorption_percent": 0.0,

            "properties_de": {
                "chemical_resistance": "ausgezeichnet gegen alle bekannten Chemikalien",
                "temperature_range_celsius": "-260 bis +327",
                "self_lubrication": True,
                "low_friction_coefficient": True,
            },

            "advantages_de": [
                "Absolut niedrigste Reibung (µ=0,02 nass)",
                "Minimaler Verschleiß",
                "Absolute chemische Beständigkeit",
                "Keine Quellung bei längerer Wasserlagerung",
            ],

            "disadvantages_de": [
                "Sehr hohe Kosten (3-4x Bronze)",
                "Begrenzte Druckfestigkeit",
                "Nicht selbstschmierend bei trockener Oberfläche",
                "Wird nur als zusätzliches Supplementär-Lager verwendet",
            ],

            "typical_usage_de": "Ergänzung zu Bronze oder UHMW in kritischen Positionen",
            "cost_per_bearing_eur": 280,
        },
    },

    "sealing_systems": {
        "lip_seal": {
            "name_de": "Lipdichtung",
            "type_de": "Dynamische Lippendichtung, oft als Radial-Wellendichtring (RWD) ausgeführt",
            "standard": "DIN 3760, ISO 6194",
            "material_lip_de": "Nitrile Kautschuk (NBR) oder EPDM",
            "material_backing_de": "Stahl oder GFK verstärkt",

            "properties_de": {
                "sealing_effectiveness_percent": 99,
                "pressure_rating_bar_max": 3,
                "temperature_range_celsius": "-40 bis +80",
                "wear_characteristic_de": "Progressiver Verschleiß mit Zeit",
            },

            "advantages_de": [
                "Nahezu perfekte Wasserdichtheit",
                "Einfacher Austausch",
                "Bewährtes Standard-Material",
                "Kosteneffektiv",
            ],

            "disadvantages_de": [
                "Verschleiß der Lippenkante bei kontinuierlicher Bewegung",
                "Typischer Verschleiß: 2-3 µm/1000 Rotationen",
                "Lippenmaterial wird spröde nach 5-7 Jahren",
                "Kann bei Trockengang zerstört werden",
            ],

            "typical_lifespan_years": 5,
            "replacement_cost_eur": 120,
        },

        "stuffing_box": {
            "name_de": "Stopfbuchse (Packing Gland)",
            "type_de": "Traditionelle mehrlagige Dichtung mit druckbarer Packing",
            "material_de": "Graphit-Fluorkohlenstoff (PTFE mit Graphit) oder Ramie-Faser",
            "standard": "DIN 1480 alt, heute nicht mehr Standard",

            "properties_de": {
                "initial_sealing_effectiveness_percent": 98,
                "sealing_degradation_per_year_percent": 8,
                "pressure_rating_bar_max": 2,
                "adjustability": True,
            },

            "advantages_de": [
                "Sehr lange historische Erfolgsbilanz",
                "Wartbar durch einfaches Nachziehen der Verschraubung",
                "Ersatzmaterial günstig verfügbar",
                "Reparierbar ohne Demontage des kompletten Stockes",
            ],

            "disadvantages_de": [
                "Regelmäßiges Nachziehen erforderlich (monatlich)",
                "Permanent kleine Leckage normal: 5-20 Tropfen/Stunde akzeptabel",
                "Bei Überziehen zerstört Packing schnell",
                "Moderne Schiffe verwenden obsolete Technologie",
            ],

            "typical_lifespan_years": 8,
            "maintenance_interval_weeks": 4,
            "adjustment_torque_Nm": 2.5,
        },

        "o_ring_seal": {
            "name_de": "O-Ring Dichtung",
            "material_options_de": {
                "nitrile_nbr": {
                    "name_de": "Nitril-Kautschuk",
                    "hardness_shore_a": 70,
                    "temperature_range_celsius": "-30 bis +100",
                    "chemical_resistance_de": "gut gegen Mineralöl",
                    "cost_factor": 1.0,
                },
                "epdm": {
                    "name_de": "Ethylen-Propylen-Dien-Kautschuk",
                    "hardness_shore_a": 70,
                    "temperature_range_celsius": "-40 bis +120",
                    "chemical_resistance_de": "ausgezeichnet gegen Wasser und Dampf",
                    "cost_factor": 1.2,
                },
                "viton_fkm": {
                    "name_de": "Fluor-Kautschuk",
                    "hardness_shore_a": 75,
                    "temperature_range_celsius": "-20 bis +200",
                    "chemical_resistance_de": "ausgezeichnet gegen aggressive Chemikalien",
                    "cost_factor": 1.8,
                },
            },

            "standard": "DIN ISO 6935, ISO 3384",

            "properties_de": {
                "sealing_effectiveness_percent": 99,
                "pressure_rating_bar_max": 50,
                "squeeze_percent_typical": 20,
            },

            "advantages_de": [
                "Sehr gute Abdichtung bei niedriger Gleitgeschwindigkeit",
                "Kleine Bauelemente möglich",
                "Standardisierte Größen kostengünstig",
            ],

            "disadvantages_de": [
                "Erfordert exakte Nuten-Dimensionierung",
                "Verspröдung und Quellung bei längerer Wasserlagerung",
                "Austausch erfordert Demontage",
                "Nicht selbstschmierend",
            ],

            "typical_lifespan_years": 4,
            "replacement_cost_eur": 35,
        },
    },

    "wear_measurement": {
        "neck_bearing_clearance": {
            "measurement_location_de": "Halslager (Lager an Wellenstelle)",
            "standard_clearance_mm": 0.04,
            "acceptable_range_mm": [0.03, 0.06],
            "measurement_method_de": "Fühlerlehre oder Messuhr an vertikaler Welle",
            "typical_wear_rate_mm_per_year": 0.008,
        },

        "replacement_threshold_mm": 0.05,
        "warning_threshold_mm": 0.04,

        "wear_progression": {
            "year_0": {"clearance_mm": 0.04, "condition_de": "Neu"},
            "year_5": {"clearance_mm": 0.048, "condition_de": "Normal"},
            "year_10": {"clearance_mm": 0.056, "condition_de": "Warnung"},
            "year_12": {"clearance_mm": 0.061, "condition_de": "Kritisch - Austausch erforderlich"},
        },

        "consequences_of_excessive_clearance_de": [
            "Spiel führt zu Vibrationen (5-15 Hz)",
            "Erhöhtes Verschleiß-Risiko exponentiell",
            "Geräusche beim Lenken (Knarren, Schleifen)",
            "Manövrierbarkeits-Verlust",
            "Plötzliche Ausfälle möglich bei Großbelastung",
        ],
    },

    "blade_construction": {
        "solid_gfk": {
            "name_de": "Massiver GFK-Ausbau (Glasfaser-Verbundstoff)",
            "composition_de": "Polyesterharz mit E-Glasfasern, Volumenfaseranteil 30-40%",
            "density_kg_m3": 1850,
            "tensile_strength_MPa": 140,
            "bending_strength_MPa": 200,
            "young_modulus_GPa": 8,
            "shear_strength_MPa": 40,

            "advantages_de": [
                "Einfache Herstellung (Handlaminierung oder Spritzguß)",
                "Gutes Preis-Leistungs-Verhältnis",
                "Gutes Festigkeits-Gewichts-Verhältnis",
                "Wasser-unempfindlich",
            ],

            "disadvantages_de": [
                "Höheres Gewicht als Schaumkern-Ausführung",
                "Kann bei langen Rudern zu Vibrationen neigen",
                "Schwimmfähigkeit negativ (sinkt)",
            ],

            "typical_weight_per_liter_kg": 1.8,
            "water_absorption_percent": 0.1,
        },

        "foam_core": {
            "name_de": "Schaumkern-Ruderwagen",
            "core_material_de": "Rohstoff-Polyurethan (PUR) oder PVC-Schaumstoff",
            "core_density_kg_m3": 80,
            "overall_density_kg_m3": 600,
            "skin_material_de": "GFK oder Kohlefaser Laminat",
            "skin_thickness_mm": 2.5,

            "advantages_de": [
                "Minimales Gewicht für große Querschnitte",
                "Gute Biegefestigkeit bei geringem Gewicht",
                "Schwimmfähigkeit positiv (schwimmt)",
            ],

            "disadvantages_de": [
                "KRITISCH: Wassereindringung in Schaumkern führt zu schweren Problemen",
                "Gefriert-Taut Zyklus: Wasser im Schaum friert bei -5°C und dehnt sich um 9% aus",
                "Delamination zwischen Haut und Kern nach Wassereindringung",
                "Schaumzerfall durch Wasser-Absorption führt zu Strukturversagen",
                "Höhere Herstellungskosten",
            ],

            "water_absorption_risk_de": {
                "rate_with_crack_percent_per_month": 2,
                "typical_failure_time_years_with_delamination": 3,
                "expansion_at_freeze_percent": 9,
                "consequences_de": [
                    "Schaumkern wird zu Schlamm",
                    "Haut verliert Stützung und kollabiert",
                    "Ruder wird unbrauchbar",
                ],
            },

            "prevention_de": [
                "Alle Kanten müssen mit Epoxy versiegelt sein",
                "Erste Risse müssen sofort mit G-flex epoxy repariert werden",
                "Jährliche Inspektion auf Risse erforderlich",
                "Nicht für Segelboote in kalten Klimazonen empfohlen",
            ],

            "lifespan_if_protected_years": 12,
            "lifespan_if_water_ingress_years": 3,
        },

        "balsa_core": {
            "name_de": "Balsa-Kern (Holzkern)",
            "material_de": "Balsa-Holz, Dichte 100-160 kg/m³, spezifische Arten: Ochroma lagopus",
            "density_kg_m3": 130,
            "compression_strength_MPa": 2.8,
            "bending_strength_MPa": 8,
            "modulus_of_elasticity_MPa": 4000,
            "density_overall_kg_m3": 700,

            "advantages_de": [
                "Traditionelles hochperformes Material",
                "Ausgezeichnetes Festigkeits-Gewichts-Verhältnis",
                "Gute Schmirgeleigenschaften",
                "Schwimmfähig",
            ],

            "disadvantages_de": [
                "KRITISCH: Fäulnis-Risiko durch Holzabbau-Pilze",
                "Anfällig für Insekten-Befall (Teredo navalis - Schiffswurmbefall)",
                "Wassereindringung führt zu Schimmelbildung und Verwesung",
                "Reparatur schwierig (Balsa-Austausch kompliziert)",
                "Höchste Kosten unter Kern-Materialien",
            ],

            "rot_risk_factors_de": [
                "Feuchte über 18%",
                "Oberflächentemperatur über 25°C kontinuierlich",
                "Schlechte Belüftung in Hohlräumen",
                "Eindringung von Meerwasser",
            ],

            "expected_lifespan_good_conditions_years": 18,
            "expected_lifespan_poor_conditions_years": 5,
            "prevention_measures_de": [
                "Mehrfach-Versiegelung mit Epoxy oder Polyester-Harz",
                "Belüftungslöcher zur Vermeidung von Feuchtestau",
                "Jährliche Inspektionen auf Verfärbungen und Weichstellen",
                "Bei Verdacht sofort ausbessern",
            ],
        },
    },
}


# =============================================================================
# ANTIFOULING KNOWLEDGE DATABASE
# =============================================================================

ANTIFOULING_DATABASE: Dict[str, Any] = {
    "metadata": {
        "name_de": "Antifouling-Beschichtungssystem-Wissensdatenbank",
        "description_de": "Umfassende Kenntnisse zu Antifouling-Systemen, Biozidfunktion, Umweltaspekten und Kompatibilität",
        "version": "1.0",
        "last_updated": "2026-03-22",
    },

    "antifouling_types": {
        "self_polishing_ablative": {
            "name_de": "Selbstpolierendes Ablations-Antifouling (SPC - Self-Polishing Copolymer)",
            "mechanism_de": "Kontinuierliche Erosion der Oberflächenschicht mit Biozid-Freisetzung",
            "chemistry_de": "Zinnbasierte Organozinn-Verbindungen oder Kupferbasierte Systeme",

            "typical_formulation_de": {
                "base_resin": "Acryl-Copolymer",
                "biocide_copper_oxide_percent": 35,
                "additional_biocides": "2-Methylisothiazol-3-one (MIT), Benzoissothiazol",
                "solvents_percent": 15,
                "filler_talc_percent": 10,
            },

            "properties_de": {
                "polishing_rate_mm_per_year": 0.15,
                "biocide_release_rate_micrograms_cm2_per_day": 3.5,
                "hardness_shore_d": 75,
                "adhesion_strength_MPa": 1.2,
                "water_uptake_percent": 2.5,
            },

            "advantages_de": [
                "Gleichmäßige Biozid-Freisetzung über gesamte Nutzungsdauer",
                "Oberfläche bleibt glatt durch kontinuierliche Erosion",
                "Gute Leistung in Brackwasser und Flussgebieten",
                "Kostengünstig in Anschaffung",
            ],

            "disadvantages_de": [
                "Dicke-Verlust über Zeit: 3-5mm pro Jahr",
                "Typische Lebensdauer: 2-3 Jahre (8-12mm Schicht)",
                "Umweltbelastung durch kontinuierliche Biozid-Freisetzung",
                "Nicht für Boote mit langem Aufenthalt optimal",
            ],

            "typical_lifespan_years": 2.5,
            "recoating_interval_months": 24,
            "cost_per_m2_eur": 35,
            "application_thickness_mm": 10,
        },

        "hard_non_sloughing": {
            "name_de": "Harte nicht-abtragende Antifouling",
            "mechanism_de": "Biozid-Freisetzung durch Diffusion ohne Oberflächenerosion",
            "chemistry_de": "Kupfer- oder Zinnpartikel in Epoxy oder Polyurethan-Matrix",

            "typical_formulation_de": {
                "base_resin": "Epoxy oder Polyurethan",
                "biocide_copper_percent": 25,
                "additional_biocides": "Zinkpyrithion, Organozinn optional",
                "fillers_percent": 15,
                "hardener_epoxy_by_volume_percent": 100,
            },

            "properties_de": {
                "polishing_rate_mm_per_year": 0.0,
                "biocide_release_rate_micrograms_cm2_per_day": 0.8,
                "hardness_shore_d": 85,
                "adhesion_strength_MPa": 2.5,
                "water_uptake_percent": 0.5,
                "gloss_retention_percent": 80,
            },

            "advantages_de": [
                "LANGLEBIG: typisch 5-7 Jahre (bis 10 Jahren möglich)",
                "Oberfläche bleibt hart und glatt",
                "Minimal Biozid-Freisetzung nach initialer Sättigung",
                "Ideal für Langstrecken und Liveaboards",
                "Umweltfreundlicher als ablative Systeme",
            ],

            "disadvantages_de": [
                "Höhere Anschaffungskosten (2-3x mehr als SPC)",
                "Oberflächenrauheit nimmt zu wenn Biozid aufgebraucht ist",
                "Wenn Biofilm etabliert ist, Erneuerung schwierig",
                "Erfordert spezialisiertes Auftragen mit Druckluft",
            ],

            "typical_lifespan_years": 6,
            "recoating_interval_months": 60,
            "cost_per_m2_eur": 85,
            "application_thickness_mm": 150,

            "biocide_depletion_timeline_years": {
                "year_1": {"release_rate_percent": 100},
                "year_2": {"release_rate_percent": 65},
                "year_3": {"release_rate_percent": 35},
                "year_4": {"release_rate_percent": 15},
                "year_5": {"release_rate_percent": 5},
                "year_6": {"release_rate_percent": 2},
            },
        },

        "silicone_foul_release": {
            "name_de": "Silikon-Antifouling (Foul-Release-System)",
            "mechanism_de": "Niedrige Oberflächenenergie verringert Adhäsion von Biofilm",
            "chemistry_de": "Polydimethylsiloxan (PDMS) oder verwandte Siloxan-Polymere",
            "tin_free": True,
            "copper_free": True,
            "biocide_free": True,

            "typical_formulation_de": {
                "base_polymer": "Polydimethylsiloxan (PDMS)",
                "cross_linking_agent": "Alkoxysilane",
                "surface_energy_dyn_cm": 20,
            },

            "properties_de": {
                "contact_angle_water_degrees": 110,
                "surface_roughness_ra_micron": 0.8,
                "adhesion_to_substrate_MPa": 0.3,
                "foul_release_effectiveness_percent": 90,
                "friction_reduction_percent": 3,
            },

            "advantages_de": [
                "Umweltfreundlich: keine Biozide",
                "Biofilm wird durch hydrodynamische Kräfte abgelöst",
                "Lange Lebensdauer: 7-8 Jahre möglich",
                "Niedriger Widerstand (3-5% Schubspannungs-Reduktion)",
                "Visuell ansprechend, hoher Glanz",
            ],

            "disadvantages_de": [
                "KRITISCH: erfordert Mindestgeschwindigkeit von 7-8 Knoten zur Funktion",
                "Bei Stillstand (Hafen, Anker) setzt Biofilm an",
                "Keine aktive biozide Wirkung, rein mechanisches Konzept",
                "Sehr hohe Kosten (4-5x mehr als harte Antifouling)",
                "Spezialisierte Applikation erforderlich",
            ],

            "minimum_velocity_requirement_knots": 7.5,
            "typical_lifespan_years": 7.5,
            "recoating_interval_months": 84,
            "cost_per_m2_eur": 160,
            "application_thickness_mm": 200,

            "performance_at_rest_de": {
                "days_in_stillwater": 7,
                "biofilm_coverage_percent": 60,
                "slime_growth_mm": 3,
            },
        },

        "copper_free_alternatives": {
            "name_de": "Kupferfreie Antifouling-Systeme",
            "motivation_de": "Umweltschutz und Regulierung gegen Kupferfreisetzung",

            "biocide_options_de": {
                "zinc_pyrithion": {
                    "name_de": "Zinkpyrithion (ZPT)",
                    "chemical_formula": "C₅H₄N₂S.2Zn",
                    "mechanism_de": "Störung von Zellmembranen und Energiestoffwechsel",
                    "effectiveness_percent": 75,
                    "environmental_concern_de": "Moderat, bioakkumulierbar in bestimmten Organismen",
                    "typical_concentration_percent": 4,
                },
                "copper_free_organic_biocides": {
                    "name_de": "Organische Biozide ohne Kupfer",
                    "examples_de": [
                        "Methylisothiazol-3-one (MIT) - breitspektrumantimikrobiell",
                        "Benzoisothiazol (BIT) - für Bakterien und Algen",
                        "Chlormethylisothiazol (CMIT) - ähnlich wie MIT",
                    ],
                    "mechanism_de": "Störung von Enzymen und Proteinsyntheseenen",
                    "effectiveness_percent": 60,
                    "environmental_concern_de": "Hoch, birgt Aquatoxizität",
                },
                "natural_bio_actives": {
                    "name_de": "Natürliche bioaktive Stoffe",
                    "examples_de": [
                        "Eichenrinde-Extrakt (Tannine)",
                        "Terpene aus Pflanzen",
                        "Meeresamalgenstoffe",
                    ],
                    "mechanism_de": "Verschiedenste (Enzyminhibition, Quorum Sensing Disruption)",
                    "effectiveness_percent": 40,
                    "environmental_concern_de": "Niedrig bis moderat",
                    "limitation_de": "Noch nicht marktreife Technologie",
                },
            },

            "regulations_driving_adoption_de": [
                "IMO MEPC 195(48) - Verbot von TBT (Tributylzinn) seit 2008",
                "EU Biozid-Richtlinie 98/8/EG - Restriktionen für aggressive Biozide",
                "Washington State Copper Ban (ab 2018) - Verbot von Kupfer-Antifouling",
                "Kalifornien Proposition 65 - Kupfer-Warnung",
            ],
        },
    },

    "compatibility_matrix": {
        "copper_on_aluminum": {
            "combination_de": "Kupfer-haltiges Antifouling auf Aluminiumrumpf",
            "risk_level": "KRITISCH - AUGENBLICKLICHES SCHEITERN",
            "galvanic_potential_volts": 0.76,
            "corrosion_current_mA_per_cm2": 800,
            "corrosion_rate_mm_per_year": 15,
            "time_to_perforation_mm_in_years": {
                "1mm_wall": 0.07,
                "2mm_wall": 0.13,
                "3mm_wall": 0.2,
            },
            "consequences_de": [
                "Lokale Lochkorrosion setzt innerhalb von Tagen ein",
                "Rumpfperforationen innerhalb von Wochen/Monaten möglich",
                "Boot-Sinken durch schnelle Wassereindringung",
                "Totale Rumpf-Zerstörung innerhalb von 1-2 Segelaison",
            ],
            "solution_de": "Niemals anwenden! Alternative Coatings oder isolierende Schichten erforderlich",
        },

        "coppercoat_epoxy_copper": {
            "combination_de": "Coppercoat Epoxy-Kupfer-System auf Aluminiumrumpf",
            "risk_level": "SICHER",
            "isolation_method_de": "Dicke Epoxy-Barriere (300 µm) isoliert Kupferpartikel von Aluminium",
            "corrosion_rate_mm_per_year": 0.01,
            "brand_examples_de": [
                "Coppercoat (UK)",
                "Nano-Shield",
                "Advanced Epoxy Copper Systems",
            ],
            "safety_requirements_de": [
                "Barriere-Schicht muss intakt sein",
                "Maximale Dicke: 500 µm, minimale Dicke: 200 µm",
                "Regelmäßige Inspektionen auf Beschädigungen",
                "Lokale Reparaturen sofort durchführen wenn Kratzer erkannt",
            ],
            "cost_premium_vs_standard_copper_percent": 45,
        },

        "overcoating_protocol": {
            "compatibility_check_de": "Neues System muss mit bestehendem System chemisch verträglich sein",

            "example_scenarios": {
                "old_tin_to_copper_free": {
                    "compatibility": "PROBLEMATISCH",
                    "reason_de": "Alte Zinnbasierte Systeme können unter Kupferfreisystem Blasenbildung verursachen",
                    "mitigation_de": "Kompletter Sandstrahl-Abschlag erforderlich, dann neues System",
                },
                "copper_to_copper": {
                    "compatibility": "GUT",
                    "reason_de": "Ähnliche chemische Natur",
                    "mitigation_de": "Oberfläche aufrauhen mit Schleifmittel 80er Körnung, dann überlackieren",
                },
                "silicone_to_copper": {
                    "compatibility": "SCHLECHT",
                    "reason_de": "Silikon-Oberflächenenergie führt zu Ablösung",
                    "mitigation_de": "Komplett abblättern mit Druckluftstrahler, dann neu auftragen",
                },
            },
        },
    },

    "biocide_regulations": {
        "european_union": {
            "regulation_name": "EU Biozid-Produkte-Verordnung (BPR) 528/2012",
            "active_biocides_approved_de": [
                "Kupferverbindungen (CuO, Cu2O) - max 50% in Antifouling",
                "Zinkpyrithion - max 3%",
                "Chlormethylisothiazol + Methylisothiazol - max 0,75%",
                "Dichlorfluanid - max 2% (auslauf)",
                "Trichoderma spp. - biologische Alternativen",
            ],
            "banned_substances_de": [
                "Tributylzinn (TBT) - seit 2008 komplett",
                "Dibutylzinn (DBT)",
                "Kupfer in Konzentrationen > 50%",
                "Nonylphenol und Nonylphenolethoxylate",
            ],
            "testing_requirements_de": "Aquatoxizität muss dokumentiert sein (LC50 für Fische, Daphnia, Algen)",
            "notification_requirement": True,
        },

        "washington_state_copper_ban": {
            "regulation_name": "Washington State Copper Antifouling Paint Ban",
            "effective_date": "2018-01-01",
            "copper_limit_mg_per_liter": 4000,
            "exemptions_de": [
                "Boote unter 25 Fuß (7,6m) Länge",
                "Boote mit metallischer Rumpfoberfläche",
                "Boote mit Tiefenwasser-Zirkulation",
            ],
            "enforcement_de": "Washington Department of Ecology, 150 EUR Mindestgeldbuße",
            "alternatives_approved_de": [
                "Zinkpyrithion-basierte Systeme",
                "Silikon-Foul-Release",
                "Kupferfreie organische Systeme",
            ],
        },

        "international_maritime_organization_imo": {
            "convention": "International Convention on the Control of Harmful Anti-fouling Systems",
            "abbreviation": "AFS Convention",
            "effective_date": "2008-09-17",
            "provisions_de": [
                "Verbot von TBT und anderen organozinn-Verbindungen",
                "Inspektionen und Zertifizierungen erforderlich",
                "Antifouling System (AFS) Statement erforderlich",
                "Port-State-Control überprüft Zertifikate",
            ],
            "surveying_requirements_de": {
                "initial_survey": "Vor Beendigung der Aufbringung",
                "renewal_survey_interval_years": 5,
                "intermediate_survey_interval_years": 2.5,
                "sea_trial_required": True,
            },
        },
    },
}


# =============================================================================
# CATHODIC PROTECTION KNOWLEDGE DATABASE
# =============================================================================

ANODE_DATABASE: Dict[str, Any] = {
    "metadata": {
        "name_de": "Kathoden-Schutzsystem-Wissensdatenbank",
        "description_de": "Umfassende Kenntnisse zu Opferanoden, Dimensionierung, Platzierung und Auswechselintervallen",
        "version": "1.0",
        "last_updated": "2026-03-22",
    },

    "anode_materials": {
        "zinc": {
            "name_de": "Zink",
            "chemical_symbol": "Zn",
            "anodic_protection_mechanism_de": "Zink oxidiert bevorzugt statt Stahl/Bronze, wirkt als Opfer",
            "galvanic_potential_vs_sce_volts": -1.1,
            "density_kg_m3": 7140,
            "current_capacity_ampere_hours_per_kg": 820,

            "advantages_de": [
                "Standard in Salzwasser",
                "Kostengünstig",
                "Bewährtes Material seit über 100 Jahren",
                "Gute Stromverteilung",
                "Keine Titanium-Barriere nötig",
            ],

            "disadvantages_de": [
                "Kürzere Lebensdauer als Magnesium oder Aluminium (2-3 Jahre Salzwasser)",
                "Langsamere Stromlieferung in Brackwasser",
                "Formationskorrosion (weiße Krusten) kann Stromfluss blockieren",
            ],

            "suitable_environment_de": "Vollständiges Salzwasser (Salinität > 18 ppt)",
            "unsuitable_in_de": "Süßwasser, Brackwasser",

            "typical_consumption_rate_in_saltwater_kg_per_year": {
                "light_duty": 0.4,
                "moderate_duty": 1.2,
                "heavy_duty": 3.5,
            },

            "cost_per_kg_eur": 6,
        },

        "magnesium": {
            "name_de": "Magnesium",
            "chemical_symbol": "Mg",
            "anodic_protection_mechanism_de": "Magnesium oxidiert noch leichter als Zink, stärkeres Opfer",
            "galvanic_potential_vs_sce_volts": -2.3,
            "density_kg_m3": 1738,
            "current_capacity_ampere_hours_per_kg": 2200,

            "advantages_de": [
                "Höhere Stromproduktion pro Gewicht",
                "Gute Wahl für Süßwasser und Brackwasser",
                "Stärkere Schutzwirkung als Zink",
            ],

            "disadvantages_de": [
                "KÜRZERE LEBENSDAUER als Zink: typisch 1-2 Jahre in Salzwasser",
                "Schnelle Verbrauchsrate in Meerwasser (bis zu 5x höher)",
                "Aggressive Stromverteilung kann zu Wasserstoff-Evolution führen",
                "Nicht ideal für lange Segelzeiten",
            ],

            "suitable_environment_de": "Süßwasser, Brackwasser, schwach salzhaltig",
            "unsuitable_in_de": "Vollständiges Salzwasser mit langen Einsatzzeiten",

            "typical_consumption_rate_in_saltwater_kg_per_year": {
                "light_duty": 2.1,
                "moderate_duty": 5.8,
                "heavy_duty": 12.0,
            },

            "typical_consumption_rate_in_freshwater_kg_per_year": {
                "light_duty": 0.3,
                "moderate_duty": 0.8,
                "heavy_duty": 1.5,
            },

            "cost_per_kg_eur": 12,
        },

        "aluminum": {
            "name_de": "Aluminium (Al-Zn-In oder ähnlich legiert)",
            "chemical_symbol": "Al",
            "anodic_protection_mechanism_de": "Höchste Stromproduktion, längste Lebensdauer",
            "galvanic_potential_vs_sce_volts": -0.83,
            "density_kg_m3": 2700,
            "current_capacity_ampere_hours_per_kg": 2800,

            "advantages_de": [
                "LÄNGSTE LEBENSDAUER: 3-5 Jahre auch in reinem Salzwasser",
                "Höchste Stromproduktion pro Volumen",
                "Universal einsetzbar (Salzwasser, Brackwasser, Süßwasser)",
                "Geringe Formationskorrosion",
                "Am besten für Langzeitschutz",
            ],

            "disadvantages_de": [
                "Höchste Kosten (2x mehr als Zink)",
                "Benötigt sorgfältige Legierungs-Zusammensetzung",
                "Nicht alle Al-Legierungen sind gleich geeignet",
                "Bei schlechter Legierung kann Selbstauflösung eintreten",
            ],

            "recommended_alloy_composition_de": {
                "aluminum_percent": 85,
                "zinc_percent": 4,
                "indium_percent": 0.05,
                "remainder_copper_etc_percent": 11,
            },

            "suitable_environment_de": "Alle (Salzwasser, Brackwasser, Süßwasser)",
            "suitable_for_extended_voyages": True,

            "typical_consumption_rate_in_saltwater_kg_per_year": {
                "light_duty": 0.25,
                "moderate_duty": 0.7,
                "heavy_duty": 1.8,
            },

            "lifespan_saltwater_years": 4,
            "lifespan_brackwater_years": 6,
            "lifespan_freshwater_years": 8,

            "cost_per_kg_eur": 18,
        },
    },

    "dimensioning_rule": {
        "one_percent_rule_de": {
            "rule_statement_de": "Opferanodengesamtmasse sollte etwa 1% der Gesamtmasse des geschützten Metalls sein",
            "formula": "M_anode = 0.01 * M_protected_metal",
            "application_de": "Faustregel für einfache Auslegung ohne detaillierte Analyse",
            "accuracy_percent": 85,
        },

        "detailed_calculation_method": {
            "method_de": "Strombedarfs-Analyse mit Stromverteilungs-Modellen",

            "input_parameters_de": [
                "Gesamtfläche der geschützten Metalloberfläche (m²)",
                "Umgebungselektrolytwiderstand (ohm·cm) - typisch 25 ohm·cm für Meerwasser",
                "Anode-zu-Kathode Entfernung (m) - kritischer Abstand",
                "Stromverteilungs-Effizienz (%) - typisch 60-80%",
                "Schutzpotential des Materials (Volts gegen Seawater Reference Electrode)",
            ],

            "calculation_steps_de": [
                "1. Strombedarfs-Berechnung: I = A * i_d",
                "   I = erforderlicher Strom (Ampere)",
                "   A = geschützte Fläche (m²)",
                "   i_d = Stromdichte für Material (mA/m²)",
                "",
                "2. Anodenmasse-Berechnung: M = (I * t) / (Q * n)",
                "   M = Anodenmasse (kg)",
                "   I = erforderlicher Strom",
                "   t = gewünschte Schutzdauer (Stunden)",
                "   Q = Stromkapazität der Anode (A·h/kg)",
                "   n = Stromausnutzungs-Effizienz",
            ],

            "typical_stromdensity_values_mA_m2": {
                "steel_bare": 150,
                "steel_painted": 50,
                "copper_nickel": 100,
                "bronze": 80,
                "stainless_steel_passive": 20,
            },

            "typical_schutzpotential_vs_swe_volts": {
                "mild_steel": -0.85,
                "cast_iron": -0.82,
                "copper_nickel": -0.50,
                "bronze": -0.40,
                "stainless_steel": -0.35,
            },
        },
    },

    "anode_positioning": {
        "principle_de": "Anoden sollten in der Nähe des zu schützenden Materials positioniert sein",
        "ion_travel_de": "Ionen wandern in ungefähr gerader Linie von Anode zu Kathode",
        "effective_distance_mm": 300,

        "typical_yacht_locations": {
            "through_hull_fittings": {
                "description_de": "Seewasser-Zuführungen wie Logge, Echolot-Transducer",
                "anode_size_grams": 50,
                "ideal_position_de": "Innerhalb 150mm des Through-Hull-Fitting",
                "typical_locations_de": [
                    "An Logge-Kopf oder direkt darunter",
                    "In der Nähe von Seewasser-Ansaugkasten",
                    "Dicht bei Echolot-Transducern",
                ],
            },

            "rudder": {
                "description_de": "Ruderstamm und Blatt mit Bronze-Lagern",
                "anode_size_grams": 200,
                "ideal_position_de": "Oben am Ruderstamm, beide Seiten",
                "typical_locations_de": [
                    "Links und rechts des Ruderstamms oberhalb von Wasserlinie",
                    "Falls möglich, direkt auf dem Ruderstamm montiert",
                    "Abstand nicht mehr als 100mm",
                ],
            },

            "propeller_shaft": {
                "description_de": "Wellen-Bolzen und Propeller-Befestigung",
                "anode_size_grams": 300,
                "ideal_position_de": "Direkt neben Propeller oder auf Welle montiert",
                "typical_locations_de": [
                    "Propeller-Nabe: 80gm Ring-Anode",
                    "Wellen-Scheibe: 120gm Ring-Anode",
                    "Shaft-Log Durchführung: 50gm kleine Anode",
                ],
            },

            "keel": {
                "description_de": "Kielmetall und Kielbolzen",
                "anode_size_grams": 400,
                "ideal_position_de": "Direkt an Kielgitter oberhalb von Kiel-Bulb",
                "typical_locations_de": [
                    "Beide Seiten des Kielschafts",
                    "An Gitter-Verschweißungen",
                    "Oberhalb des Kiel-Bolzen-Bereichs",
                ],
            },

            "heat_exchanger": {
                "description_de": "Kupfer/Kupfer-Nickel Wärmetauscher",
                "anode_size_grams": 150,
                "ideal_position_de": "Auf Wärmetauscher selbst oder darin",
                "typical_locations_de": [
                    "Im Inneren des Wärmetauschers (Stiftanode)",
                    "An Seewasser-Einlass des Wärmetauschers",
                ],
            },
        },

        "positioning_error_consequences_de": {
            "too_far_from_metal_de": {
                "distance_mm": 600,
                "effect_de": "Stromverlust durch Ohm'schen Widerstand des Elektrolyts",
                "protection_percent": 30,
                "consequence_de": "Unzureichender Schutz, Korrosion trotz Anode",
            },
            "anode_shielded_by_hull_de": {
                "effect_de": "Anode physisch von Wasser getrennt",
                "protection_percent": 0,
                "consequence_de": "Vollständiger Schutz-Ausfall",
            },
        },
    },

    "replacement_strategy": {
        "inspection_frequency": {
            "during_boat_season_months": 3,
            "during_haul_out_months": 12,
            "after_extended_voyage_days": 30,
        },

        "replacement_trigger_50_percent_rule": {
            "rule_de": "Anode auswechseln wenn 50% des Materials aufgebraucht ist",
            "reasoning_de": "Nach 50% Verbrauch sinkt Stromverteilung und Schutzeffizienz rapide",
            "visual_assessment_de": "Einfache visuelle Kontrolle reicht: Ist die Anode um die Hälfte kleiner als ursprünglich?",
            "measurement_method_de": "Vergleich mit Referenz-Anode oder Waage-Messung",
        },

        "premature_failure_indicators": {
            "white_corrosion_deposits_de": {
                "appearance_de": "Weiße Krusten um Anode",
                "cause_de": "Formationskorrosion blockiert Stromfluss",
                "action_de": "Anode entfernen und abbürsten, oder austausch",
            },
            "rapid_consumption_de": {
                "rate_above_normal_factor": 2,
                "causes_de": [
                    "Stray Current im Wasser (andere Boote, Ladestation)",
                    "Unerwartete galvanische Paare im Rumpf",
                    "Gebrochene Isolation der Anode",
                ],
                "action_de": "Elektrizität im Wasser testen, Isolation kontrollieren",
            },
        },

        "typical_lifespan_saltwater": {
            "zinc_years": 2.5,
            "magnesium_years": 1.5,
            "aluminum_years": 4.0,
        },

        "cost_of_replacement": {
            "single_propeller_anode_eur": 35,
            "complete_sacrificial_system_eur": 850,
            "labor_cost_installation_eur": 250,
        },
    },

    "inspection_best_practices": {
        "visual_inspection_checklist_de": [
            "Vollständigkeitsprüfung: fehlen Anoden?",
            "Größenvergleich: Anode deutlich geschrumpft?",
            "Oberflächenkondition: Korrosionskrusten? Weiße Beläge?",
            "Befestigung: sitzt Anode fest? Lockerung sichtbar?",
            "Isolation: ist Isolationsmaterial verschlissen?",
            "Nachbar-Materialien: Korrosionsspuren sichtbar trotz Anode?",
        ],

        "electrical_testing_de": {
            "potential_measurement": {
                "method_de": "Potentiometer-Messung gegen Seawater Reference Electrode (SRE)",
                "required_potential_vs_sre_volts": -0.80,
                "acceptable_range_volts": [-0.85, -0.75],
                "measurement_location_de": "Direkt neben geschütztem Metal",
                "measurement_technique_de": "Hochohmiger Voltmeter mit Hochohmiger Referenzelektrode",
            },

            "current_measurement": {
                "method_de": "Stromfluss-Messung mit Amperemeter oder Shunt",
                "typical_current_range_milliamperes": [50, 500],
                "too_high_current_de": "Indicates stray current oder unerwartete galvanische Paare",
                "zero_current_de": "Indicates broken anode connection oder anode consumed completely",
            },
        },
    },
}


# =============================================================================
# INTEGRATED KNOWLEDGE CROSS-REFERENCES
# =============================================================================

INTEGRATED_WARNINGS: Dict[str, Any] = {
    "critical_combinations": [
        {
            "hazard_de": "Spadelruder mit V2A-Kielbolzen und Kupfer-Antifouling auf Aluminium",
            "risk_level": "EXTREM HOCH",
            "components_affected_de": [
                "Spadelruder: cantilever forces mit hohem Ermüdungsrisiko",
                "V2A-Kielbolzen: spaltkorrosion unter Stress wahrscheinlich",
                "Kupfer auf Aluminium: sofortige galvanische Zerstörung des Rumpfes",
            ],
            "failure_timeline_months": 6,
            "catastrophic_consequence_de": "Simultane Ruder- und Kielverluste mit möglichem Bootsverlust",
            "mitigation_de": "Monel K-500 Bolzen, skegg-hängend Ruder, Silikon oder Coppercoat Antifouling",
        },
        {
            "hazard_de": "Schaum-Kern Ruderwagen in kaltem Klima mit Wassereindringung",
            "risk_level": "HOCH",
            "failure_mode_de": "Gefrieren-Schmelzen Zyklus erzeugt 9% Expansion, delamination und Strukturversagen",
            "timeline_to_failure_months": 3,
            "mitigation_de": "Balsa oder Solid GFK verwenden, oder alle Kanten mit 2-schicht Epoxy versiegeln",
        },
    ],

    "inspection_schedule_recommended_de": {
        "before_every_passage": [
            "Visuell: Kielbox auf Wasser überprüfen",
            "Visuell: Ruderblock auf Spiele und Verschleiß",
            "Visuell: Anoden auf Größe und Verschleiß",
        ],
        "every_3_months": [
            "Fadenlehre an Kielbolzen (4 Positionen)",
            "Ruder-Clearance-Messung",
            "Antifouling-Oberflächen-Inspektion",
            "Anode-Größenvergleich mit Baseline",
        ],
        "every_12_months": [
            "Ultraschall-Prüfung der Kielbolzen",
            "Kielbox-Wasserdichtigkeitsprüfung",
            "Ruder-Durchdrehtest unter Last",
            "Holslader-Abklopfen auf Delamination",
        ],
        "every_2_years": [
            "Röntgen oder Gamma-Radiographie Kielbolzen",
            "Potentiometer-Messung Kathoden-Schutz",
            "Austausch aller Anoden (Sicherheit)",
        ],
        "every_5_years": [
            "Detaillierte Vermessung Kielgitter-Risse",
            "Hochauflösende MPI-Prüfung Kielbolzen",
            "Vollständige Antifouling-Neubeschichtung",
            "Ruder-Lagergewinde-Überprüfung",
        ],
    },
}


# =============================================================================
# END OF MODULE
# =============================================================================

if __name__ == "__main__":
    """Module verification and documentation."""
    print(f"AYDI Kiel, Ruder & Unterwasserschiff — Tiefenwissen Modul")
    print(f"Version: 1.0")
    print(f"")
    print(f"Verfügbare Datenbanken:")
    print(f"  - KEEL_DATABASE: {len(KEEL_DATABASE)} Kategorien")
    print(f"  - RUDDER_DATABASE: {len(RUDDER_DATABASE)} Kategorien")
    print(f"  - ANTIFOULING_DATABASE: {len(ANTIFOULING_DATABASE)} Kategorien")
    print(f"  - ANODE_DATABASE: {len(ANODE_DATABASE)} Kategorien")
    print(f"  - INTEGRATED_WARNINGS: {len(INTEGRATED_WARNINGS)} Abschnitte")
    print(f"")
    print(f"Gesamtzeilen Code: {sum(1 for line in open(__file__).readlines())}")
