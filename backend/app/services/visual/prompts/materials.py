"""Material assessment prompt for yacht photos."""

from app.services.visual.prompt_context import (
    ASSESSABILITY_RULES,
    CLASS_FALLBACK_NOTICE,
    build_zone_note,
    resolve_boat_class_context,
)

# Alle 13 Bootsklassen aus BoatClass. Ohne eigenen Eintrag wuerde eine Klasse
# still gegen den Fahrtensegler-Massstab bewertet (B-3).
BOAT_CLASS_CONTEXT = {
    "small_sail": "Kleine Segelyacht (8-12m). Robuste, salzwasserbestaendige Materialien. GFK, Teak, Edelstahl. Funktion vor Aesthetik.",
    "cruising_sail": "Fahrtensegelyacht (12-18m). Hochwertige maritime Materialien. Teak, Mahagoni, Edelstahl, UV-bestaendige Stoffe. Balance aus Haltbarkeit und Aesthetik.",
    "racing_sail": "Regattayacht. Gewichtsoptimierte Werkstoffe: Carbon-Composite, Wabenkern, Sichtlaminat, minimale Innenverkleidung. Sichtbares Laminat und fehlende Furniere sind gewollt, kein Mangel. Bewerte Laminatqualitaet, Faserverlauf und Krafteinleitungspunkte statt Edelholzanmutung.",
    "daysailer": "Daysailer/Weekender. Wenige, pflegeleichte Materialien: GFK, lackiertes oder geoeltes Holz, abwaschbare Polster. Aussenbewitterte Flaechen dominieren — UV-Bestaendigkeit und Rutschfestigkeit sind wichtiger als Edelmaterialien.",
    "motorsailer": "Motorsegler. Grosse verglaste Deckssalonflaechen: Scheibenmaterial, Dichtungen und Rahmenkorrosion sind Schwerpunkt. Innen solide Fahrtenqualitaet — Massivholzkanten, strapazierfaehige Bezuege, seewasserfeste Beschlaege.",
    "catamaran_sail": "Segel-Katamaran. Gewichtssensibel trotz Fahrtenanspruch: Sandwichlaminat mit Schaumkern, Leichtbauplatten statt Massivholz, oft Synthetik-Teak. Leichte Bauweise ist konstruktiv gewollt. Achte auf Kernanbindung und Feuchteschutz an Beschlagsdurchbruechen.",
    "catamaran_motor": "Motor-Katamaran. Grosse Sandwichflaechen, viel Aussenbereich, oft Synthetik-Teak und witterungsfeste Polster. Bewerte UV- und Feuchtebestaendigkeit der Aussenmaterialien sowie den Zustand grosser Fensterbaender.",
    "small_motor": "Kleine Motoryacht (unter 12m). Zweckmaessige Serienmaterialien: GFK, Kunststofflaminat, Vinylpolster, verchromte Beschlaege. Bewerte Salzwassertauglichkeit und Verschleiss an Griffflaechen, nicht Exklusivitaet.",
    "large_motor": "Grosse Motoryacht (18-30m). Premium-Materialien erwartet. Edle Hoelzer, Naturstein, hochwertiges Leder, polierter Edelstahl. Luxusanmutung wichtig.",
    "sport_cruiser": "Sport-Cruiser. Hoher Aussenanteil: Kunstleder-Polster, Gelcoat-Hochglanz, Edelstahl-Reling, lackierte Sichtflaechen. UV-Belastung und Abrieb an Einstiegen sind die kritischen Punkte; innen zaehlt pflegeleichte Verarbeitung.",
    "trawler": "Trawler/Verdraenger. Langlebigkeit vor Glanz: dicke Laminate oder Stahl/Alu, Massivholz statt duennem Furnier, robuste Bodenbelaege. Bewerte Korrosionsschutz, Dichtungen und Wartbarkeit hoeher als Oberflaechenfinesse.",
    "explorer": "Explorer/Expeditionsyacht. Oft Aluminium oder Stahl mit Zweikomponenten-Lack. Schwerpunkte: Korrosions- und Galvanikschutz, Isolierung gegen Kaelte/Kondens, reparierbare Werkstoffe. Gebrauchsspuren an Arbeitsflaechen sind normal.",
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
        boat_class: One of the 13 BoatClass values (e.g. 'cruising_sail', 'trawler').
        zone_type: Optional zone type for context.
        context: Optional additional context dict.
        visual_context: Optional boat-specific context from BoatDNA (includes expert knowledge).

    Returns:
        German-language prompt string requesting JSON output.
    """
    class_desc, class_is_fallback = resolve_boat_class_context(boat_class, BOAT_CLASS_CONTEXT)
    fallback_notice = CLASS_FALLBACK_NOTICE if class_is_fallback else ""

    # Nutzerfreitext darf NICHT roh in den Prompt (Prompt-Injection, SEC-3/B-6).
    zone_note = build_zone_note(zone_type)

    visual_context_section = ""
    if visual_context:
        visual_context_section = f"\n\n{visual_context}\n"

    return f"""Du bist ein erfahrener Material-Experte im Yachtbau mit umfassendem Wissen ueber maritime Werkstoffe, deren Alterungsverhalten und Qualitaetsmerkmale. Analysiere dieses Bild.{visual_context_section}

Bootsklasse: {class_desc}{fallback_notice}{zone_note}
{ASSESSABILITY_RULES}
Bewerte die folgenden Materialaspekte, soweit im Bild erkennbar:

1. **Materialidentifikation**: Welche Materialien sind sichtbar? (Holzart, Steinart, Ledertyp, Metall, Textil, Kunststoff)
2. **Materialzustand**: Alterungszeichen, Verschleiss, Verfaerbungen, Risse, Quellungen
3. **Oberflaechenqualitaet**: Politur, Mattigkeit, Gleichmaessigkeit, Schutzschicht-Zustand
4. **Materialharmonie**: Passen die Materialien zusammen? Farbharmonie, Stilkonsistenz, Uebergaenge zwischen Materialien

WICHTIG: Wenn etwas nicht erkennbar ist, sage das explizit mit "nicht beurteilbar". Identifiziere Materialien nur, wenn du dir hinreichend sicher bist. Verwechsle nicht Echtholz mit Furnier oder Laminat — wenn unklar, sage es.

Antworte ausschliesslich mit einem JSON-Objekt (kein zusaetzlicher Text):

{{
    "material_score": <float 0-100 oder null>,
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
