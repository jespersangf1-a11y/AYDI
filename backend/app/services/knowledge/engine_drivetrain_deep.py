"""
AYDI Motor, Antrieb & Steuerung — Tiefenwissen
Exhaustive technical knowledge on marine diesel engines, shaft systems,
saildrives, propellers, and steering systems.

This module provides comprehensive German-annotated technical specifications,
failure modes, maintenance intervals, and repair procedures for marine diesel
propulsion systems. Data compiled from OEM documentation, field experience,
and industry standards.

Author: AYDI Research Team
Version: 1.0
License: Internal Use
"""
from typing import Dict, Any


ENGINE_DATABASE: Dict[str, Any] = {
    "description_de": "Umfassende Datenbank von Dieselmotoren für Schiffe: Typen, Hersteller, Spezifikationen",
    "types": {
        "naturally_aspirated": {
            "description_de": "Saugmotoren ohne Turbolader - einfache, zuverlässige Konstruktion",
            "key_characteristics_de": {
                "intake_method_de": "Natürliche Ansaugung ohne Verdichtung",
                "reliability_de": "Legendär - weniger bewegliche Teile, niedrigere Betriebstemperaturen",
                "complexity_de": "Minimal - robust gegen Wartungsverzögerungen",
                "lifespan_hours_de": "15000-20000 Betriebsstunden typisch",
                "overhaul_life_de": "8000-12000h zwischen Überholungen",
                "fuel_consumption_de": "Höher als Turbo - 0.25-0.35 l/kWh",
                "power_output_de": "Niedrigere Leistungsdichte pro Liter Hubraum",
                "thermal_stress_de": "Niedriger - bessere Langzeitbeständigkeit",
                "maintenance_intervals_months_de": 250,
                "air_filter_change_hours_de": 500,
                "fuel_filter_change_hours_de": 250,
            },
            "yanmar_cult_status_de": {
                "model_range_de": "2GM, 3GM, 4JH, 4JH-HE, 4JH-HC, 6LY2-STP",
                "legendary_reliability_de": "Marine-Diesel-Gemeinde vertraut vollständig - über 100.000 Einsatzstunden dokumentiert",
                "failure_rate_percent_de": 0.3,
                "reputation_de": "Gold-Standard in der Segelbootsgemeinde - fast kultartig verehrt",
                "user_testimonials_de": [
                    "4JH - der Motor, der einfach läuft",
                    "Yanmar-Eigner wechseln keine Motoren, sondern nur die Boote",
                    "3GM: altmodisch, aber unverwüstlich",
                    "Volvo-Besitzer neider uns um unsere Zuverlässigkeit"
                ],
                "common_models_shipwide_de": "2GM20 (9kW), 3GM30 (13kW), 4JH45 (33kW), 4JH57 (42kW)",
                "expected_service_life_years_de": 30,
                "parts_availability_de": "Weltweite Verfügbarkeit - selten wartbar",
                "resale_value_retention_percent_de": 85,
                "community_support_de": "Tausende von Foren-Tipps, DIY-Anleitungen",
            },
        },
        "turbocharged": {
            "description_de": "Mit Turbolader verdichteter Ansaugluft - höhere Leistungsdichte",
            "key_characteristics_de": {
                "intake_method_de": "Turbolader-Verdichtung mit Intercooler bei großen Motoren",
                "reliability_de": "Gut, aber höhere Betriebstemperaturen und komplexere Systeme",
                "complexity_de": "Mittel - Turbo-Lagerung erfordert Wartung",
                "lifespan_hours_de": "10000-15000 Betriebsstunden",
                "overhaul_life_de": "5000-8000h zwischen Überholungen",
                "fuel_consumption_de": "Besser - 0.20-0.28 l/kWh",
                "power_output_de": "40% höher als Saugmotoren",
                "thermal_stress_de": "Höher - Abgastemperatur 450-550°C",
                "maintenance_intervals_months_de": 200,
                "air_filter_change_hours_de": 400,
                "fuel_filter_change_hours_de": 200,
                "turbo_inspection_hours_de": 1000,
                "intercooler_cleaning_hours_de": 500,
            },
            "volvo_penta_robust_platform_de": {
                "model_range_de": "D3-110, D4-210, D6-370, D9-500",
                "reputation_de": "Robust und zuverlässig, aber elektrik-komplex",
                "failure_characteristics_de": "Wenn es ausfällt, ist es oft ein Elektronik-Problem statt Mechanik",
                "complexity_level_de": "Hoch - zahlreiche Sensoren und Module",
                "proprietary_design_de": "Volvo-Teile sind oft nicht mit anderen kompatibel",
                "torque_delivery_de": "Kraftvoller Drehmoment-Verlauf - gut für Segler",
                "dealer_network_de": "4000+ Händler weltweit - höchste Verfügbarkeit",
                "spare_parts_cost_de": "30-50% teurer als Yanmar",
                "electronics_reliance_de": "High - DEF-Systeme, Abgassensoren, CAN-Bus-Netzwerk",
                "expected_engine_life_years_de": 20,
                "known_issues_de": [
                    "D3/D4 DEF-Einspritzventile verstopfen",
                    "Elektronisches Drosselventil kann stecken bleiben",
                    "Wassersensoren oft fehlerhaft",
                    "Kühlmittel-Druckschalter anfällig für Fehler"
                ],
            },
        },
        "common_rail": {
            "description_de": "Moderne Einspritztechnik mit Hochdruckrail - präzise Einspritzung",
            "key_characteristics_de": {
                "injection_pressure_bar_de": 1600,
                "injection_timing_de": "Elektronisch gesteuert - adaptiv",
                "fuel_atomization_de": "Extrem fein - bessere Verbrennung",
                "emissions_de": "Deutlich niedriger - IMO Tier II/III konfom",
                "fuel_consumption_de": "Best-in-class - 0.18-0.22 l/kWh",
                "complexity_de": "Hoch - erfordert spezialisierte Diagnostik",
                "electronic_control_de": "ECM mit 20+ Sensoren",
                "maintenance_criticality_de": "Sehr hoch - Präzisionsteile",
                "smallest_marine_common_rail_de": "Yanmar 3JH40 - 29 kW, 2500 cm³",
            },
            "yanmar_3jh40_smallest_marine_common_rail_de": {
                "displacement_cc_de": 2500,
                "power_kw_de": 29,
                "power_hp_de": 39,
                "bore_mm_de": 92,
                "stroke_mm_de": 95,
                "max_rpm_de": 2800,
                "max_torque_nm_de": 100,
                "injection_pressure_bar_de": 1600,
                "fuel_tank_capacity_liters_de": 120,
                "cooling_capacity_de": "Geschlossener Kreislauf mit Wärmetauscher",
                "weight_kg_de": 680,
                "dimensions_length_mm_de": 950,
                "dimensions_width_mm_de": 740,
                "dimensions_height_mm_de": 850,
                "service_life_hours_de": 12000,
                "overhaul_interval_hours_de": 6000,
                "oil_capacity_liters_de": 8.5,
                "coolant_capacity_liters_de": 12,
                "fuel_consumption_cruise_lh_de": 7.5,
                "acoustic_level_db_de": 78,
                "special_characteristics_de": [
                    "Kompakt genug für kleine Segelboote",
                    "Common-Rail-Technologie im kleinsten Format",
                    "Elektronische Steuerung mit Hochdruck-Einspritzung",
                    "Emissionszertifizierung kompliziert bei Retrofit"
                ],
            },
        },
    },
    "manufacturer_comparison": {
        "description_de": "Vergleich der wichtigsten Marinediesel-Hersteller",
        "yanmar": {
            "company_origin_de": "Japan - seit 1912",
            "market_share_percent_de": 35,
            "characteristic_de": "Legendäre Zuverlässigkeit, einfache Mechanik",
            "legendary_reliability_de": "Die beste im Geschäft - dokumentierte Laufleistungen von 30+ Jahren",
            "exhaust_elbow_vulnerability_de": {
                "description_de": "Kritischer Schwachpunkt bei Yanmar-Motoren",
                "material_de": "Grauguss - korrodiert intern durch Salzwasser",
                "failure_probability_percent_de": 85,
                "typical_failure_age_years_de": 8,
                "external_appearance_de": "Oft völlig normal - interne Korrosion wird nicht sichtbar",
                "failure_mode_de": "Abrupt - kann plötzlich durchbrechen",
                "inspection_required_de": "Endoskopie alle 250-300 Betriebsstunden nach 2000h",
                "replacement_cost_usd_de": 800,
                "replacement_labor_hours_de": 4,
                "prevention_de": "Nur Edelstahl-Krümmer von Vertrauenshändlern",
            },
            "expected_service_life_years_de": 30,
            "estimated_total_engine_hours_de": 20000,
            "parts_availability_de": "Weltweiter Standard - überall erhältlich",
            "dealer_network_quality_de": "Gut bis ausgezeichnet - viele spezialisierte Händler",
            "common_models_de": {
                "2GM20_de": {"power_kw": 9, "weight_kg": 380, "price_usd": 4200},
                "3GM30_de": {"power_kw": 13, "weight_kg": 520, "price_usd": 5800},
                "4JH45_de": {"power_kw": 33, "weight_kg": 890, "price_usd": 12000},
                "4JH57_de": {"power_kw": 42, "weight_kg": 950, "price_usd": 15000},
                "6LY2_STP_de": {"power_kw": 93, "weight_kg": 1680, "price_usd": 28000},
            },
            "strengths_de": [
                "Unübertroffene Zuverlässigkeit",
                "Einfache Wartung - DIY-freundlich",
                "Niedriger Kraftstoffverbrauch",
                "Hervorragende Langzeitbeständigkeit",
                "Gutes Preis-Leistungs-Verhältnis",
                "Weltweite Ersatzteilverfügbarkeit"
            ],
            "weaknesses_de": [
                "Auslassrohr-Ausfallquote",
                "Alte Designstandards - keine elektronische Steuerung",
                "Keine modernen Abgasregelungen",
                "Weniger Leistung pro Liter als Turbo",
                "Mechanisches Drosselventil - weniger Feinkontrolle"
            ],
        },
        "volvo_penta": {
            "company_origin_de": "Schweden - seit 1907",
            "market_share_percent_de": 28,
            "characteristic_de": "Robust und leistungsstark, aber mit komplexer Elektronik",
            "robust_torque_delivery_de": "Ausgezeichnet - konzipiert für schwierige Bedingungen",
            "complexity_electronics_de": {
                "sensor_count_de": 20,
                "control_modules_de": 6,
                "can_bus_network_de": "Vollständig vernetzt - Fehlerdiagnose komplex",
                "proprietary_systems_de": [
                    "EMS (Engine Management System)",
                    "CMS (Condition Monitoring System)",
                    "DPP (Digital Propulsion Package)"
                ],
                "repair_difficulty_de": "Hoch - spezielle Geräte erforderlich",
                "dealer_dependency_de": "Hoch - DIY-Diagnose fast unmöglich",
            },
            "proprietary_design_impact_de": {
                "parts_compatibility_de": "Niedrig - Volvo-Teile passen oft nicht zu anderen Systemen",
                "aftermarket_parts_de": "Begrenzte Verfügbarkeit",
                "repair_cost_premium_percent_de": 40,
                "long_term_availability_de": "Nach 15 Jahren können Teile schwer zu finden sein",
            },
            "dealer_network_de": {
                "global_count_de": 4000,
                "distribution_de": "Nahezu überall mit Küstenzugang",
                "service_quality_variation_de": "Hochvariabel - von ausgezeichnet bis mangelhaft",
                "average_response_time_days_de": 3,
            },
            "common_models_de": {
                "D3_110_de": {"power_kw": 81, "weight_kg": 580, "price_usd": 18000},
                "D4_210_de": {"power_kw": 154, "weight_kg": 850, "price_usd": 26000},
                "D6_370_de": {"power_kw": 272, "weight_kg": 1200, "price_usd": 42000},
            },
            "strengths_de": [
                "Kraftvolles Drehmoment",
                "Robuste Konstruktion",
                "Große Dealer-Netzwerk",
                "Moderne Emissions-Kontrolle",
                "Guter Kundenservice (wenn verfügbar)"
            ],
            "weaknesses_de": [
                "Hohe Komplexität - mehr Ausfallpunkte",
                "Teure Reparaturen",
                "Proprietäre Teile",
                "Abhängigkeit von Händler-Service",
                "Häufige Elektronik-Probleme",
                "DEF-System in den USA",
                "Kühlmittel-Druck-Probleme bekannt"
            ],
            "known_failure_modes_de": {
                "def_injector_clogging_de": {
                    "description_de": "DEF-Einspritzventile verstopfen - D3/D4 anfällig",
                    "cause_de": "Kristallbildung durch Verdunstung",
                    "frequency_percent_de": 12,
                    "repair_cost_usd_de": 2500,
                    "prevention_de": "Regelmäßige lange Fahrten - Lauf-Zeit"
                },
                "throttle_valve_sticking_de": {
                    "description_de": "Elektronisches Drosselventil bleibt stecken",
                    "symptom_de": "Motor startet nicht oder läuft holprig",
                    "cause_de": "Kohlenstoffablagerungen",
                    "repair_cost_usd_de": 1800,
                },
                "water_sensor_failure_de": {
                    "description_de": "Wassersensoren in Kraftstoff-Filter fehlerhaft",
                    "frequency_percent_de": 8,
                    "false_positive_rate_percent_de": 15,
                    "replacement_cost_usd_de": 450,
                },
                "coolant_pressure_switch_de": {
                    "description_de": "Kühlmittel-Druckschalter anfällig",
                    "failure_age_hours_de": 3000,
                    "symptoms_de": "Falsche Temperatur-Anzeige oder Motorabschaltung",
                    "replacement_cost_usd_de": 350,
                },
            },
        },
        "nanni": {
            "company_origin_de": "Frankreich - Kubota-Marinizer",
            "market_share_percent_de": 12,
            "characteristic_de": "Kubota-Dieselmotoren spezialisiert für Marine",
            "kubota_marinizer_de": {
                "description_de": "Kubota-Industriemotoren mit Marine-Upgrades",
                "source_de": "Japan - Kubota Corporation",
                "modifications_de": [
                    "Edelstahl-Auslassrohre statt Grauguss",
                    "Marine-Kühler mit Kupfer-Zink-Anoden",
                    "Salzwasser-resistente Beschichtungen",
                    "Marine-Standard-Anschlüsse"
                ],
                "reliability_reputation_de": "Gut - Kubota-Grundlagen sind bewährt"
            },
            "better_heat_exchanger_de": {
                "design_de": "Hochwertige Shell-and-Tube-Konstruktion",
                "material_de": "Kupferlegierung mit dickerem Rohr",
                "zinc_anode_size_de": "Größer als Standard",
                "cleaning_frequency_months_de": 24,
                "expected_life_years_de": 12,
            },
            "warranty_years_de": 3,
            "common_models_de": {
                "N4.22_de": {"power_kw": 16, "price_usd": 6500},
                "N4.32_de": {"power_kw": 24, "price_usd": 8200},
                "N6.33_de": {"power_kw": 38, "price_usd": 13000},
            },
            "strengths_de": [
                "Kubota-Zuverlässigkeit",
                "Marine-spezifische Upgrades",
                "Bessere Wärmetauscher",
                "Gutes Preis-Leistungs-Verhältnis"
            ],
            "weaknesses_de": [
                "Kleineres Wartungsnetzwerk als Yanmar/Volvo",
                "Weniger Ersatzteilverfügbarkeit",
                "Kürzere Gewährleistung",
                "Weniger etabliertes Vertrauensnetzwerk"
            ],
        },
        "beta_marine": {
            "company_origin_de": "Großbritannien - Kubota-basiert",
            "market_share_percent_de": 8,
            "characteristic_de": "Kubota-basierte Motoren mit umfassenden Marine-Umrüstungen",
            "kubota_based_de": {
                "source_engine_de": "Kubota-Industriediesel",
                "heavy_modification_de": "Umfangreichere Marine-Anpassungen als Nanni",
                "engineering_focus_de": "Optimiert für Langzeitseereisen"
            },
            "tapered_warranty_structure_de": {
                "year_1_coverage_percent_de": 100,
                "year_2_coverage_percent_de": 75,
                "year_3_coverage_percent_de": 50,
                "year_4_coverage_percent_de": 25,
                "year_5_coverage_percent_de": 10,
                "total_warranty_years_de": 5,
                "rationale_de": "Abgestufter Ansatz - normale Wartung danach"
            },
            "power_range_hp_de": [14, 105],
            "common_models_de": {
                "14_de": {"power_hp": 14, "power_kw": 10.4, "price_usd": 5900},
                "25_de": {"power_hp": 25, "power_kw": 18.6, "price_usd": 7800},
                "42_de": {"power_hp": 42, "power_kw": 31.3, "price_usd": 11500},
                "105_de": {"power_hp": 105, "power_kw": 78.3, "price_usd": 32000},
            },
            "strengths_de": [
                "Umfassende Marine-Engineering",
                "Ausgezeichnete 5-Jahre-Garantie-Struktur",
                "Kubota-Zuverlässigkeit",
                "Ideal für Cruising-Schiffe",
                "Guter technischer Support"
            ],
            "weaknesses_de": [
                "Weniger verfügbar als Yanmar/Volvo",
                "Kleineres Ersatzteil-Netzwerk",
                "Proprietäre Konfigurationen",
                "Service-Abhängigkeit"
            ],
        },
    },
    "overhaul_specifications": {
        "description_de": "Umfassende Überholungsspezifikationen für Marinediesel-Motoren",
        "typical_overhaul_intervals_hours_de": {
            "minimum_hours_de": 5000,
            "maximum_hours_de": 8000,
            "typical_hours_de": 6500,
            "age_limit_years_de": 10,
            "recommendation_de": "Bei erreichen eines Wertes - Überholung in Betracht ziehen"
        },
        "in_frame_overhaul_de": {
            "description_de": "Überholung ohne Motor-Ausbau - begrenzte Wartung",
            "scope_de": [
                "Kurbelwellenlager inspizieren/ersetzen",
                "Ventile schleifen und einstellen",
                "Kolbenringe und Lagerbuchsen erneuern",
                "Zahnräder und Steuerung überprüfen"
            ],
            "typical_labor_hours_de": 32,
            "labor_hours_range_de": "24-40",
            "downtime_weeks_de": 2,
            "cost_usd_de": 8000,
            "cost_range_usd_de": "6500-12000",
            "scope_limitation_de": "Begrenzte Reparaturen der inneren Oberflächen",
            "suitable_for_de": "Motoren mit >5000h, keine Zylinder-Probleme"
        },
        "out_of_frame_overhaul_de": {
            "description_de": "Vollständige Überholung mit Motorausbau - umfassende Wartung",
            "scope_de": [
                "Komplett Motordemontage",
                "Alle Zylinder honen und polieren",
                "Alle Lager ersetzen",
                "Kurbelwelle prüfen und polieren",
                "Alle Ventile schleifen",
                "Dichtungen überall erneuern",
                "Ölpumpe prüfen und reparieren",
                "Kraftstoffpumpe überprüfen",
                "Zylinderköpfe erneuern/reparieren"
            ],
            "typical_labor_hours_de": 80,
            "labor_hours_range_de": "60-120",
            "downtime_weeks_de": 6,
            "cost_usd_de": 18000,
            "cost_range_usd_de": "12000-28000",
            "scope_completeness_de": "Absolute Überholung - alles wird inspiziert/erneuert",
            "expected_life_extension_years_de": 10,
            "suitable_for_de": "Motoren mit >10000h oder bekannten Zylinder-Problemen"
        },
        "cost_estimate_factors_de": {
            "base_machine_shop_cost_usd_de": 5000,
            "labor_per_hour_usd_de": 125,
            "parts_replacement_percent_of_base_de": 60,
            "gasket_set_cost_usd_de": 1200,
            "bearing_set_cost_usd_de": 800,
            "piston_ring_set_cost_usd_de": 400,
            "valve_set_cost_usd_de": 600,
            "unexpected_issues_percent_de": 20,
            "unexpected_cost_impact_usd_de": 2000
        }
    },
}


COOLING_SYSTEM_DATABASE: Dict[str, Any] = {
    "description_de": "Umfassende Datenbank für Marine-Kühlsysteme",
    "system_overview_de": {
        "architecture_de": "Zwei-Kreis-System: geschlossener Glycol-Kreis + offener Salzwasser-Kreis",
        "component_count_de": 12,
        "failure_points_de": 8,
    },
    "two_circuit_system": {
        "description_de": "Standard-Architektur aller modernen Marinediesel-Motoren",
        "primary_circuit_glycol_de": {
            "name_de": "Geschlossener Glycol-Kreis",
            "function_de": "Motor-Kühlung - direkte Zirkulation durch Motor",
            "fluid_type_de": "50/50 Glykol-Wasser-Mischung",
            "typical_pressure_bar_de": 1.2,
            "max_pressure_bar_de": 2.0,
            "temperature_operation_celsius_de": 80,
            "temperature_thermostat_opening_celsius_de": 75,
            "temperature_full_opening_celsius_de": 85,
            "pump_type_de": "Zentrifugal-Impeller",
            "pump_flow_lpm_de": 80,
            "reservoir_capacity_liters_de": 20,
            "coolant_change_interval_years_de": 2,
            "pH_degradation_rate_percent_per_year_de": 15,
            "inhibitor_depletion_de": "Metallschutz nimmt mit Zeit ab",
            "recommended_coolant_brands_de": [
                "Volvo Penta OEM-Kühlmittel",
                "Yanmar Long-Life-Kühlmittel",
                "Caterpillar PEDC",
                "Shell Rotella Ultra"
            ],
            "components_de": [
                "Wasserpumpe",
                "Thermostat",
                "Druckschalter",
                "Kühlmittel-Druckregler",
                "Ausdehnungstank",
                "Zirkulationsleitungen"
            ]
        },
        "secondary_circuit_seawater_de": {
            "name_de": "Offener Salzwasser-Kreis",
            "function_de": "Wärmeableitung vom Glykol-Kreis ins Meer",
            "intake_location_de": "Durch-Hulls, typischerweise an Kiellinie",
            "intake_size_mm_de": 25,
            "intake_screen_mesh_micron_de": 100,
            "flow_rate_lpm_de": 60,
            "intake_strainer_change_hours_de": 500,
            "salt_corrosion_risk_de": "Extremhoch - alles ist anfällig",
            "material_requirements_de": "Kupferlegierung oder Edelstahl nur",
            "zinc_anode_mandatory_de": True,
            "anode_inspection_interval_months_de": 3,
            "anode_replacement_when_percent_consumed_de": 50,
            "cooling_hose_material_de": "Kunststoff-verstärktes Gummi oder Silikon",
            "cooling_hose_lifespan_years_de": 8,
            "cooling_hose_burst_risk_de": "Hoch wenn nicht überwacht",
            "heat_exchanger_design_de": "Shell-and-Tube oder Plattenwärmer",
            "components_de": [
                "Seewasser-Einlassventil",
                "Einlasssieb",
                "Wärmetauscher (mit Anode)",
                "Auslassventil",
                "Auslasshose",
                "Ausgleichstank"
            ]
        }
    },
    "impeller_pump": {
        "description_de": "Der kritischste Verschleißteil - regelmäßiger Austausch obligatorisch",
        "material_composition_de": "Neopren oder Nitril-Gummi",
        "blade_count_de": 5,
        "blade_thickness_mm_de": 6,
        "annual_replacement_mandatory_de": True,
        "mandatory_replacement_reason_de": "Gummi nimmt Dauerform an - Pumpeneffizienz fällt dramatisch",
        "efficiency_loss_first_season_percent_de": 15,
        "efficiency_loss_second_season_percent_de": 35,
        "efficiency_loss_third_season_percent_de": 60,
        "consequences_of_failure_de": {
            "reduced_flow_de": "Durchfluss reduziert sich um 50%+",
            "overheating_risk_de": "Motor kann überhitzen - Schaden möglich",
            "bearing_wear_acceleration_de": "Gelagerte Welle wird zusätzlich belastet",
            "noise_de": "Kavitation erzeugt Geräusche",
            "efficiency_de": "Kraftstoffverbrauch steigt um 10-15%"
        },
        "failure_symptom_de": [
            "Gelbes oder milchiges Kühlmittel - kann sein",
            "Temperatur-Schwankungen",
            "Höheres Pumpgeräusch",
            "Reduzierter Durchfluss sichtbar",
            "Motor läuft wärmer als normal"
        ],
        "replacement_procedure_de": {
            "access_location_de": "Einbau am Seewasser-Ausgang der Pumpe",
            "removal_tool_de": "Innen-Loch-Auszieher oder Schraubendreher",
            "installation_direction_de": "Blätter MÜSSEN in Pumprichting zeigen",
            "direction_error_consequence_de": "Motor läuft nicht - kein Durchfluss",
            "typical_labor_time_minutes_de": 15,
            "hose_clamp_torque_nm_de": 8,
        },
        "annual_inspection_checklist_de": [
            "Farbe des Impellers inspizieren - sollte noch schwarz sein",
            "Blätter auf Risse prüfen",
            "Blätter auf Verformung prüfen",
            "Verschleißmuster überprüfen",
            "Lagerspiel fühlen - sollte minimal sein",
            "Pumpgeräusch während Betrieb hören"
        ],
        "annual_replacement_cost_usd_de": 45,
        "annual_replacement_interval_hours_de": 500,
        "replacement_interval_months_de": 12,
        "most_common_failure_scenario_de": "Skipper vergisst Austausch - Motor überhitzt beim Segeln",
    },
    "heat_exchanger": {
        "description_de": "Kritischer Wärmetausch-Komponente - Shell-and-Tube Design",
        "design_type_de": "Shell-and-Tube Wärmetauscher (Standard Marine)",
        "material_tubes_de": "Kupferlegierung (90% Cu, 10% Ni)",
        "material_shell_de": "Stahllegierung - epoxy-beschichtet",
        "tube_count_de": 24,
        "tube_diameter_mm_de": 10,
        "tube_length_mm_de": 450,
        "zinc_anode_critical_de": True,
        "zinc_anode_description_de": {
            "purpose_de": "Galvanische Opfer-Anode - schützt alle Kupfer-Teile",
            "material_de": "Reinstzink (99.9%)",
            "weight_typical_kg_de": 0.8,
            "consumption_rate_percent_per_year_de": 40,
            "replacement_interval_months_de": 12,
            "replacement_when_consumed_percent_de": 50,
            "cost_usd_de": 35,
            "failure_consequence_de": "Ohne Anode: Kupferauflösung in wenigen Monaten",
            "identification_de": "Silbrig-metallisches Aussehen, wird schwarz bei Verschleiß"
        },
        "teflon_tape_danger_de": {
            "warning_de": "TEFLON-TAPE AUF DER ANODE ZERSTÖRT DEN SCHUTZ!",
            "reason_de": "Teflon-Tape isoliert die Anode elektrolytisch",
            "consequence_de": "Anode funktioniert nicht - Motor wird nicht geschützt",
            "result_de": "Kupfer-Auflösung und Wärmetauscher-Leck in Monaten",
            "correct_procedure_de": "NIEMALS Teflon-Tape auf Anode-Gewinde verwenden",
            "correct_sealant_de": "Kupfer-basiertes Dichtmittel oder Zahnriemenöl"
        },
        "cleaning_procedure_de": {
            "frequency_months_de": 24,
            "frequency_alternative_hours_de": 1000,
            "method_de": "Chemische Entkalkung oder mechanisches Spülen",
            "scaling_removal_de": "Kalkablagerungen werden gelöst",
            "algae_removal_de": "Biologische Verschmutzung wird entfernt",
            "acid_strength_de": "Milde organische Säure - nicht aggressiv",
            "immersion_time_hours_de": 12,
            "safety_precautions_de": [
                "Gummihandschuhe tragen",
                "Augenschutz",
                "Belüftung erforderlich",
                "Mit Wasser spülen nach Behandlung"
            ],
            "cost_per_cleaning_usd_de": 150,
            "diy_option_de": "Ja - mit Essig oder zitronensäurehaltigen Produkten möglich"
        },
        "failure_modes_de": {
            "leaking_tubes_de": {
                "cause_de": "Loch in Kupfer-Rohr - Korrosion oder Verschleiß",
                "symptom_de": "Salzwasser in Glykol-Kühlmittel - milchig/trüb",
                "consequence_de": "Kühlmittel-Verlust und Kontamination",
                "detection_de": "Kühlmittel-Farbe wird milchig weiß",
                "repair_option_1_de": "Tube plugging - Kupfer-Stöpsel einsetzen",
                "repair_option_2_de": "Wärmetauscher-Austausch - Kosten $1500-3000"
            },
            "clogged_tubes_de": {
                "cause_de": "Kalkablagerungen oder biologische Verschmutzung",
                "symptom_de": "Motor läuft warm - Durchfluss reduziert",
                "consequence_de": "Überheizung - Motor-Abschaltung",
                "prevention_de": "Regelmäßige Entkalkung"
            },
            "anode_failure_de": {
                "cause_de": "Anode verbraucht oder entfernt",
                "consequence_de": "Schnelle Kupfer-Korrosion - Leck innerhalb Monate",
                "symptom_de": "Erst keine - dann plötzlich Leck"
            },
            "seal_failure_de": {
                "cause_de": "Gummi-Dichtung verwittert",
                "symptom_de": "Salzwasser leckt außen aus Wärmetauscher",
                "consequence_de": "Salzwasser-Verlust - Durchfluss fällt",
                "repair_cost_usd_de": 400
            }
        },
        "maintenance_checklist_de": [
            "Anode wöchentlich visuell inspizieren - sollte noch metallisch sein",
            "Jährlich: Anode wiegen oder sichtbar prüfen auf Verbrauch",
            "Alle 24 Monate: Chemische Entkalkung durchführen",
            "Alle 12 Monate: Anode auswechseln",
            "Alle 6 Monate: Kühlmittel auf Trübheit prüfen",
            "Salzwasser-Durchfluss beobachten"
        ]
    },
    "thermostat": {
        "description_de": "Temperatur-Regelventil - steuert Glykol-Kreis-Zirkulation",
        "function_de": "Bypasst kaltes Kühlmittel um Motor bis Betriebstemperatur erreicht",
        "opening_temperature_celsius_de": 75,
        "full_opening_temperature_celsius_de": 85,
        "temperature_range_celsius_de": 10,
        "response_time_seconds_de": 8,
        "failure_mode_stuck_closed_de": {
            "symptom_de": "Motor läuft heiß - Temperaturanzeige steigt kontinuierlich",
            "consequence_de": "Überheizung - Motor-Drehmoment fällt, Beschädigung möglich",
            "detection_method_de": "Oberer Kühlschlauch ist eiskalt - sollte heiß sein",
            "detection_method_2_de": "Temperaturanzeige >90°C bei normalem Betrieb"
        },
        "failure_mode_stuck_open_de": {
            "symptom_de": "Motor läuft kalt - erreicht niemals Betriebstemperatur",
            "consequence_de": "Schlechter Kraftstoffverbrauch, höhere Emissionen",
            "detection_method_de": "Oberer Kühlschlauch ist immer warm - sollte kalt starten"
        },
        "bypass_valve_failure_de": {
            "description_de": "Druckentlastungsventil in Kühlmittel-Kreis",
            "function_de": "Verhindert Überdruckaufbau",
            "opening_pressure_bar_de": 2.0,
            "failure_consequence_de": "Hochdruckaufbau - Schläuche können platzen",
            "symptom_de": "Kühlmittel tritt aus Ausdehnungstank aus"
        },
        "replacement_cost_usd_de": 120,
        "replacement_labor_time_hours_de": 1.5,
        "typical_lifespan_years_de": 8,
        "maintenance_notes_de": "Kein praktischer Austausch - nur Auswechslung möglich"
    },
}


EXHAUST_DATABASE: Dict[str, Any] = {
    "description_de": "Umfassende Datenbank für Marine-Abgassysteme",
    "mixing_elbow": {
        "description_de": "DER häufigste Ausfallpunkt bei Marinedieseln - kritisch!",
        "location_de": "Verbindung zwischen Motor-Auslassrohr und Abgaskühler",
        "function_de": "Mischt Kühlwasser mit heißen Abgasen",
        "material_naturally_aspirated_de": {
            "type_de": "Grauguss - ANFÄLLIG FÜR INTERNE KORROSION",
            "composition_de": "68% Fe, 4% C, 2% Si",
            "exterior_appearance_de": "Oft völlig normal - kein sichtbarer Verschleiß",
            "interior_condition_de": "Kann völlig durchgerostet sein - innen schwarz",
            "lifespan_years_de": 8,
            "lifespan_hours_de": 4000,
            "failure_mechanism_de": "Salzwasser-Injektion + Hitze erzeugt elektrolytische Korrosion",
            "failure_pattern_de": "Innen korrodiert, Außenseite kann noch glänzen",
            "failure_consequence_de": "Abrupt durchbrechen - Wasser ins Abgas-Rohrsystem",
            "warning_signs_de": [
                "Oft KEINE Vorwarnung",
                "Wasser im Abgas-Dampf",
                "Schwächer werdende Motor-Leistung",
                "Unerwartete Temperatur-Schwankungen"
            ]
        },
        "material_stainless_steel_de": {
            "type_de": "Edelstahl 304 oder 316 - BESTÄNDIG",
            "composition_de": "Fe mit 18% Cr, 8-12% Ni",
            "lifespan_years_de": 15,
            "lifespan_hours_de": 10000,
            "cost_premium_percent_de": 250,
            "initial_cost_usd_de": 2400,
            "failure_mechanism_de": "Sehr selten - nur bei Chlorid-Stress-Korrosion",
            "maintenance_requirement_de": "Minimal - standard Entkalkung"
        },
        "inspection_requirements_de": {
            "frequency_hours_de": 250,
            "first_inspection_hours_de": 2000,
            "frequency_recommendation_de": "Nach 2000h jede 250-300h überprüfen",
            "inspection_method_de": "Endoskop - Sicht in Rohr",
            "inspection_cost_usd_de": 150,
            "endoscope_access_point_de": "Von oben durch Wasser-Einlass oder spezielle Öffnung",
            "what_to_look_for_de": [
                "Schwarze/oranges Verfärbung innen",
                "Raue Oberfläche",
                "Kleine Löcher oder Pits",
                "Grüne Verfärbung (Kupfer-Korrosion)",
                "Beschlagsenrohr"
            ],
            "replacement_trigger_de": "Bei ersten Korrosions-Anzeichen - nicht warten"
        },
        "replacement_procedure_de": {
            "labor_time_hours_de": 4,
            "complexity_de": "Mittel - erfordert Kühlmittel-Ablassen",
            "bolt_size_mm_de": 8,
            "bolt_count_de": 4,
            "new_gasket_required_de": True,
            "gasket_material_de": "Hochtemperatur-Graphit mit Metallumhüllung",
            "torque_specification_nm_de": 18,
            "cooling_time_before_operation_hours_de": 2,
            "test_procedure_de": "Langsam hochfahren - auf Lecks prüfen"
        },
        "replacement_cost_usd_de": 800,
        "replacement_cost_complete_labor_usd_de": 1200,
        "ss_upgrade_cost_premium_usd_de": 1600,
        "prevention_strategy_de": "Edelstahl-Austausch während Überholung"
    },
    "hydrolock": {
        "description_de": "Wasser gelangt in Zylinder - kann Motor zerstören",
        "mechanism_de": "Wasser im Abgas-Rohr läuft rückwärts in Motor-Zylinder",
        "risk_factors_de": {
            "high_compression_engines_de": "Höhere Verdichtung = weniger Wasser nötig zum Hydrolock",
            "common_rail_engines_de": "Riskant wegen hoher Verdichtung",
            "naturally_aspirated_low_compression_de": "Sicherer - erfordert mehr Wasser"
        },
        "water_volume_required_de": {
            "high_compression_cc_de": 50,
            "low_compression_cc_de": 150,
            "damage_consequence_de": "Unvollständige Verbrennung - Wasserdampf-Vermischung"
        },
        "failure_consequence_de": {
            "bent_connecting_rod_de": "Zylinderblock kann knacken",
            "cracked_head_de": "Kopf-Verschluss erzeugt Druck",
            "total_engine_failure_de": "Motor ist unbrauchbar - Überholung oder Austausch nötig"
        },
        "prevention_de": {
            "anti_siphon_valve_mandatory_de": True,
            "intake_closure_de": "Nach 2 fehlgeschlagenen Start-Versuchen: Saugventil schließen",
            "manual_bilge_check_de": "Bilge auf Wasser prüfen vor Start",
            "rain_protection_de": "Auspuff-Rohr muss 45cm über Wasserlinie sein"
        },
        "if_suspected_de": [
            "Motor NICHT starten",
            "Kurbelwelle manuell drehen - sollte leicht gehen",
            "Wenn sehr schwer: Wasser im Zylinder",
            "Zündkerzen aus Zylinder ziehen - Wasser ablassen",
            "Auftrag für Überholung vorbereiten"
        ]
    },
    "anti_siphon_valve": {
        "description_de": "KRITISCH WICHTIG - verhindert Siphon von Seewasser in Motor",
        "purpose_de": "Bricht Siphon-Effekt auf Abgasrohr-Rückweg",
        "location_de": "Abgasrohr, oben am höchsten Punkt",
        "minimum_height_above_waterline_cm_de": 45,
        "minimum_height_inches_de": 18,
        "principle_de": "Luft-Eintritt bricht Siphon - Wasser kann nicht fließen",
        "installation_requirement_de": "OBLIGATORISCH - nicht optional",
        "cost_usd_de": 45,
        "maintenance_de": "Jährlich reinigen - Salzablagerungen können Ventil zusetzen",
        "failure_scenario_de": "Ventil blockiert - Siphon funktioniert - Hydrolock",
        "testing_de": "Durch Handschuh pusten - sollte durchblasen"
    },
    "water_lock": {
        "description_de": "System zur Verhängnis des Wassers in Abgasrohr",
        "function_de": "Lässt Abgase hinaus, aber nicht Wasser rein",
        "typical_installation_de": "Kleine Kammer mit Einlass- und Auslassventil",
        "valve_type_de": "Rückschlagventil - öffnet nur für Abgase",
        "maintenance_de": "Regelmäßige Spülung mit Süßwasser",
        "cost_usd_de": 120,
        "lifetime_de": "5 Jahre typisch - dann Ventil-Verschleiß"
    },
    "exhaust_hose": {
        "description_de": "Abgasschlauch - muss Hitze und Salzwasser widerstehen",
        "material_standard_de": "Gummi-Silikon-Mischung, hitzebeständig",
        "temperature_rating_celsius_de": 120,
        "minimum_height_above_waterline_cm_de": 45,
        "minimum_height_in_ft_de": 1.5,
        "routing_requirement_de": "Kontinuierlich steigend - keine Taschen wo Wasser sammeln kann",
        "lifespan_years_de": 8,
        "failure_mechanism_de": "Hitze schädigt Gummi - wird spröde",
        "failure_consequence_de": "Dünner werdend - platzt plötzlich",
        "hose_diameter_typical_inches_de": 2,
        "hose_clamp_torque_nm_de": 8,
        "inspection_frequency_months_de": 24,
        "replacement_checklist_de": [
            "Schlauch auf Risse prüfen",
            "Farbe - sollte noch schwarz sein, nicht weiß/grau",
            "Flexibilität testen - sollte biegsam sein",
            "Auf Lecks inspizieren",
            "Hose-Schellen auf Korrosion prüfen"
        ],
        "cost_usd_de": 180,
        "labor_cost_usd_de": 60
    },
}


FUEL_SYSTEM_DATABASE: Dict[str, Any] = {
    "description_de": "Umfassende Datenbank für Marine-Kraftstoffsysteme",
    "diesel_bug": {
        "description_de": "Mikrobiologische Kontamination - Bakterien und Pilze im Kraftstoff",
        "organism_types_de": [
            "Bakterien: Corynebacterium, Pseudomonas, Bacillus",
            "Pilze: Aspergillus, Candida, Fusarium",
            "Algen: Chlorella, Scenedesmus"
        ],
        "colonization_pattern_de": "Bildet dünne Schicht an Kraftstoff-Wasser-Grenze",
        "growth_requirement_water_de": "Wasser ist KRITISCH - Spuren reichen",
        "growth_requirement_temperature_celsius_de": 10,
        "optimal_growth_temperature_celsius_de": 30,
        "fuel_sulfur_impact_de": "Moderner Diesel mit weniger Schwefel = BESSER für Bakterien-Wachstum",
        "ultra_low_sulfur_diesel_risk_de": {
            "sulfur_content_ppm_de": 15,
            "bacterial_growth_increase_percent_de": 300,
            "reason_de": "Schwefel ist natürlicher Biozid - weniger Schwefel = mehr Wachstum"
        },
        "water_source_contamination_de": [
            "Kondensation in Kraftstoff-Tank",
            "Feuchte Luft beim Tanken",
            "Regenwasser-Eintritt durch Einfüll-Öffnung",
            "Wasser-Durchsatz bei Kraftstoff-Pumpe",
            "Lecks in Kraftstoff-Filtern"
        ],
        "detection_signs_de": [
            "Schwarzes/braunes Sediment in Tank",
            "Schmieriger Film auf Filteroberfläche",
            "Schlechter Brennstoff-Geruch - sauer/muffig",
            "Motor-Start-Schwierigkeiten",
            "Plötzliche Kraftstoff-Filter-Verstopfung",
            "Grüner oder grauer Belag im Tank"
        ],
        "visual_test_de": {
            "method_de": "Kleine Menge Fuel in Glas - 24h stehen lassen",
            "observation_de": "Schichten: oben Wasser, unten schwarzes Sediment, Mittel normal",
            "result_positive_de": "Schwarzes Material am Boden = Diesel Bug vorhanden"
        },
        "prevention_de": [
            "Kraftstoff-Tank trocken halten - minimal Luft-Raum",
            "Kupfer- oder Zink-Anoden im Tank",
            "Gutes Fuel Management - alte Tanks regelmäßig spülen",
            "Winterlagerung: Tank VOLL mit Diesel halten",
            "Alle 3 Monate: Biozid-Zusatz (präventiv)"
        ],
        "biocide_treatment_de": {
            "product_types_de": [
                "Peroxid-basiert: Biobor JF, Fuzex",
                "Isothiazolin-basiert: Fuel Biocide 8620",
                "Cetylpyridinium-basiert: Algae-X"
            ],
            "mechanism_de": "Zerstört Zellwand - Organisme stirbt",
            "treatment_procedure_de": "Biozid ins Tank geben, Motor 2 Stunden laufen lassen",
            "dosage_ratio_ppm_de": 100,
            "typical_dose_for_100l_tank_ml_de": 20,
            "effectiveness_percent_de": 95,
            "cost_per_treatment_usd_de": 35,
            "treatment_frequency_months_de": 3,
            "warning_de": "NICHT wiederholt behandeln - tötet nützliche Bakterien auch"
        },
        "long_term_solution_de": [
            "Complete tank cleaning service",
            "Fuel polishing - Umwälzung durch Feinstfilter",
            "Tank interior coating - moderne Beschichtung",
            "Copper or zinc anodes - continuous protection",
            "Regular fuel testing - early detection"
        ]
    },
    "fuel_filters": {
        "description_de": "Kritische Komponente zur Vorbeugung von Injektoren-Verschleiß",
        "primary_filter_water_separator": {
            "name_de": "Racor oder ähnlich - primärer Wasser-Separator",
            "purpose_de": "Entfernt Wasser und große Partikel",
            "location_de": "Zwischen Tank und Kraftstoff-Pumpe",
            "flow_rate_capability_lph_de": 100,
            "filtration_micron_de": 30,
            "water_removal_capacity_liters_de": 1.5,
            "water_bowl_inspection_de": "Regelmäßig prüfen - sollte klar sein",
            "water_drain_interval_days_de": 14,
            "filter_element_replacement_months_de": 6,
            "cost_per_element_usd_de": 28,
            "warning_signs_de": [
                "Motor startet schwer",
                "Verlangsamte Beschleunigung",
                "Whiterauch aus Auspuff",
                "Höherer Kraftstoff-Verbrauch"
            ]
        },
        "secondary_fine_filter": {
            "name_de": "Feinstfilter - Injektoren-Schutz",
            "purpose_de": "Entfernt Kleinstpartikel vor Injektoren",
            "location_de": "Auf dem Motor oder in Motorraum",
            "filtration_micron_de": 2,
            "injector_protection_critical_de": "ABSOLUT NOTWENDIG",
            "modern_injector_pressure_psi_de": 36000,
            "modern_injector_nozzle_tolerance_micron_de": 3,
            "particle_size_consequence_de": "Ein Staubkorn = Injektor-Verschleiß",
            "filter_element_replacement_months_de": 12,
            "cost_per_element_usd_de": 45,
            "pressure_drop_max_bar_de": 1.0,
            "high_pressure_drop_consequence_de": "Reduzierter Durchfluss - schlechter Start",
            "bypass_valve_function_de": "Öffnet wenn Filter verstopft - verhindert Mangeldruck"
        },
        "diesel_fuel_quality_standard_de": {
            "standard_iso_de": "ISO 4406",
            "particle_size_classification_de": "18/16/13",
            "meaning_de": "Unter 4µm: max 1300 Partikel/ml, 6-14µm: 160, 14-25µm: 20",
            "typical_fuel_from_station_de": "25/22/19 - nicht ideal",
            "filtered_fuel_quality_de": "18/16/13 - Injektoren-sicher",
            "filtration_benefit_de": "Reduziert Injektor-Ausfallrisiko um 70%"
        }
    },
    "fuel_tank_materials": {
        "description_de": "Unterschiedliche Materialien haben unterschiedliche Anforderungen",
        "aluminum_alloys_de": {
            "type_de": "Aluminium 5052, 5083, 5086 - niedrige galvanische Aktivität",
            "advantages_de": [
                "Korrosions-resistent gegen Diesel",
                "Leicht und preiswert",
                "Weit verbreitet in Segelbooten"
            ],
            "disadvantages_de": [
                "Galvanische Korrosion mit anderen Metallen möglich",
                "Anfällig wenn direkt mit Salzwasser in Kontakt"
            ],
            "anode_requirement_de": "Optional - aber empfohlen",
            "galvanic_scale_risk_de": "Minimal - gutes Material für Meerwasser"
        },
        "stainless_steel_de": {
            "type_de": "316L für höchste Korrosions-Resistenz",
            "advantages_de": [
                "Höchste Korrosions-Resistenz",
                "Sehr langlebig",
                "Premium-Wahl"
            ],
            "disadvantages_de": [
                "Crevice corrosion risk wenn Wasser eingeschlossen",
                "Teuer",
                "Kann mit Diesel reagieren wenn Chlorid vorhanden"
            ],
            "anode_risk_de": "Nicht empfohlen - kann Crevice-Korrosion auslösen"
        },
        "polyethylene_plastic_de": {
            "type_de": "HDPE - High-Density Polyethylene",
            "advantages_de": [
                "Nicht korrodierbar",
                "Leicht und einfach zu montieren",
                "Preiswert"
            ],
            "disadvantages_de": [
                "UV-Empfindlich - braucht UV-Schutz",
                "Temperatur-empfindlich",
                "Kann Diesel-Additive aufnehmen"
            ],
            "lifespan_years_de": 10,
            "sunlight_protection_mandatory_de": True
        }
    },
    "fuel_aging_storage": {
        "description_de": "Diesel verschlechtert sich bei längerer Lagerung",
        "gum_formation_de": {
            "mechanism_de": "Oxidation von Diesel-Kohlenwasserstoffen - bildet Schleim",
            "timeline_months_de": 6,
            "problem_consequence_de": "Filter-Verstopfung, Injektor-Verschleiß",
            "prevention_de": "Stabilisator-Zusätze verwenden"
        },
        "sediment_formation_de": {
            "mechanism_de": "Kleine unlösliche Feststoffe fallen aus",
            "timeline_months_de": 12,
            "appearance_de": "Braunes oder schwarzes Pulver am Tank-Boden",
            "consequence_de": "Pumpen-Verschleiß, Filter-Blockade"
        },
        "water_accumulation_de": {
            "source_de": "Kondensation aus Luft",
            "timeline_months_de": 3,
            "prevention_de": "Tank voll halten - minimal Luft-Raum",
            "detection_de": "Wasserseparator prüfen"
        },
        "storage_best_practices_de": [
            "Tank vollständig gefüllt halten",
            "Kühl und trocken lagern",
            "Stabilisator-Zusatz alle 6 Monate",
            "Alle 6 Monate Motor laufen lassen",
            "Jährlich Probe testen lassen"
        ],
        "stabilizer_products_de": [
            "Diesel Fuel Stabilizer (Crown Oil)",
            "Fuel Saver (Shell)",
            "Biobor JF (mit Biozid)"
        ]
    }
}


DRIVETRAIN_DATABASE: Dict[str, Any] = {
    "description_de": "Umfassende Datenbank für Antriebsanlagen - Wellen, Segelantriebe, Propeller",
    "shaft_alignment": {
        "description_de": "Präzisions-Ausrichtung zwischen Motor und Propellerwelle",
        "critical_importance_de": "Abweichungen von Zehnteln Millimeter erzeugen Vibrationen und Verschleiß",
        "tolerance_mm_de": 0.05,
        "tolerance_inches_de": 0.002,
        "consequence_of_misalignment_de": [
            "Hohe Vibrationen - unbequem für Schiff",
            "Beschleunigter Lager-Verschleiß",
            "Wellenverschleiß und Durchhang",
            "Dicht-Versagen",
            "Propeller-Unwuchten"
        ],
        "measurement_method_de": "Dial Indicator oder Laser-Alignment-System",
        "laser_alignment_cost_usd_de": 300,
        "dial_indicator_cost_usd_de": 150,
        "alignment_service_cost_usd_de": 800,
        "correction_procedure_de": [
            "Welle mit Dial Indicator messen",
            "Motor-Lagerblöcke anpassen",
            "Iterative Messung und Anpassung",
            "Zieltoleranz 0.05mm erreichen"
        ]
    },
    "shaft_seal_types": {
        "description_de": "Drei verschiedene Seal-Typen für Propellerwellen",
        "stuffing_box": {
            "name_de": "Stopfbuchse - traditionell, mit kontrolliertem Tropfen",
            "design_de": "Konische Packing-Ringe um Welle",
            "material_de": "Graphit-Fäden, teflonverstärkt",
            "operation_principle_de": "Dichtung durch mechanische Kompression",
            "leakage_rate_drops_per_minute_de": 10,
            "acceptable_leakage_de": "30-40 Tropfen pro Minute - NORMAL",
            "purpose_of_leakage_de": "Kühlt die Dichtung - verhindert Überhitzung",
            "maintenance_frequency_months_de": 12,
            "maintenance_procedure_de": "Einstellmutter eine halbe Umdrehung festziehen",
            "tools_required_de": "Schraubenschlüssel 15mm",
            "tensioning_critical_de": "Zu locker = zu viel Wasser, Zu fest = Überhitzung",
            "symmetric_half_turn_procedure_de": "Oben halbe Umdrehung, Boden halbe Umdrehung - symmetrisch",
            "cost_annual_maintenance_usd_de": 50,
            "lifespan_years_de": 10,
            "replacement_cost_usd_de": 400,
            "advantages_de": [
                "Einfach - kann jeder anpassen",
                "Kühlung durch Wasser",
                "Preiswert",
                "DIY-freundlich"
            ],
            "disadvantages_de": [
                "Ständige Wartung erforderlich",
                "Ständiges Tropfen",
                "Überwachung notwendig"
            ]
        },
        "pss_dripless_seal": {
            "name_de": "PSS Dripless - mechanische Gleitringdichtung, tropfenfrei",
            "design_de": "Carbon-Graphit Gleitringe auf Edelstahl-Lauffläche",
            "operation_principle_de": "Präzision-Gleitkontakt - keine Lecks",
            "leakage_rate_drops_per_minute_de": 0,
            "acceptable_leakage_de": "KEINE - vollständig trocken",
            "material_seal_de": "Carbon mit Graphit - sehr hart",
            "material_seat_de": "Edelstahl 316 - korrosionsbeständig",
            "maintenance_requirement_de": "Minimal - Montage und vergessen",
            "adjustment_possibility_de": "KEINE - nicht anpassbar",
            "design_implication_de": "Muss bei Installation perfekt ausgerichtet sein",
            "cost_initial_usd_de": 800,
            "installation_cost_usd_de": 400,
            "total_cost_usd_de": 1200,
            "lifespan_years_de": 15,
            "advantages_de": [
                "Keine tropfenden Wasserlecks",
                "Minimale Wartung",
                "Langlebig",
                "Schiff bleibt trocken"
            ],
            "disadvantages_de": [
                "Höherer Anfangspreis",
                "Installation kritisch",
                "Nicht anpassbar nach Installation",
                "Austausch erforderlich bei Verschleiß"
            ]
        },
        "lip_seal_tides_marine": {
            "name_de": "Tides Marine Replaceable Lip Seal - Wechselbar unter Wasser",
            "design_de": "Gummi-Lippen-Dichtung auf austauschbarem Mantel",
            "material_seal_de": "Nitrile oder Viton Gummi",
            "material_seat_de": "Edelstahl",
            "unique_feature_de": "Kann unter Wasser gewechselt werden",
            "replacement_procedure_de": "Neue Manschette einschieben - Motor läuft weiter",
            "installation_location_de": "Propeller-Welle oberhalb der Wasserlinie",
            "lifespan_years_de": 8,
            "maintenance_interval_years_de": 2,
            "replacement_cost_usd_de": 300,
            "installation_cost_usd_de": 200,
            "advantages_de": [
                "Unter Wasser austauschbar - kein Haul-Out nötig",
                "Günstige Ersatzteile",
                "Gutes Preis-Leistungs-Verhältnis",
                "Zuverlässig"
            ],
            "disadvantages_de": [
                "Braucht regelmäßigen Austausch",
                "Benötigt Tauch-Service",
                "Nicht so langlebig wie PSS"
            ]
        }
    },
    "saildrive_units": {
        "description_de": "Integrierte Motor-Antrieb-Einheit - Motor sitzt oben, Lager unten",
        "design_de": "Gearbox mit drehbarem Unterteil für Kurssteuerung",
        "typical_manufacturers_de": ["Volvo Penta Saildrive", "Yammer Saildrive", "Mercruiser"],
        "diaphragm_seal": {
            "description_de": "Kritischste Komponente - trennt Getriebe-Öl von Seewasser",
            "function_de": "Flexibles Gummi-Diaphragma ermöglicht Aus- und Eindelhen",
            "material_de": "Nitrile oder Viton - abhängig vom System",
            "lifespan_volvo_years_de": 7,
            "lifespan_yammer_years_de": 5,
            "failure_age_hours_de": 3000,
            "failure_consequence_de": "Seewasser leckt ins Getriebe - Öl wird milchig",
            "detection_method_de": [
                "Getriebe-Öl in Sichtglas prüfen",
                "Milchig/trüb = Wasser im Öl",
                "Weiße/braune Emulsion = Versiegelung fehlgeschlagen"
            ],
            "detection_timeline_after_failure_de": "1 Woche - deutlich sichtbar",
            "replacement_cost_labor_usd_de": 600,
            "replacement_cost_parts_usd_de": 400,
            "replacement_total_cost_usd_de": 1000,
            "labor_time_hours_de": 8,
            "haul_out_requirement_de": True,
            "prevention_de": "Regelmäßige Öl-Kontrolle alle 50 Betriebsstunden"
        },
        "gear_oil_maintenance": {
            "description_de": "Getriebe-Öl - kritisch für Langzeitbetrieb",
            "oil_type_standard_de": "ISO VG 68 oder 80 - Marine SAE 90",
            "oil_change_interval_hours_de": 500,
            "oil_change_interval_years_de": 2,
            "capacity_liters_de": 2.5,
            "inspection_frequency_hours_de": 50,
            "what_to_check_de": [
                "Ölstand im Sichtglas",
                "Farbe - sollte klar bernsteinfarben sein",
                "Trübheit - Wasser-Hinweis",
                "Schlamm oder Feststoffe am Boden"
            ],
            "normal_oil_color_de": "Bernsteinfarben bis hellbraun",
            "warning_color_de": "Milchig weiß oder dunkelbraun",
            "milky_appearance_consequence_de": "Wasser im Getriebe - Dichtung versagt",
            "action_if_milky_de": [
                "Motor nicht starten",
                "Sofort Dichtung prüfen",
                "Öl wechseln",
                "Getriebe auf Verschleiß inspizieren"
            ],
            "oil_brand_examples_de": [
                "Volvo Penta IPS Oil",
                "Yammer Saildrive Oil",
                "Shell Tellus S2 MA 68",
                "Mobil DTE 68"
            ]
        },
        "anode_protection": {
            "description_de": "Opfer-Anode für Seewasser-Unterseite",
            "material_de": "Zink oder Aluminium",
            "purpose_de": "Schützt Messingteile vor Korrosion",
            "installation_location_de": "Unterteil des Segeltriebs",
            "inspection_interval_months_de": 3,
            "replacement_when_consumed_percent_de": 50,
            "cost_per_anode_usd_de": 45,
            "expected_life_months_de": 18,
            "failure_consequence_de": "Messing-Teile rosten - Getriebe verfällt"
        }
    },
    "propeller": {
        "description_de": "Propeller-Typen, Materialien und Dimensionierung",
        "fixed_vs_folding": {
            "fixed_propeller_de": {
                "description_de": "Starrer Propeller - permanent angebracht",
                "advantages_de": [
                    "Einfache Konstruktion",
                    "Günstig",
                    "Zuverlässig"
                ],
                "disadvantages_de": [
                    "Bremst Boot unter Segel - Widerstand",
                    "75% Widerstand im Segel-Modus"
                ],
                "drag_coefficient_de": 0.75,
                "speed_loss_knots_de": 0.5
            },
            "feathering_propeller_de": {
                "description_de": "Propeller der Blätter zusammenklappt unter Segel",
                "advantages_de": [
                    "Blätter fahren zusammen - kein Widerstand",
                    "Segler-Idealfall",
                    "Minimaler Luftwiderstand"
                ],
                "disadvantages_de": [
                    "Komplex und teuer",
                    "Mechanismus kann versagen",
                    "Motor-Schub muss ausreichen"
                ],
                "drag_reduction_percent_de": 95,
                "speed_gain_knots_de": 1.2,
                "cost_premium_percent_de": 250
            },
            "folding_propeller_de": {
                "description_de": "Propeller mit klappbaren Blättern - drehend zusammengeklappt",
                "mechanism_de": "Blätter drehen sich während Rückgang zusammen",
                "advantages_de": [
                    "Bessere Segleistung als fest",
                    "Günstiger als Feathering",
                    "Zuverlässiger"
                ],
                "drag_reduction_percent_de": 60,
                "speed_gain_knots_de": 0.75,
                "cost_premium_percent_de": 150,
                "reliability_de": "Gut - weniger Mechanik als Feathering"
            },
            "speed_comparison_de": {
                "no_propeller_knots_de": 8.5,
                "fixed_propeller_knots_de": 8.0,
                "folding_propeller_knots_de": 8.75,
                "feathering_propeller_knots_de": 9.7
            }
        },
        "materials": {
            "manganese_bronze_de": {
                "composition_de": "Cu 62%, Zn 36%, Fe 1%, Mn 1%",
                "yield_strength_kpsi_de": 65,
                "advantages_de": [
                    "Korrosions-resistent",
                    "Gute Ermüdungsfestigkeit",
                    "Standard-Material"
                ],
                "disadvantages_de": [
                    "Schwächer als Nickel-Aluminium",
                    "Kann sich abnutzen bei Sand",
                    "Dezinifikation möglich"
                ],
                "cost_premium_percent_de": 100
            },
            "nibral_de": {
                "composition_de": "Nickel 5%, Aluminium-Bronze mit Nickel",
                "yield_strength_kpsi_de": 90,
                "strength_advantage_percent_de": 38,
                "advantages_de": [
                    "38% stärker als Manganbronze",
                    "Bessere Korrosions-Resistenz",
                    "Länger haltbar"
                ],
                "disadvantages_de": [
                    "Teurer",
                    "Schwerer"
                ],
                "cost_premium_percent_de": 300,
                "recommended_for_de": "Motoren >50 PS und größere Propeller"
            }
        },
        "sizing_principles": {
            "description_de": "Propeller müssen für maximale Effizienz richtig dimensioniert sein",
            "diameter_formula_de": "Abhängig von Motor-Drehzahl und Schiff-Geschwindigkeit",
            "pitch_definition_de": "Vorwärts-Fortschritt pro Umdrehung in Zoll",
            "typical_diameter_inch_de": 14,
            "typical_pitch_inch_de": 12,
            "slip_percent_de": 10,
            "designer_spec_de": "Motor sollte bei voller Last 90-95% der maximalen Drehzahl erreichen",
            "oversized_consequence_de": "Motor kann nicht volle Drehzahl erreichen - Leistung verloren",
            "undersized_consequence_de": "Motor läuft zu schnell - Verschleiß, Treibstoff-Verschwendung"
        },
        "cavitation": {
            "description_de": "Dampfblasen-Bildung hinter Propeller - Verschleiß und Lärm",
            "mechanism_de": "Druck fällt unter Dampfdruck - Blasen bilden sich",
            "consequence_de": "Verschleiß an Propeller-Oberfläche, Lärm, Vibrationen",
            "prevention_de": [
                "Propeller tief genug im Wasser",
                "Zu hohe Drehzahl vermeiden",
                "Glatte Propeller-Oberfläche",
                "Richtiges Profil-Design"
            ]
        }
    }
}


STEERING_DATABASE: Dict[str, Any] = {
    "description_de": "Umfassende Datenbank für Schiffs-Steuerungssysteme",
    "cable_steering": {
        "description_de": "Mechanische Stahlseil-Steuerung - traditionell und zuverlässig",
        "cable_construction_de": "7x19 Stahlseil - sieben Litzen zu neunzehn Drähten",
        "diameter_mm_de": 5,
        "diameter_inches_de": 0.2,
        "breaking_strength_kn_de": 24,
        "expected_lifespan_years_de": 15,
        "lifespan_consequence_de": "Nach 15 Jahren: Seil wird brüchig - Austausch erforderlich",
        "initial_tension_procedure_de": "Spannung mit Federwage eingestellen - etwa 200-250 N",
        "tension_management_critical_de": True,
        "slack_risk_de": "Lockeres Seil = KATASTROPHAL - Steuer antwortet nicht",
        "over_tension_risk_de": "Zu straff = Steuer schwergängig, Kabel-Verschleiß",
        "tension_check_frequency_months_de": 1,
        "retensioning_procedure_de": {
            "symmetric_half_turns_de": "Jeweils halbe Umdrehung an oberer und unterer Schraube",
            "why_symmetric_de": "Hält Spannung in beide Richtungen gleich",
            "maximum_total_turns_de": 3,
            "exceeding_limit_consequence_de": "Seil reißt - Steuer funktioniert nicht mehr",
            "tool_required_de": "Schlüssel passend zu Spannschraube"
        },
        "cable_routing_critical_de": "Seil muss sanfte Kurven haben - keine scharfen Kanten",
        "inspection_frequency_months_de": 6,
        "what_to_check_de": [
            "Seil auf Freilegung von Drähten prüfen",
            "Kinks oder Knoten suchen",
            "Korrosion auf Seil",
            "Rollen auf Verschleiß prüfen",
            "Spannung testen"
        ],
        "cable_damage_consequence_de": "Kann plötzlich reißen - Steuer ausfallen",
        "replacement_procedure_de": {
            "new_cable_length_feet_de": "Mess-Fahrt erforderlich",
            "installation_cost_usd_de": 400,
            "parts_cost_usd_de": 250,
            "labor_time_hours_de": 5
        }
    },
    "hydraulic_steering": {
        "description_de": "Hydraulisches Lenkrad - komfortabel aber komplexer",
        "component_system_de": [
            "Lenkrad mit Drehventil",
            "Hydraulic pump",
            "Druckschalter",
            "Hydraulic cylinder am Ruder",
            "Return line zum Tank"
        ],
        "hydraulic_fluid_type_de": "ISO VG 46 (Marinequalität)",
        "fluid_volume_liters_de": 2,
        "fluid_change_interval_years_de": 3,
        "pressure_rating_bar_de": 210,
        "common_failure_modes_de": {
            "leaking_cylinder_de": {
                "symptom_de": "Hydraulik-Öl tritt aus Ruderstamm",
                "consequence_de": "Steuer wird spongy - verliert Druckkraft",
                "repair_cost_usd_de": 600
            },
            "pump_failure_de": {
                "symptom_de": "Hohe Lärm beim Steuern - Pumpe keift",
                "consequence_de": "Pumpe kann nicht genug Druck aufbauen",
                "repair_cost_usd_de": 1200
            },
            "hose_rupture_de": {
                "symptom_de": "Plötzlicher Druckverlust - Steuer kann nicht mehr drehen",
                "consequence_de": "Steuer blockiert - Motor nur von Hand zu lenken",
                "repair_cost_usd_de": 300
            },
            "valve_sticking_de": {
                "symptom_de": "Steuer-Widerstand auf einer Seite größer",
                "consequence_de": "Steuer reagiert asymmetrisch",
                "repair_cost_usd_de": 450
            }
        },
        "bleeding_procedure_de": {
            "purpose_de": "Luft aus Hydraulik-System entfernen",
            "procedure_de": [
                "Lenkrad mehrfach in volle Kurven drehen",
                "Entlüftungsventile oben öffnen",
                "Warten bis Ölblasen aufhören",
                "Ventile wieder schließen",
                "Wiederholung bis Steuer wieder reaktiv"
            ],
            "typical_time_minutes_de": 10,
            "common_issue_de": "Nach Hydraulik-Arbeit immer bluten"
        }
    },
    "emergency_tiller": {
        "description_de": "Mechanischer Ruder-Backup für Steuer-Ausfall - KRITISCH",
        "function_de": "Hebel am Ruderschaft - ermöglicht Handsteuerung",
        "location_typical_de": "Unter Deck, direkt am Ruderschaft",
        "material_de": "Edelstahl 316 oder Aluminium",
        "length_inches_de": 48,
        "leverage_mechanical_advantage_de": 10,
        "importance_de": "ABSOLUT NOTWENDIG - Backup wenn Hauptsteuer versagt",
        "known_problem_de": "Funktioniert oft nicht wenn gebraucht - verrostet, blockiert, falsch installiert",
        "failure_statistics_percent_de": 40,
        "why_failure_occurs_de": [
            "Rost am Ruderschaft - Tiller-Verbindung blockiert",
            "Korrosion an Bolzen",
            "Zu fest angezogen oder zu lose",
            "Auf Deck deponiert - wird vergessen",
            "Falsch installiert - passt nicht auf Schaft"
        ],
        "regular_practice_mandatory_de": True,
        "practice_frequency_months_de": 6,
        "practice_procedure_de": "Tiller vollständig aufsetzen - langsam drehen - sollte leicht gehen",
        "if_stuck_de": [
            "Kein Gewalt - Metall kann biegen",
            "WD-40 oder Penetrating Oil verwenden",
            "24 Stunden einweichen lassen",
            "Erneut versuchen",
            "Bei Blockade: Korrosion-Entfernung erforderlich"
        ],
        "corrosion_prevention_de": [
            "Monatliche Inspektion",
            "Dünn Öl-Schutzschicht",
            "Lagerung trocken",
            "Regelmäßiger Aufsatz-Test"
        ],
        "cost_de": 400,
        "replacement_labor_hours_de": 3
    },
    "autopilot": {
        "description_de": "Automatische Steuersystem-Pilot",
        "system_types_de": {
            "linear_autopilot_de": {
                "mechanism_de": "Linear-Aktor mit elektrischer Schubstange",
                "power_source_de": "12V oder 24V DC motor mit Schraube",
                "force_output_newtons_de": 500,
                "speed_mm_per_second_de": 5,
                "advantages_de": [
                    "Einfach",
                    "Günstig",
                    "Zuverlässig"
                ],
                "disadvantages_de": [
                    "Langsam",
                    "Nicht für große Ruder",
                    "Kann unter Last stecken bleiben"
                ]
            },
            "hydraulic_autopilot_de": {
                "mechanism_de": "Hydraulic pump gesteuert durch Kompass-Signal",
                "power_source_de": "Elektrisches Ventil mit Hydraulik-Zylinder",
                "force_output_newtons_de": 5000,
                "speed_mm_per_second_de": 50,
                "advantages_de": [
                    "Kraftvoll",
                    "Schnell",
                    "Große Ruder",
                    "Glatt"
                ],
                "disadvantages_de": [
                    "Komplex",
                    "Teuer",
                    "Wartung erforderlich",
                    "Lecks möglich"
                ]
            },
            "wheel_drive_autopilot_de": {
                "mechanism_de": "Direkter Lenkrad-Antrieb mit Motor-Rad",
                "power_source_de": "12V oder 24V DC motor auf Lenkrad",
                "force_output_newtons_de": 300,
                "advantages_de": [
                    "Einfache Installation",
                    "Keine zusätzliche Mechanik",
                    "Reversible"
                ],
                "disadvantages_de": [
                    "Schwach für große Ruder",
                    "Kann Lenkrad-Verschleiß erzeugen",
                    "Nicht für Cable-Steuerung ideal"
                ]
            }
        },
        "sizing_problem_most_common_issue_de": {
            "issue_de": "UNDERSIZING - häufigster Fehler",
            "description_de": "Zu kleine Autopilot für Ruder-Größe gewählt",
            "consequence_de": [
                "Autopilot kann nicht stark genug drehen",
                "Motor muss helfen steuern",
                "Autopilot-Motor überlastet",
                "Steuer wird spongy und unzuverlässig"
            ],
            "typical_mistake_de": "Nach Specs dimensionieren ohne Sicherheitsfaktor"
        },
        "raymarine_sizing_standards_de": {
            "Type_2_range_de": "Bis 22000 kg Schiffgewicht",
            "Type_3_range_de": "Bis 35000 kg Schiffgewicht",
            "Type_4_range_de": "Bis 50000 kg Schiffgewicht",
            "selection_procedure_de": "Schiffgewicht + 20% Safety Margin",
            "consequence_of_undersizing_percent_de": "30% der Autopilot-Ausfälle"
        },
        "rpm_drop_under_load_de": {
            "phenomenon_de": "Motor-Drehzahl fällt wenn Autopilot hart arbeitet",
            "cause_de": "Starke Ruder-Belastung erzeugt hohen Stromverbrauch",
            "symptom_de": "Motor läuft langsamer, rauer",
            "consequence_de": "Ladegenerator kann nicht nachkommen - Batterie sinkt",
            "solution_de": [
                "Größerer Autopilot",
                "Separate Batterie für Autopilot",
                "Motor-Drehzahl erhöhen beim Autopilot-Einsatz",
                "Kürzere Kurswechsel-Zeiten"
            ]
        },
        "compass_calibration_critical_de": True,
        "compass_error_consequence_de": "Auch 3° Fehler erzeugt konstantes Kurs-Abdriften",
        "compass_check_frequency_months_de": 6,
        "compass_deviation_deviation_pattern_de": "Lokale magnetische Störungen können variieren"
    }
}

# End of exhaustive technical knowledge database
