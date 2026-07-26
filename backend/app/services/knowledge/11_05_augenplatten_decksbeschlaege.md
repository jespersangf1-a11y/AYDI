---
title: "Augenplatten und Decksbeschläge im Yachtbau"
kategorie: "11 Klampen Klemmen Schienensysteme"
unterkategorie: "05 Augenplatten und Decksbeschläge"
version: "1.0.0"
datum: "2026-04-25"
autor: "AYDI Research"
status: "validated"
confidence_quellen:
  - measured: "Hersteller-Datenblätter, Laborprüfungen, Zerstörungstests"
  - documented: "Hersteller-Kataloge, Rigger-Fachliteratur, Klassifikationsgesellschaften"
  - estimated: "Erfahrungswerte, Quervergleiche, Branchenpraxis"
  - benchmark: "Marktdurchschnitte, Branchenstandards, Regattaerfahrung"
tags:
  - augenplatten
  - pad_eyes
  - decksbeschläge
  - wantenplatten
  - chainplates
  - bügelbolzen
  - u_bolts
  - tang_plates
  - deck_organizers
  - leitösen
  - fairleads
  - klüsen
  - festmacherringe
  - lasteinleitung
  - backing_plates
  - rigg
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

# 11.05 — Augenplatten und Decksbeschläge im Yachtbau: Vollständige Wissensreferenz

> **AYDI Wissensdatei 11.05** — Kategorie 11: Klampen Klemmen Schienensysteme
> **Confidence-Quelle:** measured (Hersteller-TDS, Zerstörungstests), documented (Hersteller-Kataloge, Fachliteratur), estimated (Erfahrungswerte)
> **Letzte Aktualisierung:** 2026-04-25

---

## Inhaltsverzeichnis

1. [Einführung und Übersicht](#1-einführung-und-übersicht)
2. [Grundlagen und Theorie](#2-grundlagen-und-theorie)
3. [Typenübersicht](#3-typenübersicht)
4. [Produktlinien und Hersteller](#4-produktlinien-und-hersteller)
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
18. [ANHANG G — Historische Entwicklung](#anhang-g--historische-entwicklung)
19. [ANHANG H — Bezugsquellen](#anhang-h--bezugsquellen)
20. [ANHANG I — Herstellervergleich Detailtabellen](#anhang-i--herstellervergleich-detailtabellen)
21. [ANHANG J — Auswahl-Algorithmus](#anhang-j--auswahl-algorithmus)
22. [ANHANG K — Prüfprotokolle](#anhang-k--prüfprotokolle)
23. [ANHANG L — Visuelle Analyse-Referenz](#anhang-l--visuelle-analyse-referenz)
24. [ANHANG M — Korrosionsschutz-Leitfaden](#anhang-m--korrosionsschutz-leitfaden)
25. [ANHANG N — Retrofit-Leitfaden](#anhang-n--retrofit-leitfaden)
26. [ANHANG O — Regatta-Spezifikationen](#anhang-o--regatta-spezifikationen)
27. [ANHANG P — Superyacht-Sonderlösungen](#anhang-p--superyacht-sonderlösungen)
28. [ANHANG Q — Umrechnungstabellen](#anhang-q--umrechnungstabellen)
29. [ANHANG R — Checklisten](#anhang-r--checklisten)

---

## 1. Einführung und Übersicht

### 1.1 Was sind Augenplatten und Decksbeschläge?

Augenplatten (englisch: pad eyes) und Decksbeschläge (deck fittings) bilden die kritischen Lasteinleitungspunkte auf Segelyachten und Motoryachten. Sie verbinden dynamische Kräfte aus Rigg, Segeln, Festmacherleinen, Ankerketten und Sicherheitssystemen mit der Deckskonstruktion und leiten diese in den Rumpfverbund ein. Ihre korrekte Dimensionierung, Montage und Wartung ist sicherheitsrelevant — ein Versagen kann zu Riggverlust, Personenschaden oder Schiffsuntergang führen.

### 1.2 Funktionale Einordnung

Augenplatten und Decksbeschläge erfüllen folgende Grundfunktionen:

- **Lasteinleitung**: Punktförmige Aufnahme von Zug-, Scher- und kombinierten Kräften
- **Kraftumlenkung**: Veränderung der Lastrichtung über definierte Radien
- **Befestigung**: Sichere Anbindung von Tauwerk, Schäkeln, Blöcken und Beschlägen
- **Sicherung**: Anschlagpunkte für Lifelinehalterungen, Sicherheitsgurte, MOB-Systeme
- **Festmachen**: Aufnahme von Festmacherleinen, Ankerketten, Schleppleinen

### 1.3 Abgrenzung zu verwandten Beschlaggruppen

| Beschlaggruppe | Wissensdatei | Abgrenzung |
|---|---|---|
| Klampen | 11.01 | Belegen von Tauwerk durch Umschlagen |
| Klemmen (Cam Cleats) | 11.02 | Klemmen von laufendem Gut |
| Schienensysteme | 11.03 | Lineare Verstellung von Beschlagpunkten |
| Blöcke | 10.01–10.07 | Umlenkung mit Rollreibung |
| Winschen | 09.01–09.07 | Mechanische Kraftverstärkung |
| **Augenplatten/Decksbeschläge** | **11.05** | **Stationäre Lastaufnahmepunkte** |

### 1.4 Sicherheitsrelevanz

Augenplatten und Decksbeschläge gehören zu den **sicherheitskritischen Bauteilen** einer Yacht:

- **Rigg-Sicherung**: Wantenplatten tragen die gesamte Rigglast (bei einer 12m-Yacht bis zu 15 Tonnen pro Seite)
- **Personensicherheit**: Augenplatten als Anschlagpunkte für Sicherheitsgurte (EN ISO 15085)
- **Schiffssicherheit**: Festmacherbeschläge müssen Sturmlasten standhalten
- **Bergesicherheit**: Schleppösen müssen das Vielfache der Schiffsverdrängung aufnehmen

> **AYDI-Klassifikation**: Alle Augenplatten und lasttragenden Decksbeschläge werden als **Sicherheitskategorie A** eingestuft. Jede Analyse erfordert eine Confidence-Bewertung ≥ "visual_medium" für eine Beurteilung.

### 1.5 Relevanz für AYDI-Analysepipelines

| Pipeline | Relevanz | Erfasste Parameter |
|---|---|---|
| Pipeline A (Strukturiert) | Hoch | SWL, Bruchlast, Material, Maße, Schraubenanzahl |
| Pipeline B (Visuell) | Hoch | Zustand, Korrosion, Rissbildung, Montagequalität |
| Pipeline C (Text) | Mittel | Servicevermerke, Inspektionsberichte, Schadensmeldungen |

### 1.6 Normativer Rahmen

Die Auslegung von Augenplatten und Decksbeschlägen unterliegt folgenden Normen und Richtlinien:

- **ISO 15084:2003** — Verankerung und Festmachen
- **ISO 15085:2003** — Vorbeugung gegen Mann-über-Bord und Bergung
- **EN 795:2012** — Persönliche Absturzsicherung — Anschlageinrichtungen
- **GL/DNV Rules for Yachts** — Klassifikationsregeln für Decksbeschläge
- **ABS Guide for Building and Classing Yachts** — Strukturelle Anforderungen
- **ABYC H-40** — Verankerung, Festmachen und Kraftangriffspunkte (Strong Points; US-Standard)

---

## 2. Grundlagen und Theorie

### 2.1 Lastberechnung für Augenplatten

#### 2.1.1 Grundformel der Lasteinleitung

Die auf eine Augenplatte wirkende Kraft setzt sich zusammen aus:

```
F_total = F_static + F_dynamic + F_shock

Wobei:
  F_static  = Statische Grundlast (Gewicht, Vorspannung)
  F_dynamic = Dynamische Last (Wellenschlag, Böen, Manöver)
  F_shock   = Stoßlast (Ruckartige Belastung, Blockierung)
```

#### 2.1.2 Sicherheitsfaktoren

Für maritime Anwendungen gelten folgende **Mindest-Sicherheitsfaktoren**:

| Anwendung | Sicherheitsfaktor | Begründung |
|---|---|---|
| Rigg-Beschläge (stehend) | 4:1 | Dynamische Wechsellasten, Ermüdung |
| Rigg-Beschläge (laufend) | 5:1 | Zusätzliche Reibungsverluste |
| Wantenplatten | 4:1 bis 5:1 | Höchste Sicherheitsanforderung |
| Festmacherbeschläge | 3:1 | Vorwiegend statisch |
| Schleppösen | 6:1 | Extreme Stoßlasten |
| Sicherheitsgurt-Anschlag | 5:1 | Personensicherheit, EN 795 |
| Spinnaker-Beschläge | 4:1 | Hohe dynamische Lasten |
| Ankerbeschläge | 4:1 | Stoß + Ermüdung |

```
Berechnung:
  SWL (Safe Working Load) = Breaking Load / Safety Factor
  
Beispiel Wantenplatte:
  Breaking Load = 60.000 N (6t)
  Safety Factor = 4.0
  SWL = 60.000 / 4.0 = 15.000 N (1,5t)
```

#### 2.1.3 Zugwinkel-Effekt (Pull Angle Effect)

Der Zugwinkel hat erheblichen Einfluss auf die tatsächliche Belastung der Befestigung:

```
Vertikale Kraft auf Deck:
  F_vertical = F_line × sin(α)

Horizontale Kraft (Scherkraft):
  F_horizontal = F_line × cos(α)

Hebelmoment an der Grundplatte:
  M = F_line × sin(α) × h_eye

Wobei:
  α = Winkel der Leine zur Horizontalen
  h_eye = Höhe des Auges über der Decksoberfläche
  F_line = Kraft in der Leine
```

**Kritische Winkel und ihre Auswirkungen:**

| Zugwinkel α | Vertikalkraft | Scherkraft | Hebelmoment | Bewertung |
|---|---|---|---|---|
| 0° (horizontal) | 0% | 100% | Minimal | Ideal für flache Augenplatten |
| 15° | 26% | 97% | Gering | Standardfall Decksbeschläge |
| 30° | 50% | 87% | Moderat | Noch akzeptabel |
| 45° | 71% | 71% | Erhöht | Backing Plate erforderlich |
| 60° | 87% | 50% | Hoch | Verstärkung empfohlen |
| 90° (vertikal) | 100% | 0% | Maximal | Nur mit massiver Verstärkung |

> **AYDI-Regel**: Bei Zugwinkeln > 30° zur Horizontalen wird automatisch eine erweiterte Backing-Plate-Analyse ausgelöst.

#### 2.1.4 Backing-Plate-Dimensionierung

Die Backing Plate (Verstärkungsplatte, Gegenplatte) ist entscheidend für die Lastverteilung:

```
Flächenberechnung:
  A_backing = F_total / σ_zul_deck

  σ_zul_deck (zulässige Druckspannung):
    GFK-Sandwichdeck:     2–4 N/mm²
    GFK-Volllaminat:      8–12 N/mm²
    Aluminiumdeck:        20–40 N/mm²
    Teakdeck auf GFK:     2–4 N/mm² (GFK maßgebend)
    Sperrholzdeck:        4–6 N/mm²

Beispiel:
  F_total = 20.000 N (2t Wantenzug)
  Deck = GFK-Sandwich (σ_zul = 3 N/mm²)
  A_backing = 20.000 / 3 = 6.667 mm² ≈ 67 cm²
  → Mindestens 82 × 82 mm quadratisch
  → Empfohlen: 100 × 100 mm mit abgerundeten Ecken
```

**Dickenberechnung der Backing Plate:**

```
Materialdicke (Edelstahl 316L):
  t = √(6 × M_max / (b × σ_yield))

  Wobei:
    M_max = maximales Biegemoment an der Platte
    b = Plattenbreite
    σ_yield = Streckgrenze (316L: 205 N/mm²)

Faustregeln:
  Lasten bis 500 kg:   t = 3 mm Edelstahl / 5 mm Aluminium
  Lasten bis 1.500 kg: t = 5 mm Edelstahl / 8 mm Aluminium
  Lasten bis 3.000 kg: t = 8 mm Edelstahl / 12 mm Aluminium
  Lasten über 3.000 kg: Individuelle Berechnung erforderlich
```

#### 2.1.5 Kernverstärkung bei Sandwichdecks

Bei Sandwich-Konstruktionen (Balsa- oder Schaumkern) muss der Kern im Bereich der Beschlagmontage ersetzt werden:

```
Kernverstärkung (Core Reinforcement):

Schritt 1: Kern entfernen im Umkreis von:
  r_reinforcement = r_backing + 25 mm (Minimum)
  
Schritt 2: Kern ersetzen durch:
  Option A: Epoxid-Füllmasse (z.B. West System 105/205 + 404 Filler)
  Option B: G10/FR4-Einsatz (hochfester Glasfaser-Laminat-Block)
  Option C: Hartholz-Einsatz (Eiche, imprägniert)
  Option D: Aluminium-Einleger (bei höchsten Lasten)

Schritt 3: Nachträgliches Laminieren der Ober- und Unterseite:
  Mindestens 2 Lagen Biaxialgewebe 300 g/m² über den verstärkten Bereich
```

**Druckfestigkeit der Kernersatzmaterialien:**

| Material | Druckfestigkeit [N/mm²] | Gewicht | Empfehlung |
|---|---|---|---|
| Epoxid + 404 Filler | 40–60 | Mittel | Standard für die meisten Anwendungen |
| G10/FR4 Block | 250–350 | Mittel | Hochlast-Anwendungen |
| Eiche (imprägniert) | 30–50 | Hoch | Traditionell, bewährt |
| Aluminium 6082 | 250+ | Hoch | Superyacht, extreme Lasten |
| PU-Gießharz | 25–40 | Leicht | Leichtbau, moderate Lasten |

#### 2.1.6 Composite-Laminat-Lastverteilung

Die Krafteinleitung in ein GFK-Laminat erfolgt über Flächenpressung und Scherung:

```
Lochleibungsfestigkeit (Bearing Strength):
  σ_bearing = F / (d × t)

  Wobei:
    F = Schraubenkraft pro Schraube
    d = Schraubendurchmesser
    t = Laminatdicke

Zulässige Lochleibungsspannung:
  GFK-Polyester:     150–200 N/mm²
  GFK-Vinylester:    180–250 N/mm²
  GFK-Epoxid:        200–300 N/mm²
  CFK-Epoxid:        250–400 N/mm² (aber: galvanische Probleme mit Edelstahl!)
```

**Schraubenabstände im Laminat:**

```
Randabstand:         e₁ ≥ 3 × d (in Kraftrichtung)
                     e₂ ≥ 2.5 × d (quer zur Kraftrichtung)
Schraubenabstand:    p₁ ≥ 4 × d (in Kraftrichtung)
                     p₂ ≥ 3 × d (quer zur Kraftrichtung)

Wobei d = Schraubendurchmesser

Beispiel M8-Schraube:
  e₁ ≥ 24 mm, e₂ ≥ 20 mm
  p₁ ≥ 32 mm, p₂ ≥ 24 mm
```

#### 2.1.7 Bearing-Stress-Berechnung

```
Bearing Stress (Flächenpressung am Bolzen):
  σ_b = F / (n × d × t_eff)

  Wobei:
    F = Gesamtkraft am Beschlag
    n = Anzahl der Befestigungsschrauben
    d = Schrauben-Nenndurchmesser
    t_eff = effektive tragende Laminatdicke

Zulässige Werte:
  σ_b_zul (316L auf GFK) = 80–120 N/mm²
  σ_b_zul (316L auf Aluminium) = 150–200 N/mm²
  σ_b_zul (316L auf Edelstahl) = 200–280 N/mm²

Beispiel:
  F = 10.000 N, 4 × M8 Schrauben, Laminat 6 mm
  σ_b = 10.000 / (4 × 8 × 6) = 52 N/mm² → OK (< 80 N/mm²)
```

### 2.2 Ermüdungsfestigkeit

#### 2.2.1 Wöhler-Kurve für Decksbeschläge

Decksbeschläge unterliegen zyklischer Belastung durch Seegang und Manöver:

```
Lastzyklen pro Saison (geschätzt):
  Wantenplatten:       500.000–2.000.000 Zyklen (Wellenbelastung)
  Genuaschot-Augenpl.: 10.000–50.000 Zyklen (Wenden)
  Spinnaker-Beschläge: 1.000–5.000 Zyklen (Saisonnutzung)
  Festmacherbeschläge: 5.000–20.000 Zyklen (Liegeplatz)

Dauerfestigkeit (Edelstahl 316L):
  σ_D ≈ 0.35 × σ_UTS = 0.35 × 515 = 180 N/mm²
  
Dauerfestigkeit (Duplex 2205):
  σ_D ≈ 0.40 × σ_UTS = 0.40 × 620 = 248 N/mm²
```

#### 2.2.2 Kerbwirkung

Schweißnähte, Bohrungen und Radienübergänge erzeugen Spannungskonzentrationen:

```
Kerbfaktor K_t:
  Gebohrtes Loch in Platte:      K_t = 2.5–3.0
  Schweißnaht (gut ausgeführt):   K_t = 1.5–2.0
  Schweißnaht (schlecht):         K_t = 3.0–5.0
  Übergang Auge-Basis (r > 3mm):  K_t = 1.5–2.0
  Übergang Auge-Basis (r < 1mm):  K_t = 3.0–4.0

Effektive Spannung:
  σ_eff = K_t × σ_nominal

→ Ein schlecht ausgeführter Schweißnaht-Übergang kann die effektive
  Dauerfestigkeit um den Faktor 3 reduzieren!
```

### 2.3 Korrosionsaspekte bei Lasteinleitungspunkten

#### 2.3.1 Galvanische Korrosion

```
Galvanische Spannungsreihe (Seewasser, relevante Paarungen):

Material                    Potenzial [V vs. SCE]
─────────────────────────────────────────────────
Graphit / CFK               +0.20 bis +0.35
316L Edelstahl (passiv)     -0.05 bis -0.10
Duplex 2205 (passiv)        -0.05 bis -0.08
Bronze (CuSn8)              -0.24 bis -0.31
Messing                     -0.28 bis -0.36
Aluminium 5083              -0.73 bis -0.80
Aluminium 6082              -0.75 bis -0.83
Zink                        -1.00 bis -1.05

KRITISCH: CFK-Deck + Edelstahl-Beschlag → ΔV > 0.25V → Korrosion!
  → Isolation durch GFK-Zwischenlage oder Tef-Gel erforderlich
```

#### 2.3.2 Spaltkorrosion an Befestigungspunkten

```
Spaltkorrosion entsteht in:
  - Schraube/Laminat-Übergang (Bohrungsspalt)
  - Backing Plate/Laminat-Kontaktfläche
  - Unter der Kopfauflage von Schrauben
  - In Gewindeverbindungen

Gegenmaßnahmen:
  1. Sealant (Sikaflex 291i) als Dichtmittel in Schraubenlöchern
  2. Edelstahl mindestens 316L (Mo-Gehalt ≥ 2%)
  3. Duplex 2205 bei extremer Exposition
  4. Lanolin-Paste (Lanocote) auf Gewindeverbindungen
  5. Tef-Gel bei galvanisch kritischen Paarungen
```

### 2.4 Dynamische Lastfälle

#### 2.4.1 Lastfälle für Segelyachten

```
Lastfall 1: Normalfahrt (Am Wind, 15 kt)
  Wantenplatten:     0.5 × SWL (Dauerbelastung)
  Schot-Augenplatten: 0.3 × SWL
  Spinnaker:         0 (nicht gesetzt)

Lastfall 2: Starker Wind (Am Wind, 25 kt, 1. Reff)
  Wantenplatten:     0.8 × SWL
  Schot-Augenplatten: 0.6 × SWL
  Spinnaker:         0

Lastfall 3: Böe (35 kt Böe in 25 kt)
  Wantenplatten:     1.0 × SWL (kurzzeitig)
  Schot-Augenplatten: 0.8 × SWL
  Dynamic Factor:    1.5–2.0

Lastfall 4: Broaching / Knockdown
  Lee-Wantenplatten: bis 1.2 × SWL (Stoß)
  Alle Beschläge:    Dynamic Factor 2.5–3.0

Lastfall 5: Rigging Failure (Notfall)
  Einzelne Wantenpl.: bis 1.5 × SWL (Umverteilung)
  → Sicherheitsfaktor 4:1 muss dies abdecken
```

---

## 3. Typenübersicht

### 3.1 Augenplatten / Pad Eyes

#### 3.1.1 Geschweißte Augenplatten (Welded Pad Eyes)

**Beschreibung:** Ein Edelstahl-Auge ist direkt auf eine Grundplatte geschweißt. Einteilige Konstruktion nach dem Schweißvorgang. Höchste Festigkeit bei korrekter Ausführung.

**Konstruktionsmerkmale:**
- Grundplatte: 3–8 mm Edelstahl 316L
- Auge: Rundstahl oder Flachstahl, gebogen und verschweißt
- Schweißnaht: Kehlnaht umlaufend, a-Maß ≥ 0.7 × t_min
- Bohrungen: 4–8 Befestigungslöcher je nach Größe

**Typische Abmessungen und Lasten:**

| Bezeichnung | Grundplatte [mm] | Auge ∅ [mm] | SWL [kg] | Bruchlast [kg] |
|---|---|---|---|---|
| Micro | 30 × 20 × 3 | 8 | 200 | 800 |
| Klein | 50 × 30 × 4 | 12 | 500 | 2.000 |
| Mittel | 65 × 40 × 5 | 16 | 1.000 | 4.000 |
| Groß | 80 × 50 × 6 | 20 | 2.000 | 8.000 |
| XL | 100 × 65 × 8 | 25 | 3.500 | 14.000 |
| XXL | 130 × 80 × 10 | 32 | 5.000 | 20.000 |

**Vorteile:**
- Höchste Festigkeit durch durchgängige Schweißverbindung
- Keine beweglichen Teile, kein Verschleiß am Auge
- Kompakte Bauform
- Geringes Gewicht bei hoher Festigkeit

**Nachteile:**
- Schweißqualität kritisch für Lebensdauer
- Nicht zerlegbar, Austausch nur komplett
- Spannungskonzentration am Schweißnaht-Fuß
- Qualitätskontrolle der Schweißnaht schwierig

**Einsatzgebiete:**
- Genuaschot-Umlenkung
- Spinnaker-Barberholer
- Relingsdurchführungen
- Lazyjack-Befestigung
- Sicherheitsgurt-Anschlagpunkte

#### 3.1.2 Geschraubte Augenplatten (Bolted Pad Eyes)

**Beschreibung:** Das Auge wird durch eine Schraube oder einen Bolzen an einer Grundplatte befestigt. Zerlegbar und austauschbar.

**Konstruktionsmerkmale:**
- Grundplatte mit zentraler Bohrung oder Gewinde
- Augbolzen (Eye Bolt) mit Gewinde M6–M16
- Kontermutter oder Sicherungsmutter zur Fixierung
- Optional: Kugelgelenk für multidirektionale Belastung

**Typische Abmessungen und Lasten:**

| Gewinde | Auge ∅ innen [mm] | SWL [kg] | Bruchlast [kg] |
|---|---|---|---|
| M6 | 10 | 100 | 400 |
| M8 | 14 | 250 | 1.000 |
| M10 | 18 | 500 | 2.000 |
| M12 | 22 | 800 | 3.200 |
| M16 | 28 | 1.500 | 6.000 |
| M20 | 36 | 2.500 | 10.000 |

**Vorteile:**
- Zerlegbar und einzeln austauschbar
- Kugelgelenk-Variante für variable Zugrichtungen
- Einfache Montage und Demontage
- Ersatzteile leicht verfügbar

**Nachteile:**
- Geringere Festigkeit als geschweißte Varianten
- Gewindevorlast muss regelmäßig kontrolliert werden
- Korrosion im Gewinde möglich
- Größere Bauhöhe durch Augbolzen

#### 3.1.3 Klappbare Augenplatten (Folding Pad Eyes)

**Beschreibung:** Das Auge ist über einen Bolzen schwenkbar an der Grundplatte befestigt und kann flach auf das Deck geklappt werden, wenn es nicht benötigt wird.

**Konstruktionsmerkmale:**
- Grundplatte mit integrierter Mulde für eingeklapptes Auge
- Schwenkbolzen aus Edelstahl 316L
- Federraste oder Arretierung im aufgestellten Zustand
- Typisch: 3–5 mm Plattenstärke

**Typische Abmessungen und Lasten:**

| Bezeichnung | Grundplatte [mm] | SWL [kg] | Bruchlast [kg] |
|---|---|---|---|
| Klein | 55 × 30 × 3 | 200 | 800 |
| Mittel | 70 × 40 × 4 | 500 | 2.000 |
| Groß | 90 × 55 × 5 | 1.000 | 4.000 |
| XL | 110 × 70 × 6 | 1.800 | 7.200 |

**Vorteile:**
- Reduzierte Verletzungsgefahr (kein hervorstehendes Auge)
- Geringerer Luftwiderstand bei Nichtgebrauch
- Sauberes Deckslayout
- Ideal für selten genutzte Anschlagpunkte

**Nachteile:**
- Beweglicher Schwenkbolzen als Verschleißelement
- Geringere Bruchlast als starre Augenplatten (ca. 60–70%)
- Arretierung muss funktionssicher sein
- Höhere Kosten als starre Varianten

**Einsatzgebiete:**
- Spinnaker-Anschlagpunkte (nur bei Bedarf)
- Sicherheitsleinenösen am Deck
- Saisonal wechselnde Beschlagkonfigurationen
- Charteryachten (Verletzungsprävention)

#### 3.1.4 Diamant-Augenplatten (Diamond Base Pad Eyes)

**Beschreibung:** Geschweißte oder gegossene Augenplatte mit rautenförmiger (diamantförmiger) Grundplatte. Die Rautenform verteilt die Befestigungspunkte optimal für die typische Einzellast-Zugrichtung.

**Konstruktionsmerkmale:**
- Rautenförmige Grundplatte mit 4 Bohrungen an den Ecken
- Zwei Bohrungen in Zugrichtung (primäre Lastaufnahme)
- Zwei Bohrungen quer (Stabilisierung gegen Querlasten)
- Geschweißtes oder integriertes Auge in der Mitte

**Typische Abmessungen und Lasten:**

| Bezeichnung | Grundplatte [mm] | SWL [kg] | Bruchlast [kg] |
|---|---|---|---|
| S (4-Bolt) | 60 × 40 × 4 | 600 | 2.400 |
| M (4-Bolt) | 80 × 55 × 5 | 1.200 | 4.800 |
| L (4-Bolt) | 100 × 70 × 6 | 2.000 | 8.000 |
| XL (6-Bolt) | 130 × 90 × 8 | 3.500 | 14.000 |

**Vorteile:**
- Optimale Lastverteilung für unidirektionale Zugbelastung
- Effiziente Materialnutzung
- Geringere Spannungskonzentration an den Befestigungen
- Bewährte Form im professionellen Rigging

**Nachteile:**
- Nur für eine Hauptzugrichtung optimiert
- Bei multidirektionaler Belastung nicht ideal
- Größere Decksfläche erforderlich als bei Rundplatten

#### 3.1.5 Oval-Augenplatten (Oval Base Pad Eyes)

**Beschreibung:** Augenplatte mit ovaler oder elliptischer Grundplatte. Kompromiss zwischen Diamant- und Rundform mit gleichmäßiger Lastverteilung.

**Konstruktionsmerkmale:**
- Ovale Grundplatte mit 4–6 Bohrungen
- Gleichmäßig verteilte Befestigungspunkte
- Geschweißtes Auge in der Mitte
- Oft mit erhöhtem Rand (Versteifung)

**Typische Abmessungen und Lasten:**

| Bezeichnung | Grundplatte [mm] | SWL [kg] | Bruchlast [kg] |
|---|---|---|---|
| S | 50 × 35 × 3 | 400 | 1.600 |
| M | 70 × 50 × 5 | 1.000 | 4.000 |
| L | 90 × 65 × 6 | 1.800 | 7.200 |
| XL | 120 × 85 × 8 | 3.000 | 12.000 |

### 3.2 Wantenplatten / Chainplates

#### 3.2.1 Externe Wantenplatten (External Chainplates)

**Beschreibung:** Wantenplatten, die an der Außenseite des Rumpfes montiert sind. Typisch für ältere Yachten und bestimmte Konstruktionsphilosophien.

**Konstruktionsmerkmale:**
- Flachstahl 316L oder Duplex 2205, typisch 8–15 mm stark
- Durch den Rumpf gebolzte Befestigung
- Obere Ausbiegung über die Schandeckelhöhe
- Breite: 40–80 mm, Länge: 200–500 mm

**Lastpfad:**
```
Rigg-Last → Want → Gabelkopf/Toggle → Wantenbolzen →
Wantenplatte → Schrauben → Rumpflaminat → Schott/Stringer
```

**Typische Abmessungen nach Bootsgröße:**

| Bootslänge | Plattenstärke [mm] | Breite [mm] | Bolzenanzahl | SWL pro Platte [t] |
|---|---|---|---|---|
| 8–10m | 6–8 | 40–50 | 3–4 | 2–4 |
| 10–12m | 8–10 | 50–60 | 4–5 | 4–6 |
| 12–15m | 10–12 | 60–70 | 5–6 | 6–10 |
| 15–18m | 12–15 | 70–80 | 6–8 | 10–15 |
| 18m+ | 15–20 | 80–100 | 8–10 | 15–25 |

**Vorteile:**
- Einfache Inspektion von außen
- Kein Decksdurchbruch erforderlich
- Gute Zugänglichkeit für Wartung
- Bewährte Konstruktion

**Nachteile:**
- Optisch weniger ansprechend
- Erhöhter Luftwiderstand
- Wassereintritt an Rumpfdurchführung möglich
- Rumpf-Laminat-Belastung konzentriert

#### 3.2.2 Interne Wantenplatten (Internal / Through-Deck Chainplates)

**Beschreibung:** Wantenplatten, die durch das Deck geführt werden und innen am Rumpf (typisch an Schotten oder Stringern) befestigt sind. Standard bei modernen Segelyachten.

**Konstruktionsmerkmale:**
- Flachstahl durch Decksdurchführung mit Dichtung
- Untere Befestigung an Schott, Stringer oder Rumpf-Deck-Verbindung
- Bolzenreihe vertikal über 200–600 mm Länge
- Decksdurchführung mit Neopren- oder PU-Manschette abgedichtet

**Lastpfad:**
```
Rigg-Last → Want → Gabelkopf/Toggle → Wantenbolzen →
Wantenplatte → Decksdurchführung → Bolzen → Schott/Stringer →
Rumpfstruktur
```

**Kritische Punkte bei Through-Deck-Chainplates:**

1. **Decksdurchführung**: Häufigste Undichtigkeit bei Segelyachten
2. **Schott-Anbindung**: Laminat-Verbindung Schott/Rumpf muss Wantenzug aufnehmen
3. **Winkelausrichtung**: Platte muss exakt auf den Wantwinkel ausgerichtet sein
4. **Korrosion unterhalb**: Schwer inspizierbar, häufig verdeckte Schäden

**Dichtungssysteme:**

| System | Lebensdauer | Wartungsintervall | Kosten |
|---|---|---|---|
| Neopren-Manschette | 5–8 Jahre | Jährlich prüfen | Gering |
| PU-Verguss (Sikaflex) | 8–12 Jahre | Alle 2 Jahre prüfen | Gering |
| Edelstahl-Flansch + O-Ring | 15+ Jahre | Alle 3 Jahre prüfen | Mittel |
| GFK-Aufbau mit Epoxid | 20+ Jahre | Alle 5 Jahre prüfen | Hoch |
| Cover Plate (Wichard) | 10–15 Jahre | Jährlich prüfen | Mittel |

#### 3.2.3 Kielgeführte Wantenplatten (Keel-Stepped Chainplates)

**Beschreibung:** Wantenplatten, die direkt am Kielschwein oder an der Kiel-Rumpf-Verbindung angeschlagen sind. Maximale strukturelle Integrität.

**Konstruktionsmerkmale:**
- Langer Edelstahlflachstahl vom Kielbereich bis zum Deck
- Befestigung direkt am Kielschwein (Keel Floor Timbers)
- Lastpfad direkt in die stärkste Rumpfstruktur
- Typisch bei Langkielern und schweren Fahrtenyachten

**Vorteile:**
- Kürzester und stärkster Lastpfad
- Keine Abhängigkeit von Schott-Laminierung
- Geringste Rumpfverformung unter Last
- Maximale Sicherheitsreserve

**Nachteile:**
- Aufwändige Nachrüstung
- Schwer zugänglich für Inspektion
- Längere Wantenplatten = mehr Gewicht
- Nur bei geeigneter Rumpfkonstruktion möglich

### 3.3 Bügelbolzen / U-Bolts

#### 3.3.1 Geschweißte Bügelbolzen (Welded Base U-Bolts)

**Beschreibung:** U-förmig gebogener Edelstahlrundstahl, auf eine Grundplatte geschweißt. Die zwei aufstehenden Schenkel bilden eine Öse für Schäkel oder Tauwerk.

**Konstruktionsmerkmale:**
- U-Bügel aus Rundstahl 316L, Durchmesser 6–16 mm
- Grundplatte 3–8 mm mit 2–4 Befestigungsbohrungen
- Schweißnaht umlaufend an beiden Schenkeln
- Innere Bügelweite: 20–60 mm

**Typische Abmessungen und Lasten:**

| Rundstahl ∅ [mm] | Bügelweite [mm] | SWL [kg] | Bruchlast [kg] |
|---|---|---|---|
| 6 | 20 | 300 | 1.200 |
| 8 | 25 | 600 | 2.400 |
| 10 | 30 | 1.000 | 4.000 |
| 12 | 40 | 1.500 | 6.000 |
| 16 | 50 | 3.000 | 12.000 |

**Einsatzgebiete:**
- Blockbefestigung an Deck und Mast
- Leitösen für Leinen
- Anschlagpunkte für Sicherheitsleinen
- Traveller-Endanschläge

#### 3.3.2 Durchgesteckte Bügelbolzen (Through-Bolt U-Bolts)

**Beschreibung:** U-Bügel, der durch das Deck gesteckt und von unten mit Muttern auf einer Backing Plate gesichert wird. Keine Schweißnaht, sehr hohe Zugfestigkeit.

**Konstruktionsmerkmale:**
- U-Bügel aus Rundstahl 316L mit Gewinde an beiden Schenkeln
- Decksdurchführung mit Sealant abgedichtet
- Backing Plate unterhalb des Decks
- Selbstsichernde Muttern (Nyloc) oder Federscheiben + Kontermutter

**Vorteile:**
- Höchste Zugfestigkeit (keine Schweißnaht)
- Einfach zu inspizieren (Muttern von unten sichtbar)
- Nachspannbar
- Leicht austauschbar

**Nachteile:**
- Decksdurchbruch erforderlich (Undichtigkeitsrisiko)
- Backing Plate unterhalb muss zugänglich sein
- Größere Bauhöhe unter Deck
- Zwei Dichtstellen statt einer

### 3.4 Anschlussplatten / Tang Plates

**Beschreibung:** Flache, hochfeste Platten, die als Verbindungselement zwischen Rigg-Komponenten und Strukturelementen dienen. Typisch als Übergang zwischen Want/Stag und Wantenplatte oder Rumpfstruktur.

**Konstruktionsmerkmale:**
- Material: 316L, Duplex 2205, oder Titan Grade 5
- Dicke: 5–20 mm je nach Last
- Bohrungen: 1 Bolzenbohrung für Rigg-Anschluss, 2–6 Bohrungen für Strukturbefestigung
- Kanten: alle entgratet und verrundet (R ≥ 2 mm)

**Typische Anwendungen:**

| Anwendung | Material | Dicke [mm] | Bolzen | SWL [t] |
|---|---|---|---|---|
| Vorstag-Anschluss | Duplex 2205 | 10–15 | M12–M16 | 3–8 |
| Oberwant-Anschluss | 316L / Duplex | 8–12 | M10–M14 | 2–6 |
| Unterwant-Anschluss | 316L | 6–10 | M8–M12 | 1–4 |
| Backstag-Anschluss | 316L / Duplex | 8–12 | M10–M14 | 2–5 |
| Babystag-Anschluss | 316L | 6–8 | M8–M10 | 1–3 |
| Spinnaker-Aufholer | 316L | 5–8 | M8–M10 | 0.5–2 |

**Berechnung der Tang Plate:**
```
Zugquerschnitt netto:
  A_net = (b - d_hole) × t

Zulässige Zuglast:
  F_zul = A_net × σ_yield / SF

Beispiel (Oberwant, 12m Segelyacht):
  b = 50 mm, d_hole = 14 mm, t = 10 mm
  A_net = (50 - 14) × 10 = 360 mm²
  σ_yield (316L) = 205 N/mm²
  SF = 4.0
  F_zul = 360 × 205 / 4.0 = 18.450 N ≈ 1.88 t SWL
```

### 3.5 Leitösen / Deck Organizers

#### 3.5.1 Einzel-Leitösen (Single Deck Organizers)

**Beschreibung:** Einzelne Edelstahl- oder Kunststoff-Führung zur sauberen Leinenführung an Deck. Lenkt Leinen in einem definierten Winkel um.

**Konstruktionsmerkmale:**
- Führungsrolle (Sheave) oder feste Führung (Fairlead)
- Grundplatte mit 2–4 Befestigungslöchern
- Materialien: 316L Edelstahl, Delrin, Torlon, Aluminium eloxiert
- Leinendurchmesser: 6–16 mm

#### 3.5.2 Doppel-Leitösen (Double Deck Organizers)

**Beschreibung:** Zwei parallel angeordnete Leinenführungen in einem gemeinsamen Gehäuse. Platzsparend für parallele Leinenführung (z.B. Reffleinen).

**Typische Konfigurationen:**
- 2-fach für Vor- und Achterreffleine
- Rollengelagert oder Gleitführung
- Aufrecht oder liegend montiert

#### 3.5.3 Dreifach- und Mehrfach-Leitösen (Triple/Multi Deck Organizers)

**Beschreibung:** Drei oder mehr Leinenführungen in einer Einheit. Standard am Mastfuß oder Cockpit-Eingang für die gebündelte Führung aller Leinen.

**Typische Abmessungen:**

| Konfiguration | Leinenzahl | Leinen-∅ [mm] | Breite [mm] | SWL pro Leine [kg] |
|---|---|---|---|---|
| Triple S | 3 | 6–8 | 80 | 300 |
| Triple M | 3 | 8–10 | 100 | 500 |
| Triple L | 3 | 10–12 | 120 | 800 |
| Quad M | 4 | 8–10 | 130 | 500 |
| Quint M | 5 | 8–10 | 160 | 500 |
| Sextuple L | 6 | 10–12 | 200 | 800 |

**Einsatzgebiete:**
- Mastfuß: Fallen, Strecker, Reffleinen
- Cockpit-Eingang: Alle zum Cockpit geführten Leinen
- Sprayhood-Bereich: Leinensammlung vor der Winsch

### 3.6 Klüsen / Fairleads

#### 3.6.1 Geschlossene Klüsen (Closed Fairleads)

**Beschreibung:** Geschlossene Ring- oder Ovalführungen, durch die Festmacherleinen oder Ankerkette geführt werden. Die Leine kann nicht herausspringen.

**Konstruktionsmerkmale:**
- Guss oder Schmiedestück aus 316L Edelstahl oder Bronze
- Innenradien: R ≥ 4 × Leinendurchmesser (Mindestbiegeradius)
- Oberfläche poliert (Leinenschonung)
- Bolzenbefestigung durch Deck oder Schandeckel

**Typische Abmessungen:**

| Bezeichnung | Innenmaß [mm] | Leinen-∅ max. [mm] | SWL [kg] |
|---|---|---|---|
| S | 50 × 30 | 14 | 1.000 |
| M | 70 × 45 | 18 | 2.000 |
| L | 90 × 60 | 24 | 3.500 |
| XL | 120 × 80 | 32 | 5.000 |
| XXL | 150 × 100 | 40 | 8.000 |

#### 3.6.2 Offene Klüsen (Open Fairleads / Chocks)

**Beschreibung:** Offene Leinenführungen, die ein schnelles Einlegen und Entnehmen der Leine ermöglichen. Typisch als Bugklüsen und Heckklüsen.

**Typen:**
- **Hornklüsen**: Zwei aufstehende Hörner mit offener Mitte
- **Rollenklüsen**: Mit horizontaler oder vertikaler Rolle
- **Universalklüsen**: Kombiniert offen/geschlossen mit Klappe

#### 3.6.3 Rollenklüsen (Roller Fairleads)

**Beschreibung:** Klüsen mit integrierten Rollen zur Reibungsminderung. Ideal für hohe Lasten und häufiges Einlaufen/Auslaufen von Leinen.

**Konstruktionsmerkmale:**
- Edelstahl-Rahmen mit Delrin- oder Edelstahl-Rollen
- Horizontale, vertikale oder kombinierte Rollenanordnung
- Selbstschmierende Buchsen oder Kugellager
- SWL: 500–10.000 kg

### 3.7 Festmacherringe / Mooring Rings

**Beschreibung:** Stabile Ringe, die fest am Deck oder Schandeckel montiert sind, zur Aufnahme von Festmacherleinen, Fendern und Schleppverbindungen.

**Konstruktionsmerkmale:**
- Ringdurchmesser: 50–150 mm (innen)
- Materialdurchmesser: 8–20 mm Rundstahl 316L
- Befestigung: Durchgesteckt mit Grundplatte oder geschweißt
- Drehbar oder starr

**Typische Lasten:**

| Bootsklasse | Ring-∅ innen [mm] | Material-∅ [mm] | SWL [kg] |
|---|---|---|---|
| Jolle/Kleinboot | 40–50 | 6–8 | 300–600 |
| Fahrtensegler 8–12m | 60–80 | 10–12 | 1.000–2.000 |
| Blauwasser 12–16m | 80–100 | 12–16 | 2.000–4.000 |
| Yacht 16–20m | 100–120 | 16–20 | 4.000–6.000 |
| Superyacht 20m+ | 120–150 | 20–25 | 6.000–15.000 |

---

## 4. Produktlinien und Hersteller

### 4.1 Wichard (Frankreich) — Premium-Segment

**Unternehmensprofil:**
- Gegründet: 1919, Thiers, Frankreich
- Spezialisierung: Geschmiedete Edelstahl-Decksbeschläge
- Fertigungsverfahren: Warmschmieden (Forging) — höchste Festigkeit
- Material: Ausschließlich 316L und HR (High Resistance) Edelstahl
- Zertifizierungen: ISO 9001, Bureau Veritas, DNV

**Produktlinien Augenplatten:**

| Modell | Typ | Basis [mm] | SWL [kg] | Bruchlast [kg] | Material | Art.-Nr. |
|---|---|---|---|---|---|---|
| Wichard 6503 | Augenplatte geschweißt, flach | 50 × 30 | 500 | 2.000 | 316L | 6503 |
| Wichard 6504 | Augenplatte geschweißt, flach | 65 × 40 | 1.000 | 4.000 | 316L | 6504 |
| Wichard 6505 | Augenplatte geschweißt, flach | 80 × 50 | 2.000 | 8.000 | 316L | 6505 |
| Wichard 6506 | Augenplatte geschweißt, groß | 100 × 65 | 3.500 | 14.000 | 316L HR | 6506 |
| Wichard 6510 | Diamant-Augenplatte | 70 × 45 | 1.200 | 4.800 | 316L | 6510 |
| Wichard 6511 | Diamant-Augenplatte | 90 × 60 | 2.000 | 8.000 | 316L | 6511 |
| Wichard 6520 | Klapp-Augenplatte | 60 × 35 | 400 | 1.600 | 316L | 6520 |
| Wichard 6521 | Klapp-Augenplatte | 80 × 50 | 800 | 3.200 | 316L | 6521 |
| Wichard 6522 | Klapp-Augenplatte, groß | 100 × 65 | 1.500 | 6.000 | 316L HR | 6522 |

**Produktlinien U-Bolts:**

| Modell | Bügel-∅ [mm] | Weite [mm] | SWL [kg] | Bruchlast [kg] | Art.-Nr. |
|---|---|---|---|---|---|
| Wichard 6601 | 6 | 22 | 350 | 1.400 | 6601 |
| Wichard 6602 | 8 | 28 | 700 | 2.800 | 6602 |
| Wichard 6603 | 10 | 35 | 1.200 | 4.800 | 6603 |
| Wichard 6604 | 12 | 42 | 1.800 | 7.200 | 6604 |
| Wichard 6605 | 16 | 55 | 3.200 | 12.800 | 6605 |

**Besonderheiten Wichard:**
- Alle Beschläge warmgeschmiedet (nicht gegossen oder gestanzt)
- Proprietäre "HR" (High Resistance) Legierung: erhöhte Streckgrenze (>300 N/mm²)
- 100% chargenrückverfolgbar (Traceable)
- Jedes Teil mit Seriennummer und Bruchlast-Gravur
- 10 Jahre Garantie auf Material und Verarbeitung

### 4.2 Schaefer Marine (USA) — Industriequalität

**Unternehmensprofil:**
- Gegründet: 1960, New Bedford, Massachusetts, USA
- Spezialisierung: Robuste Decksbeschläge für Fahrtenyachten und gewerbliche Nutzung
- Fertigungsverfahren: Investmentguss und CNC-Bearbeitung
- Material: 316 Edelstahl, 17-4PH (für Hochlast)
- Zertifizierungen: ISO 9001, ABYC

**Produktlinien:**

| Modell | Typ | SWL [kg] | Bruchlast [kg] | Material | Art.-Nr. |
|---|---|---|---|---|---|
| Schaefer 78-01 | Pad Eye, klein | 450 | 1.800 | 316 SS | 78-01 |
| Schaefer 78-02 | Pad Eye, mittel | 900 | 3.600 | 316 SS | 78-02 |
| Schaefer 78-03 | Pad Eye, groß | 1.800 | 7.200 | 316 SS | 78-03 |
| Schaefer 78-04 | Pad Eye, XL | 3.200 | 12.800 | 316 SS | 78-04 |
| Schaefer 78-10 | Tang Plate, universal | 2.200 | 8.800 | 316 SS | 78-10 |
| Schaefer 78-11 | Tang Plate, heavy | 4.500 | 18.000 | 17-4PH | 78-11 |
| Schaefer 78-20 | Deck Organizer, 3-fach | 350/Leine | 1.400/L. | 316 SS | 78-20 |
| Schaefer 78-21 | Deck Organizer, 5-fach | 350/Leine | 1.400/L. | 316 SS | 78-21 |

### 4.3 Harken (USA/Italien) — Deck Organizers & Fairleads

**Unternehmensprofil:**
- Gegründet: 1967, Pewaukee, Wisconsin, USA
- Produktion: Italien (Limena) und USA
- Spezialisierung: Leinenführungssysteme, Blöcke, Deck-Hardware
- Fertigungsverfahren: Druckguss, CNC, Spritzguss (Delrin/Torlon)
- Zertifizierungen: ISO 9001

**Produktlinien Deck Organizers:**

| Modell | Konfiguration | Leinen-∅ [mm] | SWL/Leine [kg] | Material | Art.-Nr. |
|---|---|---|---|---|---|
| Harken 349 | Single Thru-Deck | 6–10 | 300 | 316L + Delrin | 349 |
| Harken 350 | Double Thru-Deck | 6–10 | 300 | 316L + Delrin | 350 |
| Harken 351 | Triple Thru-Deck | 6–10 | 300 | 316L + Delrin | 351 |
| Harken 352 | Triple Thru-Deck | 10–14 | 500 | 316L + Delrin | 352 |
| Harken 353 | Quad Thru-Deck | 8–12 | 400 | 316L + Delrin | 353 |
| Harken 354 | Sextuple Thru-Deck | 8–12 | 400 | 316L + Delrin | 354 |
| Harken 355 | Triple, Rolle | 10–14 | 600 | 316L + Torlon | 355 |
| Harken 356 | Quad, Rolle | 10–14 | 600 | 316L + Torlon | 356 |
| Harken 362 | Deck Organizer ESP | 8–14 | 800 | Aluminium/Torlon | 362 |

**Produktlinien Fairleads/Klüsen:**

| Modell | Typ | Leinen-∅ max [mm] | SWL [kg] | Material | Art.-Nr. |
|---|---|---|---|---|---|
| Harken 245 | Flip-Flop Fairlead | 12 | 400 | Aluminium | 245 |
| Harken 246 | Flip-Flop Fairlead | 16 | 600 | Aluminium | 246 |
| Harken 294 | Micro Pad Eye Fairlead | 8 | 200 | 316L | 294 |
| Harken 295 | Pad Eye Fairlead | 12 | 500 | 316L | 295 |
| Harken 338 | Midrange Bullseye | 14 | 600 | 316L + Delrin | 338 |
| Harken 339 | Midrange Bullseye, groß | 18 | 1.000 | 316L + Delrin | 339 |
| Harken 340 | Offshore Bullseye | 20 | 1.500 | 316L | 340 |

### 4.4 Ronstan (Australien) — RF-Serie Pad Eyes

**Unternehmensprofil:**
- Gegründet: 1953, Melbourne, Australien
- Spezialisierung: Leichtbau-Decksbeschläge, Regattahardware
- Fertigungsverfahren: CNC-gefräst, Kaltumformung
- Material: 316L, Aluminium 6082, Titan

**Produktlinien RF Pad Eyes:**

| Modell | Typ | SWL [kg] | Bruchlast [kg] | Material | Art.-Nr. |
|---|---|---|---|---|---|
| Ronstan RF601 | Pad Eye, flach, klein | 300 | 1.200 | 316L | RF601 |
| Ronstan RF602 | Pad Eye, flach, mittel | 600 | 2.400 | 316L | RF602 |
| Ronstan RF603 | Pad Eye, flach, groß | 1.200 | 4.800 | 316L | RF603 |
| Ronstan RF604 | Pad Eye, XL | 2.400 | 9.600 | 316L | RF604 |
| Ronstan RF610 | Pad Eye, Diamant | 800 | 3.200 | 316L | RF610 |
| Ronstan RF611 | Pad Eye, Diamant, groß | 1.500 | 6.000 | 316L | RF611 |
| Ronstan RF620 | Klapp-Pad Eye | 400 | 1.600 | 316L | RF620 |
| Ronstan RF621 | Klapp-Pad Eye, groß | 800 | 3.200 | 316L | RF621 |
| Ronstan RF650 | Shroud Plate (Tang) | 2.000 | 8.000 | 316L | RF650 |
| Ronstan RF651 | Shroud Plate, heavy | 4.000 | 16.000 | 316L | RF651 |
| Ronstan RF660 | Padeye, Titan | 1.500 | 6.000 | Ti Gr5 | RF660 |

**Besonderheiten Ronstan:**
- RF-Serie: durchgängig CNC-gefräst aus Vollmaterial
- Titan-Optionen für Regatta (Gewichtsersparnis 40%)
- Aluminium-Optionen für sportliche Fahrtenyachten
- Umfangreiche CAD-Bibliothek (STEP/IGES) frei verfügbar

### 4.5 Selden (Schweden) — Chainplates & Rigg-Beschläge

**Unternehmensprofil:**
- Gegründet: 1960, Göteborg, Schweden
- Spezialisierung: Rigg-Systeme, Masten, Rigg-Beschläge
- Fertigungsverfahren: Schmieden, CNC, Schweißen
- Material: 316L, Duplex 2205

**Produktlinien Chainplates/Wantenplatten:**

| Modell | Typ | Bootsgröße | SWL [t] | Bruchlast [t] | Material | Art.-Nr. |
|---|---|---|---|---|---|---|
| Selden 508-521 | Chainplate Set C20 | 6–8m | 1.5 | 6.0 | 316L | 508-521 |
| Selden 508-531 | Chainplate Set C30 | 8–11m | 2.5 | 10.0 | 316L | 508-531 |
| Selden 508-541 | Chainplate Set C40 | 11–14m | 4.0 | 16.0 | Duplex | 508-541 |
| Selden 508-551 | Chainplate Set C50 | 14–17m | 6.0 | 24.0 | Duplex | 508-551 |
| Selden 508-561 | Chainplate Set C60 | 17–20m | 8.0 | 32.0 | Duplex | 508-561 |
| Selden 508-570 | Tang Plate universal | variabel | 3.0 | 12.0 | 316L | 508-570 |
| Selden 508-580 | Toggle Assembly | variabel | 4.0 | 16.0 | 316L | 508-580 |

**Besonderheiten Selden:**
- Komplette Rigg-Systeme — Chainplates passend zum Mast/Rigg dimensioniert
- Wantenplatten-Sets bootsspezifisch vorkonfiguriert
- Duplex 2205 als Standard bei Booten > 12m
- Toggle-Systeme zur Gelenkigkeit am Wantenanschluss

### 4.6 Sea-Dog (USA) — Preissegment

**Unternehmensprofil:**
- Gegründet: 1980, Everett, Washington, USA
- Spezialisierung: Preiswerte Standard-Decksbeschläge
- Fertigungsverfahren: Investmentguss, Stanzen
- Material: 304 und 316 Edelstahl

**Produktlinien:**

| Modell | Typ | SWL [kg] | Bruchlast [kg] | Material | Art.-Nr. |
|---|---|---|---|---|---|
| Sea-Dog 0800001 | Pad Eye, klein | 200 | 800 | 316 SS | 0800001 |
| Sea-Dog 0800002 | Pad Eye, mittel | 500 | 2.000 | 316 SS | 0800002 |
| Sea-Dog 0800003 | Pad Eye, groß | 1.000 | 4.000 | 316 SS | 0800003 |
| Sea-Dog 0806001 | Klapp-Pad Eye | 250 | 1.000 | 316 SS | 0806001 |
| Sea-Dog 0810001 | U-Bolt, klein | 300 | 1.200 | 316 SS | 0810001 |
| Sea-Dog 0810002 | U-Bolt, mittel | 600 | 2.400 | 316 SS | 0810002 |
| Sea-Dog 0820001 | Fairlead, geschlossen | 400 | 1.600 | 316 SS | 0820001 |

### 4.7 Osculati (Italien) — Europäischer Standardmarkt

**Unternehmensprofil:**
- Gegründet: 1958, Segrate (Mailand), Italien
- Spezialisierung: Breites Sortiment für den europäischen Markt
- Fertigungsverfahren: Investmentguss, Import, Eigenproduktion
- Material: 316 Edelstahl, Messing verchromt

**Produktlinien (Auswahl):**

| Modell | Typ | SWL [kg] | Bruchlast [kg] | Material | Art.-Nr. |
|---|---|---|---|---|---|
| Osculati 39.310.xx | Pad Eye Serie | 200–2.500 | 800–10.000 | 316 SS | 39.310.xx |
| Osculati 39.320.xx | Klapp-Pad Eye | 200–1.000 | 800–4.000 | 316 SS | 39.320.xx |
| Osculati 39.330.xx | U-Bolt Serie | 300–2.000 | 1.200–8.000 | 316 SS | 39.330.xx |
| Osculati 39.600.xx | Klüsen, geschlossen | 500–3.000 | 2.000–12.000 | 316 SS | 39.600.xx |
| Osculati 39.610.xx | Klüsen, Rolle | 500–2.500 | 2.000–10.000 | 316 SS | 39.610.xx |
| Osculati 39.700.xx | Festmacherringe | 300–3.000 | 1.200–12.000 | 316 SS | 39.700.xx |

### 4.8 Sprenger (Deutschland) — Marine-Beschläge

**Unternehmensprofil:**
- Gegründet: 1873, Iserlohn, Deutschland
- Spezialisierung: Beschläge aus Edelstahl und Bronze
- Fertigungsverfahren: Warmschmieden, Feinguss
- Material: 316L, Bronze, Duplex

**Produktlinien (Auswahl):**

| Modell | Typ | SWL [kg] | Bruchlast [kg] | Material | Art.-Nr. |
|---|---|---|---|---|---|
| Sprenger 50 1360 | Pad Eye, geschmiedet | 600 | 2.400 | 316L | 50 1360 |
| Sprenger 50 1370 | Pad Eye, geschmiedet, groß | 1.500 | 6.000 | 316L | 50 1370 |
| Sprenger 50 1380 | Pad Eye, Diamant | 1.000 | 4.000 | 316L | 50 1380 |
| Sprenger 50 1420 | U-Bolt, geschmiedet | 800 | 3.200 | 316L | 50 1420 |
| Sprenger 50 1430 | U-Bolt, groß | 1.500 | 6.000 | 316L | 50 1430 |
| Sprenger 50 1500 | Chainplate, 8mm | 3.000 | 12.000 | Duplex | 50 1500 |
| Sprenger 50 1510 | Chainplate, 10mm | 4.500 | 18.000 | Duplex | 50 1510 |
| Sprenger 50 1520 | Chainplate, 12mm | 6.000 | 24.000 | Duplex | 50 1520 |

### 4.9 Materialvergleich der Hersteller

| Eigenschaft | 316L | Duplex 2205 | 17-4PH | Bronze CuSn8 | Titan Gr5 |
|---|---|---|---|---|---|
| Streckgrenze [N/mm²] | 205 | 450 | 725 | 170 | 830 |
| Zugfestigkeit [N/mm²] | 515 | 620 | 930 | 350 | 900 |
| Bruchdehnung [%] | 40 | 25 | 14 | 15 | 10 |
| Dichte [g/cm³] | 7.98 | 7.80 | 7.78 | 8.80 | 4.43 |
| Korrosionsbeständigkeit | Gut | Sehr gut | Mäßig | Gut (Seewasser) | Exzellent |
| Magnetisch | Nein | Leicht | Ja | Nein | Nein |
| Schweißbarkeit | Gut | Mittel | Schlecht | Gut | Spezial |
| Relative Kosten | 1.0× | 1.8× | 2.5× | 1.2× | 8–12× |

---

## 5. Montage und Installation

### 5.1 Montagevorbereitung

#### 5.1.1 Decksvorbereitung

**Schritt 1: Lage bestimmen und anzeichnen**
```
1. Lastrichtung analysieren (Zugwinkel, Kraftvektor)
2. Befestigungspunkte auf Deck markieren (Zentrierbohrung)
3. Unterdeck-Zugang prüfen (Backing Plate möglich?)
4. Kernmaterial identifizieren (Sandwich vs. Volllaminat)
5. Vorhandene Verstärkungen/Stringer lokalisieren
6. Abstand zu Deckskanten ≥ 50 mm sicherstellen
```

**Schritt 2: Unterdeck-Inspektion**
```
1. Zugang zur Unterseite sicherstellen
2. Laminatdicke messen (Ultraschall oder Bohrprobe)
3. Kernmaterial-Typ identifizieren
4. Vorhandene Schäden (Delamination, Osmose) ausschließen
5. Kabel-/Leitungsverläufe markieren (Kollisionsvermeidung)
6. Tragfähigkeit des Laminats bewerten
```

#### 5.1.2 Kernverstärkung (bei Sandwichdeck)

**Standardverfahren — Epoxid-Kernverstärkung:**

```
Werkzeuge:
  - Lochsäge (Ø = Kernverstärkungsbereich + 10mm)
  - Dremel mit Fräsaufsatz (alternativ)
  - Staubsauger
  - Injektionsspritze oder Füllpistole

Material:
  - West System 105 Harz + 205 Härter (oder äquivalent)
  - West System 404 High-Density Filler
  - Aceton (Reinigung)
  - Klebeband (Abdichtung)

Ablauf:
  1. Befestigungslöcher auf endgültiges Maß bohren
  2. Kern um jedes Loch im Radius von 15–20mm entfernen
     (Dremel, Haken-Werkzeug, Staubsauger)
  3. Hohlraum mit Aceton reinigen und trocknen lassen
  4. Unterseite mit Klebeband abdichten
  5. Epoxid + 404 Filler mischen (Konsistenz: Erdnussbutter)
  6. Hohlraum vollständig füllen (von oben injizieren)
  7. Aushärten lassen (24h bei 20°C)
  8. Befestigungslöcher auf Endmaß nachbohren
  9. Oberfläche planschleifen
```

**Kernverstärkung mit G10-Einsatz (Hochlast):**

```
Material:
  - G10/FR4-Platte, Dicke = Kerndicke
  - Epoxid-Kleber (Thixotrop)

Ablauf:
  1. Kernbereich kreisförmig oder rechteckig ausfräsen
  2. G10-Einsatz passend zuschneiden
  3. Einsatz mit thixotropem Epoxid einkleben
  4. Aushärten, planschleifen, bohren
```

### 5.2 Durchbolzung

#### 5.2.1 Schraubenauswahl

| Last pro Schraube [kg] | Mindest-Gewinde | Empfohlen | Material |
|---|---|---|---|
| bis 200 | M5 | M6 | 316L A4-70 |
| 200–500 | M6 | M8 | 316L A4-70 |
| 500–1.000 | M8 | M10 | 316L A4-80 |
| 1.000–2.000 | M10 | M12 | 316L A4-80 |
| 2.000–4.000 | M12 | M16 | 316L A4-80 / Duplex |
| über 4.000 | M16 | M20 | Duplex 2205 |

#### 5.2.2 Anzugsmomente (Torque Specs)

| Gewinde | Anzugsmoment [Nm] (316L, trocken) | Anzugsmoment [Nm] (316L, geschmiert) |
|---|---|---|
| M5 | 4–5 | 3–4 |
| M6 | 7–9 | 5–7 |
| M8 | 17–21 | 13–16 |
| M10 | 34–42 | 25–32 |
| M12 | 60–73 | 45–55 |
| M16 | 150–180 | 112–135 |
| M20 | 290–350 | 218–263 |

> **WICHTIG:** Edelstahl-Schrauben neigen zum Fressen (Galling). IMMER Anti-Seize-Paste (z.B. Tef-Gel, Lanocote, oder Loctite 8150) auf Gewinde auftragen!

#### 5.2.3 Backing Plate Installation

```
Reihenfolge:
  1. Beschlag auf Deck positionieren
  2. Durch alle Löcher gleichzeitig bohren (Deck + Beschlag als Schablone)
  3. Bohrungen entgraten (beide Seiten)
  4. Backing Plate untendrunter positionieren und ausrichten
  5. Sealant (Sikaflex 291i) in alle Bohrungen einbringen
  6. Sealant auf Beschlag-Unterseite aufbringen (geschlossene Raupe)
  7. Schrauben von oben durchstecken
  8. Unterlegscheiben + Muttern aufsetzen
  9. Über Kreuz anziehen (50%, 80%, 100%)
  10. Überschüssiges Sealant entfernen
  11. Endhärtung abwarten (Sikaflex: 7 Tage für volle Festigkeit)
```

### 5.3 Dichtungssysteme

#### 5.3.1 Sealant-Auswahl für Decksbeschläge

| Sealant | Anwendung | Haftung auf GFK | Haftung auf Edelstahl | UV-Beständigkeit | Demontierbar |
|---|---|---|---|---|---|
| Sikaflex 291i | Standard-Decksbeschläge | Sehr gut | Sehr gut | Gut | Ja (mit Mühe) |
| Sikaflex 295UV | UV-exponierte Bereiche | Sehr gut | Sehr gut | Exzellent | Ja (mit Mühe) |
| 3M 4200 | Leichte Beschläge | Gut | Gut | Gut | Ja |
| 3M 5200 | Permanente Montage | Exzellent | Exzellent | Gut | Nein (!) |
| Simson MSR-FU | Alternative zu Sikaflex | Sehr gut | Sehr gut | Gut | Ja |
| Butylband | Unter flachen Beschlägen | Mäßig | Mäßig | Gut | Leicht |

> **WARNUNG:** 3M 5200 nur verwenden, wenn die Verbindung NIEMALS gelöst werden soll. Für Decksbeschläge wird Sikaflex 291i empfohlen (demontierbar bei Bedarf).

#### 5.3.2 Sealant-Verarbeitung

```
Vorbereitung:
  1. Oberflächen reinigen (Sika Cleaner 205 oder Isopropanol)
  2. Primer auftragen wenn erforderlich:
     - GFK: Sika Primer 209 (nur bei alter/verschmutzter Oberfläche)
     - Aluminium: Sika Primer 209
     - Edelstahl: Kein Primer erforderlich
     - Teak: Sika Primer 209 + Aktivator
  3. Ablüftzeit beachten (Primer: 30–60 min)

Auftrag:
  1. Sealant-Kartusche auf Umgebungstemperatur bringen (15–25°C)
  2. Raupe auf Beschlag-Unterseite aufbringen (geschlossene Raupe, kein Ringmuster)
  3. Schraubenlöcher mit Sealant füllen (Dichtung der Bohrung)
  4. Beschlag aufsetzen und gleichmäßig anpressen
  5. Schrauben einsetzen und handfest anziehen
  6. Überschüssiges Sealant mit Spachtel entfernen
  7. 24h warten, dann Schrauben auf Endmoment nachziehen
  8. Erneut Sealant-Raupe am Rand glätten
```

### 5.4 Lastpfad-Analyse

#### 5.4.1 Prinzipien der Lasteinleitung

```
Regel 1: Der Lastpfad muss lückenlos sein
  Rigg-Kraft → Beschlag → Schrauben → Deck → Backing Plate →
  (Schott/Stringer → Rumpf) oder (Deck-Laminat allein)

Regel 2: Lasten breit verteilen
  Punktlast → über Beschlagfläche verteilen → über Backing Plate
  weiter verteilen → über Laminat in Struktur einleiten

Regel 3: Steifigkeitssprünge vermeiden
  Übergang Edelstahl → Laminat ist ein Steifigkeitssprung
  → Backing Plate als Übergang dimensionieren
  → Größere Backing Plate = sanfterer Übergang

Regel 4: Kernbereiche verstärken
  Sandwich-Kern nimmt keine Scherlasten auf
  → Kern im Befestigungsbereich IMMER ersetzen
  → Verstärkungsbereich mindestens 25mm über Beschlagkante

Regel 5: Schotts und Stringer nutzen
  Wann immer möglich, Beschlag über Schott/Stringer positionieren
  → Direkter Lastpfad ohne Biegung im Deck-Laminat
```

### 5.5 Spezielle Montagesituationen

#### 5.5.1 Montage auf Teakdeck

```
Problem: Teak bietet keine tragende Funktion, GFK-Laminat darunter ist tragend

Lösung:
  1. Teak im Beschlagbereich NICHT durchbohren (Wassereinbruch!)
  2. Teak ausfräsen (Beschlagform + 5mm Rand)
  3. GFK-Oberfläche freilegen und reinigen
  4. Beschlag direkt auf GFK montieren (Sealant-Bett)
  5. Beschlagrand mit Teak-Fugenmasse (Sikaflex 290DC) abdichten
  6. Alternativ: Beschlag-Unterfütterung auf Teak-Höhe
```

#### 5.5.2 Montage auf Aluminiumdeck

```
Besonderheiten:
  1. Galvanische Isolation: GFK-Zwischenlage oder Tef-Gel zwischen
     Edelstahl-Beschlag und Aluminium-Deck (ΔV > 0.5V!)
  2. Edelstahl-Schrauben mit Isolierhülsen verwenden
  3. Alternativ: Aluminium-Beschläge verwenden (gleiches Material)
  4. Sealant-Bett als zusätzliche Isolation
  5. NIEMALS Kupfer-basierte Anti-Seize-Paste verwenden!
     → Tef-Gel oder reines Lanolin verwenden
```

---

## 6. Anlagen-spezifische Zuordnung

### 6.1 Zuordnungstabelle: Beschlag nach Funktion

| Funktion | Empfohlener Beschlagtyp | SWL-Bereich [kg] | Zugwinkel | Mindest-SF |
|---|---|---|---|---|
| Genuaschot-Umlenkung | Diamant-Augenplatte | 500–2.000 | 15–45° | 4:1 |
| Spinnaker-Barberholer | Klapp-Augenplatte | 300–1.000 | 0–30° | 4:1 |
| Backstag-Aufholer | Tang Plate + Augenplatte | 1.000–5.000 | 60–90° | 4:1 |
| Oberwant-Anschluss | Interne Wantenplatte | 2.000–10.000 | 5–15° | 4:1 |
| Unterwant-Anschluss | Interne Wantenplatte | 1.000–5.000 | 10–25° | 4:1 |
| Vorstag-Anschluss | Bug-Tang Plate | 2.000–8.000 | 15–30° | 4:1 |
| Sicherheitsleine | Geschweißte Augenplatte | 300–800 | 30–90° | 5:1 |
| Festmacherleine | Klüse + Klampe | 500–5.000 | 0–30° | 3:1 |
| Fenderöse | Festmacherring | 200–500 | 60–90° | 3:1 |
| Reffleinen-Umlenkung | Deck Organizer (3-fach) | 300–800 | 30–60° | 4:1 |
| Fallen-Umlenkung | Deck Organizer + Block | 500–2.000 | 45–90° | 4:1 |
| Lazyjack-Befestigung | Kleine Augenplatte | 100–300 | 60–90° | 3:1 |
| Ankerkette-Führung | Geschlossene Klüse | 1.000–5.000 | 0–30° | 4:1 |
| Schleppöse | Schwerer U-Bolt + Backing | 3.000–15.000 | 0–30° | 6:1 |
| Bimini/Sprayhood-Halt | Kleine Augenplatte | 100–300 | 30–60° | 3:1 |

### 6.2 Zuordnung nach Bootsklasse

#### 6.2.1 Fahrtensegler 8–14m — Standardausstattung

```
Bug:
  - 2× Ankerklüse (geschlossen, M): SWL 2.000 kg
  - 2× Festmacherring (Bug): SWL 1.500 kg
  - 1× Vorstag-Tang Plate: SWL 4.000 kg
  - 2× Oberwant-Chainplate: SWL 4.000 kg

Mittschiff:
  - 2× Unterwant-Chainplate: SWL 2.500 kg
  - 4× Sicherheitsleinenösen: SWL 500 kg
  - 2× Genuaschot-Augenplatten: SWL 1.000 kg
  - 1× Deck Organizer 3-fach (Mastfuß): SWL 500 kg/Leine
  - 2× Spinnaker-Klapp-Augenplatten: SWL 500 kg

Cockpit:
  - 1× Deck Organizer 4-fach (Cockpit-Eingang): SWL 500 kg/Leine
  - 2× Genuaschot-Umlenkung: SWL 800 kg
  - 2× Festmacherring (Heck): SWL 1.500 kg
  - 2× Heckklüsen: SWL 1.500 kg
  - 1× Backstag-Tang Plate: SWL 3.000 kg
```

#### 6.2.2 Blauwasseryacht 12–18m — Erweiterte Ausstattung

```
Zusätzlich zum Fahrtensegler:
  - Schleppöse (Bug): SWL 8.000 kg, SF 6:1
  - Schleppöse (Heck): SWL 5.000 kg, SF 6:1
  - 6× Sicherheitsleinenösen (verstärkt): SWL 800 kg
  - Sturmfock-Augenplatten: SWL 2.000 kg
  - Trysegel-Anschlagpunkte: SWL 1.500 kg
  - Paradeanker-Augenplatte (Heck): SWL 3.000 kg
  - Davit-Augenplatten: SWL 500 kg × 4
```

#### 6.2.3 Regattayacht 8–20m — Leichtbau-Konfiguration

```
Fokus: Gewichtsminimierung, multifunktionale Beschläge

  - Titan-Augenplatten wo möglich (40% Gewichtsersparnis)
  - Aluminium-Deck-Organizer (Harken ESP-Serie)
  - Klapp-Augenplatten für selten genutzte Funktionen
  - Spinlock-Klemmen statt separater Beschlag + Klemme
  - Carbon-Backing-Plates (CFK) bei Hochlast
  - Minimale Anzahl, maximale Multifunktionalität
```

### 6.3 Zuordnung nach Lastfall

| Lastfall | Beschlag-Typ | Dimensionierung | Besonderheiten |
|---|---|---|---|
| Statisch (Dauerbelastung) | Geschweißte Augenplatte | SWL ≥ 2× Dauerlast | Ermüdungsfestigkeit beachten |
| Dynamisch (Wechselbelastung) | Geschmiedete Augenplatte | SWL ≥ 3× Spitzenlast | Kerbfaktor beachten |
| Stoß (Rucklast) | Durchgesteckter U-Bolt | SWL ≥ 4× Nennlast | Duktiles Material (316L) |
| Multidirektional | Augbolzen mit Kugelgelenk | SWL ≥ 2× max. Einzellast | Gelenkverschleiß prüfen |
| Korrosiv (Salzwasser dauernd) | Duplex 2205 oder Titan | Standard-SWL | Materialqualität entscheidend |

---

## 7. Fehlerbild-Atlas

### 7.1 FB-11.05-01: Wantenplatten-Rissbildung (Chainplate Cracking)

**Erscheinungsbild:**
Haarrisse oder offene Risse an der Wantenplatte, typisch am Übergang Platte/Decksdurchführung oder an Bohrungsrändern.

**Ursachen:**
- Spannungsrisskorrosion (SCC) durch Chlorid-Exposition
- Ermüdungsrisse durch zyklische Belastung (10⁶+ Zyklen)
- Unzureichende Radien am Lochrand (Kerbwirkung)
- Falsches Material (304 statt 316L verwendet)
- Überlastung durch falsch dimensionierte Platte

**Diagnose:**
```
Visuell:    Risse oft erst unter Lupe/10× sichtbar
            Rostfahnen an Rissaustrittsstellen
Magnetisch: Wirbelstromprüfung bei Verdacht
Ultraschall: Risslänge und -tiefe bestimmen
Farbeindringstoff: Oberflächenrisse sichtbar machen (z.B. Ardrox 996)
```

**Schweregrad:**
- **Leicht**: Haarrisse < 5mm, nur oberflächlich → Überwachung, nächste Saison austauschen
- **Mittel**: Risse 5–20mm oder durch halbe Wanddicke → Sofortiger Austausch vor nächster Fahrt
- **Schwer**: Risse > 20mm oder durch volle Wanddicke → SOFORTIGER AUSTAUSCH, Boot nicht segeln!

**AYDI-Confidence:** visual_medium (Risse auf Foto erkennbar) bis visual_low (Haarrisse kaum erkennbar)

### 7.2 FB-11.05-02: Augenplatten-Durchzug (Pad Eye Pull-Through)

**Erscheinungsbild:**
Die Augenplatte hat sich teilweise oder vollständig durch das Deck gezogen. Sichtbare Delaminierung und Aufwölbung des Laminats um die Befestigung.

**Ursachen:**
- Fehlende oder unterdimensionierte Backing Plate
- Kein Kernersatz bei Sandwich-Deck
- Schrauben-Korrosion (reduzierter Querschnitt)
- Überlastung (SWL überschritten)
- Laminat-Degradation (Osmose, UV)

**Diagnose:**
```
Visuell:    Aufwölbung, Risse im Gelcoat um Beschlag
            Wasserflecken unter Deck
Taktil:     Beschlag wackelt bei Belastung
Akustisch:  Knacken unter Last
Messung:    Spaltmaß zwischen Beschlag und Deck vergrößert
```

**Schweregrad:**
- **Leicht**: Gelcoat-Risse um Beschlag, Beschlag noch fest → Baldiger Austausch mit Verstärkung
- **Mittel**: Beschlag spürbar lose, Delamination sichtbar → Sofortige Stilllegung des Beschlags
- **Schwer**: Beschlag durchgezogen oder kurz davor → Sofortige Reparatur, alternative Lastpfade nutzen

### 7.3 FB-11.05-03: Deck-Delamination um Beschlagpunkt

**Erscheinungsbild:**
Großflächige Ablösung der oberen Deckschale vom Kern im Bereich um einen Decksbeschlag. Weiche, federnde Stelle bei Betreten.

**Ursachen:**
- Wassereinbruch durch undichte Beschlagmontage
- Frost-/Tauzyklen im durchfeuchteten Kern
- Fehlende Kernverstärkung bei Sandwich
- Unzureichende Sealant-Wartung
- Balsakern-Fäulnis (bei Balsa-Sandwich)

**Diagnose:**
```
Taktil:     "Schwamm"-Gefühl beim Betreten (ab 50mm Delamination)
Akustisch:  Klopftest — dumpfer Klang statt "klink" (gesund)
Visuell:    Verfärbungen auf Decksoberfläche, Wasserflecken unter Deck
Messung:    Feuchtemessung (Tramex Marine) → Werte > 20% = kritisch
```

**AYDI-Confidence:** visual_medium (großflächige Verfärbungen erkennbar) bis visual_insufficient (nur mit Instrumenten messbar)

### 7.4 FB-11.05-04: Schweißnaht-Versagen (Weld Failure)

**Erscheinungsbild:**
Riss oder Bruch an der Schweißnaht zwischen Auge und Grundplatte einer geschweißten Augenplatte.

**Ursachen:**
- Unzureichende Schweißnahtgüte (Poren, Bindefehler, Schlacke)
- Falsche Schweißparameter (zu heiß, zu kalt, falscher Zusatzwerkstoff)
- Zu kleines a-Maß der Kehlnaht
- Kerbwirkung am Schweißnahtübergang (fehlender Radius)
- Ermüdung bei zyklischer Belastung

**Diagnose:**
```
Visuell:    Risse am Nahtfuß, aufgerissene Naht
            Verfärbungen (Anlauffarben) deuten auf Überhitzung hin
            Porosität sichtbar bei geschliffener Naht
Magnetisch: Wirbelstromprüfung
Röntgen:    Bei Verdacht auf innere Fehler (professionell)
```

**Schweregrad:**
- **Leicht**: Oberflächenporen ohne Risse → Überwachen
- **Mittel**: Anriss am Nahtfuß < 3mm → Austausch planen
- **Schwer**: Durchgerissene Naht → SOFORTIGER AUSTAUSCH

### 7.5 FB-11.05-05: Ermüdungsrissbildung (Fatigue Cracking)

**Erscheinungsbild:**
Progressive Rissbildung an Augenplatten oder Wantenplatten nach vielen Lastzyklen. Risse starten typisch an Kerbstellen (Bohrungsrand, Schweißnahtfuß, Kantenübergang).

**Ursachen:**
- Zyklische Belastung über der Dauerfestigkeit
- Unzureichende Radien an Spannungskonzentratoren
- Material mit schlechter Ermüdungsfestigkeit
- Korrosionsunterstützte Ermüdung (Saltwater Fatigue)
- Vibrationsbelastung (Motor, Rigg-Schwingungen)

**Rissfortschrittsraten (typisch, Seewasser):**
```
316L Edelstahl:  da/dN ≈ 5×10⁻⁸ bis 5×10⁻⁶ mm/Zyklus
                 (bei ΔK = 10–30 MPa√m)

→ Ein 0.5mm Anfangsriss kann in 500.000 Zyklen (1–2 Saisons)
  auf kritische Länge wachsen
```

### 7.6 FB-11.05-06: Korrosion der Befestigungselemente

**Erscheinungsbild:**
Rostflecken, Lochfraß oder Materialverlust an Schrauben, Muttern oder Unterlegscheiben unter und in Decksbeschlägen.

**Ursachen:**
- Falsches Material (304 statt 316L, oder gar 18/8)
- Galvanische Korrosion (Edelstahl/Aluminium-Paarung)
- Spaltkorrosion in Gewindegängen
- Mangelnde Sealant-Abdichtung (Wasser in Bohrung)
- Chlorid-Konzentration durch Verdunstung

### 7.7 FB-11.05-07: Beschlag-Lockerung (Fastener Loosening)

**Erscheinungsbild:**
Beschlag wackelt spürbar, Schrauben drehen frei, Leine/Schäkel haben Spiel im Auge.

**Ursachen:**
- Setzverhalten (Relaxation) des Sealant-Bettes
- Vibrationsinduzierte Lockerung
- Kriechverhalten des GFK-Laminats unter Dauerlast
- Zu geringes Anzugsmoment bei Montage
- Fehlende Sicherungselemente (Nyloc, Federscheibe, Loctite)

### 7.8 FB-11.05-08: Laminat-Ausbruch um Befestigungsloch

**Erscheinungsbild:**
Kreisförmiger oder halbmondförmiger Ausbruch des Laminats um ein Befestigungsloch. Die Schraube hat das Laminat lokal zerstört.

**Ursachen:**
- Zu kleiner Randabstand (e < 3d)
- Zu kleiner Schraubenabstand (p < 4d)
- Fehlende Backing Plate
- Lochleibungsversagen (Bearing Failure)
- Schlagartige Überlastung

### 7.9 FB-11.05-09: Sealant-Versagen und Wassereinbruch

**Erscheinungsbild:**
Wasserflecken unter Deck im Bereich des Beschlags. Feuchter Kern. Schimmelbildung. Laminatverfärbung.

**Ursachen:**
- Sealant-Alterung (UV, Temperatur, mechanische Belastung)
- Falscher Sealant-Typ (Silikon auf GFK → schlechte Haftung)
- Unzureichende Oberflächenvorbereitung bei Montage
- Bewegung des Beschlags bricht Sealant-Verbindung
- Risse im Gelcoat als Eintrittspforte

### 7.10 FB-11.05-10: Galvanische Korrosion an Kontaktstellen

**Erscheinungsbild:**
Weiße oder grüne Korrosionsprodukte an der Kontaktstelle zwischen verschiedenen Metallen. Typisch: Edelstahl-Beschlag auf Aluminium-Deck.

**Ursachen:**
- Fehlende galvanische Isolation
- Elektrolyt (Seewasser) im Spalt
- Zu großer Potenzialunterschied (ΔV > 0.25V)
- Ungünstiges Flächenverhältnis (kleine Anode, große Kathode)

### 7.11 FB-11.05-11: Wantenplatten-Decksdurchführung — Undichtigkeit

**Erscheinungsbild:**
Chronisches Tropfen an der Wantenplatten-Decksdurchführung. Wasserflecken an Schotten. Salzablagerungen.

**Ursachen:**
- Manschette/Dichtung überaltert
- Wantenplatte bewegt sich unter Last (Dichtung arbeitet)
- Unzureichende Dichtungsfläche
- Falsche Dichtungsmethode

**Reparaturoptionen:**
```
Option 1 (Kurzfristig):
  Neopren-Manschette erneuern, Sikaflex 291i nachvergießen

Option 2 (Mittelfristig):
  Wichard Cover Plate montieren (Edelstahl-Abdeckung mit O-Ring)

Option 3 (Langfristig, empfohlen):
  GFK-Aufbau um Decksdurchführung:
  1. Bereich freibschleifen
  2. GFK-Flansch laminieren (3 Lagen Biax 300g)
  3. Epoxid-Verguss
  4. Neue Dichtung einsetzen
```

### 7.12 FB-11.05-12: Rissbildung im Deck um Hochlast-Beschlag

**Erscheinungsbild:**
Sternförmige Gelcoat-Risse ausgehend von Beschlag-Befestigungspunkten. Kann auf tiefere Laminatrisse hindeuten.

**Ursachen:**
- Unterdimensionierte Backing Plate (zu kleine Lastverteilung)
- Zu steifer Beschlag auf flexiblem Deck (Steifigkeitssprung)
- Fehlende Kernverstärkung
- Lokale Überlastung durch ungünstigen Zugwinkel

**Diagnose:**
```
Visuell:    Gelcoat-Sternrisse um Befestigungspunkte
Ultraschall: Laminatrisse unter Gelcoat detektieren
Klopftest:  Delamination im Umfeld erkennen
```

---

## 8. Troubleshooting-Entscheidungsbaum

### 8.1 Entscheidungsbaum: Beschlag wackelt

```
START: Beschlag wackelt bei manueller Prüfung
│
├── Schrauben sichtbar lose?
│   ├── JA → Schrauben nachziehen (Drehmoment prüfen)
│   │        └── Wackelt immer noch?
│   │            ├── JA → Gewinde ausgeleiert → Nächstgrößere Schraube
│   │            │        oder Gewindeeinsatz (Helicoil)
│   │            └── NEIN → Problem gelöst. Sealant erneuern.
│   │
│   └── NEIN → Laminat-Schaden prüfen
│       ├── Gelcoat-Risse um Beschlag?
│       │   ├── JA → Backing Plate prüfen (vorhanden? dimensioniert?)
│       │   │        → Kernverstärkung vorhanden?
│       │   │        → REPARATUR: Beschlag demontieren, Laminat verstärken,
│       │   │          Backing Plate vergrößern, neu montieren
│       │   └── NEIN → Sealant-Versagen
│       │            → Beschlag demontieren, reinigen, neu abdichten
│       └── Beschlag gebrochen?
│           └── JA → SOFORT STILLEGEN → Austausch erforderlich
```

### 8.2 Entscheidungsbaum: Wassereinbruch am Beschlag

```
START: Wasser tropft unter Deck am Beschlag
│
├── Welcher Beschlagtyp?
│   ├── Wantenplatte (Decksdurchführung)
│   │   ├── Manschette sichtbar beschädigt?
│   │   │   ├── JA → Manschette erneuern + Sealant
│   │   │   └── NEIN → Wantenplatte bewegt sich unter Last?
│   │   │       ├── JA → Flanschsystem nachrüsten (Wichard Cover)
│   │   │       └── NEIN → Sealant-Bett erneuern
│   │   └── Wasser kommt ZWISCHEN Platte und Schott?
│   │       → Schott-Laminierung prüfen, ggf. nachlaminieren
│   │
│   ├── Augenplatte / Pad Eye
│   │   ├── Schrauben sichtbar feucht?
│   │   │   ├── JA → Schraubenlöcher nicht abgedichtet
│   │   │   │   → Beschlag demontieren, Löcher trocknen,
│   │   │   │     mit Epoxid versiegeln, neu montieren mit Sealant
│   │   │   └── NEIN → Sealant-Bett gebrochen
│   │   │       → Vollständig neu abdichten
│   │   └── Deck federt um Beschlag?
│   │       → Delamination! → Großflächige Reparatur erforderlich
│   │
│   └── Deck Organizer / Leitöse
│       └── Durchführungsdichtung prüfen → erneuern
```

### 8.3 Entscheidungsbaum: Korrosion am Beschlag

```
START: Korrosion/Verfärbung sichtbar
│
├── Welche Farbe?
│   ├── Braun/Rot (Rost)
│   │   ├── Oberflächlich (Tea Staining)?
│   │   │   ├── JA → Reinigen mit Oxalsäure, passivieren
│   │   │   └── NEIN → Material prüfen
│   │   │       ├── 304 Edelstahl? → AUSTAUSCH gegen 316L
│   │   │       └── 316L? → Lochfraß → Beschlag ersetzen
│   │   └── An Schrauben?
│   │       → Schrauben-Material prüfen, ggf. durch A4-80 ersetzen
│   │
│   ├── Weiß (Aluminiumkorrosion)
│   │   └── Galvanische Korrosion → Isolation prüfen/nachrüsten
│   │
│   ├── Grün (Kupfer/Bronze-Patina)
│   │   ├── Gleichmäßig? → Normal bei Bronze, akzeptabel
│   │   └── Ungleichmäßig/tief? → Dezinkifizierung → AUSTAUSCH
│   │
│   └── Schwarz (Sulfidkorrosion)
│       └── Kontakt mit Antifouling-Wasser? → Isolation verbessern
```

### 8.4 Entscheidungsbaum: Beschlag-Auswahl bei Neubau/Retrofit

```
START: Neuer Beschlagpunkt benötigt
│
├── Welche Last wirkt?
│   ├── Berechne SWL nach Abschnitt 2.1
│   └── Bestimme Sicherheitsfaktor nach Tabelle 2.1.2
│
├── Welcher Zugwinkel?
│   ├── 0–30°  → Flache Augenplatte / Diamant-Pad Eye
│   ├── 30–60° → Standard-Augenplatte mit erhöhtem Auge
│   └── 60–90° → U-Bolt oder Augbolzen
│
├── Multidirektional?
│   ├── JA → Augbolzen mit Kugelgelenk
│   └── NEIN → Feste Augenplatte, ausgerichtet auf Hauptlast
│
├── Deck-Konstruktion?
│   ├── Sandwich → Kernverstärkung + Backing Plate obligatorisch
│   ├── Volllaminat → Backing Plate empfohlen ab SWL > 500 kg
│   └── Aluminium → Galvanische Isolation beachten
│
└── Budget/Qualitätsanspruch?
    ├── Premium → Wichard, Selden, Sprenger
    ├── Standard → Ronstan, Schaefer, Harken
    └── Budget → Sea-Dog, Osculati
```

### 8.5 Entscheidungsbaum: Wantenplatten-Inspektion

```
START: Jährliche Wantenplatten-Inspektion
│
├── Decksdurchführung dicht?
│   ├── JA → Weiter
│   └── NEIN → Sofort abdichten (siehe 7.11)
│
├── Sichtbare Risse an Platte?
│   ├── JA → Farbeindringstoff-Prüfung → Austausch!
│   └── NEIN → Weiter
│
├── Sichtbare Korrosion?
│   ├── Oberflächlich → Reinigen, passivieren, weiter beobachten
│   ├── Lochfraß → Austausch empfohlen
│   └── NEIN → Weiter
│
├── Bolzen/Schrauben-Zustand?
│   ├── Fest, kein Spiel → OK
│   ├── Leichtes Spiel → Nachziehen, Ursache klären
│   └── Loch vergrößert → Bolzen-Reparatur, ggf. Neubohrung
│
├── Schott-Laminierung intakt?
│   ├── JA → OK
│   └── Risse/Ablösung → Nachlaminierung erforderlich
│
└── ERGEBNIS:
    ├── Alle OK → Nächste Inspektion in 12 Monaten
    ├── Mängel behoben → Kontrollinspektion in 6 Monaten
    └── Schwere Mängel → SOFORTIGE Maßnahme
```

---

## 9. FAQ — Häufige Fragen

### F1: Welcher Sicherheitsfaktor gilt für Augenplatten?

**Antwort:** Der Mindest-Sicherheitsfaktor beträgt **4:1** (SWL = Bruchlast / 4) für Standard-Rigg-Beschläge. Für Schleppösen gilt **6:1**, für Sicherheitsgurt-Anschlagpunkte **5:1** (nach EN 795). Festmacherbeschläge mit vorwiegend statischer Belastung können mit **3:1** dimensioniert werden, wenn keine Stoßlasten auftreten.

### F2: Muss ich immer eine Backing Plate verwenden?

**Antwort:** Bei **Sandwich-Decks** ist eine Backing Plate (mit Kernverstärkung) **obligatorisch** für alle lasttragenden Beschläge. Bei **Volllaminat-Decks** ist eine Backing Plate empfohlen ab einer SWL > 500 kg. Für leichte Beschläge (z.B. Lazyjack-Ösen, SWL < 200 kg) auf Volllaminat kann auf eine Backing Plate verzichtet werden, wenn die Laminatdicke ≥ 6 mm beträgt und mindestens 4 Schrauben verwendet werden.

### F3: 316 oder 316L — macht das einen Unterschied?

**Antwort:** Ja. **316L** (Low Carbon, C ≤ 0.03%) ist **immer vorzuziehen** für marine Anwendungen. Der reduzierte Kohlenstoffgehalt verhindert interkristalline Korrosion nach Schweißarbeiten. Standard-316 (C ≤ 0.08%) kann in der Wärmeeinflusszone von Schweißnähten anfällig für Sensibilisierung werden. Die mechanischen Eigenschaften sind nahezu identisch. Preisunterschied: < 5%.

### F4: Wann sollte ich Duplex 2205 statt 316L wählen?

**Antwort:** Duplex 2205 bietet doppelte Streckgrenze (450 vs. 205 N/mm²) und deutlich bessere Korrosionsbeständigkeit (PREN 35 vs. 24). Empfohlen für: Wantenplatten ab 12m Bootslänge, Schleppösen, alle Beschläge im ständig nassen Bereich, tropische Gewässer (höhere Chlorid-Konzentration). Nachteil: ca. 80% teurer, schwieriger zu schweißen.

### F5: Kann ich Edelstahl-Beschläge auf Aluminium-Decks montieren?

**Antwort:** Ja, aber **nur mit galvanischer Isolation**. Edelstahl und Aluminium bilden ein galvanisches Element (ΔV ≈ 0.7V), das zur schnellen Zerstörung des Aluminiums führt. Gegenmaßnahmen: (1) GFK-Zwischenlage zwischen Beschlag und Deck, (2) Isolierhülsen in allen Schraubenlöchern, (3) Tef-Gel als Kontaktpaste, (4) Sealant-Bett als zusätzliche Isolation. Alternative: Aluminium-Beschläge verwenden.

### F6: Wie oft müssen Wantenplatten inspiziert werden?

**Antwort:** **Jährlich** visuelle Inspektion (Decksdurchführung, sichtbare Oberfläche). Alle **5 Jahre** umfassende Inspektion (Verkleidungen entfernen, Farbeindringstoff-Prüfung, Bolzen prüfen). Bei Booten > 20 Jahre oder nach schweren Stürmen: **sofortige Komplett-Inspektion**. Aluminium-Segelyachten: Inspektion alle **3 Jahre** (beschleunigte Korrosion möglich).

### F7: Mein Wantenplatten-Durchbruch tropft — schnelle Lösung?

**Antwort:** Kurzfristig: Butylband um die Decksdurchführung wickeln und mit Sealant überziehen. Dies ist eine **Notlösung für maximal eine Saison**. Langfristig: Dichtung komplett erneuern. Empfohlen: Wichard Cover Plate System oder GFK-Flansch-Aufbau (siehe Fehlerbild 7.11).

### F8: Welchen Kleber/Sealant für Decksbeschläge?

**Antwort:** Standardempfehlung: **Sikaflex 291i** (PU-Sealant, elastisch, demontierbar, gute Haftung auf GFK und Edelstahl). Für UV-exponierte Bereiche: **Sikaflex 295UV**. **Niemals** Silikon verwenden (schlechte Haftung auf GFK, verhindert spätere Lackierung). **Vorsicht** mit 3M 5200 (permanente Verklebung, Demontage zerstört Gelcoat).

### F9: Wie erkenne ich, ob meine Schrauben 316L sind?

**Antwort:** Kennzeichnung auf dem Schraubenkopf: **A4-70** oder **A4-80** = 316/316L Edelstahl (A4 = austenitisch, AISI 316). **A2-70** = 304 Edelstahl — **nicht marinegerecht für dauerhafte Salzwasser-Exposition**. Ohne Markierung: Magnettest (316L ist nicht magnetisch, 304 leicht magnetisch nach Kaltverformung). Im Zweifel: austauschen gegen gekennzeichnete Schrauben.

### F10: Pad Eye geschweißt oder geschraubt — was ist besser?

**Antwort:** **Geschweißt** bietet höhere Festigkeit und kompaktere Bauform, setzt aber eine qualifizierte Schweißung voraus (WIG/TIG, Schutzgas, korrekte Parameter). **Geschraubt** (Augbolzen) bietet einfacheren Austausch und Inspektion, hat aber geringere Festigkeit und erfordert regelmäßige Vorlastkontrolle. Empfehlung: geschweißt für dauerhafte Hochlast-Anwendungen, geschraubt für flexible/temporäre Anwendungen.

### F11: Wie berechne ich die nötige Augenplatten-Größe?

**Antwort:** 
1. Maximale Last bestimmen (inkl. dynamischer Faktor)
2. Sicherheitsfaktor anwenden → erforderliche Bruchlast
3. Beschlag mit entsprechender Bruchlast wählen
4. Zugwinkel berücksichtigen (Abschnitt 2.1.3)
5. Backing Plate dimensionieren (Abschnitt 2.1.4)
6. Schraubenanzahl und -größe festlegen (Abschnitt 5.2)

### F12: Was ist ein Toggle und wozu brauche ich ihn?

**Antwort:** Ein Toggle (Gabelgelenk) ist ein Zwischenglied zwischen Want und Wantenplatte, das eine Gelenkigkeit in einer Ebene ermöglicht. Ohne Toggle wird die Wantenplatte durch seitliche Auslenkung des Wants auf Biegung beansprucht, was zu Ermüdungsbrüchen führt. **Toggles sind obligatorisch bei allen Oberwant- und Vorstag-Anschlüssen**. Bei Unterwanten optional, aber empfohlen.

### F13: Kann ich Carbon-Backing-Plates verwenden?

**Antwort:** Grundsätzlich ja, aber mit Einschränkungen: CFK (Carbon) ist elektrisch leitfähig und bildet mit Edelstahl ein galvanisches Element. Isolation zwischen CFK-Backing-Plate und Edelstahl-Schrauben ist zwingend erforderlich. Vorteil: 60% leichter als Edelstahl bei vergleichbarer Steifigkeit. Einsatz vorwiegend im Regattabereich. Für Fahrtenyachten wird Edelstahl oder Aluminium empfohlen.

### F14: Wie viel Sealant ist richtig?

**Antwort:** Die Sealant-Schicht unter dem Beschlag sollte **2–3 mm** dick sein (nach Aushärtung ca. 1–2 mm durch Zusammendrücken). Zu wenig: keine Dichtung. Zu viel: Beschlag schwimmt auf Sealant, ungleichmäßige Kompression. Alle Schraubenlöcher vollständig mit Sealant füllen. Geschlossene Raupe um den gesamten Beschlagrand — keine Lücken.

### F15: Was bedeutet SWL, WLL und MBL?

**Antwort:**
- **SWL** (Safe Working Load): Maximale Last für den normalen Betrieb. Veraltet, aber weit verbreitet.
- **WLL** (Working Load Limit): Moderner Ersatz für SWL, normativ korrekt nach EN 1677.
- **MBL** (Minimum Breaking Load): Garantierte Mindest-Bruchlast. MBL = WLL × Sicherheitsfaktor.
- Beispiel: WLL 1.000 kg, SF 4:1 → MBL 4.000 kg.

### F16: Sind geschmiedete Beschläge wirklich besser als gegossene?

**Antwort:** Ja, signifikant. **Schmieden** (Forging) verdichtet das Gefüge, richtet die Kristallstruktur in Belastungsrichtung aus und eliminiert Lunker und Poren. Die Ermüdungsfestigkeit geschmiedeter Teile ist 30–50% höher als bei Guss. **Guss** (Investment Casting) kann Poren, Einschlüsse und Dendritenstrukturen enthalten, die als Rissausgangspunkte wirken. Für sicherheitskritische Anwendungen (Wantenplatten, Schleppösen): **immer geschmiedet**.

### F17: Meine Klappaugenplatte klemmt — was tun?

**Antwort:** Ursachen: Salzablagerungen im Gelenk, Korrosion am Schwenkbolzen, Verformung durch Überlastung. Lösung: (1) Mit Süßwasser und feiner Bürste reinigen, (2) Schwenkbolzen mit Lanolin oder Tef-Gel schmieren, (3) Wenn verbogen: austauschen, nicht richten (Materialermüdung). Präventiv: nach jedem Salzwassereinsatz mit Süßwasser spülen.

### F18: Welche Beschläge brauche ich für Bluewater-Sailing zusätzlich?

**Antwort:** Gegenüber Küstensegeln benötigen Blauwasseryachten: (1) Schleppöse Bug (SWL ≥ 8t), (2) Schleppöse Heck (SWL ≥ 5t), (3) Sturmfock-Augenplatten (vorlich der Wanten), (4) Trysegel-Anschlagpunkte, (5) Paradeanker-Beschlag (Heck), (6) Verstärkte Sicherheitsleinenösen (6+ Stück, SWL ≥ 800 kg), (7) Alle Beschläge in Duplex 2205 oder höher.

### F19: Kann ich Beschläge selbst schweißen?

**Antwort:** Grundsätzlich möglich, aber für sicherheitskritische Beschläge wird dringend von DIY abgeraten. Edelstahl-Schweißen erfordert: (1) WIG/TIG-Schweißgerät mit Schutzgas (Argon), (2) Formiergas auf der Rückseite, (3) Richtiger Zusatzwerkstoff (316LSi für 316L), (4) Erfahrung mit dünnwandigen Edelstahlteilen, (5) Nachbehandlung (Beizen, Passivieren). Qualitätskontrolle: Farbeindringstoffprüfung der Schweißnaht.

### F20: Wie wirkt sich der Zugwinkel auf die Schraubenlast aus?

**Antwort:** Bei einem Zugwinkel von 0° (horizontal) wirkt reine Scherkraft auf die Schrauben. Bei 90° (vertikal) wirkt reiner Zug plus Hebelmoment. Die kritischsten Winkel sind 45–60°, da hier sowohl Scher- als auch Zugkomponente hoch sind UND ein signifikantes Hebelmoment entsteht. Siehe Tabelle in Abschnitt 2.1.3 für exakte Aufschlüsselung.

### F21: Edelstahl oder Bronze für Festmacherringe?

**Antwort:** Beide Materialien sind marinegerecht. **316L Edelstahl**: höhere Festigkeit, geringeres Gewicht, modernes Erscheinungsbild, empfindlich gegen Spaltkorrosion. **Bronze (CuSn8)**: hervorragende Seewasserbeständigkeit, selbstheilende Patina (Schutzschicht), traditionelles Erscheinungsbild, schwerer, etwas geringere Festigkeit. Für **reine Funktion**: 316L. Für **Tradition/Optik**: Bronze. In **tropischen Gewässern**: Bronze leicht im Vorteil (keine Spaltkorrosion).

### F22: Was kostet ein kompletter Wantenplatten-Austausch?

**Antwort:** Orientierungswerte (Material + Arbeitskosten):
- 8–10m Segelyacht, 6 Chainplates: 2.000–4.000 EUR
- 10–13m Segelyacht, 8 Chainplates: 3.500–7.000 EUR
- 13–16m Segelyacht, 10 Chainplates: 6.000–12.000 EUR
- 16m+ Segelyacht, 10+ Chainplates: 10.000–25.000 EUR
Die Kosten hängen stark von der Zugänglichkeit ab. Verkleidungen entfernen und wieder montieren kann 30–50% der Gesamtkosten ausmachen.

### F23: Wie erkenne ich eine unterdimensionierte Augenplatte?

**Antwort:** Warnzeichen: (1) Gelcoat-Sternrisse um die Befestigungslöcher, (2) Beschlag wird warm unter Last (Reibung), (3) Sichtbare Verformung des Auges unter Betriebslast, (4) Schrauben lockern sich regelmäßig, (5) Backing Plate hat sich in das Laminat gedrückt (Abdruck sichtbar). Bei diesen Zeichen: Last berechnen, Beschlag gemäß Abschnitt 2.1 neu dimensionieren.

### F24: Gibt es eine Faustregel für die Backing-Plate-Größe?

**Antwort:** Faustregel: Die Backing Plate sollte mindestens die **dreifache Fläche** der Beschlag-Grundplatte haben. Beispiel: Augenplatte 50 × 30 mm (15 cm²) → Backing Plate mindestens 45 cm² → ca. 70 × 70 mm. Bei Sandwich-Decks: **fünffache Fläche** empfohlen. Die Dicke der Backing Plate: mindestens die Hälfte der Beschlag-Grundplattendicke (z.B. Beschlag 4 mm → Backing Plate ≥ 3 mm Edelstahl).

### F25: Wie prüfe ich Wantenplatten ohne sie auszubauen?

**Antwort:** Nicht-invasive Prüfmethoden: (1) **Visuelle Inspektion** der Decksdurchführung (Risse, Verfärbungen, Undichtigkeit), (2) **Farbeindringstoff** (Ardrox 996) auf sichtbare Oberflächen auftragen, (3) **Klopftest** um den Beschlag (Delamination erkennen), (4) **Feuchtemessung** (Tramex) im Umfeld, (5) **Rig-Tuning** beobachten (ungleichmäßige Spannung kann auf verformte Chainplate hindeuten). Für eine vollständige Prüfung ist jedoch der Ausbau unumgänglich — empfohlen spätestens alle 15 Jahre.

---

## 10. Glossar

### A

**Augenplatte (Pad Eye)**
Decksbeschlag mit einem geschlossenen oder offenen Auge zur Aufnahme von Schäkeln, Karabinern oder Leinen. Dient als stationärer Lasteinleitungspunkt.

**Augbolzen (Eye Bolt)**
Schraube mit geschlossenem Auge (Öse) anstelle eines Schraubenkopfes. Wird in ein Gewinde oder eine Durchgangsbohrung eingesetzt.

**Anlauffarbe (Heat Tint)**
Verfärbung von Edelstahl durch Hitzeeinwirkung beim Schweißen. Farben von goldgelb (200°C) über blau (300°C) bis grau (>400°C). Leichte Anlauffarben sind akzeptabel, dunkelblau bis grau deutet auf Überhitzung und reduzierte Korrosionsbeständigkeit hin.

**A4-70 / A4-80 (Stainless Steel Grade)**
Werkstoffklasse für austenitische Edelstahl-Verbindungselemente. A4 = AISI 316 / 316L (molybdänhaltig, seewassertauglich). 70/80 = Festigkeitsklasse (700 / 800 N/mm² Zugfestigkeit).

### B

**Backing Plate (Gegenplatte, Verstärkungsplatte)**
Metallplatte, die unter dem Deck angebracht wird, um die Kraft eines Decksbeschlags großflächig in das Laminat einzuleiten. Verhindert lokale Überlastung und Pull-Through.

**Bearing Stress (Lochleibungsspannung)**
Flächenpressung zwischen Bolzen/Schraube und der Bohrungswand im Laminat. Kritisch für die Dimensionierung von Bolzenverbindungen in GFK.

**Bruchlast (Breaking Load / MBL)**
Die Last, bei der ein Beschlag oder Befestigungselement versagt (bricht, reißt, sich dauerhaft verformt). Wird im Zerstörungstest ermittelt.

**Bügelbolzen (U-Bolt)**
U-förmig gebogener Edelstahlbolzen, auf eine Grundplatte geschweißt oder durchgesteckt, als Befestigungspunkt für Blöcke, Schäkel und Leinen.

### C

**Chainplate (Wantenplatte)**
Hochfester Edelstahlflachstahl, der die Rigglast (Wanten, Stage) in die Rumpfstruktur einleitet. Eines der am höchsten belasteten Bauteile einer Segelyacht.

**Core Reinforcement (Kernverstärkung)**
Ersatz des weichen Kernmaterials (Balsa, Schaum) in Sandwich-Konstruktionen durch hochfestes Material (Epoxid-Filler, G10) im Bereich von Beschlagbefestigungen.

### D

**Dauerfestigkeit (Fatigue Limit)**
Die Spannungsamplitude, unterhalb derer ein Material theoretisch unendlich viele Lastzyklen erträgt. Bei Edelstahl 316L ca. 35% der Zugfestigkeit.

**Decksdurchführung (Deck Penetration)**
Öffnung im Deck, durch die ein Bauteil (Wantenplatte, Kabel, Rohrleitungen) geführt wird. Kritischer Punkt für Dichtheit.

**Diamant-Basis (Diamond Base)**
Rautenförmige Grundplatte einer Augenplatte mit vier Befestigungspunkten an den Ecken. Optimierte Lastverteilung für unidirektionale Zugbelastung.

**Duplex 2205 (1.4462)**
Austenitisch-ferritischer Edelstahl mit doppelter Streckgrenze gegenüber 316L und deutlich besserer Chlorid-Beständigkeit. Standard für hochbelastete marine Beschläge.

### E

**Ermüdungsbruch (Fatigue Fracture)**
Bruch eines Bauteils nach wiederholter zyklischer Belastung unterhalb der statischen Bruchlast. Typische Versagensart bei Decksbeschlägen nach vielen Jahren.

### F

**Fairlead (Klüse, Leinauge)**
Führungsbeschlag zur kontrollierten Umlenkung von Festmacherleinen, Ankerketten oder Schoten. Kann offen, geschlossen oder mit Rollen versehen sein.

**Formiergas (Purge Gas)**
Schutzgas (typisch Argon oder Argon/Stickstoff-Gemisch) auf der Rückseite einer Schweißnaht, verhindert Oxidation und erhält die Korrosionsbeständigkeit des Edelstahls.

### G

**Galling (Fressen)**
Kaltverschweißung von Edelstahl-Gewinden beim Anziehen ohne Schmiermittel. Führt zum Festfressen und Zerstörung der Verbindung. Prävention: immer Anti-Seize verwenden.

**Galvanische Korrosion (Galvanic Corrosion)**
Elektrochemischer Abtrag des unedleren Metalls in einer Kontaktpaarung zweier verschiedener Metalle in Gegenwart eines Elektrolyten (Seewasser).

**Gelcoat-Sternriss (Gelcoat Star Crack)**
Sternförmige Risse im Gelcoat, ausgehend von einem Belastungspunkt. Können auf Laminatschäden darunter hindeuten.

### H

**Helicoil (Gewindeeinsatz)**
Spiralförmiger Gewindeeinsatz aus Edelstahldraht zur Reparatur von beschädigten Gewinden oder zur Verstärkung von Gewinden in weichen Materialien.

### K

**Kerbfaktor (Stress Concentration Factor, K_t)**
Verhältnis der lokalen Maximalspannung zur Nennspannung an einer geometrischen Diskontinuität (Bohrung, Schweißnahtübergang, Kerbe).

**Kernverstärkung** → siehe Core Reinforcement

**Klüse** → siehe Fairlead

### L

**Lastpfad (Load Path)**
Der Weg, den eine Kraft von ihrem Angriffspunkt durch die Struktur bis zur Abstützung (Rumpf, Kiel) nimmt. Muss lückenlos und ausreichend dimensioniert sein.

**Lochleibung** → siehe Bearing Stress

### M

**MBL (Minimum Breaking Load)**
Garantierte Mindest-Bruchlast. MBL = WLL × Sicherheitsfaktor.

### N

**Nyloc-Mutter (Self-Locking Nut)**
Mutter mit integriertem Kunststoffeinsatz (Nylon), der ein selbständiges Lösen unter Vibration verhindert. Maximale Einsatztemperatur: 120°C.

### P

**Pad Eye** → siehe Augenplatte

**PREN (Pitting Resistance Equivalent Number)**
Kennzahl für die Lochfraßbeständigkeit von Edelstahl. PREN = %Cr + 3.3 × %Mo + 16 × %N. 316L: PREN ≈ 24. Duplex 2205: PREN ≈ 35. Für Seewasser: PREN > 25 empfohlen.

**Pull-Through (Durchzug)**
Versagen, bei dem ein Beschlag sich durch das Deck zieht, weil die Flächenpressung die Druckfestigkeit des Laminats überschreitet.

### S

**Schäkel (Shackle)**
U-förmiges Verbindungselement mit Bolzenverschluss. Verbindet Augenplatten, Blöcke, Wanten und andere Rigg-Elemente.

**SWL (Safe Working Load)**
Maximal zulässige Last für den normalen Betrieb. SWL = Bruchlast / Sicherheitsfaktor.

**Spaltkorrosion (Crevice Corrosion)**
Korrosionsform in engen Spalten (Schraubenbohrungen, Kontaktflächen), wo stagnierendes Seewasser einen Sauerstoff-Konzentrationsunterschied erzeugt.

**Spannungsrisskorrosion (Stress Corrosion Cracking, SCC)**
Rissbildung unter der kombinierten Wirkung von Zugspannung und korrosivem Medium (Chlorid). Besonders kritisch bei austentischen Edelstählen in warmem Seewasser.

### T

**Tang Plate (Anschlussplatte)**
Flache Verbindungsplatte zwischen Rigg-Element (Want, Stag) und Strukturelement (Wantenplatte, Schott). Dient der kontrollierten Kraftübertragung über Bolzenverbindungen.

**Tef-Gel**
Teflonbasierte Anti-Korrosions-Paste für galvanisch kritische Kontakte. Isoliert und schmiert gleichzeitig. Standard bei Edelstahl-auf-Aluminium-Verbindungen.

**Toggle (Gabelgelenk)**
Gelenkverbindung zwischen Want/Stag und Wantenplatte/Tang Plate. Ermöglicht Winkelbewegung und verhindert Biegung der Wantenplatte.

### W

**Wantenplatte** → siehe Chainplate

**WLL (Working Load Limit)**
Moderner, normkonformer Ersatz für SWL. Maximale Betriebslast nach EN 1677.

**Wöhler-Kurve (S-N Curve)**
Diagramm, das die ertragbare Spannungsamplitude über die Anzahl der Lastzyklen darstellt. Grundlage für die Ermüdungsberechnung.

---

## 11. Schnell-Referenz

### 11.1 Augenplatten — Kurzauswahl

| Anwendung | Beschlag | SWL min. | SF | Material min. | Backing Plate |
|---|---|---|---|---|---|
| Genuaschot | Diamant Pad Eye M/L | 1.000 kg | 4:1 | 316L | Ja |
| Spinnaker | Klapp Pad Eye M | 500 kg | 4:1 | 316L | Ja (Sandwich) |
| Sicherheitsleine | Geschweißter Pad Eye | 500 kg | 5:1 | 316L | Ja |
| Lazyjack | Kleiner Pad Eye | 150 kg | 3:1 | 316L | Optional |
| Schleppöse | Schwerer U-Bolt | 5.000 kg | 6:1 | Duplex 2205 | Obligatorisch |

### 11.2 Wantenplatten — Kurzauswahl nach Bootslänge

| Bootslänge | Plattenstärke | Breite | Material | Bolzen min. |
|---|---|---|---|---|
| 8–10m | 6–8 mm | 40–50 mm | 316L | 3× M10 |
| 10–13m | 8–10 mm | 50–60 mm | 316L / Duplex | 4× M10 |
| 13–16m | 10–12 mm | 60–70 mm | Duplex 2205 | 5× M12 |
| 16–20m | 12–15 mm | 70–80 mm | Duplex 2205 | 6× M12 |

### 11.3 Sealant — Kurzauswahl

| Situation | Sealant | Primer nötig? |
|---|---|---|
| Standard-Beschlag auf GFK | Sikaflex 291i | Nein (frisches GFK) |
| UV-exponierter Beschlag | Sikaflex 295UV | Nein |
| Beschlag auf Aluminium | Sikaflex 291i + Tef-Gel | Sika Primer 209 |
| Permanente Montage | 3M 5200 | Nein |
| Teakdeck-Beschlag | Sikaflex 291i + 290DC (Teak) | Sika Primer 209 |

### 11.4 Schrauben — Kurzauswahl

| Last gesamt [kg] | Schrauben min. | Gewinde | Material |
|---|---|---|---|
| bis 500 | 4× | M6 | A4-70 |
| 500–1.500 | 4× | M8 | A4-70 |
| 1.500–3.000 | 4–6× | M10 | A4-80 |
| 3.000–6.000 | 6× | M12 | A4-80 |
| über 6.000 | 6–8× | M16 | Duplex |

---

## ANHANG A — Fallstudien

### Fallstudie A1: Wantenplatten-Bruch Bavaria 38 — Riggverlust auf See

**Yacht:** Bavaria 38, Baujahr 1998, Ostsee
**Vorfall:** Oberwant-Chainplate (Steuerbord) gebrochen bei 25 kt Am-Wind-Kurs. Vollständiger Riggverlust.

**Analyse:**
```
Material:     316 Edelstahl (nicht 316L)
Dicke:        8 mm (unterdimensioniert für 38 Fuß)
Alter:        22 Jahre, nie ausgetauscht
Inspektion:   Keine dokumentierte Inspektion der Wantenplatten
Bruchbild:    Ermüdungsbruch, ausgehend von Bohrungsrand
              Rissfortschritt über ca. 70% des Querschnitts
              Restbruchfläche nur 30% → Platte war fast vollständig
              gerissen BEVOR der finale Bruch erfolgte
```

**Ursache:** Kombination aus:
1. Unzureichende Dimensionierung (8 mm für 38 Fuß, Minimum 10 mm)
2. 22 Jahre zyklische Belastung ohne Inspektion
3. Kerbwirkung am Bohrungsrand (scharfe Kante, kein Radius)
4. Mögliche Sensibilisierung durch 316 (statt 316L) nach Wärmeeinwirkung

**Lehren:**
- Wantenplatten nach 15 Jahren zwingend zerstörungsfrei prüfen
- Bei Booten vor 2005: Material-Zertifikat anfordern oder Materialprüfung
- Bohrungen immer mit Radius (R ≥ 1 mm) entgraten
- Bavaria 38: Nachrüstung auf 10 mm Duplex 2205 empfohlen

### Fallstudie A2: Pad-Eye-Durchzug — Spinnaker-Verlust Beneteau First 36.7

**Yacht:** Beneteau First 36.7, Baujahr 2004, Mittelmeer-Regatta
**Vorfall:** Spinnaker-Barberholer-Augenplatte durch Deck gezogen bei 18 kt Vorwindkurs.

**Analyse:**
```
Beschlag:     Geschweißte Augenplatte, 4 × M6 Schrauben
Deck:         Balsa-Sandwich, 12 mm Gesamt (5+2+5)
Backing Plate: KEINE vorhanden (Werftsmontage ohne Backing Plate)
Kernverstärkung: KEINE (Balsa nicht ersetzt)
Last:         Geschätzt 800–1.200 kg (Spinnaker in Böe)
SWL Beschlag: 500 kg (Beschlag selbst hielt)
```

**Ursache:** 
1. Fehlende Backing Plate → Punktlast auf dünne GFK-Oberschale
2. Fehlende Kernverstärkung → Balsa nahm keine Last auf
3. Spinnaker-Last deutlich über SWL des Beschlags
4. M6-Schrauben zu klein für die auftretenden Kräfte

**Lehren:**
- Bei Balsa-Sandwich: IMMER Kernverstärkung + Backing Plate
- Spinnaker-Beschläge: mindestens SWL 1.000 kg bei 36-Fuß-Boot
- Werfts-Montage ≠ korrekte Montage — eigene Prüfung erforderlich
- Nachträgliche Reparatur: 4 × M8, Backing Plate 100 × 100 × 4 mm, Kernverstärkung Epoxid/404

### Fallstudie A3: Chronische Undichtigkeit — Wantenplatten-Decksdurchführung Hallberg-Rassy 34

**Yacht:** Hallberg-Rassy 34, Baujahr 2001, Nordsee/Atlantik-Überquerung
**Problem:** Chronisches Tropfen an allen 6 Wantenplatten-Decksdurchführungen trotz mehrfacher Reparaturversuche.

**Analyse:**
```
Dichtungssystem:  Original Neopren-Manschette + Silikon-Verguss
Alter:            20 Jahre
Reparaturversuche: 3× Silikon erneuert (falscher Sealant!)
Problem:          Silikon haftet nicht dauerhaft auf GFK
                  Wantenplatte bewegt sich ±1mm unter Last
                  → Dichtung bricht immer wieder
```

**Lösung (erfolgreich umgesetzt):**
```
1. Alle Manschetten und Silikon komplett entfernt
2. GFK-Oberfläche um Durchführung freigschleifen (80er Körnung)
3. 2 Lagen Biax 300g/m² als Flansch laminiert (Epoxid)
4. Flanschhöhe: 15 mm über Deckniveau
5. Wichard Cover Plates montiert (316L)
6. Sikaflex 291i als Dichtmittel
7. O-Ring zwischen Cover Plate und GFK-Flansch
Ergebnis: 5 Jahre dicht, keine Nacharbeit erforderlich
```

### Fallstudie A4: Galvanische Korrosion — Aluminium-Yacht mit Edelstahl-Beschlägen

**Yacht:** Ovni 395 (Aluminium), Baujahr 2008, Karibik/Pazifik
**Problem:** Schwere galvanische Korrosion an 8 Decksbeschlägen nach 3 Jahren in tropischen Gewässern.

**Analyse:**
```
Beschläge:    316L Edelstahl Pad Eyes und Fairleads
Deck:         Aluminium 5083
Isolation:    Ursprünglich Nylon-Unterlegscheiben + Sealant
Problem:      Sealant im tropischen Klima schneller degradiert
              Nylon-Unterlegscheiben teilweise gerissen
              → Direkter Edelstahl/Aluminium-Kontakt
              → ΔV ≈ 0.7V → massive galvanische Korrosion
              → Aluminium-Deck lokal bis 40% Materialverlust
```

**Lösung:**
```
1. Alle Edelstahl-Beschläge demontieren
2. Korrodiertes Aluminium ausschleifen und WIG-schweißen
3. GFK-Isolierplatten (3mm G10) unter alle Beschläge
4. Alle Schrauben mit PTFE-Isolierhülsen
5. Tef-Gel auf alle Kontaktflächen
6. Großzügige Sealant-Abdichtung (Sikaflex 291i)
7. Jährliche Inspektion aller Kontaktpunkte
Ergebnis: 4 Jahre ohne erneute Korrosion
```

### Fallstudie A5: Sturmschaden — Schleppösen-Versagen bei Bergung

**Yacht:** Jeanneau Sun Odyssey 440, Baujahr 2019, Biskaya
**Vorfall:** Während Bergung nach Motorschaden in schwerem Wetter. Schleppöse am Bug hat sich gelöst.

**Analyse:**
```
Beschlag:      Standard-Bugklampe als Schleppanschluss verwendet
SWL Klampe:    1.500 kg
Schlepplast:   Geschätzt 4.000–6.000 kg (Stoßlasten bei 2m Welle)
Befestigung:   4 × M8 Schrauben in Sandwich-Deck
Backing Plate: 50 × 50 × 3 mm (unterdimensioniert)
```

**Ursache:**
1. Bugklampe war NICHT als Schleppanschluss dimensioniert
2. Fehlende dedizierte Schleppöse
3. Stoßlasten beim Schleppen 3–5× höher als statische Last
4. Sicherheitsfaktor 6:1 für Schleppösen nicht eingehalten

**Lehren:**
- Dedizierte Schleppöse mit SWL ≥ 8t bei Blauwasser-Yachten
- Schleppöse direkt am Bug-Stringer oder Kielschwein angeschlagen
- Bugklampen sind KEINE Schleppanschlüsse
- Bei Bergung: Schleppverbindung über mehrere Beschläge verteilen (Bridle)

### Fallstudie A6: Ermüdungsrisse an Genuaschot-Augenplatten — Dehler 34

**Yacht:** Dehler 34, Baujahr 2006, Ostsee/Regatta
**Problem:** Risse an beiden Genuaschot-Augenplatten nach 12 Saisons intensivem Regattasegeln.

**Analyse:**
```
Beschlag:       Gegossene Augenplatten (Investment Cast)
Material:       316 Edelstahl
Lastzyklen:     Geschätzt 30.000–50.000 Wenden pro Saison × 12 = 360.000–600.000
Rissursprung:   Bohrungsrand der Grundplatte (Kerbfaktor K_t ≈ 3)
Rissrichtung:   Senkrecht zur Hauptzugrichtung
```

**Ursache:**
1. Gegossenes Material mit niedrigerer Ermüdungsfestigkeit als geschmiedet
2. Hohe Zyklenzahl durch Regattanutzung
3. Kerbwirkung am Bohrungsrand
4. 12 Saisons ohne Inspektion der Beschlagunterseite

**Lösung:**
```
1. Austausch gegen geschmiedete Wichard Diamant-Augenplatten
2. Alle Bohrungen im Deck mit Radius entgraten
3. Neue Backing Plates (100 × 70 × 5mm, 316L)
4. Inspektionsintervall: alle 3 Jahre (Regattanutzung)
```

### Fallstudie A7: Mastenfall durch Schott-Delamination am Wantenplatten-Anschluss

**Yacht:** Custom 45' Ketch, Baujahr 1985, Atlantik-Überquerung
**Vorfall:** Großmast gefallen, Ursache: Schott an Steuerbord-Oberwant-Chainplate hat sich vom Rumpf gelöst.

**Analyse:**
```
Wantenplatte:  10 mm 316L, 6 × M12 Bolzen → intakt
Schott:        18 mm Sperrholz → intakt
Laminierung:   Schott/Rumpf-Verbindung → VERSAGT
                Nur 2 Lagen 225g CSM beidseitig
                Nach 35 Jahren: Delamination der Schottverbindung
Last bei Bruch: Geschätzt 8t (Böe in Passatwind)
```

**Ursache:**
1. Unzureichende Schott-Laminierung (2 Lagen CSM zu wenig für Wantenkräfte)
2. 35 Jahre Ermüdung an der Laminierverbindung
3. CSM-Laminat hat geringere Ermüdungsfestigkeit als Gewebe
4. Keine Inspektion der Schottverbindung über 35 Jahre

**Lehren:**
- Schott-Laminierung im Wantenbereich: mindestens 4 Lagen Biax 300g beidseitig
- Ältere Yachten (>25 Jahre): Schottverbindungen prüfen
- Nachlaminierung mit Epoxid-Harz (nicht Polyester auf alte Polyester-Verbindung)

### Fallstudie A8: Deck Organizer — Leinenführung blockiert durch Salzverkrustung

**Yacht:** Hanse 388, Baujahr 2018, Mittelmeer (Griechenland)
**Problem:** Deck Organizer am Mastfuß blockiert regelmäßig. Fallen können nicht mehr frei laufen.

**Analyse:**
```
Beschlag:     Harken Triple Deck Organizer 351
Problem:      Delrin-Rollen durch Salzverkrustung blockiert
              Buchsen korrodiert (Aluminium-Buchsen in 316L-Gehäuse)
Wartung:      Keine Süßwasserspülung nach Törns
              Kein Schmiermittel aufgebracht
```

**Lösung:**
```
1. Deck Organizer demontieren
2. Alle Rollen und Buchsen in Essigwasser einlegen (12h)
3. Mit Süßwasser spülen und trocknen
4. Buchsen durch Delrin-Buchsen ersetzen (keine Aluminium/Edelstahl-Paarung)
5. McLube Sailkote auf alle beweglichen Teile
6. Präventiv: Nach jedem Törn Süßwasserspülung
```

---

## ANHANG B — AYDI-Integration (Pydantic-Modelle)

### B.1 Datenmodelle

```python
"""
AYDI Pydantic v2 models for deck fittings analysis (Augenplatten & Decksbeschläge).
Module: 11_05_augenplatten_decksbeschlaege
"""

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class DeckFittingType(str, Enum):
    """Types of deck fittings."""
    PAD_EYE_WELDED = "pad_eye_welded"
    PAD_EYE_BOLTED = "pad_eye_bolted"
    PAD_EYE_FOLDING = "pad_eye_folding"
    PAD_EYE_DIAMOND = "pad_eye_diamond"
    PAD_EYE_OVAL = "pad_eye_oval"
    CHAINPLATE_EXTERNAL = "chainplate_external"
    CHAINPLATE_INTERNAL = "chainplate_internal"
    CHAINPLATE_KEEL_STEPPED = "chainplate_keel_stepped"
    U_BOLT_WELDED = "u_bolt_welded"
    U_BOLT_THROUGH = "u_bolt_through"
    TANG_PLATE = "tang_plate"
    DECK_ORGANIZER_SINGLE = "deck_organizer_single"
    DECK_ORGANIZER_DOUBLE = "deck_organizer_double"
    DECK_ORGANIZER_TRIPLE = "deck_organizer_triple"
    DECK_ORGANIZER_MULTI = "deck_organizer_multi"
    FAIRLEAD_CLOSED = "fairlead_closed"
    FAIRLEAD_OPEN = "fairlead_open"
    FAIRLEAD_ROLLER = "fairlead_roller"
    MOORING_RING = "mooring_ring"


class FittingMaterial(str, Enum):
    """Material types for deck fittings."""
    STAINLESS_316L = "316l"
    STAINLESS_316 = "316"
    STAINLESS_304 = "304"
    DUPLEX_2205 = "duplex_2205"
    PH_17_4 = "17_4ph"
    BRONZE = "bronze"
    TITANIUM_GR5 = "titanium_gr5"
    ALUMINUM_6082 = "aluminum_6082"
    DELRIN = "delrin"
    TORLON = "torlon"


class FittingManufacturer(str, Enum):
    """Deck fitting manufacturers."""
    WICHARD = "wichard"
    SCHAEFER = "schaefer"
    HARKEN = "harken"
    RONSTAN = "ronstan"
    SELDEN = "selden"
    SEA_DOG = "sea_dog"
    OSCULATI = "osculati"
    SPRENGER = "sprenger"
    CUSTOM = "custom"
    UNKNOWN = "unknown"


class DeckConstructionType(str, Enum):
    """Deck construction types."""
    SANDWICH_BALSA = "sandwich_balsa"
    SANDWICH_PVC = "sandwich_pvc"
    SANDWICH_SAN = "sandwich_san"
    SOLID_LAMINATE = "solid_laminate"
    ALUMINUM = "aluminum"
    STEEL = "steel"
    WOOD_PLYWOOD = "wood_plywood"
    WOOD_PLANKED = "wood_planked"


class CoreReinforcementType(str, Enum):
    """Core reinforcement types for sandwich decks."""
    EPOXY_FILLER = "epoxy_filler"
    G10_INSERT = "g10_insert"
    HARDWOOD_INSERT = "hardwood_insert"
    ALUMINUM_INSERT = "aluminum_insert"
    PU_RESIN = "pu_resin"
    NONE = "none"
    UNKNOWN = "unknown"


class SealantType(str, Enum):
    """Sealant types used for deck fitting installation."""
    SIKAFLEX_291I = "sikaflex_291i"
    SIKAFLEX_295UV = "sikaflex_295uv"
    THREEBOND_4200 = "3m_4200"
    THREEBOND_5200 = "3m_5200"
    SIMSON_MSR = "simson_msr"
    BUTYL_TAPE = "butyl_tape"
    SILICONE = "silicone"
    UNKNOWN = "unknown"


class ConfidenceLevel(str, Enum):
    """AYDI confidence levels."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class FailurePatternSeverity(str, Enum):
    """Severity levels for failure patterns."""
    LIGHT = "light"
    MEDIUM = "medium"
    SEVERE = "severe"
    CRITICAL = "critical"


class SafetyCategory(str, Enum):
    """Safety categories for findings."""
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"


# ── Core Data Models ──


class DeckFittingSpecification(BaseModel):
    """Specification of a deck fitting."""

    model_config = {"from_attributes": True}

    fitting_type: DeckFittingType
    manufacturer: FittingManufacturer = FittingManufacturer.UNKNOWN
    model_number: Optional[str] = None
    material: FittingMaterial
    swl_kg: float = Field(..., gt=0, description="Safe Working Load in kg")
    breaking_load_kg: float = Field(..., gt=0, description="Breaking load in kg")
    safety_factor: float = Field(..., ge=2.0, description="Safety factor (min 2.0)")
    base_width_mm: Optional[float] = Field(None, gt=0)
    base_length_mm: Optional[float] = Field(None, gt=0)
    base_thickness_mm: Optional[float] = Field(None, gt=0)
    eye_diameter_mm: Optional[float] = Field(None, gt=0)
    bolt_count: int = Field(..., ge=1, description="Number of fasteners")
    bolt_size_mm: float = Field(..., gt=0, description="Bolt diameter in mm")
    weight_g: Optional[float] = Field(None, gt=0)

    @field_validator("safety_factor")
    @classmethod
    def validate_safety_factor(cls, v: float) -> float:
        if v < 3.0:
            raise ValueError(
                "Safety factor below 3.0 is not acceptable for marine deck fittings"
            )
        return v

    @field_validator("breaking_load_kg")
    @classmethod
    def validate_breaking_load(cls, v: float, info) -> float:
        swl = info.data.get("swl_kg")
        if swl and v < swl * 3:
            raise ValueError(
                f"Breaking load ({v} kg) must be at least 3x SWL ({swl} kg)"
            )
        return v


class BackingPlateSpec(BaseModel):
    """Backing plate specification."""

    model_config = {"from_attributes": True}

    material: FittingMaterial
    width_mm: float = Field(..., gt=0)
    length_mm: float = Field(..., gt=0)
    thickness_mm: float = Field(..., gt=0)
    area_cm2: Optional[float] = None
    has_radiused_corners: bool = True
    corner_radius_mm: float = Field(default=5.0, ge=0)

    def model_post_init(self, __context) -> None:
        if self.area_cm2 is None:
            self.area_cm2 = (self.width_mm * self.length_mm) / 100


class CoreReinforcementSpec(BaseModel):
    """Core reinforcement specification for sandwich decks."""

    model_config = {"from_attributes": True}

    reinforcement_type: CoreReinforcementType
    diameter_mm: Optional[float] = Field(None, gt=0)
    width_mm: Optional[float] = Field(None, gt=0)
    length_mm: Optional[float] = Field(None, gt=0)
    depth_mm: float = Field(..., gt=0, description="Depth matching core thickness")
    compressive_strength_mpa: Optional[float] = Field(None, gt=0)


class MountingConfiguration(BaseModel):
    """Complete mounting configuration for a deck fitting."""

    model_config = {"from_attributes": True}

    fitting: DeckFittingSpecification
    deck_type: DeckConstructionType
    deck_thickness_mm: float = Field(..., gt=0)
    core_thickness_mm: Optional[float] = Field(None, ge=0)
    backing_plate: Optional[BackingPlateSpec] = None
    core_reinforcement: Optional[CoreReinforcementSpec] = None
    sealant: SealantType = SealantType.SIKAFLEX_291I
    pull_angle_deg: float = Field(default=0.0, ge=0, le=90)
    galvanic_isolation_required: bool = False
    torque_nm: Optional[float] = Field(None, gt=0)


class LoadAnalysis(BaseModel):
    """Load analysis for a deck fitting."""

    model_config = {"from_attributes": True}

    total_load_kg: float = Field(..., gt=0)
    static_load_kg: float = Field(..., ge=0)
    dynamic_load_kg: float = Field(..., ge=0)
    shock_load_kg: float = Field(default=0.0, ge=0)
    pull_angle_deg: float = Field(default=0.0, ge=0, le=90)
    vertical_force_kg: float = Field(default=0.0, ge=0)
    horizontal_force_kg: float = Field(default=0.0, ge=0)
    bending_moment_nm: float = Field(default=0.0, ge=0)
    dynamic_factor: float = Field(default=1.5, ge=1.0)
    required_swl_kg: float = Field(default=0.0, ge=0)
    required_breaking_load_kg: float = Field(default=0.0, ge=0)
    safety_factor_applied: float = Field(default=4.0, ge=2.0)
    confidence: ConfidenceLevel = ConfidenceLevel.ESTIMATED

    def model_post_init(self, __context) -> None:
        import math
        angle_rad = math.radians(self.pull_angle_deg)
        if self.vertical_force_kg == 0:
            self.vertical_force_kg = self.total_load_kg * math.sin(angle_rad)
        if self.horizontal_force_kg == 0:
            self.horizontal_force_kg = self.total_load_kg * math.cos(angle_rad)
        if self.required_swl_kg == 0:
            self.required_swl_kg = self.total_load_kg * self.dynamic_factor
        if self.required_breaking_load_kg == 0:
            self.required_breaking_load_kg = (
                self.required_swl_kg * self.safety_factor_applied
            )


class BearingStressAnalysis(BaseModel):
    """Bearing stress analysis for bolted connections."""

    model_config = {"from_attributes": True}

    total_force_n: float = Field(..., gt=0)
    bolt_count: int = Field(..., ge=1)
    bolt_diameter_mm: float = Field(..., gt=0)
    laminate_thickness_mm: float = Field(..., gt=0)
    bearing_stress_mpa: Optional[float] = None
    allowable_bearing_stress_mpa: float = Field(default=80.0, gt=0)
    is_acceptable: Optional[bool] = None

    def model_post_init(self, __context) -> None:
        if self.bearing_stress_mpa is None:
            self.bearing_stress_mpa = self.total_force_n / (
                self.bolt_count * self.bolt_diameter_mm * self.laminate_thickness_mm
            )
        if self.is_acceptable is None:
            self.is_acceptable = (
                self.bearing_stress_mpa <= self.allowable_bearing_stress_mpa
            )


# ── Failure & Inspection Models ──


class FailurePattern(BaseModel):
    """A detected failure pattern on a deck fitting."""

    model_config = {"from_attributes": True}

    pattern_id: str = Field(..., description="e.g. FB-11.05-01")
    name_de: str
    name_en: str
    severity: FailurePatternSeverity
    safety_category: SafetyCategory
    description_de: str
    probable_causes: list[str]
    recommended_actions: list[str]
    confidence: ConfidenceLevel
    location_reference: Optional[str] = None
    photo_reference: Optional[str] = None


class InspectionResult(BaseModel):
    """Result of a deck fitting inspection."""

    model_config = {"from_attributes": True}

    fitting_id: str
    fitting_type: DeckFittingType
    inspection_date: datetime
    inspector: str
    overall_condition_score: int = Field(..., ge=0, le=100)
    corrosion_score: int = Field(..., ge=0, le=100)
    fastener_condition_score: int = Field(..., ge=0, le=100)
    sealant_condition_score: int = Field(..., ge=0, le=100)
    structural_integrity_score: int = Field(..., ge=0, le=100)
    failure_patterns: list[FailurePattern] = Field(default_factory=list)
    next_inspection_months: int = Field(default=12, ge=1)
    immediate_action_required: bool = False
    notes_de: Optional[str] = None
    confidence: ConfidenceLevel = ConfidenceLevel.VISUAL_MEDIUM


class DeckFittingAnalysisResult(BaseModel):
    """Complete analysis result for a deck fitting."""

    model_config = {"from_attributes": True}

    fitting_spec: DeckFittingSpecification
    mounting: MountingConfiguration
    load_analysis: Optional[LoadAnalysis] = None
    bearing_stress: Optional[BearingStressAnalysis] = None
    inspection: Optional[InspectionResult] = None
    overall_score: int = Field(..., ge=0, le=100)
    findings: list[FailurePattern] = Field(default_factory=list)
    recommendations_de: list[str] = Field(default_factory=list)
    confidence: ConfidenceLevel
    analysis_version: str = "1.0.0"
    analyzed_at: datetime = Field(default_factory=datetime.utcnow)


class ChainplateAssessment(BaseModel):
    """Specialized assessment model for chainplates."""

    model_config = {"from_attributes": True}

    boat_length_m: float = Field(..., gt=0)
    boat_displacement_kg: float = Field(..., gt=0)
    rig_type: str = Field(..., description="e.g. masthead_sloop, fractional_sloop, ketch")
    chainplate_material: FittingMaterial
    chainplate_thickness_mm: float = Field(..., gt=0)
    chainplate_width_mm: float = Field(..., gt=0)
    chainplate_length_mm: float = Field(..., gt=0)
    bolt_count: int = Field(..., ge=2)
    bolt_diameter_mm: float = Field(..., gt=0)
    age_years: int = Field(..., ge=0)
    last_inspection_date: Optional[datetime] = None
    deck_penetration_type: str = Field(default="through_deck")
    deck_penetration_sealed: bool = True
    toggle_installed: bool = True
    schott_connection_type: str = Field(default="laminated")
    calculated_rig_load_kg: Optional[float] = None
    chainplate_swl_kg: Optional[float] = None
    safety_margin_percent: Optional[float] = None
    condition_score: int = Field(default=50, ge=0, le=100)
    replacement_recommended: bool = False
    replacement_urgency: Optional[str] = None
    confidence: ConfidenceLevel = ConfidenceLevel.ESTIMATED
```

### B.2 Analyse-Funktionen

```python
"""
Analysis functions for deck fittings.
Module: 11_05_augenplatten_decksbeschlaege
"""

import math
from typing import Optional


def calculate_pull_angle_forces(
    line_force_kg: float,
    pull_angle_deg: float,
    eye_height_mm: float,
) -> dict:
    """Calculate vertical, horizontal forces and bending moment from pull angle.

    Args:
        line_force_kg: Force in the line in kg.
        pull_angle_deg: Pull angle from horizontal in degrees.
        eye_height_mm: Height of the eye above deck surface in mm.

    Returns:
        Dictionary with force components and bending moment.
    """
    angle_rad = math.radians(pull_angle_deg)
    force_n = line_force_kg * 9.81

    vertical_n = force_n * math.sin(angle_rad)
    horizontal_n = force_n * math.cos(angle_rad)
    bending_moment_nmm = force_n * math.sin(angle_rad) * eye_height_mm

    return {
        "vertical_force_n": round(vertical_n, 1),
        "horizontal_force_n": round(horizontal_n, 1),
        "vertical_force_kg": round(vertical_n / 9.81, 1),
        "horizontal_force_kg": round(horizontal_n / 9.81, 1),
        "bending_moment_nmm": round(bending_moment_nmm, 1),
        "bending_moment_nm": round(bending_moment_nmm / 1000, 2),
    }


def calculate_backing_plate_size(
    total_force_kg: float,
    deck_type: str,
    safety_margin: float = 1.5,
) -> dict:
    """Calculate minimum backing plate dimensions.

    Args:
        total_force_kg: Total force on the fitting in kg.
        deck_type: Type of deck construction.
        safety_margin: Additional safety margin multiplier.

    Returns:
        Dictionary with recommended backing plate dimensions.
    """
    allowable_stress = {
        "sandwich_balsa": 3.0,
        "sandwich_pvc": 3.0,
        "sandwich_san": 3.5,
        "solid_laminate": 10.0,
        "aluminum": 30.0,
        "wood_plywood": 5.0,
    }

    sigma = allowable_stress.get(deck_type, 3.0)
    force_n = total_force_kg * 9.81 * safety_margin
    area_mm2 = force_n / sigma
    side_mm = math.sqrt(area_mm2)

    # Thickness recommendation based on load
    if total_force_kg <= 500:
        thickness_ss = 3.0
        thickness_al = 5.0
    elif total_force_kg <= 1500:
        thickness_ss = 5.0
        thickness_al = 8.0
    elif total_force_kg <= 3000:
        thickness_ss = 8.0
        thickness_al = 12.0
    else:
        thickness_ss = max(10.0, total_force_kg / 400)
        thickness_al = max(15.0, total_force_kg / 250)

    return {
        "min_area_mm2": round(area_mm2, 0),
        "min_area_cm2": round(area_mm2 / 100, 1),
        "recommended_side_mm": round(side_mm + 10, 0),
        "recommended_width_mm": round(side_mm * 1.2 + 10, 0),
        "recommended_length_mm": round(side_mm * 0.8 + 10, 0),
        "thickness_stainless_mm": thickness_ss,
        "thickness_aluminum_mm": thickness_al,
        "allowable_stress_mpa": sigma,
    }


def calculate_bearing_stress(
    total_force_kg: float,
    bolt_count: int,
    bolt_diameter_mm: float,
    laminate_thickness_mm: float,
    deck_material: str = "grp_polyester",
) -> dict:
    """Calculate bearing stress at bolt holes.

    Args:
        total_force_kg: Total force on the fitting in kg.
        bolt_count: Number of bolts.
        bolt_diameter_mm: Bolt diameter in mm.
        laminate_thickness_mm: Effective laminate thickness in mm.
        deck_material: Deck laminate material type.

    Returns:
        Dictionary with bearing stress analysis.
    """
    allowable_bearing = {
        "grp_polyester": 150.0,
        "grp_vinylester": 200.0,
        "grp_epoxy": 250.0,
        "cfrp_epoxy": 300.0,
        "aluminum": 180.0,
    }

    force_n = total_force_kg * 9.81
    bearing_stress = force_n / (bolt_count * bolt_diameter_mm * laminate_thickness_mm)
    allowable = allowable_bearing.get(deck_material, 150.0)

    return {
        "bearing_stress_mpa": round(bearing_stress, 1),
        "allowable_stress_mpa": allowable,
        "utilization_percent": round((bearing_stress / allowable) * 100, 1),
        "is_acceptable": bearing_stress <= allowable,
        "force_per_bolt_n": round(force_n / bolt_count, 1),
    }


def assess_chainplate_condition(
    age_years: int,
    material: str,
    boat_length_m: float,
    thickness_mm: float,
    last_inspection_years_ago: Optional[int] = None,
    visible_corrosion: bool = False,
    visible_cracks: bool = False,
    deck_leak: bool = False,
    toggle_installed: bool = True,
) -> dict:
    """Assess chainplate condition and replacement urgency.

    Args:
        age_years: Age of chainplates in years.
        material: Chainplate material code.
        boat_length_m: Boat length overall in meters.
        thickness_mm: Chainplate thickness in mm.
        last_inspection_years_ago: Years since last inspection.
        visible_corrosion: Whether corrosion is visible.
        visible_cracks: Whether cracks are visible.
        deck_leak: Whether deck penetration leaks.
        toggle_installed: Whether toggles are installed.

    Returns:
        Dictionary with condition assessment and recommendations.
    """
    score = 100
    recommendations = []
    urgency = "routine"

    # Age deductions
    if age_years > 25:
        score -= 30
        recommendations.append("Wantenplatten älter als 25 Jahre — Austausch empfohlen")
        urgency = "high"
    elif age_years > 15:
        score -= 15
        recommendations.append(
            "Wantenplatten älter als 15 Jahre — zerstörungsfreie Prüfung empfohlen"
        )
        urgency = "medium"
    elif age_years > 10:
        score -= 5

    # Material assessment
    min_thickness = {
        "316l": {8: 6, 10: 8, 12: 8, 14: 10, 16: 12, 18: 12, 20: 15},
        "316": {8: 6, 10: 8, 12: 8, 14: 10, 16: 12, 18: 12, 20: 15},
        "duplex_2205": {8: 5, 10: 6, 12: 6, 14: 8, 16: 10, 18: 10, 20: 12},
    }

    mat_table = min_thickness.get(material, min_thickness["316l"])
    boat_len_key = min(
        mat_table.keys(),
        key=lambda x: abs(x - boat_length_m),
    )
    required_thickness = mat_table.get(boat_len_key, 10)

    if thickness_mm < required_thickness:
        score -= 25
        recommendations.append(
            f"Plattenstärke {thickness_mm}mm unter Minimum {required_thickness}mm "
            f"für {boat_length_m}m Boot"
        )
        urgency = "high"

    # Corrosion
    if visible_corrosion:
        score -= 20
        recommendations.append("Sichtbare Korrosion — Farbeindringstoffprüfung durchführen")
        if urgency != "critical":
            urgency = "high"

    # Cracks
    if visible_cracks:
        score -= 40
        recommendations.append("Rissbildung erkannt — SOFORTIGER AUSTAUSCH erforderlich")
        urgency = "critical"

    # Deck leak
    if deck_leak:
        score -= 15
        recommendations.append("Undichte Decksdurchführung — Dichtung erneuern")

    # Toggle
    if not toggle_installed:
        score -= 10
        recommendations.append("Kein Toggle installiert — Toggle nachrüsten")

    # Inspection
    if last_inspection_years_ago is not None and last_inspection_years_ago > 5:
        score -= 10
        recommendations.append(
            f"Letzte Inspektion vor {last_inspection_years_ago} Jahren — "
            "umfassende Inspektion fällig"
        )

    score = max(0, min(100, score))

    return {
        "condition_score": score,
        "replacement_recommended": score < 50 or urgency in ("high", "critical"),
        "urgency": urgency,
        "recommendations_de": recommendations,
        "next_inspection_months": 6 if urgency == "high" else (0 if urgency == "critical" else 12),
        "min_required_thickness_mm": required_thickness,
    }


def select_fitting_for_application(
    application: str,
    max_load_kg: float,
    pull_angle_deg: float,
    deck_type: str,
    boat_class: str,
    budget: str = "standard",
) -> dict:
    """Recommend a fitting type and specification for a given application.

    Args:
        application: Purpose of the fitting (e.g. 'genoa_sheet', 'spinnaker', 'safety_tether').
        max_load_kg: Maximum expected load in kg.
        pull_angle_deg: Expected pull angle in degrees.
        deck_type: Deck construction type.
        boat_class: Boat class identifier.
        budget: Budget level ('premium', 'standard', 'budget').

    Returns:
        Dictionary with fitting recommendation.
    """
    safety_factors = {
        "genoa_sheet": 4.0,
        "spinnaker": 4.0,
        "safety_tether": 5.0,
        "towing": 6.0,
        "mooring": 3.0,
        "backstay": 4.0,
        "chainplate": 4.0,
        "lazyjack": 3.0,
        "reef_line": 4.0,
    }

    sf = safety_factors.get(application, 4.0)
    required_swl = max_load_kg * 1.5  # dynamic factor
    required_breaking = required_swl * sf

    # Fitting type based on angle
    if pull_angle_deg <= 30:
        if application in ("chainplate", "backstay"):
            fitting_type = "tang_plate"
        else:
            fitting_type = "pad_eye_diamond"
    elif pull_angle_deg <= 60:
        fitting_type = "pad_eye_welded"
    else:
        fitting_type = "u_bolt_through"

    # Override for specific applications
    if application == "spinnaker":
        fitting_type = "pad_eye_folding"
    elif application == "safety_tether":
        fitting_type = "pad_eye_welded"
    elif application == "mooring":
        fitting_type = "mooring_ring"
    elif application == "towing":
        fitting_type = "u_bolt_through"

    # Manufacturer recommendation
    manufacturer_map = {
        "premium": ["wichard", "selden", "sprenger"],
        "standard": ["ronstan", "schaefer", "harken"],
        "budget": ["sea_dog", "osculati"],
    }

    manufacturers = manufacturer_map.get(budget, manufacturer_map["standard"])

    # Backing plate requirement
    needs_backing = (
        deck_type.startswith("sandwich")
        or required_swl > 500
    )

    return {
        "recommended_type": fitting_type,
        "required_swl_kg": round(required_swl, 0),
        "required_breaking_load_kg": round(required_breaking, 0),
        "safety_factor": sf,
        "dynamic_factor": 1.5,
        "recommended_manufacturers": manufacturers,
        "backing_plate_required": needs_backing,
        "core_reinforcement_required": deck_type.startswith("sandwich"),
        "material_recommendation": (
            "duplex_2205" if required_swl > 3000 or application == "towing"
            else "316l"
        ),
    }
```

---

## ANHANG C — Normen und Standards

### C.1 Relevante Normen für Augenplatten und Decksbeschläge

| Norm | Titel | Relevanz |
|---|---|---|
| ISO 15084:2003 | Kleine Wasserfahrzeuge — Verankerung und Festmachen | Festmacherbeschläge, Klüsen |
| ISO 15085:2003 | Mann-über-Bord-Prävention und Bergung | Sicherheitsleinenösen, Anschlagpunkte |
| EN 795:2012 | PSA gegen Absturz — Anschlageinrichtungen | Sicherheitsgurt-Anschlagpunkte |
| ISO 12215-5 | Rumpfkonstruktion — Bemessungsdrücke und Bemessungsspannungen (Einrumpfboote) | Deck-Lastverteilung, Backing Plates |
| ISO 12215-8 | Rumpfkonstruktion — Ruder | Ruderanlenkungsbeschläge |
| ISO 12215-9 | Rumpfkonstruktion — Segelfahrzeug-Anhänge (Kiel, Schwert, Ruder) | Kiel-/Anhang-Befestigungslasten (analog zu Wantenplatten-Lastpfaden; Rigg selbst nicht abgedeckt) |
| EN 1677-1 | Bauteile für Anschlagmittel | WLL-Definition, Prüfverfahren |
| DIN EN ISO 3506-1 | Verbindungselemente aus Edelstahl | A4-70/A4-80 Klassifizierung |
| ABYC H-40 | Verankerung, Festmachen und Kraftangriffspunkte | US-Standard für Anker-, Festmacher- und Kraftangriffspunkt-Beschläge |
| GL Rules for Yachts | Germanischer Lloyd Yacht-Regeln | Klassifikationsanforderungen |
| DNV Rules for Yachts | Det Norske Veritas | Strukturelle Anforderungen |

### C.2 Prüfnormen

| Norm | Prüfung | Anwendung |
|---|---|---|
| ISO 6892-1 | Zugversuch (Metalle) | Materialprüfung Edelstahl |
| ISO 148-1 | Kerbschlagbiegeversuch | Zähigkeitsprüfung |
| ISO 9712 | Zerstörungsfreie Prüfung — Qualifizierung | Personal für Wantenplatten-Prüfung |
| EN ISO 17637 | Sichtprüfung von Schweißverbindungen | Schweißnaht-Qualitätskontrolle |
| EN ISO 3452-1 | Eindringprüfung (PT) | Risserkennung an Beschlägen |

---

## ANHANG D — Lasttabellen

### D.1 Rigglast-Schätzung nach Bootsgröße

| Bootslänge [m] | Verdrängung [t] | Oberwant-Last [kg] | Unterwant-Last [kg] | Vorstag-Last [kg] | Backstag-Last [kg] |
|---|---|---|---|---|---|
| 8 | 2.5 | 1.500 | 800 | 1.800 | 1.200 |
| 9 | 3.5 | 2.000 | 1.100 | 2.400 | 1.600 |
| 10 | 4.5 | 2.800 | 1.500 | 3.200 | 2.200 |
| 11 | 6.0 | 3.500 | 1.900 | 4.000 | 2.800 |
| 12 | 7.5 | 4.500 | 2.400 | 5.000 | 3.500 |
| 13 | 9.0 | 5.500 | 3.000 | 6.200 | 4.300 |
| 14 | 11.0 | 6.800 | 3.700 | 7.500 | 5.200 |
| 15 | 13.0 | 8.000 | 4.300 | 8.800 | 6.100 |
| 16 | 15.5 | 9.500 | 5.100 | 10.500 | 7.300 |
| 18 | 20.0 | 12.000 | 6.500 | 13.500 | 9.500 |
| 20 | 25.0 | 15.000 | 8.000 | 17.000 | 12.000 |

> **Confidence:** estimated — Werte basieren auf typischen Rigg-Konfigurationen (Masthead-Sloop). Tatsächliche Werte hängen von Rigg-Typ, Masthöhe und Segelfläche ab.

### D.2 Wantenplatten-Dimensionierung nach Bootsgröße

| Bootslänge [m] | Material | Plattenbreite [mm] | Plattendicke [mm] | Bolzen | SWL [t] | Bruchlast [t] |
|---|---|---|---|---|---|---|
| 8–9 | 316L | 40 | 6 | 3× M8 | 2.0 | 8.0 |
| 9–10 | 316L | 45 | 8 | 3× M10 | 3.0 | 12.0 |
| 10–11 | 316L | 50 | 8 | 4× M10 | 4.0 | 16.0 |
| 11–12 | 316L/Duplex | 55 | 10 | 4× M10 | 5.0 | 20.0 |
| 12–14 | Duplex | 60 | 10 | 5× M12 | 6.5 | 26.0 |
| 14–16 | Duplex | 70 | 12 | 5× M12 | 8.0 | 32.0 |
| 16–18 | Duplex | 75 | 12 | 6× M12 | 10.0 | 40.0 |
| 18–20 | Duplex | 80 | 15 | 6× M14 | 13.0 | 52.0 |
| 20+ | Duplex | 90+ | 15+ | 8× M16 | 16+ | 64+ |

### D.3 Schrauben-Tragfähigkeit (316L, A4-80)

| Gewinde | Kern-∅ [mm] | Zugfestigkeit [kN] | Scherfestigkeit [kN] | Empf. Vorspannkraft [kN] |
|---|---|---|---|---|
| M5 | 4.13 | 10.7 | 6.2 | 5.0 |
| M6 | 4.92 | 15.2 | 8.8 | 7.2 |
| M8 | 6.47 | 26.3 | 15.2 | 12.5 |
| M10 | 8.16 | 41.8 | 24.2 | 19.8 |
| M12 | 9.85 | 60.9 | 35.2 | 28.9 |
| M14 | 11.55 | 83.7 | 48.4 | 39.7 |
| M16 | 13.55 | 115.2 | 66.6 | 54.6 |
| M20 | 16.93 | 180.0 | 104.0 | 85.3 |

---

## ANHANG E — Confidence-Mapping

### E.1 Confidence-Zuordnung für Augenplatten-Analyse

| Parameter | Pipeline A (Strukturiert) | Pipeline B (Visuell) | Pipeline C (Text) |
|---|---|---|---|
| Material-Identifikation | measured (Zertifikat) | visual_medium (Farbton) | documented (Spezifikation) |
| SWL/Bruchlast | measured (Datenblatt) | visual_insufficient | documented (Beschriftung) |
| Befestigungsqualität | measured (Drehmoment) | visual_high (Schrauben sichtbar) | documented (Bericht) |
| Korrosionszustand | measured (Materialprüfung) | visual_high (Oberfläche) | documented (Inspektion) |
| Rissbildung | measured (PT/UT-Prüfung) | visual_medium (Haarrisse) | documented (Prüfbericht) |
| Backing Plate vorhanden | measured (Zugang unten) | visual_insufficient | documented (Bauplan) |
| Kernverstärkung | measured (Ultraschall) | visual_insufficient | documented (Bauplan) |
| Sealant-Zustand | calculated (Alter + Typ) | visual_medium (Sichtbar) | documented (Wartungslog) |
| Zugwinkel | measured (CAD/Messung) | visual_medium (Foto) | estimated |
| Gesamtlast | calculated (Rigg-Berechnung) | visual_insufficient | estimated |

### E.2 Mindest-Confidence für Befundausgabe

| Befund-Schwere | Mindest-Confidence | Ausgabe |
|---|---|---|
| INFO | visual_low | Anzeigen mit Hinweis |
| WARNING | visual_medium | Anzeigen mit Confidence-Badge |
| CRITICAL | visual_medium | "Befund prüfen" (nicht "Mangel bestätigt") |
| CRITICAL | visual_low / insufficient | Nicht anzeigen, nur in Metadaten |

---

## ANHANG F — Wartungsintervalle

### F.1 Empfohlene Wartungsintervalle

| Bauteil | Prüfintervall | Wartungsumfang | Austauschintervall |
|---|---|---|---|
| Wantenplatten (Sichtprüfung) | 12 Monate | Decksdurchführung, Oberfläche | — |
| Wantenplatten (Komplett) | 60 Monate | PT-Prüfung, Bolzen, Schott | 15–25 Jahre |
| Augenplatten (Sichtprüfung) | 12 Monate | Korrosion, Risse, Sealant | — |
| Augenplatten (Nachziehen) | 12 Monate | Schrauben-Drehmoment prüfen | — |
| Augenplatten (Komplett) | 36 Monate | Demontage, Reinigung, Inspektion | 15–20 Jahre |
| U-Bolts | 12 Monate | Korrosion, Schweißnaht | 10–15 Jahre |
| Deck Organizer | 6 Monate | Rollen, Buchsen, Süßwasserspülung | 8–12 Jahre |
| Klüsen | 12 Monate | Verschleiß, Korrosion, Rollen | 15–20 Jahre |
| Festmacherringe | 12 Monate | Korrosion, Materialstärke | 15–20 Jahre |
| Sealant-Bett | 12 Monate | Sichtprüfung auf Risse/Ablösung | 5–10 Jahre |
| Backing Plates | 36 Monate | Korrosion, Verformung | Gleich mit Beschlag |

### F.2 Wartungsprotokoll-Vorlage

```
WARTUNGSPROTOKOLL — Decksbeschläge
═══════════════════════════════════

Yacht: _________________ Baujahr: _______ Datum: _________

Prüfer: _________________ Qualifikation: _________________

WANTENPLATTEN:
  □ Steuerbord Oberwant   Zustand: ○ gut  ○ mittel  ○ schlecht
  □ Backbord Oberwant     Zustand: ○ gut  ○ mittel  ○ schlecht
  □ Steuerbord Unterwant  Zustand: ○ gut  ○ mittel  ○ schlecht
  □ Backbord Unterwant    Zustand: ○ gut  ○ mittel  ○ schlecht
  □ Vorstag               Zustand: ○ gut  ○ mittel  ○ schlecht
  □ Backstag              Zustand: ○ gut  ○ mittel  ○ schlecht
  
  Decksdurchführungen dicht?    □ Ja  □ Nein → Details: ________
  Toggles vorhanden und frei?   □ Ja  □ Nein → Details: ________

AUGENPLATTEN:
  Anzahl geprüft: _____  davon Mängel: _____
  
  □ Korrosion gefunden?          □ Ja  □ Nein
  □ Risse gefunden?              □ Ja  □ Nein
  □ Schrauben nachgezogen?       □ Ja  □ Nein
  □ Sealant-Zustand:    ○ gut   ○ erneuern   ○ erneuert

Nächste Prüfung fällig: _____________

Unterschrift: _________________
```

---

## ANHANG G — Historische Entwicklung

### G.1 Entwicklung der Decksbeschlag-Technologie

| Zeitraum | Entwicklung | Material | Auswirkung |
|---|---|---|---|
| Vor 1900 | Holzbeschläge, Eisenbolzen | Eiche, Schmiedeeisen | Begrenzte Haltbarkeit, regelmäßiger Austausch |
| 1900–1950 | Bronze-Gussbeschläge | Rotguss, Manganbronze | Seewassertauglich, schwer |
| 1950–1970 | Erste Edelstahl-Beschläge | AISI 304 | Leichter als Bronze, aber korrosionsanfällig |
| 1970–1985 | 316 Edelstahl wird Standard | AISI 316 | Deutlich bessere Korrosionsbeständigkeit |
| 1985–2000 | Geschmiedete Beschläge (Wichard) | 316L | Höchste Festigkeit, industrielle Fertigung |
| 2000–2010 | Duplex-Stähle für Hochlast | Duplex 2205 | Doppelte Festigkeit bei gleicher Korrosionsbeständigkeit |
| 2010–heute | Titan und CFK-Hybrid | Ti Gr5, CFK | Ultra-Leichtbau für Regatta |
| Zukunft | 3D-Druck (Additive Manufacturing) | 316L/Titan | Topologie-optimierte Beschläge |

---

## ANHANG H — Bezugsquellen

### H.1 Bezugsquellen (Europa)

| Händler | Land | Schwerpunkt | Online-Shop | Mindestbestellung |
|---|---|---|---|---|
| SVB (Yachtausrüster) | DE | Vollsortiment | svb24.com | Nein |
| Compass24 | DE | Vollsortiment | compass24.de | Nein |
| AWN | DE | Vollsortiment | awn.de | Nein |
| Toplicht | DE | Beschläge, Rigg | toplicht.de | Nein |
| Rig-Shop | DE | Rigg-Beschläge | rig-shop.de | Nein |
| Force 4 | FR | Vollsortiment | force4.fr | Nein |
| Accastillage Diffusion | FR | Beschläge | accastillage-diffusion.com | Nein |
| Jimmy Green Marine | UK | Rigg, Beschläge | jimmygreen.co.uk | Nein |
| Sea Teach | NL | Beschläge, Rigg | seatech.nl | Nein |

### H.2 Direktbezug Hersteller

| Hersteller | Website | Katalog-Download | Händlersuche |
|---|---|---|---|
| Wichard | wichard.com | Ja (PDF) | Ja |
| Harken | harken.com | Ja (PDF) | Ja |
| Ronstan | ronstan.com | Ja (PDF + CAD) | Ja |
| Selden | seldenmast.com | Ja (PDF) | Ja |
| Schaefer Marine | schaefermarine.com | Ja (PDF) | Ja |
| Osculati | osculati.com | Ja (PDF) | Ja |

---

## ANHANG I — Herstellervergleich Detailtabellen

### I.1 Augenplatten-Vergleich (Mittelgröße, SWL ~1.000 kg)

| Eigenschaft | Wichard 6504 | Ronstan RF603 | Schaefer 78-02 | Sea-Dog 0800002 |
|---|---|---|---|---|
| SWL [kg] | 1.000 | 1.200 | 900 | 500 |
| Bruchlast [kg] | 4.000 | 4.800 | 3.600 | 2.000 |
| Material | 316L | 316L | 316 SS | 316 SS |
| Fertigung | Geschmiedet | CNC-gefräst | Investmentguss | Investmentguss |
| Grundplatte [mm] | 65 × 40 × 5 | 70 × 45 × 5 | 60 × 38 × 4 | 55 × 35 × 3 |
| Bohrungen | 4× | 4× | 4× | 4× |
| Gewicht [g] | 85 | 90 | 75 | 60 |
| Preis (ca.) [EUR] | 28 | 22 | 18 | 8 |
| Garantie | 10 Jahre | 5 Jahre | Keine Angabe | Keine Angabe |
| AYDI-Empfehlung | Premium | Standard+ | Standard | Budget |

### I.2 Wantenplatten-Vergleich (12m-Boot)

| Eigenschaft | Selden 508-531 | Wichard Custom | Sprenger 50 1510 |
|---|---|---|---|
| Für Bootslänge | 8–11m | Variabel | 10–14m |
| SWL [t] | 2.5 | Nach Berechnung | 4.5 |
| Bruchlast [t] | 10.0 | Nach Berechnung | 18.0 |
| Material | 316L | 316L HR | Duplex 2205 |
| Dicke [mm] | 8 | 8–10 | 10 |
| Breite [mm] | 50 | 50–60 | 60 |
| Toggle inklusive | Ja (Set) | Optional | Nein |
| Preis (ca.) [EUR/Satz] | 450–600 | 800–1.200 | 300–500 |

---

## ANHANG J — Auswahl-Algorithmus

### J.1 Automatisierter Beschlag-Auswahlprozess

```
ALGORITHMUS: Decksbeschlag-Auswahl

EINGABE:
  - Anwendung (Funktion des Beschlags)
  - Maximale Last [kg]
  - Zugwinkel [°]
  - Deck-Typ (Sandwich/Volllaminat/Aluminium)
  - Bootsklasse
  - Budgetstufe (Premium/Standard/Budget)

SCHRITT 1: Sicherheitsfaktor bestimmen
  IF Anwendung = "Schlepp" THEN SF = 6.0
  ELSE IF Anwendung = "Sicherheitsgurt" THEN SF = 5.0
  ELSE IF Anwendung = "Rigg" THEN SF = 4.0
  ELSE IF Anwendung = "Festmacher" THEN SF = 3.0
  ELSE SF = 4.0

SCHRITT 2: Dynamischen Faktor bestimmen
  IF Bootsklasse = "Regatta" THEN DF = 2.0
  ELSE IF Bootsklasse = "Blauwasser" THEN DF = 1.8
  ELSE DF = 1.5

SCHRITT 3: Erforderliche Bruchlast berechnen
  SWL_erforderlich = Last_max × DF
  Bruchlast_erforderlich = SWL_erforderlich × SF

SCHRITT 4: Beschlagtyp nach Zugwinkel wählen
  IF Winkel ≤ 20° THEN Typ = "Diamant-Augenplatte"
  ELSE IF Winkel ≤ 45° THEN Typ = "Geschweißte Augenplatte"
  ELSE IF Winkel ≤ 70° THEN Typ = "Augbolzen"
  ELSE Typ = "U-Bolt durchgesteckt"

SCHRITT 5: Material bestimmen
  IF Bruchlast > 12.000 kg THEN Material = "Duplex 2205"
  ELSE IF Bootsklasse = "Regatta" AND Budget = "Premium" THEN Material = "Titan"
  ELSE Material = "316L"

SCHRITT 6: Backing Plate prüfen
  IF Deck_Typ = "Sandwich" THEN Backing_Plate = OBLIGATORISCH
  ELSE IF SWL > 500 kg THEN Backing_Plate = EMPFOHLEN
  ELSE Backing_Plate = OPTIONAL

SCHRITT 7: Kernverstärkung prüfen
  IF Deck_Typ = "Sandwich" THEN Kernverstärkung = OBLIGATORISCH
  ELSE Kernverstärkung = NICHT ERFORDERLICH

AUSGABE:
  - Empfohlener Beschlagtyp
  - Erforderliche SWL und Bruchlast
  - Material
  - Backing Plate (Ja/Nein, Dimensionen)
  - Kernverstärkung (Ja/Nein, Typ)
  - Schrauben (Anzahl, Größe)
  - Hersteller-Empfehlungen (nach Budget)
```

---

## ANHANG K — Prüfprotokolle

### K.1 Prüfprotokoll — Augenplatten-Inspektion

```
PRÜFPROTOKOLL — Augenplatten & Decksbeschläge
═══════════════════════════════════════════════

Yacht: ________________  Typ: ________________  Baujahr: ______

Prüfdatum: ___________  Prüfer: ______________________________

BESCHLAG Nr.: ____  Position: ________________________________

Typ:           □ Augenplatte  □ U-Bolt  □ Klüse  □ Ring  □ Sonstig
Hersteller:    _______________  Modell: ________________________
Material:      □ 316L  □ 316  □ 304  □ Duplex  □ Bronze  □ ____

SICHTPRÜFUNG:
  Korrosion:        □ Keine  □ Oberfläche  □ Lochfraß  □ Schwer
  Risse:            □ Keine  □ Verdacht    □ Sichtbar   □ Offen
  Verformung:       □ Keine  □ Leicht      □ Deutlich   □ Schwer
  Schweißnaht:      □ OK     □ Poren       □ Anriss     □ n/a
  Sealant:          □ Intakt □ Risse       □ Ablösung   □ Fehlt

BEFESTIGUNG:
  Schraubenanzahl:  ____  Typ: ____  Material: ____
  Drehmoment:       □ OK  □ Lose  □ Nicht prüfbar
  Backing Plate:    □ Vorhanden  □ Nicht vorhanden  □ Nicht prüfbar
  Kernverstärkung:  □ Vorhanden  □ Nicht vorhanden  □ Nicht prüfbar

UMGEBUNG:
  Deck-Zustand:     □ OK  □ Gelcoatrisse  □ Delamination  □ Weich
  Feuchte:          □ Trocken  □ Feucht  □ Nass
  Klopftest:        □ OK (hart)  □ Dumpf (Verdacht)

BEWERTUNG:
  □ In Ordnung — nächste Prüfung in 12 Monaten
  □ Mängel — Maßnahme erforderlich (siehe unten)
  □ KRITISCH — sofortige Maßnahme erforderlich

EMPFOHLENE MASSNAHME:
_______________________________________________________________
_______________________________________________________________

Nächste Prüfung: ___________  Unterschrift: ___________________
```

---

## ANHANG L — Visuelle Analyse-Referenz

### L.1 AYDI Vision-Referenz für Augenplatten-Zustandsbeurteilung

```
Visuelle Merkmale für Pipeline B (Claude Vision):

ZUSTAND GUT (Score 80–100):
  - Gleichmäßige, glänzende oder matte Oberfläche
  - Keine Verfärbungen
  - Sealant-Raupe durchgängig und intakt
  - Schraubenköpfe bündig und unbeschädigt
  - Kein Spalt zwischen Beschlag und Deck
  - Gelcoat um Beschlag riss- und fleckenfrei

ZUSTAND MITTEL (Score 50–79):
  - Leichte Verfärbungen (Tea Staining)
  - Sealant leicht rissig oder verfärbt
  - Minimaler Spalt sichtbar
  - Leichte Gelcoat-Haarrisse im Umfeld
  - Oberfläche stumpf aber intakt

ZUSTAND SCHLECHT (Score 20–49):
  - Deutliche Rostflecken oder Lochfraß
  - Sealant großflächig abgelöst
  - Sichtbarer Spalt zwischen Beschlag und Deck
  - Gelcoat-Sternrisse um Befestigungspunkte
  - Wasser/Feuchtigkeit sichtbar

ZUSTAND KRITISCH (Score 0–19):
  - Offene Risse im Beschlag oder an Schweißnaht
  - Beschlag sichtbar verformt oder verschoben
  - Schrauben herausgezogen oder fehlend
  - Deck um Beschlag aufgewölbt oder eingebrochen
  - Massive Korrosion mit Materialverlust
```

### L.2 Foto-Anforderungen für visuelle Analyse

```
Mindestanforderungen für Foto-Bewertung:

AUFLÖSUNG:    Mindestens 2 Megapixel im Beschlag-Bereich
BELEUCHTUNG:  Seitliches Licht bevorzugt (Risse/Korrosion sichtbar)
ABSTAND:      20–50 cm für Einzelbeschlag
WINKEL:       Frontal (90° zur Decksoberfläche) + 45° Schrägansicht
SCHÄRFE:      Beschlag muss scharf abgebildet sein
KONTEXT:      Umgebung sichtbar (Gelcoat-Zustand um Beschlag)

FÜR CHAINPLATES ZUSÄTZLICH:
  - Foto der Decksdurchführung von oben
  - Foto der Unterseite (unter Deck) wenn zugänglich
  - Foto des Toggle-Bereichs
```

---

## ANHANG M — Korrosionsschutz-Leitfaden

### M.1 Korrosionsschutz-Maßnahmen nach Anwendung

| Anwendung | Primärschutz | Sekundärschutz | Wartung |
|---|---|---|---|
| 316L auf GFK-Deck | Sealant-Bett | Passivierung | Jährlich Sichtprüfung |
| 316L auf Aluminium-Deck | GFK-Isolation + Tef-Gel | Sealant-Bett | Halbjährlich prüfen |
| 316L auf Teakdeck | Sealant + Epoxid-Versiegelung | Fugenmasse-Abdichtung | Jährlich |
| Duplex auf GFK | Sealant-Bett | Passivierung | Alle 2 Jahre |
| Bronze auf GFK | Sealant-Bett | Keine weiteren | Jährlich (Dezinkifizierung) |

### M.2 Passivierung von Edelstahl-Beschlägen

```
Passivierungsverfahren:

Schritt 1: Reinigung
  - Oberfläche mit Aceton oder Isopropanol entfetten
  - Keine Stahlbürste verwenden (Fremdmetall-Eintrag!)
  - Edelstahl-Bürste oder Kunststoff-Pad verwenden

Schritt 2: Beizen (bei Bedarf)
  - Beizpaste (z.B. Avesta Cleaner 401) auftragen
  - 15–30 Minuten einwirken lassen
  - Mit reichlich Süßwasser abspülen

Schritt 3: Passivierung
  - Zitronensäure-Lösung (10–20%) auftragen
  - ODER kommerzielle Passivierungslösung (z.B. Derustit 4530)
  - 30–60 Minuten einwirken lassen
  - Mit reichlich Süßwasser abspülen
  - Trocknen lassen

Ergebnis: Stabile Chromoxid-Passivschicht bildet sich in 24–48h
```

---

## ANHANG N — Retrofit-Leitfaden

### N.1 Nachrüstung von Beschlagpunkten

```
Planung:
  1. Lastanalyse durchführen (Abschnitt 2.1)
  2. Position bestimmen (Lastpfad beachten)
  3. Unterdeck-Zugang sicherstellen
  4. Kerntyp und Laminatdicke ermitteln
  5. Beschlag und Befestigung dimensionieren

Durchführung:
  1. Position markieren (Deck + Unterdeck)
  2. Pilotbohrung setzen (Ø 3 mm)
  3. Kernverstärkung einbringen (bei Sandwich)
  4. Aushärten lassen (24h bei Epoxid)
  5. Endbohrungen setzen
  6. Backing Plate vorbereiten
  7. Sealant auftragen
  8. Beschlag montieren und anziehen
  9. Probebelastung (50% SWL, statisch)
  10. Dokumentieren (Foto, Beschlag-Typ, Datum)
```

### N.2 Häufige Retrofit-Szenarien

| Szenario | Aufwand | Kosten (ca.) | Komplexität |
|---|---|---|---|
| Zusätzliche Sicherheitsleinenöse | 1–2h | 50–150 EUR | Gering |
| Spinnaker-Augenplatten nachrüsten | 2–4h | 100–300 EUR | Mittel |
| Schleppöse nachrüsten | 4–8h | 300–800 EUR | Hoch |
| Wantenplatten-Austausch (6 Stück) | 16–40h | 2.000–8.000 EUR | Sehr hoch |
| Deck Organizer nachrüsten | 1–2h | 80–250 EUR | Gering |
| Rollenklüse nachrüsten | 2–3h | 150–400 EUR | Mittel |

---

## ANHANG O — Regatta-Spezifikationen

### O.1 Offshore Special Regulations (OSR) — Relevante Anforderungen

| OSR-Regel | Anforderung | Beschlag-Relevanz |
|---|---|---|
| 4.05.1 | Sicherheitsleinen-Befestigung am Cockpit | Mindestens 2× Pad Eyes im Cockpit |
| 4.05.2 | Jacklines mit zertifizierten Anschlagpunkten | Alle 3m ein Anschlagpunkt an Deck |
| 4.05.3 | Anschlagpunkte SWL ≥ 2.000 kg | Geschmiedete Pad Eyes, Backing Plate |
| 4.22 | Schleppeinrichtung | Dedizierte Schleppöse, SWL nach Bootsgröße |

### O.2 Regatta-optimierte Beschlag-Auswahl

| Beschlag | Standard | Regatta-Optimierung | Gewichtsersparnis |
|---|---|---|---|
| Pad Eye (Mittel) | 316L, 85g | Titan Gr5, 48g | 44% |
| Pad Eye (Groß) | 316L, 180g | Titan Gr5, 100g | 44% |
| Deck Organizer 3× | Edelstahl, 320g | Aluminium/Torlon, 180g | 44% |
| Backing Plate | 316L, 150g | CFK, 60g | 60% |
| Chainplate (12m) | Duplex 10mm, 800g | Titan 8mm, 420g | 48% |

---

## ANHANG P — Superyacht-Sonderlösungen

### P.1 Anforderungen ab 18m Bootslänge

```
Zusätzliche Anforderungen für Superyachten:

1. KLASSIFIKATION:
   - Lloyd's, DNV, Bureau Veritas oder ABS Zertifizierung
   - Alle Decksbeschläge müssen berechnet und geprüft sein
   - Werkstoffzeugnisse (3.1 nach EN 10204) für alle Beschläge

2. MATERIALANFORDERUNGEN:
   - Mindestens Duplex 2205 für alle Rigg-Beschläge
   - Titan für gewichtsoptimierte Anwendungen
   - Alle Schweißnähte röntgengeprüft
   - Chargenrückverfolgbarkeit

3. OBERFLÄCHENQUALITÄT:
   - Hochglanzpoliert (Mirror Finish) für sichtbare Beschläge
   - Elektropolitur für maximale Korrosionsbeständigkeit
   - Lasergravierte Teilenummern
   - Keine sichtbaren Befestigungselemente (verdeckte Montage)

4. VERDECKTE MONTAGE:
   - Pad Eyes unter Teak-Decksplanken
   - Versenkbare Festmacherringe (Pop-Up)
   - Integrierte Beschläge im Schandeckel
```

### P.2 Speziallieferanten für Superyacht-Beschläge

| Lieferant | Spezialisierung | Materialien | Zertifizierung |
|---|---|---|---|
| BSI (NL) | Custom Rigg-Beschläge | Duplex, Titan, Nitronic 50 | DNV, BV |
| Rondal (NL) | Integrierte Deckssysteme | Titan, Carbon-Hybrid | Lloyd's |
| Southern Spars | Carbon-Rigg-Beschläge | CFK, Titan | DNV |
| Hall Spars | Nitronic-50 Chainplates | Nitronic 50 | ABS |

---

## ANHANG Q — Umrechnungstabellen

### Q.1 Kraft-Umrechnungen

| Von | Nach | Faktor |
|---|---|---|
| kg (Kraft) | Newton (N) | × 9.81 |
| Newton (N) | kg (Kraft) | × 0.102 |
| kN | kg (Kraft) | × 102 |
| lbf (Pound-Force) | Newton (N) | × 4.448 |
| Newton (N) | lbf | × 0.225 |
| Tonne (metrisch) | kN | × 9.81 |
| kN | Tonne | × 0.102 |

### Q.2 Drehmoment-Umrechnungen

| Von | Nach | Faktor |
|---|---|---|
| Nm | ft-lbf | × 0.738 |
| ft-lbf | Nm | × 1.356 |
| Nm | in-lbf | × 8.851 |
| kgf-cm | Nm | × 0.0981 |

### Q.3 Spannung/Druck-Umrechnungen

| Von | Nach | Faktor |
|---|---|---|
| N/mm² (MPa) | psi | × 145.04 |
| psi | N/mm² (MPa) | × 0.00689 |
| kN/cm² | MPa | × 10 |
| bar | MPa | × 0.1 |

### Q.4 Gewinde-Referenz (Metrisch ↔ Imperial)

| Metrisch | Nächster UNC | Nächster UNF | Kern-∅ metrisch [mm] |
|---|---|---|---|
| M5 | #10-24 | #10-32 | 4.13 |
| M6 | 1/4"-20 | 1/4"-28 | 4.92 |
| M8 | 5/16"-18 | 5/16"-24 | 6.47 |
| M10 | 3/8"-16 | 3/8"-24 | 8.16 |
| M12 | 1/2"-13 | 1/2"-20 | 9.85 |
| M16 | 5/8"-11 | 5/8"-18 | 13.55 |
| M20 | 3/4"-10 | 3/4"-16 | 16.93 |

---

## ANHANG R — Checklisten

### R.1 Checkliste: Decksbeschlag-Neumontage

```
VOR DER MONTAGE:
  □ Last berechnet und Sicherheitsfaktor bestimmt
  □ Beschlag mit ausreichender SWL/Bruchlast gewählt
  □ Material verifiziert (316L / Duplex / Bronze)
  □ Backing Plate dimensioniert und beschafft
  □ Schrauben in richtiger Größe und Material (A4-70/A4-80)
  □ Sealant bereit (Sikaflex 291i empfohlen)
  □ Kernverstärkungsmaterial bereit (bei Sandwich)
  □ Werkzeuge: Bohrmaschine, Bits, Drehmomentschlüssel
  □ Unterdeck-Zugang geprüft

MONTAGE:
  □ Position angezeichnet und Unterdeck kontrolliert
  □ Kernverstärkung eingebracht und ausgehärtet (24h)
  □ Bohrungen gesetzt und entgratet
  □ Sealant in Bohrungen eingebracht
  □ Sealant auf Beschlag-Unterseite aufgebracht
  □ Beschlag positioniert
  □ Schrauben eingesetzt
  □ Backing Plate + Unterlegscheiben + Muttern aufgesetzt
  □ Über Kreuz angezogen (50% → 80% → 100%)
  □ Überschüssiges Sealant entfernt

NACH DER MONTAGE:
  □ Drehmoment nach 24h nachkontrolliert
  □ Sealant-Raupe am Rand geglättet
  □ Foto für Dokumentation
  □ Beschlag-Daten in Wartungsprotokoll eingetragen
```

### R.2 Checkliste: Saisonstart-Inspektion Decksbeschläge

```
JÄHRLICHE INSPEKTION (Saisonstart):

WANTENPLATTEN:
  □ Alle Decksdurchführungen auf Dichtheit geprüft
  □ Sichtbare Oberfläche auf Risse und Korrosion geprüft
  □ Toggle-Gelenke auf Leichtgängigkeit geprüft
  □ Wantenbolzen auf Verschleiß geprüft
  □ Unter Deck: Wasserflecken, Salzablagerungen?
  □ Schott-Laminierung: Risse oder Ablösung?

AUGENPLATTEN & PAD EYES:
  □ Alle Pad Eyes auf festen Sitz geprüft (Wackeltest)
  □ Sealant-Zustand rund um alle Beschläge geprüft
  □ Korrosion an Beschlägen und Schrauben?
  □ Gelcoat-Risse um Befestigungspunkte?
  □ Klapp-Augenplatten: Gelenk schmieren (Lanolin)

DECK ORGANIZER:
  □ Alle Rollen und Buchsen auf Leichtgängigkeit geprüft
  □ Salzablagerungen entfernt (Süßwasserspülung)
  □ Schmierung aufgetragen (McLube Sailkote)

KLÜSEN & FAIRLEADS:
  □ Oberfläche auf Verschleißrillen geprüft
  □ Rollenklüsen: Rollen drehen frei?
  □ Befestigung fest?

FESTMACHERRINGE:
  □ Materialstärke visuell geprüft (Korrosion = Materialverlust)
  □ Drehbare Ringe: Gelenk frei?

ERGEBNIS:
  □ Alle Beschläge in Ordnung
  □ Mängel gefunden (Liste anfertigen, Maßnahme planen)
  □ KRITISCHE Mängel → Boot nicht auslaufen lassen!

Datum: _________  Prüfer: ______________  Unterschrift: ________
```

### R.3 Checkliste: Sturmvorbereitung — Decksbeschläge

```
STURMVORBEREITUNG:

  □ Alle Wantenplatten auf Rissfreiheit geprüft
  □ Rigg-Spannung kontrolliert und ggf. nachgestellt
  □ Sturmfock-Augenplatten geprüft (wenn vorhanden)
  □ Trysegel-Anschlagpunkte geprüft (wenn vorhanden)
  □ Alle Festmacherbeschläge auf festen Sitz geprüft
  □ Zusätzliche Festmacherleinen an separaten Beschlägen
  □ Fender-Befestigungspunkte geprüft
  □ Sicherheitsleinenösen funktionsfähig
  □ Schleppöse zugänglich und einsatzbereit
  □ Lose Gegenstände an Deck gesichert
  □ Sprayhood/Bimini-Beschläge extra gesichert oder abgebaut
```

---

> **Ende der Wissensdatei 11.05 — Augenplatten und Decksbeschläge**
> 
> **AYDI Research** — Version 1.0.0 — 2026-04-25
> 
> Diese Datei ist Teil der AYDI-Wissensdatenbank und dient als Referenz für die
> automatisierte Analyse von Decksbeschlägen in den Pipelines A, B und C.
> Alle Lastwerte sind Richtwerte (Confidence: estimated/benchmark) sofern nicht
> anders gekennzeichnet. Für sicherheitskritische Entscheidungen sind
> individuelle Berechnungen und professionelle Inspektionen erforderlich.