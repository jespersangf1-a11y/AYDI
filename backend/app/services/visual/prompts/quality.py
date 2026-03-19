"""Build quality and craftsmanship assessment prompt."""

BOAT_CLASS_CONTEXT = {
    "small_sail": "Kleine Segelyacht (8-12m). Funktionale Verarbeitung wird erwartet. Pragmatische Loesungen sind akzeptabel, solange sie sauber ausgefuehrt sind.",
    "cruising_sail": "Fahrtensegelyacht (12-18m). Gute handwerkliche Qualitaet erwartet. Saubere Fugen, solide Beschlaege, ordentliche Polsterarbeit.",
    "large_motor": "Grosse Motoryacht (18-30m). Hohe Verarbeitungsqualitaet erwartet. Praezise Spaltmasse, hochwertige Oberflaechen, professionelle Detailloesungen.",
    "superyacht": "Superyacht (30m+). Hoechste Verarbeitungsqualitaet. Perfekte Spaltmasse, makellose Oberflaechen, unsichtbare Uebergaenge, Moebelbau auf Manufakturniveau.",
}

QUALITY_STANDARDS_BY_CLASS = {
    "small_sail": """
QUALITAETSSTANDARD fuer Serienproduktion (8-12m Segelyacht):
- Spaltmasse Schreinerei: 2-3mm akzeptabel
- Gelcoat: leichte Orangenhaut akzeptabel, keine Laeufer
- Hardware: Serienausstattung, gleichmaessige Ausrichtung
- Teakdeck: Maschinenverlegung akzeptabel, Fugen 4-6mm
- Interieur: Furnier auf Sperrholz Standard, Massivholzkanten
- Elektrik: gebuendelte Verkabelung, beschriftet am Panel
- Polster: gerade Naehte, Muster muss nicht perfekt fluchten
""",
    "cruising_sail": """
QUALITAETSSTANDARD fuer Semi-Custom Fahrtenyacht (12-18m):
- Spaltmasse: max 1-2mm, durchgehend gleichmaessig
- Gelcoat: glatt, keine sichtbaren Fehler aus 1m Abstand
- Hardware: gehobene Ausstattung, buendiger Einbau wo moeglich
- Teakdeck: Handverlegung bevorzugt, Fugen 3-5mm, gleichmaessige Maserungsrichtung
- Interieur: Massivholz oder Hochglanzfurnier, keine sichtbaren Befestigungen
- Elektrik: individuelle Kabelfuehrung, verzinntes Kupfer, Beschriftung alle 300mm
- Polster: gerade Naehte, Muster fluchten ueber Kissen hinweg
""",
    "large_motor": """
QUALITAETSSTANDARD fuer Custom Motoryacht (18-30m):
- Spaltmasse: <1mm, nirgends sichtbare Fugen
- Lack/Gelcoat: Spiegelfinish, null Fehler aus jedem Winkel
- Hardware: Premium (Lewmar/Harken/Besenzoni), perfekte Ausrichtung
- Teakdeck: handselektierte Planken, Maserung abgestimmt, Fugen 3-4mm uniform
- Interieur: Bookmatched Furnier, Massivholz, Softclose ueberall
- Elektrik: Marinekabel verzinnt, Einzeladern, vollstaendige Beschriftung, ueberall zugaenglich
- Polster: perfekte Naehte, Muster exakt ausgerichtet, keine Falten
""",
    "superyacht": """
QUALITAETSSTANDARD fuer Superyacht (30m+):
- Wie large_motor, aber: Perfektion in JEDEM Detail
- Furniere: bookmatched, sequenziert ueber ganze Raeume
- Oberflaechen: Klavierlack-Qualitaet wo Hochglanz
- Steinarbeiten: fugenlose Uebergaenge, keine Lippenbildung
- Edelstahl: Spiegelpoliert, kein Teestaining
- Beleuchtung: unsichtbare Integration, keine sichtbaren Leuchtmittel
- Gesamteindruck: Hotelqualitaet 5-Sterne+, makellos
""",
}


def get_build_quality_prompt(
    boat_class: str,
    zone_type: str | None = None,
    context: dict | None = None,
) -> str:
    """Generate the build quality assessment prompt for Claude vision API.

    Args:
        boat_class: One of small_sail, cruising_sail, large_motor, superyacht.
        zone_type: Optional zone type for context.
        context: Optional additional context dict.

    Returns:
        German-language prompt string requesting JSON output.
    """
    class_desc = BOAT_CLASS_CONTEXT.get(boat_class, BOAT_CLASS_CONTEXT["cruising_sail"])
    quality_standard = QUALITY_STANDARDS_BY_CLASS.get(boat_class, QUALITY_STANDARDS_BY_CLASS["cruising_sail"])

    zone_note = ""
    if zone_type:
        zone_note = f"\nDieser Bereich ist: {zone_type}."

    return f"""Du bist ein erfahrener Qualitaetspruefer im Yachtbau mit Spezialisierung auf Innenausbau und Verarbeitungsqualitaet. Analysiere dieses Bild.

Bootsklasse: {class_desc}{zone_note}

{quality_standard}

Bewerte die folgenden Handwerks- und Qualitaetsaspekte, soweit im Bild erkennbar:

1. **Tischlerarbeit/Schreinerei**: Spaltmasse, Ausrichtung, sichtbare Befestigungen, Oberflaechenguete
2. **Oberflaechenfinish**: Glaette, Gleichmaessigkeit, Lackqualitaet, Beschichtungen, sichtbare Maengel
3. **Beschlagmontage**: Ausrichtung von Griffen/Scharnieren/Schloessern, Dichtungsqualitaet, Befestigungsqualitaet
4. **Polsterarbeit**: Nahtfuehrung, Materialspannung, Symmetrie, Musterausrichtung, Kantenverarbeitung

REGELN:
1. Bewerte NUR was tatsaechlich im Bild sichtbar ist — keine Vermutungen.
2. Kalibriere die Bewertung an der Bootsklasse: was bei einer Serienboot akzeptabel ist, kann bei einer Superyacht ein Mangel sein.
3. Jeder Befund braucht eine Ortsangabe im Bild (oben/unten/links/rechts/Mitte).
4. Unterscheide klar zwischen gesicherter Beobachtung und Vermutung.
5. Wenn etwas nicht erkennbar ist, sage das explizit mit "nicht beurteilbar".
6. Sei EHRLICH — beschoenige keine Maengel, aber erfinde auch keine.

Antworte ausschliesslich mit einem JSON-Objekt (kein zusaetzlicher Text):

{{
    "assessable": <bool>,
    "overall_quality_score": <float 0-100>,
    "joinery": {{
        "score": <float 0-100 oder null>,
        "gap_consistency": "<gleichmaessig/ungleichmaessig/nicht beurteilbar>",
        "alignment": "<praezise/akzeptabel/mangelhaft/nicht beurteilbar>",
        "visible_fasteners": "<keine/wenige/viele/nicht beurteilbar>",
        "finish_quality": "<hochwertig/gut/maessig/mangelhaft/nicht beurteilbar>",
        "observations": ["<string>", ...]
    }},
    "surfaces": {{
        "score": <float 0-100 oder null>,
        "smoothness": "<makellos/gut/Maengel sichtbar/nicht beurteilbar>",
        "evenness": "<gleichmaessig/leichte Abweichungen/uneben/nicht beurteilbar>",
        "defects_visible": ["<string: Beschreibung>", ...],
        "observations": ["<string>", ...]
    }},
    "hardware": {{
        "score": <float 0-100 oder null>,
        "alignment": "<praezise/akzeptabel/schief/nicht beurteilbar>",
        "seal_quality": "<dicht/fraglich/undicht/nicht beurteilbar>",
        "observations": ["<string>", ...]
    }},
    "upholstery": {{
        "score": <float 0-100 oder null>,
        "seam_quality": "<praezise/akzeptabel/unsauber/nicht beurteilbar>",
        "material_tension": "<gleichmaessig/leichte Falten/wellig/nicht beurteilbar>",
        "observations": ["<string>", ...]
    }},
    "overall_findings": [
        {{
            "category": "<joinery/surfaces/hardware/upholstery/general>",
            "observation": "<string: was beobachtet wurde>",
            "location_in_image": "<oben-links/oben-rechts/unten-links/unten-rechts/mitte/...>",
            "assessment": "<positiv/neutral/negativ>",
            "confidence": "<hoch/mittel/niedrig>",
            "meets_class_standard": <bool>,
            "suggestion": "<string oder null>"
        }}
    ],
    "positive_aspects": ["<string>", ...],
    "concerns": [
        {{
            "area": "<string: betroffener Bereich>",
            "issue": "<string: Beschreibung des Problems>",
            "severity": "<kritisch/mittel/gering>",
            "suggestion": "<string>"
        }}
    ],
    "cannot_assess": ["<string: Aspekt der nicht bewertet werden kann>", ...],
    "confidence_overall": "<hoch/mittel/niedrig>",
    "confidence_reasoning": "<string: warum diese Konfidenz>"
}}"""
