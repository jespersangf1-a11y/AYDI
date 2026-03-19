"""Visual analysis prompt context builder from BoatDNA profiles.

Generates German-language boat profile strings for visual analysis prompts,
calibrated to the specific boat's identity rather than abstract classes.
"""
from __future__ import annotations

from app.domain.construction import get_construction_knowledge
from app.models.boat_dna import BoatDNA

# German labels for enum values
USE_LABELS = {
    "daysailing": "Tagestörn", "coastal_cruising": "Küstenfahrt",
    "offshore_cruising": "Offshore-Fahrtensegeln", "bluewater": "Blauwasser",
    "racing": "Regatta", "racing_cruiser": "Regatta-Cruiser",
    "weekender": "Wochenendboot", "charter": "Charter",
    "explorer": "Explorer", "sport_fishing": "Sportfischer",
    "flybridge_cruiser": "Flybridge-Cruiser", "superyacht_private": "Superyacht (privat)",
}
WATERS_LABELS = {
    "sheltered": "Geschützte Gewässer", "coastal": "Küstengewässer",
    "offshore": "Offshore", "ocean": "Ozean",
}
PROPULSION_LABELS = {"sail": "Segelboot", "motor": "Motorboot", "sail_motor": "Motorsegler"}
PRODUCTION_LABELS = {
    "mass_production": "Serienproduktion", "semi_custom": "Semi-Custom",
    "full_custom": "Full-Custom", "one_off": "Einzelbau",
}
HULL_LABELS = {
    "grp_solid": "GFK massiv", "grp_sandwich": "GFK Sandwich",
    "carbon_composite": "Carbon-Composite", "aluminium": "Aluminium",
    "steel": "Stahl", "wood_epoxy": "Holz-Epoxid", "wood_traditional": "Holz traditionell",
}
CONSTRUCTION_LABELS = {
    "hand_layup": "Handauflegung", "vacuum_bag": "Vakuumsack",
    "resin_infusion": "Vakuuminfusion", "prepreg_autoclave": "Prepreg/Autoklav",
    "welded": "Geschweißt", "riveted": "Genietet",
    "cold_molded": "Kaltgeformt", "strip_plank": "Leistenbau", "carvel": "Karweelbau",
}
CORE_LABELS = {
    "none": "Kein Kern", "balsa": "Balsaholz", "pvc_foam": "PVC-Schaum",
    "soric": "Soric", "honeycomb": "Honeycomb", "cedar": "Zedernholz",
}
DECK_LABELS = {
    "grp_nonskid": "GFK Antirutsch", "teak_laid": "Teakdeck verlegt",
    "synthetic_teak": "Synthetik-Teak", "cork": "Kork", "paint": "Lack",
}
QUALITY_LABELS = {
    "standard": "Standard (Serienproduktion)",
    "premium": "Premium (Semi-Custom)",
    "luxury": "Luxury (Custom)",
    "superyacht": "Superyacht",
}

QUALITY_BY_TIER = {
    "standard":   {"joinery_gap_mm": 3.0, "gelcoat": "leichte Orangenhaut akzeptabel", "fastener": "abgedeckt"},
    "premium":    {"joinery_gap_mm": 1.5, "gelcoat": "glatt, keine sichtbaren Fehler", "fastener": "verdeckt"},
    "luxury":     {"joinery_gap_mm": 0.8, "gelcoat": "Spiegelfinish", "fastener": "unsichtbar"},
    "superyacht": {"joinery_gap_mm": 0.5, "gelcoat": "Spiegelfinish, perfekt", "fastener": "unsichtbar"},
}


def build_visual_context(dna: BoatDNA) -> str:
    """Generate German-language boat profile for visual analysis prompts."""
    lines: list[str] = []

    # Section 1: Boot profile
    lines.append("BOOTSPROFIL:")
    lines.append(f"- Typ: {PROPULSION_LABELS.get(dna.propulsion, dna.propulsion)}, "
                 f"{dna.length_m}m × {dna.beam_m}m")
    lines.append(f"- Verwendung: {USE_LABELS.get(dna.primary_use, dna.primary_use)}")
    lines.append(f"- Fahrgebiet: {WATERS_LABELS.get(dna.operating_waters, dna.operating_waters)}")
    lines.append(f"- Bauart: {PRODUCTION_LABELS.get(dna.production_type, dna.production_type)}")
    lines.append(f"- Qualitätsniveau: {QUALITY_LABELS.get(dna.builder_quality_tier, dna.builder_quality_tier)}")
    lines.append(f"- Rumpf: {HULL_LABELS.get(dna.hull_material, dna.hull_material)}, "
                 f"{CONSTRUCTION_LABELS.get(dna.hull_construction, dna.hull_construction)}")
    if dna.core_material != "none":
        lines.append(f"- Kernmaterial: {CORE_LABELS.get(dna.core_material, dna.core_material)}")
    lines.append(f"- Deck: {DECK_LABELS.get(dna.deck_material, dna.deck_material)}")

    # Section 2: Quality standards
    quality = QUALITY_BY_TIER.get(dna.builder_quality_tier, QUALITY_BY_TIER["standard"])
    lines.append("")
    lines.append("ERWARTETE QUALITÄTSSTANDARDS für dieses Boot:")
    lines.append(f"- Spaltmaße Schreinerei: max {quality['joinery_gap_mm']}mm")
    lines.append(f"- Oberfläche: {quality['gelcoat']}")
    lines.append(f"- Befestigungen: {quality['fastener']}")

    if dna.deck_material == "teak_laid":
        caulk = 4.0 if dna.builder_quality_tier in ("standard", "premium") else 3.0
        grain = "nicht erforderlich" if dna.production_type == "mass_production" else "abgestimmt"
        lines.append(f"- Teak-Fugen: {caulk}mm, Maserung: {grain}")

    if dna.hull_material in ("aluminium", "steel"):
        weld = "strukturell" if dna.builder_quality_tier == "standard" else "kosmetisch"
        lines.append(f"- Schweißnähte: {weld}")

    if dna.hull_construction in ("resin_infusion", "prepreg_autoclave"):
        lines.append("- Laminat: gleichmäßig, hoher Glasanteil erwartet")
    elif dna.hull_construction == "hand_layup":
        lines.append("- Laminat: variable Dicke akzeptabel")

    # Section 3: Construction-specific checkpoints
    ck = get_construction_knowledge(dna.hull_material, dna.hull_construction)
    if ck:
        lines.append("")
        lines.append("KONSTRUKTIONSSPEZIFISCHE PRÜFPUNKTE:")
        for indicator in ck.get("quality_indicators_visual", []):
            lines.append(f"- {indicator}")

    # Section 4: Instruction
    lines.append("")
    lines.append("BEWERTE NACH DIESEN STANDARDS — nicht nach abstrakten Klassen.")

    return "\n".join(lines)
