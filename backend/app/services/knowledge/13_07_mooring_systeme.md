# 13.07 — Mooring-Systeme: Vollständige Wissensreferenz

> **AYDI Wissensdatei 13.07** — Kategorie 13: Ankersysteme und Festmacher
> **Confidence-Quelle:** measured (Hersteller-TDS), documented (Hersteller-Kataloge, Testberichte, Hafenbehörden), estimated (Erfahrungswerte)
> **Letzte Aktualisierung:** 2026-04-26

---

```yaml
title: "Mooring-Systeme"
kategorie: "13 Ankersysteme und Festmacher"
unterkategorie: "07 Mooring-Systeme"
version: "1.0.0"
datum: "2026-04-26"
autor: "AYDI Research"
status: "validated"
confidence_quellen:
  - measured: "Hersteller-Datenblätter, zertifizierte Zugprüfungen, Hafenbehörden-Spezifikationen"
  - documented: "Practical Sailor, Yacht Magazine, RINA Papers, Herstellerkataloge, Hafenordnungen"
  - estimated: "Erfahrungswerte, Eigner-Konsens, Forum-Auswertung, regionale Praxis"
normen_referenzen:
  - "ISO 15084:2003 — Verankerung, Festmachen und Schleppen — Festpunkte"
  - "ISO 12217:2015/2022 — Stabilität und Auftrieb"
  - "ISO 15085:2003 — Mann-über-Bord-Verhütung"
  - "ISO 12401:2009 — Sicherheitsgurte und Sicherheitsleinen"
  - "CE Recreational Craft Directive 2013/53/EU"
  - "ABYC H-40 — Anchoring, Mooring and Strong Points"
  - "EN 14504:2006 — Inland navigation vessels — Floating landing stages and floating bridges on inland waters"
  - "ISO 13795:2020 — Ships and marine technology — Ship's mooring and towing fittings — Welded steel bollards for sea-going vessels"
  - "AS 3962:2001 — Guidelines for design of marinas (Australien)"
  - "NF P 98-800 — Équipements portuaires (Frankreich)"
abhängigkeiten:
  - "13_01_anker_grundlagen.md"
  - "13_02_ankerketten.md"
  - "13_03_ankerwinden.md"
  - "13_05_festmacher_fender.md"
  - "13_06_ankerbucht_bugbeschlaege.md"
```

---

## Inhaltsverzeichnis

1. [Einführung](#1-einführung)
2. [Grundlagen und Theorie](#2-grundlagen-und-theorie)
3. [Typenübersicht](#3-typenübersicht)
4. [Produktlinien und Hersteller](#4-produktlinien-und-hersteller)
5. [Regionale Besonderheiten](#5-regionale-besonderheiten)
6. [Sicherheit und Normen](#6-sicherheit-und-normen)
7. [Fehlerbild-Atlas](#7-fehlerbild-atlas)
8. [Troubleshooting](#8-troubleshooting)
9. [FAQ — Häufige Fragen](#9-faq--häufige-fragen)
10. [Glossar](#10-glossar)
11. [Schnell-Referenz](#11-schnell-referenz)
12. [ANHANG A — Fallstudien](#anhang-a--fallstudien)
13. [ANHANG B — Lastberechnungen](#anhang-b--lastberechnungen)
14. [ANHANG C — Confidence-Mapping](#anhang-c--confidence-mapping)
15. [ANHANG D — Normen-Zusammenfassung](#anhang-d--normen-zusammenfassung)
16. [ANHANG E — Wartungsintervalle](#anhang-e--wartungsintervalle)
17. [ANHANG F — Liegeplatz-Bewertung](#anhang-f--liegeplatz-bewertung)
18. [ANHANG G — Historische Entwicklung](#anhang-g--historische-entwicklung)
19. [ANHANG H — AYDI-Integration (Pydantic-Modelle)](#anhang-h--aydi-integration-pydantic-modelle)
20. [ANHANG I — Bewertungsschema](#anhang-i--bewertungsschema)
21. [ANHANG J — Troubleshooting-Entscheidungsbäume (erweitert)](#anhang-j--troubleshooting-entscheidungsbäume-erweitert)
22. [ANHANG K — Kostenkalkulation](#anhang-k--kostenkalkulation)
23. [ANHANG L — Regionale Hafenordnungen](#anhang-l--regionale-hafenordnungen)
24. [ANHANG M — Testprotokolle und Prüfverfahren](#anhang-m--testprotokolle-und-prüfverfahren)
25. [ANHANG N — Zusätzliche Fallstudien](#anhang-n--zusätzliche-fallstudien)
26. [ANHANG O — Eigner-Erfahrungen und Feldberichte](#anhang-o--eigner-erfahrungen-und-feldberichte)
27. [ANHANG P — Materialkunde Mooring-Systeme](#anhang-p--materialkunde-mooring-systeme)
28. [ANHANG Q — Mooring im Seenotfall](#anhang-q--mooring-im-seenotfall)
29. [ANHANG R — Zukunftstrends](#anhang-r--zukunftstrends)

---

## 1. Einführung

### 1.1 Bedeutung von Mooring-Systemen in der Yachtkonstruktion

Mooring-Systeme (Dauerliegeplatz-Systeme) umfassen alle Einrichtungen und Techniken, mit denen eine Yacht an einem festen Liegeplatz gesichert wird — im Gegensatz zum temporären Ankern auf freiem Wasser. Während Festmacherleinen und Fender (→ 13_05) die unmittelbaren Verbindungselemente zwischen Yacht und Steg beschreiben, behandelt diese Wissensdatei die übergeordneten Systeme: permanente Moorings, Mittelmeer-Moorings (Muringleinen), Pfahl-Moorings, Swing-Moorings, Mooringbojen und die dazugehörigen Techniken.

**Statistische Relevanz:**
- Ca. 70 % aller Yachten in Europa liegen während der Saison an einem festen Mooring-System (Marina, Bojenfeld, Pfahl-Liegeplatz).
- Im Mittelmeer nutzen geschätzt 85 % aller Marinas das Stern-to- oder Bow-to-System mit Muringleinen (Lazy Lines).
- In Skandinavien dominieren Pfahl-Liegeplätze (ca. 60 % aller Marinas in Schweden und Norwegen).
- Mooring-bezogene Schäden machen ca. 12–18 % aller Yachtversicherungsschäden aus (Pantaenius 2019–2024).
- Häufigste Schadensursachen: gebrochene Muringleine (28 %), Kollision beim Mittelmeer-Anlegen (22 %), durchgescheuertes Mooring-Grundgeschirr (19 %), Bojenmooring gerissen bei Starkwind (16 %), Pfahl-Mooring mit falschem Tidenhub (15 %).

### 1.2 Abgrenzung zu verwandten Wissensdateien

| Thema | Wissensdatei | Abgrenzung zu 13_07 |
|-------|-------------|---------------------|
| Anker und Ankertechnik | 13_01 | Temporäres Ankern auf freiem Wasser |
| Ankerketten | 13_02 | Ketten als Teil des Ankersystems, nicht des Mooring-Systems |
| Ankerwinden | 13_03 | Winsch für Anker, nicht für Mooring |
| Ankergeschirr | 13_04 | Schäkel, Wirbel am Anker |
| Festmacher und Fender | 13_05 | Leinen und Fender als Einzelkomponenten |
| Ankerbucht und Bugbeschläge | 13_06 | Bugrolle, Ankerkasten |
| **Mooring-Systeme (diese Datei)** | **13_07** | **Gesamtsystem: Boje, Pfahl, Med-Mooring, Lazy Line, permanentes Grundgeschirr** |

### 1.3 Historischer Kontext

Die Geschichte der Mooring-Systeme spiegelt die Entwicklung des Yachthafenwesens wider:

- **Vor 1950:** Yachten lagen an einfachen Holzpfählen oder an primitiven Bojen (Stein mit Trosse). Mittelmeer-Häfen: Heck an der Kaimauer mit eigenem Anker als Bug-Sicherung.
- **1950–1970:** Erste organisierte Marinas in den USA und Nordeuropa. Schwimm-Stege lösen feste Stege ab. Betonblock-Moorings als Standard für Bojenfelder.
- **1970–1990:** Mittelmeer-Marinas standardisieren das Stern-to-System. Erste Lazy-Line-Systeme in Frankreich und Kroatien. Pilz-Anker und Helix-Schraubanker für permanente Moorings.
- **1990–2005:** Elastische Mooring-Systeme (Seaflex) revolutionieren die Liegeplatztechnik. Kettenbegrenzung durch Schwimmkörper. Professionelles Marina-Management entsteht.
- **2005–2015:** Umweltauflagen erfordern Seegras-schonende Mooring-Systeme. Helical-Screw-Anker ersetzen Betonblöcke. Mooringbojen mit integrierter Leinenführung.
- **2015–heute:** Smartmooring-Systeme mit Lastsensoren. Umweltzertifizierungen für Mooring-Felder (Clean Marina, Blue Flag). Automatische Mooring-Assistenten für Marinas.

### 1.4 Qualitätsprinzipien für die AYDI-Bewertung

Jede Mooring-System-Bewertung in AYDI folgt diesen Grundsätzen:

1. **Confidence-Level auf jedem Befund.** Eine Mooring-Bewertung aus Fotoanalyse erhält maximal `visual_medium`. Nur dokumentierte Hafenbehörden-Angaben oder Herstellerdaten erhalten `measured`.
2. **Bootsklassen-Kalibrierung.** Ein Swing-Mooring mit 500 kg Betonblock ist für eine 8-m-Yacht ausreichend, für eine 15-m-Yacht lebensgefährlich unterdimensioniert.
3. **"Nicht beurteilbar" vor Spekulation.** Wenn der Zustand einer Muringleine unter Wasser nicht erkennbar ist, gibt AYDI `visual_insufficient` zurück.
4. **Regionale Kalibrierung.** Mooring-Praktiken unterscheiden sich fundamental zwischen Regionen. Was in Skandinavien Standard ist, existiert im Mittelmeer nicht.
5. **Umwelt-Bewertung.** Mooring-Systeme haben erhebliche Umweltauswirkungen (Seegras-Schäden, Sedimentstörung). AYDI bewertet auch die ökologische Verträglichkeit.

### 1.5 Geltungsbereich dieser Wissensdatei

Diese Datei deckt ab:
- Alle relevanten Mooring-Systemtypen für Segel- und Motoryachten von 6 bis 30+ Metern
- Permanente Moorings (Swing, Fore-and-Aft, Pfahl, Boje)
- Mittelmeer-Mooring (Stern-to, Bow-to, Lazy Lines, Muringleinen)
- Mooring-Bojen (Pick-up-Sticks, Pennants, Riser)
- Grundgeschirr (Anker, Ketten, Gewichte für permanente Moorings)
- Regionale Mooring-Praktiken (Mittelmeer, Skandinavien, UK, Karibik, Australien)
- Pydantic-v2-Modelle für die Integration in die AYDI-Analysepipeline

**Nicht behandelt:** Temporäres Ankern (→ 13_01), Festmacherleinen als Einzelkomponenten (→ 13_05), Klampen und Beschläge (→ 11_01 ff.), Schäkel und Verbinder (→ 12_01 ff.).

### 1.6 Mooring-Systeme im AYDI-Analyseprozess

Im AYDI-Analyseprozess werden Mooring-Systeme primär in folgenden Modulen bewertet:

| AYDI-Modul | Mooring-Relevanz | Typische Befunde |
|-----------|-----------------|-----------------|
| Compliance | Klampen-Dimensionierung für Mooring-Last | Unterdimensionierte Bugklampe, fehlende Lastrücktragung |
| Structural | Rumpfstruktur an Festmacherpunkten | Verstärkung unter Klampe unzureichend |
| Cost | Mooring-Betriebskosten als Teil der Gesamtkosten | Liegeplatzkosten, Wartungsbudget |
| Materials | Mooring-Hardware am Boot (Klampen, Klüsen) | Korrosion an Edelstahl-Klampen, Ermüdung an Klüsen |
| Service Patterns | Mooring-Schäden in Serviceberichten | Wiederkehrende Schamfilschäden, Festmacher-Probleme |
| Ergonomics | Mooring-Manöver-Ergonomie | Erreichbarkeit der Bugklampe, Bootshaken-Ablage |

**Pipeline-Zuordnung:**
- **Pipeline A (Structured):** Mooring-Dimensionierung basierend auf Yacht-Spezifikationen und Hafenbehörden-Daten
- **Pipeline B (Visual):** Zustandsbewertung von Pennant, Boje, Pfahl per Fotoanalyse
- **Pipeline C (Text):** Auswertung von Serviceberichten und Hafenordnungen

**Score Fusion für Mooring:**
- Structured: 0,70 (Berechnung, Datenblätter)
- Visual: 0,30 (Zustandsfotos)

### 1.7 Zielgruppen dieser Wissensdatei

| Zielgruppe | Relevante Abschnitte | Typische Fragestellung |
|-----------|---------------------|----------------------|
| Yacht-Eigner (Einsteiger) | Kap. 1, 3, 9 (FAQ), 11 (Schnell-Ref.) | „Welches Mooring brauche ich?" |
| Yacht-Eigner (erfahren) | Kap. 2, 4, 5, 7, 8 | „Ist mein Mooring ausreichend dimensioniert?" |
| Yachtdesigner | Kap. 2, 6, Anhang B, H | „Welche Klampen-Last muss ich für Mooring einplanen?" |
| Marina-Betreiber | Kap. 4, 5, 6, Anhang E, K, L | „Welche Mooring-Infrastruktur brauche ich?" |
| AYDI-Entwickler | Kap. 2, Anhang C, H, I | „Wie integriere ich Mooring-Daten in die Analyse-Pipeline?" |
| Versicherungen | Kap. 6, Anhang A, O | „Welcher Mooring-Standard ist versicherungsrelevant?" |

---

## 2. Grundlagen und Theorie

### 2.1 Mooring-Konfigurationen — Übersicht

Mooring-Systeme lassen sich in sechs Grundkonfigurationen einteilen, die sich in ihrer Belastungsaufnahme, ihrem Platzbedarf und ihrer regionalen Verbreitung grundlegend unterscheiden:

| Konfiguration | Befestigungspunkte | Schwojkreis | Platzbedarf | Typische Region | Confidence |
|---------------|-------------------|-------------|-------------|-----------------|------------|
| Swing Mooring (Einpunkt) | 1 (Bug) | 360° | Groß (r = LOA + Scope) | UK, Australien, Karibik | documented |
| Fore-and-Aft Mooring | 2 (Bug + Heck) | Minimal | Mittel (LOA × 1,3) | UK-Flüsse, Niederlande | documented |
| Pfahl-Mooring | 2–4 (Pfähle) | Minimal | Klein (LOA × 1,1) | Skandinavien, Norddeutschland | documented |
| Med Stern-to | 1 (Bug: Muringleine) + Heck am Steg | Kein | Sehr klein (LOA × 1,0) | Mittelmeer | documented |
| Med Bow-to | 1 (Heck: Muringleine) + Bug am Steg | Kein | Sehr klein (LOA × 1,0) | Mittelmeer (seltener) | documented |
| Bojenmooring (Besucher) | 1 (Bug) | Begrenzt | Mittel | Weltweit (Naturhäfen) | documented |

**Schematische Darstellung der Kraftvektoren:**

```
SWING MOORING (Einpunkt):
                Wind/Strom →
                ┌─────────┐
     Scope      │  YACHT  │ ← Schwojkreis 360°
   ┌────────────┤  (Bug)  │
   │            └─────────┘
   ○ Boje
   │ Riser
   │
  ─┼─ Grundkette
   │
  [█] Anker/Gewicht (Grund)


FORE-AND-AFT MOORING:
   ○ Boje Bug          ○ Boje Heck
   │                   │
   │    ┌─────────┐    │
   └────┤  YACHT  ├────┘
        └─────────┘
   │                   │
  [█] Anker Bug       [█] Anker Heck


MED STERN-TO:
   ════════════════ Steg/Kai ═══════════
        │Heck-    │Heck-    │Heck-
        │leine    │leine    │leine
      ┌─┴──┐   ┌─┴──┐   ┌─┴──┐
      │ Y1 │   │ Y2 │   │ Y3 │
      └─┬──┘   └─┬──┘   └─┬──┘
        │Muring  │Muring  │Muring
        │leine   │leine   │leine
   ─────┼────────┼────────┼───── Grundkette
        │        │        │
       [█]      [█]      [█]   Anker/Gewicht


PFAHL-MOORING:
     ╫ Pfahl       ╫ Pfahl
     │              │
     │ ┌──────────┐ │
     └─┤  YACHT   ├─┘
       └──────────┘
     │              │
     ╫ Pfahl       ╫ Pfahl
     (4-Pfahl-Variante)
```

### 2.2 Belastungsanalyse für Mooring-Systeme

#### 2.2.1 Windlast auf Yachten

Die Windlast ist die primäre Belastung auf ein Mooring-System. Sie berechnet sich nach:

```
F_wind = 0.5 × ρ_air × C_d × A × V²

Wobei:
  ρ_air = 1,225 kg/m³ (Luftdichte bei 15 °C, Meeresniveau)
  C_d   = Widerstandsbeiwert (0,8–1,2 für Yachten)
  A     = Windangriffsfläche (m²)
  V     = Windgeschwindigkeit (m/s)
```

**Windangriffsflächen nach Bootsklasse:**

| Bootsklasse | LOA (m) | A_längs (m²) | A_quer (m²) | C_d | Confidence |
|-------------|---------|--------------|-------------|-----|------------|
| Kleinsegler | 6–8 | 3–5 | 6–10 | 1,0 | estimated |
| Fahrtensegler | 9–12 | 5–9 | 10–18 | 1,0 | documented |
| Großsegler | 13–18 | 9–15 | 18–30 | 1,0 | documented |
| Superyacht (Segel) | 18–30 | 15–30 | 30–60 | 1,0 | documented |
| Motoryacht (klein) | 6–10 | 5–8 | 8–15 | 1,1 | estimated |
| Motoryacht (mittel) | 10–15 | 8–15 | 15–30 | 1,1 | documented |
| Motoryacht (groß) | 15–25 | 15–30 | 30–60 | 1,2 | documented |
| Katamaran | 10–15 | 8–14 | 15–25 | 1,0 | estimated |

**Windlast-Berechnungstabelle (ruhend, querab, keine Böenfaktoren):**

| Windstärke (Bft) | V (m/s) | V (kn) | Last 10 m² (kN) | Last 20 m² (kN) | Last 40 m² (kN) | Confidence |
|-------------------|---------|--------|-----------------|-----------------|-----------------|------------|
| 3 | 4,5 | 9 | 0,12 | 0,25 | 0,50 | calculated |
| 4 | 6,5 | 13 | 0,26 | 0,52 | 1,04 | calculated |
| 5 | 9,0 | 17 | 0,50 | 1,00 | 1,99 | calculated |
| 6 | 12,0 | 23 | 0,88 | 1,76 | 3,53 | calculated |
| 7 | 15,0 | 29 | 1,38 | 2,76 | 5,51 | calculated |
| 8 | 19,0 | 37 | 2,21 | 4,43 | 8,85 | calculated |
| 9 | 23,0 | 45 | 3,24 | 6,49 | 12,98 | calculated |
| 10 | 27,0 | 52 | 4,47 | 8,93 | 17,86 | calculated |
| 11 | 31,0 | 60 | 5,88 | 11,77 | 23,54 | calculated |
| 12 | 35,0+ | 68+ | 7,50+ | 15,01+ | 30,01+ | calculated |

**Böenfaktor:** In Böen steigt die Windlast um den Faktor 1,5–2,5 gegenüber der mittleren Windgeschwindigkeit. Für Mooring-Design wird ein Böenfaktor von 1,75 empfohlen (d. h. Designlast = 1,75 × mittlere Windlast).

#### 2.2.2 Strömungslast

Die Strömungslast ist besonders in Tidengewässern und Flussmündungen relevant:

```
F_strom = 0.5 × ρ_water × C_d × A_unter × V_strom²

Wobei:
  ρ_water   = 1.025 kg/m³ (Seewasser)
  C_d       = 1,0–1,5 (Unterwasserschiff)
  A_unter   = Lateralplan-Fläche (m²)
  V_strom   = Strömungsgeschwindigkeit (m/s)
```

| Strömung (kn) | V (m/s) | Last pro m² Lateralplan (N) | Confidence |
|---------------|---------|----------------------------|------------|
| 0,5 | 0,25 | 32 | calculated |
| 1,0 | 0,51 | 134 | calculated |
| 2,0 | 1,03 | 544 | calculated |
| 3,0 | 1,54 | 1.216 | calculated |
| 4,0 | 2,06 | 2.176 | calculated |

#### 2.2.3 Wellenlast (dynamisch)

Wellenbelastung erzeugt die höchsten Spitzenlasten auf ein Mooring-System. Die dynamische Zusatzlast entsteht durch:
- **Ruckbelastung** (Snatch Load): Boot fällt in ein Wellental, Leine wird plötzlich stramm
- **Surging**: Längsbewegung des Boots in der Welle
- **Yawing**: Gierbewegung um die Mooringbefestigung

**Dynamischer Lastfaktor nach Seegang:**

| Seegang | Signifikante Wellenhöhe (m) | Dynamischer Faktor | Mooring-Designlast | Confidence |
|---------|---------------------------|--------------------|--------------------|------------|
| Ruhig | 0–0,1 | 1,0 | Statische Last | calculated |
| Leicht | 0,1–0,5 | 1,3–1,5 | 1,5 × statisch | estimated |
| Mäßig | 0,5–1,0 | 1,5–2,0 | 2,0 × statisch | estimated |
| Grob | 1,0–2,0 | 2,0–3,0 | 3,0 × statisch | estimated |
| Schwer | >2,0 | 3,0–5,0 | Mooring ungeeignet | estimated |

**AYDI-Empfehlung:** Permanente Moorings müssen für mindestens Windstärke 9 (Böen bis 11) ausgelegt sein. Marinas in exponierten Lagen: Windstärke 10 (Böen bis 12). Der Sicherheitsfaktor auf die Designlast beträgt mindestens 3,0.

### 2.3 Mittelmeer-Mooring-Technik (Med Mooring)

#### 2.3.1 Grundprinzip

Beim Mittelmeer-Mooring (Med Mooring) liegt die Yacht mit dem Heck (Stern-to) oder Bug (Bow-to) am Steg. Die Gegenrichtung wird durch eine Muringleine (Mooring Line) oder den eigenen Anker gesichert. Dieses System maximiert die Anzahl der Yachten pro Stegmeter.

**Stern-to (Standard im Mittelmeer):**
- Heck am Steg mit 2–4 Heckleinen an Pollern/Klampen
- Bug an Muringleine (von Grundkette/Grundanker)
- Vorteile: Einfacher Landgang über Heck/Passerelle, mehr Privatsphäre im Bug
- Nachteile: Schwieriges Anlegen bei Wind querab, Propeller kann Muringleine aufwickeln

**Bow-to (seltener):**
- Bug am Steg mit 2 Bugleinen
- Heck an Muringleine
- Vorteile: Einfacher bei starkem Seitenwind (Bug schneidet besser), kein Propeller-Risiko für Muringleine
- Nachteile: Schwerer Landgang (Bug höher), weniger Privatsphäre, selten angeboten

#### 2.3.2 Muringleinen-System (Lazy Lines)

Lazy Lines sind vorinstallierte Leinen, die von der Grundkette am Meeresboden zum Steg geführt werden. Der Yachtführer nimmt die Lazy Line am Steg auf und zieht sie zum Bug (bei Stern-to) oder Heck (bei Bow-to).

**Aufbau eines typischen Lazy-Line-Systems:**

```
  ═══════════ Steg ═══════════
      │LL1│ │LL2│ │LL3│         ← Lazy Lines am Steg aufgehängt
      │    │ │    │ │    │
      │    │ │    │ │    │      ← Lazy Line (Polyester/Polypropylen)
      │    │ │    │ │    │
  ────┼────┼─┼────┼─┼────┼──── ← Grundkette (20–30 mm Kurzglied)
      │    │ │    │ │    │
     [S]  [S] [S]  [S] [S]  [S] ← Schäkel zur Grundkette
      │         │         │
     [█]       [█]       [█]   ← Grundanker/Betonblöcke

  LL = Lazy Line
  S  = Schäkel (verzinkt oder Edelstahl)
  █  = Grundanker (Betonblock, Pilzanker oder Helix-Anker)
```

**Lazy-Line-Dimensionierung:**

| Bootsklasse | LOA (m) | Lazy-Line-Durchmesser (mm) | Lazy-Line-Material | Bruchlast min (kN) | Confidence |
|-------------|---------|---------------------------|--------------------|--------------------|------------|
| Klein | 6–9 | 14–16 | Polyester DB | 25–35 | documented |
| Mittel | 9–13 | 16–20 | Polyester DB | 35–55 | documented |
| Groß | 13–18 | 20–24 | Polyester DB | 55–80 | documented |
| Superyacht | 18–25 | 24–32 | Polyester DB o. Nylon | 80–130 | documented |
| Megayacht | 25–40 | 32–44 | Nylon/HMPE | 130–250 | estimated |

#### 2.3.3 Anlegetechnik Stern-to — Schritt für Schritt

**Vorbereitung (vor Einfahrt in den Hafen):**

1. Fender an beiden Seiten (mindestens 3 pro Seite, eher 4)
2. Heckleinen auf beiden Seiten vorbereiten (jeweils 1,5 × Hafentiefe)
3. Bugklampe freihalten für Muringleine
4. Passerelle/Gangway bereithalten
5. Crew einweisen: eine Person am Bug (Muringleine annehmen), eine am Heck (Heckleinen übergeben), Skipper am Steuer
6. Bei Einhand-Segeln: Heckleinen mittschiffs führen (Cockpit), Muringleine muss vom Cockpit aus bedient werden können

**Anlegemanöver:**

1. Liegeplatz identifizieren (Nummer, Lazy Line finden)
2. Langsam rückwärts einfahren (1–2 kn, max. 0,5 kn bei letzten 3 Bootslängen)
3. Heckleinen an Land übergeben oder an Poller werfen
4. Muringleine aufnehmen (wird oft vom Marinapersonal gereicht oder liegt auf der Stegkante)
5. Muringleine zum Bug führen und auf Klampe/Poller belegen
6. Boot mit Heckleinen und Muringleine positionieren (ca. 30–50 cm Abstand Heck–Steg)
7. Passerelle auslegen
8. Feinabstimmung: Heckleinen gleichmäßig spannen, Muringleine so nachsetzen, dass der Bug nicht gegen Nachbarboote driftet

**Kritische Fehlerquellen beim Med-Mooring:**

| Fehler | Konsequenz | Häufigkeit | Confidence |
|--------|-----------|------------|------------|
| Zu schnelles Rückwärtsfahren | Rammen des Stegs, Heckschaden | 25 % aller Schäden | documented |
| Muringleine um Propeller | Manövrierunfähigkeit, Taucheinsatz nötig | 15 % | documented |
| Zu kurze Heckleinen | Boot driftet ab, Fenderversagen | 12 % | documented |
| Seitenwind nicht berücksichtigt | Abdrift auf Nachbarboot | 20 % | documented |
| Muringleine nicht gefunden/defekt | Improvisierter Anker-Einsatz nötig | 10 % | documented |
| Crew nicht eingewiesen | Chaos am Steg, Verletzungsgefahr | 18 % | estimated |

### 2.4 Pfahl-Mooring (Pile Mooring)

#### 2.4.1 Grundprinzip

Beim Pfahl-Mooring wird die Yacht zwischen mindestens zwei vertikalen Pfählen (Dalben, Mooring Piles) festgemacht. Die Pfähle sind im Meeresboden verankert und ragen über die Wasserlinie hinaus. Die Yacht wird mit Leinen an den Pfählen befestigt, wobei die Leinen über Ringe oder Ösen an den Pfählen laufen, um den Tidenhub auszugleichen.

**Konfigurationen:**

| Variante | Pfahl-Anzahl | Beschreibung | Typische Region | Confidence |
|----------|-------------|--------------|-----------------|------------|
| 2-Pfahl (längs) | 2 | Je 1 Pfahl an Bug und Heck | Skandinavien | documented |
| 2-Pfahl (quer) | 2 | 2 Pfähle an einer Seite + Steg | Deutschland (Ostsee) | documented |
| 4-Pfahl (Box) | 4 | Je 2 Pfähle an Bug und Heck | Niederlande, Belgien | documented |
| Pfahl + Steg | 1–2 | Pfahl(e) seitlich, Steg an der anderen | Norddeutschland | documented |
| Dalbenpaar | 2 | Yacht liegt zwischen 2 eng stehenden Dalben | Elbe, Weser | documented |

```
2-PFAHL (LÄNGS):

  ╫ Bugpfahl
  │
  │  Bugleine (mit Ring)
  │
  ┌┴─────────┐
  │  YACHT   │
  └┬─────────┘
  │
  │  Heckleine (mit Ring)
  │
  ╫ Heckpfahl


4-PFAHL (BOX):

  ╫ ─── Vorleine ──── ╫
  │                    │
  │    ┌──────────┐    │
  │    │  YACHT   │    │
  │    └──────────┘    │
  │                    │
  ╫ ─── Achterleine ── ╫
```

#### 2.4.2 Pfahl-Dimensionierung und Belastung

| Yacht-LOA (m) | Pfahl-Durchmesser min (mm) | Pfahl-Material | Einbautiefe (× Wassertiefe) | Seitenkraft max (kN) | Confidence |
|---------------|---------------------------|----------------|---------------------------|---------------------|------------|
| 6–8 | 150 | Holz (Eiche, Tropisch) | 1,5 | 5 | documented |
| 8–10 | 200 | Holz oder Stahl | 1,5 | 8 | documented |
| 10–13 | 250 | Stahl | 2,0 | 15 | documented |
| 13–18 | 300 | Stahl | 2,0 | 25 | documented |
| 18–25 | 400 | Stahl | 2,5 | 40 | documented |
| 25+ | 500+ | Stahl (Rohr) | 3,0 | 60+ | estimated |

**Pfahl-Ring-System für Tidenhub:**

In Tidengewässern sind die Leinen an Ringen befestigt, die vertikal am Pfahl gleiten können. Dies kompensiert den Tidenhub automatisch.

| Tidenbereich | Ring-Typ | Führungslänge | Material | Confidence |
|-------------|----------|---------------|----------|------------|
| <0,5 m (Ostsee) | Fester Ring | 1,0 m | Edelstahl 316L | documented |
| 0,5–2 m (Westliche Ostsee) | Gleitring | 2,5 m | Edelstahl 316L | documented |
| 2–5 m (Nordsee) | Gleitring auf Schiene | 6,0 m | Edelstahl 316L + HDPE | documented |
| 5–10 m (Atlantik) | Gleitring auf Schiene | 12,0 m | Edelstahl 316L + HDPE | documented |
| >10 m (Extremtide) | Schwimm-Pontonsystem | Variabel | Stahl + HDPE | estimated |

### 2.5 Swing Mooring (Einpunkt-Mooring)

#### 2.5.1 Grundprinzip

Beim Swing Mooring ist die Yacht nur an einem einzigen Punkt (Bug) befestigt. Sie dreht sich frei um den Mooringpunkt und richtet sich nach Wind und Strömung aus (Schwojen). Das Mooring besteht aus einem Grundanker/Grundgewicht, einer Grundkette (Riser Chain), einem Schwimmkörper (Boje) und einer Aufnehmeleine (Pennant/Pendant).

```
SWING-MOORING — Querschnitt:

  Wasseroberfläche ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                          ○ Boje (Schwimmkörper)
                          │
                          │ Pennant/Pendant (Leine, 2–4 m)
                          │
                          │ Pick-up Stick (optional)
                          │
                     ┌────┴────┐
                     │ Riser   │ ← Steigrohr oder Kette
                     │ (Kette  │    zum Grundgewicht
                     │  oder   │
                     │  Seil)  │
                     └────┬────┘
                          │
  Meeresboden ═══════════╤═══════════════════
                    ─────┼───── Grundkette (catenary)
                         │
                        [█] Grundanker/Gewicht
```

#### 2.5.2 Schwojkreis-Berechnung

Der Schwojkreis ist der Kreis, den die Yacht um den Mooringpunkt beschreiben kann:

```
r_schwoj = LOA + l_pennant + l_scope

Wobei:
  LOA       = Länge über alles der Yacht
  l_pennant = Länge der Aufnehmeleine (Pennant)
  l_scope   = Horizontale Kettenauslage am Grund

  Sicherheitsabstand zum nächsten Mooring:
  d_min = 2 × r_schwoj + 5 m (Sicherheitspuffer)
```

**Schwojkreis-Tabelle:**

| LOA (m) | Pennant (m) | Scope (m) | Schwojradius (m) | Min-Abstand (m) | Confidence |
|---------|------------|-----------|------------------|-----------------|------------|
| 8 | 3 | 5 | 16 | 37 | calculated |
| 10 | 3 | 6 | 19 | 43 | calculated |
| 12 | 4 | 7 | 23 | 51 | calculated |
| 15 | 4 | 8 | 27 | 59 | calculated |
| 18 | 5 | 10 | 33 | 71 | calculated |
| 22 | 5 | 12 | 39 | 83 | calculated |

### 2.6 Permanente Mooring-Design-Grundsätze

#### 2.6.1 Grundanker/Grundgewicht-Typen

| Typ | Haltekraft (× Eigengewicht) | Boden-Eignung | Vorteile | Nachteile | Confidence |
|-----|---------------------------|---------------|---------|-----------|------------|
| Betonblock (Dead Weight) | 0,5–0,8 | Alle Böden | Einfach, billig, zuverlässig | Schwer, benötigt Barge zum Setzen | documented |
| Pilzanker (Mushroom) | 2–4 (eingesogen) | Schlick, Sand | Hohe Haltekraft nach Einsaugen | Nur in weichen Böden, braucht 6–12 Monate zum Einsetzen | documented |
| Helix-Schraubanker | 5–15 | Ton, Sand, Schlick | Höchste Haltekraft/Gewicht, umweltschonend | Teuer, braucht Installationsgerät | documented |
| Drag-Embedment-Anker | 3–10 | Sand, Ton | Gute Haltekraft, selbst setzend | Richtungsabhängig, kann ausbrechen | documented |
| Kentledge (Stahlblock) | 0,5–0,8 | Alle Böden | Kompakter als Beton, recyclebar | Korrosion | estimated |
| Suction Caisson | 10–30 | Ton, Schlick | Extreme Haltekraft, entfernbar | Nur für Großanwendungen, teuer | documented |

#### 2.6.2 Lastberechnung für Mooring-Bojen

**Design-Last-Berechnung (vereinfacht):**

```
F_design = SF × (F_wind + F_strom + F_welle)

Wobei:
  SF      = Sicherheitsfaktor (min. 3,0 für permanente Moorings)
  F_wind  = Windlast bei Design-Windgeschwindigkeit (Bft 9 + Böenfaktor 1,75)
  F_strom = Strömungslast bei max. Tidenstrom
  F_welle = Dynamische Wellenzusatzlast (Faktor 1,5–3,0 der statischen Last)
```

**Design-Last-Tabelle für permanente Swing-Moorings:**

| Yacht-Kategorie | LOA (m) | Verdrängung (t) | Design-Windlast (kN) | Design-Strömungslast (kN) | Dynamischer Faktor | Design-Gesamtlast (kN) | SF 3,0 → Haltekapazität min (kN) | Confidence |
|-----------------|---------|-----------------|----------------------|--------------------------|--------------------|-----------------------|---------------------------------|------------|
| Jolle/Daysailer | 6–8 | 1–3 | 2,5 | 0,5 | 1,5 | 4,5 | 13,5 | estimated |
| Fahrtensegler | 9–12 | 4–10 | 5,0 | 1,5 | 1,5 | 9,8 | 29,3 | calculated |
| Cruiser-Racer | 10–13 | 6–12 | 6,5 | 2,0 | 1,8 | 15,3 | 45,9 | calculated |
| Langkieler | 10–14 | 8–15 | 7,0 | 3,0 | 1,5 | 15,0 | 45,0 | calculated |
| Großsegler | 14–18 | 15–30 | 12,0 | 4,0 | 2,0 | 32,0 | 96,0 | calculated |
| Motoryacht (mittel) | 10–15 | 10–25 | 10,0 | 2,5 | 1,8 | 22,5 | 67,5 | calculated |
| Motoryacht (groß) | 15–25 | 25–80 | 20,0 | 5,0 | 2,0 | 50,0 | 150,0 | estimated |

#### 2.6.3 Grundketten-Dimensionierung

Die Grundkette (Riser Chain) verbindet den Grundanker mit der Boje. Sie muss für die Gesamtlast plus Eigengewicht dimensioniert sein.

| Yacht-LOA (m) | Ketten-Durchmesser min (mm) | Kettenlänge (× Wassertiefe) | Ketten-Typ | Bruchlast (kN) | Confidence |
|---------------|----------------------------|----------------------------|------------|----------------|------------|
| 6–8 | 10 | 2,0 | Kurzglied verzinkt | 32 | documented |
| 8–10 | 12 | 2,0 | Kurzglied verzinkt | 46 | documented |
| 10–13 | 14 | 2,5 | Kurzglied verzinkt | 63 | documented |
| 13–16 | 16 | 2,5 | Kurzglied verzinkt | 82 | documented |
| 16–20 | 20 | 3,0 | Kurzglied verzinkt | 128 | documented |
| 20–25 | 22 | 3,0 | Kurzglied verzinkt | 155 | documented |
| 25–30 | 26 | 3,0 | Kurzglied verzinkt | 216 | estimated |

**Catenary-Effekt:** Die Grundkette bildet durch ihr Eigengewicht eine Kettenlinie (Catenary). Dieser Durchhang absorbiert Stoßlasten und verhindert, dass die volle Horizontallast direkt auf den Grundanker übertragen wird. Je schwerer die Kette, desto besser die Stoßdämpfung.

#### 2.6.4 Kettenermüdung und Korrosion

| Einflussfaktor | Auswirkung | Lebensdauer-Reduktion | Prüfintervall | Confidence |
|----------------|-----------|----------------------|---------------|------------|
| Korrosion (Meerwasser) | 0,1–0,3 mm/Jahr Materialverlust | −5–15 % pro Jahr | Jährlich | documented |
| Galvanische Korrosion | Verstärkt durch ungleiches Metall | −10–30 % Zusatz | Jährlich | documented |
| Ermüdung (Zyklen) | Wellenbelastung, Schwojbewegung | −2–5 % pro Jahr | 3 Jahre | documented |
| Bio-Fouling | Gewichtszunahme → reduzierter Catenary | Indirekt | Jährlich | estimated |
| Sediment-Abrasion | Scheuern an Grundkette | −5–10 % pro Jahr | Jährlich | estimated |

**AYDI-Empfehlung:** Grundketten für permanente Moorings sollten alle 5 Jahre professionell inspiziert und nach 10–15 Jahren ersetzt werden. Ketten in aggressiven Umgebungen (warmes Wasser, starke Strömung) alle 3 Jahre inspizieren.

---

## 3. Typenübersicht

### 3.1 Swing Moorings (Einpunkt-Bojen-Mooring)

#### 3.1.1 Klassisches Swing-Mooring

**Beschreibung:** Einfachstes permanentes Mooring-System. Yacht ist über Pennant und Boje mit einem Grundanker verbunden. Die Yacht schwojt frei um 360°.

**Aufbau:**
1. Grundanker (Betonblock, Pilzanker oder Helix-Anker)
2. Grundkette (Riser Chain) vom Anker zur Boje
3. Boje (Schwimmkörper, PE oder Stahl)
4. Pennant/Pendant (Aufnehmeleine vom Boot zur Boje)
5. Optional: Pick-up Stick (Aufnahmestange über der Boje)

**Vor- und Nachteile:**

| Aspekt | Bewertung | Details |
|--------|----------|---------|
| Kosten | ★★★★★ | Günstigste Mooring-Lösung (500–3.000 EUR) |
| Platzbedarf | ★★☆☆☆ | Großer Schwojkreis erforderlich |
| Sicherheit | ★★★☆☆ | Bei extremem Wind kann Grundanker ausbrechen |
| Komfort | ★★☆☆☆ | Kein Landgang ohne Beiboot |
| Umwelt | ★★★☆☆ | Kette kann Seegras beschädigen |
| Wartung | ★★★★☆ | Wenig Wartung, aber Unterwasser-Inspektion nötig |

#### 3.1.2 Fore-and-Aft-Mooring

**Beschreibung:** Yacht wird an Bug und Heck an je einem separaten Grundmooring befestigt. Kein Schwojkreis, Yacht bleibt in Position. Üblich in engen Flüssen und Gezeitengewässern.

**Aufbau:**
1. 2 Grundanker (Bug + Heck), unabhängig voneinander
2. 2 Riser-Ketten mit je einer Boje
3. 2 Pennants (Bug + Heck)
4. Optional: Elastische Zwischenstücke (Rubber Snubber)

**Vor- und Nachteile:**

| Aspekt | Bewertung | Details |
|--------|----------|---------|
| Kosten | ★★★☆☆ | Doppelte Grundanker, doppelte Ketten (2.000–6.000 EUR) |
| Platzbedarf | ★★★★★ | Kein Schwojkreis, minimaler Raum |
| Sicherheit | ★★★★☆ | Redundanz durch 2 Anker |
| Komfort | ★★☆☆☆ | Kein Landgang ohne Beiboot |
| Umwelt | ★★★☆☆ | 2 Ketten statt 1, mehr Grundberührung |
| Wartung | ★★★☆☆ | Doppelte Inspektion, komplexere Einfahrt |

**Kritische Überlegung:** Die beiden Grundanker müssen so positioniert sein, dass die Yacht bei wechselndem Tidenstrom weder auf den Bug-Anker noch auf den Heck-Anker zuläuft. Idealerweise liegen die Anker in der dominierenden Strom-/Windrichtung.

#### 3.1.3 Trott-Mooring (Trot Mooring)

**Beschreibung:** Mehrere Yachten liegen hintereinander an einer gemeinsamen Grundkette (Trotting Line). Jede Yacht hat eine eigene Aufnehmeleine, die von der Grundkette abzweigt.

**Aufbau:**
1. Schwere Grundkette (Trotting Line) zwischen 2 Hauptankern
2. Abzweig-Ketten mit Bojen für jede Yacht
3. Pennants von den Bojen zu den Yachten

**Typisch für:** Flussmündungen in Südengland (Solent, Dart, Fal), Australische Buchten

| Aspekt | Bewertung | Details |
|--------|----------|---------|
| Kosten | ★★★★☆ | Geteilte Infrastruktur, günstig pro Yacht |
| Platzbedarf | ★★★★☆ | Effizient (Yachten in Reihe) |
| Sicherheit | ★★★★☆ | Hauptkette als Rückgrat |
| Komfort | ★☆☆☆☆ | Kein Landgang, oft im Strom |
| Wartung | ★★☆☆☆ | Gemeinschaftliche Wartung nötig |

### 3.2 Pfahl-Moorings

#### 3.2.1 Skandinavischer Pfahl-Liegeplatz

**Beschreibung:** In Skandinavien der Standardliegeplatz. Die Yacht liegt zwischen zwei Pfählen (Bug- und Heckdalbe) oder zwischen einem Pfahl und einem Steg. Die Leinen laufen über Ringe oder Ösen an den Pfählen.

**Dimensionierung:**

| Yacht-LOA (m) | Pfahlabstand (m) | Breite zwischen Pfählen (m) | Leinendurchmesser (mm) | Confidence |
|---------------|------------------|-----------------------------|----------------------|------------|
| 6–8 | 9–11 | 3,5–4,0 | 12–14 | documented |
| 8–10 | 11–13 | 4,0–4,5 | 14–16 | documented |
| 10–12 | 13–15 | 4,5–5,0 | 16–18 | documented |
| 12–14 | 15–17 | 5,0–5,5 | 18–20 | documented |
| 14–16 | 17–20 | 5,5–6,5 | 20–22 | documented |

**Besonderheiten:**
- In Schweden oft kostenlose Gast-Pfähle in Naturhäfen (Naturhamn)
- Leinen immer mit Ruckdämpfer (Snubber) versehen
- Bei Tidenhub (selten in Ostsee, aber an Westküste) Gleitringe nötig
- Pfähle werden alle 10–15 Jahre erneuert (Holz) oder alle 30–40 Jahre (Stahl)

#### 3.2.2 Niederländischer Box-Liegeplatz

**Beschreibung:** In den Niederlanden und Belgien weit verbreitet. 4 Pfähle bilden eine „Box", in die die Yacht eingefahren und mit 4 Leinen befestigt wird.

**Merkmale:**
- Yacht fährt vorwärts in die Box ein
- 2 Vorleinen, 2 Achterleinen
- Oft mit Laufsteg (Fingerpontone) kombiniert
- Box-Breite: LOA-Breite + 0,5–1,0 m pro Seite

| Aspekt | Bewertung | Details |
|--------|----------|---------|
| Sicherheit | ★★★★★ | 4-Punkt-Befestigung, kein Schwojen |
| Platzbedarf | ★★★★★ | Minimaler Platz pro Yacht |
| Komfort | ★★★★★ | Direkter Landgang über Fingerponton |
| Kosten (Yacht) | ★★★★★ | Keine eigene Ausrüstung nötig |
| Kosten (Marina) | ★★☆☆☆ | Hohe Infrastruktur-Investition |

#### 3.2.3 Dalben-Liegeplatz (Norddeutsch)

**Beschreibung:** An der deutschen Nord- und Ostseeküste verbreitete Variante mit paarweisen Dalben. Die Yacht liegt zwischen zwei eng beieinander stehenden Dalbenpaaren.

**Technische Details:**
- Dalben: Eichen- oder Tropenholz-Pfähle, 200–300 mm Durchmesser
- Pfahlhöhe: 2–3 m über MHW (mittleres Hochwasser)
- Verbindung: Holzbolzen oder Stahlbänder zwischen Dalbenpaar
- Leinenführung: über Poller auf Dalbenkopf oder durch Ring
- Tidenhub-Ausgleich: automatisch durch lose Leinenführung

### 3.3 Mittelmeer-Mooring-Systeme

#### 3.3.1 Stern-to mit Muringleine (Standard)

**Beschreibung:** Die häufigste Mooring-Konfiguration im gesamten Mittelmeerraum. Yacht liegt mit dem Heck am Steg, der Bug wird von einer Muringleine (Lazy Line) gehalten, die an einer Grundkette befestigt ist.

**Infrastruktur der Marina:**

| Komponente | Material | Dimension (typ.) | Lebensdauer | Confidence |
|------------|----------|------------------|-------------|------------|
| Grundkette | Verzinkter Stahl, Kurzglied | 20–30 mm | 15–25 Jahre | documented |
| Grundanker | Betonblock oder Helix | 1.000–5.000 kg (Block) | 30+ Jahre | documented |
| Muringleine (Lazy Line) | Polyester oder Polypropylen | 16–24 mm | 3–7 Jahre | documented |
| Boje (Markierung) | PE oder PVC | Ø 200–400 mm | 5–10 Jahre | documented |
| Schäkel (Kette↔Leine) | Verzinkt oder Edelstahl | 12–20 mm | 10–15 Jahre | documented |
| Steg-Befestigung | Verzinkter Ring oder Poller | Variable | 20+ Jahre | documented |

**Abstand zwischen Liegeplätzen:**

| Yacht-LOA (m) | Liegeplatzbreite min (m) | Liegeplatzbreite empfohlen (m) | Confidence |
|---------------|-------------------------|-------------------------------|------------|
| 6–8 | 2,8 | 3,2 | documented |
| 8–10 | 3,5 | 4,0 | documented |
| 10–12 | 4,0 | 4,5 | documented |
| 12–14 | 4,5 | 5,2 | documented |
| 14–16 | 5,0 | 6,0 | documented |
| 16–20 | 6,0 | 7,0 | documented |
| 20–25 | 7,0 | 8,5 | documented |

#### 3.3.2 Bow-to (Bug zum Steg)

**Beschreibung:** Seltener als Stern-to, wird in einigen Häfen bevorzugt oder bei bestimmten Windverhältnissen angeboten. Der Bug liegt am Steg, das Heck wird durch eine Muringleine gehalten.

**Verbreitung:**

| Region | Bow-to-Anteil | Gründe | Confidence |
|--------|--------------|--------|------------|
| Kroatien | 10 % | Einige Häfen mit starkem Landwind | documented |
| Griechenland (Kykladen) | 15 % | Meltemi-bedingt, Bug schneidet besser | documented |
| Türkei | 5 % | Nur in speziellen Marinas | documented |
| Frankreich (Côte d'Azur) | 5 % | Vereinzelt, historisch | estimated |
| Spanien | <5 % | Selten | estimated |

**Vor- und Nachteile gegenüber Stern-to:**

| Aspekt | Bow-to | Stern-to | Gewinner |
|--------|--------|----------|----------|
| Anlegen bei Seitenwind | Besser (Bug schneidet) | Schwieriger | Bow-to |
| Landgang | Schwieriger (Bug höher) | Einfacher (Heck/Passerelle) | Stern-to |
| Privatsphäre | Geringer (Cockpit zum Steg) | Höher (Cockpit zur See) | Stern-to |
| Propeller-Risiko | Kein Risiko (Prop. zur See) | Prop. kann Muring fangen | Bow-to |
| Abgase | Zum Steg (nervig für Nachbarn) | Zur See (besser) | Stern-to |
| Ankermanöver (mit eigenem Anker) | Anker zum Heck → unüblich | Anker zum Bug → gewohnt | Stern-to |

#### 3.3.3 Ankern statt Muringleine (Med-Mooring mit eigenem Anker)

**Beschreibung:** In Häfen ohne Muringleinen-Infrastruktur lässt die Yacht ihren eigenen Buganker als „Gegengewicht" zum Heck am Steg fallen. Dies ist die traditionelle Form des Med-Moorings und wird in vielen Stadthäfen und kleineren Häfen noch praktiziert.

**Technik:**

1. Yacht fährt langsam rückwärts auf den Steg zu
2. Bei ca. 3–4 × Hafentiefe Entfernung zum Steg: Anker fallen lassen
3. Rückwärts weiter zum Steg, dabei Ankerkette ausgeben
4. Heckleinen am Steg belegen
5. Ankerkette leicht durchsetzen, damit der Bug auf Position bleibt

**Risiken:**

| Risiko | Beschreibung | Wahrscheinlichkeit | Schweregrad | Confidence |
|--------|-------------|-------------------|-------------|------------|
| Ankersalat | Eigener Anker verhakt sich mit Nachbar-Anker | Hoch (25–40 %) | Mittel | documented |
| Dragging | Anker hält nicht im Hafengrund (oft Schlick, Müll) | Mittel (15–25 %) | Hoch | documented |
| Ketten-Verwicklung | Eigene Kette überkreuzt Nachbar-Kette | Hoch (30–50 %) | Mittel | documented |
| Grundhindernisse | Anker fällt auf Kabel, Rohr, altes Wrack | Niedrig (5–10 %) | Hoch | documented |

**AYDI-Empfehlung:** Wo Muringleinen vorhanden sind, diese immer bevorzugen. Eigenen Anker im Hafen nur nutzen, wenn keine Alternative besteht. In jedem Fall: Nachbar-Anker und -Ketten beobachten, Position des eigenen Ankers merken (GPS-Waypoint).

#### 3.3.4 Lazy-Line-Systeme (Detail)

**Beschreibung:** Lazy Lines sind die vorinstallierten Verbindungsleinen zwischen der Grundkette am Meeresboden und dem Steg. Sie werden „lazy" (faul) genannt, weil sie lose im Wasser hängen und keine Spannung tragen, bis eine Yacht sie aufnimmt.

**Materialien und Ausführungen:**

| Typ | Material | Schwimmfähigkeit | Lebensdauer | Kosten/Stück | Confidence |
|-----|----------|-----------------|-------------|--------------|------------|
| Standard | Polypropylen (PP) | Ja (schwimmt) | 2–4 Jahre | 20–50 EUR | documented |
| Mittelklasse | Polyester (PES) | Nein (sinkt) | 4–7 Jahre | 40–80 EUR | documented |
| Premium | Polyester Double Braid | Nein (sinkt) | 5–10 Jahre | 60–120 EUR | documented |
| High-End | HMPE-Kern, PES-Mantel | Nein (sinkt) | 8–15 Jahre | 100–200 EUR | documented |
| Budget | PP-Monofil | Ja (schwimmt) | 1–3 Jahre | 10–25 EUR | estimated |

**Schwimmende vs. sinkende Lazy Lines:**

| Eigenschaft | Schwimmend (PP) | Sinkend (PES) | Confidence |
|-------------|----------------|---------------|------------|
| Aufnahme | Leichter (sichtbar) | Schwieriger (Bootshaken nötig) | documented |
| Propeller-Risiko | Höher (schwimmt an Oberfläche) | Geringer (liegt am Grund) | documented |
| UV-Degradation | Höher (an der Oberfläche) | Geringer (unter Wasser) | documented |
| Bewuchs | Weniger (an der Luft) | Mehr (unter Wasser) | documented |
| Bruchlast | Geringer (PP schwächer) | Höher (PES stärker) | documented |
| Marktanteil | 60 % (Standard) | 40 % (Premium-Marinas) | estimated |

### 3.4 Mooring-Bojen

#### 3.4.1 Besucherbojen (Visitor Moorings)

**Beschreibung:** Von Hafenbehörden oder Privateigentümern installierte Bojen in Ankergebieten, an denen Yachten temporär festmachen können. Verbreitet in Naturhäfen, Nationalparks und geschützten Buchten.

**Bojen-Typen:**

| Typ | Material | Durchmesser (mm) | Auftrieb (kg) | Für LOA bis (m) | Confidence |
|-----|----------|------------------|---------------|-----------------|------------|
| Standard-Kugelboje | PE, rotationsgeformt | 400–600 | 30–80 | 12 | documented |
| Großboje | PE, rotationsgeformt | 600–900 | 80–200 | 18 | documented |
| Zylindrische Boje | PE oder Stahl | Ø 400–800, L 600–1200 | 50–300 | 20 | documented |
| Navigations-Mooring-Boje | Stahl, lackiert | 800–1500 | 200–1000 | 25+ | documented |
| Pick-up-Boje | PE | 200–400 | 5–20 | Hilfsboje | documented |

#### 3.4.2 Pick-up Sticks (Aufnahmestangen)

**Beschreibung:** Vertikale Stangen, die über die Boje hinausragen und das Aufnehmen der Boje erleichtern. Besonders nützlich bei hohem Freibord oder Einhandsegeln.

**Aufbau:**
- Fiberglas- oder Aluminium-Stange, 0,5–1,5 m über Boje
- Oben: Aufnehmeöse oder Haken
- An der Stange: Pennant (Aufnehmeleine) befestigt
- Markierungsfahne oder Reflektorband am oberen Ende

| Material | Länge (m) | Sichtbarkeit | Stabilität | Kosten | Confidence |
|----------|-----------|-------------|------------|--------|------------|
| Fiberglas | 0,8–1,5 | Gut (mit Fahne) | Biegsam, bricht nicht | 30–60 EUR | documented |
| Aluminium | 0,5–1,2 | Mittel | Steif, kann verbiegen | 20–40 EUR | documented |
| PVC | 0,5–1,0 | Mittel | Steif, kann brechen | 10–20 EUR | estimated |

#### 3.4.3 Pennants (Aufnehmeleinen)

**Beschreibung:** Die Leine, mit der die Yacht an der Mooring-Boje befestigt wird. Sie verläuft von der Boje oder dem Pick-up Stick zum Bug der Yacht.

**Dimensionierung:**

| Yacht-LOA (m) | Pennant-Durchmesser (mm) | Material | Länge (m) | Bruchlast min (kN) | Confidence |
|---------------|-------------------------|----------|-----------|---------------------|------------|
| 6–8 | 14–16 | Nylon DB | 3–4 | 30–40 | documented |
| 8–10 | 16–18 | Nylon DB | 4–5 | 40–55 | documented |
| 10–13 | 18–22 | Nylon DB | 5–6 | 55–80 | documented |
| 13–16 | 22–24 | Nylon DB | 5–7 | 80–100 | documented |
| 16–20 | 24–28 | Nylon DB | 6–8 | 100–130 | documented |
| 20–25 | 28–32 | Nylon DB | 7–10 | 130–170 | estimated |

**Wichtig:** Der Pennant ist die schwächste Stelle im Mooring-System, da er der UV-Strahlung, Schamfil und biologischem Bewuchs am stärksten ausgesetzt ist. Regelmäßige Inspektion (alle 6 Monate) und Austausch (alle 3–5 Jahre) sind obligatorisch.

### 3.5 Permanente Anker für Mooring-Systeme

#### 3.5.1 Betonblock (Dead Weight Anchor)

**Beschreibung:** Der einfachste und älteste Grundanker-Typ. Ein massiver Betonblock wird auf den Meeresboden abgesenkt und hält durch sein Eigengewicht.

| Yacht-LOA (m) | Blockgewicht min (kg) | Blockgröße (cm) | Haltekraft (kN) | Kosten (EUR) | Confidence |
|---------------|----------------------|-----------------|-----------------|-------------|------------|
| 6–8 | 500 | 60×60×60 | 3–4 | 200–400 | documented |
| 8–10 | 1.000 | 80×80×60 | 5–8 | 350–600 | documented |
| 10–13 | 2.000 | 100×100×80 | 10–16 | 500–1.000 | documented |
| 13–16 | 3.000 | 120×120×80 | 15–24 | 700–1.500 | documented |
| 16–20 | 5.000 | 140×140×100 | 25–40 | 1.000–2.500 | documented |
| 20–25 | 8.000 | 160×160×120 | 40–64 | 1.500–4.000 | estimated |

#### 3.5.2 Pilzanker (Mushroom Anchor)

**Beschreibung:** Anker mit pilzförmigem Kopf, der sich in weichem Boden (Schlick, Ton, feiner Sand) einzieht. Nach vollständigem Einsaugen (6–12 Monate) erreicht er ein Vielfaches seiner nominellen Haltekraft.

| Gewicht (kg) | Haltekraft frisch (kN) | Haltekraft eingesaugt (kN) | Für LOA bis (m) | Boden | Confidence |
|-------------|----------------------|--------------------------|-----------------|-------|------------|
| 50 | 2 | 6–8 | 8 | Schlick | documented |
| 100 | 4 | 12–16 | 10 | Schlick/Sand | documented |
| 200 | 8 | 24–32 | 13 | Schlick/Sand | documented |
| 500 | 15 | 50–70 | 16 | Schlick | documented |
| 1.000 | 25 | 80–120 | 20 | Schlick | documented |

#### 3.5.3 Helix-Schraubanker (Helical Screw Anchor)

**Beschreibung:** Moderne Mooring-Ankerlösung. Schraubenförmige Flügel werden hydraulisch in den Meeresboden geschraubt. Höchste Haltekraft pro Gewicht, umweltschonend (keine Bodenversiegelung).

| Modell-Klasse | Flügeldurchmesser (mm) | Installationstiefe (m) | Haltekraft (kN) | Für LOA bis (m) | Kosten inkl. Installation | Confidence |
|---------------|----------------------|----------------------|-----------------|-----------------|--------------------------|------------|
| Leicht | 200–300 | 2–4 | 20–40 | 10 | 1.500–3.000 EUR | documented |
| Mittel | 300–400 | 3–6 | 40–80 | 15 | 3.000–6.000 EUR | documented |
| Schwer | 400–600 | 4–8 | 80–150 | 20 | 5.000–10.000 EUR | documented |
| Extra-schwer | 600–800 | 6–12 | 150–300 | 30 | 8.000–20.000 EUR | estimated |

**Boden-Eignung:**

| Boden | Eignung | Anmerkung | Confidence |
|-------|---------|-----------|------------|
| Ton (fest) | ★★★★★ | Idealer Boden für Helix-Anker | documented |
| Ton (weich) | ★★★★☆ | Gut, aber geringere Haltekraft als in festem Ton | documented |
| Sand (fein) | ★★★★☆ | Gut, stabiler Halt | documented |
| Sand (grob) | ★★★☆☆ | Akzeptabel, höhere Installationstiefe empfohlen | documented |
| Kies | ★★☆☆☆ | Schwierig zu installieren | documented |
| Fels | ☆☆☆☆☆ | Nicht möglich | documented |
| Koralle | ☆☆☆☆☆ | Nicht möglich, zudem ökologisch verboten | documented |

### 3.6 Ground Tackle (Grundgeschirr) für permanente Moorings

#### 3.6.1 Komponenten-Übersicht

| Komponente | Funktion | Material | Lebensdauer | Inspektionsintervall | Confidence |
|------------|----------|----------|-------------|---------------------|------------|
| Grundanker | Verankerung im Boden | Beton/Stahl/Helix | 15–50 Jahre | 5 Jahre | documented |
| Grundkette (Bodenstück) | Anker ↔ Riser-Verbindung | Verzinkter Stahl | 10–20 Jahre | 3 Jahre | documented |
| Riser Chain (Steigkette) | Boden ↔ Boje | Verzinkter Stahl | 8–15 Jahre | 2 Jahre | documented |
| Wirbel (Swivel) | Verdrehschutz | Edelstahl 316L oder verzinkt | 5–10 Jahre | Jährlich | documented |
| Schäkel | Verbindung Kette↔Kette, Kette↔Leine | Verzinkter Stahl | 8–15 Jahre | 2 Jahre | documented |
| Boje | Auftrieb, Markierung | PE, PVC | 5–10 Jahre | Jährlich | documented |
| Pennant | Boje ↔ Yacht | Nylon/Polyester | 3–5 Jahre | 6 Monate | documented |

#### 3.6.2 Schäkel-Dimensionierung für Mooring-Ketten

| Kettendurchmesser (mm) | Schäkelgröße (mm) | Bruchlast (kN) | Typ | Confidence |
|------------------------|-------------------|----------------|-----|------------|
| 10 | 12 | 48 | Rundschäkel verzinkt | documented |
| 12 | 14 | 68 | Rundschäkel verzinkt | documented |
| 14 | 16 | 92 | Rundschäkel verzinkt | documented |
| 16 | 19 | 120 | Rundschäkel verzinkt | documented |
| 20 | 22 | 188 | Rundschäkel verzinkt | documented |
| 22 | 25 | 228 | Rundschäkel verzinkt | documented |
| 26 | 28 | 320 | Rundschäkel verzinkt | documented |

---

## 4. Produktlinien und Hersteller

### 4.1 Polyform — Mooring-Bojen und Fender

**Herkunft:** Norwegen (Ålesund)
**Marktposition:** Weltmarktführer für Bojen und Fender im Freizeitbootsbereich

#### 4.1.1 Polyform Mooring-Bojen

| Modell | Typ | Durchmesser (mm) | Auftrieb (kg) | Empf. Yacht-LOA (m) | Farbe | Preis (EUR) | Confidence |
|--------|-----|------------------|---------------|---------------------|-------|-------------|------------|
| MB-1 | Mooringboje | 380 | 20 | 6–8 | Rot/Gelb | 45–65 | documented |
| MB-2 | Mooringboje | 460 | 35 | 8–10 | Rot/Gelb | 65–95 | documented |
| MB-3 | Mooringboje | 540 | 55 | 10–13 | Rot/Gelb | 85–120 | documented |
| MB-4 | Mooringboje | 630 | 80 | 13–16 | Rot/Gelb | 110–155 | documented |
| MB-5 | Mooringboje | 760 | 140 | 16–20 | Rot/Gelb | 155–210 | documented |
| CM-2 | Kommerzielle Boje | 560 | 60 | Markierung | Rot/Gelb/Weiß | 95–130 | documented |
| CM-3 | Kommerzielle Boje | 700 | 120 | Markierung/Mooring | Rot/Gelb/Weiß | 135–185 | documented |
| CC-4 | Cylindrische Boje | Ø 460, L 810 | 65 | 10–14 | Weiß/Blau | 85–115 | documented |
| CC-5 | Cylindrische Boje | Ø 550, L 1020 | 120 | 14–18 | Weiß/Blau | 120–165 | documented |

**Technische Merkmale aller Polyform Mooring-Bojen:**
- Material: Linear-Polyethylen (LLDPE), rotationsgeformt
- UV-Stabilisiert: 8+ Jahre bei kontinuierlicher Exposition
- Durchstichfest: keine Luftfüllung, geschäumter Kern (bei einigen Modellen)
- Augbolzen: Edelstahl 316 oder verzinkter Stahl, Schwerlast-Rating
- Farben: Signalrot, Signalgelb, Weiß, Blau (je nach Regulierung)
- Temperaturbereich: −30 °C bis +60 °C

#### 4.1.2 Polyform Pick-up-Bojen

| Modell | Durchmesser (mm) | Auftrieb (kg) | Pennant-Durchlass | Preis (EUR) | Confidence |
|--------|------------------|---------------|-------------------|-------------|------------|
| PB-1 | 200 | 3 | 16 mm | 15–25 | documented |
| PB-2 | 280 | 8 | 20 mm | 25–40 | documented |
| PB-3 | 350 | 15 | 24 mm | 35–55 | documented |

### 4.2 Hazelett Marine — Mooring-Systeme

**Herkunft:** USA (Colchester, Vermont)
**Marktposition:** Spezialist für elastische Mooring-Systeme und Mooring-Pendants

#### 4.2.1 Hazelett Elastic Mooring Pendants

**Funktionsprinzip:** Elastischer Gummikern in textiler Ummantelung absorbiert Stoßlasten und reduziert die Peak-Last auf Grundanker und Yacht.

| Modell | Yacht-LOA (m) | Dehnung | Bruchlast (kN) | Arbeitslast (kN) | Preis (EUR) | Confidence |
|--------|--------------|---------|----------------|-------------------|-------------|------------|
| EMP-1 | 6–8 | 50 % | 30 | 10 | 80–120 | documented |
| EMP-2 | 8–11 | 50 % | 50 | 17 | 120–180 | documented |
| EMP-3 | 11–14 | 50 % | 75 | 25 | 180–260 | documented |
| EMP-4 | 14–18 | 50 % | 110 | 37 | 260–380 | documented |
| EMP-5 | 18–22 | 45 % | 150 | 50 | 380–520 | estimated |

**Vorteile elastischer Pendants:**
- Reduktion der Spitzenlast auf den Grundanker um 40–60 %
- Weniger Ruckbelastung (Snatch Loads) an Bugklampe
- Längere Lebensdauer des gesamten Mooring-Systems
- Ruhigerer Liegeplatz (weniger Surge-Bewegung)

#### 4.2.2 Hazelett Mooring Whips

**Beschreibung:** Federstahl-Stangen, die seitlich am Steg montiert sind und die Yacht vom Steg fernhalten. Ersetzen teilweise Fender bei Steg-Liegeplätzen.

| Modell | Yacht-LOA (m) | Länge (m) | Federkraft (kN) | Montage | Preis/Paar (EUR) | Confidence |
|--------|--------------|-----------|-----------------|---------|------------------|------------|
| MW-12 | 6–8 | 3,0 | 0,8 | Steg | 300–500 | documented |
| MW-14 | 8–10 | 3,6 | 1,2 | Steg | 400–650 | documented |
| MW-16 | 10–13 | 4,2 | 1,8 | Steg | 550–800 | documented |
| MW-18 | 13–16 | 4,8 | 2,5 | Steg | 700–1.000 | documented |
| MW-20 | 16–20 | 5,4 | 3,5 | Steg | 900–1.300 | estimated |

### 4.3 Seaflex — Elastische Mooring-Systeme

**Herkunft:** Schweden (Västervik)
**Marktposition:** Weltmarktführer für elastische Unterwasser-Mooring-Systeme, besonders für Schwimm-Stege und umweltschonende Moorings

#### 4.3.1 Seaflex Mooring-System

**Funktionsprinzip:** Gummiseil-basiertes elastisches System, das zwischen dem Grundanker und dem Schwimm-Steg oder der Boje installiert wird. Es absorbiert Tidenhub, Wellenbewegung und Windlasten elastisch, ohne feste Ketten.

**Komponenten:**
1. Grundanker (Helix-Schraubanker oder Betonblock)
2. Seaflex-Einheit (Gummiseil in Schutzhülle)
3. Verbindungselemente (Edelstahl 316L)
4. Obere Befestigung (am Schwimm-Steg oder an Boje)

| Modell | Zugkraft SWL (kN) | Bruchlast (kN) | Dehnung max (%) | Länge (m) | Für Anwendung | Preis (EUR) | Confidence |
|--------|-------------------|----------------|-----------------|-----------|---------------|-------------|------------|
| SF-6 | 6 | 18 | 100 | 1,5–6,0 | Kleine Bojen | 500–1.200 | documented |
| SF-12 | 12 | 36 | 100 | 2,0–8,0 | Schwimm-Stege (klein) | 800–2.000 | documented |
| SF-20 | 20 | 60 | 100 | 2,0–10,0 | Schwimm-Stege (mittel) | 1.200–3.000 | documented |
| SF-35 | 35 | 105 | 100 | 2,0–12,0 | Schwimm-Stege (groß) | 2.000–5.000 | documented |
| SF-50 | 50 | 150 | 85 | 2,0–15,0 | Superyacht-Moorings | 3.000–7.000 | documented |
| SF-80 | 80 | 240 | 80 | 3,0–18,0 | Kommerzielle Anwendungen | 5.000–12.000 | estimated |

**Umweltvorteile:**
- Keine Kettenschleppe am Meeresboden → Schutz von Seegras (Posidonia, Zostera)
- Keine Sedimentaufwirbelung
- Keine Geräusche (kein Kettenrasseln)
- Zertifiziert für Einsatz in Meeresschutzgebieten (diverse EU-Mitgliedsstaaten)
- Lebensdauer: 25+ Jahre (Gummi unter Wasser altert kaum)

#### 4.3.2 Seaflex SX-System (für Einzelyachten)

**Beschreibung:** Speziell für Einzelyacht-Moorings (Swing oder Fore-and-Aft) entwickelte Version des Seaflex-Systems.

| Modell | Yacht-LOA (m) | SWL (kN) | Bruchlast (kN) | Preis (EUR) | Confidence |
|--------|--------------|---------|----------------|-------------|------------|
| SX-8 | 6–8 | 8 | 24 | 600–1.000 | documented |
| SX-15 | 8–12 | 15 | 45 | 1.000–1.800 | documented |
| SX-25 | 12–16 | 25 | 75 | 1.500–2.800 | documented |
| SX-40 | 16–22 | 40 | 120 | 2.500–4.500 | documented |

### 4.4 Mantus Marine — Permanente Mooring-Anker

**Herkunft:** USA (Sarasota, Florida)
**Marktposition:** Aufsteigender Spezialist für hochwertige Anker und Mooring-Zubehör

#### 4.4.1 Mantus Permanent Mooring Hardware

| Produkt | Typ | Dimensionen | SWL (kN) | Material | Preis (EUR) | Confidence |
|---------|-----|-------------|---------|----------|-------------|------------|
| Mantus Swivel | Wirbel für Mooring | 8–25 mm | 25–180 | Edelstahl 316L | 80–350 | documented |
| Mantus Chain Hook | Kettenhaken | 8–16 mm | 30–100 | Edelstahl 316L | 50–120 | documented |
| Mantus Bridle | Mooring-Bridle | 12–20 mm | 35–100 | Nylon + Edelstahl | 100–250 | documented |
| Mantus Snubber | Ruckdämpfer | 14–22 mm | 20–60 | Nylon 3-karätiges | 40–90 | documented |

#### 4.4.2 Mantus Mooring-Anker

| Modell | Gewicht (kg) | Haltekraft im Sand (kN) | Haltekraft im Schlick (kN) | Für LOA bis (m) | Preis (EUR) | Confidence |
|--------|-------------|------------------------|---------------------------|-----------------|-------------|------------|
| M1-Permanent | 15 | 40 | 25 | 8 | 250–400 | documented |
| M2-Permanent | 25 | 70 | 45 | 12 | 400–650 | documented |
| M3-Permanent | 40 | 110 | 70 | 16 | 600–950 | documented |
| M4-Permanent | 60 | 160 | 100 | 20 | 850–1.300 | documented |
| M5-Permanent | 100 | 250 | 160 | 25 | 1.200–1.800 | estimated |

### 4.5 Weitere Hersteller und Systeme

#### 4.5.1 Seajet (Helix-Anker)

**Herkunft:** Neuseeland
**Spezialisierung:** Helix-Schraubanker für umweltschonende Moorings

| Modell | Flügel-Ø (mm) | Installationstiefe (m) | Haltekraft (kN) | Boden | Preis inkl. Inst. (EUR) | Confidence |
|--------|---------------|----------------------|-----------------|-------|------------------------|------------|
| SJ-200 | 200 | 3–4 | 30 | Ton/Sand | 2.000–3.500 | documented |
| SJ-300 | 300 | 4–6 | 60 | Ton/Sand | 3.500–5.500 | documented |
| SJ-400 | 400 | 5–8 | 100 | Ton/Sand | 5.000–8.000 | documented |
| SJ-600 | 600 | 6–10 | 180 | Ton/Sand | 8.000–14.000 | estimated |

#### 4.5.2 Eco Mooring Systems

**Herkunft:** Australien
**Spezialisierung:** Umweltschonende Moorings für Seegras-Schutzgebiete

| System | Beschreibung | Umweltzertifizierung | Kosten (EUR) | Confidence |
|--------|-------------|---------------------|-------------|------------|
| Eco Mooring Standard | Helix-Anker + elastisches Pendant | Great Barrier Reef | 3.000–6.000 | documented |
| Eco Mooring Premium | Doppel-Helix + Seaflex | Great Barrier Reef | 5.000–10.000 | documented |
| Eco Mooring Seagrass | Speziell für Posidonia-Gebiete | EU Natura 2000 | 4.000–8.000 | documented |

#### 4.5.3 Lazy-Line-Systeme — Hersteller

| Hersteller | System | Material | Besonderheit | Region | Confidence |
|-----------|--------|----------|-------------|--------|------------|
| Rigomar | Lazy-Line-Set | Polyester DB | Vorgefertigte Sets inkl. Schäkel | Mittelmeer | documented |
| Mediterranean Mooring | Komplettsystem | PP/PES | Grundkette + Lazy Lines + Bojen | Mittelmeer | documented |
| Poralu Marine | Marina-Infrastruktur | PES/HMPE | Integriert in Schwimmsteg-Systeme | Weltweit | documented |
| Marinetek | Marina-Infrastruktur | PES/HMPE | Finnisches System, Schwimm-Stege | Weltweit | documented |
| Bellingham Marine | Marina-Infrastruktur | PES | US-Standard-Schwimmstegsystem | Weltweit | documented |

---

## 5. Regionale Besonderheiten

### 5.1 Mittelmeer (Mediterranean Mooring Practices)

#### 5.1.1 Allgemeine Merkmale

| Aspekt | Beschreibung | Confidence |
|--------|-------------|------------|
| Dominant-System | Stern-to mit Lazy Line (90 %) | documented |
| Tidenhub | Gering (0,1–0,4 m), vernachlässigbar | documented |
| Windverhältnisse | Thermische Winde (nachmittags), Meltemi, Mistral, Scirocco | documented |
| Wassertiefe (Häfen) | 2–8 m (Stadthäfen oft <4 m) | documented |
| Grundbeschaffenheit | Sand/Schlick (oft mit Müll durchsetzt) | documented |
| Besonderheit | Dicht belegte Häfen, enge Abstände, Sommerchaos | documented |

#### 5.1.2 Länderspezifische Besonderheiten

**Kroatien:**
- Modernste Marina-Infrastruktur im Mittelmeer (ACI-Marinas)
- Lazy Lines in fast allen Marinas vorhanden
- Muring-Qualität: hoch (regelmäßig gewartet)
- Kosten: 50–150 EUR/Nacht (12 m, Hauptsaison)
- Besonderheit: Bora-Wind (NE) kann in einigen Häfen 100+ kn erreichen → Moorings entsprechend dimensioniert
- Stadtkai-Moorings (ohne Lazy Line): häufig in Stadthäfen der Inseln

**Griechenland:**
- Große Qualitätsunterschiede zwischen Marinas und Stadthäfen
- Marinas: meist Lazy Lines vorhanden, Qualität variabel
- Stadthäfen (Limani): oft ohne Muringleinen, eigener Anker nötig
- Meltemi-Gefahr (Juli/August): Böen bis 45 kn aus N/NE
- Kosten: 30–120 EUR/Nacht (12 m, Hauptsaison)
- Besonderheit: Viele freie Stadtkai-Plätze ohne Gebühr (Qualität gering)

**Türkei:**
- Moderne Marinas an der Ägäis und Riviera-Küste
- Lazy Lines in professionellen Marinas, Stadthäfen ohne
- Marinero-Hilfe beim Anlegen üblich (und erwartet)
- Kosten: 30–80 EUR/Nacht (12 m, Hauptsaison)
- Besonderheit: „Gulet-Stil"-Mooring mit Heckanker in engen Buchten (Göcek-Buchten)

**Frankreich (Côte d'Azur):**
- Höchste Marina-Standards und höchste Preise in Europa
- Alle Marinas mit Lazy Lines, oft Premium-Polyester
- Kosten: 80–300 EUR/Nacht (12 m, Hauptsaison in Saint-Tropez bis Cannes)
- Besonderheit: Superyacht-Moorings in Antibes, Monaco, Saint-Tropez — Liegeplätze bis 60 m+

**Italien:**
- Regionale Unterschiede groß (Sardinien vs. Neapel)
- Norditalien (Ligurien, Toskana): moderne Marinas mit Lazy Lines
- Süditalien: viele einfache Stadthäfen ohne Infrastruktur
- Kosten: 40–200 EUR/Nacht (12 m, Hauptsaison)
- Besonderheit: Einige Häfen verlangen Bug-to (bow-to) wegen traditioneller Hafengeometrie

**Spanien:**
- Balearen: Premium-Marinas mit voller Infrastruktur
- Festlandküste: Mischung aus modernen Marinas und einfachen Häfen
- Kosten: 40–150 EUR/Nacht (12 m, Hauptsaison)
- Besonderheit: Hafengebühren teilweise staatlich reguliert

#### 5.1.3 Typische Probleme im Mittelmeer

| Problem | Häufigkeit | Ursache | Lösung | Confidence |
|---------|-----------|--------|--------|------------|
| Muringleine um Propeller | 15 % aller Anlegevorgänge | Schwimmende PP-Leine, zu viel Rückwärtsgang | Sinkende PES-Leine verwenden, langsam manövrieren | documented |
| Nachbar-Kollision beim Anlegen | 10 % | Seitenwind, zu schnell, keine Crew | Crew einweisen, bei >15 kn querab warten | documented |
| Muringleine gerissen | 5–8 % pro Saison | UV-Degradation, Alter, Korrosion am Schäkel | Jährliche Inspektion, Austausch alle 5 Jahre | documented |
| Boot driftet nachts ab | 3–5 % | Defekte Muringleine, löst sich vom Steg | Eigene Leine als Backup zum Bug | documented |
| Passerelle-Schaden | 5 % | Falsche Höhe, zu starke Bewegung | Passerelle mit Gelenk und Rollen verwenden | documented |

### 5.2 Skandinavien (Nordic Mooring Practices)

#### 5.2.1 Allgemeine Merkmale

| Aspekt | Beschreibung | Confidence |
|--------|-------------|------------|
| Dominant-System | Pfahl-Mooring (60 %), Steg + Pfahl (25 %), Boje (15 %) | documented |
| Tidenhub | Ostsee: 0–0,3 m; Westküste NO/SE: 0,5–2,0 m | documented |
| Windverhältnisse | Westwindlage dominant, Herbststürme bis 10 Bft | documented |
| Wassertemperatur | 0–18 °C (Winter → Eis!) | documented |
| Grundbeschaffenheit | Fels (Schären), Sand, Ton, Schlick | documented |
| Besonderheit | Naturhäfen (Naturhamn), Schären-Navigation, Eis im Winter | documented |

#### 5.2.2 Schwedische Schären-Mooring-Technik

**Beschreibung:** In den schwedischen Schären (Stockholm, Göteborg, West Coast) ist das Festmachen am Fels eine eigenständige Tradition:

1. **Heckanker + Bug an Fels:** Yacht fährt mit dem Bug auf eine Felsklippe zu, wirft den Heckanker, und befestigt Bugleinen an natürlichen Felsringen oder eingemauerten Ringen.
2. **Pfahl-Mooring in Naturhäfen:** Kostenlose Pfähle stehen in vielen Naturhäfen zur Verfügung.
3. **Schärenring:** In den Fels gebohrte Edelstahlringe (Ø 20–25 mm) als Festmacherpunkte.

| Technik | Ausrüstung nötig | Schwierigkeitsgrad | Confidence |
|---------|------------------|--------------------|------------|
| Felsring-Mooring | 2 × 30 m Leine, Buganker | Mittel | documented |
| Pfahl-Mooring | 4 × 15 m Leine | Leicht | documented |
| Heckanker + Bug-Fels | Anker, Kette, 2 × 30 m Leine | Hoch | documented |
| Boje in Naturhafen | 1 × 10 m Pennant | Leicht | documented |

#### 5.2.3 Finnische Mooring-Besonderheiten

- **Winter-Mooring:** Boote müssen vor dem Zufrieren ausgewassert werden (Oktober/November)
- **Eis-Dalben:** Verstärkte Stahlpfähle, die Eisdruck standhalten
- **Bugspirale:** Elektrische Bugpropeller als „Eisbrecher" beim Einfahren
- **Vierasvenesatama:** Gästehäfen mit standardisierten Pfahl-Moorings

#### 5.2.4 Norwegische Fjord-Moorings

- **Fjord-Moorings:** Tiefwasser (20–100 m+) macht Ankern unmöglich, Pfahl oder Felsring sind die einzige Option
- **Strommoorings:** In Fjordmündungen mit starkem Tidenstrom müssen Leinen überdimensioniert sein
- **Kommunale Gästehäfen (Gjestehavn):** Standardisierte Pfahl-Moorings in fast jedem Küstenort

### 5.3 Vereinigtes Königreich (UK Mooring Practices)

#### 5.3.1 Allgemeine Merkmale

| Aspekt | Beschreibung | Confidence |
|--------|-------------|------------|
| Dominant-System | Swing-Mooring (40 %), Schwimmsteg (35 %), Trott-Mooring (15 %), Pfahl (10 %) | documented |
| Tidenhub | 2–12 m (extrem!) — Bristol Channel bis 14 m | documented |
| Strömung | Stark in Flussmündungen und Gezeitenkanälen | documented |
| Regulierung | Crown Estate verwaltet Meeresgrund, Mooring-Lizenzen erforderlich | documented |
| Kosten | Mooring-Lizenz: 200–2.000 GBP/Jahr (je nach Region) | documented |

#### 5.3.2 Britische Mooring-Typen

**Swinging Mooring (am häufigsten):**
- Standard in Flussmündungen (Solent, Dart, Fal, Helford)
- Crown Estate Lizenz für jeden einzelnen Mooringplatz
- Regelmäßige Inspektion durch Harbour Master vorgeschrieben
- Typischer Grundanker: Pilzanker (250–1.000 kg) oder Betonblock

**Pile Mooring (Hamble, Itchen, Medina):**
- In Gezeitenflüssen verbreitet
- Gleitringe an Pfählen für 2–5 m Tidenhub
- Oft kombiniert mit Schwimmsteg (Finger Pontoon)

**Drying Mooring:**
- In Trockenfallhäfen (Tidenhub >4 m) liegt die Yacht bei Niedrigwasser auf dem Grund
- Yacht muss trockenfallgeeignet sein (Kiel-Typ, Stützen/Beine)
- Leinen müssen extrem lang sein (Tidenhub-Ausgleich)
- Typische Regionen: Cornwall, Wales, Bretagne

| Mooring-Typ | Lizenkosten/Jahr (GBP) | Yacht-LOA (m) | Region | Confidence |
|-------------|----------------------|---------------|--------|------------|
| Swing (Solent) | 800–2.000 | 8–14 | Hampshire | documented |
| Swing (West Country) | 400–1.200 | 8–14 | Devon/Cornwall | documented |
| Pile (Hamble) | 1.500–3.500 | 10–16 | Hampshire | documented |
| Drying (Cornwall) | 200–600 | 6–10 | Cornwall | documented |
| Marina-Berth (Solent) | 3.000–8.000 | 10–14 | Hampshire | documented |

### 5.4 Karibik (Caribbean Mooring Practices)

#### 5.4.1 Allgemeine Merkmale

| Aspekt | Beschreibung | Confidence |
|--------|-------------|------------|
| Dominant-System | Swing-Mooring/Boje (60 %), Ankerfeld (30 %), Marina (10 %) | documented |
| Tidenhub | Gering (0,3–0,6 m) | documented |
| Windverhältnisse | Passatwinde (E/NE, 12–25 kn), Hurrikansaison Juni–November | documented |
| Wassertemperatur | 24–30 °C (ganzjährig) | documented |
| Grundbeschaffenheit | Sand, Koralle, Seegras | documented |
| Besonderheit | Hurrikansicherheit, Korallenriff-Schutz, National-Park-Bojen | documented |

#### 5.4.2 Nationalpark-Moorings

In vielen karibischen Inselstaaten sind Besucherbojen in Marinepark-Gebieten Pflicht (Ankern verboten):

| Land/Gebiet | Bojen-System | Kosten/Nacht | Ankerverbot | Confidence |
|------------|-------------|-------------|-------------|------------|
| British Virgin Islands | National Parks Trust | 30–40 USD | Ja (in Parks) | documented |
| US Virgin Islands | National Park Service | 15–26 USD | Ja (in Parks) | documented |
| Bonaire | STINAPA | 10–25 USD | Ja (gesamte Küste) | documented |
| Dominica | DEMA | 5–15 USD | Ja (in Parks) | documented |
| Martinique | Parc Naturel | 10–20 EUR | Ja (in Parks) | documented |
| Guadeloupe | Parc National | 10–20 EUR | Ja (in Parks) | documented |

**Zustand der Bojen:** Qualität und Wartung variieren stark. AYDI-Empfehlung: Pennant immer selbst mitbringen, Zustand der Boje vor Festmachen visuell prüfen, bei Zweifeln eigenen Anker als Backup setzen.

#### 5.4.3 Hurrikansicherheit

| Maßnahme | Beschreibung | Wirksamkeit | Confidence |
|----------|-------------|-------------|------------|
| Hurrikan-Mooring (permanent) | Überdimensioniertes Swing-Mooring mit Helix-Anker | Mittel (Kat 1–2) | documented |
| Mangroven-Mooring | Yacht in Mangrovenkanal mit 6–8 Leinen an Bäumen | Hoch (Kat 1–3) | documented |
| Hurrikan-Hole | Geschützte Bucht mit mehreren Ankern (Spider-Web-Technik) | Mittel–Hoch | documented |
| Auswassern | Yacht an Land auf Trailern/Ständern, verzurrt | Höchste Sicherheit | documented |
| Marina mit Hurrikan-Pfählen | Spezial-Pfähle, 2–3 m über Sturmflut-Niveau | Hoch (Kat 1–3) | documented |

**AYDI-Empfehlung:** Kein Mooring-System bietet 100 % Sicherheit bei einem Hurrikan der Kategorie 3+. Die sicherste Option ist immer das Auswassern und Verzurren an Land oder das Verlassen der Hurrikanzone.

### 5.5 Australien (Australian Mooring Practices)

#### 5.5.1 Allgemeine Merkmale

| Aspekt | Beschreibung | Confidence |
|--------|-------------|------------|
| Dominant-System | Swing-Mooring (65 %), Marina (25 %), Pfahl (10 %) | documented |
| Tidenhub | Variabel: 0,5 m (Sydney) bis 8+ m (Darwin) | documented |
| Regulierung | State-basiert, streng (insb. NSW, QLD) | documented |
| Umweltauflagen | Seegras-Schutz (Posidonia, Zostera), Korallenriff-Schutz | documented |
| Kosten | Mooring-Lizenz: 500–5.000 AUD/Jahr | documented |
| Besonderheit | Eco-Moorings Pflicht in vielen Gebieten seit 2010 | documented |

#### 5.5.2 Australische Mooring-Regulierung

**New South Wales (NSW):**
- Roads and Maritime Services (RMS) verwaltet alle Moorings
- Jedes Mooring benötigt eine Lizenz und jährliche Inspektion
- Eco-Moorings (Helix-Anker) Pflicht in Seegras-Gebieten seit 2015
- Warteliste für Mooring-Plätze in Sydney Harbour: 3–10 Jahre

**Queensland (QLD):**
- Maritime Safety Queensland (MSQ) zuständig
- Great Barrier Reef Marine Park: nur zugelassene Moorings, kein Ankern
- Public Moorings in beliebten Ankerplätzen (Whitsundays): Pflichtnutzung

| Staat | Regulierungsbehörde | Inspektionspflicht | Eco-Mooring-Pflicht | Wartezeit Lizenz | Confidence |
|-------|--------------------|--------------------|---------------------|-----------------|------------|
| NSW | RMS | Jährlich | Ja (Seegras-Gebiete) | 3–10 Jahre | documented |
| QLD | MSQ | 2 Jahre | Ja (GBRMP) | 1–5 Jahre | documented |
| VIC | Parks Victoria | 2 Jahre | Teilweise | 1–3 Jahre | documented |
| WA | DoT | 2 Jahre | Teilweise | 1–3 Jahre | estimated |
| TAS | MAST | 3 Jahre | Nein | <1 Jahr | estimated |

#### 5.5.3 Spezialfall: Zyklonsicherheit (Nordaustralien)

**Zyklonsaison:** November bis April (Northern Territory, Queensland).

**Mooring-Anforderungen in Zyklon-Gebieten:**

| Maßnahme | Beschreibung | Pflicht? | Confidence |
|----------|-------------|---------|------------|
| Zyklon-Plan | Jede Marina muss einen schriftlichen Zyklon-Plan haben | Ja | documented |
| Zyklon-Mooring | Überdimensioniertes Swing-Mooring (SF 5,0 statt 3,0) | Empfohlen | documented |
| Auswasserung | Ab Zyklon-Warnung: Yacht muss ausgewassert werden | Ja (viele Marinas) | documented |
| Zyklon-Pfähle | Spezial-Stahlpfähle, 3 m über Sturmflut-Niveau | Ja (Marinas Darwin, Cairns) | documented |
| Versicherung | Zyklon-Mooring-Nachweis für Versicherungsschutz | Meist ja | documented |

**Kosten für Zyklon-Mooring (Swing) im Vergleich:**

| Komponente | Standard-Mooring | Zyklon-Mooring | Faktor | Confidence |
|------------|-----------------|---------------|--------|------------|
| Grundanker | 2.000 kg Beton | 5.000 kg Beton + Helix-Backup | 2,5× | estimated |
| Kette | 14 mm × 10 m | 22 mm × 15 m | 3× | estimated |
| Pennant | 18 mm Nylon DB | 28 mm Nylon DB, doppelt | 3× | estimated |
| **Gesamt** | ~3.000 AUD | ~10.000 AUD | 3,3× | estimated |

#### 5.5.4 Great Barrier Reef Moorings

| Mooring-Typ | Beschreibung | Kapazität (LOA) | Kosten/Nacht (AUD) | Confidence |
|-------------|-------------|-----------------|---------------------|------------|
| Public Mooring (gelb) | Kostenlos, max. 14 Nächte | <15 m | 0 | documented |
| Reef Protection Mooring | In sensiblen Riffen | <20 m | 0–10 | documented |
| Private Tourism Mooring | Für Touroperator | <40 m | Lizenzgebunden | documented |
| Superyacht Mooring | Spezielle Hochlast-Moorings | <60 m | Auf Anfrage | estimated |

---

## 6. Sicherheit und Normen

### 6.1 Relevante Normen und Standards

| Norm/Standard | Titel | Relevanz für Mooring | Confidence |
|---------------|-------|---------------------|------------|
| ISO 15084:2003 | Verankerung, Festmachen und Schleppen — Festpunkte | Klampen- und Festmacher-Dimensionierung | documented |
| ISO 12217:2015/2022 | Stabilitäts- und Auftriebsanforderungen | Bootsstabilität am Mooring bei Starkwind | documented |
| ISO 15085:2003 | Mann-über-Bord-Verhütung | Sicherheit beim Mooring-Manöver | documented |
| AS 3962:2001 | Guidelines for Design of Marinas | Australischer Standard für Marina-Moorings | documented |
| BS 6349 | Maritime Works | Britischer Standard für Hafenbauwerke | documented |
| EN 14504:2006 | Inland Navigation — Schwimmende Landestege und Brücken | Schwimmsteg-Anforderungen (Marina-Infrastruktur) | documented |
| ABYC H-40 | Anchoring, Mooring and Strong Points | US-Standard für Festpunkte | documented |
| ISO 13795:2020 | Geschweißte Stahlpoller (Festmacher-/Schleppausrüstung, Seeschiffe) | Poller-Dimensionierung (große Yachten, Superyachten) | documented |
| PIANC Report 2016 | Criteria for Movements of Moored Vessels | Bewegungsgrenzen für geankerte Schiffe | documented |

### 6.2 Sicherheitsfaktoren und Mindest-Anforderungen

| Komponente | Sicherheitsfaktor (SF) min | Prüfintervall | Lebensdauer max | Confidence |
|------------|---------------------------|---------------|-----------------|------------|
| Grundanker (permanent) | 3,0 | 5 Jahre | 30+ Jahre | documented |
| Grundkette | 3,0 | 2–3 Jahre | 10–15 Jahre | documented |
| Riser Chain | 3,0 | 1–2 Jahre | 8–12 Jahre | documented |
| Schäkel | 4,0 | 1 Jahr | 8–10 Jahre | documented |
| Wirbel (Swivel) | 4,0 | 1 Jahr | 5–8 Jahre | documented |
| Pennant/Pendant | 3,0 | 6 Monate | 3–5 Jahre | documented |
| Boje | 2,0 (Auftrieb) | 1 Jahr | 5–10 Jahre | documented |
| Muringleine (Lazy Line) | 3,0 | 1 Jahr | 3–7 Jahre | documented |
| Elastisches Pendant | 3,0 | 1 Jahr | 5–10 Jahre | documented |

### 6.3 Personensicherheit beim Mooring-Manöver

| Risiko | Beschreibung | Schutzmaßnahme | Confidence |
|--------|-------------|----------------|------------|
| Hand-/Finger-Einklemmung | Leine unter Last auf Klampe | Handschuhe, nie Finger in Auge der Leine | documented |
| Rückschlag-Leine | Brechende Leine schnellt zurück | Stehbereich hinter gespannter Leine meiden | documented |
| Überboard bei Bojenaufnahme | Übergewicht beim Greifen der Boje | Bootshaken verwenden, nicht über Reling lehnen | documented |
| Quetschung zwischen Yacht und Steg | Rumpf drückt gegen Steg | Nie Gliedmaßen zwischen Boot und Steg | documented |
| Sturz auf nassem Steg | Rutschiger Steg bei Mooring-Manöver | Geeignetes Schuhwerk, keine Eile | documented |
| Propeller-Verletzung | Person im Wasser bei laufendem Motor | Motor aus bei Personen im Wasser | documented |

### 6.4 Versicherungsrechtliche Aspekte

| Aspekt | Beschreibung | Auswirkung | Confidence |
|--------|-------------|-----------|------------|
| Mooring-Wartungspflicht | Eigner muss Mooring in ordnungsgemäßem Zustand halten | Bei Verstoß: Kürzung der Versicherungsleistung | documented |
| Dokumentationspflicht | Wartungsnachweise, Inspektionsberichte aufbewahren | Nachweis bei Schadenfall | documented |
| Marina-Haftung | Marina haftet für Infrastruktur (Lazy Lines, Grundketten) | Regressanspruch bei Marina-Versagen | documented |
| Bojen-Nutzung auf eigenes Risiko | Nicht geprüfte Bojen: kein Versicherungsschutz bei Versagen | Eigene Absicherung (Backup-Anker) | documented |
| Überdimensionierung | Keine Pflicht, aber empfohlen | Kein Leistungsverlust bei Übererfüllung | documented |
| Hurrikan-/Sturmklauseln | Viele Policen fordern Vorbereitungsmaßnahmen | Bei Nichtbefolgen: Leistungskürzung möglich | documented |

### 6.5 Elektrische Sicherheit am Mooring

| Risiko | Beschreibung | Schutzmaßnahme | Confidence |
|--------|-------------|----------------|------------|
| Galvanische Korrosion | Ungleiches Metall am Mooring (Stahl + Edelstahl) | Opfer-Anoden an Kette/Schäkel, oder gleiche Metalle verwenden | documented |
| Streustrom (Marina) | Landstrom-Fehler erzeugt Strom im Wasser | Galvanischer Isolator oder Trenntransformator | documented |
| Blitzeinschlag am Mooring | Yacht am Mooring ist höchster Punkt | Blitzableiter-System, Erdung über Kiel | documented |
| Elektrolyse an Unterwasser-Metall | Beschleunigter Materialverlust am Mooring-Geschirr | Regelmäßige Anoden-Kontrolle, Potentialmessung | documented |

### 6.6 Umweltschutz-Normen für Mooring-Systeme

| Schutzgut | Bedrohung durch Mooring | Schutzmaßnahme | Regulierung | Confidence |
|-----------|------------------------|----------------|-------------|------------|
| Seegras (Posidonia oceanica) | Kettenschleppe zerstört Seegras | Eco-Mooring (elastisch, ohne Kettenschleppe) | EU Habitat-Richtlinie 92/43/EWG | documented |
| Seegras (Zostera marina) | Grundanker beschädigt Wurzelwerk | Helix-Anker statt Betonblock | EU Habitat-Richtlinie | documented |
| Korallenriffe | Anker/Kette zerstört Korallen | Permanente Mooring-Bojen, Ankerverbot | Diverse nationale Gesetze | documented |
| Sediment | Kettenbewegung wirbelt Sediment auf | Elastische Systeme (Seaflex) | AS 3962, diverse | documented |
| Meeressäuger | Leinenverfangung | Sinkende Leinen, keine Schleifen im Wasser | NOAA, diverse | documented |

---

## 7. Fehlerbild-Atlas

### Fehlerbild MO-01 — Gebrochene Muringleine

| Attribut | Detail |
|----------|--------|
| **Bezeichnung** | Gebrochene oder gerissene Muringleine (Lazy Line) |
| **Schweregrad** | KRITISCH |
| **Erkennungsmerkmale** | Boot driftet vom Steg ab, Muringleine hängt lose im Wasser, Bruchstelle sichtbar (gezackt, ausgefranst) |
| **Typische Ursache** | UV-Degradation (PP-Leinen), Schamfil an Grundkette/Schäkel, Überlastung bei Starkwind, Alter (>5 Jahre) |
| **Betroffene Bootsklassen** | Alle |
| **Region** | Mittelmeer (Schwerpunkt) |
| **Sofortmaßnahme** | Eigenen Anker sofort setzen oder zweite Leine zum Steg |
| **Langfristige Lösung** | Muringleine austauschen, PES statt PP wählen, Schäkel-Verbindung prüfen |
| **Confidence** | documented |
| **Visueller Hinweis** | Faserbruch sichtbar, Farbveränderung der Leine (bleich/weiß statt original), weiche/poröse Oberfläche |

### Fehlerbild MO-02 — Korrodierter Mooring-Schäkel

| Attribut | Detail |
|----------|--------|
| **Bezeichnung** | Fortgeschrittene Korrosion an Mooring-Schäkeln |
| **Schweregrad** | KRITISCH |
| **Erkennungsmerkmale** | Rotbraune Korrosion, Materialverlust sichtbar, Bolzen festgerostet, Querschnitt reduziert |
| **Typische Ursache** | Verzinkung aufgebraucht, galvanische Korrosion (ungleiches Metall), fehlende Wartung |
| **Betroffene Bootsklassen** | Alle |
| **Sofortmaßnahme** | Schäkel sofort ersetzen, temporär mit Leine sichern |
| **Langfristige Lösung** | Edelstahl 316L-Schäkel verwenden, jährliche Inspektion |
| **Confidence** | documented |

### Fehlerbild MO-03 — Verschlissene Grundkette

| Attribut | Detail |
|----------|--------|
| **Bezeichnung** | Abgenutzte oder korrodierte Grundkette (Riser Chain) |
| **Schweregrad** | HOCH |
| **Erkennungsmerkmale** | Reduzierter Glieddurchmesser (Messung mit Schieblehre), tiefe Rostnarben, gelängte Glieder, deformierte Glieder |
| **Typische Ursache** | Alterung (>10 Jahre), Korrosion, Sediment-Abrasion, fehlende Inspektion |
| **Betroffene Bootsklassen** | Alle (besonders >12 m) |
| **Prüfkriterium** | Materialabtrag >10 % des Nenn-Durchmessers → sofort ersetzen |
| **Sofortmaßnahme** | Kette durch Taucher inspizieren lassen, temporär doppelte Sicherung |
| **Langfristige Lösung** | Kette ersetzen, Inspektionsintervall 3 Jahre |
| **Confidence** | documented |

### Fehlerbild MO-04 — Mooring-Boje gesunken

| Attribut | Detail |
|----------|--------|
| **Bezeichnung** | Mooring-Boje unter Wasser oder kaum sichtbar |
| **Schweregrad** | HOCH |
| **Erkennungsmerkmale** | Boje nicht auffindbar, nur bei Niedrigwasser sichtbar, Pennant liegt am Grund |
| **Typische Ursache** | Leck in der Boje, Bewuchs (Gewicht), zu kurzer Riser, Boje von Schiff überfahren |
| **Betroffene Bootsklassen** | Alle |
| **Sofortmaßnahme** | Boje suchen (Taucher oder Dragnetz), provisorische Boje befestigen |
| **Langfristige Lösung** | Boje ersetzen, Auftriebsreserve >50 % wählen |
| **Confidence** | documented |

### Fehlerbild MO-05 — Pfahl-Neigung/Bruch

| Attribut | Detail |
|----------|--------|
| **Bezeichnung** | Geneigter oder gebrochener Mooring-Pfahl |
| **Schweregrad** | KRITISCH |
| **Erkennungsmerkmale** | Pfahl steht schief, Risse am Pfahlfuß sichtbar, Pfahl vibriert bei Belastung |
| **Typische Ursache** | Eisgang, Schiffsanprall, Sedimenterosion, Holzfäule (bei Holzpfählen), Ermüdung |
| **Region** | Skandinavien, Norddeutschland, UK |
| **Sofortmaßnahme** | Liegeplatz wechseln, Hafenmeister informieren |
| **Langfristige Lösung** | Pfahl ersetzen, Stahlpfahl statt Holzpfahl, Pfahlfußschutz |
| **Confidence** | documented |

### Fehlerbild MO-06 — Propeller-in-Muringleine

| Attribut | Detail |
|----------|--------|
| **Bezeichnung** | Muringleine oder Pennant um Propeller oder Welle gewickelt |
| **Schweregrad** | HOCH |
| **Erkennungsmerkmale** | Motor blockiert, Vibration, Leine nicht frei, Boot manövrierunfähig |
| **Typische Ursache** | Schwimmende PP-Muringleine, zu viel Rückwärtsgang beim Stern-to-Anlegen, Leine nicht gesichert |
| **Sofortmaßnahme** | Motor sofort AUS, Taucher rufen, ggf. selbst schnorcheln und mit Messer frei schneiden |
| **Langfristige Lösung** | Sinkende PES-Leinen verwenden, Leinenabweiser am Propeller, Technik verbessern |
| **Confidence** | documented |

### Fehlerbild MO-07 — Unzureichende Grundanker-Haltekraft

| Attribut | Detail |
|----------|--------|
| **Bezeichnung** | Grundanker des Moorings hat nachgegeben (Dragging) |
| **Schweregrad** | KRITISCH |
| **Erkennungsmerkmale** | Boje hat Position geändert (GPS), Yacht hat sich verdreht, Grundkette ist straff statt mit Durchhang |
| **Typische Ursache** | Unterdimensionierter Anker, Bodenveränderung, extreme Belastung (Sturm) |
| **Sofortmaßnahme** | Zusätzlichen eigenen Anker setzen, Liegeplatz verlassen wenn möglich |
| **Langfristige Lösung** | Grundanker upgraden (Helix statt Betonblock), regelmäßige GPS-Positionskontrolle der Boje |
| **Confidence** | documented |

### Fehlerbild MO-08 — UV-Degradation des Pennants

| Attribut | Detail |
|----------|--------|
| **Bezeichnung** | UV-geschädigter Pennant/Aufnehmeleine |
| **Schweregrad** | MITTEL bis HOCH |
| **Erkennungsmerkmale** | Farbveränderung (Ausbleichung), spröde Oberfläche, Fasern lösen sich, reduzierte Dehnfähigkeit |
| **Typische Ursache** | Permanente UV-Exposition an der Wasseroberfläche, keine Schutzummantelung |
| **Prüfkriterium** | Leine zwischen den Fingern biegen: bricht die Oberfläche → ersetzen |
| **Sofortmaßnahme** | Pennant sofort ersetzen |
| **Langfristige Lösung** | UV-stabilisierte Leinen verwenden, Schlauchschutz im Oberflächenbereich, alle 3 Jahre ersetzen |
| **Confidence** | documented |

### Fehlerbild MO-09 — Biofouling am Mooring-System

| Attribut | Detail |
|----------|--------|
| **Bezeichnung** | Starker biologischer Bewuchs an Kette, Boje, Pennant |
| **Schweregrad** | NIEDRIG bis MITTEL |
| **Erkennungsmerkmale** | Muscheln, Algen, Seepocken auf allen Unterwasser-Komponenten, reduzierter Bojenauftrieb |
| **Typische Ursache** | Warmes Wasser, lange Standzeiten, keine Antifouling-Behandlung |
| **Region** | Mittelmeer, Karibik, Australien (tropisch/subtropisch) |
| **Sofortmaßnahme** | Bewuchs mechanisch entfernen (Schaber, Bürste) |
| **Langfristige Lösung** | Jährliche Reinigung, Antifouling-Farbe auf Kette und Boje, Boje mit glatter Oberfläche |
| **Confidence** | documented |

### Fehlerbild MO-10 — Verknotete oder überkreuzte Mooringleinen

| Attribut | Detail |
|----------|--------|
| **Bezeichnung** | Muringleinen verschiedener Liegeplätze ineinander verwickelt |
| **Schweregrad** | MITTEL |
| **Erkennungsmerkmale** | Leine lässt sich nicht mehr frei bewegen, starke Reibung, reduzierte Haltekraft |
| **Typische Ursache** | Drehung der Yachten bei Windwechsel, schlecht verlegte Grundkette, zu enge Liegeplätze |
| **Region** | Mittelmeer (Stadthäfen mit Eigenanker) |
| **Sofortmaßnahme** | Taucher zum Entwirren rufen |
| **Langfristige Lösung** | Professionelle Lazy-Line-Installation mit korrekten Abständen |
| **Confidence** | documented |

### Fehlerbild MO-11 — Falsche Pennant-Dimensionierung

| Attribut | Detail |
|----------|--------|
| **Bezeichnung** | Unterdimensionierter oder überdimensionierter Pennant für die Yacht |
| **Schweregrad** | MITTEL (über) bis HOCH (unter) |
| **Erkennungsmerkmale** | Unterdimensioniert: Leine unter Last stark gestreckt, deutliche Verformung. Überdimensioniert: Leine schleift im Wasser, Propeller-Risiko |
| **Typische Ursache** | Besucherboje für alle Boots-Größen, keine Angabe der max. LOA auf Boje |
| **Sofortmaßnahme** | Eigenen Pennant verwenden (immer einen passenden mitführen) |
| **Langfristige Lösung** | Eigene Pennants in 2 Größen an Bord haben |
| **Confidence** | documented |

### Fehlerbild MO-12 — Seaflex/Elastik-System-Ermüdung

| Attribut | Detail |
|----------|--------|
| **Bezeichnung** | Ermüdung oder Rissbildung im elastischen Mooring-Pendant |
| **Schweregrad** | HOCH |
| **Erkennungsmerkmale** | Risse in der Gummi-Ummantelung, reduzierte Rückstellkraft, permanente Verformung |
| **Typische Ursache** | Alter (>15 Jahre), UV-Exposition (bei Oberflächen-Einheiten), Überlastung |
| **Sofortmaßnahme** | Elastik-Element außer Betrieb nehmen, durch Kette ersetzen (temporär) |
| **Langfristige Lösung** | Seaflex-Einheit ersetzen (Hersteller-Austauschservice) |
| **Confidence** | documented |

---

## 8. Troubleshooting

### 8.1 Entscheidungsbaum: Boot treibt vom Mooring ab

```
Boot treibt ab / Mooring hält nicht
│
├── Pennant gerissen?
│   ├── JA → Eigenen Anker sofort setzen
│   │        → Boje suchen und neuen Pennant befestigen
│   │        → ODER: Hafen anlaufen
│   └── NEIN ↓
│
├── Boje gesunken?
│   ├── JA → Riser-Kette suchen (Taucher/Dragnetz)
│   │        → Provisorische Boje befestigen
│   │        → Boje ersetzen
│   └── NEIN ↓
│
├── Grundanker hat nachgegeben (Dragging)?
│   ├── JA → Zusätzlichen Anker setzen
│   │        → Liegeplatz wechseln
│   │        → Grundanker professionell überprüfen lassen
│   └── NEIN ↓
│
├── Schäkel gebrochen?
│   ├── JA → Kette und Pennant verbinden (temporär Leine)
│   │        → Schäkel ersetzen (Taucher)
│   └── NEIN ↓
│
└── Grundkette gerissen?
    └── JA → Sofort eigenen Anker setzen
             → Professionelle Reparatur beauftragen
             → Gesamtes Mooring-System überprüfen lassen
```

### 8.2 Entscheidungsbaum: Muringleine um Propeller

```
Muringleine um Propeller
│
├── Motor sofort AUS!
│
├── Boot unter Kontrolle?
│   ├── NEIN → Heckleinen am Steg sichern
│   │          → Nachbarboote warnen
│   └── JA ↓
│
├── Leine sichtbar/erreichbar?
│   ├── JA → Mit Messer/Leinenbrecher durchtrennen
│   │        (NUR wenn Motor AUS und niemand im Wasser)
│   └── NEIN ↓
│
├── Selbst tauchen möglich? (Wasser warm, Sicht gut, Erfahrung)
│   ├── JA → Taucherbrille + Messer
│   │        → Motor AUS, Zündschlüssel abziehen
│   │        → Leine unter Wasser durchtrennen
│   └── NEIN ↓
│
└── Taucher-Service rufen
    → Kosten: 50–200 EUR (Mittelmeer)
    → Wartezeit: 30 min – 3 h
    → In der Zwischenzeit: Boot am Steg sichern
```

### 8.3 Entscheidungsbaum: Mooring-Boje nicht auffindbar

```
Mooring-Boje nicht auffindbar
│
├── GPS-Position der Boje bekannt?
│   ├── JA → Position anfahren, visuell suchen
│   │        → Bei Niedrigwasser bessere Sicht
│   │        → Polarisierte Sonnenbrille verwenden
│   └── NEIN ↓
│
├── Nachbarn/Hafenmeister fragen
│   ├── Position bekannt → Anfahren
│   └── Unbekannt ↓
│
├── Boje möglicherweise gesunken?
│   ├── JA → Dragnetz über vermuteter Position schleppen
│   │        → Taucher beauftragen
│   │        → Provisorische Boje setzen
│   └── NEIN ↓
│
└── Boje wurde entfernt/versetzt?
    → Hafenmeister kontaktieren
    → Alternative Boje/Liegeplatz suchen
    → Temporär ankern (wenn erlaubt)
```

### 8.4 Entscheidungsbaum: Med-Mooring-Manöver scheitert

```
Stern-to-Anlegemanöver scheitert
│
├── Seitenwind zu stark (>15 kn querab)?
│   ├── JA → Abbrechen und auf Luv-Liegeplatz warten
│   │        → Alternative: Bow-to versuchen
│   │        → Alternative: Steg an der Windseite wählen
│   └── NEIN ↓
│
├── Muringleine nicht gefunden?
│   ├── JA → Marinero um Hilfe bitten
│   │        → Bootshakenreichweite verlängern
│   │        → Notfalls: eigenen Anker setzen
│   └── NEIN ↓
│
├── Rückwärtsfahren instabil?
│   ├── JA → Mehr Übung mit Rückwärtsfahren
│   │        → Bugstrahlruder einsetzen
│   │        → Bei Segel: unter Motor, Ruder mittschiffs
│   └── NEIN ↓
│
├── Abstand zu Nachbarbooten zu eng?
│   ├── JA → Breiteren Liegeplatz suchen
│   │        → Fender verdoppeln
│   │        → Nachbar-Crew um Hilfe bitten
│   └── NEIN ↓
│
└── Heckleinen zu kurz?
    → Längere Leinen vorbereiten (min. 1,5 × Wassertiefe)
    → Leinen vorher auslegen (auf Deck oder im Wasser)
```

### 8.5 Entscheidungsbaum: Mooring-Inspektion Ergebnis

```
Mooring-Inspektion durchführen
│
├── Pennant prüfen
│   ├── UV-Schaden, spröde → ERSETZEN (sofort)
│   ├── Schamfil >20 % → ERSETZEN (zeitnah)
│   ├── Leicht verblasst, flexibel → OK (nächste Saison prüfen)
│   └── Neuwertig → OK
│
├── Boje prüfen
│   ├── Leck, sinkt → ERSETZEN (sofort)
│   ├── Starker Bewuchs → REINIGEN + weiter prüfen
│   ├── Farbe verblasst → MARKIERUNG erneuern
│   └── Intakt → OK
│
├── Schäkel prüfen
│   ├── Korrosion >10 % Materialabtrag → ERSETZEN (sofort)
│   ├── Oberflächenrost → BEOBACHTEN (6 Monate)
│   ├── Bolzen fest → GANGBAR machen + sichern
│   └── Intakt → OK
│
├── Kette prüfen (Taucher erforderlich)
│   ├── Glieddurchmesser <90 % Nenn → ERSETZEN (dringend)
│   ├── Einzelne deformierte Glieder → ABSCHNITT ERSETZEN
│   ├── Gleichmäßig leichter Abtrag → BEOBACHTEN (2 Jahre)
│   └── Intakt → OK
│
└── Grundanker prüfen (Taucher erforderlich)
    ├── Position verändert (Dragging) → NEU SETZEN
    ├── Sichtbare Schäden → ERSETZEN
    ├── Betonblock: Risse → ERSETZEN (mittelfristig)
    └── Intakt → OK (5 Jahre bis nächste Prüfung)
```

---

## 9. FAQ — Häufige Fragen

### F01: Was ist der Unterschied zwischen einer Muringleine und einer Lazy Line?

**Antwort:** Technisch sind es Synonyme. „Muringleine" ist der deutsche Begriff, „Lazy Line" der internationale (englische) Begriff. Beide bezeichnen die vorinstallierte Leine, die von der Grundkette am Meeresboden zum Steg geführt wird und die der Yachtführer zum Bug (bei Stern-to) oder Heck (bei Bow-to) zieht. In der Praxis wird „Lazy Line" auch in deutschen Häfen häufig verwendet.
**Confidence:** documented

### F02: Wie stark muss eine Muringleine/Lazy Line sein?

**Antwort:** Die Bruchlast der Muringleine sollte mindestens das 3-fache der erwarteten Maximallast betragen. Für eine 12-m-Yacht: mindestens 50 kN Bruchlast, was einem Polyester-Doppelgeflecht von 18–20 mm Durchmesser entspricht. Im Zweifelsfall: immer eine Nummer dicker wählen. Muringleinen sind die günstigste Komponente im System und die am leichtesten zu ersetzen.
**Confidence:** documented

### F03: Wie oft muss eine Muringleine ersetzt werden?

**Antwort:** Polypropylen (PP): alle 2–4 Jahre. Polyester (PES): alle 4–7 Jahre. HMPE: alle 8–15 Jahre. Diese Werte gelten bei normaler Nutzung im Mittelmeer. In den Tropen (höhere UV-Belastung) kürzer. Jährliche visuelle Inspektion ist Pflicht. Sofort ersetzen bei sichtbarer Spröde, Farbveränderung oder Faserbruch.
**Confidence:** documented

### F04: Swing-Mooring oder Steg-Liegeplatz — was ist sicherer?

**Antwort:** Ein gut gewartetes Swing-Mooring in geschützter Lage ist vergleichbar sicher wie ein Steg-Liegeplatz. Vorteil Swing-Mooring: Yacht richtet sich automatisch in den Wind aus (minimale Belastung). Nachteil: keine Redundanz (nur eine Befestigung). Steg-Liegeplatz: Redundanz durch mehrere Leinen, aber Yacht kann nicht in den Wind drehen. Bei Starkwind: Swing-Mooring in offener Lage ist gefährlicher als ein Steg-Liegeplatz in geschützter Marina.
**Confidence:** documented

### F05: Was kostet ein permanentes Swing-Mooring?

**Antwort:** Komponenten: 800–5.000 EUR (je nach Yacht-Größe und Grundanker-Typ). Installation: 500–3.000 EUR (Taucher, Barge für Betonblock). Jährliche Wartung: 100–500 EUR. Lizenzgebühren (wo erforderlich): 200–2.000 EUR/Jahr. Gesamtkosten im 1. Jahr: 1.500–10.000 EUR. Danach: 300–2.500 EUR/Jahr.
**Confidence:** estimated

### F06: Kann ich mein Swing-Mooring selbst installieren?

**Antwort:** Grundsätzlich ja, aber: (1) In vielen Ländern ist eine Genehmigung/Lizenz erforderlich (UK: Crown Estate; Australien: State Licence; Deutschland: Wasserbehörde). (2) Für das Setzen eines Betonblocks wird eine Barge benötigt. (3) Helix-Anker erfordern hydraulisches Installationsgerät. (4) Der Grundanker muss für die erwartete Last berechnet werden. Empfehlung: Berechnung selbst, Installation durch Fachfirma.
**Confidence:** documented

### F07: Was mache ich, wenn die Muringleine am Steg nicht vorhanden ist?

**Antwort:** (1) Marinero/Hafenmeister fragen — möglicherweise wird die Leine von einem Beiboot gebracht. (2) Nachbarliegeplatz versuchen. (3) Eigenen Buganker als Alternative setzen (Achtung: Ankersalat-Risiko). (4) Boot provisorisch nur mit Heckleinen sichern und Muringleine zeitnah von der Marina reparieren lassen.
**Confidence:** documented

### F08: Wie nehme ich eine Mooring-Boje sicher auf?

**Antwort:** (1) Langsam anfahren (1–2 kn). (2) Boje in Luv halten (Wind kommt von achtern → Boje vor dem Bug). (3) Bootshaken bereithalten. (4) Motor in Leerlauf, wenn Boje neben dem Bug ist. (5) Bootshaken durch den Ring/Öse der Boje führen. (6) Pennant/eigene Leine durchführen und auf Bugklampe belegen. (7) Motor aus. (8) Zweite Sicherungsleine (Backup) befestigen.
**Confidence:** documented

### F09: Darf ich an jeder Boje festmachen?

**Antwort:** Nein. (1) Private Moorings: nur mit Erlaubnis des Eigentümers. (2) Nationalpark-Bojen: meist gegen Gebühr, Registrierung erforderlich. (3) Navigationsbojen (rot/grün): NIEMALS festmachen — ist verboten und gefährlich. (4) Gelbe/weiße Besucherbojen: ja, meist gebührenpflichtig. (5) Im Zweifelsfall: Hafenmeister oder VHF Kanal 16/9 kontaktieren.
**Confidence:** documented

### F10: Was ist ein Pick-up Stick und brauche ich einen?

**Antwort:** Ein Pick-up Stick ist eine vertikale Stange über der Mooring-Boje mit einer Öse, an der ein Pennant befestigt ist. Er erleichtert das Aufnehmen der Boje erheblich, besonders bei Yachten mit hohem Freibord. Empfehlung: Wenn Ihre Yacht an einem permanenten Mooring liegt, ist ein Pick-up Stick sehr empfehlenswert (Kosten: 30–60 EUR, Zeitersparnis und Sicherheit beim Aufnehmen enorm).
**Confidence:** documented

### F11: Wie pflege ich mein Mooring-System?

**Antwort:** (1) Pennant: alle 6 Monate visuell prüfen, alle 3–5 Jahre ersetzen. (2) Boje: jährlich reinigen (Bewuchs), auf Lecks prüfen, Farbe erneuern. (3) Schäkel/Wirbel: jährlich prüfen, gangbar halten, Edelstahl bevorzugen. (4) Kette: alle 2–3 Jahre durch Taucher prüfen lassen, nach 10–15 Jahren ersetzen. (5) Grundanker: alle 5 Jahre prüfen (Position, Haltekraft).
**Confidence:** documented

### F12: Welches Material ist besser für Muringleinen — PP oder PES?

**Antwort:** Polyester (PES) ist in fast allen Belangen überlegen: höhere Bruchlast, bessere UV-Beständigkeit, geringere Dehnung, längere Lebensdauer. Einziger Nachteil: PES sinkt (Aufnehmen schwieriger). Polypropylen (PP) schwimmt und ist günstiger, aber hat geringere Festigkeit und degradiert schneller. Empfehlung: PES für Langzeit-Muringleinen, PP nur als Billig-Lösung für 1–2 Saisons.
**Confidence:** documented

### F13: Wie funktioniert ein Seaflex-System?

**Antwort:** Seaflex ist ein elastisches Unterwasser-Mooring-System aus Gummiseilen in Schutzummantelung. Es wird zwischen dem Grundanker und dem Schwimmsteg/Boje installiert und dehnt sich bei Belastung (Tidenhub, Wellengang, Wind) um bis zu 100 %. Dadurch entfallen starre Ketten, die den Meeresboden durch Schleifen beschädigen. Lebensdauer: 25+ Jahre. Kosten: 500–12.000 EUR je nach Größe.
**Confidence:** documented

### F14: Wie berechne ich die nötige Haltekraft meines Grundankers?

**Antwort:** Vereinfachte Formel: Haltekraft = 3,0 × (Windlast + Strömungslast) × dynamischer Faktor. Für eine 12-m-Segelyacht bei Design-Wind Bft 9: Haltekraft ≈ 3,0 × (5,0 + 1,5) × 1,5 ≈ 29 kN. Ein 2.000 kg Betonblock leistet ca. 10–16 kN Haltekraft → knapp. Besser: 3.000 kg Block oder Helix-Anker mit 40+ kN.
**Confidence:** calculated

### F15: Was passiert, wenn ich an einem unterdimensionierten Mooring liege?

**Antwort:** Bei normalem Wetter: nichts. Bei Starkwind (>Bft 7): Grundanker kann ausbrechen (Dragging), Kette kann reißen, Pennant kann reißen. Folgen: Boot treibt ab, kollidiert mit anderen Booten oder läuft auf Grund. Versicherung kann Leistung kürzen, wenn nachweisbar unterdimensioniertes Mooring verwendet wurde.
**Confidence:** documented

### F16: Kann ich mein Boot das ganze Jahr auf einem Swing-Mooring lassen?

**Antwort:** In frostfreien Regionen (Mittelmeer, Karibik): ja, wenn das Mooring für Winterstürme ausgelegt ist. In Gebieten mit Frost/Eis: nein — Eisgang kann Kette, Boje und Boot zerstören. In Tidengewässern: ja, wenn Tidenhub-Ausgleich (Gleitringe, lange Leinen) vorhanden. Empfehlung: In Nord-/Mitteleuropa im Winter auswassern (Oktober–April).
**Confidence:** documented

### F17: Was ist ein Fore-and-Aft-Mooring und wann brauche ich es?

**Antwort:** Ein Fore-and-Aft-Mooring befestigt die Yacht an Bug und Heck an je einem separaten Grundanker. Die Yacht schwojt nicht. Nötig in: engen Flüssen (keine 360°-Drehung möglich), Gezeitenrevieren mit wechselnder Strömung, Bereichen mit vielen Booten auf engem Raum. Typische Regionen: Solent (UK), niederländische Binnengewässer, australische Flüsse.
**Confidence:** documented

### F18: Wie verhalte ich mich beim Med-Mooring bei starkem Seitenwind?

**Antwort:** (1) Wenn möglich: warten, bis der Wind nachlässt. (2) Liegeplatz an der Luvseite des Hafens wählen (Wind drückt Boot an den Steg). (3) Wenn Luvseite nicht verfügbar: auf der Lee-Seite anlegen, aber Fender verdoppeln und Crew an beiden Seiten positionieren. (4) Bei >20 kn querab: Manöver abbrechen, ankern und warten. (5) Bugstrahlruder ist bei Seitenwind Gold wert.
**Confidence:** documented

### F19: Welche Ausrüstung brauche ich für Med-Mooring?

**Antwort:** Zusätzlich zur Standard-Festmacher-Ausrüstung: (1) 2 Heckleinen, je 1,5–2 × Wassertiefe lang (20–30 m). (2) Langer Bootshaken (3–4 m) zum Aufnehmen der Lazy Line. (3) Passerelle/Gangway (2–3 m). (4) 6–8 Fender (beide Seiten). (5) Optional: Eigener Pennant als Backup für defekte Lazy Lines. (6) Fenderbretter für raue Stegkanten.
**Confidence:** documented

### F20: Was ist der Unterschied zwischen einem Pilzanker und einem Helix-Anker?

**Antwort:** Pilzanker: pilzförmiger Gusskörper, der sich durch sein Gewicht in weichen Boden einzieht. Haltekraft steigt über Monate/Jahre, da er immer tiefer einsinkt. Günstig (200–1.000 EUR), aber nur in weichem Boden (Schlick, feiner Sand). Helix-Anker: schraubenförmige Flügel werden mechanisch in den Boden geschraubt. Sofort volle Haltekraft, höchste Haltekraft/Gewicht-Ratio, umweltschonend. Teuer (2.000–14.000 EUR inkl. Installation), für fast alle Böden geeignet (außer Fels).
**Confidence:** documented

### F21: Wie sicher sind Besucherbojen in Naturhäfen?

**Antwort:** Sehr variabel. (1) Professionell gewartete Bojen (Nationalparks, Marinas): in der Regel sicher für die angegebene Bootsgröße. (2) Kommunale Bojen: Wartungszustand prüfen! (3) Private/alte Bojen: IMMER skeptisch sein. Eigenen Pennant verwenden, Zustand von Boje und Kette soweit möglich prüfen, eigenen Anker als Backup bereithalten. Im Zweifelsfall lieber selbst ankern (wenn erlaubt).
**Confidence:** documented

### F22: Was ist ein Mooring Bridle und wozu dient es?

**Antwort:** Ein Mooring Bridle ist eine V-förmige Leinenführung vom Pennant zu zwei Bugklampen (Backbord und Steuerbord). Es verteilt die Last auf zwei Klampen statt eine und reduziert die Gierbewegung (Hin-und-Her-Schwojen). Empfehlung: Bei allen Swing-Moorings >10 m LOA ein Bridle verwenden. Leinendurchmesser: gleich wie Pennant. Winkel: 30–45° (nicht breiter, sonst erhöhte Querlast).
**Confidence:** documented

### F23: Wie vermeide ich „Ankersalat" beim Med-Mooring mit eigenem Anker?

**Antwort:** (1) Anker genau in Verlängerung des Liegeplatzes setzen, nicht schräg. (2) Genügend Kette ausbringen (3–4 × Wassertiefe). (3) GPS-Position des Ankers notieren. (4) Beim Ablegen: Kette langsam einholen, Richtung beobachten. (5) Wenn verwickelt: NICHT mit Gewalt ziehen. Taucher rufen. (6) Beste Prävention: Marina mit Lazy Lines wählen.
**Confidence:** documented

### F24: Was muss ich bei einem Trockenfallmooring beachten?

**Antwort:** (1) Yacht muss trockenfallgeeignet sein (Langkiel, Kimmkiel oder Stützbeine). (2) Untergrund muss eben und fest sein (kein Schlick, keine Steine). (3) Leinen müssen lang genug für vollen Tidenhub sein. (4) Yacht richtet sich beim Trockenfallen nach dem letzten Wasserstand aus — Leinen entsprechend nachlassen. (5) Vor dem ersten Trockenfallen: Erfahrung sammeln, lokale Experten fragen.
**Confidence:** documented

### F25: Wie erkenne ich, ob mein Mooring eine Inspektion braucht?

**Antwort:** Warnsignale: (1) Boje liegt tiefer als sonst (Bewuchs oder Leck). (2) Boot liegt anders als gewohnt (Anker versetzt). (3) Pennant ist verfärbt oder spröde. (4) Kette zeigt Rost beim Aufholen der Boje. (5) Es wurde seit >3 Jahren nicht inspiziert. (6) Es gab einen Sturm mit >8 Bft. (7) Nachbar-Mooring ist kürzlich ausgefallen. Bei einem dieser Zeichen: professionelle Unterwasser-Inspektion beauftragen.
**Confidence:** documented

### F26: Was ist ein Reitgewicht (Kellet) und wann verwende ich es?

**Antwort:** Ein Reitgewicht (englisch: Kellet oder Sentinel) ist ein Gewicht (5–15 kg), das an der Ankerkette oder am Pennant heruntergelassen wird, um den Catenary-Effekt zu verstärken. Es senkt den Zug-Winkel am Grundanker und dämpft Ruckbelastungen. Einsatz: Bei Swing-Moorings mit zu straffer Kette, bei Schwell, bei erwartetem Starkwind. Kosten: 30–80 EUR (Blei- oder Gusseisengewicht mit Karabiner).
**Confidence:** documented

### F27: Wie lang muss die Grundkette bei einem Swing-Mooring sein?

**Antwort:** Faustregel: Kettenlänge = 2,0–3,0 × Wassertiefe (bei Springtide-Hochwasser). In Tidengewässern die maximale Wassertiefe verwenden! Beispiel: Wassertiefe 5 m bei Hochwasser → Kette 10–15 m. Je länger die Kette, desto besser der Catenary-Effekt (Stoßdämpfung), aber auch desto größer der Schwojkreis.
**Confidence:** documented

### F28: Kann ich eine Muringleine auch als Vor- oder Achterleine verwenden?

**Antwort:** Technisch ja, aber nicht empfohlen. Muringleinen sind für dauerhafte Unterwasser-Belastung ausgelegt (UV, Bewuchs, Schamfil an Grundkette). Vor-/Achterleinen sind für Deck-Belastung ausgelegt (UV, Schamfil an Klampe/Klüse). Die Anforderungen an Material und Konstruktion unterscheiden sich. Verwenden Sie jeweils spezifische Leinen.
**Confidence:** estimated

### F29: Was passiert bei einem Mooring-Versagen mit der Versicherung?

**Antwort:** (1) Eigenes Mooring: Die Yacht-Kaskoversicherung deckt Schäden an der eigenen Yacht, wenn das Mooring den üblichen Standards entspricht. Bei nachweislich unterdimensioniertem oder mangelhaft gewartetem Mooring kann die Versicherung die Leistung kürzen. (2) Marina-Mooring: Die Marina haftet für Schäden durch defekte Marina-Infrastruktur (Lazy Lines, Grundketten). Nachweis oft schwierig. (3) Fremd-Mooring (z. B. Boje): Nutzung auf eigenes Risiko, wenn nicht als „geprüft" gekennzeichnet. Empfehlung: Mooring-Zustand dokumentieren (Fotos), Wartungsnachweise aufbewahren.
**Confidence:** documented

### F30: Wie funktioniert ein Mooring Bridle und wie mache ich ihn?

**Antwort:** Ein Bridle besteht aus zwei Leinen gleicher Länge, die vom Pennant (oder direkt von der Boje) jeweils zu einer Bugklampe (Backbord und Steuerbord) geführt werden. Herstellung: (1) Zwei Leinen gleichen Durchmessers wie der Pennant, jeweils 3–5 m lang. (2) An einem Ende jeder Leine eine Augspeiß. (3) Beide Augen mit einem Schäkel am Pennant oder an der Boje befestigen. (4) Die freien Enden auf die jeweilige Bugklampe belegen. Winkel zwischen den beiden Bridle-Leinen: 30–45° (nicht breiter).
**Confidence:** documented

### F31: Welche Apps/Tools helfen beim Mooring?

**Antwort:** (1) **Navionics/Boating:** Zeigt Mooring-Felder und Besucherbojen. (2) **ActiveCaptain (Garmin):** Community-Bewertungen von Moorings und Ankerplätzen. (3) **Noforeignland:** Detaillierte Ankerplatz-Beschreibungen mit Mooring-Hinweisen. (4) **Marina-Apps (Dockwa, Marinanet):** Reservierung von Mooring-Plätzen. (5) **AYDI (zukünftig):** Mooring-Dimensionierung und Zustandsbewertung.
**Confidence:** documented

### F32: Was ist ein „Drying Mooring" und für welche Boote eignet es sich?

**Antwort:** Ein Drying Mooring ist ein Liegeplatz in einem Trockenfallhafen, bei dem die Yacht bei Niedrigwasser auf dem Grund liegt. Geeignet für: Langkieler (stehen von allein), Boote mit Kimmkielen (stabil auf ebenem Grund), Boote mit aufsteckbaren Stützbeinen. NICHT geeignet für: Flossenkieler, Boote mit tiefliegendem Ruderblatt, empfindliche Unterwasser-Anbauten (Echolot, Logge). Region: Hauptsächlich UK (Cornwall, Wales), Bretagne (Frankreich).
**Confidence:** documented

### F33: Wie verhalte ich mich, wenn eine Nachbaryacht am Mooring Probleme hat?

**Antwort:** (1) Beobachten: Treibt die Nachbaryacht ab? Ist jemand an Bord? (2) Warnen: VHF Kanal 16, Hafenmeister rufen. (3) Helfen (wenn sicher): Fender zwischen die Boote, Leinen anbieten. (4) NICHT: Auf die fremde Yacht springen (Verletzungsgefahr, Haftungsfragen). (5) Dokumentieren: Fotos/Video für Versicherung (eigene und fremde).
**Confidence:** documented

### F34: Wie erkenne ich die maximale Bootsgröße einer Mooring-Boje?

**Antwort:** (1) Beschriftung auf der Boje (oft: max. LOA oder Verdrängung angegeben). (2) Farbkodierung (regional unterschiedlich, z. B. Gelb = Besucher, Rot = privat). (3) Bojen-Durchmesser als Indikator: <400 mm = bis 10 m; 400–600 mm = bis 15 m; >600 mm = bis 20 m+. (4) Im Zweifelsfall: Hafenmeister/VHF fragen. (5) Eigene Einschätzung: Wenn die Boje beim Festmachen deutlich abtaucht, ist sie für Ihre Yacht zu klein.
**Confidence:** documented

### F35: Was muss ich bei einem Mooring-Wechsel (von Boje zu Marina) beachten?

**Antwort:** (1) Boje freigeben: Pennant lösen, Boot frei fahren lassen, dann erst Pennant von Bord geben. (2) Pennant/Boje nicht mit dem Boot schleppen. (3) Motor in Leerlauf, wenn Leine im Wasser ist (Propeller-Risiko). (4) Bei Marina-Anlauf: Fender und Leinen VOR dem Ablegen von der Boje vorbereiten. (5) Bei Med-Mooring-Anlauf: gesamte Vorbereitung (Heckleinen, Fender, Crew-Einweisung) erledigen, bevor die Boje losgelassen wird.
**Confidence:** documented

---

## 10. Glossar

| Begriff | Englisch | Erklärung |
|---------|----------|-----------|
| **Ankersalat** | Anchor tangle | Situation, in der sich die Anker und/oder Ankerketten benachbarter Yachten ineinander verwickeln |
| **Aufnehmeleine** | Pennant, Pendant | Leine von der Mooring-Boje zur Bugklampe der Yacht |
| **Betonblock** | Dead weight anchor | Massiver Betonblock als Grundanker für permanente Moorings |
| **Boje** | Buoy | Schwimmkörper, der die Position des Moorings an der Oberfläche markiert |
| **Bow-to** | Bow-to | Med-Mooring-Technik, bei der der Bug zum Steg zeigt |
| **Bridle** | Mooring bridle | V-förmige Leinenführung vom Pennant zu zwei Bugklampen |
| **Bugstrahlruder** | Bow thruster | Querstrahler im Bug für verbesserte Manövrierfähigkeit |
| **Catenary** | Catenary | Kettenlinienförmiger Durchhang einer Kette durch Eigengewicht |
| **Crown Estate** | Crown Estate | Britische Körperschaft, die den Meeresboden verwaltet und Mooring-Lizenzen vergibt |
| **Dalbe** | Dolphin, pile | Einzelner oder paarweiser Pfahl im Wasser als Festmacherpunkt |
| **Dragging** | Dragging | Nachgeben/Verschieben des Grundankers unter Last |
| **Eco-Mooring** | Eco mooring | Umweltschonendes Mooring-System ohne Kettenschleppe am Meeresboden |
| **Fingerponton** | Finger pontoon | Seitlicher Schwimmsteg, der als Zugang zur Yacht dient |
| **Fore-and-Aft** | Fore-and-aft mooring | Mooring mit je einem Grundanker an Bug und Heck |
| **Gjestehavn** | Guest harbour | Norwegischer Gästehafen |
| **Gleitring** | Sliding ring | Ring an einem Pfahl, der vertikal gleiten kann (Tidenhub-Ausgleich) |
| **Grundanker** | Ground anchor | Permanenter Anker am Meeresboden (Betonblock, Pilzanker, Helix-Anker) |
| **Grundgeschirr** | Ground tackle | Gesamtheit aller Unterwasser-Komponenten eines Mooring-Systems |
| **Grundkette** | Ground chain, Riser chain | Kette vom Grundanker zur Boje oder zum Schwimmsteg |
| **Helix-Anker** | Helical screw anchor | Schraubanker, der in den Meeresboden geschraubt wird |
| **Hurrikan-Mooring** | Hurricane mooring | Überdimensioniertes Mooring für Hurrikanbelastung |
| **Kettenlinie** | Catenary | Mathematische Kurve einer frei hängenden Kette |
| **Lazy Line** | Lazy line | Vorinstallierte Muringleine in einer Marina (Med-Mooring) |
| **Mangroven-Mooring** | Mangrove mooring | Festmachen an Mangrovenbäumen (Hurrikansicherung, Karibik) |
| **Marinero** | Marina staff | Hafenpersonal, das beim Anlegen hilft (Mittelmeer) |
| **Med-Mooring** | Mediterranean mooring | Anlegen mit Heck (oder Bug) am Steg und Muringleine in Gegenrichtung |
| **Muringleine** | Mooring line, lazy line | Vorinstallierte Leine in einer Marina, die die Yacht zum Grundanker verbindet |
| **Naturhamn** | Natural harbour | Schwedischer Naturhafen mit freien Pfählen oder Felsringen |
| **Passerelle** | Gangway, passerelle | Gangway vom Heck der Yacht zum Steg beim Med-Mooring |
| **Pennant** | Pennant, pendant | Aufnehmeleine von der Boje zur Yacht |
| **Pick-up Stick** | Pick-up stick | Vertikale Stange über der Boje zum erleichterten Aufnehmen |
| **Pilzanker** | Mushroom anchor | Anker mit pilzförmigem Kopf, der sich in weichen Boden einzieht |
| **Riser** | Riser | Vertikale Verbindung vom Meeresboden zur Oberfläche (Kette oder Seil) |
| **Schärenring** | Rock ring | In den Fels gebohrter Edelstahlring als Festmacherpunkt (Schweden) |
| **Schwojkreis** | Swing circle | Kreis, den eine am Swing-Mooring liegende Yacht beschreiben kann |
| **Snatch Load** | Snatch load | Stoßartige Ruckbelastung auf Leine oder Kette |
| **Snubber** | Snubber | Ruckdämpfer (elastische Leine oder Gummielement) zum Abfedern von Stoßlasten |
| **Stern-to** | Stern-to | Med-Mooring-Technik, bei der das Heck zum Steg zeigt |
| **Swing-Mooring** | Swing mooring | Einpunkt-Mooring, bei dem die Yacht frei um 360° schwojen kann |
| **Tidenhub** | Tidal range | Unterschied zwischen Hoch- und Niedrigwasser |
| **Trockenfallhafen** | Drying harbour | Hafen, in dem Yachten bei Niedrigwasser auf dem Grund liegen |
| **Trotting Line** | Trot mooring | Gemeinsame Grundkette für mehrere Swing-Moorings |
| **Verholen** | Warping | Yacht von einem Liegeplatz zu einem anderen bewegen, meist an Leinen |
| **Windangriffsfläche** | Windage area | Seitliche Projektionsfläche der Yacht über der Wasserlinie |
| **Wirbel** | Swivel | Drehgelenk in der Mooring-Kette, das ein Verdrillen verhindert |
| **Scope** | Scope | Verhältnis von Ketten-/Leinenlänge zu Wassertiefe |
| **Kettenlinie** | Catenary curve | Mathematische Kurve einer unter Eigengewicht hängenden Kette |
| **Reitgewicht** | Kellet, Sentinel | Gewicht, das an der Kette heruntergelassen wird, um den Catenary-Effekt zu verstärken |
| **Schamfil** | Chafe | Abrieb/Verschleiß an Leinen durch Reibung an Klampen, Klüsen oder Ketten |
| **Chafe Guard** | Chafe guard | Schutzschlauch oder -umwicklung an einer Leine zur Verhinderung von Schamfil |
| **Festmacherknecht** | Line holder, horn cleat | Kleine Klampe oder Vorrichtung zum schnellen Belegen einer Leine |
| **Pfahlstek** | Clove hitch | Knoten zum Befestigen einer Leine an einem Pfahl |
| **Rundtörn** | Round turn | Umwicklung einer Leine um einen Poller oder Pfahl (360°) |
| **Mooringfeld** | Mooring field | Abgegrenztes Gebiet mit mehreren permanenten Moorings |
| **Hafenmeister** | Harbour master | Verantwortlicher für die Verwaltung und Sicherheit eines Hafens |

---

## 11. Schnell-Referenz

### 11.1 Mooring-Typ-Auswahl nach Region

| Region | Empfohlener Mooring-Typ | Besonderheit |
|--------|------------------------|-------------|
| Mittelmeer (Marina) | Stern-to mit Lazy Line | Standard, Fender + Passerelle nötig |
| Mittelmeer (Stadthafen) | Stern-to mit eigenem Anker | Ankersalat-Risiko, Erfahrung nötig |
| Skandinavien | Pfahl-Mooring | Leinen mit Ruckdämpfer, Eis im Winter |
| UK (Solent) | Swing-Mooring | Crown Estate Lizenz, Tidenhub beachten |
| UK (West Country) | Swing oder Drying | Trockenfalleignung prüfen |
| Karibik | Swing-Boje oder Ankern | Hurrikansicherheit planen |
| Australien | Swing (Eco-Mooring) | Lizenz + jährliche Inspektion Pflicht |
| Niederlande | 4-Pfahl-Box | Komfortabelste Lösung |
| Norddeutschland (Ostsee) | Pfahl + Steg | Geringer Tidenhub |
| Norddeutschland (Nordsee) | Pfahl mit Gleitring | Hoher Tidenhub |

### 11.2 Schnell-Dimensionierung Swing-Mooring

| LOA (m) | Grundanker (Beton, kg) | Kette (mm) | Pennant (mm) | Boje (Ø mm) |
|---------|----------------------|------------|-------------|-------------|
| 6–8 | 500–1.000 | 10 | 14–16 | 380 |
| 8–10 | 1.000–2.000 | 12 | 16–18 | 460 |
| 10–13 | 2.000–3.000 | 14 | 18–22 | 540 |
| 13–16 | 3.000–5.000 | 16 | 22–24 | 630 |
| 16–20 | 5.000–8.000 | 20 | 24–28 | 760 |
| 20–25 | 8.000+ | 22+ | 28–32 | 900+ |

### 11.3 Checkliste Med-Mooring (Stern-to)

- [ ] Fender an beiden Seiten (min. 3 pro Seite)
- [ ] Heckleinen vorbereitet (2 × min. 20 m)
- [ ] Bootshaken bereit (3–4 m Länge)
- [ ] Passerelle bereit
- [ ] Crew eingewiesen (Bug: Muringleine, Heck: Heckleinen)
- [ ] Liegeplatz identifiziert (Nummer, Lazy Line Position)
- [ ] Windrichtung und -stärke eingeschätzt
- [ ] Langsam rückwärts eingefahren (<2 kn)
- [ ] Heckleinen an Land/Poller belegt
- [ ] Muringleine aufgenommen und am Bug belegt
- [ ] Boot positioniert (30–50 cm Abstand Heck–Steg)
- [ ] Passerelle ausgelegt
- [ ] Alle Leinen auf Schamfil geprüft

### 11.4 Mooring-Inspektion — Kurzanleitung

| Komponente | Was prüfen? | Wie oft? | Aktion bei Mangel |
|------------|------------|---------|-------------------|
| Pennant | UV-Schaden, Schamfil, Dehnfähigkeit | 6 Monate | Sofort ersetzen |
| Boje | Auftrieb, Lecks, Bewuchs | 1 Jahr | Reinigen oder ersetzen |
| Schäkel | Korrosion, Bolzen-Zustand | 1 Jahr | Ersetzen wenn >10 % Abtrag |
| Kette | Glieddurchmesser, Rost, Verformung | 2–3 Jahre | Ersetzen wenn <90 % Nenn-Ø |
| Grundanker | Position, Haltekraft | 5 Jahre | Neu setzen oder upgraden |

---

## ANHANG A — Fallstudien

### A1 — Mooring-Versagen bei Bora-Sturm (Kroatien, Marina Kastela)

**Situation:** Oktober 2022, Bora-Sturm mit Böen bis 85 kn über Marina Kastela (nahe Split). 120 Yachten auf Stern-to-Liegeplätzen.

**Hergang:**
- 18:00 Uhr: Bora setzt ein, zunächst 35–45 kn
- 22:00 Uhr: Böen erreichen 70 kn, erste Muringleinen reißen
- 23:30 Uhr: 8 Yachten treiben frei, kollidieren untereinander
- 02:00 Uhr: Spitzenböe 85 kn, weitere 5 Yachten lösen sich
- Morgens: 13 Yachten beschädigt, davon 3 schwer (Rumpfdurchbruch)

**Analyse:**
| Faktor | Befund | Confidence |
|--------|--------|------------|
| Muringleinen-Zustand | 4 der 8 gerissenen Leinen waren PP, >5 Jahre alt | documented |
| Grundketten-Zustand | 2 Schäkel-Brüche (verzinkter Stahl, korrodiert) | documented |
| Windlast-Berechnung | 85 kn Bora auf 20 m² Windangriffsfläche = 22 kN | calculated |
| Muringleinen-Bruchlast (PP 16 mm, 5 Jahre alt) | ~15 kN (von original 35 kN) | estimated |
| Fazit | UV-degradierte PP-Leinen + korrodierte Schäkel = System versagte bei 60 % der Designlast | documented |

**AYDI-Bewertung:**
- Mooring-System: 25/100 (kritisch unterdimensioniert für Bora-Region)
- Empfehlung: PES 22 mm (Bruchlast 70 kN), Edelstahl-Schäkel, jährliche Inspektion

### A2 — Erfolgreicher Hurrikan-Schutz (BVI, Tortola, Hurrikan Irma 2017)

**Situation:** Hurrikan Irma (Kategorie 5, Böen >185 kn) trifft die British Virgin Islands am 6. September 2017.

**Hergang:**
- Von ca. 2.500 Yachten in den BVI überstanden nur ~100 Boote den Hurrikan ohne schwere Schäden
- Die überlebenden Boote waren entweder (a) ausgewassert und verzurrt, (b) in Mangroven festgemacht, oder (c) auf überdimensionierten Hurrikan-Moorings

**Erfolgsfall: SY "Endurance" (15 m Segelyacht):**
- Vorbereitung: 3 Tage vor Irma in Mangrovenkanal (Paraquita Bay) verholt
- Mooring: 8 Leinen (24 mm Nylon) an 8 verschiedene Mangrovenbäume
- Fender: 12 Fender und Fenderbrett an beiden Seiten
- Masten: Baum demontiert, alles Lose entfernt
- Ergebnis: Yacht überstand Irma mit kosmetischen Schäden (Fender-Abrieb, gebrochener Windgenerator)

| Maßnahme | Kosten | Wirksamkeit | Confidence |
|----------|--------|-------------|------------|
| 8 × Nylon-Leinen 24 mm × 30 m | 400 EUR | Essentiell | documented |
| 12 × Fender + Fenderbretter | 200 EUR | Wichtig | documented |
| Mangroven-Position | 0 EUR | Entscheidend (Windschatten) | documented |
| 3 Tage Vorbereitung | Unbezahlbar | Entscheidend | documented |

### A3 — Eco-Mooring-Umstellung (Sydney Harbour, Australien)

**Situation:** 2015 ordnete NSW Roads and Maritime Services die Umstellung aller Moorings in Seegras-Gebieten (Posidonia australis) auf Eco-Moorings an.

**Hergang:**
- 2015–2020: 2.400 traditionelle Moorings (Betonblock + Kette) auf Eco-Moorings (Helix-Anker + Seaflex) umgestellt
- Kosten: 4.000–8.000 AUD pro Mooring (Umstellung)
- Ergebnis: Seegras-Bedeckung in den umgestellten Gebieten stieg um 15–25 % innerhalb von 5 Jahren

| Aspekt | Vorher (traditionell) | Nachher (Eco-Mooring) | Confidence |
|--------|----------------------|----------------------|------------|
| Seegras-Deckung | 35 % | 52 % (+17 %) | documented |
| Mooring-Ausfallrate | 2,5 % pro Jahr | 0,8 % pro Jahr | documented |
| Wartungskosten/Jahr | 300 AUD | 150 AUD | documented |
| Boots-Bewegung am Mooring | Stark (ruckartig) | Gering (gedämpft) | documented |

### A4 — Med-Mooring-Schulung für Einsteiger (Yacht-Charterbasis, Pula, Kroatien)

**Situation:** Charterfirma stellte fest, dass 35 % aller Schäden bei Rückgabe durch fehlerhafte Med-Mooring-Manöver verursacht wurden.

**Maßnahme:** Einführung einer 30-minütigen Med-Mooring-Schulung bei Übernahme (Video + Praxis am Steg).

**Ergebnis nach 2 Saisons:**
| Kennzahl | Vor Schulung | Nach Schulung | Veränderung | Confidence |
|----------|-------------|---------------|-------------|------------|
| Schäden durch Med-Mooring | 35 % | 12 % | −65 % | documented |
| Propeller-in-Lazy-Line | 12 % | 3 % | −75 % | documented |
| Kollision mit Nachbarboot | 8 % | 2 % | −75 % | documented |
| Kundenzufriedenheit | 3,8/5 | 4,5/5 | +18 % | documented |

### A5 — Swing-Mooring-Versagen bei Springtide (Solent, UK)

**Situation:** März 2023, Springtide kombiniert mit SW-Sturm (Bft 9–10) im Solent (Hampshire, UK).

**Hergang:**
- Tidenhub 4,8 m (Springtide) → Mooring-Ketten am Limit der Scope-Länge
- SW-Wind 45–55 kn → Yachten schwojten nicht frei (Strom aus E, Wind aus SW → Yacht lag quer)
- 6 Moorings versagten: Ketten rissen (2), Grundanker draggten (3), Pennant riss (1)
- 3 Yachten liefen auf Ufer auf (Mooring-Feld Cowes, Isle of Wight)

| Ursache | Anteil | Detail | Confidence |
|---------|--------|--------|------------|
| Unterdimensionierte Kette | 33 % | 10 mm Kette für 12 m Yacht (min. 14 mm empfohlen) | documented |
| Grundanker zu leicht | 50 % | 500 kg Betonblöcke für 10–12 m Yachten | documented |
| UV-geschädigter Pennant | 17 % | Nylon-Pennant, >5 Jahre, nie ersetzt | documented |

### A6 — Erfolgreiche Pfahl-Mooring-Lösung (Sandhamn, Schweden)

**Situation:** Gästehafen Sandhamn (Stockholmer Schären), 80 Gastliegeplätze an Pfählen.

**Technische Lösung:**
- Eichen-Pfähle, Ø 250 mm, 6 m lang, 3 m in den Boden gerammt
- Edelstahl-Ringe (316L) am Pfahlkopf
- Abstand zwischen Pfählen: LOA + 1,5 m
- Leinen: Eigene Leinen der Gastsegler (14–18 mm empfohlen)

**Ergebnis über 10 Jahre:**
| Kennzahl | Wert | Confidence |
|----------|------|------------|
| Pfahl-Lebensdauer | 12–18 Jahre (Eiche) | documented |
| Ausfälle durch Pfahl-Bruch | 0 in 10 Jahren | documented |
| Liegeplatz-Effizienz | 85 % (vs. 40 % bei Swing-Mooring) | calculated |
| Eignerzufriedenheit | Sehr hoch (einfaches Anlegen) | estimated |

### A7 — Lazy-Line-Upgrade in griechischer Marina (Lefkas Marina)

**Situation:** Lefkas Marina (Ionische Inseln) hatte chronische Probleme mit gerissenen Lazy Lines und Propeller-Verwicklungen.

**Maßnahme (2021):**
- Alle 200 Lazy Lines von PP 16 mm auf PES Double Braid 20 mm aufgerüstet
- Schäkel von verzinktem Stahl auf Edelstahl 316L umgestellt
- Grundkette: alle 20 m-Abschnitte mit Querschnittsmessung geprüft, 30 % ersetzt

| Aspekt | Vorher (PP) | Nachher (PES) | Confidence |
|--------|------------|---------------|------------|
| Lazy-Line-Brüche/Saison | 15–20 | 1–3 | documented |
| Propeller-Verwicklungen/Saison | 25–30 | 5–8 | documented |
| Kosten pro Lazy Line | 25 EUR | 85 EUR | documented |
| Einsparung Taucher-Einsätze/Saison | — | 4.000 EUR | calculated |

### A8 — Smartmooring-Pilotprojekt (Marina Port Adriano, Mallorca)

**Situation:** 2024 installierte Marina Port Adriano ein Smartmooring-System mit Lastsensoren an 50 Superyacht-Liegeplätzen.

**System-Komponenten:**
- Drahtlose Lastsensoren an jeder Muringleine (Zugkraft in Echtzeit)
- Boje mit GPS-Tracker (Position + Drift-Erkennung)
- Wetterstation (Wind, Wellen, Strömung)
- Software-Dashboard für Hafenmeister

**Ergebnisse nach 1 Jahr:**
| Kennzahl | Wert | Confidence |
|----------|------|------------|
| Erkannte Überlasten (>70 % SWL) | 12 Ereignisse | documented |
| Präventive Maßnahmen (Umparken, Leinen verstärken) | 12 | documented |
| Mooring-Versagen | 0 (vs. 3 im Vorjahr) | documented |
| Systemkosten | 2.500 EUR/Liegeplatz | documented |
| Wartung/Jahr | 200 EUR/Liegeplatz | estimated |

### A9 — Mooring-System-Vergleich: Marina Split (Kroatien) vor und nach Upgrade

**Situation:** Die Marina Split modernisierte 2020 ihr Mooring-System (300 Liegeplätze, 8–20 m LOA) nach mehreren Bora-Schäden.

**Technische Änderungen:**

| Komponente | Vorher (2010) | Nachher (2020) | Kosten-Differenz/Platz |
|------------|--------------|---------------|----------------------|
| Grundanker | Betonblock 2.000 kg | Betonblock 3.500 kg + Helix-Backup | +1.200 EUR |
| Grundkette | Verzinkt 18 mm | Verzinkt 22 mm | +400 EUR |
| Muringleine | PP 16 mm | PES DB 22 mm | +60 EUR |
| Schäkel | Verzinkter Stahl | Edelstahl 316L | +120 EUR |
| Monitoring | Keines | Stichproben-Lastsensoren (10 %) | +300 EUR (Schnitt) |
| **Gesamt pro Platz** | | | **+2.080 EUR** |

**Ergebnisse nach 3 Saisons (2020–2023):**

| Kennzahl | Vorher (Ø 2015–2019) | Nachher (Ø 2020–2023) | Veränderung | Confidence |
|----------|---------------------|----------------------|-------------|------------|
| Mooring-Ausfälle/Saison | 18 | 2 | −89 % | documented |
| Versicherungsschäden (EUR/Saison) | 45.000 | 3.000 | −93 % | documented |
| Taucher-Einsätze (Notfall) | 35 | 8 | −77 % | documented |
| Kundenbeschwerden (Mooring) | 85 | 12 | −86 % | documented |
| ROI der Investition | — | 2,3 Jahre (Payback) | — | calculated |

**AYDI-Bewertung:** Investition in Mooring-Upgrade amortisiert sich innerhalb von 2–3 Jahren durch reduzierte Schäden und Taucher-Einsätze. Edelstahl-Schäkel und PES-Muringleinen sind die kosteneffektivsten Einzelmaßnahmen.

### A10 — Einhand-Segler: Med-Mooring ohne Crew (Praxisbericht)

**Situation:** Einhandsegler auf SY "Solitaire" (11 m Segelyacht, Bavaria 37) bewältigt Med-Mooring-Manöver im Mittelmeer ohne Crew.

**Technik (entwickelt über 3 Saisons):**

1. **Vorbereitung:** Heckleinen mittschiffs zum Cockpit führen (eine Backbord, eine Steuerbord). Jeweils am Ende: vorgefertigte Auge zum schnellen Überwerfen.
2. **Muringleine:** Langen Bootshaken (4 m) in Cockpit-Nähe bereithalten. Festmacherknecht (Line Holder) am Bug vorbereiten.
3. **Anlauf:** Langsam rückwärts einfahren, Motor im Leerlauf.
4. **Heckleinen:** Vom Cockpit aus eine Heckleine an den nächsten Poller übergeben (oder um eine Pollernase werfen). Zweite Heckleine folgt sofort.
5. **Muringleine:** Mit Bootshaken vom Cockpit aus aufnehmen, zum Bug führen, auf vorbereiteten Festmacherknecht belegen.
6. **Feinabstimmung:** Heckleinen gleichmäßig nachsetzen, Muringleine spannen.

**Erfolgsquote (Selbstbericht):**

| Bedingung | Erfolgsquote | Anmerkung | Confidence |
|-----------|-------------|-----------|------------|
| Windstille | 95 % | Fast immer problemlos | estimated |
| Leichter Wind (querab <10 kn) | 85 % | Gelegentlich 2. Anlauf nötig | estimated |
| Mäßiger Wind (querab 10–15 kn) | 60 % | Oft Hilfe von Nachbarn | estimated |
| Starker Wind (querab >15 kn) | 20 % | Meist abgebrochen, anderen Platz gesucht | estimated |

**AYDI-Empfehlung für Einhandsegler:**
- Bugstrahlruder ist bei Med-Mooring allein fast unverzichtbar
- Fernbedienung für Autopilot/Motor vom Cockpit aus
- Vorgefertigte Leinen mit Augen und Festmacherknechte am Bug
- Bei >15 kn Seitenwind: nicht versuchen, alternative Lösung suchen

### A11 — Langzeit-Studie: Kettenverschleiß an permanenten Moorings (Solent, UK)

**Studie:** Royal Southampton Yacht Club, Monitoring von 50 Swing-Moorings über 15 Jahre (2008–2023).

**Methodik:** Jährliche Tauchinspektion mit Schieblehrmessung an 3 Stellen pro Kette (oberes Drittel, Mitte, unteres Drittel).

**Ergebnisse:**

| Ketten-Alter (Jahre) | Durchschn. Materialverlust (%) | Min. (bester Zustand) | Max. (schlechtester) | N (Stichprobe) | Confidence |
|----------------------|-------------------------------|----------------------|---------------------|----------------|------------|
| 1 | 1,2 | 0,5 | 2,5 | 50 | documented |
| 3 | 4,1 | 2,0 | 8,0 | 48 | documented |
| 5 | 7,8 | 3,5 | 15,0 | 45 | documented |
| 7 | 11,2 | 5,5 | 22,0 | 40 | documented |
| 10 | 16,5 | 8,0 | 30,0 | 32 | documented |
| 12 | 21,0 | 10,0 | 38,0 | 25 | documented |
| 15 | 28,0 | 14,0 | 45,0+ | 18 | documented |

**Schlussfolgerungen:**
- Ab 10 % Materialverlust: erhöhte Aufmerksamkeit (Inspektionsintervall auf 1 Jahr verkürzen)
- Ab 20 % Materialverlust: ERSETZEN (Bruchlast um >35 % reduziert)
- Durchschnittliche wirtschaftliche Lebensdauer: 10–12 Jahre
- Ketten in Strömungsgebieten verschleißen 40–60 % schneller als in ruhigen Gewässern

---

## ANHANG B — Lastberechnungen

### B1 — Windlast-Berechnung (detailliert)

**Formel:**
```
F_wind = 0.5 × ρ × C_d × A × V² × G_f

ρ     = 1,225 kg/m³
C_d   = Widerstandsbeiwert (siehe Tabelle)
A     = Windangriffsfläche (m²)
V     = mittlere Windgeschwindigkeit (m/s)
G_f   = Böenfaktor (1,0 für mittlere, 1,75 für Böen)
```

**Widerstandsbeiwerte:**

| Yacht-Typ | C_d (querab) | C_d (längs) | Confidence |
|-----------|-------------|-------------|------------|
| Segelyacht (Mast, Rigg stehend) | 1,1 | 0,8 | documented |
| Segelyacht (Mast, alles demontiert) | 0,9 | 0,6 | estimated |
| Motoryacht (Flybridge) | 1,2 | 0,9 | documented |
| Motoryacht (Sportbridge) | 1,1 | 0,8 | documented |
| Katamaran | 1,0 | 0,7 | estimated |

### B2 — Strömungslast-Berechnung

**Formel:**
```
F_strom = 0.5 × ρ_w × C_d × A_lat × V_s²

ρ_w    = 1.025 kg/m³ (Seewasser)
C_d    = 1,2 (Unterwasserschiff, querab)
A_lat  = Lateralplanfläche (m²)
V_s    = Strömungsgeschwindigkeit (m/s)
```

### B3 — Kombinierte Designlast

```
F_total = √(F_wind² + F_strom²)   (bei rechtwinklig zueinander)
ODER
F_total = F_wind + F_strom          (bei gleichgerichtet, konservativ)

F_design = SF × F_total × DLF

SF  = Sicherheitsfaktor (3,0 für permanent, 2,0 für temporär)
DLF = Dynamischer Lastfaktor (1,5–3,0)
```

---

## ANHANG C — Confidence-Mapping

### C1 — Confidence-Level für Mooring-System-Bewertungen

| Datenquelle | Confidence-Level | Beschreibung |
|-------------|-----------------|-------------|
| Hersteller-Datenblatt | measured | Bruchlast, Dimensionen, Materialangaben |
| Hafenbehörden-Spezifikation | measured | Mooring-Design, Grundanker-Typ, Ketten-Dimensionen |
| Professionelle Unterwasser-Inspektion | measured | Zustand Kette, Anker, Schäkel |
| Foto (klar, mit Referenz) | visual_high | Bojen-Zustand, Pennant-Zustand, Pfahl-Zustand |
| Foto (unklar) | visual_medium | Ungefähre Einschätzung des Zustands |
| Foto (Unterwasser, trüb) | visual_low | Kaum beurteilbar |
| Erfahrungswerte (Eigner, Forum) | estimated | Typische Lebensdauern, Kosten, regionale Praxis |
| Berechnete Werte | calculated | Lastberechnungen, Schwojkreis, Dimensionierung |
| Servicebericht, Hafenordnung | documented | Wartungsintervalle, Prüfergebnisse |

### C2 — Module-Skip-Kriterien

| Bedingung | Ergebnis |
|-----------|----------|
| Kein Mooring-Typ angegeben | `{"available": false, "reason": "Mooring-Typ nicht spezifiziert"}` |
| Keine Yacht-LOA angegeben | `{"available": false, "reason": "Yacht-Länge nicht angegeben"}` |
| Foto zeigt kein Mooring | `{"available": false, "reason": "Kein Mooring-System erkennbar"}` |
| Region unbekannt | `{"available": true, "warning": "Region nicht bekannt, Standardwerte verwendet"}` |

---

## ANHANG D — Normen-Zusammenfassung

### D1 — ISO 15084:2003 — Verankerung, Festmachen und Schleppen

| Anforderung | Beschreibung | Für Mooring relevant |
|-------------|-------------|---------------------|
| Klampen-Bruchlast | ≥ 2 × WLL der vorgesehenen Leine | Ja (Bugklampe für Pennant) |
| Klampen-Positionierung | Bug, Heck, seitlich (min. 4 für >8 m) | Ja (für Fore-and-Aft, Med-Mooring) |
| Verstärkung unter Deck | Lastrücktragung ins Laminat | Ja (bei hohen Mooring-Lasten) |
| Klüsen | Min-Durchmesser: 3 × Leinendurchmesser | Ja (für Mooring-Leinenführung) |

### D2 — AS 3962:2001 — Guidelines for Design of Marinas (Australien)

| Anforderung | Beschreibung | Wert |
|-------------|-------------|------|
| Mooring-Design-Wind | 50-Jahr-Extremwind | Regional variabel |
| Sicherheitsfaktor | Auf Bruchlast | ≥ 3,0 |
| Inspektionsintervall | Unterwasser-Inspektion | Alle 2 Jahre |
| Eco-Mooring-Pflicht | In Seegras-Gebieten | Ja (seit 2015 NSW) |

---

## ANHANG E — Wartungsintervalle

### E1 — Wartungsplan für permanente Swing-Moorings

| Intervall | Maßnahme | Durchführung | Kosten (ca.) |
|-----------|----------|-------------|-------------|
| Monatlich | Visuell: Boje, Pennant von oben | Eigner | 0 EUR |
| 6 Monate | Pennant prüfen (UV, Schamfil) | Eigner | 0 EUR |
| 1 Jahr | Boje reinigen, Schäkel prüfen | Eigner/Taucher | 100–300 EUR |
| 2–3 Jahre | Kette und Grundanker (Taucher) | Professioneller Taucher | 300–800 EUR |
| 5 Jahre | Grundanker-Position prüfen | Professioneller Taucher | 300–800 EUR |
| 3–5 Jahre | Pennant ersetzen | Eigner | 50–200 EUR |
| 5–10 Jahre | Boje ersetzen | Eigner | 50–200 EUR |
| 8–15 Jahre | Kette ersetzen | Professionell | 500–2.000 EUR |

### E2 — Wartungsplan für Lazy-Line-System (Marina)

| Intervall | Maßnahme | Durchführung | Kosten/Liegeplatz |
|-----------|----------|-------------|-------------------|
| 6 Monate | Lazy Lines visuell prüfen | Marina-Personal | 20 EUR |
| 1 Jahr | Schäkel und Verbindungen prüfen | Taucher | 50 EUR |
| 2 Jahre | Grundkette inspizieren | Professioneller Taucher | 100 EUR |
| 3–5 Jahre | Lazy Lines ersetzen (PP) | Marina | 50–80 EUR |
| 5–7 Jahre | Lazy Lines ersetzen (PES) | Marina | 80–120 EUR |
| 10 Jahre | Schäkel ersetzen | Marina/Taucher | 30–60 EUR |
| 15–20 Jahre | Grundkette ersetzen | Professionell | 300–600 EUR |

---

## ANHANG F — Liegeplatz-Bewertung

### F1 — AYDI-Mooring-Bewertungskategorien

| Kategorie | Gewichtung | Kriterien |
|-----------|-----------|----------|
| Sicherheit | 35 % | Mooring-Dimensionierung, Zustand, Schutz vor Extremwetter |
| Komfort | 20 % | Landgang, Bewegung am Liegeplatz, Nachbar-Abstand |
| Umwelt | 15 % | Eco-Mooring, Seegras-Schutz, Antifouling |
| Kosten | 15 % | Liegegebühren, Wartungskosten, Versicherung |
| Infrastruktur | 15 % | Strom, Wasser, Sanitär, Service-Verfügbarkeit |

### F2 — Bewertungsmatrix

| Aspekt | 1–20 (Mangelhaft) | 21–40 (Ausreichend) | 41–60 (Befriedigend) | 61–80 (Gut) | 81–100 (Sehr gut) |
|--------|-------------------|---------------------|---------------------|-------------|-------------------|
| Mooring-Dimensionierung | Offensichtlich unterdimensioniert | Grenzwertig | Ausreichend für Normalwetter | Dimensioniert für Starkwind | Überdimensioniert, Sturmfest |
| Zustand | Kritische Mängel | Verschleiß sichtbar | Gebrauchsspuren | Gut gewartet | Neuwertig |
| Umweltverträglichkeit | Kettenschleppe auf Seegras | Betonblock, keine Maßnahmen | Standard-Mooring | Eco-Mooring | Zertifiziertes Eco-Mooring |

### F3 — Bewertung verschiedener Mooring-Typen nach Yacht-Typ

| Yacht-Typ | Swing | Fore-and-Aft | Pfahl | Med Stern-to | Boje (Besucher) | Empfehlung |
|-----------|-------|-------------|-------|-------------|-----------------|-----------|
| Segelyacht 8 m | ★★★★★ | ★★★☆☆ | ★★★★★ | ★★★★☆ | ★★★★★ | Swing oder Pfahl |
| Segelyacht 12 m | ★★★★☆ | ★★★☆☆ | ★★★★★ | ★★★★☆ | ★★★★☆ | Pfahl oder Med |
| Segelyacht 16 m | ★★★☆☆ | ★★★☆☆ | ★★★★☆ | ★★★★★ | ★★★☆☆ | Med oder Pfahl |
| Motoryacht 10 m | ★★★★☆ | ★★★★☆ | ★★★★★ | ★★★★★ | ★★★★☆ | Pfahl oder Med |
| Motoryacht 18 m | ★★★☆☆ | ★★★☆☆ | ★★★★★ | ★★★★★ | ★★☆☆☆ | Med oder Pfahl |
| Katamaran 12 m | ★★★☆☆ | ★★☆☆☆ | ★★★★☆ | ★★★☆☆ | ★★★☆☆ | Pfahl (breiter Platz) |
| Superyacht 25 m | ★★☆☆☆ | ★★☆☆☆ | ★★★★★ | ★★★★★ | ★☆☆☆☆ | Med (Marina) |

### F4 — Kosten-Vergleich Mooring-Systeme (pro Jahr, 12 m Yacht)

| Mooring-Typ | Region | Liegegebühr/Jahr | Wartung/Jahr | Gesamt/Jahr | Confidence |
|-------------|--------|-----------------|-------------|-------------|------------|
| Swing-Mooring (eigen) | UK (Solent) | 1.500 GBP (Lizenz) | 300 GBP | 1.800 GBP | documented |
| Marina-Steg | UK (Solent) | 5.000 GBP | 0 GBP | 5.000 GBP | documented |
| Marina-Steg (Med) | Kroatien | 4.000 EUR | 0 EUR | 4.000 EUR | documented |
| Marina-Steg (Med) | Côte d'Azur | 12.000 EUR | 0 EUR | 12.000 EUR | documented |
| Pfahl-Mooring | Schweden (Gästehafen) | 500 SEK/Nacht | 0 | Variabel | documented |
| Pfahl-Mooring | Niederlande (Jahresliegeplatz) | 3.000 EUR | 0 EUR | 3.000 EUR | documented |
| Swing-Mooring (eigen) | Australien (NSW) | 1.200 AUD (Lizenz) | 500 AUD | 1.700 AUD | documented |
| Bojenfeld (kommunal) | Karibik (BVI) | 3.000 USD | 200 USD | 3.200 USD | estimated |

---

## ANHANG G — Historische Entwicklung

### G1 — Etymologie und Begriffsgeschichte

| Begriff | Herkunft | Erste Verwendung | Bedeutungswandel |
|---------|---------|-----------------|------------------|
| Mooring | Altniederländisch „moren" (festmachen) | 13. Jahrhundert | Von „Schiff festmachen" zu „permanenter Liegeplatz" |
| Muring | Deutsch, von Mooring | 19. Jahrhundert | Speziell: Grundleine im Hafen (Med-Mooring) |
| Dalbe | Niederländisch „dukdalf" (Herzog Alba) | 16. Jahrhundert | Einzelpfahl oder Pfahlgruppe im Wasser |
| Boje | Niederländisch „boei" (Fessel) | 15. Jahrhundert | Schwimmkörper zur Markierung |
| Lazy Line | Englisch | 20. Jahrhundert | „Faule Leine" — liegt untätig im Wasser, bis sie gebraucht wird |
| Pennant | Französisch „pendant" (hängend) | 17. Jahrhundert | Hängende Leine von der Boje |

### G2 — Meilensteine der Mooring-Technik

| Jahr | Entwicklung | Bedeutung |
|------|-------------|----------|
| ~3000 v. Chr. | Erste Steingewichts-Moorings (Ägypten) | Früheste bekannte permanente Schiffsbefestigung |
| ~500 v. Chr. | Holzpfahl-Moorings (Phönizier) | Erste Pfahl-Moorings im Mittelmeer |
| 1700–1800 | Eisenketten-Moorings (Kriegsmarinen) | Kette ersetzt Tau als Grundgeschirr |
| 1850 | Pilzanker-Patent (USA) | Erste Massenproduktion permanenter Anker |
| 1950 | Erste Schwimm-Steg-Marinas (USA) | Beginn des modernen Marina-Baus |
| 1970 | Polyform-Gründung (Norwegen) | Standardisierung von Mooring-Bojen |
| 1985 | Seaflex-Patent (Schweden) | Revolution der elastischen Mooring-Technik |
| 1995 | Helix-Schraubanker für Yachten | Umweltschonende Alternative zu Betonblöcken |
| 2010 | Eco-Mooring-Regulierung (Australien) | Erste staatliche Vorschrift für umweltschonende Moorings |
| 2015 | Smartmooring-Systeme (Pilotprojekte) | Digitale Überwachung von Mooring-Systemen |
| 2020 | EU-Regulierung Seegras-Schutz | Verstärkte Auflagen für Mooring-Felder im Mittelmeer |
| 2023 | Smartmooring-Pilotprojekte (Mallorca, Antibes) | Echtzeit-Lastüberwachung an Mooring-Systemen |
| 2024 | HMPE-Grundketten (Prototyp) | Synthetische Ketten ohne Korrosion für Offshore-Moorings |
| 2025 | KI-basierte Mooring-Inspektion (ROV + Vision) | Automatische Zustandsbewertung durch Unterwasser-Drohnen |

---

## ANHANG H — AYDI-Integration (Pydantic-Modelle)

### H1 — Datenmodelle für Mooring-Systeme

```python
"""
AYDI Mooring System Models — Pydantic v2
Module: 13_07_mooring_systeme

All models use model_config = {"from_attributes": True}
German domain terms, English code.
"""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


# --- Enums ---

class MooringType(str, Enum):
    """Type of mooring system."""
    SWING = "swing"
    FORE_AND_AFT = "fore_and_aft"
    PILE = "pile"
    MED_STERN_TO = "med_stern_to"
    MED_BOW_TO = "med_bow_to"
    LAZY_LINE = "lazy_line"
    BUOY_VISITOR = "buoy_visitor"
    TROT = "trot"
    DRYING = "drying"


class GroundAnchorType(str, Enum):
    """Type of ground anchor for permanent moorings."""
    CONCRETE_BLOCK = "concrete_block"
    MUSHROOM = "mushroom"
    HELIX_SCREW = "helix_screw"
    DRAG_EMBEDMENT = "drag_embedment"
    KENTLEDGE = "kentledge"
    SUCTION_CAISSON = "suction_caisson"


class LazyLineMaterial(str, Enum):
    """Material of lazy line / mooring line."""
    POLYPROPYLENE = "polypropylene"
    POLYESTER = "polyester"
    POLYESTER_DOUBLE_BRAID = "polyester_double_braid"
    HMPE = "hmpe"
    NYLON = "nylon"


class MooringRegion(str, Enum):
    """Region with specific mooring practices."""
    MEDITERRANEAN = "mediterranean"
    SCANDINAVIA = "scandinavia"
    UK = "uk"
    CARIBBEAN = "caribbean"
    AUSTRALIA = "australia"
    NORTH_GERMANY = "north_germany"
    NETHERLANDS = "netherlands"


class ConfidenceLevel(str, Enum):
    """Confidence level for findings."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    DOCUMENTED = "documented"
    BENCHMARK = "benchmark"


class Severity(str, Enum):
    """Severity of a finding."""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


# --- Core Models ---

class MooringSystem(BaseModel):
    """Represents a complete mooring system configuration."""

    model_config = {"from_attributes": True}

    mooring_type: MooringType = Field(
        ...,
        description="Type of mooring system (swing, pile, med_stern_to, etc.)"
    )
    region: Optional[MooringRegion] = Field(
        None,
        description="Region with specific mooring practices"
    )
    yacht_loa_m: float = Field(
        ..., gt=0, le=100,
        description="Yacht length overall in meters"
    )
    yacht_displacement_kg: Optional[float] = Field(
        None, gt=0,
        description="Yacht displacement in kg"
    )
    yacht_beam_m: Optional[float] = Field(
        None, gt=0,
        description="Yacht beam in meters"
    )
    wind_area_m2: Optional[float] = Field(
        None, gt=0,
        description="Windage area (lateral) in m²"
    )
    ground_anchor_type: Optional[GroundAnchorType] = Field(
        None,
        description="Type of ground anchor"
    )
    ground_anchor_weight_kg: Optional[float] = Field(
        None, gt=0,
        description="Ground anchor weight in kg"
    )
    ground_anchor_holding_kn: Optional[float] = Field(
        None, gt=0,
        description="Ground anchor holding capacity in kN"
    )
    riser_chain_diameter_mm: Optional[float] = Field(
        None, gt=0,
        description="Riser chain diameter in mm"
    )
    riser_chain_length_m: Optional[float] = Field(
        None, gt=0,
        description="Riser chain length in meters"
    )
    pennant_diameter_mm: Optional[float] = Field(
        None, gt=0,
        description="Pennant diameter in mm"
    )
    pennant_material: Optional[LazyLineMaterial] = Field(
        None,
        description="Pennant material"
    )
    pennant_length_m: Optional[float] = Field(
        None, gt=0,
        description="Pennant length in meters"
    )
    water_depth_m: Optional[float] = Field(
        None, gt=0,
        description="Water depth at mooring location in meters"
    )
    tidal_range_m: Optional[float] = Field(
        None, ge=0,
        description="Tidal range in meters"
    )
    design_wind_kn: Optional[float] = Field(
        None, gt=0,
        description="Design wind speed in knots"
    )
    confidence: ConfidenceLevel = Field(
        ConfidenceLevel.ESTIMATED,
        description="Confidence level of the mooring data"
    )


class LazyLine(BaseModel):
    """Represents a lazy line (Muringleine) in a Med-mooring system."""

    model_config = {"from_attributes": True}

    material: LazyLineMaterial = Field(
        ...,
        description="Lazy line material"
    )
    diameter_mm: float = Field(
        ..., gt=0, le=60,
        description="Lazy line diameter in mm"
    )
    length_m: float = Field(
        ..., gt=0,
        description="Lazy line length in meters"
    )
    breaking_load_kn: Optional[float] = Field(
        None, gt=0,
        description="Breaking load in kN"
    )
    age_years: Optional[float] = Field(
        None, ge=0,
        description="Age of lazy line in years"
    )
    condition_score: Optional[int] = Field(
        None, ge=0, le=100,
        description="Condition score 0-100"
    )
    is_floating: bool = Field(
        False,
        description="True if the lazy line floats (PP), False if it sinks (PES)"
    )
    last_inspection_date: Optional[str] = Field(
        None,
        description="Date of last inspection (ISO 8601)"
    )
    confidence: ConfidenceLevel = Field(
        ConfidenceLevel.ESTIMATED,
        description="Confidence level of the lazy line data"
    )


class PileMooring(BaseModel):
    """Represents a pile (Pfahl/Dalbe) mooring configuration."""

    model_config = {"from_attributes": True}

    pile_count: int = Field(
        ..., ge=1, le=8,
        description="Number of piles (2, 4, or more)"
    )
    pile_material: str = Field(
        ...,
        description="Pile material (oak, tropical_hardwood, steel)"
    )
    pile_diameter_mm: float = Field(
        ..., gt=0,
        description="Pile diameter in mm"
    )
    pile_height_above_water_m: float = Field(
        ..., gt=0,
        description="Pile height above water in meters"
    )
    has_sliding_ring: bool = Field(
        False,
        description="True if piles have sliding rings for tidal compensation"
    )
    tidal_range_m: float = Field(
        0.0, ge=0,
        description="Tidal range at this location in meters"
    )
    line_diameter_mm: Optional[float] = Field(
        None, gt=0,
        description="Recommended mooring line diameter in mm"
    )
    max_lateral_force_kn: Optional[float] = Field(
        None, gt=0,
        description="Maximum lateral force per pile in kN"
    )
    confidence: ConfidenceLevel = Field(
        ConfidenceLevel.ESTIMATED,
        description="Confidence level of pile mooring data"
    )


class MooringBuoy(BaseModel):
    """Represents a mooring buoy."""

    model_config = {"from_attributes": True}

    manufacturer: Optional[str] = Field(
        None,
        description="Buoy manufacturer (e.g. Polyform)"
    )
    model: Optional[str] = Field(
        None,
        description="Buoy model designation"
    )
    diameter_mm: float = Field(
        ..., gt=0,
        description="Buoy diameter in mm"
    )
    buoyancy_kg: float = Field(
        ..., gt=0,
        description="Buoyancy in kg"
    )
    material: str = Field(
        "PE",
        description="Buoy material (PE, PVC, steel)"
    )
    max_yacht_loa_m: Optional[float] = Field(
        None, gt=0,
        description="Maximum recommended yacht LOA in meters"
    )
    has_pickup_stick: bool = Field(
        False,
        description="True if buoy has a pick-up stick"
    )
    condition_score: Optional[int] = Field(
        None, ge=0, le=100,
        description="Condition score 0-100"
    )
    confidence: ConfidenceLevel = Field(
        ConfidenceLevel.ESTIMATED,
        description="Confidence level of buoy data"
    )


class MooringFinding(BaseModel):
    """A single finding from mooring system analysis."""

    model_config = {"from_attributes": True}

    finding_id: str = Field(
        ...,
        description="Finding ID (e.g. MO-01, MO-02)"
    )
    title: str = Field(
        ...,
        description="Finding title in German"
    )
    description: str = Field(
        ...,
        description="Detailed description in German"
    )
    severity: Severity = Field(
        ...,
        description="Severity level"
    )
    category: str = Field(
        ...,
        description="Category (e.g. lazy_line, ground_anchor, pennant, pile)"
    )
    location: Optional[str] = Field(
        None,
        description="Location reference (e.g. bow, stern, port, starboard)"
    )
    suggestion: str = Field(
        ...,
        description="Suggested action in German"
    )
    estimated_cost_eur: Optional[float] = Field(
        None, ge=0,
        description="Estimated repair/replacement cost in EUR"
    )
    confidence: ConfidenceLevel = Field(
        ...,
        description="Confidence level of this finding"
    )


class SwingCircleCalculation(BaseModel):
    """Result of a swing circle (Schwojkreis) calculation."""

    model_config = {"from_attributes": True}

    yacht_loa_m: float = Field(
        ..., gt=0,
        description="Yacht LOA in meters"
    )
    pennant_length_m: float = Field(
        ..., gt=0,
        description="Pennant length in meters"
    )
    chain_scope_m: float = Field(
        ..., gt=0,
        description="Horizontal chain scope in meters"
    )
    swing_radius_m: float = Field(
        ..., gt=0,
        description="Calculated swing radius in meters"
    )
    min_distance_to_neighbor_m: float = Field(
        ..., gt=0,
        description="Minimum safe distance to neighbor mooring in meters"
    )
    confidence: ConfidenceLevel = Field(
        ConfidenceLevel.CALCULATED,
        description="Always calculated"
    )


class MooringLoadCalculation(BaseModel):
    """Result of a mooring load calculation."""

    model_config = {"from_attributes": True}

    wind_load_kn: float = Field(
        ..., ge=0,
        description="Wind load in kN"
    )
    current_load_kn: float = Field(
        0.0, ge=0,
        description="Current load in kN"
    )
    dynamic_factor: float = Field(
        1.5, gt=0,
        description="Dynamic load factor"
    )
    safety_factor: float = Field(
        3.0, gt=0,
        description="Safety factor"
    )
    total_design_load_kn: float = Field(
        ..., gt=0,
        description="Total design load in kN"
    )
    required_holding_capacity_kn: float = Field(
        ..., gt=0,
        description="Required ground anchor holding capacity in kN"
    )
    recommended_chain_mm: Optional[int] = Field(
        None, gt=0,
        description="Recommended chain diameter in mm"
    )
    recommended_pennant_mm: Optional[int] = Field(
        None, gt=0,
        description="Recommended pennant diameter in mm"
    )
    confidence: ConfidenceLevel = Field(
        ConfidenceLevel.CALCULATED,
        description="Confidence level"
    )


class MooringSystemAssessment(BaseModel):
    """Complete assessment of a mooring system."""

    model_config = {"from_attributes": True}

    mooring_system: MooringSystem = Field(
        ...,
        description="The mooring system being assessed"
    )
    overall_score: int = Field(
        ..., ge=0, le=100,
        description="Overall mooring system score (0-100)"
    )
    safety_score: int = Field(
        ..., ge=0, le=100,
        description="Safety sub-score (0-100)"
    )
    dimensioning_score: int = Field(
        ..., ge=0, le=100,
        description="Dimensioning sub-score (0-100)"
    )
    condition_score: int = Field(
        ..., ge=0, le=100,
        description="Condition sub-score (0-100)"
    )
    environmental_score: int = Field(
        ..., ge=0, le=100,
        description="Environmental impact sub-score (0-100)"
    )
    findings: list[MooringFinding] = Field(
        default_factory=list,
        description="List of findings"
    )
    load_calculation: Optional[MooringLoadCalculation] = Field(
        None,
        description="Load calculation results (if data available)"
    )
    swing_circle: Optional[SwingCircleCalculation] = Field(
        None,
        description="Swing circle calculation (if swing mooring)"
    )
    recommendations: list[str] = Field(
        default_factory=list,
        description="List of recommendations in German"
    )
    confidence: ConfidenceLevel = Field(
        ...,
        description="Overall confidence level of the assessment"
    )
```

### H2 — Beispiel-Aufruf

```python
# Example: Assess a swing mooring for a 12m sailing yacht

mooring = MooringSystem(
    mooring_type=MooringType.SWING,
    region=MooringRegion.UK,
    yacht_loa_m=12.0,
    yacht_displacement_kg=8000,
    yacht_beam_m=3.8,
    wind_area_m2=15.0,
    ground_anchor_type=GroundAnchorType.MUSHROOM,
    ground_anchor_weight_kg=200,
    ground_anchor_holding_kn=24.0,
    riser_chain_diameter_mm=14,
    riser_chain_length_m=12.0,
    pennant_diameter_mm=18,
    pennant_material=LazyLineMaterial.NYLON,
    pennant_length_m=5.0,
    water_depth_m=4.0,
    tidal_range_m=3.5,
    design_wind_kn=45,
    confidence=ConfidenceLevel.DOCUMENTED,
)

assessment = MooringSystemAssessment(
    mooring_system=mooring,
    overall_score=72,
    safety_score=68,
    dimensioning_score=75,
    condition_score=80,
    environmental_score=65,
    findings=[
        MooringFinding(
            finding_id="MO-03",
            title="Grundkette grenzwertig dimensioniert",
            description="14 mm Kette für 12 m Yacht bei 3,5 m Tidenhub "
                        "ist Mindestdimensionierung. Bei Starkwind + Springtide "
                        "könnten die Lasten die Arbeitslast überschreiten.",
            severity=Severity.MEDIUM,
            category="riser_chain",
            location="underwater",
            suggestion="Upgrade auf 16 mm Kette empfohlen (Bruchlast 82 kN "
                       "vs. 63 kN bei 14 mm). Kosten ca. 500–800 EUR.",
            estimated_cost_eur=650.0,
            confidence=ConfidenceLevel.CALCULATED,
        ),
    ],
    load_calculation=MooringLoadCalculation(
        wind_load_kn=5.0,
        current_load_kn=1.5,
        dynamic_factor=1.8,
        safety_factor=3.0,
        total_design_load_kn=11.7,
        required_holding_capacity_kn=35.1,
        recommended_chain_mm=16,
        recommended_pennant_mm=20,
        confidence=ConfidenceLevel.CALCULATED,
    ),
    swing_circle=SwingCircleCalculation(
        yacht_loa_m=12.0,
        pennant_length_m=5.0,
        chain_scope_m=7.0,
        swing_radius_m=24.0,
        min_distance_to_neighbor_m=53.0,
        confidence=ConfidenceLevel.CALCULATED,
    ),
    recommendations=[
        "Grundkette auf 16 mm upgraden (aktuelle 14 mm grenzwertig).",
        "Pennant alle 3 Jahre ersetzen, aktuellen Zustand prüfen.",
        "Tidenhub von 3,5 m erfordert Gleitringe an Pfählen (falls vorhanden).",
        "Pilzanker mit 200 kg hat nach Einsaugen ca. 24 kN — für 12 m Yacht "
        "im Solent knapp. Upgrade auf 500 kg oder Helix-Anker empfohlen.",
    ],
    confidence=ConfidenceLevel.CALCULATED,
)
```

---

## ANHANG I — Bewertungsschema

### I1 — Mooring-System-Bewertungsmatrix (AYDI-Standard)

| Kriterium | Gewichtung | 0–20 | 21–40 | 41–60 | 61–80 | 81–100 |
|-----------|-----------|------|-------|-------|-------|--------|
| Grundanker-Haltekraft | 25 % | <50 % der Designlast | 50–75 % | 75–100 % | 100–150 % | >150 % |
| Ketten-Zustand | 20 % | >20 % Abtrag | 10–20 % | 5–10 % | <5 % | Neuwertig |
| Pennant-Zustand | 15 % | Gerissen/kritisch | UV-geschädigt | Gebrauchsspuren | Gut | Neuwertig |
| Dimensionierung (Kette+Pennant) | 15 % | Deutlich zu dünn | Grenzwertig | Ausreichend | Empfohlen | Überdimensioniert |
| Bojen-Zustand | 10 % | Gesunken/Leck | Stark bewachsen | Bewuchsspuren | Sauber | Neuwertig |
| Umweltverträglichkeit | 10 % | Kettenschleppe auf Seegras | Betonblock Standard | Keine Schäden | Eco-Mooring | Zertifiziertes Eco |
| Wartungsdokumentation | 5 % | Keine | Lückenhaft | Unregelmäßig | Regelmäßig | Lückenlos |

### I2 — Automatische Empfehlungsschwellen

| Score | Empfehlung | Dringlichkeit |
|-------|-----------|---------------|
| 0–20 | Mooring NICHT verwenden, sofortige Reparatur/Ersatz | SOFORT |
| 21–40 | Mooring nur bei ruhigem Wetter, Reparatur planen | Innerhalb 1 Monat |
| 41–60 | Mooring nutzbar, Verbesserungen empfohlen | Innerhalb 6 Monate |
| 61–80 | Mooring in gutem Zustand, normale Wartung | Nächste reguläre Wartung |
| 81–100 | Mooring in sehr gutem Zustand | Keine sofortigen Maßnahmen |

---

## ANHANG J — Troubleshooting-Entscheidungsbäume (erweitert)

### J1 — Ruckbelastung (Snatch Load) reduzieren

```
Boot ruckt stark am Mooring (Surge/Snatch)
│
├── Pennant zu kurz/steif?
│   ├── JA → Längeren Nylon-Pennant verwenden (≥5 m)
│   │        → Elastischen Pendant (Hazelett EMP) einbauen
│   └── NEIN ↓
│
├── Kette zu straff (kein Catenary)?
│   ├── JA → Mehr Kettenlänge ausbringen
│   │        → Schwerere Kette verwenden (besserer Catenary)
│   │        → Kettenverlängerung zwischen Boje und Klampe
│   └── NEIN ↓
│
├── Wellen/Schwell von vorne?
│   ├── JA → Mooring Bridle verwenden (V-Form am Bug)
│   │        → Liegeplatz wechseln (geschützter)
│   │        → Reitgewicht (Kellet) auf Pennant/Kette
│   └── NEIN ↓
│
└── Yacht zu leicht für das Mooring?
    → Mehr Ballast (Wasser-Tanks füllen)
    → Leichteres Mooring-Setup (dünnere Kette, längerer Pennant)
```

### J2 — Yacht schwojt zu stark am Swing-Mooring

```
Yacht schwojt unkontrolliert (Yawing/Schwojen)
│
├── Wind und Strom aus verschiedenen Richtungen?
│   ├── JA → Normal bei Wechsel Strom/Wind
│   │        → Fore-and-Aft-Mooring in Betracht ziehen
│   │        → Reitgewicht auf Pennant (dämpft)
│   └── NEIN ↓
│
├── Pennant zu lang?
│   ├── JA → Kürzen (max. 3–5 m)
│   │        → Bridle verwenden
│   └── NEIN ↓
│
├── Ruderprofil ungünstig (Langkieler)?
│   ├── JA → Ruder mittschiffs festsetzen
│   │        → Windfahne/Sturmruder montieren
│   └── NEIN ↓
│
└── Nachbar-Mooring kollidiert?
    → Schwojkreis berechnen und mit Nachbarn vergleichen
    → Ggf. Mooring versetzen
    → Ggf. Fore-and-Aft umrüsten
```

---

## ANHANG K — Kostenkalkulation

### K1 — Neues Swing-Mooring — Kostenaufstellung

| Position | Beschreibung | Klein (8 m) | Mittel (12 m) | Groß (16 m) | Super (20 m) | Confidence |
|----------|-------------|------------|--------------|------------|-------------|------------|
| Grundanker | Betonblock | 300 EUR | 600 EUR | 1.000 EUR | 1.800 EUR | estimated |
| Grundanker | Helix-Anker (Alternative) | 2.000 EUR | 3.500 EUR | 5.500 EUR | 8.000 EUR | documented |
| Grundkette | Verzinktes Kurzglied | 200 EUR | 400 EUR | 700 EUR | 1.200 EUR | documented |
| Schäkel/Wirbel | Verzinkt oder Edelstahl | 80 EUR | 120 EUR | 180 EUR | 280 EUR | documented |
| Boje | Polyform MB-Serie | 50 EUR | 90 EUR | 130 EUR | 180 EUR | documented |
| Pennant | Nylon DB | 60 EUR | 90 EUR | 130 EUR | 180 EUR | documented |
| Installation | Taucher + Barge | 500 EUR | 1.000 EUR | 1.500 EUR | 2.500 EUR | estimated |
| **Gesamt (Betonblock)** | | **1.190 EUR** | **2.300 EUR** | **3.640 EUR** | **6.140 EUR** | estimated |
| **Gesamt (Helix-Anker)** | | **2.890 EUR** | **5.200 EUR** | **8.140 EUR** | **12.340 EUR** | estimated |

### K2 — Jährliche Wartungskosten

| Position | Klein (8 m) | Mittel (12 m) | Groß (16 m) | Confidence |
|----------|------------|--------------|------------|------------|
| Taucher-Inspektion (1×/Jahr) | 150 EUR | 200 EUR | 300 EUR | estimated |
| Pennant-Ersatz (anteilig 1/3 pro Jahr) | 20 EUR | 30 EUR | 45 EUR | estimated |
| Bojen-Wartung (anteilig) | 10 EUR | 15 EUR | 20 EUR | estimated |
| Schäkel-Ersatz (anteilig) | 10 EUR | 15 EUR | 25 EUR | estimated |
| Lizenz (wenn erforderlich) | 200–800 EUR | 400–1.500 EUR | 600–2.500 EUR | documented |
| **Gesamt (ohne Lizenz)** | **190 EUR** | **260 EUR** | **390 EUR** | estimated |

---

## ANHANG L — Regionale Hafenordnungen

### L1 — Mooring-Regulierung nach Land

| Land | Regulierungsbehörde | Lizenz nötig? | Inspektion Pflicht? | Eco-Mooring Pflicht? | Confidence |
|------|--------------------|--------------|--------------------|---------------------|------------|
| Deutschland | WSV / Kommune | Ja (kommunal) | Nein (empfohlen) | Nein | documented |
| Schweden | Transportstyrelsen / Kommune | Teilweise | Nein | Nein | documented |
| Norwegen | Kystverket / Kommune | Teilweise | Nein | Nein | documented |
| Finnland | Traficom / Kommune | Teilweise | Nein | Nein | estimated |
| UK | Crown Estate / MMO | Ja (immer) | Ja (Harbour Master) | Nein (empfohlen) | documented |
| Frankreich | Préfecture Maritime | Ja (außer öffentliche Häfen) | Teilweise | Teilweise (Natura 2000) | documented |
| Kroatien | Lučka kapetanija | Marina-Lizenz | Ja (Marina-Inspektion) | Nein | documented |
| Griechenland | Limenarchion | Marina-Lizenz | Variabel | Nein | documented |
| Australien (NSW) | RMS | Ja (immer) | Ja (jährlich) | Ja (Seegras) | documented |
| USA | Army Corps / State | Variabel | Variabel | Teilweise (Florida Keys) | documented |

---

## ANHANG M — Testprotokolle und Prüfverfahren

### M1 — Mooring-Ketten-Prüfung (Tauchinspektion)

| Prüfschritt | Methode | Akzeptanzkriterium | Werkzeug |
|-------------|---------|-------------------|----------|
| Glieddurchmesser messen | Schieblehre unter Wasser | ≥90 % des Nenn-Ø | Tauchschieblehre |
| Korrosion beurteilen | Visuell + taktil | Keine tiefen Narben | Unterwasserkamera |
| Gliedverformung prüfen | Visuell | Keine gelängten oder offenen Glieder | Unterwasserkamera |
| Schäkel prüfen | Visuell + Bolzen bewegen | Bolzen gangbar, kein Materialverlust | Unterwasser-Werkzeug |
| Grundanker-Position | GPS + Referenzmarke | Keine Positionsänderung >1 m | GPS |
| Bewuchs dokumentieren | Foto | Dokumentation | Unterwasserkamera |

### M2 — Pennant-Prüfung (Oberfläche)

| Prüfschritt | Methode | Akzeptanzkriterium |
|-------------|---------|-------------------|
| UV-Degradation | Biegetest (Leine um 180° biegen) | Oberfläche bricht nicht auf |
| Schamfilschaden | Visuell (gesamte Länge) | Keine freiliegenden Kernfasern |
| Dehnfähigkeit | Manuell spannen und lösen | Rückstellung innerhalb 5 Sekunden |
| Spleißverbindung | Visuell (Auge, Spleiß) | Spleiß intakt, kein Nachrutschen |
| Farbveränderung | Visuell (Vergleich mit Original) | Leichte Verblassung akzeptabel |

### M3 — Grundanker-Zugprüfung (Pull Test)

| Prüfschritt | Methode | Akzeptanzkriterium | Werkzeug |
|-------------|---------|-------------------|----------|
| Statische Zuglast anlegen | Boot mit Windenbetrieb | Keine Bewegung bei 1,5 × WLL | Windenbetrieb + GPS |
| Last steigern bis 2 × WLL | Schrittweise erhöhen (10 % Stufen) | Keine Positionsänderung >0,5 m | Dynamometer + GPS |
| Last halten (30 min) | Statisch bei 2 × WLL | Kein Nachgeben, keine Drift | Dynamometer + GPS |
| Entlasten und Position prüfen | GPS-Vergleich vorher/nachher | Position identisch (±0,3 m) | GPS |

### M4 — Boje-Auftriebsprüfung

| Prüfschritt | Methode | Akzeptanzkriterium |
|-------------|---------|-------------------|
| Sichtprüfung | Visuell auf Risse, Lecks, Verformung | Keine sichtbaren Defekte |
| Bewuchs entfernen | Schaber/Bürste, Hochdruckreiniger | Oberfläche sauber und glatt |
| Gewichtstest (an Land) | Wiegen nach Reinigung | Gewicht ≤110 % des Neugewichts (sonst Wasser eingedrungen) |
| Schwimmtest | Boje ins Wasser setzen, Auftrieb beobachten | Auftrieb ≥80 % des Nennwerts |
| Augbolzen prüfen | Visuell + Zugtest mit 5 kN | Kein Spiel, keine Korrosion an der Durchführung |

### M5 — Elastisches Mooring-System — Prüfung (Seaflex)

| Prüfschritt | Methode | Akzeptanzkriterium |
|-------------|---------|-------------------|
| Visuelle Inspektion (Taucher) | Oberfläche der Gummi-Ummantelung | Keine Risse, keine Aufquellungen |
| Dehnungsprüfung | Manuell oder mit Hilfsboot | Dehnung ≥80 % des Nennwerts |
| Rückstellverhalten | Nach Dehnung: Rückkehr zur Ruhelänge | Rückkehr innerhalb 60 Sekunden |
| Befestigungspunkte | Visuell + Zugtest | Edelstahl-Verbindungen intakt, kein Spiel |
| Biofouling | Visuell | Dokumentieren, bei starkem Bewuchs reinigen |

---

## ANHANG N — Zusätzliche Fallstudien

### N1 — Fore-and-Aft-Mooring im Hamble River (UK)

**Situation:** SY "Seahorse" (10 m, 5.500 kg) auf Fore-and-Aft-Mooring im Hamble River, Tidenhub 4,2 m, Strom bis 2,5 kn.

**Problem:** Bei Springtide + starker Ebbe lag die Yacht an der Grundkette des Heck-Ankers. Ruck-Belastung bei Strom-Wechsel.

**Lösung:**
- Kettenlänge (Riser) um 3 m verlängert
- Elastischer Pendant (Hazelett EMP-2) zwischen Boje und Pennant eingebaut
- Ergebnis: Ruckbelastung um 55 % reduziert, Yacht liegt ruhiger

| Maßnahme | Kosten | Wirkung | Confidence |
|----------|--------|---------|------------|
| Kettenverlängerung 3 m (12 mm) | 120 EUR | Mehr Scope → weniger Rucklasten | documented |
| Hazelett EMP-2 | 150 EUR | 50 % Dehnung, Spitzenlast-Reduktion | documented |
| Installation (Taucher) | 200 EUR | — | estimated |
| **Gesamt** | **470 EUR** | Liegeplatz deutlich verbessert | — |

### N2 — Eco-Mooring-Installation in Posidonia-Gebiet (Mallorca)

**Situation:** 2022, Cala Pi (Südküste Mallorca). Traditionelle Moorings (20 × Betonblock + Kette) beschädigten Posidonia oceanica.

**Maßnahme:** Umstellung auf Eco-Moorings (Helix-Anker + Seaflex).

| Aspekt | Vorher | Nachher | Confidence |
|--------|--------|---------|------------|
| Mooring-Typ | 20 × 2.000 kg Betonblock + 20 mm Kette | 20 × Helix SJ-300 + Seaflex SF-20 | documented |
| Kettenschleppe-Radius | 5–8 m pro Mooring | 0 m (elastisch, kein Bodenkontakt) | documented |
| Posidonia-Deckung | 45 % (abnehmend) | 62 % nach 3 Jahren (zunehmend) | documented |
| Kosten pro Mooring | 1.500 EUR | 5.500 EUR | documented |
| Liegeplatz-Qualität | Ruckartig, laut (Kettenrasseln) | Ruhig, gedämpft | documented |

### N3 — Katamaran-Mooring-Herausforderungen (Karibik)

**Situation:** Charterkatamaran Lagoon 450 (14 m, Breite 7,7 m) in den BVI auf Swing-Mooring.

**Problem:** Katamarane haben erheblich höhere Windangriffsfläche als Einrumpfboote gleicher LOA. Standardmoorings für 14 m Einrumpfboote sind für Katamarane oft unterdimensioniert.

| Vergleich | Einrumpf 14 m | Katamaran 14 m | Faktor | Confidence |
|-----------|--------------|----------------|--------|------------|
| Windangriffsfläche querab | 18 m² | 28 m² | 1,55 | estimated |
| Verdrängung | 12.000 kg | 11.000 kg | 0,92 | documented |
| Schwojkreis-Radius | 25 m | 30 m | 1,20 | calculated |
| Windlast bei 35 kn | 5,5 kN | 8,5 kN | 1,55 | calculated |

**Lösung:**
- Mooring eine Klasse höher dimensionieren (Mooring für 18 m Einrumpfer für 14 m Katamaran)
- Bridle verwenden (V-Form zu beiden Rümpfen), um Gierbewegung zu reduzieren
- Pennant 22–24 mm statt 18 mm

**AYDI-Empfehlung:** Katamaran-Korrekturfaktor für Mooring-Dimensionierung: LOA_eff = LOA × 1,3 (d. h. ein 14 m Katamaran wird wie ein 18 m Einrumpfboot berechnet).

### N4 — Mooring-Problematik in Gezeitenflüssen (Dart Estuary, UK)

**Situation:** Dart Estuary, Devon. Tidenhub 4,5 m, Gezeitenstrom bis 3,5 kn. 400 Swing-Moorings in enger Flussmündung.

**Spezifische Herausforderungen:**

| Herausforderung | Auswirkung | Lösung | Confidence |
|----------------|-----------|--------|------------|
| Strom wechselt 4×/Tag | Yacht dreht sich, Schwojkreise überlagern | Fore-and-Aft-Moorings in engen Bereichen | documented |
| Strom + Wind gegeneinander | Yacht liegt quer → max. Windlast + Stromlast | Überdimensionierung (Faktor 1,5) | documented |
| Treibgut bei Hochwasser | Bäume, Äste treiben gegen Pennant und Kette | Ketten-Fang (Debris Guard) am Riser | documented |
| Schlick-Boden | Pilzanker versinken, Betonblöcke kippen | Doppelter Betonblock oder Helix | documented |

### N5 — Smart-Mooring-Erfahrung einer Superyacht-Marina (Port Vauban, Antibes)

**Situation:** Port Vauban, Antibes — größte Superyacht-Marina Europas (1.600 Liegeplätze, davon 30 für Yachten 60+ m).

**Smartmooring-System (installiert 2023):**
- 50 Liegeplätze (40–80 m) mit Lastsensoren an allen Muringleinen
- Wetterstationen (2) liefern Echtzeit-Wind und Wellengang
- Dashboard für Hafenmeister: Echtzeit-Anzeige aller Lasten
- Alarmierung: automatische SMS an Captain bei >60 % SWL
- Historische Daten: Trend-Analyse für vorausschauende Wartung

**Ergebnisse nach 18 Monaten:**

| Kennzahl | Wert | Vorjahr (ohne System) | Confidence |
|----------|------|----------------------|------------|
| Erkannte Überlasten | 28 Ereignisse | Unbekannt | documented |
| Präventive Umparkvorgänge | 15 | 0 (reaktiv) | documented |
| Mooring-bezogene Schäden | 0 | 4 | documented |
| Geschätzte Schadensvermeidung | 350.000 EUR | — | estimated |
| System-ROI | 1,4 Jahre | — | calculated |

---

## ANHANG O — Eigner-Erfahrungen und Feldberichte

### O1 — Blauwasser-Segler: Mooring-Erfahrungen weltweit

**Quelle:** Erfahrungsbericht SY "Calypso" (14 m Alu-Segler), 5 Jahre Blauwasser, 47 Länder.

> „Die Mooring-Qualität weltweit variiert enorm. In Kroatien und Australien sind die Moorings erstklassig gewartet. In vielen karibischen Inseln sind die Bojen ein Glücksspiel — manche halten bei jedem Wetter, andere reißen bei 15 Knoten. Unser Grundsatz: immer einen eigenen Pennant mitführen, die Boje von außen kritisch beurteilen, und bei Zweifeln den eigenen Anker als Backup setzen. Wir haben uns nie auf eine Mooringboje allein verlassen."

**AYDI-Bewertung dieses Berichts:** Confidence: estimated (Einzelerfahrung, aber repräsentativ für Blauwasser-Praxis). Empfehlung übernommen: Eigenen Pennant immer mitführen.

### O2 — Charter-Skipper: Med-Mooring-Tipps

**Quelle:** Erfahrungsbericht Charter-Skipper (12 Jahre, >500 Med-Mooring-Manöver).

> „Die größten Fehler beim Med-Mooring: zu schnell, zu nervös, zu wenig Kommunikation mit der Crew. Mein Tipp: übe Rückwärtsfahren, bis es langweilig wird. Dann bist du bereit. Und: nimm immer die Hilfe des Marineros an. Die sind da, weil das Anlegen für Unerfahrene wirklich schwierig ist."

**AYDI-Bewertung:** Confidence: documented (professionelle Erfahrung). Kernaussage integriert in Troubleshooting und FAQ.

### O3 — Marina-Betreiber: Häufigste Mooring-Probleme (Umfrage 2024)

**Quelle:** Umfrage unter 45 Marina-Betreibern in Europa (ICOMIA Member Survey, Auszug).

**Top 10 Mooring-Probleme aus Sicht der Marina-Betreiber:**

| Rang | Problem | Häufigkeit (% der Befragten) | Confidence |
|------|---------|-------------------------------|------------|
| 1 | UV-Degradation von Lazy Lines | 89 % | documented |
| 2 | Propeller-Verwicklung in Muringleinen | 78 % | documented |
| 3 | Unerfahrene Skipper beim Med-Mooring | 73 % | documented |
| 4 | Korrosion an Schäkeln und Verbindern | 67 % | documented |
| 5 | Biofouling an Grundketten und Bojen | 62 % | documented |
| 6 | Kollisionen beim Anlegen/Ablegen | 58 % | documented |
| 7 | Überlastung bei Sturm (Bora, Meltemi) | 45 % | documented |
| 8 | Diebstahl/Vandalismus an Moorings | 35 % | documented |
| 9 | Sediment-Verlagerung (Grundanker-Drift) | 28 % | documented |
| 10 | Umweltauflagen (Seegras-Schutz) | 22 % | documented |

**Kosten-Analyse (Durchschnittswerte pro Marina/Jahr):**

| Kostenposition | Klein (<100 Plätze) | Mittel (100–300) | Groß (>300) | Confidence |
|---------------|--------------------|-----------------|--------------| ------------|
| Lazy-Line-Ersatz | 3.000 EUR | 8.000 EUR | 20.000 EUR | estimated |
| Taucher-Einsätze | 5.000 EUR | 12.000 EUR | 30.000 EUR | estimated |
| Schäkel/Verbinder-Ersatz | 1.500 EUR | 4.000 EUR | 10.000 EUR | estimated |
| Ketten-Reparatur/Ersatz | 2.000 EUR | 6.000 EUR | 15.000 EUR | estimated |
| Schadenregulierung (Haftung) | 5.000 EUR | 15.000 EUR | 40.000 EUR | estimated |
| **Gesamt** | **16.500 EUR** | **45.000 EUR** | **115.000 EUR** | estimated |

### O4 — Langfahrtsegler: Mooring in Entwicklungsländern

**Quelle:** Zusammenfassung aus 12 Langfahrt-Blogs und Cruiser-Forum-Beiträgen (2020–2025).

**Kernaussagen:**
- In vielen Entwicklungsländern gibt es keine regulierten Mooring-Felder
- Provisorische Moorings (Ölfässer, Reifen, Betonblöcke mit Drahtseil) sind üblich
- Vertrauen auf lokale Moorings ist riskant — immer eigenes Gerät als Backup verwenden
- Fischer-Moorings: oft für kleine Boote dimensioniert, für Yachten untauglich
- „Mooring-Boys": In einigen Häfen (z. B. Myanmar, Indonesien) bieten lokale Fischer Mooring-Service an — Qualität und Preis verhandeln

**AYDI-Empfehlung:** In Regionen ohne professionelle Mooring-Infrastruktur: (1) Immer eigenen Anker und Kette als Primärsicherung verwenden. (2) Lokale Moorings nur als Zusatzsicherung. (3) Tauch-Inspektion vor Nutzung unbekannter Moorings (Schnorchelausrüstung mitführen). (4) Nachtanker-Wache bei fragwürdigen Moorings.

---

## ANHANG P — Materialkunde Mooring-Systeme

### P1 — Ketten-Materialien für permanente Moorings

| Material | Korrosionsrate (mm/Jahr) | Bruchlast (Faktor) | Kosten (Faktor) | Lebensdauer (Jahre) | Confidence |
|----------|------------------------|---------------------|-----------------|---------------------|------------|
| Stahl (feuerverzinkt) | 0,05–0,15 | 1,0 (Basis) | 1,0 | 10–20 | documented |
| Stahl (kalt verzinkt) | 0,10–0,25 | 1,0 | 0,8 | 5–12 | documented |
| Edelstahl 316L | 0,01–0,03 | 0,85 | 3,5 | 30–50 | documented |
| Stahl (Duplex) | 0,01–0,02 | 1,2 | 5,0 | 40–60 | estimated |
| Gusseisen | 0,10–0,30 | 0,6 | 0,7 | 5–10 | documented |

### P2 — Bojen-Materialien im Vergleich

| Material | UV-Beständigkeit | Schlagfestigkeit | Temperaturbereich | Lebensdauer | Kosten (Faktor) | Confidence |
|----------|-----------------|-----------------|-------------------|-------------|-----------------|------------|
| LLDPE (Linear Low-Density PE) | ★★★★★ | ★★★★★ | −40 bis +60 °C | 8–15 Jahre | 1,0 | documented |
| HDPE (High-Density PE) | ★★★★☆ | ★★★★☆ | −30 bis +50 °C | 6–12 Jahre | 0,9 | documented |
| PVC (geschäumt) | ★★★☆☆ | ★★★☆☆ | −10 bis +50 °C | 4–8 Jahre | 0,7 | documented |
| Stahl (lackiert) | ★★☆☆☆ (Lack) | ★★★★★ | −50 bis +80 °C | 10–25 Jahre (mit Wartung) | 2,0 | documented |
| GFK (glasfaserverstärkt) | ★★★★★ | ★★★★☆ | −30 bis +60 °C | 15–25 Jahre | 2,5 | estimated |
| EVA-Schaum (gefüllt) | ★★★★☆ | ★★★★★ | −20 bis +50 °C | 8–15 Jahre | 1,5 | documented |

### P3 — Grundanker-Materialien

| Material | Korrosionsbeständigkeit | Gewicht/Volumen | Haltekraft/Gewicht | Kosten | Lebensdauer | Confidence |
|----------|------------------------|----------------|-------------------|--------|-------------|------------|
| Beton (Standard) | ★★★★★ (reagiert nicht) | 2.300 kg/m³ | 0,5–0,8 | ★★★★★ | 30–50 Jahre | documented |
| Beton (bewehrt) | ★★★★☆ (Bewehrung korrodiert) | 2.400 kg/m³ | 0,5–0,8 | ★★★★☆ | 25–40 Jahre | documented |
| Stahl (feuerverzinkt) | ★★★☆☆ | 7.850 kg/m³ | 0,5–0,8 (Kentledge) | ★★★☆☆ | 15–30 Jahre | documented |
| Gusseisen | ★★☆☆☆ | 7.200 kg/m³ | 0,5–0,8 | ★★★★☆ | 10–20 Jahre | documented |
| Edelstahl 316L (Helix) | ★★★★★ | — | 5–15 (geschraubt) | ★☆☆☆☆ | 30–50 Jahre | documented |

### P4 — Schamfilschutz-Materialien für Mooring-Leinen

| Material | Abriebfestigkeit | Flexibilität | UV-Beständigkeit | Kosten/m | Confidence |
|----------|-----------------|-------------|-----------------|---------|------------|
| PVC-Schlauch | ★★★☆☆ | ★★★☆☆ | ★★★☆☆ | 2–5 EUR | documented |
| Leder-Umwicklung | ★★★★★ | ★★★★☆ | ★★★☆☆ | 8–15 EUR | documented |
| Kevlar-Schlauch | ★★★★★ | ★★★★★ | ★★★★★ | 15–30 EUR | documented |
| Textil-Scheuerschutz (Dyneema) | ★★★★★ | ★★★★★ | ★★★★☆ | 10–20 EUR | documented |
| Spiralfeder (Edelstahl) | ★★★★★ | ★★☆☆☆ | ★★★★★ | 5–12 EUR | documented |
| Gummischlauch | ★★★★☆ | ★★★★★ | ★★☆☆☆ | 3–8 EUR | documented |

**AYDI-Empfehlung:** An jeder Stelle, wo eine Mooring-Leine über eine Kante läuft (Klüse, Reling, Steganker-Ring), muss ein Schamfilschutz angebracht sein. Kevlar- oder Dyneema-Schlauch für dauerhafte Moorings, PVC-Schlauch als Mindeststandard.

**Schamfil-Risikozonen am Mooring:**

| Zone | Reibungspartner | Risiko | Schutzmaßnahme | Confidence |
|------|----------------|--------|----------------|------------|
| Bugklüse | Metall/GFK-Kante | HOCH | Klüsenfutter (PE/Edelstahl), Schamfilschlauch auf Leine | documented |
| Reling-Durchführung | Edelstahl-Reling | MITTEL | Schlauchschutz oder Leder-Umwicklung | documented |
| Steg-Ring | Verzinkter Stahlring | HOCH | Karabiner statt direkter Leinenführung durch Ring | documented |
| Pfahl-Ring | Edelstahl/Eisen-Ring | HOCH | Schäkel + Wirbel, kein direkter Leinenkontakt am Ring | documented |
| Grundkette-Schäkel | Ketten-Glied auf Leine | SEHR HOCH | Kette-an-Kette-Verbindung, Thimble (Kausch) im Auge | documented |
| Boje-Auge | Metall-Auge in PE-Boje | MITTEL | Thimble (Kausch), regelmäßig prüfen | documented |
| Passerelle-Kontakt | Aluminium/Edelstahl | NIEDRIG | Gummipuffer an Passerelle-Fuß | documented |

### P4a — Thimble (Kausch) — unverzichtbar bei Mooring-Leinen

Eine Kausch (Thimble) ist ein tropfenförmiges Metallelement, das in das Auge einer gespleißten Leine eingelegt wird. Sie schützt die Leineninnenseite vor Schamfil durch den Schäkel oder Ring und erhöht die Lebensdauer des Auges um das 3–5-fache.

| Material | Für Leinendurchmesser (mm) | Kosten (EUR) | Lebensdauer | Confidence |
|----------|--------------------------|-------------|-------------|------------|
| Edelstahl 316L | 8–24 | 5–25 | 10+ Jahre | documented |
| Verzinkter Stahl | 8–24 | 3–15 | 3–8 Jahre | documented |
| Kunststoff (Nylon) | 8–18 | 2–8 | 2–5 Jahre | documented |

**AYDI-Empfehlung:** An allen Mooring-Leinen mit Augen IMMER Edelstahl-Kauschen verwenden. Kosten: minimal. Wirkung: erheblich.

### P5 — Pennant-Materialien im Vergleich

| Material | Bruchlast (bei Ø 18 mm, kN) | Dehnung bei WLL (%) | UV-Beständigkeit | Kosten/m (EUR) | Confidence |
|----------|----------------------------|---------------------|-----------------|---------------|------------|
| Nylon 3-karätiges | 40 | 15–25 | Mittel | 3–5 | documented |
| Nylon Double Braid | 55 | 12–18 | Mittel | 5–8 | documented |
| Polyester Double Braid | 50 | 5–10 | Hoch | 4–7 | documented |
| Polypropylen 3-karätiges | 25 | 10–15 | Gering | 2–3 | documented |
| HMPE (Dyneema) | 100+ | 2–4 | Hoch | 15–25 | documented |

**AYDI-Empfehlung für Pennant-Material:**
- **Standard (Swing-Mooring):** Nylon Double Braid — beste Kombination aus Dehnung (Stoßdämpfung) und Festigkeit
- **Standard (Med-Mooring/Lazy Line):** Polyester Double Braid — geringe Dehnung (präzises Positionieren), hohe UV-Beständigkeit
- **Premium:** HMPE mit Nylon-Snubber — höchste Festigkeit + externe Stoßdämpfung
- **Budget:** Polypropylen — nur temporär (1–2 Saisons), schwimmt (Propeller-Risiko)

### P6 — Korrosionsschutz-Verfahren für Mooring-Ketten

| Verfahren | Beschreibung | Schutzwirkung | Kosten (Faktor) | Lebensdauer des Schutzes | Confidence |
|-----------|-------------|--------------|-----------------|--------------------------|------------|
| Feuerverzinkung (hot-dip) | Zinkschicht durch Tauchen in flüssiges Zink | Sehr gut (60–100 µm Schicht) | 1,0 | 8–15 Jahre (Meerwasser) | documented |
| Kaltverzinkung (Spray) | Zinksprühbeschichtung | Mäßig (20–40 µm) | 0,6 | 3–8 Jahre | documented |
| Opfer-Anoden (Zink) | Zink-Anoden am Mooring-Geschirr | Gut (kathodischer Schutz) | 0,3 + jährlicher Ersatz | 1–2 Jahre pro Anode | documented |
| Kunststoff-Ummantelung (PE) | PE-Beschichtung über der Kette | Sehr gut | 2,0 | 10–20 Jahre | documented |
| Bitumen-Beschichtung | Bitumenöser Anstrich | Mäßig | 0,4 | 3–5 Jahre | estimated |
| Epoxy-Beschichtung | 2K-Epoxy-Lack auf Kette | Gut | 1,5 | 5–10 Jahre | documented |

### P7 — Opfer-Anoden-Dimensionierung für Mooring-Geschirr

| Mooring-Größe (LOA) | Anode-Typ | Anzahl | Position | Austausch-Intervall | Confidence |
|---------------------|-----------|--------|---------|---------------------|------------|
| 6–10 m | Zink-Knopf 0,5 kg | 2 | Schäkel oben + unten | 12 Monate | documented |
| 10–15 m | Zink-Knopf 1,0 kg | 3 | Schäkel + Ketten-Mitte | 12 Monate | documented |
| 15–20 m | Zink-Platte 2,0 kg | 3 | Schäkel + 2 × Kette | 12–18 Monate | documented |
| 20+ m | Zink-Platte 3,0 kg | 4+ | Gleichmäßig verteilt | 12 Monate | estimated |

**Wichtig:** In Marinas mit Landstrom-Anschluss ist galvanische Korrosion durch Streuströme ein ernstes Problem. Opfer-Anoden müssen häufiger geprüft werden (alle 6 Monate). Galvanische Isolatoren oder Trenntransformatoren an der Landstrom-Verbindung sind dringend empfohlen.

---

## ANHANG Q — Mooring im Seenotfall

### Q1 — Sturm am Mooring

| Sturmszenario | Maßnahme am Mooring | Maßnahme alternativ | Confidence |
|---------------|--------------------|--------------------|------------|
| Bft 8–9 (Starkwind) | Zusätzlichen Pennant befestigen, Chafe Guards anbringen | Wenn möglich: Hafen mit besserem Schutz anlaufen | documented |
| Bft 10–11 (Sturm) | Alle Leinen verdoppeln, Reitgewicht auf Pennant, Boot gesichert verlassen | Auf See gehen (wenn seetüchtig und erfahren) | documented |
| Bft 12+ (Orkan) | Mooring allein wird wahrscheinlich nicht halten | Auswassern, Hafen mit Sturmschutz, auf See gehen | documented |
| Hurrikan (Kat 1–2) | Spezial-Hurrikan-Mooring KANN halten | Auswassern, Mangroven-Mooring | documented |
| Hurrikan (Kat 3+) | Kein Mooring hält zuverlässig | Auswassern und verzurren, Zone verlassen | documented |

### Q2 — Notmooring — Improvisierte Lösungen

| Situation | Improvisierte Lösung | Haltekraft | Confidence |
|-----------|---------------------|-----------|------------|
| Kein Mooring, felsige Küste | Leine um Fels führen (Rundtörn + 2 halbe Schläge) | Abhängig vom Fels | documented |
| Kein Mooring, Mangroven | Leinen an mehrere Mangrovenstämme | Gut (verteilt Last) | documented |
| Boje, aber kein Pennant | Eigene Leine durch Bojen-Auge fädeln | = Leinenbruchlast | documented |
| Pfahl, aber kein Ring | Leine mehrfach um Pfahl wickeln (Pfahlstek) | Gut | documented |
| Zwei Anker als Fore-and-Aft | Buganker + Heckanker setzen | Gut (temporär) | documented |

### Q3 — Mooring bei Tsunamigefahr

**AYDI-Sicherheitshinweis:** Bei Tsunami-Warnung gelten andere Regeln als bei Sturm:

| Situation | Empfehlung | Begründung | Confidence |
|-----------|-----------|-----------|------------|
| Genügend Zeit zum Auslaufen (>2 h) | Auslaufen auf offenes Wasser (>100 m Tiefe) | Tsunami-Welle im Tiefwasser kaum spürbar | documented |
| Wenig Zeit (<2 h), Boot im Hafen | Alle Leinen lösen, Boot frei treiben lassen | Boot am Mooring wird von Welle gegen Steg/Kai gedrückt → Totalverlust | documented |
| Boot auf dem Trockenen | So hoch wie möglich lagern | Flutwelle kann >5 m erreichen | documented |

**Unterschied Tsunami vs. Sturm am Mooring:**
- Sturm: Mooring hält das Boot, Wind und Wellen sind die Bedrohung → Mooring verstärken
- Tsunami: Wasserspiegel steigt/fällt um Meter in Minuten → Mooring wird zur Todesfalle (Boot wird unter Wasser gezogen oder gegen Steg gedrückt)

### Q4 — Mooring-Evakuierung — Checkliste

**Wann muss das Mooring verlassen werden?**

| Warnsignal | Maßnahme | Dringlichkeit |
|-----------|----------|---------------|
| Wettervorhersage: >Bft 10 im Mooringbereich | Geschützteren Hafen anlaufen oder auswassern | 24–48 h vorher |
| Hurrikan-Warnung (Kat 2+) | Auswassern oder Hurrikan-Hole | 48–72 h vorher |
| Tsunami-Warnung | Auslaufen oder Leinen lösen | Sofort |
| Mooring versagt (Dragging, Bruch) | Eigenen Anker setzen oder Hafen anlaufen | Sofort |
| Nachbar-Mooring versagt | Eigenes Mooring prüfen, ggf. zusätzlich sichern | Sofort |

---

## ANHANG R — Zukunftstrends

### R1 — Technologische Entwicklungen

| Trend | Beschreibung | Zeithorizont | Wahrscheinlichkeit | Confidence |
|-------|-------------|-------------|-------------------|------------|
| Smartmooring | Lastsensoren, GPS-Tracker, Echtzeit-Überwachung | 2025–2030 | Hoch (Superyachten) | documented |
| Automatisches Anlegen | Roboter-gestützte Mooring-Systeme (Cavotec) | 2030+ | Mittel (nur kommerziell) | estimated |
| Recycling-Materialien | Mooring-Leinen aus recyceltem PET/HMPE | 2025–2028 | Hoch | documented |
| Bio-basierte Materialien | Mooring-Bojen aus Bio-Kunststoffen | 2028+ | Niedrig–Mittel | estimated |
| KI-gestützte Mooringplanung | Automatische Dimensionierung, Positionierung, Wartungsprognose | 2026–2030 | Hoch (AYDI!) | estimated |
| Drohnen-Inspektion | Unterwasser-Drohnen (ROV) für Mooring-Inspektion | 2025–2027 | Hoch | documented |

### R2 — Regulatorische Entwicklungen

| Trend | Region | Beschreibung | Zeithorizont | Confidence |
|-------|--------|-------------|-------------|------------|
| Eco-Mooring-Pflicht | EU (Mittelmeer) | Verpflichtende Eco-Moorings in Natura-2000-Gebieten | 2025–2030 | documented |
| Smartmooring-Standard | ICOMIA/ISO | Standardisierung von Mooring-Überwachungssystemen | 2028+ | estimated |
| Mooring-Inspektion Pflicht | EU-weit | Regelmäßige Pflichtinspektion aller permanenten Moorings | 2030+ | estimated |
| CO₂-Bilanz-Nachweis | EU | Lebenszyklus-Analyse für Marine-Infrastruktur | 2030+ | estimated |

### R3 — Marktentwicklung Mooring-Systeme

| Segment | Marktvolumen 2024 (geschätzt) | Wachstum (CAGR) | Treiber | Confidence |
|---------|-------------------------------|-----------------|---------|------------|
| Permanente Moorings (Freizeit) | 800 Mio. EUR (global) | 3–5 % | Wachsende Yacht-Flotte, Marina-Ausbau | estimated |
| Eco-Moorings | 120 Mio. EUR (global) | 12–18 % | Umweltregulierung, Seegras-Schutz | estimated |
| Smartmooring-Systeme | 30 Mio. EUR (global) | 25–35 % | Digitalisierung, Versicherungsanforderungen | estimated |
| Elastische Mooring-Systeme (Seaflex etc.) | 80 Mio. EUR (global) | 8–12 % | Umwelt, Komfort, Haltbarkeit | estimated |
| Marina-Infrastruktur (gesamt) | 5 Mrd. EUR (global) | 4–6 % | Globaler Tourismus, neue Marinas Asien/Mittlerer Osten | estimated |

**Regionale Schwerpunkte:**
- **Mittelmeer:** Größter Markt, getrieben durch Marina-Expansion in Kroatien, Griechenland, Montenegro
- **Australien/Neuseeland:** Eco-Mooring-Vorreiter, strengste Regulierung
- **Naher Osten:** Neue Superyacht-Marinas (Dubai, Saudi-Arabien, Oman)
- **Asien:** Aufstrebender Markt (Thailand, Malaysien, Indonesien)

### R4 — Nachhaltigkeit und Umwelt

| Trend | Beschreibung | Status | Confidence |
|-------|-------------|--------|------------|
| Seegras-Monitoring per Drohne | Unterwasser-Drohnen erfassen Seegras-Zustand rund um Moorings | Pilotprojekte (Balearen, GBR) | documented |
| Recycling-Ketten | Ketten aus recyceltem Stahl für Mooring-Anwendungen | Verfügbar, gleiche Qualität | documented |
| Bio-abbaubare Mooring-Leinen | Leinen, die sich nach Verlust im Meer zersetzen | Forschungsphase | estimated |
| Solarangetriebene Mooring-Bojen | Bojen mit LED-Beleuchtung und Sensor-Stromversorgung durch Solar | Pilotprojekte | documented |
| Zero-Impact-Marinas | Marinas mit vollständig ökologisch neutralem Mooring-System | Konzeptphase | estimated |
| Carbon-Offset für Moorings | CO₂-Kompensation für Mooring-Infrastruktur | Erste Anbieter (Skandinavien) | estimated |

### R5 — Materialinnovationen

| Innovation | Beschreibung | Vorteil | Verfügbarkeit | Confidence |
|-----------|-------------|---------|---------------|------------|
| HMPE-Grundketten | Synthetische Ketten aus HMPE statt Stahl | 80 % leichter, keine Korrosion | Prototyp (Offshore) | estimated |
| Graphen-beschichtete Ketten | Stahl-Ketten mit Graphen-Korrosionsschutz | 5× längere Lebensdauer | Forschungsphase | estimated |
| 3D-gedruckte Mooring-Hardware | Edelstahl-Schäkel und Wirbel aus 3D-Druck | Individuelle Formen, Gewichtsersparnis | Verfügbar (Spezialanfertigung) | documented |
| Self-healing Elastomere | Gummi-Pendants, die kleine Risse selbst reparieren | Längere Lebensdauer | Forschungsphase | estimated |
| Titan-Mooring-Hardware | Schäkel und Wirbel aus Titan | Korrosionsfrei, leicht | Nischenprodukt (Superyacht) | documented |

### R6 — Digitale Mooring-Verwaltung

| Feature | Beschreibung | Nutzer | Status | Confidence |
|---------|-------------|--------|--------|------------|
| Digital Twin | 3D-Modell des gesamten Mooring-Felds mit Echtzeit-Daten | Marina-Betreiber | Pilotprojekte | documented |
| Predictive Maintenance | KI-basierte Vorhersage von Kettenbruch basierend auf Lastdaten | Marina-Betreiber | Entwicklung | estimated |
| Mobile App (Eigner) | Echtzeit-Mooring-Last, Wetter, Alarm auf dem Smartphone | Yacht-Eigner | Verfügbar (einzelne Marinas) | documented |
| Blockchain-Wartungsbuch | Manipulationssichere Dokumentation aller Wartungen | Versicherungen | Konzeptphase | estimated |
| Automatische Bojen-Erkennung | KI erkennt Mooring-Bojen auf Luftbildern für Charting | Kartenherstellern | Pilotprojekt | estimated |

### R7 — AYDI-Integration: Geplante Features

| Feature | Beschreibung | Geplant für | Priorität |
|---------|-------------|-------------|-----------|
| Mooring-Dimensionierungsrechner | Automatische Berechnung aller Mooring-Komponenten basierend auf Yacht-Daten, Region und Wetterdaten | v3.0 | Hoch |
| Mooring-Zustandsbewertung (Foto) | Visuell-KI-basierte Bewertung von Pennant, Boje, Kette mittels Claude Vision API | v3.0 | Hoch |
| Mooring-Kostenrechner | Parametrische Kostenschätzung für neue Moorings (Komponenten + Installation + Wartung) | v3.5 | Mittel |
| Regionale Mooring-Empfehlung | Automatische Empfehlung basierend auf Region, Yacht-Typ und Wetter-Profil | v3.0 | Hoch |
| Med-Mooring-Trainer | Interaktive Simulation eines Stern-to-Anlegemanövers mit verschiedenen Wind-/Strömungsbedingungen | v3.5 | Niedrig |
| Smartmooring-Integration | Anbindung von Sensor-Daten in AYDI-Dashboard (API zu Mooring-Sensor-Herstellern) | v4.0 | Mittel |
| Schwojkreis-Visualisierung | 3D-Darstellung des Schwojkreises einer Yacht am Swing-Mooring | v3.5 | Niedrig |
| Mooring-Vergleichstool | Vergleich verschiedener Mooring-Konfigurationen (Kosten, Sicherheit, Umwelt) | v3.0 | Hoch |
| Wartungsplaner | Automatische Erinnerungen für Mooring-Inspektionen basierend auf Alter und Zustand | v3.5 | Mittel |
| Marina-Rating | Crowdsourced Bewertung der Mooring-Qualität in Marinas weltweit | v4.0 | Niedrig |

**Integration mit bestehenden AYDI-Modulen:**

| AYDI-Modul | Integration mit Mooring | Beschreibung |
|-----------|------------------------|-------------|
| Compliance | Mooring-Dimensionierung vs. CE-Kategorie | Yacht der Kategorie A muss stärkeres Mooring haben als Kategorie D |
| Structural | Klampen-Lastrücktragung | Mooring-Lasten müssen von Klampen ins Laminat rücktragbar sein |
| Cost | Mooring-Betriebskosten | Jährliche Mooring-Kosten als Teil der Betriebskostenanalyse |
| Materials | Korrosions-Risiko | Materialanalyse der Mooring-Beschläge und -Verbindungen |
| Service Patterns | Mooring-Wartungshistorie | Auswertung von Wartungsberichten für Mooring-Systeme |
| Market | Liegeplatz-Kosten regional | Mooring-Kosten als Faktor in der Marktbewertung |

---

## ANHANG S — Spezialthemen

### S1 — Mooring für Katamarane

**Katamarane stellen besondere Anforderungen an Mooring-Systeme:**

| Aspekt | Einrumpfer (Vergleich) | Katamaran | Konsequenz für Mooring |
|--------|----------------------|-----------|----------------------|
| Windangriffsfläche | Moderat | +30–50 % höher (breiter, höheres Brückendecks) | Stärkere Moorings erforderlich |
| Breite | ~30 % LOA | ~50 % LOA | Breitere Liegeplätze, breiterer Schwojkreis |
| Verdrängung/LOA | Hoch | Niedrig (leichter pro Meter) | Weniger Anlegeenergie, aber mehr Winddrift |
| Tiefgang | 1,5–2,5 m | 0,8–1,5 m | Flacheres Wasser möglich, aber Grundkette muss kürzer |
| Schwojverhalten | Pendeln | Stärkeres Pendeln (mehr Fläche) | Breiterer Bridle empfohlen |

**Dimensionierungs-Korrekturfaktoren:**
- Pennant-Durchmesser: LOA + 6 mm (statt LOA + 4 mm für Einrumpfer)
- Grundanker-Gewicht: ×1,5 des Einrumpfer-Werts gleicher LOA
- Schwojkreis: +20 % Radius wegen größerer Breite und Windangriffsfläche
- Bridle: Unbedingt empfohlen (breiter als bei Einrumpfer: 50–60° Winkel)

### S2 — Mooring für Superyachten (25 m+)

**Superyachten erfordern professionelles Mooring-Management:**

| Aspekt | Standard-Yacht | Superyacht | Confidence |
|--------|---------------|------------|------------|
| Liegegebühren/Nacht | 30–150 EUR | 500–10.000 EUR | documented |
| Mooring-Dimensionierung | Tabelle ausreichend | Individuelle Berechnung erforderlich | documented |
| Crew-Anforderungen | 1–2 Personen | 3–10 Personen, professionell | documented |
| Versicherungsanforderungen | Standard-Kasko | Spezial-Superyacht-Police mit Mooring-Klauseln | documented |
| Smartmooring | Optional | Zunehmend Standard | documented |
| Wartung | Eigner/Saisonarbeiter | Professionelles Yachtmanagement | documented |

**Spezial-Mooring-Infrastruktur für Superyachten:**

| Infrastruktur | Beschreibung | Verfügbar in | Kosten (EUR/Nacht, 30 m Yacht) | Confidence |
|---------------|-------------|-------------|-------------------------------|------------|
| Megayacht-Berth (Steg) | Schwimm-Steg mit extra breiten Fingern, Strom 3×400V | Monaco, Antibes, Porto Cervo | 1.000–5.000 | documented |
| Megayacht-Mooring (Boje) | Überdimensionierte Swing-Moorings mit Wachservice | BVI, St. Barths, Mykonos | 200–1.000 | documented |
| Megayacht-Pier (fest) | Fester Kai mit Versorgung, Sicherheit, Concierge | Monaco, Barcelona, Palma | 2.000–10.000 | documented |

### S3 — Mooring für historische Yachten und Holzboote

**Besondere Anforderungen:**

| Aspekt | Modernes GFK-Boot | Historisches Holzboot | Konsequenz |
|--------|-------------------|----------------------|-----------|
| Rumpf-Empfindlichkeit | Robust (Gelcoat) | Empfindlich (Lack, Planken) | Weichere Fender, kein harter Stegkontakt |
| Klampen-Belastbarkeit | Hohe Lastrücktragung (Laminat) | Geringere Belastbarkeit (Holzverbund) | Lasten verteilen, mehr Leinen mit weniger Einzellast |
| Gewicht | Leicht bis mittel | Schwer (Eiche, Teak, Blei) | Mooring für höhere Verdrängung dimensionieren |
| Wartungszustand (Unterwasser) | Antifouling Standard | Kupferbeschlag oder Antifouling, empfindlicher | Mooring-Kontaktpunkte regelmäßig prüfen |

### S4 — Winter-Mooring (Überwinterung im Wasser)

**Nicht alle Yachten werden zum Überwintern ausgewassert. In einigen Regionen bleiben Boote den Winter über im Wasser:**

| Region | Winter-Mooring üblich? | Hauptrisiko | Schutzmaßnahme | Confidence |
|--------|----------------------|------------|----------------|------------|
| Mittelmeer (Süd) | Ja | Winterstürme (Scirocco, Levante) | Mooring verstärken, Boot winterfest | documented |
| Mittelmeer (Nord) | Ja (aber gelegentlich Frost) | Frostschäden, Winterstürme | Frostwächter, Mooring-Überwachung | documented |
| Skandinavien | Nein (Eis!) | Eisgang zerstört Boot und Mooring | Auswassern Oktober/November | documented |
| UK (Süd) | Häufig | Winterstürme, Tidenhub + Sturm | Mooring für Bft 11+ dimensionieren | documented |
| UK (Nord) | Seltener | Eis (selten), Winterstürme | Auswassern empfohlen | documented |
| Karibik | Ja (ganzjährig) | Hurrikansaison | Zyklon-Vorbereitung | documented |
| Australien (Süd) | Ja | Winterstürme (Süd-Australien) | Standard-Mooring ausreichend | estimated |

**Winter-Mooring-Checkliste:**
- [ ] Mooring-Inspektion vor dem Winter (Kette, Schäkel, Pennant)
- [ ] Leinen verstärken (doppelte Pennants)
- [ ] Chafe Guards an allen Reibungspunkten
- [ ] Fender kontrollieren und ggf. ersetzen
- [ ] Borddurchlässe schließen (wo möglich)
- [ ] Bilgenpumpe funktionsfähig (mit Alarm)
- [ ] Batterieladung sicherstellen (Solar oder Landstrom)
- [ ] Abdeckplane/Persenning sichern
- [ ] Regelmäßige Kontrolle einplanen (alle 1–2 Wochen)
- [ ] Nachbarn/Hafenmeister informieren (Kontaktdaten hinterlassen)

---

## ANHANG Z — Referenzen und Quellenverzeichnis

### Z1 — Primärquellen

| Quelle | Art | Verwendung in dieser Datei |
|--------|-----|---------------------------|
| ISO 15084:2003 | Norm | Anforderungen an Festmacherpunkte |
| AS 3962:2001 | Norm | Marina-Design-Richtlinien (Australien) |
| BS 6349 | Norm | Hafenbauwerke (UK) |
| EN 14504:2006 | Norm | Binnenschifffahrt — Schwimmende Landestege und Brücken |
| PIANC Report 2016 | Richtlinie | Bewegungsgrenzen für geankerte Schiffe |
| Polyform Produktkatalog 2025/2026 | Katalog | Mooring-Bojen, Maße, Preise |
| Seaflex Technical Manual 2025 | Handbuch | Elastische Mooring-Systeme |
| Hazelett Marine Katalog 2025 | Katalog | Elastische Pendants, Mooring Whips |
| Mantus Marine Katalog 2025 | Katalog | Mooring-Hardware, Anker |
| Pantaenius Schadensstatistik 2019–2024 | Bericht | Schadensursachen und -häufigkeit |
| Crown Estate Annual Report 2024 | Bericht | Mooring-Regulierung UK |
| NSW RMS Mooring Guidelines 2023 | Richtlinie | Eco-Mooring-Anforderungen Australien |

### Z2 — Sekundärquellen

| Quelle | Art | Verwendung |
|--------|-----|-----------|
| Practical Sailor (diverse Ausgaben) | Zeitschrift | Mooring-Produkt-Tests |
| YACHT Magazin (diverse Ausgaben) | Zeitschrift | Med-Mooring-Anleitungen |
| Sailing Today (diverse Ausgaben) | Zeitschrift | UK-Mooring-Praxis |
| Nigel Calder: "Boatowner's Mechanical and Electrical Manual" | Buch | Mooring-Grundlagen |
| Tom Cunliffe: "The Complete Day Skipper" | Buch | Med-Mooring-Technik |
| Rod Heikell: "Mediterranean Cruising Handbook" | Buch | Mittelmeer-Mooring-Praxis |
| Beth Leonard: "The Voyager's Handbook" | Buch | Blauwasser-Mooring |
| Segeln-Forum.de (2020–2025) | Forum | Eigner-Erfahrungen |
| Boote-Forum.de (2020–2025) | Forum | Mooring-Diskussionen |
| Cruisers Forum (2020–2025) | Forum | Internationale Mooring-Erfahrungen |
| YachtForums.com (2020–2025) | Forum | Superyacht-Mooring |

### Z3 — AYDI-interne Referenzen

| Wissensdatei | Relation |
|-------------|----------|
| 13_01_anker_grundlagen.md | Ankertechnik (temporäres Ankern vs. permanentes Mooring) |
| 13_02_ankerketten.md | Kettenmaterial und -dimensionierung |
| 13_03_ankerwinden.md | Winsch-Einsatz beim Mooring-Aufnehmen |
| 13_05_festmacher_fender.md | Festmacherleinen und Fender (Einzelkomponenten) |
| 13_06_ankerbucht_bugbeschlaege.md | Bugrolle, Bugbeschläge für Mooring-Aufnahme |
| 11_01 – 11_05 | Klampen, Schienen, Reling (Befestigungspunkte für Mooring-Leinen) |
| 12_01 – 12_05 | Schäkel, Wirbel (Verbindungselemente im Mooring-System) |

---

*Ende der Wissensdatei 13_07 — Mooring-Systeme*
*AYDI Research — Version 1.0.0 — Stand: 2026-04-26*
*Nächste geplante Aktualisierung: 2026-10-26 (Halbjährlich)*

**Änderungshistorie:**

| Version | Datum | Autor | Änderung |
|---------|-------|-------|----------|
| 1.0.0 | 2026-04-26 | AYDI Research | Erstfassung — alle Abschnitte, 11 Fallstudien, 35 FAQ, 54 Glossar-Einträge, 12 Fehlerbilder, Pydantic v2 Modelle |

**Geplante Ergänzungen für v1.1:**
- Erweiterte Smartmooring-Datenintegration (API-Spezifikation)
- Zusätzliche Fallstudien: Asien, Naher Osten
- Detaillierte Lastberechnung für Fore-and-Aft-Moorings
- Erweiterte Katamaran-Korrekturmodelle
- Mooring-Simulation für AYDI Med-Mooring-Trainer
- ROV-Inspektionsprotokolle (automatisierte Unterwasser-Inspektion)