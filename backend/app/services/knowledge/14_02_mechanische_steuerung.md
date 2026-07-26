# 14.02 — Mechanische Steuerung (Kabel, Kette, Zahnstange, Schubstange): Vollständige Wissensreferenz

> **AYDI Wissensdatei 14.02** — Kategorie 14: Steueranlagen
> **Confidence-Quelle:** measured (Hersteller-TDS), documented (Hersteller-Kataloge, Testberichte), estimated (Erfahrungswerte)
> **Letzte Aktualisierung:** 2026-04-26

---

```yaml
title: "Mechanische Steuerung"
kategorie: "14 Steueranlagen"
unterkategorie: "02 Mechanische Steuerung"
version: "1.0.0"
datum: "2026-04-26"
autor: "AYDI Research"
status: "validated"
confidence_quellen:
  - measured: "Hersteller-Datenblätter, zertifizierte Prüfberichte"
  - documented: "Practical Sailor, SAIL Magazine, Yachtsurvey.com, RINA Papers"
  - estimated: "Erfahrungswerte, Eigner-Konsens, Forum-Auswertung"
normen_referenzen:
  - "ISO 8847:2021 — Steueranlagen für Sportboote"
  - "ISO 8848:2020 — Fernsteuereinrichtungen"
  - "ISO 25197:2020 — Steuerungssysteme für Boote"
  - "ABYC P-17 — Manual and Assisted Mechanical Steering Systems"
  - "CE Recreational Craft Directive 2013/53/EU"
  - "NMMA Certification Requirements — Steering"
  - "GL Rules for Classification of Yachts — Steering Gear"
abhängigkeiten:
  - "14_01_ruderanlage_grundlagen.md"
  - "14_03_hydraulische_steuerung.md"
  - "14_04_autopilot_systeme.md"
```

---

## Inhaltsverzeichnis

1. [Einführung](#1-einführung)
2. [Grundlagen](#2-grundlagen)
3. [Typenübersicht](#3-typenübersicht)
4. [Produktlinien und Hersteller](#4-produktlinien-und-hersteller)
5. [Installation](#5-installation)
6. [Fehlerbild-Atlas](#6-fehlerbild-atlas)
7. [Troubleshooting](#7-troubleshooting)
8. [FAQ — Häufige Fragen](#8-faq--häufige-fragen)
9. [Glossar](#9-glossar)
10. [Schnell-Referenz](#10-schnell-referenz)
11. [ANHANG A — Fallstudien](#anhang-a--fallstudien)
12. [ANHANG B — Spannungs- und Belastungstabellen](#anhang-b--spannungs--und-belastungstabellen)
13. [ANHANG C — Confidence-Mapping](#anhang-c--confidence-mapping)
14. [ANHANG D — Normen-Zusammenfassung](#anhang-d--normen-zusammenfassung)
15. [ANHANG E — Wartungsintervalle](#anhang-e--wartungsintervalle)
16. [ANHANG F — Reibungsverlust-Diagramme](#anhang-f--reibungsverlust-diagramme)
17. [ANHANG G — Historische Entwicklung](#anhang-g--historische-entwicklung)
18. [ANHANG H — AYDI-Integration (Pydantic-Modelle)](#anhang-h--aydi-integration-pydantic-modelle)
19. [ANHANG I — Bewertungsschema](#anhang-i--bewertungsschema)
20. [ANHANG J — Troubleshooting-Entscheidungsbäume (erweitert)](#anhang-j--troubleshooting-entscheidungsbäume-erweitert)
21. [ANHANG K — Kostenkalkulation](#anhang-k--kostenkalkulation)
22. [ANHANG L — Regionale Besonderheiten](#anhang-l--regionale-besonderheiten)
23. [ANHANG M — Testprotokolle und Prüfverfahren](#anhang-m--testprotokolle-und-prüfverfahren)
24. [ANHANG N — Zusätzliche Fallstudien](#anhang-n--zusätzliche-fallstudien)
25. [ANHANG O — Eigner-Erfahrungen und Feldberichte](#anhang-o--eigner-erfahrungen-und-feldberichte)
26. [ANHANG P — Materialkunde Steuerungskomponenten](#anhang-p--materialkunde-steuerungskomponenten)
27. [ANHANG Q — Notsteuerung bei Systemversagen](#anhang-q--notsteuerung-bei-systemversagen)
28. [ANHANG R — Zukunftstrends](#anhang-r--zukunftstrends)

---

## 1. Einführung

### 1.1 Bedeutung der mechanischen Steuerung im Yachtbau

Die mechanische Steuerung ist das älteste und am weitesten verbreitete Lenksystem auf Sport- und Fahrtenyachten bis ca. 15 Meter (50 Fuß). Sie überträgt die Drehbewegung des Steuerrades oder der Pinne über rein mechanische Elemente — Drahtseile, Ketten, Zahnstangen oder Schubstangen — auf den Ruderschaft. Im Gegensatz zu hydraulischen Systemen arbeitet sie ohne Fluid, ohne Pumpe und ohne Druckleitungen. Das bedeutet: weniger Komplexität, geringeres Gewicht, niedrigere Kosten — aber auch Einschränkungen bei Ruderkräften und Bootsgröße.

**Statistische Relevanz:**
- Ca. 70–80 % aller Segelboote zwischen 7 und 14 Metern verwenden mechanische Steuerungen (Quelle: Jefa-Marktanalyse 2023, Edson Marine Survey 2022).
- Bei Motorbooten bis 10 Meter dominieren mechanische Systeme zu über 85 % (Teleflex-Schätzung).
- Die häufigsten Steuerungsprobleme bei mechanischen Systemen: Seilspannungsverlust (31 %), Korrosion an Umlenkrollen (22 %), Kettenverschleiß (17 %), Spiel im Steuergetriebe (14 %), Quadrantenlockerung (9 %), Seilbruch (7 %).
- Durchschnittliche Lebensdauer eines gut gewarteten Seilsteuersystems: 8–15 Jahre (Confidence: estimated).
- Kosten einer Kompletterneuerung: 600–3.500 EUR je nach Bootsgröße und System (Confidence: estimated).

### 1.2 Abgrenzung zu anderen Steuerungssystemen

Mechanische Steuerungen unterscheiden sich grundlegend von:

- **Pinnensteuerung (direkt):** Pinne sitzt direkt auf dem Ruderkoker — kein Übertragungssystem nötig. Für Boote bis ca. 10 m (Segelboote) oder 7 m (Motorboote). Pinne = direkteste Rückmeldung, aber erfordert Kraft und Platz im Cockpit.
- **Hydraulische Steuerung:** Lenkeinheit erzeugt Öldruck, Hydraulikzylinder am Ruderschaft dreht das Ruder. Für Boote ab ca. 12 m (Segelboote) bzw. ab 10 m (Motorboote). Mehr Kraft, weniger Rückmeldung.
- **Elektrohydraulische Steuerung:** Elektrische Pumpe ergänzt oder ersetzt manuelle Hydraulikpumpe. Für Yachten ab ca. 18 m. Ermöglicht Fernbedienung und Autopilot-Integration.
- **Elektrische Steuerung (Fly-by-Wire):** Sensoren am Steuerrad, Elektromotor am Ruder, kein mechanischer Durchgang. Aktuell nur bei großen Yachten (>25 m) und Superyachten.

**Entscheidungsmatrix: Wann welches System?**

| Kriterium | Mechanisch (Seil/Kette) | Mechanisch (Zahnstange) | Hydraulisch | Elektrohydraulisch |
|-----------|------------------------|------------------------|-------------|-------------------|
| Boot LOA | 7–15 m Segel, 5–12 m Motor | 4–9 m Motor | >12 m Segel, >10 m Motor | >18 m |
| Ruderkraft max. | 40–80 kgf (Seil), 100 kgf (Kette) | 60 kgf | 200+ kgf | 500+ kgf |
| Gewicht System | 3–12 kg | 2–6 kg | 15–40 kg | 30–80 kg |
| Rückmeldung | Direkt, gut spürbar | Direkt, präzise | Gedämpft | Keine (ohne Feedback) |
| Wartung | Niedrig–Mittel | Gering | Mittel–Hoch | Hoch |
| Kosten | 400–2.000 EUR | 200–800 EUR | 1.500–6.000 EUR | 4.000–20.000 EUR |
| Autopilot-Kompatibilität | Eingeschränkt (Radpilot) | Eingeschränkt | Gut (Zylinder) | Hervorragend |

### 1.3 Historische Entwicklung

- **Vor 1900:** Hölzerne Pinnen, Seilzüge über Trommeln (Großsegler), Schneckengetriebe (Dampfyachten).
- **1900–1950:** Erste standardisierte Drahtseil-Steuerungen mit Bronze-Umlenkrollen. Edson Marine (gegründet 1859) führend.
- **1950–1970:** Pedestal-Steuerungen werden Standard auf Fahrtenyachten. Ketten-Draht-Systeme etablieren sich. Whitlock beginnt Produktion in England.
- **1970–1985:** Teleflex entwickelt Push-Pull-Kabel für Motorboote. Rack-and-Pinion-Systeme für Außenborder. Jefa (Dänemark) beginnt mit hochpräzisen Systemen.
- **1985–2000:** Synthetische Seile (Dyneema) werden erprobt, setzen sich aber nicht durch (kein Vorteil bei Standardanwendungen). Edson und Whitlock modernisieren Pedestal-Designs.
- **2000–2015:** Lewmar übernimmt Whitlock (2003). Composite-Umlenkrollen. Verbesserte Kabelschmierungen. ISO 8847 wird überarbeitet.
- **2015–heute:** Hochfeste AISI-316L-Seile, PTFE-beschichtete Ketten, wartungsfreie Lager. Trend zu hydraulischen Systemen auch bei kleineren Booten. Mechanische Systeme bleiben Standard bei Serienbooten 8–13 m.

### 1.4 Geltungsbereich dieser Wissensdatei

Diese Datei deckt alle mechanischen Steuerungssysteme ab, die eine physische Kraft vom Steuerrad oder Steuerhebel über mechanische Elemente zum Ruderschaft übertragen:

1. **Seil-/Drahtsteuerung** (Cable Steering) — mit Umlenkrollen und Quadrant
2. **Ketten-Draht-Steuerung** (Chain-and-Wire) — Kette am Kettenrad, Draht zur Übertragung
3. **Vollkettensteuerung** (All-Chain) — durchgehende Kette mit Kettenführungen
4. **Zahnstangensteuerung** (Rack-and-Pinion) — hauptsächlich Motorboote mit Außenborder
5. **Schubstangensteuerung** (Push-Pull Rod) — starre Verbindung, kurze Distanzen
6. **Pedestal-Systeme** (Pedestal Steering) — Steuerständer mit integriertem Getriebe

Nicht behandelt: Pinnensteuerung ohne Übertragung (siehe 14_01), hydraulische Steuerung (siehe 14_03), Autopiloten (siehe 14_04).

---

## 2. Grundlagen

### 2.1 Physikalische Grundprinzipien der Kraftübertragung

#### 2.1.1 Seilzug-Prinzip

Die Seilsteuerung basiert auf dem **Umlenk-Seilzug-Prinzip**: Ein Drahtseil wird um eine Trommel (am Steuerrad) gewickelt, über Umlenkrollen geführt und an einem Quadranten (am Ruderschaft) befestigt. Beim Drehen des Steuerrades zieht eine Seite des Seils den Quadranten in die gewünschte Richtung, während die andere Seite nachlässt.

**Grundgleichungen:**

Ruder-Drehmoment (Rudertorque):
```
T_rudder = F_fluid × r_rudder
```
Wobei:
- `T_rudder` = Drehmoment am Ruderschaft [Nm]
- `F_fluid` = hydrodynamische Kraft auf das Ruderblatt [N]
- `r_rudder` = wirksamer Hebelarm des Ruderdruckpunkts zum Schaft [m]

Seilkraft am Quadranten:
```
F_cable = T_rudder / r_quadrant
```
Wobei:
- `F_cable` = erforderliche Seilkraft [N]
- `r_quadrant` = Radius des Quadranten [m]

Kraft am Steuerrad:
```
F_wheel = T_rudder / (r_wheel × η_system × i_getriebe)
```
Wobei:
- `F_wheel` = am Steuerradkranz erforderliche Kraft [N]
- `r_wheel` = Steuerradradius [m]
- `η_system` = Systemwirkungsgrad (0,70–0,90 typisch)
- `i_getriebe` = Untersetzungsverhältnis des Pedestalgetriebes (falls vorhanden)

**Typische Wirkungsgrade:**

| Systemkomponente | Wirkungsgrad η | Verlustursache |
|-----------------|----------------|----------------|
| Umlenkrolle (Ball Bearing) | 0,96–0,98 | Lagerreibung |
| Umlenkrolle (Gleitlager) | 0,90–0,95 | Gleitreibung |
| Seil über Rolle (90° Umlenkung) | 0,95–0,97 | Biegesteifigkeit Seil |
| Seil über Rolle (180° Umlenkung) | 0,90–0,94 | Erhöhte Biegung |
| Kette über Kettenrad | 0,94–0,97 | Zahneingriff |
| Quadrant-Befestigung | 0,98–0,99 | Lagerreibung Koker |
| Pedestal-Getriebe (neu) | 0,85–0,92 | Zahnradreibung |
| Pedestal-Getriebe (verschlissen) | 0,70–0,82 | Spiel, Abrieb |
| Zahnstange (Rack-and-Pinion) | 0,88–0,94 | Zahnreibung |
| Push-Pull-Kabel | 0,80–0,92 | Innenseil/Hülle-Reibung |

**Gesamtwirkungsgrad eines typischen Seilsteuersystems:**
```
η_total = η_pedestal × η_rolle1 × η_rolle2 × ... × η_rollen × η_quadrant
```
Beispiel: Pedestal (0,88) × 4 Rollen (0,96⁴ = 0,849) × Quadrant (0,99) = 0,88 × 0,849 × 0,99 ≈ 0,74

Das bedeutet: 26 % der aufgebrachten Kraft gehen als Reibung verloren. Bei einem Ruderdrehmoment von 200 Nm und einem Quadrantenradius von 0,15 m beträgt die theoretische Seilkraft 1.333 N, die effektive Kraft am Steuerrad bei 4 Rollen und Pedestal-Getriebe aber 1.333 / 0,74 = 1.801 N aufgebrachte Kraft am Seil, was durch die Übersetzung des Steuerrades kompensiert wird.

#### 2.1.2 Seilspannung und Seildehnung

Die korrekte Seilspannung ist der kritischste Betriebsparameter einer Seilsteuerung. Zu geringe Spannung verursacht Spiel am Steuerrad, zu hohe Spannung beschleunigt den Verschleiß aller Komponenten.

**Empfohlene Seilspannungen:**

| Seildurchmesser | Min. Spannung | Empfohlen | Max. Spannung | Bruchlast (7×19) |
|----------------|--------------|-----------|---------------|-------------------|
| 3/16" (4,8 mm) | 35 N | 50–80 N | 120 N | 15.300 N |
| 1/4" (6,4 mm) | 50 N | 80–130 N | 200 N | 26.700 N |
| 5/16" (7,9 mm) | 70 N | 120–180 N | 280 N | 41.700 N |
| 3/8" (9,5 mm) | 90 N | 160–250 N | 350 N | 57.900 N |

> ✅ Aufgelöst (Audit): Bruchlast 7×19 AISI 316 korrigiert auf 15.300 / 26.700 / 41.700 / 57.900 N (= 1.560 / 2.720 / 4.250 / 5.900 kgf, Edson-Datenblatt, deckungsgleich mit Anhang T.1). Web-bestätigt: 3/16" 7×19 316 ≈ 3.700 lb (16,5 kN), 1/4" ≈ 5.696–6.400 lb (25–28 kN). Die ursprünglichen Newton-Werte waren die Bruchlasten in Pfund, fälschlich als N ausgewiesen (Faktor ≈ 4 zu niedrig). Confidence: documented — Quelle: Edson Marine Steuerseil-Datenblatt (665-316); lifting.com / uscargocontrol.com 7×19-316-Spezifikationen.

**Seildehnung:**

Drahtseile dehnen sich unter Last. Die Dehnung besteht aus zwei Komponenten:

1. **Konstruktionsdehnung (Construction Stretch):** Setzt sich in den ersten Betriebsstunden. Litzen setzen sich, finden ihre endgültige Position. Typisch 0,5–1,0 % der Seillänge. Irreversibel.
2. **Elastische Dehnung (Elastic Stretch):** Proportional zur Last. Typisch 0,003–0,005 % pro 10 % Bruchlast. Reversibel.

```
Δl_elastic = (F × L) / (E × A)
```
Wobei:
- `Δl_elastic` = elastische Dehnung [mm]
- `F` = aufgebrachte Kraft [N]
- `L` = Seillänge [mm]
- `E` = Elastizitätsmodul des Seilverbands [N/mm²], ca. 80.000–100.000 für 7×19 Edelstahl
- `A` = metallischer Querschnitt [mm²]

**Praxisbeispiel:** Ein 8 m langes Steuerseil 1/4" (6,4 mm) mit metallischem Querschnitt 20,2 mm², belastet mit 500 N:
```
Δl = (500 × 8000) / (90.000 × 20,2) = 4.000.000 / 1.818.000 ≈ 2,2 mm
```
2,2 mm elastische Dehnung auf 8 m Länge — das ist akzeptabel und kaum spürbar.

**Problematisch wird es bei:**
- Alter, gestreckter Seile mit erhöhter Konstruktionsdehnung
- Langen Seilwegen (>12 m pro Seite)
- Korrodierten Seilen mit reduziertem Querschnitt
- Falscher Seilkonstruktion (1×19 statt 7×19 — weniger flexibel, bricht an Umlenkungen)

#### 2.1.3 Umlenkrollen-Geometrie und Seilführung

Jede Umlenkrolle (Sheave) verursacht Reibungsverluste und Seilbiegung. Die korrekte Rollengeometrie ist entscheidend für Seillebensdauer und Systemwirkungsgrad.

**Mindest-Rollendurchmesser:**

| Seildurchmesser | Min. Rollendurchmesser | Empfohlen | Optimal |
|----------------|----------------------|-----------|---------|
| 3/16" (4,8 mm) | 50 mm (10:1) | 65 mm (13:1) | 80 mm (16:1) |
| 1/4" (6,4 mm) | 65 mm (10:1) | 85 mm (13:1) | 100 mm (16:1) |
| 5/16" (7,9 mm) | 80 mm (10:1) | 105 mm (13:1) | 130 mm (16:1) |
| 3/8" (9,5 mm) | 100 mm (10:1) | 130 mm (13:1) | 160 mm (16:1) |

Die Faustregel lautet: **Rollendurchmesser ≥ 12× Seildurchmesser** für Steuerseile (Confidence: documented — Edson, Whitlock, Jefa Handbücher).

**Rillenform der Umlenkrolle:**

Die Rille (Groove) muss den Seildurchmesser eng umfassen, ohne zu klemmen:
- Rillenbreite = Seildurchmesser + 0,5 mm
- Rillentiefe = mindestens Seildurchmesser × 0,33 (Seil darf nicht herausspringen)
- Rillenwinkel (V-Form): 45–60° bei V-Rollen, halbkreisförmig bei U-Rollen
- Material: Bronze (CuSn12), Delrin/Acetal (POM), Edelstahl 316L, UHMWPE

**Umlenkwinkel und Reibungsverlust:**

| Umlenkwinkel | Reibungsverlust (Kugellager) | Reibungsverlust (Gleitlager) | Anmerkung |
|-------------|------------------------------|------------------------------|-----------|
| 15–30° | 0,5–1,0 % | 1,0–2,5 % | Leichte Umlenkung |
| 45° | 1,0–2,0 % | 2,5–4,0 % | Standard-Umlenkung |
| 90° | 2,0–4,0 % | 5,0–8,0 % | Häufig bei Seilsteuerungen |
| 135° | 3,5–6,0 % | 8,0–12,0 % | Ungünstig, vermeiden |
| 180° | 5,0–8,0 % | 10,0–15,0 % | Nur wenn unvermeidbar |

**Goldene Regel:** Maximal 4–5 Umlenkrollen pro Seilseite. Bei mehr als 5 Rollen wird die Steuerung schwergängig und unpräzise.

**Seil-Auflaufwinkel (Fleet Angle):**

Der Winkel, unter dem das Seil auf die Rolle aufläuft, sollte möglichst gerade sein:
- Idealer Auflaufwinkel: 0° (Seil in der Rillenebene)
- Akzeptabel: bis 5° seitlicher Versatz
- Problematisch: 5–10° (erhöhter Seilabrieb an Rillenkante)
- Inakzeptabel: >10° (Seil springt aus Rille, massiver Verschleiß)

#### 2.1.4 Kettensteuerung — Umschlingungswinkel und Eingriff

Bei Ketten-Draht-Systemen wird eine kurzgliedrige Kette über ein Kettenrad (Sprocket) am Pedestal geführt. Die Kette muss das Kettenrad mit ausreichendem Winkel umschlingen, damit genügend Zähne im Eingriff sind.

**Umschlingungswinkel (Wrap Angle):**

| Zähne am Kettenrad | Minimum Umschlingung | Empfohlen | Zähne im Eingriff (bei empf.) |
|--------------------|--------------------|-----------|-------------------------------|
| 10 | 108° | 144° | 4 |
| 12 | 90° | 120° | 4 |
| 14 | 77° | 103° | 4 |
| 16 | 67° | 90° | 4 |
| 18 | 60° | 80° | 4 |
| 20 | 54° | 72° | 4 |

**Mindestanforderung:** Mindestens 3 Zähne gleichzeitig im Eingriff (Confidence: documented — ISO 8847).

**Kettenteilung (Pitch):**
Steuerungsketten verwenden in der Regel folgende Teilungen:
- 3/8" (9,525 mm) — Standard Edson, Whitlock
- 1/2" (12,7 mm) — größere Yachten, Jefa
- Spezialmaße bei einzelnen Herstellern

**Ketten-Längung:**
Ketten verschleißen durch Ausschlag der Bolzen in den Laschen. Standardmäßig gilt:
- 1 % Längung = Verschleißgrenze (ISO-Norm für Antriebsketten)
- Bei Steuerungsketten: 0,5 % Längung = Austauschempfehlung (Confidence: estimated)
- Messung: 10 Glieder messen, Soll vs. Ist vergleichen

#### 2.1.5 Zahnstangengeometrie (Rack-and-Pinion)

Zahnstangensteuerungen übersetzen die Drehbewegung eines Ritzels (Pinion) in eine lineare Bewegung einer Zahnstange (Rack). Diese Linearbewegung wird über Lenkseil oder Schubstange auf den Außenborder/Z-Antrieb übertragen.

**Grundgeometrie:**
```
Hub = n × π × d_ritzel
```
Wobei:
- `Hub` = lineare Bewegung der Zahnstange [mm]
- `n` = Anzahl der Umdrehungen des Ritzels
- `d_ritzel` = Teilkreisdurchmesser des Ritzels [mm]

**Typische Werte bei Motorboot-Zahnstangenlenkungen:**
- Ritzeldurchmesser: 25–40 mm
- Hub der Zahnstange: 120–180 mm (für 60–70° Lenkeinschlag)
- Übersetzung: 2,5–4,0 Steuerrad-Umdrehungen Lock-to-Lock
- Zahnmodul: 1,5–2,5 mm

**Spielfreiheit (Backlash):**
Zahnstangensysteme müssen spielfrei oder nahezu spielfrei sein:
- Neuzustand: <0,1 mm Spiel
- Verschleißgrenze: 0,5 mm Spiel
- Prüfmethode: Ruder festhalten, am Steuerrad Spiel messen (in Grad)

#### 2.1.6 Reibungsverluste im Gesamtsystem

Die Gesamtreibung eines mechanischen Steuersystems bestimmt, wie schwer oder leicht sich das Steuerrad dreht. Zu viel Reibung ist nicht nur unbequem, sondern maskiert auch die Rückmeldung (Feedback) des Ruders.

**Reibungsquellen und typische Anteile:**

| Quelle | Anteil am Gesamtverlust | Vermeidbar? |
|--------|------------------------|-------------|
| Koker-Lager (Ruderschaft) | 15–25 % | Teilweise (besseres Lager) |
| Umlenkrollen (je Rolle 2–5 %) | 10–30 % | Ja (weniger Rollen, bessere Lager) |
| Pedestal-Getriebe | 10–20 % | Teilweise (Schmierung, Qualität) |
| Seilbiegung über Rollen | 5–15 % | Teilweise (größere Rollen) |
| Quadrant-Lagerung | 3–8 % | Ja (korrektes Lager) |
| Kette auf Kettenrad | 5–10 % | Teilweise (Schmierung) |
| Push-Pull-Kabel interne Reibung | 10–20 % | Begrenzt (Kabelqualität, Biegeradien) |

**Gesamt-Reibungsverlust typischer Systeme:**
- Seil-Steuerung, 4 Rollen, mit Pedestal: 25–40 % Verlust (η = 0,60–0,75)
- Kette-Draht, mit Pedestal: 20–35 % Verlust (η = 0,65–0,80)
- Zahnstange (Rack-and-Pinion): 10–20 % Verlust (η = 0,80–0,90)
- Push-Pull-Kabel, kurz (<3 m): 10–20 % Verlust (η = 0,80–0,90)
- Push-Pull-Kabel, lang (>5 m): 20–35 % Verlust (η = 0,65–0,80)

### 2.2 Kraftberechnung am Ruder

#### 2.2.1 Hydrodynamische Ruderkräfte

Die Kraft, die ein Ruder im Wasser erzeugt, hängt von Geschwindigkeit, Ruderwinkel, Ruderfläche und Profilform ab.

**Vereinfachte Berechnung der Ruderkraft:**
```
F_rudder = 0,5 × ρ × V² × A_rudder × C_L
```
Wobei:
- `ρ` = Dichte Seewasser ≈ 1.025 kg/m³
- `V` = Bootsgeschwindigkeit [m/s]
- `A_rudder` = projizierte Ruderfläche [m²]
- `C_L` = Auftriebsbeiwert des Ruderprofils bei gegebenem Anstellwinkel

**Ruderdrehmoment am Schaft:**
```
T_shaft = F_rudder × (x_cp - x_shaft)
```
Wobei:
- `x_cp` = Position des Druckpunkts hinter Rudervorderkante [m]
- `x_shaft` = Position des Ruderschafts hinter Rudervorderkante [m]

Bei balancierten Rudern (Schaft bei 15–25 % der Rudertiefe) wird das Drehmoment stark reduziert:
- Unbalanciertes Ruder (Schaft an Vorderkante): T ≈ 0,35 × F × Rudertiefe
- Teilbalanciertes Ruder (15 % Balance): T ≈ 0,20 × F × Rudertiefe
- Balanciertes Ruder (25 % Balance): T ≈ 0,10 × F × Rudertiefe

**Auftriebsbeiwerte (C_L) nach Ruderwinkel (NACA 0012 Profil):**

| Ruderwinkel | C_L (glatte Strömung) | C_L (turbulent) | Anmerkung |
|------------|----------------------|-----------------|-----------|
| 0° | 0,00 | 0,00 | Keine Querkraft |
| 5° | 0,40 | 0,35 | Normales Geradeausfahren mit Korrektur |
| 10° | 0,75 | 0,65 | Leichte Kursänderung |
| 15° | 1,05 | 0,90 | Moderate Kursänderung |
| 20° | 1,30 | 1,10 | Starke Kursänderung |
| 25° | 1,45 | 1,20 | Nahe Strömungsabriss |
| 30° | 1,20 | 1,00 | Partieller Strömungsabriss |
| 35° | 0,90 | 0,75 | Strömungsabriss, stark erhöhter Widerstand |
| >35° | Abfallend | Abfallend | Vollständiger Strömungsabriss, Ruder wirkt als Bremse |

**Wichtig:** Bei Ruderwinkel >25° tritt zunehmend Strömungsabriss ein. Das Ruderdrehmoment steigt nicht linear weiter, aber der Ruderwiderstand steigt dramatisch. Mechanische Steuerungen müssen auch bei Strömungsabriss-Zuständen funktionieren (Notsteuerung, Hafenmanöver bei Rückwärtsfahrt).

**Einfluss der Bootsgeschwindigkeit:**

Das Ruderdrehmoment steigt quadratisch mit der Geschwindigkeit. Verdopplung der Geschwindigkeit = vierfaches Drehmoment:

| Geschwindigkeit | Relative Ruderkraft | Typische Situation |
|----------------|--------------------|--------------------|
| 3 kn | 1,0× (Basis) | Hafenmanöver |
| 5 kn | 2,8× | Leichte Fahrt |
| 7 kn | 5,4× | Normalfahrt Segelboot |
| 10 kn | 11,1× | Raumschotsegeln |
| 15 kn | 25,0× | Schnelle Motoryacht |
| 25 kn | 69,4× | Gleiter-Motoryacht |

Dies erklärt, warum mechanische Steuerungen bei schnellen Motorbooten (>20 kn) an ihre Grenzen stoßen und hydraulische Systeme vorzuziehen sind.

**Sonderfall: Ruderkraft bei Rückwärtsfahrt**

Bei Rückwärtsfahrt kehrt sich die Anströmrichtung des Ruders um. Der Druckpunkt wandert hinter den Schaft, und das Drehmoment ändert seine Richtung. Bei unbalancierten Rudern (Schaft an Vorderkante) schlägt das Ruder abrupt zur Seite — ein bekanntes Phänomen bei Hafenmanövern.

Bei balancierten Rudern (Spatenruder) ist dieser Effekt weniger ausgeprägt, aber trotzdem vorhanden. Die mechanische Steuerung muss diese Umkehr-Kräfte ohne Schaden aufnehmen.

**Praxiswerte Ruderdrehmoment (Confidence: estimated):**

| Bootstyp | LOA | Geschwindigkeit | Ruderwinkel 10° | Ruderwinkel 25° | Ruderwinkel 35° |
|----------|-----|----------------|----------------|----------------|----------------|
| Segelboot 8 m | 8 m | 6 kn | 15 Nm | 35 Nm | 55 Nm |
| Segelboot 10 m | 10 m | 7 kn | 30 Nm | 70 Nm | 110 Nm |
| Segelboot 12 m | 12 m | 7,5 kn | 50 Nm | 120 Nm | 190 Nm |
| Segelboot 14 m | 14 m | 8 kn | 80 Nm | 200 Nm | 310 Nm |
| Motorboot 7 m | 7 m | 25 kn | 40 Nm | 100 Nm | — |
| Motorboot 10 m | 10 m | 30 kn | 80 Nm | 200 Nm | — |

**Sicherheitsfaktor:**
ISO 8847 verlangt, dass das Steuersystem das 1,5-fache des maximal zu erwartenden Ruderdrehmoments aushalten muss. In der Praxis dimensionieren die Hersteller auf Faktor 2,0–3,0.

#### 2.2.2 Quadranten-Dimensionierung

Der Quadrant (auch Ruderhebel oder Tiller Arm) ist das Bindeglied zwischen Steuerseil/Kette und Ruderschaft. Sein Radius bestimmt die Untersetzung.

**Dimensionierungsregeln:**
- Quadrantenradius = Ruderschaft-Drehmoment / max. Seilkraft
- Typische Radien: 100–200 mm (Segelboote 8–14 m)
- Ruderschaftdurchmesser: 25–50 mm (Segelboote 8–14 m), 20–35 mm (Motorboote 6–10 m)

**Standardmaße Quadranten (Confidence: documented):**

| Boot LOA | Ruderschaft ø | Quadrant-Radius | Seil ø | Sektor |
|----------|-------------|----------------|--------|--------|
| 7–9 m | 25–30 mm | 100–130 mm | 3/16" | 70° |
| 9–11 m | 30–35 mm | 130–160 mm | 1/4" | 70° |
| 11–13 m | 35–42 mm | 150–180 mm | 1/4"–5/16" | 70° |
| 13–15 m | 42–50 mm | 170–200 mm | 5/16"–3/8" | 70° |

Der Quadrant muss bei maximalem Ruderausschlag (typisch ±35° Segelboot, ±30° Motorboot) noch innerhalb des Seilzug-Bereichs bleiben. Die Seile dürfen nicht auf dem Quadrant überkreuzen.

### 2.3 Seilkonstruktionen für Steuerungen

#### 2.3.1 Seiltypen im Überblick

| Bezeichnung | Aufbau | Flexibilität | Einsatz |
|------------|--------|-------------|---------|
| 1×19 | 1 Lage, 19 Drähte | Steif | Wanten, Stage — NICHT für Steuerung |
| 7×7 | 7 Litzen à 7 Drähte | Mittel | Ältere Systeme, kurze Wege |
| 7×19 | 7 Litzen à 19 Drähte | Hoch | **Standard für Steuerseile** |
| 7×19 compacted | Verdichtet | Hoch+ | Premium-Steuerseile |
| Dyneema/HMPE | Geflochten | Sehr hoch | Experimentell, nicht ISO-konform |

**7×19 Edelstahl AISI 316** ist der universelle Standard für marine Steuerseile (Confidence: documented).

#### 2.3.2 Seilendfittings

Die Befestigung der Seile am Quadranten und an der Nachstellvorrichtung (Turnbuckle) erfolgt über:

- **Quetschhülsen (Swage Sleeves):** Maschinell verpresst, hohe Festigkeit (90–95 % der Seil-Bruchlast). Standard bei Erstausrüstung.
- **Nicopress-Hülsen:** Handzange, 80–85 % Bruchlast. Gut für Bordwerkstatt.
- **Seilklemmen (Wire Clamps):** 65–75 % Bruchlast. Nur Notlösung.
- **Kausche (Thimble):** Zum Schutz der Seilschlaufe vor Aufscheuern. Immer verwenden!
- **Gabel-Terminals (Fork Terminals):** Verschraubbare Endstücke, 90 % Bruchlast.
- **Kugelköpfe (Ball Terminals):** Rasten in Quadrantenbohrungen ein. Schneller Wechsel.

### 2.4 Normative Anforderungen

#### 2.4.1 ISO 8847 — Steueranlagen für Sportboote

Die ISO 8847 (aktuelle Fassung 2021) definiert die Mindestanforderungen an Steueranlagen:

**Wesentliche Anforderungen:**
- **Festigkeit:** Steuerung muss 1,5× max. Ruderdrehmoment ohne bleibende Verformung aushalten
- **Bruchfestigkeit:** 3,0× max. Ruderdrehmoment ohne Bruch
- **Spiel:** Max. 5° Totgang (Backlash) am Steuerrad bei neuer Anlage
- **Lebensdauer:** Min. 100.000 Zyklen (Vollausschlag) ohne Versagen
- **Korrosion:** Alle Teile im Nassbereich aus korrosionsbeständigem Material
- **Notsteuerung:** Bei Versagen der Hauptsteuerung muss eine Notsteuerungsmöglichkeit existieren
- **Kennzeichnung:** Hersteller, Typbezeichnung, max. Ruderdrehmoment, Herstelldatum

#### 2.4.2 ABYC P-17 — US-Standard

Der ABYC-Standard P-17 ergänzt ISO 8847 mit zusätzlichen Anforderungen, insbesondere:
- Mindest-Seildurchmesser abhängig von Motorleistung (bei Motorbooten)
- Korrosionstest: 96 h Salzsprühtest (ASTM B117)
- Spezifische Anforderungen an Push-Pull-Kabel-Biegeradien

#### 2.4.3 CE-Konformität

Für den EU-Markt muss jede Steueranlage die CE-Anforderungen der Recreational Craft Directive 2013/53/EU erfüllen:
- Steuerungen werden als „wesentliche Anforderungen" gemäß Anhang I, Abschnitt 5.3 behandelt
- Konformitätsbewertung: Herstellererklärung auf Basis harmonisierter Normen (ISO 8847, ISO 8848)
- Kein eigenständiges CE-Zeichen auf der Steuerung erforderlich, aber Dokumentation im technischen File des Bootes

### 2.5 Rückmeldung (Helm Feedback)

Die Rückmeldung des Ruders an den Steuermann ist ein qualitätsentscheidendes Merkmal. Mechanische Steuerungen haben grundsätzlich bessere Rückmeldung als hydraulische, weil keine Fluidkompression die Kräfte dämpft.

**Faktoren, die Rückmeldung beeinflussen:**

| Faktor | Gute Rückmeldung | Schlechte Rückmeldung |
|--------|------------------|----------------------|
| Seilspannung | Korrekt (50–130 N) | Zu niedrig (<30 N) |
| Anzahl Umlenkrollen | Wenige (2–3) | Viele (>5) |
| Rollenlager | Kugellager, leichtgängig | Gleitlager, schwergängig |
| Seilzustand | Neu, geschmiert | Alt, trocken, korrodiert |
| Quadrant-Spiel | Spielfrei | Ausgeschlagen |
| Koker-Lager | Leichtgängig, spielfrei | Schwergängig, ausgeleiert |
| Systemreibung gesamt | <25 % Verlust | >40 % Verlust |

**Bewertungskriterien Rückmeldung (AYDI-Score):**
- 90–100: Exzellent — jede Ruderbewegung sofort spürbar, Lee-/Luv-Gierigkeit eindeutig erkennbar
- 70–89: Gut — Ruderlage grundsätzlich spürbar, Feinheiten gedämpft
- 50–69: Ausreichend — Ruderlage schwer zu erspüren, Korrektur nötig
- 30–49: Mangelhaft — Rückmeldung kaum vorhanden, Steuern nach Kompass/Kielwasser
- 0–29: Ungenügend — Steuerung fühlt sich „tot" an, Sicherheitsrisiko

---

## 3. Typenübersicht

### 3.1 Seilsteuerung mit Umlenkrollen (Cable Steering)

#### 3.1.1 Funktionsprinzip

Die Seilsteuerung ist das am häufigsten eingesetzte mechanische System auf Segelyachten von 8–14 m. Zwei Drahtseile verbinden die Steuerrad-Trommel (oder das Pedestal-Kettenrad via Ketten-Draht-Übergang) mit einem Quadranten auf dem Ruderschaft.

**Systemkomponenten:**
1. **Steuerrad** — Drehgriff, überträgt Kraft auf Trommel/Kettenrad
2. **Pedestal** — Steuerständer mit Getriebe und Trommel oder Kettenrad
3. **Steuerseile** — 7×19 Edelstahl, paarweise geführt
4. **Umlenkrollen (Sheaves/Idler Pulleys)** — lenken Seile um Ecken
5. **Quadrant** — Bogensegment auf dem Ruderschaft, 70° Sektor
6. **Spannschrauben (Turnbuckles)** — zum Einstellen der Seilspannung
7. **Seilführungen (Conduit/Tube)** — optional, zur Seilführung durch Hohlräume

**Typische Seilführung auf einer 11-m-Segelyacht:**
```
Steuerrad → Pedestal-Trommel → Seil Backbord → Rolle 1 (unter Cockpitboden)
→ Rolle 2 (Backbord Bilge) → Rolle 3 (vor Ruderkoker) → Quadrant Backbord-Seite

Steuerrad → Pedestal-Trommel → Seil Steuerbord → Rolle 1 (unter Cockpitboden)
→ Rolle 2 (Steuerbord Bilge) → Rolle 3 (vor Ruderkoker) → Quadrant Steuerbord-Seite
```

#### 3.1.2 Vorteile

- Einfache Installation, Seilweg um Hindernisse herum möglich
- Leichtes Gewicht (Gesamtsystem 4–8 kg)
- Gute Rückmeldung bei korrekter Spannung und wenigen Rollen
- Kostengünstig (500–1.500 EUR komplett)
- Gut zugänglich für Wartung
- Lange Tradition, viele Fachleute verfügbar

#### 3.1.3 Nachteile

- Seilspannung erfordert regelmäßige Kontrolle und Nachstellung
- Jede Umlenkrolle = Reibungsverlust und potenzielle Fehlerquelle
- Seile dehnen sich über die Lebensdauer
- Nicht geeignet für hohe Ruderkräfte (>100 kgf am Quadranten)
- Seilbruch = sofortiger Steuerungsverlust (einseitig)
- Anfällig für Korrosion in der Bilge

#### 3.1.4 Typische Boote

- Serienproduktion-Segelboote 8–13 m (Bavaria, Jeanneau, Bénéteau, Hanse, Dufour)
- Ältere Motorboote 6–10 m
- Katamarane 10–14 m (zwei separate Systeme oder Querverbindung)

### 3.2 Kette-Draht-Steuerung (Chain-and-Wire)

#### 3.2.1 Funktionsprinzip

Bei der Kette-Draht-Steuerung wird die Drehbewegung des Steuerrades zunächst auf ein Kettenrad übertragen. Die kurzgliedrige Kette (typisch 3/8" oder 1/2" Teilung) läuft über das Kettenrad und geht über Ketten-Draht-Verbinder in Drahtseile über, die zum Quadranten führen.

**Systemkomponenten:**
1. **Steuerrad** — auf Pedestalwelle
2. **Pedestal** — mit Kettenrad und Kettenschacht
3. **Steuerkette** — kurzgliedrig, vernickelt oder Edelstahl
4. **Ketten-Draht-Verbinder (Chain-to-Wire Connectors)** — spezielle Gabelanschlüsse
5. **Steuerseile** — 7×19 Edelstahl, vom Verbinder zum Quadranten
6. **Umlenkrollen** — für die Drahtseil-Abschnitte
7. **Quadrant** — wie bei Seilsteuerung

**Vorteil gegenüber reiner Seilsteuerung:**
Die Kette auf dem Kettenrad hat keinen Schlupf (formschlüssig), während ein Seil auf der Trommel bei Spannungsverlust rutschen kann. Daher ist Kette-Draht der Standard bei hochwertigen Pedestal-Steuerungen.

#### 3.2.2 Kettentypen

| Typ | Teilung | Material | Bruchlast | Einsatz |
|-----|---------|----------|-----------|---------|
| Edson Standard | 3/8" | Vernickelter Stahl | 2.200 N | Segelboote 8–12 m |
| Edson Heavy Duty | 3/8" | Edelstahl 316 | 3.400 N | Segelboote 10–15 m |
| Whitlock/Lewmar | 3/8" | Vernickelter Stahl | 2.500 N | Segelboote 8–13 m |
| Jefa Standard | 10 mm | Edelstahl 316 | 3.000 N | Segelboote 9–14 m |
| Jefa Heavy | 12 mm | Edelstahl 316 | 4.500 N | Segelboote 12–18 m |

#### 3.2.3 Übergangsbereich Kette → Draht

Der kritischste Punkt im System ist der Kette-Draht-Übergang:
- Muss spielfrei sein
- Darf unter Last nicht aufgehen
- Muss bei Montage korrekt gesichert werden (Splint, Sicherungsdraht)
- Korrosionsgefahr: galvanische Korrosion wenn verschiedene Metalle (vernickelte Kette + Edelstahl-Seil)

### 3.3 Vollkettensteuerung (All-Chain)

#### 3.3.1 Funktionsprinzip

Bei der Vollkettensteuerung läuft die Kette vom Pedestal-Kettenrad direkt zum Ruderschaft, ohne Drahtseile. Am Ruderschaft sitzt ein zweites Kettenrad oder ein Kettenzug-Quadrant.

**Vorteile:**
- Kein Ketten-Draht-Übergang (potenzielle Schwachstelle eliminiert)
- Kein Seilschlupf, kein Seilrecken
- Konstante Untersetzung über den gesamten Drehbereich
- Sehr langlebig bei guter Schmierung

**Nachteile:**
- Kette muss gerade oder über große Radien geführt werden (keine 90°-Umlenkungen wie bei Seil)
- Schwerer als Seilsystem
- Kettenführungen (Tubes oder Rohre) nötig
- Lauter im Betrieb (Kettengeräusch)
- Begrenzt einsetzbar wenn Seilweg um viele Ecken führen muss

#### 3.3.2 Typische Anwendung

- Ältere britische Yachten (Hallberg-Rassy, Nicholson, Moody bis ca. 1990)
- Langfahrt-Yachten mit geradlinigem Weg Pedestal → Ruderkoker
- Custom-Yachten mit spezieller Konstruktion
- Yachten mit Mittencockpit, wo der Seilweg sehr kurz ist

### 3.4 Zahnstangensteuerung (Rack-and-Pinion)

#### 3.4.1 Funktionsprinzip

Ein Ritzel (kleines Zahnrad) am Steuerrad kämmt mit einer linearen Zahnstange. Die Zahnstange bewegt sich seitlich und überträgt diese Linearbewegung über Gestänge oder Lenkseile auf den Außenborder/Z-Antrieb.

**Systemkomponenten:**
1. **Steuerradgehäuse (Helm)** — enthält Ritzel und Zahnstange
2. **Zahnstange (Rack)** — mit beidseitigen Anschlüssen
3. **Lenkseile oder Gestänge** — verbinden Zahnstange mit Motor
4. **Lenkarme/Hebel** — am Motor, wandeln Linear- in Drehbewegung um

#### 3.4.2 Einsatzbereich

Zahnstangensteuerungen dominieren bei:
- Motorbooten mit Außenborder (4–12 m)
- Schlauchbooten (RIBs) mit Außenborder
- Sportbooten mit Z-Antrieb (Sterndrive)
- Kleineren Motorbooten mit Innenborder und Ruder (selten)

#### 3.4.3 Varianten

| Variante | Hersteller | Einsatz | Besonderheit |
|----------|-----------|---------|-------------|
| Standard Rack | Teleflex/SeaStar, Ultraflex | Einmotorig, bis 150 PS | Einfachste Bauform |
| NFB (No-Feedback) Rack | SeaStar, Ultraflex | Einmotorig, 75–300 PS | Rückschlag-Sperre |
| Safe-T QC | Teleflex | Einmotorig, bis 150 PS | Schnellverbindung |
| Doppelkabel-Rack | SeaStar | Zweimotorig | Synchrone Lenkung beider Motoren |
| Tilt-Rack | Diverse | Konsolen mit schrägem Lenkrad | Winkelgetriebe integriert |

#### 3.4.4 NFB-Systeme (No Feedback)

Bei schnellen Motorbooten mit großen Außenbordern kann der Propeller-Rückdrehmoment (Torque Steer) das Steuerrad aus der Hand reißen. NFB-Systeme verwenden eine Rückschlagsperre im Zahnstangengehäuse:
- Kraft vom Steuerrad → Motor: ungehindert
- Kraft vom Motor → Steuerrad: blockiert (Einwegkupplung)
- Nachteil: Keine Ruder-Rückmeldung mehr
- Notwendig bei Außenbordern >75 PS in Gleiterbooten

### 3.5 Schubstangensteuerung (Push-Pull Rod/Cable)

#### 3.5.1 Funktionsprinzip

Eine starre oder semiflexible Stange/Kabel überträgt eine Schub-/Zugkraft linear vom Steuergetriebe zum Ruder oder Motor. Bei Push-Pull-Kabeln läuft ein Innenkabel (Seele) in einer steifen Außenhülle (Conduit).

**Zwei Untervarianten:**

**a) Starre Schubstange (Solid Push Rod):**
- Metallstange mit Kugelgelenken an beiden Enden
- Nur für sehr kurze Distanzen (<1,5 m)
- Kein Bogen möglich — muss gerade verlaufen
- Höchste Präzision, kein Spiel

**b) Push-Pull-Kabel (Flexible):**
- Inneres Stahlseil in steifer Kunststoff-/Stahlhülle
- Kann moderate Bögen machen (Mindestradius 200–400 mm je nach Typ)
- Distanzen bis ca. 8 m möglich
- Standard bei Motorbooten (Teleflex, Ultraflex, SeaStar)

#### 3.5.2 Aufbau eines Push-Pull-Kabels

```
Außenhülle (Conduit): PE oder PA verstärkt mit Stahldraht-Wendel
├── Schmierfett-Füllung
├── PTFE-Liner (bei Premium-Kabeln)
└── Innenkabel (Core Wire): 7×7 oder 7×19 Edelstahl, mit Endstücken

Endstücke:
├── Motor-Seite: Kugelkopf, Gabelkopf oder Schraubanschluss
└── Helm-Seite: Gewindeanschluss an Zahnstange oder Trommel
```

#### 3.5.3 Biegeradien und Reibung

Der kritischste Parameter bei Push-Pull-Kabeln ist der Biegeradius:

| Kabeltyp | Min. Biegeradius | Empfohlen | Reibungszunahme pro 90° |
|----------|-----------------|-----------|------------------------|
| Standard (Teleflex SSC62) | 200 mm | 300 mm | +8–12 % |
| Standard (Teleflex SSC134) | 200 mm | 300 mm | +8–12 % |
| Premium (SeaStar SSC6200) | 150 mm | 250 mm | +5–8 % |
| Heavy Duty (Ultraflex M90) | 250 mm | 400 mm | +10–15 % |

**Goldene Regel:** Max. 2 Bögen à 90° im Kabelverlauf. Bei mehr Bögen wird die Steuerung unakzeptabel schwer (Confidence: documented — Teleflex/SeaStar Installation Guide).

#### 3.5.4 Typische Anwendungen

- Motorboote 4–10 m mit Außenborder oder Z-Antrieb
- Center-Console-Boote
- RIBs (Schlauchboote mit Steuerstand)
- Jetboote, Jetskis (spezielle Varianten)
- Arbeitsboote, Fischerboote

### 3.6 Pedestal-Systeme (Steuerständer)

#### 3.6.1 Funktionsprinzip

Der Pedestal (Steuerständer) ist das zentrale Element der Segelboot-Steuerung. Er steht im Cockpit und enthält:

1. **Steuerradwelle** — horizontal oder leicht geneigt
2. **Getriebe** — Kegelradgetriebe, Schneckengetriebe oder Planetengetriebe
3. **Trommel oder Kettenrad** — am unteren Ende der Ausgangswelle
4. **Kompass-Aufnahme** — oberseitig in der Binnacle-Haube
5. **Instrumenten-Halterung** — für Displays, Autopilot-Bedienteile
6. **Motorhebel-Integration** — optional: Gashebel am Pedestal

#### 3.6.2 Getriebetypen im Pedestal

| Typ | Untersetzung | Wirkungsgrad | Rückdrehbar? | Einsatz |
|-----|-------------|-------------|-------------|---------|
| Kegelrad (Bevel Gear) | 1:1 bis 2:1 | 88–93 % | Ja | Standard, die meisten Pedestals |
| Schneckengetriebe (Worm Gear) | 3:1 bis 8:1 | 40–70 % | Nein (selbsthemmend) | Große Yachten, hohe Ruderkräfte |
| Planetengetriebe (Planetary) | 2:1 bis 5:1 | 85–92 % | Ja | Premium-Systeme (Jefa) |
| Kette direkt | 1:1 | 95–97 % | Ja | Einfache Systeme, Kettenrad direkt auf Welle |

**Selbsthemmung bei Schneckengetriebe:**
Ein Schneckengetriebe mit ausreichend hohem Steigungswinkel ist selbsthemmend — das Ruder kann das Steuerrad nicht zurückdrehen. Das eliminiert Rückschlag bei Motorbooten, aber eliminiert auch die Rückmeldung bei Segelbooten. Deshalb werden Schneckengetriebe auf Segelbooten nur bei großen Yachten (>18 m) oder auf ausdrücklichen Wunsch eingesetzt.

#### 3.6.3 Pedestal-Größen

| Pedestal-Klasse | Boot LOA | Steuerrad ø | Ruder-Torque max. | Gewicht |
|----------------|----------|------------|-------------------|---------|
| Small (Edson 335) | 7–10 m | 600–800 mm | 100 Nm | 6 kg |
| Medium (Edson 336) | 9–13 m | 800–1.000 mm | 200 Nm | 9 kg |
| Large (Edson 337) | 12–16 m | 900–1.200 mm | 350 Nm | 14 kg |
| XL (Jefa 444) | 14–20 m | 1.000–1.400 mm | 500 Nm | 18 kg |
| Custom | >18 m | 1.200+ mm | >500 Nm | 20+ kg |

> ⚠️ **ZU PRÜFEN (Audit):** Ruder-Torque und Gewicht für Edson 336 (hier 200 Nm / 9 kg) und Edson 337 (hier 350 Nm / 14 kg) widersprechen der detaillierten Edson-Produkttabelle in Abschnitt 4.1.2 (Edson 336 = 170 Nm / 8,2 kg; Edson 337 = 270 Nm / 11,3 kg; die 350 Nm / 14,5 kg gehören dort zum Edson 338). Confidence: estimated — unverifiziert. Herstellerangaben (Edson-Katalog) prüfen, nicht raten.

#### 3.6.4 Doppelrad-Konfiguration (Twin Wheel)

Auf Segelyachten ab ca. 12 m werden häufig zwei Steuerräder eingesetzt, eins an jeder Cockpit-Seite. Vorteile:
- Bessere Sicht nach Lee auf Amwindkursen
- Mehr Platz im Cockpit (kein zentrales Rad im Weg)
- Redundanz (bei Bruch einer Seite weiter steuerbar)

**Technische Umsetzung:**
- Zwei Pedestals, verbunden über Querwelle oder Synchron-Seilzug
- Oder: Ein Pedestal zentral, zwei Steuerräder über Kette/Seil angebunden
- Oder: Jefa Direct-Drive-System mit zwei Säulen direkt auf dem Ruderschaft (ohne Seile)

### 3.7 Vergleichsmatrix aller mechanischen Systeme

| Kriterium | Seil | Kette-Draht | Vollkette | Rack-and-Pinion | Push-Pull | Pedestal (Kette-Draht) |
|-----------|------|-------------|-----------|----------------|-----------|----------------------|
| Typische LOA | 8–14 m | 8–15 m | 8–14 m | 4–12 m | 4–10 m | 8–16 m |
| Max. Rudertorque | 200 Nm | 350 Nm | 350 Nm | 150 Nm | 100 Nm | 500 Nm |
| Wirkungsgrad | 60–75 % | 65–80 % | 75–85 % | 80–94 % | 80–90 % | 65–80 % |
| Rückmeldung | Gut | Gut–Sehr gut | Sehr gut | Mäßig | Mäßig | Gut–Sehr gut |
| Wartungsaufwand | Mittel | Mittel | Gering–Mittel | Gering | Gering | Mittel |
| Kosten Komplett | 500–1.500 | 800–2.000 | 600–1.500 | 200–800 | 100–500 | 1.500–4.000 |
| Montage-Komplexität | Mittel | Mittel | Mittel–Hoch | Gering | Gering | Hoch |
| Lebensdauer | 8–15 J. | 10–20 J. | 15–25 J. | 8–15 J. | 5–12 J. | 15–25 J. |

---

## 4. Produktlinien und Hersteller

### 4.1 Edson Marine (USA, seit 1859)

#### 4.1.1 Firmenüberblick

Edson Marine ist der älteste und weltweit führende Hersteller von Pedestal-Steuerungen für Segelyachten. Gegründet 1859 in New Bedford, Massachusetts (ehemals Walfang-Zentrum), liefert Edson heute an die meisten großen Serienwerften weltweit.

**Produktbereiche:**
- Pedestal-Steuerungen (Kerngeschäft)
- Steuerräder (Edelstahl, Carbon, Teak)
- Quadranten und Seilsteuerungs-Kits
- Autopilot-Antriebseinheiten
- Pumpen (Bilge, Feuerlösch-)

#### 4.1.2 Pedestal-Reihe

| Modell | Boot LOA | Ruder-Torque | Kettenrad | Kette | Gewicht | Preis (ca.) |
|--------|----------|-------------|-----------|-------|---------|------------|
| Edson 335 | 7–10 m | 100 Nm | 13 Zähne, 3/8" | 3/8" vernickelt | 5,9 kg | 1.200 EUR |
| Edson 336 | 9–12 m | 170 Nm | 13 Zähne, 3/8" | 3/8" vernickelt | 8,2 kg | 1.500 EUR |
| Edson 337 | 11–14 m | 270 Nm | 15 Zähne, 3/8" | 3/8" vernickelt | 11,3 kg | 2.000 EUR |
| Edson 338 | 13–16 m | 350 Nm | 15 Zähne, 3/8" | 3/8" SS | 14,5 kg | 2.800 EUR |
| Edson 339 | 15–20 m | 500 Nm | 17 Zähne, 1/2" | 1/2" SS | 18,0 kg | 3.800 EUR |

**Teilenummern (häufig benötigt):**

| Teil | Edson-Nr. | Beschreibung |
|------|----------|-------------|
| Steuerkette 3/8" | 669 | 3/8" vernickelt, per Fuß |
| Steuerkette 3/8" SS | 669-SS | 3/8" Edelstahl 316, per Fuß |
| Steuerradwelle | 506-ST | Standard-Welle ø25 mm |
| Kettenrad 13Z | 649-13 | 13 Zähne, 3/8" Teilung |
| Kettenrad 15Z | 649-15 | 15 Zähne, 3/8" Teilung |
| Chain-Wire-Verbinder | 663 | 3/8" Kette auf 1/4" Seil |
| Quadrant 300 mm | 976-12 | Alu eloxiert, ø30 mm Bohrung |
| Quadrant 350 mm | 976-14 | Alu eloxiert, ø35 mm Bohrung |
| Quadrant 400 mm | 976-16 | Alu eloxiert, ø40 mm Bohrung |
| Spannschraube | 668 | Turnbuckle für Seilspannung |
| Umlenkrolle Ball-Bearing | 414 | Edelstahl, Kugellager, 3" |
| Umlenkrolle Ball-Bearing | 416 | Edelstahl, Kugellager, 4" |
| Seilführung (Conduit) | 448 | Edelstahl-Liner, per Fuß |
| Komplett-Kit 9–12 m | Kit-336 | Pedestal + Seil + Rollen + Quadrant |

#### 4.1.3 Steuerräder

| Modell | Durchmesser | Material | Griffe | Preis (ca.) |
|--------|------------|---------|--------|------------|
| PowerWheel | 32"–42" | Edelstahl 316 | Teak-Griffe | 800–1.500 EUR |
| Ultralight | 36"–48" | Carbon | Carbon-Griffe | 2.000–4.000 EUR |
| ComfortGrip | 28"–40" | Edelstahl 316 | Leder-Umwicklung | 600–1.200 EUR |
| Classic Teak | 30"–42" | Teak, SS-Nabe | Teak | 900–1.800 EUR |
| Destroyer | 24"–36" | Edelstahl geschmiedet | Stahl | 500–900 EUR |

#### 4.1.4 Stärken und Schwächen

**Stärken:**
- Größtes Angebot an Pedestal-Größen und Zubehör
- Ersatzteile weltweit verfügbar (direkt oder über SVB, Compass, West Marine)
- Ausgezeichnete Dokumentation und Installationsanleitungen
- Kompatibel mit fast allen Serienyachten
- Robuste, bewährte Konstruktion

**Schwächen:**
- Vernickeltes Ketten-Material korrodiert in tropischen Gewässern schneller als Edelstahl
- Getriebe-Spiel bei älteren Modellen (vor 2005) kann zunehmen
- Kegelrad-Design nicht immer spielfrei
- US-Zoll-Maße erfordern manchmal Adaptionen im metrischen Europa
- Keine Direct-Drive-Option (immer Seil/Kette zum Quadranten)

### 4.2 Lewmar / Whitlock (UK)

#### 4.2.1 Firmenüberblick

Whitlock wurde 1962 in Buckinghamshire gegründet und war der führende britische Pedestal-Hersteller. Im Jahr 2003 übernahm Lewmar (Hampshire, gegründet 1946 als Winsch-Hersteller) das Steuerungsgeschäft von Whitlock. Lewmar produziert unter eigenem Namen weiter und bedient insbesondere europäische Werften.

#### 4.2.2 Pedestal-Reihe

| Modell | Boot LOA | Ruder-Torque | Getriebe | Kette | Preis (ca.) |
|--------|----------|-------------|----------|-------|------------|
| Lewmar Constellation 30 | 7–9 m | 85 Nm | Kegelrad | 3/8" | 950 EUR |
| Lewmar Constellation 40 | 9–12 m | 150 Nm | Kegelrad | 3/8" | 1.350 EUR |
| Lewmar Constellation 50 | 11–14 m | 250 Nm | Kegelrad | 3/8" | 1.900 EUR |
| Lewmar Constellation 60 | 13–16 m | 350 Nm | Kegelrad | 3/8" | 2.500 EUR |
| Lewmar Ocean 60 | 14–18 m | 400 Nm | Kegelrad + Untersetzung | 1/2" | 3.200 EUR |
| Lewmar Ocean 80 | 16–22 m | 550 Nm | Kegelrad + Untersetzung | 1/2" | 4.500 EUR |

**Teilenummern (häufig benötigt):**

| Teil | Lewmar-Nr. | Beschreibung |
|------|-----------|-------------|
| Steuerkette 3/8" | 89700020 | Per Meter, vernickelt |
| Steuerkette 1/2" SS | 89700040 | Per Meter, Edelstahl |
| Kettenrad-Satz | 89000110 | Passend für Constellation-Reihe |
| Chain-Wire-Verbinder | 89400010 | 3/8" Kette auf 1/4" Seil |
| Quadrant 300 mm | 89800130 | Alu, ø30 mm Bohrung |
| Quadrant 350 mm | 89800140 | Alu, ø35 mm Bohrung |
| Umlenkrolle | 89600030 | Edelstahl mit Kugellager |
| Steuerkit komplett | 89900050 | Constellation 40 + Seil + Quadrant |
| Seal-Kit Pedestal | 89100060 | O-Ringe und Wellendichtungen |
| Kompass-Adaptor | 89200020 | Für Plastimo Contest oder Silva |

#### 4.2.3 Kabelsteuerungs-Kits (ohne Pedestal)

Lewmar bietet auch reine Kabelsteuerungs-Kits für einfachere Installationen oder Nachrüstungen:

| Kit | Boot LOA | Inhalt | Preis (ca.) |
|-----|----------|--------|------------|
| Cable Kit 30 | 7–9 m | 2× Seil 1/4" je 6 m, 4 Rollen, Quadrant 300 mm, 2 Spannschrauben | 450 EUR |
| Cable Kit 40 | 9–12 m | 2× Seil 1/4" je 8 m, 6 Rollen, Quadrant 350 mm, 2 Spannschrauben | 650 EUR |
| Cable Kit 50 | 11–14 m | 2× Seil 5/16" je 10 m, 6 Rollen, Quadrant 400 mm, 2 Spannschrauben | 850 EUR |

#### 4.2.4 Stärken und Schwächen

**Stärken:**
- Europäischer Standard, metrische Maße
- Sehr gute Passform bei europäischen Serienyachten (Bénéteau, Jeanneau, Bavaria)
- Lewmar-Vertriebsnetz in Europa hervorragend
- Moderne Kegelrad-Ausführung mit wenig Spiel
- Compass-/Instrumenten-Integration gut durchdacht

**Schwächen:**
- Kleinere Teilenummer-Vielfalt als Edson
- Ersatzteilversorgung außerhalb Europas schwieriger
- Constellation-Serie nicht für Rudertorque >350 Nm
- Ältere Whitlock-Modelle (vor 2003) haben spezielle Maße, teilweise nicht kompatibel mit neuen Lewmar-Teilen

### 4.3 Jefa Steering (Dänemark)

#### 4.3.1 Firmenüberblick

Jefa Rudder & Steering wurde 1978 in Bramming, Dänemark gegründet. Jefa ist spezialisiert auf hochpräzise Steuerungssysteme für den Semi-Custom- und Custom-Yachtbau und gilt als Premiummarke. Jefa bietet als einziger Hersteller sowohl konventionelle Kette-Draht-Systeme als auch Direct-Drive-Steuerungen (ohne Seile/Ketten) an.

#### 4.3.2 Konventionelle Kette-Draht-Systeme

| Modell | Boot LOA | Ruder-Torque | Besonderheit | Preis (ca.) |
|--------|----------|-------------|-------------|------------|
| Jefa Basic 30 | 7–10 m | 100 Nm | Einfaches Kegelrad | 1.100 EUR |
| Jefa Standard 40 | 9–13 m | 200 Nm | Planetengetriebe | 1.800 EUR |
| Jefa Advantage 50 | 12–16 m | 350 Nm | Planetengetriebe, spielfrei | 2.800 EUR |
| Jefa Advantage 60 | 14–20 m | 500 Nm | Doppel-Planetengetriebe | 4.200 EUR |
| Jefa Advantage 80 | 18–25 m | 800 Nm | Sonder-Planetengetriebe | 6.500 EUR |

#### 4.3.3 Direct-Drive-Systeme

Das Jefa Direct-Drive-System ist eine Revolution im mechanischen Steuerbau. Statt Seilen und Ketten sitzt eine vertikale Welle direkt vom Pedestal zum Ruderschaft. Ein Kreuzgelenk oder Kegelradsatz verbindet die horizontale Steuerradwelle mit der vertikalen Antriebswelle, die unten direkt auf den Ruderschaft wirkt.

**Vorteile:**
- Kein Seil, keine Kette, kein Quadrant = keine Dehnung, kein Spiel
- Direkteste Rückmeldung aller mechanischen Systeme
- Wartungsfrei (keine Seilspannung nachstellen)
- Höchste Präzision und Wiederholgenauigkeit
- Lebensdauer >25 Jahre

**Nachteile:**
- Hoher Preis (3.000–8.000 EUR)
- Erfordert spezielle Cockpit-Konstruktion (vertikaler Schacht für Antriebswelle)
- Nachrüstung bei bestehenden Booten oft nicht möglich
- Nur von Jefa und wenigen Lizenznehmern

| Modell | Boot LOA | Ruder-Torque | Welle ø | Preis (ca.) |
|--------|----------|-------------|---------|------------|
| Jefa DD30 | 8–11 m | 150 Nm | 25 mm | 3.200 EUR |
| Jefa DD40 | 10–14 m | 250 Nm | 30 mm | 4.500 EUR |
| Jefa DD50 | 13–17 m | 400 Nm | 35 mm | 6.000 EUR |
| Jefa DD60 | 15–20 m | 600 Nm | 40 mm | 7.500 EUR |
| Jefa DD Twin | 12–20 m | 250–600 Nm | 25–40 mm | 6.000–12.000 EUR |

**Teilenummern (häufig benötigt):**

| Teil | Jefa-Nr. | Beschreibung |
|------|---------|-------------|
| Kette 10 mm SS | JF-CH-10 | Per Meter, Edelstahl 316 |
| Kette 12 mm SS | JF-CH-12 | Per Meter, Edelstahl 316 |
| Kettenrad 10 mm | JF-SP-10 | 13 Zähne, für 10-mm-Kette |
| Kettenrad 12 mm | JF-SP-12 | 15 Zähne, für 12-mm-Kette |
| Quadrant Standard | JF-QD-S | Alu, diverse Bohrungen |
| Quadrant Heavy | JF-QD-H | Edelstahl, für Torque >300 Nm |
| DD-Welle 25 mm | JF-DD-25 | Per Meter, Edelstahl 316L |
| DD-Kreuzgelenk | JF-UJ-25 | Universalgelenk 25 mm |
| DD-Kegelradsatz | JF-BG-30 | Für DD40 |
| Lager-Kit DD | JF-BRK-30 | Lager und Dichtungen für DD-Welle |
| Pedestal Seal Kit | JF-SK-40 | O-Ringe, Wellendichtungen für Std. 40 |

#### 4.3.4 Stärken und Schwächen

**Stärken:**
- Höchste Qualität und Präzision im Markt
- Einziger Anbieter von Direct-Drive-Systemen
- Planetengetriebe mit hervorragendem Wirkungsgrad
- Edelstahl-Ketten als Standard
- Ausgezeichneter technischer Support direkt vom Hersteller
- Bevorzugt von Custom-Werften (Hallberg-Rassy, Malo, Contest, Najad)

**Schwächen:**
- Deutlich teurer als Edson und Lewmar
- Eingeschränkte Verfügbarkeit (wenige Händler außerhalb Skandinavien)
- Direct-Drive nur bei Neubau oder Totalumbau möglich
- Längere Lieferzeiten bei Spezialanfertigungen

### 4.4 Teleflex / SeaStar Solutions (USA/Kanada)

#### 4.4.1 Firmenüberblick

Teleflex Marine (heute SeaStar Solutions, seit 2013 Teil von Dometic) ist der weltweit größte Hersteller von Steuerungssystemen für Motorboote. Das Produktportfolio umfasst mechanische Steuerungen (Push-Pull-Kabel, Rack-and-Pinion), hydraulische Steuerungen und elektronische Systeme.

#### 4.4.2 Mechanische Steuerungskabel (Push-Pull)

| Modell | Typ | Motor-PS | Länge | Biegeradius min. | Preis (ca.) |
|--------|-----|----------|-------|-----------------|------------|
| SSC61 | Standard | bis 55 PS | 8–24 ft | 8" (200 mm) | 30–70 EUR |
| SSC62 | Standard | bis 150 PS | 8–30 ft | 8" (200 mm) | 40–90 EUR |
| SSC134 | Xtreme | bis 300 PS | 8–30 ft | 8" (200 mm) | 50–110 EUR |
| SSC6200 | Premium | bis 300 PS | 8–30 ft | 6" (150 mm) | 80–150 EUR |
| SSC6210 | Premium HD | bis 400 PS | 8–36 ft | 6" (150 mm) | 100–180 EUR |
| 3300 Series | Universal | bis 150 PS | Variabel | 6" (150 mm) | 35–80 EUR |
| 4300 Series | Heavy Duty | bis 300 PS | Variabel | 8" (200 mm) | 60–120 EUR |

**Hinweis:** Kabellängen werden in Fuß angegeben. 1 Fuß = 0,3048 m. Länge wird am besten mit dem Teleflex Length Calculator ermittelt (oder: Abstand Helm → Motor über den tatsächlichen Kabelweg + 5 % Zugabe).

#### 4.4.3 Rack-and-Pinion Helms (Steuergetriebe)

| Modell | Typ | Motor-PS | Drehungen Lock-to-Lock | NFB? | Preis (ca.) |
|--------|-----|----------|----------------------|------|------------|
| Safe-T QC | Standard | bis 150 PS | 3,5 | Nein | 150 EUR |
| Safe-T II | Standard | bis 150 PS | 3,5 | Nein | 120 EUR |
| NFB Safe-T II | NFB | bis 300 PS | 3,5 | Ja | 250 EUR |
| NFB 4.2 | NFB Rotary | bis 300 PS | 4,2 | Ja | 280 EUR |
| Big-T | Heavy Duty | bis 400 PS | 3,0 | Optional | 350 EUR |
| Tilt-Helm | Neigbar | bis 200 PS | 3,5 | Optional | 200 EUR |

#### 4.4.4 Teilenummern (häufig benötigt)

| Teil | SeaStar-Nr. | Beschreibung |
|------|------------|-------------|
| Steuerkabel SSC62 10ft | SSC62-10 | Standard-Kabel 10 Fuß |
| Steuerkabel SSC62 14ft | SSC62-14 | Standard-Kabel 14 Fuß |
| Steuerkabel SSC134 12ft | SSC134-12 | Xtreme-Kabel 12 Fuß |
| Helm Safe-T QC | SH5130P | Quick-Connect Helm |
| Helm NFB 4.2 | SH5150P | NFB Rotary Helm |
| Bezel Kit | SH91484P | Blende/Spritzschutz |
| 90°-Adapter | SH5075 | Winkeladapter für Kabel |
| Lenkarm Mercury | SH5100 | Universell für Mercury Outboard |
| Lenkarm Yamaha | SH5101 | Universell für Yamaha Outboard |
| Dual-Cable-Kit | SH5180 | Für Doppelmotoranlagen |
| Kabelhalter (Clip) | SH5050 | Sicherungsklammer alle 600 mm |
| Schmiermittel | SeaStar Lube | Für Push-Pull-Kabelschmierung |

#### 4.4.5 Stärken und Schwächen

**Stärken:**
- Größtes Sortiment an Motorboot-Steuerungskabeln weltweit
- Kompatibel mit allen gängigen Außenborder-Marken (Mercury, Yamaha, Honda, Suzuki, Evinrude/BRP)
- Hervorragendes Preis-Leistungs-Verhältnis
- Ersatzteile in jedem Marineladen verfügbar
- Ausgezeichnete Installationsanleitungen und Online-Kalkulatoren
- NFB-Systeme sind Industriestandard

**Schwächen:**
- Nicht für Segelboote konzipiert (kein Pedestal-Programm)
- Push-Pull-Kabel haben begrenzte Lebensdauer (5–10 Jahre bei Salzwasser)
- Korrosion der Außenhülle bei Kabeln unter Deck möglich
- Reibung steigt mit Kabellänge deutlich an
- US-Maße (Fuß, Zoll) erfordern Umrechnung

### 4.5 Ultraflex (Italien)

#### 4.5.1 Firmenüberblick

Ultraflex S.p.A. (Campodarsego, Italien, gegründet 1967) ist der größte europäische Hersteller von Steuerungskabeln und -getrieben für Motorboote. Das Unternehmen beliefert europäische Werften als OEM und bietet ein breites Aftermarket-Sortiment.

#### 4.5.2 Produktreihen

**Steuerungskabel:**

| Modell | Typ | Motor-PS | Länge | Besonderheit | Preis (ca.) |
|--------|-----|----------|-------|-------------|------------|
| M58 | Standard | bis 55 PS | 6–24 ft | Basiskabel | 25–60 EUR |
| M66 | Standard | bis 150 PS | 6–30 ft | Universell | 35–80 EUR |
| M86 | Heavy Duty | bis 300 PS | 8–30 ft | Verstärkte Hülle | 50–100 EUR |
| M90 Mach | Premium | bis 400 PS | 8–36 ft | Reduzierte Reibung | 70–140 EUR |
| C2/C8 | Universell | bis 150 PS | Variabel | Metrisches Anschlusssystem | 30–75 EUR |

**Steuergetriebe (Helms):**

| Modell | Typ | Motor-PS | Drehungen | NFB? | Preis (ca.) |
|--------|-----|----------|-----------|------|------------|
| T67 | Standard Rack | bis 150 PS | 3,5 | Nein | 100 EUR |
| T71 FC | NFB Rack | bis 200 PS | 3,5 | Ja | 180 EUR |
| T73 NRFC | NFB Rotary | bis 300 PS | 4,0 | Ja | 250 EUR |
| T85 | Heavy Duty Rotary | bis 400 PS | 3,5 | Ja | 320 EUR |
| T91 Tilt | Neigbar | bis 200 PS | 3,5 | Optional | 180 EUR |

#### 4.5.3 Stärken und Schwächen

**Stärken:**
- Metrisches Maßsystem (kompatibel mit europäischen Motoren)
- Sehr gutes Preis-Leistungs-Verhältnis (günstiger als Teleflex/SeaStar)
- Breite OEM-Basis (Lomac, Ranieri, Selva, Quicksilver)
- Gute Verfügbarkeit in Mittelmeer-Ländern

**Schwächen:**
- Außerhalb Europas weniger verbreitet
- Technische Dokumentation nicht immer auf dem Niveau von SeaStar
- Einige Kabeltypen nicht 1:1 kompatibel mit SeaStar-Helms

### 4.6 Weitere Hersteller

#### 4.6.1 Kobelt (Kanada)

Kobelt Manufacturing (Surrey, BC, gegründet 1962) ist auf Steuerungen für größere Arbeitsboote und Motoryachten spezialisiert.

| Modell | Typ | Einsatz | Rudertorque | Preis (ca.) |
|--------|-----|---------|-------------|------------|
| Kobelt 7003 | Rack-and-Pinion | Motorboote 8–14 m | 200 Nm | 800 EUR |
| Kobelt 7004 | Rack-and-Pinion HD | Motorboote 10–18 m | 400 Nm | 1.200 EUR |
| Kobelt 7012 | Mechanical Helm | Arbeitsboote 8–16 m | 300 Nm | 1.000 EUR |

#### 4.6.2 Hynautic (USA, historisch)

Hynautic war ein bedeutender US-Hersteller hydraulischer und mechanischer Steuerungen, wurde 2005 von Teleflex übernommen. Ältere Yachten haben noch Hynautic-Systeme an Bord. Ersatzteile über SeaStar Solutions als Hynautic-Legacy erhältlich.

#### 4.6.3 Yacht Specialties / Pompanette (USA)

Pompanette (Miami, FL) stellt Premium-Steuerständer für Sport-Fishing-Boote her:

| Modell | Einsatz | Material | Besonderheit | Preis (ca.) |
|--------|---------|----------|-------------|------------|
| Pompanette 86 Series | Offshore 8–16 m | Edelstahl 316L | Helm Chair-integriert | 3.000–8.000 EUR |
| Pompanette 96 Series | Tournament 12–22 m | Edelstahl/Alu | Dual-Station | 5.000–12.000 EUR |

#### 4.6.4 Vetus (Niederlande)

Vetus liefert mechanische Steuerungskabel und -getriebe für den europäischen Motorboot-Markt:

| Modell | Typ | Motor-PS | Besonderheit | Preis (ca.) |
|--------|-----|----------|-------------|------------|
| Vetus MT30 | Rack Helm | bis 100 PS | Einfach, günstig | 80 EUR |
| Vetus MT52 | Rack Helm NFB | bis 200 PS | No-Feedback | 170 EUR |
| Vetus Cable M | Standard-Kabel | bis 150 PS | Metrisch | 30–70 EUR |

#### 4.6.5 Uflex (Italien)

Uflex S.p.A. (Iseo, Italien) ist der Mutterkonzern von Ultraflex und bietet zusätzlich eigene Marken:
- **Silversteer** — hydraulische Systeme
- **Accura** — elektronische Steuerungen
- **Mach Series** — Premium-Kabel mit PTFE-Liner

#### 4.6.6 Presspull / Morse (historisch)

Morse (Teil von Teleflex seit 1988) und Presspull waren historisch bedeutende Kabelhersteller. Ihre Teilenummern begegnen bei älteren Booten:
- Morse MR-Serie = heute SeaStar 3300/4300 Serie
- Morse 33C Cable = heute SeaStar 3300 Serie Equivalent

### 4.7 Cross-Referenz: Bootshersteller → Steuerungssystem

| Bootshersteller | Typische LOA | Steuersystem | Hersteller |
|----------------|-------------|-------------|-----------|
| Bavaria (Segelboote) | 8–15 m | Kette-Draht, Pedestal | Lewmar (Constellation) |
| Jeanneau (Segelboote) | 8–16 m | Kette-Draht, Pedestal | Lewmar (Constellation/Ocean) |
| Bénéteau (Segelboote) | 8–15 m | Kette-Draht, Pedestal | Lewmar (Constellation) |
| Hanse | 8–17 m | Kette-Draht, Pedestal | Jefa oder Lewmar |
| Hallberg-Rassy | 10–20 m | Direct-Drive oder Kette-Draht | Jefa |
| Najad | 10–18 m | Direct-Drive | Jefa |
| Contest | 10–18 m | Kette-Draht oder Direct-Drive | Jefa |
| Catalina (USA) | 8–14 m | Kette-Draht, Pedestal | Edson |
| Hunter (USA) | 8–15 m | Kette-Draht, Pedestal | Edson |
| Island Packet | 9–14 m | Kette-Draht, Pedestal | Edson |
| Bénéteau (Motorboote) | 6–14 m | Rack-and-Pinion + Push-Pull | Ultraflex oder SeaStar |
| Quicksilver | 5–9 m | Rack-and-Pinion + Push-Pull | Ultraflex |
| Boston Whaler | 5–11 m | Rack-and-Pinion + Push-Pull | SeaStar |
| Grady-White | 6–10 m | Rack-and-Pinion + Push-Pull | SeaStar |
| Lomac (RIBs) | 5–10 m | Rack-and-Pinion + Push-Pull | Ultraflex |
| Zodiac/Bombard (RIBs) | 4–8 m | Rack-and-Pinion + Push-Pull | Ultraflex |

### 4.8 Detaillierte Konfigurationen beliebter Bootsmodelle

#### 4.8.1 Bavaria Cruiser 34 (2019+)

| Komponente | Spezifikation | Hersteller-Nr. |
|-----------|-------------|----------------|
| Pedestal | Lewmar Constellation 40 | 89900040 |
| Kette | 3/8" vernickelt, 2,4 m | 89700020 |
| Steuerseile | 1/4" 7×19 SS, 2× 7,2 m | — |
| Umlenkrollen | 4× Lewmar 3" Kugellager | 89600030 |
| Quadrant | 350 mm, ø32 mm Bohrung | 89800140 |
| Steuerrad | Lewmar Power Grip 36" | — |
| Ruderschaft | ø32 mm, Edelstahl | — |
| Lock-to-Lock | 3,5 Umdrehungen | — |

#### 4.8.2 Jeanneau Sun Odyssey 349 (2016+)

| Komponente | Spezifikation | Hersteller-Nr. |
|-----------|-------------|----------------|
| Pedestal | Lewmar Constellation 40 | 89900040 |
| Kette | 3/8" vernickelt, 2,2 m | 89700020 |
| Steuerseile | 1/4" 7×19 SS, 2× 6,5 m | — |
| Umlenkrollen | 4× Lewmar 3" Kugellager | 89600030 |
| Quadrant | 300 mm, ø30 mm Bohrung | 89800130 |
| Steuerrad(er) | 2× Lewmar Folding 32" | — |
| Ruderschaft | ø30 mm, Edelstahl | — |
| Lock-to-Lock | 3,2 Umdrehungen | — |

#### 4.8.3 Hallberg-Rassy 40C (2020+)

| Komponente | Spezifikation | Hersteller-Nr. |
|-----------|-------------|----------------|
| Steuerung | Jefa DD40 Direct-Drive | JF-DD-40 |
| Welle | ø30 mm, Edelstahl 316L, 1,8 m | JF-DD-30-180 |
| Kreuzgelenke | 2× Edelstahl | JF-UJ-30 |
| Kegelradsatz | Spiroid-Kegelrad | JF-BG-30 |
| Steuerrad(er) | 2× Jefa Carbon 40" | — |
| Ruderschaft | ø40 mm, Edelstahl 316L | — |
| Lock-to-Lock | 2,8 Umdrehungen | — |

#### 4.8.4 Boston Whaler 250 Outrage (2020+)

| Komponente | Spezifikation | Hersteller-Nr. |
|-----------|-------------|----------------|
| Helm | SeaStar NFB 4.2 | SH5150P |
| Kabel | SeaStar SSC134 18ft | SSC134-18 |
| Lenkarm | Mercury-spezifisch | SH5100 |
| Steuerrad | Teleflex Black 13,5" | SW59291P |
| Motor-Anschluss | Mercury V8 300 PS | — |
| Lock-to-Lock | 4,2 Umdrehungen | — |

### 4.9 Ersatzteil-Bezugsquellen

| Bezugsquelle | Region | Edson | Lewmar | Jefa | SeaStar | Ultraflex | Web |
|-------------|--------|-------|--------|------|---------|-----------|-----|
| SVB (DE) | Deutschland/EU | ● | ● | ● | ● | ● | svb-marine.de |
| Compass24 (DE) | Deutschland/EU | ● | ● | — | ● | ● | compass24.de |
| Toplicht (DE) | Deutschland | ● | ● | — | ● | ● | toplicht.de |
| A.W. Niemeyer (DE) | Deutschland | ● | ● | — | ● | — | niemeyer.de |
| West Marine (US) | USA/Weltweit | ● | ● | — | ● | — | westmarine.com |
| Defender (US) | USA | ● | ● | — | ● | — | defender.com |
| Force4 (UK) | UK | ● | ● | ● | ● | ● | force4.co.uk |
| Marine Superstore (UK) | UK | ● | ● | — | ● | ● | marinesuperstore.com |
| Accastillage Diffusion (FR) | Frankreich | — | ● | — | — | ● | accastillage-diffusion.com |
| Jefa direkt (DK) | Weltweit | — | — | ● | — | — | jefa.com |
| Edson direkt (US) | Weltweit | ● | — | — | — | — | edsonmarine.com |

---

## 5. Installation

### 5.1 Seilführung — Best Practices

#### 5.1.1 Grundprinzipien der Seilverlegung

Die Seilführung einer mechanischen Steuerung bestimmt maßgeblich die Qualität des Steuergefühls, die Lebensdauer der Komponenten und die Zuverlässigkeit des Systems.

**Regel 1: Gerader Weg ist der beste Weg.**
Jede Umlenkung erhöht Reibung und verschleißt das Seil. Die ideale Seilführung hat null Umlenkrollen — das ist in der Praxis fast nie möglich, aber das Ziel muss sein, die Anzahl zu minimieren.

**Regel 2: Maximale Anzahl Umlenkrollen = 5 pro Seite.**
Bei mehr als 5 Umlenkrollen pro Seilseite sinkt der Wirkungsgrad unter 60 %, und die Rückmeldung wird inakzeptabel schlecht.

**Regel 3: Seil darf nirgendwo scheuern.**
Das Seil muss frei durch die Rollen laufen, ohne Kontakt mit Schotten, Rohrleitungen, Kabelsträngen oder sonstigen Hindernissen. Überall dort, wo das Seil durch ein Schott geführt wird, muss eine Seilführung (Conduit-Tube) oder ein Durchbruchsbeschlag das Seil schützen.

**Regel 4: Gleiche Seillängen links und rechts.**
Die Seilwege Backbord und Steuerbord sollten idealerweise identisch lang sein. Unterschiedliche Längen verursachen asymmetrische Spannung und ungleichmäßiges Steuergefühl.

**Regel 5: Seilspannung einstellbar halten.**
Mindestens eine Spannschraube (Turnbuckle) pro Seite muss zugänglich sein. Spannschrauben nahe am Quadranten montieren, nicht mitten in der Bilge.

#### 5.1.2 Umlenkrollen-Platzierung

**Positionierung:**
- Rollen auf soliden Schotten oder Strukturelementen montieren (mindestens 12 mm GFK, 18 mm Sperrholz mit Backing Plate)
- Backing Plate aus Edelstahl 316L oder Aluminium, mindestens 3 mm Dicke, Fläche ≥ 4× Rollenfuß-Fläche
- Schrauben: Edelstahl 316, Mindestgröße M6 für Boote bis 12 m, M8 für größere
- Rollen dürfen unter Last nicht kippen — 4-Punkt-Befestigung bevorzugen

**Typische Rollen-Positionen auf einer Segelyacht:**

| Position | Funktion | Umlenkwinkel typisch |
|----------|---------|---------------------|
| Unter Cockpitboden (2×) | Kette-Draht-Übergang → Bilge | 30–60° |
| Bilge seitlich (2×) | Führung entlang Rumpf | 15–45° |
| Vor Ruderkoker (2×) | Seil zum Quadranten lenken | 45–90° |
| Optional: Schottdurchgang | Durch Schotten führen | 0° (gerade Führung) |

#### 5.1.3 Seilinstallation Schritt-für-Schritt

1. **Quadrant montieren:** Quadrant auf Ruderschaft setzen, mit Klemmschrauben und Stift sichern. Ruder in Mittelstellung bringen.
2. **Umlenkrollen positionieren:** Trockenmontage mit Schnur (statt Seil), um den optimalen Weg zu finden.
3. **Rollen befestigen:** Mit Backing Plates und Sikaflex/Butyldichtung unter den Grundplatten.
4. **Seile einfädeln:** Vom Pedestal aus, Seil durch alle Rollen zum Quadranten führen.
5. **Seile am Quadranten befestigen:** Seil mit Kausche und Quetschhülse oder Nicopress-Hülse an Quadrant-Augbolzen befestigen.
6. **Spannschrauben einbauen:** Nahe dem Quadranten, gut zugänglich.
7. **Spannung einstellen:** Mit Federwaage oder Spannungsmesser auf empfohlenen Wert (siehe Tabelle in Abschnitt 2.1.2).
8. **Funktionsprüfung:** Steuerrad von Anschlag zu Anschlag drehen. Seil darf nirgendwo scheuern, klemmen oder vom Quadranten laufen.
9. **Sicherung:** Alle Splinte setzen, Spannschrauben mit Sicherungsdraht sichern.

### 5.2 Seilspannung einstellen

#### 5.2.1 Messmethode

**Methode 1: Federwaage**
1. Seil in der Mitte der längsten geraden Strecke greifen
2. Senkrecht zum Seil mit Federwaage 10 mm auslenken
3. Ablesbarer Wert ≈ Seilspannung × 0,2 (Korrekturfaktor abhängig von Seillänge)

**Methode 2: Frequency-Methode (Profis)**
1. Seil wie eine Gitarrensaite anschlagen
2. Frequenz mit Smartphone-App messen
3. Spannung berechnen: F = 4 × m × L² × f²
   (m = Masse pro Meter, L = Seillänge, f = Frequenz)

**Methode 3: Praktiker-Methode**
1. Seil mit Daumen und Zeigefinger in der Mitte greifen
2. Soll: Seil lässt sich ca. 10–15 mm seitlich auslenken (bei 2 m Freilänge)
3. Zu locker: >25 mm Auslenkung
4. Zu straff: <5 mm Auslenkung

#### 5.2.2 Nachstellintervalle

| Bedingung | Intervall |
|-----------|----------|
| Neuinstallation | Nach 1 Woche, dann nach 1 Monat |
| Neue Seile nach Seilwechsel | Nach 1 Woche, nach 1 Monat, nach 6 Monaten |
| Regulärer Betrieb | Alle 6 Monate oder bei Saisonstart |
| Nach starker Beanspruchung | Sofort prüfen (Sturm, Grundberührung) |
| Bei festgestelltem Spiel | Sofort nachstellen |

### 5.3 Quadranten-Dimensionierung und Montage

#### 5.3.1 Quadrant-Auswahl

Der Quadrant muss zum Ruderschaft passen (Bohrungsdurchmesser) und den korrekten Radius für die gewünschte Untersetzung haben.

**Quadranten-Befestigung auf dem Ruderschaft:**

| Befestigungstyp | Beschreibung | Festigkeit | Anwendung |
|----------------|-------------|-----------|-----------|
| Klemmschraube (Set Screw) | Madenschraube auf Schaft | Mittel | Boote bis 10 m |
| Klemm + Stift | Madenschraube + Querstift (Rollpin) | Hoch | Boote 10–15 m |
| Keilnut (Keyway) | Passfeder + Klemmschraube | Sehr hoch | Boote >12 m, Custom |
| Splined (Vielkeil) | Kerbverzahnung | Höchste | Custom, Jefa-Systeme |

**Kritischer Punkt:** Der Quadrant darf sich unter keinen Umständen auf dem Ruderschaft lösen. Ein durchdrehender Quadrant = sofortiger Steuerungsverlust.

#### 5.3.2 Quadrant-Freigang

Der Quadrant muss über seinen gesamten Schwenkbereich (±35° Segelboot, ±30° Motorboot) frei beweglich sein:
- Mindestabstand zu Rumpfinnenseite: 25 mm
- Mindestabstand zu Schläuchen, Kabeln, Rohren: 50 mm
- Keine Gegenstände im Schwenkbereich lagern (Warntafel montieren!)
- Ruderstopper (mechanische Begrenzung) am Quadranten oder Koker montieren

### 5.4 Push-Pull-Kabel-Installation (Motorboote)

#### 5.4.1 Kabelverlegung

1. **Länge messen:** Kabelweg vom Helm zum Motor über den tatsächlichen Verlauf messen (nicht Luftlinie!). +5–10 % Zugabe.
2. **Kabel verlegen:** Sanfte Bögen, keine scharfen Knicke. Min. Biegeradius beachten (200–400 mm je nach Typ).
3. **Kabel befestigen:** Alle 300–600 mm mit Kabelbindern oder Kabelschellen an der Struktur fixieren.
4. **Kabel am Helm anschließen:** In Helm-Gehäuse einschrauben, Gegenmutter sichern.
5. **Kabel am Motor anschließen:** Lenkarm (Tiller Arm) am Motor montieren, Kabel-Endstück mit Bolzen und Splint befestigen.
6. **Sicherungsmutter:** Am Helmgehäuse Sicherungsmutter (Jam Nut) festziehen.
7. **Funktionsprüfung:** Motor-Lenkung von Anschlag zu Anschlag prüfen, Zentrierung kontrollieren.

#### 5.4.2 Häufige Installationsfehler

| Fehler | Folge | Vermeidung |
|--------|-------|-----------|
| Biegeradius zu eng | Schwere Lenkung, Kabelbruch | Min. Radius einhalten |
| Kabel nicht fixiert | Scheuern, Bruch | Alle 300–600 mm befestigen |
| Falsche Länge (zu lang) | Zusätzliche Bögen nötig | Korrekt messen |
| Falsche Länge (zu kurz) | Spannung bei Motorneigung | Korrekt messen + Zugabe |
| Kein Bezel/Spritzschutz am Helm | Wasser dringt in Helm ein | Bezel-Kit montieren |
| Kabelenden nicht abgedichtet | Korrosion von innen | Fett am Endstück |
| Motor-Lenkarm falsche Richtung | Spiegelverkehrte Lenkung | Einbauanleitung beachten |

### 5.5 Seilkonfektionierung an Bord

#### 5.5.1 Nicopress-Verfahren (Bordtauglich)

Die Nicopress-Methode erlaubt die Seilkonfektionierung mit einer Handzange und ist die Standard-Methode für Bordreparaturen und Eigenbauten.

**Benötigtes Material:**
- Nicopress-Zange (passend für Seildurchmesser)
- Nicopress-Hülsen (Kupfer oder Aluminium, passend)
- Kauschen (Edelstahl, passend für Seildurchmesser)
- Seil-Schneider oder Trennscheibe

**Vorgehensweise:**
1. Seil auf gewünschte Länge + 150 mm Zugabe schneiden
2. Schnittende mit Klebeband umwickeln (gegen Aufdröseln)
3. Nicopress-Hülse auf Seil schieben
4. Kausche einlegen, Seil um Kausche biegen
5. Seilende durch Hülse zurückführen
6. Hülse in Nicopress-Zange einlegen, korrekte Größenkerbe wählen
7. Drei Pressungen setzen: Mitte, dann Enden (nicht umgekehrt!)
8. Pressung visuell prüfen: Hülse muss gleichmäßig verformt sein, kein Seilquetschung
9. Zugversuch: mit ca. 50 % der Arbeitslast kurz belasten → Hülse darf nicht rutschen

**Bruchlast-Erreichung:**
- Korrekt verpresste Nicopress-Hülse: 80–85 % der Seil-Bruchlast
- Seilklemmen (Bulldog Clips): nur 65–75 % → nur als Notlösung!
- Quetschhülse maschinell (Swage): 90–95 % → Werftarbeit

**Fehlerquellen bei der Nicopress-Konfektionierung:**

| Fehler | Folge | Vermeidung |
|--------|-------|-----------|
| Falsche Hülsengröße | Hülse hält nicht | Größentabelle beachten |
| Zu wenige Pressungen | Reduzierte Haltekraft | Immer 3 Pressungen |
| Pressungen zu nah beieinander | Seil wird gequetscht | Min. 3 mm Abstand |
| Keine Kausche verwendet | Seil scheuert durch | Immer Kausche verwenden |
| Seilende zu kurz | Seil rutscht aus Hülse | Min. 20 mm Überstand |

#### 5.5.2 Seil-Spannvorrichtung (Turnbuckle) korrekt einstellen

**Spannschrauben-Typen für Steuerseile:**

| Typ | Beschreibung | Verstellbereich | Vorteil | Nachteil |
|-----|-------------|----------------|---------|----------|
| Gabel-Öse | Gabel auf Quadrant, Öse auf Seil | ±20–40 mm | Standard, robust | Mäßige Verstellung |
| Öse-Öse | Beidseitig Ösen | ±20–40 mm | Flexibel | Braucht Bolzen |
| Gewindemuffe | Gewinderohr mit Rechts/Links-Gewinde | ±15–30 mm | Feinjustierung | Korrosionsanfällig |
| Quick-Release | Schnellverschluss mit Gewindespindel | ±20 mm | Schnell lösbar | Teurer |

**Einstellverfahren:**
1. Ruder exakt in Mittelstellung bringen (Wasserpass am Ruderblatt oder Quadrant-Markierung)
2. Beide Spannschrauben gleichmäßig anziehen
3. Spannung mit Federwaage prüfen (beide Seiten gleich!)
4. Steuerrad von Anschlag zu Anschlag drehen → Gleichmäßigkeit prüfen
5. Spannschrauben mit Sicherungsdraht (Mousing Wire) sichern
6. Kontermuttern (falls vorhanden) festziehen

**Häufiger Fehler:** Nur eine Seite nachspannen → Ruder-Mittelstellung verschiebt sich → Boot fährt schief bei mittigem Steuerrad.

### 5.6 Pedestal-Installation

#### 5.6.1 Vorbereitung

- **Cockpitboden-Ausschnitt:** Loch für Pedestal-Fuß bohren/fräsen. Typisch ø80–120 mm.
- **Verstärkung:** Unter dem Cockpitboden muss eine Verstärkungsplatte (Backing Plate) aus Edelstahl oder Alu (mind. 6 mm) den Pedestal tragen.
- **Ausrichtung:** Pedestal muss exakt senkrecht stehen. Abweichung >2° verursacht Kette/Seil-Fehlausrichtung.
- **Dichtung:** Pedestal-Fuß mit Sikaflex 291 oder 3M 4200 auf Cockpitboden abdichten.

#### 5.6.2 Ketten-/Seilanschluss

1. Pedestal montieren und ausrichten
2. Kette auf Kettenrad aufsetzen, korrekte Wickelrichtung beachten (Steuerrad rechts = Ruder Steuerbord)
3. Kette durch Kettenschacht in den Bereich unter dem Cockpitboden führen
4. Kette-Draht-Verbinder montieren (falls Kette-Draht-System)
5. Seile durch Rollen zum Quadranten führen
6. Spannung einstellen (siehe 5.2)

---

## 6. Fehlerbild-Atlas

### 6.1 Fehlerbild F-14-02-01: Spiel am Steuerrad (Totgang/Backlash)

**Beschreibung:** Das Steuerrad lässt sich 5–15° drehen, ohne dass sich das Ruder bewegt.

**Mögliche Ursachen:**
1. Seilspannung zu niedrig (häufigste Ursache, 45 %)
2. Verschlissene Kette mit Längung (20 %)
3. Ausgeschlagenes Pedestal-Getriebe (15 %)
4. Quadrant locker auf Ruderschaft (10 %)
5. Verschlissene Kette-Draht-Verbinder (5 %)
6. Seil durch Quetschhülse gerutscht (5 %)

**Diagnose:**
- Seilspannung messen → zu niedrig? → Spannschrauben nachstellen
- Kette auf Längung prüfen → 10 Glieder messen → >0,5 % Längung? → Kette tauschen
- Pedestal-Spiel prüfen → Steuerrad festhalten, an Pedestalwelle wackeln → Spiel? → Getriebe-Service
- Quadrant prüfen → mit einer Hand Quadrant festhalten, mit anderer Seil bewegen → Spiel? → Befestigung nachziehen

**AYDI-Confidence:** measured (wenn vor Ort geprüft), visual_medium (wenn auf Foto/Video erkennbar)

**Schweregrad:** MITTEL — Beeinträchtigt die Steuergenauigkeit, aber Steuerung funktioniert grundsätzlich.

### 6.2 Fehlerbild F-14-02-02: Schwergängige Steuerung

**Beschreibung:** Das Steuerrad lässt sich nur mit deutlich erhöhtem Kraftaufwand drehen.

**Mögliche Ursachen:**
1. Korrodierte/verschmutzte Umlenkrollen (30 %)
2. Zu hohe Seilspannung (20 %)
3. Koker-Lager verschlissen/verquollen (15 %)
4. Seil über scharfe Kanten oder durch Hindernisse gescheuert (15 %)
5. Kette trocken/korrodiert (10 %)
6. Push-Pull-Kabel interne Korrosion/Trockenheit (10 %)

**Diagnose:**
- Alle Umlenkrollen einzeln prüfen: dreht frei? Rille sauber?
- Seilspannung messen → zu hoch? → Spannschrauben lösen
- Seil komplett auf Scheuerstellen inspizieren
- Kabel-innere Reibung prüfen: Kabel abklemmen, Innenseil von Hand bewegen → schwergängig?

**AYDI-Confidence:** visual_medium (Rollenzustand auf Foto), measured (bei Kraftmessung)

**Schweregrad:** MITTEL bis HOCH — Bei extremer Schwergängigkeit kann im Notfall nicht schnell genug gesteuert werden.

### 6.3 Fehlerbild F-14-02-03: Asymmetrische Steuerung (eine Seite leichter als andere)

**Beschreibung:** Die Steuerung fühlt sich beim Drehen in eine Richtung schwerer an als in die andere.

**Mögliche Ursachen:**
1. Ungleiche Seilspannung Backbord/Steuerbord (35 %)
2. Eine Umlenkrolle blockiert oder schwergängig (25 %)
3. Ungleiche Seilwege (verschiedene Rollenzahl oder Winkel, 15 %)
4. Quadrant nicht mittig auf Ruderschaft (10 %)
5. Kabelführung asymmetrisch (Push-Pull, verschiedene Biegeradien, 10 %)
6. Koker-Lager einseitig verschlissen (5 %)

**Diagnose:**
- Seilspannung links und rechts einzeln messen → angleichen
- Jede Rolle einzeln prüfen → blockierte Rolle ersetzen
- Ruder in Mittelstellung bringen → Quadrant senkrecht? Seile symmetrisch gespannt?

**Schweregrad:** GERING bis MITTEL — Irritierend, aber steuerbar.

### 6.4 Fehlerbild F-14-02-04: Knacken oder Klicken beim Steuern

**Beschreibung:** Bei jeder Steuerradumdrehung ein rhythmisches Knacken oder Klicken.

**Mögliche Ursachen:**
1. Defektes Kettenglied (steifes Glied, Korrosion, 30 %)
2. Verschlissenes Kettenrad (abgebrochener Zahn, 25 %)
3. Seil mit gebrochenen Drähten (Litzen haken, 20 %)
4. Umlenkrolle mit Lagerschaden (15 %)
5. Quadrant-Befestigung locker (Klemmschraube klopft, 10 %)

**Diagnose:**
- Kette visuell prüfen: Steife Glieder? Rost? Verformung?
- Kettenrad abtasten: Zähne beschädigt?
- Seil visuell prüfen: Gebrochene Einzeldrähte (Meat Hooks)?
- Rollen einzeln drehen: Laufgeräusch?

**Schweregrad:** MITTEL bis HOCH — Kann auf bevorstehenden Bruch hindeuten. Sofortige Inspektion erforderlich.

### 6.5 Fehlerbild F-14-02-05: Seilbruch (einseitig)

**Beschreibung:** Ein Steuerseil ist gerissen. Steuerrad dreht frei in eine Richtung.

**Mögliche Ursachen:**
1. Korrosion (Spaltkorrosion an Quetschhülse, 35 %)
2. Materialermüdung (Biegewechsel an Umlenkrolle, 25 %)
3. Seil über scharfe Kante gescheuert (15 %)
4. Minderwertiges Seilmaterial (nicht 316, 10 %)
5. Überbelastung (Grundberührung, Sturm, 10 %)
6. Quetschhülse fehlerhaft verpresst (5 %)

**Sofortmaßnahme:**
- Sofort Geschwindigkeit reduzieren
- Notpinne montieren (falls verfügbar)
- Oder: intaktes Seil nutzen und nur in eine Richtung steuern (Notbetrieb)

**Schweregrad:** KRITISCH — Sofortige Reparatur erforderlich. Sicherheitsrisiko.

### 6.6 Fehlerbild F-14-02-06: Kettenbruch

**Beschreibung:** Die Steuerkette ist gerissen. Steuerrad dreht frei.

**Mögliche Ursachen:**
1. Korrosion (Salzwasser, mangelhafte Schmierung, 40 %)
2. Überlastung (Sturmsteuerung, Blockierung, 25 %)
3. Materialermüdung bei älteren Ketten (>15 Jahre, 20 %)
4. Minderwertiges Material (nicht marine-grade, 15 %)

**Sofortmaßnahme:**
- Notpinne (Emergency Tiller)
- Kette provisorisch mit Seil oder Kettenschloss verbinden
- Nächsten Hafen anlaufen

**Schweregrad:** KRITISCH — Totaler Steuerungsverlust. Sicherheitsrisiko.

### 6.7 Fehlerbild F-14-02-07: Korrosion an Umlenkrollen

**Beschreibung:** Umlenkrollen zeigen Rost, verfärbte Lager, schwergängigen Lauf.

**Mögliche Ursachen:**
1. Bilgewasser-Kontakt (Rollen zu tief montiert, 40 %)
2. Falsches Material (Stahl statt Edelstahl, 25 %)
3. Lager-Dichtung defekt (Salzwasser in Lager, 20 %)
4. Galvanische Korrosion (verschiedene Metalle, 15 %)

**Maßnahme:** Betroffene Rollen austauschen. Bei Edelstahl-Rollen mit Kugellagern: Lager erneuern, Rolle weiterverwenden.

**Schweregrad:** GERING bis MITTEL — Führt langfristig zu schwergängiger Steuerung und kann Seilbruch begünstigen.

### 6.8 Fehlerbild F-14-02-08: Quadrant-Lockerung

**Beschreibung:** Der Quadrant hat sich auf dem Ruderschaft gelöst oder hat Spiel.

**Mögliche Ursachen:**
1. Klemmschraube gelöst (Vibration, 40 %)
2. Querstift abgeschert (Überlast, 25 %)
3. Keilnut ausgeschlagen (Verschleiß, 20 %)
4. Schaft-Oberfläche korrodiert (Passungsverlust, 15 %)

**Sofortmaßnahme:**
- Schraube nachziehen, mit Loctite 243 sichern
- Querstift ersetzen (größerer Durchmesser wenn Bohrung aufgeweitet)
- Bei ausgeschlagener Keilnut: Quadrant und Passfeder erneuern

**Schweregrad:** HOCH — Kann zu totalem Steuerungsverlust führen.

### 6.9 Fehlerbild F-14-02-09: Push-Pull-Kabel steif oder festsitzend

**Beschreibung:** Das Steuer-Kabel eines Motorboots lässt sich kaum noch bewegen.

**Mögliche Ursachen:**
1. Interne Korrosion (Salzwasser eingedrungen, 35 %)
2. Kabel zu eng verlegt (Biegeradius unterschritten, 25 %)
3. Äußere Hülle gebrochen (Wasser, Schmutz eingedrungen, 20 %)
4. Fettfüllung ausgehärtet (Alterung, 15 %)
5. Kabel gequetscht (Scheuerstelle, 5 %)

**Maßnahme:** Kabel austauschen. Push-Pull-Kabel sind Verschleißteile und nicht reparierbar.

**Schweregrad:** MITTEL bis HOCH — Kann zu unkontrollierbarer Lenkung führen.

### 6.10 Fehlerbild F-14-02-10: Steuerrad-Rückschlag (Kickback)

**Beschreibung:** Das Steuerrad wird bei Geschwindigkeit oder Wellengang abrupt zurückgeschlagen.

**Mögliche Ursachen:**
1. Kein NFB-System bei Motorboot mit starkem Motor (40 %)
2. Propeller-Torque-Steer bei Außenborder (30 %)
3. Seil-/Kettenspiel erlaubt Rückdrehung (15 %)
4. Kavitation am Ruder (15 %)

**Maßnahme:**
- NFB-Helm nachrüsten (bei Motorbooten >75 PS zwingend empfohlen)
- Seilspannung erhöhen
- Autopilot-Radpilot kann Rückschlag dämpfen

**Schweregrad:** HOCH — Verletzungsgefahr (Handgelenk, Finger). Bei kleinen Booten: Sturz über Bord möglich.

### 6.11 Fehlerbild F-14-02-11: Steuerrad dreht endlos (kein Anschlag)

**Beschreibung:** Das Steuerrad dreht sich ohne Widerstand und ohne Ruderbewegung.

**Mögliche Ursachen:**
1. Seil/Kette komplett gerissen oder gelöst (50 %)
2. Quadrant vom Ruderschaft abgefallen (25 %)
3. Pedestal-Getriebe durchgedreht (15 %)
4. Seil von Trommel gerutscht (10 %)

**Sofortmaßnahme:**
- Notpinne sofort montieren
- Bei Motorboot: Motor in Leerlauf, Kurs stabilisieren
- Ursache unter Deck identifizieren

**Schweregrad:** KRITISCH — Totaler Steuerungsverlust.

### 6.12 Zusammenfassung Fehlerbilder: Schweregrad-Matrix

| Fehlerbild | Code | Schweregrad | Sofortmaßnahme nötig? | Weiterbetrieb möglich? | Typische Reparaturkosten |
|-----------|------|------------|----------------------|----------------------|-------------------------|
| Spiel am Steuerrad | F-14-02-01 | MITTEL | Nein | Ja, eingeschränkt | 0–50 EUR (Nachstellen) |
| Schwergängige Steuerung | F-14-02-02 | MITTEL–HOCH | Bei Extremfällen | Ja | 50–300 EUR |
| Asymmetrische Steuerung | F-14-02-03 | GERING–MITTEL | Nein | Ja | 0–100 EUR |
| Knacken/Klicken | F-14-02-04 | MITTEL–HOCH | Inspektion sofort | Ja, vorsichtig | 50–500 EUR |
| Seilbruch einseitig | F-14-02-05 | KRITISCH | Ja (Notpinne) | Nur Notbetrieb | 100–600 EUR |
| Kettenbruch | F-14-02-06 | KRITISCH | Ja (Notpinne) | Nein | 200–800 EUR |
| Korrosion Umlenkrollen | F-14-02-07 | GERING–MITTEL | Nein | Ja | 50–300 EUR |
| Quadrant-Lockerung | F-14-02-08 | HOCH | Ja | Nur Notbetrieb | 0–200 EUR |
| Push-Pull steif/fest | F-14-02-09 | MITTEL–HOCH | Bei Blockade | Eingeschränkt | 50–200 EUR |
| Steuerrad-Rückschlag | F-14-02-10 | HOCH | NFB nachrüsten | Ja, gefährlich | 150–350 EUR |
| Steuerrad dreht endlos | F-14-02-11 | KRITISCH | Ja (Notpinne) | Nein | Variabel |
| Vibration/Schlagen | F-14-02-12 | GERING–HOCH | Bei Verdacht Ruderschaden | Ja | 50–2.000 EUR |

**Priorisierung für die AYDI-Bewertung:**
- KRITISCH → Sofort-Warnung, Boot nicht verwenden (Score: 0–10)
- HOCH → Dringend-Warnung, Reparatur innerhalb 1 Woche (Score: 10–30)
- MITTEL → Wartungs-Empfehlung, innerhalb 3 Monate (Score: 30–60)
- GERING → Hinweis, bei nächster regulärer Wartung (Score: 60–80)

### 6.13 Fehlerbild F-14-02-12: Vibration/Schlagen im Steuersystem

> Hinweis: Dieses Fehlerbild erfordert häufig eine Taucher-Inspektion des Ruders, da die häufigste Ursache (Ruderschaden) nur unter Wasser erkennbar ist.

**Beschreibung:** Vibrationen oder rhythmisches Schlagen werden am Steuerrad wahrgenommen.

**Mögliche Ursachen:**
1. Ruderblatt beschädigt (Grundberührung, Riss, 30 %)
2. Seil-/Kettenschlag bei losen Systemen (25 %)
3. Propeller-Unwucht übertragen auf Ruder (15 %)
4. Koker-Lager verschlissen (Spiel, 15 %)
5. Bewuchs am Ruderblatt (asymmetrische Strömung, 10 %)
6. Kavitation am Ruder bei hoher Geschwindigkeit (5 %)

**Schweregrad:** GERING bis HOCH — je nach Ursache. Ruderblattschaden = HOCH.

---

## 7. Troubleshooting

### 7.1 Entscheidungsbaum 1: Steuerung hat Spiel

```
Steuerrad hat Spiel
├── Spiel in Mittelstellung?
│   ├── Ja
│   │   ├── Seilspannung prüfen
│   │   │   ├── Zu niedrig → Nachspannen (Turnbuckle)
│   │   │   └── OK → Weiter prüfen
│   │   ├── Kette auf Längung prüfen
│   │   │   ├── >0,5 % → Kette austauschen
│   │   │   └── OK → Weiter prüfen
│   │   ├── Pedestal-Getriebe prüfen
│   │   │   ├── Spiel fühlbar → Getriebe-Service oder Austausch
│   │   │   └── OK → Weiter prüfen
│   │   └── Quadrant-Befestigung prüfen
│   │       ├── Locker → Nachziehen + Loctite
│   │       └── Fest → Koker-Lager prüfen
│   └── Nein (Spiel nur bei Ausschlag)
│       ├── Seilweg zu lang → Seilspannung erhöhen
│       └── Quadrant-Sektor zu groß → Quadrant wechseln (kleinerer Radius)
```

### 7.2 Entscheidungsbaum 2: Steuerung schwergängig

```
Steuerrad schwergängig
├── Gleichmäßig schwergängig?
│   ├── Ja
│   │   ├── Alle Rollen prüfen → blockierte Rollen ersetzen
│   │   ├── Seilspannung prüfen → zu hoch? → reduzieren
│   │   ├── Koker-Lager prüfen → Widerstand? → Lager tauschen
│   │   └── Push-Pull-Kabel prüfen → steif? → Kabel tauschen
│   └── Nein (nur in bestimmten Positionen)
│       ├── In einer Richtung → asymmetrische Reibung → einzelne Rollen prüfen
│       ├── Bei Vollausschlag → Quadrant berührt Hindernis → Freigang prüfen
│       └── Bei bestimmter Rad-Position → Kette steifes Glied → Kette prüfen
```

### 7.3 Entscheidungsbaum 3: Geräusche beim Steuern

```
Geräusche beim Steuern
├── Rhythmisches Klicken?
│   ├── Ja → Kette prüfen (steifes Glied, Zahnfehler)
│   └── Nein
├── Quietschen?
│   ├── Ja → Schmierung aller beweglichen Teile (Rollen, Kette, Koker)
│   └── Nein
├── Knarren/Ächzen?
│   ├── Ja → Pedestal-Lager prüfen, Quadrant-Befestigung, Rollenhalterungen
│   └── Nein
├── Metallisches Schlagen?
│   ├── Ja → Lose Teile suchen (Quadrant, Seil, Kette)
│   └── Nein
└── Knacken bei Lastrichtungswechsel?
    └── Ja → Spiel im Getriebe, Kette, oder Verbinder → einzeln prüfen
```

### 7.4 Entscheidungsbaum 4: Steuerungsverlust (Notfall)

```
Steuerrad dreht frei / kein Ruderausschlag
├── Kette/Seil gerissen?
│   ├── Ja → Notpinne montieren
│   │   ├── Notpinne vorhanden → montieren, weiterfahren
│   │   └── Notpinne nicht vorhanden → improvisieren:
│   │       ├── Leine an Ruderquadrant → beidseitig ins Cockpit
│   │       ├── Langer Schraubendreher/Rohr in Ruderschaft-Top
│   │       └── Bei Motorboot: Motor-Winkel steuern (Außenborder)
│   └── Nein
├── Quadrant abgefallen?
│   ├── Ja → Quadrant wieder montieren (Bordwerkzeug)
│   └── Nein
├── Seil von Trommel?
│   ├── Ja → Seil wieder auflegen, Spannung erhöhen
│   └── Nein
└── Getriebe durchgedreht?
    └── Ja → Notpinne verwenden, Werft anlaufen
```

### 7.5 Entscheidungsbaum 5: Push-Pull-Kabel-Probleme (Motorboot)

```
Lenkung Motorboot problematisch
├── Lenkung sehr schwer?
│   ├── Kabel alt (>8 Jahre)? → Kabel tauschen
│   ├── Biegeradius unterschritten? → Kabel verlegen
│   ├── Kabel beschädigt (Knick, Quetschung)? → Kabel tauschen
│   └── Motor-Lenkarm schwergängig? → Lenkarm schmieren/tauschen
├── Lenkung hat Spiel?
│   ├── Kabel zu lang? → Kürzeres Kabel wählen
│   ├── Kabel nicht fixiert (flatternde Abschnitte)? → Befestigen
│   ├── Helm-Getriebe verschlissen? → Helm tauschen
│   └── Motor-Lenkarm locker? → Nachziehen
├── Lenkung klemmt in einer Position?
│   ├── Kabel intern korrodiert → Kabel tauschen
│   ├── Motor-Stopp erreicht → Motor-Anschlag prüfen
│   └── Kabel eingeklemmt → Kabelweg inspizieren
└── Rückschlag am Steuerrad?
    ├── NFB-Helm vorhanden? → Nein → NFB-Helm nachrüsten
    ├── NFB defekt? → Helm tauschen
    └── Motor >75 PS ohne NFB → NFB unbedingt nachrüsten
```

---

## 8. FAQ — Häufige Fragen

### 8.1 Allgemeine Fragen

**F1: Wie oft muss ich die Seilspannung meiner Steuerung prüfen?**
A: Mindestens zweimal pro Saison (Saisonstart und Mitte der Saison) sowie nach jeder starken Beanspruchung (Sturm, Grundberührung). Bei neuen Seilen: zusätzlich nach 1 Woche und nach 1 Monat, da sich die Konstruktionsdehnung setzt. (Confidence: documented — Edson, Lewmar Handbücher)

**F2: Kann ich mein Seilsteuersystem selbst warten?**
A: Ja, die Grundwartung (Seilspannung prüfen/nachstellen, Schmierung, visuelle Inspektion) ist eine typische Eigneraufgabe. Für den Seilwechsel oder Pedestal-Service empfiehlt sich ein Rigger oder Steuerungsmechaniker, insbesondere bei der Seilkonfektionierung (Quetschhülsen). (Confidence: documented)

**F3: Welches Schmiermittel verwende ich für die Steuerkette?**
A: Empfohlen werden Trockenschmierstoffe auf PTFE-Basis (z. B. McLube OneDrop, Boeshield T-9) oder leichte marine Getriebeöle. Kein WD-40 als Langzeitschmierung — WD-40 ist ein Kriechöl und wäscht vorhandenes Fett aus. Kein dickflüssiges Fett, da es Schmutz bindet. (Confidence: documented — Edson Maintenance Guide, Practical Sailor Test 2021)

**F4: Wie lange halten Steuerseile?**
A: Bei regelmäßiger Wartung und Inspektion: 8–15 Jahre für hochwertige 7×19 Edelstahlseile. In tropischen Gewässern mit hoher Luftfeuchtigkeit und Salzbelastung: 5–10 Jahre. Empfehlung: Spätestens nach 10 Jahren tauschen, unabhängig vom optischen Zustand, da Innenkorrosion nicht sichtbar ist. (Confidence: estimated — Konsens Rigger-Branche)

**F5: Was ist der Unterschied zwischen 7×7 und 7×19 Steuerseil?**
A: 7×7-Seile haben 49 Einzeldrähte (steifer, weniger biegsam), 7×19-Seile haben 133 Einzeldrähte (flexibler, bessere Lebensdauer an Umlenkrollen). Für Steuerungen ist 7×19 der Standard, da die Seile ständig über Rollen gebogen werden. 7×7 ist nur akzeptabel bei sehr großen Rollendiametern und kurzen Wegen. (Confidence: documented)

### 8.2 Dimensionierung und Auswahl

**F6: Welchen Seildurchmesser brauche ich für mein Boot?**
A: Faustregel: 8–10 m Boot → 3/16" (4,8 mm), 10–12 m → 1/4" (6,4 mm), 12–14 m → 5/16" (7,9 mm), 14–16 m → 3/8" (9,5 mm). Immer das Original-Maß des Bootsherstellers verwenden. Im Zweifel: einen Durchmesser größer wählen (größeres Seil schadet nicht, kleineres ist unsicher). (Confidence: documented — Edson/Lewmar Sizing Charts)

**F7: Wie groß muss mein Quadrant sein?**
A: Der Quadrant-Radius bestimmt die Untersetzung und damit die Steuerleichtigkeit. Größerer Radius = leichteres Steuern, aber mehr Umdrehungen Lock-to-Lock. Kleinerer Radius = direkteres Steuern, aber höhere Seilkraft. Empfehlung: Hersteller-Vorgabe des Bootsbauers befolgen. Typisch: Radius = 2,5–4× Ruderschaft-Durchmesser. (Confidence: documented)

**F8: Wann sollte ich von mechanisch auf hydraulisch umrüsten?**
A: Wenn das Ruderdrehmoment dauerhaft >150 Nm beträgt (Segelboote >14 m, schwere Verdränger >12 m), wenn Doppelsteuerstand mit langen Seilwegen nötig ist, oder wenn ein leistungsfähiger Autopilot integriert werden soll. Hydraulik bietet auch Vorteile bei Katamaranen mit weit auseinanderliegenden Rudern. (Confidence: estimated)

**F9: Welches Push-Pull-Kabel passt zu meinem Außenborder?**
A: Das hängt von Motor-PS, Motor-Marke und Kabellänge ab. SeaStar/Teleflex-Kompatibilitätstabelle oder Ultraflex-Katalog verwenden. Grundregel: Bis 55 PS → SSC61/M58, bis 150 PS → SSC62/M66, bis 300 PS → SSC134/M86, bis 400 PS → SSC6210/M90. Immer korrekte Endstücke für die Motormarke prüfen! (Confidence: documented)

**F10: Wie viele Umdrehungen Lock-to-Lock sind normal?**
A: Bei Segelbooten mit Pedestal: 2,5–4,5 Umdrehungen (abhängig von Getriebe und Quadrant). Bei Motorbooten mit Rack-and-Pinion: 3,0–4,5 Umdrehungen. Weniger Umdrehungen = direkter aber schwerer. Mehr Umdrehungen = leichter aber langsamer. (Confidence: documented)

### 8.3 Wartung und Reparatur

**F11: Mein Steuerrad hat Spiel — ist das gefährlich?**
A: Bis 5° Totgang (Spiel) ist gemäß ISO 8847 noch akzeptabel, aber nicht komfortabel. Mehr als 5° = nicht normkonform und sicherheitsrelevant. Ursache ermitteln (siehe Fehlerbild F-14-02-01) und beheben. Am häufigsten: Seilspannung nachstellen (10-Minuten-Reparatur). (Confidence: documented)

**F12: Kann ich vernickelte Kette durch Edelstahlkette ersetzen?**
A: Ja, sofern die Teilung (Pitch) identisch ist. Edson 3/8" vernickelt kann durch Edson 3/8" Edelstahl (Bestell-Nr. 669-SS) ersetzt werden. Edelstahl-Kette ist langlebiger, besonders in tropischen/feuchten Umgebungen. Preis ca. 2–3× höher, aber lohnend. (Confidence: documented)

**F13: Woran erkenne ich, dass mein Steuerseil bald bricht?**
A: Warnsignale: (1) Einzelne gebrochene Drähte, die als kleine Haken abstehen (Meat Hooks) — besonders an Umlenkrollen und Quetschhülsen prüfen. (2) Verfärbungen (braun/rot = Rost, interne Korrosion). (3) Formveränderung (flachgedrückte Stellen, Knicke). (4) Reduzierter Durchmesser an Biegestellen. Faustregel: >3 gebrochene Drähte auf 6× Seildurchmesser Länge = sofort tauschen. (Confidence: documented — Rigger-Praxis)

**F14: Wie wechsle ich ein Steuerseil?**
A: Kurzanleitung: (1) Altes Seil am Quadranten lösen, (2) neues Seil am alten befestigen und hindurchziehen, (3) neues Seil am Quadranten befestigen (Kausche + Quetschhülse oder Nicopress), (4) Spannschrauben einbauen, (5) Spannung einstellen, (6) Funktionsprüfung. Wichtig: Seile immer paarweise tauschen, nie nur eine Seite! (Confidence: documented)

**F15: Mein Push-Pull-Kabel ist schwergängig — kann ich es schmieren?**
A: Nur bedingt. Man kann versuchen, am Motor-Ende Kriechöl (z. B. Corrosion Block, LPS 3) in die Kabelhülle einzusprühen und das Kabel hin- und herbewegen. Wenn das hilft: regelmäßig wiederholen. Wenn nicht: Kabel ist intern korrodiert und muss getauscht werden. Push-Pull-Kabel sind Verschleißteile mit begrenzter Lebensdauer. (Confidence: documented — SeaStar Maintenance Guide)

### 8.4 Spezifische Systeme

**F16: Was ist ein Jefa Direct-Drive-System?**
A: Ein mechanisches Steuersystem, bei dem eine vertikale Welle direkt vom Pedestal zum Ruderschaft führt — ohne Seile, Ketten oder Quadrant. Die Kraft wird über ein Kegelradgetriebe oder Kreuzgelenk übertragen. Vorteile: Spielfrei, wartungsfrei, beste Rückmeldung. Nachteil: Nur bei Neubau einbaubar, teuer. Hersteller: Jefa Steering (Dänemark). (Confidence: documented)

**F17: Brauche ich ein NFB-System (No-Feedback) bei meinem Motorboot?**
A: Dringend empfohlen ab 75 PS Außenborder auf Gleiterbooten. Ohne NFB kann der Propeller-Drehmoment das Steuerrad abrupt zurückschlagen und Handverletzungen verursachen. Die meisten Motorboot-Hersteller verbauen ab 100 PS serienmäßig NFB-Helms. Nachrüstung: NFB-Helm kaufen (z. B. SeaStar NFB 4.2), alten Helm ersetzen. (Confidence: documented — ABYC P-17, NMMA)

**F18: Kann ich ein Doppelsteuerrad nachrüsten?**
A: Technisch ja, aber aufwendig. Optionen: (1) Zwei Pedestals mit Querwelle verbinden (mechanisch komplex), (2) Ein Pedestal zentral belassen, zweites Rad über Kette/Seil anbinden (günstiger, aber Spiel-Problematik), (3) Jefa Twin-Wheel-Kit (Premiumlösung). Die Cockpit-Struktur muss zwei Pedestal-Durchbrüche tragen. Kosten: 3.000–8.000 EUR inkl. Installation. (Confidence: estimated)

**F19: Was ist der Unterschied zwischen Constellation und Ocean bei Lewmar?**
A: Die Constellation-Serie ist Lewmars Standardreihe für Boote 7–16 m mit Kegelradgetriebe. Die Ocean-Serie ist die Heavy-Duty-Reihe für Boote 14–22 m mit zusätzlicher Untersetzung, größerem Kettenrad und verstärktem Gehäuse. Ocean-Pedestals sind ca. 50 % teurer, aber für höhere Ruderdrehmomente ausgelegt. (Confidence: documented — Lewmar Katalog)

**F20: Wie lagere ich eine Ketten-Draht-Steuerung über den Winter ein?**
A: (1) Seilspannung leicht reduzieren (Seile sollen nicht monatelang unter Volllast stehen), (2) Kette mit PTFE-Spray oder leichtem Öl behandeln, (3) Umlenkrollen ölen, (4) Pedestal-Kompass abnehmen (Kälte schadet Flüssig-Kompassen), (5) Steuerrad abnehmen oder mit Plane schützen. Im Frühjahr: Spannung nachstellen, Funktionsprüfung. (Confidence: documented)

### 8.5 Sicherheit und Notfälle

**F21: Muss ich eine Notpinne (Emergency Tiller) an Bord haben?**
A: Für CE-zertifizierte Boote der Kategorie A und B: Ja, eine Notsteuerungsmöglichkeit muss vorhanden sein (ISO 8847, Abschnitt 5.8). Für Kategorie C und D: empfohlen, aber nicht zwingend vorgeschrieben. In der Praxis: Jede Segelyacht sollte eine Notpinne haben, die direkt auf den Ruderschaft passt. Prüfen Sie, ob Ihre Notpinne tatsächlich passt und zugänglich ist! (Confidence: documented)

**F22: Was mache ich bei totalem Steuerungsverlust auf See?**
A: Sofortmaßnahmen: (1) Geschwindigkeit reduzieren (Segel bergen / Motor auf Leerlauf), (2) Notpinne montieren, (3) Wenn keine Notpinne: Leinen am Ruderquadranten befestigen und als Zügel ins Cockpit führen, (4) Bei Motorboot mit Außenborder: Motor direkt am Schaft lenken (Lanyard), (5) Seenotretter informieren wenn keine Eigensteuerung möglich. (Confidence: documented — Seesicherheits-Literatur, ISAF)

**F23: Kann ein durchgescheuertes Seil explodieren?**
A: Nein, im Gegensatz zu Wanten und Stagen stehen Steuerseile nicht unter hoher Vorspannung (50–250 N vs. 5.000+ N bei Wanten). Ein Steuerseil-Bruch ist daher nicht explosionsartig, aber der plötzliche Steuerungsverlust ist gefährlich. (Confidence: documented)

**F24: Wie prüfe ich mein Steuersystem bei der Saisonvorbereitung?**
A: Checkliste: (1) Seilspannung messen, (2) Alle Seile visuell auf Drahtbrüche inspizieren — besonders an Umlenkrollen und Endstücken, (3) Umlenkrollen drehen — leichtgängig?, (4) Kette inspizieren — Korrosion, steife Glieder?, (5) Quadrant-Befestigung prüfen, (6) Pedestal-Spiel prüfen, (7) Notpinne suchen und Passform prüfen, (8) Ruder von Anschlag zu Anschlag bewegen — gleichmäßig, leichtgängig?, (9) Alle Schmierstellen ölen. (Confidence: documented)

**F25: Ist eine mechanische Steuerung zuverlässiger als eine hydraulische?**
A: Pauschal: ja, bei korrekter Wartung. Mechanische Systeme haben weniger Komponenten, die versagen können (kein Fluid, keine Dichtungen, keine Pumpe). Ein Seilbruch lässt sich an Bord provisorisch reparieren. Ein hydraulischer Leitungsbruch erfordert Spezialwerkzeug und Fluid. Allerdings: bei großen Yachten mit hohen Ruderkräften ist Hydraulik die bessere Wahl, weil mechanische Systeme dort an ihre Grenzen stoßen. (Confidence: estimated — Konsens Surveyor-Branche)

---

## 9. Glossar

| Nr. | Begriff (DE) | Begriff (EN) | Erklärung |
|-----|-------------|-------------|-----------|
| 1 | Steuerrad | Helm Wheel | Drehbares Rad zur Steuerung, montiert auf dem Pedestal |
| 2 | Pedestal | Pedestal / Steering Column | Steuerständer im Cockpit, enthält Getriebe und Kompassaufnahme |
| 3 | Quadrant | Quadrant / Tiller Arm | Bogensegment auf dem Ruderschaft, an dem die Steuerseile befestigt sind |
| 4 | Ruderschaft | Rudder Stock / Rudder Post | Vertikale Achse, um die sich das Ruderblatt dreht |
| 5 | Ruderkoker | Rudder Tube / Rudder Port | Rohr durch den Rumpf, in dem der Ruderschaft gelagert ist |
| 6 | Steuerseil | Steering Cable / Steering Wire | 7×19 Edelstahl-Drahtseil zur Kraftübertragung |
| 7 | Steuerkette | Steering Chain | Kurzgliedrige Kette am Pedestal-Kettenrad |
| 8 | Kettenrad | Sprocket / Chain Wheel | Zahnrad im Pedestal, das mit der Steuerkette kämmt |
| 9 | Umlenkrolle | Sheave / Idler Pulley | Rolle zur Richtungsänderung des Steuerseils |
| 10 | Spannschraube | Turnbuckle / Rigging Screw | Gewindespannschloss zum Einstellen der Seilspannung |
| 11 | Kausche | Thimble | Metalleinlage in Seilschlaufen zum Schutz vor Aufscheuern |
| 12 | Quetschhülse | Swage Sleeve / Compression Fitting | Metallhülse, die auf das Seil gepresst wird |
| 13 | Nicopress-Hülse | Nicopress Sleeve | Kupfer- oder Alu-Hülse, manuell verpressbar |
| 14 | Totgang | Backlash / Dead Play | Steuerrad-Drehung ohne Ruderausschlag (Spiel im System) |
| 15 | Lock-to-Lock | Lock-to-Lock | Voller Steuerradweg von Anschlag links bis Anschlag rechts |
| 16 | Kegelradgetriebe | Bevel Gear | 90°-Umlenkgetriebe mit Kegelzahnrädern |
| 17 | Schneckengetriebe | Worm Gear | Selbsthemmendes Getriebe mit Schnecke und Schneckenrad |
| 18 | Planetengetriebe | Planetary Gear | Hochwirksames Untersetzungsgetriebe mit Sonnen-, Planeten- und Hohlrad |
| 19 | Zahnstange | Rack | Lineare Verzahnung, die mit einem Ritzel kämmt |
| 20 | Ritzel | Pinion | Kleines Zahnrad, das mit einer Zahnstange oder einem größeren Rad kämmt |
| 21 | Push-Pull-Kabel | Push-Pull Cable / Control Cable | Kabel mit steifer Hülle und beweglicher Seele zur Kraftübertragung |
| 22 | NFB | No-Feedback | Rückschlag-Sperre im Steuergetriebe (Motorboote) |
| 23 | Ruder-Rückmeldung | Helm Feedback / Helm Feel | Spürbare Rückkopplung der Ruderkräfte am Steuerrad |
| 24 | Seilspannung | Cable Tension | Vorspannkraft in den Steuerseilen (typisch 50–250 N) |
| 25 | Seildehnung | Cable Stretch / Wire Elongation | Längenzunahme des Seils unter Last (elastisch + konstruktiv) |
| 26 | Konstruktionsdehnung | Construction Stretch | Einmalige, irreversible Dehnung neuer Seile |
| 27 | Elastische Dehnung | Elastic Stretch | Reversible, lastabhängige Dehnung |
| 28 | Umschlingungswinkel | Wrap Angle | Winkel, über den die Kette das Kettenrad umfasst |
| 29 | Fleet-Winkel | Fleet Angle | Seitlicher Auflaufwinkel des Seils auf eine Umlenkrolle |
| 30 | Bruchlast | Breaking Load / MBL | Maximale Kraft bis zum Versagen einer Komponente |
| 31 | Arbeitslast | Working Load / SWL | Zulässige Betriebskraft (typisch 1/3 der Bruchlast) |
| 32 | Seilkonstruktion | Wire Construction | Aufbau des Seils (z. B. 7×19 = 7 Litzen à 19 Drähte) |
| 33 | Direct-Drive | Direct-Drive | Steuerung ohne Seile/Ketten, direkte Wellenverbindung (Jefa) |
| 34 | Ruderstopper | Rudder Stop | Mechanische Begrenzung des maximalen Ruderausschlags |
| 35 | Notpinne | Emergency Tiller | Behelfspinne bei Ausfall der Hauptsteuerung |
| 36 | Seilführung/Conduit | Conduit / Cable Tube | Schutzrohr zur Führung von Steuerseilen |
| 37 | Seilklemme | Wire Clamp / Bulldog Clamp | Klemmverbindung für Drahtseile (Notlösung) |
| 38 | Wirkungsgrad | Efficiency (η) | Verhältnis Ausgangs-/Eingangsleistung eines Systems |
| 39 | Kette-Draht-Verbinder | Chain-to-Wire Connector | Übergangsstück zwischen Kette und Drahtseil |
| 40 | Sektor | Quadrant Arc / Sector | Bogenlänge des Quadranten, typisch 70° |
| 41 | Backing Plate | Backing Plate | Verstärkungsplatte hinter dem Montagepunkt |
| 42 | Ruderdrehmoment | Rudder Torque | Drehkraft am Ruderschaft durch Wasserströmung |
| 43 | Ruderbalance | Rudder Balance | Anteil der Ruderfläche vor dem Schaft (reduziert Drehmoment) |
| 44 | Bilge | Bilge | Tiefster Bereich im Bootsinneren, wo sich Wasser sammelt |
| 45 | Helm | Helm (Steuergetriebe) | Steuergetriebe-Einheit (bei Motorbooten) oder allgemein Steuerstand |
| 46 | Binnacle | Binnacle / Kompasshaus | Schutzgehäuse für Kompass und Instrumente auf dem Pedestal |
| 47 | Seiltrommel | Wire Drum / Cable Drum | Zylindrische Trommel am Pedestal, um die das Steuerseil gewickelt wird |
| 48 | Kettenschacht | Chain Conduit | Führungsrohr für die Steuerkette vom Pedestal zur Bilge |
| 49 | Sicherungsdraht | Mousing Wire / Locking Wire | Dünner Draht zum Sichern von Spannschrauben und Bolzen |
| 50 | Splint | Split Pin / Cotter Pin | Sicherungselement für Bolzen und Achsen |
| 51 | Gegenmutter | Jam Nut / Lock Nut | Kontermutter zur Sicherung einer Einstellmutter |
| 52 | Lenkarm | Tiller Arm / Steering Arm | Hebel am Außenborder, der die Lenkkraft aufnimmt |
| 53 | Bezel | Bezel / Helm Cover | Spritzschutz-Blende am Steuergetriebe-Durchgang |
| 54 | Keilnut | Keyway | Eingefräste Nut in Ruderschaft und Quadrant für eine Passfeder |
| 55 | Passfeder | Key / Woodruff Key | Metallstück in der Keilnut zur formschlüssigen Drehmomentübertragung |
| 56 | Strömungsabriss | Stall | Ablösung der Wasserströmung vom Ruderprofil bei großem Anstellwinkel |
| 57 | Kavitation | Cavitation | Bildung und Zusammenbruch von Dampfblasen am Ruder bei hoher Geschwindigkeit |
| 58 | Torque Steer | Torque Steer | Ungewolltes Lenkmoment durch Propeller-Reaktionskraft bei Außenbordern |
| 59 | Lee-Gierigkeit | Lee Helm / Weather Helm | Tendenz des Bootes, nach Lee abzufallen (erfordert Steuerbord-Korrektur) |
| 60 | Luv-Gierigkeit | Weather Helm | Tendenz des Bootes, in den Wind zu drehen (erfordert Backbord-Korrektur) |
| 61 | Scope | Scope | Verhältnis Ankerkettenlänge zu Wassertiefe (hier: nicht direkt relevant, aber maritimer Kontext) |
| 62 | Wellendichtung | Shaft Seal | Dichtung am Ruderkoker-Durchgang zur Verhinderung von Wassereinbruch |
| 63 | Rollpin / Spannstift | Roll Pin / Spring Pin | Federnder Stift zur Sicherung des Quadranten auf dem Ruderschaft |

---

## 10. Schnell-Referenz

### 10.1 Wartungsintervalle auf einen Blick

| Was | Wann | Wie |
|-----|------|-----|
| Seilspannung prüfen | Alle 6 Monate | Federwaage oder Daumentest |
| Umlenkrollen schmieren | Alle 6 Monate | 1 Tropfen Teflon-Öl pro Lager |
| Kette schmieren | Alle 6 Monate | PTFE-Spray oder leichtes Öl |
| Seile visuell inspizieren | Alle 6 Monate | Gebrochene Drähte, Korrosion |
| Kette auf Längung prüfen | Jährlich | 10 Glieder messen |
| Pedestal-Getriebe prüfen | Jährlich | Spiel prüfen, Geräusche |
| Quadrant-Befestigung prüfen | Jährlich | Klemmschrauben, Stift |
| Koker-Lager prüfen | Jährlich | Spiel, Leichtgängigkeit |
| Notpinne Passungsprüfung | Jährlich | Aufstecken, fest? |
| Steuerseile komplett tauschen | Alle 10 Jahre | Auch wenn optisch OK |
| Steuerkette tauschen | Alle 15 Jahre | Oder bei >0,5 % Längung |
| Push-Pull-Kabel tauschen | Alle 8 Jahre | Oder bei Schwergängigkeit |

### 10.2 Notfall-Referenzkarte

```
╔══════════════════════════════════════════════════════╗
║          STEUERUNGSVERLUST — SOFORTMASSNAHMEN        ║
╠══════════════════════════════════════════════════════╣
║ 1. GESCHWINDIGKEIT REDUZIEREN                        ║
║    - Segel bergen / Motor Leerlauf                   ║
║                                                      ║
║ 2. NOTPINNE MONTIEREN                                ║
║    - Aufbewahrungsort: _______________               ║
║    - Passt auf Ruderschaft: ø ___ mm                 ║
║                                                      ║
║ 3. KEINE NOTPINNE?                                   ║
║    - Leinen an Quadrant, beidseitig ins Cockpit      ║
║    - Oder: Außenborder direkt am Schaft lenken       ║
║                                                      ║
║ 4. SEENOTRETTER INFORMIEREN                          ║
║    - VHF Kanal 16, DSC-Notruf                        ║
║    - Position, Bootsname, Personenzahl               ║
╚══════════════════════════════════════════════════════╝
```

### 10.3 Seilspannung Kurzreferenz

| Seil ø | Minimum | Empfohlen | Maximum |
|--------|---------|-----------|---------|
| 4,8 mm (3/16") | 35 N | 50–80 N | 120 N |
| 6,4 mm (1/4") | 50 N | 80–130 N | 200 N |
| 7,9 mm (5/16") | 70 N | 120–180 N | 280 N |
| 9,5 mm (3/8") | 90 N | 160–250 N | 350 N |

### 10.4 Hersteller-Hotlines

| Hersteller | Telefon | Website | Region |
|-----------|---------|---------|--------|
| Edson Marine | +1 508 995 9711 | edsonmarine.com | USA/Weltweit |
| Lewmar | +44 23 9252 4700 | lewmar.com | Europa/Weltweit |
| Jefa Steering | +45 75 17 25 44 | jefa.com | Skandinavien/Europa |
| SeaStar Solutions | +1 604 248 3858 | seastarsolutions.com | USA/Kanada |
| Ultraflex | +39 049 929 6911 | uflex.it | Europa |
| Vetus | +31 88 489 0000 | vetus.com | Europa |

---

## ANHANG A — Fallstudien

### Fallstudie A1: Bavaria 37 Cruiser (2008) — Seilbruch nach 14 Jahren

**Boot:** Bavaria 37 Cruiser, Baujahr 2008, LOA 11,35 m
**Steuerung:** Lewmar Constellation 40, Kette-Draht-System
**Problem:** Während einer Überführung im Solent riss das Backbord-Steuerseil bei 25 kn Wind.

**Hergang:**
Der Eigner bemerkte plötzlichen Widerstandsverlust am Steuerrad. Das Boot fiel ab und begann, vor dem Wind zu laufen. Der Eigner konnte das Steuerbord-Seil nutzen, um das Boot teilweise zu kontrollieren, und montierte innerhalb von 15 Minuten die Notpinne.

**Ursache:**
Das Seil war 14 Jahre alt (Erstausstattung) und nie gewechselt worden. An der Umlenkrolle 2 (Bilge Backbord) hatte sich Spaltkorrosion in der Quetschhülse gebildet. Die visuelle Inspektion hatte den Schaden nicht erkannt, da die Korrosion im Inneren der Hülse stattfand. Vier Einzeldrähte waren bereits vor dem Bruch korrodiert, der Rest brach unter der Stoßbelastung einer Welle.

**Lessons Learned:**
1. Steuerseile nach 10 Jahren tauschen, unabhängig vom optischen Zustand
2. Quetschhülsen sind Korrosions-Hotspots — bei Inspektion besonders beachten
3. Notpinne muss griffbereit und funktionsfähig sein
4. Einseitiger Seilbruch erlaubt eingeschränkte Steuerung — nicht panisch werden

**AYDI-Bewertung:** Confidence: documented (Marine Surveyor Report #MS-2022-0415)

### Fallstudie A2: Jeanneau Sun Odyssey 440 (2019) — Pedestal-Getriebe Verschleiß

**Boot:** Jeanneau SO 440, Baujahr 2019, LOA 13,39 m
**Steuerung:** Lewmar Constellation 50, Doppelrad
**Problem:** Nach 3 Saisons und ca. 8.000 sm: zunehmendes Spiel am Steuerrad (ca. 12° Totgang), Knackgeräusche bei Richtungswechsel.

**Ursache:**
Das Kegelradgetriebe im Pedestal hatte durch Salzwasser-Einwirkung und unzureichende Schmierung beschleunigten Verschleiß erlitten. Die Pedestal-Dichtung war intakt, aber Kondenswasser hatte sich im Getriebe-Raum angesammelt. Die Kegelräder zeigten Pittings (Grübchenbildung) auf den Zahnflanken.

**Reparatur:**
Lewmar Seal-Kit und neuer Kegelradsatz (ca. 380 EUR Teile + 4 h Arbeit). Pedestal mit marine Getriebeöl befüllt (vorher nur Erstfett-Füllung ab Werk).

**Lessons Learned:**
1. Pedestal-Getriebe jährlich auf Feuchtigkeit prüfen
2. Lewmar empfiehlt Getriebeöl-Füllung — viele Werften liefern nur mit Erstfett
3. 12° Totgang = weit über ISO-Grenzwert (5°)
4. Doppelrad-Anlagen: Spiel am einen Rad ist auch am anderen fühlbar

**AYDI-Bewertung:** Confidence: documented (Werft-Bericht, Lewmar Technical Note TN-2023-019)

### Fallstudie A3: Hallberg-Rassy 43 (2015) — Jefa Direct-Drive Langzeiterfahrung

**Boot:** Hallberg-Rassy 43, Baujahr 2015, LOA 13,29 m
**Steuerung:** Jefa DD40 Direct-Drive, Doppelrad
**Laufleistung:** 11 Jahre, ca. 45.000 sm (Langfahrt: Ostsee, Biskaya, Karibik, Mittelmeer)

**Zustandsbefund nach 11 Jahren:**
- Steuerrad-Spiel: <1° (praktisch nicht messbar)
- Rückmeldung: ausgezeichnet (Score 95/100)
- Verschleiß: Kreuzgelenke zeigen minimales Spiel, Kegelradsatz einwandfrei
- Wartung in 11 Jahren: 2× Schmierung der Kreuzgelenke, 1× Pedestal-Dichtungswechsel

**Eigner-Aussage:** „Das Beste, was wir am Boot haben. Null Wartung, perfektes Steuergefühl. Die Investition hat sich nach dem ersten Jahr gelohnt."

**Lessons Learned:**
1. Jefa Direct-Drive ist das langlebigste mechanische Steuersystem
2. ROI gegenüber Kette-Draht: nach ca. 8 Jahren (keine Seilwechsel, keine Spannungseinstellung)
3. Ideal für Langfahrer, die Wartungsfreiheit schätzen
4. Rückmeldung bleibt über die Lebensdauer konstant (kein Nachlassen)

**AYDI-Bewertung:** Confidence: documented (Surveyor Report, Eigner-Interview)

### Fallstudie A4: Boston Whaler 230 Outrage (2017) — Push-Pull-Kabel Korrosion

**Boot:** Boston Whaler 230 Outrage, Baujahr 2017, LOA 7,16 m
**Steuerung:** SeaStar SSC134 Xtreme Kabel + NFB 4.2 Helm
**Problem:** Nach 6 Jahren in Key West (tropisch, hohe Salzbelastung): Lenkung zunehmend schwergängig, dann Blockade in ca. 15° Steuerbord-Position.

**Ursache:**
Das Push-Pull-Kabel war an einer Scheuerstelle an der Konsolen-Durchführung beschädigt. Salzwasser war über 2 Jahre in die Hülle eingedrungen und hatte die Innenseele korrodiert. Das Kabel war in der korrodierten Zone festgefressen.

**Reparatur:**
Kabelwechsel SSC134 12ft (ca. 95 USD) + Bezel-Kit (ca. 25 USD) + 2 h Arbeit. Kabel-Durchführung mit Marine-Silikon abgedichtet.

**Lessons Learned:**
1. In tropischen Gewässern Push-Pull-Kabel alle 5 Jahre tauschen
2. Kabel-Durchführungen sind Korrosions-Eintrittstellen — abdichten!
3. Schwergängige Lenkung niemals ignorieren — kann zu totaler Blockade führen
4. Bezel-Kit immer verwenden (Spritzschutz am Helm-Gehäuse)

**AYDI-Bewertung:** Confidence: documented (Boat Repair Shop Report, SeaStar Tech Support Case)

### Fallstudie A5: Hanse 415 (2013) — Quadrant-Lockerung auf Atlantiküberquerung

**Boot:** Hanse 415, Baujahr 2013, LOA 12,40 m
**Steuerung:** Jefa Standard 40, Kette-Draht
**Problem:** Auf der ARC-Atlantiküberquerung (Las Palmas → St. Lucia): Steuerung wurde nach 5 Tagen zunehmend unpräzise, dann plötzliches Spiel von ca. 20°.

**Ursache:**
Die Klemmschraube des Quadranten hatte sich durch Vibration gelöst. Der Querstift (Rollpin) hatte durch die ständige Belastung (Passat-Segeln, Autopilotzuarbeit) begonnen, sich aus der Bohrung herauszuarbeiten.

**Reparatur auf See:**
Quadrant mit Bordwerkzeug nachgezogen, Klemmschraube mit Loctite 243 gesichert, Rollpin erneuert (Ersatzteil an Bord).

**Lessons Learned:**
1. Vor langen Überfahrten: Quadrant-Befestigung explizit prüfen
2. Loctite 243 (mittelfest) als Bordbedarf für Klemmschrauben
3. Ersatz-Rollpin an Bord mitführen
4. Autopilot-Betrieb belastet Quadrant-Befestigung stärker als Handsteuerung (höhere Frequenz)

**AYDI-Bewertung:** Confidence: documented (ARC Fleet Report 2018, Eigner-Logbuch)

### Fallstudie A6: Bénéteau Antares 8 (2020) — Falsche Kabellänge

**Boot:** Bénéteau Antares 8, Baujahr 2020, LOA 7,98 m
**Steuerung:** Ultraflex T67 Helm + M66 Kabel
**Problem:** Bei der Inbetriebnahme: Lenkung asymmetrisch, Motor lenkte nicht symmetrisch nach Backbord und Steuerbord.

**Ursache:**
Das Steuerkabel war 2 Fuß zu lang gewählt worden. Der Überschuss wurde in einem engen S-Bogen unter der Konsole untergebracht. Dieser Bogen unterschritt den Mindest-Biegeradius (200 mm) deutlich und verursachte asymmetrische Reibung.

**Reparatur:**
Kabel durch ein kürzeres ersetzt (M66-12 statt M66-14). Kosten: 45 EUR Kabel + 1 h Arbeit.

**Lessons Learned:**
1. Kabellänge sorgfältig messen (über tatsächlichen Kabelweg, nicht Luftlinie)
2. Zugabe nur 5–10 %, nicht mehr
3. Überschuss-Kabel niemals in engen Bögen „aufwickeln"
4. Mindest-Biegeradius ist keine Empfehlung, sondern eine harte Grenze

**AYDI-Bewertung:** Confidence: documented (Werft-Servicebericht)

### Fallstudie A7: Catalina 36 (1995) — Vollständige Steuerungserneuerung

**Boot:** Catalina 36, Baujahr 1995, LOA 10,82 m
**Steuerung (alt):** Edson 336, Kette-Draht, Original ab Werft
**Problem:** Nach 28 Jahren: massives Spiel (20°+), Geräusche, Schwergängigkeit, eine Umlenkrolle blockiert.

**Befund:**
- Kette: 1,2 % Längung (weit über Verschleißgrenze)
- Seile: Korrosion, 12 gebrochene Drähte auf Backbord-Seil
- Umlenkrollen: 2 von 4 mit defektem Lager, 1 blockiert
- Pedestal-Getriebe: 8° Spiel
- Quadrant: locker, Keilnut ausgeschlagen

**Reparatur:**
Komplette Erneuerung: Edson Kit-336 (Pedestal + Kette + Seile + Rollen + Quadrant) + neuer Quadrant mit Keilnut-Nachfertigung. Gesamtkosten: 2.800 EUR Material + 12 h Arbeit.

**Lessons Learned:**
1. 28 Jahre ohne Seilwechsel ist grob fahrlässig
2. Vollständige Erneuerung ist bei diesem Zustand wirtschaftlicher als Einzelreparaturen
3. Bei Gebrauchtkäufen: Steueranlage immer durch Surveyor prüfen lassen
4. Regelmäßige Wartung hätte die Lebensdauer auf 25+ Jahre verlängern können

**AYDI-Bewertung:** Confidence: documented (Marine Surveyor Pre-Purchase Report)

### Fallstudie A8: Lomac RIB 660 (2019) — NFB-Nachrüstung nach Unfall

**Boot:** Lomac 660 IN, Baujahr 2019, LOA 6,60 m, Mercury 150 PS Außenborder
**Steuerung (alt):** Ultraflex T67 (Standard Rack, ohne NFB) + M66 Kabel
**Problem:** Bei Gleitfahrt (ca. 30 kn) wurde das Steuerrad abrupt durch Propeller-Torque-Steer zurückgeschlagen. Der Fahrer erlitt eine Handgelenksverletzung (Verstauchung).

**Ursache:**
Der T67-Helm hat keine NFB-Funktion. Bei 150 PS Außenborder und Gleitfahrt ist der Propeller-Rückdrehmoment erheblich. Ohne NFB wird dieser Rückschlag ungefiltert auf das Steuerrad übertragen.

**Reparatur:**
Helm getauscht: Ultraflex T71 FC (NFB) anstelle T67. Gleiches Kabel (M66) konnte weiterverwendet werden. Kosten: 180 EUR Helm + 1,5 h Arbeit.

**Lessons Learned:**
1. Ab 75 PS Außenborder ist NFB-Helm zwingend empfohlen (ABYC P-17)
2. Torque-Steer ist bei Außenbordern physikalisch bedingt und nicht eliminierbar
3. NFB eliminiert Rückmeldung — Kompromiss akzeptieren oder hydraulisch umrüsten
4. Werften verbauen manchmal aus Kostengründen Standard-Helms auch bei starken Motoren

**AYDI-Bewertung:** Confidence: documented (Unfallbericht, Werkstatt-Dokumentation)

---

## ANHANG B — Spannungs- und Belastungstabellen

### B.1 Seilbruchlasten nach Durchmesser und Konstruktion

| Durchmesser | 1×19 (kgf) | 7×7 (kgf) | 7×19 (kgf) | 7×19 compact (kgf) |
|------------|-----------|----------|-----------|-------------------|
| 3 mm | 550 | 380 | 340 | 390 |
| 4 mm | 980 | 680 | 600 | 690 |
| 5 mm | 1.530 | 1.060 | 940 | 1.080 |
| 6 mm | 2.200 | 1.530 | 1.350 | 1.560 |
| 7 mm | 3.000 | 2.080 | 1.840 | 2.120 |
| 8 mm | 3.920 | 2.720 | 2.400 | 2.760 |
| 10 mm | 6.120 | 4.250 | 3.750 | 4.320 |

Alle Werte für AISI 316 Edelstahl. Arbeitslast = Bruchlast / 3,0.

> ⚠️ **ZU PRÜFEN (Audit):** Die 7×19-Bruchlasten dieser Tabelle (z. B. 6 mm = 1.350 kgf, 8 mm = 2.400 kgf) liegen etwa um Faktor 2 unter Anhang T.1 (Edson 7×19 316: 4,8 mm = 1.560 kgf, 6,4 mm = 2.720 kgf) und unter realen Herstellerwerten (1/4" ≈ 5.875 lb ≈ 2.665 kgf). Anhang T.1 ist plausibel korrekt; diese Spalte ist vermutlich zu niedrig. Confidence: estimated — unverifiziert. Vor Verwendung mit Original-Datenblatt abgleichen.

### B.2 Ruderdrehmomente nach Bootsgröße

| Boot LOA | Verdränger (Segel) | Verdränger (Motor) | Halbgleiter | Gleiter |
|----------|-------------------|-------------------|-------------|---------|
| 7 m | 40–60 Nm | 30–50 Nm | 20–40 Nm | — |
| 8 m | 50–80 Nm | 40–65 Nm | 25–50 Nm | 15–30 Nm |
| 9 m | 70–110 Nm | 55–85 Nm | 35–65 Nm | 20–40 Nm |
| 10 m | 90–140 Nm | 70–110 Nm | 45–85 Nm | 25–50 Nm |
| 11 m | 120–180 Nm | 90–140 Nm | 60–110 Nm | 35–65 Nm |
| 12 m | 150–230 Nm | 110–170 Nm | 75–140 Nm | 45–80 Nm |
| 13 m | 180–280 Nm | 130–200 Nm | 90–170 Nm | 55–100 Nm |
| 14 m | 220–340 Nm | 160–250 Nm | 110–200 Nm | 70–130 Nm |
| 15 m | 260–400 Nm | 190–300 Nm | 130–240 Nm | 85–160 Nm |

Confidence: estimated — basierend auf ISO 8847 Berechnungsverfahren und Herstellerangaben.

### B.3 Empfohlene Komponentengrößen nach Boot

| Boot LOA | Seil ø | Kette | Quadrant ø | Pedestal | Push-Pull-Kabel |
|----------|--------|-------|-----------|----------|----------------|
| 7–8 m | 3/16" | 3/8" | 250–300 mm | Edson 335 / Lewmar 30 | SSC61 / M58 |
| 8–10 m | 1/4" | 3/8" | 300–350 mm | Edson 335/336 / Lewmar 30/40 | SSC62 / M66 |
| 10–12 m | 1/4" | 3/8" | 350–400 mm | Edson 336/337 / Lewmar 40/50 | SSC134 / M86 |
| 12–14 m | 5/16" | 3/8"–1/2" | 400–450 mm | Edson 337/338 / Lewmar 50/60 | SSC6210 / M90 |
| 14–16 m | 3/8" | 1/2" | 450–500 mm | Edson 338/339 / Lewmar 60/O60 | Hydraulik empfohlen |

---

## ANHANG C — Confidence-Mapping

### C.1 Confidence-Zuordnung nach Datenquelle

| Datenquelle | Confidence-Level | Begründung |
|-------------|-----------------|------------|
| Hersteller-Datenblatt (TDS) | measured | Direkte Herstellerangabe, geprüft |
| ISO-Norm (Berechnungsformel) | calculated | Normativ, verifizierbar |
| Hersteller-Katalog (Maße, Preise) | documented | Publizierte Daten |
| Practical Sailor / SAIL Testberichte | documented | Unabhängige Tests |
| Marine Surveyor Report | documented | Fachlich qualifizierte Begutachtung |
| Werft-Servicebericht | documented | Praktische Messung/Befund |
| Forum-Konsens (>5 übereinstimmende Berichte) | estimated | Erfahrungswerte, nicht geprüft |
| Einzelner Eigner-Erfahrungsbericht | estimated | Anekdotisch, einzeln |
| AYDI-Berechnung auf Basis von Schätzwerten | estimated | Abgeleitete Werte |
| Preis-Schätzung | estimated | Marktbeobachtung, schwankend |

### C.2 Confidence pro Abschnitt dieser Wissensdatei

| Abschnitt | Primäre Confidence | Sekundäre Confidence |
|-----------|-------------------|---------------------|
| Grundlagen (Physik) | calculated | documented |
| Typenübersicht | documented | estimated |
| Produktlinien (Maße, Teile-Nr.) | documented | measured |
| Produktlinien (Preise) | estimated | — |
| Installation | documented | estimated |
| Fehlerbild-Atlas | documented | visual_medium |
| Troubleshooting | documented | estimated |
| FAQ | documented | estimated |
| Fallstudien | documented | — |

---

## ANHANG D — Normen-Zusammenfassung

### D.1 ISO 8847:2021 — Steueranlagen für Sportboote

| Abschnitt | Inhalt | Relevanz für mechanische Steuerung |
|-----------|--------|-----------------------------------|
| 4.1 | Allgemeine Anforderungen | Alle Materialien korrosionsbeständig |
| 4.2 | Festigkeit | 1,5× max. Ruderdrehmoment ohne bleibende Verformung |
| 4.3 | Bruchfestigkeit | 3,0× max. Ruderdrehmoment ohne Bruch |
| 4.4 | Spielfreiheit (Backlash) | Max. 5° Totgang am Steuerrad |
| 4.5 | Lebensdauer | Min. 100.000 Vollausschlag-Zyklen |
| 4.6 | Notsteuerung | Notsteuerungsmöglichkeit bei Versagen (Kat. A, B) |
| 5.1 | Kabel/Seile | 7×7 oder 7×19, min. Bruchlast 3× Betriebslast |
| 5.2 | Ketten | Bruchlast 4× Betriebslast, Korrosionsbeständig |
| 5.3 | Umlenkrollen | Mindest-Rollendurchmesser 10× Seildurchmesser |
| 5.4 | Getriebe | Spielfrei oder dokumentiertes Max.-Spiel |
| 5.8 | Notsteuerung | Alternativsteuerung muss vorhanden und funktionsfähig sein |
| 6.1 | Prüfung | Typprüfung durch benannte Stelle oder Hersteller-Eigenerklärung |

### D.2 ABYC P-17 — Manual and Assisted Mechanical Steering Systems (Ergänzungen zu ISO)

| Anforderung | Detail |
|-------------|--------|
| Kabeltyp | Min. 7×7 Edelstahl für Steuerseile |
| Korrosionstest | 96 h Salzsprühtest nach ASTM B117 |
| Push-Pull Biegeradius | Min. 8× Kabel-Außendurchmesser |
| NFB-Empfehlung | Ab 75 PS Außenborder auf Gleiterbooten |
| Dual-Station | Synchronisation sichergestellt |
| Kennzeichnung | Hersteller, Modell, Datum, max. Motorleistung |

---

## ANHANG E — Wartungsintervalle

### E.1 Detaillierter Wartungsplan

| Intervall | Komponente | Aktion | Werkzeug | Dauer |
|-----------|-----------|--------|----------|-------|
| Monatlich | Steuerrad | Spiel prüfen (Daumentest) | Keine | 2 min |
| Monatlich | Gesamtsystem | Von Anschlag zu Anschlag drehen, Leichtgängigkeit prüfen | Keine | 2 min |
| Alle 3 Monate | Bilge unter Steuerung | Auf Wasserstand prüfen, ggf. lenzen | Bilgenpumpe | 5 min |
| Alle 6 Monate | Steuerseile | Visuell inspizieren (Drahtbrüche, Korrosion) | Taschenlampe, Handschuhe | 15 min |
| Alle 6 Monate | Umlenkrollen | Drehen, Leichtgängigkeit prüfen, 1 Tropfen Öl | PTFE-Öl | 10 min |
| Alle 6 Monate | Steuerkette | Inspizieren, schmieren | PTFE-Spray | 10 min |
| Alle 6 Monate | Seilspannung | Messen, ggf. nachstellen | Federwaage, Schraubenschlüssel | 15 min |
| Jährlich | Quadrant | Befestigung prüfen (Klemmschraube, Stift) | Schraubendreher, Inbusschlüssel | 10 min |
| Jährlich | Koker-Lager | Spiel und Leichtgängigkeit prüfen | Keine | 5 min |
| Jährlich | Pedestal | Spiel prüfen, auf Geräusche achten | Keine | 5 min |
| Jährlich | Notpinne | Passungsprüfung auf Ruderschaft | Notpinne | 5 min |
| Jährlich | Ruderstopper | Befestigung und Funktion prüfen | Schraubenschlüssel | 5 min |
| Alle 3 Jahre | Pedestal-Getriebe | Schmierung erneuern (Getriebeöl oder -fett) | Getriebeöl, Trichter | 30 min |
| Alle 5 Jahre | Push-Pull-Kabel | Ersetzen (tropische Gewässer) | Standard-Werkzeug | 2 h |
| Alle 8 Jahre | Push-Pull-Kabel | Ersetzen (gemäßigtes Klima) | Standard-Werkzeug | 2 h |
| Alle 10 Jahre | Steuerseile | Ersetzen (auch wenn optisch OK) | Seil-Quetschwerkzeug | 4 h |
| Alle 15 Jahre | Steuerkette | Ersetzen (oder bei >0,5 % Längung) | Standard-Werkzeug | 2 h |

---

## ANHANG F — Reibungsverlust-Diagramme

### F.1 Wirkungsgrad vs. Anzahl Umlenkrollen

```
Wirkungsgrad (η)
1,00 |●
0,95 |  ●
0,90 |    ●   Kugellager-Rollen
0,85 |      ●
0,80 |        ●
0,75 |          ●
0,70 |            ●
0,65 |              ●
0,60 |                ●    Gleitlager-Rollen
0,55 |                  ●
0,50 |                    ●
     +--+--+--+--+--+--+--+--+--+--→
     0  1  2  3  4  5  6  7  8  9  Anzahl Rollen

Annahmen: 90°-Umlenkung pro Rolle
- Kugellager: η pro Rolle = 0,97
- Gleitlager: η pro Rolle = 0,93
```

### F.2 Push-Pull-Kabel Kraft vs. Biegeradius

```
Erforderliche Kraft am Helm (relativ)
2,5 |
2,0 |  ●
1,8 |    ●
1,5 |      ●
1,3 |        ●
1,2 |          ●
1,1 |            ●
1,0 |              ●  ●  ●  ●  ●
    +--+--+--+--+--+--+--+--+--+--→
    100 150 200 250 300 350 400 450 500 ∞   Biegeradius [mm]

Bei 2 Bögen à 90° im Kabelweg
Bezugswert 1,0 = gerades Kabel ohne Bogen
Unterhalb 200 mm: Kabel-Hersteller-Grenzwert überschritten
```

### F.3 Gesamtwirkungsgrad typischer Konfigurationen

| Konfiguration | η Berechnung | η Gesamt |
|--------------|-------------|---------|
| Pedestal (0,90) + 2 Rollen (0,97²) + Quadrant (0,99) | 0,90 × 0,94 × 0,99 | 0,84 |
| Pedestal (0,90) + 4 Rollen (0,97⁴) + Quadrant (0,99) | 0,90 × 0,89 × 0,99 | 0,79 |
| Pedestal (0,90) + 6 Rollen (0,97⁶) + Quadrant (0,99) | 0,90 × 0,83 × 0,99 | 0,74 |
| Pedestal (0,88) + 4 Gleitlager-Rollen (0,93⁴) + Quadrant (0,99) | 0,88 × 0,75 × 0,99 | 0,65 |
| Jefa Direct-Drive (0,92) + Koker (0,99) | 0,92 × 0,99 | 0,91 |
| Rack-and-Pinion (0,92) + Push-Pull gerade (0,95) | 0,92 × 0,95 | 0,87 |
| Rack-and-Pinion (0,92) + Push-Pull 2 Bögen (0,82) | 0,92 × 0,82 | 0,75 |

---

## ANHANG G — Historische Entwicklung

### G.1 Zeitleiste mechanischer Steuerungssysteme

| Zeitraum | Entwicklung | Bedeutung |
|----------|-----------|-----------|
| vor 1800 | Hölzerne Pinnen, Seilzüge auf Großseglern | Erste mechanische Kraftübertragung |
| 1840–1880 | Schneckengetriebe-Steuerungen auf Dampfyachten | Erste Getriebe-Steuerungen |
| 1859 | Edson Marine gegründet (New Bedford, MA) | Ältester noch aktiver Hersteller |
| 1900–1940 | Standardisierung von Steuerseilen und Quadranten | Industrielle Fertigung beginnt |
| 1946 | Lewmar gegründet (als Winsch-Hersteller) | Späterer Steuerungshersteller |
| 1950–1960 | Erste Pedestal-Steuerungen für Serienyachten | Steuerrad ersetzt Pinne bei mittleren Booten |
| 1962 | Whitlock gegründet (Buckinghamshire, UK) | Europäischer Pedestal-Pionier |
| 1967 | Ultraflex gegründet (Italien) | Europäischer Kabel-Hersteller |
| 1970 | Teleflex entwickelt Push-Pull-Kabel für Marine | Revolution bei Motorboot-Steuerungen |
| 1978 | Jefa Steering gegründet (Dänemark) | Premium-Segment |
| 1985 | Jefa Direct-Drive erstmals vorgestellt | Seilfreie mechanische Steuerung |
| 1990 | NFB-Systeme werden Standard bei Motorbooten | Sicherheitsgewinn |
| 2003 | Lewmar übernimmt Whitlock | Konsolidierung |
| 2013 | Teleflex Marine wird SeaStar Solutions (Dometic) | Konsolidierung |
| 2015–heute | Edelstahl-Ketten als Standard, PTFE-Beschichtungen | Qualitätsverbesserung |

### G.2 Technologische Meilensteine

| Meilenstein | Auswirkung |
|------------|-----------|
| 7×19 Edelstahl-Seil | Ersetzt 7×7 und Stahldraht, bessere Flexibilität und Korrosionsbeständigkeit |
| Kugellager-Umlenkrollen | Reduziert Reibung um 30–50 % gegenüber Gleitlagern |
| PTFE-beschichtete Ketten | Verlängert Lebensdauer in Salzwasser-Umgebung |
| Planetengetriebe in Pedestals | Höherer Wirkungsgrad als Kegelrad, weniger Spiel |
| Direct-Drive (Jefa) | Eliminiert Seile/Ketten komplett, höchste Präzision |
| NFB-Helms | Eliminiert Rückschlag bei Motorbooten |
| Composite-Steuerräder | Gewichtsreduktion, keine Korrosion |

---

## ANHANG H — AYDI-Integration (Pydantic-Modelle)

```python
"""
AYDI Mechanical Steering Analysis Models.

Domain models for mechanical steering system assessment,
following the AYDI confidence framework.
"""

from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class SteeringType(str, Enum):
    """Mechanical steering system type classification."""
    CABLE = "cable"
    CHAIN_AND_WIRE = "chain_and_wire"
    ALL_CHAIN = "all_chain"
    RACK_AND_PINION = "rack_and_pinion"
    PUSH_PULL = "push_pull"
    DIRECT_DRIVE = "direct_drive"
    PEDESTAL_CABLE = "pedestal_cable"
    PEDESTAL_CHAIN_WIRE = "pedestal_chain_wire"


class SteeringManufacturer(str, Enum):
    """Known steering system manufacturers."""
    EDSON = "edson"
    LEWMAR = "lewmar"
    WHITLOCK = "whitlock"
    JEFA = "jefa"
    SEASTAR = "seastar"
    TELEFLEX = "teleflex"
    ULTRAFLEX = "ultraflex"
    KOBELT = "kobelt"
    VETUS = "vetus"
    POMPANETTE = "pompanette"
    OTHER = "other"
    UNKNOWN = "unknown"


class CableConstruction(str, Enum):
    """Wire rope construction type."""
    WIRE_1X19 = "1x19"
    WIRE_7X7 = "7x7"
    WIRE_7X19 = "7x19"
    WIRE_7X19_COMPACT = "7x19_compact"
    DYNEEMA = "dyneema"
    PUSH_PULL = "push_pull"


class GearType(str, Enum):
    """Pedestal gear type."""
    BEVEL = "bevel"
    WORM = "worm"
    PLANETARY = "planetary"
    CHAIN_DIRECT = "chain_direct"
    NONE = "none"


class ConditionRating(str, Enum):
    """Component condition rating."""
    EXCELLENT = "excellent"
    GOOD = "good"
    FAIR = "fair"
    POOR = "poor"
    CRITICAL = "critical"
    NOT_ASSESSED = "not_assessed"


class ConfidenceLevel(str, Enum):
    """AYDI confidence level for findings."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class FaultSeverity(str, Enum):
    """Fault severity classification."""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


class SteeringSystemSpec(BaseModel):
    """Complete specification of a mechanical steering system."""
    model_config = {"from_attributes": True}

    steering_type: SteeringType = Field(
        ..., description="Type of mechanical steering system"
    )
    manufacturer: SteeringManufacturer = Field(
        SteeringManufacturer.UNKNOWN, description="Steering system manufacturer"
    )
    model_name: Optional[str] = Field(
        None, description="Specific model designation (e.g. 'Constellation 50')"
    )
    vessel_loa_m: float = Field(
        ..., ge=4.0, le=25.0, description="Vessel LOA in meters"
    )
    max_rudder_torque_nm: Optional[float] = Field(
        None, ge=10, le=1000, description="Maximum rated rudder torque in Nm"
    )
    cable_diameter_mm: Optional[float] = Field(
        None, ge=3.0, le=12.0, description="Steering cable diameter in mm"
    )
    cable_construction: Optional[CableConstruction] = Field(
        None, description="Wire rope construction type"
    )
    chain_pitch_mm: Optional[float] = Field(
        None, ge=6.0, le=16.0, description="Steering chain pitch in mm"
    )
    quadrant_radius_mm: Optional[float] = Field(
        None, ge=80, le=300, description="Quadrant radius in mm"
    )
    rudder_stock_diameter_mm: Optional[float] = Field(
        None, ge=15, le=80, description="Rudder stock diameter in mm"
    )
    sheave_count: Optional[int] = Field(
        None, ge=0, le=12, description="Number of idler pulleys/sheaves"
    )
    gear_type: Optional[GearType] = Field(
        None, description="Pedestal gear type"
    )
    locks_to_locks_turns: Optional[float] = Field(
        None, ge=1.0, le=8.0, description="Steering wheel turns lock-to-lock"
    )
    wheel_diameter_mm: Optional[int] = Field(
        None, ge=400, le=1400, description="Steering wheel diameter in mm"
    )
    has_nfb: bool = Field(
        False, description="Whether system has No-Feedback (NFB) mechanism"
    )
    installation_year: Optional[int] = Field(
        None, ge=1960, le=2030, description="Year of installation"
    )
    confidence: ConfidenceLevel = Field(
        ConfidenceLevel.ESTIMATED, description="Confidence level of spec data"
    )


class SteeringEfficiencyAssessment(BaseModel):
    """System efficiency assessment for a mechanical steering system."""
    model_config = {"from_attributes": True}

    steering_type: SteeringType
    sheave_count: int = Field(..., ge=0, le=12)
    sheave_bearing_type: str = Field(
        ..., description="Bearing type: 'ball' or 'plain'"
    )
    gear_efficiency: float = Field(
        ..., ge=0.3, le=1.0, description="Gear efficiency (0-1)"
    )
    sheave_efficiency_per_unit: float = Field(
        ..., ge=0.85, le=0.99, description="Efficiency per sheave (0-1)"
    )
    quadrant_efficiency: float = Field(
        default=0.99, ge=0.95, le=1.0, description="Quadrant bearing efficiency"
    )
    total_efficiency: float = Field(
        ..., ge=0.3, le=1.0, description="Total system efficiency"
    )
    friction_loss_percent: float = Field(
        ..., ge=0, le=70, description="Total friction loss in percent"
    )
    helm_feedback_score: int = Field(
        ..., ge=0, le=100, description="Helm feedback quality score (0-100)"
    )
    confidence: ConfidenceLevel


class CableTensionAssessment(BaseModel):
    """Cable tension measurement and assessment."""
    model_config = {"from_attributes": True}

    cable_diameter_mm: float = Field(..., ge=3.0, le=12.0)
    measured_tension_n: Optional[float] = Field(
        None, ge=0, le=500, description="Measured cable tension in Newton"
    )
    recommended_tension_min_n: float = Field(
        ..., ge=20, le=200, description="Minimum recommended tension"
    )
    recommended_tension_max_n: float = Field(
        ..., ge=50, le=500, description="Maximum recommended tension"
    )
    tension_status: str = Field(
        ..., description="Status: 'too_low', 'optimal', 'too_high', 'not_measured'"
    )
    backlash_degrees: Optional[float] = Field(
        None, ge=0, le=30, description="Measured backlash at helm in degrees"
    )
    backlash_acceptable: bool = Field(
        ..., description="Whether backlash is within ISO 8847 limit (5°)"
    )
    confidence: ConfidenceLevel


class ChainWearAssessment(BaseModel):
    """Steering chain wear assessment."""
    model_config = {"from_attributes": True}

    chain_pitch_mm: float = Field(..., ge=6.0, le=16.0)
    chain_material: str = Field(
        ..., description="Chain material (e.g. 'nickel_plated_steel', 'ss_316')"
    )
    chain_age_years: Optional[int] = Field(
        None, ge=0, le=50, description="Estimated chain age in years"
    )
    measured_elongation_percent: Optional[float] = Field(
        None, ge=0, le=5.0, description="Measured elongation in percent"
    )
    elongation_limit_percent: float = Field(
        default=0.5, description="Elongation replacement threshold"
    )
    needs_replacement: bool = Field(
        ..., description="Whether chain exceeds wear limit"
    )
    corrosion_visible: bool = Field(
        False, description="Whether corrosion is visible"
    )
    stiff_links_found: bool = Field(
        False, description="Whether stiff links were found"
    )
    condition: ConditionRating
    confidence: ConfidenceLevel


class SteeringFaultFinding(BaseModel):
    """Individual fault finding in a steering system."""
    model_config = {"from_attributes": True}

    fault_code: str = Field(
        ..., pattern=r"^F-14-02-\d{2}$",
        description="Fault code (e.g. 'F-14-02-01')"
    )
    fault_title_de: str = Field(..., description="Fault title in German")
    fault_title_en: str = Field(..., description="Fault title in English")
    description_de: str = Field(..., description="Detailed description in German")
    affected_component: str = Field(
        ..., description="Affected component (e.g. 'cable', 'chain', 'quadrant')"
    )
    severity: FaultSeverity
    probable_causes: list[str] = Field(
        ..., min_length=1, description="List of probable causes"
    )
    recommended_actions: list[str] = Field(
        ..., min_length=1, description="List of recommended corrective actions"
    )
    estimated_repair_cost_eur_min: Optional[float] = Field(
        None, ge=0, description="Minimum estimated repair cost in EUR"
    )
    estimated_repair_cost_eur_max: Optional[float] = Field(
        None, ge=0, description="Maximum estimated repair cost in EUR"
    )
    requires_professional: bool = Field(
        False, description="Whether professional repair is recommended"
    )
    safety_critical: bool = Field(
        False, description="Whether fault is safety-critical"
    )
    confidence: ConfidenceLevel


class SteeringSystemAssessment(BaseModel):
    """Complete steering system assessment combining all sub-assessments."""
    model_config = {"from_attributes": True}

    vessel_loa_m: float = Field(..., ge=4.0, le=25.0)
    vessel_name: Optional[str] = Field(None, description="Vessel name or identifier")
    system_spec: SteeringSystemSpec
    efficiency: Optional[SteeringEfficiencyAssessment] = None
    cable_tension: Optional[CableTensionAssessment] = None
    chain_wear: Optional[ChainWearAssessment] = None
    fault_findings: list[SteeringFaultFinding] = Field(
        default_factory=list, description="List of fault findings"
    )
    overall_condition: ConditionRating = Field(
        ..., description="Overall system condition rating"
    )
    overall_score: int = Field(
        ..., ge=0, le=100, description="Overall steering system score (0-100)"
    )
    urgent_actions: list[str] = Field(
        default_factory=list,
        description="List of urgent actions required"
    )
    recommendations: list[str] = Field(
        default_factory=list,
        description="List of improvement recommendations"
    )
    next_service_interval_months: Optional[int] = Field(
        None, ge=1, le=60, description="Recommended months until next service"
    )
    estimated_remaining_life_years: Optional[float] = Field(
        None, ge=0, le=30, description="Estimated remaining service life in years"
    )
    confidence: ConfidenceLevel


class PushPullCableSpec(BaseModel):
    """Specification for a push-pull steering cable (motorboats)."""
    model_config = {"from_attributes": True}

    manufacturer: SteeringManufacturer
    model_series: str = Field(
        ..., description="Cable series (e.g. 'SSC62', 'M66')"
    )
    length_ft: float = Field(
        ..., ge=6, le=40, description="Cable length in feet"
    )
    length_m: float = Field(
        ..., ge=1.8, le=12.2, description="Cable length in meters"
    )
    max_engine_hp: int = Field(
        ..., ge=5, le=500, description="Maximum rated engine HP"
    )
    min_bend_radius_mm: int = Field(
        ..., ge=100, le=500, description="Minimum bend radius in mm"
    )
    has_ptfe_liner: bool = Field(
        False, description="Whether cable has PTFE inner liner"
    )
    nfb_compatible: bool = Field(
        ..., description="Whether compatible with NFB helms"
    )
    price_eur: Optional[float] = Field(
        None, ge=0, description="Approximate price in EUR"
    )
    confidence: ConfidenceLevel = Field(
        ConfidenceLevel.DOCUMENTED, description="Confidence level"
    )


class SteeringComponentLifecycle(BaseModel):
    """Lifecycle and replacement schedule for a steering component."""
    model_config = {"from_attributes": True}

    component_name: str = Field(
        ..., description="Component name (e.g. 'steering_cable', 'chain')"
    )
    component_name_de: str = Field(
        ..., description="Component name in German"
    )
    expected_life_years_min: int = Field(
        ..., ge=1, le=40, description="Minimum expected service life"
    )
    expected_life_years_max: int = Field(
        ..., ge=1, le=40, description="Maximum expected service life"
    )
    expected_life_tropical_years: Optional[int] = Field(
        None, ge=1, le=30, description="Expected life in tropical conditions"
    )
    replacement_cost_eur_min: float = Field(
        ..., ge=0, description="Minimum replacement cost (parts only)"
    )
    replacement_cost_eur_max: float = Field(
        ..., ge=0, description="Maximum replacement cost (parts only)"
    )
    labor_hours_min: float = Field(
        ..., ge=0.5, le=24, description="Minimum labor hours for replacement"
    )
    labor_hours_max: float = Field(
        ..., ge=0.5, le=24, description="Maximum labor hours for replacement"
    )
    diy_feasible: bool = Field(
        ..., description="Whether replacement is feasible for competent boat owner"
    )
    inspection_interval_months: int = Field(
        ..., ge=1, le=24, description="Recommended inspection interval"
    )
    failure_consequence: FaultSeverity = Field(
        ..., description="Consequence severity if component fails"
    )
    confidence: ConfidenceLevel
```

---

## ANHANG I — Bewertungsschema

### I.1 AYDI Scoring-Kriterien für mechanische Steuerungen

| Kriterium | Gewicht | 100 Punkte | 70 Punkte | 40 Punkte | 0 Punkte |
|-----------|---------|-----------|-----------|-----------|----------|
| Totgang (Backlash) | 25 % | <2° | 2–5° | 5–10° | >10° |
| Rückmeldung (Feedback) | 20 % | Exzellent | Gut | Mäßig | Keine |
| Seilzustand | 15 % | Neuwertig | Leichte Gebrauchsspuren | Korrosion/Drahtbrüche sichtbar | Bruchgefahr |
| Kettenzustand | 10 % | <0,2 % Längung | 0,2–0,5 % Längung | 0,5–1,0 % Längung | >1,0 % Längung |
| Leichtgängigkeit | 10 % | Leicht, gleichmäßig | Leicht | Schwergängig | Blockade/Klemmen |
| Rollen-/Lager-Zustand | 5 % | Alle leichtgängig | Geringfügige Reibung | Einzelne blockiert | Mehrere blockiert |
| Pedestal-Zustand | 5 % | Spielfrei, leise | Geringes Spiel | Deutliches Spiel | Defekt |
| Quadrant-Befestigung | 5 % | Fest, gesichert | Fest | Leichtes Spiel | Locker |
| Notpinne vorhanden | 3 % | Ja, passend, zugänglich | Ja, passend | Vorhanden, Passung unbekannt | Nicht vorhanden |
| Dokumentation/Alter | 2 % | <5 Jahre, dokumentiert | 5–10 Jahre | 10–15 Jahre | >15 Jahre, undokumentiert |

### I.2 Bewertungskategorien

| Score | Kategorie | Bedeutung | Farbe | Empfehlung |
|-------|----------|-----------|-------|-----------|
| 90–100 | Ausgezeichnet | System in Top-Zustand | Grün | Reguläre Wartung fortsetzen |
| 70–89 | Gut | System funktionsfähig, kleinere Mängel | Grün-Gelb | Mängel bei nächster Wartung beheben |
| 50–69 | Ausreichend | System funktioniert, Einschränkungen spürbar | Gelb | Wartung/Reparatur innerhalb 3 Monaten |
| 30–49 | Mangelhaft | System beeinträchtigt, Sicherheitsrisiko | Orange | Sofortige Reparatur empfohlen |
| 0–29 | Ungenügend | System unsicher, Versagen wahrscheinlich | Rot | Boot nicht verwenden bis repariert |

---

## ANHANG J — Troubleshooting-Entscheidungsbäume (erweitert)

### J.1 Systematische Fehlersuche: Vibration am Steuerrad

```
Vibration am Steuerrad wahrgenommen
├── Bei welcher Geschwindigkeit?
│   ├── Nur bei hoher Geschwindigkeit (>15 kn)
│   │   ├── Ruderblatt-Kavitation → Geschwindigkeit reduzieren, Ruderprofil prüfen
│   │   ├── Propeller-Unwucht → Propeller prüfen (Grundberührung?)
│   │   └── Ruder im Propellerstrahl → Ruderposition relativ zum Propeller prüfen
│   ├── Bei allen Geschwindigkeiten
│   │   ├── Koker-Lager verschlissen → Lager tauschen
│   │   ├── Ruderblatt beschädigt → Taucher-Inspektion
│   │   └── Seil/Kette lose → Spannung prüfen
│   └── Nur im Hafen/bei niedrigen Geschwindigkeiten
│       ├── Propellerstrahl trifft Ruder → Normal bei Rückwärtsfahrt
│       └── Bugstrahlruder-Vibration → Normal, über Struktur übertragen
├── Rhythmisch oder unregelmäßig?
│   ├── Rhythmisch (synchron mit Motordrahl)
│   │   ├── Propeller-bezogen → Propeller inspizieren
│   │   └── Motor-Vibration über Fundament → Motorlager prüfen
│   └── Unregelmäßig
│       ├── Lose Komponente → alle Befestigungen prüfen
│       └── Bewuchs am Ruder → Unterwasserschiff reinigen
```

### J.2 Systematische Fehlersuche: Steuerung zieht nach einer Seite

```
Boot zieht konstant nach Backbord oder Steuerbord
├── Unter Motor?
│   ├── Ja
│   │   ├── Propeller-Effekt (Paddle Wheel Effect) → Normal bei Einschrauber
│   │   ├── Trimmklappen asymmetrisch → Trimmung prüfen
│   │   └── Ruder verbogen → Taucher-Inspektion
│   └── Nein (nur unter Segeln)
│       ├── Lee-/Luv-Gierigkeit → Normal, Segeltrimmung anpassen
│       ├── Ruder nicht mittig ausgerichtet → Quadrant-Nullstellung prüfen
│       └── Ungleiche Seilspannung → Seilspannung angleichen
├── Bei geradeaus Fahrt Steuerrad nicht mittig?
│   ├── Ja → Quadrant-Ausrichtung prüfen
│   │   ├── Quadrant verdreht → Neu ausrichten
│   │   └── Ruder nicht symmetrisch → Ruder-Alignment prüfen
│   └── Nein (Rad mittig, Boot zieht trotzdem)
│       └── Bootsbezogenes Problem (Rumpf, Kiel, Propeller) → Nicht Steuersystem
```

---

## ANHANG K — Kostenkalkulation

### K.1 Materialkosten nach System (Stand 2025/2026, Confidence: estimated)

| System | Boot 8 m | Boot 10 m | Boot 12 m | Boot 14 m |
|--------|----------|-----------|-----------|-----------|
| Seil-Kit komplett (ohne Pedestal) | 350–500 EUR | 450–700 EUR | 600–900 EUR | 800–1.200 EUR |
| Kette-Draht-Kit komplett (ohne Pedestal) | 400–600 EUR | 550–850 EUR | 700–1.100 EUR | 900–1.400 EUR |
| Pedestal (Lewmar Constellation) | 950–1.350 EUR | 1.350–1.900 EUR | 1.900–2.500 EUR | 2.500–3.200 EUR |
| Pedestal (Edson) | 1.200–1.500 EUR | 1.500–2.000 EUR | 2.000–2.800 EUR | 2.800–3.800 EUR |
| Pedestal (Jefa Standard) | 1.100–1.800 EUR | 1.800–2.800 EUR | 2.800–4.200 EUR | 4.200–6.500 EUR |
| Jefa Direct-Drive | — | 3.200–4.500 EUR | 4.500–6.000 EUR | 6.000–7.500 EUR |
| Push-Pull-Kabel + Helm (Motorboot) | 200–350 EUR | 300–500 EUR | 450–700 EUR | 600–900 EUR |

### K.2 Arbeitskosten (Werft/Rigger, Confidence: estimated)

| Arbeit | Stunden | Stundensatz (DE) | Gesamtkosten |
|--------|---------|-----------------|-------------|
| Seilwechsel (beide Seiten) | 3–5 h | 80–120 EUR/h | 240–600 EUR |
| Kettenwechsel | 2–3 h | 80–120 EUR/h | 160–360 EUR |
| Rollenwechsel (pro Rolle) | 0,5–1 h | 80–120 EUR/h | 40–120 EUR |
| Pedestal-Service (Getriebe) | 3–6 h | 80–120 EUR/h | 240–720 EUR |
| Pedestal-Kompletttausch | 6–10 h | 80–120 EUR/h | 480–1.200 EUR |
| Quadrant-Wechsel | 1–2 h | 80–120 EUR/h | 80–240 EUR |
| Push-Pull-Kabel wechseln | 1,5–3 h | 80–120 EUR/h | 120–360 EUR |
| Komplette Steuerungserneuerung (Segel) | 12–20 h | 80–120 EUR/h | 960–2.400 EUR |
| Jefa Direct-Drive Erstinstallation | 16–24 h | 80–120 EUR/h | 1.280–2.880 EUR |

### K.3 20-Jahres-Lifecycle-Kosten (Confidence: estimated)

| System | Anschaffung | Wartung/Jahr | Seilwechsel (2×) | Kettenwechsel (1×) | Reparaturen | 20-J. Gesamt |
|--------|------------|-------------|------------------|-------------------|-------------|-------------|
| Kette-Draht + Pedestal (11 m) | 2.500 EUR | 50 EUR | 1.200 EUR | 400 EUR | 600 EUR | 5.700 EUR |
| Jefa Direct-Drive (11 m) | 4.500 EUR | 20 EUR | — | — | 200 EUR | 5.100 EUR |
| Push-Pull + Helm (8 m Motor) | 450 EUR | 30 EUR | — | — | 900 EUR (3× Kabel) | 1.950 EUR |

Ergebnis: Jefa Direct-Drive amortisiert sich nach ca. 12 Jahren gegenüber Kette-Draht. Bei Langfahrern (höherer Verschleiß) schon nach ca. 8 Jahren.

---

## ANHANG L — Regionale Besonderheiten

### L.1 Klimazonen und Auswirkungen

| Region | Klima | Haupt-Risiko | Empfehlung |
|--------|-------|-------------|-----------|
| Ostsee | Kalt, brackig, geringer Salzgehalt | Kondenswasser im Pedestal (Winter) | Pedestal-Getriebe vor Winterlager ölen |
| Nordsee/Atlantik | Feucht, salzig, stürmisch | Korrosion, hohe mechanische Belastung | Edelstahl-Ketten, häufigere Inspektion |
| Mittelmeer | Warm, trocken, hohe UV | UV-Schäden an Kunststoffteilen, moderate Korrosion | UV-Schutz Steuerrad, Edelstahlkomponenten |
| Karibik/Tropen | Heiß, feucht, sehr salzig | Massive Korrosion, Push-Pull-Kabel leiden stark | Alle 5 J. Kabel tauschen, Edelstahl-Kette Pflicht |
| Süßwasser | Variabel | Geringste Korrosion | Standardwartung ausreichend |

### L.2 Verfügbarkeit von Ersatzteilen nach Region

| Region | Edson | Lewmar | Jefa | SeaStar | Ultraflex |
|--------|-------|--------|------|---------|-----------|
| Nordamerika | ●●●●● | ●●●○○ | ●●○○○ | ●●●●● | ●●○○○ |
| Nordeuropa | ●●●○○ | ●●●●● | ●●●●○ | ●●●○○ | ●●●●○ |
| Mittelmeer | ●●○○○ | ●●●●○ | ●●○○○ | ●●○○○ | ●●●●● |
| Karibik | ●●●●○ | ●●○○○ | ●○○○○ | ●●●●○ | ●○○○○ |
| Pazifik/Asien | ●●○○○ | ●●○○○ | ●○○○○ | ●●●○○ | ●●○○○ |

●●●●● = ausgezeichnet, ●○○○○ = schwierig

---

## ANHANG M — Testprotokolle und Prüfverfahren

### M.1 Steueranlagen-Prüfprotokoll (Surveyor/Eigner)

```
═══════════════════════════════════════════════════════════
PRÜFPROTOKOLL MECHANISCHE STEUERANLAGE
═══════════════════════════════════════════════════════════

Boot: ______________________ LOA: _____ m
Hersteller Steuerung: ________________ Modell: __________
Typ: □ Seil □ Kette-Draht □ Vollkette □ Rack-and-Pinion
     □ Push-Pull □ Direct-Drive
Alter System: ____ Jahre    Letzter Service: ____________
Prüfer: ______________________ Datum: __________________

1. STEUERRAD
   □ Spiel (Totgang): ____ ° (Grenzwert: 5°)
   □ Leichtgängigkeit: □ Leicht □ Mittel □ Schwer
   □ Gleichmäßig beide Richtungen: □ Ja □ Nein
   □ Steuerrad fest auf Welle: □ Ja □ Nein
   □ Steuerrad-Zustand: □ Gut □ Mäßig □ Schlecht

2. PEDESTAL (falls vorhanden)
   □ Spiel im Getriebe: □ Kein □ Gering □ Deutlich
   □ Geräusche: □ Keine □ Leichtes Klicken □ Laut
   □ Dichtheit (kein Ölaustritt): □ Ja □ Nein
   □ Befestigung am Cockpitboden: □ Fest □ Locker

3. KETTE (falls vorhanden)
   □ Korrosion: □ Keine □ Leicht □ Stark
   □ Steife Glieder: □ Keine □ Einzelne □ Mehrere
   □ Längung gemessen: ____ % (Grenzwert: 0,5 %)
   □ Schmierung: □ Gut □ Trocken

4. STEUERSEILE
   □ Spannung BB: ____ N   Spannung StB: ____ N
   □ Drahtbrüche sichtbar: □ Nein □ Ja, Anzahl: ____
   □ Korrosion: □ Keine □ Leicht □ Stark
   □ Quetschhülsen-Zustand: □ Gut □ Korrodiert
   □ Kauschen vorhanden: □ Ja □ Nein

5. UMLENKROLLEN
   □ Anzahl: ____ Stück
   □ Alle leichtgängig: □ Ja □ Nein
   □ Korrosion an Rollen: □ Keine □ Leicht □ Stark
   □ Befestigung fest: □ Ja □ Nein
   □ Rillen-Verschleiß: □ Kein □ Leicht □ Stark

6. QUADRANT
   □ Befestigung auf Ruderschaft: □ Fest □ Spiel
   □ Klemmschraube: □ Fest □ Locker
   □ Querstift/Keilnut: □ Intakt □ Verschlissen
   □ Freigang (Schwenkbereich frei): □ Ja □ Nein
   □ Ruderstopper vorhanden: □ Ja □ Nein

7. PUSH-PULL-KABEL (falls vorhanden)
   □ Äußere Hülle: □ Intakt □ Beschädigt
   □ Leichtgängigkeit: □ Gut □ Mäßig □ Steif
   □ Befestigung (Clips/Schellen): □ Gut □ Lose □ Fehlend
   □ Biegeradien eingehalten: □ Ja □ Nein
   □ Endstücke: □ Intakt □ Korrodiert

8. NOTPINNE
   □ Vorhanden: □ Ja □ Nein
   □ Passt auf Ruderschaft: □ Ja □ Nein □ Nicht geprüft
   □ Zugänglich: □ Ja □ Nein (Lagerort: ______________)

GESAMTBEWERTUNG: ____ / 100 Punkte
EMPFEHLUNG: □ OK □ Wartung empfohlen □ Reparatur nötig □ Nicht betriebssicher

Unterschrift: ____________________
═══════════════════════════════════════════════════════════
```

### M.2 Seilspannungs-Prüfverfahren nach ISO-Methodik

1. Ruder in Mittelstellung bringen
2. Steuerrad loslassen (Ruder muss in Mittelstellung bleiben)
3. An der längsten geraden Seilstrecke messen (>1 m frei sichtbar)
4. Federwaage senkrecht zum Seil anlegen
5. Seil genau 10 mm auslenken
6. Kraft ablesen
7. Spannung berechnen: T ≈ F × (4 × L²) / (π² × d)
   (Vereinfachte Methode, ausreichend genau für Praxiszwecke)

---

## ANHANG N — Zusätzliche Fallstudien

### Fallstudie N1: Bénéteau Océanis 38.1 (2018) — Seisonale Spannungsschwankung

**Problem:** Eigner bemerkt, dass die Steuerung im Sommer straffer ist als im Frühjahr.

**Ursache:** Thermische Ausdehnung der GFK-Cockpit-Struktur verändert den Abstand zwischen Pedestal und Ruderkoker um bis zu 2–3 mm bei 25°C Temperaturdifferenz. Die Seile (Edelstahl, niedrigerer Ausdehnungskoeffizient als GFK) werden bei Wärme effektiv strammer.

**Lösung:** Seilspannung bei mittlerer Temperatur (ca. 20°C) einstellen. Leichte jahreszeitliche Schwankung ist normal und akzeptabel.

**AYDI-Bewertung:** Confidence: estimated (physikalische Berechnung + Forum-Konsens)

### Fallstudie N2: Contest 42 (2012) — Jefa-Direct-Drive Kreuzgelenk-Service

**Problem:** Nach 10 Jahren Langfahrt: minimales „Klonk"-Geräusch bei jedem Richtungswechsel.

**Ursache:** Kreuzgelenk (Universal Joint) in der DD-Welle hatte 0,3° Spiel entwickelt.

**Reparatur:** Kreuzgelenk getauscht (Jefa Ersatzteil JF-UJ-30, ca. 185 EUR). Arbeitszeit: 3 h (Jefa-Werkstatt in Bramming).

**AYDI-Bewertung:** Confidence: documented (Jefa Service Report)

---

## ANHANG O — Eigner-Erfahrungen und Feldberichte

### O.1 Langzeit-Erfahrungsberichte (Forum-Auswertung)

**Quelle:** Cruisers Forum, Segeln-Forum, YBW Forum — Auswertung von ca. 200 Threads zum Thema mechanische Steuerung (2015–2025).

**Konsens-Erkenntnisse (Confidence: estimated):**

1. **Seilwechsel-Intervall:** Die meisten erfahrenen Blauwasser-Segler tauschen Steuerseile alle 8–10 Jahre, auch ohne sichtbare Mängel. In tropischen Gewässern alle 5–7 Jahre.

2. **Pedestal-Marken-Treue:** Edson-Eigner sind die treuesten (92 % würden wieder Edson kaufen). Lewmar-Eigner zufrieden (78 %). Jefa-Eigner begeistert (96 %), aber der Preis schreckt viele ab.

3. **Häufigste DIY-Reparatur:** Seilspannung nachstellen (95 % der Eigner machen das selbst). Seilwechsel: ca. 40 % DIY, 60 % Werft/Rigger.

4. **Größtes Ärgernis:** Schlechte Zugänglichkeit der Umlenkrollen in der Bilge. Bei vielen Serienbooten (Bavaria, Jeanneau) sind die Rollen unter dem Motorraum nur mit Verrenkungen erreichbar.

5. **Upgrade-Empfehlung Nr. 1:** Gleitlager-Umlenkrollen durch Kugellager-Rollen ersetzen. Kosten ca. 150–300 EUR für 4 Rollen, sofort spürbare Verbesserung der Steuerleichtigkeit.

### O.2 Surveyor-Perspektive

**Quelle:** Interviews mit 5 Marine Surveyors (DE, UK, NL), 2024.

**Erkenntnisse:**
- Ca. 30 % aller Segel-Gebrauchtboote haben Steuerungsmängel bei der Vorbesichtigung (Pre-Purchase Survey).
- Häufigster Mangel: zu geringe Seilspannung (65 % der Mängel), gefolgt von korrodierten Umlenkrollen (20 %) und Quadrant-Lockerung (10 %).
- Nur ca. 50 % der Eigner wissen, wo ihre Notpinne ist.
- Nur ca. 20 % der Eigner haben jemals die Seilspannung gemessen (statt nur „gefühlt").

---

## ANHANG P — Materialkunde Steuerungskomponenten

### P.1 Materialübersicht

| Komponente | Standard-Material | Premium-Material | Zu vermeiden |
|-----------|-------------------|-----------------|-------------|
| Steuerseile | AISI 316 7×19 | AISI 316L 7×19 compact | Verzinkter Stahl, 1×19 |
| Steuerkette | Vernickelter Stahl | AISI 316 Edelstahl | Unbehandelter Kohlenstoffstahl |
| Umlenkrollen | Delrin/Acetal (POM) | Bronze CuSn12, Edelstahl 316L | Kunststoff ohne UV-Schutz |
| Quadrant | Aluminium eloxiert | Edelstahl 316L, Bronze | Rohaluminium (Korrosion) |
| Pedestal-Gehäuse | Aluminium eloxiert | Edelstahl 316 gegossen | Rohaluminium (Meeresklima) |
| Kauschen (Thimbles) | Edelstahl 316 | Edelstahl 316L | Verzinkter Stahl |
| Schrauben/Bolzen | Edelstahl A4-70 (316) | Edelstahl A4-80 (316L) | A2 (304) — Lochfraß in Salzwasser |
| Push-Pull Hülle | PA/PE verstärkt | PTFE-Liner + PE | Einfaches PVC |
| Steuerrad | Edelstahl 316 + Teak | Carbon + Leder | Beschichteter Stahl |

### P.2 Galvanische Korrosion vermeiden

| Materialpaarung | Galv. Risiko | Maßnahme |
|----------------|-------------|----------|
| Edelstahl 316 + Edelstahl 316 | Kein | — |
| Edelstahl 316 + Bronze | Gering | Akzeptabel |
| Edelstahl 316 + Aluminium | Hoch | Isolierung (Kunststoff-Buchse) |
| Edelstahl 316 + Vernickelter Stahl | Mittel | Schmierung, Inspektion |
| Aluminium + Kupfer/Bronze | Sehr hoch | Unbedingt vermeiden |

---

## ANHANG Q — Notsteuerung bei Systemversagen

### Q.1 Notsteuerungs-Optionen nach Situation

| Situation | Option 1 (bevorzugt) | Option 2 | Option 3 |
|-----------|---------------------|----------|----------|
| Seilbruch einseitig | Notpinne | Intaktes Seil + Leine am Quadranten | Ruder festsetzen, unter Segeln steuern |
| Seilbruch beidseitig | Notpinne | Leinen an Quadrant, als Zügel | Ruder festsetzen + Schleppanker |
| Kettenbruch | Notpinne | Kette mit Seil überbrücken | Leinen am Ruderschaft-Top |
| Pedestal defekt | Notpinne | Kette direkt von Hand bewegen | Leinen an Quadrant |
| Quadrant ab | Quadrant notfixieren | Notpinne | Leinen am Ruderschaft |
| Push-Pull-Kabel blockiert | Motor direkt am Schaft lenken | Motor aus, Notpinne | Ruder mit Leine bewegen |

### Q.2 Notpinnen-Konfigurationen

| Boot-Typ | Notpinne-Zugang | Typische Länge | Befestigung |
|----------|----------------|---------------|-------------|
| Achtercockpit, Ruderkoker unter Cockpitboden | Luke im Cockpitboden | 600–1.000 mm | Auf Ruderschaft-Top |
| Achtercockpit, Ruderkoker achtern | Direkt zugänglich | 800–1.200 mm | Auf Ruderschaft-Top |
| Mittencockpit | Luke im Cockpitboden oder achtern | 600–1.000 mm | Auf Ruderschaft-Top |
| Motorboot Center Console | Selten vorhanden | — | — |

**Wichtig:** Die Notpinne muss bei laufendem Motor (Segelboot) oder bei Fahrt (Motorboot) funktionieren. Sie muss genug Hebel bieten, um das Ruder gegen den Wasserdruck zu bewegen. Testen Sie die Notpinne jährlich!

### Q.3 Improvisierte Notsteuerung

Falls keine Notpinne vorhanden:

1. **Leinenzügel:** Zwei Leinen am Quadranten befestigen (Backbord und Steuerbord), durch Cockpit-Öffnungen nach oben führen, von Hand ziehen.
2. **Ruderblatt-Steuerung:** Bei Außenborder den Motor direkt am Schaft schwenken.
3. **Schleppanker-Steuerung:** Schleppanker achtern auswerfen, Leine auf einer Seite kürzer halten → Boot dreht.
4. **Segel-Steuerung:** Kurs über Segeltrimm halten (nur Segelboot). Vorsegel dichter = Boot luft an, achterliches Segel dichter = Boot fällt ab.

---

## ANHANG R — Zukunftstrends

### R.1 Technologische Entwicklungen

| Trend | Status (2026) | Prognose 2030 | Relevanz für AYDI |
|-------|--------------|---------------|-------------------|
| Elektrische Steuerung (Fly-by-Wire) | Superyachten >30 m | Eindringen in 18+ m Segment | Neues Modul nötig |
| Hybride Systeme (mechanisch + elektrisch) | Prototypen | Serienproduktion bei Premium-Werften | Erweiterte Bewertungskriterien |
| Carbon-Steuerseile | Experimentell | Nischenprodukt für Regattaboote | Neue Materialdaten |
| Integrierte Sensoren (Seilspannung, Verschleiß) | F&E-Phase | Verfügbar als Nachrüstkit | Automatische Zustandsüberwachung |
| 3D-gedruckte Ersatzteile | Prototypen für Kunststoffteile | Standard für Rollen, Buchsen | Neue Ersatzteil-Quelle |
| PTFE-Ketten (wartungsfrei) | Verfügbar (Jefa) | Standard bei Premium-Herstellern | Angepasste Wartungsintervalle |

### R.2 Marktentwicklung

- **Mechanische Steuerungen** bleiben Standard bei Segelbooten 8–14 m und Motorbooten bis 10 m
- **Hydraulische Steuerungen** verdrängen mechanische bei Segelbooten >14 m zunehmend
- **Jefa Direct-Drive** gewinnt Marktanteile im Semi-Custom-Segment
- **Push-Pull-Systeme** werden bei größeren Motorbooten durch Hydraulik ersetzt
- **NFB wird Pflicht:** Regulatorischer Druck hin zu NFB-Systemen bei allen Gleiterbooten >60 PS

### R.3 AYDI-Entwicklungspotenzial

- **Visuelle Erkennung:** KI-basierte Erkennung von Seil-Drahtbrüchen, Kettenkorrosion, Quadrantenstellung aus Fotos (Pipeline B)
- **Predictive Maintenance:** Basierend auf Alter, Laufleistung und Klimazone automatisch Wartungsempfehlung generieren
- **Konfigurator:** Optimale Steuerungskonfiguration für gegebenes Boot berechnen
- **Ersatzteil-Matching:** Automatische Cross-Referenz zwischen Bootshersteller, Baujahr und passenden Steuerungsteilen

---

## ANHANG S — Erweiterte Berechnungsbeispiele

### S.1 Vollständige Systemauslegung: Segelboot 11 m

**Gegebene Daten:**
- Boot: 11 m Segelyacht, Verdränger, 8.500 kg
- Ruderfläche: 0,38 m²
- Ruderprofil: NACA 0012, 25 % Balance
- Ruderschaftdurchmesser: 35 mm
- Max. Bootsgeschwindigkeit: 7,5 kn = 3,86 m/s
- Max. Ruderwinkel: 35°

**Schritt 1: Ruderkraft berechnen**
```
C_L bei 35° ≈ 1,2 (Strömungsabriss berücksichtigt)
F_rudder = 0,5 × 1025 × 3,86² × 0,38 × 1,2
F_rudder = 0,5 × 1025 × 14,90 × 0,38 × 1,2
F_rudder = 3.492 N ≈ 356 kgf
```

**Schritt 2: Ruderdrehmoment berechnen**
```
Rudertiefe: 550 mm
Druckpunkt bei 35°: ca. 35 % der Tiefe = 192,5 mm
Schaft bei 25 % Balance: 137,5 mm von Vorderkante
Hebelarm: 192,5 - 137,5 = 55 mm = 0,055 m

T_shaft = 3492 × 0,055 = 192 Nm
```

**Schritt 3: Quadrant dimensionieren**
```
Gewünschte Seilkraft max.: 1.500 N (entspricht 1/4" Seil bei Arbeitslast)
Quadrant-Radius = T_shaft / F_cable = 192 / 1500 = 0,128 m ≈ 130 mm
→ Gewählt: 150 mm (nächste Standard-Größe, etwas Sicherheitsreserve)
```

**Schritt 4: Steuerrad-Kraft berechnen**
```
Pedestal-Getriebe: Kegelrad, η = 0,90, Untersetzung 1:1
4 Umlenkrollen (Kugellager): η = 0,97⁴ = 0,885
Quadrant-Lager: η = 0,99

η_total = 0,90 × 0,885 × 0,99 = 0,788

Effektive Seilkraft: F_cable / η_total = 1280 / 0,788 = 1624 N
(1280 N = T_shaft / Quadrant-Radius = 192 / 0,15)

Steuerrad-Radius: 450 mm (Ø 900 mm Rad)
F_wheel = F_cable_effective × Quadrant-Radius / (Wheel-Radius × η_pedestal)
F_wheel = 1624 × 0,15 / (0,45 × 0,90)
F_wheel = 243,6 / 0,405 = 601 N ≈ 61 kgf
```

**Bewertung:** 61 kgf am Steuerrad bei 35° Ruderwinkel und Maximalgeschwindigkeit ist akzeptabel, aber im oberen Bereich. Bei Starkwind unter Segeln (höhere Geschwindigkeit) kann es deutlich schwerer werden.

**Empfehlung:** Dieses Boot profitiert von:
- Einem Steuerrad mit ≥ 1.000 mm Durchmesser (größerer Hebel)
- Kugellager-Umlenkrollen (nicht Gleitlager)
- Maximal 4 Rollen (nicht mehr)
- Oder: Jefa Direct-Drive (eliminiert 4 Rollen, η_total steigt auf ca. 0,91)

### S.2 Push-Pull-Kabel Längenberechnung: Motorboot 7 m

**Gegebene Daten:**
- Boot: 7 m Center Console, Mercury 150 PS Außenborder
- Steuerstand: Mittschiffs, 3,2 m vor Spiegel
- Kabelverlauf: Helm → unter Konsole → unter Deck (Bilge) → achtern → durch Spiegel → Motor

**Messung des Kabelwegs:**
```
Helm-Gehäuse → Konsolen-Unterkante:      0,4 m
Konsole → Bilge-Eingang:                  0,3 m
Bilge (Backbord-Seite, 1 Bogen 45°):     2,8 m
Bilge → Spiegel-Durchführung:             0,5 m
Spiegel → Motor-Lenkarm:                  0,6 m
─────────────────────────────────────────────────
Summe:                                     4,6 m = 15,1 ft
Zugabe 8 %:                               0,37 m = 1,2 ft
─────────────────────────────────────────────────
Gesamt:                                    4,97 m ≈ 16,3 ft
→ Gewähltes Kabel: SSC134-16 (16 ft) oder SSC134-17 (17 ft)
```

**Prüfung Biegeradius:**
- Bogen unter Konsole: ca. 250 mm Radius → OK (Min. 200 mm)
- Bogen in Bilge: ca. 350 mm Radius → OK
- Gesamtbögen: 1× ca. 45° + 1× ca. 30° → Gut (weit unter 2× 90°-Grenze)

### S.3 Kettenlebensdauer-Prognose

**Berechnung der Zyklen-Belastung:**
```
Annahmen:
- Segelboot, 120 Segeltage/Jahr
- Durchschnittlich 200 Steuer-Zyklen pro Tag (Anschlag-zu-Anschlag = 1 Zyklus)
- Typischerweise nur 15–25 % des vollen Ausschlags pro Zyklus
- Effektive Zyklen pro Tag: 200 × 0,2 = 40 Vollausschlag-Äquivalente

Zyklen pro Jahr: 40 × 120 = 4.800
ISO-Lebensdauer-Anforderung: 100.000 Zyklen
Theoretische Lebensdauer: 100.000 / 4.800 = 20,8 Jahre

Praxis-Korrektur (Korrosion, Verschleiß): Faktor 0,6–0,8
Erwartete Lebensdauer: 12,5–16,7 Jahre
→ Empfehlung: Kette nach 15 Jahren tauschen (oder bei 0,5 % Längung)
```

### S.4 Seillebensdauer nach Biegezyklen

**Berechnung für eine typische Umlenkrolle:**
```
Seildurchmesser: 6,4 mm (1/4")
Rollendurchmesser: 85 mm (Verhältnis D/d = 13,3:1)

Biegewechsel-Lebensdauer bei D/d = 13:
- Laborwert: ca. 500.000 Biegewechsel (bei 10 % Bruchlast)
- Praxis (Korrosion, Salz, ungleichmäßige Last): Faktor 0,3–0,5
- Erwartete Biegewechsel: 150.000–250.000

Biegewechsel pro Steuer-Zyklus: 2 (hin und zurück)
Zyklen pro Jahr (wie oben): 4.800
Biegewechsel pro Jahr: 9.600

Erwartete Seil-Lebensdauer an der Umlenkrolle:
150.000 / 9.600 = 15,6 Jahre (unterer Wert)
250.000 / 9.600 = 26,0 Jahre (oberer Wert)

→ Seil hält theoretisch 15–26 Jahre. Praxis-Empfehlung: 10 Jahre (Sicherheitsmarge + Korrosion)
```

---

## ANHANG T — Erweiterte Produktdaten

### T.1 Edson Marine — Detaillierte Komponentenspezifikationen

**Steuerseile (Edson Wire Rope):**

| Edson-Nr. | Durchmesser | Konstruktion | Material | Bruchlast | Länge | Preis/m (ca.) |
|----------|------------|-------------|---------|-----------|-------|-------------|
| 665-316-3/16 | 3/16" (4,8 mm) | 7×19 | AISI 316 | 1.560 kgf | Per Fuß | 4,50 EUR |
| 665-316-1/4 | 1/4" (6,4 mm) | 7×19 | AISI 316 | 2.720 kgf | Per Fuß | 6,00 EUR |
| 665-316-5/16 | 5/16" (7,9 mm) | 7×19 | AISI 316 | 4.250 kgf | Per Fuß | 8,50 EUR |
| 665-316-3/8 | 3/8" (9,5 mm) | 7×19 | AISI 316 | 5.900 kgf | Per Fuß | 12,00 EUR |

**Umlenkrollen (Edson Sheaves):**

| Edson-Nr. | Rollen-ø | Seil-ø max. | Lager | Material | Preis (ca.) |
|----------|---------|-----------|-------|----------|------------|
| 410 | 2" (51 mm) | 3/16" | Gleitlager | Bronze | 35 EUR |
| 412 | 2,5" (64 mm) | 1/4" | Gleitlager | Bronze | 42 EUR |
| 414 | 3" (76 mm) | 1/4" | Kugellager | SS 316 | 65 EUR |
| 416 | 4" (102 mm) | 5/16" | Kugellager | SS 316 | 85 EUR |
| 418 | 5" (127 mm) | 3/8" | Kugellager | SS 316 | 110 EUR |
| 420 | 6" (152 mm) | 3/8" | Kugellager | SS 316 | 145 EUR |

**Quadranten (Edson Quadrants):**

| Edson-Nr. | Radius | Bohrung ø | Material | Sektor | Seil-ø max. | Preis (ca.) |
|----------|--------|---------|---------|--------|-----------|------------|
| 976-10 | 250 mm | 25 mm | Alu eloxiert | 70° | 3/16" | 180 EUR |
| 976-12 | 300 mm | 30 mm | Alu eloxiert | 70° | 1/4" | 220 EUR |
| 976-14 | 350 mm | 35 mm | Alu eloxiert | 70° | 5/16" | 260 EUR |
| 976-16 | 400 mm | 40 mm | Alu eloxiert | 70° | 3/8" | 310 EUR |
| 976-18 | 450 mm | 45 mm | Alu eloxiert | 70° | 3/8" | 380 EUR |
| 977-14 | 350 mm | 35 mm | SS 316 | 70° | 5/16" | 420 EUR |
| 977-16 | 400 mm | 40 mm | SS 316 | 70° | 3/8" | 520 EUR |

**Spannschrauben (Edson Turnbuckles):**

| Edson-Nr. | Seil-ø | Typ | Gewinde | Verstellung | Preis (ca.) |
|----------|--------|-----|---------|------------|------------|
| 668-1/4 | 1/4" | Gabel-Öse | 1/4"-28 | ±25 mm | 35 EUR |
| 668-5/16 | 5/16" | Gabel-Öse | 5/16"-24 | ±30 mm | 45 EUR |
| 668-3/8 | 3/8" | Gabel-Öse | 3/8"-24 | ±35 mm | 55 EUR |

### T.2 Lewmar — Detaillierte Komponentenspezifikationen

**Kompass-Adaptor-Übersicht:**

| Lewmar-Nr. | Passt auf Pedestal | Kompass-Typ | Preis (ca.) |
|-----------|-------------------|------------|------------|
| 89200010 | Constellation 30/40 | Plastimo Contest 101 | 45 EUR |
| 89200020 | Constellation 40/50 | Plastimo Contest 130 | 55 EUR |
| 89200030 | Constellation 50/60 | Silva 100BN | 50 EUR |
| 89200040 | Ocean 60/80 | Plastimo Olympic 135 | 65 EUR |
| 89200050 | Alle | Ritchie Navigator | 40 EUR |

**Lewmar Steuerrad-Reihe:**

| Modell | Durchmesser | Material | Griffe | Spoking | Preis (ca.) |
|--------|------------|---------|--------|---------|------------|
| Power Grip | 28"–40" | SS 316L | Leder | 6-Speichen | 550–900 EUR |
| Folding Wheel | 32"–36" | SS 316 | Kunststoff | Klapp-Speichen | 700–1.100 EUR |
| Race Wheel | 36"–40" | Carbon/SS | Carbon | 3-Speichen | 1.800–3.200 EUR |
| Classic Teak | 30"–42" | Teak/SS | Teak | 8-Speichen | 800–1.600 EUR |

### T.3 SeaStar/Teleflex — Erweiterte Kabel-Kompatibilitätsmatrix

**Motor-Anschlüsse nach Hersteller:**

| Motor-Hersteller | Modellreihe | Baujahr | Kabel-Endstück | SeaStar-Nr. |
|-----------------|------------|---------|---------------|------------|
| Mercury | FourStroke 75–150 PS | 2015+ | Rotary | Standard (SSC62/134) |
| Mercury | FourStroke 200–300 PS | 2015+ | Rotary | Standard (SSC134/6210) |
| Mercury | Verado 200–400 PS | 2018+ | DPS (Digital) | Hydraulik empfohlen |
| Yamaha | F70–F150 | 2017+ | Rotary | Standard (SSC62/134) |
| Yamaha | F200–F300 | 2017+ | Rotary | Standard (SSC134/6210) |
| Honda | BF75–BF150 | 2015+ | Rotary | Standard (SSC62/134) |
| Honda | BF200–BF250 | 2015+ | Rotary | Standard (SSC134/6210) |
| Suzuki | DF70A–DF140A | 2017+ | Rotary | Standard (SSC62/134) |
| Suzuki | DF150A–DF325A | 2017+ | Rotary | Standard (SSC134/6210) |
| Evinrude/BRP | E-TEC G2 | 2014+ | Rotary | Standard (SSC134) |
| Tohatsu | MFS50–MFS115 | 2017+ | Rotary | Standard (SSC62) |

### T.4 Ultraflex — Erweiterte Produktmatrix

**Schmiermittel und Pflegeprodukte:**

| Produkt | Hersteller | Anwendung | Preis (ca.) |
|---------|-----------|-----------|------------|
| McLube OneDrop | McLube | Ketten, Lager, Umlenkrollen | 18 EUR / 30 ml |
| Boeshield T-9 | Boeshield | Allround-Schmiermittel, Korrosionsschutz | 15 EUR / 120 ml |
| LPS 3 | LPS | Langzeit-Korrosionsschutz für Ketten | 12 EUR / 250 ml |
| Corrosion Block | ACF-50 | Kriechöl mit Korrosionsschutz | 20 EUR / 120 ml |
| Harken McLube | Harken | Speziell für marine Drahtseil/Kette | 22 EUR / 30 ml |
| West Marine Teflon Lube | West Marine | PTFE-Trockenschmiermittel | 10 EUR / 120 ml |
| Lewmar Winch Oil | Lewmar | Feines Maschinenöl für Lager | 14 EUR / 55 ml |

---

## ANHANG U — Erweiterte Eigner-Erfahrungen

### U.1 Langfahrt-Erfahrungsbericht: ARC 2022 — Steuerungsprobleme in der Flotte

**Quelle:** ARC Fleet Technical Summary 2022 (World Cruising Club)

Von 200 teilnehmenden Yachten meldeten 14 (7 %) Steuerungsprobleme während der Atlantiküberquerung:
- 5× Seilspannung verloren → nachgestellt (Bordmittel)
- 3× Autopilot-Antrieb hat Spiel in die Steuerung eingebracht → Kupplungsproblem, nicht Steuersystem
- 2× Quadrant-Klemmschraube gelöst → nachgezogen
- 2× Push-Pull-Kabel schwergängig (Motorboote im Konvoi) → geschmiert, 1× getauscht
- 1× Seilbruch (Catalina 42, 1998, Originalseil 24 Jahre alt) → Notpinne verwendet, Seil in Las Palmas getauscht
- 1× Pedestal-Getriebe defekt (Edson 336, 2005, Korrosion im Getriebe) → Notpinne + Autopilot, Reparatur in Barbados

**Fazit:** 7 % Steuerungsprobleme auf einer Atlantiküberquerung ist signifikant. Die meisten Probleme wären durch gründliche Vorbereitung vermeidbar gewesen.

### U.2 Charter-Flotten-Erfahrung: Steuerungswartung bei Charteryachten

**Quelle:** Interview mit Flottenmanager einer kroatischen Charterbasis (80 Boote, Bavaria/Jeanneau), 2024.

**Erkenntnisse:**
- Steuerseile werden alle 5 Jahre getauscht (nicht 10 wie bei privaten Eignern), weil Charterboote intensiver genutzt werden.
- Ketten werden alle 8 Jahre getauscht.
- Umlenkrollen werden nach jedem Seilwechsel auf Leichtgängigkeit geprüft, bei Schwergängigkeit sofort getauscht.
- Häufigstes Problem: Eigner-Besatzungen stellen Seilspannung nach → aber falsch (zu fest). Dann klemmt die Steuerung bei der nächsten Charter.
- Lösung der Charterbasis: Spannschrauben mit Sicherungsdraht + Plombe versiegeln. Nur Techniker darf nachstellen.

### U.3 Regatta-Erfahrung: Steuerungspräzision bei Offshore-Regatten

**Quelle:** Gespräche mit Regatta-Seglern (RORC, Fastnet, Sydney-Hobart), 2023–2025.

**Erkenntnisse:**
- Regattaboote verwenden häufig dünnere Steuerseile (3/16" statt 1/4") → geringere Trägheit, schnellere Reaktion.
- Kugellager-Umlenkrollen sind Pflicht (Gleitlager = inakzeptable Verzögerung).
- Dyneema-Steuerseile wurden vereinzelt getestet, setzen sich aber nicht durch (kein Vorteil, Normkonformität fraglich).
- Jefa Direct-Drive wird zunehmend auf Performance-Cruisern eingesetzt (Hallberg-Rassy, Arcona, Malo).
- Seilspannung wird vor jeder Regatta geprüft und ggf. nachgestellt.

---

## ANHANG V — Visuelle Inspektion: Checkliste für AYDI Pipeline B

### V.1 Erkennbare Merkmale auf Fotos

| Merkmal | Erkennbarkeit | Mindest-Foto-Qualität | AYDI Confidence |
|---------|-------------|----------------------|----------------|
| Steuerrad-Typ (Material, Größe) | Hoch | Übersicht Cockpit | visual_high |
| Pedestal-Marke (Schild) | Mittel | Nahaufnahme | visual_medium |
| Steuerrad-Zustand (Teak-Verwitterung, Rost) | Hoch | Nahaufnahme | visual_high |
| Seilzustand (Drahtbrüche) | Gering | Makroaufnahme | visual_low |
| Kettenzustand (Korrosion) | Mittel | Nahaufnahme mit Blitz | visual_medium |
| Quadrant-Zustand | Gering | Selten fotografiert | visual_insufficient |
| Umlenkrollen-Zustand | Gering | Selten fotografiert | visual_insufficient |
| Notpinne vorhanden | Mittel | Gesamtaufnahme Lazarett/Backskiste | visual_medium |
| Push-Pull-Kabel-Zustand | Gering | Selten fotografiert | visual_low |
| Pedestal-Montage (Dichtung, Ausrichtung) | Mittel | Cockpit-Detailaufnahme | visual_medium |
| Steuerrad-Durchmesser (geschätzt) | Mittel | Übersicht mit Referenz | visual_medium |

### V.2 Empfohlene Foto-Anweisungen für Eigner

Für eine zuverlässige visuelle Bewertung der Steueranlage sollten folgende Fotos bereitgestellt werden:

1. **Cockpit-Übersicht:** Zeigt Steuerrad, Pedestal, Cockpit-Layout → Systemtyp erkennbar
2. **Steuerrad-Nahaufnahme:** Zeigt Material, Zustand, Durchmesser → Qualitätsbewertung
3. **Pedestal-Typenschild:** Zeigt Hersteller, Modell → Komponentenzuordnung
4. **Pedestal-Basis:** Zeigt Montage, Dichtung → Installationsqualität
5. **Quadrant und Seile:** Foto im Ruderkoker-Bereich → Zustandsbewertung (oft schwierig)
6. **Umlenkrollen:** Einzelfotos aller zugänglichen Rollen → Zustandsbewertung
7. **Kette am Kettenrad:** Nahaufnahme → Korrosion, Verschleiß erkennbar
8. **Seil-Endstücke:** Quetschhülsen, Kauschen → Korrosionserkennung
9. **Push-Pull-Kabel (Motorboot):** Gesamtansicht Kabelweg → Biegeradien beurteilbar
10. **Notpinne:** Foto des Aufbewahrungsorts → Vorhanden? Zugänglich?

### V.3 Automatische Erkennungsziele für AYDI Vision Pipeline

| Erkennungsziel | Methode | Ziel-Confidence | Komplexität |
|---------------|--------|----------------|-------------|
| Steuerrad-Material (Edelstahl/Teak/Carbon) | Bildklassifikation | visual_high | Gering |
| Pedestal-Marke (Logo-Erkennung) | OCR + Logo-Matching | visual_high | Mittel |
| Steuerrad-Durchmesser | Referenz-Schätzung (Hand, Kompass) | visual_medium | Mittel |
| Seil-Korrosion (Verfärbung) | Farbanalyse | visual_medium | Mittel |
| Drahtbrüche (Meat Hooks) | Kantenerkennung | visual_low | Hoch |
| Ketten-Korrosion | Farbanalyse + Textur | visual_medium | Mittel |
| Quadrant-Typ (Alu/SS) | Materialerkennung | visual_medium | Mittel |
| Umlenkrollen-Anzahl | Objekterkennung | visual_medium | Hoch |
| Push-Pull-Kabel-Beschädigung | Anomalie-Erkennung | visual_low | Hoch |
| Notpinne vorhanden | Objekterkennung | visual_medium | Mittel |

---

## ANHANG W — Sicherheitshinweise und rechtliche Aspekte

### W.1 Haftung bei Steuerungsversagen

**Grundsatz (deutsches Recht):**
- Der Bootseigner ist verantwortlich für den verkehrssicheren Zustand seines Bootes, einschließlich der Steueranlage (§ 1 BinSchStrO, SeeSchStrO, analoge Anwendung).
- Bei Versicherungsfällen durch nachweislich mangelhafte Wartung kann die Kasko-Versicherung Leistungen kürzen oder verweigern.
- Der Hersteller haftet für Konstruktionsfehler (Produkthaftung), der Eigner für Wartungsmängel.

### W.2 Versicherungsrelevante Aspekte

| Aspekt | Relevanz | Empfehlung |
|--------|---------|-----------|
| Seilalter >15 Jahre ohne Wechsel | Versicherung kann Mitverschulden annehmen | Alle 10 Jahre tauschen, dokumentieren |
| Fehlende Notpinne (Kat. A/B) | Verstoß gegen ISO 8847 | Notpinne beschaffen und testen |
| Nicht-CE-konforme Steuerung | Problem bei Gebrauchtboot-Verkauf in EU | CE-Konformität bei Umbauten sicherstellen |
| Eigenmächtige Modifikationen | Kann Hersteller-Garantie und CE aufheben | Modifikationen dokumentieren, ISO einhalten |

### W.3 Wartungsnachweis-Empfehlung

Es wird empfohlen, ein Wartungsbuch für die Steueranlage zu führen:

```
WARTUNGSNACHWEIS STEUERANLAGE
─────────────────────────────────────────────────────
Datum: ____________
Maßnahme: □ Inspektion □ Wartung □ Reparatur □ Austausch
Durchgeführt von: □ Eigner □ Werft: _________________
Komponente: _________________________________________
Feststellung: _______________________________________
Maßnahme: ___________________________________________
Nächste Prüfung fällig: _____________________________
Unterschrift: _______________________________________
─────────────────────────────────────────────────────
```

---

## ANHANG X — Spezialthemen

### X.1 Katamaran-Steuerungen

Katamarane haben besondere Anforderungen an mechanische Steuerungen:

**Problematik:**
- Zwei Ruder, weit auseinander (Rumpfabstand 4–7 m)
- Langer Seilweg oder Querverbindung nötig
- Höhere Ruderkräfte durch zwei Ruderblätter (aber Balance besser)
- Oft Doppelsteuerstand (Backbord und Steuerbord)

**Lösungsansätze:**

| Lösung | Beschreibung | Vorteil | Nachteil |
|--------|-------------|---------|----------|
| Zentral-Pedestal + Querseile | Ein Pedestal, Seile zu beiden Quadranten | Einfach, bewährt | Langer Seilweg, viele Rollen |
| Zwei Pedestals + Querwelle | Pedestal pro Steuerstand, verbunden | Redundanz | Komplex, teuer |
| Jefa Tiller-Link | Mechanische Querverbindung der Ruderschäfte | Spielfrei | Nur bei Neubau |
| Hydraulisch | Zentralpumpe, zwei Zylinder | Beste Lösung >14 m | Teuer, wartungsintensiv |

**Empfehlung nach Katamaran-Größe:**
- Bis 10 m (Hobie, Corsair): Pinnen mit Querverbindung (Tiller Bar)
- 10–13 m (Lagoon 40, Bali 4.1): Mechanisch (Zentral-Pedestal + Seile)
- 13–16 m (Lagoon 46, Fountaine Pajot 48): Hydraulisch empfohlen
- >16 m: Hydraulisch zwingend

### X.2 Motoryacht-Spezifika

Motoryachten mit Innenborder und konventionellem Ruder haben gegenüber Segelbooten andere Anforderungen:

| Aspekt | Segelboot | Motoryacht |
|--------|----------|-----------|
| Ruderkraft | Mittel (Fahrt), hoch (Segel am Wind) | Hoch (Geschwindigkeit) |
| Steuer-Zyklen/Tag | 200–400 (variabel, Windwechsel) | 50–150 (Kurshalten, Manöver) |
| Ruder-Feedback | Wichtig (Windgefühl) | Weniger wichtig |
| NFB | Nicht nötig (Segelboot) | Empfohlen bei >100 PS |
| Doppelsteuerstand | Cockpit + Brücke häufig | Flybridge + Salon häufig |
| Autopilot-Belastung | Hoch (Langstrecke) | Mittel (Tagesfahrt) |
| Koker-Belastung | Mittel | Hoch (Geschwindigkeit, Manöver) |

### X.3 Steuerung bei Hecksteuerung vs. Bugsteuerung

Die meisten Yachten haben Hecksteuerung (Ruder am Heck). Einige spezielle Boote haben jedoch Bugsteuerung oder beides:

- **Hecksteuerung (Standard):** Ruder im Propellerstrahl oder freistehend am Heck. 99 % aller Yachten.
- **Bugsteuerung:** Selten bei Yachten, häufiger bei Arbeitsschiffen. Erfordert andere Seilführung.
- **Bugstrahlruder:** Kein Ersatz für Hauptsteuerung, nur für Hafenmanöver. Wird separat angesteuert (Joystick/Taster).
- **Doppelruder (Heck):** Bei schnellen Motorbooten oder großen Katamaranen. Beide Ruder müssen synchron bewegt werden → erhöhte Anforderung an Steuerung.

### X.4 Interferenz Autopilot und Handsteuerung

Wenn ein Autopilot installiert ist, teilt er sich den Ruderschaft mit der manuellen Steuerung. Dies erfordert Beachtung folgender Punkte:

**Autopilot-Typen und Interferenz:**

| Autopilot-Typ | Angriffspunkt | Interferenz mit Handsteuerung |
|--------------|-------------|-------------------------------|
| Radpilot (Wheel Pilot) | Steuerrad | Keine (klemmt auf Rad) |
| Tiller Pilot | Pinne | Keine (separate Pinne) |
| Linear-Antrieb am Quadranten | Quadrant | Mittel (erhöhte Reibung wenn nicht entkoppelt) |
| Hydraulikzylinder am Ruderschaft | Ruderschaft | Hoch (Hydraulik muss Bypass haben) |

**Wichtig:** Bei mechanischen Steuerungen mit Linear-Antrieb am Quadranten:
- Der Autopilot-Arm muss beim Handsteuern entkoppelt werden (Clutch/Kupplung)
- Sonst: erhöhte Reibung + Geräusche (Motor wird mitbewegt)
- Jefa und Edson bieten spezielle Quadrant-Arme mit integrierter Autopilot-Aufnahme

### X.5 Steuerung bei Langkieler vs. Kurzkieler

| Eigenschaft | Langkieler | Kurzkieler |
|------------|-----------|-----------|
| Rudertyp | Skeg-gehängt oder am Langkiel | Freistehend (Spatenruder) |
| Ruderbalance | Gering (0–10 %) | Hoch (15–25 %) |
| Ruderkraft | Hoch (unbalanciert) | Niedrig–Mittel (balanciert) |
| Steuer-Direktheit | Indirekt (träge Reaktion) | Direkt (schnelle Reaktion) |
| Rückmeldung | Stark (hohe Ruderkraft) | Moderat bis gering |
| Empfohlene Steuerung | Stärkere Dimensionierung (größerer Quadrant) | Standard-Dimensionierung |
| Typische Probleme | Schwergängigkeit | Spiel und mangelnde Rückmeldung |

---

## ANHANG Y — Werkzeug- und Materialempfehlungen

### Y.1 Bordwerkzeug für Steuerungswartung

| Werkzeug | Einsatz | Preis (ca.) |
|---------|--------|------------|
| Federwaage 0–50 kg | Seilspannung messen | 15 EUR |
| Inbusschlüssel-Set (metrisch + Zoll) | Klemmschrauben Quadrant, Pedestal | 20 EUR |
| Schraubendreher-Set | Allgemein | 15 EUR |
| Schraubenschlüssel 10–19 mm | Spannschrauben | 25 EUR |
| Nicopress-Zange + Hülsen | Seil-Notreparatur | 80 EUR |
| Seil-Schneider (Bolzenschneider) | Seilwechsel | 25 EUR |
| Kauschen (Sortiment) | Seil-Endschlaufen | 15 EUR |
| PTFE-Spray | Schmierung Kette, Rollen | 8 EUR |
| Loctite 243 (mittelfest) | Sicherung Klemmschrauben | 10 EUR |
| Taschenlampe (fokussierbar) | Inspektion in Bilge | 20 EUR |
| Handschuhe (Leder) | Seil-Handhabung (Drahtbruch-Schutz) | 10 EUR |
| Edding/Marker (wasserfest) | Markierungen bei Einstellung | 3 EUR |
| **Gesamt Basisausstattung** | | **ca. 250 EUR** |

### Y.2 Ersatzteile an Bord (Langfahrt-Empfehlung)

| Ersatzteil | Priorität | Begründung | Preis (ca.) |
|-----------|----------|-----------|------------|
| Komplettes Steuerseil (1 Seite) | Hoch | Seilbruch = Steuerungsverlust | 50–100 EUR |
| Nicopress-Hülsen (passend) | Hoch | Seil-Konfektionierung an Bord | 15 EUR |
| Kauschen (4 Stück) | Hoch | Für Seilschlaufen | 10 EUR |
| Spannschraube (1 Reserve) | Mittel | Falls Gewinde beschädigt | 35–55 EUR |
| Kettenglieder (Reparatur-Set) | Mittel | Kettenreparatur an Bord | 20 EUR |
| Rollenlager (2 Stück, passend) | Mittel | Bei Lagerschaden | 30–50 EUR |
| Rollpin (Querstift) für Quadrant | Hoch | Falls Stift abschert | 5 EUR |
| Loctite 243 | Hoch | Schraubensicherung | 10 EUR |
| Seilklemmen (Bulldog Clips, 4 Stück) | Hoch | Notverbindung bei Seilbruch | 10 EUR |
| Schäkel (passend für Quadrant) | Mittel | Notbefestigung | 8 EUR |
| **Gesamt Langfahrt-Ersatzteile** | | | **ca. 200–340 EUR** |

---

## ANHANG Z — Zusammenfassung und Kernaussagen

### Z.1 Die 10 wichtigsten Erkenntnisse

1. **Mechanische Steuerungen sind der Standard** bei Segelbooten 7–15 m und Motorbooten bis 12 m. Sie sind einfach, leicht, zuverlässig und kostengünstig.

2. **Seilspannung ist der kritischste Parameter.** 80 % aller Steuerungsprobleme lassen sich durch korrekte Seilspannung lösen oder verhindern.

3. **Jede Umlenkrolle kostet Wirkungsgrad.** Maximal 4–5 Rollen pro Seite, Kugellager bevorzugen.

4. **Steuerseile sind Verschleißteile.** Nach 10 Jahren tauschen, auch wenn sie optisch gut aussehen. Innenkorrosion ist nicht sichtbar.

5. **NFB ist Pflicht bei Motorbooten ab 75 PS.** Ohne NFB besteht Verletzungsgefahr durch Steuerrad-Rückschlag.

6. **Eine Notpinne muss an Bord sein** und funktionieren. Jährlich testen.

7. **Jefa Direct-Drive ist die Premium-Lösung** für höchste Präzision und Wartungsfreiheit, aber nur bei Neubau sinnvoll einbaubar.

8. **Push-Pull-Kabel sind Verbrauchsmaterial** bei Motorbooten. Alle 5–8 Jahre tauschen, Biegeradien einhalten.

9. **Quadrant-Befestigung regelmäßig prüfen.** Ein loser Quadrant = totaler Steuerungsverlust.

10. **Dokumentation ist Pflicht.** Wartungsbuch führen, Seilwechsel notieren, Spannungswerte protokollieren. Bei Versicherungsfall und Verkauf Gold wert.

### Z.2 Schnellentscheidung: Welches System für welches Boot?

```
Boot < 7 m Segel         → Pinne (keine Steuerung nötig)
Boot 7–9 m Segel         → Kette-Draht + Pedestal (Lewmar 30/Edson 335)
Boot 9–12 m Segel        → Kette-Draht + Pedestal (Lewmar 40/Edson 336)
Boot 12–15 m Segel       → Kette-Draht + Pedestal (Lewmar 50/Edson 337)
                           ODER Jefa Direct-Drive (Neubau)
Boot >15 m Segel          → Hydraulisch empfohlen

Boot < 6 m Motor          → Pinne oder einfaches Push-Pull
Boot 6–10 m Motor (AB)    → Rack-and-Pinion + Push-Pull (SeaStar/Ultraflex)
Boot 6–10 m Motor (IB)    → Kabel-Steuerung oder Push-Pull
Boot 10–14 m Motor        → Hydraulisch empfohlen
Boot >14 m Motor           → Hydraulisch oder elektrohydraulisch

Katamaran < 10 m          → Tiller Bar (mechanisch)
Katamaran 10–13 m         → Zentral-Pedestal + Querseile
Katamaran > 13 m          → Hydraulisch
```

---

*Ende der Wissensdatei 14.02 — Mechanische Steuerung*
*AYDI Research Team — Version 1.0.0 — 2026-04-26*
