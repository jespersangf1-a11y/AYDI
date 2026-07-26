---
titel: "Spinnaker und Gennaker — Leichtwindsegel"
kategorie: "Segel"
unterkategorie: "Spinnaker und Gennaker"
version: "2.0"
letzte_aktualisierung: "2026-04"
autor: "AYDI Maritime Knowledge Base"
---

# 16_04 — Spinnaker und Gennaker — Leichtwindsegel

---

## Inhaltsverzeichnis

1. [Einführung](#1-einführung)
2. [Spinnaker-Typen](#2-spinnaker-typen)
3. [Materialien und Tuchgewichte](#3-materialien-und-tuchgewichte)
4. [Konstruktion](#4-konstruktion)
5. [Trimm und Handling](#5-trimm-und-handling)
6. [Hardware](#6-hardware)
7. [Hersteller](#7-hersteller)
8. [Fehlerbild-Atlas](#8-fehlerbild-atlas)
9. [Troubleshooting](#9-troubleshooting)
10. [Sicherheit](#10-sicherheit)
11. [Kosten](#11-kosten)
12. [FAQ](#12-faq)
13. [Glossar](#13-glossar)
14. [Schnell-Referenz](#14-schnell-referenz)
15. [ANHANG A–H: Fallstudien](#15-anhang-a-h-fallstudien)
16. [ANHANG I–R: Pydantic v2 Modelle](#16-anhang-i-r-pydantic-v2-modelle)

---

## 1. Einführung

### 1.1 Bedeutung von Leichtwindsegeln

Leichtwindsegel — Spinnaker, Gennaker, Code 0 und verwandte Segeltypen — sind die leistungskritischsten
Segel an Bord einer Yacht. Während Groß- und Vorsegel den Standardbetrieb abdecken, erschließen
Leichtwindsegel den gesamten Bereich von raumem bis achterlichem Wind, der auf den meisten Revieren
40–60 % der Segelzeit ausmacht. Ohne geeignetes Vorwindsegel verliert eine typische 38-Fuß-Fahrtenyacht
auf raumen Kursen 2–4 Knoten Fahrt gegenüber ihrem Potenzial.

Die Leistungssteigerung durch Leichtwindsegel ist erheblich:

| Bedingung | Ohne Spinnaker/Gennaker | Mit Spinnaker/Gennaker | Gewinn |
|-----------|------------------------|------------------------|--------|
| 10 kn TWS, 140° TWA | 4,2 kn | 6,8 kn | +62 % |
| 12 kn TWS, 160° TWA | 4,8 kn | 7,2 kn | +50 % |
| 8 kn TWS, 90° TWA (Code 0) | 5,0 kn | 6,5 kn | +30 % |
| 15 kn TWS, 120° TWA | 5,5 kn | 7,8 kn | +42 % |
| 6 kn TWS, 100° TWA (Code 0) | 3,2 kn | 5,1 kn | +59 % |

Diese Zahlen basieren auf typischen Polardaten einer 38-Fuß-Fahrtenyacht (z. B. Bavaria 38 Cruiser,
Hanse 388). Sie verdeutlichen: Leichtwindsegel sind keine optionale Spielerei, sondern ein
fundamentaler Leistungsfaktor.

### 1.2 Historische Entwicklung

Die Geschichte der Vorwindsegel reicht bis in die Anfänge der Segelschifffahrt zurück:

- **Vor 1900**: Rahsegel und Passatsegel als Vorwindsegel auf Großseglern
- **1920er–1960er**: Klassische Baumspinnaker auf Regattayachten, symmetrisch, mit festem Spinnakerbaum
- **1970er**: Entwicklung des modernen symmetrischen Spinnakers mit Nylon-Ripstop
- **1980er**: Aufkommen asymmetrischer Spinnaker im Regattasegeln
- **1990er**: Gennaker-Konzept etabliert sich im Fahrtensegeln; erste Snuffer/Socken
- **2000er**: Code 0 und Screecher als laminierte Leichtwindsegel; Rollsysteme
- **2010er**: Hochleistungs-Laminate (Pentex, Technora); Top-Down-Furler
- **2020er**: Hybridkonstruktionen, leichtere Materialien, verbesserte Furltechnik

### 1.3 Klassifizierung im Yachtdesign-Kontext

Im AYDI-System werden Leichtwindsegel nach folgenden Kriterien klassifiziert:

**Nach Symmetrie:**
- Symmetrisch (traditioneller Spinnaker mit Baum)
- Asymmetrisch (Gennaker, Code 0, ohne Baum)

**Nach Windwinkelbereich:**
- Vorwindsegel (TWA 140°–180°): Symmetrischer Spinnaker
- Halbwindsegel (TWA 80°–140°): Gennaker, asymmetrischer Spinnaker
- Leichtwindvorsegel (TWA 60°–100°): Code 0, Screecher

**Nach Einsatzzweck:**
- Regattasegel (leichter, größer, empfindlicher)
- Fahrtensegel (robuster, einfacher zu handhaben, kleiner)
- Einhand-/Kurzhandsegel (mit Furler, selbstbergend)

### 1.4 Relevanz für die Yacht-Bewertung

Für die AYDI-Analyse sind Leichtwindsegel in mehreren Modulen relevant:

- **Ergonomie-Modul**: Handling-Anforderungen, Crewgröße, Snuffer-Bedienbarkeit
- **Compliance-Modul**: Bugspriet-Festigkeit, Beschlagdimensionierung, CE-Kategorie
- **Material-Modul**: Tuchzustand, UV-Alterung, Nahtintegrität
- **Kosten-Modul**: Anschaffung, Wartung, Ersatzzyklen
- **Sicherheits-Modul**: Broaching-Risiko, Windlimits, MOB-Risiko
- **Leistungs-Modul**: Polardaten-Verbesserung, Reviereignung

### 1.5 Windbereichs-Übersicht

```
TWA (True Wind Angle):
  60°  70°  80°  90° 100° 110° 120° 130° 140° 150° 160° 170° 180°
   |    |    |    |    |    |    |    |    |    |    |    |    |
   |<-- Code 0 / Screecher -->|    |    |    |    |    |    |
   |    |    |<--- Gennaker / A-Spi -------->|    |    |    |
   |    |    |    |    |    |    |<-- Symm. Spinnaker ------>|
   |    |    |<-- Code D / Blister -->|    |    |    |    |    |
   |    |    |    |    |    |<---- MPS / Reacher ---->|    |    |
```

### 1.6 Nomenklatur in diesem Dokument

| Begriff | Bedeutung |
|---------|-----------|
| TWA | True Wind Angle — wahrer Windwinkel |
| TWS | True Wind Speed — wahre Windgeschwindigkeit |
| AWA | Apparent Wind Angle — scheinbarer Windwinkel |
| AWS | Apparent Wind Speed — scheinbare Windgeschwindigkeit |
| I | Vorstag-Höhe (Fock-Dreieck) |
| J | Vorstag-Fußlänge (Mastfuß bis Bug) |
| SPL | Spinnaker-Pfahllänge |
| SMW | Spinnaker-Mittelbreite |
| SFL | Spinnaker-Fußlänge |
| SLU | Spinnaker-Vorliek |
| SLE | Spinnaker-Achterliek |

---

## 2. Spinnaker-Typen

### 2.1 Symmetrischer Spinnaker (S-Type)

#### 2.1.1 Definition und Charakteristik

Der symmetrische Spinnaker ist das klassische Vorwindsegel. Er wird an beiden Schothörnern
identisch geschnitten, sodass Luv- und Leeseite spiegelbildlich sind. Die Steuerung erfolgt
über einen Spinnakerbaum, der das Luvschothorn (den „Hals") nach außen hält.

**Geometrische Merkmale:**
- Symmetrische Schnittform um die vertikale Mittelachse
- Vorliek = Achterliek (SLU = SLE)
- Maximale Mittelbreite (SMW) bei ca. 50–60 % der Höhe
- Bauchtiefe: 15–25 % der Mittelbreite (je nach Windstärke-Auslegung)
- Oberes Profil voller als unteres für vertikale Stabilität

**Typische Dimensionen relativ zu I×J:**
- Regatta: SLU = 0,95 × √(I² + J²), SMW = 1,8 × J, SFL = 1,8 × J
- Fahrt: SLU = 0,90 × √(I² + J²), SMW = 1,6 × J, SFL = 1,6 × J

**Windbereich:**
- TWA: 120°–180° (optimal 140°–170°)
- TWS: 6–25 kn (je nach Tuchgewicht)
- AWA: 80°–160°

#### 2.1.2 Untertypen

**S1 — Leichtwind-Runner (TWS 4–12 kn):**
- Tuchgewicht: 0,5–0,75 oz Nylon
- Sehr voller Schnitt, maximales Volumen
- Große Fläche (SMW bis 2,0 × J)
- Empfindlich gegen Überpressung
- Einsatz: reine Vorwindkurse bei Leichtwind

**S2 — Allround-Spinnaker (TWS 8–20 kn):**
- Tuchgewicht: 0,75–1,5 oz Nylon
- Moderater Bauch, vielseitig einsetzbar
- Standard-Dimensionen
- Guter Kompromiss zwischen Leistung und Handling
- Einsatz: Standardsegel für Regatta und Fahrt

**S3 — Starkwind-Runner (TWS 15–30 kn):**
- Tuchgewicht: 1,5–2,2 oz Nylon oder Polyester
- Flacherer Schnitt, reduziertes Volumen
- Kleinere Fläche (SMW 1,4 × J)
- Verstärkte Ecken und Nähte
- Einsatz: Vorwind bei viel Wind, Offshore-Rennen

**S4 — Flanker/Reaching-Spinnaker:**
- Tuchgewicht: 0,75–1,0 oz Nylon
- Flacher geschnitten als Runner
- Engerer Windbereich: TWA 100°–140°
- Wird mit kurzem Baum gefahren
- Einsatz: Halbwind-Reaching auf Regatten

#### 2.1.3 Vor- und Nachteile

| Vorteil | Nachteil |
|---------|----------|
| Maximale Fläche vor dem Wind | Spinnakerbaum erforderlich |
| Symmetrie erlaubt einfache Halsen | Komplexes Handling (Baum, Topping, Niederholer) |
| Bewährtes Konzept, viel Erfahrung | Höheres Broaching-Risiko |
| Große Windwinkel-Abdeckung | Crew-Anforderung: mind. 3 Personen |
| ORC/IRC-Vermessung standardisiert | Nicht einhandsegel-tauglich |
| Gut für reine Vorwindkurse | Baum-Lagerung an Bord |

### 2.2 Asymmetrischer Spinnaker (A-Type)

#### 2.2.1 Definition und Charakteristik

Der asymmetrische Spinnaker wird am Vorliek (Luvseite) über eine Halsleine am Bug oder
Bugspriet befestigt. Er hat ein definiertes Vorliek und Achterliek und wird ohne Spinnakerbaum
gefahren. Die Form ähnelt einem sehr großen, bauchigen Vorsegel.

**Geometrische Merkmale:**
- Asymmetrische Schnittform
- Vorliek kürzer als Achterliek (SLU < SLE, typisch 5–10 % Differenz)
- Vorliek straffer, Achterliek freier geschnitten
- Tack (Hals) am Bug/Bugspriet, Head (Kopf) am Masttopp
- Maximaler Bauch bei 40–50 % der Sehnenlänge

**Typische Dimensionen relativ zu I×J:**
- Regatta: SLU = 0,95 × I, SMW = 1,6 × J, SFL = 1,5 × J
- Fahrt: SLU = 0,90 × I, SMW = 1,4 × J, SFL = 1,3 × J

**Windbereich:**
- TWA: 80°–160° (optimal 90°–140°)
- TWS: 6–25 kn
- AWA: 50°–120°

#### 2.2.2 Untertypen

**A1 — Leichtwind-Reaching (TWS 4–10 kn):**
- Tuchgewicht: 0,5–0,75 oz Nylon
- Voller Schnitt, große Fläche
- TWA: 80°–130°
- Leichtes Material, empfindlich

**A2 — Allround-Reaching (TWS 8–18 kn):**
- Tuchgewicht: 0,75–1,5 oz Nylon
- Mittlerer Bauch, universell einsetzbar
- TWA: 90°–150°
- Standardsegel für die meisten Yachten

**A3 — Starkwind-Reaching (TWS 14–28 kn):**
- Tuchgewicht: 1,5–2,0 oz Nylon oder Polyester
- Flacher Schnitt, verstärkte Konstruktion
- TWA: 100°–160°
- Robusteres Handling

**A4 — Heavy Runner (TWS 12–25 kn):**
- Tuchgewicht: 1,2–1,8 oz Nylon
- Sehr voller Schnitt für tiefe Windwinkel
- TWA: 130°–180°
- Ersatz für symmetrischen Spinnaker auf Fahrtenyachten

#### 2.2.3 Vor- und Nachteile

| Vorteil | Nachteil |
|---------|----------|
| Kein Spinnakerbaum nötig | Weniger effektiv bei TWA >160° |
| Einfacheres Handling (2-Personen-Crew möglich) | Bugspriet oder Bugbeschlag nötig |
| Halsen ohne Baummanöver | Asymmetrische Belastung am Rigg |
| Snuffer/Sock-kompatibel | Bei reinem Vorwind unterlegen |
| Gut für Kurzhandcrews | Scheuergefahr am Vorstag |
| Weniger Broaching als symmetrisch | Größerer Trimm-Aufwand am Achterliek |

### 2.3 Gennaker

#### 2.3.1 Definition und Abgrenzung

Der Begriff „Gennaker" ist eine Wortkombination aus „Genua" und „Spinnaker" und bezeichnet
ein asymmetrisches Leichtwindsegel, das spezifisch für den Fahrensegel-Einsatz konzipiert ist.
Im Vergleich zum reinen A-Spinnaker ist der Gennaker:

- Flacher geschnitten (geringere Bauchtiefe)
- Kleiner dimensioniert (typisch 80–90 % der A-Spi-Fläche)
- Robuster gebaut (schwereres Tuch, stärkere Nähte)
- Einfacher zu handhaben (Snuffer-optimiert)
- Weniger leistungsorientiert, dafür vielseitiger

**Windbereich:**
- TWA: 80°–150° (optimal 90°–130°)
- TWS: 6–22 kn
- AWA: 55°–110°

#### 2.3.2 Gennaker-Typen nach Einsatz

**Cruising-Gennaker:**
- Tuchgewicht: 1,0–1,5 oz Nylon
- Snuffer integriert oder nachrüstbar
- Moderate Fläche, leicht zu handhaben
- Für 2-Personen-Crew ausgelegt
- Preisgünstig, wartungsarm
- Lebensdauer: 8–12 Jahre bei Fahrteneinsatz

**Performance-Gennaker:**
- Tuchgewicht: 0,75–1,2 oz Nylon
- Optimiert auf maximale Projected Area
- Größere Fläche als Cruising-Variante
- Regatta-tauglich, aber fahrtentauglich
- Lebensdauer: 4–8 Jahre

**Furling-Gennaker:**
- Auf Rollanlage (Top-Down-Furler) konzipiert
- Vorliek mit Torsionsseil oder -kabel
- Anti-Torsions-Konstruktion
- Kann vom Cockpit aus geborgen werden
- Höchster Komfort, aber Leistungseinbuße 5–10 %

#### 2.3.3 Dimensionierung

| Bootslänge (LOA) | Fläche (m²) | SLU (m) | SMW (m) | Tuchgewicht (oz) |
|-------------------|-------------|---------|---------|-------------------|
| 28 ft / 8,5 m | 45–55 | 10,5 | 6,0 | 0,75–1,0 |
| 32 ft / 9,8 m | 60–75 | 12,0 | 7,0 | 0,75–1,2 |
| 36 ft / 11,0 m | 80–100 | 13,5 | 8,0 | 1,0–1,5 |
| 40 ft / 12,2 m | 100–130 | 15,0 | 9,5 | 1,0–1,5 |
| 44 ft / 13,4 m | 130–160 | 16,5 | 10,5 | 1,2–1,5 |
| 50 ft / 15,2 m | 170–220 | 18,5 | 12,0 | 1,5–2,0 |

### 2.4 Code 0

#### 2.4.1 Definition und Charakteristik

Der Code 0 ist ein hochspezialisiertes Leichtwindsegel für enge Halbwindkurse. Er füllt die
Lücke zwischen Genua und Gennaker und wird typischerweise auf einer Rollanlage am Bugspriet
oder einem dedizierten Vorstag gefahren.

**Charakteristische Merkmale:**
- Sehr flacher Schnitt (Bauchtiefe 8–14 % der Sehnenlänge)
- Laminiertuch oder leichtes Membrantuch (kein Nylon!)
- Torsionsseil im Vorliek für Furling-Betrieb
- Enger Windbereich, aber höchste Effizienz
- Profilform ähnelt einem großen, leichten Vorsegel

**Windbereich:**
- TWA: 55°–100° (optimal 65°–85°)
- TWS: 4–16 kn
- AWA: 40°–75°

**Typische Dimensionen:**
- Vorliek: 100–105 % von I
- Fußlänge: 120–140 % von J
- Mittelbreite: 100–120 % von J

#### 2.4.2 Materialien

Code-0-Segel werden nicht aus Nylon, sondern aus steiferen Materialien gefertigt:

- **Dimension Polyant CZ**: Mylar-Laminat mit Taffeta, 80–120 g/m²
- **Dimension Polyant GP**: Hochleistungs-Laminat, 60–100 g/m²
- **Pentex-Laminat**: Geringerer Stretch als Polyester, 90–130 g/m²
- **Technora-Laminat**: Ultra-Low-Stretch, 70–110 g/m²
- **Dyneema-Membran**: Hochleistung, 50–90 g/m²

#### 2.4.3 Furling-Systeme für Code 0

Der Code 0 wird fast ausschließlich mit Rollanlage eingesetzt:

| System | Hersteller | Typ | Trommel | Gewicht (kg) | Preis EUR |
|--------|-----------|-----|---------|-------------|-----------|
| Karver KF-3 | Karver Systems | Top-Down | Kopf | 3,5 | 2.800–3.500 |
| Karver KF-5 | Karver Systems | Top-Down | Kopf | 5,2 | 3.500–4.500 |
| Facnor FX-2500 | Facnor | Top-Down | Kopf | 4,8 | 3.200–4.000 |
| Facnor FX-4500 | Facnor | Top-Down | Kopf | 6,5 | 4.200–5.500 |
| Selden GX | Selden Mast | Top-Down | Fuß | 5,0 | 3.000–4.200 |
| Ronstan FurlBoom | Ronstan | Top-Down | Kopf | 3,8 | 2.500–3.800 |
| Profurl C350 | Profurl | Top-Down | Kopf | 4,2 | 2.900–3.800 |
| Profurl C490 | Profurl | Top-Down | Kopf | 6,0 | 3.800–5.200 |

#### 2.4.4 Vor- und Nachteile

| Vorteil | Nachteil |
|---------|----------|
| Leistungssteigerung bei 60–90° TWA | Enger optimaler Windbereich |
| Furling erlaubt Einhand-Bedienung | Teures Furling-System nötig |
| Schnelles Setzen/Bergen | Empfindliches Laminat-Tuch |
| Kein Snuffer nötig | Nicht bei >16 kn TWS einsetzbar |
| Füllt die Genua-Gennaker-Lücke | Hohe Anschaffungskosten |
| Geringer Stauraum (aufgerollt) | Torsionsseil kann versagen |

### 2.5 Code D (Code Downwind)

#### 2.5.1 Definition

Der Code D ist eine Weiterentwicklung des Code 0 für tiefere Windwinkel. Er kombiniert
die Furling-Fähigkeit des Code 0 mit dem breiteren Windbereich eines Gennakers.

**Windbereich:**
- TWA: 90°–140° (optimal 100°–130°)
- TWS: 6–18 kn
- AWA: 55°–100°

**Konstruktionsmerkmale:**
- Bauchiger als Code 0 (Bauchtiefe 14–20 %)
- Torsionsseil im Vorliek
- Nylon oder leichtes Laminat (0,75–1,2 oz)
- Top-Down-Furler-kompatibel
- Größere Fläche als Code 0

#### 2.5.2 Einsatzprofil

Der Code D ist das ideale Segel für:
- Küstenkreuzer, die einen Snuffer vermeiden möchten
- Einhand- und Kurzhandsegler
- Yachten ohne Bugspriet (mit Bugbeschlag)
- Reviere mit vorherrschend raumen Winden (Passatreviere)

### 2.6 Screecher

#### 2.6.1 Definition und Abgrenzung zum Code 0

Der Screecher ist funktional dem Code 0 sehr ähnlich, wird aber typischerweise am bestehenden
Vorstag oder an einem separaten, nicht abgestützten Innenstag gefahren. Er ist flacher als
ein Code 0 und näher am Wind einsetzbar.

**Windbereich:**
- TWA: 50°–90° (optimal 55°–75°)
- TWS: 4–14 kn
- AWA: 35°–65°

**Unterschiede zum Code 0:**
- Flacherer Schnitt
- Oft am Vorstag auf vorhandenem Roller
- Kein Bugspriet nötig
- Geringere Fläche
- Profil näher an einer Light-Genua

### 2.7 Blister / Reacher

#### 2.7.1 Definition

Der Blister (auch „Reacher" oder „Reaching-Spinnaker") ist ein asymmetrisches Segel für
den Bereich zwischen Code 0 und vollem Gennaker. Er ist aus leichtem Nylon gefertigt,
aber flacher geschnitten als ein Standard-Gennaker.

**Windbereich:**
- TWA: 75°–130° (optimal 85°–115°)
- TWS: 8–20 kn
- AWA: 50°–90°

**Merkmale:**
- Nylon-Ripstop, 0,75–1,0 oz
- Flacher als Gennaker, bauchiger als Code 0
- Wird mit Snuffer oder freifliegend gefahren
- Kein Furling-System
- Gute Vielseitigkeit

### 2.8 MPS (Multi-Purpose Spinnaker)

#### 2.8.1 Definition und Konzept

Der MPS ist ein Kompromiss-Segel, das den breitestmöglichen Windbereich abdecken soll.
Es wird von Herstellern wie North Sails und Elvström als „Ein-Segel-Lösung" für
Fahrtensegler vermarktet.

**Windbereich:**
- TWA: 80°–165° (breiter als jeder Einzeltyp)
- TWS: 6–20 kn
- AWA: 50°–120°

**Konstruktionsmerkmale:**
- Nylon-Ripstop, 0,9–1,5 oz
- Moderater Bauch (Kompromiss-Profil)
- Snuffer-kompatibel
- Mittlere Fläche (kleiner als dedizierter A2, größer als Code 0)
- Verstärkte Ecken und Nähte

#### 2.8.2 Bewertung

| Aspekt | Bewertung |
|--------|-----------|
| Vielseitigkeit | ★★★★★ |
| Leistung Vorwind | ★★★☆☆ |
| Leistung Halbwind | ★★★☆☆ |
| Handling | ★★★★☆ |
| Kosten-Nutzen | ★★★★☆ |
| Regatta-Eignung | ★★☆☆☆ |

Der MPS ist ideal für:
- Fahrtensegler mit nur einem Leichtwindsegel
- Yachten mit begrenztem Stauraum
- Crews mit wenig Spinnaker-Erfahrung
- Charterboote

### 2.9 Vergleichsmatrix aller Typen

| Typ | TWA opt. | TWS (kn) | Material | Baum | Furler | Snuffer | Crew min. | Kosten-Index |
|-----|----------|----------|----------|------|--------|---------|-----------|-------------|
| S1 Runner | 150–180° | 4–12 | Nylon 0,5 oz | Ja | Nein | Nein | 3 | 100 |
| S2 Allround | 130–170° | 8–20 | Nylon 0,75 oz | Ja | Nein | Nein | 3 | 100 |
| S3 Heavy | 130–170° | 15–30 | Nylon 1,5 oz | Ja | Nein | Nein | 3 | 110 |
| A1 Light | 80–130° | 4–10 | Nylon 0,5 oz | Nein | Nein | Ja | 2 | 90 |
| A2 Allround | 90–150° | 8–18 | Nylon 0,75 oz | Nein | Nein | Ja | 2 | 90 |
| A3 Heavy | 100–160° | 14–28 | Nylon 1,5 oz | Nein | Nein | Ja | 2 | 95 |
| A4 Runner | 130–180° | 12–25 | Nylon 1,2 oz | Nein | Nein | Ja | 2 | 95 |
| Gennaker | 90–130° | 6–22 | Nylon 1,0 oz | Nein | Optional | Ja | 2 | 85 |
| Code 0 | 65–85° | 4–16 | Laminat | Nein | Ja | Nein | 1 | 140 |
| Code D | 100–130° | 6–18 | Nylon/Laminat | Nein | Ja | Nein | 1 | 130 |
| Screecher | 55–75° | 4–14 | Laminat | Nein | Ja | Nein | 1 | 120 |
| Blister | 85–115° | 8–20 | Nylon 0,75 oz | Nein | Nein | Ja | 2 | 80 |
| MPS | 90–150° | 6–20 | Nylon 1,0 oz | Nein | Nein | Ja | 2 | 90 |

### 2.10 Empfehlungsmatrix nach Yachttyp

| Yachttyp | Empfehlung 1 | Empfehlung 2 | Empfehlung 3 |
|----------|-------------|-------------|-------------|
| Regatta-Eintonner | S1+S2+A2 | Code 0 | A3 |
| Performance Cruiser 35–40 ft | A2 (Gennaker) | Code 0 | S2 (optional) |
| Fahrtenyacht 36–42 ft | MPS oder Cruising-Gennaker | Code 0 (optional) | — |
| Blauwasseryacht 42–50 ft | MPS mit Snuffer | Code D | S2 (optional) |
| Einhandsegler | Code 0 mit Furler | Code D mit Furler | — |
| Katamaran Cruising | Screecher/Code 0 | A2 Gennaker | — |
| Katamaran Racing | Code 0 | A2 | A5 (Reaching) |
| Daysailer/Sportboot | Gennaker mit Snuffer | — | — |

---

## 3. Materialien und Tuchgewichte

### 3.1 Nylon-Ripstop

#### 3.1.1 Grundlagen

Nylon (Polyamid 6.6) ist das klassische Spinnaker-Material. Seine hohe Elastizität ermöglicht
die aerodynamisch vorteilhafte Formgebung von Leichtwindsegeln. Das Ripstop-Gewebe enthält
in regelmäßigen Abständen (typisch 5–8 mm) verstärkte Fäden, die eine Rissausbreitung
verhindern.

**Physikalische Eigenschaften:**
- Dichte: 1,14 g/cm³
- Zugfestigkeit: 70–85 MPa
- Bruchdehnung: 15–25 %
- Elastizitätsmodul: 2,5–5,0 GPa
- UV-Beständigkeit: Mäßig (ohne Beschichtung)
- Wasseraufnahme: 3,5–4,5 % (nassbedingte Dehnung!)
- Schmelzpunkt: 260 °C

#### 3.1.2 Tuchgewichte und Einsatzbereich

| Gewicht (oz/yd²) | Gewicht (g/m²) | Einsatz | TWS max (kn) | Lebensdauer |
|-------------------|---------------|---------|--------------|-------------|
| 0,50 | 17 | S1, A1, ultraleicht | 10–12 | 3–5 Jahre |
| 0,60 | 20 | Leichtwind-Regatta | 12–14 | 4–6 Jahre |
| 0,75 | 25 | Standard-Regatta, A2 | 16–18 | 5–8 Jahre |
| 0,90 | 30 | Allround, Gennaker | 18–20 | 6–10 Jahre |
| 1,00 | 34 | Fahrt, MPS | 20–22 | 8–12 Jahre |
| 1,20 | 41 | Starkwind-Reaching | 22–25 | 8–12 Jahre |
| 1,50 | 51 | S3, A3, Heavy | 25–28 | 10–15 Jahre |
| 2,00 | 68 | Offshore-Heavy | 28–32 | 12–18 Jahre |
| 2,20 | 75 | Superyacht-Heavy | 30–35 | 15–20 Jahre |

#### 3.1.3 Nylon-Qualitäten

**Standard-Nylon (z. B. Bainbridge, Contender):**
- Grundqualität, gutes Preis-Leistungs-Verhältnis
- Silikon- oder PU-beschichtet
- UV-Stabilisatoren eingearbeitet
- Farbauswahl: ca. 15–20 Standardfarben
- Preis: 8–15 EUR/m²

**Premium-Nylon (z. B. Dimension Polyant AP-Serie):**
- Höhere Fadenzahl, gleichmäßigere Struktur
- Verbesserte Beschichtung (beidseitig)
- Geringere Porosität
- Bessere UV-Beständigkeit
- Preis: 15–28 EUR/m²

**High-Tenacity-Nylon (z. B. Bainbridge HT):**
- 15–20 % höhere Reißfestigkeit
- Geringere Dehnung bei Belastung
- Für Starkwind-Spinnaker
- Preis: 18–32 EUR/m²

#### 3.1.4 Beschichtungen

| Beschichtung | Funktion | Gewichtszunahme | Haltbarkeit |
|-------------|----------|-----------------|-------------|
| Silikon | Porositätsminderung | +5–8 % | 5–8 Jahre |
| PU (Polyurethan) | Porositätsminderung, UV-Schutz | +8–12 % | 8–12 Jahre |
| DWR (Water Repellent) | Wasserabweisung | +2–3 % | 3–5 Jahre |
| UV-Stabilisator | UV-Schutz | +1–2 % | 5–10 Jahre |
| Anti-Microbial | Schimmelschutz | +1 % | 5–8 Jahre |

### 3.2 Polyester

#### 3.2.1 Einsatz bei Leichtwindsegeln

Polyester (PET, Dacron) wird bei Leichtwindsegeln seltener eingesetzt als Nylon, hat aber
Vorteile in spezifischen Anwendungen:

- **Starkwind-Spinnaker (S3, A3)**: Geringere Dehnung als Nylon
- **Screecher**: Formstabilität bei höheren Windstärken
- **Code 0 (als Taffeta in Laminaten)**: Abriebschutz

**Physikalische Eigenschaften:**
- Dichte: 1,38 g/cm³
- Zugfestigkeit: 55–75 MPa
- Bruchdehnung: 12–15 %
- Elastizitätsmodul: 3,0–5,5 GPa
- UV-Beständigkeit: Gut
- Wasseraufnahme: 0,4 % (Vorteil gegenüber Nylon!)

**Tuchgewichte für Spinnaker-Einsatz:**
- 1,5 oz (51 g/m²): Starkwind-Spinnaker
- 2,0 oz (68 g/m²): Heavy-Reacher
- 2,5 oz (85 g/m²): Code 0 (schwere Ausführung)

### 3.3 Pentex

#### 3.3.1 Eigenschaften

Pentex (PEN = Polyethylennaphthalat) ist ein hochleistungs-Polyester mit deutlich
geringerem Kriechverhalten und höherer Steifigkeit als Standard-PET.

**Physikalische Eigenschaften:**
- Zugfestigkeit: 110–130 MPa
- Bruchdehnung: 4–6 %
- Elastizitätsmodul: 8–12 GPa
- UV-Beständigkeit: Sehr gut
- Kriechfestigkeit: 3× besser als PET

**Einsatz:**
- Code 0 (Hochleistung)
- Screecher
- Regatta-Gennaker-Vorlieke

**Preis:** 30–55 EUR/m² (als Laminat)

### 3.4 Technora

#### 3.4.1 Eigenschaften

Technora ist eine Aramidfaser (Co-Poly-p-Phenylendiamin/3,4'-Oxydiphenylendiamin-Terephthalamid)
von Teijin, die höhere UV-Beständigkeit als Kevlar bietet.

**Physikalische Eigenschaften:**
- Zugfestigkeit: 340–390 MPa (als Faser: 3.400 MPa)
- Bruchdehnung: 4,5 %
- Elastizitätsmodul: 73 GPa
- UV-Beständigkeit: Gut (besser als Kevlar)
- Feuchtigkeitsaufnahme: 2,0 %

**Einsatz:**
- Hochleistungs-Code-0-Segel
- Verstärkungsstreifen in Spinnakern
- Torsionsseile

**Preis:** 50–90 EUR/m² (als Laminat)

### 3.5 Mylar (Polyester-Film)

#### 3.5.1 Einsatz in Laminaten

Mylar ist kein eigenständiges Segeltuch, sondern ein PET-Film, der als Trägerschicht in
Laminaten verwendet wird. Er verleiht dem Laminat Steifigkeit und geringe Porosität.

**Laminataufbau (typisch):**
```
Außen-Taffeta (Polyester oder Nylon)
↓
Mylar-Film (6–12 µm)
↓
Fasern (Pentex, Technora, Dyneema)
↓
Mylar-Film (6–12 µm)
↓
Innen-Taffeta (Polyester oder Nylon)
```

**Eigenschaften des Mylar-Films:**
- Dicke: 6–25 µm
- Zugfestigkeit: 190 MPa
- UV-Beständigkeit: Schlecht (muss durch Taffeta geschützt sein)
- Delaminierung: Hauptversagensmechanismus bei Laminatsegeln

### 3.6 Carbon-Fasern

#### 3.6.1 Einsatz bei Leichtwindsegeln

Carbonfasern werden in Hochleistungs-Leichtwindsegeln als Verstärkungsfasern in
Laminatkonstruktionen verwendet.

**Physikalische Eigenschaften:**
- Zugfestigkeit: 3.500–7.000 MPa (als Faser)
- Elastizitätsmodul: 230–400 GPa
- Bruchdehnung: 1,5–2,0 %
- Dichte: 1,75–1,95 g/cm³

**Einsatz:**
- Hochleistungs-Code-0-Segel (Regatta)
- Superyacht-Spinnaker (als Verstärkung)
- Torsionsseile (Carbon-Kern)

**Preis:** 80–180 EUR/m² (als Laminat)

### 3.7 Dyneema / Spectra (UHMWPE)

#### 3.7.1 Eigenschaften

Dyneema (DSM) und Spectra (Honeywell) sind Ultra-High-Molecular-Weight-Polyethylen-Fasern
mit der höchsten spezifischen Festigkeit aller kommerziellen Fasern.

**Physikalische Eigenschaften:**
- Zugfestigkeit: 3.500–4.000 MPa (als Faser)
- Elastizitätsmodul: 100–130 GPa
- Bruchdehnung: 3,5–4,0 %
- Dichte: 0,97 g/cm³ (schwimmt!)
- UV-Beständigkeit: Gut
- Kriechverhalten: Problematisch bei Dauerbelastung

**Einsatz bei Leichtwindsegeln:**
- Verstärkungsstreifen in Spinnakern
- Code-0-Laminate
- Hochleistungs-Schoten (Dyneema SK78, SK99)
- Halskauschen und Kopfbrett-Verstärkungen

**Preis:** 60–140 EUR/m² (als Laminat)

### 3.8 Dimension Polyant Produktlinien

#### 3.8.1 AP-Serie (All Purpose Nylon)

| Produkt | Gewicht (g/m²) | Reißfestigkeit (N/5cm) | Dehnung (%) | Einsatz |
|---------|---------------|------------------------|-------------|---------|
| AP-20 | 20 | 180/160 | 18/20 | Ultraleicht-Spinnaker |
| AP-25 | 25 | 240/220 | 16/18 | Standard-Regatta-Spinnaker |
| AP-30 | 30 | 300/280 | 15/17 | Allround-Spinnaker |
| AP-34 | 34 | 350/330 | 14/16 | Fahrt-Spinnaker |
| AP-41 | 41 | 420/400 | 13/15 | Starkwind-Spinnaker |
| AP-51 | 51 | 520/500 | 12/14 | Heavy-Spinnaker |
| AP-68 | 68 | 680/650 | 11/13 | Superyacht-Spinnaker |

(Werte: Kette/Schuss, typische Werte, herstellerabhängig)

#### 3.8.2 CZ-Serie (Code Zero Laminate)

| Produkt | Gewicht (g/m²) | Fasermaterial | Dehnung (%) | Einsatz |
|---------|---------------|---------------|-------------|---------|
| CZ-80 | 80 | Pentex | 1,2/1,5 | Leichtwind-Code 0 |
| CZ-100 | 100 | Pentex | 1,0/1,3 | Standard-Code 0 |
| CZ-120 | 120 | Pentex/Technora | 0,8/1,0 | Regatta-Code 0 |
| CZ-90T | 90 | Technora | 0,7/0,9 | High-Performance Code 0 |
| CZ-110D | 110 | Dyneema | 0,6/0,8 | Top-Performance Code 0 |

#### 3.8.3 GP-Serie (Grand Prix Laminate)

| Produkt | Gewicht (g/m²) | Fasermaterial | Einsatz |
|---------|---------------|---------------|---------|
| GP-60 | 60 | Carbon/Technora | Ultra-Regatta Code 0 |
| GP-75 | 75 | Carbon/Dyneema | Grand-Prix-Spinnaker |
| GP-90 | 90 | Carbon/Pentex | Offshore-Regatta |
| GP-110 | 110 | Carbon/Technora | Maxi-Yacht Spinnaker |

### 3.9 Materialvergleich

| Material | Festigkeit | Dehnung | UV | Kosten | Gewicht | Handling | Lebensdauer |
|----------|-----------|---------|-----|--------|---------|----------|-------------|
| Nylon 0,75 oz | ★★★☆☆ | ★★☆☆☆ | ★★☆☆☆ | ★★★★★ | ★★★★★ | ★★★★★ | ★★★☆☆ |
| Nylon 1,5 oz | ★★★★☆ | ★★★☆☆ | ★★★☆☆ | ★★★★☆ | ★★★★☆ | ★★★★☆ | ★★★★☆ |
| Polyester | ★★★★☆ | ★★★★☆ | ★★★★☆ | ★★★★☆ | ★★★☆☆ | ★★★★☆ | ★★★★☆ |
| Pentex-Laminat | ★★★★☆ | ★★★★★ | ★★★★☆ | ★★★☆☆ | ★★★★☆ | ★★★☆☆ | ★★★★☆ |
| Technora-Laminat | ★★★★★ | ★★★★★ | ★★★★☆ | ★★☆☆☆ | ★★★★☆ | ★★★☆☆ | ★★★★☆ |
| Carbon-Laminat | ★★★★★ | ★★★★★ | ★★★☆☆ | ★☆☆☆☆ | ★★★★★ | ★★☆☆☆ | ★★★☆☆ |
| Dyneema-Laminat | ★★★★★ | ★★★★★ | ★★★★☆ | ★★☆☆☆ | ★★★★★ | ★★★☆☆ | ★★★★☆ |

### 3.10 UV-Degradation

#### 3.10.1 UV-Auswirkungen nach Material

| Material | UV-Verlust nach 500 h | UV-Verlust nach 1000 h | UV-Verlust nach 2000 h |
|----------|----------------------|------------------------|------------------------|
| Nylon (unbeschichtet) | -15 % | -30 % | -55 % |
| Nylon (UV-stabilisiert) | -8 % | -18 % | -35 % |
| Nylon (PU-beschichtet) | -5 % | -12 % | -25 % |
| Polyester | -3 % | -8 % | -15 % |
| Pentex | -2 % | -5 % | -12 % |
| Technora | -5 % | -12 % | -22 % |
| Dyneema | -3 % | -8 % | -18 % |
| Mylar-Film | -20 % | -40 % | -70 % |

(UV-Verlust = Reduktion der Reißfestigkeit gegenüber Neuzustand)

#### 3.10.2 Empfehlungen zur UV-Minimierung

1. Spinnaker niemals unnötig gesetzt lassen (auch bei Flaute)
2. An Bord: Spinnaker im Segel-Beutel unter Deck lagern
3. Code 0: nach Gebrauch aufrollen (Furler) oder mit UV-Schutzstreifen
4. Snuffer als UV-Schutz bei längerem Setzen nutzen
5. Dunkle Farben absorbieren mehr UV → kürzere Lebensdauer
6. Weiße oder hellblaue Spinnaker halten am längsten
7. Regelmäßig Festigkeit prüfen (Daumendrucktest: Nagel durch Tuch = sofort ersetzen)

---

## 4. Konstruktion

### 4.1 Panelschnitt-Methoden

#### 4.1.1 Radialer Schnitt

Beim radialen Schnitt verlaufen die Panels strahlenförmig von den drei Ecken (Kopf, Hals,
Schothorn) zur Mitte des Segels. Dieser Schnitt richtet die stärkere Kettrichtung des
Tuchs entlang der Hauptbelastungslinien aus.

**Vorteile:**
- Optimale Lastverteilung
- Weniger Verzerrung unter Last
- Bessere Formhaltung
- Standard bei Regattasegeln

**Nachteile:**
- Mehr Materialverschnitt (15–25 %)
- Mehr Nähte
- Höhere Arbeitskosten
- Komplexeres Nähmuster

**Typische Panel-Anzahl:**
- 30-ft-Spinnaker: 18–24 Panels
- 40-ft-Spinnaker: 24–36 Panels
- 50-ft-Spinnaker: 32–48 Panels

#### 4.1.2 Tri-radialer Schnitt

Der tri-radiale Schnitt ist die Weiterentwicklung des radialen Schnitts. Die Panels
strahlen von allen drei Ecken aus und treffen sich in einer zentralen „Clocking-Zone".

**Besonderheiten:**
- Drei separate Panelgruppen (Kopf, Hals, Schothorn)
- Jede Gruppe hat eigene Fadenausrichtung
- Übergangszone in der Segelmitte
- Höchste Formkontrolle

**Einsatz:**
- Hochleistungs-Regattaspinnaker
- Maxi-Yacht-Spinnaker
- Alle Segel über 100 m²

#### 4.1.3 Bi-radialer Schnitt

Der bi-radiale Schnitt kombiniert radiale Panels an den Ecken mit horizontalen Panels in
der Mitte. Er ist ein Kompromiss zwischen Leistung und Kosten.

**Einsatz:**
- Fahrt-Spinnaker und Gennaker
- Mittelpreissegment
- Segel bis ca. 80 m²

#### 4.1.4 Horizontaler Schnitt (Cross-Cut)

Der einfachste Schnitt: horizontale Panels von Vorliek zu Achterliek. Heute nur noch bei
sehr preisgünstigen Spinnakern oder bei Bootsklassen-Restriktionen.

**Nachteile:**
- Schlechte Formhaltung unter Last
- Verzerrung in den Ecken
- Nicht für Regatta geeignet

**Vorteil:**
- Günstigste Herstellungsmethode
- Geringster Materialverschnitt (5–10 %)

### 4.2 Nähte und Verbindungen

#### 4.2.1 Nahttypen

| Nahttyp | Beschreibung | Festigkeit | Einsatz |
|---------|-------------|-----------|---------|
| Überlappt (Lapped) | Panels überlappen 15–25 mm | 85–90 % Tuchfestigkeit | Standard bei Nylon-Spinnakern |
| Doppelt überlappt | Doppelte Überlappung | 90–95 % | Starkwind-Spinnaker |
| Glatt (Butted) | Panels stoßen aneinander, Klebeband | 70–80 % | Regatta-Ultraleicht |
| Wulstnaht (Rolled) | Umgeschlagene Naht | 95 % | Achterliek, Vorliek |
| Tapes + Kleber | Tape-Verbindung mit Klebstoff | 85–90 % | Laminate, Code 0 |

#### 4.2.2 Nähgarn

- **Standard**: Polyester-Nähgarn, V-92 oder V-138
- **Hochleistung**: PTFE-beschichtetes Polyester (Gore Tenara)
- **UV-beständig**: Solution-Dyed Polyester
- **Stiche pro cm**: 3–5 (Standard), 5–7 (Hochleistung)
- **Stichmuster**: Zickzack (Standard), Dreifach-Zickzack (Hochlast)

#### 4.2.3 Klebeband-Verbindungen

Bei Laminat-Segeln (Code 0, Screecher) werden zunehmend Klebeband-Verbindungen eingesetzt:

- **PSA-Tape (Pressure Sensitive Adhesive)**: Selbstklebend, 25–50 mm breit
- **Hotmelt-Tape**: Thermisch aufgeklebt, stärkere Verbindung
- **Kombination**: Genäht + getaped für maximale Festigkeit

### 4.3 Verstärkungen (Patches)

#### 4.3.1 Eck-Patches

Die drei Ecken (Kopf, Hals, Schothorn) sind die höchstbelasteten Bereiche. Sie erhalten
mehrlagige Verstärkungen:

**Kopf-Patch (Head):**
- Fläche: 0,3–0,6 m² (je nach Segelgröße)
- Lagen: 3–6 Lagen Nylon oder Dacron
- Ring: Edelstahl oder Titan, 20–40 mm Durchmesser
- Webbing: Polyester- oder Dyneema-Gurtband, 25–50 mm breit
- Lastverteilung über Fächer-Patches (radialer Schnitt)

**Hals-Patch (Tack):**
- Fläche: 0,4–0,8 m²
- Lagen: 4–8 Lagen
- Ring: Edelstahl, 25–50 mm
- Scheuerschutz: Dacron-Overlay gegen Vorstagkontakt
- Bei asymmetrisch: Halskausch oder Softschäkel-Ring

**Schothorn-Patch (Clew):**
- Fläche: 0,4–0,8 m²
- Lagen: 4–8 Lagen
- Ring: Edelstahl, 25–50 mm
- Bei symmetrisch: identisch mit Hals-Patch
- Scheuerschutz gegen Wanten und Vorstag

#### 4.3.2 Zwischen-Patches (Intermediate)

- Entlang der Nahtknotenpunkte
- An Stellen hoher Scheuerbelastung
- Typisch 2–3 Lagen, 0,05–0,15 m²

#### 4.3.3 Leech-Tape (Achterliekband)

- Material: Polyester-Gurtband oder Dacron-Streifen
- Breite: 15–30 mm
- Funktion: Achterliek-Stabilisierung, Flatterreduzierung
- Aufnährichtung: leichte Zugabe für Cup-Kontrolle

#### 4.3.4 Anti-Curl-Seil (Rollschutzseil)

Am Vorliek und/oder Achterliek eingenähtes dünnes Seil (Dyneema 3–5 mm), das das
Einrollen des Segels bei Leichtwind verhindert.

**Einsatz:**
- Code 0 (Vorliek): zwingend erforderlich
- Gennaker (Vorliek): empfohlen
- A-Spinnaker (Achterliek): optional

### 4.4 Torsionsseil / Torsionskabel

#### 4.4.1 Funktion

Das Torsionsseil ist das Schlüsselelement bei Code-0- und Furling-Gennaker-Segeln. Es
wird in das Vorliek eingenäht und überträgt die Drehbewegung des Furlers auf das gesamte
Vorliek, sodass sich das Segel gleichmäßig aufrollt.

#### 4.4.2 Typen

| Typ | Material | Durchmesser (mm) | Drehsteifigkeit | Einsatz |
|-----|----------|-----------------|-----------------|---------|
| Standard-Seil | Dyneema-Kern, PES-Mantel | 8–14 | Mittel | Fahrt-Code 0 |
| Carbon-Seil | Carbon-Kern, PES-Mantel | 6–10 | Hoch | Regatta-Code 0 |
| Hybridkabel | Edelstahldraht + Dyneema | 8–12 | Sehr hoch | Superyacht |
| Volldraht | 1×19 Edelstahl | 5–8 | Sehr hoch | Ältere Systeme |

#### 4.4.3 Dimensionierung

| Segelfläche (m²) | Seil-Durchmesser (mm) | Bruchlast (kN) |
|-------------------|----------------------|-----------------|
| 30–50 | 8 | 15 |
| 50–80 | 10 | 25 |
| 80–120 | 12 | 35 |
| 120–180 | 14 | 50 |
| 180–300 | 16 | 70 |

#### 4.4.4 Kritische Aspekte

- **Drehsteifigkeit**: Muss ausreichend sein, um das gesamte Segel gleichmäßig zu drehen
- **Spannung**: Zu wenig → Segel furlt schlecht; zu viel → Vorliek-Profil verzerrt
- **Termination**: Die Verbindung Seil ↔ Furler ist der häufigste Versagenspunkt
- **Ermüdung**: Torsionsseile unterliegen zyklischer Belastung (jeder Furl-/Unfurl-Zyklus)
- **Lebensdauer**: 500–2.000 Furl-Zyklen (materialabhängig)

### 4.5 Snuffer/Sock-Integration

#### 4.5.1 Konstruktive Anforderungen

Ein Segel, das mit Snuffer/Sock geborgen werden soll, muss konstruktiv darauf ausgelegt sein:

- **Kopf-Patch**: Muss Snuffer-Ringführung aufnehmen
- **Vorliek**: Glatte Nähte, keine vorstehenden Patches
- **Panels**: Keine scharfen Kanten an Nahtkreuzungen
- **Beschlagösen**: Keine vorstehenden Metallteile, die den Snuffer-Strumpf beschädigen
- **Segel-Breite**: Maximale Mittelbreite muss zum Snuffer-Durchmesser passen

#### 4.5.2 Snuffer-Kompatibilitätsmatrix

| Snuffer-Durchmesser (mm) | Max. Segelfläche (m²) | Max. Tuchgewicht (oz) |
|--------------------------|----------------------|----------------------|
| 150 | 40 | 0,75 |
| 200 | 70 | 1,0 |
| 250 | 110 | 1,5 |
| 300 | 160 | 1,5 |
| 350 | 220 | 2,0 |
| 400 | 300 | 2,0 |

### 4.6 Kennzeichnungspflicht

Gemäß ORC/IRC-Regeln müssen Spinnaker folgende Markierungen tragen:

- **Segelzeichen**: im oberen Drittel, Mindestgröße abhängig von Segelfläche
- **Segelnummer**: unter dem Segelzeichen
- **Nationale Buchstaben**: über der Segelnummer
- **Vermessungsmarken**: Kopf, Hals, Schothorn, Mittelpunkt (Regatta)
- **Herstellerangabe**: Firmenlogo an Kopf-Patch (optional)

---

## 5. Trimm und Handling

### 5.1 Symmetrischer Spinnaker — Trimm

#### 5.1.1 Spinnakerbaum-Einstellung

**Baumhöhe (Topping-Lift):**
- Grundregel: Beide Schothorn-Ecken auf gleicher Höhe
- Hals (Luv-Ecke am Baum) = Schothorn (Lee-Ecke an der Schot)
- Baum zu hoch → Segel wird instabil, kippt nach Lee
- Baum zu tief → Vorliek knickt, Segel kollabiert
- Feineinstellung: Baum 5–10 cm variieren, Luvliek beobachten

**Baumwinkel (Achterholer / Guy):**
- Grundregel: Baum 90° zum scheinbaren Wind
- Praktisch: Baum so weit achterlich wie möglich, bevor Luvliek einfällt
- Baum zu weit achterlich → Segel wird vom Groß abgedeckt
- Baum zu weit vorlich → Spinnaker steht nicht frei

**Baumniederholer (Foreguy/Downhaul):**
- Verhindert das Hochsteigen des Baums
- Muss unter Last bedienbar sein
- Spannung: so wenig wie nötig, um Baum stabil zu halten

#### 5.1.2 Schot-Trimm

**Schot (Lee-Schot):**
- Kontinuierlich trimmen (Spinnaker-Trimm = Vollzeit-Job!)
- Grundregel: Schot fieren, bis Luvliek gerade anfängt zu kippen
- Dann 10–15 cm dichter nehmen
- Bei Böen: 30–50 cm fieren lassen
- Schot-Führung: über die Leeseite, so weit achtern wie möglich
- Barberholer: reguliert die vertikale Schot-Führung

**Guy (Luv-Schot / Achterholer):**
- Fixiert die Position des Baumhalters
- Wird über den Achterholer (Tweaker) geführt
- Feineinstellung der Baumposition

#### 5.1.3 Fall-Trimm

- Spinnaker immer vollständig durchsetzen
- Fall nie am Mast belegen, sondern an der Winsch
- Markierung am Fall für exakte Höhe
- Bei Leichtwind: Fall 5–10 cm fieren für mehr Projektion

#### 5.1.4 Profil-Kontrolle

| Windstärke | Bauchlage | Baumhöhe | Schot-Druck |
|-----------|-----------|----------|-------------|
| 4–8 kn | 50–55 % | Höher (Ecken gleich) | Leicht, Achterliek offen |
| 8–14 kn | 45–50 % | Standard (Ecken gleich) | Mittel |
| 14–20 kn | 40–45 % | Standard bis tiefer | Dichter, Achterliek kontrolliert |
| 20–25 kn | 35–40 % | Tiefer | Dicht, Stabilität > Leistung |

### 5.2 Asymmetrischer Spinnaker / Gennaker — Trimm

#### 5.2.1 Halsleine (Tack Line)

Die Halsleine ist das Haupttrimmwerkzeug des asymmetrischen Spinnakers:

- **Durchgesetzt (kurz)**: Vorliek straff, flacheres Profil, höher am Wind
- **Gefiert (lang)**: Vorliek lockerer, volleres Profil, tiefer am Wind
- **Faustregel**: 1 m Halsleine fieren = ca. 5–8° tieferer Windwinkel möglich

**Einstellbereiche:**
| TWA | Halsleine | Profil |
|-----|-----------|--------|
| 80–100° | Kurz (durchgesetzt) | Flach, vorsegel-ähnlich |
| 100–120° | Mittel | Moderate Bauchtiefe |
| 120–140° | Lang (50–100 cm gefiert) | Voll, großer Bauch |
| 140–160° | Sehr lang (100–200 cm gefiert) | Sehr voll, max. Fläche |

#### 5.2.2 Schot-Trimm

- Gleiche Grundregel wie symmetrischer Spinnaker
- Schot fieren bis Luvliek kippt, dann 10–15 cm dichter
- Schot-Führung: Lee-Seite, Position variabel (Barberholer)
- Bei Halbwind (TWA 80–110°): Schot weiter vorne (wie Genua-Schot)
- Bei Raumwind (TWA 120–150°): Schot weiter achtern

#### 5.2.3 Bugspriet-Effekt

Der Bugspriet vergrößert den effektiven J-Wert und damit den Abstand des Segels zum Vorstag:

- **Ohne Bugspriet**: Segel steht nah am Vorstag, Scheuergefahr
- **Kurzer Bugspriet (1,0–1,5 m)**: Standardlösung, ausreichend für die meisten Gennaker
- **Langer Bugspriet (1,5–2,5 m)**: Für große Gennaker und Code 0
- **Ausfahrbarer Bugspriet**: Einfahrbar wenn nicht benötigt, Selden Bowsprit Kit

### 5.3 Code 0 — Trimm

#### 5.3.1 Besonderheiten

Der Code 0 wird wie ein Vorsegel getrimmt, nicht wie ein Spinnaker:

- **Schot-Führung**: Ähnlich wie Genua, aber weiter außen (auf dem Schandeckel)
- **Schot-Winkel**: 12–18° zur Mittschiffslinie (flacher als Genua)
- **Fall**: Immer voll durchgesetzt
- **Halsleine**: Immer voll durchgesetzt (straff)
- **Profil**: Flach, kontrolliert, vorsegel-ähnlich

#### 5.3.2 Furling-Betrieb

- **Unfurlen**: Schot in Lee vorbereitet, Furlleine lösen, Schot dichtnehmen
- **Furlen**: Schot kontrolliert fieren, Furlleine gleichzeitig dichtnehmen
- **Wichtig**: Nie gegen den Wind furlen (zu viel Last auf Furler!)
- **Windlimit**: Furlen bei max. 14–16 kn TWS (je nach System)
- **Wickelrichtung**: Muss mit Torsionsseil-Richtung übereinstimmen

#### 5.3.3 Problemlösung beim Furlen

| Problem | Ursache | Lösung |
|---------|---------|--------|
| Segel furlt nicht ein | Zu viel Wind | Abfallen, Last reduzieren |
| Segel furlt ungleichmäßig | Torsionsseil-Spannung falsch | Halsleine adjustieren |
| Segel furlt nur oben | Unteres Torsionsseil verschlissen | Torsionsseil prüfen/ersetzen |
| Segel öffnet sich beim Furlen | Schot zu dicht | Schot schneller fieren |
| Stundenglasform beim Furlen | Zu schnell gefurlt | Langsamer furlen, Schot kontrollieren |

### 5.4 Halsen

#### 5.4.1 Symmetrischer Spinnaker — Dip-Pole-Halse

Die Dip-Pole-Halse (Baum durch den Vordreieck tauchen) ist das Standardmanöver für
Yachten mit innerer Vorstag-Befestigung:

**Ablauf:**
1. Kurs: Toter Vorwind (TWA 170–180°)
2. Topping etwas ansetzen, Niederholer lösen
3. Baum-Nock vom Guy lösen (Trip-Line oder Schnapper)
4. Baum nach innen holen, unter dem Vorstag durchtauchen
5. Neuen Guy in Baum-Nock einhaken
6. Baum nach Lee ausfahren (neuer Guy)
7. Alte Schot wird neuer Guy, alter Guy wird neue Schot
8. Topping und Niederholer nachstellen
9. Neuen Kurs anliegen

**Crew-Anforderung:** Mindestens 3 Personen (Steuermann, Baum, Schoten)

#### 5.4.2 Symmetrischer Spinnaker — End-for-End-Halse

Für kleinere Yachten (bis ca. 35 ft) mit abnehmbarem Baum:

**Ablauf:**
1. Kurs: Toter Vorwind
2. Baum-Nock vom Guy lösen
3. Baum vom Mast lösen
4. Baum auf die andere Seite bringen
5. Baum am Mast befestigen
6. Baum-Nock am neuen Guy befestigen
7. Schoten wechseln

**Crew-Anforderung:** 2–3 Personen

#### 5.4.3 Asymmetrischer Spinnaker / Gennaker — Halse

Deutlich einfacher als die symmetrische Halse:

**Ablauf:**
1. Abfallen auf tiefen Raumwindkurs
2. Alte Schot (Lee) fieren
3. Segel wandert um das Vorstag herum (oder darunter durch)
4. Neue Schot (neue Lee-Seite) dichtnehmen
5. Neuen Kurs anliegen

**Varianten:**
- **Innen-Halse**: Segel wandert zwischen Vorstag und Mast → sauberer
- **Außen-Halse**: Segel wandert vor dem Vorstag → einfacher, aber Scheuergefahr

**Crew-Anforderung:** 1–2 Personen (Steuermann + Schot-Trimmer)

### 5.5 Setzen und Bergen

#### 5.5.1 Konventionelles Setzen (ohne Snuffer)

**Symmetrischer Spinnaker:**
1. Segel im Luv-Seitengang oder in der Bugluke vorbereiten
2. Kopf, Hals und Schothorn identifizieren und sortieren
3. Baum vorbereiten (Topping, Niederholer, Guy)
4. Fall anschlagen, Guy und Schot anschlagen
5. Baum am Mast befestigen, Guy in Baum-Nock
6. „Hoch!" — Fall durchsetzen, Guy und Schot simultan trimmen
7. Groß wird ggf. gefiert oder eingeholt

**Asymmetrischer Spinnaker:**
1. Segel am Bugspriet/Bug vorbereiten
2. Halsleine anschlagen, Schoten (Lee und Luv) anschlagen
3. Fall anschlagen
4. „Hoch!" — Fall durchsetzen, Schot trimmen, Halsleine einstellen
5. Genua einrollen

#### 5.5.2 Bergen (ohne Snuffer)

**Symmetrischer Spinnaker:**
1. Baum nach vorne schwenken (Guy fieren)
2. Lee-Schot fieren
3. Segel flattert frei hinter dem Groß
4. Crew greift die Schot oder das Achterliek
5. Segel wird hinter dem Groß eingeholt
6. Fall kontrolliert fieren
7. Segel unter Deck oder in den Segel-Beutel

**Asymmetrischer Spinnaker:**
1. Schot fieren
2. Segel flattert im Windschatten des Groß
3. Halsleine fieren (Segel kommt ans Deck)
4. Segel am Vorliek einsammeln
5. Fall fieren

#### 5.5.3 Setzen und Bergen mit Snuffer/Sock

**Setzen:**
1. Segel im Snuffer-Strumpf am Fall befestigt
2. Fall durchsetzen (Segel steigt im Strumpf auf)
3. Snuffer-Leine ziehen → Strumpf fährt hoch, Segel entfaltet sich
4. Schot trimmen

**Bergen:**
1. Schot fieren
2. Snuffer-Leine ziehen → Strumpf fährt herunter, umhüllt das Segel
3. Fall fieren (optional — Segel kann im Strumpf oben bleiben)

**Vorteile des Snuffer-Systems:**
- Einhand-tauglich (Setzen und Bergen vom Cockpit)
- Segel wird nie lose am Deck (kein Wasser-Kontakt)
- Bergung bei bis zu 25 kn TWS möglich
- UV-Schutz wenn Segel im Strumpf bleibt

#### 5.5.4 Top-Down-Furler

**Funktionsprinzip:**
- Segel wird von oben nach unten aufgerollt
- Torsionsseil im Vorliek überträgt die Drehung
- Furltrommel am Kopf (Karver, Facnor) oder am Fuß (Selden)
- Furlleine wird vom Cockpit bedient

**Setzen:**
1. Furlleine lösen
2. Schot dichtnehmen → Segel entrollt sich
3. Trimmen

**Bergen:**
1. Schot kontrolliert fieren
2. Furlleine dichtnehmen → Segel rollt sich auf
3. Fertig (Segel bleibt aufgerollt am Vorstag/Bugspriet)

### 5.6 Broach-Recovery

#### 5.6.1 Erkennung

Ein Broach (unkontrollierte Drehung in den Wind mit extremer Krängung) kündigt sich an durch:

- Steigenden Ruderdruck (Lee-Giermoment)
- Zunehmende Krängung trotz Abfallen
- Wetter-Ruder wird wirkungslos
- Boot beschleunigt unkontrolliert in der Bö

#### 5.6.2 Sofortmaßnahmen

1. **Schot werfen!** (Lee-Spinnaker-Schot sofort komplett freigeben)
2. Ruder mittschiffs oder leicht nach Lee
3. Groß fieren
4. Crew nach Luv
5. Wenn Segel im Wasser: NICHT sofort bergen, erst Boot stabilisieren
6. Dann kontrolliert bergen

#### 5.6.3 Prävention

- Rechtzeitiges Reffen des Groß bei steigendem Wind
- Ständiger Schottrimm (nie Schot belegen!)
- Kurs anpassen (tieferer Vorwindkurs = weniger Broach-Risiko)
- Bei Böen sofort Schot fieren
- Spinnaker rechtzeitig bergen (bevor es kritisch wird)

---

## 6. Hardware

### 6.1 Spinnakerbaum

#### 6.1.1 Materialien und Typen

| Typ | Material | Gewicht (kg/m) | Steifigkeit | Preis-Index | Einsatz |
|-----|----------|----------------|------------|-------------|---------|
| Standard-Rohr | Aluminium 6082-T6 | 1,8–2,5 | Mittel | 100 | Fahrt, Club-Regatta |
| Leicht-Rohr | Aluminium 7075-T6 | 1,2–1,8 | Mittel-Hoch | 130 | Regatta |
| Carbon-Rohr | CFK (Prepreg) | 0,6–1,0 | Sehr hoch | 350 | Regatta, Performance |
| Teleskop-Alu | Aluminium 6082 | 2,5–3,5 | Mittel | 120 | Fahrt (flexibel) |
| Teleskop-Carbon | CFK + Alu | 1,0–1,8 | Hoch | 400 | Performance Cruiser |

#### 6.1.2 Dimensionierung

| Bootslänge (ft) | Baum-Länge (m) | Rohrdurchmesser (mm) | Wandstärke (mm) |
|-----------------|----------------|---------------------|-----------------|
| 25–30 | 2,5–3,5 | 70–80 | 2,0–2,5 |
| 30–35 | 3,5–4,5 | 80–90 | 2,5–3,0 |
| 35–40 | 4,5–5,5 | 90–100 | 3,0–3,5 |
| 40–45 | 5,5–6,5 | 100–120 | 3,0–4,0 |
| 45–50 | 6,5–7,5 | 120–140 | 3,5–4,5 |
| 50–60 | 7,5–9,0 | 140–160 | 4,0–5,0 |

#### 6.1.3 Beschläge am Spinnakerbaum

**Mast-Ende (Inboard End):**
- Gabelkopf (Fork) auf Mastbeschlag (Kugel/Ring-System)
- Drehgelenk mit vertikalem und horizontalem Freiheitsgrad
- Arretierung: Bolzen oder Federschnapper
- Hersteller: Forespar, Selden, RWO, Schaefer

**Nock-Ende (Outboard End):**
- Öffnungsmechanismus: Trip-Line oder Federschnapper
- Öse/Gabelkopf für Guy-Befestigung
- Hersteller: Forespar, Selden, Ronstan

#### 6.1.4 Preise Spinnakerbaum (Stand 2026)

| Hersteller | Modell | Länge (m) | Material | Preis EUR |
|-----------|--------|-----------|----------|-----------|
| Forespar | Standard | 3,0 | Aluminium | 680–850 |
| Forespar | Standard | 4,0 | Aluminium | 850–1.100 |
| Forespar | Standard | 5,0 | Aluminium | 1.100–1.400 |
| Forespar | Ultralight | 3,5 | Aluminium 7075 | 1.200–1.600 |
| Forespar | Ultralight | 4,5 | Aluminium 7075 | 1.600–2.100 |
| Selden | Carbon | 3,0 | Carbon | 2.800–3.500 |
| Selden | Carbon | 4,0 | Carbon | 3.500–4.500 |
| Selden | Carbon | 5,0 | Carbon | 4.500–5.800 |
| Forespar | Twist-Lock Tele | 3,0–4,5 | Aluminium | 1.400–1.800 |
| Forespar | Twist-Lock Tele | 4,0–6,0 | Aluminium | 1.800–2.400 |

### 6.2 Bugspriet

#### 6.2.1 Typen

**Feststehend (Fixed Bowsprit):**
- Dauerhaft montierter GFK- oder Carbon-Sprit
- Integriert in Bugbeschlag oder Ankerrolle
- Länge: 1,0–3,0 m (je nach Bootsgröße)
- Typisch bei Performance-Cruisern und Regattayachten

**Einfahrbar/Teleskop (Retractable):**
- In den Rumpf oder Deck einfahrbar
- Aluminium- oder Carbon-Rohr in GFK-Führung
- Länge: 1,0–2,5 m (ausgefahren)
- Ideal für Fahrtenyachten (kein Bugspriet im Hafen)

**Abnehmbar:**
- Steckbarer Sprit in Deck-Buchse
- Aluminium oder Carbon
- Wird nur bei Bedarf montiert
- Einfachste Nachrüstlösung

#### 6.2.2 Selden Bowsprit Kit

Das Selden Bowsprit Kit ist die meistverkaufte Nachrüstlösung:

| Modell | Bootslänge | Sprit-Länge (m) | Material | Preis EUR |
|--------|-----------|-----------------|----------|-----------|
| Selden BSK 406 | 28–34 ft | 1,2 | Aluminium/Carbon | 1.800–2.200 |
| Selden BSK 508 | 34–40 ft | 1,5 | Aluminium/Carbon | 2.200–2.800 |
| Selden BSK 610 | 40–48 ft | 1,8 | Carbon | 3.200–4.000 |
| Selden BSK 810 | 48–60 ft | 2,2 | Carbon | 4.500–5.800 |

**Lieferumfang:**
- Bugspriet-Rohr mit Endkappe
- Deck-Montageplatte (Edelstahl oder Aluminium)
- Bobstay-Befestigung
- Befestigungsbolzen und Dichtungen
- Montageanleitung

#### 6.2.3 Festigkeitsanforderungen

Der Bugspriet muss folgende Lasten aufnehmen:

- **Vertikallast (Halsleine)**: 2–8 kN (je nach Segelfläche)
- **Horizontallast (Schot)**: 1–5 kN
- **Biegelast**: Kombination aus Vertikal- und Horizontallast
- **Sicherheitsfaktor**: Mindestens 3:1

**Bobstay:**
- Unterstützt den Bugspriet gegen Hochbiegen
- Material: Edelstahl-Draht 5–8 mm oder Dyneema 8–12 mm
- Befestigung: Am Vorstevenfuß (Waterline) oder unter dem Bug
- Spannung: 500–2.000 N (Vorspannung)

### 6.3 Snuffer / Sock-Systeme

#### 6.3.1 Funktionsprinzip

Ein Snuffer (auch „Sock" oder „Dousing Sleeve") ist ein zylindrischer Strumpf aus leichtem
Tuch, der über das gesamte Segel gezogen werden kann. Durch Ziehen an einer Leine wird der
Strumpf hochgezogen (Segel entfaltet sich) oder heruntergelassen (Segel wird eingehüllt).

#### 6.3.2 Hersteller und Modelle

| Hersteller | Modell | Segelfläche (m²) | Durchmesser (mm) | Preis EUR |
|-----------|--------|------------------|-------------------|-----------|
| ATN | Tacker | 30–50 | 200 | 450–650 |
| ATN | Tacker | 50–80 | 250 | 650–850 |
| ATN | Tacker | 80–120 | 300 | 850–1.100 |
| ATN | Tacker | 120–180 | 350 | 1.100–1.500 |
| ATN | Tacker | 180–300 | 400 | 1.500–2.200 |
| Chutescoop | Standard | 30–50 | 200 | 380–550 |
| Chutescoop | Standard | 50–80 | 250 | 550–750 |
| Chutescoop | Standard | 80–120 | 300 | 750–1.000 |
| Robline/Marlow | Snuffer Kit | 40–70 | 220 | 320–480 |
| Robline/Marlow | Snuffer Kit | 70–110 | 280 | 480–680 |

#### 6.3.3 Aufbau eines Snuffer-Systems

**Komponenten:**
1. **Strumpf/Sock**: Zylindrischer Nylon-Schlauch, leichtgewichtig
2. **Ringführung**: Edelstahl- oder Kunststoffring am unteren Ende
3. **Bergeleine**: Polyester oder Dyneema, 6–8 mm
4. **Kopfstück**: Verbindung zum Segel-Fall, mit Wirbel
5. **Stopper**: Begrenzung der oberen Position

#### 6.3.4 Wartung

- Strumpf nach Saison waschen (Süßwasser, mildes Waschmittel)
- Ringführung auf Grat und Korrosion prüfen
- Bergeleine auf Verschleiß prüfen (jährlich)
- Wirbel schmieren (Teflon-Spray)
- UV-Schutz: Strumpf einpacken wenn nicht in Gebrauch

### 6.4 Furler-Systeme

#### 6.4.1 Top-Down-Furler — Detailvergleich

| Hersteller | Modell | Segelfläche (m²) | Furltrommel | Gewicht (kg) | Preis EUR |
|-----------|--------|------------------|------------|-------------|-----------|
| Karver | KF-1 | 20–40 | Kopf | 2,2 | 1.800–2.400 |
| Karver | KF-3 | 40–70 | Kopf | 3,5 | 2.800–3.500 |
| Karver | KF-5 | 70–110 | Kopf | 5,2 | 3.500–4.500 |
| Karver | KF-7 | 110–160 | Kopf | 7,0 | 4.800–6.200 |
| Karver | KF-10 | 160–250 | Kopf | 10,5 | 6.500–8.500 |
| Facnor | FX-1500 | 20–35 | Kopf | 2,0 | 1.600–2.200 |
| Facnor | FX-2500 | 35–60 | Kopf | 4,8 | 3.200–4.000 |
| Facnor | FX-4500 | 60–100 | Kopf | 6,5 | 4.200–5.500 |
| Facnor | FX-7000 | 100–160 | Kopf | 8,5 | 5.800–7.500 |
| Selden | GX-15 | 20–40 | Fuß | 3,5 | 2.200–2.800 |
| Selden | GX-25 | 40–70 | Fuß | 5,0 | 3.000–4.200 |
| Selden | GX-35 | 70–110 | Fuß | 6,5 | 4.000–5.500 |
| Ronstan | FurlBoom S | 25–45 | Kopf | 2,5 | 1.900–2.600 |
| Ronstan | FurlBoom M | 45–75 | Kopf | 3,8 | 2.500–3.800 |
| Ronstan | FurlBoom L | 75–120 | Kopf | 5,5 | 3.800–5.200 |
| Profurl | C250 | 20–35 | Kopf | 2,3 | 1.700–2.300 |
| Profurl | C350 | 35–60 | Kopf | 4,2 | 2.900–3.800 |
| Profurl | C490 | 60–100 | Kopf | 6,0 | 3.800–5.200 |
| Profurl | C700 | 100–160 | Kopf | 8,8 | 5.500–7.200 |

#### 6.4.2 Furler-Wartung

**Jährlich:**
- Furltrommel demontieren, reinigen, schmieren
- Lager auf Spiel und Korrosion prüfen
- Furlleine auf Verschleiß prüfen
- Torsionsseil auf Kinks und Abrieb prüfen
- Alle Bolzen und Schäkel auf festen Sitz prüfen

**Alle 3–5 Jahre:**
- Lager tauschen
- Furlleine erneuern
- Torsionsseil prüfen lassen (ggf. tauschen)

**Alle 8–10 Jahre:**
- Komplettes Service beim Hersteller
- Trommel und Swivel tauschen (Verschleiß)

### 6.5 Schoten

#### 6.5.1 Material und Dimensionierung

| Bootslänge (ft) | Schot-Durchmesser (mm) | Material | Bruchlast (kN) | Preis EUR/m |
|-----------------|----------------------|----------|-----------------|-------------|
| 25–30 | 8–10 | Polyester geflochten | 15–25 | 2,50–4,00 |
| 25–30 | 6–8 | Dyneema SK78 | 20–35 | 8,00–14,00 |
| 30–36 | 10–12 | Polyester geflochten | 25–40 | 3,50–5,50 |
| 30–36 | 8–10 | Dyneema SK78 | 35–55 | 12,00–20,00 |
| 36–42 | 12–14 | Polyester geflochten | 40–60 | 5,00–7,50 |
| 36–42 | 10–12 | Dyneema SK78 | 55–80 | 18,00–28,00 |
| 42–50 | 14–16 | Polyester geflochten | 60–85 | 7,00–10,00 |
| 42–50 | 12–14 | Dyneema SK78 | 80–120 | 25,00–40,00 |
| 50–60 | 16–18 | Polyester geflochten | 85–120 | 9,00–14,00 |
| 50–60 | 14–16 | Dyneema SK78 | 120–180 | 35,00–55,00 |

#### 6.5.2 Schot-Länge

- **Symmetrischer Spinnaker**: 2 × (LOA + Masthöhe) pro Schot/Guy
- **Asymmetrischer Spinnaker**: 2 × (LOA + 50 %) pro Schot
- **Code 0**: 1,5 × LOA pro Schot

#### 6.5.3 Empfehlungen

- **Fahrt**: Polyester-Kern mit Dyneema-Mantel (Hybrid) — bester Kompromiss
- **Regatta**: Volldyneema SK78 — leicht, griffig, teuer
- **Budget**: Doppelgeflecht Polyester — günstig, bewährt, schwerer
- **Immer**: Handschuhe beim Spinnaker-Trimm tragen!

### 6.6 Launcher-Tubes (Spinnaker-Schacht)

#### 6.6.1 Konzept

Ein Launcher-Tube ist ein fest eingebauter Schacht vom Cockpit/Deck zum Bug, durch den
der Spinnaker gesetzt und geborgen wird. Das Segel wird durch den Schacht nach vorne
gedrückt (Setzen) oder nach achtern gezogen (Bergen).

**Vorteile:**
- Schnelles Setzen und Bergen
- Kein Crew-Einsatz am Vordeck nötig
- Segel bleibt trocken
- Standard bei Regattayachten

**Nachteile:**
- Fest eingebaut, benötigt Platz im Vorschiff
- Wrap-Gefahr im Schacht
- Nachrüstung schwierig
- Nur für symmetrische Spinnaker geeignet

#### 6.6.2 Dimensionierung

| Bootslänge | Schacht-Durchmesser (mm) | Schacht-Länge (m) |
|------------|-------------------------|--------------------|
| 25–30 ft | 150–200 | 3,0–4,0 |
| 30–36 ft | 200–250 | 4,0–5,0 |
| 36–42 ft | 250–300 | 5,0–6,0 |
| 42–50 ft | 300–350 | 6,0–7,0 |

---

## 7. Hersteller

### 7.1 North Sails

#### 7.1.1 Unternehmenprofil

North Sails ist der weltweit größte Segelhersteller mit Produktionsstätten in den USA,
Europa (Spanien, Italien), Sri Lanka und Australien. Im Bereich Spinnaker und Gennaker
bietet North eine vollständige Produktpalette von Regatta bis Cruising.

#### 7.1.2 Produktlinien

**North NorDac Nylon:**
- Hauseigenes Nylon-Tuch
- Gewichte: 0,5 oz bis 2,2 oz
- Spezielle Beschichtung für geringere Porosität
- Verfügbar in 20+ Farben

**North 3Di Downwind:**
- Hochleistungs-Laminat für Code 0
- Filament-basierte Konstruktion
- Geringster Stretch aller Code-0-Materialien
- Nur für Regatta und Superyachten

**Spinnaker-Modelle:**

| Modell | Typ | TWA | TWS (kn) | Material | Preis 36 ft EUR |
|--------|-----|-----|----------|----------|----------------|
| North S1 | Symm. Runner | 140–180° | 4–12 | NorDac 0,5 oz | 3.200–4.000 |
| North S2 | Symm. Allround | 120–170° | 8–22 | NorDac 0,75 oz | 3.500–4.500 |
| North S3 | Symm. Heavy | 120–170° | 15–30 | NorDac 1,5 oz | 3.800–5.000 |
| North A2 | Asym. Reaching | 80–140° | 6–18 | NorDac 0,75 oz | 3.200–4.200 |
| North A3 | Asym. Heavy | 90–155° | 12–25 | NorDac 1,5 oz | 3.500–4.500 |
| North A4 | Asym. Runner | 120–180° | 10–22 | NorDac 1,2 oz | 3.400–4.400 |
| North Code 0 | Furling Reacher | 55–90° | 4–16 | 3Di/CZ | 5.500–8.500 |
| North Headsail 0 | Code 0 Cruising | 55–85° | 4–14 | CZ-100 | 4.800–6.500 |
| North Gennaker | Cruising | 80–140° | 6–20 | NorDac 1,0 oz | 3.000–4.000 |
| North MPS | Allround | 80–160° | 6–20 | NorDac 1,0 oz | 3.200–4.200 |

### 7.2 Elvström Sails

#### 7.2.1 Unternehmensprofil

Elvström Sails, gegründet von Paul Elvström, ist ein dänischer Hersteller mit
Produktionsstätten in Dänemark und Asien. Bekannt für hohe Qualität und Innovation
im Fahrtensegel-Bereich.

#### 7.2.2 Spinnaker-Produkte

| Modell | Typ | TWA | TWS (kn) | Material | Preis 36 ft EUR |
|--------|-----|-----|----------|----------|----------------|
| Elvström EPEX S | Symm. Spinnaker | 130–180° | 6–22 | Nylon 0,75 oz | 2.800–3.500 |
| Elvström EPEX A | Asym. Gennaker | 80–150° | 6–20 | Nylon 0,75–1,0 oz | 2.600–3.300 |
| Elvström EPEX C0 | Code 0 | 55–90° | 4–16 | Pentex-Laminat | 4.500–6.000 |
| Elvström Cruising G | Cruising Gennaker | 85–140° | 6–18 | Nylon 1,0 oz | 2.200–2.800 |
| Elvström MPS | Multi-Purpose | 80–155° | 6–20 | Nylon 1,0 oz | 2.500–3.200 |

### 7.3 Doyle Sails

#### 7.3.1 Unternehmensprofil

Doyle Sails ist ein neuseeländischer Hersteller mit globalem Netzwerk. Bekannt für die
Stratis-Technologie (gespreitete Fasern auf Film) und hochwertige Cruising-Segel.

#### 7.3.2 Spinnaker-Produkte

| Modell | Typ | TWA | TWS (kn) | Preis 36 ft EUR |
|--------|-----|-----|----------|----------------|
| Doyle Stratis Code 0 | Code 0 | 55–90° | 4–16 | 5.800–7.500 |
| Doyle Centric A-Spi | Asym. Allround | 80–150° | 6–20 | 3.000–3.800 |
| Doyle Centric S-Spi | Symm. Allround | 120–180° | 6–22 | 3.200–4.000 |
| Doyle Cruising Gennaker | Cruising | 85–140° | 6–18 | 2.400–3.200 |
| Doyle Delta Drifter | Leichtwind Code 0 | 60–95° | 3–12 | 4.800–6.200 |

### 7.4 Quantum Sails

#### 7.4.1 Unternehmensprofil

Quantum Sails ist ein US-amerikanischer Hersteller mit Produktionsstätten weltweit.
Bekannt für die Fusion-M-Technologie und eine starke Präsenz im Fahrtensegel-Markt.

#### 7.4.2 Spinnaker-Produkte

| Modell | Typ | TWA | TWS (kn) | Preis 36 ft EUR |
|--------|-----|-----|----------|----------------|
| Quantum Fusion M Code 0 | Code 0 | 55–90° | 4–16 | 5.200–6.800 |
| Quantum A-Spi | Asym. Reaching | 80–145° | 6–20 | 2.800–3.600 |
| Quantum S-Spi | Symm. Allround | 125–180° | 6–22 | 3.000–3.800 |
| Quantum Gennaker | Cruising | 85–140° | 6–18 | 2.400–3.000 |
| Quantum MPS | Multi-Purpose | 80–155° | 6–20 | 2.600–3.400 |

### 7.5 UK Sailmakers

#### 7.5.1 Spinnaker-Produkte

| Modell | Typ | TWA | TWS (kn) | Preis 36 ft EUR |
|--------|-----|-----|----------|----------------|
| UK Tape-Drive Code 0 | Code 0 | 55–90° | 4–16 | 4.800–6.200 |
| UK X-Drive Spi | Asym./Symm. | variabel | 6–22 | 2.600–3.500 |
| UK Cruising Gennaker | Cruising | 85–140° | 6–18 | 2.000–2.600 |

### 7.6 OneSails

#### 7.6.1 Unternehmensprofil

OneSails ist ein internationales Netzwerk mit Produktion in Italien (Segel) und eigener
Tuchherstellung (4T Forte). Bekannt für die einzigartige 4T-Forte-Membrantechnologie.

#### 7.6.2 Spinnaker-Produkte

| Modell | Typ | TWA | TWS (kn) | Preis 36 ft EUR |
|--------|-----|-----|----------|----------------|
| OneSails 4T Code 0 | Code 0 | 55–90° | 4–16 | 5.000–6.500 |
| OneSails MPS | Multi-Purpose | 80–155° | 6–20 | 2.800–3.600 |
| OneSails Gennaker | Cruising | 85–140° | 6–18 | 2.400–3.000 |
| OneSails A-Spi | Asym. Reaching | 80–145° | 6–20 | 2.800–3.500 |

### 7.7 Rolly Tasker Sails

#### 7.7.1 Unternehmensprofil

Rolly Tasker Sails ist ein thailändischer Hersteller mit über 45 Jahren Erfahrung.
Bekannt für gutes Preis-Leistungs-Verhältnis, insbesondere im Fahrtensegel-Segment.

#### 7.7.2 Spinnaker-Produkte

| Modell | Typ | TWA | TWS (kn) | Preis 36 ft EUR |
|--------|-----|-----|----------|----------------|
| Rolly Tasker S-Spi | Symm. Allround | 125–180° | 6–22 | 1.800–2.400 |
| Rolly Tasker A-Spi | Asym. Reaching | 80–145° | 6–20 | 1.600–2.200 |
| Rolly Tasker Code 0 | Code 0 | 55–90° | 4–16 | 3.200–4.200 |
| Rolly Tasker Gennaker | Cruising | 85–140° | 6–18 | 1.400–1.900 |
| Rolly Tasker MPS | Multi-Purpose | 80–155° | 6–20 | 1.600–2.100 |

### 7.8 Preisvergleich 36 ft — Alle Hersteller

| Segeltyp | North | Elvström | Doyle | Quantum | UK | OneSails | Rolly Tasker |
|----------|-------|----------|-------|---------|-----|----------|-------------|
| Symm. Spi | 3.500 | 2.800 | 3.200 | 3.000 | 2.600 | — | 1.800 |
| Asym. Spi | 3.200 | 2.600 | 3.000 | 2.800 | 2.600 | 2.800 | 1.600 |
| Gennaker | 3.000 | 2.200 | 2.400 | 2.400 | 2.000 | 2.400 | 1.400 |
| Code 0 | 5.500 | 4.500 | 5.800 | 5.200 | 4.800 | 5.000 | 3.200 |
| MPS | 3.200 | 2.500 | — | 2.600 | — | 2.800 | 1.600 |

(Preise in EUR, Mittelwerte, Stand 2026, 36-ft-Yacht, ohne Montage)

### 7.9 Preisvergleich 44 ft

| Segeltyp | North | Elvström | Doyle | Quantum | UK | OneSails | Rolly Tasker |
|----------|-------|----------|-------|---------|-----|----------|-------------|
| Symm. Spi | 5.200 | 4.200 | 4.800 | 4.500 | 3.900 | — | 2.700 |
| Asym. Spi | 4.800 | 3.900 | 4.500 | 4.200 | 3.900 | 4.200 | 2.400 |
| Gennaker | 4.500 | 3.300 | 3.600 | 3.600 | 3.000 | 3.600 | 2.100 |
| Code 0 | 8.200 | 6.800 | 8.700 | 7.800 | 7.200 | 7.500 | 4.800 |
| MPS | 4.800 | 3.800 | — | 3.900 | — | 4.200 | 2.400 |

### 7.10 Preisvergleich 50 ft

| Segeltyp | North | Elvström | Doyle | Quantum | UK | OneSails | Rolly Tasker |
|----------|-------|----------|-------|---------|-----|----------|-------------|
| Symm. Spi | 7.500 | 6.000 | 6.800 | 6.500 | 5.600 | — | 3.800 |
| Asym. Spi | 6.800 | 5.500 | 6.200 | 6.000 | 5.500 | 6.000 | 3.400 |
| Gennaker | 6.200 | 4.800 | 5.200 | 5.000 | 4.200 | 5.000 | 3.000 |
| Code 0 | 12.000 | 9.500 | 12.500 | 11.500 | 10.500 | 11.000 | 7.000 |
| MPS | 6.800 | 5.200 | — | 5.500 | — | 6.000 | 3.400 |

---

## 8. Fehlerbild-Atlas

### 8.1 Übersicht

| Code | Bezeichnung | Schwere | Häufigkeit |
|------|------------|---------|-----------|
| F-16_04-01 | Riss bei Patenthalse | KRITISCH | Mittel |
| F-16_04-02 | Nylon-UV-Degradation | HOCH | Sehr häufig |
| F-16_04-03 | Torsionsseil-Versagen | KRITISCH | Selten |
| F-16_04-04 | Wickler / Wrap | HOCH | Häufig |
| F-16_04-05 | Bugspriet-Ausriss | KRITISCH | Selten |
| F-16_04-06 | Snuffer-Blockade | MITTEL | Häufig |
| F-16_04-07 | Schothorn-Ausriss | KRITISCH | Mittel |
| F-16_04-08 | Halskausch-Versagen | HOCH | Selten |
| F-16_04-09 | Baum-Bruch | KRITISCH | Selten |
| F-16_04-10 | Hourglassing | MITTEL | Häufig |
| F-16_04-11 | Tack-Line Chafe | HOCH | Häufig |
| F-16_04-12 | Luff-Tape Ablösung | HOCH | Mittel |

### 8.2 F-16_04-01 — Riss bei Patenthalse

#### Beschreibung
Ein Riss im Spinnaker-Tuch, der während einer unkontrollierten Halse (Patenthalse / Chinese Gybe)
entsteht. Die plötzliche Lastumkehr und das Schlagen des Segels führen zu Rissen entlang der
Nähte oder durch das Tuch.

#### Erscheinungsbild
- Riss typischerweise entlang einer Nahtlinie, ausgehend von einer Ecke
- Oft Dreiecksförmiger Riss von einem Patch-Rand
- Tuch um den Riss herum gedehnt und verformt
- Naht-Trennung auf 30–200 cm Länge

#### Ursachen
- Patenthalse bei Wind >15 kn
- Unbeabsichtigte Halse (Steuerfehler, Windsprung)
- Geschwächtes Tuch (UV, Alter)
- Unterdimensionierte Nähte
- Fehlende oder zu kleine Patches

#### Risikoerhöhung
- Alter des Segels >8 Jahre
- Sichtbare UV-Verfärbung
- Bereits reparierte Stellen
- Zu großer Spinnaker für die Windstärke

#### Prävention
- Nie auf Vorwindkurs ohne aktiven Trimmer segeln
- Präventivhalse bei Windaufnahme
- Segel rechtzeitig bergen
- Regelmäßige Inspektion der Nähte und Patches

#### Reparatur
- Kleine Risse (<30 cm): Spinnaker-Reparaturklebeband (sofort), dann Segelmacher-Naht
- Mittlere Risse (30–100 cm): Segelmacher-Reparatur mit Patch, 150–400 EUR
- Große Risse (>100 cm): Segelmacher-Bewertung, ggf. Neubau wirtschaftlicher
- Naht-Trennung: Nachnähen + Tape, 100–300 EUR

#### AYDI-Bewertung
- Confidence: `visual_medium` (Riss sichtbar auf Fotos)
- Schwere: KRITISCH (Segel nicht einsatzfähig)
- Empfehlung: „Segelmacher-Begutachtung erforderlich"

### 8.3 F-16_04-02 — Nylon-UV-Degradation

#### Beschreibung
UV-Strahlung zersetzt die Polyamid-Molekülketten im Nylon. Das Tuch wird spröde, verliert
Reißfestigkeit und verfärbt sich. Dies ist die häufigste Alterungserscheinung bei Spinnakern.

#### Erscheinungsbild
- Verfärbung: Weiß wird gelblich, Farben bleichen aus
- Tuch wird spröde und steif (verliert Geschmeidigkeit)
- „Knistergeräusch" beim Zusammenfalten
- Obere Panels stärker betroffen als untere
- Sonnenseite stärker als Schattenseite

#### Diagnosemethoden
- **Daumendrucktest**: Nagel mit mittlerem Druck gegen Tuch drücken
  - Nagel durchdringt Tuch → sofort ersetzen
  - Tuch gibt nach, kein Durchstich → noch brauchbar
  - Tuch widersteht → gut
- **Falttest**: Tuch scharf knicken und wieder öffnen
  - Weißer Knickstreifen → UV-Schaden, Fasern gebrochen
  - Kein Streifen → OK
- **Vergleichstest**: Gleiche Stelle an geschützter und ungeschützter Stelle vergleichen

#### Stadien

| Stadium | Alter (typisch) | Festigkeitsverlust | Maßnahme |
|---------|----------------|--------------------|---------  |
| 1 - Leicht | 3–5 Jahre | 10–20 % | Beobachten, UV-Schutz verbessern |
| 2 - Mittel | 5–8 Jahre | 20–40 % | Windlimit reduzieren |
| 3 - Stark | 8–12 Jahre | 40–60 % | Nur Leichtwind, Ersatz planen |
| 4 - Kritisch | >12 Jahre | >60 % | Nicht mehr segeln |

#### Prävention
- Segel nach Gebrauch sofort bergen und im Beutel verstauen
- Snuffer als UV-Schutz nutzen
- Helle Farben wählen (geringere UV-Absorption)
- PU-beschichtetes Nylon wählen
- Nicht trocknen lassen in der Sonne

#### AYDI-Bewertung
- Confidence: `visual_high` (auf Fotos gut erkennbar)
- Schwere: HOCH (schleichend, aber irreversibel)
- Empfehlung: „Daumendrucktest durchführen, Festigkeitstest durch Segelmacher"

### 8.4 F-16_04-03 — Torsionsseil-Versagen

#### Beschreibung
Das Torsionsseil im Vorliek eines Code-0- oder Furling-Gennakers versagt, sodass das Segel
nicht mehr gefurlt werden kann. Dies ist ein kritischer Defekt, da das Segel ohne Furler
nur schwer geborgen werden kann.

#### Erscheinungsbild
- Segel furlt nicht mehr gleichmäßig
- „Bauch" im Vorliek an der Versagensstelle
- Torsionsseil-Enden sichtbar am Vorliek
- Segel dreht sich nur noch im oberen oder unteren Bereich

#### Ursachen
- Materialermüdung nach vielen Furl-Zyklen (>1.000)
- Überbelastung (Furlen bei zu viel Wind)
- Korrosion (bei Edelstahl-Kern)
- UV-Degradation des Mantelgewebes
- Kink-Schaden durch falsches Aufwickeln

#### Sofortmaßnahmen bei Versagen auf See
1. Abfallen auf tiefen Vorwindkurs
2. Versuch, das Segel von Hand einzuholen (Crew am Vorstag)
3. Wenn nicht möglich: Halsleine lösen, Segel flattert frei
4. Segel am Achterliek einsammeln, am Deck sichern
5. Fall fieren

#### Prävention
- Torsionsseil alle 5 Jahre inspizieren lassen
- Nie bei >16 kn TWS furlen
- Furl-Richtung immer gleich (nicht alternierend)
- Seil nicht knicken oder unter Last biegen

#### Reparatur
- Torsionsseil komplett ersetzen: 400–1.200 EUR (je nach Länge und Material)
- Segel muss zum Segelmacher (Vorliek öffnen, neues Seil einziehen)
- Arbeitszeit: 4–8 Stunden
- Gesamtkosten: 800–2.500 EUR

### 8.5 F-16_04-04 — Wickler / Wrap

#### Beschreibung
Der Spinnaker wickelt sich um das Vorstag, die Wanten oder um sich selbst und kann nicht
mehr kontrolliert getrimmt oder geborgen werden.

#### Erscheinungsbild
- Segel umwickelt das Vorstag in Spiralform
- Oder: Segel wickelt sich um sich selbst (Stundenglasform)
- Schoten und Halsleine sind eingeklemmt
- Segel steht nicht mehr frei

#### Ursachen
- Zu viel Schot beim Bergen (Segel kommt vor das Vorstag)
- Schot um Vorstag gewickelt vor dem Setzen
- Windsprung während des Manövers
- Unkoordiniertes Halsen
- Genua nicht eingerollt vor Spinnaker-Setzen

#### Sofortmaßnahmen
1. NICHT weiter am Fall oder den Schoten ziehen!
2. Kurs auf toten Vorwind (Wind direkt von achtern)
3. Alle Schoten lösen, Segel soll frei wehen
4. Versuch, durch leichtes Anluven und wieder Abfallen das Segel zu lösen
5. Wenn das nicht hilft: Crew mit Bootshaken am Vorstag den Wickler lösen
6. Letzter Ausweg: Fall fieren und Segel ins Wasser, dann einsammelnen

#### Prävention
- Vor dem Setzen: alle Schoten frei von Hindernissen
- Genua vor Spinnaker-Setzen vollständig einrollen
- Klare Kommandos während des Manövers
- Windfahne/Windanzeiger permanent beobachten
- Bei mehr als 3 Wicklungen sofort das Fall kappen (Notfallschere bereithalten)

### 8.6 F-16_04-05 — Bugspriet-Ausriss

#### Beschreibung
Der Bugspriet löst sich aus seiner Decksbefestigung oder bricht, typischerweise bei
hoher dynamischer Belastung (Bö, Surfen, Broach).

#### Erscheinungsbild
- Bugspriet steht schief oder fehlt ganz
- Deckslaminat um die Montageplatte gerissen
- Bolzen ausgerissen oder verbogen
- Bobstay-Befestigung versagt

#### Ursachen
- Unterdimensionierte Decksbefestigung
- Fehlendes oder zu schwaches Bobstay
- Laminatschwäche im Bugbereich
- Dynamische Überlastung (Surfen in Wellen + Bö)
- Korrosion der Befestigungsbolzen
- Keine Unterlegplatte (Lastverteilung)

#### Schwere
KRITISCH — Kann zu Rigg-Schäden führen, wenn der Bugspriet gegen das Vorstag schlägt.
Potenzielle MOB-Gefahr bei Crew am Vordeck.

#### Prävention
- Bugspriet-Befestigung professionell ausführen (Ingenieur/Bootsbauer)
- Edelstahlplatte unter Deck als Lastverteilung (mind. 200×200 mm, 4 mm dick)
- Bobstay korrekt dimensionieren (3× Bruchlast der Halsleine)
- Jährliche Inspektion aller Bolzen und Verbindungen
- Maximale Segelfläche und Windlimit definieren

#### Reparatur
- Deckslaminat-Reparatur: 1.500–5.000 EUR
- Neue Bugspriet-Befestigung: 800–2.500 EUR
- Neuer Bugspriet: je nach Typ (siehe Abschnitt 6.2)
- Gesamtkosten: 3.000–10.000 EUR

### 8.7 F-16_04-06 — Snuffer-Blockade

#### Beschreibung
Der Snuffer-Strumpf blockiert und kann weder hoch- noch heruntergelassen werden. Das Segel
kann nicht gesetzt oder — kritischer — nicht geborgen werden.

#### Erscheinungsbild
- Snuffer-Strumpf bewegt sich nicht trotz Kraftaufwand
- Strumpf-Ring klemmt an einer Naht oder einem Patch
- Segel ist halb entfaltet, halb im Strumpf
- Bergeleine ist unter Spannung, bewegt aber nichts

#### Ursachen
- Nähte oder Patches stehen über und blockieren den Ring
- Strumpf-Stoff verknotet sich am Ring
- Segel-Tuch zu steif (neues Segel, kaltes Wetter)
- Ring-Durchmesser zu klein für die Segelfläche
- Salzablagerungen am Ring

#### Sofortmaßnahmen (Blockade beim Bergen)
1. Schot vollständig fieren (Entlastung)
2. Ruckweise an der Bergeleine ziehen
3. Wenn das nicht hilft: Abfallen auf toten Vorwind
4. Crew am Vorstag: Strumpf manuell herunterziehen
5. Notfall: Fall fieren, Segel ins Wasser, dann einsammeln

#### Prävention
- Snuffer-Ring und Innenseite regelmäßig mit Silikonspray behandeln
- Segel-Nähte bei der Herstellung snuffer-kompatibel ausführen (keine vorstehenden Nähte)
- Richtigen Snuffer-Durchmesser wählen (siehe Tabelle 4.5.2)
- Vor jedem Einsatz: Snuffer-Laufbahn auf Fremdkörper prüfen
- Alten, steifen Strumpf durch neuen ersetzen

### 8.8 F-16_04-07 — Schothorn-Ausriss

#### Beschreibung
Das Schothorn (Clew) reißt aus dem Segel. Die Schot zieht das Schothorn-Patch oder den
Schothorn-Ring aus dem Tuch. Das Segel flattert unkontrolliert.

#### Erscheinungsbild
- Schothorn-Ring oder -Kausch liegt noch an der Schot
- Segel hat ein Loch oder Riss am ehemaligen Schothorn
- Patch-Material ist vom Tuch getrennt
- Segel flattert frei (keine Schot-Kontrolle mehr)

#### Ursachen
- Überlastung (zu viel Wind für das Segel)
- Schock-Belastung (Bö, Patenthalse)
- Unterdimensionierte Patches
- UV-geschwächtes Tuch im Patch-Bereich
- Fehlerhafte Vernähung (Segelmacher-Fehler)
- Korrodierte Öse/Ring

#### Sofortmaßnahmen
1. Fall sofort fieren!
2. Segel am Vorliek einsammeln
3. Schot sichern (Peitscheneffekt!)
4. Segel unter Deck

#### Reparatur
- Neuer Patch + Ring: 200–600 EUR
- Bei Tuchschaden um das Schothorn: Panel-Ersatz, 400–1.200 EUR
- Bei großflächigem Schaden: Wirtschaftlicher Totalschaden möglich

### 8.9 F-16_04-08 — Halskausch-Versagen

#### Beschreibung
Die Halskausch (Tack Ring) am Bug des asymmetrischen Spinnakers oder Gennakers versagt.
Der Hals löst sich, das Segel fliegt frei und wird nur noch am Fall und der Schot gehalten.

#### Erscheinungsbild
- Halskausch-Ring verformt oder gebrochen
- Hals-Patch vom Tuch getrennt
- Segel steht frei am Fall, flattert unkontrolliert
- Halsleine hängt ohne Verbindung zum Segel

#### Ursachen
- Dynamische Überlastung (Surfen, Bö)
- Korrodierter Ring (Edelstahl 304 statt 316L!)
- UV-geschwächtes Tuch am Hals
- Unterdimensionierter Patch
- Falsches Anschlagen (direkt am Ring statt über Schäkel)

#### Sofortmaßnahmen
1. Schot fieren → Segel flattert frei
2. Fall fieren → Segel kommt herunter
3. Segel am Achterliek einsammeln
4. ACHTUNG: Segel kann sich um Vorstag wickeln!

#### Prävention
- Halskausch-Ring regelmäßig auf Korrosion und Verformung prüfen
- Nur Edelstahl 316L verwenden
- Hals-Patch alle 5 Jahre durch Segelmacher inspizieren
- Softschäkel statt Metallschäkel (schont den Ring)

### 8.10 F-16_04-09 — Baum-Bruch

#### Beschreibung
Der Spinnakerbaum bricht während des Einsatzes, typischerweise bei einer Halse,
einem Broach oder einer Patenthalse.

#### Erscheinungsbild
- Baum geknickt oder in zwei Teilen
- Bruchstelle typischerweise in der Mitte oder am Nock-Ende
- Bei Aluminium: scharfe Bruchkanten (Verletzungsgefahr!)
- Bei Carbon: Splitter und Faserbruch
- Guy/Schot hängen lose

#### Ursachen
- Dynamische Überlastung (Patenthalse, Broach)
- Materialermüdung (viele Biegezyklen)
- Korrosion (bei Aluminium)
- Unterdimensionierter Baum
- Beschädigung durch unsachgemäße Lagerung
- Kerbwirkung durch Befestigungslöcher

#### Schwere
KRITISCH — Ein brechender Baum kann Crewmitglieder verletzen (Peitscheneffekt).
Carbon-Splitter können Segel und Personen verletzen.

#### Sofortmaßnahmen
1. Crew in Sicherheit bringen (weg vom Vordeck!)
2. Lose Teile sichern
3. Spinnaker bergen (Fall fieren, Segel einsammeln)
4. Gebrochenen Baum an Deck sichern
5. Scharfe Kanten mit Tape abkleben

#### Prävention
- Baum auf Dellen, Knicke und Korrosion inspizieren (jährlich)
- Carbon-Bäume auf Delamination prüfen (Klopftest)
- Maximale Windstärke beachten
- Bei Halse: Baum nie durchschwingen lassen (kontrolliert!)
- Baum sachgemäß lagern (horizontal, keine Punktbelastung)

### 8.11 F-16_04-10 — Hourglassing

#### Beschreibung
Das Segel nimmt beim Furlen oder Setzen eine Stundenglasform an: Der obere und untere
Teil sind entfaltet, die Mitte ist verdreht und eingeschnürt.

#### Erscheinungsbild
- Segel sieht aus wie eine Sanduhr
- Mittelteil verdreht und eingewickelt
- Oberer und unterer Bereich gebläht
- Tritt bei Code 0 und Furling-Gennaker auf

#### Ursachen
- Zu schnelles Furlen/Unfurlen
- Ungleichmäßige Torsionsseil-Spannung
- Wind dreht während des Manövers
- Falscher Schottrimm beim Furlen
- Torsionsseil am Ende seiner Lebensdauer

#### Sofortmaßnahmen
1. Furlen stoppen!
2. Versuchen, das Segel in der entgegengesetzten Richtung zu öffnen
3. Leichte Kurzkorrekturen (Anluven/Abfallen)
4. Schot-Spannung variieren
5. Wenn nichts hilft: Fall fieren und Segel im Wasser entwirren

#### Prävention
- Langsam und kontrolliert furlen/unfurlen
- Schot beim Furlen kontrolliert nachgeben (nicht freigeben!)
- Torsionsseil-Spannung korrekt einstellen
- Code 0 nur bei passenden Bedingungen furlen (<14 kn TWS)
- Furlen immer in gleicher Richtung

### 8.12 F-16_04-11 — Tack-Line Chafe (Halsleine-Schamfilen)

#### Beschreibung
Die Halsleine des asymmetrischen Spinnakers oder Gennakers scheuert an der
Bugspriet-Spitze, dem Ankerbeschlag oder dem Vorstag. Dies kann zu plötzlichem
Versagen führen.

#### Erscheinungsbild
- Aufgerauhte Stellen an der Halsleine
- Fasern stehen ab (fuzzing)
- Mantel der Leine aufgescheuert
- Kern sichtbar (bei Kern-Mantel-Konstruktion)
- Reduzierter Durchmesser an der Scheuerstelle

#### Ursachen
- Scharfe Kanten am Bugspriet oder Bugbeschlag
- Fehlende Scheuerschutz-Hülse
- Zu dünne Halsleine
- Halsleine läuft über Metallkante ohne Umlenkrolle
- Salzwasser-Verschärfung (Salzkristalle als Schleifmittel)

#### Prävention
- Chafe Guard (Scheuerschutz) an allen Kontaktstellen
- Halsleine regelmäßig inspizieren und drehen (alle 3 Monate)
- Umlenkrolle am Bugspriet installieren
- Alle scharfen Kanten entgraten und verrunden
- Dyneema-Halsleine mit Chafe-Guard bevorzugen

#### Reparatur
- Halsleine ersetzen: 30–120 EUR (je nach Material und Länge)
- Umlenkrolle nachrüsten: 80–250 EUR
- Chafe Guard: 15–40 EUR

### 8.13 F-16_04-12 — Luff-Tape Ablösung

#### Beschreibung
Das Vorliekband (Luff Tape) löst sich vom Segel. Bei Code 0 und Furling-Gennaker führt
dies zum Versagen des Furling-Systems.

#### Erscheinungsbild
- Vorliekband steht ab oder hängt lose
- Segel „beult" entlang des Vorlieks
- Torsionsseil sichtbar (bei Code 0)
- Segel furlt nicht mehr gleichmäßig

#### Ursachen
- Klebstoff-Versagen (Alterung, UV)
- Naht-Auflösung entlang des Vorlieks
- Überlastung (zu hohe Vorliekspannung)
- Falsche Reparatur durch nicht-spezialisierten Segelmacher

#### Reparatur
- Vorliekband neu einnähen/kleben: 300–800 EUR
- Bei Code 0 mit Torsionsseil: 800–2.000 EUR (komplette Vorliek-Rekonstruktion)
- Muss vom spezialisierten Segelmacher ausgeführt werden

---

## 9. Troubleshooting

### 9.1 Entscheidungsbaum: Spinnaker lässt sich nicht setzen

```
Spinnaker lässt sich nicht setzen
├── Fall blockiert?
│   ├── Ja → Fall-Umlenkrolle am Masttop prüfen
│   │        ├── Rolle dreht nicht → Lager defekt, schmieren oder tauschen
│   │        ├── Fall verklemmt in Nut → Fall mit Bootshaken befreien
│   │        └── Fall um Stag gewickelt → Mast-Top inspizieren
│   └── Nein ↓
├── Segel kommt nicht aus dem Beutel/Schacht?
│   ├── Ja → Segel verknotet im Beutel → Segel herausnehmen, sortieren
│   │        ├── Schacht blockiert → Schacht von unten durchschieben
│   │        └── Segel nass und verklumpt → Segel trocknen, erneut packen
│   └── Nein ↓
├── Segel öffnet sich nicht (bleibt zusammen)?
│   ├── Ja → Stops/Gummibänder lösen sich nicht → dickere Stops verwenden
│   │        ├── Zu wenig Wind → warten auf mehr Wind, ggf. Segel schütteln
│   │        └── Segel im Windschatten des Groß → Kurs korrigieren
│   └── Nein ↓
├── Segel steht verdreht?
│   ├── Ja → Schoten oder Fall verdreht → Bergen, Verdrehung beseitigen
│   │        ├── Kopf und Hals vertauscht → Bergen, korrekt anschlagen
│   │        └── Segel um Vorstag gewickelt → Bergen, Genua einrollen
│   └── Nein ↓
└── Snuffer lässt sich nicht hochziehen?
    ├── Ring blockiert → Silikonspray, Hindernisse entfernen
    ├── Bergeleine zu kurz → Verlängern
    └── Segel zu schwer (nass) → Trocknen lassen
```

### 9.2 Entscheidungsbaum: Broaching

```
Boot neigt zum Broaching
├── Bei jeder Windstärke?
│   ├── Ja → Ruder-/Autopilot-Problem
│   │        ├── Autopilot zu langsam → Manuell steuern, Verstärkung erhöhen
│   │        ├── Ruder zu klein → Bootsbau-Problem, Segelfläche reduzieren
│   │        └── Ruder-Spiel zu groß → Ruder-Lagerung prüfen
│   └── Nein, nur bei >X kn ↓
├── Groß zu dicht?
│   ├── Ja → Groß fieren, Traveller nach Lee
│   │        ├── Achterliek des Groß zu geschlossen → Achterliek öffnen
│   │        └── Baumniederholer zu fest → Lösen
│   └── Nein ↓
├── Spinnaker-Schot zu dicht?
│   ├── Ja → Schot fieren bis Luvliek gerade kippt
│   │        ├── Barberholer zu weit oben → Barberholer nach unten
│   │        └── Schot-Führung zu weit vorne → Weiter achtern
│   └── Nein ↓
├── Spinnaker zu groß für die Bedingungen?
│   ├── Ja → Kleineres / flacheres Segel setzen
│   │        ├── S1 → S2 oder A3
│   │        └── A2 → A3 oder MPS
│   └── Nein ↓
├── Kurs zu hoch (zu dicht am Wind)?
│   ├── Ja → Abfallen, tieferer Kurs
│   │        └── TWA <120° mit symm. Spi → Abfallen auf >130°
│   └── Nein ↓
└── Crew-Gewicht falsch verteilt?
    ├── Zu wenig Gewicht achtern → Crew nach achtern
    └── Zu wenig Gewicht nach Luv → Crew nach Luv
```

### 9.3 Entscheidungsbaum: Code 0 furlt nicht ein

```
Code 0 lässt sich nicht furlen
├── Wind zu stark (>16 kn TWS)?
│   ├── Ja → Abfallen auf toten Vorwind, Last reduzieren
│   │        ├── Dann Furlleine ziehen → OK
│   │        └── Hilft nicht → Schot komplett fieren, Fall fieren, Segel am Deck bergen
│   └── Nein ↓
├── Torsionsseil blockiert?
│   ├── Ja → Wicklung am Torsionsseil prüfen
│   │        ├── Kink/Knick → Fall fieren, Kink lösen
│   │        ├── Seil gebrochen → Manuell bergen (siehe F-16_04-03)
│   │        └── Seil-Termination gelöst → Manuell bergen, Segelmacher
│   └── Nein ↓
├── Furltrommel blockiert?
│   ├── Ja → Furlleine prüfen
│   │        ├── Furlleine verheddert → Entwirren
│   │        ├── Trommel korrodiert → Spray (Notlösung), dann Service
│   │        └── Lager defekt → Manuell bergen, Furler zum Service
│   └── Nein ↓
├── Hourglassing?
│   ├── Ja → Entgegengesetzt drehen, Schot variieren (siehe F-16_04-10)
│   └── Nein ↓
└── Segel hat sich um Vorstag gewickelt?
    ├── Ja → Fall fieren, Segel von Hand abwickeln
    └── Nein → Alle Leinen auf freien Lauf prüfen
```

### 9.4 Entscheidungsbaum: Hourglassing beim Furlen

```
Hourglassing beim Furlen
├── Beim Erstfurlen (neues Segel)?
│   ├── Ja → Torsionsseil-Spannung prüfen
│   │        ├── Zu wenig Spannung → Halsleine durchsetzen
│   │        ├── Zu viel Spannung → Halsleine etwas fieren
│   │        └── Torsionsseil falsch eingebaut → Segelmacher kontaktieren
│   └── Nein ↓
├── Immer an der gleichen Stelle?
│   ├── Ja → Lokales Problem am Torsionsseil
│   │        ├── Kink im Seil → Seil ersetzen
│   │        ├── Naht/Patch blockiert → Segelmacher nacharbeiten
│   │        └── Vorliek-Tape lose → Reparieren (siehe F-16_04-12)
│   └── Nein ↓
├── Wind zu stark?
│   ├── Ja → Bei weniger Wind furlen
│   └── Nein ↓
└── Schot-Handling falsch?
    ├── Schot zu schnell gefiert → Langsamer, kontrollierter fieren
    ├── Schot zu dicht → Vor dem Furlen etwas fieren
    └── Schot nicht geführt → Schot aktiv kontrollieren während des Furlens
```

### 9.5 Entscheidungsbaum: Spinnakerbaum-Handling

```
Probleme mit dem Spinnakerbaum
├── Baum lässt sich nicht am Mast befestigen?
│   ├── Gabelkopf passt nicht → Mast-Ring/Kugel verschmutzt oder korrodiert → Reinigen
│   │        ├── Falscher Gabelkopf → Richtigen Adapter beschaffen
│   │        └── Beschlag verformt → Tauschen
│   └── Kein Platz für Befestigung → Topping-Lift kollidiert → Führung korrigieren
├── Baum lässt sich nicht nach Lee ausschieben?
│   ├── Topping-Lift zu kurz → Verlängern
│   ├── Niederholer blockiert → Niederholer lösen
│   ├── Wanten im Weg → Baum-Route korrigieren
│   └── Guy zu kurz → Guy verlängern
├── Nock-Ende öffnet sich nicht/nicht kontrolliert?
│   ├── Federschnapper defekt → Schmieren oder tauschen
│   ├── Trip-Line verknotet → Entwirren
│   └── Guy verklemmt → Freikämpfen, ggf. karabinerhaken verwenden
├── Baum schwingt unkontrolliert?
│   ├── Niederholer nicht angesetzt → Niederholer befestigen und spannen
│   ├── Topping zu lose → Topping nachsetzen
│   └── Guy nicht belegt → Guy auf Winsch oder Klampe belegen
└── Baum bricht (siehe F-16_04-09)?
    └── Sofortmaßnahmen einleiten
```

---

## 10. Sicherheit

### 10.1 Broach-Prävention

#### 10.1.1 Grundregeln

1. **Ständiger Trimm**: Spinnaker-Schot nie belegen — immer in der Hand oder sofort lösbar
2. **Groß kontrollieren**: Bei Bö sofort Groß fieren
3. **Crew-Position**: Ausreichend Gewicht nach Luv und achtern
4. **Windüberwachung**: Ständig AWA und AWS beobachten
5. **Kurs anpassen**: Bei steigendem Wind tiefer abfallen
6. **Rechtzeitig bergen**: Lieber zu früh als zu spät

#### 10.1.2 Windlimits

| Segeltyp | Max TWS Fahrt (kn) | Max TWS Regatta (kn) | Max TWS Einhand (kn) |
|----------|--------------------|-----------------------|---------------------|
| S1 Leichtwind | 12 | 14 | — |
| S2 Allround | 20 | 25 | — |
| A2 Allround | 18 | 22 | 14 |
| Gennaker (Fahrt) | 18 | — | 14 |
| Code 0 | 14 | 16 | 14 |
| Code D | 16 | 18 | 14 |
| MPS | 18 | — | 14 |

#### 10.1.3 Krängungsgrenzwerte

| Bootstyp | Max. Krängung unter Spi | Sofort-Bergen-Winkel |
|----------|-------------------------|---------------------|
| Modernes Breitschiff (>40° Stabilitätsbereich) | 20° | 25° |
| Klassisch (30–40° Stabilitätsbereich) | 15° | 20° |
| Schwerer Langkieler | 18° | 22° |
| Multihull | 5° (!) | 8° |

### 10.2 Chinesische Halse (Chinese Gybe)

#### 10.2.1 Beschreibung

Eine chinesische Halse ist eine unkontrollierte Halse des Großsegels, die durch eine
Kursänderung unter Spinnaker ausgelöst wird. Das Groß schlägt gewaltsam auf die andere
Seite, was zu schweren Verletzungen und Rigg-Schäden führen kann.

#### 10.2.2 Prävention

- **Preventer / Bullenstander**: Immer gesetzt bei Vorwindkurs mit Spinnaker
- **Kursüberwachung**: Nie tiefer als TWA 170° ohne Preventer
- **Groß-Kontrolle**: Großschot belegt, Traveller nach Lee
- **Baumvang**: Baumvang unter Zug, um unkontrolliertes Schleudern zu verhindern
- **Autopilot-Kurs**: Nicht auf AWA-Modus segeln bei tiefem Vorwind

### 10.3 MOB-Risiko

#### 10.3.1 Risikoanalyse

Spinnaker-Segeln erhöht das MOB-Risiko durch:
- Crew-Einsatz am Vordeck (Setzen, Bergen, Halsen)
- Plötzliche Bewegungen (Broach, Patenthalse)
- Schoten unter Last (Peitscheneffekt)
- Konzentration auf Segel-Manöver statt Sicherheit

#### 10.3.2 Präventionsmaßnahmen

- **Lifeline**: Am Vordeck immer Lifeline tragen
- **Strecktau**: Strecktau gespannt, Karabiner eingepickt
- **Handschuhe**: Handschuhe tragen (Schoten unter Last!)
- **Briefing**: Vor jedem Manöver klare Aufgabenverteilung
- **Helm**: Empfohlen bei Nachtsegelei und Starkwind
- **Notfallschere**: Am Mast oder im Cockpit bereithalten

### 10.4 Nacht-Segeln mit Spinnaker

#### 10.4.1 Besondere Risiken

- Eingeschränkte Sicht auf Segeltrimm und Vorliek
- Verzögerte Erkennung von Windänderungen
- Ermüdete Crew
- Erschwerte Bergung bei Problemen

#### 10.4.2 Empfehlungen

- Nur erfahrene Crews sollten nachts Spinnaker segeln
- Konservatives Windlimit (50–70 % des Tageslimits)
- Telltale-Leuchten am Luvliek (LED-Strips)
- Masttopp-Licht für Segel-Beleuchtung
- Schot-Markierungen (fluoreszierend)
- Bergen bei jedem Zweifel — „Im Zweifel: Bergen!"

### 10.5 Kurzhand-Segeln mit Spinnaker

#### 10.5.1 Empfohlene Ausrüstung

- Code 0 mit Top-Down-Furler (Einhand-kompatibel)
- Snuffer für Gennaker/Asym. Spinnaker
- Autopilot mit Wind-Modus
- Alle Leinen ins Cockpit geführt
- Schot-Schlaufen für schnelles Loswerfen
- Notfallschere am Steuerstand
- Kein symmetrischer Spinnaker einhand!

#### 10.5.2 Windlimits für Einhandsegler

| Segel | Max TWS (kn) | Empfohlen TWS (kn) |
|-------|-------------|---------------------|
| Code 0 (Furler) | 14 | 10 |
| Code D (Furler) | 14 | 10 |
| Gennaker + Snuffer | 14 | 10 |
| Asymm. Spi + Snuffer | 16 | 12 |
| Symmetrischer Spi | — (nicht empfohlen!) | — |

### 10.6 Notfallverfahren

#### 10.6.1 Spinnaker-Bergung bei Starkwind

**Schritt-für-Schritt:**
1. Crew warnen: „Spinnaker-Bergung! Vorsicht!"
2. Kurs auf toten Vorwind
3. Schot vollständig fieren (Segel flattert hinter dem Groß)
4. Bei symm. Spi: Baum nach vorne schwenken
5. Segel am Achterliek/Schot einsammeln
6. Fall kontrolliert fieren (NICHT ruckartig!)
7. Segel sofort unter Deck oder in den Beutel

**Wenn Bergen nicht möglich ist:**
1. Schot und Guy/Halsleine kappen (Notfallschere)
2. Fall fieren → Segel fliegt weg (verloren, aber Boot sicher)
3. Alternative: Segel ins Wasser fallen lassen, dann einsammeln

---

## 11. Kosten

### 11.1 Anschaffungskosten nach Bootsgröße

#### 11.1.1 Symmetrischer Spinnaker

| Bootslänge (ft) | Segelfläche (m²) | Budget EUR | Mittelklasse EUR | Premium EUR |
|-----------------|------------------|-----------|------------------|-------------|
| 25 | 35–45 | 1.200–1.600 | 1.800–2.400 | 2.800–3.600 |
| 28 | 45–55 | 1.400–1.800 | 2.000–2.800 | 3.200–4.200 |
| 30 | 50–65 | 1.600–2.000 | 2.400–3.200 | 3.600–4.800 |
| 33 | 60–80 | 1.800–2.400 | 2.800–3.600 | 4.200–5.500 |
| 36 | 75–100 | 2.000–2.800 | 3.200–4.200 | 5.000–6.500 |
| 40 | 100–130 | 2.600–3.400 | 4.000–5.200 | 6.000–8.000 |
| 44 | 130–160 | 3.200–4.200 | 5.000–6.500 | 7.500–10.000 |
| 50 | 170–220 | 4.200–5.500 | 6.500–8.500 | 10.000–14.000 |

#### 11.1.2 Asymmetrischer Spinnaker / Gennaker

| Bootslänge (ft) | Budget EUR | Mittelklasse EUR | Premium EUR |
|-----------------|-----------|------------------|-------------|
| 25 | 1.000–1.400 | 1.600–2.200 | 2.600–3.400 |
| 28 | 1.200–1.600 | 1.800–2.600 | 3.000–3.800 |
| 30 | 1.400–1.800 | 2.200–3.000 | 3.400–4.500 |
| 33 | 1.600–2.200 | 2.600–3.400 | 4.000–5.200 |
| 36 | 1.800–2.600 | 3.000–4.000 | 4.800–6.200 |
| 40 | 2.400–3.200 | 3.600–4.800 | 5.600–7.500 |
| 44 | 3.000–3.800 | 4.500–6.000 | 7.000–9.500 |
| 50 | 3.800–5.000 | 6.000–8.000 | 9.500–13.000 |

#### 11.1.3 Code 0

| Bootslänge (ft) | Budget EUR | Mittelklasse EUR | Premium EUR |
|-----------------|-----------|------------------|-------------|
| 25 | 2.200–2.800 | 3.200–4.200 | 5.000–6.500 |
| 28 | 2.600–3.200 | 3.800–5.000 | 5.800–7.500 |
| 30 | 3.000–3.800 | 4.200–5.500 | 6.500–8.500 |
| 33 | 3.400–4.200 | 5.000–6.500 | 7.500–10.000 |
| 36 | 3.800–4.800 | 5.500–7.500 | 8.500–12.000 |
| 40 | 4.800–6.200 | 7.000–9.500 | 11.000–15.000 |
| 44 | 6.000–7.800 | 9.000–12.000 | 14.000–19.000 |
| 50 | 7.500–10.000 | 11.000–15.000 | 18.000–25.000 |

### 11.2 Hardware-Kosten

| Komponente | Klein (25–32 ft) EUR | Mittel (33–42 ft) EUR | Groß (43–55 ft) EUR |
|-----------|---------------------|----------------------|--------------------|
| Spinnakerbaum Alu | 600–1.000 | 1.000–1.800 | 1.800–3.200 |
| Spinnakerbaum Carbon | 2.200–3.200 | 3.200–5.000 | 5.000–8.000 |
| Bugspriet (Nachrüst) | 1.500–2.200 | 2.200–3.500 | 3.500–5.500 |
| Snuffer/Sock | 350–550 | 550–900 | 900–1.800 |
| Top-Down-Furler | 1.600–2.800 | 2.800–4.500 | 4.500–7.500 |
| Schoten (Paar, Polyester) | 80–140 | 140–250 | 250–450 |
| Schoten (Paar, Dyneema) | 200–380 | 380–650 | 650–1.200 |
| Barberholer-Set | 60–120 | 120–220 | 220–400 |
| Blocks/Umlenkrollen | 200–400 | 400–800 | 800–1.500 |

### 11.3 Gesamtkosten-Pakete

| Paket | 36 ft Fahrt | 36 ft Regatta | 44 ft Fahrt | 44 ft Regatta |
|-------|------------|---------------|------------|---------------|
| Gennaker + Snuffer + Bugspriet | 5.500–7.500 | — | 8.000–11.000 | — |
| Code 0 + Furler + Bugspriet | 8.000–12.000 | 10.000–15.000 | 12.000–18.000 | 15.000–23.000 |
| Symm. Spi + Baum + Zubehör | 5.000–7.000 | 6.000–9.000 | 7.500–10.500 | 9.000–14.000 |
| Komplett (Gennaker + Code 0) | 12.000–18.000 | 15.000–22.000 | 18.000–27.000 | 22.000–35.000 |

### 11.4 Wartungs- und Betriebskosten (jährlich)

| Position | Gennaker | Symm. Spi | Code 0 |
|----------|----------|-----------|--------|
| Inspektion (Segelmacher) | 80–150 | 80–150 | 120–200 |
| Waschen/Reinigen | 50–100 | 50–100 | 80–150 |
| Kleine Reparaturen | 0–200 | 0–300 | 0–400 |
| Furler-Wartung | — | — | 100–250 |
| Schot-Erneuerung (alle 3–5 Jahre) | 30–60/Jahr | 30–60/Jahr | 30–60/Jahr |
| Snuffer-Wartung | 20–50 | — | — |
| **Gesamt pro Jahr** | **180–560** | **160–610** | **330–1.060** |

### 11.5 Ersatzzyklen

| Komponente | Lebensdauer Fahrt | Lebensdauer Regatta | Ersatzkosten (36 ft) |
|-----------|-------------------|---------------------|---------------------|
| Nylon-Spinnaker | 8–15 Jahre | 3–6 Jahre | 2.000–4.500 |
| Laminat-Code 0 | 6–10 Jahre | 2–5 Jahre | 4.500–8.500 |
| Snuffer-Strumpf | 8–12 Jahre | 5–8 Jahre | 200–500 |
| Furler-Lager | 5–8 Jahre | 3–5 Jahre | 300–800 |
| Torsionsseil | 5–8 Jahre | 3–5 Jahre | 400–1.200 |
| Spinnakerbaum Alu | 15–25 Jahre | 8–15 Jahre | 800–1.800 |
| Bugspriet Carbon | 15–25 Jahre | 10–15 Jahre | 2.200–4.000 |
| Schoten Polyester | 3–5 Jahre | 1–3 Jahre | 100–250 |
| Schoten Dyneema | 5–8 Jahre | 2–4 Jahre | 300–650 |

---

## 12. FAQ

### 12.1 Grundlagen

**F1: Was ist der Unterschied zwischen Spinnaker und Gennaker?**
A: Der symmetrische Spinnaker ist ein bauchiges, symmetrisches Vorwindsegel, das mit einem
Spinnakerbaum gefahren wird (TWA 120–180°). Der Gennaker ist ein asymmetrisches Segel ohne
Baum, das am Bug oder Bugspriet befestigt wird (TWA 80–150°). Der Gennaker ist einfacher
zu handhaben, aber bei reinem Vorwind weniger effektiv.

**F2: Brauche ich einen Bugspriet für einen Gennaker?**
A: Empfohlen, aber nicht zwingend. Ein Bugspriet (1,0–2,0 m) vergrößert den Abstand des
Segels zum Vorstag und verhindert Scheuern. Ohne Bugspriet kann ein Gennaker an einem
Decksbeschlag am Bug befestigt werden, allerdings mit geringerer Effektivität.

**F3: Kann ich einen Spinnaker einhand segeln?**
A: Einen symmetrischen Spinnaker einhand zu segeln, wird nicht empfohlen — zu viele
gleichzeitige Kontrollen (Baum, Schot, Guy, Ruder). Asymmetrische Segel (Gennaker, Code 0)
mit Snuffer oder Furler sind einhand-tauglich, aber nur bei moderatem Wind (<14 kn TWS).

**F4: Was ist ein Code 0?**
A: Ein Code 0 ist ein flaches, laminiertes Leichtwindsegel für enge Halbwindkurse
(TWA 55–100°). Es wird auf einer Rollanlage (Top-Down-Furler) gefahren und füllt die
Lücke zwischen Genua und Gennaker. Material: Laminat (nicht Nylon!).

**F5: Was bedeutet „0,75 oz" bei Spinnaker-Tuch?**
A: Das Tuchgewicht wird in Unzen pro Quadratyard (oz/yd²) angegeben. 0,75 oz = ca. 25 g/m².
Leichtere Tuche (0,5 oz) sind für Leichtwind, schwerere (1,5 oz) für Starkwind geeignet.

### 12.2 Auswahl

**F6: Welches Leichtwindsegel für eine 36-ft-Fahrtenyacht?**
A: Für die meisten Fahrtensegler empfehlen wir als erstes Segel einen MPS (Multi-Purpose
Spinnaker) oder einen Cruising-Gennaker mit Snuffer. Budget: 2.500–4.000 EUR für das Segel,
plus 2.000–3.000 EUR für Bugspriet und Snuffer. Bei genügend Budget: zusätzlich Code 0.

**F7: Regatta oder Cruising — welchen Spinnaker?**
A: Regattasegel sind leichter (dünneres Tuch), größer, leistungsstärker, aber empfindlicher
und kurzlebiger. Fahrtensegel sind robuster, schwerer, kleiner, dafür langlebiger und
einfacher zu handhaben. Preis ähnlich, Lebensdauer unterschiedlich (Regatta: 3–6 Jahre,
Fahrt: 8–15 Jahre).

**F8: Lohnt sich ein Code 0 zusätzlich zum Gennaker?**
A: Ja, wenn Sie viel bei Leichtwind segeln (Mittelmeer, Ostsee im Sommer). Der Code 0
deckt TWA 55–100° ab, der Gennaker 80–150°. Zusammen haben Sie nahezu lückenloses
Leichtwindsegeln. Kosten für beide: 8.000–15.000 EUR (36 ft, inkl. Furler und Bugspriet).

**F9: Welche Farbe soll mein Spinnaker haben?**
A: Helle Farben (weiß, hellblau, gelb) halten länger (geringere UV-Absorption). Dunkle
Farben (rot, schwarz, dunkelblau) sehen gut aus, aber altern schneller. Für Regatten:
Sichtbarkeit (Segelnummern müssen lesbar sein). Für Fahrt: Helle Farben bevorzugen.

**F10: Gebrauchter Spinnaker — worauf achten?**
A: 1) Daumendrucktest (Nagel darf nicht durchs Tuch gehen). 2) Falttest (keine weißen
Knickstreifen). 3) Nähte prüfen (keine losen Fäden, keine Naht-Trennung). 4) Ecken-Patches
inspizieren. 5) Alter erfragen (<8 Jahre ist OK für Fahrt). 6) Reparaturstellen zählen
(>3 große Reparaturen → nicht kaufen). Preis: 30–50 % vom Neupreis.

### 12.3 Handling

**F11: Wie packe ich einen Spinnaker richtig?**
A: Symmetrisch: Alle drei Ecken sortieren (Kopf oben, Hals und Schothorn getrennt), dann
das Vorliek und Achterliek Bahn für Bahn einsammeln, Segel in den Beutel stopfen (nicht
falten!). Asymmetrisch: Hals und Schothorn identifizieren, Vorliek als Leitfaden nehmen,
Segel entlang des Vorlieks zusammenlegen, in den Beutel.

**F12: Was tun, wenn sich der Spinnaker um das Vorstag wickelt?**
A: 1) Nicht ziehen! 2) Auf toten Vorwind gehen. 3) Alle Schoten lösen. 4) Leichtes
Anluven und Abfallen versuchen. 5) Crew mit Bootshaken den Wickler lösen. 6) Letzter
Ausweg: Fall fieren, Segel ins Wasser. Prävention: Genua vorher einrollen, Schoten frei halten.

**F13: Wie halse ich einen Gennaker?**
A: 1) Auf tiefen Vorwindkurs abfallen (TWA >150°). 2) Alte Schot fieren. 3) Segel wandert
um/unter das Vorstag. 4) Neue Schot dichtnehmen. 5) Neuen Kurs anliegen. Tipp: Schot der
neuen Seite vorher vorbereiten, nicht zu früh die alte Schot fieren.

**F14: Wann muss ich den Spinnaker bergen?**
A: Faustregel: Bergen, bevor es unbequem wird. Konkreter: Wenn TWS das Segel-Limit
erreicht (siehe Abschnitt 10.1.2), wenn die Krängung >20° dauerhaft ist, wenn der
Steuermann den Kurs nicht mehr halten kann, wenn die Crew sich unsicher fühlt, oder
wenn der Wind weiter zunimmt.

**F15: Kann ich einen Spinnaker waschen?**
A: Ja, aber nur mit Süßwasser und mildem Segelreiniger (z. B. Sail Bath von McLube).
Auf dem Rasen oder einem sauberen Boden ausbreiten, mit weichem Schwamm reinigen.
Kein Hochdruckreiniger! Kein Chlor! Trocknen lassen, aber nicht in der prallen Sonne.
Nylon kann in der Waschmaschine gewaschen werden (30°, Schongang, Wäschesack).

### 12.4 Technik

**F16: Was ist ein Torsionsseil und warum brauche ich das?**
A: Das Torsionsseil ist ein steifes Seil im Vorliek eines Code 0 oder Furling-Gennakers.
Es überträgt die Drehbewegung des Furlers auf das gesamte Vorliek, sodass sich das Segel
gleichmäßig aufrollt. Ohne Torsionsseil wickelt sich das Segel unkontrolliert auf.

**F17: Was ist der Unterschied zwischen einem Snuffer und einem Furler?**
A: Ein Snuffer ist ein Strumpf, der über das Segel gezogen wird — das Segel wird
komplett eingehüllt. Ein Furler rollt das Segel auf eine Linie auf, ähnlich einer
Rollgenua. Snuffer: günstiger, einfacher, für Nylon-Segel. Furler: teurer, komfortabler,
für Laminatsegel (Code 0).

**F18: Wie lange hält ein Spinnaker?**
A: Fahrteneinsatz: Nylon-Segel 8–15 Jahre (abhängig von UV-Exposition), Code 0 (Laminat)
6–10 Jahre. Regattaeinsatz: Nylon 3–6 Jahre, Code 0 2–5 Jahre. Hauptalterungsfaktor ist
UV-Strahlung, nicht mechanische Belastung.

**F19: Was ist der Unterschied zwischen Top-Down- und Bottom-Up-Furler?**
A: Top-Down-Furler: Furltrommel am Masttop, Segel wickelt von oben nach unten auf.
Kein stehendes Vorstag nötig, ideal für fliegende Segel. Bottom-Up-Furler: Furltrommel
am Deck/Bugspriet, Segel wickelt von unten nach oben auf. Stärkere Konstruktion, für
größere Segel. Die meisten Code-0-Furler sind Top-Down.

**F20: Kann ich meinen vorhandenen Genua-Furler für einen Code 0 verwenden?**
A: Nein. Der Genua-Furler (z. B. Furlex) ist ein Bottom-Up-Furler am Vorstag und nicht
für freifliegende Segel geeignet. Ein Code 0 benötigt einen dedizierten Top-Down-Furler
(Karver, Facnor, Selden GX etc.) mit Torsionsseil im Vorliek.

### 12.5 Kosten und Wirtschaftlichkeit

**F21: Was kostet ein komplettes Gennaker-Paket für eine 36-ft-Yacht?**
A: Gennaker (Fahrt-Qualität): 2.500–3.500 EUR, Snuffer: 550–800 EUR, Bugspriet (Nachrüst):
2.200–3.000 EUR, Schoten (Dyneema): 300–500 EUR, Kleinteile: 200–400 EUR.
Gesamt: ca. 5.500–8.000 EUR.

**F22: Lohnt sich die Investition in einen Spinnaker/Gennaker?**
A: Wenn Sie mehr als 20 Segeltage/Jahr haben und mindestens 30 % davon raumen Wind
erwarten, ja. Die Fahrtgeschwindigkeit steigt bei raumem Wind um 30–60 %, was auf einer
Mittelmeer-Überfahrt (z. B. Mallorca–Sardinien, 300 sm) 12–24 Stunden Zeitersparnis
bedeuten kann.

**F23: Was kostet eine Spinnaker-Reparatur?**
A: Kleine Risse (<30 cm): 80–200 EUR. Mittlere Risse (30–100 cm): 200–500 EUR.
Schothorn-/Hals-Patch-Reparatur: 200–600 EUR. Code 0 Vorliek-Reparatur: 500–1.500 EUR.
Großflächiger Schaden: Oft Neubau günstiger als Reparatur.

**F24: Gebrauchter Spinnaker — lohnt sich das?**
A: Ja, wenn das Segel <6 Jahre alt ist, den Daumendrucktest besteht und keine
strukturellen Schäden hat. Preis: 30–50 % vom Neupreis. Risiko: Versteckte UV-Schäden,
falsche Größe für Ihre Yacht. Empfehlung: Segelmacher-Bewertung vor dem Kauf (50–100 EUR).

**F25: Wie viel Leistung gewinne ich mit einem Spinnaker gegenüber einer Genua unter Land?**
A: Auf einem tiefen Raumwindkurs (TWA >120°) gewinnen Sie typischerweise 2–4 Knoten
gegenüber der unter Land gestellten Genua. Auf Halbwindkursen (TWA 80–120°) mit Code 0
oder Gennaker: 1–2 Knoten Gewinn. Bei Leichtwind (<8 kn TWS) ist der Gewinn noch größer,
da die Genua unter Land bei wenig Wind fast nicht mehr wirkt.

### 12.6 Fortgeschritten

**F26: Wie wähle ich zwischen Code 0 und Code D?**
A: Code 0: TWA 55–100°, für Halbwind-Reaching, flach, steif. Code D: TWA 90–140°, für
tieferes Reaching, bauchiger, oft aus Nylon. Wenn Sie nur ein Furling-Segel wollen und
überwiegend raumschots segeln → Code D. Wenn Sie auch bei Halbwind Leistung brauchen → Code 0.
Ideal: beide.

**F27: Was bedeutet „Projected Area" und warum ist sie wichtig?**
A: Die Projected Area ist die Segelfläche, die der Wind „sieht" — also die Projektion des
dreidimensionalen Segels auf eine Ebene senkrecht zum Wind. Ein voller Spinnaker hat eine
größere tatsächliche Fläche, aber nicht unbedingt eine größere Projected Area. Optimales
Trimmen maximiert die Projected Area.

**F28: Warum sind Spinnaker aus Nylon und Code 0 aus Laminat?**
A: Spinnaker brauchen Elastizität für ihre aerodynamische Form — Nylon dehnt sich 15–25 %
und bildet dadurch das gewünschte tiefe Profil. Code 0 funktioniert wie ein Vorsegel und
braucht ein flaches, stabiles Profil — Laminat dehnt sich nur 1–3 %, hält die Form.

**F29: Kann ich einen Gennaker auf einer Rollanlage fahren?**
A: Ja, mit einem speziellen Furling-Gennaker und Top-Down-Furler. Das Segel braucht ein
Torsionsseil im Vorliek und muss für Furling-Betrieb konstruiert sein (Anti-Torsion-Schnitt).
Leistungseinbuße gegenüber freifliegendem Gennaker: ca. 5–10 %. Kosten für Furler zusätzlich:
2.500–5.000 EUR.

**F30: Was ist der Unterschied zwischen einer Patent-Halse und einer kontrollierten Halse?**
A: Eine kontrollierte Halse ist ein geplantes Manöver mit koordinierter Crew (Baum, Schoten,
Ruder). Eine Patenthalse ist eine unkontrollierte, unbeabsichtigte Halse — oft durch
Windsprung oder Steuerfehler ausgelöst — die zu Segel- und Rigg-Schäden führen kann.
Prävention: Ständige Windbeobachtung, nie auf tiefem Vorwindkurs unaufmerksam segeln.

---

## 13. Glossar

### 13.1 Begriffe A–Z (DE/EN)

| Nr. | Deutsch | Englisch | Erklärung |
|-----|---------|----------|-----------|
| 1 | Achterliek | Leech | Hintere Kante des Segels |
| 2 | Achterholer | Afterguy / Guy | Leine, die den Spinnakerbaum nach achtern hält |
| 3 | Asymmetrischer Spinnaker | Asymmetric Spinnaker | Vorwindsegel ohne Baum, am Bug befestigt |
| 4 | Barberholer | Barber Hauler | Leine zur Kontrolle der Schot-Führungsposition |
| 5 | Bauch | Draft / Belly | Maximale Tiefe des Segelprofils |
| 6 | Broach / Broaching | Broach | Unkontrollierte Drehung in den Wind unter Spinnaker |
| 7 | Bugspriet | Bowsprit | Horizontaler Sprit am Bug zur Segel-Befestigung |
| 8 | Bullenstander | Preventer | Leine gegen unkontrolliertes Schlagen des Großbaums |
| 9 | Code 0 | Code Zero | Flaches Leichtwindsegel für Halbwindkurse |
| 10 | Code D | Code D | Furling-Segel für tiefere Windwinkel als Code 0 |
| 11 | Dip-Pole-Halse | Dip-Pole Gybe | Halsenmanöver, bei dem der Baum durch das Vordreieck taucht |
| 12 | End-for-End-Halse | End-for-End Gybe | Halsenmanöver mit Abnehmen und Umsetzen des Baums |
| 13 | Fall | Halyard | Leine zum Hochziehen des Segels |
| 14 | Furler | Furler / Roller | Aufrollsystem für Segel |
| 15 | Gennaker | Gennaker | Asymmetrisches Leichtwindsegel, Kreuzung aus Genua und Spinnaker |
| 16 | Hals | Tack | Untere vordere Ecke des Segels |
| 17 | Halskausch | Tack Ring/Thimble | Ring oder Kausch am Hals des Segels |
| 18 | Halsleine | Tack Line | Leine zur Befestigung und Trimmung des Halses |
| 19 | Kopf | Head | Obere Ecke des Segels |
| 20 | Kopfbrett | Headboard | Verstärkungsplatte am Kopf des Segels |
| 21 | Krängung | Heeling | Seitliche Neigung des Bootes |
| 22 | Luvliek | Luff | Vordere Kante des Segels (windzugewandt) |
| 23 | MPS | MPS (Multi-Purpose Spinnaker) | Allzweck-Vorwindsegel |
| 24 | Niederholer | Downhaul / Foreguy | Leine, die den Spinnakerbaum nach unten hält |
| 25 | Nylon-Ripstop | Nylon Ripstop | Leichtes Polyamid-Gewebe mit Riss-Stopp-Fäden |
| 26 | Patch | Reinforcement Patch | Verstärkungsfeld an belasteten Stellen |
| 27 | Patenthalse | Chinese Gybe / Accidental Gybe | Unkontrollierte Halse |
| 28 | Radialschnitt | Radial Cut | Panel-Anordnung strahlenförmig von den Ecken |
| 29 | Schot | Sheet | Leine zur Trimmung des Segels (Lee-Seite) |
| 30 | Schothorn | Clew | Untere hintere Ecke des Segels |
| 31 | Screecher | Screacher | Flaches Leichtwindsegel, ähnlich Code 0 |
| 32 | Snuffer | Snuffer / Sock / Dousing Sleeve | Berge-Strumpf für Spinnaker/Gennaker |
| 33 | Spinnaker | Spinnaker | Bauchiges Vorwindsegel |
| 34 | Spinnakerbaum | Spinnaker Pole | Horizontaler Baum zur Steuerung des Spinnakers |
| 35 | Stundenglasform | Hourglass | Verdrehte Segelform beim Furlen |
| 36 | Symmetrischer Spinnaker | Symmetric Spinnaker | Spiegelbildliches Vorwindsegel mit Baum |
| 37 | Top-Down-Furler | Top-Down Furler | Aufroller, der das Segel von oben nach unten einrollt |
| 38 | Topping | Topping Lift | Leine, die den Spinnakerbaum nach oben hält |
| 39 | Torsionsseil | Torque Rope / Anti-Torsion Cable | Seil im Vorliek zur Übertragung der Furler-Drehung |
| 40 | Tri-radial | Tri-radial | Panel-Schnitt mit drei radialen Zentren |
| 41 | TWA | TWA (True Wind Angle) | Wahrer Windwinkel |
| 42 | TWS | TWS (True Wind Speed) | Wahre Windgeschwindigkeit |
| 43 | Vordreieck | Fore Triangle | Dreieck zwischen Mast, Deck und Vorstag |
| 44 | Wickler | Wrap | Verdrehung des Segels um Vorstag oder sich selbst |
| 45 | Windschatten | Wind Shadow / Blanket | Bereich hinter einem Segel ohne Wind |

---

## 14. Schnell-Referenz

### 14.1 Segel-Auswahl nach Windwinkel und -stärke

```
               TWS (kn)
         4    8   12   16   20   24   28
TWA 60° [C0] [C0] [C0] [ — ] [ — ] [ — ] [ — ]
    70° [C0] [C0] [C0] [C0] [ — ] [ — ] [ — ]
    80° [C0] [GK] [GK] [GK] [ — ] [ — ] [ — ]
    90° [GK] [GK] [GK] [GK] [A3] [ — ] [ — ]
   100° [GK] [GK] [GK] [GK] [A3] [A3] [ — ]
   110° [A1] [A2] [A2] [A2] [A3] [A3] [ — ]
   120° [A1] [A2] [A2] [A2] [A3] [A3] [S3]
   130° [A1] [A2] [A2] [S2] [S2] [S3] [S3]
   140° [S1] [S2] [S2] [S2] [S2] [S3] [S3]
   150° [S1] [S2] [S2] [S2] [S2] [S3] [S3]
   160° [S1] [S1] [S2] [S2] [S2] [S3] [S3]
   170° [S1] [S1] [S2] [S2] [S2] [S3] [S3]
   180° [S1] [S1] [S2] [S2] [S2] [S3] [S3]

Legende: C0=Code 0, GK=Gennaker, A1-A3=Asym. Spi, S1-S3=Symm. Spi
```

### 14.2 Checkliste: Vor dem Spinnaker-Setzen

```
□ Wind prüfen: TWS und TWA im Einsatzbereich des Segels?
□ Segel vorbereitet: Kopf, Hals, Schothorn sortiert?
□ Schoten klar: Beide Schoten frei von Hindernissen?
□ Fall klar: Fall nicht verdreht, Umlenkrolle frei?
□ Genua: Eingerollt oder auf der Lee-Seite?
□ Baum (symm.): Topping, Niederholer, Guy bereit?
□ Snuffer (asym.): Bergeleine klar, Ring frei?
□ Crew briefing: Aufgaben klar verteilt?
□ Autopilot: Kurs stabil, Wind-Modus aktiv?
□ Preventer: Am Großbaum gesetzt (bei Vorwindkurs)?
□ Notfallschere: Griffbereit?
□ Lifeline: Crew am Vordeck eingepickt?
```

### 14.3 Checkliste: Nach dem Spinnaker-Bergen

```
□ Segel trocken? → Unter Deck zum Trocknen
□ Segel nass? → Nicht im Beutel lassen, ausbreiten
□ Schäden sichtbar? → Dokumentieren, Reparatur planen
□ Schoten aufschießen
□ Baum (symm.): Sichern, Topping ablegen
□ Snuffer: Bergeleine sichern
□ Fall am Mast belegen
□ Genua: Wieder ausrollen
□ Preventer: Ablegen (falls nötig)
```

### 14.4 Kurzformel-Tabelle

| Parameter | Formel |
|-----------|--------|
| Spinnaker-Fläche (grob) | 1,5 × I × J |
| Schot-Länge (symm.) | 2 × (LOA + Masthöhe) |
| Schot-Länge (asym.) | 2 × LOA × 1,5 |
| Bugspriet-Länge | 0,12–0,18 × LOA |
| Baum-Länge | J × 1,0 bis J × 1,1 |
| Max. SMW (Regatta) | 1,8 × J |
| Max. SMW (Fahrt) | 1,6 × J |
| Snuffer-Durchmesser | √(Segelfläche × 0,8) × 10 mm |

---

## 15. ANHANG A–H: Fallstudien

### ANHANG A: Bavaria 38 Cruiser — Gennaker-Nachrüstung

**Ausgangssituation:**
- Boot: Bavaria 38 Cruiser, Baujahr 2019
- LOA: 11,70 m, I: 14,20 m, J: 4,10 m
- Revier: Mittelmeer (Kroatien, Griechenland)
- Crew: 2 Personen (Ehepaar)
- Budget: max. 8.000 EUR

**Anforderung:**
- Leichtwindsegel für 2-Personen-Bedienung
- Einfaches Handling, kein Vordeck-Einsatz
- Kein Spinnakerbaum

**Gewählte Lösung:**
- Segel: Elvström Cruising Gennaker, 85 m², 1,0 oz Nylon
- Snuffer: ATN Tacker, 250 mm
- Bugspriet: Selden BSK 508, 1,5 m
- Schoten: Marlow D2 Dyneema, 10 mm × 2 × 24 m
- Halsleine: Dyneema SK78, 8 mm × 6 m
- Montage: durch Bootswerft

**Kosten:**
| Position | EUR |
|----------|-----|
| Gennaker | 2.600 |
| Snuffer | 720 |
| Bugspriet | 2.450 |
| Schoten und Halsleine | 380 |
| Blöcke und Klemmen | 320 |
| Montage | 650 |
| **Gesamt** | **7.120** |

**Ergebnis nach einer Saison:**
- 28 Segeltage, davon 14 mit Gennaker
- Durchschnittlicher Geschwindigkeitsgewinn: +2,5 kn bei TWA 100–140°
- Handling: „Nach 3× Setzen/Bergen waren wir sicher"
- Probleme: Einmal leichtes Scheuern der Halsleine → Chafe Guard nachgerüstet

### ANHANG B: Hanse 415 — Code 0 für Einhandsegler

**Ausgangssituation:**
- Boot: Hanse 415, Baujahr 2021
- LOA: 12,40 m, I: 15,80 m, J: 4,50 m
- Revier: Ostsee, geplant Atlantiküberquerung
- Crew: 1 Person (Einhandsegler)
- Budget: max. 12.000 EUR

**Anforderung:**
- Leichtwindsegel für Einhand-Bedienung
- Alle Leinen im Cockpit
- Furling-System (kein Snuffer — zu aufwändig einhand)

**Gewählte Lösung:**
- Code 0: North Headsail 0, 95 m², CZ-100 Laminat
- Furler: Karver KF-5
- Bugspriet: Selden BSK 508 (bereits ab Werft vorhanden)
- Schoten: Dyneema SK78 Tapered, 10 mm → 8 mm
- Umlenkung: 2× Harken Carbo Block 57 mm

**Kosten:**
| Position | EUR |
|----------|-----|
| Code 0 | 5.800 |
| Furler Karver KF-5 | 3.800 |
| Schoten | 420 |
| Blöcke und Umlenkungen | 480 |
| Montage | 750 |
| **Gesamt** | **11.250** |

**Ergebnis:**
- Code 0 wird bei TWA 60–90° und TWS 4–14 kn eingesetzt
- Furling funktioniert zuverlässig einhand vom Cockpit
- Geschwindigkeitsgewinn bei Leichtwind: +1,5–2,5 kn
- Probleme: Bei TWS >14 kn muss sofort gefurlt werden (Windlimit beachten)

### ANHANG C: J/112E — Regatta-Spinnaker-Ausstattung

**Ausgangssituation:**
- Boot: J/112E, Baujahr 2020
- LOA: 11,20 m, I: 14,50 m, J: 4,20 m
- Revier: Nordsee, RORC-Regatten
- Crew: 7 Personen
- Budget: 20.000 EUR

**Gewählte Lösung (3-Segel-Garderobe):**
- S2: North S2 Allround, 105 m², NorDac 0,75 oz
- A2: North A2 Reaching, 90 m², NorDac 0,75 oz
- Code 0: North 3Di Code 0, 80 m²
- Spinnakerbaum: Selden Carbon, 4,5 m
- Furler: Karver KF-3
- Bugspriet: J/Boats Original, Carbon

**Kosten:**
| Position | EUR |
|----------|-----|
| S2 Spinnaker | 4.200 |
| A2 Spinnaker | 3.800 |
| Code 0 (3Di) | 7.500 |
| Spinnakerbaum | 4.200 |
| Furler | 3.000 |
| Schoten und Beschläge | 1.800 |
| **Gesamt** | **24.500** (Budget überschritten, Kompromiss bei Schoten) |

**Ergebnis:**
- S2: Eingesetzt bei Vorwindkursen, 130–180° TWA
- A2: Eingesetzt bei Reaching, 80–140° TWA
- Code 0: Eingesetzt bei Leichtwind-Halbwind, 60–90° TWA
- Regatta-Platzierungen verbessert um durchschnittlich 2 Plätze

### ANHANG D: Hallberg-Rassy 44 — Blauwasser-MPS

**Ausgangssituation:**
- Boot: Hallberg-Rassy 44, Baujahr 2018
- LOA: 13,55 m, I: 17,20 m, J: 5,00 m
- Revier: Weltumsegelung (Passatrouten)
- Crew: 2 Personen (Ehepaar, 60+)
- Budget: 10.000 EUR

**Anforderung:**
- Ein einziges Leichtwindsegel für alle Bedingungen
- Maximale Einfachheit und Sicherheit
- Snuffer-Bergung
- Keine Furler-Technik (KISS-Prinzip)

**Gewählte Lösung:**
- MPS: Quantum MPS, 140 m², 1,2 oz Nylon, verstärkte Ausführung
- Snuffer: ATN Tacker, 300 mm, Heavy-Duty
- Bugspriet: Vorhanden (HR44 ab Werft)
- Schoten: Polyester Doppelgeflecht 14 mm (bewusst kein Dyneema — griffiger)

**Kosten:**
| Position | EUR |
|----------|-----|
| MPS | 4.200 |
| Snuffer Heavy-Duty | 980 |
| Schoten | 280 |
| Halsleine | 60 |
| Kleinteile | 180 |
| **Gesamt** | **5.700** |

**Ergebnis nach 18 Monaten Blauwassersegeln:**
- MPS bei TWA 85–160° eingesetzt (breiter als erwartet)
- Passatwind (TWS 12–18 kn): „Phantastisch, Boot macht 7–8 kn statt 5–6 kn unter Genua"
- Snuffer-Bergung funktioniert zuverlässig zu zweit
- 2× kleine Reparaturen (Naht am Schothorn — Segelmacher in Las Palmas, 120 EUR)
- Fazit der Eigner: „Bestes Investment der gesamten Ausrüstung"

### ANHANG E: Jeanneau Sun Odyssey 440 — Nachrüstung Furling-Gennaker

**Ausgangssituation:**
- Boot: Jeanneau Sun Odyssey 440, Baujahr 2022
- LOA: 13,30 m, I: 16,80 m, J: 4,80 m
- Revier: Balearen, Sardinien, Korsika
- Crew: 2–4 Personen (Familie)
- Budget: 10.000 EUR

**Gewählte Lösung:**
- Furling-Gennaker: OneSails, 120 m², Nylon 0,9 oz mit Torsionsseil
- Furler: Facnor FX-4500
- Bugspriet: Vorhanden (ab Werft)
- Schoten: Hybrid (Dyneema-Kern, Polyester-Mantel), 12 mm

**Kosten:**
| Position | EUR |
|----------|-----|
| Furling-Gennaker | 3.800 |
| Furler Facnor FX-4500 | 4.600 |
| Schoten und Halsleine | 350 |
| Blöcke | 280 |
| Montage | 520 |
| **Gesamt** | **9.550** |

**Ergebnis:**
- Gennaker wird regelmäßig bei TWA 85–135° eingesetzt
- Furling funktioniert zuverlässig (auch die 12-jährige Tochter kann es bedienen)
- Einmal Hourglassing bei zu schnellem Furlen → gelöst durch langsames Entfurlen
- Geschwindigkeitsgewinn: +2–3 kn gegenüber unter Land gestellter Genua

### ANHANG F: Swan 48 — Premium Code 0 + Gennaker

**Ausgangssituation:**
- Boot: Swan 48, Baujahr 2023
- LOA: 14,75 m, I: 18,50 m, J: 5,20 m
- Revier: Mittelmeer (ORC-Regatten + Cruising)
- Crew: 4–8 Personen
- Budget: 25.000 EUR

**Gewählte Lösung:**
- Code 0: Doyle Stratis, 110 m², Dyneema/Carbon-Laminat
- Gennaker: Doyle Centric A-Spi, 150 m², 0,75 oz Nylon
- Furler: Karver KF-7
- Snuffer: ATN Tacker 300 mm

**Kosten:**
| Position | EUR |
|----------|-----|
| Code 0 (Stratis) | 9.200 |
| Gennaker | 4.500 |
| Furler Karver KF-7 | 5.600 |
| Snuffer | 950 |
| Schoten (2 Sets) | 1.200 |
| Beschläge und Montage | 1.800 |
| **Gesamt** | **23.250** |

### ANHANG G: Catana 47 — Katamaran Code 0

**Ausgangssituation:**
- Boot: Catana 47, Baujahr 2020
- LOA: 14,02 m, I: 17,50 m, J: 5,80 m (breiteres Vordreieck)
- Revier: Karibik (Charterkatamaran mit Eigner-Nutzung)
- Crew: 2–4 Personen
- Budget: 12.000 EUR

**Besonderheit Katamaran:**
- Höhere Geschwindigkeiten → scheinbarer Wind dreht nach vorne
- Kein Krängen → kein Broaching-Risiko
- Breiteres Vordreieck → größere Segelfläche möglich
- Doppelrumpf → zwei Buganschläge möglich

**Gewählte Lösung:**
- Screecher/Code 0: UK Sailmakers Tape-Drive, 120 m², Pentex-Laminat
- Furler: Profurl C490
- Bugspriet: Carbon, integriert (ab Werft)

**Kosten:**
| Position | EUR |
|----------|-----|
| Screecher/Code 0 | 6.800 |
| Furler Profurl C490 | 4.200 |
| Schoten | 480 |
| Montage | 380 |
| **Gesamt** | **11.860** |

**Ergebnis:**
- Screecher wird bei TWA 50–85° eingesetzt
- Bei 10 kn TWS: Bootgeschwindigkeit steigt von 7 auf 9,5 kn
- Furling funktioniert auch bei Passatwind zuverlässig
- Ideales Segel für Katamaran (scheinbarer Wind ist bei Kats immer weiter vorne)

### ANHANG H: Bénéteau First 36.7 — Budget-Regatta-Lösung

**Ausgangssituation:**
- Boot: Bénéteau First 36.7, Baujahr 2005
- LOA: 10,90 m, I: 13,80 m, J: 4,10 m
- Revier: Regatta (Clubregatten, keine ORC)
- Crew: 5–6 Personen
- Budget: 5.000 EUR (knapp!)

**Gewählte Lösung (Budget-optimiert):**
- Symmetrischer Spinnaker: Rolly Tasker S-Spi, 75 m², 0,75 oz Nylon
- Spinnakerbaum: Gebraucht (Forespar Aluminium, 3,8 m), 400 EUR
- Schoten: Polyester Doppelgeflecht 10 mm

**Kosten:**
| Position | EUR |
|----------|-----|
| Symmetrischer Spinnaker | 1.900 |
| Spinnakerbaum (gebraucht) | 400 |
| Baum-Beschläge (neu) | 280 |
| Schoten und Guy | 180 |
| Blöcke | 240 |
| Topping und Niederholer | 120 |
| **Gesamt** | **3.120** |

**Ergebnis:**
- Deutlich unter Budget — restliches Geld für Trimm-Training investiert
- Spinnaker funktioniert auf Clubregatten einwandfrei
- Qualität von Rolly Tasker überraschend gut für den Preis
- Nach 2 Saisons: Platzierung in der Clubwertung von Platz 12 auf Platz 5 verbessert

---

## 16. ANHANG I–R: Pydantic v2 Modelle

### ANHANG I: SpinnakerSpec

```python
"""Spezifikation eines Spinnakers oder Gennakers."""

from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class SpinnakerType(str, Enum):
    """Typ des Spinnakers."""
    SYMMETRIC_S1 = "symmetric_s1"
    SYMMETRIC_S2 = "symmetric_s2"
    SYMMETRIC_S3 = "symmetric_s3"
    SYMMETRIC_S4 = "symmetric_s4"
    ASYMMETRIC_A1 = "asymmetric_a1"
    ASYMMETRIC_A2 = "asymmetric_a2"
    ASYMMETRIC_A3 = "asymmetric_a3"
    ASYMMETRIC_A4 = "asymmetric_a4"
    GENNAKER_CRUISING = "gennaker_cruising"
    GENNAKER_PERFORMANCE = "gennaker_performance"
    GENNAKER_FURLING = "gennaker_furling"
    CODE_0 = "code_0"
    CODE_D = "code_d"
    SCREECHER = "screecher"
    BLISTER = "blister"
    MPS = "mps"


class SpinnakerMaterial(str, Enum):
    """Material des Spinnakers."""
    NYLON_050 = "nylon_0.50oz"
    NYLON_060 = "nylon_0.60oz"
    NYLON_075 = "nylon_0.75oz"
    NYLON_090 = "nylon_0.90oz"
    NYLON_100 = "nylon_1.00oz"
    NYLON_120 = "nylon_1.20oz"
    NYLON_150 = "nylon_1.50oz"
    NYLON_200 = "nylon_2.00oz"
    POLYESTER = "polyester"
    PENTEX_LAMINATE = "pentex_laminate"
    TECHNORA_LAMINATE = "technora_laminate"
    CARBON_LAMINATE = "carbon_laminate"
    DYNEEMA_LAMINATE = "dyneema_laminate"
    MEMBRANE = "membrane"


class PanelCut(str, Enum):
    """Panelschnitt-Methode."""
    RADIAL = "radial"
    TRI_RADIAL = "tri_radial"
    BI_RADIAL = "bi_radial"
    CROSS_CUT = "cross_cut"


class SpinnakerSpec(BaseModel):
    """Vollständige Spezifikation eines Spinnakers oder Gennakers."""

    model_config = {"from_attributes": True}

    # Identifikation
    name: str = Field(..., description="Segelname (z. B. 'A2 Gennaker')")
    manufacturer: str = Field(..., description="Hersteller (z. B. 'North Sails')")
    model: Optional[str] = Field(None, description="Modellbezeichnung")
    year_built: Optional[int] = Field(None, description="Baujahr", ge=1950, le=2030)
    serial_number: Optional[str] = Field(None, description="Seriennummer")

    # Typ und Material
    spinnaker_type: SpinnakerType = Field(..., description="Typ des Spinnakers")
    material: SpinnakerMaterial = Field(..., description="Tuchmaterial")
    panel_cut: PanelCut = Field(PanelCut.RADIAL, description="Panelschnitt")
    panel_count: Optional[int] = Field(None, description="Anzahl Panels", ge=6, le=80)

    # Dimensionen (mm)
    luff_length_mm: float = Field(..., description="Vorliek-Länge in mm", gt=0)
    leech_length_mm: float = Field(..., description="Achterliek-Länge in mm", gt=0)
    foot_length_mm: float = Field(..., description="Fußlänge in mm", gt=0)
    mid_girth_mm: float = Field(..., description="Mittelbreite in mm", gt=0)
    area_m2: float = Field(..., description="Segelfläche in m²", gt=0)

    # Windbereich
    twa_min_deg: float = Field(..., description="Minimaler TWA in Grad", ge=0, le=180)
    twa_max_deg: float = Field(..., description="Maximaler TWA in Grad", ge=0, le=180)
    tws_min_kn: float = Field(..., description="Minimaler TWS in Knoten", ge=0)
    tws_max_kn: float = Field(..., description="Maximaler TWS in Knoten", ge=0)

    # Gewicht und Zustand
    weight_kg: Optional[float] = Field(None, description="Segelgewicht in kg", gt=0)
    cloth_weight_gsm: Optional[float] = Field(None, description="Tuchgewicht in g/m²", gt=0)
    condition_percent: Optional[float] = Field(
        None, description="Zustand in Prozent (100=neu)", ge=0, le=100
    )
    uv_degradation_percent: Optional[float] = Field(
        None, description="UV-Degradation in Prozent", ge=0, le=100
    )

    # Ausstattung
    has_snuffer: bool = Field(False, description="Snuffer-kompatibel")
    has_furler: bool = Field(False, description="Furler-kompatibel")
    has_torsion_rope: bool = Field(False, description="Torsionsseil vorhanden")
    has_anti_curl: bool = Field(False, description="Anti-Curl-Seil vorhanden")

    # Kosten
    purchase_price_eur: Optional[float] = Field(None, description="Kaufpreis in EUR", ge=0)
    replacement_cost_eur: Optional[float] = Field(None, description="Ersatzkosten in EUR", ge=0)
```

### ANHANG J: GennakerSpec

```python
"""Erweiterte Spezifikation speziell für Gennaker."""

from pydantic import BaseModel, Field
from typing import Optional


class GennakerSpec(BaseModel):
    """Erweiterte Gennaker-Spezifikation mit Fahrt-spezifischen Feldern."""

    model_config = {"from_attributes": True}

    # Basis-Referenz
    base_spec_id: str = Field(..., description="Referenz auf SpinnakerSpec-ID")

    # Bugspriet-Konfiguration
    bowsprit_length_mm: Optional[float] = Field(
        None, description="Bugspriet-Länge in mm", gt=0
    )
    bowsprit_material: Optional[str] = Field(
        None, description="Bugspriet-Material (z. B. 'carbon', 'aluminium')"
    )
    bowsprit_manufacturer: Optional[str] = Field(None, description="Bugspriet-Hersteller")
    has_bobstay: bool = Field(True, description="Bobstay vorhanden")

    # Snuffer-Details
    snuffer_model: Optional[str] = Field(None, description="Snuffer-Modell")
    snuffer_diameter_mm: Optional[float] = Field(
        None, description="Snuffer-Durchmesser in mm", gt=0
    )
    snuffer_manufacturer: Optional[str] = Field(None, description="Snuffer-Hersteller")

    # Schot-Konfiguration
    sheet_material: Optional[str] = Field(None, description="Schot-Material")
    sheet_diameter_mm: Optional[float] = Field(
        None, description="Schot-Durchmesser in mm", gt=0
    )
    sheet_length_m: Optional[float] = Field(None, description="Schot-Länge in m", gt=0)
    tack_line_material: Optional[str] = Field(None, description="Halsleine-Material")
    tack_line_diameter_mm: Optional[float] = Field(
        None, description="Halsleine-Durchmesser in mm", gt=0
    )

    # Performance-Daten
    twa_optimal_deg: Optional[float] = Field(
        None, description="Optimaler TWA in Grad", ge=0, le=180
    )
    speed_gain_percent: Optional[float] = Field(
        None, description="Geschwindigkeitsgewinn gegenüber Genua in %", ge=0
    )
    max_crew_size: Optional[int] = Field(
        None, description="Minimale Crew für sicheres Handling", ge=1, le=20
    )
```

### ANHANG K: DownwindSailTrim

```python
"""Trimm-Einstellungen für Leichtwindsegel."""

from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class TrimCondition(str, Enum):
    """Trimm-Bedingung."""
    LIGHT_AIR = "light_air"
    MODERATE = "moderate"
    FRESH = "fresh"
    STRONG = "strong"
    HEAVY = "heavy"


class DownwindSailTrim(BaseModel):
    """Aktuelle oder empfohlene Trimm-Einstellungen."""

    model_config = {"from_attributes": True}

    # Bedingungen
    twa_deg: float = Field(..., description="Aktueller TWA in Grad", ge=0, le=180)
    tws_kn: float = Field(..., description="Aktueller TWS in Knoten", ge=0)
    awa_deg: Optional[float] = Field(None, description="Aktueller AWA in Grad", ge=0, le=180)
    aws_kn: Optional[float] = Field(None, description="Aktueller AWS in Knoten", ge=0)
    trim_condition: TrimCondition = Field(..., description="Trimm-Bedingung")

    # Schot-Einstellungen
    sheet_tension: Optional[str] = Field(
        None, description="Schot-Spannung: 'loose', 'moderate', 'firm'"
    )
    sheet_lead_position_mm: Optional[float] = Field(
        None, description="Schot-Führungsposition (Abstand vom Heck) in mm"
    )
    barber_hauler_mm: Optional[float] = Field(
        None, description="Barberholer-Einstellung in mm"
    )

    # Halsleine (asymmetrisch)
    tack_line_length_mm: Optional[float] = Field(
        None, description="Halsleine-Länge (gefiert) in mm", ge=0
    )

    # Spinnakerbaum (symmetrisch)
    pole_height_deg: Optional[float] = Field(
        None, description="Baum-Höhenwinkel in Grad", ge=-10, le=45
    )
    pole_angle_deg: Optional[float] = Field(
        None, description="Baum-Seitenwinkel in Grad", ge=0, le=180
    )

    # Profil
    draft_depth_percent: Optional[float] = Field(
        None, description="Bauchtiefe in Prozent der Sehnenlänge", ge=0, le=40
    )
    draft_position_percent: Optional[float] = Field(
        None, description="Bauchlage in Prozent des Vorlieks", ge=20, le=70
    )

    # Leistung
    boat_speed_kn: Optional[float] = Field(
        None, description="Aktuelle Bootsgeschwindigkeit in Knoten", ge=0
    )
    target_speed_kn: Optional[float] = Field(
        None, description="Zielgeschwindigkeit in Knoten", ge=0
    )
    vmg_kn: Optional[float] = Field(
        None, description="Velocity Made Good in Knoten"
    )
```

### ANHANG L: SpinnakerPoleConfig

```python
"""Konfiguration des Spinnakerbaums."""

from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class PoleMaterial(str, Enum):
    """Material des Spinnakerbaums."""
    ALUMINIUM_6082 = "aluminium_6082"
    ALUMINIUM_7075 = "aluminium_7075"
    CARBON = "carbon"
    TELESCOPING_ALUMINIUM = "telescoping_aluminium"
    TELESCOPING_CARBON = "telescoping_carbon"


class PoleEndFitting(str, Enum):
    """Beschlag am Baum-Ende."""
    FORK = "fork"
    SNAP_SHACKLE = "snap_shackle"
    TRIP_LINE = "trip_line"
    PISTON = "piston"


class SpinnakerPoleConfig(BaseModel):
    """Konfiguration des Spinnakerbaums."""

    model_config = {"from_attributes": True}

    # Dimensionen
    length_mm: float = Field(..., description="Baum-Länge in mm", gt=0)
    diameter_mm: float = Field(..., description="Rohrdurchmesser in mm", gt=0)
    wall_thickness_mm: float = Field(..., description="Wandstärke in mm", gt=0)

    # Material und Gewicht
    material: PoleMaterial = Field(..., description="Baum-Material")
    weight_kg: float = Field(..., description="Baum-Gewicht in kg", gt=0)

    # Beschläge
    inboard_fitting: PoleEndFitting = Field(..., description="Innenbord-Beschlag")
    outboard_fitting: PoleEndFitting = Field(..., description="Außenbord-Beschlag")
    mast_track_height_mm: Optional[float] = Field(
        None, description="Mast-Gleitschiene Höhe in mm"
    )

    # Zugehörige Leinen
    topping_lift_diameter_mm: Optional[float] = Field(
        None, description="Topping-Lift Durchmesser in mm"
    )
    downhaul_diameter_mm: Optional[float] = Field(
        None, description="Niederholer Durchmesser in mm"
    )

    # Hersteller und Kosten
    manufacturer: Optional[str] = Field(None, description="Hersteller")
    model_name: Optional[str] = Field(None, description="Modellbezeichnung")
    purchase_price_eur: Optional[float] = Field(None, description="Kaufpreis in EUR", ge=0)

    # Zustand
    condition_percent: Optional[float] = Field(
        None, description="Zustand in Prozent", ge=0, le=100
    )
    has_dents: bool = Field(False, description="Dellen vorhanden")
    has_corrosion: bool = Field(False, description="Korrosion vorhanden")
```

### ANHANG M: SnufferSystem

```python
"""Konfiguration des Snuffer-/Sock-Systems."""

from pydantic import BaseModel, Field
from typing import Optional


class SnufferSystem(BaseModel):
    """Snuffer-System-Konfiguration."""

    model_config = {"from_attributes": True}

    # Identifikation
    manufacturer: str = Field(..., description="Hersteller (z. B. 'ATN')")
    model: str = Field(..., description="Modellbezeichnung")

    # Dimensionen
    diameter_mm: float = Field(..., description="Strumpf-Durchmesser in mm", gt=0)
    max_sail_area_m2: float = Field(
        ..., description="Maximale Segelfläche in m²", gt=0
    )
    sock_length_m: Optional[float] = Field(
        None, description="Strumpf-Länge in m", gt=0
    )

    # Material
    sock_material: str = Field("nylon", description="Strumpf-Material")
    ring_material: str = Field(
        "stainless_steel", description="Ring-Material ('stainless_steel', 'plastic')"
    )
    retrieval_line_diameter_mm: Optional[float] = Field(
        None, description="Bergeleine-Durchmesser in mm"
    )

    # Zustand
    condition_percent: Optional[float] = Field(
        None, description="Zustand in Prozent", ge=0, le=100
    )
    sock_intact: bool = Field(True, description="Strumpf intakt")
    ring_smooth: bool = Field(True, description="Ring glatt (kein Grat)")
    retrieval_line_condition: Optional[str] = Field(
        None, description="Zustand der Bergeleine: 'good', 'worn', 'replace'"
    )

    # Kosten
    purchase_price_eur: Optional[float] = Field(None, description="Kaufpreis in EUR", ge=0)
    replacement_cost_eur: Optional[float] = Field(
        None, description="Ersatzkosten in EUR", ge=0
    )
```

### ANHANG N: CodeZeroConfig

```python
"""Konfiguration eines Code-0-Segel-Systems."""

from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class FurlerType(str, Enum):
    """Typ des Furlers."""
    TOP_DOWN_HEAD = "top_down_head"
    TOP_DOWN_FOOT = "top_down_foot"
    BOTTOM_UP = "bottom_up"


class TorsionRopeType(str, Enum):
    """Typ des Torsionsseils."""
    DYNEEMA_STANDARD = "dyneema_standard"
    CARBON = "carbon"
    HYBRID = "hybrid"
    STAINLESS_WIRE = "stainless_wire"


class CodeZeroConfig(BaseModel):
    """Vollständige Code-0-System-Konfiguration."""

    model_config = {"from_attributes": True}

    # Segel-Referenz
    sail_spec_id: str = Field(..., description="Referenz auf SpinnakerSpec-ID")

    # Furler
    furler_manufacturer: str = Field(..., description="Furler-Hersteller")
    furler_model: str = Field(..., description="Furler-Modell")
    furler_type: FurlerType = Field(..., description="Furler-Typ")
    furler_max_area_m2: float = Field(
        ..., description="Furler max. Segelfläche in m²", gt=0
    )
    furler_weight_kg: Optional[float] = Field(
        None, description="Furler-Gewicht in kg", gt=0
    )

    # Torsionsseil
    torsion_rope_type: TorsionRopeType = Field(..., description="Torsionsseil-Typ")
    torsion_rope_diameter_mm: float = Field(
        ..., description="Torsionsseil-Durchmesser in mm", gt=0
    )
    torsion_rope_breaking_load_kn: Optional[float] = Field(
        None, description="Bruchlast des Torsionsseils in kN", gt=0
    )
    torsion_rope_age_years: Optional[float] = Field(
        None, description="Alter des Torsionsseils in Jahren", ge=0
    )
    torsion_rope_cycles: Optional[int] = Field(
        None, description="Anzahl Furl-Zyklen", ge=0
    )

    # Furlleine
    furl_line_diameter_mm: Optional[float] = Field(
        None, description="Furlleine-Durchmesser in mm"
    )
    furl_line_length_m: Optional[float] = Field(
        None, description="Furlleine-Länge in m"
    )

    # Windlimits
    max_tws_set_kn: float = Field(16.0, description="Max TWS zum Setzen in kn")
    max_tws_furl_kn: float = Field(14.0, description="Max TWS zum Furlen in kn")

    # Kosten
    furler_price_eur: Optional[float] = Field(None, description="Furler-Preis in EUR", ge=0)
    torsion_rope_price_eur: Optional[float] = Field(
        None, description="Torsionsseil-Preis in EUR", ge=0
    )
    total_system_price_eur: Optional[float] = Field(
        None, description="Gesamtsystem-Preis in EUR", ge=0
    )
```

### ANHANG O: DownwindSailCondition

```python
"""Zustandsbewertung eines Leichtwindsegels."""

from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum


class ConditionRating(str, Enum):
    """Zustandsbewertung."""
    EXCELLENT = "excellent"
    GOOD = "good"
    FAIR = "fair"
    POOR = "poor"
    CONDEMNED = "condemned"


class DamageType(str, Enum):
    """Art des Schadens."""
    TEAR = "tear"
    UV_DEGRADATION = "uv_degradation"
    SEAM_FAILURE = "seam_failure"
    PATCH_FAILURE = "patch_failure"
    CHAFE = "chafe"
    DELAMINATION = "delamination"
    TORSION_ROPE_DAMAGE = "torsion_rope_damage"
    RING_CORROSION = "ring_corrosion"
    LUFF_TAPE_SEPARATION = "luff_tape_separation"
    CLOTH_POROSITY = "cloth_porosity"


class DamageRecord(BaseModel):
    """Einzelner Schadenseintrag."""

    model_config = {"from_attributes": True}

    damage_type: DamageType = Field(..., description="Art des Schadens")
    location: str = Field(..., description="Position am Segel (z. B. 'Kopf-Patch')")
    severity: str = Field(..., description="Schwere: 'minor', 'moderate', 'major', 'critical'")
    size_mm: Optional[float] = Field(None, description="Schadengröße in mm")
    repaired: bool = Field(False, description="Bereits repariert")
    repair_cost_eur: Optional[float] = Field(None, description="Reparaturkosten in EUR")
    notes: Optional[str] = Field(None, description="Anmerkungen")


class DownwindSailCondition(BaseModel):
    """Vollständige Zustandsbewertung eines Leichtwindsegels."""

    model_config = {"from_attributes": True}

    # Referenz
    sail_spec_id: str = Field(..., description="Referenz auf SpinnakerSpec-ID")
    inspection_date: str = Field(..., description="Inspektionsdatum (ISO 8601)")
    inspector: Optional[str] = Field(None, description="Inspektor/Segelmacher")

    # Gesamtbewertung
    overall_rating: ConditionRating = Field(..., description="Gesamtbewertung")
    overall_score: float = Field(
        ..., description="Gesamtpunktzahl 0–100", ge=0, le=100
    )
    remaining_life_years: Optional[float] = Field(
        None, description="Geschätzte Restlebensdauer in Jahren", ge=0
    )
    remaining_life_confidence: Optional[str] = Field(
        None, description="Confidence der Restlebensdauer-Schätzung"
    )

    # Detailbewertungen
    cloth_strength_percent: Optional[float] = Field(
        None, description="Tuchfestigkeit in % des Neuzustands", ge=0, le=100
    )
    seam_integrity_percent: Optional[float] = Field(
        None, description="Naht-Integrität in %", ge=0, le=100
    )
    patch_condition_percent: Optional[float] = Field(
        None, description="Patch-Zustand in %", ge=0, le=100
    )
    uv_degradation_percent: Optional[float] = Field(
        None, description="UV-Degradation in %", ge=0, le=100
    )
    porosity_rating: Optional[str] = Field(
        None, description="Porosität: 'low', 'medium', 'high'"
    )

    # Schäden
    damages: List[DamageRecord] = Field(
        default_factory=list, description="Liste der Schäden"
    )

    # Empfehlungen
    recommended_action: Optional[str] = Field(
        None, description="Empfohlene Maßnahme"
    )
    max_tws_reduced_kn: Optional[float] = Field(
        None, description="Reduziertes Windlimit in kn"
    )
    estimated_repair_cost_eur: Optional[float] = Field(
        None, description="Geschätzte Gesamtreparaturkosten in EUR"
    )
    replacement_recommended: bool = Field(
        False, description="Ersatz empfohlen"
    )
```

### ANHANG P: SpinnakerIncidentReport

```python
"""Vorfallbericht für Spinnaker-/Gennaker-Zwischenfälle."""

from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum


class IncidentType(str, Enum):
    """Typ des Vorfalls."""
    BROACH = "broach"
    CHINESE_GYBE = "chinese_gybe"
    WRAP = "wrap"
    TEAR = "tear"
    POLE_BREAK = "pole_break"
    BOWSPRIT_FAILURE = "bowsprit_failure"
    FURLER_FAILURE = "furler_failure"
    SNUFFER_BLOCKAGE = "snuffer_blockage"
    HALYARD_FAILURE = "halyard_failure"
    TACK_FAILURE = "tack_failure"
    CLEW_FAILURE = "clew_failure"
    MOB = "mob"
    OTHER = "other"


class IncidentSeverity(str, Enum):
    """Schwere des Vorfalls."""
    MINOR = "minor"
    MODERATE = "moderate"
    SERIOUS = "serious"
    CRITICAL = "critical"


class SpinnakerIncidentReport(BaseModel):
    """Vorfallbericht für Spinnaker-/Gennaker-Zwischenfälle."""

    model_config = {"from_attributes": True}

    # Identifikation
    incident_id: str = Field(..., description="Eindeutige Vorfall-ID")
    report_date: str = Field(..., description="Berichtsdatum (ISO 8601)")
    incident_date: str = Field(..., description="Vorfallsdatum (ISO 8601)")

    # Boot und Segel
    boat_name: Optional[str] = Field(None, description="Bootsname")
    boat_type: Optional[str] = Field(None, description="Bootstyp")
    boat_loa_m: Optional[float] = Field(None, description="Bootslänge in m")
    sail_spec_id: Optional[str] = Field(None, description="Referenz auf SpinnakerSpec")

    # Vorfall
    incident_type: IncidentType = Field(..., description="Typ des Vorfalls")
    severity: IncidentSeverity = Field(..., description="Schwere")
    description: str = Field(..., description="Beschreibung des Vorfalls")

    # Bedingungen
    tws_kn: Optional[float] = Field(None, description="TWS zum Zeitpunkt in kn")
    twa_deg: Optional[float] = Field(None, description="TWA zum Zeitpunkt in Grad")
    sea_state: Optional[str] = Field(
        None, description="Seegang: 'calm', 'moderate', 'rough', 'heavy'"
    )
    crew_count: Optional[int] = Field(None, description="Crew-Anzahl")
    night: bool = Field(False, description="Vorfall bei Nacht")

    # Schäden
    sail_damage: bool = Field(False, description="Segelschaden")
    hardware_damage: bool = Field(False, description="Hardwareschaden")
    rigging_damage: bool = Field(False, description="Rigg-Schaden")
    hull_damage: bool = Field(False, description="Rumpfschaden")
    personal_injury: bool = Field(False, description="Personenschaden")
    damage_description: Optional[str] = Field(None, description="Schadensbeschreibung")

    # Kosten
    repair_cost_eur: Optional[float] = Field(None, description="Reparaturkosten in EUR")
    replacement_cost_eur: Optional[float] = Field(None, description="Ersatzkosten in EUR")

    # Lessons Learned
    root_cause: Optional[str] = Field(None, description="Ursachenanalyse")
    corrective_actions: List[str] = Field(
        default_factory=list, description="Korrekturmaßnahmen"
    )
    preventive_actions: List[str] = Field(
        default_factory=list, description="Präventivmaßnahmen"
    )
```

### ANHANG Q: Fehlerbild-Referenz-Modell

```python
"""Fehlerbild-Referenzmodell für die AYDI-Wissensbasis."""

from pydantic import BaseModel, Field
from typing import Optional, List


class FaultPatternReference(BaseModel):
    """Referenz auf ein Fehlerbild aus dem Fehlerbild-Atlas."""

    model_config = {"from_attributes": True}

    code: str = Field(
        ..., description="Fehlerbild-Code (z. B. 'F-16_04-01')"
    )
    name_de: str = Field(..., description="Bezeichnung (Deutsch)")
    name_en: str = Field(..., description="Bezeichnung (Englisch)")
    severity: str = Field(
        ..., description="Schwere: 'low', 'medium', 'high', 'critical'"
    )
    frequency: str = Field(
        ..., description="Häufigkeit: 'rare', 'uncommon', 'common', 'very_common'"
    )

    # Visuelle Erkennung
    visual_detectability: str = Field(
        ..., description="Visuelle Erkennbarkeit: 'easy', 'moderate', 'difficult', 'impossible'"
    )
    confidence_level: str = Field(
        ..., description="AYDI-Confidence: 'visual_high', 'visual_medium', 'visual_low'"
    )

    # Typische Reparaturkosten
    repair_cost_min_eur: Optional[float] = Field(None, description="Min. Reparaturkosten EUR")
    repair_cost_max_eur: Optional[float] = Field(None, description="Max. Reparaturkosten EUR")

    # Verknüpfte Segeltypen
    affected_sail_types: List[str] = Field(
        default_factory=list, description="Betroffene Segeltypen"
    )

    # Schlüsselwörter für Suche
    keywords_de: List[str] = Field(
        default_factory=list, description="Suchbegriffe (Deutsch)"
    )
    keywords_en: List[str] = Field(
        default_factory=list, description="Suchbegriffe (Englisch)"
    )
```

### ANHANG R: Bewertungsmodell für Leichtwindsegel-Ausrüstung

```python
"""Bewertungsmodell für die Gesamtbewertung der Leichtwindsegel-Ausrüstung."""

from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum


class EquipmentCompleteness(str, Enum):
    """Vollständigkeit der Ausrüstung."""
    NONE = "none"
    BASIC = "basic"
    ADEQUATE = "adequate"
    GOOD = "good"
    COMPREHENSIVE = "comprehensive"
    RACE_READY = "race_ready"


class DownwindEquipmentAssessment(BaseModel):
    """Gesamtbewertung der Leichtwindsegel-Ausrüstung einer Yacht."""

    model_config = {"from_attributes": True}

    # Boot-Referenz
    boat_id: str = Field(..., description="Boot-ID")
    assessment_date: str = Field(..., description="Bewertungsdatum (ISO 8601)")

    # Vorhandene Segel
    sails: List[str] = Field(
        default_factory=list, description="Liste der SpinnakerSpec-IDs"
    )
    sail_count: int = Field(0, description="Anzahl vorhandener Leichtwindsegel")

    # Bewertung
    completeness: EquipmentCompleteness = Field(
        ..., description="Vollständigkeit der Ausrüstung"
    )
    completeness_score: float = Field(
        ..., description="Vollständigkeits-Score 0–100", ge=0, le=100
    )
    condition_score: float = Field(
        ..., description="Zustands-Score 0–100", ge=0, le=100
    )
    coverage_score: float = Field(
        ..., description="Windbereichs-Abdeckung 0–100", ge=0, le=100
    )
    overall_score: float = Field(
        ..., description="Gesamt-Score 0–100", ge=0, le=100
    )

    # Windbereichs-Abdeckung
    twa_coverage_min_deg: Optional[float] = Field(
        None, description="Minimaler abgedeckter TWA"
    )
    twa_coverage_max_deg: Optional[float] = Field(
        None, description="Maximaler abgedeckter TWA"
    )
    tws_coverage_max_kn: Optional[float] = Field(
        None, description="Maximaler abgedeckter TWS"
    )
    coverage_gaps: List[str] = Field(
        default_factory=list,
        description="Identifizierte Lücken in der Windbereichs-Abdeckung"
    )

    # Empfehlungen
    recommendations: List[str] = Field(
        default_factory=list, description="Empfehlungen zur Verbesserung"
    )
    estimated_investment_eur: Optional[float] = Field(
        None, description="Geschätzte Investition für empfohlene Verbesserungen in EUR"
    )

    # Confidence
    confidence: str = Field(
        ..., description="AYDI-Confidence-Level der Bewertung"
    )
    data_sources: List[str] = Field(
        default_factory=list,
        description="Datenquellen: 'measured', 'visual', 'estimated', 'documented'"
    )
```

---

*Ende des Dokuments — AYDI Maritime Knowledge Base v2.0*
*Letzte Aktualisierung: April 2026*
*Dieses Dokument ist Teil der AYDI-Wissensbasis (Kategorie 16: Segel)*
