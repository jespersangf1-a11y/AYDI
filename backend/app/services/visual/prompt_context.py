"""Visual analysis prompt context builder from BoatDNA profiles.

Generates German-language boat profile strings for visual analysis prompts,
calibrated to the specific boat's identity rather than abstract classes.
Includes deep expert knowledge injection from AYDI knowledge base.
"""
from __future__ import annotations

from app.domain.construction import get_construction_knowledge
from app.models.boat_dna import BoatDNA
from app.services.knowledge.hull_construction_deep import RESIN_DATABASE
from app.services.knowledge.inspection_knowledge import INSPECTION_ZONES

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
    """Generate German-language boat profile for visual analysis prompts.

    Includes expert knowledge injection from AYDI knowledge base.
    """
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

    # Section 4: EXPANDED KNOWLEDGE INJECTION
    lines.append("")
    lines.append("="*80)
    lines.append("EXPERT WISSENS-KONTEXT (AYDI Knowledge Base)")
    lines.append("="*80)

    # Material knowledge
    lines.append("")
    lines.append(build_material_knowledge_context(
        hull_material=dna.hull_material,
        hull_construction=dna.hull_construction,
        core_material=dna.core_material if dna.core_material != "none" else None,
        deck_material=dna.deck_material,
    ))

    # Degradation knowledge
    lines.append("")
    lines.append(build_degradation_knowledge_context(
        hull_material=dna.hull_material,
        hull_construction=dna.hull_construction,
        core_material=dna.core_material if dna.core_material != "none" else None,
    ))

    # Manufacturer context
    lines.append("")
    lines.append(build_manufacturer_context(
        builder_name=dna.builder_name if hasattr(dna, 'builder_name') else None,
        production_type=dna.production_type,
        quality_tier=dna.builder_quality_tier,
    ))

    # Safety & compliance
    lines.append("")
    lines.append(build_safety_compliance_context(
        propulsion=dna.propulsion,
        length_m=dna.length_m,
    ))

    # Systems knowledge
    lines.append("")
    lines.append(build_systems_knowledge_context(
        propulsion=dna.propulsion,
    ))

    # Section 5: Instruction
    lines.append("")
    lines.append("="*80)
    lines.append("BEWERTUNGS-ANWEISUNG:")
    lines.append("="*80)
    lines.append("")
    lines.append("1. BEWERTE NACH DEN BOOT-SPEZIFISCHEN STANDARDS oben, nicht nach abstrakten Klassen.")
    lines.append("2. NUTZE das EXPERT WISSEN als Hintergrund für Inspektions-Schwerpunkte.")
    lines.append("3. BEI MATERIAL-BEFUNDEN: Referenziere spezifische Harztypen, Fasertechniken, "
                "Kernmaterial-Risiken aus dem Wissen-Kontext.")
    lines.append("4. BEI DEGRADATION: Erkenne Osmose-Stadien, Korrosionsmuster, "
                "Kern-Ausfallmodi mit Bezug zum Boot-Alter und Material.")
    lines.append("5. BEI SYSTEMEN: Prüfe auf Boot-spezifische Risiken (Motor, Segelanlage, "
                "Sicherheits-Systeme) basierend auf Propulsion und Größe.")
    lines.append("6. NOCH IMMER REGEL: Bewerte NUR was sichtbar ist. Sag 'nicht beurteilbar' "
                "wenn unsicher.")

    return "\n".join(lines)


def build_material_knowledge_context(
    hull_material: str | None = None,
    hull_construction: str | None = None,
    core_material: str | None = None,
    deck_material: str | None = None,
) -> str:
    """Build detailed material knowledge section for vision prompts.

    Includes resin properties, fiber characteristics, core material risks,
    known degradation patterns, and visual inspection indicators.

    Args:
        hull_material: Hull material type (grp_solid, grp_sandwich, aluminium, etc.)
        hull_construction: Construction method (hand_layup, resin_infusion, etc.)
        core_material: Sandwich core material (balsa, pvc_foam, etc.)
        deck_material: Deck material type (teak_laid, grp_nonskid, etc.)

    Returns:
        German-language knowledge context string.
    """
    lines = []
    lines.append("MATERIAL-TIEFENWISSEN:")
    lines.append("")

    # Hull material knowledge
    if hull_material == "grp_solid" or hull_material == "grp_sandwich":
        lines.append("RUMPFLAMINAT (GFK):")
        lines.append("- Harztypen: Orthophthal-Polyester (anfällig für Osmose nach 10-15J), "
                    "Isophthal-Polyester (bessere Wasserfestigkeit, 15-20J), "
                    "Vinylester (bis 40J osmosefrei, premium)")
        lines.append("- Gelcoat: Schützende erste Lage, 0,5-1,0mm. "
                    "Orangenhaut (Oberflächenrauheit) ist normal bei älteren Booten.")
        lines.append("- Glasfasertypen: E-Glas (Standard), S-Glas/R-Glas (höhere Festigkeit), "
                    "Kohlefaser (premium/Performance)")
        lines.append("- Laminataufbau: äußerer Gelcoat → Chopped-Strands (zufällig) → "
                    "Rovings (Längsfestigkeit) → bei Sandwich: Kernmaterial → Spiegellaminat")
        lines.append("- Osmose-Mechanismus: Wasser diffundiert durch Gelcoat, hydrolysiert "
                    "Ester-Bindungen im Polyester, erzeugt saure Abbauprodukte (Essiggeruch), "
                    "osmotischer Druck hebt Gelcoat ab → domförmige Blasen")
        lines.append("- Visuelle Indikatoren für Probleme: Blasen >5mm, Säure-Geruch, "
                    "Verfärbungen (dunkelbraun), Gelcoat-Abbröskelung, Delamination bei Druck")
        lines.append("")

    if hull_construction == "resin_infusion" or hull_construction == "vacuum_bag":
        lines.append("VAKUUMINFUSION (Hochwertiges Verfahren):")
        lines.append("- Gleichmäßiges Laminat durch Vakuumdruckverteilung, "
                    "höherer Glasfaseranteil (55-65% vs. 40-55% bei Handlaminat)")
        lines.append("- Vorteil: Reproduzierbare Qualität, bessere Steifigkeit")
        lines.append("- Risiken: Kerndelamination bei Wassereintritt (besonders um "
                    "Hardware-Befestigungen), Druckstellen im Kern (1-5J nach Bau)")
        lines.append("- Inspektions-Checkpoint: Klopftest auf hohle Stellen (Delamination), "
                    "Dellen um Winschen/Klampen (Kernkompression)")
        lines.append("")

    elif hull_construction == "hand_layup":
        lines.append("HANDAUFLEGUNG (Traditionelle Methode):")
        lines.append("- Variable Qualität abhängig vom Laminierteam")
        lines.append("- Glasanteil kann schwanken (40-55%)")
        lines.append("- Lufteinschlüsse möglich → Schwachstellen")
        lines.append("- Visuelle Zeichen guter Ausführung: gleichmäßige Gelcoat-Oberfläche, "
                    "keine sichtbaren Blasen, saubere Kanten")
        lines.append("")

    # Core material knowledge
    if core_material and core_material != "none":
        lines.append("KERNMATERIAL (Sandwich-Konstruktion):")
        if core_material == "balsa":
            lines.append("- Balsaholz: Natürliches Holz, hohes Steifigkeit-zu-Gewicht, "
                        "aber anfällig für Feuchtigkeit")
            lines.append("- Risiko: Fäulnis bei Wassereintritt (besonders um Through-Hulls, "
                        "Hardware-Verschraubungen)")
            lines.append("- Visuelle Warnsignale: Dellen, Druckstellen, dunkle Verfärbungen "
                        "(Feuchtigkeit), Delamination")
            lines.append("- Prüfmethode: Klopftest (hohler Klang = Wasser im Kern)")
        elif core_material == "pvc_foam":
            lines.append("- PVC-Schaum (Divinycell, etc.): Synthetisch, sehr feuchtigkeitsresistent")
            lines.append("- Länger haltbar als Balsa, aber teurer")
            lines.append("- Risiko: Scherversagen bei Überbelastung (Dellen, Verformung)")
            lines.append("- Visuelle Zeichen: saubere Oberfläche, keine Druckstellen, "
                        "keine Verfärbungen")
        lines.append("")

    # Deck material knowledge
    if deck_material == "teak_laid":
        lines.append("TEAKDECK (verlegt):")
        lines.append("- Echtholz-Planken (Teak aus Burma oder Plantagen)")
        lines.append("- Fugenfüllstoff: üblicherweise polyurethane-basiert oder Terpentin-Filler")
        lines.append("- Alterszeichen: Silbergraue Oberfläche (normale UV-Patina), "
                    "feine Risse in Querfasern (normal bei Alterung)")
        lines.append("- Visuelle Warnsignale: tiefe Längsfäden (Schrumpfung), fehlende "
                    "Fugenmasse (Undichtheit), schwarze Flecken (Schimmel/Feuchtigkeit), "
                    "Verformungen (Quellung/Schwund)")
        lines.append("- Zustand-Bewertung: Die graumetallisch angewitterte Oberfläche ist normal "
                    "und nicht negativ — wichtig ist die strukturelle Integrität")
        lines.append("")
    elif deck_material == "grp_nonskid":
        lines.append("GFK-DECK (Anti-Rutsch):")
        lines.append("- Oberfläche mit eingearbeiteten Rutschkörnchen (Aluminiumoxid, etc.)")
        lines.append("- Geringere Wartung als Teak, langlebiger")
        lines.append("- Visuelle Zeichen von Verschleiß: abgelöste Körner, "
                    "matte/verschlissene Bereiche")
        lines.append("")

    return "\n".join(lines)


def build_degradation_knowledge_context(
    hull_material: str | None = None,
    hull_construction: str | None = None,
    core_material: str | None = None,
) -> str:
    """Build degradation cycle knowledge for vision prompts.

    Includes osmosis mechanisms, moisture paths, galvanic risks,
    and material lifespan expectations.

    Args:
        hull_material: Hull material type
        hull_construction: Construction method
        core_material: Sandwich core material

    Returns:
        German-language degradation knowledge string.
    """
    lines = []
    lines.append("ABBAU- UND ALTERUNGSMECHANISMEN:")
    lines.append("")

    if hull_material and "grp" in hull_material:
        lines.append("OSMOTISCHE BLASENBILDUNG (GFK-spezifisch):")
        lines.append("1. ANFANGSPHASE (Jahre 5-10 bei Dauerbelastung):")
        lines.append("   - Wasser diffundiert durch mikroskopische Poren im Gelcoat")
        lines.append("   - Beim Eindringen: kaum sichtbar, keine Symptome")
        lines.append("")
        lines.append("2. HYDROLYSE-PHASE (Jahre 10-20):")
        lines.append("   - Wassermoleküle spalten Ester-Bindungen im Polyester-Harz")
        lines.append("   - Entstehung von Essigsäure, Glykol, Wasser (flüchtige Abbauprodukte)")
        lines.append("   - Erste Blasen erscheinen, oft am Unterwasserschiff")
        lines.append("")
        lines.append("3. SELBSTVERSTÄRKENDE PHASE (Jahre 20+):")
        lines.append("   - Abbauprodukte greifen restliche Ester-Gruppen an")
        lines.append("   - Blasen wachsen, Säurekonzentration steigt (Essiggeruch wird deutlich)")
        lines.append("   - Osmotischer Druck hebt Gelcoat ab → domförmige weiße Blasen")
        lines.append("")
        lines.append("PRÄVENTION & SYMPTOME:")
        lines.append("- Frühe Warnsignale: Säuerlicher Geruch (essig-ähnlich), "
                    "Blasen <3mm an Unterwasserschiff")
        lines.append("- Entwicklung: Blasen >5mm, gehäuft, dunkler/verfärbt")
        lines.append("- Langfristig: Gelcoat-Abbau, Faseraufrauung, Laminat-Schwachstellen")
        lines.append("")

    if hull_material == "aluminium":
        lines.append("GALVANISCHE KORROSION (Aluminium-spezifisch):")
        lines.append("- Aluminium ist unedles Metall (Galvanische Reihe)")
        lines.append("- Risiko: Kontakt mit edleren Metallen (Kupfer, Stahl, Bronze, Edelstahl)")
        lines.append("  in Gegenwart von Salzwasser = Galvani-Element → Aluminium wird Anode → korrodiert")
        lines.append("- Häufige Fehler: Stahlschrauben in Aluminium ohne Isolierung, "
                    "Kupferleitungen direkt auf Aluminium, Bronzebeschlagverschraubungen")
        lines.append("- Visuell: Weiße Oxidation (Aluminium-Hydroxid) um Befestigungsstellen, "
                    "schwarze Verfärbungen (Korrosion)")
        lines.append("- Prävention: Isoliermaterial (Teflon, Nylon), passende Metalle, "
                    "Opferanoden (Zink/Magnesium)")
        lines.append("")

    if core_material == "balsa":
        lines.append("KERNMATERIAL-DEGRADATION (Balsaholz):")
        lines.append("- Balsaholz hat Holzfasern (porig, hygroskopisch)")
        lines.append("- Feuchtigkeitspfade: Risse im Gelcoat → Wasser ins Laminat → Kern")
        lines.append("- Fäulnismechanismus: Feuchte + mangelnde Belüftung → Pilzbefall → Holzabbau")
        lines.append("- Häufig um: Through-Hull-Verschraubungen, Fender-Augen, "
                    "Winschen-Befestigungen, Klampen")
        lines.append("- Frühe Zeichen: Dellen, lokale Weichheit beim Druck, leichte Druckstellen")
        lines.append("- Späte Zeichen: Großflächige Delamination, Kern-Raumgeruch, "
                    "Strukturelles Versagen")
        lines.append("")

    lines.append("ALTERSERWARTUNG nach Material:")
    lines.append("- Orthophthal-Polyester GFK: 20-25 Jahre osmosefrei (dann anfällig)")
    lines.append("- Isophthal-Polyester mit Barriere-Coat: 25-35 Jahre")
    lines.append("- Vinylester (vollständig): 40+ Jahre")
    lines.append("- Teak-Deck: 30-50 Jahre mit regelmäßiger Wartung, 20 Jahre ohne")
    lines.append("- Holzernmaterial (Balsa): 25-35 Jahre, bei Leckage sofort Risiko")
    lines.append("")

    return "\n".join(lines)


def build_manufacturer_context(
    builder_name: str | None = None,
    production_type: str | None = None,
    quality_tier: str | None = None,
) -> str:
    """Build manufacturer-specific knowledge context.

    Includes known issues, quality patterns, and common weak points.

    Args:
        builder_name: Yard/manufacturer name
        production_type: mass_production, semi_custom, full_custom, one_off
        quality_tier: standard, premium, luxury, superyacht

    Returns:
        German-language manufacturer knowledge string.
    """
    lines = []
    lines.append("HERSTELLER- UND PRODUKTIONSTYP-WISSEN:")
    lines.append("")

    if production_type == "mass_production":
        lines.append("SERIENPRODUKTION (Massenherstellung):")
        lines.append("- Standardisierte Werkzeuge, wiederholte Prozesse")
        lines.append("- Fokus: Kostenkontrolle, schnelle Fertigung")
        lines.append("- Typische Material-Qualität: Orthophthal-Polyester GFK (kostengünstig)")
        lines.append("- Schwachstellen: Variable Handwerk-Qualität, Spaltmaße größer, "
                    "Beschlagmontage einfacher")
        lines.append("- Qualitäts-Streuschwankungen zwischen Booten derselben Serie möglich")
        lines.append("- Erwartung: Solide Funktion, handwerkliche Fehler verzeihlich")
        lines.append("")

    elif production_type == "semi_custom":
        lines.append("SEMI-CUSTOM (Teilweise Anpassung):")
        lines.append("- Einzelne Werkzeuge pro Boot, aber Standard-Laminat-Prozesse")
        lines.append("- Fokus: Qualität und Kundenspezifikation im Gleichgewicht")
        lines.append("- Typische Material-Qualität: Isophthal-Polyester oder Vinylester, "
                    "Vakuum-Infusion häufig")
        lines.append("- Höhere Handwerk-Standards erwartet")
        lines.append("- Schwachstellen: Gelegentliche Verarbeitungsfehler, aber reparabel")
        lines.append("")

    elif production_type == "full_custom":
        lines.append("FULL-CUSTOM (Vollständige Kundenentwicklung):")
        lines.append("- Maßgeschneidert, Hochleistungs-Prozesse (Prepreg, Infusion)")
        lines.append("- Fokus: Perfektion, Premium-Materialien")
        lines.append("- Materialien: Vinylester, Carbon, höchste Spezifikationen")
        lines.append("- Handwerk-Standard: Sehr hoch, Fehler sind Mangel")
        lines.append("- Erwartung: Makellose Verarbeitung, präzise Spaltmaße, "
                    "unsichtbare Befestigungen")
        lines.append("")

    if quality_tier == "superyacht":
        lines.append("SUPERYACHT-BAUTEN:")
        lines.append("- Höchste Standards überall — nicht nur Struktur sondern auch Details")
        lines.append("- Materialien: Edelhölzer (Teak, Mahagoni), Marmor, Naturstein, feinstes Leder")
        lines.append("- Verarbeitung: Manufaktur-Niveau, jedes Detail kalibriert")
        lines.append("- Gelcoat-Standard: Spiegelfinish, Null-Fehler")
        lines.append("- Hardware: Premium-Marken (Lewmar, Harken), vollständig poliert")
        lines.append("- Teak: Handverlegt, Maserung sequenziert, fugen 3-4mm konsistent")
        lines.append("")

    return "\n".join(lines)


def build_safety_compliance_context(
    propulsion: str | None = None,
    length_m: float | None = None,
) -> str:
    """Build safety and compliance knowledge context.

    Includes relevant ISO standards, fire safety, stability requirements.

    Args:
        propulsion: Propulsion type (sail, motor, sail_motor)
        length_m: Boat length in meters

    Returns:
        German-language safety/compliance knowledge string.
    """
    lines = []
    lines.append("SICHERHEITS- UND NORMEN-WISSEN:")
    lines.append("")

    lines.append("RELEVANTE ISO-STANDARDS (EU-Bootssicherheit):")
    lines.append("- ISO 12215 (Rumpf-Laminat Konstruktion): Mindeststärken nach Bootsgröße")
    lines.append("- ISO 12216 (Fenster & Luken): Wasserdichtheits- und Druckanforderungen")
    lines.append("- ISO 11812 (Elektrische Systeme): Kabelquerschnitte, Schutzvorrichtungen")
    lines.append("- ISO 11192 (Abgasanlage): Auspuff-Durchmesser, Temperatur-Limits")
    lines.append("- ISO 10088 (Edelstahl-Rohre): Legierungsstandards, Dicken")
    lines.append("")

    if propulsion == "motor" or propulsion == "sail_motor":
        lines.append("MOTORISCHE ANTRIEBSSYSTEME:")
        lines.append("- Typische Motoren: Diesel (zuverlässig, lange Lebensdauer), "
                    "Benzin (leiser, höheres Brandrisiko)")
        lines.append("- Inspektions-Checkpoints: Getriebeöl-Stand, Kühlwasser-Stand, "
                    "Abgasanlage (Korrosion), Motorlager-Verschleiß")
        lines.append("- Seewasser-Kühlsystem: Durch-Hull Seacock (ISO 1770), "
                    "Kühlwasser-Schlauch (zugelastete Qualität), Zinkanoden (Schutz)")
        lines.append("- Kraftstoffsystem: Marine-Grade Leitungen (nicht Auto), "
                    "Benzin-Verdampfungsrisiko (Explosivgefahr), Diesel-Kontamination (Wasser, "
                    "Partikel)")
        lines.append("")

    if propulsion == "sail" or propulsion == "sail_motor":
        lines.append("SEGELANTRIEB:")
        lines.append("- Rigg-Inspektionen: Wanten (Drahtseil), Vorstag, Fallen (Stahlseil oder Tauwerk)")
        lines.append("- Wantenspannung: Visuelle Symmetrie, kein extremes Durchhängen")
        lines.append("- Baum-Befestigung: Gooseneck-Lager (sollte nicht locker sein), "
                    "Baum-Beschlag-Integrität")
        lines.append("- Segel: Material (Dacron, Laminat), Verschleiß an Kanten, Risse, "
                    "UV-Schäden (Verbleichung)")
        lines.append("")

    if length_m is not None:
        lines.append(f"LÄNGEN-SPEZIFISCHE ANFORDERUNGEN (Boot: {length_m}m):")
        if length_m < 7:
            lines.append("- Kleine Schiffe <7m: Vereinfachte Anforderungen, "
                        "aber Sicherheit gleich wichtig")
        elif length_m < 12:
            lines.append("- Schiffe 7-12m: Grundanforderungen nach ISO 12215, "
                        "Stabilität-Berechnung nötig für Motor")
        elif length_m < 24:
            lines.append("- Schiffe 12-24m: Vollständige ISO-Anforderungen, "
                        "Gewichtskontrolle kritisch, Stabilitäts-Nachweise erforderlich")
        else:
            lines.append("- Große Schiffe >24m: Professionelle Standards, "
                        "möglicherweise Klassifizierungen, regelmäßige Inspektionen, "
                        "Zertifikationen (Lloyd's, ABS, DNV, Germanischer Lloyd)")
        lines.append("")

    return "\n".join(lines)


def build_systems_knowledge_context(
    propulsion: str | None = None,
) -> str:
    """Build systems knowledge for engine/electrical/plumbing analysis.

    Includes engine failure modes, electrical standards, seacock requirements.

    Args:
        propulsion: Propulsion type (sail, motor, sail_motor)

    Returns:
        German-language systems knowledge string.
    """
    lines = []
    lines.append("SYSTEME UND INSTALLATION-WISSEN:")
    lines.append("")

    if propulsion == "motor" or propulsion == "sail_motor":
        lines.append("MOTOR & ANTRIEBSSYSTEM (Diesel/Benzin):")
        lines.append("")
        lines.append("TYPISCHE AUSFALLMODI:")
        lines.append("- Kühlwasser-Blockade: Salzwasser-Seacock verstopft, Algen im Schlauch, "
                    "korrodierte Nippel")
        lines.append("- Getriebeöl-Emulsion: Wasser im Öl (milchig) → Motor-Wassereintritt, "
                    "falsche Drainageleitung")
        lines.append("- Kraftstoff-Kontamination: Wasser im Tank (braune Ablagerungen), "
                    "Algenbefall bei Diesel, Oxidation bei älterem Benzin")
        lines.append("- Auspuff-Korrosion: Seewasser durch Auspuff-Leck zurück in Motor, "
                    "fehlende Rückstau-Vorrichtung")
        lines.append("- Starter/Lichtmaschine: Salzwasser-Korrosion, fehlender Schutz, "
                    "Scheuerstellen an Kabeln")
        lines.append("")
        lines.append("INSPEKTIONS-CHECKPOINTS:")
        lines.append("- Motorraumzustand: Saubere, keine Ölflecken, kein Fuel-Odor")
        lines.append("- Seacock-Zustand: Griff drehbar? Nicht korrodiert? Wasserdicht? "
                    "Falsche Position = Gefahr beim Segeln")
        lines.append("- Auspuff-Rohr: Keine Risse, keine Einfahrtswasser-Leckage, "
                    "Wasserleitung nicht drucklos")
        lines.append("- Kraftstoff-Leitungen: Verschlouchert (nicht hart/brüchig), keine Druckstellen, "
                    "Seewasser-Schlauch ISO 6134 oder besser")
        lines.append("- Batterie-Installation: Befestigt, kein korrosives Nagetier-Nesting, "
                    "Kabel verzinnt (nicht kupfer-blank)")
        lines.append("")

    lines.append("ELEKTRISCHES SYSTEM (Allgemein):")
    lines.append("- Hauptschalter (Batteriemaster): Sollte zugänglich und sicher sein")
    lines.append("- Kabelquerschnitte: Marine-Standard verzinntes Kupfer, Größe nach "
                "Stromstärke (amp-rating)")
    lines.append("- Erdung (Ground): Negative Batteriepol mit Schiffsrumpf verbunden? "
                "(Isolations-Fehler möglich)")
    lines.append("- Schutzschalter (RCD/GFCI): Für Landstrom-Anschlüsse (230V), "
                "nicht immer Standard in älteren Booten")
    lines.append("- LED-Umrüstung: Modern, aber Pulsation-Probleme mit elektronischen "
                "Reglern möglich")
    lines.append("- Beschriftung: Alle Stromkreise sollten beschriftet sein, oft nicht vorhanden "
                "bei älteren Yachten")
    lines.append("")

    lines.append("FRISCHWASSER & ABWASSERSYSTEM (Plumbing):")
    lines.append("- Seacocks (Durchbrüche ins Wasser): Sollten zugänglich und drehbar sein, "
                "Notfall-Verschluss erforderlich")
    lines.append("- Material: Bronzekörper (nicht Kunststoff — bricht bei Stosslast), "
                "verchromte Griffe (korrodieren aber funktionieren)")
    lines.append("- Schläuche: Marinequalität (FDA- oder USDA-zertifiziert), "
                "nicht Standard-Auto-Schläuche")
    lines.append("- Rückstau-Vorrichtung: Gegen Rückfluss (z.B. Auspuff), sollte vorhanden sein")
    lines.append("- Toiletten-System: Direkter Überboard (veraltet), Holding-Tank, "
                "oder Kompost-Toilette")
    lines.append("- Verschlaucherung: Alte Schläuche werden hart/spröde → Undichtigkeit, "
                "Risse bei Vibration")
    lines.append("")

    return "\n".join(lines)
