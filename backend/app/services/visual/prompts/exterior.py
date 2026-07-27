"""Exterior assessment prompt for yacht photos."""

# All 13 boat classes (not the legacy 4) so each gets exterior context matched
# to its idiom rather than silently defaulting to cruising_sail.
BOAT_CLASS_CONTEXT = {
    "small_sail": "Kleine Segelyacht (8-12m). Funktionale Linien, Segelleistung steht im Vordergrund. Saubere Ausfuehrung wichtiger als Designinnovation.",
    "cruising_sail": "Fahrtensegelyacht (12-18m). Elegante Segellinien, harmonisches Verhaeltnis von Aufbau zu Rumpf. Gute Balance zwischen Segeleigenschaften und Komfortvolumen.",
    "racing_sail": "Regattayacht. Kompromisslose Segelleistung, flaches Freibord, breites Heck, oft harte Kimmkante (Chine) und Doppelruder. Funktion vor Zierde.",
    "daysailer": "Daysailer/Weekender. Klare, elegante Linien, niedriges Profil, grosse Cockpitflaeche, minimaler Aufbau.",
    "motorsailer": "Motorsailer. Kraeftiger Aufbau/Deckssalon, hohes Freibord, kompromissbetont zwischen Motor- und Segelnutzung.",
    "catamaran_sail": "Segel-Katamaran. Zwei schlanke Ruempfe, breite Brueckendeck-Struktur; Volumen-vs-Performance-Balance zeigt sich an Bugform und Steuerstand.",
    "catamaran_motor": "Motor-Katamaran. Voluminoese Brueckenstruktur, oft Flybridge, Fokus auf Raum und Stabilitaet.",
    "small_motor": "Kleine Motoryacht. Kompakte, funktionale Proportionen, Sportboot- oder Cabin-Charakter.",
    "large_motor": "Grosse Motoryacht (18-30m). Repraesentatives Erscheinungsbild. Ausgewogene Proportionen, elegante Linien, hochwertiger Oberflaecheneindruck.",
    "sport_cruiser": "Sport-Cruiser. Dynamische, keilfoermige Silhouette, tiefe Fensterbaender, sportlich-flaches Profil.",
    "trawler": "Trawler/Verdraenger. Hoher trockener Bug, kastiges Deckshaus/Steuerhaus, robuste seegehende Anmutung; oft Portugiesische Bruecke.",
    "explorer": "Explorer/Expedition. Robuste, versorger-inspirierte Linien, erhoehtes Steuerhaus, sichtbare Ausruestung/Krane, funktionale Wuchtigkeit.",
    "superyacht": "Superyacht (30m+). Ikonisches Design. Einzigartige Designsprache, makellose Ausfuehrung, unverwechselbare Silhouette.",
}


def get_exterior_assessment_prompt(
    boat_class: str,
    zone_type: str | None = None,
    context: dict | None = None,
    visual_context: str | None = None,
) -> str:
    """Generate the exterior assessment prompt for Claude vision API.

    Args:
        boat_class: One of small_sail, cruising_sail, large_motor, superyacht.
        zone_type: Optional zone type for context.
        context: Optional additional context dict.
        visual_context: Optional boat-specific context from BoatDNA (includes expert knowledge).

    Returns:
        German-language prompt string requesting JSON output.
    """
    class_desc = BOAT_CLASS_CONTEXT.get(boat_class, BOAT_CLASS_CONTEXT["cruising_sail"])

    extra = ""
    if context:
        if "length_m" in context:
            extra += f"\nBootslaenge: {context['length_m']}m."

    visual_context_section = ""
    if visual_context:
        visual_context_section = f"\n\n{visual_context}\n"

    return f"""Du bist ein erfahrener Yachtdesigner mit besonderem Augenmerk auf Exterieur-Design und Proportionslehre. Du erkennst gute Linien, harmonische Verhaeltnisse und handwerkliche Qualitaet auf den ersten Blick. Analysiere dieses Bild.{visual_context_section}

Bootsklasse: {class_desc}{extra}

Bewerte folgende Aspekte des Exterieurs, soweit im Bild erkennbar:

1. **Linienharmonie**: Rumpflinien, Aufbaulinien, Fensterband, Uebergaenge
2. **Proportionen**: Verhaeltnis Aufbau/Rumpf, Bug/Heck-Balance, Fenstergrösse zu Wandflaeche
3. **Oberflaechenqualitaet**: Lack/Gelcoat-Zustand, Reflexionen, sichtbare Maengel
4. **Hardware**: Relingqualitaet, Beschlaege, Fender, Ankeranlage
5. **Markenkonsistenz**: Designsprache, Wiedererkennbarkeit, Stilsicherheit
6. **Epochen-/Stil-Einordnung**: grobe Bauepoche und Stilrichtung anhand sichtbarer Designsprache-Cues

Designsprache-Cues (NUR verwenden, wenn im Bild eindeutig erkennbar — sonst "nicht beurteilbar"; niemals raten):
- Bug: geneigt/ueberhaengend -> eher aelter (bis ~2000er); senkrecht (plumb) -> 2010er+; Scow/breiter Bugradius -> 2020er-Regatta.
- Kimm & Ruder (Segel): harte Kante (Chine) + Doppelruder -> Volumen-Aera 2010er+; runde Kimm + Einzelruder -> klassischer.
- Heck: Konterheck/geschlossen -> klassisch; offener Spiegel mit Badeplattform -> modern.
- Motoryacht-Silhouette: Fensterband-Grafik + Bugform (geneigt/plumb/keilfoermig) verweisen auf die Werft-Schule (z.B. keilfoermig-scharf -> Sport/Performance).

WICHTIG: Wenn etwas nicht erkennbar ist, sage das explizit mit "nicht beurteilbar". Bewerte Wetter- und Lichtverhaeltnisse im Foto mit ein — ein Bild bei schlechtem Licht erlaubt weniger Detailbewertung.

Antworte ausschliesslich mit einem JSON-Objekt (kein zusaetzlicher Text):

{{
    "exterior_score": <float 0-100>,
    "assessable": <bool>,
    "line_harmony": {{
        "hull_lines": "<fliessend/harmonisch/unruhig/nicht beurteilbar>",
        "superstructure": "<integriert/akzeptabel/aufgesetzt/nicht beurteilbar>",
        "transitions": "<nahtlos/sauber/abrupt/nicht beurteilbar>",
        "assessment": "<string>"
    }},
    "proportions": {{
        "superstructure_ratio": "<ausgewogen/etwas hoch/zu massig/nicht beurteilbar>",
        "bow_stern_balance": "<harmonisch/buglastig/hecklastig/nicht beurteilbar>",
        "window_ratio": "<elegant/angemessen/zu klein/zu gross/nicht beurteilbar>",
        "assessment": "<string>"
    }},
    "surface_quality": {{
        "paint_gelcoat": "<makellos/gut/Gebrauchsspuren/beschaedigt/nicht beurteilbar>",
        "reflections": "<spiegelnd/gut/matt/stumpf/nicht beurteilbar>",
        "defects_visible": ["<string>", ...],
        "assessment": "<string>"
    }},
    "hardware": {{
        "railing_quality": "<hochwertig/solide/einfach/mangelhaft/nicht beurteilbar>",
        "fittings": "<premium/gut/funktional/billig/nicht beurteilbar>",
        "observations": ["<string>", ...]
    }},
    "design_language": {{
        "era_estimate": "<z.B. '1980er', '1990-2005', '2010er+', '2020er', 'nicht beurteilbar'>",
        "style_tags": ["<z.B. 'klassisch','plumb-bow','volumen-cruiser','gin-palace','quiet-luxury','downeast'>", ...],
        "brand_cues": ["<sichtbare markentypische Merkmale, sonst leer>", ...],
        "assessment": "<string>",
        "confidence": "<hoch/mittel/niedrig>"
    }},
    "findings": [
        {{
            "aspect": "<string>",
            "observation": "<string>",
            "rating": "<positiv/neutral/negativ>",
            "suggestion": "<string oder null>"
        }}
    ],
    "confidence": "<hoch/mittel/niedrig>",
    "cannot_assess": ["<string>", ...]
}}"""
