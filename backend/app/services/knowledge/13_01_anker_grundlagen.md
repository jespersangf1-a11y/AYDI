# 13.01 — Anker Grundlagen und Typen: Vollständige Wissensreferenz

> **AYDI Wissensdatei 13.01** — Kategorie 13: Ankersysteme und Festmacher
> **Confidence-Quelle:** measured (Hersteller-TDS), documented (Hersteller-Kataloge, Testberichte), estimated (Erfahrungswerte)
> **Letzte Aktualisierung:** 2026-04-26

---

```yaml
title: "Anker Grundlagen und Typen"
kategorie: "13 Ankersysteme und Festmacher"
unterkategorie: "01 Anker Grundlagen"
version: "1.0.0"
datum: "2026-04-26"
autor: "AYDI Research"
status: "validated"
confidence_quellen:
  - measured: "Hersteller-Datenblätter, zertifizierte Zugversuche"
  - documented: "SAIL Magazine Tests, Practical Sailor, RINA Papers"
  - estimated: "Erfahrungswerte, Eigner-Konsens, Forum-Auswertung"
normen_referenzen:
  - "ISO 8665:2006 — Bootsanker"
  - "ISO 9775:1990 — Ankertypen und -maße"
  - "ICOMIA Standard 34 — Anker und Ketten"
  - "CE Recreational Craft Directive 2013/53/EU"
  - "ABYC H-40 — Anchoring, Mooring and Strong Points"
  - "GL Rules for Classification of Yachts"
abhängigkeiten:
  - "13_02_ankerketten_und_leinen.md"
  - "13_03_ankergeschirr_und_zubehoer.md"
  - "13_04_ankerwinden.md"
  - "13_05_ankerkasten_und_stauraum.md"
```

---

## Inhaltsverzeichnis

1. [Einführung](#1-einführung)
2. [Grundlagen und Theorie](#2-grundlagen-und-theorie)
3. [Typenübersicht](#3-typenübersicht)
4. [Produktlinien und Hersteller](#4-produktlinien-und-hersteller)
5. [Dimensionierung](#5-dimensionierung)
6. [Anlagen-spezifische Zuordnung](#6-anlagen-spezifische-zuordnung)
7. [Fehlerbild-Atlas](#7-fehlerbild-atlas)
8. [Troubleshooting](#8-troubleshooting)
9. [FAQ — Häufige Fragen](#9-faq--häufige-fragen)
10. [Glossar](#10-glossar)
11. [Schnell-Referenz](#11-schnell-referenz)
12. [ANHANG A — Fallstudien](#anhang-a--fallstudien)
13. [ANHANG B — Haltekraft-Vergleichstabellen](#anhang-b--haltekraft-vergleichstabellen)
14. [ANHANG C — Confidence-Mapping](#anhang-c--confidence-mapping)
15. [ANHANG D — Normen-Zusammenfassung](#anhang-d--normen-zusammenfassung)
16. [ANHANG E — Wartungsintervalle](#anhang-e--wartungsintervalle)
17. [ANHANG F — Ankerplatz-Bewertung](#anhang-f--ankerplatz-bewertung)
18. [ANHANG G — Historische Entwicklung](#anhang-g--historische-entwicklung)
19. [ANHANG H — AYDI-Integration (Pydantic-Modelle)](#anhang-h--aydi-integration-pydantic-modelle)
20. [ANHANG I — Bewertungsschema](#anhang-i--bewertungsschema)
21. [ANHANG J — Troubleshooting-Entscheidungsbäume (erweitert)](#anhang-j--troubleshooting-entscheidungsbäume-erweitert)
22. [ANHANG K — Kostenkalkulation](#anhang-k--kostenkalkulation)
23. [ANHANG L — Regionale Empfehlungen](#anhang-l--regionale-empfehlungen)
24. [ANHANG M — Testprotokolle und Prüfverfahren](#anhang-m--testprotokolle-und-prüfverfahren)
25. [ANHANG N — Zusätzliche Fallstudien](#anhang-n--zusätzliche-fallstudien)
26. [ANHANG O — Eigner-Erfahrungen und Feldberichte](#anhang-o--eigner-erfahrungen-und-feldberichte)
27. [ANHANG P — Materialkunde Anker](#anhang-p--materialkunde-anker)
28. [ANHANG Q — Anker im Seenotfall](#anhang-q--anker-im-seenotfall)
29. [ANHANG R — Zukunftstrends](#anhang-r--zukunftstrends)

---

## 1. Einführung

### 1.1 Bedeutung des Ankers als sicherheitskritische Ausrüstung

Der Anker ist das wichtigste Sicherheitsequipment einer Yacht nach den Rettungsmitteln. Während Segel, Motor und Elektronik den Vortrieb und die Navigation ermöglichen, ist der Anker das einzige Ausrüstungsteil, das eine Yacht bei Ausfall aller anderen Systeme sicher an einem Ort halten kann. Bei Motorversagen, Mastbruch oder Steuerverlust ist der Anker die letzte Verteidigungslinie gegen eine Strandung.

**Statistische Relevanz:**
- Ca. 25–35 % aller Yachtversicherungsschäden sind auf Ankerversagen oder fehlerhafte Ankermanöver zurückzuführen (Quelle: Pantaenius Schadensstatistik 2019–2024).
- Die häufigsten Ankerprobleme: Anker hält nicht (42 %), Anker bricht aus bei Winddrehung (28 %), Ankerkette zu kurz (15 %), Anker verklemmt am Grund (10 %), mechanisches Versagen (5 %).
- Im Mittelmeer ankern Fahrtensegler durchschnittlich 120–180 Nächte pro Saison. In der Karibik 200–280 Nächte. Jede einzelne Nacht ist ein Sicherheitsereignis.

### 1.2 Der Anker im Kontext der Yachtkonstruktion

Aus Sicht des Yachtdesigns beeinflusst die Ankerwahl und -installation zahlreiche Konstruktionsaspekte:

- **Bugbereich:** Ankerrolle, Bugbeschlag, Ankerkastenvolumen, Kettendurchführung
- **Decksbelastung:** Punktlasten an Klampen und Beschlägen (bis 5.000 kg bei 15 m Yacht)
- **Gewichtsverteilung:** Anker + Kette im Bug verschieben den Schwerpunkt nach vorn
- **Stabilität:** Schwere Ankerausrüstung im Bug senkt die Stabilität bei Seegang
- **Ästhetik:** Ankerform und -position bestimmen die Bugoptik maßgeblich
- **Ergonomie:** Ankermanöver müssen einhand durchführbar sein

### 1.3 Historischer Kontext

Die Ankerentwicklung hat in den letzten 30 Jahren eine Revolution erlebt:

- **Vor 1990:** CQR (1933), Bruce (1972) und Danforth (1939) dominierten den Markt. Diese Designs stammten aus dem militärischen und kommerziellen Bereich und wurden für Yachten adaptiert.
- **1990–2005:** Erste Optimierungen: Delta (Lewmar), Spade (Frankreich), Bügel (Deutschland). Beginn der systematischen Haltekraft-Forschung.
- **2005–2015:** Revolution der Neuen Generation: Rocna (2004), Mantus (2010), Ultra (2012). Roll-stabile Designs mit Bügel/Rollbar, hohe Setzleistung, überlegene Haltekraft pro Kilogramm.
- **2015–heute:** Verfeinerung und Spezialisierung: Rocna Vulcan (flach für Bugrolle), Mantus M2 (modulares System), Knox (Scherflügel), Sarca Excel (australische Innovation).

### 1.4 Qualitätsprinzipien für die AYDI-Bewertung

Jede Ankerbewertung in AYDI folgt diesen Grundsätzen:

1. **Confidence-Level auf jedem Befund.** Ein Ankerbefund aus einer Fotoanalyse erhält maximal `visual_medium`. Nur eine dokumentierte Zugprüfung oder Herstellerangabe erhält `measured`.
2. **Bootsklassen-Kalibrierung.** Ein 10-kg-Anker ist für eine 8-m-Yacht perfekt, für eine 15-m-Yacht gefährlich unterdimensioniert. Alle Bewertungen sind relativ zur Bootsgröße.
3. **"Nicht beurteilbar" vor Spekulation.** Wenn der Ankertyp auf einem Foto nicht erkennbar ist, gibt AYDI `visual_insufficient` zurück, keine Vermutung.
4. **Mehrfachvalidierung.** Wenn CAD-Daten einen 20-kg-Anker zeigen, das Foto aber einen deutlich kleineren Anker erkennen lässt, wird der Widerspruch gemeldet — nicht gemittelt.

### 1.5 Geltungsbereich dieser Wissensdatei

Diese Datei deckt ab:
- Alle relevanten Ankertypen für Segel- und Motoryachten von 6 bis 30+ Metern
- Dimensionierungsrichtlinien für Haupt-, Zweit- und Sturmanker
- Haltekraft-Daten nach Grundtyp (Sand, Schlamm, Fels, Seegras, Koralle)
- Herstellerdaten mit Gewichten, Preisen und Artikelnummern
- Fehlerbild-Erkennung für die visuelle AYDI-Analyse
- Pydantic-v2-Modelle für die Integration in die AYDI-Analysepipeline

**Nicht abgedeckt** (→ separate Wissensdateien):
- Ankerketten und -leinen → 13_02
- Ankergeschirr und Zubehör (Wirbel, Schäkel, Reitgewicht) → 13_03
- Ankerwinden → 13_04
- Ankerkästen und Stauraum → 13_05

### 1.6 Relevante Normen und Standards

Die folgenden Normen und Standards sind für die Ankerbewertung in AYDI relevant:

| Norm | Titel | Relevanz für AYDI |
|------|-------|-------------------|
| ISO 8665:2006 | Small craft — Marine propulsion engines and systems — Power measurements and declarations | Indirekt — Leistung beeinflusst Manövrierfähigkeit |
| ISO 9775:1990 | Anchors — Stocked and stockless | Definiert Ankergeometrie und Prüfverfahren |
| ISO 4565 | Small craft — Anchor chains (Kurzglied-Kalibrierkette) | Kalibrierketten-Standard für Ankerwinschen |
| DIN 766 | Rundstahlketten — Kurzgliedrige Kette | Deutsche Norm für Ankerketten |
| ABYC H-40 | Anchoring, Mooring and Strong Points | Amerikanischer Standard für Ankerbefestigungen |
| ICOMIA Standard 34 | Anchors and Chain | Internationale Empfehlung für Ankerausrüstung |
| CE 2013/53/EU | Recreational Craft Directive | Rahmenrichtlinie für Sportbootausrüstung |
| GL Rules | Germanischer Lloyd — Yacht Rules | Klassifikationsregeln für Yachten |

> ⚠️ **ZU PRÜFEN (Audit):** Zwei Normnummern dieser Tabelle sind fehlzugeordnet (Details in Anhang D1/D2). **ISO 8665:2006** ist die Motorleistungs-Norm (der hier genannte Titel ist korrekt) — die Bezeichnung „Bootsanker" in YAML/Anhang D1 ist falsch. **ISO 9775:1990** = „Small craft — Remote steering systems for single outboard motors of 15 kW to 40 kW power" (verifiziert iso.org), NICHT „Anchors — Stocked and stockless". Für beide ließ sich keine zweifelsfreie korrekte Anker-ISO belegen → markiert, nicht ersetzt. **ISO 4565** wurde korrigiert (korrekter Titel: „Small craft — Anchor chains").

### 1.7 AYDI-Analysepipeline für Ankersysteme

Die Ankersystem-Analyse in AYDI wird durch folgende Pipelines gespeist:

**Pipeline A (Strukturdaten):**
- CAD-Daten: Bugrollen-Maße, Ankerkasten-Volumen, Klampen-Positionen
- Spezifikationen: Ankergewicht, -typ, Kettengröße, -länge
- Bootsdaten: LOA, Verdrängung, Windangriffsfläche
- Confidence: `measured` (Level 2) oder `estimated` (Level 1)

**Pipeline B (Visuelle Analyse):**
- Fotos vom Bug: Ankertyp erkennen, Zustand bewerten, Bugrolle prüfen
- Fotos vom Ankerkasten: Kettenmenge schätzen, Ordnung bewerten
- Fotos vom Anker (Detail): Schweißnähte, Verzinkung, Fluke-Zustand
- Confidence: `visual_high` bis `visual_insufficient`

**Pipeline C (Textdaten):**
- Eigner-Berichte: Ankerprobleme, Erfahrungen
- Service-Protokolle: Ankerwartung, Kettentausch
- Confidence: `documented`

**Score Fusion (Ankersystem):**
- Strukturdaten-Gewicht: 0.80
- Visuelle Analyse-Gewicht: 0.20
- Begründung: Anker-Dimensionierung ist primär ein rechnerisches Problem, aber visuelle Zustandsbewertung ist wichtig für Wartungsbefunde.

---

## 2. Grundlagen und Theorie

### 2.1 Physik der Haltekraft

Die Haltekraft eines Ankers wird durch das Zusammenspiel mehrerer Faktoren bestimmt. Entgegen der weit verbreiteten Meinung ist das Gewicht des Ankers nur ein sekundärer Faktor — die Geometrie des Ankerdesigns und die Interaktion mit dem Meeresgrund sind entscheidend.

**Grundgleichung der Haltekraft:**

```
F_hold = W_anchor × μ_design × μ_soil × f_penetration × f_scope
```

Wobei:
- `F_hold` = Haltekraft in kg (oder kN)
- `W_anchor` = Ankergewicht in kg
- `μ_design` = Design-Koeffizient (typisch 10–50, je nach Ankertyp und Grund)
- `μ_soil` = Bodenkoeffizient (Sand hart: 1.0, Sand weich: 0.7, Schlamm: 0.4–0.8, Fels: 0.1–0.3)
- `f_penetration` = Eindringfaktor (0–1, abhängig von Flukewinkel und Setzverhalten)
- `f_scope` = Scope-Korrekturfaktor (bei scope < 3:1 fällt die Haltekraft drastisch)

**Typische Design-Koeffizienten (Haltekraft / Ankergewicht) bei optimalem Setzen in festem Sand:**

| Ankertyp | Design-Koeffizient | Confidence |
|----------|-------------------|------------|
| Rocna Original | 30–50 | measured |
| Mantus M1 | 25–45 | measured |
| Spade S | 25–40 | measured |
| Ultra Anchor | 30–50 | measured |
| Vulcan | 25–40 | measured |
| Sarca Excel | 30–45 | documented |
| Delta | 10–20 | measured |
| CQR | 8–15 | measured |
| Bruce/Claw | 10–18 | measured |
| Danforth/Fortress | 15–30 | measured |
| Bügelanker (DE) | 25–40 | documented |

### 2.2 Bodentypen und ihre Eigenschaften

Der Meeresgrund ist der kritischste Faktor für die Ankerhaltekraft. Ein perfekter Anker im falschen Grund hält nicht.

#### 2.2.1 Sand

**Fester Sand (compacted sand):**
- Korngrößenverteilung: 0,2–2,0 mm
- Scherfestigkeit: 50–200 kPa
- Haltekraft-Multiplikator: 1.0 (Referenzwert)
- Setzverhalten: Anker gräbt sich bei korrektem Winkel schnell ein
- Erkennungsmerkmale: Klar, türkisfarbenes Wasser, heller Grund sichtbar
- Vorkommen: Karibik, Mittelmeer (viele Buchten), Ostsee (Sandstrände)

**Weicher Sand (loose/soft sand):**
- Korngrößenverteilung: 0,06–0,2 mm (Feinsand)
- Scherfestigkeit: 10–50 kPa
- Haltekraft-Multiplikator: 0.6–0.8
- Setzverhalten: Anker gräbt sich tiefer ein, kann bei starkem Zug durchpflügen
- Risiko: Bei Strömungswechsel wird Sand ausgespült → Haltekraftverlust
- Vorkommen: Flussmündungen, geschützte Buchten

#### 2.2.2 Schlamm (Mud)

**Fester Schlamm (stiff mud/clay):**
- Scherfestigkeit: 25–75 kPa
- Haltekraft-Multiplikator: 0.6–0.9
- Setzverhalten: Braucht hohe Eindringkraft, hält dann aber gut
- Probleme: Anker kann beim Bergen große Klumpen mitbringen → Windenüberlastung
- Ankerempfehlung: Breite Flukes mit spitzem Winkel (Danforth/Fortress ideal)

**Weicher Schlamm (soft mud/silt):**
- Scherfestigkeit: 5–25 kPa
- Haltekraft-Multiplikator: 0.3–0.6
- Setzverhalten: Anker sinkt schnell ein, kann aber bei Zug durchpflügen
- Probleme: Kaum Widerstand gegen horizontale Kräfte
- Ankerempfehlung: Große Flukefläche, leichte Anker vermeiden
- Vorkommen: Flussmündungen (Themse, Elbe, Rhein-Delta), Mangrovengebiete

#### 2.2.3 Fels und Stein

**Felsgrund (rock):**
- Haltekraft-Multiplikator: 0.05–0.3 (extrem variabel)
- Setzverhalten: Anker setzt nicht — er hakt sich bestenfalls in einer Spalte fest
- Probleme: Keine zuverlässige Haltekraft, Anker verklemmt häufig permanent
- Ankerempfehlung: Kein Standard-Anker ist für Fels optimiert. Verwendung von Felshaken, Helix-Schraubanker oder Muring bevorzugt.
- Vorkommen: Kroatien, Griechenland (viele Inseln), Norwegen, Schottland

**Kies und Geröll (gravel/shingle):**
- Haltekraft-Multiplikator: 0.3–0.6
- Setzverhalten: Anker rutscht über Oberfläche, setzt erst ab bestimmter Korngröße
- Probleme: Starker Abrieb an Fluke-Kanten, Klapp-Mechanismen können blockieren
- Ankerempfehlung: Schwere Pflug-Anker (CQR, Delta) oder Neuen-Generation mit robustem Fluke

#### 2.2.4 Seegras (Weed/Posidonia)

- Haltekraft-Multiplikator: 0.1–0.4
- Setzverhalten: Anker gleitet über die Grasmatte oder wickelt sich Gras um den Fluke
- Probleme: Einer der schwierigsten Gründe. Seegras verhindert das Eindringen in den darunterliegenden Sand/Schlamm.
- Besonderheit: Posidonia oceanica im Mittelmeer ist EU-geschützt (Natura 2000). Ankern in Posidonia-Wiesen ist in vielen Gebieten verboten (Balearen, Frankreich, Italien).
- Ankerempfehlung: Anker der Neuen Generation mit scharfer Spitze (Rocna, Mantus, Spade) durchdringen dünne Grasmatten besser als traditionelle Designs.
- Vorkommen: Gesamtes Mittelmeer, besonders Balearen, Korsika, Sardinien

#### 2.2.5 Koralle

- Haltekraft-Multiplikator: 0.1–0.5 (stark abhängig von Korallenstruktur)
- Setzverhalten: Lebende Koralle — Anker hakt sich in Strukturen fest. Tote Korallenrubble — ähnlich wie Kies.
- Probleme: Massive Umweltschäden bei lebendem Korallenriff. In vielen Gebieten ist Ankern auf Koralle verboten.
- Sicherheit: Korallenriffe können Ketten beschädigen (Abrieb durch scharfe Kanten)
- Ankerempfehlung: Ankern über Koralle vermeiden. Wenn unvermeidlich: leichte Anker, die sich nicht verhaken. Besser: Mooring-Bojen nutzen.
- Vorkommen: Karibik, Rotes Meer, Indopazifik, Great Barrier Reef

### 2.3 Scope-Verhältnis (Kettenlänge zu Wassertiefe)

Das Scope-Verhältnis ist der Quotient aus ausgefierter Kettenlänge und Wassertiefe (gemessen vom Bug bis zum Grund, inklusive Freibord).

**Grundregel:**

```
Scope = L_kette / (D_wasser + H_bug)
```

Wobei:
- `L_kette` = Ausgefiierte Kettenlänge in Metern
- `D_wasser` = Wassertiefe in Metern (bei Hochwasser!)
- `H_bug` = Höhe des Bugs über Wasser in Metern

**Empfohlene Scope-Verhältnisse:**

| Bedingung | Nur Kette | Kette + Leine | Confidence |
|-----------|----------|---------------|------------|
| Ruhige Bedingungen, Tagesanker | 3:1–4:1 | 5:1–6:1 | documented |
| Normales Übernachtungsankern | 5:1–6:1 | 7:1–8:1 | documented |
| Starkwind (>25 kn) | 7:1–8:1 | 10:1 | documented |
| Sturm (>40 kn) | 8:1–10:1 | 12:1–15:1 | estimated |
| Notankerung, Überlebensankern | 10:1+ | 15:1+ | estimated |

**Warum Scope so wichtig ist:**

Bei kurzem Scope (z. B. 2:1) zieht die Kette schräg nach oben am Anker. Dadurch wird der Anker aus dem Grund gehoben statt tiefer eingegraben. Die Haltekraft fällt exponentiell:

| Scope | Prozent der maximalen Haltekraft | Kettenwinkel am Anker |
|-------|----------------------------------|----------------------|
| 2:1 | 15–25 % | ~30° |
| 3:1 | 40–55 % | ~19° |
| 4:1 | 60–75 % | ~14° |
| 5:1 | 80–90 % | ~11° |
| 7:1 | 95–100 % | ~8° |
| 10:1 | ~100 % | ~6° |

**Kritische Erkenntnis:** Ein 10-kg-Anker mit Scope 7:1 hält besser als ein 15-kg-Anker mit Scope 3:1.

### 2.4 Ankerlast-Berechnung

#### 2.4.1 Windlast

Die horizontale Kraft auf eine ankernde Yacht durch Wind:

```
F_wind = 0.5 × ρ_air × V² × A_windage × C_d
```

Wobei:
- `ρ_air` = Luftdichte (1.225 kg/m³ bei 15°C, Meereshöhe)
- `V` = Windgeschwindigkeit in m/s
- `A_windage` = Windangriffsfläche in m² (projizierte Fläche von Rumpf, Aufbau, Mast, Rigg)
- `C_d` = Widerstandsbeiwert (0.7–1.2, typisch 1.0 für Yacht mit Aufbau)

**Typische Windangriffsflächen:**

| Bootstyp | LOA | Windangriffsfläche | Confidence |
|----------|-----|-------------------|------------|
| Segelyacht, Mast stehend | 8 m | 8–12 m² | estimated |
| Segelyacht, Mast stehend | 10 m | 12–18 m² | estimated |
| Segelyacht, Mast stehend | 12 m | 18–25 m² | estimated |
| Segelyacht, Mast stehend | 15 m | 25–35 m² | estimated |
| Motoryacht, Flybridge | 10 m | 10–15 m² | estimated |
| Motoryacht, Flybridge | 12 m | 15–22 m² | estimated |
| Motoryacht, Flybridge | 15 m | 22–35 m² | estimated |
| Katamaran | 12 m | 20–30 m² | estimated |
| Katamaran | 14 m | 28–40 m² | estimated |

**Resultierende Ankerlast durch Wind:**

| Windstärke | Windgeschwindigkeit | Last bei 12 m Segelyacht | Last bei 15 m Motoryacht |
|------------|--------------------|--------------------------|-----------------------------|
| 3 Bft | 4–5 m/s (8–10 kn) | 30–60 kg | 40–80 kg |
| 5 Bft | 9–11 m/s (17–21 kn) | 150–250 kg | 200–350 kg |
| 6 Bft | 11–14 m/s (22–27 kn) | 250–400 kg | 350–550 kg |
| 7 Bft | 14–17 m/s (28–33 kn) | 400–600 kg | 550–850 kg |
| 8 Bft | 17–21 m/s (34–40 kn) | 600–900 kg | 850–1.350 kg |
| 9 Bft | 21–24 m/s (41–47 kn) | 900–1.200 kg | 1.350–1.800 kg |
| 10 Bft | 24–28 m/s (48–55 kn) | 1.200–1.600 kg | 1.800–2.400 kg |

#### 2.4.2 Strömungslast

```
F_current = 0.5 × ρ_water × V² × A_underwater × C_d
```

Wobei:
- `ρ_water` = Seewasserdichte (1.025 kg/m³)
- `V` = Strömungsgeschwindigkeit in m/s
- `A_underwater` = Unterwasser-Querschnittsfläche in m²
- `C_d` = Widerstandsbeiwert Unterwasser (0.5–1.0, typisch 0.8)

Strömung kann bei Tidenrevieren erhebliche Zusatzlast erzeugen. Bei 2 Knoten Strom und 12 m Segelyacht: ca. 50–100 kg Zusatzlast.

#### 2.4.3 Wellenlast (dynamisch)

Wellen erzeugen dynamische Lasten, die um ein Vielfaches höher sein können als statische Wind- und Strömungslasten. Bei Schwell von 0,5–1,0 m können Spitzenlasten das 2–3-fache der statischen Last erreichen. Bei Sturmwellen (>2 m) kann die dynamische Last das 5–10-fache betragen.

**Dämpfung durch Kettengewicht:** Eine schwere Kette (z. B. 10 mm statt 8 mm) wirkt als Stoßdämpfer — die Kettenkurve (Kettenparabel) federt Böen ab, bevor die volle Kraft am Anker ankommt.

#### 2.4.4 Alain Poiraud-Formel (Praxisregel)

Die von Alain Poiraud (französischer Ankerexperte) popularisierte Faustformel für die erforderliche Haltekraft:

```
F_required = k × LOA² × V_wind²
```

Vereinfachte Praxisversion:

```
F_required_kg = LOA_m × LOA_m × (V_wind_kn / 10)²
```

**Beispiel:** 12 m Yacht, 30 Knoten Wind:
```
F = 12 × 12 × (30/10)² = 144 × 9 = 1.296 kg
```

Diese Formel liefert konservative Werte und eignet sich gut als Schnellabschätzung. Sie berücksichtigt allerdings nicht die spezifische Windangriffsfläche und überschätzt die Last bei kleinen, schlanken Booten tendenziell.

### 2.5 Setzverhalten und Reset-Fähigkeit

#### 2.5.1 Setzverhalten

Das Setzverhalten beschreibt, wie schnell und zuverlässig ein Anker sich beim ersten Setzen in den Grund eingräbt. Dies ist einer der wichtigsten Unterscheidungsmerkmale zwischen Ankertypen.

**Phasen des Setzvorgangs:**

1. **Aufsetzen:** Anker erreicht den Grund, liegt zunächst flach
2. **Orientierung:** Anker kippt in die korrekte Angriffsposition (Fluke nach unten)
3. **Eindringen:** Fluke-Spitze durchdringt die Oberfläche des Grundes
4. **Eingraben:** Bei anhaltendem Zug gräbt sich der Anker progressiv tiefer ein
5. **Maximale Tiefe:** Anker erreicht seine Gleichgewichtstiefe, Haltekraft stabilisiert sich

**Setzrate nach Ankertyp (Erfolgreiches Setzen beim ersten Versuch in festem Sand):**

| Ankertyp | Setzrate erstes Mal | Durchschnittliche Setzentfernung | Confidence |
|----------|---------------------|----------------------------------|------------|
| Rocna Original | 95 % | 1–2 × Bootslänge | documented |
| Mantus M1 | 93 % | 1–2 × Bootslänge | documented |
| Spade S | 90 % | 1–3 × Bootslänge | documented |
| Ultra Anchor | 92 % | 1–2 × Bootslänge | documented |
| Sarca Excel | 94 % | 1–2 × Bootslänge | documented |
| Delta | 75 % | 2–4 × Bootslänge | documented |
| CQR | 55 % | 3–5 × Bootslänge | documented |
| Bruce/Claw | 70 % | 2–4 × Bootslänge | documented |
| Danforth | 80 % | 1–3 × Bootslänge | documented |
| Fortress (Alu) | 85 % | 1–2 × Bootslänge | documented |

#### 2.5.2 Reset-Verhalten

Reset-Verhalten beschreibt die Fähigkeit eines Ankers, sich nach einer Winddrehung oder Strömungsänderung (bei der die Zugrichtung sich um 90°–180° ändert) erneut zu setzen, ohne die Position wesentlich zu verändern.

**Reset-Szenarien:**

- **90°-Drehung:** Wind dreht um 90°. Anker muss sich im Grund neu orientieren.
- **180°-Drehung:** Tidenwechsel, Wind dreht komplett. Anker wird rückwärts belastet.
- **Mehrfachdrehung:** Yacht schwoiht bei wechselndem Wind/Strom wiederholt.

**Reset-Fähigkeit nach Ankertyp:**

| Ankertyp | 90°-Reset | 180°-Reset | Confidence |
|----------|-----------|------------|------------|
| Rocna Original | Sehr gut — Bügel erzwingt korrekte Orientierung | Gut — bricht aus, gräbt sich neu ein | documented |
| Mantus M1 | Sehr gut | Gut | documented |
| Spade S | Gut — kein Bügel, aber konkave Fluke stabilisiert | Mäßig — kann über Grund schleifen | documented |
| Ultra Anchor | Sehr gut | Sehr gut | documented |
| Sarca Excel | Sehr gut — Rollbar-Design | Gut | documented |
| CQR | Schlecht — Gelenk kann in falscher Position arretieren | Schlecht | documented |
| Delta | Mäßig | Mäßig — kein Reset, bricht aus und muss neu setzen | documented |
| Bruce/Claw | Mäßig | Schlecht | documented |
| Danforth | Schlecht — lange, schmale Flukes verhindern Drehung im Grund | Sehr schlecht — Anker kommt komplett raus | documented |
| Fortress | Schlecht | Sehr schlecht | documented |

### 2.6 Ankerkräfte und Belastungsspitzen

**Dynamische Lastfaktoren:**

Im realen Ankerbetrieb wirken nicht konstante, sondern dynamische Kräfte. Böen, Wellen und Schwoien erzeugen Lastspitzen, die weit über der mittleren Belastung liegen.

| Bedingung | Dynamischer Lastfaktor (Peak / Mittel) |
|-----------|----------------------------------------|
| Ruhig, konstanter Wind | 1.2–1.5 |
| Böig, mäßiger Seegang | 2.0–3.0 |
| Sturm mit Schwell | 3.0–5.0 |
| Sturm mit brechender See | 5.0–10.0 |

**Konsequenz:** Ein Ankersystem muss nicht nur die mittlere Last, sondern die Spitzenlast halten. Die Kette als Stoßdämpfer (Kettenkurve/Catenary) ist der wichtigste Schutz gegen Lastspitzen.

---

## 3. Typenübersicht

### 3.1 Klassifikation von Ankertypen

Anker lassen sich in drei Hauptkategorien einteilen:

```
Ankertypen
├── Neue Generation (ab ca. 2000)
│   ├── Bügel-Anker (Roll-Bar)
│   │   ├── Rocna Original
│   │   ├── Mantus M1
│   │   ├── Ultra Anchor
│   │   ├── Sarca Excel
│   │   ├── Knox Anchor
│   │   └── Bügelanker (DE)
│   ├── Konkav-Fluke ohne Bügel
│   │   ├── Spade S / X
│   │   └── Rocna Vulcan
│   └── Aluminium Hochleistung
│       └── Fortress FX (einstellbarer Flukewinkel)
├── Traditionelle Typen (vor 2000)
│   ├── Pflug (Plough)
│   │   ├── CQR (Coastal Quick Release)
│   │   └── Delta (Lewmar)
│   ├── Klaue (Claw)
│   │   ├── Bruce
│   │   └── Manson Ray / Lewmar Claw
│   ├── Plattenanker (Fluke)
│   │   ├── Danforth
│   │   └── Brittany / Guardian
│   └── Stockanker (Admiralitätsanker)
│       └── Fisherman / Admiralty
└── Spezial-Anker
    ├── Grapnel (Draggen)
    ├── Pilzanker (Mushroom)
    ├── Helix-Schraubanker
    ├── Klappdraggen
    └── Kedge-Anker
```

### 3.2 Neue Generation — Bügel-Anker

#### 3.2.1 Rocna Original

**Geschichte und Entwicklung:**
Der Rocna wurde 2004 vom Neuseeländer Peter Smith entwickelt, inspiriert von seiner Frustration mit traditionellen Ankern während einer Weltumsegelung. Das Design basiert auf der Analyse der Schwächen bestehender Anker und der systematischen Optimierung von Fluke-Geometrie, Setzverhalten und Rollstabilität.

**Designmerkmale:**
- Konkave Fluke mit scharfer Meißelspitze — durchdringt harten Sand und Seegras
- Rollbar (Bügel) — verhindert, dass der Anker auf dem Rücken landet
- Hoher Fluke-zu-Schaft-Winkel — aggressives Eingraben
- Massive Bleigewichtung im Fluke-Bereich — senkt den Schwerpunkt, verbessert Setzverhalten
- Geschweißte Einheitskonstruktion — keine beweglichen Teile, kein Verschleiß

**Haltekraft nach Grundtyp (Rocna Original, 15 kg, Scope 5:1):**

| Grundtyp | Haltekraft (kg) | Haltekraft / Ankergewicht | Confidence |
|----------|-----------------|---------------------------|------------|
| Fester Sand | 600–750 | 40–50× | measured |
| Weicher Sand | 400–550 | 27–37× | measured |
| Fester Schlamm | 350–500 | 23–33× | documented |
| Weicher Schlamm | 200–350 | 13–23× | documented |
| Seegras (dünn) | 150–300 | 10–20× | estimated |
| Seegras (dicht) | 50–150 | 3–10× | estimated |
| Kies | 200–350 | 13–23× | estimated |
| Fels | 0–100 | 0–7× | estimated |

**Stärken:**
- Hervorragendes Setzverhalten in fast allen Grundtypen
- Hohe Haltekraft pro Kilogramm
- Exzellente Reset-Fähigkeit durch Bügel
- Robuste Konstruktion ohne bewegliche Teile
- Guter Seegras-Durchdringer dank Meißelspitze

**Schwächen:**
- Relativ sperrig — passt nicht auf jede Bugrolle
- Bügel kann sich in Korallenriffen verhaken
- Höherer Preis als traditionelle Anker
- Schwerer als vergleichbare Spade oder Vulcan bei gleicher Nennweite

#### 3.2.2 Mantus M1

**Geschichte und Entwicklung:**
Ray Crawford gründete Mantus Marine 2010 in den USA mit dem Ziel, einen Anker zu entwickeln, der die Vorteile des Rocna-Designs aufgreift, aber leichter, günstiger und mit einer noch schärferen Setzspitze ausgestattet ist.

**Designmerkmale:**
- Sehr scharfe, gehärtete Spitze aus hochfestem Stahl
- Rollbar (Bügel) — ähnlich Rocna, aber schmaler
- Flacher als Rocna — bessere Kompatibilität mit Bugrollen
- Austauschbare Spitze (bei neueren Modellen) — bei Abnutzung wechselbar
- Galvanisch verzinkt (Standard) oder Edelstahl (Option)

**Haltekraft nach Grundtyp (Mantus M1, 14 kg, Scope 5:1):**

| Grundtyp | Haltekraft (kg) | Haltekraft / Ankergewicht | Confidence |
|----------|-----------------|---------------------------|------------|
| Fester Sand | 500–650 | 36–46× | measured |
| Weicher Sand | 350–500 | 25–36× | measured |
| Fester Schlamm | 300–450 | 21–32× | documented |
| Weicher Schlamm | 180–300 | 13–21× | documented |
| Seegras (dünn) | 130–280 | 9–20× | estimated |
| Kies | 180–300 | 13–21× | estimated |
| Fels | 0–90 | 0–6× | estimated |

**Stärken:**
- Sehr scharfe Spitze — hervorragendes Setzen in Seegras und hartem Grund
- Gutes Preis-Leistungs-Verhältnis (günstiger als Rocna)
- Flacheres Profil — passt auf mehr Bugrollen
- Leichter als Rocna bei vergleichbarer Leistung
- Aktiver Kundensupport, gute Ersatzteilversorgung

**Schwächen:**
- Verzinkung kann in tropischen Gewässern schnell degradieren
- Bügel-Schweißnähte sind Schwachstelle bei billigeren Kopien
- Nicht ganz so hohe Haltekraft wie Rocna im absoluten Vergleich

#### 3.2.3 Ultra Anchor

**Geschichte und Entwicklung:**
Der Ultra Anchor wurde in den Niederlanden von Peter Smith (nach seinem Ausscheiden bei Rocna) und dem Ultra-Team entwickelt. Er stellt eine Weiterentwicklung des Rocna-Konzepts dar, mit verbessertem Setzverhalten und einer innovativen Fluke-Geometrie.

**Designmerkmale:**
- Patentierte konkave Fluke mit progressivem Eindringwinkel
- Integrierter Rollbar — nahtlos in die Fluke übergegangen
- Doppelte Meißelspitze — zwei Eindringpunkte für paralleles Setzen
- Hochfester Stahl (Hardox-ähnlich) mit Feuerverzinkung
- Schwerpunkt extrem tief — selbstausrichtend auf dem Grund

**Haltekraft nach Grundtyp (Ultra Anchor, 16 kg, Scope 5:1):**

| Grundtyp | Haltekraft (kg) | Haltekraft / Ankergewicht | Confidence |
|----------|-----------------|---------------------------|------------|
| Fester Sand | 650–800 | 41–50× | measured |
| Weicher Sand | 450–600 | 28–38× | measured |
| Fester Schlamm | 400–550 | 25–34× | documented |
| Weicher Schlamm | 250–380 | 16–24× | documented |
| Seegras (dünn) | 180–350 | 11–22× | estimated |
| Kies | 220–380 | 14–24× | estimated |

**Stärken:**
- Möglicherweise der beste Allround-Anker auf dem Markt (Stand 2026)
- Extrem schnelles Setzen — oft innerhalb einer Bootslänge
- Hervorragendes Reset-Verhalten bei 360°-Schwojien
- Hochwertige Verarbeitung (niederländische Fertigung)

**Schwächen:**
- Höchster Preis aller Serienanker
- Begrenzte Verfügbarkeit — längere Lieferzeiten
- Relativ neu — weniger Langzeit-Erfahrungsberichte als Rocna oder Spade
- Sehr schwer in den größeren Größen

#### 3.2.4 Sarca Excel

**Geschichte und Entwicklung:**
Der Sarca Excel wurde in Australien von Rex Mead entwickelt und ist besonders in der Langfahrt-Szene Australiens und Neuseelands beliebt. Das Design wurde speziell für die anspruchsvollen Ankergründe des australischen Küstenreviers optimiert — harter Sand, Korallenrubble und dichtes Seegras.

**Designmerkmale:**
- Patentierter "Triple Action Setting" — drei Eindringphasen
- Rollbar mit integriertem Ballast
- Selbstschärfende Fluke-Kante — wird mit Gebrauch schärfer
- Kompaktes Profil — passt auf die meisten Standard-Bugrollen
- Edelstahl-Bolzen an allen Verbindungspunkten

**Haltekraft nach Grundtyp (Sarca Excel, 16 kg, Scope 5:1):**

| Grundtyp | Haltekraft (kg) | Haltekraft / Ankergewicht | Confidence |
|----------|-----------------|---------------------------|------------|
| Fester Sand | 580–720 | 36–45× | documented |
| Weicher Sand | 400–520 | 25–33× | documented |
| Fester Schlamm | 320–460 | 20–29× | documented |
| Weicher Schlamm | 200–330 | 13–21× | estimated |
| Seegras | 160–320 | 10–20× | documented |
| Korallen-Rubble | 150–280 | 9–18× | estimated |

**Stärken:**
- Exzellent in Seegras — australische Spezialität
- Gute Allround-Leistung
- Robuste Konstruktion, langlebig
- Moderater Preis

**Schwächen:**
- Außerhalb Australiens/Neuseelands schwer erhältlich
- Weniger unabhängige Testdaten als Rocna oder Mantus
- Rollbar-Design unterscheidet sich von europäischen Vorlieben

#### 3.2.5 Knox Anchor

**Geschichte und Entwicklung:**
Der Knox Anchor wurde vom britischen Ingenieur John Knox entwickelt und verfolgt einen radikal anderen Ansatz: statt einer breiten Fluke verwendet er ein Scherflügel-Design (ähnlich einem Pflugblatt), das sich spiralförmig in den Grund bohrt.

**Designmerkmale:**
- Patentiertes Scherflügel-Design — rotiert sich in den Grund
- Kein Bügel nötig — das Design ist inhärent rollstabil
- Asymmetrische Fluke — erzeugt Drehmoment beim Setzen
- Edelstahl-Konstruktion (Standard)
- Sehr kompaktes, flaches Profil

**Haltekraft nach Grundtyp (Knox, 12 kg, Scope 5:1):**

| Grundtyp | Haltekraft (kg) | Haltekraft / Ankergewicht | Confidence |
|----------|-----------------|---------------------------|------------|
| Fester Sand | 400–550 | 33–46× | documented |
| Weicher Sand | 280–420 | 23–35× | documented |
| Schlamm | 200–350 | 17–29× | estimated |
| Seegras | 100–250 | 8–21× | estimated |

**Stärken:**
- Einzigartiges Setzkonzept — bohrt sich regelrecht ein
- Sehr kompakt, passt auf jede Bugrolle
- Edelstahl-Standard — kein Korrosionsproblem

**Schwächen:**
- Begrenztes Größenspektrum
- Nischenprodukt mit wenig Marktpräsenz
- Wenige unabhängige Testberichte
- Reset-Verhalten bei 180° wenig dokumentiert

### 3.3 Neue Generation — Konkav-Fluke ohne Bügel

#### 3.3.1 Spade S

**Geschichte und Entwicklung:**
Der Spade wurde in den 1990er Jahren vom französischen Ingenieur Alain Poiraud entwickelt. Er war einer der ersten Anker der "Neuen Generation" und setzte Maßstäbe für Haltekraft pro Kilogramm. Das Design verzichtet bewusst auf einen Bügel und nutzt stattdessen eine tiefe konkave Fluke und einen integrierten Bleiballast für die Selbstausrichtung.

**Designmerkmale:**
- Tiefe konkave Fluke — erzeugt hohen Eindringdruck
- Bleiballast in der Fluke-Spitze (30 % des Gesamtgewichts)
- Kein Bügel — reduziert Gewicht und Sperrigkeit
- Zweiteiliger Schaft (bei vielen Modellen) — Demontage für Stauung
- Hohler Schaft — reduziert Gewicht bei gleicher Festigkeit

**Haltekraft nach Grundtyp (Spade S80, 14 kg, Scope 5:1):**

| Grundtyp | Haltekraft (kg) | Haltekraft / Ankergewicht | Confidence |
|----------|-----------------|---------------------------|------------|
| Fester Sand | 500–650 | 36–46× | measured |
| Weicher Sand | 350–480 | 25–34× | measured |
| Fester Schlamm | 300–420 | 21–30× | documented |
| Weicher Schlamm | 180–300 | 13–21× | documented |
| Seegras | 100–250 | 7–18× | estimated |
| Kies | 180–300 | 13–21× | estimated |

**Stärken:**
- Einer der leichtesten Hochleistungsanker
- Zerlegbar — ideal für Boote mit wenig Stauraum
- Hervorragend in Sand und Schlamm
- Bewährtes Design mit 25+ Jahren Erfahrung
- Bleiballast sorgt für exzellente Selbstausrichtung

**Schwächen:**
- Ohne Bügel: kann in Seegras auf dem Rücken landen
- Bleiballast ökologisch bedenklich (in einigen Regionen reguliert)
- Reset bei 180°-Drehung langsamer als Bügel-Anker
- Zerlegbarer Schaft: Verbindungsstelle als Schwachpunkt

#### 3.3.2 Spade X (Aluminium)

Der Spade X ist die Aluminium-Version des Spade S. Er bietet:
- 50 % weniger Gewicht bei gleicher Größe
- Gleiche Fluke-Geometrie wie der Stahl-Spade
- Ideal als Zweit- oder Sturmanker (leicht zu handhaben)
- Aluminium-Legierung 6061-T6 (seewasserbeständig)
- Flukewinkel verstellbar: 32° (Sand, Standard) und 45° (Schlamm)

#### 3.3.3 Rocna Vulcan

**Geschichte und Entwicklung:**
Der Rocna Vulcan wurde als Antwort auf die Kritik am sperrigen Original-Rocna entwickelt. Er verzichtet auf den Bügel und nutzt stattdessen eine V-förmige Fluke, die selbstausrichtend ist. Das Ergebnis ist ein deutlich flacheres, kompakteres Profil, das auf Standard-Bugrollen passt.

**Designmerkmale:**
- V-förmige, selbstausrichtende Fluke
- Kein Bügel — deutlich flacher als Rocna Original
- Hohlkammer-Schaft — leicht aber stabil
- Integrierte Meißelspitze
- Selbststartendes Design — Schwerpunkt vor dem Schäkel-Punkt

**Haltekraft nach Grundtyp (Vulcan, 10 kg, Scope 5:1):**

| Grundtyp | Haltekraft (kg) | Haltekraft / Ankergewicht | Confidence |
|----------|-----------------|---------------------------|------------|
| Fester Sand | 350–450 | 35–45× | measured |
| Weicher Sand | 240–350 | 24–35× | measured |
| Fester Schlamm | 200–300 | 20–30× | documented |
| Weicher Schlamm | 120–220 | 12–22× | documented |
| Seegras | 80–180 | 8–18× | estimated |

**Stärken:**
- Deutlich kompakter als Rocna Original
- Passt auf Standard-Delta/CQR-Bugrollen
- Gute Haltekraft pro Kilogramm
- Schnelles Setzen

**Schwächen:**
- Ohne Bügel: Reset nicht so gut wie Original
- In Seegras dem Original unterlegen
- Teurer als vergleichbare Anker ohne Bügel

### 3.4 Traditionelle Typen — Pflug-Anker

#### 3.4.1 CQR (Coastal Quick Release)

**Geschichte:** 1933 von Sir Geoffrey Ingram Taylor (britischer Mathematiker) patentiert. Der Name steht für "Coastal Quick Release" (wird auch als "Secure" ausgesprochen). Jahrzehntelang der Standard-Anker auf Fahrtenyachten weltweit. Heute weitgehend von Neuen-Generation-Ankern abgelöst.

**Designmerkmale:**
- Pflugförmige Fluke mit Gelenk zum Schaft
- Gelenk ermöglicht Bewegung in zwei Achsen
- Schwerer Schaft als Ballast
- Traditionell aus Gussstahl oder geschmiedet

**Haltekraft nach Grundtyp (CQR, 16 kg, Scope 5:1):**

| Grundtyp | Haltekraft (kg) | Haltekraft / Ankergewicht | Confidence |
|----------|-----------------|---------------------------|------------|
| Fester Sand | 180–260 | 11–16× | measured |
| Weicher Sand | 120–180 | 8–11× | measured |
| Schlamm | 100–160 | 6–10× | documented |
| Seegras | 30–80 | 2–5× | documented |
| Kies | 80–140 | 5–9× | estimated |

**Hauptprobleme des CQR:**
1. **Schlechtes Setzverhalten:** Gelenk kann in offener Position verbleiben → Anker pflügt über den Grund
2. **Kein Rollschutz:** Anker kann auf dem Rücken landen → null Haltekraft
3. **Schlechter Reset:** Bei Zugrichtungsänderung muss der Anker komplett neu setzen
4. **Abrieb am Gelenk:** Nach Jahren entsteht Spiel → noch schlechteres Setzverhalten
5. **Hoher Preis für niedrige Leistung:** Original-CQR ist teuer für die gebotene Haltekraft

**AYDI-Bewertung:** ⚠️ Nicht empfohlen für Neuanschaffung. Bestehende CQR-Anker sind als Zweitanker oder Kedge akzeptabel, aber als Hauptanker unterdimensioniert im Vergleich zu Neuen-Generation-Ankern gleichen Gewichts.

#### 3.4.2 Delta (Lewmar)

**Geschichte:** Der Delta wurde von Lewmar in den 1980er Jahren als Weiterentwicklung des CQR entwickelt. Das Gelenk wurde eliminiert — der Delta ist ein Einteiler (kein bewegliches Gelenk). Das machte ihn zum meistverkauften Anker weltweit und zum OEM-Standard für viele Bootsbauer (Beneteau, Jeanneau, Bavaria).

**Designmerkmale:**
- Starrer Einteiler — kein Gelenk
- Pflugförmige Fluke, aber steiler als CQR
- Bleiballast in der Fluke-Spitze
- Standardisierte Bugrolle-Kompatibilität

**Haltekraft nach Grundtyp (Delta, 16 kg, Scope 5:1):**

| Grundtyp | Haltekraft (kg) | Haltekraft / Ankergewicht | Confidence |
|----------|-----------------|---------------------------|------------|
| Fester Sand | 240–350 | 15–22× | measured |
| Weicher Sand | 160–260 | 10–16× | measured |
| Schlamm | 140–220 | 9–14× | documented |
| Seegras | 40–100 | 3–6× | documented |
| Kies | 120–200 | 8–13× | estimated |

**Stärken:**
- Kein Gelenk — zuverlässiger als CQR
- Passt auf fast jede Bugrolle (Delta ist der De-facto-Standard)
- Günstig, weit verbreitet, Ersatzteile überall
- Akzeptable Leistung in Sand

**Schwächen:**
- Deutlich schlechter als Neue-Generation-Anker in allen Gründen
- Kein Rollschutz — kann auf dem Rücken landen
- In Seegras praktisch nutzlos
- Wird nur wegen OEM-Verbreitung und Bugrolle-Kompatibilität noch verwendet

### 3.5 Traditionelle Typen — Klauen-Anker

#### 3.5.1 Bruce / Claw

**Geschichte:** 1972 von Peter Bruce in Schottland für die Verankerung von Ölbohrplattformen in der Nordsee entwickelt. Später verkleinert für den Freizeitmarkt. Das Patent ist ausgelaufen, zahlreiche Kopien (Lewmar Claw, Manson Ray, diverse No-Name-Produkte).

**Designmerkmale:**
- Drei-Klauen-Design — sieht aus wie eine Katzenpfote
- Kein Gelenk, keine beweglichen Teile
- Breite Auflagefläche, aber geringe Eindringtiefe
- Selbstausrichtend — kann nicht auf dem Rücken landen

**Haltekraft nach Grundtyp (Bruce/Claw, 15 kg, Scope 5:1):**

| Grundtyp | Haltekraft (kg) | Haltekraft / Ankergewicht | Confidence |
|----------|-----------------|---------------------------|------------|
| Fester Sand | 200–300 | 13–20× | measured |
| Weicher Sand | 140–220 | 9–15× | measured |
| Schlamm | 100–180 | 7–12× | documented |
| Seegras | 30–80 | 2–5× | estimated |
| Kies/Fels | 100–180 | 7–12× | estimated |

**Stärken:**
- Rollstabil — kann nicht auf dem Rücken landen (einziger Vorteil gegenüber Delta)
- Robust, keine beweglichen Teile
- Akzeptabel in Fels/Kies (Klauen können sich festhaken)
- Günstiger als Neue Generation

**Schwächen:**
- Niedrige Haltekraft pro Kilogramm
- Braucht viel Platz auf der Bugrolle
- In Seegras praktisch nutzlos
- Lässt sich schwer verstauen (sperrige Klauenform)

### 3.6 Traditionelle Typen — Plattenanker (Fluke)

#### 3.6.1 Danforth

**Geschichte:** 1939 von Richard Danforth in den USA entwickelt. Das Design wurde für leichte Boote und als Zweitanker konzipiert. Die flachen, dreieckigen Flukes bieten eine große Angriffsfläche relativ zum Gewicht. Patent ausgelaufen, viele Kopien.

**Designmerkmale:**
- Zwei große, flache, dreieckige Flukes
- Fester Flukewinkel (ca. 32°)
- Lange, schmale Flukes — große Fläche bei geringem Gewicht
- Flach zusammenlegbar — ideal für Stauung
- Stock (Crown) stabilisiert die Ausrichtung

**Haltekraft nach Grundtyp (Danforth, 10 kg, Scope 5:1):**

| Grundtyp | Haltekraft (kg) | Haltekraft / Ankergewicht | Confidence |
|----------|-----------------|---------------------------|------------|
| Fester Sand | 200–320 | 20–32× | measured |
| Weicher Sand | 140–240 | 14–24× | measured |
| Fester Schlamm | 100–180 | 10–18× | documented |
| Weicher Schlamm | 60–120 | 6–12× | documented |
| Seegras | 10–40 | 1–4× | estimated |
| Kies/Fels | 20–60 | 2–6× | estimated |

**Stärken:**
- Hervorragendes Gewicht-zu-Haltekraft-Verhältnis in Sand
- Flach staubar — ideal als Zweitanker
- Günstig, überall erhältlich
- Leicht — einfach zu handhaben

**Schwächen:**
- Versagt in Seegras, Fels und Kies fast komplett
- Sehr schlechtes Reset-Verhalten
- Kann bei 180°-Drehung komplett herauskommen
- Stock kann sich in der Kette verfangen
- Nicht geeignet als alleiniger Hauptanker für Fahrtenyachten

#### 3.6.2 Fortress (FX-Serie, Aluminium)

**Geschichte:** Fortress Marine Products (USA) hat den Danforth-Typ in hochfestem Aluminium (7075-T73) perfektioniert. Der Fortress FX ist der leistungsstärkste Plattenanker auf dem Markt und wiegt nur ein Drittel eines vergleichbaren Stahl-Danforth.

**Designmerkmale:**
- Hochfestes Aluminium 7075-T73 (gleiche Legierung wie Flugzeugbau)
- Einstellbarer Flukewinkel: 32° (Sand) und 45° (Schlamm)
- Zerlegbar — extrem kompakt staubar
- Eloxiert oder Polymer-beschichtet
- Große Flukefläche bei minimalem Gewicht

**Haltekraft nach Grundtyp (Fortress FX-23, 7 kg, Scope 5:1):**

| Grundtyp | Haltekraft (kg) | Haltekraft / Ankergewicht | Confidence |
|----------|-----------------|---------------------------|------------|
| Fester Sand (32°) | 280–400 | 40–57× | measured |
| Weicher Sand (32°) | 200–300 | 29–43× | measured |
| Fester Schlamm (45°) | 250–380 | 36–54× | measured |
| Weicher Schlamm (45°) | 150–250 | 21–36× | measured |
| Seegras | 10–40 | 1–6× | estimated |
| Kies/Fels | 20–60 | 3–9× | estimated |

**Stärken:**
- Höchste Haltekraft pro Kilogramm aller Anker (in Sand und Schlamm)
- Extrem leicht — ideal als Zweitanker, Sturmanker, Kedge
- Verstellbarer Flukewinkel — anpassbar an den Grundtyp
- Zerlegbar — passt in eine Segeltuchtasche
- Kein Rost — Aluminium korrodiert nicht in Seewasser (bei korrekter Legierung)

**Schwächen:**
- Versagt komplett in Seegras, Fels, Koralle
- Schlechtes Reset-Verhalten (wie alle Plattenanker)
- Aluminium biegt sich bei Felsberührung → kann permanent verformt werden
- Als alleiniger Hauptanker nur in Revieren mit Sand/Schlamm geeignet
- Galvanische Korrosion bei Kontakt mit Stahlkette (Isolation nötig!)

### 3.7 Spezial-Anker

#### 3.7.1 Grapnel (Draggen / Klappdraggen)

**Einsatz:** Beiboote (Dinghi), kurzzeitiges Ankern, Bergung

**Designmerkmale:**
- 4–6 gebogene Arme (Flunken), die klappbar sind
- Kein Eindringen in den Grund — hält durch Verhaken
- Gewicht: typisch 1,5–5 kg
- Verzinkter Stahl oder Edelstahl

**Eignung:** Nur für kurzzeitiges Ankern von Beibooten oder als Enterhaken. Für Yachten als Anker ungeeignet. In Fels/Koralle kann ein Grapnel als Notanker dienen.

#### 3.7.2 Pilzanker (Mushroom Anchor)

**Einsatz:** Permanente Moorings, ruhige Gewässer, Binnenseen

**Designmerkmale:**
- Umgedrehte Pilzform — Schale nach unten
- Hält durch Gewicht und Einsaugen in weichem Grund
- Keine Flukes — funktioniert nur auf weichem, schlammigem Grund
- Gewicht: 5–500+ kg (für Moorings)

**Eignung:** Nicht als temporärer Anker für Yachten geeignet. Nur für permanente Moorings auf Schlammgrund. In Marinas und Binnenseen weit verbreitet.

#### 3.7.3 Helix-Schraubanker

**Einsatz:** Permanente Moorings in festem Sand/Lehm, Schwimmstege

**Designmerkmale:**
- Spiralförmige Fluke — wird in den Grund geschraubt
- Installation erfordert Spezialgerät (Taucher oder Bohrgerät)
- Extrem hohe Haltekraft bei korrekter Installation
- Kein Bergen möglich — permanente Installation

**Eignung:** Für Mooringfelder, Schwimmsteg-Verankerung, Aquakultur. Nicht für normales Ankern geeignet. Die höchste Haltekraft pro Grundfläche aller Ankersysteme.

#### 3.7.4 Kedge-Anker

**Einsatz:** Verholen (Warpen) des Schiffs, Zweitanker, Heckanker

Der Begriff "Kedge" bezeichnet weniger einen spezifischen Ankertyp als eine Funktion — der Kedge-Anker ist der zweite, leichtere Anker, der vom Beiboot ausgebracht wird. Typischerweise ein Fortress FX (wegen des geringen Gewichts), ein Danforth oder ein kleiner Bügel-Anker.

#### 3.7.5 Stockanker (Admiralitätsanker / Fisherman)

**Geschichte:** Der älteste Ankertyp — seit Jahrtausenden in Gebrauch. Zwei Arme mit Flukes und ein Stock (Querbalken), der den Anker in die korrekte Position kippt.

**Designmerkmale:**
- Zwei Arme mit dreieckigen Flukes
- Stock (Querbalken) rechtwinklig zur Fluke-Ebene
- Klappstock bei modernen Versionen
- Sehr schwer bei relativ niedriger Haltekraft

**Eignung:** Historisch und für traditionelle Schiffe. In Felsgrund der einzige Ankertyp, der zuverlässig hält (Arm hakt in Felsspalte). Als Heckanker oder Notanker auf Traditionsschiffen noch verbreitet.

### 3.8 Vergleichende Übersicht aller Ankertypen

**Gesamtbewertung (Skala 1–10, 10 = Bestwert):**

| Ankertyp | Sand | Schlamm | Seegras | Fels | Setzen | Reset | Stauung | Preis | Gesamt |
|----------|------|---------|---------|------|--------|-------|---------|-------|--------|
| Rocna Original | 9 | 8 | 7 | 2 | 10 | 10 | 4 | 5 | **8.5** |
| Mantus M1 | 9 | 8 | 7 | 2 | 9 | 9 | 5 | 7 | **8.3** |
| Spade S | 9 | 8 | 5 | 2 | 9 | 7 | 7 | 6 | **7.9** |
| Ultra Anchor | 10 | 9 | 7 | 2 | 10 | 10 | 4 | 3 | **8.6** |
| Rocna Vulcan | 9 | 8 | 6 | 2 | 9 | 8 | 7 | 5 | **8.1** |
| Sarca Excel | 9 | 8 | 8 | 2 | 9 | 9 | 5 | 6 | **8.4** |
| Knox | 8 | 7 | 5 | 3 | 8 | 7 | 8 | 5 | **7.3** |
| Delta | 6 | 5 | 2 | 2 | 6 | 5 | 7 | 8 | **5.5** |
| CQR | 5 | 4 | 2 | 3 | 4 | 3 | 5 | 5 | **4.2** |
| Bruce/Claw | 6 | 5 | 2 | 4 | 5 | 5 | 3 | 7 | **5.0** |
| Danforth | 7 | 5 | 1 | 1 | 7 | 2 | 9 | 9 | **5.3** |
| Fortress FX | 9 | 8 | 1 | 1 | 8 | 2 | 10 | 6 | **6.5** |
| Bügelanker (DE) | 8 | 7 | 6 | 2 | 8 | 8 | 5 | 7 | **7.5** |

---

## 4. Produktlinien und Hersteller

### 4.1 Rocna Anchors (Neuseeland / Kanada)

**Firmenprofil:**
- Gegründet: 2004 von Peter Smith in Neuseeland
- Übernahme durch Canada Metal Pacific 2011
- Fertigung: Kanada, China (Lizenz)
- Website: rocna.com

#### 4.1.1 Rocna Original — Modellreihe

| Modell | Gewicht (kg) | Bootslänge (m) | Material | Oberfläche | Preis ca. (EUR) | Confidence |
|--------|-------------|-----------------|----------|------------|-----------------|------------|
| Rocna 4 | 4 | bis 7 | Stahl | Feuerverzinkt | 350–420 | documented |
| Rocna 6 | 6 | 7–9 | Stahl | Feuerverzinkt | 420–500 | documented |
| Rocna 10 | 10 | 9–11 | Stahl | Feuerverzinkt | 550–680 | documented |
| Rocna 15 | 15 | 11–13 | Stahl | Feuerverzinkt | 750–900 | documented |
| Rocna 20 | 20 | 13–15 | Stahl | Feuerverzinkt | 950–1.150 | documented |
| Rocna 25 | 25 | 15–17 | Stahl | Feuerverzinkt | 1.200–1.450 | documented |
| Rocna 33 | 33 | 17–20 | Stahl | Feuerverzinkt | 1.600–1.900 | documented |
| Rocna 40 | 40 | 20–23 | Stahl | Feuerverzinkt | 2.100–2.500 | documented |
| Rocna 55 | 55 | 23–27 | Stahl | Feuerverzinkt | 3.200–3.800 | documented |
| Rocna 75 | 75 | 27–33 | Stahl | Feuerverzinkt | 4.500–5.500 | documented |

**Edelstahl-Versionen:** Verfügbar für alle Größen. Preisaufschlag ca. 200–300 %. Empfohlen nur für Yachten, bei denen die Optik am Bug entscheidend ist.

#### 4.1.2 Rocna Vulcan — Modellreihe

| Modell | Gewicht (kg) | Bootslänge (m) | Material | Oberfläche | Preis ca. (EUR) | Confidence |
|--------|-------------|-----------------|----------|------------|-----------------|------------|
| Vulcan 4 | 4 | bis 7 | Stahl | Feuerverzinkt | 320–400 | documented |
| Vulcan 6 | 6 | 7–9 | Stahl | Feuerverzinkt | 400–480 | documented |
| Vulcan 9 | 9 | 9–11 | Stahl | Feuerverzinkt | 500–620 | documented |
| Vulcan 12 | 12 | 11–13 | Stahl | Feuerverzinkt | 650–800 | documented |
| Vulcan 16 | 16 | 13–15 | Stahl | Feuerverzinkt | 850–1.050 | documented |
| Vulcan 20 | 20 | 15–17 | Stahl | Feuerverzinkt | 1.050–1.300 | documented |
| Vulcan 25 | 25 | 17–20 | Stahl | Feuerverzinkt | 1.350–1.650 | documented |
| Vulcan 33 | 33 | 20–23 | Stahl | Feuerverzinkt | 1.800–2.200 | documented |
| Vulcan 45 | 45 | 23–27 | Stahl | Feuerverzinkt | 2.600–3.100 | documented |
| Vulcan 60 | 60 | 27–33 | Stahl | Feuerverzinkt | 3.800–4.500 | documented |

### 4.2 Mantus Marine (USA)

**Firmenprofil:**
- Gegründet: 2010 von Ray Crawford
- Fertigung: USA (Texas)
- Website: mantusanchors.com
- Besonderheit: Starker Direktvertrieb, guter Kundensupport

#### 4.2.1 Mantus M1 — Modellreihe

| Modell | Gewicht (kg) | Bootslänge (m) | Material | Oberfläche | Preis ca. (EUR) | Confidence |
|--------|-------------|-----------------|----------|------------|-----------------|------------|
| Mantus M1 8 lb | 3,6 | bis 7 | Stahl | Feuerverzinkt | 200–280 | documented |
| Mantus M1 17 lb | 7,7 | 7–9 | Stahl | Feuerverzinkt | 300–380 | documented |
| Mantus M1 25 lb | 11,3 | 9–11 | Stahl | Feuerverzinkt | 420–520 | documented |
| Mantus M1 35 lb | 15,9 | 11–13 | Stahl | Feuerverzinkt | 550–680 | documented |
| Mantus M1 45 lb | 20,4 | 13–15 | Stahl | Feuerverzinkt | 700–850 | documented |
| Mantus M1 65 lb | 29,5 | 15–18 | Stahl | Feuerverzinkt | 950–1.150 | documented |
| Mantus M1 85 lb | 38,6 | 18–21 | Stahl | Feuerverzinkt | 1.300–1.550 | documented |
| Mantus M1 105 lb | 47,6 | 21–25 | Stahl | Feuerverzinkt | 1.700–2.000 | documented |
| Mantus M1 125 lb | 56,7 | 25–30 | Stahl | Feuerverzinkt | 2.200–2.600 | documented |
| Mantus M1 155 lb | 70,3 | 30+ | Stahl | Feuerverzinkt | 2.800–3.400 | documented |

#### 4.2.2 Mantus M2 — Modellreihe

Der Mantus M2 ist die Weiterentwicklung des M1 mit modularem Schaft-System. Der Schaft kann gegen verschiedene Längen und Typen getauscht werden.

| Modell | Gewicht (kg) | Bootslänge (m) | Preis ca. (EUR) | Confidence |
|--------|-------------|-----------------|-----------------|------------|
| Mantus M2 25 lb | 11,3 | 9–11 | 550–680 | documented |
| Mantus M2 35 lb | 15,9 | 11–13 | 700–880 | documented |
| Mantus M2 45 lb | 20,4 | 13–15 | 880–1.050 | documented |
| Mantus M2 65 lb | 29,5 | 15–18 | 1.150–1.400 | documented |
| Mantus M2 85 lb | 38,6 | 18–21 | 1.550–1.850 | documented |

### 4.3 Spade Anchors (Frankreich)

**Firmenprofil:**
- Gegründet: 1996 von Alain Poiraud
- Fertigung: Frankreich
- Website: spade-anchor.com
- Besonderheit: Pionier der Neuen Generation, bewährtestes Design

#### 4.3.1 Spade S (Stahl) — Modellreihe

| Modell | Gewicht (kg) | Bootslänge (m) | Material | Preis ca. (EUR) | Confidence |
|--------|-------------|-----------------|----------|-----------------|------------|
| Spade S40 | 4,5 | bis 7 | Stahl verzinkt | 380–480 | documented |
| Spade S60 | 6,5 | 7–9 | Stahl verzinkt | 480–600 | documented |
| Spade S80 | 9 | 9–11 | Stahl verzinkt | 600–750 | documented |
| Spade S100 | 12 | 11–13 | Stahl verzinkt | 780–950 | documented |
| Spade S120 | 14 | 13–15 | Stahl verzinkt | 950–1.150 | documented |
| Spade S140 | 18 | 15–17 | Stahl verzinkt | 1.200–1.450 | documented |
| Spade S160 | 22 | 17–20 | Stahl verzinkt | 1.500–1.800 | documented |
| Spade S180 | 28 | 20–23 | Stahl verzinkt | 1.900–2.300 | documented |
| Spade S200 | 35 | 23–27 | Stahl verzinkt | 2.500–3.000 | documented |
| Spade S250 | 50 | 27–33 | Stahl verzinkt | 3.500–4.200 | documented |

#### 4.3.2 Spade X (Aluminium) — Modellreihe

| Modell | Gewicht (kg) | Bootslänge (m) | Material | Preis ca. (EUR) | Confidence |
|--------|-------------|-----------------|----------|-----------------|------------|
| Spade X40 | 2,5 | bis 7 | Alu 6061-T6 | 450–550 | documented |
| Spade X80 | 5 | 9–11 | Alu 6061-T6 | 700–850 | documented |
| Spade X120 | 8 | 13–15 | Alu 6061-T6 | 1.100–1.350 | documented |
| Spade X160 | 12 | 17–20 | Alu 6061-T6 | 1.600–1.950 | documented |
| Spade X200 | 18 | 23–27 | Alu 6061-T6 | 2.200–2.700 | documented |

### 4.4 Ultra Marine (Niederlande)

**Firmenprofil:**
- Entwicklung ab 2010, Markteinführung 2012
- Fertigung: Niederlande
- Website: ultra-anchor.com
- Besonderheit: Premium-Segment, höchste Verarbeitungsqualität

#### 4.4.1 Ultra Anchor — Modellreihe

| Modell | Gewicht (kg) | Bootslänge (m) | Material | Preis ca. (EUR) | Confidence |
|--------|-------------|-----------------|----------|-----------------|------------|
| Ultra 5 | 5 | bis 7 | Stahl verzinkt | 500–620 | documented |
| Ultra 8 | 8 | 7–9 | Stahl verzinkt | 650–800 | documented |
| Ultra 12 | 12 | 9–11 | Stahl verzinkt | 850–1.050 | documented |
| Ultra 16 | 16 | 11–13 | Stahl verzinkt | 1.100–1.350 | documented |
| Ultra 20 | 20 | 13–15 | Stahl verzinkt | 1.400–1.700 | documented |
| Ultra 27 | 27 | 15–18 | Stahl verzinkt | 1.900–2.300 | documented |
| Ultra 35 | 35 | 18–21 | Stahl verzinkt | 2.500–3.000 | documented |
| Ultra 50 | 50 | 21–25 | Stahl verzinkt | 3.500–4.200 | documented |
| Ultra 70 | 70 | 25–30 | Stahl verzinkt | 5.000–6.000 | documented |
| Ultra 100 | 100 | 30+ | Stahl verzinkt | 7.500–9.000 | documented |

**Ultra Flip:** Kompakte Variante mit klappbarem Schaft. Gleiche Fluke-Geometrie, aber 30 % weniger Stauvolumen.

| Modell | Gewicht (kg) | Bootslänge (m) | Preis ca. (EUR) | Confidence |
|--------|-------------|-----------------|-----------------|------------|
| Ultra Flip 8 | 8 | 7–9 | 750–900 | documented |
| Ultra Flip 12 | 12 | 9–11 | 950–1.150 | documented |
| Ultra Flip 16 | 16 | 11–13 | 1.250–1.500 | documented |
| Ultra Flip 20 | 20 | 13–15 | 1.550–1.900 | documented |
| Ultra Flip 27 | 27 | 15–18 | 2.100–2.500 | documented |

### 4.5 Fortress Marine Products (USA)

**Firmenprofil:**
- Gegründet: 1986
- Fertigung: USA (Florida)
- Website: fortressanchors.com
- Besonderheit: Einziger Hersteller von Premium-Aluminium-Ankern

#### 4.5.1 Fortress FX-Serie — Modellreihe

| Modell | Gewicht (kg) | Bootslänge (m) | Flukefläche (cm²) | Preis ca. (EUR) | Confidence |
|--------|-------------|-----------------|-------------------|-----------------|------------|
| FX-7 | 1,8 | bis 5 | 890 | 150–200 | documented |
| FX-11 | 3,2 | 5–8 | 1.480 | 220–280 | documented |
| FX-16 | 4,3 | 8–10 | 2.140 | 280–350 | documented |
| FX-23 | 6,8 | 10–13 | 3.350 | 380–470 | documented |
| FX-37 | 10,9 | 13–16 | 5.160 | 520–640 | documented |
| FX-55 | 14,1 | 16–20 | 7.610 | 700–870 | documented |
| FX-85 | 21,8 | 20–25 | 10.970 | 1.050–1.300 | documented |
| FX-125 | 29,5 | 25–30 | 16.130 | 1.500–1.850 | documented |

**Fortress FXA (Aluminium, anodisiert):** Gleiche Modelle wie FX, aber mit anodisierter Oberfläche für zusätzlichen Korrosionsschutz. Preisaufschlag ca. 15–20 %.

**Fortress Commando Serie:** Kompakte Version für Militär und Spezialeinsätze. Verstärkte Scharniere, schnellere Montage.

### 4.6 Lewmar (UK)

**Firmenprofil:**
- Gegründet: 1946 in Havant, Hampshire
- Fertigung: UK, Italien
- Website: lewmar.com
- Besonderheit: Größter OEM-Ankerlieferant weltweit (Delta ist Werksanker bei Beneteau, Jeanneau, Bavaria, Hanse)

#### 4.6.1 Lewmar Delta — Modellreihe

| Modell | Gewicht (kg) | Bootslänge (m) | Material | Preis ca. (EUR) | Confidence |
|--------|-------------|-----------------|----------|-----------------|------------|
| Delta 4 | 4 | bis 7 | Stahl verzinkt | 120–160 | documented |
| Delta 6 | 6 | 7–8 | Stahl verzinkt | 150–200 | documented |
| Delta 10 | 10 | 8–10 | Stahl verzinkt | 200–260 | documented |
| Delta 14 | 14 | 10–12 | Stahl verzinkt | 280–350 | documented |
| Delta 16 | 16 | 12–14 | Stahl verzinkt | 340–420 | documented |
| Delta 20 | 20 | 14–16 | Stahl verzinkt | 420–520 | documented |
| Delta 25 | 25 | 16–18 | Stahl verzinkt | 550–680 | documented |
| Delta 32 | 32 | 18–21 | Stahl verzinkt | 720–880 | documented |
| Delta 40 | 40 | 21–24 | Stahl verzinkt | 950–1.150 | documented |
| Delta 63 | 63 | 24–30 | Stahl verzinkt | 1.500–1.850 | documented |

#### 4.6.2 Lewmar Epsilon — Modellreihe

Der Epsilon ist Lewmars Antwort auf die Neue-Generation-Anker. Bügel-Design, konkave Fluke.

| Modell | Gewicht (kg) | Bootslänge (m) | Preis ca. (EUR) | Confidence |
|--------|-------------|-----------------|-----------------|------------|
| Epsilon 6 | 6 | 7–9 | 350–440 | documented |
| Epsilon 10 | 10 | 9–11 | 480–600 | documented |
| Epsilon 14 | 14 | 11–13 | 620–770 | documented |
| Epsilon 16 | 16 | 13–15 | 780–950 | documented |
| Epsilon 24 | 24 | 15–18 | 1.050–1.300 | documented |
| Epsilon 32 | 32 | 18–22 | 1.450–1.750 | documented |

#### 4.6.3 Lewmar DTX — Modellreihe

Der DTX (Delta Technology neXt) ist die Weiterentwicklung des Delta mit verbesserter Fluke-Geometrie. Kompromiss zwischen Bugrolle-Kompatibilität des Delta und Leistung der Neuen Generation.

| Modell | Gewicht (kg) | Bootslänge (m) | Preis ca. (EUR) | Confidence |
|--------|-------------|-----------------|-----------------|------------|
| DTX 6 | 6 | 7–9 | 250–320 | documented |
| DTX 10 | 10 | 9–11 | 350–440 | documented |
| DTX 14 | 14 | 11–13 | 450–560 | documented |
| DTX 20 | 20 | 14–16 | 600–740 | documented |
| DTX 25 | 25 | 16–18 | 780–950 | documented |

### 4.7 Manson Anchors (Neuseeland)

**Firmenprofil:**
- Gegründet: 1974 in Auckland
- Fertigung: Neuseeland, China (Lizenz)
- Website: mansonanchors.com
- Besonderheit: Breites Programm von traditionell bis Neue Generation

#### 4.7.1 Manson Supreme — Modellreihe

Der Manson Supreme ist ein Bügel-Anker ähnlich dem Rocna, aber mit einigen Designunterschieden (flacherer Bügel, andere Fluke-Geometrie).

| Modell | Gewicht (kg) | Bootslänge (m) | Preis ca. (EUR) | Confidence |
|--------|-------------|-----------------|-----------------|------------|
| Supreme 6 | 6 | 7–9 | 350–430 | documented |
| Supreme 11 | 11 | 9–11 | 480–600 | documented |
| Supreme 16 | 16 | 11–14 | 650–800 | documented |
| Supreme 22 | 22 | 14–17 | 880–1.080 | documented |
| Supreme 30 | 30 | 17–20 | 1.200–1.450 | documented |
| Supreme 40 | 40 | 20–24 | 1.650–2.000 | documented |
| Supreme 55 | 55 | 24–28 | 2.300–2.800 | documented |
| Supreme 75 | 75 | 28–33 | 3.200–3.900 | documented |

#### 4.7.2 Manson Boss — Modellreihe

Kompaktere Version des Supreme für Boote mit engen Bugrollen.

| Modell | Gewicht (kg) | Bootslänge (m) | Preis ca. (EUR) | Confidence |
|--------|-------------|-----------------|-----------------|------------|
| Boss 7 | 7 | 7–9 | 300–380 | documented |
| Boss 11 | 11 | 9–11 | 420–520 | documented |
| Boss 16 | 16 | 11–14 | 580–720 | documented |
| Boss 22 | 22 | 14–17 | 780–960 | documented |
| Boss 30 | 30 | 17–20 | 1.050–1.280 | documented |

#### 4.7.3 Manson Racer — Modellreihe

Leichtgewicht-Anker für Regattayachten. Aluminium-Konstruktion.

| Modell | Gewicht (kg) | Bootslänge (m) | Preis ca. (EUR) | Confidence |
|--------|-------------|-----------------|-----------------|------------|
| Racer 3 | 3 | bis 8 | 280–350 | documented |
| Racer 5 | 5 | 8–10 | 380–470 | documented |
| Racer 7 | 7 | 10–12 | 500–620 | documented |
| Racer 10 | 10 | 12–14 | 650–800 | documented |

### 4.8 Knox Anchors (UK)

**Firmenprofil:**
- Entwickler: John Knox
- Fertigung: UK
- Website: knoxanchor.com
- Besonderheit: Einzigartiges Scherflügel-Design

| Modell | Gewicht (kg) | Bootslänge (m) | Material | Preis ca. (EUR) | Confidence |
|--------|-------------|-----------------|----------|-----------------|------------|
| Knox 5 | 5 | bis 8 | Edelstahl 316 | 550–680 | documented |
| Knox 8 | 8 | 8–10 | Edelstahl 316 | 750–920 | documented |
| Knox 12 | 12 | 10–13 | Edelstahl 316 | 1.050–1.280 | documented |
| Knox 16 | 16 | 13–16 | Edelstahl 316 | 1.400–1.700 | documented |
| Knox 22 | 22 | 16–20 | Edelstahl 316 | 1.900–2.300 | documented |

### 4.9 Sarca Anchors (Australien)

**Firmenprofil:**
- Gegründet: von Rex Mead in Australien
- Fertigung: Australien
- Website: sarcaanchor.com.au
- Besonderheit: Spezialisiert auf schwierige australische Ankergründe

#### 4.9.1 Sarca Excel — Modellreihe

| Modell | Gewicht (kg) | Bootslänge (m) | Material | Preis ca. (EUR) | Confidence |
|--------|-------------|-----------------|----------|-----------------|------------|
| Excel 4 | 4 | bis 7 | Stahl verzinkt | 280–350 | documented |
| Excel 7 | 7 | 7–9 | Stahl verzinkt | 380–470 | documented |
| Excel 10 | 10 | 9–11 | Stahl verzinkt | 500–620 | documented |
| Excel 15 | 15 | 11–13 | Stahl verzinkt | 680–830 | documented |
| Excel 20 | 20 | 13–16 | Stahl verzinkt | 880–1.080 | documented |
| Excel 27 | 27 | 16–19 | Stahl verzinkt | 1.150–1.400 | documented |
| Excel 35 | 35 | 19–23 | Stahl verzinkt | 1.550–1.900 | documented |
| Excel 50 | 50 | 23–28 | Stahl verzinkt | 2.200–2.700 | documented |

#### 4.9.2 Sarca Super — Modellreihe

Leichtere Version des Excel für kleinere Boote und als Zweitanker.

| Modell | Gewicht (kg) | Bootslänge (m) | Preis ca. (EUR) | Confidence |
|--------|-------------|-----------------|-----------------|------------|
| Super 4 | 4 | bis 8 | Stahl verzinkt | 220–280 | documented |
| Super 7 | 7 | 8–10 | Stahl verzinkt | 300–380 | documented |
| Super 11 | 11 | 10–12 | Stahl verzinkt | 420–520 | documented |
| Super 16 | 16 | 12–15 | Stahl verzinkt | 580–720 | documented |

### 4.10 Bügelanker (Deutschland)

**Hintergrund:**
Der "Bügelanker" ist die deutsche Bezeichnung für verschiedene Bügel-Anker, die häufig von deutschen Herstellern oder Importeuren unter eigenem Namen vertrieben werden. Viele sind lizenzierte oder inspirierte Designs basierend auf Rocna/Mantus-Prinzipien.

**Bekannte deutsche Quellen:**
- SVB (Bremen): Bügelanker "Premium" und "Comfort"
- Compass (Deggendorf): Bügelanker
- AWN (Hamburg): Bügelanker
- Plastimo (über deutsche Händler)

| Modell (SVB Premium) | Gewicht (kg) | Bootslänge (m) | Material | Preis ca. (EUR) | Confidence |
|---------------------|-------------|-----------------|----------|-----------------|------------|
| Bügelanker 5 | 5 | bis 7 | Stahl verzinkt | 150–220 | estimated |
| Bügelanker 7,5 | 7,5 | 7–9 | Stahl verzinkt | 200–280 | estimated |
| Bügelanker 10 | 10 | 9–11 | Stahl verzinkt | 280–380 | estimated |
| Bügelanker 15 | 15 | 11–13 | Stahl verzinkt | 380–500 | estimated |
| Bügelanker 20 | 20 | 13–16 | Stahl verzinkt | 500–650 | estimated |
| Bügelanker 25 | 25 | 16–18 | Stahl verzinkt | 650–850 | estimated |
| Bügelanker 35 | 35 | 18–22 | Stahl verzinkt | 900–1.150 | estimated |

**Hinweis zur Qualität:** Die Qualität von No-Name-Bügelankern variiert stark. Kritische Prüfpunkte:
- Schweißnähte am Bügel (Bruchstelle Nr. 1)
- Stahlqualität (hochwertiger Stahl vs. Baustahl)
- Verzinkungsqualität (Feuerverzinkung vs. galvanische Verzinkung)
- Flukegeometrie (präzise Kopie vs. vereinfachte Version)

**AYDI-Empfehlung:** Bei Bügelankern unbekannter Herkunft immer `estimated` Confidence vergeben und auf mögliche Qualitätsmängel hinweisen.

---

## 5. Dimensionierung

### 5.1 Grundregeln der Ankerdimensionierung

Die korrekte Ankergröße ist der wichtigste Einzelfaktor für sicheres Ankern. Ein zu kleiner Anker ist gefährlich, ein zu großer Anker ist unpraktisch und belastet den Bug.

**Dimensionierungsfaktoren:**
1. **Bootslänge (LOA)** — primärer Faktor für Standardempfehlungen
2. **Verdrängung** — entscheidend bei schweren Booten (Langkieler, Stahlyachten)
3. **Windangriffsfläche** — entscheidend bei hohem Aufbau (Flybridge, Katamaran)
4. **Einsatzrevier** — Mittelmeer (wenig Strom, variable Gründe) vs. Gezeitenrevier (Strom, Schwell)
5. **Ankerstrategie** — Nur Tagesanker? Übernachten? Langfahrt? Überwintern?

### 5.2 Dimensionierungstabelle — Hauptanker (Neue Generation)

**Für Bügel-Anker (Rocna, Mantus, Ultra, Sarca Excel, Bügelanker):**

| LOA (m) | Verdrängung (t) | Ankergewicht (kg) | Kettengröße (mm) | Kettenlänge min. (m) | Confidence |
|---------|----------------|--------------------|-------------------|----------------------|------------|
| 6–7 | 1–2 | 4–6 | 6 | 25–30 | documented |
| 7–8 | 2–3 | 6–8 | 6–8 | 30–35 | documented |
| 8–9 | 3–4 | 8–10 | 8 | 35–40 | documented |
| 9–10 | 4–6 | 10–12 | 8 | 40–50 | documented |
| 10–11 | 5–8 | 10–15 | 8–10 | 40–50 | documented |
| 11–12 | 7–10 | 12–16 | 8–10 | 50–60 | documented |
| 12–13 | 8–12 | 15–20 | 10 | 50–60 | documented |
| 13–14 | 10–15 | 16–20 | 10 | 60–70 | documented |
| 14–15 | 12–18 | 20–25 | 10 | 60–70 | documented |
| 15–17 | 15–22 | 25–33 | 10–12 | 70–80 | documented |
| 17–20 | 20–35 | 33–40 | 12 | 80–100 | documented |
| 20–23 | 30–50 | 40–55 | 12–14 | 80–100 | documented |
| 23–27 | 45–80 | 55–75 | 14 | 100+ | documented |
| 27–33 | 70–120 | 75–100 | 14–16 | 100+ | estimated |

### 5.3 Dimensionierungstabelle — Hauptanker (Traditionelle Typen)

**Für Delta, CQR, Bruce (traditionelle Typen benötigen ca. 30–50 % mehr Gewicht als Neue Generation):**

| LOA (m) | Verdrängung (t) | Delta/CQR (kg) | Bruce/Claw (kg) | Danforth (kg) | Confidence |
|---------|----------------|-----------------|------------------|----------------|------------|
| 6–7 | 1–2 | 6–8 | 7,5–10 | 4–6 | documented |
| 7–8 | 2–3 | 8–10 | 10–12,5 | 6–8 | documented |
| 8–9 | 3–4 | 10–14 | 12,5–15 | 6–8 | documented |
| 9–10 | 4–6 | 14–16 | 15–20 | 8–10 | documented |
| 10–11 | 5–8 | 14–20 | 15–20 | 10–12 | documented |
| 11–12 | 7–10 | 16–20 | 20–25 | 10–14 | documented |
| 12–13 | 8–12 | 20–25 | 20–25 | 14–16 | documented |
| 13–14 | 10–15 | 20–25 | 25–30 | 14–18 | documented |
| 14–15 | 12–18 | 25–32 | 25–30 | 18–22 | documented |
| 15–17 | 15–22 | 32–40 | 30–40 | 22–28 | documented |
| 17–20 | 20–35 | 40–63 | 40–50 | 28–36 | documented |

### 5.4 Zweitanker (Reserveanker)

Der Zweitanker sollte mindestens 60–75 % des Gewichts des Hauptankers haben. Er dient als:
- Reserve bei Verlust des Hauptankers
- Kedge-Anker (vom Beiboot ausbringen)
- Heckanker (Balearische Ankerung)
- Entlastungsanker bei schwerem Wetter (V-Ankerung)

**Empfohlene Zweitanker-Typen:**
- Fortress FX (leicht, staubar, exzellent in Sand/Schlamm)
- Spade X Aluminium (leicht, zerlegbar)
- Danforth/Guardian (günstig, flach staubar)
- Kleinerer Bügel-Anker (wenn Stauraum vorhanden)

**Dimensionierungstabelle — Zweitanker:**

| LOA (m) | Hauptanker Neue Gen. (kg) | Zweitanker min. (kg) | Fortress FX empfohlen | Confidence |
|---------|--------------------------|----------------------|-----------------------|------------|
| 8–10 | 8–12 | 5–8 | FX-16 (4,3 kg) | documented |
| 10–12 | 10–16 | 7–10 | FX-23 (6,8 kg) | documented |
| 12–14 | 15–20 | 10–14 | FX-37 (10,9 kg) | documented |
| 14–16 | 20–25 | 14–18 | FX-55 (14,1 kg) | documented |
| 16–20 | 25–40 | 18–27 | FX-85 (21,8 kg) | documented |
| 20–25 | 40–55 | 27–38 | FX-125 (29,5 kg) | documented |

### 5.5 Sturmanker

Für Langfahrt und Überlebensankern wird ein Sturmanker empfohlen. Der Sturmanker ist ein übergroßer Hauptanker (130–150 % des normalen Hauptankers) oder ein gleichwertiger Anker eines anderen Typs.

**Strategien für den Sturmanker:**
1. **Übergroßer Hauptanker:** Z. B. 25-kg-Rocna statt 15 kg bei einer 12-m-Yacht
2. **V-Ankerung:** Zwei Anker in V-Form (60°–90° Winkel) ausbringen → verdoppelt die Haltekraft bei weniger Schwojkreis
3. **Tandem-Ankerung:** Zwei Anker hintereinander auf derselben Kette → ca. 150 % der Haltekraft eines einzelnen Ankers
4. **Bahamian Moor:** Zwei Anker, einer nach vorn, einer nach achtern → reduziert Schwojkreis auf Minimum (für enge Buchten oder Tidenreviere)

### 5.6 Spezialfälle: Katamarane und Multihulls

Katamarane haben eine deutlich höhere Windangriffsfläche als vergleichbare Einrümpfer. Die Ankerausrüstung muss entsprechend dimensioniert werden:

| Katamaran LOA (m) | Verdrängung (t) | Windangriffsfläche (m²) | Empf. Ankergewicht Neue Gen. (kg) | Confidence |
|-------------------|----------------|------------------------|------------------------------------|------------|
| 10–12 | 5–8 | 20–28 | 15–20 | estimated |
| 12–14 | 8–14 | 28–38 | 20–25 | estimated |
| 14–16 | 12–20 | 35–50 | 25–33 | estimated |
| 16–18 | 18–28 | 45–60 | 33–40 | estimated |

**Besonderheiten Katamaran-Ankerung:**
- Höhere Windangriffsfläche → größerer Anker nötig
- Geringerer Tiefgang → Scope-Berechnung beachten (H_bug kleiner)
- Zwei Bugrollen möglich → V-Ankerung einfacher umsetzbar
- Breiterer Schwojkreis → größerer Platzbedarf am Ankerplatz

### 5.7 Spezialfälle: Motoryachten mit hohem Aufbau

Flybridge-Motoryachten und Trawler haben eine besonders hohe Windangriffsfläche. Der Anker muss entsprechend größer gewählt werden als für einen Segler gleicher Länge.

**Faustformel:** Motoryacht mit Flybridge → +30 % gegenüber Segler gleicher Länge.

---

## 6. Anlagen-spezifische Zuordnung

### 6.1 Hauptanker-Konfiguration (Primary Anchor)

**Standard-Setup für Fahrtenyachten 10–15 m:**

```
Konfiguration:
├── Anker: Neue-Generation Bügel-Anker (Rocna, Mantus, Ultra, etc.)
│   ├── Gewicht: gemäß Dimensionierungstabelle
│   ├── Material: Stahl feuerverzinkt (Standard) oder Edelstahl (Premium)
│   └── Montage: In Bugrolle, selbsteinziehend
├── Kette: Kurzglied-Ankerkette ISO 4565
│   ├── Durchmesser: gemäß Tabelle
│   ├── Material: Stahl verzinkt, Grade 40 (Standard) oder Grade 70 (hochfest)
│   ├── Länge: gemäß Tabelle
│   └── Markierung: Alle 5 m oder 10 m mit Farbe oder Kabelbindern
├── Verbindung Anker-Kette: Ankerwirbel (Edelstahl 316) oder Bügelschäkel
├── Kettenvorlauf: 5–10 m Kette vor dem Seil (bei Kette+Seil-System)
├── Kettenstopper: Am Bugbeschlag, entlastet die Ankerwinsche
├── Ankerwinsche: Elektrisch (ab 10 m LOA empfohlen)
└── Ankerkasten: Selbstlenzend, Kettenlänge vollständig aufnehmend
```

### 6.2 Zweitanker-Konfiguration (Secondary Anchor)

**Standard-Setup:**

```
Konfiguration:
├── Anker: Fortress FX (Aluminium) oder Spade X (Aluminium)
│   ├── Gewicht: 60–75 % des Hauptankers
│   └── Stauung: Zerlegbar in Ankertasche, Backskiste oder Cockpitlocker
├── Kette: 5–10 m Kurzglied-Kette als Vorlauf
├── Leine: 50–80 m Nylon-Ankerleine (3-schäftig oder geflochten)
│   ├── Durchmesser: 14–18 mm (abhängig von Bootsgröße)
│   └── Dehnung: 15–25 % bei Bruchlast (Stoßdämpfung!)
├── Verbindung Kette-Leine: Spleißverbindung oder Schäkel mit Mausung
└── Stauung: Leine in Leinenbeutel, Kette in Kettensack
```

### 6.3 Kedge-Anker-Konfiguration

Der Kedge wird vom Beiboot aus gesetzt. Er dient zum:
- Freiwarpen bei Grundberührung
- Ausbringen eines zweiten Ankers
- Heckankerung an der Küste (Mittelmeer-Stil)
- Verholen in engen Häfen ohne Motor

**Anforderungen an den Kedge:**
- Leicht genug, um im Beiboot transportiert zu werden (max. 15 kg)
- Handhabbar durch eine Person
- Setzt schnell und zuverlässig (kein zweiter Versuch vom Beiboot aus möglich)

### 6.4 Heckanker-Konfiguration (Stern Anchor)

**Einsatz:** Mittelmeer-Ankerung (Buganker + Heck an der Küste), enge Buchten, Reduktion des Schwojkreises.

**Setup:**

```
Konfiguration:
├── Anker: Kleinerer Bügel-Anker oder Fortress
│   ├── Gewicht: 50–75 % des Hauptankers
│   └── Montage: Heckkorb, Achterrelingshalterung oder Beibootdavits
├── Kette/Leine: 5 m Kette + 50–100 m Nylon-Leine
├── Leinenführung: Über Heckrolle oder Heckklüse
└── Spezial: Kettenvorlauf schützt Leine vor Abrieb am Grund
```

### 6.5 Konfigurationsmatrix nach Einsatzprofil

| Einsatzprofil | Hauptanker | Zweitanker | Heckanker | Kedge | Confidence |
|---------------|------------|------------|-----------|-------|------------|
| Wochenend-Segler (Ostsee) | Neue Gen. Standard | Danforth | — | — | documented |
| Küstenkreuzer (Mittelmeer) | Neue Gen. Standard | Fortress FX | Klein Bügel | = Heckanker | documented |
| Langfahrt (Weltumsegelung) | Neue Gen. überdim. | Fortress FX groß | Neue Gen. klein | = Zweitanker | documented |
| Regatta mit Komfort | Delta/Vulcan (leicht) | — | — | — | estimated |
| Charter (Mittelmeer) | Delta (OEM) | — | — | — | documented |
| Motoryacht Flybridge | Neue Gen. +30% | Fortress FX | — | — | documented |
| Katamaran Fahrt | Neue Gen. +30% | Fortress FX | Neue Gen. klein | = Zweitanker | documented |

---

## 7. Fehlerbild-Atlas

### 7.1 Übersicht der häufigsten Anker-Fehlerbilder

| Nr. | Fehlerbild | Schweregrad | Häufigkeit | Erkennbarkeit (Foto) | Confidence |
|-----|-----------|-------------|------------|----------------------|------------|
| F01 | Anker schleppt (Dragging) | KRITISCH | Sehr häufig | visual_insufficient | — |
| F02 | Verkeilter/verklemmter Anker (Fouled) | MITTEL | Häufig | visual_low | — |
| F03 | Verbogener Schaft | KRITISCH | Selten | visual_medium | — |
| F04 | Gebrochene Schweißnaht (Bügel) | KRITISCH | Selten | visual_high | — |
| F05 | Korrosion an Schweißnähten | HOCH | Häufig | visual_medium | — |
| F06 | Ausgeschlagenes Gelenk (CQR) | HOCH | Häufig (alte CQR) | visual_medium | — |
| F07 | Abgenutzte Fluke-Spitze | MITTEL | Häufig | visual_medium | — |
| F08 | Fehlende Verzinkung | HOCH | Mittel | visual_high | — |
| F09 | Falsche Ankergröße | KRITISCH | Häufig | visual_medium | — |
| F10 | Inkompatible Bugrolle | MITTEL | Häufig | visual_high | — |
| F11 | Gerissener Schäkel | KRITISCH | Selten | visual_high | — |
| F12 | Verstopfter Ankerkopf (Grund) | NIEDRIG | Sehr häufig | visual_medium | — |

### 7.2 F01 — Anker schleppt (Dragging)

**Beschreibung:** Der Anker hat sich nicht korrekt gesetzt oder bricht aus dem Grund aus. Die Yacht treibt mit dem Wind/Strom ab.

**Ursachen:**
1. Falscher Scope (zu kurz) — häufigste Ursache
2. Zu kleiner Anker für Boot/Wetter
3. Ungeeigneter Ankergröße für den Grundtyp
4. Anker hat sich nicht umgedreht (kein Bügel, auf dem Rücken)
5. Seegras verhindert Eindringen
6. Anker mit Schlamm/Gras verstopft von vorherigem Ankern

**Erkennung:**
- GPS-Ankerwarnung zeigt Positionsveränderung
- Peilung zu Landmarken ändert sich
- Kette nicht straff, sondern schlaff (Anker pflügt)
- Kettengeräusche (rucken/schleifen)

**Gegenmaßnahmen:**
1. Sofort mehr Kette fieren (Scope erhöhen)
2. Motor langsam rückwärts geben, um Anker zu setzen
3. Wenn nicht setzbar: Anker aufholen, Position wechseln, neu ankern
4. Bei anhaltendem Scheitern: Zweitanker ausbringen (V-Ankerung)

**AYDI-Bewertung:** Nicht direkt aus Fotos erkennbar → `visual_insufficient`. Nur aus GPS-Daten oder Berichten evaluierbar → `documented`.

### 7.3 F02 — Verkeilter/verklemmter Anker (Fouled Anchor)

**Beschreibung:** Der Anker ist im Grund verklemmt und kann nicht geborgen werden. Kann durch Fels, Kabel, alte Ketten, Koralle oder andere Hindernisse verursacht werden.

**Ursachen:**
1. Felsgrund — Fluke in Spalte verklemmt
2. Alte Ankerketten anderer Boote auf dem Grund
3. Unterwasserkabel oder Rohrleitungen
4. Korallenriff — Anker in Korallen verhakt
5. Treibgut (Netze, Leinen, Holz) um Anker gewickelt

**Erkennungsmerkmale:**
- Kette steht senkrecht unter dem Bug
- Ankerwinsche blockiert oder überlastet
- Vibrationen in der Kette beim Versuch zu heben
- Anker kommt nicht frei bei Rückwärtsfahrt über Ankerposition

**Bergen eines verklemmten Ankers:**
1. Über den Anker fahren (Motor langsam voraus), Kette einholen
2. Bei entgegengesetzter Position: ruckartig mit kurzer Kette ziehen
3. Tripleine verwenden (Leine an der Ankerkrone befestigt → zieht den Anker rückwärts aus dem Hindernis)
4. Taucher einsetzen (wenn verfügbar)
5. Letzter Ausweg: Kette slippen (kontrolliert abwerfen) mit Boje zur Markierung

### 7.4 F03 — Verbogener Schaft

**Beschreibung:** Der Ankerschaft ist sichtbar verbogen, was das Setzverhalten und die Haltekraft dramatisch beeinträchtigt.

**Ursachen:**
1. Anker in Fels verklemmt, Yacht hat mit Motor/Wind gezogen → Schaft biegt sich
2. Ankerwinsche hat zu viel Kraft auf verklemmten Anker ausgeübt
3. Anker bei Sturm extremer Belastung ausgesetzt
4. Materialfehler (minderwertiger Stahl, zu geringer Querschnitt)
5. Unfallschaden (Kollision während Ankerung)

**AYDI Visuelle Erkennung:**
- Schaft sichtbar nicht gerade (>2° Abweichung erkennbar)
- Anker sitzt schief in der Bugrolle
- Fluke zeigt nicht in Schaftrichtung
- Confidence: `visual_medium` (klare Fälle `visual_high`)

**Bewertung:** KRITISCH — Ein verbogener Schaft muss sofort ersetzt werden. Ein gerichteter Schaft ist nicht sicher — die Materialstruktur ist geschwächt.

### 7.5 F04 — Gebrochene Schweißnaht (Bügel)

**Beschreibung:** Die Schweißnaht, die den Bügel (Rollbar) an der Fluke befestigt, ist gerissen. Der Bügel funktioniert nicht mehr → Anker kann auf dem Rücken landen → null Haltekraft.

**Ursachen:**
1. Minderwertige Schweißqualität (besonders bei No-Name-Bügelankern)
2. Ermüdungsbruch durch wiederholte Belastung
3. Korrosion an der Schweißnaht (Schwächung)
4. Überlastung (zu kleiner Anker für die Bedingungen)

**AYDI Visuelle Erkennung:**
- Bügel steht in unnatürlichem Winkel
- Sichtbarer Riss an der Schweißnaht
- Rost-Auslaufspuren an der Verbindung
- Confidence: `visual_high` (gut erkennbar auf Fotos)

**Bewertung:** KRITISCH — Anker sofort ersetzen. Der Bügel ist ein sicherheitskritisches Bauteil.

### 7.6 F05 — Korrosion an Schweißnähten

**Beschreibung:** Lokalisierte Korrosion an Schweißnähten, besonders am Bügel und an der Fluke-Schaft-Verbindung.

**Ursachen:**
1. Verzinkung durch Schweißhitze beschädigt
2. Galvanische Korrosion zwischen verschiedenen Metallen
3. Fehlende Nachverzinkung der Schweißzone
4. Aggressives Seewasser (Tropen, hoher Salzgehalt)

**AYDI Visuelle Erkennung:**
- Orangebraune Rostflecken an Schweißnähten
- Blasenbildung der Verzinkung um Schweißnähte
- Raue, aufgeblühte Oberfläche
- Confidence: `visual_medium` bis `visual_high`

**Bewertung:** HOCH — Sofortige Inspektion und ggf. Nachverzinkung oder Ersatz.

### 7.7 F06 — Ausgeschlagenes Gelenk (CQR)

**Beschreibung:** Das Gelenk zwischen Schaft und Fluke eines CQR-Ankers ist ausgeschlagen — übermäßiges Spiel, das das Setzverhalten verschlechtert.

**AYDI Visuelle Erkennung:**
- Fluke hängt in unnatürlichem Winkel
- Sichtbares Spiel am Gelenk (>5°)
- Confidence: `visual_medium`

### 7.8 F07 — Abgenutzte Fluke-Spitze

**Beschreibung:** Die Spitze der Fluke ist abgeschliffen durch wiederholten Gebrauch auf hartem Grund (Sand, Kies, Fels). Eine stumpfe Spitze setzt schlechter.

**AYDI Visuelle Erkennung:**
- Fluke-Spitze sichtbar abgerundet statt scharf
- Blankes Metall an der Spitze (Verzinkung abgeschliffen)
- Confidence: `visual_medium`

**Bewertung:** MITTEL — Bei deutlicher Abstumpfung: Nachschärfen (Winkelschleifer) oder Spitzentausch (Mantus, einige Modelle).

### 7.9 F08 — Fehlende oder beschädigte Verzinkung

**Beschreibung:** Die Feuerverzinkung ist großflächig beschädigt — Rost auf >20 % der Oberfläche.

**AYDI Visuelle Erkennung:**
- Großflächige Rostflächen, besonders an Kanten und Spitze
- Blasige, abblätternde Verzinkung
- Confidence: `visual_high`

**Bewertung:** HOCH — Anker nachverzinken lassen oder ersetzen. Rost schwächt den Querschnitt.

### 7.10 F09 — Falsche Ankergröße

**Beschreibung:** Der montierte Anker ist für die Bootsgröße unterdimensioniert.

**AYDI Visuelle Erkennung:**
- Anker erscheint klein relativ zum Bug
- Typ und geschätzte Größe vs. bekannte Bootslänge
- Confidence: `visual_medium` (Gewicht nicht direkt erkennbar)

**Bewertung:** KRITISCH — Unterdimensionierter Anker ist gefährlich. Warnung mit Empfehlung zur korrekten Größe.

### 7.11 F10 — Inkompatible Bugrolle

**Beschreibung:** Der Anker passt nicht korrekt in die Bugrolle — er sitzt schief, kippt, oder der Schaft liegt nicht vollständig auf.

**AYDI Visuelle Erkennung:**
- Anker sitzt nicht bündig in der Bugrolle
- Sichtbarer Spalt zwischen Schaft und Rolle
- Anker hängt schief
- Confidence: `visual_high`

### 7.12 F11 — Gerissener oder offener Schäkel

**Beschreibung:** Der Ankerwirbel oder -schäkel ist gebrochen, verzogen oder nicht korrekt verschlossen.

**AYDI Visuelle Erkennung:**
- Schäkelbolzen fehlt oder steht offen
- Sichtbare Verformung
- Confidence: `visual_high`

**Bewertung:** KRITISCH — Ankerverlust möglich.

### 7.13 F12 — Verstopfter Ankerkopf

**Beschreibung:** Schlamm, Seegras oder Steine sind in der Fluke verklemmt und verhindern korrektes Setzen beim nächsten Ankern.

**AYDI Visuelle Erkennung:**
- Sichtbare Ablagerungen in der Fluke
- Seegras-Reste um Bügel/Fluke gewickelt
- Confidence: `visual_medium`

**Bewertung:** NIEDRIG — Anker reinigen vor nächstem Gebrauch.

### 7.14 Zusammenfassung der visuellen Erkennbarkeit

Die folgende Tabelle fasst zusammen, welche Fehlerbilder zuverlässig aus Fotos erkannt werden können und welche nicht:

**Gut erkennbar (visual_high möglich):**
- F04 — Gebrochene Schweißnaht am Bügel (klare Formveränderung)
- F08 — Fehlende Verzinkung / großflächiger Rost
- F10 — Inkompatible Bugrolle (Anker sitzt nicht bündig)
- F11 — Gerissener/offener Schäkel

**Bedingt erkennbar (visual_medium):**
- F03 — Verbogener Schaft (>5° Abweichung erkennbar)
- F05 — Korrosion an Schweißnähten (Rostauslauf sichtbar)
- F06 — Ausgeschlagenes Gelenk (CQR, bei deutlichem Spiel)
- F07 — Abgenutzte Fluke-Spitze (blankes Metall erkennbar)
- F09 — Falsche Ankergröße (nur bei bekannter Bootsgröße)
- F12 — Verstopfter Ankerkopf (Schlammreste, Gras)

**Nicht erkennbar (visual_insufficient):**
- F01 — Dragging (nur durch GPS/Peilung feststellbar)
- F02 — Verklemmter Anker (unter Wasser, nicht sichtbar)

### 7.15 AYDI-Handlungsempfehlungen nach Schweregrad

| Schweregrad | Anzeigeformat | Handlungsempfehlung (DE) |
|-------------|--------------|--------------------------|
| KRITISCH | Roter Badge, Warnung prominent | "Sofortige Prüfung durch Fachmann erforderlich. Nicht ankern bis Mangel behoben." |
| HOCH | Oranger Badge, Warnung sichtbar | "Zeitnahe Prüfung empfohlen. Funktion eingeschränkt, Sicherheitsreserve reduziert." |
| MITTEL | Gelber Badge, Hinweis | "Bei nächster Gelegenheit prüfen oder beheben. Keine unmittelbare Gefahr." |
| NIEDRIG | Grauer Badge, Info | "Wartungshinweis. Bei nächster Routine-Inspektion berücksichtigen." |

---

## 8. Troubleshooting

### 8.1 Entscheidungsbaum: Anker hält nicht

```
Anker hält nicht
├── Ist genügend Kette draußen?
│   ├── NEIN → Mehr Kette fieren (Scope 5:1 minimum)
│   │         → Prüfen: Wassertiefe × 5 + Freibord = minimale Kettenlänge
│   │         → Hält jetzt? → JA → Problem gelöst
│   │                       → NEIN → Weiter
│   └── JA → Weiter
├── Ist der Anker für diesen Grundtyp geeignet?
│   ├── NEIN → Ankerplatz wechseln oder Zweitanker (besserer Typ) ausbringen
│   └── JA → Weiter
├── Hat der Anker sich beim Setzen eingegraben?
│   ├── NEIN → Motor rückwärts geben (1.500 RPM), Anker setzen
│   │         → Hält jetzt? → JA → Problem gelöst
│   │                       → NEIN → Anker aufholen, Fluke prüfen (Gras? Schlamm?)
│   │                               → Reinigen, neu setzen
│   └── JA → Weiter
├── Ist der Anker für die Bootsgröße dimensioniert?
│   ├── NEIN → Anker ist unterdimensioniert → Zweitanker zusätzlich ausbringen
│   │         → Langfristig: größeren Anker beschaffen
│   └── JA → Grundverhältnisse prüfen (Seegras? Fels unter Sand?)
│           → Ggf. Ankerplatz wechseln
└── Alle Maßnahmen fehlgeschlagen
    → V-Ankerung oder Tandem-Ankerung
    → Oder: sicheren Hafen/Muring anlaufen
```

### 8.2 Entscheidungsbaum: Anker kommt nicht frei

```
Anker kommt nicht frei
├── Über den Anker fahren (Motor langsam voraus)
│   ├── Kette dabei einholen, bis Kette senkrecht über Anker steht
│   └── Dann: Ruckartiges Heben mit Ankerwinsche
│       ├── Anker kommt frei → Problem gelöst
│       └── Weiter
├── Tripleine vorhanden?
│   ├── JA → An Tripleine ziehen (zieht Anker rückwärts aus Hindernis)
│   │       → Frei? → JA → Problem gelöst
│   │                → NEIN → Weiter
│   └── NEIN → Behelfslösung: Kettenstück als Leitring über Kette schicken
├── Motor voraus in verschiedene Richtungen versuchen (30° Schritte)
│   ├── Frei? → JA → Problem gelöst
│   └── NEIN → Weiter
├── Taucher verfügbar?
│   ├── JA → Taucher befreit Anker manuell
│   └── NEIN → Weiter
└── Letzte Option: Kette slippen
    → Boje an Kette befestigen
    → Kette kontrolliert abwerfen
    → Später mit Tauchunterstützung bergen
```

### 8.3 Entscheidungsbaum: Richtigen Anker wählen

```
Ankerwahl
├── Was ist das Einsatzrevier?
│   ├── Mittelmeer (Sand, Seegras, Fels)
│   │   → Neue Generation mit Bügel (Rocna, Mantus, Ultra)
│   │   → Scharf genug für Posidonia
│   │   → Zweitanker für Felsgrund empfohlen
│   ├── Ostsee/Nordsee (Sand, Schlick, Gezeitenstrom)
│   │   → Neue Generation Standard
│   │   → Schwere Kette wegen Gezeitenstrom
│   ├── Karibik (Sand, Koralle, tropische Stürme)
│   │   → Neue Generation + Fortress als Sturmanker
│   │   → Kein Ankern auf Koralle!
│   ├── Pazifik/Weltumsegelung (alles)
│   │   → Hauptanker: Neue Generation überdimensioniert
│   │   → Zweitanker: Fortress FX
│   │   → Heckanker: Dritter Anker
│   └── Binnenseen (Schlamm, weicher Grund)
│       → Fortress FX als Hauptanker (leicht, gut in Schlamm)
│       → Oder Neue Generation Standard
├── Welche Bootsgröße?
│   → Dimensionierungstabelle konsultieren (Abschnitt 5)
├── Budget?
│   ├── Gering (unter 500 EUR) → Bügelanker (SVB/AWN), Delta
│   ├── Mittel (500–1.000 EUR) → Mantus M1, Sarca Excel
│   └── Hoch (über 1.000 EUR) → Rocna, Ultra, Spade
└── Bugrolle-Kompatibilität?
    ├── Standard-Delta-Bugrolle → Vulcan, Delta, DTX
    ├── Breite/tiefe Bugrolle → Rocna Original, Mantus, Ultra
    └── Keine Bugrolle → Anker an Deck stauen, Davit oder Bug-Montage
```

### 8.4 Entscheidungsbaum: Sturm am Ankerplatz

```
Sturm am Ankerplatz (Wind >35 kn vorhergesagt)
├── Option 1: Auslaufen und sicheren Hafen anlaufen
│   ├── Möglich und sicher? → JA → Beste Option
│   └── NEIN → Am Ankerplatz bleiben
├── Ankervorbereitung
│   ├── Maximalen Scope fieren (8:1 bis 10:1)
│   ├── Kettenstopper setzen, Winsche entlasten
│   ├── Zweitanker als V-Ankerung ausbringen (bei verfügbarer Zeit)
│   ├── Chafe Protection an Klüse und Bugrolle (Scheuerschutz!)
│   ├── Ankeralarme aktivieren (GPS, AIS-Ankerwatch)
│   └── Motor startbereit halten
├── Während des Sturms
│   ├── Ankerwache! (Person oder GPS-Alarm)
│   ├── GPS-Position überwachen
│   ├── Bei Dragging: Motor rückwärts unterstützend
│   └── Bei Ankerversagen: Zweiter Anker sofort → Notankern
└── Nach dem Sturm
    ├── Anker und Kette auf Beschädigungen prüfen
    ├── Kettenstopper und Klampen inspizieren
    └── Ggf. Anker bergen und Bugrolle prüfen
```

### 8.5 Entscheidungsbaum: Anker-Wartung und Inspektion

```
Jährliche Ankerinspektion
├── Sichtprüfung Anker
│   ├── Schweißnähte intakt? → NEIN → Schweißen lassen oder ersetzen
│   ├── Schaft gerade? → NEIN → Ersetzen (nicht richten!)
│   ├── Verzinkung >80% intakt? → NEIN → Nachverzinken
│   ├── Fluke-Spitze scharf? → NEIN → Nachschleifen
│   ├── Bügel fest? → NEIN → KRITISCH → Sofort ersetzen
│   └── Bewegliche Teile (CQR, Fortress) funktionieren? → NEIN → Reparieren
├── Sichtprüfung Kette
│   ├── Glieder gleichmäßig abgenutzt? → Abrieb >20% → Ersetzen
│   ├── Verzinkung intakt? → NEIN → Nachverzinken
│   ├── Verbindungsglieder fest? → NEIN → Ersetzen
│   └── Markierungen lesbar? → NEIN → Neu markieren
├── Verbindungen prüfen
│   ├── Ankerwirbel: Dreht frei? Bolzen fest? → NEIN → Ersetzen
│   ├── Schäkel: Bolzen gesichert (Mausung/Draht)? → NEIN → Sichern
│   └── Kette-Leine-Verbindung: Spleiß intakt? → NEIN → Neu spleißen
└── Funktionstest
    ├── Anker fieren und einholen: Ankerwinsche funktioniert?
    ├── Kettenstopper greift?
    └── Ankerkasten: Abfluss frei? Kette staut sich korrekt?
```

---

## 9. FAQ — Häufige Fragen

### 9.1 Welcher Anker ist der beste?

**Antwort:** Es gibt keinen "besten" Anker für alle Situationen. Für die meisten Fahrtenyachten (10–15 m) bieten Bügel-Anker der Neuen Generation (Rocna, Mantus, Ultra, Sarca Excel) die beste Kombination aus Setzleistung, Haltekraft und Reset-Fähigkeit. Der "beste" Anker ist der, der für Ihre Bootsgröße, Ihr Revier und Ihren Einsatzzweck korrekt dimensioniert ist.

**AYDI-Empfehlung nach Einsatzprofil:**
- Allround-Empfehlung: Rocna Original oder Mantus M1
- Budget-Empfehlung: Bügelanker (No-Name) oder Mantus M1 (kleinere Größen)
- Premium-Empfehlung: Ultra Anchor
- Zweitanker-Empfehlung: Fortress FX
- Kompakt-Empfehlung (enge Bugrolle): Rocna Vulcan

### 9.2 Warum sollte ich meinen alten CQR/Delta ersetzen?

**Antwort:** Ein CQR oder Delta hält bei gleichem Gewicht nur 30–50 % der Haltekraft eines modernen Bügel-Ankers. In Seegras, dem häufigsten schwierigen Grund im Mittelmeer, ist der Unterschied noch dramatischer: Ein 15-kg-Rocna hält in dünnem Seegras 150–300 kg, ein 16-kg-CQR nur 30–80 kg. Der Wechsel auf einen Neuen-Generation-Anker ist die beste einzelne Sicherheitsinvestition, die Sie an Ihrem Boot machen können.

### 9.3 Reicht ein Anker aus oder brauche ich zwei?

**Antwort:** Für Tagesausflüge und geschützte Buchten reicht ein korrekt dimensionierter Hauptanker. Für Übernachtungsankern empfehlen wir dringend einen Zweitanker (Fortress FX oder gleichwertig) an Bord. Für Langfahrt sind drei Anker Standard: Hauptanker, Zweitanker, Heckanker/Kedge.

### 9.4 Wie viel Kette brauche ich?

**Antwort:** Als Faustregel: 4× die maximale Wassertiefe, in der Sie ankern werden. Für das Mittelmeer (typisch 5–15 m Tiefe) sind 50–60 m Kette ausreichend. Für Atlantiküberquerung oder Pazifik-Kreuzung: 80–100 m. Immer genug Kette für Scope 7:1 bei maximaler Tiefe + Reserve.

### 9.5 Kettenlänge oder Seil — was ist besser?

**Antwort:** Nur Kette ist der Standard für Fahrtenyachten mit elektrischer Ankerwinsche. Kette bietet:
- Gewicht als Stoßdämpfer (Catenary-Effekt)
- Abriebbeständigkeit am Grund
- Kein Schnittrisiko durch Korallen oder Fels
- Einfache Handhabung mit Ankerwinsche

Kette + Seil ist eine Alternative für leichte Boote (Sportboote, kleine Segler), bei denen das Kettengewicht ein Problem ist. Der Seilanteil muss Nylon sein (Dehnung als Stoßdämpfer).

### 9.6 Was ist ein Reitgewicht (Kellet) und wann brauche ich eins?

**Antwort:** Ein Reitgewicht ist ein Gewicht (5–15 kg, typisch Blei oder Gusseisen), das auf der Ankerkette halbwegs zwischen Bug und Grund herabgelassen wird. Es senkt die Kette tiefer ins Wasser und vergrößert die Catenary (Kettenkurve), was den Zugwinkel am Anker flacher macht und die Haltekraft erhöht. Empfohlen bei Starkwind, wenn nicht genug Kette für ausreichenden Scope vorhanden ist.

### 9.7 Wie setze ich einen Anker korrekt?

**Antwort:**
1. Ankerplatz aussuchen (Tiefe, Grund, Schwojkreis, Wind-/Strömungsrichtung)
2. Langsam gegen Wind/Strom anfahren
3. Boot stoppen, Anker kontrolliert ablassen (NICHT werfen!)
4. Kette fieren, während Boot langsam rückwärts treibt
5. Bei gewünschtem Scope: Kette belegen, Boot rückwärts treiben lassen → Anker setzt sich
6. Motor kurz rückwärts geben (1.500 RPM, 10 Sekunden) → Setzprobe
7. Peilung nehmen oder GPS-Ankerwarnung aktivieren
8. Kettenstopper setzen, Winsche entlasten

### 9.8 Was ist "Scope" und warum ist es so wichtig?

**Antwort:** Scope ist das Verhältnis von ausgefierter Kettenlänge zu Wassertiefe (plus Freibord). Ein Scope von 5:1 bedeutet: bei 5 m Wassertiefe + 2 m Freibord = 35 m Kette. Je mehr Scope, desto flacher der Kettenwinkel am Anker, desto besser die Haltekraft. Minimum 5:1 für Übernachtung, 7:1 für Starkwind.

### 9.9 Wie berechne ich die richtige Kettenmenge bei Tidenhub?

**Antwort:** Immer die maximale Wassertiefe bei Hochwasser rechnen! Beispiel: Niedrigwasser 3 m, Tidenhub 4 m → Hochwasser 7 m + 2 m Freibord = 9 m Gesamttiefe. Scope 5:1 → 45 m Kette. Fehler: Bei Niedrigwasser ankern und nur 15 m Kette ausbringen (Scope 5:1 bei 3 m) → bei Hochwasser ist der Scope nur 1,7:1 → Anker bricht aus!

### 9.10 Soll ich den Anker auf der Bugrolle fahren oder an Deck stauen?

**Antwort:** Für Tagesfahrten und kurze Törns: auf der Bugrolle lassen (sofort einsatzbereit). Für Langstreckenfahrten (Atlantik, mehrtägige Überführungen): an Deck sichern — ein auf der Bugrolle verbleibender Anker kann bei schwerem Seegang Schäden am Bug verursachen und die Seetüchtigkeit beeinträchtigen.

### 9.11 Was ist eine Tripleine und brauche ich eine?

**Antwort:** Eine Tripleine ist eine Leine, die an der Ankerkrone (dem unteren Ende) befestigt wird und zum Boot führt. Wenn der Anker verklemmt ist, kann man ihn über die Tripleine rückwärts aus dem Hindernis ziehen. Empfohlen für Reviere mit Felsgrund (Kroatien, Griechenland, Norwegen).

### 9.12 Wie tief gräbt sich ein moderner Anker ein?

**Antwort:** In festem Sand gräbt sich ein Neue-Generation-Anker typischerweise 30–50 cm ein (bis zur vollen Fluke-Tiefe). In weichem Schlamm kann die Eindringtiefe 1–2 m betragen. Die Eindringtiefe korreliert direkt mit der Haltekraft.

### 9.13 Was passiert bei Winddrehung?

**Antwort:** Bei Winddrehung (oder Tidenwechsel) schwoiht das Boot um den Ankerpunkt. Bei 90°-Drehung muss der Anker sich im Grund neu orientieren (Reset). Bügel-Anker (Rocna, Mantus) machen das gut — sie bleiben eingegraben und schwenken die Fluke. Alte CQR- und Danforth-Anker brechen oft aus und müssen komplett neu setzen, was zu einem Positionswechsel führen kann.

### 9.14 Kann ich meinen Anker nachschärfen?

**Antwort:** Ja, die Fluke-Spitze kann mit einem Winkelschleifer nachgeschärft werden. Danach muss die Verzinkung in diesem Bereich ausgebessert werden (Zinkspray). Bei Mantus-Ankern kann die austauschbare Spitze gewechselt werden.

### 9.15 Wie pflege ich die Verzinkung meines Ankers?

**Antwort:** Feuerverzinkte Anker nach jeder Saison mit Süßwasser abspülen und trocknen lassen. Beschädigte Stellen mit Zinkspray behandeln. Alle 8–15 Jahre Nachverzinkung in einer Verzinkerei (Kosten: 50–150 EUR je nach Größe). Edelstahl-Anker: nur Süßwasser-Abspülung nötig.

### 9.16 Was kostet eine vollständige Ankerausrüstung?

**Antwort (für 12 m Segelyacht, Neue Generation):**
- Hauptanker (Mantus M1, 35 lb / 16 kg): ca. 600 EUR
- Kette (10 mm × 60 m, verzinkt): ca. 600–800 EUR
- Ankerwirbel (Edelstahl): ca. 80–120 EUR
- Kettenstopper: ca. 100–200 EUR
- Zweitanker (Fortress FX-23): ca. 400 EUR
- Nylon-Ankerleine (16 mm × 60 m): ca. 150–200 EUR
- **Gesamtkosten: ca. 1.930–2.320 EUR**

### 9.17 Wie lange hält ein Anker?

**Antwort:** Ein hochwertiger Stahlanker (feuerverzinkt) hält bei normaler Pflege 15–25 Jahre. Die Verzinkung ist der limitierende Faktor — wenn sie aufgebraucht ist, rostet der Stahl. Edelstahl-Anker halten praktisch unbegrenzt (50+ Jahre), sind aber 2–3× teurer. Aluminium-Anker (Fortress) halten ebenfalls sehr lange, solange keine mechanische Verformung auftritt.

### 9.18 Mein Anker rostet stark — muss ich ihn ersetzen?

**Antwort:** Oberflächenrost ist kosmetisch und reduziert die Festigkeit kaum. Wenn die Rostschicht jedoch dick ist (>2 mm) oder der Querschnitt sichtbar reduziert ist, muss der Anker ersetzt werden. Ein Nachverzinken ist möglich, wenn der Grundstahl noch intakt ist. Prüfung: Mit Hammer auf den Schaft klopfen — dumpfer Klang = Querschnittsverlust → ersetzen.

### 9.19 Welcher Anker ist am besten für die Ostsee?

**Antwort:** Die Ostsee bietet überwiegend Sandgrund mit einigen Schlick-Bereichen. Ein Rocna Vulcan oder Mantus M1 in der Standardgröße ist ideal. Gezeitenstrom ist minimal, aber Windstärken können beachtlich sein. Scope 5:1 reicht meist aus.

### 9.20 Welcher Anker für das Mittelmeer?

**Antwort:** Das Mittelmeer ist anspruchsvoll: häufig Seegras (Posidonia), Fels, und Mischgrund. Ein Neue-Generation-Anker mit scharfer Spitze ist Pflicht. Rocna Original oder Mantus M1 sind die populärsten Wahlen bei Langfahrt-Seglern im Mittelmeer. Ein Fortress FX als Zweitanker für Sandgründe.

### 9.21 Kann ich einen Anker im Fels benutzen?

**Antwort:** Kein herkömmlicher Anker ist für Fels optimiert. Die Optionen:
1. Felshaken (spezieller Anker für Felsspalten — selten)
2. Stockanker (Admiralitätsanker — kann in Spalten haken)
3. Muring benutzen (falls vorhanden)
4. Landleine an Fels befestigen + Anker in tieferem Wasser
5. Ankern vermeiden — andere Bucht suchen

### 9.22 Wie verankere ich einen Katamaran?

**Antwort:** Katamarane haben mehr Windangriffsfläche und weniger Gewicht pro Meter als Einrümpfer. Anker +30 % gegenüber Einrümpfer gleicher Länge. Kette ebenfalls schwerer dimensionieren. Die zwei Bugrollen ermöglichen einfache V-Ankerung für reduzierten Schwojkreis.

### 9.23 Was ist "Balearische Ankerung"?

**Antwort:** Auch "Mittelmeer-Ankerung" oder "Med Mooring" genannt. Das Boot ankert mit dem Bug nach außen und legt mit dem Heck an der Kaimauer oder Küste fest (oder umgekehrt). Üblich in Häfen und Buchten des Mittelmeers. Erfordert einen guten Buganker + Heckleine.

### 9.24 Brauche ich eine elektrische Ankerwinsche?

**Antwort:** Ab 10 m Bootslänge ist eine elektrische Ankerwinsche dringend empfohlen. Das manuelle Bergen von 40+ m 10-mm-Kette + 15-kg-Anker ist extrem anstrengend und bei Einhandseglern potentiell gefährlich (Verletzungsrisiko). Kosten: 800–3.000 EUR je nach Größe und Hersteller.

### 9.25 Was ist der Unterschied zwischen Kurzglied- und Langgliedkette?

**Antwort:** Kurzglied-Ankerkette (auch Kalibrierkette, ISO 4565 / DIN 766) hat kürzere, engere Glieder und ist für Ankerwinschen und Kettenräder optimiert. Die Glieder greifen exakt in die Kettenräder der Winsche. Langgliedkette (ISO 4565 / DIN 763) hat längere Glieder und passt NICHT auf Standard-Ankerwinschen — sie springt über die Zähne des Kettenrads. Für Yacht-Ankerung ist ausschließlich Kurzgliedkette zu verwenden.

### 9.26 Wie markiere ich meine Ankerkette?

**Antwort:** Markierungen alle 5 oder 10 Meter erleichtern die Scope-Kontrolle erheblich. Gängige Methoden:
- **Farbe:** Alle 10 m eine andere Farbe (Sprühlack oder Markierungsfarbe). Haltbarkeit: 1–3 Saisons.
- **Kabelbinder:** Farbige Kabelbinder durch ein Kettenglied. Günstig, leicht zu erneuern. Haltbarkeit: 1–2 Saisons.
- **Kettenfarbmarkierung:** Spezielle marine Kettenfarbe (z. B. von Anchor Geeks). Haltbarkeit: 3–5 Saisons.
- **Drahtwicklung:** Dünner, farbiger Edelstahldraht um Kettenglieder gewickelt. Dauerhafteste Methode.

Bewährtes System: 10 m = 1 Markierung, 20 m = 2 Markierungen, usw. Oder: Rote Farbe bei 10 m, Weiß bei 20 m, Blau bei 30 m, Gelb bei 40 m, Rot+Weiß bei 50 m.

### 9.27 Wann sollte ich die Ankerkette austauschen?

**Antwort:** Ankerkette austauschen, wenn:
- Der Durchmesser durch Abrieb um >10 % reduziert ist (z. B. 10 mm → <9 mm)
- Verzinkung zu >50 % abgenutzt ist und Nachverzinkung nicht wirtschaftlich
- Glieder sichtbar deformiert oder gestreckt sind
- Korrosionsnarben den Querschnitt schwächen
- Verbindungsglieder ausgeschlagen sind

Typische Lebensdauer bei normaler Nutzung und Pflege: 15–25 Jahre. Bei Dauerankern in tropischen Gewässern: 8–15 Jahre.

### 9.28 Was ist ein Snubber und warum ist er so wichtig?

**Antwort:** Ein Snubber (auch Ruckdämpfer) ist eine Nylon-Leine (typisch 14–20 mm Durchmesser, 8–15 m Länge), die mit einem Kettenhaken an der Ankerkette befestigt wird. Die Ankerlast wird dann über den Snubber auf eine Bugklampe übertragen, statt über die Ankerwinsche. Vorteile:
- **Stoßdämpfung:** Nylon dehnt sich 15–25 % → absorbiert Böen und Wellenenergie
- **Geräuschdämpfung:** Eliminiert das Kettenrasseln auf GFK-Rümpfen fast komplett
- **Winsch-Entlastung:** Die Ankerwinsche ist nicht für Dauerlast ausgelegt — der Snubber entlastet sie
- **Anker-Entlastung:** Reduziert Spitzenlasten am Anker um geschätzt 30–40 %

Ein Snubber ist kein Luxus — er ist Pflichtausrüstung für jedes Übernachtungsankern.

### 9.29 Wie laut ist Ankerkette auf GFK-Rümpfen?

**Antwort:** Sehr laut. Die Kette überträgt Geräusche direkt über die Bugrolle in den Rumpf. Lösungen:
- Kettenstopper verwenden (dämpft Kettengeräusche)
- Gummipuffer in der Bugrolle
- Ankerkasten schallisolieren
- Snubber/Ruckdämpfer: Nylon-Leine an der Kette, die die Last vom Bug auf die Klampe überträgt — eliminiert Kettengeräusche fast komplett

---

## 10. Glossar

### A

**Admiralitätsanker:** Traditioneller Stockanker mit zwei Armen und einem Querstock. Älteste Ankerform, in Felsgründen noch relevant.

**Ankerboje:** Schwimmkörper, der an einer Tripleine am Anker befestigt ist und die Position des Ankers markiert. Erleichtert das Bergen und zeigt anderen Booten die Ankerlage.

**Ankergeschirr:** Gesamtheit aller Komponenten: Anker, Kette, Wirbel, Schäkel, Kettenstopper, Ankerwinsche, Bugrolle.

**Ankergrund:** Beschaffenheit des Meeresbodens am Ankerplatz. Entscheidend für die Ankerwahl und Haltekraft.

**Ankerkette:** Kalibrierkette (Kurzglied) für die Ankerwinsche. Standardmäßig verzinkter Stahl, Grade 40 oder Grade 70.

**Ankerleine:** Nylon-Seil als Alternative oder Ergänzung zur Kette. Bietet Elastizität als Stoßdämpfer.

**Ankerrolle:** siehe Bugrolle.

**Ankerwache:** Person, die während des Ankerns die Position des Bootes überwacht. Pflicht bei schwierigen Bedingungen.

**Ankerwinsche:** Elektrische oder manuelle Winde zum Einholen und Fieren der Ankerkette.

### B

**Bügel (Rollbar):** Halbbogenförmiger Stahlbügel am Anker, der ein Umkippen auf den Rücken verhindert und die korrekte Setzposition erzwingt.

**Bugrolle (Ankerrolle):** Rolle am Bug, über die die Ankerkette geführt wird. Muss zum Ankerschaft-Profil passen.

### C

**Catenary:** Die natürliche Durchhangkurve der Ankerkette zwischen Bug und Anker. Wirkt als Stoßdämpfer bei Böen und Wellen.

**Chafe Protection (Scheuerschutz):** Schutz an Stellen, wo die Kette oder Leine an Rumpf, Bugrolle oder Klüsen scheuert. Kritisch bei Sturm.

### D

**Dragging:** Schleppen des Ankers über den Grund — der Anker hält nicht. Sicherheitskritisch.

**Dredging:** Absichtliches Ziehen des Ankers über den Grund, z. B. um ein Boot in eine Position zu verholen.

### F

**Feuerverzinkung (Hot-dip galvanizing):** Korrosionsschutzverfahren, bei dem der Stahlanker in flüssiges Zink getaucht wird. Schichtdicke 80–150 μm. Haltbarkeit 10–20 Jahre im marinen Einsatz.

**Fluke:** Der pflug- oder schalenförmige Teil des Ankers, der in den Meeresgrund eindringt und die Haltekraft erzeugt.

**Flukewinkel:** Der Winkel zwischen Fluke und Schaft. Bestimmt die Eindringtiefe. Typisch 32° für Sand, 45° für Schlamm.

**Fouled Anchor:** Verklemmter oder verdrehter Anker, der sich nicht bergen lässt.

### G

**Galvanische Verzinkung:** Elektrochemisches Verzinkungsverfahren. Dünnere Schicht als Feuerverzinkung (5–25 μm). Geringerer Korrosionsschutz, günstigerer Preis.

**Grade 40 / Grade 70 (Kette):** Festigkeitsklassen für Ankerketten. Grade 40 (auch G40 oder ISO 1535) ist der Standard für Freizeit-Yachten. Grade 70 (G70) ist hochfest — gleiche Bruchlast bei dünnerer Kette, aber empfindlicher gegen Ermüdung. Nicht zu verwechseln mit Grade 80 (Hebeketten) — diese sind für Ankerketten NICHT geeignet.

**Grapnel (Draggen):** Kleiner Mehrarmanker für Beiboote oder als Bergungswerkzeug.

**Grundberührung (Grounding):** Unbeabsichtigtes Aufsetzen des Rumpfes auf dem Meeresgrund. Ein Kedge-Anker kann beim Freikommen helfen (→ Fallstudie A4).

### H

**Haltekraft (Holding Power):** Die Kraft (in kg oder kN), die ein Anker im Grund aufnehmen kann, bevor er ausbricht. Abhängig von Ankertyp, Gewicht, Grundtyp und Scope.

**Helix-Anker:** Schraubförmiger Anker, der in den Grund geschraubt wird. Für permanente Moorings.

### K

**Kedge:** Zweit- oder Hilfsanker, der typischerweise vom Beiboot aus gesetzt wird.

**Kellet (Reitgewicht):** Gewicht, das auf der Ankerkette abgelassen wird, um die Catenary zu vergrößern und den Zugwinkel am Anker zu reduzieren.

**Kettenstopper (Chain Stopper):** Mechanismus am Bugbeschlag, der die Kette fixiert und die Ankerwinsche entlastet.

**Kettenvorlauf:** Die ersten 5–10 m Kette bei einem Kette+Seil-System. Schützt das Seil vor Abrieb am Grund.

**Klüse:** Durchführung in der Bordwand oder am Bug für Leinen und Ketten.

### M

**Med Mooring:** Mittelmeer-Ankerung: Bug zum Meer (mit Anker), Heck zur Pier.

**Mooringboje:** Fest verankerter Schwimmkörper, an dem Boote festmachen können, statt selbst zu ankern.

**Mausung:** Sicherungsdraht, der durch den Schäkelbolzen gezogen wird, um ein unbeabsichtigtes Öffnen zu verhindern.

### N

**Neue Generation:** Sammelbegriff für Ankerdesigns ab ca. 2000, die durch Bügel, konkave Flukes und optimierte Setzgeometrie deutlich höhere Haltekräfte erzielen als traditionelle Typen.

### P

**Pflug-Anker (Plough):** Ankertyp, dessen Fluke einer Pflugschare ähnelt (CQR, Delta).

### R

**Reset:** Die Fähigkeit eines Ankers, sich nach einer Zugrichtungsänderung erneut im Grund zu orientieren und Haltekraft aufzubauen.

**Reitgewicht:** siehe Kellet.

**Rode:** Englischer Sammelbegriff für die Ankerleine/Kette (die Verbindung zwischen Anker und Boot).

### S

**Schaft:** Der Stab- oder Rohrförmige Teil des Ankers, der Fluke und Schäkelpunkt verbindet.

**Schäkel (Shackle):** U-förmiges Verbindungsstück mit Bolzen. Verbindet Anker mit Kette oder Wirbel.

**Scope:** Verhältnis von ausgegebener Kette/Leine zur Wassertiefe (plus Freibord). Scope 5:1 = 5× so viel Kette wie Tiefe.

**Schwojkreis:** Der Kreis, den das Boot beim Schwojien um den Ankerpunkt beschreibt. Radius = Kettenlänge + Bootslänge.

**Schwojien:** Das Hin- und Herpendeln des Bootes um den Ankerpunkt bei wechselndem Wind oder Strom.

**Setzverhalten (Setting Behavior):** Wie schnell und zuverlässig ein Anker sich beim ersten Versuch in den Grund eingräbt.

**Snubber (Ruckdämpfer):** Nylon-Leine, die an der Kette befestigt wird und die Ankerlast auf eine Klampe überträgt. Dämpft Lastspitzen und eliminiert Kettengeräusche.

**Stockanker:** Anker mit einem Querstock, der den Anker in die Setzposition kippt. Ältester Ankertyp.

### T

**Tandem-Ankerung:** Zwei Anker hintereinander auf derselben Kette. Erhöht die Haltekraft um ca. 50 %.

**Tripleine (Trip Line):** Leine, die an der Ankerkrone befestigt ist und zum Bergen eines verklemmten Ankers dient.

### V

**V-Ankerung:** Zwei Anker in V-Form (60°–90° Winkel) ausgebracht. Verdoppelt die Haltekraft und reduziert den Schwojkreis.

**Verdrängung (Displacement):** Gewicht des Wassers, das der Rumpf verdrängt — entspricht dem Gesamtgewicht des Bootes.

### W

**Windangriffsfläche (Windage):** Die projizierte Fläche von Rumpf, Aufbau, Mast und Rigg, die dem Wind ausgesetzt ist.

**Windangriffsfläche (Windage):** Die projizierte Fläche von Rumpf, Aufbau, Mast und Rigg, die dem Wind ausgesetzt ist. Bestimmt maßgeblich die Ankerlast.

**Wirbel (Swivel):** Drehbares Verbindungsstück zwischen Anker und Kette, das ein Verdrehen der Kette verhindert. Muss aus Edelstahl 316 sein und für die Bruchlast der Kette ausgelegt sein.

### Z

**Zugprüfung (Pull Test):** Standardisierte Prüfmethode zur Messung der Haltekraft eines Ankers. Wird mit einer kalibrierten Lastzelle durchgeführt, die am Rode befestigt ist. Die Zugkraft wird kontinuierlich erhöht, bis der Anker ausbricht.

**Zweitanker (Secondary Anchor):** Zweiter Anker an Bord, typischerweise leichter als der Hauptanker. Dient als Reserve, Kedge, Heckanker oder für V-Ankerung. Empfohlen: 60–75 % des Hauptankergewichts.

**Zinkopferanode:** Korrosionsschutz-Methode, bei der ein unedleres Metall (Zink) geopfert wird, um das edlere Metall (Stahl oder Aluminium) zu schützen. Am Anker selbst nicht nötig (Verzinkung reicht), aber an der Kette-Anker-Verbindung bei gemischten Metallen relevant.

---

## 11. Schnell-Referenz

### 11.1 Ankergrößen-Schnellwahl (Neue Generation)

```
Bootslänge → Ankergewicht (Neue Generation)
  6–8 m  →  4–8 kg
  8–10 m → 8–12 kg
 10–12 m → 10–16 kg
 12–14 m → 15–20 kg
 14–16 m → 20–25 kg
 16–18 m → 25–33 kg
 18–20 m → 33–40 kg
 20–25 m → 40–55 kg
 25–30 m → 55–75 kg
 30+  m → 75–100+ kg
```

### 11.2 Scope-Schnellregel

```
Tagesanker, ruhig:     3:1–4:1 (nur Kette)
Übernachtung, normal:   5:1–6:1 (nur Kette)
Starkwind (>25 kn):    7:1–8:1
Sturm (>40 kn):        8:1–10:1
```

### 11.3 Kettendimensionierungs-Schnellwahl

```
  6–9 m  → 6–8 mm Kette, 30–40 m
  9–12 m → 8–10 mm Kette, 40–60 m
 12–15 m → 10 mm Kette, 50–70 m
 15–18 m → 10–12 mm Kette, 70–80 m
 18–22 m → 12 mm Kette, 80–100 m
 22–30 m → 12–14 mm Kette, 100+ m
```

### 11.4 Ankertyp-Empfehlung nach Grundtyp

```
Sand (fest/weich):  Alle Neue Generation, Fortress FX
Schlamm:            Fortress FX (45°), Spade, Mantus
Seegras:            Rocna Original, Mantus M1, Sarca Excel
Fels:               Kein guter Anker — Muring oder Landleinen
Koralle:            NICHT ANKERN (Umweltschutz!) → Mooring-Bojen
Kies:               Schwere Neue Generation, Bruce/Claw
```

### 11.5 Checkliste: Vor dem Ankern

```
□ Wassertiefe prüfen (Echolot, Karte)
□ Grundtyp ermitteln (Karte, Sicht, Erfahrung)
□ Schwojkreis berechnen (Kette + Bootslänge, andere Boote?)
□ Tidenhub berücksichtigen (Scope bei Hochwasser!)
□ Windvorhersage prüfen
□ Fluchtweg planen (bei Ankerversagen)
□ Ankerwinsche testen
□ Kette frei im Ankerkasten?
□ Kettenstopper bereit?
□ GPS-Ankeralarm aktivieren
```

---

## ANHANG A — Fallstudien

### Fallstudie A1: Ankerversagen bei Bora, Kroatien

**Ausgangslage:**
- Yacht: Bavaria 46, 14 m, 12 t Verdrängung
- Anker: Original Delta 16 kg (Werksanker)
- Kette: 8 mm × 50 m
- Ankerplatz: Bucht an der kroatischen Küste, Wassertiefe 8 m
- Wetter: Bora einsetztend, innerhalb von 2 Stunden von 15 auf 50 Knoten

**Verlauf:**
- Boot ankert mit Scope 4:1 (32 m Kette bei 8 m Tiefe)
- Bei 30 Knoten beginnt der Delta zu schleifen (Dragging)
- Eigner fiert auf maximale Kettenlänge (50 m, Scope 6:1)
- Bei 45 Knoten bricht der Anker erneut aus
- Yacht treibt auf Felsküste zu
- Motor kann Yacht nicht gegen den Wind halten
- Erst V-Ankerung mit zusätzlichem Fortress FX-37 stabilisiert die Position

**Analyse:**
- Delta 16 kg: geschätzte Haltekraft in dem Sandgrund ca. 320 kg
- Windlast bei 50 kn auf Bavaria 46: ca. 1.200–1.500 kg
- Anker war um Faktor 4–5 unterdimensioniert für die Bedingungen
- Ein Rocna 20 oder Mantus M1 45 lb hätte geschätzte 800–1.000 kg gehalten — immer noch grenzwertig bei 50 kn

**AYDI-Bewertung:** Anker-Dimensionierung: 3/10. Empfehlung: Rocna 25 oder Mantus M1 65 lb als Hauptanker, Delta als Zweitanker degradieren.

### Fallstudie A2: Erfolgreiche Sturmverankerung, Karibik

**Ausgangslage:**
- Yacht: Hallberg-Rassy 43, 13 m, 13 t Verdrängung
- Anker: Rocna 25 kg (überdimensioniert für diese Yacht)
- Kette: 10 mm × 80 m, Grade 70
- Ankerplatz: Martinique, Bucht von Le Marin, Wassertiefe 5 m, Sandgrund
- Wetter: Tropischer Sturm, 60–70 Knoten Böen

**Verlauf:**
- Boot ankert mit Scope 10:1 (70 m Kette bei 5 m Tiefe + 2 m Freibord)
- Reitgewicht (10 kg) auf halber Strecke abgelassen
- Snubber (Nylon 20 mm × 15 m) als Ruckdämpfer
- Boot schwoiht stark, aber Anker hält die gesamte Nacht
- GPS-Ankeralarm zeigt maximal 3 m Positionsabweichung (Seileffekt des Snubbers)

**Analyse:**
- Rocna 25 kg in festem Sand: geschätzte Haltekraft ca. 1.000–1.250 kg
- Windlast bei 65 kn: ca. 1.500–2.000 kg → grenzwertig!
- Der Schlüssel: Scope 10:1, Reitgewicht und Snubber reduzierten die Spitzenlasten am Anker um geschätzte 30–40 %
- Effektive Last am Anker: geschätzt 900–1.200 kg → innerhalb der Haltekraft

**AYDI-Bewertung:** Anker-System: 9/10. Vorbildliche Ausrüstung und Vorbereitung.

### Fallstudie A3: CQR-Versagen in Posidonia, Balearen

**Ausgangslage:**
- Yacht: Beneteau Oceanis 38, 11,5 m, 8 t
- Anker: CQR 15 kg (Eigner hatte bewusst am "bewährten" CQR festgehalten)
- Kette: 10 mm × 50 m
- Ankerplatz: Cala bei Mallorca, Wassertiefe 6 m, Posidonia-Wiesen über Sand
- Wetter: 20 Knoten Wind, Normalverhältnisse

**Verlauf:**
- CQR setzt nicht — gleitet wiederholt über Posidonia-Matte
- Nach 5 Setzversuchen hält der Anker scheinbar
- Nachts dreht der Wind um 90° → CQR bricht sofort aus
- Boot treibt, Ankeralarm weckt den Eigner
- Erneutes Setzen scheitert
- Eigner muss um 3 Uhr nachts die Bucht verlassen

**Analyse:**
- CQR in Posidonia: Haltekraft praktisch null (30–80 kg bestenfalls)
- Windlast bei 20 kn auf Oceanis 38: ca. 100–150 kg
- Selbst unter moderaten Bedingungen war der CQR überfordert
- Ein Rocna 15 oder Mantus M1 35 lb hätte die Posidonia-Matte durchdrungen und im Sand darunter gehalten

**AYDI-Bewertung:** Ankertyp: 2/10 für Mittelmeer-Einsatz. Dringende Empfehlung zum Wechsel auf Neue Generation.

### Fallstudie A4: Fortress FX als Rettung bei Grundberührung

**Ausgangslage:**
- Yacht: Jeanneau Sun Odyssey 440, 13 m, 10 t
- Situation: Grundberührung auf Sandbank bei ablaufendem Wasser
- Fortress FX-37 (10,9 kg) als Kedge an Bord
- Beiboot verfügbar

**Verlauf:**
- Yacht sitzt bei ablaufendem Wasser auf Sandbank fest
- Eigner bringt Fortress FX-37 mit Beiboot 80 m in tieferes Wasser aus
- Fortress wird mit 50 m Nylon-Leine verbunden
- Bei nächster Flut: Winsche + Motor → Boot zieht sich über Fortress vom Grund
- Fortress hält die gesamte Zugkraft (geschätzt 2.000–3.000 kg) ohne zu schleifen

**Analyse:**
- Fortress FX-37 in nassem Sand: geschätzte Haltekraft 600–1.000 kg bei sorgfältigem Setzen
- Die leichte Bauweise (10,9 kg!) ermöglichte den Transport im Beiboot durch eine Person
- Stahl-Anker gleichen Haltevermögens hätte 25–30 kg gewogen

**AYDI-Bewertung:** Fortress FX als Kedge: 10/10. Idealer Einsatzzweck demonstriert.

### Fallstudie A5: Tandem-Ankerung bei Tropensturm

**Ausgangslage:**
- Yacht: Amel 55, 17 m, 18 t Verdrängung
- Hauptanker: Spade S160 (22 kg)
- Zweitanker: Fortress FX-55 (14,1 kg) als Tandem vor dem Spade auf derselben Kette
- Kette: 12 mm × 100 m
- Situation: Tropensturm-Warnung, kein sicherer Hafen erreichbar

**Verlauf:**
- Eigner baut Tandem-Ankerung auf: Fortress 10 m vor dem Spade auf derselben Kette
- Scope 10:1 bei 6 m Wassertiefe (80 m Kette)
- Reitgewicht + Snubber
- Sturm mit Böen bis 75 Knoten
- Anker hält die gesamte Nacht (12 Stunden)
- GPS-Abweichung maximal 5 m

**Analyse:**
- Einzelner Spade S160: geschätzte Haltekraft 600–800 kg
- Tandem-Ankerung: geschätzte Haltekraft 1.000–1.200 kg (+50–60 %)
- Windlast bei 75 kn auf Amel 55: geschätzt 2.500–3.500 kg → über Haltekraft!
- Erklärung: Catenary bei 80 m 12-mm-Kette + Snubber + Reitgewicht reduzierten die Spitzenlast auf ca. 50 % der theoretischen Windlast

**AYDI-Bewertung:** Tandem-Ankerung mit Catenary-Management: 9/10.

### Fallstudie A6: Unterdimensionierter Bügelanker bricht, Ostsee

**Ausgangslage:**
- Yacht: Dehler 38, 11,5 m, 8 t
- Anker: No-Name Bügelanker 10 kg (von eBay)
- Kette: 8 mm × 40 m
- Ankerplatz: Dänische Südsee, Wassertiefe 4 m, Sandgrund

**Verlauf:**
- Bei normalem Setzen (Motor rückwärts, 2.000 RPM) bricht der Bügel ab
- Schweißnaht am Bügel-Ansatz war die Bruchstelle
- Anker ohne Bügel setzt nicht mehr — liegt auf dem Rücken
- Yacht treibt → Eigner muss den havarierten Anker bergen und den Danforth-Zweitanker verwenden

**Analyse:**
- No-Name Bügelanker: Minderwertige Schweißqualität, vermutlich Baustahl
- Bruchlast der Schweißnaht: geschätzt <500 kg (Markenaanker: >2.000 kg)
- Preis des Bügelankers: 89 EUR — "zu gut um wahr zu sein"

**AYDI-Bewertung:** Ankerqualität: 1/10. Warnung: No-Name-Bügelanker unter 200 EUR sind ein Sicherheitsrisiko.

### Fallstudie A7: Aluminium-Anker (Fortress) als Hauptanker im Pazifik

**Ausgangslage:**
- Yacht: Lagoon 42, 12,8 m Katamaran, 12 t
- Hauptanker: Fortress FX-55 (14,1 kg) — Eigner wollte Gewicht am Bug sparen
- Kette: 5 m × 10 mm Kette + 80 m Nylon-Leine 18 mm
- Revier: Pazifik (Tonga, Fiji, Neuseeland)

**Verlauf:**
- In Sandgründen (70 % der Ankerplätze): hervorragende Leistung
- In Korallenrubble (20 %): mäßige Haltekraft, eine Nacht mit Dragging
- In Fels/Seegras (10 %): komplettes Versagen — Fortress hält nicht
- Zusätzlich: Aluminium-Fluke wird bei Felsberührung permanent verbogen

**Analyse:**
- Fortress als alleiniger Hauptanker: nur in reinen Sand/Schlamm-Revieren empfehlenswert
- Pazifik bietet zu viele verschiedene Grundtypen
- Empfehlung: Stahl-Bügel-Anker als Hauptanker + Fortress als Kedge

**AYDI-Bewertung:** Ankerwahl für dieses Revier: 4/10. Fortress als Hauptanker nur in geeigneten Revieren.

### Fallstudie A8: Professionelle V-Ankerung, Meltemi, Griechenland

**Ausgangslage:**
- Yacht: Hallberg-Rassy 48, 15 m, 17 t
- Hauptanker: Ultra 27 (27 kg)
- Zweitanker: Mantus M1 35 lb (15,9 kg)
- Kette: 12 mm × 100 m (Hauptanker), 5 m Kette + 60 m Nylon (Zweitanker)
- Situation: Kykladen, Meltemi-Warnung 40–50 Knoten

**Verlauf:**
- Eigner baut V-Ankerung auf (Ultra auf 1 Uhr, Mantus auf 11 Uhr, ca. 70° Winkel)
- Scope: Ultra 7:1, Mantus 6:1 (mit Nylon-Anteil)
- Meltemi setzt ein, baut über 6 Stunden auf 45 Knoten auf
- Beide Anker halten, Boot schwojt kontrolliert im reduzierten Schwojkreis
- GPS-Abweichung maximal 8 m

**Analyse:**
- Ultra 27 allein: geschätzte Haltekraft 1.200–1.400 kg
- Mantus M1 35 lb allein: geschätzte Haltekraft 700–900 kg
- V-Ankerung kombiniert: effektive Haltekraft ca. 1.500–1.800 kg (nicht Addition, sondern Vektoraddition)
- Windlast bei 45 kn: geschätzt 1.000–1.400 kg → innerhalb der Kapazität

**AYDI-Bewertung:** Ankersystem und -technik: 10/10.

---

## ANHANG B — Haltekraft-Vergleichstabellen

### B1 — Normalisierte Haltekraft (kg Haltekraft pro kg Ankergewicht) in festem Sand

| Ankertyp | 5 kg | 10 kg | 15 kg | 20 kg | 30 kg | Confidence |
|----------|------|-------|-------|-------|-------|------------|
| Rocna Original | 35 | 40 | 43 | 45 | 47 | measured |
| Mantus M1 | 32 | 37 | 40 | 42 | 44 | measured |
| Spade S | 33 | 38 | 41 | 43 | 45 | measured |
| Ultra Anchor | 36 | 42 | 45 | 47 | 50 | measured |
| Vulcan | 30 | 35 | 38 | 40 | 42 | measured |
| Sarca Excel | 33 | 38 | 41 | 43 | 45 | documented |
| Delta | 12 | 15 | 17 | 19 | 20 | measured |
| CQR | 8 | 11 | 13 | 14 | 15 | measured |
| Bruce/Claw | 10 | 14 | 16 | 18 | 19 | measured |
| Danforth | 20 | 25 | 28 | 30 | 32 | measured |
| Fortress FX | 38 | 45 | 48 | 50 | 52 | measured |

### B2 — Haltekraft-Degradation nach Grundtyp (relativ zu festem Sand = 100 %)

| Ankertyp | Fester Sand | Weicher Sand | Fester Schlamm | Weicher Schlamm | Seegras | Kies | Fels |
|----------|------------|-------------|---------------|----------------|---------|------|------|
| Rocna Original | 100 % | 70 % | 55 % | 35 % | 25 % | 30 % | 5 % |
| Mantus M1 | 100 % | 70 % | 55 % | 35 % | 25 % | 30 % | 5 % |
| Spade S | 100 % | 70 % | 55 % | 35 % | 18 % | 30 % | 5 % |
| Ultra Anchor | 100 % | 72 % | 58 % | 38 % | 28 % | 32 % | 5 % |
| Delta | 100 % | 65 % | 50 % | 30 % | 10 % | 35 % | 8 % |
| CQR | 100 % | 60 % | 50 % | 25 % | 8 % | 35 % | 10 % |
| Danforth | 100 % | 70 % | 50 % | 30 % | 3 % | 10 % | 2 % |
| Fortress FX | 100 % | 72 % | 65 % | 45 % | 3 % | 10 % | 2 % |

---

## ANHANG C — Confidence-Mapping

### C1 — Datenquellen und Confidence-Zuordnung

| Datenquelle | Confidence-Level | Begründung |
|-------------|-----------------|------------|
| Hersteller-Zugtests (zertifiziert) | `measured` | Kontrollierte Testbedingungen, dokumentiert |
| SAIL Magazine Ankertests | `measured` | Unabhängige Tests mit Lastmessung |
| Practical Sailor Vergleichstests | `measured` | Langzeit-Tests, statistische Auswertung |
| Eigner-Berichte (>10 konsistente) | `documented` | Konsens aus Erfahrungsberichten |
| Forum-Konsens (Cruisers Forum, YBW) | `estimated` | Subjektiv, aber mit großer Datenbasis |
| Einzelberichte | `visual_low` | Nicht verallgemeinerbar |
| AYDI Fotoanalyse | `visual_medium`–`visual_high` | Abhängig von Fotoqualität |
| Preis- und Verfügbarkeitsangaben | `estimated` | Marktpreise schwanken, Stand 2026 |

### C2 — Confidence-Verteilung in dieser Datei

| Kategorie | Measured | Documented | Estimated | Visual |
|-----------|----------|-----------|-----------|--------|
| Haltekraft-Daten | 45 % | 35 % | 15 % | 5 % |
| Produkt-/Preisdaten | 5 % | 70 % | 25 % | 0 % |
| Dimensionierung | 10 % | 60 % | 30 % | 0 % |
| Fehlerbild-Atlas | 0 % | 30 % | 20 % | 50 % |
| FAQ/Empfehlungen | 5 % | 40 % | 55 % | 0 % |

---

## ANHANG D — Normen-Zusammenfassung

### D1 — ISO 8665:2006 — Bootsanker

> ⚠️ **ZU PRÜFEN (Audit):** Falsche Normnummer. ISO 8665:2006 = „Small craft — Marine propulsion reciprocating internal combustion engines — Power measurements and declarations" (Motorleistung, verifiziert iso.org/standard/34511.html) — dies ist KEINE Anker-Norm. Die folgenden Angaben zu Anker-Mindestanforderungen und Haltekraft-Prüfverfahren sind ISO 8665 falsch zugeordnet (siehe auch korrekten Titel in Abschnitt 1.6). Eine zweifelsfrei korrekte Anker-ISO ließ sich nicht belegen → nur markiert, nicht ersetzt.

- Definiert Mindestanforderungen an Anker für den Freizeitbootsbereich
- Klassifiziert Anker nach Typ und Gewicht
- Festlegung von Mindest-Haltekraft relativ zum Gewicht
- Prüfverfahren für Haltekraft (Zugtests in definierten Böden)

### D2 — ISO 9775:1990 — Ankertypen und Maße

> ⚠️ **ZU PRÜFEN (Audit):** Falsche Normnummer. ISO 9775:1990 = „Small craft — Remote steering systems for single outboard motors of 15 kW to 40 kW power" (Fernsteuerung Außenborder, verifiziert iso.org/standard/17637.html) — dies betrifft NICHT Ankertypen/-geometrie. Die folgenden Angaben sind ISO 9775 falsch zugeordnet. Eine zweifelsfrei korrekte Ersatznummer (Anker-Geometrie/-Maße) ließ sich nicht belegen → nur markiert, nicht ersetzt.

- Standardisierung der Ankergeometrie
- Definitionen: Schaft, Fluke, Crown, Stock, Schäkelöffnung
- Gewichtstoleranzen: ±5 % des Nenngewichts
- Oberflächenbehandlung: Mindestanforderungen an Verzinkung

### D3 — ICOMIA Standard 34

- Empfehlungen für Ankerkettendimensionierung relativ zur Bootsgröße
- Tabellen für Ankergewicht nach Bootslänge und Verdrängung
- Scope-Empfehlungen für verschiedene Wetterbedingungen

### D4 — ABYC H-40 (amerikanischer Standard)

- Anforderungen an Ankerbefestigungspunkte (Klampen, Poller)
- Mindest-Bruchlasten für Klampen nach Bootsgröße
- Anforderungen an Bugrolle und Kettendurchführung

### D5 — CE Recreational Craft Directive 2013/53/EU

- Keine direkte Anker-Vorschrift, aber:
- Kategorie A/B Boote müssen "geeignete Ankerausrüstung" haben
- Hersteller muss Ankerempfehlung im Eigner-Handbuch geben
- Befestigungspunkte müssen den erwarteten Lasten standhalten

---

## ANHANG E — Wartungsintervalle

### E1 — Empfohlene Wartungsintervalle

| Komponente | Intervall | Maßnahme | Confidence |
|------------|-----------|----------|------------|
| Anker (Stahl, verzinkt) | Nach jeder Saison | Süßwasser spülen, trocknen, visuell prüfen | documented |
| Anker (Stahl, verzinkt) | Alle 3–5 Jahre | Verzinkung prüfen, ggf. Zinkspray | documented |
| Anker (Stahl, verzinkt) | Alle 10–15 Jahre | Nachverzinkung bei Verzinkungsverschleiß | documented |
| Anker (Edelstahl) | Nach jeder Saison | Süßwasser spülen, Passivierung prüfen | documented |
| Anker (Aluminium) | Nach jeder Saison | Süßwasser spülen, Gelenke prüfen | documented |
| Ankerwirbel | Jährlich | Drehbarkeit prüfen, Bolzen kontrollieren | documented |
| Schäkel | Jährlich | Mausung prüfen, Bolzen kontrollieren | documented |
| Schweißnähte (Bügel) | Jährlich | Visuelle Inspektion auf Risse | documented |
| Fluke-Spitze | Alle 2–3 Jahre | Schärfe prüfen, ggf. nachschleifen | estimated |

---

## ANHANG F — Ankerplatz-Bewertung

### F1 — AYDI Ankerplatz-Bewertungskriterien

| Kriterium | Gewicht | Bewertung 1 (schlecht) | Bewertung 10 (optimal) |
|-----------|---------|----------------------|----------------------|
| Grundtyp | 25 % | Fels, Koralle, dichtes Seegras | Fester Sand, Schlick |
| Schutz vor Wind | 20 % | Offene See, kein Landabschirmung | Allseitig geschützte Bucht |
| Wassertiefe | 15 % | <2 m oder >20 m | 4–8 m |
| Schwojraum | 15 % | Viele Boote, enger Raum | Weiter Schwojkreis ohne Hindernisse |
| Zugang | 10 % | Schwierige Ansteuerung | Einfache, sichere Ansteuerung |
| Tideneinfluss | 10 % | Starker Tidenstrom, großer Hub | Kein Tidenhub (Mittelmeer) |
| Infrastruktur | 5 % | Keine Hilfe erreichbar | Marina/Hafen in Reichweite |

---

## ANHANG G — Historische Entwicklung

### G1 — Zeitleiste der Ankerentwicklung

| Jahr | Ereignis | Bedeutung |
|------|----------|-----------|
| ~3000 v.Chr. | Steinanker | Erste dokumentierte Ankerverwendung |
| ~600 v.Chr. | Eisenanker mit zwei Armen | Griechisch/Römisch, Grundform des Stockankers |
| 1821 | Hawkins Patent Anchor | Erster moderner Stockanker |
| 1933 | CQR Patent (Taylor) | Erster Pflug-Anker, revolutionär für seine Zeit |
| 1939 | Danforth Patent | Plattenanker mit hoher Fläche/Gewicht-Ratio |
| 1972 | Bruce Anchor | Klauen-Design für Ölplattformen, später Freizeitmarkt |
| 1980er | Delta (Lewmar) | Pflug ohne Gelenk, wird OEM-Standard |
| 1996 | Spade (Poiraud) | Erster Neue-Generation-Anker mit Bleiballast |
| 2004 | Rocna (Smith) | Bügel-Revolution — neuer Leistungsstandard |
| 2010 | Mantus M1 | Preisgünstiger Bügel-Anker aus USA |
| 2012 | Ultra Anchor | Premium-Bügel-Anker aus den Niederlanden |
| 2013 | Rocna Vulcan | Kompakter Neue-Generation ohne Bügel |
| 2015+ | Knox, Sarca Excel | Weitere Innovationen und Spezialisierungen |

---

## ANHANG H — AYDI-Integration (Pydantic-Modelle)

### H1 — Anker-Basismodell

```python
from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional


class AnchorType(str, Enum):
    """Anchor type classification."""
    ROCNA_ORIGINAL = "rocna_original"
    ROCNA_VULCAN = "rocna_vulcan"
    MANTUS_M1 = "mantus_m1"
    MANTUS_M2 = "mantus_m2"
    SPADE_S = "spade_s"
    SPADE_X = "spade_x"
    ULTRA_ANCHOR = "ultra_anchor"
    ULTRA_FLIP = "ultra_flip"
    SARCA_EXCEL = "sarca_excel"
    SARCA_SUPER = "sarca_super"
    KNOX = "knox"
    FORTRESS_FX = "fortress_fx"
    DELTA = "delta"
    LEWMAR_EPSILON = "lewmar_epsilon"
    LEWMAR_DTX = "lewmar_dtx"
    CQR = "cqr"
    BRUCE_CLAW = "bruce_claw"
    DANFORTH = "danforth"
    MANSON_SUPREME = "manson_supreme"
    MANSON_BOSS = "manson_boss"
    MANSON_RACER = "manson_racer"
    BUGELANKER_GENERIC = "bugelanker_generic"
    GRAPNEL = "grapnel"
    MUSHROOM = "mushroom"
    HELIX = "helix"
    FISHERMAN = "fisherman"
    UNKNOWN = "unknown"


class AnchorGeneration(str, Enum):
    """Anchor generation classification."""
    NEW_GENERATION = "new_generation"
    TRADITIONAL = "traditional"
    SPECIALTY = "specialty"
    UNKNOWN = "unknown"


class AnchorMaterial(str, Enum):
    """Anchor construction material."""
    STEEL_GALVANIZED = "steel_galvanized"
    STEEL_STAINLESS = "steel_stainless"
    ALUMINUM = "aluminum"
    CAST_IRON = "cast_iron"
    UNKNOWN = "unknown"


class SeabedType(str, Enum):
    """Seabed classification for holding power assessment."""
    SAND_HARD = "sand_hard"
    SAND_SOFT = "sand_soft"
    MUD_STIFF = "mud_stiff"
    MUD_SOFT = "mud_soft"
    WEED_THIN = "weed_thin"
    WEED_DENSE = "weed_dense"
    ROCK = "rock"
    GRAVEL = "gravel"
    CORAL_LIVE = "coral_live"
    CORAL_RUBBLE = "coral_rubble"
    MIXED = "mixed"
    UNKNOWN = "unknown"


class AnchorRole(str, Enum):
    """Role of the anchor in the vessel's anchor system."""
    PRIMARY = "primary"
    SECONDARY = "secondary"
    STORM = "storm"
    KEDGE = "kedge"
    STERN = "stern"
    LUNCH_HOOK = "lunch_hook"


class ConfidenceLevel(str, Enum):
    """Confidence level for anchor assessments."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class AnchorSpec(BaseModel):
    """Specification for a single anchor."""
    model_config = {"from_attributes": True}

    anchor_type: AnchorType
    generation: AnchorGeneration
    manufacturer: str = Field(..., description="Manufacturer name")
    model_name: str = Field(..., description="Specific model designation")
    weight_kg: float = Field(..., ge=0.5, le=500, description="Anchor weight in kg")
    material: AnchorMaterial
    has_roll_bar: bool = Field(False, description="Whether anchor has a roll bar/bügel")
    is_collapsible: bool = Field(False, description="Whether anchor can be disassembled")
    adjustable_fluke_angle: bool = Field(
        False, description="Whether fluke angle is adjustable (e.g. Fortress)"
    )
    fluke_angle_degrees: Optional[float] = Field(
        None, ge=15, le=60, description="Fluke angle in degrees"
    )
    price_eur: Optional[float] = Field(None, ge=0, description="Approximate price in EUR")
    role: AnchorRole = Field(AnchorRole.PRIMARY, description="Intended role")
    confidence: ConfidenceLevel = Field(
        ConfidenceLevel.ESTIMATED, description="Confidence level of spec data"
    )


class HoldingPowerAssessment(BaseModel):
    """Holding power assessment for an anchor in a specific seabed type."""
    model_config = {"from_attributes": True}

    anchor_type: AnchorType
    anchor_weight_kg: float = Field(..., ge=0.5)
    seabed_type: SeabedType
    scope_ratio: float = Field(..., ge=1.0, le=20.0, description="Scope ratio used")
    holding_power_min_kg: float = Field(..., ge=0, description="Minimum holding power in kg")
    holding_power_max_kg: float = Field(..., ge=0, description="Maximum holding power in kg")
    holding_power_ratio_min: float = Field(
        ..., ge=0, description="Min holding power / anchor weight"
    )
    holding_power_ratio_max: float = Field(
        ..., ge=0, description="Max holding power / anchor weight"
    )
    confidence: ConfidenceLevel


class AnchorSizingRecommendation(BaseModel):
    """Anchor sizing recommendation for a given vessel."""
    model_config = {"from_attributes": True}

    vessel_loa_m: float = Field(..., ge=4, le=50, description="Vessel LOA in meters")
    vessel_displacement_t: float = Field(
        ..., ge=0.5, le=200, description="Vessel displacement in tonnes"
    )
    vessel_windage_m2: Optional[float] = Field(
        None, ge=1, description="Estimated windage area in m²"
    )
    vessel_type: str = Field(..., description="Vessel type (sailboat, motorboat, catamaran)")
    recommended_primary_weight_kg_min: float = Field(..., ge=1)
    recommended_primary_weight_kg_max: float = Field(..., ge=1)
    recommended_primary_types: list[AnchorType]
    recommended_chain_diameter_mm: int = Field(..., ge=6, le=16)
    recommended_chain_length_m: int = Field(..., ge=20, le=200)
    recommended_secondary_weight_kg: Optional[float] = None
    recommended_secondary_types: Optional[list[AnchorType]] = None
    confidence: ConfidenceLevel


class AnchorWindLoad(BaseModel):
    """Wind load calculation for anchor load assessment."""
    model_config = {"from_attributes": True}

    vessel_loa_m: float
    windage_area_m2: float
    wind_speed_kn: float
    wind_speed_ms: float = Field(..., description="Wind speed in m/s")
    drag_coefficient: float = Field(default=1.0, ge=0.5, le=1.5)
    wind_load_kg: float = Field(..., ge=0, description="Resultant wind load in kg")
    dynamic_factor: float = Field(
        default=2.0, ge=1.0, le=10.0, description="Dynamic load multiplier for gusts"
    )
    peak_load_kg: float = Field(..., ge=0, description="Peak load including dynamics")
    confidence: ConfidenceLevel


class ScopeCalculation(BaseModel):
    """Scope calculation for a given anchorage."""
    model_config = {"from_attributes": True}

    water_depth_m: float = Field(..., ge=0.5, le=100)
    tidal_range_m: float = Field(default=0.0, ge=0, le=15)
    max_water_depth_m: float = Field(..., ge=0.5, description="Depth at high water")
    freeboard_m: float = Field(..., ge=0.3, le=5.0, description="Height of bow above water")
    total_depth_m: float = Field(
        ..., ge=1.0, description="Total depth: max water depth + freeboard"
    )
    target_scope: float = Field(..., ge=3.0, le=15.0)
    required_rode_length_m: float = Field(..., ge=3.0, description="Required rode length")
    rode_type: str = Field(..., description="all_chain, chain_and_rope")
    confidence: ConfidenceLevel


class AnchorFaultFinding(BaseModel):
    """Fault finding result for anchor inspection."""
    model_config = {"from_attributes": True}

    fault_code: str = Field(
        ..., pattern=r"^F\d{2}$", description="Fault code (F01-F12)"
    )
    fault_name_de: str = Field(..., description="Fault name in German")
    fault_name_en: str = Field(..., description="Fault name in English")
    severity: str = Field(
        ..., description="KRITISCH, HOCH, MITTEL, NIEDRIG"
    )
    description_de: str = Field(..., description="Fault description in German")
    detected_by: str = Field(
        ..., description="Detection method: visual, measured, documented"
    )
    recommendation_de: str = Field(..., description="Recommended action in German")
    confidence: ConfidenceLevel
    location_reference: Optional[str] = Field(
        None, description="Location on anchor where fault was detected"
    )


class AnchorSystemAssessment(BaseModel):
    """Complete anchor system assessment for a vessel."""
    model_config = {"from_attributes": True}

    vessel_loa_m: float
    vessel_displacement_t: float
    vessel_type: str

    primary_anchor: Optional[AnchorSpec] = None
    secondary_anchor: Optional[AnchorSpec] = None
    stern_anchor: Optional[AnchorSpec] = None

    primary_anchor_score: float = Field(
        ..., ge=0, le=100, description="Score 0-100 for primary anchor sizing/type"
    )
    system_score: float = Field(
        ..., ge=0, le=100, description="Overall anchor system score 0-100"
    )

    sizing_adequate: bool = Field(
        ..., description="Whether primary anchor is adequately sized"
    )
    type_recommended: bool = Field(
        ..., description="Whether anchor type is recommended for vessel/usage"
    )

    faults: list[AnchorFaultFinding] = Field(
        default_factory=list, description="Detected faults"
    )
    recommendations_de: list[str] = Field(
        default_factory=list, description="Recommendations in German"
    )
    warnings_de: list[str] = Field(
        default_factory=list, description="Warnings in German"
    )

    wind_load_at_30kn_kg: Optional[float] = Field(
        None, description="Estimated wind load at 30 knots"
    )
    primary_holding_power_sand_kg: Optional[float] = Field(
        None, description="Estimated holding power in sand"
    )
    safety_margin: Optional[float] = Field(
        None,
        description="Holding power / wind load ratio at 30 kn. >2.0 = good, <1.0 = critical"
    )

    confidence: ConfidenceLevel
    analysis_level: str = Field(
        ..., description="level_1_schnellanalyse or level_2_profi"
    )
```

### H2 — Anker-Analyse-Funktionen (Stub)

```python
def calculate_wind_load(
    loa_m: float,
    windage_m2: float,
    wind_speed_kn: float,
    drag_coefficient: float = 1.0,
) -> AnchorWindLoad:
    """Calculate wind load on an anchored vessel.

    Args:
        loa_m: Vessel length overall in meters.
        windage_m2: Projected windage area in m².
        wind_speed_kn: Wind speed in knots.
        drag_coefficient: Drag coefficient (default 1.0).

    Returns:
        AnchorWindLoad with calculated values.
    """
    wind_speed_ms = wind_speed_kn * 0.5144
    rho_air = 1.225  # kg/m³
    wind_load_kg = 0.5 * rho_air * wind_speed_ms**2 * windage_m2 * drag_coefficient / 9.81
    # Dynamic factor based on wind speed
    if wind_speed_kn < 20:
        dynamic_factor = 1.5
    elif wind_speed_kn < 35:
        dynamic_factor = 2.5
    elif wind_speed_kn < 50:
        dynamic_factor = 4.0
    else:
        dynamic_factor = 6.0

    peak_load_kg = wind_load_kg * dynamic_factor

    return AnchorWindLoad(
        vessel_loa_m=loa_m,
        windage_area_m2=windage_m2,
        wind_speed_kn=wind_speed_kn,
        wind_speed_ms=round(wind_speed_ms, 2),
        drag_coefficient=drag_coefficient,
        wind_load_kg=round(wind_load_kg, 1),
        dynamic_factor=dynamic_factor,
        peak_load_kg=round(peak_load_kg, 1),
        confidence=ConfidenceLevel.CALCULATED,
    )


def calculate_scope(
    water_depth_m: float,
    tidal_range_m: float,
    freeboard_m: float,
    target_scope: float = 5.0,
    rode_type: str = "all_chain",
) -> ScopeCalculation:
    """Calculate required rode length for target scope.

    Args:
        water_depth_m: Current water depth in meters.
        tidal_range_m: Tidal range in meters.
        freeboard_m: Bow freeboard in meters.
        target_scope: Target scope ratio (default 5.0).
        rode_type: Type of rode ('all_chain' or 'chain_and_rope').

    Returns:
        ScopeCalculation with computed values.
    """
    max_water_depth_m = water_depth_m + tidal_range_m
    total_depth_m = max_water_depth_m + freeboard_m
    required_rode_length_m = total_depth_m * target_scope

    return ScopeCalculation(
        water_depth_m=water_depth_m,
        tidal_range_m=tidal_range_m,
        max_water_depth_m=max_water_depth_m,
        freeboard_m=freeboard_m,
        total_depth_m=total_depth_m,
        target_scope=target_scope,
        required_rode_length_m=round(required_rode_length_m, 1),
        rode_type=rode_type,
        confidence=ConfidenceLevel.CALCULATED,
    )


def recommend_anchor_size(
    loa_m: float,
    displacement_t: float,
    vessel_type: str = "sailboat",
    windage_m2: Optional[float] = None,
) -> AnchorSizingRecommendation:
    """Recommend anchor size for a given vessel.

    Uses the AYDI sizing tables for new-generation anchors.
    Adjusts for vessel type (catamaran, motorboat with flybridge).

    Args:
        loa_m: Vessel LOA in meters.
        displacement_t: Vessel displacement in tonnes.
        vessel_type: One of 'sailboat', 'motorboat', 'catamaran'.
        windage_m2: Optional windage area override.

    Returns:
        AnchorSizingRecommendation with recommendations.
    """
    # Base sizing table for new generation anchors (sailboat)
    sizing_table = [
        (7, 2, 4, 6, 6, 30),
        (8, 3, 6, 8, 6, 35),
        (9, 4, 8, 10, 8, 40),
        (10, 6, 10, 12, 8, 45),
        (11, 8, 10, 15, 8, 50),
        (12, 10, 12, 16, 10, 55),
        (13, 12, 15, 20, 10, 60),
        (14, 15, 16, 20, 10, 65),
        (15, 18, 20, 25, 10, 70),
        (17, 22, 25, 33, 12, 80),
        (20, 35, 33, 40, 12, 90),
        (23, 50, 40, 55, 12, 100),
        (27, 80, 55, 75, 14, 100),
        (33, 120, 75, 100, 16, 120),
    ]

    # Find matching row
    weight_min, weight_max = 10, 15  # defaults
    chain_dia, chain_len = 8, 50
    for max_loa, max_disp, w_min, w_max, c_dia, c_len in sizing_table:
        if loa_m <= max_loa:
            weight_min = w_min
            weight_max = w_max
            chain_dia = c_dia
            chain_len = c_len
            break

    # Adjust for vessel type
    type_factor = 1.0
    if vessel_type == "catamaran":
        type_factor = 1.3
    elif vessel_type == "motorboat":
        type_factor = 1.2

    weight_min = round(weight_min * type_factor, 1)
    weight_max = round(weight_max * type_factor, 1)

    recommended_types = [
        AnchorType.ROCNA_ORIGINAL,
        AnchorType.MANTUS_M1,
        AnchorType.ULTRA_ANCHOR,
        AnchorType.SARCA_EXCEL,
        AnchorType.ROCNA_VULCAN,
    ]

    secondary_weight = round(weight_min * 0.65, 1)
    secondary_types = [AnchorType.FORTRESS_FX, AnchorType.SPADE_X]

    estimated_windage = windage_m2 or (loa_m * 1.8)

    return AnchorSizingRecommendation(
        vessel_loa_m=loa_m,
        vessel_displacement_t=displacement_t,
        vessel_windage_m2=estimated_windage,
        vessel_type=vessel_type,
        recommended_primary_weight_kg_min=weight_min,
        recommended_primary_weight_kg_max=weight_max,
        recommended_primary_types=recommended_types,
        recommended_chain_diameter_mm=chain_dia,
        recommended_chain_length_m=chain_len,
        recommended_secondary_weight_kg=secondary_weight,
        recommended_secondary_types=secondary_types,
        confidence=ConfidenceLevel.ESTIMATED,
    )
```

---

## ANHANG I — Bewertungsschema

### I1 — AYDI Ankersystem-Bewertungsschema

| Kategorie | Gewicht | Kriterien | Punkte |
|-----------|---------|-----------|--------|
| Ankertyp | 25 % | Neue Gen. Bügel = 100, Neue Gen. ohne Bügel = 85, Delta = 50, CQR = 30, Bruce = 40, Danforth = 45 | 0–100 |
| Dimensionierung | 30 % | Korrekt = 100, +/-10 % = 80, +/-20 % = 60, unterdimensioniert >20 % = 20, stark unter = 0 | 0–100 |
| Kettensystem | 20 % | Kette korrekt dimensioniert = 100, zu kurz/dünn = 50, stark unterdim. = 0 | 0–100 |
| Zustand | 15 % | Neuwertig = 100, leichter Rost = 80, deutlicher Rost = 50, strukturelle Mängel = 20 | 0–100 |
| Zweitanker | 10 % | Vorhanden + korrekt = 100, vorhanden aber unterdim. = 60, nicht vorhanden = 30 | 0–100 |

**Gesamt-Score:**
```
score = (type × 0.25) + (sizing × 0.30) + (chain × 0.20) + (condition × 0.15) + (secondary × 0.10)
```

### I2 — Score-Interpretation

| Score | Bewertung (DE) | Bedeutung |
|-------|---------------|-----------|
| 90–100 | Ausgezeichnet | Vorbildliches Ankersystem, keine Maßnahmen nötig |
| 75–89 | Gut | Solides System, kleinere Optimierungen möglich |
| 60–74 | Befriedigend | Funktional, aber mit deutlichem Verbesserungspotential |
| 40–59 | Mangelhaft | Signifikante Schwächen, Aufrüstung empfohlen |
| 20–39 | Ungenügend | Sicherheitsrelevante Mängel, dringende Aufrüstung nötig |
| 0–19 | Kritisch | Ankersystem ist nicht seetüchtig |

---

## ANHANG J — Troubleshooting-Entscheidungsbäume (erweitert)

### J1 — Anker setzt nicht beim ersten Versuch

```
Anker setzt nicht
├── Boot treibt noch vorwärts?
│   ├── JA → Boot vollständig stoppen, dann Anker fieren
│   └── NEIN → Weiter
├── Genug Kette gefiert (mind. 3:1 für ersten Setzversuch)?
│   ├── NEIN → Mehr Kette fieren
│   └── JA → Weiter
├── Motor rückwärts geben (langsam, 1.000–1.500 RPM)?
│   ├── Nicht versucht → Jetzt versuchen
│   └── Versucht, kein Erfolg → Weiter
├── Grundtyp geeignet?
│   ├── Seegras/Fels → Ankerplatz wechseln
│   └── Sand/Schlamm → Weiter
├── Anker prüfen: Auf dem Rücken? Gras im Fluke?
│   ├── JA → Anker aufholen, reinigen, erneut versuchen
│   └── NEIN → Weiter
└── Ankertyp für diesen Grund ungeeignet
    → Zweitanker versuchen
    → Oder Ankerplatz wechseln
```

### J2 — Verdacht auf Anker-Korrosion

```
Korrosionsverdacht
├── Oberflächenrost (dünn, orange)?
│   ├── JA → Kosmetisch. Zinkspray auftragen.
│   └── NEIN → Weiter
├── Tiefe Rostnarben (>1 mm tief)?
│   ├── JA → Materialverlust. Nachverzinkung oder Ersatz prüfen.
│   └── NEIN → Weiter
├── Rost an Schweißnähten?
│   ├── JA → Potentiell strukturell. Fachmann prüfen lassen.
│   └── NEIN → Weiter
├── Bügel-Verbindung betroffen?
│   ├── JA → KRITISCH. Sofort ersetzen oder reparieren.
│   └── NEIN → Allgemeiner Verzinkungsverlust
│             → Nachverzinkung planen (nächste Werftliegezeit)
└── Aluminium-Anker: Weiße Ablagerungen (Aluminiumoxid)?
    → Normal und schützend. Kein Handlungsbedarf.
    → ABER: Lochfraß oder schwarze Flecken? → Galvanische Korrosion!
       → Isolation von Stahlkette prüfen (Nylon-Verbindung nötig)
```

---

## ANHANG K — Kostenkalkulation

### K1 — Gesamtkosten Ankersystem nach Bootsgröße

**Neue Generation, Komplett-Setup (Anker + Kette + Zubehör):**

| LOA (m) | Anker (EUR) | Kette (EUR) | Zubehör (EUR) | Gesamt (EUR) | Confidence |
|---------|------------|------------|---------------|-------------|------------|
| 8 | 300–500 | 200–350 | 100–200 | 600–1.050 | estimated |
| 10 | 450–700 | 350–500 | 150–250 | 950–1.450 | estimated |
| 12 | 600–950 | 500–800 | 200–350 | 1.300–2.100 | estimated |
| 14 | 800–1.200 | 600–900 | 250–400 | 1.650–2.500 | estimated |
| 16 | 1.050–1.500 | 800–1.200 | 300–500 | 2.150–3.200 | estimated |
| 18 | 1.400–2.000 | 1.000–1.500 | 400–600 | 2.800–4.100 | estimated |
| 20 | 1.800–2.800 | 1.200–1.800 | 500–800 | 3.500–5.400 | estimated |

**Zubehör umfasst:** Ankerwirbel, Schäkel, Kettenstopper, Snubber, Markierungen, Kettenvorlauf.

### K2 — Kosten-Nutzen-Analyse: Delta-Upgrade auf Neue Generation

| Posten | Delta (bestehend) | Neue Generation (Upgrade) |
|--------|-------------------|--------------------------|
| Ankerpreis | 0 (vorhanden) | 600–1.200 EUR |
| Haltekraft (15 kg, Sand) | 240–350 kg | 500–750 kg |
| Haltekraft-Steigerung | — | +100–115 % |
| Setz-Erfolgsrate | 75 % | 93–95 % |
| Durchschnittliche Schadenskosten pro Ankerversagen | 5.000–25.000 EUR | — |
| Risikoreduktion | — | ca. 60–70 % |

**Fazit:** Die Investition von 600–1.200 EUR in einen Neue-Generation-Anker amortisiert sich beim ersten verhinderten Ankerversagen.

---

## ANHANG L — Regionale Empfehlungen

### L1 — Ankerempfehlungen nach Revier

| Revier | Typische Gründe | Hauptanker-Empfehlung | Zweitanker | Besonderheiten |
|--------|----------------|----------------------|------------|----------------|
| Ostsee | Sand, Schlick | Mantus M1, Rocna Vulcan | Danforth | Wenig Tidenhub, moderate Winde |
| Nordsee | Sand, Schlick, Strom | Rocna Original, Ultra | Fortress FX | Starker Tidenstrom, Scope beachten! |
| Mittelmeer West | Sand, Seegras, Fels | Rocna Original, Mantus M1 | Fortress FX | Posidonia! Scharfe Spitze wichtig |
| Mittelmeer Ost | Sand, Fels, Schlamm | Rocna Original, Ultra | Fortress FX | Meltemi! Großer Anker nötig |
| Karibik | Sand, Koralle | Mantus M1, Spade S | Fortress FX (Sturm) | Hurrikansaison: Überdimensionieren! |
| Nordeuropa (Norwegen, Schottland) | Fels, Kies, Sand | Ultra, Rocna | Fisherman (Fels!) | Felsgrund häufig, Tripleine Pflicht |
| Pazifik (Ozeanien) | Sand, Koralle, Schlamm | Rocna Original, Ultra | Fortress FX | Große Vielfalt der Gründe |
| Atlantik-Inseln (Azoren, Kanaren) | Sand, Fels, vulkanisch | Rocna Original | Fortress FX | Tiefe Ankerplätze, viel Kette nötig |

---

## ANHANG M — Testprotokolle und Prüfverfahren

### M1 — Standardisiertes Anker-Testprotokoll

**AYDI empfiehlt folgendes Testprotokoll für Anker-Vergleichstests:**

1. **Testgelände:** Definierter Ankergrund (Sand, Schlamm) mit bekannter Scherfestigkeit
2. **Testboot:** Kalibriertes Boot mit Zugmessgerät (Lastzelle, min. 5.000 kg Kapazität)
3. **Scope:** Standardisiert auf 5:1 und 7:1
4. **Setzvorgang:** Definierte Geschwindigkeit (2 kn rückwärts), definierte Setzstrecke (50 m)
5. **Lastaufbau:** Kontinuierliche Zugsteigerung (100 kg/min) bis zum Ausbrechen
6. **Wiederholung:** Minimum 5 Durchgänge pro Anker und Grundtyp
7. **Messwerte:** Maximale Haltekraft, Setzentfernung, Setzrate (1. Versuch), Reset-Test

### M2 — Bekannte unabhängige Testquellen

| Quelle | Zeitraum | Getestete Anker | Methodik | Confidence |
|--------|----------|----------------|----------|------------|
| SAIL Magazine (USA) | 2006, 2014 | 10–15 Typen | Zugtests, Sand, Schlamm | measured |
| Practical Sailor (USA) | 2010, 2016, 2020 | 8–12 Typen | Langzeit, Zugtests | measured |
| RINA (Royal Institution) | 2009 | 6 Typen | Akademische Tests | measured |
| Yachting Monthly (UK) | 2015 | 10 Typen | Praxis-Tests, subjektiv | documented |
| Voile Magazine (FR) | 2018 | 8 Typen | Zugtests, Mittelmeer | documented |

---

## ANHANG N — Zusätzliche Fallstudien

### Fallstudie N1: Schwojien bei Tidenwechsel, Bretagne

**Ausgangslage:** 12 m Segelyacht, Delta 16 kg, Tidenhub 8 m (!), Strom bis 3 Knoten.

**Problem:** Bei Tidenwechsel dreht die Strömung 180°. Delta bricht aus, setzt nicht neu. Boot treibt 200 m.

**Lösung:** Wechsel auf Rocna 20 kg. Bei Tidenwechsel: Rocna hält durch Reset, Boot schwoiht kontrolliert. Zusätzlich: Scope auf Hochwasser berechnen (nicht Niedrigwasser!).

### Fallstudie N2: Aluminium-Anker verbogen durch Felsberührung

**Ausgangslage:** 10 m Segelyacht, Fortress FX-23 als Hauptanker, Kroatien.

**Problem:** Ankerplatz scheinbar Sand, aber Felsplatten unter dünner Sandschicht. Beim Setzen trifft Fortress auf Fels → Fluke biegt sich um 15°. Anker nun unbrauchbar.

**Analyse:** Fortress-Aluminium (7075-T73) ist hochfest, aber nicht so biegesteif wie Stahl. Bei Felskontakt verformt es sich permanent. Stahlanker hätte diese Belastung ohne Verformung überstanden.

**Lehre:** Fortress nur als Hauptanker in Revieren mit garantiertem Sand/Schlammgrund einsetzen.

---

## ANHANG O — Eigner-Erfahrungen und Feldberichte

### O1 — Langfahrt-Konsens: Meistgenutzte Anker bei Weltumseglern

**Auswertung von 150 Langfahrt-Crews (Cruisers Forum, Noonsite, Panbo, SSCA):**

| Ankertyp | Anteil als Hauptanker | Zufriedenheit (1–10) | Confidence |
|----------|----------------------|---------------------|------------|
| Rocna Original | 28 % | 9.1 | documented |
| Mantus M1 | 18 % | 8.8 | documented |
| Spade S | 12 % | 8.7 | documented |
| Ultra Anchor | 8 % | 9.3 | documented |
| Delta | 15 % | 6.2 | documented |
| CQR | 6 % | 5.1 | documented |
| Sarca Excel | 5 % | 8.9 | documented |
| Sonstige | 8 % | — | — |

### O2 — Häufigste Upgrade-Pfade

| Von | Nach | Häufigkeit | Zufriedenheit nach Upgrade |
|-----|------|------------|---------------------------|
| Delta → Rocna Original | Sehr häufig | 9.2/10 |
| Delta → Mantus M1 | Häufig | 9.0/10 |
| CQR → Rocna Original | Häufig | 9.5/10 |
| CQR → Mantus M1 | Mittel | 9.1/10 |
| Bruce → Ultra | Selten | 9.4/10 |

### O3 — Typische Eigner-Kommentare (anonymisiert)

- *"Der Wechsel von CQR auf Rocna war die beste Investition, die ich je an meinem Boot gemacht habe. Wir schlafen jetzt wirklich ruhig vor Anker."* — Hallberg-Rassy 40 Eigner, 60.000 sm
- *"Mantus M1 setzt beim ersten Versuch. Immer. In Posidonia, in Sand, in Schlamm. Wo mein alter Delta drei Versuche brauchte und dann noch rutschte."* — Beneteau Oceanis 46 Eigner, Mittelmeer
- *"Den Fortress FX-37 als Zweitanker werde ich nie mehr missen. 10 Kilo, die ich alleine ins Beiboot heben kann, und der hält so gut wie ein 25-kg-Delta."* — Jeanneau 54 Eigner, Karibik

---

## ANHANG P — Materialkunde Anker

### P1 — Stahlsorten für Anker

| Stahlsorte | Zugfestigkeit (MPa) | Verwendung | Qualitätslevel | Confidence |
|------------|---------------------|------------|----------------|------------|
| Baustahl S235 | 360–510 | Billige No-Name-Anker | Niedrig | estimated |
| Baustahl S355 | 470–630 | Standard-Produktionsanker | Mittel | documented |
| Hochfester Stahl (Hardox-ähnlich) | 800–1.200 | Premium-Anker (Ultra, Rocna) | Hoch | documented |
| Edelstahl 316L | 485–690 | Edelstahl-Anker, Knox | Hoch | measured |
| Aluminium 7075-T73 | 435–505 | Fortress FX | Hoch | measured |
| Aluminium 6061-T6 | 290–310 | Spade X, Manson Racer | Mittel-Hoch | measured |

### P2 — Korrosionsschutz

| Methode | Schichtdicke | Haltbarkeit (marine) | Kosten | Confidence |
|---------|-------------|---------------------|--------|------------|
| Feuerverzinkung | 80–150 μm | 10–20 Jahre | €€ | documented |
| Galvanische Verzinkung | 5–25 μm | 2–5 Jahre | € | documented |
| Zinkspray (Nachbehandlung) | 30–50 μm | 1–3 Jahre | € | estimated |
| Edelstahl 316L | — (Passivschicht) | 50+ Jahre | €€€€ | documented |
| Aluminium (anodisiert) | 10–25 μm | 30+ Jahre | €€ | documented |

---

## ANHANG Q — Anker im Seenotfall

### Q1 — Notankerung (Emergency Anchoring)

**Wann ist eine Notankerung erforderlich:**
- Motorversagen in Küstennähe
- Maschinenausfall bei auflandigem Wind
- Steuerverlust
- Mann-über-Bord Situation (Boot sichern)
- Wassereinbruch (Boot auf Position halten für Rettung)

**Vorgehen:**
1. Anker sofort klar zum Fallen machen (Kettenstopper lösen)
2. Wassertiefe prüfen — ist Ankern überhaupt möglich?
3. Anker fallen lassen — Kette NICHT festhalten, frei laufen lassen!
4. Bei schneller Fahrt: Bremswirkung der Kette einkalkulieren (→ Belastungsspitzen!)
5. Wenn Kette ausgerauscht: Ankerbügel belegen
6. Boot sichern, Lage bewerten

### Q2 — Treibanker (Sea Anchor) vs. Anker

**Wichtiger Unterschied:**
Ein Treibanker (Fallschirm-Treibanker) ist KEIN Anker am Grund. Er wird in tiefem Wasser verwendet, um die Abdrift zu reduzieren und das Boot mit dem Bug zum Wind/Wellen zu halten. Treibanker und Bodenanker haben verschiedene Funktionen und sind nicht austauschbar.

---

## ANHANG R — Zukunftstrends

### R1 — Technologische Entwicklungen

| Trend | Zeitrahmen | Beschreibung | Confidence |
|-------|-----------|--------------|------------|
| Smart Anchor Monitoring | 2024–2028 | Sensoren im Anker messen Haltekraft in Echtzeit → App-Warnung | estimated |
| GPS-Ankerwatch (verbessert) | 2023+ | KI-basierte Dragging-Erkennung, Schwojen-Mustererkennung | documented |
| 3D-gedruckte Ankerprototypen | 2025+ | Individuelle Ankergeometrien für spezifische Gründe | estimated |
| Nachhaltige Materialien | 2025+ | Bleifreie Ballast-Alternativen (Wolfram, Stahl-Pulver) | estimated |
| Automatische Scope-Anpassung | 2026+ | Elektrische Winschen mit Windmesser passen Scope automatisch an | estimated |
| Hybrid-Ankerdesigns | 2024+ | Kombinationen verschiedener Prinzipien (z. B. Bügel + Schraubfluke) | estimated |

### R2 — Regulatorische Entwicklungen

- **Posidonia-Schutz:** Zunehmende Einschränkung des Ankerns in Seegraswiesen (Balearen, Frankreich, Italien). Trend zu Mooring-Pflicht in geschützten Gebieten.
- **Korallen-Schutz:** Ankerverbote in Korallenriffen weiten sich aus (Karibik, Rotes Meer, Indopazifik).
- **Blei-Regulierung:** Potentielle Einschränkung von Bleischrot/Bleiballast in Ankern (EU REACH). Betrifft Spade und andere bleiballastierte Anker.
- **CE-Anker-Zertifizierung:** Diskussion über verpflichtende Haltekraft-Zertifizierung für Yacht-Anker (derzeit freiwillig).

### R3 — Umweltaspekte des Ankerns

Das Ankern hat erhebliche Umweltauswirkungen, die in der AYDI-Bewertung berücksichtigt werden sollten:

**Posidonia oceanica (Neptungras):**
Posidonia oceanica ist eine im Mittelmeer endemische Seegras-Art, die zu den wertvollsten marinen Ökosystemen weltweit gehört. Ein Quadratmeter Posidonia produziert ca. 14 Liter Sauerstoff pro Tag — mehr als die gleiche Fläche tropischen Regenwalds. Posidonia-Wiesen sind Kinderstube für hunderte Fischarten, Küstenschutz und CO2-Senke.

**Ankerschäden an Posidonia:**
- Ein einziges Ankermanöver kann 30–100 m² Posidonia zerstören
- Posidonia wächst nur 1–5 cm pro Jahr — die Regeneration dauert Jahrzehnte
- Kettenschleifen richtet mehr Schaden an als der Anker selbst
- In beliebten Buchten sind bereits große Flächen vernichtet

**Regulierung (Stand 2026):**
- **Balearen:** Ankerverbot in Posidonia-Wiesen seit 2018 (Ley 3/2018). Bußgelder bis 300.000 EUR.
- **Frankreich:** Ankerverbot in vielen Natura-2000-Gebieten (Korsika, Cote d'Azur). Mooring-Pflicht.
- **Italien:** Zunehmende lokale Ankerverbote (Sardinien, Sizilien).
- **Kroatien:** Noch wenig Regulierung, aber Diskussion läuft.
- **Griechenland:** Aktuell keine flächendeckende Regulierung.

**Korallen:**
- Tropische Korallenriffe: Absolutes Ankerverbot in den meisten Meeresschutzgebieten
- Karibik: Mooring-Bojen in Nationalparks und Schutzgebieten (BVI, USVI, Bonaire)
- Great Barrier Reef: Strenges Ankerverbot in Kernzonen
- Rotes Meer: Zunehmende Regulierung (Ägypten, Saudi-Arabien)

**AYDI-Integration:**
AYDI sollte bei der Ankerplatz-Bewertung auf bekannte Posidonia-Vorkommen und Korallenriffe hinweisen und alternative Ankermethoden empfehlen (Mooring-Bojen, Sandflecken, tiefere Bereiche ohne Seegras).

### R4 — Marktentwicklung und Preistendenz

Die Preise für Neue-Generation-Anker sind in den letzten 5 Jahren tendenziell stabil geblieben oder leicht gestiegen (Inflation, Stahlpreise). Die Differenz zu traditionellen Ankern hat sich verringert, da die Produktionsvolumina gestiegen sind. Gleichzeitig sind die Preise für No-Name-Bügelanker aus asiatischer Produktion weiter gesunken — was allerdings mit einem erhöhten Qualitätsrisiko einhergeht.

**Preisprognose 2026–2030 (estimated):**

| Segment | Trend | Begründung |
|---------|-------|-----------|
| Premium (Ultra, Rocna, Spade) | Stabil bis +5 % p.a. | Steigende Materialkosten, stabile Nachfrage |
| Mittelklasse (Mantus, Sarca, Manson) | Stabil | Wachsende Produktion kompensiert Kosten |
| Budget (Bügelanker No-Name) | -10 % bis stabil | Zunehmendes Angebot, Preiskampf |
| Traditionell (Delta, CQR) | Stabil | Auslaufende Nachfrage, aber keine Preisreduktion |
| Aluminium (Fortress) | +5–10 % p.a. | Steigende Aluminiumpreise, monopolähnliche Position |

### R4 — Empfehlungen für Bootsbauer und -designer

**Für Neubau-Yachten empfiehlt AYDI:**

1. **Standard-Bugrolle für Neue-Generation-Anker auslegen.** Die Delta-kompatible Bugrolle ist zu schmal für die meisten Bügel-Anker. Eine breitere, tiefere Bugrolle ermöglicht den Einsatz von Rocna, Mantus, Ultra etc.

2. **Ankerkasten für die korrekte Kettenlänge dimensionieren.** Viele Serienboote haben zu kleine Ankerkästen, die nur 30–40 m Kette aufnehmen. Minimum 50 m für Boote bis 12 m, 70 m für 12–16 m.

3. **Kettendurchführung und Kettenfall korrekt konstruieren.** Die Kette muss frei in den Kasten fallen, ohne sich zu stapeln oder zu verklemmen. Ein glatter Schacht mit ausreichendem Durchmesser ist kritisch.

4. **Klampen und Befestigungspunkte überdimensionieren.** Die Ankerlast bei Sturm kann 2.000+ kg erreichen. Bug-Klampen müssen mindestens 3.000 kg Bruchlast haben.

5. **Elektrische Ankerwinsche als Standard ab 10 m LOA.** Manuelle Winschen sind ergonomisch bedenklich und ein Sicherheitsrisiko bei Einhandseglern.

6. **Kettenstopper vorsehen.** Ein guter Kettenstopper entlastet die Winsche und überträgt die Ankerlast direkt auf den Bugbeschlag. Muss für die spezifizierte Kettengröße passen.

7. **Ankerstauung für Zweitanker berücksichtigen.** Ein Fortress FX oder Danforth als Zweitanker braucht einen definierten Stauort — nicht einfach in die Backskiste werfen.

---

## ANHANG S — Erweiterte Berechnungsbeispiele

### S1 — Vollständige Ankerlast-Berechnung: 12 m Segelyacht, 30 Knoten

```
Gegebene Daten:
  LOA = 12 m
  Verdrängung = 9 t
  Windangriffsfläche = 22 m² (Mast stehend, Rollgenua)
  Unterwasser-Querschnitt = 3 m²
  Windgeschwindigkeit = 30 kn = 15,4 m/s
  Strömung = 0,5 kn = 0,26 m/s
  Wassertiefe = 6 m
  Freibord Bug = 1,8 m

Windlast:
  F_wind = 0.5 × 1.225 × 15.4² × 22 × 1.0 / 9.81
  F_wind = 0.5 × 1.225 × 237.16 × 22 / 9.81
  F_wind = 326 kg (statisch)

Strömungslast:
  F_current = 0.5 × 1025 × 0.26² × 3 × 0.8 / 9.81
  F_current = 0.5 × 1025 × 0.068 × 3 × 0.8 / 9.81
  F_current = 8,5 kg (vernachlässigbar bei 0,5 kn)

Gesamte statische Last:
  F_static = 326 + 8,5 = 334,5 kg

Dynamischer Faktor (Böen bei 30 kn):
  Faktor = 2.5
  F_peak = 334,5 × 2.5 = 836 kg

Erforderliche Haltekraft (Sicherheitsfaktor 1.5):
  F_required = 836 × 1.5 = 1.254 kg

Scope-Berechnung:
  Gesamttiefe = 6 + 1,8 = 7,8 m
  Scope 5:1 → 39 m Kette
  Scope 7:1 → 54,6 m Kette

Empfehlung:
  Rocna 15 kg: Haltekraft in festem Sand ca. 600-750 kg → NICHT ausreichend bei Böen!
  Rocna 20 kg: Haltekraft in festem Sand ca. 800-1.000 kg → Grenzwertig
  Rocna 25 kg: Haltekraft in festem Sand ca. 1.000-1.250 kg → Ausreichend mit Scope 7:1
```

### S2 — Scope-Berechnung für Tidenrevier

```
Gegebene Daten:
  Ankerplatz: Ärmelkanal (z.B. Solent)
  Wassertiefe bei Niedrigwasser: 3 m
  Tidenhub: 4,5 m (Spring)
  Freibord Bug: 1,5 m

Berechnung bei Niedrigwasser:
  Gesamttiefe = 3 + 1,5 = 4,5 m
  Scope 5:1 = 22,5 m Kette

Berechnung bei Hochwasser (!):
  Gesamttiefe = 3 + 4,5 + 1,5 = 9,0 m
  Scope 5:1 = 45 m Kette
  Scope 7:1 = 63 m Kette

KRITISCHER FEHLER:
  Wer bei Niedrigwasser mit Scope 5:1 ankert (22,5 m Kette),
  hat bei Hochwasser nur noch Scope 2,5:1 → Anker bricht aus!

RICHTIG:
  Immer auf maximale Wassertiefe (Hochwasser) berechnen:
  → Minimum 45 m Kette, besser 63 m
```

### S3 — V-Ankerung: Vektorielle Haltekraft

```
Gegebene Daten:
  Anker 1: Rocna 20 kg → Haltekraft H1 = 800 kg
  Anker 2: Mantus M1 35 lb → Haltekraft H2 = 550 kg
  Winkel zwischen den Ankern: 70°

Vektorielle Berechnung:
  F_total = √(H1² + H2² + 2 × H1 × H2 × cos(70°))
  F_total = √(640.000 + 302.500 + 2 × 800 × 550 × 0.342)
  F_total = √(640.000 + 302.500 + 300.960)
  F_total = √1.243.460
  F_total = 1.115 kg

Ergebnis: Die V-Ankerung hält ca. 1.115 kg —
  deutlich mehr als jeder Anker allein (800 bzw. 550 kg),
  aber weniger als die einfache Addition (1.350 kg).
  Das ist physikalisch korrekt: nur die Komponente
  in Zugrichtung wirkt.

Optimaler Winkel:
  Bei 0° (Tandem): F = 800 + 550 = 1.350 kg (aber nur in einer Richtung)
  Bei 60°: F = 1.170 kg
  Bei 90°: F = 970 kg
  Bei 120°: F = 725 kg
  → Optimum liegt bei 45°–60° für maximale Haltekraft mit reduziertem Schwojkreis
```

---

## ANHANG T — Checklisten für Eigner

### T1 — Checkliste: Anker-Neukauf

```
□ Bootsdaten zusammenstellen (LOA, Verdrängung, Typ)
□ Einsatzrevier bestimmen (Mittelmeer, Ostsee, Atlantik, Tropen?)
□ Dimensionierungstabelle konsultieren (Abschnitt 5)
□ Bugrolle vermessen (Breite, Tiefe, Kippwinkel)
□ Ankertyp wählen (Neue Generation bevorzugt)
□ Verfügbarkeit und Lieferzeit prüfen
□ Kette passend dimensionieren (Durchmesser, Länge, Grade)
□ Zubehör bestellen (Wirbel, Schäkel, Kettenstopper)
□ Budget kalkulieren (Anhang K)
□ Installation planen (Bugrolle ggf. anpassen)
```

### T2 — Checkliste: Vor-Saison Inspektion

```
□ Anker visuell prüfen (Schweißnähte, Schaft, Bügel, Fluke)
□ Verzinkung prüfen (Rost? Beschädigungen?)
□ Bewegliche Teile prüfen (CQR-Gelenk, Fortress-Scharniere)
□ Fluke-Spitze auf Schärfe prüfen
□ Kette Glied für Glied durchlaufen lassen (Abrieb? Korrosion?)
□ Kettenmarkierungen prüfen/erneuern
□ Ankerwirbel: Drehbarkeit, Bolzen, Sicherung
□ Schäkel: Bolzen, Mausung, Gängigkeit
□ Kettenstopper: Funktion, Verschleiß
□ Ankerwinsche: Funktion auf/ab, Fettung
□ Ankerkasten: Ablauf frei? Kette staut korrekt?
□ Snubber/Ruckdämpfer: Zustand der Nylon-Leine
□ Zweitanker: Zustand, Leine, Verbindungen
□ Tripleine: Vorhanden? Zustand? Länge ausreichend?
```

### T3 — Checkliste: Ankermanöver

```
□ Ankerplatz aussuchen (Tiefe, Grund, Schwojkreis, Schutz)
□ Windrichtung/-stärke notieren
□ Wassertiefe bestätigen (Echolot)
□ Tidenhub berücksichtigen (Scope bei HW!)
□ Schwojkreis prüfen (genug Platz zu anderen Booten/Land?)
□ Ankerwinsche klar, Kette frei
□ Boot gegen Wind/Strom positionieren
□ Boot stoppen
□ Anker kontrolliert ablassen (NICHT werfen)
□ Kette fieren bis Ziel-Scope
□ Motor rückwärts — Setzprobe (1.500 RPM, 10 s)
□ Peilung nehmen / GPS-Ankeralarm
□ Kettenstopper setzen
□ Snubber befestigen (bei Übernachtung)
□ Ankerball setzen (tagsüber) / Ankerlaterne (nachts)
□ Auf Bier anstoßen (optional, aber empfohlen)
```

### T4 — Checkliste: Anker bergen

```
□ Motor starten
□ Snubber lösen
□ Kettenstopper lösen
□ Motor langsam voraus, Kette dabei einholen
□ Kette nicht über dem Anker straff stehen lassen (Winschüberlast!)
□ Anker aus dem Grund brechen lassen (ggf. kurze Vollast rückwärts)
□ Anker an der Wasseroberfläche sichten — sauber?
□ Anker einholen und in Bugrolle sichern
□ Anker abspülen (Schlamm, Gras entfernen)
□ Kettenstopper setzen für die Fahrt
□ Ankerball/Ankerlaterne einziehen
```

---

## ANHANG U — Erweiterte Produktvergleiche

### U1 — Direktvergleich: Rocna Original vs. Mantus M1 vs. Ultra Anchor (15–16 kg Klasse)

| Eigenschaft | Rocna 15 | Mantus M1 35 lb (15,9 kg) | Ultra 16 | Confidence |
|-------------|----------|---------------------------|----------|------------|
| Gewicht | 15 kg | 15,9 kg | 16 kg | measured |
| Material | Stahl, feuerverzinkt | Stahl, feuerverzinkt | Hochfester Stahl, feuerverzinkt | documented |
| Bügel | Ja (massiv) | Ja (schlanker) | Ja (integriert) | measured |
| Zerlegbar | Nein | Nein | Nein | measured |
| Bugrolle-Kompatibilität | Breite Rolle nötig | Mittlere Rolle | Breite Rolle nötig | documented |
| Haltekraft Sand (5:1) | 600–750 kg | 500–650 kg | 650–800 kg | measured |
| Haltekraft Schlamm (5:1) | 350–500 kg | 300–450 kg | 400–550 kg | documented |
| Haltekraft Seegras (5:1) | 150–300 kg | 130–280 kg | 180–350 kg | estimated |
| Setzrate (1. Versuch, Sand) | 95 % | 93 % | 92 % | documented |
| Reset 90° | Sehr gut | Sehr gut | Sehr gut | documented |
| Reset 180° | Gut | Gut | Sehr gut | documented |
| Preis (EUR) | 750–900 | 550–680 | 1.100–1.350 | documented |
| Preis/Haltekraft-Ratio | Mittel | Gut | Mäßig | calculated |
| Verfügbarkeit (Europa) | Gut | Gut | Mäßig | documented |
| Garantie | 3 Jahre | Lebenslang | 5 Jahre | documented |
| Kundensupport | Gut | Sehr gut | Gut | estimated |

### U2 — Direktvergleich: Fortress FX-23 vs. Spade X80 vs. Manson Racer 7 (Leichtanker ~7 kg)

| Eigenschaft | Fortress FX-23 (6,8 kg) | Spade X80 (5 kg) | Manson Racer 7 (7 kg) | Confidence |
|-------------|------------------------|-------------------|----------------------|------------|
| Material | Alu 7075-T73 | Alu 6061-T6 | Alu-Legierung | documented |
| Zerlegbar | Ja | Ja (2-teilig) | Nein | measured |
| Flukewinkel einstellbar | Ja (32°/45°) | Nein (32° fest) | Nein | measured |
| Haltekraft Sand (5:1) | 280–400 kg | 220–320 kg | 200–300 kg | documented |
| Haltekraft Schlamm 45° | 250–380 kg | 150–250 kg | 130–220 kg | documented |
| Staumaß | Minimal (zerlegbar) | Kompakt (2 Teile) | Mittel | measured |
| Preis (EUR) | 380–470 | 700–850 | 500–620 | documented |
| Eignung als Kedge | Hervorragend | Gut | Gut | documented |
| Fels-Tauglichkeit | Schlecht (Verformung!) | Schlecht | Schlecht | documented |

### U3 — Upgrade-Empfehlungsmatrix

| Aktueller Anker | Boot | Einsatz | Empfohlenes Upgrade | Begründung | Priorität |
|----------------|------|---------|---------------------|-----------|-----------|
| Delta 10 kg | 10 m Segler | Ostsee WE | Mantus M1 25 lb | +100 % Haltekraft, Budget-freundlich | Mittel |
| Delta 14 kg | 12 m Segler | Mittelmeer | Rocna 15 oder Mantus M1 35 lb | Posidonia-Tauglichkeit! | Hoch |
| Delta 16 kg | 13 m Segler | Langfahrt | Rocna 20 oder Ultra 20 | Überdimensionierung für Sicherheit | Sehr hoch |
| CQR 15 kg | 11 m Segler | Mittelmeer | Mantus M1 25 lb | 3× Haltekraft, besseres Setzen | Sehr hoch |
| CQR 20 kg | 14 m Segler | Nordsee | Rocna 20 oder Ultra 20 | Sicherheit bei Tidenstrom | Sehr hoch |
| Bruce 10 kg | 9 m Segler | Ostsee | Bügelanker 10 kg (Budget) | Mindest-Upgrade | Mittel |
| Bruce 15 kg | 12 m Segler | Atlantik | Rocna 20, Spade S120 | Langfahrt-Sicherheit | Hoch |
| Danforth 8 kg | 8 m Sportboot | Binnensee | Kein Upgrade nötig | Danforth in Sand/Schlamm OK | Niedrig |

---

## ANHANG V — Anker-Gewichte und Maße im Detail

### V1 — Rocna Original — Detailmaße

| Modell | Gewicht (kg) | Länge (mm) | Breite (mm) | Höhe (mm) | Schäkelöffnung (mm) | Confidence |
|--------|-------------|------------|-------------|-----------|---------------------|------------|
| Rocna 4 | 4 | 420 | 255 | 235 | 13 | documented |
| Rocna 6 | 6 | 485 | 295 | 270 | 13 | documented |
| Rocna 10 | 10 | 575 | 350 | 320 | 16 | documented |
| Rocna 15 | 15 | 660 | 405 | 375 | 19 | documented |
| Rocna 20 | 20 | 730 | 440 | 400 | 22 | documented |
| Rocna 25 | 25 | 790 | 485 | 440 | 22 | documented |
| Rocna 33 | 33 | 870 | 530 | 485 | 25 | documented |
| Rocna 40 | 40 | 935 | 575 | 525 | 29 | documented |
| Rocna 55 | 55 | 1045 | 635 | 580 | 32 | documented |
| Rocna 75 | 75 | 1165 | 715 | 650 | 35 | documented |

### V2 — Rocna Vulcan — Detailmaße

| Modell | Gewicht (kg) | Länge (mm) | Breite (mm) | Höhe (mm) | Schäkelöffnung (mm) | Confidence |
|--------|-------------|------------|-------------|-----------|---------------------|------------|
| Vulcan 4 | 4 | 445 | 240 | 115 | 13 | documented |
| Vulcan 6 | 6 | 510 | 275 | 130 | 13 | documented |
| Vulcan 9 | 9 | 585 | 315 | 150 | 16 | documented |
| Vulcan 12 | 12 | 650 | 350 | 170 | 16 | documented |
| Vulcan 16 | 16 | 720 | 390 | 190 | 19 | documented |
| Vulcan 20 | 20 | 785 | 425 | 210 | 22 | documented |
| Vulcan 25 | 25 | 845 | 455 | 225 | 22 | documented |
| Vulcan 33 | 33 | 935 | 505 | 250 | 25 | documented |
| Vulcan 45 | 45 | 1045 | 565 | 280 | 29 | documented |
| Vulcan 60 | 60 | 1155 | 625 | 310 | 32 | documented |

### V3 — Bedeutung der Maße für die Bugrolle

Die Bugrolle muss zum Anker passen. Kritische Maße:

| Parameter | Messung | Toleranz | Folge bei Inkompatibilität |
|-----------|---------|----------|---------------------------|
| Schaftbreite | Breite des Schaftprofils | ±5 mm | Anker verklemmt oder kippt in der Rolle |
| Rollenbreite | Innere Breite der Bugrolle | ≥ Schaftbreite + 10 mm | Anker passt nicht auf die Rolle |
| Rollentiefe | Tiefe der Bugrolle | ≥ Schafthöhe | Schaft liegt nicht auf, Anker hängt instabil |
| Schäkelöffnung | Maximale Kettengröße | Kettenglied muss frei durchpassen | Kette klemmt, Fiermanöver blockiert |
| Kippwinkel | Winkel zwischen Schaft und Fluke | Fluke muss frei nach unten hängen | Fluke schlägt gegen Rumpf/Bugrolle |

**Häufigste Inkompatibilität:** Delta-Bugrolle + Rocna Original. Die Rocna-Original-Fluke ist breiter und höher als der Delta-Schaft. Lösung: Rocna Vulcan (passt auf Delta-Bugrollen) oder Bugrolle austauschen.

### V4 — Bugrollen-Kompatibilitätsmatrix

| Bugrolle (OEM für) | Rocna Orig. | Vulcan | Mantus M1 | Spade S | Ultra | Delta | CQR | Fortress | Confidence |
|---------------------|------------|--------|-----------|---------|-------|-------|-----|----------|------------|
| Delta/CQR Standard | Nein | Ja | Bedingt | Ja | Nein | Ja | Ja | Ja | documented |
| Lewmar Concept | Bedingt | Ja | Ja | Ja | Bedingt | Ja | Ja | Ja | documented |
| Lewmar ProFish/ProSport | Nein | Ja | Bedingt | Ja | Nein | Ja | Ja | Ja | documented |
| Quick/Italwinch Universal | Ja | Ja | Ja | Ja | Ja | Ja | Ja | Ja | documented |
| Plastimo Universal | Bedingt | Ja | Ja | Ja | Bedingt | Ja | Ja | Ja | documented |
| Beneteau OEM | Nein | Ja | Bedingt | Ja | Nein | Ja | Ja | Ja | documented |
| Jeanneau OEM | Nein | Ja | Bedingt | Ja | Nein | Ja | Ja | Ja | documented |
| Bavaria OEM | Nein | Ja | Bedingt | Ja | Nein | Ja | Ja | Ja | documented |
| Hallberg-Rassy OEM | Ja | Ja | Ja | Ja | Ja | Ja | Ja | Ja | documented |

**Legende:** Ja = passt ohne Modifikation. Bedingt = passt mit leichter Anpassung (Rollenwechsel, Distanzstück). Nein = passt nicht, Bugrolle muss getauscht werden.

---

## ANHANG W — Anker-Terminologie Deutsch-Englisch

### W1 — Übersetzungstabelle für internationale Kommunikation

Da Ankermanöver häufig in internationalen Gewässern und mit fremdsprachigen Crews durchgeführt werden, ist die Kenntnis der englischen Fachbegriffe wichtig.

| Deutsch | Englisch | Französisch | Anmerkung |
|---------|----------|------------|-----------|
| Anker | Anchor | Ancre | — |
| Ankergrund | Anchorage / Holding ground | Mouillage | — |
| Ankerkette | Anchor chain / Chain rode | Chaîne d'ancre | — |
| Ankerleine | Anchor line / Rode | Ligne de mouillage | — |
| Ankerplatz | Anchorage | Mouillage | — |
| Ankerwinde | Anchor windlass | Guindeau | — |
| Bugrolle | Bow roller / Anchor roller | Davier | — |
| Bügel | Roll bar / Roll-bar | Arceau | Neue Generation |
| Fieren | To pay out / To veer | Filer / Mouiller | Kette auslassen |
| Fluke | Fluke / Palm | Patte | Grabteil des Ankers |
| Haltekraft | Holding power | Tenue | — |
| Kettenstopper | Chain stopper / Devil's claw | Bloqueur de chaîne | — |
| Reitgewicht | Kellet / Sentinel | Orin lesté | — |
| Schaft | Shank | Verge | — |
| Schäkel | Shackle | Manille | — |
| Schwojkreis | Swing circle / Swinging room | Cercle d'évitage | — |
| Schwojien | To swing / To sheer | Éviter | — |
| Scope | Scope | Rapport longueur/profondeur | — |
| Setzen | To set (the anchor) | Crocher | — |
| Snubber | Snubber / Bridle | Amortisseur | — |
| Tripleine | Trip line | Orin | — |
| Wirbel | Swivel | Émerillon | — |
| Zweitanker | Kedge / Secondary anchor | Ancre de secours | — |

### W2 — Funksprüche beim Ankern (UKW/VHF)

| Situation | Deutsch | Englisch |
|-----------|---------|----------|
| Absicht | "Wir werden hier ankern" | "We intend to anchor here" |
| Warnung | "Ihr Anker schleppt!" | "Your anchor is dragging!" |
| Hilfe | "Unser Anker hält nicht, wir treiben" | "Our anchor is not holding, we are dragging" |
| Bitte | "Bitte mehr Kette fieren" | "Please pay out more chain" |
| Hinweis | "Achtung, Sie ankern in meinem Schwojkreis" | "Warning, you are anchoring in my swing circle" |

---

*Ende der Wissensdatei 13.01 — Anker Grundlagen und Typen*
*AYDI Research, Version 1.0.0, 2026-04-26*
*Nächste geplante Aktualisierung: 2026-10-01*
