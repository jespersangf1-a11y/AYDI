"""Build quality and craftsmanship assessment prompt."""

from app.services.visual.prompt_context import (
    ASSESSABILITY_RULES,
    CLASS_FALLBACK_NOTICE,
    build_zone_note,
    resolve_boat_class_context,
)

# Alle 13 Bootsklassen aus BoatClass. Ohne eigenen Eintrag wuerde eine Klasse
# still gegen den Fahrtensegler-Massstab bewertet (B-3).
BOAT_CLASS_CONTEXT = {
    "small_sail": "Kleine Segelyacht (8-12m). Funktionale Verarbeitung wird erwartet. Pragmatische Loesungen sind akzeptabel, solange sie sauber ausgefuehrt sind.",
    "cruising_sail": "Fahrtensegelyacht (12-18m). Gute handwerkliche Qualitaet erwartet. Saubere Fugen, solide Beschlaege, ordentliche Polsterarbeit.",
    "racing_sail": "Regattayacht. Bewertungsmassstab ist die technische Ausfuehrung, nicht die Moebelqualitaet. Sichtlaminat, freiliegende Verstaerkungen und fehlende Verkleidung sind gewollt. Entscheidend sind saubere Laminatkanten, praezise Krafteinleitung an Beschlaegen und verklebte statt gebohrte Loesungen.",
    "daysailer": "Daysailer/Weekender. Wenig Ausbau, aber das Wenige muss sauber sein. Bewerte Cockpit-Detaillierung, Lukenpassungen, Beschlagmontage und Kantenverarbeitung. Fehlender Innenausbau ist kein Verarbeitungsmangel.",
    "motorsailer": "Motorsegler. Kritisch sind die grossen Deckssalon-Verglasungen: Rahmenpassung, Dichtungsbild, Korrosionsspuren. Innen wird solide Fahrtenqualitaet erwartet, keine Superyacht-Praezision.",
    "catamaran_sail": "Segel-Katamaran. Leichtbau-Innenausbau (Sandwichplatten, Schaumkerne) ist bauartbedingt normal und kein Sparsignal. Bewerte Kantenabschluesse, Plattenstoesse und vor allem die Verarbeitung an Beschlagsdurchbruechen und Kernanbindungen.",
    "catamaran_motor": "Motor-Katamaran. Grosse Flaechen zeigen Verarbeitungsfehler deutlich: Plattenstoesse, Fugenverlauf ueber lange Strecken, Fensterbaender. Bewerte Gleichmaessigkeit ueber die Flaeche, nicht nur Detailpunkte.",
    "small_motor": "Kleine Motoryacht (unter 12m). Serienverarbeitung erwartet. Kunststoffteile, sichtbare Schraubverbindungen und einfache Polster sind akzeptabel, solange Passung und Ausrichtung stimmen.",
    "large_motor": "Grosse Motoryacht (18-30m). Hohe Verarbeitungsqualitaet erwartet. Praezise Spaltmasse, hochwertige Oberflaechen, professionelle Detailloesungen.",
    "sport_cruiser": "Sport-Cruiser. Schwerpunkt auf Aussenbereich: Polsternaehte, Gelcoat-Hochglanz, Edelstahlmontage, Einstiegskanten. Bewerte Abriebspuren an Griff- und Trittflaechen und die Passung grossflaechiger Klappen und Luken.",
    "trawler": "Trawler/Verdraenger. Massstab ist seegehende Soliditaet vor Feinheit: sichere Handlaeufe, sicher schliessende Schranktueren, verschraubte statt geklebte Verbindungen. Robuste, etwas kraeftigere Ausfuehrung ist ein Vorteil, kein Mangel.",
    "explorer": "Explorer/Expeditionsyacht. Gebrauchs- und Werkstattspuren sind normal. Bewerte Schweissnaehte, Korrosionsschutz an Kanten, Wartungszugaenge und die Sicherung von Ausruestung. Ausfuehrungsqualitaet an Struktur und Technik wiegt schwerer als Sichtflaechen.",
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
    "racing_sail": """
QUALITAETSSTANDARD fuer Regattayacht:
- Sichtlaminat ist die Oberflaeche: gleichmaessiger Faserverlauf, keine Lufteinschluesse, saubere Abrisskanten
- Krafteinleitung: Verstaerkungen an Winschen/Puetting/Mastfuss sauber auflaminiert, keine Risse im Harz
- Spaltmasse Innenausbau: nachrangig, da Ausbau minimal — bewerte stattdessen die Verklebungen
- Hardware: verklebt oder mit Gegenplatte verschraubt, kein blankes Bohren ins Sandwich
- Kein Furnier, keine Polsterarbeit erwartet — Fehlen ist kein Mangel
""",
    "daysailer": """
QUALITAETSSTANDARD fuer Daysailer/Weekender:
- Spaltmasse: 2-3mm akzeptabel, Schwerpunkt liegt auf Aussenflaechen
- Gelcoat/Lack: aussen gleichmaessig, UV-Schaeden an Kanten beachten
- Luken und Klappen: buendig, dicht, leichtgaengig
- Hardware: sauber ausgerichtet, korrosionsfrei, mit Gegenplatte
- Innenausbau: minimal — bewerten, was da ist, nicht was fehlt
- Polster: abwaschbar, gerade Naehte, keine offenen Kanten
""",
    "motorsailer": """
QUALITAETSSTANDARD fuer Motorsegler:
- Spaltmasse: max 1-2mm im Deckssalon, 2-3mm im Unterdeck akzeptabel
- Verglasung: Rahmenpassung gleichmaessig, Dichtung ohne Risse, keine Korrosionsfahnen
- Innensteuerstand: saubere Einbauten, verdeckte Kabelfuehrung
- Hardware: seewasserfest, buendiger Einbau wo moeglich
- Interieur: Massivholzkanten, strapazierfaehige Bezuege
- Elektrik: verzinntes Kupfer, beschriftet
""",
    "catamaran_sail": """
QUALITAETSSTANDARD fuer Segel-Katamaran:
- Spaltmasse: max 2mm, ueber lange Plattenstoesse gleichmaessig
- Leichtbauplatten: saubere Kantenabschluesse, keine offenen Kernkanten
- Durchbrueche/Beschlaege: Kern ausgeschnitten und versiegelt, keine offenen Sandwichkanten
- Gelcoat: glatt, keine sichtbaren Fehler aus 1m Abstand
- Interieur: Leichtbau ist bauartbedingt, kein Sparsignal
- Polster: gerade Naehte, Muster fluchten
""",
    "catamaran_motor": """
QUALITAETSSTANDARD fuer Motor-Katamaran:
- Spaltmasse: max 1-2mm, ueber die gesamte Salonbreite gleichmaessig
- Grossflaechen: keine Wellen, keine sichtbaren Plattenstoesse im Streiflicht
- Fensterbaender: gleichmaessige Fuge, saubere Dichtungsraupe
- Hardware: buendiger Einbau, praezise Ausrichtung
- Aussenpolster: witterungsfest, saubere Kantenverarbeitung
- Elektrik: verzinntes Kupfer, vollstaendig beschriftet
""",
    "small_motor": """
QUALITAETSSTANDARD fuer kleine Motoryacht (unter 12m):
- Spaltmasse: 2-3mm akzeptabel
- Gelcoat: leichte Orangenhaut akzeptabel, keine Laeufer
- Hardware: Serienausstattung, gleichmaessige Ausrichtung, korrosionsfrei
- Kunststoffteile und sichtbare Schrauben akzeptabel, wenn sauber gesetzt
- Interieur: Furnier oder Laminatplatte Standard
- Polster: gerade Naehte, Vinyl ohne Risse an Kanten
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
    "sport_cruiser": """
QUALITAETSSTANDARD fuer Sport-Cruiser:
- Spaltmasse: max 1-2mm an Sichtkanten
- Gelcoat/Lack: Hochglanz, gleichmaessig, keine Politurschleier
- Edelstahl: poliert, kein Teestaining an Reling und Handlaeufen
- Grossklappen (Garage, Sonnenliege): gleichmaessige Fuge, saubere Scharnierarbeit
- Aussenpolster: exakte Naehte, UV-festes Garn, keine offenen Kanten
- Trittflaechen: Abriebspuren bewerten, aber altersgerecht einordnen
""",
    "trawler": """
QUALITAETSSTANDARD fuer Trawler/Verdraenger:
- Spaltmasse: max 2mm, gleichmaessig; kraeftige Ausfuehrung ist erwuenscht
- Handlaeufe und Griffe: fest verschraubt, durchgehend erreichbar
- Schranktueren/Klappen: sicher schliessende Verschluesse (seegehend), kein blosses Magnetschloss
- Oberflaechen: robust und reparierbar wichtiger als Hochglanz
- Metallarbeit (Stahl/Alu): saubere Schweissnaehte, vollstaendiger Korrosionsschutz an Kanten
- Elektrik: verzinnt, beschriftet, zugaenglich
""",
    "explorer": """
QUALITAETSSTANDARD fuer Explorer/Expeditionsyacht:
- Struktur vor Sichtflaeche: Schweissnaehte gleichmaessig, keine Einbrandkerben, keine Rostfahnen
- Korrosionsschutz: vollstaendig an Kanten, Durchbruechen und Schweissnahtbereichen
- Wartungszugaenge: vorhanden, ausreichend gross, sauber ausgefuehrt
- Ausruestungssicherung: Kraene, Tender, Vorraete fest gelascht, definierte Anschlagpunkte
- Innenausbau: solide und reparierbar, Gebrauchsspuren an Arbeitsflaechen sind normal
- Isolierung: durchgehend, keine Kaeltebruecken/Kondensspuren an Spanten
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
    visual_context: str | None = None,
) -> str:
    """Generate the build quality assessment prompt for Claude vision API.

    Args:
        boat_class: One of the 13 BoatClass values (e.g. 'cruising_sail', 'trawler').
        zone_type: Optional zone type for context.
        context: Optional additional context dict.
        visual_context: Optional boat-specific context from BoatDNA (includes expert knowledge).

    Returns:
        German-language prompt string requesting JSON output.
    """
    class_desc, class_is_fallback = resolve_boat_class_context(boat_class, BOAT_CLASS_CONTEXT)
    quality_standard, _ = resolve_boat_class_context(boat_class, QUALITY_STANDARDS_BY_CLASS)
    fallback_notice = CLASS_FALLBACK_NOTICE if class_is_fallback else ""

    # Nutzerfreitext darf NICHT roh in den Prompt (Prompt-Injection, SEC-3/B-6).
    zone_note = build_zone_note(zone_type)

    visual_context_section = ""
    if visual_context:
        visual_context_section = f"\n\n{visual_context}\n"

    return f"""Du bist ein erfahrener Qualitaetspruefer im Yachtbau mit Spezialisierung auf Innenausbau und Verarbeitungsqualitaet. Analysiere dieses Bild.{visual_context_section}

Bootsklasse: {class_desc}{fallback_notice}{zone_note}

{quality_standard}
{ASSESSABILITY_RULES}
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
    "overall_quality_score": <float 0-100 oder null>,
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
    "confidence": "<hoch/mittel/niedrig>",
    "confidence_overall": "<hoch/mittel/niedrig>",
    "confidence_reasoning": "<string: warum diese Konfidenz>"
}}"""
