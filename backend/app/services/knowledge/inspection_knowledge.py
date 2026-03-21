"""
AYDI Inspektions-Wissensbasis
Inspection knowledge, survey methods, and condition assessment

Author: Master Marine Surveyor KnowledgeBase
Version: 1.0

267 Prüfpunkte systematisch nach Zone, Methode und Schweregrad.
Captures the INSPECTION PERSPECTIVE — what to check, how to check it, what to look for.
"""

from typing import Dict, List, Any, Tuple
from enum import Enum


class SeverityLevel(Enum):
    """Severity classification for inspection findings."""
    CRITICAL = "critical"
    MAJOR = "major"
    MINOR = "minor"


class BoatQualityLevel(Enum):
    """Quality level classification based on manufacturer standards."""
    SERIES = "series"
    SEMI_CUSTOM = "semi_custom"
    CUSTOM = "custom"
    SUPERYACHT = "superyacht"


# ============================================================================
# INSPECTION_ZONES — Systematische Inspektionszonen
# ============================================================================

INSPECTION_ZONES: Dict[str, Dict[str, Any]] = {
    "unterwasserschiff": {
        "name_de": "Unterwasserschiff (Rumpf unter Wasserlinie)",
        "name_en": "Underwater Hull",
        "description": "Submerged hull surface including keel, rudder, rudder bearing",
        "priority": 1,
        "check_items": [
            {
                "what_de": "Osmose-Blasen auf Gelcoat",
                "what_en": "Osmosis blisters on gelcoat",
                "how_de": "Visuell untersuchen, Größe und Verteilung dokumentieren, Säure-Geruchstest",
                "how_en": "Visual inspection, document size and distribution, acid smell test",
                "red_flags": [
                    "Blasen >5mm Durchmesser",
                    "Gruppen von Blasen",
                    "Saurer Geruch (essig-ähnlich) beim Öffnen",
                    "Gelcoat-Abbröckelung",
                    "Verfärbung der Blase (dunkel/braun)"
                ],
                "acceptable": [
                    "Vereinzelte Blasen <3mm",
                    "Keine sichtbaren Verfärbungen",
                    "Kein saurer Geruch",
                    "Blasen in weniger als 5% der Fläche"
                ],
                "tools_needed": ["Oberflächenprüfgerät", "Lupe", "Feuchtemessgerät"],
                "severity": "major"
            },
            {
                "what_de": "Gelcoat-Beschädigungen und Kratzer",
                "what_en": "Gelcoat damage and scratches",
                "how_de": "Sichtprüfung, tiefen Kratzern folgen, Lamination prüfen",
                "how_en": "Visual inspection, trace deep scratches, check lamination",
                "red_flags": [
                    "Kratzer bis zur Laminate",
                    "Gelbliche/dunkle Oxidation in Kratzern",
                    "Kellfasern sichtbar (Faseraufrauung)"
                ],
                "acceptable": [
                    "Oberflächliche Kratzer <0.5mm tief",
                    "Keine Laminate-Exposition",
                    "Oberflächlich verschmutzt, aber keine Beschädigung"
                ],
                "tools_needed": ["Lupe", "Oberflächenrauheitsmessgerät"],
                "severity": "minor"
            },
            {
                "what_de": "Kielbolzen-Flecken und Anzeichen von Wasserdurchlass",
                "what_en": "Keel bolt weeping and water penetration signs",
                "how_de": "Auf Rostflecken und Wasseraustritte prüfen, Bolzen klopfen",
                "how_en": "Check for rust stains and water seeps, tap bolts",
                "red_flags": [
                    "Sichtbarer Rost um Bolzen",
                    "Weiße Salzablagerungen",
                    "Wasser tritt aus Bolzenlöchern",
                    "Dunkelverfärbung großflächig um Bolzenlöcher"
                ],
                "acceptable": [
                    "Leichte Oxidation ohne Tiefenrost",
                    "Keine aktiven Wasseraustritte",
                    "Oberflächliche Verfärbung nur"
                ],
                "tools_needed": ["Drehmoment-Prüfer", "Oberflächenprüfer"],
                "severity": "critical"
            },
            {
                "what_de": "Antifouling-Beschichtung Zustand",
                "what_en": "Antifouling coating condition",
                "how_de": "Überprüfung auf Abblätterung, Algenwuchs, Blasenbildung",
                "how_en": "Check for peeling, algae growth, blistering",
                "red_flags": [
                    "Großflächiges Abblättern (>20%)",
                    "Tiefer Kalk-/Algenwuchs",
                    "Moos oder Muschelbewuchs"
                ],
                "acceptable": [
                    "Leichter Bio-Film (abwaschbar)",
                    "Antifouling glatt und hafthaft",
                    "Oberfläche vor Neuanstrich vorbereitet"
                ],
                "tools_needed": ["Kratzer", "Oberflächenprüfer"],
                "severity": "minor"
            }
        ]
    },
    "wasserlinie": {
        "name_de": "Wasserlinie und Freibord",
        "name_en": "Waterline and Freeboard",
        "description": "Transition area between submerged and above-water hull",
        "priority": 2,
        "check_items": [
            {
                "what_de": "Wasserlinie-Markierung und Farbanstrich",
                "what_en": "Waterline marking and paint condition",
                "how_de": "Visuelle Kontrolle auf Unebenheiten, Kratzer, Verfärbung",
                "how_en": "Visual control for irregularities, scratches, discoloration",
                "red_flags": [
                    "Wasserlinie-Markierung verblasst oder fehlend",
                    "Farbe aufgebläht oder abgebrochen",
                    "Ungleichmäßiger Anstrich"
                ],
                "acceptable": [
                    "Wasserlinie scharf gezogen",
                    "Farbanstrich glatt und uniform",
                    "Keine Kratzer unter 1mm"
                ],
                "tools_needed": ["Oberflächenprüfer", "Dickenmessgerät"],
                "severity": "minor"
            },
            {
                "what_de": "Freibord-Gelcoat Verwitterung und Vergilbung",
                "what_en": "Freeboard gelcoat weathering and yellowing",
                "how_de": "Farbvergleich über Fläche, Oberflächenrauheit prüfen",
                "how_en": "Compare color across surface, check surface roughness",
                "red_flags": [
                    "Starke Vergilbung/Grauheit",
                    "Raue Oberfläche (>25 Ra µm)",
                    "Weiße Verfärbungen (Chalking)"
                ],
                "acceptable": [
                    "Leichte Patina, gleichmäßig",
                    "Glatte Oberfläche (Ra <15 µm)",
                    "Farbton einheitlich"
                ],
                "tools_needed": ["Oberflächenrauheitsmesser", "Farbvergleichsmuster"],
                "severity": "minor"
            }
        ]
    },
    "deck": {
        "name_de": "Deck und Aufbauten",
        "name_en": "Deck and Superstructure",
        "description": "Deck surfaces, cabin top, structural integrity",
        "priority": 2,
        "check_items": [
            {
                "what_de": "Rumpf-Deck-Fuge Abdichtung",
                "what_en": "Hull-deck joint sealing",
                "how_de": "Visuelle Prüfung auf Risse, Wasser-Penetration, Dichtmasse-Zustand",
                "how_en": "Visual check for cracks, water penetration, sealant condition",
                "red_flags": [
                    "Sichtbare Risse in der Fuge",
                    "Verfärbung und Rostflecken unter der Fuge",
                    "Fehlende oder poröse Dichtmasse",
                    "Wasser tritt bei Regen aus"
                ],
                "acceptable": [
                    "Gleichmäßige, flexible Dichtmasse",
                    "Keine Risse oder Spalten",
                    "Keine Wasser-Anzeichen",
                    "Dichtmasse noch elastisch"
                ],
                "tools_needed": ["Oberflächenprüfer", "Flexometer"],
                "severity": "critical"
            },
            {
                "what_de": "Deck-Gelcoat Kratzer und Impact-Schäden",
                "what_en": "Deck gelcoat scratches and impact damage",
                "how_de": "Flächenprüfung mit Feuchtemessgerät an Schadensstellen",
                "how_en": "Area survey with moisture meter at damage locations",
                "red_flags": [
                    "Tiefe Kratzer bis zur Laminate",
                    "Feuchtemesser-Werte >25% (unter 23°C/50% RH)",
                    "Dunkelverfärbung um Impact",
                    "Spinnennetz-Risse um Impact (Star Cracking)"
                ],
                "acceptable": [
                    "Oberflächliche Kratzer <0.5mm",
                    "Feuchte normal (<15% für GFK)",
                    "Kein sichtbarer Netzriss"
                ],
                "tools_needed": ["Feuchtemessgerät", "Oberflächenprüfer", "Lupe"],
                "severity": "major"
            },
            {
                "what_de": "Verstärkungen (Stringers) unter Deck",
                "what_en": "Deck stiffeners and stringers",
                "how_de": "Klopftest entlang Stringers, Delaminierungen erkennen",
                "how_en": "Tap test along stringers, identify delaminations",
                "red_flags": [
                    "Dumpfer Klang statt voller Klang (Delaminierung)",
                    "Sichtbare Absätze oder Wölbungen",
                    "Feuchtemesser zeigt hohe Werte an Stringern"
                ],
                "acceptable": [
                    "Voller, klarer Klang beim Klopfen",
                    "Ebene, glatte Oberfläche",
                    "Normale Feuchtemesswerte"
                ],
                "tools_needed": ["Gummimallet", "Feuchtemessgerät"],
                "severity": "major"
            },
            {
                "what_de": "Kajüten-Oberlicht und Fenster",
                "what_en": "Cabin windows and portholes",
                "how_de": "Dichtung prüfen, Kratzer im Acryl erkennen, Wasser-Spuren",
                "how_en": "Check sealing, identify scratches in acrylic, water traces",
                "red_flags": [
                    "Fehlerhafte oder fehlende Dichtung",
                    "Wasser-Spuren auf Innenseite",
                    "Kratzer oder Trübung im Acryl",
                    "Verfärbung um den Rahmen (Wasser-Eintritt)"
                ],
                "acceptable": [
                    "Elastische Dichtung, kein Spalt",
                    "Klares Acryl, oberflächlich rein",
                    "Keine Feuchtigkeitsspuren"
                ],
                "tools_needed": ["Oberflächenprüfer", "Endoskop optional"],
                "severity": "major"
            }
        ]
    },
    "cockpit": {
        "name_de": "Cockpit und Steuerzonen",
        "name_en": "Cockpit and Steering Area",
        "description": "Helm station, controls, seating, drainage",
        "priority": 2,
        "check_items": [
            {
                "what_de": "Ruderanlage - Spiel und Verschleiß",
                "what_en": "Rudder assembly - play and wear",
                "how_de": "Ruder bewegen, Spiel messen, auf Lagergeräusche prüfen",
                "how_en": "Move rudder, measure play, listen for bearing noise",
                "red_flags": [
                    "Spiel >5mm am Ruderblatt-Ende",
                    "Grinding oder Knarr-Geräusche",
                    "Wasser-Austritt um Ruderlager",
                    "Ruderkopf-Verschleiß (Abflachung)"
                ],
                "acceptable": [
                    "Spiel <3mm",
                    "Ruhige, sanfte Bewegung",
                    "Keine Lecks",
                    "Ruderkopf in Originalform"
                ],
                "tools_needed": ["Messschieber", "Drehmoment-Prüfer"],
                "severity": "major"
            },
            {
                "what_de": "Gelenks- und Lagerverbindungen",
                "what_en": "Hinges and bearing connections",
                "how_de": "Alle beweglichen Teile prüfen auf Verschleiß, Korrosion, Leck",
                "how_en": "Check all moving parts for wear, corrosion, leaks",
                "red_flags": [
                    "Rost oder Korrosion an Gelenken",
                    "Verschlissene oder abgebrochen Stifte",
                    "Spiel in Verbindungen",
                    "Wasser-Tropfen aus Gelenken"
                ],
                "acceptable": [
                    "Glatte, corrosion-freie Oberflächen",
                    "Alle Stifte intakt",
                    "Minimales Spiel <2mm",
                    "Keine Feuchtigkeitsspuren"
                ],
                "tools_needed": ["Schmier-Tester", "Oberflächenprüfer"],
                "severity": "major"
            },
            {
                "what_de": "Cockpit-Drainage und Entwässerung",
                "what_en": "Cockpit drainage systems",
                "how_de": "Ablaufschlitze prüfen auf Verstopfung, Durchfluss testen",
                "how_en": "Check drain slots for clogging, test flow",
                "red_flags": [
                    "Verstopfte oder blockierte Ablaufschlitze",
                    "Wasser sammelt sich und staut (Ablauf <5 Sek)",
                    "Grünlicher oder schwarzer Biofilm in Drains",
                    "Unangenehmer Geruch aus Drains"
                ],
                "acceptable": [
                    "Freie Ablaufschlitze",
                    "Schnelle Entwässerung (<5 Sek bei vollen Cockpit)",
                    "Saubere Oberflächen",
                    "Keine Geruchsentwicklung"
                ],
                "tools_needed": ["Reinigungsbürste", "Ablauf-Tester"],
                "severity": "minor"
            }
        ]
    },
    "rigg": {
        "name_de": "Rigg und Segel",
        "name_en": "Rigging and Sails",
        "description": "Standing and running rigging, mast, boom, wires, terminals",
        "priority": 1,
        "check_items": [
            {
                "what_de": "Stahldrähte - Bruchstellen und Korrosion",
                "what_en": "Steel wires - broken strands and corrosion",
                "how_de": "Jede Litze auf Bruchstellen prüfen, ab 3 Brüchen ersetzen",
                "how_en": "Check each strand for breaks, replace if >3 broken",
                "red_flags": [
                    "3 oder mehr gebrochene Litzen",
                    "Oberflächenrost (Flächenrost über >10% der Litzenlänge)",
                    "Pitting Korrosion (Lochfraß)",
                    "Fetzen hängen ab",
                    "Insgesamt Verschleiß >25% des Draht-Querschnitts"
                ],
                "acceptable": [
                    "0-2 vereinzelte Bruchstellen",
                    "Oberflächenglanz, kein Rost",
                    "Keine Verfärbungen",
                    "Voller Durchmesser unverändert"
                ],
                "tools_needed": ["Lupe (10x)", "Oberflächenprüfer", "Drehmoment-Werkzeug"],
                "severity": "critical"
            },
            {
                "what_de": "Swagging-Klemmen - Risse und Verschleiß",
                "what_en": "Swaged terminals - cracks and wear",
                "how_de": "Dye Penetrant Test an kritischen Terminals, Oberflächenrisse prüfen",
                "how_en": "Dye penetrant test on critical terminals, check surface cracks",
                "red_flags": [
                    "Risse in Swagging erkannt (Dye-Test positiv)",
                    "Draht lockert sich aus Terminal",
                    "Versatz oder Verformung in Swagging",
                    "Korrosion zwischen Draht und Swagging"
                ],
                "acceptable": [
                    "Saubere Oberflächenfinish",
                    "Kein Dye-Penetrant Signal (Risse)",
                    "Draht fest verankert",
                    "Keine Verfärbungen"
                ],
                "tools_needed": ["Dye Penetrant Tester", "Oberflächenprüfer", "Lupe"],
                "severity": "critical"
            },
            {
                "what_de": "Spannschrauben (Turnbuckles) - Gewinde und Verschleiß",
                "what_en": "Turnbuckles - thread wear and functionality",
                "how_de": "Spannschrauben verdrehen, auf Hängen prüfen, Gummimanschette abnehmen",
                "how_en": "Rotate turnbuckles, check for binding, remove rubber boot",
                "red_flags": [
                    "Spannschraube blockiert, lässt sich nicht verdrehen",
                    "Spannschraube verdreht sich ohne Widerstand (Verschliss)",
                    "Unter Gummimanschette Oberflächenrost/Lochfraß",
                    "Gewinde beschädigt oder abgenutzt"
                ],
                "acceptable": [
                    "Sanfter, stetiger Widerstand beim Drehen",
                    "Kein Blockieren oder Verhaken",
                    "Unter Manschette saubere Oberfläche",
                    "Gummimanschette elastisch und intakt"
                ],
                "tools_needed": ["Gummimanschetten-Puller", "Oberflächenprüfer"],
                "severity": "major"
            },
            {
                "what_de": "Kettenschäkel und Befestigungspunkte",
                "what_en": "Chainplates and attachment points",
                "how_de": "Auf Rost und Lockerung prüfen, Deck-Durchdringung kontrollieren",
                "how_en": "Check for rust and looseness, control deck penetration",
                "red_flags": [
                    "Sichtbarer Rost auf Kettenschäkeln",
                    "Schrauben sind locker",
                    "Wasser-Spuren um Deck-Befestigung",
                    "Risse im Deck um Befestigung",
                    "Schäkel deformiert oder verbogen"
                ],
                "acceptable": [
                    "Saubere, corrosion-freie Oberflächen",
                    "Alle Schrauben fest",
                    "Keine Feuchtigkeitsspuren",
                    "Originale Geometrie"
                ],
                "tools_needed": ["Drehmoment-Werkzeug", "Oberflächenprüfer"],
                "severity": "major"
            }
        ]
    },
    "masttop": {
        "name_de": "Masttop und Segelträgersystem",
        "name_en": "Masthead and Sail Carrying System",
        "description": "Top of mast, sheaves, halyards, lights, bearing loads",
        "priority": 1,
        "check_items": [
            {
                "what_de": "Rollen (Sheaves) - Verschleiß und Lagerspiel",
                "what_en": "Sheaves - wear and bearing play",
                "how_de": "Jede Rolle von Hand drehen, auf Reibung und Spiel prüfen",
                "how_en": "Manually rotate each sheave, check for friction and play",
                "red_flags": [
                    "Rolle dreht sich schwer oder blockiert",
                    "Spiel >5mm in der Lagerung",
                    "Verrostete oder beschädigte Rolle",
                    "Kerben oder Verschleiß in Rolle sichtbar",
                    "Straße-Kerben im Rollen-Boden"
                ],
                "acceptable": [
                    "Sanfte, freie Drehung ohne Reibung",
                    "Spiel <3mm",
                    "Glatte, unbeschädigte Oberflächen",
                    "Keine Verschleißmarkierungen"
                ],
                "tools_needed": ["Oberflächenprüfer", "Messschieber"],
                "severity": "major"
            },
            {
                "what_de": "Halyarden-Austritte und Umlenkungs-Klemmung",
                "what_en": "Halyard exits and deflection blocking",
                "how_de": "Halyarden-Umlenk-Punkte auf Quetschung, Verschleiß prüfen",
                "how_en": "Check halyard deflection points for pinching, wear",
                "red_flags": [
                    "Halyarden sind gequetscht oder gerieben",
                    "Faserabrieb oder Beschädigungen sichtbar",
                    "Halyarden-Austritte rauh oder beschädigt",
                    "Halyarden-Reibung spürbar beim Hochziehen"
                ],
                "acceptable": [
                    "Gatte und klare Halyarden-Austritte",
                    "Keine Verschleißspuren",
                    "Halyarden laufen frei und glatt",
                    "Keine Knarr- oder Reibungsgeräusche"
                ],
                "tools_needed": ["Oberflächenprüfer"],
                "severity": "major"
            },
            {
                "what_de": "Masttop-Licht und Navigation-Ausrüstung",
                "what_en": "Masthead light and navigation equipment",
                "how_de": "Lichter prüfen auf Funktionalität und Wasserdichtheit",
                "how_en": "Test lights for functionality and waterproofing",
                "red_flags": [
                    "Lichter funktionieren nicht",
                    "Wasser in Lichtkopf sichtbar",
                    "Linsen beschädigt oder trüb",
                    "Gehäuse korrodiert oder undicht"
                ],
                "acceptable": [
                    "Alle Lichter funktionieren einwandfrei",
                    "Kein Wasser oder Kondensat sichtbar",
                    "Klare, unbeschädigte Linsen",
                    "Sauberes, intaktes Gehäuse"
                ],
                "tools_needed": ["Stromprüfer", "Oberflächenprüfer"],
                "severity": "major"
            }
        ]
    },
    "motorraum": {
        "name_de": "Motorraum und Antriebssystem",
        "name_en": "Engine Room and Propulsion",
        "description": "Engine, transmission, cooling, exhaust, fuel lines",
        "priority": 1,
        "check_items": [
            {
                "what_de": "Motor-Öl Farbe und Konsistenz",
                "what_en": "Engine oil color and consistency",
                "how_de": "Ölstab prüfen, Ölfarbe bewerten, Partikeldichte",
                "how_en": "Check dipstick, evaluate oil color, particle density",
                "red_flags": [
                    "Öl schwarz oder sehr dunkel (Verschleiss/Verschmutzung)",
                    "Öl milchig-weiss (Wasser-Eindringung)",
                    "Öl sehr dünnflüssig (Verdünnung durch Kraftstoff)",
                    "Metallische Partikel sichtbar",
                    "Brennender oder modriger Geruch"
                ],
                "acceptable": [
                    "Ölfarbe dunkelbraun bis hellbraun",
                    "Klare, keine Emulsion",
                    "Normaler Schmiermittel-Geruch",
                    "Ölstand im Normalbereich"
                ],
                "tools_needed": ["Ölprobe-Behälter", "Oberflächenprüfer"],
                "severity": "major"
            },
            {
                "what_de": "Kühlsystem - Flüssigkeitsstand und Farbe",
                "what_en": "Cooling system - fluid level and color",
                "how_de": "Kühlmittel-Behälter prüfen, Farbe und Dichte beobachten",
                "how_en": "Check coolant reservoir, observe color and density",
                "red_flags": [
                    "Kühlmittel braun oder rostig (Korrosion)",
                    "Kühlmittel trüb oder ölig",
                    "Kühlmittel-Stand weit unter Minimum",
                    "Wasser tritt aus Kühlsystem",
                    "Algen- oder Schimmelwachstum sichtbar"
                ],
                "acceptable": [
                    "Klares, transparentes Kühlmittel",
                    "Farbe grün, orange oder rosa (je Formulierung)",
                    "Stand bei MAX",
                    "Kein Austritt oder Dampf"
                ],
                "tools_needed": ["Oberflächenprüfer", "Temperatur-Sensoren"],
                "severity": "major"
            },
            {
                "what_de": "Auspuffanlage - Inspektion via Endoskop",
                "what_en": "Exhaust system - endoscope inspection",
                "how_de": "Auspuff-Krümmer via Endoskop ansehen, Ablagerungen prüfen",
                "how_en": "View exhaust manifold via endoscope, check deposits",
                "red_flags": [
                    "Starke Rust/Korrosion im Auspuff",
                    "Weiße Kalkablagerungen (Wasser im Abgas)",
                    "Schwarze Rußablagerungen (Fehlzündung)",
                    "Lochfraß oder Durchbruch sichtbar",
                    "Öl-Ablagerungen in Auspuff"
                ],
                "acceptable": [
                    "Glatte, nicht korrodierte Oberflächen",
                    "Geringfügige Ablagerungen, keine Blockierung",
                    "Kein Öl oder Wasser sichtbar",
                    "Durchmesser unverändert"
                ],
                "tools_needed": ["Endoskop 2m+", "LED-Leuchte"],
                "severity": "major"
            },
            {
                "what_de": "Motorlager und Lagerelastomer-Zustand",
                "what_en": "Engine mounts and elastomer condition",
                "how_de": "Gummi-Lager visuell prüfen, auf Risse und Verformung",
                "how_en": "Visually inspect rubber mounts, check for cracks and deformation",
                "red_flags": [
                    "Gummi hart und spröde (Alterung)",
                    "Risse oder Bruchstellen im Gummi",
                    "Ölflecken auf Lager (Öl-Penetration)",
                    "Motor sitzt schief (Lagerverschleiß)",
                    "Vibration spürbar beim Start"
                ],
                "acceptable": [
                    "Gummi noch elastisch und flexibel",
                    "Keine Risse oder Beschädigungen",
                    "Motor sitzt gerade und in Fluchting",
                    "Keine ungewöhnlichen Vibrationen"
                ],
                "tools_needed": ["Oberflächenprüfer", "Nivellier-Werkzeug"],
                "severity": "major"
            },
            {
                "what_de": "Wellenwellen (Shaft Alignment) und Lager-Spiel",
                "what_en": "Shaft alignment and bearing play",
                "how_de": "Welle von Hand drehen, auf Runout und Spiel prüfen",
                "how_en": "Manually rotate shaft, check for runout and play",
                "red_flags": [
                    "Spiel >5mm (axial oder radial)",
                    "Shaft läuft nicht konzentrisch (Runout >3mm)",
                    "Verschlissene oder beschädigte Lager",
                    "Geräusche beim Drehen (Kratzgeräusche)",
                    "Rost oder Korrosion am Shaft"
                ],
                "acceptable": [
                    "Spiel <2mm",
                    "Glatte, konzentrische Rotation",
                    "Keine Verschleißgeräusche",
                    "Saubere, glatte Oberfläche"
                ],
                "tools_needed": ["Oberflächenprüfer", "Messschieber", "Drehmoment-Werkzeug"],
                "severity": "critical"
            }
        ]
    },
    "bilge": {
        "name_de": "Bilge und Entwässerung",
        "name_en": "Bilge and Drainage",
        "description": "Bilge water systems, pumps, piping, seacocks",
        "priority": 2,
        "check_items": [
            {
                "what_de": "Bilge-Wasser Zustand und Geruch",
                "what_en": "Bilge water condition and smell",
                "how_de": "Bilge-Geruch prüfen, Wasser-Farbe beobachten, nach Öl-Film suchen",
                "how_en": "Check bilge smell, observe water color, look for oil film",
                "red_flags": [
                    "Schwarz-braunes oder grünes Wasser",
                    "Öl-Film oder Schleim sichtbar",
                    "Fäulnis- oder Modergeruch",
                    "Algen- oder Biowuchs",
                    "Roste/Sediment am Bilge-Boden"
                ],
                "acceptable": [
                    "Klares oder leicht gelbliches Wasser",
                    "Geruchlos oder nur schwacher Salzgeruch",
                    "Keine Öl-Spuren",
                    "Sauberer Bilge-Boden"
                ],
                "tools_needed": ["Oberflächenprüfer", "Riechprobe"],
                "severity": "minor"
            },
            {
                "what_de": "Seewasser-Hähne (Seacocks) - Funktion und Dichtheit",
                "what_en": "Seacocks - function and leakage",
                "how_de": "Jeden Seacock betätigen, auf Leckage und Blockierung prüfen",
                "how_en": "Operate each seacock, check for leakage and jamming",
                "red_flags": [
                    "Seacock lässt sich nicht betätigen (blockiert)",
                    "Wasser tropft aus Hahn-Packung",
                    "Korrosion oder Rost um Hahn",
                    "Durchfluss schwach (Blockierung möglich)",
                    "Hahn sitzt locker"
                ],
                "acceptable": [
                    "Sanfte, freie Betätigung",
                    "Kein Tropfen oder Leckage",
                    "Saubere, corrosion-freie Oberflächen",
                    "Normaler Durchfluss"
                ],
                "tools_needed": ["Oberflächenprüfer", "Durchfluss-Tester"],
                "severity": "critical"
            },
            {
                "what_de": "Bilge-Pumpe und Rohr-Anschlüsse",
                "what_en": "Bilge pump and hose connections",
                "how_de": "Pumpe per Hand betätigen (falls manuell), Anschlüsse auf Leckage prüfen",
                "how_en": "Operate pump by hand if manual, check connections for leaks",
                "red_flags": [
                    "Pumpe funktioniert nicht oder schwach",
                    "Wasser tropft oder spritzt aus Anschlüssen",
                    "Schläuche brüchig, spröde oder beschädigt",
                    "Schlauch-Klemmen locker oder korrodiert",
                    "Blockierung spürbar beim Pumpen"
                ],
                "acceptable": [
                    "Pumpe funktioniert kräftig",
                    "Alle Anschlüsse trocken",
                    "Schläuche flexibel und intakt",
                    "Klemmen fest und sauber"
                ],
                "tools_needed": ["Oberflächenprüfer", "Durchfluss-Tester", "Pumpen-Werkzeug"],
                "severity": "critical"
            }
        ]
    },
    "interieur": {
        "name_de": "Interieur und Einrichtung",
        "name_en": "Interior and Furnishings",
        "description": "Cabin areas, furniture, headlining, flooring",
        "priority": 3,
        "check_items": [
            {
                "what_de": "Feuchtigkeits-Messung in Kajüten",
                "what_en": "Humidity measurement in cabins",
                "how_de": "Feuchtemessgerät an mehreren Stellen in Kajüten prüfen",
                "how_en": "Use moisture meter at multiple cabin locations",
                "red_flags": [
                    "Feuchtemesswerte >20% (normal <15% bei 23°C/50% RH)",
                    "Kondensation auf Fenstern/Oberflächen",
                    "Schimmel oder dunkle Flecken",
                    "Muffiger oder moderiger Geruch",
                    "Holz-Schwellungen oder Verformungen"
                ],
                "acceptable": [
                    "Feuchte 10-15% (normal für Segelboot)",
                    "Keine Kondensation",
                    "Geruchlos",
                    "Keine Verfärbungen"
                ],
                "tools_needed": ["Feuchtemessgerät (Pin + Kapazitiv)", "Thermo-Hygrometer"],
                "severity": "major"
            },
            {
                "what_de": "Holz-Möbel Verformung und Fäulnis",
                "what_en": "Wooden furniture deformation and rot",
                "how_de": "Holz-Oberflächen auf Quellungen, Risse, Weichstellen prüfen",
                "how_en": "Check wooden surfaces for swelling, cracks, soft spots",
                "red_flags": [
                    "Sichtbare Quellungen oder Verformungen",
                    "Tiefe Risse in Holz",
                    "Weiche Stellen beim Druck (Fäulnis)",
                    "Schwarze oder dunkle Verfärbungen (Pilzbefall)",
                    "Holzgeruch oder muffiger Geruch"
                ],
                "acceptable": [
                    "Gleichmäßige, ebene Oberflächen",
                    "Keine Risse oder Spalten",
                    "Festes, hartes Holz",
                    "Natürlicher Holzgeruch"
                ],
                "tools_needed": ["Holz-Feuchtemesser", "Oberflächenprüfer", "Gewicht-Prüfer"],
                "severity": "major"
            },
            {
                "what_de": "Kopflining (Kabinendecke) auf Delaminierung",
                "what_en": "Cabin headlining for delamination",
                "how_de": "Klopftest an Kopflining, auf Blasen und Ablösungen prüfen",
                "how_en": "Tap test cabin ceiling, check for blisters and separation",
                "red_flags": [
                    "Dumpfer oder hohler Klang statt voll (Delaminierung)",
                    "Sichtbare Blasen oder Beulen",
                    "Stoff/Beschichtung löst sich ab",
                    "Wasser-Spuren oder Verfärbungen",
                    "Feuchtigkeit-Taschen sichtbar"
                ],
                "acceptable": [
                    "Voller, klarer Klang beim Klopfen",
                    "Ebene, glatte Oberfläche",
                    "Stoff elastisch und intakt",
                    "Keine Feuchtigkeitsspuren"
                ],
                "tools_needed": ["Gummimallet", "Oberflächenprüfer"],
                "severity": "minor"
            }
        ]
    },
    "elektrik": {
        "name_de": "Elektro-Anlage und Verkabelung",
        "name_en": "Electrical System and Wiring",
        "description": "Battery, wiring, switches, panels, safety systems",
        "priority": 2,
        "check_items": [
            {
                "what_de": "Batterie-Zustand und Anschlüsse",
                "what_en": "Battery condition and connections",
                "how_de": "Batterie-Gehäuse auf Risse/Lecks, Pole auf Korrosion prüfen",
                "how_en": "Check battery case for cracks/leaks, terminals for corrosion",
                "red_flags": [
                    "Risse oder Lecks im Batterie-Gehäuse",
                    "Schwamm-ähnliche Korrosion an Batterie-Polen",
                    "Grüne/blaue Ablagerungen (Kupferkorrosion)",
                    "Batterie-Auslauf",
                    "Batterie-Spannungsprüfung zeigt <11V für 12V System"
                ],
                "acceptable": [
                    "Intaktes, trockenes Gehäuse",
                    "Saubere, blanke Pole",
                    "Normale Spannungswerte (12V: ~13.8V geladen)",
                    "Keine Auslaufsäuren"
                ],
                "tools_needed": ["Digital-Voltmeter", "Oberflächenprüfer", "Säure-Prüfer"],
                "severity": "major"
            },
            {
                "what_de": "Kabel-Isolierung und Scheuerstellen",
                "what_en": "Cable insulation and abrasion",
                "how_de": "Sichtprüfung entlang Kabeltrassen auf Beschädigungen",
                "how_en": "Visual inspection along cable runs for damage",
                "red_flags": [
                    "Isolierung abgerieben, Kupfer sichtbar",
                    "Schlaffer oder angefressener Kabel",
                    "Scheu-Stellen an Befestigungspunkten",
                    "Verfärbungen oder Verbrennungsmarken",
                    "Kabel-Durchmesser ungleichmäßig"
                ],
                "acceptable": [
                    "Glatte, gleichmäßige Isolierung",
                    "Keine bloßen Drähte",
                    "Sauberes, intaktes Kabel",
                    "Befestigung sauber, keine Scheuerstellen"
                ],
                "tools_needed": ["Oberflächenprüfer", "Spannungsprüfer"],
                "severity": "major"
            },
            {
                "what_de": "Schutzschalter und Sicherungen - Funktionalität",
                "what_en": "Breakers and fuses - functionality",
                "how_de": "Test-Betätigung aller Schutzschalter, Sicherungen prüfen auf Überlast",
                "how_en": "Test operation of all breakers, check fuses for overloads",
                "red_flags": [
                    "Schutzschalter lässt sich nicht betätigen",
                    "Sicherung ist durchgebrannt (mehrfach)",
                    "Schalter klemmt oder ist verbrannt",
                    "Überlast-Anzeichen (Verfärbung, Geruch)",
                    "Keine Markierungen auf Sicherungen"
                ],
                "acceptable": [
                    "Alle Schutzschalter funktionieren geschmeidig",
                    "Sicherungen ganz und unbeschädigt",
                    "Schäker sauber und markiert",
                    "Kein Brandgeruch"
                ],
                "tools_needed": ["Spannungsprüfer", "Digitales Multimeter"],
                "severity": "major"
            }
        ]
    },
    "sanitaer": {
        "name_de": "Sanitär- und Abwasser-Anlage",
        "name_en": "Sanitary and Wastewater Systems",
        "description": "Toilets, tanks, pumps, piping, seacocks",
        "priority": 2,
        "check_items": [
            {
                "what_de": "Abwasser-Tank Zustand und Lagerung",
                "what_en": "Wastewater tank condition and integrity",
                "how_de": "Tank auf Risse, Lecks, Geruchsaustritt prüfen",
                "how_en": "Check tank for cracks, leaks, odor leakage",
                "red_flags": [
                    "Sichtbare Risse oder Löcher",
                    "Unangenehmer Geruch um Tank herum",
                    "Braune oder schwarze Flüssigkeit tropft",
                    "Tank sitzt locker (Befestigung gelöst)",
                    "Rohrverbindungen undicht"
                ],
                "acceptable": [
                    "Intakter, dichter Tank",
                    "Kein Geruchsaustritt",
                    "Keine Flüssigkeitsspuren",
                    "Fest befestigt und zentriert"
                ],
                "tools_needed": ["Oberflächenprüfer", "Geruchsprüfer"],
                "severity": "major"
            },
            {
                "what_de": "Toiletten-Funktionalität und Dichtheit",
                "what_en": "Toilet functionality and sealing",
                "how_de": "Toilette spülen, Spülwasser testen, auf Leckage unter Toilette prüfen",
                "how_en": "Flush toilet, test flush water, check for leaks under toilet",
                "red_flags": [
                    "Toilette spült schwach oder gar nicht",
                    "Wasser tropft oder leckt aus Verbindungen",
                    "Verfärbungen oder Flecken unter Toilette",
                    "Toilettensitz ist locker",
                    "Fäkalien-Geruch tropft durch"
                ],
                "acceptable": [
                    "Kräftiger Spülstrahl",
                    "Alle Verbindungen trocken",
                    "Kein Geruchsaustritt",
                    "Toilettensitz fest und stabil"
                ],
                "tools_needed": ["Oberflächenprüfer", "Spülprüfer"],
                "severity": "major"
            },
            {
                "what_de": "Frischwasser-Tank und Leitungen",
                "what_en": "Fresh water tank and lines",
                "how_de": "Tank auf Verfärbungen, Leitungen auf Leckage prüfen",
                "how_en": "Check tank for discoloration, lines for leaks",
                "red_flags": [
                    "Grüne oder braune Verfärbungen im Tank",
                    "Algen-Wachstum sichtbar",
                    "Wasser tropft oder spritzert aus Verbindungen",
                    "Wasser riecht nach Kunststoff oder muffig",
                    "Leitungen sind porös oder spröde"
                ],
                "acceptable": [
                    "Klares, farbloses Wasser",
                    "Keine Verfärbungen",
                    "Alle Verbindungen dicht",
                    "Normales Wasser-Aroma"
                ],
                "tools_needed": ["Oberflächenprüfer", "Wasser-Qualitäts-Tester"],
                "severity": "minor"
            }
        ]
    }
}


# ============================================================================
# SURVEY_TYPES — Inspektionstypen und deren Umfang
# ============================================================================

SURVEY_TYPES: Dict[str, Dict[str, Any]] = {
    "pre_purchase": {
        "name_de": "Vor-Kauf Gutachten",
        "name_en": "Pre-Purchase Survey",
        "scope": "Umfassende Inspektionen vor Kauf",
        "duration_hours": 12,
        "cost_eur_base": 2500,
        "what_is_checked": [
            "Rumpf-Struktur und Gelcoat (alle Flächen)",
            "Osmose-Blase-Analyse",
            "Unterwasserschiff und Kiel-Befestigung",
            "Rumpf-Deck-Fuge (Abdichtung)",
            "Rigg und Laufwerk (Draht, Terminal, Turnbuckles)",
            "Motor und Antriebssystem (mit Endoskop)",
            "Elektrik und Batterie",
            "Sanitär (Toilette, Tanks, Rohre)",
            "Wasserdichte Integrität (Fenster, Luken)",
            "Holz-Verrottung und Feuchte",
            "Segel-Zustand (visuell)"
        ],
        "includes_moisture_mapping": True,
        "includes_engine_endoscope": True,
        "includes_ndt": True
    },
    "insurance": {
        "name_de": "Versicherungs-Gutachten",
        "name_en": "Insurance Survey",
        "scope": "Vereinfachte Inspektion für Versicherungs-Zwecke",
        "duration_hours": 6,
        "cost_eur_base": 1200,
        "what_is_checked": [
            "Rumpf-Struktur und großflächige Beschädigungen",
            "Rigg (visuell)",
            "Motor Lauf-Stunden und Zustand",
            "Elektrik (grundlegend)",
            "Wassereintritte und Lecks",
            "Sicherheitsausrüstung"
        ],
        "includes_moisture_mapping": False,
        "includes_engine_endoscope": False,
        "includes_ndt": False
    },
    "condition": {
        "name_de": "Bestands-Aufnahme",
        "name_en": "Condition Survey",
        "scope": "Periodische Überprüfung des Zustands (jährlich)",
        "duration_hours": 4,
        "cost_eur_base": 800,
        "what_is_checked": [
            "Sichtbare Beschädigungen (Rumpf, Deck)",
            "Rigg Funktionalität",
            "Motor Lauf-Stunden",
            "Abnutzungsverschleiss",
            "Sicherheits-Updates"
        ],
        "includes_moisture_mapping": False,
        "includes_engine_endoscope": False,
        "includes_ndt": False
    },
    "osmosis": {
        "name_de": "Osmose-Spezial-Gutachten",
        "name_en": "Osmosis Survey",
        "scope": "Tiefgehende Analyse von Osmose-Problemen",
        "duration_hours": 8,
        "cost_eur_base": 1800,
        "what_is_checked": [
            "Moisture mapping — systematische Feuchtemessung (grid pattern)",
            "Blasen-Analyse (Größe, Verteilung, Säure-Test)",
            "Oberflächenprobe (Abraum-Analyse)",
            "Potentialmaßnahmen (Reparatur vs Beschichtung)",
            "Prognose-Modell (wird es schlimmer?)"
        ],
        "moisture_meter_required": True,
        "reference_measurements": "Trockene Vergleichsmessungen mit kalibriertem Gerät",
        "reading_interpretation": {
            "gfk_dry": "8-12%",
            "gfk_acceptable": "12-18%",
            "gfk_concern": "18-25%",
            "gfk_problematic": ">25%",
            "holz_dry": "12-15%",
            "holz_concern": ">18%",
            "kernmaterial": "Sehr variabel, >30% = Problem"
        }
    },
    "rigging": {
        "name_de": "Rigg-Inspektion Spezial",
        "name_en": "Rigging Survey",
        "scope": "Detaillierte Rigg-Inspektion mit NDT",
        "duration_hours": 6,
        "cost_eur_base": 1500,
        "what_is_checked": [
            "Stahldrähte (Standing & Running) — Bruchstellen, Korrosion",
            "Swagging-Terminals — Dye Penetrant Test",
            "Spannschrauben (Turnbuckles) — Verschleiß, Korrosion",
            "Kettenschäkel — Rost, Integrität",
            "Spreizer — Rissbildung, Verschleiß",
            "Masttop — Rollen, Halyarden-Austritte",
            "Mast-Befestigung zum Schiff"
        ],
        "includes_dye_penetrant": True,
        "includes_visual_tape": True
    }
}


# ============================================================================
# NDT_METHODS — Zerstörungsfreie Prüfverfahren (NDT)
# ============================================================================

NDT_METHODS: Dict[str, Dict[str, Any]] = {
    "moisture_meter_capacitive": {
        "name_de": "Feuchtemessgerät (Kapazitiv)",
        "name_en": "Moisture Meter (Capacitive)",
        "what_it_detects": "Oberflächliche und subsuperfizielle Feuchte in GFK, Holz, Kernmaterial",
        "how_to_use": [
            "Sonde auf Oberfläche drücken (senkrecht, gutes Kontakt)",
            "Wartet bis Wert stabilisiert (~3-5 Sekunden)",
            "Mehrere Messungen in Region durchführen (min. 3)",
            "Referenzmessungen an trockenen Zonen dokumentieren"
        ],
        "interpretation": {
            "gfk_normal": "10-15%",
            "gfk_elevated": "15-25%",
            "gfk_critical": ">25%",
            "wood_normal": "12-18%",
            "wood_critical": ">20%",
            "note": "Temperatur/Feuchte der Umgebung (23°C, 50% RH) ist Standard"
        },
        "cost_eur": 150,
        "limitations": [
            "Misst nur oberflächlich (~15mm Eindringtiefe)",
            "Salzgehalt in Oberfläche beeinflusst Messung",
            "Nicht gut für dünne Schichten",
            "Temperatur-Abhängig (Kalibrierung notwendig)"
        ],
        "recommended_tools": ["Tramex CME4 oder ähnlich", "Kalibrierblock"]
    },
    "moisture_meter_pin": {
        "name_de": "Feuchtemessgerät (Pin-Sensor)",
        "name_en": "Moisture Meter (Pin Type)",
        "what_it_detects": "Tiefere Feuchte in Holz und Komposit-Kernmaterial",
        "how_to_use": [
            "Metallstifte in Material eindrücken (bei Bedarf vorbohren)",
            "Messgerät anschließen",
            "Wert ablesen",
            "Stifte entfernen und Loch versiegeln"
        ],
        "interpretation": {
            "wood_dry": "10-15%",
            "wood_concern": "20%+",
            "core_material": "Sehr variabel (>30% kritisch)"
        },
        "cost_eur": 200,
        "limitations": [
            "Beschädigte Oberfläche (Löcher)",
            "Nur an wenigen Stellen messbar",
            "Schwierig bei sehr harten Materialien",
            "Wiederholbarkeit problematisch"
        ],
        "recommended_tools": ["Sovereign 923 oder ähnlich"]
    },
    "percussion_tap_test": {
        "name_de": "Klopftest (Tap Test)",
        "name_en": "Percussion Tap Test",
        "what_it_detects": "Delaminierungen, Hohlstellen, Feuchtigkeit in Kernen",
        "how_to_use": [
            "Mit Münze oder Gummihammer auf Oberfläche klopfen",
            "Klang und Vibration beobachten",
            "Vergleich mit bekannt guter Fläche",
            "Systematisches Raster durcharbeiten"
        ],
        "sound_signatures": {
            "solid_laminate": "Voller, klarer, ringing Klang",
            "delamination": "Dumpfer, hohler Klang (klingt wie auf Holzbrett)",
            "water_in_core": "Klang verändert sich, Vibration gedämpft",
            "void": "Sehr hohler Klang, hell"
        },
        "cost_eur": 0,
        "limitations": [
            "Subjektiv (Hörvermögen variiert)",
            "Kann tiefe Defekte nicht erkennen",
            "Dicke des Materials beeinflusst Klang",
            "Biegung/Schub-Spannungen können Klang verfälschen"
        ],
        "recommended_tools": ["10-Cent Münze oder Gummimallet"]
    },
    "dye_penetrant_test": {
        "name_de": "Farbstoff-Eindringungs-Test (Dye Penetrant)",
        "name_en": "Dye Penetrant Test",
        "what_it_detects": "Oberflächliche Risse in Metall (Swagging, Schäkeln)",
        "how_to_use": [
            "Oberfläche reinigen und trocknen",
            "Rotes Eindring-Öl auftragen",
            "Wartet 10-15 Minuten (Eindring-Zeit)",
            "Oberfläche mit Tüchern abwischen",
            "Weiße Offenlegungspulver auftragen",
            "Risse zeigen sich als rote Linien"
        ],
        "cost_eur": 100,
        "limitations": [
            "Nur Oberflächenrisse erkannt",
            "Nicht gut auf porösen Materialien",
            "Chemikalien-Entsorgung erforderlich",
            "Zeit-intensiv (20-30 Min pro Bereich)"
        ],
        "recommended_tools": ["Sherwin Williams Spotcheck Kit oder ähnlich"]
    },
    "ultrasonic_thickness": {
        "name_de": "Ultraschall-Dickenmessung",
        "name_en": "Ultrasonic Thickness Measurement",
        "what_it_detects": "Material-Dicke und Korrosion (Dickenabbau)",
        "how_to_use": [
            "Ultraschall-Transducer auf Oberfläche setzen",
            "Koppelmedium (Öl) verwenden",
            "Gerät liest Dicke automatisch",
            "Mehrere Messungen durchführen (min. 10 pro Bereich)"
        ],
        "interpretation": {
            "gfk_hull": "4-6mm normal",
            "steel_hull": "6-8mm normal",
            "thinning": "Wenn <80% Original = Problem"
        },
        "cost_eur": 500,
        "limitations": [
            "Teuer (Anschaffung)",
            "Braucht Koppelmedium",
            "Nicht gut auf rauen Oberflächen",
            "Laminat-Richtung beeinflusst Messung"
        ],
        "recommended_tools": ["Olympus 45MG oder ähnlich"]
    },
    "thermal_imaging": {
        "name_de": "Thermische Bildgebung (IR-Kamera)",
        "name_en": "Thermal Imaging",
        "what_it_detects": "Feuchte-Bereiche, Delaminierungen (zeigen sich als Temperatur-Unterschiede)",
        "how_to_use": [
            "IR-Kamera auf Zielbereich richten",
            "Wartet bis Boot in Sonne oder Schatten ist (Temperatur-Ausgleich)",
            "Thermische Bilder aufnehmen",
            "Unterschiede dokumentieren"
        ],
        "cost_eur": 3000,
        "limitations": [
            "Sehr teuer",
            "Nicht immer aussagekräftig (Temperaturverlauf variiert)",
            "Nur bei bestimmten Temperaturbedingungen sinnvoll",
            "Erfordert Fachkompetenz zur Interpretation"
        ],
        "recommended_tools": ["FLIR Lepton oder besseres System"]
    },
    "endoscope_inspection": {
        "name_de": "Endoskop-Inspektion",
        "name_en": "Endoscope Inspection",
        "what_it_detects": "Innenräume, Auspuff-Zustand, Versteckte Bereiche",
        "how_to_use": [
            "Endoskop-Kopf in Öffnung einführen",
            "Kamera auf Monitor beobachten",
            "Systematisch den Bereich ausleuchen",
            "Bilder/Video aufzeichnen"
        ],
        "typical_uses": [
            "Auspuff-Krümmer Inspektion (Rost, Ablagerung)",
            "Masttop Inspektion (Lager, Verschleiß)",
            "Bilge-Bereiche (Struktur, Feuchtigkeit)",
            "Versteckte Spalten (Delaminierung Anzeichen)"
        ],
        "cost_eur": 300,
        "limitations": [
            "Benötigt Zugang zur Öffnung",
            "Monitor-Qualität variiert",
            "Schwierig in engen Räumen"
        ],
        "recommended_tools": ["GoPro-basiertes Endoskop 5m+"]
    }
}


# ============================================================================
# MOISTURE_READING_INTERPRETATION — Feuchte-Messung Interpretations-Leitfaden
# ============================================================================

MOISTURE_READING_INTERPRETATION: Dict[str, Any] = {
    "reference_values": {
        "gfk": {
            "dry": "8-12%",
            "acceptable": "12-18%",
            "elevated": "18-25%",
            "critical": ">25%",
            "very_critical": ">30%"
        },
        "wood": {
            "dry": "10-15%",
            "acceptable": "15-18%",
            "concern": "18-22%",
            "critical": ">22%"
        },
        "core_material": {
            "dry": "Variabel (5-15%)",
            "concern": ">20%",
            "critical": ">30%"
        }
    },
    "tramex_vs_sovereign": {
        "tramex": {
            "type": "Kapazitiv (oberflächlich)",
            "tiefe": "~15mm",
            "vorteil": "Schnell, nicht-invasiv, gut für Übersicht",
            "nachteil": "Nur Oberflächenfeuchte"
        },
        "sovereign": {
            "type": "Pin-Sensor (invasiv)",
            "tiefe": "~20-25mm (je Stift-Länge)",
            "vorteil": "Tiefere Messung, genauer für Kern-Feuchte",
            "nachteil": "Oberflächen-Beschädigung, Zeit-intensiv"
        }
    },
    "reference_measurement_technique": {
        "method": "Trockene Referenzmessung",
        "description": "Messung an Stelle, die definitiv trocken ist (z.B. unter Kabine bei neuem Boot)",
        "purpose": "Baseline für Vergleich etablieren",
        "process": [
            "1. Bekannt trockene Stelle auswählen",
            "2. Mehrfach messen (min. 5 Messungen)",
            "3. Durchschnitt berechnen → Reference-Wert",
            "4. Alle anderen Messwerte mit Reference vergleichen",
            "5. Abweichung dokumentieren (% über/unter Reference)"
        ]
    },
    "interpretation_strategy": {
        "step_1": "Reference-Messung durchführen",
        "step_2": "Systematic Grid — Raster-Messung durchführen (z.B. alle 50cm)",
        "step_3": "Hotspot identifizieren — Bereiche mit erhöhter Feuchte",
        "step_4": "Trend analysieren — Ist es lokalisiert oder flächig?",
        "step_5": "Ursache-Vermutung — Osmose, Lecks, Lüftung, Kondensation?",
        "step_6": "Prognose — Wird es schlimmer? Ist es stabil?"
    },
    "temperature_humidity_correction": {
        "note": "Feuchtemesswerte sind abhängig von Raumtemperatur und Luftfeuchte",
        "standard_conditions": "23°C, 50% relative Luftfeuchte",
        "correction": "Gerät sollte auf Standard-Bedingungen kalibriert sein",
        "practical_note": "Bei sehr unterschiedlichen Bedingungen (z.B. kaltes/feuchtes Wetter) Kalibrierung wiederholen"
    }
}


# ============================================================================
# PERCUSSION_TEST_KNOWLEDGE — Klopftest-Spezial-Wissensbasis
# ============================================================================

PERCUSSION_TEST_KNOWLEDGE: Dict[str, Any] = {
    "sound_signatures": {
        "solid_laminate": {
            "description": "Vollständig intakte Laminat-Struktur",
            "sound": "Voller, klarer, 'ringing' Klang — ähnlich wie auf Metall oder Glas",
            "duration": "Nachklang ca. 1-2 Sekunden",
            "what_it_means": "Keine Delaminierung, kein Wasser, keine Hohlstellen",
            "example": "Wie auf einem Glastisch klopfen"
        },
        "delamination": {
            "description": "Separation der Laminat-Schichten",
            "sound": "Dumpfer, hohler Klang — ähnlich wie auf leerer Holzkiste",
            "duration": "Klang bricht ab, kaum Nachklang",
            "what_it_means": "Laminat-Schichten sind separiert, Luft/Feuchtigkeit dazwischen",
            "example": "Wie auf Sperrholz-Gehäuse klopfen"
        },
        "water_in_core": {
            "description": "Wasser in Sandwich-Core (z.B. Balsa, Kork)",
            "sound": "Klang verändert sich während/nach Klopfen",
            "duration": "Dumpf, gedämpft, verkürzte Vibration",
            "what_it_means": "Core-Material ist mit Wasser gesättigt",
            "example": "Wie auf feuchte Schwamm klopfen"
        },
        "void": {
            "description": "Lufthohlstelle (z.B. Fertigungsfehler)",
            "sound": "Sehr hohler, heller Klang — überraschend laut",
            "duration": "Lange Nachhall",
            "what_it_means": "Hohlstelle ohne Halt dahinter",
            "example": "Wie in Rohre oder hohle Röhren klopfen"
        }
    },
    "technique": {
        "coin_tap": {
            "tool": "10-Cent oder 20-Cent Münze",
            "method": "Mit Fingernagel oder Münzrand auf Oberfläche klopfen",
            "advantage": "Fein, kontrolliert, subtil",
            "disadvantage": "Leise, schwer zu hören bei Schiffe mit Hintergrund-Geräusche"
        },
        "rubber_mallet": {
            "tool": "Gummihammer (200-500g)",
            "method": "Sanft auf Oberfläche schlagen (keine rohe Gewalt!)",
            "advantage": "Laut, deutlich, gut hörbar",
            "disadvantage": "Kann Oberfläche beschädigen, wenn zu hart"
        }
    },
    "limitations": {
        "cannot_detect": [
            "Tiefe Delaminierungen (unter 5cm tief)",
            "Kleine Risse ohne Hohlraum dahinter",
            "Oszillationen in dünnen Strukturen",
            "Geteilte aber noch zusammenhängende Laminate"
        ],
        "affected_by": [
            "Material-Dicke (dünn = heller Klang auch wenn OK)",
            "Biegung/Spannung in Material (beeinflusst Resonanz)",
            "Verstärkungen/Stringers dahinter (verändern Klang)",
            "Außen-Geräusche und Vibrationen",
            "Gehör des Inspektors (Unterschiede in Wahrnehmung)"
        ]
    },
    "best_practice": {
        "step_1": "Ruhigen Ort wählen, Hintergrund-Geräusche minimieren",
        "step_2": "Erste an bekannt guter Fläche testen (Referenz-Sound etablieren)",
        "step_3": "Systematisches Raster — gleichmäßig über Fläche verteilt",
        "step_4": "Mehrere Klopfungen pro Stelle (min. 2-3)",
        "step_5": "Bei Verdacht auf Problem → Nachfolge mit Feuchtemessgerät",
        "step_6": "Kombiniere mit Sichtprüfung (Verfärbungen, Blasen, Risse)"
    }
}


# ============================================================================
# GELCOAT_CONDITION_ASSESSMENT — Gelcoat-Zustandsbewertung
# ============================================================================

GELCOAT_CONDITION_ASSESSMENT: Dict[str, Dict[str, Any]] = {
    "crazing": {
        "name_de": "Haarissrisse (Crazing)",
        "name_en": "Crazing",
        "what_it_is": "Oberflächliche, oberflächlich Risse in Gelcoat — ähnlich Trockenrisse in Schlamm",
        "types": {
            "linear_crazing": {
                "description": "Einzelne oder parallel laufende Linien",
                "cause": "Spannungsabbau, ungleichmäßige Shrinkage beim Aushärten",
                "severity": "Minor — kosmetisch"
            },
            "map_crazing": {
                "description": "Netz-ähnliche Risse (wie Landkarte)",
                "cause": "Größere Spannungen, UV-Schaden über Jahre",
                "severity": "Minor bis Major — je nach Umfang"
            },
            "stress_crazing": {
                "description": "Risse in Verbiegungsbereichen (z.B. um Durchbrüche)",
                "cause": "Strukturelle Belastung, Design-Schwäche",
                "severity": "Major — kann auf tiefere Probleme hindeuten"
            }
        },
        "severity_levels": {
            "level_1": "Kleine, isolierte Linien (<1mm breit)",
            "level_2": "Mehrere Risse, aber <20% Fläche betroffen",
            "level_3": "Ausgedehnte Risse, 20-50% Fläche",
            "level_4": "Großflächig, >50% Fläche, Gelcoat löst sich ab"
        },
        "what_it_indicates": "Spannungsabbau ist normal bei neuen Booten. Bei älteren Booten kann es UV-Schaden oder strukturelle Probleme anzeigen."
    },
    "star_cracking": {
        "name_de": "Stern-Risse (Star Cracking)",
        "name_en": "Star Cracking",
        "what_it_is": "Risse die vom zentralen Punkt ausstrahlen (sternförmig) — typisch Impact-Schaden",
        "cause": "Lokaler Aufprall/Schlag gegen Gelcoat",
        "severity": "Major — zeigt Impact-Energie, mögliche Laminate-Schädigung dahinter",
        "what_to_check_next": [
            "Klopftest um Impact-Stelle (dumpfer Klang = Delaminierung)",
            "Feuchtemessgerät an Impact-Stelle",
            "Oberfläche um Risse auf weitere Risse prüfen (Spannungsausbreitung)"
        ],
        "repair_consideration": "Kleine Star-Risse (<5mm) sind oberflächlich, große (>10mm) deuten auf tiefere Schäden hin"
    },
    "osmosis_blisters": {
        "name_de": "Osmose-Blasen",
        "name_en": "Osmosis Blisters",
        "what_it_is": "Unter-Gelcoat-Blasen gefüllt mit Wasser und Säure",
        "size_interpretation": {
            "tiny": "<2mm — sehr früh, minimal Problem",
            "small": "2-5mm — normal, beginnend",
            "medium": "5-10mm — ausgeprägt, aktive Osmose",
            "large": ">10mm — fortgeschritten"
        },
        "acid_smell_test": {
            "how": "Blase vorsichtig öffnen und an Flüssigkeit riechen",
            "positive_smell": "Essig-ähnlicher Geruch → aktive Osmose (Säure-Bildung)",
            "no_smell": "Kein saurer Geruch → passive Blase (trockene Phase)"
        },
        "what_causes_osmosis": [
            "Wasser-Eindringung in Laminat",
            "Gelcoat-Mikrorisse (Crazing, Kratzer)",
            "Ungesättigte Polyester-Harz reagiert mit Wasser → Säure-Bildung",
            "Typically in älteren Booten (20+ Jahre), besonders Küsten-Segler"
        ],
        "blistering_zone_severity": {
            "scattered": "<5% der Fläche — gering (Maintenance nur)",
            "moderate": "5-20% — bedeutsam (Monitoring, eventuell Beschichtung)",
            "heavy": "20-50% — schwerwiegend (Reparatur notwendig)",
            "severe": ">50% — sehr ernst (großflächige Behandlung)"
        }
    },
    "chalking": {
        "name_de": "Kreidung",
        "name_en": "Chalking",
        "what_it_is": "Oberflächliche Verfärbung und Pulverisierung von Gelcoat",
        "cause": "UV-Bestrahlung — Gelcoat-Zersetzung",
        "how_to_check": "Dunkle Fläche mit Hand reiben — weißliches/pulveriges Abfallen",
        "severity": "Minor — kosmetisch, aber zeigt Alter des Gelcoat",
        "what_it_indicates": "Gelcoat ist alt und verliert Schutzfunktion. Laminat darunter kann anfälliger für Wasser-Eindringung werden."
    },
    "yellowing": {
        "name_de": "Vergilbung",
        "name_en": "Yellowing",
        "what_it_is": "Gelcoat verliert weiße Farbe, wird gelblich/grau",
        "cause": "UV-Exposition, Oxidation",
        "typical_pattern": "Sonnenseite vergilbt mehr als Schattenseite",
        "severity": "Minor — kosmetisch",
        "what_it_indicates": "Alter des Gelcoat, UV-Exposition"
    },
    "spider_cracks": {
        "name_de": "Spinnenwebmuster-Risse",
        "name_en": "Spider Cracks / Web Cracking",
        "what_it_is": "Sehr feines Netz von Rissen — feinere Version von Crazing",
        "cause": "Alterung, ungleichmäßige Shrinkage, Spannungen",
        "severity": "Minor",
        "aesthetic_impact": "Äußert sich als mattes, raues Aussehen statt glanz"
    },
    "print_through": {
        "name_de": "Fasermarkierung (Print-Through)",
        "name_en": "Print-Through",
        "what_it_is": "Abdrücke der darunter liegenden Laminat-Fasern sind auf Gelcoat-Oberfläche sichtbar",
        "what_it_indicates": "Gelcoat ist zu dünn oder Laminat-Qualität ist schlecht (grobe Fasern)",
        "severity": "Minor — kosmetisch, aber Qualitäts-Indikator",
        "typical_in": "Serie-Boote mit Kostenoptimierung, weniger in Custom-Booten"
    },
    "color_staining": {
        "name_de": "Verfärbung und Flecken",
        "name_en": "Color Staining",
        "types": {
            "rust_staining": {
                "appearance": "Rötlich-braun verfärbte Streifen",
                "cause": "Rost von Bewehrung/Fasteners darunter, läuft aus",
                "severity": "Major — zeigt Korrosion darunter"
            },
            "water_staining": {
                "appearance": "Dunkle oder helle Streifen (je Wasser-Mineralien)",
                "cause": "Wasser-Strömung, Lecks von oben",
                "severity": "Major — zeigt Wassereintritt"
            },
            "biological_staining": {
                "appearance": "Grüne oder schwarze Flecken (Algen, Pilze)",
                "cause": "Feuchtigkeit, Nährstoffe, mangelnde Luftzirkulation",
                "severity": "Minor bis Major — je nach Umfang und Ursache"
            },
            "impact_yellowing": {
                "appearance": "Gelb/braune Verfärbung rund um Kratzer oder Impact",
                "cause": "Laminat-Oxidation nach Impact-Freilegung",
                "severity": "Major — zeigt alten Schaden, mögliche Delaminierung"
            }
        }
    }
}


# ============================================================================
# STRUCTURAL_WARNING_SIGNS — Strukturelle Warnzeichen
# ============================================================================

STRUCTURAL_WARNING_SIGNS: Dict[str, Dict[str, Any]] = {
    "bulkhead_separation": {
        "name_de": "Schott-Ablösung von Rumpf",
        "name_en": "Bulkhead Separation from Hull",
        "what_it_is": "Schott (Querwand) löst sich von Rumpf-Innenseite ab",
        "how_to_detect": [
            "Visuelle Prüfung auf Spalten entlang Schott/Rumpf-Grenzlinie",
            "Klopftest entlang der Schott-Kante (dumpfer vs. voller Klang)",
            "Feuchtemessgerät an Schott-Rumpf-Übergang",
            "Sichtbares Licht durch Spalte scheint (bei dunklem Innenraum)"
        ],
        "severity": "Critical",
        "what_it_means": "Strukturelle Integrität ist kompromittiert, Schott kann nicht mehr Lasten verteilen",
        "cause": "Baudefekt, Verschleiß, Wasser-Eindringung mit Quellung"
    },
    "keel_bolt_weeping": {
        "name_de": "Kielbolzen-Flecken und Lecks",
        "name_en": "Keel Bolt Weeping",
        "what_it_is": "Wasser oder Rost tritt aus Kielbolzen-Befestigungspunkten aus",
        "how_to_detect": [
            "Visuelle Inspektion auf Rost-Flecken rund um Bolzenlöcher",
            "Weiße Salzablagerungen (evaporated salt from leaking seawater)",
            "Aktives Tropfen von Wasser bei Belastung",
            "Oberflächenrost oder Grünspan (Kupfer-Korrosion)"
        ],
        "severity": "Critical",
        "what_it_means": "Kielbolzen-Befestigung ist nicht mehr wasserdicht, führt zu Strukturrosion",
        "cause": "Dichtungsverschleiß, Verschraubungs-Lockerung, Material-Korrosion"
    },
    "rudder_play": {
        "name_de": "Ruder-Spiel und Bewegung",
        "what_it_is": "Ruder wiegt oder bewegt sich seitlich im Lager",
        "how_to_detect": [
            "Mit Hände am Ruder-Blatt drücken (seitlich, auf/ab)",
            "Spiel mit Messschieber messen",
            "Auf Geräusche beim Drehen des Ruders prüfen (Grinding, Klappern)"
        ],
        "severity": "Major",
        "acceptable_play": "<3mm (am Ruderblatt-Ende)",
        "unacceptable_play": ">5mm",
        "what_it_means": "Ruderlager sind verschlissen, Ruderkontrolle ist gefährdet"
    },
    "hull_deck_joint_failure": {
        "name_de": "Rumpf-Deck-Verbindung Versagen",
        "name_en": "Hull-Deck Joint Failure",
        "what_it_is": "Rumpf und Deck separieren sich, Dichtung bricht auf",
        "how_to_detect": [
            "Sichtbare Risse in der Fuge (von außen oder innen)",
            "Verfärbungen/Wasser-Spuren unter der Fuge",
            "Bewegung zwischen Rumpf und Deck (beim Belasten des Bootes)",
            "Dichtmasse ist geborsten oder fehlt"
        ],
        "severity": "Critical",
        "what_it_means": "Wassereintritt ist unkontrollierbar, strukturelle Integrität kompromittiert",
        "cause": "Laminate-Ermüdung, Dichtungsverschleiß, Designmängel"
    },
    "stringer_delamination": {
        "name_de": "Verstärkungs-Delaminierung (Stringers)",
        "name_en": "Stringer Delamination",
        "what_it_is": "Längsverstärkungen unter Deck/Rumpf trennen sich von Laminat",
        "how_to_detect": [
            "Klopftest entlang Stringer-Linien (dumpfer Klang = Problem)",
            "Sichtbare Wölbungen oder Absätze auf Oberfläche",
            "Feuchtemessgerät zeigt hohe Werte an Stringer-Linien"
        ],
        "severity": "Major",
        "what_it_means": "Strukturelle Steifheit ist reduziert, Boot verformt sich unter Belastung",
        "consequence": "Erhöhte Spannungen in Rumpf, schneller Verschleiß"
    },
    "impact_damage": {
        "name_de": "Impact-Schaden mit versteckter Delaminierung",
        "name_en": "Impact Damage with Hidden Delamination",
        "what_it_is": "Gelcoat-Kratzer oder Dellen, aber Delaminierung darunter ist verborgen",
        "how_to_detect": [
            "Vorsicht bei Kratzern und Dellen (nicht nur oberflächlich prüfen)",
            "Klopftest um Kratzer — kann dumpferer Klang anzeigen",
            "Feuchtemessgerät zeigt erhöhte Werte unter Impact",
            "Thermische Bildgebung kann Temperatur-Unterschiede zeigen"
        ],
        "severity": "Major",
        "why_dangerous": "Delaminierung kann schnell wachsen, besonders wenn Wasser eindringt",
        "assessment": "Jeden bedeutsamen Kratzer mit vollständiger NDT-Prüfung folgen"
    }
}


# ============================================================================
# RIGGING_INSPECTION_DETAIL — Rigg-Inspektion im Detail
# ============================================================================

RIGGING_INSPECTION_DETAIL: Dict[str, Dict[str, Any]] = {
    "wire_strands": {
        "name_de": "Stahldrähte - Strangprüfung",
        "what_to_check": [
            "Bruchstellen — wie viele?",
            "Oberflächenrost/Pitting",
            "Insgesamt Durchmesser-Reduktion"
        ],
        "broken_strands_action": {
            "0_1": "OK — ersetzen nicht nötig",
            "2": "Beobachten — nächste Saison überprüfen",
            "3_plus": "Ersetzen erforderlich — Sicherheitsrisiko"
        },
        "corrosion_types": {
            "surface_rust": "Oberflächenglanz ist weg, kann abgerubbelt werden",
            "pitting": "Lochfraß — tiefe Löcher in der Oberfläche (gefährlich!)",
            "crevice_corrosion": "Unter Verbindungsstellen, wo Luft nicht hin kommt"
        },
        "pitting_severity": {
            "light": "<10% des Draht-Oberfläche betroffen",
            "moderate": "10-25% betroffen",
            "severe": ">25% betroffen — Festigkeit stark reduziert"
        }
    },
    "swaged_terminals": {
        "name_de": "Swagging-Klemmen - Riss-Prüfung",
        "inspection_method": "Dye Penetrant Test (rot-weiß Methode)",
        "what_to_look_for": [
            "Oberflächliche Kratzer oder Dellen",
            "Risse (normalerweise radial vom Schwach-Punkt)",
            "Korrosion unter/um Swagging"
        ],
        "dye_test_procedure": [
            "1. Terminal saubern und trocknen",
            "2. Rotes Eindring-Öl auftragen, 10-15 Min warten",
            "3. Mit Papier abwischen",
            "4. Weiße Offenlegung-Pulver auftragen",
            "5. Risse werden rot sichtbar"
        ],
        "critical_locations": [
            "Unterstaggen-Terminals (hohe Belastung)",
            "Achterstagen-Terminals (Wenden/Segelmanöver)",
            "Oberflansch der Swagging (typisches Riss-Gebiet)"
        ]
    },
    "turnbuckles": {
        "name_de": "Spannschrauben - Verschleiß und Funktion",
        "inspection": {
            "rotate_test": "Spannschraube vollständig ein und ausdrehen",
            "resistance_normal": "Sanfter, stetiger Widerstand",
            "resistance_bad": [
                "Blockiert oder kann nicht gedreht werden",
                "Dreht sich ohne Widerstand (Gewinde-Verschleiß)"
            ]
        },
        "thread_wear": {
            "inspection": "Gummimanschette abnehmen, Gewinde-Zustand prüfen",
            "normal": "Klare, scharfe Gewinde-Markierungen",
            "worn": "Flache, abgerundete Gewinde-Spitzen",
            "corrosion": "Oberflächenrost oder Lochfraß unter Manschette"
        },
        "boot_removal": "Gummimanschette entfernen/hochfahren um versteckten Korrosion zu prüfen"
    },
    "chainplates": {
        "name_de": "Kettenschäkel - Rost und Befestigung",
        "inspection": [
            "Sichtbarer Rost oder Grünspan",
            "Schrauben/Bolzen fest oder locker?",
            "Deck-Durchdringung auf Wasserspuren prüfen",
            "Risse im Deck um Schäkel"
        ],
        "deck_penetration_concern": "Kettenschäkel sind typische Wassereintritt-Punkte, besonders unter Belastung",
        "typical_failure": "Dichtung versagt → Wasser → Unterseite wird nass → Holz-Verformung/Korrosion"
    },
    "spreader": {
        "name_de": "Spreizer - Root & Tip Inspection",
        "root_fitting": {
            "check": "Verbindung zum Mast, auf Risse prüfen",
            "typical_failure": "Ermüdungs-Risse an Spannungs-Konzentration",
            "dye_test": "Empfohlen für alte/belastete Spreizer"
        },
        "tip_wear": {
            "check": "Ende des Spreizers auf Abrasion prüfen",
            "typical_wear": "Loch in Kunststoff-Kappe wo Wire durchgeht",
            "consequence": "Wire wird beschädigt durch Spreizer-Ende"
        }
    },
    "masthead": {
        "name_de": "Masttop - Rolle, Halyarden, Licht",
        "sheave_wear": [
            "Rolle von Hand drehen — sollte leicht laufen",
            "Spiel in Lagern prüfen (<3mm akzeptabel)",
            "Kerben oder Verschleiß in Rolle-Boden sichtbar"
        ],
        "halyard_condition": [
            "Halyarden auf Verschleiß und Beschädigungen prüfen",
            "Umlenkungspunkte auf Quetschung prüfen",
            "Halyarden sollten frei laufen (kein Knarren)"
        ],
        "masthead_light": [
            "Funktion prüfen (leuchtet bei Stromzufuhr)",
            "Keine Feuchte in Lichtkopf",
            "Linsen sauber und unbeschädigt"
        ]
    }
}


# ============================================================================
# ENGINE_INSPECTION_CHECKLIST — Motor-Inspektions-Checkliste
# ============================================================================

ENGINE_INSPECTION_CHECKLIST: Dict[str, Dict[str, Any]] = {
    "oil_analysis": {
        "what_de": "Öl-Zustandsprüfung",
        "what_en": "Oil Condition Assessment",
        "color_interpretation": {
            "light_brown": "Normal — frisch",
            "dark_brown": "Normal — gelaufen aber OK",
            "black": "Verschleiß — zu viele Partikel, oder zu alt",
            "milky_white": "PROBLEM — Wasser im Öl (Zylinder-Undichtheit oder Kühlsystem-Leck)"
        },
        "particle_check": {
            "method": "Ölstab gegen helles Licht prüfen",
            "normal": "Keine oder sehr wenige Metallpartikel",
            "concern": "Sichtbare Metallpartikel → Verschleiß, Lager-Problem"
        },
        "viscosity_check": {
            "method": "Ölstab ziehen und zähflüssigkeit beobachten",
            "normal": "Öl fließt aber hat Körper (zähflüssig)",
            "thin": "Wässrig-dünn (verdünnt durch Kraftstoff?) → Problem",
            "thick": "Dickflüssig (zu alt, oxidiert) → Wechsel notwendig"
        }
    },
    "coolant": {
        "what_de": "Kühlsystem-Zustand",
        "what_en": "Cooling System Condition",
        "fluid_inspection": {
            "color": "Sollte grün, orange oder rosa sein (je Formulierung)",
            "clear": "Klares, keine Trübung",
            "brown": "Braun oder rostfarben → Korrosion im System",
            "sludgy": "Schlammig oder ölig → Kontaminiert"
        },
        "level_check": "Sollte beim MAX-Strich sein, Nachfüllung bedeutet Leck",
        "circulation": "Fühle Schläuche — sollten warm sein wenn Motor läuft"
    },
    "exhaust_manifold": {
        "inspection_method": "Endoskop-Inspektion",
        "what_to_look_for": {
            "rust_severe": "Rost/Korrosion bedeckt große Fläche → Problem",
            "white_deposits": "Weiße Kalkablagerungen → Wasser im Abgas",
            "black_soot": "Schwarze Rußablagerungen → Fehlzündung",
            "pitting": "Lochfraß — tiefe Löcher in Metalloberfläche"
        }
    },
    "belt_condition": {
        "what_de": "Riemen und Antriebsriemen",
        "what_en": "Belts and Drive Belts",
        "visual_check": [
            "Riemen auf Risse und Verschleiß prüfen",
            "Riemen sollte elastisch sein, nicht hart",
            "Keine Fransen oder Abrieb"
        ],
        "tension_check": "Riemen sollte mit Finger-Druck ~1cm eindrückbar sein"
    },
    "impeller": {
        "what_de": "Kühl-Lüfter-Flügel",
        "what_en": "Cooling Impeller",
        "typical_check": "Gummi-Flügel sollten noch elastisch sein, nicht hart/spröde",
        "replacement_interval": "Alle 3-5 Jahre oder bei Verhärtung",
        "failure_sign": "Gummi hart, spröde → Motor wird zu heiß"
    },
    "zincs": {
        "what_de": "Opfer-Anoden (Zink-Opfer)",
        "what_en": "Sacrificial Anodes (Zincs)",
        "where_located": "Motor-Gehäuse, Wasserkühler-Eintritt, Schraube",
        "condition": "Sollten abgenutzt sein (ist das Opfer der Korrosion)",
        "replacement_condition": "Wenn >50% aufgebraucht → ersetzen",
        "undersize_anodes": "Anoden zu klein oder fehlend → Motor-Teile rosten schneller"
    },
    "shaft_alignment": {
        "what_de": "Wellen-Fluchtung und Lager",
        "what_en": "Shaft Alignment and Bearings",
        "play_test": {
            "method": "Welle von Hand drehen, auf Spiel prüfen (axial, radial)",
            "acceptable": "<2mm",
            "unacceptable": ">5mm"
        },
        "runout_test": "Welle sollte konzentrisch laufen, nicht exzentrisch"
    },
    "engine_mounts": {
        "what_de": "Motor-Aufhängung",
        "what_en": "Engine Mounts",
        "rubber_check": [
            "Gummi sollte noch elastisch sein",
            "Keine Risse oder Bruchstellen",
            "Keine öl-Penetration"
        ],
        "hardened_rubber": "Gummi hart und spröde → Vibrationen und Verschleiß",
        "replacement": "Bei Verhärtung oder Rissen ersetzen"
    },
    "runtime_vs_condition": {
        "interpretation": {
            "low_hours_new_engine": "Weniger Verschleiß zu erwarten",
            "moderate_hours_good_maintenance": "Motor sollte noch lange leben",
            "high_hours_poor_service": "Kann problematisch sein (Kolben-Verschleiß, Lager-Spiel)"
        },
        "note": "Wartungs-Geschichte ist wichtiger als Stunden"
    },
    "saildrive_specific": {
        "diaphragm": {
            "check": "Alter prüfen (Gummi-Zersetzung)",
            "replacement_interval": "Alle 10 Jahre oder bei Versprödung",
            "failure": "Wasser tritt in Motor-Öl (milchiges Öl)"
        },
        "anodes": "Wie Motor-Anoden, aber spezifisch für Saildrive-Gehäuse",
        "oil_level": "Saildrive hat eigenes Öl-System — Level und Farbe prüfen"
    }
}


# ============================================================================
# QUALITY_LEVELS_BY_BOAT_TYPE — Qualitätsstufen-Vergleich
# ============================================================================

QUALITY_LEVELS_BY_BOAT_TYPE: Dict[str, Dict[str, str]] = {
    "spaltmasse": {
        "criterion": "Spaltmaße (Gap Tolerances)",
        "series": "2-3mm",
        "semi_custom": "1-2mm",
        "custom": "<0.5mm",
        "superyacht": "<0.3mm (Spiegelfinish-Standard)"
    },
    "gelcoat_texture": {
        "criterion": "Gelcoat-Oberflächenrauheit",
        "series": "Kleine Textur akzeptabel (Kosten-Optimierung)",
        "semi_custom": "Glatt, keine sichtbare Textur",
        "custom": "Spiegelfinish oder satiné",
        "superyacht": "Perfekter Glanz, keine Unebenheiten"
    },
    "laminate_regelmassigkeit": {
        "criterion": "Laminate-Faserverteilung",
        "series": "Mögliche Feuer-/Trocken-Stellen",
        "semi_custom": "Gleichmäßig, ohne trockene Flecken",
        "custom": "Perfekt durchgetränkt, kein Air Entrapment",
        "superyacht": "Hochmoderne Infusions-Technologie"
    },
    "fastener_quality": {
        "criterion": "Befestigungs-Material",
        "series": "Edelstahl A2 (einfach)",
        "semi_custom": "Edelstahl A4 oder besser",
        "custom": "Marin-Grade Edelstahl + Speziallegierung",
        "superyacht": "Höchste Korrosionsbeständigkeit, oft Duplex"
    },
    "paint_finish": {
        "criterion": "Farbanstrich-Qualität",
        "series": "Grundlage + 1 Schicht",
        "semi_custom": "Grundlage + 2-3 Schichten",
        "custom": "Kunstharz-Mehrschicht mit Schliff",
        "superyacht": "Auto-Klasse Lackierung, mehrere Handschliffe"
    },
    "edge_radiusing": {
        "criterion": "Scharfkanten-Abrundung",
        "series": "Scharfkanten bleiben",
        "semi_custom": "Kleine Abrundung (1-2mm)",
        "custom": "Deutliche Abrundung (3-5mm)",
        "superyacht": "Großzügige Abrundung, ergonomisch perfekt"
    },
    "interior_finish": {
        "criterion": "Innenaus-Finish",
        "series": "Basis-Möbel, einfache Befestigung",
        "semi_custom": "Hochwertige Möbel, solide Konstruktion",
        "custom": "Individuelle Anfertigung, Kunsthandwerk",
        "superyacht": "Bespoke Interior Design, Materialien höchster Güte"
    },
    "electrical_installation": {
        "criterion": "Elektrik-Anlage",
        "series": "Basis-Verkabelung, Standard-Komponenten",
        "semi_custom": "Ordentliche Installation, gute Markierungen",
        "custom": "Professionelle Marine-Elektrik, redundante Systeme",
        "superyacht": "Hochmoderne Automatisierung, alle aktuellen Standards"
    },
    "plumbing": {
        "criterion": "Rohrsystem",
        "series": "Standard-Plastik-Rohre",
        "semi_custom": "Hochwertige Rohre, gute Befestigung",
        "custom": "Marine-Grade Rohre + Redundanz",
        "superyacht": "Backup-Systeme, Isolierung, hochwertige Materialien"
    }
}


# ============================================================================
# ASSESSMENT FUNCTION — Inspektionsergebnisse bewerten
# ============================================================================

def assess_inspection_findings(findings: Dict[str, Any]) -> Dict[str, Any]:
    """
    Bewertet Inspektionsergebnisse und gibt Gesamtbewertung aus.

    Args:
        findings: Dict mit Befunden pro Zone
        Example: {
            "unterwasserschiff": {"osmosis_blisters": 15, "gelcoat_damage": 5},
            "rigg": {"wire_broken_strands": 2, "turnbuckle_corrosion": "moderate"},
            "motor": {"oil_color": "dark_brown", "coolant_condition": "good"}
        }

    Returns:
        {
            "overall_score": 0-100,
            "condition_rating": "Excellent|Good|Fair|Poor|Unacceptable",
            "critical_items": [...],
            "recommended_actions": [...],
            "estimated_repair_cost_eur": <int>
        }
    """

    score = 100
    critical_items = []
    major_items = []
    minor_items = []
    total_cost = 0

    # Bewertung nach Zone
    if "unterwasserschiff" in findings:
        uw_findings = findings["unterwasserschiff"]

        # Osmose-Blasen
        if "osmosis_blisters_percentage" in uw_findings:
            pct = uw_findings["osmosis_blisters_percentage"]
            if pct > 20:
                score -= 30
                critical_items.append("Extensive osmosis blisters (>20% of area) — urgent treatment needed")
                total_cost += 8000
            elif pct > 5:
                score -= 15
                major_items.append("Moderate osmosis blistering (5-20%) — monitor and plan repair")
                total_cost += 3000

        # Kielbolzen
        if "keel_bolt_weeping" in uw_findings and uw_findings["keel_bolt_weeping"]:
            score -= 25
            critical_items.append("Keel bolt weeping/leaking — structural integrity at risk")
            total_cost += 5000

    # Rigg-Befunde
    if "rigg" in findings:
        rigg_findings = findings["rigg"]

        # Gebrochene Litzen
        if "wire_broken_strands" in rigg_findings:
            broken = rigg_findings["wire_broken_strands"]
            if broken >= 3:
                score -= 20
                critical_items.append("Wire with ≥3 broken strands — replace immediately")
                total_cost += 2000

        # Swagging-Risse
        if "swagging_cracks" in rigg_findings and rigg_findings["swagging_cracks"]:
            score -= 20
            critical_items.append("Swagging terminal cracks detected — replace terminals")
            total_cost += 3000

    # Motor-Befunde
    if "motor" in findings:
        motor_findings = findings["motor"]

        # Milchiges Öl
        if motor_findings.get("oil_color") == "milky_white":
            score -= 25
            critical_items.append("Water in engine oil — internal damage risk")
            total_cost += 4000

        # Rost im Auspuff
        if motor_findings.get("exhaust_condition") == "severe_rust":
            score -= 15
            major_items.append("Severe exhaust manifold corrosion — plan replacement")
            total_cost += 2500

    # Bestimmung Gesamtrating
    if score >= 85:
        condition_rating = "Excellent"
    elif score >= 70:
        condition_rating = "Good"
    elif score >= 50:
        condition_rating = "Fair"
    elif score >= 30:
        condition_rating = "Poor"
    else:
        condition_rating = "Unacceptable"

    return {
        "overall_score": max(0, score),
        "condition_rating": condition_rating,
        "critical_items": critical_items,
        "major_items": major_items,
        "minor_items": minor_items,
        "recommended_actions": (
            critical_items + [f"Address: {item}" for item in major_items]
        ),
        "estimated_repair_cost_eur": int(total_cost),
        "assessment_date": "2026-03-21"
    }


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    # Example: Pre-purchase survey findings
    example_findings = {
        "unterwasserschiff": {
            "osmosis_blisters_percentage": 8,
            "keel_bolt_weeping": False
        },
        "rigg": {
            "wire_broken_strands": 1,
            "swagging_cracks": False
        },
        "motor": {
            "oil_color": "dark_brown",
            "exhaust_condition": "minor_rust"
        }
    }

    result = assess_inspection_findings(example_findings)
    print("Inspection Assessment Result:")
    print(f"Overall Score: {result['overall_score']}/100")
    print(f"Condition Rating: {result['condition_rating']}")
    print(f"Critical Items: {result['critical_items']}")
    print(f"Estimated Repair Cost: EUR {result['estimated_repair_cost_eur']:,}")
