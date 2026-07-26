---
title: "Hochlast-Blöcke und Umlenkrollen im Yachtbau"
kategorie: "10 Blöcke und Umlenkrollen"
unterkategorie: "04 Hochlast-Blöcke"
version: "1.0.0"
datum: "2026-04-25"
autor: "AYDI Research"
status: "validated"
confidence_quellen:
  - measured: "Hersteller-Datenblätter, Laborprüfungen, Bruchlast-Zertifikate"
  - documented: "Hersteller-Kataloge, Segelfachpresse, Forum-Konsens"
  - estimated: "Erfahrungswerte, Quervergleiche, Feldbeobachtungen"
  - benchmark: "Marktdurchschnitte, Branchenstandards, Regatta-Erfahrung"
tags:
  - hochlast
  - bloecke
  - umlenkrollen
  - deck_organizer
  - turning_block
  - cheek_block
  - mainsheet
  - vang
  - backstag
  - running_backstay
  - flaschenzug
  - talje
  - laufendes_gut
  - deck_hardware
  - rigg_beschlaege
boot_klassen:
  - fahrtensegler (8–14m)
  - performance_cruiser (10–16m)
  - blauwasseryacht (12–18m)
  - regattayacht (8–20m)
  - maxi_yacht (18–25m)
  - superyacht (18m+)
---

# 10.04 — Hochlast-Blöcke und Umlenkrollen im Yachtbau: Vollständige Wissensreferenz

> **AYDI Wissensdatei 10.04** — Kategorie 10: Blöcke und Umlenkrollen
> **Confidence-Quelle:** measured (Hersteller-TDS, Bruchlast-Zertifikate), documented (Hersteller-Kataloge, Fachliteratur, Regatta-Erfahrung), estimated (Erfahrungswerte)
> **Letzte Aktualisierung:** 2026-04-25

---

## Inhaltsverzeichnis

1. [Einführung und Übersicht](#1-einführung-und-übersicht)
2. [Grundlagen und Theorie](#2-grundlagen-und-theorie)
3. [Typenübersicht](#3-typenübersicht)
4. [Produktlinien](#4-produktlinien)
5. [Montage und Installation](#5-montage-und-installation)
6. [Anlagen-spezifische Zuordnung](#6-anlagen-spezifische-zuordnung)
7. [Fehlerbild-Atlas](#7-fehlerbild-atlas)
8. [Troubleshooting-Entscheidungsbaum](#8-troubleshooting-entscheidungsbaum)
9. [FAQ — Häufige Fragen](#9-faq--häufige-fragen)
10. [Glossar](#10-glossar)
11. [Schnell-Referenz](#11-schnell-referenz)
12. [ANHANG A — Fallstudien](#anhang-a--fallstudien)
13. [ANHANG B — AYDI-Integration (Pydantic-Modelle)](#anhang-b--aydi-integration-pydantic-modelle)
14. [ANHANG C — Normen und Standards](#anhang-c--normen-und-standards)
15. [ANHANG D — Lasttabellen](#anhang-d--lasttabellen)
16. [ANHANG E — Confidence-Mapping](#anhang-e--confidence-mapping)
17. [ANHANG F — Wartungsintervalle](#anhang-f--wartungsintervalle)
18. [ANHANG G — Kostenvergleich](#anhang-g--kostenvergleich)
19. [ANHANG H — Montage-Checklisten](#anhang-h--montage-checklisten)
20. [ANHANG I — Bruchlast-Referenz](#anhang-i--bruchlast-referenz)
21. [ANHANG J — Zusätzliche Fallstudien](#anhang-j--zusätzliche-fallstudien)
22. [ANHANG K — Hersteller-Teilenummern-Index](#anhang-k--hersteller-teilenummern-index)
23. [ANHANG L — Visuelle Inspektion Referenzkarten](#anhang-l--visuelle-inspektion-referenzkarten)
24. [ANHANG M — Saisonale Wartung Hochlast-Blöcke](#anhang-m--saisonale-wartung-hochlast-bloecke)
25. [ANHANG N — Retrofit-Szenarien](#anhang-n--retrofit-szenarien)
26. [ANHANG O — Prüfprotokolle und Dokumentation](#anhang-o--pruefprotokolle-und-dokumentation)
27. [ANHANG P — Berechnungsbeispiele](#anhang-p--berechnungsbeispiele)
28. [ANHANG Q — Materialzertifikate und Anforderungen](#anhang-q--materialzertifikate-und-anforderungen)
29. [ANHANG R — Weiterführende Ressourcen](#anhang-r--weiterfuehrende-ressourcen)

---

## 1. Einführung und Übersicht

### 1.1 Definition und Abgrenzung

Hochlast-Blöcke (High-Load Blocks) sind Umlenkrollen, die für Anwendungen mit besonders hohen statischen und dynamischen Lasten konzipiert sind. Im Gegensatz zu Standard-Blöcken für Fallen und Schoten müssen Hochlast-Blöcke Betriebslasten von typischerweise 2.000 bis 25.000 kg (SWL — Safe Working Load) standhalten. Sie kommen überall dort zum Einsatz, wo die Kräfte im Rigg ihre höchsten Werte erreichen.

**Typische Hochlast-Anwendungen:**

| Anwendung | Typische Betriebslast | Bootsklasse |
|-----------|----------------------|-------------|
| Großschot-System (Mainsheet) | 800–5.000 kg | 8–20m |
| Baumniederholer (Vang/Kicker) | 600–4.000 kg | 8–20m |
| Backstag-Trimmer | 1.500–8.000 kg | 10–25m |
| Running Backstays | 2.000–10.000 kg | 12–25m |
| Rollreff-Leinen | 500–3.000 kg | 10–18m |
| Genuaschot-Umlenk (Turning Block) | 800–4.000 kg | 10–20m |
| Spinnaker-Systeme | 1.000–6.000 kg | 10–25m |
| Mastfuß-Umlenkung | 1.500–8.000 kg | 12–25m |

### 1.2 Warum Hochlast-Blöcke eine eigene Kategorie erfordern

Die Unterscheidung zwischen Standard-Blöcken und Hochlast-Blöcken ist keine bloße Marketingkategorisierung. Es bestehen fundamentale Unterschiede:

1. **Materialanforderungen**: Hochlast-Blöcke verwenden hochfeste Aluminium-Legierungen (7075-T6), geschmiedeten Edelstahl (17-4 PH), Titan (Grade 5) oder CFK-Verbundwerkstoffe. Standard-Blöcke kommen oft mit Glasfaser-Verbund oder 6061-T6 Aluminium aus.

2. **Lagerung**: Hochlast-Blöcke erfordern Nadellager, Torlon-Buchsen oder spezielle UHMWPE-Lagerschalen, die unter extremen Flächenpressungen funktionieren. Einfache Gleitlager versagen unter diesen Lasten.

3. **Befestigung**: Die Montage erfordert durchgehende Bolzenverbindungen mit Verstärkungsplatten (Backing Plates), Kernverstärkung im Sandwich-Laminat und definierte Drehmomente. Schraubbefestigungen sind bei Hochlast-Anwendungen grundsätzlich unzureichend.

4. **Prüfanforderungen**: Jeder Hochlast-Block muss mit seiner Bruchlast (Breaking Load) und Arbeitslast (SWL/WLL) gekennzeichnet sein. Prüfnormen verlangen definierte Sicherheitsfaktoren.

5. **Versagensmodi**: Ein versagender Hochlast-Block setzt enorme kinetische Energie frei. Splitter, Seilbruch und Rückschlag können schwere Verletzungen oder Todesfälle verursachen. Die Konsequenzen eines Versagens sind ungleich schwerwiegender als bei einem defekten Fallen-Block.

### 1.3 Historische Entwicklung

Die Entwicklung von Hochlast-Blöcken im Yachtbau lässt sich in drei Phasen unterteilen:

**Phase 1 (bis 1980):** Edelstahl- und Bronze-Blöcke mit Messingbuchsen. Schwer, robust, wartungsintensiv. Typische Bruchlasten 3.000–8.000 kg. Montage über massive Augplatten und Schäkel.

**Phase 2 (1980–2005):** Einführung von Aluminium-Gehäusen mit Kunststoff-Rollen (zunächst Delrin/Acetal, später Torlon). Harken revolutionierte den Markt mit der Einführung von Kugellager-Blöcken. Gewichtsreduktion um 40–60%. Bruchlasten bis 15.000 kg.

**Phase 3 (2005–heute):** Carbon-Verbundwerkstoffe, Titan-Beschläge, keramische Lager. Extreme Gewichtsoptimierung für Racing. Digitale Lastüberwachung (Load Cells). Bruchlasten bis 30.000+ kg bei minimalem Gewicht. Modulare Systeme mit austauschbaren Rollen und Lagern.

### 1.4 Scope dieser Wissensdatei

Diese Datei behandelt ausschließlich Blöcke und Umlenksysteme für Hochlast-Anwendungen. Standard-Blöcke für Fallen und leichte Schoten werden in 10.01 (Grundlagen) und 10.02/10.03 (Hersteller-spezifisch) behandelt. Die Abgrenzung erfolgt bei einer SWL von ca. 1.500 kg — darüber gilt als Hochlast.

**Nicht behandelt werden:**
- Winch-Systeme (→ separate Wissensdatei)
- Hydraulische Zylinder für Backstag/Vang (→ Hydraulik-Wissensdatei)
- Stehende Rigg-Beschläge wie Wanten-Terminals (→ Rigg-Wissensdatei)
- Klüsenplatten und Anker-Beschläge (→ Deck-Hardware)

---

## 2. Grundlagen und Theorie

### 2.1 Lastberechnung — Grundprinzipien

Die korrekte Dimensionierung von Hochlast-Blöcken erfordert das Verständnis mehrerer Lasttypen und ihrer Zusammenwirkung.

#### 2.1.1 Statische Grundlast

Die statische Last an einem Block ergibt sich aus der Schot-/Seilspannung und dem Umlenkwinkel:

```
Block-Last = 2 × Seil-Spannung × sin(Umlenkwinkel / 2)

Beispiele:
- 180° Umlenkung: Block-Last = 2 × Seil-Spannung × sin(90°) = 2 × Seil-Spannung
- 90° Umlenkung:  Block-Last = 2 × Seil-Spannung × sin(45°) = 1,414 × Seil-Spannung
- 60° Umlenkung:  Block-Last = 2 × Seil-Spannung × sin(30°) = 1,0 × Seil-Spannung
- 30° Umlenkung:  Block-Last = 2 × Seil-Spannung × sin(15°) = 0,518 × Seil-Spannung
```

**Kritischer Hinweis:** Bei 180°-Umlenkung (Turning Block) verdoppelt sich die Seilspannung am Befestigungspunkt. Dies wird häufig unterschätzt und ist eine der häufigsten Ursachen für Beschlagversagen.

#### 2.1.2 Dynamische Lastfaktoren

Statische Berechnungen genügen im Yachtbau nicht. Folgende dynamische Faktoren müssen berücksichtigt werden:

| Lastfall | Faktor | Beschreibung |
|----------|--------|-------------|
| Normaler Betrieb | 1,0 | Gleichmäßiges Dichtholen |
| Böenlast | 1,5–2,0 | Plötzliche Windzunahme |
| Schock-Last (Halse) | 2,0–3,0 | Plötzliches Auftreffen des Großbaums |
| Klemm-Schock | 3,0–5,0 | Seil klemmt und wird ruckartig frei |
| Broaching/Kontrollverlust | 2,5–4,0 | Unkontrollierte Kursänderung unter Segeldruck |
| Spinnaker-Stunde (Bear-Away) | 2,0–3,5 | Spinnaker füllt sich schlagartig |
| Rollreff unter Last | 1,5–2,5 | Reffsystem unter Segeldruck |
| Ankerwinsch-Rücklauf | 2,0–3,0 | Kettenstopper/Umlenkblock bei Wellengang |

#### 2.1.3 Schock-Lasten im Detail

Schock-Lasten (Shock Loads) sind die kritischste Lastform im Rigg. Sie treten auf, wenn:

1. **Seil-Rutschen:** Ein geklemmt geglaubtes Seil rutscht durch und wird abrupt gestoppt.
2. **Halsen-Schlag:** Der Großbaum schlägt bei einer unvorbereiteten Halse von einer Seite zur anderen.
3. **Backwind:** Ein Segel füllt sich mit Wind von der falschen Seite.
4. **Welleneinwirkung:** Eine brechende Welle trifft das Segel oder den Baum.
5. **Material-Versagen stromaufwärts:** Ein Schäkel oder Seil-Terminal versagt, und die gespeicherte Energie wird schlagartig auf den nächsten Beschlag übertragen.

**Berechnung der Schock-Last:**

```
F_schock = F_statisch × k_dynamisch × k_sicherheit

wobei:
  k_dynamisch = 2,0–5,0 (abhängig von Anwendung)
  k_sicherheit = gemäß Sicherheitsfaktor-Tabelle
```

#### 2.1.4 Ermüdungslast-Zyklen (Fatigue Loading)

Hochlast-Blöcke unterliegen nicht nur Einzellasten, sondern zyklischen Belastungen über ihre Lebensdauer:

| Anwendung | Zyklen/Stunde | Stunden/Saison | Zyklen/Saison | Zyklen/10 Jahre |
|-----------|--------------|----------------|---------------|----------------|
| Großschot (Fahrtensegler) | 5–15 | 200 | 1.000–3.000 | 10.000–30.000 |
| Großschot (Regatta) | 30–120 | 150 | 4.500–18.000 | 45.000–180.000 |
| Baumniederholer | 2–8 | 200 | 400–1.600 | 4.000–16.000 |
| Backstag-Trimmer | 10–40 | 150 | 1.500–6.000 | 15.000–60.000 |
| Running Backstay | 5–20 | 150 | 750–3.000 | 7.500–30.000 |
| Genuaschot-Umlenkung | 3–10 | 200 | 600–2.000 | 6.000–20.000 |

**Ermüdungsfestigkeit:**
- Aluminium 7075-T6: Kein echtes Dauerfestigkeitsniveau. Versagt nach ausreichend Zyklen bei jeder Spannungsamplitude.
- Edelstahl 17-4 PH: Dauerfestigkeit bei ca. 40% der Zugfestigkeit (10⁷ Zyklen).
- Titan Grade 5: Dauerfestigkeit bei ca. 50% der Zugfestigkeit.
- CFK: Hervorragende Ermüdungsfestigkeit, aber empfindlich gegenüber Schlag und UV.

### 2.2 Sicherheitsfaktoren

#### 2.2.1 Standardanforderungen

| Anwendung | Sicherheitsfaktor (SF) | Begründung |
|-----------|----------------------|------------|
| Laufendes Gut allgemein | 3:1 (Bruch:Betrieb) | ISO 8328, Industriestandard |
| Personensicherheit (MOB, Trapez) | 5:1 | Lebensrettende Funktion |
| Stehende Rigg-Anbindung | 4:1 | Rigg-Totalverlust bei Versagen |
| Hebevorrichtungen | 5:1 | EN 13157, Arbeitssicherheit |
| Regatta (Einhand/Kurzstrecke) | 2,5:1 | Reduziert bei kontrollierten Bedingungen |
| Offshore-Regatta (Langstrecke) | 3,5:1 | Erhöhter SF wegen fehlender Reparaturmöglichkeit |
| Superyacht (MCA/LY3) | 5:1 | Regulatorische Anforderung |
| Charter-Yacht | 4:1 | Erhöhte Beanspruchung, unbekannte Besatzung |

> ⚠️ **ZU PRÜFEN (Audit):** Das Normzitat "ISO 8328" (Zeile "Laufendes Gut allgemein 3:1") ist fehlerhaft. ISO 8328 ist eine zurückgezogene Kunststoff-Norm ("Plastics — Amorphous thermoplastic moulding materials — Determination of maximum reversion", ISO 8328:1989), kein Block-/Deck-Hardware-Standard (web-verifiziert: iso.org, GlobalSpec). Der Sicherheitsfaktor 3:1 ist ein etablierter Branchen-Faustwert; eine zweifelsfrei korrekte ISO-Norm für Block-Sicherheitsfaktoren ist nicht belegbar. Das Zitat "EN 13157" (Hebevorrichtungen 5:1) ist dagegen korrekt (Cranes — Safety — Hand powered lifting equipment; erfasst ausdrücklich Umlenkrollen/Blöcke).

#### 2.2.2 Berechnung der erforderlichen Bruchlast

```
Erforderliche Bruchlast = Betriebslast × Dynamikfaktor × Sicherheitsfaktor

Beispiel: Großschot-Turning-Block, 12m Segelboot
  Betriebslast Großschot: 800 kg
  Umlenkwinkel: 180° → Block-Last = 2 × 800 = 1.600 kg
  Dynamikfaktor (Böe): 2,0
  Sicherheitsfaktor: 3:1
  
  Erforderliche Bruchlast = 1.600 × 2,0 × 3,0 = 9.600 kg
  → Block mit mindestens 10.000 kg Bruchlast erforderlich
```

#### 2.2.3 Degradationsfaktoren über die Lebensdauer

Die nominale Bruchlast eines neuen Blocks muss mit Degradationsfaktoren reduziert werden:

| Degradationsursache | Faktor nach 5 Jahren | Faktor nach 10 Jahren |
|--------------------|---------------------|----------------------|
| UV-Exposition (Kunststoff-Rollen) | 0,90 | 0,75 |
| Korrosion (Edelstahl, Salzwasser) | 0,95 | 0,85 |
| Korrosion (Aluminium, anodisiert) | 0,92 | 0,80 |
| Lagerverschleiß | 0,95 | 0,85 |
| Achsverschleiß | 0,90 | 0,75 |
| Ermüdung (Regatta-Nutzung) | 0,85 | 0,65 |
| Ermüdung (Fahrten-Nutzung) | 0,95 | 0,85 |

**Gesamt-Degradation** (worst case, Regatta, 10 Jahre): 0,75 × 0,85 × 0,80 × 0,85 × 0,75 × 0,65 × 0,85 ≈ **0,18**
→ Ein Hochlast-Block unter extremen Bedingungen kann nach 10 Jahren nur noch 18% seiner ursprünglichen Bruchlast aufweisen.

**Empfehlung:** Hochlast-Blöcke in kritischen Anwendungen nach 8–10 Jahren Regatta-Nutzung oder 12–15 Jahren Fahrten-Nutzung ersetzen, unabhängig vom sichtbaren Zustand.

### 2.3 Wirkungsgrad und Reibung

#### 2.3.1 Wirkungsgrad verschiedener Lagertypen

| Lagertyp | Wirkungsgrad (η) | Typische Anwendung |
|----------|-----------------|-------------------|
| Kugellager (Edelstahl) | 95–98% | Standard-Hochlast |
| Nadellager | 96–99% | Premium-Hochlast |
| Torlon-Buchse | 88–93% | Hochlast bei begrenztem Platz |
| UHMWPE-Buchse | 85–92% | Budget-Hochlast |
| Delrin/Acetal-Buchse | 80–88% | Nicht für Hochlast empfohlen |
| Keramik-Kugellager | 97–99% | Racing, Superyacht |

#### 2.3.2 Flaschenzug-Effizienz

Bei Mehrfach-Übersetzung (Talje) akkumuliert der Reibungsverlust:

```
Gesamt-Effizienz = η^n

wobei n = Anzahl der Umlenkungen

Beispiel: 6:1 Großschot-Talje mit Kugellager-Blöcken (η = 0,97):
  Effizienz = 0,97^6 = 0,83 (83%)
  → Von 6:1 theoretischem Vorteil bleiben effektiv 6 × 0,83 = 4,98:1

Beispiel: 6:1 Großschot-Talje mit Torlon-Buchsen (η = 0,90):
  Effizienz = 0,90^6 = 0,53 (53%)
  → Effektiver Vorteil nur 6 × 0,53 = 3,18:1
```

**Konsequenz:** Bei Hochlast-Taljensystemen mit vielen Umlenkungen ist die Lagerqualität entscheidend. Minderwertige Lager fressen den mechanischen Vorteil auf.

#### 2.3.3 Rollenrille und Seildurchmesser

Die Rollenrille (Sheave Groove) muss zum Seildurchmesser passen:

```
Optimaler Rillendurchmesser = Seildurchmesser × 1,05 bis 1,15

Zu eng: Seil wird gequetscht, Mantelschaden, erhöhte Reibung
Zu weit: Seil legt sich schief, einseitiger Lagerverschleiß
Zu klein (Rollendurchmesser): Seil wird übermäßig gebogen → Seil-Ermüdung
```

**Mindest-Rollendurchmesser für Hochlast-Anwendungen:**

| Seiltyp | Min. Rollen-∅ / Seil-∅ | Empfohlen |
|---------|------------------------|-----------|
| 3-litzig gedreht | 8:1 | 10:1 |
| Doppelgeflecht (Polyester) | 6:1 | 8:1 |
| Dyneema/Spectra-Kern | 5:1 | 7:1 |
| PBO-Kern | 8:1 | 10:1 |
| Aramid/Kevlar-Kern | 8:1 | 10:1 |
| Draht-Seil (1×19) | 20:1 | 25:1 |

### 2.4 Lastverteilung bei Mehrfach-Blöcken

#### 2.4.1 Doppel- und Dreifach-Blöcke

Bei Mehrfach-Blöcken (Double/Triple Blocks) verteilt sich die Last nicht gleichmäßig auf alle Rollen:

```
Doppelblock in 4:1 Talje:
  Rolle 1 (Einlauf): 100% der Seil-Spannung
  Rolle 2 (Auslauf): 100% × η = 97% (bei Kugellager)
  Gesamtlast auf Block: ~200% der Seil-Spannung (bei 180° Umlenkung)
  Achslast: 200% × sin(90°) ≈ 200% (da Seile parallel)

Dreifachblock in 6:1 Talje:
  Rolle 1: 100%
  Rolle 2: 97%
  Rolle 3: 94%
  Gesamtlast auf Block: ~291% der Seil-Spannung
```

#### 2.4.2 Deck-Organizer Lastverteilung

Bei Deck-Organizern mit 3–6 Rollen nebeneinander ist die Lastsituation anders, da jede Rolle ein eigenes Seil führt:

```
Worst Case: Alle Rollen gleichzeitig unter Last
  Gesamt-Last = Summe aller Einzellasten
  
Typischer Fall: 2–3 von 6 Rollen gleichzeitig unter Last
  Design-Last = Max-Einzellast × Rollenanzahl × 0,6 (Gleichzeitigkeitsfaktor)
```

### 2.5 Thermische Effekte

Bei extremer Beanspruchung (Regatta, schwere See) können Hochlast-Blöcke signifikante Wärmeentwicklung zeigen:

| Reibungsleistung | Kunststoff-Rolle | Alu-Rolle | Symptom |
|------------------|-----------------|-----------|---------|
| < 50 W | Kein Problem | Kein Problem | — |
| 50–200 W | Erweichung möglich | Kein Problem | Rollen quietschen |
| 200–500 W | Verformung/Versagen | Heiß, Lager leiden | Seil schmilzt lokal |
| > 500 W | Sofortiges Versagen | Lagerschaden | Rauchentwicklung |

**Formel:**

```
P_reib = F_seil × v_seil × (1 - η)

Beispiel: F = 3000 kg = 29.430 N, v = 0,5 m/s, η = 0,95
  P = 29.430 × 0,5 × 0,05 = 736 W → Kritisch!
```

**Konsequenz:** Bei Hochlast-Anwendungen mit hohen Seilgeschwindigkeiten (Großschot bei Regatta-Halsen, Spinnaker-Trimm) sind Metallrollen oder hochtemperaturfeste Kunststoffe (Torlon: bis 260°C) erforderlich.

---

## 3. Typenübersicht

### 3.1 Hochlast-Einzelblöcke (Single High-Load Blocks)

#### 3.1.1 Charakteristik

Einzelblöcke für Hochlast-Anwendungen sind die Basiskomponente für einfache Umlenkungen. Sie werden eingesetzt, wenn nur eine Seilführung am jeweiligen Punkt erforderlich ist.

**Bauformen:**

- **Bügel-Block (Becket Block):** Mit integriertem Befestigungsauge unten für Taljen-Anwendungen. Das stehende Part wird am Becket befestigt.
- **Schäkel-Block (Shackle Block):** Standard-Aufhängung über Schäkel am Augbolzen.
- **Gabel-Block (Fork Block/Clevis Block):** Breite Gabel-Aufhängung für seitliche Belastungen.
- **Stand-Up Block:** Aufrechte Montage direkt auf dem Deck. Kein Schäkel erforderlich.
- **Fiddle Block:** Zwei übereinander angeordnete Rollen in einem Gehäuse für kompakte Taljen.

#### 3.1.2 Typische Spezifikationen

| Parameter | 40mm Klasse | 57mm Klasse | 75mm Klasse | 100mm Klasse |
|-----------|------------|------------|------------|-------------|
| Rollendurchmesser | 40 mm | 57 mm | 75 mm | 100 mm |
| Max. Seildurchmesser | 10 mm | 14 mm | 18 mm | 22 mm |
| SWL (Arbeitslast) | 800 kg | 1.800 kg | 3.500 kg | 6.000 kg |
| Bruchlast | 2.400 kg | 5.400 kg | 10.500 kg | 18.000 kg |
| Gewicht (Alu/Kugellager) | 120 g | 280 g | 550 g | 1.100 g |
| Gewicht (Edelstahl) | 200 g | 450 g | 900 g | 1.800 g |

### 3.2 Hochlast-Doppelblöcke (Double High-Load Blocks)

#### 3.2.1 Charakteristik

Doppelblöcke enthalten zwei Rollen auf einer gemeinsamen Achse oder auf gestaffelten Achsen. Sie bilden das Herzstück von 4:1 Taljensystemen und werden vor allem im Großschot-System eingesetzt.

**Varianten:**
- **Parallele Doppelblöcke:** Beide Rollen nebeneinander auf einer Achse. Kompakt, aber breiterer Einbau.
- **Fiddle-Doppelblöcke:** Rollen übereinander angeordnet (obere Rolle größer). Schmalerer Einbau, bessere Seilführung.
- **Doppelblöcke mit Klemme:** Integrierte Fallklemme (Cam Cleat) für Großschot oder Vang.
- **Doppelblöcke mit Becket:** Befestigungspunkt für stehendes Part integriert.

#### 3.2.2 Typische Spezifikationen

| Parameter | 57mm Klasse | 75mm Klasse | 100mm Klasse |
|-----------|------------|------------|-------------|
| Rollendurchmesser | 57 mm | 75 mm | 100 mm |
| Max. Seildurchmesser | 14 mm | 18 mm | 22 mm |
| SWL (Arbeitslast) | 2.500 kg | 5.000 kg | 8.000 kg |
| Bruchlast | 7.500 kg | 15.000 kg | 24.000 kg |
| Gewicht (Alu/Kugellager) | 480 g | 950 g | 1.900 g |
| Bootsklasse | 8–12m | 10–18m | 16–25m |

### 3.3 Hochlast-Dreifachblöcke (Triple High-Load Blocks)

#### 3.3.1 Charakteristik

Dreifachblöcke kommen bei 6:1 Taljensystemen zum Einsatz. Sie sind in der Regel Fiddle-Anordnung (drei Rollen übereinander, abnehmende Größe von oben nach unten).

**Anwendungen:**
- Großschot-System 6:1 auf Yachten 12–18m
- Baumniederholer-System auf größeren Yachten
- Backstag-Talje auf Racing-Yachten
- Spinnaker-Barber-Hauler-Systeme

| Parameter | 57mm Klasse | 75mm Klasse |
|-----------|------------|------------|
| SWL (Arbeitslast) | 3.200 kg | 6.500 kg |
| Bruchlast | 9.600 kg | 19.500 kg |
| Gewicht | 680 g | 1.400 g |
| Höhe gesamt | 280 mm | 380 mm |

### 3.4 Deck-Organizer (Umlenkplatten)

#### 3.4.1 Charakteristik

Deck-Organizer sind Mehrfach-Umlenkrollen, die am Cockpit-Eingang oder am Mastfuß montiert werden. Sie bündeln mehrere Leinen (Fallen, Strecker, Reff-Leinen) und führen sie geordnet zur Winch oder zum Klemmenfeld.

**Bauformen:**
- **Mastfuß-Organizer (3–6 Rollen):** Montage direkt am Mastfuß oder auf dem Kajütdach. Leiten Fallen und Strecker vom Mast zum Cockpit.
- **Cockpit-Organizer (4–8 Rollen):** Montage am Cockpit-Eingang. Leiten alle Leinen geordnet zu den Winschen.
- **Traveller-Organizer:** Spezielle Anordnung für Großschot-Traveller mit integrierter Umlenkung.
- **Flush-Mount-Organizer:** Bündig in das Deck eingelassen. Saubere Optik, aber aufwendigere Installation.

#### 3.4.2 Anforderungen an Hochlast-Organizer

- Jede Rolle muss individuell belastbar sein (nicht alle über eine gemeinsame Achse).
- Seitliche Belastung muss aufgenommen werden (Leinen kommen in unterschiedlichen Winkeln).
- Anti-Chafe-Leisten zwischen den Rollen verhindern Seil-zu-Seil-Reibung.
- Selbstreinigende Rollen (Open-Cage) verhindern Versalzung.
- Schnelle Identifizierung der Leinen durch Farbcodierung oder Nummerierung.

#### 3.4.3 Typische Spezifikationen

| Parameter | Leichte Klasse | Mittlere Klasse | Schwere Klasse |
|-----------|---------------|-----------------|----------------|
| Rollenanzahl | 3–4 | 4–6 | 5–8 |
| Rollendurchmesser | 40 mm | 50 mm | 60–75 mm |
| Max. Seildurchmesser | 10 mm | 12 mm | 14–16 mm |
| SWL pro Rolle | 500 kg | 1.200 kg | 2.500 kg |
| SWL gesamt (Gleichzeitigkeit) | 1.200 kg | 3.500 kg | 8.000 kg |
| Bootsklasse | 8–10m | 10–14m | 14–20m |
| Gewicht | 350–600 g | 600–1.200 g | 1.200–2.500 g |

### 3.5 Turning Blocks (Umlenkblöcke)

#### 3.5.1 Charakteristik

Turning Blocks sind flach bauende Umlenkblöcke, die direkt auf dem Deck montiert werden. Sie leiten Seile um 90° bis 180° um, typischerweise von horizontal nach horizontal oder von vertikal (vom Mast kommend) nach horizontal.

**Bauformen:**
- **Pad-Eye-Montage:** Block wird über einen Augenbolzen (Pad Eye) befestigt. Erlaubt Schwenken in der horizontalen Ebene.
- **Through-Bolt-Montage:** Bolzen geht durch das Deck hindurch mit Backing Plate. Höchste Festigkeit.
- **U-Bracket-Montage:** U-förmiger Bügel, durch den Deck gebolt. Erlaubt mehr Rollenfreigang.
- **Slide-Montage (Schiene):** Block auf einer T-Schiene verschiebbar. Für variable Genuaschot-Positionen.

#### 3.5.2 Kritischer Hinweis: Lastvektor bei Turning Blocks

Bei Turning Blocks liegt die Hauptlast senkrecht zum Deck (Ausziehkraft). Dies stellt extreme Anforderungen an die Decksbefestigung:

```
Ausziehkraft bei 180° Umlenkung:
  F_auszug = 2 × F_seil (senkrecht zum Deck)
  
Ausziehkraft bei 90° Umlenkung:
  F_auszug = F_seil × √2 ≈ 1,414 × F_seil (45° zum Deck)

Beispiel: Genuaschot 2.000 kg, 180° Turning Block:
  F_auszug = 2 × 2.000 = 4.000 kg senkrecht zum Deck
  → Mindestens M10 Durchgangsbolzen mit 120×120×6mm Backing Plate
```

#### 3.5.3 Typische Spezifikationen

| Parameter | Leicht | Mittel | Schwer | Extrem |
|-----------|--------|--------|--------|--------|
| Rollendurchmesser | 40 mm | 57 mm | 75 mm | 100 mm |
| Max. Seildurchmesser | 12 mm | 16 mm | 20 mm | 24 mm |
| SWL | 1.000 kg | 2.500 kg | 5.000 kg | 8.000 kg |
| Bruchlast | 3.000 kg | 7.500 kg | 15.000 kg | 24.000 kg |
| Bauhöhe über Deck | 35 mm | 50 mm | 65 mm | 85 mm |
| Gewicht | 150 g | 350 g | 700 g | 1.400 g |

### 3.6 Cheek Blocks (Wangenblöcke)

#### 3.6.1 Charakteristik

Cheek Blocks werden seitlich am Mast, am Baum oder am Rumpf montiert. Die Befestigung erfolgt über die Seitenwange (Cheek) — daher der Name. Sie bieten eine platzsparende Umlenkung bei moderaten bis hohen Lasten.

**Typische Positionen:**
- Mastfuß: Umlenkung der Fallen aus dem Mast-Inneren
- Baum: Umlenkung des Großschot-Achterliektrimms
- Saling: Umlenkung von Spinnaker-Bären
- Rumpf (innen): Umlenkung von Backstag-Leinen

**Vorteile gegenüber Standard-Blöcken:**
- Flache Bauweise, kein Schäkel nötig
- Geringere Biegemomente auf die Befestigung
- Saubere Optik, weniger Haken-Risiko

#### 3.6.2 Typische Spezifikationen

| Parameter | 40mm | 57mm | 75mm |
|-----------|------|------|------|
| Rollendurchmesser | 40 mm | 57 mm | 75 mm |
| Max. Seildurchmesser | 12 mm | 16 mm | 20 mm |
| SWL | 600 kg | 1.500 kg | 3.000 kg |
| Bruchlast | 1.800 kg | 4.500 kg | 9.000 kg |
| Gewicht | 80 g | 180 g | 380 g |
| Befestigung | 4× M6 | 4× M8 | 4× M10 |

### 3.7 Mastfuß-Blöcke

#### 3.7.1 Charakteristik

Mastfuß-Blöcke sind speziell für die Umlenkung von Fallen und Streckern am Mastfuß konzipiert. Sie müssen:

- Viele Leinen (4–10) auf engem Raum umlenken
- Verschiedene Seil-Winkel aufnehmen
- Schnelle Identifizierung der Leinen ermöglichen
- Robuster Korrosionsschutz (ständig im Spritzwasser)

**Systeme:**
- Einzelblock-Array: Mehrere Einzelblöcke auf einer gemeinsamen Montageplatte
- Integrierter Mastfuß-Organizer: Alle Umlenkungen in einem Gehäuse
- Mastinterne Umlenkung: Blöcke im Mastprofil verbaut (bei modernen Masten)

### 3.8 Großschot-Systeme (Mainsheet Systems)

#### 3.8.1 Übersetzungsverhältnisse und Komponenten

| Übersetzung | Blöcke benötigt | Typische Bootsgröße | Großschot-Last (Endtakel) |
|-------------|----------------|--------------------|-----------------------------|
| 4:1 | 1× Doppel + 1× Einzel (Becket) | 7–10m | 250–600 kg |
| 6:1 | 1× Dreifach + 1× Doppel (Becket) | 10–13m | 400–900 kg |
| 8:1 | 2× Vierfach oder Fiddle-Systeme | 13–16m | 600–1.200 kg |
| 10:1 | Komplexe Kaskade | 16–20m | 800–1.500 kg |
| 12:1 | Doppel-Kaskade mit Winch | 20m+ | 1.000–2.000 kg |

#### 3.8.2 Großschot-Konfigurationen

**Mittschiffs-Traveller (Mid-Boom):**
- Traveller-Wagen auf Schiene, Talje zwischen Wagen und Baum-Mitte
- Vorteile: Kurzer Schotweg, direkte Kraftübertragung
- Nachteile: Traveller-Schiene im Cockpit, eingeschränkter Cockpit-Raum

**Achterliek-Großschot (End-Boom):**
- Talje am Baum-Ende, Schot führt zum Heck oder zum Cockpitboden
- Vorteile: Cockpit frei, guter Achterliek-Trimm
- Nachteile: Längerer Schotweg, höhere Lasten am Baumende

**Kaskaden-System:**
- Erste Stufe: 2:1 oder 4:1 am Baumende
- Zweite Stufe: 2:1 oder 4:1 am Cockpitboden
- Gesamt-Übersetzung: 4:1 bis 16:1
- Vorteile: Hohe Übersetzung bei moderatem Platzbedarf
- Nachteile: Viele Blöcke, mehr Reibungsverlust, komplexe Seilführung

#### 3.8.3 Lastberechnung Großschot-System

```
Großsegel-Kraft (vereinfacht):
  F_segel = 0,5 × ρ_luft × V² × A_segel × C_l
  
  ρ_luft = 1,225 kg/m³
  V = Windgeschwindigkeit (m/s)
  A_segel = Segelfläche (m²)
  C_l = Auftriebsbeiwert (0,8–1,5)

Beispiel: 12m Segelyacht, Großsegel 35m², 25 kt Wind (12,9 m/s):
  F_segel = 0,5 × 1,225 × 12,9² × 35 × 1,2 = 4.275 kg
  
  Großschot-Last am Schothorn:
  F_schot = F_segel × L_segel / L_baum ≈ F_segel × 0,7 = 2.993 kg
  
  Bei 6:1 Talje: Handkraft = 2.993 / (6 × η) = 2.993 / (6 × 0,83) = 601 kg
  → Noch zu viel für Handkraft, Winch erforderlich
  
  Block-Lasten im System:
  - Baumblock (Dreifach): 3 × 2.993 / 6 × (1 + η + η²) = ~2.900 kg
  - Traveller-Block (Doppel + Becket): ~2.993 kg
  - Einzelblock am Becket: 2.993 / 6 = ~500 kg
```

### 3.9 Baumniederholer-Systeme (Vang/Kicker Systems)

#### 3.9.1 Grundprinzip

Der Baumniederholer (Vang oder Kicker) hält den Großbaum unten und kontrolliert damit den Achterliek-Trimm des Großsegels. Im Hochlast-Bereich gibt es zwei Grundsysteme:

**Mechanischer Vang (Talje):**
- 4:1 bis 16:1 Übersetzung
- Typisch: Gasdruckfeder + Talje (Rigid Vang) oder reine Talje
- Blöcke: Doppel- und Dreifachblöcke in der 40–75mm Klasse
- Lasten: 500–3.000 kg am Befestigungspunkt

**Hydraulischer Vang:**
- Hydraulikzylinder ersetzt Talje
- Keine Blöcke nötig (nur Umlenk-Blöcke für Steuerleinen bei manuellem Override)
- Lasten: 1.000–8.000 kg

#### 3.9.2 Lastberechnung Vang

```
F_vang = F_segel × L_segel_druck / L_baum × sin(α)

wobei α = Winkel zwischen Vang und Baum (typisch 30–50°)

Bei α = 35°:
  F_vang = 4.275 × 0,4 / sin(35°) = 4.275 × 0,4 / 0,574 = 2.979 kg
```

### 3.10 Backstag-Trimmer und Running Backstays

#### 3.10.1 Backstag-Trimmer

Der Backstag-Trimmer spannt das Achterstag, um den Mastbogen zu kontrollieren und die Vorstag-Spannung indirekt zu beeinflussen.

**Systeme:**
- Talje (4:1 bis 16:1) mit Hochlast-Blöcken
- Hydraulischer Zylinder
- Schneckengetriebe (selten, veraltet)

**Lasten:**
- 8m Jolle: nicht vorhanden
- 10m Fahrtensegler: 1.500–3.000 kg
- 14m Performance Cruiser: 3.000–6.000 kg
- 18m Racer: 5.000–10.000 kg
- 22m Maxi: 8.000–15.000 kg

#### 3.10.2 Running Backstays

Running Backstays (Checkstays, Runners) sind paarweise angeordnete, wechselseitig gesetzte Stagen. Sie erzeugen die höchsten Einzellasten im laufenden Gut.

**Lasten an den Umlenkblöcken:**

| Bootsgröße | Runner-Last | Umlenkwinkel | Block-Last |
|-----------|-------------|-------------|------------|
| 10m | 2.000 kg | 170° | 3.990 kg |
| 12m | 3.500 kg | 170° | 6.983 kg |
| 14m | 5.000 kg | 170° | 9.976 kg |
| 18m | 8.000 kg | 170° | 15.962 kg |
| 22m | 12.000 kg | 170° | 23.943 kg |

**Erforderliche Block-Spezifikationen für Runners:**

| Bootsgröße | Min. SWL Block | Min. Bruchlast | Empfohlene Klasse |
|-----------|---------------|---------------|-------------------|
| 10m | 4.000 kg | 12.000 kg | 75mm Kugellager |
| 12m | 7.000 kg | 21.000 kg | 100mm Kugellager |
| 14m | 10.000 kg | 30.000 kg | 100mm+ Nadellager |
| 18m | 16.000 kg | 48.000 kg | Spezial-Hochlast |
| 22m | 24.000 kg | 72.000 kg | Custom-Schmiedestück |

---

## 4. Produktlinien

### 4.1 Harken

#### 4.1.1 Firmengeschichte und Positionierung

Harken (Pewaukee, Wisconsin, USA, gegr. 1967) ist der weltweit führende Hersteller von Rigg-Beschlägen. Peter Harken revolutionierte die Branche mit der Einführung von Kugellager-Blöcken in den 1970er Jahren. Im Hochlast-Segment ist Harken der Benchmark, an dem sich alle anderen Hersteller messen lassen.

#### 4.1.2 Black Magic 75mm Serie

Die Black Magic 75mm Serie ist Harkens Premium-Linie für Hochlast-Anwendungen auf Yachten von 10–20m.

**Materialien:**
- Gehäuse: Anodisiertes Aluminium 6061-T6 (schwarz)
- Rollen: Glasfaserverstärktes Acetal (Delrin AF)
- Achse: Edelstahl 17-4 PH
- Lager: Nadellager (Torlon-Käfig)
- Schäkel: Edelstahl 316L, geschmiedet

**Produktübersicht:**

| Artikel-Nr. | Typ | SWL (kg) | Bruchlast (kg) | Gewicht (g) | Seil max. (mm) |
|-------------|-----|----------|---------------|-------------|----------------|
| 2645 | Einzelblock | 2.950 | 8.850 | 425 | 18 |
| 2646 | Einzelblock mit Wirbel | 2.950 | 8.850 | 510 | 18 |
| 2648 | Einzelblock, Becket | 2.950 | 8.850 | 465 | 18 |
| 2649 | Einzelblock, Becket + Schäkel | 2.950 | 8.850 | 545 | 18 |
| 2655 | Doppelblock | 3.900 | 11.700 | 770 | 18 |
| 2656 | Doppelblock, Becket | 3.900 | 11.700 | 810 | 18 |
| 2658 | Dreifachblock | 4.800 | 14.400 | 1.100 | 18 |
| 2660 | Dreifachblock, Becket | 4.800 | 14.400 | 1.140 | 18 |
| 2637 | Fiddle Block | 3.500 | 10.500 | 680 | 18 |
| 2638 | Fiddle Block, Becket | 3.500 | 10.500 | 720 | 18 |
| 2643 | Fiddle Block, Cam Cleat | 3.500 | 10.500 | 820 | 18 |

#### 4.1.3 Carbo 75mm Serie

Die Carbo-Serie nutzt kohlefaserverstärktes Nylon für Gehäuse und Seitenplatten. Leichter als Black Magic, aber geringere Bruchlasten.

| Artikel-Nr. | Typ | SWL (kg) | Bruchlast (kg) | Gewicht (g) | Seil max. (mm) |
|-------------|-----|----------|---------------|-------------|----------------|
| 2672 | Einzelblock, Wirbel | 1.500 | 4.500 | 200 | 16 |
| 2673 | Einzelblock, Becket | 1.500 | 4.500 | 185 | 16 |
| 2674 | Doppelblock | 2.000 | 6.000 | 310 | 16 |
| 2675 | Doppelblock, Becket | 2.000 | 6.000 | 330 | 16 |
| 2676 | Dreifachblock | 2.500 | 7.500 | 440 | 16 |
| 2677 | Fiddle Block | 1.800 | 5.400 | 270 | 16 |

#### 4.1.4 Harken Stand-Up Spring Blocks

Stand-Up Spring Blocks stehen aufrecht auf dem Deck und richten sich automatisch aus. Ideal als Turning Blocks.

| Artikel-Nr. | Typ | SWL (kg) | Bruchlast (kg) | Gewicht (g) | Seil max. (mm) |
|-------------|-----|----------|---------------|-------------|----------------|
| 2691 | Stand-Up Spring, 57mm | 1.400 | 4.200 | 190 | 14 |
| 2692 | Stand-Up Spring, 75mm | 2.950 | 8.850 | 350 | 18 |
| 2693 | Stand-Up Spring, 75mm doppelt | 3.900 | 11.700 | 650 | 18 |

#### 4.1.5 Harken Mainsheet Systems

Vormontierte Großschot-Systeme von Harken:

| Artikel-Nr. | System | Übersetzung | Max. Baum-Last (kg) | Bootsklasse |
|-------------|--------|-------------|---------------------|-------------|
| 7404 | Midrange Traveller + Talje | 4:1 | 1.800 | 7–10m |
| 7406 | Midrange Traveller + Talje | 6:1 | 2.800 | 10–12m |
| 7471 | ESP Doppel/Einzel | 4:1 | 2.200 | 8–11m |
| 7472 | ESP Dreifach/Doppel | 6:1 | 3.500 | 11–14m |
| 7476 | Black Magic Dreifach/Doppel | 6:1 | 4.800 | 12–16m |
| 7481 | Black Magic Vierfach/Dreifach | 8:1 | 6.000 | 14–18m |

#### 4.1.6 Harken Deck Organizer

| Artikel-Nr. | Rollen | Rollendurchm. | SWL/Rolle (kg) | Gewicht (g) |
|-------------|--------|--------------|----------------|-------------|
| 3232 | 3 | 40mm | 900 | 350 |
| 3233 | 4 | 40mm | 900 | 450 |
| 3234 | 5 | 40mm | 900 | 550 |
| 3235 | 6 | 40mm | 900 | 650 |
| 3252 | 3 | 57mm | 1.800 | 650 |
| 3253 | 4 | 57mm | 1.800 | 850 |
| 3254 | 5 | 57mm | 1.800 | 1.050 |
| 3255 | 6 | 57mm | 1.800 | 1.250 |
| 3272 | 3 | 75mm | 2.950 | 1.100 |
| 3273 | 4 | 75mm | 2.950 | 1.450 |
| 3274 | 5 | 75mm | 2.950 | 1.800 |

#### 4.1.7 Harken ESP (Element, Structure, Performance) Serie

Die ESP-Serie ist Harkens Mittelklasse für Performance-orientierte Fahrtensegler.

| Artikel-Nr. | Typ | SWL (kg) | Bruchlast (kg) | Gewicht (g) | Seil max. (mm) |
|-------------|-----|----------|---------------|-------------|----------------|
| 1086 | ESP 57mm Einzel, Wirbel | 1.400 | 4.200 | 160 | 14 |
| 1087 | ESP 57mm Einzel, Becket | 1.400 | 4.200 | 155 | 14 |
| 1088 | ESP 57mm Doppel | 1.800 | 5.400 | 260 | 14 |
| 1089 | ESP 57mm Fiddle | 1.600 | 4.800 | 230 | 14 |
| 1091 | ESP 75mm Einzel | 2.200 | 6.600 | 310 | 18 |
| 1092 | ESP 75mm Doppel | 2.800 | 8.400 | 520 | 18 |
| 1093 | ESP 75mm Fiddle | 2.500 | 7.500 | 460 | 18 |

#### 4.1.8 Harken Cheek Blocks (Hochlast)

| Artikel-Nr. | Typ | SWL (kg) | Bruchlast (kg) | Gewicht (g) | Seil max. (mm) |
|-------------|-----|----------|---------------|-------------|----------------|
| 243 | Mastfuß Cheek Block, 57mm | 1.200 | 3.600 | 120 | 14 |
| 244 | Mastfuß Cheek Block, 75mm | 2.200 | 6.600 | 220 | 18 |
| 245 | Exit Block, 57mm | 1.400 | 4.200 | 145 | 14 |
| 246 | Exit Block, 75mm | 2.500 | 7.500 | 250 | 18 |

### 4.2 Lewmar

#### 4.2.1 Firmengeschichte und Positionierung

Lewmar (Havant, Hampshire, UK, gegr. 1946) ist primär für seine Winschen bekannt, bietet aber ein vollständiges Sortiment an Deck-Beschlägen. Im Hochlast-Segment positioniert sich Lewmar mit der Synchro-Serie und der Ocean-Serie im mittleren bis oberen Preisbereich.

#### 4.2.2 Synchro Serie

Die Synchro-Serie nutzt ein patentiertes Gehäusedesign mit selbstausrichtenden Rollen.

**Synchro 60mm:**

| Artikel-Nr. | Typ | SWL (kg) | Bruchlast (kg) | Gewicht (g) | Seil max. (mm) |
|-------------|-----|----------|---------------|-------------|----------------|
| 29925035 | Einzel, Schäkel | 2.000 | 6.000 | 310 | 16 |
| 29925036 | Einzel, Becket | 2.000 | 6.000 | 330 | 16 |
| 29925037 | Doppel | 2.800 | 8.400 | 540 | 16 |
| 29925038 | Doppel, Becket | 2.800 | 8.400 | 570 | 16 |
| 29925039 | Dreifach | 3.500 | 10.500 | 780 | 16 |
| 29925040 | Fiddle | 2.500 | 7.500 | 470 | 16 |
| 29925041 | Fiddle, Becket | 2.500 | 7.500 | 500 | 16 |
| 29925042 | Stand-Up Spring | 2.000 | 6.000 | 280 | 16 |

**Synchro 80mm:**

| Artikel-Nr. | Typ | SWL (kg) | Bruchlast (kg) | Gewicht (g) | Seil max. (mm) |
|-------------|-----|----------|---------------|-------------|----------------|
| 29925055 | Einzel, Schäkel | 3.500 | 10.500 | 580 | 20 |
| 29925056 | Einzel, Becket | 3.500 | 10.500 | 610 | 20 |
| 29925057 | Doppel | 4.800 | 14.400 | 1.020 | 20 |
| 29925058 | Doppel, Becket | 4.800 | 14.400 | 1.060 | 20 |
| 29925059 | Dreifach | 6.000 | 18.000 | 1.480 | 20 |
| 29925060 | Fiddle | 4.200 | 12.600 | 880 | 20 |
| 29925061 | Stand-Up Spring | 3.500 | 10.500 | 520 | 20 |

#### 4.2.3 Ocean High-Load Serie

Die Ocean-Serie ist Lewmars Heavy-Duty-Linie für Offshore- und Blauwasser-Yachten.

| Artikel-Nr. | Typ | SWL (kg) | Bruchlast (kg) | Gewicht (g) | Seil max. (mm) |
|-------------|-----|----------|---------------|-------------|----------------|
| 29926010 | Ocean 60 Einzel | 2.500 | 7.500 | 380 | 16 |
| 29926012 | Ocean 60 Doppel | 3.500 | 10.500 | 680 | 16 |
| 29926015 | Ocean 80 Einzel | 4.200 | 12.600 | 720 | 20 |
| 29926017 | Ocean 80 Doppel | 5.500 | 16.500 | 1.250 | 20 |
| 29926020 | Ocean 80 Dreifach | 7.000 | 21.000 | 1.800 | 20 |
| 29926025 | Ocean 100 Einzel | 6.500 | 19.500 | 1.300 | 24 |
| 29926027 | Ocean 100 Doppel | 8.500 | 25.500 | 2.200 | 24 |

#### 4.2.4 Lewmar Deck Organizer

| Artikel-Nr. | Rollen | Rollendurchm. | SWL/Rolle (kg) | Gewicht (g) |
|-------------|--------|--------------|----------------|-------------|
| 29925070 | 3 | 50mm | 1.200 | 450 |
| 29925071 | 4 | 50mm | 1.200 | 580 |
| 29925072 | 5 | 50mm | 1.200 | 710 |
| 29925073 | 6 | 50mm | 1.200 | 840 |
| 29925080 | 3 | 60mm | 2.000 | 680 |
| 29925081 | 4 | 60mm | 2.000 | 880 |
| 29925082 | 5 | 60mm | 2.000 | 1.080 |

### 4.3 Ronstan

#### 4.3.1 Firmengeschichte und Positionierung

Ronstan (Melbourne, Australien, gegr. 1953) bietet ein breites Sortiment von Jolle bis Superyacht. Im Hochlast-Segment ist Ronstan mit der Orbit-Serie und den Series 55/60/75/100 präsent. Gutes Preis-Leistungs-Verhältnis.

#### 4.3.2 Ronstan Series 55

Die Series 55 ist Ronstans Einstieg in den Hochlast-Bereich.

| Artikel-Nr. | Typ | SWL (kg) | Bruchlast (kg) | Gewicht (g) | Seil max. (mm) |
|-------------|-----|----------|---------------|-------------|----------------|
| RF55110 | Einzel, Schäkel | 1.300 | 3.900 | 180 | 14 |
| RF55120 | Einzel, Becket | 1.300 | 3.900 | 195 | 14 |
| RF55210 | Doppel | 1.800 | 5.400 | 310 | 14 |
| RF55220 | Doppel, Becket | 1.800 | 5.400 | 330 | 14 |
| RF55310 | Dreifach | 2.200 | 6.600 | 450 | 14 |
| RF55510 | Fiddle | 1.600 | 4.800 | 260 | 14 |
| RF55520 | Fiddle, Becket | 1.600 | 4.800 | 280 | 14 |

#### 4.3.3 Ronstan Series 60

| Artikel-Nr. | Typ | SWL (kg) | Bruchlast (kg) | Gewicht (g) | Seil max. (mm) |
|-------------|-----|----------|---------------|-------------|----------------|
| RF60110 | Einzel, Schäkel | 2.200 | 6.600 | 310 | 16 |
| RF60120 | Einzel, Becket | 2.200 | 6.600 | 330 | 16 |
| RF60130 | Einzel, Wirbel | 2.200 | 6.600 | 370 | 16 |
| RF60210 | Doppel | 3.000 | 9.000 | 540 | 16 |
| RF60220 | Doppel, Becket | 3.000 | 9.000 | 570 | 16 |
| RF60310 | Dreifach | 3.800 | 11.400 | 780 | 16 |
| RF60510 | Fiddle | 2.700 | 8.100 | 460 | 16 |

#### 4.3.4 Ronstan Series 75

| Artikel-Nr. | Typ | SWL (kg) | Bruchlast (kg) | Gewicht (g) | Seil max. (mm) |
|-------------|-----|----------|---------------|-------------|----------------|
| RF75110 | Einzel, Schäkel | 3.200 | 9.600 | 480 | 18 |
| RF75120 | Einzel, Becket | 3.200 | 9.600 | 510 | 18 |
| RF75130 | Einzel, Wirbel | 3.200 | 9.600 | 560 | 18 |
| RF75210 | Doppel | 4.500 | 13.500 | 850 | 18 |
| RF75220 | Doppel, Becket | 4.500 | 13.500 | 890 | 18 |
| RF75310 | Dreifach | 5.500 | 16.500 | 1.250 | 18 |
| RF75510 | Fiddle | 4.000 | 12.000 | 720 | 18 |

#### 4.3.5 Ronstan Series 100

Ronstans Schwerlast-Linie für Yachten ab 16m.

| Artikel-Nr. | Typ | SWL (kg) | Bruchlast (kg) | Gewicht (g) | Seil max. (mm) |
|-------------|-----|----------|---------------|-------------|----------------|
| RF100110 | Einzel, Schäkel | 5.500 | 16.500 | 950 | 22 |
| RF100120 | Einzel, Becket | 5.500 | 16.500 | 990 | 22 |
| RF100210 | Doppel | 7.500 | 22.500 | 1.700 | 22 |
| RF100310 | Dreifach | 9.500 | 28.500 | 2.500 | 22 |
| RF100510 | Fiddle | 6.800 | 20.400 | 1.450 | 22 |

#### 4.3.6 Ronstan Orbit Blocks (55mm Hochlast)

Die Orbit-Serie nutzt ein einzigartiges Design mit durchgehender Seitenplatte und offenem Zugang für schnelles Einlegen des Seils.

| Artikel-Nr. | Typ | SWL (kg) | Bruchlast (kg) | Gewicht (g) | Seil max. (mm) |
|-------------|-----|----------|---------------|-------------|----------------|
| RF45111 | Orbit 55 Einzel | 1.800 | 5.400 | 155 | 14 |
| RF45112 | Orbit 55 Einzel, Becket | 1.800 | 5.400 | 170 | 14 |
| RF45211 | Orbit 55 Doppel | 2.400 | 7.200 | 270 | 14 |
| RF45311 | Orbit 55 Dreifach | 3.000 | 9.000 | 400 | 14 |
| RF45511 | Orbit 55 Fiddle | 2.100 | 6.300 | 230 | 14 |

#### 4.3.7 Ronstan Deck Organizer

| Artikel-Nr. | Rollen | Rollendurchm. | SWL/Rolle (kg) | Gewicht (g) |
|-------------|--------|--------------|----------------|-------------|
| RF78010 | 3 | 40mm | 800 | 310 |
| RF78020 | 4 | 40mm | 800 | 400 |
| RF78030 | 5 | 40mm | 800 | 490 |
| RF78040 | 6 | 40mm | 800 | 580 |
| RF78110 | 3 | 55mm | 1.400 | 520 |
| RF78120 | 4 | 55mm | 1.400 | 680 |
| RF78130 | 5 | 55mm | 1.400 | 840 |
| RF78210 | 3 | 75mm | 2.500 | 880 |
| RF78220 | 4 | 75mm | 2.500 | 1.150 |

### 4.4 Antal

#### 4.4.1 Firmengeschichte und Positionierung

Antal (Certaldo, Toscana, Italien, gegr. 1988) produziert hochwertige Rigg-Beschläge mit starkem Fokus auf italienisches Design und Innovation. Die XT-Carbon-Serie ist Antals Flaggschiff für Hochlast-Anwendungen.

#### 4.4.2 Antal XT Carbon High-Load Serie

Die XT Carbon-Serie verwendet CFK-Seitenplatten und Titan-Achsen für extreme Gewichtseinsparung.

| Artikel-Nr. | Typ | SWL (kg) | Bruchlast (kg) | Gewicht (g) | Seil max. (mm) |
|-------------|-----|----------|---------------|-------------|----------------|
| XT55C-S | XT55 Carbon Einzel | 1.800 | 5.400 | 95 | 14 |
| XT55C-SB | XT55 Carbon Einzel, Becket | 1.800 | 5.400 | 108 | 14 |
| XT55C-D | XT55 Carbon Doppel | 2.500 | 7.500 | 165 | 14 |
| XT55C-DB | XT55 Carbon Doppel, Becket | 2.500 | 7.500 | 180 | 14 |
| XT55C-T | XT55 Carbon Dreifach | 3.100 | 9.300 | 245 | 14 |
| XT55C-F | XT55 Carbon Fiddle | 2.200 | 6.600 | 140 | 14 |
| XT75C-S | XT75 Carbon Einzel | 3.200 | 9.600 | 180 | 18 |
| XT75C-D | XT75 Carbon Doppel | 4.500 | 13.500 | 320 | 18 |
| XT75C-T | XT75 Carbon Dreifach | 5.600 | 16.800 | 470 | 18 |
| XT100C-S | XT100 Carbon Einzel | 5.800 | 17.400 | 350 | 22 |
| XT100C-D | XT100 Carbon Doppel | 8.000 | 24.000 | 620 | 22 |

#### 4.4.3 Antal V-Grip Organizer

| Artikel-Nr. | Rollen | Rollendurchm. | SWL/Rolle (kg) | Gewicht (g) |
|-------------|--------|--------------|----------------|-------------|
| VG403 | 3 | 40mm | 900 | 280 |
| VG404 | 4 | 40mm | 900 | 360 |
| VG405 | 5 | 40mm | 900 | 440 |
| VG406 | 6 | 40mm | 900 | 520 |
| VG553 | 3 | 55mm | 1.500 | 480 |
| VG554 | 4 | 55mm | 1.500 | 620 |
| VG555 | 5 | 55mm | 1.500 | 760 |

### 4.5 Schaefer Marine

#### 4.5.1 Firmengeschichte und Positionierung

Schaefer Marine (New Bedford, Massachusetts, USA, gegr. 1960) ist ein etablierter amerikanischer Hersteller mit starkem Fokus auf Fahrtensegler und Blauwasser-Yachten. Schaefer-Produkte sind für ihre Robustheit und Langlebigkeit bekannt.

#### 4.5.2 Schaefer Hochlast-Blöcke

| Artikel-Nr. | Typ | SWL (kg) | Bruchlast (kg) | Gewicht (g) | Seil max. (mm) |
|-------------|-----|----------|---------------|-------------|----------------|
| 504-51 | Series 5 Einzel, 57mm | 1.800 | 5.400 | 280 | 16 |
| 504-52 | Series 5 Einzel, Becket | 1.800 | 5.400 | 300 | 16 |
| 504-53 | Series 5 Doppel, 57mm | 2.500 | 7.500 | 480 | 16 |
| 504-54 | Series 5 Doppel, Becket | 2.500 | 7.500 | 510 | 16 |
| 504-55 | Series 5 Dreifach | 3.200 | 9.600 | 700 | 16 |
| 504-71 | Series 7 Einzel, 75mm | 2.800 | 8.400 | 450 | 20 |
| 504-72 | Series 7 Einzel, Becket | 2.800 | 8.400 | 480 | 20 |
| 504-73 | Series 7 Doppel, 75mm | 3.800 | 11.400 | 800 | 20 |
| 504-74 | Series 7 Doppel, Becket | 3.800 | 11.400 | 840 | 20 |
| 504-75 | Series 7 Dreifach | 4.800 | 14.400 | 1.200 | 20 |

#### 4.5.3 Schaefer Mainsheet Systems

| Artikel-Nr. | System | Übersetzung | Max. Last (kg) | Bootsklasse |
|-------------|--------|-------------|---------------|-------------|
| 504-MS4 | Series 5 Mainsheet | 4:1 | 2.500 | 8–11m |
| 504-MS6 | Series 5 Mainsheet | 6:1 | 3.200 | 10–13m |
| 504-MS6H | Series 7 Mainsheet | 6:1 | 4.800 | 12–16m |
| 504-MS8 | Series 7 Mainsheet | 8:1 | 6.000 | 14–18m |

### 4.6 Garhauer Marine

#### 4.6.1 Firmengeschichte und Positionierung

Garhauer Marine (Lemon Grove, Kalifornien, USA, gegr. 1972) ist der bekannteste Anbieter für budgetfreundliche Hochlast-Blöcke. Alle Produkte werden aus Edelstahl 316L gefertigt und direkt an den Endkunden verkauft, ohne Zwischenhandel.

**Garhauer-Philosophie:** Robuster Edelstahl statt leichtem Aluminium. Höheres Gewicht, aber deutlich niedrigerer Preis (oft 40–60% günstiger als Harken/Lewmar).

#### 4.6.2 Garhauer Hochlast-Blöcke

| Artikel-Nr. | Typ | SWL (kg) | Bruchlast (kg) | Gewicht (g) | Seil max. (mm) | Preis ca. (€) |
|-------------|-----|----------|---------------|-------------|----------------|--------------|
| 60-01-OT | Single, 60mm, Kugellager | 1.800 | 5.400 | 340 | 16 | 85 |
| 60-02-OT | Single, Becket | 1.800 | 5.400 | 370 | 16 | 95 |
| 60-04-OT | Double | 2.500 | 7.500 | 580 | 16 | 140 |
| 60-05-OT | Double, Becket | 2.500 | 7.500 | 620 | 16 | 155 |
| 60-06-OT | Triple | 3.200 | 9.600 | 850 | 16 | 195 |
| 60-10-OT | Fiddle | 2.200 | 6.600 | 480 | 16 | 120 |
| 75-01-OT | Single, 75mm, Kugellager | 2.800 | 8.400 | 550 | 20 | 120 |
| 75-02-OT | Single, Becket | 2.800 | 8.400 | 590 | 20 | 135 |
| 75-04-OT | Double | 3.800 | 11.400 | 980 | 20 | 195 |
| 75-05-OT | Double, Becket | 3.800 | 11.400 | 1.030 | 20 | 215 |
| 75-06-OT | Triple | 4.800 | 14.400 | 1.450 | 20 | 275 |

**Preisvergleich (75mm Einzelblock):**

| Hersteller | Modell | Bruchlast (kg) | Gewicht (g) | Preis ca. (€) | €/kg Bruchlast |
|-----------|--------|---------------|-------------|--------------|----------------|
| Garhauer | 75-01-OT | 8.400 | 550 | 120 | 0,014 |
| Ronstan | RF75110 | 9.600 | 480 | 185 | 0,019 |
| Lewmar | Synchro 80 | 10.500 | 580 | 220 | 0,021 |
| Harken | Black 75 (2645) | 8.850 | 425 | 245 | 0,028 |
| Antal | XT75C-S (Carbon) | 9.600 | 180 | 385 | 0,040 |

#### 4.6.3 Garhauer Mainsheet und Vang Systeme

| Artikel-Nr. | System | Übersetzung | Max. Last (kg) | Preis ca. (€) |
|-------------|--------|-------------|---------------|--------------|
| 60-MS-4 | Mainsheet 60mm | 4:1 | 2.500 | 240 |
| 60-MS-6 | Mainsheet 60mm | 6:1 | 3.200 | 360 |
| 75-MS-6 | Mainsheet 75mm | 6:1 | 4.800 | 480 |
| 75-MS-8 | Mainsheet 75mm | 8:1 | 6.000 | 650 |
| 60-VK-6 | Vang/Kicker 60mm | 6:1 | 2.500 | 280 |
| 75-VK-8 | Vang/Kicker 75mm | 8:1 | 3.800 | 420 |

### 4.7 Weitere Hersteller

#### 4.7.1 Rutgerson (Schweden)

Hochwertige Aluminium-Blöcke, stark im skandinavischen Markt.

| Artikel-Nr. | Typ | SWL (kg) | Bruchlast (kg) | Gewicht (g) |
|-------------|-----|----------|---------------|-------------|
| R60S | 60mm Einzel, Kugellager | 2.000 | 6.000 | 290 |
| R60D | 60mm Doppel | 2.800 | 8.400 | 500 |
| R80S | 80mm Einzel | 3.500 | 10.500 | 540 |
| R80D | 80mm Doppel | 4.800 | 14.400 | 960 |
| R80T | 80mm Dreifach | 6.000 | 18.000 | 1.400 |

#### 4.7.2 Selden (Schweden)

Mast- und Rigg-Hersteller mit eigenem Block-Sortiment.

| Artikel-Nr. | Typ | SWL (kg) | Bruchlast (kg) | Gewicht (g) |
|-------------|-----|----------|---------------|-------------|
| 481-011 | 60mm Einzel | 1.500 | 4.500 | 260 |
| 481-012 | 60mm Doppel | 2.200 | 6.600 | 440 |
| 481-021 | 80mm Einzel | 2.800 | 8.400 | 480 |
| 481-022 | 80mm Doppel | 3.800 | 11.400 | 860 |

#### 4.7.3 Frederiksen (Dänemark)

Spezialist für Rollen und Blöcke im europäischen Jollen- und Kielboot-Segment.

| Artikel-Nr. | Typ | SWL (kg) | Bruchlast (kg) | Gewicht (g) |
|-------------|-----|----------|---------------|-------------|
| FK60S | 60mm Einzel | 1.800 | 5.400 | 250 |
| FK60D | 60mm Doppel | 2.500 | 7.500 | 420 |
| FK75S | 75mm Einzel | 2.800 | 8.400 | 410 |

#### 4.7.4 Karver (Frankreich)

Innovativer Hersteller mit Fokus auf Racing. Bekannt für Furler und Hochlast-Beschläge.

| Artikel-Nr. | Typ | SWL (kg) | Bruchlast (kg) | Gewicht (g) |
|-------------|-----|----------|---------------|-------------|
| KV-HL60S | HL60 Einzel | 2.200 | 6.600 | 220 |
| KV-HL60D | HL60 Doppel | 3.000 | 9.000 | 380 |
| KV-HL80S | HL80 Einzel | 3.800 | 11.400 | 400 |
| KV-HL80D | HL80 Doppel | 5.200 | 15.600 | 720 |

#### 4.7.5 Allen Brothers (UK)

Starkes Sortiment für Jollen und kleinere Kielboote. Im Hochlast-Bereich begrenzt.

| Artikel-Nr. | Typ | SWL (kg) | Bruchlast (kg) | Gewicht (g) |
|-------------|-----|----------|---------------|-------------|
| A2060 | 60mm Einzel | 1.500 | 4.500 | 240 |
| A2061 | 60mm Doppel | 2.000 | 6.000 | 400 |
| A2075 | 75mm Einzel | 2.200 | 6.600 | 380 |

---

## 5. Montage und Installation

### 5.1 Grundprinzipien der Hochlast-Montage

#### 5.1.1 Kraftfluss-Analyse

Vor jeder Hochlast-Installation muss der Kraftfluss analysiert werden:

```
1. Lastquelle identifizieren (Segel, Rigg, Anker)
2. Lastvektor bestimmen (Richtung, Größe, Dynamik)
3. Umlenkwinkel berechnen → Block-Last ermitteln
4. Lasteinleitung in die Struktur definieren
5. Strukturverstärkung dimensionieren
6. Befestigungsmittel auswählen
7. Drehmomente festlegen
```

#### 5.1.2 Niemals nur Schrauben bei Hochlast

**Grundregel:** Hochlast-Blöcke werden IMMER mit Durchgangsbolzen (Through-Bolts) befestigt. Blechschrauben, Holzschrauben oder selbstschneidende Schrauben sind bei Lasten über 500 kg am Befestigungspunkt unzulässig.

| Befestigungsart | Max. Auszugskraft (kg) | Anwendung |
|-----------------|----------------------|-----------|
| Blechschraube 5mm in GFK | 150–250 | Kein Hochlast |
| Maschinenschraube M6 in Einschlagmutter | 400–600 | Kein Hochlast |
| Durchgangsbolzen M8 mit Backing Plate | 2.500–4.000 | Mittlere Hochlast |
| Durchgangsbolzen M10 mit Backing Plate | 4.000–6.500 | Schwere Hochlast |
| Durchgangsbolzen M12 mit Backing Plate | 6.500–10.000 | Extreme Hochlast |
| Durchgangsbolzen M16 mit Backing Plate | 10.000–18.000 | Superyacht |
| Einlaminierte Lastplatte | 15.000+ | Custom/Racing |

### 5.2 Decksverstärkung (Deck Reinforcement)

#### 5.2.1 Sandwich-Kern-Verstärkung

Moderne Yachtdecks verwenden Sandwich-Bauweise (GFK-Kern-GFK). Der Kern (Balsa, PVC-Schaum, Nomex) hat nur geringe Druckfestigkeit. Unter Hochlast-Beschlägen muss der Kern entfernt und durch Massiv-Laminat oder Epoxid-Füllung ersetzt werden.

**Verfahren:**

```
1. Kernbereich markieren (min. 1,5× Backing-Plate-Fläche)
2. Obere GFK-Haut lokal entfernen (Fräser/Router)
3. Kern entfernen (Stechbeitel, Oszillierwerkzeug)
4. Hohlraum reinigen (Aceton, Staubsauger)
5. Mit Epoxid-Füllmasse füllen (z.B. West System 105/206 + 407 Filler)
6. Aushärten lassen (min. 24h bei 20°C)
7. Oberfläche planschleifen
8. Optional: Zusätzliche GFK-Lagen über die Füllung laminieren
9. Bohrungen durch verstärkten Bereich setzen
10. Bolzen montieren mit Dichtmasse (Sikaflex 295 UV)
```

#### 5.2.2 Kernverstärkung mit Kompressionsröhrchen

Alternative zur Kern-Entfernung: Kompressionsröhrchen (Compression Tubes) werden durch das gesamte Sandwich gesteckt und verhindern, dass der Kern beim Anziehen der Bolzen zusammengedrückt wird.

**Material:** Edelstahl 316L oder Aluminium 6061-T6
**Dimensionierung:** Innendurchmesser = Bolzendurchmesser + 0,5 mm, Länge = Decksstärke

```
Kompressionsröhrchen-Einbau:
1. Bohrung durch Deck (Durchmesser = Röhrchen-Außendurchmesser)
2. Kern um die Bohrung herum auskratzen (5mm Radius)
3. Hohlraum mit Epoxid verfüllen
4. Röhrchen einsetzen und in Epoxid einbetten
5. Aushärten lassen
6. Bolzen durch Röhrchen führen
7. Backing Plate unterseitig montieren
8. Anziehen — das Röhrchen nimmt die Kompressionskraft auf
```

### 5.3 Backing Plates (Verstärkungsplatten)

#### 5.3.1 Dimensionierung

Die Backing Plate verteilt die Ausziehkraft auf eine größere Fläche der Unterseite des Decks.

**Mindestanforderungen:**

| Block-SWL (kg) | Min. Backing Plate | Material | Stärke |
|----------------|-------------------|----------|--------|
| 500–1.500 | 80×80 mm | Edelstahl 316L | 3 mm |
| 1.500–3.000 | 100×100 mm | Edelstahl 316L | 4 mm |
| 3.000–5.000 | 120×120 mm | Edelstahl 316L | 5 mm |
| 5.000–8.000 | 150×150 mm | Edelstahl 316L | 6 mm |
| 8.000–12.000 | 180×180 mm | Edelstahl 316L | 8 mm |
| 12.000–20.000 | 220×220 mm | Edelstahl 316L | 10 mm |
| 20.000+ | Custom, einlaminiert | Edelstahl/Titan | 12+ mm |

#### 5.3.2 Backing Plate vs. Fender Washer

**Fender Washer (große Unterlegscheibe):** Nur für Lasten unter 1.000 kg akzeptabel. Verformt sich unter Hochlast und bietet keine ausreichende Lastverteilung.

**Backing Plate:** Durchgehende Platte unter allen Bolzen eines Beschlags. Verbindet die Bolzen strukturell und verhindert lokales Versagen.

**Brückenplatte:** Verstärkungsplatte, die über mehrere Beschläge hinweggeht und die Last auf die Stringer oder Rahmenstruktur überträgt. Erforderlich bei extremen Lasten (>10.000 kg).

### 5.4 Chainplates für Hochlast-Blöcke

#### 5.4.1 Design-Prinzipien

Chainplates (Püttinge) leiten die Rigg-Kräfte vom Beschlag in die Schiffsstruktur ein. Bei Running Backstays und Backstag-Trimmern sind die Lasten so hoch, dass dedizierte Chainplates erforderlich sind.

**Materialien:**
- Edelstahl 316L (Standard): Zugfestigkeit 500–620 MPa
- Edelstahl 17-4 PH (Racing): Zugfestigkeit 1.070–1.310 MPa
- Titan Grade 5 (Superyacht): Zugfestigkeit 950 MPa, korrosionsbeständig, leicht

**Dimensionierung (vereinfacht):**

```
Chainplate-Querschnitt = Designlast × SF / Zugfestigkeit_Material

Beispiel: Running Backstay, 14m Yacht
  Designlast: 5.000 kg = 49.050 N
  SF: 4:1
  Material: 316L, 550 MPa
  
  A = (49.050 × 4) / 550 = 357 mm²
  → Flachstahl 50 × 8 mm (400 mm²) oder 40 × 10 mm (400 mm²)
```

### 5.5 Lastverteilung über Stringer

Bei Lasten über 5.000 kg reicht eine Backing Plate allein nicht aus. Die Last muss über Stringer (Längsversteifungen) in die Gesamtstruktur eingeleitet werden.

**Methoden:**
1. **Knees (Kniebleche):** Edelstahl-Winkel, die vom Beschlag-Bereich zu einem Stringer oder Schott führen.
2. **Einlaminierte Verstärkung:** GFK-Lagen, die vom Deck durch den Rumpf zu Stringer oder Kiel-Laminat führen.
3. **Stahlrahmen:** Bei Aluminiumyachten werden Stahlrahmen unter dem Deck geschweißt.

### 5.6 Dichtung und Korrosionsschutz

#### 5.6.1 Bolzendurchführungen abdichten

Jede Durchbohrung des Decks ist eine potenzielle Leckstelle. Bei Hochlast-Befestigungen ist die Abdichtung besonders kritisch, da die Beschläge unter Last arbeiten und sich minimal bewegen.

**Empfohlene Dichtstoffe:**

| Dichtstoff | Anwendung | Vorteile | Nachteile |
|-----------|-----------|---------|-----------|
| Sikaflex 295 UV | Standard-Abdichtung | UV-beständig, elastisch | Langsame Aushärtung |
| Sikaflex 291i | Bolzen-Abdichtung | Thixotrop, läuft nicht | Schwer entfernbar |
| 3M 4200 | Bolzen-Abdichtung | Gut entfernbar | Weniger UV-beständig |
| Butylband | Unter Backing Plate | Preiswert, sofort dicht | Keine strukturelle Festigkeit |

#### 5.6.2 Galvanische Korrosion verhindern

Bei Hochlast-Blöcken treffen häufig verschiedene Metalle aufeinander (Aluminium-Block auf Edelstahl-Bolzen auf GFK-Deck). Galvanische Korrosion muss verhindert werden:

- **Isolierbuchsen** (Nylon oder PTFE) zwischen Aluminium und Edelstahl
- **Isolier-Unterlegscheiben** unter dem Aluminium-Gehäuse
- **Duralac oder Tef-Gel** als Kontaktschutzmittel auf allen Metalloberflächen
- **Lanolin-basierte Fette** (Lanocote) auf Bolzen und in Gewinden

### 5.7 Drehmomente für Hochlast-Befestigungen

| Bolzengröße | Material | Drehmoment (Nm) | Bemerkung |
|-------------|---------|----------------|-----------|
| M6 | A4-80 | 8–10 | Nur Cheek Blocks |
| M8 | A4-80 | 18–22 | Leichte Hochlast |
| M10 | A4-80 | 35–42 | Standard-Hochlast |
| M12 | A4-80 | 60–72 | Schwere Hochlast |
| M16 | A4-80 | 140–170 | Extreme Hochlast |
| M6 | Titan Gr.5 | 10–12 | Racing |
| M8 | Titan Gr.5 | 22–26 | Racing |
| M10 | Titan Gr.5 | 44–52 | Racing |

**Immer mit Drehmomentschlüssel anziehen!** Überdrehen zerstört den GFK-Kern oder die Kompressionsröhrchen. Unterdrehen führt zu lockerem Sitz und Ermüdungsbruch.

### 5.8 Retrofit-Überlegungen

Beim nachträglichen Einbau von Hochlast-Blöcken auf bestehenden Yachten:

1. **Vorhandene Verstärkung prüfen:** Oft sind unter dem ursprünglichen Beschlag bereits Kernverstärkungen vorhanden. Position genau dokumentieren.
2. **Laminat-Dicke messen:** Ultraschall-Dickenmessung oder destruktive Probe an verdeckter Stelle.
3. **Stringer-Lage ermitteln:** Stringer können durch leichtes Klopfen (Klangunterschied) oder mit einem Metallsucher lokalisiert werden.
4. **Vorhandene Bohrungen nutzen:** Wenn möglich, vorhandene Durchgangsbolzen-Positionen übernehmen. Neue Bohrungen schwächen das Laminat.
5. **Kernverstärkung nachrüsten:** Bei Sandwich-Bauweise ist nachträgliche Kernverstärkung von oben möglich (Kern ausbohren, Epoxid einfüllen).

---

## 6. Anlagen-spezifische Zuordnung

### 6.1 Zuordnungstabelle: System → Hochlast-Block

| System | Block-Typ | Rollengrößen | SWL-Bereich | Befestigung | Besonderheiten |
|--------|-----------|-------------|-------------|-------------|----------------|
| Großschot (Mittschiffs) | Doppel/Dreifach + Becket | 57–100mm | 2.000–8.000 kg | Traveller-Wagen | Integrierte Klemme üblich |
| Großschot (End-Boom) | Einzel/Doppel + Becket | 57–100mm | 2.500–10.000 kg | Deck/Cockpitboden | Längerer Schotweg |
| Baumniederholer (Vang) | Doppel/Dreifach | 40–75mm | 1.000–4.000 kg | Mastfuß + Baum | Oft mit Gasdruckfeder |
| Backstag-Trimmer | Einzel/Doppel | 57–100mm | 2.000–10.000 kg | Heckbereich | Hohe Einzellast |
| Running Backstay | Einzel (Turning) | 75–100mm | 3.000–15.000 kg | Cockpit-Seite | Extremste Lasten im laufenden Gut |
| Genuaschot-Umlenkung | Turning Block | 57–75mm | 1.500–5.000 kg | Deck, Schiene | Variable Position |
| Rollreff-Leine | Einzel + Deck-Organizer | 40–57mm | 800–3.000 kg | Deck/Cockpit | Muss unter Last drehen |
| Spinnaker-Barber-Hauler | Einzel (Turning) | 40–57mm | 800–3.000 kg | Deck-Schiene | Variable Position |
| Mastfuß-Umlenkung | Cheek Block / Organizer | 40–75mm | 500–3.000 kg | Mastfuß-Bereich | Viele Leinen eng beieinander |
| Trysegel-Schot | Einzel | 57–75mm | 1.500–5.000 kg | Deck, Relingsbereich | Muss bei Sturm funktionieren |
| Code 0 / Gennaker | Turning Block | 57–75mm | 1.500–5.000 kg | Bug/Deck | Hohe Dynamik |
| Cunningham/Vorliek-Strecker | Einzel/Doppel | 40–57mm | 500–2.000 kg | Mastfuß | Schnell trimmen |

### 6.2 Bootsgröße → System → Block-Empfehlung

#### 6.2.1 Fahrtensegler 8–10m

| System | Empfohlener Block | Beispiel-Modell |
|--------|-------------------|----------------|
| Großschot 4:1 | Doppel 57mm + Einzel 57mm Becket | Harken 1088 + 1087 |
| Vang 4:1 | Doppel 40mm + Einzel 40mm Becket | Ronstan RF45211 + RF45112 |
| Genuaschot-Turning | Einzel 57mm Stand-Up | Harken 2691 |
| Mastfuß-Organizer | 3-Rollen, 40mm | Harken 3232 |

#### 6.2.2 Performance Cruiser 10–14m

| System | Empfohlener Block | Beispiel-Modell |
|--------|-------------------|----------------|
| Großschot 6:1 | Dreifach 57mm + Doppel 57mm Becket | Harken 2658 + 2656 |
| Vang 8:1 | Kaskade mit 57mm Blöcken | Harken 1088 × 2 + 1087 |
| Backstag-Trimmer | Einzel 75mm × 2 | Lewmar Synchro 80 |
| Genuaschot-Turning | Einzel 57mm Stand-Up | Ronstan RF60130 |
| Mastfuß-Organizer | 5-Rollen, 50mm | Lewmar 29925072 |

> ⚠️ **ZU PRÜFEN (Audit):** Größenangabe "Dreifach 57mm + Doppel 57mm Becket" widerspricht den zitierten Artikelnummern: Harken 2658 (Dreifach) und 2656 (Doppel, Becket) sind laut Abschnitt 4.1.2 und Anhang K die Black-Magic-**75-mm**-Blöcke (in 6.2.3 werden dieselben Artikel korrekt als 75 mm geführt). Eine 57-mm-Variante dieser Artikel existiert im Katalog dieser Datei nicht — Größenangabe oder Artikelnummer ist widersprüchlich.

#### 6.2.3 Blauwasser-Yacht 12–18m

| System | Empfohlener Block | Beispiel-Modell |
|--------|-------------------|----------------|
| Großschot 6:1 / 8:1 | Dreifach 75mm + Doppel 75mm Becket | Harken 2660 + 2656 |
| Vang 8:1 | Dreifach 57mm + Doppel 57mm | Lewmar Synchro 60 |
| Backstag-Trimmer | Einzel 75mm × 2 mit Talje | Ronstan RF75130 |
| Running Backstay | Einzel 100mm | Ronstan RF100110 |
| Genuaschot-Turning | Einzel 75mm | Harken 2646 |
| Mastfuß-Organizer | 5-Rollen, 60mm | Harken 3254 |
| Trysegel-Schot | Einzel 57mm × 2 | Lewmar Ocean 60 |

#### 6.2.4 Regatta-Yacht 12–20m

| System | Empfohlener Block | Beispiel-Modell |
|--------|-------------------|----------------|
| Großschot 8:1 | Kaskade, Carbon-Blöcke | Antal XT75C-T + XT75C-D |
| Vang 16:1 | Kaskade mit Winch-Assist | Antal XT55C Kaskade |
| Running Backstay | Einzel 100mm, Nadellager | Harken Black 100mm |
| Mastfuß-Organizer | 6-Rollen, 55mm, Carbon | Antal VG556 |

### 6.3 Budget-Szenarien

| Szenario | Empfehlung | Preis-Niveau |
|---------|------------|-------------|
| Budget-Refit, 10m Fahrtensegler | Garhauer 60mm Edelstahl-Systeme | € 300–800 gesamt |
| Standard-Refit, 12m Cruiser | Ronstan Series 60 oder Harken ESP | € 800–2.000 gesamt |
| Performance-Upgrade, 14m | Harken Black Magic oder Lewmar Synchro 80 | € 1.500–4.000 gesamt |
| Racing-Optimierung, 12m | Antal XT Carbon oder Harken Titanium | € 3.000–8.000 gesamt |
| Superyacht-Neubau, 20m+ | Harken Custom + Lewmar Ocean 100 | € 8.000–25.000 gesamt |

---

## 7. Fehlerbild-Atlas

### 7.1 Fehlerbild F-HL-01: Achsbruch unter Last

**Beschreibung:** Die Rollenachse bricht unter Betriebslast. Katastrophales Versagen — Block gibt sofort auf, Seil wird frei.

**Symptome:**
- Metallisches Knacken vor dem Versagen
- Sichtbare Biegung der Achse
- Ungleichmäßiger Rollenlauf (Vorstufe)
- Feine Risse an der Achse (nur mit Lupe sichtbar)

**Ursachen:**
- Überlast (falsche Dimensionierung)
- Ermüdungsbruch nach vielen Zyklen
- Korrosionsriss (Spannungsrisskorrosion bei 304-Edelstahl in Salzwasser)
- Material-Defekt (Einschlüsse im Schmiedestück)

**AYDI-Bewertung:**
- Confidence: `measured` (wenn Achse inspizierbar), `visual_medium` (Foto)
- Schweregrad: KRITISCH
- Sofortmaßnahme: Block sofort ersetzen

**Prävention:**
- Achsdurchmesser kontrollieren (Schieblehre, Vergleich mit Neuzustand)
- Achse alle 2 Jahre auf Risse prüfen (Magnetpulverprüfung oder Farbeindringverfahren)
- Bei Anzeichen von Biegung sofort tauschen
- Nur Blöcke mit dokumentierter Bruchlast verwenden

### 7.2 Fehlerbild F-HL-02: Lagerschaden durch Überlast

**Beschreibung:** Die Kugel- oder Nadellager im Block werden durch zu hohe Flächenpressung deformiert (Brinelling). Die Rolle läuft rau und hat erhöhte Reibung.

**Symptome:**
- Raues, knirschendes Geräusch beim Drehen
- Spürbare Rastpunkte beim langsamen Drehen
- Erhöhter Schotzug erforderlich
- Sichtbarer Metallabrieb (grau-schwarze Paste)

**Ursachen:**
- Schocklasten über der Lagertragzahl
- Mangelhafte Schmierung
- Seewasser-Eindrang in das Lager
- Falsche Seilgröße (zu dick → erhöhte Radialkraft)

**AYDI-Bewertung:**
- Confidence: `measured` (Lager inspizierbar), `visual_low` (nur äußerlich)
- Schweregrad: MITTEL bis HOCH (betriebseinschränkend, kein sofortiges Versagen)

**Prävention:**
- Regelmäßige Schmierung (alle 200 Betriebsstunden)
- Lager-Austausch alle 5 Jahre (Fahrten) oder 3 Jahre (Regatta)
- Seilgröße gemäß Hersteller-Empfehlung

### 7.3 Fehlerbild F-HL-03: Gehäuseriss (Aluminium)

**Beschreibung:** Das Aluminium-Gehäuse des Blocks zeigt Ermüdungsrisse, typischerweise an den Bohrungen und Übergangsradien.

**Symptome:**
- Sichtbare Haarrisse in der Anodisierung
- Riss folgt Bearbeitungsspuren
- Weiß-graue Korrosionsprodukte an der Rissöffnung
- Leichtes Klappern des Blocks

**Ursachen:**
- Ermüdung durch zyklische Belastung
- Kerb-Wirkung an Bearbeitungsfehlern
- Galvanische Korrosion (ungeschützter Kontakt mit Edelstahl)
- Überhitzung beim Anodisieren (Materialschädigung)

**AYDI-Bewertung:**
- Confidence: `visual_high` (gut sichtbar bei Nahaufnahme)
- Schweregrad: HOCH bis KRITISCH
- Sofortmaßnahme: Block sofort ersetzen, keinesfalls weiter belasten

### 7.4 Fehlerbild F-HL-04: Rollenverschleiß (Scheave Groove Wear)

**Beschreibung:** Die Rollenrille ist durch langjährigen Einsatz ausgeschliffen. Der Seildurchmesser passt nicht mehr optimal.

**Symptome:**
- Sichtbare Rille tiefer als Neuzustand
- Seil liegt tief in der Rolle (erkennbar am Seilstand)
- Seil-Mantel zeigt übermäßigen Abrieb
- Seil springt leichter aus der Rolle

**Ursachen:**
- Normaler Verschleiß (10.000+ Zyklen)
- Verwendung von Dyneema/Spectra-Seilen (schneidet in Kunststoff-Rollen)
- Sand und Salzkristalle in der Rille (Schleifwirkung)
- Zu hohe Seil-Spannung für die Rollengröße

**AYDI-Bewertung:**
- Confidence: `visual_medium` (erkennbar bei Detailaufnahme)
- Schweregrad: MITTEL
- Maßnahme: Rolle tauschen (bei modularen Blöcken) oder Block ersetzen

### 7.5 Fehlerbild F-HL-05: Befestigungsversagen (Bolt Pull-Out)

**Beschreibung:** Die Durchgangsbolzen reißen aus dem Deck. Das häufigste und gefährlichste Hochlast-Versagen.

**Symptome:**
- Block hebt sich sichtbar vom Deck ab
- Risse im Gelcoat um die Bolzenköpfe
- Backing Plate verformt oder durchgestanzt
- Wasser-Eintritt an den Bolzendurchführungen

**Ursachen:**
- Fehlende oder unzureichende Backing Plate
- Kein Kernverstärkung im Sandwich-Aufbau
- Falsche Bolzengröße (zu dünn)
- Bolzen nicht korrekt angezogen (zu wenig Drehmoment → Mikrobewegung → Aufweitung)
- Überlast (falsche Dimensionierung des Gesamtsystems)

**AYDI-Bewertung:**
- Confidence: `visual_high` (deutlich sichtbar)
- Schweregrad: KRITISCH
- Sofortmaßnahme: Block sofort entlasten, System nicht weiter nutzen

### 7.6 Fehlerbild F-HL-06: Seil-Einklemmung (Line Jam)

**Beschreibung:** Das Seil klemmt sich zwischen Rolle und Gehäuse ein und kann nicht mehr bewegt werden.

**Symptome:**
- Seil lässt sich weder dichtholen noch fieren
- Sichtbare Seil-Deformation (Quetschung)
- Extreme Kräfte auf den Block (Winch dreht gegen Klemmer)

**Ursachen:**
- Zu dünnes Seil für die Rollenrille
- Seil-Mantel-Schaden (aufgeplusterte Fasern)
- Fremdkörper in der Rille (Splitter, Bolzen, Seilreste)
- Fehlende Anti-Chafe-Platte

**AYDI-Bewertung:**
- Confidence: `visual_high` (sofort erkennbar)
- Schweregrad: HOCH (kann zu Folgeschäden führen)
- Sofortmaßnahme: Last reduzieren, Seil aus Block befreien, Block inspizieren

### 7.7 Fehlerbild F-HL-07: Wirbel-Versagen (Swivel Failure)

**Beschreibung:** Der Wirbel (Swivel) am Blockkopf versagt — entweder durch Ermüdung oder Korrosion.

**Symptome:**
- Wirbel dreht schwer oder gar nicht
- Sichtbare Verformung des Wirbel-Stifts
- Korrosionsprodukte am Wirbel-Gelenk
- Ungleichmäßige Abnutzung der Wirbel-Backen

**Ursachen:**
- Dauerhaft seitliche Belastung (Wirbel soll nur kurzzeitig seitlich belastet werden)
- Korrosion im Wirbel-Gelenk (Spalt-Korrosion)
- Überlast

**AYDI-Bewertung:**
- Confidence: `visual_medium`
- Schweregrad: HOCH (Wirbel-Bruch = Block-Verlust)

### 7.8 Fehlerbild F-HL-08: Galvanische Korrosion am Befestigungspunkt

**Beschreibung:** Elektrochemische Korrosion zwischen Aluminium-Block und Edelstahl-Bolzen oder zwischen verschiedenen Metallteilen.

**Symptome:**
- Weiß-graue Korrosionsprodukte (Aluminium) um die Bolzen
- Braune Verfärbung (Edelstahl) an Kontaktflächen
- Gelcoat-Blasen oder -Abplatzungen um den Beschlag
- Block sitzt fest und lässt sich nicht mehr lösen

**Ursachen:**
- Fehlende Isolierung zwischen ungleichen Metallen
- Kein Kontaktschutzmittel (Tef-Gel, Duralac) verwendet
- Mangelhafte Abdichtung (Salzwasser als Elektrolyt)

**AYDI-Bewertung:**
- Confidence: `visual_high` (farblich gut erkennbar)
- Schweregrad: MITTEL bis HOCH (langfristiger Festigkeitsverlust)

### 7.9 Fehlerbild F-HL-09: Schäkel-Ermüdung

**Beschreibung:** Der Schäkel zwischen Block und Augplatte/Chainplate ermüdet und entwickelt Risse.

**Symptome:**
- Schäkel ist sichtbar aufgebogen
- Bolzen sitzt nicht mehr stramm
- Feine Risse am Schäkelbogen (oft nur mit Lupe sichtbar)
- Schäkel hat sich verdreht

**Ursachen:**
- Unterdimensionierter Schäkel
- Zyklische Belastung (Ermüdung)
- Falscher Schäkeltyp (D-Schäkel statt Bogenschäkel bei seitlicher Last)

**AYDI-Bewertung:**
- Confidence: `visual_medium` (Risse schwer erkennbar)
- Schweregrad: HOCH
- Maßnahme: Schäkel nach Inspektion tauschen, SF 4:1 beachten

### 7.10 Fehlerbild F-HL-10: Deck-Organizer Fehlausrichtung

**Beschreibung:** Ein Deck-Organizer ist schief montiert, einzelne Rollen laufen unter Zwang.

**Symptome:**
- Seile laufen nicht frei durch einzelne Rollen
- Einseitiger Verschleiß an den Rollen
- Seil-Mantel-Abrieb auf einer Seite
- Erhöhte Reibung, schweres Trimmen

**Ursachen:**
- Fehlerhafte Montage (schief gebohrt)
- Deck-Verformung unter Last
- Organizer für falschen Seilwinkel installiert

**AYDI-Bewertung:**
- Confidence: `visual_medium` (bei Betriebsaufnahme erkennbar)
- Schweregrad: NIEDRIG bis MITTEL

### 7.11 Fehlerbild F-HL-11: Thermische Überlastung der Rolle

**Beschreibung:** Die Kunststoff-Rolle erweicht oder verformt sich durch Reibungswärme bei hoher Last und Seilgeschwindigkeit.

**Symptome:**
- Glänzende, glatte Stellen auf der Rille
- Rolle hat eine ovale Form angenommen
- Seil-Mantel zeigt Schmelzspuren
- Geruch nach verbranntem Kunststoff

**Ursachen:**
- Zu hohe Last für Kunststoff-Rolle (hätte Metall-Rolle sein sollen)
- Blockiertes Lager (Rolle dreht nicht, Seil gleitet über stehende Rolle)
- Übermäßig schnelles Fieren unter Last

**AYDI-Bewertung:**
- Confidence: `visual_high` (Verformung deutlich sichtbar)
- Schweregrad: HOCH (sofortiger Austausch)

### 7.12 Fehlerbild F-HL-12: Seilrille-Gratbildung (Burr Formation)

**Beschreibung:** An der Kante der Metallrille (Aluminium oder Edelstahl) bildet sich ein scharfer Grat, der den Seil-Mantel beschädigt.

**Symptome:**
- Seil-Mantel hat scharfe Schnittspuren (einseitig)
- Sichtbarer Grat an der Rollenkante
- Fasern hängen aus dem Mantel
- Seil-Bruchlast signifikant reduziert

**Ursachen:**
- Schlagschaden am Block (Block wurde getroffen oder eingeklemmt)
- Fertigungsfehler (unzureichend entgratet)
- Korrosions-Pittings an der Rollenkante

**AYDI-Bewertung:**
- Confidence: `visual_high` (Seilschaden deutlich sichtbar)
- Schweregrad: HOCH (Seil-Bruch-Risiko)
- Sofortmaßnahme: Grat entfernen (Schleifpapier 400er), Block-Kante polieren, Seil prüfen

---

## 8. Troubleshooting-Entscheidungsbaum

### 8.1 Entscheidungsbaum: Block wird heiß unter Last

```
Block wird heiß (>50°C handwarm) unter Last
├── Rolle dreht frei (von Hand)?
│   ├── JA
│   │   ├── Seil-Spannung > SWL?
│   │   │   ├── JA → Block unterdimensioniert. Größere Klasse wählen.
│   │   │   └── NEIN → Seil zu dünn für Rille? 
│   │   │       ├── JA → Seil durch korrekten Durchmesser ersetzen.
│   │   │       └── NEIN → Normaler Betrieb bei hoher Last. 
│   │   │           Prüfen: Kunststoff- oder Metall-Rolle?
│   │   │           ├── Kunststoff → Metall-Rolle nachrüsten.
│   │   │           └── Metall → Lager schmieren, beobachten.
│   └── NEIN (Rolle klemmt)
│       ├── Fremdkörper in der Rolle?
│       │   ├── JA → Reinigen, Rolle prüfen.
│       │   └── NEIN → Lagerschaden.
│       │       ├── Lager austauschbar?
│       │       │   ├── JA → Lager tauschen. Ursache: Korrosion? Überlast?
│       │       │   └── NEIN → Block ersetzen.
│       └── Achse verbogen?
│           ├── JA → Block sofort ersetzen. KRITISCH.
│           └── NEIN → Achse reinigen, schmieren, testen.
```

### 8.2 Entscheidungsbaum: Block hebt sich vom Deck ab

```
Block hebt sich sichtbar vom Deck
├── Unter Last oder dauerhaft?
│   ├── Unter Last (geht zurück wenn entlastet)
│   │   ├── <1mm Bewegung
│   │   │   └── Akzeptabel wenn Bolzen korrekt angezogen. Nachziehen auf Drehmoment.
│   │   └── >1mm Bewegung
│   │       ├── Backing Plate vorhanden?
│   │       │   ├── JA → Backing Plate zu klein oder verformt. Größere Plate einbauen.
│   │       │   └── NEIN → SOFORT Backing Plate nachrüsten! KRITISCH.
│   │       └── Sandwich-Kern komprimiert?
│   │           ├── JA → Kern-Verstärkung erforderlich. Kernbereich mit Epoxid füllen.
│   │           └── NEIN → Bolzen prüfen (korrekte Größe? Drehmoment?).
│   └── Dauerhaft (auch ohne Last angehoben)
│       ├── Bolzen gelockert?
│       │   ├── JA → Bolzen auf Drehmoment nachziehen. Ursache: Vibration? 
│       │   │   → Sicherungsmutter (Nyloc) verwenden.
│       │   └── NEIN → Deck-Laminat beschädigt. Strukturelle Reparatur erforderlich.
│       └── Gelcoat-Risse sichtbar?
│           ├── JA → Deck unter Block inspizieren (von unten). 
│           │   Laminat-Reparatur + größere Backing Plate.
│           └── NEIN → Dichtstoff hat sich gelöst. Neu abdichten.
```

### 8.3 Entscheidungsbaum: Großschot-System trimmt schwer

```
Großschot lässt sich nur schwer trimmen
├── Problem bei allen Windstärken oder nur bei viel Wind?
│   ├── Alle Windstärken
│   │   ├── Rollen frei? (Einzeln prüfen, Seil raus)
│   │   │   ├── Alle frei → Seilführung prüfen. Knicke? Zu enge Radien?
│   │   │   └── Eine oder mehrere schwergängig → Lager-Problem.
│   │   │       → Schmieren oder Lager/Block tauschen.
│   │   └── Seil-Zustand prüfen
│   │       ├── Seil aufgeplustert/verdickt → Seil ersetzen
│   │       └── Seil OK → Schotweg prüfen. Zu viel Reibung in den Umlenkungen?
│   │           → Blöcke mit besseren Lagern nachrüsten.
│   └── Nur bei viel Wind
│       ├── Übersetzung ausreichend?
│       │   ├── NEIN → Höhere Übersetzung (6:1 statt 4:1) oder Winch-Assist
│       │   └── JA → System korrekt dimensioniert. 
│       │       Physikalische Grenze der Handkraft erreicht.
│       │       → Winch für Großschot verwenden.
│       └── Blöcke unter Last blockiert?
│           └── Mögliches Lagerproblem unter Extremlast. Premium-Lager einbauen.
```

### 8.4 Entscheidungsbaum: Seil-Mantel-Schaden am Block

```
Seil-Mantel zeigt Schäden an Block-Position
├── Art des Schadens?
│   ├── Schnittspuren (einseitig, scharf)
│   │   └── Grat an der Rollenkante. Block inspizieren, Grat entfernen.
│   │       Wenn Rille beschädigt: Rolle oder Block tauschen.
│   ├── Abrieb (rundherum, gleichmäßig)
│   │   ├── Seil zu dick für Rille?
│   │   │   ├── JA → Seil oder Block anpassen.
│   │   │   └── NEIN → Rolle dreht nicht frei. Lagerproblem → Seil gleitet über stehende Rolle.
│   │   └── Rille verschlissen → Rolle tauschen.
│   ├── Schmelzspuren (glänzend, verhärtet)
│   │   └── Thermische Überlastung. Siehe Fehlerbild F-HL-11.
│   │       → Rolle auf Verformung prüfen. Metall-Rolle nachrüsten.
│   └── Quetschspuren
│       └── Seil hat sich zwischen Rolle und Gehäuse eingeklemmt.
│           → Seilgröße prüfen. Anti-Chafe-Platte nachrüsten.
```

### 8.5 Entscheidungsbaum: Korrosion am Hochlast-Block

```
Korrosion am Hochlast-Block entdeckt
├── Material des Blocks?
│   ├── Aluminium
│   │   ├── Weiß-graue Flecken (Aluminium-Oxidation)
│   │   │   ├── Oberflächlich → Reinigen (Scotch-Brite), Schutz (Boeshield T-9)
│   │   │   └── Tiefe Pitting → Block-Festigkeit prüfen. Bei >0,5mm Tiefe: Ersetzen.
│   │   └── An Kontaktfläche mit Edelstahl-Bolzen?
│   │       └── Galvanische Korrosion. SOFORT:
│   │           1. Isolierbuchsen einbauen
│   │           2. Tef-Gel auftragen
│   │           3. Wenn Querschnitt reduziert: Block ersetzen.
│   ├── Edelstahl
│   │   ├── Braune Flecken (Tea Staining)
│   │   │   └── Meist oberflächlich. Citric Acid Passivation.
│   │   │       Wenn tiefe Pitting: Material prüfen — wirklich 316L oder nur 304?
│   │   └── Risse (Spannungsrisskorrosion)
│   │       └── KRITISCH. Block sofort ersetzen. 
│   │           Ursache: Falsches Material (304 statt 316L) oder extreme mechanische Spannung.
│   └── Carbon (CFK)
│       ├── Mattierung/Aufhellung
│       │   └── UV-Schaden. Lackieren mit UV-Klarlack.
│       └── Delamination sichtbar?
│           └── KRITISCH. Carbon-Block sofort ersetzen.
│               CFK-Delamination ist nicht reparabel.
```

---

## 9. FAQ — Häufige Fragen

### 9.1 Allgemeine Fragen

**F1: Was ist der Unterschied zwischen SWL, WLL und Bruchlast?**

- **SWL (Safe Working Load):** Die maximal zulässige Arbeitslast im regulären Betrieb. Berücksichtigt den Sicherheitsfaktor.
- **WLL (Working Load Limit):** Im Prinzip identisch mit SWL. WLL ist der modernere, in EU-Normen bevorzugte Begriff.
- **Bruchlast (Breaking Load/Strength):** Die Last, bei der der Block rechnerisch oder im Test versagt. Typisch 3× SWL.
- **MBL (Minimum Breaking Load):** Die garantierte Mindest-Bruchlast. Jeder Block muss diese überschreiten.

**Faustregel:** Bruchlast = 3 × SWL (bei 3:1 Sicherheitsfaktor)

**F2: Kann ich einen Aluminium-Block durch einen Edelstahl-Block ersetzen und umgekehrt?**

Ja, solange die Bruchlast gleich oder höher ist. Beachten:
- Edelstahl ist ca. 2× schwerer als Aluminium bei gleicher Bruchlast
- Bei Aluminium-Deck: galvanische Korrosion beachten (Isolierung erforderlich)
- Befestigungspunkte müssen passen oder angepasst werden

**F3: Wie oft müssen Hochlast-Blöcke inspiziert werden?**

| Nutzung | Intervall |
|---------|-----------|
| Fahrtensegler | Jährlich (vor Saisonbeginn) |
| Regatta (Club-Level) | Alle 6 Monate |
| Offshore-Regatta | Vor und nach jeder Regatta |
| Charter | Alle 3 Monate |
| Superyacht (MCA) | Halbjährlich, dokumentiert |

**F4: Welche Blöcke brauche ich für Dyneema/Spectra-Seile?**

Dyneema/Spectra-Seile haben spezielle Anforderungen an Blöcke:
- Rollendurchmesser: Min. 7× Seildurchmesser (Dyneema-Kern biegt steifer als Polyester)
- Rollenmaterial: Aluminium oder Torlon bevorzugt (Kunststoff-Rollen verschleißen schneller durch Dyneema)
- Rillenform: V-förmig oder flach (nicht tiefe U-Rille, da Dyneema weniger komprimierbar)
- Harken und Ronstan haben spezielle "High-Performance"-Rollen für Dyneema

**F5: Muss ich beim Seil-Upgrade auch die Blöcke tauschen?**

Wenn der neue Seildurchmesser anders ist als der alte: Ja, prüfen ob er noch in die Rollenrille passt. Wenn das neue Seil eine höhere Bruchlast hat und dadurch höhere Betriebslasten möglich werden: Block-Bruchlast ebenfalls prüfen.

### 9.2 Dimensionierung und Auswahl

**F6: Wie berechne ich die Hochlast-Block-Größe für meine Yacht?**

Schritt-für-Schritt:
1. Segelfläche und maximale Windstärke bestimmen → Segelkraft berechnen
2. Rigg-Geometrie analysieren → Schot-/Stag-Last ableiten
3. Umlenkwinkel am Block bestimmen → Block-Last berechnen
4. Dynamikfaktor anwenden (Böe, Halse)
5. Sicherheitsfaktor anwenden
6. Ergebnis = erforderliche Bruchlast
7. Block auswählen mit Bruchlast ≥ erforderliche Bruchlast

**F7: Mein Boot hat 12m. Welche Blockgröße für die Großschot?**

Typische Empfehlung für 12m Fahrtensegler:
- 6:1 Talje mit 57mm Blöcken (Dreifach oben, Doppel unten mit Becket)
- SWL-Anforderung: ca. 2.500–3.500 kg
- Empfohlene Bruchlast: 7.500–10.500 kg
- Seilgröße: 10–12mm Doppelgeflecht
- Beispiel: Harken Black Magic 57mm oder Ronstan Series 60

**F8: Ist ein teurerer Block wirklich besser?**

In vielen Fällen ja, aber der Vorteil ist kontextabhängig:
- **Gewichtsersparnis:** Bei Regatta relevant, bei Fahrtensegler kaum spürbar
- **Lager-Qualität:** Nadellager (teuer) vs. Gleitlager (günstig) → besserer Wirkungsgrad
- **Langlebigkeit:** Teure Blöcke halten oft 2–3× länger als Billig-Blöcke
- **Service:** Harken bietet lebenslangen Lager-Austausch auf einigen Serien
- **Budget-Tipp:** Garhauer Edelstahl-Blöcke bieten 80% der Leistung für 40% des Preises

**F9: Wann brauche ich Fiddle-Blöcke statt Doppel-Blöcke?**

- **Fiddle-Block:** Rollen übereinander (unterschiedliche Größe). Schmaler Einbau, gute Seilführung bei engen Platzverhältnissen. Bevorzugt wenn das Seil gerade ein- und ausläuft.
- **Doppel-Block:** Rollen nebeneinander (gleiche Größe). Breiter, aber flacher. Höhere Lastkapazität. Bevorzugt für Taljensysteme mit parallelen Seil-Parten.

**F10: Was sind "Open-Cage" Blöcke und wann brauche ich sie?**

Open-Cage (offener Käfig) bedeutet, dass das Seil seitlich in die Rolle eingelegt werden kann, ohne es durch den Block fädeln zu müssen. Vorteile:
- Schneller Seilwechsel
- Selbstreinigend (Wasser und Schmutz fließen ab)
- Geringeres Gewicht

Nachteile:
- Seil kann unter extremen Umständen aus dem Block springen
- Nicht für alle Hochlast-Anwendungen geeignet (Backstag, Runners: geschlossen bevorzugt)

### 9.3 Installation und Wartung

**F11: Kann ich Hochlast-Blöcke selbst montieren?**

Ja, wenn folgende Voraussetzungen erfüllt sind:
- Verständnis der Lastwirkung und Befestigungstechnik
- Richtiges Werkzeug (Bohrmaschine, Drehmomentschlüssel, Fräser für Kernverstärkung)
- Kenntnis des Deckaufbaus (Sandwich? Massiv-Laminat? Kern-Material?)
- Bereitschaft, die Arbeit von einem Fachmann prüfen zu lassen

Bei Lasten über 5.000 kg SWL wird professionelle Installation empfohlen.

**F12: Wie dichte ich Durchgangsbolzen korrekt ab?**

1. Bolzenloch 0,5mm größer als Bolzen bohren
2. Gelcoat-Kante leicht anfasen (1mm × 45°)
3. Sikaflex 291i oder 295 UV großzügig um den Bolzen und in die Bohrung auftragen
4. Bolzen einsetzen, Backing Plate aufsetzen
5. Drehmoment schrittweise anziehen (50%, 75%, 100%)
6. Austretenden Dichtstoff sauber abstreichen
7. 24h aushärten lassen vor Belastung

**F13: Welches Schmiermittel für Hochlast-Block-Lager?**

| Schmiermittel | Anwendung | Intervall |
|--------------|-----------|-----------|
| McLube Sailkote | Rollen, leichte Lager | Alle 50 Stunden |
| Harken OneDrop | Harken-Kugellagersysteme | Alle 100 Stunden |
| Lanocote (Lanolin) | Bolzen, Schäkel, Achsen | Saisonbeginn |
| Teflon-Spray (trocken) | Torlon-Buchsen | Alle 50 Stunden |
| Marine-Kugellagerfett | Kugellager bei Demontage | Alle 2 Jahre |

**F14: Wie erkenne ich, ob mein Block getauscht werden muss?**

Sofort-Tausch-Kriterien (eines reicht):
- Sichtbare Risse im Gehäuse, Achse oder Schäkel
- Achse verbogen (erkennbar an ungleichmäßigem Rollenlauf)
- Rolle dreht nicht mehr frei auch nach Reinigung und Schmierung
- Block hat sich unter Last verformt
- Bruchlast-Spezifikation passt nicht mehr zur Anwendung (Boot aufgerüstet)
- Aluminium-Block zeigt tiefe Korrosions-Pitting (>0,5mm)

**F15: Muss ich bei einem Rigg-Upgrade auch die Blöcke upgraden?**

Wenn eine der folgenden Änderungen vorgenommen wurde:
- Größeres Großsegel: Ja, Großschot-Blöcke prüfen
- Größere Genua oder Code 0: Ja, Genuaschot-Turning-Blocks prüfen
- Spinnaker/Gennaker nachgerüstet: Zusätzliche Turning Blocks erforderlich
- Stärkerer Mast: Running Backstay-Blöcke ggf. upgraden
- Neues Rigg (z.B. Upgrade auf Frachtional-Rigg): Gesamtes Block-System prüfen

### 9.4 Spezifische Systeme

**F16: Warum braucht der Baumniederholer (Vang) so viel Übersetzung?**

Der Vang arbeitet unter einem flachen Winkel (30–50° zum Baum). Durch den Sinus-Effekt muss die Vang-Kraft deutlich höher sein als die gewünschte Kraft auf den Baum:

```
F_vang = F_baum_unten / sin(winkel)
Bei 35°: F_vang = F_baum / 0,574 = 1,74 × F_baum
```

Zusätzlich muss die Vang gegen die Windkraft auf dem Großsegel arbeiten. Daher braucht ein 12m-Boot oft eine 8:1 oder sogar 16:1 Talje am Vang.

**F17: Was sind die Vorteile eines Rigid Vang gegenüber einer Talje?**

Rigid Vang (Gasdruckfeder + Teleskop-Strebe):
- Hält den Baum oben, auch ohne Großsegel (keine Baumstütze nötig)
- Weniger Seil im Cockpit
- Schneller zu bedienen
- Höherer Preis (€ 500–3.000)
- Schwerer als eine Talje

Talje-Vang:
- Günstiger (€ 100–500)
- Leichter
- Einfacher zu reparieren
- Baum fällt ohne Segel herunter (Baumstütze nötig)

**F18: Welche Turning Blocks für den Genuaschot?**

Die Genuaschot-Umlenkung ist eine klassische Hochlast-Anwendung:
- Umlenkwinkel: 90–150° (je nach Schotführung)
- Empfehlung: Stand-Up Spring Block auf Schiene
- Schiene: T-Schiene mit Gleiter, verschraubt auf verstärktem Deck
- Wichtig: Schienen-Stopper muss die volle Seitenlast aufnehmen können

**F19: Wie dimensioniere ich das Backstag-Trimmer-System?**

1. Backstag-Last aus Rigg-Berechnung (oder Faustformel: 0,5 × Vorstaglast)
2. Gewünschte Handkraft bestimmen (max. 30 kg für Handtrimmer, unbegrenzt mit Winch)
3. Übersetzung = Backstag-Last / Handkraft
4. Blöcke: Alle Blöcke im System müssen die Backstag-Last × 2 (Umlenkung 180°) als SWL haben
5. Befestigung: Chainplate mit 4:1 SF

**F20: Brauche ich spezielle Blöcke für Rollreff-Leinen?**

Rollreff-Leinen (Furling Lines) haben besondere Anforderungen:
- Die Last steigt beim Reffen unter Wind stark an (Segel unter Druck einrollen)
- Block muss unter Last frei drehen (kein Blockieren!)
- Seil darf nicht in der Rille klemmen
- Empfehlung: Blöcke mit Nadellager, selbstreinigend (Open Cage)
- Größe: Mindestens eine Klasse über der "normalen" Lastberechnung, da Schock-Lasten beim Reffen hoch sind

### 9.5 Problemlösung

**F21: Mein Großschot-Block quietscht. Was tun?**

Quietschen deutet auf Reibung im Lager oder zwischen Rolle und Gehäuse hin:
1. Block reinigen (Süßwasser-Spülung)
2. Rolle prüfen: Dreht sie frei?
3. Lager schmieren (McLube Sailkote oder Harken OneDrop)
4. Wenn Quietschen bleibt: Rolle ausbauen, Lager inspizieren
5. Wenn Lager beschädigt: Lager tauschen oder Block ersetzen

**F22: Mein Block hat nach einer Saison bereits Rost. Ist das normal?**

Abhängig vom Material:
- **Edelstahl 316L:** Leichtes "Tea Staining" in Küstennähe ist normal und oberflächlich. Mit Citric-Acid-Passivierung behandeln. Wenn echter Rost: Vermutlich 304 statt 316L → Reklamation.
- **Aluminium:** Kein Rost möglich. Weiße Korrosion ist Aluminium-Oxidation → galvanische Korrosion prüfen.
- **Carbon:** Kein Rost möglich. Braune Flecken sind Kontakt-Korrosion mit Stahlteilen → Isolation prüfen.

**F23: Kann ich gebrauchte Hochlast-Blöcke kaufen und einsetzen?**

Grundsätzlich möglich, aber mit Risiken:
- Vorgeschichte unbekannt (Überlast-Ereignisse, Ermüdung)
- Lagerverschleiß nicht von außen erkennbar
- Interne Risse nicht sichtbar
- Empfehlung: Nur von bekannter Quelle, mit dokumentierter Nutzung
- Sicherheitsfaktor erhöhen (4:1 statt 3:1)
- Für sicherheitskritische Anwendungen (Runners, Backstag): Nur neue Blöcke

**F24: Welche Block-Marke für Langfahrt?**

Für Blauwasser und Langfahrt sind folgende Kriterien entscheidend:
- **Ersatzteil-Verfügbarkeit weltweit:** Harken (beste globale Verfügbarkeit), Lewmar (gut in Europa und USA)
- **Korrosionsbeständigkeit:** Edelstahl-Blöcke (Garhauer) oder marine-grade Aluminium
- **Wartbarkeit:** Austauschbare Lager und Rollen bevorzugt
- **Robustheit:** Lieber eine Klasse größer dimensionieren

**Empfehlung Langfahrt:** Harken Black Magic (Aluminium, gute Lager, weltweit Ersatzteile) oder Garhauer (Edelstahl, nahezu unzerstörbar, günstig)

**F25: Wie lagere ich Hochlast-Blöcke im Winter?**

1. Gründlich mit Süßwasser spülen
2. Trocknen lassen (nicht mit Heißluft!)
3. Lager leicht schmieren (McLube oder Harken OneDrop)
4. Achsen und Bolzen mit Lanolin (Lanocote) behandeln
5. An trockenem, frostfreien Ort lagern
6. Nicht in Plastiktüte einpacken (Kondenswasser!)
7. Schäkel lösen und separat lagern (verhindert galvanische Korrosion)

---

## 10. Glossar

### Marine-spezifische Begriffe

| Begriff (DE) | Begriff (EN) | Definition |
|-------------|-------------|-----------|
| Achterliektrimmer | Leech line | Leine zum Einstellen der Achterliek-Spannung des Segels |
| Augbolzen | Eye bolt / Pad eye | Befestigungspunkt mit Auge auf dem Deck |
| Backstag | Backstay | Stehendes Gut vom Masttop zum Heck |
| Baumniederholer | Vang / Kicker | System zum Herunterziehen des Großbaums |
| Becket | Becket | Befestigungsauge am Block für das stehende Part |
| Bruchlast | Breaking load / Breaking strength | Last bei der ein Bauteil versagt |
| Chainplate | Chainplate | Metallbeschlag zur Einleitung von Rigg-Kräften in den Rumpf |
| Cheek Block | Cheek block | Seitlich montierter Umlenkblock |
| Cockpit-Organizer | Cockpit organizer | Mehrfach-Umlenkung am Cockpit-Eingang |
| Doppelblock | Double block | Block mit zwei Rollen |
| Dreifachblock | Triple block | Block mit drei Rollen |
| Deck-Organizer | Deck organizer | Mehrfach-Umlenkplatte auf dem Deck |
| Dreifaltigkeitsblock | Fiddle block | Zwei Rollen übereinander, unterschiedliche Größe |
| Durchgangsbolzen | Through-bolt | Bolzen der durch das gesamte Deck geht |
| Einlaminiert | Laminated-in | In das GFK-Laminat eingebettet |
| Einzelblock | Single block | Block mit einer Rolle |
| Ermüdung | Fatigue | Materialschwächung durch zyklische Belastung |
| Fall | Halyard | Leine zum Setzen eines Segels |
| Fieren | To ease / To pay out | Kontrolliertes Nachlassen einer Leine |
| Fiddle Block | Fiddle block | Block mit gestaffelten Rollen (oben größer) |
| Flaschenzug | Purchase / Tackle | Mechanisches System zur Kraftverstärkung mit Blöcken und Seil |
| Flush-Mount | Flush mount | Bündig in die Oberfläche eingelassene Montage |
| Galvanische Korrosion | Galvanic corrosion | Elektrochemische Korrosion zwischen ungleichen Metallen |
| Genuaschot | Genoa sheet | Schot zum Trimmen der Genua-Vorsegel |
| Großschot | Mainsheet | Schot zum Trimmen des Großsegels |
| Halse | Gybe / Jibe | Kurswechsel mit dem Heck durch den Wind |
| Kernverstärkung | Core reinforcement | Verstärkung des Sandwich-Kerns unter Beschlägen |
| Klemme | Cam cleat | Klemmvorrichtung zum Festsetzen einer Leine |
| Laufendes Gut | Running rigging | Alle beweglichen Leinen und Seile am Rigg |
| Mastfuß | Mast base / Mast step | Befestigungspunkt des Mastes auf dem Deck oder Kiel |
| Nadellager | Needle bearing | Zylindrisches Wälzlager mit zylindrischen Rollen |
| Pütting | Chainplate / Tang | Metallbeschlag für die Wantenanbindung |
| Rolle / Scheibe | Sheave | Die drehbare Komponente im Block |
| Rollenrille | Sheave groove | Vertiefung in der Rolle, in der das Seil läuft |
| Running Backstay | Running backstay / Runner | Paarweise wechselseitig gesetzte Achterstagen |
| Schäkel | Shackle | U-förmiger Verbinder mit Bolzen |
| Schot | Sheet | Leine zum Trimmen eines Segels |
| Schothorn | Clew | Untere hintere Ecke eines Segels |
| Sicherheitsfaktor | Safety factor | Verhältnis Bruchlast zu Arbeitslast |
| Spinnaker | Spinnaker | Leichtes Vorsegel für Vorwind-Kurse |
| Stand-Up Block | Stand-up block | Aufrecht stehendes Block-Design für Deck-Montage |
| Stehende Part | Standing part | Das feste Ende in einem Taljensystem |
| Talje | Purchase / Tackle | Flaschenzug-System mit Blöcken |
| Traveller | Traveller | Schiene mit fahrbarem Wagen für die Großschot-Umlenkung |
| Turning Block | Turning block | Deck-montierter Umlenkblock |
| Übersetzung | Purchase ratio / Mechanical advantage | Kraftverstärkungsverhältnis einer Talje |
| Umlenkrolle | Sheave / Fairlead | Rolle zur Richtungsänderung eines Seils |
| Umlenkwinkel | Deflection angle | Winkel um den ein Seil am Block umgelenkt wird |
| Verstärkungsplatte | Backing plate | Platte zur Lastverteilung unter dem Deck |
| Vorstaglast | Forestay load | Zugkraft im Vorstag |
| Wende | Tack | Kurswechsel mit dem Bug durch den Wind |
| Wirbel | Swivel | Drehbares Gelenk am Blockkopf |
| Wirkungsgrad | Efficiency | Verhältnis Nutzarbeit zu aufgewendeter Arbeit |

---

## 11. Schnell-Referenz

### 11.1 Hochlast-Block Auswahl — Kurzanleitung

```
Schritt 1: Betriebslast bestimmen
  → Segel-Kraft × Rigg-Geometrie-Faktor = Schot-/Stag-Last

Schritt 2: Block-Last berechnen
  → Block-Last = 2 × Seil-Spannung × sin(Umlenkwinkel / 2)

Schritt 3: Dynamik anwenden
  → Design-Last = Block-Last × Dynamikfaktor (1,5–5,0)

Schritt 4: Sicherheitsfaktor anwenden
  → Erforderliche Bruchlast = Design-Last × SF (3:1 bis 5:1)

Schritt 5: Block auswählen
  → Bruchlast ≥ Erforderliche Bruchlast
  → Seildurchmesser ≤ Max. Seildurchmesser
  → Rollendurchmesser ≥ 6× Seildurchmesser
```

### 11.2 Schnell-Referenz: Block-Größe nach Bootsgröße

| Bootsgröße | Großschot | Vang | Backstag | Genuaschot | Organizer |
|-----------|-----------|------|----------|------------|-----------|
| 8–10m | 57mm, 4:1 | 40mm, 4:1 | — | 40mm | 3×40mm |
| 10–12m | 57mm, 6:1 | 57mm, 6:1 | 57mm | 57mm | 4×50mm |
| 12–14m | 75mm, 6:1 | 57mm, 8:1 | 75mm | 57mm | 5×57mm |
| 14–18m | 75mm, 8:1 | 75mm, 8:1 | 75–100mm | 75mm | 5×57mm |
| 18–22m | 100mm, 8:1 | 75mm, 16:1 | 100mm | 75mm | 6×75mm |
| 22m+ | 100mm+, 12:1 | Hydraulisch | Custom | 100mm | Custom |

### 11.3 Schnell-Referenz: Bolzen und Backing Plates

| Block-SWL | Bolzen | Backing Plate | Kernverstärkung |
|-----------|--------|--------------|----------------|
| <1.500 kg | M8, A4-80 | 80×80×3 mm SS | Empfohlen |
| 1.500–3.000 kg | M10, A4-80 | 100×100×4 mm SS | Erforderlich |
| 3.000–5.000 kg | M10, A4-80 | 120×120×5 mm SS | Erforderlich |
| 5.000–8.000 kg | M12, A4-80 | 150×150×6 mm SS | Erforderlich |
| >8.000 kg | M12–M16 | 180×180×8 mm+ | Erforderlich + Stringer |

### 11.4 Checkliste: Jährliche Inspektion Hochlast-Blöcke

```
□ Rollen drehen frei? (Jede Rolle einzeln prüfen)
□ Achse gerade? (Sichtprüfung, Schieblehre)
□ Gehäuse rissfrei? (Lupe, besonders an Bohrungen)
□ Schäkel intakt? (Bolzen stramm, keine Verformung)
□ Befestigung fest? (Drehmoment-Kontrolle)
□ Kein Spiel zwischen Block und Deck?
□ Gelcoat um Befestigung rissfrei?
□ Backing Plate intakt? (von unten prüfen)
□ Keine Korrosion an Kontaktflächen?
□ Seilrille verschlissen? (Tiefe messen)
□ Seil-Zustand am Block-Kontakt?
□ Schmierung ausreichend?
```

---

## ANHANG A — Fallstudien

### Fallstudie A1: Backstag-Block-Versagen, Swan 48

**Boot:** Nautor Swan 48, Baujahr 1998, Backstag-Trimmer mit 4:1 Talje
**Situation:** Herbstregatta, 25–30 Knoten Wind, Kreuz, harte See
**Versagen:** Der untere Backstag-Block (Harken 75mm, 15 Jahre alt) versagte durch Achsbruch. Das Backstag ging sofort lose, der Mast begann unkontrolliert zu pumpen.
**Ursache:** Ermüdungsbruch der 17-4 PH Achse nach geschätzt 50.000+ Lastzyklen. Der Block hatte nie ein Lager-Service erhalten. Die Achse zeigte bei der Nachuntersuchung fortgeschrittene Ermüdungsrisse.
**Konsequenz:** Rigg-Totalverlust konnte durch sofortiges Abfallen und Setzen des Running Backstays verhindert werden. Block-Paar ersetzt, gesamtes Backstag-System auf 100mm Blöcke aufgerüstet.
**Lehre:** Hochlast-Blöcke in kritischen Anwendungen haben eine definierte Lebensdauer. Sichtprüfung allein ist unzureichend — Ermüdungsrisse sind oft nicht sichtbar.

### Fallstudie A2: Turning-Block Ausriss, Bavaria 40 Cruiser

**Boot:** Bavaria 40 Cruiser, Baujahr 2005, Genuaschot-Turning-Block
**Situation:** 20 Knoten Wind, volle Genua, Wende
**Versagen:** Der Turning Block (Ronstan 57mm) riss mitsamt den Schrauben aus dem Deck. Genua schlug unkontrolliert.
**Ursache:** Der Turning Block war nur mit vier selbstschneidenden Schrauben montiert — ohne Durchgangsbolzen, ohne Backing Plate, ohne Kernverstärkung. Typischer Werft-Fehler bei Serienproduktion. Die Ausziehkraft bei 150°-Umlenkung und 2.000 kg Schotkraft betrug ~3.900 kg — weit über der Tragfähigkeit der Schraubbefestigung.
**Konsequenz:** Alle Turning Blocks auf Durchgangsbolzen mit Backing Plates umgerüstet. Gesamtkosten: € 450 (Material) + 8h Arbeit.
**Lehre:** Hochlast-Blöcke niemals mit Schrauben befestigen. Durchgangsbolzen mit Backing Plate sind für jede Hochlast-Anwendung zwingend erforderlich.

### Fallstudie A3: Großschot-Talje Ineffizienz, Hallberg-Rassy 37

**Boot:** Hallberg-Rassy 37, Baujahr 2002, 6:1 Großschot-Talje
**Problem:** Crew konnte die Großschot bei 18+ Knoten nicht mehr per Hand dichtholen. Das Boot segelte mit permanent zu losem Großsegel.
**Diagnose:** Wirkungsgrad-Messung zeigte, dass die 6:1 Talje nur noch einen effektiven mechanischen Vorteil von 2,8:1 bot.
**Ursache:** Alle sechs Rollen hatten Gleitlager (Delrin), die nach 12 Jahren Fahrtensegelei (geschätzt 8.000 Zyklen) einen Wirkungsgrad von nur noch η = 0,82 pro Rolle hatten. Gesamt: 0,82^6 = 0,30 (30%).
**Lösung:** Alle Blöcke durch Harken Black Magic 57mm mit Nadellagern ersetzt. Neuer Wirkungsgrad: 0,97^6 = 0,83 (83%). Effektiver mechanischer Vorteil: 4,98:1. Crew kann Großschot jetzt bis 25 Knoten von Hand dichtholen.
**Kosten:** € 1.200 für sechs Blöcke. Amortisation: sofort (keine Winch-Nachrüstung für € 3.500 nötig).

### Fallstudie A4: Thermische Überlastung, TP52 Regatta

**Boot:** TP52 Regatta-Yacht, Spinnaker-Barber-Hauler
**Situation:** Langstrecken-Regatta, 8h Downwind, Spinnaker unter ständigem Trimm
**Versagen:** Die Acetal-Rolle des Barber-Hauler-Blocks erweichte und verformte sich oval. Der Spinnaker-Barber-Hauler blockierte.
**Ursache:** Reibungsleistung P = 15.000 N × 0,3 m/s × 0,05 = 225 W über 8 Stunden. Die Dauertemperatur an der Acetal-Rolle überstieg 100°C (Erweichungspunkt ~120°C, aber dauerhaft 100°C+ reduziert die Festigkeit um 50%).
**Lösung:** Alle Barber-Hauler-Blöcke auf Torlon-Rollen (Erweichungspunkt 285°C) umgerüstet.
**Lehre:** Bei dauerhafter Hochlast-Beanspruchung mit Seilbewegung: Torlon oder Metall-Rollen statt Acetal/Delrin.

### Fallstudie A5: Galvanische Korrosion, Amel 54

**Boot:** Amel 54, Langfahrt-Yacht, 3 Jahre Tropen-Einsatz
**Problem:** Aluminium-Blöcke am Mastfuß zeigten schwere Korrosion. Blöcke saßen fest und ließen sich nicht mehr lösen.
**Ursache:** Aluminium-Block (6061-T6) direkt auf Edelstahl-Augbolzen montiert, ohne Isolierbuchsen, im tropischen Salzwasser-Klima. Galvanisches Potential: 0,5–0,8 V → aggressive Korrosion des Aluminium-Anodikums.
**Konsequenz:** Alle Mastfuß-Blöcke erneuert (€ 2.800). Edelstahl-Augbolzen ersetzt. Nylon-Isolierbuchsen eingebaut. Tef-Gel an allen Kontaktflächen aufgetragen.
**Lehre:** In tropischen Klimazonen ist galvanische Isolation zwischen ungleichen Metallen überlebenswichtig für die Beschläge.

### Fallstudie A6: Deck-Organizer Fehlinstallation, Beneteau Oceanis 46.1

**Boot:** Beneteau Oceanis 46.1, Baujahr 2019
**Problem:** Fallen und Strecker ließen sich nur schwer trimmen. Drei von fünf Rollen des Deck-Organizers liefen unter Zwang.
**Ursache:** Der Deck-Organizer war 15° verdreht zum optimalen Seilwinkel montiert. Die Seile kamen unter einem Winkel an, der seitliche Kräfte auf die Rollen erzeugte. Zusätzlich war die Montagefläche nicht plan — eine Ecke stand 3mm hoch.
**Lösung:** Organizer demontiert, Montagefläche plangeschliffen, korrekt ausgerichtet neu montiert. Seilführung überprüft und optimiert.
**Kosten:** € 150 (Arbeit, 4h Werft). € 0 Material.
**Lehre:** Deck-Organizer-Installation erfordert sorgfältige Ausrichtung auf den Seilwinkel. Trockenmontage (ohne Dichtstoff) und Funktionsprüfung vor dem endgültigen Einbau.

### Fallstudie A7: Running-Backstay Systemdesign, IRC 40-Fuß Racer

**Boot:** Custom IRC 40-Fuß Regattayacht
**Problem:** Neubau-Systemdesign. Running Backstay Lasten: 6.000 kg pro Seite.
**Lösung:**
- Block: Harken Black Magic 100mm (Bruchlast 18.000 kg)
- Schäkel: Wichard HR Titanium (Bruchlast 22.000 kg)
- Chainplate: 17-4 PH Edelstahl, 60×10mm (Querschnitt 600mm², Tragfähigkeit 642.000 N / 65.500 kg bei SF 4)
- Seil: Dyneema SK78, 14mm (Bruchlast 15.000 kg)
- Talje: 8:1 Kaskade für Handtrimm
- Befestigung: Einlaminierte Lastplatte mit GFK-Verstärkung
**Ergebnis:** System funktioniert seit 4 Saisons einwandfrei. Inspektionen alle 6 Monate, bisher keine Befunde.

### Fallstudie A8: Budget-Refit Großschot, Jeanneau Sun Odyssey 36i

**Boot:** Jeanneau Sun Odyssey 36i, Baujahr 2008
**Problem:** Großschot-System (Original Lewmar Synchro 50mm, 4:1) verschlissen. Rollen schwergängig, Schäkel verbogen.
**Budget:** Max. € 600 für das gesamte System.
**Lösung:** Garhauer Marine Edelstahl-System:
- 1× Doppelblock 60mm mit Becket (60-05-OT): € 155
- 1× Einzelblock 60mm mit Schäkel (60-01-OT): € 85
- 1× Traveller-Wagen mit Blöcken: € 220
- Seil 12mm Double-Braid, 15m: € 75
- Schäkel und Kleinteile: € 45
- Gesamt: € 580
**Ergebnis:** 4:1 System mit 5.400 kg Bruchlast an den Hauptblöcken. Funktioniert seit 3 Saisons problemlos. Gewicht 30% höher als das Original, aber optisch ansprechend (polierter Edelstahl).

---

## ANHANG B — AYDI-Integration (Pydantic-Modelle)

### B.1 Block-Datenmodell

```python
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class BlockType(str, Enum):
    SINGLE = "single"
    DOUBLE = "double"
    TRIPLE = "triple"
    FIDDLE = "fiddle"
    STAND_UP = "stand_up"
    CHEEK = "cheek"
    TURNING = "turning"
    ORGANIZER = "organizer"


class BearingType(str, Enum):
    BALL_BEARING = "ball_bearing"
    NEEDLE_BEARING = "needle_bearing"
    TORLON_BUSHING = "torlon_bushing"
    UHMWPE_BUSHING = "uhmwpe_bushing"
    DELRIN_BUSHING = "delrin_bushing"
    CERAMIC_BEARING = "ceramic_bearing"
    PLAIN_BUSHING = "plain_bushing"


class BlockMaterial(str, Enum):
    ALUMINUM_6061 = "aluminum_6061_t6"
    ALUMINUM_7075 = "aluminum_7075_t6"
    STAINLESS_316L = "stainless_316l"
    STAINLESS_17_4PH = "stainless_17_4ph"
    TITANIUM_GR5 = "titanium_grade_5"
    CARBON_COMPOSITE = "carbon_composite"
    GLASS_FIBER_NYLON = "glass_fiber_nylon"


class MountingType(str, Enum):
    SHACKLE = "shackle"
    SWIVEL = "swivel"
    BECKET = "becket"
    CLEVIS = "clevis"
    STAND_UP_SPRING = "stand_up_spring"
    PAD_EYE = "pad_eye"
    THROUGH_BOLT = "through_bolt"
    U_BRACKET = "u_bracket"
    SLIDE = "slide"
    FLUSH_MOUNT = "flush_mount"
    CHEEK_MOUNT = "cheek_mount"


class HighLoadBlockSpec(BaseModel):
    """Specification for a high-load block in yacht rigging."""
    
    model_config = {"from_attributes": True}
    
    manufacturer: str = Field(..., description="Block manufacturer name")
    part_number: str = Field(..., description="Manufacturer part number")
    block_type: BlockType = Field(..., description="Type classification")
    sheave_diameter_mm: float = Field(..., ge=20, le=200, description="Sheave diameter in mm")
    max_line_diameter_mm: float = Field(..., ge=4, le=30, description="Maximum line diameter in mm")
    swl_kg: float = Field(..., ge=100, description="Safe Working Load in kg")
    breaking_load_kg: float = Field(..., ge=300, description="Breaking load in kg")
    weight_g: float = Field(..., ge=10, description="Weight in grams")
    bearing_type: BearingType = Field(..., description="Type of bearing")
    housing_material: BlockMaterial = Field(..., description="Housing/side plate material")
    sheave_material: str = Field(..., description="Sheave material description")
    mounting_type: MountingType = Field(..., description="Mounting configuration")
    num_sheaves: int = Field(1, ge=1, le=8, description="Number of sheaves")
    has_becket: bool = Field(False, description="Whether block has a becket")
    has_cam_cleat: bool = Field(False, description="Whether block has integrated cam cleat")
    efficiency_percent: float = Field(
        ..., ge=50, le=100, description="Bearing efficiency in percent"
    )
    suitable_for_dyneema: bool = Field(
        False, description="Whether sheave is suitable for Dyneema/Spectra lines"
    )
    price_eur: Optional[float] = Field(None, ge=0, description="Approximate price in EUR")
    
    @property
    def safety_factor(self) -> float:
        """Calculate the safety factor (breaking load / SWL)."""
        return self.breaking_load_kg / self.swl_kg


class BackingPlateSpec(BaseModel):
    """Specification for a backing plate under a high-load fitting."""
    
    model_config = {"from_attributes": True}
    
    width_mm: float = Field(..., ge=40, le=500, description="Width in mm")
    height_mm: float = Field(..., ge=40, le=500, description="Height in mm")
    thickness_mm: float = Field(..., ge=2, le=20, description="Thickness in mm")
    material: str = Field(..., description="Material designation")
    bolt_pattern: str = Field(
        ..., description="Bolt pattern description (e.g., '4x M10')"
    )
    max_load_kg: float = Field(..., ge=500, description="Maximum design load in kg")
    requires_core_reinforcement: bool = Field(
        True, description="Whether sandwich core reinforcement is required"
    )


class TackleSystemSpec(BaseModel):
    """Specification for a complete tackle (purchase) system."""
    
    model_config = {"from_attributes": True}
    
    application: str = Field(
        ..., description="System application (e.g., 'mainsheet', 'vang', 'backstay')"
    )
    purchase_ratio: str = Field(
        ..., description="Mechanical advantage ratio (e.g., '6:1')"
    )
    upper_block: HighLoadBlockSpec = Field(
        ..., description="Upper (head) block specification"
    )
    lower_block: HighLoadBlockSpec = Field(
        ..., description="Lower (tail/becket) block specification"
    )
    line_diameter_mm: float = Field(..., ge=4, le=24, description="Line diameter in mm")
    line_material: str = Field(
        ..., description="Line material (e.g., 'Polyester double braid')"
    )
    line_length_m: float = Field(
        ..., ge=1, le=100, description="Required line length in meters"
    )
    max_working_load_kg: float = Field(
        ..., ge=100, description="Maximum working load on the system"
    )
    effective_purchase: float = Field(
        ..., ge=1, le=20, description="Effective purchase ratio after friction losses"
    )
    total_weight_g: float = Field(
        ..., ge=50, description="Total system weight in grams"
    )
    boat_size_range_m: str = Field(
        ..., description="Suitable boat size range (e.g., '10-14m')"
    )
    estimated_price_eur: Optional[float] = Field(
        None, ge=0, description="Estimated total system price in EUR"
    )
```

### B.2 Inspektions-Datenmodell

```python
from datetime import date
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class InspectionSeverity(str, Enum):
    OK = "ok"
    MONITOR = "monitor"
    SERVICE_REQUIRED = "service_required"
    REPLACE_SOON = "replace_soon"
    REPLACE_IMMEDIATELY = "replace_immediately"
    CRITICAL_DO_NOT_USE = "critical_do_not_use"


class HighLoadBlockCondition(str, Enum):
    NEW = "new"
    GOOD = "good"
    FAIR = "fair"
    WORN = "worn"
    DAMAGED = "damaged"
    FAILED = "failed"


class ConfidenceLevel(str, Enum):
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    DOCUMENTED = "documented"


class HighLoadBlockInspection(BaseModel):
    """Inspection result for a high-load block."""
    
    model_config = {"from_attributes": True}
    
    inspection_date: date = Field(..., description="Date of inspection")
    inspector: str = Field(..., description="Inspector name or ID")
    block_location: str = Field(
        ..., description="Location on the yacht (e.g., 'mainsheet_upper')"
    )
    block_manufacturer: str = Field(..., description="Block manufacturer")
    block_part_number: str = Field(..., description="Block part number")
    block_age_years: Optional[float] = Field(
        None, ge=0, description="Estimated age in years"
    )
    
    # Roller/Sheave condition
    sheave_rotation_free: bool = Field(
        ..., description="Whether sheave rotates freely by hand"
    )
    sheave_groove_wear_mm: Optional[float] = Field(
        None, ge=0, description="Measured groove wear in mm"
    )
    sheave_condition: HighLoadBlockCondition = Field(
        ..., description="Overall sheave condition"
    )
    
    # Bearing condition
    bearing_noise: bool = Field(
        False, description="Whether bearing makes noise (grinding, clicking)"
    )
    bearing_play_mm: Optional[float] = Field(
        None, ge=0, description="Measured bearing play in mm"
    )
    bearing_condition: HighLoadBlockCondition = Field(
        ..., description="Overall bearing condition"
    )
    
    # Housing/structure condition
    housing_cracks: bool = Field(
        False, description="Whether housing shows visible cracks"
    )
    housing_corrosion: bool = Field(
        False, description="Whether housing shows corrosion"
    )
    housing_condition: HighLoadBlockCondition = Field(
        ..., description="Overall housing condition"
    )
    
    # Axis condition
    axis_straight: bool = Field(
        True, description="Whether axis is straight (not bent)"
    )
    axis_wear_mm: Optional[float] = Field(
        None, ge=0, description="Measured axis wear in mm"
    )
    axis_condition: HighLoadBlockCondition = Field(
        ..., description="Overall axis condition"
    )
    
    # Mounting condition
    mounting_secure: bool = Field(
        True, description="Whether mounting is secure (no movement)"
    )
    mounting_corrosion: bool = Field(
        False, description="Whether mounting shows corrosion"
    )
    gelcoat_cracks_around_mounting: bool = Field(
        False, description="Whether gelcoat around mounting shows cracks"
    )
    backing_plate_present: bool = Field(
        True, description="Whether backing plate is present"
    )
    backing_plate_condition: Optional[HighLoadBlockCondition] = Field(
        None, description="Backing plate condition if accessible"
    )
    
    # Overall assessment
    overall_severity: InspectionSeverity = Field(
        ..., description="Overall inspection severity rating"
    )
    confidence: ConfidenceLevel = Field(
        ..., description="Confidence level of the inspection"
    )
    findings: list[str] = Field(
        default_factory=list, description="List of inspection findings"
    )
    recommendations: list[str] = Field(
        default_factory=list, description="List of recommendations"
    )
    next_inspection_date: Optional[date] = Field(
        None, description="Recommended next inspection date"
    )
    photos: list[str] = Field(
        default_factory=list, description="List of photo file references"
    )
```

### B.3 Lastberechnungs-Modell

```python
import math
from typing import Optional
from pydantic import BaseModel, Field


class LoadCalculationInput(BaseModel):
    """Input parameters for high-load block load calculation."""
    
    model_config = {"from_attributes": True}
    
    application: str = Field(..., description="Application type")
    line_tension_kg: float = Field(
        ..., ge=0, description="Line tension in kg (one side)"
    )
    deflection_angle_deg: float = Field(
        ..., ge=0, le=180, description="Deflection angle in degrees"
    )
    dynamic_factor: float = Field(
        1.5, ge=1.0, le=5.0, description="Dynamic load factor"
    )
    safety_factor: float = Field(
        3.0, ge=2.0, le=6.0, description="Required safety factor"
    )
    degradation_factor: float = Field(
        1.0, ge=0.1, le=1.0,
        description="Degradation factor for aged equipment (1.0 = new)"
    )


class LoadCalculationResult(BaseModel):
    """Result of a high-load block load calculation."""
    
    model_config = {"from_attributes": True}
    
    static_block_load_kg: float = Field(
        ..., description="Static load on block in kg"
    )
    dynamic_block_load_kg: float = Field(
        ..., description="Dynamic load on block in kg"
    )
    required_breaking_load_kg: float = Field(
        ..., description="Required minimum breaking load in kg"
    )
    required_swl_kg: float = Field(
        ..., description="Required minimum SWL in kg"
    )
    recommended_block_class_mm: int = Field(
        ..., description="Recommended sheave diameter class in mm"
    )
    confidence: str = Field(
        "calculated", description="Confidence level of the result"
    )
    notes: list[str] = Field(
        default_factory=list, description="Calculation notes and warnings"
    )


def calculate_block_load(input_data: LoadCalculationInput) -> LoadCalculationResult:
    """Calculate the required block specifications for a high-load application."""
    
    # Static block load
    angle_rad = math.radians(input_data.deflection_angle_deg / 2)
    static_load = 2 * input_data.line_tension_kg * math.sin(angle_rad)
    
    # Dynamic block load
    dynamic_load = static_load * input_data.dynamic_factor
    
    # Required breaking load (accounting for degradation)
    required_breaking = (
        dynamic_load * input_data.safety_factor / input_data.degradation_factor
    )
    
    # Required SWL
    required_swl = dynamic_load / input_data.degradation_factor
    
    # Determine recommended block class
    if required_breaking <= 5000:
        block_class = 40
    elif required_breaking <= 8000:
        block_class = 57
    elif required_breaking <= 15000:
        block_class = 75
    elif required_breaking <= 25000:
        block_class = 100
    else:
        block_class = 120  # Custom / special
    
    notes = []
    if input_data.deflection_angle_deg >= 170:
        notes.append(
            "Umlenkwinkel nahe 180°: Block-Last entspricht nahezu "
            "der doppelten Seilspannung. Besondere Beachtung der "
            "Deck-Befestigung erforderlich."
        )
    if input_data.dynamic_factor >= 3.0:
        notes.append(
            "Hoher Dynamikfaktor: Schock-Last-Szenario. "
            "Empfehlung: Geschmiedete Edelstahl- oder Titan-Achse."
        )
    if required_breaking > 20000:
        notes.append(
            "Extrem hohe Bruchlast-Anforderung. "
            "Custom-Block oder Spezial-Lösung erforderlich."
        )
    if input_data.degradation_factor < 0.7:
        notes.append(
            "Starke Degradation berücksichtigt. "
            "Austausch des Blocks wird empfohlen statt Weiterbetrieb."
        )
    
    return LoadCalculationResult(
        static_block_load_kg=round(static_load, 1),
        dynamic_block_load_kg=round(dynamic_load, 1),
        required_breaking_load_kg=round(required_breaking, 1),
        required_swl_kg=round(required_swl, 1),
        recommended_block_class_mm=block_class,
        confidence="calculated",
        notes=notes,
    )
```

### B.4 Effizienz-Berechnungsmodell

```python
import math
from pydantic import BaseModel, Field


class TackleEfficiencyInput(BaseModel):
    """Input for tackle system efficiency calculation."""
    
    model_config = {"from_attributes": True}
    
    num_sheaves: int = Field(
        ..., ge=1, le=12, description="Total number of sheaves in the system"
    )
    bearing_efficiency: float = Field(
        0.97, ge=0.70, le=0.99,
        description="Single sheave bearing efficiency (0-1)"
    )
    purchase_ratio: int = Field(
        ..., ge=1, le=16, description="Nominal purchase ratio"
    )
    load_kg: float = Field(
        ..., ge=0, description="Load to be overcome in kg"
    )


class TackleEfficiencyResult(BaseModel):
    """Result of a tackle efficiency calculation."""
    
    model_config = {"from_attributes": True}
    
    total_efficiency: float = Field(
        ..., description="Total system efficiency (0-1)"
    )
    effective_purchase: float = Field(
        ..., description="Effective purchase ratio after friction"
    )
    required_input_force_kg: float = Field(
        ..., description="Required input force in kg"
    )
    friction_loss_percent: float = Field(
        ..., description="Total friction loss in percent"
    )
    recommendation: str = Field(
        ..., description="System assessment and recommendation"
    )


def calculate_tackle_efficiency(
    input_data: TackleEfficiencyInput,
) -> TackleEfficiencyResult:
    """Calculate the efficiency of a tackle system."""
    
    total_eff = input_data.bearing_efficiency ** input_data.num_sheaves
    effective_purchase = input_data.purchase_ratio * total_eff
    required_force = input_data.load_kg / effective_purchase
    friction_loss = (1 - total_eff) * 100
    
    if total_eff >= 0.80:
        recommendation = (
            "System-Effizienz gut. Aktuelle Lager-Konfiguration ist angemessen."
        )
    elif total_eff >= 0.60:
        recommendation = (
            "System-Effizienz akzeptabel, aber Upgrade auf bessere Lager "
            "würde die Handkraft deutlich reduzieren."
        )
    elif total_eff >= 0.40:
        recommendation = (
            "System-Effizienz unzureichend. Lager-Upgrade dringend empfohlen. "
            "Alternative: Winch-Unterstützung."
        )
    else:
        recommendation = (
            "System-Effizienz kritisch niedrig. Talje ist praktisch unwirksam. "
            "Kompletter Austausch der Blöcke oder Winch-Betrieb erforderlich."
        )
    
    return TackleEfficiencyResult(
        total_efficiency=round(total_eff, 4),
        effective_purchase=round(effective_purchase, 2),
        required_input_force_kg=round(required_force, 1),
        friction_loss_percent=round(friction_loss, 1),
        recommendation=recommendation,
    )
```

---

## ANHANG C — Normen und Standards

### C.1 Relevante ISO-Normen

| Norm | Titel | Relevanz für Hochlast-Blöcke |
|------|-------|------------------------------|
| ISO 8328:2000 | Sailing yachts — Deck hardware — Blocks | Prüfmethoden und Klassifizierung von Blöcken |
| ISO 10133:2012 | Small craft — Electrical systems — Extra-low-voltage DC installations | Kabelführung durch Deck-Beschläge |
| ISO 12215-5:2019 | Hull construction — Scantlings — Design pressures, stresses | Deckbelastung und Verstärkung |
| ISO 12215-9:2012 | Hull construction — Appendages and rig attachment | Rigg-Anbindung und Lasteinleitung |
| ISO 15085:2003 | Man-overboard prevention and recovery | Deck-Beschläge im Sicherheitskontext |
| ISO 13929:2001 | Tack fittings | Schot-Beschläge Dimensionierung |

> ⚠️ **ZU PRÜFEN (Audit):** Zwei Normzitate in dieser Tabelle sind fehlerhaft (web-verifiziert: iso.org):
> - **ISO 8328:2000 "Sailing yachts — Deck hardware — Blocks"** existiert so nicht. ISO 8328:1989 ist eine (zurückgezogene) Kunststoff-Norm über thermoplastische Formmassen — kein Block-/Deck-Hardware-Standard.
> - **ISO 13929:2001** heißt tatsächlich "Small craft — Steering gear — Geared link systems" (Ruderanlage/Lenkgetriebe für Boote bis 24 m), NICHT "Tack fittings / Schot-Beschläge". Fehlzitat.
>
> Ein zweifelsfrei korrekter ISO-Ersatz für Block-/Schot-Beschlag-Dimensionierung ist nicht belegbar (daher hier nicht ersetzt). Die übrigen Einträge (ISO 10133:2012, ISO 12215-5:2019, ISO 12215-9:2012, ISO 15085:2003) sind korrekt; Hinweis: ISO 12215-9:2012 trägt den Titel "Sailing craft appendages" (Kiel/Anhänge und deren Anbindung), die Ergänzung "rig attachment" ist eine Auslegung.

### C.2 Hersteller-Prüfstandards

**Harken Block Testing Protocol:**
1. Statischer Zugtest: 3× SWL über 60 Sekunden → keine bleibende Verformung
2. Bruchlasttest: Steigerung bis zum Versagen → muss ≥ angegebene Bruchlast erreichen
3. Zyklischer Test: 10.000 Zyklen bei 50% SWL → keine Risse, kein Lagerschaden
4. Salzsprühtest: 500h nach ISO 9227 → keine funktionsmindernde Korrosion
5. UV-Test (Kunststoff-Rollen): 1.000h nach ISO 4892-2 → max. 20% Festigkeitsverlust

**Lewmar Block Testing Protocol:**
1. Proof Load Test: 2× WLL → keine bleibende Verformung
2. Breaking Load Test: 3× WLL Minimum
3. Fatigue Test: 50.000 Zyklen bei 30% WLL
4. Side Load Test: 15° Seitenlast bei WLL → keine Verformung

### C.3 CE-Konformität und Rigg-Beschläge

Rigg-Beschläge fallen nicht direkt unter die Recreational Craft Directive 2013/53/EU (die CE-Kennzeichnung von Booten regelt). Jedoch:
- Der Bootshersteller muss bei der CE-Zertifizierung nachweisen, dass alle Rigg-Beschläge für die Design-Kategorie ausgelegt sind.
- MCA (Maritime and Coastguard Agency) für kommerzielle Yachten: LY3 Code verlangt 5:1 SF auf alle Rigg-Beschläge.
- Bei Eigenumbauten und Retrofits: Kein CE-Zwang auf einzelne Beschläge, aber der Eigner trägt die Verantwortung für die sichere Dimensionierung.

---

## ANHANG D — Lasttabellen

### D.1 Großschot-Lasten nach Bootsgröße und Windstärke

| Bootsgröße | Großsegel (m²) | 12 kt | 18 kt | 25 kt | 30 kt | 35 kt |
|-----------|---------------|-------|-------|-------|-------|-------|
| 8m | 18 | 280 kg | 630 kg | 1.210 kg | 1.750 kg | 2.380 kg |
| 10m | 28 | 435 kg | 980 kg | 1.890 kg | 2.720 kg | 3.700 kg |
| 12m | 38 | 590 kg | 1.330 kg | 2.560 kg | 3.690 kg | 5.020 kg |
| 14m | 50 | 780 kg | 1.750 kg | 3.370 kg | 4.860 kg | 6.610 kg |
| 16m | 65 | 1.010 kg | 2.280 kg | 4.380 kg | 6.310 kg | 8.590 kg |
| 18m | 82 | 1.280 kg | 2.870 kg | 5.530 kg | 7.960 kg | 10.830 kg |
| 20m | 100 | 1.560 kg | 3.510 kg | 6.740 kg | 9.710 kg | 13.210 kg |

*Hinweis: Werte sind Näherungen. Tatsächliche Lasten hängen von Rigg-Geometrie, Segelschnitt, Twist und Segeltuch ab.*

### D.2 Backstag-Lasten nach Bootsgröße

| Bootsgröße | Vorstag-Spannung (kg) | Backstag-Last (kg) | Min. Block-SWL (kg) | Min. Bruchlast (kg) |
|-----------|----------------------|--------------------|--------------------|---------------------|
| 10m | 2.500 | 1.500 | 3.000 | 9.000 |
| 12m | 3.800 | 2.500 | 5.000 | 15.000 |
| 14m | 5.500 | 3.500 | 7.000 | 21.000 |
| 16m | 7.500 | 5.000 | 10.000 | 30.000 |
| 18m | 10.000 | 6.500 | 13.000 | 39.000 |
| 20m | 13.000 | 8.500 | 17.000 | 51.000 |

### D.3 Vang-Lasten nach Bootsgröße

| Bootsgröße | Vang-Winkel (°) | Vang-Last bei 20 kt (kg) | Min. Block-SWL (kg) | Empf. Übersetzung |
|-----------|----------------|--------------------------|--------------------|--------------------|
| 8m | 40° | 650 | 1.300 | 4:1 |
| 10m | 38° | 1.100 | 2.200 | 6:1 |
| 12m | 35° | 1.700 | 3.400 | 8:1 |
| 14m | 33° | 2.500 | 5.000 | 8:1 |
| 16m | 30° | 3.600 | 7.200 | 12:1 oder Hydraulik |
| 18m | 28° | 5.200 | 10.400 | 16:1 oder Hydraulik |

### D.4 Bolzen-Tragfähigkeit in GFK-Laminat

| Bolzen | Laminat 6mm | Laminat 8mm | Laminat 10mm | Laminat 12mm | Laminat 15mm |
|--------|------------|------------|-------------|-------------|-------------|
| M6 | 1.200 kg | 1.600 kg | 2.000 kg | 2.400 kg | 3.000 kg |
| M8 | 1.800 kg | 2.400 kg | 3.000 kg | 3.600 kg | 4.500 kg |
| M10 | 2.400 kg | 3.200 kg | 4.000 kg | 4.800 kg | 6.000 kg |
| M12 | 3.000 kg | 4.000 kg | 5.000 kg | 6.000 kg | 7.500 kg |
| M16 | 4.200 kg | 5.600 kg | 7.000 kg | 8.400 kg | 10.500 kg |

*Werte für Auszug senkrecht zum Laminat mit Backing Plate, E-Glas/Polyester-Laminat.*

---

## ANHANG E — Confidence-Mapping

### E.1 Confidence-Zuordnung für Hochlast-Block-Bewertung

| Datenpunkt | Methode | Confidence |
|-----------|---------|-----------|
| Block-Bruchlast | Hersteller-Datenblatt | `measured` |
| Block-Bruchlast | Zugtest im Labor | `measured` |
| Block-Bruchlast | Schätzung nach Baugröße | `estimated` |
| Block-Zustand | Demontage und Inspektion | `measured` |
| Block-Zustand | Nahaufnahme mit Lupe | `visual_high` |
| Block-Zustand | Foto aus Entfernung | `visual_medium` |
| Block-Zustand | Allgemeines Deckfoto | `visual_low` |
| Achsverschleiß | Schieblehre-Messung | `measured` |
| Achsverschleiß | Visuell mit Referenz | `visual_medium` |
| Rollenverschleiß | Rillentiefe-Messung | `measured` |
| Rollenverschleiß | Visuell | `visual_medium` |
| Befestigung | Drehmoment-Kontrolle | `measured` |
| Befestigung | Visuell (Gelcoat-Risse) | `visual_high` |
| Backing Plate | Von unten inspiziert | `measured` |
| Backing Plate | Vorhanden/nicht vorhanden (Bauplan) | `documented` |
| Backing Plate | Nicht einsehbar | `estimated` |
| Korrosion | Materialanalyse (XRF) | `measured` |
| Korrosion | Visuell (Farbveränderung) | `visual_high` |
| Lastberechnung | Rigg-Berechnung mit Messdaten | `calculated` |
| Lastberechnung | Faustformel nach Bootsgröße | `estimated` |
| Ermüdungszustand | Zyklen dokumentiert | `documented` |
| Ermüdungszustand | Geschätzt nach Nutzungsprofil | `estimated` |

### E.2 Minimal erforderliche Confidence für Bewertung

| Bewertung | Min. Confidence | Begründung |
|-----------|----------------|-----------|
| "Block ist in Ordnung" | `visual_high` oder besser | Muss sichtbare Defekte ausschließen können |
| "Block muss getauscht werden" | `visual_medium` oder besser | Eindeutiger Defekt bereits bei mittlerer Sichtbarkeit |
| "Befestigung ist sicher" | `measured` | Muss messtechnisch bestätigt sein |
| "Block ist für Anwendung geeignet" | `measured` (Bruchlast) + `calculated` (Lastberechnung) | Keine Schätzungen bei Sicherheitsfragen |
| "Nicht beurteilbar" | unter `visual_medium` | Ehrliche Antwort wenn Daten unzureichend |

---

## ANHANG F — Wartungsintervalle

### F.1 Wartungsplan für Hochlast-Blöcke

| Maßnahme | Fahrtensegler | Regatta | Offshore | Charter |
|----------|--------------|---------|---------|---------|
| Süßwasser-Spülung | Nach jeder Tour | Nach jeder Regatta | Wöchentlich | Wöchentlich |
| Lager-Schmierung | Monatlich (Saison) | Alle 2 Wochen | Monatlich | Alle 2 Wochen |
| Sichtprüfung (Rollen, Achse) | Saisonbeginn | Monatlich | Monatlich | Wöchentlich |
| Drehmoment-Kontrolle | Jährlich | Halbjährlich | Halbjährlich | Vierteljährlich |
| Detailinspektion (Lupe, Lehre) | Alle 2 Jahre | Jährlich | Jährlich | Halbjährlich |
| Lager-Austausch | Alle 5–8 Jahre | Alle 2–3 Jahre | Alle 3–5 Jahre | Alle 2–3 Jahre |
| Block-Austausch | 10–15 Jahre | 5–8 Jahre | 8–12 Jahre | 5–8 Jahre |
| Backing-Plate-Kontrolle | Alle 5 Jahre | Alle 3 Jahre | Alle 3 Jahre | Alle 2 Jahre |

### F.2 Schmiermittel-Empfehlungen nach Hersteller

| Hersteller | Empfohlenes Schmiermittel | Alternative |
|-----------|--------------------------|-------------|
| Harken | Harken OneDrop | McLube Sailkote |
| Lewmar | Lewmar Winch Oil | McLube Sailkote |
| Ronstan | McLube Sailkote | Boeshield T-9 |
| Antal | Antal Block Lube | McLube Sailkote |
| Garhauer | Marine-Kugellagerfett | Boeshield T-9 |
| Schaefer | McLube Sailkote | Harken OneDrop |

---

## ANHANG G — Kostenvergleich

### G.1 Komplettsystem-Kosten: Großschot 6:1 für 12m Yacht

| Hersteller | Blöcke (3× + 2×) | Seil | Kleinteile | Gesamt | Gewicht |
|-----------|-------------------|------|-----------|--------|---------|
| Garhauer (Edelstahl) | € 550 | € 80 | € 50 | **€ 680** | 2.450 g |
| Ronstan Series 60 | € 780 | € 80 | € 50 | **€ 910** | 1.870 g |
| Lewmar Synchro 60 | € 920 | € 80 | € 50 | **€ 1.050** | 1.980 g |
| Harken ESP 57 | € 980 | € 80 | € 50 | **€ 1.110** | 1.620 g |
| Harken Black Magic 57 | € 1.350 | € 80 | € 50 | **€ 1.480** | 1.750 g |
| Antal XT Carbon 55 | € 1.950 | € 80 | € 50 | **€ 2.080** | 850 g |

### G.2 Preis pro kg Bruchlast (Benchmark)

| Hersteller/Serie | € pro kg Bruchlast | Segment |
|-----------------|---------------------|---------|
| Garhauer Edelstahl | 0,012–0,016 | Budget |
| Ronstan Series 55/60 | 0,017–0,022 | Mittelklasse |
| Lewmar Synchro | 0,019–0,025 | Mittelklasse |
| Harken ESP | 0,022–0,028 | Obere Mittelklasse |
| Schaefer Series 5/7 | 0,020–0,026 | Obere Mittelklasse |
| Harken Black Magic | 0,026–0,035 | Premium |
| Lewmar Ocean | 0,024–0,030 | Premium |
| Ronstan Series 100 | 0,020–0,026 | Premium |
| Antal XT Carbon | 0,035–0,050 | Ultra-Premium |

---

## ANHANG H — Montage-Checklisten

### H.1 Checkliste: Hochlast-Block Neuinstallation

```
VORBEREITUNG:
□ Lastberechnung durchgeführt (Block-Last, Dynamik, SF)
□ Block-Spezifikation verifiziert (Bruchlast ≥ erforderlich)
□ Seilgröße passt zur Rollenrille
□ Befestigungspunkte identifiziert
□ Deckaufbau dokumentiert (Sandwich? Massiv? Kernmaterial?)
□ Backing Plate dimensioniert und beschafft
□ Bolzen dimensioniert und beschafft (A4-80 oder besser)
□ Kompressionsröhrchen beschafft (bei Sandwich-Deck)
□ Dichtstoff bereitgestellt (Sikaflex 295 UV oder äquivalent)
□ Isolierbuchsen bereitgestellt (bei Alu-Block auf SS-Bolzen)
□ Werkzeug komplett (Bohrmaschine, Drehmomentschlüssel, Fräser)

KERNVERSTÄRKUNG (bei Sandwich-Deck):
□ Kernbereich markiert (1,5× Backing-Plate-Fläche)
□ Obere GFK-Haut entfernt (Fräser)
□ Kern entfernt (Stechbeitel)
□ Hohlraum gereinigt (Aceton, Staubsauger)
□ Epoxid-Füllmasse angemischt (105/206 + 407)
□ Hohlraum verfüllt
□ Aushärtezeit eingehalten (min. 24h / 20°C)
□ Oberfläche plangeschliffen

MONTAGE:
□ Position markiert (Trockenmontage!)
□ Bohrungen gesetzt (0,5mm größer als Bolzen)
□ Kompressionsröhrchen eingesetzt (mit Epoxid)
□ Dichtstoff aufgetragen (Bolzen + Bohrung + Unterseite Block)
□ Bolzen eingesetzt
□ Isolierbuchsen korrekt platziert
□ Backing Plate aufgesetzt
□ Unterlegscheiben + Muttern aufgesetzt
□ Drehmoment schrittweise angezogen (50% → 75% → 100%)
□ Drehmoment dokumentiert
□ Austretender Dichtstoff sauber entfernt
□ 24h Aushärtezeit eingehalten vor Belastung

FUNKTIONSPRÜFUNG:
□ Rolle dreht frei
□ Seil läuft durch ohne Klemmen
□ Kein Spiel zwischen Block und Deck
□ Umlenkwinkel korrekt
□ Kein Kontakt Seil-Deck bei Betrieb
□ Belastungstest (50% → 100% Arbeitslast)
□ Keine Verformung oder Bewegung unter Last

DOKUMENTATION:
□ Block-Typ und Artikelnummer notiert
□ Einbaudatum notiert
□ Drehmomente dokumentiert
□ Fotos von Ober- und Unterseite
□ In Bordbuch eingetragen
```

### H.2 Checkliste: Jährliche Inspektion Hochlast-Blöcke

```
VISUELLE PRÜFUNG:
□ Alle Blöcke identifiziert und lokalisiert
□ Rollen: Frei drehend? Geräusche?
□ Gehäuse: Risse? Korrosion? Verformung?
□ Achse: Gerade? Verschleiß?
□ Schäkel: Bolzen fest? Verformung? Risse?
□ Wirbel (falls vorhanden): Dreht frei?
□ Seilrille: Verschleiß? Grate?

BEFESTIGUNG:
□ Block sitzt fest am Deck (keine Bewegung)
□ Gelcoat um Befestigung rissfrei
□ Keine Korrosion an Bolzenköpfen
□ Backing Plate von unten prüfen (wenn zugänglich)
□ Drehmoment stichprobenartig kontrollieren

SEIL AM BLOCK:
□ Seil-Mantel intakt an Block-Kontaktflächen
□ Keine Quetschspuren oder Schnitte
□ Keine Schmelzspuren
□ Seil-Durchmesser passt noch zur Rille

SCHMIERUNG:
□ Rollen geschmiert
□ Achsen geschmiert
□ Schäkel-Bolzen gefettet (Lanolin)

DOKUMENTATION:
□ Befunde protokolliert
□ Fotos gemacht
□ Nächster Inspektionstermin festgelegt
□ Befunde an Eigner/Kapitän kommuniziert
```

---

## ANHANG I — Bruchlast-Referenz

### I.1 Bruchlast-Vergleich: Alle Hersteller, 75mm Klasse

| Hersteller | Modell | Typ | Bruchlast (kg) | SWL (kg) | Gewicht (g) | Lager |
|-----------|--------|-----|---------------|----------|------------|-------|
| Harken | 2645 Black Magic | Einzel | 8.850 | 2.950 | 425 | Nadel |
| Harken | 1091 ESP | Einzel | 6.600 | 2.200 | 310 | Kugel |
| Lewmar | Synchro 80 | Einzel | 10.500 | 3.500 | 580 | Kugel |
| Lewmar | Ocean 80 | Einzel | 12.600 | 4.200 | 720 | Nadel |
| Ronstan | RF75110 | Einzel | 9.600 | 3.200 | 480 | Kugel |
| Antal | XT75C-S | Einzel | 9.600 | 3.200 | 180 | Nadel |
| Schaefer | 504-71 | Einzel | 8.400 | 2.800 | 450 | Kugel |
| Garhauer | 75-01-OT | Einzel | 8.400 | 2.800 | 550 | Kugel |
| Rutgerson | R80S | Einzel | 10.500 | 3.500 | 540 | Kugel |

### I.2 Bruchlast-Vergleich: Alle Hersteller, 57/60mm Klasse

| Hersteller | Modell | Typ | Bruchlast (kg) | SWL (kg) | Gewicht (g) | Lager |
|-----------|--------|-----|---------------|----------|------------|-------|
| Harken | 1086 ESP 57 | Einzel | 4.200 | 1.400 | 160 | Kugel |
| Harken | Black Magic 57 | Einzel | 8.850 | 2.950 | 425 | Nadel |
| Lewmar | Synchro 60 | Einzel | 6.000 | 2.000 | 310 | Kugel |
| Lewmar | Ocean 60 | Einzel | 7.500 | 2.500 | 380 | Kugel |
| Ronstan | RF60110 | Einzel | 6.600 | 2.200 | 310 | Kugel |
| Ronstan | RF55110 | Einzel | 3.900 | 1.300 | 180 | Kugel |
| Antal | XT55C-S | Einzel | 5.400 | 1.800 | 95 | Nadel |
| Garhauer | 60-01-OT | Einzel | 5.400 | 1.800 | 340 | Kugel |
| Schaefer | 504-51 | Einzel | 5.400 | 1.800 | 280 | Kugel |

> ⚠️ **ZU PRÜFEN (Audit):** Die Zeile "Harken Black Magic 57" enthält 75-mm-Werte (Bruchlast 8.850 kg / SWL 2.950 kg / 425 g = Artikel 2645, Black Magic **75 mm** laut Abschnitt 4.1.2 und Anhang I.1) in einer 57/60-mm-Vergleichstabelle. Eine 57-mm-Black-Magic-Serie existiert im Katalog dieser Datei nicht — Größenangabe oder Datensatz ist widersprüchlich. (Die erste Harken-Zeile wurde von "2645" auf "1086" korrigiert, da Artikel 2645 der Black-Magic-75-mm-Einzelblock ist, während die Werte 4.200/1.400/160 g dem ESP-57-Einzelblock 1086 aus Abschnitt 4.1.7 entsprechen.)

---

## ANHANG J — Zusätzliche Fallstudien

### Fallstudie J1: Vang-System Upgrade, X-Yachts X-362

**Boot:** X-Yachts X-362, Baujahr 1996, 10,97m
**Problem:** Originaler Vang (Selden 4:1 Talje mit Gleitlager-Blöcken) unzureichend bei Starkwind. Baum hebt sich bei Böen, Achterliek öffnet unkontrolliert.
**Diagnose:** Vang-Last bei 20 Knoten: ~1.100 kg. System-Effizienz der alten Blöcke: 0,85^4 = 0,52. Effektive Übersetzung: 2,1:1 statt nominell 4:1. Handkraft erforderlich: 524 kg — unmöglich.
**Lösung:** Upgrade auf Harken ESP 57mm Doppel/Einzel mit Becket (6:1) + Ronstan Rigid-Vang-Strebe. Neue Effizienz: 0,97^6 = 0,83. Effektive Übersetzung: 4,98:1. Handkraft: 221 kg — noch hoch, aber mit kurzem Zug machbar.
**Kosten:** € 1.200 (Blöcke + Strebe + Seil + Installation)
**Ergebnis:** Deutlich bessere Achterliek-Kontrolle, Boot zeigt messbar bessere VMG bei Kreuz in 18+ Knoten.

### Fallstudie J2: Notfall-Reparatur Running Backstay, Transatlantik

**Boot:** Oyster 56, Transatlantik-Überführung, Tag 14
**Situation:** Steuerbord Running Backstay-Block (Lewmar Synchro 80) verliert Rolle — Kugellager zerfallen, Rolle fällt ab.
**Sofortmaßnahme:** Auf Steuerbord-Halse gewechselt (Backbord-Runner arbeitet). Provisorische Reparatur mit Ersatz-Schäkel als Umlenkung (kein Block, nur Reibung). Kurs auf Horta (Azoren) geändert.
**Endgültige Reparatur:** In Horta wurde ein Ronstan RF75110 als Ersatz beschafft (der einzige verfügbare Hochlast-Block auf der Insel). Originaler Lewmar-Block zur Überprüfung nach UK geschickt.
**Analyse:** Lager-Ausfall durch Salzwasser-Eindrang und mangelhafte Wartung. Der Block hatte in 6 Jahren nie ein Lager-Service erhalten.
**Lehre:** Für Langfahrt/Offshore immer Ersatz-Blöcke an Bord haben. Mindestens: 2× Hochlast-Einzelblock passend zum größten installierten System.

### Fallstudie J3: Deck-Organizer Wassereintritt, Contest 46CS

**Boot:** Contest 46CS, Baujahr 2012
**Problem:** Regelmäßiger Wasseintritt im Vorschiff, Quelle lange nicht lokalisierbar.
**Diagnose:** Der 6-fach Deck-Organizer am Mastfuß hatte nach 8 Jahren so viel Mikrobewegung unter Last gezeigt, dass die Sikaflex-Abdichtung der Durchgangsbolzen gerissen war. Wasser lief entlang der Bolzen ins Schiffsinnere.
**Lösung:** Organizer demontiert, alte Dichtung entfernt, Oberflächen gereinigt, mit Sikaflex 295 UV neu abgedichtet. Zusätzlich: Nyloc-Muttern gegen selbstsichernde Muttern ausgetauscht.
**Kosten:** € 35 (Sikaflex + Muttern) + 4h Eigenarbeit.
**Lehre:** Auch korrekt installierte Hochlast-Beschläge können durch jahrelange Mikrobewegung unter Last ihre Abdichtung verlieren. Regelmäßige Kontrolle (Spritzwassertest) ist wichtig.

---

## ANHANG K — Hersteller-Teilenummern-Index

### K.1 Schnell-Referenz: Artikelnummern nach Anwendung

#### Großschot 4:1 (8–10m Yacht)

| Hersteller | Oberer Block | Unterer Block (Becket) | System-Art.-Nr. |
|-----------|-------------|----------------------|----------------|
| Harken | 1088 (ESP 57 Doppel) | 1087 (ESP 57 Einzel B) | 7471 |
| Lewmar | 29925037 (Synchro 60 D) | 29925036 (Synchro 60 S B) | — |
| Ronstan | RF60210 (S60 Doppel) | RF60120 (S60 Einzel B) | — |
| Garhauer | 60-04-OT (60 Doppel) | 60-02-OT (60 Einzel B) | 60-MS-4 |

#### Großschot 6:1 (10–14m Yacht)

| Hersteller | Oberer Block | Unterer Block (Becket) | System-Art.-Nr. |
|-----------|-------------|----------------------|----------------|
| Harken | 2658 (Black 75 Dreifach) | 2656 (Black 75 Doppel B) | 7476 |
| Lewmar | 29925059 (Synchro 80 T) | 29925058 (Synchro 80 D B) | — |
| Ronstan | RF75310 (S75 Dreifach) | RF75220 (S75 Doppel B) | — |
| Garhauer | 75-06-OT (75 Dreifach) | 75-05-OT (75 Doppel B) | 75-MS-6 |

#### Backstag-Trimmer (12–16m Yacht)

| Hersteller | Block (×2) | Art.-Nr. |
|-----------|-----------|---------|
| Harken | Black Magic 75 Einzel, Wirbel | 2646 |
| Lewmar | Synchro 80 Einzel, Schäkel | 29925055 |
| Ronstan | Series 75 Einzel, Wirbel | RF75130 |
| Antal | XT75 Carbon Einzel | XT75C-S |

#### Genuaschot Turning Block (10–14m Yacht)

| Hersteller | Block | Art.-Nr. |
|-----------|-------|---------|
| Harken | Stand-Up Spring 57mm | 2691 |
| Harken | Stand-Up Spring 75mm | 2692 |
| Lewmar | Synchro 60 Stand-Up | 29925042 |
| Ronstan | Series 60 Einzel, Wirbel | RF60130 |

---

## ANHANG L — Visuelle Inspektion Referenzkarten

### L.1 Visuelle Kriterien für AYDI-Bildanalyse

| Zustand | Visuelle Indikatoren | Confidence | Schweregrad |
|---------|---------------------|-----------|------------|
| Neuwertiger Block | Glatte Oberfläche, keine Kratzer, klare Anodisierung | `visual_high` | OK |
| Gebrauchter Block (gut) | Leichte Gebrauchsspuren, Anodisierung intakt | `visual_high` | OK |
| Leichter Verschleiß | Kratzer, matter Glanz, Seil-Abriebspuren in der Rille | `visual_medium` | MONITOR |
| Korrosion (leicht) | Weiße Flecken (Alu) oder braune Punkte (Edelstahl) | `visual_high` | MONITOR |
| Korrosion (mittel) | Flächige Verfärbung, Pitting sichtbar | `visual_high` | SERVICE |
| Korrosion (schwer) | Material abgetragen, Strukturverlust sichtbar | `visual_high` | ERSETZEN |
| Riss sichtbar | Linie im Material, oft an Bohrung/Radius | `visual_high` | KRITISCH |
| Verformung sichtbar | Block ist verbogen, Achse schief | `visual_high` | KRITISCH |
| Befestigung lose | Block steht ab, Spalt unter Block sichtbar | `visual_high` | KRITISCH |
| Gelcoat-Schäden | Risse im Gelcoat um Befestigung | `visual_high` | SERVICE |
| Seilschaden am Block | Aufgeplusterter Mantel, Schnittstellen | `visual_high` | SERVICE |

### L.2 Foto-Anforderungen für zuverlässige Bewertung

| Aspekt | Minimum für `visual_medium` | Empfohlen für `visual_high` |
|--------|---------------------------|----------------------------|
| Auflösung | 5 MP | 12+ MP |
| Abstand | < 50 cm | < 20 cm |
| Beleuchtung | Tageslicht, keine Gegenlicht | Tageslicht + LED-Taschenlampe seitlich |
| Winkel | Draufsicht | Draufsicht + 2× Seitenansicht |
| Fokus | Block im Fokus | Block + Befestigung + Seil im Fokus |
| Referenz | Keine | Maßstab (Lineal, Münze) im Bild |

---

## ANHANG M — Saisonale Wartung Hochlast-Blöcke

### M.1 Frühjahrs-Inbetriebnahme (vor Saisonbeginn)

```
1. Alle Hochlast-Blöcke visuell inspizieren (Checkliste ANHANG H.2)
2. Rollen auf Freigängigkeit prüfen
3. Süßwasser-Spülung aller Blöcke
4. Lager schmieren (herstellerspezifisches Schmiermittel)
5. Bolzen-Drehmomente stichprobenartig kontrollieren
6. Seil-Zustand an Block-Kontaktflächen prüfen
7. Gelcoat um Befestigungspunkte auf Risse prüfen
8. Funktionstest unter moderater Last (Anlegemanöver)
9. Befunde dokumentieren
```

### M.2 Mitte-Saison-Check (Juli/August)

```
1. Visueller Rundgang über alle Hochlast-Positionen
2. Rollen-Freigängigkeit prüfen (trockenes Drehen von Hand)
3. Schmierung auffrischen wenn nötig
4. Besondere Aufmerksamkeit auf Running Backstay und Backstag-Trimmer
```

### M.3 Einwinterung (Saisonende)

```
1. Gründliche Süßwasser-Spülung aller Blöcke
2. Trocknen lassen (nicht föhnen)
3. Lager großzügig schmieren
4. Achsen und Bolzen mit Lanolin (Lanocote) einreiben
5. Schäkel-Bolzen lösen und separat lagern
6. Persenning oder Schutzabdeckung über exponierte Blöcke
7. Dokumentation: Befunde notieren, nächste Saison planen
```

---

## ANHANG N — Retrofit-Szenarien

### N.1 Upgrade von 4:1 auf 6:1 Großschot

**Ausgangslage:** 10m Fahrtensegler mit 4:1 Großschot (Doppel/Einzel mit Becket), 57mm Blöcke.
**Ziel:** 6:1 für besseres Trimmen bei Starkwind.

**Erforderliche Änderungen:**
1. Oberer Block: Doppel → Dreifach (57mm oder 75mm)
2. Unterer Block: Einzel mit Becket → Doppel mit Becket
3. Schotlänge: Erhöht sich um ca. 2× Abstand Baumende-Traveller
4. Traveller-Befestigung prüfen: Höhere Last durch bessere Übersetzung
5. Befestigungspunkt am Baum prüfen: Last bleibt gleich

**Kosten (Harken ESP):** € 520–680 (Blöcke + Seil)
**Arbeitszeit:** 2–4 Stunden

### N.2 Nachrüstung Running Backstays

**Ausgangslage:** 14m Performance Cruiser ohne Running Backstays, aber mit Fraktionalrigg.
**Ziel:** Running Backstays für bessere Vorstag-Spannung und Segel-Trimm.

**Erforderliche Komponenten:**
1. 2× Hochlast-Einzelblock 75mm (z.B. Harken 2646): ca. € 490
2. 2× Chainplate (17-4 PH Edelstahl, einlaminiert): ca. € 800
3. 2× Deck-Umlenkblock 57mm: ca. € 320
4. 2× Talje 8:1 mit 57mm Blöcken: ca. € 960
5. Dyneema-Seil 12mm, 2× 18m: ca. € 350
6. Backing Plates, Bolzen, Dichtstoff: ca. € 180

**Gesamtkosten:** ca. € 3.100
**Arbeitszeit:** 20–30 Stunden (inkl. Laminierarbeiten für Chainplates)

### N.3 Umstellung auf Dyneema-Seile

**Ausgangslage:** Alle Systeme mit Polyester-Doppelgeflecht-Seilen.
**Ziel:** Umstellung auf Dyneema-Kern-Seile für weniger Reck und kleinere Durchmesser.

**Blockauswirkungen:**
- Geringerer Seildurchmesser → prüfen ob Rollenrille noch passt
- Dyneema schneidet in weiche Kunststoff-Rollen → ggf. Torlon/Alu-Rollen nachrüsten
- Min. Rollendurchmesser beachten (7× statt 6× Seildurchmesser)
- Rollenrillen-Form: Flach oder V-förmig bevorzugt (nicht tiefe U-Rille)

---

## ANHANG O — Prüfprotokolle und Dokumentation

### O.1 Prüfprotokoll-Vorlage für Hochlast-Blöcke

```
=== HOCHLAST-BLOCK PRÜFPROTOKOLL ===

Datum: ____________
Prüfer: ____________
Boot: _____________ (Typ, Baujahr, Name)

BLOCK-IDENTIFIKATION:
Position: _____________ (z.B. Großschot oben, Backstag Stb)
Hersteller: _____________
Artikelnummer: _____________
Typ: _____________ (Einzel/Doppel/Dreifach/Fiddle/Turning/Cheek)
Alter (ca.): _____________ Jahre
Letzte Inspektion: _____________

BEFUND:
Rolle(n): □ i.O.  □ Verschleiß  □ Beschädigt  □ n/a
Lager:    □ i.O.  □ Schwergängig □ Beschädigt  □ n/a
Achse:    □ i.O.  □ Verschleiß  □ Verbogen   □ n/a
Gehäuse:  □ i.O.  □ Korrosion   □ Risse      □ n/a
Schäkel:  □ i.O.  □ Verformt   □ Verschlissen □ n/a
Wirbel:   □ i.O.  □ Schwergängig □ Beschädigt  □ n/a
Befest.:  □ i.O.  □ Lose       □ Gelcoat-Risse □ n/a
Backing:  □ i.O.  □ Verformt   □ Nicht vorhanden □ Nicht einsehbar

BEWERTUNG:
□ In Ordnung — keine Maßnahmen erforderlich
□ Beobachten — bei nächster Inspektion erneut prüfen
□ Service erforderlich — Schmierung/Reinigung/Nachziehen
□ Austausch bald — innerhalb der nächsten Saison
□ Sofort austauschen — NICHT weiter belasten
□ KRITISCH — Boot darf nicht segeln bis behoben

BEMERKUNGEN:
_____________________________________________
_____________________________________________
_____________________________________________

Nächste Inspektion fällig: ____________
Prüfer-Unterschrift: ____________
```

### O.2 Dokumentationsanforderungen nach Anwendung

| Anwendung | Prüf-Intervall | Dokumentation erforderlich | Aufbewahrung |
|-----------|---------------|--------------------------|-------------|
| Privatyacht, Fahrten | Jährlich | Empfohlen | 5 Jahre |
| Charter-Yacht | Vierteljährlich | Pflicht (Versicherung) | 10 Jahre |
| Offshore-Regatta | Vor jeder Regatta | Pflicht (ORC/RORC) | 3 Jahre |
| Superyacht (MCA) | Halbjährlich | Pflicht (MCA Compliance) | Lebensdauer |
| Segelschule | Vierteljährlich | Pflicht (BG Verkehr) | 10 Jahre |

---

## ANHANG P — Berechnungsbeispiele

### P.1 Vollständige Dimensionierung: Großschot-System, 12m Fahrtensegler

```
GEGEBENE DATEN:
  Bootslänge: 12m
  Großsegelfläche: 38 m²
  Design-Windstärke: 25 kt (12,9 m/s) 
  Segelprofil: Bermudasegel, 7/8-Rigg
  Baumlänge: 4,5 m
  Traveller auf Cockpit-Dach, mittschiffs

SCHRITT 1: Segelkraft berechnen
  F_segel = 0,5 × 1,225 × 12,9² × 38 × 1,2
  F_segel = 0,5 × 1,225 × 166,41 × 38 × 1,2
  F_segel = 4.650 kg

SCHRITT 2: Großschot-Last
  F_schot = F_segel × 0,7 (Faktor für Schothorn-Last)
  F_schot = 4.650 × 0,7 = 3.255 kg

SCHRITT 3: Block-Last am Traveller-Block (180° Umlenkung)
  F_block = 2 × F_schot_part (Last pro Seilpart)
  Bei 6:1: F_part = 3.255 / 6 = 543 kg (am losen Ende)
  Aber: Am Traveller-Block wirkt die volle Großschotkraft:
  F_block_traveller = 3.255 kg (direkte Übertragung)

SCHRITT 4: Dynamikfaktor
  Böenlast (25 kt, böig): Faktor 2,0
  F_design = 3.255 × 2,0 = 6.510 kg

SCHRITT 5: Sicherheitsfaktor
  Fahrtensegler: 3:1
  F_bruch_erforderlich = 6.510 × 3,0 = 19.530 kg

SCHRITT 6: Block-Auswahl
  Oberer Block (Baum): Dreifach, Bruchlast ≥ 19.530 kg
  → Harken Black Magic 75mm Dreifach (2660): Bruchlast 14.400 kg — NICHT AUSREICHEND
  → Lewmar Synchro 80 Dreifach (29925059): Bruchlast 18.000 kg — KNAPP
  → Lewmar Ocean 80 Dreifach (29926020): Bruchlast 21.000 kg — OK
  
  Alternative: Übersetzung auf 8:1 erhöhen → reduziert Last pro Part
  Oder: 25 kt ist Design-Maximum, Reffen bei >20 kt → Last-Reduktion

PRAGMATISCHE EMPFEHLUNG:
  75mm Blöcke, 6:1, mit der Maßgabe dass bei >20 kt ein Reff gesetzt wird.
  → Harken Black Magic 75mm (14.400 kg Bruchlast) ist mit 
     Reef-Strategie ausreichend.
  → Für "Aufrecht-Segeln bis 25 kt ohne Reff": 
     Lewmar Ocean 80 oder Ronstan Series 100
```

### P.2 Effizienz-Vergleich: Lager-Upgrade

```
AUSGANGSLAGE:
  8:1 Vang-Talje, 8 Umlenkungen
  Alte Blöcke: Delrin-Buchsen, η = 0,85

ALTE EFFIZIENZ:
  η_gesamt = 0,85^8 = 0,272 (27,2%)
  Effektive Übersetzung = 8 × 0,272 = 2,18:1
  Handkraft bei 1.500 kg Vang-Last: 1.500 / 2,18 = 688 kg → UNMÖGLICH

NEUE BLÖCKE: Kugellager, η = 0,97
  η_gesamt = 0,97^8 = 0,784 (78,4%)
  Effektive Übersetzung = 8 × 0,784 = 6,27:1
  Handkraft bei 1.500 kg Vang-Last: 1.500 / 6,27 = 239 kg → Sehr hoch, aber kurz möglich

PREMIUM-BLÖCKE: Nadellager, η = 0,98
  η_gesamt = 0,98^8 = 0,851 (85,1%)
  Effektive Übersetzung = 8 × 0,851 = 6,81:1
  Handkraft bei 1.500 kg Vang-Last: 1.500 / 6,81 = 220 kg → Etwas besser

FAZIT: Der Sprung von Gleitlager (η=0,85) zu Kugellager (η=0,97) ist 
       dramatisch: Handkraft sinkt von unmöglich auf machbar.
       Der weitere Sprung zu Nadellager (η=0,98) bringt nur noch 
       marginale Verbesserung.
```

---

## ANHANG Q — Materialzertifikate und Anforderungen

### Q.1 Materialanforderungen für Hochlast-Block-Komponenten

| Komponente | Material | Min. Zugfestigkeit | Min. Streckgrenze | Bemerkung |
|-----------|---------|-------------------|-------------------|-----------|
| Achse | 17-4 PH SS (H1025) | 1.070 MPa | 1.000 MPa | Ausgehärtet |
| Achse (Budget) | 316L SS | 500 MPa | 200 MPa | Kaltverformt bis 600 MPa |
| Achse (Racing) | Titan Grade 5 | 950 MPa | 880 MPa | Leicht + stark |
| Gehäuse | 6061-T6 Alu | 310 MPa | 276 MPa | Standard |
| Gehäuse (Racing) | 7075-T6 Alu | 572 MPa | 503 MPa | Höchstfest, korrosionsempfindlicher |
| Seitenplatte (Carbon) | CFK UD/Gewebe | 1.500 MPa (Faser) | n/a | Faserdominiert |
| Schäkel | 316L SS, geschmiedet | 500 MPa | 200 MPa | Nicht gegossen! |
| Bolzen (Befestigung) | A4-80 SS | 800 MPa | 600 MPa | ISO 3506 |
| Backing Plate | 316L SS | 500 MPa | 200 MPa | Platte, nicht Blech |
| Kompressionsröhrchen | 316L SS oder 6061-T6 | 200 MPa (min) | n/a | Nur Druckbelastung |

### Q.2 Materialkennzeichnung prüfen

**Edelstahl-Identifikation:**
- 316L (A4): Nicht magnetisch. Markierung "A4" oder "316" auf dem Beschlag.
- 304 (A2): Nicht magnetisch. NICHT für maritime Hochlast geeignet (Spannungsrisskorrosion).
- 17-4 PH: Leicht magnetisch. Markierung "17-4" oder "630".

**Test:** Magnet-Test — 316L und 304 sind nicht magnetisch. 17-4 PH ist schwach magnetisch. Wenn ein angeblicher "316L" Block stark magnetisch ist, handelt es sich wahrscheinlich um ein minderwertiges Material.

**Aluminium-Identifikation:**
- 6061-T6: Standard-Yachtbeschlag. Hart, gut anodisierbar.
- 7075-T6: Racing. Härter, stärker, aber korrosionsempfindlicher.
- Kennzeichnung oft nur über Hersteller-Dokumentation möglich.

---

## ANHANG R — Weiterführende Ressourcen

### R.1 Fachliteratur

| Titel | Autor | Relevanz |
|-------|-------|----------|
| Rigging Modern Sailboats | Ivar Dedekam | Umfassende Rigg-Planung inkl. Block-Dimensionierung |
| The Complete Rigger's Apprentice | Brion Toss | Klassiker, traditionelle und moderne Techniken |
| Yacht Design Explained | Steve Killing | Grundlagen der Yacht-Konstruktion und Lastwege |
| High Performance Sailing | Frank Bethwaite | Aerodynamik und Kräfte im Rigg |
| Stress and Strain | Eric Sponberg | Strukturelle Analyse von Yachten |

### R.2 Hersteller-Technische Dokumentation

| Hersteller | Dokument | Zugang |
|-----------|---------|--------|
| Harken | Technical Reference Guide | harken.com/tech |
| Lewmar | Product Catalogue & Technical Data | lewmar.com/catalogue |
| Ronstan | Product Guide | ronstan.com/products |
| Antal | Technical Catalogue | antal.it/catalogue |
| Garhauer | Product Catalogue | garhauermarine.com |
| Schaefer | Marine Hardware Catalogue | schaefermarine.com |

### R.3 Online-Ressourcen und Foren

| Ressource | Sprache | Fokus |
|-----------|---------|-------|
| SailNet Forums — Rigging | EN | Rigg-Diskussionen, Erfahrungsberichte |
| Cruisers Forum — Hardware | EN | Langfahrt-Beschläge, Budget-Lösungen |
| Segeln-Forum.de | DE | Deutsche Segler-Community |
| YBW Forum — Rigging | EN | UK-fokussierte Rigg-Diskussionen |
| Sailing Anarchy — Hardware | EN | Racing-fokussierte Beschlag-Diskussionen |

### R.4 AYDI-interne Verweise

| Wissensdatei | Inhalt | Bezug zu Hochlast-Blöcken |
|-------------|--------|---------------------------|
| 10.01 | Blöcke Grundlagen | Basis-Wissen, Standard-Blöcke |
| 10.02 | Harken Blöcke (Detail) | Vollsortiment Harken |
| 10.03 | Lewmar/Ronstan Blöcke | Vollsortiment Lewmar und Ronstan |
| (geplant) 10.05 | Traveller-Systeme | Großschot-Traveller, Genuaschot-Schienen |
| (geplant) 10.06 | Winschen | Winch-Systeme für Hochlast |
| (geplant) 11.xx | Laufendes Gut — Seile | Seiltypen, Dimensionierung |
| (geplant) 12.xx | Rigg — Stehendes Gut | Wanten, Stagen, Terminals |

---

## ANHANG S — Erweiterte Lastszenarien und Sonderfälle

### S.1 Lastszenarien bei Starkwind und Sturm

Bei Starkwind-Bedingungen (>30 Knoten) und Sturm (>40 Knoten) ändern sich die Anforderungen an Hochlast-Blöcke fundamental. Die normalen Betriebslasten werden um ein Vielfaches überschritten.

#### S.1.1 Sturm-Lastfaktoren

| Windstärke | Faktor vs. 20 kt | Laststeigerung | Empfehlung |
|-----------|------------------|----------------|-----------|
| 25 kt (Bft 6) | 1,6× | +56% | Erstes Reff |
| 30 kt (Bft 7) | 2,3× | +125% | Zweites Reff |
| 35 kt (Bft 8) | 3,1× | +206% | Drittes Reff oder Trysegel |
| 40 kt (Bft 8-9) | 4,0× | +300% | Trysegel oder Beidrehen |
| 50 kt (Bft 10) | 6,3× | +525% | Beidrehen oder Lenzen |
| 60 kt (Bft 11) | 9,0× | +800% | Nur Sturmfock oder blank |

**Konsequenz für Hochlast-Blöcke:**
Die Blöcke müssen für das schlimmste realistische Szenario dimensioniert werden — nicht für den normalen Betrieb. Ein Fahrtensegler, der mit Trysegel in 40 Knoten segelt, braucht Blöcke, die diese Lasten sicher aufnehmen.

#### S.1.2 Trysegel-Schot-Umlenkung

Das Trysegel wird über separate Schot-Blöcke gefahren, die nicht zur normalen Großschot-Führung gehören:

```
Trysegel-Schot-Last (12m Yacht, 40 kt):
  Trysegel-Fläche: ~8 m² (vs. 38 m² Großsegel)
  F_segel = 0,5 × 1,225 × 20,6² × 8 × 1,0 = 2.076 kg
  
  Umlenkwinkel am Turning Block: ~120°
  F_block = 2 × 2.076 × sin(60°) = 3.596 kg
  
  Mit Dynamik (Böe in Sturm): × 3,0
  F_design = 3.596 × 3,0 = 10.788 kg
  
  SF 3:1: Bruchlast_erf = 32.364 kg
  → Extrem hohe Anforderung! Block muss entsprechend dimensioniert sein.
```

**Empfehlung:** Trysegel-Umlenkblöcke: Ronstan Series 100 oder Lewmar Ocean 80 minimum.

#### S.1.3 Sturmfock-Umlenkung

Die Sturmfock wird an den Genuaschot-Turning-Blocks oder an separaten Blöcken gefahren. Die Lasten sind trotz der kleinen Segelfläche hoch, da die Windgeschwindigkeit extrem ist.

```
Sturmfock-Schot-Last (12m Yacht, 45 kt):
  Sturmfock-Fläche: ~6 m²
  F_segel = 0,5 × 1,225 × 23,2² × 6 × 1,0 = 1.979 kg
  
  Am Turning Block (150° Umlenkung):
  F_block = 2 × 1.979 × sin(75°) = 3.824 kg
  
  Dynamik (Sturm, brechende See): × 3,5
  F_design = 3.824 × 3,5 = 13.384 kg
```

### S.2 Sonderlast: Mann-über-Bord-Bergen

Wenn ein MOB-Flaschenzug (Rettungsflaschenzug) über Hochlast-Blöcke an Bord gehievt wird:

```
Gewicht Person (inkl. nasse Kleidung): 100 kg
Dynamik (Wellengang): × 3,0
Erforderliche Hebekraft: 300 kg

Bei 4:1 Flaschenzug: Handkraft = 300 / (4 × 0,95) = 79 kg
Block-Last am oberen Block: ~300 kg

SF für lebensrettende Funktion: 5:1
Bruchlast_erf = 300 × 5 = 1.500 kg
```

**Wichtig:** MOB-Bergen ist eine lebensrettende Funktion. Sicherheitsfaktor 5:1 ist zwingend. Die verwendeten Blöcke müssen mindestens 1.500 kg Bruchlast haben — selbst bei "nur" 100 kg Person.

### S.3 Sonderlast: Ankerberge-Umlenkung

Bei Yachten mit Heckanker oder Buganker-Umlenkung über Hochlast-Blöcke:

```
Ankerlast (schwere See, 12m Yacht):
  Ankergewicht + Kette (30m): 50 kg
  Dynamik (Schwell, Strömung): × 5,0
  F_design = 50 × 5 = 250 kg
  
  ABER: Ankerlast bei Sturm (Haltekraft des Ankers):
  F_anker = bis 2.000 kg (bei 12m Yacht in 50 kt Wind)
  F_block (90° Umlenkung) = 1,414 × 2.000 = 2.828 kg
  
  SF 3:1: Bruchlast_erf = 8.484 kg
```

### S.4 Sonderlast: Spinnaker-Holepunkt-Crash

Ein gefürchtetes Szenario: Der Spinnaker füllt sich unkontrolliert bei einem Kurswechsel. Die Kräfte können das 5–10-fache der normalen Betriebslast erreichen.

```
Spinnaker-Crash-Last (14m Yacht, 18 kt):
  Normale Spinnaker-Schotlast: 800 kg
  Crash-Faktor (plötzliches Füllen): × 5,0
  F_crash = 800 × 5 = 4.000 kg
  
  Am Barber-Hauler-Block (90° Umlenkung):
  F_block = 1,414 × 4.000 = 5.656 kg
  
  SF 3:1: Bruchlast_erf = 16.968 kg
  → 75mm oder 100mm Block erforderlich!
```

**Empfehlung:** Spinnaker-Systeme immer mit einer "Sollbruchstelle" (Weak Link) im Seil versehen, die bei 150% der Betriebslast bricht und damit den Spinnaker kontrolliert freigibt, bevor der Block oder die Decksbefestigung versagt.

---

## ANHANG T — Innovationen und Trends

### T.1 Aktuelle Trends im Hochlast-Block-Design (2024–2026)

#### T.1.1 Digitale Lastüberwachung (Smart Blocks)

Mehrere Hersteller arbeiten an Blöcken mit integrierten Dehnungsmessstreifen oder piezoelektrischen Sensoren, die die aktuelle Last in Echtzeit messen und per Bluetooth an einen Bordcomputer übertragen.

**Vorteile:**
- Echtzeit-Lastanzeige im Cockpit
- Aufzeichnung von Lastspitzen (Schock-Lasten)
- Ermüdungsberechnung basierend auf tatsächlichen Zyklen
- Warnung bei Überschreitung der SWL

**Nachteile:**
- Hoher Preis (3–5× Standard-Block)
- Batterie erforderlich (Lebensdauer begrenzt)
- Elektronik in Salzwasser-Umgebung
- Noch nicht in Serie verfügbar (Stand 2026)

**Anbieter:** Cyclops Marine (Lastmess-Schäkel, kompatibel mit Standard-Blöcken), Harken (Prototyp-Stadium), diverse Startups

#### T.1.2 Additive Fertigung (3D-Druck) von Hochlast-Blöcken

Titan-3D-Druck (Selective Laser Melting, SLM) ermöglicht geometrisch optimierte Block-Gehäuse, die mit konventioneller Fertigung nicht herstellbar wären.

**Vorteile:**
- Topologie-Optimierung: Material nur dort, wo Kraft fließt → 30–50% Gewichtsersparnis
- Keine Werkzeugkosten → wirtschaftlich bei Kleinserien
- Individuelle Anpassung an spezifische Einbausituationen

**Nachteile:**
- Hohe Stückkosten (€ 500–3.000 pro Block)
- Oberflächen-Nachbearbeitung erforderlich
- Begrenzte Materialauswahl (Ti6Al4V, 316L, Inconel)
- Prüfung/Zertifizierung aufwendig

**Anbieter:** Diverse Spezialisten im Superyacht-Segment, Southern Spars (Rigg-Beschläge)

#### T.1.3 Hybride Blöcke (Carbon + Titan)

Die neueste Generation von Racing-Blöcken kombiniert CFK-Seitenplatten mit Titan-Achsen und Torlon-Rollen. Diese Kombination bietet:

```
Gewichtsvergleich (75mm Einzelblock):
  Edelstahl (Garhauer):    550 g
  Aluminium (Harken Black): 425 g
  Carbon/Titan (Antal XT):  180 g → 67% leichter als Aluminium!
```

#### T.1.4 Keramik-Kugellager

Siliziumnitrid-Kugeln (Si3N4) in Edelstahl-Laufringen:
- Wirkungsgrad: 98–99%
- Korrosionsfrei (Kugeln)
- Höhere Härte → längere Lebensdauer
- Temperaturbeständig bis 1.000°C
- Preis: 5–10× Standard-Kugellager

**Einsatz:** Superyacht und Offshore-Racing, wo jedes Prozent Effizienz zählt.

### T.2 Zukunftsperspektiven

#### T.2.1 Vollautomatische Trimmsysteme

Elektrische Winschen in Kombination mit Lastmess-Blöcken und Segeltrimm-Algorithmen ermöglichen vollautomatisches Trimmen. Die Blöcke der Zukunft werden voraussichtlich:

- Integrierte Lastmessung als Standard haben
- Drahtlos mit dem Bordcomputer kommunizieren
- Verschleißüberwachung bieten (Lager-Zustand, Ermüdungs-Zyklen)
- Wartungserinnerungen automatisch generieren

#### T.2.2 Nachhaltige Materialien

Die Yacht-Industrie bewegt sich langsam in Richtung nachhaltigerer Materialien:
- Recyceltes Aluminium für Block-Gehäuse
- Bio-basierte Hochleistungskunststoffe für Rollen
- Flachs-Verbundwerkstoffe statt CFK (für nicht-kritische Anwendungen)
- Kreislaufwirtschaft: Hersteller-Rücknahme-Programme für alte Blöcke

---

## ANHANG U — Regatta-spezifische Anforderungen

### U.1 Klassenvorschriften und Block-Beschränkungen

Einige Regatta-Klassen beschränken die Art oder Anzahl der verwendeten Blöcke:

| Klasse | Beschränkung | Auswirkung auf Hochlast-Blöcke |
|--------|-------------|-------------------------------|
| ORC/IRC Rating | Keine direkte Beschränkung, aber Gewicht fließt ins Rating | Leichtere Blöcke = Rating-Vorteil |
| IMOCA 60 | Keine Beschränkung | Maximale Performance, Carbon/Titan Standard |
| Class 40 | Materialbeschränkungen im Bau | Blöcke frei wählbar |
| Mini 6.50 | Kostenbeschränkungen (Proto/Serie) | Serie: Budget-Blöcke, Proto: frei |
| J/70, J/80 etc. | One-Design: vorgeschriebene Blöcke | Nur Originalteile erlaubt |
| Volvo/The Ocean Race | Keine Beschränkung | Höchste Lasten, Custom-Lösungen |

### U.2 Regatta-Inspektions-Checkliste (ORC/RORC Offshore)

```
VOR JEDER OFFSHORE-REGATTA:
□ Alle Hochlast-Blöcke visuell inspiziert
□ Rollen-Freigängigkeit bestätigt
□ Schäkel-Bolzen gesichert (Kabelbinder/Draht)
□ Backing Plates geprüft (von innen)
□ Seil-Zustand an allen Block-Kontakten geprüft
□ Ersatz-Blöcke an Bord (min. 2× passende Einzelblöcke)
□ Ersatz-Schäkel an Bord (sortiert nach Größe)
□ Werkzeug für Block-Tausch an Bord
□ Inspektionsbefunde dokumentiert und unterschrieben
□ Bei Offshore: Prüfprotokoll dem Race Committee vorlegen
```

### U.3 Gewichtsoptimierung für Regatta

Gewichtsvergleich eines kompletten Hochlast-Block-Satzes für eine 12m Regattayacht:

| System | Standard (Edelstahl) | Performance (Alu) | Racing (Carbon/Titan) |
|--------|---------------------|-------------------|----------------------|
| Großschot 6:1 | 3.200 g | 2.100 g | 950 g |
| Vang 8:1 | 2.800 g | 1.800 g | 820 g |
| Backstag-Trimmer | 1.400 g | 900 g | 400 g |
| 2× Genuaschot-Turning | 1.100 g | 700 g | 320 g |
| Mastfuß-Organizer (5×) | 1.600 g | 1.050 g | 480 g |
| Spinnaker-Systeme | 1.800 g | 1.200 g | 550 g |
| **Gesamt** | **11.900 g** | **7.750 g** | **3.520 g** |
| **Einsparung vs. Standard** | — | **4.150 g (35%)** | **8.380 g (70%)** |
| **Kosten ca.** | **€ 2.000** | **€ 4.500** | **€ 12.000** |

**Kosten pro kg Einsparung:**
- Standard → Performance: € 4.500−€ 2.000 = € 2.500 / 4,15 kg = **€ 602/kg**
- Standard → Racing: € 12.000−€ 2.000 = € 10.000 / 8,38 kg = **€ 1.193/kg**
- Performance → Racing: € 12.000−€ 4.500 = € 7.500 / 4,23 kg = **€ 1.773/kg**

### U.4 Pre-Race Block-Service Protokoll

```
72h VOR DER REGATTA:
1. Alle Blöcke mit Süßwasser spülen
2. Trocknen lassen (12h)
3. Rollen ausbauen (bei zerlegbaren Blöcken)
4. Lager mit Isopropanol reinigen
5. Lager mit Harken OneDrop oder McLube Sailkote schmieren
6. Rollen wieder einbauen
7. Achsen mit dünnem Film Schmiermittel versehen
8. Seilrillen auf Grate prüfen (Fingernagel-Test)
9. Funktionstest aller Systeme unter Last
10. Schäkel-Bolzen mit Monel-Draht oder UV-beständigem Kabelbinder sichern
```

---

## ANHANG V — Spezielle Montagesituationen

### V.1 Mastfuß auf Deck (Deck-Stepped Mast)

Bei deckgesteppten Masten (häufig bei Fahrtenseglern) konzentrieren sich extreme Lasten am Mastfuß. Die Mastfuß-Blöcke müssen diese strukturelle Besonderheit berücksichtigen:

- **Lasteinleitung:** Mastlast (Kompressionskraft) geht durch das Deck in den Kiel-Bereich. Die Mastfuß-Platte verteilt diese Last. Blöcke in diesem Bereich dürfen die Mastfuß-Platte nicht schwächen.
- **Bolzen-Position:** Nicht durch die Mastfuß-Verstärkung bohren! Blöcke neben der Mastfuß-Platte montieren.
- **Seilwinkel:** Fallen kommen aus dem Mast nach unten und müssen zum Cockpit umgelenkt werden. Typische Winkel: 45–90°.

### V.2 Cockpit-Boden-Montage

Großschot-Systeme mit End-Boom-Führung und Cockpit-Boden-Block:

- **Drainage:** Block darf Cockpit-Drainage nicht blockieren
- **Ergonomie:** Block muss begehbar sein (Schutzkappe bei Nicht-Nutzung)
- **Lasteinleitung:** Cockpit-Boden ist oft dünner als das Hauptdeck → zusätzliche Verstärkung
- **Wasser:** Block steht permanent in Spritzwasser → Korrosionsschutz erhöht priorisieren

### V.3 Mast-interne Blöcke

Moderne Masten haben interne Fallen-Führung mit Cheek Blocks oder Exit Blocks am Mastfuß.

**Herausforderungen:**
- Zugang für Inspektion und Wartung sehr eingeschränkt
- Korrosion durch Kondenswasser im Mastprofil
- Seilstaub und Ablagerungen verstopfen Lager
- Ersatzteil-Beschaffung oft nur über Mast-Hersteller

**Wartungs-Empfehlung:**
- Jährlich: Fallen herausziehen und Block von außen inspizieren
- Alle 3 Jahre: Mast legen und interne Blöcke prüfen/schmieren
- Alle 8–10 Jahre: Interne Blöcke präventiv ersetzen

### V.4 Aluminium-Rumpf-Montage

Bei Aluminium-Yachten (z.B. Garcia, Allures, Boreal):

- **Keine galvanische Isolation nötig** bei Aluminium-Block auf Aluminium-Rumpf
- **Edelstahl-Bolzen in Aluminium:** Isolierbuchsen zwingend erforderlich!
- **Schweißbare Augenplatten:** Können direkt auf den Rumpf geschweißt werden → stärkste Befestigung
- **Elektrolyse-Risiko:** In der Bilge oder bei ständigem Wasserkontrakt erhöht → Opferanoden prüfen

### V.5 GFK-Rumpf mit Innenliner

Viele Serienyachten (Bavaria, Beneteau, Jeanneau) haben einen GFK-Innenliner, der im Deckbereich mit dem Außenlaminat verklebt ist.

**Problem:** Zwischen Außenlaminat und Innenliner befindet sich oft ein Hohlraum. Durchgangsbolzen finden keinen Halt im Innenliner.

**Lösungen:**
1. **Hohlraum mit Epoxid verfüllen** (beste Lösung, aber aufwendig)
2. **Lange Bolzen durch beide Schichten** mit Kompressionsröhrchen
3. **Backing Plate auf dem Innenliner** — nur wenn Innenliner strukturell angebunden ist
4. **Vermeidung:** Block auf Deck-Bereich montieren, der keinen Innenliner hat (z.B. Cockpit-Boden)

### V.6 Catamaran-spezifische Montage

Katamarane stellen besondere Anforderungen an Hochlast-Blöcke:

**Brücken-Deck (Trampolin-Bereich):**
- Großschot-Traveller oft auf dem Brücken-Deck zwischen den Rümpfen
- Extreme Belastung auf die Traveller-Schiene und deren Befestigung
- Brücken-Deck ist oft leichter gebaut als Rumpf-Deck → Verstärkung kritisch

**Höhere Lasten bei gleicher Größe:**
- Katamarane segeln aufrechter → weniger Krängungs-induzierte Entlastung
- Effektive Segelfläche ist größer (kein Heel-Faktor)
- Großschot-Lasten können 1,3–1,5× höher sein als bei vergleichbarem Monohull

**Besonderheiten:**
- Daggerboard-Fallen/-Strecker: Hochlast-Anwendung, oft übersehen
- Traveller-Schienen: Müssen breiter sein als bei Monohulls
- Cockpit-Organizer: Oft 8–10 Rollen erforderlich (beide Rümpfe + Brücken-Systeme)

| System | Monohull 12m | Katamaran 12m | Faktor |
|--------|-------------|---------------|--------|
| Großschot-Last (20 kt) | 2.560 kg | 3.840 kg | 1,5× |
| Backstag-Last | 2.500 kg | — (meist kein Backstag) | — |
| Genuaschot | 1.800 kg | 2.700 kg | 1,5× |
| Spinnaker/Gennaker | 2.000 kg | 3.000 kg | 1,5× |
| Daggerboard-Strecker | — | 1.500–4.000 kg | Nur Katamaran |

### V.7 Multihull-Sicherheitsaspekte

Bei Katamaranen und Trimaranen ist das Kentern (Kapseln) ein reales Risiko. Hochlast-Block-Versagen unter Extremlast kann zum Kontrollverlust und damit zum Kapseln führen.

**Erhöhte Sicherheitsfaktoren für Multihulls:**
- Großschot: SF 4:1 (statt 3:1 bei Monohull)
- Traveller: SF 5:1 (Totalversagen → sofortiger Kontrollverlust)
- Daggerboard-Systeme: SF 4:1

**Schnell-Entlastungssysteme:**
- Großschot mit Ratchet-Block und Schnellöffner (Cam Cleat)
- Traveller mit Schnellöffner (Trigger Release)
- Automatische Entlastung bei Überlast (Friction Clutch statt fester Klemme)

---

## ANHANG W — Erfahrungswerte und Praxis-Tipps

### W.1 Die häufigsten Fehler bei Hochlast-Blöcken

| Rang | Fehler | Häufigkeit | Konsequenz |
|------|--------|-----------|-----------|
| 1 | Schraubbefestigung statt Durchgangsbolzen | Sehr häufig | Ausriss unter Last |
| 2 | Keine Backing Plate | Häufig | Deck-Schaden, Ausriss |
| 3 | Falsche Seilgröße (zu dünn oder zu dick) | Häufig | Klemmen oder übermäßiger Verschleiß |
| 4 | Keine galvanische Isolation | Häufig | Korrosion, Block sitzt fest |
| 5 | Zu kleine Block-Klasse | Mäßig häufig | Überlast, Lager-/Achsschaden |
| 6 | Fehlende Kernverstärkung (Sandwich-Deck) | Mäßig häufig | Kern-Quetschung, Spiel |
| 7 | Keine Wartung/Schmierung | Sehr häufig | Effizienz-Verlust, Lagerschaden |
| 8 | Schäkel-Bolzen nicht gesichert | Mäßig häufig | Verlust bei Regatta |
| 9 | Falsche Ausrichtung (Deck-Organizer) | Gelegentlich | Schwergängigkeit, Seilschaden |
| 10 | Alte Blöcke nicht ersetzt (>15 Jahre) | Häufig | Ermüdungsbruch-Risiko |

### W.2 Praxis-Tipps von erfahrenen Riggers

**Tipp 1: Trockenmontage**
Vor dem endgültigen Einbau immer eine Trockenmontage (ohne Dichtstoff) durchführen. Block aufsetzen, Seil einlegen, unter Last prüfen. Erst wenn alles passt: endgültige Montage mit Dichtstoff.

**Tipp 2: Seil-Durchführung markieren**
Bei Deck-Organizern und Mastfuß-Blöcken: Die Seil-Zuordnung mit farbigen Markierungen am Block kennzeichnen. Erspart Verwechslungen beim Segeln.

**Tipp 3: Ersatzteile an Bord**
Für Langfahrt: Mindestens 2× universal-passende Hochlast-Einzelblöcke an Bord haben. Dazu passende Schäkel, Bolzen und Backing Plates. Ein kaputter Block auf See kann jedes System lahmlegen.

**Tipp 4: Fotos bei der Montage**
Die Montage von Hochlast-Blöcken fotografisch dokumentieren — besonders die Backing Plates und Kernverstärkungen. Nach dem Einbau sind diese nicht mehr sichtbar, aber bei einer späteren Inspektion oder Demontage sind die Fotos Gold wert.

**Tipp 5: Drehmomente notieren**
Die Anzieh-Drehmomente der Bolzen auf einem Aufkleber an der Backing Plate oder im Bordbuch notieren. Bei der jährlichen Kontrolle kann dann auf das korrekte Drehmoment nachgezogen werden.

**Tipp 6: Lager-Service im Winter**
Die ideale Zeit für Lager-Service ist die Einwinterung. Blöcke sind trocken, es gibt keinen Zeitdruck, und die Lager haben über den Winter Zeit, das Schmiermittel aufzunehmen.

**Tipp 7: Korrosionsschutz bei Langfahrt**
In tropischen Gewässern: Alle Aluminium-Blöcke alle 3 Monate mit Boeshield T-9 einsprühen. Schäkel-Bolzen mit Lanolin (Lanocote) einfetten. Galvanische Kontaktstellen regelmäßig prüfen.

---

*Ende der Wissensdatei 10.04 — Hochlast-Blöcke und Umlenkrollen*
*AYDI Research, Version 1.0.0, 2026-04-25*
*Status: validated*