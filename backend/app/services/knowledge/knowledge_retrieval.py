"""
AYDI KNOWLEDGE RETRIEVAL SERVICE — Zentrale Wissensdatenbank-Schnittstelle

This is a CENTRAL KNOWLEDGE RETRIEVAL SERVICE for the AYDI yacht analysis platform.
It serves as the bridge between the ~50,000 lines of expert knowledge databases
and the analysis/prompt systems that need to consume them.

The service provides context-aware knowledge retrieval based on BoatDNA parameters:
- hull_material, hull_construction, core_material, deck_material
- propulsion, length_m, builder_quality_tier, production_type

All returned text for prompt injection is in German (Deutsch) with English technical
terms in parentheses where appropriate.

Author: AYDI Research Team
Version: 1.0
Date: 2026-03-22
"""

from typing import Dict, Any, List, Optional, Union
import logging

logger = logging.getLogger(__name__)

# =============================================================================
# IMPORT ALL KNOWLEDGE DATABASES
# =============================================================================

try:
    from .hull_construction_deep import (
        RESIN_DATABASE,
        FIBER_DATABASE,
        GELCOAT_DATABASE,
        CORE_MATERIALS_DATABASE,
        CONSTRUCTION_METHODS_DATABASE,
        HULL_DECK_JOINT_DATABASE,
        ENVIRONMENTAL_AND_DURABILITY,
        REPAIR_AND_MAINTENANCE_GUIDE,
    )
except ImportError:
    RESIN_DATABASE = {}
    FIBER_DATABASE = {}
    GELCOAT_DATABASE = {}
    CORE_MATERIALS_DATABASE = {}
    CONSTRUCTION_METHODS_DATABASE = {}
    HULL_DECK_JOINT_DATABASE = {}
    ENVIRONMENTAL_AND_DURABILITY = {}
    REPAIR_AND_MAINTENANCE_GUIDE = {}

try:
    from .keel_rudder_underwater_deep import (
        KEEL_DATABASE,
        RUDDER_DATABASE,
        ANTIFOULING_DATABASE,
        ANODE_DATABASE,
        INTEGRATED_WARNINGS,
    )
except ImportError:
    KEEL_DATABASE = {}
    RUDDER_DATABASE = {}
    ANTIFOULING_DATABASE = {}
    ANODE_DATABASE = {}
    INTEGRATED_WARNINGS = {}

try:
    from .engine_drivetrain_deep import (
        ENGINE_DATABASE,
        COOLING_SYSTEM_DATABASE,
        EXHAUST_DATABASE,
        FUEL_SYSTEM_DATABASE,
        DRIVETRAIN_DATABASE,
    )
except ImportError:
    ENGINE_DATABASE = {}
    COOLING_SYSTEM_DATABASE = {}
    EXHAUST_DATABASE = {}
    FUEL_SYSTEM_DATABASE = {}
    DRIVETRAIN_DATABASE = {}

try:
    from .electrical_systems_deep import (
        BATTERY_DATABASE,
        WIRING_DATABASE,
        SHORE_POWER_DATABASE,
        INVERTER_GENERATOR_DATABASE,
        CORROSION_DATABASE,
        CRITICAL_WARNINGS,
    )
except ImportError:
    BATTERY_DATABASE = {}
    WIRING_DATABASE = {}
    SHORE_POWER_DATABASE = {}
    INVERTER_GENERATOR_DATABASE = {}
    CORROSION_DATABASE = {}
    CRITICAL_WARNINGS = {}

try:
    from .sanitary_interior_safety_deep import (
        SEACOCK_DATABASE,
        TOILET_DATABASE,
        GAS_INSTALLATION_DATABASE,
        INTERIOR_DATABASE,
        MOISTURE_DATABASE,
        FIRE_SAFETY_DATABASE,
        STABILITY_DATABASE,
        STANDARDS_DATABASE,
    )
except ImportError:
    SEACOCK_DATABASE = {}
    TOILET_DATABASE = {}
    GAS_INSTALLATION_DATABASE = {}
    INTERIOR_DATABASE = {}
    MOISTURE_DATABASE = {}
    FIRE_SAFETY_DATABASE = {}
    STABILITY_DATABASE = {}
    STANDARDS_DATABASE = {}

try:
    from .rigging_sails_deck_deep import (
        STANDING_RIGGING_DATABASE,
        MAST_DATABASE,
        SAIL_DATABASE,
        TEAK_DECK_DATABASE,
        DECK_HARDWARE_MOUNTING_DATABASE,
    )
except ImportError:
    STANDING_RIGGING_DATABASE = {}
    MAST_DATABASE = {}
    SAIL_DATABASE = {}
    TEAK_DECK_DATABASE = {}
    DECK_HARDWARE_MOUNTING_DATABASE = {}

try:
    from .aging_lifecycle_manufacturers_deep import (
        MATERIAL_LIFESPAN_DATABASE,
        DEGRADATION_CYCLES_DATABASE,
        MANUFACTURER_DATABASE_SAIL,
        MANUFACTURER_DATABASE_MOTOR,
        MANUFACTURER_DATABASE_CUSTOM,
    )
except ImportError:
    MATERIAL_LIFESPAN_DATABASE = {}
    DEGRADATION_CYCLES_DATABASE = {}
    MANUFACTURER_DATABASE_SAIL = {}
    MANUFACTURER_DATABASE_MOTOR = {}
    MANUFACTURER_DATABASE_CUSTOM = {}

try:
    from .coatings_sealants_deep import (
        SEALANT_DATABASE,
        EPOXY_SYSTEMS,
        COMPATIBILITY_MATRIX,
    )
except ImportError:
    SEALANT_DATABASE = {}
    EPOXY_SYSTEMS = {}
    COMPATIBILITY_MATRIX = {}

try:
    from .deck_hardware_deep import (
        WINCH_DATABASE,
        BLOCK_DATABASE,
        HATCH_DATABASE,
        MAINTENANCE_MATRIX,
    )
except ImportError:
    WINCH_DATABASE = {}
    BLOCK_DATABASE = {}
    HATCH_DATABASE = {}
    MAINTENANCE_MATRIX = {}

try:
    from .expert_community_knowledge import (
        PURCHASE_EXPERTISE,
        OSMOSIS_EXPERTISE,
        RIGGING_EXPERTISE,
        ENGINE_EXPERTISE,
        ELECTRICAL_EXPERTISE,
        INTERIOR_EXPERTISE,
        SEACOCK_EXPERTISE,
        MANUFACTURER_REPUTATION,
    )
except ImportError:
    PURCHASE_EXPERTISE = {}
    OSMOSIS_EXPERTISE = {}
    RIGGING_EXPERTISE = {}
    ENGINE_EXPERTISE = {}
    ELECTRICAL_EXPERTISE = {}
    INTERIOR_EXPERTISE = {}
    SEACOCK_EXPERTISE = {}
    MANUFACTURER_REPUTATION = {}

try:
    from .forensic_failure_analysis import (
        CUMULATIVE_DEGRADATION_CYCLES,
        HIDDEN_MOISTURE_PATHS,
        OSMOSIS_KNOWLEDGE,
        GALVANIC_SERIES_MARINE,
        MATERIAL_INTERACTION_FAILURES,
    )
except ImportError:
    CUMULATIVE_DEGRADATION_CYCLES = {}
    HIDDEN_MOISTURE_PATHS = {}
    OSMOSIS_KNOWLEDGE = {}
    GALVANIC_SERIES_MARINE = {}
    MATERIAL_INTERACTION_FAILURES = {}

try:
    from .practical_experience import (
        MANUFACTURER_PATTERNS,
        REAL_FAILURE_CASES,
    )
except ImportError:
    MANUFACTURER_PATTERNS = {}
    REAL_FAILURE_CASES = {}


# =============================================================================
# MATERIAL MAPPING & NORMALIZATION
# =============================================================================

HULL_MATERIAL_MAPPING = {
    "grp": "grp",
    "gfk": "grp",
    "fiberglass": "grp",
    "polyester": "grp",
    "aluminium": "aluminium",
    "aluminum": "aluminium",
    "alu": "aluminium",
    "carbon": "carbon",
    "wood": "wood",
    "steel": "steel",
    "ferro_cement": "ferro_cement",
    "ferrocement": "ferro_cement",
}

HULL_CONSTRUCTION_MAPPING = {
    "hand_layup": "hand_layup",
    "hand_lay": "hand_layup",
    "resin_infusion": "resin_infusion",
    "infusion": "resin_infusion",
    "rti": "resin_infusion",
    "prepreg_autoclave": "prepreg_autoclave",
    "prepreg": "prepreg_autoclave",
    "autoclave": "prepreg_autoclave",
    "welded": "welded",
    "cold_molded": "cold_molded",
    "cold_moulded": "cold_molded",
}

CORE_MATERIAL_MAPPING = {
    "balsa": "balsa",
    "pvc_foam": "pvc_foam",
    "pvc": "pvc_foam",
    "san_foam": "san_foam",
    "san": "san_foam",
    "honeycomb": "honeycomb",
    "none": "none",
    "solid": "none",
    "no_core": "none",
}

DECK_MATERIAL_MAPPING = {
    "grp": "grp",
    "gfk": "grp",
    "fiberglass": "grp",
    "teak": "teak",
    "wood": "wood",
    "non_slip_paint": "non_slip_paint",
    "paint": "non_slip_paint",
    "aluminum": "aluminum",
    "aluminium": "aluminum",
}


# =============================================================================
# CORE RETRIEVAL FUNCTIONS
# =============================================================================


def normalize_hull_material(hull_material: Optional[str]) -> str:
    """Normalize hull material name to canonical form."""
    if not hull_material:
        return "grp"
    normalized = hull_material.lower().strip().replace(" ", "_")
    return HULL_MATERIAL_MAPPING.get(normalized, normalized)


def normalize_hull_construction(hull_construction: Optional[str]) -> str:
    """Normalize hull construction name to canonical form."""
    if not hull_construction:
        return "hand_layup"
    normalized = hull_construction.lower().strip().replace(" ", "_")
    return HULL_CONSTRUCTION_MAPPING.get(normalized, normalized)


def normalize_core_material(core_material: Optional[str]) -> str:
    """Normalize core material name to canonical form."""
    if not core_material:
        return "none"
    normalized = core_material.lower().strip().replace(" ", "_")
    return CORE_MATERIAL_MAPPING.get(normalized, normalized)


def normalize_deck_material(deck_material: Optional[str]) -> str:
    """Normalize deck material name to canonical form."""
    if not deck_material:
        return "grp"
    normalized = deck_material.lower().strip().replace(" ", "_")
    return DECK_MATERIAL_MAPPING.get(normalized, normalized)


def get_knowledge_for_visual_analysis(
    image_type: str,
    hull_material: Optional[str] = None,
    hull_construction: Optional[str] = None,
    core_material: Optional[str] = None,
    deck_material: Optional[str] = None,
    propulsion: str = "sail",
    builder_quality_tier: str = "standard",
    **kwargs,
) -> Dict[str, Any]:
    """
    Returns a dict with sections of knowledge text (German) relevant to the visual analysis type.
    Used by prompt generators to inject expert knowledge into Claude Vision prompts.

    Args:
        image_type: "interior_detail", "exterior_overview", "material_sample", "hull_section",
                   "deck_detail", "rigging", "engine_room", "electrical_panel", etc.
        hull_material: "grp", "aluminium", "carbon", "wood", "steel", "ferro_cement"
        hull_construction: "hand_layup", "resin_infusion", "prepreg_autoclave", "welded", "cold_molded"
        core_material: "balsa", "pvc_foam", "san_foam", "honeycomb", "none"
        deck_material: "grp", "teak", "wood", "non_slip_paint", "aluminum"
        propulsion: "sail", "motor", "hybrid"
        builder_quality_tier: "budget", "standard", "premium", "custom", "luxury"

    Returns:
        Dict with keys: construction_knowledge, material_knowledge, degradation_knowledge,
                       inspection_points (list), critical_warnings (list), image_type_guidance
    """
    hull_mat = normalize_hull_material(hull_material)
    hull_const = normalize_hull_construction(hull_construction)
    core_mat = normalize_core_material(core_material)
    deck_mat = normalize_deck_material(deck_material)

    knowledge = {
        "construction_knowledge": "",
        "material_knowledge": "",
        "degradation_knowledge": "",
        "inspection_points": [],
        "critical_warnings": [],
        "image_type_guidance": "",
    }

    # =========================================================================
    # IMAGE-TYPE-SPECIFIC GUIDANCE
    # =========================================================================

    if image_type == "interior_detail":
        knowledge["image_type_guidance"] = (
            "Suchen Sie nach Wasserschäden, Feuchtigkeitsflecken, Schimmelherde, "
            "lockere Befestigungen, Korrosionsspuren an Stahlbeschlägen, "
            "Verformungen an GFK-Spanten, Risse in Kabinenaufbauten. "
            "Testen Sie die Festigkeit des Deckkerns mit Druck."
        )
        knowledge["inspection_points"] = [
            "Feuchtigkeitsspuren an Wänden und Decke",
            "Schimmelherde in dunklen Ecken und unter Polstern",
            "Korrosion an Edelstahl-Befestigungen",
            "Lockere oder rostige Schrauben/Bolzen",
            "Weiche Stellen im Deckenkern (Balsa-Durchfeuchtung)",
            "Verfärbungen und Verfärbungsmuster (Salzkristalle, Rostflecken)",
            "Risse in GFK-Aufbauten und Spanten",
        ]

    elif image_type == "exterior_overview":
        knowledge["image_type_guidance"] = (
            "Beobachten Sie Gelcoat-Glanzgrad und Verfärbungen. "
            "Suchen Sie nach Kratzer, Dellen, Rissen. Überprüfen Sie die Übergänge "
            "zwischen Rumpf und Aufbauten auf Spaltkorrosion. "
            "Notieren Sie UV-Degradation (Rauheit, Verfärbung)."
        )
        knowledge["inspection_points"] = [
            "Gelcoat-Oberflächenrauheit und Glanzgrad",
            "UV-Degradation und Verfärbung",
            "Kratzer, Dellen, strukturelle Beschädigungen",
            "Risse oder Blasenbildung im Gelcoat",
            "Wasserlinie-Verschmutzung (Algenbelag, Kalkablagerungen)",
            "Übergänge Rumpf-Aufbau: Spaltkorrisions-Anfälligkeit",
            "Antifouling-Zustand und Verschleiß",
        ]

    elif image_type == "material_sample":
        knowledge["image_type_guidance"] = (
            "Untersuchen Sie die Fasern und Harz-Struktur unter Lupe. "
            "Suchen Sie nach Blasen, Poren, Harz-Überfluss oder -Mangel. "
            "Prüfen Sie auf Delamination zwischen Lagen. Achten Sie auf Verfärbungen "
            "in der Harz-Matrix (Hinweis auf Wasserschaden oder Osmose)."
        )
        knowledge["inspection_points"] = [
            "Poren und Hohlräume in der Harz-Matrix",
            "Faserausrichtung und Wicklung",
            "Harz/Faser-Verhältnis (sollte 40/60 sein, nicht 50/50)",
            "Delamination oder Schichttrennungen",
            "Verfärbung oder Verfärbungsmuster in Harz",
            "Wasserschäden oder Osmose-Anzeichen",
            "Kratzer und Verschleißspuren auf der Oberfläche",
        ]

    elif image_type == "hull_section":
        knowledge["image_type_guidance"] = (
            "Prüfen Sie die Schichtdicke und Gleichmäßigkeit. "
            "Suchen Sie nach Rissen in Längsspannungsrichtung. "
            "Überprüfen Sie Kern-Integrität (bei Sandwich-Konstruktion). "
            "Achten Sie auf Feuchtigkeitseintritte oder Osmose-Blasen."
        )
        knowledge["inspection_points"] = [
            "Schichtdicken-Uniformität",
            "Risse in Rumpf-Längslinie",
            "Kern-Feuchte und -Integrität (bei Sandwich)",
            "Osmose-Blasen unter der Wasserlinie",
            "Delamination oder Kern-Ausfallstellen",
            "Belastungskonzentrationen (Riss-Initiierung)",
        ]

    elif image_type == "deck_detail":
        knowledge["image_type_guidance"] = (
            "Untersuchen Sie Deck-Oberflächenzustand. "
            "Testen Sie Befestigungen (Wanten, Beschläge): Drehmoment-Test. "
            "Achten Sie auf Spaltkorrosion unter Stahlbeschlägen. "
            "Prüfen Sie Dicht-Integrität an Luken und Durchführungen."
        )
        knowledge["inspection_points"] = [
            "Deck-Material (GFK, Teak, Aluminium) Oberflächenzustand",
            "Befestigungs-Festigkeit (Beschläge, Wanten-Pins)",
            "Spaltkorrosion um Stahlbeschläge",
            "Dichtheitszustand an Luken, Verschlüssen",
            "Verformung oder Durchsenkung des Decks",
            "Teak-Spalt-Breite (sollte 3-5 mm sein)",
        ]

    elif image_type == "rigging":
        knowledge["image_type_guidance"] = (
            "Prüfen Sie Wanten-, Vorstag-Zustand. "
            "Überprüfen Sie auf Korrosion und Verformung. "
            "Achten Sie auf Abnutzung in Turnbuckeln. "
            "Suchen Sie nach Rissen oder Verformungen im Mast."
        )
        knowledge["inspection_points"] = [
            "Draht-Rigg-Zustand und Korrosion",
            "Kauschen und Ösen auf Verschleiß",
            "Turnbuckel-Drehmoment und Korrosion",
            "Mast-Kratzer, Dellen, Risse",
            "Segel-Verschleiß und UV-Degradation",
            "Befestigungs-Festigkeit am Mastfuß und Masttopp",
        ]

    elif image_type == "engine_room":
        knowledge["image_type_guidance"] = (
            "Prüfen Sie Motor-Allgemeinzustand und Sauberkeit. "
            "Achten Sie auf Öllecks und Kühlmittel-Lecks. "
            "Überprüfen Sie Befestigungs-Bolzen und Vibrations-Isolator. "
            "Suchen Sie nach Korrosion an Kupfer-, Messing- und Edelstahl-Teilen."
        )
        knowledge["inspection_points"] = [
            "Motor-Oberflächenzustand und Verschmutzung",
            "Öl- und Kühlmittel-Lecks",
            "Befestigungs-Bolzen und Motor-Vibrations-Isolation",
            "Abgassystem-Integrität (Korrosion, Undichtheiten)",
            "Kraftstoff-Druckleitungen und Filter",
            "Kühlwasser-Lecks und Schlauch-Verschleiß",
        ]

    elif image_type == "electrical_panel":
        knowledge["image_type_guidance"] = (
            "Untersuchen Sie Kabelisolation und Anschluss-Sauberkeit. "
            "Suchen Sie nach Korrosion an Klemmen und Kontakten. "
            "Überprüfen Sie Schutzschalter und Sicherungen. "
            "Achten Sie auf Kontakt-Überhitzung (schwarze Verfärbungen)."
        )
        knowledge["inspection_points"] = [
            "Kabel-Isolations-Zustand (Risse, Bruchstellen)",
            "Kontakt- und Klemmen-Korrosion",
            "Schutzschalter-Beschaffenheit und Auslöse-Funktion",
            "Sicherungs-Größen und Kabel-Querschnitte (Kompatibilität)",
            "Feuchtigkeitsspuren in Schalter-Gehäusen",
            "Überlastungs-Anzeichen (Verfärbung, Geruch)",
        ]

    # =========================================================================
    # MATERIAL-SPEZIFISCHES WISSEN HINZUFÜGEN
    # =========================================================================

    if hull_mat == "grp":
        knowledge["material_knowledge"] += (
            "GFK-RUMPF (Glasfaserkunststoff): Meistens Polyester-Harz mit E-Glas-Fasern. "
            "Typisches Harz/Faser-Verhältnis 60:40. "
        )

        # Resin-specific knowledge
        if "orthophthalic" in str(RESIN_DATABASE.get("orthophthalic_polyester", {})).lower():
            knowledge["material_knowledge"] += (
                "Orthophthal-Polyester: Günstig, anfällig für Osmose nach 10-15 Jahren. "
                "Wahrscheinlich in Booten vor 1990. "
            )
        if "isophthalic" in str(RESIN_DATABASE.get("isophthalic_polyester", {})).lower():
            knowledge["material_knowledge"] += (
                "Isophthal-Polyester: Standard seit 1995, bessere Osmose-Resistenz (15-20 Jahre). "
            )
        if "vinylester" in str(RESIN_DATABASE.get("vinylester", {})).lower():
            knowledge["material_knowledge"] += (
                "Vinylester: Premiumwahl für Osmose-Resistenz (40+ Jahre). 300x wasserfester als Polyester. "
            )

        # Core material knowledge
        if core_mat != "none":
            knowledge["material_knowledge"] += f"\nKERNMATERIAL: {core_mat.upper()}. "
            if core_mat == "balsa":
                knowledge["material_knowledge"] += (
                    "Balsa-Kern: Leicht, gute Isolierung, aber extremempfindlich gegen Feuchte. "
                    "Durchfeuchtung führt zu Kern-Kollaps und Delaminierung. "
                    "Drucktests regelmäßig durchführen. Lebenserwartung trocken 30+ Jahre, nass <1 Jahr."
                )
                knowledge["critical_warnings"].append(
                    "KRITISCH: Balsa-Kern-Feuchte über 15% bedeutet drohenden Kern-Kollaps."
                )
            elif core_mat == "pvc_foam":
                knowledge["material_knowledge"] += (
                    "PVC-Schaum-Kern: Feuchtebeständiger als Balsa, aber weniger isolierend. "
                    "Lebensdauer 20-30 Jahre bei gutem Dichtungszustand. "
                    "Empfindlich gegen bestimmte Harze und Lösemittel."
                )
            elif core_mat == "san_foam":
                knowledge["material_knowledge"] += (
                    "SAN-Schaum: Gute chemische Resistenz, anständige Isolierung. "
                    "Lebensdauer ähnlich PVC. Weniger häufig als Balsa oder PVC."
                )

        knowledge["degradation_knowledge"] += (
            "GFK-DEGRADATION: Osmose durch Wasserdiffusion in Harz (insbes. Polyester). "
            "Gelcoat-Alterung durch UV (~2-3% pro Jahr in Tropen). "
            "Matrizzen-Hydrolyse führt zu Umlagerung. "
            "Prognose: 50-80 Jahre bis schwerwiegende Probleme, abhängig von Harztyp und Klima."
        )

    elif hull_mat == "aluminium":
        knowledge["material_knowledge"] += (
            "ALUMINIUM-RUMPF: Seewasser-Korrosion ist Hauptproblem. "
            "Typischerweise 5083-H116 oder 5086-H32 (Magnesium-Aluminium-Legierung). "
            "Erfordert Zink-Anoden und Isolations-Schichten gegen Galvanische Korrosion. "
            "Gute mechanische Eigenschaften, aber komplexe Erhaltung."
        )
        knowledge["degradation_knowledge"] += (
            "ALUMINIUM-DEGRADATION: Elektrochemische Korrosion (Galvanische Reihe). "
            "Lokalisierte Pitting-Korrosion unter Schichten und Verschmutzung. "
            "Typische Abtragungsrate 0,02-0,1 mm/Jahr ohne Schutz. "
            "Mit Anoden und Isolierung: 0,002-0,01 mm/Jahr. "
            "Lebensdauer typischerweise 40-50 Jahre mit guter Wartung."
        )

    elif hull_mat == "steel":
        knowledge["material_knowledge"] += (
            "STAHL-RUMPF: Höchste Festigkeit und Verschleiß-Resistenz. "
            "Typischerweise Baustahl (S235, S355) oder Korrosionsschutz-Stahl (COR-TEN-ähnlich). "
            "Obligatorische Innen- und Außen-Beschichtung gegen Rost. "
        )
        knowledge["degradation_knowledge"] += (
            "STAHL-DEGRADATION: Oberflächenrost durch Feuchte und Salzwasser. "
            "Durchrostung droht nach 15-25 Jahren ohne Wartung. "
            "Mit gutem Beschichtungs-System und regelmäßiger Reparatur: 50+ Jahre. "
            "Kritische Schwachstellen: Schweißnähte, Rohre, Spitzen."
        )

    elif hull_mat == "wood":
        knowledge["material_knowledge"] += (
            "HOLZ-RUMPF: Traditionelle Bauweise, heute selten. "
            "Typisch Mahagoni oder Eiche für Struktur, Teak/Zeder für Außenschale. "
            "Erfordert intensive Pflege: regelmäßiges Ölen, Anstriches, Trocknung. "
        )
        knowledge["degradation_knowledge"] += (
            "HOLZ-DEGRADATION: Holzwürmer, Pilze, Verrottung durch Feuchte. "
            "Lebensdauer bei guter Pflege 50-100 Jahre. "
            "Ohne Wartung: 10-15 Jahre bis Strukturverlust. "
            "Kritisch: Risse, Faseraufquellen, sichtbare Fraßspuren."
        )

    # =========================================================================
    # KONSTRUKTIONS-METHODEN-WISSEN
    # =========================================================================

    if hull_const == "hand_layup":
        knowledge["construction_knowledge"] += (
            "HANDLAMINIEREN: Arbeiter legen Fasern und Harz per Hand. "
            "Variabel in Qualität, sehr abhängig von Handwerkskunst. "
            "Porengehalt 3-8%, oft ungleichmäßig. "
            "Typisch in Booten vor 2000, noch heute bei Custom-Bauten. "
        )
    elif hull_const == "resin_infusion":
        knowledge["construction_knowledge"] += (
            "RTI / RESIN INFUSION: Fasern trocken in Form, Harz wird vakuum-infundiert. "
            "Geringere Poren (0,5-2%), gleichmäßiger und leichter. "
            "Bessere Harz-Faser-Verteilung. Standard seit 2000er Jahren. "
        )
    elif hull_const == "prepreg_autoclave":
        knowledge["construction_knowledge"] += (
            "PREPREG / AUTOCLAVE: Vorgefüllte Fasern, Aushärtung im Autoklav unter Druck/Temperatur. "
            "Maximale Qualität, sehr geringe Porenrate (<0,5%). "
            "Nur bei Premium-Yachten, hohe Kosten. "
        )
    elif hull_const == "welded":
        knowledge["construction_knowledge"] += (
            "VERSCHWEISST: Typisch Stahl oder Aluminium. "
            "Schweißnähte sind Schwachstellen: Korrosion, Spannungskonzentration. "
            "Regelmäßige Inspektionen und Nachbearbeitung erforderlich. "
        )
    elif hull_const == "cold_molded":
        knowledge["construction_knowledge"] += (
            "KALT-GEFORMT: Dünne Holzschichten, diagonal geklebt und mit Epoxydharz getränkt. "
            "Traditionelle Hochleistungs-Konstruktion, heute selten. "
            "Hohe Festigkeit-zu-Gewicht, aber komplexe Reparatur. "
        )

    # =========================================================================
    # ALTERUNGS- UND HERSTELLER-WISSEN
    # =========================================================================

    if builder_quality_tier == "budget":
        knowledge["critical_warnings"].append(
            "BUDGET-WERFT: Höhere Wahrscheinlichkeit für Sparprozesse bei Material und Verarbeitung. "
            "Osmose-Risiko erhöht, schwächer Laminierung, schlechtere Detailqualität."
        )
    elif builder_quality_tier == "premium":
        knowledge["construction_knowledge"] += "Premium-Werft: Erwarten Sie hochwertiges Harz, sorgfältige Verarbeitung. "
    elif builder_quality_tier == "custom":
        knowledge["construction_knowledge"] += (
            "Custom-Bau: Hochvariabel, abhängig vom einzelnen Erbauer. "
            "Gründliche Inspektionen auf Bauvarianten und Qualitätsschwankungen erforderlich."
        )

    return knowledge


def get_knowledge_for_materials_analysis(
    hull_material: Optional[str],
    hull_construction: Optional[str],
    core_material: Optional[str] = None,
    deck_material: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Returns material-specific knowledge for the deterministic materials analysis module.

    Returns dict with keys:
    - resin_data: specific resin properties
    - fiber_data: fiber type and properties
    - core_data: core material properties if sandwich
    - degradation_cycles: list of degradation mechanisms
    - material_lifespans: dict of component lifespans
    - known_issues: list of known material-specific issues
    - compatibility_warnings: list of material incompatibility warnings
    """
    hull_mat = normalize_hull_material(hull_material)
    hull_const = normalize_hull_construction(hull_construction)
    core_mat = normalize_core_material(core_material)

    knowledge = {
        "resin_data": {},
        "fiber_data": {},
        "core_data": {},
        "degradation_cycles": [],
        "material_lifespans": {},
        "known_issues": [],
        "compatibility_warnings": [],
    }

    # Populate resin data for GFK
    if hull_mat == "grp":
        if RESIN_DATABASE:
            # Extract key resin types
            for resin_name, resin_info in RESIN_DATABASE.items():
                if isinstance(resin_info, dict) and "mechanical_properties" in resin_info:
                    knowledge["resin_data"][resin_name] = {
                        "type": resin_name,
                        "properties": resin_info.get("mechanical_properties", {}),
                        "osmosis_risk": resin_info.get("osmosis_mechanism", {}),
                    }

        # Standard fiber info for marine GFK
        knowledge["fiber_data"] = {
            "type": "E-Glass",
            "typical_volume_fraction": "40%",
            "tensile_strength_MPa": "3400",
            "modulus_GPa": "72.5",
            "description_de": "Standard in Bootsbau. Ausreichende Festigkeit, gutes Kosten-Nutzen-Verhältnis.",
        }

        # Core material data
        if core_mat != "none" and CORE_MATERIALS_DATABASE:
            for core_name, core_info in CORE_MATERIALS_DATABASE.items():
                if isinstance(core_info, dict):
                    knowledge["core_data"][core_name] = core_info

        # Degradation cycles from forensic analysis
        if CUMULATIVE_DEGRADATION_CYCLES:
            knowledge["degradation_cycles"] = list(
                CUMULATIVE_DEGRADATION_CYCLES.items()
            )[:10]

    # Populate lifespans
    if MATERIAL_LIFESPAN_DATABASE:
        knowledge["material_lifespans"] = {
            k: v.get("typical_lifespan_years", "Unknown")
            for k, v in MATERIAL_LIFESPAN_DATABASE.items()
            if isinstance(v, dict)
        }

    # Known issues
    knowledge["known_issues"] = [
        "Osmose in Polyester-Rumpfen (vor 1990)",
        "Balsa-Kern-Durchfeuchtung bei älteren Sandwich-Konstruktionen",
        "UV-Gelcoat-Degradation in südlichen Klimaten",
        "Delamination unter Belastungsspitzen",
        "Risse an Konstruktions-Übergängen",
    ]

    # Compatibility warnings
    if COMPATIBILITY_MATRIX:
        knowledge["compatibility_warnings"] = [
            "Epoxy-Grundierungen nicht direkt auf Polyester-Laminat (Haftverlust)",
            "Acetonflussmittel-Reste beschädigen Gelcoat",
            "Bestimmte Formentrenner reagieren mit Vinylester",
        ]

    return knowledge


def get_knowledge_for_structural_analysis(
    hull_material: Optional[str],
    hull_construction: Optional[str],
    core_material: Optional[str] = None,
    keel_type: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Returns structural knowledge for the structural analysis module.

    Returns dict with keys:
    - construction_method: construction process details
    - hull_deck_joint: joint design and failure modes
    - keel_data: keel design and stress distribution
    - rudder_data: rudder system details
    - structural_standards: applicable ISO standards
    """
    hull_mat = normalize_hull_material(hull_material)
    hull_const = normalize_hull_construction(hull_construction)
    core_mat = normalize_core_material(core_material)

    knowledge = {
        "construction_method": {},
        "hull_deck_joint": {},
        "keel_data": {},
        "rudder_data": {},
        "structural_standards": [],
    }

    # Construction method details
    if CONSTRUCTION_METHODS_DATABASE:
        for const_name, const_info in CONSTRUCTION_METHODS_DATABASE.items():
            if const_name in hull_const:
                knowledge["construction_method"] = const_info

    # Hull-deck joint knowledge
    if HULL_DECK_JOINT_DATABASE:
        knowledge["hull_deck_joint"] = HULL_DECK_JOINT_DATABASE

    # Keel database
    if KEEL_DATABASE:
        knowledge["keel_data"] = {
            "types": KEEL_DATABASE.get("keel_types", {}),
            "materials": KEEL_DATABASE.get("material_specifications", {}),
        }

    # Rudder data
    if RUDDER_DATABASE:
        knowledge["rudder_data"] = RUDDER_DATABASE

    # Standards
    knowledge["structural_standards"] = [
        "ISO 12215 — Kleine Wasserfahrzeuge — Rumpf-Konstruktion und Stabilität",
        "ISO 8666 — Boote unter 24m — Definierte Länge und Abmessungen",
        "ISO 8847 — Bewertung der Schiffsstabilität",
    ]

    return knowledge


def get_knowledge_for_compliance(
    propulsion: Optional[str] = "sail",
    length_m: Optional[float] = 12.0,
    operating_waters: Optional[str] = "coastal",
) -> Dict[str, Any]:
    """
    Returns compliance-relevant knowledge: ISO standards, CE categories, safety requirements.

    Args:
        propulsion: "sail", "motor", "hybrid"
        length_m: overall length in meters
        operating_waters: "coastal", "offshore", "inland", "lakes"

    Returns dict with keys:
    - applicable_standards: list of relevant ISO/CE standards
    - fire_safety: fire safety requirements and materials
    - stability_requirements: stability criteria per category
    - gas_requirements: LPG/CNG safety (if applicable)
    - electrical_standards: electrical system standards
    """
    knowledge = {
        "applicable_standards": [],
        "fire_safety": {},
        "stability_requirements": {},
        "gas_requirements": {},
        "electrical_standards": [],
    }

    # Normalize None values to defaults
    length_m = length_m or 12.0
    propulsion = propulsion or "sail"
    operating_waters = operating_waters or "coastal"

    # Determine CE category based on length and operating waters
    ce_category = "C"  # default
    if length_m > 24:
        ce_category = "B"
    if operating_waters == "offshore":
        ce_category = "A"
    if length_m < 7:
        ce_category = "D"

    knowledge["applicable_standards"] = [
        f"CE Kategorie {ce_category}",
        "ISO 12215 — Rumpf-Konstruktion",
        "ISO 8847 — Stabilität",
        "ISO 10240 — Motorboote bis 15 m",
    ]

    if STANDARDS_DATABASE:
        knowledge["applicable_standards"].extend(
            STANDARDS_DATABASE.get("iso_standards", [])
        )

    # Fire safety
    if FIRE_SAFETY_DATABASE:
        knowledge["fire_safety"] = FIRE_SAFETY_DATABASE

    # Stability requirements
    if STABILITY_DATABASE:
        knowledge["stability_requirements"] = STABILITY_DATABASE

    # Gas installation safety
    if GAS_INSTALLATION_DATABASE:
        knowledge["gas_requirements"] = GAS_INSTALLATION_DATABASE

    # Electrical standards
    knowledge["electrical_standards"] = [
        "ISO 13849-1 — Sicherheit von Schiffe unter 24 m",
        "IEC 60092-504 — Schiffs-Elektrik",
        "12V DC oder 230V AC mit Isolationsüberwachung",
    ]

    knowledge["notes"] = f"Compliance-Daten für CE-Kategorie {ce_category}, {propulsion}-Antrieb, {operating_waters}-Gewässer"

    return knowledge


def get_knowledge_for_service_patterns(
    hull_material: Optional[str],
    hull_construction: Optional[str],
    production_type: str = "series",
    builder_name: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Returns degradation cycles, material lifespans, manufacturer-specific patterns.

    Args:
        hull_material: material type
        hull_construction: construction method
        production_type: "series", "semi_custom", "custom"
        builder_name: name of the builder/shipyard

    Returns dict with keys:
    - degradation_cycles: list of degradation mechanisms in sequence
    - material_lifespans: dict of component lifespans
    - manufacturer_profile: profile of the builder
    - common_failure_modes: list of common failure modes
    - maintenance_intervals: recommended maintenance schedule
    """
    hull_mat = normalize_hull_material(hull_material)

    knowledge = {
        "degradation_cycles": [],
        "material_lifespans": {},
        "manufacturer_profile": {},
        "common_failure_modes": [],
        "maintenance_intervals": {},
    }

    # Degradation cycles from forensic analysis
    if DEGRADATION_CYCLES_DATABASE:
        knowledge["degradation_cycles"] = DEGRADATION_CYCLES_DATABASE.get(
            "cycles", []
        )

    # Material lifespans
    if MATERIAL_LIFESPAN_DATABASE:
        knowledge["material_lifespans"] = {
            k: v.get("typical_lifespan_years")
            for k, v in MATERIAL_LIFESPAN_DATABASE.items()
            if isinstance(v, dict)
        }

    # Manufacturer profile
    if builder_name:
        knowledge["manufacturer_profile"] = get_manufacturer_knowledge(builder_name)

    # Common failure modes
    if REAL_FAILURE_CASES:
        if isinstance(REAL_FAILURE_CASES, dict):
            knowledge["common_failure_modes"] = list(
                REAL_FAILURE_CASES.values()
            )[:15]
        elif isinstance(REAL_FAILURE_CASES, list):
            knowledge["common_failure_modes"] = REAL_FAILURE_CASES[:15]
        else:
            knowledge["common_failure_modes"] = []

    # Maintenance intervals
    knowledge["maintenance_intervals"] = {
        "monthly": "Kontrolle Rigging, Bilgen-Flüssigkeitsstände, Sichtprüfung",
        "annual": "Haul-Out, Antifouling, Anoden-Check, Rumpf-Inspektion",
        "five_yearly": "Schweißnähte prüfen, Kern-Feuchtemessung, größere Reparaturen",
        "ten_yearly": "Große Überholungen, möglicherweise Kern-Erneuerung",
    }

    return knowledge


def get_manufacturer_knowledge(builder_name: Optional[str]) -> Dict[str, Any]:
    """
    Looks up manufacturer in sail/motor/custom databases.
    Returns full manufacturer profile or empty dict.

    Args:
        builder_name: name of the builder/shipyard

    Returns dict with manufacturer profile information
    """
    if not builder_name:
        return {}

    builder_lower = builder_name.lower()
    profile = {}

    # Search in sailboat manufacturer database
    if MANUFACTURER_DATABASE_SAIL:
        for mfg_name, mfg_data in MANUFACTURER_DATABASE_SAIL.items():
            if builder_lower in mfg_name.lower():
                profile.update(mfg_data)
                break

    # Search in motor database
    if not profile and MANUFACTURER_DATABASE_MOTOR:
        for mfg_name, mfg_data in MANUFACTURER_DATABASE_MOTOR.items():
            if builder_lower in mfg_name.lower():
                profile.update(mfg_data)
                break

    # Search in custom database
    if not profile and MANUFACTURER_DATABASE_CUSTOM:
        for mfg_name, mfg_data in MANUFACTURER_DATABASE_CUSTOM.items():
            if builder_lower in mfg_name.lower():
                profile.update(mfg_data)
                break

    # Search in manufacturer reputation database
    if not profile and MANUFACTURER_REPUTATION:
        for mfg_name, rep_data in MANUFACTURER_REPUTATION.items():
            if builder_lower in mfg_name.lower():
                profile["reputation"] = rep_data
                break

    return profile


def format_knowledge_for_prompt(
    knowledge: Union[Dict[str, Any], str], max_lines: int = 50
) -> str:
    """
    Formats knowledge dict into German-language text suitable for inclusion in Claude Vision prompts.
    Prioritizes critical warnings, then inspection points, then general knowledge.
    Truncates to max_lines to fit prompt context.

    Args:
        knowledge: dict or string of knowledge
        max_lines: maximum number of lines in output

    Returns:
        Formatted German text ready for prompt injection
    """
    if isinstance(knowledge, str):
        lines = knowledge.split("\n")[:max_lines]
        return "\n".join(lines)

    if not isinstance(knowledge, dict):
        return ""

    output_lines = []

    # Critical warnings first (highest priority)
    if "critical_warnings" in knowledge and knowledge["critical_warnings"]:
        output_lines.append("⚠️ KRITISCHE WARNUNGEN:")
        for warning in knowledge["critical_warnings"][:5]:
            output_lines.append(f"  • {warning}")
        output_lines.append("")

    # Inspection points
    if "inspection_points" in knowledge and knowledge["inspection_points"]:
        output_lines.append("🔍 INSPEKTIONSPUNKTE:")
        for point in knowledge["inspection_points"][:8]:
            output_lines.append(f"  • {point}")
        output_lines.append("")

    # Image type guidance
    if "image_type_guidance" in knowledge and knowledge["image_type_guidance"]:
        output_lines.append("📸 BILD-ANALYSE-LEITFADEN:")
        output_lines.append(f"  {knowledge['image_type_guidance']}")
        output_lines.append("")

    # Construction knowledge
    if "construction_knowledge" in knowledge and knowledge["construction_knowledge"]:
        output_lines.append("🏗️ KONSTRUKTIONSWISSEN:")
        output_lines.append(f"  {knowledge['construction_knowledge']}")
        output_lines.append("")

    # Material knowledge
    if "material_knowledge" in knowledge and knowledge["material_knowledge"]:
        output_lines.append("⚙️ MATERIALWISSEN:")
        output_lines.append(f"  {knowledge['material_knowledge']}")
        output_lines.append("")

    # Degradation knowledge
    if "degradation_knowledge" in knowledge and knowledge["degradation_knowledge"]:
        output_lines.append("⏳ ALTERUNGS- UND DEGRADATIONSMUSTER:")
        output_lines.append(f"  {knowledge['degradation_knowledge']}")
        output_lines.append("")

    # Flatten to string and truncate
    formatted_text = "\n".join(output_lines)
    lines = formatted_text.split("\n")
    truncated = "\n".join(lines[:max_lines])

    return truncated


def get_combined_knowledge(
    image_type: str,
    hull_material: Optional[str] = None,
    hull_construction: Optional[str] = None,
    core_material: Optional[str] = None,
    deck_material: Optional[str] = None,
    propulsion: str = "sail",
    builder_quality_tier: str = "standard",
    length_m: float = 12.0,
    builder_name: Optional[str] = None,
    operating_waters: str = "coastal",
    production_type: str = "series",
    max_lines: int = 50,
) -> str:
    """
    Convenience function to retrieve and format all relevant knowledge
    for a given image analysis task in a single call.

    Returns German-formatted text ready for Claude Vision prompt injection.
    """
    # Get all knowledge sources
    visual_knowledge = get_knowledge_for_visual_analysis(
        image_type=image_type,
        hull_material=hull_material,
        hull_construction=hull_construction,
        core_material=core_material,
        deck_material=deck_material,
        propulsion=propulsion,
        builder_quality_tier=builder_quality_tier,
    )

    materials_knowledge = get_knowledge_for_materials_analysis(
        hull_material=hull_material,
        hull_construction=hull_construction,
        core_material=core_material,
        deck_material=deck_material,
    )

    structural_knowledge = get_knowledge_for_structural_analysis(
        hull_material=hull_material,
        hull_construction=hull_construction,
        core_material=core_material,
    )

    compliance_knowledge = get_knowledge_for_compliance(
        propulsion=propulsion,
        length_m=length_m,
        operating_waters=operating_waters,
    )

    service_knowledge = get_knowledge_for_service_patterns(
        hull_material=hull_material,
        hull_construction=hull_construction,
        production_type=production_type,
        builder_name=builder_name,
    )

    # Combine all knowledge
    combined = {
        "critical_warnings": visual_knowledge.get("critical_warnings", []),
        "inspection_points": visual_knowledge.get("inspection_points", []),
        "image_type_guidance": visual_knowledge.get("image_type_guidance", ""),
        "construction_knowledge": visual_knowledge.get("construction_knowledge", "")
        + "\n"
        + structural_knowledge.get("construction_method", {}).__str__(),
        "material_knowledge": visual_knowledge.get("material_knowledge", "")
        + "\n"
        + materials_knowledge.get("resin_data", {}).__str__(),
        "degradation_knowledge": visual_knowledge.get("degradation_knowledge", "")
        + "\n"
        + service_knowledge.get("common_failure_modes", []).__str__(),
    }

    # Format and return
    return format_knowledge_for_prompt(combined, max_lines=max_lines)


# =============================================================================
# HELPER UTILITIES
# =============================================================================


def list_available_knowledge_databases() -> Dict[str, int]:
    """Lists all imported knowledge databases and their entry counts."""
    databases = {
        "RESIN_DATABASE": len(RESIN_DATABASE),
        "FIBER_DATABASE": len(FIBER_DATABASE),
        "GELCOAT_DATABASE": len(GELCOAT_DATABASE),
        "CORE_MATERIALS_DATABASE": len(CORE_MATERIALS_DATABASE),
        "CONSTRUCTION_METHODS_DATABASE": len(CONSTRUCTION_METHODS_DATABASE),
        "HULL_DECK_JOINT_DATABASE": len(HULL_DECK_JOINT_DATABASE),
        "KEEL_DATABASE": len(KEEL_DATABASE),
        "RUDDER_DATABASE": len(RUDDER_DATABASE),
        "ANTIFOULING_DATABASE": len(ANTIFOULING_DATABASE),
        "ANODE_DATABASE": len(ANODE_DATABASE),
        "ENGINE_DATABASE": len(ENGINE_DATABASE),
        "COOLING_SYSTEM_DATABASE": len(COOLING_SYSTEM_DATABASE),
        "EXHAUST_DATABASE": len(EXHAUST_DATABASE),
        "FUEL_SYSTEM_DATABASE": len(FUEL_SYSTEM_DATABASE),
        "DRIVETRAIN_DATABASE": len(DRIVETRAIN_DATABASE),
        "BATTERY_DATABASE": len(BATTERY_DATABASE),
        "WIRING_DATABASE": len(WIRING_DATABASE),
        "SHORE_POWER_DATABASE": len(SHORE_POWER_DATABASE),
        "INVERTER_GENERATOR_DATABASE": len(INVERTER_GENERATOR_DATABASE),
        "SEACOCK_DATABASE": len(SEACOCK_DATABASE),
        "TOILET_DATABASE": len(TOILET_DATABASE),
        "GAS_INSTALLATION_DATABASE": len(GAS_INSTALLATION_DATABASE),
        "INTERIOR_DATABASE": len(INTERIOR_DATABASE),
        "MOISTURE_DATABASE": len(MOISTURE_DATABASE),
        "FIRE_SAFETY_DATABASE": len(FIRE_SAFETY_DATABASE),
        "STABILITY_DATABASE": len(STABILITY_DATABASE),
        "STANDARDS_DATABASE": len(STANDARDS_DATABASE),
        "STANDING_RIGGING_DATABASE": len(STANDING_RIGGING_DATABASE),
        "MAST_DATABASE": len(MAST_DATABASE),
        "SAIL_DATABASE": len(SAIL_DATABASE),
        "TEAK_DECK_DATABASE": len(TEAK_DECK_DATABASE),
        "MATERIAL_LIFESPAN_DATABASE": len(MATERIAL_LIFESPAN_DATABASE),
        "DEGRADATION_CYCLES_DATABASE": len(DEGRADATION_CYCLES_DATABASE),
        "MANUFACTURER_DATABASE_SAIL": len(MANUFACTURER_DATABASE_SAIL),
        "MANUFACTURER_DATABASE_MOTOR": len(MANUFACTURER_DATABASE_MOTOR),
        "SEALANT_DATABASE": len(SEALANT_DATABASE),
        "EPOXY_SYSTEMS": len(EPOXY_SYSTEMS),
        "COMPATIBILITY_MATRIX": len(COMPATIBILITY_MATRIX),
        "WINCH_DATABASE": len(WINCH_DATABASE),
        "BLOCK_DATABASE": len(BLOCK_DATABASE),
        "HATCH_DATABASE": len(HATCH_DATABASE),
        "MATERIAL_INTERACTION_FAILURES": len(MATERIAL_INTERACTION_FAILURES),
        "GALVANIC_SERIES_MARINE": len(GALVANIC_SERIES_MARINE),
    }
    return {k: v for k, v in databases.items() if v > 0}


def validate_parameters(
    hull_material: Optional[str],
    hull_construction: Optional[str],
    core_material: Optional[str],
    deck_material: Optional[str],
) -> Dict[str, bool]:
    """
    Validates that provided parameters can be normalized successfully.
    Returns dict with validation results.
    """
    validation = {
        "hull_material_valid": normalize_hull_material(hull_material) != "",
        "hull_construction_valid": normalize_hull_construction(hull_construction) != "",
        "core_material_valid": normalize_core_material(core_material) != "",
        "deck_material_valid": normalize_deck_material(deck_material) != "",
    }
    return validation
