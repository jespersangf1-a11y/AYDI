"""Material assessment prompt for yacht photos."""

BOAT_CLASS_CONTEXT = {
    "small_sail": "Kleine Segelyacht (8-12m). Robuste, salzwasserbestaendige Materialien. GFK, Teak, Edelstahl. Funktion vor Aesthetik.",
    "cruising_sail": "Fahrtensegelyacht (12-18m). Hochwertige maritime Materialien. Teak, Mahagoni, Edelstahl, UV-bestaendige Stoffe. Balance aus Haltbarkeit und Aesthetik.",
    "large_motor": "Grosse Motoryacht (18-30m). Premium-Materialien erwartet. Edle Hoelzer, Naturstein, hochwertiges Leder, polierter Edelstahl. Luxusanmutung wichtig.",
    "superyacht": "Superyacht (30m+). Exklusivste Materialien. Marmor, exotische Hoelzer, feinstes Leder, massgeschneiderte Textilien, vergoldete oder galvanisierte Beschlaege.",
}


def get_material_assessment_prompt(
    boat_class: str,
    zone_type: str | None = None,
    context: dict | None = None,
    visual_context: str | None = None,
) -> str:
    """Generate the material assessment prompt for Claude vision API.

    Args:
        boat_class: One of small_sail, cruising_sail, large_motor, superyacht.
        zone_type: Optional zone type for context.
        context: Optional additional context dict.
        visual_context: Optional boat-specific context from BoatDNA (includes expert knowledge).

    Returns:
        German-language prompt string requesting JSON output.
    """
    class_desc = BOAT_CLASS_CONTEXT.get(boat_class, BOAT_CLASS_CONTEXT["cruising_sail"])

    zone_note = ""
    if zone_type:
        zone_note = f"\nDieser Bereich ist: {zone_type}."

    visual_context_section = ""
    if visual_context:
        visual_context_section = f"\n\n{visual_context}\n"

    return f"""Du bist ein erfahrener Material-Experte im Yachtbau mit umfassendem Wissen ueber maritime Werkstoffe, deren Alterungsverhalten und Qualitaetsmerkmale. Analysiere dieses Bild.{visual_context_section}

Bootsklasse: {class_desc}{zone_note}

Bewerte die folgenden Materialaspekte, soweit im Bild erkennbar:

1. **Materialidentifikation**: Welche Materialien sind sichtbar? (Holzart, Steinart, Ledertyp, Metall, Textil, Kunststoff)
2. **Materialzustand**: Alterungszeichen, Verschleiss, Verfaerbungen, Risse, Quellungen
3. **Oberflaechenqualitaet**: Politur, Mattigkeit, Gleichmaessigkeit, Schutzschicht-Zustand
4. **Materialharmonie**: Passen die Materialien zusammen? Farbharmonie, Stilkonsistenz, Uebergaenge zwischen Materialien

WICHTIG: Wenn etwas nicht erkennbar ist, sage das explizit mit "nicht beurteilbar". Identifiziere Materialien nur, wenn du dir hinreichend sicher bist. Verwechsle nicht Echtholz mit Furnier oder Laminat — wenn unklar, sage es.

Antworte ausschliesslich mit einem JSON-Objekt (kein zusaetzlicher Text):

{{
    "material_score": <float 0-100>,
    "assessable": <bool>,
    "materials_identified": [
        {{
            "material": "<string: Materialbezeichnung>",
            "location": "<string: wo im Bild sichtbar>",
            "confidence": "<sicher/wahrscheinlich/vermutet>",
            "quality_impression": "<hochwertig/gut/durchschnittlich/mangelhaft/nicht beurteilbar>",
            "maritime_eignung": "<hervorragend/gut/bedingt/ungeeignet/nicht beurteilbar>"
        }}
    ],
    "condition_assessment": {{
        "overall_condition": "<neuwertig/gut erhalten/Gebrauchsspuren/renovierungsbeduerftig/nicht beurteilbar>",
        "aging_signs": ["<string>", ...],
        "maintenance_quality": "<vorbildlich/angemessen/vernachlaessigt/nicht beurteilbar>"
    }},
    "harmony": {{
        "color_harmony": "<harmonisch/akzeptabel/dissonant/nicht beurteilbar>",
        "style_consistency": "<einheitlich/leichte Brueche/inkonsistent/nicht beurteilbar>",
        "material_count_visible": <int>,
        "assessment": "<string>"
    }},
    "findings": [
        {{
            "material": "<string>",
            "observation": "<string>",
            "rating": "<positiv/neutral/negativ>",
            "suggestion": "<string oder null>"
        }}
    ],
    "confidence": "<hoch/mittel/niedrig>",
    "cannot_assess": ["<string>", ...]
}}"""
