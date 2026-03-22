"""
AYDI Deck-Hardware Tiefenwissen
Exhaustive technical specifications for all marine deck hardware.

Covers: Winches, Blocks, Cleats, Tracks, Pad Eyes, Stanchions, Hatches, Portlights
Manufacturers: Harken, Lewmar, Antal, Ronstan, Andersen, Spinlock, Goiot, Bomar, Wichard

Author: AYDI Research Team
Version: 1.0
Last Updated: 2026-03-22
"""

from typing import Dict, List, Any


# ============================================================================
# WINSCH-DATENBANK — Winch specifications by manufacturer
# ============================================================================

WINCH_DATABASE: Dict[str, Any] = {
    "sizing_principles": {
        "power_ratio_formula": "(handle_length / drum_radius) * gear_ratio",
        "mechanical_advantage_definition": "Kraft-Ausgang / Kraft-Eingang bei Kurbelgriff",
        "standard_handle_length_mm": 254,
        "standard_handle_length_inch": 10,
        "8_inch_handle_reduction_percent": 20,
        "8_inch_handle_note_de": "20% weniger Kraftvorteil als 10-Zoll Standardgriff",
        "rule_of_thumb_de": "Winschgröße_kg = mindestens 2× maximale Schot-Last in kg",
        "safety_margin_de": "3× für Hochsee-Fahrt bei unverhofften Böen empfohlen",
        "sheet_load_calculation": "Segelfläche_m2 × 30 = Schot-Last in kg (Faustregel für Kreuzer)",
        "racing_calculation": "Segelfläche_m2 × 45 = Schot-Last in kg (Faustregel für Racing)",
        "calculation_note_de": "Diese Faustregel gilt für stabilen, moderaten Wind. In Böen bis 3× höhere Belastung möglich!",
        "power_ratio_definition": "Kraft am Griff × Power Ratio = maximale Schot-Last",
        "example_calculation": {
            "winch_size": 40,
            "power_ratio_2speed": 37.2,
            "operator_weight_kg": 75,
            "estimated_line_load_with_leverage": "75 kg × 37.2 = 2790 kg (27.9 kN) theoretisch",
            "note_de": "Real: ~50% weniger durch Reibung in Getriebe und Schäkeln"
        }
    },
    "harken": {
        "manufacturer": "Harken Inc. (Ventura, California / Società Italiana Harken, Genua)",
        "ranges": {
            "radial": {
                "description_de": "Standard-Winsch mit Radiallager, bewährtes Design seit 1975",
                "design_feature": "Axiale + Radiale Kugellagerkombination",
                "sizes": [15, 20, 32, 35, 40, 46, 50, 60, 70, 80],
                "models": [
                    {
                        "size": 35,
                        "type": "Self-Tailing Radial",
                        "power_ratio_2speed": 35.9,
                        "max_line_mm": 12,
                        "drum_diameter_mm": 63.5,
                        "weight_kg": 4.1,
                        "height_mm": 152,
                        "mounting": "5-loch Edelstahl-Flansch M6",
                        "self_tailing_teeth": "16"
                    },
                    {
                        "size": 40,
                        "type": "2-Speed Self-Tailing",
                        "power_ratio_1st_gear": 8.5,
                        "power_ratio_2nd_gear": 37.2,
                        "gear_ratio_1st": 2.2,
                        "gear_ratio_2nd": 9.6,
                        "max_line_mm": 14,
                        "drum_diameter_mm": 76.2,
                        "weight_kg": 6.3,
                        "height_mm": 178,
                        "application_1st_gear_de": "Schnelles Schoteintritt unter hoher Last (Halsen in schwerer See)",
                        "application_2nd_gear_de": "Fein-Trimm mit leichter Hand, präzise Segelsteller"
                    },
                    {
                        "size": 46,
                        "type": "2-Speed Self-Tailing",
                        "power_ratio_1st": 10.2,
                        "power_ratio_2nd": 44.8,
                        "gear_ratio_1st": 2.65,
                        "gear_ratio_2nd": 11.6,
                        "max_line_mm": 16,
                        "drum_diameter_mm": 88.9,
                        "weight_kg": 8.8,
                        "height_mm": 203,
                        "application_de": "Spinnaker-Winschen auf Segelyachten 40-55 Fuß"
                    },
                    {
                        "size": 50,
                        "type": "2-Speed Self-Tailing",
                        "power_ratio_1st": 11.5,
                        "power_ratio_2nd": 51.3,
                        "max_line_mm": 16,
                        "drum_diameter_mm": 101.6,
                        "weight_kg": 12.2,
                        "height_mm": 229,
                        "application_de": "Großboot-Spinnaker (50-65 Fuß), Hauptschot-Winschen Motorsailer"
                    },
                    {
                        "size": 60,
                        "type": "3-Speed Self-Tailing",
                        "power_ratio_3rd": 62.0,
                        "gear_count": 3,
                        "max_line_mm": 18,
                        "drum_diameter_mm": 114.3,
                        "weight_kg": 16.4,
                        "height_mm": 254,
                        "gear_2_power_ratio": 24.8,
                        "application_de": "Professionelle Racing und Hochsee-Kreuzer 60-75 Fuß"
                    },
                    {
                        "size": 70,
                        "type": "3-Speed Self-Tailing",
                        "power_ratio_3rd": 75.0,
                        "gear_2_power_ratio": 28.5,
                        "max_line_mm": 20,
                        "drum_diameter_mm": 127.0,
                        "weight_kg": 22.3,
                        "height_mm": 279,
                        "application_de": "Großyachten, Seeschiffe, Formel-40 Racer"
                    },
                    {
                        "size": 80,
                        "type": "3-Speed Self-Tailing",
                        "power_ratio_3rd": 93.24,
                        "gear_2_power_ratio": 37.1,
                        "max_line_mm": 22,
                        "drum_diameter_mm": 152.4,
                        "weight_kg": 29.5,
                        "height_mm": 330,
                        "breaking_load_kg": 4000,
                        "application_de": "Superyachten, Werften, schwere Lasten"
                    }
                ],
                "drum_materials_info": {
                    "aluminum": {
                        "weight": "leicht (100% Referenz)",
                        "durability": "mittel",
                        "finish": "matt",
                        "corrosion_resistance": "gering ohne Anodisierung",
                        "note_de": "Verschleißt bei Regatta-Einsatz schneller, Oberfläche raut auf",
                        "maintenance_interval_months": 6,
                        "cost_factor": 1.0
                    },
                    "chrome_bronze": {
                        "weight": "schwer (~3× Aluminium)",
                        "durability": "hoch",
                        "finish": "glänzend (anlaufend)",
                        "corrosion_resistance": "sehr hoch",
                        "note_de": "Klassisch, robust, anlaufend mit der Zeit (Patina grünlich-braun)",
                        "maintenance_interval_months": 12,
                        "patina_reduction": "Weißes Schraubermittel oder Taublutzitrat",
                        "cost_factor": 3.5
                    },
                    "stainless_steel": {
                        "weight": "mittel",
                        "durability": "sehr hoch",
                        "finish": "glänzend (beständig)",
                        "corrosion_resistance": "excellent (316L)",
                        "note_de": "Kein Anlaufen, längste Lebensdauer (30+ Jahre)",
                        "maintenance_interval_months": 24,
                        "cost_factor": 5.0,
                        "density_g_cm3": 7.75
                    }
                }
            },
            "performa": {
                "description_de": "Performance-Serie mit optimiertem Getriebe, leichterer Kurbelbetrieb",
                "design_feature": "Hochleistungs-Zahnkronen mit verbesserter Verzahnung",
                "sizes": [20, 30, 35, 40, 46, 50, 60],
                "features_de": [
                    "15% leichterer Kurbelbetrieb vs. Standard Radial",
                    "Geringere Reibung durch Precision-Getriebe",
                    "Schnellerer Schoteintritt (höhere Drehgeschwindigkeit)",
                    "Optimiert für Racing und regelmäßiges Trimmen"
                ],
                "target_audience": "Wettfahrtsegler, ambitionierte Kreuzer-Rennfahrer"
            },
            "electric": {
                "description_de": "Elektrische Winschen (12V/24V/48V DC), Betrieb mit Fußschalter oder Fernbedienung",
                "motor_type": "Bürstenloser DC-Motor mit Getriebe",
                "models": [
                    {
                        "size": 40,
                        "voltage": "12V / 24V wählbar",
                        "current_draw_amps": "150A (12V) / 75A (24V)",
                        "line_speed_m_per_min": 18,
                        "pulling_force_kg": 1200,
                        "runtime_continuous_seconds": 15,
                        "cooldown_required_seconds": 45,
                        "motor_power_kw": 1.8
                    },
                    {
                        "size": 46,
                        "voltage": "12V / 24V",
                        "line_speed_m_per_min": 15,
                        "pulling_force_kg": 1600,
                        "motor_power_kw": 2.2
                    },
                    {
                        "size": 50,
                        "voltage": "24V (Standard)",
                        "line_speed_m_per_min": 13,
                        "pulling_force_kg": 1900,
                        "motor_power_kw": 2.5
                    },
                    {
                        "size": 60,
                        "voltage": "24V",
                        "line_speed_m_per_min": 12,
                        "pulling_force_kg": 2400,
                        "motor_power_kw": 3.0
                    },
                    {
                        "size": 70,
                        "voltage": "24V / 48V",
                        "line_speed_m_per_min": 11,
                        "pulling_force_kg": 3000,
                        "motor_power_kw": 3.6
                    },
                    {
                        "size": 80,
                        "voltage": "24V / 48V",
                        "line_speed_m_per_min": 10,
                        "pulling_force_kg": 4000,
                        "motor_power_kw": 4.0
                    }
                ],
                "control_options": [
                    "Direkt-Fußschalter (wartbar, zuverlässig)",
                    "Wireless Fernbedienung 2.4 GHz (bis 100m)",
                    "Automatische Spannungs-Regelung"
                ],
                "note_de": "3-Gang-Elektro: Gang 1 (schnell, niedrig Last) → Trimmen, Gang 2 (mittel) → Normalbetrieb, Gang 3 (langsam, hohe Last) → Fein-Trimm unter Druck",
                "power_consumption_comparison": {
                    "12v_system": "Hohe Stromaufnahme (150A+) — erfordert dicke Kabel (16-25 mm² Kupfer)",
                    "24v_system": "Halbierte Stromaufnahme, leichtere Verkabelung, bevorzugt bei Renovierungen",
                    "48v_system": "Viertel-Stromaufnahme, minimale Kabel-Querschnitte, neue Yachten"
                }
            },
            "manual_ratios_explained": {
                "single_speed": "Einfach, robust, leicht zu warten",
                "two_speed": "Kompromiss: schneller Schoteintritt + präzises Trimmen",
                "three_speed": "Professionell: Optimale Leistung in allen Wind-Bedingungen",
                "switching_mechanism": "Schaltring unter der Trommel — während Betrieb nicht schaltbar (Getriebebelastung)"
            }
        },
        "service_interval_months": 12,
        "service_requirements": [
            "Getriebefett erneuern (Lithium-Complex oder Marine-spezifisch)",
            "Kugellager-Spiel prüfen und nachjustieren",
            "Trommel-Oberflächenrauheit kontrollieren",
            "Selbstsichernde Schäkel prüfen (müssen fest sitzen)"
        ],
        "heavy_use_interval_months": 6,
        "heavy_use_definition": "Mehr als 100 Betriebsstunden pro Jahr oder täglicher Gebrauch"
    },
    "lewmar": {
        "manufacturer": "Lewmar Limited (Southhampton, UK) — Teil der Jabsco-Gruppe",
        "ranges": {
            "evo": {
                "description_de": "EVO Self-Tailing Serie — wartungsfreundlich, ohne Werkzeug zerlegbar, 2006+ Design",
                "innovation": "Komplett modularer Aufbau — Trommel, Getriebe und Lager einzeln austauschbar",
                "sizes": [15, 16, 30, 40, 45, 50, 55, 65],
                "models": [
                    {
                        "size": 30,
                        "gear_ratio_1st": 1.6,
                        "gear_ratio_2nd": 6.4,
                        "power_ratio_1st": 7.6,
                        "power_ratio_2nd": 30.8,
                        "max_line_mm": 10,
                        "weight_kg": 2.8,
                        "application_de": "Jib-Winsch auf Booten 24-32 Fuß, leichte Blaubelag-Ausrüstung"
                    },
                    {
                        "size": 40,
                        "gear_ratio_1st": 2.0,
                        "gear_ratio_2nd": 8.0,
                        "power_ratio_1st": 9.7,
                        "power_ratio_2nd": 38.6,
                        "max_line_mm": 12,
                        "weight_kg": 4.5,
                        "application_de": "Spinnaker-Winschen Segelyachten 32-42 Fuß (universal verwendbar)"
                    },
                    {
                        "size": 45,
                        "gear_ratio_1st": 2.3,
                        "gear_ratio_2nd": 9.2,
                        "power_ratio_1st": 11.1,
                        "power_ratio_2nd": 44.5,
                        "max_line_mm": 14,
                        "weight_kg": 6.2
                    },
                    {
                        "size": 50,
                        "gear_ratio_1st": 2.5,
                        "gear_ratio_2nd": 10.0,
                        "power_ratio_1st": 12.1,
                        "power_ratio_2nd": 48.3,
                        "max_line_mm": 16,
                        "weight_kg": 8.1
                    },
                    {
                        "size": 55,
                        "gear_ratio_1st": 2.8,
                        "gear_ratio_2nd": 11.2,
                        "power_ratio_1st": 13.6,
                        "power_ratio_2nd": 54.4,
                        "max_line_mm": 16,
                        "weight_kg": 10.3
                    },
                    {
                        "size": 65,
                        "gear_ratio_1st": 3.0,
                        "gear_ratio_2nd": 12.0,
                        "power_ratio_1st": 14.5,
                        "power_ratio_2nd": 58.0,
                        "max_line_mm": 20,
                        "weight_kg": 13.6,
                        "application_de": "Hauptschot Großboote, Racing-Yachten 50+ Fuß"
                    }
                ],
                "feature_de": "Ohne Werkzeug zum Service — Kugel-Deckel aufschrauben, Trommel entnehmen, zurücksetzen",
                "maintenance_advantage": "Ersatzteil-Set (Getriebe + Kugellager) unter 200 EUR, selbst austauschbar"
            },
            "els_electric": {
                "description_de": "Electric Load Sensing — Intelligente Elektronik passt Motor-Leistung an",
                "feature_de": "Überlastschutz schaltet automatisch ab, startet nach Lastreduktion selbst wieder",
                "voltage_options": ["12V", "24V"],
                "current_limit_amps": 200,
                "load_sensing_principle": "Drucksensor im Getriebe misst Belastung, drosselt Strom bei Überlast",
                "recovery_time_seconds": 10,
                "recovery_note_de": "System prüft jede Sekunde, ob Lastreduzierung möglich ist — intelligente Escala"
            },
            "ls_load_sensing_series": {
                "description_de": "Manuelle Load-Sensing Serie — Fliehkraft-gesteuerte Kupplung",
                "mechanism": "Getriebe-Input lädt Fliehkraft-Ring, bei Überbelastung löst Kupplung kurzzeitig",
                "advantage": "Schrittweise Kraft-Reduktion, kein abruptes Blockieren",
                "application_de": "Ideal für Anfänger, weniger technisches Verständnis nötig"
            }
        }
    },
    "andersen": {
        "manufacturer": "Andersen Winches (Dänemark) — seit 1946",
        "material_philosophy": "316L Edelstahl-Trommel, 329 Duplex-Edelstahl Antriebswellen",
        "material_advantage": "Null Korrosion im Meerwasser, wartungsfrei in Salzluft-Umgebung",
        "features_de": [
            "Power Rib Trommeldesign für kontrollierten Grip unter Last",
            "360° drehbarer Self-Tailing-Arm (ab Größe 40ST) — nie wieder Schot neu fädeln",
            "Selbstabdichtende Edelstahl-Rollen- und Kugellager",
            "Integrated Drag-Control (Reibungs-Dämpfer in Getriebe)"
        ],
        "sizes": [20, 28, 40, 50, 60, 70, 80],
        "models": [
            {
                "size": 20,
                "type": "Standard Single-Speed",
                "power_ratio": 18.5,
                "max_line_mm": 8,
                "weight_kg": 1.9,
                "application_de": "Dinghy racing, sehr leichte Yachten"
            },
            {
                "size": 28,
                "type": "Standard",
                "power_ratio": 24.0,
                "max_line_mm": 10,
                "weight_kg": 3.2
            },
            {
                "size": 40,
                "type": "ST (Self-Tailing)",
                "power_ratio": 35.0,
                "max_line_mm": 12,
                "weight_kg": 5.8,
                "rotating_arm": True,
                "rotation_degrees": 360
            },
            {
                "size": 50,
                "type": "ST Two-Speed",
                "gear_1_power": 10.2,
                "gear_2_power": 51.0,
                "max_line_mm": 14,
                "weight_kg": 8.9
            }
        ],
        "service_interval_months": 24,
        "service_note_de": "Andersen empfiehlt nur alle 2 Jahre Service bei normalem Gebrauch — Qualitätsmaterial braucht weniger Aufmerksamkeit",
        "drag_control_feature": "Einstellbares Reibungsdämpfer-System (ähnlich Spinnrolle) für Schnelle Schoten-Freigabe"
    },
    "antal": {
        "manufacturer": "Antal (Italien) — hochpräzise CNC-Fertigung",
        "design_philosophy": "Leichtgewicht + höchste Präzision = minimale Reibung",
        "material": "CNC-gefrästes Aluminium 7075-T6, hochfeste Zahnkronen aus Stahl",
        "ranges": ["Standard", "XT Cruise", "XT Race"],
        "models": [
            {
                "size": "16XT",
                "type": "Single-Speed Self-Tailing",
                "gear_ratio": 2.0,
                "power_ratio": 14.0,
                "line_range_mm": "6-10",
                "max_line_mm": 10,
                "weight_kg": 2.4,
                "height_mm": 119,
                "drum_diameter_mm": 71,
                "material": "CNC 7075-T6 Aluminium",
                "application_de": "Dinghies, Optimist, leichte Kielboote"
            },
            {
                "size": "28XT",
                "type": "Standard",
                "gear_ratio": 2.5,
                "power_ratio": 22.0,
                "line_mm": "8-12",
                "weight_kg": 4.1,
                "height_mm": 145
            },
            {
                "size": "40XT",
                "type": "Self-Tailing",
                "gear_ratio": 3.0,
                "power_ratio": 32.0,
                "line_mm": "10-14",
                "weight_kg": 7.8,
                "height_mm": 178,
                "drum_diameter_mm": 101
            },
            {
                "size": "50XT",
                "type": "Two-Speed Self-Tailing",
                "gear_ratio_1st": 2.0,
                "gear_ratio_2nd": 8.0,
                "power_ratio_1st": 11.5,
                "power_ratio_2nd": 46.0,
                "max_line_mm": 14,
                "weight_kg": 11.2
            }
        ],
        "feature_de": "Federbelastetes Self-Tailing mit automatischer Taudurchmesser-Anpassung — funktioniert mit 6-12mm Schoten",
        "auto_release_feature": "Sicherheits-Feder gibt unter Überlast (>2× rated load) automatisch frei",
        "lightweight_advantage": "30-40% leichter als Harken bei gleicher Größe",
        "precision_note": "CNC-Bearbeitung ermöglicht Toleranzen <0.1mm — minimale Verschleißteile",
        "target_audience": "Racing-orientierte Segler, Gewichts-bewusste Hochsee-Fahrer"
    },
    "spinlock": {
        "manufacturer": "Spinlock (UK) — spezialisiert auf Hochsee-Ausrüstung",
        "design_focus": "Sicherheit + Zuverlässigkeit über Geschwindigkeit",
        "features": [
            "Vollständig gekapselt gegen Salzwasser-Eindringung",
            "Manuelle Übersteuer-Möglichkeit auch bei Fehlfunktion",
            "Breite Schoten-Kompatibilität (Dyneema, Nylon, Naturseile)"
        ],
        "models": [
            {
                "series": "Evo4",
                "description_de": "Neue Generation, leichte Kurbel, großer Drehbereich",
                "sizes": [20, 30, 40, 50, 60]
            },
            {
                "series": "Classic",
                "description_de": "Bewährtes Design, schwerer, aber extrem robust",
                "advantage_de": "Kann buchstäblich nicht kaputtgehen"
            }
        ]
    }
}


# ============================================================================
# BLOCK-DATENBANK — Block/Pulley specifications
# ============================================================================

BLOCK_DATABASE: Dict[str, Any] = {
    "load_calculation": {
        "fundamental_principle": "Schot-Last × Umlenkfaktor = Gesamtlast auf Block",
        "working_load_limit": "WLL = Bruchlast / Sicherheitsfaktor",
        "deflection_factors_de": {
            "180_degrees": {"factor": 2.0, "description": "Block 180° umgelenkt (Leine zu sich selbst parallel)"},
            "150_degrees": {"factor": 1.93, "description": "Typisch in manchen Flaschenzugssystemen"},
            "120_degrees": {"factor": 1.73, "description": "Häufig bei Spinaker-Umlenkungen"},
            "90_degrees": {"factor": 1.41, "description": "90°-Umlenkung (rechtwinkliger Block)"},
            "60_degrees": {"factor": 1.0, "description": "Block lenkt minimal ab"},
            "45_degrees": {"factor": 0.77, "description": "Sehr flache Umlenkung"},
            "0_degrees_fairlead": {"factor": 1.0, "description": "Keine Umlenkung (gerade Leitung)"}
        },
        "example_calculation_de": {
            "scenario": "Spinnaker-Schot 300kg über 120°-Block",
            "calculation": "300 kg × 1.73 = 519 kg Gesamtlast auf Block",
            "required_block_swl": "519 kg × 2 (Sicherheitsfaktor Cruising) = 1038 kg WLL Block erforderlich"
        },
        "safety_factor_cruising": {"ratio": "2:1", "definition": "SWL = Breaking Load / 2", "note_de": "Standard für Fahrtensegler, Hochsee-Fahrt"},
        "safety_factor_racing": {"ratio": "1.5:1", "definition": "SWL = Breaking Load / 1.5", "note_de": "Nur für gut gepflegte, regelmäßig inspizierte Blocks"}
    },
    "bearing_types": {
        "ball_bearing": {
            "friction": "minimal (0.5-1% Energieverlust)",
            "load_capacity": "mittel (20-50 kN WLL pro Block)",
            "speed": "hoch (bis 1000 RPM typisch)",
            "maintenance": "gering (jährlich Fett-Prüfung)",
            "cost": "hoch",
            "application_de": "Standard für Schoten, Spinnaker, Fenderwerk",
            "material": "Chromstahl-Kugeln, Edelstahl-Käfig"
        },
        "roller_bearing": {
            "friction": "gering (2-3% Energieverlust)",
            "load_capacity": "hoch (bis 150 kN möglich)",
            "speed": "mittel (200-500 RPM max)",
            "maintenance": "etwas (halbjährlich Service)",
            "cost": "mittel",
            "application_de": "Hauptschot-Blöcke, schwere Lasten, Traveller-Wagen",
            "material": "Stahlrollen in Stahlkäfig"
        },
        "plain_bearing": {
            "friction": "hoch (5-8% Energieverlust)",
            "load_capacity": "sehr hoch (bis 200 kN Bruchlast)",
            "speed": "niedrig (max 100 RPM)",
            "maintenance": "regelmäßig (monatlich Fett/Öl nötig)",
            "cost": "niedrig",
            "application_de": "Schwerst-Lasten, Werft-Kräne, stationäre Befestigung",
            "material": "Bronze oder Kunststoff direkt auf Stahlachse"
        },
        "composite": {
            "friction": "sehr gering (0.2-0.5% Energieverlust)",
            "load_capacity": "mittel (bis 30 kN)",
            "speed": "sehr hoch (bis 2000 RPM)",
            "maintenance": "keine (wartungsfrei)",
            "cost": "mittel",
            "application_de": "Ultraleicht-Rigging, Racing, moderne Superyachten",
            "material": "Kunststoff-Composite (PTFE, Acetal) oder Polymer-Rollen",
            "note_de": "Kein Quietschen, kein Verschleiß, ideal für Dacron/Dyneema-Seile"
        }
    },
    "harken": {
        "philosophy": "Premium-Qualität, weltweit Standard in der Seglindustrie",
        "models": [
            {
                "model": "Midrange 76mm",
                "size_inch": 3,
                "swl_kg": 1043,
                "breaking_kg": 2086,
                "max_line_mm": 14,
                "bearing_type": "Ball Bearing (Kugellager)",
                "weight_kg": 0.65,
                "material": "Aluminium-Körper, 316 Edelstahl-Schäkel",
                "application": "Großschoten, Spinnaker-Blöcke auf 40-50 Fuß Yachten",
                "rating_swl_safety_factor": 2.0
            },
            {
                "model": "16mm Block",
                "swl_kg": 226,
                "breaking_kg": 452,
                "weight_g": 12,
                "material": "Mini-Composite-Block",
                "application": "Kleinere Abspannungen, Racing-Details"
            },
            {
                "model": "40mm Fly Block",
                "swl_kg": 652,
                "max_line_mm": 9,
                "bearing": "Ball Bearing",
                "application": "Jib-Blöcke, kompaktes Design",
                "weight_kg": 0.23
            },
            {
                "model": "High Load Snatch 3299",
                "swl_kg": 2300,
                "breaking_load_kg": 4600,
                "max_line_mm": 11,
                "bearing": "Roller Bearing (Walzenlager)",
                "weight_kg": 0.98,
                "feature": "Unidirektional (Schnelle Leine bevorzugt)"
            },
            {
                "model": "57mm Carbo Ratchamatic",
                "swl_kg": 907,
                "breaking_kg": 1814,
                "max_line_mm": 12,
                "bearing": "Ball + Composite Hybrid",
                "feature": "Ratchet-Funktion: freier Durchlauf in eine Richtung, blockiert in andere",
                "application_de": "Spinnaker-Freigabe unter Last — löst automatisch bei Richtungswechsel"
            }
        ]
    },
    "lewmar": {
        "philosophy": "Innovative Designs, häufig erste mit neuen Materialien",
        "models": [
            {
                "model": "Synchro 50mm",
                "swl_kg": 450,
                "weight_kg": 0.32,
                "bearing": "Ball Bearing",
                "application": "Kleine bis mittlere Schoten"
            },
            {
                "model": "Synchro 60mm Stand Up",
                "swl_kg": 800,
                "breaking_kg": 1600,
                "max_line_mm": 12,
                "material": "Composite-Körper (gewichtsoptimiert)",
                "feature": "Aufrechtes Design — sitzt auf Deck statt zu hängen"
            },
            {
                "model": "HTX 60mm",
                "swl_kg": 1100,
                "breaking_kg": 2200,
                "max_line_mm": 14,
                "bearing": "Hybrid-Lager (Ball + Composite)",
                "application": "Großschoten Motorsailer"
            },
            {
                "model": "Synchro 72mm Double",
                "swl_kg": 1100,
                "description": "Doppel-Block (zwei Rollen nebeneinander)",
                "application": "Flaschenzug-Systeme, doppelte Umlenk-Kapazität"
            },
            {
                "model": "Tweeker Control Snatch 40mm",
                "swl_kg": 140,
                "weight_g": 60,
                "feature": "Schnellspanner für Fein-Umlenk-Blöcke"
            },
            {
                "model": "Double Foot with Jammer 60mm",
                "swl_kg": 400,
                "feature": "Integrierte Klemme + Block (zwei Funktionen in einem)",
                "weight_kg": 0.45,
                "application": "Platzsparing auf kleinen Booten"
            }
        ]
    },
    "antal": {
        "philosophy": "Leichtgewicht-Racing-Spezialist",
        "models": [
            {
                "model": "80mm Mast Block",
                "swl_kg": 2200,
                "max_line_mm": 14,
                "length_mm": 162,
                "width_mm": 34.5,
                "height_mm": 62.5,
                "weight_kg": 0.68,
                "bearing": "Advanced Ball Bearing",
                "material": "CNC Aluminium-Casting",
                "application": "Mast-Block für Grand-Prix Regatta Yachten"
            },
            {
                "model": "40mm Snatch",
                "swl_kg": 700,
                "weight_kg": 0.10,
                "max_line_mm": 12,
                "application": "Ultra-leicht für Racing"
            }
        ]
    },
    "ronstan": {
        "philosophy": "Australischer Qualitäts-Hersteller, wartungsfreundliches Design",
        "orbit_series": [
            {
                "series": 20,
                "swl_kg": 250,
                "breaking_kg": 500,
                "weight_g": 9,
                "bearing": "2-Stage Composite Bearing",
                "application": "Dinghies, Optimist, leichte Boote"
            },
            {
                "series": 30,
                "swl_kg": 400,
                "breaking_kg": 800,
                "weight_g": 18,
                "bearing": "Ball Bearing",
                "application": "Sport-Kielboote, kleine Fahrtensegler"
            },
            {
                "series": 40,
                "swl_kg": 700,
                "breaking_kg": 1400,
                "max_line_mm": 10,
                "configurations": 23,
                "bearing": "Advanced Composite",
                "application": "Mainsheet / Spinnaker auf 25-35 Fuß Yachten",
                "weight_kg": 0.28,
                "features": ["Modularer Aufbau", "viele Halterungsvarianten"]
            }
        ],
        "product_feature": "Alle Blocks mit austauschbaren Verschleißteilen konstruiert"
    },
    "soft_blocks_dyneema": {
        "description_de": "Textil-Blöcke mit Dyneema/Spectra statt klassischer Schäkel",
        "inventor": "Entwickelt von Lewmar und Harken, now standard in moderne Rigging",
        "material": "UHMWPE (Ultra High Molecular Weight Polyethylene)",
        "properties": {
            "strength_vs_steel": "10× stärker bei gleichem Gewicht",
            "density_g_cm3": 0.97,
            "floats": True,
            "tensile_strength_gpa": 3.7,
            "modulus_of_elasticity_gpa": 70,
            "max_temp_celsius": 150,
            "softening_temp_celsius": 200,
            "stretch_percent": "3-5% bei Bruchlast (minimal)",
            "uv_stability": "Sehr gut (moderne UV-stabilisierte Varianten)",
            "color": "Goldgelb oder Blau (je nach Hersteller)"
        },
        "advantages_de": [
            "Leichter als Metallschäkel — halbiertes Gewicht typisch",
            "Einfacherer Blocktausch — keine Edelstahl-Verschraubung nötig",
            "Schwimmt — nicht verlorener Block bei Überboardfall",
            "Kein Verschleiß an Seile — Dyneema extrem glatt",
            "Ideal für Regatta-Boote — jedes Gramm zählt"
        ],
        "disadvantages": [
            "Nicht so robust gegen Beschädigungen wie Metall",
            "Fadenzug/Risse können Haltbarkeit gefährden",
            "Höherer Preis (2-3× teurer als Metall)",
            "Nicht reparierbar — kompletter Block-Austausch erforderlich"
        ],
        "maintenance": "Jährliche Sicht-Kontrolle auf Risse, unter UV-Schutz lagern"
    }
}


# ============================================================================
# KLAMPEN UND CAM-CLEATS — Cleats and Cam-Cleats
# ============================================================================

CLEAT_DATABASE: Dict[str, Any] = {
    "horn_cleats_overview": {
        "principle": "Zwei gehörnte Arme, Seil wird spiral-formig um die Hörner gewickelt",
        "load_capacity": "Abhängig von Material und Größe, typisch 500-2000 kg",
        "advantage": "Einfach, wartungsfrei, niemals Verschleiß-teile",
        "disadvantage": "Belastung ist handwerklich (Wickel-Technik), langsame Freigabe unter Last"
    },
    "horn_cleats_materials": {
        "bronze": {
            "type": "Massiv-Bronze (Cu-Sn Legierung, typisch 88% Cu / 12% Sn)",
            "corrosion_resistance": "excellent (besser als V4A in Salzwasser)",
            "weight": "heavy (15-20× leichter Kunststoff)",
            "aesthetic": "classic nautisch, glänzend grünlich-braun patina mit Zeit",
            "note_de": "Massiv-Bronze für Cockpit/Deck, beste Korrosionsbeständigkeit überhaupt",
            "maintenance": "Alle 12 Monate mit Weißbronze-Mittel aufpolieren",
            "cost_factor": 5.0,
            "density_g_cm3": 8.8,
            "breaking_load_typical": "4000-6000 kg (extrem robust)"
        },
        "stainless_316": {
            "type": "Austenitischer Edelstahl 316L (hochlegiert)",
            "corrosion_resistance": "very_good",
            "weight": "medium",
            "aesthetic": "modern, glänzend beständig",
            "note_de": "Goldstandard für Salzwasser, industrie-üblich",
            "maintenance": "Gelegentliches Polieren reicht",
            "cost_factor": 3.0,
            "density_g_cm3": 8.0,
            "breaking_load_typical": "2500-4000 kg"
        },
        "nylon": {
            "type": "Glasfaser-verstärktes Polyamid (PA6/PA66 + 30% Glasfasern)",
            "corrosion_resistance": "excellent (kein Rost möglich)",
            "weight": "very_light (1/5 von Edelstahl)",
            "aesthetic": "functional, schwarz oder blau",
            "note_de": "UV-stabilisiert, für leichtere Lasten, moderne Racing-Boote",
            "uv_stabilizer": "Carbon-schwarz oder spezielles UV-Absorber-System",
            "cost_factor": 1.5,
            "breaking_load_typical": "800-1500 kg",
            "maintenance": "Praktisch wartungsfrei"
        },
        "aluminum": {
            "type": "Druckgegossenes Aluminium (Al-Si-Mg Legierung)",
            "corrosion_resistance": "Mittel (anodisiert 316 Edelstahl-Befestigung nötig)",
            "weight": "light",
            "aesthetic": "Modern, silber",
            "cost_factor": 1.0,
            "breaking_load_typical": "1000-2000 kg",
            "note_de": "Nur mit Edelstahl-Hardware verwenden!"
        }
    },
    "horn_cleat_sizing": {
        "rule_of_thumb": "Klampenlänge (Horn zu Horn) = 1.5× bis 2× Taudurchmesser",
        "example_sizing": {
            "rope_4mm": {"cleat_length_mm_min": 60, "cleat_length_mm_max": 80},
            "rope_8mm": {"cleat_length_mm_min": 120, "cleat_length_mm_max": 160},
            "rope_12mm": {"cleat_length_mm_min": 180, "cleat_length_mm_max": 240},
            "rope_16mm": {"cleat_length_mm_min": 240, "cleat_length_mm_max": 320}
        },
        "oversizing_warning": "Zu große Klamps sind unpraktisch (Handgriff lang), aber sicherer"
    },
    "cam_cleats": {
        "harken_carbo_cam": {
            "description_de": "Leichtgewicht-Cam-Cleat aus faserverstärktem Composite (Karbon/Epoxid)",
            "mechanism": "Zwei federbelastete Nocken klemmen Leine unter Spannung zwischen sich",
            "cam_shape": "Exzentrische Nockenscheibe mit berechnetem Profil",
            "principle": "Je größer Last, desto fester Druck der Nocken (selbstverstärkender Effekt)",
            "features": [
                "Mehrreihige Kugellager für Nocken-Drehung",
                "V-Profil in Klemm-Zone reduziert Seil-Reibung",
                "Handgelenk-Snap Aktivierung — schnelle Freigabe mit Daumen möglich",
                "Federvorspannung einstellbar (Wartungsschrauben)"
            ],
            "max_line_mm": "8-12 (größenabhängig)",
            "weight_g": "35-65",
            "material": "Carbon-Epoxid-Composite (nicht metallisch)",
            "cost_factor": 3.0,
            "weight_advantage": "1/3 von Aluminium-Cleats"
        },
        "lewmar_ratchet_cam": {
            "description_de": "Innovative Ratchet-Funktion: automatische Einwegbremse",
            "mechanism": "Zahnkranz + Sperrklinke = blockiert Rückwärtslauf",
            "feature": "Kann Schote NICHT versehentlich auslaufen",
            "application": "Genua-Blöcke (Jib-Positionen), wo Rutsch-Sicherheit kritisch",
            "disadvantage": "Etwas höhere Reibung durch Zahnräder"
        }
    },
    "clamcleat": {
        "manufacturer": "Clamcleat Ltd. (UK)",
        "principle": "Gezahnte Oberflächen (Ober- und Unterklemme) greifen Leine mechanisch",
        "advantage": "Absolut wartungsfrei, keine beweglichen Teile",
        "models": [
            {
                "model": "CL282 Micros",
                "line_mm": "1-3",
                "material": "Kunststoff (Nylon) + Stahl-Zähne",
                "weight_g": 8,
                "application": "Abspannung, Fein-Einstellung auf Traveller",
                "cost": "niedrig"
            },
            {
                "model": "CL231",
                "line_mm": "4-8",
                "material": "Aluminium-Gehäuse",
                "weight_g": 25,
                "application": "Kompakte Schot-Führung, Racing-Details"
            },
            {
                "model": "CL228 mit Fairlead",
                "line_mm": "6-12",
                "material": "Nylon schwarz, Fairlead integriert",
                "weight_g": 45,
                "application": "Kontroll-Leinen, Traveller-Halter",
                "feature": "Verhindert Leine-Verdreh"
            }
        ],
        "clamcleat_principle": "Gezahnte Oberfläche greift Leine unter Last — je mehr Zug, desto fester Halt",
        "holding_power": "Theoretisch unbegrenzt bei Zahnform, praktisch abhängig von Seil-Material",
        "dyneema_warning": "Dyneema-Leinen können in Clamcleats rutschen — raue Zahnung nötig (CL228A-Variante)"
    }
}


# ============================================================================
# SCHIENEN UND LAUFWAGEN — Track and Car Systems
# ============================================================================

TRACK_SYSTEMS: Dict[str, Any] = {
    "t_track_fundamentals": {
        "inventor": "Harken, 1970er Jahre",
        "geometry": "T-Profil (Kopf oben, Stamm unten) ermöglicht Gleiter-Blöcke überall",
        "extruded_material": "Aluminium 6082-T6 (marine-grade)",
        "standard_sizes_mm": [22, 25, 27, 32],
        "market_penetration": "32mm ist de-facto-Industrie-Standard seit ~2000"
    },
    "t_track_sizes": {
        "22mm": {
            "boat_range_ft": "20-28",
            "boat_range_m": "6.7-8.5",
            "weight_per_meter_g": 520,
            "max_span_mm": 750,
            "swl_per_car_kg": 900,
            "typical_application": "Kleine Kielboote, Seegras-Charterboote"
        },
        "25mm": {
            "boat_range_ft": "24-32",
            "boat_range_m": "7.3-9.8",
            "weight_per_meter_g": 680,
            "max_span_mm": 850,
            "swl_per_car_kg": 1200,
            "typical_application": "Mittlere Segelyachten, moderne Mini-Yachten"
        },
        "27mm": {
            "boat_range_ft": "26-35",
            "boat_range_m": "7.9-10.7",
            "weight_per_meter_g": 750,
            "max_span_mm": 900,
            "swl_per_car_kg": 1500,
            "typical_application": "Übergangs-Größe, seltener verwendet"
        },
        "32mm": {
            "boat_range_ft": "34-46",
            "boat_range_m": "10.4-14.0",
            "weight_per_meter_g": 865,
            "max_span_mm": 900,
            "max_span_note": "Länger spannen nur mit Mitteltraveller-Auflager",
            "swl_per_car_kg": 2350,
            "typical_application": "Standard für Fahrtensegler + Racing, am weitesten verbreitet",
            "note_de": "Industrie-Standard, beste Verfügbarkeit Ersatzteile"
        }
    },
    "lewmar_32mm_detailed_specs": {
        "height_mm": 55,
        "width_mm": 32,
        "weight_per_m_g": 865,
        "max_span_between_fixings_mm": 900,
        "max_swl_car_kg": 2350,
        "moment_of_inertia_mm4": 19899,
        "second_moment_area_mm4": 19899,
        "fixing_bolt": "5/16 inch (M8)",
        "material": "Extrudiertes Aluminium 6082-T6",
        "surface_finish": "Klarglas-eloxiert oder Silber-eloxiert",
        "profile_shape": "T-Profil mit seitlichen Nut-Kanälen",
        "deflection_at_max_span_mm": 2.5,
        "young_modulus": "69 GPa (Aluminium Standard)"
    },
    "mainsheet_traveller_systems": {
        "purchase_ratio_3_to_1": {
            "description": "3 m Schote für 1 m Wagen-Bewegung",
            "mechanical_advantage": 3.0,
            "control_line_load_percent_of_wagen": "20-25%",
            "advantage": "Genaues Trimmen, niedriger Kontroll-Kraft",
            "disadvantage": "Langsame Wagen-Bewegung"
        },
        "purchase_ratio_4_to_1": {
            "description": "4 m Schote für 1 m Wagen-Bewegung",
            "mechanical_advantage": 4.0,
            "control_line_load_percent": "15-20%",
            "advantage": "Sehr präzise Kontroll-Leinen",
            "disadvantage": "Viel Seil erforderlich"
        },
        "purchase_ratio_6_to_1": {
            "description": "Seltene Racing-Ausführung",
            "mechanical_advantage": 6.0,
            "control_line_load_percent": "10-15%",
            "advantage": "Minimal-Kraft Traveller-Einstellung",
            "disadvantage": "Extrem lange Kontroll-Leine"
        },
        "example_calculation": {
            "boat": "11 Meter Fahrtensegler",
            "mainsheet_load_kg": 160,
            "traveller_wagen_load_kg": 160,
            "control_line_load_with_4_to_1": "160 kg / 4 = 40 kg Kontroll-Kraft",
            "control_line_diameter_mm": 10,
            "note_de": "Realistisch ~20% mehr Kraft nötig wegen Reibung, also ~48 kg effektiv"
        }
    },
    "traveller_car_types": {
        "ball_bearing_car": {
            "description": "Kugellagereinsätze unter/oben, Standard seit 1995",
            "advantage": "Reibungsarm, einfacher Betrieb",
            "bearing_count": 4,
            "friction_percent": "3-5% Energieverlust"
        },
        "roller_car": {
            "description": "Gewalzte Stahlrollen, alter Standard",
            "advantage": "Sehr robust, kann extrem überlastet werden",
            "disadvantage": "Höhere Reibung (10-15% Energieverlust)",
            "wear_characteristic": "Rauhe Rollen-Oberfläche mit Zeit"
        }
    }
}


# ============================================================================
# LUKEN UND FENSTER — Hatches and Portlights
# ============================================================================

HATCH_DATABASE: Dict[str, Any] = {
    "hatch_basics": {
        "purpose": "Belüftung + Licht + Zugang zu Innenräumen, MUSS wetterdicht sein",
        "failure_mode": "Wasser-Eindringung während Fahrt in See-Bedingungen",
        "critical_factor": "Dichtung + korrekte Montage in Sandwich-Kern mindestens 80% des Undicht-Ursachen"
    },
    "lewmar": {
        "manufacturer": "Lewmar Limited (Southampton, UK)",
        "ranges": {
            "low_profile": {
                "height_above_deck_mm": 20,
                "acrylic_thickness_mm": 8,
                "opening_angle": 180,
                "friction_lever_angle": 95,
                "frame": "Klarglas-eloxiertes Aluminium",
                "sizes": ["S", "M", "L", "XL"],
                "note_de": "Standard für Fahrtensegler, bewährt und zuverlässig seit 1990er",
                "installation": "Decksmontage mit Sandwich-Einsatz und Sikaflex"
            },
            "ultra_low_profile": {
                "height_above_deck_mm": 10,
                "acrylic": "Rauchgrau 8mm",
                "acrylic_benefit": "Verhindert Innenraum-Hitze im Hafen (UV-Reduktion 60%)",
                "frame": "Silber-eloxiertes Aluminium oder Edelstahl 316",
                "note_de": "Flush-Design für moderne, niedrig-profilierte Boote",
                "aesthetic": "Hochwertig, saubere Linien"
            },
            "ocean": {
                "description_de": "Hochsee-tauglich, verstärkte Konstruktion, Acryl 10mm",
                "certification": "CE Design Category A / Area 2 (Weltmeere)",
                "feature": "Druck-Ausgleichs-Ventil (verhindert Druckaufbau bei Temperatur-Änderung)",
                "mounting": "Verstärkte Edelstahl-Flansch-Ummantelung"
            }
        }
    },
    "goiot": {
        "manufacturer": "Goiot Systems S.A. (Frankreich, seit 1993)",
        "origin": "Französische Qualität, verwendet auf vielen französischen Yachten",
        "ranges": ["Tradition", "Cristal", "Opal", "Integration", "Escape Hatches", "Flush-mount"],
        "feature_de": "Einstellbare Reibungsscharniere — keine Stützarme nötig (Gasdruckfedern)",
        "typical_range": {
            "tradition": "Klassisch, robust, bekannt",
            "cristal": "Modern, größeres Licht, gutes Aussehen",
            "opal": "Premium, ultraflach, sehr hochwertig"
        },
        "opal_specs": {
            "height_mm": 15,
            "monoblock_frame": "Einteilig gegossen (kein Verschrauben)",
            "reversible_counterglass": "Acryl-Gegenscheibe austauschbar ohne Werkzeug",
            "wall_thickness_range_mm": "5-33mm automatische Anpassung"
        }
    },
    "bomar": {
        "manufacturer": "Bomar (USA, seit 1958)",
        "origin": "Amerikanischer Standard, vor allem auf US-Booten",
        "models": [
            {
                "series": 1000,
                "type": "Low-Profile Standard",
                "size_mm": "273 × 273",
                "weight_kg": 1.2
            },
            {
                "series": 7000,
                "type": "Low-Profile A (moderne Version)",
                "size_mm": "310 × 208",
                "height_mm": 22
            },
            {
                "series": 900,
                "type": "Large Hatch",
                "size_mm": "429 × 429",
                "weight_kg": 2.8
            },
            {
                "series": 2000,
                "type": "High-Profile (für große Übersicht)",
                "features": [
                    "Heavy-Duty Extruded Aluminium Rahmen",
                    "Quick-Acting Tie-Down Dogs (schnelle Verriegelung)",
                    "Verriegelbare Lüftungsstellung (bleibt offen ohne Hände halten)"
                ],
                "height_mm": 60
            }
        ]
    },
    "mounting_sandwich_deck": {
        "critical_procedure": "Kernmaterial im Montagebereich KOMPLETT entfernen und durch festen Einsatz ersetzen",
        "reason": "Kernmaterial (Balsa, Schaum) nimmt Wasser auf → Delamination → Strukturschaden",
        "core_types_problematic": ["Balsa-Holz (quillt in Wasser auf)", "PVC-Schaum (weniger schlimm)", "Polyurethan-Schaum (auch problematisch)"],
        "insert_materials": [
            {"material": "Festes Epoxid/Glasfaser-Laminat (Kern-Replacement)", "strength": "original"},
            {"material": "Marine-Sperrholz (Balsaflieg-Qualität)", "strength": "80% original"},
            {"material": "Edelstahl-Platte (nur für größte Belastungen)", "strength": "120% original"}
        ],
        "backing_plate_requirements": {
            "material_options": ["6mm eloxiertes Aluminium", "3-lagiges Epoxid-Sperrholz"],
            "max_hull_thickness_mm": 34,
            "important_note_de": "Schnittkanten des Kernmaterials MÜSSEN mit Epoxid versiegelt sein — Verhindert Wassereinbruch in Kernmaterial!",
            "sealing_material": "Dickflüssiges Epoxid (z.B. WEST-System mit Microfibers)",
            "sealing_application": "Alle Schnitt-Kanten, auch unter Dichtung"
        },
        "installation_steps": [
            "1. Hatch-Öffnung mit Band abkleben",
            "2. Kernmaterial ausfräsen (oder mit Dremel+ Spachtel entfernen)",
            "3. Hohlraum mit verdicktem Epoxid füllen — vollständig auffüllen",
            "4. Insert-Platte einlegen, ausrichten",
            "5. Epoxid aushärten (je nach System 24-48h)",
            "6. Oberflächenschliff, Bohrungen markieren",
            "7. Dichtungsmaterial (Sikaflex 295 UV) auftragen",
            "8. Hatch-Rahmen positionieren und verschrauben"
        ]
    },
    "sealing_gasket_materials": [
        {
            "type": "EPDM Schwammgummi",
            "properties": "Nicht verblassend, nicht schrumpfend, nicht reißend (mit der Zeit)",
            "lifespan_years": "12-15",
            "compression_setability": "Gering",
            "uv_stability": "Sehr hoch",
            "cost": "niedrig",
            "note_de": "Industrie-Standard für Originalausstattung Yachten"
        },
        {
            "type": "Silikon ZZR-765",
            "properties": "Temperaturbeständig (bis 200°C), wasserdicht",
            "lifespan_years": "15-20",
            "uv_stability": "Hervorragend",
            "cost": "mittel",
            "disadvantage": "Schwierig zu kleben, nicht überall in Nuten verwendbar"
        },
        {
            "type": "Neopren Thermoplast",
            "properties": "Haltbar, flexibel bei Extremtemperaturen (-40 bis +80°C)",
            "lifespan_years": "10-12",
            "cost": "mittel",
            "note_de": "Gute Balance zwischen Preis und Leistung"
        }
    ],
    "gasket_compression_spec": {
        "optimal_percent": 25,
        "optimal_definition": "25% Kompression der ursprünglichen Höhe (z.B. 5mm Dichtung comprimiert auf 3.75mm)",
        "acceptable_range_percent": "25-40%",
        "too_little_compression_percent": "< 15% - undicht",
        "too_much_compression_percent": "> 50% - Dauerschaden der Dichtung",
        "measurement_method": "Mit Schieblehre messen, ODER mit Bleistift-Markierungen vor/nach"
    },
    "bonding_adhesives_for_gaskets": [
        {
            "product": "Loctite Super Bonder 495",
            "application": "Gasket-Befestigung am Rahmen",
            "cure_time_minutes": 30,
            "advantage": "Schnelle Klebung, geruchsarm"
        },
        {
            "product": "3M Peel-N-Stick (oder ähnliche Kontakt-Klebstoffe)",
            "application": "Pre-bonded Gaskets (werksseitig laminiert)",
            "advantage": "Erspart Kleber-Auftrag vor Ort"
        },
        {
            "product": "Sikaflex 221 (polyurethane Klebstoff)",
            "application": "Hybrid-Dichtung + Kleber in einem",
            "cure_time_hours": 24,
            "advantage": "Sehr flexible Endigung, auch feuchte Flächen tolerable"
        }
    ]
}

PORTLIGHT_DATABASE: Dict[str, Any] = {
    "portlight_basics": {
        "purpose": "Fenster in Rumpf oder Aufbau, muss absolut wetterdicht sein",
        "failure_modes": [
            "Dichtungs-Alterung (Gummi wird spröde)",
            "Ungleichmäßige Kompression beim Verschrauben",
            "Acryl-Kratzer (entstehen mit Jahren)",
            "Bonding-Fehler (Dichtung nicht vollständig geklebt)"
        ],
        "inspection_interval_months": 12
    },
    "lewmar_portlights": {
        "frame_material": "Eloxiertes Aluminium (natürlich oder silber)",
        "lens_material": "Rauchgraues Acryl (8mm standard, 10mm optional)",
        "interior_component": "ABS-Kunststoff mit Insektenschutz-Netz (optional)",
        "fastener_spec": "12× M5 25mm Edelstahl Schrauben (vollständig rostfrei)",
        "hull_thickness_range_standard_mm": "7-25",
        "hull_thickness_range_max_mm": 34,
        "surface_tolerance_during_installation_mm": 1,
        "ce_certification": "Design Category A / Area 2 (Weltmeere erlaubt)",
        "standard_models": [
            {"name": "Standard", "price_factor": 1.0, "size": "200×200mm - 400×400mm"},
            {"name": "Atlantic", "price_factor": 1.2, "description": "Robuster, thickwall"},
            {"name": "Edelstahl", "price_factor": 1.8, "material": "316 Edelstahl statt Aluminium"},
            {"name": "Flush Mitre", "price_factor": 1.5, "description": "Bündig-Montage, kein Rand sichtbar"}
        ],
        "opening_positions": "4 feste Öffnungspositionen (Quick-Stop Scharniere)",
        "opening_angles": ["0° (geschlossen)", "20° (Lüftung)", "45° (Belüftung)", "90° (offen)"],
        "installation_flange": "Außen-Flansch 40×40mm (von Rumpf sichtbar)"
    },
    "goiot_portlights": {
        "luxair_line": {
            "description": "Direkt in 12 oder 15mm Acryl-Glas integriert, vormontiert",
            "advantage": "Keine separate Dichtung nötig, einteiliges Fenster",
            "size": "Auf Maß konfigurierbar bis 1000×500mm",
            "material": "Acryl 12-15mm Mono-Block"
        },
        "opal_line": {
            "description": "Monoblock-Rahmen, reversibler Gegenrahmen, wandstärke-adaptiv",
            "feature": "Wandstärke-Erkennung von 5-33mm automatisch",
            "frame": "Komplettes Edelstahl optional",
            "opening": "Verschiedene Öffnungs-Mechaniken möglich"
        }
    },
    "glazing_materials_comparison": {
        "acrylic_pmma": {
            "scratch_resistance": "hoch (5x kratzfester als Polycarbonat)",
            "uv_durability": "hervorragend (PMMA ist UV-stabil)",
            "breakage_risk": "höher als Polycarbonat (scharfe Bruchstücke)",
            "thermal_expansion": 0.000039,
            "thermal_expansion_note": "35-39 ppm/K typisch",
            "note_de": "Industriestandard für Hochsee/Blauwasser. Kratzfester, deutlich bessere UV-Beständigkeit.",
            "lifespan_years": "25-35",
            "cost_factor": 1.0,
            "density_g_cm3": 1.19,
            "refractive_index": 1.49,
            "light_transmission_percent": 92
        },
        "polycarbonate": {
            "scratch_resistance": "niedrig (bekommt Kratzer leicht)",
            "uv_durability": "niedrig (UV-empfindlich, vergilbt nach 5-10 Jahren)",
            "breakage_risk": "sehr niedrig (praktisch unzerbrechlich)",
            "thermal_expansion": 0.000039,
            "note_de": "Bruchfester, aber vergilbt und trübt schneller. Dichtungsversagen häufiger.",
            "lifespan_years": "8-15 (Vergilbung)",
            "cost_factor": 1.5,
            "density_g_cm3": 1.20,
            "advantage": "Absolut schlagfest",
            "uv_absorption": "Rapid bei direkter Sonneneinstrahlung"
        },
        "tempered_glass": {
            "scratch_resistance": "sehr hoch (Glas ist härtester Material)",
            "uv_durability": "sehr hoch",
            "breakage_risk": "zersplittert in kleine Krümel (sicher, kein Risiko)",
            "thermal_expansion": "niedrig",
            "note_de": "Premium-Option für Deckssalons und Superyachten. Schwer (3x Acryl).",
            "lifespan_years": "50+ (praktisch unbegrenzt)",
            "cost_factor": 5.0,
            "density_g_cm3": 2.50,
            "breakage_safe": True,
            "disadvantage": "Spiegelt Licht (8% Reflektion), sehr schwer für Rahmen"
        }
    },
    "sealing_methods_detailed": {
        "gasket_seal": {
            "description_de": "Gummi-/EPDM-Dichtung in Rahmennut (klassisches System)",
            "composition": "EPDM Schwammgummi, typisch 4-6mm Profil",
            "advantage": "Austauschbar, nachstellbar, günstig",
            "disadvantage": "Altert nach 10-15 Jahren, muss erneuert werden",
            "installation": "Dichtung in Nut quetschen, Gegenseite verschrauben",
            "maintenance": "Alle 5 Jahre Dichtung checken (drücken — sollte federnd zurückgehen)"
        },
        "bonded_seal": {
            "description_de": "Acryl/Glas mit Sikaflex/3M direkt in Rahmen geklebt",
            "bonding_process": "Raum zwischen Fenster und Rahmen vollständig mit Klebstoff gefüllt",
            "advantage": "Absolut dicht, keine Alterung der Dichtung, wartungsfrei",
            "disadvantage": "Nicht nachstellbar, Austausch schwieriger (muss komplett demontiert)",
            "lifespan_years": "30+",
            "sealants_suitable": [
                {"product": "Sikaflex 295 UV", "cure_time_hours": 24, "flexibility": "sehr hoch"},
                {"product": "3M 4000UV", "cure_time_hours": 36, "flexibility": "mittel"},
                {"product": "Dow Corning 795", "cure_time_hours": 48, "flexibility": "sehr hoch"}
            ],
            "installation_requirement": "Glasfläche absolut sauber und trocken"
        }
    },
    "installation_hull_preparation": {
        "surface_preparation": "Oberfläche schleifen (Körnung 120) — entfernt alte Dichtung und Lack",
        "primer_application": "Epoxid-Grundierung auftragen (2 Schichten, 200 g/m²)",
        "frame_seating": "Rahmen provisorisch positionieren",
        "gasket_installation": "Dichtung einsetzen, Spannschrauben diagonal anziehen (1/4-Umdrehung abwechselnd)"
    }
}


# ============================================================================
# RELINGS UND SEERELING — Stanchions and Lifelines
# ============================================================================

STANCHION_LIFELINE_DATABASE: Dict[str, Any] = {
    "railing_function": "Personen-Sicherung an Deck, obligatorisch nach Internationalen Regeln",
    "safety_standard": "ISO 14431-1:2012 (Internationale Sicherheitsnorm für Geländer auf Yachten)",
    "stanchion_bases_overview": {
        "fixed": {
            "description_de": "Permanent auf Deck montiert, 5-Zoll (127mm) Stahlflansch",
            "mounting": "Verschraubt durch Deck, Unterlegscheibe innen",
            "cost": "niedrig",
            "weight": "schwer",
            "flexibility": "Null",
            "breakage_risk": "Null (wenn korrekt montiert)"
        },
        "toggle": {
            "description_de": "Flexibel, ~10° Neigung möglich, 350° Rotation",
            "mounting": "Eingelenk-Verbindung mit Federgelenk",
            "cost": "mittel",
            "flexibility": "Hoch (nachgiebig bei Druck)",
            "advantage": "Fender-Schutz (Relings absorbieren Dock-Kontakt)",
            "disadvantage": "Mit Zeit Spiel entwickeln (ölbar mit 3-in-1 Öl)"
        },
        "removable": {
            "description_de": "Stecksockel mit Federverriegelung, komplett entfernbar",
            "mounting": "Sockel fest, Stanchion-Rohr wird eingesteckt",
            "cost": "hoch",
            "flexibility": "Mittel (Spiel ist Verschleiß-Eigenschaft)",
            "advantage": "Entfernbar für Decksspüligung, Kunstharz-Arbeit",
            "disadvantage": "Teuer, komplexer zu montieren, mit Zeit lockerer"
        }
    },
    "stanchion_height_requirements": {
        "minimum_iso_mm": 600,
        "minimum_iso_inch": 24,
        "minimum_iso_definition": "Mindesthöhe über Arbeitsdeck",
        "recommended_mm": 750,
        "recommended_definition": "Empfohlen für Hochsee-Fahrt, besserer Personen-Schutz",
        "regulatory_requirement_ft_loa": "Ab 28 Fuß (8.5m Länge) obligatorisch mindestens 600mm",
        "typical_spacing_mm": 1500,
        "typical_spacing_note": "Maximal 1.5m Abstände zwischen Stanchions (ISO-Forderung: max 2m)"
    },
    "lifeline_materials_detailed": {
        "stainless_wire_1x19": {
            "material": "1×19 Flechtweise (19 Drähte in 1 Lage) V4A Edelstahl 316L",
            "wire_diameter_mm": "2-4mm typisch",
            "breaking_strength_3mm_kg": 1200,
            "lifespan_years": "10-15",
            "note_de": "Traditionell, rostfrei, nicht UV-empfindlich, schwer (1.85 g/m/1mm)",
            "disadvantage": "Scharfe Kanten wenn beschädigt, schwer zu spleißen",
            "cost": "mittel",
            "maintenance": "Jährlich mit feiner Stahlbürste abbürsten, Whitespirit",
            "tensioning": "Mit Spannschrauben, Nachspannung alle 6 Monate"
        },
        "dyneema_uhmwpe": {
            "material": "UHMWPE 12-Fach geflochten (Dyneema oder Spectra)",
            "diameter_mm": "5-8mm äquivalent zu Draht",
            "breaking_strength_6mm_kg": 2000,
            "lifespan_years": "8-12",
            "note_de": "10× stärker als Stahl bei gleichem Gewicht, kein Rost, spleißbar",
            "advantage": "Leicht, schwimmt, kann bei Beschädigung überknotet werden",
            "disadvantage": "UV-empfindlich (muss unter Verwendung gebündelt sein)",
            "cost": "hoch",
            "tensioning": "Identer zu Draht, Nachspannung aber weniger nötig (Elastizität)",
            "spleißing": "Möglich, erfordert Spezialistenschiff für reparaturfreundlichkeit"
        },
        "pvc_coated_wire_7x7": {
            "material": "PVC-ummantelt 7×7 Flechtweise Stahlseile",
            "breaking_strength_4mm_kg": 800,
            "lifespan_years": "5-10",
            "note_de": "VORSICHT: Korrosion UNTER dem PVC nicht sichtbar! PVC-Risse ermöglichen Wasser-Eindring",
            "disadvantage": "Rostet unsichtbar unter Mantel, teuer bei Austausch nötig",
            "cost": "mittel-hoch",
            "not_recommended_reason": "Moderne Segler bevorzugen Dyneema oder bloßen Draht"
        }
    },
    "pelican_hooks": {
        "material": "316L Edelstahl, Präzisionsguss",
        "breaking_strength_kn": 17,
        "max_working_load_kn": 15,
        "mechanical_function": "Hebel-Mechanismus sperrt bei Abzug, löst bei Druck",
        "critical_note_de": "NIEMALS für stehendes Gut verwenden! Nur für Seereling-Gates (Durchgänge).",
        "lifetime_years": "Unbegrenzt (Metall), aber Gelenk-Spiel entwickelt sich",
        "use_case": "Gates in Seereling zum Betreten/Verlassen von Badeplattform",
        "maintenance": "Jährlich mit 3-in-1-Öl schmieren"
    }
}


# ============================================================================
# PAD EYES UND BEFESTIGUNGSPUNKTE — Pad Eyes and Attachment Points
# ============================================================================

PAD_EYE_DATABASE: Dict[str, Any] = {
    "pad_eye_function": "Lokalisierter Befestigungspunkt für Schoten, Seile, Abspannungen",
    "load_bearing_principle": "Gesamte Last verteilt sich auf Unterlage (Pad) unter Flansch",
    "critical_success_factor": "Unterlegplatte (Backing Plate) muss Last verteilen über große Fläche",
    "wichard_specifications": [
        {
            "diameter_mm": 4,
            "breaking_load_kg": 1000,
            "working_load_kg": 480,
            "material": "316L Edelstahl",
            "eye_height_mm": 15,
            "pad_diameter_mm": 20,
            "cost_factor": 1.0
        },
        {
            "diameter_mm": 5,
            "breaking_load_kg": 1800,
            "working_load_kg": 800,
            "material": "316L",
            "eye_height_mm": 19,
            "pad_diameter_mm": 25,
            "cost_factor": 1.3
        },
        {
            "diameter_mm": 6,
            "breaking_load_kg": 3000,
            "working_load_kg": 1280,
            "material": "316L",
            "length_mm": 70,
            "eye_height_mm": 22,
            "pad_diameter_mm": 30,
            "cost_factor": 1.8
        },
        {
            "diameter_mm": 8,
            "breaking_load_kg": 5000,
            "working_load_kg": 2200,
            "material": "316L",
            "eye_height_mm": 28,
            "pad_diameter_mm": 40,
            "cost_factor": 3.2
        },
        {
            "diameter_mm": 10,
            "breaking_load_kg": 8000,
            "working_load_kg": 3500,
            "material": "316L",
            "eye_height_mm": 35,
            "pad_diameter_mm": 50,
            "cost_factor": 5.0
        }
    ],
    "safety_calculation": {
        "safety_factor_standard": 5,
        "safety_factor_definition": "WLL = Bruchlast / 5",
        "example": {
            "pad_eye": "6mm Wichard",
            "breaking_load_kg": 3000,
            "safety_factor": 5,
            "working_load_limit_kg": 600,
            "practical_load_kg": 1280,
            "note": "Praktisch-Wert ist großzügiger, aber 5:1 ist Standard"
        }
    },
    "backing_plate_solid_grp": {
        "requirement": "19mm Marine-Sperrholz Klasse A — KEIN Massivholz (reißt entlang der Maserung)",
        "plywood_type": "3 Schichten, Fagott + Buche (alternativ Meranti)",
        "reason_no_solid": "Massivholz entwickelt Spaltrisse radial → Befestigung wird locker",
        "installation": "Sperrholz-Platte unter Flansch lagern, mit Schrauben zusammenpresst"
    },
    "backing_plate_sandwich": {
        "material_options": [
            {"option": "16mm G-10 (Glasfaser-Composite)", "strength_vs_plywood": "60% stärker", "cost": "höher"},
            {"option": "16mm Marine-Sperrholz", "strength": "Referenz (100%)", "cost": "niedrig"},
            {"option": "GPO-3 (Glasfaser-gefülltes Phenolharz)", "strength": "ähnlich G-10", "cost": "mittel"}
        ],
        "no_metallic_only_reason": "Metall-Platte würde Galvanische Korrosion im Laminat verursachen"
    },
    "mounting_in_sandwich_procedure": {
        "step_1": "Kernmaterial im Befestigungsbereich entfernen (Kreis 15-20cm größer als Beschlag-Fußabdruck)",
        "step_1_method": "Oder mit heißem Lüftungskanal (Balsa quillt und kommt raus), oder Dremel mit Spachtel",
        "step_2": "Hohlraum mit verdicktem Epoxid (+ Colloidal Silica) füllen und aushärten lassen",
        "step_2_alternative": "ALTERNATIV: Massiv-Insert aus G-10 oder Sperrholz einharzen, dann auf Höhe schleifen",
        "step_3": "Bohren und Beschlag montieren mit Edelstahl-Schrauben",
        "step_4_critical": "JEDE Bohrung muss mit Epoxid versiegelt sein — Wasser im Kern = Katastrophe!",
        "seal_method": "Nach Bohren Epoxid um Schrauben-Loch auftragen"
    },
    "example_calculation": {
        "scenario": "Spinnaker-Auslöser-Pad Eye auf Traveller-Decksrahmen",
        "load": "150 kg Spinnaker-Schot + Umlenkung",
        "pad_eye_required": "8mm Wichard (WLL 2200 kg, 5:1 Sicherheit)",
        "backing_plate": "16mm G-10 Composite (25×25 cm)",
        "note_de": "Sperrholz-Insert muss fest in Rumpf verankert sein — nicht 'locker' in Kernmaterial sitzen"
    }
}


# ============================================================================
# ERSATZTEIL- UND WARTUNGS-MATRIX
# ============================================================================

MAINTENANCE_MATRIX: Dict[str, Any] = {
    "winches": {
        "inspection_interval_months": 6,
        "service_interval_months": 12,
        "heavy_use_service_months": 3,
        "grease_type": "Lithium-Complex NLGI-Grade 2 oder marine-spezifisch",
        "grease_change_volume_ml": {"size_40": 150, "size_50": 200, "size_60": 250},
        "critical_checkpoints": [
            "Getriebefett-Farbe und Konsistenz (dunkel = Verschleiß-Metallteilchen)",
            "Trommeldrehung ohne Last (sollte 5+ Umdrehungen frei rollen)",
            "Self-Tailing Zahn-Griff (kein Slip unter normaler Last)",
            "Kugellager-Axialspiel prüfen (max. 2mm Spiel akzeptabel)"
        ]
    },
    "blocks": {
        "inspection_interval_months": 3,
        "visual_checks": [
            "Rollen auf Kratzer/Risse prüfen (besonders composite)",
            "Achse auf Verschleißmarken kontrollieren",
            "Lager-Käfig auf Verformung prüfen",
            "Gehäuse-Risse oder Bruchstücke"
        ],
        "bearing_lubrication": {
            "grease_type": "Leichte Scheerfestigkeit (NLGI 1) für hohe Drehzahlen",
            "application": "Jährlich 2-3 Tropfen neben Achse, lass auslaufen und trocknen"
        }
    },
    "cleats": {
        "inspection_interval_months": 12,
        "checks": [
            "Klampen: Horn auf Risse prüfen (besonders bei Bronze)",
            "Cam-Cleats: Sperrklinken-Bewegung und Feder-Spiel prüfen",
            "Clamcleats: Zahn-Profil auf Verschleiß kontrollieren"
        ],
        "maintenance": "Jährliches Polieren (Bronze-Klampen) oder Schmieren (Cam-Lager)"
    },
    "track_and_cars": {
        "inspection_interval_months": 6,
        "checks": [
            "T-Profil auf Verformung prüfen (besonders Kopf)",
            "Wagen-Rollen auf Verschleißflecken kontrollieren",
            "Kugellager-Spiel prüfen (sollte glatt rollen, kein Rattern)",
            "Befestigungsschrauben auf Lockerheit prüfen (jährlich anziehen)"
        ],
        "lubrication": {
            "material": "Marine-Schmierspray (PTFE-haltig) oder leichtes Maschinenöl",
            "frequency": "Monatlich bei Hochseeeinsatz, quartalsweise sonst"
        }
    }
}


# ============================================================================
# QUALITÄTS- UND HERKUNFTS-MATRIX
# ============================================================================

QUALITY_AND_ORIGIN_MATRIX: Dict[str, Any] = {
    "manufacturer_origins": {
        "usa": {
            "companies": ["Harken Inc.", "Bomar (Connecticut)", "Lewmar (USA-Tochter)"],
            "characteristics": "Hohe Qualität, Innovation, höherer Preis"
        },
        "uk": {
            "companies": ["Lewmar Limited", "Ronstan", "Spinlock"],
            "characteristics": "Traditionelle Qualität, bewährte Designs"
        },
        "dänemark": {
            "companies": ["Andersen Winches"],
            "characteristics": "Skandinavische Genauigkeit, Edelstahl-Philosophie"
        },
        "frankreich": {
            "companies": ["Antal", "Goiot Systems"],
            "characteristics": "Präzisions-Konstruktion, leichtgewichtig"
        },
        "italien": {
            "companies": ["Harken Italia (Genua)"],
            "characteristics": "Lokale Produktionsstätte, schnelle Verfügbarkeit EU"
        }
    },
    "price_vs_quality_guidance": {
        "budget_tier": {
            "price_range": "EUR 500-1500 Winsch",
            "manufacturers": "Unbekannte Marken, Aliexpress, knockoffs",
            "reliability": "Niedrig, Ersatzteil-Beschaffung schwierig",
            "recommendation": "Nicht für Hochsee-Fahrt"
        },
        "mid_tier": {
            "price_range": "EUR 1500-3500 Winsch",
            "manufacturers": ["Antal", "Lewmar Evo", "Spinlock Evo"],
            "reliability": "Gut, Ersatzteile verfügbar",
            "recommendation": "Gut für Fahrtensegler"
        },
        "premium_tier": {
            "price_range": "EUR 3500-8000 Winsch",
            "manufacturers": ["Harken Radial", "Andersen ST", "Lewmar LS"],
            "reliability": "Ausgezeichnet, Weltweite Unterstützung",
            "recommendation": "Racing und anspruchsvolle Hochsee"
        }
    }
}


# ============================================================================
# INSTALLATION BEST PRACTICES
# ============================================================================

INSTALLATION_BEST_PRACTICES: Dict[str, Any] = {
    "deck_hardware_mounting": {
        "core_principle": "Last MUSS verteilt werden — nie konzentriert auf einen Punkt",
        "sandwich_deck_standard": {
            "identify_location": "Ultraschall-Messung oder Kernbohrung zur Schichtdicken-Bestimmung",
            "remove_core": "Kernmaterial 50mm größer als Beschlag-Footprint entfernen",
            "fill_core": "Mit verdicktem Epoxid (Colloidal Silica) auffüllen — Schwammkern DARF bleiben",
            "backing_approach": "6mm Alu-Platte oder 3-ply Sperrholz unter Beschlag lagern",
            "fastener_selection": "Edelstahl-Schrauben mit Unterlegscheiben (minimale 12mm Durchmesser)",
            "loctite_application": "Threadlocker Loctite 243 (mittlere Stärke) auf Gewinde auftragen"
        },
        "solid_fiberglass": {
            "surface_prep": "Oberflächen-Versiegelung (Lack/Epoxid) mit Körnung 120 schleifen",
            "fastener": "Edelstahl-Schrauben mit großer Unterlegscheibe",
            "sealant": "Sikaflex 295 UV rund um Schrauben"
        }
    },
    "rigging_installation": {
        "wire_rigging": {
            "turnbuckles": "Stainless-Spannschrauben, Gewinde-Sperrlack",
            "swaging": "Quetschen statt Knotenband für permanente Installation",
            "testing": "Nach Quetschung mit Zugprüfmaschine testen (mindestens 5× Bruchspannung)"
        },
        "tensioning": "Mit Dynamometer (Zugspannungs-Messgerät), nicht 'Gefühl'"
    },
    "electrical_integration": {
        "electric_winch_power": {
            "12v_installations": "Dicke Kabel (16-25 mm²) mit Sicherung nächst zur Batterie",
            "24v_installations": "Dünnere Kabel möglich (10-16 mm²), sauberer",
            "voltage_drop_max_percent": 3,
            "installation_note": "Alle Kabel in Leerrohren, NOT unter Deck (Hitzestau)"
        }
    }
}
