---
title: "Blöcke Grundlagen und Typen im Yachtbau"
kategorie: "10 Blöcke und Umlenkrollen"
unterkategorie: "01 Grundlagen"
version: "1.0.0"
datum: "2026-04-25"
autor: "AYDI Research"
status: "validated"
confidence_quellen:
  - measured: "Hersteller-Datenblätter, Laborprüfungen"
  - documented: "Hersteller-Kataloge, Segelfachpresse, Forum-Konsens"
  - estimated: "Erfahrungswerte, Quervergleiche"
  - benchmark: "Marktdurchschnitte, Branchenstandards"
tags:
  - blöcke
  - umlenkrollen
  - rigg
  - flaschenzug
  - talje
  - beschläge
  - laufendes_gut
  - deck_hardware
boot_klassen:
  - jolle (4–8m)
  - fahrtensegler (8–14m)
  - performance_cruiser (10–16m)
  - blauwasseryacht (12–18m)
  - regattayacht (8–20m)
  - motoryacht (8–25m)
  - superyacht (18m+)
---

# 10.01 — Blöcke Grundlagen und Typen im Yachtbau: Vollständige Wissensreferenz

> **AYDI Wissensdatei 10.01** — Kategorie 10: Blöcke und Umlenkrollen
> **Confidence-Quelle:** measured (Hersteller-TDS), documented (Hersteller-Kataloge, Fachliteratur), estimated (Erfahrungswerte)
> **Letzte Aktualisierung:** 2026-04-25

---

## Inhaltsverzeichnis

1. [Einführung und Übersicht](#1-einführung-und-übersicht)
2. [Grundlagen und Theorie](#2-grundlagen-und-theorie)
3. [Typenübersicht](#3-typenübersicht)
4. [Materialien und Konstruktion](#4-materialien-und-konstruktion)
5. [Dimensionierung und Auswahl](#5-dimensionierung-und-auswahl)
6. [Hersteller-Übersicht](#6-hersteller-übersicht)
7. [Anlagen-spezifische Zuordnung](#7-anlagen-spezifische-zuordnung)
8. [Fehlerbild-Atlas](#8-fehlerbild-atlas)
9. [Troubleshooting-Entscheidungsbaum](#9-troubleshooting-entscheidungsbaum)
10. [FAQ — Häufige Fragen](#10-faq--häufige-fragen)
11. [Glossar](#11-glossar)
12. [Schnell-Referenz](#12-schnell-referenz)
13. [ANHANG A — Fallstudien](#anhang-a--fallstudien)
14. [ANHANG B — AYDI-Integration (Pydantic-Modelle)](#anhang-b--aydi-integration-pydantic-modelle)
15. [ANHANG C — Normen und Standards](#anhang-c--normen-und-standards)
16. [ANHANG D — Lasttabellen](#anhang-d--lasttabellen)
17. [ANHANG E — Confidence-Mapping](#anhang-e--confidence-mapping)
18. [ANHANG F — Wartungsintervalle](#anhang-f--wartungsintervalle)
19. [ANHANG G — Historische Entwicklung](#anhang-g--historische-entwicklung)
20. [ANHANG H — Bezugsquellen](#anhang-h--bezugsquellen)
21. [ANHANG I — Herstellervergleich Detailtabellen](#anhang-i--herstellervergleich-detailtabellen)
22. [ANHANG J — Blockauswahl-Algorithmus](#anhang-j--blockauswahl-algorithmus)
23. [ANHANG K — Prüfprotokolle](#anhang-k--prüfprotokolle)
24. [ANHANG L — Visuelle Analyse-Referenz](#anhang-l--visuelle-analyse-referenz)
25. [ANHANG M — Schmierstoff-Kompatibilität](#anhang-m--schmierstoff-kompatibilität)
26. [ANHANG N — Retrofit-Leitfaden](#anhang-n--retrofit-leitfaden)
27. [ANHANG O — Regatta-Spezifikationen](#anhang-o--regatta-spezifikationen)
28. [ANHANG P — Superyacht-Sonderlösungen](#anhang-p--superyacht-sonderlösungen)
29. [ANHANG Q — Umrechnungstabellen](#anhang-q--umrechnungstabellen)
30. [ANHANG R — Checklisten](#anhang-r--checklisten)

---

## 1. Einführung und Übersicht

### 1.1 Was sind Blöcke?

Blöcke (englisch: blocks, pulleys) sind fundamentale mechanische Bauteile im Rigg- und Deckssystem von Segelyachten. Sie dienen der Umlenkung, Untersetzung und Führung von Tauwerk (Schoten, Fallen, Streckern, Reffleinen) und ermöglichen es dem Segler, die enormen Kräfte des Windes mit menschlicher Muskelkraft zu kontrollieren.

Ein Block besteht in seiner Grundform aus drei Komponenten:

- **Scheibe (Sheave)**: Die drehbare Rolle, über die das Tauwerk läuft
- **Wangen (Cheeks)**: Die seitlichen Gehäuseteile, die die Scheibe umschließen
- **Achse mit Lagerung (Bearing/Axle)**: Die zentrale Drehachse mit Lagertechnik
- **Befestigungselemente**: Schäkel, Hundsfott, Bügel oder direkte Verschraubung

### 1.2 Bedeutung im Segelsystem

Auf einer modernen 12-Meter-Fahrtenyacht befinden sich typischerweise 25–45 Blöcke. Auf einer Regattayacht gleicher Größe können es 60–100+ sein. Jeder einzelne Block ist Teil einer Kraftkette, und das Versagen eines einzigen Blocks kann zum Kontrollverlust über ein Segel, zur Beschädigung des Riggs oder — im schlimmsten Fall — zu Personenschäden führen.

Die Gesamtkosten für Blöcke einer 40-Fuß-Fahrtenyacht liegen typischerweise bei:

| Bootsklasse | Blockanzahl | Kostenbereich (EUR) |
|-------------|-------------|---------------------|
| Jolle (4–8m) | 8–15 | 200–800 |
| Fahrtensegler (8–14m) | 25–45 | 1.500–5.000 |
| Performance Cruiser (10–16m) | 35–60 | 3.000–12.000 |
| Blauwasseryacht (12–18m) | 30–50 | 2.500–8.000 |
| Regattayacht (8–20m) | 60–100+ | 5.000–30.000 |
| Superyacht (18m+) | 50–150+ | 15.000–100.000+ |

### 1.3 Historische Entwicklung

Die Geschichte des Blocks im Segeln reicht Jahrtausende zurück:

**Antike (3000 v. Chr. – 500 n. Chr.):**
Erste dokumentierte Verwendung von Umlenkrollen in der ägyptischen und phönizischen Seefahrt. Einfache Holzscheiben auf Holzachsen, geschmiert mit Tierfett. Hauptsächlich für Fallen und einfache Schot-Führung.

**Zeitalter der Entdeckungen (1400–1700):**
Entwicklung komplexer Taljensysteme für Großsegler. Lignum-vitae-Holz (Guajakholz) als bevorzugtes Scheibenmaterial wegen seiner selbstschmierenden Eigenschaften. Ein Dreimaster des 17. Jahrhunderts trug 200–400 Blöcke. Die Blockherstellung war einer der größten Industriezweige Englands — die Blockmills in Portsmouth (ab 1803, Marc Isambard Brunel) waren die erste Massenproduktion der Welt.

**Industriezeitalter (1800–1950):**
Übergang zu Metallachsen und schließlich Kugellagern. Bronze- und Messingblöcke für die Yachtfahrt. Erste standardisierte Blockgrößen.

**Moderne Ära (1950–heute):**
- 1960er: Einführung von Kunststoff-Scheiben (Delrin/Acetal)
- 1970er: Peter Harken revolutioniert den Blockbau mit dem ersten selbstklemmenden Block und später dem Carbo-System
- 1980er: Kugellager-Blöcke werden Standard, Ratschenblöcke für Großschot
- 1990er: Hochleistungs-Keramiklager, Kohlefaser-Wangen
- 2000er: Orbit-Technologie (Ronstan), T2 (Harken), Loop-Systeme
- 2010er+: Integration von Textil-Dyneema-Blöcken, Low-Friction-Ringe als Alternative

### 1.4 Abgrenzung: Block vs. Klemme vs. Low-Friction-Ring

Blöcke sind nicht die einzige Möglichkeit, Tauwerk umzulenken:

| Element | Reibung | Lastbereich | Gewicht | Preis | Einsatz |
|---------|---------|-------------|---------|-------|---------|
| Block (Kugellager) | 2–3% | Hoch | Mittel | Hoch | Standard |
| Block (Gleitlager) | 5–8% | Mittel | Gering | Gering | Budget |
| Low-Friction-Ring | 3–5% | Mittel | Sehr gering | Mittel | Gewichtsoptimiert |
| Bullaugenführung | 10–15% | Gering | — | Gering | Statische Umlenkung |
| Leitöse | 15–25% | Gering | Sehr gering | Gering | Einfache Führung |

Low-Friction-Ringe (z. B. Antal LFR, Ronstan Orbit Blocks) haben in den letzten Jahren insbesondere im Regattabereich Marktanteile gewonnen. Für hochbelastete Anwendungen (Großschot, Genuaschot, Fallen) bleiben konventionelle Blöcke jedoch Standard.

---

## 2. Grundlagen und Theorie

### 2.1 Mechanischer Vorteil (Untersetzung)

Das Grundprinzip des Flaschenzugs: Durch die Umlenkung über Scheiben wird die erforderliche Zugkraft reduziert, während der Zugweg proportional zunimmt.

**Formel für den idealen mechanischen Vorteil:**

```
MA = n (Anzahl tragender Parten)
```

**Formel für den realen mechanischen Vorteil (mit Reibung):**

```
MA_real = (1 - μ^n) / (1 - μ)

wobei:
  μ = Reibungskoeffizient pro Scheibe (Verlustfaktor = 1 - Wirkungsgrad)
  n = Anzahl der Scheiben
```

### 2.2 Reibungskoeffizienten nach Lagertyp

| Lagertyp | Reibungskoeffizient | Wirkungsgrad pro Scheibe | Typische Anwendung |
|----------|--------------------|--------------------------|--------------------|
| Kugellager (ball bearing) | 0,02 (2%) | 98% | Hochlast, Standard |
| Nadellager (needle bearing) | 0,03 (3%) | 97% | Mittellast |
| Gleitlager Delrin (plain bearing) | 0,05–0,08 (5–8%) | 92–95% | Niedriglast, Budget |
| Keramik-Hybridlager | 0,015 (1,5%) | 98,5% | Regatta-Hochleistung |
| Torlon-Gleitlager | 0,04 (4%) | 96% | Mittellast, salzwassertolerant |
| Dyneema-Loop | 0,03–0,05 (3–5%) | 95–97% | Ultraleicht, Offshore-Regatta |

**Confidence:** measured (Herstellerangaben Harken, Ronstan)

### 2.3 Wirkungsgrad-Kaskade in Mehrschiebensystemen

Bei jedem Durchlauf durch eine Scheibe geht Energie durch Reibung verloren. In einem Flaschenzug mit mehreren Scheiben multiplizieren sich die Verluste:

**Gesamtwirkungsgrad:**

```
η_gesamt = η_1 × η_2 × η_3 × ... × η_n
```

**Beispiel: 4:1-Talje mit Kugellagern (η = 0,98 pro Scheibe):**

```
η_gesamt = 0,98^4 = 0,922 = 92,2%
Tatsächlicher mechanischer Vorteil: 4 × 0,922 = 3,69:1
```

**Beispiel: 4:1-Talje mit Gleitlagern (η = 0,93 pro Scheibe):**

```
η_gesamt = 0,93^4 = 0,748 = 74,8%
Tatsächlicher mechanischer Vorteil: 4 × 0,748 = 2,99:1
```

### 2.4 Wirkungsgrad-Tabelle nach Untersetzung und Lagertyp

| Untersetzung | Scheiben | Kugellager (98%) | Nadellager (97%) | Gleitlager (93%) |
|-------------|----------|------------------|------------------|-------------------|
| 2:1 | 1 | 1,96 | 1,94 | 1,86 |
| 3:1 | 2 | 2,88 | 2,82 | 2,60 |
| 4:1 | 3 | 3,76 | 3,65 | 3,22 |
| 6:1 | 5 | 5,42 | 5,17 | 4,22 |
| 8:1 | 7 | 6,93 | 6,47 | 4,86 |
| 10:1 | 9 | 8,34 | 7,60 | 5,20 |
| 12:1 | 11 | 9,65 | 8,57 | 5,28 |

**Erkenntnis:** Ab 8:1-Untersetzung mit Gleitlagern ist der Wirkungsverlust so groß, dass Kugellager zwingend erforderlich werden. Die theoretische 12:1-Untersetzung mit Gleitlagern liefert effektiv nur 5,28:1.

### 2.5 Lastberechnung: Stehende und laufende Part

**Definitionen:**

- **Stehende Part (standing part):** Das Ende des Tauwerks, das an einem festen Punkt befestigt ist
- **Laufende Part (running/hauling part):** Das Ende, an dem gezogen wird
- **Arbeitslast (Working Load Limit, WLL):** Die maximale Last im Dauerbetrieb
- **Bruchlast (Breaking Load, BL):** Die Last bei Versagen

**Lastverteilung im Flaschenzug:**

```
Last an der laufenden Part:
F_hauling = F_load / MA_real

Last an der Befestigung (Kopfblock):
F_head = F_load + F_hauling = F_load × (1 + 1/MA_real)

Bei 2:1 mit Kugellager:
F_head = F_load × (1 + 1/1,96) = F_load × 1,51
```

### 2.6 Untersetzungssysteme (Purchase Systems)

#### 2:1-Talje (Handy Billy)

```
    ┌─ Festpunkt
    │
   [Block]
    │  │
    │  └── laufende Part
    │
    └── Last
```

- Scheiben: 1
- Zugweg-Multiplikator: 2×
- Typische Anwendung: Baumniederholer, einfache Strecker, Dirk

#### 3:1-Talje

```
    ┌─ Festpunkt
    │
   [Block]──┐
    │        │
   [Block]   │
    │  │     │
    │  └─────┘
    │
    └── Last
```

- Scheiben: 2
- Zugweg-Multiplikator: 3×
- Typische Anwendung: Cunningham, Baumniederholer (Jolle)

#### 4:1-Talje

- Scheiben: 3 (typisch: Doppelblock oben, Einzelblock unten)
- Zugweg-Multiplikator: 4×
- Typische Anwendung: Großschot (Jolle), Achterstag-Spanner

#### 6:1-Talje

- Scheiben: 5 (Dreifachblock + Doppelblock)
- Zugweg-Multiplikator: 6×
- Typische Anwendung: Großschot (kleine Kielboote), Genuaschot-Feintrimmung

#### 8:1-Talje (Cascading)

- Oft als 4:1 × 2:1 Kaskade realisiert
- Scheiben: 5–7
- Typische Anwendung: Großschot (Fahrtenyacht 10–14m)

#### 12:1-Talje

- Als 4:1 × 3:1 oder 6:1 × 2:1 Kaskade
- Scheiben: 7–11
- Typische Anwendung: Großschot (große Yacht), Backstag-Spanner

### 2.7 Kaskadierende Taljesysteme

Für hohe Untersetzungen ist es effizienter, zwei separate Taljensysteme hintereinander zu schalten (Kaskade) als ein einzelnes System mit vielen Scheiben:

**Vorteile der Kaskade:**
- Weniger Gesamtreibung (Weg durch weniger Scheiben pro Teilsystem)
- Einfacherer Aufbau und Wartung
- Schnelleres Dichtholen durch Entkopplung des Grobholens

**Beispiel: 12:1 als Kaskade vs. Direktsystem:**

| Methode | Scheiben | η (Kugellager) | Realer MA |
|---------|----------|----------------|-----------|
| Direkt 12:1 | 11 | 0,98^11 = 0,80 | 9,6 |
| 4:1 × 3:1 Kaskade | 3+2 = 5 | 0,98^3 × 0,98^2 = 0,90 | 10,8 |
| 6:1 × 2:1 Kaskade | 5+1 = 6 | 0,98^5 × 0,98 = 0,89 | 10,6 |

Die Kaskade mit 5 Scheiben liefert einen höheren realen mechanischen Vorteil als das Direktsystem mit 11 Scheiben.

### 2.8 Scheiben-Geometrie

Die Geometrie der Scheibe beeinflusst Leistung, Tauwerk-Lebensdauer und Blockgröße:

**Scheibendurchmesser zu Tauwerk-Durchmesser:**

| Tauwerk-Typ | Verhältnis D_Scheibe : d_Tauwerk | Minimum | Optimal |
|-------------|-----------------------------------|---------|---------|
| Draht (Wire) | 8:1 | 6:1 | 10:1 |
| Draht mit Textilmantel | 6:1 | 5:1 | 8:1 |
| Flechtleine (Polyester) | 4:1 | 3:1 | 6:1 |
| Dyneema/Spectra (HMPE) | 5:1 | 4:1 | 8:1 |
| Vectran | 5:1 | 4:1 | 7:1 |
| Aramid (Kevlar/Technora) | 6:1 | 5:1 | 8:1 |

**Warum das Verhältnis wichtig ist:**
- Zu kleine Scheibe → übermäßige Biegung des Tauwerks → Kernbruch bei HMPE, Mantelabrieb
- Zu große Scheibe → unnötiges Gewicht und Kosten
- HMPE-Leinen (Dyneema) sind besonders empfindlich gegenüber kleinen Biegeradien

**Rillenprofile:**

| Profil | Beschreibung | Anwendung |
|--------|-------------|-----------|
| V-Rille | Konische Rille, 30–45° | Standard für geflochtenes Tauwerk |
| U-Rille | Halbkreisförmig | Draht, dickere Leinen |
| Flach | Minimal konkav | Flachband (Webbing), Dyneema-Litzen |

### 2.9 Umlenkwinkel und Reibung

Der Umlenkwinkel des Tauwerks am Block beeinflusst sowohl die Reibung als auch die Belastung des Blocks:

**Effektive Last auf den Block:**

```
F_block = 2 × F_leine × sin(α/2)

wobei α = Umlenkwinkel (180° = volle Umkehr)
```

| Umlenkwinkel | Lastfaktor | Beispiel: 500 daN Leinenzug |
|-------------|------------|---------------------------|
| 180° (Umkehr) | 2,00 | 1.000 daN Blocklast |
| 150° | 1,93 | 966 daN |
| 120° | 1,73 | 866 daN |
| 90° | 1,41 | 707 daN |
| 60° | 1,00 | 500 daN |
| 45° | 0,77 | 383 daN |
| 30° | 0,52 | 259 daN |

**Praxisregel:** Ein Umlenkblock, der eine Schot um 90° umlenkt, trägt das 1,41-fache der Schotlast. Ein Block in einer Talje (180°) trägt die doppelte Leinenlast.

### 2.10 Dynamische Lasten

Statische Lastberechnungen allein genügen nicht. Im Segelbetrieb treten dynamische Lastspitzen auf:

| Situation | Lastfaktor (×statisch) | Dauer |
|-----------|----------------------|-------|
| Normales Segeln | 1,0× | Dauerhaft |
| Böe (Windzunahme 50%) | 1,5–2,0× | Sekunden |
| Halse (Groß) | 2,0–3,0× | < 1 Sekunde |
| Spi-Gennaker füllt plötzlich | 3,0–5,0× | < 1 Sekunde |
| Blockierung/Klemmen | 5,0–10,0× | Variabel |
| Rigg-Bruch/Peitscheneffekt | 10,0+× | Millisekunden |

**Sicherheitsfaktor-Empfehlung:**

```
SWL (Safe Working Load) = BL (Breaking Load) / SF (Safety Factor)

Fahrtenyacht: SF = 4:1 (BL = 4 × Arbeitslast)
Regattayacht: SF = 3:1 (akzeptiert höheres Risiko)
Charter/Ausbildung: SF = 5:1 (erhöhte Sicherheit)
Superyacht/gewerblich: SF = 5:1 bis 6:1 (Vorschrift)
```

### 2.11 Schot- und Fallkräfte nach Bootsklasse

Typische maximale Kräfte im Betrieb (gemessen, Windstärke 6 Bft):

| Anlage | Jolle (5m) | Fahrten (10m) | Fahrten (13m) | Perf. (13m) | Blauws. (15m) |
|--------|-----------|---------------|---------------|-------------|----------------|
| Großschot | 200 daN | 600 daN | 1.000 daN | 1.200 daN | 1.500 daN |
| Genuaschot | 150 daN | 800 daN | 1.400 daN | 1.800 daN | 2.200 daN |
| Spi-Schot | 100 daN | 500 daN | 900 daN | 1.200 daN | 1.500 daN |
| Großfall | 300 daN | 800 daN | 1.500 daN | 2.000 daN | 2.500 daN |
| Vorsegel-Fall | 250 daN | 700 daN | 1.200 daN | 1.600 daN | 2.000 daN |
| Spi-Fall | 150 daN | 400 daN | 700 daN | 1.000 daN | 1.200 daN |
| Baumniederholer | 200 daN | 500 daN | 800 daN | 1.200 daN | 1.200 daN |
| Reffleinen | — | 400 daN | 700 daN | 900 daN | 1.000 daN |
| Backstag | — | 600 daN | 1.000 daN | 1.500 daN | 2.000 daN |
| Achterstag | — | 300 daN | 500 daN | 800 daN | 1.000 daN |

**Confidence:** measured (Werte aus Rigg-Monitoring-Systemen, gemittelt)

---

## 3. Typenübersicht

### 3.1 Einfachblock (Single Block)

**Beschreibung:** Ein Block mit einer einzelnen Scheibe. Der universellste Blocktyp.

**Aufbau:**
- 1 Scheibe
- 2 Wangen (oder geschlossenes Gehäuse)
- Befestigung oben: Schäkel, Hundsfott, Bügel, oder Fixierung
- Optional: Hundsfott (Becket) unten für stehende Part

**Typische Anwendungen:**
- Umlenkung von Schoten und Fallen
- Einzelne Part in Taljensystemen
- Decksblock für Leinenführung
- Mastblock (Fallumlenkung am Masttop)

**Varianten:**
- Mit Schäkel (Swivel) — drehbare Kopfbefestigung
- Mit Hundsfott (Becket) — Befestigungspunkt für stehende Part
- Mit Kausch (Thimble) — für textile Befestigung
- Stehend (Standing) — fest montiert

**Größenbereich:**
| Leinendurchmesser | Scheibendurchmesser | Bruchlast (typisch) |
|-------------------|--------------------|--------------------|
| 4–6 mm | 16–25 mm | 300–600 daN |
| 6–8 mm | 25–38 mm | 600–1.200 daN |
| 8–10 mm | 38–50 mm | 1.200–2.500 daN |
| 10–12 mm | 50–57 mm | 2.500–4.000 daN |
| 12–14 mm | 57–75 mm | 4.000–6.000 daN |
| 14–18 mm | 75–100 mm | 6.000–12.000 daN |

> ⚠️ **ZU PRÜFEN (Audit):** Diese "Bruchlast (typisch)"-Werte überschneiden sich betragsmäßig mit den als "Typische SWL" bezeichneten Werten in Abschnitt 5.2 (z. B. 1.200–2.500 daN) — die Kennzeichnung SWL/WLL vs. Bruchlast ist zwischen den Tabellen uneinheitlich. Für einen 57-mm-Block nennt ANHANG I.1 Bruchlasten von 1.200–3.800 daN bei WLL 300–950 daN. Last-/sicherheitskritisch: **estimated — unverifiziert**, maßgeblich ist das jeweilige Hersteller-Datenblatt.

### 3.2 Doppelblock (Double Block)

**Beschreibung:** Block mit zwei nebeneinander oder übereinander angeordneten Scheiben.

**Anwendung:**
- Oberer Block einer 3:1- oder 4:1-Talje
- Großschot-Systeme
- Parallele Leinenführung

**Varianten:**
- Nebeneinander (side-by-side) — für parallele Leinen
- Übereinander (stacked/fiddle) — für Taljensysteme

**Vorteile gegenüber zwei Einzelblöcken:**
- Kompakter
- Leichter
- Keine Verdrehungsgefahr der Talje
- Bessere Lastverteilung auf eine Befestigung

### 3.3 Dreifachblock (Triple Block)

**Beschreibung:** Block mit drei Scheiben. Seltener im Yachtbau, aber für hohe Untersetzungen.

**Anwendung:**
- Teil einer 6:1-Talje (Dreifach + Dreifach)
- Großschot auf großen Yachten
- Klassische Yachten (traditioneller Look)

**Hinweis:** In der modernen Yachtpraxis werden Dreifachblöcke zunehmend durch kaskadierende Systeme oder Winschen ersetzt.

### 3.4 Violinblock (Fiddle Block)

**Beschreibung:** Zwei Scheiben unterschiedlicher Größe übereinander in einem Gehäuse. Die größere Scheibe oben nimmt die höhere Last auf.

**Aufbau:**
- Große Scheibe oben (höhere Last)
- Kleine Scheibe unten (geringere Last, laufende Part)
- Gemeinsame Achse oder getrennte Achsen
- Oft mit integriertem Klemmer (Cam Cleat) an der unteren Scheibe

**Anwendung:**
- Standard-Großschotsystem auf Jollen und kleinen Kielbooten
- Genuaschot-Feintrimmung
- Überall dort, wo eine Talje mit Klemmer benötigt wird

**Vorteil:** Der Violinblock verhindert, dass sich die Leinen zwischen den Scheiben verklemmen (im Gegensatz zu einem Doppelblock mit gleich großen Scheiben).

### 3.5 Ratschenblock (Ratchet Block)

**Beschreibung:** Ein Block mit integrierter Ratsche (Freilaufkupplung), die in einer Richtung freien Lauf ermöglicht und in der anderen Richtung das Tauwerk klemmt. Dies ermöglicht dem Segler, die Schot ohne permanenten Zug zu halten.

**Funktionsprinzip:**
- Beim Dichtholen dreht sich die Scheibe frei (minimale Reibung)
- Beim Nachlassen greift die Ratsche und erhöht die Reibung drastisch
- Der Segler kann die Last mit einem Bruchteil der Kraft halten
- Effektive Haltekraft-Reduktion: 5:1 bis 10:1

**Anwendung:**
- Großschot auf Jollen und Sportbooten (insbesondere bei Trapez-Segeln)
- Spinnaker-Schot
- Jede Schot, die unter Last gehalten werden muss

**Varianten:**
- Automatik-Ratsche: Greift bei Lastzunahme automatisch
- Schaltbare Ratsche: Kann ein-/ausgeschaltet werden
- Doppel-Ratsche: Zwei unabhängige Ratschen für zwei Scheiben

**Nachteile:**
- Höheres Gewicht als Standardblöcke
- Höherer Preis (2–4× gegenüber Standardblock)
- Ratschenmechanismus kann verschleißen/korrodieren
- Typisches Klickgeräusch

**Marktführer:** Harken (Erfinder des modernen Ratschenblocks)

**Größenübersicht Ratschenblöcke:**

| Modell (Harken) | Leine | Bruchlast | Gewicht | Preis (ca.) |
|----------------|-------|-----------|---------|-------------|
| 40mm Carbo Ratchamatic | 6–10 mm | 1.500 daN | 128 g | 80 EUR |
| 57mm Carbo Ratchamatic | 8–12 mm | 2.500 daN | 277 g | 140 EUR |
| 75mm Ratchamatic | 10–14 mm | 5.000 daN | 570 g | 250 EUR |
| 57mm T2 Ratchet | 8–12 mm | 3.000 daN | 230 g | 200 EUR |

### 3.6 Snatchblock (Schnappblock)

**Beschreibung:** Ein Block, dessen Wange sich öffnen lässt, sodass eine Leine seitlich eingelegt werden kann, ohne dass ein Leinenende durchgefädelt werden muss.

**Funktionsprinzip:**
- Eine Wange ist als Schnappverschluss, Drehverriegelung oder Schieber ausgeführt
- Öffnung gegen Federkraft oder Verriegelung
- Leine wird seitlich in die geöffnete Rille eingelegt
- Block schließt sich und funktioniert wie ein normaler Block

**Anwendung:**
- Rettungsmanöver (Leine schnell umlenken)
- Flexible Schot-Verlegung
- Leinenführung, die häufig geändert wird
- Ankerwinschen-Umlenkung
- Berge- und Schleppmanöver

**Sicherheitshinweis:** Snatchblöcke müssen sicher verriegeln. Ein versehentliches Öffnen unter Last kann zum Peitscheneffekt führen.

**Bewertung nach Bootsklasse:**

| Bootsklasse | Empfehlung | Anzahl an Bord |
|-------------|-----------|----------------|
| Jolle | Optional | 0–1 |
| Fahrtensegler | Empfohlen | 2–4 |
| Blauwasseryacht | Zwingend | 4–6 |
| Regattayacht | Situativ | 1–3 |
| Motoryacht | Empfohlen | 2–4 |

### 3.7 Orbitblock (Orbit Block)

**Beschreibung:** Ein revolutionäres Blockdesign von Ronstan (patentiert), bei dem sich die Scheibe sowohl um die zentrale Achse als auch orbital um den Befestigungspunkt dreht. Dies ermöglicht eine automatische Ausrichtung auf die Leinenzugrichtung.

**Funktionsprinzip:**
- Die Scheibe ist nicht in festen Wangen gelagert
- Stattdessen schwebt sie in einem Ring oder Käfig
- Sie kann sich in jede Richtung ausrichten
- Selbstausrichtung minimiert seitliche Reibung

**Vorteile:**
- Reduzierte Reibung bei nicht-idealen Leinenführungen
- Kompakte Bauform
- Geringeres Gewicht (kein separater Wirbel nötig)
- Weniger Verschleiß am Tauwerk

**Anwendung:**
- Decksblöcke für vielfältige Leinenführung
- Fallen-Umlenkung
- Überall dort, wo der Leinenwinkel variiert

### 3.8 Carbo-Block

**Beschreibung:** Harkens Markenname für ihre Composite-Block-Serie aus glasfaserverstärktem Polymer. Leicht, preiswert und korrosionsbeständig.

**Eigenschaften:**
- Wangen aus glasfaserverstärktem Nylon
- Delrin-Scheiben (Standard) oder Kugellager
- UV-stabilisiert
- Schwimmfähig (einige Modelle)
- Geringes Gewicht

**Positionierung:**
- Einstiegs- und Mittelklasse-Segment
- Standard-Ausstattung vieler Serienyachten
- Preis: 30–60% günstiger als Aluminium-/Edelstahl-Blöcke

**Grenzen:**
- Geringere Bruchlast als Metall-Blöcke gleicher Größe
- UV-Alterung bei Dauerexposition (5–10 Jahre)
- Nicht für Superyacht-Anwendungen

### 3.9 Flip-Flop-Block

**Beschreibung:** Ein Block, der seitlich umgelegt werden kann, um die Leine einzuführen. Ähnlich dem Snatchblock, aber mit einem anderen Öffnungsmechanismus.

**Funktionsprinzip:**
- Eine Seitenplatte klappt um 180° zur Seite
- Leine wird eingelegt
- Seitenplatte klappt zurück und verriegelt

**Anwendung:**
- Spinnaker-Schoten
- Lazy-Jacks
- Anwendungen mit häufigem Leinenwechsel

### 3.10 Wangenblock (Cheek Block)

**Beschreibung:** Ein flacher Block, der direkt auf einer Oberfläche (Deck, Mast, Baum) montiert wird. Keine hängende Befestigung, sondern flächige Verschraubung.

**Aufbau:**
- Flaches Gehäuse mit integrierter Scheibe
- Schraubbefestigung durch Grundplatte
- Oft nur eine offene Seite (Leine wird seitlich eingelegt)

**Anwendung:**
- Mastwangenblöcke für Fallen
- Baum-Ausholblöcke
- Decksblöcke an Schienen
- Überall dort, wo kein Platz für einen hängenden Block ist

**Vorteile:**
- Extrem flache Bauform
- Keine Schäkelverbindung nötig
- Direkte Kraftübertragung auf die Montagefläche
- Kein Pendeln

**Varianten:**
- Einfach-Wangenblock (Single Cheek)
- Doppel-Wangenblock (Double Cheek)
- Ratschen-Wangenblock
- Wangenblock mit Klemme

### 3.11 Fußblock (Foot Block / Stand-Up Block)

**Beschreibung:** Ein Block mit einer flachen Basis, der aufrecht auf dem Deck steht. Die Scheibe steht senkrecht zur Decksoberfläche.

**Anwendung:**
- Genuaschot-Umlenkung zum Cockpit
- Fallen-Umlenkung am Mastfuß
- Allgemeine Decksleinenführung
- Traveler-Systeme

**Befestigung:**
- Verschraubung durch Basisplatte
- Ggf. mit Schienenreiter

### 3.12 Masttopblock (Masthead Block)

**Beschreibung:** Speziell für den Masttop konstruierter Block zur Umlenkung von Fallen. Höchste Belastung aller Bordblöcke.

**Anforderungen:**
- Höchste Bruchlast (Fallen-Kräfte + dynamische Lasten)
- Absolut zuverlässige Befestigung (Masttopp-Beschlag)
- Wartungsarm (schwer zugänglich)
- Mehrere Scheiben nebeneinander (Groß-, Vorsegel-, Spi-Fall)

**Typische Konfiguration (40-Fuß-Fahrtenyacht):**
- 1× Großfall-Scheibe (12–14 mm Leine)
- 1× Vorsegel-Fall-Scheibe (10–12 mm)
- 1× Spi-Fall-Scheibe (8–10 mm)
- Ggf. weitere für Topp-Backstag, Antennenkabel etc.

**Scheibendurchmesser:** Masttopblöcke sollten mindestens 8:1-Verhältnis haben (oft limitiert durch Platz).

### 3.13 Umlenkblock (Turning Block)

**Beschreibung:** Block, der eine horizontale Leinenführung auf Decksniveau ermöglicht. Oft mit Schienenreiter (Genua-Holepunkt) oder direkter Decksmontage.

**Anwendung:**
- Genuaschot-Holepunkt auf Schiene
- Fallen-Umlenkung vom Mast zum Cockpit
- Leinenführung entlang des Decks

**Varianten:**
- Schienen-Umlenkblock (auf Genua-Schiene)
- Deck-Umlenkblock (fest montiert)
- Barber-Hauler-Block (auf Querschiene)

### 3.14 Großschotsysteme

Die Großschot ist eines der anspruchsvollsten Systeme auf einer Segelyacht. Je nach Bootstyp kommen verschiedene Konfigurationen zum Einsatz:

**Mittelschot-System (Center Mainsheet):**

| Komponente | Typ | Spezifikation |
|-----------|-----|---------------|
| Oberer Block (Baum) | Dreifach oder Vierfach | Kugellager, Schäkel |
| Unterer Block (Traveler) | Doppel oder Dreifach | Kugellager, Hundsfott |
| Untersetzung | 4:1 bis 6:1 | Abhängig von Bootsklasse |
| Optional | Ratschenblock | Am unteren Block |
| Optional | Fiddle + Klemmer | Für Feinjustierung |

**Achterschot-System (Aft Mainsheet):**

| Komponente | Typ | Spezifikation |
|-----------|-----|---------------|
| Oberer Block (Baum-Ende) | Doppel | Kugellager |
| Unterer Block (Cockpit) | Doppel + Klemmer | Kugellager + Cam Cleat |
| Untersetzung | 3:1 bis 4:1 | Kaskade möglich |
| Verlängerung | Schiene am Baum | Verstellbarer Angriffspunkt |

**Systemvergleich:**

| Eigenschaft | Mittelschot | Achterschot |
|------------|------------|-------------|
| Segeltrimm | Besser (vertikaler Zug) | Gut (mehr Twist) |
| Cockpit-Freiheit | Geringer | Besser |
| Kosten | Höher (Traveler) | Geringer |
| Typische Boote | Regatta, Performance | Fahrt, Cruiser |

### 3.15 Vergleichstabelle aller Blocktypen

| Typ | Scheiben | Befestigung | Typischer Einsatz | Last | Preis-Rel. |
|-----|----------|------------|-------------------|------|------------|
| Einfachblock | 1 | Schäkel/Bügel | Universell | Alle | 1,0× |
| Doppelblock | 2 | Schäkel/Bügel | Taljen | Mittel-Hoch | 1,5× |
| Dreifachblock | 3 | Schäkel/Bügel | Hochleistungs-Taljen | Hoch | 2,0× |
| Violinblock | 2 (versch.) | Schäkel | Großschot, Taljen | Mittel | 1,4× |
| Ratschenblock | 1 | Schäkel | Großschot, Spischot | Mittel-Hoch | 2,5× |
| Snatchblock | 1 | Schäkel/Bügel | Flexible Umlenkung | Alle | 1,8× |
| Orbitblock | 1 | Loop/Ring | Decksführung | Mittel | 1,6× |
| Carbo-Block | 1–2 | Schäkel | Budget/Standard | Niedrig-Mittel | 0,6× |
| Flip-Flop | 1 | Schäkel | Spi-Schot | Mittel | 1,5× |
| Wangenblock | 1–2 | Verschraubung | Mast, Baum | Alle | 1,2× |
| Fußblock | 1 | Verschraubung | Decksumlenkung | Mittel | 1,3× |
| Masttopblock | 2–4 | Bolzen | Fallen | Sehr hoch | 3,0× |
| Umlenkblock | 1 | Schiene/Deck | Schot-Holepunkt | Mittel-Hoch | 1,4× |

### 3.16 Sonderblöcke und Spezialformen

**Barber-Hauler-Block:** Kleiner Block auf einer Querleine zur seitlichen Verstellung des Genuaschot-Holepunkts.

**Bullseye-Block:** Durchgeführter Ring ohne drehbare Scheibe. Sehr niedrige Reibung bei geringen Lasten. Oft für Lazy-Jacks und Leichtwind-Schoten.

**Drahtblock:** Speziell für Draht-Fallen mit V-Rille oder passender Drahtnut. Zunehmend durch textile Fallen obsolet.

**Spreizklampe mit Block:** Kombination aus Klampe und Block in einem Gehäuse. Platzsparend für Fallen am Mast.

**Leitblock mit Rolle:** Vertikale Umlenkung (z. B. vom Cockpitboden zur Sprayhood-Stange).

**Doppelgelenkblock:** Scheibe mit zwei Drehpunkten (Kopf und Fuß), maximale Bewegungsfreiheit.

**Schwerlast-Block (Heavy Duty):** Übergroße Blöcke für Ankerspill-Umlenkung, Schlepp-Einsatz, Bergung. Bruchlasten >20.000 daN.

---

## 4. Materialien und Konstruktion

### 4.1 Scheibenmaterialien (Sheave Materials)

#### 4.1.1 Delrin/Acetal (POM — Polyoxymethylen)

**Eigenschaften:**
- Selbstschmierend
- Guter Abriebwiderstand
- Chemisch resistent gegen Salzwasser
- UV-beständig (eingeschränkt)
- Dichte: 1,41 g/cm³

**Reibungskoeffizient:** 0,05–0,08 (Gleitlager), 0,02–0,03 (mit Kugellager)

**Einsatz:** Standard-Scheibenmaterial für alle Block-Preisklassen. Am weitesten verbreitet.

**Lebensdauer:** 5–15 Jahre abhängig von Belastung und UV-Exposition.

**Erkennungsmerkmale:** Weiß, cremefarben oder schwarz. Glatte, leicht wachsartige Oberfläche.

#### 4.1.2 Torlon (PAI — Polyamidimid)

**Eigenschaften:**
- Höchste Festigkeit aller Thermoplaste
- Temperaturbeständig bis 260°C
- Exzellenter Abriebwiderstand
- Selbstschmierend unter Last
- Dichte: 1,42 g/cm³

**Reibungskoeffizient:** 0,04 (Gleitlager)

**Einsatz:** Premium-Blöcke für höchste Belastungen. Lager und Scheiben.

**Lebensdauer:** 10–20+ Jahre.

**Preis:** 3–5× teurer als Delrin.

**Erkennungsmerkmale:** Dunkelbraun bis olivgrün. Hart und schwer.

#### 4.1.3 Aluminium (eloxiert)

**Eigenschaften:**
- Hohe Festigkeit bei geringem Gewicht
- Korrosionsschutz durch Eloxierung
- Gute Wärmeableitung
- Dichte: 2,7 g/cm³

**Einsatz:** Hochlast-Scheiben für Fallen und Winschen. Regatta-Blöcke.

**Oberflächenbehandlung:** Hart-Eloxierung (Typ III) für marine Anwendung. Schichtdicke 25–75 μm.

**Achtung:** Aluminium und Edelstahl in Salzwasser → Kontaktkorrosion! Isolierung erforderlich.

#### 4.1.4 Edelstahl (316/316L)

**Eigenschaften:**
- Höchste Festigkeit
- Hervorragende Korrosionsbeständigkeit
- Schwer
- Dichte: 8,0 g/cm³

**Einsatz:** Hochlast-Scheiben, Superyacht-Blöcke, Masttopp-Blöcke.

**Hinweis:** 316L (Low Carbon) ist zwingend für den Marineeinsatz. 304er-Stahl ist nicht ausreichend salzwasserbeständig.

#### 4.1.5 Kohlefaser (CFK)

**Eigenschaften:**
- Extrem leicht bei höchster Festigkeit
- Keine Korrosion
- Hohe Steifigkeit
- Dichte: 1,6 g/cm³

**Einsatz:** Regatta-Hochleistungsblöcke, America's Cup, Volvo Ocean Race.

**Preis:** 5–15× teurer als Standardblöcke.

**Lebensdauer:** Theoretisch unbegrenzt, aber empfindlich gegen Schlagbelastung.

#### 4.1.6 Keramik (Siliziumnitrid, Zirkonoxid)

**Eigenschaften:**
- Extrem hart (keine Rillenbildung)
- Korrosionsfrei
- Wärmebeständig
- Sehr glatte Oberfläche
- Dichte: 3,2 g/cm³ (Si₃N₄)

**Einsatz:** Keramik-Kugellager in Hochleistungsblöcken. Selten als Scheibenmaterial.

**Vorteil:** Keramik-Lager reduzieren die Reibung um 20–30% gegenüber Stahl-Kugellagern.

#### 4.1.7 Materialvergleich Scheiben

| Material | Dichte (g/cm³) | Festigkeit | Abrieb | Korrosion | UV | Preis |
|----------|---------------|-----------|--------|-----------|-----|-------|
| Delrin/POM | 1,41 | Mittel | Gut | Exzellent | Mittel | € |
| Torlon/PAI | 1,42 | Sehr hoch | Exzellent | Exzellent | Gut | €€€ |
| Aluminium | 2,70 | Hoch | Mittel | Gut* | — | €€ |
| Edelstahl 316L | 8,00 | Sehr hoch | Gut | Sehr gut | — | €€€ |
| Kohlefaser | 1,60 | Höchst | Gut | Exzellent | Gut** | €€€€€ |
| Keramik | 3,20 | Höchst | Exzellent | Exzellent | — | €€€€ |

*Eloxierung erforderlich. **UV-Schutzlack erforderlich.

### 4.2 Lagertypen (Bearing Types)

#### 4.2.1 Kugellager (Ball Bearing)

**Aufbau:** Laufring mit Stahlkugeln, abgedichtet oder offen.

**Reibungskoeffizient:** ~0,02 (2%)

**Vorteile:**
- Geringste Reibung aller konventionellen Lager
- Hohe Tragfähigkeit
- Lange Lebensdauer bei Wartung
- Standard in allen Preisklassen ab Mittelklasse

**Nachteile:**
- Empfindlich gegen Salzwasser (ohne Dichtung)
- Wartung erforderlich (Fetten, Spülen)
- Höheres Gewicht als Gleitlager
- Höherer Preis

**Wartung:** Süßwasserspülung nach Salzwassereinsatz. Jährliches Nachfetten mit Teflon-/PTFE-Fett.

**Materialien der Kugeln:**
- Stahl (Standard): AISI 52100 Chromstahl
- Edelstahl (Marine): AISI 316 oder 440C
- Keramik (Hochleistung): Si₃N₄ (Siliziumnitrid)

#### 4.2.2 Nadellager (Needle Bearing)

**Aufbau:** Zylindrische Rollen (Nadeln) statt Kugeln. Sehr kompakt.

**Reibungskoeffizient:** ~0,03 (3%)

**Vorteile:**
- Kompakter als Kugellager bei gleicher Tragfähigkeit
- Höhere Flächenpressung möglich
- Gut für begrenzte Einbauräume

**Nachteile:**
- Etwas höhere Reibung als Kugellager
- Empfindlich gegen axiale Kräfte

**Anwendung:** Mittelklasse-Blöcke, insbesondere wo Platz begrenzt ist.

#### 4.2.3 Gleitlager (Plain Bearing)

**Aufbau:** Scheibe läuft direkt auf der Achse. Material-zu-Material-Kontakt.

**Reibungskoeffizient:** 0,05–0,08 (5–8%)

**Vorteile:**
- Einfachster Aufbau
- Geringes Gewicht
- Kein Wartungsbedarf (selbstschmierend bei Delrin)
- Niedrigster Preis
- Salzwasser-unempfindlich
- Keine Dichtungsprobleme

**Nachteile:**
- Höchste Reibung
- Begrenzte Lebensdauer unter hoher Last
- Nicht für Hochlast geeignet

**Anwendung:** Einstiegs-Blöcke, Jollen, niedrig belastete Umlenkungen.

#### 4.2.4 Keramik-Hybridlager (Ceramic Hybrid Bearing)

**Aufbau:** Stahl-Laufringe mit Keramik-Kugeln (Si₃N₄).

**Reibungskoeffizient:** ~0,015 (1,5%)

**Vorteile:**
- Geringste Reibung aller Lager
- Keine Korrosion der Kugeln
- Höhere Drehzahl möglich
- Längere Lebensdauer

**Nachteile:**
- Höchster Preis (3–5× Stahl-Kugellager)
- Empfindlich gegen Schlag
- Reparatur nur als Komplettaustausch

**Anwendung:** Regatta-Blöcke, Superyacht-Premium-Ausstattung.

#### 4.2.5 Lagervergleich

| Eigenschaft | Kugellager | Nadellager | Gleitlager | Keramik-Hybrid |
|-------------|-----------|------------|------------|----------------|
| Reibung | 2% | 3% | 5–8% | 1,5% |
| Tragfähigkeit | Hoch | Sehr hoch | Mittel | Hoch |
| Gewicht | Mittel | Mittel | Gering | Mittel |
| Wartung | Mittel | Mittel | Gering | Gering |
| Salzwasser | Mittel* | Mittel* | Hoch | Hoch |
| Preis | €€ | €€ | € | €€€€ |
| Lebensdauer | 5–10 J. | 5–10 J. | 3–8 J. | 10–20 J. |

*Mit Dichtung deutlich verbessert.

### 4.3 Wangenmaterialien (Cheek Materials)

#### 4.3.1 Edelstahl 316/316L

**Einsatz:** Hochlast-Blöcke, Superyacht, Masttopp-Blöcke.

**Vorteile:** Höchste Festigkeit, korrosionsbeständig, langlebig.
**Nachteile:** Schwer, teuer.

**Oberflächenbehandlung:**
- Poliert (Mirror): Optik, leichte Reinigung
- Gebürstet (Brushed): Dezente Optik
- Elektro-poliert: Beste Korrosionsbeständigkeit

#### 4.3.2 Aluminium (eloxiert)

**Einsatz:** Performance-Blöcke, Regatta, gewichtsoptimiert.

**Vorteile:** Leicht, steif, gute Festigkeit.
**Nachteile:** Kontaktkorrosion mit Edelstahl, nicht so langlebig wie Stahl.

**Hart-Eloxierung:** Typ III, 25–75 μm Schichtdicke, Vickers-Härte 300–600 HV.

#### 4.3.3 Kohlefaser (CFK)

**Einsatz:** Racing-Blöcke, Gewichtsoptimierung.

**Vorteile:** Extremes Festigkeits-Gewichts-Verhältnis, steif, korrosionsfrei.
**Nachteile:** Teuer, empfindlich gegen Punktbelastung, aufwändige Reparatur.

#### 4.3.4 Composite/Carbo (glasfaserverstärktes Polymer)

**Einsatz:** Harkens Carbo-Serie, Einstiegs-/Mittelklasse.

**Vorteile:** Leicht, korrosionsfrei, UV-stabilisiert, schwimmfähig, preiswert.
**Nachteile:** Geringere Festigkeit als Metall, Alterung durch UV.

#### 4.3.5 Titan

**Einsatz:** Extreme Anwendungen, Superyacht-Custom, America's Cup.

**Vorteile:** Höchste Korrosionsbeständigkeit, sehr leicht für die Festigkeit.
**Nachteile:** Extrem teuer, schwer zu bearbeiten.

### 4.4 Befestigungselemente

#### 4.4.1 Schäkel (Shackle)

**Typen:**
- **D-Schäkel:** Standard, hohe Tragfähigkeit, geringe Bewegungsfreiheit
- **Omega-Schäkel:** Breitere Öffnung, seitliche Belastung möglich
- **Schnapp-Schäkel (Snap Shackle):** Schnelles Öffnen unter Last, Spi-Fallen
- **Halyard-Schäkel:** Schmal, für Segel-Kopfbrett
- **Wirbelschäkel (Swivel Shackle):** Drehbar, verhindert Leinenverdrillung

**Material:** Ausschließlich AISI 316/316L für Marineeinsatz.

**Sicherung:** Schäkelbolzen immer mit Splint, Draht oder Loctite sichern. Schraubschäkel regelmäßig nachziehen.

#### 4.4.2 Hundsfott (Becket)

Ein fester Befestigungspunkt am Block für die stehende Part einer Talje. Kann als geschmiedetes Auge, Drahtschlaufe oder Textilschlaufe ausgeführt sein.

#### 4.4.3 Bügel (Toggle)

Ein Zwischenglied, das zwischen Schäkel und Befestigungspunkt geschaltet wird, um Biegebelastungen auszugleichen. Wichtig bei Fallen-Blöcken und Wantenbefestigungen.

#### 4.4.4 Direkte Verschraubung

Wangenblöcke und Fußblöcke werden oft direkt mit Schrauben (Edelstahl A4) auf Deck, Mast oder Baum montiert. Unterlage/Verstärkung auf der Innenseite zwingend.

---

## 5. Dimensionierung und Auswahl

### 5.1 Grundregeln der Blockauswahl

1. **Leinendurchmesser bestimmt Scheibengröße** — Minimum 4:1-Verhältnis für Flechtleinen
2. **Arbeitslast bestimmt Blockgröße** — SWL (Safe Working Load) muss die maximale Betriebslast abdecken
3. **Sicherheitsfaktor beachten** — Bruchlast = SWL × Sicherheitsfaktor
4. **Lagertyp nach Anwendung** — Kugellager für Hochlast und häufige Bewegung
5. **Material nach Umgebung** — Edelstahl für Salzwasser-Dauereinsatz
6. **Gewicht vs. Festigkeit** — Regatta: Gewicht minimieren, Fahrt: Festigkeit priorisieren

### 5.2 Dimensionierungstabelle nach Leinendurchmesser

| Leinendurchmesser | Min. Scheibendurchmesser | Block-Größenklasse | Typische SWL |
|-------------------|--------------------------|--------------------|-------------|
| 4 mm | 16 mm | Micro | 200–400 daN |
| 5 mm | 20 mm | Mini | 300–600 daN |
| 6 mm | 25 mm | 25 mm | 400–800 daN |
| 8 mm | 32 mm | 29–40 mm | 800–1.500 daN |
| 10 mm | 40 mm | 40–57 mm | 1.200–2.500 daN |
| 12 mm | 48 mm | 57–75 mm | 2.000–4.000 daN |
| 14 mm | 56 mm | 75 mm | 3.000–5.000 daN |
| 16 mm | 64 mm | 75–100 mm | 4.000–7.000 daN |
| 18 mm | 72 mm | 100 mm | 5.000–10.000 daN |
| 20 mm | 80 mm | 100+ mm | 7.000–12.000 daN |
| 22 mm | 88 mm | 125+ mm | 10.000–15.000 daN |

> ⚠️ **ZU PRÜFEN (Audit):** Die SWL-Werte dieser Tabelle (z. B. 40–57-mm-Block: 1.200–2.500 daN) widersprechen der WLL-Angabe in ANHANG I.1 (Harken 57mm: WLL nur 300–950 daN) und liegen betragsmäßig auf dem Niveau der *Bruchlast*-Werte in Abschnitt 3.1. Diese Spalte ist last-/sicherheitskritisch und ohne Herstellerkatalog als **estimated — unverifiziert** zu behandeln (WLL/SWL ≠ Bruchlast; nicht ungeprüft als zulässige Arbeitslast verwenden).

### 5.3 SWL vs. Bruchlast (Breaking Load)

**Definition:**
- **SWL (Safe Working Load / WLL):** Maximale Last im normalen Betrieb
- **Bruchlast (BL / MBL):** Last bei der der Block versagt (Verformung oder Bruch)
- **Sicherheitsfaktor (SF):** BL / SWL

**Empfohlene Sicherheitsfaktoren:**

| Anwendung | Sicherheitsfaktor | Begründung |
|-----------|-------------------|------------|
| Regattayacht, Profi-Crew | 3:1 | Kontrollierte Bedingungen |
| Fahrtenyacht, erfahrene Crew | 4:1 | Standard |
| Charteryacht, Ausbildung | 5:1 | Bedienungsfehler wahrscheinlicher |
| Superyacht, gewerblich | 5:1 bis 6:1 | Vorschriften, Haftung |
| Personen-tragend (Bosunsstuhl) | 8:1 bis 10:1 | Lebensschutz |

### 5.4 Blockauswahl nach Bootsklasse

#### Jolle (4–8m)

| Anlage | Blocktyp | Leine | SWL | Empfehlung |
|--------|---------|-------|-----|------------|
| Großschot | Violinblock + Klemmer | 6–8 mm | 400 daN | Harken 29mm/40mm Carbo |
| Fock-Schot | Einfachblock | 5–6 mm | 300 daN | Ronstan S15/S20 |
| Großfall | Einfachblock | 4–6 mm | 500 daN | Standard Gleitlager |
| Baumniederholer | Violinblock 2:1–4:1 | 4–6 mm | 300 daN | Harken Micro |
| Cunningham | Einfachblock | 4–5 mm | 200 daN | Miniblock |
| Trapez | Einfachblock Ratsche | 4–5 mm | 300 daN | Ronstan S15 Ratchet |

#### Fahrtensegler (8–14m)

| Anlage | Blocktyp | Leine | SWL | Empfehlung |
|--------|---------|-------|-----|------------|
| Großschot | Talje 4:1–6:1 | 10–12 mm | 1.500 daN | Harken 57mm |
| Genuaschot | Einfach + Umlenkblock | 10–12 mm | 2.000 daN | Harken 57mm Kugellager |
| Genuaschot-Holepunkt | Schienen-Umlenkblock | 10–12 mm | 2.000 daN | Harken 1642 oder Lewmar |
| Großfall | Masttop + Umlenkung | 10–12 mm | 2.500 daN | Harken 57mm oder 75mm |
| Vorsegel-Fall | Masttop + Umlenkung | 10 mm | 2.000 daN | Harken 57mm |
| Spi-Fall | Einfachblock | 8–10 mm | 1.200 daN | Harken 40mm |
| Baumniederholer | Talje 4:1 | 8–10 mm | 800 daN | Harken 40mm System |
| Reffleinen | Einfach/Doppel | 8–10 mm | 1.000 daN | Harken 40mm |
| Backstag | Talje 6:1–8:1 | 8–10 mm | 1.500 daN | Kaskade |
| Traveler-Wagen | Kugellager-Wagen | — | 2.500 daN | Harken/Lewmar Traveler |

#### Performance Cruiser (10–16m)

| Anlage | Blocktyp | Leine | SWL | Empfehlung |
|--------|---------|-------|-----|------------|
| Großschot | Talje 6:1–8:1 | 12 mm | 2.000 daN | Harken 75mm T2 |
| Genuaschot | Hochlast-Einfachblock | 12–14 mm | 3.000 daN | Harken 75mm Black |
| Großfall | Hochlast-Umlenkung | 12 mm | 3.500 daN | Harken 75mm Kugellager |
| Spi/Gennaker | Snatch + Einfach | 10–12 mm | 2.000 daN | Harken 57mm |
| Baumniederholer | Talje 6:1–8:1 | 10 mm | 1.500 daN | Harken 57mm |

#### Blauwasseryacht (12–18m)

| Anlage | Blocktyp | Leine | SWL | Empfehlung |
|--------|---------|-------|-----|------------|
| Großschot | Talje 6:1–8:1 | 12–14 mm | 2.500 daN | Harken 75mm Kugellager |
| Genuaschot | Hochlast + Snatch | 12–14 mm | 3.000 daN | Lewmar Synchro 72mm |
| Großfall | Masttop Kugellager | 12–14 mm | 4.000 daN | Harken 75mm |
| Reffleinen | Doppel + Umlenkung | 10–12 mm | 1.500 daN | Harken 57mm |
| Snatchblöcke | 4–6 Stück | 12–14 mm | 3.000 daN | Lewmar Synchro Snatch |

**Blauwasser-Besonderheiten:**
- Korrosionsbeständigkeit hat absolute Priorität (Edelstahl 316L)
- Ersatzteil-Verfügbarkeit weltweit: Harken und Lewmar bevorzugen
- Redundanz einplanen: Ersatzblöcke für kritische Positionen
- Gleitlager-Backup-Blöcke mitnehmen (wartungsfrei, notlauffähig)

#### Regattayacht (8–20m)

| Anlage | Blocktyp | Leine | SWL | Empfehlung |
|--------|---------|-------|-----|------------|
| Großschot | T2/Black Ratsche | 10–12 mm | 2.500 daN | Harken T2 Ratchamatic |
| Genuaschot | Kugellager Ultra | 10–12 mm | 3.000 daN | Harken Black 75mm |
| Spi-Schot | Ratsche | 8–10 mm | 1.500 daN | Harken 57mm T2 Ratchet |
| Fallen | Leichtgewicht-Kugellager | 8–10 mm | 2.500 daN | Harken Black oder Ronstan Orbit |
| Achterstag | Kaskade 12:1 | 8 mm | 2.000 daN | Harken Hochlast |

**Regatta-Besonderheiten:**
- Gewicht minimieren (CFK-Wangen, Dyneema-Befestigung)
- Maximale Effizienz (Keramik-Hybridlager)
- Ratschenblöcke für Schoten (Handsegelbar)
- Jedes Gramm zählt bei ORC/IRC-Vermessung

### 5.5 Überdimensionierung vs. Unterdimensionierung

**Folgen der Unterdimensionierung:**
- Vorzeitiger Verschleiß (Lager, Scheibe, Leine)
- Erhöhte Reibung durch Verformung
- Risiko eines Blockbruchs (Katastrophal)
- Leinenbeschädigung (Rillenbildung in der Scheibe)

**Folgen der Überdimensionierung:**
- Unnötiges Gewicht (besonders am Mast kritisch)
- Höhere Kosten
- Ggf. ungünstige Geometrie (zu große Blöcke passen nicht)
- Ästhetische Nachteile

**Faustregel:** Ein Block eine Größe zu groß ist besser als eine Größe zu klein.

---

## 6. Hersteller-Übersicht

### 6.1 Harken (USA/Italien)

**Gegründet:** 1967 in Pewaukee, Wisconsin, USA (Peter Harken)
**Hauptsitz:** Pewaukee, USA + Produktionsstandort Limena, Italien
**Marktposition:** Weltmarktführer für Segelblöcke und Decksbeschläge

**Produktserien:**

#### Harken Carbo
- **Segment:** Einstieg/Mittelklasse
- **Wangen:** Glasfaserverstärktes Polymer (schwarz)
- **Scheiben:** Delrin
- **Lager:** Delrin-Gleitlager (Standard), Kugellager (Carbo Air)
- **Größen:** 22mm, 29mm, 40mm, 57mm, 75mm
- **Bruchlast:** 300–5.000 daN
- **Preis:** 8–120 EUR
- **Stärken:** Leicht, preiswert, korrosionsfrei, UV-stabilisiert
- **Schwächen:** Geringere Bruchlast als Metall, begrenzte Lebensdauer
- **Typische Anwendung:** Jollen, Fahrtensegler bis 12m, Budget-Ausstattung

#### Harken Black
- **Segment:** Hochleistung/Racing
- **Wangen:** Aluminium hart-eloxiert (schwarz)
- **Scheiben:** Aluminium oder Torlon
- **Lager:** Edelstahl-Kugellager, optional Keramik
- **Größen:** 29mm, 40mm, 57mm, 75mm
- **Bruchlast:** 600–8.000 daN
- **Preis:** 30–350 EUR
- **Stärken:** Leicht, hohe Bruchlast, geringe Reibung
- **Schwächen:** Aluminium-Edelstahl-Kontaktkorrosion möglich
- **Typische Anwendung:** Regattayachten, Performance Cruiser

#### Harken T2
- **Segment:** Hochleistung
- **Wangen:** Aluminium hart-eloxiert mit Teflon-Beschichtung
- **Scheiben:** Torlon oder Aluminium
- **Lager:** Kugellager Edelstahl oder Keramik-Hybrid
- **Größen:** 40mm, 57mm, 75mm
- **Bruchlast:** 1.200–8.000 daN
- **Preis:** 60–500 EUR
- **Stärken:** Höchste Leistung bei geringstem Gewicht
- **Schwächen:** Teuer, Verfügbarkeit
- **Typische Anwendung:** Hochsee-Regatta, TP52, Fast40+

#### Harken Midrange
- **Segment:** Standard/Mittelklasse
- **Wangen:** Edelstahl 316 oder Aluminium
- **Scheiben:** Delrin oder Aluminium
- **Lager:** Kugellager Edelstahl
- **Größen:** 22mm, 29mm, 40mm, 57mm, 75mm, 100mm
- **Bruchlast:** 300–12.000 daN
- **Preis:** 20–600 EUR
- **Stärken:** Robuste Standardausstattung, breite Verfügbarkeit
- **Schwächen:** Höheres Gewicht als Carbo/Black
- **Typische Anwendung:** Fahrtenyachten 8–18m, Charterflotten

#### Harken Element
- **Segment:** Einstieg
- **Wangen:** Composite/Polymer
- **Scheiben:** Delrin
- **Lager:** Gleitlager
- **Größen:** 22mm, 29mm, 40mm
- **Bruchlast:** 200–1.500 daN
- **Preis:** 5–40 EUR
- **Stärken:** Günstigste Harken-Serie
- **Typische Anwendung:** Jollen, Leichtwind, niedrige Lasten

**Harken Produktmatrix:**

| Serie | Gewicht (rel.) | Bruchlast (rel.) | Reibung | Preis (rel.) |
|-------|---------------|-----------------|---------|-------------|
| Element | 1,0× | 0,7× | Hoch | 0,3× |
| Carbo | 0,8× | 1,0× | Mittel | 0,5× |
| Midrange | 1,3× | 1,2× | Gering | 1,0× |
| Black | 0,9× | 1,5× | Sehr gering | 1,5× |
| T2 | 0,7× | 1,5× | Minimal | 2,5× |

### 6.2 Lewmar (Großbritannien)

**Gegründet:** 1946 in Havant, Hampshire, UK
**Marktposition:** Zweitgrößter Hersteller weltweit. Stark im Fahrtensegler- und Superyacht-Segment.

**Produktserien:**

#### Lewmar Synchro
- **Segment:** Premium-Fahrt/Performance
- **Wangen:** Edelstahl 316 hochglanzpoliert
- **Scheiben:** Delrin oder Acetal
- **Lager:** Kugellager Edelstahl
- **Größen:** 30mm, 40mm, 50mm, 60mm, 72mm
- **Bruchlast:** 600–7.000 daN
- **Preis:** 30–350 EUR
- **Stärken:** Extrem robust, elegante Optik, hervorragende Korrosionsbeständigkeit
- **Typische Anwendung:** Fahrtenyachten 10–18m, Blauwasser

> ⚠️ **ZU PRÜFEN (Audit):** Laut Lewmar-/Händler-Datenblatt hat die Synchro 72mm eine WLL von 1.100 kg (2.420 lb ≈ 1.079 daN) — sie ist **nicht** der in ANHANG D.4 (Beispiel) genannte 10.000-daN-Block; 10.000 daN gehören zur Ocean-Serie. Die hier angegebene Bruchlast-Spanne 600–7.000 daN gegen den aktuellen Lewmar-Katalog prüfen (**estimated — unverifiziert**).

#### Lewmar Control
- **Segment:** Standard
- **Wangen:** Aluminium oder Edelstahl
- **Scheiben:** Delrin
- **Lager:** Kugellager
- **Größen:** 30mm, 40mm, 50mm, 60mm
- **Bruchlast:** 400–4.000 daN
- **Preis:** 20–200 EUR
- **Stärken:** Gutes Preis-Leistungs-Verhältnis
- **Typische Anwendung:** Fahrtensegler 8–14m

#### Lewmar Ocean
- **Segment:** Schwerlast/Blauwasser
- **Wangen:** Edelstahl 316 massiv
- **Scheiben:** Acetal/Delrin verstärkt
- **Lager:** Kugellager, abgedichtet
- **Größen:** 50mm, 60mm, 72mm, 80mm
- **Bruchlast:** 4.000–10.000 daN
- **Preis:** 80–500 EUR
- **Stärken:** Höchste Robustheit, abgedichtete Lager
- **Typische Anwendung:** Blauwasseryachten 14–20m, Superyachten

#### Lewmar HTX
- **Segment:** Racing
- **Wangen:** Aluminium hart-eloxiert
- **Scheiben:** Aluminium/Torlon
- **Lager:** Hochleistungs-Kugellager
- **Größen:** 40mm, 50mm, 60mm, 72mm
- **Bruchlast:** 1.000–7.000 daN
- **Preis:** 50–400 EUR
- **Stärken:** Geringes Gewicht, hohe Festigkeit
- **Typische Anwendung:** Club-Regatta, Performance Cruiser

### 6.3 Antal (Italien)

**Gegründet:** 1964 in Vigevano, Italien
**Marktposition:** Drittgrößter Hersteller. Stark in Südeuropa. Innovativ bei Low-Friction-Ringen.

**Produktserien:**

#### Antal Classic
- **Segment:** Standard/Fahrt
- **Wangen:** Edelstahl oder Aluminium
- **Lager:** Kugellager
- **Größen:** 20mm–75mm
- **Preis:** 15–250 EUR
- **Typische Anwendung:** Fahrtensegler, OEM-Ausstatter

#### Antal Black Line
- **Segment:** Performance
- **Wangen:** Aluminium hart-eloxiert schwarz
- **Lager:** Kugellager Edelstahl
- **Größen:** 30mm–75mm
- **Preis:** 30–350 EUR
- **Typische Anwendung:** Performance Cruiser, Regatta

#### Antal Low Friction Ring (LFR)
- **Segment:** Innovativ/Regatta
- **Konstruktion:** Textilring mit Dyneema-Ummantelung statt konventionellem Block
- **Reibung:** 3–5%
- **Gewicht:** 70–90% leichter als konventionelle Blöcke
- **Preis:** 15–80 EUR
- **SWL:** 300–3.000 daN
- **Typische Anwendung:** Fallen-Umlenkung, Spinnaker-Systeme, Lazy-Jacks

### 6.4 Ronstan (Australien)

**Gegründet:** 1953 in Melbourne, Australien
**Marktposition:** Innovationsführer bei Orbit-Technologie. Stark im Jollen- und Regattabereich.

**Produktserien:**

#### Ronstan Orbit
- **Segment:** Innovation/Performance
- **Funktionsprinzip:** Orbital-drehbare Scheibe (patentiert)
- **Wangen:** Aluminium oder Composite
- **Lager:** Kugellager
- **Größen:** 20mm, 30mm, 40mm, 55mm, 75mm
- **Bruchlast:** 400–6.000 daN
- **Preis:** 15–300 EUR
- **Stärken:** Selbstausrichtend, kompakt, geringe Reibung
- **Typische Anwendung:** Universal, insbesondere Decksumlenkung

#### Ronstan Series 15/20/25/30/40/55
- **Segment:** Standard
- **Wangen:** Aluminium oder Nylon
- **Lager:** Gleitlager oder Kugellager
- **Größen:** 15mm, 20mm, 25mm, 30mm, 40mm, 55mm
- **Bruchlast:** 200–4.000 daN
- **Preis:** 5–200 EUR
- **Typische Anwendung:** Jollen, Einsteiger, OEM

#### Ronstan Rhino
- **Segment:** Schwerlast
- **Wangen:** Edelstahl 316 massiv
- **Größen:** 55mm, 75mm
- **Bruchlast:** 5.000–10.000 daN
- **Preis:** 80–400 EUR
- **Typische Anwendung:** Blauwasser, Großyachten

### 6.5 Schaefer Marine (USA)

**Gegründet:** 1960 in New Bedford, Massachusetts
**Marktposition:** Nischenhersteller für Decksbeschläge und Rollanlagen. Solide Blöcke im Mittelfeld.

**Produktserien:**
- **Series 5:** Leichtgewicht-Blöcke, 5/16"–1/2" Leine, 400–2.000 daN
- **Series 7:** Standard-Blöcke, 3/8"–5/8" Leine, 800–4.000 daN
- **Series 9:** Schwerlast-Blöcke, 1/2"–3/4" Leine, 2.000–8.000 daN

**Besonderheit:** Starke Präsenz im nordamerikanischen Fahrtensegler-Markt. Guter Kundenservice.

### 6.6 Seldén (Schweden)

**Gegründet:** 1960 in Göteborg, Schweden
**Marktposition:** Marktführer für Masten und Riggs. Blöcke als Ergänzungsprogramm.

**Block-Programm:**
- Hauptsächlich Systeme (Großschot-Systeme, Fall-Systeme)
- Edelstahl- und Aluminium-Blöcke
- Optimiert für Integration mit Seldén-Riggs
- Preis: Mittelfeld bis Premium
- Verfügbarkeit: Über Seldén-Rigg-Händlernetz

**Stärke:** Perfekte Integration mit Seldén-Masten (Schienensysteme, Wangenblöcke).

### 6.7 Wichard / Facnor (Frankreich)

**Gegründet:** 1919 (Wichard), Zusammenschluss mit Facnor
**Marktposition:** Stark im französischen Markt, Premium-Segment.

**Block-Programm:**
- Edelstahl 316L geschmiedet
- Hochwertige Kugellager
- Fokus auf Robustheit und Langlebigkeit
- Preis: Premium
- Typische Anwendung: Blauwasser, französische Serienyachten (Bénéteau, Jeanneau OEM)

**Besonderheit:** Wichard ist auch führend bei Schäkeln und Karabinern.

### 6.8 Viadana (Italien)

**Gegründet:** 1975 in Brescia, Italien
**Marktposition:** Preis-Leistungs-Führer, starker OEM-Zulieferer.

**Produktserien:**

#### Viadana Block Serie
- **Segment:** Budget bis Mittelklasse
- **Wangen:** Nylon, Aluminium oder Edelstahl
- **Größen:** 14mm–75mm
- **Bruchlast:** 200–6.000 daN
- **Preis:** 5–150 EUR (30–50% günstiger als Harken)
- **Stärken:** Hervorragendes Preis-Leistungs-Verhältnis, breites Sortiment
- **Schwächen:** Geringerer Markenwert, Ersatzteile schwieriger

**Typische Anwendung:** OEM für italienische Werften, Budget-Refits.

### 6.9 Herstellervergleich — Übersicht

| Hersteller | Herkunft | Segment | Preis | Qualität | Innovation | Verfügbarkeit |
|-----------|---------|---------|-------|----------|-----------|---------------|
| Harken | USA/IT | Alle | €€–€€€€ | Sehr hoch | Sehr hoch | Weltweit |
| Lewmar | UK | Fahrt/Premium | €€–€€€ | Sehr hoch | Hoch | Weltweit |
| Antal | IT | Standard/Perf. | €–€€€ | Hoch | Hoch (LFR) | Europa |
| Ronstan | AUS | Jolle/Perf. | €–€€€ | Hoch | Sehr hoch (Orbit) | Weltweit |
| Schaefer | USA | Fahrt | €€ | Hoch | Mittel | Nordamerika |
| Seldén | SE | Rigg-Zubehör | €€–€€€ | Sehr hoch | Mittel | Europa |
| Wichard | FR | Premium | €€€ | Sehr hoch | Mittel | Europa |
| Viadana | IT | Budget | €–€€ | Mittel-Hoch | Mittel | Europa |

### 6.10 Preisbereiche nach Blockgröße und Hersteller (EUR, ca.)

| Größe | Harken Carbo | Harken Black | Harken T2 | Lewmar Synchro | Ronstan Orbit | Viadana |
|-------|-------------|-------------|-----------|----------------|--------------|---------|
| 25mm | 8–15 | — | — | — | 10–20 | 5–10 |
| 29mm | 12–25 | 25–50 | — | — | 15–30 | 8–18 |
| 40mm | 18–45 | 35–80 | 55–120 | 30–70 | 25–55 | 12–30 |
| 57mm | 35–80 | 65–150 | 100–220 | 55–130 | 45–100 | 25–60 |
| 75mm | 60–130 | 120–280 | 180–450 | 100–250 | 80–180 | 50–100 |
| 100mm | — | — | — | 200–450 | — | 80–160 |

**Confidence:** estimated (Marktpreise variieren, Stand 2026)

---

## 7. Anlagen-spezifische Zuordnung

### 7.1 Großschot (Mainsheet)

Die Großschot ist die höchstbelastete Schot auf einer Segelyacht und erfordert ein ausgeklügeltes Blocksystem.

**Anforderungen:**
- Hohe Bruchlast (dynamische Böenlasten)
- Geringe Reibung (häufiges Dichtholen/Fieren)
- Ratsche (bei Handsegelung ohne Winsch)
- Klemmer (Cam Cleat) oder Winsch

**System nach Bootsgröße:**

| Bootsgröße | System | Untersetzung | Block-Empfehlung |
|-----------|--------|-------------|-----------------|
| Jolle (5m) | Violinblock + Einfach | 4:1 | Harken 40mm Carbo |
| Daysailer (7m) | Violinblock + Doppel | 4:1–6:1 | Harken 40mm–57mm |
| Fahrt (10m) | Traveler + Talje | 4:1–6:1 | Harken 57mm + Ratsche |
| Fahrt (13m) | Traveler + Winsch | 2:1–4:1 + Winsch | Harken 57mm–75mm |
| Performance (13m) | Traveler + Talje + Feintrimmung | 6:1–8:1 | Harken 75mm T2 |
| Blauws. (15m) | Traveler + Winsch | 3:1 + Winsch | Harken 75mm + Lewmar Winsch |
| Superyacht (20m+) | Hydraulik oder elektr. | — | Custom oder Lewmar Ocean |

### 7.2 Genuaschot (Genoa Sheet)

**Anforderungen:**
- Höchste Schotkraft aller Segel
- Selbstwendend (auf manchen Yachten) oder konventionell mit Winsch
- Holepunkt-Verstellung (Genua-Schiene)

**Blockauswahl:**

| Position | Blocktyp | Bemerkung |
|---------|---------|-----------|
| Holepunkt (Schiene) | Schienen-Umlenkblock | Kugellager auf Schiene |
| Umlenkung zum Cockpit | Fußblock oder Umlenkblock | Fest montiert |
| Winsch-Vorblock | Einfachblock | Leinenführung zur Winsch |
| Barber-Hauler | 2× Einfachblock | Querschiene oder Leine |

### 7.3 Spinnaker-/Gennaker-System

**Besonderheiten:**
- Sehr hohe dynamische Lasten (plötzliches Füllen)
- Schnelles Dichtholen/Fieren erforderlich
- Leine muss schnell und sicher eingelegt werden (Snatchblöcke)

**Blockauswahl:**

| Position | Blocktyp | Bemerkung |
|---------|---------|-----------|
| Spi-Fall (Mast) | Masttop-Block | Höchste Last |
| Spi-Fall (Deck) | Umlenkblock | Am Mastfuß |
| Spi-Schot (Achterdeck) | Snatchblock oder Einfach | Große Scheibe, schnelles Laufen |
| Spi-Schot (Ratsche) | Ratschenblock | Optional für Handsegelung |
| Spi-Barber-Hauler | 2× Einfachblock | Für Anlaufwinkel-Verstellung |
| Gennaker-Tacker | Umlenkblock | Am Bug |

### 7.4 Fallen (Halyards)

| Fall | Masttop-Block | Mast-Fuß-Umlenkung | Cockpit-Umlenkung |
|------|-------------|--------------------|--------------------|
| Großfall | Kugellager, SWL 3.000+ daN | Wangenblock am Mast | Fußblock zum Cockpit |
| Vorsegel-Fall | Kugellager, SWL 2.500+ daN | Wangenblock am Mast | Fußblock zum Cockpit |
| Spi-Fall | Kugellager, SWL 1.500+ daN | Wangenblock am Mast | Optional |
| Topp-Fall | Optional | — | — |

### 7.5 Reffleinen (Reef Lines)

**System-Varianten:**
- **Mast-Reff:** Leinen laufen durch Ösen im Segel, über Blöcke am Baum und Mast
- **Einleinen-Reff:** Eine Leine pro Reffreihe, Umlenkung am Baum
- **Lazy-Jacks:** Auffangsystem für das gerefftes Segel, mit Blöcken am Mast

**Blockauswahl (Einleinen-Reff, 12m-Yacht):**

| Position | Blocktyp | SWL |
|---------|---------|-----|
| Baum-Ende (Nock) | Einfachblock Edelstahl | 1.500 daN |
| Baum-Innenseite (Führung) | Wangenblock | 1.000 daN |
| Mast-Fuß (Umlenkung) | Einfachblock Kugellager | 1.200 daN |
| Cockpit (Umlenkung) | Fußblock | 1.000 daN |

### 7.6 Baumniederholer (Vang / Kicking Strap)

| Bootsklasse | System | Untersetzung | Block-Typ |
|------------|--------|-------------|-----------|
| Jolle | Talje | 4:1–6:1 | Miniblöcke Gleitlager |
| Fahrt (10m) | Gasfeder + Talje | 4:1 | 40mm Kugellager |
| Fahrt (14m) | Hydraulikzylinder | — | — |
| Performance | Talje oder Rigid Vang | 6:1–8:1 | 40mm–57mm |

### 7.7 Ausholer (Outhaul)

Zur Verstellung der Unterliek-Spannung des Großsegels.

| Bootsklasse | System | Untersetzung | Block-Typ |
|------------|--------|-------------|-----------|
| Jolle | Direkt oder 2:1 | 2:1 | Miniblock |
| Fahrt | Innenlaufend im Baum | 2:1–4:1 | Wangenblock im Baum |
| Performance | Innenlaufend + Cockpit-Bedinung | 4:1–8:1 | Kugellager im Baum |

### 7.8 Backstag (Backstay Adjuster)

| System | Blocktyp | Untersetzung |
|--------|---------|-------------|
| Talje manuell | Doppel/Dreifach, Kugellager | 8:1–12:1 |
| Talje + Winsch | Doppel, Kugellager | 4:1 + Winsch |
| Hydraulik | — | — |
| Textil-Backstag | Dyneema-Loop | — |

### 7.9 Traveler (Traveller System)

| Komponente | Typ | Bemerkung |
|-----------|-----|-----------|
| Traveler-Wagen | Kugellager-Schlitten | Auf Aluminiumschiene |
| Kontrollleinen (2×) | Einfachblock + Klemmer | Dichtholen/Fieren des Wagens |
| Umlenkung | Endblöcke an Schiene | An den Schienenenden |

---

## 8. Fehlerbild-Atlas

### 8.1 Fehlerbild F01: Scheibenabrieb / Flachstelle (Flat Spot)

**Beschreibung:** Die Scheibe zeigt eine abgeflachte Stelle statt einer runden Kontur. Typisch bei Gleitlagern, die über längere Zeit unter Last stehen, ohne dass die Leine bewegt wird.

**Ursachen:**
- Lange Standzeiten unter Last (Leine steht fest)
- Gleitlager ohne Rotation
- Überlastung (Scheibe verformt sich plastisch)
- Minderwertiges Scheibenmaterial

**Symptome:**
- Ruckeliges Laufen der Leine
- Ratterndes Geräusch bei Leinenbewegung
- Sichtbare Abflachung der Scheibe
- Erhöhter Verschleiß der Leine

**Bewertung:** MITTEL — Funktionsbeeinträchtigung, aber kein Sicherheitsrisiko bei geringer Ausprägung.

**Maßnahme:**
- Leichte Abflachung: Block weiter verwenden, Scheibe regelmäßig drehen lassen
- Starke Abflachung: Scheibe tauschen (wenn möglich) oder Block ersetzen
- Prävention: Leinen regelmäßig bewegen, Last bei Liegezeiten entlasten

**AYDI-Confidence:** visual_medium (erkennbar in Foto bei Nahaufnahme)

### 8.2 Fehlerbild F02: Lagerversagen (Bearing Failure)

**Beschreibung:** Das Lager dreht nicht mehr frei, klemmt oder hat Spiel.

**Ursachen:**
- Korrosion (Salzwasser, fehlende Wartung)
- Überlastung (Lager überlastet, Kugeln verformt)
- Verunreinigung (Sand, Schmutz, Fasern im Lager)
- Alterung (Fettverlust, Dichtungsversagen)

**Symptome:**
- Scheibe dreht schwer oder gar nicht
- Knirschende/kratzende Geräusche
- Fühlbares Spiel in der Scheibe
- Leine rutscht statt die Scheibe zu drehen → extremer Leinenverschleiß

**Bewertung:** HOCH — Erhöhte Reibung = erhöhte Belastung auf Beschläge und Tauwerk. Scheibe, die nicht dreht, zerstört die Leine.

**Maßnahme:**
- Sofort: Block öffnen, reinigen, nachfetten (Teflon-Fett)
- Mittelfristig: Lager austauschen (Ersatzteile bei Harken/Lewmar erhältlich)
- Langfristig: Bei wiederholtem Versagen Block-Upgrade auf abgedichtete Lager

**AYDI-Confidence:** visual_high (erkennbar in Video durch fehlendes Drehen)

### 8.3 Fehlerbild F03: Wangenriss (Cheek Cracking)

**Beschreibung:** Riss oder Bruch in der Seitenwange des Blocks.

**Ursachen:**
- Überlastung (Last über SWL)
- Materialermüdung (zyklische Belastung über Jahre)
- UV-Degradation (bei Kunststoffwangen)
- Schlagbelastung (Block wird gegen Beschlag geschlagen)
- Fertigungsfehler

**Symptome:**
- Sichtbare Risse in der Wange
- Scheibe sitzt schief
- Verformung des Gehäuses
- Geräuschveränderung

**Bewertung:** KRITISCH — Sofortige Entlastung und Austausch. Weiternutzung = Risiko des vollständigen Versagens.

**Maßnahme:**
- Sofort: Block aus dem System nehmen
- Ersatz: Gleiche oder nächstgrößere Blockgröße
- Analyse: Ursache feststellen (Überlastung → System überprüfen)

**AYDI-Confidence:** visual_high (eindeutig in Foto erkennbar)

### 8.4 Fehlerbild F04: Schäkelbolzen-Verschleiß (Shackle Pin Wear)

**Beschreibung:** Der Schäkelbolzen zeigt Materialabtrag an der Kontaktstelle.

**Ursachen:**
- Normaler Verschleiß durch Schwenkbewegung
- Korrosion + mechanischer Abrieb
- Unterschiedliche Metalle (Kontaktkorrosion)
- Unterdimensionierter Schäkel

**Symptome:**
- Rillenbildung am Bolzen
- Spiel im Schäkel
- Bolzen lässt sich nicht mehr lösen (festkorrodiert)
- Bolzen hat sichtbar reduzierten Querschnitt

**Bewertung:** HOCH — Reduzierter Bolzenquerschnitt = reduzierte Bruchlast.

**Maßnahme:**
- Bolzen tauschen (oft Verschleißteil, separat erhältlich)
- Bei >20% Querschnittsverlust: Schäkel komplett tauschen
- Prävention: Edelstahl 316L, regelmäßig lösen und fetten

**AYDI-Confidence:** visual_medium (erkennbar bei Nahaufnahme)

### 8.5 Fehlerbild F05: UV-Degradation

**Beschreibung:** Materialveränderung durch langjährige UV-Einstrahlung.

**Ursachen:**
- Dauerexposition an Deck ohne Abdeckung
- Mangelnder UV-Stabilisator im Material
- Tropische/subtropische Stationierung

**Symptome:**
- Verfärbung (Vergilben, Ausbleichen)
- Versprödung (Material wird brüchig)
- Oberflächenrisse (Crazing)
- Festigkeitsverlust (nicht sichtbar!)

**Betroffene Materialien:**
| Material | UV-Empfindlichkeit | Lebensdauer ohne Schutz |
|----------|-------------------|------------------------|
| Delrin/POM weiß | Mittel | 5–8 Jahre |
| Delrin/POM schwarz | Gering | 8–12 Jahre |
| Nylon/PA | Hoch | 3–5 Jahre |
| Carbo-Composite | Mittel | 7–10 Jahre |
| Aluminium eloxiert | Sehr gering | 15+ Jahre |
| Edelstahl | Keine | Unbegrenzt |

**Bewertung:** MITTEL bis HOCH — Versprödung kann zu Spontanbruch führen.

**Maßnahme:**
- Persenning/Abdeckung über Blöcke bei Liegezeiten
- UV-Schutzspray (z. B. 303 Aerospace Protectant)
- Nach 8–10 Jahren: Kunststoffblöcke tauschen (präventiv)

**AYDI-Confidence:** visual_high (Verfärbung klar erkennbar)

### 8.6 Fehlerbild F06: Rillenbildung in der Scheibe (Line Groove Cutting)

**Beschreibung:** Die Leine gräbt eine Rille in die Scheibe, die tiefer ist als das Standardprofil.

**Ursachen:**
- Leine zu dünn für die Rille
- Sandverschmutzung in der Leine
- Dyneema-Kern schleift unter Last
- Übermäßige Leinengeschwindigkeit (Regatten)

**Symptome:**
- Leine sitzt tiefer in der Scheibe als vorgesehen
- Leine klemmt gelegentlich
- Erhöhter Leinenverschleiß
- Sichtbare tiefe Rille in der Scheibe

**Bewertung:** MITTEL — Fortschreitend, kann zum Klemmen führen.

**Maßnahme:**
- Scheibe tauschen
- Korrekte Leinengröße verwenden
- Leinen regelmäßig mit Süßwasser spülen (Sand entfernen)

**AYDI-Confidence:** visual_medium (erkennbar bei Nahaufnahme)

### 8.7 Fehlerbild F07: Fehlende oder gelöste Splinte

**Beschreibung:** Sicherungssplinte an Schäkelbolzen oder Achsen fehlen oder sind geöffnet.

**Ursachen:**
- Mangelnde Wartung
- Vibrationsbelastung
- Korrosion des Splints
- Vergessen bei Montage

**Symptome:**
- Sichtbar fehlender oder abgeknickter Splint
- Bolzen arbeitet heraus
- Scheibe hat axiales Spiel

**Bewertung:** HOCH — Bolzenverlust = Block fällt auseinander.

**Maßnahme:**
- Sofort: Neuen Splint einsetzen
- Alternative: Sicherungsdraht (Monel-Draht 0,8 mm)
- Prävention: Bei jedem Rigg-Check Splinte kontrollieren

**AYDI-Confidence:** visual_high (gut erkennbar)

### 8.8 Fehlerbild F08: Verdrehte Talje (Twisted Purchase)

**Beschreibung:** Die Parten einer Talje sind verdreht oder verwickelt.

**Ursachen:**
- Fehlende Wirbelschäkel (Anti-Twist)
- Falsche Scherung (Reihenfolge der Parten)
- Leine unter Last verdreht

**Symptome:**
- Talje lässt sich schwer bewegen
- Leinen reiben aneinander
- Blockscheiben stehen schräg
- Leine klemmt zwischen Scheibe und Wange

**Bewertung:** MITTEL — Erhöhte Reibung, potenzielle Beschädigung.

**Maßnahme:**
- Talje entlasten und korrekt scheren
- Wirbelschäkel am oberen Block nachrüsten
- Wirbel (Swivel) zwischen Befestigung und Block

**AYDI-Confidence:** visual_high (klar erkennbar in Foto)

### 8.9 Fehlerbild F09: Korrosion an Metallteilen

**Beschreibung:** Rostbildung, Lochfraß oder Kontaktkorrosion an Metallkomponenten.

**Ursachen:**
- Falsches Material (304 statt 316L)
- Kontaktkorrosion (Aluminium-Edelstahl ohne Isolation)
- Chlorid-Einwirkung (Salzwasser-Konzentration)
- Crevice Corrosion (in Spalten)

**Symptome:**
- Braune Verfärbung (Rost)
- Lochfraß (Pitting) an Oberflächen
- Weiße Ablagerungen (Aluminium-Korrosion)
- Festsitzende Bolzen und Schäkel

**Bewertung:** HOCH — Korrosion reduziert Festigkeit und kann zum Versagen führen.

**Maßnahme:**
- Leichte Korrosion: Reinigung + Schutz (Lanolin, Tef-Gel)
- Lochfraß: Bauteil tauschen
- Prävention: Nur 316L-Edelstahl verwenden, Kontaktkorrosion vermeiden

**AYDI-Confidence:** visual_high (Rost und Pitting sind klar sichtbar)

### 8.10 Fehlerbild F10: Ratschen-Verschleiß (Ratchet Wear)

**Beschreibung:** Der Ratschenmechanismus greift nicht mehr zuverlässig oder rattert.

**Ursachen:**
- Normaler Verschleiß der Ratschen-Zähne
- Korrosion im Mechanismus
- Verunreinigung (Sand, Salz)
- Überlastung

**Symptome:**
- Ratsche greift nicht → Leine rutscht
- Unregelmäßiges Klicken
- Ratsche greift permanent (auch beim Dichtholen)
- Kein Freilauf mehr

**Bewertung:** HOCH — Funktionsverlust, insbesondere bei Handsegelung gefährlich.

**Maßnahme:**
- Reinigen und fetten (spezifisches Ratschenfett, NICHT normales Fett)
- Ratschen-Kit austauschen (Harken bietet Rebuild-Kits)
- Block komplett tauschen bei fortgeschrittenem Verschleiß

**AYDI-Confidence:** visual_low (Verschleiß nur bei Demontage sichtbar)

### 8.11 Fehlerbild F11: Leine klemmt zwischen Scheibe und Wange

**Beschreibung:** Die Leine gerät zwischen die rotierende Scheibe und die feststehende Wange.

**Ursachen:**
- Leinendurchmesser zu dünn für den Block
- Verformte Wangen (Spaltvergrößerung)
- Mantelverschleiß der Leine (Fasern stehen ab)
- Falsches Leinenmaterial (zu weicher Mantel)

**Symptome:**
- Leine klemmt plötzlich
- Leinenbeschädigung (Abrieb, Faserbruch)
- Scheibe dreht nicht mehr
- Extremer Kraftaufwand nötig

**Bewertung:** HOCH — Kontrollverlust über Segel möglich.

**Maßnahme:**
- Korrekte Leine-zu-Block-Zuordnung prüfen
- Abgenutzte Leinen tauschen
- Verformte Wangen → Block tauschen
- Bei häufigem Problem: nächstgrößeren Block verwenden

**AYDI-Confidence:** visual_medium (erkennbar wenn Leine eingeklemmt sichtbar)

### 8.12 Fehlerbild F12: Achsbruch (Axle Failure)

**Beschreibung:** Die zentrale Achse des Blocks bricht oder verbiegt sich.

**Ursachen:**
- Massive Überlastung
- Materialermüdung (nach vielen Lastwechseln)
- Korrosion (Querschnittsreduktion)
- Fertigungsfehler

**Symptome:**
- Scheibe verkippt oder fällt heraus
- Block trennt sich in zwei Hälften
- Katastrophales Versagen

**Bewertung:** KRITISCH — Sofortiger Totalausfall des Blocks.

**Maßnahme:**
- Keine Reparatur möglich, sofortiger Austausch
- Ursache analysieren (Überlastung → System überprüfen)
- Prävention: Regelmäßige Inspektion, Sicherheitsfaktoren einhalten

**AYDI-Confidence:** visual_high (Bruch klar erkennbar)

---

## 9. Troubleshooting-Entscheidungsbaum

### 9.1 Entscheidungsbaum: Block dreht schwer

```
Block dreht schwer/nicht
├── Unter Last?
│   ├── JA → Normaler Betrieb? (Last > SWL?)
│   │   ├── Last normal → Lager defekt
│   │   │   ├── Reinigen + Fetten → Gelöst?
│   │   │   │   ├── JA → Regelmäßig warten
│   │   │   │   └── NEIN → Lager tauschen
│   │   │   └── Lager nicht tauschbar → Block ersetzen
│   │   └── Überlast → Block unterdimensioniert
│   │       └── Nächstgrößeren Block wählen
│   └── NEIN (ohne Last) → Verschmutzung oder Korrosion
│       ├── Süßwasser-Spülung → Gelöst?
│       │   ├── JA → Sand/Salz war Ursache
│       │   └── NEIN → Block öffnen, Lager inspizieren
│       └── Korrosion sichtbar?
│           ├── JA → Lager tauschen oder Block ersetzen
│           └── NEIN → Fremdstoffe (Leinenfasern) entfernen
```

### 9.2 Entscheidungsbaum: Leine klemmt im Block

```
Leine klemmt
├── Leine zwischen Scheibe und Wange?
│   ├── JA → Leinendurchmesser prüfen
│   │   ├── Leine zu dünn → Korrekte Leine verwenden
│   │   └── Leine korrekt → Wangen verformt?
│   │       ├── JA → Block tauschen
│   │       └── NEIN → Mantel der Leine abgenutzt?
│   │           ├── JA → Leine tauschen
│   │           └── NEIN → Seltenes Problem → Beobachten
│   └── NEIN → Leine in Rille verkeilt?
│       ├── JA → Rillenprofil prüfen
│       │   ├── Rille zu eng → Falsche Scheibe für Leinen-Typ
│       │   └── Rille verschlissen → Scheibe tauschen
│       └── NEIN → Talje verdreht?
│           ├── JA → Talje korrekt scheren
│           └── NEIN → Leinenführung prüfen (Winkel?)
```

### 9.3 Entscheidungsbaum: Geräusche am Block

```
Ungewöhnliche Geräusche
├── Quietschen?
│   └── Lager trocken → Fetten (Teflon-Fett)
├── Knirschen/Kratzen?
│   └── Sand/Fremdkörper im Lager
│       └── Spülen + Fetten
├── Klappern/Rattern?
│   ├── Scheibe hat Spiel → Lager verschlissen
│   └── Schäkel lose → Nachziehen + Sichern
├── Klicken (rhythmisch)?
│   └── Ratsche → Normal bei Ratschenblock
│       └── Unregelmäßig? → Ratschen-Verschleiß
└── Knacken?
    └── KRITISCH → Wangenriss oder Achsbruch
        └── Sofort entlasten und inspizieren
```

### 9.4 Entscheidungsbaum: Leistungsverlust der Talje

```
Talje schwergängig / geringe Kraftübersetzung
├── Schoten/Fallen-Kräfte erhöht?
│   ├── JA → Windverhältnisse? Segelgröße?
│   │   └── Normal → System-Wirkungsgrad prüfen
│   └── NEIN → Reibung im System erhöht
│       ├── Lager prüfen (alle Blöcke einzeln)
│       │   └── Defekten Block identifizieren + tauschen
│       ├── Leinenführung prüfen (Knicke, scharfe Umlenkungen)
│       │   └── Zusätzliche Umlenkblöcke setzen
│       └── Leine verschlissen (rauer Mantel)?
│           └── Leine tauschen
```

### 9.5 Entscheidungsbaum: Blockauswahl für Neubau/Refit

```
Blockauswahl
├── Anlage bestimmen (Großschot, Fall, etc.)
│   └── Maximale Arbeitslast berechnen
│       └── Sicherheitsfaktor anwenden
│           └── → Mindest-SWL des Blocks
├── Leinendurchmesser festlegen
│   └── → Mindest-Scheibendurchmesser
├── Lagertyp wählen
│   ├── Hochlast + häufige Bewegung → Kugellager
│   ├── Mittel-Last → Nadellager oder Kugellager
│   └── Niedrig-Last + statisch → Gleitlager
├── Material wählen
│   ├── Blauwasser → Edelstahl 316L
│   ├── Performance → Aluminium oder CFK
│   └── Budget → Carbo/Composite
├── Befestigung wählen
│   ├── Hängend → Schäkel (Swivel wenn Winkel variiert)
│   ├── Flach → Wangenblock (Verschraubung)
│   └── Schiene → Schienenreiter
└── Hersteller/Modell auswählen
    ├── Budget → Viadana, Ronstan Serie, Harken Element
    ├── Standard → Harken Carbo/Midrange, Lewmar Control
    ├── Performance → Harken Black/T2, Ronstan Orbit
    └── Premium → Lewmar Synchro/Ocean, Harken Custom
```

---

## 10. FAQ — Häufige Fragen

### FAQ 01: Wie oft müssen Blöcke gewartet werden?

**Antwort:** Die Wartungsintervalle hängen vom Lagertyp, der Nutzung und der Umgebung ab:

| Lagertyp | Gelegenheitssegler | Vielsegler | Regatta | Tropen/Charter |
|----------|-------------------|------------|---------|---------------|
| Kugellager | Jährlich | Halbjährlich | Monatlich | Halbjährlich |
| Nadellager | Jährlich | Halbjährlich | Monatlich | Halbjährlich |
| Gleitlager | Alle 2 Jahre | Jährlich | — | Jährlich |
| Keramik | Alle 2 Jahre | Jährlich | Halbjährlich | Jährlich |

**Wartungsschritte:**
1. Süßwasserspülung (nach jedem Salzwasser-Einsatz ideal, mindestens monatlich)
2. Sichtkontrolle auf Risse, Korrosion, Verschleiß
3. Drehtest: Jede Scheibe von Hand drehen, auf Leichtgängigkeit prüfen
4. Nachfetten mit PTFE-/Teflon-basiertem Schmiermittel
5. Schäkelbolzen und Splinte prüfen

**Confidence:** documented (Hersteller-Empfehlungen)

### FAQ 02: Kugellager oder Gleitlager — wann lohnt sich der Aufpreis?

**Antwort:** Kugellager lohnen sich immer dann, wenn:
- Die Last regelmäßig über 500 daN liegt
- Die Leine häufig und schnell bewegt wird
- Maximale Effizienz der Talje erforderlich ist
- Die Anlage über Muskelkraft (ohne Winsch) bedient wird

Gleitlager sind ausreichend bei:
- Niedrigen Lasten (<500 daN)
- Seltener Benutzung (Lazy-Jacks, Flaggenfall)
- Budget-Einschränkungen
- Situationen, in denen wartungsfreier Betrieb Priorität hat

### FAQ 03: Kann ich Blöcke verschiedener Hersteller mischen?

**Antwort:** Ja, technisch ist das unproblematisch. Blöcke sind standardisiert bezüglich Leinendurchmesser und Befestigung (Schäkel). Zu beachten:
- Schäkelgrößen können leicht variieren → vor Kauf prüfen
- Ästhetik: Unterschiedliche Designs auf einem Boot können störend wirken
- Ersatzteil-Logistik: Weniger verschiedene Hersteller = einfacher

### FAQ 04: Wie erkenne ich, ob ein Block überlastet wurde?

**Antwort:** Anzeichen einer Überlastung:
- Verformung der Wangen (Aufbiegen)
- Verformung der Scheibe (Ovalität)
- Verfärbung bei Aluminium (dunkle Stellen durch plastische Verformung)
- Schäkelbolzen ist verbogen
- Achse hat Spiel (Lager beschädigt)
- Risse in Wangen oder Befestigung

Bei Verdacht auf Überlastung: Block sofort aus dem System nehmen und ersetzen.

### FAQ 05: Wie entferne ich einen festkorrodierten Schäkelbolzen?

**Antwort:** Stufenweise vorgehen:
1. Kriechöl (WD-40, Caramba, Würth Rost Off) auftragen, 24h einwirken lassen
2. Vorsichtiges Klopfen mit Messinghammer (nicht Stahl auf Edelstahl)
3. Wärme anwenden (Heißluftföhn, 150–200°C)
4. Bolzenausdreher oder Locking Pliers verwenden
5. Letzter Ausweg: Bolzen aufbohren (HSS-Bohrer für Edelstahl)

**Prävention:** Bolzen bei jeder Wartung lösen, reinigen, mit Tef-Gel oder Lanolin wieder einsetzen.

### FAQ 06: Was ist der Unterschied zwischen SWL, WLL und MBL?

**Antwort:**
- **SWL (Safe Working Load):** Historischer Begriff, wird zunehmend durch WLL ersetzt
- **WLL (Working Load Limit):** Maximale Last im Normalbetrieb, offizieller EU-Term
- **MBL (Minimum Breaking Load):** Die niedrigste Last, bei der Versagen auftritt (Test)
- **BL (Breaking Load):** = MBL, gebräuchlicher in der Segelbranche

Zusammenhang: WLL = MBL / Sicherheitsfaktor

### FAQ 07: Sind Dyneema-Soft-Blöcke eine echte Alternative?

**Antwort:** Bedingt. Soft-Blöcke (Dyneema-Loops mit Kunststoff-/Titan-Röhre als Scheibe) sind:
- 60–80% leichter als konventionelle Blöcke
- Höhere Reibung (3–5% vs. 2% bei Kugellagern)
- Begrenzte Lebensdauer der Dyneema-Ummantelung
- Nicht geeignet für häufige schnelle Leinenbewegungen (Wärmeentwicklung)
- Keine Ratschenfunktion möglich

**Empfehlung:** Gut für Fallen-Umlenkung, Lazy-Jacks, Reacher-Systeme. Nicht empfohlen für Großschot-Taljen oder Winsch-Vorblöcke.

### FAQ 08: Wie viele Blöcke braucht meine Yacht?

**Antwort:** Grobe Richtwerte nach Bootstyp:

| Anlage | Jolle | 10m Fahrt | 13m Fahrt | 13m Perf. | 15m Blauws. |
|--------|-------|----------|----------|----------|-------------|
| Großschot | 2–3 | 3–5 | 4–6 | 5–7 | 4–6 |
| Genuaschot | 2 | 2–4 | 3–5 | 4–6 | 4–6 |
| Fallen | 2–4 | 4–6 | 5–8 | 6–10 | 6–8 |
| Reff | 0 | 2–4 | 4–6 | 4–6 | 6–8 |
| Spi/Gennaker | 0–2 | 2–4 | 3–5 | 5–8 | 4–6 |
| Sonstige | 2–4 | 4–8 | 6–10 | 8–15 | 8–12 |
| **Gesamt** | **8–15** | **17–31** | **25–40** | **32–52** | **32–46** |

### FAQ 09: Muss ich alle Blöcke beim Refit tauschen?

**Antwort:** Nein. Systematisch vorgehen:
1. Alle Blöcke inspizieren (Sichtkontrolle, Drehtest, Lasttest)
2. Blöcke in Kategorien einteilen: OK / Wartung nötig / Tauschen
3. Sicherheitskritische Blöcke (Großschot, Fallen, Backstag) zuerst tauschen
4. Blöcke mit Gleitlagern auf Kugellager upgraden, wenn Budget erlaubt
5. Alle Schäkel und Splinte erneuern (günstig, hohe Wirkung)

**Faustregel:** Nach 10–15 Jahren sollten alle Kunststoffblöcke getauscht werden. Edelstahlblöcke halten 20+ Jahre bei guter Wartung.

### FAQ 10: Warum sind Blöcke so teuer?

**Antwort:** Die Preise spiegeln die Anforderungen wider:
- **Material:** Edelstahl 316L, Delrin, Keramik sind teure Werkstoffe
- **Fertigung:** Enge Toleranzen (Lager), Oberflächenbehandlung (Eloxierung)
- **Prüfung:** Jeder Block wird auf Bruchlast getestet (oder stichprobenweise)
- **Entwicklung:** Jahrelange Forschung an Geometrie und Materialien
- **Haftung:** Marine-Produkte tragen Produkthaftung
- **Markt:** Nischenmarkt mit kleinen Stückzahlen

**Tipp:** Großhändler und Saison-Rabatte nutzen. SVB, Compass24, AWN bieten oft 15–25% unter UVP.

### FAQ 11: Welche Blöcke für tropische Gewässer?

**Antwort:** In den Tropen sind besondere Anforderungen zu beachten:
- **UV-Belastung:** Edelstahl oder UV-stabilisiertes Composite (schwarz)
- **Korrosion:** Ausschließlich 316L-Edelstahl, keine Aluminium-Blöcke
- **Feuchtigkeit:** Abgedichtete Lager bevorzugen
- **Wachstum:** Blöcke regelmäßig auf Bewuchs prüfen (Scheiben blockieren)

**Empfehlung:** Lewmar Synchro oder Harken Midrange in Edelstahl.

### FAQ 12: Kann ich Blöcke selbst reparieren?

**Antwort:** Ja, bei vielen Modellen sind Ersatzteile erhältlich:
- **Harken:** Umfangreiche Rebuild-Kits (Scheiben, Lager, Ratschen, Schäkel)
- **Lewmar:** Lager und Scheiben als Ersatzteile
- **Ronstan:** Eingeschränktes Ersatzteil-Angebot
- **Antal/Viadana:** Kaum Ersatzteile, Komplett-Tausch üblich

**Werkzeug:** Sprengring-Zange, kleiner Schraubendreher, PTFE-Fett, Süßwasser, Lappen.

### FAQ 13: Was bedeuten die Farben der Harken-Blöcke?

**Antwort:**
- **Schwarz (Carbo):** Composite-Serie, leicht, Standard
- **Schwarz (Black):** Aluminium-Racing-Serie, eloxiert
- **Grau/Silber (Midrange):** Edelstahl-Standard-Serie
- **Rot (T2):** Hochleistungs-Racing-Serie mit Teflon
- **Orange (Element):** Einstiegs-Serie

Die Farbcodierung hilft bei der schnellen Identifikation der Serie.

### FAQ 14: Brauche ich Ratschenblöcke?

**Antwort:** Ratschenblöcke sind empfehlenswert, wenn:
- Die Großschot ohne Winsch bedient wird (Jolle, kleiner Kielboot)
- Die Spinnaker-Schot von Hand gefahren wird
- Die Crew-Stärke begrenzt ist (Einhandsegler)
- Die Schot unter Last gehalten werden muss (Regatta-Kurse)

Nicht nötig, wenn:
- Eine Winsch die Schot hält
- Die Lasten gering sind
- Ein Klemmer (Cam Cleat) die Last übernimmt

### FAQ 15: Wie messe ich die Bruchlast meines Blocks?

**Antwort:** **Nicht selbst messen!** Die Bruchlast ist auf dem Block geprägt/gedruckt oder in den Hersteller-Datenblättern angegeben. Eigene Bruchversuche sind:
- Gefährlich (Schrapnell-Effekt)
- Nicht normgerecht (definierte Prüfverfahren)
- Nach dem Test ist der Block zerstört

Stattdessen: Modellnummer identifizieren → Herstellerkatalog → Bruchlast ablesen.

### FAQ 16: Was ist ein Kaskadensystem und wann brauche ich es?

**Antwort:** Ein Kaskadensystem teilt eine hohe Untersetzung in zwei hintereinander geschaltete Teil-Systeme. Beispiel: 4:1 × 2:1 = 8:1 Gesamtuntersetzung.

Vorteile gegenüber einem einzelnen 8:1-System:
- Geringerer Reibungsverlust (weniger Scheiben im Weg)
- Grob/Fein-Modus (2:1 für schnelles Holen, dann 4:1 für Feintrimmung)
- Einfachere Handhabung und Wartung

### FAQ 17: Welche Leine passt zu welchem Block?

**Antwort:** Die Leine muss zum Rillen-Profil der Scheibe passen:
- **V-Rille:** Geflochtene Polyester- oder Dyneema-Leinen (Standard)
- **U-Rille:** Dickere Leinen, dreischlaggeflochtene Leinen
- **Draht-Rille:** Nur für Draht oder draht-textil-Kombinationen

Der Leinendurchmesser muss im Bereich des Block-Spezifikation liegen (auf dem Block oder im Katalog angegeben).

### FAQ 18: Kann Salzwasser Kugellager zerstören?

**Antwort:** Ja, definitiv. Salzwasser (NaCl ~3,5%) ist einer der Hauptfeinde von Kugellagern:
- Chlorid-Ionen greifen selbst 316L-Stahl an (Lochfraß)
- Salzkristalle in den Lagern erhöhen Reibung und Abrieb
- Salzlösung wirkt als Elektrolyt → beschleunigte Korrosion

**Gegenmaßnahmen:**
- Regelmäßige Süßwasserspülung
- Abgedichtete Lager bevorzugen (2RS-Dichtung)
- Marine-spezifisches Fett verwenden (z. B. Harken Lubricant, McLube)
- Keramik-Hybridlager sind korrosionsbeständiger (Keramik-Kugeln rosten nicht)

### FAQ 19: Wie lagere ich Ersatzblöcke auf einer Blauwasseryacht?

**Antwort:** Empfohlene Ersatzteil-Ausstattung:
- 2× Einfachblock (passend für Großschot/Genuaschot)
- 1× Snatchblock (universal)
- 2× kleiner Einfachblock (für Reff, Strecker)
- 1 Set Schäkel (verschiedene Größen)
- 1 Set Splinte
- 1× Rebuild-Kit für den häufigsten Blocktyp an Bord
- PTFE-Fett, Kriechöl

**Lagerung:** Trocken, vor UV geschützt, in einem Beutel oder Box.

### FAQ 20: Kann ich einen größeren Block verwenden als spezifiziert?

**Antwort:** Grundsätzlich ja, aber mit Einschränkungen:
- **Gewicht:** Ein größerer Block wiegt mehr (besonders am Mast problematisch)
- **Platz:** Der Block muss physisch in die vorgesehene Position passen
- **Leine:** Der Block muss für den vorhandenen Leinendurchmesser geeignet sein (Leine zu dünn → klemmt)
- **Kosten:** Unnötig hohe Ausgaben

**Faustregel:** Eine Größe hoch ist normalerweise unproblematisch. Zwei Größen hoch → spezifisch prüfen.

### FAQ 21: Was bedeutet "Ratchamatic" bei Harken?

**Antwort:** "Ratchamatic" ist Harkens Markenname für automatisch zuschaltende Ratschenblöcke. Die Ratsche aktiviert sich bei zunehmender Last automatisch (lastabhängig) und deaktiviert sich bei geringer Last. Der Segler muss keinen Schalter betätigen.

Im Gegensatz dazu: "Manual Ratchet" — die Ratsche wird manuell ein-/ausgeschaltet.

### FAQ 22: Welche Blockmarke wird von welcher Werft verbaut (OEM)?

**Antwort:** Typische OEM-Zuordnungen:

| Werft | Haupt-Blockhersteller | Bemerkung |
|-------|----------------------|-----------|
| Bénéteau/Jeanneau | Wichard/Facnor, Harken | Modellabhängig |
| Bavaria | Harken, Lewmar | Modellabhängig |
| Hanse | Harken | Standard |
| Dufour | Harken, Wichard | Modellabhängig |
| Hallberg-Rassy | Lewmar | Premium-Ausstattung |
| Najad | Lewmar, Seldén | Premium |
| X-Yachts | Harken | Performance |
| J-Boats | Harken | Performance/Racing |
| Dehler | Harken | Performance |
| Lagoon (Kat.) | Harken, Lewmar | Modellabhängig |
| Fountaine Pajot | Harken | Standard |
| Swan (Nautor) | Harken, Custom | Superyacht-Segment |

### FAQ 23: Gibt es eine Norm für Blöcke?

**Antwort:** Direkte Block-Normen im Sinne einer ISO-Blockprüfung gibt es nicht in dem Maße wie für Riggschrauben. Relevante Normen sind:
- **EN 13089** (Bergsteigerausrüstung — Rollen): Angewendet auf Segelblöcke teilweise
- **ISO 15085** (Man-over-board-Schutz): Betrifft Befestigung von Deck-Hardware
- **ISO 12215-9** (Zubehör und Ausrüstung): Allgemeine Anforderungen an Deck-Hardware
- **Herstellerinterne Standards:** Harken, Lewmar etc. testen nach eigenen Verfahren, die oft strenger sind als Normen

### FAQ 24: Wie identifiziere ich das Modell eines unbekannten Blocks?

**Antwort:** Schritte zur Identifikation:
1. **Markierung lesen:** Logo, Modellnummer (oft auf der Wange geprägt)
2. **Maße nehmen:** Scheibendurchmesser, Leinenkapazität, Gesamthöhe
3. **Foto:** Hersteller-Website oder Google-Bildersuche
4. **Farbe/Material:** Eingrenzen der Serie (z. B. schwarz Composite = Harken Carbo)
5. **Herstellerservice:** Foto an den Hersteller senden

### FAQ 25: Was sind die häufigsten Fehler bei der Blockauswahl?

**Antwort:**
1. **Unterdimensionierung:** Block zu klein für die tatsächliche Last
2. **Falscher Leinendurchmesser:** Leine zu dünn oder zu dick für die Scheibe
3. **Gleitlager bei Hochlast:** Spart kurzfristig Geld, kostet langfristig Leistung
4. **Fehlender Wirbel (Swivel):** Talje verdreht sich
5. **Aluminium in Salzwasser ohne Isolation:** Kontaktkorrosion
6. **Kein Snatchblock an Bord:** Im Notfall fehlt Flexibilität
7. **Alle Blöcke vom gleichen Typ:** Jede Anlage hat andere Anforderungen
8. **Keine Ersatzteile:** Auf Langfahrt können Blöcke nicht einfach ersetzt werden
9. **Überdimensionierung am Mast:** Unnötiges Gewicht in der Höhe → schlechtere Stabilität
10. **Ignorieren der Umlenkwinkel:** Block-Last ist abhängig vom Umlenkwinkel

---

## 11. Glossar

### A

**Achse (Axle/Pin):** Die zentrale Drehachse eines Blocks, um die sich die Scheibe dreht. Material: Edelstahl 316L oder Titan.

**Arbeitslast (Working Load Limit, WLL):** Die maximale Last, die ein Block im normalen Betrieb dauerhaft tragen darf. Wird vom Hersteller angegeben.

**Aufschießen:** Das ordentliche Aufwickeln einer Leine in kreisförmigen Buchten. Relevant für die Funktion des Blocks: aufgeschossene Leinen laufen ohne Klemmer durch den Block.

### B

**Baumniederholer (Vang/Kicking Strap):** Talje oder Hydraulikzylinder zwischen Baum und Mastfuß zur Kontrolle des Großsegel-Twists. Typisch 4:1- bis 8:1-Untersetzung.

**Becket (Hundsfott):** Befestigungspunkt am Block für die stehende Part einer Talje. Kann als Auge, Bügel oder Textilschlaufe ausgeführt sein.

**Block:** Mechanisches Bauteil zur Umlenkung und Untersetzung von Tauwerk, bestehend aus Scheibe(n), Wangen, Achse und Befestigung.

**Bruchlast (Breaking Load, BL/MBL):** Die Last, bei der ein Block versagt (Verformung >2% oder Bruch). Labormäßig getestet.

### C

**Cam Cleat (Schotklemme):** Klemmvorrichtung mit zwei federbelasteten, gezahnten Backen. Oft in Violinblöcke integriert.

**Carbo:** Harken-Markenname für die Composite-Block-Serie aus glasfaserverstärktem Polymer.

**CFK (Kohlefaserverstärkter Kunststoff):** Material für ultraleichte Hochleistungs-Blockwangen.

### D

**daN (Dekanewton):** Krafteinheit, gebräuchlich in der Segelbranche. 1 daN ≈ 1,02 kgf ≈ 2,25 lbf. 1.000 daN = 1 Tonne Kraft (ungefähr).

**Delrin/Acetal (POM):** Polyoxymethylen. Standard-Scheibenmaterial für Blöcke. Selbstschmierend, chemisch beständig.

**Dirk (Topping Lift):** Leine vom Masttop zum Baum-Ende, die den Baum trägt, wenn das Segel nicht gesetzt ist. Wird über Blöcke am Masttop geführt.

**Doppelblock (Double Block):** Block mit zwei Scheiben, entweder nebeneinander oder übereinander.

### E

**Einscherung (Reeving):** Die Art und Weise, wie eine Leine durch ein Blocksystem geführt wird. Korrekte Einscherung ist entscheidend für die Funktion.

**Eloxierung (Anodizing):** Elektrolytische Oxidation von Aluminium zur Bildung einer harten, korrosionsbeständigen Oberfläche.

### F

**Fall (Halyard):** Leine zum Setzen und Bergen von Segeln. Wird vom Deck über Masttop-Blöcke zum Segelkopf geführt.

**Fiddle Block (Violinblock):** Block mit zwei unterschiedlich großen Scheiben übereinander.

**Flaschenzug (Purchase/Tackle):** System aus Blöcken und Leine zur Kraftübersetzung.

### G

**GFK (Glasfaserverstärkter Kunststoff):** Basis-Material für Composite-Blöcke (z. B. Harken Carbo).

**Gleitlager (Plain Bearing):** Einfachstes Lagerprinzip: Scheibe läuft direkt auf der Achse (Material-zu-Material).

### H

**HMPE (High Modulus Polyethylene):** Handelsnamen: Dyneema, Spectra. Hochfestes Fasermaterial für moderne Leinen und Soft-Blöcke.

**Hundsfott:** Siehe Becket.

### K

**Kaskade (Cascade):** Hintereinanderschaltung zweier Taljensysteme für hohe Untersetzung bei geringer Reibung.

**Kugellager (Ball Bearing):** Wälzlager mit Stahlkugeln. Reibungskoeffizient ~2%. Standard für mittlere bis hohe Lasten.

### L

**Laufende Part (Running/Hauling Part):** Das Ende des Tauwerks, an dem gezogen wird.

**Low-Friction-Ring (LFR):** Alternative zu konventionellen Blöcken. Textilring mit glatter Führungsfläche. Sehr leicht, mittlere Reibung.

### M

**Masttopp (Masthead):** Oberstes Ende des Masts. Hier befinden sich die Fallen-Umlenkblöcke.

**Mechanischer Vorteil (Mechanical Advantage, MA):** Verhältnis von Last zu erforderlicher Zugkraft in einem Flaschenzug.

### N

**Nadellager (Needle Bearing):** Wälzlager mit zylindrischen Rollen statt Kugeln. Kompakt, hohe Tragfähigkeit.

### O

**Orbit-Block:** Ronstan-Patent. Scheibe dreht sich sowohl um die eigene Achse als auch orbital um den Befestigungspunkt.

### P

**Part:** Ein Abschnitt des Tauwerks in einem Flaschenzug zwischen zwei Umlenkpunkten.

**POM (Polyoxymethylen):** Siehe Delrin/Acetal.

**PTFE (Polytetrafluorethylen):** Teflon. Wird als Schmiermittel (PTFE-Fett) und Beschichtung (Harken T2) verwendet.

**Purchase (Talje):** Englischer Begriff für Flaschenzug/Taljensystem.

### R

**Ratsche (Ratchet):** Freilaufkupplung in einem Block, die in einer Richtung freien Lauf ermöglicht und in der anderen klemmt.

**Reffleinen (Reef Lines):** Leinen zum Verkleinern der Segelfläche (Reffen). Werden über Blöcke am Baum und Mast geführt.

**Reeving (Einscherung):** Die korrekte Führung einer Leine durch ein Blocksystem.

### S

**Scheibe (Sheave):** Die drehbare Rolle in einem Block, über die das Tauwerk läuft.

**Schäkel (Shackle):** U-förmiges Verbindungselement mit Bolzen zur Befestigung von Blöcken.

**Schot (Sheet):** Leine zur Steuerung des Segelwinkels zum Wind.

**SWL (Safe Working Load):** Maximale Betriebslast. Gleichbedeutend mit WLL.

**Snatchblock:** Block mit öffenbarer Wange zum seitlichen Einlegen der Leine.

**Splint (Split Pin/Cotter Pin):** Sicherungselement für Bolzen. Verhindert das Herausarbeiten.

**Stehende Part (Standing Part):** Das fest befestigte Ende des Tauwerks in einer Talje.

### T

**Talje (Purchase/Tackle):** System aus Blöcken und Leine zur Kraftübersetzung.

**Torlon (PAI):** Polyamidimid. Hochleistungs-Thermoplast für Scheiben und Lager.

**Traveler:** Schlitten auf einer Querschiene zur seitlichen Verstellung des Großschot-Angriffspunkts.

### U

**Umlenkblock (Turning Block):** Block zur Richtungsänderung einer Leine.

**Umlenkwinkel (Deflection Angle):** Der Winkel, um den eine Leine im Block umgelenkt wird. Beeinflusst die Block-Belastung.

**Untersetzung (Purchase Ratio):** Verhältnis der Kraftübersetzung in einer Talje (z. B. 4:1).

### V

**Violinblock (Fiddle Block):** Block mit zwei unterschiedlich großen Scheiben.

### W

**Wangen (Cheeks):** Die seitlichen Gehäuseteile eines Blocks, die die Scheibe umschließen und die Last auf die Achse übertragen.

**Wirbel (Swivel):** Drehbares Verbindungselement, das ein Verdrillen der Talje verhindert.

**WLL (Working Load Limit):** Maximale Arbeitslast. EU-konformer Begriff für SWL.

---

## 12. Schnell-Referenz

### 12.1 Blockgrößen-Schnellwahl

```
Leinendurchmesser → Blockgröße (Harken-Nomenklatur):
  4–6 mm  → 22mm–29mm Block (Micro/Mini)
  6–8 mm  → 29mm–40mm Block (Small)
  8–10 mm → 40mm–57mm Block (Medium)
 10–12 mm → 57mm–75mm Block (Large)
 12–14 mm → 75mm Block (XL)
 14–18 mm → 75mm–100mm Block (XXL)
```

### 12.2 Lagertyp-Schnellwahl

```
Niedrige Last (<500 daN) + selten bewegt  → Gleitlager
Mittlere Last (500–2000 daN)               → Kugellager (Standard)
Hohe Last (>2000 daN)                      → Kugellager (Premium)
Höchste Last + Regatta                     → Keramik-Hybridlager
Budget + Salzwasser                        → Gleitlager (wartungsfrei)
```

### 12.3 Sicherheitsfaktor-Schnellwahl

```
Regatta, Profi-Crew:      3:1
Fahrt, erfahrene Crew:    4:1
Charter, Ausbildung:      5:1
Gewerblich, Superyacht:   5:1–6:1
Personentragend:          8:1–10:1
```

### 12.4 Hersteller-Schnellwahl

```
Budget:       Viadana, Ronstan Serie, Harken Element
Standard:     Harken Carbo, Lewmar Control
Performance:  Harken Black/T2, Ronstan Orbit
Premium:      Lewmar Synchro/Ocean, Wichard
Superyacht:   Lewmar Ocean, Harken Custom, Antal Mega
```

### 12.5 Anlage-Block-Schnellzuordnung (13m-Fahrtenyacht)

```
Großschot:       4:1–6:1 Talje, 57mm–75mm Kugellager
Genuaschot:      57mm–75mm Kugellager + Schienen-Umlenkblock
Großfall:        75mm Kugellager (Masttop + Deck)
Vorsegel-Fall:   57mm Kugellager (Masttop + Deck)
Spi-Fall:        40mm–57mm Kugellager
Baumniederholer: 4:1 Talje, 40mm Kugellager
Reffleinen:      40mm Kugellager
Backstag:        6:1–8:1 Kaskade, 40mm Kugellager
Traveler:        Kugellager-Wagen + Kontrollleinen
Snatchblöcke:    3–4 Stück, 57mm
```

### 12.6 Wartungs-Schnellplan

```
Nach jedem Segeltag:    Süßwasserspülung (ideal)
Monatlich:              Sichtkontrolle, Drehtest
Halbjährlich:           Nachfetten (PTFE-Fett)
Jährlich:               Vollinspektion, Schäkel prüfen
Alle 5 Jahre:           Lager tauschen (Kugellager)
Alle 10 Jahre:          Kunststoffblöcke ersetzen (UV-Alterung)
Alle 15–20 Jahre:       Edelstahlblöcke überprüfen/ggf. ersetzen
```

---

## ANHANG A — Fallstudien

### Fallstudie A1: Großschot-Upgrade Bavaria 40 (2015)

**Ausgangslage:** Bavaria 40 Cruiser, Baujahr 2008. Original-Großschot mit Lewmar Control 50mm Gleitlager-Blöcken, 4:1-Talje. Crew klagt über schwergängige Großschot, insbesondere bei Starkwind.

**Analyse:**
- Gleitlager nach 7 Jahren deutlich verschlissen (Abrieb, Flat Spots)
- Reibungsverlust in der 4:1-Talje: ~25% (Gleitlager 93%^3 = 80%)
- Effektive Untersetzung: nur 3,2:1 statt 4:1
- Ergänzend: Großschot-Leine (12mm Polyester) war veraltet, rauer Mantel

**Maßnahme:**
- Tausch aller 4 Blöcke gegen Harken 57mm Carbo Air (Kugellager)
- Neue Großschot-Leine: 12mm Dyneema-Kern mit Polyester-Mantel
- Kosten: 4× 65 EUR (Blöcke) + 80 EUR (Leine) = 340 EUR

**Ergebnis:**
- Effektive Untersetzung: 3,84:1 (98%^3 = 94%)
- Subjektiv: "Wie ein neues Boot" (Eigner-Zitat)
- Quantifiziert: ~20% geringerer Kraftaufwand beim Dichtholen

**AYDI-Relevanz:** Typisches Level-2-Analyse-Szenario. Visuell erkennbarer Scheibenverschleiß (F01), messbarer Leistungsgewinn nach Upgrade.

### Fallstudie A2: Snatchblock-Versagen Hallberg-Rassy 36

**Ausgangslage:** HR36, Blauwasseryacht. Auf Atlantiküberquerung versagt ein Snatchblock (Lewmar 60mm, unbekanntes Alter) während eines Spinnaker-Manövers.

**Analyse:**
- Verriegelungsmechanismus des Snatchblocks löste sich unter dynamischer Last
- Ursache: UV-Degradation der Kunststoff-Verriegelung (geschätzt >15 Jahre alt)
- Folge: Spi-Schot rutschte aus dem Block, Kontrollverlust über Spinnaker
- Sekundärschaden: Riss im Spi-Vorliek

**Maßnahme:**
- Alle Snatchblöcke an Bord ersetzt (4 Stück) durch Harken 57mm Snatch
- Alter der Blöcke dokumentiert
- Inspektions-Checkliste für Snatchblock-Verriegelung erstellt

**Ergebnis:**
- Kosten: 4× 85 EUR = 340 EUR + 1.200 EUR Spi-Reparatur
- Lektion: Snatchblock-Verriegelungen sind sicherheitskritisch und altern

**AYDI-Relevanz:** Fehlerbild F05 (UV-Degradation). Potenzielle KRITISCHE Warnung im Condition Report.

### Fallstudie A3: Optimierung Regatta-Yacht J/109

**Ausgangslage:** J/109, Regatta-Einsatz ORC Club. Crew sucht Leistungsoptimierung im Block-System.

**Analyse:**
- Original: Harken Midrange Edelstahl-Blöcke (Standard-Auslieferung)
- Gesamtgewicht Blöcke: ~8,5 kg
- 42 Blöcke an Bord

**Maßnahme:**
- Kritische Blöcke (15 Stück) ersetzt durch Harken T2 (Aluminium + Keramik)
- 12 niedrig belastete Blöcke durch Antal Low-Friction-Ringe ersetzt
- 15 Blöcke beibehalten (Mittellast, Harken Midrange)

**Ergebnis:**
- Gewichtsreduktion: 8,5 kg → 5,2 kg (-3,3 kg / -39%)
- Reibungsreduktion: geschätzt 15–20% im Gesamtsystem
- Kosten: ~2.800 EUR
- ORC-Rating-Verbesserung: Nicht direkt (Blöcke nicht im Rating), aber Performance spürbar

### Fallstudie A4: Superyacht-Blockanlage Nautor Swan 65

**Ausgangslage:** Swan 65 Custom, Neubau. Blockauswahl und -planung für das gesamte Rigg.

**Spezifikation:**
- 78 Blöcke gesamt
- Großschot: 6:1 Kaskade + hydraulische Winsch → Harken 100mm Custom Edelstahl
- Genuaschot: Harken 75mm Black + Lewmar 72 Synchro Umlenkblöcke
- Fallen: Harken 75mm Custom Masttop-Block (5-fach) mit Keramik-Lagern
- Spi-System: Harken 57mm T2 + Snatch 57mm
- Reff: Harken 57mm Midrange
- Alle Schäkel: Wichard geschmiedet 316L

**Kosten Blöcke gesamt:** ~28.000 EUR

**AYDI-Relevanz:** Level-2-Planungswerkzeug. Vollständige Anlagen-Konfiguration mit Kostenschätzung.

### Fallstudie A5: Kontaktkorrosion nach Refit

**Ausgangslage:** X-Yachts Xp44, 3 Jahre nach Refit. Aluminium-Blöcke (Harken Black) auf Edelstahl-Beschlägen zeigen weiße Korrosionsablagerungen.

**Analyse:**
- Kontaktkorrosion (galvanische Korrosion) zwischen Aluminium-Blockwangen und Edelstahl-Schäkel
- Beschleunigt durch Salzwasser als Elektrolyt
- Ursache: Fehlende Isolation zwischen den Metallen beim Refit

**Maßnahme:**
- Alle Aluminium-Edelstahl-Kontaktstellen mit Tef-Gel behandelt
- Kunststoff-Unterlegscheiben zwischen Blockwange und Schäkel eingesetzt
- Regelmäßige Reinigung und Schutzbehandlung

**Ergebnis:**
- Korrosion gestoppt
- Kosten: ~150 EUR (Tef-Gel, Unterlegscheiben, Arbeitszeit)

### Fallstudie A6: Lazy-Jack mit Low-Friction-Ringen

**Ausgangslage:** Jeanneau Sun Odyssey 440, Lazy-Jack-System soll installiert werden. Budget-orientierter Eigner.

**Analyse:**
- Lazy-Jacks tragen geringe Lasten (<100 daN)
- Blöcke werden selten bewegt
- UV-Exposition am Mast hoch

**Lösung:**
- Statt 8 Blöcken: 8 Antal Low-Friction-Ringe (LFR20)
- Gewicht: 8× 12g = 96g statt 8× 80g = 640g
- Kosten: 8× 18 EUR = 144 EUR statt 8× 35 EUR = 280 EUR

**Ergebnis:**
- 54% Kosteneinsparung
- 85% Gewichtseinsparung am Mast
- Funktional: Einwandfrei (geringe Lasten, seltene Bewegung)

### Fallstudie A7: Ratschen-Rebuild Harken 57mm

**Ausgangslage:** Großschot-Ratschenblock Harken 57mm Ratchamatic, 6 Jahre alt. Ratsche greift nicht mehr zuverlässig.

**Diagnose:**
- Visuell: Salzkristalle im Ratschenmechanismus
- Mechanisch: Ratschen-Sperrklinken verschlissen, Feder geschwächt
- Funktional: Ratsche rutscht unter Last → gefährlich bei Starkwind

**Maßnahme:**
- Harken Ratchet Rebuild Kit (#2677) bestellt: 32 EUR
- Demontage: Sprengring entfernen, Scheibe herausnehmen
- Reinigung: Süßwasser + Pinsel
- Neue Ratschen-Komponenten eingesetzt
- Zusammenbau + Schmierung mit Harken OneDrop (spezifisches Ratschen-Öl)

**Ergebnis:**
- Block funktioniert wie neu
- Gesamtkosten: 32 EUR + 1h Arbeitszeit
- Neukauf hätte 140 EUR gekostet

### Fallstudie A8: Fallen-Umlenkung am Mastfuß — Layout-Optimierung

**Ausgangslage:** Dehler 38, alle Fallen zum Cockpit geführt. Ursprünglich über 4 Fußblöcke am Mastfuß. Leinen kreuzen sich, Reibung hoch.

**Analyse:**
- 6 Fallen (Groß, Genua, Spi, 2× Reff, Topp) durch 4 Blöcke → Leinen kreuzen
- Kreuzende Leinen verursachen 20–30% zusätzliche Reibung
- Blöcke zu nah beieinander montiert

**Maßnahme:**
- 4 Fußblöcke durch 6 Organizer-Scheiben (Lewmar Deck Organizer) ersetzt
- Leinen laufen parallel ohne Kreuzung
- Abstand zwischen Leinen: 40mm (statt 15mm)
- Zusätzlich: 2× Umlenkblock in der Kajütdach-Verschanzung

**Ergebnis:**
- Reibung reduziert um geschätzt 25%
- Fallen lassen sich leichter setzen und bergen
- Kein Verheddern mehr
- Kosten: ~350 EUR

---

## ANHANG B — AYDI-Integration (Pydantic-Modelle)

```python
"""
AYDI Block Analysis Models — Pydantic v2
Module: blocks_fundamentals
"""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class BearingType(str, Enum):
    """Types of block bearings."""
    BALL = "ball_bearing"
    NEEDLE = "needle_bearing"
    PLAIN = "plain_bearing"
    CERAMIC_HYBRID = "ceramic_hybrid"
    DYNEEMA_LOOP = "dyneema_loop"


class BlockType(str, Enum):
    """Types of sailing blocks."""
    SINGLE = "single"
    DOUBLE = "double"
    TRIPLE = "triple"
    FIDDLE = "fiddle"
    RATCHET = "ratchet"
    SNATCH = "snatch"
    ORBIT = "orbit"
    CARBO = "carbo"
    FLIP_FLOP = "flip_flop"
    CHEEK = "cheek"
    FOOT = "foot"
    MASTHEAD = "masthead"
    TURNING = "turning"
    HEAVY_DUTY = "heavy_duty"
    LOW_FRICTION_RING = "low_friction_ring"


class SheeveMaterial(str, Enum):
    """Materials for block sheaves."""
    DELRIN = "delrin_pom"
    TORLON = "torlon_pai"
    ALUMINUM = "aluminum_anodized"
    STAINLESS_STEEL = "stainless_316l"
    CARBON_FIBER = "carbon_fiber"
    CERAMIC = "ceramic"


class CheekMaterial(str, Enum):
    """Materials for block cheeks."""
    STAINLESS_316 = "stainless_316"
    ALUMINUM_ANODIZED = "aluminum_anodized"
    CARBON_FIBER = "carbon_fiber"
    COMPOSITE_CARBO = "composite_carbo"
    TITANIUM = "titanium"
    NYLON_GF = "nylon_glass_filled"


class ConfidenceLevel(str, Enum):
    """Confidence levels for assessments."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class BlockManufacturer(str, Enum):
    """Major block manufacturers."""
    HARKEN = "harken"
    LEWMAR = "lewmar"
    ANTAL = "antal"
    RONSTAN = "ronstan"
    SCHAEFER = "schaefer"
    SELDEN = "selden"
    WICHARD = "wichard"
    VIADANA = "viadana"
    OTHER = "other"


class RiggingApplication(str, Enum):
    """Applications / rigging positions for blocks."""
    MAINSHEET = "mainsheet"
    GENOA_SHEET = "genoa_sheet"
    SPINNAKER_SHEET = "spinnaker_sheet"
    SPINNAKER_HALYARD = "spinnaker_halyard"
    MAIN_HALYARD = "main_halyard"
    GENOA_HALYARD = "genoa_halyard"
    REEF_LINE = "reef_line"
    VANG = "vang"
    OUTHAUL = "outhaul"
    BACKSTAY = "backstay"
    TRAVELER = "traveler"
    CUNNINGHAM = "cunningham"
    TOPPING_LIFT = "topping_lift"
    LAZY_JACKS = "lazy_jacks"
    BARBER_HAULER = "barber_hauler"


class BoatClassBlock(str, Enum):
    """Boat classes for block sizing."""
    DINGHY = "dinghy_4_8m"
    CRUISER_SMALL = "cruiser_8_14m"
    PERFORMANCE_CRUISER = "performance_10_16m"
    BLUEWATER = "bluewater_12_18m"
    RACER = "racer_8_20m"
    MOTOR_YACHT = "motor_yacht_8_25m"
    SUPERYACHT = "superyacht_18m_plus"


class FailurePattern(str, Enum):
    """Block failure patterns."""
    SHEAVE_FLAT_SPOT = "sheave_flat_spot"
    BEARING_FAILURE = "bearing_failure"
    CHEEK_CRACKING = "cheek_cracking"
    SHACKLE_PIN_WEAR = "shackle_pin_wear"
    UV_DEGRADATION = "uv_degradation"
    LINE_GROOVE_CUTTING = "line_groove_cutting"
    MISSING_SPLIT_PIN = "missing_split_pin"
    TWISTED_PURCHASE = "twisted_purchase"
    CORROSION = "corrosion"
    RATCHET_WEAR = "ratchet_wear"
    LINE_JAMMING = "line_jamming"
    AXLE_FAILURE = "axle_failure"


class FailureSeverity(str, Enum):
    """Severity levels for failures."""
    LOW = "niedrig"
    MEDIUM = "mittel"
    HIGH = "hoch"
    CRITICAL = "kritisch"


# ─── Core Data Models ────────────────────────────────────────────────

class BlockSpecification(BaseModel):
    """Specification of a single block."""

    model_config = {"from_attributes": True}

    block_type: BlockType
    manufacturer: BlockManufacturer
    model_name: str = Field(..., description="Manufacturer model name")
    model_number: Optional[str] = None

    sheave_diameter_mm: float = Field(..., ge=10, le=200)
    sheave_count: int = Field(1, ge=1, le=6)
    sheave_material: SheeveMaterial
    bearing_type: BearingType

    max_line_diameter_mm: float = Field(..., ge=2, le=30)
    min_line_diameter_mm: float = Field(..., ge=1, le=25)

    breaking_load_dan: float = Field(..., ge=50, description="Breaking load in daN")
    working_load_dan: float = Field(..., ge=25, description="Working load in daN")
    safety_factor: float = Field(4.0, ge=2.0, le=10.0)

    weight_g: float = Field(..., ge=1, description="Weight in grams")

    cheek_material: CheekMaterial
    has_swivel: bool = False
    has_becket: bool = False
    has_ratchet: bool = False
    has_cam_cleat: bool = False

    price_eur: Optional[float] = Field(None, ge=0)
    price_confidence: ConfidenceLevel = ConfidenceLevel.ESTIMATED


class PurchaseSystem(BaseModel):
    """Configuration of a purchase (tackle) system."""

    model_config = {"from_attributes": True}

    application: RiggingApplication
    purchase_ratio: str = Field(..., description="e.g., '4:1' or '4:1 x 2:1'")
    is_cascade: bool = False
    cascade_stages: Optional[list[str]] = Field(
        None,
        description="e.g., ['4:1', '2:1'] for a cascade"
    )

    blocks: list[BlockSpecification] = Field(
        ..., min_length=1, description="Blocks in the system"
    )

    total_sheave_count: int = Field(..., ge=1)
    theoretical_ma: float = Field(..., ge=1.0, description="Theoretical mechanical advantage")
    actual_ma: float = Field(..., ge=1.0, description="Actual MA with friction losses")
    system_efficiency: float = Field(..., ge=0.0, le=1.0, description="Overall system efficiency")

    max_load_dan: float = Field(..., ge=0)
    hauling_load_dan: float = Field(..., ge=0, description="Force required at hauling part")


class BlockConditionAssessment(BaseModel):
    """Assessment of a block's condition."""

    model_config = {"from_attributes": True}

    block_spec: Optional[BlockSpecification] = None
    location: str = Field(..., description="Location on the yacht (e.g., 'Masttop Stb')")
    application: RiggingApplication

    age_years: Optional[float] = Field(None, ge=0)
    estimated_cycles: Optional[int] = Field(None, ge=0)

    failure_patterns: list[FailurePattern] = Field(default_factory=list)
    severity: FailureSeverity = FailureSeverity.LOW
    is_functional: bool = True

    bearing_condition: str = Field(
        "nicht_beurteilt",
        description="Bearing condition: gut, verschlissen, defekt, nicht_beurteilt"
    )
    sheave_condition: str = Field(
        "nicht_beurteilt",
        description="Sheave condition: gut, abgenutzt, beschaedigt, nicht_beurteilt"
    )
    cheek_condition: str = Field(
        "nicht_beurteilt",
        description="Cheek condition: gut, rissig, gebrochen, nicht_beurteilt"
    )
    shackle_condition: str = Field(
        "nicht_beurteilt",
        description="Shackle condition: gut, verschlissen, korrodiert, nicht_beurteilt"
    )

    uv_exposure: str = Field(
        "mittel",
        description="UV exposure level: gering, mittel, hoch, extrem"
    )

    recommendation: str = Field(
        ...,
        description="Action recommendation in German"
    )
    recommended_replacement: Optional[BlockSpecification] = None

    confidence: ConfidenceLevel = ConfidenceLevel.VISUAL_MEDIUM
    notes: Optional[str] = None


class BlockSystemAnalysis(BaseModel):
    """Complete analysis of all blocks on a yacht."""

    model_config = {"from_attributes": True}

    boat_class: BoatClassBlock
    boat_name: Optional[str] = None
    boat_type: Optional[str] = None
    boat_loa_m: Optional[float] = Field(None, ge=2, le=100)

    total_block_count: int = Field(0, ge=0)
    assessed_block_count: int = Field(0, ge=0)

    blocks: list[BlockConditionAssessment] = Field(default_factory=list)
    purchase_systems: list[PurchaseSystem] = Field(default_factory=list)

    overall_score: float = Field(0, ge=0, le=100)
    condition_score: float = Field(0, ge=0, le=100)
    appropriateness_score: float = Field(0, ge=0, le=100)

    critical_findings: list[str] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)
    suggestions: list[str] = Field(default_factory=list)

    estimated_replacement_cost_eur: Optional[float] = None
    estimated_upgrade_cost_eur: Optional[float] = None

    confidence: ConfidenceLevel = ConfidenceLevel.VISUAL_MEDIUM
    analysis_version: str = "1.0.0"


class FrictionCalculation(BaseModel):
    """Friction and efficiency calculation for a block system."""

    model_config = {"from_attributes": True}

    bearing_type: BearingType
    friction_coefficient: float = Field(..., ge=0.0, le=0.5)
    efficiency_per_sheave: float = Field(..., ge=0.5, le=1.0)

    sheave_count: int = Field(..., ge=1)
    system_efficiency: float = Field(..., ge=0.0, le=1.0)

    theoretical_ma: float = Field(..., ge=1.0)
    actual_ma: float = Field(..., ge=0.5)

    load_dan: float = Field(..., ge=0)
    hauling_force_dan: float = Field(..., ge=0)
    head_block_load_dan: float = Field(..., ge=0)


class DeflectionLoadCalculation(BaseModel):
    """Load calculation based on deflection angle."""

    model_config = {"from_attributes": True}

    line_load_dan: float = Field(..., ge=0)
    deflection_angle_deg: float = Field(..., ge=0, le=180)
    block_load_factor: float = Field(..., ge=0, le=2.0)
    block_load_dan: float = Field(..., ge=0)


class BlockRecommendation(BaseModel):
    """Block recommendation for a specific application."""

    model_config = {"from_attributes": True}

    application: RiggingApplication
    boat_class: BoatClassBlock

    required_swl_dan: float = Field(..., ge=0)
    required_line_diameter_mm: float = Field(..., ge=0)

    recommended_blocks: list[BlockSpecification] = Field(..., min_length=1)
    alternative_blocks: list[BlockSpecification] = Field(default_factory=list)

    estimated_total_cost_eur: Optional[float] = None
    confidence: ConfidenceLevel = ConfidenceLevel.ESTIMATED
    notes: Optional[str] = None
```

---

## ANHANG C — Normen und Standards

### C.1 Direkt relevante Normen

| Norm | Titel | Relevanz für Blöcke |
|------|-------|---------------------|
| ISO 12215-9:2012 | Kleinfahrzeuge — Rumpfbau und Dimensionierung — Teil 9: Zubehör und Ausrüstung | Allgemeine Anforderungen an Decksbeschläge inkl. Blöcke |
| ISO 15085:2003 | Kleinfahrzeuge — Verhütung des Überbordgehens und Wiedereinstieg | Befestigung von Deck-Hardware, die als Haltepunkt dienen könnte |
| EN 13089:2011+A1:2015 | Bergsteigerausrüstung — Rollen | Teilweise angewendet auf Segelblöcke (Bruchlastprüfung) |
| ISO 8212:1986 | Segelzubehör — Blöcke | Historische Norm für Segelblöcke (teilweise ersetzt) |
| DNV GL Rules for Classification | Yachten >24m | Anforderungen an Decksbeschläge für klassifizierte Yachten |

### C.2 Indirekt relevante Normen

| Norm | Titel | Relevanz |
|------|-------|----------|
| ISO 12217:2022 | Stabilität und Auftrieb | Gewicht der Blöcke beeinflusst Stabilitätsberechnung |
| ISO 12215-5:2019 | Dimensionierung Rumpf | Befestigungspunkte der Blöcke auf dem Deck |
| ISO 9094:2015 | Brandschutz | Materialanforderungen (selbstverlöschend) |
| ISO 10133:2012 | Elektrische Systeme (NV) | Kabelführung durch Blockbereiche |

### C.3 Hersteller-Prüfverfahren

**Harken-Prüfverfahren:**
- Statische Bruchlastprüfung: Block wird in Prüfmaschine bis zum Versagen belastet
- Dynamische Ermüdungsprüfung: 100.000 Lastwechsel bei 50% WLL
- Salzsprühtest: 500h bei 5% NaCl (ASTM B117)
- UV-Prüfung: 2.000h Xenon-Arc (ASTM G155)

**Lewmar-Prüfverfahren:**
- Ähnlich Harken, zusätzlich:
- Seitenbelastungstest: 30° Seitenzug bei 50% WLL
- Extremtemperaturtest: -20°C bis +60°C Funktionsprüfung

---

## ANHANG D — Lasttabellen

### D.1 Großschot-Lasten nach Bootsgröße und Windstärke (daN)

| LOA (m) | 2 Bft | 3 Bft | 4 Bft | 5 Bft | 6 Bft | 7 Bft | 8 Bft |
|---------|-------|-------|-------|-------|-------|-------|-------|
| 6 | 30 | 60 | 100 | 160 | 250 | 350 | 500 |
| 8 | 50 | 100 | 180 | 300 | 450 | 650 | 900 |
| 10 | 80 | 160 | 280 | 450 | 700 | 1.000 | 1.400 |
| 12 | 120 | 240 | 400 | 650 | 1.000 | 1.400 | 2.000 |
| 14 | 160 | 320 | 550 | 900 | 1.350 | 1.900 | 2.700 |
| 16 | 200 | 400 | 700 | 1.100 | 1.700 | 2.400 | 3.400 |
| 18 | 250 | 500 | 850 | 1.350 | 2.100 | 3.000 | 4.200 |
| 20 | 300 | 600 | 1.000 | 1.600 | 2.500 | 3.500 | 5.000 |

**Confidence:** estimated (berechnet aus Segelfläche × Winddruck × Schotgeometrie)

### D.2 Genuaschot-Lasten nach Bootsgröße und Windstärke (daN)

| LOA (m) | 2 Bft | 3 Bft | 4 Bft | 5 Bft | 6 Bft | 7 Bft | 8 Bft |
|---------|-------|-------|-------|-------|-------|-------|-------|
| 8 | 80 | 160 | 280 | 480 | 720 | 1.050 | 1.400 |
| 10 | 120 | 250 | 420 | 700 | 1.050 | 1.500 | 2.100 |
| 12 | 170 | 350 | 600 | 1.000 | 1.500 | 2.100 | 3.000 |
| 14 | 220 | 450 | 780 | 1.300 | 1.950 | 2.750 | 3.900 |
| 16 | 280 | 560 | 960 | 1.600 | 2.400 | 3.400 | 4.800 |
| 18 | 340 | 680 | 1.160 | 1.950 | 2.900 | 4.100 | 5.800 |

### D.3 Fall-Lasten nach Bootsgröße (maximale Betriebslast, daN)

| LOA (m) | Großfall | Vorsegel-Fall | Spi-Fall | Topp-Fall |
|---------|---------|---------------|---------|-----------|
| 6 | 400 | 300 | 200 | 100 |
| 8 | 700 | 550 | 350 | 150 |
| 10 | 1.100 | 850 | 500 | 200 |
| 12 | 1.600 | 1.200 | 750 | 300 |
| 14 | 2.200 | 1.700 | 1.000 | 400 |
| 16 | 2.800 | 2.200 | 1.300 | 500 |
| 18 | 3.500 | 2.800 | 1.600 | 600 |
| 20 | 4.200 | 3.400 | 2.000 | 750 |

**Confidence:** measured (Rigg-Monitoring-Daten, Durchschnitt mehrerer Quellen)

### D.4 Sicherheitsfaktor-Berechnung: Mindest-Bruchlast des Blocks

**Formel:** BL_min = Max_Betriebslast × Sicherheitsfaktor × Dynamik-Faktor

**Beispiel: Genuaschot-Block, 13m Fahrtenyacht, Sicherheitsfaktor 4, Böenfaktor 1,5:**

```
BL_min = 1.500 daN × 4 × 1,5 = 9.000 daN
→ Block mit mindestens 9.000 daN Bruchlast wählen
→ z.B. Harken 75mm (BL 8.000 daN) — NICHT ausreichend!
→ z.B. Lewmar Ocean-Serie (BL bis 10.000 daN, siehe Abschn. 6.2) — ausreichend
```

> ⚠️ **ZU PRÜFEN (Audit):** Ursprünglich stand hier "Lewmar Synchro 72mm (BL 10.000 daN)". Das ist falsch: Die Lewmar Synchro 72mm hat laut Hersteller-/Händler-Datenblatt eine WLL von 1.100 kg (2.420 lb ≈ 1.079 daN) und ist **kein** 10.000-daN-Block. Die 10.000-daN-Bruchlast gehört zur Lewmar **Ocean**-Serie (Abschn. 6.2, 4.000–10.000 daN). Die exakte Bruchlast des konkret gewählten Ocean-Modells vor Verwendung im Lewmar-Katalog verifizieren (**estimated — unverifiziert**).

**Hinweis:** In der Praxis werden Dynamik-Faktoren oft nicht separat ausgewiesen, sondern in den empfohlenen Sicherheitsfaktor eingerechnet. Harken und Lewmar geben WLL an, die bereits einen Sicherheitsfaktor beinhalten.

---

## ANHANG E — Confidence-Mapping

### E.1 Confidence-Level pro Datenquelle

| Datenquelle | Confidence-Level | Begründung |
|------------|-----------------|------------|
| Hersteller-Datenblatt (TDS) | measured | Labordaten, geprüft |
| Hersteller-Katalog | documented | Veröffentlichte Spezifikationen |
| Fachliteratur (Bethwaite, Marchaj) | documented | Wissenschaftlich basiert |
| Segelfachpresse (YACHT, Sail) | documented | Redaktionell geprüft |
| Forum-Konsens (Segeln-Forum.de) | estimated | Erfahrungswerte, nicht verifiziert |
| Rigg-Monitoring-Systeme | measured | Sensor-Daten |
| AYDI-Berechnung | calculated | Aus measured-Daten abgeleitet |
| Visuelle Inspektion (Foto) | visual_high bis visual_low | Abhängig von Bildqualität |
| Altersschätzung | estimated | Ungefähre Angabe |
| Preise | estimated | Marktpreise variieren |

### E.2 Confidence-Level für AYDI-Analyseergebnisse

| Analyse-Aspekt | Level 1 (Schnellanalyse) | Level 2 (Profi-Werkzeug) |
|---------------|-------------------------|--------------------------|
| Blocktyp-Identifikation | visual_medium | measured |
| Zustandsbewertung | visual_medium | measured + visual_high |
| Lastberechnung | estimated | calculated |
| Dimensionierungsprüfung | estimated | measured |
| Verschleißprognose | estimated | calculated |
| Kostenabschätzung | benchmark | calculated |
| Handlungsempfehlung | estimated | calculated + documented |

---

## ANHANG F — Wartungsintervalle

### F.1 Wartungsmatrix nach Block-Typ und Umgebung

| Wartungsmaßnahme | Süßwasser-Revier | Küsten-Segler | Blauwasser | Tropen/Charter |
|-----------------|-----------------|--------------|------------|----------------|
| Süßwasserspülung | Monatlich | Wöchentlich | Nach Salzwasser | Wöchentlich |
| Sichtkontrolle | Vierteljährlich | Monatlich | Monatlich | Monatlich |
| Drehtest alle Scheiben | Halbjährlich | Vierteljährlich | Monatlich | Monatlich |
| Nachfetten (PTFE) | Jährlich | Halbjährlich | Vierteljährlich | Vierteljährlich |
| Schäkel/Splinte prüfen | Jährlich | Halbjährlich | Vierteljährlich | Vierteljährlich |
| Vollständige Demontage | Alle 3 Jahre | Alle 2 Jahre | Jährlich | Jährlich |
| Lager-Austausch | Alle 8 Jahre | Alle 5 Jahre | Alle 3 Jahre | Alle 3 Jahre |
| Komplett-Tausch (Kunststoff) | Alle 15 Jahre | Alle 10 Jahre | Alle 8 Jahre | Alle 6 Jahre |
| Komplett-Tausch (Edelstahl) | Alle 25 Jahre | Alle 20 Jahre | Alle 15 Jahre | Alle 10 Jahre |

### F.2 Schmierung

**Empfohlene Schmierstoffe:**

| Schmierstoff | Anwendung | Hersteller |
|-------------|-----------|------------|
| Harken OneDrop | Ratschen-Mechanismen | Harken |
| Harken Pawl Oil | Block-Lager allgemein | Harken |
| McLube Sailkote | Leinen + Scheiben | McLube/Harken |
| Tef-Gel | Gewinde, Schäkel (Anti-Seize) | Sealand Technology |
| Lanocote/Lanolin | Schäkelbolzen, Achsen | Forespar |
| PTFE-Fett (Teflon) | Kugellager | Diverse |

**Nicht verwenden:**
- WD-40 als Langzeitschmiermittel (nur als Kriechöl/Reiniger)
- Silikonfett in Ratschenblöcken (hebt die Ratsche auf)
- Normales Maschinenfett (zieht Schmutz an, verharzt)

---

## ANHANG G — Historische Entwicklung

### G.1 Meilensteine der Blocktechnik

| Jahr | Meilenstein | Bedeutung |
|------|-----------|-----------|
| ~3000 v.Chr. | Erste Holzblöcke | Ägyptische/phönizische Schifffahrt |
| ~1200 | Lignum-vitae-Blöcke | Selbstschmierendes Tropenholz wird Standard |
| 1803 | Blockmills Portsmouth | Erste industrielle Massenproduktion (Brunel) |
| ~1850 | Metallachsen | Bronze/Messing ersetzt Holzachsen |
| ~1920 | Kugellager-Blöcke | Erste Anwendung aus der Industrie |
| 1967 | Gründung Harken | Beginn der modernen Blockentwicklung |
| 1970 | Harken Ratschenblock | Revolution in der Schot-Handhabung |
| 1975 | Delrin-Scheiben | Kunststoff ersetzt Metall für Standard-Anwendungen |
| 1980 | Carbo-Blöcke | Leichte Composite-Blöcke für jedermann |
| 1990 | Keramik-Hybridlager | Höchste Effizienz im Regattabereich |
| 1995 | CFK-Wangen | Kohlefaser-Blöcke für Hochleistung |
| 2005 | Ronstan Orbit | Orbital-drehbare Scheibe (Patent) |
| 2008 | Harken T2 | Teflon-beschichtete Racing-Serie |
| 2012 | Low-Friction-Ringe | Textil-Alternative zu konventionellen Blöcken |
| 2015 | Dyneema-Soft-Blöcke | Textile Blöcke ohne Metallteile |
| 2020 | 3D-gedruckte Blöcke | Prototypen für Custom-Anwendungen |

### G.2 Entwicklung der Bruchlasten (57mm-Einfachblock, Kugellager)

| Jahrzehnt | Typische Bruchlast | Material |
|-----------|-------------------|----------|
| 1970er | 1.500 daN | Bronze/Messing |
| 1980er | 2.000 daN | Edelstahl/Delrin |
| 1990er | 2.500 daN | Edelstahl/Delrin optimiert |
| 2000er | 3.000 daN | Aluminium/Torlon |
| 2010er | 3.500 daN | Aluminium + Keramiklager |
| 2020er | 4.000 daN | CFK/Titan + Keramiklager |

---

## ANHANG H — Bezugsquellen

### H.1 Online-Händler (Deutschland/Europa)

| Händler | Land | Stärken | Rabatte |
|---------|------|---------|---------|
| SVB (svb-marine.de) | DE | Breites Sortiment, guter Service | 10–15% auf UVP |
| Compass24 (compass24.de) | DE | Große Auswahl, Markenvielfalt | 10–20% auf UVP |
| AWN (awn.de) | DE | Premiumnhandel, Beratung | Gering |
| Toplicht (toplicht.de) | DE | Hamburger Traditions-Händler | 5–15% |
| 12seemeilen.de | DE | Discounter, günstige Preise | 15–30% auf UVP |
| Promarine (pro-marine.de) | DE | Profi-Segment | Mengenrabatt |
| AD Nautik (ad-nautik.de) | DE | Süddeutschland, Bootszubehör | 10–15% |
| Force 4 (force4.co.uk) | UK | UK-Markt, gute Lewmar-Preise | 15–25% |
| Marine Superstore (marinesuperstore.com) | UK | Großes UK-Sortiment | 10–20% |
| Accastillage Diffusion (accastillage-diffusion.com) | FR | Französischer Markt | 10–20% |
| Nauticalia (nauticalia.es) | ES | Spanischer Markt | 10–15% |

### H.2 Direkt-Bezug beim Hersteller

| Hersteller | Direkt-Kauf | Ersatzteile | Online-Shop |
|-----------|------------|-------------|-------------|
| Harken | Nein (über Händler) | Ja (harken.com) | Nein |
| Lewmar | Nein (über Händler) | Ja (lewmar.com) | Nein |
| Ronstan | Nein (über Händler) | Eingeschränkt | Nein |
| Antal | Teils direkt (antal.it) | Eingeschränkt | Ja |
| Viadana | Teils direkt (viadana.it) | Nein | Ja |

### H.3 Gebrauchte Blöcke

Gebrauchte Blöcke können eine wirtschaftliche Option sein, erfordern aber Inspektion:

**Quellen:**
- eBay Kleinanzeigen / eBay
- Segeln-Forum.de Marktplatz
- YachtWorld / boat24.com (bei Bootskäufen)
- Regatta-Flohmärkte
- Yacht-Verschrottung

**Checkliste Gebraucht-Kauf:**
- [ ] Modell und Hersteller identifizieren
- [ ] Bruchlast nachschlagen
- [ ] Scheibe auf Flat Spots prüfen
- [ ] Lager auf Leichtgängigkeit prüfen
- [ ] Wangen auf Risse inspizieren
- [ ] UV-Schäden (Versprödung, Verfärbung) prüfen
- [ ] Schäkel auf Verschleiß prüfen
- [ ] Splinte vorhanden?

---

## ANHANG I — Herstellervergleich Detailtabellen

### I.1 Harken 57mm Vergleich über Serien

| Eigenschaft | Element 57 | Carbo 57 | Midrange 57 | Black 57 | T2 57 |
|------------|-----------|----------|-------------|---------|-------|
| Wangen | Nylon | Carbo-Composite | Edelstahl 316 | Aluminium | Aluminium + PTFE |
| Scheibe | Delrin | Delrin | Delrin | Aluminium | Torlon |
| Lager | Gleitlager | Delrin GL | Kugellager | Kugellager | Keramik-Hybrid |
| Bruchlast (daN) | 1.200 | 1.800 | 2.500 | 3.500 | 3.800 |
| WLL (daN) | 300 | 450 | 625 | 875 | 950 |
| Gewicht (g) | 95 | 112 | 195 | 142 | 118 |
| Max. Leine (mm) | 12 | 12 | 12 | 12 | 12 |
| Preis (EUR ca.) | 15 | 35 | 55 | 80 | 130 |

> ⚠️ **ZU PRÜFEN (Audit):** Bruchlast/WLL dieser 57-mm-Serien (WLL 300–950 daN, Bruchlast 1.200–3.800 daN) widersprechen der Spalte "Typische SWL" in Abschnitt 5.2 (dort 1.200–2.500 daN für 40–57-mm-Blöcke). Ohne Abgleich mit dem jeweiligen Hersteller-Datenblatt sind diese Werte als **estimated — unverifiziert** zu führen.

### I.2 57mm-Klasse Herstellervergleich

| Eigenschaft | Harken 57 Carbo | Lewmar 50 Control | Ronstan 55 Orbit | Antal 55 Classic | Viadana 57 |
|------------|----------------|-------------------|------------------|-----------------|-----------|
| Wangen | Composite | Aluminium | Composite | Edelstahl | Nylon |
| Scheibe | Delrin | Acetal | Acetal | Delrin | Delrin |
| Lager | Gleitlager | Kugellager | Kugellager | Kugellager | Gleitlager |
| Bruchlast (daN) | 1.800 | 2.200 | 2.800 | 2.500 | 1.500 |
| Gewicht (g) | 112 | 165 | 98 | 180 | 90 |
| Preis (EUR ca.) | 35 | 45 | 50 | 40 | 22 |

---

## ANHANG J — Blockauswahl-Algorithmus

### J.1 Algorithmus-Beschreibung

Der AYDI-Blockauswahl-Algorithmus ermittelt den optimalen Block für eine gegebene Anwendung:

```python
"""
AYDI Block Selection Algorithm — Pseudocode
"""


def select_block(
    application: str,
    boat_class: str,
    line_diameter_mm: float,
    max_load_dan: float,
    safety_factor: float = 4.0,
    priority: str = "balanced",  # "weight", "cost", "performance", "durability"
) -> list[dict]:
    """
    Select optimal block for given parameters.

    Returns ranked list of suitable blocks.
    """
    required_bl = max_load_dan * safety_factor

    # Step 1: Filter by line diameter
    candidates = filter_by_line_diameter(line_diameter_mm)

    # Step 2: Filter by breaking load
    candidates = [b for b in candidates if b.breaking_load_dan >= required_bl]

    # Step 3: Filter by application suitability
    candidates = filter_by_application(candidates, application)

    # Step 4: Filter by boat class (material, corrosion requirements)
    candidates = filter_by_boat_class(candidates, boat_class)

    # Step 5: Rank by priority
    if priority == "weight":
        candidates.sort(key=lambda b: b.weight_g)
    elif priority == "cost":
        candidates.sort(key=lambda b: b.price_eur or float("inf"))
    elif priority == "performance":
        candidates.sort(key=lambda b: friction_coefficient(b.bearing_type))
    elif priority == "durability":
        candidates.sort(
            key=lambda b: durability_score(b),
            reverse=True,
        )
    else:  # balanced
        candidates.sort(
            key=lambda b: balanced_score(b),
            reverse=True,
        )

    return candidates[:5]  # Top 5 recommendations
```

### J.2 Scoring-Funktion

```python
def balanced_score(block: dict) -> float:
    """Calculate balanced score for block ranking."""
    score = 0.0

    # Performance (30%)
    friction = friction_coefficient(block["bearing_type"])
    score += (1.0 - friction / 0.10) * 30

    # Weight efficiency (20%)
    weight_ratio = block["breaking_load_dan"] / block["weight_g"]
    score += min(weight_ratio / 50, 1.0) * 20

    # Durability (25%)
    score += durability_score(block) * 25

    # Cost efficiency (25%)
    cost_ratio = block["breaking_load_dan"] / (block["price_eur"] or 100)
    score += min(cost_ratio / 50, 1.0) * 25

    return score
```

---

## ANHANG K — Prüfprotokolle

### K.1 Block-Inspektionsprotokoll

```
AYDI BLOCK-INSPEKTIONSPROTOKOLL
================================

Yacht: __________________ LOA: ______m  Typ: ______________
Datum: __________________ Prüfer: _________________________

Block Nr.: _____  Position: ____________________________
Hersteller: ____________  Modell: _______________________
Geschätztes Alter: _______ Jahre

SICHTKONTROLLE:
□ Wangen intakt, keine Risse               [OK / MANGEL / N/A]
□ Scheibe rund, keine Flat Spots            [OK / MANGEL / N/A]
□ Schäkel intakt, kein Verschleiß          [OK / MANGEL / N/A]
□ Splint/Sicherung vorhanden               [OK / MANGEL / N/A]
□ Keine Korrosion sichtbar                  [OK / MANGEL / N/A]
□ Keine UV-Schäden (Versprödung)           [OK / MANGEL / N/A]

FUNKTIONSPRÜFUNG:
□ Scheibe dreht frei (ohne Last)            [OK / MANGEL / N/A]
□ Scheibe dreht frei (unter Handlast)       [OK / MANGEL / N/A]
□ Kein Spiel in Achse/Lager                 [OK / MANGEL / N/A]
□ Ratsche greift/löst korrekt              [OK / MANGEL / N/A]
□ Kein ungewöhnliches Geräusch             [OK / MANGEL / N/A]

GESAMTBEWERTUNG: □ OK  □ Wartung nötig  □ Tauschen
Maßnahme: ________________________________________________
Priorität: □ Sofort  □ Nächste Saison  □ Bei Gelegenheit
```

### K.2 Taljen-Inspektionsprotokoll

```
AYDI TALJEN-INSPEKTIONSPROTOKOLL
=================================

Yacht: __________________ Datum: __________________
Anlage: _________________ (z.B. Großschot, Backstag)

Untersetzung: ______:1  Kaskade: □ Ja □ Nein
Anzahl Blöcke: _____  Anzahl Scheiben: _____

BLOCK-INSPEKTION (je Block):
Block 1 (oben): Modell _________ Zustand: [OK / MANGEL]
Block 2 (unten): Modell _________ Zustand: [OK / MANGEL]
Block 3 (ggf.): Modell _________ Zustand: [OK / MANGEL]

LEINENPRÜFUNG:
□ Leine korrekt geschert (nicht verdreht)   [OK / MANGEL]
□ Leinendurchmesser passt zu Scheibe        [OK / MANGEL]
□ Leinenmantel intakt (kein Abrieb)         [OK / MANGEL]
□ Leine richtige Länge                      [OK / MANGEL]

FUNKTIONSPRÜFUNG:
□ Talje läuft leichtgängig                  [OK / MANGEL]
□ Volle Untersetzung nutzbar                [OK / MANGEL]
□ Klemmer hält Last                          [OK / MANGEL]
□ Keine Verdrillung der Parten              [OK / MANGEL]

GESAMTBEWERTUNG: □ OK  □ Wartung  □ Upgrade empfohlen  □ Erneuerung
```

---

## ANHANG L — Visuelle Analyse-Referenz

### L.1 Erkennungsmerkmale für die AYDI-Bildanalyse

Die folgende Tabelle definiert, welche Block-Eigenschaften und -Zustände durch die Claude Vision API (Pipeline B) erkannt werden können:

| Merkmal | Erkennbarkeit | Confidence | Mindest-Bildqualität |
|---------|-------------|-----------|---------------------|
| Blocktyp (Single/Double/etc.) | Hoch | visual_high | Gesamtansicht, >500px |
| Hersteller (Logo) | Mittel | visual_medium | Nahaufnahme, >800px |
| Modellnummer | Niedrig | visual_low | Makro, >1200px |
| Scheibenmaterial | Mittel | visual_medium | Farbidentifikation |
| Wangenmaterial | Hoch | visual_high | Textur/Glanz erkennbar |
| Wangenrisse | Hoch | visual_high | Nahaufnahme, gutes Licht |
| Korrosion | Hoch | visual_high | Farbveränderung erkennbar |
| UV-Degradation | Mittel | visual_medium | Vergilbung/Versprödung |
| Scheiben-Flat-Spot | Niedrig | visual_low | Seitenansicht, Makro |
| Lager-Zustand | Nicht möglich | visual_insufficient | Nur bei offenem Block |
| Ratsche-Zustand | Nicht möglich | visual_insufficient | Nur bei Demontage |
| Schäkel-Verschleiß | Mittel | visual_medium | Nahaufnahme |
| Splint vorhanden | Hoch | visual_high | Nahaufnahme |
| Korrekte Einscherung | Hoch | visual_high | Gesamtansicht der Talje |
| Leinenverschleiß | Hoch | visual_high | Nahaufnahme der Leine |

### L.2 Prompt-Hinweise für Claude Vision (Pipeline B)

```
Analyse-Prompt für Block-Inspektion:

"Analysiere dieses Foto eines Segelblocks. Bestimme:
1. Blocktyp (Einfach, Doppel, Violin, Ratsche, Snatch, etc.)
2. Geschätzter Hersteller und Serie (wenn Logo erkennbar)
3. Wangenmaterial (Edelstahl, Aluminium, Composite, CFK)
4. Sichtbare Schäden oder Verschleiß:
   - Risse in Wangen
   - Korrosion
   - UV-Schäden (Vergilbung, Versprödung)
   - Schäkel-Verschleiß
   - Fehlende Splinte
5. Geschätzter Zustand: gut / befriedigend / mangelhaft / kritisch
6. Wenn 'nicht beurteilbar': angeben warum (Bildqualität, Blickwinkel)

Antworte auf Deutsch. Verwende AYDI-Confidence-Level."
```

---

## ANHANG M — Schmierstoff-Kompatibilität

### M.1 Kompatibilitätsmatrix

| Schmierstoff | Delrin | Torlon | Aluminium | Edelstahl | CFK | Keramik |
|-------------|--------|--------|-----------|-----------|-----|---------|
| PTFE-Fett | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Silikonfett | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Lanolin/Lanocote | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| WD-40 (kurzzeitig) | ✓ | ✓ | ✓ | ✓ | ⚠ | ✓ |
| Graphitfett | ✓ | ✓ | ⚠* | ✓ | ✓ | ✓ |
| Mineralöl | ⚠ | ✓ | ✓ | ✓ | ⚠ | ✓ |
| McLube Sailkote | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Harken OneDrop | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

✓ = Kompatibel, ⚠ = Eingeschränkt, ⚠* = Kann Eloxierung angreifen

### M.2 Schmierstoff-Empfehlung nach Anwendung

| Anwendung | Empfohlener Schmierstoff | Intervall |
|-----------|------------------------|-----------|
| Kugellager allgemein | PTFE-Fett (Teflon) | 6 Monate |
| Ratschen-Mechanismus | Harken OneDrop (spezifisch!) | 3 Monate |
| Schäkelbolzen | Tef-Gel oder Lanolin | Bei jeder Demontage |
| Scheiben-Oberfläche | McLube Sailkote | Monatlich |
| Traveler-Wagen | PTFE-Fett + McLube | 3 Monate |

---

## ANHANG N — Retrofit-Leitfaden

### N.1 Typische Retrofit-Szenarien

#### Szenario 1: Gleitlager → Kugellager Upgrade

**Aufwand:** Gering (Blocktausch)
**Kosten:** 30–100% Aufpreis pro Block
**Wirkung:** 15–25% geringere Reibung pro Block, deutlich spürbar in Taljen

**Vorgehen:**
1. Alle Blöcke identifizieren (Typ, Größe, Position)
2. Blöcke mit höchster Belastung und häufigstem Gebrauch priorisieren
3. Gleiche Größe, bessere Serie wählen (z. B. Harken Element → Harken Midrange)
4. Tausch: Schäkel lösen → alten Block entfernen → neuen Block einsetzen

#### Szenario 2: Großschot-System Upgrade

**Aufwand:** Mittel (Blocktausch + ggf. Traveler)
**Kosten:** 300–1.500 EUR je nach Umfang
**Wirkung:** Deutlich leichteres Segeln, besserer Trimm

#### Szenario 3: Fallen ins Cockpit verlegen

**Aufwand:** Hoch (neue Blöcke, Clutches, Umlenkungen)
**Kosten:** 800–3.000 EUR
**Wirkung:** Bequemere Bedienung, Einhandfähigkeit

### N.2 Retrofit-Checkliste

```
RETROFIT-CHECKLISTE BLÖCKE
===========================

Phase 1: Bestandsaufnahme
□ Alle bestehenden Blöcke katalogisieren
□ Zustand bewerten (Inspektionsprotokoll)
□ Lasten berechnen/abschätzen
□ Schwachstellen identifizieren

Phase 2: Planung
□ Ziel definieren (Komfort, Performance, Sicherheit)
□ Budget festlegen
□ Blöcke auswählen (Dimensionierung, Hersteller)
□ Befestigungspunkte prüfen (Verstärkung nötig?)
□ Leinenführung planen

Phase 3: Beschaffung
□ Blöcke bestellen (Lieferzeit beachten)
□ Schäkel, Splinte, Schrauben bestellen
□ Werkzeug bereitlegen
□ Ggf. neue Leinen bestellen

Phase 4: Installation
□ Alte Blöcke demontieren
□ Befestigungspunkte reinigen/prüfen
□ Neue Blöcke montieren
□ Leinen scheren
□ Funktionsprüfung unter Last

Phase 5: Dokumentation
□ Modellnummern notieren
□ Installationsdatum dokumentieren
□ Fotos anfertigen (AYDI Level 2)
□ Nächsten Wartungstermin planen
```

---

## ANHANG O — Regatta-Spezifikationen

### O.1 Klassenvorschriften (Beispiele)

| Klasse | Block-Einschränkungen | Max. Blöcke | Material-Beschränkung |
|--------|----------------------|-------------|----------------------|
| Laser/ILCA | Harken Carbo vorgeschrieben | Fest definiert | Nur zugelassene Blöcke |
| 420er | Keine Marken-Vorschrift | Fest definiert | Keine Exoten |
| J/24 | Keine Exoten, kein CFK | Klassenregeln | Kein CFK |
| Melges 24 | Frei | Frei | Frei |
| IRC | Frei (nicht im Rating) | Frei | Frei |
| ORC | Frei (Gewicht relevant) | Frei | Frei |

### O.2 Gewichtsoptimierung für Regatta

| Maßnahme | Gewichtseinsparung | Kosten | Aufwand |
|----------|-------------------|--------|---------|
| Edelstahl → Aluminium (alle) | 30–40% | Mittel | Gering |
| Aluminium → CFK (kritische) | 20–30% | Hoch | Gering |
| Blöcke → LFR (niedrige Last) | 60–80% | Gering | Gering |
| Reduzierung Blockanzahl | 5–15% | Null | Mittel |
| Downsizing (Überprüfung) | 10–20% | Null | Gering |

### O.3 Quick-Change-Systeme für Regatta

Für Regatten mit unterschiedlichen Kursen (Bahn/Langstrecke) werden Block-Konfigurationen schnell gewechselt:

- **Snatchblöcke:** Schnelles Umsetzen von Schot-Umlenkungen
- **Dyneema-Loops:** Blöcke können in Sekunden ein-/ausgehängt werden
- **Schraubschäkel:** Langsamer als Snap-Schäkel, aber sicherer

---

## ANHANG P — Superyacht-Sonderlösungen

### P.1 Blöcke für Superyachten (>18m)

**Besonderheiten:**

| Aspekt | Superyacht-Anforderung | Standard-Yacht |
|--------|----------------------|----------------|
| Bruchlast | 10.000–50.000+ daN | 500–5.000 daN |
| Material | Edelstahl 316L, Titan | Composite, Edelstahl |
| Oberfläche | Hochglanzpoliert, deckweiß | Standard-Finish |
| Geräusch | Minimal (Eigner-Komfort) | Akzeptabel |
| Sichtbarkeit | Oft verdeckt/versenkt | Sichtbar auf Deck |
| Bedienung | Elektrisch/hydraulisch | Manuell/Winsch |

**Hersteller für Superyacht-Blöcke:**
- **Harken Custom:** Maßanfertigung in jeder Größe
- **Lewmar Ocean/Custom:** Standardisierte Großblöcke
- **Antal Mega-Serie:** Blöcke bis 200mm Scheibendurchmesser
- **Frederiksen:** Dänischer Spezialist für Superyacht-Beschläge
- **Spinlock:** Hochlast-Clutches und -Blöcke

### P.2 Verdeckte Blocksysteme (Concealed Blocks)

Auf Superyachten werden Blöcke oft unter Deck oder in Verkleidungen montiert:

- **Unter-Deck-Fallen:** Fallen laufen durch Deck-Durchführungen zu unter-Deck-Blöcken
- **In-Mast-Systeme:** Blöcke im Mastprofil integriert
- **In-Baum-Systeme:** Ausholer und Reff innenliegend

**Vorteil:** Aufgeräumtes Deck, keine Stolperfallen, Schutz vor UV und Wetter.
**Nachteil:** Schwierigere Wartung, höhere Installationskosten, Zugang bei Versagen.

### P.3 Captive-Winsch-Systeme

Auf Superyachten ersetzen Captive-Winschen (versenkte, elektrische/hydraulische Winschen) in Kombination mit verdeckten Blöcken konventionelle Deck-Layouts. Die Blöcke müssen für folgende Anforderungen ausgelegt sein:

- Dauerbetrieb unter hoher Last (elektrische Winschen erzeugen konstante Kraft)
- Abgedichtete Lager (verdeckte Position, schwierige Wartung)
- Überlast-Sicherung (Winsch kann höhere Kräfte als Handkurbel erzeugen)

---

## ANHANG Q — Umrechnungstabellen

### Q.1 Kraft-Einheiten

| Von | Nach | Faktor |
|-----|------|--------|
| daN | N | × 10 |
| daN | kgf | × 1,02 |
| daN | lbf | × 2,248 |
| kN | daN | × 100 |
| kgf | daN | × 0,981 |
| lbf | daN | × 0,445 |
| Tonnen (metr.) | daN | × 981 |
| Tons (short) | daN | × 890 |

### Q.2 Längen-Einheiten

| Von | Nach | Faktor |
|-----|------|--------|
| mm | Zoll (inch) | × 0,03937 |
| Zoll | mm | × 25,4 |
| m | Fuß (ft) | × 3,281 |
| Fuß | m | × 0,3048 |

### Q.3 Scheibendurchmesser — Harken vs. Lewmar Nomenklatur

| Harken-Bezeichnung | Scheibendurchmesser (mm) | Lewmar-Äquivalent |
|-------------------|--------------------------|-------------------|
| Micro (16mm) | 16 | — |
| Mini (22mm) | 22 | Size 1 (20mm) |
| 29mm | 29 | Size 2 (30mm) |
| 40mm | 40 | Size 3 (40mm) |
| 57mm | 57 | Size 5 (50mm) |
| 75mm | 75 | Size 7 (60mm/72mm) |
| 100mm | 100 | Size 9 (80mm) |

---

## ANHANG R — Checklisten

### R.1 Saisonstart-Checkliste Blöcke

```
SAISONSTART — BLOCK-INSPEKTION
================================

□ Alle Persennings und Abdeckungen entfernen
□ Sichtkontrolle aller Blöcke an Deck
□ Sichtkontrolle aller Blöcke am Mast (von Deck aus mit Fernglas)
□ Jede Scheibe von Hand drehen — dreht sie frei?
□ Alle Schäkelbolzen auf Festsitz prüfen
□ Alle Splinte vorhanden und intakt?
□ Leinen durch alle Blöcke laufen lassen — kein Klemmen?
□ Taljen auf korrekte Einscherung prüfen
□ Klemmer (Cam Cleats) auf Funktion prüfen
□ Ratschen-Blöcke auf Funktion prüfen
□ Alle Blöcke mit PTFE-Fett schmieren
□ McLube auf Scheiben-Oberflächen
□ Traveler-Wagen auf Leichtgängigkeit prüfen
□ Masttop-Blöcke inspizieren (beim Maststellen oder per Bosunsstuhl)
□ Befestigungspunkte auf Deck prüfen (Schrauben fest, keine Risse)
□ Defekte oder verdächtige Blöcke markieren → Tausch planen
□ Inspektionsergebnis dokumentieren (AYDI Level 2)
```

### R.2 Saisonende-Checkliste Blöcke

```
SAISONENDE — BLOCK-KONSERVIERUNG
==================================

□ Alle Blöcke mit Süßwasser gründlich spülen
□ Leinen aus Blöcken entfernen (wo möglich)
□ Blöcke trocknen lassen
□ PTFE-Fett auf alle Lager
□ Schäkelbolzen lösen, reinigen, mit Tef-Gel einsetzen
□ Persennings/Abdeckungen über Deck-Hardware
□ Bei Winterlager an Land: Mast-Blöcke separat lagern
□ Defekte Blöcke für Winterarbeit beiseitelegen
□ Ersatzteile/Ersatzblöcke bestellen (für nächste Saison)
```

### R.3 Blauwasser-Vorbereitung Checkliste

```
BLAUWASSER-VORBEREITUNG — BLÖCKE
==================================

□ Alle Blöcke auf Mindestalter prüfen (<10 Jahre für Kunststoff)
□ Alle Kugellager auf Korrosion prüfen (Salzwasser-Revier geplant)
□ Mindestens 4 Ersatzblöcke beschaffen (2× groß, 2× klein)
□ Rebuild-Kit für häufigsten Blocktyp mitnehmen
□ 2× Snatchblock universal mitnehmen
□ Ersatz-Schäkel (6–10 Stück, verschiedene Größen)
□ Splinte (20+ Stück)
□ PTFE-Fett (2 Tuben)
□ McLube Sailkote (2 Dosen)
□ Tef-Gel (1 Tube)
□ Harken OneDrop (1 Flasche, wenn Ratschen an Bord)
□ Sprengring-Zange klein
□ Kontaktkorrosion prüfen (Alu-Blöcke auf Edelstahl-Beschlägen)
□ Alle Blöcke fotografieren und katalogisieren
□ Hersteller-Kontaktdaten für Reparatur/Ersatzteile weltweit notieren
□ AYDI Level-2-Analyse durchführen und Bericht speichern
```

### R.4 Notfall-Checkliste Block-Versagen auf See

```
NOTFALL — BLOCK VERSAGT AUF SEE
==================================

SOFORT:
□ Last von der betroffenen Anlage nehmen (Segel bergen/fieren)
□ Betroffene Leine sichern (Klampe, Winsch, Knoten)
□ Crew warnen (Peitschengefahr durch lose Leinen)

ASSESSMENT:
□ Welcher Block ist betroffen?
□ Welche Funktion hat er? (Sicherheitskritisch?)
□ Ist eine temporäre Reparatur möglich?
□ Gibt es einen Ersatzblock an Bord?

TEMPORÄRE LÖSUNG:
□ Ersatzblock einsetzen
□ Snatchblock als Ersatz verwenden
□ Textil-Loop als Umlenkung (Dyneema-Schlaufe um Beschlag)
□ Leine direkt über Winsch führen (ohne Umlenkblock)
□ Segelfläche reduzieren (Reffen), um Last zu senken

DOKUMENTATION:
□ Fotos vom Schaden (für AYDI-Analyse)
□ Ursache notieren (sofern erkennbar)
□ Maßnahme dokumentieren
□ Permanente Reparatur im nächsten Hafen planen
```

---

*Ende der Wissensdatei 10.01 — Blöcke Grundlagen und Typen*

*AYDI Research, Version 1.0.0, 2026-04-25*
*Status: validated*
*Confidence: measured (Hersteller-TDS), documented (Kataloge, Fachliteratur), estimated (Erfahrungswerte)*
