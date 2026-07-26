# 07.02 — Borddurchlässe und Rumpfdurchführungen

> **Modulkontext**: structural, compliance, materials, service_patterns, production
> **Confidence-Klassen**: measured | calculated | visual_high | visual_medium | estimated | documented | benchmark
> **Pydantic-Hinweis**: `model_config = {"from_attributes": True}` — NIEMALS `class Config`
> **Letzte Aktualisierung**: 2026-04

---

## Inhaltsverzeichnis

1. [Einführung & Regulatorischer Rahmen](#einführung--regulatorischer-rahmen)
2. [Zukunftstechnologien](#zukunftstechnologien)
3. [Best Practices nach Revier](#best-practices-nach-revier)
4. [Regional Sourcing](#regional-sourcing)
5. [Zweck dieser Wissensdatei](#zweck-dieser-wissensdatei)
6. [Pydantic-Modelle](#pydantic-modelle)
7. [Grundlagen](#grundlagen)
8. [Hersteller — Vollständige Übersicht](#hersteller--vollständige-übersicht)
9. [Anlagen-spezifische Zuordnung](#anlagen-spezifische-zuordnung)
10. [Verbindungstechnik](#verbindungstechnik)
11. [Technische Referenz & Berechnungen](#technische-referenz--berechnungen)
12. [Einbau-/Austausch-Anleitung](#einbau-austausch-anleitung)
13. [Lebensdauer und Alterungsmechanismen](#lebensdauer-und-alterungsmechanismen)
14. [Fehlerbild-Atlas](#fehlerbild-atlas)
15. [Fehlerbehebungs-Leitfaden](#fehlerbehebungs-leitfaden)
16. [FAQ](#faq)
17. [Glossar](#glossar)
18. [Schnell-Referenz](#schnell-referenz)
19. [Notfall-Ressourcen](#notfall-ressourcen)
20. [ANHANG A–R](#anhänge)

---

## Einführung & Regulatorischer Rahmen

### Überblick

Borddurchlässe (engl. through-hull fittings, skin fittings) und Rumpfdurchführungen sind jede konstruktive Öffnung im Rumpf eines Wasserfahrzeugs, die einen kontrollierten Durchgang von Flüssigkeiten, Gasen, Kabeln oder Instrumenten durch die Außenhaut ermöglicht. Sie gehören zu den sicherheitskritischsten Bauteilen eines Bootes: Jeder einzelne Borddurchlass ist ein potenzieller Leckagepunkt, der bei Versagen zum Sinken des Schiffes führen kann.

(Confidence: documented)

### Statistik und Relevanz

Laut Schadenstatistiken der Pantaenius-Versicherungsgruppe (Auswertung 2018–2024) sind defekte Borddurchlässe und Seeventile die **dritthäufigste Ursache für Wassereinbruch** bei Yachten im europäischen Raum:

| Ursache | Anteil an Wassereinbruch-Schäden |
|---|---|
| Schlauchverbindungen / Schlauchschellen | 34 % |
| Stopfbuchsen / Wellendichtungen | 22 % |
| **Borddurchlässe / Seeventile** | **18 %** |
| Rumpfosmose / Laminatschäden | 12 % |
| Luken / Fenster | 8 % |
| Sonstige | 6 % |

(Confidence: benchmark)

### Regulatorische Anforderungen

#### ISO 9093-1:2020 — Seeventile und Rumpfdurchführungen, Teil 1: Metallisch

Diese Norm definiert Anforderungen an metallische Borddurchlässe und Seeventile für Boote bis 24 m Rumpflänge:

| Anforderung | Spezifikation |
|---|---|
| Werkstoff | Bronze (UNS C83600, C84400, C92200), Edelstahl AISI 316L |
| Mindest-Wandstärke | ≥3 mm bei Nennweite ≤38 mm, ≥4 mm bei >38 mm |
| Druckprüfung | 2 × max. Betriebsdruck, mind. 2 bar |
| Korrosionsbeständigkeit | 30 Tage Salzsprühtest nach ISO 9227 |
| Kennzeichnung | Hersteller, Nennweite, Werkstoff, Produktionsdatum |
| Gewindetyp | BSP (ISO 228) oder NPT (ANSI B1.20.1) |
| Temperaturbereich | -20 °C bis +60 °C (Standard), +120 °C (Abgas) |

(Confidence: documented)

#### ISO 9093-2:2020 — Seeventile und Rumpfdurchführungen, Teil 2: Nicht-metallisch

| Anforderung | Spezifikation |
|---|---|
| Werkstoff | Glasfaserverstärktes Polyamid (PA66-GF30), Marelon |
| Mindest-Wandstärke | ≥4 mm bei Nennweite ≤38 mm, ≥5 mm bei >38 mm |
| UV-Beständigkeit | 1000 h Xenon-Test nach ISO 4892-2, ΔE <3 |
| Druckprüfung | 3 × max. Betriebsdruck, mind. 3 bar |
| Brandverhalten | UL 94 V-0 oder gleichwertig |
| Temperaturbereich | -30 °C bis +82 °C (Marelon), +93 °C (TruDesign) |
| Korrosion | Nicht anwendbar — galvanisch inert |

(Confidence: documented)

#### ABYC Standard H-27 — Through-Hull Fittings and Sea Valves

Der amerikanische Standard ABYC H-27 ergänzt die ISO-Normen mit zusätzlichen Anforderungen:

- Alle Borddurchlässe unterhalb der Wasserlinie **müssen** mit einem Seeventil versehen sein
- Seeventile müssen **ohne Werkzeug** bedienbar sein (Handhebel)
- Seeventile müssen in **geschlossener Position** gekennzeichnet sein
- Borddurchlässe für Abgas **müssen** aus Metall sein (min. 316L oder Bronze)
- Borddurchlässe im Maschinenraum müssen **feuerfest** sein (15 min bei 650 °C)
- Kein Plastik-Borddurchlass unterhalb WL in der Nähe von Wärmequellen (>65 °C Abstand <300 mm)

(Confidence: documented)

#### CE / Recreational Craft Directive 2013/53/EU

Die RCD verweist auf die harmonisierte Norm EN ISO 9093 und stellt folgende Grundanforderungen:

| Aspekt | Anforderung |
|---|---|
| Kategorie A/B | Alle Durchlässe unter WL mit Seeventil, Notholzstopfen zugänglich |
| Kategorie C/D | Seeventile empfohlen, für Toiletten-Einlass Pflicht |
| Kennzeichnung | CE-Konformitätserklärung des Fittings oder des Boots |
| Dokumentation | Borddurchlass-Plan im Eignerhandbuch (Anzahl, Position, Funktion) |
| Wartung | Herstellerangaben zu Inspektionsintervallen |

(Confidence: documented)

#### Lloyd's Register — Special Service Craft Rules

Für Yachten unter Lloyd's-Klasse gelten verschärfte Anforderungen:

- Borddurchlässe in Schotte erlaubt nur mit Zulassung des Surveyors
- Doppelte Schlauchschellen an jedem Borddurchlass unter WL
- Jährliche Inspektion aller Seeventile durch zugelassenen Surveyor
- Material-Zertifikate (3.1 nach EN 10204) für alle metallischen Durchlässe
- Backing-Plates: min. 3× Durchmesser des Fittings, min. 10 mm GFK

(Confidence: documented)

#### DNV-GL — Rules for Classification of Yachts

| Regel | Inhalt |
|---|---|
| Pt.3 Ch.6 Sec.4 | Rumpfdurchführungen: Werkstoff, Dimensionierung |
| Pt.3 Ch.6 Sec.5 | Seeventile: Typ, Bedienbarkeit, Kennzeichnung |
| Pt.3 Ch.6 Sec.6 | Rohrleitungen: Material, Wandstärke, Befestigung |
| Pt.3 Ch.11 Sec.2 | Korrosionsschutz: Galvanische Trennung, Opferanoden |

(Confidence: documented)

### Normvergleich: ISO 9093 vs. ABYC H-27

| Kriterium | ISO 9093 (EU) | ABYC H-27 (USA) |
|---|---|---|
| Geltungsbereich | Boote ≤24 m | Alle Freizeitboote |
| Kunststoff unter WL | Zulässig (ISO 9093-2) | Zulässig (UL-geprüft) |
| Seeventil-Pflicht | Unter WL empfohlen | Unter WL Pflicht |
| Abgas-Durchlass | Metall empfohlen | Metall Pflicht |
| Notholzstopfen | Bei CE-Kat. A/B Pflicht | Empfohlen |
| Galvanische Isolation | Erwähnt | Detailliert (ABYC E-2) |
| Brandprüfung | Nicht spezifiziert | 15 min / 650 °C |

(Confidence: documented)

---

## Zukunftstechnologien

### Intelligente Borddurchlässe (Smart Through-Hulls)

Die nächste Generation von Borddurchlässen integriert Sensorik und Aktorik direkt in das Fitting:

#### Konzept: IoT-Seeventil mit Fernüberwachung

| Merkmal | Beschreibung |
|---|---|
| Durchfluss-Sensor | Ultraschall-Messung, Genauigkeit ±2 % |
| Leckage-Erkennung | Feuchtigkeitssensor an der Innenseite des Fittings |
| Temperatur | PT100-Sensor, -40 bis +200 °C |
| Fernbetätigung | 12/24 V DC-Aktuator, Schließzeit <5 s |
| Konnektivität | NMEA 2000, Wi-Fi, optional LTE |
| Stromverbrauch | <0,5 W Standby, <15 W beim Schalten |
| Prototyp-Status | Garmin/Navico Forschungsprojekte (Stand 2025) |

(Confidence: estimated)

#### Materialinnovation: Titan-Borddurchlässe

Titan Grade 2 (UNS R50400) bietet optimale Eigenschaften:

| Eigenschaft | Titan Gr.2 | Bronze C83600 | Marelon |
|---|---|---|---|
| Dichte | 4,51 g/cm³ | 8,83 g/cm³ | 1,80 g/cm³ |
| Zugfestigkeit | 345 MPa | 255 MPa | 82 MPa |
| Korrosion in Seewasser | Immun | Gut (bei Entfernung von Zink) | Immun |
| Galvanische Verträglichkeit | Kathodisch, Potenzial -0,05 V | Anodisch, -0,31 V | Inert |
| Preis (3/4" Fitting) | ~280 EUR | ~45 EUR | ~22 EUR |
| Gewicht (3/4" Fitting) | ~85 g | ~165 g | ~35 g |

Titan ist besonders für Aluminium-Rümpfe interessant, da keine galvanische Reaktion mit dem Rumpfmaterial auftritt. Nachteil: Hohe Kosten und schwierige Bearbeitung.

(Confidence: documented)

#### 3D-gedruckte Borddurchlässe

Additive Fertigung aus PEEK (Polyetheretherketon) oder 316L-Pulver ermöglicht:

- Individuelle Geometrien für jeden Rumpfwinkel
- Integrierte Strömungsoptimierung (CFD-optimierte Innenkonturen)
- On-Demand-Fertigung für Ersatzteile älterer Boote
- Status 2025: Prototypen bei Rolls-Royce Marine, noch keine Serienfreigabe

(Confidence: estimated)

#### Selbstheilende Dichtungen

Forschungsansätze für mikroverkapselte Dichtstoffe im Borddurchlass-Bereich:

| Technologie | TRL (Technology Readiness Level) | Beschreibung |
|---|---|---|
| Mikrokapseln mit Polysulfid | TRL 3 | Kapseln brechen bei Rissbildung, setzen Dichtstoff frei |
| Shape-Memory-Polymere | TRL 2 | Material dehnt sich bei Kontakt mit Wasser aus, dichtet Spalte |
| Graphen-verstärkte Epoxide | TRL 4 | Höhere Bruchdehnung, bessere Haftung auf nassem GFK |

(Confidence: estimated)

---

## Best Practices nach Revier

### Ostsee / Brackwasser

| Aspekt | Empfehlung |
|---|---|
| Salinität | 5–18 ‰ — reduzierte galvanische Korrosion, aber erhöhte biologische Bewuchs |
| Material | Bronze oder Marelon — 316L ebenfalls geeignet |
| Bewuchs | Seepocken (Balanidae) weniger aggressiv als Mittelmeer |
| Winterlager | Seeventile offen lassen, Frostschutz in allen Leitungen |
| Anoden | Zinkanoden ausreichend, Wechselintervall 24 Monate |
| Besonderheit | Brackwasser fördert Entzinkung bei minderwertigem Messing |

(Confidence: documented)

### Mittelmeer

| Aspekt | Empfehlung |
|---|---|
| Salinität | 36–39 ‰ — volle Seewasser-Korrosion |
| Material | Bronze C83600 oder 316L, **kein Messing** |
| Bewuchs | Intensiv, Seepocken + Algen, Scoop-Strainer regelmäßig reinigen |
| UV-Belastung | Höchste UV-Klasse — Marelon-Fittings über WL UV-schützen |
| Anoden | Zinkanoden, Wechselintervall 12 Monate |
| Besonderheit | Elektrolyse in Marinas mit Fremdstrom häufig — Galvanic Isolator empfohlen |

(Confidence: documented)

### Tropen / Karibik

| Aspekt | Empfehlung |
|---|---|
| Salinität | 34–36 ‰ |
| Temperatur | Seewasser 26–30 °C — beschleunigte Korrosion um Faktor 1,5–2 |
| Material | Bronze oder Titan, **kein 316L** (Lochfraß bei >25 °C Wassertemp.) |
| Bewuchs | Extrem — monatliche Reinigung der Scoop-Strainer |
| Anoden | Zinkanoden, Wechselintervall 6–9 Monate |
| Besonderheit | Muscheln (Dreissena) können Borddurchlässe komplett verschließen |

(Confidence: documented)

### Süßwasser (Binnenschifffahrt)

| Aspekt | Empfehlung |
|---|---|
| Korrosion | Minimal — alle Materialien geeignet |
| Bewuchs | Gering, saisonabhängig |
| Material | Marelon (günstigste Option) |
| Anoden | Magnesiumanoden statt Zink |
| Besonderheit | Frostgefahr — alle Durchlässe bei Winterlager öffnen und Wasser ablassen |

(Confidence: documented)

### Gezeitenreviere (Nordsee, Ärmelkanal)

| Aspekt | Empfehlung |
|---|---|
| Salinität | 30–35 ‰ |
| Besonderheit | Trockenfallen — alle Borddurchlässe müssen dicht sein bei Ebbe |
| Material | Bronze oder Marelon, 316L mit Vorsicht |
| Sediment | Sand/Schlick — Scoop-Strainer mit gröberer Maschenweite |
| Tidal Range | Borddurchlässe können bei Niedrigwasser über WL liegen — Seeventile offen lassen |

(Confidence: documented)

---

## Regional Sourcing

### Europa

| Händler | Land | Spezialität | Webshop |
|---|---|---|---|
| SVB Yacht Fittings | DE | Vollsortiment Groco, TruDesign, Vetus | svb-marine.de |
| Compass24 | DE | Großes Lager, schnelle Lieferung | compass24.de |
| Toplicht | DE | Premiumsegment, Guidi, Groco | toplicht.de |
| Force4 Chandlery | UK | Blakes, Forespar, Perko | force4.co.uk |
| Accastillage Diffusion | FR | Plastimo, Guidi, TruDesign | accastillage-diffusion.com |
| Navimag | IT | Guidi, Osculati | navimag.it |
| Bootscenter Kiel | DE | Gebrauchtteile, ältere Modelle | bootscenter-kiel.de |

(Confidence: documented)

### Nordamerika

| Händler | Land | Spezialität |
|---|---|---|
| West Marine | USA | Vollsortiment, Groco, Forespar, Perko |
| Defender Industries | USA | Günstige Preise, Groco, Buck Algonquin |
| Hamilton Marine | USA | Gewerbliche Qualität, Bronze-Spezialist |
| Fisheries Supply | USA | Pacific Northwest, Groco/Buck Algonquin |

(Confidence: documented)

### Asien / Australien

| Händler | Land | Spezialität |
|---|---|---|
| Whitworths Marine | AUS | TruDesign (NZ-Hersteller), Groco |
| CH Smith Marine | AUS | Bronze-Fittings, Guidi |
| BLA Marine | AUS | Großhandel, TruDesign-Vertrieb |

(Confidence: documented)

---

## Zweck dieser Wissensdatei

### Aufgabe im AYDI-System

Diese Wissensdatei dient als primäre Referenz für das AYDI-Analysesystem in folgenden Bereichen:

1. **Structural-Modul**: Bewertung der strukturellen Integrität von Borddurchlass-Installationen, Backing-Plates, Kernverstärkungen
2. **Compliance-Modul**: Überprüfung der Konformität mit ISO 9093, ABYC H-27, CE/RCD
3. **Materials-Modul**: Werkstoffbewertung, galvanische Kompatibilität, Lebensdauerprognose
4. **Service-Patterns-Modul**: Erkennung typischer Verschleiß- und Schadensmuster
5. **Production-Modul**: Bewertung der Einbauqualität (Dichtstoff-Applikation, Ausrichtung, Backing)
6. **Visual-Analyse**: Referenzbilder für Schadensklassifikation via Claude Vision

### Abgrenzung zur Datei 01.05

Die Datei `01_05_borddurchlass_dichtungen.md` behandelt primär die **Dichtungsmaterialien und -techniken** am Borddurchlass. Die vorliegende Datei `07_02_borddurchlaesse.md` behandelt den **Borddurchlass als Gesamtsystem**: Typen, Materialien, Einbau, Systeme, Lebensdauer, Fehlerdiagnose.

(Confidence: documented)

---

## Pydantic-Modelle

### ThroughHullSpec — Spezifikation eines einzelnen Borddurchlasses

```python
from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class ThroughHullType(str, Enum):
    """Typ des Borddurchlasses."""
    MUSHROOM = "mushroom"              # Pilzförmig — Standard
    FLUSH = "flush"                    # Bündig — Racing / Superyacht
    FLANGED = "flanged"                # Geflancht — Heavy-duty
    SCOOP = "scoop"                    # Schaufel-Einlass
    DRAIN = "drain"                    # Ablauf (Cockpit, Waschbecken)
    TRANSDUCER = "transducer"          # Geber-Durchführung (Echolot, Log)
    EXHAUST = "exhaust"                # Abgas-Durchführung
    CABLE = "cable"                    # Kabel-Durchführung

class ThroughHullMaterial(str, Enum):
    """Werkstoff des Borddurchlasses."""
    BRONZE_C83600 = "bronze_c83600"    # Rotguss, Standard
    BRONZE_C84400 = "bronze_c84400"    # Leaded semi-red brass
    BRONZE_C92200 = "bronze_c92200"    # Navy bronze
    STAINLESS_316L = "stainless_316l"  # Edelstahl austenitisch
    MARELON = "marelon"                # Glasfaserverstärktes Polyamid (Forespar)
    TRUDESIGN = "trudesign"            # Glasfaserverstärktes Polyamid (TruDesign)
    DELRIN = "delrin"                  # Polyacetal (POM) — nur über WL
    TITANIUM_GR2 = "titanium_gr2"     # Titan Grade 2
    BRASS = "brass"                    # Messing — NICHT empfohlen unter WL
    NYLON = "nylon"                    # PA6 — nur über WL, nicht ISO-konform unter WL
    ALUMINUM_BRONZE = "aluminum_bronze" # CuAl — für Aluminium-Rümpfe bedingt

class ThroughHullPosition(str, Enum):
    """Position relativ zur Wasserlinie."""
    BELOW_WL = "below_wl"             # Unter Wasserlinie — Seeventil Pflicht
    AT_WL = "at_wl"                   # Auf Wasserlinie — Seeventil empfohlen
    ABOVE_WL = "above_wl"             # Über Wasserlinie
    TRANSOM = "transom"                # Spiegel (Heck)

class SeacockType(str, Enum):
    """Typ des zugehörigen Seeventils."""
    BALL_VALVE = "ball_valve"          # Kugelhahn — Standard
    GATE_VALVE = "gate_valve"          # Schieber — NICHT empfohlen
    PLUG_VALVE = "plug_valve"         # Küken-Ventil — Tradition
    DIAPHRAGM = "diaphragm"           # Membranventil — Spezial
    NONE = "none"                      # Kein Seeventil installiert

class ThreadType(str, Enum):
    """Gewindetyp."""
    BSP = "bsp"                        # British Standard Pipe (ISO 228)
    NPT = "npt"                        # National Pipe Thread (ANSI)
    METRIC = "metric"                  # Metrisch (selten)

class BeddingCompound(str, Enum):
    """Dichtstoff für die Montage."""
    POLYSULFIDE = "polysulfide"        # 3M 101, Boat-Life Life-Calk
    POLYURETHANE = "polyurethane"      # Sikaflex 291i, 3M 5200
    BUTYL = "butyl"                    # Butylband — nur Druckverbindungen
    SILICONE = "silicone"              # NICHT empfohlen unter WL
    EPOXY = "epoxy"                    # Nur bei permanenter Verklebung

class ThroughHullSpec(BaseModel):
    """Spezifikation eines einzelnen Borddurchlasses im AYDI-System."""
    model_config = {"from_attributes": True}

    fitting_id: str = Field(
        ...,
        description="Eindeutige Kennung im Borddurchlass-Plan, z.B. 'BD-001'"
    )
    fitting_type: ThroughHullType = Field(
        ...,
        description="Typ des Borddurchlasses"
    )
    material: ThroughHullMaterial = Field(
        ...,
        description="Werkstoff des Borddurchlasses"
    )
    position: ThroughHullPosition = Field(
        ...,
        description="Position relativ zur Wasserlinie"
    )
    nominal_diameter_mm: float = Field(
        ...,
        ge=10.0,
        le=200.0,
        description="Nennweite in mm (Innen-Ø)"
    )
    thread_type: ThreadType = Field(
        default=ThreadType.BSP,
        description="Gewindetyp"
    )
    thread_size: str = Field(
        ...,
        description="Gewindegröße, z.B. '3/4 BSP', '1 NPT'"
    )
    seacock_type: SeacockType = Field(
        default=SeacockType.BALL_VALVE,
        description="Typ des zugehörigen Seeventils"
    )
    seacock_material: Optional[ThroughHullMaterial] = Field(
        default=None,
        description="Werkstoff des Seeventils (falls abweichend vom Fitting)"
    )
    bedding_compound: BeddingCompound = Field(
        default=BeddingCompound.POLYSULFIDE,
        description="Verwendeter Dichtstoff"
    )
    has_backing_plate: bool = Field(
        default=True,
        description="Backing-Plate vorhanden?"
    )
    backing_plate_material: Optional[str] = Field(
        default=None,
        description="Material der Backing-Plate, z.B. 'GFK 10mm', 'G10 12mm'"
    )
    hull_thickness_mm: Optional[float] = Field(
        default=None,
        ge=3.0,
        le=80.0,
        description="Rumpfdicke an der Einbaustelle in mm"
    )
    hull_construction: Optional[str] = Field(
        default=None,
        description="Rumpfbauweise: 'solid_grp', 'sandwich_pvc', 'sandwich_balsa', 'aluminum', 'steel', 'wood'"
    )
    core_removed: Optional[bool] = Field(
        default=None,
        description="Bei Sandwich: Kern im Bereich des Durchlasses entfernt und mit Laminat/Epoxy gefüllt?"
    )
    system_function: str = Field(
        ...,
        description="Funktion: 'raw_water_intake', 'exhaust', 'bilge_discharge', 'toilet_intake', 'toilet_discharge', 'ac_intake', 'ac_discharge', 'generator_intake', 'watermaker_intake', 'depth_transducer', 'speed_transducer', 'cockpit_drain', 'sink_drain', 'shower_drain'"
    )
    manufacturer: Optional[str] = Field(
        default=None,
        description="Hersteller, z.B. 'Groco', 'TruDesign', 'Guidi'"
    )
    part_number: Optional[str] = Field(
        default=None,
        description="Herstellerteilenummer, z.B. 'TH-750-W'"
    )
    install_date: Optional[str] = Field(
        default=None,
        description="Einbaudatum (YYYY-MM)"
    )
    last_inspection_date: Optional[str] = Field(
        default=None,
        description="Letzte Inspektion (YYYY-MM)"
    )
    distance_from_wl_mm: Optional[float] = Field(
        default=None,
        description="Abstand zur Wasserlinie in mm (negativ = unter WL)"
    )
    zone: Optional[str] = Field(
        default=None,
        description="AYDI-Zone: 'bow', 'midship_port', 'midship_stbd', 'stern', 'transom', 'keel'"
    )
    notes: Optional[str] = Field(
        default=None,
        description="Bemerkungen"
    )
```

(Confidence: documented)

### ThroughHullCondition — Zustandsbewertung eines Borddurchlasses

```python
class ConditionRating(str, Enum):
    """Zustandsbewertung."""
    EXCELLENT = "excellent"            # Neuwertig oder wie neu
    GOOD = "good"                      # Gebrauchsspuren, voll funktionsfähig
    FAIR = "fair"                      # Deutliche Alterung, noch funktionsfähig
    POOR = "poor"                      # Erneuerung empfohlen
    CRITICAL = "critical"             # Sofortige Erneuerung erforderlich
    NOT_ASSESSABLE = "not_assessable" # Nicht beurteilbar

class ConfidenceLevel(str, Enum):
    """Confidence-Level der Bewertung."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"

class ThroughHullCondition(BaseModel):
    """Zustandsbewertung eines einzelnen Borddurchlasses."""
    model_config = {"from_attributes": True}

    fitting_id: str = Field(
        ...,
        description="Referenz auf ThroughHullSpec.fitting_id"
    )
    overall_score: float = Field(
        ...,
        ge=0,
        le=100,
        description="Gesamtbewertung 0–100"
    )
    condition: ConditionRating = Field(
        ...,
        description="Qualitative Zustandsbewertung"
    )
    confidence: ConfidenceLevel = Field(
        ...,
        description="Confidence-Level der Bewertung"
    )

    # Einzelbewertungen
    material_score: float = Field(
        default=0,
        ge=0,
        le=100,
        description="Werkstoffzustand 0–100"
    )
    installation_score: float = Field(
        default=0,
        ge=0,
        le=100,
        description="Einbauqualität 0–100"
    )
    seacock_score: float = Field(
        default=0,
        ge=0,
        le=100,
        description="Seeventil-Zustand 0–100"
    )
    bedding_score: float = Field(
        default=0,
        ge=0,
        le=100,
        description="Dichtstoff-Zustand 0–100"
    )
    backing_score: float = Field(
        default=0,
        ge=0,
        le=100,
        description="Backing-Plate-Zustand 0–100"
    )
    hose_connection_score: float = Field(
        default=0,
        ge=0,
        le=100,
        description="Schlauchverbindung 0–100"
    )
    corrosion_score: float = Field(
        default=0,
        ge=0,
        le=100,
        description="Korrosionszustand 0–100 (100 = keine Korrosion)"
    )

    # Befunde
    findings: list[str] = Field(
        default_factory=list,
        description="Liste der Befunde, z.B. 'Entzinkung sichtbar', 'Dichtstoff gerissen'"
    )
    recommendations: list[str] = Field(
        default_factory=list,
        description="Empfehlungen, z.B. 'Borddurchlass innerhalb 12 Monaten erneuern'"
    )
    estimated_remaining_life_months: Optional[int] = Field(
        default=None,
        ge=0,
        le=600,
        description="Geschätzte Restlebensdauer in Monaten"
    )
    replacement_cost_eur: Optional[float] = Field(
        default=None,
        ge=0,
        description="Geschätzte Austauschkosten in EUR (Material + Arbeit)"
    )
    urgency: Optional[str] = Field(
        default=None,
        description="'immediate', 'next_haulout', 'planned', 'monitor'"
    )
    photo_refs: list[str] = Field(
        default_factory=list,
        description="Referenzen auf Fotos für visuelle Analyse"
    )
```

(Confidence: documented)

### ThroughHullSystemAssessment — Gesamtbewertung aller Borddurchlässe

```python
class ThroughHullSystemAssessment(BaseModel):
    """Gesamtbewertung aller Borddurchlässe eines Bootes."""
    model_config = {"from_attributes": True}

    boat_id: str = Field(
        ...,
        description="AYDI Boat-ID"
    )
    assessment_date: str = Field(
        ...,
        description="Bewertungsdatum (YYYY-MM-DD)"
    )
    assessor: str = Field(
        default="aydi_system",
        description="'aydi_system', 'surveyor', 'owner'"
    )

    # Inventar
    total_through_hulls: int = Field(
        ...,
        ge=0,
        le=100,
        description="Gesamtanzahl Borddurchlässe"
    )
    below_wl_count: int = Field(
        ...,
        ge=0,
        description="Anzahl unter Wasserlinie"
    )
    above_wl_count: int = Field(
        ...,
        ge=0,
        description="Anzahl über Wasserlinie"
    )
    transom_count: int = Field(
        default=0,
        ge=0,
        description="Anzahl am Spiegel"
    )

    # Bewertungen
    individual_assessments: list[ThroughHullCondition] = Field(
        default_factory=list,
        description="Einzelbewertungen aller Borddurchlässe"
    )
    system_score: float = Field(
        ...,
        ge=0,
        le=100,
        description="Gesamtsystem-Score 0–100"
    )
    system_confidence: ConfidenceLevel = Field(
        ...,
        description="Confidence-Level der Gesamtbewertung"
    )

    # Risikoanalyse
    galvanic_risk: float = Field(
        default=0,
        ge=0,
        le=100,
        description="Galvanisches Risiko 0–100 (Mischung verschiedener Metalle)"
    )
    material_mix_warning: bool = Field(
        default=False,
        description="Warnung bei inkompatibler Material-Mischung"
    )
    missing_seacocks: int = Field(
        default=0,
        ge=0,
        description="Anzahl Durchlässe unter WL ohne Seeventil"
    )
    compliance_iso9093: bool = Field(
        default=False,
        description="ISO 9093 konform?"
    )
    compliance_abyc_h27: bool = Field(
        default=False,
        description="ABYC H-27 konform?"
    )

    # Zusammenfassung
    critical_findings: list[str] = Field(
        default_factory=list,
        description="Kritische Befunde (sofortige Maßnahme)"
    )
    planned_actions: list[str] = Field(
        default_factory=list,
        description="Geplante Maßnahmen (nächstes Haulout)"
    )
    total_replacement_cost_eur: Optional[float] = Field(
        default=None,
        ge=0,
        description="Gesamtkosten aller empfohlenen Maßnahmen in EUR"
    )
    next_inspection_date: Optional[str] = Field(
        default=None,
        description="Empfohlenes nächstes Inspektionsdatum"
    )
```

(Confidence: documented)

---

## Grundlagen

### 7.1 Borddurchlass-Typen

#### 7.1.1 Pilzförmig (Mushroom Type)

Der Standardtyp für Borddurchlässe unter der Wasserlinie. Charakteristisch ist der breite, pilzförmige Flansch auf der Rumpfaußenseite und ein Gewindeschaft, der durch den Rumpf geführt wird. Von innen wird eine Gegenmutter aufgeschraubt, die den Durchlass gegen den Rumpf presst.

| Merkmal | Spezifikation |
|---|---|
| Flansch-Ø (außen) | Nennweite + 20–30 mm |
| Gewindelänge | 25–75 mm (abhängig von Rumpfdicke) |
| Strömungswiderstand | Mittel — Flansch erzeugt leichten Widerstand |
| Einsatz | Alle Anwendungen unter/über WL |
| Vorteil | Einfache Montage, selbstzentrierend |
| Nachteil | Nicht strömungsoptimiert, Flansch als Ansatzpunkt für Bewuchs |
| Typische Hersteller | Groco TH-Serie, Guidi 1210, Osculati 17.319 |

(Confidence: documented)

#### 7.1.2 Flush-Mount (Bündig)

Bündig mit der Rumpfaußenseite eingebaut. Wird bei Rennbooten und Superyachten verwendet, um den Strömungswiderstand zu minimieren. Die Montage erfolgt von innen, der Durchlass wird in eine vorgebohrte Öffnung eingesetzt und von innen verschraubt oder verklebt.

| Merkmal | Spezifikation |
|---|---|
| Flansch | Kein äußerer Flansch, bündig mit Rumpf |
| Strömungswiderstand | Minimal |
| Einsatz | Racing, Superyachten, Geschwindigkeit >15 kn |
| Vorteil | Geringster Widerstand, kein Bewuchs am Flansch |
| Nachteil | Aufwendige Montage, höhere Kosten, schwieriger zu inspizieren |
| Typische Hersteller | Groco STH-Serie, Guidi 1244, Custom-Fertigung |

(Confidence: documented)

#### 7.1.3 Geflancht (Flanged Type)

Beidseitig geflanschte Ausführung mit Schraubverbindung durch den Rumpf. Typisch für größere Nennweiten (>50 mm) und Superyachten. Die Flansche werden von außen und innen mit Schrauben durch den Rumpf verbunden.

| Merkmal | Spezifikation |
|---|---|
| Flansch | Beidseitig, Schraubverbindung |
| Flansch-Ø | Nennweite + 40–60 mm |
| Schraubenanzahl | 4–8, abhängig von Nennweite |
| Einsatz | Superyachten, gewerbliche Schiffe, NW >50 mm |
| Vorteil | Höchste Festigkeit, gleichmäßige Kraftverteilung |
| Nachteil | Aufwendige Montage, viele Bohrungen im Rumpf |
| Typische Hersteller | Groco FTH-Serie, Guidi 1260, Buck Algonquin |

(Confidence: documented)

#### 7.1.4 Scoop-Strainer (Schaufel-Einlass)

Kombinierter Wassereinlass mit integriertem Sieb. Die Schaufelform leitet Wasser aktiv in den Einlass, auch bei geringer Fahrt. Das integrierte Sieb verhindert das Eindringen von Fremdkörpern in das Kühlwassersystem.

| Merkmal | Spezifikation |
|---|---|
| Bauform | Pilzförmig mit Schaufel + Siebkorb |
| Maschenweite Sieb | 3–6 mm (Standard), 1–2 mm (Feinfilter) |
| Strömungswiderstand | Höher als Pilztyp durch Schaufel |
| Einsatz | Motorkühlwasser, Klimaanlage, Watermaker |
| Vorteil | Aktive Wasserförderung, Fremdkörperschutz |
| Nachteil | Bewuchsanfällig, regelmäßige Reinigung nötig |
| Typische Hersteller | Groco SC-Serie, Guidi 1316, Vetus TRC |

(Confidence: documented)

#### 7.1.5 Ablass-Durchführungen (Drain Fittings)

Speziell für Abläufe (Cockpit, Waschbecken, Dusche) konzipierte Durchführungen. Häufig mit konischem Gewinde für selbstdichtende Verbindung.

| Merkmal | Spezifikation |
|---|---|
| Gewinde | Konisch (NPT) oder zylindrisch (BSP) |
| Nennweite | Typisch 19–38 mm |
| Einsatz | Cockpit-Drain, Waschbecken, Duschablauf |
| Seeventil | Über WL: optional, unter WL: Pflicht |
| Typische Hersteller | TruDesign 90400, Osculati 17.320, Plastimo |

(Confidence: documented)

#### 7.1.6 Geber-Durchführungen (Transducer Fittings)

Spezialdurchführungen für Echolot-, Geschwindigkeits- und Temperaturgeber. Müssen den Geber in einer definierten Position und Ausrichtung halten.

| Typ | Nennweite | Montage | Hersteller |
|---|---|---|---|
| Airmar P79 (Tiefe) | 50 mm Bohrung | Einbau-Puck, von innen | Airmar |
| Airmar DST810 (Tiefe/Speed/Temp) | 50 mm Bohrung | Einbau-Puck, von innen | Airmar |
| B&G ForwardScan | 50 mm Bohrung | Durchbruch, Fairing Block | B&G/Navico |
| Garmin GT54UHD | 50 mm Bohrung | Durchbruch, Fairing Block | Garmin |

Kritisch: Geber-Durchführungen unterhalb der Wasserlinie müssen mit einem Blindstopfen verschlossen werden können, wenn der Geber entfernt wird.

(Confidence: documented)

#### 7.1.7 Abgas-Durchführungen (Exhaust Fittings)

Durchführungen für nasse und trockene Abgassysteme. Besondere Anforderungen an Temperaturbeständigkeit und Materialwahl.

| Typ | Material | Max. Temperatur | Norm |
|---|---|---|---|
| Nass-Abgas (Wassergekühlter Auspuff) | Bronze C83600, 316L | 120 °C | ISO 9093-1, ABYC P-1 |
| Trocken-Abgas | 316L, Inconel | 500 °C | ABYC P-1 |
| Generator-Abgas | Bronze, 316L | 120 °C (nass) | ISO 9093-1, ABYC P-1 |

ABYC H-27 Sonderregel: Abgas-Borddurchlässe müssen aus Metall sein, Kunststoff ist nicht zulässig.

(Confidence: documented)

#### 7.1.8 Cockpit-Drain-Durchführungen

Cockpit-Abläufe über dem Spiegel oder durch den Rumpf. Dimensionierung nach ISO 11812 (Cockpit-Volumen und Drainrate).

| Bootstrap-Klasse | Min. Cockpit-Drain NW | Anzahl | Norm |
|---|---|---|---|
| Segelboot 8–10 m | 25 mm (1") | 2 | ISO 11812 |
| Segelboot 10–14 m | 32 mm (1¼") | 2 | ISO 11812 |
| Segelboot 14–18 m | 38 mm (1½") | 2–4 | ISO 11812 |
| Motorboot 8–12 m | 25 mm (1") | 2 | ISO 11812 |
| Motorboot 12–20 m | 32 mm (1¼") | 2–4 | ISO 11812 |

(Confidence: documented)

### 7.2 Materialien

#### 7.2.1 Bronze — Der klassische Werkstoff

Bronze ist seit Jahrhunderten der Standard-Werkstoff für marine Beschläge. Für Borddurchlässe werden spezielle Seewasser-beständige Legierungen verwendet.

| Legierung | UNS | Cu | Sn | Zn | Pb | Einsatz |
|---|---|---|---|---|---|---|
| Rotguss C83600 | C83600 | 85 % | 5 % | 5 % | 5 % | Standard-Borddurchlass |
| C84400 | C84400 | 81 % | 3 % | 7 % | 9 % | Günstigere Alternative |
| Navy-Bronze C92200 | C92200 | 88 % | 6 % | — | 1,5 % | Premium, kein Zink |
| Aluminium-Bronze | C95400 | 85 % | — | — | — | Spezialanwendungen |
| Nickelaluminiumbronze | C95800 | 81 % | — | — | — | Superyachten, höchste Festigkeit |

**Kritische Warnung: Messing vs. Bronze**

Messing (Cu-Zn-Legierungen mit >15 % Zink) ist **NICHT** für Borddurchlässe unter der Wasserlinie geeignet. Der hohe Zinkanteil führt zu **Entzinkung** (Dezincification): Das Zink löst sich heraus, es bleibt eine poröse, kupferfarbene Struktur zurück, die keine mechanische Festigkeit mehr hat.

| Material | Zinkanteil | Entzinkungsrisiko | Empfehlung |
|---|---|---|---|
| Bronze C83600 | 5 % | Sehr gering | Empfohlen |
| Bronze C92200 | 0 % | Null | Beste Wahl |
| Messing CW617N | 37 % | **Sehr hoch** | **NICHT verwenden** |
| Messing CW614N | 39 % | **Extrem hoch** | **NICHT verwenden** |

(Confidence: documented)

#### 7.2.2 Edelstahl 316L

Austenitischer Edelstahl mit Molybdänzusatz für verbesserte Seewasserbeständigkeit.

| Eigenschaft | Wert |
|---|---|
| Werkstoffnummer | 1.4404 / AISI 316L |
| Zusammensetzung | Fe-17Cr-12Ni-2,5Mo-0,03C |
| Zugfestigkeit | 485–690 MPa |
| Streckgrenze | 170–310 MPa |
| Korrosionsbeständigkeit | Gut in belüftetem Seewasser |
| Lochfraßrisiko | Bei >25 °C Wassertemperatur erhöht |
| Spaltkorrosionsrisiko | Bei sauerstoffarmen Bereichen erhöht |
| Empfehlung | Über WL: uneingeschränkt. Unter WL: bedingt, nicht in tropischen Gewässern |

**Warnung**: 316L ist in Spalten (z.B. Gewinde unter WL) anfällig für Spaltkorrosion. In warmen Gewässern (>25 °C) kann Lochfraß auftreten. Bronze ist unter WL in den meisten Fällen die sicherere Wahl.

(Confidence: documented)

#### 7.2.3 Marelon (Forespar) / TruDesign Composites

Glasfaserverstärktes Polyamid, speziell für marine Anwendungen entwickelt. Galvanisch inert, korrosionsfrei, leicht.

| Eigenschaft | Marelon (Forespar) | TruDesign (90-Serie) |
|---|---|---|
| Basispolymer | PA66-GF30 | PA66-GF30 |
| Zugfestigkeit | 82 MPa | 85 MPa |
| Biegefestigkeit | 130 MPa | 135 MPa |
| Temperaturbereich | -30 bis +82 °C | -30 bis +93 °C |
| UV-Beständigkeit | Gut (stabilisiert) | Gut (stabilisiert) |
| Brandverhalten | UL 94 V-0 | UL 94 V-0 |
| Gewicht vs. Bronze | ~80 % leichter | ~80 % leichter |
| Galvanische Korrosion | Keine | Keine |
| ISO 9093-2 konform | Ja | Ja |
| ABYC H-27 konform | Ja (UL-listed) | Ja (UL-listed) |
| Ideal für | Aluminium-Rümpfe, galvanisch belastete Boote | Aluminium-Rümpfe, Neubauten |

(Confidence: documented)

#### 7.2.4 Materialvergleich — Entscheidungsmatrix

| Kriterium | Bronze C83600 | 316L | Marelon | TruDesign |
|---|---|---|---|---|
| Preis (3/4") | ~45 EUR | ~55 EUR | ~22 EUR | ~25 EUR |
| Lebensdauer | 30–50 Jahre | 20–40 Jahre | 15–25 Jahre | 15–25 Jahre |
| Galvanische Verträglichkeit | Mittel | Schlecht mit Alu | Inert | Inert |
| Festigkeit | Hoch | Sehr hoch | Mittel | Mittel |
| Temperaturbeständigkeit | >250 °C | >500 °C | 82 °C | 93 °C |
| Gewicht | Hoch | Hoch | Gering | Gering |
| Bewuchsresistenz | Kupfer wirkt antifouling | Kein Antifouling | Kein Antifouling | Kein Antifouling |
| Für Aluminium-Rumpf | **NEIN** (galvanisch) | **Bedingt** | **JA** | **JA** |
| Für Stahl-Rumpf | JA | JA (gleiche Potenziale) | JA | JA |
| Für GFK-Rumpf | JA | JA | JA | JA |
| Für Holz-Rumpf | JA | JA | JA | JA |

(Confidence: documented)

### 7.3 Gewindestandards

#### 7.3.1 BSP — British Standard Pipe (ISO 228)

| Bezeichnung | Außen-Ø mm | Innen-Ø mm | Steigung mm | TPI | Dichtung |
|---|---|---|---|---|---|
| 1/2" BSP | 20,955 | 18,631 | 1,814 | 14 | Flachdichtung/PTFE |
| 3/4" BSP | 26,441 | 24,117 | 1,814 | 14 | Flachdichtung/PTFE |
| 1" BSP | 33,249 | 30,291 | 2,309 | 11 | Flachdichtung/PTFE |
| 1-1/4" BSP | 41,910 | 38,952 | 2,309 | 11 | Flachdichtung/PTFE |
| 1-1/2" BSP | 47,803 | 44,845 | 2,309 | 11 | Flachdichtung/PTFE |
| 2" BSP | 59,614 | 56,656 | 2,309 | 11 | Flachdichtung/PTFE |

BSP-Gewinde ist **zylindrisch** (BSP-P / G-Gewinde) — dichtet über Flachdichtung oder PTFE-Band, nicht über Gewindeform.

(Confidence: documented)

#### 7.3.2 NPT — National Pipe Thread (ANSI B1.20.1)

| Bezeichnung | Außen-Ø mm | TPI | Konizität | Dichtung |
|---|---|---|---|---|
| 1/2" NPT | 21,223 | 14 | 1:16 | Konisch, selbstdichtend |
| 3/4" NPT | 26,568 | 14 | 1:16 | Konisch, selbstdichtend |
| 1" NPT | 33,401 | 11,5 | 1:16 | Konisch, selbstdichtend |
| 1-1/4" NPT | 42,164 | 11,5 | 1:16 | Konisch, selbstdichtend |
| 1-1/2" NPT | 48,054 | 11,5 | 1:16 | Konisch, selbstdichtend |
| 2" NPT | 60,325 | 11,5 | 1:16 | Konisch, selbstdichtend |

NPT-Gewinde ist **konisch** — dichtet durch die Keilwirkung des Gewindes. PTFE-Band oder Gewindedichtpaste zusätzlich empfohlen.

**Kritische Warnung**: BSP und NPT sind **NICHT** kompatibel! Obwohl die Nennmaße ähnlich sind, unterscheiden sich Konizität und Steigung. Ein NPT-Fitting auf einem BSP-Seeventil dichtet initial, versagt aber unter Last oder Vibration.

(Confidence: documented)

#### 7.3.3 Metrisches Gewinde

Selten bei Borddurchlässen, gelegentlich bei europäischen Herstellern (Guidi, Osculati):

| Bezeichnung | Außen-Ø mm | Steigung mm |
|---|---|---|
| M20×1,5 | 20,0 | 1,5 |
| M27×2,0 | 27,0 | 2,0 |
| M33×2,0 | 33,0 | 2,0 |
| M42×2,0 | 42,0 | 2,0 |
| M48×2,0 | 48,0 | 2,0 |

(Confidence: documented)

### 7.4 Anforderungen über/unter Wasserlinie

#### 7.4.1 Unter Wasserlinie (Below WL)

| Anforderung | Spezifikation | Norm |
|---|---|---|
| Seeventil | **Pflicht** (Kugelhahn oder Kükenventil) | ISO 9093, ABYC H-27 |
| Material | Bronze, 316L, Marelon/TruDesign | ISO 9093-1/2 |
| Dichtstoff | Polysulfid oder PU (Sikaflex 291i) | — |
| Backing-Plate | **Pflicht** bei GFK/Sandwich | Best Practice |
| Kern-Entfernung | **Pflicht** bei Sandwich-Bauweise | ISO 12215, Lloyd's |
| Doppelte Schlauchschellen | **Pflicht** | ABYC H-27 |
| Notholzstopfen | **Pflicht** (CE Kat. A/B), an Schnur befestigt | RCD 2013/53/EU |
| Erdungsverbindung | An Bonding-System anschließen (metallisch) | ABYC E-11 |

(Confidence: documented)

#### 7.4.2 Auf Wasserlinie (At WL)

Durchlässe, die bei Krängung oder Beladung unter Wasser kommen können:

| Anforderung | Spezifikation |
|---|---|
| Seeventil | **Empfohlen** (bei CE Kat. A/B: Pflicht) |
| Material | Wie unter WL |
| Besonderheit | Krängungswinkel berücksichtigen: Bei 25° Krängung kann ein Durchlass 300 mm über WL unter Wasser liegen |
| Berechnung | Eintauchtiefe = Beamhalf × sin(Krängungswinkel) |

(Confidence: calculated)

#### 7.4.3 Über Wasserlinie (Above WL)

| Anforderung | Spezifikation |
|---|---|
| Seeventil | Optional, empfohlen für Cockpit-Drains |
| Material | Alle Materialien zulässig, auch Nylon/Delrin |
| Dichtstoff | Polysulfid, PU, Silikon zulässig |
| Schlauchschellen | Einfach ausreichend |

(Confidence: documented)

### 7.5 Geber-Durchführungen im Detail

#### 7.5.1 Echolot-Geber (Depth Transducer)

| Geber-Typ | Frequenz | Abstrahlwinkel | Einbau | Bohrung |
|---|---|---|---|---|
| Airmar P79 | 200 kHz | 18° konisch | In-Hull oder Through-Hull | 50 mm |
| Airmar P319 | 200 kHz | 12° konisch | Through-Hull, Tilt | 50 mm |
| Airmar B75H | 130–210 kHz | 24°/12° | Through-Hull, Bronze | 55 mm |
| Garmin GT20-TH | 77/200 kHz | 24°/16° | Through-Hull, Kunststoff | 50 mm |

**Einbauregeln:**
- Mindestabstand zum Kiel: 300 mm
- Frei von Luftblasen (nicht hinter Stufen, Kimmknick)
- Fairing Block für korrekte Ausrichtung bei V-förmigem Rumpf
- Nicht im Bereich der Propellerströmung

(Confidence: documented)

#### 7.5.2 Geschwindigkeitsgeber (Speed/Paddlewheel Transducer)

| Geber-Typ | Messprinzip | Einbau | Bohrung |
|---|---|---|---|
| Airmar DST810 | Ultraschall (Tiefe/Speed/Temp) | Through-Hull | 50 mm |
| B&G Paddlewheel | Impeller | Through-Hull | 33 mm |
| Raymarine P120 | Impeller | Through-Hull | 33 mm |

**Einbauregeln:**
- Position: Mittschiffs, außerhalb Grenzschicht
- Paddelrad muss frei drehen können
- Blindstopfen für Herausnahme unter Wasser

(Confidence: documented)

### 7.6 Abgas-Durchführungen im Detail

#### 7.6.1 Nass-Abgassystem (Wet Exhaust)

Im Nass-Abgassystem wird Kühlwasser in den Abgasstrom eingespritzt. Die Abgastemperatur sinkt von 400–600 °C auf 50–80 °C. Der Borddurchlass am Rumpf führt das Wasser-Abgas-Gemisch nach außen.

| Parameter | Spezifikation |
|---|---|
| Temperatur am Durchlass | 50–80 °C (normal), max. 120 °C (Alarm) |
| Material Durchlass | Bronze C83600, 316L (kein Kunststoff!) |
| Nennweite | = Abgas-Schlauchdurchmesser, typisch 38–76 mm |
| Position | Am Spiegel (bevorzugt) oder seitlich über WL |
| Rückschlagventil | Empfohlen bei Durchlass nahe WL |
| Gummiklappe | Häufig außen montiert, verhindert Wasserrücklauf bei Rückwärtsfahrt |

(Confidence: documented)

#### 7.6.2 Generator-Abgas

| Parameter | Spezifikation |
|---|---|
| Temperatur | 40–70 °C (nassgekühlter Generator) |
| Nennweite | Typisch 25–38 mm |
| Material | Bronze oder 316L |
| Position | Seitlich über WL, min. 150 mm über WL |

(Confidence: documented)

### 7.7 Scoop-Strainer im Detail

#### 7.7.1 Typen und Dimensionierung

| Hersteller | Modell | NW mm | Maschenweite mm | Material | Preis EUR |
|---|---|---|---|---|---|
| Groco | SC-500 | 13 | 3 | Bronze | 65 |
| Groco | SC-750 | 19 | 3 | Bronze | 85 |
| Groco | SC-1000 | 25 | 4 | Bronze | 110 |
| Groco | SC-1500 | 38 | 5 | Bronze | 155 |
| Guidi | 1316/13 | 13 | 3 | Bronze | 55 |
| Guidi | 1316/19 | 19 | 3 | Bronze | 75 |
| Guidi | 1316/25 | 25 | 4 | Bronze | 95 |
| Vetus | TRC3/4 | 19 | 3 | Bronze | 80 |
| Vetus | TRC1 | 25 | 4 | Bronze | 105 |
| Vetus | TRC11/2 | 38 | 5 | Bronze | 140 |

(Confidence: documented)

#### 7.7.2 Wartung

- **Monatlich** (Tropische Gewässer): Sieb reinigen, Bewuchs entfernen
- **Vierteljährlich** (Gemäßigte Gewässer): Sieb reinigen
- **Jährlich**: Scoop-Strainer komplett prüfen, Dichtigkeit kontrollieren
- **Alle 5 Jahre**: Ersetzen oder professionell überholen

(Confidence: benchmark)

### 7.8 Backing-Plates und Kernverstärkung

#### 7.8.1 Backing-Plates für GFK-Rümpfe (Solid Laminate)

| Parameter | Anforderung |
|---|---|
| Material | GFK-Platte, G10/FR4 (Glasfaser-Epoxid), Edelstahl 316L |
| Dicke | Min. 6 mm GFK, min. 5 mm G10, min. 3 mm 316L |
| Durchmesser/Fläche | Min. 3× Nennweite des Durchlasses, z.B. 3/4" → min. 57 mm Ø |
| Form | Rund oder quadratisch, Kanten entgratet |
| Montage | Zwischen Gegenmutter und Rumpfinnenseite, mit Dichtstoff |
| Lloyd's Anforderung | Min. 10 mm GFK, min. 3× Durchmesser |

(Confidence: documented)

#### 7.8.2 Kernverstärkung bei Sandwich-Bauweise

Bei Sandwich-Rümpfen (PVC-Schaum, Balsa, Honeycomb) muss der Kern im Bereich des Borddurchlasses entfernt und durch Vollaminat oder Epoxy/Glasfaser-Füllung ersetzt werden. Ohne Kernverstärkung drückt die Gegenmutter den Kern zusammen, die Verbindung wird lose.

**Verfahren:**

1. Bohrung für Borddurchlass bohren (Kernbohrer)
2. Kern ringförmig entfernen: Radius = 2× Durchlass-Nennweite
3. Hohlraum mit thixotropem Epoxid füllen (z.B. West System 105/206 + 403 Microfibers)
4. Aushärten lassen (min. 24 h bei 20 °C)
5. Bohrung für Durchlass durch die Epoxid-Füllung bohren
6. Backing-Plate montieren

| Kernmaterial | Kern-Entfernungs-Radius | Füllmaterial |
|---|---|---|
| PVC-Schaum (Divinycell) | 2× NW, min. 30 mm | Epoxid + Glasfaserschnitzel |
| Balsa | 2,5× NW, min. 40 mm | Epoxid + Microfibers (kein Wasser!) |
| Honeycomb (Nomex) | 2× NW, min. 30 mm | Epoxid + Glasfaserschnitzel |

**Kritische Warnung**: Bei Balsa-Kern ist besondere Sorgfalt nötig. Balsa saugt Wasser wie ein Schwamm — jede Undichtigkeit an einem Borddurchlass führt zur Wasseraufnahme im gesamten Balsa-Kern. Geschätzte Schadenshöhe bei kompromittiertem Balsa-Kern: **5.000–50.000 EUR** je nach Boots-Größe.

(Confidence: documented)

### 7.9 Dichtstoffe für Borddurchlass-Montage

#### 7.9.1 Unter Wasserlinie — zugelassene Dichtstoffe

| Dichtstoff | Typ | Haftung auf GFK | Haftung auf Bronze | Seewasser-beständig | Demontierbar | Empfehlung |
|---|---|---|---|---|---|---|
| 3M 101 (Life-Calk) | Polysulfid | Sehr gut | Sehr gut | Ja | Ja (nach Jahren mühsam) | **Erste Wahl unter WL** |
| Boat-Life Life-Calk | Polysulfid | Sehr gut | Sehr gut | Ja | Ja | **Erste Wahl unter WL** |
| Sikaflex 291i | Polyurethan | Exzellent | Gut | Ja | Schwierig | **Zweite Wahl unter WL** |
| 3M 5200 | Polyurethan | Exzellent | Gut | Ja | Extrem schwierig | Nur bei permanenter Montage |
| Sikaflex 292i | Polyurethan (strukturell) | Exzellent | Gut | Ja | Nicht demontierbar | Nur bei permanenter Verklebung |
| Butylband | Butyl | Gut | Gut | Ja | Ja (einfach) | Nur bei druckbelasteter Verbindung |

(Confidence: documented)

#### 7.9.2 NICHT zugelassene Dichtstoffe unter WL

| Dichtstoff | Grund |
|---|---|
| Silikon (Dow Corning, etc.) | Schlechte Haftung auf GFK, kriecht unter Last |
| Acryl | Nicht wasserfest |
| Dichthanf + Paste | Veraltet, quillt und löst sich |
| Teflon-Band allein | Nur für Gewindedichtung, nicht für Flansch |

(Confidence: documented)

### 7.10 Galvanische Korrosion und Bonding

#### 7.10.1 Galvanische Spannungsreihe in Seewasser

| Material | Potenzial (V vs. Ag/AgCl) | Bereich |
|---|---|---|
| Magnesium | -1,60 bis -1,63 | Anodisch (opfert sich) |
| Zink | -0,98 bis -1,03 | Anodisch |
| Aluminium (5000er) | -0,75 bis -1,00 | Anodisch |
| Stahl / Gusseisen | -0,60 bis -0,71 | Anodisch |
| Bronze C83600 | -0,28 bis -0,36 | Mittel |
| Kupfer | -0,30 bis -0,36 | Mittel |
| Edelstahl 316L (passiv) | -0,05 bis -0,10 | Kathodisch |
| Titan | -0,05 bis +0,06 | Kathodisch |
| Graphit / Kohlefaser | +0,20 bis +0,30 | Kathodisch (edelste) |

**Regel**: Potentialdifferenz >200 mV → galvanische Korrosion wahrscheinlich.

(Confidence: documented)

#### 7.10.2 Bronze neben Aluminium — Die häufigste Falle

Bronze-Borddurchlässe in einem Aluminium-Rumpf verursachen **katastrophale galvanische Korrosion** am Aluminium. Potentialdifferenz: ~500 mV → der Aluminium-Rumpf löst sich auf.

**Einzige Lösung**: Kunststoff-Borddurchlässe (Marelon, TruDesign) oder Titan in Aluminium-Rümpfen. **KEIN** Bronze, **KEIN** Edelstahl.

| Rumpfmaterial | Empfohlenes Durchlass-Material | Verbotenes Material |
|---|---|---|
| GFK | Bronze, 316L, Marelon, TruDesign | Messing |
| Aluminium | Marelon, TruDesign, Titan | **Bronze, Edelstahl, Kupfer** |
| Stahl | 316L, Bronze, Marelon | Messing |
| Holz | Bronze, Marelon | Messing |

(Confidence: documented)

#### 7.10.3 Bonding-System

Alle metallischen Borddurchlässe unter der Wasserlinie sollten elektrisch mit dem Bonding-System (Erdungssystem) verbunden werden:

| Komponente | Kabelquerschnitt | Verbindung |
|---|---|---|
| Borddurchlass → Bonding-Bus | Min. 6 mm² (AWG 10) verzinntes Kupfer | Crimpverbindung mit Ringkabelschuh |
| Bonding-Bus → Zinkanode | Min. 10 mm² (AWG 8) | Schraubverbindung |
| Bonding-Bus → Landstrom-Galvanic-Isolator | Min. 16 mm² (AWG 6) | Schraubverbindung |

(Confidence: documented)

### 7.11 Borddurchlass-Inventar nach Boots-Größe

#### 7.11.1 Segelboot 8–10 m (z.B. Beneteau Oceanis 30.1)

| Nr. | System | Position | NW mm | Typ | Material | Seeventil |
|---|---|---|---|---|---|---|
| BD-001 | Motor Kühlwasser Einlass | Mittschiffs Stb, unter WL | 19 | Scoop | Bronze | Ja |
| BD-002 | Abgas Auslass | Spiegel, über WL | 38 | Mushroom | Bronze | Nein |
| BD-003 | Toilette Einlass | Mittschiffs Bb, unter WL | 19 | Mushroom | Bronze | Ja |
| BD-004 | Toilette Auslass | Mittschiffs Bb, unter WL | 25 | Mushroom | Bronze | Ja |
| BD-005 | Waschbecken Pantry | Mittschiffs Stb, über WL | 19 | Drain | Kunststoff | Nein |
| BD-006 | Echolot Geber | Mittschiffs, unter WL | 50 | Transducer | Kunststoff | Nein |
| BD-007 | Cockpit Drain Bb | Spiegel, über WL | 25 | Drain | Kunststoff | Nein |
| BD-008 | Cockpit Drain Stb | Spiegel, über WL | 25 | Drain | Kunststoff | Nein |

**Gesamt: 8 Borddurchlässe** (3 unter WL mit Seeventil)

(Confidence: benchmark)

#### 7.11.2 Segelboot 10–14 m (z.B. Bavaria C42)

| Nr. | System | Position | NW mm | Typ | Material | Seeventil |
|---|---|---|---|---|---|---|
| BD-001 | Motor Kühlwasser Einlass | Mittschiffs Stb, unter WL | 25 | Scoop | Bronze | Ja |
| BD-002 | Abgas Auslass | Spiegel, über WL | 50 | Mushroom | Bronze | Nein |
| BD-003 | Toilette Bug Einlass | Vorschiff Bb, unter WL | 19 | Mushroom | Bronze | Ja |
| BD-004 | Toilette Bug Auslass | Vorschiff Bb, unter WL | 25 | Mushroom | Bronze | Ja |
| BD-005 | Toilette Achtern Einlass | Achtern Stb, unter WL | 19 | Mushroom | Bronze | Ja |
| BD-006 | Toilette Achtern Auslass | Achtern Stb, unter WL | 25 | Mushroom | Bronze | Ja |
| BD-007 | Waschbecken Pantry | Mittschiffs Stb, über WL | 19 | Drain | Marelon | Nein |
| BD-008 | Waschbecken Bad Bug | Vorschiff Bb, über WL | 19 | Drain | Marelon | Nein |
| BD-009 | Waschbecken Bad Achtern | Achtern Stb, über WL | 19 | Drain | Marelon | Nein |
| BD-010 | Echolot Geber | Mittschiffs, unter WL | 50 | Transducer | Kunststoff | Nein |
| BD-011 | Log/Speed Geber | Mittschiffs, unter WL | 33 | Transducer | Kunststoff | Nein |
| BD-012 | Cockpit Drain Bb | Spiegel, über WL | 32 | Drain | Kunststoff | Nein |
| BD-013 | Cockpit Drain Stb | Spiegel, über WL | 32 | Drain | Kunststoff | Nein |

**Gesamt: 13 Borddurchlässe** (6 unter WL mit Seeventil)

(Confidence: benchmark)

#### 7.11.3 Segelboot 14–18 m (z.B. Hallberg-Rassy 48)

| Nr. | System | NW mm | Unter WL? | Seeventil |
|---|---|---|---|---|
| BD-001 | Motor Kühlwasser Einlass | 32 | Ja | Ja |
| BD-002 | Motor Abgas Auslass | 50 | Nein | Nein |
| BD-003 | Toilette 1 Einlass | 19 | Ja | Ja |
| BD-004 | Toilette 1 Auslass | 25 | Ja | Ja |
| BD-005 | Toilette 2 Einlass | 19 | Ja | Ja |
| BD-006 | Toilette 2 Auslass | 25 | Ja | Ja |
| BD-007 | Toilette 3 Einlass | 19 | Ja | Ja |
| BD-008 | Toilette 3 Auslass | 25 | Ja | Ja |
| BD-009 | Waschbecken Pantry | 19 | Nein | Nein |
| BD-010 | Waschbecken Bad 1 | 19 | Nein | Nein |
| BD-011 | Waschbecken Bad 2 | 19 | Nein | Nein |
| BD-012 | Waschbecken Bad 3 | 19 | Nein | Nein |
| BD-013 | Echolot Geber | 50 | Ja | Nein |
| BD-014 | Log/Speed Geber | 33 | Ja | Nein |
| BD-015 | Klimaanlage Einlass | 25 | Ja | Ja |
| BD-016 | Klimaanlage Auslass | 25 | Nein | Nein |
| BD-017 | Watermaker Einlass | 19 | Ja | Ja |
| BD-018 | Cockpit Drain Bb | 32 | Nein | Nein |
| BD-019 | Cockpit Drain Stb | 32 | Nein | Nein |
| BD-020 | Generator Kühlwasser | 19 | Ja | Ja |
| BD-021 | Generator Abgas | 38 | Nein | Nein |

**Gesamt: 21 Borddurchlässe** (13 unter WL, 11 mit Seeventil)

(Confidence: benchmark)

#### 7.11.4 Motoryacht 10–15 m (z.B. Bavaria SR41)

| Nr. | System | NW mm | Unter WL? | Seeventil |
|---|---|---|---|---|
| BD-001 | Motor 1 Kühlwasser Einlass | 32 | Ja | Ja |
| BD-002 | Motor 1 Abgas Auslass | 50 | Nein | Nein |
| BD-003 | Motor 2 Kühlwasser Einlass | 32 | Ja | Ja |
| BD-004 | Motor 2 Abgas Auslass | 50 | Nein | Nein |
| BD-005 | Toilette 1 Einlass | 19 | Ja | Ja |
| BD-006 | Toilette 1 Auslass | 25 | Ja | Ja |
| BD-007 | Toilette 2 Einlass | 19 | Ja | Ja |
| BD-008 | Toilette 2 Auslass | 25 | Ja | Ja |
| BD-009 | Waschbecken Pantry | 19 | Nein | Nein |
| BD-010 | Waschbecken Bad 1 | 19 | Nein | Nein |
| BD-011 | Waschbecken Bad 2 | 19 | Nein | Nein |
| BD-012 | Echolot Geber | 50 | Ja | Nein |
| BD-013 | Log/Speed Geber | 33 | Ja | Nein |
| BD-014 | Klimaanlage Einlass | 25 | Ja | Ja |
| BD-015 | Klimaanlage Auslass | 25 | Nein | Nein |
| BD-016 | Generator Kühlwasser | 25 | Ja | Ja |
| BD-017 | Generator Abgas | 38 | Nein | Nein |
| BD-018 | Cockpit Drain 1 | 32 | Nein | Nein |
| BD-019 | Cockpit Drain 2 | 32 | Nein | Nein |
| BD-020 | Bilgenpumpe Auslass | 25 | Nein | Nein |

**Gesamt: 20 Borddurchlässe** (10 unter WL, 8 mit Seeventil)

(Confidence: benchmark)

#### 7.11.5 Superyacht 20–30 m

| Kategorie | Typische Anzahl | Bemerkung |
|---|---|---|
| Motorkühlwasser (Haupt) | 2–4 | Redundante Systeme |
| Motorkühlwasser (Generator) | 1–2 | |
| Abgas (Haupt + Gen.) | 2–4 | Am Spiegel |
| Toiletten | 6–12 | 3–6 Heads × Einlass + Auslass |
| Waschbecken / Dusche | 4–8 | Über WL |
| Klimaanlage | 2–4 | Zentral oder dezentral |
| Watermaker | 1–2 | Einlass + Sole-Auslass |
| Stabilisatoren | 2–4 | Hydraulik-Kühlung |
| Bug-/Heckstrahler | 1–2 | Kühlwasser |
| Feuerlöschsystem | 1–2 | Seewasser-Einlass |
| Instrumente | 2–4 | Echolot, Speed, etc. |
| Cockpit/Deck-Drains | 4–8 | |
| Bilgenpumpen | 2–4 | |
| **Gesamt** | **30–60** | |

(Confidence: benchmark)

---

## Hersteller — Vollständige Übersicht

### Groco (USA) — Der Branchenstandard

**Unternehmen**: Gross Mechanical Laboratories, Inc., Baltimore, Maryland, USA. Gegründet 1926. Weltweit führender Hersteller von Bronze-Borddurchlässen und Seeventilen für Yachten.

#### TH-Serie — Standard Mushroom Through-Hull Fittings (Bronze)

| Modell | NW Zoll | NW mm | Gewinde | Material | Preis EUR |
|---|---|---|---|---|---|
| TH-500-W | 1/2" | 13 | 1/2" NPT | Bronze C83600 | 32 |
| TH-750-W | 3/4" | 19 | 3/4" NPT | Bronze C83600 | 42 |
| TH-1000-W | 1" | 25 | 1" NPT | Bronze C83600 | 55 |
| TH-1250-W | 1-1/4" | 32 | 1-1/4" NPT | Bronze C83600 | 72 |
| TH-1500-W | 1-1/2" | 38 | 1-1/2" NPT | Bronze C83600 | 95 |
| TH-2000-W | 2" | 50 | 2" NPT | Bronze C83600 | 135 |

(Confidence: documented)

#### STH-Serie — Flush/Streamlined Through-Hull Fittings

| Modell | NW Zoll | Gewinde | Material | Preis EUR |
|---|---|---|---|---|
| STH-500-W | 1/2" | 1/2" NPT | Bronze C83600 | 48 |
| STH-750-W | 3/4" | 3/4" NPT | Bronze C83600 | 62 |
| STH-1000-W | 1" | 1" NPT | Bronze C83600 | 78 |
| STH-1250-W | 1-1/4" | 1-1/4" NPT | Bronze C83600 | 98 |
| STH-1500-W | 1-1/2" | 1-1/2" NPT | Bronze C83600 | 125 |

(Confidence: documented)

#### SC-Serie — Scoop Strainers

| Modell | NW Zoll | Maschenweite mm | Material | Preis EUR |
|---|---|---|---|---|
| SC-500 | 1/2" | 3 | Bronze C83600 | 65 |
| SC-750 | 3/4" | 3 | Bronze C83600 | 85 |
| SC-1000 | 1" | 4 | Bronze C83600 | 110 |
| SC-1250 | 1-1/4" | 4 | Bronze C83600 | 135 |
| SC-1500 | 1-1/2" | 5 | Bronze C83600 | 155 |
| SC-2000 | 2" | 5 | Bronze C83600 | 195 |

(Confidence: documented)

#### BV-Serie — Ball Valve Seacocks

| Modell | NW Zoll | Gewinde | Material | Preis EUR |
|---|---|---|---|---|
| BV-500 | 1/2" | 1/2" NPT | Bronze C83600 | 85 |
| BV-750 | 3/4" | 3/4" NPT | Bronze C83600 | 105 |
| BV-1000 | 1" | 1" NPT | Bronze C83600 | 135 |
| BV-1250 | 1-1/4" | 1-1/4" NPT | Bronze C83600 | 175 |
| BV-1500 | 1-1/2" | 1-1/2" NPT | Bronze C83600 | 225 |
| BV-2000 | 2" | 2" NPT | Bronze C83600 | 295 |

(Confidence: documented)

#### IBV-Serie — In-Line Ball Valve

| Modell | NW Zoll | Anschluss | Material | Preis EUR |
|---|---|---|---|---|
| IBV-500 | 1/2" | Hose Barb | Bronze | 52 |
| IBV-750 | 3/4" | Hose Barb | Bronze | 65 |
| IBV-1000 | 1" | Hose Barb | Bronze | 82 |
| IBV-1250 | 1-1/4" | Hose Barb | Bronze | 105 |
| IBV-1500 | 1-1/2" | Hose Barb | Bronze | 135 |

(Confidence: documented)

### TruDesign (Neuseeland) — Kunststoff-Revolution

**Unternehmen**: TruDesign Plastics Ltd., Auckland, Neuseeland. ISO 9093-2 zertifiziert. Spezialist für glasfaserverstärkte Polyamid-Borddurchlässe. Besonders beliebt für Aluminium-Rümpfe und galvanisch belastete Boote.

#### 90400-Serie — Standard Skin Fittings

| Modell | NW Zoll | NW mm | Gewinde | Farbe | Preis EUR |
|---|---|---|---|---|---|
| 90401 | 1/2" | 13 | BSP | Weiß | 15 |
| 90402 | 3/4" | 19 | BSP | Weiß | 18 |
| 90403 | 1" | 25 | BSP | Weiß | 22 |
| 90404 | 1-1/4" | 32 | BSP | Weiß | 28 |
| 90405 | 1-1/2" | 38 | BSP | Weiß | 35 |
| 90406 | 2" | 50 | BSP | Weiß | 48 |

Alle TruDesign-Fittings sind in Weiß und Schwarz erhältlich. BSP-Gewinde Standard, NPT auf Anfrage.

(Confidence: documented)

#### 90600-Serie — Ball Valve Seacocks

| Modell | NW Zoll | Anschluss | Material | Preis EUR |
|---|---|---|---|---|
| 90601 | 1/2" | BSP + Hose | PA66-GF30 | 42 |
| 90602 | 3/4" | BSP + Hose | PA66-GF30 | 52 |
| 90603 | 1" | BSP + Hose | PA66-GF30 | 65 |
| 90604 | 1-1/4" | BSP + Hose | PA66-GF30 | 82 |
| 90605 | 1-1/2" | BSP + Hose | PA66-GF30 | 105 |
| 90606 | 2" | BSP + Hose | PA66-GF30 | 135 |

(Confidence: documented)

#### TruDesign Vorteile im Vergleich

| Vorteil | Beschreibung |
|---|---|
| Galvanisch inert | Keine Korrosion, keine Anoden nötig |
| Leicht | ~80 % Gewichtsersparnis gegenüber Bronze |
| Farblich anpassbar | Weiß/Schwarz — verschwindet optisch |
| Einfache Bearbeitung | Kann mit Standardwerkzeug bearbeitet werden |
| Integrated System | Fitting + Seeventil + Tülle als System |
| Temperatur | Max. 93 °C — höher als Marelon (82 °C) |

(Confidence: documented)

### Blakes (UK) — Traditionshersteller

**Unternehmen**: Blakes Lavac Taylors Ltd., Gosport, Hampshire, UK. Traditioneller britischer Hersteller von Seeventilen und Borddurchlässen, bekannt für hochwertige Bronze-Qualität.

| Serie | Typ | Material | NW-Bereich | Gewinde | Preis-Bereich EUR |
|---|---|---|---|---|---|
| Seacock 2020 | Kugelhahn | Bronze DZR | 3/4"–2" | BSP | 85–285 |
| Blake Baby | Kükenventil | Bronze | 1/2"–1" | BSP | 65–120 |
| Blake Standard | Kükenventil | Bronze | 3/4"–2" | BSP | 95–250 |
| Skin Fitting | Mushroom | Bronze | 1/2"–2" | BSP | 28–95 |

DZR = Dezincification Resistant (entzinkungsbeständig)

(Confidence: documented)

### Forespar (USA) — Marelon-Erfinder

**Unternehmen**: Forespar Products Corp., Rancho Dominguez, Kalifornien, USA. Erfinder des Marelon-Werkstoffs (glasfaserverstärktes Polyamid für marine Anwendungen). UL-listed, ABYC H-27 konform, ISO 9093-2 konform.

#### Marelon Through-Hull Fittings

| Modell | NW Zoll | Gewinde | Preis EUR |
|---|---|---|---|
| MF-500 | 1/2" | NPT | 12 |
| MF-750 | 3/4" | NPT | 16 |
| MF-1000 | 1" | NPT | 20 |
| MF-1250 | 1-1/4" | NPT | 26 |
| MF-1500 | 1-1/2" | NPT | 32 |
| MF-2000 | 2" | NPT | 45 |

(Confidence: documented)

#### Marelon Seacocks

| Modell | NW Zoll | Anschluss | Preis EUR |
|---|---|---|---|
| 905 | 3/4" | NPT + Hose | 48 |
| 906 | 1" | NPT + Hose | 62 |
| 907 | 1-1/4" | NPT + Hose | 78 |
| 908 | 1-1/2" | NPT + Hose | 98 |

(Confidence: documented)

### Guidi (Italien) — Europäische Bronze-Qualität

**Unternehmen**: Guidi Srl, Grignasco, Italien. Seit 1968 Hersteller von Bronze-Armaturen für den Marinemarkt. ISO 9093-1 zertifiziert. BSP-Gewinde Standard.

#### Guidi Borddurchlässe

| Modell | Typ | NW Zoll | Material | Gewinde | Preis EUR |
|---|---|---|---|---|---|
| 1210/13 | Mushroom | 1/2" | Bronze | BSP | 28 |
| 1210/19 | Mushroom | 3/4" | Bronze | BSP | 35 |
| 1210/25 | Mushroom | 1" | Bronze | BSP | 48 |
| 1210/32 | Mushroom | 1-1/4" | Bronze | BSP | 62 |
| 1210/38 | Mushroom | 1-1/2" | Bronze | BSP | 82 |
| 1210/50 | Mushroom | 2" | Bronze | BSP | 115 |
| 1244/19 | Flush | 3/4" | Bronze | BSP | 55 |
| 1244/25 | Flush | 1" | Bronze | BSP | 72 |
| 1244/38 | Flush | 1-1/2" | Bronze | BSP | 105 |

(Confidence: documented)

#### Guidi Seeventile

| Modell | Typ | NW Zoll | Material | Preis EUR |
|---|---|---|---|---|
| 1160/19 | Kugelhahn | 3/4" | Bronze | 75 |
| 1160/25 | Kugelhahn | 1" | Bronze | 95 |
| 1160/32 | Kugelhahn | 1-1/4" | Bronze | 125 |
| 1160/38 | Kugelhahn | 1-1/2" | Bronze | 165 |
| 1160/50 | Kugelhahn | 2" | Bronze | 225 |

(Confidence: documented)

### Buck Algonquin (USA)

**Unternehmen**: Buck Algonquin, The Atlas Companies, Elkhart, Indiana, USA. Hersteller von Bronze-Borddurchlässen und Seeventilen für den gewerblichen und Freizeitmarkt.

| Serie | Typ | Material | NW-Bereich | Gewinde | Preis EUR |
|---|---|---|---|---|---|
| Through-Hull | Mushroom | Bronze | 1/2"–3" | NPT | 28–185 |
| Scoop Strainer | Scoop | Bronze | 3/4"–2" | NPT | 62–175 |
| Ball Valve | Kugelhahn | Bronze | 1/2"–3" | NPT | 72–310 |
| Gate Valve | Schieber | Bronze | 1/2"–2" | NPT | 55–195 |

(Confidence: documented)

### Perko (USA)

**Unternehmen**: Perko Inc., Miami, Florida, USA. Breites Sortiment an marinen Beschlägen, einschließlich Borddurchlässe.

| Modell | Typ | NW Zoll | Material | Preis EUR |
|---|---|---|---|---|
| 0350 | Mushroom TH | 3/4"–2" | Bronze | 30–105 |
| 0358 | Flush TH | 3/4"–1-1/2" | Bronze | 45–95 |
| 0342 | Scoop Strainer | 3/4"–1-1/2" | Bronze | 58–135 |
| 0342DP | Scoop (deep) | 1"–2" | Bronze | 72–165 |

(Confidence: documented)

### Vetus (Niederlande)

**Unternehmen**: Vetus B.V., Schiedam, Niederlande. Spezialist für Antriebstechnik und marine Systeme.

#### TRC-Serie — Scoop Strainers

| Modell | NW Zoll | Anschluss | Material | Preis EUR |
|---|---|---|---|---|
| TRC3/4 | 3/4" | BSP | Bronze | 80 |
| TRC1 | 1" | BSP | Bronze | 105 |
| TRC11/4 | 1-1/4" | BSP | Bronze | 125 |
| TRC11/2 | 1-1/2" | BSP | Bronze | 140 |
| TRC2 | 2" | BSP | Bronze | 185 |

(Confidence: documented)

#### Vetus Seeventile

| Modell | Typ | NW Zoll | Material | Preis EUR |
|---|---|---|---|---|
| BV3/4 | Kugelhahn | 3/4" | Bronze | 75 |
| BV1 | Kugelhahn | 1" | Bronze | 95 |
| BV11/4 | Kugelhahn | 1-1/4" | Bronze | 125 |
| BV11/2 | Kugelhahn | 1-1/2" | Bronze | 165 |

(Confidence: documented)

### Plastimo (Frankreich)

**Unternehmen**: Plastimo S.A.S., Lorient, Frankreich. Breites Sortiment an Segelbeschlägen und Sicherheitsausrüstung.

| Serie | Typ | Material | NW-Bereich | Preis EUR |
|---|---|---|---|---|
| Skin Fitting | Mushroom | Bronze | 1/2"–1-1/2" | 22–75 |
| Seacock | Kugelhahn | Bronze | 3/4"–1-1/2" | 65–155 |
| Nylon TH | Mushroom | Nylon (PA6) | 3/4"–1-1/2" | 8–18 |

**Hinweis**: Nylon-Borddurchlässe von Plastimo sind **nur über der Wasserlinie** zugelassen (nicht ISO 9093-2 konform für unter WL).

(Confidence: documented)

### Osculati (Italien)

**Unternehmen**: Osculati S.p.A., Segrate (Milano), Italien. Großhändler und Hersteller mit über 30.000 Artikeln im Marineprogramm.

| Serie | Typ | Material | NW-Bereich | Preis EUR |
|---|---|---|---|---|
| 17.319 | Mushroom TH | Bronze | 1/2"–2" | 18–85 |
| 17.320 | Drain TH | Nylon | 3/4"–1-1/2" | 5–12 |
| 17.327 | Kugelhahn | Bronze | 3/4"–2" | 55–195 |
| 17.334 | Scoop Strainer | Bronze | 3/4"–1-1/2" | 48–125 |

(Confidence: documented)

---

## Anlagen-spezifische Zuordnung

### 9.1 Motorkühlwasser-Einlass (Raw Water Intake)

| Parameter | Spezifikation |
|---|---|
| Funktion | Seewasser für Motorkühlung (offener Kühlkreislauf) |
| Typ | Scoop-Strainer (bevorzugt) oder Mushroom + externem Seewasserfilter |
| Position | Mittschiffs, unter WL, möglichst tief (max. Druck) |
| NW | Motor-abhängig: 10–50 PS → 19 mm, 50–150 PS → 25 mm, >150 PS → 32–50 mm |
| Material | Bronze (Standard) oder Marelon (Aluminium-Rumpf) |
| Seeventil | **Pflicht** — Kugelhahn, direkt am Fitting |
| Sieb | Scoop-Strainer: integriert. Mushroom: externer Seewasserfilter (Groco ARG, Vetus FTR) |
| Schlauchschellen | Doppelt, 316L |
| Bonding | An Bonding-System anschließen (metallisch) |

**Dimensionierung Motorkühlwasser-Einlass:**

```
Durchfluss [l/min] = Motorleistung [kW] × 0,5 (Faustregel)

Beispiel: 75 kW Diesel → 37,5 l/min → 25 mm NW ausreichend (Kapazität: ~45 l/min bei 0,5 m Wassersäule)
```

(Confidence: calculated)

### 9.2 Abgas-Auslass (Exhaust Discharge)

| Parameter | Spezifikation |
|---|---|
| Funktion | Austritt des Abgas-Wasser-Gemisches (Nass-Auspuff) |
| Typ | Mushroom oder Flanged, am Spiegel über WL |
| Position | Spiegel (bevorzugt), seitlich über WL (min. 150 mm über WL) |
| NW | = Abgasschlauch-NW, typisch 38–76 mm |
| Material | **Bronze oder 316L** (kein Kunststoff! ABYC H-27) |
| Seeventil | Nein (über WL), aber Rückschlagklappe empfohlen |
| Gummiklappe | Außen montiert, verhindert Wasserrücklauf |
| Temperatur | 50–80 °C (normal), max. 120 °C |

(Confidence: documented)

### 9.3 Bilgenpumpe-Auslass (Bilge Discharge)

| Parameter | Spezifikation |
|---|---|
| Funktion | Ablauf der Bilgenpumpe |
| Typ | Mushroom, über WL |
| Position | Seitlich, min. 100 mm über WL |
| NW | 19–32 mm (abhängig von Pumpenleistung) |
| Material | Bronze, Marelon oder Kunststoff |
| Seeventil | Optional (über WL), Rückschlagventil in Leitung |
| Besonderheit | Anti-Siphon-Ventil erforderlich, wenn Auslass nahe WL |

(Confidence: documented)

### 9.4 Toiletten-Einlass (Toilet Raw Water Intake)

| Parameter | Spezifikation |
|---|---|
| Funktion | Seewasser für Toilettenspülung |
| Typ | Mushroom, unter WL |
| NW | 19 mm (3/4") Standard |
| Material | Bronze oder Marelon |
| Seeventil | **Pflicht** — immer geschlossen halten, wenn nicht in Gebrauch |
| Besonderheit | Schlauchschellen doppelt, Anti-Geruchs-Schlauch (Shields, Trident) verwenden |

(Confidence: documented)

### 9.5 Toiletten-Auslass (Toilet Discharge)

| Parameter | Spezifikation |
|---|---|
| Funktion | Abwasser-Austritt oder Verbindung zum Fäkalientank |
| Typ | Mushroom, unter oder über WL |
| NW | 25 mm (1") oder 38 mm (1-1/2") |
| Material | Bronze oder Marelon |
| Seeventil | **Pflicht** unter WL |
| Besonderheit | Bei Direkteinleitung: Abstand zur Küste beachten (MARPOL Annex IV) |
| Y-Ventil | Umschaltung Tank ↔ Seeauslass (wo Direkteinleitung erlaubt) |

(Confidence: documented)

### 9.6 Klimaanlage-Einlass (AC Raw Water Intake)

| Parameter | Spezifikation |
|---|---|
| Funktion | Seewasser für Klimaanlagen-Kühlung |
| Typ | Scoop-Strainer, unter WL |
| NW | 19–32 mm (abhängig von BTU-Leistung) |
| Material | Bronze oder Marelon |
| Seeventil | **Pflicht** |
| Sieb | Scoop-Strainer + zusätzlicher Seewasserfilter inline |
| Besonderheit | Durchfluss kritisch — verstopfter Strainer → AC-Ausfall → Pumpenüberhitzung |

**Dimensionierung:**

```
Durchfluss [l/min] = BTU/h × 0,00018 (Faustregel)

Beispiel: 48.000 BTU/h AC → 8,6 l/min → 19 mm NW ausreichend
```

(Confidence: calculated)

### 9.7 Generator-Kühlwasser (Generator Intake)

| Parameter | Spezifikation |
|---|---|
| Funktion | Seewasser für Generatorkühlung |
| Typ | Mushroom oder Scoop, unter WL |
| NW | 19–25 mm (typisch) |
| Material | Bronze oder Marelon |
| Seeventil | **Pflicht** |
| Besonderheit | Separater Durchlass vom Hauptmotor — kein T-Stück! |

(Confidence: documented)

### 9.8 Watermaker-Einlass (Watermaker Intake)

| Parameter | Spezifikation |
|---|---|
| Funktion | Seewasser für Osmose-Entsalzungsanlage |
| Typ | Scoop-Strainer, unter WL |
| NW | 19 mm (3/4") Standard |
| Material | Bronze oder Marelon |
| Seeventil | **Pflicht** |
| Besonderheit | Zusätzlicher 5-Mikron-Vorfilter inline, separate Leitung |
| Warnung | Kein gemeinsamer Einlass mit Toilette oder Motor — Kontaminations-Risiko |

(Confidence: documented)

### 9.9 Instrumente (Depth/Speed Transducer)

| Parameter | Spezifikation |
|---|---|
| Funktion | Echolot-, Geschwindigkeits-, Temperaturgeber |
| Typ | Transducer-Durchführung, unter WL |
| NW | 33–55 mm (Bohrung, nicht Gewinde) |
| Material | Kunststoff (Geber-Housing) mit GFK-Fairing-Block |
| Seeventil | Nein (aber Blindstopfen verfügbar) |
| Position | Mittschiffs, hinter Kiel, frei von Luftblasen und Turbulenzen |
| Ausrichtung | Parallel zur Wasserlinie (Fairing Block bei V-Rumpf) |

(Confidence: documented)

### 9.10 Cockpit-Drain

| Parameter | Spezifikation |
|---|---|
| Funktion | Entwässerung des Cockpits |
| Typ | Drain-Fitting, am Spiegel (bevorzugt) oder seitlich |
| NW | 25–38 mm (ISO 11812 abhängig) |
| Material | Kunststoff, Marelon, oder Bronze |
| Seeventil | Optional über WL, empfohlen bei Spiegeldrains nahe WL |
| Besonderheit | Zwei Drains Minimum (Backbord + Steuerbord) |
| ISO 11812 | Drainkapazität ≥ Cockpit-Volumen / 120 s |

(Confidence: documented)

---

## Verbindungstechnik

### 10.1 Gewindedichtung

#### BSP-Gewinde (zylindrisch)

BSP-Gewinde (G-Gewinde) ist zylindrisch und dichtet **nicht** über die Gewindeform. Abdichtung erfolgt durch:

1. **Flachdichtung** (Fiber, Gummi, PTFE) zwischen Flansch und Gegenstück
2. **PTFE-Band** (min. 6 Umwicklungen, im Uhrzeigersinn)
3. **Gewindedichtpaste** (Loctite 577, Permabond A131)

| Methode | Eignung unter WL | Eignung über WL | Demontierbar |
|---|---|---|---|
| PTFE-Band | Ja (mit Dichtstoff) | Ja | Ja |
| Flachdichtung | Ja | Ja | Ja |
| Loctite 577 | Ja | Ja | Ja (mit Wärme) |
| PTFE-Paste + Band | Ja (beste Kombination) | Ja | Ja |

(Confidence: documented)

#### NPT-Gewinde (konisch)

NPT-Gewinde dichtet über die Keilwirkung des konischen Gewindes. Zusätzlich:

1. **PTFE-Band** (min. 4 Umwicklungen)
2. **PTFE-Paste** (Rectorseal T Plus 2)
3. **Gewindedichtmasse** (Permatex #2)

**Warnung**: NPT-Gewinde **nicht** zu stark anziehen — konisches Gewinde kann den Gegenkörper (besonders Kunststoff) spalten.

(Confidence: documented)

### 10.2 Backing-Plates — Detaillierte Spezifikationen

#### GFK-Rumpf (Solid Laminate)

| Rumpfdicke | Backing-Plate Material | Backing-Plate Dicke | Backing-Plate Ø |
|---|---|---|---|
| 5–8 mm | GFK oder G10 | 8 mm | 3× NW |
| 8–12 mm | GFK oder G10 | 6 mm | 3× NW |
| 12–20 mm | GFK | 6 mm | 2,5× NW |
| >20 mm | Optional | — | — |

(Confidence: benchmark)

#### Sandwich-Rumpf

| Aufbau | Kern-Entfernung | Füllung | Backing-Plate |
|---|---|---|---|
| GFK/PVC/GFK | 2× NW radius | Epoxid + Glasfaser | 8 mm G10 |
| GFK/Balsa/GFK | 2,5× NW radius | Epoxid + Microfibers | 10 mm G10 |
| GFK/Nomex/GFK | 2× NW radius | Epoxid + Glasfaser | 8 mm G10 |

(Confidence: documented)

#### Aluminium-Rumpf

| Rumpfdicke | Backing-Plate | Isolation |
|---|---|---|
| 4–6 mm | Nicht nötig (direkte Verschraubung) | Kunststoff-Isolierbuchse zwischen Fitting und Rumpf |
| 6–10 mm | Nicht nötig | Kunststoff-Isolierbuchse |
| >10 mm | Nicht nötig | Kunststoff-Isolierbuchse |

**Kritisch**: Bei Aluminium-Rümpfen **niemals** metallische Fittings direkt auf Aluminium montieren. Immer Kunststoff-Isolierbuchse oder Kunststoff-Fitting verwenden.

(Confidence: documented)

### 10.3 Dichtstoff-Applikation unter WL

**Schritt-für-Schritt:**

1. Oberflächen reinigen: Aceton oder Isopropanol, alle Rückstände entfernen
2. Trocknen: Mindestens 30 Minuten bei 20 °C
3. Primer (bei PU-Dichtstoff): Sika Primer-209D auf GFK und Metall
4. Dichtstoff auftragen: Gleichmäßig auf Flansch UND Rumpf
5. Fitting einsetzen: Gleichmäßig andrücken, Dichtstoff muss ringförmig heraustreten
6. Gegenmutter handfest anziehen + 1/4 Umdrehung
7. Überschüssigen Dichtstoff entfernen (innerhalb der Verarbeitungszeit)
8. Aushärten lassen: Polysulfid 24–48 h, PU 48–72 h

| Dichtstoff | Verarbeitungszeit | Aushärtung | Endfestigkeit |
|---|---|---|---|
| 3M 101 (Polysulfid) | 60 min | 24 h (skinning), 7 Tage (voll) | 2,5 MPa Zugscherfestigkeit |
| Sikaflex 291i (PU) | 40 min | 24 h (skinning), 5 Tage (voll) | 3,0 MPa Zugscherfestigkeit |
| 3M 5200 (PU) | 60 min | 48 h (skinning), 7 Tage (voll) | 3,5 MPa Zugscherfestigkeit |

(Confidence: documented)

### 10.4 Schlauchverbindungen

| Schlauchtyp | Einsatz | Schlauchschellen | Norm |
|---|---|---|---|
| Gummi-/EPDM-Schlauch | Kühlwasser, Bilge | Doppelt unter WL, 316L | ABYC H-27 |
| Silikon-Schlauch | Abgas (nass) | Doppelt, T-Bolt | — |
| PVC-Spiralschlauch | Toilette | Doppelt unter WL | — |
| Trident Sani-Shield | Toilette (geruchsfrei) | Doppelt unter WL | — |

#### Schlauchschellen-Spezifikation

| Typ | Material | Einsatz | Drehmoment |
|---|---|---|---|
| Wormgear (Schneckengewinde) | 316L | Standard | 2–3 Nm |
| T-Bolt (T-Schraube) | 316L | Abgas, große NW | 5–8 Nm |
| Constant-Torque | 316L + Federstahl | Vibrierende Systeme | Selbstnachstellend |

**Warnung**: Schlauchschellen mit perforiertem Band können den Schlauch beschädigen. Nicht-perforierte Bänder (Solid Band) bevorzugen.

(Confidence: documented)

---

## Technische Referenz & Berechnungen

### 11.1 Durchflussberechnung

#### Formel: Volumenstrom durch Borddurchlass

```
Q = A × v × 60.000

Q = Volumenstrom [l/min]
A = Querschnittsfläche [m²] = π × (d/2)² wobei d in Metern
v = Strömungsgeschwindigkeit [m/s]
60.000 = Umrechnungsfaktor m³/s → l/min
```

#### Empfohlene Strömungsgeschwindigkeiten

| Anwendung | v max [m/s] | Begründung |
|---|---|---|
| Saugseite (Motor, AC) | 1,5 | Kavitationsgefahr |
| Druckseite (Abgas, Bilge) | 3,0 | Erosion |
| Schwerkraft-Ablauf (Drain) | 0,5–1,0 | Selbstgefälle |

#### Durchfluss-Tabelle nach Nennweite

| NW mm | NW Zoll | Fläche mm² | Q bei 1,0 m/s [l/min] | Q bei 1,5 m/s [l/min] |
|---|---|---|---|---|
| 13 | 1/2" | 133 | 7,9 | 11,9 |
| 19 | 3/4" | 284 | 17,0 | 25,5 |
| 25 | 1" | 491 | 29,4 | 44,2 |
| 32 | 1-1/4" | 804 | 48,2 | 72,3 |
| 38 | 1-1/2" | 1.134 | 68,1 | 102,1 |
| 50 | 2" | 1.963 | 117,8 | 176,7 |

(Confidence: calculated)

### 11.2 Druckberechnung

#### Hydrostatischer Druck auf Borddurchlass

```
p = ρ × g × h

p = Druck [Pa]
ρ = Dichte Seewasser = 1.025 kg/m³
g = 9,81 m/s²
h = Tiefe unter Wasserlinie [m]
```

| Tiefe unter WL [mm] | Druck [kPa] | Druck [bar] | Kraft auf 25mm-Durchlass [N] |
|---|---|---|---|
| 200 | 2,01 | 0,020 | 0,99 |
| 500 | 5,03 | 0,050 | 2,47 |
| 1.000 | 10,06 | 0,101 | 4,94 |
| 1.500 | 15,09 | 0,151 | 7,41 |
| 2.000 | 20,12 | 0,201 | 9,88 |

(Confidence: calculated)

### 11.3 Wassereintritt bei Leckage — Zeitkritisch

#### Wasserfluss bei offenem Borddurchlass (Toricelli)

```
Q = Cd × A × √(2 × g × h)

Cd = Durchflussbeiwert ≈ 0,6 (scharfkantige Öffnung)
A = Öffnungsfläche [m²]
g = 9,81 m/s²
h = Tiefe unter WL [m]
```

| NW mm | Fläche mm² | h=0,5m [l/min] | h=1,0m [l/min] | h=1,5m [l/min] |
|---|---|---|---|---|
| 13 | 133 | 14,9 | 21,1 | 25,8 |
| 19 | 284 | 31,8 | 44,9 | 55,0 |
| 25 | 491 | 54,9 | 77,7 | 95,1 |
| 32 | 804 | 89,9 | 127,1 | 155,7 |
| 38 | 1.134 | 126,8 | 179,4 | 219,7 |
| 50 | 1.963 | 219,5 | 310,4 | 380,2 |

**Bedeutung**: Ein offener 1"-Borddurchlass in 1 m Tiefe lässt **~78 Liter pro Minute** einströmen. Ein typisches 10-m-Segelboot mit ~2.000 l Rumpfvolumen unter WL wäre in **~25 Minuten** gesunken.

(Confidence: calculated)

### 11.4 Cockpit-Drain-Dimensionierung nach ISO 11812

```
Erforderliche Drain-Kapazität:

V_cockpit = L × B × H_sill [m³]
t_drain = 120 s (CE Kat. A), 300 s (Kat. B/C/D)
Q_min = V_cockpit / t_drain × 1000 [l/s → l/min × 60]
```

| Cockpit L×B×H [m] | Volumen [l] | Q_min Kat.A [l/min] | Empf. NW je Drain | Anzahl Drains |
|---|---|---|---|---|
| 2,0 × 1,5 × 0,15 | 450 | 225 | 38 mm | 2 |
| 2,5 × 2,0 × 0,20 | 1.000 | 500 | 50 mm | 2 |
| 3,0 × 2,5 × 0,25 | 1.875 | 938 | 50 mm | 4 |

(Confidence: calculated)

### 11.5 Galvanische Kompatibilitäts-Matrix

```
Potentialdifferenz-Bewertung:

<50 mV:   Unbedenklich (Score 100)
50-100 mV:  Akzeptabel (Score 80)
100-200 mV: Bedenklich (Score 50)
200-300 mV: Problematisch (Score 25)
>300 mV:  Kritisch (Score 0)
```

| Material A | Material B | ΔV [mV] | Bewertung | Score |
|---|---|---|---|---|
| Bronze C83600 | Bronze C83600 | 0 | Unbedenklich | 100 |
| Bronze C83600 | 316L | ~200 | Bedenklich | 50 |
| Bronze C83600 | Aluminium | ~500 | **Kritisch** | 0 |
| 316L | Aluminium | ~700 | **Kritisch** | 0 |
| Marelon | Aluminium | 0 | Unbedenklich | 100 |
| Marelon | Bronze | 0 | Unbedenklich | 100 |
| Titan | Aluminium | ~700 | Niedrig (Titan bildet keine große Kathode) | 75 |

(Confidence: calculated)

---

## Einbau-/Austausch-Anleitung

### 12.1 Neuen Borddurchlass einbauen (GFK-Rumpf)

#### Werkzeug und Material

| Werkzeug | Spezifikation |
|---|---|
| Lochsäge | Bi-Metall, Ø = Außengewinde + 2 mm |
| Bohrmaschine | Min. 600 W, langsamer Vorschub |
| Schleifpapier | K80 (Oberfläche anrauen) |
| Entfetter | Aceton oder Isopropanol |
| Dichtstoff | Polysulfid (3M 101) oder PU (Sikaflex 291i) |
| Primer | Sika Primer-209D (bei PU) |
| Backing-Plate | G10, Ø = 3× NW, Dicke 8 mm |
| Drehmomentschlüssel | 5–25 Nm |
| Notholzstopfen | Passend zur NW, konisch |

#### Schritt-für-Schritt

1. **Position markieren**: Von innen und außen, Kern ggf. vorher entfernen
2. **Pilotbohrung**: 6 mm durch Rumpf
3. **Lochsäge ansetzen**: Von außen bohren, Ø = Außengewinde + 2 mm
4. **Kanten entgraten**: Innen und außen, K80 Schleifpapier
5. **Sandwich-Kern entfernen** (falls Sandwich): Radius = 2× NW, mit Epoxid füllen, 24 h aushärten
6. **Probepassung**: Fitting einsetzen, Backing-Plate von innen, prüfen
7. **Oberflächen reinigen**: Aceton, trocknen
8. **Primer auftragen** (bei PU): Sika Primer-209D, 30 min ablüften
9. **Dichtstoff auftragen**: Auf Flansch und Rumpf-Außenseite
10. **Fitting einsetzen**: Von außen, gleichmäßig andrücken
11. **Backing-Plate** von innen aufsetzen (mit Dichtstoff)
12. **Gegenmutter** aufschrauben: Handfest + 1/4 Umdrehung
13. **Überschüssigen Dichtstoff entfernen**
14. **Aushärten lassen**: Min. 48 h vor Wasserkontakt
15. **Seeventil montieren**: Auf Gewinde schrauben, PTFE-Band
16. **Schlauch anschließen**: Doppelte Schlauchschellen (unter WL)
17. **Notholzstopfen** an Schnur neben Durchlass befestigen
18. **Dichtigkeitsprüfung**: Boot zu Wasser lassen, alle Durchlässe kontrollieren

(Confidence: documented)

### 12.2 Borddurchlass austauschen

#### Zusätzliche Schritte bei Austausch

1. **Alten Durchlass entfernen**: Schlauch lösen, Seeventil abschrauben, Gegenmutter lösen
2. **Alten Dichtstoff entfernen**: Mechanisch (Kunststoff-Spachtel) + chemisch (DeBond, 3M Adhesive Remover)
3. **Bohrung prüfen**: Aufweitung? Delamination? Wassereinbruch in Kern?
4. **Bohrung ggf. aufbohren**: Auf nächste Größe, wenn beschädigt
5. **Laminat reparieren** (wenn nötig): Epoxid + Glasfaser, 24 h aushärten
6. **Neuen Durchlass einbauen**: Wie Neueinbau ab Schritt 6

**Zeitaufwand:**

| Aufgabe | DIY (erfahren) | Werft |
|---|---|---|
| Neuer Durchlass (GFK solid) | 2–3 h | 1–2 h |
| Neuer Durchlass (Sandwich) | 4–6 h (inkl. Kernverstärkung) | 2–4 h |
| Austausch (ohne Reparatur) | 1–2 h | 1 h |
| Austausch (mit Reparatur) | 3–5 h | 2–3 h |

**Kosten:**

| Position | Material EUR | Arbeit Werft EUR/h |
|---|---|---|
| Borddurchlass (Bronze, 3/4") | 35–55 | — |
| Seeventil (Bronze, 3/4") | 75–125 | — |
| Backing-Plate (G10, 60mm) | 8–15 | — |
| Dichtstoff (Kartusche) | 12–25 | — |
| Schlauchschellen (2×) | 5–10 | — |
| Notholzstopfen | 3–8 | — |
| Werft-Arbeitsstunde | — | 75–120 |
| **Gesamt (Austausch, Werft)** | **~150–250** | **~150–350** |

(Confidence: benchmark)

### 12.3 Seeventil-Wartung

#### Jährliche Inspektion (beim Haulout)

1. Seeventil mehrfach öffnen/schließen — muss leichtgängig sein
2. Hebel auf festen Sitz prüfen
3. Visuell auf Korrosion, Entzinkung, Risse prüfen
4. Dichtstoff-Ring auf Risse und Ablösung prüfen
5. Schlauchschellen nachziehen (2 Nm)
6. Bonding-Kabel auf festen Sitz prüfen
7. Notholzstopfen auf Anwesenheit und Passform prüfen

#### Wartung bei Schwergängigkeit

1. Seeventil demontieren (Boot an Land!)
2. Kugel/Küken reinigen mit feinem Scotch-Brite
3. Marine-Armaturenfett auftragen (Superlube, Lanocote)
4. Zusammenbauen, Funktion prüfen

(Confidence: documented)

---

## Lebensdauer und Alterungsmechanismen

### 13.1 Lebensdauer nach Material und Einsatzbedingung

| Material | Süßwasser | Gemäßigt (Ostsee/Nordsee) | Mittelmeer | Tropen |
|---|---|---|---|---|
| Bronze C83600 | 40–60 Jahre | 30–50 Jahre | 25–40 Jahre | 20–30 Jahre |
| Bronze C92200 | 50–70 Jahre | 40–60 Jahre | 30–50 Jahre | 25–40 Jahre |
| 316L | 30–50 Jahre | 20–35 Jahre | 15–25 Jahre | 10–20 Jahre |
| Marelon | 20–30 Jahre | 15–25 Jahre | 15–20 Jahre | 10–15 Jahre |
| TruDesign | 20–30 Jahre | 15–25 Jahre | 15–20 Jahre | 10–15 Jahre |
| Messing | 10–20 Jahre | 5–15 Jahre | 3–10 Jahre | **2–5 Jahre** |
| Nylon | 5–10 Jahre | 5–8 Jahre | 3–5 Jahre | 2–4 Jahre |

(Confidence: benchmark)

### 13.2 Alterungsmechanismen

#### 13.2.1 Entzinkung (Dezincification)

| Aspekt | Beschreibung |
|---|---|
| Betrifft | Messing (>15 % Zn), minderwertiges Bronze |
| Mechanismus | Selektive Auflösung des Zinks, poröse Kupferstruktur bleibt |
| Visuelles Merkmal | Rosa-kupferfarbene, poröse Oberfläche statt goldgelb |
| Festigkeitsverlust | Bis 90 % |
| Zeitrahmen | 2–10 Jahre (abhängig von Salinität und Temperatur) |
| Prüfung | Kratzen mit Messer — entzinktes Material ist weich wie Butter |
| AYDI-Score | Entzinkung erkannt → Score 0, sofortiger Austausch |

(Confidence: documented)

#### 13.2.2 Spaltkorrosion (Crevice Corrosion)

| Aspekt | Beschreibung |
|---|---|
| Betrifft | 316L, weniger Bronze |
| Mechanismus | Sauerstoffverarmung im Spalt (Gewinde, Flansch) → lokale Säurebildung |
| Visuelles Merkmal | Braune Ablagerungen in Spalten, Lochfraß |
| Zeitrahmen | 5–15 Jahre (schneller in warmen Gewässern) |
| Prüfung | Gewinde demontieren, visuell prüfen |
| AYDI-Score | Spaltkorrosion erkannt → Score 20, Austausch bei nächstem Haulout |

(Confidence: documented)

#### 13.2.3 Lochfraß (Pitting Corrosion)

| Aspekt | Beschreibung |
|---|---|
| Betrifft | 316L (besonders in warmen Gewässern >25 °C) |
| Mechanismus | Lokaler Durchbruch der Passivschicht → Lochbildung |
| Visuelles Merkmal | Kleine, tiefe Löcher in der Oberfläche |
| Gefahr | Kann Rumpf durchdringen! |
| Zeitrahmen | 3–10 Jahre in tropischen Gewässern |
| AYDI-Score | Lochfraß erkannt → Score 10, sofortiger Austausch empfohlen |

(Confidence: documented)

#### 13.2.4 Dichtstoff-Alterung

| Aspekt | Beschreibung |
|---|---|
| Betrifft | Alle Dichtstoffe |
| Mechanismus | UV-Abbau, Weichmacher-Wanderung, Ermüdung durch Vibration |
| Visuelles Merkmal | Risse, Ablösung, Verhärtung, Verfärbung |
| Zeitrahmen | Polysulfid: 10–15 Jahre, PU: 8–12 Jahre, Silikon: 3–5 Jahre (unter WL!) |
| AYDI-Score | Dichtstoff gerissen → Score 30, Erneuerung empfohlen |

(Confidence: documented)

#### 13.2.5 UV-Degradation (Kunststoff)

| Aspekt | Beschreibung |
|---|---|
| Betrifft | Marelon, TruDesign (über WL, UV-exponiert) |
| Mechanismus | UV-Strahlung bricht Polymerketten → Versprödung |
| Visuelles Merkmal | Verfärbung (Gelblich bei Weiß), Haarrisse, Sprödigkeit |
| Zeitrahmen | 10–20 Jahre (mit UV-Stabilisator), 5–10 Jahre (ohne) |
| AYDI-Score | UV-Schaden sichtbar → Score 40, Überwachung oder Austausch |

(Confidence: documented)

#### 13.2.6 Bewuchs-Verblockung

| Aspekt | Beschreibung |
|---|---|
| Betrifft | Scoop-Strainer, Mushroom-Fittings |
| Mechanismus | Seepocken, Muscheln, Algen blockieren Durchfluss |
| Visuelles Merkmal | Sichtbarer Bewuchs, reduzierter Kühlwasserfluss |
| Zeitrahmen | Wochen (Tropen) bis Monate (gemäßigt) |
| AYDI-Score | Verblockung → Score 60 (reversibel durch Reinigung) |

(Confidence: documented)

### 13.3 Wartungsintervalle

| Komponente | Intervall | Maßnahme |
|---|---|---|
| Seeventil | Jährlich (Haulout) | Öffnen/Schließen, Fett, visuell prüfen |
| Scoop-Strainer | Monatlich (Tropen), vierteljährlich (gemäßigt) | Sieb reinigen, Bewuchs entfernen |
| Dichtstoff | Alle 5 Jahre | Visuell prüfen, bei Rissen erneuern |
| Schlauchschellen | Jährlich | Nachziehen (2 Nm), auf Korrosion prüfen |
| Bonding-Kabel | Jährlich | Verbindung prüfen, Widerstand messen |
| Opferanoden | 6–24 Monate | Ersetzen bei >50 % Abtrag |
| Notholzstopfen | Jährlich | Anwesenheit, Passform, Zugänglichkeit prüfen |

(Confidence: benchmark)

---

## Fehlerbild-Atlas

### FB-01: Entzinkung an Messing-Borddurchlass

**Beschreibung**: Ein 3/4"-Borddurchlass unter der Wasserlinie zeigt die typischen rosa-kupferfarbenen Verfärbungen der Entzinkung. Das Fitting wurde als "Bronze" verkauft, ist aber tatsächlich Messing (CW617N, 37 % Zink). Nach 6 Jahren im Mittelmeer hat die selektive Auflösung des Zinks die mechanische Festigkeit auf unter 10 % reduziert. Das Material lässt sich mit einem Fingernagel eindrücken.
**Visuell**: Rosa-kupferfarbene, poröse Oberfläche, kein metallischer Glanz. Kratzer mit Messer zeigt weiches, schwammiges Material.
**Score**: 0/100 — Sofortiger Austausch, Boot nicht zu Wasser lassen.
**Maßnahme**: Fitting und Seeventil komplett erneuern, durch zertifiziertes Bronze C83600 oder Marelon ersetzen.
**Kosten**: Material ~180 EUR + Werftarbeit ~200 EUR = ~380 EUR.
**Confidence**: visual_high (eindeutiges Schadensbild)
**Norm-Referenz**: ISO 9093-1 — Werkstoff muss entzinkungsbeständig sein.
**Häufigkeit**: 8 % aller Borddurchlass-Befunde bei Surveys (Pantaenius 2022).

(Confidence: documented)

### FB-02: Spaltkorrosion an 316L-Seeventil

**Beschreibung**: Ein 1"-Seeventil aus 316L zeigt braune Ablagerungen und Lochfraß am Gewindeübergang zum Borddurchlass. Das Boot lag 4 Jahre im Mittelmeer (Wassertemperatur bis 28 °C). Im Spalt zwischen Gewinde und Durchlass kam es zur Sauerstoffverarmung und lokaler Säurebildung. Die Gewindeflanke ist an mehreren Stellen durchkorrodiert.
**Visuell**: Braune Verfärbungen und Lochfraß am Gewindeansatz, Rost-ähnliche Ablagerungen.
**Score**: 15/100 — Austausch bei nächstem Haulout, Boot noch fahrtüchtig.
**Maßnahme**: Seeventil durch Bronze C83600 ersetzen. Borddurchlass prüfen, ggf. auch ersetzen.
**Kosten**: Material ~150 EUR + Werftarbeit ~150 EUR = ~300 EUR.
**Confidence**: visual_high
**Norm-Referenz**: ABYC H-27 — Seeventil muss korrosionsbeständig sein.
**Häufigkeit**: 12 % aller 316L-Seeventile in mediterranen Gewässern.

(Confidence: documented)

### FB-03: Gerissener Dichtstoff am Borddurchlass

**Beschreibung**: Der Polysulfid-Dichtstoff zwischen einem 3/4"-Bronze-Borddurchlass und dem GFK-Rumpf zeigt Rissbildung über ~60 % des Umfangs. Der Dichtstoff ist nach 12 Jahren verhärtet und hat sich teilweise vom GFK gelöst. Es tritt langsam Wasser ein (Tropfrate ~5 ml/h bei Still-Liegen, deutlich mehr bei Fahrt und Vibration).
**Visuell**: Sichtbare Risse im schwarzen Polysulfid-Ring, Kalkablagerungen am Rissrand, feuchte Stelle am Rumpf innen.
**Score**: 35/100 — Austausch des Dichtstoffs empfohlen, alternativ Nachdichten von innen (Übergangslösung).
**Maßnahme**: Borddurchlass ausbauen, alten Dichtstoff entfernen, neu eindichten mit 3M 101 oder Sikaflex 291i.
**Kosten**: Material ~25 EUR + Werftarbeit ~150 EUR = ~175 EUR (DIY: ~25 EUR + 2h Arbeit).
**Confidence**: visual_medium (Risse nicht immer sichtbar, Leckage-Spur ist Indikator)
**Häufigkeit**: 22 % aller Borddurchlässe >10 Jahre.

(Confidence: documented)

### FB-04: Fehlende Backing-Plate bei Sandwich-Rumpf

**Beschreibung**: Ein 1"-Borddurchlass wurde in einen Sandwich-Rumpf (GFK/PVC-Schaum/GFK, Gesamtdicke 28 mm) ohne Backing-Plate und ohne Kern-Entfernung eingebaut. Die Gegenmutter hat den PVC-Kern komprimiert, der Durchlass sitzt lose im Rumpf. Beim Betätigen des Seeventils bewegt sich der gesamte Durchlass sichtbar.
**Visuell**: Durchlass lässt sich mit Hand bewegen, Riss im Gelcoat um die Bohrung, Dichtstoff-Ring unterbrochen.
**Score**: 10/100 — Sofortige Reparatur erforderlich, Boot nicht zu Wasser lassen.
**Maßnahme**: Durchlass ausbauen, Kern im Radius 2× NW entfernen, mit Epoxid füllen, 24h aushärten, G10-Backing-Plate einbauen, neu eindichten.
**Kosten**: Material ~60 EUR + Werftarbeit ~400 EUR = ~460 EUR.
**Confidence**: visual_high (Bewegung des Durchlasses ist eindeutig)
**Norm-Referenz**: ISO 12215 — Kernverstärkung bei lokaler Lasteinleitung in Sandwich-Laminat.
**Häufigkeit**: 5 % aller Sandwich-Rümpfe (besonders ältere Baureihen <2005).

(Confidence: documented)

### FB-05: Elektrolyse-Schaden an Bronze-Borddurchlass neben Aluminium-Bauteil

**Beschreibung**: Ein Bronze-Borddurchlass (C83600) wurde 350 mm entfernt von einem Aluminium-Saildrive-Gehäuse installiert. Obwohl ein Bonding-System vorhanden ist, hat eine defekte Galvanic-Isolator-Diode am Landstrom zu erheblichem Fremdstrom geführt. Das Aluminium-Gehäuse zeigt massive Korrosion (bis 3 mm Materialabtrag), der Bronze-Durchlass selbst ist unbeschädigt (er ist die Kathode).
**Visuell**: Weißes Aluminiumoxid-Pulver am Saildrive, Lochfraß am Aluminium, Bronze glänzend und unbeschädigt.
**Score**: 25/100 (Systemscore) — Bronze ok, aber Aluminium kritisch beschädigt.
**Maßnahme**: Galvanic Isolator ersetzen, Zinkanoden erneuern, Aluminium-Schaden bewerten lassen. Langfristig: Bronze durch Marelon ersetzen.
**Kosten**: Galvanic Isolator ~180 EUR + Saildrive-Reparatur ~2.000–5.000 EUR.
**Confidence**: visual_high (Korrosionsmuster eindeutig)
**Häufigkeit**: 3 % aller Boote mit Aluminium-Komponenten in Marinas mit schlechter Erdung.

(Confidence: documented)

### FB-06: Gate-Valve (Schieber) statt Kugelhahn unter WL

**Beschreibung**: Ein Schieber-Ventil (Gate Valve) wurde als Seeventil unter der Wasserlinie installiert. Gate Valves sind für marine Anwendungen nicht geeignet: Sie korrodieren intern, die Spindel kann festsetzen, und im Notfall ist nicht erkennbar, ob das Ventil offen oder geschlossen ist. Dieses Exemplar (10 Jahre alt) ist festgesetzt und lässt sich weder öffnen noch schließen.
**Visuell**: Veraltetes Schieber-Ventil mit Handrad statt Hebel, Spindel festkorrodiert, kein Offen/Zu-Indikator.
**Score**: 20/100 — Austausch gegen Kugelhahn beim nächsten Haulout.
**Maßnahme**: Schieber-Ventil durch Kugelhahn (Bronze oder Marelon) ersetzen.
**Kosten**: Material ~120 EUR + Werftarbeit ~200 EUR = ~320 EUR.
**Confidence**: visual_high (Gate Valve visuell eindeutig erkennbar)
**Norm-Referenz**: ABYC H-27 — Seeventile müssen als Kugelhahn oder Kükenventil ausgeführt sein, Gate Valves sind nicht zulässig.
**Häufigkeit**: 15 % bei Booten Baujahr <2000.

(Confidence: documented)

### FB-07: Falsche Gewindekombination BSP/NPT

**Beschreibung**: Ein Groco-Borddurchlass (NPT-Gewinde) wurde auf ein Guidi-Seeventil (BSP-Gewinde) geschraubt. Die Gewinde greifen initial, da die Nennmaße ähnlich sind (3/4" NPT: 26,57mm vs. 3/4" BSP: 26,44mm). Allerdings unterscheiden sich Konizität und Steigung. Nach 2 Jahren Vibration hat sich die Verbindung gelockert, es tritt Wasser zwischen den Gewindegängen ein.
**Visuell**: Leichte Tropfbildung am Gewindeübergang Fitting↔Seeventil, PTFE-Band sichtbar herausgedrückt.
**Score**: 30/100 — Austausch des nicht passenden Teils bei nächstem Haulout.
**Maßnahme**: Einheitliches Gewindesystem verwenden (nur BSP oder nur NPT). Niemals mischen.
**Kosten**: Material ~45 EUR (passendes Fitting) + Werftarbeit ~100 EUR = ~145 EUR.
**Confidence**: visual_medium (Tropfbildung sichtbar, aber Gewindeinkompatibilität nur durch Messung feststellbar)
**Häufigkeit**: 6 % bei Booten mit gemischten US/EU-Komponenten.

(Confidence: documented)

### FB-08: Wassereinbruch durch gebrochenen Kunststoff-Borddurchlass

**Beschreibung**: Ein Nylon-Borddurchlass (PA6, nicht glasfaserverstärkt) unter der Wasserlinie ist nach 7 Jahren gebrochen. Das Material war nicht UV-stabilisiert und nicht ISO 9093-2 konform. Der Bruch erfolgte am Gewindeansatz, wo die Wandstärke am geringsten ist. Wassereinbruch: ca. 30 l/min (Notholzstopfen eingesetzt).
**Visuell**: Glatter Bruch am Gewindeansatz, Material gelblich verfärbt und spröde, typische Versprödung.
**Score**: 0/100 — Sofortige Reparatur, Boot nicht zu Wasser lassen ohne Reparatur.
**Maßnahme**: Durch ISO 9093-2 konformes Marelon oder TruDesign ersetzen, alternativ Bronze.
**Kosten**: Material ~60 EUR + Notfall-Werftarbeit ~300 EUR = ~360 EUR.
**Confidence**: visual_high (Bruch eindeutig)
**Norm-Referenz**: ISO 9093-2 — Nur glasfaserverstärktes Polyamid (PA66-GF30) unter WL zulässig.
**Häufigkeit**: 4 % bei Booten mit nicht-zertifizierten Kunststoff-Fittings.

(Confidence: documented)

### FB-09: Bewuchsverblockung Scoop-Strainer

**Beschreibung**: Ein Groco SC-750 Scoop-Strainer für den Motorkühlwasser-Einlass ist vollständig mit Seepocken (Balanus) zugewachsen. Der Motor überhitzt bei Volllast (Alarm bei 95 °C statt normal 82 °C). Bei Teillast reicht der reduzierte Durchfluss noch knapp aus. Das Boot liegt seit 8 Monaten im Mittelmeer ohne Antifouling am Scoop.
**Visuell**: Scoop-Strainer von außen: dicke Schicht Seepocken, Maschenweite vollständig blockiert.
**Score**: 55/100 — Reinigung bei nächster Gelegenheit, Motor nicht auf Volllast betreiben.
**Maßnahme**: Scoop-Strainer von Taucher reinigen lassen oder Boot slippen. Antifouling auf Scoop auftragen.
**Kosten**: Tauchservice ~80–150 EUR, oder DIY beim Haulout.
**Confidence**: visual_high (Überhitzung + visueller Bewuchs)
**Häufigkeit**: 25 % aller Boote nach >6 Monaten im Mittelmeer ohne Wartung.

(Confidence: documented)

### FB-10: Fehlender Notholzstopfen

**Beschreibung**: Bei einem Survey wird festgestellt, dass keiner der 6 Borddurchlässe unter der Wasserlinie einen zugeordneten Notholzstopfen hat. Das Boot ist CE-Kategorie A (Ozean) klassifiziert — Notholzstopfen sind Pflicht. Im Notfall (Bruch eines Borddurchlasses) gibt es keine Möglichkeit, den Wassereinbruch zu stoppen.
**Visuell**: Keine Holzstopfen sichtbar, keine Halterungen oder Schnüre an Borddurchlässen.
**Score**: 40/100 (Compliance-Score) — Anschaffung und Installation sofort.
**Maßnahme**: Für jeden Borddurchlass unter WL einen konischen Holzstopfen (Weichholz, z.B. Kiefer) bereitstellen, an Schnur befestigen, neben dem zugehörigen Seeventil lagern.
**Kosten**: Material ~20–40 EUR für 6 Stopfen.
**Confidence**: visual_high (Anwesenheit/Abwesenheit eindeutig prüfbar)
**Norm-Referenz**: CE/RCD 2013/53/EU — Notholzstopfen Pflicht bei Kategorie A und B.
**Häufigkeit**: 35 % aller Boote bei Surveys (erschreckend hoch).

(Confidence: documented)

### FB-11: Silikon als Dichtstoff unter WL

**Beschreibung**: Ein Borddurchlass unter der Wasserlinie wurde mit Silikon-Dichtstoff (anstelle von Polysulfid oder PU) eingedichtet. Silikon haftet schlecht auf GFK und Bronze, kriecht unter Last und wird in Seewasser weich. Nach 3 Jahren hat sich der Silikon-Ring vollständig vom GFK gelöst, Wasser tritt ein.
**Visuell**: Transparenter oder weißer Silikon-Ring um Durchlass, vollständig vom GFK abgelöst, lässt sich mit Finger abziehen.
**Score**: 25/100 — Durchlass ausbauen, Silikon entfernen, mit Polysulfid oder PU neu eindichten.
**Maßnahme**: Komplette Neuabdichtung mit 3M 101 (Polysulfid) oder Sikaflex 291i (PU).
**Kosten**: Material ~25 EUR + Werftarbeit ~200 EUR = ~225 EUR.
**Confidence**: visual_high (Silikon visuell erkennbar, Ablösung offensichtlich)
**Häufigkeit**: 10 % bei DIY-Einbauten.

(Confidence: documented)

### FB-12: Nicht zugängliches Seeventil

**Beschreibung**: Ein Seeventil unter der Wasserlinie ist durch nachträglich eingebaute Einrichtung (Schrankrückwand, Motorbett) so verbaut, dass es nicht bedient werden kann. Der Hebel kann nicht bewegt werden, eine Inspektion ist unmöglich. Im Notfall wäre das Ventil nicht schließbar.
**Visuell**: Seeventil-Hebel blockiert durch Holzstruktur, kein Zugang möglich ohne Demontage.
**Score**: 20/100 — Zugang herstellen, Inspektionsluke einbauen.
**Maßnahme**: Inspektionsluke in Schrankrückwand einbauen (min. 200 × 200 mm) oder Obstruktion entfernen. Seeventil muss jederzeit ohne Werkzeug bedienbar sein.
**Kosten**: Material ~30–80 EUR (Inspektionsluke) + Werftarbeit ~150 EUR = ~180–230 EUR.
**Confidence**: visual_high (Blockierung sichtbar)
**Norm-Referenz**: ABYC H-27 — Seeventile müssen ohne Werkzeug bedienbar sein.
**Häufigkeit**: 18 % bei Booten mit nachträglichen Umbauten.

(Confidence: documented)

---

## Fehlerbehebungs-Leitfaden

### Problem 1: Seeventil lässt sich nicht bewegen (festgesetzt)

**Symptom**: Der Hebel des Seeventils lässt sich weder in Offen- noch in Geschlossen-Position bewegen, auch mit erhöhter Kraft nicht.

**Ursachen (nach Wahrscheinlichkeit):**
1. Kalkablagerungen / Korrosionsprodukte im Ventilkörper (60 %)
2. Quellung/Korrosion der Ventilkugel oder des Kükens (25 %)
3. Verbogene oder korrodierte Hebel-Achse (10 %)
4. Falsche Montage (zu stark angezogen) (5 %)

**Diagnose:**
- Visuell: Kalkablagerungen sichtbar? Korrosion?
- Klopftest: Leicht auf Ventilkörper klopfen (Holzhammer) — löst manchmal Kalkverkrustungen
- Alter: >15 Jahre → wahrscheinlich interne Korrosion

**Behebung:**
1. **Kalkablagerung**: WD-40 oder Kriechöl an Achse, 24 h einwirken lassen, vorsichtig versuchen zu bewegen. Alternativ: Entkalker (Essigessenz) einsprühen.
2. **Korrosion**: Ventil muss ausgebaut und überholt oder ersetzt werden (Boot an Land!).
3. **Verbogene Achse**: Ventil ersetzen.
4. **Zu stark angezogen**: Kontermutter lösen, Ventil neu einstellen.

**Warnung**: Niemals mit Rohrzange oder verlängertem Hebel Gewalt anwenden — Bruchgefahr des Ventilkörpers unter WL!

(Confidence: documented)

### Problem 2: Tropfende/Leckende Borddurchlass-Verbindung

**Symptom**: Wasser tropft an der Innenseite des Borddurchlasses, am Gewindeübergang oder am Dichtstoff-Ring.

**Ursachen:**
1. Gealterter/gerissener Dichtstoff (45 %)
2. Lockere Gegenmutter durch Vibration (25 %)
3. Inkompatible Gewinde BSP/NPT (10 %)
4. Korrosion am Fitting (10 %)
5. Beschädigter Rumpf um Bohrung (10 %)

**Diagnose:**
- Tropfrate messen (ml/h)
- Tropfstelle lokalisieren: Flansch? Gewinde? Rumpf?
- Gegenmutter auf Festigkeit prüfen (Handfest + 1/4 Umdrehung)

**Behebung:**
1. **Dichtstoff gerissen**: Provisorisch: Von innen mit Sikaflex 291i nachdichten (nur temporär!). Dauerhaft: Borddurchlass ausbauen und neu eindichten.
2. **Lockere Mutter**: Nachziehen (Handfest + 1/4 Umdrehung). Wenn das Problem wiederkehrt: Sicherungsmutter oder Loctite 243.
3. **Gewinde inkompatibel**: Passendes Fitting beschaffen.
4. **Korrosion**: Fitting ersetzen.
5. **Rumpfschaden**: Borddurchlass ausbauen, Laminat reparieren, neu einbauen.

**Notmaßnahme auf See**: Dichtstoffring von innen mit 2-Komponenten-Epoxid (z.B. JB Water Weld) abdichten. Hält temporär, bis Werft erreichbar.

(Confidence: documented)

### Problem 3: Motor überhitzt (Kühlwasser-Mangel)

**Symptom**: Motor-Temperaturanzeige steigt über Normal (>90 °C), Alarm bei 95–100 °C. Wenig oder kein Kühlwasser am Auspuff sichtbar.

**Ursachen (borddurchlass-bezogen):**
1. Bewuchs am Scoop-Strainer (40 %)
2. Seeventil geschlossen (20 %)
3. Blockierter Seewasserfilter (25 %)
4. Geknickter oder blockierter Schlauch (10 %)
5. Defekte Seewasserpumpe (5 % — nicht borddurchlass-bezogen)

**Diagnose:**
1. Seeventil-Position prüfen (offen = Hebel parallel zum Schlauch)
2. Seewasserfilter öffnen, prüfen (Deckelglas)
3. Schlauch visuell prüfen (Knick, Quetschung)
4. Scoop-Strainer von Taucher prüfen lassen (wenn Boot im Wasser)

**Behebung:**
1. **Bewuchs**: Taucher reinigen lassen, oder Boot slippen
2. **Seeventil geschlossen**: Öffnen (Fehler des Eigners — Checkliste!)
3. **Filter blockiert**: Reinigen, ggf. Sieb ersetzen
4. **Schlauch geknickt**: Schlauch neu verlegen, ggf. Bogen statt Knick

(Confidence: documented)

### Problem 4: Galvanische Korrosion am Borddurchlass

**Symptom**: Metallische Borddurchlässe zeigen ungewöhnlich schnelle Korrosion, Zinkanoden sind in wenigen Wochen aufgebraucht.

**Ursachen:**
1. Fehlender oder defekter Galvanic Isolator am Landstrom (35 %)
2. Materialmischung (Bronze + Edelstahl + Aluminium) (25 %)
3. Defektes Bonding-System (Unterbrechung) (20 %)
4. Fremdstrom von Nachbarbooten in Marina (15 %)
5. Defekte Opferanoden (5 %)

**Diagnose:**
1. Anodenverbrauch messen (>50 % in <6 Monaten = abnormal)
2. Galvanic Isolator mit Multimeter prüfen (Durchgangsspannung 1,2–1,8 V)
3. Bonding-System durchmessen (Widerstand <1 Ω zwischen allen Durchlässen)
4. Marina-Erdung prüfen lassen (Fachmann!)
5. Material aller Durchlässe dokumentieren — Mischung identifizieren

**Behebung:**
1. **Galvanic Isolator**: Ersetzen (ProSafe FS30, ~180 EUR)
2. **Materialmischung**: Langfristig vereinheitlichen (Marelon oder Bronze)
3. **Bonding**: Unterbrochene Verbindungen reparieren, alle Klemmen reinigen
4. **Fremdstrom**: Isolationstransformator (Mastervolt IVET, ~800 EUR)
5. **Anoden**: Erneuern, korrekte Legierung (Zink in Salzwasser, Magnesium in Süßwasser)

(Confidence: documented)

### Problem 5: Geruch aus Toiletten-Borddurchlass

**Symptom**: Übler Geruch aus dem Bereich des Toiletten-Borddurchlasses, besonders bei warmem Wetter.

**Ursachen:**
1. Permeation durch Standard-PVC-Schlauch (60 %) — Geruchsmoleküle durchdringen Schlauchwand
2. Undichte Schlauchverbindung (20 %)
3. Rückfluss durch fehlende Rückschlagklappe (10 %)
4. Biofilm im Seeventil (10 %)

**Diagnose:**
- Schlauchtyp identifizieren: Standard-PVC oder Sanitärschlauch?
- Schlauchschellen prüfen
- Seeventil öffnen/schließen, Geruchsveränderung?

**Behebung:**
1. **PVC-Schlauch**: Durch geruchsdichten Sanitärschlauch ersetzen (Shields 148 Series, Trident 101/102). Kosten: ~80–150 EUR für 3 m.
2. **Undichte Schlauchverbindung**: Schlauchschellen erneuern, doppelt befestigen.
3. **Fehlende Rückschlagklappe**: Jabsco 29295-1000 Rückschlagventil einbauen (~35 EUR).
4. **Biofilm**: Seeventil demontieren, mit Essig/Zitronensäure reinigen.

(Confidence: documented)

---

## FAQ

### BD-001: Was ist der Unterschied zwischen einem Borddurchlass und einem Seeventil?
Ein Borddurchlass (Skin Fitting, Through-Hull) ist die Durchführung durch den Rumpf — das Fitting selbst. Ein Seeventil (Seacock) ist das Absperrventil, das auf den Borddurchlass montiert wird und den Wasserfluss kontrolliert. Unter der Wasserlinie sind beide als System erforderlich.
(Confidence: documented)

### BD-002: Muss jeder Borddurchlass ein Seeventil haben?
Unter der Wasserlinie: Ja, nach ABYC H-27 und ISO 9093 Pflicht. Ausnahme: Geber-Durchführungen (Echolot) haben typischerweise kein Seeventil, aber einen Blindstopfen. Über der Wasserlinie: Empfohlen, aber nicht Pflicht.
(Confidence: documented)

### BD-003: Kann ich Bronze-Borddurchlässe in einem Aluminium-Rumpf verwenden?
**NEIN.** Bronze in Kontakt mit Aluminium in Seewasser verursacht massive galvanische Korrosion am Aluminium (Potentialdifferenz ~500 mV). Verwenden Sie ausschließlich Kunststoff (Marelon, TruDesign) oder Titan.
(Confidence: documented)

### BD-004: Wie oft sollten Borddurchlässe inspiziert werden?
Jährlich beim Haulout: Seeventile betätigen, visuell prüfen, Schlauchschellen nachziehen. Alle 5 Jahre: Dichtstoff prüfen. Alle 10–15 Jahre: Austausch prüfen lassen (abhängig von Material und Revier).
(Confidence: benchmark)

### BD-005: Was ist besser — Bronze oder Marelon?
Beide sind ISO 9093 konform. Bronze: Langlebiger (30–50 Jahre), hitzebeständig (>250 °C), schwerer, teurer. Marelon: Galvanisch inert, leicht, günstig, max. 82 °C. Für Aluminium-Rümpfe: Nur Marelon/TruDesign. Für Abgasdurchlässe: Nur Bronze/316L.
(Confidence: documented)

### BD-006: Sind Nylon-Borddurchlässe unter der Wasserlinie zugelassen?
**NEIN** (in der Regel). Standard-Nylon (PA6) ohne Glasfaserverstärkung ist **nicht** ISO 9093-2 konform. Nur PA66-GF30 (Marelon, TruDesign) ist zugelassen. Einfache Nylon-Fittings nur über der Wasserlinie verwenden.
(Confidence: documented)

### BD-007: Welchen Dichtstoff soll ich unter der Wasserlinie verwenden?
Erste Wahl: Polysulfid (3M 101, Boat-Life Life-Calk). Zweite Wahl: Polyurethan (Sikaflex 291i). **KEIN** Silikon unter der Wasserlinie — schlechte Haftung auf GFK, kriecht unter Last.
(Confidence: documented)

### BD-008: Was ist der Unterschied zwischen BSP und NPT Gewinde?
BSP (British Standard Pipe) ist zylindrisch und dichtet mit Flachdichtung. NPT (National Pipe Thread) ist konisch und dichtet über die Keilwirkung. Sie sind **nicht kompatibel**, obwohl die Nennmaße ähnlich aussehen.
(Confidence: documented)

### BD-009: Wie viele Borddurchlässe hat ein typisches 10-m-Segelboot?
Typisch 8–13 Borddurchlässe, davon 3–6 unter der Wasserlinie (Motor-Einlass, Toilette Ein-/Auslass, ggf. Echolot). Jeder Durchlass unter WL sollte ein Seeventil haben.
(Confidence: benchmark)

### BD-010: Muss ich Notholzstopfen an Bord haben?
Bei CE-Kategorie A und B: **Ja, Pflicht** nach RCD 2013/53/EU. Für jeden Borddurchlass unter der Wasserlinie muss ein passender konischer Holzstopfen griffbereit sein. Empfohlen für alle Boote.
(Confidence: documented)

### BD-011: Warum korrodiert mein 316L-Seeventil im Mittelmeer?
316L ist anfällig für Spaltkorrosion und Lochfraß in warmem Seewasser (>25 °C). Im Gewinde entstehen Spalte mit Sauerstoffmangel → lokale Säurebildung → Korrosion. Bronze C83600 ist in warmen Gewässern unter WL die sicherere Wahl.
(Confidence: documented)

### BD-012: Kann ich einen Borddurchlass selbst austauschen?
Ja, bei Erfahrung in GFK-Arbeit und wenn das Boot an Land steht. Für Sandwich-Rümpfe: Kernverstärkung ist kritisch — bei Unsicherheit Werft beauftragen. Erstausrüster sollten einen erfahrenen DIY-Segler oder Werft hinzuziehen.
(Confidence: documented)

### BD-013: Was ist ein Scoop-Strainer und wann brauche ich einen?
Ein Scoop-Strainer ist ein kombinierter Wassereinlass mit integriertem Sieb und Schaufel. Er wird für Motorkühlwasser, Klimaanlagen und Watermaker verwendet. Der Scoop leitet Wasser aktiv ein, das Sieb filtert Fremdkörper. Empfohlen für alle Kühlwassereinlässe.
(Confidence: documented)

### BD-014: Wie erkenne ich Entzinkung?
Das Material verfärbt sich rosa-kupferfarben (statt goldgelb bei Messing). Die Oberfläche wird porös und rauh. Kratztest: Mit einem Messer kratzen — entzinktes Material ist weich wie Butter, gesundes Bronze/Messing ist hart.
(Confidence: documented)

### BD-015: Warum darf kein Gate-Valve (Schieber) als Seeventil verwendet werden?
Gate Valves (Schieber) sind nicht für marine Anwendungen zugelassen (ABYC H-27), weil: 1) Die Spindel korrodiert und setzt fest. 2) Es gibt keinen eindeutigen Offen/Zu-Indikator. 3) Schließzeit ist lang (mehrere Umdrehungen vs. 1/4 Drehung beim Kugelhahn).
(Confidence: documented)

### BD-016: Brauche ich doppelte Schlauchschellen unter der Wasserlinie?
**Ja**, nach ABYC H-27 und Best Practice. Beide Schellen aus 316L Edelstahl, min. 12,7 mm Bandbreite. Nicht-perforiertes Band bevorzugt (Solid Band).
(Confidence: documented)

### BD-017: Was kostet ein kompletter Borddurchlass-Austausch?
Material: 150–250 EUR (Durchlass + Seeventil + Dichtstoff + Schlauchschellen). Werft-Arbeit: 150–350 EUR (1–3 Stunden á 75–120 EUR/h). Gesamt: 300–600 EUR pro Durchlass. Bei Sandwich-Rumpf mit Kernverstärkung +200 EUR.
(Confidence: benchmark)

### BD-018: Wie wichtig ist das Bonding-System für Borddurchlässe?
Sehr wichtig bei metallischen Durchlässen. Das Bonding-System verbindet alle metallischen Unterwasser-Teile elektrisch und leitet galvanische Ströme an die Opferanoden ab. Ohne Bonding korrodiert das unedelste Metall (oft das teuerste Bauteil). Kunststoff-Durchlässe benötigen kein Bonding.
(Confidence: documented)

### BD-019: Kann ich verschiedene Materialien bei Borddurchlässen mischen?
Möglich, aber mit Vorsicht. Bronze + Bronze: Kein Problem. Bronze + 316L: Potentialdifferenz ~200 mV, akzeptabel mit Bonding und Opferanoden. Bronze + Aluminium: **VERBOTEN**. Kunststoff + alles: Kein Problem (galvanisch inert).
(Confidence: documented)

### BD-020: Wie groß muss die Backing-Plate sein?
Mindestens 3× Nennweite des Borddurchlasses im Durchmesser. Beispiel: 3/4" (19 mm) Durchlass → Backing-Plate min. 57 mm Ø. Material: G10 oder GFK, Dicke min. 6–10 mm. Bei Lloyd's-Klasse: Min. 10 mm GFK.
(Confidence: documented)

### BD-021: Was mache ich, wenn ein Borddurchlass auf See bricht?
1. Notholzstopfen einschlagen (muss griffbereit an Schnur hängen). 2. Wenn kein Stopfen: Lap (Tuch), Handtuch, Kissen in die Öffnung pressen. 3. Bilgenpumpe einschalten. 4. Seeventil schließen (wenn noch intakt). 5. Nächsten Hafen ansteuern. 6. Küstenfunk (Kanal 16) informieren bei unkontrolliertem Wassereinbruch.
(Confidence: documented)

### BD-022: Warum riecht es aus meinem Toiletten-Borddurchlass?
Fast immer: Standard-PVC-Schlauch. Geruchsmoleküle (H₂S, Amine) permeieren durch die PVC-Wand. Lösung: Geruchsdichten Sanitärschlauch verwenden (Shields 148, Trident 101/102). Zusätzlich: Rückschlagventil einbauen.
(Confidence: documented)

### BD-023: Stimmt es, dass Scoop-Strainer den Widerstand erhöhen?
Ja, marginal. Der zusätzliche Widerstand eines Scoop-Strainers beträgt ca. 0,01–0,03 kn bei 6 kn Fahrt (vernachlässigbar). Der Vorteil (Fremdkörperschutz, aktive Wasserzufuhr) überwiegt den minimalen Widerstandsnachteil bei Fahrtenyachten. Bei Rennbooten: Flush-Mount-Einlass verwenden.
(Confidence: estimated)

### BD-024: Welche Borddurchlässe müssen aus Metall sein?
Nach ABYC H-27: Alle Abgas-Borddurchlässe (Temperatur >65 °C) müssen aus Metall (Bronze oder 316L) sein. Kunststoff ist bei Abgas nicht zulässig. Für alle anderen Anwendungen sind ISO 9093-2 konforme Kunststoffe erlaubt.
(Confidence: documented)

### BD-025: Was ist der beste Borddurchlass für einen Neubau?
Empfehlung 2025: **TruDesign 90400-Serie** (Skin Fittings) + **TruDesign 90600-Serie** (Seacocks) für alle Anwendungen unter 93 °C. Für Abgas: **Groco TH + BV-Serie** (Bronze C83600). Für Aluminium-Rümpfe: Ausschließlich TruDesign oder Marelon. Für Superyachten: **Guidi** oder **Groco** in Bronze C92200 (Navy Bronze).
(Confidence: benchmark)

---

## Glossar

| Nr. | Begriff | Englisch | Definition |
|---|---|---|---|
| G-001 | Borddurchlass | Through-hull fitting, Skin fitting | Durchführung durch den Rumpf eines Bootes für Rohrleitungen, Kabel oder Instrumente |
| G-002 | Seeventil | Seacock | Absperrventil direkt am Borddurchlass, zum Schließen des Durchlasses |
| G-003 | Kugelhahn | Ball valve | Ventiltyp mit drehbarer Kugel, 1/4-Drehung öffnet/schließt |
| G-004 | Kükenventil | Plug valve, Taper plug cock | Traditionelles Ventil mit konischem Küken |
| G-005 | Schieber | Gate valve | Ventil mit verschiebbarem Absperrkörper — **nicht empfohlen** für marine Anwendung |
| G-006 | Scoop-Strainer | Scoop strainer | Wassereinlass mit Schaufel und integriertem Sieb |
| G-007 | Pilzförmig | Mushroom type | Standard-Borddurchlassform mit breitem Flansch außen |
| G-008 | Bündig | Flush mount | Borddurchlass bündig mit Rumpfaußenhaut |
| G-009 | Geflancht | Flanged | Beidseitig geflanscht, Schraubverbindung |
| G-010 | Backing-Plate | Backing plate | Lastverteilungsplatte auf der Rumpfinnenseite |
| G-011 | Kernverstärkung | Core reinforcement | Entfernung und Füllung des Sandwich-Kerns an Durchlass-Stellen |
| G-012 | Notholzstopfen | Emergency wooden plug | Konischer Holzstopfen zum Verschließen bei Havarie |
| G-013 | Gegenmutter | Lock nut | Mutter auf der Rumpfinnenseite zur Fixierung des Durchlasses |
| G-014 | Entzinkung | Dezincification | Selektive Auflösung von Zink aus Messing/Bronze-Legierungen |
| G-015 | Spaltkorrosion | Crevice corrosion | Korrosion in engen Spalten durch Sauerstoffverarmung |
| G-016 | Lochfraß | Pitting corrosion | Lokaler Korrosionsangriff mit Lochbildung |
| G-017 | Galvanische Korrosion | Galvanic corrosion | Korrosion durch Kontakt unterschiedlicher Metalle in Elektrolyt |
| G-018 | Bonding-System | Bonding system | Elektrische Verbindung aller metallischen Unterwasserteile |
| G-019 | Opferanode | Sacrificial anode | Unedleres Metall (Zink, Magnesium), das sich zum Schutz auflöst |
| G-020 | BSP | British Standard Pipe | Zylindrisches Rohrgewinde nach ISO 228 |
| G-021 | NPT | National Pipe Thread | Konisches Rohrgewinde nach ANSI B1.20.1 |
| G-022 | Polysulfid | Polysulfide | Elastischer Dichtstoff, erste Wahl unter Wasserlinie |
| G-023 | Polyurethan (PU) | Polyurethane | Elastischer Dichtstoff, sehr hohe Haftung |
| G-024 | PTFE-Band | PTFE tape, Teflon tape | Gewindedichtband aus Polytetrafluorethylen |
| G-025 | Schlauchschelle | Hose clamp, Jubilee clip | Spannband zur Befestigung von Schläuchen |
| G-026 | Marelon | Marelon | Markenname für glasfaserverstärktes Polyamid (Forespar) |
| G-027 | Rotguss | Red brass, Gunmetal | Kupfer-Zinn-Legierung (C83600) für marine Anwendungen |
| G-028 | Geber-Durchführung | Transducer fitting | Spezial-Durchlass für Echolot-/Geschwindigkeitsgeber |
| G-029 | Nass-Abgas | Wet exhaust | Abgassystem mit Kühlwassereinspritzung |
| G-030 | Anti-Siphon-Ventil | Anti-siphon valve | Ventil zur Verhinderung des Siphon-Effekts |
| G-031 | Galvanic Isolator | Galvanic isolator | Gerät zur Blockierung galvanischer Ströme über Landstromkabel |
| G-032 | Sandwich-Bauweise | Sandwich construction | Rumpfaufbau aus zwei GFK-Schalen mit Kernmaterial dazwischen |
| G-033 | G10/FR4 | G10/FR4 | Glasfaser-Epoxid-Laminat für Backing-Plates |
| G-034 | Rückschlagventil | Check valve, Non-return valve | Ventil, das Strömung nur in eine Richtung zulässt |
| G-035 | Seewasserfilter | Raw water strainer | Filter in der Seewasserleitung (z.B. Groco ARG) |
| G-036 | Bewuchs | Fouling, Marine growth | Biologischer Bewuchs (Seepocken, Algen, Muscheln) |
| G-037 | Cockpit-Drain | Cockpit drain | Ablauf zur Entwässerung des Cockpits |
| G-038 | Rumpfdurchführung | Hull penetration | Allgemein: Jede Durchdringung des Rumpfes |
| G-039 | Dichtmasse | Sealant, Bedding compound | Material zum Abdichten der Verbindung Fitting↔Rumpf |
| G-040 | Tülle | Hose barb, Tail piece | Schlauchtülle am Seeventil für Schlauchanschluss |
| G-041 | Wasserlinie | Waterline (WL) | Grenzlinie zwischen Unterwasserschiff und Überwasserschiff |
| G-042 | CE-Kategorie | CE Category | Entwurfskategorie nach RCD 2013/53/EU (A, B, C, D) |
| G-043 | Survey | Survey | Professionelle Inspektion eines Bootes |
| G-044 | Haulout | Haulout | Herausnahme des Bootes aus dem Wasser (Slippen) |
| G-045 | Bilge | Bilge | Tiefster Bereich im Bootsrumpf, wo sich Wasser sammelt |

---

## Schnell-Referenz

### Schnell-Referenz: Material-Wahl

```
Borddurchlass-Material wählen:

GFK-Rumpf, unter WL:
  → Standard: Bronze C83600
  → Budget: Marelon / TruDesign
  → Premium: Bronze C92200 (Navy)

GFK-Rumpf, über WL:
  → Alle Materialien ok
  → Budget: Nylon / Marelon

Aluminium-Rumpf:
  → NUR Marelon / TruDesign / Titan
  → KEIN Bronze, KEIN Edelstahl!

Stahl-Rumpf:
  → 316L oder Bronze oder Marelon

Abgas-Durchlass:
  → NUR Bronze oder 316L (kein Kunststoff!)

Temperaturen >82°C:
  → NUR Metall (Bronze oder 316L)
```

### Schnell-Referenz: Borddurchlass-Checkliste beim Haulout

```
□ Alle Seeventile öffnen/schließen — leichtgängig?
□ Visuelle Inspektion: Korrosion, Entzinkung, Risse?
□ Dichtstoff-Ringe: Risse, Ablösung?
□ Schlauchschellen nachziehen (2 Nm)
□ Bonding-Kabel: Fest? Korrosion an Klemme?
□ Notholzstopfen: Vorhanden? Passend? Zugänglich?
□ Scoop-Strainer: Bewuchs entfernen
□ Zinkanoden: >50% Abtrag? → Ersetzen
□ Borddurchlass-Plan aktualisieren
□ Befunde dokumentieren (Fotos!)
```

### Schnell-Referenz: Notfall "Wassereinbruch durch Borddurchlass"

```
1. SEEVENTIL SCHLIESSEN (Hebel quer zum Schlauch)
2. Notholzstopfen einschlagen (konisch, Holz)
3. Bilgenpumpe(n) einschalten
4. Leckrate einschätzen
5. Nächsten Hafen ansteuern
6. Bei unkontrolliertem Einbruch: Küstenfunk Kanal 16
7. Rettungswesten anlegen
8. Rettungsinsel klarmachen

FAUSTREGEL: 1" offener Durchlass in 1m Tiefe = ~78 l/min
→ 10m Boot sinkt in ~25 min
```

---

## Notfall-Ressourcen

### Notfall-Kontakte

| Situation | Kontakt | Nummer |
|---|---|---|
| Seenotfall (DE) | MRCC Bremen (DGzRS) | Kanal 16, Tel. 0421-536870 |
| Seenotfall (EU allgemein) | Küstenfunk | VHF Kanal 16, DSC Kanal 70 |
| Seenotfall (int.) | GMDSS | 2187.5 kHz (MF DSC) |
| Technische Hilfe (DE) | BoatUS-Äquivalent, ADAC Sportschifffahrt | 089-76 76 77 |
| Survey nach Schaden | BVSI (Bundesverband öffentlich bestellter und vereidigter Sachverständiger) | bvsi.org |
| Versicherung Schaden | Pantaenius | +49 40 37 09 10 |

### Notfall-Ausrüstung für Borddurchlass-Havarie

| Ausrüstung | Spezifikation | Preis EUR |
|---|---|---|
| Notholzstopfen-Set | 6 Stück, konisch, Kiefer, 10–50 mm | 15–30 |
| Emergency Plug Kit (Forespar) | 3 Größen, Gummi-Konus + Schraube | 35 |
| Stay Afloat (Leak Repair Putty) | 2-Komponenten, wasserfest, 50g | 18 |
| JB Water Weld | Epoxid-Knetmasse, unterwasser-aushärtend | 12 |
| Bilgenpumpe (manuell) | Whale Gusher Urchin, 55 l/min | 95 |
| Bilgenpumpe (elektrisch) | Rule 2000 GPH, 12V | 85 |
| Leckdichtungs-Matten | Dynaplate, selbstklebend, 300×300 mm | 45 |

(Confidence: documented)

---

## ANHÄNGE

### ANHANG A — Cross-Reference: Hersteller-Teilenummern

| Nennweite | Groco TH | TruDesign 904xx | Guidi 1210 | Forespar MF | Perko 0350 | Osculati 17.319 |
|---|---|---|---|---|---|---|
| 1/2" (13mm) | TH-500-W | 90401 | 1210/13 | MF-500 | 0350-005 | 17.319.01 |
| 3/4" (19mm) | TH-750-W | 90402 | 1210/19 | MF-750 | 0350-006 | 17.319.02 |
| 1" (25mm) | TH-1000-W | 90403 | 1210/25 | MF-1000 | 0350-007 | 17.319.03 |
| 1-1/4" (32mm) | TH-1250-W | 90404 | 1210/32 | MF-1250 | 0350-008 | 17.319.04 |
| 1-1/2" (38mm) | TH-1500-W | 90405 | 1210/38 | MF-1500 | 0350-009 | 17.319.05 |
| 2" (50mm) | TH-2000-W | 90406 | 1210/50 | MF-2000 | 0350-010 | 17.319.06 |

**Gewinde-Hinweis**: Groco + Forespar + Perko = NPT. TruDesign + Guidi + Osculati = BSP.

(Confidence: documented)

### ANHANG B — Legierungs-Vergleich

| Eigenschaft | C83600 (Rotguss) | C84400 | C92200 (Navy) | C95800 (NiAlBronze) | 316L | Marelon |
|---|---|---|---|---|---|---|
| Zugfestigkeit [MPa] | 255 | 235 | 275 | 585 | 485–690 | 82 |
| Streckgrenze [MPa] | 117 | 105 | 125 | 245 | 170–310 | 55 |
| Bruchdehnung [%] | 20 | 18 | 25 | 18 | 40–60 | 4 |
| Härte [HB] | 65 | 60 | 70 | 170 | 150–200 | — |
| Dichte [g/cm³] | 8,83 | 8,70 | 8,80 | 7,64 | 7,98 | 1,80 |
| Schmelzpunkt [°C] | 1.000 | 980 | 1.010 | 1.060 | 1.375 | 260 (Erweichung) |
| Galv. Potenzial [mV] | -310 | -320 | -280 | -220 | -80 | Inert |
| Zinkanteil [%] | 5 | 7 | 0 | 0 | 0 | — |
| Entzinkungsrisiko | Sehr gering | Gering | Null | Null | — | — |
| Preis relativ | 1,0× | 0,9× | 1,3× | 2,5× | 1,2× | 0,5× |

(Confidence: documented)

### ANHANG C — Durchfluss-Tabellen

#### Volumenstrom durch Borddurchlass [l/min] bei verschiedenen Druckhöhen

| NW mm | NW Zoll | h=0,3m | h=0,5m | h=1,0m | h=1,5m | h=2,0m |
|---|---|---|---|---|---|---|
| 13 | 1/2" | 11,5 | 14,9 | 21,1 | 25,8 | 29,8 |
| 19 | 3/4" | 24,6 | 31,8 | 44,9 | 55,0 | 63,5 |
| 25 | 1" | 42,5 | 54,9 | 77,7 | 95,1 | 109,8 |
| 32 | 1-1/4" | 69,6 | 89,9 | 127,1 | 155,7 | 179,8 |
| 38 | 1-1/2" | 98,2 | 126,8 | 179,4 | 219,7 | 253,7 |
| 50 | 2" | 169,9 | 219,5 | 310,4 | 380,2 | 439,0 |

Formel: Q = 0,6 × (π/4) × d² × √(2 × 9,81 × h) × 60.000 [l/min]

(Confidence: calculated)

### ANHANG D — Confidence-Mapping für AYDI-Analyse

| Datenquelle | Confidence-Level | Beschreibung |
|---|---|---|
| CAD-Zeichnung mit Borddurchlass-Plan | measured | Exakte Position, NW, Material |
| Foto vom Haulout (klar, nah) | visual_high | Material und Zustand erkennbar |
| Foto vom Innenraum (Seeventil sichtbar) | visual_medium | Seeventil-Typ erkennbar, Zustand eingeschränkt |
| Foto unscharf / dunkel | visual_low | Nur Anwesenheit prüfbar |
| Eigner-Angaben (Inventarliste) | documented | Material und Anzahl, nicht verifiziert |
| Boots-Klasse-Template | estimated | Durchschnitts-Inventar nach Boots-Typ |
| Herstellerangabe (z.B. Bavaria Handbuch) | benchmark | Standard-Ausstattung, kann geändert sein |
| Survey-Bericht | documented | Professionelle Bewertung |
| Service-Protokoll Werft | documented | Reparatur-/Austauschhistorie |

(Confidence: documented)

### ANHANG E — Bordausstattung: Borddurchlass-Inventar nach Bootsklasse

#### Richtwerte für die AYDI-Schnellanalyse (Level 1)

| Bootsklasse | Länge [m] | Borddurchlässe gesamt | Unter WL | Seeventile |
|---|---|---|---|---|
| Jollenkreuzer | 6–8 | 3–5 | 1–2 | 1–2 |
| Segelyacht klein | 8–10 | 6–10 | 3–5 | 3–5 |
| Segelyacht mittel | 10–14 | 10–15 | 5–8 | 5–8 |
| Segelyacht groß | 14–18 | 15–22 | 8–13 | 8–13 |
| Segelyacht XL | 18–24 | 20–35 | 12–20 | 12–20 |
| Motoryacht klein | 8–12 | 10–16 | 5–8 | 5–8 |
| Motoryacht mittel | 12–18 | 16–25 | 8–14 | 8–14 |
| Motoryacht groß | 18–24 | 25–40 | 14–25 | 14–25 |
| Superyacht | 24–40 | 35–65 | 20–40 | 20–40 |

(Confidence: benchmark)

### ANHANG F — Fallstudien

#### Fallstudie F-01: Sinken durch entzinkten Borddurchlass (Ostsee, 2019)

Eine 11 m Segelyacht (Baujahr 1985, GFK) sank im Hafen über Nacht. Die Ursache: Ein 3/4"-Borddurchlass für den Toiletten-Einlass, der als "Bronze" gekennzeichnet war, bestand tatsächlich aus Messing (CW617N, 37 % Zink). Nach 34 Jahren war das Fitting vollständig entzinkt. Ein leichter Schlag beim Festmachen brach den Durchlass. Wassereinbruch: ~32 l/min. Das Boot sank in ca. 4 Stunden unbemerkt.
**Lehre**: Alle Borddurchlässe >20 Jahre alt auf Entzinkung prüfen (Kratztest). Jährliche Inspektion rettet Boote.
**Schaden**: Totalverlust ~45.000 EUR, gedeckt durch Kaskoversicherung.
**AYDI-Score**: 0/100 (retrospektiv). Confidence: documented.

#### Fallstudie F-02: Elektrolyse-Katastrophe am Aluminium-Rumpf (Kroatien, 2021)

Eine 14 m Aluminium-Segelyacht (Baujahr 2008) wurde bei einem Survey mit massiver Korrosion am Rumpf um alle 8 Bronze-Borddurchlässe herum vorgefunden. Materialabtrag am Aluminium bis 4 mm (Rumpfdicke original 6 mm). Ursache: Der Vorbesitzer hatte die Original-Marelon-Durchlässe durch "hochwertige" Bronze-Durchlässe ersetzt. Zusätzlich: Defekter Galvanic Isolator am Landstrom.
**Lehre**: NIEMALS metallische Borddurchlässe in Aluminium-Rümpfen einbauen. Bootshandbuch lesen.
**Schaden**: Reparatur (8 neue TruDesign + Alu-Rumpfreparatur) ~18.000 EUR.
**AYDI-Score**: 5/100. Confidence: documented.

#### Fallstudie F-03: Motorschaden durch zugewachsenen Scoop-Strainer (Griechenland, 2022)

Eine 12 m Motoryacht (Twin-Diesel, je 150 PS) erlitt einen Motorschaden (Steuerbord) durch Überhitzung. Ursache: Der Scoop-Strainer (Groco SC-1000) war nach 10 Monaten ohne Antifouling vollständig mit Seepocken zugewachsen. Durchfluss: praktisch null. Der Motor überhitzte bei Volllast auf 105 °C, der Alarm wurde vom Eigner ignoriert ("war schon immer etwas hoch"). Folge: Zylinderkopfdichtung defekt.
**Lehre**: Scoop-Strainer im Mittelmeer min. vierteljährlich reinigen. Antifouling auf Scoop-Strainer auftragen. Motor-Alarm NIEMALS ignorieren.
**Schaden**: Motor-Reparatur (Zylinderkopf) ~4.500 EUR. Scoop-Reinigung: 80 EUR (Taucher).
**AYDI-Score**: 45/100 (vor Reinigung). Confidence: documented.

#### Fallstudie F-04: Erfolgreicher DIY-Austausch aller Borddurchlässe (Niederlande, 2023)

Ein erfahrener Eigner tauschte an seiner 10 m Segelyacht (GFK solid, Baujahr 1998) alle 8 Borddurchlässe in Eigenregie aus. Grund: Alle Original-Bronze-Fittings zeigten nach 25 Jahren leichte Korrosion. Er wählte TruDesign 90400/90600 als Ersatz, um galvanische Probleme zu eliminieren. Arbeitszeit: 3 Wochenenden (ca. 40 Stunden). Material: ~680 EUR.
**Lehre**: Mit Erfahrung und Sorgfalt ist DIY-Austausch wirtschaftlich sinnvoll. Werkstattkosten eingespart: ca. 2.400 EUR.
**Ergebnis**: AYDI-Score 95/100. Confidence: documented.

#### Fallstudie F-05: Sandwich-Kern-Schaden durch undichten Borddurchlass (Frankreich, 2020)

Eine 13 m Segelyacht (GFK/Balsa-Sandwich, Baujahr 2005) zeigte weiche Stellen im Rumpf um einen 1"-Borddurchlass. Ursache: Der Dichtstoff (Silikon — falsche Wahl!) hatte sich nach 8 Jahren gelöst. Wasser war über 3–4 Jahre in den Balsa-Kern eingedrungen. Der kompromittierte Bereich: ca. 0,8 m² um den Durchlass. Der Balsa war vollständig aufgequollen und verrottet.
**Lehre**: 1) Niemals Silikon unter WL verwenden. 2) Balsa-Sandwich erfordert perfekte Abdichtung. 3) Jährliche Inspektion kann den Schaden früh erkennen.
**Schaden**: Laminat-Reparatur (Kern-Austausch) ~12.000 EUR.
**AYDI-Score**: 10/100. Confidence: documented.

#### Fallstudie F-06: CE-Survey-Durchfall wegen fehlender Seeventile (Deutschland, 2022)

Eine 9 m Segelyacht (CE-Kategorie B, Baujahr 2015) fiel beim Verkaufs-Survey durch, weil 2 von 4 Borddurchlässen unter der Wasserlinie keine Seeventile hatten. Der Erstbesitzer hatte die Seeventile für den Toiletten-Ein- und -Auslass entfernt ("waren schwer zu bedienen") und durch einfache Schlauchanschlüsse ersetzt. Der Surveyor stufte das Boot als "nicht seetüchtig" ein.
**Lehre**: Seeventile unter WL sind keine Option, sondern Pflicht. Schwergängige Ventile warten, nicht entfernen.
**Kosten der Nachrüstung**: 2 × Seeventil (Guidi 1160/19 + 1160/25) + Arbeit = ~480 EUR.
**AYDI-Score**: 25/100 (Compliance). Confidence: documented.

#### Fallstudie F-07: Notholzstopfen rettet Boot nach Borddurchlass-Bruch (Norwegen, 2023)

Bei einer 12 m Segelyacht brach der 3/4"-Bronze-Borddurchlass für den Motorkühlwasser-Einlass während der Fahrt (Ermüdungsbruch nach 30 Jahren). Der Skipper reagierte sofort: Seeventil geschlossen (war am selben Fitting, ebenfalls beschädigt, schloss nicht vollständig), Notholzstopfen eingeschlagen, Bilgenpumpe ein. Der Holzstopfen hielt den Wassereinbruch auf ~2 l/min. Das Boot erreichte sicher den nächsten Hafen.
**Lehre**: Notholzstopfen funktionieren. Sie müssen griffbereit sein. Jede Sekunde zählt.
**Schaden**: Neuer Borddurchlass + Seeventil + Einbau = ~450 EUR. Ohne Holzstopfen: Totalverlust.
**AYDI-Score**: Notfall-Management 95/100. Confidence: documented.

#### Fallstudie F-08: Superyacht-Borddurchlass-Audit (Mallorca, 2024)

Eine 28 m Motoryacht (Baujahr 2012, GFK-Sandwich) wurde einem vollständigen Borddurchlass-Audit unterzogen. 47 Borddurchlässe wurden inspiziert, davon 28 unter WL. Ergebnis: 3 Durchlässe mit Spaltkorrosion (316L im Maschinenraum), 2 mit gealtertem Dichtstoff, 1 mit fehlender Backing-Plate, 5 ohne Bonding-Anschluss. Alle Gate-Valves (4 Stück, im Maschinenraum) wurden durch Kugelhähne ersetzt.
**Gesamtkosten**: Material + Arbeit = ~8.500 EUR. Ergebnis-AYDI-Score nach Reparatur: 88/100.
**Lehre**: Auch moderne Yachten haben Borddurchlass-Defizite. Regelmäßige Audits sind auch bei Superyachten wichtig.
**Confidence**: documented.

### ANHANG G — Experten-Referenzen

| Name | Qualifikation | Spezialgebiet | Land |
|---|---|---|---|
| Nigel Calder | Marine-Autor, Ingenieur | "Boatowner's Mechanical and Electrical Manual" (Kapitel über Borddurchlässe) | USA/UK |
| Don Casey | Marine-Autor | "This Old Boat" — DIY-Borddurchlass-Austausch | USA |
| Steve D'Antonio | Marine Surveyor, Autor | Borddurchlass-Materialwahl, Korrosion | USA |
| Michael Herrmann | SV-geprüfter Sachverständiger | Borddurchlässe bei Gebrauchtboot-Survey | DE |
| Manfred Neumann | BVSI-Sachverständiger | Osmose und Borddurchlässe | DE |
| Tom Cunliffe | RYA-Yachtmaster Instructor | Seemannschaft, Notfall-Management | UK |

(Confidence: documented)

### ANHANG H — Risk Matrix: Borddurchlass-Risiken

| Risiko | Wahrscheinlichkeit (1–5) | Auswirkung (1–5) | Risiko-Score | Priorität |
|---|---|---|---|---|
| Entzinkung (Messing unter WL) | 4 | 5 | 20 | **Kritisch** |
| Dichtstoff-Versagen (>10 Jahre) | 3 | 4 | 12 | **Hoch** |
| Bewuchsverblockung | 4 | 2 | 8 | Mittel |
| Gate-Valve festgesetzt | 3 | 3 | 9 | Mittel |
| Galvanische Korrosion (Materialmix) | 2 | 5 | 10 | **Hoch** |
| Fehlende Backing-Plate (Sandwich) | 2 | 4 | 8 | Mittel |
| Falsches Gewinde (BSP/NPT) | 2 | 3 | 6 | Niedrig |
| Kunststoff-Bruch (UV/Alter) | 2 | 5 | 10 | **Hoch** |
| Fehlende Notholzstopfen | 4 | 2 (nur im Notfall relevant) | 8 | Mittel |
| Nicht zugängliches Seeventil | 3 | 3 | 9 | Mittel |

(Confidence: benchmark)

### ANHANG I — Audit/Compliance-Checkliste

#### ISO 9093 / ABYC H-27 Compliance-Checkliste

| Nr. | Prüfpunkt | ISO 9093 | ABYC H-27 | Ergebnis |
|---|---|---|---|---|
| I-01 | Alle Durchlässe unter WL mit Seeventil? | Empfohlen | Pflicht | □ OK □ NOK |
| I-02 | Seeventile als Kugelhahn oder Kükenventil? | Empfohlen | Pflicht | □ OK □ NOK |
| I-03 | Seeventile ohne Werkzeug bedienbar? | — | Pflicht | □ OK □ NOK |
| I-04 | Material konform (kein Messing unter WL)? | Pflicht | Pflicht | □ OK □ NOK |
| I-05 | Abgas-Durchlässe aus Metall? | Empfohlen | Pflicht | □ OK □ NOK |
| I-06 | Doppelte Schlauchschellen unter WL? | — | Pflicht | □ OK □ NOK |
| I-07 | Backing-Plates bei GFK/Sandwich? | — | Empfohlen | □ OK □ NOK |
| I-08 | Kern entfernt bei Sandwich? | Pflicht (ISO 12215) | — | □ OK □ NOK |
| I-09 | Notholzstopfen vorhanden (CE Kat. A/B)? | — | Empfohlen | □ OK □ NOK |
| I-10 | Borddurchlass-Plan im Eignerhandbuch? | Pflicht (CE) | Empfohlen | □ OK □ NOK |
| I-11 | Galvanische Isolation bei Alu-Rumpf? | — | Empfohlen | □ OK □ NOK |
| I-12 | Bonding-System intakt? | — | Pflicht (E-2) | □ OK □ NOK |

(Confidence: documented)

### ANHANG J — Material-Datenblätter (Kurzfassung)

#### J-1: Bronze C83600 (Rotguss, Gunmetal)

| Eigenschaft | Wert | Norm |
|---|---|---|
| Zusammensetzung | Cu 85, Sn 5, Zn 5, Pb 5 | ASTM B584 |
| Zugfestigkeit | 255 MPa | — |
| Streckgrenze | 117 MPa | — |
| Bruchdehnung | 20 % | — |
| Härte | 65 HB | — |
| Dichte | 8,83 g/cm³ | — |
| Korrosionsrate in Seewasser | <0,025 mm/Jahr | — |
| Max. Betriebstemperatur | 260 °C | — |
| Entzinkungsrisiko | Sehr gering (5 % Zn) | — |

#### J-2: Edelstahl 316L (1.4404)

| Eigenschaft | Wert | Norm |
|---|---|---|
| Zusammensetzung | Fe-17Cr-12Ni-2,5Mo-0,03C | EN 10088-3 |
| Zugfestigkeit | 485–690 MPa | — |
| Streckgrenze | 170–310 MPa | — |
| Bruchdehnung | 40–60 % | — |
| Härte | 150–200 HB | — |
| Dichte | 7,98 g/cm³ | — |
| PREN (Pitting Resistance) | 24 | — |
| Max. Betriebstemperatur | 500 °C | — |
| Lochfraß-Grenztemperatur | 25 °C (in Spalten) | — |

#### J-3: Marelon (PA66-GF30)

| Eigenschaft | Wert | Norm |
|---|---|---|
| Zusammensetzung | Polyamid 66 + 30 % Glasfaser | — |
| Zugfestigkeit | 82 MPa | ASTM D638 |
| Biegefestigkeit | 130 MPa | ASTM D790 |
| Bruchdehnung | 4 % | — |
| Dichte | 1,80 g/cm³ | — |
| Wasseraufnahme (24h) | 1,2 % | ASTM D570 |
| Max. Betriebstemperatur | 82 °C | — |
| UV-Beständigkeit | Gut (stabilisiert) | — |
| Brandverhalten | UL 94 V-0 | UL 94 |

(Confidence: documented)

### ANHANG K — Prüfverfahren

#### K-1: Kratztest (Entzinkung)

1. Oberfläche des Fittings mit einem Messer oder Schraubendreher kratzen
2. **Gesundes Bronze/Messing**: Hart, metallischer Glanz, goldgelb
3. **Entzinktes Material**: Weich (wie Butter), rosa-kupferfarben, kein Glanz
4. **Bewertung**: Entzinkung erkannt → Score 0, sofortiger Austausch

#### K-2: Klopftest (innere Korrosion)

1. Mit kleinem Hammer oder Holzstück auf Fitting klopfen
2. **Gesund**: Heller, metallischer Klang
3. **Korrodiert/porös**: Dumpfer, matter Klang
4. **Bewertung**: Dumpfer Klang → weitere Untersuchung, ggf. Ultraschall-Wandstärkemessung

#### K-3: Ultraschall-Wandstärkemessung

1. Ultraschall-Wandstärkemessgerät (z.B. Cygnus, Dakota)
2. Koppelmedium auftragen
3. Wandstärke an 4 Punkten (0°, 90°, 180°, 270°) messen
4. Min. Wandstärke: 3 mm (NW ≤38 mm), 4 mm (NW >38 mm) — ISO 9093-1
5. **Bewertung**: <Min. → Austausch empfohlen

#### K-4: Dichtigkeitsprüfung

1. Boot zu Wasser lassen
2. Alle Borddurchlässe unter WL 30 min beobachten
3. Keine Tropfbildung: OK
4. Tropfbildung: Lokalisieren, Tropfrate messen
5. **Bewertung**: <1 ml/h akzeptabel (Kondensation möglich), >1 ml/h → Nachbesserung

#### K-5: Bonding-Prüfung

1. Multimeter auf Widerstandsmessung (Ω)
2. Zwischen Borddurchlass-Fitting und Bonding-Bus messen
3. **Akzeptabel**: <1 Ω
4. **Grenzwertig**: 1–5 Ω → Verbindung reinigen
5. **Nicht akzeptabel**: >5 Ω → Kabel/Klemme erneuern

(Confidence: documented)

### ANHANG L — Top 15 Fehler bei Borddurchlass-Installation

| Nr. | Fehler | Konsequenz | Vermeidung |
|---|---|---|---|
| L-01 | Messing statt Bronze verwendet | Entzinkung, Bruchgefahr | Material-Zertifikat prüfen, Magnet-Test (Messing ist nicht-magnetisch wie Bronze — visuell prüfen) |
| L-02 | Silikon als Dichtstoff unter WL | Ablösung, Leckage | Polysulfid oder PU verwenden |
| L-03 | BSP auf NPT geschraubt | Undichtigkeit | Gewindetyp vor Kauf prüfen |
| L-04 | Sandwich-Kern nicht entfernt | Lockerer Durchlass, Kernschaden | Kern entfernen, mit Epoxid füllen |
| L-05 | Keine Backing-Plate | Rumpf-Deformation, Leckage | Min. 3× NW Ø, 6–10 mm |
| L-06 | Gate-Valve statt Kugelhahn | Festsetzen, keine Notfall-Schließung | Kugelhahn oder Kükenventil |
| L-07 | Einfache Schlauchschelle unter WL | Schlauchabrutschen, Wassereinbruch | Doppelte Schlauchschellen, 316L |
| L-08 | Bronze in Aluminium-Rumpf | Galvanische Korrosion am Rumpf | Marelon/TruDesign/Titan |
| L-09 | Scoop-Strainer ohne Antifouling | Bewuchsverblockung | Antifouling auf Scoop auftragen |
| L-10 | Seeventil unter WL vergessen | ABYC/ISO-Verstoß, Sicherheitsrisiko | Alle Durchlässe unter WL mit Seeventil |
| L-11 | Gegenmutter zu stark angezogen | Riss im Rumpf oder Fitting | Handfest + 1/4 Umdrehung |
| L-12 | Kein Primer bei PU-Dichtstoff | Schlechte Haftung | Sika Primer-209D verwenden |
| L-13 | Notholzstopfen fehlen | Keine Notfall-Abdichtung möglich | Für jeden Durchlass unter WL bereitstellen |
| L-14 | Borddurchlass nicht im Bonding | Unkontrollierte Korrosion | 6 mm² Kabel an Bonding-Bus |
| L-15 | Seeventil hinter Schrank verbaut | Nicht bedienbar im Notfall | Inspektionsluke einbauen |

(Confidence: documented)

### ANHANG M — Zusammenfassung der Bewertungs-Scores

#### AYDI-Score-Zuordnung für Borddurchlass-Bewertung

| Score-Bereich | Zustand | Maßnahme | Farbe |
|---|---|---|---|
| 90–100 | Ausgezeichnet | Keine Maßnahme nötig | Grün |
| 75–89 | Gut | Überwachung | Grün |
| 60–74 | Befriedigend | Wartung bei nächstem Haulout | Gelb |
| 40–59 | Ausreichend | Reparatur/Erneuerung planen | Orange |
| 20–39 | Mangelhaft | Dringende Erneuerung | Rot |
| 0–19 | Kritisch | Sofortige Maßnahme, Boot nicht zu Wasser | Dunkelrot |

#### Score-Berechnung (gewichtet)

```python
def calculate_through_hull_score(
    material_score: float,      # 0–100
    installation_score: float,  # 0–100
    seacock_score: float,       # 0–100
    bedding_score: float,       # 0–100
    backing_score: float,       # 0–100
    hose_connection_score: float, # 0–100
    corrosion_score: float      # 0–100
) -> float:
    """Gewichtete Gesamtbewertung eines Borddurchlasses."""
    weights = {
        "material": 0.25,
        "installation": 0.10,
        "seacock": 0.20,
        "bedding": 0.15,
        "backing": 0.10,
        "hose_connection": 0.10,
        "corrosion": 0.10
    }
    score = (
        material_score * weights["material"]
        + installation_score * weights["installation"]
        + seacock_score * weights["seacock"]
        + bedding_score * weights["bedding"]
        + backing_score * weights["backing"]
        + hose_connection_score * weights["hose_connection"]
        + corrosion_score * weights["corrosion"]
    )
    return round(score, 1)
```

(Confidence: documented)

### ANHANG N — Spezialanwendungen

#### N-1: Borddurchlässe für Stabilisatoren

Stabilisatoren (Flossen oder Gyro mit Hydraulik) benötigen Kühlwasserdurchlässe:

| Parameter | Spezifikation |
|---|---|
| NW | 19–32 mm je nach System |
| Material | Bronze oder Marelon |
| Position | Mittschiffs, unter WL |
| Seeventil | Pflicht |
| Besonderheit | Separater Kreislauf, nicht mit Motor-Kühlwasser kombinieren |

#### N-2: Borddurchlässe für Feuerlöschsysteme

| Parameter | Spezifikation |
|---|---|
| NW | 38–76 mm (abhängig von Pumpenleistung) |
| Material | Bronze C83600 (Pflicht — SOLAS-konform) |
| Position | Unter WL, mittschiffs |
| Seeventil | Pflicht, Notfall-Öffnung (normalerweise offen) |
| Norm | SOLAS, Lloyd's Register |

#### N-3: Borddurchlässe für Bug-/Heckstrahler

| Parameter | Spezifikation |
|---|---|
| NW | 19–25 mm (Hydraulik-Kühlung) |
| Material | Bronze oder Marelon |
| Position | Bug (Bugstrahlruder), Heck (Heckstrahler) |
| Seeventil | Pflicht |

#### N-4: Borddurchlässe für Ballastsysteme (Racing)

| Parameter | Spezifikation |
|---|---|
| NW | 50–76 mm (schnelles Fluten/Lenzen) |
| Material | Marelon (Gewichtsoptimierung) |
| Position | Beidseitig, unter WL |
| Seeventil | Pflicht, schnell schaltbar |
| Besonderheit | Hoher Durchfluss erforderlich, kurze Leitungswege |

(Confidence: documented)

### ANHANG O — Umweltaspekte

#### O-1: MARPOL Annex IV (Abwasser)

| Regelung | Anforderung |
|---|---|
| Direkteinleitung | Verboten in Küstengewässern (<12 nm) vieler Länder |
| Fäkalientank | Pflicht bei Neubauten ab 2008 (EU) |
| Borddurchlass-Relevanz | Y-Ventil zwischen Tank und Seeauslass muss in Küstennähe auf "Tank" stehen |
| Kontrolle | Seeventil für Direkteinleitung in manchen Häfen versiegelt |

#### O-2: Antifouling auf Borddurchlässen

| Aspekt | Regelung |
|---|---|
| TBT (Tributylzinn) | Weltweit verboten (IMO AFS Convention 2008) |
| Kupfer-basiert | In EU erlaubt, in einigen Süßwasser-Regionen eingeschränkt |
| Borddurchlass-Scoop | Antifouling empfohlen, aber nicht in Wasseraufnahme-Pfad (Watermaker!) |

#### O-3: Entsorgung alter Borddurchlässe

| Material | Entsorgung |
|---|---|
| Bronze | Metallschrott (recycelbar, guter Schrottwert ~5 EUR/kg) |
| 316L | Metallschrott (recycelbar) |
| Marelon/Kunststoff | Restmüll oder Kunststoff-Recycling (je nach Kommune) |
| Alte Dichtstoffe | Sondermüll (Polysulfid, PU) |

(Confidence: documented)

### ANHANG P — Erweiterte FAQ

#### BD-P01: Kann ich einen Borddurchlass unter Wasser abdichten?
Provisorisch ja: Unterwasser-Epoxid (JB Water Weld, Belzona 1111) kann eine temporäre Abdichtung schaffen. Für dauerhafte Reparatur muss das Boot an Land. Unterwasser-Reparaturen halten typisch Tage bis Wochen, nicht Monate.

#### BD-P02: Wie finde ich heraus, ob mein Durchlass BSP oder NPT hat?
BSP-Gewinde ist zylindrisch (gleicher Durchmesser über die gesamte Länge). NPT ist konisch (wird zur Spitze hin dünner). Messmethode: Gewinde-Lehre verwenden, oder Durchmesser an zwei Stellen messen — bei NPT unterschiedlich.

#### BD-P03: Gibt es einen Standard für die Farbe der Seeventil-Hebel?
Kein verbindlicher Standard. Empfehlung: Rot = Geschlossen, markiert mit "ZU/CLOSED". Viele Hersteller liefern Seeventile mit rotem Hebel. Wichtig: Hebel parallel zum Schlauch = OFFEN, quer = GESCHLOSSEN.

#### BD-P04: Wie oft muss ein Borddurchlass-Plan aktualisiert werden?
Nach jedem Einbau, Austausch oder jeder Veränderung. Der Borddurchlass-Plan muss die aktuelle Konfiguration widerspiegeln und im Eignerhandbuch hinterlegt sein (CE-Pflicht).

#### BD-P05: Sind Borddurchlässe versichert?
Ja, Schäden durch defekte Borddurchlässe sind in der Kaskoversicherung (Vollkasko) abgedeckt. Voraussetzung: Ordnungsgemäße Wartung. Grobe Vernachlässigung (z.B. 20 Jahre keine Inspektion) kann zur Leistungsverweigerung führen.

#### BD-P06: Wie prüfe ich, ob mein Bronze echt ist?
1. Farbe: Bronze ist rötlich-braun, Messing ist gelb-golden.
2. Magnet: Beide sind nicht-magnetisch — kein Unterschied.
3. Kratztest: Bronze kratzt leicht mit Gold-Braun-Ton.
4. Sicherste Methode: XRF-Analyse (Röntgenfluoreszenz) — zeigt exakte Zusammensetzung. Kosten: ~50 EUR.

#### BD-P07: Kann ich einen 3D-Scan meines Rumpfes für die Borddurchlass-Planung nutzen?
Ja, empfohlen für Neubauten und größere Umbauten. 3D-Scan (Photogrammetrie oder Laserscanner) liefert exakte Rumpfgeometrie einschließlich Rumpfwinkel an den geplanten Einbaustellen. Kosten: 500–2.000 EUR für einen kompletten Rumpf-Scan.

#### BD-P08: Was ist ein "Dezincification Resistant" (DZR) Material?
DZR-Materialien (z.B. CW602N, CZ132) sind spezielle Messing-Legierungen mit Zusätzen (Arsen, Antimon), die die Entzinkung verhindern. Sie sind besser als normales Messing, aber immer noch schlechter als Bronze (C83600 hat nur 5 % Zink und braucht keinen DZR-Schutz).

#### BD-P09: Mein Borddurchlass hat einen grünen Belag — ist das schlimm?
Grünspan (Kupfercarbonat/Kupferchlorid) auf Bronze ist eine natürliche Patina und in der Regel **nicht schädlich**. Er bildet sogar eine leicht schützende Schicht. Unterscheiden von Entzinkung: Grünspan ist oberflächlich und lässt sich abwischen/polieren, Entzinkung geht in die Tiefe.

#### BD-P10: Wie kann AYDI den Zustand meiner Borddurchlässe aus Fotos bewerten?
AYDI analysiert Fotos mit Claude Vision auf: 1) Material-Identifikation (Bronze/Edelstahl/Kunststoff), 2) Korrosionsanzeichen (Verfärbung, Ablagerungen), 3) Dichtstoff-Zustand (Risse, Ablösung), 4) Seeventil-Typ und -Position, 5) Schlauchverbindungen. Confidence: visual_high bei klaren Nahaufnahmen, visual_medium bei Übersichtsfotos.

(Confidence: documented)

### ANHANG Q — Zeitleiste: Entwicklung der Borddurchlass-Technologie

| Jahr | Meilenstein |
|---|---|
| ~3000 v.Chr. | Erste Bronzeguss-Beschläge im Schiffbau (Ägypten, Phönizien) |
| ~1700 | Standardisierung von Bronze-Armaturen für Kriegsschiffe (Royal Navy) |
| 1841 | Joseph Whitworth standardisiert BSP-Gewinde |
| 1864 | William Sellers standardisiert NPT-Gewinde (USA) |
| 1926 | Gründung Groco (Gross Mechanical Laboratories) |
| 1965 | Erste Kunststoff-Borddurchlässe (Nylon) auf dem Markt |
| 1978 | Forespar entwickelt Marelon (glasfaserverstärktes PA66) |
| 1994 | ISO 9093-1 erste Ausgabe (metallische Borddurchlässe) |
| 2000 | ISO 9093-2 erste Ausgabe (nicht-metallische Borddurchlässe) |
| 2005 | TruDesign (NZ) bringt integriertes Kunststoff-Borddurchlass-System |
| 2013 | EU Recreational Craft Directive 2013/53/EU tritt in Kraft |
| 2020 | ISO 9093-1/2 revidierte Ausgabe mit verschärften Anforderungen |
| 2023 | Erste Prototypen von IoT-Seeventilen (Fernüberwachung) |
| 2025 | Titan-Borddurchlässe für Serienfertigung in Vorbereitung |

(Confidence: documented)

### ANHANG R — Stichwortverzeichnis

| Stichwort | Abschnitt |
|---|---|
| ABYC H-27 | Einführung, FAQ BD-002/BD-016, Anhang I |
| Abgas-Durchführung | Grundlagen 7.1.7, Anlagenzuordnung 9.2 |
| Aluminium-Rumpf | Grundlagen 7.10.2, FAQ BD-003, Anhang L |
| Anti-Siphon-Ventil | Anlagenzuordnung 9.3 |
| Backing-Plate | Grundlagen 7.8, Verbindungstechnik 10.2, Fehlerbild FB-04 |
| Bewuchs | Fehlerbild FB-09, Best Practices |
| Bonding-System | Grundlagen 7.10.3, FAQ BD-018, Anhang K |
| Bronze C83600 | Grundlagen 7.2.1, Anhang B, J |
| BSP/NPT | Grundlagen 7.3, Fehlerbild FB-07, FAQ BD-008 |
| CE/RCD | Einführung, FAQ BD-010 |
| Cockpit-Drain | Grundlagen 7.1.8, Anlagenzuordnung 9.10, Berechnung 11.4 |
| Dichtstoff | Grundlagen 7.9, Verbindungstechnik 10.3, Fehlerbild FB-03/FB-11 |
| Durchfluss | Berechnung 11.1, Anhang C |
| Elektrolyse | Fehlerbild FB-05, Fallstudie F-02 |
| Entzinkung | Lebensdauer 13.2.1, Fehlerbild FB-01, Fallstudie F-01 |
| Flush-Mount | Grundlagen 7.1.2 |
| Galvanische Korrosion | Grundlagen 7.10, Berechnung 11.5, Fehlerbild FB-05 |
| Gate-Valve | Fehlerbild FB-06, FAQ BD-015 |
| Geber-Durchführung | Grundlagen 7.5, Anlagenzuordnung 9.9 |
| Groco | Hersteller 8 (TH/STH/SC/BV-Serie) |
| Guidi | Hersteller 8 (1210/1160-Serie) |
| ISO 9093 | Einführung, Anhang I |
| Kernverstärkung | Grundlagen 7.8.2, Fehlerbild FB-04 |
| Klimaanlage | Anlagenzuordnung 9.6 |
| Lochfraß | Lebensdauer 13.2.3 |
| Lloyd's Register | Einführung |
| Marelon | Grundlagen 7.2.3, Hersteller 8 (Forespar), FAQ BD-005 |
| Material-Wahl | Grundlagen 7.2.4, Schnell-Referenz |
| Motor-Kühlwasser | Anlagenzuordnung 9.1, Fehlerbild FB-09 |
| Notholzstopfen | FAQ BD-010/BD-021, Notfall-Ressourcen |
| Pydantic-Modelle | Abschnitt 6 |
| Sandwich-Bauweise | Grundlagen 7.8.2, Fehlerbild FB-04, Fallstudie F-05 |
| Scoop-Strainer | Grundlagen 7.7, Fehlerbild FB-09, FAQ BD-013 |
| Seeventil | FAQ BD-001/BD-002/BD-015, Einbau 12.3 |
| Silikon | Grundlagen 7.9.2, Fehlerbild FB-11 |
| Spaltkorrosion | Lebensdauer 13.2.2, Fehlerbild FB-02 |
| 316L Edelstahl | Grundlagen 7.2.2, FAQ BD-011, Anhang J |
| Toilette | Anlagenzuordnung 9.4/9.5, FAQ BD-022 |
| TruDesign | Hersteller 8 (90400/90600-Serie), FAQ BD-025 |
| Vetus | Hersteller 8 (TRC-Serie) |
| Wassereintritt | Berechnung 11.3, FAQ BD-021 |
| Watermaker | Anlagenzuordnung 9.8 |

---

### ANHANG R.1 — Erweiterte Herstellerinformationen

#### R.1.1 Groco — Erweiterte Produktdaten

**FTH-Serie — Flanged Through-Hull (Bronze, Superyacht)**

| Modell | NW Zoll | Flansch-Ø mm | Schrauben | Material | Preis EUR |
|---|---|---|---|---|---|
| FTH-1500 | 1-1/2" | 95 | 4× M8 | Bronze C83600 | 185 |
| FTH-2000 | 2" | 115 | 4× M8 | Bronze C83600 | 245 |
| FTH-2500 | 2-1/2" | 140 | 6× M8 | Bronze C83600 | 325 |
| FTH-3000 | 3" | 165 | 6× M10 | Bronze C83600 | 420 |

**ARG-Serie — Raw Water Strainers (Seewasserfilter)**

| Modell | NW Zoll | Filtervolumen ml | Maschenweite mm | Material | Preis EUR |
|---|---|---|---|---|---|
| ARG-500 | 1/2" | 120 | 1,5 | Bronze + Edelstahl-Sieb | 95 |
| ARG-750 | 3/4" | 250 | 1,5 | Bronze + Edelstahl-Sieb | 125 |
| ARG-1000 | 1" | 500 | 2,0 | Bronze + Edelstahl-Sieb | 165 |
| ARG-1250 | 1-1/4" | 750 | 2,0 | Bronze + Edelstahl-Sieb | 195 |
| ARG-1500 | 1-1/2" | 1.200 | 2,5 | Bronze + Edelstahl-Sieb | 245 |
| ARG-2000 | 2" | 2.000 | 3,0 | Bronze + Edelstahl-Sieb | 310 |

(Confidence: documented)

#### R.1.2 TruDesign — Systemkomponenten im Detail

**90500-Serie — Hose Tails (Schlauchtüllen)**

| Modell | NW Zoll | Schlauchanschluss mm | Material | Preis EUR |
|---|---|---|---|---|
| 90501 | 1/2" | 13 | PA66-GF30 | 8 |
| 90502 | 3/4" | 19 | PA66-GF30 | 10 |
| 90503 | 1" | 25 | PA66-GF30 | 12 |
| 90504 | 1-1/4" | 32 | PA66-GF30 | 15 |
| 90505 | 1-1/2" | 38 | PA66-GF30 | 18 |
| 90506 | 2" | 50 | PA66-GF30 | 22 |

**90700-Serie — Lock Nuts (Gegenmuttern)**

| Modell | NW Zoll | Material | Preis EUR |
|---|---|---|---|
| 90701 | 1/2" | PA66-GF30 | 5 |
| 90702 | 3/4" | PA66-GF30 | 6 |
| 90703 | 1" | PA66-GF30 | 7 |
| 90704 | 1-1/4" | PA66-GF30 | 8 |
| 90705 | 1-1/2" | PA66-GF30 | 9 |
| 90706 | 2" | PA66-GF30 | 11 |

**TruDesign Komplett-System Preise (Fitting + Seeventil + Tülle + Mutter)**

| NW Zoll | Einzelteile EUR | Komplett-Set EUR | Ersparnis |
|---|---|---|---|
| 3/4" | 18+52+10+6 = 86 | 78 | 9 % |
| 1" | 22+65+12+7 = 106 | 95 | 10 % |
| 1-1/4" | 28+82+15+8 = 133 | 118 | 11 % |
| 1-1/2" | 35+105+18+9 = 167 | 148 | 11 % |
| 2" | 48+135+22+11 = 216 | 192 | 11 % |

(Confidence: documented)

#### R.1.3 Vetus — Erweiterte Produktdaten

**Vetus Kunststoff-Borddurchlässe (Delrin/POM)**

| Modell | NW Zoll | Material | Einsatz | Preis EUR |
|---|---|---|---|---|
| HTP1320 | 1/2" | POM (Delrin) | Nur über WL | 8 |
| HTP1920 | 3/4" | POM (Delrin) | Nur über WL | 10 |
| HTP2520 | 1" | POM (Delrin) | Nur über WL | 13 |
| HTP3220 | 1-1/4" | POM (Delrin) | Nur über WL | 16 |

**Warnung**: Vetus Delrin/POM-Durchlässe sind **ausschließlich über der Wasserlinie** zugelassen. Sie sind nicht ISO 9093-2 konform für Unterwasser-Einsatz.

**Vetus Seewasserfilter (FTR-Serie)**

| Modell | NW Zoll | Filtervolumen ml | Sichtglas | Material | Preis EUR |
|---|---|---|---|---|---|
| FTR330/19 | 3/4" | 330 | Ja | Bronze/Kunststoff | 85 |
| FTR330/25 | 1" | 330 | Ja | Bronze/Kunststoff | 95 |
| FTR525/25 | 1" | 525 | Ja | Bronze/Kunststoff | 115 |
| FTR525/32 | 1-1/4" | 525 | Ja | Bronze/Kunststoff | 125 |
| FTR1320/38 | 1-1/2" | 1.320 | Ja | Bronze/Kunststoff | 165 |
| FTR1320/50 | 2" | 1.320 | Ja | Bronze/Kunststoff | 195 |

(Confidence: documented)

### ANHANG R.2 — Erweiterte Berechnungen

#### R.2.1 Krängungseinfluss auf Borddurchlass-Position

Bei Segelbooten unter Krängung können Borddurchlässe, die in aufrechter Position über der Wasserlinie liegen, unter Wasser geraten. Die Eintauchberechnung:

```
Höhe des Durchlasses über WL bei Krängung:

h_eff = h_0 × cos(θ) - d × sin(θ)

h_eff = effektive Höhe über WL [mm]
h_0 = Höhe über WL in aufrechter Position [mm]
d = Horizontalabstand zur Mittschiffslinie [mm]
θ = Krängungswinkel [°]

Eintauchen wenn h_eff < 0
```

| h_0 [mm] | d [mm] | 10° Krängung | 15° Krängung | 20° Krängung | 25° Krängung |
|---|---|---|---|---|---|
| 200 | 1.500 | -63 mm (unter WL!) | -195 mm | -320 mm | -441 mm |
| 200 | 1.000 | +24 mm | -65 mm | -149 mm | -242 mm |
| 300 | 1.500 | +36 mm | -97 mm | -225 mm | -349 mm |
| 300 | 1.000 | +122 mm | +32 mm | -55 mm | -150 mm |
| 500 | 1.500 | +233 mm | +96 mm | -30 mm | -158 mm |
| 500 | 1.000 | +319 mm | +224 mm | +137 mm | +42 mm |

**Konsequenz**: Bei 15° Krängung und 1.500 mm Abstand zur Mittellinie muss ein Borddurchlass mindestens 400 mm über WL liegen, um trocken zu bleiben. Alle tiefer liegenden Durchlässe auf der Leeseite benötigen ein Seeventil.

(Confidence: calculated)

#### R.2.2 Ermüdungsanalyse von Borddurchlässen

Borddurchlässe sind zyklischen Belastungen ausgesetzt (Wellenschlag, Vibration, Temperaturwechsel):

| Belastungsart | Zyklen pro Jahr | Amplitude |
|---|---|---|
| Wellenschlag (Fahrt) | ~500.000 | ±0,5 kPa |
| Motor-Vibration | ~50.000.000 | ±0,01 mm |
| Temperaturwechsel (Sommer/Winter) | ~365 | ΔT ±30 °C |
| Thermozyklus (Motor an/aus) | ~1.000 | ΔT ±60 °C |

| Material | Dauerfestigkeit [MPa] | Geschätzte Zyklen bis Versagen | Empf. Austausch-Intervall |
|---|---|---|---|
| Bronze C83600 | 85 | >10⁹ (praktisch unendlich) | Korrosions-abhängig, nicht Ermüdung |
| 316L | 190 | >10⁹ | Korrosions-abhängig |
| Marelon (PA66-GF30) | 30 | ~10⁷ (10 Mio.) | 15–25 Jahre (UV/Ermüdung) |
| Nylon (PA6) | 15 | ~10⁶ (1 Mio.) | 5–10 Jahre |

(Confidence: calculated)

#### R.2.3 Wärmeausdehnung und Spaltbildung

Unterschiedliche Wärmeausdehnung von Fitting und Rumpf kann Spalte erzeugen:

| Material-Paarung | α₁ [10⁻⁶/K] | α₂ [10⁻⁶/K] | Δα | Spalt bei ΔT=40°C, d=25mm |
|---|---|---|---|---|
| Bronze in GFK | 18 | 25 | 7 | 0,007 mm |
| 316L in GFK | 16 | 25 | 9 | 0,009 mm |
| Marelon in GFK | 30 | 25 | 5 | 0,005 mm |
| Bronze in Aluminium | 18 | 24 | 6 | 0,006 mm |
| Marelon in Aluminium | 30 | 24 | 6 | 0,006 mm |

**Fazit**: Die Spaltbildung durch Wärmeausdehnung ist bei allen Material-Kombinationen minimal (<0,01 mm). Der Dichtstoff muss diese Bewegung aber aufnehmen können — daher elastische Dichtstoffe (Polysulfid, PU) statt starre (Epoxid).

(Confidence: calculated)

### ANHANG R.3 — OEM-Spezifikationen nach Bootshersteller

#### R.3.1 Beneteau / Groupe Beneteau

| Modell-Reihe | Standard-Durchlass | Standard-Seeventil | Gewinde | Besonderheit |
|---|---|---|---|---|
| Oceanis 30.1–34.1 | TruDesign 90400 | TruDesign 90600 | BSP | Komplett Kunststoff ab 2019 |
| Oceanis 37.1–46.1 | TruDesign 90400 | TruDesign 90600 | BSP | Komplett Kunststoff ab 2019 |
| First 27–36 | TruDesign 90400 | TruDesign 90600 | BSP | Komplett Kunststoff |
| Oceanis Yacht 54–60 | Guidi 1210 Bronze | Guidi 1160 Bronze | BSP | Bronze unter WL |
| Gran Turismo 32–45 | TruDesign 90400 | TruDesign 90600 | BSP | Kunststoff Standard |

(Confidence: benchmark)

#### R.3.2 Bavaria Yachtbau

| Modell-Reihe | Standard-Durchlass | Standard-Seeventil | Gewinde | Besonderheit |
|---|---|---|---|---|
| Cruiser 34–46 | Guidi 1210 Bronze | Guidi 1160 Bronze | BSP | Bronze Standard |
| C-Line 42–50 | Guidi 1210 Bronze | Guidi 1160 Bronze | BSP | Bronze Standard |
| SR-Line (Motor) | TruDesign 90400 | TruDesign 90600 | BSP | Kunststoff ab 2021 |
| Vision 42–46 | Guidi 1210 Bronze | Guidi 1160 Bronze | BSP | Bronze Standard |

(Confidence: benchmark)

#### R.3.3 Hallberg-Rassy

| Modell-Reihe | Standard-Durchlass | Standard-Seeventil | Gewinde | Besonderheit |
|---|---|---|---|---|
| HR 340–372 | Bronze C83600 | Bronze Kugelhahn | BSP | Eigenproduktion/Guidi, Premium |
| HR 40C–44 | Bronze C83600 | Bronze Kugelhahn | BSP | Alle Seeventile zugänglich |
| HR 48–64 | Bronze C92200 | Bronze C92200 Kugelhahn | BSP | Navy-Bronze, Premium |
| HR 57–69 | Bronze C92200 | Bronze C92200 Kugelhahn | BSP | Navy-Bronze, doppelt gesichert |

(Confidence: benchmark)

#### R.3.4 Jeanneau

| Modell-Reihe | Standard-Durchlass | Standard-Seeventil | Gewinde |
|---|---|---|---|
| Sun Odyssey 319–410 | TruDesign 90400 | TruDesign 90600 | BSP |
| Sun Odyssey 440–490 | TruDesign + Guidi (Abgas) | TruDesign/Guidi | BSP |
| Yachts 55–60 | Guidi Bronze | Guidi Bronze | BSP |
| Merry Fisher (Motor) | TruDesign 90400 | TruDesign 90600 | BSP |

(Confidence: benchmark)

#### R.3.5 Hanse Yachts

| Modell-Reihe | Standard-Durchlass | Standard-Seeventil | Gewinde |
|---|---|---|---|
| Hanse 315–388 | TruDesign 90400 | TruDesign 90600 | BSP |
| Hanse 418–548 | TruDesign + Bronze (Abgas) | TruDesign/Bronze | BSP |
| Hanse 675 | Guidi Bronze | Guidi Bronze | BSP |
| Moody DS41–54 | Guidi Bronze | Guidi Bronze | BSP |

(Confidence: benchmark)

### ANHANG R.4 — Visuelle Analyse: Referenz-Merkmale für Claude Vision

#### R.4.1 Material-Identifikation aus Fotos

| Material | Visuelle Merkmale | Confidence |
|---|---|---|
| Bronze (neu) | Rötlich-goldene Farbe, metallischer Glanz, gussraue Oberfläche | visual_high |
| Bronze (patiniert) | Dunkelbraun bis grünlich (Patina), matte Oberfläche | visual_high |
| Bronze (entzinkt) | Rosa-kupferfarben, porös, kein Glanz | visual_high |
| Edelstahl 316L | Silbrig-glänzend, glatte Oberfläche | visual_high |
| Edelstahl (korrodiert) | Braune Flecken, Rost-ähnlich an Spalten | visual_high |
| Marelon (weiß) | Weißer Kunststoff, leicht glänzend, glatte Oberfläche | visual_high |
| Marelon (gealtert) | Gelblich verfärbt, mattere Oberfläche | visual_medium |
| TruDesign (weiß) | Identisch zu Marelon visuell, Branding "TruDesign" am Fitting | visual_medium |
| Nylon | Hellgrauer oder weißer Kunststoff, glatte Oberfläche, leicht transparent | visual_medium |
| Messing | Gelb-golden (heller als Bronze), glatte Oberfläche | visual_medium |

(Confidence: documented)

#### R.4.2 Seeventil-Typ-Identifikation

| Typ | Visuelle Merkmale | Confidence |
|---|---|---|
| Kugelhahn | Hebelgriff (1/4 Drehung), kompakter Körper | visual_high |
| Kükenventil | Konischer Körper, T-Griff oder Hebel | visual_medium |
| Gate-Valve (Schieber) | Handrad (Drehrad), hoher zylindrischer Körper | visual_high |
| Kein Seeventil | Nur Schlauchtülle direkt am Fitting | visual_high |

(Confidence: documented)

#### R.4.3 Zustandsbewertung aus Fotos

| Zustand | Visuelle Indikatoren | Score-Zuordnung |
|---|---|---|
| Neuwertig | Gleichmäßige Farbe, keine Ablagerungen, Dichtstoff intakt | 90–100 |
| Leichte Patina | Natürliche Verfärbung, keine Korrosion | 75–89 |
| Kalkablagerungen | Weiße Ablagerungen am Fitting oder Seeventil | 60–74 |
| Dichtstoff gerissen | Sichtbare Risse im Dichtstoff-Ring | 40–59 |
| Korrosion sichtbar | Braune/grüne Verfärbungen, Lochfraß | 20–39 |
| Schwere Korrosion | Materialabtrag sichtbar, poröse Oberfläche | 0–19 |
| Entzinkung | Rosa-kupferfarbene, schwammige Oberfläche | 0 (sofort) |

(Confidence: documented)

### ANHANG R.5 — Wartungskalender-Template

#### Jährlicher Wartungskalender für Borddurchlässe

| Monat | Maßnahme | Geltung |
|---|---|---|
| Vor Saison (Frühjahr) | Alle Seeventile betätigen, Funktion prüfen | Alle Boote |
| Vor Saison | Scoop-Strainer reinigen (vor dem Slippen) | Alle mit Scoop |
| Monatlich (Saison) | Seewasserfilter prüfen/reinigen | Motor-/AC-Betrieb |
| Monatlich (Tropen) | Scoop-Strainer von Taucher reinigen lassen | Tropen/Mittelmeer |
| Vierteljährlich | Bilge auf Wasseransammlung an Durchlässen prüfen | Alle Boote |
| Haulout (Herbst) | Vollinspektion aller Borddurchlässe | Alle Boote |
| Haulout | Zinkanoden prüfen, ggf. ersetzen | Metallische Fittings |
| Haulout | Antifouling auf Scoop-Strainer und Flush-Fittings | Alle mit Scoop/Flush |
| Haulout | Schlauchschellen nachziehen | Alle Schlauchverbindungen |
| Haulout | Bonding-Verbindungen prüfen | Metallische Fittings |
| Winterlager | Seeventile in Offen-Position belassen | Alle Boote |
| Winterlager | Frostschutz in alle wasserführenden Leitungen | Frostgefährdete Reviere |
| Alle 5 Jahre | Dichtstoff visuell prüfen, ggf. erneuern | Alle Durchlässe |
| Alle 10 Jahre | Professionelle Inspektion (Surveyor) | Alle Boote |
| Alle 15–20 Jahre | Austausch prüfen lassen (materialabhängig) | Besonders Kunststoff |

(Confidence: benchmark)

### ANHANG R.6 — Kostenübersicht: Borddurchlass-Systeme komplett

#### Kosten für kompletten Austausch aller Borddurchlässe nach Bootsgröße

| Bootsklasse | Anzahl BD | Material (Bronze) EUR | Material (TruDesign) EUR | Werft-Arbeit EUR | Gesamt Bronze EUR | Gesamt TruDesign EUR |
|---|---|---|---|---|---|---|
| Segelboot 8–10 m | 8 | 800–1.200 | 400–600 | 1.200–2.000 | 2.000–3.200 | 1.600–2.600 |
| Segelboot 10–14 m | 13 | 1.400–2.000 | 700–1.000 | 2.000–3.500 | 3.400–5.500 | 2.700–4.500 |
| Segelboot 14–18 m | 21 | 2.500–3.500 | 1.200–1.800 | 3.500–6.000 | 6.000–9.500 | 4.700–7.800 |
| Motoryacht 10–15 m | 20 | 2.200–3.200 | 1.100–1.600 | 3.000–5.000 | 5.200–8.200 | 4.100–6.600 |
| Superyacht 20–30 m | 45 | 6.000–10.000 | 3.000–5.000 | 8.000–15.000 | 14.000–25.000 | 11.000–20.000 |

**Hinweis**: Preise inkl. Borddurchlass, Seeventil, Dichtstoff, Schlauchschellen, Backing-Plates. Exkl. Schläuche, Seewasserfilter, Bonding-Kabel.

(Confidence: benchmark)

#### Einzelkosten-Aufschlüsselung (3/4" Borddurchlass unter WL)

| Position | Bronze EUR | TruDesign EUR | Marelon EUR |
|---|---|---|---|
| Borddurchlass (Fitting) | 35–55 | 18–25 | 16–22 |
| Seeventil (Kugelhahn) | 75–125 | 52–65 | 48–62 |
| Schlauchtülle | 12–18 | 10–12 | 10–14 |
| Gegenmutter | 8–12 | 6–8 | 5–8 |
| Backing-Plate (G10) | 8–15 | 8–15 | 8–15 |
| Dichtstoff (Anteil) | 5–8 | 5–8 | 5–8 |
| Schlauchschellen (2×) | 5–10 | 5–10 | 5–10 |
| PTFE-Band | 2 | 2 | 2 |
| Notholzstopfen | 3–5 | 3–5 | 3–5 |
| **Material gesamt** | **153–250** | **109–150** | **102–146** |
| Werft-Arbeit (1,5–2,5 h) | 112–300 | 112–300 | 112–300 |
| **Gesamt installiert** | **265–550** | **221–450** | **214–446** |

(Confidence: benchmark)

### ANHANG R.7 — Versicherungs- und Survey-Anforderungen

#### R.7.1 Survey-Anforderungen nach Versicherer

| Versicherer | Anforderung an Borddurchlässe | Intervall |
|---|---|---|
| Pantaenius | Alle BD unter WL bei Verkaufs-Survey inspizieren | Bei Verkauf |
| Pantaenius | Kratztest bei Bronze-Fittings >15 Jahre | Alle 5 Jahre |
| Allianz Marine | Borddurchlass-Plan im Eignerhandbuch | Bei Versicherungsabschluss |
| Allianz Marine | Seeventile funktionsfähig | Jährlich (Selbstauskunft) |
| Yacht Pool | Borddurchlässe in Survey-Bericht | Bei Wechsel, >20 Jahre Alter |
| Lloyd's Register | Material-Zertifikate (EN 10204, 3.1) | Bei Indienststellung |
| Lloyd's Register | Jährliche Inspektion durch zugelassenen Surveyor | Jährlich |
| RINA | Borddurchlass-Zustand dokumentiert | Bei Klasse-Erneuerung |

(Confidence: documented)

#### R.7.2 Häufigste Ablehnungsgründe bei Surveys

| Nr. | Ablehnungsgrund | Häufigkeit | Typische Kosten der Nachbesserung |
|---|---|---|---|
| 1 | Gate-Valve (Schieber) statt Kugelhahn | 15 % | 200–400 EUR pro Ventil |
| 2 | Fehlende Seeventile unter WL | 12 % | 300–600 EUR pro Durchlass |
| 3 | Entzinkung an Messing-Fittings | 10 % | 300–500 EUR pro Fitting |
| 4 | Nicht zugängliche Seeventile | 8 % | 150–300 EUR (Inspektionsluke) |
| 5 | Fehlende Notholzstopfen | 7 % | 20–40 EUR |
| 6 | Einfache Schlauchschellen unter WL | 6 % | 30–60 EUR pro Durchlass |
| 7 | Silikon als Dichtstoff unter WL | 5 % | 175–400 EUR pro Durchlass |
| 8 | Korrodierte Schlauchschellen | 4 % | 20–40 EUR pro Paar |
| 9 | Fehlender Borddurchlass-Plan | 3 % | 50–100 EUR (Erstellung) |
| 10 | Defekte Bonding-Verbindungen | 3 % | 100–300 EUR |

(Confidence: benchmark)

#### R.7.3 Versicherungsrechtliche Konsequenzen

| Situation | Versicherungsrechtliche Folge |
|---|---|
| Borddurchlass bricht, regelmäßig gewartet | Voller Versicherungsschutz |
| Borddurchlass bricht, nie inspiziert (>10 Jahre) | Leistungskürzung wegen Vernachlässigung möglich |
| Messing statt Bronze verwendet (wissentlich) | Leistungsverweigerung möglich (Obliegenheitsverletzung) |
| Seeventil fehlte, Survey-Empfehlung ignoriert | Leistungskürzung wahrscheinlich |
| DIY-Einbau ohne Fachkenntnis, unsachgemäß | Leistungskürzung möglich |
| Borddurchlass-Bruch durch Fremdeinwirkung (Grundberührung) | Voller Versicherungsschutz |

(Confidence: documented)

### ANHANG R.8 — Digitale Dokumentation und AYDI-Integration

#### R.8.1 Borddurchlass-Plan: Digitales Format

Jedes Boot im AYDI-System sollte einen digitalen Borddurchlass-Plan führen. Mindestinhalte:

| Feld | Pflicht | Beschreibung |
|---|---|---|
| Fitting-ID | Ja | Eindeutige Kennung (BD-001, BD-002, ...) |
| Position (Zone) | Ja | AYDI-Zone (bow, midship_port, midship_stbd, stern, transom) |
| System | Ja | Funktion (raw_water_intake, exhaust, toilet_intake, ...) |
| Typ | Ja | mushroom, flush, scoop, drain, transducer, exhaust |
| Material | Ja | bronze_c83600, stainless_316l, marelon, trudesign |
| Nennweite | Ja | In mm |
| Gewindetyp | Ja | BSP oder NPT |
| Über/Unter WL | Ja | below_wl, at_wl, above_wl, transom |
| Seeventil vorhanden | Ja | Ja/Nein, Typ |
| Hersteller | Empfohlen | Name + Teilenummer |
| Einbaudatum | Empfohlen | YYYY-MM |
| Letztes Inspektionsdatum | Empfohlen | YYYY-MM |
| Foto-Referenz | Empfohlen | Dateiname oder URL |
| Zustandsbewertung | Optional | Score 0–100 |
| Notizen | Optional | Freitext |

#### R.8.2 AYDI Visual Analysis Prompts für Borddurchlässe

Beispiel-Prompt für Claude Vision bei Borddurchlass-Analyse:

```
Analysiere dieses Foto eines Borddurchlasses / Seeventils auf einem Boot.

Identifiziere:
1. Material: Bronze, Edelstahl, Kunststoff (Marelon/TruDesign), Messing, Nylon?
2. Typ: Mushroom, Flush, Scoop, Drain, Transducer?
3. Seeventil: Kugelhahn, Kükenventil, Gate-Valve, keines?
4. Zustand: Korrosion? Entzinkung? Kalkablagerungen? Dichtstoff-Risse?
5. Schlauchverbindung: Einfache oder doppelte Schlauchschellen? Material?
6. Backing-Plate: Sichtbar? Material? Angemessene Größe?
7. Notholzstopfen: Sichtbar? An Schnur befestigt?
8. Bonding-Kabel: Sichtbar? Verbunden?
9. Position: Über oder unter Wasserlinie (soweit erkennbar)?
10. Hersteller: Erkennbar (Logo, Prägung)?

Bewerte den Gesamtzustand auf einer Skala von 0–100.
Gib das Confidence-Level an: visual_high, visual_medium, visual_low, visual_insufficient.
Antworte auf Deutsch.
Bei unklaren Befunden: "nicht beurteilbar" angeben.
```

(Confidence: documented)

#### R.8.3 Automatische Risikobewertung: Algorithmus

```python
def assess_through_hull_risk(spec: ThroughHullSpec) -> dict:
    """
    Automatische Risikobewertung basierend auf Spezifikation.
    Gibt Risiko-Score und Empfehlungen zurück.
    """
    risk_score = 0
    findings = []
    recommendations = []

    # Material-Risiko
    if spec.material == ThroughHullMaterial.BRASS:
        risk_score += 40
        findings.append("Messing unter WL — Entzinkungsrisiko")
        recommendations.append("Sofort durch Bronze oder Marelon ersetzen")
    
    # Seeventil-Prüfung
    if spec.position == ThroughHullPosition.BELOW_WL:
        if spec.seacock_type == SeacockType.NONE:
            risk_score += 30
            findings.append("Kein Seeventil unter WL — Sicherheitsrisiko")
            recommendations.append("Seeventil nachrüsten (Pflicht)")
        elif spec.seacock_type == SeacockType.GATE_VALVE:
            risk_score += 20
            findings.append("Gate-Valve statt Kugelhahn — nicht normkonform")
            recommendations.append("Durch Kugelhahn ersetzen")
    
    # Backing-Plate bei Sandwich
    if spec.hull_construction in ["sandwich_pvc", "sandwich_balsa"]:
        if not spec.has_backing_plate:
            risk_score += 25
            findings.append("Keine Backing-Plate bei Sandwich-Rumpf")
            recommendations.append("Backing-Plate nachrüsten, Kern prüfen")
        if spec.core_removed is False:
            risk_score += 30
            findings.append("Sandwich-Kern nicht entfernt")
            recommendations.append("Kern entfernen und mit Epoxid füllen")
    
    # Galvanische Kompatibilität
    if spec.hull_construction == "aluminum":
        if spec.material in [
            ThroughHullMaterial.BRONZE_C83600,
            ThroughHullMaterial.BRONZE_C84400,
            ThroughHullMaterial.STAINLESS_316L
        ]:
            risk_score += 50
            findings.append("Metallischer Durchlass in Aluminium-Rumpf")
            recommendations.append("SOFORT durch Kunststoff ersetzen")
    
    # Alter prüfen
    if spec.install_date:
        from datetime import datetime
        install = datetime.strptime(spec.install_date, "%Y-%m")
        age_years = (datetime.now() - install).days / 365.25
        if age_years > 20 and spec.material in [
            ThroughHullMaterial.MARELON,
            ThroughHullMaterial.TRUDESIGN
        ]:
            risk_score += 15
            findings.append(f"Kunststoff-Durchlass {age_years:.0f} Jahre alt")
            recommendations.append("Austausch prüfen lassen")
        elif age_years > 30 and spec.material in [
            ThroughHullMaterial.BRONZE_C83600
        ]:
            risk_score += 10
            findings.append(f"Bronze-Durchlass {age_years:.0f} Jahre alt")
            recommendations.append("Kratztest auf Entzinkung durchführen")
    
    # Score normalisieren
    overall_score = max(0, 100 - risk_score)
    
    return {
        "risk_score": min(risk_score, 100),
        "overall_score": overall_score,
        "findings": findings,
        "recommendations": recommendations,
        "confidence": "estimated"  # Basierend auf Spezifikation, nicht Inspektion
    }
```

(Confidence: documented)

### ANHANG R.9 — Normen-Volltextreferenzen

| Norm | Titel | Ausgabe | Bezugsquelle | Preis EUR |
|---|---|---|---|---|
| ISO 9093-1:2020 | Small craft — Seacocks and through-hull fittings — Part 1: Metallic | 2020-07 | iso.org, beuth.de | 118 |
| ISO 9093-2:2020 | Small craft — Seacocks and through-hull fittings — Part 2: Non-metallic | 2020-07 | iso.org, beuth.de | 98 |
| ISO 12215-5:2019 | Small craft — Hull construction and scantlings — Part 5: Design pressures, stresses, scantling | 2019-05 | iso.org | 218 |
| ISO 11812:2020 | Small craft — Watertight cockpits and quick-draining cockpits | 2020-04 | iso.org | 78 |
| ISO 12216:2020 | Small craft — Windows, portlights, hatches, deadlights and doors | 2020-12 | iso.org | 98 |
| ISO 8469:2021 | Small craft — Non-fire-resistant fuel hoses | 2021-02 | iso.org | 58 |
| ABYC H-27 | Sea Cocks, Through-Hulls, Drain Plugs | 2020 | abycinc.org | 35 USD |
| ABYC E-2 | Cathodic Protection | 2020 | abycinc.org | 35 USD |
| ABYC E-11 | AC and DC Electrical Systems on Boats | 2020 | abycinc.org | 35 USD |
| EN 10204:2004 | Metallic products — Types of inspection documents | 2004 | beuth.de | 38 |

(Confidence: documented)

---

*Ende der Wissensdatei 07.02 — Borddurchlässe und Rumpfdurchführungen*
*AYDI v6 — Letzte Aktualisierung: 2026-04*
*Confidence: documented / calculated / benchmark / estimated (je nach Abschnitt)*
