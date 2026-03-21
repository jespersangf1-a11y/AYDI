"""
AYDI Dichtungs- und Abdichtungstechnik Knowledge Base
Seals, Gaskets and Sealing Technology for yacht design analysis
Author: Master Marine Sealing Engineer KnowledgeBase
Version: 1.0

Umfassendes Wissen über Dichtungsmaterialien, Dichtungsprofile, Einbautechniken
und Bewertung von Abdichtungen im Yachtbau. Von Wellendichtungen über
Luken-Profile bis zu O-Ringen und Flachdichtungen.
"""

from typing import Dict, List, Any

# ============================================================================
# SEAL MATERIALS — Dichtungsmaterialien mit vollständiger Charakterisierung
# ============================================================================

SEAL_MATERIALS = {
    "epdm": {
        "name": "EPDM (Ethylen-Propylen-Dien-Kautschuk)",
        "name_de": "EPDM-Gummi",
        "composition": {
            "base_polymer": "Ethylen-Propylen-Dien-Monomer",
            "ethylene_content_percent": "45-75",
            "diene_content_percent": "2.5-12",
            "fillers": ["Ruß (Carbon Black)", "Kieselsäure", "Kaolin", "Talkum"],
            "plasticizers": "Paraffinisches Öl",
            "vulcanization": "Schwefel oder Peroxid",
        },
        "shore_hardness_range": "40A-90A",
        "typical_shore_marine": "60A-70A",
        "temperature_range_c": {"min": -50, "max": 130, "continuous_max": 120},
        "elongation_at_break_percent": 300,
        "tensile_strength_mpa": 12,
        "compression_set_percent_70h_100c": 25,
        "uv_resistance": "ausgezeichnet",
        "ozone_resistance": "ausgezeichnet",
        "seawater_resistance": "sehr gut",
        "oil_resistance": "schlecht — quillt in Mineralöl/Diesel",
        "fuel_resistance": "ungeeignet",
        "acid_resistance": "gut (verdünnte Säuren)",
        "color_options": ["schwarz", "grau", "weiß"],
        "typical_applications": [
            "Luken-Dichtungsprofile",
            "Fenster-Dichtungen",
            "Decksdurchführungen",
            "Kokerrohr-Dichtungen",
            "Lüfterausschnitte",
            "Ankerkasten-Deckel",
        ],
        "aging_behavior": {
            "uv_years_outdoor": 15,
            "ozone_cracking": "sehr widerstandsfähig",
            "chalking": "minimal",
            "permanent_set_5yr": "10-15% bei korrekt dimensionierter Kompression",
        },
        "incompatible_with": [
            "Diesel", "Benzin", "Mineralöl", "Aromate",
            "konzentrierte Säuren",
        ],
        "standards": ["DIN 7863", "ISO 3302-1"],
    },

    "nbr_nitrile": {
        "name": "NBR (Acrylnitril-Butadien-Kautschuk)",
        "name_de": "Nitrilkautschuk (Perbunan)",
        "composition": {
            "base_polymer": "Acrylnitril-Butadien-Copolymer",
            "acn_content_percent": "18-50",
            "note": "Höherer ACN-Gehalt = bessere Ölbeständigkeit, schlechtere Kälteflexibilität",
            "fillers": ["Ruß", "Kieselsäure"],
            "vulcanization": "Schwefel",
        },
        "shore_hardness_range": "40A-90A",
        "typical_shore_marine": "70A",
        "temperature_range_c": {"min": -30, "max": 100, "continuous_max": 80},
        "elongation_at_break_percent": 400,
        "tensile_strength_mpa": 15,
        "compression_set_percent_70h_100c": 30,
        "uv_resistance": "mäßig — schützen vor direkter Sonneneinstrahlung",
        "ozone_resistance": "schlecht — Rissbildung bei Ozonbelastung",
        "seawater_resistance": "gut",
        "oil_resistance": "sehr gut — Standard für Öldichtungen",
        "fuel_resistance": "gut (Diesel), mäßig (Benzin)",
        "typical_applications": [
            "Motorraum-Dichtungen",
            "Ölkühler-Dichtungen",
            "Kraftstoffleitung-O-Ringe",
            "Hydraulik-Dichtungen",
            "Getriebe-Dichtungen",
        ],
        "aging_behavior": {
            "uv_years_outdoor": 3,
            "ozone_cracking": "anfällig — nur geschützt einbauen",
            "oil_swell_percent": "5-15 je nach ACN-Gehalt",
        },
        "incompatible_with": [
            "Ozon", "UV-Strahlung (ungeschützt)", "Ketone", "Ester",
            "chlorierte Kohlenwasserstoffe",
        ],
    },

    "fkm_viton": {
        "name": "FKM (Fluorkautschuk / Viton®)",
        "name_de": "Fluorelastomer (Viton)",
        "composition": {
            "base_polymer": "Fluoriertes Kohlenwasserstoff-Elastomer",
            "fluorine_content_percent": "66-70",
            "note": "Höherer Fluorgehalt = bessere Chemikalienbeständigkeit",
            "vulcanization": "Bisphenol oder Peroxid",
        },
        "shore_hardness_range": "60A-90A",
        "typical_shore_marine": "75A",
        "temperature_range_c": {"min": -20, "max": 200, "continuous_max": 175},
        "elongation_at_break_percent": 200,
        "tensile_strength_mpa": 10,
        "compression_set_percent_70h_200c": 20,
        "uv_resistance": "ausgezeichnet",
        "ozone_resistance": "ausgezeichnet",
        "seawater_resistance": "ausgezeichnet",
        "oil_resistance": "ausgezeichnet",
        "fuel_resistance": "ausgezeichnet (Benzin, Diesel, Biodiesel)",
        "acid_resistance": "ausgezeichnet",
        "typical_applications": [
            "Abgaskrümmer-Dichtungen",
            "Kraftstoffsystem-Dichtungen",
            "Hochtemperatur-Wellendichtungen",
            "Hydraulik-Hochdruck-O-Ringe",
            "Turbolader-Verbindungen",
        ],
        "aging_behavior": {
            "uv_years_outdoor": 20,
            "chemical_degradation": "minimal bei üblichen Medien",
        },
        "incompatible_with": [
            "Ketone (Aceton)", "Ammoniak", "niedermolekulare Ester",
            "Heißwasser >150°C langfristig",
        ],
        "cost_factor": "4-8x teurer als EPDM",
    },

    "silikon": {
        "name": "VMQ (Vinyl-Methyl-Silikon)",
        "name_de": "Silikongummi",
        "composition": {
            "base_polymer": "Polydimethylsiloxan (PDMS)",
            "fillers": ["pyrogene Kieselsäure", "gefällte Kieselsäure"],
            "vulcanization": "Peroxid oder Platin-katalysiert (LSR)",
        },
        "shore_hardness_range": "20A-80A",
        "typical_shore_marine": "50A-60A",
        "temperature_range_c": {"min": -60, "max": 200, "continuous_max": 180},
        "elongation_at_break_percent": 500,
        "tensile_strength_mpa": 8,
        "compression_set_percent_70h_150c": 15,
        "uv_resistance": "ausgezeichnet",
        "ozone_resistance": "ausgezeichnet",
        "seawater_resistance": "gut",
        "oil_resistance": "mäßig",
        "fuel_resistance": "schlecht",
        "tear_resistance": "schlecht — reißt leicht ein",
        "typical_applications": [
            "Hochtemperatur-Dichtungen (Auspuff-Bereich)",
            "Lebensmittel-Kontakt (Trinkwassersystem)",
            "Ofen-/Heizungsdichtungen",
            "Flexible Manschetten",
            "Kabeleinführungen",
        ],
        "aging_behavior": {
            "uv_years_outdoor": 20,
            "compression_set_recovery": "exzellent — bestes Rückstellverhalten",
        },
        "incompatible_with": [
            "Dampf >150°C langfristig", "Kraftstoffe", "konzentrierte Säuren/Laugen",
        ],
        "special_grades": {
            "fda_food_grade": "Für Trinkwassersysteme an Bord",
            "flame_retardant": "UL94 V-0 für Motorraum",
        },
    },

    "neopren_cr": {
        "name": "CR (Chloropren-Kautschuk / Neopren®)",
        "name_de": "Neopren (Chloropren)",
        "composition": {
            "base_polymer": "Polychloropren",
            "crystallization": "Teilkristallin bei niedrigen Temperaturen",
            "vulcanization": "Metalloxide (ZnO + MgO)",
        },
        "shore_hardness_range": "40A-90A",
        "typical_shore_marine": "60A-70A",
        "temperature_range_c": {"min": -35, "max": 100, "continuous_max": 80},
        "elongation_at_break_percent": 350,
        "tensile_strength_mpa": 15,
        "compression_set_percent_70h_100c": 30,
        "uv_resistance": "gut",
        "ozone_resistance": "gut",
        "seawater_resistance": "sehr gut",
        "oil_resistance": "mäßig bis gut",
        "flame_resistance": "selbstverlöschend — Vorteil im Motorraum",
        "typical_applications": [
            "Maschinenraum-Dichtungen",
            "Kabeldurchführungen",
            "Wellenschutzbälge",
            "Schlauchschellen-Unterlagen",
            "Motorlager-Puffer",
            "Flexible Rohr-Manschetten",
        ],
        "aging_behavior": {
            "uv_years_outdoor": 10,
            "note": "Verhärtet langsam durch Nachkristallisation bei Kälte",
        },
        "incompatible_with": [
            "Aromate", "Ketone", "oxidierend wirkende Säuren",
        ],
    },

    "butylkautschuk": {
        "name": "IIR (Isobutylen-Isopren-Kautschuk)",
        "name_de": "Butylkautschuk / Butyl-Dichtband",
        "composition": {
            "base_polymer": "Isobutylen-Isopren-Copolymer",
            "isoprene_content_percent": "0.5-3.0",
            "note": "Sehr niedrige Gasdurchlässigkeit",
        },
        "shore_hardness_range": "40A-75A",
        "temperature_range_c": {"min": -40, "max": 120, "continuous_max": 100},
        "gas_permeability": "extrem niedrig — bestes Elastomer für Gasabdichtung",
        "seawater_resistance": "sehr gut",
        "oil_resistance": "schlecht",
        "uv_resistance": "gut",
        "typical_applications": [
            "Butylband unter Decksbeschlägen",
            "Luken-Rahmen-Abdichtung (als Tape)",
            "Stringer-Laminat-Abdichtung",
            "Fensterrahmen-Vorabbdichtung",
            "Vibrationsdämpfung",
        ],
        "application_as_tape": {
            "width_mm": [15, 20, 25, 30, 50],
            "thickness_mm": [1.5, 2.0, 3.0],
            "compression_target_percent": "30-50",
            "working_temperature_c": "15-30 für Verarbeitung",
            "surface_prep": "Entfetten mit Isopropanol, kein Silikonreiniger",
        },
    },

    "ptfe": {
        "name": "PTFE (Polytetrafluorethylen / Teflon®)",
        "name_de": "PTFE / Teflon",
        "composition": {
            "base_polymer": "Polytetrafluorethylen",
            "fillers_optional": ["Glasfaser 15-25%", "Carbon 10-25%", "Bronze", "MoS2"],
            "note": "Reines PTFE = universelle Chemikalienbeständigkeit, aber hoher Kaltverlust",
        },
        "shore_hardness": "55D (Shore D, nicht A — PTFE ist ein Thermoplast)",
        "temperature_range_c": {"min": -200, "max": 260, "continuous_max": 250},
        "seawater_resistance": "ausgezeichnet — inert",
        "oil_resistance": "ausgezeichnet — inert",
        "chemical_resistance": "universell — Ausnahme: Alkalimetalle, elementares Fluor",
        "friction_coefficient": 0.04,
        "compression_creep": "hoch — PTFE kriecht unter Last (cold flow), daher korrekte Vorspannung nötig",
        "typical_applications": [
            "Wellenlager (gefüllt mit Carbon/Graphit)",
            "Ruderlager",
            "Ventilsitze",
            "Flanschdichtungen (als Flachdichtung)",
            "Gewindedichtband",
            "Stevenrohr-Gleitlager",
        ],
        "special_grades": {
            "glass_filled_15": "Bessere Druckfestigkeit, Lager",
            "carbon_filled_25": "Bestes Gleitlager-Material, geringster Verschleiß",
            "bronze_filled_40": "Höchste Wärmeleitfähigkeit, für Wellenlager",
        },
    },
}

# ============================================================================
# SEAL PROFILES — Dichtungsprofile nach Querschnittsform
# ============================================================================

SEAL_PROFILES = {
    "o_ring": {
        "name": "O-Ring",
        "name_de": "O-Ring (Runddichtring)",
        "description": "Kreisförmiger Dichtring mit rundem Querschnitt — universellste Dichtung",
        "cross_section": "rund",
        "compression_percent": {"min": 15, "max": 30, "optimal": 20},
        "materials_suitable": ["nbr_nitrile", "fkm_viton", "epdm", "silikon", "ptfe"],
        "sizing_standards": {
            "metric": "DIN 3771 / ISO 3601",
            "imperial": "AS568 (USA)",
            "japanese": "JIS B 2401",
        },
        "groove_design": {
            "groove_depth_factor": "Schnurdurchmesser × (1 - Kompression)",
            "groove_width_factor": "Schnurdurchmesser × 1.3-1.5",
            "surface_roughness_max_um": 0.8,
            "edge_radius_min_mm": 0.2,
            "fill_percent_max": 85,
            "note": "Füllung >85% führt zu Extrusion, <60% zu ungenügendem Kontakt",
        },
        "failure_modes": [
            {"mode": "Extrusion", "cause": "Spaltmaß zu groß, Druck zu hoch", "prevention": "Stützringe verwenden ab >5 MPa"},
            {"mode": "Spiralförmiger Ausfall", "cause": "Reibung bei Rotation", "prevention": "Nur für statische Anwendungen oder spezielle Compound"},
            {"mode": "Explosive Dekompression", "cause": "Gas dringt ein, dann schneller Druckabfall", "prevention": "FKM/Viton verwenden oder spezielles ED-Compound"},
            {"mode": "Compression Set", "cause": "Dauerhaft verformte Dichtung dichtet nicht mehr", "prevention": "Korrekte Materialwahl, nicht über Temperaturgrenze"},
            {"mode": "Chemischer Angriff", "cause": "Medienunverträglichkeit", "prevention": "Materialverträglichkeit prüfen vor Einbau"},
        ],
        "inspection_criteria": {
            "visual": ["Risse", "Verformung", "Quellung", "Verhärtung", "Verfärbung"],
            "dimensional": ["Schnurdurchmesser ±0.1mm", "Innendurchmesser ±0.3mm"],
            "shore_change_max_percent": 15,
        },
    },

    "lip_seal": {
        "name": "Lip Seal (Radial-Wellendichtring)",
        "name_de": "Radialwellendichtring (RWDR / Simmerring)",
        "description": "Dichtring mit Dichtlippe die auf rotierender Welle gleitet",
        "cross_section": "asymmetrisch mit Lippe",
        "typical_materials": ["nbr_nitrile", "fkm_viton"],
        "speed_max_m_s": {
            "nbr": 12,
            "fkm": 20,
            "ptfe": 30,
        },
        "pressure_max_bar": {
            "standard": 0.5,
            "with_support_ring": 7,
        },
        "sizing_standard": "DIN 3760 / DIN 3761 (ISO 6194)",
        "installation_rules": [
            "Welle: Einführschräge 15-20° am Ende",
            "Oberfläche: Ra 0.2-0.8 µm, keine Drehriefen in Einbaurichtung",
            "Härte Welle: >45 HRC empfohlen",
            "Lippe Richtung: Dichtlippe zeigt zum abzudichtenden Medium",
            "Fett auf Lippe vor Einbau — niemals trocken montieren",
            "Gehäusebohrung: H8 Toleranz, Ra <1.6 µm",
        ],
        "failure_modes": [
            {"mode": "Lippenverschleiß", "cause": "Raue Wellenoberfläche, Verschmutzung", "interval_h": 5000},
            {"mode": "Verhärtung", "cause": "Übertemperatur, Ölalterung", "sign": "Harte, rissige Dichtlippe"},
            {"mode": "Exzentrizität", "cause": "Wellenschlag, Fluchtungsfehler", "max_runout_mm": 0.3},
        ],
        "marine_applications": [
            "Propellerwellen-Dichtung (bei älteren Booten)",
            "Ruderstock-Dichtung (einfache Variante)",
            "Getriebe-Ausgangswelle",
            "Pumpen-Dichtungen",
        ],
    },

    "mechanical_face_seal": {
        "name": "Mechanical Face Seal (Gleitringdichtung)",
        "name_de": "Gleitringdichtung (GLRD)",
        "description": "Präzisionsdichtung mit zwei planen Gleitflächen — Standard für moderne Propellerwellen",
        "principle": "Rotierender Ring (auf Welle) gleitet auf stationärem Ring (im Gehäuse) mit Wasserfilm dazwischen",
        "ring_materials": {
            "rotating": ["Siliziumkarbid (SiC)", "Carbon-Graphit"],
            "stationary": ["Siliziumkarbid (SiC)", "Keramik (Al2O3)"],
            "optimal_pairing": "SiC/SiC oder SiC/Carbon — je nach Anwendung",
        },
        "secondary_seals": "O-Ringe (EPDM oder FKM) als Sekundärdichtung",
        "surface_flatness": "< 1 Lichtband (0.3 µm)",
        "brands_marine": {
            "pss": {
                "name": "PSS Shaft Seal (PYI Inc.)",
                "type": "Kohlefläche auf Edelstahl-Rotor",
                "cooling": "Selbstkühlend durch Wasserfilm",
                "maintenance": "Wartungsfrei — nur O-Ring-Wechsel alle 7-10 Jahre",
            },
            "volvo_sail_drive": {
                "name": "Volvo Saildrive Dichtung",
                "type": "Spezielle Gleitringdichtung im Saildrive-Gehäuse",
                "inspection_interval_h": 200,
                "replacement_interval_years": 7,
            },
            "tides_marine": {
                "name": "Tides Marine SureSeal",
                "type": "Lippendichtung mit Carbon-Ring",
                "cooling": "Wasserkühlung erforderlich",
            },
        },
        "installation_critical": [
            "Wellenausrichtung: max. 0.5° Winkelversatz",
            "Axialer Abstand exakt nach Hersteller — Federvorspannung muss stimmen",
            "Welle entgraten, polieren auf Ra <0.4 µm im Dichtungsbereich",
            "Einbau im Trockenen, Boot auf dem Kran",
            "O-Ringe mit Silikonöl (NICHT Vaseline!) gleitfähig machen",
            "Rohrverbindungen für Kühlwasser: Schlauchschellen doppelt sichern",
            "Nach Einbau: Dichtigkeitsprüfung zu Wasser lassen — Bilge beobachten",
        ],
        "acceptable_leakage": "PSS: 0 Tropfen nach Einfahrzeit (wenige Stunden Motorlauf)",
        "failure_modes": [
            {"mode": "O-Ring-Alterung", "cause": "UV, Ozon, Medienkontakt", "interval_years": "7-10"},
            {"mode": "Kohlering-Verschleiß", "cause": "Normal — Lebensdauer 10-15 Jahre", "sign": "Zunehmende Tropfrate"},
            {"mode": "Wellen-Riefen", "cause": "Verschmutzung zwischen Ring und Welle", "prevention": "Filter im Kühlwasserzulauf"},
        ],
    },

    "stuffing_box": {
        "name": "Stuffing Box (Stopfbuchse)",
        "name_de": "Stopfbuchse (traditionell)",
        "description": "Traditionelle Wellendichtung mit Packungsringen — komprimierbare Dichtschnur",
        "packing_materials": {
            "flax_tallow": {
                "name": "Flachs mit Talg",
                "name_de": "Werg / Flachspackung (traditionell)",
                "use": "Nur Holzboote, historische Restauration",
                "leakage": "1 Tropfen alle 10-15 Sekunden akzeptabel",
            },
            "ptfe_graphite": {
                "name": "PTFE-Graphit-Packung",
                "name_de": "PTFE/Graphit Dichtschnur",
                "use": "Standard für GFK/Stahl — moderne Stopfbuchse",
                "leakage": "1 Tropfen pro 30 Sekunden",
                "brands": ["GFO (Gore)", "Volvo Penta original"],
            },
            "ptfe_aramid": {
                "name": "PTFE-Aramid-Packung",
                "name_de": "PTFE/Kevlar Dichtschnur",
                "use": "Höhere Wellendrehzahlen",
                "speed_max_m_s": 15,
            },
        },
        "ring_count": {"min": 3, "max": 5, "typical": 4},
        "stagger_angle_deg": 90,
        "compression_adjustment": {
            "initial": "Handwarm anziehen, dann 1/4 Umdrehung",
            "running_in": "Motor laufen lassen, Welle muss tropfen",
            "final": "Nachziehen bis Tropfrate stimmt — NIEMALS komplett zudrehen!",
            "overheating_sign": "Stopfbuchse heiß (>60°C) = zu stark angezogen",
        },
        "inspection_interval_h": 100,
        "marine_use_note": "Wird zunehmend durch Gleitringdichtungen (PSS) ersetzt, aber noch Standard bei vielen Booten",
    },

    "hatch_seal_profile": {
        "name": "Hatch Seal Profile",
        "name_de": "Luken-Dichtungsprofil",
        "description": "Extrudierte EPDM- oder Silikon-Profile für Luken und Deckel",
        "profile_types": {
            "d_profile": {
                "name_de": "D-Profil",
                "cross_section": "halbrund mit flacher Klebeseite",
                "compression_percent": 25,
                "width_mm": [8, 10, 12, 14, 18],
                "height_mm": [6, 8, 10, 12, 14],
                "use": "Standard-Lukendichtung, Ankerkasten",
            },
            "p_profile": {
                "name_de": "P-Profil (Hohlkammer)",
                "cross_section": "Rundkammer mit Fuß",
                "compression_percent": 30,
                "advantage": "Geringerer Schließdruck nötig",
                "use": "Große Luken, Motorraumdeckel",
            },
            "e_profile": {
                "name_de": "E-Profil (Schlüssellochform)",
                "cross_section": "Tropfenform mit Schlitz für Klemmmontage",
                "compression_percent": 20,
                "advantage": "Kein Kleber nötig — Klemmmontage in Nut",
                "use": "Hochwertige Luken (Lewmar, Goiot)",
            },
            "omega_profile": {
                "name_de": "Omega-Profil (Fensterdichtung)",
                "cross_section": "Omega-Form umgreift Glasrand und Rahmen",
                "compression_percent": 15,
                "use": "Festverglasungen, Bullaugen-Einfassungen",
            },
            "torpedo_profile": {
                "name_de": "Torpedo-Profil (Keder)",
                "cross_section": "Rundprofil mit Keder-Nase für Nut",
                "use": "Schiebeluken, Cockpitdeckel",
            },
        },
        "material_recommendation": {
            "standard": "EPDM schwarz, Shore 60A",
            "uv_exposed": "EPDM grau oder weiß, Shore 60A",
            "high_temp": "Silikon, Shore 50A (Motorraum)",
            "fuel_contact": "FKM/Viton (Tankdeckel)",
        },
        "adhesive_systems": {
            "contact_adhesive": {
                "name_de": "Kontaktkleber",
                "brands": ["3M 1300L Marine", "Bostik 1400"],
                "surface_prep": "Schleifen P120, Reinigen mit Aceton/MEK",
                "cure_time_h": 24,
            },
            "self_adhesive": {
                "name_de": "Selbstklebend (Acrylatkleber)",
                "note": "Nur bei sauberer, fettfreier Fläche — nicht dauerhaft bei Außenanwendung",
                "min_temperature_c": 15,
            },
            "mechanical": {
                "name_de": "Klemmnut (E-Profil, Torpedo)",
                "advantage": "Wartungsfreundlich, austauschbar ohne Rückstände",
            },
        },
        "aging_signs": [
            "Verformter Querschnitt (Compression Set)",
            "Risse quer zur Längsachse",
            "Verhärtung (nicht mehr elastisch)",
            "Klebeverlust an der Montagefläche",
            "Vergrauen/Verkreiden der Oberfläche",
        ],
        "replacement_interval_years": "5-8 (Außen), 10-15 (Innen/geschützt)",
    },

    "window_seal": {
        "name": "Window Seal System",
        "name_de": "Fenster-Abdichtungssystem",
        "description": "Komplette Abdichtung von Fenstern, Bullaugen und Festverglasungen",
        "window_types": {
            "fixed_flush": {
                "name_de": "Bündig eingeklebte Festverglasung",
                "sealing_method": "PU-Klebstoff (Sikaflex 295UV oder 296)",
                "bond_width_mm": {"min": 10, "max": 15},
                "bond_thickness_mm": {"min": 3, "max": 5},
                "primer_glass": "Sika Primer-206 G+P",
                "primer_hull": "Sika Primer-209 D oder 206 G+P",
                "cure_time_days": 7,
                "movement_capability_percent": 12,
            },
            "framed_opening": {
                "name_de": "Rahmenfenster (öffenbar)",
                "sealing_method": "EPDM-Profildichtung in Rahmen",
                "compression": "15-25% des Profilquerschnitts",
                "brands": ["Lewmar", "Goiot", "Bomar", "New Found Metals"],
            },
            "porthole": {
                "name_de": "Bullauge (rund, öffenbar)",
                "sealing_method": "O-Ring oder Profildichtung",
                "bolt_torque_nm": "2-4 Nm (Messingrahmen)",
                "sealing_check": "Wassertest mit Gartenschlauch, kein Hochdruckreiniger",
            },
        },
        "failure_modes": [
            {"mode": "Klebstoff-Alterung", "cause": "UV, Flexion, thermische Zyklen", "sign": "Lücke zwischen Glas und Rumpf"},
            {"mode": "Profildichtung Compression Set", "cause": "Alterung", "sign": "Tropfwasser an Unterkante"},
            {"mode": "Rahmen-Korrosion", "cause": "Galvanische Korrosion Alu-Rahmen auf Stahlrumpf", "prevention": "Isolierung oder gleiche Legierung"},
        ],
    },

    "rudder_seal": {
        "name": "Rudder Stock Seal",
        "name_de": "Ruderkoker-Dichtung",
        "description": "Abdichtung des Ruderschafts wo er durch den Rumpf tritt",
        "seal_types": {
            "lip_seal_type": {
                "name_de": "Lippendichtung (Standard)",
                "material": "NBR oder FKM",
                "suitable_for": "Kleine bis mittlere Yachten",
                "max_shaft_diameter_mm": 60,
            },
            "pss_type": {
                "name_de": "Gleitringdichtung (Premium)",
                "suitable_for": "Große Yachten, Superyachten",
                "brands": ["Jefa Rudder Seal", "Lewmar"],
                "maintenance": "O-Ring-Wechsel alle 10 Jahre",
            },
            "stuffing_box_type": {
                "name_de": "Stopfbuchse (traditionell)",
                "suitable_for": "Ältere Boote, Langfahrtsegler",
                "advantage": "Überall auf der Welt reparierbar",
            },
        },
        "critical_points": [
            "Ruderschaft-Oberfläche: rostfrei, poliert, keine Riefen",
            "Kokerrohr-Innenfläche: glatt, korrosionsfrei",
            "Fluchtung: Ruderschaft muss mittig im Kokerrohr sitzen",
            "Schmierung: Fett über Schmiernippel (wo vorhanden)",
            "Notdichtung: Unterwasserschiff-Reparatur mit Quellpackung kennen!",
        ],
    },

    "through_hull_seal": {
        "name": "Through-Hull Fitting Seal",
        "name_de": "Rumpfdurchbruch-Abdichtung",
        "description": "Abdichtung von Seeventilen, Gebern, Transducern am Unterwasserschiff",
        "sealing_methods": {
            "sikaflex_bedding": {
                "name_de": "Sikaflex-Bettung",
                "product": "Sikaflex 291i oder 591 (nur für Unterwasser)",
                "procedure": [
                    "Bohrung bohren, Laminat versiegeln (Epoxid)",
                    "Gewinde und Flanschfläche reinigen, grundieren",
                    "Sikaflex auf Flansch und in Gewinde aufbringen",
                    "Durchbruch einsetzen, Gegenmutter mit Backing Plate",
                    "Überschüssiges Sikaflex sauber abwischen",
                    "24h aushärten lassen vor Wasserkontakt",
                ],
            },
            "flat_gasket": {
                "name_de": "Flachdichtung",
                "material": "Neopren oder EPDM, 2-3mm",
                "use": "Große Flansch-Durchbrüche (Echolotgeber)",
            },
        },
        "backing_plate": {
            "material": "GFK-Platte oder Edelstahl-Platte",
            "thickness_min_mm": 6,
            "purpose": "Druckverteilung, verhindert Delaminierung des Rumpflaminats",
        },
        "inspection_interval_years": 5,
        "replacement_trigger": [
            "Seeventil lässt sich schwer bedienen",
            "Verfärbung oder Kalkablagerung am Gewinde",
            "Rissbildung im Rumpflaminat um Durchbruch",
            "Tropfenbildung an Gegenmutter",
        ],
    },
}

# ============================================================================
# SEALANT COMPATIBILITY MATRIX — Verträglichkeitstabelle
# ============================================================================

MEDIA_COMPATIBILITY = {
    # Material → Medium → Bewertung (A=ausgezeichnet, B=gut, C=bedingt, X=ungeeignet)
    "epdm": {
        "seawater": "A", "freshwater": "A", "diesel": "X", "gasoline": "X",
        "hydraulic_oil": "X", "motor_oil": "X", "glycol_coolant": "A",
        "acetone": "X", "ethanol": "C", "uv_direct": "A", "ozone": "A",
        "steam_100c": "A", "dilute_acid": "B", "dilute_alkali": "A",
    },
    "nbr_nitrile": {
        "seawater": "B", "freshwater": "A", "diesel": "A", "gasoline": "B",
        "hydraulic_oil": "A", "motor_oil": "A", "glycol_coolant": "B",
        "acetone": "X", "ethanol": "B", "uv_direct": "C", "ozone": "X",
        "steam_100c": "C", "dilute_acid": "B", "dilute_alkali": "B",
    },
    "fkm_viton": {
        "seawater": "A", "freshwater": "A", "diesel": "A", "gasoline": "A",
        "hydraulic_oil": "A", "motor_oil": "A", "glycol_coolant": "A",
        "acetone": "X", "ethanol": "A", "uv_direct": "A", "ozone": "A",
        "steam_100c": "A", "dilute_acid": "A", "dilute_alkali": "B",
    },
    "silikon": {
        "seawater": "B", "freshwater": "A", "diesel": "X", "gasoline": "X",
        "hydraulic_oil": "C", "motor_oil": "C", "glycol_coolant": "A",
        "acetone": "X", "ethanol": "B", "uv_direct": "A", "ozone": "A",
        "steam_100c": "A", "dilute_acid": "C", "dilute_alkali": "C",
    },
    "neopren_cr": {
        "seawater": "A", "freshwater": "A", "diesel": "B", "gasoline": "C",
        "hydraulic_oil": "B", "motor_oil": "B", "glycol_coolant": "A",
        "acetone": "X", "ethanol": "B", "uv_direct": "B", "ozone": "B",
        "steam_100c": "C", "dilute_acid": "B", "dilute_alkali": "B",
    },
    "ptfe": {
        "seawater": "A", "freshwater": "A", "diesel": "A", "gasoline": "A",
        "hydraulic_oil": "A", "motor_oil": "A", "glycol_coolant": "A",
        "acetone": "A", "ethanol": "A", "uv_direct": "A", "ozone": "A",
        "steam_100c": "A", "dilute_acid": "A", "dilute_alkali": "A",
    },
}

MEDIA_NAMES_DE = {
    "seawater": "Seewasser",
    "freshwater": "Frischwasser",
    "diesel": "Diesel",
    "gasoline": "Benzin",
    "hydraulic_oil": "Hydrauliköl",
    "motor_oil": "Motoröl",
    "glycol_coolant": "Glykol-Kühlmittel",
    "acetone": "Aceton",
    "ethanol": "Ethanol",
    "uv_direct": "UV-Strahlung direkt",
    "ozone": "Ozon",
    "steam_100c": "Dampf 100°C",
    "dilute_acid": "Verdünnte Säure",
    "dilute_alkali": "Verdünnte Lauge",
}

# ============================================================================
# O-RING SIZING — Normgrößen und Nutberechnung
# ============================================================================

O_RING_SIZING = {
    "metric_standard_sizes": {
        "standard": "DIN 3771 / ISO 3601-1",
        "common_cord_diameters_mm": [1.5, 1.78, 2.0, 2.62, 3.0, 3.53, 4.0, 5.0, 5.33, 6.0, 6.99, 8.4],
        "inner_diameter_range_mm": "3 - 600",
    },
    "groove_design_static_radial": {
        "compression_percent": {"min": 15, "max": 30},
        "groove_depth": "cord_dia × 0.75 (für ~25% Kompression)",
        "groove_width": "cord_dia × 1.4",
        "surface_finish_groove_ra_um": 0.8,
        "surface_finish_seal_face_ra_um": 0.4,
        "edge_break_mm": {"min": 0.1, "max": 0.3},
        "volumetric_fill_percent": {"min": 60, "max": 85},
    },
    "groove_design_static_axial": {
        "compression_percent": {"min": 15, "max": 25},
        "groove_depth": "cord_dia × 0.80",
        "groove_width": "cord_dia × 1.3",
    },
    "stretch_and_squeeze": {
        "max_stretch_percent": 5,
        "max_compression_diametral_percent": 3,
        "note": "Bei Innendruck dehnt sich O-Ring → Innendurchmesser etwas kleiner als Nutdurchmesser wählen",
    },
    "gap_extrusion_limits_mm": {
        "10_bar": 0.10,
        "50_bar": 0.05,
        "100_bar": 0.03,
        "note": "Bei größerem Spalt → Stützringe (Back-up Rings) aus PTFE verwenden",
    },
}

# ============================================================================
# COMPRESSION AND RECOVERY — Kompressionsverhalten
# ============================================================================

COMPRESSION_BEHAVIOR = {
    "compression_set_test": {
        "standard": "ISO 815 / DIN 53517 / ASTM D395",
        "method": "25% Kompression über 70h bei Prüftemperatur",
        "result": "Compression Set % = (Ausgangshöhe - Erholungshöhe) / (Ausgangshöhe - gepresste Höhe) × 100",
        "interpretation": {
            "0_percent": "Vollständige Rückstellung — perfekt",
            "10_percent": "Ausgezeichnet — langlebige Dichtung",
            "20_percent": "Gut — Standardbereich",
            "40_percent": "Noch akzeptabel — Ende Lebensdauer naht",
            "60_percent": "Ungenügend — Dichtung tauschen",
            "100_percent": "Keine Rückstellung — Dichtung ausgefallen",
        },
    },
    "factors_affecting_set": [
        {"factor": "Temperatur", "effect": "Höhere Temperatur → mehr Set → kürzere Lebensdauer"},
        {"factor": "Kompressionsgrad", "effect": "Mehr Kompression → mehr Set, aber bessere Anfangsdichtung"},
        {"factor": "Materialtyp", "effect": "Silikon beste Rückstellung, NBR schlechteste"},
        {"factor": "Vulkanisation", "effect": "Peroxid-vernetzt besser als Schwefel-vernetzt"},
        {"factor": "Mediumskontakt", "effect": "Quellung kann Set kompensieren oder verschlechtern"},
        {"factor": "Zeit", "effect": "Logarithmisch — größter Anteil in ersten 1000h"},
    ],
    "shore_hardness_selection": {
        "30A_40A": {
            "use": "Weiche Dichtungen, große Kompression, niedrige Schließkräfte",
            "example": "Große Lukendeckel mit wenig Verschlusskraft",
        },
        "50A_60A": {
            "use": "Standard Marine-Dichtungsprofile, Luken, Fenster",
            "example": "EPDM-Lukenprofil, Fensterdichtungen",
        },
        "70A": {
            "use": "Standard O-Ringe, Flanschdichtungen, Wellendichtringe",
            "example": "Die meisten O-Ring-Anwendungen",
        },
        "80A_90A": {
            "use": "Hochdruckanwendungen, Stützringe, Ventilsitze",
            "example": "Hydraulik-Dichtungen, hohe Druckbelastung",
        },
    },
}

# ============================================================================
# SURFACE PREPARATION FOR SEALING — Dichtflächen-Vorbereitung
# ============================================================================

SEALING_SURFACE_PREPARATION = {
    "surface_roughness": {
        "o_ring_groove": {
            "ra_max_um": 0.8,
            "method": "Feindrehen oder Schleifen",
        },
        "flange_face_metallic": {
            "ra_max_um": 1.6,
            "method": "Planfräsen, Schleifen",
        },
        "adhesive_bonded_seal": {
            "ra_range_um": "20-60",
            "method": "Schleifen P80-P120 für mechanische Verkrallung",
        },
        "grp_flange": {
            "ra_range_um": "5-20",
            "method": "Schleifen P120, Entfetten, ggf. Primer",
        },
    },
    "flatness_requirements": {
        "o_ring_face_seal": {
            "max_deviation_mm_per_100mm": 0.05,
        },
        "gasket_seal_soft": {
            "max_deviation_mm_per_100mm": 0.2,
        },
        "gasket_seal_hard": {
            "max_deviation_mm_per_100mm": 0.05,
        },
    },
    "cleaning_protocol": {
        "metallic": [
            "Entfetten mit Aceton oder MEK",
            "Keine Silikonreiniger — kontaminiert die Dichtfläche",
            "Fusselfreies Tuch (kein Küchenpapier)",
            "Innerhalb 30min weiterarbeiten nach Reinigung",
        ],
        "grp_composite": [
            "Schleifen mit P120 (frische Oberfläche)",
            "Staubsaugen und Abblasen (Druckluft öl-frei)",
            "Entfetten mit Aceton (kurze Einwirkzeit — löst sonst Harz)",
        ],
        "aluminium": [
            "Scotchbrite Schleifen für mechanische Verkrallung",
            "Reinigen mit Isopropanol",
            "Primer auftragen (z.B. Sika Primer-206 G+P) bei Klebedichtung",
        ],
    },
}

# ============================================================================
# INSPECTION AND ASSESSMENT CRITERIA
# ============================================================================

SEAL_INSPECTION_CRITERIA = {
    "visual_inspection": {
        "weight": 30,
        "checks": [
            {"item": "Rissbildung", "severity": "critical", "description": "Querrisse = sofort tauschen"},
            {"item": "Verformung", "severity": "major", "description": "Dauerhafter Querschnittsverlust >40%"},
            {"item": "Quellung", "severity": "major", "description": "Dichtung aufgequollen = falsches Material"},
            {"item": "Verhärtung", "severity": "major", "description": "Fingernagel-Test: Material muss nachgeben"},
            {"item": "Verfärbung", "severity": "minor", "description": "Leichte Verfärbung normal, starke = Mediumangriff"},
            {"item": "Extrusion", "severity": "major", "description": "Material quillt aus der Nut heraus"},
        ],
    },
    "functional_check": {
        "weight": 40,
        "checks": [
            {"item": "Dichtigkeit", "severity": "critical", "description": "Kein Wasserdurchtritt bei Betriebsdruck"},
            {"item": "Schließkraft", "severity": "major", "description": "Luke/Fenster schließt ohne Überkraft"},
            {"item": "Gleichmäßige Kompression", "severity": "major", "description": "Profil überall gleichmäßig zusammengedrückt"},
            {"item": "Rückstellung", "severity": "major", "description": "Nach Öffnen muss Profil zurückfedern"},
        ],
    },
    "installation_quality": {
        "weight": 30,
        "checks": [
            {"item": "Klebung/Montage", "severity": "major", "description": "Dichtung sitzt fest, kein Verrutschen"},
            {"item": "Stoßstelle", "severity": "major", "description": "Enden sauber verbunden (vulkanisiert oder geklebt)"},
            {"item": "Korrekte Kompression", "severity": "major", "description": "15-30% je nach Profiltyp"},
            {"item": "Oberflächenvorbereitung", "severity": "minor", "description": "Dichtfläche sauber, plan, korrekte Rauheit"},
            {"item": "Materialwahl", "severity": "critical", "description": "Richtiges Material für Medium und Temperatur"},
        ],
    },
}

# ============================================================================
# ASSESSMENT FUNCTION
# ============================================================================

def assess_seal_installation(
    seal_type: str,
    material: str,
    application_zone: str,
    medium_contact: str = "seawater",
    temperature_c: float = 25.0,
    compression_percent: float = 20.0,
    age_years: float = 0.0,
    visual_condition: str = "good",
    leakage_observed: bool = False,
) -> Dict[str, Any]:
    """
    Bewertet eine Dichtungsinstallation auf Korrektheit und Zustand.

    Args:
        seal_type: Art der Dichtung (o_ring, lip_seal, hatch_seal_profile, etc.)
        material: Dichtungsmaterial (epdm, nbr_nitrile, fkm_viton, silikon, neopren_cr, ptfe)
        application_zone: Einbauort (deck, engine_room, underwater, interior, etc.)
        medium_contact: Medium mit dem Dichtung in Kontakt ist
        temperature_c: Betriebstemperatur
        compression_percent: Tatsächliche Kompression der Dichtung
        age_years: Alter der Dichtung in Jahren
        visual_condition: Sichtzustand (good, fair, poor, critical)
        leakage_observed: Ob Undichtigkeit festgestellt wurde

    Returns:
        Dict mit score (0-100), findings, recommendations
    """
    score = 100
    findings = []
    recommendations = []

    # 1. Material-Medien-Verträglichkeit prüfen
    if material in MEDIA_COMPATIBILITY and medium_contact in MEDIA_COMPATIBILITY[material]:
        rating = MEDIA_COMPATIBILITY[material][medium_contact]
        if rating == "X":
            score -= 50
            medium_de = MEDIA_NAMES_DE.get(medium_contact, medium_contact)
            mat_info = SEAL_MATERIALS.get(material, {})
            mat_name = mat_info.get("name_de", material)
            findings.append(f"KRITISCH: {mat_name} ist unverträglich mit {medium_de}")
            recommendations.append(f"Material sofort wechseln — {mat_name} quillt/zersetzt sich bei Kontakt mit {medium_de}")

            # Empfehlung für richtiges Material
            best_materials = []
            for mat_key, compat in MEDIA_COMPATIBILITY.items():
                if compat.get(medium_contact) == "A":
                    alt_info = SEAL_MATERIALS.get(mat_key, {})
                    best_materials.append(alt_info.get("name_de", mat_key))
            if best_materials:
                recommendations.append(f"Empfohlene Alternative(n): {', '.join(best_materials[:3])}")

        elif rating == "C":
            score -= 15
            medium_de = MEDIA_NAMES_DE.get(medium_contact, medium_contact)
            findings.append(f"Bedingt geeignet: Material nur eingeschränkt verträglich mit {medium_de}")
            recommendations.append("Engere Inspektionsintervalle einplanen, ggf. auf besser geeignetes Material wechseln")

    # 2. Temperaturbereich prüfen
    mat_info = SEAL_MATERIALS.get(material, {})
    temp_range = mat_info.get("temperature_range_c", {})
    if temp_range:
        if temperature_c > temp_range.get("continuous_max", 999):
            score -= 30
            findings.append(f"Temperatur {temperature_c}°C überschreitet Dauergrenze von {temp_range['continuous_max']}°C")
            recommendations.append("Material mit höherer Temperaturbeständigkeit wählen (z.B. FKM/Viton oder Silikon)")
        elif temperature_c > temp_range.get("max", 999):
            score -= 40
            findings.append(f"Temperatur {temperature_c}°C überschreitet absolute Grenze von {temp_range['max']}°C")
            recommendations.append("SOFORT wechseln — Material versagt bei dieser Temperatur")
        elif temperature_c < temp_range.get("min", -999):
            score -= 25
            findings.append(f"Temperatur {temperature_c}°C unter Minimumgrenze von {temp_range['min']}°C — Material versprödet")

    # 3. Kompression bewerten
    profile_info = SEAL_PROFILES.get(seal_type, {})
    if isinstance(profile_info, dict):
        comp_range = profile_info.get("compression_percent", {})
        if isinstance(comp_range, dict):
            comp_min = comp_range.get("min", 10)
            comp_max = comp_range.get("max", 35)
            comp_opt = comp_range.get("optimal", (comp_min + comp_max) / 2)

            if compression_percent < comp_min:
                score -= 20
                findings.append(f"Kompression {compression_percent}% zu gering (Minimum: {comp_min}%)")
                recommendations.append("Dichtflächen-Abstand verringern oder dickeres Profil wählen")
            elif compression_percent > comp_max:
                score -= 15
                findings.append(f"Kompression {compression_percent}% zu hoch (Maximum: {comp_max}%) — erhöhter Verschleiß und Compression Set")
                recommendations.append("Nuttiefe vergrößern oder dünneres Profil verwenden")
            elif abs(compression_percent - comp_opt) <= 5:
                findings.append(f"Kompression {compression_percent}% im optimalen Bereich")

    # 4. Alter bewerten
    if age_years > 0:
        # Allgemeine Altersbewertung
        if material == "epdm":
            if application_zone in ("deck", "cockpit", "exterior"):
                max_life = 8
            else:
                max_life = 15
        elif material == "nbr_nitrile":
            max_life = 6 if application_zone in ("deck", "exterior") else 10
        elif material == "fkm_viton":
            max_life = 15
        elif material == "silikon":
            max_life = 15
        elif material == "neopren_cr":
            max_life = 10
        else:
            max_life = 10

        life_ratio = age_years / max_life
        if life_ratio > 1.0:
            score -= 25
            findings.append(f"Dichtung ist {age_years:.0f} Jahre alt — über erwarteter Lebensdauer von {max_life} Jahren")
            recommendations.append("Dichtung zeitnah erneuern, auch wenn optisch noch akzeptabel")
        elif life_ratio > 0.75:
            score -= 10
            findings.append(f"Dichtung bei {life_ratio*100:.0f}% der erwarteten Lebensdauer — Inspektion empfohlen")
            recommendations.append("Engere Kontrolle planen, Ersatzdichtung bereithalten")

    # 5. Visuelle Bewertung
    condition_penalties = {
        "good": 0,
        "fair": -10,
        "poor": -25,
        "critical": -40,
    }
    score += condition_penalties.get(visual_condition, 0)

    condition_findings = {
        "fair": "Leichte Alterungszeichen sichtbar (Verhärtung, leichte Verformung)",
        "poor": "Deutliche Alterungszeichen: Risse, starke Verformung, Verhärtung",
        "critical": "Schwere Schäden: Durchgehende Risse, Materialausfall, keine Elastizität",
    }
    if visual_condition in condition_findings:
        findings.append(condition_findings[visual_condition])

    # 6. Undichtigkeit
    if leakage_observed:
        score -= 30
        findings.append("Undichtigkeit festgestellt — Dichtfunktion beeinträchtigt")
        recommendations.append("Ursache feststellen: Materialversagen, falsche Kompression, beschädigte Dichtfläche, oder falsche Materialwahl")

    # 7. Zonenbezogene Bewertung
    zone_risks = {
        "underwater": {"risk": "hoch", "note": "Undichtigkeit = Wassereinbruch, sicherheitskritisch"},
        "engine_room": {"risk": "hoch", "note": "Hohe Temperaturen, Ölnebel, Vibrationen"},
        "deck": {"risk": "mittel", "note": "UV-Belastung, Salzwasser, mechanische Belastung"},
        "fuel_system": {"risk": "sehr hoch", "note": "Kraftstoffkontakt, Brandgefahr bei Versagen"},
        "cockpit": {"risk": "mittel", "note": "UV, Regen, mechanische Belastung durch Nutzung"},
        "interior": {"risk": "gering", "note": "Geschützt, wenig Umweltbelastung"},
    }
    zone_info = zone_risks.get(application_zone)
    if zone_info:
        findings.append(f"Einbauzone '{application_zone}': Risikostufe {zone_info['risk']} — {zone_info['note']}")
        if zone_info["risk"] in ("hoch", "sehr hoch") and score < 70:
            recommendations.append(f"Bei Risikostufe '{zone_info['risk']}' sollte Score >70 sein — Maßnahmen priorisieren")

    # Ergebnis zusammenstellen
    score = max(0, min(100, score))

    if score >= 80:
        overall = "Gut — Dichtung korrekt installiert und in gutem Zustand"
    elif score >= 60:
        overall = "Ausreichend — einige Punkte zu verbessern"
    elif score >= 40:
        overall = "Mangelhaft — Dichtung sollte zeitnah überarbeitet/getauscht werden"
    else:
        overall = "Ungenügend — sofortige Maßnahmen erforderlich"

    return {
        "score": score,
        "overall": overall,
        "seal_type": seal_type,
        "material": material,
        "application_zone": application_zone,
        "findings": findings,
        "recommendations": recommendations,
    }
