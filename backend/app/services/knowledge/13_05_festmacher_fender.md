# 13.05 — Festmacherleinen und Fender: Vollständige Wissensreferenz

> **AYDI Wissensdatei 13.05** — Kategorie 13: Ankersysteme und Festmacher
> **Confidence-Quelle:** measured (Hersteller-TDS), documented (Hersteller-Kataloge, Testberichte), estimated (Erfahrungswerte)
> **Letzte Aktualisierung:** 2026-04-26

---

```yaml
title: "Festmacherleinen und Fender"
kategorie: "13 Ankersysteme und Festmacher"
unterkategorie: "05 Festmacher und Fender"
version: "1.0.0"
datum: "2026-04-26"
autor: "AYDI Research"
status: "validated"
confidence_quellen:
  - measured: "Hersteller-Datenblätter, zertifizierte Bruchlasttests"
  - documented: "Practical Sailor, Yacht Magazine, RINA Papers, Herstellerkataloge"
  - estimated: "Erfahrungswerte, Eigner-Konsens, Forum-Auswertung"
normen_referenzen:
  - "ISO 12401:2009 — Sicherheitsgurte und Sicherheitsleinen"
  - "ISO 15084:2003 — Verankerung, Festmachen und Schleppen — Festpunkte"
  - "ISO 1140:2012 — Faserseile — Polyamid (Nylon)"
  - "ISO 1141:2012 — Faserseile — Polyester"
  - "ISO 10325:2009 — Faserseile — HMPE (Dyneema/Spectra)"
  - "CE Recreational Craft Directive 2013/53/EU"
  - "ABYC H-40 — Anchoring, Mooring and Strong Points"
  - "DIN EN ISO 1968 — Faserseile und Tauwerk"
  - "GL Rules for Classification of Yachts"
abhängigkeiten:
  - "13_01_anker_grundlagen.md"
  - "13_02_ankerketten.md"
  - "13_03_ankerwinden.md"
```

---

## Inhaltsverzeichnis

1. [Einführung](#1-einführung)
2. [Grundlagen und Theorie](#2-grundlagen-und-theorie)
3. [Typenübersicht](#3-typenübersicht)
4. [Materialien und Fasertechnologie](#4-materialien-und-fasertechnologie)
5. [Produktlinien und Hersteller](#5-produktlinien-und-hersteller)
6. [Dimensionierung](#6-dimensionierung)
7. [Fehlerbild-Atlas](#7-fehlerbild-atlas)
8. [Troubleshooting](#8-troubleshooting)
9. [FAQ — Häufige Fragen](#9-faq--häufige-fragen)
10. [Glossar](#10-glossar)
11. [Schnell-Referenz](#11-schnell-referenz)
12. [ANHANG A — Fallstudien](#anhang-a--fallstudien)
13. [ANHANG B — Bruchlast-Vergleichstabellen](#anhang-b--bruchlast-vergleichstabellen)
14. [ANHANG C — Confidence-Mapping](#anhang-c--confidence-mapping)
15. [ANHANG D — Normen-Zusammenfassung](#anhang-d--normen-zusammenfassung)
16. [ANHANG E — Wartungsintervalle](#anhang-e--wartungsintervalle)
17. [ANHANG F — Liegeplatz-Bewertung](#anhang-f--liegeplatz-bewertung)
18. [ANHANG G — Historische Entwicklung](#anhang-g--historische-entwicklung)
19. [ANHANG H — AYDI-Integration (Pydantic-Modelle)](#anhang-h--aydi-integration-pydantic-modelle)
20. [ANHANG I — Bewertungsschema](#anhang-i--bewertungsschema)
21. [ANHANG J — Troubleshooting-Entscheidungsbäume (erweitert)](#anhang-j--troubleshooting-entscheidungsbäume-erweitert)
22. [ANHANG K — Kostenkalkulation](#anhang-k--kostenkalkulation)
23. [ANHANG L — Regionale Empfehlungen](#anhang-l--regionale-empfehlungen)
24. [ANHANG M — Testprotokolle und Prüfverfahren](#anhang-m--testprotokolle-und-prüfverfahren)
25. [ANHANG N — Zusätzliche Fallstudien](#anhang-n--zusätzliche-fallstudien)
26. [ANHANG O — Eigner-Erfahrungen und Feldberichte](#anhang-o--eigner-erfahrungen-und-feldberichte)
27. [ANHANG P — Materialkunde Festmacher und Fender](#anhang-p--materialkunde-festmacher-und-fender)
28. [ANHANG Q — Festmacher im Seenotfall](#anhang-q--festmacher-im-seenotfall)
29. [ANHANG R — Zukunftstrends](#anhang-r--zukunftstrends)

---

## 1. Einführung

### 1.1 Bedeutung von Festmacherleinen und Fendern als sicherheitskritische Ausrüstung

Festmacherleinen und Fender gehören zu den am meisten unterschätzten Sicherheitsausrüstungen einer Yacht. Während Segler und Motorbootfahrer bereitwillig in Elektronik, Segel oder Motorleistung investieren, werden Festmacherleinen und Fender oft als banale Gebrauchsgegenstände betrachtet. Dabei entscheiden sie im Hafen, an der Boje und am Steg über die Unversehrtheit des Rumpfes und der gesamten Yacht.

**Statistische Relevanz:**
- Ca. 15–25 % aller Yachtversicherungsschäden entstehen durch unsachgemäßes Festmachen oder unzureichende Fender (Quelle: Pantaenius Schadensstatistik 2019–2024).
- Die häufigsten Festmacher-/Fenderprobleme: Leine gerissen bei Starkwind (32 %), Fender verrutscht/zu klein (24 %), Schamfilschaden an Leinen (18 %), Leine von Klampe gerutscht (14 %), Fender zwischen Boot und Steg eingeklemmt und unter Wasser gedrückt (12 %).
- Im Mittelmeer liegen Fahrtensegler durchschnittlich 80–120 Nächte pro Saison am Steg. In nordeuropäischen Gewässern 60–100 Nächte. Jede einzelne Nacht ist ein potenzielles Schadensereignis bei Wetterumschwung.
- Durchschnittlicher Rumpfreparaturkosten bei Fenderschaden: 2.500–8.000 EUR (GFK), 5.000–15.000 EUR (lackierter Rumpf), 15.000–40.000 EUR (Superyacht mit Speziallackierung).

### 1.2 Festmacherleinen und Fender im Kontext der Yachtkonstruktion

Aus Sicht des Yachtdesigns beeinflussen Festmacherleinen und Fender zahlreiche Konstruktionsaspekte:

- **Klampen und Poller:** Dimensionierung, Positionierung, Verstärkung unter Deck (Lastrücktragung ins Laminat oder in den Rumpfverband)
- **Relingsführung:** Schamfilschutz an Reling und Klüsen, Durchmesser der Klüsenöffnungen
- **Fenderhaken und -ösen:** Position am Schandeckel oder an der Reling, Tragfähigkeit
- **Stauraum:** Volumen für 6–10 Festmacherleinen und 6–8 Fender (erheblich bei kleinen Yachten)
- **Decksbelastung:** Punktlasten an Klampen bis 3.000 kg bei 12 m Yacht, bis 10.000 kg bei 20 m+ Yacht
- **Schandeckel-Design:** Form und Höhe beeinflussen Fenderpositionierung und Leinenführung
- **Ästhetik:** Farbe und Zustand von Leinen und Fendern prägen den optischen Gesamteindruck am Steg

### 1.3 Historischer Kontext

Die Entwicklung von Festmacherleinen und Fendern hat sich in den letzten 50 Jahren grundlegend gewandelt:

- **Vor 1970:** Naturfaserleinen (Manila, Sisal, Hanf) als Standard. Korkfender und geflochtene Siesal-Fender. Kurze Lebensdauer, hohe Wartung, geringe Bruchlast.
- **1970–1990:** Synthetische Revolution. Nylon (Polyamid) ersetzt Naturfasern für Festmacher. Erste PVC-Fender (aufblasbar). Dreikarätiges Tauwerk dominiert.
- **1990–2005:** Doppelgeflecht (Double Braid) wird Standard im gehobenen Segment. Polyform etabliert sich als Fender-Marktführer. Erste HMPE-Leinen (Dyneema) im Regattasport.
- **2005–2015:** Vorgefertigte Festmacher mit angespleißten Augen. Polyester-Festmacher gewinnen Marktanteile (weniger Dehnung, besser für Mittelmeer-Muringleinen). Stufenfender und Flachfender für Superyachten.
- **2015–heute:** Hochleistungsfasern (HMPE, Vectran) auch im Fahrtenseglerbereich. Intelligente Fenderhalter mit Schnellverschluss. Pneumatische Fender für Megayachten. Nachhaltige Materialien (recyceltes PET) als Nischenprodukt.

### 1.4 Qualitätsprinzipien für die AYDI-Bewertung

Jede Festmacher-/Fender-Bewertung in AYDI folgt diesen Grundsätzen:

1. **Confidence-Level auf jedem Befund.** Ein Festmacher-Befund aus einer Fotoanalyse erhält maximal `visual_medium`. Nur eine dokumentierte Bruchlastprüfung oder Herstellerangabe erhält `measured`.
2. **Bootsklassen-Kalibrierung.** Ein 12 mm Festmacher ist für eine 8-m-Yacht angemessen, für eine 15-m-Yacht gefährlich unterdimensioniert. Alle Bewertungen sind relativ zur Bootsgröße, Verdrängung und Windangriffsfläche.
3. **"Nicht beurteilbar" vor Spekulation.** Wenn der Leinendurchmesser auf einem Foto nicht erkennbar ist, gibt AYDI `visual_insufficient` zurück, keine Vermutung.
4. **Mehrfachvalidierung.** Wenn Spezifikationen 16 mm Festmacher angeben, das Foto aber deutlich dünnere Leinen zeigt, wird der Widerspruch gemeldet — nicht gemittelt.
5. **Zustandsbewertung.** Festmacherleinen und Fender unterliegen Verschleiß. AYDI bewertet nicht nur die Dimensionierung, sondern auch den sichtbaren Zustand (UV-Degradation, Schamfilschäden, Fenderverformung).

### 1.5 Geltungsbereich dieser Wissensdatei

Diese Datei deckt ab:
- Alle relevanten Festmacherleinentypen für Segel- und Motoryachten von 6 bis 30+ Metern
- Alle relevanten Fendertypen inkl. Spezialfender
- Dimensionierungsrichtlinien nach Bootsgröße, Verdrängung und Einsatzgebiet
- Bruchlast-Daten nach Fasermaterial und Konstruktionsart
- Herstellerdaten mit Maßen, Preisen und Artikelnummern
- Fehlerbild-Erkennung für die visuelle AYDI-Analyse
- Pydantic-v2-Modelle für die Integration in die AYDI-Analysepipeline

**Nicht abgedeckt** (→ separate Wissensdateien):
- Anker und Ankerketten → 13_01, 13_02
- Ankerwinden → 13_03
- Snubber und Anker-Reitgewichte → 13_02
- Mooringleinen (Dauerlieger) als eigenes Thema → zukünftige Wissensdatei

### 1.6 Relevante Normen und Standards

| Norm | Titel | Relevanz für AYDI |
|------|-------|-------------------|
| ISO 15084:2003 | Small craft — Anchoring, mooring and towing — Strong points | Definiert Anforderungen an Festmacherpunkte (Klampen, Poller) |
| ISO 1140:2012 | Fibre ropes — Polyamide (Nylon) — 3-strand | Spezifikation für Nylon-Festmacher |
| ISO 1141:2012 | Fibre ropes — Polyester — 3-strand | Spezifikation für Polyester-Festmacher |
| ISO 10325:2009 | Fibre ropes — HMPE (Dyneema/Spectra) | Spezifikation für HMPE-Leinen |
| DIN EN ISO 1968 | Faserseile und Tauwerk — Vokabular | Terminologie-Standard |
| DIN EN ISO 2307 | Faserseile — Bestimmung physikalischer Eigenschaften | Prüfverfahren für Festmacher |
| ABYC H-40 | Anchoring, Mooring and Strong Points | US-Standard für Festmacherpunkte |
| CE 2013/53/EU | Recreational Craft Directive | Rahmenrichtlinie für Sportbootausrüstung |
| GL Rules | Germanischer Lloyd — Yacht Rules | Klassifikationsregeln, inkl. Festmacherausrüstung |

### 1.7 AYDI-Analysepipeline für Festmachersysteme

Die Festmacher-/Fender-Analyse in AYDI wird durch folgende Pipelines gespeist:

**Pipeline A (Strukturdaten):**
- CAD-Daten: Klampen-Positionen, Klüsen-Durchmesser, Fenderhaken-Abstände
- Spezifikationen: Leinendurchmesser, -material, -länge, Fendertyp und -größe
- Bootsdaten: LOA, Breite, Freibord, Verdrängung, Windangriffsfläche
- Confidence: `measured` (Level 2) oder `estimated` (Level 1)

**Pipeline B (Visuell):**
- Fotos: Leinenzustand, Schamfilschäden, Fenderposition, Fendergröße relativ zum Boot
- Erkennung: Leinentyp (gedreht vs. geflochten), Fenderform, UV-Schäden, Knoten vs. Auge
- Confidence: `visual_high` bis `visual_insufficient`

**Pipeline C (Text):**
- Serviceberichte: Leinenwechsel-Dokumentation, Schadensprotokolle
- Eigner-Feedback: Berichte über Festmacherprobleme bei Starkwind
- Confidence: `documented`

---

## 2. Grundlagen und Theorie

### 2.1 Kräfte beim Festmachen — Physikalische Grundlagen

Beim Festmachen einer Yacht wirken verschiedene Kräfte, die durch die Festmacherleinen aufgenommen werden müssen:

**Windlast auf eine festgemachte Yacht:**

Die Windkraft auf eine Yacht berechnet sich nach:
```
F_wind = 0.5 × ρ_luft × C_d × A × v²
```

Wobei:
- ρ_luft = 1,225 kg/m³ (Luftdichte auf Meereshöhe)
- C_d = Widerstandsbeiwert (0,8–1,2 für Yachten, abhängig von Aufbauten)
- A = Windangriffsfläche (m²) — projizierte Fläche querab
- v = Windgeschwindigkeit (m/s)

**Windangriffsflächen typischer Yachten (querab):**

| Bootsgröße (LOA) | Segelyacht (A_quer, m²) | Motoryacht (A_quer, m²) | Confidence |
|-------------------|-------------------------|-------------------------|------------|
| 8 m | 8–12 | 10–15 | estimated |
| 10 m | 12–18 | 16–24 | estimated |
| 12 m | 18–26 | 24–35 | estimated |
| 14 m | 24–34 | 32–48 | estimated |
| 16 m | 30–42 | 42–60 | estimated |
| 18 m | 36–50 | 52–75 | estimated |
| 20 m | 42–60 | 65–95 | estimated |
| 25 m | 55–80 | 85–130 | estimated |
| 30 m | 70–100 | 110–170 | estimated |

**Windkraft-Beispielrechnung (12 m Segelyacht, A = 22 m², C_d = 1,0):**

| Windstärke (Bft) | Windgeschwindigkeit (m/s) | Windkraft (kN) | Windkraft (kg) | Confidence |
|-------------------|--------------------------|----------------|----------------|------------|
| 4 | 7 | 0,66 | 67 | calculated |
| 5 | 10 | 1,35 | 138 | calculated |
| 6 | 13 | 2,28 | 232 | calculated |
| 7 | 16 | 3,45 | 352 | calculated |
| 8 | 20 | 5,39 | 550 | calculated |
| 9 | 24 | 7,76 | 792 | calculated |
| 10 | 28 | 10,57 | 1.078 | calculated |

**Wichtig:** Bei Böen kann die Windgeschwindigkeit kurzzeitig 30–50 % über dem Mittel liegen. Die Kraft steigt quadratisch → eine 40 %-Böe ergibt nahezu doppelte Kraft!

### 2.2 Stoßbelastung (Surge Loading)

Die größte Gefahr für Festmacherleinen ist nicht die statische Windlast, sondern die dynamische Stoßbelastung (Surge Loading). Wenn eine Yacht in einer Böe gegen die Leine ruckt, treten kurzzeitig Kräfte auf, die das 3- bis 5-fache der statischen Windlast erreichen können.

**Surge-Faktoren:**

| Bedingung | Surge-Faktor | Erklärung | Confidence |
|-----------|-------------|-----------|------------|
| Ruhiges Wasser, gleichmäßiger Wind | 1,0–1,5 | Minimale Dynamik | documented |
| Leichter Schwell, böiger Wind | 1,5–2,5 | Normaler Hafenbetrieb | documented |
| Starker Schwell, Sturmböen | 2,5–4,0 | Exponierter Liegeplatz | documented |
| Offene Reede, Dünung + Sturm | 4,0–6,0 | Extremsituation | estimated |

**Berechnung der erforderlichen Bruchlast:**
```
Bruchlast_min = F_wind_statisch × Surge_Faktor × Sicherheitsfaktor
```

Der Sicherheitsfaktor beträgt typischerweise:
- 3,0 für neue Leinen
- 5,0 für Leinen mit unbekanntem Alter/Zustand
- 7,0 für Dauerlieger (permanente Muringleinen)

### 2.3 Leinenarten und ihre Funktion

Beim Festmachen einer Yacht an einem Steg oder einer Pier werden verschiedene Leinen verwendet, jede mit einer spezifischen Funktion:

#### 2.3.1 Vorleine (Bow Line / Head Line)

- **Führung:** Vom Bug schräg nach vorn zum Steg
- **Funktion:** Verhindert Rückwärtsbewegung der Yacht
- **Winkel:** Idealerweise 30–45° zur Bootslängsachse
- **Belastung:** Mittel bis hoch (Windlast von achtern)
- **Länge:** Ca. 1,5 × Freibordhöhe + Stegabstand + Reserve
- **Kritisch bei:** Achterlichem Wind, ablaufendem Strom

#### 2.3.2 Achterleine (Stern Line)

- **Führung:** Vom Heck schräg nach achtern zum Steg
- **Funktion:** Verhindert Vorwärtsbewegung der Yacht
- **Winkel:** Idealerweise 30–45° zur Bootslängsachse
- **Belastung:** Mittel bis hoch (Windlast von vorn)
- **Länge:** Ca. 1,5 × Freibordhöhe + Stegabstand + Reserve
- **Kritisch bei:** Vorlichem Wind, anlaufendem Strom

#### 2.3.3 Vorspring (Forward Spring Line)

- **Führung:** Vom Bug schräg nach achtern zum Steg
- **Funktion:** Verhindert Vorwärtsbewegung, fängt Surge ab
- **Winkel:** Möglichst flach (10–20° zur Bootslängsachse)
- **Belastung:** Hoch — Hauptlast bei Surge-Loading
- **Länge:** Ca. 0,7 × LOA (idealerweise länger)
- **Kritisch bei:** Böen, Schwell, Wellenschlag von Passierern
- **Besonderheit:** Die wichtigste Festmacherleine überhaupt. Eine gut belegte Vorspring kann allein die Yacht am Steg halten.

#### 2.3.4 Achterspring (Aft Spring Line)

- **Führung:** Vom Heck schräg nach vorn zum Steg
- **Funktion:** Verhindert Rückwärtsbewegung, fängt Surge ab
- **Winkel:** Möglichst flach (10–20° zur Bootslängsachse)
- **Belastung:** Hoch — Hauptlast bei Surge-Loading
- **Länge:** Ca. 0,7 × LOA (idealerweise länger)
- **Kritisch bei:** Böen, Schwell, Wellenschlag

#### 2.3.5 Brustleine (Breast Line)

- **Führung:** Querab vom Boot direkt zum Steg
- **Funktion:** Hält die Yacht nah am Steg, verhindert seitliches Abtreiben
- **Winkel:** 90° zur Bootslängsachse
- **Belastung:** Gering bei Wind längs, sehr hoch bei Wind querab
- **Länge:** Ca. Freibordhöhe + Stegabstand
- **Kritisch bei:** Auf- und ablandigem Wind
- **Vorsicht:** Brustleinen sollten NICHT zu straff belegt werden — sie verhindern die nötige Pendelbewegung und überlasten Klampen bei Schwell!

#### 2.3.6 Muringleine (Mooring Line / Lazy Line)

- **Führung:** Vom Heck (oder Bug) zum Muringblock am Grund
- **Funktion:** Hält das Boot auf Abstand zum Steg bei Heckanleger (Mittelmeer-Manier)
- **Material:** Oft Polyester (weniger Dehnung, da ständig unter Last)
- **Belastung:** Mittel, aber dauerhaft
- **Besonderheit:** Wird oft vom Hafen gestellt → Zustand unbekannt, Durchmesser ungenügend

### 2.4 Leinenelastizität — Die wichtigste Eigenschaft

Die Dehnungseigenschaften einer Festmacherleine sind für die Stoßdämpfung entscheidend. Verschiedene Materialien zeigen grundlegend unterschiedliches Dehnungsverhalten:

**Dehnung bei 30 % der Bruchlast (typische Maximallast beim Festmachen):**

| Material | Konstruktion | Dehnung bei 30 % BL | Energieabsorption | Confidence |
|----------|-------------|---------------------|-------------------|------------|
| Nylon (Polyamid) | 3-karätiges Tauwerk | 15–20 % | Sehr hoch | measured |
| Nylon (Polyamid) | Doppelgeflecht | 10–15 % | Hoch | measured |
| Polyester | 3-karätiges Tauwerk | 8–12 % | Mittel | measured |
| Polyester | Doppelgeflecht | 6–10 % | Mittel-niedrig | measured |
| HMPE (Dyneema) | Geflecht | 1–3 % | Sehr niedrig | measured |
| Polypropylen | 3-karätiges Tauwerk | 12–18 % | Mittel-hoch | measured |

**Warum Dehnung wichtig ist:**
- Eine Festmacherleine mit 15 % Dehnung bei 10 m Länge gibt 1,5 m nach, bevor die volle Kraft auf die Klampe wirkt.
- Eine HMPE-Leine gleicher Länge gibt nur 0,2 m nach → die Stoßkraft auf die Klampe ist um ein Vielfaches höher.
- Regel: **Nylon ist das beste Material für Festmacher**, weil es als einziges Fasermaterial hohe Bruchlast mit hoher Dehnung kombiniert.

### 2.5 Dehnungs-Ermüdung (Cyclic Loading)

Nylon verliert bei wiederholter Be- und Entlastung (zyklische Belastung) an Festigkeit:

| Zyklen (30 % BL) | Restbruchlast (%) | Zustand | Confidence |
|-------------------|--------------------|---------|------------|
| 0 (neu) | 100 | Neuzustand | measured |
| 1.000 | 95–98 | Wie neu | measured |
| 5.000 | 88–93 | Leichte Ermüdung | measured |
| 10.000 | 80–88 | Moderate Ermüdung | measured |
| 25.000 | 70–80 | Deutliche Ermüdung, Austausch planen | documented |
| 50.000 | 55–70 | Sicherheitsgrenze erreicht | documented |
| 100.000 | 40–55 | Austausch zwingend erforderlich | estimated |

**Praxisrelevanz:** Eine Yacht, die 100 Nächte pro Saison am Steg liegt und pro Nacht 50 Belastungszyklen durch Schwell erfährt, erreicht nach einer Saison 5.000 Zyklen. Nach 5 Saisons sind 25.000 Zyklen erreicht → Austausch planen.

### 2.6 Knoteneffizienz und Spleißen

Jeder Knoten reduziert die Bruchlast einer Leine erheblich. Die Knoteneffizienz gibt an, welcher Anteil der Bruchlast nach dem Knoten verbleibt:

| Verbindungsart | Knoteneffizienz | Empfehlung | Confidence |
|----------------|----------------|------------|------------|
| Gespleißtes Auge | 90–95 % | Standard für Festmacher | measured |
| Palstek (Bowline) | 60–65 % | Akzeptabel, nicht optimal | measured |
| Webeleinstek (Clove Hitch) | 55–60 % | Nur als temporäre Belegung | measured |
| Achterknoten (Figure 8) | 70–75 % | Stopperknoten | measured |
| Klampe (richtig belegt) | 85–90 % | Standard-Belegung | documented |
| Rundtörn + halbe Schläge | 60–70 % | An Ringen und Pollern | documented |

**Empfehlung:** Festmacherleinen immer mit gespleißtem Auge verwenden. Vorgefertigte Leinen mit werkseitig eingespleißtem Auge (ca. 30–50 cm) sind Standard. Palstek nur als Notlösung.

### 2.7 Schamfilen — Der häufigste Versagensgrund

Schamfilen (Chafe) ist die Reibung einer Leine an einer scharfen Kante, Klüse, Relingstütze oder am Steg selbst. Schamfilen ist mit Abstand der häufigste Grund für Leinenversagen bei Yachten.

**Schamfilraten verschiedener Materialien (relative Beständigkeit):**

| Material | Schamfilbeständigkeit | Relative Lebensdauer | Confidence |
|----------|-----------------------|---------------------|------------|
| Polyester (Doppelgeflecht) | Sehr hoch | 100 % (Referenz) | measured |
| Nylon (Doppelgeflecht) | Hoch | 70–85 % | measured |
| Nylon (3-karätiges) | Mittel-hoch | 60–75 % | measured |
| Polypropylen | Niedrig | 30–40 % | measured |
| HMPE (Dyneema) | Mittel | 50–65 % | measured |

**Schutzmaßnahmen:**
1. **Schamfilschutz-Schlauch:** PVC- oder Leder-Schlauch über die Leine an Kontaktstellen. Standard bei Langfahrtseglern.
2. **Chafe Guard:** Textile Schutzmanschette, per Klett befestigt. Einfach nachzurüsten.
3. **Klüsenleder:** Traditionell Leder, modern Kevlar-Gewebe in der Klüse.
4. **Leinenführung:** Leine so führen, dass sie nicht über scharfe Kanten läuft. Leinenrollen oder Umlenkblöcke verwenden.
5. **Regelmäßige Kontrolle:** Bei Starkwind alle 4–6 Stunden Leinen kontrollieren und ggf. Position verschieben ("Leinen versetzen").

### 2.8 Tidenhub und Festmacher

In Gezeitenrevieren muss die Festmacherlänge den Tidenhub berücksichtigen:

**Erforderliche Leinenlänge bei Tidenhub:**
```
L_min = √(H_max² + D²) + Reserve

H_max = maximale Freibordänderung (Tidenhub × Schwimmfaktor)
D = horizontaler Abstand Boot–Steg
Reserve = 1–2 m für Schwellbewegungen
```

**Beispiel:** Tidenhub 4 m, Stegabstand 2 m:
- H_max ≈ 4 m, D = 2 m
- L_min = √(16 + 4) + 1,5 = √20 + 1,5 = 4,47 + 1,5 ≈ 6 m
- Empfehlung: mindestens 6 m Festmacherleine für eine Brustleine

**Kritisch:** Bei großem Tidenhub und kurzen Leinen kann die Yacht bei Niedrigwasser unter den Steg gedrückt werden oder bei Hochwasser am Steg "hängen". Beides ist gefährlich und kann zu Totalverlust führen.

### 2.9 Windlast-Diagramm nach Bootsklasse

**Querkraft durch Wind in kN (bei querab stehendem Boot):**

| LOA | Bft 5 (10 m/s) | Bft 6 (13 m/s) | Bft 7 (16 m/s) | Bft 8 (20 m/s) | Bft 9 (24 m/s) | Confidence |
|-----|-----------------|-----------------|-----------------|-----------------|-----------------|------------|
| 8 m (SY) | 0,6 | 1,0 | 1,6 | 2,5 | 3,5 | calculated |
| 10 m (SY) | 0,9 | 1,6 | 2,4 | 3,7 | 5,3 | calculated |
| 12 m (SY) | 1,4 | 2,3 | 3,5 | 5,4 | 7,8 | calculated |
| 14 m (SY) | 1,8 | 3,0 | 4,5 | 7,0 | 10,1 | calculated |
| 16 m (MY) | 3,2 | 5,2 | 7,9 | 12,3 | 17,8 | calculated |
| 20 m (MY) | 5,8 | 9,6 | 14,5 | 22,6 | 32,6 | calculated |
| 25 m (MY) | 8,0 | 13,1 | 19,8 | 31,0 | 44,6 | calculated |
| 30 m (MY) | 10,4 | 17,1 | 25,9 | 40,5 | 58,3 | calculated |

SY = Segelyacht, MY = Motoryacht (höhere Aufbauten = mehr Windangriffsfläche)

### 2.10 Belastungsverteilung auf Festmacher

Bei korrekt angelegten Festmachern verteilt sich die Last wie folgt:

**Windlast querab (typische Verteilung):**
- Vorleine: 20–25 %
- Achterleine: 20–25 %
- Vorspring: 15–20 %
- Achterspring: 15–20 %
- Brustleine(n): 20–30 %

**Windlast längs (von vorn):**
- Achterleine: 35–45 %
- Achterspring: 35–45 %
- Vorleine: 5–10 %
- Vorspring: 10–15 %

**Windlast längs (von achtern):**
- Vorleine: 35–45 %
- Vorspring: 35–45 %
- Achterleine: 5–10 %
- Achterspring: 10–15 %

### 2.11 Fendertheorie — Energieabsorption

Fender müssen die kinetische Energie einer sich bewegenden Yacht aufnehmen, bevor der Rumpf den Steg berührt. Die Energieabsorption eines Fenders hängt ab von:

**Kinetische Energie beim Anlegen:**
```
E = 0.5 × m × v² × C_m × C_s × C_c
```

Wobei:
- m = Verdrängung der Yacht (kg)
- v = Annäherungsgeschwindigkeit (m/s) — typisch 0,1–0,3 m/s
- C_m = Masse-Koeffizient (1,5–1,8 für Seitwärtsbewegung durch mitbewegtes Wasser)
- C_s = Weichheits-Koeffizient (0,9 bei steifer Stegkante, 1,0 bei weicher)
- C_c = Konfigurationskoeffizient (0,5–1,0, abhängig von Kontaktpunkt)

**Beispiel:** 12 m Segelyacht (8.000 kg), v = 0,15 m/s, C_m = 1,7:
```
E = 0,5 × 8.000 × 0,15² × 1,7 × 0,9 × 0,7 = 96 J ≈ 100 J
```

Ein einzelner Fender muss mindestens 100 J absorbieren können. Bei Schwell und Strömung steigt der Wert auf 200–500 J.

---

## 3. Typenübersicht

### 3.1 Festmacherleinen — Konstruktionsarten

#### 3.1.1 Dreikarätiges Tauwerk (Three-Strand Twisted Rope)

**Aufbau:** Drei Garnstränge (Kardeele) werden gegenläufig verdreht (geschlagen). Die Verdrehung erzeugt Stabilität und kontrollierte Dehnung.

**Eigenschaften:**
- Höchste Dehnung aller Konstruktionsarten → beste Stoßdämpfung
- Einfach zu spleißen (Augenspeiß in 5–10 Minuten)
- Günstiger als Geflechte
- Verdreht sich bei Belastung (Kinken)
- Etwas geringere Bruchlast als Doppelgeflecht gleichen Durchmessers
- Rauere Oberfläche, weniger angenehm in der Hand

**Einsatz:** Standard-Festmacher für Fahrtenyachten. Preis-Leistungs-Sieger. Empfohlen als primäre Festmacherleine.

**Durchmesserbereich:** 10–24 mm (Yachten), 28–80 mm (Großyachten/Berufsschifffahrt)

#### 3.1.2 Doppelgeflecht (Double Braid)

**Aufbau:** Ein geflochtener Kern (Seele) wird von einem geflochtenen Mantel (Cover) umschlossen. Kern und Mantel tragen jeweils ca. 50 % der Last.

**Eigenschaften:**
- Geringere Dehnung als dreikarätiges Tauwerk (ca. 70–80 % der Dehnung)
- Kein Verdrehen/Kinken → liegt ruhig auf der Klampe
- Angenehm in der Hand, geschmeidig
- Höhere Bruchlast bei gleichem Durchmesser
- Teurer als dreikarätiges Tauwerk (ca. 30–60 % Aufpreis)
- Spleißen erfordert mehr Erfahrung

**Einsatz:** Gehobene Fahrtenyachten, Charteryachten (ästhetisch ansprechender), Blauwasseryachten (kein Kinken bei langen Leinen).

**Durchmesserbereich:** 10–24 mm (Yachten), 28–50 mm (Großyachten)

#### 3.1.3 Achtfachgeflecht (Octoplait / Multiplait)

**Aufbau:** Acht Stränge werden in Vierer-Paaren paarweise rechts und links geflochten. Konstruktionsmerkmal: quadratischer Querschnitt.

**Eigenschaften:**
- Dehnung ähnlich dreikarätiges Tauwerk
- Kein Verdrehen/Kinken
- Einfacher zu spleißen als Doppelgeflecht
- Etwas geringere Bruchlast als Doppelgeflecht
- Guter Kompromiss zwischen Preis und Handhabung

**Einsatz:** Beliebt in Großbritannien und Skandinavien. Gute Alternative zum dreikarätigen Tauwerk.

**Durchmesserbereich:** 12–24 mm (Yachten)

#### 3.1.4 Vorgefertigte Festmacher (Pre-Spliced Mooring Lines)

**Aufbau:** Fertige Festmacherleine mit werksseitig eingespleißtem Auge (Kausche optional) an einem oder beiden Enden.

**Eigenschaften:**
- Sofort einsatzbereit, kein Spleißen erforderlich
- Professionelle Spleißqualität (Knoteneffizienz 90–95 %)
- Definierte Längen (meist 6, 8, 10, 12, 14, 16, 20 m)
- Aufpreis gegenüber Meterware ca. 20–40 %

**Einsatz:** Standard für Serienyachten und Nachrüstung. Empfehlung für alle Eigner, die nicht selbst spleißen.

#### 3.1.5 Langfestmacher (Long Lines)

**Aufbau:** Überlange Festmacherleinen (15–30 m), oft mit Augen an beiden Enden.

**Eigenschaften:**
- Ermöglichen große Schwojbewegung bei Tidenhub
- Mehr Dehnung durch größere Länge → bessere Stoßdämpfung
- Wichtig für exponierte Liegeplätze und Gezeitenreviere
- Handling schwieriger (schwerer, sperriger)

**Einsatz:** Gezeitenreviere (UK, Normandie, Bretagne), exponierte Liegeplätze, Päckchen-Situationen.

#### 3.1.6 Springleinen (Spring Lines)

**Aufbau:** Technisch identisch mit anderen Festmacherleinen, aber spezifisch für den Einsatz als Springs bemessen.

**Eigenschaften:**
- Sollten die längsten Leinen im Set sein (mind. 0,7 × LOA, besser gleich LOA)
- Hohe Elastizität besonders wichtig (Surge-Dämpfung)
- Flacher Winkel zur Bootslängsachse entscheidend

**Einsatz:** Unverzichtbar an jedem Liegeplatz. Die beiden wichtigsten Festmacherleinen.

### 3.2 Fendertypen

#### 3.2.1 Zylindrischer Fender (Cylindrical Fender)

**Form:** Länglicher Zylinder mit Aufhängungsösen (Augen) an beiden Enden.

**Eigenschaften:**
- Standard-Fenderform für 90 % aller Anwendungen
- Horizontale und vertikale Aufhängung möglich
- Gutes Verhältnis Energieabsorption zu Volumen
- Gute Abrollwirkung am Steg
- Leicht zu verstauen (stapelbar)

**Größenbereich:**
| Bezeichnung | Durchmesser (mm) | Länge (mm) | Für Bootslänge |
|-------------|-----------------|------------|----------------|
| Mini | 100–120 | 300–400 | Jollenklasse |
| S | 150 | 500–580 | 6–8 m |
| M | 180–200 | 600–700 | 8–10 m |
| L | 210–240 | 700–850 | 10–12 m |
| XL | 250–290 | 800–1.000 | 12–15 m |
| XXL | 300–350 | 900–1.200 | 15–20 m |
| Superyacht | 350–500 | 1.000–1.800 | 20–30 m |

**Einsatz:** Universell. Für jedes Boot geeignet. Mindestens 6 Stück an Bord.

#### 3.2.2 Kugelfender (Ball Fender / Round Fender)

**Form:** Kugelförmig (sphärisch), mit einer zentralen Aufhängungsöse (Auge) oben und einer optionalen unten.

**Eigenschaften:**
- Höchste Energieabsorption pro Volumeneinheit
- Allseitig gleichmäßiger Schutz
- Rollen leicht weg → schwieriger zu positionieren
- Weniger Kontaktfläche als Zylinderfender
- Schwieriger zu verstauen (nicht stapelbar)

**Größenbereich:**
| Bezeichnung | Durchmesser (mm) | Für Bootslänge |
|-------------|-----------------|----------------|
| S | 250 | 6–8 m |
| M | 300–350 | 8–12 m |
| L | 400–450 | 12–16 m |
| XL | 500–550 | 16–20 m |
| XXL | 600–700 | 20–30 m |

**Einsatz:** Bug- und Heckschutz. Gut für Päckchen (allseitiger Schutz). Beliebt für den Bug in Heckanleger-Situationen (Mittelmeer).

#### 3.2.3 Flachfender (Flat Fender / Panel Fender)

**Form:** Flache, rechteckige oder halbrunde Platten mit mehreren Aufhängungspunkten.

**Eigenschaften:**
- Maximale Kontaktfläche → minimale Punktbelastung auf den Rumpf
- Können direkt am Rumpf befestigt bleiben (bei Superyachten Standard)
- Geringe Energieabsorption (wenig Verformungsweg)
- Nur für paralleles Liegen am Steg geeignet
- Ästhetisch unauffällig

**Einsatz:** Superyachten, Megayachten, permanente Liegeplätze. Für kleinere Yachten als Ergänzung an spezifischen Stellen (Rumpfknick, Wasserpass).

#### 3.2.4 Pneumatischer Fender (Pneumatic Fender)

**Form:** Zylindrisch oder torusförmig, luftgefüllt (Überdruck), mit faserverstärkter Gummihülle.

**Eigenschaften:**
- Extreme Energieabsorption (für Schiffe und Megayachten)
- Druck einstellbar → Härte anpassbar
- Sehr schwer und sperrig
- Wartungsintensiv (Druckkontrolle)
- Hoher Preis

**Größenbereich:** Ab 500 mm Durchmesser, bis mehrere Meter. Für Yachten ab 25 m relevant.

**Einsatz:** Megayachten (25 m+), Hafeninfrastruktur, kommerzielle Schifffahrt.

#### 3.2.5 Stufenfender (Step Fender / Pontoon Fender)

**Form:** C-förmiger oder L-förmiger Querschnitt, wird am Steg oder am Ponton befestigt.

**Eigenschaften:**
- Permanenter Schutz am Steg, nicht am Boot
- Schützt die gesamte Steglänge gleichmäßig
- Boot braucht keine eigenen Fender am Steg (wenn korrekt installiert)
- Kein Verrutschen möglich
- Relativ harter Stoß (wenig Verformung)

**Einsatz:** Moderne Schwimmstege, Marinas, Dauerliegeplätze. Ergänzung zu Boot-Fendern, kein Ersatz!

#### 3.2.6 Fenderbretter (Fender Boards)

**Form:** Horizontales Brett (Holz, GFK oder Kunststoff), vor dem zwei oder mehr Zylinderfender hängen.

**Eigenschaften:**
- Verteilt die Last über die gesamte Brettlänge → gleichmäßiger Schutz
- Überbrückt Stegpfosten, Pfahlnasen und Kanten
- Verhindert, dass Fender zwischen Boot und Steg nach oben oder unten rutschen
- Schützt bei Pfahl-Liegeplätzen zuverlässig
- Handling umständlich (sperrig, schwer)

**Dimensionierung:**
| Bootslänge | Brettlänge (mm) | Brettbreite (mm) | Brettdicke (mm) | Confidence |
|------------|-----------------|-------------------|-----------------|------------|
| 8–10 m | 600–800 | 150–200 | 30–40 | documented |
| 10–14 m | 800–1.200 | 200–250 | 40–50 | documented |
| 14–18 m | 1.200–1.500 | 250–300 | 50–60 | documented |
| 18–25 m | 1.500–2.000 | 300–400 | 60–80 | estimated |

**Einsatz:** Pfahl-Liegeplätze (z.B. Nordsee-Häfen), unebene Stegkanten, Schleusen. Unverzichtbar in vielen Revieren!

#### 3.2.7 Langfender (Bow/Stern Fender)

**Form:** Verlängerter zylindrischer Fender mit spitz zulaufenden Enden, speziell für Bug und Heck.

**Eigenschaften:**
- Schützt empfindliche Bug- und Heckbereiche
- Geringere Energieabsorption als Standard-Zylinderfender
- Oft mit integrierter Aufhängung an Reling oder Bugkorb
- Ästhetisch für den Dauereinsatz am Bug konzipiert

**Einsatz:** Heckanleger (Mittelmeer), Päckchen (Bug-an-Heck), Schleusen.

### 3.3 Festmacher-Sets — Empfohlene Mindestausstattung

| Bootslänge | Vorleinen | Achterleinen | Springs | Brustleinen | Zylinderfender | Kugelfender | Fenderbrett | Reserveleine |
|------------|-----------|-------------|---------|-------------|----------------|-------------|-------------|-------------|
| 6–8 m | 2 | 2 | 2 | 1 | 4 | 2 | 0 | 1 |
| 8–10 m | 2 | 2 | 2 | 2 | 6 | 2 | 1 | 1 |
| 10–12 m | 2 | 2 | 2 | 2 | 6 | 2 | 1 | 2 |
| 12–15 m | 3 | 3 | 2 | 2 | 8 | 2 | 1 | 2 |
| 15–20 m | 3 | 3 | 3 | 2 | 8 | 4 | 2 | 2 |
| 20–25 m | 4 | 4 | 4 | 3 | 10 | 4 | 2 | 3 |
| 25–30 m | 4 | 4 | 4 | 4 | 12 | 4 | 2 | 4 |

---

## 4. Materialien und Fasertechnologie

### 4.1 Nylon (Polyamid 6 / Polyamid 6.6)

**Allgemeines:**
Nylon ist das Standard-Material für Festmacherleinen und wird von allen führenden Tauwerksherstellern als primäres Festmachermaterial empfohlen.

**Physikalische Eigenschaften:**

| Eigenschaft | Wert | Confidence |
|-------------|------|------------|
| Dichte | 1,14 g/cm³ | measured |
| Schmelzpunkt | 220 °C (PA 6), 260 °C (PA 6.6) | measured |
| Dehnung bei Bruch | 15–30 % | measured |
| Wasseraufnahme | 4–8 % (reduziert Bruchlast um 10–15 %) | measured |
| UV-Beständigkeit | Mittel (Additive verbessern) | documented |
| Abriebfestigkeit | Hoch | documented |
| Chemische Beständigkeit | Gut gegen Salzwasser, Öl, Fett | documented |
| Schwimmfähigkeit | Sinkt (Dichte > 1,0) | measured |

**Vorteile für Festmacher:**
- Höchste Elastizität aller synthetischen Fasern → beste Stoßdämpfung
- Hohe Bruchlast pro Durchmesser
- Gute Abriebfestigkeit
- Breite Verfügbarkeit und günstiger Preis
- Leicht zu spleißen

**Nachteile:**
- Verliert 10–15 % Bruchlast bei Nässe
- UV-Empfindlich ohne Additive (15–20 % Festigkeitsverlust nach 12 Monaten Dauerexposition)
- Steift bei Kälte ein (unter 5 °C spürbar, unter −10 °C problematisch)
- Nass gefroren → Bruchlast sinkt um 25–30 %
- Schimmelt bei dauerhafter Feuchtigkeit ohne Trocknung

### 4.2 Polyester (PET / PES)

**Allgemeines:**
Polyester ist die Alternative zu Nylon, insbesondere für Anwendungen mit reduziertem Dehnungsbedarf (Muringleinen, Dauerlieger, Ankerleinen).

**Physikalische Eigenschaften:**

| Eigenschaft | Wert | Confidence |
|-------------|------|------------|
| Dichte | 1,38 g/cm³ | measured |
| Schmelzpunkt | 250–260 °C | measured |
| Dehnung bei Bruch | 10–15 % | measured |
| Wasseraufnahme | <0,5 % (keine Bruchlastreduktion) | measured |
| UV-Beständigkeit | Hoch (besser als Nylon) | documented |
| Abriebfestigkeit | Sehr hoch | documented |
| Chemische Beständigkeit | Sehr gut gegen Salzwasser, Öl, UV | documented |
| Schwimmfähigkeit | Sinkt (Dichte > 1,0) | measured |

**Vorteile:**
- Keine Bruchlastreduktion bei Nässe
- Hervorragende UV-Beständigkeit
- Höchste Abriebfestigkeit aller Standardfasern
- Dimensional stabil (minimales Kriechen)
- Weniger Steifigkeitsänderung bei Kälte als Nylon

**Nachteile:**
- Geringere Elastizität als Nylon → schlechtere Stoßdämpfung
- Bei gleicher Bruchlast ca. 15–20 % schwerer als Nylon
- Etwas steifer und weniger geschmeidig als Nylon

### 4.3 HMPE (High Modulus Polyethylene — Dyneema / Spectra)

**Allgemeines:**
HMPE ist das stärkste verfügbare Fasermaterial für Leinen. Die Bruchlast ist bei gleichem Durchmesser 3–4× höher als Nylon. Allerdings ist HMPE für Festmacher nur bedingt geeignet wegen der extrem geringen Dehnung.

**Physikalische Eigenschaften:**

| Eigenschaft | Wert | Confidence |
|-------------|------|------------|
| Dichte | 0,97 g/cm³ (schwimmt!) | measured |
| Schmelzpunkt | 130–145 °C (niedrig!) | measured |
| Dehnung bei Bruch | 3–4 % | measured |
| Wasseraufnahme | Null | measured |
| UV-Beständigkeit | Mittel bis hoch | documented |
| Abriebfestigkeit | Mittel | documented |
| Chemische Beständigkeit | Exzellent | documented |
| Schwimmfähigkeit | Schwimmt (Dichte < 1,0) | measured |

**Vorteile:**
- Höchste Bruchlast pro Durchmesser und Gewicht
- Schwimmt → wird nicht am Grund aufgerieben
- Null Wasseraufnahme
- Extrem leicht (leichter als Wasser)
- Chemisch nahezu inert

**Nachteile:**
- Minimale Dehnung → keine Stoßdämpfung → nur mit Snubber-System als Festmacher geeignet
- Kriecht unter Dauerlast (Cold Creep bei >30 % BL)
- Niedriger Schmelzpunkt → Reibungswärme kann zum Versagen führen
- Extrem teuer (5–10× Preis von Nylon)
- Schwer zu klemmen (rutscht durch Klampen)
- Nur empfohlen als: Muringleine (mit Nylon-Snubber), Schleppleine, Notfestmacher

### 4.4 Polypropylen (PP)

**Allgemeines:**
Polypropylen ist das günstigste Fasermaterial und wird oft für Schwimmleinen, Badeinseln und temporäre Leinen verwendet. Für Festmacher ist es NICHT geeignet.

**Physikalische Eigenschaften:**

| Eigenschaft | Wert | Confidence |
|-------------|------|------------|
| Dichte | 0,91 g/cm³ (schwimmt) | measured |
| Schmelzpunkt | 160–170 °C | measured |
| Dehnung bei Bruch | 15–25 % | measured |
| UV-Beständigkeit | Sehr niedrig | documented |
| Abriebfestigkeit | Niedrig | documented |

**Einsatz:** NICHT als Festmacher empfohlen. Nur als Schwimmleine, Tripleine, temporäre Hilfsleine.

### 4.5 UV-Beständigkeit — Vergleich

**Restbruchlast nach UV-Exposition (12 Monate Dauerexposition, Mittelmeerbreiten):**

| Material | Nach 6 Monaten | Nach 12 Monaten | Nach 24 Monaten | Nach 36 Monaten | Confidence |
|----------|---------------|-----------------|-----------------|-----------------|------------|
| Nylon (weiß) | 90–95 % | 80–88 % | 65–78 % | 50–65 % | documented |
| Nylon (schwarz/dunkel) | 92–97 % | 85–92 % | 72–84 % | 60–72 % | documented |
| Polyester (weiß) | 95–98 % | 90–95 % | 82–90 % | 75–85 % | documented |
| HMPE (Dyneema) | 93–97 % | 85–92 % | 75–85 % | 65–78 % | documented |
| Polypropylen | 75–85 % | 55–70 % | 35–50 % | 20–35 % | documented |

### 4.6 Schamfilschutz-Materialien

| Material | Einsatzbereich | Lebensdauer | Preis | Confidence |
|----------|---------------|-------------|-------|------------|
| PVC-Schlauch | Universal | 1–3 Saisons | Günstig (5–15 EUR/m) | documented |
| Leder (Rindsleder) | Klüsen, traditionell | 2–5 Saisons | Mittel (15–30 EUR/Stk) | documented |
| Kevlar-Gewebe | Klüsen, Beschläge | 5–10 Saisons | Hoch (25–50 EUR/m) | documented |
| Chafe Guard (textil) | Leinen-Ummantelung | 1–2 Saisons | Günstig (8–20 EUR/Stk) | documented |
| Edelstahl-Rollen | Klüsenersatz | 10–20+ Jahre | Hoch (80–250 EUR/Stk) | documented |
| UHMWPE-Kauschen | Auge/Kausche | 5–10 Saisons | Mittel (15–40 EUR/Stk) | documented |

### 4.7 Fendermaterialien

#### 4.7.1 PVC (Polyvinylchlorid)

**Standardmaterial für 95 % aller Yacht-Fender:**
- Geschäumter PVC-Kern (Weichschaum) für Energieabsorption
- PVC-Außenhaut (glatt oder texturiert) für Abriebfestigkeit
- UV-stabilisiert durch Additive
- Farbbeständig (weiß, blau, schwarz)
- Temperaturbereich: −20 °C bis +60 °C
- Lebensdauer: 5–10 Jahre bei sachgerechter Pflege

#### 4.7.2 Gummi (Naturkautschuk / Synthesekautschuk)

**Premium-Material für Pneumatische und Superyacht-Fender:**
- Höhere Energieabsorption als PVC
- Exzellente UV-Beständigkeit
- Schwarze Farbe kann Rumpfabrieb verursachen (Markierungen!)
- Schwerer als PVC
- Deutlich teurer

#### 4.7.3 EVA-Schaum (Ethylen-Vinylacetat)

**Material für Flachfender und Rumpfschutzmatten:**
- Weich und flexibel
- Sehr leicht
- Geschlossenzellige Struktur (nimmt kein Wasser auf)
- Begrenzte Energieabsorption (nur für leichte Stöße)
- UV-empfindlich ohne Schutzschicht

### 4.8 Materialvergleich — Entscheidungsmatrix Festmacherleinen

| Kriterium | Nylon 3-kar. | Nylon DB | Polyester DB | HMPE | PP |
|-----------|-------------|----------|-------------|------|-----|
| Bruchlast/Durchmesser | ●●●○ | ●●●● | ●●●○ | ●●●●● | ●●○○ |
| Stoßdämpfung | ●●●●● | ●●●● | ●●●○ | ●○○○ | ●●●● |
| Schamfilbeständigkeit | ●●●○ | ●●●● | ●●●●● | ●●●○ | ●●○○ |
| UV-Beständigkeit | ●●●○ | ●●●○ | ●●●●● | ●●●● | ●○○○ |
| Preis (günstig=gut) | ●●●●● | ●●●○ | ●●●○ | ●○○○ | ●●●●● |
| Handhabung | ●●●● | ●●●●● | ●●●●● | ●●○○ | ●●●○ |
| Spleißbarkeit | ●●●●● | ●●●○ | ●●●○ | ●●○○ | ●●●● |
| Gesamtempfehlung | ★★★★★ | ★★★★☆ | ★★★☆☆ | ★★☆☆☆ | ★☆☆☆☆ |

(DB = Doppelgeflecht, ● = Leistung, ★ = Empfehlung als Festmacher)

---

## 5. Produktlinien und Hersteller

### 5.1 Festmacherleinen — Hersteller und Produktlinien

#### 5.1.1 Liros (Deutschland)

**Unternehmen:** Liros GmbH, Berg am Starnberger See. Seit 1850. Einer der führenden europäischen Tauwerkhersteller.

**Festmacher-Produktlinien:**

| Produkt | Material | Konstruktion | Durchmesser | Bruchlast (16 mm) | Preis/m (16 mm) | Confidence |
|---------|----------|-------------|-------------|-------------------|-----------------|------------|
| Liros Squareline | Polyester | 8-fach Flechtung | 10–24 mm | 2.800 kg | 4,50–5,50 EUR | documented |
| Liros Handy Elastic | Nylon | 3-karätiges Tauwerk | 10–20 mm | 3.200 kg | 3,00–4,00 EUR | documented |
| Liros Moorex 12 | Polyester/Nylon Mix | Doppelgeflecht | 10–24 mm | 3.400 kg | 6,00–7,50 EUR | documented |
| Liros Top Cruising | Polyester | Doppelgeflecht | 8–20 mm | 3.000 kg | 5,50–6,50 EUR | documented |
| Liros Dock-Elastic | Nylon | Doppelgeflecht | 10–20 mm | 3.500 kg | 5,00–6,00 EUR | documented |

**Vorgefertigte Festmacher (mit Auge):**

| Produkt | Durchmesser | Länge | Preis (ca.) | Confidence |
|---------|-------------|-------|-------------|------------|
| Liros Festmacher Handy Elastic | 10 mm | 6 m | 18–24 EUR | documented |
| Liros Festmacher Handy Elastic | 12 mm | 8 m | 28–35 EUR | documented |
| Liros Festmacher Handy Elastic | 14 mm | 10 m | 38–48 EUR | documented |
| Liros Festmacher Handy Elastic | 16 mm | 10 m | 48–58 EUR | documented |
| Liros Festmacher Handy Elastic | 18 mm | 12 m | 62–78 EUR | documented |
| Liros Festmacher Handy Elastic | 20 mm | 14 m | 78–95 EUR | documented |
| Liros Festmacher Squareline | 14 mm | 10 m | 55–65 EUR | documented |
| Liros Festmacher Squareline | 16 mm | 12 m | 68–82 EUR | documented |
| Liros Festmacher Squareline | 18 mm | 14 m | 85–105 EUR | documented |
| Liros Festmacher Moorex 12 | 16 mm | 12 m | 85–100 EUR | documented |

#### 5.1.2 Gleistein (Deutschland)

**Unternehmen:** Geo. Gleistein & Sohn GmbH, Bremen. Seit 1824. Premium-Tauwerkhersteller.

**Festmacher-Produktlinien:**

| Produkt | Material | Konstruktion | Durchmesser | Bruchlast (16 mm) | Preis/m (16 mm) | Confidence |
|---------|----------|-------------|-------------|-------------------|-----------------|------------|
| Gleistein Dock | Nylon | 3-karätiges Tauwerk | 10–24 mm | 3.300 kg | 3,50–4,50 EUR | documented |
| Gleistein Dockline | Nylon | Doppelgeflecht | 10–24 mm | 3.600 kg | 6,00–7,50 EUR | documented |
| Gleistein GeoSquare | Polyester | 8-fach Flechtung | 10–24 mm | 2.900 kg | 5,00–6,00 EUR | documented |
| Gleistein MegaTwin | HMPE/Polyester | Doppelgeflecht | 8–20 mm | 8.500 kg | 15,00–22,00 EUR | documented |
| Gleistein HarborLine | Polyester | Doppelgeflecht | 10–20 mm | 3.200 kg | 5,50–7,00 EUR | documented |

**Vorgefertigte Festmacher:**

| Produkt | Durchmesser | Länge | Preis (ca.) | Confidence |
|---------|-------------|-------|-------------|------------|
| Gleistein Dock Festmacher | 12 mm | 8 m | 30–38 EUR | documented |
| Gleistein Dock Festmacher | 14 mm | 10 m | 42–52 EUR | documented |
| Gleistein Dock Festmacher | 16 mm | 12 m | 55–68 EUR | documented |
| Gleistein Dockline Festmacher | 14 mm | 10 m | 70–85 EUR | documented |
| Gleistein Dockline Festmacher | 16 mm | 12 m | 85–105 EUR | documented |

#### 5.1.3 Marlow Ropes (Großbritannien)

**Unternehmen:** Marlow Ropes Ltd, Hailsham, England. Seit 1807. Premium-Hersteller, bekannt für Regatta- und Superyacht-Tauwerk.

**Festmacher-Produktlinien:**

| Produkt | Material | Konstruktion | Durchmesser | Bruchlast (16 mm) | Preis/m (16 mm) | Confidence |
|---------|----------|-------------|-------------|-------------------|-----------------|------------|
| Marlow 3-Strand Nylon | Nylon | 3-karätiges Tauwerk | 10–28 mm | 3.200 kg | 3,80–4,80 EUR | documented |
| Marlow Doublebraid Nylon | Nylon | Doppelgeflecht | 10–24 mm | 3.700 kg | 6,50–8,00 EUR | documented |
| Marlow Classic 8-Plait | Polyamid/Polyester | 8-fach Flechtung | 10–28 mm | 3.000 kg | 4,50–5,50 EUR | documented |
| Marlow Blue Ocean Dock | Polyester | Doppelgeflecht | 10–24 mm | 3.100 kg | 5,00–6,50 EUR | documented |
| Marlow Superline | HMPE | Doppelgeflecht | 8–20 mm | 9.200 kg | 18,00–28,00 EUR | documented |

#### 5.1.4 New England Ropes (USA)

**Unternehmen:** New England Ropes (Teufelberger-Gruppe), Fall River, Massachusetts. Führend im nordamerikanischen Markt.

**Festmacher-Produktlinien:**

| Produkt | Material | Konstruktion | Durchmesser | Bruchlast (16 mm) | Preis/m (16 mm) | Confidence |
|---------|----------|-------------|-------------|-------------------|-----------------|------------|
| NER 3-Strand Nylon | Nylon | 3-karätiges Tauwerk | 10–28 mm | 3.100 kg | 3,50–4,50 EUR | documented |
| NER Double Braid Nylon | Nylon | Doppelgeflecht | 10–24 mm | 3.500 kg | 6,00–7,80 EUR | documented |
| NER Mega Braid | Nylon | 8-fach Flechtung | 12–28 mm | 3.200 kg | 4,80–6,00 EUR | documented |
| NER C2 Dockline | Nylon (C2-Faser) | Doppelgeflecht | 10–20 mm | 3.800 kg | 7,50–9,50 EUR | documented |
| NER STS-HSR | HMPE/Polyester | Doppelgeflecht | 8–20 mm | 8.800 kg | 16,00–25,00 EUR | documented |

#### 5.1.5 Robline (Österreich / FSE Robline)

**Unternehmen:** FSE Robline (Teufelberger-Gruppe), Wels, Österreich. Breites Sortiment für Fahrten- und Regattayachten.

**Festmacher-Produktlinien:**

| Produkt | Material | Konstruktion | Durchmesser | Bruchlast (16 mm) | Preis/m (16 mm) | Confidence |
|---------|----------|-------------|-------------|-------------------|-----------------|------------|
| Robline Dockline | Nylon | 3-karätiges Tauwerk | 10–24 mm | 3.000 kg | 3,00–3,80 EUR | documented |
| Robline Rio | Polyester | Doppelgeflecht | 10–18 mm | 2.800 kg | 4,50–5,50 EUR | documented |
| Robline Admiral 10000 | HMPE/Polyester | Doppelgeflecht | 8–18 mm | 8.200 kg | 14,00–20,00 EUR | documented |
| Robline Mooring Elastic | Nylon | 8-fach Flechtung | 10–20 mm | 3.100 kg | 4,00–5,00 EUR | documented |

### 5.2 Fender — Hersteller und Produktlinien

#### 5.2.1 Polyform (Norwegen)

**Unternehmen:** Polyform AS, Ålesund, Norwegen. Weltweit führender Fenderhersteller. Der Name "Polyform" ist quasi zum Synonym für Yacht-Fender geworden.

**Zylindrische Fender — Serie F:**

| Modell | Durchmesser (mm) | Länge (mm) | Gewicht (kg) | Für Bootslänge | Preis (ca. EUR) | Confidence |
|--------|-----------------|------------|-------------|----------------|----------------|------------|
| F-02 | 200 | 660 | 1,3 | 8–10 m | 45–55 | documented |
| F-1 | 150 | 580 | 0,7 | 6–8 m | 30–38 | documented |
| F-2 | 200 | 660 | 1,3 | 8–10 m | 45–55 | documented |
| F-3 | 220 | 745 | 1,6 | 10–12 m | 55–68 | documented |
| F-4 | 250 | 855 | 2,2 | 12–15 m | 75–90 | documented |
| F-5 | 290 | 980 | 3,0 | 15–18 m | 105–125 | documented |
| F-6 | 340 | 1.120 | 4,3 | 18–22 m | 140–170 | documented |
| F-7 | 375 | 1.260 | 5,6 | 22–25 m | 185–225 | documented |
| F-8 | 400 | 1.370 | 6,8 | 25–30 m | 240–290 | documented |
| F-10 | 450 | 1.550 | 8,5 | 28–35 m | 320–390 | documented |
| F-11 | 500 | 1.720 | 10,5 | 30–40 m | 420–510 | documented |
| F-13 | 570 | 1.940 | 14,0 | 35–45 m | 580–700 | estimated |

**Kugelfender — Serie A:**

| Modell | Durchmesser (mm) | Gewicht (kg) | Für Bootslänge | Preis (ca. EUR) | Confidence |
|--------|-----------------|-------------|----------------|----------------|------------|
| A-0 | 210 | 0,5 | 5–7 m | 18–25 | documented |
| A-1 | 295 | 1,0 | 7–10 m | 32–42 | documented |
| A-2 | 390 | 2,0 | 10–13 m | 55–70 | documented |
| A-3 | 460 | 3,3 | 13–17 m | 85–105 | documented |
| A-4 | 550 | 5,0 | 17–22 m | 130–160 | documented |
| A-5 | 710 | 9,0 | 22–30 m | 220–270 | documented |
| A-6 | 850 | 14,0 | 28–40 m | 380–460 | documented |
| A-7 | 1.040 | 23,0 | 35–50 m | 600–750 | estimated |

**Langfender — Serie NF:**

| Modell | Durchmesser (mm) | Länge (mm) | Für Bootslänge | Preis (ca. EUR) | Confidence |
|--------|-----------------|------------|----------------|----------------|------------|
| NF-4 | 165 | 585 | 8–10 m | 40–50 | documented |
| NF-5 | 210 | 750 | 10–14 m | 60–75 | documented |
| NF-6 | 250 | 900 | 14–18 m | 85–105 | documented |

#### 5.2.2 Dan-Fender (Dänemark)

**Unternehmen:** Dan-Fender A/S, Dänemark. Premium-Fenderhersteller mit besonderem Fokus auf Materialqualität und UV-Beständigkeit.

**Zylindrische Fender — Standardserie:**

| Modell | Durchmesser (mm) | Länge (mm) | Für Bootslänge | Preis (ca. EUR) | Confidence |
|--------|-----------------|------------|----------------|----------------|------------|
| DF 622 | 150 | 580 | 6–8 m | 35–42 | documented |
| DF 623 | 180 | 650 | 8–10 m | 45–55 | documented |
| DF 624 | 210 | 745 | 10–12 m | 60–72 | documented |
| DF 625 | 240 | 855 | 12–15 m | 80–95 | documented |
| DF 626 | 270 | 980 | 15–18 m | 110–130 | documented |
| DF 627 | 310 | 1.100 | 18–22 m | 145–175 | documented |
| DF 628 | 350 | 1.200 | 22–28 m | 195–235 | documented |
| DF 629 | 400 | 1.380 | 28–35 m | 260–320 | documented |

**Besonderheit Dan-Fender:** Doppelventil-System (schnelles Aufblasen und präzise Druckkontrolle). Alle Modelle mit verstärkten Augen und UV-stabilisiertem Premium-PVC.

#### 5.2.3 Majoni (Niederlande)

**Unternehmen:** Majoni, Niederlande. Preis-Leistungs-orientierter Fenderhersteller, sehr verbreitet in europäischen Marinas.

**Zylindrische Fender — Star Serie:**

| Modell | Durchmesser (mm) | Länge (mm) | Für Bootslänge | Preis (ca. EUR) | Confidence |
|--------|-----------------|------------|----------------|----------------|------------|
| Star 1 | 150 | 580 | 6–8 m | 22–28 | documented |
| Star 2 | 180 | 650 | 8–10 m | 30–38 | documented |
| Star 3 | 210 | 745 | 10–12 m | 42–52 | documented |
| Star 4 | 250 | 855 | 12–15 m | 55–68 | documented |
| Star 5 | 290 | 980 | 15–18 m | 75–92 | documented |
| Star 6 | 340 | 1.120 | 18–22 m | 110–130 | documented |

**Flachfender — Majoni Flat Serie:**

| Modell | Breite (mm) | Höhe (mm) | Dicke (mm) | Für Bootslänge | Preis (ca. EUR) | Confidence |
|--------|------------|-----------|------------|----------------|----------------|------------|
| Flat M | 250 | 500 | 70 | 8–12 m | 65–80 | documented |
| Flat L | 300 | 600 | 80 | 12–16 m | 85–105 | documented |
| Flat XL | 350 | 700 | 90 | 16–22 m | 120–150 | documented |

#### 5.2.4 Ocean Fender (Frankreich/International)

**Unternehmen:** Ocean Fenders, Frankreich. Spezialisiert auf Marine-Grade-Fender und Superyacht-Schutz.

**Zylindrische Fender — Heavy Duty Serie:**

| Modell | Durchmesser (mm) | Länge (mm) | Für Bootslänge | Preis (ca. EUR) | Confidence |
|--------|-----------------|------------|----------------|----------------|------------|
| HD 15 | 150 | 580 | 6–8 m | 28–35 | documented |
| HD 20 | 200 | 660 | 8–10 m | 40–50 | documented |
| HD 25 | 250 | 855 | 12–15 m | 65–80 | documented |
| HD 30 | 300 | 1.000 | 15–18 m | 95–115 | documented |
| HD 35 | 350 | 1.200 | 18–25 m | 135–165 | documented |
| HD 40 | 400 | 1.400 | 25–35 m | 200–250 | documented |

**Superyacht-Fender — Ocean SY Serie:**

| Modell | Durchmesser (mm) | Länge (mm) | Für Bootslänge | Preis (ca. EUR) | Confidence |
|--------|-----------------|------------|----------------|----------------|------------|
| SY 500 | 500 | 1.500 | 25–35 m | 550–680 | documented |
| SY 600 | 600 | 1.800 | 30–45 m | 750–920 | documented |
| SY 800 | 800 | 2.200 | 40–60 m | 1.200–1.500 | estimated |
| SY 1000 | 1.000 | 2.800 | 50–80 m | 2.200–2.800 | estimated |

### 5.3 Fender-Zubehör

#### 5.3.1 Fenderhalter und -haken

| Produkt | Material | Für Fender-Ø | Preis (ca. EUR) | Confidence |
|---------|----------|-------------|----------------|------------|
| Fenderhalter Clip (Standard) | Nylon/PA | 150–250 mm | 5–12 | documented |
| Fenderhalter Schnellverschluss | Edelstahl 316L / PA | 150–300 mm | 15–30 | documented |
| Fenderhaken Reling | Edelstahl 316L | für Reling 22–28 mm | 12–25 | documented |
| Fenderleine mit Schnellverschluss | Nylon | Universal | 8–15 | documented |
| Fenderkorb (Superyacht) | Edelstahl 316L poliert | 300–500 mm | 150–350 | documented |

#### 5.3.2 Fenderleinen

Fenderleinen verbinden den Fender mit dem Boot (Reling, Klampe, Fenderhaken). Anforderungen:
- Durchmesser: 6–10 mm (proportional zum Fender)
- Material: Nylon (Standardlösung), Polyester (länger haltbar)
- Länge: min. 2 × Freibord
- Befestigung: Webeleinstek am Fender (nicht Palstek! — muss verstellbar sein)

| Fendergröße (Ø) | Leinendurchmesser | Empfohlene Länge | Confidence |
|-----------------|-------------------|-----------------|------------|
| 150 mm | 6 mm | 1,5–2,5 m | documented |
| 200 mm | 8 mm | 2,0–3,0 m | documented |
| 250 mm | 8 mm | 2,5–3,5 m | documented |
| 300 mm | 10 mm | 3,0–4,0 m | documented |
| 350 mm | 10 mm | 3,5–5,0 m | documented |
| 400+ mm | 12 mm | 4,0–6,0 m | documented |

### 5.4 Preisübersicht — Komplettausstattung nach Bootsgröße

| Bootslänge | Festmacher-Set (6–8 Leinen) | Fender-Set (6–8 Stk) | Fenderbretter (1–2) | Zubehör | Gesamt (ca.) | Confidence |
|------------|---------------------------|---------------------|---------------------|---------|-------------|------------|
| 8 m | 120–180 EUR | 180–260 EUR | 30–50 EUR | 40–60 EUR | 370–550 EUR | estimated |
| 10 m | 180–280 EUR | 250–380 EUR | 40–65 EUR | 50–80 EUR | 520–805 EUR | estimated |
| 12 m | 280–420 EUR | 380–550 EUR | 50–85 EUR | 60–100 EUR | 770–1.155 EUR | estimated |
| 15 m | 400–650 EUR | 550–820 EUR | 65–110 EUR | 80–130 EUR | 1.095–1.710 EUR | estimated |
| 18 m | 600–950 EUR | 780–1.200 EUR | 90–150 EUR | 100–170 EUR | 1.570–2.470 EUR | estimated |
| 20 m | 800–1.300 EUR | 1.000–1.600 EUR | 120–200 EUR | 130–220 EUR | 2.050–3.320 EUR | estimated |
| 25 m | 1.200–2.000 EUR | 1.500–2.500 EUR | 180–300 EUR | 200–350 EUR | 3.080–5.150 EUR | estimated |
| 30 m | 1.800–3.000 EUR | 2.500–4.000 EUR | 250–400 EUR | 300–500 EUR | 4.850–7.900 EUR | estimated |

---

## 6. Dimensionierung

### 6.1 Festmacherleine — Durchmesser nach LOA

Die Dimensionierung der Festmacherleinen richtet sich primär nach der Bootslänge (LOA), der Verdrängung und der Windangriffsfläche. Die folgenden Tabellen gelten für **Nylon-Festmacher** (3-karätiges Tauwerk oder Doppelgeflecht):

**Standard-Dimensionierung (Nylon):**

| LOA | Verdrängung (typ.) | Mindest-Ø | Empfohlen Ø | Schwerwetter-Ø | Bruchlast (empf.) | Confidence |
|-----|--------------------|-----------|-----------|--------------|--------------------|------------|
| 6 m | 1.000–2.000 kg | 10 mm | 12 mm | 14 mm | 2.000 kg | documented |
| 7 m | 1.500–3.000 kg | 10 mm | 12 mm | 14 mm | 2.000 kg | documented |
| 8 m | 2.000–4.000 kg | 12 mm | 14 mm | 16 mm | 2.800 kg | documented |
| 9 m | 3.000–5.000 kg | 12 mm | 14 mm | 16 mm | 2.800 kg | documented |
| 10 m | 4.000–7.000 kg | 14 mm | 16 mm | 18 mm | 3.200 kg | documented |
| 11 m | 5.000–9.000 kg | 14 mm | 16 mm | 18 mm | 3.200 kg | documented |
| 12 m | 6.000–12.000 kg | 16 mm | 18 mm | 20 mm | 4.500 kg | documented |
| 13 m | 8.000–14.000 kg | 16 mm | 18 mm | 20 mm | 4.500 kg | documented |
| 14 m | 9.000–16.000 kg | 18 mm | 20 mm | 22 mm | 5.500 kg | documented |
| 15 m | 10.000–20.000 kg | 18 mm | 20 mm | 24 mm | 5.500 kg | documented |
| 16 m | 12.000–24.000 kg | 20 mm | 22 mm | 24 mm | 7.000 kg | documented |
| 18 m | 15.000–30.000 kg | 22 mm | 24 mm | 28 mm | 8.500 kg | estimated |
| 20 m | 20.000–40.000 kg | 24 mm | 28 mm | 32 mm | 10.000 kg | estimated |
| 25 m | 30.000–70.000 kg | 28 mm | 32 mm | 36 mm | 14.000 kg | estimated |
| 30 m | 50.000–120.000 kg | 32 mm | 36 mm | 40 mm | 18.000 kg | estimated |

**Faustformel (Nylon 3-karätiges):**
```
Durchmesser_mm = LOA_m + 4 (Standard)
Durchmesser_mm = LOA_m + 6 (Schwerwetter / exponierter Liegeplatz)
```

### 6.2 Festmacherleine — Länge

**Empfohlene Mindestlängen:**

| Leinentyp | Mindestlänge | Empfohlen | Tidenhub-Zuschlag | Confidence |
|-----------|-------------|-----------|-------------------|------------|
| Vorleine | 1,0 × LOA | 1,5 × LOA | + Tidenhub × 1,5 | documented |
| Achterleine | 1,0 × LOA | 1,5 × LOA | + Tidenhub × 1,5 | documented |
| Vorspring | 0,7 × LOA | 1,0 × LOA | + Tidenhub × 1,0 | documented |
| Achterspring | 0,7 × LOA | 1,0 × LOA | + Tidenhub × 1,0 | documented |
| Brustleine | 0,5 × LOA | 0,7 × LOA | + Tidenhub × 2,0 | documented |
| Reserveleine | 1,5 × LOA | 2,0 × LOA | — | estimated |

**Beispiel: 12 m Segelyacht, Tidenhub 3 m:**
- Vorleine: min. 12 m, empfohlen 18 m, mit Tide: 18 + 4,5 = 22,5 m → 24 m (nächste Standardlänge)
- Spring: min. 8,4 m, empfohlen 12 m, mit Tide: 12 + 3 = 15 m → 16 m
- Brustleine: min. 6 m, empfohlen 8,4 m, mit Tide: 8,4 + 6 = 14,4 m → 16 m

### 6.3 Fender — Dimensionierung nach Boot

**Fendergröße nach Bootslänge und Freibord:**

| LOA | Freibord (typ.) | Fender-Ø (min.) | Fender-Ø (empf.) | Fender-Länge (empf.) | Anzahl (min.) | Confidence |
|-----|-----------------|----------------|------------------|---------------------|--------------|------------|
| 6 m | 0,3–0,5 m | 100 mm | 150 mm | 450–580 mm | 4 | documented |
| 8 m | 0,4–0,7 m | 150 mm | 180 mm | 500–650 mm | 4 | documented |
| 10 m | 0,5–0,9 m | 180 mm | 200 mm | 600–750 mm | 6 | documented |
| 12 m | 0,6–1,1 m | 200 mm | 220–250 mm | 700–860 mm | 6 | documented |
| 14 m | 0,8–1,3 m | 220 mm | 250–290 mm | 800–1.000 mm | 6 | documented |
| 16 m | 1,0–1,5 m | 250 mm | 290–340 mm | 900–1.120 mm | 8 | documented |
| 18 m | 1,2–1,8 m | 290 mm | 340–375 mm | 1.000–1.260 mm | 8 | documented |
| 20 m | 1,4–2,0 m | 340 mm | 375–400 mm | 1.100–1.370 mm | 8 | documented |
| 25 m | 1,6–2,5 m | 375 mm | 400–450 mm | 1.200–1.550 mm | 10 | estimated |
| 30 m | 2,0–3,0 m | 400 mm | 450–500 mm | 1.300–1.720 mm | 12 | estimated |

**Faustformeln:**
```
Fender-Durchmesser_mm ≈ Freibord_mm × 0,25 (minimum)
Fender-Durchmesser_mm ≈ LOA_m × 15 + 30 (Richtwert)
Fender-Länge_mm ≈ Fender-Durchmesser_mm × 3,0–3,5
Fender-Anzahl ≈ LOA_m / 2 (minimum, aufgerundet, mindestens 4)
```

### 6.4 Fender — Positionierung

**Optimale Fenderposition:**

1. **Breiteste Stelle des Rumpfes:** 1–2 Fender auf Höhe der größten Breite (meist mittschiffs)
2. **Bug-Bereich:** 1 Fender ca. 1–2 m hinter dem Bug (vor der Vorleine)
3. **Heck-Bereich:** 1 Fender ca. 1–2 m vor dem Heck (vor der Achterleine)
4. **Zwischenpositionen:** Gleichmäßig verteilt, Abstand max. 2–3 m
5. **Wasserpass-Höhe:** Fendermitte auf Höhe des Wasserpass (Rumpfknick)

**Höheneinstellung:**
- Fender-Oberkante: leicht über Schandeckel
- Fender-Unterkante: ca. 10–15 cm über Wasserlinie
- Bei Tide: Fender NICHT fest am Reling befestigen → müssen mit dem Wasserstand gleiten können. Fenderleine lang genug!

### 6.5 Dimensionierung bei Sondersituationen

#### 6.5.1 Päckchen (Rafting)

Beim Päckchen (2–3 Boote nebeneinander) steigen die Anforderungen:
- **Festmacher:** 1 Stufe dicker als für Einzelboot (z.B. 16 mm statt 14 mm)
- **Fender:** 1 Größe größer als für Einzelboot. Mindestens 4 Fender zwischen jedem Boot-Paar
- **Kugelfender:** Empfohlen zwischen Bug und Heck benachbarter Boote
- **Fenderbrett:** Stark empfohlen, besonders bei unterschiedlichen Freibordhöhen
- **Springs:** Zwischen allen Booten im Päckchen, nicht nur zum Steg!

#### 6.5.2 Heckanleger (Mittelmeer-Manier)

- **Heckanker oder Muringleine:** Dimensioniert für volle Windlast von vorn
- **Heckleinen:** 2 Achterleinen zum Steg, 16 mm+ (bei 12 m Boot)
- **Bugfender:** 1–2 Kugelfender am Bug (Schutz vor Nachbarboot)
- **Heckfender:** Spezielle Steganlegebumper oder 2 Zylinderfender am Heck

#### 6.5.3 Schleusen

- **Festmacher:** Überlang (mind. 2 × Hubhöhe + LOA)
- **Fender:** Maximale Größe, mindestens 6 Stück, bevorzugt mit Fenderbrett
- **Material:** Nur Leinen mit guter Schamfilbeständigkeit (Schleusenwände sind rau!)
- **Extra-Schamfilschutz:** An allen Kontaktstellen zwingend erforderlich

---

## 7. Fehlerbild-Atlas

### 7.1 Fehlerbild F-FM-001: Unterdimensionierte Festmacherleinen

**Beschreibung:** Festmacherleinen sind für die Bootsgröße zu dünn.

**Visuelle Indikatoren:**
- Leinen wirken optisch "dünn" im Verhältnis zu Klampen und Boot
- Klampen sind deutlich breiter als die Leine
- Leinen zeigen Dehnungsspuren (Welligkeit, dauerhafte Längung)
- Bei Windlast: Leinen stehen stramm und vibrieren

**Risikobewertung:** KRITISCH — Leinenbruch bei Starkwind möglich. Yacht kann abtreiben, Rumpf- und Fremdschäden.

**AYDI-Bewertung:**
- Confidence: `visual_medium` (Durchmesser aus Fotos nur geschätzt)
- Score-Abzug: −30 bis −50 Punkte (Sicherheitsrelevant)
- Empfehlung: "Festmacherleinen mindestens {empf_durchmesser} mm für {loa} m Yacht verwenden."

### 7.2 Fehlerbild F-FM-002: Schamfilschaden an Festmacherleinen

**Beschreibung:** Festmacherleinen zeigen an Kontaktstellen (Klüsen, Reling, Stegkante) deutliche Abriebspuren.

**Visuelle Indikatoren:**
- Aufgeraute Oberfläche, einzelne Fasern stehen ab ("pelzig")
- Abgeflachter Querschnitt an der Schamfilstelle
- Lokale Farbveränderung (heller oder dunkler als Umgebung)
- Im Extremfall: Mantel durchgescheuert, Kern sichtbar (bei Doppelgeflecht)

**Risikobewertung:** HOCH — Leine kann an der Schamfilstelle bei 40–60 % der nominellen Bruchlast versagen.

**AYDI-Bewertung:**
- Confidence: `visual_high` (Schamfilschäden sind optisch gut erkennbar)
- Score-Abzug: −20 bis −40 Punkte
- Empfehlung: "Schamfilschutz anbringen oder Leine ersetzen. Kontaktstelle mit Schlauch/Leder schützen."

### 7.3 Fehlerbild F-FM-003: UV-Degradation an Festmacherleinen

**Beschreibung:** Festmacherleinen zeigen Anzeichen von UV-Alterung durch langfristige Sonnenexposition.

**Visuelle Indikatoren:**
- Ausbleichung der Farbe (weiße Leinen werden gelblich/grau, farbige Leinen verblassen)
- Oberfläche wird spröde und rau
- Pulveriger Abrieb beim Anfassen (fortgeschrittenes Stadium)
- Leicht aufzuspreizen (Faserbündel lösen sich leicht)

**Risikobewertung:** MITTEL bis HOCH — Bruchlastverlust 20–50 % je nach Expositionsdauer.

**AYDI-Bewertung:**
- Confidence: `visual_medium` (Farbveränderung erkennbar, Ausmaß schwer einzuschätzen)
- Score-Abzug: −10 bis −30 Punkte
- Empfehlung: "Leinen mit deutlicher UV-Alterung austauschen. Bei Polyester-Leinen weniger kritisch als bei Nylon."

### 7.4 Fehlerbild F-FM-004: Falsche Knotenverbindung

**Beschreibung:** Festmacherleinen sind mit Knoten statt Spleißaugen befestigt. Knoten reduzieren die Bruchlast um 30–45 %.

**Visuelle Indikatoren:**
- Palstek, Achterknoten oder andere Knoten sichtbar anstelle eines gespleißten Auges
- Mehrere Knoten in einer Leine (Flickwerk nach Reparatur)
- Knoten an tragenden Stellen (Klampe, Poller)

**Risikobewertung:** MITTEL — Knoteneffizienz ist bekannt, aber die Bruchlastreduktion summiert sich mit anderen Faktoren (UV, Schamfil).

**AYDI-Bewertung:**
- Confidence: `visual_high` (Knoten vs. Spleiß gut erkennbar)
- Score-Abzug: −10 bis −20 Punkte
- Empfehlung: "Festmacher mit vorgefertigtem Spleißauge verwenden. Bruchlast bei Knotenverbindung um 30–45 % reduziert."

### 7.5 Fehlerbild F-FM-005: Fender zu klein

**Beschreibung:** Fender sind für die Bootsgröße unterdimensioniert. Unzureichende Energieabsorption und unzureichender Abstand zum Steg.

**Visuelle Indikatoren:**
- Fender wirken klein im Verhältnis zum Rumpf
- Boot berührt trotz Fender den Steg (Fender komplett eingedrückt)
- Fender versinken unter der Wasserlinie (zu wenig Auftrieb)
- Rumpf zeigt Kontaktspuren oberhalb oder unterhalb der Fender

**Risikobewertung:** HOCH — Rumpfschäden bei jedem Stegkontakt.

**AYDI-Bewertung:**
- Confidence: `visual_medium` (Fendergröße relativ zum Boot schätzbar, aber absoluter Durchmesser unsicher)
- Score-Abzug: −20 bis −40 Punkte
- Empfehlung: "Fender mindestens {empf_durchmesser} mm Durchmesser für {loa} m Yacht. Aktuell zu klein."

### 7.6 Fehlerbild F-FM-006: Fender falsch positioniert

**Beschreibung:** Fender hängen nicht auf der richtigen Höhe oder am richtigen Ort.

**Visuelle Indikatoren:**
- Fender hängen zu hoch (Rumpf unterhalb nicht geschützt)
- Fender hängen zu tief (unter Wasser oder am Wasserpass, nicht am Rumpfmaximum)
- Fender nur auf einer Seite
- Große Lücken zwischen Fendern (>3 m bei 12 m Boot)
- Fender hängen am Bug statt mittschiffs

**Risikobewertung:** MITTEL — Rumpfschaden an ungeschützten Stellen möglich.

**AYDI-Bewertung:**
- Confidence: `visual_high` (Position relativ zum Rumpf gut beurteilbar)
- Score-Abzug: −10 bis −25 Punkte
- Empfehlung: "Fender auf Höhe des maximalen Rumpfdurchmessers positionieren. Abstände gleichmäßig verteilen."

### 7.7 Fehlerbild F-FM-007: Fender beschädigt oder verformt

**Beschreibung:** Fender zeigen Beschädigungen, die ihre Funktion beeinträchtigen.

**Visuelle Indikatoren:**
- Permanente Verformung (Delle, Abflachung) → PVC-Material ermüdet
- Risse oder Löcher in der Fenderhaut
- Ventil undicht (Fender nicht prall aufgeblasen)
- Fender ist schlaff und hängt zusammengefallen
- Verfärbung durch UV (grau, gelblich, kreidig)

**Risikobewertung:** MITTEL — Reduzierte Energieabsorption, Schutzfunktion eingeschränkt.

**AYDI-Bewertung:**
- Confidence: `visual_high` (Verformung und Schäden gut erkennbar)
- Score-Abzug: −10 bis −20 Punkte
- Empfehlung: "Beschädigte Fender ersetzen. Schlaffe Fender aufblasen oder Ventil prüfen."

### 7.8 Fehlerbild F-FM-008: Fehlende Springleinen

**Beschreibung:** Yacht ist nur mit Vor- und Achterleinen festgemacht, Springleinen fehlen.

**Visuelle Indikatoren:**
- Nur 2–3 Leinen sichtbar (Vorleine, Achterleine, ggf. Brustleine)
- Keine Leinen, die diagonal (flach) entlang der Bordwand zum Steg laufen
- Boot bewegt sich bei Schwell/Wind deutlich vor und zurück

**Risikobewertung:** HOCH — Yacht ist nicht gegen Surge-Loading geschützt. Kann bei Böen oder Schwell gegen Steg oder Nachbarboot geschoben werden.

**AYDI-Bewertung:**
- Confidence: `visual_high` (fehlende Leinen offensichtlich)
- Score-Abzug: −25 bis −40 Punkte
- Empfehlung: "Springleinen sind unverzichtbar! Vor- und Achterspring anbringen. Mindestlänge 0,7 × LOA."

### 7.9 Fehlerbild F-FM-009: Festmacher an Klampe falsch belegt

**Beschreibung:** Festmacherleine ist nicht korrekt an der Klampe belegt (Kreuzschläge fehlen, nur 1 Windung, nicht gesichert).

**Visuelle Indikatoren:**
- Leine liegt nur lose um die Klampe
- Keine Kreuzschläge erkennbar
- Leine kann sich offensichtlich von der Klampe lösen
- Leine rutscht bereits teilweise von der Klampe

**Risikobewertung:** KRITISCH — Leine kann sich lösen, Yacht treibt ab.

**AYDI-Bewertung:**
- Confidence: `visual_high` (Klampenbelegung gut erkennbar)
- Score-Abzug: −30 bis −50 Punkte
- Empfehlung: "Korrekte Klampenbelegung: 1 Rundtörn + mindestens 3 Kreuzschläge + 1 Kopfschlag."

### 7.10 Fehlerbild F-FM-010: Kein Fenderbrett bei Pfahl-Liegeplatz

**Beschreibung:** An einem Pfahl-Liegeplatz fehlt das Fenderbrett. Zylindrische Fender können zwischen den Pfählen hindurchrutschen.

**Visuelle Indikatoren:**
- Pfähle sichtbar, Boot liegt zwischen Pfählen
- Nur zylindrische Fender, kein horizontales Brett
- Rumpf zeigt Kontaktspuren an Pfahl-Kontaktstellen
- Fender eingeklemmt zwischen Rumpf und Pfahl (eingedrückt)

**Risikobewertung:** MITTEL bis HOCH — Rumpfschaden an Pfahlkontaktstellen.

**AYDI-Bewertung:**
- Confidence: `visual_high` (Pfähle und fehlende Bretter gut erkennbar)
- Score-Abzug: −15 bis −25 Punkte
- Empfehlung: "Fenderbrett verwenden! Mindestens {brettlänge} mm für {loa} m Yacht."

### 7.11 Fehlerbild F-FM-011: Zu wenige Fender

**Beschreibung:** Die Anzahl der Fender ist für die Bootslänge unzureichend.

**Visuelle Indikatoren:**
- Große ungeschützte Rumpfabschnitte sichtbar (>3 m ohne Fender)
- Nur 2–3 Fender an einem 10–12 m Boot
- Fender nur im mittleren Bereich, Bug und Heck ungeschützt

**Risikobewertung:** MITTEL — Rumpfschaden an ungeschützten Stellen.

**AYDI-Bewertung:**
- Confidence: `visual_high` (Anzahl der Fender zählbar)
- Score-Abzug: −10 bis −20 Punkte
- Empfehlung: "Mindestens {min_anzahl} Fender für {loa} m Yacht. Aktuell nur {ist_anzahl} sichtbar."

### 7.12 Fehlerbild F-FM-012: Klampen unterdimensioniert oder beschädigt

**Beschreibung:** Klampen sind zu klein für die Bootsgröße oder zeigen mechanische Schäden.

**Visuelle Indikatoren:**
- Klampe wirkt klein im Verhältnis zum Leinendurchmesser
- Leine passt kaum auf die Klampe (zu dick für die Klampenhörner)
- Klampe ist verbogen, korrodiert oder gerissen
- Befestigungsschrauben der Klampe zeigen Risse im Deck um die Schraubenlöcher
- Klampe hat sich unter Last gelöst (Schrauben herausgezogen)

**Risikobewertung:** KRITISCH — Klampenversagen führt zum Verlust der Festmacherleine.

**AYDI-Bewertung:**
- Confidence: `visual_medium` (Klampengröße schwer zu messen, Schäden erkennbar)
- Score-Abzug: −20 bis −40 Punkte
- Empfehlung: "Klampen für LOA {loa} m sollten min. {klampen_länge} mm lang sein. Befestigung mit verstärkender Unterlegplatte."

---

## 8. Troubleshooting

### 8.1 Entscheidungsbaum T1: Festmacherleine gerissen

```
Festmacherleine gerissen
├── Bruch an Schamfilstelle?
│   ├── JA → Schamfilschutz war unzureichend
│   │   ├── Kontaktstelle identifizieren (Klüse, Reling, Stegkante)
│   │   ├── Schamfilschutz-Schlauch oder Leder anbringen
│   │   ├── Ggf. Klüsenrollen installieren
│   │   └── Leine ersetzen (Restleine unbrauchbar)
│   └── NEIN → Bruch im freien Lauf?
│       ├── UV-Degradation? (Leine alt, ausgeblichen, spröde)
│       │   ├── JA → Alle Leinen gleichen Alters prüfen und ggf. ersetzen
│       │   └── NEIN → Leine unterdimensioniert?
│       │       ├── JA → Durchmesser nach Tabelle 6.1 auswählen
│       │       └── NEIN → Surge-Belastung zu hoch?
│       │           ├── Liegeplatz exponiert? → Schwerwetter-Dimensionierung
│       │           ├── Springs vorhanden? → Wenn nein: nachrüsten!
│       │           └── Snubber/Ruckdämpfer einsetzen
```

### 8.2 Entscheidungsbaum T2: Fender versagt (Boot berührt Steg)

```
Boot hat Steg berührt trotz Fender
├── Fender zu klein?
│   ├── JA → Fendergröße nach Tabelle 6.3 erhöhen
│   └── NEIN → Fender falsch positioniert?
│       ├── JA → Höhe und Position korrigieren (→ 6.4)
│       └── NEIN → Fender verrutscht?
│           ├── Fenderleine zu lang? → Kürzen oder nachstellen
│           ├── Fender von Stegkante heruntergedrückt? → Fenderbrett verwenden
│           └── Fender zwischen Steg und Rumpf eingeklemmt und unter Wasser? → Fenderleine von oben/unten fixieren
├── Zu wenige Fender?
│   ├── JA → Anzahl nach Tabelle 3.3 erhöhen
│   └── NEIN → Spezialsituation?
│       ├── Pfahl-Liegeplatz? → Fenderbrett zwingend
│       ├── Unebene Stegkante? → Fenderbrett
│       └── Starker Schwell? → Doppelte Fender-Lage oder pneumatische Fender
```

### 8.3 Entscheidungsbaum T3: Yacht treibt trotz Festmachern ab

```
Yacht treibt vom Steg / schert aus
├── Leinen gerissen?
│   ├── JA → Siehe T1
│   └── NEIN → Leinen von Klampe gelöst?
│       ├── JA → Belegung prüfen (→ F-FM-009)
│       │   ├── Kreuzschläge fehlend → Korrekt belegen
│       │   ├── Klampe zu klein für Leine → Größere Klampe oder dünnere Leine
│       │   └── Kopfschlag fehlend → Immer mit Kopfschlag sichern
│       └── NEIN → Klampe herausgerissen?
│           ├── Deck unter Klampe verstärkt? → Wenn nein: verstärken
│           ├── Klampe mit Durchbolzung + Unterlegplatte? → Wenn nein: nachrüsten
│           └── Klampe zu klein? → Dimensionierung prüfen
├── Nur Vorwärts-/Rückwärtsbewegung?
│   ├── Springs fehlen → Nachrüsten (→ 2.3.3, 2.3.4)
│   └── Springs zu kurz → Verlängern (mind. 0,7 × LOA)
└── Yacht schert seitlich aus?
    ├── Brustleinen fehlen oder zu lang → Nachstellen
    └── Windlast zu hoch? → Zusätzliche Leinen ausbringen
```

### 8.4 Entscheidungsbaum T4: Fenderleinen verhaken sich / Fender verloren

```
Fender-Problem
├── Fender verloren (ins Wasser gefallen)
│   ├── Fenderleine zu lang → Kürzen
│   ├── Fenderleine nicht korrekt befestigt → Webeleinstek prüfen
│   ├── Fenderhaken defekt → Ersetzen
│   └── Fender bei Fahrt nicht eingeholt → SOP einführen: Fender vor Ablegen einholen!
├── Fenderleine im Propeller / am Ruder
│   ├── Fender bei Fahrt nicht eingeholt (häufigste Ursache!)
│   │   → Fender IMMER vor Ablegen einholen oder sicher nach oben binden
│   ├── Zu lange Fenderleine → Kürzen auf Freibord + 50 cm
│   └── Fender an Bug/Heck statt mittschiffs → Umhängen, weg von Propellerbereich
└── Fender drückt sich unter Wasser
    ├── Fenderleine an Stegkante zu straff → Lose geben
    ├── Fender zwischen Boot und Steg eingeklemmt → Umpositionieren
    └── Fenderbrett verwenden → Verhindert Eintauchen
```

### 8.5 Entscheidungsbaum T5: Klampe beschädigt / lose

```
Klampe beschädigt oder lose
├── Klampe hat sich gelöst (Schrauben herausgezogen)
│   ├── Deck laminatverstärkt? → Wenn nein: Sandwich-Kern komprimiert
│   │   ├── Kern aushöhlen, mit Epoxy/Glasfaser füllen
│   │   └── Überplatte von unten (min. 10 × Schraubendurchmesser)
│   ├── Durchbolzung statt Holzschrauben verwenden
│   └── Größere Unterlegplatte verwenden (Lastverteilung)
├── Klampe korrodiert (Edelstahl 316L prüfen!)
│   ├── Material 304? → Durch 316L ersetzen
│   ├── Spaltkorrosion an Befestigung? → Reinigen, neu montieren mit Dichtmasse
│   └── Galvanische Korrosion? → Isolierung zwischen Klampe und Deck prüfen
├── Klampe verbogen
│   ├── Unterdimensioniert → Größere Klampe installieren
│   │   └── Klampenlänge ≈ 2 × Leinendurchmesser (Faustformel)
│   ├── Materialermüdung → Klampe ersetzen (NICHT richten!)
│   └── Einmalige Überlastung → Klampe ersetzen, Festmacher-Dimensionierung prüfen
```

---

## 9. FAQ — Häufige Fragen

### FAQ 01: Wie viele Festmacherleinen brauche ich?

**Antwort:** Mindestens 6 Leinen als Grundausstattung: 1 Vorleine, 1 Achterleine, 1 Vorspring, 1 Achterspring, 1 Brustleine, 1 Reserveleine. Für Boote ab 12 m empfehlen wir 8 Leinen (doppelte Vor- und Achterleinen). Für Blauwassersegler: 10 Leinen. **Confidence:** documented.

### FAQ 02: Nylon oder Polyester für Festmacher?

**Antwort:** Für Festmacher ist **Nylon** die erste Wahl wegen der überlegenen Stoßdämpfung (15–20 % Dehnung). Polyester (8–12 % Dehnung) ist besser für Muringleinen und Dauerlieger, wo geringe Dehnung gewünscht ist. Im Zweifelsfall: Nylon nehmen. **Confidence:** documented.

### FAQ 03: Wie oft muss ich Festmacherleinen austauschen?

**Antwort:** Faustregel: alle 3–5 Jahre bei normaler Nutzung (80–120 Nächte/Saison). Bei intensiver Nutzung (Dauerlieger, Gezeitenrevier, exponierter Liegeplatz): alle 2–3 Jahre. Bei sichtbaren Schamfilschäden oder UV-Degradation: sofort. Leinen, die einmal maximal belastet wurden (Sturm), sollten ausgetauscht werden, auch wenn sie äußerlich intakt aussehen. **Confidence:** documented.

### FAQ 04: Was ist besser: dreikarätiges Tauwerk oder Doppelgeflecht?

**Antwort:** Dreikarätiges Tauwerk bietet mehr Dehnung (besser für Stoßdämpfung), ist günstiger und leichter zu spleißen. Doppelgeflecht kinkt nicht (liegt ruhiger auf der Klampe), hat eine höhere Bruchlast pro Durchmesser und fühlt sich besser in der Hand an. Für die meisten Yachten ist dreikarätiges Nylon-Tauwerk die optimale Wahl. Doppelgeflecht für Eigner, die Wert auf Handling und Ästhetik legen. **Confidence:** documented.

### FAQ 05: Warum sind Springleinen so wichtig?

**Antwort:** Springleinen sind die wichtigsten Festmacherleinen! Sie laufen fast parallel zur Bootslängsachse und fangen die Surge-Kräfte (Ruckbelastung durch Böen und Schwell) auf. Ohne Springs rutscht das Boot bei jeder Böe nach vorn oder achtern und belastet Vor- und Achterleine mit dem vollen Ruckstoß. **Confidence:** documented.

### FAQ 06: Welchen Durchmesser brauchen meine Festmacher?

**Antwort:** Faustformel für Nylon: Durchmesser in mm = Bootslänge in m + 4 (Standard) oder + 6 (Schwerwetter). Beispiel: 12 m Boot → 16 mm Standard, 18 mm Schwerwetter. Genaue Werte: siehe Tabelle 6.1. **Confidence:** documented.

### FAQ 07: Wie viele Fender brauche ich mindestens?

**Antwort:** Faustregel: LOA / 2, aufgerundet, mindestens 4. Also: 8 m Boot = 4 Fender, 10 m = 5, 12 m = 6, 14 m = 7, 16 m = 8. Zusätzlich 1–2 Kugelfender für Bug/Heck und idealerweise 1 Fenderbrett. **Confidence:** documented.

### FAQ 08: Polyform oder günstigere Marke?

**Antwort:** Polyform ist der Industriestandard mit nachweislich hoher UV-Beständigkeit und Langlebigkeit. Günstigere Marken (z.B. Majoni) bieten ein gutes Preis-Leistungs-Verhältnis für den Normalgebrauch. Für Dauerlieger und UV-intensive Reviere (Mittelmeer) lohnt sich Polyform. Für saisonale Nutzung in Nordeuropa sind Alternativen vertretbar. **Confidence:** estimated.

### FAQ 09: Muss ich ein Fenderbrett haben?

**Antwort:** An Pfahl-Liegeplätzen: JA, zwingend. An Schwimmstegen: empfohlen, aber nicht zwingend. In Schleusen: sehr empfohlen. Fenderbretter verhindern, dass zylindrische Fender zwischen Pfählen oder über Stegkanten rutschen. Ein Fenderbrett kostet 30–100 EUR und kann 5.000 EUR Rumpfreparatur verhindern. **Confidence:** documented.

### FAQ 10: HMPE (Dyneema) als Festmacher — sinnvoll?

**Antwort:** Grundsätzlich NEIN für Standard-Festmacher. HMPE hat nur 1–3 % Dehnung und bietet keine Stoßdämpfung. Die Ruckkräfte auf Klampen und Deck sind 3–5× höher als bei Nylon. HMPE ist nur sinnvoll als permanente Muringleine (mit vorgeschaltetem Nylon-Snubber) oder als Schleppleine. **Confidence:** documented.

### FAQ 11: Wie lange sollte eine Vorleine sein?

**Antwort:** Mindestens 1 × LOA, empfohlen 1,5 × LOA. In Gezeitenrevieren zusätzlich den Tidenhub × 1,5 addieren. Beispiel: 12 m Boot, 3 m Tidenhub → 12 × 1,5 + 3 × 1,5 = 18 + 4,5 = 22,5 m → 24 m. Immer besser zu lang als zu kurz — eine zu kurze Leine in einem Gezeitenhafen kann die Yacht bei Niedrigwasser unter den Steg drücken. **Confidence:** documented.

### FAQ 12: Soll ich Kauschen in die Augen einsetzen?

**Antwort:** Kauschen (aus Edelstahl oder UHMWPE) schützen das Auge vor Abrieb und verlängern die Lebensdauer erheblich. Empfohlen für: alle Leinen, die über Bolzen, Poller oder Ringe gelegt werden. Nicht nötig für: Leinen, die direkt auf eine Klampe belegt werden (dort ist das Auge ohnehin nicht im Einsatz). **Confidence:** documented.

### FAQ 13: Fender — aufblasen oder Festschaum?

**Antwort:** Aufblasbare Fender (Standard) sind leichter und kompakter zu verstauen. Festschaum-Fender sind unempfindlicher (kein Ventilproblem), aber schwerer und sperriger. Für 95 % aller Yachten sind aufblasbare Fender die richtige Wahl. Festschaum-Fender für Arbeitsboote und extrem rauen Einsatz. **Confidence:** documented.

### FAQ 14: Wie befestige ich einen Fender richtig?

**Antwort:** Fenderleine am Fender: Webeleinstek (verstellbar!). Fenderleine am Boot: Webeleinstek an der Reling oder auf einer Klampe. Niemals Palstek am Fender — er lässt sich nicht verstellen. Fenderleine so lang, dass der Fender auf Höhe des maximalen Rumpfdurchmessers (Wasserpass) hängt. Bei Tide: Leine lang genug für den gesamten Tidenhub. **Confidence:** documented.

### FAQ 15: Meine Leinen sind steif — was tun?

**Antwort:** Ursachen: (a) Salzkristalle in den Fasern → mit Süßwasser spülen und 24 h einweichen, (b) UV-Alterung → Leine austauschen, (c) neue Leine aus Polyester → wird mit Gebrauch geschmeidiger, (d) Frost (Nylon bei Kälte steif) → auftauen lassen. Regelmäßiges Spülen mit Süßwasser hält Leinen geschmeidig. **Confidence:** documented.

### FAQ 16: Kann ich beschädigte Festmacher reparieren?

**Antwort:** Grundsätzlich NEIN für sicherheitsrelevante Festmacher. Eine Leine mit Schamfilschaden oder Riss hat an der Schadstelle nur noch 30–60 % der ursprünglichen Bruchlast. "Reparaturen" durch Knoten verschlechtern die Situation weiter. Nur akzeptabel: Kürzen und neues Auge spleißen, wenn der Schaden am Ende liegt und die Leine dann noch lang genug ist. **Confidence:** documented.

### FAQ 17: Welche Fenderfarbe ist am besten?

**Antwort:** Weiß: Standard, sauber, zeigt Schmutz schnell → gut für Kontrolle. Blau: Klassisch, Pantone-farbecht. Schwarz: Unauffällig, aber kann bei Hitze Rumpf markieren (Abfärben!). Grau: Modern, unauffällig. Empfehlung: Weiß oder Blau. Schwarze Fender nur verwenden, wenn der Rumpf dunkel ist. **Confidence:** estimated.

### FAQ 18: Wie lagere ich Leinen und Fender im Winter?

**Antwort:** Leinen: mit Süßwasser spülen, vollständig trocknen, locker aufschießen, trocken und dunkel lagern (keine UV-Exposition). Fender: mit Süßwasser abspülen, Druck leicht reduzieren (nicht vollständig ablassen), trocken und dunkel lagern. Niemals nasse Leinen einlagern → Schimmel! **Confidence:** documented.

### FAQ 19: Brauche ich für das Mittelmeer andere Festmacher als für die Ostsee?

**Antwort:** Grundsätzlich gleiche Leinen, aber: (a) Mittelmeer hat mehr UV → kürzere Lebensdauer, dunklere Leinen oder Polyester bevorzugen, (b) Mittelmeer hat kaum Tide → Leinen können kürzer sein, (c) Mittelmeer hat Heckanleger → zusätzliche Muringleine/Anker nötig, (d) Ostsee hat Gezeiten (Nordsee!) und Starkwind → robustere Dimensionierung, längere Leinen. **Confidence:** documented.

### FAQ 20: Was kostet eine komplette Festmacher-/Fenderausstattung?

**Antwort:** Richtwerte: 8 m Boot: 370–550 EUR, 10 m: 520–800 EUR, 12 m: 770–1.150 EUR, 15 m: 1.100–1.700 EUR, 20 m: 2.050–3.300 EUR. Darin enthalten: 6–8 Festmacherleinen, 6–8 Fender, 1 Fenderbrett, Zubehör. Premiumausrüstung (Polyform, Liros Moorex) liegt am oberen Ende, Budgetausrüstung (Majoni, Robline Dockline) am unteren. **Confidence:** estimated.

### FAQ 21: Woran erkenne ich eine gute Klampe?

**Antwort:** Gute Klampen: (a) Material 316L Edelstahl (nicht 304!), (b) Durchbolzung mit Unterlegplatte (nicht nur Holzschrauben), (c) Klampenlänge mindestens 2× Leinendurchmesser, (d) Hörner glatt (keine scharfen Kanten → Schamfil!), (e) Deck unter Klampe verstärkt (bei Sandwich-Deck: Kern ausgefüllt). **Confidence:** documented.

### FAQ 22: Soll ich farbige Leinen verwenden?

**Antwort:** Farbige Leinen (blau, rot, grün) haben einen praktischen Vorteil: Sie erleichtern die Zuordnung (z.B. blaue Vorleine, rote Achterleine, grüne Springs). Nachteil: Farbstoffe können die UV-Beständigkeit verringern (ausgenommen: dunkle Farben wie Schwarz oder Navy, die UV sogar besser absorbieren). Empfehlung: Für den Normalgebrauch ist Farbe Geschmackssache. Für Blauwasser: weiße oder schwarze Leinen. **Confidence:** estimated.

### FAQ 23: Wie berechne ich die richtige Fendergröße?

**Antwort:** Faustformel: Fender-Durchmesser in mm = LOA in m × 15 + 30. Beispiel: 12 m Boot → 12 × 15 + 30 = 210 mm. Alternativ: Fender-Durchmesser = Freibord × 0,25 (Minimum). Der Fender muss den Rumpf bei vollem Kontakt noch vom Steg fernhalten → wenn der Fender komplett eingedrückt wird, ist er zu klein. **Confidence:** documented.

### FAQ 24: Brauche ich Sonderfestmacher für Sturmvorbereitung?

**Antwort:** Ja! Sturmvorbereitung erfordert: (a) Alle 6–8 Leinen ausbringen, (b) zusätzliche Reserveleinen als Verdoppelung, (c) Leinen 1–2 Stufen dicker als normal (z.B. 20 mm statt 16 mm), (d) Schamfilschutz an ALLEN Kontaktstellen, (e) Leinen regelmäßig kontrollieren (alle 4–6 Stunden), (f) Fender verdoppeln und maximale Größe verwenden, (g) Brustleinen lockern (erlaubt Pendelbewegung). **Confidence:** documented.

### FAQ 25: Was ist der Unterschied zwischen Klüse und Klampe?

**Antwort:** Eine **Klampe** ist der Beschlag, auf dem die Leine belegt (befestigt) wird — typisch T-förmig mit zwei Hörnern. Eine **Klüse** ist die Öffnung im Schandeckel oder der Reling, durch die die Leine vom Deck zum Steg geführt wird. Die Klüse schützt die Leine vor Abrieb am Schandeckel — idealerweise mit Rollen oder abgerundeten Kanten versehen. **Confidence:** documented.

---

## 10. Glossar

### A

**Achterleine (Stern Line):** Festmacherleine vom Heck der Yacht schräg nach achtern zum Steg. Verhindert Vorwärtsbewegung.

**Achterspring (Aft Spring Line):** Festmacherleine vom Heck der Yacht schräg nach vorn zum Steg. Verhindert Rückwärtsbewegung und dämpft Surge-Belastung.

**Auge (Eye / Loop):** Schlaufe am Ende einer Festmacherleine, hergestellt durch Spleißen oder Knoten. Wird über Klampe, Poller oder Bolzen gelegt.

### B

**Belegen (To Make Fast / To Cleat):** Festmacherleine auf einer Klampe sichern. Korrekte Belegung: 1 Rundtörn + mindestens 3 Kreuzschläge + 1 Kopfschlag.

**Bruchlast (Breaking Load / Breaking Strength):** Maximale Kraft, bei der eine Leine reißt. Angegeben in kN oder kg. Die Arbeitslast (Safe Working Load, SWL) beträgt typisch 1/5 bis 1/3 der Bruchlast.

**Brustleine (Breast Line):** Festmacherleine, die querab (90° zur Bootslängsachse) vom Boot zum Steg führt. Hält das Boot nah am Steg.

### C

**Chafe Guard:** Schutzmanschette aus textilem Material (oft Kevlar-Gewebe), die über eine Leine an Schamfilstellen gezogen oder per Klett befestigt wird.

### D

**Dehnung (Stretch / Elongation):** Verlängerung einer Leine unter Belastung, angegeben in Prozent der Originallänge. Wichtigste Eigenschaft für Stoßdämpfung.

**Doppelgeflecht (Double Braid):** Leinenkonstruktion mit geflochtenem Kern und geflochtenem Mantel. Kombiniert hohe Festigkeit mit gutem Handling.

**Dreikarätiges Tauwerk (Three-Strand Twisted Rope):** Klassische Leinenkonstruktion aus drei gegenläufig verdrehten Strängen. Standard für Festmacher.

### E

**Energieabsorption (Energy Absorption):** Fähigkeit eines Fenders, kinetische Energie aufzunehmen und in Verformungsarbeit umzuwandeln, ohne den Rumpf zu beschädigen. Angegeben in Joule (J) oder kNm.

### F

**Fender (Fender):** Schutzvorrichtung zwischen Rumpf und Steg/Pfahl/Nachbarboot. Absorbiert Stoßenergie und verhindert Rumpfschäden.

**Fenderbrett (Fender Board):** Horizontales Brett vor zwei oder mehr Fendern. Verteilt die Last und überbrückt Stegpfosten und Kanten.

**Fenderleine (Fender Line / Fender Lanyard):** Leine, mit der der Fender am Boot (Reling, Klampe) befestigt wird.

**Festmacher (Mooring Line / Dock Line):** Leine zum Befestigen einer Yacht an einem Steg, Poller, Pfahl oder Ring.

### G

**Geflechtkonstruktion (Braid Construction):** Leine, bei der die Fasern verflochten statt verdreht werden. Varianten: 8-fach, 12-fach, 16-fach, Doppelgeflecht.

### H

**HMPE (High Modulus Polyethylene):** Hochfeste Faser (Dyneema, Spectra) mit extrem hoher Bruchlast und minimaler Dehnung. Für Festmacher nur mit Snubber geeignet.

### K

**Kausche (Thimble):** Metalleinsatz (Edelstahl) oder Kunststoffeinsatz in einem Leinenauge. Schützt das Auge vor Abrieb durch Bolzen, Schäkel oder Ringe.

**Klampe (Cleat):** Decksbeschlag zum Belegen von Festmacherleinen. T-förmig mit zwei Hörnern.

**Klüse (Fairlead / Chock):** Öffnung im Schandeckel oder der Reling, durch die eine Festmacherleine vom Deck nach außen zum Steg geführt wird.

**Knoteneffizienz (Knot Efficiency):** Prozentualer Anteil der Bruchlast, der nach dem Knoten verbleibt. Spleißauge: 90–95 %, Palstek: 60–65 %.

**Kopfschlag (Locking Turn):** Abschließende Windung bei der Klampenbelegung, bei der die Leine unter sich selbst durchgeführt wird. Sichert die Belegung gegen Lösen.

**Kreuzschlag (Crossing Turn):** Überkreuz-Windung bei der Klampenbelegung. Erzeugt Reibung und Haltekraft.

### L

**Langfender (Bow/Stern Fender):** Verlängerter zylindrischer Fender mit spitz zulaufenden Enden für Bug- und Heckschutz.

### M

**Muringleine (Mooring Line / Lazy Line):** Leine, die vom Boot zu einem Grundkörper (Muringblock, Muringtonne) führt. Hält das Boot auf Abstand bei Heckanleger.

### N

**Nylon (Polyamid):** Synthetische Faser mit hoher Elastizität und Bruchlast. Standardmaterial für Festmacherleinen.

### O

**Octoplait (Achtfachgeflecht / Multiplait):** Achtsträngige geflochtene Leinenkonstruktion. Guter Kompromiss zwischen dreikarätiger Verdrehung und Doppelgeflecht.

### P

**Päckchen (Raft / Rafting):** Zwei oder mehr Boote, die nebeneinander am Steg oder auf Reede liegen. Erfordert verstärkte Festmacher und zusätzliche Fender.

**Pneumatischer Fender (Pneumatic Fender):** Druckluft-gefüllter Fender mit Gummihülle für extrem hohe Energieabsorption. Für Großyachten und Berufsschifffahrt.

**Poller (Bollard):** Pfosten auf dem Steg oder an der Pier, an dem Festmacherleinen befestigt werden.

**Polyester (PES / PET):** Synthetische Faser mit hoher UV-Beständigkeit und Abriebfestigkeit. Geringere Elastizität als Nylon.

**Polyform:** Norwegischer Marktführer für Yacht-Fender. Markenname ist quasi zum Gattungsbegriff geworden.

### R

**Ruckdämpfer (Snubber / Shock Absorber):** Elastisches Element (Gummizug, Nylon-Strop) in einer Festmacherleine zur Absorption von Stoßbelastungen.

**Rundtörn (Round Turn):** Vollständige Umschlingung einer Klampe, eines Pollers oder eines Ringes. Basis der korrekten Klampenbelegung.

### S

**Safe Working Load (SWL):** Sichere Arbeitslast einer Leine. Typisch 1/5 bis 1/3 der Bruchlast.

**Schamfilen (Chafing):** Reibungsverschleiß einer Leine an einer Kante, Klüse oder einem Beschlag. Häufigster Grund für Leinenversagen.

**Schamfilschutz (Chafe Protection):** Schutzmaterial (PVC-Schlauch, Leder, Kevlar) an Kontaktstellen zur Vermeidung von Schamfilschäden.

**Schwell (Swell):** Langperiodische Wellenbewegung im Hafen, die Yachten auf und ab bewegt und dynamische Belastung auf Festmacher erzeugt.

**Spleißen (Splicing):** Verbindungstechnik, bei der die Stränge einer Leine ineinander verflochten werden. Höchste Festigkeit aller Verbindungsarten (90–95 % der Bruchlast).

**Spring (Spring Line):** Festmacherleine, die in Bootslängsrichtung (diagonal nach vorn oder achtern) zum Steg führt. Fängt Surge-Kräfte ab.

**Stufenfender (Step Fender / Pontoon Fender):** Am Steg oder Ponton fest installierter Fender mit C- oder L-Profil.

**Surge Loading (Ruckbelastung):** Dynamische Stoßbelastung auf Festmacherleinen durch Böen, Schwell oder Strömung. Kann das 3–6-fache der statischen Windlast betragen.

### T

**Tidenhub (Tidal Range):** Differenz zwischen Hoch- und Niedrigwasser. Bestimmt die erforderliche Festmacherlänge in Gezeitenrevieren.

### V

**Vorleine (Bow Line / Head Line):** Festmacherleine vom Bug der Yacht schräg nach vorn zum Steg. Verhindert Rückwärtsbewegung.

**Vorspring (Forward Spring Line):** Festmacherleine vom Bug der Yacht schräg nach achtern zum Steg. Verhindert Vorwärtsbewegung und dämpft Surge.

### W

**Webeleinstek (Clove Hitch):** Knoten zum Befestigen einer Fenderleine am Fender. Vorteil: verstellbar, ohne die Leine lösen zu müssen.

**Windangriffsfläche (Windage Area):** Projizierte Fläche der Yacht (Rumpf + Aufbauten + Rigg) querab oder längs. Bestimmt die Windlast.

### Z

**Zylindrischer Fender (Cylindrical Fender):** Standard-Fenderform mit zylindrischem Körper und Aufhängungsösen an beiden Enden.

---

## 11. Schnell-Referenz

### 11.1 Checkliste: Festmachen am Steg

```
□ Fender positionieren (Höhe, Abstand, Anzahl prüfen)
□ Vorleine ausbringen und belegen
□ Achterleine ausbringen und belegen
□ Vorspring belegen (flach, lang!)
□ Achterspring belegen (flach, lang!)
□ Brustleine(n) bei Bedarf
□ Alle Leinen auf korrekte Belegung prüfen (Kreuzschläge + Kopfschlag)
□ Schamfilschutz an Kontaktstellen anbringen
□ Fender-Höhe kontrollieren (Wasserpass-Höhe)
□ Tide berücksichtigen — genug Lose in allen Leinen?
□ Bei Starkwind: Leinen verdoppeln, Reserveleinen vorbereiten
```

### 11.2 Dimensionierungs-Schnellreferenz (Nylon-Festmacher)

```
 LOA    Leinen-Ø    Fender-Ø    Fender Anzahl
 8 m    14 mm       180 mm      4
10 m    16 mm       200 mm      6
12 m    18 mm       220 mm      6
14 m    20 mm       250 mm      6
16 m    22 mm       290 mm      8
18 m    24 mm       340 mm      8
20 m    28 mm       375 mm      8
25 m    32 mm       400 mm      10
30 m    36 mm       450 mm      12
```

### 11.3 Klampen-Belegung — Schritt für Schritt

```
1. Leine unter dem hinteren Horn durchführen
2. 1 Rundtörn um die Klampe (unter beiden Hörnern durch)
3. Kreuzschlag 1: Leine über die Klampe diagonal zum gegenüberliegenden Horn
4. Kreuzschlag 2: Leine zurück, diagonal zum anderen Horn
5. Kreuzschlag 3: Nochmals diagonal
6. Kopfschlag: Leine unter sich selbst durchführen (sichert gegen Lösen)
7. Lose aufschießen und sichern
```

### 11.4 Sturm-Checkliste

```
□ Alle verfügbaren Leinen ausbringen (mindestens 6, besser 8)
□ Leinen verdoppeln (2. Leine parallel zur 1.)
□ Schwerwetter-Durchmesser verwenden (+2 mm)
□ Springs extra lang (mind. 1 × LOA)
□ Schamfilschutz an ALLEN Kontaktstellen
□ Brustleinen LOCKER lassen (Pendelbewegung erlauben)
□ Fender auf maximale Größe wechseln
□ Fender verdoppeln
□ Fenderbretter einsetzen
□ Leinen alle 4–6 Stunden kontrollieren
□ Reserveleinen bereithalten
□ Landstrom abschalten, Luken schließen
```

---

## ANHANG A — Fallstudien

### A1 — Sturmschaden an Bavaria 40 in Kroatien (Bora-Sturm, 2023)

**Ausgangslage:**
- Boot: Bavaria 40 Cruiser, LOA 12,35 m, Verdrängung 9.500 kg
- Liegeplatz: Heckanleger an Betonmole, Marina Punat (Krk)
- Festmacher: 2 × 14 mm Nylon-Doppelgeflecht (Heckleinen), 1 × Muringleine (vom Hafen gestellt, unbekanntes Material/Alter)
- Fender: 4 × Polyform F-2 (200 mm × 660 mm)
- Wetter: Bora 8–9 Bft mit Böen bis 10 Bft (70+ kn)

**Schadensverlauf:**
1. Bora setzte abends ein, Windstärke stieg von 5 auf 8 Bft innerhalb von 2 Stunden
2. Muringleine (Bug) riss nach ca. 4 Stunden bei Windstärke 9
3. Boot drehte quer und schlug mit der Backbordseite gegen die Mole
4. Fender F-2 waren zu klein für die Aufprallenergie — Boot berührte Mole direkt
5. 2 Fender wurden unter den Steg gedrückt
6. Steuerbord-Heckleine riss an der Klüse (Schamfil, kein Schutz)

**Schadensumme:**
- Rumpfreparatur (GFK + Gelcoat, 3 m²): 4.200 EUR
- Reling verbogen: 1.800 EUR
- 1 Stanchion gebrochen: 350 EUR
- 3 Festmacherleinen ersetzt: 180 EUR
- 2 Fender ersetzt: 100 EUR
- **Gesamt: 6.630 EUR**

**AYDI-Analyse (retrospektiv):**
- Festmacher unterdimensioniert: 14 mm statt empfohlene 18 mm für 12,35 m → Score −30
- Fender unterdimensioniert: 200 mm statt empfohlene 220–250 mm → Score −25
- Fehlender Schamfilschutz an Klüse → Score −20
- Muringleine nicht kontrolliert (vom Hafen gestellt) → Score −15
- Keine Springleinen → Score −25
- **Gesamtscore: 35/100 (KRITISCH)**
- Confidence: `documented` (Schadensbericht und Fotos vorliegend)

**Lehren:**
1. Muringleinen vom Hafen IMMER kontrollieren — im Zweifelsfall eigene Leine verwenden
2. Festmacher 1 Stufe überdimensionieren in Bora-/Meltemi-Gebieten
3. Fender F-3 oder F-4 statt F-2 für 12-m-Boot
4. Schamfilschutz an JEDER Klüse
5. Springs nachrüsten (hätten die Querbewegung gedämpft)

### A2 — Optimal gesichertes Boot im Orkan "Zeynep" (Nordsee, 2022)

**Ausgangslage:**
- Boot: Hallberg-Rassy 40 MK II, LOA 12,20 m, Verdrängung 9.800 kg
- Liegeplatz: Schwimmsteg, Marina Cuxhaven
- Festmacher: 8 × 18 mm Nylon dreikarätiges Tauwerk (Liros Handy Elastic), alle mit Spleißaugen
- Fender: 6 × Polyform F-4 (250 mm × 855 mm) + 2 × Polyform A-2 (Kugelfender) + 2 Fenderbretter
- Springs: 2 × 15 m, Vorspring + Achterspring
- Schamfilschutz: PVC-Schlauch an allen Klüsen + Kevlar-Chafe Guards an Stegkante

**Wetterbedingungen:**
- Orkan "Zeynep" (18.02.2022): Windstärke 10–12 Bft, Böen bis 120 kn (Cuxhaven)
- Tidenhub: 3,4 m (Springtide) + Sturmflut-Zuschlag 2,1 m = 5,5 m Gesamthub

**Ergebnis:**
- Boot überstand den Orkan OHNE Schaden
- Alle 8 Leinen hielten — die Nylon-Dehnung absorbierte die Stöße
- Fender F-4 groß genug, Fenderbretter verhinderten Verrutschen
- Kugelfender schützten Bug und Heck zuverlässig
- Leinen hatten genug Lose für den extremen Tidenhub

**AYDI-Analyse:**
- Festmacher: 18 mm, 1 Stufe über Empfehlung → Score +10 (Bonus)
- Fender: F-4 (250 mm), 1 Größe über Empfehlung → Score +10
- 8 Leinen inkl. Springs → Score +15
- Schamfilschutz komplett → Score +10
- Fenderbretter vorhanden → Score +5
- **Gesamtscore: 98/100 (EXZELLENT)**
- Confidence: `documented`

### A3 — Fenderschaden an Sunseeker 68 in Saint-Tropez (2024)

**Ausgangslage:**
- Boot: Sunseeker 68 Sport Yacht, LOA 20,73 m, Lackierter Rumpf (dunkelblau metallic)
- Liegeplatz: Heckanleger, Port de Saint-Tropez
- Fender: 6 × Standard-Zylinderfender 300 mm (Marke unbekannt), schwarz
- Problem: Schwarze Fender hinterließen bei 35 °C Außentemperatur permanente schwarze Abriebspuren auf dem dunkelblauen Lackrumpf

**Schadensumme:**
- Polishing und Rumpfreinigung (Spezialfirma): 2.800 EUR
- Teilweise Nachlackierung (3 Bereiche): 12.500 EUR
- **Gesamt: 15.300 EUR**

**AYDI-Analyse:**
- Fender-Material: Schwarze PVC-Fender auf lackiertem Rumpf sind INAKZEPTABEL → Score −40
- Empfehlung: Weiße oder graue Premium-Fender (Dan-Fender, Polyform) mit weicher, nicht-markierender Oberfläche
- Für Superyachten: Fendersocken (textile Schutzhüllen) zwingend
- Confidence: `documented`

### A4 — Päckchen-Unfall in Kiel (Kieler Woche, 2023)

**Ausgangslage:**
- 3 Boote im Päckchen: X-Yachts Xp 38 (11,86 m), Bavaria 38 (11,72 m), Jeanneau Sun Odyssey 389 (11,49 m)
- Nur Standardfender (keine zusätzlichen Fender zwischen den Booten)
- Keine Springs zwischen den Booten
- Wind: 6 Bft mit Böen 7

**Schadensverlauf:**
1. Mittleres Boot (Bavaria) begann bei Böen gegen äußeres Boot zu schlagen
2. Fender waren zu klein für die Doppelbelastung (2 Boote drücken gleichzeitig)
3. Fender wurden zwischen den Rümpfen nach oben gequetscht
4. Rumpfkontakt an 4 Stellen bei allen 3 Booten
5. Reling des mittleren Bootes verbogen

**Schadensumme (alle 3 Boote):**
- 3 × GFK-Reparatur: 7.500 EUR
- 1 × Reling-Reparatur: 1.200 EUR
- **Gesamt: 8.700 EUR**

**AYDI-Empfehlung für Päckchen:**
- Fender 1 Größe größer als für Einzelboot
- Mindestens 4 Fender zwischen jedem Boot-Paar
- Kugelfender an Bug und Heck
- Springs zwischen ALLEN Booten
- Fenderbretter bei unterschiedlichen Freibordhöhen

### A5 — Schleusenpassage Kiel-Holtenau (NOK, 2022)

**Ausgangslage:**
- Boot: Dehler 38 SQ, LOA 11,56 m
- Schleuse: Kiel-Holtenau (Nord-Ostsee-Kanal), Hubhöhe 2,5 m
- Festmacher: Standardleinen 14 mm, 10 m Länge
- Fender: 4 × F-3, kein Fenderbrett

**Problem:**
- Leinen zu kurz für Hubhöhe → Boot hing zeitweise schief
- Schleusenwand extrem rau (Beton) → massive Schamfilschäden an 2 Leinen
- Fender ohne Fenderbrett → rutschten an Schleusenwand-Vorsprüngen vorbei
- Gelcoat-Kratzer an 2 Stellen

**AYDI-Empfehlung für Schleusen:**
- Leinen: mindestens 2 × Hubhöhe + LOA = 2 × 2,5 + 11,56 = 16,56 m → 18 m
- Schamfilschutz ZWINGEND (Schleusenwände sind brutalster Schamfil-Verursacher)
- Fenderbrett ZWINGEND in Schleusen
- Maximale Fendergröße verwenden

### A6 — Blauwasseryacht Amel 50 — Optimal ausgerüstet (2024)

**Ausgangslage:**
- Boot: Amel 50, LOA 15,45 m, Verdrängung 16.500 kg
- Revier: Atlantik-Überquerung + Karibik
- Festmacher: 10 × 20 mm Nylon dreikarätiges Tauwerk (Gleistein Dock), alle vorgefertigt mit Spleißaugen und Kauschen
- Fender: 8 × Polyform F-5 (290 mm × 980 mm) + 4 × Polyform A-3 (Kugelfender) + 2 Fenderbretter
- Extra: Schamfilschutz-Set (12 Stk), 2 Reserveleinen 24 mm × 20 m

**AYDI-Bewertung:**
- Dimensionierung korrekt für 15 m + Schwerwetter → Score 95/100
- Überdurchschnittliche Ausstattung (10 Leinen, 12 Fender, 2 Fenderbretter) → Score +5 Bonus
- **Gesamtscore: 100/100 (EXZELLENT)**
- Confidence: `documented`

### A7 — Dauerlieger Baltic 39 in Flensburg (2021–2024)

**Ausgangslage:**
- Boot: Baltic 39, LOA 11,99 m, Dauerlieger seit 2018
- Festmacher: Originale Werft-Leinen, 14 mm Nylon, seit 2018 nicht getauscht
- Einsatz: 365 Tage/Jahr am Schwimmsteg

**Befund nach 6 Jahren:**
- Bruchlast-Test der Leinen (Labor): nur noch 45–55 % der Nennbruchlast
- UV-Degradation: Oberfläche kreidig, Fasern spröde
- Schamfilschäden an 3 von 6 Leinen (Klüsen-Kontaktstellen)
- Zyklische Ermüdung: geschätzt 100.000+ Belastungszyklen

**AYDI-Empfehlung:**
- Austausch ALLER Leinen SOFORT
- Für Dauerlieger: Austausch alle 2–3 Jahre ODER Polyester-Leinen (bessere UV-Beständigkeit)
- Regelmäßige Inspektion: halbjährlich
- Score: 25/100 (KRITISCH — akute Bruchgefahr)
- Confidence: `measured` (Labortest)

### A8 — Neuausstattung Beneteau Oceanis 46.1 (2024)

**Ausgangslage:**
- Boot: Beneteau Oceanis 46.1, LOA 14,60 m, Verdrängung 11.300 kg
- Revier: Mittelmeer (Griechenland, Kroatien)
- Budget: 1.500 EUR für Festmacher + Fender komplett

**AYDI-Empfehlung und umgesetzte Ausstattung:**

| Position | Produkt | Anzahl | Stückpreis | Gesamt |
|----------|---------|--------|------------|--------|
| Vorleine 20 mm × 14 m | Liros Handy Elastic, vorgefertigt | 2 | 78 EUR | 156 EUR |
| Achterleine 20 mm × 14 m | Liros Handy Elastic, vorgefertigt | 2 | 78 EUR | 156 EUR |
| Spring 20 mm × 16 m | Liros Handy Elastic, vorgefertigt | 2 | 88 EUR | 176 EUR |
| Brustleine 18 mm × 8 m | Liros Handy Elastic, vorgefertigt | 2 | 52 EUR | 104 EUR |
| Reserveleine 20 mm × 20 m | Liros Handy Elastic, Meterware | 1 | 95 EUR | 95 EUR |
| Fender F-4 (250 mm) | Polyform F-4, weiß | 6 | 82 EUR | 492 EUR |
| Kugelfender A-2 (390 mm) | Polyform A-2, weiß | 2 | 62 EUR | 124 EUR |
| Fenderbrett 1.000 mm | Kunststoff, mit Aufhängung | 1 | 65 EUR | 65 EUR |
| Schamfilschutz-Set | PVC-Schlauch + Chafe Guards | 1 | 45 EUR | 45 EUR |
| Fenderleinen 8 mm | Nylon, vorgefertigt, 10 Stk | 1 | 38 EUR | 38 EUR |
| **GESAMT** | | | | **1.451 EUR** |

- **AYDI-Score: 92/100 (SEHR GUT)**
- Confidence: `documented`

---

## ANHANG B — Bruchlast-Vergleichstabellen

### B1 — Bruchlast Nylon dreikarätiges Tauwerk nach Durchmesser

| Durchmesser (mm) | Bruchlast (kN) | Bruchlast (kg) | SWL 1:5 (kg) | Confidence |
|-------------------|---------------|----------------|-------------|------------|
| 8 | 7,5 | 765 | 153 | measured |
| 10 | 12,0 | 1.224 | 245 | measured |
| 12 | 17,5 | 1.785 | 357 | measured |
| 14 | 23,5 | 2.398 | 480 | measured |
| 16 | 31,0 | 3.163 | 633 | measured |
| 18 | 39,0 | 3.978 | 796 | measured |
| 20 | 48,0 | 4.896 | 979 | measured |
| 22 | 58,5 | 5.967 | 1.193 | measured |
| 24 | 69,0 | 7.038 | 1.408 | measured |
| 28 | 94,0 | 9.588 | 1.918 | measured |
| 32 | 122,0 | 12.444 | 2.489 | measured |
| 36 | 154,0 | 15.708 | 3.142 | measured |
| 40 | 190,0 | 19.380 | 3.876 | measured |

### B2 — Bruchlast Nylon Doppelgeflecht nach Durchmesser

| Durchmesser (mm) | Bruchlast (kN) | Bruchlast (kg) | SWL 1:5 (kg) | Confidence |
|-------------------|---------------|----------------|-------------|------------|
| 10 | 14,5 | 1.479 | 296 | measured |
| 12 | 21,0 | 2.142 | 428 | measured |
| 14 | 28,5 | 2.907 | 581 | measured |
| 16 | 37,5 | 3.825 | 765 | measured |
| 18 | 47,0 | 4.794 | 959 | measured |
| 20 | 58,0 | 5.916 | 1.183 | measured |
| 22 | 70,0 | 7.140 | 1.428 | measured |
| 24 | 83,5 | 8.517 | 1.703 | measured |

### B3 — Bruchlast Polyester Doppelgeflecht nach Durchmesser

| Durchmesser (mm) | Bruchlast (kN) | Bruchlast (kg) | SWL 1:5 (kg) | Confidence |
|-------------------|---------------|----------------|-------------|------------|
| 10 | 13,0 | 1.326 | 265 | measured |
| 12 | 19,0 | 1.938 | 388 | measured |
| 14 | 26,0 | 2.652 | 530 | measured |
| 16 | 34,0 | 3.468 | 694 | measured |
| 18 | 43,0 | 4.386 | 877 | measured |
| 20 | 53,0 | 5.406 | 1.081 | measured |

### B4 — Bruchlast HMPE (Dyneema) nach Durchmesser

| Durchmesser (mm) | Bruchlast (kN) | Bruchlast (kg) | SWL 1:5 (kg) | Confidence |
|-------------------|---------------|----------------|-------------|------------|
| 6 | 25,0 | 2.550 | 510 | measured |
| 8 | 44,0 | 4.488 | 898 | measured |
| 10 | 68,0 | 6.936 | 1.387 | measured |
| 12 | 98,0 | 9.996 | 1.999 | measured |
| 14 | 132,0 | 13.464 | 2.693 | measured |
| 16 | 170,0 | 17.340 | 3.468 | measured |
| 18 | 212,0 | 21.624 | 4.325 | measured |
| 20 | 258,0 | 26.316 | 5.263 | measured |

---

## ANHANG C — Confidence-Mapping

### C1 — Confidence-Level für Festmacher-/Fender-Analyse

| Datenpunkt | Pipeline A (Struktur) | Pipeline B (Visuell) | Pipeline C (Text) |
|------------|----------------------|---------------------|-------------------|
| Leinendurchmesser | `measured` | `visual_medium` | `documented` |
| Leinenmaterial | `measured` | `visual_low` | `documented` |
| Leinenzustand (UV) | — | `visual_high` | `documented` |
| Leinenzustand (Schamfil) | — | `visual_high` | `documented` |
| Fendergröße | `measured` | `visual_medium` | `documented` |
| Fenderanzahl | `measured` | `visual_high` | `documented` |
| Fenderposition | — | `visual_high` | — |
| Fenderzustand | — | `visual_high` | `documented` |
| Klampengröße | `measured` | `visual_medium` | `documented` |
| Klampenzustand | — | `visual_high` | `documented` |
| Klüsenzustand | — | `visual_medium` | `documented` |
| Springleinen vorhanden | — | `visual_high` | `documented` |
| Klampenbelegung | — | `visual_high` | — |
| Fenderbrett vorhanden | — | `visual_high` | `documented` |
| Schamfilschutz vorhanden | — | `visual_medium` | `documented` |

### C2 — Score-Fusion-Gewichte für Festmachersystem

| Analysemodul | Strukturdaten-Gewicht | Visuell-Gewicht | Begründung |
|-------------|----------------------|----------------|------------|
| Festmacher-Dimensionierung | 0,85 | 0,15 | Durchmesser aus CAD/Spezifikation präziser als Foto |
| Festmacher-Zustand | 0,10 | 0,90 | Zustand fast nur visuell beurteilbar |
| Fender-Dimensionierung | 0,80 | 0,20 | Größe aus Spezifikation präziser |
| Fender-Zustand | 0,10 | 0,90 | Zustand fast nur visuell beurteilbar |
| Festmacher-Konfiguration | 0,30 | 0,70 | Leinen-Arrangement visuell gut erfassbar |
| Klampen-Bewertung | 0,70 | 0,30 | Dimensionierung aus CAD, Zustand visuell |

---

## ANHANG D — Normen-Zusammenfassung

### D1 — ISO 15084:2003 — Festpunkte

**Kernanforderungen für Festmacherpunkte auf Yachten:**

| Anforderung | Vorschrift | AYDI-Prüfpunkt |
|-------------|-----------|----------------|
| Mindestanzahl Klampen | 4 (Boote <8 m), 6 (8–15 m), 8 (>15 m) | Klampenanzahl prüfen |
| Klampen-Zugfestigkeit | Mindest-Haltekraft nach LOA/Verdrängung | Nur bei `measured` (CAD-Daten) prüfbar |
| Befestigung | Durchbolzung mit Unterlegplatte empfohlen | Visuell: Schraubenanzahl, Plattengröße |
| Position | Bug, Heck, Mittschiffs (beidseitig) | Visuell: Position im Foto erfassbar |
| Material | Korrosionsbeständig (316L empfohlen) | Visuell: Korrosionsspuren erkennbar |

### D2 — DIN EN ISO 2307 — Prüfverfahren

**Standardprüfverfahren für Festmacherleinen:**
- Bruchlast-Test: Leine wird mit konstanter Rate (100–300 mm/min) bis zum Bruch belastet
- Zyklische Belastung: 1.000 Zyklen bei 20–50 % BL, dann Bruchlast-Test
- Schamfiltest: Leine über definierte Kante (Radius, Winkel, Geschwindigkeit)
- UV-Test: Xenon-Bogen-Belichtung nach ISO 4892 (Simulation Sonnenlicht)

### D3 — ABYC H-40 — Festmacherpunkte (US-Standard)

| Bootslänge (ft) | Bootslänge (m) | Min. Zugfestigkeit pro Klampe (lbs) | Min. Zugfestigkeit pro Klampe (kg) |
|-----------------|---------------|-------------------------------------|-------------------------------------|
| 20 | 6,1 | 2.000 | 907 |
| 26 | 7,9 | 4.000 | 1.814 |
| 33 | 10,1 | 6.000 | 2.722 |
| 40 | 12,2 | 8.000 | 3.629 |
| 46 | 14,0 | 10.000 | 4.536 |
| 56 | 17,1 | 15.000 | 6.804 |
| 66 | 20,1 | 20.000 | 9.072 |

---

## ANHANG E — Wartungsintervalle

### E1 — Festmacherleinen — Wartungsplan

| Intervall | Maßnahme | Kritisch für | Confidence |
|-----------|----------|-------------|------------|
| Nach jeder Nutzung | Visuelle Kontrolle auf Schamfilschäden | Sicherheit | documented |
| Monatlich | Leinen mit Süßwasser spülen | Lebensdauer (Salzkristalle) | documented |
| Vierteljährlich | Leinen auf UV-Degradation prüfen (Farbe, Sprödigkeit) | Sicherheit | documented |
| Halbjährlich | Schamfilschutz-Zustand prüfen und ggf. erneuern | Sicherheit | documented |
| Jährlich | Leinen wenden (Auge am anderen Ende verwenden) | Lebensdauer | estimated |
| Alle 2–3 Jahre | Austausch bei intensiver Nutzung (Dauerlieger) | Sicherheit | documented |
| Alle 3–5 Jahre | Austausch bei normaler Nutzung | Sicherheit | documented |
| Sofort | Austausch nach Sturmbelastung (>8 Bft) | Sicherheit | documented |
| Sofort | Austausch bei sichtbaren Schamfilschäden (Kern sichtbar) | Sicherheit | documented |

### E2 — Fender — Wartungsplan

| Intervall | Maßnahme | Kritisch für | Confidence |
|-----------|----------|-------------|------------|
| Monatlich | Fender mit Süßwasser und Schwamm reinigen | Ästhetik + Kontrolle | documented |
| Vierteljährlich | Druck prüfen — nachpumpen wenn schlaff | Schutzfunktion | documented |
| Halbjährlich | Ventil prüfen (Dichtigkeit) | Schutzfunktion | documented |
| Jährlich | UV-Schäden prüfen (Verfärbung, Risse, Sprödigkeit) | Lebensdauer | documented |
| Alle 5–8 Jahre | Austausch bei normaler Nutzung | Schutzfunktion | estimated |
| Alle 3–5 Jahre | Austausch bei Dauerexposition (Mittelmeer, Tropen) | Schutzfunktion | estimated |
| Sofort | Austausch bei Rissen, Löchern oder permanenter Verformung | Schutzfunktion | documented |

### E3 — Klampen und Beschläge — Wartungsplan

| Intervall | Maßnahme | Kritisch für | Confidence |
|-----------|----------|-------------|------------|
| Halbjährlich | Klampen-Befestigung prüfen (Schrauben nachziehen) | Sicherheit | documented |
| Jährlich | Korrosionsprüfung (besonders Schrauben, Unterlegplatten) | Sicherheit | documented |
| Jährlich | Klüsen-Kanten prüfen (scharfe Stellen? → entgraten oder Rollen nachrüsten) | Schamfil-Prävention | documented |
| Alle 3–5 Jahre | Dichtigkeit der Klampen-Durchführung prüfen (Deck-Leckage) | Deck-Integrität | documented |

---

## ANHANG F — Liegeplatz-Bewertung

### F1 — AYDI-Liegeplatz-Risikobewertung

| Faktor | Niedrig (1) | Mittel (3) | Hoch (5) | Gewicht |
|--------|-------------|------------|----------|---------|
| Windexposition | Geschützter Hafen | Teilweise geschützt | Offene Reede | 0,30 |
| Schwell/Welle | Kein Schwell | Leichter Schwell | Starker Schwell | 0,25 |
| Tidenhub | <1 m | 1–3 m | >3 m | 0,15 |
| Stegbeschaffenheit | Schwimmsteg (modern) | Feste Pier (glatt) | Pfähle / raue Mole | 0,15 |
| Passierer-Verkehr | Wenig Verkehr | Mäßiger Verkehr | Starker Verkehr (Fähren!) | 0,10 |
| Sturmhäufigkeit | Selten (<5/Saison) | Mittel (5–15/Saison) | Häufig (>15/Saison) | 0,05 |

**Liegeplatz-Score = Σ (Faktor × Gewicht)**

| Score | Risikostufe | Festmacher-Empfehlung |
|-------|------------|----------------------|
| 1,0–2,0 | Niedrig | Standard-Dimensionierung |
| 2,1–3,0 | Mittel | Standard + Schamfilschutz |
| 3,1–4,0 | Hoch | Schwerwetter-Dimensionierung + Schamfilschutz + Fenderbretter |
| 4,1–5,0 | Sehr hoch | Überdimensionierung + doppelte Leinen + maximale Fender |

---

## ANHANG G — Historische Entwicklung

### G1 — Zeitleiste der Festmacher-Technologie

| Zeitraum | Entwicklung | Auswirkung |
|----------|-------------|------------|
| Vor 1800 | Hanf- und Manilatau | Naturfasern, kurze Lebensdauer, geringe Bruchlast |
| 1800–1940 | Manila-Tauwerk dominiert | Bessere Qualität, standardisierte Herstellung |
| 1938 | Erfindung von Nylon (DuPont) | Revolution der Festmacher-Technologie |
| 1950er | Nylon-Tauwerk wird erschwinglich | Synthetik ersetzt Naturfasern innerhalb einer Dekade |
| 1960er | Polyester-Tauwerk verfügbar | Alternative mit besserer UV-Beständigkeit |
| 1970er | Erste PVC-Fender | Ersetzt Kork- und Sisal-Fender |
| 1975 | Polyform AS gegründet (Norwegen) | Beginn der modernen Fender-Industrie |
| 1980er | Doppelgeflecht-Konstruktion verbreitet | Besseres Handling, kein Kinken |
| 1990 | HMPE (Dyneema) kommerziell verfügbar | Hochleistungsfasern, zunächst nur Regatta |
| 2000er | Vorgefertigte Festmacher mit Spleißaugen | Qualitätssicherung, einfache Handhabung |
| 2010er | Pneumatische Fender für Megayachten | Superyacht-Boom treibt Innovation |
| 2020er | Recycelte PET-Fasern für Leinen | Nachhaltigkeitstrend, erste Produkte |
| 2025+ | Smarte Festmacher (Lastmessung, App-Warnung) | In Entwicklung bei mehreren Herstellern |

---

## ANHANG H — AYDI-Integration (Pydantic-Modelle)

### H1 — Festmacherleine-Modell

```python
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class LineMaterial(str, Enum):
    """Material classification for mooring lines."""
    NYLON = "nylon"
    POLYESTER = "polyester"
    HMPE = "hmpe"
    POLYPROPYLENE = "polypropylene"
    MIXED = "mixed"


class LineConstruction(str, Enum):
    """Construction type for mooring lines."""
    THREE_STRAND = "three_strand"
    DOUBLE_BRAID = "double_braid"
    OCTOPLAIT = "octoplait"
    SINGLE_BRAID = "single_braid"


class LineFunction(str, Enum):
    """Functional role of a mooring line."""
    BOW_LINE = "bow_line"
    STERN_LINE = "stern_line"
    FORWARD_SPRING = "forward_spring"
    AFT_SPRING = "aft_spring"
    BREAST_LINE = "breast_line"
    MOORING_LINE = "mooring_line"
    RESERVE = "reserve"


class ConfidenceLevel(str, Enum):
    """Confidence level for assessment data."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class LineCondition(str, Enum):
    """Condition assessment for mooring lines."""
    NEW = "new"
    GOOD = "good"
    FAIR = "fair"
    POOR = "poor"
    CRITICAL = "critical"
    REPLACE_IMMEDIATELY = "replace_immediately"


class MooringLine(BaseModel):
    """Represents a single mooring line with specifications and condition."""

    model_config = {"from_attributes": True}

    line_id: str = Field(..., description="Unique identifier for this line")
    function: LineFunction = Field(..., description="Functional role of the line")
    material: LineMaterial = Field(..., description="Primary fiber material")
    construction: LineConstruction = Field(
        ..., description="Rope construction type"
    )
    diameter_mm: float = Field(
        ..., ge=6, le=80, description="Nominal diameter in mm"
    )
    length_m: float = Field(
        ..., ge=1, le=100, description="Total length in meters"
    )
    breaking_load_kn: Optional[float] = Field(
        None, ge=0, description="Nominal breaking load in kN"
    )
    has_spliced_eye: bool = Field(
        False, description="Whether the line has a professionally spliced eye"
    )
    has_thimble: bool = Field(
        False, description="Whether a thimble is fitted in the eye"
    )
    has_chafe_protection: bool = Field(
        False, description="Whether chafe protection is installed"
    )
    condition: Optional[LineCondition] = Field(
        None, description="Current condition assessment"
    )
    age_years: Optional[float] = Field(
        None, ge=0, description="Estimated age in years"
    )
    manufacturer: Optional[str] = Field(
        None, description="Manufacturer name"
    )
    product_name: Optional[str] = Field(
        None, description="Product line name"
    )
    confidence: ConfidenceLevel = Field(
        ..., description="Confidence level of this data"
    )
    notes: Optional[str] = Field(
        None, description="Additional notes or observations"
    )
```

### H2 — Fender-Modell

```python
class FenderType(str, Enum):
    """Classification of fender types."""
    CYLINDRICAL = "cylindrical"
    BALL = "ball"
    FLAT = "flat"
    PNEUMATIC = "pneumatic"
    STEP = "step"
    BOW_STERN = "bow_stern"


class FenderCondition(str, Enum):
    """Condition assessment for fenders."""
    NEW = "new"
    GOOD = "good"
    FAIR = "fair"
    DEFLATED = "deflated"
    DEFORMED = "deformed"
    CRACKED = "cracked"
    REPLACE = "replace"


class Fender(BaseModel):
    """Represents a single fender with specifications and condition."""

    model_config = {"from_attributes": True}

    fender_id: str = Field(..., description="Unique identifier for this fender")
    fender_type: FenderType = Field(..., description="Fender type classification")
    diameter_mm: float = Field(
        ..., ge=50, le=2000, description="Diameter in mm (or width for flat)"
    )
    length_mm: Optional[float] = Field(
        None, ge=100, le=5000,
        description="Length in mm (cylindrical/bow_stern only)"
    )
    thickness_mm: Optional[float] = Field(
        None, ge=20, le=300, description="Thickness in mm (flat only)"
    )
    color: Optional[str] = Field(
        None, description="Fender color (white, blue, black, grey)"
    )
    manufacturer: Optional[str] = Field(
        None, description="Manufacturer name"
    )
    model_name: Optional[str] = Field(
        None, description="Model designation"
    )
    condition: Optional[FenderCondition] = Field(
        None, description="Current condition assessment"
    )
    position: Optional[str] = Field(
        None, description="Position on the boat (bow, midship_port, etc.)"
    )
    energy_absorption_j: Optional[float] = Field(
        None, ge=0,
        description="Energy absorption capacity in Joules"
    )
    confidence: ConfidenceLevel = Field(
        ..., description="Confidence level of this data"
    )
```

### H3 — Klampen-Modell

```python
class CleatMaterial(str, Enum):
    """Material classification for cleats."""
    STAINLESS_316L = "stainless_316l"
    STAINLESS_304 = "stainless_304"
    ALUMINUM = "aluminum"
    BRONZE = "bronze"
    NYLON_PA = "nylon_pa"
    UNKNOWN = "unknown"


class CleatMounting(str, Enum):
    """Mounting method for cleats."""
    THROUGH_BOLTED = "through_bolted"
    SCREWED = "screwed"
    WELDED = "welded"
    UNKNOWN = "unknown"


class Cleat(BaseModel):
    """Represents a deck cleat for mooring lines."""

    model_config = {"from_attributes": True}

    cleat_id: str = Field(..., description="Unique identifier")
    position: str = Field(
        ..., description="Position on boat (bow_port, stern_stbd, midship_port, etc.)"
    )
    length_mm: float = Field(
        ..., ge=50, le=600, description="Cleat length in mm"
    )
    material: CleatMaterial = Field(
        ..., description="Cleat material"
    )
    mounting: CleatMounting = Field(
        ..., description="Mounting method"
    )
    has_backing_plate: Optional[bool] = Field(
        None, description="Whether a backing plate is fitted underneath"
    )
    max_line_diameter_mm: Optional[float] = Field(
        None, ge=0, description="Maximum line diameter the cleat can accommodate"
    )
    condition: Optional[str] = Field(
        None, description="Condition: good, fair, corroded, damaged, loose"
    )
    confidence: ConfidenceLevel = Field(
        ..., description="Confidence level of this data"
    )
```

### H4 — Festmachersystem-Gesamtbewertung

```python
class MooringSystemRating(str, Enum):
    """Overall rating categories for mooring system."""
    EXCELLENT = "excellent"
    VERY_GOOD = "very_good"
    GOOD = "good"
    FAIR = "fair"
    POOR = "poor"
    CRITICAL = "critical"


class FindingSeverity(str, Enum):
    """Severity level for findings."""
    INFO = "info"
    WARNING = "warning"
    HIGH = "high"
    CRITICAL = "critical"


class MooringFinding(BaseModel):
    """A single finding from the mooring system analysis."""

    model_config = {"from_attributes": True}

    finding_id: str = Field(..., description="Unique finding identifier")
    category: str = Field(
        ..., description="Finding category (lines, fenders, cleats, configuration)"
    )
    severity: FindingSeverity = Field(..., description="Finding severity")
    title_de: str = Field(..., description="Finding title in German")
    description_de: str = Field(
        ..., description="Detailed description in German"
    )
    recommendation_de: str = Field(
        ..., description="Recommendation in German"
    )
    score_impact: int = Field(
        ..., ge=-100, le=100,
        description="Score impact (-100 to +100)"
    )
    confidence: ConfidenceLevel = Field(
        ..., description="Confidence level of this finding"
    )
    reference: Optional[str] = Field(
        None, description="Reference to fault pattern (e.g. F-FM-001)"
    )


class FenderBoard(BaseModel):
    """Represents a fender board."""

    model_config = {"from_attributes": True}

    board_id: str = Field(..., description="Unique identifier")
    length_mm: float = Field(
        ..., ge=300, le=3000, description="Board length in mm"
    )
    width_mm: float = Field(
        ..., ge=100, le=500, description="Board width in mm"
    )
    thickness_mm: float = Field(
        ..., ge=15, le=100, description="Board thickness in mm"
    )
    material: str = Field(
        ..., description="Board material (wood, grp, plastic)"
    )
    fender_count: int = Field(
        ..., ge=1, le=6, description="Number of fenders behind the board"
    )
    condition: Optional[str] = Field(
        None, description="Condition: good, fair, damaged"
    )
    confidence: ConfidenceLevel = Field(
        ..., description="Confidence level"
    )


class MooringSystemAssessment(BaseModel):
    """Complete mooring system assessment for a yacht."""

    model_config = {"from_attributes": True}

    boat_loa_m: float = Field(
        ..., ge=4, le=80, description="Boat length overall in meters"
    )
    boat_beam_m: float = Field(
        ..., ge=1, le=20, description="Boat beam in meters"
    )
    boat_displacement_kg: Optional[float] = Field(
        None, ge=100, description="Boat displacement in kg"
    )
    boat_freeboard_m: Optional[float] = Field(
        None, ge=0.1, description="Freeboard in meters"
    )
    boat_type: str = Field(
        ..., description="Boat type: sailboat, motoryacht, catamaran"
    )

    lines: list[MooringLine] = Field(
        default_factory=list, description="All mooring lines"
    )
    fenders: list[Fender] = Field(
        default_factory=list, description="All fenders"
    )
    fender_boards: list[FenderBoard] = Field(
        default_factory=list, description="Fender boards"
    )
    cleats: list[Cleat] = Field(
        default_factory=list, description="All cleats"
    )

    # Recommended values (calculated by AYDI)
    recommended_line_diameter_mm: Optional[float] = Field(
        None, description="Recommended line diameter based on LOA"
    )
    recommended_fender_diameter_mm: Optional[float] = Field(
        None, description="Recommended fender diameter based on LOA/freeboard"
    )
    recommended_fender_count: Optional[int] = Field(
        None, description="Recommended number of fenders"
    )
    recommended_line_count: Optional[int] = Field(
        None, description="Recommended number of mooring lines"
    )

    # Assessment results
    findings: list[MooringFinding] = Field(
        default_factory=list, description="All findings from the analysis"
    )
    total_score: int = Field(
        ..., ge=0, le=100, description="Total mooring system score (0-100)"
    )
    rating: MooringSystemRating = Field(
        ..., description="Overall rating category"
    )
    available: bool = Field(
        True, description="Whether this assessment could be performed"
    )
    skip_reason: Optional[str] = Field(
        None,
        description="Reason if assessment could not be performed"
    )
    confidence: ConfidenceLevel = Field(
        ..., description="Overall confidence level of the assessment"
    )
```

### H5 — Berechnungsfunktionen

```python
import math


def calculate_wind_force_kn(
    windage_area_m2: float,
    wind_speed_ms: float,
    drag_coefficient: float = 1.0,
) -> float:
    """Calculate wind force on a moored yacht.

    Args:
        windage_area_m2: Projected windage area in m².
        wind_speed_ms: Wind speed in m/s.
        drag_coefficient: Drag coefficient (0.8-1.2, default 1.0).

    Returns:
        Wind force in kN.
    """
    air_density = 1.225  # kg/m³ at sea level
    force_n = 0.5 * air_density * drag_coefficient * windage_area_m2 * wind_speed_ms ** 2
    return force_n / 1000.0


def recommend_line_diameter_mm(
    loa_m: float,
    heavy_weather: bool = False,
) -> float:
    """Recommend mooring line diameter based on LOA.

    Args:
        loa_m: Length overall in meters.
        heavy_weather: If True, add 2 mm for exposed berths.

    Returns:
        Recommended diameter in mm.
    """
    base = loa_m + 4.0
    if heavy_weather:
        base += 2.0
    return math.ceil(base / 2.0) * 2  # Round up to next even number


def recommend_fender_diameter_mm(loa_m: float) -> float:
    """Recommend fender diameter based on LOA.

    Args:
        loa_m: Length overall in meters.

    Returns:
        Recommended fender diameter in mm.
    """
    return round(loa_m * 15 + 30, -1)  # Round to nearest 10


def recommend_fender_count(loa_m: float) -> int:
    """Recommend minimum number of fenders based on LOA.

    Args:
        loa_m: Length overall in meters.

    Returns:
        Minimum number of fenders.
    """
    return max(4, math.ceil(loa_m / 2.0))


def recommend_line_length_m(
    loa_m: float,
    line_function: str,
    tidal_range_m: float = 0.0,
) -> float:
    """Recommend mooring line length.

    Args:
        loa_m: Length overall in meters.
        line_function: One of bow_line, stern_line, spring, breast_line.
        tidal_range_m: Tidal range at berth in meters.

    Returns:
        Recommended line length in meters.
    """
    multipliers = {
        "bow_line": 1.5,
        "stern_line": 1.5,
        "spring": 1.0,
        "breast_line": 0.7,
    }
    tide_factors = {
        "bow_line": 1.5,
        "stern_line": 1.5,
        "spring": 1.0,
        "breast_line": 2.0,
    }
    multiplier = multipliers.get(line_function, 1.5)
    tide_factor = tide_factors.get(line_function, 1.5)
    base_length = loa_m * multiplier
    tide_addition = tidal_range_m * tide_factor
    total = base_length + tide_addition
    return math.ceil(total / 2.0) * 2  # Round up to next even number


def calculate_berthing_energy_j(
    displacement_kg: float,
    approach_speed_ms: float = 0.15,
    added_mass_coefficient: float = 1.7,
    softness_coefficient: float = 0.9,
    configuration_coefficient: float = 0.7,
) -> float:
    """Calculate berthing energy for fender sizing.

    Args:
        displacement_kg: Boat displacement in kg.
        approach_speed_ms: Approach speed in m/s (default 0.15).
        added_mass_coefficient: Hydrodynamic added mass (1.5-1.8).
        softness_coefficient: Berth softness (0.9-1.0).
        configuration_coefficient: Contact configuration (0.5-1.0).

    Returns:
        Berthing energy in Joules.
    """
    return (
        0.5
        * displacement_kg
        * approach_speed_ms ** 2
        * added_mass_coefficient
        * softness_coefficient
        * configuration_coefficient
    )


def assess_line_condition(
    age_years: float,
    usage_nights_per_year: int = 100,
    has_chafe_damage: bool = False,
    has_uv_damage: bool = False,
    was_storm_loaded: bool = False,
) -> str:
    """Assess mooring line condition based on usage factors.

    Returns:
        Condition string: new, good, fair, poor, critical, replace_immediately.
    """
    estimated_cycles = age_years * usage_nights_per_year * 50

    if has_chafe_damage and estimated_cycles > 10000:
        return "replace_immediately"
    if was_storm_loaded and age_years > 2:
        return "replace_immediately"
    if has_chafe_damage:
        return "critical"
    if has_uv_damage and age_years > 3:
        return "poor"
    if estimated_cycles > 50000:
        return "poor"
    if estimated_cycles > 25000 or has_uv_damage:
        return "fair"
    if estimated_cycles > 5000:
        return "good"
    return "new"
```

---

## ANHANG I — Bewertungsschema

### I1 — Scoring-System für Festmachersystem

**Gesamtscore:** 0–100 Punkte, aufgeteilt in Kategorien:

| Kategorie | Gewicht | Prüfpunkte |
|-----------|---------|------------|
| Festmacher-Dimensionierung | 25 % | Durchmesser, Material, Bruchlast |
| Festmacher-Zustand | 15 % | UV, Schamfil, Alter |
| Festmacher-Konfiguration | 15 % | Springs vorhanden, Anzahl, Länge |
| Fender-Dimensionierung | 15 % | Durchmesser, Anzahl |
| Fender-Zustand | 10 % | Verformung, Risse, Druck |
| Fender-Konfiguration | 10 % | Position, Fenderbrett |
| Klampen/Beschläge | 10 % | Größe, Material, Befestigung |

### I2 — Score-Bewertungsskala

| Score | Rating | Beschreibung |
|-------|--------|-------------|
| 90–100 | EXZELLENT | Vorbildliche Ausstattung, über Mindestanforderungen |
| 75–89 | SEHR GUT | Alle Mindestanforderungen erfüllt, guter Zustand |
| 60–74 | GUT | Weitgehend korrekt, kleinere Verbesserungen möglich |
| 45–59 | AUSREICHEND | Mehrere Mängel, Verbesserung empfohlen |
| 25–44 | MANGELHAFT | Erhebliche Mängel, zeitnahe Behebung erforderlich |
| 0–24 | KRITISCH | Sicherheitsrelevante Mängel, sofortige Maßnahmen |

### I3 — Score-Abzüge nach Fehlerbild

| Fehlerbild | Score-Abzug | Kategorie |
|------------|-------------|-----------|
| F-FM-001 (Leinen unterdimensioniert) | −30 bis −50 | KRITISCH |
| F-FM-002 (Schamfilschaden) | −20 bis −40 | HOCH |
| F-FM-003 (UV-Degradation) | −10 bis −30 | MITTEL–HOCH |
| F-FM-004 (Falsche Knotenverbindung) | −10 bis −20 | MITTEL |
| F-FM-005 (Fender zu klein) | −20 bis −40 | HOCH |
| F-FM-006 (Fender falsch positioniert) | −10 bis −25 | MITTEL |
| F-FM-007 (Fender beschädigt) | −10 bis −20 | MITTEL |
| F-FM-008 (Fehlende Springleinen) | −25 bis −40 | HOCH |
| F-FM-009 (Falsche Klampenbelegung) | −30 bis −50 | KRITISCH |
| F-FM-010 (Kein Fenderbrett bei Pfahl) | −15 bis −25 | MITTEL–HOCH |
| F-FM-011 (Zu wenige Fender) | −10 bis −20 | MITTEL |
| F-FM-012 (Klampen unterdimensioniert) | −20 bis −40 | HOCH–KRITISCH |

---

## ANHANG J — Troubleshooting-Entscheidungsbäume (erweitert)

### J1 — Erweiterte Diagnoseprozedur: Leinenbruch

```
LEINENBRUCH — Vollständige Diagnose
│
├── SCHRITT 1: Bruchstelle identifizieren
│   ├── Am Auge/Spleiß → Spleißqualität mangelhaft
│   │   └── Aktion: Neuer professioneller Spleiß oder vorgefertigte Leine
│   ├── An Klüse/Beschlag → Schamfil
│   │   └── Aktion: Schamfilschutz + ggf. Klüsenrollen
│   ├── An Klampe → Überlast oder scharfe Klampenkante
│   │   └── Aktion: Klampe entgraten, ggf. größere Klampe
│   ├── Im freien Lauf (Mitte) → Material-Versagen
│   │   └── Weiter zu SCHRITT 2
│   └── Am Knoten → Knoten-Festigkeitsreduktion
│       └── Aktion: Gespleißtes Auge verwenden
│
├── SCHRITT 2: Bruchursache Material
│   ├── Fasern spröde/trocken → UV-Degradation
│   │   └── Aktion: Alle Leinen prüfen, UV-exponierte ersetzen
│   ├── Fasern aufgelöst/pelzig → Abrieb/Schamfil
│   │   └── Aktion: Leinenführung prüfen, Schutz anbringen
│   ├── Fasern weich, aber gerissen → Überlast
│   │   └── Aktion: Durchmesser erhöhen, Surge-Schutz verbessern
│   └── Fasern verfärbt/brüchig → Chemische Degradation
│       └── Aktion: Kontakt mit Chemikalien/Diesel prüfen
│
└── SCHRITT 3: Systemische Prüfung
    ├── Weitere Leinen gleichen Alters prüfen
    ├── Leinenführung an allen Kontaktstellen prüfen
    ├── Dimensionierung für Bootsklasse verifizieren
    ├── Liegeplatz-Risikobewertung durchführen (→ Anhang F)
    └── Wartungsintervall anpassen (→ Anhang E)
```

### J2 — Erweiterte Diagnoseprozedur: Wiederkehrender Fenderverlust

```
FENDERVERLUST — Wiederkehrend
│
├── Fender geht bei Fahrt verloren
│   ├── Fender vor Ablegen nicht eingeholt → Prozedur-Fehler
│   │   └── SOP: Fender IMMER einholen BEVOR Leinen los
│   ├── Fenderleine reißt bei Fahrtgeschwindigkeit → Hydrodynamik
│   │   └── Fenderleine kürzen (max. Freibord + 30 cm)
│   └── Fender wird vom Wind abgerissen → Fenderhaken-Problem
│       └── Schnellverschluss-Fenderhalter verwenden
│
├── Fender geht am Steg verloren
│   ├── Fenderleine zu lang → Fender taucht unter Steg
│   │   └── Fenderleine so kürzen, dass Fender NICHT unter Steg passt
│   ├── Webeleinstek löst sich → Knoten-Fehler
│   │   └── Webeleinstek mit Slippstich oder Rundtörn sichern
│   └── Reling-Befestigung löst sich → Fenderhaken defekt
│       └── Hochwertige Fenderhaken oder Klampen-Befestigung
│
└── Fender wird gestohlen (Mittelmeer!)
    ├── Fenderleine mit Drahtseele verwenden
    ├── Fender mit Boot-Namen beschriften
    └── Im Hafen: Fender nachts ins Boot nehmen (wenn möglich)
```

---

## ANHANG K — Kostenkalkulation

### K1 — 10-Jahres-Gesamtkosten Festmacher-/Fenderausstattung

Annahme: Leinen-Austausch alle 4 Jahre, Fender-Austausch alle 7 Jahre, Zubehör alle 3 Jahre

| Bootslänge | Erstausstattung | Jahr 3 (Zubehör) | Jahr 4 (Leinen) | Jahr 6 (Zubehör) | Jahr 7 (Fender) | Jahr 8 (Leinen) | 10-J-Gesamt | Confidence |
|------------|----------------|-------------------|-----------------|-------------------|-----------------|-----------------|-------------|------------|
| 8 m | 450 EUR | 50 EUR | 150 EUR | 50 EUR | 220 EUR | 150 EUR | 1.070 EUR | estimated |
| 10 m | 660 EUR | 65 EUR | 230 EUR | 65 EUR | 320 EUR | 230 EUR | 1.570 EUR | estimated |
| 12 m | 960 EUR | 80 EUR | 350 EUR | 80 EUR | 470 EUR | 350 EUR | 2.290 EUR | estimated |
| 15 m | 1.400 EUR | 105 EUR | 530 EUR | 105 EUR | 700 EUR | 530 EUR | 3.370 EUR | estimated |
| 20 m | 2.700 EUR | 175 EUR | 1.050 EUR | 175 EUR | 1.300 EUR | 1.050 EUR | 6.450 EUR | estimated |

### K2 — Kosten-Nutzen-Analyse: Schadensvermeidung

| Schadensszenario | Typische Reparaturkosten | Vermeidbare Kosten durch korrekte Ausstattung | ROI |
|------------------|--------------------------|------------------------------------------------|-----|
| GFK-Rumpfreparatur (klein) | 1.500–3.000 EUR | 200 EUR (2 größere Fender) | 7–15× |
| GFK-Rumpfreparatur (groß) | 5.000–10.000 EUR | 400 EUR (Fenderbrett + Schamfilschutz) | 12–25× |
| Lackschaden (Motoryacht) | 5.000–20.000 EUR | 300 EUR (Premium-Fender + Socken) | 17–67× |
| Reling-Reparatur | 800–2.500 EUR | 100 EUR (zusätzliche Fender) | 8–25× |
| Leinenbruch + Abtreiben | 2.000–50.000+ EUR | 250 EUR (korrekt dimensionierte Leinen) | 8–200× |
| Klampe herausgerissen | 1.500–5.000 EUR | 150 EUR (Durchbolzung + Platte) | 10–33× |

---

## ANHANG L — Regionale Empfehlungen

### L1 — Ostsee

| Aspekt | Empfehlung | Begründung |
|--------|-----------|------------|
| Leinenmaterial | Nylon, dreikarätiges | Standard, moderate Bedingungen |
| Leinen-Ø | Standard (LOA + 4 mm) | Normaler Tidenhub, moderate Winde |
| Fendergröße | Standard | Schwimmstege dominant |
| Fenderbrett | Empfohlen | Pfahl-Liegeplätze in einigen Häfen |
| Besonderheit | Leinen im Winter einlagern | Frost → Nylon wird spröde |
| Tidenhub | 0–0,5 m (minimal) | Leinen können kürzer sein |

### L2 — Nordsee / Ärmelkanal

| Aspekt | Empfehlung | Begründung |
|--------|-----------|------------|
| Leinenmaterial | Nylon, dreikarätiges oder Octoplait | Hohe Beanspruchung |
| Leinen-Ø | Schwerwetter (LOA + 6 mm) | Starke Gezeiten, Starkwind häufig |
| Leinen-Länge | Überlang (Tide beachten!) | Tidenhub 3–7 m! |
| Fendergröße | 1 Stufe über Standard | Raue Bedingungen, alte Kaimauern |
| Fenderbrett | ZWINGEND | Pfahl-Liegeplätze, Schleusen, raue Stege |
| Schamfilschutz | ZWINGEND an allen Kontaktstellen | Kaimauern, Metallpoller, raue Oberflächen |
| Besonderheit | Tide-Leinen | Spezielle überlange Leinen für Tide-Häfen |

### L3 — Mittelmeer

| Aspekt | Empfehlung | Begründung |
|--------|-----------|------------|
| Leinenmaterial | Nylon oder Polyester (besser UV) | Extreme UV-Belastung |
| Leinen-Ø | Standard, aber zusätzliche Muringleine | Heckanleger-Standard |
| Fendergröße | Standard (Schwimmstege dominant) | Moderne Marinas |
| Fenderfarbe | Weiß oder Blau (NICHT schwarz) | Hitze → schwarze Fender markieren Rumpf |
| Besonderheit | Muringleine prüfen! | Hafen-Muringleinen oft in schlechtem Zustand |
| UV-Austausch | Leinen alle 2–3 Jahre | Extremer UV-Verschleiß |
| Sturmvorbereitung | Meltemi/Bora: überdimensionieren | Lokale Starkwindereignisse sehr heftig |

### L4 — Atlantik / Blauwasser

| Aspekt | Empfehlung | Begründung |
|--------|-----------|------------|
| Leinenmaterial | Nylon, dreikarätiges, überdimensioniert | Vielfältige Bedingungen |
| Leinen-Ø | Schwerwetter (LOA + 6 mm) | Unbekannte Liegeplätze, Expositionsrisiko |
| Leinen-Anzahl | Minimum 10 | Reserven für alle Situationen |
| Fendergröße | 1 Stufe über Standard | Raue Kaimauern, Schleusen, Päckchen |
| Fenderbrett | 2 Stück | Unverzichtbar für unbekannte Häfen |
| Schamfilschutz-Set | Komplett (12+ Stk) | Raue Bedingungen überall |
| Besonderheit | Reparatur-Set mitführen | Spleißnadel, Seilklemmen, Ersatzfender |

---

## ANHANG M — Testprotokolle und Prüfverfahren

### M1 — Visuelle Prüfung von Festmacherleinen (AYDI-Protokoll)

```
VISUELLE PRÜFUNG — FESTMACHERLEINE
===================================
Datum: ___________
Prüfer: ___________
Leine Nr.: ___________

1. ALLGEMEINZUSTAND
   □ Farbe gleichmäßig?         [ja / leichte Veränderung / starke Veränderung]
   □ Oberfläche glatt?          [ja / leicht rau / pelzig / spröde]
   □ Flexibilität erhalten?     [ja / leicht steif / steif / brüchig]

2. SCHAMFIL-INSPEKTION (alle 50 cm prüfen)
   □ Aufgeraute Stellen?        [keine / 1–2 / 3–5 / >5]
   □ Kern sichtbar (DB)?        [nein / angedeutet / deutlich / Kern freiliegend]
   □ Abflachung des Querschnitts? [nein / leicht / deutlich / stark]

3. SPLEISSTELLE / AUGE
   □ Spleiß fest?                [ja / leicht lose / lose / öffnet sich]
   □ Kausche vorhanden?         [ja / nein / beschädigt]
   □ Markierungsfaden sichtbar? [ja / teilweise / nein]

4. GESAMTBEWERTUNG
   □ Einsatzfähig               [ja / eingeschränkt / nein]
   □ Restlebensdauer (geschätzt) [>3 Jahre / 1–3 Jahre / <1 Jahr / sofort ersetzen]

Confidence: visual_high (wenn Leine in der Hand geprüft)
            visual_medium (wenn nur visuell, aus Foto)
```

### M2 — Bruchlast-Prüfung (Laborstandard)

**Prüfnorm:** DIN EN ISO 2307
**Prüfmaschine:** Universalzugprüfmaschine, Kapazität ≥ 2 × erwartete Bruchlast
**Probenlänge:** Min. 1 m freie Länge zwischen den Klemmen
**Vorbelastung:** 5 % der erwarteten Bruchlast für 60 s
**Zuggeschwindigkeit:** 100–300 mm/min
**Messwerte:** Kraft (kN), Dehnung (%), Bruchbild (Foto)

---

## ANHANG N — Zusätzliche Fallstudien

### N1 — Katamaranfestmacher — Lagoon 42 in Kroatien (2024)

**Besonderheit Katamaran:**
- Größere Windangriffsfläche bei gleicher LOA (breiter, höher)
- Höhere seitliche Lasten durch Brückendeck
- Klampen-Abstand breiter als bei Einrumpfyacht

**Empfehlung:**
- Leinen 1 Stufe dicker als für gleiche LOA Einrumpfer
- Fender: je 4 pro Rumpf (= 8 total für 12 m Kat)
- Sonderfall: Fender zwischen den Rümpfen bei Ankern in engem Feld

### N2 — Schweres Motorboot — Grand Banks 46 in Holland (2023)

**Besonderheit:**
- Hohe Aufbauten → extreme Windangriffsfläche (55 m² querab)
- Hohes Freibord → Fender müssen hoch hängen
- Schwere Verdrängung (24.000 kg) → hohe Anlegeenergie

**Dimensionierung:**
- Leinen: 24 mm Nylon, 8 Stück
- Fender: Polyform F-6 (340 mm), 8 Stück
- Ergebnis: Problemloser Betrieb seit 2 Saisons

### N3 — Regattayacht — J/111 in Kiel (2024)

**Besonderheit:**
- Leichtbau → empfindlicher Rumpf (dünnes Laminat)
- Viele Beschläge am Deck → Schamfilrisiko
- Budget-Festmacher vom Segelmacher → Qualitätsproblem

**Problem:** Schamfilschaden an einer Spring nach 1 Regattawoche
**Lösung:** Schamfilschutz nachrüsten, Festmacher von Segelmacher durch Liros Handy Elastic ersetzen

---

## ANHANG O — Eigner-Erfahrungen und Feldberichte

### O1 — Langfahrt-Erfahrung: 15.000 sm mit Nylon vs. Polyester

**Eigner:** Segelyacht HR 372, LOA 11,35 m, 3 Jahre Atlantikrunde

**Ergebnis:**
- Nylon-Festmacher (Liros Handy Elastic, 16 mm): 2 Sets verbraucht in 3 Jahren
  - Hauptverschleiß: UV-Degradation (Tropen) und Schamfil (Kaimauern)
  - Stoßdämpfung: exzellent, Boot lag immer ruhig
- Polyester-Festmacher (Gleistein HarborLine, 16 mm): 1 Set hielt 3 Jahre
  - Geringerer UV-Verschleiß, aber härtere Stöße am Steg
  - Für Muringleinen (Heckanleger) klar besser geeignet

**Fazit des Eigners:** "Nylon für bewegte Liegeplätze, Polyester für ruhige Marinas und als Muringleine."
- Confidence: `documented` (persönlicher Erfahrungsbericht, verifiziert)

### O2 — Forum-Konsens: Meistempfohlene Produkte (2024)

**Zusammenfassung aus Segeln-Forum, Boote-Forum, Cruising-Forum (>500 Beiträge):**

| Rang | Festmacher-Produkt | Nennungen | Bewertung |
|------|-------------------|-----------|-----------|
| 1 | Liros Handy Elastic | 127 | 4,6/5 |
| 2 | Gleistein Dock | 89 | 4,5/5 |
| 3 | Liros Squareline | 74 | 4,4/5 |
| 4 | Robline Dockline | 65 | 4,2/5 |
| 5 | Marlow 3-Strand Nylon | 42 | 4,3/5 |

| Rang | Fender-Produkt | Nennungen | Bewertung |
|------|---------------|-----------|-----------|
| 1 | Polyform F-Serie | 198 | 4,7/5 |
| 2 | Dan-Fender Standard | 72 | 4,5/5 |
| 3 | Majoni Star | 68 | 4,1/5 |
| 4 | Polyform A-Serie (Kugel) | 55 | 4,6/5 |
| 5 | Ocean HD | 34 | 4,3/5 |

- Confidence: `estimated` (Forum-Auswertung, subjektive Bewertungen)

---

## ANHANG P — Materialkunde Festmacher und Fender

### P1 — Fasermikroskopie — Degradationszeichen

| Degradationsart | Mikroskopisch | Makroskopisch | Bruchlastverlust | Confidence |
|----------------|---------------|--------------|-----------------|------------|
| UV (Nylon) | Fibrillenrisse, Oberflächenrisse | Verblassung, Sprödigkeit | 10–50 % | measured |
| UV (Polyester) | Oberflächenerosion | Leichte Verblassung | 5–25 % | measured |
| Schamfil | Faserbruch, abgeschliffene Oberfläche | Aufrauhung, Abflachung | 20–70 % | measured |
| Zyklische Ermüdung | Fibrillenbrüche im Kern | Keine äußerlichen Zeichen! | 20–60 % | measured |
| Chemische Degradation | Querschnittsreduktion, Quellung | Verfärbung, Weichheit | 10–80 % | documented |
| Frost (Nylon, nass) | Eisbildung zwischen Fibrillen | Steifigkeit, Risse | 15–30 % | documented |

### P2 — PVC-Fendermaterial — Alterungsverhalten

| Expositionsdauer (Mittelmeer) | UV-Index | Farbveränderung | Elastizitätsverlust | Confidence |
|------------------------------|----------|----------------|---------------------|------------|
| 0 Jahre (neu) | — | Keine | 0 % | measured |
| 2 Jahre | 6–10 | Leichte Verblassung | 5–10 % | documented |
| 4 Jahre | 6–10 | Deutliche Verblassung | 10–20 % | documented |
| 6 Jahre | 6–10 | Starke Verblassung, kreidig | 20–35 % | documented |
| 8 Jahre | 6–10 | Grau, spröde | 35–50 % | estimated |
| 10+ Jahre | 6–10 | Rissbildung wahrscheinlich | >50 % | estimated |

### P3 — Faservergleich — Detaildaten

| Eigenschaft | PA 6 (Nylon) | PA 6.6 (Nylon) | PET (Polyester) | HMPE (Dyneema SK78) | PP |
|-------------|-------------|---------------|----------------|--------------------|----|
| Zugfestigkeit (cN/dtex) | 6–8 | 7–9 | 5–7 | 30–40 | 4–6 |
| E-Modul (cN/dtex) | 30–40 | 35–50 | 80–120 | 800–1.200 | 30–50 |
| Bruchdehnung (%) | 15–25 | 15–22 | 10–15 | 3–4 | 15–25 |
| Dichte (g/cm³) | 1,14 | 1,14 | 1,38 | 0,97 | 0,91 |
| Wasseraufnahme (%) | 4–5 | 3–4 | <0,4 | 0 | 0 |
| Schmelzpunkt (°C) | 220 | 260 | 260 | 145 | 165 |

---

## ANHANG Q — Festmacher im Seenotfall

### Q1 — Notfestmacher bei Motorausfall

Wenn der Motor in Stegnähe ausfällt, können Festmacherleinen als Notfall-Sicherung verwendet werden:

1. **Leine an Bug-Klampe vorbereiten** (gespleißtes Auge über Klampe)
2. **Leine als Wurfleine verwenden** → Zum Steg werfen oder an Helfer übergeben
3. **Rundtörn um Steg-Poller** → Boot kontrolliert aufstoppen
4. **Fender ausbringen** (so viele wie möglich, schnell!)
5. **Brustleine als Bremse** → Leine um Poller führen und langsam fieren

### Q2 — Abschleppen mit Festmachern

Festmacherleinen können als Notfall-Schleppverbindung dienen:

- **Schleppgeschwindigkeit:** Max. 3–4 kn (niedrige Lasten)
- **Leine:** Längste verfügbare Nylon-Leine (Dehnung = Stoßdämpfung)
- **Befestigung:** An der stärksten Klampe (Bug-Klampe oder Ankerwinsch)
- **NIEMALS HMPE als Schleppleine** → Rückstoß bei Bruch kann tödlich sein ("snap-back")
- **Sicherheitsabstand:** Niemand im Bereich der gespannten Leine

### Q3 — Mann-über-Bord — Leine als Rettungsmittel

Eine Festmacherleine mit Auge kann als Rettungsleine für eine über Bord gegangene Person dienen:

1. Leine mit Auge als Schlaufe werfen
2. Person greift Auge und schlüpft unter die Arme
3. Person wird längsseits gezogen und über die niedrigste Stelle (Heck, Badeleiter) an Bord geholt

---

## ANHANG R — Zukunftstrends

### R1 — Smarte Festmacher (2025–2030)

Mehrere Unternehmen entwickeln sensorbasierte Festmachersysteme:

| Technologie | Funktion | Status (2026) | Potenzial | Confidence |
|-------------|---------|---------------|-----------|------------|
| Kraftsensor in Klampe | Misst Leinenbelastung in Echtzeit | Prototyp | Hoch | estimated |
| Dehnungsmessung in Leine | Integrierter Sensor in Leinenkern | Forschung | Mittel | estimated |
| App-Warnung | Benachrichtigung bei Überlast auf Smartphone | Prototyp (Dock Sense) | Hoch | documented |
| Automatische Winsch | Automatisches Nachgeben/Dichtholen bei Tide | Verfügbar (Superyachten) | Hoch | documented |
| Drohnen-Inspektion | Visuelle Prüfung per Drohne | Verfügbar | Mittel | documented |

### R2 — Nachhaltige Materialien

| Material | Beschreibung | Verfügbarkeit (2026) | Leistung vs. Standard | Confidence |
|----------|-------------|---------------------|----------------------|------------|
| Recyceltes PET-Tauwerk | Leinen aus recycelten PET-Flaschen | Marktreif (Teufelberger) | 90–95 % | documented |
| Bio-basiertes Nylon | Nylon aus erneuerbaren Rohstoffen | Pilotproduktion | 85–90 % | estimated |
| Recycelte PVC-Fender | Fender aus recyceltem PVC | Marktreif (Majoni) | 95 % | documented |
| Naturfaser-Compounds | Hanf/Flachs + Kunstharz-Hybrid | Forschung | 60–70 % | estimated |

### R3 — AYDI-Integration: Zukünftige Analysefähigkeiten

| Fähigkeit | Beschreibung | Geplant für |
|-----------|-------------|-------------|
| Automatische Leinendurchmesser-Erkennung | KI erkennt Durchmesser aus Foto | v2.0 |
| Fender-Zustandserkennung | KI erkennt Verformung, Risse, UV-Schäden | v2.0 |
| Leinenalter-Schätzung | KI schätzt Alter anhand von UV-Degradation | v2.5 |
| Klampen-Analyse | KI erkennt Klampentyp, -größe, -zustand | v2.5 |
| Automatische Dimensionierungs-Empfehlung | Vollautomatische Empfehlung basierend auf Bootsdaten | v1.5 |
| Berth Risk Assessment | Automatische Liegeplatz-Risikobewertung aus Wetterdaten | v3.0 |

---

## ANHANG S — Festmacher-Terminologie Deutsch-Englisch

### S1 — Übersetzungstabelle

| Deutsch | Englisch | Französisch | Anmerkung |
|---------|----------|------------|-----------|
| Festmacher | Mooring line / Dock line | Amarre | — |
| Vorleine | Bow line / Head line | Amarre d'étrave | — |
| Achterleine | Stern line | Amarre arrière | — |
| Vorspring | Forward spring | Spring avant | — |
| Achterspring | Aft spring | Spring arrière | — |
| Brustleine | Breast line | Travers | — |
| Muringleine | Mooring line / Lazy line | Pendille | Mittelmeer |
| Fender | Fender | Pare-battage / Défense | — |
| Fenderbrett | Fender board | Planche de défense | — |
| Klampe | Cleat | Taquet | — |
| Klüse | Fairlead / Chock | Chaumard | — |
| Poller | Bollard | Bitte | Am Steg |
| Ring | Ring / Mooring ring | Anneau d'amarrage | Am Steg |
| Spleißen | Splicing | Épisser | — |
| Schamfilen | Chafing | Ragage | — |
| Schamfilschutz | Chafe protection / Chafe guard | Protection anti-ragage | — |
| Kausche | Thimble | Cosse | Im Auge |
| Bruchlast | Breaking load | Charge de rupture | — |
| Dehnung | Stretch / Elongation | Allongement | — |
| Ruckbelastung | Surge loading / Shock loading | Charge de choc | — |
| Leine belegen | To make fast / To cleat | Tourner / Frapper | — |
| Leinen los | Cast off / Let go | Larguer les amarres | — |
| Festmachen | To moor / To make fast | Amarrer | — |
| Längsseits | Alongside | À couple | — |
| Päckchen | Raft / Rafting | À couple (plusieurs) | — |
| Heckanleger | Mediterranean moor / Med moor | Amarrage cul | — |
| Tide / Gezeiten | Tide | Marée | — |

### S2 — Hafenkommandos (Deutsch / Englisch)

| Situation | Deutsch | Englisch |
|-----------|---------|----------|
| Anweisung | "Vorleine zuerst!" | "Bow line first!" |
| Anweisung | "Springs belegen!" | "Make fast the springs!" |
| Warnung | "Fender tiefer hängen!" | "Lower the fenders!" |
| Warnung | "Ihre Leine rutscht!" | "Your line is slipping!" |
| Hilfe | "Können Sie meine Leine annehmen?" | "Can you take my line?" |
| Hilfe | "Bitte um den Poller legen!" | "Please put it around the bollard!" |
| Ablegen | "Alle Leinen los!" | "Cast off all lines!" |
| Ablegen | "Vorspring halten!" | "Hold the forward spring!" |

---

## ANHANG T — Checklisten und SOPs

### T1 — Checkliste: Festmacher-/Fender-Inventur (Saisonstart)

```
INVENTUR FESTMACHER UND FENDER — Saisonstart
=============================================
Datum: ___________
Boot: ___________
LOA: ___________

FESTMACHERLEINEN:
□ Vorleine 1:   Ø ___ mm × ___ m   Zustand: ___   Auge/Spleiß: ___
□ Vorleine 2:   Ø ___ mm × ___ m   Zustand: ___   Auge/Spleiß: ___
□ Achterleine 1: Ø ___ mm × ___ m   Zustand: ___   Auge/Spleiß: ___
□ Achterleine 2: Ø ___ mm × ___ m   Zustand: ___   Auge/Spleiß: ___
□ Vorspring:    Ø ___ mm × ___ m   Zustand: ___   Auge/Spleiß: ___
□ Achterspring: Ø ___ mm × ___ m   Zustand: ___   Auge/Spleiß: ___
□ Brustleine 1: Ø ___ mm × ___ m   Zustand: ___   Auge/Spleiß: ___
□ Brustleine 2: Ø ___ mm × ___ m   Zustand: ___   Auge/Spleiß: ___
□ Reserveleine 1: Ø ___ mm × ___ m  Zustand: ___   Auge/Spleiß: ___
□ Reserveleine 2: Ø ___ mm × ___ m  Zustand: ___   Auge/Spleiß: ___

FENDER:
□ Fender 1: Typ ___ Ø ___ mm × ___ mm   Zustand: ___   Druck: ___
□ Fender 2: Typ ___ Ø ___ mm × ___ mm   Zustand: ___   Druck: ___
□ Fender 3: Typ ___ Ø ___ mm × ___ mm   Zustand: ___   Druck: ___
□ Fender 4: Typ ___ Ø ___ mm × ___ mm   Zustand: ___   Druck: ___
□ Fender 5: Typ ___ Ø ___ mm × ___ mm   Zustand: ___   Druck: ___
□ Fender 6: Typ ___ Ø ___ mm × ___ mm   Zustand: ___   Druck: ___
□ Fender 7: Typ ___ Ø ___ mm × ___ mm   Zustand: ___   Druck: ___
□ Fender 8: Typ ___ Ø ___ mm × ___ mm   Zustand: ___   Druck: ___
□ Kugelfender 1: Ø ___ mm   Zustand: ___   Druck: ___
□ Kugelfender 2: Ø ___ mm   Zustand: ___   Druck: ___

ZUBEHÖR:
□ Fenderbrett 1: ___ mm × ___ mm   Zustand: ___
□ Fenderbrett 2: ___ mm × ___ mm   Zustand: ___
□ Fenderleinen: ___ Stück   Zustand: ___
□ Fenderhalter: ___ Stück   Zustand: ___
□ Schamfilschutz: ___ Stück   Zustand: ___
□ Kauschen: ___ Stück

BESCHLÄGE:
□ Klampe Bug BB:     Größe ___ mm   Zustand: ___   Befestigung: ___
□ Klampe Bug StB:    Größe ___ mm   Zustand: ___   Befestigung: ___
□ Klampe Mitte BB:   Größe ___ mm   Zustand: ___   Befestigung: ___
□ Klampe Mitte StB:  Größe ___ mm   Zustand: ___   Befestigung: ___
□ Klampe Heck BB:    Größe ___ mm   Zustand: ___   Befestigung: ___
□ Klampe Heck StB:   Größe ___ mm   Zustand: ___   Befestigung: ___
□ Klüsen:            Zustand: ___   Kanten glatt? ___

BEWERTUNG:
□ Alle Leinen dimensioniert für LOA?     [ja / nein → nachrüsten]
□ Alle Fender dimensioniert für LOA?     [ja / nein → nachrüsten]
□ Springs vorhanden?                     [ja / nein → DRINGEND nachrüsten]
□ Schamfilschutz vorhanden?              [ja / nein → nachrüsten]
□ Fenderbrett vorhanden?                 [ja / nein → empfohlen]
□ Ersatzleinen vorhanden?                [ja / nein → empfohlen]
```

### T2 — SOP: Anlegen Längsseits (Standard)

```
STANDARD OPERATING PROCEDURE — Anlegen Längsseits
==================================================

VORBEREITUNG (5 min vor Anlegen):
1. Fender ausbringen — Luvseite (= Stegseite)
   - Mindestens 4 Fender (6 bei >12 m Boot)
   - Höhe: Wasserpass des Rumpfes
   - Abstand: gleichmäßig über die Bootslänge
2. Festmacher vorbereiten
   - Vorleine: Auge über Bug-Klampe, Leine klar zum Übergeben
   - Achterleine: Auge über Heck-Klampe, Leine klar zum Übergeben
   - Springs: bereitgelegt (NICHT vergessen!)
3. Bootshaken bereithalten
4. Motor in Bereitschaft, Gang frei

ANLEGEN:
1. Boot parallel zum Steg bringen (Abstand 0,5–1 m)
2. Wind/Strom berücksichtigen:
   - Auflandiger Wind: VORSICHTIG! Fender checken!
   - Ablandiger Wind: Dicht an Steg, da Wind abdrückt
3. Vorleine übergeben oder an Poller legen
4. Achterleine übergeben oder belegen
5. Boot sanft an Steg heranholen
6. Vorspring belegen (Bug-Klampe → nach achtern zum Steg)
7. Achterspring belegen (Heck-Klampe → nach vorn zum Steg)
8. Brustleinen bei Bedarf (querab, NICHT zu straff!)
9. Alle Leinen auf korrekte Belegung prüfen
10. Schamfilschutz anbringen

NACHKONTROLLE (15 min nach Anlegen):
□ Fender-Position korrekt?
□ Leinen nicht zu straff / zu lose?
□ Schamfilschutz an Kontaktstellen?
□ Tide berücksichtigt? (genug Lose?)
□ Andere Boote behindert? (Schwojkreis bei Längslieger?)
```

### T3 — SOP: Heckanleger (Mittelmeer-Manier)

```
STANDARD OPERATING PROCEDURE — Heckanleger
==========================================

VORBEREITUNG:
1. Anker oder Muringleine vorbereiten (Bug)
2. Heckleinen vorbereiten (2 Achterleinen, je 1 an BB und StB Heck-Klampe)
3. Heckfender ausbringen (2 × Zylinder oder Langfender am Heck)
4. Seitliche Fender bereithalten (für Nachbarboote)
5. Kugelfender am Bug (Schutz gegen Nachbarboot-Anker)

ANLEGEN:
1. Position vor dem Liegeplatz ansteuern (1,5–2 × LOA Abstand zum Steg)
2. Boot mit dem Bug zum offenen Wasser drehen
3. Anker setzen ODER Muringleine aufnehmen
4. Langsam rückwärts zum Steg fahren
5. Ankerkette/Muringleine kontrolliert fieren
6. Heckleinen an Steg übergeben oder belegen
7. Boot auf Position bringen: Abstand zum Steg 50–80 cm
8. Ankerkette/Muringleine durchsetzen (Boot soll zwischen Anker und Steg hängen)
9. Heckleinen nachstellen (nicht zu straff — Boot muss pendeln können)
10. Gangway auslegen (wenn vorhanden)
11. Fender-Position kontrollieren

BESONDERE RISIKEN:
□ Nachbar-Anker überfahren → Tiefe prüfen, Position der Nachbar-Ketten beachten
□ Wind von querab → Boot driftet seitlich, Fender zum Nachbar ausbringen
□ Muringleine zu dünn → eigene Leine als Backup durchstecken
□ Heck zu nah am Steg → Ruder-/Propellerschaden bei Schwell!
```

### T4 — SOP: Sturmvorbereitung am Liegeplatz

```
STANDARD OPERATING PROCEDURE — Sturmvorbereitung
=================================================

BEI STURMWARNUNG (>48 h vorher):
1. Wetterbericht genau studieren (Windrichtung, Stärke, Dauer)
2. Liegeplatz-Exposition bewerten (Wind von wo? Schutz von wo?)
3. Ggf. Liegeplatz wechseln in geschützteren Hafen

VORBEREITUNG (>24 h vorher):
1. Alle Festmacher prüfen und ggf. ersetzen
2. Schamfilschutz an ALLEN Kontaktstellen anbringen
3. Zusätzliche Leinen vorbereiten (Verdoppelung)
4. Fender auf Maximum wechseln (1 Größe über Standard)
5. Fender verdoppeln (je 2 Fender übereinander oder nebeneinander)
6. Fenderbretter einsetzen
7. Bordnetz-Backup prüfen (Bilgenpumpe, Navigationslichter)

UNMITTELBARE VORBEREITUNG (>6 h vorher):
1. Alle 8+ Leinen ausbringen (Vor, Achter, Springs, Brust)
2. Jede Leine verdoppeln (2. Leine parallel)
3. Alle Leinen kontrolliert einstellen:
   - Springs: lang und flach (maximale Surge-Dämpfung)
   - Brustleinen: LOSE! (Boot muss pendeln können)
   - Vor-/Achterleinen: mit genug Lose für Pendelbewegung
4. Segel entfernen oder bombenfest sichern
5. Bimini/Sprayhood abbauen (Windangriffsfläche reduzieren!)
6. Dinghy an Deck oder an Land
7. Lose Gegenstände unter Deck oder sichern
8. Luken und Fenster schließen und sichern
9. Landstrom abstecken (Überspannung/Kurzschluss-Risiko)

WÄHREND DES STURMS:
□ Leinen alle 4–6 Stunden kontrollieren
□ Schamfilschutz-Position prüfen und ggf. versetzen
□ Fender-Position prüfen
□ Bilge prüfen (Leckage?)
□ Nachbarboote beobachten (treiben sie?)
□ Notfallplan bereithalten (Leinen kappen, Motor starten, auslaufen)

NACH DEM STURM:
□ Alle Leinen auf Schäden prüfen (Schamfil, Dehnung, Risse)
□ Fender auf Verformung prüfen
□ Klampen auf Verformung/Lockerung prüfen
□ Beschädigte Leinen SOFORT ersetzen (auch wenn äußerlich OK — innere Ermüdung!)
□ Schadensdokumentation für Versicherung (Fotos!)
```

### T5 — Checkliste: Saisonende — Festmacher und Fender einwintern

```
EINWINTERUNG — FESTMACHER UND FENDER
=====================================

FESTMACHERLEINEN:
□ Alle Leinen abnehmen und kennzeichnen (Position markieren)
□ In Süßwasser einweichen (2–4 Stunden, Salzkristalle lösen)
□ Mit klarem Wasser ausspülen
□ Vollständig trocknen lassen (NICHT in der Sonne — UV!)
□ Zustand dokumentieren (Fotos, Notizen)
□ Beschädigte Leinen markieren und für Ersatz vormerken
□ Locker aufschießen (nicht zu eng binden)
□ Trocken, dunkel und belüftet lagern
□ NICHT in Plastiktüten lagern (Schimmel!)

FENDER:
□ Mit Süßwasser und Schwamm reinigen
□ Algenansatz und Muschelkalk entfernen (milder Reiniger OK)
□ Druck leicht reduzieren (ca. 20 % ablassen, NICHT komplett entleeren)
□ Ventile auf Dichtigkeit prüfen
□ Fenderhaut auf Risse und UV-Schäden prüfen
□ Beschädigte Fender markieren und für Ersatz vormerken
□ Trocken und dunkel lagern (UV-Schutz!)
□ Nicht stapeln mit Gewicht drauf (Verformung!)

FENDERBRETTER:
□ Reinigen und trocknen
□ Holz: auf Risse und Absplitterungen prüfen, ggf. nachschleifen
□ GFK: auf Delamination prüfen
□ Aufhängungen prüfen (Schäkel, Leinen)

BESCHLÄGE:
□ Klampen reinigen und auf Korrosion prüfen
□ Befestigungsschrauben nachziehen
□ Klüsen reinigen und entgraten
□ Fenderhaken prüfen und ggf. ersetzen

ERSATZBESCHAFFUNG:
□ Fehlende oder beschädigte Teile auflisten
□ Im Winter bestellen (Preisvorteile, keine Eile)
□ Nächste Saison: alle Teile beim Aufrüsten parat
```

---

## ANHANG U — Erweiterte Produktvergleiche

### U1 — Direktvergleich: Nylon 3-karätiges Tauwerk (16 mm, 5 Hersteller)

| Eigenschaft | Liros Handy Elastic | Gleistein Dock | Marlow 3-Strand | NER 3-Strand | Robline Dockline | Confidence |
|-------------|--------------------|--------------|--------------------|-------------|-----------------|------------|
| Material | PA 6 | PA 6.6 | PA 6.6 | PA 6 | PA 6 | documented |
| Bruchlast (kN) | 31,0 | 33,0 | 32,0 | 31,0 | 30,0 | measured |
| Dehnung bei 30 % BL | 17 % | 16 % | 16 % | 18 % | 17 % | measured |
| Gewicht (g/m) | 148 | 152 | 150 | 146 | 145 | measured |
| UV-Stabilisierung | Standard | Standard | Premium | Standard | Standard | documented |
| Farben | weiß, blau, schwarz | weiß, navy | weiß, schwarz | weiß, gold | weiß, blau | documented |
| Preis/m (EUR) | 3,50 | 4,00 | 4,20 | 3,80 | 3,20 | documented |
| Vorgefertigt (10 m) | 48 EUR | 55 EUR | 58 EUR | 52 EUR | 42 EUR | documented |
| Verfügbarkeit (EU) | Sehr gut | Sehr gut | Gut | Mittel | Sehr gut | documented |
| Spleißbarkeit | Sehr gut | Sehr gut | Sehr gut | Sehr gut | Sehr gut | documented |

**AYDI-Empfehlung:** Liros Handy Elastic als Preis-Leistungs-Sieger. Gleistein Dock für höchste Bruchlast. Robline Dockline als Budget-Option.

### U2 — Direktvergleich: Doppelgeflecht Nylon (16 mm, 4 Hersteller)

| Eigenschaft | Liros Dock-Elastic | Gleistein Dockline | Marlow DB Nylon | NER C2 Dockline | Confidence |
|-------------|-------------------|--------------------|-----------------|-----------------|------------|
| Bruchlast (kN) | 35,0 | 36,0 | 37,0 | 38,0 | measured |
| Dehnung bei 30 % BL | 12 % | 11 % | 12 % | 11 % | measured |
| Gewicht (g/m) | 162 | 165 | 164 | 168 | measured |
| Geschmeidigkeit | Sehr gut | Gut | Sehr gut | Exzellent | documented |
| Preis/m (EUR) | 5,50 | 6,50 | 7,00 | 8,00 | documented |
| Vorgefertigt (10 m) | 68 EUR | 82 EUR | 88 EUR | 98 EUR | documented |

**AYDI-Empfehlung:** Liros Dock-Elastic als Preis-Leistungs-Sieger. NER C2 für Premium-Handling.

### U3 — Direktvergleich: Zylinderfender (250 mm Klasse, 4 Hersteller)

| Eigenschaft | Polyform F-4 | Dan-Fender DF 625 | Majoni Star 4 | Ocean HD 25 | Confidence |
|-------------|-------------|-------------------|---------------|-------------|------------|
| Durchmesser (mm) | 250 | 240 | 250 | 250 | measured |
| Länge (mm) | 855 | 855 | 855 | 855 | measured |
| Gewicht (kg) | 2,2 | 2,3 | 2,0 | 2,1 | measured |
| Wandstärke | Mittel | Hoch | Mittel-dünn | Mittel | documented |
| UV-Beständigkeit | Sehr gut | Exzellent | Gut | Gut | documented |
| Ventilqualität | Gut | Exzellent (Doppelventil) | Standard | Gut | documented |
| Farbbeständigkeit | Sehr gut (5+ Jahre) | Exzellent (7+ Jahre) | Gut (3–5 Jahre) | Gut (4–6 Jahre) | documented |
| Preis (EUR) | 75–90 | 80–95 | 55–68 | 65–80 | documented |
| Verfügbarkeit (EU) | Exzellent | Sehr gut | Sehr gut | Gut | documented |
| Garantie | 2 Jahre | 3 Jahre | 1 Jahr | 2 Jahre | documented |

**AYDI-Empfehlung:** Polyform F-4 als Allrounder. Dan-Fender DF 625 für maximale Langlebigkeit. Majoni Star 4 als Budget-Option.

### U4 — Upgrade-Empfehlungsmatrix

| Aktuell | Boot | Problem | Empfohlenes Upgrade | Kosten (ca.) | Priorität |
|---------|------|---------|---------------------|-------------|-----------|
| 12 mm Nylon, 4 Stk | 10 m SY | Nur Vor-/Achterleinen | + 2 Springs 14 mm × 10 m | 60 EUR | HOCH |
| 4× F-2 Fender | 12 m SY | Zu klein, Rumpfkontakt | 6× F-3 oder F-4 | 340–540 EUR | HOCH |
| Keine Schamfilschutz | 14 m SY | Leinen schamfilen an Klüsen | Schamfilschutz-Set | 45 EUR | MITTEL |
| Kein Fenderbrett | 10 m SY, Nordsee | Pfahl-Liegeplatz | 1 Fenderbrett + 2 F-3 | 180 EUR | HOCH |
| 14 mm Leinen | 14 m MY | Unterdimensioniert | 8× 20 mm × 14 m | 450 EUR | KRITISCH |
| PP-Festmacher | 8 m SY | Falsches Material! | 6× 12 mm Nylon | 120 EUR | KRITISCH |
| Schwarze Fender | 18 m MY (lackiert) | Rumpfmarkierungen | 8× Polyform F-5 weiß + Socken | 1.200 EUR | HOCH |

---

## ANHANG V — Spleißanleitung (Kurzfassung)

### V1 — Augenspleiß dreikarätiges Nylon (Schritt-für-Schritt)

**Werkzeug:** Spleiß-Fid (passend zum Durchmesser), Isolierband, Messer, Feuerzeug

**Schritte:**

```
1. VORBEREITUNG
   - Augengroß festlegen (ca. 15–20 cm Innendurchmesser für Festmacher)
   - Rückholstrecke markieren: 12 × Durchmesser + Augenlänge
   - Sicherungswicklung aus Isolierband am Markierungspunkt
   - Stränge auftrennen und Enden mit Band sichern

2. SPLEISSTECHNIK
   - Strang 1: unter dem nächsten Fremdstrang durchfädeln (gegen die Schlagrichtung)
   - Seil drehen (120°)
   - Strang 2: unter dem nächsten Fremdstrang durchfädeln
   - Seil drehen (120°)
   - Strang 3: unter dem letzten Fremdstrang durchfädeln

3. WIEDERHOLUNGEN
   - Minimum 5 volle Durchstiche (= 5 × alle 3 Stränge)
   - Für Festmacher: 6–7 Durchstiche empfohlen
   - Letzter Durchstich: halber Strang (Tapering)

4. ABSCHLUSS
   - Überstehende Enden auf 2 cm kürzen
   - Enden verschmelzen (Feuerzeug) — NICHT am PVC-Schamfilschutz!
   - Isolierband um den Spleiß wickeln (temporär, bis Spleiß sich setzt)
   - Spleiß unter Last setzen lassen (1× kräftig ziehen)

5. QUALITÄTSKONTROLLE
   - Spleiß gleichmäßig? (keine herausstehenden Stränge)
   - Auge symmetrisch? (nicht verdreht)
   - Kausche sitzt fest? (wenn eingesetzt)
   - Testbelastung: mindestens 50 % SWL (kurz, nicht halten)
```

**Hinweis:** Ein korrekt ausgeführter Augenspleiß hat 90–95 % der Bruchlast der Originalleine. Ein fehlerhaft ausgeführter Spleiß kann auf 50–70 % fallen! Im Zweifel: vorgefertigte Leinen mit Werksspleiß kaufen.

### V2 — Kausche einsetzen

```
KAUSCHE IM AUGENSPLEIIS EINSETZEN
==================================

1. Kauschengröße = Leinendurchmesser (Kausche muss exakt zum Ø passen)
2. Kausche VOR dem Spleißen in die Schlaufe einlegen
3. Auge eng um die Kausche formen (kein Spiel!)
4. Spleißen wie oben beschrieben
5. Nach dem Spleißen: Kausche sitzt fest, kann nicht herausfallen

Kauschenmaterial:
- Edelstahl 316L: Standard, langlebig, schwer
- UHMWPE (Dyneema-Kausche): leicht, kein Rost, teurer
- Nylon/PA: leicht, günstig, für Fenderleinen ausreichend
```

---

## ANHANG W — Versicherungsrelevante Hinweise

### W1 — Versicherungsanforderungen an Festmachersysteme

| Anforderung | Typische Klausel | AYDI-Relevanz | Confidence |
|-------------|-----------------|---------------|------------|
| Seetüchtige Ausrüstung | "Boot muss mit ausreichenden Festmachern ausgerüstet sein" | Dimensionierungsprüfung | documented |
| Sorgfaltspflicht | "Eigner muss bei Starkwind-Warnung zusätzliche Maßnahmen treffen" | Sturmvorbereitung-SOP | documented |
| Inspektionspflicht | "Regelmäßige Prüfung der Festmacherausrüstung" | Wartungsintervalle | documented |
| Haftung Dauerlieger | "Dauerlieger müssen Festmacher halbjährlich prüfen lassen" | Wartungsplan Dauerlieger | documented |
| Selbstbehalt-Reduktion | "Nachweis professioneller Festmacher kann Selbstbehalt reduzieren" | AYDI-Zertifikat potenziell nutzbar | estimated |

### W2 — Schadendokumentation für Versicherung

Bei Festmacher-/Fenderschäden sollte dokumentiert werden:

```
SCHADENSDOKUMENTATION
=====================
□ Datum und Uhrzeit des Schadensereignisses
□ Wetterbedingungen (Wind, Seegang, Tide)
□ Fotos: Festmacher (Bruchstelle, Zustand)
□ Fotos: Fender (Verformung, Position)
□ Fotos: Rumpfschaden (Übersicht + Detail)
□ Fotos: Klampen/Beschläge (Zustand, Befestigung)
□ Liegeplatz-Beschreibung (Stegtyp, Exposition)
□ Festmacher-Spezifikation (Material, Ø, Alter)
□ Fender-Spezifikation (Typ, Größe, Marke)
□ Zeugenaussagen (Marina-Personal, Nachbarlieger)
□ Wetterbericht-Ausdruck (amtliche Daten)
□ ggf. AYDI-Bewertung als unabhängige Analyse
```

### W3 — Haftung bei Päckchen-Schäden

Bei Schäden im Päckchen gelten besondere Haftungsregeln:

- **Innenliegendes Boot:** Haftet für eigene Fender und Festmacher
- **Außenliegendes Boot:** Haftet für ausreichende Sicherung nach außen
- **Marinabetreiber:** Haftet, wenn die Anweisung zum Päckchen erteilt wurde und die Bedingungen unsicher waren
- **AYDI-Empfehlung:** Vor dem Päckchen den Fender- und Festmacherzustand des Nachbarbootes visuell prüfen. Bei erkennbar unzureichender Ausstattung: Päckchen ablehnen oder eigene Fender zwischen die Boote hängen.

---

## ANHANG X — Energieabsorptions-Tabellen Fender

### X1 — Energieabsorption Polyform F-Serie (bei 60 % Kompression)

| Modell | Durchmesser (mm) | Energieabsorption (J) | Reaktionskraft (kN) | Für Verdrängung bis (kg) | Confidence |
|--------|------------------|-----------------------|--------------------|--------------------------|------------|
| F-1 | 150 | 25 | 3,2 | 3.000 | documented |
| F-2 | 200 | 55 | 5,5 | 6.000 | documented |
| F-3 | 220 | 80 | 7,0 | 8.000 | documented |
| F-4 | 250 | 120 | 9,5 | 12.000 | documented |
| F-5 | 290 | 190 | 13,0 | 18.000 | documented |
| F-6 | 340 | 310 | 18,5 | 28.000 | documented |
| F-7 | 375 | 420 | 23,0 | 38.000 | documented |
| F-8 | 400 | 520 | 27,0 | 48.000 | documented |
| F-10 | 450 | 740 | 35,0 | 70.000 | documented |
| F-11 | 500 | 1.010 | 44,0 | 95.000 | documented |
| F-13 | 570 | 1.500 | 58,0 | 140.000 | estimated |

### X2 — Energieabsorption Polyform A-Serie (Kugelfender, bei 60 % Kompression)

| Modell | Durchmesser (mm) | Energieabsorption (J) | Reaktionskraft (kN) | Für Verdrängung bis (kg) | Confidence |
|--------|------------------|-----------------------|--------------------|--------------------------|------------|
| A-0 | 210 | 20 | 3,0 | 2.500 | documented |
| A-1 | 295 | 55 | 5,8 | 5.500 | documented |
| A-2 | 390 | 130 | 10,5 | 12.000 | documented |
| A-3 | 460 | 220 | 15,0 | 20.000 | documented |
| A-4 | 550 | 380 | 22,0 | 35.000 | documented |
| A-5 | 710 | 820 | 40,0 | 75.000 | documented |
| A-6 | 850 | 1.400 | 60,0 | 130.000 | estimated |

### X3 — Mindest-Energieabsorption nach Verdrängung

| Verdrängung (kg) | Anlegeenergie bei 0,15 m/s (J) | Anlegeenergie bei 0,25 m/s (J) | Empf. Fender-Energie pro Stk (J) | Confidence |
|-------------------|-------------------------------|-------------------------------|-----------------------------------|------------|
| 3.000 | 32 | 89 | 35–50 | calculated |
| 5.000 | 54 | 148 | 55–80 | calculated |
| 8.000 | 86 | 237 | 90–130 | calculated |
| 10.000 | 107 | 296 | 110–160 | calculated |
| 15.000 | 161 | 445 | 170–250 | calculated |
| 20.000 | 214 | 593 | 220–320 | calculated |
| 30.000 | 321 | 890 | 330–480 | calculated |
| 50.000 | 536 | 1.483 | 550–800 | calculated |

Annahmen: C_m = 1,7; C_s = 0,9; C_c = 0,7; pro Fender = mindestens 1 Fender absorbiert die volle Energie.

---

## ANHANG Y — Spezialthemen

### Y1 — Festmacher für Katamarane

Katamarane haben besondere Anforderungen an Festmacher und Fender aufgrund ihrer Bauweise:

**Unterschiede zum Einrumpfer:**

| Aspekt | Einrumpfer | Katamaran | Auswirkung auf Festmacher |
|--------|-----------|-----------|--------------------------|
| Windangriffsfläche | Moderat | Hoch (+30–50 %) | Dickere Leinen erforderlich |
| Gewicht | Moderat | Leicht (für LOA) | Weniger Anlegeenergie |
| Breite | ~0,3 × LOA | ~0,5 × LOA | Breitere Fender-Verteilung |
| Freibord | Variabel | Niedrig (Rümpfe) + Hoch (Brücke) | 2 Fenderhöhen erforderlich |
| Klampen | 4–6 | 6–8 (2 pro Rumpf + Heck) | Mehr Befestigungspunkte |
| Schwojverhalten | Rundschwoj | Stärker pendelnd | Längere Springs erforderlich |

**Dimensionierungs-Korrekturfaktoren für Katamarane:**
- Leinendurchmesser: LOA + 6 mm (statt LOA + 4 mm) wegen Windangriffsfläche
- Fenderanzahl: LOA / 2 × 1,5 (aufgerundet) — je Rumpf Fender nötig
- Fendergröße: gleich wie Einrumpfer gleicher LOA
- Springs: mindestens 1,2 × LOA Länge (statt 1,0)

**Spezial-Fenderlösung für Katamarane:**
- Je 3 Fender pro Rumpf (innerer Fender oft nicht nötig, da Zwischenraum)
- Kugelfender zwischen den Rümpfen bei Päckchen oder engem Liegeplatz
- Bei Heckanleger: je 1 Fender pro Heckseite + Heckfender

### Y2 — Festmacher für Superyachten (25 m+)

Superyachten erfordern professionelle Festmachersysteme, die sich grundlegend von der Fahrtenyacht-Ausstattung unterscheiden:

**Materialkategorien:**

| Kategorie | Beschreibung | Durchmesserbereich | Material | Preis/m |
|-----------|-------------|-------------------|----------|---------|
| Standard | Werft-Ausstattung | 24–36 mm | Nylon DB | 8–15 EUR |
| Premium | Upgrade für Langlebigkeit | 24–40 mm | Polyester DB | 12–22 EUR |
| Racing | Minimales Gewicht | 16–28 mm | HMPE/Poly | 20–40 EUR |
| Superyacht | Höchste Qualität | 28–50 mm | Nylon oder HMPE | 15–50 EUR |

**Fender für Superyachten:**

| Typ | Einsatz | Vorteile | Nachteile | Preis (pro Stk) |
|-----|---------|---------|-----------|-----------------|
| Flachfender (EVA) | Permanent am Rumpf | Unsichtbar, permanent | Geringe Energieabsorption | 200–800 EUR |
| Pneumatisch | Anlegen/Ablegen | Höchste Absorption | Schwer, Wartung | 500–3.000 EUR |
| Zylinder (XL) | Universal | Bewährt, vielseitig | Optisch störend | 250–700 EUR |
| Fendersocke | Über Zylinder | Rumpfschutz (Lack) | Zusätzlicher Aufwand | 30–80 EUR |

**Crew-Anforderungen:**
- Professionelle Crew muss Festmacher-SOPs beherrschen
- Mindestens 2 Personen für Anlegemanöver >25 m
- Festmacher-Training ist Pflichtbestandteil der Crew-Ausbildung
- Captain trägt Gesamtverantwortung für Festmacher-Zustand

### Y3 — Festmacher in Extrembedingungen

#### Y3.1 Arktische Bedingungen (<0 °C)

| Problem | Auswirkung | Gegenmaßnahme | Confidence |
|---------|-----------|---------------|------------|
| Nylon wird steif | Handling erschwert, Bruchlast −10 % | Polyester-Leinen bevorzugen | documented |
| Nass gefroren | Bruchlast −25–30 % | Leinen trocken halten, nicht einfrieren lassen | documented |
| Eis auf Steg/Klampe | Leine rutscht | Zusätzliche Windungen, anti-slip Klüsen | documented |
| Eisgang | Fender werden zerstört | Fender einholen, Boot mit Leinen mittig halten | documented |

#### Y3.2 Tropische Bedingungen (>30 °C, UV-Index >10)

| Problem | Auswirkung | Gegenmaßnahme | Confidence |
|---------|-----------|---------------|------------|
| Extreme UV | Bruchlast −30–50 % in 12 Monaten | Polyester-Leinen, Schutzschläuche, Leinen abdecken | documented |
| Hitze auf PVC-Fender | Verfärbung, Abfärben auf Rumpf | Weiße Fender, Fendersocken verwenden | documented |
| Tropengewitter (Squalls) | Plötzlich 40+ kn aus wechselnden Richtungen | Überdimensionierung, alle Leinen dauerhaft ausbringen | documented |
| Biologischer Bewuchs | Leinen und Fender bewachsen | Regelmäßige Reinigung, anti-fouling-beschichtete Leinen | documented |

#### Y3.3 Tsunami-Gefahr (Pazifik, Indischer Ozean)

**AYDI-Hinweis:** Bei Tsunami-Warnung: Boot NICHT am Steg lassen. Auslaufen und auf offenes Wasser fahren (Wassertiefe >100 m). Kein Festmachersystem kann Tsunami-Kräfte aufnehmen. Wenn Auslaufen nicht möglich: alle Leinen lösen, Boot frei treiben lassen (Versicherung bevorzugt frei treibendes Boot gegenüber zerstörtem Boot + Steg).

### Y4 — Automatische Festmachersysteme

Für Superyachten und kommerzielle Fähren existieren automatische Festmachersysteme:

| System | Hersteller | Funktionsweise | Für Bootsgröße | Preis (ca.) | Confidence |
|--------|-----------|---------------|----------------|-------------|------------|
| MoorMaster | Cavotec | Vakuumsauger am Steg | 20 m+ (kommerziell) | 100.000+ EUR | documented |
| AutoMoor | Trelleborg | Automatische Poller | 20 m+ (kommerziell) | 50.000+ EUR | documented |
| DockSense | — | Sensorbasierte Winsch | 15 m+ (Yacht) | 10.000–25.000 EUR | estimated |
| Dock & Go | Volvo Penta | Automatisches Anlegen (IPS) | 10–20 m (MY) | In Entwicklung | estimated |

**AYDI-Bewertung automatischer Systeme:** Derzeit nur für Superyachten und kommerzielle Anwendungen relevant. Für Fahrtenyachten sind manuelle Festmacher auf absehbare Zeit der Standard. Die Integration automatischer Systeme in AYDI ist für v4.0+ geplant.

---

## ANHANG Z — Referenzen und Quellenverzeichnis

### Z1 — Primärquellen

| Quelle | Art | Verwendung in dieser Datei |
|--------|-----|---------------------------|
| ISO 15084:2003 | Norm | Anforderungen an Festmacherpunkte |
| ISO 1140:2012 | Norm | Nylon-Tauwerk-Spezifikation |
| ISO 1141:2012 | Norm | Polyester-Tauwerk-Spezifikation |
| ISO 10325:2009 | Norm | HMPE-Spezifikation |
| DIN EN ISO 2307 | Norm | Prüfverfahren für Faserseile |
| ABYC H-40 | Standard | US-Anforderungen an Festmacherpunkte |
| Liros Produktkatalog 2025/2026 | Katalog | Bruchlast, Preise, Spezifikationen |
| Gleistein Produktkatalog 2025 | Katalog | Bruchlast, Preise, Spezifikationen |
| Polyform Technische Daten 2025 | Datenblatt | Fendermaße, Energieabsorption |
| Dan-Fender Katalog 2025 | Katalog | Fendermaße, Preise |
| Marlow Ropes Technical Manual | Handbuch | Bruchlast, Dehnungswerte |
| Pantaenius Schadensstatistik 2019–2024 | Bericht | Schadensursachen und -häufigkeit |

### Z2 — Sekundärquellen

| Quelle | Art | Verwendung |
|--------|-----|-----------|
| Practical Sailor (diverse Ausgaben) | Zeitschrift | Produkttests, Vergleiche |
| YACHT Magazin (diverse Ausgaben) | Zeitschrift | Produkttests, Praxisberichte |
| Segeln Magazin (diverse Ausgaben) | Zeitschrift | Eigner-Erfahrungen |
| Nigel Calder: "Boatowner's Mechanical and Electrical Manual" | Buch | Festmacher-Grundlagen |
| Don Casey: "This Old Boat" | Buch | Praxisanleitungen Spleißen |
| Beth Leonard: "The Voyager's Handbook" | Buch | Blauwasser-Festmacher |
| Segeln-Forum.de (2020–2025) | Forum | Eigner-Erfahrungen, Produktbewertungen |
| Boote-Forum.de (2020–2025) | Forum | Eigner-Erfahrungen, Produktbewertungen |
| Cruisers Forum (2020–2025) | Forum | Internationale Erfahrungen |

### Z3 — AYDI-interne Referenzen

| Wissensdatei | Relation |
|-------------|----------|
| 13_01_anker_grundlagen.md | Ankersysteme (gleiche Klampen und Beschläge) |
| 13_02_ankerketten.md | Kettenmaterial und -dimensionierung |
| 13_03_ankerwinden.md | Winsch-Klampen-Interaktion |
| 11_01 – 11_05 | Klampen, Schienen, Reling (Befestigungspunkte) |
| 12_01 – 12_05 | Schäkel, Wirbel (Verbindungselemente) |

---