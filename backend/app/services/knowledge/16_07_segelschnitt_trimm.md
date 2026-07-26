---
titel: "Segelschnitt und Trimm — Design, Formgebung und Einstellung"
kategorie: "Segel"
unterkategorie: "Segelschnitt und Trimm"
version: "2.0"
letzte_aktualisierung: "2026-04"
autor: "AYDI Maritime Knowledge Base"
---

# 16_07 — Segelschnitt und Trimm

> **AYDI Wissensdatei 16.07** — Kategorie 16: Segel
> **Confidence-Quelle:** measured (Hersteller-TDS, Windkanalstudien), documented (Segelmacher-Literatur, Regattaerfahrung), estimated (Erfahrungswerte)
> **Letzte Aktualisierung:** 2026-04

---

## Inhaltsverzeichnis

1. [Einführung](#1-einführung)
2. [Grundlagen der Segelformgebung](#2-grundlagen-der-segelformgebung)
3. [Schnittmethoden](#3-schnittmethoden)
4. [Formgebungstechniken](#4-formgebungstechniken)
5. [Latten-Design](#5-latten-design)
6. [Trimminstrumente Großsegel](#6-trimminstrumente-großsegel)
7. [Trimminstrumente Vorsegel](#7-trimminstrumente-vorsegel)
8. [Trimm nach Wind und Kurs](#8-trimm-nach-wind-und-kurs)
9. [Telltales und Strömungsindikatoren](#9-telltales-und-strömungsindikatoren)
10. [Fehlerbild-Atlas](#10-fehlerbild-atlas)
11. [Troubleshooting](#11-troubleshooting)
12. [Segelvermessung und -analyse](#12-segelvermessung-und--analyse)
13. [FAQ — Häufige Fragen](#13-faq--häufige-fragen)
14. [Glossar](#14-glossar)
15. [Schnell-Referenz](#15-schnell-referenz)
16. [ANHANG A — Fallstudie: Regatta-Großsegel Bavaria 40](#anhang-a--fallstudie-regatta-großsegel-bavaria-40)
17. [ANHANG B — Fallstudie: Fahrtensegel-Trimm Hallberg-Rassy 44](#anhang-b--fallstudie-fahrtensegel-trimm-hallberg-rassy-44)
18. [ANHANG C — Fallstudie: Code 0 Optimierung J/111](#anhang-c--fallstudie-code-0-optimierung-j111)
19. [ANHANG D — Fallstudie: Membransegel vs. Tri-Radial Swan 53](#anhang-d--fallstudie-membransegel-vs-tri-radial-swan-53)
20. [ANHANG E — Fallstudie: Langfahrt-Segelgarderobe Oyster 565](#anhang-e--fallstudie-langfahrt-segelgarderobe-oyster-565)
21. [ANHANG F — Fallstudie: Rollgroßsegel-Problematik Beneteau Oceanis 51.1](#anhang-f--fallstudie-rollgroßsegel-problematik-beneteau-oceanis-511)
22. [ANHANG G — Fallstudie: Performance-Cruiser Dehler 46 Segeltrimm](#anhang-g--fallstudie-performance-cruiser-dehler-46-segeltrimm)
23. [ANHANG H — Fallstudie: Klassische Yacht — Dacron-Segel Restoration](#anhang-h--fallstudie-klassische-yacht--dacron-segel-restoration)
24. [ANHANG I — AYDI-Integration: Pydantic-Modelle Segelschnitt](#anhang-i--aydi-integration-pydantic-modelle-segelschnitt)
25. [ANHANG J — AYDI-Integration: Pydantic-Modelle Segeltrimm](#anhang-j--aydi-integration-pydantic-modelle-segeltrimm)
26. [ANHANG K — AYDI-Integration: Pydantic-Modelle Fehlerbild](#anhang-k--aydi-integration-pydantic-modelle-fehlerbild)
27. [ANHANG L — AYDI-Integration: Bewertungsschema](#anhang-l--aydi-integration-bewertungsschema)
28. [ANHANG M — AYDI-Integration: Trimm-Empfehlungsengine](#anhang-m--aydi-integration-trimm-empfehlungsengine)
29. [ANHANG N — AYDI-Integration: Visueller Segelanalyse-Prompt](#anhang-n--aydi-integration-visueller-segelanalyse-prompt)
30. [ANHANG O — AYDI-Integration: Segelverschleiß-Scoring](#anhang-o--aydi-integration-segelverschleiß-scoring)
31. [ANHANG P — AYDI-Integration: Confidence-Mapping Segel](#anhang-p--aydi-integration-confidence-mapping-segel)
32. [ANHANG Q — AYDI-Integration: Troubleshooting-Entscheidungsbaum](#anhang-q--aydi-integration-troubleshooting-entscheidungsbaum)
33. [ANHANG R — AYDI-Integration: Schnittmethoden-Vergleichsmodell](#anhang-r--aydi-integration-schnittmethoden-vergleichsmodell)

---

## 1. Einführung

### 1.1 Warum Segelschnitt und Trimm zusammengehören

Ein Segel ist kein statisches Bauteil — es ist ein dreidimensionaler Tragflügel, dessen Form sich unter Windlast, Materialspannung und Trimmeinstellung permanent verändert. Der Segelschnitt (englisch: sail design/cut) definiert das Potenzial; der Trimm realisiert es auf dem Wasser.

Diese Wissensdatei behandelt beide Aspekte als untrennbare Einheit:

- **Segelschnitt**: Wie wird die dreidimensionale Form in zweidimensionale Stoffbahnen übersetzt? Welche Schnittmethode eignet sich für welchen Einsatzzweck? Wie beeinflussen Materialwahl und Paneelanordnung die Langzeitformstabilität?
- **Segeltrimm**: Wie wird die eingebaute Form unter variablen Bedingungen (Wind, Kurs, Seegang) optimal aktiviert? Welche Instrumente stehen zur Verfügung, und wie interagieren sie?

### 1.2 Historische Entwicklung

Die Geschichte des Segelschnitts ist eine Evolution von Handwerk zu High-Tech:

**Vor 1960 — Ära des Baumwollsegels:**
- Schnitt nach Erfahrung und Augenmaß
- Horizontale Stoffbahnen (Cross-Cut) als einzige Methode
- Formgebung durch Nähen und Dehnung des Gewebes
- Segel mussten vor Gebrauch gewässert werden (Faserschwellung für Dichtigkeit)
- Segelform: bauchig, wenig Höhe am Wind, kurze Lebensdauer (1–3 Saisons)

**1960–1980 — Dacron-Revolution:**
- DuPont Dacron (Polyester) ersetzt Baumwolle
- Deutlich geringere Dehnung, höhere UV-Beständigkeit
- Cross-Cut bleibt dominierend, aber Broadseaming ermöglicht gezielte Formgebung
- Erste computergestützte Entwürfe (Ted Hood, Lowell North)
- Segel halten 5–10 Saisons
- Preise: Großsegel 40-Fuß ca. 1.500–3.000 DM

**1980–2000 — Laminate und Radialschnitt:**
- Mylar/Kevlar-Laminate für Regattasegel
- Tri-Radial-Schnitt optimiert Faserausrichtung
- Computergestütztes Design wird Standard
- Windkanaltests bei North Sails, Sobstad, Hood
- Segel werden flacher, effizientere Höhelaufprofile

**2000–2015 — Membrantechnologie:**
- North Sails 3DL: Filamente auf Formkörper gelegt
- Elvstrom EPEX: thermisch verschweißte Paneele
- Dimension Polyant Laminate für Drittanbieter
- Entfall traditioneller Nähte bei Hochleistungssegeln
- Preise: Membran-Großsegel 40-Fuß ab ca. 8.000 EUR

**2015–heute — 3Di und digitale Fertigung:**
- North Sails 3Di: gespreizte Filamente in Thermokunststoffmatrix
- Doyle Stratis: Filamente direkt auf Segel-Skin gelegt
- OneSails 4T Forte: thermogeformte Paneele
- Quantum Fusion M: membranartige Paneel-Technologie
- Inkjet-Druck für Logos und Segelkennzeichen
- Preise: 3Di Großsegel 40-Fuß ab ca. 12.000–18.000 EUR

### 1.3 Bedeutung für die Praxis

Für den Fahrtensegler ist korrekt getrimmtes Dacron-Cross-Cut-Segel fast immer besser als ein schlecht getrimmtes Laminsegel. Die Hierarchie der Einflussfaktoren auf die Segelleistung:

1. **Segelform (Trimm)** — 40% des Leistungspotenzials
2. **Segelplan-Balance** — 20%
3. **Segelmaterial und -zustand** — 15%
4. **Schnittmethode** — 10%
5. **Anstellwinkel (Schot/Traveller)** — 10%
6. **Oberflächenqualität** — 5%

**Confidence: documented** — basierend auf Windkanalstudien MIT/Webb Institute und Regattadatenanalyse

### 1.4 Geltungsbereich dieser Wissensdatei

Diese Datei deckt ab:
- Segel für Einrumpf-Segelyachten 7–25 m (CE-Kategorie A–C)
- Vorstags-/Rollvorsegel, Großsegel (Baum/In-Mast/In-Boom-Reff), Code-Segel
- Fahrtensegel, Performance-Cruiser-Segel und Club-Regattasegel
- Nicht abgedeckt: Mehrrumpfboote (partiell), Vollregatta/America's Cup, Windsurfen, Kitesegel

### 1.5 Relevante Normen und Messstandards

| Standard | Beschreibung | Relevanz |
|----------|-------------|----------|
| ISAF/World Sailing ERS | Equipment Rules of Sailing | Vermessungsregeln, Segelmaße |
| ORC Rating | Offshore Racing Congress | VPP-Segelparameter |
| IRC Rule | RORC Rating | Segelflächenberechnung |
| EN ISO 12217 | Stabilitätsberechnung | Segelfläche vs. Stabilität |
| DIN EN ISO 12215-10 | Rigg-Lasten und Rigg-Befestigung | Lasten auf Segel/Rigg-Verbindung |

### 1.6 Terminologie-Konvention

In dieser Datei werden deutsche Fachbegriffe bevorzugt, mit englischem Äquivalent in Klammern bei Erstnennung. Viele Segeltrimm-Begriffe sind im Deutschen international etabliert:
- Schothornausholer = Outhaul
- Unterliekstrecker = Outhaul (synonym)
- Vorliekstrecker = Cunningham
- Baumniederholer = Vang / Kicking Strap
- Großschot = Mainsheet
- Achterstag = Backstay
- Vorstag = Forestay / Headstay
- Holepunkt = Sheet Lead / Car Position
- Trimm = Trim (allgemein)
- Segellatten = Battens
- Achterliek = Leech
- Vorliek = Luff
- Unterliek = Foot
- Kopf = Head
- Schothorn = Clew
- Hals = Tack

---

## 2. Grundlagen der Segelformgebung

### 2.1 Das Segel als aerodynamischer Körper

Ein Segel funktioniert physikalisch als dünnes, gekrümmtes Profil (Tragflügelprofil), das Auftrieb erzeugt. Im Gegensatz zu einem starren Flugzeugflügel verformt sich das Segel unter Last — es ist ein flexibles, membranartiges System.

**Grundlegende Aerodynamik:**

Der Auftrieb (Lift) eines Segels entsteht durch Druckunterschiede zwischen Lee- und Luvseite:
- **Leeseite**: beschleunigte Strömung → Unterdruck (ca. 2/3 des Gesamtauftriebs)
- **Luvseite**: verzögerte Strömung → Überdruck (ca. 1/3 des Gesamtauftriebs)

Die resultierende Kraft teilt sich in:
- **Vortriebskraft** (Komponente in Fahrtrichtung)
- **Seitenkraft/Krängung** (Komponente quer zur Fahrtrichtung)
- **Induzierter Widerstand** (durch Wirbelbildung am Segel-Kopf und -Fuß)

**Anstellwinkel und Strömungsabriss:**
- Optimaler Anstellwinkel (Angle of Attack): 15–25° je nach Profiltiefe
- Strömungsabriss (Stall): ab ca. 30–35° — Lee-Strömung löst sich ab
- Am Wind: kleiner Anstellwinkel, flaches Profil → hoher Lift/Drag-Quotient
- Vorwind: großer Anstellwinkel, bauchiges Profil → maximaler Vortrieb

### 2.2 Profilparameter — Bauchtiefe (Draft/Camber)

Die Bauchtiefe (auch: Wölbung, Camber) ist der maximale Abstand der Segelmitte (Chord Line) zur tatsächlichen Segelkurve, ausgedrückt als Prozentsatz der Profiltiefe (Chord Length).

**Typische Bauchtiefen:**

| Segel / Einsatz | Bauchtiefe | Anwendung |
|-----------------|-----------|-----------|
| Flach getrimmt am Wind (frisch) | 6–8% | Hoch am Wind bei 18+ kn |
| Moderat am Wind | 10–12% | Standard-Amwind-Trimm 8–16 kn |
| Leichtwind am Wind | 12–15% | Leichtwind <8 kn, Power gefragt |
| Halbwind | 12–16% | Raumschotkurse |
| Raumschots/Vorwind | 15–20% | Maximum Vortrieb |
| Spinnaker | 18–30% | Reine Vortriebsmaximierung |
| Code 0 | 10–14% | Leichtwind-Reaching |

**Bauchtiefe und Windstärke:**
- Mehr Wind → flacheres Profil (weniger Bauch) → weniger Krängung
- Weniger Wind → bauchigeres Profil → mehr Auftrieb bei geringer Strömungsgeschwindigkeit
- Faustformel: Bei Verdopplung der Windgeschwindigkeit → Bauchtiefe um ~30% reduzieren

**Confidence: measured** — Windkanalstudien (North Sails Design Suite, MARIN Institute)

### 2.3 Bauchposition (Draft Position)

Die Bauchposition gibt an, wo sich der tiefste Punkt des Profils befindet, gemessen vom Vorliek als Prozent der Profiltiefe.

**Optimale Bauchpositionen:**

| Bedingung | Bauchposition | Erläuterung |
|-----------|--------------|-------------|
| Leichtwind (<8 kn) | 45–50% | Weiter achtern für toleranteres Profil |
| Mittelwind (8–16 kn) | 38–42% | Standard-Position |
| Frischer Wind (16–25 kn) | 33–38% | Weiter vorn für Depowering |
| Schwerwetter (>25 kn) | 28–35% | Maximal vorn, flaches Exit-Profil |
| Raumschots | 45–55% | Bauchiger, tolerantes Profil |

**Manipulation der Bauchposition:**
- **Vorliekstrecker (Cunningham)**: Zieht den Bauch nach vorn
- **Schot/Traveller**: Beeinflusst den Anstellwinkel
- **Achterstag**: Biegt den Mast → verschiebt Bauch nach vorn
- **Großfall (Halyard)**: Leicht nachlassen → Bauch wandert nach achtern

### 2.4 Eintrittswinkel (Entry Angle)

Der Eintrittswinkel ist der Winkel des Segelprofils am Vorliek, wo die Luft auf das Segel trifft. Er bestimmt maßgeblich, wie hoch am Wind gesegelt werden kann und wie tolerant das Segel gegenüber Windwinkeländerungen ist.

**Typische Eintrittswinkel:**

| Segeltyp | Eintrittswinkel | Charakteristik |
|----------|----------------|---------------|
| Regatta am Wind (flach) | 5–8° | Sehr hoch am Wind, aber empfindlich |
| Fahrtensegel am Wind | 10–15° | Toleranter, etwas weniger Höhe |
| Genua überlappend | 8–12° | Breiterer Groove |
| Selbstwendefock | 12–18° | Sehr tolerant, weniger Höhe |
| Code 0 | 6–10° | Quasi Amwind-Segel für leichte Winde |

**Eintrittswinkel und Vorstag-Durchhang:**
Bei Rollvorsegeln beeinflusst der Durchhang des Vorstags (Forestay Sag) den Eintrittswinkel erheblich:
- 50 mm Durchhang bei 13 m Vorstag → ca. 3° zusätzlicher Eintrittswinkel
- 100 mm Durchhang → ca. 6° zusätzlich
- Gegenmaßnahme: Achterstag spannen, Babystag, Running Backstays

### 2.5 Austrittswinkel (Exit Angle)

Der Austrittswinkel am Achterliek bestimmt, wie die Luft das Segel verlässt. Er wird primär durch Twist und Achterliek-Spannung kontrolliert.

**Auswirkungen:**
- **Geschlossenes Achterliek** (kleiner Exit Angle): Mehr Auftrieb, aber höherer induzierter Widerstand. Risiko: Achterliek-Hook, Strömungsabriss
- **Offenes Achterliek** (großer Exit Angle): Weniger Widerstand, weniger Auftrieb, reduzierte Krängung
- **Optimum**: Achterliek gerade bis leicht geöffnet, Leechtelltales strömen 80–90% der Zeit

### 2.6 Twist

Twist bezeichnet die Verdrehung des Segels von unten nach oben. Am Fuß ist das Segel dichter geholt (geschlossener Anstellwinkel), am Kopf offener.

**Warum Twist notwendig ist:**

1. **Windgradient**: Die Windgeschwindigkeit nimmt mit der Höhe zu (Grenzschichteffekt). Am Masttopp weht es ca. 10–20% stärker als in Deckhöhe. Da der scheinbare Wind mit höherer Geschwindigkeit weiter vorlich dreht, muss das Segel oben offener stehen.

2. **Induzierter Widerstand**: Optimale Lastverteilung (elliptisch) erfordert reduzierten Auftrieb an der Spitze.

3. **Böentoleranz**: Twist ermöglicht automatisches Depowering bei Böen — der obere Segelbereich öffnet sich, Krängungsmoment reduziert sich.

**Twist-Kontrolle:**
- **Großschot**: Hauptinstrument — dichter = weniger Twist, fieren = mehr Twist
- **Traveller**: Verändert den Grundanstellwinkel ohne Twist zu beeinflussen
- **Vang (Baumniederholer)**: Kontrolliert Twist auf Raumschotkursen, wo die Schot den Baum nicht nach unten zieht
- **Holepunkt (Sheet Lead)**: Beim Vorsegel — weiter vorn = weniger Twist, weiter achtern = mehr Twist

**Optimaler Twist nach Windstärke:**

| Windstärke | Twist (Großsegel) | Twist (Vorsegel) |
|------------|-------------------|-------------------|
| 0–6 kn | Minimal (Schot dicht) | Minimal |
| 6–12 kn | Moderat | Moderat |
| 12–18 kn | Moderat bis offen | Moderat |
| 18–25 kn | Offen (Depowering) | Offen |
| 25+ kn | Maximal offen | Maximal offen |

### 2.7 Slot-Effekt (Slot Effect)

Der Slot ist der Spalt zwischen Achterliek des Vorsegels und Luvseite des Großsegels. In diesem Bereich interagieren die Strömungsfelder beider Segel.

**Physikalische Wirkung:**
- Das Vorsegel beschleunigt die Strömung in den Slot → die Luv-Strömung am Großsegel wird energetisiert
- Das Großsegel erzeugt einen Upwash am Achterliek des Vorsegels → der effektive Anstellwinkel des Vorsegels erhöht sich
- Resultat: Beide Segel erzeugen zusammen mehr Auftrieb als die Summe einzeln

**Slot-Dimensionierung:**
- Zu eng (Vorsegel zu dicht geholt): Stau → Leeseite Großsegel wird gestört, erhöhter Widerstand
- Zu weit (Vorsegel zu weit offen): Kein Slot-Effekt, Segel arbeiten unabhängig
- Optimal: Achterliek-Vorsegel parallel oder leicht divergierend zur Luvseite Großsegel

**Visualisierung — Slot-Breite:**
Am Achterliek des Vorsegels sollte bei optimaler Einstellung ein gleichmäßiger Abstand von:
- Überlappende Genua (130–155%): 15–25 cm Abstand zum Großsegel in Baumhöhe
- Nicht überlappende Fock (100–108%): Slot ist weiter, weniger Interaktion
- Selbstwendefock: Sehr weiter Slot, geringer Effekt

### 2.8 Segelschwerpunkt (CE) und Lateralplan-Schwerpunkt (CLR)

**CE — Centre of Effort:**
Der Druckpunkt des gesamten Segelplans. Verschiebung nach achtern erzeugt Luvgierigkeit, nach vorn Leegierigkeit.

**CLR — Centre of Lateral Resistance:**
Der Schwerpunkt des Unterwasser-Lateralplans (Kiel, Ruder, Rumpf).

**CE-CLR-Beziehung:**
- Standard-Lead (CE vor CLR): 5–12% der Wasserlinienlänge
- Fahrtenyacht: 8–12% Lead (leicht luvgierig gewünscht)
- Regattayacht: 5–8% Lead (neutraler, aber erfordert Aufmerksamkeit)
- Moderner Kiel-/Ruder-Plan (Spatenruder): 10–15% Lead

**Trimm-Einfluss auf CE:**
- Großsegel dichter → CE wandert nach achtern → mehr Luvgierigkeit
- Vorsegel dichter → CE wandert nach vorn → weniger Luvgierigkeit
- Reff im Groß → CE wandert nach vorn
- Segelwechsel (kleine Fock statt Genua) → CE wandert nach achtern (weniger Fläche vorn)

**Confidence: documented** — Larsson/Eliasson "Principles of Yacht Design", Marchaj "Sail Performance"

### 2.9 Profiltiefe (Chord Length) und Aspektverhältnis (Aspect Ratio)

**Aspektverhältnis = Segelhöhe² / Segelfläche**

| Segeltyp | Aspect Ratio | Charakteristik |
|----------|-------------|---------------|
| Hohes AR Großsegel (≥3.5) | Regatta | Weniger induzierter Widerstand, höher am Wind |
| Mittleres AR (2.5–3.5) | Fahrtenyacht | Kompromiss Leistung/Handling |
| Niedriges AR (≤2.5) | Ketsch, Schoner | Niedrigerer Schwerpunkt, einfacheres Reffen |
| Hohes AR Vorsegel | Regatta-Fock | Höhe am Wind, aber weniger Power |
| Niedriges AR Genua | Fahrtenyacht | Mehr Power, weniger Höhe |

**Einfluss auf Segelschnitt:**
- Hohes AR → engere Broadseam-Verteilung, feinere Profile oben
- Niedriges AR → breitere Paneele, gleichmäßigere Bauchverteilung

### 2.10 Auftriebsverteilung und induzierter Widerstand

Die ideale Auftriebsverteilung über die Segelhöhe ist elliptisch — ähnlich wie bei Flugzeugflügeln. Dies minimiert den induzierten Widerstand.

**Praktische Umsetzung:**
- Twist sorgt für reduzierten Auftrieb am Segelkopf
- Segellatten am Achterliek halten oben mehr Fläche → tendenziell höherer Auftrieb
- Kompromiss: Latten-Großsegel mit moderatem Twist nähert sich elliptischer Verteilung an
- Full-Batten-Segel: besser kontrollierbares Profil über gesamte Höhe

**Druckverteilung messen:**
- Telltales in verschiedenen Höhen (4–5 Streifen)
- Streifen-Analyse-Fotos (Stripe Analysis)
- Elektronische Drucksensoren (nur Regatta-Hochleistung)

---

## 3. Schnittmethoden

### 3.1 Überblick und Vergleich

| Methode | Paneel-Richtung | Material | Formstabilität | Preis (40-Fuß Groß) | Lebensdauer |
|---------|----------------|----------|---------------|---------------------|-------------|
| Cross-Cut | Horizontal | Dacron | ★★★☆☆ | 2.500–5.000 EUR | 6–12 Jahre |
| Tri-Radial | Radial 3-Zonen | Dacron/Laminat | ★★★★☆ | 4.000–8.000 EUR | 5–10 Jahre |
| Radial (Vollradial) | Von Ecken ausgehend | Laminat | ★★★★☆ | 5.000–9.000 EUR | 4–8 Jahre |
| Membran (3DL) | Filamente auf Form | Dyneema/Carbon | ★★★★★ | 12.000–22.000 EUR | 3–7 Jahre |
| 3Di | Gespreizte Filamente | Carbon/Dyneema | ★★★★★ | 14.000–25.000 EUR | 5–10 Jahre |
| Stratis (Doyle) | Filamente auf Skin | Dyneema/Carbon | ★★★★★ | 12.000–20.000 EUR | 5–9 Jahre |
| EPEX (Elvstrom) | Thermopaneele | Laminat | ★★★★☆ | 6.000–12.000 EUR | 5–8 Jahre |

**Confidence: estimated** — Herstellerangaben, Marktkonsens 2025/2026

### 3.2 Cross-Cut (Horizontalschnitt)

#### Prinzip
Beim Cross-Cut werden die Stoffbahnen (Paneele) horizontal angeordnet, d.h. senkrecht zum Achterliek. Dies ist die älteste und einfachste Schnittmethode.

#### Paneelanordnung
```
      HEAD
      / |
     /  |
    / P5|
   / P4 |
  / P3  |
 / P2   |
/ P1    |
TACK----CLEW
  (Horizontal Paneele P1-P5)
```

Die Paneele verlaufen von der Vorliekkurve bis zum Achterliek. Jedes Paneel ist leicht gewölbt zugeschnitten (Broadseaming), um die dreidimensionale Segelform zu erzeugen.

#### Stressverteilung
- **Kettrichtung (Warp)**: Vertikal — nimmt die Hauptlast auf (Hals→Kopf, Schot→Achterliek)
- **Schussrichtung (Fill/Weft)**: Horizontal — entlang der Paneele
- **Problem**: Die Hauptlasten (diagonal Hals→Schothorn, Kopf→Schothorn) verlaufen weder in Kett- noch in Schussrichtung. Sie belasten das Gewebe in der Bias-Richtung (diagonal), wo die Dehnung maximal ist.

#### Materialwahl
- **Dacron (Polyester-Tuch)**: Standard für Cross-Cut. Fill-oriented (Schussfaden-orientiert) für höhere Festigkeit in Paneel-Richtung. Hersteller: Dimension Polyant, Contender, Bainbridge
- **Typische Gewebegewichte:**

| Bootslänge | Großsegel (g/m²) | Vorsegel (g/m²) |
|-----------|-----------------|-----------------|
| 7–9 m | 170–220 | 150–200 |
| 9–12 m | 220–280 | 200–250 |
| 12–15 m | 280–350 | 250–310 |
| 15–20 m | 350–420 | 310–380 |
| 20–25 m | 420–520 | 380–460 |

#### Vorteile Cross-Cut
1. Günstigster Schnitt (geringer Verschnitt, einfache Fertigung)
2. Einfach zu reparieren (horizontale Nähte, Standard-Material)
3. Langlebig bei Dacron-Tuch
4. UV-beständig (Dacron)
5. Tolerant gegenüber Falten (Rollreff, Lazybag)
6. Ideal für Fahrtensegel, Rollsegel, Sturmbesegelung

#### Nachteile Cross-Cut
1. Höchste Bias-Dehnung → Form verschlechtert sich mit der Zeit (Bauch wandert nach achtern)
2. Nicht optimal für hohe Windlasten
3. Geringere Formstabilität als Radial-Schnitte
4. Bei Laminaten nicht sinnvoll (Laminate nutzen Faserausrichtung)

#### Preisspektrum (2025/2026)

| Bootslänge | Großsegel Cross-Cut | Genua Cross-Cut |
|-----------|-------------------|----------------|
| 30 Fuß | 1.500–2.800 EUR | 1.200–2.200 EUR |
| 35 Fuß | 2.200–3.800 EUR | 1.800–3.200 EUR |
| 40 Fuß | 2.800–5.000 EUR | 2.400–4.500 EUR |
| 45 Fuß | 3.800–6.500 EUR | 3.200–5.500 EUR |
| 50 Fuß | 5.000–8.500 EUR | 4.200–7.000 EUR |

**Hersteller Cross-Cut (Auswahl):**
- Rolly Tasker Sails (Thailand) — hervorragendes Preis-Leistungs-Verhältnis
- Quantum Sails — FusionM für Performance-Cruiser
- North Sails — NORDAC Serie
- Elvstrom Sails — Fahrtensegel
- UK Sailmakers — Tape-Drive Cross-Cut (verstärkte Lastpfade)
- Ullman Sails — Standard Dacron-Serie
- Sanders Sails (Deutschland) — lokale Fertigung
- Latsch Sails (Deutschland) — Bodensee-Region
- Rolly Tasker / Lee Sails — Hong Kong/Thailand Fertigung

### 3.3 Tri-Radial (Dreizonen-Radialschnitt)

#### Prinzip
Der Tri-Radial-Schnitt teilt das Segel in drei Zonen, wobei die Paneele jeweils radial von einem der drei Ecken (Hals, Kopf, Schothorn) ausgehen. Die Paneelanordnung folgt den Hauptlastpfaden.

#### Paneelanordnung
```
         HEAD
        /|\  \
       / | \  \
      / Zone \  \
     / Kopf   \  \
    /    |     \   \
   / Zone| Zone \   \
  / Hals |Schoth.\   \
 /       |        \   \
TACK-----+---------CLEW
```

**Drei Zonen:**
1. **Hals-Zone (Tack Zone)**: Paneele strahlen vom Hals aus → fängt Vorliek-Lasten ab
2. **Kopf-Zone (Head Zone)**: Paneele strahlen vom Kopf aus → fängt Fall-Lasten ab
3. **Schothorn-Zone (Clew Zone)**: Paneele strahlen vom Schothorn aus → fängt Schot-Lasten ab

Die Nähte (Seams) zwischen den Zonen verlaufen entlang der Hauptlastpfade, wo Dehnung am kritischsten ist. Die Faserorientierung des Materials wird so optimiert.

#### Stressverteilung
- Deutlich bessere Lastpfad-Orientierung als Cross-Cut
- Bias-Dehnung reduziert um 30–50% gegenüber Cross-Cut
- Besonders vorteilhaft in den hochbelasteten Eckbereichen
- Mittlerer Segelbereich profitiert weniger (Kompromiss-Orientierung)

#### Materialwahl
- **Dacron (Polyester)**: Warp-oriented für radiale Paneele (Kettfaden in Paneel-Längsrichtung)
- **Pentex (High-Modulus Polyester)**: 30–40% geringere Dehnung als Standard-Dacron
- **Leichte Laminate**: Für Performance-Cruiser geeignet
- **Hydra Net (Dimension Polyant)**: Gitterlaminate mit radialer Faserverstärkung

#### Vorteile Tri-Radial
1. Bessere Formstabilität als Cross-Cut (Bauch bleibt länger an der richtigen Stelle)
2. Kann aus Dacron oder Laminat gefertigt werden
3. Moderater Preis bei deutlichem Leistungsgewinn
4. Guter Kompromiss für Performance-Cruiser
5. Reparierbar (wenn auch aufwendiger als Cross-Cut)
6. Geringerer Bias-Stretch in den kritischen Ecken

#### Nachteile Tri-Radial
1. Höherer Verschnitt (mehr dreieckige Reststücke) → teurer
2. Mehr Nähte → potenziell mehr Schwachstellen
3. Aufwendigere Fertigung → längere Lieferzeiten
4. Bei reinem Dacron nur ca. 15–20% besser als Cross-Cut

#### Preisspektrum (2025/2026)

| Bootslänge | Großsegel Tri-Radial (Dacron) | Großsegel Tri-Radial (Laminat) |
|-----------|------------------------------|-------------------------------|
| 30 Fuß | 2.200–3.800 EUR | 3.500–5.500 EUR |
| 35 Fuß | 3.200–5.200 EUR | 5.000–7.500 EUR |
| 40 Fuß | 4.000–7.000 EUR | 6.500–10.000 EUR |
| 45 Fuß | 5.500–9.000 EUR | 8.000–13.000 EUR |
| 50 Fuß | 7.500–12.000 EUR | 11.000–17.000 EUR |

### 3.4 Radialschnitt (Vollradial)

#### Prinzip
Beim Vollradialschnitt gehen alle Paneele von den Ecken oder Segelkanten aus. Es gibt keine horizontalen Paneele. Die Materialfasern verlaufen konsequent entlang der Lastpfade.

#### Typische Anwendung
- Spinnaker (immer radial, da symmetrische Last vom Kopf)
- Regatta-Vorsegel (Laminate)
- Code-Segel (Code 0, A-Segel, Gennaker)

**Bei Spinnakern:**
```
         HEAD
        / | \
       /  |  \
      / R | R \
     / a  |  a \
    / d   |   d \
   / i    |    i \
  / a     |     a \
 / l      |      l \
TACK------+------CLEW
```

Alle Paneele strahlen vom Kopf nach unten — maximale Formkontrolle im oberen, hochbelasteten Bereich.

#### Materialwahl
- Nylon (Spinnaker): 20–60 g/m² (0.5 oz, 0.75 oz, 1.5 oz)
- Laminat (Vorsegel): Mylar/Dyneema, Mylar/Technora, Mylar/Carbon
- Dimension Polyant D4 Serie: Standard für Regatta-Laminate
- Contender CX Serie: Alternative Laminate

### 3.5 Membran-/Filament-Technologien

#### 3.5.1 North Sails 3DL (Dreidimensional laminiert)

**Verfahren:**
1. Computergestützte Berechnung der Lastpfade (Finite-Elemente-Analyse)
2. Ein glatter Formkörper (Mold) in der exakten Segelform wird aufgeblasen
3. Filamente (Dyneema, Vectran, Carbon, Technora) werden auf den Formkörper gelegt — exakt entlang der berechneten Lastpfade
4. Mylar-Folien oben und unten einlaminiert
5. Thermische Aushärtung im Autoklaven

**Materialien:**
- 3DL Endurance: Dyneema-Filamente — langlebig, UV-beständig
- 3DL Regatta: Carbon-Filamente — maximale Steifigkeit, geringes Gewicht
- 3DL Performance: Mischung Dyneema/Carbon

**Vorteile:**
- Exakte Formgebung ohne Nähte als Schwachstellen
- Filamente exakt entlang der Lastpfade
- Geringste Dehnung in der Klasse (Ausnahme: 3Di)
- Sehr glattes Finish

**Nachteile:**
- Empfindlich gegenüber Falten und Knicken (Mylar bricht)
- Nicht für Rollreff geeignet (außer Spezialversionen)
- Delamination nach 3–5 Jahren (besonders an Faltstellen)
- Reparatur nur bei North Sails möglich
- Hoher Preis: 40-Fuß-Großsegel 12.000–18.000 EUR
- **Eingestellt seit 2023** — North Sails konzentriert sich auf 3Di

**Confidence: documented** — North Sails Technische Dokumentation

#### 3.5.2 North Sails 3Di

**Verfahren:**
1. Filamente werden in dünne, gespreizte Bänder (Spread Tow Tapes) aufgelöst
2. Mehrere Lagen Filamente in unterschiedlichen Winkeln übereinandergelegt
3. In Thermokunststoff-Matrix (nicht Mylar) eingebettet
4. Unter Hitze und Druck verschmolzen
5. Entstehen als Panels, die dann zusammengefügt werden

**Produktlinien (2025/2026):**

| Produkt | Filament | Zielgruppe | Preis 40-Fuß Groß |
|---------|----------|-----------|-------------------|
| 3Di NORDAC | Polyester + Dyneema | Fahrtensegel | 8.000–12.000 EUR |
| 3Di ENDURANCE | Dyneema dominant | Performance Cruiser | 12.000–16.000 EUR |
| 3Di 780 | Dyneema/Carbon Mix | Club-Regatta | 14.000–20.000 EUR |
| 3Di RAW | Carbon dominant | Offshore-Regatta | 18.000–25.000 EUR |
| 3Di RAW+C | Carbon High-Modulus | Grand Prix | 22.000–35.000 EUR |

**Vorteile gegenüber 3DL:**
- Keine Mylar-Folie → kein Delaminations-Risiko
- Kann gerollt/gefaltet werden (eingeschränkt)
- Längere Lebensdauer (5–10 Jahre vs. 3–7 Jahre)
- Besseres Handling (fühlt sich an wie Tuch, nicht wie Folie)
- Teilweise rollrefftauglich (3Di NORDAC)

**Nachteile:**
- Höchster Preis auf dem Markt
- Nur über North Sails Lofts erhältlich
- Spezial-Reparatur erforderlich
- Nicht UV-resistent (bei Carbon-Varianten Schutzschicht nötig)

**Confidence: measured** — North Sails Engineering Data, unabhängige Tests Seahorse Magazine

#### 3.5.3 Doyle Sails Stratis

**Verfahren:**
1. Computergestützte Lastpfad-Berechnung
2. Segelprofil wird auf flache Membranen (Taffeta-Skins) projiziert
3. Filamente (Dyneema, Vectran, Technora, Carbon) werden direkt auf die Skin gelegt
4. Laser-positionierte Filamentbahnen
5. Zweite Skin aufgebracht und thermisch verbunden
6. Kein Formkörper nötig → günstigere Produktion als 3DL

**Produktlinien:**
- Stratis ICE: Dyneema-Filamente — Fahrtensegel
- Stratis GTX: Performance Cruising
- Stratis GP: Grand Prix Regatta (Carbon)

**Vorteile:**
- Günstiger als 3Di (ca. 15–25% weniger)
- Lokale Lofts weltweit (Doyle Franchise-System)
- Gute Reparierbarkeit (Skin-Patches)
- Flexible Filamenten-Kombinationen

**Nachteile:**
- Formgenauigkeit etwas unter 3Di
- Skins können delaminieren (seltener als 3DL)
- Weniger Forschungsbudget als North Sails

**Preise 40-Fuß-Großsegel:** 10.000–18.000 EUR

#### 3.5.4 Elvstrom Sails EPEX

**Verfahren:**
1. Konventionelle Paneele aus Laminat
2. Paneele werden über eine beheizte 3D-Form thermogeformt
3. Nähte durch thermische Fügung (kein Faden) ersetzt
4. Resultat: nähtefreie Paneele mit vorgeformter 3D-Kurve

**Vorteile:**
- Günstiger als Membrantechnologie
- Bessere Formstabilität als genähte Laminate
- Reparierbar mit Standard-Laminatverfahren
- Guter Kompromiss Preis/Leistung

**Nachteile:**
- Nicht so formstabil wie echte Membransegel
- Thermogeformte Paneele können sich bei Hitze rückverformen
- Begrenzte Materialauswahl

**Preise 40-Fuß-Großsegel:** 6.000–10.000 EUR

#### 3.5.5 Weitere Membran-/Panel-Technologien

**Quantum Fusion M:**
- Filamente auf Laminat-Paneele aufgebracht
- Paneel-basiert (nicht nahtfrei wie 3Di)
- Guter Performance-Cruiser-Kompromiss
- Preis 40-Fuß Groß: 8.000–14.000 EUR

**OneSails 4T FORTE:**
- Thermogeformte Paneele
- Italienische Fertigung
- Gutes Preis-Leistungs-Verhältnis in Europa
- Preis 40-Fuß Groß: 6.000–11.000 EUR

**UK Sailmakers Tape-Drive X-Drive:**
- Taffeta-Laminate mit Faserverstärkungen (Tapes) in den Lastpfaden
- Cross-Cut-Grundstruktur mit radialen Verstärkungen
- Günstiger Einstieg in verstärkte Segel
- Preis 40-Fuß Groß: 4.500–8.000 EUR

**Incidence Sails (Frankreich):**
- Matrix Technology: Faser-verstärkte Laminat-Paneele
- Starke Präsenz im französischen Regattasegelmarkt
- Preis 40-Fuß Groß: 5.000–10.000 EUR

### 3.6 Entscheidungshilfe: Welcher Schnitt für welchen Einsatz?

| Einsatzzweck | Empfehlung | Begründung |
|-------------|-----------|-----------|
| Langfahrt (Blauwasser) | Cross-Cut Dacron | Reparierbar, langlebig, UV-beständig |
| Fahrtensegel (Mittelmeer/Ostsee) | Cross-Cut oder Tri-Radial Dacron | Preis/Leistung, Langlebigkeit |
| Performance Cruiser | Tri-Radial Laminat oder 3Di NORDAC | Formstabilität bei vertretbarer Lebensdauer |
| Club-Regatta | Tri-Radial Laminat oder Stratis | Performance vs. Budget |
| Offshore-Regatta | 3Di oder Stratis GP | Maximum Formstabilität und geringes Gewicht |
| Rollgroßsegel (In-Mast) | Cross-Cut Dacron | Muss rollbar bleiben, keine Latten |
| Rollgroßsegel (In-Boom) | Tri-Radial oder Cross-Cut | Mehr Optionen als In-Mast, Latten möglich |
| Sturmsegel | Cross-Cut Dacron (schwer) | Robustheit vor Performance |
| Code 0 / Gennaker | Radial Laminat oder Stratis | Leichtwind-Performance |

---

## 4. Formgebungstechniken

### 4.1 Broadseaming (Nahtformgebung)

Broadseaming ist die wichtigste Technik, um einem flachen Tuch eine dreidimensionale Form zu geben. Dabei werden die Paneele an den Nähten nicht gerade, sondern gewölbt zugeschnitten — beim Zusammennähen entsteht die gewünschte Segelwölbung.

**Prinzip:**
```
Paneel A (flach):     |===============|
                         \         /
Naht-Overlap (Broadseam): \=======/

Paneel B (flach):     |===============|
```

Durch das Wegschneiden von Material entlang der Naht werden die Paneele gezwungen, eine Kurve zu bilden. Mehr Material entfernt = mehr Wölbung an dieser Stelle.

**Broadseam-Verteilung für ein typisches Großsegel:**

| Segelhöhe | Broadseam max. | Bauchtiefe |
|-----------|---------------|-----------|
| 0–15% (Fuß-Bereich) | 15–25 mm | 10–14% |
| 15–40% | 20–35 mm | 11–15% |
| 40–60% (Mitte) | 25–40 mm | 10–13% |
| 60–80% | 15–30 mm | 8–11% |
| 80–100% (Kopf) | 5–15 mm | 5–8% |

**Computergestützte Broadseam-Berechnung:**
Moderne Segelmacher verwenden Software wie:
- SMAR Azure (Standard-Industrie-Software)
- North Sails Design Suite (proprietär)
- Sailpack (offenes System)
- Membrane FEA (Finite-Elemente-Analyse für Membransegel)

Der Computer berechnet für jede Naht das optimale Broadseam-Profil basierend auf:
- Gewünschtem Segelprofil (3D-Form)
- Materialeigenschaften (Dehnung in Kett-/Schuss-/Bias-Richtung)
- Erwarteter Windlast (Design-Windstärke)
- Nahtposition und -orientierung

### 4.2 Vorliekkurve (Luff Curve)

Die Vorliekkurve ist die Kurve, die das Vorliek (Vorderkante) des Segels relativ zu einer geraden Linie zwischen Hals und Kopf beschreibt.

**Großsegel — Vorliekkurve und Mast:**
- Das Vorliek des Großsegels liegt am Mast an
- Die Vorliekkurve muss zur Mastbiegung (Mast Bend) passen
- Mehr Mastbiegung → flacheres Segel (Vorliek wird gestreckt)
- Weniger Mastbiegung → bauchigeres Segel

**Typische Vorliekkurve Großsegel:**

| Mastprofil | Vorliekkurve max. | Position max. |
|-----------|------------------|--------------|
| Steifer Mast (Fahrt) | 40–80 mm | 40–50% Höhe |
| Mittlerer Mast | 80–130 mm | 42–48% Höhe |
| Weicher Mast (Regatta) | 120–200 mm | 40–45% Höhe |

**Zusammenspiel Mast Bend und Vorliekkurve:**
- Mastbiegung = Vorliekkurve → optimale Segelform (Segel wird flach bei Biegung)
- Mastbiegung < Vorliekkurve → Segel hat Falten am Vorliek
- Mastbiegung > Vorliekkurve → Segel wird invertiert (Bauch wird negativ) — GEFÄHRLICH

**Cunningham (Vorliekstrecker):**
Durch Anziehen des Cunningham wird das Vorliek unter Spannung gesetzt:
- Effekt: Bauch wandert nach vorn
- Das überschüssige Tuch am Vorliek wird nach unten gezogen
- Nützlich bei zunehmendem Wind zum Depowering

**Vorsegel — Vorliekkurve und Vorstag:**
- Das Vorliek des Vorsegels ist entlang des Vorstags gespannt
- Vorstag-Durchhang beeinflusst die effektive Vorliekkurve
- Mehr Durchhang → bauchigeres Segel, mehr Eintrittswinkel
- Weniger Durchhang (mehr Achterstag-Spannung) → flacheres Segel

### 4.3 Achterliekkurve (Leech Curve/Hollow)

Das Achterliek (Hinterkante) des Segels kann gerade, hohl (hollow) oder rund (roach) verlaufen.

**Leech Hollow (Hohlschnitt):**
- Material wird am Achterliek entfernt → nach innen gewölbte Kante
- Reduziert den induzierten Widerstand
- Standard bei Vorsegeln (weniger Flattern)
- Typisch: 1–3% der Profiltiefe
- Bei Regatta-Fock: bis 5% Hollow

**Leech Fall-off (Achterliek öffnet sich):**
- Kontrolliert durch Schot-Spannung und Latten
- Kontrollierter Fall-off reduziert Widerstand bei höheren Windstärken
- Zu viel Fall-off → Leistungsverlust

### 4.4 Roach (Achterliekausrundung — Großsegel)

Roach ist die Segelfläche, die über eine gerade Linie zwischen Kopf und Schothorn hinausragt. Sie wird durch Segellatten gestützt.

**Typische Roach-Werte:**

| Segeltyp | Roach (% der Verbindungslinie) |
|----------|-------------------------------|
| IOR-Großsegel (historisch) | 5–8% |
| IRC/ORC Regatta | 10–15% |
| Fahrtensegel | 8–12% |
| Full-Batten Fahrt | 12–18% |
| Square-Top Regatta | 18–25% |
| Katamaran-Großsegel | 15–22% |
| Rollgroßsegel (In-Mast) | 0% (kein Roach, keine Latten) |
| Rollgroßsegel (In-Boom) | 5–12% (mit Latten) |

**Roach und Segelfläche:**
- Jeder Prozentpunkt Roach erhöht die Segelfläche um ca. 1,5–2,5%
- Mehr Fläche = mehr Vortrieb, aber auch mehr Krängungsmoment
- Rating-Regeln (IRC, ORC) begrenzen oder bestrafen Roach

**Square-Top-Großsegel:**
- Extrem breiter Kopf mit sehr hohem Roach (20–25%)
- Ermöglicht durch Full-Batten und steife obere Latte
- Effektiv höherer Aspektratio → weniger induzierter Widerstand
- Populär bei: TP52, Melges 32, moderne Einhand-Sportboote
- Herausforderung: Oberes Paneel muss perfekt geschnitten sein

### 4.5 Fußrundung (Foot Round)

Die Fußrundung definiert die Segelfläche unterhalb einer geraden Linie zwischen Hals und Schothorn.

**Typen:**
- **Loose-Footed (ohne Unterlieksleine)**: Fuß hängt frei, Fußrundung erzeugt zusätzlichen Bauch im unteren Segel
- **Attached Foot (Unterliek auf Baum)**: Fuß ist am Baum befestigt, Fußrundung wird durch Outhaul kontrolliert
- **Shelf Foot**: Zusätzliches Paneel am Unterliek für mehr Fläche bei Leichtwind (bei Regatta-Segeln)

**Outhaul-Effekt auf Fußrundung:**
- Outhaul durchgesetzt → Fuß flach → weniger Bauch im unteren Segel
- Outhaul lose → Fuß bauchig → mehr Power im unteren Bereich
- Faustformel: Outhaul-Verstellung = 10–20 cm → ca. 2–4% Bauchtiefenänderung im unteren Drittel

### 4.6 Seam Shaping (Nahtformgebung — Detail)

Neben Broadseaming gibt es weitere Naht-basierte Formgebungstechniken:

**Luff Tabling:**
- Verstärkungsband entlang des Vorlieks
- Integriert die Vorliekkurve
- Breite: 50–150 mm je nach Segel/Belastung
- Tabling wird oft doppelt gelegt für Formkontrolle

**Leech Tabling:**
- Verstärkungsband am Achterliek
- Kontrolliert Stretch und Flattern
- Breite: 30–100 mm
- Bei Vorsegeln oft mit UV-Schutzband kombiniert

**Seam Profiling:**
- Computergesteuertes Nähen mit variablem Nahtabstand
- Mehr Stiche pro cm in hochbelasteten Bereichen
- Typisch: 4–6 Stiche/cm Standard, 8–10 Stiche/cm bei Eckpatches

**Patches und Verstärkungen:**
- Eckpatches (Hals, Kopf, Schothorn): Mehrlagig, oft Kevlar/Dyneema-Gewebe
- Reffpunkte: Zusätzliche Patches für Reff-Kauschen
- Latten-Taschen: Verstärkung an Latten-Enden
- Schamfil-Patches: Gegen Scheuern an Want/Saling

### 4.7 Panel-Layout-Optimierung

**Computergestützte Optimierung:**
Moderne Segelmacher-Software optimiert das Panel-Layout iterativ:

1. **Input**: Gewünschte 3D-Segelform, Material-Eigenschaften, Windlast-Szenario
2. **FEA-Berechnung**: Spannungs-/Dehnungsverteilung im Segel
3. **Paneel-Anordnung**: Software generiert optimale Panel-Grenzen
4. **Broadseam-Berechnung**: Für jede Naht wird die optimale Kurve berechnet
5. **Flachlegung (Flattening)**: 3D-Paneele werden in 2D-Schnittmuster umgewandelt
6. **Verschnitt-Optimierung**: Paneele werden auf Stoffbahn-Breiten optimiert (Nesting)

**Standard-Stoffbreiten:**
- Dacron: 91 cm (36"), 137 cm (54")
- Laminate: 137 cm (54"), 152 cm (60")
- Spinnaker-Nylon: 137 cm (54")

---

## 5. Latten-Design

### 5.1 Grundlagen und Funktion

Segellatten (Battens) stützen das Achterliek des Großsegels und halten den Roach offen. Ohne Latten würde die Segelfläche jenseits der Kopf-Schothorn-Linie nach Lee einfallen.

**Funktionen:**
1. Stützung des Roach
2. Verbesserung der Profilkontrolle über die gesamte Segelhöhe
3. Reduktion von Achterliek-Flattern
4. Ermöglichung kontrollierter Achterliek-Spannung
5. Verbesserung der Aerodynamik im oberen Segel (weniger Turbulenz am Austritt)
6. Absorbing von Schlag-Lasten (bei Wende/Halse)

### 5.2 Teillatten vs. Volllatten (Full Battens)

#### Teillatten (Partial Battens)
- Typische Länge: 60–100 cm (ca. 15–25% der lokalen Profiltiefe)
- Nur im Achterliek-Bereich → stützen Roach
- Standard bei den meisten Fahrtensegeln
- Meist 3–4 Latten bei Fahrtensegeln

**Vorteile Teillatten:**
- Geringeres Gewicht
- Einfacheres Reffen (keine Reibung an Latten)
- Weniger Verschleiß an Lattentaschen
- Kein Kompression-Loading am Mast

**Nachteile Teillatten:**
- Begrenzte Roach möglich (~8–12%)
- Kein durchgängiges Profil im Lattenlosen Bereich
- Achterliek-Flattern bei abfallendem Wind
- Chafe (Scheuern) an der inneren Lattenende-Position

#### Volllatten (Full Battens)
- Erstrecken sich über die gesamte Profiltiefe (Vorliek bis Achterliek)
- Standard bei modernen Regattasegeln und zunehmend bei Fahrtensegeln
- Meist 3–5 Latten bei Fahrtensegeln, 5–7 bei Regatta

**Vorteile Volllatten:**
- Deutlich bessere Profilkontrolle → gleichmäßigeres Profil
- Kein Flattern — Segel ist quasi-starr
- Größerer Roach möglich (15–25%)
- Reduzierter Verschleiß (weniger Schlagen)
- Bessere Leichtwind-Performance (Profil bleibt stehen)
- Verlängerte Segel-Lebensdauer (20–30% nach Studien)

**Nachteile Volllatten:**
- Mehr Gewicht (2–5 kg zusätzlich bei 40 Fuß)
- Reibung in Lattentaschen → schwereres Reffen
- Latten-Slides oder -Cars am Mast nötig
- Kompression am Mast → Mastbiegung wird beeinflusst
- Teurer (Latten + Beschläge)
- Bei Wende: verzögertes Umschlagen des Segels (Latten "haken" ein)

### 5.3 Latten-Materialien

| Material | Steifigkeit | Gewicht | Lebensdauer | Preis (Satz 4 Volllatten 40 Fuß) |
|----------|-----------|---------|-------------|----------------------------------|
| Fiberglas (GFK) | ★★★☆☆ | ★★★☆☆ | ★★★★☆ | 150–300 EUR |
| Carbon-GFK-Hybrid | ★★★★☆ | ★★★★☆ | ★★★★☆ | 300–600 EUR |
| Voll-Carbon | ★★★★★ | ★★★★★ | ★★★☆☆ | 600–1.500 EUR |
| Fiberglas verstärkt | ★★★★☆ | ★★☆☆☆ | ★★★★★ | 200–400 EUR |

**Hersteller:**
- RBS Battens (Australien) — Marktführer, Carbon und GFK
- Forespar (USA) — GFK-Standard
- Forte (Neuseeland) — Performance-Carbon
- Holt Allen (UK) — Budget-GFK

### 5.4 Latten-Profil und Steifigkeit

**Steifigkeitsverteilung entlang der Latte:**
- Am Mast (Vorliek-Ende): steifer → unterstützt Profil-Vorderkante
- In der Mitte: weicher → erlaubt Segelwölbung
- Am Achterliek: mittlere Steifigkeit → kontrolliert Austrittswinkel

**Biegekurve:**
Jede Latte hat eine definierte Biegekurve, die zur gewünschten Segelform passen muss:
- Zu steife Latte → flaches Profil im Lattenbereich, harter Knick an den Lattenenden
- Zu weiche Latte → zu viel Bauch, kein Profil am Achterliek
- Optimale Latte → glatter Übergang, gleichmäßige Kurve

**Latten-Dimensionen (typisch 40-Fuß-Großsegel):**

| Latte | Position | Länge | Breite | Dicke |
|-------|----------|-------|--------|-------|
| L1 (unten) | 25% Höhe | 1.200–1.500 mm | 35–45 mm | 5–8 mm |
| L2 | 42% Höhe | 1.600–2.000 mm | 30–40 mm | 4–7 mm |
| L3 | 58% Höhe | 1.800–2.300 mm | 28–38 mm | 4–6 mm |
| L4 (oben) | 78% Höhe | 1.500–1.900 mm | 25–35 mm | 3–5 mm |

### 5.5 Latten-Spannung und -Einstellung

**Spannung einstellen:**
Die meisten Lattentaschen haben einen Spannmechanismus (Kompressionsschrauben, Schnüre, Clips).

**Korrekte Spannung:**
- Latte soll das Segel im Lattenbereich unterstützen, aber keine eigene Form aufzwingen
- Zu viel Spannung → horizontale Wulst im Segel (Latten "drücken" durch)
- Zu wenig Spannung → Latte klappert in der Tasche, kein Profilhalt
- Richtwert: Latte soll bei schwebendem Segel (kein Wind) gerade so das Profil halten

**Kontrollmethode:**
1. Segel bei Windstille setzen
2. Spannung so einstellen, dass im Lattenbereich keine Dellen oder Wülste sichtbar sind
3. Im Wind: Achterliek soll zwischen den Latten gleichmäßig öffnen
4. Ungleichmäßiges Achterliek → Latten-Spannung einzeln nachregulieren

### 5.6 Latten-Beschläge am Mast

**Slides (Rutscher/Schlitten):**
- Standard: Kunststoff-Slides in Mast-Nut
- Problem bei Volllatten: hohe Kompressionslasten
- Reibung beim Reffen
- Hersteller: Rutgerson, Harken, Antal, Ronstan

**Cars (Wagen):**
- Auf Schiene am Mast geführt
- Deutlich reduzierte Reibung → leichteres Reffen
- Nötig bei Full-Batten-Segeln über 35 Fuß
- Hersteller: Antal, Batten-Cars.com, Frederiksen

**Ball-Bearing Cars:**
- Kugelgelagerte Wagen → minimale Reibung
- Standard bei Performance-Yachten >40 Fuß
- Preis: 40–120 EUR pro Car
- Hersteller: Harken (BattSlide), Antal, Ronstan

**Typischer Preis für Batten-Car-Umrüstung (40-Fuß-Segel, 4 Full Battens):**
- Antal Batten Cars: 400–700 EUR
- Harken BattSlide: 600–1.000 EUR
- Schiene + Installation: 200–500 EUR zusätzlich
- **Gesamt: 600–1.500 EUR**

---

## 6. Trimminstrumente Großsegel

### 6.1 Übersicht Trimmkontrollen

```
                    MASTTOPP
                      |  ← Achterstag (Backstay)
     Fall (Halyard) → |
                      |  ← Mastbiegung (Mast Bend)
                      |
                      |  ← Cunningham (Vorliekstrecker)
     Salingtrimm ←   |
                      |
                      |
    BAUM ═════════════╪═══════════════════
    |                 |                   |
    Vang ←            Traveller ←         → Outhaul
    (Baumniederholer) |                   (Schothornausholer)
                      |
                      → Großschot (Mainsheet)
```

### 6.2 Großschot (Mainsheet)

Die Großschot ist das primäre Trimminstrument. Sie kontrolliert gleichzeitig:

**Funktionen:**
1. **Anstellwinkel**: Dichter = enger zum Wind, Fieren = weiter ab
2. **Twist**: Dichter = weniger Twist (oberes Segel geschlossener), Fieren = mehr Twist
3. **Achterliek-Spannung**: Dichter = gespannter (Achterliek geschlossen), Fieren = lockerer

**Schot-Systeme:**

| System | Anwendung | Übersetzung | Schot-Durchmesser |
|--------|----------|-------------|-------------------|
| End-Boom | Kleine Boote (<30 Fuß) | 4:1 bis 6:1 | 8–10 mm |
| Mid-Boom | Fahrtenyachten 30–45 Fuß | 4:1 bis 6:1 | 10–12 mm |
| Traveller + Mid-Boom | Performance Cruiser | 4:1 bis 8:1 | 10–12 mm |
| Hydraulisch | Yacht >50 Fuß | Stufenlos | n/a |

**Trimm-Richtlinien:**

| Bedingung | Schot-Einstellung | Begründung |
|-----------|------------------|-----------|
| Leichtwind am Wind | Schot so dicht, dass Achterliek gerade geschlossen | Maximaler Auftrieb |
| Mittelwind am Wind | Moderat dicht, Achterliek leicht offen | Optimales Lift/Drag |
| Frischer Wind am Wind | Fieren für Twist → oberes Segel öffnet | Depowering, weniger Krängung |
| Halbwind | Fieren, Traveller Lee | Mehr Twist, Baum raus |
| Raumschots | Gefiert, Vang übernimmt Twist-Kontrolle | Maximaler Vortrieb |

### 6.3 Traveller

Der Traveller ist eine Schiene (typisch: auf dem Cockpit-Boden oder der Kajütdach-Hinterkante), auf der der Großschot-Angriffspunkt seitlich verschoben wird.

**Funktion:**
- Verändert den Anstellwinkel des Großsegels OHNE den Twist zu verändern
- Traveller Luv = Baum in Schiffsmitte bei gleicher Schot-Einstellung → mehr Power
- Traveller Lee = Baum weiter außen → weniger Power/Krängung → Depowering

**Trimm-Strategie:**
1. **Leichtwind**: Traveller auf Luv → Baum in Mittschiffs → Segel voll
2. **Mittelwind**: Traveller Mitte → Standardposition
3. **Frischer Wind**: Traveller nach Lee → Depower ohne Twist zu verändern
4. **Böen**: Traveller schnell nach Lee → sofortiges Depower
5. **Halbwind/Raumschots**: Traveller ganz Lee, Schot übernimmt

**Traveller-Systeme:**
- Harken: Standardwagen mit Kugellagern, ca. 300–800 EUR
- Lewmar: Integrierte Systeme, ca. 400–1.000 EUR
- Antal: Budget bis Performance, ca. 250–700 EUR
- Frederiksen: Performance-Wagen, ca. 500–1.200 EUR

### 6.4 Baumniederholer / Vang

Der Baumniederholer (Vang, Kicking Strap) zieht den Baum nach unten und kontrolliert den Twist auf Raumschotkursen, wo die Großschot den Baum nicht mehr nach unten ziehen kann.

**Funktion:**
- Kontrolliert Twist bei gefierten Segeln
- Verhindert, dass der Baum bei Raumschots nach oben wandert
- Spannt das Achterliek → geschlosseneres Profil
- Kann auch am Wind als Ergänzung zur Schot verwendet werden

**Systeme:**

| Typ | Anwendung | Kraft | Preis (40 Fuß) |
|-----|----------|-------|----------------|
| Seilzug (Tackle) | Kleine Boote <30 Fuß | 500–1.500 kg | 100–300 EUR |
| Solid Vang (Gasdruckfeder + Seilzug) | Standard 30–45 Fuß | 1.000–3.000 kg | 400–1.200 EUR |
| Hydraulisch | Yachten >45 Fuß | 2.000–10.000 kg | 2.000–6.000 EUR |

**Hersteller:**
- Selden: Rodkicker (Gasdruckfeder), Standard in Europa, 400–800 EUR
- Hall Spars: Hydraulische Systeme
- Navtec (jetzt Rig-Rite): Hydraulik
- Garhauer: Budget-Tackle-Systeme (USA)

**Trimm-Hinweise:**
- Auf Raumschotkursen: Vang dicht genug, dass das Achterliek kontrolliert bleibt
- Zu viel Vang → Baum drückt nach unten, Mast biegt nach vorn, Vorliek wird zu lose
- Zu wenig Vang → Oberes Segel öffnet zu weit, kein Profil oben
- ACHTUNG: Bei Böen auf Raumschots kann ein zu dicht gezogener Vang eine Patenthalse auslösen → gefährlich

### 6.5 Cunningham / Vorliekstrecker

Der Cunningham ist eine Leine, die am Vorliek des Großsegels (ca. 30–50 cm über dem Hals) angreift und das Vorliek nach unten spannt.

**Funktion:**
- Verlagert den Segelbauch nach vorn
- Strafft das Vorliek → Falten am Vorliek verschwinden
- Flacht das Segel ab (indirekter Effekt)
- Ermöglicht Depowering ohne Segel zu reffen

**Wann einsetzen:**
- Bei zunehmendem Wind (>14–16 kn am Wind)
- Wenn der Bauch zu weit achtern gewandert ist
- Bei älteren Segeln, die den Bauch verloren haben
- In Kombination mit Achterstag → maximales Depowering

**Trimm:**
- Leichtwind: Cunningham lose (kein Zug)
- Mittelwind: Leicht anziehen → Horizontalfalten am Vorliek verschwinden gerade eben
- Frischer Wind: Fest anziehen → Bauch deutlich nach vorn
- Schwerwetter: Maximum → so flach wie möglich

### 6.6 Outhaul / Schothornausholer

Der Outhaul (Unterliekstrecker) spannt das Unterliek des Großsegels entlang des Baums.

**Funktion:**
- Kontrolliert den Bauch im unteren Drittel des Segels
- Durchgesetzt: flacher Fuß → weniger Krängung
- Lose: bauchiger Fuß → mehr Power

**Trimm:**

| Bedingung | Outhaul | Effekt |
|-----------|---------|--------|
| Leichtwind (<8 kn) | 10–15 cm lose | Bauchiger Fuß für Power |
| Mittelwind (8–16 kn) | 5–8 cm lose | Moderater Bauch |
| Frischer Wind (16–25 kn) | Durchgesetzt | Flacher Fuß, weniger Krängung |
| Schwerwetter (>25 kn) | Maximum | So flach wie möglich |
| Raumschots | Lose | Maximaler Vortrieb |

**Systeme:**
- Seilzug durch den Baum: Standard bei den meisten Yachten
- Kugellager-Wagen am Baum: Bei Performance-Booten
- Clam-Cleat oder Winch am Baum: Für schnelle Verstellung
- Preis: Outhaul-System 100–400 EUR (nachrüstbar)

### 6.7 Achterstag (Backstay)

Das Achterstag beeinflusst den Segeltrimm über zwei Mechanismen:

**1. Mastbiegung:**
- Mehr Achterstag → Mast biegt sich nach vorn → Vorliek wird gestreckt → Segel wird flacher
- Hauptinstrument für Mastbiegung bei Masttop-Rigg
- Bei Fraktional-Rigg: Achterstag biegt obere Masthälfte

**2. Vorstag-Spannung:**
- Mehr Achterstag → Vorstag wird straffer → weniger Sag → Vorsegel wird flacher
- Weniger Achterstag → Vorstag durchhängt → Vorsegel wird bauchiger
- Besonders wichtig für hoch-am-Wind-Leistung

**Systeme:**
- Feststehendes Achterstag mit Spanner: Standard Fahrtenyacht
- Hydraulik-Achterstag: Performance Cruiser / Regatta
- Running Backstays: Bei Fraktional-Rigg → Unterstützung der Mittelmastsalinge
- Checkstays: Ähnlich Running Backstays, permanent montiert

**Trimm:**

| Bedingung | Achterstag | Effekt |
|-----------|-----------|--------|
| Leichtwind | Locker | Bauchiges Vorsegel, voller Mast |
| Mittelwind | Moderat | Kontrollierter Sag, gute Form |
| Frischer Wind | Fest | Flaches Vorsegel, flaches Groß |
| Schwerwetter | Maximum | Maximum flat |
| Raumschots | Locker | Nicht relevant für Amwind-Leistung |

### 6.8 Latten-Spannung

Wie in Abschnitt 5.5 beschrieben, beeinflusst die Latten-Spannung das Segelprofil lokal.

**Saisonale Anpassung:**
- Saisonstart: Latten kontrollieren, Spannung einstellen
- Mitte Saison: Nachkontrollieren (Material ermüdet)
- Saisonende: Latten entspannen (Segel lagern ohne Kompression)

### 6.9 Mast Rake und Prebend

**Mast Rake (Mastneigung):**
- Neigung des Mastes nach achtern (Standard: 0,5–2° bei Fahrtenyachten)
- Mehr Rake → CE wandert nach achtern → mehr Luvgierigkeit
- Weniger Rake → CE vorn → neutraler/Leegierig
- Einstellung über Vorstag-Länge und Wanten-Länge

**Prebend (Vorbiegen):**
- Der Mast wird ohne Segel bereits leicht nach vorn gebogen eingestellt
- Typisch: 30–80 mm bei 40-Fuß-Mast
- Zweck: Definierter Ausgangspunkt für Biegung unter Last
- Mehr Prebend → Segel wird unter Last schneller flach

**Einstellung:**
- Wanten dichter → Mast gerader (weniger Prebend)
- Babystag dichter → Mast biegt nach vorn (mehr Prebend)
- Unterwant-Spannung: kontrolliert seitliche Mastbiegung und Pumpen

---

## 7. Trimminstrumente Vorsegel

### 7.1 Übersicht

```
MASTTOPP
|     \
|      \  ← Vorstag (Forestay)
|       \
|        \  ← Fall (Halyard)
|         \
|          \
|    SEGEL  \
|     |      \
|     |       VORSTAG-HALS
|     |
|     → Holepunkt (Sheet Lead/Car)
|     → Barber Hauler
|     → Schot (Jib Sheet)
```

### 7.2 Holepunkt / Sheet Lead Position

Der Holepunkt (Sheet Lead, Car Position) ist der Punkt, an dem die Vorsegelschot umgelenkt wird und der das Verhältnis von Achterliek-Spannung zu Unterliek-Spannung bestimmt.

**Auswirkung der Holepunkt-Position:**

| Position | Effekt auf Achterliek | Effekt auf Twist | Effekt auf Unterliek |
|----------|---------------------|-------------------|---------------------|
| Weiter vorn | Gespannter | Weniger Twist | Lockerer (bauchiger Fuß) |
| Weiter achtern | Lockerer | Mehr Twist | Gespannter (flacher Fuß) |
| Weiter innen | Enger zum Boot | Weniger Twist | - |
| Weiter außen | Weiter vom Boot | Mehr Twist | - |

**Grundeinstellung finden:**
1. Vorsegelschot-Verlängerung denken: Verlängert man die Schot über den Holepunkt hinaus, soll sie das Vorliek in der Mitte treffen
2. Alternativ: Achterliek-Telltales beobachten — alle sollten gleichzeitig flattern, wenn die Schot leicht gefiert wird
3. Faustformel Voraus-Achteraus: Holepunkt so, dass der Winkel der Schot zum Unterliek 7–12° beträgt

**Holepunkt nach Windstärke:**

| Windstärke | Holepunkt | Begründung |
|------------|----------|-----------|
| Leichtwind (<8 kn) | Standard bis leicht vorn | Wenig Twist, geschlossenes Achterliek |
| Mittelwind (8–16 kn) | Standard | Optimale Balance |
| Frischer Wind (16–25 kn) | Leicht achtern | Mehr Twist → oberes Segel öffnet |
| Schwerwetter (>25 kn) | Achtern | Maximum Twist → Maximum Depower |

### 7.3 Barber Hauler

Ein Barber Hauler ist eine zusätzliche Leine, die den Holepunkt seitlich (nach innen oder außen) verschiebt.

**Anwendung:**
- **Inboard Barber Hauler**: Zieht den Holepunkt zur Bootsmitte → engerer Schotwinkel am Wind
- **Outboard Barber Hauler**: Zieht den Holepunkt nach außen → breiterer Schotwinkel auf Raumschots-Kursen

**Wann einsetzen:**
- Bei überlappender Genua auf Raumschots: Outboard Barber → Segel öffnet sich nach Lee
- Bei nicht-überlappender Fock auf Raumschots: Outboard Barber → Segel steht weiter vom Großsegel
- Bei enger Am-Wind-Einstellung: Inboard Barber → maximale Höhe am Wind

### 7.4 Car Track (Holepunkt-Schiene)

Die Schiene, auf der der Holepunkt-Wagen gleitet. Typisch auf dem Seitendeck montiert.

**Systeme:**

| System | Verstellung | Anwendung | Preis |
|--------|-----------|-----------|-------|
| Pin-Track | Manuell (Bolzen) | Budget-Fahrtenyacht | 100–300 EUR |
| Freilaufend mit Stopper | Unter Last | Standard-Fahrtenyacht | 300–600 EUR |
| Leinenführung (Spin-Lock) | Vom Cockpit | Performance Cruiser | 500–1.000 EUR |
| Hydraulisch | Stufenlos | Regatta / Superyacht | 2.000–5.000 EUR |

**Hersteller:**
- Harken: Marktführer, Aluminium- und Composite-Tracks
- Lewmar: Integrierte Systeme
- Antal: Preis-Leistung
- Ronstan: Performance-Tracks

### 7.5 Fall (Halyard) — Vorsegel

Die Fallspannung beeinflusst die Vorliekspannung und damit die Segelform:

**Mehr Fall-Spannung:**
- Vorliek wird gestreckt → Bauch wandert nach vorn
- Ähnlicher Effekt wie Cunningham beim Großsegel
- Bei zunehmendem Wind: mehr Fall-Spannung

**Weniger Fall-Spannung:**
- Vorliek hat mehr Material → Bauch wandert nach achtern
- Horizontale Falten am Vorliek erscheinen
- Segel wird im Eintritt bauchiger → toleranter

**Hinweis:** Bei Rollvorsegeln wird die Fall-Spannung einmal eingestellt und bleibt dann fixiert. Trimm nur über Schot und Holepunkt.

### 7.6 Vorstag-Durchhang (Forestay Sag)

Der Durchhang des Vorstags hat enormen Einfluss auf die Vorsegel-Form:

**Physik:**
- Windlast auf das Vorsegel zieht das Vorstag nach Lee
- Typischer Durchhang: 30–150 mm bei 14 m Vorstag
- Durchhang vergrößert den Eintrittswinkel und den Bauch des Segels

**Kontrolle:**
- **Achterstag spannen**: Reduziert Durchhang (Hauptinstrument)
- **Babystag / Innerforestay**: Unterstützt das Vorstag → weniger Sag
- **Running Backstays**: Bei Fraktional-Rigg zur Sag-Kontrolle
- **Wantspanner**: Grundspannung des Riggs → Baseline-Sag

**Richtwerte Forestay Sag:**

| Windstärke | Akzeptabler Sag (14 m Vorstag) | Achterstag |
|------------|-------------------------------|-----------|
| 0–8 kn | 80–120 mm | Locker → etwas Sag = bauchiger Eintritt |
| 8–14 kn | 50–80 mm | Moderat |
| 14–20 kn | 30–50 mm | Fest |
| 20+ kn | 20–30 mm | Maximum |

### 7.7 Telltales am Vorsegel

Siehe ausführlich Abschnitt 9. Kurzzusammenfassung:

- **Luv-Telltale steigt/flattert**: Zu hoch am Wind oder Segel zu dicht geholt → abfallen oder Schot fieren
- **Lee-Telltale steigt/flattert**: Zu tief am Wind oder Segel zu offen → anluven oder Schot dichter
- **Beide horizontal**: Optimale Anströmung → "in the groove"

### 7.8 Selbstwendefock (Self-Tacking Jib)

Selbstwendefocken laufen auf einer Querschiene (Athwartships Track) und wechseln bei der Wende automatisch die Seite.

**Trimm-Besonderheiten:**
- Kein Überlapp → kein Slot-Effekt
- Breiter Eintrittswinkel → tolerant aber weniger Höhe
- Holepunkt nur Voraus-Achteraus verstellbar (keine Seiten-Verstellung)
- Typisch 95–108% LP (Perpendicular)

**Systeme:**
- Harken Self-Tacking System: 800–1.500 EUR
- Facnor: Integrierte Rollreff-Selbstwendefock
- Bartels: Budget-Variante

### 7.9 Code 0 / Screecher

Der Code 0 ist ein flaches Reaching-Segel, das am Vorstag oder einem eigenen Bugspriet-Fall gefahren wird.

**Trimm-Besonderheiten:**
- Gefahren bei TWA 50–90° in Leichtwind (4–14 kn)
- Holepunkt weit achtern und außen
- Schot-Spannung moderat → Achterliek soll leicht flattern
- Twist: Moderat — oberes Drittel soll öffnen
- Häufig auf Furler (Facnor, Karver) → Reffen durch Einrollen

**Trimm-Fehler Code 0:**
- Zu dicht geholt → Strömungsabriss, Segel backt an Vorstag
- Zu offen → Kein Profil, nur Flattern
- Falscher TWA → Code 0 bei >16 kn TWS → Überlastung

---

## 8. Trimm nach Wind und Kurs

### 8.1 Systematik

Die folgende Matrix gibt detaillierte Trimm-Einstellungen für verschiedene Kombinationen aus Windstärke und Kurs. Alle Angaben für eine typische 35–42-Fuß-Segelyacht mit Standardrigg (Fraktional oder Masttop).

**Windstärke-Kategorien:**
- **Leichtwind**: 0–8 kn TWS (True Wind Speed)
- **Mittelwind**: 8–16 kn TWS
- **Frischer Wind**: 16–25 kn TWS
- **Starkwind**: 25+ kn TWS

**Kurs-Kategorien:**
- **Hoch am Wind (Close-Hauled)**: TWA 30–50°
- **Halbwind (Beam Reach)**: TWA 70–100°
- **Raumschots (Broad Reach)**: TWA 110–150°
- **Vor dem Wind (Run)**: TWA 150–180°

### 8.2 Leichtwind — Hoch am Wind (0–8 kn, TWA 35–50°)

**Ziel**: Maximaler Auftrieb bei minimaler Strömungsgeschwindigkeit. Profil muss stehen, obwohl wenig Winddruck vorhanden.

| Parameter | Einstellung | Begründung |
|-----------|-----------|-----------|
| **Großschot** | Moderat dicht, nicht blockiert | Achterliek gerade geschlossen |
| **Traveller** | Luv von Mitte | Baum fast mittschiffs |
| **Vang** | Lose | Nicht relevant am Wind |
| **Cunningham** | Lose | Bauchiger Eintritt gewünscht |
| **Outhaul** | 10–15 cm lose | Bauchiger Fuß |
| **Achterstag** | Locker | Vorstag-Sag erlaubt → bauchiges Vorsegel |
| **Vorsegel-Schot** | Moderat, nicht übertrimmt | Achterliek geschlossen aber nicht gehooked |
| **Holepunkt** | Standard bis leicht vorn | Wenig Twist, volle Power |
| **Mastbiegung** | Minimal | Segel soll voll stehen |
| **Crew** | Lee-Seite, tief | Boot flach oder leicht Lee-Krängung (1–3°) |

**Spezialhinweise Leichtwind:**
- Boot möglichst wenig bewegen (Crew sitzt still)
- Kein übermäßiges Steuern (Ruder als Bremse)
- Segel sollen natürlich stehen — nicht mit Kraft in Form zwingen
- Leichte Lee-Krängung (2–3°) hilft den Segeln, durch Schwerkraft in Form zu fallen

### 8.3 Leichtwind — Halbwind/Raumschots (0–8 kn, TWA 70–150°)

| Parameter | Einstellung | Begründung |
|-----------|-----------|-----------|
| **Großschot** | Gefiert, Baum 70–90° zum Boot | Maximale Fläche zum Wind |
| **Traveller** | Ganz Lee | Baum frei |
| **Vang** | Leicht gesetzt | Achterliek leicht kontrollieren |
| **Cunningham** | Lose | Nicht relevant |
| **Outhaul** | 15–20 cm lose | Maximaler Bauch |
| **Vorsegel-Schot** | Weit gefiert, Barber Hauler aus | Segel bauchig und offen |
| **Holepunkt** | Weit achtern und außen | Maximale Power |
| **Alternativ** | Gennaker / Code 0 setzen | Bei TWA >60° und <12 kn |

### 8.4 Mittelwind — Hoch am Wind (8–16 kn, TWA 30–45°)

**Ziel**: Optimaler Kompromiss zwischen Vortrieb und Seitenkraft. Idealzustand für die meisten Segelyachten.

| Parameter | Einstellung | Begründung |
|-----------|-----------|-----------|
| **Großschot** | Dicht, Achterliek-Telltale 80% strömend | Standard-Amwind-Trimm |
| **Traveller** | Leicht Lee von Mitte | Kontrolle ohne Übertrimm |
| **Vang** | Moderat | Unterstützt Schot am Wind |
| **Cunningham** | Leicht (Falten gerade verschwunden) | Bauch bei ca. 40% |
| **Outhaul** | 5–8 cm lose | Moderater Fuß-Bauch |
| **Achterstag** | Moderat bis fest | Vorstag kontrolliert, mittlerer Sag |
| **Vorsegel-Schot** | Dicht, Telltales parallel | Optimale Anströmung |
| **Holepunkt** | Standard | Gleichmäßiger Twist oben-unten |
| **Mastbiegung** | Moderat | Segel moderat flach |
| **Krängung** | 15–20° (Fahrt), 20–25° (Regatta) | Ziel-Krängung für max VMG |

**Dies ist der "Sweet Spot" — hier sollte das Segel am besten aussehen und sich am effizientesten anfühlen.**

### 8.5 Mittelwind — Halbwind (8–16 kn, TWA 70–100°)

| Parameter | Einstellung | Begründung |
|-----------|-----------|-----------|
| **Großschot** | Halbe Fahrt, Baum ~60° | Profil zum Reaching |
| **Traveller** | Ganz Lee | Baum frei |
| **Vang** | Moderat bis fest | Kontrolliert Twist |
| **Cunningham** | Lose | Nicht primär relevant |
| **Outhaul** | Leicht lose | Etwas Bauch erlaubt |
| **Vorsegel-Schot** | Gefiert, Segel steht breit | Reaching-Profil |
| **Holepunkt** | Achtern und außen | Reaching-Setup |

### 8.6 Mittelwind — Raumschots/Vor dem Wind (8–16 kn, TWA 110–180°)

| Parameter | Einstellung | Begründung |
|-----------|-----------|-----------|
| **Großschot** | Ganz gefiert | Baum fast 90° |
| **Traveller** | Ganz Lee | — |
| **Vang** | Fest | Hauptinstrument Twist-Kontrolle |
| **Cunningham** | Lose | — |
| **Outhaul** | Lose | Maximaler Bauch |
| **Vorsegel** | Ausgebaumt (Whisker Pole) oder Schmetterling | Maximale Fläche |
| **Alternativ** | Spinnaker / Gennaker | Bei TWA >110° |

### 8.7 Frischer Wind — Hoch am Wind (16–25 kn, TWA 30–45°)

**Ziel**: Depowering — Krängung und Ruderdruck reduzieren, VMG maximieren.

| Parameter | Einstellung | Begründung |
|-----------|-----------|-----------|
| **Großschot** | Fieren für Twist | Oberes Segel öffnet |
| **Traveller** | Deutlich Lee | Reduziert Krängungsmoment |
| **Vang** | Fest | Unterstützt Achterliek-Kontrolle |
| **Cunningham** | Fest anziehen | Bauch nach vorn, flacheres Exit-Profil |
| **Outhaul** | Durchgesetzt | Flacher Fuß |
| **Achterstag** | Fest | Mast biegt → Segel flach, Vorstag straff |
| **Vorsegel-Schot** | Leicht fieren | Twist erhöhen → oberes Segel öffnet |
| **Holepunkt** | 5–10 cm achtern | Mehr Twist |
| **Mastbiegung** | Ausgeprägt | Maximales Depowering über Mastbiegung |
| **1. Reff** | Bei 18–22 kn (je nach Boot) | Wenn Krängung >25–30° |
| **Vorsegel wechseln** | Genua → Fock, oder Roll-Genua reffen | Bei Überpower |

**Depower-Reihenfolge (empfohlen):**
1. Traveller Lee
2. Cunningham + Outhaul durchsetzen
3. Achterstag fest
4. Schot fieren (Twist)
5. 1. Reff (Großsegel)
6. Vorsegel reffen / wechseln
7. 2. Reff

### 8.8 Frischer Wind — Halbwind (16–25 kn, TWA 70–100°)

| Parameter | Einstellung | Begründung |
|-----------|-----------|-----------|
| **Großschot** | Gefiert, kontrolliert | Baum ca. 45–60° |
| **Vang** | Fest | Twist-Kontrolle dominant |
| **Cunningham** | Moderat | Profil-Kontrolle |
| **Outhaul** | Leicht durchgesetzt | Kompromiss Power/Kontrolle |
| **Vorsegel-Schot** | Moderat gefiert | Reaching-Profil |
| **Achtung** | Broaching-Gefahr! | Ruder aufmerksam führen |

### 8.9 Frischer Wind — Raumschots/Vor dem Wind (16–25 kn, TWA 110–180°)

| Parameter | Einstellung | Begründung |
|-----------|-----------|-----------|
| **Großschot** | Gefiert | Baum weit aus |
| **Vang** | Fest bis sehr fest | Verhindert Patenthalse |
| **Vorsegelschot** | Ausgebaumt oder Schmetterling | Stabilisierung |
| **ACHTUNG** | Patenthalse-Gefahr! | Preventer / Bullenstander IMMER fahren |
| **Bei Spinnaker** | Erfahrene Crew erforderlich | Broaching/Chinesische Halse vermeiden |

### 8.10 Starkwind — Hoch am Wind (25+ kn, TWA 30–45°)

**Ziel**: Sicherheit, kontrollierte Fahrt, VMG sekundär zu Boots-Kontrolle.

| Parameter | Einstellung | Begründung |
|-----------|-----------|-----------|
| **Großsegel** | 2. oder 3. Reff | Segelfläche drastisch reduziert |
| **Cunningham** | Maximum | Segel so flach wie möglich |
| **Outhaul** | Maximum | — |
| **Achterstag** | Maximum | — |
| **Traveller** | Ganz Lee | — |
| **Vorsegel** | Kleine Fock oder stark gereffte Rollgenua | Segelbalance halten |
| **Schot** | Moderat — nicht übertrimmen! | Boot muss steuerbar bleiben |
| **Alternativ** | Sturmbesegelung (Trysegel + Sturmfock) | Ab 35+ kn |

### 8.11 Starkwind — Raumschots/Vorwind (25+ kn, TWA 110–180°)

**ACHTUNG: Gefährlichste Segelkonfiguration!**

| Parameter | Einstellung | Begründung |
|-----------|-----------|-----------|
| **Großsegel** | Tief gerefft oder geborgen | Kontrollierbarkeit |
| **Vorsegel** | Kleine Fock, eventuell ausgebaumt | Stabilisierung |
| **Preventer** | IMMER fahren | Patenthalse kann Mast/Crew gefährden |
| **Alternative** | Nur unter Sturmfock laufen | Ab 30+ kn |
| **Alternative** | Beidrehen / Lenzen unter Starkwind | Survival-Taktik |

**Confidence: documented** — Marchaj "Seaworthiness", Rousmaniere "Fastnet Force 10", ORC Special Regulations

---

## 9. Telltales und Strömungsindikatoren

### 9.1 Arten von Telltales

| Typ | Material | Platzierung | Zweck |
|-----|---------|-------------|-------|
| Vorliek-Telltales (Luv/Lee) | Wolle, Nylon-Band | Vorsegel-Vorliek, 3–4 Paare | Anströmsituation |
| Achterliek-Telltales | Wolle, Leichtband | Großsegel-Achterliek, 2–3 Stück | Austrittsströmung |
| Shroud-Telltales | Wolle, Cassetten-Band | Oberwant, mittlere Höhe | Scheinbarer Wind-Richtung |
| Masttopp-Verklicker | Windfahne, Pfeil | Masttopp | Wahrer/scheinbarer Wind |
| Streamer | Mylar-Streifen | Am Vorsegel, Full-Length | Strömungsvisualisierung |
| Bauch-Telltales | Wolle | Auf dem Segel, am Bauchpunkt | Profil-Tiefenindikator |

### 9.2 Platzierung am Vorsegel

**Standard-Anordnung:**

```
    KOPF
    /|
   / |
  /  |
 / ● ← Paar 3 (oberes Drittel, ca. 75% Höhe)
/   |
/ ● ← Paar 2 (Mitte, ca. 50% Höhe)
/   |
/ ● ← Paar 1 (unteres Drittel, ca. 25% Höhe)
/   |
HALS-CLEW
```

**Abstand vom Vorliek:**
- 15–30 cm hinter dem Vorliek
- Luv- und Lee-Telltale auf gleicher Höhe, jeweils auf ihrer Seite
- Materiallänge: 20–30 cm

**Farbcode (Empfehlung):**
- Luv (Windseite): Rot oder Grün
- Lee (Windabgewandt): Grün oder Schwarz
- Verschiedene Farben → einfachere Unterscheidung

### 9.3 Telltales am Vorsegel lesen

| Luv-Telltale | Lee-Telltale | Diagnose | Aktion |
|-------------|-------------|----------|--------|
| Strömt horizontal | Strömt horizontal | Perfekte Anströmung | Kurs/Trimm beibehalten |
| Steigt/flattert | Strömt horizontal | Anströmwinkel zu gering (zu hoch am Wind) | Abfallen oder Schot fieren |
| Strömt horizontal | Steigt/flattert | Anströmwinkel zu groß (zu tief am Wind) | Anluven oder Schot dichter |
| Beide flattern | Beide flattern | Stall / Strömungsabriss | Schot fieren, abfallen |
| Strömt nach oben | Strömt nach oben | Holepunkt zu weit achtern | Holepunkt nach vorn |
| Unten gut, oben Lee flattert | — | Holepunkt zu weit vorn | Holepunkt nach achtern |

**Twist-Kontrolle über Telltales:**
- **Obere und untere Telltales reagieren gleichzeitig**: Twist ist korrekt
- **Obere flattern zuerst (Lee)**: Zu viel Twist → Holepunkt vorn
- **Untere flattern zuerst (Lee)**: Zu wenig Twist → Holepunkt achtern

### 9.4 Achterliek-Telltales (Großsegel)

**Platzierung:**
- 2–3 Telltales an den Latten-Enden (Achterliek)
- Aus dem Leech Tabling herausragend
- Material: leichte Wolle oder Nylon-Bänder (15–25 cm)

**Lesen:**

| Telltale-Verhalten | Diagnose | Aktion |
|--------------------|----------|--------|
| Strömt achteraus (80–100% der Zeit) | Achterliek optimal offen | Beibehalten |
| Steht still / hinter Achterliek verschwunden | Achterliek zu geschlossen (Hook) | Schot fieren, Traveller Lee |
| Flattert stark | Achterliek zu offen | Schot dichter, Vang dichter |
| Oberes Telltale steht, unteres strömt | Zu wenig Twist | Schot fieren oder Traveller Lee |
| Unteres steht, oberes strömt | Zu viel Twist | Schot dichter |

### 9.5 Shroud-Telltales und Verklicker

**Shroud-Telltales:**
- Auf dem Oberwant montiert (auf halber Höhe der Saling)
- Zeigen die Richtung des scheinbaren Windes
- Material: Kassetten-Band, Wolle, oder leichte Plastik-Streifen
- Zweck: Schnelle Referenz für Windrichtung bei Manövern

**Masttopp-Verklicker:**
- Windfahne am Masttopp (Windex o.ä.)
- Zeigt den scheinbaren Wind in der Höhe an
- Berücksichtigt den Windgradienten
- Hersteller: Davis Instruments (Windex), Ronstan

### 9.6 Elektronische Strömungsindikatoren

Moderne Instrumente ergänzen visuelle Telltales:

- **Windmesser (Anemometer + Windfahne)**: B&G, Garmin, Raymarine
- **Heel-Sensor**: Misst Krängung als Indikator für Trimm
- **Polar-Target**: Vergleicht aktuelle Geschwindigkeit mit theoretischem Optimum (VPP)
- **Apps**: SailTrim (B&G), Expedition, TimeZero

---

## 10. Fehlerbild-Atlas

### 10.1 F-16_07-01: Zu bauchiges Segelprofil

**Beschreibung:**
Das Segel zeigt übermäßige Tiefe (Bauchtiefe >15% am Wind). Der Bauch ist oft zu weit achtern (>50% Profiltiefe). Das Boot krängt stark, macht wenig Höhe und hat übermäßigen Ruderdruck.

**Visuelle Erkennungsmerkmale:**
- Stark gerundetes Profil bei Seitenansicht
- Achterliek gehooked (nach Luv zeigend)
- Übermäßige Krängung trotz moderatem Wind
- Leehelm (Ruder muss nach Lee gehalten werden)

**Ursachen:**
1. Schot zu dicht geholt ohne Traveller-Ausgleich
2. Vorstag durchhängt zu stark (bei Vorsegel)
3. Segel gealtert — Tuch gedehnt, Bauch permanent zu tief
4. Outhaul nicht durchgesetzt (Großsegel-Fuß)
5. Cunningham nicht gesetzt (Bauch zu weit achtern)
6. Zu wenig Mastbiegung (Achterstag zu locker)
7. Falsches Segel für den Wind (zu schweres Tuch bei Leichtwind)

**Korrekturmaßnahmen:**
1. Cunningham setzen → Bauch nach vorn
2. Outhaul durchsetzen → Fuß flacher
3. Achterstag spannen → Mast biegen → Vorliek strecken
4. Traveller Lee → Gesamtanstellwinkel reduzieren
5. Schot leicht fieren → Twist erhöhen
6. Segel beim Segelmacher überprüfen lassen (Nachmessen)

**AYDI-Fehlerkennzeichnung:** `F-16_07-01`
**Schweregrad:** Mittel (Leistungsverlust) bis Hoch (Kontrollverlust bei Starkwind)
**Confidence bei visueller Erkennung:** `visual_high` (charakteristisches Profil)

### 10.2 F-16_07-02: Zu flaches Segelprofil

**Beschreibung:**
Das Segel zeigt zu geringe Bauchtiefe (<8% auch bei Leichtwind). Das Boot beschleunigt schlecht, hat wenig Power und fühlt sich "leblos" an.

**Visuelle Erkennungsmerkmale:**
- Flaches, brett-ähnliches Profil
- Achterliek offen (nach Lee fallend)
- Boot macht gute Höhe, aber wenig Speed
- Telltales am Vorliek flattern häufig (empfindlich)

**Ursachen:**
1. Achterstag zu fest → Mast zu stark gebogen
2. Cunningham zu fest angezogen
3. Outhaul zu weit durchgesetzt
4. Segel für stärkeren Wind geschnitten (Regattasegel bei Leichtwind)
5. Vorstag zu straff (Vorsegel) → kein Entry-Angle

**Korrekturmaßnahmen:**
1. Achterstag lockern → Mast gerader → Segel bauchiger
2. Cunningham lösen
3. Outhaul 10–15 cm lose
4. Traveller auf Luv → mehr Anstellwinkel
5. Segel wechseln (Leichtwind-Segel)

**AYDI-Fehlerkennzeichnung:** `F-16_07-02`
**Schweregrad:** Niedrig bis Mittel (Leistungsverlust)
**Confidence bei visueller Erkennung:** `visual_high`

### 10.3 F-16_07-03: Falscher Bauchpunkt (Draft Position Error)

**Beschreibung:**
Der tiefste Punkt des Segelprofils befindet sich nicht an der für die Bedingungen optimalen Position. Typisch: Bauch zu weit achtern bei frischem Wind, oder zu weit vorn bei Leichtwind.

**Visuelle Erkennungsmerkmale:**
- Profil erscheint asymmetrisch bei Betrachtung von unten
- Streifen-Analyse zeigt Bauch bei >50% (zu achtern) oder <30% (zu vorn)
- Vorliek-Falten (bei Bauch zu weit achtern)
- Rundliches, undefiniertes Vorliek (bei Bauch zu weit vorn)

**Ursachen (Bauch zu weit achtern):**
1. Cunningham nicht gesetzt
2. Segel gealtert (Tuch hat sich permanent gedehnt)
3. Fall-Spannung zu gering
4. Achterstag zu locker

**Ursachen (Bauch zu weit vorn):**
1. Cunningham zu stark gesetzt
2. Fall-Spannung zu hoch
3. Mast zu stark gebogen

**Korrekturmaßnahmen:**
- Cunningham: Anziehen verschiebt Bauch nach vorn, Lösen nach achtern
- Achterstag: Spannen verschiebt Bauch nach vorn (über Mastbiegung)
- Fall: Mehr Spannung → Bauch nach vorn
- Bei permanent falschem Bauchpunkt: Segel beim Segelmacher überarbeiten lassen

**AYDI-Fehlerkennzeichnung:** `F-16_07-03`
**Schweregrad:** Mittel
**Confidence bei visueller Erkennung:** `visual_medium` (erfordert Streifen-Analyse für genaue Beurteilung)

### 10.4 F-16_07-04: Zu viel Twist

**Beschreibung:**
Das obere Segel öffnet sich übermäßig. Das Großsegel-Kopf steht fast parallel zum Wind. Das Vorsegel zeigt deutlich unterschiedliche Anströmung zwischen unten und oben.

**Visuelle Erkennungsmerkmale:**
- Oberes Drittel des Segels flattert oder steht weit offen
- Großsegel-Achterliek fällt nach Lee ab (von oben betrachtet: S-Kurve)
- Untere Telltales strömen, obere flattern stark
- Leech-Telltales im oberen Bereich flattern permanent

**Ursachen:**
1. Großschot nicht genug durchgesetzt
2. Vang/Baumniederholer zu locker (auf Raumschots)
3. Holepunkt zu weit achtern (Vorsegel)
4. Latten-Spannung oben zu gering
5. Obere Latte zu weich

**Korrekturmaßnahmen:**
1. Großschot dichter holen
2. Vang setzen (besonders auf Raumschots)
3. Holepunkt nach vorn (Vorsegel)
4. Obere Latten-Spannung erhöhen
5. Steifere obere Latte einsetzen

**AYDI-Fehlerkennzeichnung:** `F-16_07-04`
**Schweregrad:** Mittel
**Confidence bei visueller Erkennung:** `visual_high`

### 10.5 F-16_07-05: Achterliek-Hook

**Beschreibung:**
Das Achterliek zeigt im oberen Bereich einen deutlichen Knick nach Luv (Hook). Das Segel bremst aktiv, da die Strömung am Achterliek blockiert wird.

**Visuelle Erkennungsmerkmale:**
- Achterliek biegt nach Luv (von achtern betrachtet: nach innen)
- Achterliek-Telltales stehen still oder verschwinden hinter dem Segel
- Übermäßige Krängung bei wenig Vortrieb
- Deutlicher Luvhelm

**Ursachen:**
1. Großschot zu dicht in Kombination mit Traveller zu hoch
2. Vang zu fest (drückt Achterliek nach Luv)
3. Latten-Spannung zu hoch (obere Latten)
4. Zu viel Roach ohne ausreichende Latten-Steifigkeit
5. Achterstag zu locker → Mast zu gerade → Achterliek-Überschuss

**Korrekturmaßnahmen:**
1. Großschot leicht fieren → Twist erhöhen
2. Traveller nach Lee → Grundanstellwinkel reduzieren
3. Vang lockern (am Wind)
4. Obere Latten-Spannung reduzieren
5. Achterstag spannen → Mast biegen → Achterliek öffnet sich

**AYDI-Fehlerkennzeichnung:** `F-16_07-05`
**Schweregrad:** Hoch (erheblicher Leistungsverlust und Kontrollprobleme)
**Confidence bei visueller Erkennung:** `visual_high` (sehr charakteristisch)

### 10.6 F-16_07-06: Vorliek-Flutter (Luff Flutter)

**Beschreibung:**
Das Vorliek des Segels flattert unrhythmisch — auch bei ausreichend Wind und scheinbar korrektem Trimm. Das Flattern verursacht Lärm, Verschleiß und reduziert die Aerodynamik.

**Visuelle Erkennungsmerkmale:**
- Sichtbares Flattern/Schlagen am Vorliek
- Horizontale Falten vom Vorliek ausgehend
- Bei Vorsegel: Vorliek löst sich periodisch vom Vorstag
- Lärm (typisches "Flattern")

**Ursachen:**
1. Fall-Spannung zu gering → Vorliek nicht gespannt
2. Vorliekkurve passt nicht zur Mastbiegung (Großsegel)
3. Vorstag zu locker / zu viel Sag (Vorsegel)
4. Segel für anderes Rigg geschnitten (falsches Segel am falschen Mast)
5. Vorliek-Tabling hat sich gelöst
6. Segel ist zu alt — Material permanent gedehnt

**Korrekturmaßnahmen:**
1. Fall durchsetzen
2. Cunningham setzen
3. Achterstag spannen → Vorstag straffer (Vorsegel)
4. Mastbiegung an Vorliekkurve anpassen (Rigger konsultieren)
5. Segelmacher: Vorliekkurve überprüfen/korrigieren

**AYDI-Fehlerkennzeichnung:** `F-16_07-06`
**Schweregrad:** Mittel (Verschleiß) bis Niedrig (Ästhetik)
**Confidence bei visueller Erkennung:** `visual_high`

### 10.7 F-16_07-07: Alterungsverformung (Age Distortion)

**Beschreibung:**
Das Segel zeigt permanente Formveränderungen durch Alterung des Materials. Typisch: Bauch ist permanent zu weit achtern, Segel ist insgesamt zu bauchig, Achterliek hat permanent zu wenig Spannung.

**Visuelle Erkennungsmerkmale:**
- Segel wirkt "ausgeleiert" auch bei optimalem Trimm
- Horizontal-Falten vom Vorliek (Tuch hat sich gestreckt)
- Bauch permanent bei >50% Profiltiefe
- Kein Trimm kann das Segel flach bekommen
- Unterschiedliche Bereiche altern unterschiedlich schnell (UV-exponierte Stellen)

**Typische Lebensdauern:**

| Material | Fahrteneinsatz | Regattaeinsatz |
|----------|---------------|---------------|
| Dacron Cross-Cut | 6–12 Jahre | 3–5 Jahre |
| Dacron Tri-Radial | 5–10 Jahre | 2–4 Jahre |
| Laminat (Mylar) | 4–7 Jahre | 2–3 Jahre |
| 3Di NORDAC | 7–12 Jahre | 3–5 Jahre |
| 3Di Carbon | 5–8 Jahre | 2–4 Jahre |
| Doyle Stratis | 5–9 Jahre | 3–5 Jahre |

**Korrekturmaßnahmen:**
1. Segelmacher kann begrenzt "Reprofilieren" (Nähte umsetzen): 300–800 EUR
2. UV-Schutzbänder nachrüsten (verlängert Restlebensdauer)
3. Segel als Reservesegel/Sturmsegel degradieren
4. Neues Segel bestellen

**AYDI-Fehlerkennzeichnung:** `F-16_07-07`
**Schweregrad:** Niedrig (frühes Stadium) bis Hoch (Segel nicht mehr trimm-bar)
**Confidence bei visueller Erkennung:** `visual_medium`

### 10.8 F-16_07-08: Unbalancierter Segelplan

**Beschreibung:**
Der Segelplan ist nicht ausbalanciert — zu viel oder zu wenig Segelfläche vorn (Vorsegel) relativ zum Großsegel. Das Boot zeigt starke Luvgierigkeit oder Leegierigkeit.

**Visuelle Erkennungsmerkmale:**
- Starker Luvhelm → Boot will permanent anluven (zu viel Groß / zu wenig Vorsegel)
- Starker Leehelm → Boot will permanent abfallen (zu viel Vorsegel / zu wenig Groß)
- Ruderlage permanent >5° → erheblicher Widerstand
- Unterschiedliche Krängung Groß vs. Vorsegel

**Ursachen:**
1. Falsches Segel-Verhältnis (z.B. große Genua + volles Groß bei viel Wind)
2. Segel mit unterschiedlichem Alter/Zustand
3. Rigg-Einstellung (Mast Rake) falsch
4. CE-CLR-Verhältnis nicht korrekt

**Korrekturmaßnahmen:**
1. Bei Luvgierigkeit: Großsegel reffen oder Fieren / größeres Vorsegel setzen
2. Bei Leegierigkeit: Vorsegel reffen / kleiner wählen / Großsegel dichter
3. Mast Rake anpassen (Langzeit-Lösung)
4. Segelplan vom Segelmacher/Rigger überprüfen lassen

**AYDI-Fehlerkennzeichnung:** `F-16_07-08`
**Schweregrad:** Hoch (Steuerbarkeit, Sicherheit)
**Confidence bei visueller Erkennung:** `visual_medium`

### 10.9 F-16_07-09: Leichtwind-Performance-Mangel

**Beschreibung:**
Das Boot zeigt bei Leichtwind (<8 kn) deutlich schlechtere Performance als erwartet. Segel stehen nicht, füllen sich nicht, das Boot kommt nicht in Fahrt.

**Visuelle Erkennungsmerkmale:**
- Segel hängen schlaff, kein Profil erkennbar
- Boot liegt quasi still trotz messbarem Wind
- Telltales hängen herunter (keine Strömung)
- Segel zu schwer für den Wind (Dacron-Schwergut bei Leichtwind)

**Ursachen:**
1. Segel-Material zu schwer (schweres Dacron für Leichtwind)
2. Segel-Profil zu flach geschnitten (Regattasegel für frischen Wind)
3. Crew-Gewicht zu weit auf Luv → Boot zu flach → Segel fallen nicht in Form
4. Rigg zu straff → Segel können nicht bauchig werden
5. Kein Leichtwind-Segel im Segelschrank (Code 0, Gennaker)
6. Rumpfbewuchs → Strömungswiderstand zu hoch

**Korrekturmaßnahmen:**
1. Leichtwind-Segelsatz erwägen (leichtes Tuch)
2. Code 0 oder Gennaker → ab TWA >50° enorme Verbesserung
3. Crew-Position: Lee und tief, Boot leicht krängen
4. Achterstag lösen, Cunningham lösen, Outhaul lösen
5. Segel für Leichtwind trimmen (siehe 8.2)

**AYDI-Fehlerkennzeichnung:** `F-16_07-09`
**Schweregrad:** Niedrig (Komfort) bis Mittel (Regatta-Performance)
**Confidence bei visueller Erkennung:** `visual_medium`

### 10.10 F-16_07-10: Übermäßiger Heel (Excessive Heel)

**Beschreibung:**
Das Boot krängt permanent über 25–30° trotz moderatem Wind (12–18 kn). Der Trimm ist nicht angepasst, oder der Segelplan ist für die Bedingungen zu groß.

**Visuelle Erkennungsmerkmale:**
- Boot liegt stark über, Lee-Reling im Wasser
- Crew auf Luvseite kann Boot nicht aufrecht halten
- Ruderlage stark nach Luv (Luvhelm)
- Boot fährt seitlich (hoher Abdrift)

**Ursachen:**
1. Keine Reff-Reaktion bei zunehmendem Wind
2. Traveller nicht nach Lee → Segel überpower
3. Cunningham und Outhaul nicht gesetzt → Segel zu bauchig
4. Achterstag nicht gespannt
5. Segelplan generell zu groß für das Boot (Design-Thema)

**Korrekturmaßnahmen:**
1. Depower-Sequenz durchlaufen (siehe 8.7)
2. Reffen (Großsegel und/oder Vorsegel)
3. Crew auf Luv
4. Bei chronischem Problem: Segelplan-Änderung erwägen (Rigger/Designer)

**AYDI-Fehlerkennzeichnung:** `F-16_07-10`
**Schweregrad:** Hoch (Sicherheit, Stabilität)
**Confidence bei visueller Erkennung:** `visual_high`

### 10.11 F-16_07-11: Flogging-Schäden

**Beschreibung:**
Durch unkontrolliertes Schlagen (Flogging) des Segels sind Materialschäden entstanden. Typisch bei: schlecht geborgenem Segel, Manövern mit offenen Segeln, Motor unter Segel mit schlagenden Segeln.

**Visuelle Erkennungsmerkmale:**
- Abrieb entlang der Nähte
- Gelöste Nähte (besonders am Achterliek)
- Delamination bei Laminatsegeln (weiße Flecken)
- Lose/gebrochene Latten
- Gelöste Patches oder Verstärkungen
- Rissbildung an Lattentaschen-Enden

**Ursachen:**
1. Segel nicht rechtzeitig geborgen oder gerefft
2. Regelmäßiges Motoren mit schlagendem Groß
3. Fehlende Lazybag/Lazyjack → Segel schlägt beim Bergen
4. Wende mit losem Vorsegel (Fock schlägt gegen Want)
5. Hafen-/Ankerliegen mit teilweise gesetztem Segel

**Korrekturmaßnahmen:**
1. Geschädigte Nähte durch Segelmacher nähen lassen: 50–200 EUR pro Reparatur
2. Delaminations-Patches bei Laminatsegeln: 100–400 EUR
3. Prävention: Lazybag/Lazyjack installieren (200–600 EUR)
4. Segel bei Nichtgebrauch immer vollständig bergen
5. Vorsegel-Furler nutzen (statt lose lassen)

**AYDI-Fehlerkennzeichnung:** `F-16_07-11`
**Schweregrad:** Mittel (Lebensdauerverkürzung) bis Hoch (Sicherheit bei Nahtversagen)
**Confidence bei visueller Erkennung:** `visual_high`

### 10.12 F-16_07-12: Laminare Separation (Laminar Separation Bubble)

**Beschreibung:**
Die laminare Grenzschicht löst sich vom Segel ab, bevor sie turbulent wird. Es entsteht eine "Blase" langsamer/rückwärts strömender Luft auf der Seeseite. Dies reduziert den Auftrieb erheblich und erhöht den Widerstand.

**Visuelle Erkennungsmerkmale:**
- Schwierig visuell zu erkennen
- Telltale-Indikatoren: Lee-Telltales am Vorliek steigen trotz scheinbar korrektem Trimm periodisch an
- Boot macht weniger Höhe und Speed als erwartet
- Problem tritt besonders bei glattem Seegang und konstantem Wind auf

**Ursachen:**
1. Eintrittswinkel zu klein (zu scharfe Vorderkante)
2. Segel zu flach bei Leichtwind → Reynolds-Zahl zu niedrig
3. Vorliek-Profil nicht aerodynamisch (zu eckig)
4. Übertriebenes Depowering bei Leichtwind

**Korrekturmaßnahmen:**
1. Segel bauchiger trimmen → Eintrittswinkel vergrößern
2. Cunningham lösen → weicherer Eintritt
3. Achterstag lockern → Vorstag-Sag erlauben → bauchigerer Eintritt
4. Turbulatoren (selten) → nur bei Regattasegeln (umstritten)

**AYDI-Fehlerkennzeichnung:** `F-16_07-12`
**Schweregrad:** Niedrig (subtiler Leistungsverlust)
**Confidence bei visueller Erkennung:** `visual_low` (visuell kaum erkennbar)

---

## 11. Troubleshooting

### 11.1 Entscheidungsbaum: "Boot macht keine Höhe am Wind"

```
Boot macht keine Höhe am Wind
├── Segel zu bauchig?
│   ├── Ja → Cunningham setzen, Outhaul durchsetzen, Achterstag spannen
│   │   └── Immer noch zu bauchig? → Segel gealtert → Segelmacher konsultieren
│   └── Nein → Weiter
├── Vorstag-Sag zu groß?
│   ├── Ja → Achterstag spannen, Running Backstays setzen
│   │   └── Sag reduziert sich nicht? → Rigg-Spannung prüfen (Rigger)
│   └── Nein → Weiter
├── Achterliek gehooked?
│   ├── Ja → Schot fieren, Traveller Lee, Vang lockern
│   │   └── Hook bleibt? → Segel-Profil vom Segelmacher prüfen
│   └── Nein → Weiter
├── Slot zu eng?
│   ├── Ja → Vorsegel-Schot fieren, Holepunkt nach außen
│   └── Nein → Weiter
├── Segelplan nicht balanciert?
│   ├── Luvhelm → Groß reffen oder Vorsegel vergrößern
│   └── Leehelm → Vorsegel reffen oder Groß dichter
└── Rumpf-Problem?
    ├── Unterwasserschiff verschmutzt → Reinigen
    ├── Kiel-/Ruder-Profil beschädigt → Werft
    └── Seegras am Kiel → Rückwärts fahren
```

### 11.2 Entscheidungsbaum: "Boot krängt zu stark"

```
Boot krängt übermäßig (>25° bei 14 kn TWS)
├── Segel zu bauchig?
│   ├── Ja → Depower-Sequenz (Cunningham, Outhaul, Achterstag)
│   └── Nein → Weiter
├── Traveller zu hoch?
│   ├── Ja → Traveller nach Lee
│   └── Nein → Weiter
├── Segelfläche zu groß?
│   ├── Ja → 1. Reff setzen (Großsegel)
│   │   └── Immer noch zu viel? → 2. Reff + Vorsegel reffen
│   └── Nein → Weiter
├── Crew-Gewicht falsch positioniert?
│   ├── Ja → Crew auf Luvseite, ausreiten
│   └── Nein → Weiter
└── Strukturelles Stabilitätsproblem?
    └── Möglich → Ballast, Trimmtanks, Design-Analyse
```

### 11.3 Entscheidungsbaum: "Segel flattert am Vorliek"

```
Vorliek-Flutter
├── Fall ausreichend durchgesetzt?
│   ├── Nein → Fall dichtholen
│   └── Ja → Weiter
├── Cunningham gesetzt (Großsegel)?
│   ├── Nein → Cunningham leicht setzen
│   └── Ja → Weiter
├── Vorliekkurve passt zum Mast?
│   ├── Zu viel Mastbiegung → Babystay lockern, Achterstag lockern
│   ├── Zu wenig Mastbiegung → Unwahrscheinlich als Flutter-Ursache
│   └── Nicht bekannt → Segelmacher konsultieren
├── Vorstag-Spannung ausreichend (Vorsegel)?
│   ├── Nein → Achterstag spannen
│   └── Ja → Weiter
└── Segel permanent verformt?
    └── Ja → Segelmacher: Vorliekkurve korrigieren oder Segel ersetzen
```

### 11.4 Entscheidungsbaum: "Ruderdruck zu hoch"

```
Übermäßiger Ruderdruck (Lee- oder Luvhelm)
├── Luvhelm (Boot will anluven)?
│   ├── Großsegel dominant → Groß fieren / reffen
│   ├── Vorsegel zu klein → Größeres Vorsegel setzen
│   ├── Mast zu weit achtern geneigt → Mast Rake reduzieren
│   └── Boot krängt zu stark → Depower (siehe 11.2)
├── Leehelm (Boot will abfallen)?
│   ├── Vorsegel dominant → Vorsegel reffen / kleiner
│   ├── Großsegel zu klein / offen → Groß dichter
│   ├── Mast zu weit vorn geneigt → Mast Rake erhöhen
│   └── Seltener: Rigg-Problem → Rigger konsultieren
└── Helm variiert stark mit Böen?
    ├── Normal bei Böen bis ±3° Ruderlage
    └── Exzessiv (>5° Schwankung) → Segel nicht autobalanciert → Twist erhöhen
```

### 11.5 Entscheidungsbaum: "Performance unter Polar"

```
Boot fährt unter Polardaten-Potenzial
├── Segel-Trimm korrekt?
│   ├── Nein → Trimm nach Windstärke/Kurs optimieren (Abschnitt 8)
│   └── Ja → Weiter
├── Segel-Zustand gut?
│   ├── Nein (Alter, Verschleiß) → Segel ersetzen/überarbeiten
│   └── Ja → Weiter
├── Rumpf-Zustand?
│   ├── Bewuchs → Reinigen, Antifouling
│   ├── Propeller → Faltpropeller nachrüsten
│   └── Wasserpass-Linie korrekt?
├── Rigg-Tuning?
│   ├── Wanten-Spannung korrekt? → Rigger-Check
│   ├── Mast Rake optimal? → Einstellen
│   └── Mastbiegung kontrolliert? → Babystay, Wanten
├── Segelfläche optimal?
│   ├── Zu wenig Fläche → Genua statt Fock, Code 0
│   └── Zu viel Fläche → Reffen
└── Instrumente kalibriert?
    ├── Log (Geschwindigkeit) → Kalibrieren
    ├── Windmesser → Korrektur
    └── Kompass → Deviation prüfen
```

---

## 12. Segelvermessung und -analyse

### 12.1 Streifen-Analyse (Stripe Analysis)

Die Streifen-Analyse ist die wichtigste Methode zur Segelform-Beurteilung auf dem Wasser.

**Methode:**
1. Horizontale Streifen werden auf das Segel aufgebracht (bei der Herstellung oder nachträglich)
2. Typisch: 4–5 Streifen in gleichmäßigen Abständen (25%, 40%, 55%, 70%, 85% Höhe)
3. Foto von unten (durch die Luke) oder von achtern
4. Streifen zeigen die Profilkurve in der jeweiligen Höhe

**Analyse der Streifen:**
- **Bauchtiefe**: Maximale Auslenkung des Streifens = Bauchtiefe an dieser Höhe
- **Bauchposition**: Position der maximalen Auslenkung entlang des Streifens = Draft Position
- **Twist**: Verdrehung der Streifen von unten nach oben = Twist
- **Entry Angle**: Winkel am Vorliek-Ende des Streifens
- **Exit Angle**: Winkel am Achterliek-Ende des Streifens

**Fotografieren:**
- Kamera direkt unter dem Baum, nach oben gerichtet
- Oder: vom Heck, Kamera auf Baumhöhe
- Segel muss geladen sein (im Wind stehen)
- Mehrere Fotos bei verschiedenen Windstärken

### 12.2 SailTrim Apps und digitale Analyse

**B&G SailTrim:**
- Integriert in B&G Instrumenten-System
- Polardaten-Vergleich in Echtzeit
- Trimm-Vorschläge basierend auf Wind/Kurs

**Sailmon:**
- Unabhängiges Trimm-Analyse-System
- Verwendet Kameras im Mast → automatische Streifen-Analyse
- Echtzeit-Profil-Darstellung
- Preis: System ab ca. 3.000 EUR

**Expedition (Nick White Software):**
- Routing- und Performance-Software
- VPP-basierte Trimm-Analyse
- Standard bei Offshore-Regatten
- Preis: Lizenz ca. 500–1.500 EUR

**SailOracle:**
- KI-basierte Segelanalyse aus Fotos
- App-basiert (iOS/Android)
- Analyse von Profil, Twist, Bauch per Fotoanalyse
- Preis: ca. 10–20 EUR/Monat

### 12.3 WB-Sails und Sail-Analyse-Software

**WB-Sails (Finne):**
- Professionelle Segelmacher-Software
- FEA-basierte Analyse der Segelform unter Last
- Used by: Doyle, Quantum, viele unabhängige Lofts
- Berechnet optimale Broadseam-Verteilung

**SMAR Azure:**
- Standard-Industrie-Segelmacher-CAD
- Panel-Layout, Schnittmuster, Broadseaming
- Datenbank-Integration für Materialien

### 12.4 Segel-Dokumentation für AYDI

Für die AYDI-Analyse werden folgende Segel-Daten benötigt:

**Level 1 (Schnellanalyse):**
- Segeltyp (Groß, Genua, Fock, etc.)
- Material (Dacron, Laminat, 3Di, etc.)
- Alter in Jahren
- Schnittmethode (wenn bekannt)
- Fotos (mindestens Profilansicht von der Seite)

**Level 2 (Profi-Werkzeug):**
- Alle Level-1-Daten
- Streifen-Analyse-Fotos (min. 3 Windstärken)
- Segelmacher und Modell
- Vermessungsdaten (Luff, Leech, Foot, LP)
- Materialspezifikation (Tuchgewicht, Hersteller)
- Reparatur-Historie
- Segelstunden / Seemeilen

---

## 13. FAQ — Häufige Fragen

### FAQ 1: Wie oft sollte ein Segel gewechselt werden?
**Antwort:** Fahrtensegel aus Dacron halten bei guter Pflege 6–12 Jahre. Indikatoren für Ersatz: Bauch permanent zu weit achtern (nicht mehr trimmbar), UV-Verfärbung >50%, Nähte gelöst, Tuch fühlt sich "knisternd" an. Ein Segelmacher kann die Restlebensdauer einschätzen (Confidence: documented).

### FAQ 2: Lohnt sich der Aufpreis für Tri-Radial gegenüber Cross-Cut?
**Antwort:** Für Performance-Cruiser und Club-Regatta ja (ca. 40–60% Aufpreis für 15–25% bessere Formstabilität). Für reine Fahrtensegel, die primär gerollt werden, ist der Vorteil gering. Für Blauwasser-Segler mit Reparatur-Anforderung ist Cross-Cut Dacron die sicherere Wahl (Confidence: estimated).

### FAQ 3: 3Di oder Stratis — was ist besser?
**Antwort:** 3Di hat eine leicht bessere Formstabilität (besonders bei Carbon-Varianten). Stratis ist flexibler in der Materialkombination und ca. 15–20% günstiger. Für Performance-Cruiser sind beide ausgezeichnet. Entscheidend ist oft der lokale Segelmacher-Support (Confidence: estimated).

### FAQ 4: Kann ich mein Großsegel selbst trimmen lernen?
**Antwort:** Ja. Die Grundlagen (Schot, Traveller, Cunningham, Outhaul) sind in einem Segeltrimm-Kurs (z.B. NRV, KYC, DSV) in 1–2 Tagen erlernbar. Die Feinabstimmung (Mastbiegung, Vorstag-Sag) erfordert Erfahrung. Empfehlung: 10 Stunden bewusstes Üben auf dem Wasser mit Streifen-Analyse-Fotos (Confidence: documented).

### FAQ 5: Was kostet eine komplette Segelgarderobe für eine 40-Fuß-Yacht?
**Antwort (2025/2026 Schätzung):**
| Segel | Budget (Dacron) | Mittelklasse | Premium (3Di/Stratis) |
|-------|----------------|-------------|----------------------|
| Großsegel | 3.500 EUR | 6.000 EUR | 14.000 EUR |
| Genua (135%) | 3.000 EUR | 5.000 EUR | 11.000 EUR |
| Fock (100%) | 2.000 EUR | 3.500 EUR | 7.000 EUR |
| Gennaker | 2.500 EUR | 4.000 EUR | 7.000 EUR |
| Sturmfock | 800 EUR | 1.200 EUR | 1.200 EUR |
| **Gesamt** | **11.800 EUR** | **19.700 EUR** | **40.200 EUR** |
(Confidence: estimated — Marktpreise 2025/2026)

### FAQ 6: Rollgroßsegel — empfehlenswert?
**Antwort:** In-Mast-Rollgroßsegel bieten enormen Komfort (Einhand-Reffen), aber mit erheblichem Performance-Verlust (ca. 15–25% Segelfläche weniger, kein Roach, keine Latten, schlechteres Profil). In-Boom-Rollgroß ist der bessere Kompromiss (Latten möglich, etwas Roach), aber teuer (System 5.000–15.000 EUR). Für Kurzhandsegler und Charteryachten sehr sinnvoll, für Performance-orientierte Segler nicht empfehlenswert (Confidence: documented).

### FAQ 7: Wann sollte ich reffen?
**Antwort:** Faustregeln:
- 1. Reff Großsegel: Wenn das Boot >25° krängt bei konstantem Wind (oder >5° Ruderlage)
- Vorsegel reffen: Gleichzeitig oder kurz nach 1. Reff Groß
- 2. Reff Groß: Bei >20 kn TWS für Fahrtensegler / >25 kn für Regatta
- 3. Reff / Sturmbesegelung: Bei >30 kn TWS
- "If you think about reefing, it's time to reef." (Confidence: documented)

### FAQ 8: Was ist der optimale Schotwinkel für hoch am Wind?
**Antwort:** 7–12° bei überlappender Genua, 10–15° bei nicht-überlappender Fock. Gemessen als Winkel zwischen Bootsmittellinie und der Linie Holepunkt→Schothorn. Performance-Yachten segeln bei 6–8°, Fahrtenyachten bei 10–14° (Confidence: documented).

### FAQ 9: Mein Segel hat Schimmelflecken — was tun?
**Antwort:** Dacron: Mit Oxalsäure-Lösung (3–5%) oder speziellem Segelreiniger (z.B. Star brite Sail & Canvas Cleaner) behandeln. Einweichen, sanft bürsten, gründlich spülen. Laminatsegel: Nur sanft waschen, kein Schrubben (Delamination-Risiko). Prävention: Segel trocken lagern, gute Belüftung, Segel nie nass einpacken (Confidence: documented).

### FAQ 10: Wie messe ich den Vorstag-Sag?
**Antwort:** Methode 1: Senkblei vom Masttopp-Beschlag hängen und Abstand zum Vorstag in halber Höhe messen (bei ruhigem Wasser, ohne Segel). Methode 2: Foto des Vorstags unter Last (mit Segel bei Wind), Abstand zum geraden Referenz messen (skaliert). Typische Werte: 30–150 mm bei 14 m Vorstag (Confidence: documented).

### FAQ 11: Was bedeutet "LP" bei Vorsegeln?
**Antwort:** LP = Luff Perpendicular = die kürzeste (senkrechte) Distanz vom Schothorn (Clew) zum Vorliek (Luff). LP in Prozent des Vordreiecks-Fuß (J) gibt die Überlappung an: LP/J × 100%. Genua 135% = LP ist 35% länger als J. Nicht-überlappende Fock: LP/J ≤ 100% (Confidence: measured).

### FAQ 12: Kann ich Carbon-Segel reparieren?
**Antwort:** 3Di Carbon: Nur im North-Sails-Loft reparierbar (Spezialverfahren). Stratis mit Carbon: Doyle-Lofts oder autorisierte Partner. Preis für Patch-Reparatur: 200–800 EUR je nach Größe. Für große Schäden oft nicht wirtschaftlich (Confidence: documented).

### FAQ 13: Welche Telltale-Wolle ist die beste?
**Antwort:** Merino-Wolle (fein, 1-fädig) ist der Klassiker. Alternativ: Nylon-Bänder (länger sichtbar bei Regen). Marken: Davis Instruments Telltale Strips, Easysails. Selbstgemacht: rote + grüne Wolle, 20–25 cm lang, mit Segelnadel durch das Segel gestochen und verknotet (Confidence: documented).

### FAQ 14: Wie lagere ich Segel über den Winter?
**Antwort:** 1. Segel waschen (Süßwasser, Segelreiniger). 2. Vollständig trocknen (nie feucht lagern!). 3. Locker falten oder rollen (nie knicken bei Laminaten). 4. In trockenem, belüftetem Raum lagern. 5. Nicht in Segeltasche lassen (Kondensation). 6. UV-geschützt lagern. 7. Bei Laminaten: in Rolle lagern, nicht falten (Confidence: documented).

### FAQ 15: Lohnt sich ein Segeltrimm-Kurs?
**Antwort:** Eindeutig ja. Ein 2-Tages-Trimm-Kurs (z.B. beim DSV, NRV, oder bei Segelmachern wie Quantum/North) verbessert die Performance typischerweise um 5–15% und den Spaß um 100%. Kosten: 200–500 EUR. Amortisiert sich durch weniger Segelverschleiß und längere Lebensdauer (Confidence: documented).

### FAQ 16: Was ist der Unterschied zwischen Warp und Fill bei Dacron?
**Antwort:** Warp = Kettfaden (Längsrichtung des Webstuhls, stärker). Fill = Schussfaden (Querrichtung, leicht dehnbarer). Fill-oriented Dacron: Schussfaden in Paneel-Längsrichtung → ideal für Cross-Cut. Warp-oriented: Kettfaden in Paneel-Richtung → für Tri-Radial. Die Wahl beeinflusst die Dehnungseigenschaften entlang und quer zur Paneel-Richtung (Confidence: measured).

### FAQ 17: Mein Vorsegel hat sich oben geöffnet — was tun?
**Antwort:** Symptom: Oberes Drittel des Vorsegels steht zu weit offen (zu viel Twist oben). Ursachen: Holepunkt zu weit achtern, Schot zu lose, oder Vorstag zu viel Sag oben. Maßnahme: Holepunkt 5–10 cm nach vorn, Schot dichter holen, Achterstag spannen (Confidence: documented).

### FAQ 18: Kann ich ein Großsegel ohne Latten fahren?
**Antwort:** Technisch ja, aber mit erheblichem Leistungsverlust (kein Roach, Achterliek flattert). Einzige sinnvolle Anwendung: In-Mast-Rollgroßsegel (dort zwingend lattenlos). Für alle anderen Anwendungen sind mindestens Teillatten Standard und empfohlen (Confidence: documented).

### FAQ 19: Wie erkenne ich, ob mein Segel UV-geschädigt ist?
**Antwort:** 1. Farbveränderung (Bleichen, besonders an der UV-Schutzleiste). 2. Tuch fühlt sich steif und spröde an ("Knistertest"). 3. Nähgarn dünn und brüchig. 4. Bei Laminaten: Mylar wird milchig/opak. 5. Festigkeitsverlust: Tuch kann mit den Fingern eingerissen werden (bei starker Schädigung). Test: An einer Stelle ohne Belastung ein Stück Tuch zwischen Daumen und Zeigefinger reiben — bei UV-Schaden lösen sich Fasern (Confidence: documented).

### FAQ 20: Was kostet eine Segelreparatur?
**Antwort (Richtwerte 2025/2026):**
| Reparatur | Dacron | Laminat |
|-----------|--------|---------|
| Naht nacharbeiten (1 m) | 30–60 EUR | 50–100 EUR |
| Patch setzen (30×30 cm) | 80–150 EUR | 150–400 EUR |
| Riss reparieren (50 cm) | 100–250 EUR | 200–500 EUR |
| Lattentasche ersetzen | 60–120 EUR | 100–200 EUR |
| Eckpatch ersetzen | 150–300 EUR | 250–600 EUR |
| Segel reprofilieren | 300–800 EUR | Nicht empfohlen |
| UV-Band ersetzen (Vorsegel) | 200–500 EUR | 200–500 EUR |
(Confidence: estimated)

### FAQ 21: Welches Material für Blauwasser — Dacron oder Laminat?
**Antwort:** Dacron ist für Blauwasser der klare Gewinner: UV-beständig, reparierbar in jedem Hafen weltweit, langlebig, robust gegen Schlagen/Knicken. Laminat und Membransegel können auf Blauwasser-Reisen nicht oder nur schwer repariert werden. Ausnahme: 3Di NORDAC zeigt gute Langlebigkeit und lässt sich teilweise lokal reparieren (Confidence: documented).

### FAQ 22: Wie berechne ich die ideale Segelfläche für mein Boot?
**Antwort:** Grobe Faustformel: SA/D-Ratio (Sail Area to Displacement Ratio) = Segelfläche (m²) / (Verdrängung in m³)^(2/3). Werte: Cruiser 16–20, Cruiser-Racer 20–24, Racer 24–30. Ein Bootsdesigner oder Segelmacher kann die optimale Segelfläche basierend auf Stabilitätsrechnungen und CE-Kategorie ermitteln (Confidence: calculated).

### FAQ 23: Was bedeutet ORC/IRC-Rating im Bezug auf Segelschnitt?
**Antwort:** ORC und IRC vermessen Segel (Luff, Leech, Foot, Roach, LP) und berechnen daraus ein Handicap. Ein Segel mit mehr Fläche oder höherem Roach erhält ein schlechteres (höheres) Rating. Segelmacher optimieren daher "auf die Regel" — maximale Performance innerhalb der Rating-Grenze (Confidence: documented).

### FAQ 24: Mein neues Segel hat Falten — ist das normal?
**Antwort:** Leichte Falten bei einem neuen Segel sind normal — das Tuch muss sich "einfahren" (ca. 20–50 Segelstunden). Horizontale Falten am Vorliek verschwinden, wenn sich das Tuch leicht streckt. Wenn Falten nach 50 Stunden bestehen bleiben, Segelmacher kontaktieren. Bei Laminatsegeln sollten ab Werk keine Falten vorhanden sein (Confidence: documented).

### FAQ 25: Wie beeinflusst die Crew-Größe den Segeltrimm?
**Antwort:** Mehr Crew-Gewicht auf Luv → Boot aufrechter → weniger Reff nötig → aggressiverer Trimm möglich. Weniger Crew → früher reffen, defensiverer Trimm. Einhandsegler → selbstwendende Fock empfohlen, Rollreff für schnelle Anpassung, konservativer Segelplan. Die Trimm-Strategie muss immer an die verfügbare Crew-Power angepasst werden (Confidence: documented).

### FAQ 26: Was ist ein "Depower Groove"?
**Antwort:** Der Bereich, in dem das Segel durch Trimm schrittweise entmachtet wird, bevor gerefft werden muss. Ein gutes Segel hat einen breiten Depower-Groove (z.B. 12–20 kn TWS ohne Reff). Die Depower-Reihenfolge: Traveller Lee → Cunningham + Outhaul → Achterstag → Schot-Twist → Reffen. Ein breiter Groove macht seltenes Reffen nötig (Confidence: documented).

---

## 14. Glossar

| Begriff | Englisch | Definition |
|---------|----------|-----------|
| Achterliek | Leech | Hinterkante des Segels (Kopf → Schothorn) |
| Achterstag | Backstay | Stag vom Masttopp nach Heck; kontrolliert Mastbiegung und Vorstag-Spannung |
| Anstellwinkel | Angle of Attack | Winkel zwischen Sehne des Segelprofils und der Anströmrichtung |
| Aufschießer | Luffing | Boot dreht in den Wind → Segel flattern |
| Babystag | Babystay / Innerforestay | Zusätzliches Stag vom Mast (ca. 60% Höhe) zum Vordeck |
| Barber Hauler | Barber Hauler | Leine zur seitlichen Verschiebung des Holepunkts |
| Bauchpunkt | Draft Position | Position der maximalen Profiltiefe, gemessen vom Vorliek |
| Bauchtiefe | Draft / Camber | Maximale Tiefe des Segelprofils, in % der Profiltiefe |
| Baumniederholer | Vang / Kicking Strap | Zug zwischen Baum und Mast-Fuß; kontrolliert Twist |
| Broadseaming | Broadseaming | Nahtformgebung zur 3D-Formgebung flacher Paneele |
| Bullenstander | Preventer | Leine vom Baum nach vorn; verhindert Patenthalse |
| CE | Centre of Effort | Druckpunkt des Segelplans |
| CLR | Centre of Lateral Resistance | Schwerpunkt des Unterwasser-Lateralplans |
| Cross-Cut | Cross-Cut | Horizontale Paneel-Anordnung |
| Cunningham | Cunningham | Vorliekstrecker; zieht Vorliek nach unten → Bauch nach vorn |
| Depowering | Depowering | Schrittweises Entmachten des Segels bei zunehmendem Wind |
| Draft | Draft | Bauchtiefe des Segelprofils |
| Eintrittswinkel | Entry Angle | Winkel des Profils am Vorliek |
| Fieren | Ease / Pay Out | Schot oder Leine lockern / nachlassen |
| Forestay Sag | Forestay Sag | Durchhang des Vorstags unter Last |
| Full Battens | Full Battens | Volllatten (reichen von Vorliek bis Achterliek) |
| Groß | Main / Mainsail | Großsegel |
| Holepunkt | Sheet Lead / Car Position | Umlenkpunkt der Vorsegelschot |
| Hook | Leech Hook | Achterliek biegt nach Luv — Strömungsblockade |
| Latte | Batten | Steifes Element in Segeltasche zur Profilstützung |
| Leehelm | Lee Helm | Boot will abfallen — CE vor CLR |
| Loose-Footed | Loose-Footed | Segel nur an Hals und Schothorn am Baum befestigt |
| Luvhelm | Weather Helm | Boot will anluven — CE achtern von CLR |
| Mast Bend | Mast Bend | Biegung des Mastes (vorn-achtern) |
| Mast Rake | Mast Rake | Neigung des Mastes nach achtern |
| Outhaul | Outhaul | Schothornausholer am Unterliek |
| Prebend | Prebend | Vorbiegen des Mastes ohne Segellast |
| Roach | Roach | Segelfläche jenseits der Kopf-Schothorn-Linie |
| Schamfilen | Chafe | Reibungsverschleiß |
| Schothorn | Clew | Hintere untere Ecke des Segels |
| Slot | Slot | Spalt zwischen Vorsegel-Achterliek und Groß-Luvseite |
| Square-Top | Square-Top | Großsegel mit breitem, eckigem Kopf |
| Telltale | Telltale | Strömungsfaden/Wollfaden zur Strömungsvisualisierung |
| Tri-Radial | Tri-Radial | Drei-Zonen-Radialschnitt |
| Trimm | Trim | Einstellung/Optimierung der Segelform |
| Twist | Twist | Verdrehung des Segels von Fuß zu Kopf |
| Vorliek | Luff | Vorderkante des Segels |
| Vorstag | Forestay / Headstay | Stag vom Masttopp (oder fraktional) zum Bug |

---

## 15. Schnell-Referenz

### 15.1 Trimm-Schnellübersicht Großsegel

```
┌────────────────────────────────────────────────────────────────────────┐
│              GROSSSEGEL-TRIMM — SCHNELLREFERENZ                       │
├──────────────┬──────────────┬──────────────┬──────────────────────────┤
│              │ Leichtwind   │ Mittelwind   │ Frischer Wind            │
│              │ (0-8 kn)     │ (8-16 kn)    │ (16-25 kn)               │
├──────────────┼──────────────┼──────────────┼──────────────────────────┤
│ Großschot    │ Moderat      │ Dicht        │ Fieren (Twist!)          │
│ Traveller    │ Luv          │ Mitte        │ Lee                      │
│ Cunningham   │ Lose         │ Leicht       │ Fest                     │
│ Outhaul      │ Lose         │ Moderat      │ Durchgesetzt             │
│ Vang         │ Lose         │ Moderat      │ Fest                     │
│ Achterstag   │ Locker       │ Moderat      │ Fest                     │
│ Bauchtiefe   │ 12-15%       │ 10-12%       │ 6-8%                     │
│ Bauchpunkt   │ 45-50%       │ 38-42%       │ 33-38%                   │
│ Twist        │ Minimal      │ Moderat      │ Offen                    │
└──────────────┴──────────────┴──────────────┴──────────────────────────┘
```

### 15.2 Trimm-Schnellübersicht Vorsegel

```
┌────────────────────────────────────────────────────────────────────────┐
│              VORSEGEL-TRIMM — SCHNELLREFERENZ                         │
├──────────────┬──────────────┬──────────────┬──────────────────────────┤
│              │ Leichtwind   │ Mittelwind   │ Frischer Wind            │
│              │ (0-8 kn)     │ (8-16 kn)    │ (16-25 kn)               │
├──────────────┼──────────────┼──────────────┼──────────────────────────┤
│ Schot        │ Moderat      │ Dicht        │ Leicht fieren            │
│ Holepunkt    │ Standard     │ Standard     │ Achtern (+5-10 cm)       │
│ Fall         │ Locker       │ Moderat      │ Fest                     │
│ Achterstag   │ Locker       │ Moderat      │ Fest                     │
│ Slot         │ Moderat      │ Optimal      │ Weiter                   │
│ Telltales    │ Alle gleich  │ Alle gleich  │ Oben etwas offen         │
└──────────────┴──────────────┴──────────────┴──────────────────────────┘
```

### 15.3 Depower-Sequenz

```
Zunehmender Wind →

1. Traveller nach Lee (sofortiger Effekt)
2. Cunningham + Outhaul durchsetzen (Profil flacher)
3. Achterstag spannen (Mast biegen + Vorstag straff)
4. Großschot fieren für Twist (oberes Segel öffnet)
5. *** 1. REFF *** (ab ca. 18-22 kn / 25° Krängung)
6. Vorsegel reffen / kleineres Vorsegel
7. *** 2. REFF *** (ab ca. 25-28 kn)
8. Vorsegel stark reffen
9. *** 3. REFF / STURMBESEGELUNG *** (ab ca. 30+ kn)
```

### 15.4 Fehlerbild-Schnelldiagnose

| Symptom | Wahrscheinliches Problem | Erste Maßnahme |
|---------|------------------------|----------------|
| Boot krängt stark | Zu viel Segelfläche/Bauch | Depower (15.3) |
| Wenig Höhe am Wind | Segel zu bauchig / Vorstag-Sag | Achterstag + Cunningham |
| Wenig Speed am Wind | Segel zu flach | Achterstag lockern, Cunningham lose |
| Starker Luvhelm | Groß zu dominant | Groß fieren/reffen |
| Achterliek-Flattern | Zu wenig Schot/Vang | Schot/Vang dichter |
| Vorliek-Falten | Cunningham nötig oder Mast zu gebogen | Cunningham / Achterstag |

---

## ANHANG A — Fallstudie: Regatta-Großsegel Bavaria 40

### Ausgangssituation
- **Boot**: Bavaria 40 Cruiser (Bj. 2018)
- **Bestehendes Segel**: Cross-Cut Dacron Großsegel, ab Werft, 5 Jahre alt
- **Problem**: Boot ist in Club-Regatten (ORC) nicht konkurrenzfähig. Segel wirkt bauchig und unkontrolliert.

### Analyse (AYDI Level 2)
- Streifen-Analyse: Bauchtiefe 16% bei 12 kn → zu bauchig
- Bauchposition: 52% → deutlich zu weit achtern
- Twist: Übermäßig → obere 30% des Segels leisten nichts
- Material-Zustand: Dacron gedehnt, UV-Schaden am Achterliek (Lee-Seite)
- **AYDI-Score Segelzustand: 42/100** (unzureichend für Regatta)

### Empfehlung
1. Neues Großsegel: Tri-Radial Laminat (Dimension Polyant D4-Serie)
2. Full-Batten-Konversion (4 Volllatten + Antal Batten Cars)
3. Segelmacher: Quantum Sails Deutschland (Loft Hamburg)

### Umsetzung und Kosten
| Position | Kosten |
|----------|--------|
| Großsegel Tri-Radial Laminat (Quantum Fusion M) | 6.800 EUR |
| Full-Batten-Umrüstung (Latten + Cars) | 950 EUR |
| Installation und Trimm-Einstellung | 300 EUR |
| **Gesamt** | **8.050 EUR** |

### Ergebnis
- Streifen-Analyse nach 20 Segelstunden: Bauchtiefe 11%, Position 40% → exzellent
- ORC-Regatta-Performance: +0,8 kn VMG am Wind → 2 Platzierungen besser
- **AYDI-Score nach Upgrade: 84/100**

---

## ANHANG B — Fallstudie: Fahrtensegel-Trimm Hallberg-Rassy 44

### Ausgangssituation
- **Boot**: Hallberg-Rassy 44 (Bj. 2020)
- **Segel**: North Sails 3Di NORDAC Großsegel + Genua (2 Jahre alt)
- **Problem**: Eigner klagt über übermäßige Krängung bei 14–18 kn, Boot fühlt sich "schwer" an

### Analyse (AYDI Level 2)
- Trimm-Analyse (Fotos unter Segeln): Traveller permanent auf Mitte, Cunningham nicht gesetzt
- Achterstag: Handspanner nur auf 30% Spannung
- Vorstag-Sag: Geschätzt 90 mm bei 14 kn → zu viel
- Holepunkt: Standardposition, nicht windabhängig angepasst
- Segel-Zustand: Exzellent (2 Jahre, 3Di NORDAC)
- **AYDI-Score Trimm: 45/100** (Segel gut, Trimm schlecht)

### Empfehlung
1. Trimm-Kurs für Eigner (2 Tage, bei North Sails oder Sailing-Academy)
2. Achterstag-Hydraulik nachrüsten (statt Handspanner): schnellere Verstellung
3. Trimm-Protokoll nach AYDI-Empfehlung

### Umsetzung
- Trimm-Kurs: 400 EUR
- Achterstag-Hydraulik (Navtec): 2.800 EUR inkl. Einbau
- 5 Stunden Trimm-Training auf dem Wasser mit Profi: 500 EUR

### Ergebnis
- Krängung bei 16 kn TWS: von 28° auf 20° reduziert
- VMG am Wind: +0,5 kn
- Eigner-Zufriedenheit: "Wie ein neues Boot"
- **AYDI-Score Trimm nach Training: 78/100**

---

## ANHANG C — Fallstudie: Code 0 Optimierung J/111

### Ausgangssituation
- **Boot**: J/111 (Performance Racer-Cruiser)
- **Problem**: Code 0 von Drittanbieter-Segelmacher kollabiert bei >12 kn TWS, flattern bei <6 kn
- **Einsatzbereich**: TWA 50–90°, 4–16 kn TWS

### Analyse
- Code 0 Material: zu leichtes Laminat (0.75 oz statt 1.5 oz)
- Schnitt: Flacher als nötig, Entry Angle zu gering (4°)
- Luff Tape: zu dünn, gibt nach → Profil kollabiert
- Furler: Facnor FX+ 2500 → korrekt dimensioniert
- **AYDI-Score: 38/100**

### Empfehlung
- Neuer Code 0 von UK Sailmakers (Tape-Drive Laminat)
- Stärkeres Luff Tape (Dyneema, 8 mm)
- Entry Angle 8–10° für breiteren Einsatzbereich

### Ergebnis nach Neukauf
- Einsatzbereich: TWA 45–100°, 5–18 kn TWS → deutlich breiter
- Material: Dimension Polyant MLX (1.5 oz Laminat)
- Kosten: 4.200 EUR
- **AYDI-Score: 82/100**

---

## ANHANG D — Fallstudie: Membransegel vs. Tri-Radial Swan 53

### Ausgangssituation
- **Boot**: Nautor Swan 53 (Bj. 2016)
- **Dilemma**: Eigner segelt 80% Fahrt, 20% Club-Regatta. Bisherige Segel: 3DL (6 Jahre alt, Delamination)
- **Budget**: max. 35.000 EUR für Großsegel + Genua

### Vergleichsanalyse

| Kriterium | Tri-Radial Pentex | Doyle Stratis ICE | North 3Di NORDAC |
|-----------|-------------------|-------------------|------------------|
| Großsegel | 8.500 EUR | 12.000 EUR | 14.000 EUR |
| Genua 135% | 7.000 EUR | 10.000 EUR | 12.000 EUR |
| **Gesamt** | **15.500 EUR** | **22.000 EUR** | **26.000 EUR** |
| Formstabilität | ★★★★☆ | ★★★★★ | ★★★★★ |
| Lebensdauer (Fahrt) | 7–10 Jahre | 7–9 Jahre | 8–12 Jahre |
| Reparierbarkeit | ★★★★★ | ★★★★☆ | ★★★☆☆ |
| Regatta-Performance | ★★★☆☆ | ★★★★☆ | ★★★★★ |
| Rollreff-Eignung | ★★★★☆ | ★★★☆☆ | ★★★★☆ (NORDAC) |

### Empfehlung
Doyle Stratis ICE als optimaler Kompromiss: Performance für Regatta, Haltbarkeit für Fahrt, innerhalb Budget.

### Ergebnis
- Stratis ICE Großsegel + Genua bestellt: 22.000 EUR
- Nach 1 Saison: 3 Regatta-Podiumsplätze, Fahrt-Performance hervorragend
- **AYDI-Score: 88/100**

---

## ANHANG E — Fallstudie: Langfahrt-Segelgarderobe Oyster 565

### Ausgangssituation
- **Boot**: Oyster 565 (Bj. 2019)
- **Vorhaben**: 3-Jahres-Weltumsegelung ab 2026
- **Anforderung**: Maximale Zuverlässigkeit, weltweite Reparierbarkeit, breiter Windbereich

### Segelgarderobe-Empfehlung

| Segel | Material/Schnitt | Segelmacher | Preis |
|-------|-----------------|-------------|-------|
| Großsegel (Full-Batten) | Cross-Cut Dacron (Challenge HTX) | Sanders Sails (DE) | 6.500 EUR |
| Genua 135% (Rollreff) | Cross-Cut Dacron mit UV-Band | Sanders Sails (DE) | 5.200 EUR |
| Fock 100% (Sturmvorsegel) | Cross-Cut Dacron (schwer) | Sanders Sails (DE) | 2.800 EUR |
| Sturmfock (orange) | Cross-Cut Dacron (500 g/m²) | Rolly Tasker | 1.200 EUR |
| Trysegel | Cross-Cut Dacron (500 g/m²) | Rolly Tasker | 1.500 EUR |
| Gennaker (asymmetrisch) | Radial Nylon | UK Sailmakers | 3.800 EUR |
| Code 0 | Tri-Radial Laminat | UK Sailmakers | 4.500 EUR |
| Reservegroß (einfach) | Cross-Cut Dacron | Rolly Tasker | 4.000 EUR |
| **Gesamt** | | | **29.500 EUR** |

### Begründung
- Cross-Cut Dacron für alle Primärsegel → reparierbar überall auf der Welt
- Challenge HTX Dacron → Premium-Dacron mit hoher Formstabilität
- Reservegroß → bei 3 Jahren auf See unverzichtbar
- Code 0 als einziges Laminat → Leichtwind-Performance für die Passate
- Orange Sturmfock → Sichtbarkeit (SOLAS/ISAF-konform)

### AYDI-Score
- **Langfahrt-Eignung: 94/100**
- **Regatta-Performance: 52/100**
- **Gesamtwert (Langfahrt-gewichtet): 89/100**

---

## ANHANG F — Fallstudie: Rollgroßsegel-Problematik Beneteau Oceanis 51.1

### Ausgangssituation
- **Boot**: Beneteau Oceanis 51.1 (Bj. 2021) mit In-Mast-Rollgroß
- **Problem**: Segel lässt sich schwer ausrollen, Profil ist "flach wie ein Brett", kein Vortrieb bei <10 kn

### Analyse
- In-Mast-Rollgroß: bauartbedingt kein Roach, keine Latten → ca. 25% weniger Segelfläche als Standardgroß
- Profil: Eingebaute Bauchtiefe nur 6–8% (muss flach sein zum Rollen)
- Roller-Mechanismus: Seldén Furlex Rollmast → mechanisch in Ordnung
- Vorliek-Tape: leicht verdreht → klemmt beim Ausrollen
- **AYDI-Score In-Mast-Rollgroß: 55/100** (systemimmanente Limitierung)

### Empfehlung
1. **Sofortmaßnahme**: Vorliek-Tape durch Segelmacher korrigieren → Rollfunktion verbessern
2. **Mittelfristig**: Gennaker/Code 0 anschaffen für Leichtwind-Kompensation
3. **Langfristig erwägen**: Umrüstung auf In-Boom-Furling (z.B. Leisure Furl oder Bartels) — erheblicher Aufwand (8.000–15.000 EUR + Segel)

### Kosten
- Vorliek-Korrektur: 400 EUR
- Code 0 (Quantum Fusion M): 5.200 EUR
- Facnor FX+ Furler für Code 0: 2.800 EUR
- **Gesamt: 8.400 EUR**

### Ergebnis
- Rollfunktion wiederhergestellt
- Leichtwind-Performance mit Code 0 deutlich verbessert
- In-Mast-Rollgroß bleibt systembedingt limitiert → akzeptierter Kompromiss
- **AYDI-Score nach Maßnahmen: 68/100**

---

## ANHANG G — Fallstudie: Performance-Cruiser Dehler 46 Segeltrimm

### Ausgangssituation
- **Boot**: Dehler 46 (Bj. 2022) — Performance-Cruiser mit Semi-Custom-Rigg
- **Segel**: Elvstrom EPEX Großsegel + Genua (Erstausstattung)
- **Problem**: Boot erreicht bei Regatten nur 90% der Polargeschwindigkeit. Eigner hat wenig Trimm-Erfahrung.

### AYDI Trimm-Analyse (Level 2, 3 Windstärken)

**Leichtwind (7 kn TWS, Close-Hauled):**
- Bauchtiefe: 9% → zu flach
- Bauchposition: 36% → zu weit vorn
- Twist: Zu viel → oberes Drittel leistet nichts
- Diagnosis: Cunningham und Achterstag zu straff für Leichtwind

**Mittelwind (14 kn TWS, Close-Hauled):**
- Bauchtiefe: 12% → optimal
- Bauchposition: 41% → optimal
- Twist: Korrekt
- Diagnosis: Guter Trimm — Basis-Setup passt

**Frischer Wind (20 kn TWS, Close-Hauled):**
- Bauchtiefe: 13% → zu bauchig
- Bauchposition: 48% → zu weit achtern
- Twist: Zu wenig → Boot krängt über
- Diagnosis: Cunningham nicht gesetzt, Achterstag zu locker

### Empfehlung
Trimm-Korrekturtabelle erstellt und an Steuerrad laminiert:

| TWS | Cunningham | Outhaul | Achterstag | Traveller |
|-----|-----------|---------|-----------|----------|
| 0–8 | 0 | 10 cm lose | 20% | Luv +10 |
| 8–14 | 2 cm | 5 cm lose | 50% | Mitte |
| 14–20 | 5 cm | durchgesetzt | 80% | Lee -10 |
| 20+ | max | max | 100% | Lee max |

### Ergebnis
- Nach 3 Regatten mit Trimm-Tabelle: 96% Polar erreicht
- **AYDI-Score Trimm vorher: 61/100 → nachher: 85/100**

---

## ANHANG H — Fallstudie: Klassische Yacht — Dacron-Segel Restoration

### Ausgangssituation
- **Boot**: Swan 47 (Bj. 1974, klassisch, S&S Design)
- **Segel**: Original North Sails Dacron (Bj. 2005, 20 Jahre alt!)
- **Problem**: Segel komplett ausgeformt, Bauch permanent bei 55–60%, UV-Schäden, Nähte lösen sich

### Analyse
- Tuch-Festigkeit: 40% der Nennfestigkeit (Zugtest am Muster)
- UV-Schaden: schwer (Lee-Seite weiß, Luv-Seite normal)
- Nähte: 30% der Nähte gelöst oder stark geschwächt
- Profil: nicht mehr trimmbar
- **AYDI-Score: 15/100** (Sicherheitsbedenken)

### Empfehlung
- Segel ersetzen (nicht reparierbar bei diesem Verschleißgrad)
- Cross-Cut Dacron (Challenge Marblehead) — passend zum klassischen Erscheinungsbild
- Hersteller: Sanders Sails (Deutschland) oder Ratsey & Lapthorn (UK, klassische Yachten)
- Tan-Farbe (traditionell) statt Weiß → passt zur klassischen Swan

### Umsetzung
| Position | Kosten |
|----------|--------|
| Großsegel Cross-Cut Dacron (Tan) | 5.800 EUR |
| Genua Cross-Cut Dacron (Tan) | 4.200 EUR |
| Sturmfock | 1.600 EUR |
| Vermessung und Mast-Anpassung | 400 EUR |
| **Gesamt** | **12.000 EUR** |

### Ergebnis
- Klassisches Erscheinungsbild wiederhergestellt
- Performance nahe Neuzustand (Swan 47 Polardaten)
- **AYDI-Score: 82/100**

---

## ANHANG I — AYDI-Integration: Pydantic-Modelle Segelschnitt

```python
"""AYDI Pydantic v2 Models — Sail Cut Design (16_07)"""

from __future__ import annotations
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class SailCutMethod(str, Enum):
    """Schnittmethode des Segels."""
    CROSS_CUT = "cross_cut"
    TRI_RADIAL = "tri_radial"
    RADIAL = "radial"
    MEMBRANE_3DL = "membrane_3dl"
    THREE_DI = "3di"
    STRATIS = "stratis"
    EPEX = "epex"
    FUSION_M = "fusion_m"
    FOUR_T_FORTE = "4t_forte"
    TAPE_DRIVE = "tape_drive"
    UNKNOWN = "unknown"


class SailMaterial(str, Enum):
    """Segelmaterial."""
    DACRON_STANDARD = "dacron_standard"
    DACRON_PREMIUM = "dacron_premium"
    PENTEX = "pentex"
    MYLAR_KEVLAR = "mylar_kevlar"
    MYLAR_DYNEEMA = "mylar_dyneema"
    MYLAR_CARBON = "mylar_carbon"
    DYNEEMA_COMPOSITE = "dyneema_composite"
    CARBON_COMPOSITE = "carbon_composite"
    NYLON = "nylon"
    UNKNOWN = "unknown"


class SailType(str, Enum):
    """Segeltyp."""
    MAINSAIL = "mainsail"
    GENOA = "genoa"
    JIB = "jib"
    SELF_TACKING_JIB = "self_tacking_jib"
    CODE_0 = "code_0"
    GENNAKER = "gennaker"
    SPINNAKER_SYM = "spinnaker_symmetric"
    SPINNAKER_ASYM = "spinnaker_asymmetric"
    STORM_JIB = "storm_jib"
    TRYSAIL = "trysail"
    STAYSAIL = "staysail"


class BattenType(str, Enum):
    """Lattentyp."""
    NO_BATTENS = "no_battens"
    PARTIAL_BATTENS = "partial_battens"
    FULL_BATTENS = "full_battens"
    MIXED = "mixed"


class BattenMaterial(str, Enum):
    """Latten-Material."""
    FIBERGLASS = "fiberglass"
    CARBON_HYBRID = "carbon_hybrid"
    FULL_CARBON = "full_carbon"
    FIBERGLASS_REINFORCED = "fiberglass_reinforced"


class FurlingSystem(str, Enum):
    """Reff-/Roll-System."""
    NONE = "none"
    SLAB_REEFING = "slab_reefing"
    IN_MAST_FURLING = "in_mast_furling"
    IN_BOOM_FURLING = "in_boom_furling"
    HEADSAIL_FURLING = "headsail_furling"
    CODE_SAIL_FURLING = "code_sail_furling"


class SailCutDesign(BaseModel):
    """Detaillierte Beschreibung des Segelschnitts."""

    model_config = {"from_attributes": True}

    sail_type: SailType = Field(
        ..., description="Typ des Segels"
    )
    cut_method: SailCutMethod = Field(
        ..., description="Schnittmethode"
    )
    material: SailMaterial = Field(
        ..., description="Segelmaterial"
    )
    sailmaker: Optional[str] = Field(
        None, description="Segelmacher (Hersteller)"
    )
    model_name: Optional[str] = Field(
        None, description="Modellbezeichnung des Segels"
    )
    year_built: Optional[int] = Field(
        None, ge=1960, le=2030, description="Baujahr des Segels"
    )
    luff_length_mm: Optional[float] = Field(
        None, gt=0, description="Vorliek-Länge in mm"
    )
    leech_length_mm: Optional[float] = Field(
        None, gt=0, description="Achterliek-Länge in mm"
    )
    foot_length_mm: Optional[float] = Field(
        None, gt=0, description="Unterliek-Länge in mm"
    )
    area_sqm: Optional[float] = Field(
        None, gt=0, description="Segelfläche in m²"
    )
    lp_mm: Optional[float] = Field(
        None, gt=0, description="LP (Luff Perpendicular) in mm — nur Vorsegel"
    )
    overlap_percent: Optional[float] = Field(
        None, ge=0, le=200, description="Überlappung LP/J in %"
    )
    roach_percent: Optional[float] = Field(
        None, ge=0, le=30, description="Roach in %"
    )
    batten_type: BattenType = Field(
        BattenType.PARTIAL_BATTENS, description="Lattentyp"
    )
    batten_count: Optional[int] = Field(
        None, ge=0, le=10, description="Anzahl der Latten"
    )
    batten_material: Optional[BattenMaterial] = Field(
        None, description="Latten-Material"
    )
    furling_system: FurlingSystem = Field(
        FurlingSystem.NONE, description="Reff-/Rollsystem"
    )
    cloth_weight_gsm: Optional[float] = Field(
        None, gt=0, description="Tuchgewicht in g/m²"
    )
    luff_curve_max_mm: Optional[float] = Field(
        None, ge=0, description="Maximale Vorliekkurve in mm"
    )
    design_draft_percent: Optional[float] = Field(
        None, ge=0, le=30, description="Design-Bauchtiefe in %"
    )
    design_draft_position_percent: Optional[float] = Field(
        None, ge=0, le=100, description="Design-Bauchposition in %"
    )
    uv_protection: bool = Field(
        False, description="UV-Schutzband vorhanden"
    )
    estimated_price_eur: Optional[float] = Field(
        None, ge=0, description="Geschätzter Preis in EUR"
    )
    estimated_lifespan_years: Optional[float] = Field(
        None, ge=0, description="Geschätzte Lebensdauer in Jahren"
    )
    condition_score: Optional[float] = Field(
        None, ge=0, le=100, description="Zustandsbewertung 0-100"
    )
    notes: Optional[str] = Field(
        None, description="Zusätzliche Bemerkungen"
    )
```

---

## ANHANG J — AYDI-Integration: Pydantic-Modelle Segeltrimm

```python
"""AYDI Pydantic v2 Models — Sail Trim Settings (16_07)"""

from __future__ import annotations
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class WindStrengthCategory(str, Enum):
    """Windstärke-Kategorie."""
    LIGHT = "light"           # 0-8 kn
    MEDIUM = "medium"         # 8-16 kn
    FRESH = "fresh"           # 16-25 kn
    HEAVY = "heavy"           # 25+ kn


class PointOfSail(str, Enum):
    """Kurs zum Wind."""
    CLOSE_HAULED = "close_hauled"   # TWA 30-50
    CLOSE_REACH = "close_reach"     # TWA 50-70
    BEAM_REACH = "beam_reach"       # TWA 70-100
    BROAD_REACH = "broad_reach"     # TWA 100-150
    RUN = "run"                     # TWA 150-180


class TrimSetting(str, Enum):
    """Qualitative Trimm-Einstellung."""
    MINIMUM = "minimum"
    LOOSE = "loose"
    LIGHT = "light"
    MODERATE = "moderate"
    FIRM = "firm"
    MAXIMUM = "maximum"


class MainsailTrimState(BaseModel):
    """Aktueller Trimm-Zustand des Großsegels."""

    model_config = {"from_attributes": True}

    mainsheet: TrimSetting = Field(
        ..., description="Großschot-Einstellung"
    )
    traveller_offset_mm: Optional[int] = Field(
        None, description="Traveller-Versatz von Mitte in mm (negativ=Lee)"
    )
    vang: TrimSetting = Field(
        TrimSetting.LOOSE, description="Baumniederholer"
    )
    cunningham: TrimSetting = Field(
        TrimSetting.LOOSE, description="Vorliekstrecker"
    )
    outhaul_offset_mm: Optional[int] = Field(
        None, ge=0, description="Outhaul-Versatz vom Maximum in mm (0=durchgesetzt)"
    )
    backstay: TrimSetting = Field(
        TrimSetting.MODERATE, description="Achterstag-Spannung"
    )
    reef_level: int = Field(
        0, ge=0, le=3, description="Reff-Stufe (0=kein Reff)"
    )
    batten_tension: TrimSetting = Field(
        TrimSetting.MODERATE, description="Latten-Spannung"
    )
    measured_draft_percent: Optional[float] = Field(
        None, ge=0, le=30, description="Gemessene Bauchtiefe in %"
    )
    measured_draft_position_percent: Optional[float] = Field(
        None, ge=0, le=100, description="Gemessene Bauchposition in %"
    )
    twist_description: Optional[str] = Field(
        None, description="Twist-Beschreibung (qualitativ)"
    )
    leech_telltale_streaming_percent: Optional[float] = Field(
        None, ge=0, le=100,
        description="Anteil der strömenden Achterliek-Telltales in %"
    )


class HeadsailTrimState(BaseModel):
    """Aktueller Trimm-Zustand des Vorsegels."""

    model_config = {"from_attributes": True}

    sheet_tension: TrimSetting = Field(
        ..., description="Schot-Spannung"
    )
    car_position_from_default_mm: Optional[int] = Field(
        None,
        description="Holepunkt-Versatz von Standard in mm (negativ=vorn)"
    )
    barber_hauler_inboard: TrimSetting = Field(
        TrimSetting.LOOSE, description="Barber Hauler inboard"
    )
    barber_hauler_outboard: TrimSetting = Field(
        TrimSetting.LOOSE, description="Barber Hauler outboard"
    )
    halyard: TrimSetting = Field(
        TrimSetting.MODERATE, description="Fall-Spannung"
    )
    reef_percent: float = Field(
        0.0, ge=0, le=100, description="Roll-Reff in % (0=voll, 100=komplett gerollt)"
    )
    forestay_sag_mm: Optional[float] = Field(
        None, ge=0, description="Gemessener Vorstag-Durchhang in mm"
    )
    luff_telltales_balanced: Optional[bool] = Field(
        None, description="Vorliek-Telltales ausbalanciert (Luv+Lee horizontal)"
    )


class SailTrimSnapshot(BaseModel):
    """Vollständiger Trimm-Snapshot zu einem Zeitpunkt."""

    model_config = {"from_attributes": True}

    timestamp: Optional[str] = Field(
        None, description="Zeitstempel ISO 8601"
    )
    tws_kn: float = Field(
        ..., ge=0, le=80, description="True Wind Speed in Knoten"
    )
    twa_deg: float = Field(
        ..., ge=0, le=180, description="True Wind Angle in Grad"
    )
    wind_category: WindStrengthCategory = Field(
        ..., description="Windstärke-Kategorie"
    )
    point_of_sail: PointOfSail = Field(
        ..., description="Kurs zum Wind"
    )
    boat_speed_kn: Optional[float] = Field(
        None, ge=0, description="Bootsgeschwindigkeit in Knoten"
    )
    heel_angle_deg: Optional[float] = Field(
        None, ge=0, le=60, description="Krängungswinkel in Grad"
    )
    mainsail_trim: Optional[MainsailTrimState] = Field(
        None, description="Großsegel-Trimm"
    )
    headsail_trim: Optional[HeadsailTrimState] = Field(
        None, description="Vorsegel-Trimm"
    )
    vmg_kn: Optional[float] = Field(
        None, description="Velocity Made Good in Knoten"
    )
    polar_percent: Optional[float] = Field(
        None, ge=0, le=150, description="Performance in % der Polardaten"
    )
    notes: Optional[str] = Field(
        None, description="Trimm-Notizen"
    )
    confidence: str = Field(
        "estimated", description="Confidence Level des Snapshots"
    )
```

---

## ANHANG K — AYDI-Integration: Pydantic-Modelle Fehlerbild

```python
"""AYDI Pydantic v2 Models — Sail Defect Patterns (16_07)"""

from __future__ import annotations
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class SailDefectCode(str, Enum):
    """Fehlerbild-Codes für Segelschnitt und Trimm."""
    EXCESSIVE_DRAFT = "F-16_07-01"
    INSUFFICIENT_DRAFT = "F-16_07-02"
    WRONG_DRAFT_POSITION = "F-16_07-03"
    EXCESSIVE_TWIST = "F-16_07-04"
    LEECH_HOOK = "F-16_07-05"
    LUFF_FLUTTER = "F-16_07-06"
    AGE_DISTORTION = "F-16_07-07"
    UNBALANCED_SAIL_PLAN = "F-16_07-08"
    LIGHT_WIND_PERFORMANCE = "F-16_07-09"
    EXCESSIVE_HEEL = "F-16_07-10"
    FLOGGING_DAMAGE = "F-16_07-11"
    LAMINAR_SEPARATION = "F-16_07-12"


class SailDefectSeverity(str, Enum):
    """Schweregrad des Fehlerbilds."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class SailDefectFinding(BaseModel):
    """Einzelnes Fehlerbild-Ergebnis."""

    model_config = {"from_attributes": True}

    defect_code: SailDefectCode = Field(
        ..., description="Fehlerbild-Code"
    )
    severity: SailDefectSeverity = Field(
        ..., description="Schweregrad"
    )
    sail_affected: str = Field(
        ..., description="Betroffenes Segel (z.B. 'Großsegel', 'Genua')"
    )
    description_de: str = Field(
        ..., description="Beschreibung des Fehlerbilds (Deutsch)"
    )
    location_on_sail: Optional[str] = Field(
        None, description="Position auf dem Segel (z.B. 'oberes Drittel Achterliek')"
    )
    visual_indicators: list[str] = Field(
        default_factory=list,
        description="Visuelle Erkennungsmerkmale"
    )
    probable_causes: list[str] = Field(
        default_factory=list,
        description="Wahrscheinliche Ursachen"
    )
    corrective_actions: list[str] = Field(
        default_factory=list,
        description="Empfohlene Korrekturmaßnahmen"
    )
    estimated_repair_cost_eur: Optional[float] = Field(
        None, ge=0, description="Geschätzte Reparaturkosten in EUR"
    )
    requires_sailmaker: bool = Field(
        False, description="Erfordert Segelmacher-Intervention"
    )
    confidence: str = Field(
        "visual_medium",
        description="Confidence Level der Erkennung"
    )
    notes: Optional[str] = Field(
        None, description="Zusätzliche Bemerkungen"
    )


class SailDefectReport(BaseModel):
    """Gesamter Fehlerbild-Bericht für ein Segel-Setup."""

    model_config = {"from_attributes": True}

    boat_name: Optional[str] = Field(None, description="Bootsname")
    boat_type: Optional[str] = Field(None, description="Bootstyp")
    analysis_date: Optional[str] = Field(None, description="Analyse-Datum ISO 8601")
    findings: list[SailDefectFinding] = Field(
        default_factory=list,
        description="Liste der Fehlerbilder"
    )
    overall_sail_score: Optional[float] = Field(
        None, ge=0, le=100, description="Gesamt-Segel-Score 0-100"
    )
    overall_trim_score: Optional[float] = Field(
        None, ge=0, le=100, description="Gesamt-Trimm-Score 0-100"
    )
    recommendations_de: list[str] = Field(
        default_factory=list,
        description="Allgemeine Empfehlungen (Deutsch)"
    )
    confidence: str = Field(
        "estimated", description="Gesamt-Confidence Level"
    )
```

---

## ANHANG L — AYDI-Integration: Bewertungsschema

```python
"""AYDI Pydantic v2 Models — Sail Scoring Schema (16_07)"""

from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SailCutScore(BaseModel):
    """Bewertung des Segelschnitts."""

    model_config = {"from_attributes": True}

    material_quality: float = Field(
        ..., ge=0, le=100,
        description="Material-Qualität (Tuch, Nähte, Verstärkungen)"
    )
    cut_method_suitability: float = Field(
        ..., ge=0, le=100,
        description="Eignung der Schnittmethode für den Einsatzzweck"
    )
    form_stability: float = Field(
        ..., ge=0, le=100,
        description="Formstabilität (Wie gut hält das Segel seine Form über Zeit)"
    )
    batten_system: float = Field(
        ..., ge=0, le=100,
        description="Latten-System (Typ, Material, Einstellung)"
    )
    furling_compatibility: float = Field(
        ..., ge=0, le=100,
        description="Kompatibilität mit Reff-/Rollsystem"
    )
    repairability: float = Field(
        ..., ge=0, le=100,
        description="Reparierbarkeit (Material, Verfügbarkeit, Kosten)"
    )
    uv_protection: float = Field(
        ..., ge=0, le=100,
        description="UV-Schutz (Band, Material-Eignung)"
    )
    price_performance: float = Field(
        ..., ge=0, le=100,
        description="Preis-Leistungs-Verhältnis"
    )
    overall_cut_score: Optional[float] = Field(
        None, ge=0, le=100,
        description="Gesamt-Score Segelschnitt (gewichteter Mittelwert)"
    )
    confidence: str = Field(
        "estimated", description="Confidence Level"
    )

    def calculate_overall(self) -> float:
        """Berechnet den gewichteten Gesamtscore."""
        weights = {
            "material_quality": 0.20,
            "cut_method_suitability": 0.20,
            "form_stability": 0.20,
            "batten_system": 0.10,
            "furling_compatibility": 0.10,
            "repairability": 0.08,
            "uv_protection": 0.05,
            "price_performance": 0.07,
        }
        total = sum(
            getattr(self, attr) * weight
            for attr, weight in weights.items()
        )
        self.overall_cut_score = round(total, 1)
        return self.overall_cut_score


class SailTrimScore(BaseModel):
    """Bewertung des Segeltrimms."""

    model_config = {"from_attributes": True}

    draft_depth_accuracy: float = Field(
        ..., ge=0, le=100,
        description="Bauchtiefe optimal für Bedingungen"
    )
    draft_position_accuracy: float = Field(
        ..., ge=0, le=100,
        description="Bauchposition optimal für Bedingungen"
    )
    twist_control: float = Field(
        ..., ge=0, le=100,
        description="Twist-Einstellung korrekt"
    )
    leech_tension: float = Field(
        ..., ge=0, le=100,
        description="Achterliek-Spannung korrekt"
    )
    slot_optimization: float = Field(
        ..., ge=0, le=100,
        description="Slot-Breite zwischen Vorsegel und Großsegel optimal"
    )
    sail_plan_balance: float = Field(
        ..., ge=0, le=100,
        description="Segelplan-Balance (CE vs CLR)"
    )
    depower_execution: float = Field(
        ..., ge=0, le=100,
        description="Depowering-Maßnahmen korrekt ausgeführt"
    )
    overall_trim_score: Optional[float] = Field(
        None, ge=0, le=100,
        description="Gesamt-Score Trimm (gewichteter Mittelwert)"
    )
    confidence: str = Field(
        "estimated", description="Confidence Level"
    )

    def calculate_overall(self) -> float:
        """Berechnet den gewichteten Gesamtscore."""
        weights = {
            "draft_depth_accuracy": 0.20,
            "draft_position_accuracy": 0.15,
            "twist_control": 0.20,
            "leech_tension": 0.15,
            "slot_optimization": 0.10,
            "sail_plan_balance": 0.10,
            "depower_execution": 0.10,
        }
        total = sum(
            getattr(self, attr) * weight
            for attr, weight in weights.items()
        )
        self.overall_trim_score = round(total, 1)
        return self.overall_trim_score
```

---

## ANHANG M — AYDI-Integration: Trimm-Empfehlungsengine

```python
"""AYDI Pydantic v2 Models — Sail Trim Recommendation Engine (16_07)"""

from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TrimRecommendation(BaseModel):
    """Einzelne Trimm-Empfehlung."""

    model_config = {"from_attributes": True}

    parameter: str = Field(
        ..., description="Trimm-Parameter (z.B. 'cunningham', 'outhaul')"
    )
    current_setting_de: str = Field(
        ..., description="Aktuelle Einstellung (Deutsch)"
    )
    recommended_setting_de: str = Field(
        ..., description="Empfohlene Einstellung (Deutsch)"
    )
    reason_de: str = Field(
        ..., description="Begründung (Deutsch)"
    )
    priority: int = Field(
        ..., ge=1, le=5, description="Priorität (1=höchste)"
    )
    expected_improvement_de: str = Field(
        ..., description="Erwartete Verbesserung (Deutsch)"
    )


class TrimRecommendationSet(BaseModel):
    """Vollständiger Satz Trimm-Empfehlungen."""

    model_config = {"from_attributes": True}

    wind_speed_kn: float = Field(
        ..., ge=0, description="Windgeschwindigkeit in Knoten"
    )
    wind_angle_deg: float = Field(
        ..., ge=0, le=180, description="Windwinkel in Grad"
    )
    boat_type: Optional[str] = Field(
        None, description="Bootstyp"
    )
    boat_length_m: Optional[float] = Field(
        None, ge=5, le=30, description="Bootslänge in Metern"
    )
    mainsail_recommendations: list[TrimRecommendation] = Field(
        default_factory=list,
        description="Großsegel-Empfehlungen"
    )
    headsail_recommendations: list[TrimRecommendation] = Field(
        default_factory=list,
        description="Vorsegel-Empfehlungen"
    )
    general_recommendations_de: list[str] = Field(
        default_factory=list,
        description="Allgemeine Empfehlungen (Deutsch)"
    )
    should_reef: bool = Field(
        False, description="Sollte gerefft werden"
    )
    reef_recommendation_de: Optional[str] = Field(
        None, description="Reff-Empfehlung (Deutsch)"
    )
    safety_warnings_de: list[str] = Field(
        default_factory=list,
        description="Sicherheitswarnungen (Deutsch)"
    )
    confidence: str = Field(
        "estimated", description="Confidence Level"
    )
```

---

## ANHANG N — AYDI-Integration: Visueller Segelanalyse-Prompt

```python
"""AYDI Pydantic v2 Models — Visual Sail Analysis Prompt (16_07)"""

from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


SAIL_VISUAL_ANALYSIS_PROMPT_DE = """
Du bist ein erfahrener Segelmacher und Segeltrimmexperte. Analysiere das
bereitgestellte Foto eines Segels/Segelplans und bewerte folgende Aspekte:

## Pflichtfelder (immer bewerten, wenn sichtbar):

1. **Schnittmethode**: Cross-Cut, Tri-Radial, Radial, Membran/3Di/Stratis?
   - Erkennbar an Nahtmuster und Paneelverlauf

2. **Bauchtiefe (Draft)**: Schätze die Profiltiefe in %
   - Flach (<8%), Moderat (8-12%), Bauchig (12-16%), Übermäßig (>16%)

3. **Bauchposition**: Wo befindet sich der tiefste Punkt?
   - Vorn (30-38%), Mitte (38-45%), Achtern (45-55%)

4. **Twist**: Ist die Verdrehung von unten nach oben angemessen?
   - Zu wenig / Korrekt / Zu viel

5. **Achterliek**: Gerade / Leicht offen / Hook (nach Luv) / Zu offen

6. **Segel-Zustand**: Neu / Gut / Gealtert / Schlecht
   - Achte auf: Falten, Verfärbungen, UV-Schäden, lose Nähte

7. **Latten**: Typ und Zustand (wenn sichtbar)

8. **Fehlerbild**: Identifiziere Fehlerbilder F-16_07-01 bis F-16_07-12

## Antwortformat:

Für jeden bewerteten Aspekt gib an:
- Bewertung (numerisch oder Kategorie)
- Confidence: visual_high / visual_medium / visual_low / visual_insufficient
- Begründung (1-2 Sätze)

Wenn ein Aspekt nicht beurteilbar ist, antworte: "nicht beurteilbar" mit
Begründung.

Verwende IMMER Deutsch für die Beschreibung.
"""


class VisualSailAnalysisConfig(BaseModel):
    """Konfiguration für visuelle Segelanalyse."""

    model_config = {"from_attributes": True}

    prompt_template: str = Field(
        default=SAIL_VISUAL_ANALYSIS_PROMPT_DE,
        description="Prompt-Template für Claude Vision"
    )
    min_confidence_display: str = Field(
        "visual_medium",
        description="Minimales Confidence-Level für Anzeige"
    )
    enable_defect_detection: bool = Field(
        True, description="Fehlerbild-Erkennung aktivieren"
    )
    enable_trim_analysis: bool = Field(
        True, description="Trimm-Analyse aktivieren"
    )
    enable_cut_identification: bool = Field(
        True, description="Schnittmethoden-Erkennung aktivieren"
    )
    max_defects_per_image: int = Field(
        5, ge=1, le=12, description="Max. Fehlerbilder pro Bild"
    )


class VisualSailAnalysisResult(BaseModel):
    """Ergebnis der visuellen Segelanalyse."""

    model_config = {"from_attributes": True}

    image_id: str = Field(
        ..., description="ID des analysierten Bildes"
    )
    detected_cut_method: Optional[str] = Field(
        None, description="Erkannte Schnittmethode"
    )
    detected_cut_confidence: str = Field(
        "visual_insufficient",
        description="Confidence der Schnittmethoden-Erkennung"
    )
    estimated_draft_percent: Optional[float] = Field(
        None, ge=0, le=30, description="Geschätzte Bauchtiefe in %"
    )
    estimated_draft_position_percent: Optional[float] = Field(
        None, ge=0, le=100, description="Geschätzte Bauchposition in %"
    )
    twist_assessment_de: Optional[str] = Field(
        None, description="Twist-Bewertung (Deutsch)"
    )
    leech_assessment_de: Optional[str] = Field(
        None, description="Achterliek-Bewertung (Deutsch)"
    )
    condition_assessment_de: Optional[str] = Field(
        None, description="Zustandsbewertung (Deutsch)"
    )
    condition_score: Optional[float] = Field(
        None, ge=0, le=100, description="Zustandsscore 0-100"
    )
    defect_codes: list[str] = Field(
        default_factory=list,
        description="Erkannte Fehlerbild-Codes"
    )
    analysis_text_de: Optional[str] = Field(
        None, description="Volltext-Analyse (Deutsch)"
    )
    confidence: str = Field(
        "visual_medium", description="Gesamt-Confidence"
    )
```

---

## ANHANG O — AYDI-Integration: Segelverschleiß-Scoring

```python
"""AYDI Pydantic v2 Models — Sail Wear Scoring (16_07)"""

from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SailWearAssessment(BaseModel):
    """Bewertung des Segel-Verschleißzustands."""

    model_config = {"from_attributes": True}

    sail_type: str = Field(
        ..., description="Segeltyp"
    )
    sail_age_years: Optional[float] = Field(
        None, ge=0, description="Alter in Jahren"
    )
    estimated_sailing_hours: Optional[float] = Field(
        None, ge=0, description="Geschätzte Segelstunden"
    )

    # Einzelbewertungen
    cloth_strength_percent: Optional[float] = Field(
        None, ge=0, le=100,
        description="Restfestigkeit des Tuchs in % (100=neu)"
    )
    seam_integrity_score: float = Field(
        ..., ge=0, le=100,
        description="Naht-Integrität (100=perfekt, 0=alle gelöst)"
    )
    uv_damage_score: float = Field(
        ..., ge=0, le=100,
        description="UV-Schaden-Bewertung (100=kein Schaden, 0=schwer)"
    )
    shape_retention_score: float = Field(
        ..., ge=0, le=100,
        description="Formhaltung (100=wie neu, 0=komplett verformt)"
    )
    hardware_condition_score: float = Field(
        ..., ge=0, le=100,
        description="Beschläge-Zustand (Kauschen, Patches, Latten)"
    )
    chafe_damage_score: float = Field(
        ..., ge=0, le=100,
        description="Scheuerschäden (100=keine, 0=schwer)"
    )

    # Berechnete Werte
    overall_wear_score: Optional[float] = Field(
        None, ge=0, le=100,
        description="Gesamt-Verschleiß-Score (100=neuwertig)"
    )
    estimated_remaining_life_years: Optional[float] = Field(
        None, ge=0,
        description="Geschätzte Restlebensdauer in Jahren"
    )
    replacement_urgency_de: Optional[str] = Field(
        None,
        description="Ersatz-Dringlichkeit: 'nicht nötig', 'mittelfristig planen', 'bald ersetzen', 'sofort ersetzen'"
    )
    confidence: str = Field(
        "estimated", description="Confidence Level"
    )

    def calculate_overall(self) -> float:
        """Berechnet den gewichteten Gesamt-Verschleiß-Score."""
        weights = {
            "seam_integrity_score": 0.25,
            "uv_damage_score": 0.15,
            "shape_retention_score": 0.30,
            "hardware_condition_score": 0.10,
            "chafe_damage_score": 0.20,
        }
        total = sum(
            getattr(self, attr) * weight
            for attr, weight in weights.items()
        )
        if self.cloth_strength_percent is not None:
            total = total * 0.7 + self.cloth_strength_percent * 0.3
        self.overall_wear_score = round(total, 1)
        return self.overall_wear_score
```

---

## ANHANG P — AYDI-Integration: Confidence-Mapping Segel

```python
"""AYDI Pydantic v2 Models — Confidence Mapping for Sails (16_07)"""

from __future__ import annotations
from pydantic import BaseModel, Field


class SailConfidenceMapping(BaseModel):
    """Confidence-Zuordnung für verschiedene Segel-Analyse-Parameter."""

    model_config = {"from_attributes": True}

    # Schnittmethode
    cut_method_from_photo: str = Field(
        "visual_medium",
        description="Schnittmethode aus Foto erkannt"
    )
    cut_method_from_sailmaker_docs: str = Field(
        "documented",
        description="Schnittmethode aus Segelmacher-Dokumentation"
    )

    # Bauchtiefe
    draft_from_stripe_analysis: str = Field(
        "measured",
        description="Bauchtiefe aus professioneller Streifen-Analyse"
    )
    draft_from_photo: str = Field(
        "visual_medium",
        description="Bauchtiefe aus normalem Foto geschätzt"
    )
    draft_from_app: str = Field(
        "visual_high",
        description="Bauchtiefe aus spezialisierter App (SailTrim etc.)"
    )

    # Materialzustand
    material_condition_from_photo: str = Field(
        "visual_medium",
        description="Materialzustand aus Foto"
    )
    material_condition_from_inspection: str = Field(
        "measured",
        description="Materialzustand aus physischer Inspektion"
    )

    # Trimm-Bewertung
    trim_from_photo: str = Field(
        "visual_medium",
        description="Trimm-Bewertung aus Segelfoto"
    )
    trim_from_instruments: str = Field(
        "measured",
        description="Trimm-Bewertung aus Bord-Instrumenten"
    )
    trim_from_polar_comparison: str = Field(
        "calculated",
        description="Trimm-Bewertung aus Polar-Vergleich"
    )

    # Fehlerbild-Erkennung
    defect_from_clear_photo: str = Field(
        "visual_high",
        description="Fehlerbild aus klarem Foto (z.B. Achterliek-Hook)"
    )
    defect_from_ambiguous_photo: str = Field(
        "visual_low",
        description="Fehlerbild aus undeutlichem Foto"
    )
    defect_from_sailmaker_report: str = Field(
        "documented",
        description="Fehlerbild aus Segelmacher-Bericht"
    )

    # Preis-Schätzungen
    price_from_quote: str = Field(
        "measured",
        description="Preis aus Angebot/Rechnung"
    )
    price_from_market_data: str = Field(
        "estimated",
        description="Preis aus Marktdaten/Erfahrungswerten"
    )
    price_from_benchmark: str = Field(
        "benchmark",
        description="Preis aus Branchenbenchmarks"
    )
```

---

## ANHANG Q — AYDI-Integration: Troubleshooting-Entscheidungsbaum

```python
"""AYDI Pydantic v2 Models — Sail Troubleshooting Decision Tree (16_07)"""

from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TroubleshootingNode(BaseModel):
    """Ein Knoten im Troubleshooting-Entscheidungsbaum."""

    model_config = {"from_attributes": True}

    node_id: str = Field(
        ..., description="Eindeutige Knoten-ID"
    )
    question_de: str = Field(
        ..., description="Frage an den Benutzer (Deutsch)"
    )
    yes_next_node: Optional[str] = Field(
        None, description="Nächster Knoten bei 'Ja'"
    )
    no_next_node: Optional[str] = Field(
        None, description="Nächster Knoten bei 'Nein'"
    )
    is_solution: bool = Field(
        False, description="Ist dies ein Lösungsknoten?"
    )
    solution_de: Optional[str] = Field(
        None, description="Lösung (Deutsch), falls Lösungsknoten"
    )
    related_defect_codes: list[str] = Field(
        default_factory=list,
        description="Zugehörige Fehlerbild-Codes"
    )
    priority: int = Field(
        3, ge=1, le=5, description="Dringlichkeit (1=höchste)"
    )


class TroubleshootingTree(BaseModel):
    """Vollständiger Troubleshooting-Baum für ein Symptom."""

    model_config = {"from_attributes": True}

    tree_id: str = Field(
        ..., description="Baum-ID (z.B. 'keine_hoehe')"
    )
    symptom_de: str = Field(
        ..., description="Ausgangs-Symptom (Deutsch)"
    )
    root_node_id: str = Field(
        ..., description="ID des Wurzel-Knotens"
    )
    nodes: list[TroubleshootingNode] = Field(
        default_factory=list,
        description="Alle Knoten des Baums"
    )


# Vordefinierte Bäume
TROUBLESHOOTING_TREES = [
    {
        "tree_id": "keine_hoehe",
        "symptom_de": "Boot macht keine Höhe am Wind",
        "root_node_id": "kh_01",
    },
    {
        "tree_id": "zu_viel_kraengung",
        "symptom_de": "Boot krängt übermäßig",
        "root_node_id": "zk_01",
    },
    {
        "tree_id": "vorliek_flutter",
        "symptom_de": "Segel flattert am Vorliek",
        "root_node_id": "vf_01",
    },
    {
        "tree_id": "ruderdruck",
        "symptom_de": "Übermäßiger Ruderdruck",
        "root_node_id": "rd_01",
    },
    {
        "tree_id": "unter_polar",
        "symptom_de": "Performance unter Polardaten",
        "root_node_id": "up_01",
    },
]
```

---

## ANHANG R — AYDI-Integration: Schnittmethoden-Vergleichsmodell

```python
"""AYDI Pydantic v2 Models — Sail Cut Comparison (16_07)"""

from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CutMethodProfile(BaseModel):
    """Profil einer Schnittmethode für Vergleiche."""

    model_config = {"from_attributes": True}

    method_name: str = Field(
        ..., description="Name der Schnittmethode"
    )
    method_code: str = Field(
        ..., description="Methodencode (z.B. 'cross_cut')"
    )

    # Bewertungen (0-100)
    form_stability: float = Field(
        ..., ge=0, le=100,
        description="Formstabilität über die Lebensdauer"
    )
    light_wind_performance: float = Field(
        ..., ge=0, le=100,
        description="Leichtwind-Performance"
    )
    heavy_wind_performance: float = Field(
        ..., ge=0, le=100,
        description="Starkwind-Performance"
    )
    durability: float = Field(
        ..., ge=0, le=100,
        description="Langlebigkeit"
    )
    repairability: float = Field(
        ..., ge=0, le=100,
        description="Reparierbarkeit"
    )
    uv_resistance: float = Field(
        ..., ge=0, le=100,
        description="UV-Beständigkeit"
    )
    fold_tolerance: float = Field(
        ..., ge=0, le=100,
        description="Toleranz gegenüber Falten/Knicken"
    )
    price_performance: float = Field(
        ..., ge=0, le=100,
        description="Preis-Leistung"
    )
    weight: float = Field(
        ..., ge=0, le=100,
        description="Leichtigkeit (100=sehr leicht)"
    )
    furling_suitability: float = Field(
        ..., ge=0, le=100,
        description="Eignung für Rollsysteme"
    )

    # Preis-Referenz
    price_factor: float = Field(
        ..., ge=0.5, le=5.0,
        description="Preisfaktor relativ zu Cross-Cut Dacron (=1.0)"
    )
    typical_lifespan_cruising_years: float = Field(
        ..., ge=1, le=20,
        description="Typische Lebensdauer Fahrt (Jahre)"
    )
    typical_lifespan_racing_years: float = Field(
        ..., ge=1, le=15,
        description="Typische Lebensdauer Regatta (Jahre)"
    )

    # Empfehlungs-Texte
    best_for_de: str = Field(
        ..., description="Am besten geeignet für (Deutsch)"
    )
    not_recommended_for_de: str = Field(
        ..., description="Nicht empfohlen für (Deutsch)"
    )


# Vordefinierte Profile
CUT_METHOD_PROFILES = {
    "cross_cut": {
        "method_name": "Cross-Cut (Horizontalschnitt)",
        "method_code": "cross_cut",
        "form_stability": 55,
        "light_wind_performance": 60,
        "heavy_wind_performance": 55,
        "durability": 85,
        "repairability": 95,
        "uv_resistance": 80,
        "fold_tolerance": 90,
        "price_performance": 95,
        "weight": 50,
        "furling_suitability": 90,
        "price_factor": 1.0,
        "typical_lifespan_cruising_years": 9,
        "typical_lifespan_racing_years": 4,
        "best_for_de": "Fahrtensegel, Blauwasser, Rollsegel, Budget",
        "not_recommended_for_de": "Hochleistungsregatta",
    },
    "tri_radial": {
        "method_name": "Tri-Radial (Dreizonen-Radialschnitt)",
        "method_code": "tri_radial",
        "form_stability": 72,
        "light_wind_performance": 72,
        "heavy_wind_performance": 70,
        "durability": 75,
        "repairability": 80,
        "uv_resistance": 75,
        "fold_tolerance": 75,
        "price_performance": 78,
        "weight": 60,
        "furling_suitability": 75,
        "price_factor": 1.6,
        "typical_lifespan_cruising_years": 7,
        "typical_lifespan_racing_years": 3,
        "best_for_de": "Performance-Cruiser, Club-Regatta",
        "not_recommended_for_de": "Budget-Fahrtensegel, In-Mast-Rollgroß",
    },
    "3di": {
        "method_name": "North Sails 3Di",
        "method_code": "3di",
        "form_stability": 95,
        "light_wind_performance": 92,
        "heavy_wind_performance": 95,
        "durability": 78,
        "repairability": 40,
        "uv_resistance": 65,
        "fold_tolerance": 60,
        "price_performance": 45,
        "weight": 90,
        "furling_suitability": 55,
        "price_factor": 3.5,
        "typical_lifespan_cruising_years": 8,
        "typical_lifespan_racing_years": 4,
        "best_for_de": "Performance-Cruiser, Offshore-Regatta, Grand Prix",
        "not_recommended_for_de": "Budget, Blauwasser ohne Segelmacher-Zugang",
    },
    "stratis": {
        "method_name": "Doyle Stratis",
        "method_code": "stratis",
        "form_stability": 90,
        "light_wind_performance": 88,
        "heavy_wind_performance": 90,
        "durability": 75,
        "repairability": 55,
        "uv_resistance": 65,
        "fold_tolerance": 55,
        "price_performance": 55,
        "weight": 85,
        "furling_suitability": 50,
        "price_factor": 3.0,
        "typical_lifespan_cruising_years": 7,
        "typical_lifespan_racing_years": 4,
        "best_for_de": "Performance-Cruiser, Club-Regatta, Offshore",
        "not_recommended_for_de": "Budget, In-Mast-Rollgroß",
    },
    "epex": {
        "method_name": "Elvstrom EPEX",
        "method_code": "epex",
        "form_stability": 78,
        "light_wind_performance": 76,
        "heavy_wind_performance": 78,
        "durability": 72,
        "repairability": 70,
        "uv_resistance": 70,
        "fold_tolerance": 65,
        "price_performance": 72,
        "weight": 68,
        "furling_suitability": 60,
        "price_factor": 2.0,
        "typical_lifespan_cruising_years": 7,
        "typical_lifespan_racing_years": 3,
        "best_for_de": "Performance-Cruiser (Preis-Leistung)",
        "not_recommended_for_de": "Grand Prix Regatta",
    },
}


class CutMethodComparison(BaseModel):
    """Vergleich zweier oder mehrerer Schnittmethoden."""

    model_config = {"from_attributes": True}

    boat_type: Optional[str] = Field(
        None, description="Bootstyp für kontextbezogenen Vergleich"
    )
    boat_length_m: Optional[float] = Field(
        None, ge=5, le=30, description="Bootslänge in Metern"
    )
    primary_use: Optional[str] = Field(
        None, description="Haupteinsatz (z.B. 'fahrt', 'regatta', 'blauwasser')"
    )
    methods_compared: list[CutMethodProfile] = Field(
        default_factory=list,
        description="Verglichene Schnittmethoden"
    )
    recommendation_de: Optional[str] = Field(
        None, description="AYDI-Empfehlung (Deutsch)"
    )
    recommendation_reasoning_de: Optional[str] = Field(
        None, description="Begründung der Empfehlung (Deutsch)"
    )
    confidence: str = Field(
        "estimated", description="Confidence Level"
    )
```

---

> **Ende der Wissensdatei 16_07 — Segelschnitt und Trimm**
> AYDI Maritime Knowledge Base v2.0 — 2026-04
> Confidence-Quellen: measured, documented, estimated (siehe Einzelangaben)
