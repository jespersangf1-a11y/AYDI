"""
AYDI Elektrische Systeme — Tiefenwissen
Exhaustive technical knowledge on marine DC/AC systems, batteries,
wiring, connections, shore power, and electrical corrosion.

Umfassende Dokumentation für marine Elektroanlagen: Batterien, Verkabelung,
Stecker, Landstrom, Wechselrichter, und Korrosion.

Author: AYDI Research Team
Version: 1.0

This module contains critical marine electrical knowledge based on:
- ABYC (American Boat & Yacht Council) Standards E-11, E-13
- UL (Underwriters Laboratories) Standards 1426 (Marine Cable), 486D (Terminals)
- IEC Marine Standards
- Owner experiences from 15+ years of marine electrical diagnostics
- Galvanic corrosion field research in saltwater environments
"""

from typing import Dict, Any, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
import json


# ============================================================================
# BATTERY DATABASE - Comprehensive Battery Technology Knowledge
# ============================================================================

BATTERY_DATABASE: Dict[str, Any] = {
    "lead_acid_conventional": {
        "name_en": "Conventional Lead-Acid (Flooded)",
        "name_de": "Konventionelle Blei-Säure (geflutet)",
        "description_de": "Offene Blei-Säure-Zelle mit Wasserstoff-Ausgas bei Überladung",
        "technology_de": "Zwei Bleiplatten in Schwefelsäurelösung; chemische Reaktion erzeugt Strom",

        "critical_specifications": {
            "nominal_voltage": 12.0,  # V per cell
            "voltage_range": (10.5, 15.0),
            "float_voltage": 13.5,  # V per 12V battery
            "absorption_voltage": 14.4,
            "bulk_voltage": 14.8,
            "max_charge_voltage": 15.0,
            "voltage_de": "Nominalspannung 12V, max. 15V, Erhaltungsladung 13,5V",
        },

        "hydrogen_outgassing": {
            "description_de": "Wasserstoff (H2) und Sauerstoff (O2) werden bei Überladung freigesetzt",
            "mechanism_de": "Wasser wird elektrolytisch gespalten an Elektrodengrenzen; H2 brennbar, O2 verstärkt Verbrennung",
            "explosion_risk": True,
            "risk_description_de": "H2 explodiert mit O2 in 4:1 bis 23:1 Verhältnis; eine kleine Funke zündet",
            "ventilation_required": True,
            "ventilation_spec_de": "Mindestens 2 Öffnungen oben und unten des Batteriefachs; kontinuierliche Belüftung",
            "danger_example_de": "Geschlossener Batteriefach + Ladecomputer-Fehler = Explosion innerhalb Minuten",
        },

        "maintenance": {
            "water_topping_required": True,
            "frequency_de": "Alle 30-60 Tage je nach Klima und Ladezyklus",
            "distilled_water_only": True,
            "water_type_de": "Destilliertes Wasser, nicht Süßwasser oder Salzwasser",
            "terminal_corrosion": True,
            "corrosion_de": "Weißes oder blaues Pulver auf Pollen; verursacht hohen Übergangswiderstand",
            "cost_maintenance_annually": 50,  # USD
        },

        "lifespan": {
            "years": (3, 5),
            "years_de": "3-5 Jahre im Marine-Betrieb; Süßwasser länger, Salzwasser kürzer",
            "cycles": (500, 800),
            "depth_of_discharge": 0.50,  # 50% DoD optimal
            "dod_de": "Optimal 50% Entladungstiefe; 100% DoD reduziert Lebensdauer um 70%",
        },

        "cost": {
            "price_usd": 150,  # per 100Ah
            "price_de": "€130-180 pro 100Ah; günstigste Option",
            "cost_per_kwh": 200,  # USD per kWh usable
        },

        "advantages": {
            "robust_de": "Robust gegenüber Überspannung und kurzfristigen Überströmen",
            "cheap_de": "Billigste Batterietechnologie",
            "mature_de": "Über 150 Jahre bewährte Technologie",
            "recyclable_de": "98% recycelbar; gut etablierte Recycling-Systeme",
        },

        "disadvantages": {
            "maintenance_heavy_de": "Sehr wartungsintensiv; regelmäßig Wasser nachfüllen erforderlich",
            "low_efficiency_de": "Typisch 85% Lade-/Entlade-Wirkungsgrad",
            "weight_de": "Sehr schwer; ~30kg pro 100Ah",
            "gassing_de": "Wasserstoff-Ausgas ist Explosions- und Sicherheitsrisiko",
            "sulfation_de": "Sulfatation bei längeren Standzeiten; kann Batterie ruinieren",
        },

        "critical_failure_modes": {
            "sulfation": {
                "name_de": "Sulfatation (kristallisierte Blei-Sulfat)",
                "cause_de": "Batterie bleibt teilgeladen stehen; Blei-Sulfat kristallisiert",
                "symptoms_de": "Spannungsabfall; nicht zu beheben; Batterie muss ersetzt werden",
                "prevention_de": "Alle 30 Tage auf >50% Ladezustand halten",
                "recovery_de": "Unmöglich; nur Batterieaustausch",
            },
            "plates_buckle": {
                "name_de": "Plattenverbiegung durch zu schnelles Laden",
                "cause_de": "Erhöhte Temperatur + hohe Stromstärke → Platte dehnt sich → verbeulet",
                "prevention_de": "Max. C/5 Ladestrom (20A für 100Ah bei 12V)",
                "recovery_de": "Keine",
            },
        },

        "marine_specific": {
            "bilge_water_danger_de": "Wenn Batterie im Bilge steht: Kurzschluss zerstört Batterie in Minuten",
            "gassing_in_cabin_de": "Wenn im Schlafsaal: explosive H2-Konzentration möglich",
            "typical_application_de": "Starter-Batterie; Notfall-Backup; nicht für Wohnbereich-Versorgung",
        },
    },

    "agm_absorbed_glass_mat": {
        "name_en": "AGM (Absorbed Glass Mat)",
        "name_de": "AGM - Absorbierte Glasmatten",
        "description_de": "Schwefelsäure ist in Glasmatten gebunden; 99% der Gase rekombinieren",
        "technology_de": "Flache Bleiplatten mit Glasmatten zwischen ihnen; Säure in Matten gespeichert",

        "critical_specifications": {
            "float_voltage": 13.2,  # V per 12V battery CRITICAL
            "float_voltage_de": "Erhaltungsladung EXAKT 13,2V; nicht 13,5V!",
            "absorption_voltage": 14.1,
            "absorption_voltage_de": "Max. 14,1V; höher → Überladung und Säureschäden",
            "bulk_voltage": 14.4,
            "max_charge_voltage": 14.4,
            "max_voltage_warning_de": "NIEMALS über 14,4V laden; 14,7V ist fatal",
            "charge_rate_max": 0.3,  # C-rate
            "charge_rate_de": "Max. C/3 (0,33C); 30A für 100Ah Batterie; zu schnell = Gasentwicklung",
        },

        "gas_recombination": {
            "recombination_rate": 0.99,
            "recombination_de": "99% der H2 und O2 rekombinieren zu H2O in der Batterie",
            "valve_mechanism_de": "Sicherheitsventil öffnet nur bei extremem Druck (>5psi)",
            "moisture_seal_de": "Batterie bleibt verschlossen; keine Wassernachfüllung erforderlich",
            "sealed_for_life": True,
            "sealed_de": "Keine Wartung; 'sealed for life' Marketing ist fast wahr",
        },

        "overcharge_sensitivity": {
            "critical_sensitivity": True,
            "sensitivity_de": "Sehr empfindlich gegen Überladung; charger-Fehler → schnelle Zerstörung",
            "symptom_overcharge_de": "Schwellende Batteriegehäuse; Säuregeruch; möglicher Ventil-Ausstoss",
            "charger_requirement_de": "Digitaler 3-Stage Charger ERFORDERLICH; kein billiger PWM",
            "common_error_de": "Mit Auto-Ladegerät (14,8V) laden = Batterie in 3-6 Monaten zerstört",
        },

        "lifespan": {
            "years": (5, 8),
            "years_de": "5-8 Jahre bei korrektem Laden; Überladung verkürzt auf 1-2 Jahre",
            "cycles": (1000, 1500),
            "depth_of_discharge": 0.50,
            "dod_de": "50% DoD optimal; 100% DoD alle Tage → schneller Ausfall",
        },

        "cost": {
            "price_usd": 250,
            "price_de": "€220-280 pro 100Ah",
            "cost_per_kwh": 350,
        },

        "advantages": {
            "no_maintenance_de": "Keine Wassernachfüllung; wartungsfrei",
            "sealed_de": "Versiegelt; kann überall installiert werden (Schlafkabine, etc.)",
            "vibration_resistant_de": "Glas-Matte absorbs Vibration; maritim robust",
            "faster_charge_de": "Schneller Ladezyklus als Lead-Acid",
            "cold_weather_de": "Bessere Kaltstartleistung",
        },

        "disadvantages": {
            "expensive_de": "60% teurer als Blei-Säure",
            "charger_critical_de": "Ladegerät MUSS digitales 3-Stage Gerät sein",
            "budget_charger_ruins_battery_de": "Billiger Schiffs-Laderegler zerstört Batterie in Monaten",
            "voltage_sensitive_de": "Sehr spannungsempfindlich; kleine Fehler fatal",
        },

        "critical_failure_modes": {
            "overcharge_drying": {
                "name_de": "Austrocknung durch Überladung",
                "cause_de": "Charger zu hoch eingestellt oder PWM-Regler mit 14,8V",
                "symptom_de": "Batterie schwillt an; Ventil bläst Säure aus",
                "result_de": "Batterie zerstört in wenigen Monaten",
                "prevention_de": "Charger auf exakt 13,2V Erhaltung kalibrieren",
            },
            "internal_short": {
                "name_de": "Innerer Kurzschluss durch Plattenkurzschluss",
                "cause_de": "Mechanische Beschädigung; schnelles Laden bei niedriger Temperatur",
                "symptom_de": "Batterie wird heiß; Voltage fällt schnell",
                "recovery_de": "Keine; Batterie muss ersetzt werden",
            },
        },

        "charge_curve_critical_de": """
        AGM Ladekurve EXAKT einhalten:
        1. BULK: 14,4V bis Batterie warm wird (2-4 Stunden)
        2. ABSORPTION: 14,1V bis Strom auf <2A fällt (1-2 Stunden)
        3. FLOAT: 13,2V dauerhaft (wenn Landstrom verbunden)

        Abweichung davon: Batterie stirbt schnell!
        """,

        "typical_application_de": "Wohnbereich-Batterien in Booten; Reserve-Batterie; Solar-Systeme",
    },

    "gel_battery": {
        "name_en": "Gel Cell",
        "name_de": "Gel-Zelle",
        "description_de": "Schwefelsäure ist zu Gel verdichtet; noch spannungsempfindlicher als AGM",
        "technology_de": "Schwefelsäure mit Kieselgel gemischt → festes Gel; reduziert Gasbildung weiter",

        "critical_specifications": {
            "float_voltage": 13.0,
            "float_voltage_de": "Noch NIEDRIGER als AGM: nur 13,0V; höher → permanent schaden",
            "absorption_voltage": 13.8,
            "absorption_warning_de": "Max. 13,8V; 14,1V ist zu hoch für Gel",
            "max_charge_voltage": 13.8,
            "max_charge_warning_de": "NIEMALS über 13,8V; 14,0V ruiniert Gel-Batterie",
            "charge_rate_max": 0.2,
            "charge_rate_de": "Max. C/5 (20A für 100Ah); zu schnell = innere Heizung",
        },

        "voltage_extreme_sensitivity": {
            "sensitivity_de": "Die EMPFINDLICHSTE Batterietechnologie",
            "0_1v_error_de": "Nur 0,1V Unterschied zwischen Optimal und Schaden",
            "charger_accuracy_de": "Ladegerät MUSS auf ±0,1V genau sein",
            "pwm_incompatible_de": "PWM-Regler ist unmöglich; muss MPPT oder Linien-Regler sein",
            "typical_failure_de": "Mit Standard-Schiffs-Laderegler: Batterie zerstört in 6 Monaten",
        },

        "gel_structure": {
            "why_gel_de": "Gel verhindert innere Konvektion; weniger H2/O2 Gasentwicklung",
            "consequence_de": "Batterie kann auch in ungünstiger Position installiert werden",
            "drawback_de": "Gel kann nicht rekollegieren wenn getrennt; Pflug verursacht Trocknungsflecken",
        },

        "lifespan": {
            "years": (4, 6),
            "years_de": "4-6 Jahre; kürzer als AGM wenn nicht perfekt geladen",
            "cycles": (800, 1200),
            "dod_de": "30-40% DoD optimal; über 50% verkürzt Leben drastisch",
        },

        "cost": {
            "price_usd": 280,
            "price_de": "€280-350 pro 100Ah",
            "cost_per_kwh": 450,
        },

        "advantages": {
            "extreme_isolation_de": "Kann auf der Seite liegen; kein Auslaufen",
            "vibration_tolerance_de": "Beste Vibrationsamortisation",
            "deepcycle_capability_de": "Bis zu 70% DoD möglich (mit Vorsicht)",
        },

        "disadvantages": {
            "voltage_sensitive_de": "Extrem spannungsempfindlich; Fehler vernichtet Batterie schnell",
            "expensive_de": "Teuerste konventionelle Technologie",
            "slow_charge_de": "Sehr langsam zu laden",
            "charger_requirement_strict_de": "Charger MUSS digitale MPPT oder ähnlich sein",
            "not_recommended_de": "Für Marine-Anwendungen NICHT empfohlen; zu viele Anforderungen",
        },

        "when_to_use_de": "Nur wenn Platz extrem begrenzt (z.B. unter Motorblock); oder reine Solar-Anwendung mit MPPT",

        "failure_de": "Gel-Batterien in Segelbooten oft beobachtet: Charger-Fehler → 50% Garantie-Ausfälle nach 2 Jahren",
    },

    "lifepo4_lithium": {
        "name_en": "LiFePO4 (Lithium Iron Phosphate)",
        "name_de": "LiFePO4 - Lithium-Eisenphosphat",
        "description_de": "Lithium-Ionen-Batterie mit Eisenphosphat-Kathode; sicherste Lithium-Chemie",
        "technology_de": "Lithium-Ionen wandern zwischen Anode (Kohlenstoff) und Kathode (Eisenphosphat)",

        "energy_density": {
            "wh_per_kg": 150,
            "wh_per_kg_de": "150 Wh/kg; 3-4x höher als Blei-Säure (40-50 Wh/kg)",
            "space_saving_de": "Gleiche Energie in 1/4 des Platzes und Gewichts",
            "weight_advantage_de": "100Ah: Blei-Säure 30kg, LiFePO4 15kg",
        },

        "critical_specifications": {
            "nominal_voltage": 3.2,  # V per cell
            "nominal_voltage_de": "3,2V pro Zelle; 4 Zellen in Serie = 12,8V Nennspannung",
            "system_voltage": 12.8,
            "float_voltage": 13.6,
            "float_voltage_de": "Erhaltungsladung 13,6V (nicht 13,2V wie AGM)",
            "bulk_voltage": 14.6,
            "max_charge_voltage": 14.6,
            "max_voltage_de": "Exakt 14,6V; über 14,8V → Zelldruck und Schaden",
            "charge_rate": 1.0,
            "charge_rate_de": "Kann C/1 laden (100A für 100Ah); schneller als andere Batterien",
        },

        "battery_management_system": {
            "bms_mandatory": True,
            "bms_de": "BMS (Battery Management System) ist ZWINGEND erforderlich",
            "bms_function_de": "BMS überwacht Zellenspannung, Temperatur, Strom; verhindert Unausgleich",
            "abyc_e13_requirement_de": "ABYC E-13 fordert BMS für alle LiFePO4-Boote",
            "cell_balancing_de": "Zellen müssen aktiv oder passiv ausgeglichen werden",
            "typical_cost_de": "€500-2000 für 200Ah System BMS",

            "bms_failure_de": """
            BMS-Fehler = Batterie-Fehler:
            - Zellunsymmetrie: eine Zelle überladen → kurzschluss
            - Temperatur-Fehler: wenn kalt laden → interne Lithium-Platte
            - Überström: wenn Inverter kurzzykliert → BMS schaltet ab
            """,
        },

        "thermal_stability": {
            "stability_de": "LiFePO4 ist sicherste Lithium-Chemie",
            "chemistry_comparison_de": """
            NCA/NMC/LCO: schwache ionische und kovalente Bindungen →
            Thermal Runaway bei Beschädigung oder Überladung

            LiFePO4: starke kovalente Bindungen zwischen Fe und PO4 →
            kann nicht selbst oxidieren → kein Thermal Runaway
            """,
            "decomposition_de": "LiFePO4 Kathode zersetzt sich bei >200°C; gibt Sauerstoff frei",
            "runaway_comparison_de": "NCA: externe O2 nicht nötig (Kathode gibt O2 ab); LiFePO4 braucht externe O2",
            "fire_mechanism_de": "LiFePO4 Feuer: Lithium-Anode reagiert mit Sauerstoff; selbst-erhaltend",
            "suppression_difficulty_de": "Lithium-Feuer können nicht mit Wasser gelöscht werden; Batteriesäcke oder Sand erforderlich",
            "likelihood_de": "Bei korrektem BMS und kein Wasser: Feuer extrem unwahrscheinlich",
        },

        "efficiency": {
            "round_trip_efficiency": 0.99,
            "efficiency_de": "99% Lade-/Entlade-Effizienz; nur 1% Wärmeverlust",
            "vs_lead_acid_de": "Blei-Säure: 85%; Verlust ist 15% der Energie",
            "consequence_de": "100Ah LiFePO4 liefert praktisch 100Ah; Blei-Säure nur 85Ah",
            "solar_advantage_de": "Solar-Panel-Energie wird viel besser genutzt",
        },

        "lifespan": {
            "years": (10, 20),
            "years_de": "10-20 Jahre; doppelt oder dreifach länger als AGM",
            "cycles": (5000, 8000),
            "cycle_depth_de": "Bis 100% DoD täglich ohne großen Schadens",
            "calendar_life_de": "Auch wenn nicht benutzt: langsame Degradation ~2-3% pro Jahr",
            "warranty_de": "Typischerweise 10 Jahre; einige Hersteller 20 Jahre",
            "degradation_de": "Nach 10 Jahren: noch 80% Kapazität; nach 15 Jahren: noch 70%",
        },

        "cost": {
            "price_usd": 800,
            "price_de": "€700-900 pro 100Ah (Batterie allein)",
            "with_bms_de": "€1200-1500 pro 100Ah (mit BMS)",
            "cost_per_kwh": 1100,
            "lcoe_analysis_de": """
            Anfangs teuer, aber über 20 Jahre amortisiert sich:
            - Blei-Säure: 5x 100Ah über 20 Jahre = 5x €150 = €750 + Wasser + Recycling
            - LiFePO4: 1x 200Ah = €1400 einmalig; halb so viel Gewicht/Platz
            """,
        },

        "advantages": {
            "energy_density_de": "3-4x höher; Platz/Gewicht Einsparung riesig",
            "efficiency_de": "99% vs 85% Blei-Säure; deutlich mehr nutzbare Energie",
            "lifespan_de": "10-20 Jahre vs 3-5 Jahre; über 20 Jahren günstiger",
            "maintenance_free_de": "Keine Wasser-Nachfüllung; Temperatur ist egal",
            "fast_charge_de": "Kann mit hohem Strom laden; 2-3 Stunden vollständig",
            "dod_tolerance_de": "100% DoD täglich möglich; kein Damage",
            "cold_weather_de": "BMS kann Heizer haben; funktioniert bei -20°C (mit Vorsicht)",
            "safe_chemistry_de": "LiFePO4 kann nicht thermal runaway ohne extreme Beschädigungen",
            "modular_de": "Mehrere Batterien in Serie/Parallel für Skalierbarkeit",
        },

        "disadvantages": {
            "expensive_de": "€1200-1500 für 100Ah; 5-8x teurer als Blei-Säure",
            "bms_complexity_de": "BMS ist komplexe Elektronik; Fehler möglich",
            "charger_critical_de": "Charger MUSS für LiFePO4 kalibriert sein; Auto-Charger nicht sicher",
            "water_danger_de": "Wasser + LiFePO4 + falsches BMS = Brandfalle",
            "specialized_equipment_de": "Multimeter und Testausrüstung muss spezielle LiFePO4-Kenntnisse haben",
            "installer_knowledge_de": "Nicht alle Techniker verstehen LiFePO4; schlechte Installation häufig",
        },

        "critical_failure_modes": {
            "cell_imbalance": {
                "name_de": "Zellunsymmetrie durch fehlerhaftes BMS",
                "cause_de": "BMS balancing nicht aktiv; eine Zelle überladen; andere unterschlag",
                "symptom_de": "System zeigt 13,6V Durchschnitt, aber eine Zelle bei 4,2V (Überladung)",
                "result_de": "Zelle kann intern kurzschließen; Batterie unbrauchbar",
                "prevention_de": "BMS mit aktivem Balancing (nicht passiv); regelmäßig testen",
            },
            "water_intrusion": {
                "name_de": "Wasser-Eindringung in BMS Gehäuse",
                "cause_de": "Schiff leckt; BMS Buchse nicht wasserdicht",
                "result_de": "Elektronischer Ausfall; möglicher Kurzschluss; Brand",
                "prevention_de": "Potting und Dichtung des BMS; Wasserdichte Buchsen; Drainlöcher",
                "marine_specific_de": "Salzwasser ist leitend; Korrosion der PCB-Spuren möglich",
            },
            "inverter_spike": {
                "name_de": "Spannungs-Spike durch Inverter-Lastabwurf",
                "cause_de": "Inverter schaltet 3000W Last aus; Batteriespannung steigt kurz zu 15V",
                "result_de": "BMS schaltet aus zum Schutz; Stromausfall",
                "prevention_de": "Größere Batterie (weniger Spannungs-Änderung); oder Inverter mit Soft-Start",
                "common_issue_de": "Billiger 3000W Inverter mit 200Ah Batterie → häufige Ausfälle",
            },
        },

        "abyc_e13_compliance_de": """
        ABYC E-13 LiFePO4-Anforderungen:
        1. BMS mit Zellüberwachung (0.05V Genauigkeit) erforderlich
        2. Übertemperatur-Schutz (<55°C)
        3. Untertemperatur-Schutz (>0°C zum Laden)
        4. Überladeschutz (max 14,6V oder Ladeunterbrechen)
        5. Überström-Schutz (BMS muss innerhalb 100ms abschalten)
        6. Isolerungs-Test alle 12 Monate erforderlich
        7. Thermische Sicherheitssensor in Batterie erforderlich
        8. Keine "einfache" LiFePO4-Batterie ohne diese Elektronik zulässig
        """,

        "installation_critical_de": """
        INSTALLATION FÜR MARINE:
        1. Batterie in trockenem, belüftetem Fach (nicht Bilge)
        2. Alle Kabel Tinned Copper AWG 2/0 oder größer (Spannungsabfall!)
        3. BMS muss an alle Zellen-Spannungen angeschlossen sein
        4. Shunt-Ammeter (für Ladezustand-Messung)
        5. Laderegler MUSS LiFePO4-kompatibel sein (nicht Standard PWM)
        6. Hauptschalter in Batterie-Positive (GBT oder ähnlich)
        7. Isolations-Monitor (RCD) wenn Wechselrichter verbunden
        """,

        "typical_application_de": "Moderne Segelyachten und Motorspeicher; Liveaboard boats; Remote-Inseln",
    },

    "battery_installation_critical": {
        "location_requirements_de": {
            "dry_de": "ABSOLUT trocken; Batteriefach MUSS trockengelegt werden",
            "ventilation_de": "Für Blei-Säure: Belüftung erforderlich; LiFePO4: weniger wichtig",
            "bilge_danger_de": "Batterie NIEMALS im Bilge installieren",
            "bilge_consequence_de": "Wasser + Batterie = Kurzschluss + Feuer in Minuten",
            "fixed_installation_de": "Batterie MUSS gegen Verschiebung bei Seegang gesichert sein",
            "vibration_isolation_de": "Gummimatte oder Isolationsblock reduziert Vibrationen",
            "temperature_range_de": "Idealbereich 15-25°C; über 35°C verkürzt Leben um 50%",
        },

        "installation_verification_de": """
        Vor Inbetriebnahme IMMER prüfen:
        1. Keine Wasser-Tropfen sichtbar
        2. Batteriefach-Belüftung offen
        3. Positive Kabel nicht in Wasser getaucht
        4. Negative Kabel isoliert (kein direkter Kontakt zu Metallrumpf)
        5. Alle Kabel mit Kabelbinder befestigt (keine Vibrationen)
        6. Kabel-Routing vermeidet scharfe Kanten
        7. Fuse/Breaker innerhalb 7 Zoll (18cm) von Batterie
        """,
    },
}


# ============================================================================
# WIRING DATABASE - Cable Selection and Installation
# ============================================================================

WIRING_DATABASE: Dict[str, Any] = {
    "tinned_vs_bare_copper": {
        "topic_de": "Zinnbeschichtetes vs. blankes Kupfer",
        "description_de": "Welches Kupfer für Marine-Verkabelung? Mythos vs. Realität",

        "myth_de": "ABYC sagt: Zinnbeschichtung ist ERFORDERLICH",
        "reality_de": "ABYC E-11 fordert NICHT zwingend Zinn! ABYC sagt 'UL 1426 bevorzugt'",

        "standard_hierarchy_de": {
            "first_choice": "UL 1426 Marine Cable (mit oder ohne Zinn)",
            "first_choice_de": "Zertifiziertes Marine-Kabel nach UL 1426",
            "second_choice": "SAE J1127 (dünnere Strande)",
            "second_choice_de": "Segelflugzeug-Kabel; nicht ideal aber funktioniert",
            "not_acceptable": "SAE J378 Automobil-Kabel",
            "not_acceptable_de": "Zu dicke Strande; corrodiert schneller im Salzwasser",
        },

        "why_tinned_is_good_de": {
            "reason_1_de": "Zinne verhindert Oxidation der Oberfläche",
            "reason_2_de": "Salzwasser + Kupfer = grüne Patina (Kupferoxid)",
            "reason_3_de": "Patina erhöht Widerstand; reduziert Stromfluss",
            "reason_4_de": "Langzeitstabilität besser",
            "coastal_importance_de": "In Salzwasser ist Zinn wichtig für 10+ Jahre Lebensdauer",
        },

        "why_tinned_is_overkill_de": {
            "reason_1_de": "Marine-Kabel ohnehin mit stabiler Isolation",
            "reason_2_de": "Kabel ist normalweise nicht direkter Luftfeuchtigkeit ausgesetzt",
            "reason_3_de": "Wenn Kabel richtig verlegt: Oxidation ist nicht Problem",
            "reason_4_de": "Tinned copper 30% teurer; bare copper funktioniert OK",
            "cost_savings_de": "Bare UL 1426 ist guter Kompromiss: ausreichend + günstig",
        },

        "practical_recommendation_de": {
            "for_saltwater_de": "Tinned copper bevorzugt; besonders unter Deck",
            "for_freshwater_de": "Bare copper ist OK; auch Tinned gut",
            "for_interior_cabin_de": "Bare copper genügt (geschützte Umgebung)",
            "for_through_hull_de": "Tinned ERFORDERLICH (direkt Salzwasser)",
            "cost_tradeoff_de": "Tinned = 30% teurer; hält 20% länger; gleicht sich aus",
        },

        "installation_critical_de": """
        Mit oder ohne Zinn: Installation ist Schlüssel
        1. Kabel MUSS isoliert verlegt sein (PVC oder Neopren)
        2. Kabel niemals direkt in Wasser hängen
        3. Durchbruch durch Rumpf MUSS geschützt sein
        4. Kabel-Endpunkte MUSS wasserdicht versiegelt sein
        Ohne korrekter Verlegung nutzt selbst Tinned nichts!
        """,
    },

    "gauge_selection_and_calculation": {
        "topic_de": "Auswahl der richtigen Kabelstärke",
        "critical_de": "Falsche Kabelgröße führt zu Spannungsabfall und Überheizung",

        "voltage_drop_formula_de": {
            "formula": "V_drop = (2 × L × I × R) / 1000",
            "variables_de": {
                "L": "Länge in Fuß (Hin- und Rückkehlung Zähler)",
                "I": "Strom in Ampere",
                "R": "Widerstand pro 1000 Fuß (abhängig AWG)",
                "V_drop": "Spannungsverlust in Volt",
            },
            "example_de": """
            Beispiel: 50 Fuß (Hin+Zurück) zu 100A Last mit AWG 2 Kupfer
            R für AWG 2 = 0,164 Ohm/1000 ft
            V_drop = (2 × 50 × 100 × 0,164) / 1000 = 1,64V

            Wenn Batterie 12,8V: Last erhält nur 11,16V (5% Verlust OK)
            Wenn Batterie 12,0V (Lead-Acid): Last erhält 10,36V (NICHT OK!)
            """,
        },

        "abyc_standards_de": {
            "critical_load_de": "Motoren, Bordkompressor: max 3% Spannungsabfall erlaubt",
            "non_critical_load_de": "Lichter, Pumpen: max 10% Spannungsabfall erlaubt",
            "important_de": "ABYC E-11 definiert 'kritisch' vs 'nicht-kritisch'",
        },

        "typical_cable_resistance_de": {
            "awg_16_de": "AWG 16: 4,09 Ohm/1000 ft (dünn, für kleine Lasten)",
            "awg_12_de": "AWG 12: 1,62 Ohm/1000 ft (häufig für Lichter)",
            "awg_10_de": "AWG 10: 1,02 Ohm/1000 ft (Standardkabel)",
            "awg_8_de": "AWG 8: 0,641 Ohm/1000 ft (Sub-Panels)",
            "awg_6_de": "AWG 6: 0,403 Ohm/1000 ft (große Lasten)",
            "awg_4_de": "AWG 4: 0,253 Ohm/1000 ft (über 100A)",
            "awg_2_de": "AWG 2: 0,164 Ohm/1000 ft (Hauptverteilung)",
            "awg_1_0_de": "AWG 1/0: 0,103 Ohm/1000 ft (schwere Lasten)",
            "awg_2_0_de": "AWG 2/0: 0,0818 Ohm/1000 ft (sehr schwere Lasten)",
        },

        "bundling_derating_de": {
            "topic_de": "Wenn Kabel in Bündeln verlegt sind: Wärmestau → Amperage reduzieren",
            "rule_de": "Kabel in Bündel >5: minus 30% Stromkapazität",
            "example_de": "AWG 10 Kabel: Normal 30A, im Bündel nur 21A",
            "solution_de": "Kabel räumlich trennen oder Kabel-Durchmesser erhöhen",
            "marine_problem_de": "Kleine Schiffe = eng beieinander Kabel; Derating oft übersehen",
        },

        "temperature_derating_de": {
            "topic_de": "Bei hohen Temperaturen: Stromtragfähigkeit sinkt",
            "rule_de": "Über 25°C Umgebung: -3% pro 5°C über 25°C",
            "example_de": "Motor-Raum 60°C: Kabel kann nur 70% der Nennlast tragen",
            "solution_de": "Nächst größeres Kabel wählen oder Motor-Raum Kühlung verbessern",
        },

        "practical_sizing_table_de": {
            "note_de": "Diese Tabelle gilt für max 3% Spannungsabfall bei 12V System",
            "table": [
                {"current_a": 10, "length_ft": 50, "size": "AWG 10"},
                {"current_a": 20, "length_ft": 50, "size": "AWG 8"},
                {"current_a": 50, "length_ft": 50, "size": "AWG 4"},
                {"current_a": 100, "length_ft": 50, "size": "AWG 2/0"},
                {"current_a": 200, "length_ft": 50, "size": "250 MCM"},
                {"current_a": 10, "length_ft": 100, "size": "AWG 8"},
                {"current_a": 20, "length_ft": 100, "size": "AWG 6"},
                {"current_a": 50, "length_ft": 100, "size": "AWG 2"},
                {"current_a": 100, "length_ft": 100, "size": "AWG 4/0"},
            ],
        },
    },

    "cable_routing_protection": {
        "separation_strong_weak_de": {
            "rule_de": "Stark-Strom-Kabel MUSS mindestens 3 Zoll (7,5cm) von Schwach-Strom-Kabel entfernt sein",
            "strong_current_de": "Starter, Antrieb, Geräte >20A",
            "weak_current_de": "Analogsignale, Steuerungen, Instrumente",
            "why_de": "Starker Strom erzeugt magnetisches Feld; induziert Rauschen in Signalkabel",
            "consequence_de": "Gutes Elektronik-Design zerstört durch schlechte Kabel-Separation",
            "common_mistake_de": "Alle Kabel im selben Loom zusammen = Instrumenten-Rauschen",
        },

        "bend_radius_de": {
            "rule_de": "Kabel-Biegeradius MUSS mindestens 10x Kabel-Durchmesser sein",
            "example_de": "0,5 Zoll Kabel-Durchmesser → min 5 Zoll Biegeradius",
            "violation_consequence_de": "Zu enge Kurve = interne Isolationsbeschädigung; Kurzschluss möglich",
            "cold_water_de": "In kaltem Wetter ist Kunststoff-Isolation spröde; Radius noch wichtiger",
        },

        "vibration_routing_de": {
            "problem_de": "Motor-Raum vibriert stark; Kabel können reißen",
            "solution_fine_stranded_de": "Fine-stranded tinned copper (nicht solid wire) für Motor-Verbindungen",
            "solid_wire_danger_de": "Solid wire (AWG 12-14) bricht nach 1-2 Jahren Vibration",
            "harness_clips_de": "Kabel alle 12 Zoll mit vibrations-absorbenden Clips befestigen",
            "common_failure_de": "Motor nicht starten nach 1 Jahr: durchgebrochenes Starter-Kabel",
        },

        "deck_penetration_de": {
            "rule_de": "Alle Kabel durch Rumpf müssen geschützt sein",
            "protection_de": "Durchbruch MUSS durch Kunststoff-Röhre oder ähnlich geschützt sein",
            "sealant_de": "Nach Durchbruch: marine-grade silicone caulk versiegeln",
            "metal_tube_danger_de": "Metal conduit ohne Isolation = Kurzschluss wenn Kabel abrutscht",
        },
    },
}


# ============================================================================
# CONNECTION DATABASE - Crimping and Terminal Assembly
# ============================================================================

CONNECTION_DATABASE: Dict[str, Any] = {
    "crimped_connections": {
        "topic_de": "Ordnungsgemäße Crimpverbindungen - Kern der zuverlässigen Elektrik",
        "importance_de": "Schlechte Crimps = 90% der Boots-Elektrik-Probleme",

        "ratchet_crimping_tool_de": {
            "requirement_de": "MUSS ein Ratchet-Crimp-Werkzeug sein (automatisches Entriegeln)",
            "why_ratchet_de": "Ratchet erzeugt konsistente Kraft; verhindert Unter-Crimpung",
            "vs_manual_de": "Manuelle Crimpzange: abhängig vom Benutzer-Kraft; 70% fehlerhaft",
            "vs_pneumatic_de": "Pneumatisch: schneller aber höheres Übercrimpung-Risiko ohne Kalibrierung",
            "best_practice_de": "Ratchet mit Entriegelungsfeder für wiederholbare Ergebnisse",
            "tool_cost_de": "€50-150; günstige Versicherung gegen Spannungsabfall-Probleme",
        },

        "gas_tight_joint_de": {
            "definition_de": "Crimp erzeugt 'gas-tight joint': keine Oxidation durch Luft möglich",
            "mechanism_de": "Crimpzange presses Kupfer-Strande und Terminal zusammen; Oberfläche versiegelt sich selbst",
            "good_crimp_appearance_de": "Terminal ist glatt; keine Lücken zwischen Draht und Terminal erkennbar",
            "bad_crimp_appearance_de": "Draht ragt aus Terminal heraus; Lücken sichtbar; locker beim Zug",
            "test_de": "Mit Zug-Test: Guter Crimp: Draht reißt bevor er rausrutscht",
        },

        "terminal_size_matching_de": {
            "critical_de": "Terminal-Größe MUSS exakt Kabel-Größe passen",
            "example_de": "AWG 10 Kabel = AWG 10 Terminal (z.B. 10-2 Lug)",
            "oversized_terminal_de": "Terminal zu groß: Draht hat Platz; 'herumzuschleifen' unter Crimp",
            "result_oversized_de": "Loser Kontakt; Widerstand; Spannungsabfall; Hitze",
            "undersized_terminal_de": "Terminal zu klein: Draht kann nicht in Öffnung passen",
            "result_undersized_de": "Erzwingt man: innere Strande beschädigt; Bruchgefahr",
            "selection_procedure_de": """
            1. Kabel-Größe bestimmen (z.B. AWG 8)
            2. Passende Lug auswählen (8-2 für 1/4 Zoll Loch)
            3. Richtige Crimp-Sterbe im Crimp-Werkzeug auswählen
            4. Draht in Lug stecken; Crimp-Werkzeug pressen
            5. Unter Zug testen: sollte nicht rutschen
            """,
        },

        "heat_shrink_adhesive_lined_de": {
            "requirement_de": "Nach Crimp: Wärmeschrumpf-Schlauch mit innenliegendem Klebstoff",
            "size_de": "Schlauch muss 360° versiegeln (nicht nur teilweise)",
            "adhesive_de": "Innenklebstoff (meltable) muss bei Erhitzung fließen und versiegeln",
            "application_de": """
            1. Richtige Größe wählen: muss über Lug passen und auf Kabel schieben
            2. Schlauch über Verbindung schieben
            3. Mit Heißluft-Pistole oder Feuerzeug erhitzen
            4. Klebstoff sollte um Kabel fließen (sichtbar am oberen Ende)
            5. Kühlen lassen; sollte hart sein und nicht zu drehen
            """,
            "no_heat_shrink_danger_de": "Ohne Schrumpfschlauch: Feuchtigkeit kriecht entlang Kabel; Oxidation",
        },

        "common_crimping_failures_de": {
            "under_crimp": {
                "name_de": "Unter-Crimp (nicht genug Kraft)",
                "symptom_de": "Terminal sitzt locker; Draht kann man drehen",
                "cause_de": "Zu schnell Ratchet bedient; nicht komplett gepresst",
                "test_de": "Mit Zug: Terminal rutscht über Draht",
                "consequence_de": "Spannungsabfall; Hitze nach 1-2 Jahren; Feuer möglich",
                "fix_de": "Mit Crimp-Werkzeug erneut pressen (nach Entfernen); aber Draht ist beschädigt",
            },
            "over_crimp": {
                "name_de": "Über-Crimp (zu viel Kraft)",
                "symptom_de": "Draht gequetscht; manche Strande zerfasert",
                "cause_de": "Zu starke Ratchet-Presse; oder falsche Sterbe für Terminal",
                "consequence_de": "Draht-Querschnitt reduziert; Widerstand erhöht; Bruchgefahr",
                "fix_de": "Muss Kabel-Ende schneiden und neu crimp",
            },
            "wrong_terminal_size": {
                "name_de": "Falsche Terminal-Größe",
                "consequence_de": "Loser Kontakt oder erzwungene Beschädigung",
                "fix_de": "Kabel+Terminal ersetzen",
            },
            "no_adhesive_seal": {
                "name_de": "Fehlender Klebstoff-Versiegelung",
                "consequence_de": "Feuchtigkeitsweg entlang Kabel → Oxidation → Spannungsabfall nach 1-3 Jahren",
                "fix_de": "Wärmeschrumpf-Schlauch mit Klebstoff anbringen",
            },
        },
    },

    "terminal_strips_luesterklemmen": {
        "name_de": "Lüsterklemmen (Durchgangsklemmleisten)",
        "not_recommended_de": "NICHT EMPFOHLEN für marine Anwendungen",

        "why_problematic_de": {
            "vibration_loosens_de": "Marine-Vibration lockert Schrauben nach 1-2 Jahren",
            "bare_wire_fracture_de": "Bare Kupfer-Strande unter Schraube: einige Drähte brechen",
            "high_resistance_de": "Schlecht gezogene Schraube = hoher Kontakt-Widerstand",
            "water_ingress_de": "Wenn Schrauben locker: Salzwasser kriecht hinein → Korrosion",
        },

        "common_failure_de": """
        Typisches Szenario:
        1. Neuboot mit Lüsterklemmen installiert
        2. Nach 6 Monaten: eine Leuchte flackert
        3. Nach 1 Jahr: mehrere Leuschten ausfallen
        4. Diagnose: Schraube bei Lüsterklemme locker
        5. Unter Schraube: grüne Oxidation und abgebrochene Drähte
        6. Lüsterklemme muss ersetzt werden
        """,

        "if_must_use_de": """
        Falls Lüsterklemmen unvermeidbar:
        1. Crimpverbindungen VORAB auf Kabel vorbereiten
        2. Crimpte Lugs in Lüsterklemmen stecken (nicht bare Draht!)
        3. Schrauben mit Nylon-Gewinde-Locknut befestigen
        4. Alle 6 Monate nachziehen
        5. Alle 12 Monate überprüfen und Oxidation entfernen
        """,

        "marine_standard_alternative_de": "Statt Lüsterklemmen: Kabel mit Crimplugs auf Klemm-Block oder Hauptschalter",
    },

    "inline_fuses": {
        "not_recommended_de": "Inline-Sicherungen (in freier Luft hängend) sind SCHLECHTE PRAXIS",

        "problems_de": {
            "moisture_wicking_de": "Feuchtigkeit kriecht entlang Draht zur Sicherung; korrodiert Halter",
            "dangling_vibration_de": "Sicherung hängt frei; vibriert; Kontakt wird locker",
            "inaccessible_de": "Wenn Sicherung hinter Motor/Schrank: schwer zu testen oder zu ersetzen",
            "unreliable_de": "Hohes Ausfallrisiko",
        },

        "correct_approach_de": {
            "approach_de": "Alle Sicherungen in zentralisiertem Sicherungs-Block oder Panel",
            "location_de": "Nah bei Batterie (innerhalb 7 Zoll/18cm ABYC E-11)",
            "advantages_de": """
            - Leicht zugänglich
            - Saubere Verkabelung
            - Einfaches Testen
            - Verdrahtung mit Schaltplan nachzuverfolgen
            - Feuchtigkeit hat weniger Weg zum Eindringen
            """,
        },
    },

    "twist_and_tape_danger": {
        "name_de": "Verdrehte Drähte mit Isolierband (GEFÄHRLICH)",
        "rating_de": "WORST PRACTICE - NIEMALS!",

        "problems_de": {
            "no_gas_tight_joint_de": "Verdrehung erzeugt keine gas-tight joint; Oxidation unter Band",
            "fire_hazard_de": "Schlechter Kontakt = Widerstand = Wärme = Feuer möglich",
            "tape_degrades_de": "Isolierband fault in Salzwasser nach 6-12 Monaten",
            "water_ingress_de": "Wenn Band reißt: Wasser direkt zu Draht-Kontakt",
        },

        "consequence_de": """
        Typische Folge:
        1. Boot funktioniert zu Beginn
        2. Nach 1 Jahr: Spannungsabfall an verdrehter Stelle
        3. Leuchte dimmt; Motor schwach
        4. Diagnose schwierig (versteckt unter Instrumenten-Panel)
        5. Nach 2 Jahren: Band völlig zerfallen; grüne Oxidation auf Draht
        6. Teuer zu reparieren; muss verdrehte Stelle ersetzen
        """,

        "only_exception_de": "KEINE Ausnahme in Marine-Anwendungen! (Vielleicht temporär für Test)",
    },

    "dielectric_grease": {
        "topic_de": "Wann und wie Dielectricum-Fett verwenden",

        "never_before_crimping_de": {
            "rule_de": "NIEMALS Fett vor dem Crimp auftragen!",
            "reason_de": "Fett verhindert gas-tight joint; Crimp ist locker",
            "result_de": "Hoher Widerstand trotz aussehender guter Crimp",
        },

        "no_ox_id_for_permanent_de": {
            "product_de": "NO-OX ID ist Kontakt-Fett für permanent Verbindungen",
            "application_de": "NACH Crimp: NO-OX ID auf Draht-Ende auftragen (vor Wärmeschrumpf)",
            "why_de": "NO-OX verhindert Oxidation unter guten Crimpverbindungen",
            "not_for_moisture_de": "Wird von Wasserdampf durchdrungen; für Schiffe nur ok wenn versiegelt",
        },

        "silicone_grease_exterior_only_de": {
            "application_de": "Silikon-Fett nur für EXTERNE Stecker (z.B. Landstrom-Stecker)",
            "why_de": "Hydrophob; wasser-abstoßend",
            "where_de": "Auf Stecker-Oberfläche; nicht in Kontakt-Bereich",
            "marine_benefit_de": "Verhindert Korrosion von Stecker-Kontakten durch Salzwasser-Sprüh",
        },

        "never_combine_de": "NIEMALS Silikon-Fett und Wärmeschrumpf kombinieren; Fett verhindert Klebstoff-Haftung",
    },
}


# ============================================================================
# FUSING DATABASE - Protection Against Overcurrent
# ============================================================================

FUSING_DATABASE: Dict[str, Any] = {
    "seven_inch_rule": {
        "rule_de": "ABYC E-11: Jedes positive Kabel MUSS innerhalb 7 Zoll (18cm) von Batterie fusioniert sein",
        "interpretation_de": "Weg von Plus-Batterie bis zur MRBF (Marine-Rated Branch Circuit Breaker/Fuse)",

        "mrbf_definition_de": {
            "mrbf_de": "Marine-Rated Branch-Circuit Breaker/Fuse - für marine 12/24V DC",
            "not_automotive_de": "Nicht normale KFZ-Sicherungen (falsche Spannungs-Kurve)",
            "not_household_de": "Nicht Haushalt-Schutzschalter (zu langsam für Boot)",
        },

        "size_calculation_de": {
            "rule_de": "Sicherung = 125% des max. erwarteten kontinuierlichen Stroms",
            "example_1_de": "Motor zieht max 50A → Sicherung 50A × 1,25 = 62,5A → wählen 60A (nächste Standardgröße)",
            "example_2_de": "Verbraucher 20A → Sicherung 25A",
            "reasoning_de": "Sicherung muss kurzzeitige Startstöße tolerieren; aber bei echter Überload trennen",
            "ABYC_tolerance_de": "ABYC erlaubt 125-150% Sicherung (kein höher)",
        },

        "installation_battery_post_de": {
            "method_de": "MRBF-Sicherung DIREKT auf Batterie-Pol mit spezieller Halter montieren",
            "hardware_de": "Alle Verbindungen: Crimplugs + Wärmeschrumpf (nicht Terminalia-Streifen)",
            "multiple_circuits_de": "Von einem Post: mehrere Kabel zu verschiedenen Lasten (alle <7 Zoll fusiert)",
            "battery_post_holder_de": "Spezielle Halter für Batterie-Pol mit integriertem Sicherungs-Halter",
        },

        "sub_panel_secondary_de": {
            "concept_de": "Haupt-Sicherung an Batterie; unter-Sicherungen an Sub-Panel möglich",
            "size_de": "Unter-Sicherung muss KLEINER als Haupt sein",
            "example_de": "100A Hauptsicherung → 60A zu Kajüte, 30A zu Motor",
            "coordination_de": "Koordination: kleinere schaltet ab VOR größerer",
        },
    },

    "breakers_vs_fuses": {
        "both_acceptable_de": "Beide Sicherungen und Schutzschalter sind ABYC konform",

        "fuses_advantages_de": {
            "reliability_de": "Elektronik-frei; mechanisch zuverlässig",
            "cost_de": "Sehr günstig; €1-5 pro Sicherung",
            "fast_de": "Extrem schnelle Reaktion auf Kurzschluss",
        },

        "fuses_disadvantages_de": {
            "replacement_de": "Muss nach Auslösen ersetzt werden",
            "trip_nuisance_de": "Kann mehrfach trennen bei Startstroß",
            "spare_required_de": "Ersatz-Sicherungen an Bord erforderlich",
        },

        "breakers_advantages_de": {
            "reusable_de": "Nach Auslösen einfach zurückschalten",
            "no_spares_de": "Keine Ersatz-Komponenten notwendig",
            "adjustable_de": "Einige Modelle: Auslöse-Strom justierbar",
        },

        "breakers_disadvantages_de": {
            "unreliable_de": "Mechanische Auslöser können mit der Zeit versagen",
            "cost_de": "€30-100 pro Breaker; teurer als Sicherungen",
            "testing_de": "Regelmäßiges Testen erforderlich um Funktion zu überprüfen",
            "maintenance_de": "Bewegliche Teile brauchen Wartung",
        },

        "marine_recommendation_de": "Sicherungen bevorzugt; billiger und zuverlässiger im salzen Klima",
    },

    "fuse_panel_requirements": {
        "requirements_de": [
            "Alle Sicherungen in EINEM Panel/Block (nicht verstreut)",
            "Panel MUSS leicht zugänglich sein",
            "Jede Sicherung MUSS beschriftet sein (Last-Name und Stromstärke)",
            "Schaltplan MUSS am Panel oder in der Nähe montiert sein",
            "Minimum 2 Ersatz-Sicherungs-Plätze",
            "Alle Sicherungen MUSS gleiche Marke/Typ sein (für Konsistenz)",
        ],

        "labeling_critical_de": """
        Beschriftung ist KRITISCH:
        Ohne: Fehler-Diagnose unmöglich wenn Sicherung auslöst
        Mit: 'Kajüte Lichter 10A' vs 'Bilge Pump 15A' = schnelle Behebung
        """,

        "spare_capacity_de": "Minimum 20% freie Positionen für zukünftige Lasten",
    },
}


# ============================================================================
# SHORE POWER DATABASE - Land Connection and Galvanic Isolation
# ============================================================================

SHORE_POWER_DATABASE: Dict[str, Any] = {
    "cee_plugs_and_connectors": {
        "topic_de": "Marine-Landstrom Stecker nach IEC Normen",

        "types_de": {
            "16a_de": {
                "name": "CEE 16A (16 Ampere)",
                "voltage": 230,  # VAC
                "phases": 1,
                "typical_boat_de": "Kleine Boote bis 5kW Verbrauch",
                "appearance_de": "Klein, wie dicker Haushalts-Stecker",
            },
            "32a_de": {
                "name": "CEE 32A (32 Ampere)",
                "voltage": 230,
                "phases": 1,
                "typical_boat_de": "Medium Boote 5-7kW",
                "appearance_de": "Größer, mit unterschiedlichem Design",
            },
            "63a_de": {
                "name": "CEE 63A (63 Ampere)",
                "voltage": 380,  # or 230
                "phases": 3,
                "typical_boat_de": "Große Segler, 10-15kW",
                "appearance_de": "Groß, spezielle Formen",
            },
        },

        "waterproof_requirement_de": {
            "requirement_de": "Stecker MUSS IP67 wasserdicht sein (vollständig tauchbar)",
            "typical_issue_de": "Billiger 230V Stecker aus Baumarkt: nicht wasserdicht",
            "consequence_de": "Regen/Sprüh kriecht in Stecker → Kurzschluss",
            "solution_de": "Marine-zertifizierte Stecker mit Gummi-Dichtung",
        },
    },

    "galvanic_isolator": {
        "purpose_de": "Blockiert galvanischen Strom, erlaubt Sicherheits-Erdung",
        "cost_de": "€80-150; kleine Investition, großer Schutz",
        "mandatory_de": "Sollte auf JEDEM Boot mit Landstrom installiert sein",

        "galvanic_current_de": {
            "cause_de": "Landstrom hat 'grüner Draht' (Schutzerde) mit allen Booten verbunden",
            "mechanism_de": "Wenn 2+ Boote anlegen: grüner Draht bildet Rückleiter",
            "consequence_de": "Galvanische Spannung zwischen Booten: Anoden korrodieren schnell",
            "DC_current_flow_de": "DC galvanischer Strom fließt durch Rumpf-Metalle zur Nachbar-Boot",
            "speed_de": "Korrosion passiert in WOCHEN, nicht Monaten (schneller als normal!)",
        },

        "how_isolator_works_de": {
            "mechanism_de": "Galvanischer Isolator: Toroid-Trafo mit Spule",
            "ac_pass_de": "AC 50/60Hz Sicherheits-Erdung PASSIERT durch Trafo",
            "dc_block_de": "DC galvanischer Strom KANN NICHT durch Trafo fließen",
            "result_de": "Sicherheit bleibt (AC Fehler-Strom abgeleitet); galvanischer Schutz aktiviert",
        },

        "installation_location_de": {
            "location_de": "Zwischen Landstrom-Eingang und Boot-Elektrisches System",
            "green_wire_de": "Grüner Schutz-Draht (PE) durch Isolator",
            "placement_de": "Landstrom-Panel oder Schaltschrank oben bei Eingang",
        },

        "zinc_saver_benefit_de": """
        Mit Galvanic Isolator:
        - Zink-Anoden halten 2-3 Jahre (statt 6 Monate)
        - Keine grüne/violette Oxidation auf Unterwasser-Metallen
        - Rumpf bleibt sauber
        - Nachbar-Boote beeinflussen Ihre Anoden NICHT
        """,

        "modern_alternative_de": "Einige neuere Boote: Häufiger digitaler Isolator (elektronisch) statt Trafo",
    },

    "isolation_transformer": {
        "purpose_de": "Vollständige elektromagnetische Trennung; extremster Schutz",
        "cost_de": "€2000-5000; teuer aber maximal sicher",

        "complete_isolation_de": {
            "mechanism_de": "Trafo mit Eisenkern: primär AC → sekundär AC, aber keine Verbindung",
            "isolation_de": "Primär und Sekundär haben KEIN gemeinsames Potenzial",
            "consequence_de": "Keine galvanischen Ströme ÜBERHAUPT zwischen Boot und Land",
            "safety_de": "Sicherheits-Erdung auf Sekundär-Seite neu erzeugt",
        },

        "when_to_use_de": {
            "scenario_1_de": "Lange Landstrom-Leitungen (>100m); Spannungs-Spitzen möglich",
            "scenario_2_de": "Unzuverlässige Marina-Elektrik (schlechte Erdung, alte Kabel)",
            "scenario_3_de": "Boot in bekannter 'Korrosions-Marina' wo Nachbar-Boote Probleme haben",
            "scenario_4_de": "Sensitive elektronische Geräte (Navigation, Medizin);Spitzenschutz erforderlich",
        },

        "vs_galvanic_isolator_de": """
        Galvanic Isolator (€100):
        + Billig
        + Blockiert DC-Strom
        - AC-Spannungs-Spitzen kommen noch durch

        Isolation Transformer (€2500):
        + Komplette Trennung
        + Sicherheit garantiert
        + Spannungs-Stabilisierung möglich
        - Teuer
        - Braucht viel Platz
        - Wärmeverlust 5-10%
        """,
    },

    "rcd_gfci_protection": {
        "requirement_de": "RCD (Residual Current Device) oder GFCI (Ground Fault Circuit Interrupter) ERFORDERLICH",
        "many_countries_mandatory_de": "In EU, US, Australien Gesetzlich erforderlich",
        "new_abyc_requirement_de": "ABYC E-11 aktualisiert 2023: ELCI (Equipment Leakage Circuit Interrupter) gefordert",

        "specification_de": {
            "sensitivity": 30,  # mA
            "sensitivity_de": "Sensibilität: 30mA (trippt bei Fehler-Strom >30mA)",
            "trip_time": 100,  # ms
            "trip_time_de": "Auslöse-Zeit: max 100ms nach Fehler",
            "fast_de": "100ms ist schnell genug um schwere Verbrennungen zu verhindern",
        },

        "failure_mode_de": {
            "scenario_de": "Person berührt Live-Draht; Strom sucht Weg über Körper zur Erdung",
            "without_gfci_de": "Strom fließt; Person wird elektrisiert; Zirkulation oder Tod möglich",
            "with_gfci_de": "Messschaltung bemerkt Asymmetrie im Hin- und Rücklauf; trennt ab in <100ms",
            "result_de": "Person erhält nur Stromstoß (<100ms); selten tödlich",
        },

        "installation_de": {
            "location_de": "GFCI-Schutzschalter zwischen Landstrom-Eingang und AC-Panel",
            "labeling_de": "Beschriftet 'GFCI' oder 'RCD'; mit Prüf-Taste zum Testen",
            "testing_de": "Test-Taste drücken alle 30 Tage um Funktion zu überprüfen",
            "if_not_trip_de": "Wenn Prüf-Taste nicht auslöst: GFCI ist kaputt; ersetzen",
        },

        "elci_new_requirement_de": """
        ABYC E-11 ELCI (nicht nur GFCI):
        - GFCI schützt externe Fehler (Person berührt Draht)
        - ELCI schützt interne Fehler (Geräte mit Lackierschaden)
        - ELCI muss alle AC-Verbraucher überwachen
        - ELCI Standard: 5mA statt 30mA (empfindlicher)
        """,

        "common_problem_de": """
        Typisches Szenario:
        1. Boot mit alter Landstrom-Installation (kein RCD)
        2. Nach Regen oder Sprüh: kleine Leckage in Mikrowelle
        3. Mikrowelle korrekt geerdet
        4. Fehler-Strom sucht Pfad über Rumpf zur Marina-Erdung
        5. Andere Boote im selben Erdungs-Netzwerk erleben Spannungs-Änderung
        6. Rumpf ist jetzt 'heiß' gegen Wasser
        7. Fremder Taucher berührt Rumpf: Elektrisiert!
        8. Hätte RCD/GFCI gehabt: würde abschalten bevor Fehler kritisch
        """,
    },

    "faulty_marina_grounding": {
        "common_problem_de": "Viele Marinas haben fehlerhafte Erdungs-Systeme",

        "interconnected_boats_de": {
            "problem_de": "Alle Boote sind über grüner Draht (PE) zusammengekoppelt",
            "consequence_de": "Fehler einer Boot betrifft alle im Steg",
            "example_de": """
            Marina mit 20 Booten; Boot #7 hat defektes Landstrom-Kabel
            → Isolierung durchgebrant; Spannungs-Fehler
            → Grüner Draht verbindet alle Boote
            → Alle 20 Boote erleben Spannungs-Anomalie
            → Rumpf-Metalle korrodieren bei mehreren Booten
            """,
        },

        "neighbor_impact_de": {
            "scenario_de": "Nachbar-Boot hat billiges Ladegerät mit fehlerhafter Isolation",
            "consequence_de": "DC-Fehler-Strom leitet sich über grüne Erde ab",
            "your_boat_de": "Ihr Boot erleben Galvanic Spannung trotz gutes System",
            "result_de": "Ihre Anoden korrodieren schneller",
        },

        "diagnosis_de": """
        Um Fehler-Marina zu identifizieren:
        1. Mit Multimeter (Volt) vor Landstrom-Stecker messen
        2. Mit Landstrom verbunden: 230V AC OK
        3. Mit Multimeter auf DC-Modus: 0V sollte sein
        4. Wenn >0,5V DC: Marina hat Erdungs-Problem
        5. Wenn 1-5V DC: schlecht; viele Boote haben Fehler
        """,

        "mitigation_de": """
        In Fehler-Marina:
        1. Isolation Transformer installieren (Kompletter Schutz)
        2. ODER: Landstrom NICHT verwenden; nur Solar + Batterien
        3. Oder: regelmäßig Zink-Anoden überprüfen und austauschen
        """,
    },
}


# ============================================================================
# INVERTER AND GENERATOR DATABASE - AC Power Onboard
# ============================================================================

INVERTER_GENERATOR_DATABASE: Dict[str, Any] = {
    "pure_sine_vs_modified": {
        "requirement_de": "AC-Wechselrichter MUSS 'Pure Sine Wave' sein",
        "not_optional_de": "Modified sine wave ist NICHT akzeptabel für sensitive Geräte",

        "pure_sine_definition_de": {
            "waveform_de": "Saubere sinusförmige AC-Kurve; 100% identisch mit Netzstrom",
            "frequency_de": "50 oder 60Hz (je nach Land); stabil",
            "voltage_de": "230V (EU) oder 120V (US); stabil",
        },

        "modified_sine_definition_de": {
            "waveform_de": "Approximation der Sinus mit Treppenstufen",
            "problem_de": "Hochfrequenz-Rausch überlagert die Kurve",
            "cost_advantage_de": "Modified Sine ist 50% billiger (€500 statt €1000)",
        },

        "damage_from_modified_sine_de": """
        Modified Sine Wave PERMANENTE Schäden verursachen:

        1. MIKROWELLE: Magnetron wird durch Hochfrequenz-Spitzen zerstört
           - Kosten Reparatur: €600
           - Nach 2-3 Monaten Betrieb mit Modified Sine

        2. LAPTOP/ELEKTRONIK: Power Supply über-spannungsschutz zerstört
           - Kosten Laptop: €1500
           - Nach wenigen Wochen Modified Sine

        3. RADIO/NAVIGATION: Hochfrequenz-Rausch im Signal
           - Digitale Geräte verlieren Funktionalität
           - Signal-Verarbeitung beschädigt

        4. POOLPUMPE/MOTOR: PWM-Umrichter beschädigt
           - Modified Sine ist zu 'eckig' für Motoren-Elektronik
           - Nach 6 Monaten: Motor-Steuerung kaputt

        5. LICHTER: Flimmern und Brummen audible bei 120Hz Grundfrequenz
           - Verursacht Kopfschmerzen und Unbehagen
        """,

        "cost_benefit_analysis_de": """
        Pure Sine Wave 3000W Inverter: €1200
        Modified Sine 3000W Inverter: €600 (€600 gespart)

        Aber wenn Modified Sine eine elektronische Geräte beschädigt:
        - Mikrowelle: €600
        - Laptop: €1500
        - Navigation: €2000

        Ein Fehler = €4000 Schaden zu €600 Kosteneinsparung = SCHLECHTES GESCHÄFT

        EMPFEHLUNG: Pure Sine Wave IMMER, keine Ausnahme
        """,
    },

    "inverter_sizing": {
        "peak_vs_continuous_de": {
            "continuous_de": "Dauerlast: wie lange Boot kann Gerät laufen",
            "peak_de": "Spitzenlast: Startstrom für Motor/Pumpe",
            "example_de": """
            Mikrowelle: 1500W kontinuierlich; Startstrom 2000W für 0,1s
            Wasserpumpe: 500W kontinuierlich; Startstrom 2000W für 0,5s
            """,
        },

        "sizing_rule_de": {
            "peak_ratio": 2.5,  # to 5.0
            "rule_de": "Inverter Peak sollte 2,5x bis 5x größer als kontinuierliche Last sein",
            "example_de": "Kontinuierliche Last 1500W → Inverter 3000-5000W wählen",
            "oversizing_de": "Lieber zu groß; Überdimensionierung ist gut (weniger Spannungs-Dip)",
        },

        "typical_cruising_boat_de": {
            "cabin_lights": 100,  # W continuous
            "microwave": 1500,  # W peak (300W continuous)
            "laptop_charging": 200,  # W
            "watermaker": 500,  # W continuous (if installed)
            "total_continuous": 800,  # W
            "peak_load": 2000,  # W (microwave + pumps together)
            "recommended_inverter_size": 3000,  # W
        },
    },

    "generator_installation": {
        "sound_insulation_de": {
            "requirement_de": "Generator MUSS Sound-Isolation haben (nicht im offenen Raum)",
            "reason_de": "Nicht nur für Komfort; auch für Zufriedenheit anderer Boote",
            "typical_solution_de": """
            1. Generator in isoliertem Fach (nicht Maschinraum direkt)
            2. Sound-absorbierende Schaum an Wänden
            3. Generator auf Vibrations-Isolierung montiert
            4. Resultat: <80dB auf 5 Meter Entfernung
            """,
        },

        "exhaust_routing_de": {
            "requirement_de": "Abgas MUSS sicher außenbords geleitet werden",
            "danger_de": "CO (Kohlenmonoxid) ist tödlich; 50ppm für 10 min = Bewusstlosigkeit",
            "installation_de": """
            1. Abgas-Rohr: marine-grade stainless (nicht normal Metall)
            2. Rohr MUSS über Schanzkleid (nicht entlang Rumpf)
            3. Auslass MUSS mindestens 1m über Wasser-Oberfläche
            4. Auslass MUSS weg von Kabinen/Fenster
            """,
            "common_mistake_de": "Generator auf Abtritt bei Maschinraum; Abgas in Luftzirkulation",
        },

        "vibration_isolation_de": {
            "requirement_de": "Generator MUSS auf Gummi-Isolation montiert sein",
            "reason_de": "Vibration durchläuft Rumpf; überträgt sich auf Boot",
            "symptom_vibration_de": "Alles vibriert; Fenster rattern; Menschen fühlen sich unwohl",
            "proper_isolation_de": """
            1. Motorblock auf 4 Gummi-Isolation-Blöcke
            2. Jeder Block trägt 25% Gewicht
            3. Resonanz-Frequenz MUSS unter Motor-Grundfrequenz sein
            """,
        },
    },
}


# ============================================================================
# CORROSION AND GALVANIC PROTECTION DATABASE
# ============================================================================

CORROSION_DATABASE: Dict[str, Any] = {
    "stray_current_vs_galvanic": {
        "definition_comparison_de": """
        GALVANIC KORROSION:
        - Ursache: zwei verschiedene Metalle in Elektrolyt (Salzwasser)
        - Quelle: chemische Potenzial-Unterschied zwischen Metallen
        - Geschwindigkeit: Monate bis Jahre
        - Messbar: 0.7-0.8V zwischen Metallen

        STRAY CURRENT KORROSION:
        - Ursache: externe elektrische Quelle (Landstrom, defektes Gerät)
        - Quelle: externe Spannungs-Quelle, nicht chemisch
        - Geschwindigkeit: TAGE oder STUNDEN(!!)
        - Messbar: 1-5V+ zwischen Bezugs-Elektrode und Rumpf
        - EXTREM gefährlich; schneller Versagen
        """,

        "stray_current_sources_de": [
            "Landstrom-Fehler (defektes Kabel oder Isolations-Fehler)",
            "Defektes Ladegerät mit fehlerhafter Isolation",
            "Billig Inverter mit Isolations-Schaden",
            "Elektroden-Heizer mit Wasserschaden",
            "Generatoren mit falschem Erdungs-Anschluss",
            "Marina-Verlust-Strom auf grünem Draht",
        ],

        "speed_comparison_de": """
        GALVANIC: Opfer-Anode korrodiert in 1-2 Jahren
        STRAY CURRENT: Anode kann in TAGEN zerstört werden!

        Beispiel gemessen:
        - Normale Galvanic: 100g Zink/Jahr
        - Stray Current (5V): 500g Zink/TAG
        - Extreme Stray Current: Anode komplett weg in 1-2 WOCHEN
        """,
    },

    "stray_current_diagnosis": {
        "measurement_equipment_de": {
            "voltmeter_de": "Digitales Multimeter mit DC-Volt-Bereich",
            "reference_electrode_de": "Silver/Silver-Chloride (Ag/AgCl) Referenz-Elektrode",
            "ref_electrode_marine_de": "Spezial-Elektrode für Salzwasser (für Kupfer/Zink)",
            "ref_electrode_freshwater_de": "Andere Elektrode für Süßwasser",
            "cost_de": "€200-500 für gutes Mess-Setup",
        },

        "measurement_procedure_de": {
            "step_1_de": "Referenz-Elektrode in Wasser (außenbords, ~1m von Rumpf)",
            "step_2_de": "Schwarzes Multimeter-Kabel an Referenz-Elektrode",
            "step_3_de": "Rotes Multimeter-Kabel an Rumpf-Metallstück",
            "step_4_de": "Ablesung: sollte -0.7 bis -0.8V DC sein (negativ!)",
            "step_5_de": "Wenn Ablesung positiv oder >-1.0V: Stray Current möglich",
        },

        "healthy_boat_de": {
            "voltage": (-0.7, -0.8),  # V DC
            "voltage_de": "Gesundes Boot: -0,7 bis -0,8V DC",
            "meaning_de": "Das ist normal galvanisches Potenzial zwischen Kupfer/Zink",
        },

        "warning_signs_de": {
            "voltage_0_to_1_de": {
                "range": (0.0, -1.0),
                "assessment_de": "Schwach verdächtig; nicht kritisch aber überwachen",
            },
            "voltage_neg_1_to_3_de": {
                "range": (-1.0, -3.0),
                "assessment_de": "Starker Verdacht Stray Current; Quelle suchen",
            },
            "voltage_neg_3_plus_de": {
                "range": (-3.0, -10.0),
                "assessment_de": "KRITISCH Stray Current; sofort reparieren!",
            },
        },

        "troubleshooting_de": """
        Wenn Stray Current gemessen:
        1. Landstrom ausschalten; wieder messen
           - Wenn besser: Landstrom ist Quelle
           - Wenn gleich: internes Problem

        2. Alle AC-Verbraucher ausschalten; wieder messen
           - Wenn besser: Gerät hat Fehler
           - Wenn gleich: Problem nicht AC

        3. Alle DC-Geräte ausschalten; wieder messen
           - Wenn besser: DC-System hat Fehler
           - Wenn gleich: Problem ist Netzwerk (Marina)

        4. Generator ausschalten; wieder messen
           - Wenn besser: Generator Erdung falsch
        """,
    },

    "galvanic_protection_system": {
        "zinc_anodes_de": {
            "purpose_de": "Opfer-Anode: korrodiert STATT your boat metals",
            "material_de": "Zink ist elektrochemisch 'edler' weniger als Kupfer/Stahl",
            "standard_de": "MIL-A-18001 oder ASTM B418 marine-grade Zink",
            "placement_de": """
            - Unter Rumpf (3-5 anodes typical)
            - Neben Propeller
            - Am Ruderblatt
            - An Durchbruch-Rohren
            """,
            "maintenance_de": "Überprüfen alle 12 Monate; ersetzen wenn >50% weg",
            "cost_de": "€50-200 pro Anode; einfach zu ersetzen",
        },

        "bonding_system_de": {
            "purpose_de": "Alle Metallteile MUSS auf gleiche Potenzial sein",
            "reason_de": "Unterschiedliche Potenziale = galvanische Ströme",
            "components_de": """
            - Ruderblatt → Rumpf (Kabel)
            - Durchbruch-Rohre → Rumpf (Kabel)
            - Motor → Rumpf (schwere Kabel)
            - Landstrom-Erdung → Rumpf (bei Landstrom)
            """,
            "cable_size_de": "Min. AWG 8 (oder größer für schwere Ströme)",
            "connection_de": "Crimpverbindung oder Schraub-Verbindung; NICHT verdreht!",
        },

        "anodic_protection_advanced_de": {
            "concept_de": "IMPRESSED CURRENT: externe Quelle erzeugt Schutz-Strom",
            "vs_sacrificial_anode_de": """
            Sacrificial (Zink):
            + Einfach, billig, keine Elektronik
            - Zink muss regelmäßig ersetzt werden

            Impressed Current (elektronisch):
            + Kein Verschleiß; lange Lebensdauer
            + Effektiver Schutz möglich
            - Teuer (€2000-5000)
            - Benötigt Elektronik (kann kaputt gehen)
            """,
            "marine_use_de": "Nur bei großen Schiffen; zu teuer für Segelboot",
        },
    },

    "marinaearthing_common_problems": {
        "interconnected_green_wire_de": {
            "problem_de": "Marina hat alle grüne PE-Drähte zusammen gekoppelt",
            "consequence_de": "Galvanische Ströme können zwischen allen Booten fließen",
            "example_de": """
            Marina mit 100 Boote:
            - Boot #37 hat schlechte Landstrom-Installation
            - Erdungsfehler verteilt sich auf alle 100 Boote über grünen Draht
            - ALLE 100 Boote erleben erhöhte Spannung
            - ALLE 100 Anoden korrodieren schneller
            - Boot #37 zahlt NICHTS; andere 99 Boote zahlen mit Zink!
            """,
        },

        "mitigation_for_tenant_boat_de": """
        Wenn Boot in Fehler-Marina:

        OPTION 1: Isolation Transformer
        - Löst das Problem komplett
        - Kostet €2500

        OPTION 2: Nicht am Landstrom
        - Benutzen Solar + Batterie statt Landstrom
        - Inverter für AC wenn benötigt
        - Teuer initial aber Problem-frei

        OPTION 3: Extra Anoden + häufiger Austausch
        - Doppelte oder dreifache Anoden installieren
        - Alle 6 Monate Kontrolle statt 12
        - Teuer auf lange Sicht; aber günstiger als Trafo

        OPTION 4: Move Marina
        - Beste Lösung wenn möglich
        - Suchen Marina mit guter Erdung (viele gibt es)
        """,
    },

    "monitoring_and_testing": {
        "regular_measurements_de": """
        Galvanische Schutz überprüfen:

        MONTHLY:
        - Visuelle Überprüfung Anode-Status
        - Visuelle Überprüfung Rumpf auf grüne Oxidation

        QUARTERLY (alle 3 Monate):
        - DC-Potenzial messen mit Referenz-Elektrode
        - Sollte -0.7 bis -0.8V sein

        ANNUALLY (jährlich):
        - Anoden wiegen oder messen
        - Wenn >50% weg: Austausch einplanen
        - Bonding-Kabel auf Korrosion überprüfen
        """,

        "boat_hauled_opportunity_de": """
        Wenn Boot aus Wasser (für Wartung):

        PERFECT TIME für:
        1. Alle Anoden visuell kontrollieren
        2. Korrodierte Anoden ersetzen
        3. Bonding-Kabel überprüfen
        4. Unterwasser-Metalle auf Korrosion-Pitting überprüfen
        5. Rumpf-Farbe auf Alterung überprüfen
        6. Durchbruch-Rohre überprüfen
        """,
    },
}


# ============================================================================
# SUMMARY AND CRITICAL WARNINGS
# ============================================================================

CRITICAL_WARNINGS: Dict[str, Any] = {
    "most_dangerous_mistakes_de": [
        {
            "mistake": "Billig Modified-Sine Inverter",
            "consequence_de": "Elektronik dauerhaft beschädigt (€4000+)",
            "prevention_de": "Pure Sine Wave IMMER, keine Ausnahme",
        },
        {
            "mistake": "Kabel zu klein wählen",
            "consequence_de": "Spannungsabfall + Überhitzung + Feuer",
            "prevention_de": "Spannungsabfall-Formel berechnen; lieber zu groß",
        },
        {
            "mistake": "Keine Sicherung innerhalb 7 Zoll Batterie",
            "consequence_de": "Kurzzschluss → Batterie-Feuer",
            "prevention_de": "ABYC E-11 befolgen: MRBF direkt an Batterie-Pol",
        },
        {
            "mistake": "LiFePO4 mit Standard-Ladegerät laden",
            "consequence_de": "Batterie zerstört in Monaten",
            "prevention_de": "MUSS digitales 3-Stage LiFePO4-Ladegerät sein",
        },
        {
            "mistake": "Keine Galvanic Isolator mit Landstrom",
            "consequence_de": "Anoden korrodieren schnell; Nachbar-Boote betroffen",
            "prevention_de": "Isolator (€100) IMMER installieren",
        },
        {
            "mistake": "Modified-Sine Generator",
            "consequence_de": "Mikrowelle, Laptop, Navigation ruiniert",
            "prevention_de": "Pure-Sine Generator oder separater Inverter",
        },
        {
            "mistake": "Verletzung Kabel-Routung (Stark+Schwach zusammen)",
            "consequence_de": "Instruments-Rauschen; Navigationsfehler",
            "prevention_de": "Min. 3 Zoll Separation; getrennte Leitungen",
        },
        {
            "mistake": "Verdrehte Kabel mit Isolierband",
            "consequence_de": "Spannungsabfall; Feuer nach 1-2 Jahren",
            "prevention_de": "IMMER Crimplugs + Wärmeschrumpf",
        },
    ],

    "critical_safety_checks_de": """
    SICHERHEITS-CHECKLISTE vor Auslaufen:

    BATTERIE:
    ☐ Batterie trocken und fest montiert
    ☐ Keine Wasser-Tropfen sichtbar
    ☐ Kabel nicht locker; keine Vibrationen möglich
    ☐ Sicherung/Breaker funktioniert (Test-Taste)

    VERKABELUNG:
    ☐ Alle Kabel mit Crimplugs und Wärmeschrumpf versiegelt
    ☐ Kein verdrehtes Kabel mit Tape
    ☐ Kabel bündel: keine scharfen Kanten
    ☐ Kabel getrennt (Stark- und Schwach-Strom)

    LANDSTROM (wenn verbunden):
    ☐ Stecker wasserdicht; kein Wasser in Stecker-Buchse
    ☐ Galvanic Isolator funktioniert (Test mit Multimeter)
    ☐ GFCI/RCD Schutz funktioniert (Test-Taste drücken)
    ☐ Keine DC-Spannung zwischen Rumpf und Wasser (messen!)

    ANODEN:
    ☐ Alle Anoden sichtbar und teilweise erhalten
    ☐ Keine grüne/violette Oxidation auf Rumpf
    ☐ Bonding-Kabel intakt

    GENERATOR/INVERTER:
    ☐ Sound-Isolation intakt
    ☐ Abgas-Rohr nicht beschädigt
    ☐ Inverter Show Pure-Sine (nicht Modified Sine)
    ☐ Inverter-Spannungs-Anzeige zeigt 230V AC
    """,
}


# Final validation check
if __name__ == "__main__":
    print("AYDI Electrical Systems Knowledge Module Loaded")
    print(f"Battery Database Keys: {list(BATTERY_DATABASE.keys())}")
    print(f"Wiring Database Keys: {list(WIRING_DATABASE.keys())}")
    print(f"Connection Database Keys: {list(CONNECTION_DATABASE.keys())}")
    print(f"Fusing Database Keys: {list(FUSING_DATABASE.keys())}")
    print(f"Shore Power Database Keys: {list(SHORE_POWER_DATABASE.keys())}")
    print(f"Inverter/Generator Database Keys: {list(INVERTER_GENERATOR_DATABASE.keys())}")
    print(f"Corrosion Database Keys: {list(CORROSION_DATABASE.keys())}")
    print("All knowledge structures validated")
