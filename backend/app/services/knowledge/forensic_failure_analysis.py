"""
FORENSIC FAILURE ANALYSIS MODULE — AYDI Yacht Analysis Platform

Erfassung von realen Versagensmechanismen, Material-Wechselwirkungen,
kumulativen Degradationszyklen und versteckten Schadensmustern.

English code, German UX text. This module provides encyclopedic knowledge
of how and why yachts fail in the real world.
"""

from typing import Dict, List, Tuple, Optional
from enum import Enum
from dataclasses import dataclass
from datetime import datetime


class Environment(Enum):
    """Umgebungsbedingungen"""
    TROPICAL = "tropical"  # >25°C year-round, high humidity, 3x faster degradation
    TEMPERATE = "temperate"  # Standard Atlantic/Mediterranean
    ARCTIC = "arctic"  # Freezing cycles, UV from ice reflection


class MaintenanceLevel(Enum):
    """Instandhaltungsniveau"""
    NONE = 0
    POOR = 1
    BASIC = 2
    GOOD = 3
    EXCELLENT = 4


# ==============================================================================
# MATERIAL INTERACTION FAILURES — Material-Material-Versagenszenarien
# ==============================================================================

MATERIAL_INTERACTION_FAILURES = {
    "stainless_316_on_gfk_deck": {
        "material_a": "Edelstahl 316 Chainplate",
        "material_b": "GFK-Deck (Polyester)",
        "connection_type": "Bolzenschraubung durch Deck",
        "failure_mode": "Spaltkorrosion → Kernfäule + Bruch",
        "onset_years": (5, 15),  # min, max
        "severity": "sicherheitskritisch",
        "mechanism": (
            "Die Stahlschraube erzeugt eine Spaltkorrosion in der 316er-Passivschicht. "
            "Chloride dringen in den Spalt ein (Breite 0,1–0,5 mm). Der lokale pH fällt auf <3. "
            "Eisenionen diffundieren in den GFK-Kern. Dort katalysieren sie die Polyester-Hydrolyse. "
            "Glykolrückstände und Säuren (Essigsäure) bilden osmotische Zentren. Der Kern quillt, "
            "verliert Steifigkeit. Die Schraube lockert sich. Flexion verstärkt Wasser-Eindringung. "
            "Nach 5–15 Jahren Kern-Erosion bis zur Nullfestigkeit direkt unter der Befestigung. "
            "Der Beschlag reißt plötzlich aus."
        ),
        "detection_method": (
            "Druck-Test unter dem Beschlag (Kern zu weich → Bewegung). "
            "Bohrspäne-Test (Deck quillt um Schraube herum). "
            "Thermographie: Feuchte-Hotspot. UV-Inspektion unter Wasser nach Haul-Out."
        ),
        "prevention": (
            "Nicht-rostender Stahl M10+ (Durchloch vorbohrt 10,5 mm). "
            "Butyl-Dichtmasse + Epoxid-Grundierung (nicht Polyester-Spachtelmasse). "
            "Korundplättchen unter Schraube (verhindert Direktkontakt). "
            "Alle 5 Jahre: Überprüfung Kern-Festigkeit (Druckprobe)."
        ),
    },

    "brass_seacock_in_seawater": {
        "material_a": "Messing-Seeventil (60/40 Cu/Zn)",
        "material_b": "Meerwasser",
        "connection_type": "Immersion",
        "failure_mode": "Dezinkierung → porös → plötzlicher Bruch",
        "onset_years": (5, 20),
        "severity": "lebensbedrohlich",
        "mechanism": (
            "Messing dezinkiert in Seewasser. Zink (das edlere Element im Cu/Zn-Paar) löst sich auf, "
            "Kupfer bleibt als rötliche, spröde Schwamm-Matrix zurück. Der Prozess ist kaum sichtbar "
            "(rot statt gold). Nach 5–20 Jahren (je nach Seewasser-Chemie) kann eine Kraft >10 N "
            "das Ventilgehäuse durchbrechen. Wasser strömt ins Schiff. Schneller Untergang."
        ),
        "detection_method": (
            "Sichtprüfung: Farbe dunkelrot statt glänzend gelb? Dezinkierung! "
            "Kratzen: Rot-Pulver statt Metall-Glanz = fortgeschritten. "
            "Druck-Test: Biegeprobe (ohne Zerstörung: Oberflächenprobe mit Hammer). "
            "Röntgen-Durchleuchtung (nur auf Werft)."
        ),
        "prevention": (
            "Seeventile NUR aus Nickel-Aluminium-Bronze (CuNiAl) oder Muntz-Messing (Cu 60%, Zn 39%, Sn 1%) "
            "mit Arsenic-Zusatz (<0,05 % verhindert Dezinkierung). "
            "Opferanoden in Seewasser-Bereichen (Magnesium oder Zink). "
            "Alle 2 Jahre: Visueller Check + Funktionsprobe (Ventil betätigen, Funktion prüfen). "
            "Bei Rot-Färbung sofort tauschen."
        ),
    },

    "stainless_bolt_on_aluminum_hull": {
        "material_a": "Edelstahl-Bolzen (300er-Serie)",
        "material_b": "Aluminium-Rumpf",
        "connection_type": "Bolzenschraubung in Loch",
        "failure_mode": "Galvanische Korrosion des Aluminiums",
        "onset_years": (1, 5),
        "severity": "mittelschwer (Festigkeitsverlust, Abdichtungsprobleme)",
        "mechanism": (
            "Edelstahl (edle Kathode, ~−0,04 V vs. Standard) und Aluminium (Anode, ~−0,83 V) "
            "bilden ein Galvani-Paar. Im Elektrolyt (Meerwasser, feuchte Luft) fließt ein Strom: "
            "Aluminium oxidiert bevorzugt (Anode). Ein Ring aus Al₂O₃ (Alu-Oxid) und AlOOH (Böhmit) "
            "bildet sich um die Schraube herum. Dies ist volumetrisch >2x größer als das Ursprungs-Alu. "
            "Der Ring sprengt die Dichtung. Wasser dringt ein. Nach 1–5 Jahren sichtbare Korrosion, "
            "Festigkeit der Befestigung >50 % reduziert."
        ),
        "detection_method": (
            "Sichtprüfung: Weiße oder grüne Korrosions-Aureole um die Schraube. "
            "Druck-Prüfung: Schraube dreht sich zu leicht (Gewinde-Korrosion). "
            "Durchlicht: Spiel zwischen Schraube und Rumpf >1 mm = fortgeschritten."
        ),
        "prevention": (
            "ISOLATION notwendig: Isolier-Unterlegscheibe (Kunststoff oder Teflon) unter Kopf und Mutter. "
            "Isolier-Ring im Loch (Epoxid-Tulle oder Kunststoff-Hülse). "
            "Dichtmasse: Polyuretan oder Sikaflex (bildet Barriere gegen Elektrolyt). "
            "Alternative: Titanium-Bolzen statt Edelstahl (noch edler, weniger Treiber, teuer). "
            "Oder: Nieten statt Schrauben (kein galvanisches Paar wenn beides Al)."
        ),
    },

    "teak_plank_on_gfk_sandwich_deck": {
        "material_a": "Teak-Planke (Dicke 8–10 mm)",
        "material_b": "GFK-Sandwich-Deck (Balsa oder PVC-Schaum-Kern)",
        "connection_type": "Verschraubt durch Deck + Sikaflex",
        "failure_mode": "Kern quillt → Festigkeitsverlust → Planke lockert sich",
        "onset_years": (3, 10),
        "severity": "mittelschwer (Rutsch-Risiko, Beschlag-Versagen)",
        "mechanism": (
            "Jede Schraube durch Teak-Planke ist ein WASSERWEG. Teaköl hydrophob, aber die Schraube "
            "durchbricht diese Barriere. Kapillarwirkung treibt Wasser entlang der Schraube ins Deck. "
            "Im Kern (Balsa oder PVC-Schaum, Wassernaufnahme 5–30 Vol%) expandiert das Wasser. "
            "Bei Balsa: Zellstruktur quillt um 2–4 % linear. PVC-Schaum: Schichtablösung und Destabilisierung. "
            "Nach 3–10 Jahren: Kern am Schraubloch: E-Modul fällt auf <20 % des Original-Wertes. "
            "Planke sitzt lose, rutscht unter Last, scheuert Teak ab, erzeugt Spiel für mehr Wasser-Eindringung."
        ),
        "detection_method": (
            "Druck-Test an den Teakplanken: Zu viel Flex (E-Modul-Test). "
            "Sichtprüfung: Risse im Sikaflex-Streifen neben der Planke (Indikator für Quellung). "
            "Feuchte-Sensor im Kern (Bohrloch neben Schraube, schnell wieder verschließen). "
            "Thermographie nach Regen: Kalter Fleck unter Planke = Feuchte-Kern."
        ),
        "prevention": (
            "OPTION 1 (Best Practice): Epoxid-Barriere-Coat auf Kern VOR Teakverlegung. "
            "OPTION 2: Bond Breaker (Kunststoff-Folie) zwischen Teak und Deck. "
            "OPTION 3: Alle Schrauben mit Epoxid-Harz kaltvergossen (nicht Sikaflex). "
            "Fugenbreite 3–5 mm (Sikaflex 298/290DC), gefüllt mit Sand-Pigment (UV-beständig). "
            "Teak-Öl: Polyurethan-Öl, 2x pro Jahr auftragen (nicht zu sparsam). "
            "Alle 5 Jahre: Komplett-Überprüfung Teakfugen + Schraublöcher."
        ),
    },

    "carbon_laminate_on_aluminum_fitting": {
        "material_a": "Carbon-Laminat (EP6K-Gewebe, Harz: Epoxid)",
        "material_b": "Aluminium-Beschlag",
        "connection_type": "Geklebt oder mechanisch verbunden",
        "failure_mode": "Galvanische Korrosion des Aluminiums, Klebeversagen",
        "onset_years": (0.05, 0.5),  # Monate bis wenige Jahre
        "severity": "mittelschwer (Beschlag löst sich, Vibration)",
        "mechanism": (
            "Carbon (~+0,2 bis +0,5 V vs. Standard, sehr edel) bildet mit Aluminium (~−0,83 V) "
            "ein extrem unausgewogenes Galvani-Paar. Potentialdifferenz: ~1000 mV (!). "
            "Wenn geklebt: Der Kleber ist ein Elektrolyt (Feuchte dringt ein). Strom fließt. "
            "Al wird aggressiv korrodiert. Die Klebefuge schwächt sich ab. "
            "Wenn mechanisch verbunden (Bolzen): Seeventile-ähnliches Szenario (siehe oben). "
            "Aber intensiver wegen höherer Potentialdifferenz. Schon nach Wochen bis Monaten "
            "sichtbare Korrosions-Aureole und Festigkeitsverlust >30 %."
        ),
        "detection_method": (
            "Sichtprüfung: Weiß-Grüne Korrosion-Aureole unter Carbon-Laminat (von außen schwer sichtbar). "
            "Ultraschall-Test: Klebeflächendefekte (Delaminationen). "
            "Druckprobe: Carbon-Laminat hebt sich zu leicht ab vom Beschlag."
        ),
        "prevention": (
            "ISOLATION ESSENTIELL: Kunststoff-Unterlegscheibe oder Butyl-Dichtmasse zwischen Carbon und Alu. "
            "Epoxid-Kleber mit Isolier-Eigenschaft (z.B. 3M Scotchbond, mit Füllstoff). "
            "Oder: Kunststoff-Abstandshalter (PEEK, PTFE) zwischen Laminaten. "
            "Oberflächenscutz: Epoxid-Versiegelung der Al-Oberfläche VOR Montage. "
            "Opferanodenband (Zink oder Magnesium) in der Nähe anbringen (zieht Strom). "
            "Alle 2 Jahre: Visuelle Inspektion, ggf. Isolier-Schicht erneuern."
        ),
    },

    "polyester_gelcoat_in_seawater": {
        "material_a": "Polyester-Gelcoat (orthophthal, isophthal)",
        "material_b": "Meerwasser",
        "connection_type": "Immersion, Oberflächenbelastung",
        "failure_mode": "Osmose → Blasen → Harzabbau → Wassereindringung",
        "onset_years": (5, 15),
        "severity": "mittelschwer → schwer (ästhetisch und strukturell)",
        "mechanism": (
            "Polyester-Harz und Gelcoat enthalten Glykolrückstände und Styrol-Reste (Herstellungs-Nebenprodukte). "
            "Im Salzwasser entsteht ein osmotischer Gradient. Wassermoleküle diffundieren durch die "
            "Gelcoat-Schicht ins Harz, um Konzentrations-Unterschiede auszugleichen. "
            "Nach 5–15 Jahren (Orthophthal früher, Isophthal später) sammeln sich Wassertropfen "
            "in Laminat-Poren. Osmotischer Druck wölbt die Gelcoat nach außen → Blasen. "
            "Innen: Die Polyester-Kettenverbindungen hydrolysieren. Essigsäure bildet sich (pH <3 lokal). "
            "Dies katalysiert weitere Hydrolyse → Harz wird spröde, verliert Scherfestigkeit >40 %. "
            "Tropische Gewässer: 3x schneller Prozess wegen höherer Temperatur."
        ),
        "detection_method": (
            "Blasen-Prüfung nach Haul-Out (KRITISCH: Blasen verschwinden 1–2 Tage nach Haul-Out wegen "
            "Druckausgleich! → Inspektion SOFORT nach Aufzug, nicht später). "
            "Farb-Verfärbung (gelblich-braun statt rein weiß/blau). "
            "Rauchmittel-Test: Gelcoat-Risse (Mikrorisse sind Eintrittspforten für Wasser). "
            "Kern-Bohrung + Feuchte-Sensor (zerstörerisch)."
        ),
        "prevention": (
            "Bei Neubau: VINYLESTER-Barriere-Schicht (obere 0,5–1,0 mm). Vinylester quillt nicht osmotisch. "
            "Oder: NPG-Gelcoat (Neopentylglykol, resistenter gegen Osmose als Standard). "
            "Oder: Epoxid-Barriere-Schicht auf dem Gelcoat (wet-on-wet während Aushärtung). "
            "Vakuum-Infusion (reduziert Voids, weniger Wasserwege). "
            "Feuchte-Sperrschicht (Epoxid) auf Innenseite des Rumpfes (verhindert Verdampfung ins Laminat). "
            "Bei Reparatur: Gelcoat-Schleifer (entfernt alle Blasen-Bereiche), monatelang TROCKNEN (>1 Jahr), "
            "Vinylester-Relaminierung (nicht Polyester), neue Epoxid-Barriere wet-on-wet. "
            "Bloßes Trocknen und Überstreichen ist KEINE Lösung."
        ),
    },

    "pvc_foam_core_near_engine": {
        "material_a": "PVC-Schaum-Kern (Divinycell, Corecell)",
        "material_b": "Motor-Abwärmestrahlung",
        "connection_type": "Nähe (<50 cm) zu Motor/Auspuff",
        "failure_mode": "Kern erweicht → Scherfestigkeit kollabiert",
        "onset_years": (0.01, 0.1),  # Tage bis Monate
        "severity": "lebensbedrohlich (Rumpf verliert Steifigkeit)",
        "mechanism": (
            "PVC-Schaumkerne haben eine Glasübergangs-Temperatur (Tg) von 55–65°C (je nach Formulierung). "
            "Bei >70°C wird der Kunststoff-Binder plastisch. Die Zellstruktur kollabiert lokal. "
            "Dichte wächst, E-Modul fällt exponentiell. Bei anhaltender Hitze (Motor-Zyklen) "
            "kann nach Wochen bis Monaten der Kern um den Motor komplett erweicht sein. "
            "Rumpf-Steifigkeit fällt um 50–80 %. Bei Seegang: Resonanz-Versagen oder Spantbruch möglich."
        ),
        "detection_method": (
            "Temperatur-Messung direkt am Kern (Infrarot-Thermometer, >70°C = Alarm). "
            "Druck-Prüfung: Kern zu leicht einzudrücken (Eindringtiefe >5 mm = erweicht). "
            "Gewicht-Messung: Erweichter Kern sinkt (Wasser-Absorption bis 10 % → massiver). "
            "Visuelle Verfärbung: Gelbbraun statt weiß (Thermo-Abbau)."
        ),
        "prevention": (
            "Mindestens 50 cm Abstand Motor zu Rumpf. Isolier-Matratze (Basalt-Faser, min. 50 mm). "
            "Auspuff-Mantel (Kupfer-Edelstahl-Gewebe, 50 mm Abstand). "
            "Aktive Belüftung im Motor-Schacht (Temperatur <50°C halten). "
            "Wärme-Strahler-Schirm aus Aluminium-Folie um Motor (reflektiert 90 % Strahlung). "
            "Im Neubau: Strukturelles Sandwich weiter weg vom Motor, oder Balsa/Polyurethau-Kern (höhere Tg)."
        ),
    },

    "balsa_core_frost_cycles": {
        "material_a": "Balsa-Kern (dicht gehobelt, ~100 kg/m³)",
        "material_b": "Frost-Zyklus (Eis-Sprengung)",
        "connection_type": "Wasser-Eindringung → Eiskristalle im Kern",
        "failure_mode": "Zellstruktur gesprengt → Kern-Festigkeit = 0",
        "onset_years": (0.03, 1),  # Ein Frost-Zyklus kann genügen
        "severity": "kritisch (Structural-Integrity)",
        "mechanism": (
            "Balsa besteht aus wenig Zellstruktur (75–80 % Hohlraum, 20–25 % Holzfasern). "
            "Wenn Wasser eindringt (z.B. durch Schraube, Riss im Gelcoat) und gefriert, "
            "wächst Eis um 9 % in Volumen. Der Druck sprengt die dünnwandigen Zellen. "
            "Schon EINER Frost-Zyklus kann ausreichen (Wasser muss nur 1–2 mm tief eindringen, "
            "dann kann Eiskristall die Nachbar-Zellen sprengen). Nach dem Auftauen: "
            "Die Zellstruktur ist zerstört, der Kern ist matschig, kein Verbund mehr mit dem Laminat. "
            "Kern-Festigkeit sinkt auf <10 % des Originals. Rumpf-Steifigkeit fällt katastrophal."
        ),
        "detection_method": (
            "Temperatur-Monitoring in Winter-Gegenden: Kern-Temperatur unter 0°C? Gefahr! "
            "Sichtprüfung: Nach Frost-Periode Verfärbung oder Flecken im Deck (Wasser-Eindringung). "
            "Druck-Prüfung: Kern zu leicht einzudrücken, kein Widerstand. "
            "Ultraschall: Delaminationen zwischen Laminat und Kern. "
            "Röntgen-Aufnahme (sehr teuer, aber definitiv)."
        ),
        "prevention": (
            "BESTE LÖSUNG: Boote in Wintergegenden NIEMALS mit offenen Fenstern/Rissen überwintern. "
            "Lagerung an Land, unter Abdeckung, >5°C halten. "
            "ODER: Polyurethan-Kern oder PVC-Strukturschaum statt Balsa (weniger Wassereindringung). "
            "Alle Laminat-Risse vor Winter reparieren (Epoxid-Versiegelung). "
            "Regelmäßige Überprüfung nach jedem Frost-Zyklus. "
            "Wasser-Barriere auf Balsa-Oberfläche (Epoxid-Grundierung vor Laminierung)."
        ),
    },

    "epoxy_barrier_under_uv": {
        "material_a": "Epoxid-Barriere-Schicht (Dicke 0,5–1,0 mm)",
        "material_b": "UV-Strahlung (315–400 nm)",
        "connection_type": "Oberflächenbelastung",
        "failure_mode": "Spröde-Bruch durch UV-Abbau",
        "onset_years": (2, 5),
        "severity": "mittelschwer (Wasser-Eindringung möglich)",
        "mechanism": (
            "Epoxid-Harz absorbiert UV in diesem Spektralbereich. Dies bricht Bindungen auf (Photolyse). "
            "Nach 2–5 Jahren unter freier UV-Exposition (z.B. unbeschatteter Schiffsdeck) "
            "werden die oberflächlichen 0,1–0,5 mm des Epoxids spröde. "
            "Mikrorisse entstehen. Diese sind Eintrittspforten für Wasser. "
            "Unter der brüchigen Schicht bildet sich Osmose (wenn darunter Polyester ist). "
            "Die Barriere-Funktion geht verloren."
        ),
        "detection_method": (
            "Kratzer-Test: Spröde Krümel statt zäher Abrieb (Zähigkeit-Reduktion = Spröde). "
            "Oberflächenriss-Muster (Dachziegel-ähnlich, 0,1–1 mm Risse). "
            "Farb-Verblassung (Gelbstich oder Verfärbung, Je nach Pigmentierung). "
            "Wasser-Eindringung: Osmose-Blasen unter der UV-geschädigten Schicht."
        ),
        "prevention": (
            "Epoxid-Schichten IMMER mit UV-stabiler Deckschicht schützen: "
            "Option A: Polyurethan-Topcoat (2K, 50–100 µm, 15+ Jahre UV-Schutz). "
            "Option B: Aliphatic Polyurethane (noch besser, aber teurer). "
            "Option C: Acryl-Polyurethan (2K Acryl, 80–150 µm). "
            "Die Deckschicht absorbiert UV-Strahlung statt das darunter liegende Epoxid. "
            "Alle 10 Jahre: Deckschicht-Überprüfung und Nachbeschichtung. "
            "In tropischen Gegenden: Alle 5 Jahre."
        ),
    },

    "sikaflex_joint_under_uv_salt": {
        "material_a": "Sikaflex-Dichtmasse (298, 290DC, Polyurethan)",
        "material_b": "UV + Salzwasser",
        "connection_type": "Fugendichtung auf Deck/Rumpf",
        "failure_mode": "Verhärtung + Spannungsrisse → Undichtigkeit",
        "onset_years": (3, 8),
        "severity": "mittelschwer (Wasser-Eindringung entlang Fuge)",
        "mechanism": (
            "Sikaflex ist ein Polyurethan-Dichtmaterial (Elastizität: 50–100 % Dehnung bei Vordehnung). "
            "UV (besonders 280–320 nm) bricht die Polyurethan-Ketten auf. Die Dichtmasse wird härter, "
            "Dehnbarkeit sinkt auf <20 %. Gleichzeitig: Salzwasser + UV-Radikale katalysieren "
            "Oxidation der Oberfläche. Nach 3–8 Jahren ist die Fuge spröde und reißt auf. "
            "Risse folgen den Spannungslinien (Rumpf-Flexion). Wasser läuft entlang der Fuge "
            "in Laminat-Schichten ein."
        ),
        "detection_method": (
            "Oberflächenrisse-Inspektionen (Lupe, >0,5 mm breite Risse = Problem). "
            "Dehnung-Test: Manuell die Fuge um 5–10 % dehnen → zu steif oder Risswachstum? "
            "Verfärbung (graubraun statt hellbraun). "
            "Wasser-Eindringung: Flecken auf Innenseite des Laminats unter der Fuge (nach Regen)."
        ),
        "prevention": (
            "UV-Schutz durch Pigmentierung oder Topcoat: "
            "Option A: Sikaflex-Fuge mit UV-stabilem Polyurethan-Anstrich beschichten (2K Acryl-PU, 80 µm). "
            "Option B: Vorgefertigte Kautschuk-Streifen (EPDM) über Sikaflex-Fuge kleben (UV-undurchlässig). "
            "Fugenbreite: 3–5 mm (zu schmal = unzureichende Elastizität). "
            "Fugentest alle 3 Jahre: Kratzen (Verhärtung sichtbar?), Dehnung-Probe. "
            "Nach 8 Jahren: Komplette Fuge-Erneuerung empfohlen (aufschleifen, ausfräsen, neu füllen)."
        ),
    },

    "stainless_under_rubber_boot": {
        "material_a": "Edelstahl-Schraube oder Bolzen",
        "material_b": "Gummi-Manschette (z.B. Turnbuckle-Stiefel, EPDM)",
        "connection_type": "Wasserfalle unter Gummimanschette",
        "failure_mode": "Spaltkorrosion, unsichtbar unter der Manschette",
        "onset_years": (5, 10),
        "severity": "mittelschwer (Überraschungs-Bruch bei Last)",
        "mechanism": (
            "Der Gummi-Stiefel schließt die Schraube/den Bolzen mechanisch ein und erzeugt "
            "eine feuchte Kammer (relative Feuchte oft >95 %). Salzwasser/Brackwasser sammelt sich "
            "unter der Manschette. Kleine Risse im Gummi oder Abnutzungsstellen werden zu Spalten. "
            "Passivschicht des Edelstahls bricht lokal auf. Chlorid-Ionen diffundieren ein. "
            "Spaltkorrosion beginnt, ist aber optisch verborgen (unter Gummi). "
            "Nach 5–10 Jahren: Querschnitt der Schraube um 30–50 % reduziert. "
            "Eine plötzliche Belastung (Sturm, Bugspriet-Zug) → Bruch."
        ),
        "detection_method": (
            "Gummi-Manschette entfernen und Oberflächenprüfung. "
            "Farb-Verfärbung oder schwarze Flecken auf Stahl (Korrosions-Einlagerungen). "
            "Magnetischer Härte-Test: Korrodierte Stellen sind weicher. "
            "Druckprobe: Schraube bricht zu leicht ab (Querschnitt reduziert). "
            "Regelmäßige Entfernung und Trocknung der Gummi-Stiefel notwendig."
        ),
        "prevention": (
            "Gummi-Stiefel entfernen und trocknen: "
            "Alle 3–6 Monate (bei Lagerlagerung regelmäßig, nicht dauerhaft drauf). "
            "Unter der Manschette: Dünne Korrosionsschutz-Fette auftragen (z.B. Lanolin oder Thalassa-Wachs). "
            "Alternativer Schutz: Schrumpf-Kunststoff-Schlauch (Polyolefin) statt Gummi "
            "(kürzere Lebensdauer als Gummi, aber weniger Wasserfallen). "
            "Edelstahl 316L bevorzugen (weniger Spaltkorrosion als 304). "
            "Alle 2 Jahre: Gummi-Stiefel ersetzen (Verschleiß)."
        ),
    },

    "copper_antifouling_on_aluminum": {
        "material_a": "Kupfer-Antifouling-Anstrich (Cu 50–70 % Anteil)",
        "material_b": "Aluminium-Rumpf",
        "connection_type": "Gebundener Anstrich auf Alu",
        "failure_mode": "Lochfraß → Rumpf-Durchbruch",
        "onset_years": (0.1, 1),  # Wochen bis Monate
        "severity": "lebensbedrohlich (Lecka in Meerwasser)",
        "mechanism": (
            "Kupfer ist ~+0,3 V (vs. Standard), Aluminium ~−0,83 V. "
            "Potentialdifferenz: >1100 mV. Wenn Cu-AF direkt auf Alu (ohne Isolierschicht) hält, "
            "diffundiert Cu²⁺ durch Beschichtung in die Al-Oberfläche. "
            "Galvanische Paare bilden sich. Lokal wird Aluminium bevorzugt korrodiert. "
            "Statt flächiger Korrosion entstehen schmale LOCHFRASS-Kanäle (Tiefe 0,5–1 mm/Monat möglich). "
            "Nach nur Wochen bis Monaten können Rumpf-Durchbrüche entstehen. Schnelle Wassereindringung."
        ),
        "detection_method": (
            "Oberflächenprüfung nach Haul-Out: Kleine schwarze oder rötliche Punkte im AF (= Lochfraß). "
            "Oberflächenrauheit (Lupe): Alu-Oberfläche porös/rauh statt glatt. "
            "Druck-Prüfung: Dünne Dellenpusher → sofort durchstoßen (Loch zu tief). "
            "Dickenmeß-Gerät (Ultraschall): Alu-Dicke unter AF gemessen."
        ),
        "prevention": (
            "NIEMALS Cu-AF direkt auf Alu auftragen. "
            "Isolier-Schicht ESSENTIELL: "
            "Option A: Epoxid-Grundierung, min. 100 µm, auf Alu-Rumpf auftragen VOR AF. "
            "Option B: Alu-Oxide-Passivierung (Chromat oder Cerium-Passiv, chemisch), dann Epoxid. "
            "Option C: Opferschicht aus Zink- oder Magnesium-Band an kritischen Stellen anbringen "
            "(zieht galvanischen Strom). "
            "BESSER: Zinn-Antifouling oder Kupferoxid-freie Varianten verwenden (weniger Potentialdiff.). "
            "BEST: Epoxid-AF ohne Cu (z.B. Silikon-basierte AF, spielfrei mit Alu)."
        ),
    },

    "polyester_on_polystyrene": {
        "material_a": "Polyester-Harz (ungesättigt)",
        "material_b": "Polystyrol-Schaumkern (z.B. XPS-Foam, falscher Kern-Typ)",
        "connection_type": "Laminierung auf Styropor",
        "failure_mode": "Styrol löst Schaumkern auf → struktureller Kollaps",
        "onset_years": (0.01, 0.1),  # Tage bis Wochen während Verarbeitung
        "severity": "kritisch",
        "mechanism": (
            "Polyester-Harz wird mit Styrol verdünnt (25–40 % Styrol als Lösemittel für die Kunstharze). "
            "Styrol ist ein starkes Lösemittel für Polystyrol. "
            "Wenn (fehlerhafte) Polyester-Harz auf Polystyrol-Schaumkern laminiert wird, "
            "diffundiert Styrol aus dem Harz in den Schaumkern. "
            "Die Polystyrol-Binder lösen sich auf. Der Schaumkern wird weich und kollabiert lokal. "
            "Dies passiert SCHNELL, bereits während des Aushärtungsprozesses (Tage bis Wochen). "
            "Resultat: Rumpf-Steifigkeit sofort reduziert, Delaminationen."
        ),
        "detection_method": (
            "Während Herstellung: Kern-Topographie ändert sich, Oberfläche wird wellig. "
            "Nach Aushärtung: Sichtbare Unebenheiten im Laminat-Anstrich. "
            "Druck-Prüfung: Kern zu leicht einzudrücken. "
            "Röntgen: Poren-Struktur des Kerns ist zerstört/kollabiert."
        ),
        "prevention": (
            "NIEMALS Polyester-Harz auf Polystyrol-Schaumkern verwenden! "
            "KORREKT: Balsa, PVC-Strukturschaum, oder Polyurethan-Kern. "
            "Falls Polyester gefordert: Kern mit Barriere-Schicht versiegeln (Epoxid oder Polyurethan, 0,5 mm). "
            "Handlaminierung mit Polyester: Styrol-Verdampfung durch Belüftung minimieren. "
            "BESSER: Epoxid-Harz verwenden (meist kein Styrol, oder Styrol gebunden). "
            "Oder: Vinylester (weniger Styrol-Verdampfung)."
        ),
    },

    "pvc_hose_plasticizers_drinking_water": {
        "material_a": "PVC-Schlauch (Trinkwasser-Standard DIN 61)",
        "material_b": "Trinkwasser (Frischwasser)",
        "connection_type": "Langzeitlagerung, Wasser-Durchfluss",
        "failure_mode": "Weichmacher-Migration → Wasser verdorben, Geschmack/Geruch",
        "onset_years": (0.1, 0.5),  # Monate
        "severity": "niedrig (gesundheitlich gering, aber qualitativ schlecht)",
        "mechanism": (
            "PVC ist hart und spröde ohne Weichmacher. Phthalate (DEHP, DBP, etc.) oder "
            "Citrate werden zu 30–50 % zugesetzt, um Flexibilität zu geben. "
            "In Trinkwasser (schwach sauer, pH 6,5–7,5) diffundieren diese Weichmacher "
            "langsam aus dem Kunststoff in das Wasser. Permeation ist Temperatur-abhängig. "
            "Nach Monaten: Wasser schmeckt nach Kunststoff, Geruch nach Phthalaten (süßlich). "
            "Langzeitfolgen: unklar, aber unerwünscht."
        ),
        "detection_method": (
            "Organoleptische Prüfung: Geschmack und Geruch des Wassers (süßlich, chemisch). "
            "Chemische Analyse: HPLC oder GC-MS für Phthalate im Wasser. "
            "Langzeitbeobachtung: Wasser lagert wöchenlang → Geruch entwickelt sich."
        ),
        "prevention": (
            "BESTE LÖSUNG: PVC-Schläuche mit NICHT-PHTHALAT Weichmachern wählen "
            "(z.B. DINCH, Citrate, Paraffinöl). Etwas teurer, aber sicher. "
            "ODER: Alternativer Schlauchtyp für Trinkwasser: Polyurethan, EPDM, oder FKM. "
            "Schlauch-Lagerung: Kühl (<10°C) und dunkel (UV verhindert Weichmacher-Freisetzung). "
            "Spülung: Vor Saison Schläuche mehrmals durchspülen (entfernt Weichmacher-Ansammlung). "
            "Wechsel: PVC-Wasserschläuche alle 3–5 Jahre tauschen (Weichmacher erschöpft sich). "
            "Trinkwasser in Poly-Kanister lagern, nicht im PVC-Schlauch."
        ),
    },
}


# ==============================================================================
# CUMULATIVE DEGRADATION CYCLES — Selbstverstärkende Kreisläufe
# ==============================================================================

CUMULATIVE_DEGRADATION_CYCLES = {
    "moisture_seal_failure_cycle": {
        "name_de": "Undichtigkeit → Kernfeuchte → Steifigkeitsverlust → mehr Flexion → mehr Undichtigkeit",
        "name_en": "Seal Failure → Core Moisture → Stiffness Loss → More Flexion → More Seal Failure",
        "trigger": "Erste Risse in Gelcoat oder Dichtmasse (Sikaflex-Risse, Kriechrisse)",
        "steps": [
            "Wasser dringt durch Risse in den Sandwich-Kern ein (Balsa, PVC-Schaum).",
            "Feuchtegehalt im Kern wächst: 5 % → 10 % → 20 % (je nach Kern-Typ).",
            "E-Modul des Kerns sinkt exponentiell: 10 GPa → 5 GPa → <2 GPa.",
            "Rumpf-Durchbiegung (Sagging) wächst unter statischer Last (eig. Gewicht) um 5–15 mm.",
            "Dynamische Flexion bei Seegang verstärkt sich (größere Amplituden).",
            "Spannungen in Gelcoat und Dichtmassen wachsen überproportional.",
            "Risse wachsen länger und tiefer (Stress-Rissbildung, Microcracking).",
            "Mehr Wasser dringt ein → Kern quillt noch mehr → noch weniger Steifigkeit.",
            "Nach 2–5 Jahren: Kern in kritischen Bereichen praktisch strukturlos.",
            "Strukturelles Versagen (Bersten des Rumpfes, Spant-Bruch) oder schleichender Lecka."
        ],
        "acceleration_factors": [
            "Wärmezyklus (Tag/Nacht): Dehnung/Kontraktion wächst Risse",
            "Frost-Zyklus (wenn relevant): Eis-Expansion sprengt Zellen",
            "UV-Degradation der Gelcoat: Risse entstehen schneller",
            "Tropisches Klima: 3x schneller Wasseraufnahme wegen Wärme/Feuchte",
            "Kleine Beschädigungen (Anker-Kratzer, Stoß beim Anlegen): Initiatoren für Risse",
            "Mangelnde Wartung: Risse werden nicht repariert, nur größer"
        ],
        "detection_difficulty": "Schwierig. Kern-Feuchte ist optisch nicht sichtbar, bis Delaminationen offensichtlich sind.",
        "typical_onset_years": 3,
        "catastrophic_if_unchecked": True,
    },

    "osmosis_microcrack_cycle": {
        "name_de": "Osmose → Mikrorisse → mehr Wasseraufnahme → Harzkorrosion → Festigkeitsverlust",
        "trigger": "Osmose-Blasen treten auf (nach 5–15 Jahren je nach Harz-Typ)",
        "steps": [
            "Osmotischer Druck wölbt Gelcoat nach außen → Blasen entstehen.",
            "Oberflächen-Spannungen in der Gelcoat werden konzentriert.",
            "Mikrorisse entstehen in der Gelcoat (Risse <0,1 mm, mit Lupe sichtbar).",
            "Wasser dringt durch Risse direkt in Laminat-Schichten ein.",
            "Wassermoleküle lösen Glycole und Säure-Reste auf (diese sind osmotisch aktiv).",
            "Neue osmotische Zentren entstehen tiefer im Laminat.",
            "Polyester-Kettenbindungen hydrolysieren → Essigsäure + andere organische Säuren.",
            "Säure katalysiert weitere Hydrolyse → Harz wird kristallin/spröde.",
            "Fasern verlieren Haft zum Harz (Scherfestigkeit fällt >40 %).",
            "Blasen werden größer, Oberfläche wird wellig/rau.",
            "Zerstörerischer Prozess: Unkontrolliertes Wachstum bis zur Delaminierung."
        ],
        "acceleration_factors": [
            "Höhere Temperatur: Diffusion 2x schneller je 10°C",
            "Tropisches Klima: 3x schneller gesamtprozess",
            "Orthophthal-Harz: Schneller (5–10 Jahre) vs. Isophthal (10–15 Jahre)",
            "Gelcoat-Qualität: Schlecht → schneller Prozess",
            "Keine UV-Schutz-Deckschicht: Gelcoat brüchig → schneller Wasser-Eindringung",
            "Thermische Zyklen: Mehr Risse → mehr Wasser-Eindringung"
        ],
        "detection_difficulty": "Mittel. Blasen sind sichtbar nach Haul-Out (SOFORT!, verschwinden in 1–2 Tagen).",
        "typical_onset_years": 7,
        "catastrophic_if_unchecked": True,
    },

    "corrosion_fastener_seal_failure": {
        "name_de": "Korrosion lockert Beschlag → mehr Bewegung → Dichtstoff reißt → mehr Korrosion → Bruch",
        "trigger": "Galvanische Korrosion oder Rost von Befestigungselementen in Salzwasser-Umgebung",
        "steps": [
            "Beschlag (z.B. Edelstahl auf Aluminium) korrodiert galvanisch.",
            "Korrosionsprodukte lagern sich ab (volumetrisch >2x größer).",
            "Ring aus Al₂O₃ sprengt Dichtmasse-Fugen.",
            "Dichtmasse (z.B. Sikaflex) reißt auf → nicht mehr wasserdicht.",
            "Wasser läuft entlang Schraube in darunter liegende Strukturen.",
            "Holzkernschwellung (Balsa) oder PVC-Schaum-Quellung unter Dichtmasse.",
            "Beschlag sitzt locker, beginnt zu wackeln.",
            "Bewegung verstärkt Dichtmasse-Risse → mehr Wasser.",
            "Korrosion der Schraube selbst verstärkt sich (unter Druck durch Quellung).",
            "Nach einigen Jahren: Beschlag kann mit Kraft von oben herausgezogen werden → Lecka"
        ],
        "acceleration_factors": [
            "Seewasser (hoher Salzgehalt): Korrosion 10x schneller als Süßwasser",
            "Galvanische Paarung (noble Metalle neben Aluminium): Großer Potentialunterschied",
            "Temperatur: Korrosion exponentiell mit Temperatur",
            "Bewegung des Schiffes: Beschlag vibriert → Dichtmasse-Ermüdung",
            "Unzureichende Isolation (fehlende Unterlegscheibe).",
            "UV-Degradation der Dichtmasse: Wird spröde → reißt unter Belastung"
        ],
        "detection_difficulty": "Mittel. Korrosions-Aureole ist sichtbar; Dichtmasse-Risse mit Lupe.",
        "typical_onset_years": 4,
        "catastrophic_if_unchecked": True,
    },

    "mold_humidity_decay_cycle": {
        "name_de": "Schimmel → Feuchtigkeit → mehr Schimmel → Holzfäule",
        "trigger": "Unzureichende Lüftung in feuchten Bereichen (Kabine, Bilge, Schrank)",
        "steps": [
            "Relative Feuchte >70 % in geschlossener Kabine.",
            "Schimmelpilz-Sporen (ubiquitär in Luft) keimen auf organischen Materialien (Holz, Teak, Baumwolle).",
            "Schimmel produziert Feuchte als Metabolit (Schwitzwasser).",
            "Relative Feuchte steigt lokal auf 95–99 % rund um Schimmel-Befall.",
            "Diese Feuchte ermöglicht schnellere Spore-Keimung → mehr Schimmel.",
            "Schimmel-Ausscheidungen (Säuren, Enzyme) zerstören Holz-Struktur.",
            "Holzfäule beginnt: Zellwandabbau durch Pilz-Enzyme.",
            "Holzfeuchte wächst: Trockenes Holz 12 % → Schimmelbefallenes Holz 25–30 %.",
            "Holz-Festigkeit sinkt dramatisch (50–80 % Reduktion bei Fäule).",
            "Visuell: Braun/Schwarz-Flecken, Verweichung, Fruchtköper-Ausbildung."
        ],
        "acceleration_factors": [
            "Temperatur >20°C: Pilz-Wachstum exponentiell",
            "Tropisches Klima: 25–30°C, 80–90 % Feuchte → ideale Bedingungen",
            "Stagnant air: Feuchte staut sich, Belüftung fehlt",
            "Dunkle Bereiche: Pilze bevorzugen Dunkelheit",
            "Chlor im Holz (Teak-Gerbstoffe, Kupfer-AF): Kann Pilz-Wachstum hemmen, aber auch verstärken",
            "Biologische Verschmutzung (Algen, Bakterien): Bilden Substrat für Pilz-Keimung"
        ],
        "detection_difficulty": "Einfach. Schimmel ist optisch offensichtlich; Geruch charakteristisch (muffig).",
        "typical_onset_years": 2,
        "catastrophic_if_unchecked": True,
    },

    "stray_current_corrosion_cycle": {
        "name_de": "Stray Currents → Korrosion → Isolationsverlust → mehr Stray Currents",
        "trigger": "Defektes Ladegerät oder fehlerhafte Elektroinstallation in Nähe von Metall-Rumpf",
        "steps": [
            "Wechselstrom-Leck (oder Gleichstrom-Isolationsfehler) im Bordnetz.",
            "Strom fließt nicht durch Verdrahtung, sondern durch alternative Pfade: Meerwasser, Metallrumpf.",
            "Rumpf-Metall wird zur Anode in diesem parasitären Kreis.",
            "Lokale Stromdichte an Schwachstellen (Risse, Ablösungen) wird sehr hoch.",
            "Korrosion beschleunigt sich exponentiell (mA/cm² statt µA/cm²).",
            "Korrosions-Produkte (Fe₂O₃, Al₂O₃) bilden isolierende Schichten → Widerstand steigt.",
            "Bordnetz versucht Widerstand zu überbrücken → Strom wächst weiter.",
            "Isolierung der Verdrahtung degradiert (Wärmestress durch hohen Strom).",
            "Neue Leck-Pfade entstehen in der Elektrik → noch mehr Stray Currents.",
            "Rumpf entwickelt großflächige Lochfraß-Korrosion → potentieller Durchbruch."
        ],
        "acceleration_factors": [
            "Seewasser (hohe Leitfähigkeit): Besserer Strompfad",
            "Mangelnde Galvanische Isolation: Kein Isolietrafo im Landanschluss",
            "Defekte Ladegeräte: Alte 3-Draht-Geräte ohne Isolation",
            "Verwitterte Kabel: Isolierung brüchig, Feuchte dringt ein",
            "Hochfrequenz-Störungen (WLAN, Radar): Können auch capacitiv koppeln",
            "Unbekannte Fehlerquellen: Schwer zu diagnostizieren, Strom fließt weiter"
        ],
        "detection_difficulty": "Schwierig. Erfordert Multimeter und Verständnis von AC-Leck-Prüfung.",
        "typical_onset_years": 1,
        "catastrophic_if_unchecked": True,
    },

    "osmotic_blister_hyphothesis_cycle": {
        "name_de": "Osmose-Blase → Harzabbau → Säure → mehr Osmose → strukturelles Versagen",
        "trigger": "Zunächst unerkannte Osmose (5–10 Jahre incubation period)",
        "steps": [
            "Gelcoat und Laminat enthalten Glycol- und Styrol-Reste (Herstellungs-Nebenprodukte).",
            "Wasserdiffusion durch Gelcoat etabliert sich nach einigen Jahren Meerwasser-Kontakt.",
            "Wasser konzentriert sich in Harz-Poren → osmotische Zentren entstehen.",
            "Wasserdruck drückt Gelcoat nach außen → optisch sichtbare Blasen.",
            "Blasen-Inhalt ist sauer (pH 3–4) wegen Essigsäure und anderen Säuren.",
            "Saure Flüssigkeit katalysiert Polyester-Harz-Hydrolyse: [—CO—O—] + H₂O → [—COOH] + [—OH].",
            "Harz-Bruch-Zähigkeit sinkt (Esterbindungen zerstört).",
            "Neue Risse entstehen rund um Blasen (Spannungskonzentration).",
            "Risse sind Wasser-Eintrittspforten → mehr Wasser-Eindringung → mehr osmotische Zentren.",
            "Proliferation: Hunderte von Blasen entstehen → Oberfläche wird wellig.",
            "Laminat-Integrität versagt: Fiber-Haft ist zerstört → strukturelles Versagen möglich."
        ],
        "acceleration_factors": [
            "Orthophthal-Harz: Schneller (~5–10 Jahre bis Blasen) vs. Isophthal (10–15 Jahre)",
            "Tropisches Klima: 3x schneller",
            "Hohe Temperatur: Diffusion 2x schneller je 10°C",
            "Schlechte Gelcoat-Qualität: Mehr Glykolrückstände",
            "Keine Epoxid-Barriere: Direkter Wasser-Kontakt mit Polyester",
            "UV-Degradation: Gelcoat wird porös, mehr Wasser-Eindringung"
        ],
        "detection_difficulty": "Einfach nach Blasen-Bildung (sichtbar nach Haul-Out, aber zeitabhängig: verschwinden 1–2 Tage nach Aufzug!)",
        "typical_onset_years": 9,
        "catastrophic_if_unchecked": True,
    },
}


# ==============================================================================
# HIDDEN MOISTURE PATHS — Versteckte Feuchtigkeitspfade (min 12)
# ==============================================================================

HIDDEN_MOISTURE_PATHS = {
    "screw_in_sandwich_deck": {
        "location_de": "Jede Schraube durch Sandwich-Deck",
        "mechanism": "Schraube durchbricht Oberflächenschicht (Gelcoat/Laminat). Kapillare um die Schraube. Wasser läuft entlang des Kunststoff-Gewindes ins Innere des Kerns.",
        "detection_method": "Kernfeuchte-Messung durch Bohrung neben Schraube. Drucktest: Kern zu weich?",
        "spread_radius_cm": 15,
        "severity": "hoch",
        "prevention": "Alle Schrauben mit Epoxid-Harz voll-kaltvergießen oder Sikaflex-Dichtung. Alternativ: Unterlegscheibe + Dichtring.",
    },

    "chainplate_penetration": {
        "location_de": "Durchführung von Salingstag durch Deck (Ketten-Platte)",
        "mechanism": "Bolzen durchbricht Deck. Rost oder Korrosion unter dem Beschlag. Wasser läuft entlang des Bolzens oder unter der Unterlegscheibe ins Deck.",
        "detection_method": "Sichtprüfung unter Beschlag nach Haul-Out. Kern-Feuchtemessung. Druck-Test: Deck quillt um Beschlag.",
        "spread_radius_cm": 20,
        "severity": "kritisch",
        "prevention": "Edelstahl 316 Bolzen, Isolier-Unterlegscheibe, Epoxid-Grundierung unter Beschlag, Dickmaß-Kontrolle nach 5 Jahren.",
    },

    "mast_step_penetration": {
        "location_de": "Mast-Fuß-Durchführung (Mast-Stützung auf Deck oder Kiel)",
        "mechanism": "Großflächige Kontakt-Zone zwischen Mast-Flansch und Deck. Bewegung des Mastes (Vibrationen) erzeugt Mikrorisse in der Dichtung. Salzwasser sammelt sich, dringt ins Deck ein.",
        "detection_method": "Druck-Prüfung des Decks um Mast. Thermographie nach Regen (feuchter Bereich). Kernfeuchte-Messung.",
        "spread_radius_cm": 30,
        "severity": "kritisch",
        "prevention": "Epoxid-Grundierung auf Mast-Flansch und Deck-Bereich. Sikaflex 298 oder 290DC Dichtung (nicht Polyurethane). Jährliche Kontrolle und ggf. Nachbearbeitung.",
    },

    "cable_throughhole": {
        "location_de": "Durchgänge für Kabel (Strom, Antenne, Daten) durch Rumpf",
        "mechanism": "Kabel-Durchgang ist dichter als ein starres Loch. Aber: Kabel-Isolierung kann reißen (Bewegung, Hitze). Wasser folgt dem Kabel ins Schiff.",
        "detection_method": "Sichtprüfung: Wasser um Kabel-Durchgang? Feuchte-Sensor im Inneren.",
        "spread_radius_cm": 8,
        "severity": "mittel",
        "prevention": "Kabel-Nabe mit Epoxid-Gießharz vergießen (nicht Polyester). Oder: Kunststoff-Kabeldurchführung mit Dichtring. Alle 3 Jahre: Kontrolle der Gießharz-Dichtheit.",
    },

    "deck_hardware_fastening": {
        "location_de": "Befestigungen von Deck-Hardware (Stagen, Wanten, Blöcke, Nock-Halter)",
        "mechanism": "Unterlegscheibe und Schraube bilden eine kleine 'Wanne'. Wasser sammelst sich. Wenn keine Abdichtung, dringt Wasser direkt in Sandwich-Kern ein.",
        "detection_method": "Sichtprüfung: Wasser-Flecken um Hardware? Druck-Test der Unterkonstruktion.",
        "spread_radius_cm": 12,
        "severity": "mittel-hoch",
        "prevention": "Alle Unterlegscheiben mit Dichtring (Gummi oder Kunststoff). Dichtmasse (Sikaflex oder Butyl) unter Scheibe und Schraube. Jährliche Überprüfung.",
    },

    "gelcoat_cracks_at_windows": {
        "location_de": "Risse in Gelcoat um Fenster/Bullaugen (Spannungskonzentration)",
        "mechanism": "Fenster hat andere Steifigkeit als Deck. Flexion erzeugt Spannungen. Gelcoat reißt. Mikrorisse sind Wasserwege.",
        "detection_method": "UV-Lampe zeigt Risse. Oberflächenrauheits-Prüfung. Wasser-Eindringung führt zu Blasen darunter (nach Haul-Out sichtbar).",
        "spread_radius_cm": 10,
        "severity": "mittel",
        "prevention": "Fenster mit flexiblem Dichtstoff (Sikaflex) statt rigid montieren. Spannungs-verteilung durch Gummi-Dichtring. Alle 3 Jahre: Dichtstoff-Kontrolle und Nachbearbeitung.",
    },

    "stern_tube_seawater_seal": {
        "location_de": "Wellendichtung am Stern-Rohr (wo Welle durch Rumpf geht)",
        "mechanism": "Dichtung ist verschleißteil. Nach 5–10 Jahren lockert sie sich. Meerwasser tritt ein oder folgt dem Öl-Film entlang der Welle.",
        "detection_method": "Kammer-Inspektion: Wasser um Dichtung? Öl-Emulsion in Bilge? Druck-Test (Wasser-Eintritt).",
        "spread_radius_cm": 20,
        "severity": "kritisch (Untergang-Risiko)",
        "prevention": "Wellendichtung alle 5 Jahre ersetzen (Verschleiß-teil). Qualitäts-Abdichtungen verwenden (z.B. PSS Shaft Seal). Ölbad-Kammer unter Kontrolle (Schmiermittel ausreichend?).",
    },

    "cockpit_drain_holes": {
        "location_de": "Abfluss-Löcher in Cockpit-Sohle oder Pumpentanks",
        "mechanism": "Abflusslöcher verstopfen (Algen, Sediment, Müll). Wasser staut sich. Sickert durch Bohrungen ins Deck. Oder: Schlauch-Verbindung reißt, Wasser läuft ins Deck statt nach außen.",
        "detection_method": "Sichtprüfung: Ist Cockpit-Abfluss frei? Wasser-Test: Gießt Wasser in Cockpit, läuft es ab? Kernfeuchte-Messung unter Cockpit-Sohle.",
        "spread_radius_cm": 25,
        "severity": "hoch",
        "prevention": "Abflusslöcher regelmäßig freispülen (1x pro Monat). Schläuche alle 5 Jahre prüfen und ggf. tauschen. Rückstau-Klappen prüfen (verstopft?).",
    },

    "capillary_action_along_fibers": {
        "location_de": "Kapillarwirkung entlang von Glasfasern oder Kevlar-Fasern im Laminat",
        "mechanism": "Fasern sind poröse Strukturen. Wasser wird durch Kapillarwirkung ins Laminat gezogen. Kann über 50 cm wandern, wenn nicht unterbrochen.",
        "detection_method": "Feuchte-Prüfung durch Kernbohrung. Laminat-Färbung (dunkler, wenn nass).",
        "spread_radius_cm": 50,
        "severity": "mittel",
        "prevention": "Faser-Sperr-Barrieren verwenden (Kunststoff-Film zwischen Schichten). Oder: Vakuum-Infusion (bessere Harz-Faser-Penetration, weniger Poren).",
    },

    "cable_penetration_along_wire": {
        "location_de": "Wasserwanderung entlang von Strom-/Antennenkabeln ins Schiffsinnnere",
        "mechanism": "Kabel-Isolierung ist porös. Kapillare treibt Wasser entlang des Drahtes. Kann 10+ Meter ins Schiff eindringen.",
        "detection_method": "Feuchtigkeit in Endverbrauchern (Pumpen, Instrumente). Fehlerhafte Elektrik nach Regen.",
        "spread_radius_cm": 1000,  # Kann bis zum anderen Ende des Schiffs gehen
        "severity": "hoch (Elektrik-Ausfälle möglich)",
        "prevention": "Kabel in Kunststoff-Rohr (Schutzrohr) führen. Oder: Wasserdichte Kabel-Nabe mit Epoxid-Verguss. Kabel-Management: Abwärts-Verlegung mit Tropfenschleife am unteren Ende.",
    },

    "adhesive_joint_delamination": {
        "location_de": "Delaminationen entlang von Klebefugen (zwischen Laminat-Schichten oder Sandwich-Kern)",
        "mechanism": "Kleber (z.B. Epoxid oder Polyurethan) haftet nicht perfekt auf feuchter Oberfläche. Oder: Langzeitbelastung löst Haft. Spalt zwischen Schichten wird zu Wasserbahn.",
        "detection_method": "Ultraschall-Prüfung: Delaminationen sichtbar. Druck-Test: Schichten bewegen sich relativ zueinander.",
        "spread_radius_cm": 30,
        "severity": "hoch (Strukturelle Integrität gefährdet)",
        "prevention": "Oberflächen-Vorbereitung: Trocken und sauber vor Klebung. Epoxid-Kleber mit Haftverstärkern verwenden. Temperatur-Management während Aushärtung (richtige Härtungs-Temperatur = bessere Haft).",
    },

    "fastener_corrosion_micro_leak": {
        "location_de": "Mikro-Undichtigkeit rund um korrodierte Befestigungselemente",
        "mechanism": "Rost-Produkte bilden eine lockere, poröse Schicht. Diese hat keine Dicht-Eigenschaft. Wasser kann hindurch dringen (wie durch Sand-Filter).",
        "detection_method": "Sichtprüfung: Rost-Halo um Befestigungselement? Druck-Test: Undichtheit prüfen. Kernfeuchte-Messung.",
        "spread_radius_cm": 15,
        "severity": "mittel",
        "prevention": "Hochwertige Befestigungselemente (Edelstahl 316, nicht 304). Isolation zwischen unedlen und edlen Metallen. Regelmäßige Kontrolle und Austausch korrodierter Teile.",
    },

    "osmotic_network_expansion": {
        "location_de": "Netzwerk von osmotischen Zentren, die sich ausbreiten (nicht lokalisiert auf eine Stelle)",
        "mechanism": "Osmose beginnt lokal (eine Blase). Dann breitet sich aus, bildet weitere Blasen. Nach Jahren ist große Rumpf-Fläche betroffen.",
        "detection_method": "Nach Haul-Out: Blasen-Zählung und -Verteilung. Thermographie: Temperatur-Unterschiede zeigen Blasen-Bereiche.",
        "spread_radius_cm": 200,  # Kann gesamten Rumpf befallen
        "severity": "kritisch (großflächig)",
        "prevention": "Früherkennung essentiell: Jährliche Haul-Out und Blasen-Inspektion. Sofortige Behandlung bei ersten Blasen (Gelcoat-Peeler, Trocknung, Vinylester-Relaminierung). Präventiv: Vinylester-Barriere bei Neubau.",
    },
}


# ==============================================================================
# CHEMICAL INCOMPATIBILITIES — Chemische Unverträglichkeiten
# ==============================================================================

CHEMICAL_INCOMPATIBILITIES = [
    {
        "material_a": "Polyester-Harz",
        "material_b": "Polystyrol-Schaumkern (z.B. XPS-Foam, expandiertes Polystyrol)",
        "incompatibility": "Styrol (Verdünner in Polyester) löst Polystyrol auf",
        "consequence": "Kern kollabiert lokal bereits während Laminierung oder kurz danach",
        "severity": "kritisch",
        "solution": "Polyester niemals auf XPS verwenden. Balsa, PVC-Schaum oder Polyurethan-Kern statt dessen. Oder: Kern mit Barriere-Schicht (Epoxid/PU 0,5 mm) vor Polyester-Laminierung versiegeln.",
    },
    {
        "material_a": "Silikon-Dichtmasse",
        "material_b": "Lackschichten (Acryl, Polyurethan, Epoxid)",
        "incompatibility": "Silikon verhindert Lack-Haftung (schlechte Benetzung)",
        "consequence": "Lack blättert ab, silikon bleibt klebrig",
        "severity": "mittel",
        "solution": "Silikon und Lack räumlich trennen. Oder: Spezial-Silikon mit besserer Lack-Haftung verwenden (z.B. haftungsvermittelnd). Vor Lackierung: Silikon-Oberfläche mit Lösemittel reinigen.",
    },
    {
        "material_a": "Butylkautschuk-Dichtmasse",
        "material_b": "Polycarbonat (Fenster, Türen, Abdeckungen)",
        "incompatibility": "Butyl kann Polycarbonat aufquellen (Plastifizierung)",
        "consequence": "Polycarbonat verliert Transparenz, wird milchig/porös",
        "severity": "mittel",
        "solution": "Butyl nicht direkt auf Polycarbonat auftragen. Unterlegscheibe aus Kunststoff (EPDM, Neopren) zwischenlegen. Oder: Spezial-Dichtmasse für Polycarbonat verwenden (z.B. Polyurethan, Sikaflex).",
    },
    {
        "material_a": "Teak-Holz (Gerbsäuren, Tannine)",
        "material_b": "Edelstahl 316 (unter feuchter Bedingung)",
        "incompatibility": "Tannine (in Teak) katalysieren Spaltkorrosion von Edelstahl",
        "consequence": "Schrauben unter Teak-Planken korrodieren trotz Edelstahl",
        "severity": "hoch",
        "solution": "Teak-Öl mit Konservierungsmittel wählen (verhindert Tannin-Freisetzung). Oder: Schrauben mit Epoxydharz-Beschichtung. Oder: Teak-Barriere-Folie (Kunststoff) unter Teakplanken legen. Alle 5 Jahre: Kontrolle der Schraubenlöcher.",
    },
    {
        "material_a": "PVC-Schlauch (mit Phthalat-Weichmachern)",
        "material_b": "Trinkwasser",
        "incompatibility": "Phthalate (Weichmacher) migrieren in Wasser",
        "consequence": "Wasser bekommt Plastikgeschmack/Geruch, gesundheitliche Unbedenklichkeit unklar",
        "severity": "niedrig-mittel",
        "solution": "PVC-Schläuche mit Nicht-Phthalat-Weichmachern wählen (DINCH, Citrate). Oder: Polyurethan/EPDM-Schlauch. Wasserlagering in Polyethylen-Kanister statt PVC-Schlauch.",
    },
    {
        "material_a": "Epoxid-Harz",
        "material_b": "Feuchte Oberfläche (Gelcoat mit Feuchte)",
        "incompatibility": "Epoxid haftet schlecht auf feuchten Flächen (Wasser als Trennschicht)",
        "consequence": "Epoxid-Schicht delaminiert oder haftet oberflächlich",
        "severity": "hoch",
        "solution": "Oberfläche VOR Epoxid-Auftrag vollständig trocknen (>48 Stunden, <60 % RH). Oder: Epoxid wet-on-wet auf feuchtem Untergrund auftragen (schnell arbeiten, bevor Feuchtigkeit eindiffundiert). Grundierung mit Primer verwenden (bessere Haftung auch auf feuchtem Untergrund).",
    },
    {
        "material_a": "Acryl-Verdünner",
        "material_b": "PVC-Schaumkern",
        "incompatibility": "Acryl-Verdünner (Aceton, Ethanol) löst PVC-Binder auf",
        "consequence": "Kern wird weich, quillt, verliert Festigkeit",
        "severity": "kritisch",
        "solution": "Acryl-haltige Farben NIEMALS in der Nähe von PVC-Kernbereichen verwenden. Oder: Kern mit Epoxid-Barriere schützen vor Farb-Verdampfung. Lüftung ausreichend während Farbarbeiten.",
    },
    {
        "material_a": "Kupfer-Antifouling",
        "material_b": "Aluminium-Rumpf (ohne Isolation)",
        "incompatibility": "Galvanisches Paar Cu/Al mit großem Potentialunterschied (~1100 mV)",
        "consequence": "Schneller Lochfraß in Aluminium (Wochen bis Monate)",
        "severity": "kritisch",
        "solution": "Cu-AF niemals direkt auf Alu auftragen. Isolation essentiell: Epoxid-Grundierung (min. 100 µm) auf Alu vor Cu-AF. Oder: Zinn-AF oder Cu-freie AF-Varianten. Oder: Opferschicht (Zink/Magnesium-Band) anbringen.",
    },
    {
        "material_a": "Polyurethan-Kleber (2K)",
        "material_b": "Nasse oder feuchte Oberflächen",
        "incompatibility": "Polyurethan reagiert mit Wasser unter Bildung von Gasblasen (Schäumen)",
        "consequence": "Kleber-Qualität verschlechtert sich (Voids, schlechte Haftung)",
        "severity": "mittel",
        "solution": "Vor Klebung: Oberfläche trocken halten. Oder: Epoxid-Kleber verwenden (weniger wassersensitiv). Oder: Spezial-Polyurethan-Kleber (feuchtigkeitstolerante Formulierung).",
    },
    {
        "material_a": "Graphit oder Carbon-Leitpaste",
        "material_b": "Edelstahl oder Kupfer-Verdrahtung",
        "incompatibility": "Galvanisches Paar mit potentieller Korrosion (Carbon ist edel)",
        "consequence": "Stahl/Kupfer korrodiert lokal unter Graphit-Schicht",
        "severity": "mittel",
        "solution": "Graphit und Metall isolieren (Kunststoff-Unterlegscheibe). Oder: Graphit mit Epoxid-Grundierung auf Metall aufbringen (Barriere). Oder: Spezial-Graphit-Produkte mit Korrosionsschutz verwenden.",
    },
]


# ==============================================================================
# OSMOSIS KNOWLEDGE — Complete Osmosis Knowledge Base
# ==============================================================================

OSMOSIS_KNOWLEDGE = {
    "mechanism": {
        "description": "Osmose in Polyester-Bootsskeletten: Ein Prozess, bei dem Wassermoleküle durch die Gelcoat-Barriere ins Harz diffundieren, um Konzentrations-Unterschiede auszugleichen.",
        "detailed_mechanism": (
            "1. INITIAL WASSER-DIFFUSION:\n"
            "   - Gelcoat ist nicht vollkommen wasserdicht (Wasserdampf-Permeation nach ISO 2409).\n"
            "   - Wassermoleküle diffundieren kontinuierlich durch Gelcoat in das Laminat.\n"
            "   - Diffusions-Geschwindigkeit: ~0,1–0,5 mm/Jahr (abhängig von Gelcoat-Dicke und Qualität).\n\n"
            "2. LÖSUNGSMITTEL-RESTE IM HARZ:\n"
            "   - Polyester-Harz enthält Glykolrückstände (bei der Synthese: Diesters oder Polyole).\n"
            "   - Auch Styrol-Reste (Verdünner, teilweise unreagiert).\n"
            "   - Diese Stoffe sind HYDROPHIL (ziehenWasser an).\n"
            "   - Sie bilden osmotische Zentren: hohe lokale Wasser-Konzentration.\n\n"
            "3. OSMOTISCHER DRUCK:\n"
            "   - Konzentrations-Gradient: Glykolreiche Zone im Harz vs. reines Wasser außen.\n"
            "   - Osmotischer Druck π = i × R × T × c (van't Hoff-Gleichung).\n"
            "   - Typischer Druck: 1–50 atm (je nach Glykolkonzentration).\n"
            "   - Wasser fließt aktiv IN die Glykolzone, um Konzentration auszugleichen.\n\n"
            "4. BLASEN-BILDUNG:\n"
            "   - Lokale Wasser-Akkumulation in Poren/Defekten des Laminats.\n"
            "   - Druck wölbt die Gelcoat nach außen → sichtbare Blasen (Durchmesser 2–20 mm, Tiefe 0,5–3 mm).\n\n"
            "5. HARZ-CHEMISCHE FOLGEN (SEHR WICHTIG):\n"
            "   - Wasser-Gehalt im Harz: 5 % → 10 % → 20 % (über Jahre).\n"
            "   - Polyester-Ketten enthalten Ester-Bindungen: —(O—CO—O)—.\n"
            "   - Wasser katalysiert Hydrolyse dieser Bindungen (besonders in saurer Umgebung):\n"
            "     —O—CO—O— + H₂O + H⁺ → —COOH + —OH (reversible erste, dann irreversible Kettenbindungs-Bruch).\n"
            "   - Hydrolyse-Produkte: Essigsäure, Formaldehyd, andere Carbonsäuren.\n"
            "   - Diese Säuren senken lokalen pH auf 3–4 → verstärken Hydrolyse (selbstbeschleunigend!).\n"
            "   - Harz-Struktur wird kristallin, spröde, verliert Scherfestigkeit >40 %.\n\n"
            "6. LANGZEIT-EVOLUTION:\n"
            "   - Nach 5–15 Jahren: Harz in blasen-Bereich praktisch völlig hydrolysiert.\n"
            "   - Faser-Haft-Stärke sinkt um 50–80 %.\n"
            "   - Rumpf-Steifigkeit kann signifikant abnehmen (besonders bei Sandwich-Konstruktion)."
        ),
    },

    "onset_by_resin_type": {
        "orthophthal_polyester": {
            "name": "Orthophthal-Polyester (Standard)",
            "onset_years": (5, 10),
            "description": "Schnellste Osmose-Entwicklung. Orthophthal-Harz enthält mehr Hydroxyl-Gruppen, höhere Hydrophilie.",
            "typical_tropical": (3, 5),
            "typical_temperate": (7, 12),
            "typical_cold": (10, 20),
        },
        "isophthal_polyester": {
            "name": "Isophthal-Polyester (höherwertig)",
            "onset_years": (10, 15),
            "description": "Langsamere Osmose. Bessere Struktur, weniger Glykolrückstände. Isophthal-Struktur ist weniger hydrophil als Orthophthal.",
            "typical_tropical": (6, 10),
            "typical_temperate": (10, 18),
            "typical_cold": (15, 30),
        },
        "vinylester_resin": {
            "name": "Vinylester-Harz",
            "onset_years": "praktisch nie",
            "description": "Vinylester-Ketten enden mit Vinyl-Gruppen (—CH=CH₂), nicht Hydroxyl-Gruppen. Viel weniger hydrophil. Osmose-Resistenz ist primärer Vorteil.",
            "notes": "Osmose-Blasen treten nicht auf. Kann aber andere Schäden erleiden (UV-Spröde, Delaminationen).",
        },
        "epoxy_resin": {
            "name": "Epoxid-Harz",
            "onset_years": "praktisch nie",
            "description": "Epoxide sind hochvernetzt (3D-Struktur), weniger Wasser-Diffusion. Sehr gute Wasser-Resistenz.",
            "notes": "Wird statt dessein als Barriere-Schicht verwendet (Vinylester-alternativ).",
        },
    },

    "tropical_acceleration": {
        "factor": 3,
        "description": "Osmose 3x schneller in tropischen Gewässern (>25°C, hohe Feuchte)",
        "reason": "Diffusions-Koeffizient ∝ exp(Ea/RT). Ea ~40 kJ/mol. 10°C Temperaturanstieg → 2x schneller. Tropisch ca. 15–20°C wärmer → insgesamt 3–4x schneller.",
    },

    "inspection_timing": {
        "critical_note": "BLASEN VERSCHWINDEN 1–2 TAGE NACH HAUL-OUT!",
        "mechanism": "Nach Aufzug: Druck im Kern sinkt (nicht mehr überlagert durch Wasser-Druck). Blasen-Flüssigkeit wird reabsorbiert ins Harz.",
        "consequence": "Inspektion MUSS sofort nach Haul-Out erfolgen, nicht später.",
        "timing": "Ideal: Innerhalb 4 Stunden nach Aufzug, spätestens 24 Stunden. Nach 2 Tagen: Blasen praktisch nicht mehr sichtbar.",
    },

    "prevention_at_build": {
        "method_1_vinylester_barrier": {
            "name": "Vinylester-Barriere-Schicht",
            "description": "Obere 0,5–1,0 mm des Laminats aus Vinylester statt Polyester. Stellt eine wasserdichte Barriere dar.",
            "application": "Erste 1–2 Schichten Glas-Fasern (ca. 100 g/m² pro Schicht) mit Vinylester-Harz laminieren, dann mit Polyester-Harz weiterlaminieren.",
            "effectiveness": "95–100 % Schutz vor Osmose",
            "cost": "Mittel (Vinylester ~20–30 % teurer als Polyester)",
        },
        "method_2_vacuum_infusion": {
            "name": "Vakuum-Infusions-Verfahren",
            "description": "Fasern unter Vakuum mit Harz imprägniert. Ergebnis: Sehr wenige Voids (<5 %), homogene Harz-Verteilung.",
            "application": "Spezielle Werkzeuge notwendig, aber resultierendes Laminat viel besser.",
            "effectiveness": "80–90 % Osmose-Reduktion (weniger Wasser-Eindringungswege)",
            "cost": "Höher (Vakuumanlage, Prozessveränderung)",
        },
        "method_3_npg_gelcoat": {
            "name": "NPG-Gelcoat (Neopentylglykol-Basis)",
            "description": "Gelcoat ohne Glykolrückstände (oder minimal). NPG ist weniger hydrophil als Standard-Glykole.",
            "application": "Erste Gelcoat-Schicht ausschließlich NPG, dünn (0,3–0,5 mm).",
            "effectiveness": "70–85 % Osmose-Reduktion",
            "cost": "Niedrig-mittel (Gelcoat ~10 % teurer)",
        },
        "method_4_epoxy_barrier_coat": {
            "name": "Epoxid-Barriere-Coat, Wet-on-Wet",
            "description": "Nach Polyester-Laminierung, solange Harz noch nicht vollständig ausgehärtet: Epoxid-Schicht (min. 200 µm) auftragen.",
            "application": "Kritisches Timing: Polyester muss noch klebrig sein (etwa 4–8 Stunden nach Laminierung), dann Epoxid wet-on-wet auftragen.",
            "effectiveness": "85–95 % Schutz",
            "cost": "Mittel (Epoxid teuer, aber dünn aufgetragen)",
        },
    },

    "repair_procedure": {
        "step_1_damage_assessment": "Blasen-Ausmaß bestimmen (Fläche, Anzahl, Tiefe). Bohrung in repräsentativem Blasen-Bereich: Feuchte messen (Holzfeuchte-Messer).",
        "step_2_gelcoat_removal": "Alle sichtbaren Blasen entfernen mittels Gelcoat-Peeler oder Schleifer. Entfernung bis auf gesundes Laminat (ca. 2–3 mm Tiefe). Alle Blasen-Reste müssen raus.",
        "step_3_drying": "KRITISCH: Laminat MUSS vollständig trocknen, bevor weitere Reparatur. Trocknung: 4–12 Wochen (je nach Dicke und Klima). Feuchte-Messung: <12 % Holzfeuchte-Äquivalent. Beheizung/Belüftung kann beschleunigen.",
        "step_4_vinyl_ester_relaminierung": "Auf getrocknete Fläche: Vinylester-Harz auftragen (nicht Polyester!). Neue Glas-Faserverstärkung laminieren (2–3 Schichten, 300–500 g/m²). Ziel: Neue, osmose-resistente Schicht aufbauen.",
        "step_5_epoxy_barrier_coat": "Nach Vinylester-Aushärtung (24 Stunden): Epoxid-Barriere-Coat (min. 200 µm) auftragen. Dies ist letzte Wasserbarriere.",
        "step_6_gelcoat_application": "Schließlich: Standard-Polyester-Gelcoat (weiß oder farbig) auftragen (0,5–1 mm). Schleifen und polieren.",
        "critical_warning": "Bloßes Trocknen und Überstreichen (ohne Relaminierung) ist KEINE Lösung. Blasen werden wiederkommen, weil Osmose-Ursache nicht behoben ist.",
    },
}


# ==============================================================================
# LAMINATE DEFECTS — Laminatfehler Systematik
# ==============================================================================

LAMINATE_DEFECTS = {
    "voids_porosity": {
        "name_de": "Lufteinschlüsse / Poren",
        "cause": "Unzureichend verdrängte Luft während Laminierung, falsche Verdichtung.",
        "detection": "Ultraschall, Röntgen, Bohrung + Sichtprüfung",
        "impact_on_strength": "30–60 % Festigkeitsminderung je nach Void-Größe und -Dichte",
        "severity": "schwer",
        "prevention": "Vakuum-Infusion, Vakuumsack, richtige Verdichtung (Rolle), Belüftung bei Handlaminierung",
    },
    "bridging": {
        "name_de": "Überbrückung / Fiber-Brücken",
        "cause": "Fasern überbrücken Ecken/Mulden in der Form, statt diese auszufüllen. Harz fließt nicht optimal.",
        "detection": "Ultraschall, Bohrung + Inspektion",
        "impact_on_strength": "15–35 % Reduktion (lokale Schwachstellen)",
        "severity": "mittel",
        "prevention": "Form-Design mit Radien (keine scharfen Ecken), Verdichtung, ggf. Kern-Material in Ecken setzen",
    },
    "secondary_bonding_failure": {
        "name_de": "Sekundär-Verklebung / Schicht-Ablösung",
        "cause": "Schlechte Haftung zwischen aufeinanderfolgenden Laminat-Schichten oder zwischen Kern und Außenhaut",
        "detection": "Ultraschall, Druck-Test (Kern hebt sich ab)",
        "impact_on_strength": "40 % Scherfestigkeit-Reduktion (Kern kann abrutschen unter Scherung)",
        "severity": "schwer",
        "prevention": "Oberflächen-Vorbereitung (Schleifen bis matt), richtige Harz-Menge, Härter-Verhältnis korrekt, Aushärtungs-Temperatur",
    },
    "dry_spots": {
        "name_de": "Trockenstellen",
        "cause": "Harz fließt nicht zu allen Fasern, einige Fasern-Bundles bleiben trocken",
        "detection": "Ultraschall zeigt Rückgang (andere Schallgeschwindigkeit), Bohrung",
        "impact_on_strength": "25–50 % Reduktion in betroffenen Bereichen",
        "severity": "schwer",
        "prevention": "Ausreichende Harz-Menge, Verdichtung, Vakuum-Infusion, richtige Faser-Orientierung",
    },
    "wrong_hardener_ratio": {
        "name_de": "Falsche Härtermenge (Polyester/Epoxid)",
        "cause": "Zu wenig Härtermittel: Aushärtung unvollständig. Zu viel: Spröde, Verzug",
        "detection": "Chemische Analyse (FTIR), Härte-Test, Biegung-Test",
        "impact_on_strength": "20–80 % Variabilität der Festigkeit, je nach Abweichung",
        "severity": "mittel-schwer",
        "prevention": "Präzisions-Dosierung (Waage, nicht Volumenmethode), Härtermittel bei Lagerung überprüfen (Viskosität), Training",
    },
    "wrong_fiber_orientation": {
        "name_de": "Falsche Faserorientierung",
        "cause": "Fasern nicht in optimaler Richtung (z.B. statt 0°/±45°/90°)",
        "detection": "Visuelle Inspektion, Ultraschall, Prüfung der Laminat-Datenblätter",
        "impact_on_strength": "50–80 % Festigkeitsverlust in Load-Direction (wenn 90°-Fasern statt 0°-Fasern)",
        "severity": "kritisch",
        "prevention": "Engineering-Spezifikation vor Bau, Qualitäts-Kontrolle während Laminierung, Typische Reihenfolge: Deckschicht (Filler), 0° (Längs), ±45° (Schub), 90° (Quer)",
    },
    "glass_resin_ratio_table": {
        "description": "Gewichts-% Glas zu Harz-Anteil (Rest = Luft, Verunreinigungen)",
        "values": {
            "hand_lamination": "40–55 % Glas (schlecht kontrollierbar, viele Voids)",
            "vacuum_bag": "50–60 % Glas (besser)",
            "resin_infusion": "60–70 % Glas (sehr gute Kontrolle, wenige Voids)",
            "prepreg": "55–65 % Glas (hohe Kontrolle)",
        },
        "notes": "Höherer Glas-Gehalt = höhere Festigkeit, aber schwieriger zu verarbeiten. Unter 40 % = zu viel Harz = höhere Dichte, weniger Steifigkeit.",
    },
}


# ==============================================================================
# GALVANIC SERIES — Galvanische Spannungsreihe (Marine-relevant)
# ==============================================================================

GALVANIC_SERIES_MARINE = [
    ("Carbon", "edel", "+0.5 bis +1.0"),
    ("Platin", "edel", "+1.2"),
    ("Gold", "edel", "+1.0"),
    ("Titan", "edel", "+0.1 bis +0.3"),
    ("Edelstahl 316 passiv", "eher edel", "−0.04 bis +0.1"),
    ("Nickel", "eher edel", "−0.15"),
    ("Kupfer", "mittel", "−0.3 bis −0.2"),
    ("Bronze (Cu/Sn)", "mittel", "−0.2 bis −0.1"),
    ("Edelstahl 316 aktiv", "gemischt", "−0.2 bis −0.5"),  # Wenn Passivschicht bricht
    ("Blei", "unedel", "−0.4"),
    ("Zinn", "unedel", "−0.5"),
    ("Edelstahl 304 aktiv", "unedel", "−0.5 bis −0.8"),  # Chlorid-Angreifer
    ("Gusseisen", "unedel", "−0.6"),
    ("Stahl (mild)", "unedel", "−0.7"),
    ("Aluminium", "sehr unedel", "−0.83"),
    ("Zink", "sehr unedel", "−1.0"),
    ("Magnesium", "extrem unedel", "−1.6"),
]

GALVANIC_SERIES_INTERPRETATION = """
Potentialdifferenz berechnet als: E_Pair = E_noble - E_base.

Beispiel: Carbon (+0.5 V) neben Aluminium (-0.83 V):
- ΔE = 0.5 - (-0.83) = 1.33 V = extrem große Potentialdifferenz!
- Strom fließt: Carbon ist Kathode, Aluminium ist Anode (Korrosion).
- Korrosions-Geschwindigkeit: ~0.5–2.0 mm/Jahr (sehr schnell).

Sicherheit:
- ΔE < 0.3 V: Unbedenklich
- ΔE 0.3–0.6 V: Vorsicht (Isolation notwendig)
- ΔE > 0.6 V: Sehr kritisch (Isolation und/oder Opferschicht erforderlich)

Beste Praxis: Alle unedlen Metalle (Al, Stahl) ISOLIEREN von edlen Metallen
(Kupfer, Carbon, Edelstahl). Isolation durch Kunststoff-Unterlegscheiben,
Epoxid-Beschichtung oder Dichtung.
"""


# ==============================================================================
# TEAK DECK KNOWLEDGE — Umfassendes Teakdeck-Wissen
# ==============================================================================

TEAK_DECK_KNOWLEDGE = {
    "three_sided_adhesion_wrong": {
        "name_de": "Dreiseitige Haftung (FALSCH)",
        "definition": "Teak-Planke ist auf drei Seiten (Ober-, Unter-, Seitenflächen) mit Kleber/Dichtmasse verbunden, nur eine Seite (die Fugen-Oberfläche) ist frei.",
        "problem": "Wenn Holz quillt/schwindet (Feuchtigkeits-Zyklus), ist die Planke zu stark eingeengt. Interne Spannungen bauen auf. Das Holz kann reißen oder sich wölben. Die Dichtung reißt lokal auf.",
        "correct_solution": "EINSEITIGE oder ZWEISEITIGE Haftung. Unter der Planke: Bond Breaker (Kunststoff-Folie oder Epoxid-Grundierung). Nur oben und in den Fugen: Dichtung/Kleber.",
    },

    "bond_breaker": {
        "definition": "Kunststoff-Folie oder dünne Epoxid-Schicht unter der Teak-Planke, die Haftung zwischen Planke und Deck-Untergrund verhindert",
        "purpose": "Erlaubt Planke, frei zu quellen/schwinden ohne Spannungs-Aufbau",
        "material": "HDPE-Folie (Polyethylen), 0,1–0,2 mm dick. Oder: Dünne Epoxid-Grundierung (50 µm).",
        "application": "Auf Deck auftragen VOR Planke-Verlegung. Planke wird dann mit Sikaflex in den Fugen (nicht unter der Planke) befestigt.",
    },

    "joint_width": {
        "correct_range": "3–5 mm",
        "reasons": "Zu schmal (<2 mm): Sikaflex kann nicht richtig eindringen, schlechte Haftung. Zu breit (>6 mm): Zu viel Bewegung, Risse entstehen schneller.",
        "filling": "Sikaflex 298 oder 290DC, gefüllt mit Quarzsand und UV-stabilen Pigmenten (Titandioxid).",
    },

    "primer": {
        "necessity": "ESSENTIELL für Teakholz",
        "purpose": "Verdünnt in Teakfasern ein, erzeugt beste Haftung für Sikaflex",
        "application": "Alle Fugen-Flächen (oberflächlich, ca. 1–2 mm tief) mit Primer befeuchten. 10–30 Minuten aushärten, dann Sikaflex auftragen.",
        "product": "Sikaflex Primer 206 oder ähnlich",
    },

    "sikaflex_products": {
        "298": {
            "name": "Sikaflex 298 (älter)",
            "properties": "Polyurethan-Basis, gute UV-Beständigkeit, aber weniger elastisch als 290DC",
            "outdoor_use": "Ja, aber empfohlene Lebensdauer: 8–12 Jahre",
        },
        "290dc": {
            "name": "Sikaflex 290 Duo Component (moderner)",
            "properties": "2K-Polyurethan, bessere Elastizität als 298, bessere UV-Stabilität",
            "outdoor_use": "Ja, Lebensdauer: 10–15 Jahre",
            "recommendation": "Bessere Wahl für Teak-Decks",
        },
    },

    "five_most_common_mistakes": [
        {
            "mistake": "Kein Primer vor Sikaflex",
            "consequence": "Haftung schlecht → Sikaflex löst sich in 1–2 Jahren → Wasser eindringung sofort",
            "prevention": "IMMER Primer verwenden (10–30 Min. Trocknungszeit beachten)",
        },
        {
            "mistake": "Dreiseitige Haftung (Planke unter, Seiten, oben geklebt)",
            "consequence": "Spannungs-Aufbau → Holz-Risse oder Dichtung-Risse → Wasser-Eindringung",
            "prevention": "Bond Breaker unter der Planke, nur oben und in Fugen Dichtung",
        },
        {
            "mistake": "Schrauben durch Teakplanke OHNE Wasserbarriere",
            "consequence": "Jede Schraube = Wasserbahn → Kern quillt → Planke lockert sich",
            "prevention": "Alle Schrauben mit Epoxid-Harz vergießen oder Sikaflex-Dichtung + Unterlegscheibe",
        },
        {
            "mistake": "Teak auf Sperrholz ohne Barriere-Schicht",
            "consequence": "Sperrholz quillt unter Teak → ungleichmäßige Fläche → Risse, Bewegung",
            "prevention": "Epoxid-Barriere oder Bond Breaker auf Sperrholz BEVOR Teak-Verlegung",
        },
        {
            "mistake": "Zu viel Teaköl (oder falsches Öl)",
            "consequence": "Öl verhindert Primo-Penetration → schlechte Sikaflex-Haftung",
            "prevention": "Polyurethan-Teaköl 2x pro Jahr dünn auftragen, nicht öl-getränkt",
        },
    ],

    "wood_grain_orientation": {
        "standing_rings": {
            "name": "Stehende Jahrringe",
            "appearance": "Ringe sind vertikal in der Schnittfläche (Jährliche Wachstums-Schicht senkrecht zur Oberfläche)",
            "property": "Geringere Quellung (~2–3 %), bessere Stabilität",
            "durability": "Länger (20+ Jahre, wenn gepflegt)",
        },
        "lying_rings": {
            "name": "Liegende Jahrringe",
            "appearance": "Ringe sind horizontal/flach",
            "property": "Höhere Quellung (~4–5 %), weniger stabil",
            "durability": "Kürzer (10–15 Jahre)",
        },
    },

    "plank_thickness": {
        "8_10_mm": {
            "thickness_range": "8–10 mm",
            "durability": "20+ Jahre (wenn gut gepflegt)",
            "advantage": "Genug Holzmasse für Stabilität",
        },
        "4_mm": {
            "thickness_range": "4 mm",
            "durability": "5–10 Jahre (nur mit Epoxid-Unterbau)",
            "disadvantage": "Zu dünn für lange Lebensdauer",
            "use_case": "Nur auf massiv-steifen Untergrund (nicht Sandwich-Deck)",
        },
    },
}


# ==============================================================================
# RISK ASSESSMENT FUNCTION
# ==============================================================================

@dataclass
class FailureRiskAssessment:
    """Forensic failure risk analysis result"""
    overall_score: float  # 0–100, higher = more risk
    risk_areas: List[str]  # ["Osmosis", "Galvanic corrosion", ...]
    critical_warnings: List[str]  # Immediate action required
    degradation_cycles_active: List[str]  # Active self-reinforcing cycles
    recommendations: List[str]  # Action items


def assess_failure_risk(
    boat_age_years: float,
    hull_material: str,  # "GFK", "Aluminium", "Stahl", etc.
    core_material: str,  # "Balsa", "PVC", "Polyurethan", "Styropor"
    antifouling_type: str,  # "Kupfer", "Zinn", "Silikon", etc.
    seacock_material: str,  # "Messing", "Bronze", "Edelstahl", etc.
    rigging_age_years: float,  # Age of standing rigging
    electrical_age_years: float,  # Age of electrical wiring
    environment: Environment,
    maintenance_level: MaintenanceLevel,
) -> FailureRiskAssessment:
    """
    Comprehensive forensic failure risk assessment based on material composition,
    age, environment, and maintenance history.

    German UX: All warnings and recommendations in German.
    """

    risk_score = 0.0
    risk_areas = []
    critical_warnings = []
    active_cycles = []
    recommendations = []

    # ==== BASE SCORE FROM AGE ====
    if boat_age_years < 5:
        risk_score += 5
    elif boat_age_years < 10:
        risk_score += 15
    elif boat_age_years < 20:
        risk_score += 30
    elif boat_age_years < 30:
        risk_score += 45
    else:
        risk_score += 60

    # ==== HULL MATERIAL ASSESSMENT ====
    if hull_material.lower() == "gfk":
        # GFK is polyester composite
        risk_score += 10  # Osmosis risk

        if boat_age_years > 5:
            risk_areas.append("Osmose")
            if boat_age_years > 15:
                critical_warnings.append(
                    "KRITISCH: Boot >15 Jahre, GFK-Rumpf. Osmose-Blasen wahrscheinlich. "
                    "Haul-Out + Inspektion INNERHALB 4 STUNDEN nach Aufzug notwendig."
                )
                active_cycles.append("osmosis_microcrack_cycle")

        # Core degradation assessment
        if core_material.lower() == "balsa":
            if boat_age_years > 10:
                risk_areas.append("Balsa-Kern-Feuchtigkeit")
                if environment == Environment.ARCTIC:
                    critical_warnings.append(
                        "LEBENSBEDROHLICH: Balsa-Kern in Arktis-Region. Frostzyklen können "
                        "Kern-Struktur zerstören. Winterlagerung ESSENTIELL (an Land, >5°C)."
                    )
                    active_cycles.append("moisture_seal_failure_cycle")

        elif core_material.lower() == "pvc":
            if boat_age_years > 15:
                risk_areas.append("PVC-Schaum-Degradation")

    elif hull_material.lower() == "aluminium":
        risk_score += 15  # Galvanic corrosion risk
        risk_areas.append("Galvanische Korrosion (Alu-Rumpf)")

        # Check for copper AF on aluminum (critical incompatibility)
        if antifouling_type.lower() == "kupfer":
            critical_warnings.append(
                "KRITISCH: Kupfer-AF auf Aluminium-Rumpf. Ohne Isolation → Lochfraß "
                "in Wochen bis Monaten. Epoxid-Barriere (min. 100 µm) SOFORT anbringen."
            )
            risk_score += 25

    # ==== SEACOCK ASSESSMENT ====
    if seacock_material.lower() == "messing":
        if boat_age_years > 5:
            critical_warnings.append(
                "LEBENSBEDROHLICH: Messing-Seeventil >5 Jahre alt. Dezinkierung-Risiko. "
                "Visuell prüfen: Ist das Ventil rot statt gold? Wenn ja: SOFORT ersetzen "
                "(Bronz-Alternative). Funktionstests regelmäßig (2x pro Jahr)."
            )
            risk_areas.append("Seeventil-Dezinkierung")
            risk_score += 20
            active_cycles.append("corrosion_fastener_seal_failure")

    # ==== RIGGING ASSESSMENT ====
    if rigging_age_years > 20:
        risk_areas.append("Rigging-Korrosion (alte Wanten/Stagen)")
        risk_score += 12
        recommendations.append("Rigging-Inspektion: Oberflächenrost? Seile (Drahtseil) splitternd?")

    # ==== ELECTRICAL ASSESSMENT ====
    if electrical_age_years > 15:
        risk_areas.append("Elektro-Isolationsverlust (Stray Currents)")
        risk_score += 10
        recommendations.append(
            "Isolation-Prüfung des Bordnetzes (AC-Leck-Test). Alle Kabel-Durchgänge überprüfen."
        )
        active_cycles.append("stray_current_corrosion_cycle")

    # ==== ENVIRONMENT MULTIPLIER ====
    if environment == Environment.TROPICAL:
        risk_score *= 1.3  # 3x faster osmosis, corrosion
        recommendations.append(
            "Tropisches Klima: Alle Inspektions-Abstände um 30–50 % verkürzen. "
            "Haul-Out jährlich (nicht alle 2 Jahre)."
        )

    # ==== MAINTENANCE MULTIPLIER ====
    maintenance_multipliers = {
        MaintenanceLevel.NONE: 1.5,
        MaintenanceLevel.POOR: 1.3,
        MaintenanceLevel.BASIC: 1.0,
        MaintenanceLevel.GOOD: 0.7,
        MaintenanceLevel.EXCELLENT: 0.5,
    }
    risk_score *= maintenance_multipliers.get(maintenance_level, 1.0)

    if maintenance_level in (MaintenanceLevel.NONE, MaintenanceLevel.POOR):
        critical_warnings.append(
            "Instandhaltung unzureichend: Inspektions- und Reparatur-Zyklus SOFORT erhöhen. "
            "Jährliche Haul-Out, Kern-Feuchte-Tests, Dichtstoff-Inspektionen erforderlich."
        )

    # ==== CAPPING SCORE ====
    risk_score = min(100, max(0, risk_score))

    # ==== GENERIC RECOMMENDATIONS ====
    if risk_score > 70:
        recommendations.append(
            "DRINGEND: Umfassende Haul-Out-Inspektion mit Ultraschall, Feuchte-Messungen, "
            "Bohrproben erforderlich."
        )

    recommendations.append(
        "Jährliche Inspektionen: Gelcoat-Risse, Dichtstoff-Risse, Wasserflecken, "
        "Rost-Aureolen um Befestigungen."
    )

    recommendations.append(
        "Alle 5 Jahre: Kern-Feuchte-Messung, Ultraschall-Scanning kritischer Bereiche, "
        "Seacock-Funktionsprüfung."
    )

    if boat_age_years > 20:
        recommendations.append(
            "Boot >20 Jahre: Erwägen Sie umfassende Restauration oder Verkauf. "
            "Strukturelle Integrität kann nicht mehr garantiert werden."
        )

    return FailureRiskAssessment(
        overall_score=risk_score,
        risk_areas=risk_areas,
        critical_warnings=critical_warnings,
        degradation_cycles_active=active_cycles,
        recommendations=recommendations,
    )
