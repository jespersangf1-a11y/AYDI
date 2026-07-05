---
title: "Schäkel Grundlagen und Typen im Yachtbau"
kategorie: "12 Schäkel, Wirbel und Verbinder"
unterkategorie: "01 Grundlagen"
version: "1.0.0"
datum: "2026-04-25"
autor: "AYDI Research"
status: "validated"
confidence_quellen:
  - measured: "Hersteller-Datenblätter, Laborprüfungen, CE-Zertifikate"
  - documented: "Hersteller-Kataloge, Segelfachpresse, Forum-Konsens"
  - estimated: "Erfahrungswerte, Quervergleiche"
  - benchmark: "Marktdurchschnitte, Branchenstandards"
tags:
  - schäkel
  - shackles
  - d_schäkel
  - bügelschäkel
  - wirbelschäkel
  - fallenschäkel
  - snap_schäkel
  - soft_schäkel
  - verbinder
  - rigg
  - beschläge
  - laufendes_gut
  - stehendes_gut
  - deck_hardware
  - anker
boot_klassen:
  - jolle (4–8m)
  - fahrtensegler (8–14m)
  - performance_cruiser (10–16m)
  - blauwasseryacht (12–18m)
  - regattayacht (8–20m)
  - motoryacht (8–25m)
  - superyacht (18m+)
---

# 12.01 — Schäkel Grundlagen und Typen im Yachtbau: Vollständige Wissensreferenz

> **AYDI Wissensdatei 12.01** — Kategorie 12: Schäkel, Wirbel und Verbinder
> **Confidence-Quelle:** measured (Hersteller-TDS, CE-Prüfzeugnisse), documented (Hersteller-Kataloge, Fachliteratur), estimated (Erfahrungswerte)
> **Letzte Aktualisierung:** 2026-04-25

---

## Inhaltsverzeichnis

1. [Einführung und Übersicht](#1-einführung-und-übersicht)
2. [Grundlagen und Theorie](#2-grundlagen-und-theorie)
3. [Typenübersicht](#3-typenübersicht)
4. [Materialien und Konstruktion](#4-materialien-und-konstruktion)
5. [Produktlinien und Hersteller](#5-produktlinien-und-hersteller)
6. [Dimensionierung und Auswahl](#6-dimensionierung-und-auswahl)
7. [Montage und Installation](#7-montage-und-installation)
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
22. [ANHANG J — Schäkelauswahl-Algorithmus](#anhang-j--schäkelauswahl-algorithmus)
23. [ANHANG K — Prüfprotokolle](#anhang-k--prüfprotokolle)
24. [ANHANG L — Visuelle Analyse-Referenz](#anhang-l--visuelle-analyse-referenz)
25. [ANHANG M — Korrosionsschutz und Pflege](#anhang-m--korrosionsschutz-und-pflege)
26. [ANHANG N — Retrofit-Leitfaden](#anhang-n--retrofit-leitfaden)
27. [ANHANG O — Regatta-Spezifikationen](#anhang-o--regatta-spezifikationen)
28. [ANHANG P — Superyacht-Sonderlösungen](#anhang-p--superyacht-sonderlösungen)
29. [ANHANG Q — Umrechnungstabellen](#anhang-q--umrechnungstabellen)
30. [ANHANG R — Checklisten](#anhang-r--checklisten)

---

## 1. Einführung und Übersicht

### 1.1 Was sind Schäkel?

Schäkel (englisch: shackles) sind U- oder Ω-förmige Metallverbinder mit einem verschließbaren Bolzen, die als lösbare Verbindungselemente im gesamten Rigg- und Deckssystem von Yachten eingesetzt werden. Sie bilden die kritischen Verbindungspunkte zwischen Tauwerk, Ketten, Drähten, Blöcken, Winschen, Beschlägen und Strukturelementen.

Ein Schäkel besteht in seiner Grundform aus zwei Komponenten:

- **Bügel (Body/Bow)**: Der U- oder Ω-förmige Hauptkörper, der die Last aufnimmt
- **Bolzen (Pin)**: Der verschließbare Stift, der den Bügel schließt und die Verbindung sichert

Die Geometrie des Bügels, die Art des Bolzens und das Material definieren den Schäkeltyp und seinen Einsatzbereich.

### 1.2 Bedeutung im Yacht-System

Schäkel sind die universellen „Gelenke" eines Yachtsystems. Auf einer modernen 12-Meter-Fahrtenyacht befinden sich typischerweise 40–80 Schäkel in verschiedenen Größen und Typen. Auf einer Regattayacht gleicher Größe können es 80–150+ sein, wenn man Spinnaker-Equipment, Trimmeinrichtungen und Reserven mitzählt.

Jeder einzelne Schäkel ist ein potenzieller Single Point of Failure. Das Versagen eines einzigen Schäkels kann katastrophale Folgen haben — vom Verlust eines Segels über Riggversagen bis hin zu Personenschäden durch peitschende Drähte oder herabfallende Teile.

Die Gesamtkosten für Schäkel einer Yacht liegen typischerweise bei:

| Bootsklasse | Schäkelanzahl | Kostenbereich (EUR) |
|-------------|---------------|---------------------|
| Jolle (4–8m) | 10–25 | 50–300 |
| Fahrtensegler (8–14m) | 40–80 | 300–1.500 |
| Performance Cruiser (10–16m) | 60–120 | 800–3.500 |
| Blauwasseryacht (12–18m) | 50–100 | 600–2.500 |
| Regattayacht (8–20m) | 80–150+ | 1.500–8.000 |
| Motoryacht (8–25m) | 20–50 | 200–1.200 |
| Superyacht (18m+) | 80–200+ | 3.000–25.000+ |

### 1.3 Historische Entwicklung

Die Geschichte des Schäkels in der Seefahrt reicht Jahrhunderte zurück:

**Frühzeit (vor 1800):**
Erste Schäkelformen aus geschmiedetem Eisen dienten der Verbindung von Ankerketten und stehendem Gut auf Segelschiffen. Die Bolzen wurden durch Splinte gesichert. Die Qualität war stark von der Schmiedekunst des jeweiligen Handwerkers abhängig — standardisierte Traglasten existierten nicht.

**Industriezeitalter (1800–1950):**
Mit der Industrialisierung kamen genormte Schäkelgrößen auf. Gusseisen und später Stahl ersetzten Schmiedeeisen. Die Einführung von Gewindebolzen (screw pin) vereinfachte die Handhabung. Die Lloyds-Klassifikation begann, Mindest-Bruchlasten für Ankerketten-Schäkel zu normieren.

**Nachkriegsära (1950–1980):**
Edelstahl (zunächst AISI 304, dann 316) setzte sich für Yachtschäkel durch. Erste geschmiedete Edelstahlschäkel von europäischen Herstellern (Wichard, Pfeiffer). Aluminium-Schäkel für den Regattasport.

**Moderne Ära (1980–heute):**
- 1980er: Wichard führt geschmiedete Edelstahlschäkel mit Self-Locking-Bolzen ein
- 1990er: Harken entwickelt das Titelok-System (werkzeugloses Öffnen unter Last)
- 2000er: Hochfeste Dyneema-Soft-Schäkel kommen aus dem America's-Cup-Umfeld
- 2010er: Titanschäkel für Extremanwendungen; Allen-Key-Bolzen als Standard für Rigg-Schäkel
- 2020er: CNC-gefräste Schäkel aus hochfestem Aluminium; hybride Soft-/Metallschäkel

### 1.4 Abgrenzung zu verwandten Verbindern

| Verbinder | Unterschied zum Schäkel |
|-----------|------------------------|
| Wirbelschäkel (Swivel) | Enthält Drehlager, erlaubt Rotation um Längsachse |
| Karabiner (Snap Hook) | Federbelasteter Verschluss, kein Bolzen |
| Gabelkopf (Toggle/Clevis) | Längliche Form, speziell für stehendes Gut |
| Kettenschloss (Chain Link) | Permanente Verbindung, nicht lösbar |
| Bolzen mit Splint (Clevis Pin) | Kein Bügel, nur ein Stift durch zwei Gabeln |
| Schnappschäkel (Snap Shackle) | Federbelasteter Kolbenbolzen, schnelles Lösen unter Last |

### 1.5 Einsatzbereiche auf der Yacht

**Stehendes Gut (Standing Rigging):**
- Wantabschlüsse oben (Mastkopf) und unten (Pütting)
- Vorstag-Anschluss am Bug und am Mastkopf
- Backstag-Verbindungen
- Babystag und Checkstag

**Laufendes Gut (Running Rigging):**
- Fallen am Segelkopf (Halyard Shackle)
- Schoten an Segelschothörnern
- Spinnaker-Fallen und -Schoten
- Reffleinen-Anschlüsse
- Block-Befestigungen

**Ankergeschirr:**
- Verbindung Ankerkette–Anker
- Verbindung Ankerkette–Vorleine
- Ankerwirbel (Swivel)
- Kettenstopper-Befestigung

**Sicherheitsausrüstung:**
- Rettungsinsel-Befestigung
- MOB-Ausrüstung (Mann-über-Bord)
- Lifeline-Befestigungen
- Sicherungspunkte für Lifebelts

---

## 2. Grundlagen und Theorie

### 2.1 Lastkennwerte: WLL vs. MBL vs. Proof Load

Die drei fundamentalen Lastkennwerte eines Schäkels sind:

**WLL — Working Load Limit (Arbeitslastgrenze):**
Die maximale Last, die im normalen Betrieb dauerhaft auf den Schäkel wirken darf. Die WLL berücksichtigt Ermüdung, dynamische Lasten und einen Sicherheitsfaktor gegenüber dem Bruch. Im Yachtbereich wird die WLL in daN (Dekanewton) oder kN angegeben.

**MBL — Minimum Breaking Load (Mindest-Bruchlast):**
Die Last, bei der der Schäkel unter statischer Belastung mit Sicherheit versagt. Die MBL wird durch zerstörende Prüfung einer statistisch relevanten Stichprobe ermittelt. Die tatsächliche Bruchlast einzelner Schäkel kann höher liegen.

**Proof Load (Prüflast):**
Die Last, mit der jeder einzelne Schäkel (oder eine Stichprobe) werksseitig geprüft wird, ohne dass eine bleibende Verformung auftritt. Die Proof Load liegt typischerweise bei 40–60 % der MBL.

**Zusammenhang:**

```
MBL = WLL × Sicherheitsfaktor
Proof Load ≈ 0,4–0,6 × MBL
```

### 2.2 Sicherheitsfaktoren

Der Sicherheitsfaktor (Safety Factor, SF) definiert das Verhältnis von MBL zu WLL. Er kompensiert:

- Dynamische Lasten (Böen, Wellen, Rucke)
- Materialermüdung über die Lebensdauer
- Korrosion und Materialdegradation
- Fertigungstoleranzen
- Unvorhergesehene Belastungen

**Standard-Sicherheitsfaktoren im Yachtbau:**

| Anwendung | Sicherheitsfaktor | Begründung |
|-----------|-------------------|------------|
| Stehendes Gut allgemein | 4:1 | Statisch belastet, regelmäßig inspizierbar |
| Laufendes Gut allgemein | 5:1 | Dynamische Lasten, Reibung, Ermüdung |
| Ankerkette und -schäkel | 4:1 | Hohe dynamische Lasten, aber seltene Maximalbelastung |
| Lifelines und Sicherung | 5:1 bis 6:1 | Personenschutz, höchste Anforderungen |
| Hebezeug (Davits, Kran) | 6:1 | Gesetzliche Anforderung (EN 13889) |
| Regatta (gewichtsoptimiert) | 3:1 bis 4:1 | Kontrollierte Bedingungen, häufige Inspektion |
| Superyacht (Lloyd's/RINA) | 5:1 bis 6:1 | Klassifikationsgesellschaft-Vorgaben |

**Berechnungsbeispiel:**

```
Gesucht: Schäkel für Großfall einer 12m-Yacht
Maximale Falllast (gemessen/berechnet): 800 daN
Sicherheitsfaktor laufendes Gut: 5:1
Erforderliche MBL: 800 × 5 = 4.000 daN (40 kN)
Erforderliche WLL: 800 daN (= max. Betriebslast)
→ Schäkel mit MBL ≥ 4.000 daN auswählen
```

### 2.3 Statische vs. dynamische Belastung

**Statische Last:**
Konstante, gleichmäßige Belastung. Beispiel: Want unter Grundspannung ohne Seegang. Der Schäkel wird mit einem definierten, gleichbleibenden Zug belastet.

**Dynamische Last:**
Wechselnde, stoßartige oder schwingende Belastung. Beispiel: Großschot bei Böen, Ankerschäkel bei Seegang. Dynamische Lasten können kurzfristig das 2–4-fache der statischen Last erreichen.

**Wechsellast (Fatigue Load):**
Wiederholte Be- und Entlastung. Beispiel: Genua-Fallenschäkel beim Reffen und Setzen. Wechsellasten führen zu Materialermüdung — der Schäkel kann bei einer Last deutlich unter der MBL versagen.

**Dynamische Lastfaktoren im Yachtbau:**

| Situation | Dynamischer Faktor |
|-----------|--------------------|
| Ruhig vor Anker | 1,0–1,5 |
| Leichte See, normaler Segelbetrieb | 1,5–2,0 |
| Raue See, Reffbedingungen | 2,0–3,0 |
| Sturmbed., Ankern bei Starkwind | 3,0–4,0 |
| Ruckartig (Segel schlägt, Leine rutscht) | 3,0–5,0 |
| Rigg-Pumpen (Mast schwingt) | 2,0–3,5 |

### 2.4 Bolzentypen und Verschlussmechanismen

Der Bolzen ist das kritische Element jedes Schäkels — er bestimmt Sicherheit, Handhabung und Einsatzbereich:

**2.4.1 Schraubbolzen (Screw Pin)**

Der häufigste Bolzentyp. Ein Gewindestift wird von Hand in den Bügel geschraubt.

- **Vorteile:** Einfach, günstig, universell, werkzeuglos bedienbar
- **Nachteile:** Kann sich durch Vibration lösen, erfordert Sicherung (Draht, Loctite, Kabelbinder)
- **Sicherung:** Seizing wire (Monel-Draht 0,8mm) durch Bolzenauge und Bügelloch
- **Typische Anwendung:** Ankerkette, stehendes Gut (gesichert), allgemeine Verbindungen
- **Anzugsdrehmoment:** Handfest + 1/4 Umdrehung. KEIN Werkzeug verwenden (Gewindeüberlastung)

**2.4.2 Sicherungsbolzen (Bolt Type / Safety Pin)**

Ein durchgehender Bolzen mit Mutter und Splint auf der gegenüberliegenden Seite.

- **Vorteile:** Kann sich nicht lösen, höchste Sicherheit, für dauerhafte Installationen
- **Nachteile:** Benötigt Werkzeug (Zange für Splint), langsamer zu öffnen
- **Sicherung:** Splint (Edelstahl oder Bronze) durch Bolzenbohrung, Enden umbiegen
- **Typische Anwendung:** Ankerkette–Anker, Wantabschlüsse permanent, Sicherheitsrelevante Punkte
- **Praxis-Tipp:** Splinte immer 1x verwenden und dann ersetzen — ein gebogener und wieder gerichteter Splint ist vorgeschädigt

**2.4.3 Captive Pin (Unverlierbar)**

Der Bolzen ist über einen Splintring, eine Feder oder einen Sicherungsring im Bügel gehalten und kann nicht vollständig entfernt werden.

- **Vorteile:** Bolzen kann nicht verloren gehen, schneller als Bolt Type
- **Nachteile:** Teurer, begrenzte Größenvarianten, Feder kann korrodieren
- **Typische Anwendung:** Fallen-Schäkel, Spi-Schäkel, alle Positionen mit häufigem Öffnen
- **Hersteller-Beispiele:** Wichard Captive Pin, HR (Harken Rigger) Schäkel

**2.4.4 Allen-Key-Bolzen (Inbus-Bolzen)**

Ein Bolzen mit Innensechskant-Aufnahme, der nur mit einem Inbusschlüssel geöffnet werden kann.

- **Vorteile:** Sehr sicher gegen unbeabsichtigtes Öffnen, glatte Oberfläche (kein Schlitz/Kreuz)
- **Nachteile:** Benötigt Werkzeug, bei Korrosion schwer zu lösen
- **Sicherung:** Inhärent sicher durch Werkzeugbedarf; optional Loctite 243 (mittelfest)
- **Typische Anwendung:** Rigg-Schäkel (Wantterminals, Vorstag), semi-permanente Verbindungen
- **Schlüsselgrößen:** 3mm (bis 6mm Bolzen), 4mm (8mm Bolzen), 5mm (10mm Bolzen), 6mm (12mm+ Bolzen)

**2.4.5 Self-Locking (Selbstsichernd)**

Patentierte Mechanismen, bei denen der Bolzen durch eine Feder, einen Nocken oder eine Kurvenbahn automatisch gesichert wird.

- **Vorteile:** Werkzeuglos, schnell, vibrationssicher, kann sich nicht selbst lösen
- **Nachteile:** Teuer, herstellerspezifisch, Mechanismus muss gewartet werden
- **Typische Anwendung:** Fallen, Spi, alle Positionen mit häufigem Öffnen unter Deck-Bedingungen
- **Hersteller-Beispiele:** Wichard Self-Locking (rote Markierung), Blue Wave Quick-Release

**2.4.6 Snap-Mechanismus (Schnappschäkel)**

Federbelasteter Kolbenbolzen, der durch Zurückziehen gegen die Feder geöffnet wird. Kann unter Last geöffnet werden (Trip-Line-Systeme).

- **Vorteile:** Schnellstes Öffnen und Schließen, auch unter Last lösbar (bei Tripping-Varianten)
- **Nachteile:** Kann sich bei falscher Belastungsrichtung selbst öffnen, Feder ermüdet
- **Typische Anwendung:** Spinnaker-Fall (Tripping), Spi-Schot, Groß-Schot an Baum
- **WARNUNG:** Snap-Schäkel NIEMALS für stehendes Gut oder Sicherheitsanwendungen verwenden

### 2.5 Belastungsrichtung und deren Einfluss

Die Tragfähigkeit eines Schäkels hängt entscheidend von der Belastungsrichtung ab:

**2.5.1 Axiale Belastung (In-Line)**

Zug in Längsrichtung des Schäkels — die vorgesehene Hauptbelastung. Die WLL/MBL-Angaben beziehen sich immer auf diese Richtung.

```
    ↑ Zug
    |
   ┌─┐  ← Bolzen
   │ │
   └─┘
    |
    ↓ Zug
```

Effizienz: 100 % der Nenn-WLL

**2.5.2 Querbelastung (Side Load)**

Zug quer zur Schäkelebene. Reduziert die Tragfähigkeit erheblich.

```
  ← Zug ─ ┌─┐ ─ Zug →
           │ │
           └─┘
```

Effizienz: 50–70 % der Nenn-WLL (je nach Typ)

**Warum Querbelastung gefährlich ist:**
- Der Bolzen wird auf Biegung belastet statt auf Scherung
- Der Bügel wird aufgebogen (besonders bei D-Schäkeln)
- Ungleichmäßige Lastverteilung auf die Schenkel

**2.5.3 Mehrfachbelastung (Multi-Directional)**

Bügelschäkel (Bow Shackles/Omega-Schäkel) sind für Lasten aus mehreren Richtungen ausgelegt. D-Schäkel hingegen verlieren bei Mehrfachbelastung deutlich an Tragfähigkeit.

| Belastungsrichtung | D-Schäkel (% WLL) | Bügelschäkel (% WLL) |
|--------------------|--------------------|--------------------|
| Axial (0°) | 100 % | 100 % |
| 15° seitlich | 90 % | 95 % |
| 30° seitlich | 75 % | 90 % |
| 45° seitlich | 60 % | 80 % |
| 90° quer | 50 % | 70 % |
| Dreipunkt (120°) | n/a | 65 % |

### 2.6 Ermüdung und Lebensdauer

**Ermüdungsversagen (Fatigue Failure):**
Schäkel können nach vielen tausend Lastzyklen bei einer Last deutlich unter der MBL versagen. Dies ist besonders relevant für:

- Fallen-Schäkel (tägliches Setzen/Bergen)
- Reff-Schäkel (häufiges Reffen bei Fahrtenboot)
- Ankerschäkel (Schwojzyklus bei Wind/Strom)

**Lebensdauer-Richtwerte:**

| Anwendung | Zyklen/Saison | Empfohlener Tausch |
|-----------|---------------|-------------------|
| Stehendes Gut (permanent) | 1–2 | Alle 10 Jahre oder bei Inspektion |
| Fallen | 200–500 | Alle 5–7 Jahre |
| Spinnaker-Schäkel | 50–200 | Alle 3–5 Jahre |
| Ankerschäkel | 50–300 | Alle 5–8 Jahre |
| Reff-Schäkel | 100–400 | Alle 5 Jahre |
| Regatta (hohe Last) | 500–2.000 | Jährlich inspizieren, alle 2–3 Jahre tauschen |

**Frühzeichen der Ermüdung:**
1. Feine Haarrisse (nur mit Lupe oder Rissprüfung sichtbar)
2. Verfärbung an Spannungskonzentrationspunkten
3. Leichte Verformung des Bügels (Symmetrie prüfen)
4. Rauhe Stellen am Bolzen (Oberflächen-Pitting)
5. Gewindegang fühlt sich „sandig" an

### 2.7 Korrosion und Materialverträglichkeit

**Galvanische Korrosion:**
Wenn zwei unterschiedliche Metalle in Salzwasser-Kontakt stehen, korrodiert das unedlere Metall beschleunigt. Relevante Paarungen:

| Paarung | Risiko | Maßnahme |
|---------|--------|----------|
| Edelstahl 316 + Edelstahl 316 | Kein Risiko | — |
| Edelstahl 316 + Aluminium | HOCH | Vermeiden oder isolieren (Tef-Gel) |
| Edelstahl 316 + Bronze | Gering | Akzeptabel, Bronze opfert minimal |
| Edelstahl 316 + verzinkter Stahl | HOCH | Vermeiden, Zink opfert schnell |
| Edelstahl 316 + Titan | Gering | Akzeptabel |
| Aluminium + Bronze | HOCH | Vermeiden |
| Dyneema + jedes Metall | Kein Risiko | Keine galvanische Reaktion |

**Spaltkorrosion (Crevice Corrosion):**
Besonders gefährlich bei Schäkeln: In engen Spalten (Bolzen–Bügel-Kontakt, Gewinde) sinkt der Sauerstoffgehalt, was bei Edelstahl zu lokalem Versagen der Passivschicht führt. Betrifft vor allem:

- Schraubbolzen im Gewinde
- Bolzen-Bügel-Kontaktflächen
- Unter Ablagerungen (Salzkristalle, Schmutz)

**Prävention:** Regelmäßiges Süßwasserspülen, Tef-Gel auf Gewinde, Anti-Seize-Paste, jährliches Lösen und Neu-Einsetzen aller Bolzen.

---

## 3. Typenübersicht

### 3.1 D-Schäkel (Dee Shackle / Straight Shackle)

**Form:** Schmaler U-förmiger Bügel mit geradem Bolzen. Die Innenseite des Bügels hat eine D-ähnliche Form (daher der Name).

**Merkmale:**
- Kompakteste Bauform aller Schäkeltypen
- Höchste Tragfähigkeit bei axialer Belastung (bezogen auf Gewicht)
- Nicht geeignet für Mehrpunkt-Belastung oder starke Querlasten
- Bolzen muss frei drehbar bleiben (nicht durch Last verklemmt)

**Einsatz auf der Yacht:**
- Wantanschlüsse (Rigg-Schäkel mit Allen-Key-Bolzen)
- Vorstag-Anschluss
- Fallenanschlüsse am Segelkopf
- Block-Befestigung an Augbolzen (single-point)
- Überall, wo die Last in einer einzigen Achse verläuft

**Typische Größen (Bolzendurchmesser / WLL):**

| Bolzen-Ø (mm) | WLL (daN) | MBL (daN) | Typische Anwendung |
|----------------|-----------|-----------|-------------------|
| 4 | 160 | 800 | Jolle, leichtes Zubehör |
| 5 | 250 | 1.250 | Jolle, kleine Fahrtenyacht |
| 6 | 400 | 2.000 | Fallen 8–10m Yacht |
| 8 | 750 | 3.750 | Fallen/Wanten 10–14m |
| 10 | 1.200 | 6.000 | Wanten 12–16m |
| 12 | 1.700 | 8.500 | Wanten/Vorstag 14–18m |
| 14 | 2.300 | 11.500 | Superyacht |
| 16 | 3.200 | 16.000 | Superyacht |

### 3.2 Bügelschäkel (Bow Shackle / Omega Shackle / Anchor Shackle)

**Form:** Bauchiger, Ω-förmiger Bügel mit geradem Bolzen. Die breitere Form erlaubt Mehrpunktbelastung und bessere Ausrichtung bei wechselnden Lastrichtungen.

**Merkmale:**
- Breiter Innenraum nimmt mehrere Leinen, Ketten oder Beschläge auf
- Besser bei seitlicher Belastung als D-Schäkel
- Etwas geringere WLL bei gleichem Bolzendurchmesser als D-Schäkel (ca. 80–85 %)
- Selbstausrichtend bei wechselnden Zugrichtungen

**Einsatz auf der Yacht:**
- Ankerkette–Anker-Verbindung (Standardschäkel)
- Mehrpunkt-Befestigungen (z.B. zwei Leinen in einem Schäkel)
- Ankerwirbel-Anschluss
- Block-Befestigung bei wechselnden Zugwinkeln
- Mooring-Leinen an Dalben

**Typische Größen:**

| Bolzen-Ø (mm) | WLL (daN) | MBL (daN) | Typische Anwendung |
|----------------|-----------|-----------|-------------------|
| 5 | 200 | 1.000 | Kleine Jollen |
| 6 | 320 | 1.600 | Anker 8–10m Yacht |
| 8 | 600 | 3.000 | Anker 10–12m Yacht |
| 10 | 1.000 | 5.000 | Anker 12–14m Yacht |
| 12 | 1.400 | 7.000 | Anker 14–18m Yacht |
| 14 | 2.000 | 10.000 | Superyacht |
| 16 | 2.700 | 13.500 | Superyacht |
| 19 | 4.000 | 20.000 | Superyacht |
| 22 | 5.500 | 27.500 | Superyacht (Anker) |

### 3.3 Wirbelschäkel (Twist Shackle / Twisted Shackle)

**Form:** D- oder Bügelschäkel, bei dem der Bügel um 90° verdreht ist, sodass Bolzenebene und Bügelöffnung senkrecht zueinander stehen.

**Merkmale:**
- Ermöglicht die Verbindung zweier Beschläge, die in unterschiedlichen Ebenen liegen
- Verhindert das Verdrillen von Tauwerk und Gewebe
- Gleiche Tragfähigkeit wie der entsprechende unverdrehte Schäkel (bei axialer Last)
- Die Verdrehung ist werksseitig eingebracht, NIEMALS einen geraden Schäkel selbst verdrehen

**Einsatz auf der Yacht:**
- Fallenschäkel am Segelkopf: Die Falle kommt vertikal, das Segelliek liegt horizontal → Twist gleicht die 90°-Drehung aus
- Blockbefestigung, wenn Block und Befestigungspunkt in verschiedenen Ebenen liegen
- Genuafall am Kopfbrett
- Spinnaker-Fall am Spi-Kopf

**WARNUNG:** Einen geraden Schäkel manuell zu verdrehen ist **streng verboten**. Die Kaltverformung schwächt das Material an der Torsionsstelle erheblich (Tragfähigkeitsverlust 40–60 %) und erzeugt eine Sollbruchstelle.

**Typische Größen:**

| Bolzen-Ø (mm) | WLL (daN) | MBL (daN) | Typische Anwendung |
|----------------|-----------|-----------|-------------------|
| 5 | 250 | 1.250 | Jolle, Fallen |
| 6 | 400 | 2.000 | Fallen 8–12m |
| 8 | 700 | 3.500 | Fallen 10–14m |
| 10 | 1.100 | 5.500 | Fallen 14–18m |

### 3.4 Fallenschäkel (Halyard Shackle)

**Form:** Spezialisierte Schäkelform mit schmalem, abgeflachtem Profil, das durch Mastschlitze (Mastnut, Luff-Groove) passt und das Blockieren des Segels beim Setzen verhindert.

**Merkmale:**
- Extrem flaches Profil (Dicke oft nur 5–8mm)
- Abgerundete Kanten, um Segeltuch und Laminat nicht zu beschädigen
- Oft mit Captive Pin oder Self-Locking-Bolzen (kein Verlieren am Masttop)
- Gewichtsoptimiert (Gewicht am Masttop = Krängungsmoment)
- Teilweise asymmetrisch geformt, um das Einfädeln in die Mastnut zu erleichtern

**Einsatz auf der Yacht:**
- Großfall am Segelkopf
- Genuafall am Kopfbrett
- Spinnaker-Fall (spezielle Spi-Fallen-Schäkel)
- Code-0/Gennaker-Fall

**Typische Größen:**

| Bolzen-Ø (mm) | WLL (daN) | MBL (daN) | Profilbreite (mm) | Typische Anwendung |
|----------------|-----------|-----------|--------------------|--------------------|
| 4 | 150 | 750 | 12 | Jolle, Optimist |
| 5 | 250 | 1.250 | 14 | Jolle, J/24, Laser |
| 6 | 400 | 2.000 | 16 | Fallen 8–12m |
| 8 | 700 | 3.500 | 20 | Fallen 12–16m |
| 10 | 1.100 | 5.500 | 24 | Fallen 16–20m |

### 3.5 Schnappschäkel (Snap Shackle)

**Form:** Kolbenbolzen mit Feder-Rückhaltung und oftmals einem Auslöse-Hebel (Trigger). Der Bügel ist fest, der Bolzen wird durch Federdruck geschlossen gehalten.

**Merkmale:**
- Schnellstes Öffnen und Schließen aller Schäkeltypen
- Einhand-Bedienung möglich
- Tripping-Varianten: Können unter Last geöffnet werden (Auslöseleine)
- NICHT so sicher wie Schraubschäkel — können sich unter bestimmten Umständen selbst öffnen
- Höheres Gewicht als vergleichbare Schraubschäkel

**Einsatz auf der Yacht:**
- Spinnaker-Fall (Standard): Schnelles Bergen des Spinnakers
- Spinnaker-Schot (bei Gennaker/Asymmetrisch)
- Großschot am Baumbeschlag
- Fockschot-Barberhauler
- Trapezhaken (bei Jollen)

**WARNUNG:** Snap-Schäkel dürfen NIEMALS für stehendes Gut, Wanten, Vorstag oder sicherheitsrelevante Verbindungen verwendet werden. Ein versehentliches Auslösen kann zu sofortigem Riggversagen führen.

**Typische Größen:**

| Gesamtlänge (mm) | WLL (daN) | MBL (daN) | Typische Anwendung |
|-------------------|-----------|-----------|-------------------|
| 70 | 200 | 1.000 | Jolle, Spi-Fall klein |
| 85 | 350 | 1.750 | Spi-Fall 8–12m |
| 100 | 600 | 3.000 | Spi-Fall 10–14m |
| 120 | 900 | 4.500 | Spi-Fall 14–18m |
| 145 | 1.400 | 7.000 | Spi-Fall 18m+ |
| 170 | 2.000 | 10.000 | Superyacht |

### 3.6 Langschäkel (Long Shackle / Long Dee)

**Form:** Verlängerter D-Schäkel mit größerem Abstand zwischen Bolzen und Bügelgrund. Wird dort eingesetzt, wo der Standardschäkel zu kurz ist, um beide Anschlagpunkte zu erreichen.

**Merkmale:**
- Größere lichte Weite als Standard-D-Schäkel
- Etwas geringere WLL als Standard-D bei gleichem Bolzendurchmesser (80–90 %)
- Kann gestapelte Beschläge aufnehmen (z.B. zwei Augplatten)

**Einsatz auf der Yacht:**
- Wantanschlüsse, wenn Abstand Augplatte–Spanner zu groß für Standard-D
- Backstag-Anschlüsse
- Verbindung von Ketten unterschiedlicher Gliedgröße
- Mooring-Anwendungen

**Typische Größen:**

| Bolzen-Ø (mm) | WLL (daN) | MBL (daN) | Lichte Weite (mm) |
|----------------|-----------|-----------|-------------------|
| 6 | 350 | 1.750 | 18 |
| 8 | 650 | 3.250 | 22 |
| 10 | 1.050 | 5.250 | 28 |
| 12 | 1.500 | 7.500 | 34 |

### 3.7 Weitbügelschäkel (Wide Body Shackle / Super Broad)

**Form:** Bügelschäkel mit besonders breitem Innenraum. Nimmt breite Bänder, Gurte oder mehrere Leinen auf.

**Merkmale:**
- Sehr breite Bügelöffnung (bis zu 3× Standard)
- Für Gurtbandverbindungen (Webbing) und breite Augplatten
- Oft in Hebezeuganwendungen, aber auch auf Yachten relevant
- Lastminderung gegenüber Standard-Bügelschäkel beachten

**Einsatz auf der Yacht:**
- Rettungsinsel-Befestigung (Gurtband)
- Davit-Haken (Beiboot-Hebezeug)
- Ankerbugrolle (breites Auge)
- Mooring-Poller mit breitem Auge

### 3.8 Kettenschäkel (Chain Shackle / Joining Shackle)

**Form:** Speziell für die Verbindung von Kettensträngen. Die Bügel-Innendimensionen passen exakt zu den Gliedern einer bestimmten Kettengröße (nach ISO 1704 / EN 818).

**Merkmale:**
- Passgenau für definierte Kettenglied-Maße
- Muss durch die Ankerwinsch passen (Wildcat/Kettennuss)
- Oft mit Bolt-Type-Bolzen und Splint für maximale Sicherheit
- Kalibrierte Varianten für kalibrierte Ankerkette

**Einsatz auf der Yacht:**
- Verbindung Ankerkette–Anker (Standardanwendung)
- Kettenverlängerung (zwei Kettenenden verbinden)
- Ersatz für beschädigte Kettenglieder
- Verbindung Kette–Vorleine (Kettenvorläufer)

**WICHTIG:** Der Kettenschäkel muss zur Kettennuss (Wildcat) der Ankerwinsch passen. Ein zu großer Schäkel blockiert die Winsch, ein zu kleiner hält die Kette nicht sicher.

**Größenzuordnung Kette–Schäkel:**

| Kettendurchmesser (mm) | Schäkel-Bolzen (mm) | Passender Bügel-Innen (mm) |
|------------------------|---------------------|-----------------------------|
| 6 | 8 | 9–10 |
| 8 | 10 | 12–13 |
| 10 | 12 | 15–16 |
| 12 | 14 | 18–19 |
| 13 | 16 | 20–21 |
| 16 | 19 | 24–25 |

### 3.9 Ankerschäkel (Anchor Shackle)

**Form:** Hochfester Bügelschäkel, speziell für die Verbindung zwischen Ankerkette und Anker dimensioniert. Oft verzinkt oder aus hochfestem Stahl (Klasse 6 oder 8).

**Merkmale:**
- Höhere MBL als Standard-Bügelschäkel gleicher Größe
- Oft mit Bolt-Type-Bolzen und Splint
- Verzinkter Stahl für Großanker, Edelstahl 316L für Yachten bis ca. 18m
- Muss zum Ankerauge passen

**Einsatz auf der Yacht:**
- Ankerkette–Anker (primärer Einsatz)
- Zweitanker-Verbindung
- Mooring-Kette

**Dimensionierungsregel:**
Der Ankerschäkel sollte eine MBL von mindestens 120 % der MBL der Ankerkette haben. Bei kalibrierter Kette muss er außerdem durch die Kettennuss passen.

---

## 4. Materialien und Konstruktion

### 4.1 Edelstahl AISI 316L (V4A / 1.4404)

**Der Standard im Yachtbau.**

**Zusammensetzung:**
- Chrom: 16–18 %
- Nickel: 10–14 %
- Molybdän: 2–3 % (wesentlich für Salzwasserbeständigkeit)
- Kohlenstoff: ≤0,03 % (L = Low Carbon, besser schweißbar, weniger Sensibilisierung)

**Eigenschaften:**

| Eigenschaft | Wert | Bewertung |
|-------------|------|-----------|
| Zugfestigkeit | 480–620 MPa | Mittel |
| Streckgrenze | 170–220 MPa | Mittel |
| Dehnung | 40–50 % | Hoch (duktil) |
| Dichte | 7,98 g/cm³ | Schwer |
| Korrosionsbeständigkeit | Sehr gut | Meerwasser geeignet |
| Magnetisch | Nein (austenitisch) | Vorteil (Kompass-Nähe) |

**Vorteile:**
- Sehr gute Korrosionsbeständigkeit in Salzwasser
- Gute Duktilität — Verformung vor Bruch (Warnung)
- Universell verfügbar, viele Hersteller
- Gutes Preis-Leistungs-Verhältnis
- Schweißbar (für Sonderanfertigungen)

**Nachteile:**
- Anfällig für Spaltkorrosion (Gewinde, enge Passungen)
- Tea Staining in belüfteten Salzwasser-Umgebungen
- Schwer (verglichen mit Aluminium, Titan)
- Kann in sauerstoffarmen Umgebungen (Unterwasser, unter Ablagerungen) korrodieren

**Qualitätsmerkmal:** Geschmiedet (forged) > Gegossen (cast) > Gestanzt (stamped). Geschmiedete Schäkel haben eine bis zu 30 % höhere Festigkeit bei gleichem Gewicht.

### 4.2 Duplex-Edelstahl 2205 (1.4462)

**Premium-Material für höchste Anforderungen.**

**Zusammensetzung:**
- Chrom: 22 %
- Nickel: 5 %
- Molybdän: 3 %
- Stickstoff: 0,14–0,20 %
- Gefüge: 50 % Austenit + 50 % Ferrit (= Duplex)

**Eigenschaften:**

| Eigenschaft | Wert | vs. 316L |
|-------------|------|----------|
| Zugfestigkeit | 620–880 MPa | +40–60 % |
| Streckgrenze | 450–550 MPa | +130–160 % |
| Dehnung | 25–30 % | Etwas geringer |
| Dichte | 7,80 g/cm³ | Gleich |
| Korrosionsbeständigkeit | Exzellent | Deutlich besser |
| Spaltkorrosionsbeständigkeit | Exzellent | Wesentlich besser |

**Vorteile:**
- Doppelte Streckgrenze im Vergleich zu 316L → kleinere, leichtere Schäkel bei gleicher WLL
- Hervorragende Beständigkeit gegen Spaltkorrosion und Spannungsrisskorrosion
- Ideal für permanent belastete Anwendungen (stehendes Gut)

**Nachteile:**
- 2–3× teurer als 316L
- Begrenzte Verfügbarkeit im Yachtbeschlag-Sortiment
- Schwieriger zu bearbeiten (härter)
- Leicht magnetisch (kann Kompass beeinflussen)

**Hersteller:** Blue Wave (DK) bietet eine vollständige Duplex-2205-Linie für Rigg-Beschläge.

### 4.3 Titan (Grade 5 / Ti-6Al-4V)

**Das ultimative Material für gewichtskritische Anwendungen.**

**Eigenschaften:**

| Eigenschaft | Wert | vs. 316L |
|-------------|------|----------|
| Zugfestigkeit | 900–1.100 MPa | +80–100 % |
| Streckgrenze | 830–900 MPa | +350–400 % |
| Dehnung | 10–15 % | Deutlich geringer |
| Dichte | 4,43 g/cm³ | –44 % (fast halb so schwer) |
| Korrosionsbeständigkeit | Exzellent | Besser, kein Spaltkorrosionsproblem |

**Vorteile:**
- Höchste Festigkeit bei geringstem Gewicht
- Vollständig immun gegen Salzwasser-Korrosion (keine Spaltkorrosion)
- Keine galvanische Korrosion mit Carbon-Rigg (wichtig für Superyachten)
- Extrem lange Lebensdauer

**Nachteile:**
- 5–10× teurer als 316L
- Spröder als 316L (weniger Warnung vor Bruch)
- Sehr schwierig zu bearbeiten (Spezialwerkzeug)
- Galvanische Probleme mit Aluminium
- Begrenzte Auswahl an Standardgrößen

**Hersteller:** Karver (FR), Tylaska (US), diverse Superyacht-Zulieferer.

### 4.4 Dyneema Soft-Schäkel (UHMWPE)

**Die Revolution aus dem Hochleistungssegeln.**

Soft-Schäkel bestehen aus Ultra-High-Molecular-Weight-Polyethylen (UHMWPE, Markenname Dyneema SK78/SK99) und ersetzen in vielen Anwendungen Metallschäkel vollständig.

**Aufbau:**
Ein Soft-Schäkel besteht aus einem Strang Dyneema-Tauwerk (typisch 12-fach geflochten), der an einem Ende einen Knoten (Diamond Knot oder Button Knot) hat und am anderen Ende eine Schlaufe (Eye). Die Schlaufe wird über den Knoten gezogen und sichert so die Verbindung.

**Eigenschaften:**

| Eigenschaft | Wert | vs. 316L Schäkel |
|-------------|------|-----------------|
| Zugfestigkeit | Abhängig von Ø (s.u.) | Vergleichbar bis höher |
| Gewicht | 3–15 g (je nach Größe) | –80–95 % |
| Korrosion | Keine | Kein Thema |
| UV-Beständigkeit | Mäßig (Schutz nötig) | n/a |
| Wärmebeständigkeit | Max. 60–70°C | Deutlich geringer |
| Abriebfestigkeit | Mäßig bis gut | Geringer als Metall |

**Tragfähigkeiten nach Leinendurchmesser:**

| Dyneema-Ø (mm) | MBL Soft-Schäkel (daN) | Entspricht Metall-Bolzen (mm) |
|-----------------|------------------------|------------------------------|
| 2 | 500 | ~4 |
| 3 | 1.100 | ~5 |
| 4 | 2.000 | ~6 |
| 5 | 3.100 | ~8 |
| 6 | 4.500 | ~9 |
| 8 | 8.000 | ~12 |
| 10 | 12.500 | ~14 |
| 12 | 18.000 | ~16+ |

**Vorteile:**
- Extrem leicht (besonders wichtig am Masttop: Gewicht × Hebelarm = Krängungsmoment)
- Keine Korrosion, keine galvanische Problematik
- Kein Beschädigen von Segeln, Tauwerk oder Deck bei Kontakt
- Leise (kein metallisches Klappern am Mast)
- Kann selbst hergestellt/repariert werden (Bordmittel)
- Schwimmt (wenn verloren gegangen)

**Nachteile:**
- UV-Degradation: Muss vor dauerhafter UV-Einstrahlung geschützt werden
- Wärmeempfindlich: Nicht an Reibungsstellen verwenden (Winsch, Block-Scheibe)
- Abrieb: Nicht über scharfe Kanten führen
- Creep: Unter Dauerlast kann UHMWPE kriechen (Längenänderung)
- Inspektion schwieriger als bei Metall (keine sichtbare Verformung)
- Selbstherstellung erfordert Erfahrung (Knotenfestigkeit!)

**WARNUNG:** Soft-Schäkel NIEMALS an Stellen verwenden, wo sie über Metall oder raue Oberflächen reiben. Die Fasern schmelzen bei ca. 65°C durch Reibungswärme.

### 4.5 Bronze (CuSn8 / Rotguss)

**Traditionelles Material, heute noch in Nischenanwendungen.**

**Eigenschaften:**

| Eigenschaft | Wert |
|-------------|------|
| Zugfestigkeit | 350–450 MPa |
| Dichte | 8,8 g/cm³ |
| Korrosionsbeständigkeit | Gut (patiniert, selbstschützend) |
| Galvanische Verträglichkeit | Gut mit Edelstahl, schlecht mit Aluminium |

**Einsatz:**
- Traditionsyachten (optische Gründe)
- Ankerketten-Verbindungen (historische Boote)
- Unter-Wasser-Anwendungen (selbstschützend durch Patina)

**Nachteile:**
- Deutlich schwerer als Edelstahl
- Geringere Festigkeit
- Begrenzte Verfügbarkeit moderner Formen
- Muss regelmäßig poliert werden (oder Patina akzeptieren)

### 4.6 Hochfester Stahl (verzinkt)

**Standard für Ankerketten-Schäkel und Großanwendungen.**

| Klasse | Zugfestigkeit | MBL-Faktor vs. 316L | Anwendung |
|--------|---------------|---------------------|-----------|
| Klasse 4 (M) | 400 MPa | ~0,8× | Standard-Ankerkette |
| Klasse 6 (S) | 600 MPa | ~1,2× | Hochfeste Ankerkette |
| Klasse 8 (T) | 800 MPa | ~1,6× | Spezial-Hebezeug |

**Vorteile:** Sehr hohe Festigkeit, günstig, passend zu Stahl-Ankerketten.
**Nachteile:** Korrodiert bei Beschädigung der Verzinkung, nicht für dauerhaften Unterwassereinsatz, galvanische Probleme mit Edelstahl.

### 4.7 Aluminium (hochfest, 7075-T6)

**Leicht, aber mit Einschränkungen im Marineeinsatz.**

| Eigenschaft | Wert |
|-------------|------|
| Zugfestigkeit | 540–570 MPa |
| Dichte | 2,81 g/cm³ (1/3 von Stahl) |
| Korrosionsbeständigkeit | Mäßig (eloxiert: gut) |

**Einsatz:** Regatta-Schäkel, temporäre Anwendungen, Jollen.
**WARNUNG:** Nicht für dauerhafte Salzwasser-Anwendungen ohne Eloxierung. Galvanische Korrosion mit Edelstahl und Bronze beachten.

### 4.8 Materialvergleich Gesamtübersicht

| Material | Festigkeit | Gewicht | Korrosion | Preis | Lebensdauer | Empfehlung |
|----------|-----------|---------|-----------|-------|-------------|------------|
| 316L geschmiedet | ●●●○○ | ●●○○○ | ●●●●○ | ●●●●○ | ●●●●○ | Standard Yacht |
| 316L gegossen | ●●○○○ | ●●○○○ | ●●●○○ | ●●●●● | ●●●○○ | Budget |
| Duplex 2205 | ●●●●○ | ●●○○○ | ●●●●● | ●●●○○ | ●●●●● | Premium Rigg |
| Titan Gr.5 | ●●●●● | ●●●●○ | ●●●●● | ●○○○○ | ●●●●● | Superyacht/Race |
| Dyneema SK78 | ●●●●○ | ●●●●● | ●●●●● | ●●●○○ | ●●●○○ | Race/Cruiser |
| Bronze | ●●○○○ | ●○○○○ | ●●●○○ | ●●●○○ | ●●●○○ | Tradition |
| Stahl verzinkt | ●●●●○ | ●●○○○ | ●●○○○ | ●●●●● | ●●○○○ | Anker/Mooring |
| Alu 7075 | ●●●○○ | ●●●●○ | ●●○○○ | ●●●○○ | ●●○○○ | Regatta temp. |

---

## 5. Produktlinien und Hersteller

### 5.1 Wichard (Frankreich) — Geschmiedete Edelstahlschäkel

**Unternehmenshintergrund:**
Wichard (gegründet 1919, Thiers, Frankreich) ist der weltweit führende Hersteller geschmiedeter Edelstahl-Yachtbeschläge. Jeder Wichard-Schäkel wird aus einem einzigen Stück AISI 316L warmgeschmiedet (nicht gegossen oder gestanzt), was eine um 20–30 % höhere Festigkeit bei gleicher Größe ergibt.

**Fertigungsverfahren:**
1. Warmschmieden bei 1.100–1.200°C aus Rundstahl
2. Gratentfernung und Formgebung
3. Wärmebehandlung (Lösungsglühen)
4. Kugelstrahlen (Shot Peening) für Oberflächenverdichtung
5. Polieren oder Satin-Finish
6. 100 % Proof-Load-Prüfung (jeder einzelne Schäkel!)
7. Laser-Gravur mit Artikelnummer und CE-Zeichen

**Produktlinien:**

#### 5.1.1 Wichard Standard D-Schäkel (Screw Pin)

| Art.-Nr. | Bolzen (mm) | WLL (daN) | MBL (daN) | Abmessungen L×B (mm) | Gewicht (g) | Preis (EUR) |
|----------|-------------|-----------|-----------|----------------------|-------------|-------------|
| 1401 | 4 | 160 | 800 | 16×10 | 8 | 3,50 |
| 1402 | 5 | 300 | 1.500 | 20×12 | 14 | 4,80 |
| 1403 | 6 | 500 | 2.500 | 24×14 | 22 | 6,50 |
| 1404 | 8 | 1.000 | 5.000 | 32×18 | 52 | 10,90 |
| 1405 | 10 | 1.500 | 7.500 | 40×22 | 100 | 16,80 |
| 1406 | 12 | 2.000 | 10.000 | 48×26 | 170 | 24,50 |
| 1407 | 14 | 2.800 | 14.000 | 56×30 | 260 | 35,00 |
| 1408 | 16 | 3.600 | 18.000 | 64×34 | 380 | 48,00 |

#### 5.1.2 Wichard Self-Locking D-Schäkel

Patentierter Selbstsicherungsmechanismus mit roter Markierung am Bolzen. Werkzeuglos bedienbar, vibrationssicher.

| Art.-Nr. | Bolzen (mm) | WLL (daN) | MBL (daN) | Gewicht (g) | Preis (EUR) |
|----------|-------------|-----------|-----------|-------------|-------------|
| 1441 | 5 | 280 | 1.400 | 16 | 9,50 |
| 1442 | 6 | 450 | 2.250 | 26 | 12,80 |
| 1443 | 8 | 900 | 4.500 | 58 | 19,50 |
| 1444 | 10 | 1.400 | 7.000 | 110 | 28,00 |
| 1445 | 12 | 1.900 | 9.500 | 185 | 38,00 |

#### 5.1.3 Wichard Captive-Pin D-Schäkel

Unverlierbare Bolzen durch integrierten Federmechanismus. Ideal für Masttop und über Wasser.

| Art.-Nr. | Bolzen (mm) | WLL (daN) | MBL (daN) | Gewicht (g) | Preis (EUR) |
|----------|-------------|-----------|-----------|-------------|-------------|
| 1461 | 5 | 280 | 1.400 | 18 | 11,00 |
| 1462 | 6 | 450 | 2.250 | 28 | 14,50 |
| 1463 | 8 | 900 | 4.500 | 62 | 22,00 |
| 1464 | 10 | 1.400 | 7.000 | 115 | 32,00 |

#### 5.1.4 Wichard Bügelschäkel (Bow Shackle, Screw Pin)

| Art.-Nr. | Bolzen (mm) | WLL (daN) | MBL (daN) | Gewicht (g) | Preis (EUR) |
|----------|-------------|-----------|-----------|-------------|-------------|
| 1421 | 5 | 250 | 1.250 | 16 | 5,20 |
| 1422 | 6 | 400 | 2.000 | 26 | 7,00 |
| 1423 | 8 | 800 | 4.000 | 60 | 12,50 |
| 1424 | 10 | 1.200 | 6.000 | 115 | 18,50 |
| 1425 | 12 | 1.700 | 8.500 | 190 | 27,00 |
| 1426 | 14 | 2.400 | 12.000 | 290 | 38,00 |

#### 5.1.5 Wichard Twist-Schäkel

| Art.-Nr. | Bolzen (mm) | WLL (daN) | MBL (daN) | Gewicht (g) | Preis (EUR) |
|----------|-------------|-----------|-----------|-------------|-------------|
| 1481 | 5 | 280 | 1.400 | 15 | 7,50 |
| 1482 | 6 | 450 | 2.250 | 24 | 10,00 |
| 1483 | 8 | 900 | 4.500 | 56 | 16,50 |
| 1484 | 10 | 1.400 | 7.000 | 105 | 24,00 |

#### 5.1.6 Wichard Fallenschäkel (Halyard Shackle)

| Art.-Nr. | Bolzen (mm) | WLL (daN) | MBL (daN) | Profil (mm) | Gewicht (g) | Preis (EUR) |
|----------|-------------|-----------|-----------|-------------|-------------|-------------|
| 1491 | 5 | 250 | 1.250 | 14 | 12 | 8,50 |
| 1492 | 6 | 400 | 2.000 | 16 | 20 | 11,50 |
| 1493 | 8 | 750 | 3.750 | 20 | 42 | 17,50 |
| 1494 | 10 | 1.200 | 6.000 | 24 | 80 | 26,00 |

#### 5.1.7 Wichard Snap-Schäkel

| Art.-Nr. | Typ | MBL (daN) | Länge (mm) | Gewicht (g) | Preis (EUR) |
|----------|-----|-----------|------------|-------------|-------------|
| 2671 | Standard | 1.200 | 70 | 30 | 22,00 |
| 2672 | Standard | 2.000 | 85 | 48 | 28,00 |
| 2673 | Standard | 3.000 | 100 | 72 | 36,00 |
| 2674 | Standard | 5.000 | 120 | 115 | 48,00 |
| 2681 | Tripping | 1.200 | 75 | 35 | 28,00 |
| 2682 | Tripping | 2.000 | 92 | 55 | 36,00 |
| 2683 | Tripping | 3.500 | 110 | 85 | 48,00 |
| 2684 | Tripping | 5.500 | 135 | 130 | 62,00 |

### 5.2 HR — Harken Rigger (USA/Italien)

**Unternehmenshintergrund:**
Harken (gegründet 1967, Pewaukee, Wisconsin, USA) ist vor allem für Blöcke und Winschen bekannt, bietet aber mit der HR-Linie (Harken Rigger) ein eigenständiges Sortiment an Rigg-Beschlägen und Schäkeln. HR-Produkte werden in Italien gefertigt.

#### 5.2.1 HR Forged D-Schäkel

| Art.-Nr. | Bolzen (mm) | WLL (daN) | MBL (daN) | Bolzentyp | Gewicht (g) | Preis (EUR) |
|----------|-------------|-----------|-----------|-----------|-------------|-------------|
| HR1305 | 5 | 270 | 1.350 | Screw Pin | 13 | 5,50 |
| HR1306 | 6 | 470 | 2.350 | Screw Pin | 21 | 7,50 |
| HR1308 | 8 | 950 | 4.750 | Screw Pin | 50 | 12,00 |
| HR1310 | 10 | 1.450 | 7.250 | Screw Pin | 95 | 18,00 |
| HR1312 | 12 | 1.950 | 9.750 | Screw Pin | 165 | 26,00 |

#### 5.2.2 HR Allen-Key D-Schäkel

| Art.-Nr. | Bolzen (mm) | WLL (daN) | MBL (daN) | Allen-Key (mm) | Gewicht (g) | Preis (EUR) |
|----------|-------------|-----------|-----------|----------------|-------------|-------------|
| HR1505 | 5 | 280 | 1.400 | 3 | 14 | 8,00 |
| HR1506 | 6 | 480 | 2.400 | 4 | 23 | 10,50 |
| HR1508 | 8 | 980 | 4.900 | 5 | 54 | 15,50 |
| HR1510 | 10 | 1.500 | 7.500 | 5 | 100 | 22,00 |
| HR1512 | 12 | 2.000 | 10.000 | 6 | 172 | 30,00 |

### 5.3 Harken Titelok-System

**Das werkzeuglose Schnellbefestigungssystem.**

Das Titelok-System von Harken ermöglicht das Öffnen und Schließen von Bolzen ohne Werkzeug. Ein Federmechanismus sichert den Bolzen automatisch. Besonders für Anwendungen, bei denen häufiges Umschäkeln nötig ist.

| Art.-Nr. | Bolzen (mm) | WLL (daN) | MBL (daN) | Gewicht (g) | Preis (EUR) |
|----------|-------------|-----------|-----------|-------------|-------------|
| TL2005 | 5 | 250 | 1.250 | 18 | 14,00 |
| TL2006 | 6 | 420 | 2.100 | 30 | 18,50 |
| TL2008 | 8 | 850 | 4.250 | 65 | 26,00 |
| TL2010 | 10 | 1.350 | 6.750 | 120 | 36,00 |

### 5.4 Blue Wave (Dänemark) — Duplex und Standard

**Unternehmenshintergrund:**
Blue Wave (Kolding, Dänemark) ist spezialisiert auf Rigg-Beschläge aus Edelstahl 316 und Duplex 2205. Bekannt für hervorragende Oberflächenqualität und konsequente CE-Zertifizierung.

#### 5.4.1 Blue Wave 316L D-Schäkel

| Art.-Nr. | Bolzen (mm) | WLL (daN) | MBL (daN) | Gewicht (g) | Preis (EUR) |
|----------|-------------|-----------|-----------|-------------|-------------|
| BW-D05-316 | 5 | 260 | 1.300 | 14 | 5,90 |
| BW-D06-316 | 6 | 440 | 2.200 | 22 | 7,80 |
| BW-D08-316 | 8 | 900 | 4.500 | 52 | 12,90 |
| BW-D10-316 | 10 | 1.400 | 7.000 | 98 | 19,00 |
| BW-D12-316 | 12 | 1.900 | 9.500 | 168 | 27,00 |

#### 5.4.2 Blue Wave Duplex 2205 D-Schäkel

| Art.-Nr. | Bolzen (mm) | WLL (daN) | MBL (daN) | Gewicht (g) | Preis (EUR) |
|----------|-------------|-----------|-----------|-------------|-------------|
| BW-D05-DX | 5 | 400 | 2.000 | 13 | 12,50 |
| BW-D06-DX | 6 | 680 | 3.400 | 21 | 16,00 |
| BW-D08-DX | 8 | 1.400 | 7.000 | 50 | 25,00 |
| BW-D10-DX | 10 | 2.200 | 11.000 | 95 | 36,00 |
| BW-D12-DX | 12 | 3.000 | 15.000 | 162 | 50,00 |

**Beachte:** Die Duplex-2205-Schäkel von Blue Wave haben bei gleichem Bolzendurchmesser eine um ~55 % höhere WLL als die 316L-Variante. Alternativ kann ein kleinerer (leichterer) Duplex-Schäkel den gleichen 316L-Schäkel ersetzen.

#### 5.4.3 Blue Wave Quick-Release D-Schäkel

| Art.-Nr. | Bolzen (mm) | WLL (daN) | MBL (daN) | Gewicht (g) | Preis (EUR) |
|----------|-------------|-----------|-----------|-------------|-------------|
| BW-QR06 | 6 | 420 | 2.100 | 25 | 14,00 |
| BW-QR08 | 8 | 860 | 4.300 | 58 | 20,00 |
| BW-QR10 | 10 | 1.350 | 6.750 | 108 | 28,00 |

### 5.5 Seldén (Schweden)

**Unternehmenshintergrund:**
Seldén (Göteborg, Schweden) ist vor allem als Mast- und Rigg-Hersteller bekannt, bietet aber ein umfassendes Sortiment an Beschlägen und Schäkeln, die speziell auf Seldén-Riggs abgestimmt sind.

#### 5.5.1 Seldén Rigg-Schäkel

| Art.-Nr. | Bolzen (mm) | WLL (daN) | MBL (daN) | Bolzentyp | Preis (EUR) |
|----------|-------------|-----------|-----------|-----------|-------------|
| 508-652 | 5 | 250 | 1.250 | Allen-Key 3mm | 7,50 |
| 508-653 | 6 | 430 | 2.150 | Allen-Key 4mm | 10,00 |
| 508-654 | 8 | 880 | 4.400 | Allen-Key 5mm | 14,50 |
| 508-655 | 10 | 1.350 | 6.750 | Allen-Key 5mm | 20,00 |
| 508-656 | 12 | 1.850 | 9.250 | Allen-Key 6mm | 28,00 |

#### 5.5.2 Seldén Fallenschäkel

| Art.-Nr. | Bolzen (mm) | WLL (daN) | MBL (daN) | Profil (mm) | Preis (EUR) |
|----------|-------------|-----------|-----------|-------------|-------------|
| 508-701 | 5 | 240 | 1.200 | 14 | 9,00 |
| 508-702 | 6 | 390 | 1.950 | 16 | 12,00 |
| 508-703 | 8 | 720 | 3.600 | 20 | 17,00 |

### 5.6 Sea-Dog (USA)

**Unternehmenshintergrund:**
Sea-Dog (Everett, Washington, USA) bietet ein breites Sortiment an Yachtbeschlägen im mittleren Preissegment. Die Schäkel sind gegossen (investment casting) aus AISI 316 Edelstahl.

#### 5.6.1 Sea-Dog Cast D-Schäkel

| Art.-Nr. | Bolzen (mm) | WLL (daN) | MBL (daN) | Gewicht (g) | Preis (EUR) |
|----------|-------------|-----------|-----------|-------------|-------------|
| 147054 | 5 | 200 | 800 | 15 | 2,80 |
| 147064 | 6 | 340 | 1.360 | 24 | 3,90 |
| 147084 | 8 | 680 | 2.720 | 56 | 6,50 |
| 147104 | 10 | 1.050 | 4.200 | 105 | 10,50 |
| 147124 | 12 | 1.500 | 6.000 | 178 | 15,00 |

**Hinweis:** Sea-Dog-Schäkel sind gegossen, nicht geschmiedet. Die MBL liegt daher ca. 20–30 % unter geschmiedeten Schäkeln gleicher Größe. Für kritische Rigg-Anwendungen (Wanten, Vorstag) wird ausdrücklich geschmiedete Ware empfohlen.

#### 5.6.2 Sea-Dog Cast Bow-Schäkel

| Art.-Nr. | Bolzen (mm) | WLL (daN) | MBL (daN) | Gewicht (g) | Preis (EUR) |
|----------|-------------|-----------|-----------|-------------|-------------|
| 147254 | 5 | 170 | 680 | 17 | 3,20 |
| 147264 | 6 | 280 | 1.120 | 28 | 4,50 |
| 147284 | 8 | 560 | 2.240 | 65 | 7,50 |
| 147304 | 10 | 880 | 3.520 | 120 | 12,00 |
| 147324 | 12 | 1.250 | 5.000 | 200 | 17,00 |

### 5.7 Kong (Italien)

**Unternehmenshintergrund:**
Kong (Monte Marenzo, Italien, gegründet 1830) ist ein traditionsreicher Hersteller von Verbindungselementen für Marine, Klettern und Industrie. Bekannt für hochwertige Snap-Schäkel und Karabiner.

#### 5.7.1 Kong Snap-Schäkel (Marine-Serie)

| Art.-Nr. | Typ | MBL (daN) | Länge (mm) | Gewicht (g) | Preis (EUR) |
|----------|-----|-----------|------------|-------------|-------------|
| 10.070 | Standard | 1.000 | 66 | 28 | 18,00 |
| 10.072 | Standard | 1.800 | 82 | 44 | 24,00 |
| 10.074 | Standard | 2.800 | 98 | 68 | 32,00 |
| 10.076 | Standard | 4.500 | 118 | 108 | 42,00 |
| 10.080 | Tripping | 1.200 | 72 | 32 | 24,00 |
| 10.082 | Tripping | 2.200 | 90 | 52 | 32,00 |
| 10.084 | Tripping | 3.500 | 108 | 82 | 42,00 |
| 10.086 | Tripping | 5.000 | 130 | 125 | 55,00 |

#### 5.7.2 Kong D-Schäkel (Forged)

| Art.-Nr. | Bolzen (mm) | WLL (daN) | MBL (daN) | Gewicht (g) | Preis (EUR) |
|----------|-------------|-----------|-----------|-------------|-------------|
| 11.050 | 5 | 270 | 1.350 | 14 | 5,00 |
| 11.060 | 6 | 460 | 2.300 | 22 | 6,80 |
| 11.080 | 8 | 920 | 4.600 | 52 | 11,00 |
| 11.100 | 10 | 1.420 | 7.100 | 98 | 17,00 |
| 11.120 | 12 | 1.950 | 9.750 | 170 | 25,00 |

### 5.8 Allen Brothers (UK)

**Unternehmenshintergrund:**
Allen Brothers (Brentwood, Essex, UK, gegründet 1956) ist auf Jollen- und Kleinkiel-Beschläge spezialisiert. Ihre Schäkel und Beschläge sind für den Regattaeinsatz optimiert — leicht, funktional, preisbewusst.

#### 5.8.1 Allen D-Schäkel (Geschmiedet, 316L)

| Art.-Nr. | Bolzen (mm) | WLL (daN) | MBL (daN) | Gewicht (g) | Preis (EUR) |
|----------|-------------|-----------|-----------|-------------|-------------|
| A-085 | 4 | 150 | 750 | 7 | 2,50 |
| A-086 | 5 | 250 | 1.250 | 13 | 3,80 |
| A-087 | 6 | 420 | 2.100 | 20 | 5,20 |
| A-088 | 8 | 850 | 4.250 | 48 | 8,50 |

#### 5.8.2 Allen Twist-Schäkel

| Art.-Nr. | Bolzen (mm) | WLL (daN) | MBL (daN) | Gewicht (g) | Preis (EUR) |
|----------|-------------|-----------|-----------|-------------|-------------|
| A-095 | 5 | 240 | 1.200 | 12 | 5,00 |
| A-096 | 6 | 400 | 2.000 | 19 | 7,00 |
| A-097 | 8 | 800 | 4.000 | 45 | 11,00 |

#### 5.8.3 Allen Snap-Schäkel (Nylon-Body)

Leichte Snap-Schäkel mit Nylon-Körper und Edelstahl-Bolzen. Für Jollen und Leichtwindsegel.

| Art.-Nr. | MBL (daN) | Länge (mm) | Gewicht (g) | Preis (EUR) |
|----------|-----------|------------|-------------|-------------|
| A-401 | 400 | 55 | 8 | 6,50 |
| A-402 | 650 | 68 | 12 | 8,50 |
| A-403 | 1.000 | 82 | 18 | 12,00 |

### 5.9 Herstellervergleich Zusammenfassung

| Hersteller | Material | Fertigung | Stärke | Schwäche | Preisniveau |
|-----------|----------|-----------|--------|----------|-------------|
| Wichard | 316L | Geschmiedet | Qualität, Vielfalt, Self-Lock | Preis | ●●●●○ |
| HR (Harken) | 316L | Geschmiedet | Rigg-Expertise, Passgenau | Sortimentsbreite | ●●●●○ |
| Harken Titelok | 316L | Geschmiedet | Werkzeugloses System | Preis, Spezialformat | ●●●●● |
| Blue Wave | 316L/Duplex | Geschmiedet | Duplex-Linie, CE-Doku | Bekanntheitsgrad | ●●●○○ |
| Seldén | 316L | Geschmiedet | Rigg-Kompatibilität | Nur eigenes System | ●●●○○ |
| Sea-Dog | 316 | Gegossen | Preis | Festigkeit (gegossen) | ●●○○○ |
| Kong | 316L | Geschmiedet | Snap-Schäkel, Tradition | Kleineres Yacht-Sortiment | ●●●○○ |
| Allen Brothers | 316L | Geschmiedet | Jollen/Regatta, Preis | Nur bis 8mm Bolzen | ●●○○○ |

---

## 6. Dimensionierung und Auswahl

### 6.1 Dimensionierung nach Leinendurchmesser

Der Schäkel muss zur Leine passen. Grundregel: Der lichte Schäkeldurchgang (Innenweite) muss mindestens dem 1,5-fachen des Leinendurchmessers entsprechen.

| Leinen-Ø (mm) | Min. Schäkel-Innenweite (mm) | Empfohlener Bolzen-Ø (mm) | MBL Schäkel min. (daN) |
|----------------|------------------------------|---------------------------|------------------------|
| 4 | 6 | 4 | 750 |
| 5 | 8 | 5 | 1.250 |
| 6 | 9 | 5–6 | 1.500 |
| 8 | 12 | 6–8 | 2.500 |
| 10 | 15 | 8–10 | 4.000 |
| 12 | 18 | 10–12 | 6.000 |
| 14 | 21 | 12–14 | 8.000 |
| 16 | 24 | 14–16 | 12.000 |

### 6.2 Dimensionierung nach erwarteter Last

**Schritt-für-Schritt-Verfahren:**

1. **Maximale Betriebslast ermitteln:**
   - Aus Rigg-Berechnung (gemessen → confidence: measured)
   - Aus Herstellerangaben des Mastes/Riggs
   - Oder: Faustformel-Schätzung (confidence: estimated)

2. **Dynamischen Lastfaktor anwenden:**
   - Ruhige Bedingungen: ×1,5
   - Normaler Segelbetrieb: ×2,0
   - Schwerwetter: ×3,0

3. **Sicherheitsfaktor anwenden:**
   - Stehendes Gut: ×4
   - Laufendes Gut: ×5
   - Sicherheitsausrüstung: ×6

4. **Erforderliche MBL berechnen:**
   ```
   MBL_erforderlich = Betriebslast × Dynamischer_Faktor × Sicherheitsfaktor
   ```

5. **Schäkel aus Herstellerkatalog wählen mit MBL ≥ MBL_erforderlich**

**Berechnungsbeispiel 1: Genuafall 12m-Yacht**

```
Betriebslast (aus Rigg-Berechnung): 600 daN
Dynamischer Faktor (normales Segeln): ×2,0
→ Dynamische Last: 1.200 daN
Sicherheitsfaktor (laufendes Gut): ×5
→ Erforderliche MBL: 6.000 daN
→ Wichard 1404 (8mm, MBL 5.000 daN) → NICHT ausreichend
→ Wichard 1405 (10mm, MBL 7.500 daN) → Ausreichend ✓
```

**Berechnungsbeispiel 2: Ankerschäkel 14m-Yacht**

```
Ankerhaltekraft (Ankergewicht × Haltekraftfaktor): 800 daN
Dynamischer Faktor (Ankern bei Starkwind): ×3,5
→ Dynamische Last: 2.800 daN
Sicherheitsfaktor (Ankergeschirr): ×4
→ Erforderliche MBL: 11.200 daN
→ Bügelschäkel 12mm (MBL 7.000 daN) → NICHT ausreichend
→ Bügelschäkel 14mm (MBL 10.000 daN) → NICHT ausreichend
→ Bügelschäkel 16mm (MBL 13.500 daN) → Ausreichend ✓
```

### 6.3 Dimensionierung nach Bootsklasse

**Faustregeln für schnelle Orientierung (confidence: estimated):**

| Anwendung | Jolle (4–8m) | Fahrten (8–14m) | Perf. Cruiser (10–16m) | Blauwasser (12–18m) | Superyacht (18m+) |
|-----------|-------------|-----------------|----------------------|--------------------|--------------------|
| Großfall | 4–5mm | 6–8mm | 8–10mm | 10–12mm | 12–16mm |
| Genuafall | 4–5mm | 6–8mm | 8–10mm | 8–10mm | 12–16mm |
| Spi-Fall | 4mm | 5–6mm | 6–8mm | 8mm | 10–12mm |
| Wanten oben | — | 6–8mm | 8–10mm | 10–12mm | 14–16mm |
| Wanten unten | — | 8–10mm | 10–12mm | 12–14mm | 16–19mm |
| Vorstag | — | 8–10mm | 10–12mm | 12–14mm | 16–22mm |
| Anker | 5–6mm | 8–10mm | 10–12mm | 12–14mm | 16–22mm |

### 6.4 Checkliste Schäkelauswahl

```
SCHÄKELAUSWAHL — CHECKLISTE
==============================

□ 1. Lastanforderung bestimmen (WLL/MBL)
□ 2. Belastungsrichtung klären (axial / seitlich / multi)
□ 3. Typ wählen (D / Bow / Twist / Halyard / Snap)
□ 4. Material wählen (316L / Duplex / Titan / Dyneema)
□ 5. Bolzentyp wählen (Screw / Bolt / Captive / Allen / Self-Lock / Snap)
□ 6. Innenweite prüfen (passt Leine / Kette / Beschlag?)
□ 7. Profil prüfen (passt durch Mastnut? Stört am Segel?)
□ 8. Galvanische Verträglichkeit prüfen
□ 9. Gewicht prüfen (besonders am Masttop)
□ 10. Sicherungskonzept klären (Draht / Loctite / inherent)
□ 11. Ersatzteil-Verfügbarkeit prüfen
□ 12. Budget berücksichtigen
```

---

## 7. Montage und Installation

### 7.1 Allgemeine Montageregeln

**Regel 1: Der Bolzen muss frei bleiben.**
Der Schäkelbolzen darf nicht die Last tragen. Die Last muss immer auf dem Bügel liegen, der Bolzen schließt nur den Bügel. Wenn der Bolzen Hauptlastträger wird, ist die Anwendung falsch.

**Regel 2: Keine Querbelastung auf D-Schäkel.**
D-Schäkel müssen axial belastet werden. Bei wechselnden Zugrichtungen: Bügelschäkel verwenden.

**Regel 3: Nie mehr als einen Schäkel für eine Verbindung.**
Zwei Schäkel ineinander zu hängen (Schäkel-Kette) ist verboten. Die Lastübertragung wird unkontrollierbar, der innere Schäkel belastet den äußeren Bolzen auf Biegung.

**Regel 4: Bolzen immer sichern.**
- Schraubbolzen: Seizing Wire oder Loctite 243
- Bolt-Type: Splint einsetzen, Enden umbiegen
- Allen-Key: Loctite 243 (mittelfest)
- Self-Locking: Funktion prüfen (roter Indikator sichtbar)
- Captive Pin: Federrückhaltung prüfen

**Regel 5: Passgenaue Größe.**
Der Schäkel muss zur Öse/Augplatte passen. Ein zu kleiner Schäkel wird am Bolzen überlastet. Ein zu großer Schäkel kann sich verkanten und Querlasten erzeugen.

### 7.2 Montage Rigg-Schäkel (Wanten, Vorstag)

**Vorbereitung:**
1. Schäkel und Bolzen inspizieren (Risse, Korrosion, Verformung)
2. Gewinde reinigen (Lappen mit Bremsenreiniger)
3. Tef-Gel oder Duralac auf Gewinde und Kontaktflächen auftragen
4. Inbus-Schlüssel in korrekter Größe bereitlegen

**Montage:**
1. Schäkel in die Gabelkopf-Gabel (Toggle) einführen
2. Bolzen von der zugänglichen Seite einsetzen
3. Bolzen mit Inbusschlüssel anziehen: handfest + 1/4 Umdrehung
4. Bei Schraubbolzen: Seizing Wire durchfädeln und sichern
5. Sicherstellen, dass der Schäkel sich frei bewegen kann (keine Verkantung)

**Kontrolle:**
- Bolzen bündig mit Bügelaußenseite? (nicht vorstehend)
- Schäkel schwenkt frei?
- Seizing Wire korrekt?
- Keine Klemmung gegen benachbarte Beschläge?

### 7.3 Montage Fallenschäkel

**Vorbereitung:**
1. Fallenende vorbereiten (Spleiß mit Auge oder Pressung)
2. Segelkopf (Head Board) auf Zustand prüfen
3. Schäkel passend zum Mastnut-Profil wählen

**Montage:**
1. Schäkel durch das Fallauge führen
2. Durch das Segelkopf-Auge führen
3. Bolzen einsetzen und sichern
4. Prüfen, dass der Schäkel durch die Mastnut passt (Segel testweise anheben)
5. Sicherstellen, dass keine scharfen Kanten am Segeltuch reiben

**Häufiger Fehler:** Der Schäkel ist zu breit für die Mastnut und blockiert beim Segelsetzen am Masttop. → Immer vor dem Masthissen oder Segelsetzen am Boden testen.

### 7.4 Montage Ankerschäkel

**Vorbereitung:**
1. Ankerkette und Ankerauge reinigen
2. Passenden Bügelschäkel wählen (muss durch Kettennuss passen)
3. Splint bereitlegen

**Montage:**
1. Kette letztes Glied in den Schäkel-Bügel einführen
2. Ankerauge in den Schäkel-Bügel einführen
3. Bolzen einsetzen, Mutter aufschrauben (handfest + 1/4 Umdrehung)
4. Splint durch Bolzenbohrung stecken
5. Splintenden umbiegen (beide Seiten)
6. Optional: Seizing Wire als Backup

**WICHTIG:** Nach dem Anker-Einfahren den Schäkel durch die Kettennuss laufen lassen und prüfen, ob er sauber durchläuft. Ein blockierender Schäkel kann die Ankerwinsch beschädigen und ein Bergen des Ankers unmöglich machen.

### 7.5 Montage Snap-Schäkel

1. Snap-Schäkel am Fallenende (oder Leinenende) befestigen — durch Spleiß-Auge oder vorhandene Öse
2. Federbolzen testen: Öffnen, Schließen, Einrasten prüfen
3. Tripping-Leine anbringen (bei Tripping-Varianten)
4. Prüfen, dass der Bolzen vollständig einrastet (kein Halb-Offen)
5. Unter leichter Last Sitz prüfen

### 7.6 Soft-Schäkel Montage

1. Soft-Schäkel auf Beschädigung prüfen (Abrieb, UV-Schäden, Knotenintegrität)
2. Schlaufe (Eye) durch die zu verbindende Öse führen
3. Knoten (Button) durch die Schlaufe führen
4. Unter Last: Schlaufe zieht sich um den Knoten zusammen → selbstsichernd
5. Prüfen: Knoten muss deutlich größer als Schlaufen-Öffnung sein

**WARNUNG:** Einen Soft-Schäkel mit beschädigten Fasern (Abrieb >10 % des Querschnitts, verfärbte Fasern, aufgeraute Oberfläche) sofort ersetzen.

### 7.7 Drehmomente und Anzugshinweise

| Bolzentyp | Anzugsmoment | Werkzeug |
|-----------|-------------|----------|
| Screw Pin (alle Größen) | Handfest + 1/4 Umdrehung | Finger |
| Allen-Key 3mm | 2–3 Nm | Inbus 3mm |
| Allen-Key 4mm | 4–6 Nm | Inbus 4mm |
| Allen-Key 5mm | 8–12 Nm | Inbus 5mm |
| Allen-Key 6mm | 15–20 Nm | Inbus 6mm |
| Bolt-Type mit Mutter | Handfest + Splint | Gabelschlüssel |

**WICHTIG:** Schraubbolzen NIEMALS mit Zange oder Schraubenschlüssel anziehen. Das Gewinde wird überlastet und der Schäkel kann nicht mehr gelöst werden (oder das Gewinde reißt).

---

## 8. Fehlerbild-Atlas

### 8.1 Fehlerbild F-01: Bügelverformung (Aufbiegen)

**Beschreibung:** Der Bügel ist sichtbar aufgebogen — der Abstand zwischen den Schenkelenden ist größer als im Neuzustand. Der Bolzen sitzt nicht mehr bündig oder kann sogar herausfallen.

**Ursache:**
- Überlastung (Last > WLL)
- Querbelastung auf D-Schäkel
- Schlagbelastung (z.B. schlagendes Segel)
- Material-Ermüdung nach vielen Zyklen

**Bewertung:** KRITISCH — Sofort ersetzen. Ein verformter Bügel hat eine reduzierte MBL (geschätzt 40–60 % des Nennwerts) und kann sich unter Last öffnen.

**AYDI-Erkennung (Visuell):** Symmetrieabweichung >2mm sichtbar auf Foto → confidence: visual_high

### 8.2 Fehlerbild F-02: Bolzenverschleiß (Durchmesserreduzierung)

**Beschreibung:** Der Bolzen zeigt sichtbaren Materialabtrag an der Kontaktfläche zum Bügel oder zur angeschlagenen Öse. Der Durchmesser ist messbar reduziert.

**Ursache:**
- Reibung durch wechselnde Lastrichtung
- Vibration unter Last
- Korrosiver Verschleiß (Salzkristalle als Abrasiv)
- Mangelnde Schmierung

**Bewertung:** KRITISCH bei >10 % Durchmesserreduzierung. WARNUNG bei 5–10 %. Der Bolzen ist das schwächste Glied — seine Scherquerschnitts-Fläche sinkt mit dem Quadrat des Durchmessers.

**Messmethode:** Messschieber am Bolzen an der dünnsten Stelle. Vergleich mit Nenn-Ø (auf Schäkel eingraviert oder aus Katalog).

### 8.3 Fehlerbild F-03: Spaltkorrosion am Gewinde

**Beschreibung:** Braune oder schwarze Verfärbung am Schraubbolzen-Gewinde. Das Gewinde fühlt sich rau an, der Bolzen lässt sich schwer drehen. In fortgeschrittenen Fällen sitzt der Bolzen fest.

**Ursache:**
- Sauerstoffarmut im engen Gewindespalt
- Salzablagerungen im Gewinde
- Mangelnde Wartung (Bolzen wurde nie gelöst und gereinigt)
- Falsches Material (304 statt 316L)

**Bewertung:** WARNUNG bis KRITISCH. Bolzen ersetzen. Bügel-Gewinde prüfen (Gewindelehre oder neuen Bolzen einschrauben — wenn er klemmt, Schäkel ersetzen).

**Prävention:** Tef-Gel auf Gewinde, jährliches Lösen/Reinigen/Neu-Einsetzen.

### 8.4 Fehlerbild F-04: Ermüdungsriss

**Beschreibung:** Feiner, oft kaum sichtbarer Riss am Übergang Bügel–Schenkel (Radiusbereich) oder am Schenkelende nahe der Bolzenbohrung.

**Ursache:**
- Zyklische Belastung über lange Zeit
- Spannungskonzentration an Radien und Bohrungen
- Korrosionsbedingte Rissinitiierung (Stress Corrosion Cracking)

**Bewertung:** KRITISCH — Sofort ersetzen. Ein Ermüdungsriss wächst unter Last exponentiell und führt zum plötzlichen Bruch ohne weitere Vorwarnung.

**Erkennung:** Farbeindringprüfung (Penetrant Testing) mit Diffu-Therm oder Magnaflux. Visuell nur bei fortgeschrittenen Rissen erkennbar.

**AYDI-Erkennung (Visuell):** Nur bei deutlich sichtbaren Rissen → confidence: visual_medium (kleine Risse nicht erkennbar)

### 8.5 Fehlerbild F-05: Festsitzender Bolzen (Kaltverschweißung)

**Beschreibung:** Der Schraubbolzen oder Allen-Key-Bolzen lässt sich nicht mehr drehen. Auch mit erhöhtem Drehmoment (Werkzeug) bewegt sich der Bolzen nicht.

**Ursache:**
- Kaltverschweißung (Galling): Edelstahl auf Edelstahl ohne Schmierung unter Druck
- Korrosionsprodukte im Gewinde
- Übermäßiges Anzugsmoment bei der Montage
- Fehlendes Anti-Seize

**Bewertung:** Funktional — Schäkel kann nicht geöffnet werden. Wenn Öffnen nötig, muss der Schäkel zerstört werden (Bolzen ausbohren oder Bügel auftrennen).

**Prävention:** IMMER Anti-Seize-Paste oder Tef-Gel auf Gewinde vor der Montage.

### 8.6 Fehlerbild F-06: Tea Staining (Oberflächenkorrosion)

**Beschreibung:** Braune, tee-ähnliche Verfärbungen auf der Edelstahl-Oberfläche, besonders in belüfteten Bereichen (nicht unter Wasser).

**Ursache:**
- Salzablagerungen auf passivierter Oberfläche
- Kontamination mit Fremd-Eisen (Funkenflug, Stahlwolle, Werkzeug)
- Unzureichende Passivierung bei der Herstellung

**Bewertung:** Kosmetisch (bei Oberflächenbeschränkung). WARNUNG, wenn tiefe Pitting-Korrosion darunter liegt.

**Behebung:** Oxalsäure-Reiniger (Barkeeper's Friend), dann Passivierung mit Citronen-Passivierungsgel. Bei Pitting: Schäkel ersetzen.

### 8.7 Fehlerbild F-07: Falsche Belastungsrichtung

**Beschreibung:** Ein D-Schäkel wird sichtbar schief belastet — die Leine oder der Beschlag zieht seitlich statt axial. Erkennbar an ungleichmäßigen Abnutzungsspuren am Bolzen.

**Ursache:**
- Falscher Schäkeltyp für die Anwendung (D statt Bow)
- Falsche Montage
- Veränderte Rigg-Geometrie nach Umrüstung

**Bewertung:** WARNUNG — Korrektur durch Typwechsel (Bügelschäkel) oder Neuausrichtung.

### 8.8 Fehlerbild F-08: Snap-Schäkel Feder-Ermüdung

**Beschreibung:** Der Snap-Schäkel schließt nicht mehr vollständig — der Federbolzen rastet nicht sicher ein, oder die Feder ist sichtbar schwächer (Bolzen springt langsam zurück).

**Ursache:**
- Materialermüdung der Feder (Alter, Zyklen)
- Salzkorrosion im Federmechanismus
- Verschmutzung (Sand, Salzkristalle) im Bolzenkanal
- UV-Degradation bei Feder-Gehäuse-Dichtungen

**Bewertung:** KRITISCH — Snap-Schäkel kann sich unter Last öffnen. Sofort ersetzen. Keine Reparatur möglich (Feder nicht austauschbar bei den meisten Modellen).

### 8.9 Fehlerbild F-09: Soft-Schäkel UV-Degradation

**Beschreibung:** Die Dyneema-Fasern sind verfärbt (von weiß nach grau/gelb), fühlen sich steif und spröde an. Der Knoten oder die Schlaufe zeigen aufgeraute Fasern.

**Ursache:**
- Dauerhafte UV-Einstrahlung ohne Schutz
- Alter (UHMWPE degradiert auch bei UV-Schutz über Jahre)
- Kombination UV + Salzablagerungen

**Bewertung:** WARNUNG bei leichter Verfärbung, KRITISCH bei spröden Fasern oder sichtbarem Faserverlust. Die MBL kann bei starker UV-Degradation um 30–50 % sinken.

**Prüfung:** Biegetest — das Seil/der Schäkel muss sich geschmeidig biegen lassen. Wenn es knistert oder steif bleibt, sofort ersetzen.

### 8.10 Fehlerbild F-10: Soft-Schäkel Knoten-Verrutschen

**Beschreibung:** Der Button-Knoten des Soft-Schäkels hat sich unter Last gelockert oder ist teilweise durch die Schlaufe gerutscht.

**Ursache:**
- Knoten wurde nicht korrekt gebunden (zu wenige Durchgänge)
- Dyneema-Creep unter Dauerlast
- Zu große Schlaufe im Verhältnis zum Knoten
- Nasses UHMWPE (glatter als trocken)

**Bewertung:** KRITISCH — Der Schäkel kann sich öffnen. Knoten neu binden oder Schäkel ersetzen.

### 8.11 Fehlerbild F-11: Galvanische Korrosion am Kontaktpunkt

**Beschreibung:** Starke Korrosion am Kontaktpunkt Schäkel–Beschlag, obwohl der Schäkel selbst aus korrosionsbeständigem Material besteht. Typisch: weiße Pulverablagerungen (Aluminium) oder grüne Patina (Bronze) am Kontaktpunkt.

**Ursache:**
- Kontakt zweier unverträglicher Metalle in Salzwasser-Umgebung
- Typisch: Edelstahl-Schäkel auf Aluminium-Mastbeschlag
- Fehlende Isolation (Tef-Gel, Kunststoff-Buchse)

**Bewertung:** WARNUNG bis KRITISCH (je nach Materialverlust am schwächeren Metall). Isolation herstellen, beschädigte Teile ersetzen.

### 8.12 Fehlerbild F-12: Unsachgemäße Sicherung

**Beschreibung:** Der Bolzen ist nicht gesichert — kein Seizing Wire bei Schraubbolzen, kein Splint bei Bolt-Type, kein Loctite bei Allen-Key. Der Bolzen kann sich durch Vibration lösen.

**Ursache:**
- Nachlässigkeit bei der Montage
- Sicherungsmittel nicht an Bord
- „Wird beim nächsten Mal gemacht" (nie)

**Bewertung:** WARNUNG — Potenziell KRITISCH. Umgehend sichern.

**AYDI-Erkennung (Visuell):** Fehlender Seizing Wire bei sichtbarem Schraubbolzen → confidence: visual_high

---

## 9. Troubleshooting-Entscheidungsbaum

### 9.1 Baum T-01: Schäkel lässt sich nicht öffnen

```
Schäkel lässt sich nicht öffnen
├── Schraubbolzen?
│   ├── JA → WD-40 / Kriechöl einsprühen, 30 min warten
│   │   ├── Löst sich → Bolzen reinigen, Tef-Gel, wieder einsetzen
│   │   └── Löst sich nicht → Rohrzange auf Bolzen (Tuch unterlegen)
│   │       ├── Löst sich → Gewinde prüfen, ggf. Schäkel ersetzen
│   │       └── Löst sich nicht → Kaltverschweißung
│   │           ├── Bolzen ausbohren (Ø kleiner als Gewinde)
│   │           └── Schäkel mit Bolzenschneider/Flex auftrennen
│   │               └── Schäkel ersetzen
│   └── NEIN → Allen-Key-Bolzen?
│       ├── JA → Inbus einsetzen, Kriechöl, Schlagschraubendreher
│       │   ├── Löst sich → Reinigen, Loctite 243, neu einsetzen
│       │   └── Löst sich nicht → Innensechskant ausgenudet?
│       │       ├── JA → Torx-Einsatz einschlagen, versuchen
│       │       │   └── Sonst: Ausbohren oder Auftrennen
│       │       └── NEIN → Erhitzen auf 80°C (Heißluftföhn)
│       │           → Erneut versuchen
│       └── NEIN → Self-Locking / Captive Pin?
│           └── Mechanismus prüfen, Feder ggf. mit Ahle lösen
│               └── Sonst: Hersteller-Anleitung konsultieren
```

### 9.2 Baum T-02: Welcher Schäkeltyp für meine Anwendung?

```
Welcher Schäkeltyp?
├── Last aus einer Richtung?
│   ├── JA → D-Schäkel
│   │   ├── Permanent installiert? → Allen-Key oder Bolt-Type
│   │   ├── Häufig öffnen? → Self-Locking oder Captive Pin
│   │   └── Braucht 90°-Drehung? → Twist-Schäkel
│   └── NEIN → Bügelschäkel (Bow)
│       ├── Ankerkette? → Passenden Kettenschäkel wählen
│       └── Mehrere Leinen? → Weitbügelschäkel prüfen
├── Muss durch Mastnut passen?
│   └── JA → Fallenschäkel (Halyard Shackle)
├── Muss unter Last lösbar sein?
│   └── JA → Snap-Schäkel (nur für Spi/Gennaker!)
├── Gewicht kritisch (Masttop/Regatta)?
│   └── JA → Soft-Schäkel (Dyneema) oder Titan
└── Budget-Lösung (nicht sicherheitskritisch)?
    └── Gegossener Schäkel (Sea-Dog o.ä.)
```

### 9.3 Baum T-03: Schäkel-Material richtig wählen

```
Materialwahl
├── Salzwasser-Umgebung?
│   ├── JA → Edelstahl 316L (Standard)
│   │   ├── Höhere Festigkeit nötig? → Duplex 2205 (Blue Wave)
│   │   ├── Gewicht kritisch? → Titan oder Dyneema
│   │   └── Carbon-Rigg? → Titan (keine galvanische Korrosion)
│   └── NEIN (Süßwasser/Binnenrevier)
│       ├── Budget? → Edelstahl 316 (auch 304 akzeptabel)
│       └── Regatta-Jolle? → Aluminium 7075 eloxiert
├── Kontakt mit Aluminium-Beschlag?
│   └── JA → Tef-Gel verwenden oder Dyneema-Soft-Schäkel
├── Traditionelle Optik gewünscht?
│   └── JA → Bronze (CuSn8)
└── Ankerkette aus verzinktem Stahl?
    └── JA → Verzinkter Stahlschäkel (gleiche Galvanik)
```

### 9.4 Baum T-04: Schäkel hat sich gelöst / ist verloren

```
Schäkel hat sich gelöst
├── Unter Segeln (Last auf dem System)?
│   ├── JA → SOFORT Last wegnehmen (Segel bergen/fieren)
│   │   ├── Crew warnen (peitschende Leinen)
│   │   ├── Betroffene Leine sichern (Winsch/Klampe)
│   │   └── Provisorium:
│   │       ├── Ersatzschäkel vorhanden? → Einsetzen
│   │       ├── Kein Ersatz? → Dyneema-Schlinge als Ersatz
│   │       └── Auch das nicht? → Leine direkt befestigen (Palstek)
│   └── NEIN → Schäkel suchen und prüfen
│       ├── Bolzen vorhanden? → Warum gelöst?
│       │   ├── Fehlende Sicherung → Sichern
│       │   ├── Vibration → Self-Locking-Typ verwenden
│       │   └── Gewinde verschlissen → Ersetzen
│       └── Bolzen verloren → Neuen Bolzen beschaffen
│           └── Nicht verfügbar? → Provisorischer Bolzen
│               (Edelstahl-Schraube passender Größe + Mutter)
└── WARNUNG: Jeden improvisierten Schäkel-Ersatz
    bei nächster Gelegenheit durch Originalschäkel ersetzen
```

### 9.5 Baum T-05: Ankerschäkel-Probleme

```
Ankerschäkel-Problem
├── Schäkel passt nicht durch Kettennuss
│   ├── Schäkel zu groß → Kleineren Schäkel wählen
│   │   └── Aber MBL ausreichend? → Prüfen!
│   └── Kettennuss zu klein → Kettennuss tauschen oder
│       Schäkel vor Kettennuss positionieren (Stopper)
├── Schäkel korrodiert (festsitzend)
│   ├── Kriechöl + Schlagschraubendreher
│   └── Nicht lösbar → Bolzenschneider (Schäkel opfern)
├── Splint verloren
│   ├── Ersatz-Splint vorhanden? → Einsetzen
│   └── Kein Splint? → Provisorium:
│       ├── Edelstahl-Draht durch Bolzenbohrung
│       ├── Kabelbinder (temporär, nur Notfall!)
│       └── Bei nächster Gelegenheit: Splint ersetzen
├── Ankerwirbel klemmt
│   └── → Siehe separate Wissensdatei 12_02
└── Kette verdreht sich im Schäkel
    ├── Ankerwirbel einbauen (zwischen Kette und Anker)
    └── Bügelschäkel statt D-Schäkel verwenden
```

---

## 10. FAQ — Häufige Fragen

### F-01: Was ist der Unterschied zwischen WLL und SWL?

**Antwort:** WLL (Working Load Limit) und SWL (Safe Working Load) bezeichnen im Wesentlichen das Gleiche — die maximal zulässige Betriebslast. Der Begriff SWL ist veraltet und wurde in der Normen-Welt durch WLL ersetzt, weil SWL fälschlicherweise suggerierte, dass die Last „sicher" sei. WLL betont stärker, dass es sich um einen Grenzwert handelt, der nicht überschritten werden darf. In Herstellerkatalogen und auf Schäkeln finden Sie heute überwiegend WLL.

### F-02: Muss ein Schäkel vom TÜV geprüft sein?

**Antwort:** Für Yacht-Schäkel gibt es keine TÜV-Pflicht. Die CE-Kennzeichnung ist für Beschläge im Sinne der Maschinenrichtlinie (2006/42/EG) relevant, wenn sie als Hebezeug-Komponente eingesetzt werden. Für reine Yachtanwendungen gilt die Recreational Craft Directive (2013/53/EU), die jedoch keine einzelnen Beschläge, sondern das Boot als Ganzes zertifiziert. Seriöse Hersteller (Wichard, Blue Wave, Kong) lassen ihre Schäkel freiwillig nach EN 13889 (geschmiedete Stahlschäkel) oder internen Standards prüfen und geben MBL/WLL an.

### F-03: Wie oft muss ich Schäkel inspizieren?

**Antwort:** Empfohlene Inspektionsintervalle:
- Vor jeder Saison: Sichtinspektion aller zugänglichen Schäkel
- Jährlich: Alle Schäkel lösen, reinigen, prüfen, Tef-Gel, wieder einsetzen
- Nach jedem Starkwind-Ereignis (>6 Bft): Rigg-Schäkel visuell prüfen
- Alle 5 Jahre: Professionelle Rigg-Inspektion inkl. Rissprüfung kritischer Schäkel
- Regatta-Boote: Vor jeder Regatta Sicht-Check aller belasteten Schäkel

### F-04: Kann ich einen verformten Schäkel zurückbiegen?

**Antwort:** NEIN. Ein verformter Schäkel hat seine Streckgrenze überschritten. Das Material ist plastisch verformt und intern vorgeschädigt. Zurückbiegen verschärft die Schädigung (Kaltverfestigung + Rissinitiierung). Verformte Schäkel IMMER ersetzen.

### F-05: Warum sind Wichard-Schäkel teurer als No-Name?

**Antwort:** Wichard-Schäkel werden warmgeschmiedet (nicht gegossen), was eine um 20–30 % höhere Festigkeit ergibt. Jeder einzelne Schäkel wird mit Proof Load geprüft. Die Oberfläche wird kugelgestrahlt (Druckspannungen → Ermüdungsfestigkeit). Material ist garantiert AISI 316L (nicht nur „Edelstahl"). Die Qualitätskontrolle und Rückverfolgbarkeit sind lückenlos. Für sicherheitskritische Anwendungen (Rigg, Anker) ist der Preisunterschied eine lohnende Investition.

### F-06: Kann ich Dyneema-Soft-Schäkel selbst herstellen?

**Antwort:** Ja, mit Erfahrung. Benötigt wird: Dyneema SK78 oder SK99 Flechtleine (12-fach geflochten), eine Spleißnadel (Fid), Anleitung für den Diamond Knot. Die kritische Stelle ist der Knoten — er muss mindestens 60 % der Leinenfestigkeit erhalten. Für sicherheitskritische Anwendungen wird die Verwendung von kommerziell gefertigten Soft-Schäkeln mit geprüfter MBL empfohlen. Selbstgefertigte Soft-Schäkel haben eine confidence von „estimated".

### F-07: 316 oder 316L — macht das einen Unterschied?

**Antwort:** 316L hat einen niedrigeren Kohlenstoffgehalt (≤0,03 % vs. ≤0,08 % bei 316). Dies macht 316L weniger anfällig für interkristalline Korrosion, besonders in geschweißten Bereichen. Für geschmiedete Schäkel (nicht geschweißt) ist der Unterschied in der Praxis gering. Für gegossene Schäkel kann der höhere C-Gehalt von 316 zu Karbidausscheidungen an Korngrenzen führen. Empfehlung: Wenn möglich, immer 316L wählen.

### F-08: Warum darf man zwei Schäkel nicht ineinander hängen?

**Antwort:** Bei zwei ineinander gehängten Schäkeln wird der Bolzen des äußeren Schäkels auf Biegung belastet, wofür er nicht ausgelegt ist. Die Kontaktfläche zwischen den Schäkeln ist sehr klein (Punkt- statt Flächenkontakt), was zu extremem Flächenpressdruck führt. Außerdem entsteht ein Gelenk, das unkontrollierte Bewegungen ermöglicht. Die effektive Tragfähigkeit sinkt auf geschätzt 30–50 % des schwächeren Schäkels. Stattdessen: Einen größeren Schäkel verwenden oder ein Kettenglied als Zwischenverbinder.

### F-09: Ist ein Snap-Schäkel für das Großfall geeignet?

**Antwort:** Technisch möglich, aber NICHT empfohlen für Fahrtenyachten. Die Feder kann ermüden und ein unbeabsichtigtes Öffnen unter Last hätte den Verlust des Großsegels zur Folge. Für Regattayachten, bei denen schnelles Segelwechseln Priorität hat, werden Snap-Schäkel am Großfall manchmal verwendet — unter der Voraussetzung regelmäßiger Inspektion und jährlichem Tausch. Standard-Empfehlung: Captive-Pin- oder Self-Locking-Schäkel für Fallen.

### F-10: Wie sichere ich einen Schraubbolzen gegen Lösen?

**Antwort:** Drei bewährte Methoden:
1. **Seizing Wire (bevorzugt):** Monel-Draht (0,8mm) durch das Bolzenauge und eine Bohrung im Bügel fädeln, verdrehen, Enden kürzen. Muss bei jedem Öffnen neu gemacht werden.
2. **Loctite 243 (mittelfest):** Auf das Gewinde auftragen. Lösbar mit Inbus und normalem Drehmoment, aber vibrationssicher. Ideal für semi-permanente Verbindungen.
3. **Kabelbinder (Notlösung):** Durch Bolzenauge und Bügel. UV-instabil, muss regelmäßig ersetzt werden. Nur als temporäre Lösung akzeptabel.

### F-11: Was bedeutet „geschmiedet" vs. „gegossen"?

**Antwort:** **Geschmiedet (forged):** Das Metall wird bei hoher Temperatur (1.100–1.200°C) in eine Form gepresst. Das Korngeflecht wird verdichtet und ausgerichtet, was höhere Festigkeit und Zähigkeit ergibt. **Gegossen (cast/investment cast):** Flüssiges Metall wird in eine Form gegossen und erstarrt. Das Gefüge ist gröber, mit potenziellen Poren und Lunkern. Geschmiedete Schäkel haben typisch 20–30 % höhere MBL bei gleichem Gewicht und sind weniger anfällig für Materialfehler.

### F-12: Kann ich einen verzinkten Stahlschäkel an meiner Edelstahlkette verwenden?

**Antwort:** Technisch möglich, aber galvanisch problematisch. Zink (Opferanode) wird im Kontakt mit Edelstahl beschleunigt korrodieren. Der Schäkel wird innerhalb weniger Monate seine Zinkschicht verlieren und dann als blanker Stahl rosten. Empfehlung: Gleiches Material verwenden — Edelstahlkette mit Edelstahlschäkel, verzinkte Kette mit verzinktem Schäkel.

### F-13: Wie erkenne ich einen 316L-Schäkel?

**Antwort:** Seriöse Hersteller prägen/gravieren die Materialbezeichnung (316, 316L, A4, 1.4404) auf den Schäkel. Im Zweifelsfall hilft ein Magnettest: 316/316L ist nicht magnetisch (austenitisch). Wenn der Schäkel am Magneten haftet, ist es kein austenitischer Edelstahl — möglicherweise 430 (ferritisch) oder gar verzinkter Stahl. ACHTUNG: Kaltverformung (z.B. am Bügelradius geschmiedeter Schäkel) kann lokale Magnetisierbarkeit erzeugen — dies allein ist kein Ausschlusskriterium.

### F-14: Wie viele Ersatzschäkel brauche ich für eine Blauwasserreise?

**Antwort:** Empfohlenes Minimum:
- 4× D-Schäkel (2× in der häufigsten Rigg-Größe, 2× eine Größe kleiner)
- 2× Bügelschäkel (Ankergröße)
- 2× Fallenschäkel (in der Fallengröße)
- 2× Snap-Schäkel (Spi-Größe)
- 4× Soft-Schäkel (verschiedene Größen)
- 10× Splinte (passend zu Bolt-Type-Schäkeln)
- 1× Seizing Wire (Rolle Monel-Draht)
- 1× Tef-Gel (Tube)
Gesamt ca. 14–16 Schäkel + Zubehör.

### F-15: Was ist ein „HR"-Schäkel?

**Antwort:** HR steht für „Harken Rigger" — die Rigg-Beschlag-Linie von Harken. HR-Schäkel werden in Italien geschmiedet und sind speziell für Rigg-Anwendungen (Wanten, Vorstag) optimiert. Sie sind oft mit Allen-Key-Bolzen ausgestattet und haben eine sehr gute Passform zu Harken-Blöcken und -Beschlägen.

### F-16: Darf ein Schäkel bei der Ankerwinsch durch die Kettennuss laufen?

**Antwort:** Idealerweise nicht — der Schäkel sollte vor der Kettennuss stoppen (manueller Stopp oder Kettenstopper). In der Praxis laufen viele Bügelschäkel problemlos durch die Kettennuss, wenn sie korrekt dimensioniert sind. ABER: Der Schäkel-Bolzen kann in der Kettennuss klemmen und die Winsch blockieren. Vor Inbetriebnahme IMMER testen. Spezielle „Ankerwinsch-kompatible" Schäkel sind erhältlich (z.B. Mantus, Ultra-Marine).

### F-17: Kann ich einen Schäkel reparieren (z.B. schweißen)?

**Antwort:** NEIN. Ein reparierter (geschweißter, gelöteter, gebogener) Schäkel hat keine definierte Tragfähigkeit mehr und darf nicht weiterverwendet werden. Schweißen verändert das Gefüge, erzeugt Wärmeeinflusszonen und hebt die Vorteile des Schmiedens auf. Defekte Schäkel ersetzen, nicht reparieren.

### F-18: Sind Titan-Schäkel ihr Geld wert?

**Antwort:** Für die meisten Fahrtenyachten: Nein. Das Preis-Leistungs-Verhältnis von 316L oder Duplex 2205 ist für Normalanwendungen besser. Titan lohnt sich bei: Masttop-Schäkeln (Gewicht × Hebelarm), Carbon-Rigg (keine galvanische Korrosion), Superyachten (Budget sekundär, Lebensdauer primär), Hochleistungsregatta (jedes Gramm zählt).

### F-19: Warum haben manche Schäkel eine rote Markierung?

**Antwort:** Die rote Markierung bei Wichard-Schäkeln kennzeichnet das Self-Locking-System. Sie zeigt an, dass der Bolzen korrekt verriegelt ist. Wenn die rote Markierung nicht sichtbar ist, ist der Bolzen nicht vollständig geschlossen. Andere Hersteller verwenden ähnliche Farbcodes: Grün = gesichert, Rot = offen/entsichert (variiert nach Hersteller).

### F-20: Wie lagere ich Schäkel über den Winter?

**Antwort:** 
1. Alle Schäkel mit Süßwasser spülen (Salz entfernen)
2. Trocknen lassen (Druckluft in Gewinde)
3. Bolzen lösen, Gewinde reinigen
4. Tef-Gel auf Gewinde und Kontaktflächen
5. Bolzen wieder einsetzen (nur leicht anziehen)
6. Trocken lagern (nicht in Plastiktüte — Kondenswasser!)
7. Idealerweise in einem mit Silicagel bestückten Behälter

### F-21: Was ist ein „Swage-Schäkel"?

**Antwort:** Ein Swage-Schäkel wird durch Pressen (Swaging) am Drahtende eines Wants befestigt. Er ist ein Hybrid aus Schäkel und Wantterminal — der untere Teil wird auf den Draht gepresst, der obere Teil ist ein Standard-Schäkelkopf mit Bolzen. Swage-Schäkel werden in Rigg-Shops mit hydraulischen Pressmaschinen montiert und sind nicht selbst herstellbar.

### F-22: Kann ich Edelstahl-Schäkel in Aluminium-Masten verwenden?

**Antwort:** Ja, aber mit Vorsichtsmaßnahmen gegen galvanische Korrosion. IMMER Tef-Gel oder Duralac auf die Kontaktflächen auftragen. Bei Neubau: Kunststoff-Isolierbuchsen zwischen Schäkel und Aluminium-Beschlag. Regelmäßig inspizieren — weiße, puderige Ablagerungen am Aluminium deuten auf galvanische Korrosion hin.

### F-23: Was ist besser für das Spinnaker-Fall: Snap-Schäkel oder Soft-Schäkel?

**Antwort:** Beide haben Berechtigung:
- **Snap-Schäkel:** Schnelleres Handling, unter Last lösbar (Tripping), bewährt. Aber: schwerer, teurer, Feder-Ermüdung.
- **Soft-Schäkel:** Leichter (80–90 % weniger Gewicht am Masttop), kein Beschädigen des Spinnaker-Stoffs, kein Klappern. Aber: langsamer beim Schäkeln, nicht unter Last lösbar.
Empfehlung: Soft-Schäkel für Fahrtensegler (weniger Handlings, Gewicht am Masttop reduziert), Snap-Schäkel für Regattasegler (schnelles Handling wichtiger).

### F-24: Wie berechne ich die nötige Schäkelgröße für mein Want?

**Antwort:** 
1. Drahtdurchmesser des Wants ermitteln (Messschieber oder Rigg-Plan)
2. Wantlast aus Rigg-Berechnung ablesen (oder: Faustformel: Verdrängung × 1,3 für V1-Want einer Fahrtenyacht)
3. Sicherheitsfaktor 4:1 anwenden → Erforderliche MBL = Wantlast × 4
4. Schäkel-Innenweite muss zum Gabelkopf und Toggle passen
5. Schäkel mit MBL ≥ erforderlicher MBL und passender Innenweite wählen
Im Zweifelsfall: Eine Nummer größer wählen. Das Mehrgewicht eines größeren Schäkels ist vernachlässigbar.

### F-25: Warum klappert mein Fallenschäkel am Mast?

**Antwort:** Metallschäkel klappern gegen das Aluminium- oder Carbon-Mastprofil, wenn das Fall locker ist. Lösungen:
1. **Fall durchsetzen** (leicht spannen, auch wenn kein Segel gesetzt ist)
2. **Soft-Schäkel verwenden** (kein metallisches Klappern)
3. **Schäkel-Schutz** (Schrumpfschlauch oder Tape um den Schäkel)
4. **Fall von Mast wegführen** (Elastik-Leine zieht Fall seitlich weg)
5. **Fall komplett ablegen** (bei Langzeitliegeplatz)
Klappernde Fallen sind nicht nur lästig für Stegnachbarn, sondern verursachen auch Eloxal-Abrieb am Mast.

---

## 11. Glossar

### A

**Ankergeschirr (Ground Tackle):**
Gesamtheit aller Komponenten der Ankerausrüstung: Anker, Kette, Vorleine, Schäkel, Wirbel, Kettenstopper, Winsch.

**Ankerschäkel (Anchor Shackle):**
Hochfester Bügelschäkel für die Verbindung zwischen Ankerkette und Anker. Muss zur Kettennuss der Ankerwinsch passen.

**Anti-Seize-Paste:**
Schmier- und Korrosionsschutzpaste für Gewinde und Kontaktflächen. Verhindert Kaltverschweißung (Galling) und Spaltkorrosion. Empfohlen: Tef-Gel (PTFE-basiert), Duralac (für Aluminium-Kontakt), Lanocote.

**Austenitisch:**
Kristallstruktur von Edelstahl 316/316L. Nicht magnetisch, gute Korrosionsbeständigkeit, gute Verformbarkeit.

### B

**Bolt-Type (Sicherungsbolzen):**
Schäkelbolzen mit durchgehendem Schaft, Mutter und Splintbohrung. Höchste Sicherheit gegen unbeabsichtigtes Lösen.

**Bow Shackle (Bügelschäkel):**
Schäkel mit Ω-förmigem Bügel für Mehrrichtungsbelastung. Standardschäkel für Ankerverbindungen.

**Bruchlast (Breaking Load / MBL):**
Die minimale Last, bei der der Schäkel unter statischer Belastung versagt. Prüfwert, nicht Betriebswert.

**Button Knot (Stopperknoten):**
Kugelförmiger Knoten am Ende eines Soft-Schäkels. Hält die Schlaufe geschlossen. Typisch: Diamond Knot.

### C

**Captive Pin:**
Unverlierbarker Bolzen, der durch einen Federmechanismus oder Sicherungsring im Bügel gehalten wird.

**CE-Kennzeichnung:**
Europäisches Konformitätszeichen. Für Schäkel relevant, wenn als Hebezeug-Komponente eingesetzt (EN 13889).

**Creep (Kriechen):**
Langsame, plastische Verformung unter Dauerlast. Bei UHMWPE/Dyneema relevant — Soft-Schäkel können sich unter Dauerlast längen.

**Crevice Corrosion (Spaltkorrosion):**
Lokale Korrosion in engen Spalten (Gewinde, Bolzen-Bügel-Kontakt), wo der Sauerstoffgehalt absinkt.

### D

**D-Schäkel (Dee Shackle):**
Schmaler, D-förmiger Schäkel für einachsige Belastung. Kompakteste und leichteste Bauform.

**Dekanewton (daN):**
Krafteinheit im Yachtbau. 1 daN = 10 N ≈ 1,02 kgf. Bequeme Einheit, da sie in etwa der Kilogramm-Kraft entspricht.

**Diamond Knot:**
Spezialknoten für Soft-Schäkel. Bildet einen kompakten, kugelförmigen Stopper, der die Schlaufe sichert.

**Duralac:**
Korrosionsschutzpaste speziell für Aluminium-Edelstahl-Kontakt. Verhindert galvanische Korrosion.

**Duplex-Edelstahl:**
Edelstahl mit gemischtem austenitisch-ferritischem Gefüge. Höhere Festigkeit und bessere Korrosionsbeständigkeit als 316L. Typisch: Duplex 2205.

**Dyneema:**
Markenname für UHMWPE-Fasern (Ultra-High-Molecular-Weight-Polyethylen) der Firma DSM. Höchste Festigkeit bei geringstem Gewicht unter allen synthetischen Fasern.

### E

**EN 13889:**
Europäische Norm für geschmiedete Stahlschäkel. Definiert Prüfverfahren, WLL-Bestimmung und Kennzeichnungspflichten.

**Ermüdung (Fatigue):**
Materialversagen durch wiederholte zyklische Belastung bei einer Last unter der statischen Bruchlast.

### F

**Fallenschäkel (Halyard Shackle):**
Flach profilierter Schäkel für die Verbindung Fall–Segelkopf. Muss durch die Mastnut passen.

**Fid (Spleißnadel):**
Werkzeug zum Spleißen von Dyneema-Leinen. Benötigt für die Herstellung von Soft-Schäkeln.

**Forged (Geschmiedet):**
Herstellungsverfahren, bei dem Metall bei hoher Temperatur in Form gepresst wird. Ergibt höhere Festigkeit als Gießen.

### G

**Galling (Kaltverschweißung):**
Festfressen zweier Edelstahloberflächen unter Druck. Typisch: Schraubbolzen in Edelstahl-Bügel ohne Schmierung.

**Galvanische Korrosion:**
Elektrochemische Korrosion bei Kontakt zweier unterschiedlicher Metalle in einem Elektrolyten (Salzwasser).

**Geschmiedet:**
→ Siehe Forged.

### H

**Halyard Shackle:**
→ Siehe Fallenschäkel.

### I

**Investment Casting (Feinguss):**
Gießverfahren mit Wachsmodell. Ergibt bessere Oberfläche und Maßhaltigkeit als Sandguss, aber geringere Festigkeit als Schmieden.

### K

**Kettennuss (Wildcat / Gypsy):**
Kettenlaufrad der Ankerwinsch. Der Ankerschäkel muss durch die Kettennuss passen.

**Kaltverformung (Cold Working):**
Formgebung bei Raumtemperatur. Erhöht lokal die Härte, aber verringert die Duktilität. NIEMALS Schäkel kalt verformen (biegen, verdrehen).

### L

**Loctite 243:**
Mittelfeste Schraubensicherung (anaerob). Für Allen-Key-Bolzen in Schäkeln empfohlen. Lösbar mit normalem Werkzeug und leichter Erwärmung.

### M

**MBL (Minimum Breaking Load):**
Mindest-Bruchlast eines Schäkels unter statischer Belastung. Der Schäkel versagt garantiert NICHT unterhalb dieser Last.

**Monel-Draht:**
Nickel-Kupfer-Legierung (67 % Ni, 30 % Cu). Wird als Seizing Wire (Sicherungsdraht) für Schäkelbolzen verwendet. Korrosionsbeständig, weich genug zum Biegen.

### N

**Nicht beurteilbar:**
AYDI-Standardantwort, wenn eine zuverlässige Bewertung nicht möglich ist. Besser als eine unsichere Schätzung.

### O

**Omega-Schäkel:**
→ Siehe Bügelschäkel (Bow Shackle).

### P

**Passivierung:**
Bildung einer schützenden Chromoxid-Schicht auf Edelstahl. Kann durch Beizen oder Citronensäure-Behandlung verbessert werden.

**Proof Load (Prüflast):**
Die Last, mit der ein Schäkel werksseitig geprüft wird, ohne bleibende Verformung. Typisch: 40–60 % der MBL.

**Pütting (Chainplate):**
Befestigungspunkt der Wanten am Rumpf. Der Rigg-Schäkel verbindet Want (über Spanner/Toggle) mit dem Pütting.

### Q

**Querbelastung (Side Load):**
Belastung quer zur Schäkelhauptachse. Reduziert die effektive Tragfähigkeit erheblich (50–70 % bei D-Schäkel).

### R

**Recreational Craft Directive (2013/53/EU):**
EU-Richtlinie für Sportboote 2,5–24m. Regelt CE-Zertifizierung des Gesamtbootes, nicht einzelner Beschläge.

### S

**Safety Factor (Sicherheitsfaktor):**
Verhältnis MBL/WLL. Kompensiert dynamische Lasten, Ermüdung, Korrosion und Unvorhergesehenes.

**Seizing Wire (Sicherungsdraht):**
Dünner Metalldraht (Monel oder Edelstahl, 0,8–1,0mm) zum Sichern von Schraubbolzen.

**Self-Locking:**
Selbstsichernder Bolzenmechanismus. Patentierte Systeme verschiedener Hersteller (z.B. Wichard).

**Shackle:**
Englisch für Schäkel.

**Shot Peening (Kugelstrahlen):**
Oberflächenbehandlung, bei der kleine Stahlkugeln auf die Oberfläche geschossen werden. Erzeugt Druckspannungen, die die Ermüdungsfestigkeit erhöhen.

**Snap Shackle (Schnappschäkel):**
Schäkel mit federbelastetem Kolbenbolzen für schnelles Öffnen/Schließen.

**Soft Shackle (Textilschäkel):**
Schäkel aus UHMWPE/Dyneema-Fasern. Extrem leicht, keine Korrosion.

**Spaltkorrosion:**
→ Siehe Crevice Corrosion.

**Splint (Cotter Pin / Split Pin):**
Doppelschenkliger Sicherungsstift aus Edelstahl oder Bronze. Wird durch die Bolzenbohrung gesteckt und umgebogen.

**Streckgrenze (Yield Strength):**
Die Spannung, ab der ein Material bleibend verformt wird. Unterhalb der Streckgrenze federt das Material zurück (elastisch).

**SWL (Safe Working Load):**
Veralteter Begriff für WLL. Wird in aktuellen Normen nicht mehr verwendet.

### T

**Tea Staining:**
Braune Oberflächenverfärbung auf Edelstahl durch Salzablagerungen. Kosmetisch, aber kann auf Pitting hindeuten.

**Tef-Gel:**
PTFE-basierte Anti-Seize-Paste. Standardprodukt für Gewinde und Metall-Metall-Kontaktflächen auf Yachten.

**Titelok:**
Harken-patentiertes Schnellverschlusssystem für Schäkelbolzen. Werkzeugloses Öffnen/Schließen.

**Toggle (Gabelkopf):**
Gelenkiges Verbindungselement zwischen Want-Spanner und Pütting-Schäkel. Ermöglicht winkeltreue Lasteinleitung.

**Twist Shackle (Wirbelschäkel):**
Um 90° verdrehter D- oder Bügelschäkel für Verbindungen zwischen verschiedenen Belastungsebenen.

### U

**UHMWPE:**
Ultra-High-Molecular-Weight-Polyethylen. Grundmaterial für Dyneema-Fasern und Soft-Schäkel.

### V

**V4A:**
Deutsche Werkstoffbezeichnung für austenitischen Edelstahl mit Molybdän (entspricht AISI 316/316L).

### W

**Wildcat (Kettennuss):**
→ Siehe Kettennuss.

**WLL (Working Load Limit):**
Maximale zulässige Betriebslast eines Schäkels im Dauerbetrieb. MBL ÷ Sicherheitsfaktor = WLL.

### Z

**Zugfestigkeit (Tensile Strength):**
Die maximale Spannung, die ein Material unter einachsigem Zug aushält, bevor es bricht. Nicht identisch mit MBL (die ist ein Bauteilwert, Zugfestigkeit ist ein Materialwert).

---

## 12. Schnell-Referenz

### 12.1 Schäkeltyp-Schnellwahl

| Anwendung | Empfohlener Typ | Bolzentyp | Material |
|-----------|----------------|-----------|----------|
| Want (permanent) | D-Schäkel | Allen-Key | 316L/Duplex |
| Vorstag | D-Schäkel | Allen-Key | 316L/Duplex |
| Backstag | D-/Langschäkel | Allen-Key | 316L |
| Großfall | Fallenschäkel | Captive/Self-Lock | 316L |
| Genuafall | Fallenschäkel/Twist | Captive/Self-Lock | 316L |
| Spi-Fall | Snap-Schäkel oder Soft | Snap/Dyneema | 316L/Dyneema |
| Anker–Kette | Bügelschäkel | Bolt+Splint | 316L/verz. Stahl |
| Block-Befestigung | D-/Bügelschäkel | Screw Pin | 316L |
| Mooring | Bügelschäkel | Bolt+Splint | 316L |
| Lifeline | D-Schäkel | Bolt+Splint | 316L |
| Rettungsinsel | Weitbügelschäkel | Bolt+Splint | 316L |

### 12.2 Kurzformel Dimensionierung

```
MBL_erforderlich = Betriebslast × Dynamikfaktor × Sicherheitsfaktor

Dynamikfaktoren:
  Ruhig: 1,5 | Normal: 2,0 | Schwer: 3,0 | Ruckartig: 4,0

Sicherheitsfaktoren:
  Stehendes Gut: 4 | Laufendes Gut: 5 | Sicherheit: 6

Beispiel: 500 daN × 2,0 × 5 = 5.000 daN → Schäkel mit MBL ≥ 5.000 daN
```

### 12.3 Preis-Orientierung (Stand 2026)

| Typ | 6mm Bolzen (EUR) | 8mm Bolzen (EUR) | 10mm Bolzen (EUR) |
|-----|-----------------|-----------------|-------------------|
| 316L geschmiedet (Wichard) | 6–7 | 11–12 | 17–18 |
| 316L gegossen (Sea-Dog) | 3–4 | 6–7 | 10–11 |
| Duplex 2205 (Blue Wave) | 16 | 25 | 36 |
| Allen-Key (HR) | 10–11 | 15–16 | 22 |
| Self-Locking (Wichard) | 12–13 | 19–20 | 28 |
| Snap-Schäkel (Wichard) | 28–36 | — | — |
| Soft-Schäkel (Dyneema 5mm) | 12–18 | — | — |

---

## ANHANG A — Fallstudien

### A.1 Fallstudie: Riggversagen durch verformten Schäkel — Bavaria 40 Cruiser

**Yacht:** Bavaria 40 Cruiser, Baujahr 2012, 12,35m
**Revier:** Ägäis (Griechenland)
**Vorfall:** Während einer Überfahrt bei 25 kn Wind (6 Bft) und 1,5m Seegang versagte das V1-Oberwant backbord.

**Analyse:**
Der D-Schäkel (8mm Bolzen, Screw Pin, Hersteller unbekannt — kein Branding) am Masttop-Beschlag des V1-Wants war aufgebogen. Der Bolzen war herausgefallen. Das Want fiel lose auf Deck.

**Ursache:**
- Der Schäkel war ein gegossener (nicht geschmiedeter) Billig-Schäkel ohne MBL-Angabe
- Geschätzte MBL: ca. 2.500–3.000 daN (gegossen, 8mm)
- V1-Wantlast bei 25 kn + 1,5m Seegang (Rigg-Berechnung): ca. 1.800 daN statisch × 2,5 (dynamisch) = 4.500 daN
- Der Schäkel war für die Anwendung unterdimensioniert
- Zusätzlich fehlte der Seizing Wire — der Bolzen war ungesichert

**Lehren:**
1. Rigg-Schäkel MÜSSEN geschmiedet sein und eine Hersteller-MBL-Angabe tragen
2. Dimensionierung: MBL ≥ Wantlast × 4 (Sicherheitsfaktor stehendes Gut)
3. Bolzensicherung (Seizing Wire oder Allen-Key) ist keine Option, sondern Pflicht
4. Bei Bavaria-Serienyachten: Originalschäkel prüfen und ggf. durch Wichard/HR ersetzen

**AYDI-Bewertung:** Confidence: documented (Schadensbericht Versicherung). Fehlercode: F-01 + F-12.

### A.2 Fallstudie: Galvanische Korrosion Mast–Schäkel — Hanse 415

**Yacht:** Hanse 415, Baujahr 2016, 12,40m
**Revier:** Ostsee (Dänemark)
**Vorfall:** Bei der Winterinspektion wurde starke weiße Korrosion an den Aluminium-Mastbeschlägen im Bereich der Wantschäkel festgestellt.

**Analyse:**
Die Edelstahl-316L-Schäkel (Wichard, 10mm) waren direkt auf Aluminium-Augplatten am Mast montiert — ohne jegliche Isolation. Nach 8 Jahren Nutzung zeigte das Aluminium an den Kontaktflächen Pitting-Korrosion von bis zu 1,5mm Tiefe. Die Wandstärke der Augplatten war von 5mm auf 3,5mm reduziert.

**Ursache:**
- Galvanische Korrosion: Edelstahl (edel) + Aluminium (unedel) in Salzwasser
- Kein Tef-Gel oder Duralac auf den Kontaktflächen
- 8 Jahre ohne Inspektion der Kontaktstellen

**Maßnahmen:**
1. Alle Augplatten durch neue ersetzt (Rigger-Werkstatt)
2. Tef-Gel auf alle Kontaktflächen
3. Kunststoff-Isolierbuchsen zwischen Schäkel und Augplatte
4. Jährliche Inspektion der Kontaktflächen in AYDI Level 2 hinterlegt

**AYDI-Bewertung:** Confidence: measured (Pitting-Tiefe mit Messschieber gemessen). Fehlercode: F-11.

### A.3 Fallstudie: Soft-Schäkel-Versagen am Spi-Fall — J/109

**Yacht:** J/109, Baujahr 2005, 10,97m
**Revier:** Solent (UK)
**Vorfall:** Beim Bergen des Asymmetrischen Spinnakers bei 18 kn riss der Soft-Schäkel am Fall. Der Spinnaker fiel ins Wasser und wurde unter der Yacht durchgezogen.

**Analyse:**
Der Soft-Schäkel (Dyneema SK78, 4mm, geschätzte MBL 2.000 daN) war seit 3 Saisons permanent am Masttop installiert und der UV-Strahlung ausgesetzt. Die Fasern waren vergilbt und spröde.

**Ursache:**
- UV-Degradation der UHMWPE-Fasern (3 Jahre ungeschützt am Masttop)
- Geschätzte MBL nach UV-Degradation: 1.000–1.200 daN (50–60 % Verlust)
- Spi-Fall-Last beim Bergen: ca. 600–800 daN (kurzzeitig höher bei Schlagen)
- Dynamischer Faktor 2,5 → 1.500–2.000 daN → Bruch

**Lehren:**
1. Soft-Schäkel an UV-exponierten Stellen jährlich inspizieren und alle 2 Saisons tauschen
2. UV-Schutz verwenden (Schrumpfschlauch über den Schäkel, wenn permanent installiert)
3. Für permanente Masttop-Installationen: Metall-Fallenschäkel oder UV-stabilisierte Soft-Schäkel (Dyneema SK99 DM20)

**AYDI-Bewertung:** Confidence: documented (Crew-Bericht). Fehlercode: F-09.

### A.4 Fallstudie: Ankerschäkel — Passungsproblem Kettennuss — Hallberg-Rassy 43

**Yacht:** Hallberg-Rassy 43 Mk II, Baujahr 2018, 13,28m
**Revier:** Mittelmeer (Kroatien)
**Vorfall:** Beim Ankereinfahren blockierte der Ankerschäkel in der Kettennuss der Lofrans-Ankerwinsch. Die Winsch stoppte, die Kette konnte nicht weiter eingeholt werden.

**Analyse:**
Der Eigner hatte den originalen Ankerschäkel (verzinkter Stahl, passend zur 10mm-Kette und Lofrans-Kettennuss) durch einen Edelstahl-316L-Bügelschäkel von Sea-Dog ersetzt. Der Sea-Dog-Schäkel hatte einen breiteren Bügel als der Original-Kettenschäkel und passte nicht durch die Kettennuss.

**Ursache:**
- Falscher Schäkeltyp: Standard-Bügelschäkel statt kalibriertem Kettenschäkel
- Die Bügel-Außenbreite des Sea-Dog-Schäkels war 3mm breiter als die Kettennuss-Öffnung
- Keine Vorab-Prüfung der Passung (Schäkel durch Kettennuss laufen lassen)

**Maßnahmen:**
1. Schäkel vor Ort mit Rohrzange gelöst (Kette manuell an Deck geholt)
2. Kalibrierter Kettenschäkel (Lofrans-Original) beschafft und montiert
3. Passung getestet: Schäkel läuft sauber durch die Kettennuss

**Lehre:** Bei Ankerschäkel IMMER die Kompatibilität mit der Kettennuss prüfen. Idealerweise den vom Winschhersteller empfohlenen Schäkel verwenden.

**AYDI-Bewertung:** Confidence: documented (Eigner-Bericht). Fehlercode: F-07 (funktional).

### A.5 Fallstudie: Kaltverschweißung Allen-Key-Bolzen — Swan 48

**Yacht:** Nautor Swan 48, Baujahr 2001, 14,60m
**Revier:** Karibik
**Vorfall:** Bei einer geplanten Rigg-Inspektion konnte der Allen-Key-Bolzen des V1-Oberwant-Schäkels (HR, 12mm, Allen-Key 6mm) nicht gelöst werden. Auch mit verlängertem Inbus-Schlüssel und vorsichtigem Schlagschraubendreher bewegte sich der Bolzen nicht.

**Analyse:**
Der Schäkel war seit 10 Jahren nicht gelöst worden. In der tropischen Umgebung (hohe Temperatur, hohe Luftfeuchtigkeit, Salzluft) hatte sich Galling (Kaltverschweißung) zwischen dem Edelstahl-Bolzen und dem Edelstahl-Bügel gebildet. Zusätzlich waren Salzkorrosionsprodukte im Gewinde.

**Ursache:**
- 10 Jahre ohne Lösen/Schmieren
- Kein Anti-Seize bei der Originalmontage
- Tropisches Klima beschleunigt Korrosionsprozesse

**Maßnahme:**
1. Kriechöl (CRC Marine) mehrmals über 48 Stunden aufgetragen
2. Vorsichtiges Erwärmen des Bügels mit Heißluftföhn (80°C)
3. Bolzen mit Schlagschraubendreher gelöst (nach 3 Versuchen)
4. Gewinde gereinigt, Tef-Gel aufgetragen, Bolzen wieder eingesetzt
5. Alle Rigg-Schäkel am Boot nach gleichem Verfahren behandelt
6. Wartungsintervall: Jährliches Lösen/Reinigen/Schmieren aller Rigg-Schäkel

**AYDI-Bewertung:** Confidence: documented (Rigger-Bericht). Fehlercode: F-05.

### A.6 Fallstudie: Überdimensionierter Schäkel — Dufour 36

**Yacht:** Dufour 36, Baujahr 2019, 10,74m
**Revier:** Côte d'Azur (Frankreich)
**Vorfall:** Der Eigner hatte alle Fallen-Schäkel durch zwei Nummern größere ersetzt „zur Sicherheit". Das Großfall blockierte beim Segelsetzen — der übergroße Fallenschäkel passte nicht mehr durch die Mastnut.

**Analyse:**
Der Eigner hatte Wichard-Fallenschäkel mit 10mm Bolzen (Profil 24mm) montiert, obwohl der Seldén-Mast eine Nutbreite von nur 20mm hatte. Die originalen 6mm-Fallenschäkel (Profil 16mm) waren korrekt dimensioniert.

**Ursache:**
- Fehlannahme: „Größer = sicherer"
- Keine Prüfung der Mastnut-Kompatibilität
- Die 6mm-Schäkel mit MBL 2.000 daN waren für die Falllast (max. 400 daN × 5 = 2.000 daN) vollkommen ausreichend

**Lehre:** Überdimensionierung kann genauso problematisch sein wie Unterdimensionierung. Immer die Kompatibilität mit dem Gesamtsystem prüfen (Mastnut, Blockscheibe, Winsch, etc.).

**AYDI-Bewertung:** Confidence: documented (Eigner-Bericht). Fehlercode: funktional (kein Defekt, sondern Dimensionierungsfehler).

### A.7 Fallstudie: Snap-Schäkel Selbstöffnung — X-Yachts X-35

**Yacht:** X-Yachts X-35, Baujahr 2006, 10,60m
**Revier:** Kieler Bucht (Deutschland)
**Vorfall:** Bei einer Wettfahrt öffnete sich der Snap-Schäkel am Gennaker-Fall selbsttätig. Der Gennaker fiel ins Wasser.

**Analyse:**
Der Snap-Schäkel (Kong Standard, 82mm, MBL 1.800 daN) war korrekt dimensioniert. Der Auslösemechanismus wurde durch ein Klemmen der Gennaker-Schot am Snap-Schäkel-Hebel ausgelöst — die Schot drückte den Trigger beim Gennaker-Schlagen seitlich gegen den Auslösehebel.

**Ursache:**
- Schot-Routing zu nahe am Snap-Schäkel-Trigger
- Keine Schutzabdeckung über dem Trigger
- Seitliche Krafteinwirkung auf den Trigger-Hebel

**Maßnahmen:**
1. Snap-Schäkel mit geschütztem Trigger ersetzt (Wichard Tripping, versenkte Auslösung)
2. Alternativ: Soft-Schäkel für Gennaker-Fall (kein Trigger-Problem)
3. Schot-Routing geändert, um Kontakt mit Trigger zu vermeiden

**AYDI-Bewertung:** Confidence: documented (Crew-Bericht). Fehlercode: F-08 (funktional).

### A.8 Fallstudie: Splint-Versagen Ankerschäkel — Catamaran Lagoon 42

**Yacht:** Lagoon 42, Baujahr 2020, 12,80m
**Revier:** Seychellen
**Vorfall:** Während einer Übernachtung vor Anker bei auffrischendem Wind (20+ kn) verlor die Yacht den Anker. Die Kette war noch intakt, der Anker fehlte.

**Analyse:**
Der Splint des Ankerschäkels (Bolt-Type, 12mm, Edelstahl 316L) war gebrochen. Der Bolzen hatte sich durch die Schwojbewegung über viele Stunden gelockert und war schließlich herausgefallen. Der Anker trennte sich von der Kette.

**Ursache:**
- Der Splint war ein Edelstahl-Splint, der bereits einmal entfernt und wiederverwendet worden war
- Durch das erneute Umbiegen war der Splint an der Biegestelle vorgeschädigt (Ermüdung)
- Die Schwojzyklen (Tide + Wind) über 12 Stunden erzeugten Wechsellasten am Bolzen
- Der vorgeschädigte Splint brach, der Bolzen vibrierte heraus

**Lehren:**
1. Splinte NIEMALS wiederverwenden — immer neue Splinte einsetzen
2. Zusätzliche Sicherung: Seizing Wire als Backup über den Bolzen
3. Bei tropischen Ankernächten: Ankergeschirr morgens inspizieren
4. Ersatz-Splinte (20+ Stück) in der Bordausrüstung mitführen

**AYDI-Bewertung:** Confidence: documented (Versicherungsbericht). Fehlercode: F-12.

---

## ANHANG B — AYDI-Integration (Pydantic-Modelle)

```python
"""
AYDI Shackle Analysis Models — Pydantic v2
Module: shackle_fundamentals
"""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class ShackleType(str, Enum):
    """Types of marine shackles."""
    D_SHACKLE = "d_shackle"
    BOW_SHACKLE = "bow_shackle"
    TWIST_SHACKLE = "twist_shackle"
    HALYARD_SHACKLE = "halyard_shackle"
    SNAP_SHACKLE = "snap_shackle"
    SNAP_SHACKLE_TRIPPING = "snap_shackle_tripping"
    LONG_SHACKLE = "long_shackle"
    WIDE_BODY_SHACKLE = "wide_body_shackle"
    CHAIN_SHACKLE = "chain_shackle"
    ANCHOR_SHACKLE = "anchor_shackle"
    SOFT_SHACKLE = "soft_shackle"


class PinType(str, Enum):
    """Types of shackle pins."""
    SCREW_PIN = "screw_pin"
    BOLT_TYPE = "bolt_type"
    CAPTIVE_PIN = "captive_pin"
    ALLEN_KEY = "allen_key"
    SELF_LOCKING = "self_locking"
    SNAP_MECHANISM = "snap_mechanism"
    DYNEEMA_KNOT = "dyneema_knot"


class ShackleMaterial(str, Enum):
    """Materials for shackles."""
    STAINLESS_316L = "stainless_316l"
    STAINLESS_316L_FORGED = "stainless_316l_forged"
    STAINLESS_316_CAST = "stainless_316_cast"
    DUPLEX_2205 = "duplex_2205"
    TITANIUM_GR5 = "titanium_grade5"
    DYNEEMA_SK78 = "dyneema_sk78"
    DYNEEMA_SK99 = "dyneema_sk99"
    BRONZE = "bronze_cusn8"
    GALVANIZED_STEEL_CL4 = "galvanized_steel_class4"
    GALVANIZED_STEEL_CL6 = "galvanized_steel_class6"
    GALVANIZED_STEEL_CL8 = "galvanized_steel_class8"
    ALUMINUM_7075 = "aluminum_7075"


class ShackleApplication(str, Enum):
    """Applications for shackles on a yacht."""
    SHROUD_UPPER = "shroud_upper"
    SHROUD_LOWER = "shroud_lower"
    FORESTAY = "forestay"
    BACKSTAY = "backstay"
    MAIN_HALYARD = "main_halyard"
    GENOA_HALYARD = "genoa_halyard"
    SPINNAKER_HALYARD = "spinnaker_halyard"
    GENNAKER_HALYARD = "gennaker_halyard"
    MAINSHEET = "mainsheet"
    ANCHOR_CHAIN = "anchor_chain"
    MOORING = "mooring"
    BLOCK_ATTACHMENT = "block_attachment"
    LIFELINE = "lifeline"
    LIFERAFT = "liferaft"
    REEFING = "reefing"
    PREVENTER = "preventer"


class ShackleManufacturer(str, Enum):
    """Major shackle manufacturers."""
    WICHARD = "wichard"
    HR_HARKEN = "hr_harken"
    HARKEN_TITELOK = "harken_titelok"
    BLUE_WAVE = "blue_wave"
    SELDEN = "selden"
    SEA_DOG = "sea_dog"
    KONG = "kong"
    ALLEN_BROTHERS = "allen_brothers"
    TYLASKA = "tylaska"
    KARVER = "karver"
    OTHER = "other"


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


class BoatClass(str, Enum):
    """Boat class categories."""
    DINGHY = "dinghy_4_8m"
    CRUISER = "cruiser_8_14m"
    PERFORMANCE_CRUISER = "performance_cruiser_10_16m"
    BLUEWATER = "bluewater_12_18m"
    RACING = "racing_8_20m"
    MOTORBOAT = "motorboat_8_25m"
    SUPERYACHT = "superyacht_18m_plus"


class FaultCode(str, Enum):
    """Fault codes from the Fehlerbild-Atlas."""
    F01_DEFORMATION = "f01_deformation"
    F02_PIN_WEAR = "f02_pin_wear"
    F03_CREVICE_CORROSION = "f03_crevice_corrosion"
    F04_FATIGUE_CRACK = "f04_fatigue_crack"
    F05_GALLING = "f05_galling"
    F06_TEA_STAINING = "f06_tea_staining"
    F07_WRONG_LOAD_DIRECTION = "f07_wrong_load_direction"
    F08_SPRING_FATIGUE = "f08_spring_fatigue"
    F09_UV_DEGRADATION = "f09_uv_degradation"
    F10_KNOT_SLIPPAGE = "f10_knot_slippage"
    F11_GALVANIC_CORROSION = "f11_galvanic_corrosion"
    F12_MISSING_SECURITY = "f12_missing_security"


class ShackleSpecification(BaseModel):
    """Complete specification of a marine shackle."""

    model_config = {"from_attributes": True}

    shackle_type: ShackleType = Field(..., description="Type of shackle")
    pin_type: PinType = Field(..., description="Type of pin/closure mechanism")
    material: ShackleMaterial = Field(..., description="Shackle body material")
    manufacturer: Optional[ShackleManufacturer] = Field(None, description="Manufacturer")
    article_number: Optional[str] = Field(None, description="Manufacturer article number")
    pin_diameter_mm: float = Field(..., ge=2.0, le=50.0, description="Pin diameter in mm")
    wll_dan: float = Field(..., ge=0, description="Working Load Limit in daN")
    mbl_dan: float = Field(..., ge=0, description="Minimum Breaking Load in daN")
    proof_load_dan: Optional[float] = Field(None, ge=0, description="Proof Load in daN")
    weight_g: Optional[float] = Field(None, ge=0, description="Weight in grams")
    inner_width_mm: Optional[float] = Field(None, ge=0, description="Inner width of bow in mm")
    inner_length_mm: Optional[float] = Field(None, ge=0, description="Inner length of bow in mm")
    overall_length_mm: Optional[float] = Field(None, ge=0, description="Overall length in mm")
    overall_width_mm: Optional[float] = Field(None, ge=0, description="Overall width in mm")
    profile_width_mm: Optional[float] = Field(None, ge=0, description="Profile width for halyard shackles in mm")
    allen_key_size_mm: Optional[float] = Field(None, description="Allen key size for allen key pins")
    price_eur: Optional[float] = Field(None, ge=0, description="Price in EUR")
    forged: bool = Field(False, description="Whether the shackle is forged (True) or cast (False)")
    ce_certified: bool = Field(False, description="Whether CE certified")
    safety_factor: float = Field(4.0, ge=2.0, le=10.0, description="Safety factor (MBL/WLL)")
    confidence: ConfidenceLevel = Field(ConfidenceLevel.MEASURED, description="Data confidence")


class ShackleConditionAssessment(BaseModel):
    """Assessment of a shackle's condition."""

    model_config = {"from_attributes": True}

    shackle_id: str = Field(..., description="Unique identifier for the shackle")
    location: str = Field(..., description="Location on the yacht (e.g. 'V1 upper shroud port')")
    application: ShackleApplication = Field(..., description="Application/position")
    installed_shackle: ShackleSpecification = Field(..., description="Installed shackle specification")
    age_years: Optional[float] = Field(None, ge=0, description="Estimated age in years")
    load_cycles_estimated: Optional[int] = Field(None, ge=0, description="Estimated load cycles")
    deformation_detected: bool = Field(False, description="Whether deformation was detected")
    deformation_mm: Optional[float] = Field(None, ge=0, description="Measured deformation in mm")
    pin_wear_percent: Optional[float] = Field(None, ge=0, le=100, description="Pin wear as percentage of original diameter")
    corrosion_type: Optional[str] = Field(None, description="Type of corrosion if detected")
    corrosion_severity: Optional[str] = Field(None, description="none/light/moderate/severe")
    pin_secured: bool = Field(True, description="Whether pin is properly secured")
    security_method: Optional[str] = Field(None, description="Seizing wire / loctite / split pin / none")
    fault_codes: list[FaultCode] = Field(default_factory=list, description="Detected fault codes")
    overall_condition: str = Field(..., description="good / warning / critical / replace_immediately")
    recommended_action: str = Field(..., description="Recommended action in German")
    next_inspection_months: int = Field(12, ge=1, description="Recommended next inspection in months")
    confidence: ConfidenceLevel = Field(..., description="Assessment confidence level")
    notes: Optional[str] = Field(None, description="Additional notes in German")


class ShackleDimensioningResult(BaseModel):
    """Result of shackle dimensioning calculation."""

    model_config = {"from_attributes": True}

    application: ShackleApplication = Field(..., description="Target application")
    boat_class: BoatClass = Field(..., description="Boat class")
    boat_length_m: float = Field(..., ge=2.0, le=100.0, description="Boat LOA in meters")
    operating_load_dan: float = Field(..., ge=0, description="Maximum operating load in daN")
    operating_load_source: str = Field(..., description="Source: rigging_calc / manufacturer / faustformel")
    dynamic_factor: float = Field(..., ge=1.0, le=5.0, description="Dynamic load factor applied")
    safety_factor: float = Field(..., ge=2.0, le=10.0, description="Safety factor applied")
    required_mbl_dan: float = Field(..., ge=0, description="Required MBL in daN")
    recommended_shackle_type: ShackleType = Field(..., description="Recommended shackle type")
    recommended_pin_type: PinType = Field(..., description="Recommended pin type")
    recommended_material: ShackleMaterial = Field(..., description="Recommended material")
    recommended_pin_diameter_mm: float = Field(..., ge=2.0, description="Recommended pin diameter in mm")
    recommended_products: list[ShackleSpecification] = Field(default_factory=list, description="Recommended products from catalog")
    line_diameter_mm: Optional[float] = Field(None, ge=0, description="Connected line diameter in mm")
    chain_diameter_mm: Optional[float] = Field(None, ge=0, description="Connected chain diameter in mm")
    must_fit_mast_groove: bool = Field(False, description="Must fit through mast groove")
    mast_groove_width_mm: Optional[float] = Field(None, description="Mast groove width in mm")
    must_fit_wildcat: bool = Field(False, description="Must fit through anchor windlass wildcat")
    wildcat_model: Optional[str] = Field(None, description="Windlass/wildcat model")
    confidence: ConfidenceLevel = Field(..., description="Dimensioning confidence level")


class ShackleLoadCalculation(BaseModel):
    """Load calculation for a shackle position."""

    model_config = {"from_attributes": True}

    position: str = Field(..., description="Position description")
    application: ShackleApplication = Field(..., description="Application type")
    static_load_dan: float = Field(..., ge=0, description="Static load in daN")
    static_load_source: str = Field(..., description="Source of static load value")
    dynamic_factor: float = Field(..., ge=1.0, description="Dynamic multiplication factor")
    dynamic_load_dan: float = Field(..., ge=0, description="Dynamic load (static × factor) in daN")
    load_direction: str = Field("axial", description="axial / side / multi")
    direction_efficiency: float = Field(1.0, ge=0.0, le=1.0, description="Load direction efficiency factor")
    effective_load_dan: float = Field(..., ge=0, description="Effective load (dynamic × direction) in daN")
    safety_factor: float = Field(..., ge=2.0, description="Safety factor for this application")
    required_mbl_dan: float = Field(..., ge=0, description="Required MBL (effective × SF) in daN")
    confidence: ConfidenceLevel = Field(..., description="Calculation confidence level")


class ShackleRecommendation(BaseModel):
    """Complete shackle recommendation for a yacht."""

    model_config = {"from_attributes": True}

    boat_class: BoatClass = Field(..., description="Boat class")
    boat_length_m: float = Field(..., ge=2.0, description="LOA in meters")
    boat_model: Optional[str] = Field(None, description="Boat model name")
    positions: list[ShackleDimensioningResult] = Field(default_factory=list, description="Dimensioning results for each position")
    total_shackle_count: int = Field(0, ge=0, description="Total number of shackles recommended")
    total_cost_eur: Optional[float] = Field(None, ge=0, description="Total estimated cost in EUR")
    spare_kit: list[ShackleSpecification] = Field(default_factory=list, description="Recommended spare shackle kit")
    spare_kit_cost_eur: Optional[float] = Field(None, ge=0, description="Spare kit cost in EUR")
    confidence: ConfidenceLevel = Field(..., description="Overall recommendation confidence")
    notes: list[str] = Field(default_factory=list, description="Additional notes in German")


class SoftShackleSpecification(BaseModel):
    """Specification for a Dyneema soft shackle."""

    model_config = {"from_attributes": True}

    material: ShackleMaterial = Field(..., description="UHMWPE material type")
    line_diameter_mm: float = Field(..., ge=1.0, le=20.0, description="Dyneema line diameter in mm")
    mbl_dan: float = Field(..., ge=0, description="Minimum Breaking Load in daN")
    equivalent_metal_pin_mm: float = Field(..., ge=0, description="Equivalent metal shackle pin diameter in mm")
    knot_type: str = Field("diamond_knot", description="Type of stopper knot")
    eye_type: str = Field("brummel_lock", description="Type of eye splice")
    weight_g: float = Field(..., ge=0, description="Weight in grams")
    length_mm: float = Field(..., ge=0, description="Overall length in mm")
    color: Optional[str] = Field(None, description="Color for identification")
    uv_protected: bool = Field(False, description="Whether UV protection is applied")
    max_temperature_c: float = Field(65.0, description="Maximum working temperature in Celsius")
    self_made: bool = Field(False, description="Whether self-made or commercially produced")
    confidence: ConfidenceLevel = Field(..., description="Specification confidence level")


class ShackleVisualAssessment(BaseModel):
    """Visual assessment of a shackle from a photo."""

    model_config = {"from_attributes": True}

    image_id: str = Field(..., description="Reference to the analyzed image")
    detected_shackle_type: Optional[ShackleType] = Field(None, description="Detected shackle type")
    detected_material: Optional[str] = Field(None, description="Detected material (visual estimate)")
    detected_manufacturer: Optional[ShackleManufacturer] = Field(None, description="Detected manufacturer (from markings)")
    estimated_pin_diameter_mm: Optional[float] = Field(None, description="Estimated pin diameter from photo")
    condition_assessment: str = Field(..., description="good / warning / critical / not_assessable")
    detected_faults: list[FaultCode] = Field(default_factory=list, description="Detected fault codes")
    deformation_visible: bool = Field(False, description="Whether deformation is visible")
    corrosion_visible: bool = Field(False, description="Whether corrosion is visible")
    pin_secured_visible: Optional[bool] = Field(None, description="Whether pin security is visible (None if not determinable)")
    photo_quality: str = Field(..., description="good / adequate / poor / insufficient")
    confidence: ConfidenceLevel = Field(..., description="Assessment confidence level")
    findings_de: list[str] = Field(default_factory=list, description="Findings in German")
    recommendations_de: list[str] = Field(default_factory=list, description="Recommendations in German")
```

---

## ANHANG C — Normen und Standards

### C.1 Relevante Normen

| Norm | Titel | Relevanz für Schäkel |
|------|-------|---------------------|
| EN 13889 | Geschmiedete Stahlschäkel — Klasse 6 — Screw/Bolt | WLL/MBL-Bestimmung, Prüfverfahren, Kennzeichnung |
| EN 13889-1 | Geschmiedete Stahlschäkel — Bügel-Schäkel | Spezifisch für Bow Shackles |
| EN 13889-2 | Geschmiedete Stahlschäkel — D-Schäkel | Spezifisch für Dee Shackles |
| ISO 2415 | Geschmiedete Schäkel (international) | Internationale Dimensionsnormen |
| DIN 82101 | Schäkel Form A (D) und B (Bügel) | Deutsche Maßnorm (historisch) |
| EN 12385 | Drahtseile — Sicherheit | Relevanz für Drahtseil-Schäkel |
| ISO 1704 | Ankerketten — Allgemeine Bedingungen | Kettenschäkel-Dimensionierung |
| EN 818-2 | Kurzgliedrige Rundstahlkette | Kettenkompatibilität |
| 2013/53/EU | Recreational Craft Directive | CE-Konformität Gesamtboot |
| 2006/42/EG | Maschinenrichtlinie | CE für Hebezeug-Schäkel |

### C.2 Prüfverfahren nach EN 13889

1. **Proof Load Test:** 2× WLL statisch für 60 Sekunden → keine bleibende Verformung
2. **Breaking Load Test:** Statischer Zug bis Bruch → MBL muss ≥ Nennwert sein
3. **Maßprüfung:** Alle Abmessungen innerhalb Toleranz
4. **Oberflächenprüfung:** Keine Risse, Lunker, scharfen Kanten
5. **Kennzeichnung:** WLL, Herstellerzeichen, Rückverfolgbarkeit, CE (wenn applicable)

### C.3 AYDI-interne Prüfkriterien

| Kriterium | Methode | Confidence |
|-----------|---------|------------|
| MBL/WLL vorhanden | Hersteller-Datenblatt | measured |
| Geschmiedet/gegossen | Visuell + Hersteller | visual_high / documented |
| Verformung | Messschieber (<0,5mm) | measured |
| Verformung | Visuell (>2mm) | visual_high |
| Verformung | Visuell (<2mm) | visual_medium |
| Korrosion (Oberfläche) | Visuell | visual_medium |
| Korrosion (Spalt/Gewinde) | Bolzen lösen + inspizieren | measured |
| Ermüdungsriss | Farbeindringprüfung | measured |
| Ermüdungsriss | Visuell | visual_low (nur grobe Risse) |
| Bolzensicherung | Visuell | visual_high |

---

## ANHANG D — Lasttabellen

### D.1 Typische Rigg-Lasten nach Bootsgröße

| LOA (m) | V1-Want (daN) | D1-Want (daN) | Vorstag (daN) | Backstag (daN) | Großfall (daN) | Genuafall (daN) |
|---------|--------------|--------------|---------------|----------------|----------------|-----------------|
| 8 | 800 | 400 | 1.000 | 600 | 300 | 250 |
| 10 | 1.400 | 700 | 1.800 | 1.000 | 500 | 400 |
| 12 | 2.200 | 1.100 | 2.800 | 1.600 | 700 | 600 |
| 14 | 3.200 | 1.600 | 4.000 | 2.200 | 1.000 | 800 |
| 16 | 4.500 | 2.200 | 5.500 | 3.000 | 1.400 | 1.100 |
| 18 | 6.000 | 3.000 | 7.500 | 4.000 | 1.800 | 1.500 |
| 20 | 8.000 | 4.000 | 10.000 | 5.500 | 2.400 | 2.000 |

**Hinweis:** Werte sind Richtwerte (confidence: estimated) für Fahrtenyachten mit Standard-Rigg. Regattayachten können 20–40 % höhere Lasten aufweisen. Verbindliche Werte nur aus der jeweiligen Rigg-Berechnung (confidence: measured).

### D.2 Empfohlene Schäkel-MBL nach Rigg-Last

Basierend auf Sicherheitsfaktor 4:1 (stehendes Gut) bzw. 5:1 (laufendes Gut):

| LOA (m) | V1-Schäkel MBL (daN) | Vorstag-Schäkel MBL (daN) | Großfall-Schäkel MBL (daN) | Anker-Schäkel MBL (daN) |
|---------|---------------------|--------------------------|---------------------------|------------------------|
| 8 | 3.200 | 4.000 | 1.500 | 3.000 |
| 10 | 5.600 | 7.200 | 2.500 | 5.000 |
| 12 | 8.800 | 11.200 | 3.500 | 8.000 |
| 14 | 12.800 | 16.000 | 5.000 | 12.000 |
| 16 | 18.000 | 22.000 | 7.000 | 16.000 |
| 18 | 24.000 | 30.000 | 9.000 | 20.000 |
| 20 | 32.000 | 40.000 | 12.000 | 28.000 |

### D.3 Ankerketten-Tabelle

| Kettengröße (mm) | MBL Kette (daN) | Empf. Schäkel-MBL (daN) | Empf. Bolzen-Ø (mm) |
|-----------------|-----------------|------------------------|---------------------|
| 6 | 2.000 | 2.400 | 8 |
| 8 | 3.200 | 3.840 | 10 |
| 10 | 5.000 | 6.000 | 12 |
| 12 | 7.200 | 8.640 | 14 |
| 13 | 8.500 | 10.200 | 16 |
| 16 | 12.800 | 15.360 | 19 |

---

## ANHANG E — Confidence-Mapping

### E.1 Confidence-Zuordnung Schäkel-Analyse

| Datenpunkt | Level 1 (Schnellanalyse) | Level 2 (Profi) |
|-----------|-------------------------|-----------------|
| Schäkeltyp | estimated (aus Bootsklasse) | measured (aus Inventar) |
| MBL/WLL | estimated (Standardwerte) | measured (Hersteller-TDS) |
| Material | estimated (Standard 316L) | measured (Gravur/Zertifikat) |
| Zustand | visual_medium (Foto) | measured (Inspektion) |
| Bolzensicherung | visual_high (Foto) | measured (Inspektion) |
| Korrosion | visual_medium (Foto) | measured (Pitting-Tiefe) |
| Ermüdungsriss | visual_low (Foto) | measured (Farbeindringprüfung) |
| Verformung >2mm | visual_high (Foto) | measured (Messschieber) |
| Verformung <2mm | visual_low (Foto) | measured (Messschieber) |
| Galvanische Korrosion | visual_medium (Foto) | measured (Materialanalyse) |
| Lebensdauer-Prognose | estimated | calculated |
| Dimensionierung | estimated (Faustformel) | calculated (Rigg-Berechnung) |

### E.2 Confidence-Fusion Strukturiert + Visuell

Gewichtung für Schäkel-Module gemäß AYDI-Fusionsmatrix:

| Aspekt | Strukturiert (Gewicht) | Visuell (Gewicht) |
|--------|----------------------|-------------------|
| Tragfähigkeit (MBL/WLL) | 1,00 | 0,00 |
| Zustandsbewertung | 0,40 | 0,60 |
| Materialidentifikation | 0,80 | 0,20 |
| Korrosionsbewertung | 0,35 | 0,65 |
| Verformungserkennung | 0,50 | 0,50 |
| Bolzensicherung | 0,30 | 0,70 |
| Dimensionierung | 0,95 | 0,05 |

---

## ANHANG F — Wartungsintervalle

### F.1 Empfohlene Wartungsintervalle

| Anwendung | Sichtinspektion | Vollinspektion (Lösen/Prüfen) | Tausch (präventiv) |
|-----------|----------------|------------------------------|-------------------|
| Rigg-Schäkel (Wanten) | Saisonstart | Jährlich | Alle 10 Jahre |
| Vorstag-Schäkel | Saisonstart | Jährlich | Alle 10 Jahre |
| Fallen-Schäkel | Monatlich (in Saison) | Saisonstart | Alle 5–7 Jahre |
| Spi-Snap-Schäkel | Vor jedem Einsatz | Saisonstart | Alle 3–5 Jahre |
| Ankerschäkel | Vor jeder Ankerung | Jährlich | Alle 5–8 Jahre |
| Mooring-Schäkel | Monatlich | Halbjährlich | Alle 3–5 Jahre |
| Soft-Schäkel (UV-exponiert) | Monatlich | Saisonstart | Alle 2 Saisons |
| Soft-Schäkel (geschützt) | Saisonstart | Jährlich | Alle 3–4 Saisons |

### F.2 Wartungsprotokoll

```
SCHÄKEL-WARTUNGSPROTOKOLL
===========================
Datum: ___________
Boot: ____________
Bearbeiter: ______

Nr. | Position | Typ | Material | Bolzen-Ø | Zustand | Sicherung | Maßnahme
----|----------|-----|----------|----------|---------|-----------|----------
 1  | V1 oben BB | D | 316L | 10mm | gut | Allen+Loctite | Reinigung, Tef-Gel
 2  | V1 oben StB | D | 316L | 10mm | gut | Allen+Loctite | Reinigung, Tef-Gel
 3  | Vorstag oben | D | 316L | 12mm | Korr. | Allen | Tausch empfohlen
 4  | Großfall | Halyard | 316L | 8mm | gut | Captive | Gereinigt
 ...

Bemerkungen: ____________________
Nächste Inspektion: _____________
```

---

## ANHANG G — Historische Entwicklung

### G.1 Zeittafel

| Jahr | Meilenstein |
|------|------------|
| ~3000 v.Chr. | Erste Metallverbinder in der Seefahrt (Bronze) |
| 1800 | Genormte Ankerketten-Schäkel (Royal Navy) |
| 1850 | Erste geschmiedete Stahlschäkel industriell gefertigt |
| 1919 | Gründung Wichard (Thiers, Frankreich) |
| 1950er | Edelstahl-Schäkel (AISI 304) im Yachtbau |
| 1960er | AISI 316 wird Standard für Marine-Anwendungen |
| 1970er | Erste Allen-Key-Bolzen für Rigg-Schäkel |
| 1980er | Wichard Self-Locking-System patentiert |
| 1990er | Harken Titelok-System eingeführt |
| 1990er | Erste Dyneema-Soft-Schäkel im America's Cup |
| 2000er | Duplex-2205-Schäkel von Blue Wave |
| 2005+ | Titan-Schäkel für Superyachten und Regatta |
| 2010er | Soft-Schäkel werden im Fahrten- und Regattasegeln alltäglich |
| 2020er | CNC-gefräste Aluminium-Schäkel für Ultraleicht-Regatta |
| 2025 | Hybridschäkel (Metall-Dyneema-Kombination) in Erprobung |

### G.2 Entwicklungstrends

1. **Gewichtsreduktion:** Soft-Schäkel, Titan, hochfestes Aluminium ersetzen Edelstahl
2. **Werkzeugloser Betrieb:** Self-Locking, Captive-Pin, Titelok ersetzen Screw Pin und Allen-Key
3. **Duplex-Edelstahl:** Höhere Festigkeit bei gleichem Gewicht → kleinere Schäkel
4. **Digitale Rückverfolgbarkeit:** QR-Codes auf Schäkeln für Hersteller-Datenblatt und MBL
5. **Nachhaltigkeit:** Recycelbare Materialien, längere Lebensdauer, weniger Korrosionsschutz-Chemie

---

## ANHANG H — Bezugsquellen

### H.1 Online-Händler (Deutschland/EU)

| Händler | Website | Stärke | Versand DE |
|---------|---------|--------|-----------|
| SVB | svb24.de | Größtes Sortiment, alle Marken | 1–3 Tage |
| Compass24 | compass24.de | Gute Preise, breites Sortiment | 1–3 Tage |
| Toplicht | toplicht.de | Premium-Sortiment, Beratung | 2–4 Tage |
| AWN | awn.de | Großes Sortiment, Filialen | 1–3 Tage |
| Bootszubehör BUSSE | busse-yachtshop.de | Rigg-Spezialist | 2–4 Tage |
| Segelladen | segelladen.de | Regatta-Fokus, Soft-Schäkel | 2–4 Tage |
| West Marine EU | westmarine.eu | US-Marken (Sea-Dog, Harken) | 3–7 Tage |

### H.2 Rigg-Werkstätten (Auswahl)

| Werkstatt | Standort | Spezialität |
|-----------|----------|-------------|
| Z-Spars / Seldén Service | Hamburg, Kiel | Seldén-Rigg, Original-Schäkel |
| Reckmann | Wolfsburg | Rollreffanlagen, Rigg-Beschläge |
| BSI (Bootsbau Schmidt) | Flensburg | Custom-Rigg, Inspektion |
| Alurigger | Stralsund | Aluminium-Rigg, Beschläge |
| Hall Spars EU | Niederlande | Carbon-Rigg, Titan-Schäkel |

---

## ANHANG I — Herstellervergleich Detailtabellen

### I.1 D-Schäkel 8mm Bolzen — Vergleich

| Hersteller | Art.-Nr. | Material | Fertigung | WLL (daN) | MBL (daN) | Gewicht (g) | Preis (EUR) | MBL/€ | MBL/g |
|-----------|----------|----------|-----------|-----------|-----------|-------------|-------------|-------|-------|
| Wichard | 1404 | 316L | Geschmiedet | 1.000 | 5.000 | 52 | 10,90 | 459 | 96 |
| HR (Harken) | HR1308 | 316L | Geschmiedet | 950 | 4.750 | 50 | 12,00 | 396 | 95 |
| Blue Wave | BW-D08-316 | 316L | Geschmiedet | 900 | 4.500 | 52 | 12,90 | 349 | 87 |
| Blue Wave | BW-D08-DX | Duplex | Geschmiedet | 1.400 | 7.000 | 50 | 25,00 | 280 | 140 |
| Kong | 11.080 | 316L | Geschmiedet | 920 | 4.600 | 52 | 11,00 | 418 | 88 |
| Sea-Dog | 147084 | 316 | Gegossen | 680 | 2.720 | 56 | 6,50 | 418 | 49 |
| Allen Brothers | A-088 | 316L | Geschmiedet | 850 | 4.250 | 48 | 8,50 | 500 | 89 |

**Analyse:**
- **Bestes MBL/EUR:** Allen Brothers (500 daN/€) — bester Wert, aber nur bis 8mm erhältlich
- **Bestes MBL/g:** Blue Wave Duplex (140 daN/g) — höchste Leistung pro Gramm
- **Höchste absolute MBL:** Blue Wave Duplex (7.000 daN) — 40–56 % mehr als 316L
- **Budget-Option:** Sea-Dog (6,50 EUR) — aber gegossen, deutlich geringere MBL

### I.2 Snap-Schäkel ~100mm — Vergleich

| Hersteller | Art.-Nr. | MBL (daN) | Länge (mm) | Gewicht (g) | Preis (EUR) | Tripping |
|-----------|----------|-----------|------------|-------------|-------------|----------|
| Wichard | 2673 | 3.000 | 100 | 72 | 36,00 | Nein |
| Wichard | 2683 | 3.500 | 110 | 85 | 48,00 | Ja |
| Kong | 10.074 | 2.800 | 98 | 68 | 32,00 | Nein |
| Kong | 10.084 | 3.500 | 108 | 82 | 42,00 | Ja |

---

## ANHANG J — Schäkelauswahl-Algorithmus

### J.1 Algorithmus-Beschreibung

```python
"""
AYDI Shackle Selection Algorithm — Pseudocode
Input: application, boat_class, boat_length_m, line_diameter_mm, load_source
Output: ShackleRecommendation
"""

def select_shackle(application, boat_class, boat_length_m, line_diameter_mm=None, load_dan=None):
    # Step 1: Determine operating load
    if load_dan is not None:
        operating_load = load_dan  # confidence: measured
    else:
        operating_load = estimate_load(application, boat_class, boat_length_m)  # confidence: estimated

    # Step 2: Apply dynamic factor
    dynamic_factor = get_dynamic_factor(application)
    dynamic_load = operating_load * dynamic_factor

    # Step 3: Apply safety factor
    safety_factor = get_safety_factor(application)
    required_mbl = dynamic_load * safety_factor

    # Step 4: Determine shackle type
    shackle_type = get_recommended_type(application)

    # Step 5: Determine pin type
    pin_type = get_recommended_pin_type(application)

    # Step 6: Determine material
    material = get_recommended_material(application, boat_class)

    # Step 7: Check line/chain compatibility
    if line_diameter_mm:
        min_inner_width = line_diameter_mm * 1.5

    # Step 8: Select from catalog
    candidates = query_catalog(
        shackle_type=shackle_type,
        material=material,
        min_mbl=required_mbl,
        min_inner_width=min_inner_width if line_diameter_mm else None,
    )

    # Step 9: Rank by MBL/weight ratio
    ranked = sorted(candidates, key=lambda s: s.mbl_dan / s.weight_g, reverse=True)

    return ranked[:3]  # Top 3 recommendations
```

### J.2 Entscheidungsmatrix

| Eingabe | Auswahl-Einfluss |
|---------|-----------------|
| Anwendung | → Typ, Bolzentyp, Sicherheitsfaktor |
| Bootsklasse | → Material, Preisniveau |
| Bootslänge | → Lastschätzung, Bolzendurchmesser |
| Leinendurchmesser | → Min. Innenweite |
| Mastnut-Breite | → Max. Profilbreite (Fallenschäkel) |
| Kettengröße | → Kettenschäkel-Kompatibilität |
| Budget | → Hersteller-Auswahl |
| Gewichtsziel | → Material (Titan/Dyneema vs. 316L) |

---

## ANHANG K — Prüfprotokolle

### K.1 Sichtprüfung Schäkel (Level 2)

```
AYDI SICHTPRÜFUNG — SCHÄKEL
==============================
Prüfer: ____________ Datum: ___________
Boot: ______________ Bootsklasse: _____

Position: __________________________
Typ: D / Bow / Twist / Halyard / Snap / Soft / Kette
Hersteller: ________________________
Art.-Nr.: __________________________
Bolzen-Ø: _______ mm  Material: ________
WLL: _______ daN  MBL: _______ daN (lt. Gravur/Katalog)

ZUSTANDSPRÜFUNG:
□ Verformung sichtbar?          □ Ja → Ausmaß: ___mm
□ Risse sichtbar?               □ Ja → Position: ___
□ Korrosion sichtbar?           □ Ja → Typ: ___  Schwere: ___
□ Bolzen drehbar?               □ Ja / □ Nein (festsitzend)
□ Bolzen gesichert?             □ Ja (Methode: ___) / □ Nein
□ Gewinde-Zustand?              □ Gut / □ Schwergängig / □ Beschädigt
□ Galvanische Korrosion?        □ Ja → Kontaktmetall: ___
□ Bolzen-Verschleiß?            □ Ja → Ø-Reduzierung: ___%
□ (Snap) Feder-Funktion?       □ Gut / □ Schwach / □ Defekt
□ (Soft) Faserzustand?         □ Gut / □ Verfärbt / □ Spröde
□ (Soft) Knoten-Integrität?    □ Fest / □ Locker

BEWERTUNG:
□ Gut — Weiterverwendung         □ Nächste Prüfung: __ Monate
□ Warnung — Beobachten           □ Nächste Prüfung: __ Monate
□ Kritisch — Tausch empfohlen   □ Sofort / □ Saisonende
□ Sofort ersetzen                □ Erledigt: Ja / Nein

Bemerkungen: ______________________________
Foto-Nr.: _________________________________
```

### K.2 Rissprüfung (Penetrant Testing) — Kurzanleitung

```
FARBEINDRINGPRÜFUNG (PT) — SCHÄKEL
=====================================

Benötigtes Material:
- Reiniger (z.B. MR 79 von MR Chemie)
- Eindringmittel rot (z.B. MR 68 NF)
- Entwickler weiß (z.B. MR 70)
- Lappen, Handschuhe

Durchführung:
1. Schäkel gründlich reinigen (Reiniger aufsprühen, abwischen)
2. Trocknen lassen (5 min)
3. Eindringmittel rot auftragen (sprühen oder pinseln)
4. Einwirkzeit: 15–30 Minuten
5. Überschuss abwischen (Lappen + Reiniger, NICHT absprühen)
6. Entwickler weiß auftragen (dünne, gleichmäßige Schicht)
7. Warten: 10–30 Minuten → Risse zeigen sich als rote Linien

Interpretation:
- Keine roten Linien → Kein Riss nachgewiesen
- Feine rote Linie → Haarriss → KRITISCH, Schäkel ersetzen
- Breite rote Linie → Fortgeschrittener Riss → SOFORT ersetzen
- Rote Punkte → Pitting-Korrosion → Bewertung je nach Tiefe
```

---

## ANHANG L — Visuelle Analyse-Referenz

### L.1 AYDI Vision-Prompt für Schäkel-Erkennung

```
[AYDI Visual Analysis — Shackle Assessment]

Analyze the provided image for marine shackles. For each shackle detected:

1. IDENTIFY:
   - Shackle type (D/bow/twist/halyard/snap/soft/chain)
   - Approximate pin diameter (mm)
   - Material (stainless steel/galvanized/bronze/dyneema)
   - Manufacturer (if markings visible)

2. ASSESS CONDITION:
   - Deformation: Is the bow visibly bent/deformed?
   - Corrosion: Surface rust, pitting, crevice corrosion visible?
   - Pin security: Is seizing wire/split pin visible? Is pin secured?
   - Load direction: Is the shackle loaded correctly (axial)?
   - Wear: Visible wear marks on pin or bow?

3. RATE:
   - Condition: good / warning / critical / not_assessable
   - Confidence: visual_high / visual_medium / visual_low / visual_insufficient

4. OUTPUT in German:
   - Befund (finding)
   - Empfehlung (recommendation)
   - Begründung (reasoning)

Report "nicht beurteilbar" rather than guess if image quality is insufficient.
```

### L.2 Visuelle Erkennungsmerkmale

| Merkmal | Erkennbar ab Confidence | Beschreibung |
|---------|------------------------|-------------|
| Schäkeltyp | visual_high | D vs. Bow vs. Snap eindeutig an Form erkennbar |
| Größe (Bolzen-Ø) | visual_medium | Nur mit Referenzobjekt im Bild (Hand, Münze, Leine) |
| Material | visual_medium | Edelstahl (glänzend) vs. verzinkt (matt) vs. Bronze (goldbraun) |
| Hersteller | visual_high | Wenn Gravur/Prägung lesbar (Wichard-Logo, HR, etc.) |
| Verformung >2mm | visual_high | Asymmetrie des Bügels erkennbar |
| Verformung <2mm | visual_low | Kaum erkennbar auf Fotos |
| Korrosion (Oberfläche) | visual_medium | Braune Flecken (Tea Staining), Pitting |
| Korrosion (Spalt) | visual_low | Nur bei gelöstem Bolzen erkennbar |
| Bolzensicherung | visual_high | Seizing Wire gut sichtbar / nicht vorhanden |
| Ermüdungsriss | visual_insufficient | Auf Fotos praktisch nicht erkennbar |

---

## ANHANG M — Korrosionsschutz und Pflege

### M.1 Pflegemittel für Schäkel

| Produkt | Einsatz | Anwendung | Preis (ca.) |
|---------|---------|-----------|-------------|
| Tef-Gel | Gewinde, Kontaktflächen | Dünn auftragen vor Montage | 15 EUR/30ml |
| Duralac | Alu-Edelstahl-Kontakt | Auf beide Kontaktflächen | 12 EUR/115ml |
| Lanocote | Allgemeiner Korrosionsschutz | Dünn auftragen | 18 EUR/120ml |
| Boeshield T-9 | Verdränger + Schutzfilm | Aufsprühen, trocknen lassen | 16 EUR/340ml |
| CRC Marine | Kriechöl, Lösen | Aufsprühen, einwirken lassen | 8 EUR/300ml |
| Loctite 243 | Gewindesicherung mittelfest | 1 Tropfen auf Gewinde | 12 EUR/10ml |
| Barkeeper's Friend | Edelstahl-Reinigung | Paste auftragen, polieren | 6 EUR/350g |
| Citronen-Passivierungsgel | Passivierung nach Reinigung | Auftragen, 30 min, abspülen | 25 EUR/250ml |

### M.2 Jährliche Wartungsprozedur

```
JÄHRLICHE SCHÄKEL-WARTUNG
===========================

1. VORBEREITUNG:
   - Alle benötigten Werkzeuge bereitlegen (Inbus-Set, Spleißnadel, Zange)
   - Tef-Gel, Reiniger, Lappen, neue Splinte, Seizing Wire bereitlegen
   - Schäkel-Inventar / Wartungsprotokoll vorbereiten

2. INSPEKTION (jeden Schäkel einzeln):
   a. Bolzen lösen (bei Allen-Key: Inbus; bei Screw: von Hand)
   b. Bolzen entnehmen und inspizieren:
      - Durchmesser messen (Verschleiß?)
      - Gewinde prüfen (Korrosion? Beschädigung?)
      - Oberfläche prüfen (Riefen? Pitting?)
   c. Bügel inspizieren:
      - Innengewinde prüfen (neuen Bolzen probeweise eindrehen)
      - Bügel-Geometrie prüfen (verformt? Symmetrie?)
      - Oberfläche prüfen (Risse? Korrosion?)
   d. Befund dokumentieren (AYDI Level 2)

3. REINIGUNG:
   a. Bolzen und Bügel mit Süßwasser und Bürste reinigen
   b. Gewinde mit Reiniger (CRC Marine) sprühen
   c. Trocknen lassen

4. SCHUTZ:
   a. Tef-Gel auf Bolzen-Gewinde und Bolzen-Schaft
   b. Tef-Gel auf Bügel-Innengewinde
   c. Bei Alu-Kontakt: Duralac auf Kontaktflächen

5. MONTAGE:
   a. Bolzen einsetzen
   b. Anziehen: Handfest + 1/4 Umdrehung (Screw Pin)
      oder Drehmoment lt. Tabelle (Allen-Key)
   c. Sicherung anbringen (Seizing Wire / Splint / Loctite)

6. DOKUMENTATION:
   a. Zustand im Wartungsprotokoll festhalten
   b. Fotos in AYDI Level 2 hochladen
   c. Nächsten Inspektionstermin festlegen
```

---

## ANHANG N — Retrofit-Leitfaden

### N.1 Upgrade-Empfehlungen

| Ausgangssituation | Empfohlenes Upgrade | Begründung | Kosten (typisch) |
|-------------------|--------------------|-----------|--------------------|
| Gegossene Schäkel am Rigg | Geschmiedete (Wichard/HR) | +20–30 % MBL, höhere Zuverlässigkeit | 100–300 EUR |
| Screw Pin am Rigg | Allen-Key (HR) | Sicherer gegen Lösen, glatte Oberfläche | 80–200 EUR |
| Metall-Fallenschäkel | Soft-Schäkel | –80 % Gewicht am Masttop, kein Klappern | 30–80 EUR |
| 316L am Oberwant | Duplex 2205 (Blue Wave) | +55 % WLL bei gleichem Bolzen-Ø | 100–250 EUR |
| Snap-Schäkel am Spi | Soft-Schäkel + Snap-Backup | Leichter, Segel-schonender | 20–50 EUR |
| Kein Anti-Seize | Tef-Gel auf alle Gewinde | Verhindert Galling, Spaltkorrosion | 15 EUR (1 Tube) |

### N.2 Retrofit-Checkliste

```
SCHÄKEL-RETROFIT CHECKLISTE
==============================

□ 1. Bestands-Inventar erstellen (alle Schäkel mit Typ, Größe, Position)
□ 2. Kritische Positionen identifizieren (Rigg, Anker, Sicherheit)
□ 3. Aktuelle MBL vs. erforderliche MBL vergleichen
□ 4. Upgrade-Plan erstellen (Priorität: sicherheitskritisch zuerst)
□ 5. Kompatibilität prüfen:
   □ Passt neuer Schäkel zum Toggle/Gabelkopf?
   □ Passt neuer Fallenschäkel in die Mastnut?
   □ Passt neuer Ankerschäkel durch die Kettennuss?
□ 6. Material bestellen (Ersatzschäkel + Tef-Gel + Splinte)
□ 7. Installation (idealerweise beim Winterlager)
□ 8. Test unter Last (Rigg spannen, Anker einfahren)
□ 9. Dokumentation aktualisieren (AYDI Level 2)
```

---

## ANHANG O — Regatta-Spezifikationen

### O.1 Gewichtsoptimierung

| Maßnahme | Gewichtseinsparung | Kosten | Aufwand |
|----------|-------------------|--------|---------|
| 316L → Titan (Masttop) | 40–45 % | Hoch | Gering |
| 316L → Soft-Schäkel (Fallen) | 80–95 % | Gering | Gering |
| 316L → Alu 7075 (Deck) | 60–65 % | Mittel | Gering |
| Größe reduzieren (SF 3:1 statt 5:1) | 20–30 % | Null | Gering |
| Snap → Soft (Spi-Fall) | 70–85 % | Gering | Gering |

### O.2 Klassenvorschriften (Beispiele)

| Klasse | Relevante Regel | Auswirkung auf Schäkel |
|--------|----------------|----------------------|
| ORC | IMS/ORC Rating berücksichtigt Gewicht | Leichtere Schäkel = besser |
| IRC | Keine spezifische Schäkel-Regel | Freie Wahl |
| ISAF Offshore | Category 0–4 Safety Equipment | Mindest-Sicherungsniveau |
| J/70 One-Design | Strenge Klassenvorschrift | Nur zugelassene Originalschäkel |
| Laser/ILCA | Klassenstrenge Vorschrift | Original-Equipment-Pflicht |
| 420 | Klassenvorschrift | Original-Equipment |

### O.3 Schnellwechsel-Systeme

Für Regatten mit unterschiedlichen Konfigurationen:

- **Titelok-Schäkel (Harken):** Werkzeuglos in Sekunden umschäkeln
- **Soft-Schäkel:** Leicht und schnell wechselbar, kein Werkzeug
- **Captive-Pin-Schäkel:** Schnell, Bolzen bleibt am Schäkel
- **Snap-Schäkel:** Schnellstes System, aber mit Risiken

---

## ANHANG P — Superyacht-Sonderlösungen

### P.1 Schäkel für Superyachten (>18m)

**Besonderheiten:**

| Aspekt | Superyacht-Anforderung | Standard-Yacht |
|--------|----------------------|----------------|
| MBL | 10.000–50.000+ daN | 1.000–10.000 daN |
| Material | 316L geschmiedet, Duplex, Titan | 316L geschmiedet/gegossen |
| Oberfläche | Hochglanzpoliert, matt eloxiert | Standard-Finish |
| Sichtbarkeit | Oft verdeckt (clean deck) | Sichtbar |
| Zertifizierung | Lloyd's/RINA/BV Klasse | Freiwillig |
| Wartung | Professionelle Crew | Eigner |
| Dokumentation | Lückenlose Rückverfolgung | Eigenverantwortung |

**Hersteller für Superyacht-Schäkel:**
- **Wichard Custom:** Sonderanfertigungen in jeder Größe
- **Blue Wave Duplex:** Hochfeste Standardgrößen bis 22mm
- **Tylaska (US):** Titan-Snap-Schäkel und Hochlast-Schäkel
- **Karver (FR):** Carbon/Titan-Hybridlösungen
- **Reckmann:** Rollreffanlagen-integrierte Schäkel

### P.2 Clean-Deck-Konzepte

Auf Superyachten werden Schäkel oft unsichtbar unter Deck oder in Verkleidungen montiert:

- **Unter-Deck-Fallen:** Schäkel und Blöcke unter Deck, Leine durch Deck-Durchführung
- **Versenkte Augplatten:** Schäkel in Deck-Vertiefungen, bündig mit Oberfläche
- **Verkleidete Püttings:** Schäkel hinter Edelstahl-Blenden

**Konsequenz für Schäkel:** Höhere Korrosionsanfälligkeit (weniger Belüftung), schwierigere Inspektion, oft Allen-Key-Bolzen mit Loctite (selten geöffnet).

### P.3 Klassifikationsanforderungen

| Klasse | Anforderung an Schäkel |
|--------|----------------------|
| Lloyd's Register | MBL zertifiziert, Material-Zertifikat 3.1, Proof Load jeder Schäkel |
| RINA | Ähnlich Lloyd's, italienische Norm-Ergänzungen |
| Bureau Veritas | MBL + Ermüdungsnachweis für kritische Verbindungen |
| DNV GL | Strengste Anforderungen, zerstörungsfreie Prüfung alle 5 Jahre |

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

### Q.3 Bolzen-Ø — metrisch vs. imperial

| Metrisch (mm) | Imperial (Zoll) | Nächste Standard-Größe |
|---------------|-----------------|----------------------|
| 4 | 5/32" | 5/32" |
| 5 | 3/16" | 3/16" |
| 6 | 1/4" | 1/4" |
| 8 | 5/16" | 5/16" |
| 10 | 3/8" | 3/8" |
| 12 | 1/2" | 1/2" |
| 14 | 9/16" | 9/16" |
| 16 | 5/8" | 5/8" |
| 19 | 3/4" | 3/4" |
| 22 | 7/8" | 7/8" |
| 25 | 1" | 1" |

### Q.4 WLL/MBL-Schnellrechner

```
MBL = WLL × SF

SF-Faktoren:
  4:1 → MBL = WLL × 4
  5:1 → MBL = WLL × 5
  6:1 → MBL = WLL × 6

Umgekehrt:
  WLL = MBL ÷ SF

Beispiele:
  WLL 500 daN, SF 5:1 → MBL = 2.500 daN
  MBL 10.000 daN, SF 4:1 → WLL = 2.500 daN
  MBL 7.500 daN, SF 5:1 → WLL = 1.500 daN
```

---

## ANHANG R — Checklisten

### R.1 Saisonstart-Checkliste Schäkel

```
SAISONSTART — SCHÄKEL-INSPEKTION
==================================

□ Alle Persennings und Abdeckungen entfernen
□ Sichtkontrolle aller Schäkel an Deck
□ Sichtkontrolle aller Schäkel am Mast (von Deck mit Fernglas)
□ Jeden Schäkelbolzen auf Festsitz prüfen (nicht lösen, nur testen)
□ Alle Seizing Wires vorhanden und intakt?
□ Alle Splinte vorhanden und intakt?
□ Allen-Key-Bolzen: Stichprobenweise mit Inbus prüfen (sitzt fest?)
□ Snap-Schäkel: Federmechanismus testen (öffnet/schließt korrekt?)
□ Soft-Schäkel: Fasern inspizieren (Verfärbung? Abrieb? Steifheit?)
□ Ankerschäkel: Splint prüfen, Bolzen-Festsitz prüfen
□ Galvanische Korrosion an Kontaktpunkten? (weiße/grüne Ablagerungen)
□ Defekte oder verdächtige Schäkel markieren → Tausch planen
□ Inspektionsergebnis dokumentieren (AYDI Level 2)
```

### R.2 Saisonende-Checkliste Schäkel

```
SAISONENDE — SCHÄKEL-KONSERVIERUNG
=====================================

□ Alle Schäkel mit Süßwasser gründlich spülen
□ Rigg-Schäkel: Bolzen lösen, reinigen, Tef-Gel, wieder einsetzen
□ Ankerschäkel: Bolzen lösen, Splint ersetzen, Tef-Gel, Bolzen einsetzen
□ Snap-Schäkel: Mechanismus mit WD-40 spülen, trocknen lassen
□ Soft-Schäkel: Süßwasser spülen, trocknen, UV-geschützt lagern
□ Defekte Schäkel für Winterarbeit beiseitelegen
□ Ersatzschäkel für nächste Saison bestellen
□ Wartungsprotokoll vervollständigen
```

### R.3 Blauwasser-Vorbereitung Checkliste

```
BLAUWASSER-VORBEREITUNG — SCHÄKEL
====================================

□ Alle Rigg-Schäkel auf Alter prüfen (<10 Jahre)
□ Alle Fallen-Schäkel prüfen (<7 Jahre)
□ Ankerschäkel prüfen und ggf. ersetzen
□ Vollinspektion aller Schäkel (Lösen, Reinigen, Prüfen, Schmieren)
□ Farbeindringprüfung kritischer Schäkel (Rigg-Top, Vorstag)
□ Ersatzschäkel beschaffen:
   □ 4× D-Schäkel (2× Rigg-Größe, 2× eine Größe kleiner)
   □ 2× Bügelschäkel (Ankergröße)
   □ 2× Fallenschäkel
   □ 2× Snap-Schäkel (Spi-Größe)
   □ 4× Soft-Schäkel (verschiedene Größen)
□ Verbrauchsmaterial:
   □ 10–20× Splinte (passend)
   □ 1 Rolle Seizing Wire (Monel 0,8mm)
   □ 2× Tef-Gel (Tube)
   □ 1× Loctite 243
   □ 1× CRC Marine (Kriechöl)
□ Werkzeug:
   □ Inbus-Schlüssel-Set (3–6mm, Edelstahl!)
   □ Seitenschneider für Seizing Wire
   □ Spitzzange für Splinte
   □ Messschieber (für Bolzen-Verschleißmessung)
□ Alle Schäkel fotografieren und katalogisieren (AYDI Level 2)
□ Hersteller-Kontaktdaten für Ersatzteile weltweit notieren
```

### R.4 Notfall-Checkliste Schäkel-Versagen auf See

```
NOTFALL — SCHÄKEL VERSAGT AUF SEE
====================================

SOFORT:
□ Last von der betroffenen Anlage nehmen (Segel bergen/fieren)
□ Betroffene Leine/Draht sichern (Klampe, Winsch, Knoten)
□ Crew warnen — Peitschengefahr durch lose Drähte/Leinen!
□ Ggf. Mast sichern (wenn Rigg-Schäkel betroffen)

ASSESSMENT:
□ Welcher Schäkel ist betroffen?
□ Welche Funktion hat er? (Rigg → KRITISCH, Fall → HOCH, Trimm → MITTEL)
□ Ist eine temporäre Reparatur möglich?
□ Gibt es einen Ersatzschäkel an Bord?

TEMPORÄRE LÖSUNG:
□ Ersatzschäkel einsetzen (identische oder nächstgrößere Größe)
□ Soft-Schäkel als Ersatz verwenden (Dyneema-Schlaufe)
□ Palstek oder Schotstek als temporäre Verbindung
□ Bei Rigg-Versagen: Notzurring mit Dyneema-Leine und Kauschen
□ Segelfläche reduzieren (Reffen), um Last auf verbleibende Schäkel zu senken

DOKUMENTATION:
□ Fotos vom versagten Schäkel (für AYDI-Analyse und Versicherung)
□ Ursache notieren (sofern erkennbar)
□ Maßnahme dokumentieren
□ Permanente Reparatur im nächsten Hafen planen
```

### R.5 Ankermanöver-Checkliste (Schäkel-relevant)

```
ANKERMANÖVER — SCHÄKEL-CHECK
===============================

VOR DEM ANKERN:
□ Ankerschäkel auf Festsitz prüfen (Bolzen + Splint)
□ Ankerwirbel (falls vorhanden) auf Leichtgängigkeit prüfen
□ Kettenstopper-Schäkel prüfen
□ Vorleine-Schäkel prüfen (falls Kettenvorläufer)

NACH DEM ANKERN:
□ Kettenstopper einlegen (Last nicht nur auf Winsch!)
□ Schäkel-Position relativ zur Winsch prüfen (nicht in Kettennuss?)
□ Ankerlicht setzen

ANKER EINFAHREN:
□ Kette langsam einfahren
□ Schäkel durch Kettennuss beobachten (blockiert?)
□ Ankerschäkel an Deck: Sichtkontrolle

NACH JEDER ANKERNACHT >20 KN WIND:
□ Ankerschäkel visuell prüfen
□ Splint prüfen (noch intakt?)
□ Kette auf Verdrehung prüfen
```

---

---

## ANHANG S — Erweiterte Materialverträglichkeitsmatrix

### S.1 Galvanische Spannungsreihe maritimer Werkstoffe

Die folgende Tabelle zeigt das galvanische Potenzial in belüftetem Meerwasser (Referenz: gesättigte Kalomelelektrode, SCE).

| Werkstoff | Potenzial (mV vs. SCE) | Gruppe |
|-----------|------------------------|--------|
| Titan Gr.5 | -50 bis +50 | Edel |
| Hastelloy C | -60 bis +10 | Edel |
| Edelstahl 316L (passiv) | -100 bis +50 | Edel |
| Duplex 2205 (passiv) | -80 bis +20 | Edel |
| Bronze CuSn8 | -280 bis -230 | Mittel-edel |
| Kupfer | -300 bis -250 | Mittel-edel |
| Messing | -350 bis -280 | Mittel-edel |
| Edelstahl 316L (aktiv/Spalt) | -400 bis -200 | Mittel |
| Blei | -500 bis -400 | Mittel-unedel |
| Gusseisen | -600 bis -500 | Unedel |
| Baustahl (unlegiert) | -650 bis -550 | Unedel |
| Aluminium 5083 | -750 bis -650 | Unedel |
| Aluminium 7075 | -800 bis -700 | Unedel |
| Zink (Opferanode) | -1030 bis -980 | Sehr unedel |
| Magnesium (Opferanode) | -1600 bis -1500 | Extrem unedel |

### S.2 Verträglichkeitsregeln für Schäkelkombinationen

**Regel 1 — Maximale Potentialdifferenz:**
Zwei Materialien in direktem Kontakt dürfen max. 200 mV Potentialdifferenz aufweisen. Bei >200 mV: Isolation oder Opferanode erforderlich.

**Regel 2 — Flächenverhältnis:**
Kleine Anode + große Kathode = schnelle Korrosion des Anodenmaterials.
- SCHLECHT: Aluminium-Schäkel an Edelstahlkette (kleines Al, großes V4A)
- GUT: Edelstahl-Schäkel an Aluminium-Mast (kleiner V4A, großes Al — aber Isolation trotzdem empfohlen)

**Regel 3 — Kontaktflächen-Isolation:**
| Kombination | Zulässig? | Maßnahme |
|-------------|-----------|----------|
| 316L Schäkel + 316L Kette | Ja | Keine |
| 316L Schäkel + verzinkte Kette | Bedingt | Opferanode nahe Kontaktstelle |
| 316L Schäkel + Alu-Mast | Bedingt | TefGel oder Duralac zwischen Kontaktflächen |
| Titan Schäkel + 316L Terminal | Ja | Keine (Differenz <150 mV) |
| Titan Schäkel + Alu-Mast | Nein | Zwischenstück aus 316L oder Isolation |
| Bronze Schäkel + 316L Kette | Ja | Keine (Differenz <200 mV) |
| Duplex Schäkel + 316L Wire | Ja | Keine |
| Alu-Schäkel + Cu-Kabel | Nein | Bimetallklemme verwenden |

### S.3 Korrosionsrisiko-Bewertung nach Einsatzzone

| Zone | Salzwasser-Exposition | Belüftung | Spaltkorrosions-Risiko | Empfohlenes Material |
|------|----------------------|-----------|----------------------|---------------------|
| Unterwasser (Anker) | Permanent | Gering | Hoch | 316L geschmiedet, Duplex 2205 |
| Wasserlinie (Bugbeschlag) | Wechselnd | Mittel | Sehr hoch | Duplex 2205, Titan |
| Deck (Beschläge) | Spritzwasser | Gut | Mittel | 316L geschmiedet |
| Mast (Riggbeschläge) | Aerosol | Gut | Gering | 316L, Titan, Dyneema |
| Mastspitze (Toppbeschläge) | Aerosol | Sehr gut | Gering | 316L, Titan |
| Innenraum (Stauklappe) | Minimal | Gut | Sehr gering | 316L, Bronze |

---

## ANHANG T — Erweiterte Inspektionskriterien

### T.1 Quantitative Verschleißmessung

Schäkel müssen bei Überschreitung folgender Grenzwerte ausgetauscht werden:

**Bügel-Durchmesser:**
| Nennmaß | Max. zulässige Reduzierung | Messmethode |
|---------|---------------------------|-------------|
| ≤5mm | 0,3mm (6%) | Messschieber |
| 6–8mm | 0,5mm (6–8%) | Messschieber |
| 10–12mm | 0,8mm (6,5–8%) | Messschieber |
| 14–16mm | 1,0mm (6–7%) | Messschieber |
| ≥18mm | 1,2mm (≤6,5%) | Messschieber + Bügelmessschraube |

**Bolzen-Durchmesser:**
| Nennmaß | Max. zulässige Reduzierung | Messmethode |
|---------|---------------------------|-------------|
| ≤5mm | 0,2mm (4%) | Bügelmessschraube |
| 6–8mm | 0,3mm (4–5%) | Bügelmessschraube |
| 10–12mm | 0,5mm (4–5%) | Bügelmessschraube |
| 14–16mm | 0,7mm (4–5%) | Bügelmessschraube |
| ≥18mm | 0,9mm (≤5%) | Bügelmessschraube |

**Bügel-Aufweitung (Lichte Weite):**
| Nennmaß Innenweite | Max. zulässige Aufweitung | Bewertung |
|--------------------|--------------------------|-----------|
| Alle Größen | +5% | OK |
| Alle Größen | +5–10% | Warnung — erhöhte Überwachung |
| Alle Größen | >10% | Austausch sofort |

### T.2 Inspektionshäufigkeit nach Einsatzprofil

| Einsatzprofil | Sichtprüfung | Messtechnische Prüfung | Komplett-Austausch |
|---------------|-------------|----------------------|-------------------|
| Regatta (intensiv) | Nach jeder Regatta | Alle 6 Monate | Alle 2–3 Jahre |
| Performance Cruising | Monatlich | Jährlich | Alle 3–5 Jahre |
| Fahrtenyacht (aktiv) | Alle 3 Monate | Jährlich | Alle 5–7 Jahre |
| Wochenend-Segler | Saisonstart + -ende | Alle 2 Jahre | Alle 7–10 Jahre |
| Liegeplatz (selten bewegt) | Saisonstart | Alle 2 Jahre | Alle 10 Jahre |
| Charter | Wöchentlich | Halbjährlich | Alle 3 Jahre |
| Blauwasser | Wöchentlich auf See | Alle 6 Monate | Alle 3–4 Jahre |

### T.3 Soft-Schäkel-spezifische Inspektionskriterien

| Kriterium | OK | Warnung | Austausch |
|-----------|-----|---------|----------|
| Farbveränderung | Keine | Leichte Vergilbung | Starke Verfärbung, spröde Fasern |
| Fasern | Geschlossen, glatt | Einzelne Fuzzing-Fasern | Faserbrüche sichtbar |
| Knoten (Diamond) | Fest, symmetrisch | Leicht asymmetrisch | Locker, Schlupf erkennbar |
| Auge (Brummel Lock) | Glatt, rund | Leichte Abflachung | Einschnürung, Faserbruch |
| Durchmesser | Nennmaß ±5% | -5 bis -10% (Kompression) | >-10% Durchmesserreduzierung |
| Scheuerung | Keine | Oberflächlich (<10% Tiefe) | >10% Querschnittsverlust |
| UV-Degradation | Keine Veränderung | Oberfläche leicht rau | Fasern spröde, Bruch bei Biegung |

---

## ANHANG U — Lastberechnung Detailformeln

### U.1 Rigg-Lasten-Berechnung

**Wantlast Überschlagsrechnung (Segelboot):**

```
Krängungsmoment M_k = Displacement [kg] × Stability_Arm [m] × g [m/s²]

Wantkraft_gesamt = M_k / (Hebelarm_Wanten × cos(Wantwinkel))

Wantkraft_oberwant = Wantkraft_gesamt × 0,60  (bei 2 Saling-Rigg)
Wantkraft_unterwant = Wantkraft_gesamt × 0,40

Dynamik-Faktor:
  - Geschütztes Revier (Kat C/D): 1,5
  - Küstenfahrt (Kat B): 2,0
  - Ozean (Kat A): 2,5–3,0
  - Regatta (Böen, harte Manöver): 3,0–4,0

Erforderliche MBL_Schäkel = Wantkraft × Dynamik-Faktor × Sicherheitsfaktor_Schäkel
  - Sicherheitsfaktor_Schäkel: 2,0 (Standard), 2,5 (Blauwasser), 3,0 (Charter)
```

**Beispielrechnung Bavaria 40 Cruiser:**
```
Displacement: 8.500 kg
Stability Arm (bei 25° Krängung): 0,85 m
Hebelarm Wanten: 3,2 m (Abstand Mast–Püttingeisen)
Wantwinkel: 12° (zum Mast)

M_k = 8.500 × 0,85 × 9,81 = 70.886 Nm
Wantkraft_gesamt = 70.886 / (3,2 × cos(12°)) = 22.648 N ≈ 2.265 daN
Oberwant: 2.265 × 0,60 = 1.359 daN
Unterwant: 2.265 × 0,40 = 906 daN

Dynamik (Kat B, Küste): × 2,0
Oberwant dynamisch: 2.718 daN

SF Schäkel: 2,0
Erforderliche MBL Oberwant-Schäkel: 5.436 daN

→ Wichard D-Schäkel 8mm Bolzen (MBL 7.500 daN) ✓
→ Wichard D-Schäkel 6mm Bolzen (MBL 4.000 daN) ✗ zu schwach
```

> ⚠️ **ZU PRÜFEN (Audit):** 8mm-Bolzen MBL 7.500 daN vs. Katalog §5.1.1/§6.2: Wichard 8mm (Art. 1404) = MBL 5.000 daN — 7.500 daN gilt dort für den 10mm-Schäkel (Art. 1405). Ebenso 6mm-Bolzen MBL 4.000 daN vs. Katalog: Wichard 6mm (Art. 1403) = MBL 2.500 daN. Sicherheitskritisch: Mit dem Katalogwert 5.000 daN läge der 8mm-Schäkel UNTER der geforderten MBL von 5.436 daN (→ NICHT ausreichend, 10mm erforderlich). Ob im Beispiel die Bolzengröße (→ 10mm) oder der MBL-Wert (→ 5.000 daN) falsch ist, ist nicht zweifelsfrei entscheidbar. Diese MBL-Beispielwerte sind daher **estimated — unverifiziert** (nicht „measured"); vor Verwendung mit Hersteller-TDS gegenprüfen.

### U.2 Fall-Lasten Berechnung

```
Großfall-Last = Segelfläche [m²] × Winddruck [N/m²] × Segelschwerpunkt-Faktor

Winddruck (Beaufort-Näherung):
  Bft 4: ~  50 N/m²
  Bft 5: ~  90 N/m²
  Bft 6: ~ 150 N/m²
  Bft 7: ~ 230 N/m²
  Bft 8: ~ 340 N/m²

Segelschwerpunkt-Faktor:
  Bermudasegel: 0,33 (Schwerpunkt bei 1/3 Masthöhe)
  Genua: 0,45

Dynamik-Faktor Fall: 2,5–3,5 (Böen, Reffmanöver, Patenthalse)

Beispiel: Großsegel 38 m², Bft 6, Mastlänge 16m:
  Last = 38 × 150 × 0,33 = 1.881 N
  Dynamisch: 1.881 × 3,0 = 5.643 N ≈ 564 daN
  MBL Fallenschäkel: 564 × 2,5 = 1.410 daN
  → Wichard Fallenschäkel 5mm (MBL 2.000 daN) ✓
```

> ⚠️ **ZU PRÜFEN (Audit):** 5mm-Fallenschäkel MBL 2.000 daN vs. Katalog §3.4/§5.1.6: Wichard 5mm (Art. 1491) = MBL 1.250 daN — 2.000 daN gilt dort für den 6mm-Fallenschäkel (Art. 1492). Sicherheitskritisch: Mit dem Katalogwert 1.250 daN läge der 5mm-Schäkel UNTER der geforderten MBL von 1.410 daN (→ NICHT ausreichend, 6mm erforderlich). Ob im Beispiel die Bolzengröße (→ 6mm) oder der MBL-Wert (→ 1.250 daN) falsch ist, ist nicht zweifelsfrei entscheidbar. Dieser MBL-Beispielwert ist daher **estimated — unverifiziert** (nicht „measured"); vor Verwendung mit Hersteller-TDS gegenprüfen.

### U.3 Ankerschäkel-Lasten

```
Ankerlast = Haltkraft_Anker + Kettenlast_Freihängendes_Stück

Haltkraft_Anker (typisch, guter Grund):
  10 kg Anker: ~ 300 daN
  15 kg Anker: ~ 500 daN
  20 kg Anker: ~ 700 daN
  30 kg Anker: ~1.100 daN

Kettenlast pro Meter 10mm DIN766: 2,2 kg/m = 0,22 daN/m

Dynamik-Faktor Ankerlieger:
  Ruhig (< 15 kn): 2,0
  Mäßig (15–25 kn): 3,0
  Schwer (25–35 kn): 5,0
  Sturm (>35 kn): 8,0–10,0

Beispiel: 20 kg Anker, 40m Kette 10mm, 30 kn Wind:
  Haltkraft: 700 daN
  Kettenlast (10m freihängend): 10 × 0,22 = 2,2 daN
  Gesamt statisch: 702 daN
  Dynamisch (Faktor 5,0): 3.512 daN
  Erforderliche MBL Ankerschäkel: 3.512 × 2,0 = 7.024 daN
  → Stahl-Ankerschäkel 12mm (MBL 12.000 daN) ✓
```

---

## ANHANG V — Typische Fehler bei der Schäkelauswahl

### V.1 Die 15 häufigsten Fehler

| Nr. | Fehler | Konsequenz | Korrekte Vorgehensweise |
|-----|--------|------------|------------------------|
| 1 | Gegossener statt geschmiedeter Schäkel im Rigg | Bruchgefahr bei dynamischer Last | Nur geschmiedete Schäkel für Rigg und sicherheitsrelevante Anwendungen |
| 2 | WLL mit MBL verwechselt | Überlastung (Faktor 4–6 zu wenig Reserve) | Immer MBL als Basis der Berechnung verwenden |
| 3 | Keine Sicherung des Schraubbolzens | Selbstöffnung durch Vibration | Draht, Kabelbinder oder Loctite je nach Anwendung |
| 4 | Falsches Material (304 statt 316L) | Korrosion in Salzwasser | Nur 316L, Duplex oder Titan für Salzwasser |
| 5 | Schäkel in falscher Ebene belastet | Aufbiegen, Bruch | Belastung immer in der Schäkelebene |
| 6 | Zwei Schäkel ineinander gehängt | Punktlast, Aufbiegen | Immer über Auge, Kausch oder Ring verbinden |
| 7 | Zu großer Schäkel für die Anwendung | Verhaken, Blockieren, Gewicht | Schäkelgröße an Leinendurchmesser/Last anpassen |
| 8 | Zu kleiner Schäkel (grenzwertig dimensioniert) | Keine Sicherheitsreserve | Mindestens SF 2,0 gegenüber Betriebslast |
| 9 | Snap-Schäkel an hochbelasteten Fallen | Selbstöffnung unter Last | Schraubschäkel oder Captive-Pin für Hauptfälle |
| 10 | Soft-Schäkel auf scharfen Kanten | Durscheuern, Bruch | Kausch oder Rundung an Kontaktstellen |
| 11 | Verzinkter Stahlschäkel an Edelstahlkette | Galvanische Korrosion (Zink löst sich) | Gleiche Materialfamilie oder Isolation |
| 12 | Allen-Key-Schäkel zu fest angezogen | Kaltverschweißung (Galling) | Maximales Drehmoment beachten, Anti-Seize verwenden |
| 13 | Bolzen nicht vollständig eingeschraubt | Geringere WLL, Rissansatz | Bolzen bis Anschlag einschrauben, dann sichern |
| 14 | Gebrauchte Schäkel ohne Prüfung wiederverwendet | Unbekannter Zustand | Sichtprüfung + Maßkontrolle vor Wiederverwendung |
| 15 | Schäkel im Geschäft nach Optik ausgewählt | Falsche WLL/Typ für Anwendung | Immer nach Last und Anwendung auswählen, WLL prüfen |

### V.2 Kostenvergleich: Richtiger vs. falscher Schäkel

| Szenario | Kosten richtiger Schäkel | Kosten falscher Schäkel (Folgeschaden) |
|----------|-------------------------|---------------------------------------|
| Rigg-Schäkel Want | 35–80 EUR | Mastfall: 15.000–80.000 EUR |
| Ankerschäkel | 15–40 EUR | Ankerverlust + Strandung: 5.000–50.000 EUR |
| Großfall-Schäkel | 25–60 EUR | Baum auf Crew: Personenschaden + Haftung |
| Rettungsinsel-Schäkel | 15–30 EUR | Insel nicht auslösbar: Lebensgefahr |
| Spi-Snap-Schäkel | 40–120 EUR | Spinnaker im Wasser: 500–3.000 EUR Segel |

---

## ANHANG W — Saisonale Wartungsprotokolle (Detailliert)

### W.1 Frühjahrs-Inspektion (Detailprotokoll)

```
SCHÄKEL-INSPEKTION — FRÜHJAHRSFITTING
Yacht: _________________ Datum: ___________
Prüfer: _________________ Wetter: ___________

RIGG — OBERWANT STEUERBORD
Position: Want-Auge → Püttingeisen
□ Schäkeltyp: _______ Hersteller: _______ Größe: _______
□ Bolzentyp: _______ Sicherung: _______
□ Sichtprüfung Bügel: □ OK □ Verschleiß □ Riss □ Verformung
□ Sichtprüfung Bolzen: □ OK □ Verschleiß □ Korrosion □ Fest
□ Messung Bügel-Ø: _____ mm (Soll: _____ mm, Grenze: _____ mm)
□ Messung Bolzen-Ø: _____ mm (Soll: _____ mm, Grenze: _____ mm)
□ Messung Lichte Weite: _____ mm (Soll: _____ mm, Grenze: _____ mm)
□ Korrosion: □ Keine □ Tea Staining □ Spalt □ Loch □ Galvanisch
□ Bolzen öffnen + schließen: □ Leichtgängig □ Schwer □ Fest
□ Gewinde-Zustand: □ OK □ Beschädigt □ Verschlissen
□ Sicherungsmittel erneuert: □ Ja □ Nein □ N/A
□ Bewertung: □ GUT □ WARNUNG □ AUSTAUSCH
□ Maßnahme: _______________________________________

RIGG — OBERWANT BACKBORD
[identische Felder]

RIGG — UNTERWANT STEUERBORD
[identische Felder]

RIGG — UNTERWANT BACKBORD
[identische Felder]

RIGG — VORSTAG
[identische Felder]
Zusatz: □ Furler-Lager geprüft □ Kopfschäkel geprüft

RIGG — ACHTERSTAG
[identische Felder]
Zusatz: □ Spanner geprüft □ Hydraulikzylinder geprüft

FALLEN
□ Großfall-Schäkel: □ OK □ WARNUNG □ AUSTAUSCH
□ Vorstags-/Genuafall-Schäkel: □ OK □ WARNUNG □ AUSTAUSCH
□ Spi-/Gennaker-Fall-Schäkel: □ OK □ WARNUNG □ AUSTAUSCH
□ Topping-Lift-Schäkel: □ OK □ WARNUNG □ AUSTAUSCH

ANKERGESCHIRR
□ Ankerschäkel Kette→Anker: □ OK □ WARNUNG □ AUSTAUSCH
□ Splint-Zustand: □ Intakt □ Fehlt □ Ersetzt
□ Verbindungsschäkel Kette→Leine: □ OK □ WARNUNG □ AUSTAUSCH
□ Kettenstopper-Schäkel: □ OK □ WARNUNG □ AUSTAUSCH

SICHERHEITSAUSRÜSTUNG
□ Rettungsinsel-Auslöseschäkel: □ OK □ WARNUNG □ AUSTAUSCH
□ Reling-Befestigungsschäkel: □ OK □ WARNUNG □ AUSTAUSCH

GESAMTBEWERTUNG
□ Alle Schäkel OK — Saison freigegeben
□ Folgende Schäkel austauschen: _______________________________
□ Folgende Schäkel beobachten: _______________________________

Unterschrift: _________________ Datum: ___________
```

### W.2 Herbst-Konservierung (Detailprotokoll)

```
SCHÄKEL-KONSERVIERUNG — WINTERLAGER
Yacht: _________________ Datum: ___________

REINIGUNG (alle Schäkel)
□ Salzwasser abspülen (Süßwasser, lauwarm)
□ Schäkel trocknen lassen (nicht mit Druckluft!)
□ Bolzen aus Gewinde herausdrehen (falls über 6 Monate eingebaut)
□ Gewinde mit Süßwasser + Bürste reinigen
□ Gewinde trocknen

KONSERVIERUNG
□ Gewinde mit Tef-Gel oder Lanolin behandeln
□ Bolzen leicht einschrauben (nicht festziehen — Winterbelüftung)
□ Snap-Schäkel-Federn entlasten (Schäkel offen lagern)
□ Soft-Schäkel dunkel lagern (UV-Schutz)
□ Reserveschäkel in trockenem Beutel mit Silica-Gel lagern

DOKUMENTATION
□ Alle Maße im Schäkel-Logbuch notiert
□ Fotos aller sicherheitsrelevanten Schäkel gemacht
□ Fällige Austauschtermine im Kalender eingetragen
□ Bestellliste für Frühjahrsfitting erstellt
```

---

## ANHANG X — Erweiterte Pydantic-Modelle (AYDI v2)

```python
"""
AYDI Shackle Analysis — Extended Models — Pydantic v2
Module: shackle_fundamentals_extended
"""

from __future__ import annotations

from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class InspectionResult(str, Enum):
    """Results of a shackle inspection."""
    OK = "ok"
    WARNING = "warning"
    REPLACE = "replace"
    NOT_ASSESSABLE = "not_assessable"


class CorrosionType(str, Enum):
    """Types of corrosion found on shackles."""
    NONE = "none"
    TEA_STAINING = "tea_staining"
    CREVICE = "crevice"
    PITTING = "pitting"
    GALVANIC = "galvanic"
    STRESS_CORROSION = "stress_corrosion"
    INTERGRANULAR = "intergranular"


class WearLocation(str, Enum):
    """Locations of wear on a shackle."""
    BOW = "bow"
    PIN = "pin"
    PIN_HOLE = "pin_hole"
    THREAD = "thread"
    SHOULDER = "shoulder"
    CROWN = "crown"


class ShackleInspectionRecord(BaseModel):
    """Record of a single shackle inspection."""

    model_config = {"from_attributes": True}

    yacht_id: str = Field(..., description="AYDI yacht identifier")
    position: str = Field(..., description="Position on yacht (e.g., 'oberwant_steuerbord')")
    inspection_date: date = Field(..., description="Date of inspection")
    inspector: Optional[str] = Field(None, description="Name of inspector")
    shackle_type: str = Field(..., description="Type of shackle")
    manufacturer: Optional[str] = Field(None, description="Manufacturer")
    nominal_pin_diameter_mm: float = Field(..., ge=1.0, description="Nominal pin diameter in mm")
    measured_pin_diameter_mm: Optional[float] = Field(None, ge=0, description="Measured pin diameter in mm")
    nominal_bow_diameter_mm: float = Field(..., ge=1.0, description="Nominal bow wire diameter in mm")
    measured_bow_diameter_mm: Optional[float] = Field(None, ge=0, description="Measured bow wire diameter in mm")
    nominal_inner_width_mm: float = Field(..., ge=1.0, description="Nominal inner width in mm")
    measured_inner_width_mm: Optional[float] = Field(None, ge=0, description="Measured inner width in mm")
    corrosion_type: CorrosionType = Field(CorrosionType.NONE, description="Type of corrosion found")
    wear_locations: list[WearLocation] = Field(default_factory=list, description="Locations with wear")
    pin_security_intact: bool = Field(True, description="Whether pin security (wire/tape/loctite) is intact")
    result: InspectionResult = Field(..., description="Overall inspection result")
    photo_ids: list[str] = Field(default_factory=list, description="References to inspection photos")
    notes_de: str = Field("", description="Inspector notes in German")
    confidence: str = Field("measured", description="Confidence level of inspection")


class ShackleLifecycleRecord(BaseModel):
    """Lifecycle tracking for a shackle."""

    model_config = {"from_attributes": True}

    shackle_id: str = Field(..., description="Unique shackle identifier (etched/tagged)")
    yacht_id: str = Field(..., description="AYDI yacht identifier")
    position: str = Field(..., description="Current position on yacht")
    install_date: date = Field(..., description="Installation date")
    manufacturer: str = Field(..., description="Manufacturer")
    model: str = Field(..., description="Model designation")
    material: str = Field(..., description="Material code")
    nominal_mbl_dan: float = Field(..., ge=0, description="Nominal MBL in daN")
    purchase_price_eur: Optional[float] = Field(None, ge=0, description="Purchase price in EUR")
    inspections: list[ShackleInspectionRecord] = Field(default_factory=list, description="Inspection history")
    estimated_remaining_life_years: Optional[float] = Field(None, ge=0, description="Estimated remaining service life")
    replacement_due_date: Optional[date] = Field(None, description="Recommended replacement date")
    is_active: bool = Field(True, description="Whether shackle is currently in service")
    retirement_reason: Optional[str] = Field(None, description="Reason for retirement")
    confidence: str = Field("measured", description="Confidence level")


class GalvanicCompatibility(BaseModel):
    """Galvanic compatibility assessment between two materials."""

    model_config = {"from_attributes": True}

    material_a: str = Field(..., description="First material (shackle)")
    material_b: str = Field(..., description="Second material (connected component)")
    potential_diff_mv: float = Field(..., description="Galvanic potential difference in mV")
    compatible: bool = Field(..., description="Whether combination is acceptable")
    risk_level: str = Field(..., description="none / low / medium / high / critical")
    mitigation_de: Optional[str] = Field(None, description="Mitigation measure in German")
    area_ratio_critical: bool = Field(False, description="Whether area ratio is unfavorable")
    confidence: str = Field("calculated", description="Confidence level")


class ShackleLoadCalculation(BaseModel):
    """Detailed load calculation for a shackle position."""

    model_config = {"from_attributes": True}

    position: str = Field(..., description="Position identifier")
    static_load_dan: float = Field(..., ge=0, description="Static load in daN")
    dynamic_factor: float = Field(..., ge=1.0, description="Dynamic amplification factor")
    dynamic_load_dan: float = Field(..., ge=0, description="Dynamic load in daN (static × factor)")
    safety_factor: float = Field(..., ge=1.5, description="Safety factor applied")
    required_mbl_dan: float = Field(..., ge=0, description="Required MBL (dynamic × SF) in daN")
    calculation_method: str = Field(..., description="Method used: 'formula' / 'measured' / 'estimated'")
    assumptions_de: list[str] = Field(default_factory=list, description="Assumptions made (in German)")
    confidence: str = Field("calculated", description="Confidence level")
```

---

## ANHANG Y — Expertenwissen und Praxistipps

### Y.1 Profi-Tipps von Rigger-Meistern

**Tipp 1 — Schraubbolzen sichern (Rigg-Praxis):**
Einen kurzen Abschnitt Messing- oder Edelstahldraht (0,8–1,0mm) durch die Bolzenbohrung und um den Bügel wickeln. Der Draht muss leicht zu entfernen sein (Seitenschneider), aber zuverlässig gegen Vibration sichern. NIEMALS so fest wickeln, dass der Schäkel im Notfall nicht geöffnet werden kann.

**Tipp 2 — Schäkel am Mast markieren:**
Farbige Kabelbinder oder Lackmarkierungen (Nagellack) an der Oberkante des Bolzens helfen, bei der Sichtprüfung von Deck sofort zu erkennen, ob sich ein Schäkel gelöst hat. Der Bolzen dreht sich → Markierung verschoben → sofort prüfen.

**Tipp 3 — Anti-Seize richtig anwenden:**
Tef-Gel oder Lanocote dünn auf das Gewinde auftragen — NICHT auf die Auflagefläche des Bolzenkopfes. Auf der Auflagefläche reduziert Anti-Seize die Reibung und der Bolzen kann sich unter Vibration leichter lösen.

**Tipp 4 — Schäkel-Inventar führen:**
Professionelle Yachten führen ein Schäkel-Register mit: Position, Typ, Hersteller, Einbaudatum, MBL, Messwerte. AYDI automatisiert dies über das ShackleLifecycleRecord-Modell. Auch auf privaten Yachten empfehlenswert ab 12m.

**Tipp 5 — Reserveschäkel-Kit zusammenstellen:**
Für Blauwasserfahrten mindestens je 2 Stück der verbauten Rigg-Schäkelgrößen mitführen, dazu 2 Snap-Schäkel für Fallen und einen Ankerschäkel als Reserve. Gesamtkosten Reserve-Kit: 150–400 EUR — verglichen mit dem Risiko eines Rigg-Verlusts vernachlässigbar.

**Tipp 6 — Temperatur und Dyneema:**
Soft-Schäkel beginnen ab 65°C an Festigkeit zu verlieren. An dunklen Beschlägen (schwarzes Aluminium, dunkler Mast) können in der prallen Sonne Oberflächentemperaturen von 80°C+ auftreten. In tropischen Revieren: Soft-Schäkel nicht direkt an dunklen Metallbeschlägen einsetzen oder helle Abdeckung verwenden.

**Tipp 7 — Bolzen-Richtung bei Fallenschäkeln:**
Der Bolzen eines Fallenschäkels zeigt immer vom Segel weg. So kann sich das Tuch nicht am Bolzen verfangen. Bei Schraubbolzen zeigt der Kopf nach Lee (weniger Belastung auf das Gewinde durch Segeldruck).

**Tipp 8 — Schäkelreparatur auf See (Notfall):**
Falls ein Schäkelbolzen verloren geht und kein Ersatz vorhanden: Provisorisch einen passenden Edelstahl-Bolzen oder -Nagel durchstecken und mit Sicherungsdraht fixieren. Dies ist KEINE Dauerlösung. Nächsten Hafen anlaufen und professionell ersetzen. Die provisorische WLL beträgt maximal 30% des Nennwerts.

### Y.2 Häufige Fragen aus der Werftpraxis

**Frage: Wie erkenne ich die Qualität eines Schäkels im Laden?**
- Geschmiedet: Gratnaht sichtbar, gleichmäßige Oberfläche, CE-Markierung eingeschlagen (nicht aufgeklebt)
- Gegossen: oft rauere Oberfläche, manchmal Porositäten sichtbar
- Gravur/Prägung der WLL muss lesbar und dauerhaft sein
- Bolzen muss satt passen (kein Spiel, kein Klemmen)
- Gewinde muss sauber geschnitten sein (keine Grate)
- Verpackung mit Hersteller, WLL, MBL, Norm-Referenz

**Frage: Kann ich Schäkel verschiedener Hersteller mischen?**
Ja, solange Material und Dimensionierung stimmen. Wichtig: gleiche Materialfamilie (nicht 316L mit verzinktem Stahl), passende Bolzendurchmesser zu Augen/Kauschen. Bei Rigg-Schäkeln aus optischen Gründen oft einheitliche Marke bevorzugt.

**Frage: Wie lange halten Schäkel wirklich?**
Bei korrekter Dimensionierung, regelmäßiger Wartung und normalem Fahrtensegeln:
- Edelstahl 316L geschmiedet: 10–15 Jahre
- Duplex 2205: 15–20 Jahre
- Titan: 20+ Jahre
- Soft-Schäkel (Dyneema): 2–5 Jahre (UV-abhängig)
- Verzinkter Stahl (Ankerschäkel): 5–8 Jahre in Salzwasser

---

## ANHANG Z — Regelwerks-Referenz (Zusammenfassung)

### Z.1 Relevante Normen für Schäkel im Yachtbau

| Norm | Titel | Inhalt |
|------|-------|--------|
| EN 13889:2003+A1:2008 | Geschmiedete Stahl-Schäkel, Klasse 4, 6, 8 | Prüfverfahren, Tragfähigkeiten, Kennzeichnung |
| EN 13889-1 | Schäkel Typ A (Bügelschäkel) | Maße und Tragfähigkeiten Bügelschäkel |
| EN 13889-2 | Schäkel Typ B (D-Schäkel) | Maße und Tragfähigkeiten D-Schäkel |
| DIN 82101 | Schäkel (zurückgezogen, ersetzt durch EN 13889) | Historische Referenz, oft noch zitiert |
| AISI 316L | Austenit. Cr-Ni-Mo Stahl (Werkstoff 1.4404) | Korrosionsbeständigkeits-Anforderungen |
| ISO 12401:2009 | Sicherheitsgurte und Sicherheitsleinen | Schäkel an Sicherheitsausrüstung |
| RCD 2013/53/EU | Sportboot-Richtlinie | CE-Konformität von Ausrüstung |
| GL Rules Part 3 | Germanischer Lloyd — Ausrüstung | Klassifikationsanforderungen Superyachten |
| ISAF OSR | Offshore Special Regulations | Regatta-Anforderungen an Beschläge |
| MIL-S-24214 | US-Militärspezifikation Schäkel | Referenz für Hochleistungsschäkel |

### Z.2 Prüfzeichen und Kennzeichnung

| Zeichen | Bedeutung | Verpflichtend? |
|---------|-----------|---------------|
| CE | Konformität mit EU-Richtlinie | Ja (für Hebezeuge) |
| WLL | Working Load Limit (Tragfähigkeit) | Ja (EN 13889) |
| Grade (4/6/8) | Festigkeitsklasse | Ja (EN 13889) |
| Herstellerkürzel | Identifizierung des Herstellers | Ja (EN 13889) |
| Chargennummer | Rückverfolgbarkeit | Empfohlen |
| DNV-GL | Klassifikationsgesellschaft geprüft | Nur Superyachten |
| BV (Bureau Veritas) | Klassifikationsgesellschaft geprüft | Nur Superyachten |
| RINA | Klassifikationsgesellschaft geprüft | Nur Superyachten |

---

*Ende der Wissensdatei 12.01 — Schäkel Grundlagen und Typen*

*AYDI Research, Version 1.1.0, 2026-04-26*
*Status: validated, erweitert*