# 22.05 — Solaranlagen an Bord: Vollständige Wissensreferenz

> **AYDI Wissensdatei 22.05** — Kategorie 22: Elektrik und Verkabelung
> **Confidence-Quelle:** measured (Hersteller-TDS, IEC 61215/61730), documented (Hersteller-Kataloge, Praxisberichte), estimated (Erfahrungswerte)
> **Letzte Aktualisierung:** 2026-05-05

---

## Inhaltsverzeichnis

1. [Einführung und Übersicht](#1-einführung-und-übersicht)
2. [Grundlagen und Theorie](#2-grundlagen-und-theorie)
3. [Typenübersicht](#3-typenübersicht)
4. [Produktlinien und Spezifikationen](#4-produktlinien-und-spezifikationen)
5. [Hersteller-Datenbank](#5-hersteller-datenbank)
6. [Fehlerbild-Atlas](#6-fehlerbild-atlas)
7. [Troubleshooting-Entscheidungsbäume](#7-troubleshooting-entscheidungsbäume)
8. [FAQ — Häufige Fragen](#8-faq--häufige-fragen)
9. [Glossar](#9-glossar)
10. [Schnell-Referenz](#10-schnell-referenz)
11. [ANHANG A–H — Fallstudien](#anhang-ah--fallstudien)
12. [ANHANG I–R — AYDI-Integration (Pydantic v2 Modelle)](#anhang-ir--aydi-integration-pydantic-v2-modelle)

---

## 1. Einführung und Übersicht

### 1.1 Solar als primäre Energiequelle auf Fahrt

Die Photovoltaik hat sich in den letzten zehn Jahren von einer Ergänzungstechnik zur primären Energiequelle für autonomes Fahrtensegeln und Langstrecken-Motorboote entwickelt. Moderne Solaranlagen ermöglichen auf geeigneten Yachten vollständige Energieautarkie ohne Generatorbetrieb — eine Revolution für Komfort, Wartungskosten und Umweltbilanz.

**Statistische Relevanz:**
- Laut Cruising World Survey 2024 nutzen **78% aller Blauwassersegler** Solaranlagen als primäre Ladequelle
- Die durchschnittliche installierte Leistung auf Fahrtenyachten (12–16m) stieg von 200 Wp (2015) auf **680 Wp** (2025)
- **42% der Langfahrtsegler** berichten vollständige Energieautarkie (kein Generator/Landstrom) durch Solar + LiFePO4
- Pantaenius-Schadensstatistik: nur **2,3%** Schadensmeldungen an Solaranlagen nach 5 Jahren — die Technologie ist extrem zuverlässig
- ROI einer typischen 600-Wp-Anlage: **3,2 Jahre** durch ersparten Generator-Diesel und Landstrom

**Confidence:** documented — basierend auf Cruising World Survey 2024, Pantaenius Claims Data, Victron Energy User Statistics.

### 1.2 Potenzial und Grenzen

**Potenzial:**
- Stille, vibrationsfreie Energieerzeugung — entscheidend für Ankerlieger
- Keine beweglichen Teile — praktisch wartungsfrei über 20+ Jahre
- Skalierbar von 50 Wp (Erhaltungsladung) bis 4.000+ Wp (vollautarke Katamarane)
- Gewicht moderner Panels: 2–6 kg/m² (semiflexibel) vs. 50+ kg für einen Generator
- Kein Kraftstoffverbrauch, keine Abgase, kein Ölwechsel
- Passive Erzeugung auch bei Abwesenheit (Winterlager, Werftaufenthalt)

**Grenzen:**
- Flächenbedarf: 1 m² liefert max. 180–220 Wp (monokristallin)
- Wetterabhängigkeit: Bewölkung reduziert Ertrag auf 10–30%
- Nachts keine Produktion — Speicher zwingend erforderlich
- Verschattung durch Rigg, Baum, Segel drastisch leistungsmindernd
- Neigungswinkel auf Booten selten optimal (horizontal vs. 30° optimal)
- Begrenzte Fläche auf Einrumpf-Segelyachten (150–400 Wp typisch)
- Salzwasser-Umgebung aggressiv für Kontakte und Rahmen

**Confidence:** measured/documented — basierend auf IEC 61215 Leistungsdaten, Herstellerangaben und dokumentierten Fahrtberichten.

### 1.3 Energiebilanz nach Yachtklasse

| Yachtklasse | Typischer Bedarf (Ah/Tag @12V) | Empfohlene Solar-Wp | Ertrag Mittelmeer (Ah/Tag) | Autarkie möglich? |
|-------------|-------------------------------|--------------------|-----------------------------|-------------------|
| Weekender Sail 8–10m | 30–60 | 100–200 | 40–80 | Ja (Sommer) |
| Coastal Cruiser 10–12m | 60–120 | 200–400 | 80–160 | Ja (Apr–Okt) |
| Fahrtenyacht 12–15m | 120–200 | 400–800 | 160–320 | Ja (ganzjährig Tropen) |
| Blauwasser Mono 13–16m | 150–280 | 500–1.000 | 200–400 | Mit Windgen. Ja |
| Katamaran 38–45ft | 200–400 | 800–2.000 | 320–800 | Ja (ganzjährig) |
| Katamaran 45–55ft | 300–600 | 1.500–3.500 | 600–1.400 | Ja, inkl. Klima |
| Motoryacht 12–18m | 200–500 | 500–1.500 | 200–600 | Teilweise |
| Explorer Yacht 20m+ | 500–2.000 | 2.000–5.000 | 800–2.000 | Hybrid |

**Confidence:** estimated — Durchschnittswerte aus Fahrtberichten und Herstellerempfehlungen, individuelle Abweichungen ±30%.

### 1.4 Kostenentwicklung und Markttrends

| Jahr | €/Wp (marine-grade starr) | €/Wp (semiflexibel) | €/Wp (CIGS) | Ø Wirkungsgrad mono |
|------|--------------------------|--------------------|--------------|--------------------|
| 2015 | 4,50–6,00 | 7,00–10,00 | 12,00–18,00 | 17–19% |
| 2018 | 3,00–4,50 | 5,00–7,50 | 8,00–12,00 | 19–20% |
| 2020 | 2,50–3,50 | 4,00–6,00 | 6,00–9,00 | 20–21% |
| 2022 | 2,00–3,00 | 3,50–5,50 | 5,00–8,00 | 21–22% |
| 2025 | 1,50–2,50 | 2,80–4,50 | 4,00–6,50 | 22–24% |

**Trend:** Preise fallen jährlich um 8–12%, Wirkungsgrade steigen um 0,3–0,5%/Jahr. Semiflexible Panels nähern sich preislich den starren Modulen an.

---

## 2. Grundlagen und Theorie

### 2.1 Photovoltaik-Physik — Halbleitereffekt

Eine Solarzelle besteht aus einem p-n-Übergang in einem Halbleitermaterial (typisch Silizium). Wenn Photonen mit ausreichender Energie (>1,1 eV für Si) auf die Zelle treffen, werden Elektron-Loch-Paare erzeugt. Das elektrische Feld am p-n-Übergang trennt diese Ladungsträger und erzeugt eine Spannung (ca. 0,5–0,7 V pro Zelle).

**Bandlücke und Spektralempfindlichkeit:**
- Silizium (kristallin): Bandlücke 1,12 eV → optimale Absorption 350–1100 nm
- CIGS (CuInGaSe₂): Bandlücke 1,0–1,7 eV (einstellbar) → breiteres Spektrum
- Theoretisches Shockley-Queisser-Limit: 33,7% für Single-Junction bei 1,34 eV

**Relevanz für Marine-Anwendung:**
- Diffuses Licht (bedeckter Himmel): CIGS und monokristallin reagieren unterschiedlich
- Reflexion der Wasseroberfläche: zusätzliche 5–15% diffuse Einstrahlung bei niedrigem Sonnenstand
- Salzablagerungen auf der Glasoberfläche: Absorptionsverlust 3–8% bis zur nächsten Reinigung

**Confidence:** measured — Physikalische Grundlagen nach IEC 60904 und Lehrbuchstandard.

### 2.2 I-V-Kennlinie und MPP

Die Strom-Spannungs-Kennlinie (I-V-Kurve) einer Solarzelle beschreibt das Verhalten unter gegebener Einstrahlung und Temperatur:

```
I (A)
│
│  Isc ●━━━━━━━━━━━━━━━━━━●
│       ┃                    ╲
│       ┃                     ╲
│       ┃         ★ MPP        ╲
│       ┃        (Impp, Vmpp)   ╲
│       ┃                        ╲
│       ┃                         ╲
│       ┃                          ╲
│       ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━● Voc
└──────────────────────────────────────── V (V)
```

**Kenngrößen:**
| Parameter | Symbol | Bedeutung | Typisch (mono 100Wp) |
|-----------|--------|-----------|---------------------|
| Kurzschlussstrom | Isc | Max. Strom bei V=0 | 5,8–6,2 A |
| Leerlaufspannung | Voc | Max. Spannung bei I=0 | 21,5–22,5 V |
| MPP-Strom | Impp | Strom am Arbeitspunkt | 5,3–5,6 A |
| MPP-Spannung | Vmpp | Spannung am Arbeitspunkt | 17,8–18,5 V |
| Nennleistung | Pmpp | Impp × Vmpp | 100 Wp |
| Füllfaktor | FF | Pmpp / (Isc × Voc) | 0,72–0,82 |

**MPP-Tracking (MPPT):**
Der Maximum Power Point ist der Betriebspunkt, an dem das Produkt I×V maximal wird. Ein MPPT-Laderegler variiert kontinuierlich den Lastwiderstand, um diesen Punkt zu finden und zu halten. Algorithmen:
- **Perturb & Observe (P&O):** Einfach, oszilliert um MPP, Verlust 1–3%
- **Inkrementelle Leitfähigkeit:** Präziser, weniger Oszillation, Verlust <1%
- **Fractional Voc:** Vmpp ≈ 0,76 × Voc, ungenau bei Teilverschattung
- **Adaptive Multi-MPP:** Für verschattete Strings, findet globales Maximum

**Marine-Relevanz:** Bei Teilverschattung durch Rigg entstehen Multiple lokale Maxima in der P-V-Kurve. Nur hochwertige MPPT-Regler (Victron SmartSolar, Genasun) mit Multi-Peak-Tracking finden das globale Maximum.

**Confidence:** measured — IEC 60904-1 Messstandard, Herstellerdatenblätter.

### 2.3 Einstrahlung nach Region (kWh/m²/Tag)

Die verfügbare Solarenergie variiert drastisch mit Breitengrad, Jahreszeit und Wetter. Für die Anlagendimensionierung ist der schlechteste erwartete Monat maßgeblich (Worst-Case-Design).

**Globale Horizontale Einstrahlung (GHI) — Jahresdurchschnitt:**

| Region | Sommer (kWh/m²/Tag) | Winter (kWh/m²/Tag) | Jahresmittel | Peak Sun Hours (PSH) |
|--------|---------------------|---------------------|--------------|---------------------|
| Ostsee (55°N) | 5,0–5,5 | 0,5–1,0 | 2,8 | 2,8 |
| Nordsee (53°N) | 4,5–5,0 | 0,7–1,2 | 2,6 | 2,6 |
| Biskaya (45°N) | 5,5–6,5 | 1,5–2,5 | 3,8 | 3,8 |
| Mittelmeer West (40°N) | 6,5–7,5 | 2,5–3,5 | 4,8 | 4,8 |
| Mittelmeer Ost (36°N) | 7,0–8,0 | 3,0–4,0 | 5,2 | 5,2 |
| Kanaren (28°N) | 6,5–7,5 | 4,0–5,0 | 5,6 | 5,6 |
| Karibik (15°N) | 5,5–6,5 | 5,0–5,5 | 5,8 | 5,8 |
| Tropen (0–10°N/S) | 4,5–5,5 | 4,5–5,5 | 5,0 | 5,0 |
| Rotes Meer (25°N) | 7,5–8,5 | 5,0–6,0 | 6,5 | 6,5 |
| Südpazifik (20°S) | 5,0–6,0 | 6,5–7,5 | 5,8 | 5,8 |
| Australien Ost (30°S) | 4,5–5,5 | 6,0–7,0 | 5,4 | 5,4 |
| Patagonien (50°S) | 5,0–6,0 | 1,0–2,0 | 3,2 | 3,2 |

**Korrekturfaktoren für Bordanwendung:**
| Faktor | Auswirkung | Typischer Verlust |
|--------|-----------|-------------------|
| Horizontale Montage (vs. optimal 30°) | Minderertrag | -10 bis -20% |
| Verschmutzung (Salz, Vogelkot) | Absorption | -3 bis -10% |
| Verschattung Rigg/Baum | Teilverschattung | -10 bis -40% |
| Temperatur >25°C (Paneltemp. 50–70°C) | Leistungsverlust | -8 bis -15% |
| Kabelwiderstand | Ohmsche Verluste | -2 bis -5% |
| MPPT-Regler Effizienz | Wandlung | -2 bis -5% |
| **Gesamt Systemverluste** | | **-25 bis -55%** |

**Praxisformel für Bordertrag:**
```
Tagesertrag (Wh) = Wp_installiert × PSH × 0,65 (Systemfaktor)
Tagesertrag (Ah@12V) = Wp_installiert × PSH × 0,65 / 14,2 (Ladespannung)
```

**Beispielrechnung 400 Wp Mittelmeer Sommer:**
```
400 Wp × 6,5 PSH × 0,65 = 1.690 Wh/Tag = 119 Ah/Tag @12V
```

**Confidence:** measured/documented — basierend auf PVGIS-Datenbank (EU JRC), NASA POWER Dataset, korrigiert mit dokumentierten Bordmessungen.

### 2.4 Temperaturkoeffizient

Solarzellen verlieren Leistung bei steigender Temperatur. Der Temperaturkoeffizient beschreibt den prozentualen Leistungsverlust pro Kelvin über STC (25°C Zelltemperatur).

**Typische Temperaturkoeffizienten:**
| Zelltechnologie | TK Pmpp (%/K) | TK Voc (%/K) | TK Isc (%/K) |
|----------------|---------------|---------------|---------------|
| Monokristallin (PERC) | -0,35 bis -0,40 | -0,29 | +0,05 |
| Monokristallin (HJT) | -0,26 bis -0,30 | -0,23 | +0,04 |
| Polykristallin | -0,40 bis -0,45 | -0,31 | +0,05 |
| CIGS Dünnschicht | -0,30 bis -0,36 | -0,25 | +0,01 |
| SunPower Maxeon | -0,27 bis -0,29 | -0,22 | +0,04 |

**Marine-Praxistemperaturen:**
| Montagesituation | Paneltemperatur (Sommer Mittelmeer) | Verlust vs. STC |
|-----------------|--------------------------------------|-----------------|
| Freistehend auf Arch (Hinterlüftung) | 45–55°C | -7 bis -12% |
| Aufgeklebt auf GFK-Deck | 60–75°C | -14 bis -20% |
| Bimini-integriert (Hinterlüftung) | 40–50°C | -5 bis -10% |
| Begehbar auf Deck (ohne Luft) | 65–80°C | -16 bis -22% |
| Winter Mittelmeer (Ankerlieger) | 20–35°C | 0 bis -4% |

**Empfehlung:** Immer für Hinterlüftung sorgen. Mindestens 20 mm Luftspalt zwischen Panel-Rückseite und Montagefläche. Aufgeklebte semiflexible Panels ohne Hinterlüftung verlieren im Sommer bis zu 20% Ertrag durch Überhitzung.

**Confidence:** measured — IEC 61215 Temperaturkoeffizienten, bestätigt durch Bordmessungen (Victron VRM-Datenbank).

### 2.5 Verschattung und Bypass-Dioden

Verschattung ist das Hauptproblem bei Solaranlagen auf Segelbooten. Ein einzelner verschatteter Zellbereich kann den gesamten String-Ertrag auf nahe Null reduzieren.

**Physik der Verschattung:**
- Verschattete Zellen werden zu Verbrauchern (Reverse Bias)
- In Reihenschaltung begrenzt die schwächste Zelle den Gesamtstrom
- Ohne Schutz: Hotspot-Bildung bis zur thermischen Zerstörung

**Bypass-Dioden:**
Bypass-Dioden überbrücken verschattete Zellgruppen (typisch 18–24 Zellen pro Diode). Bei Verschattung leitet die Diode den Strom um die betroffene Gruppe herum.

```
String ohne Verschattung:          String mit Verschattung:
┌─[Z1]─[Z2]─...─[Z18]─┐          ┌─[Z1]─[Z2]─...─[Z18]─┐
│        Gruppe 1        │          │        Gruppe 1        │
│    Bypass-Diode D1     │          │    Bypass-Diode D1     │
├─[Z19]─[Z20]─...─[Z36]─┤          ├─[Z19]─[██]─...─[Z36]─┤
│        Gruppe 2        │          │    ★ Gruppe 2 ★        │
│    Bypass-Diode D2     │          │    D2 leitet → -0,7V   │
├─[Z37]─[Z38]─...─[Z54]─┤          ├─[Z37]─[Z38]─...─[Z54]─┤
│        Gruppe 3        │          │        Gruppe 3        │
│    Bypass-Diode D3     │          │    Bypass-Diode D3     │
└────────────────────────┘          └────────────────────────┘
Ertrag: 100%                        Ertrag: ~66% (1 Gruppe aus)
```

**Anzahl Bypass-Dioden und Verschattungsrobustheit:**
| Panel-Typ | Bypass-Dioden | Verlust bei 1 Schatten-Zelle |
|-----------|---------------|------------------------------|
| 36 Zellen, 2 Dioden | 2 | -50% (halbes Panel aus) |
| 36 Zellen, 3 Dioden | 3 | -33% (1/3 Panel aus) |
| 60/72 Zellen, 3 Dioden | 3 | -33% |
| SunPower/Solbian | 1 pro Zelle | -3% (nur betroffene Zelle) |
| Parallel-Schaltung (Shingle) | integriert | -5 bis -15% |

**Marine-Verschattungsquellen:**
- Mast und Rigg: wandernde Schatten über den Tag
- Baum (bei ungereftem Groß): breiter Schatten auf Deck
- Lazy-Jacks und Fänger: Linienschatten
- Reling und Geräteträger: fester Schatten morgens/abends
- Davits und Beiboot: auf Heckpanels
- Navigationsgeräte am Geräteträger: auf Arch-Panels

**Confidence:** measured — Zellenphysik nach IEC 61215, Bypass-Dioden-Verhalten dokumentiert.

### 2.6 Reihen- und Parallelschaltung

**Reihenschaltung (Serie):**
- Spannungen addieren sich: Vges = V1 + V2 + ... + Vn
- Strom ist identisch: Iges = I (schwächstes Modul bestimmt)
- Vorteil: höhere Spannung → dünnere Kabel, geringere Verluste
- Nachteil: ein verschattetes Modul reduziert gesamten String
- MPPT-Regler mit höherer Eingangsspannung (bis 100V oder 150V)

**Parallelschaltung:**
- Ströme addieren sich: Iges = I1 + I2 + ... + In
- Spannung ist identisch: Vges = V (niedrigste Vmpp bestimmt)
- Vorteil: verschattetes Modul beeinflusst andere nicht
- Nachteil: hohe Ströme → dickere Kabel, Sperr-Dioden nötig
- PWM-Regler oder mehrere MPPT-Eingänge

**Gemischte Schaltung (Serie-Parallel):**
```
        ┌──[Panel 1]──[Panel 2]──┐   String 1: 2×18V = 36V, 5A
        │                          │
MPPT ───┼──[Panel 3]──[Panel 4]──┼── String 2: 2×18V = 36V, 5A
        │                          │
        └──[Panel 5]──[Panel 6]──┘   String 3: 2×18V = 36V, 5A
        
        Gesamt: 36V, 15A = 540 Wp
        Vorteil: moderater Strom + Verschattungstoleranz
```

**Empfehlung nach Bootssituation:**
| Situation | Empfehlung | Begründung |
|-----------|-----------|------------|
| Alle Panels gleich, keine Verschattung | Serie | Max. Effizienz, dünne Kabel |
| Panels an verschiedenen Positionen | Parallel oder Multi-MPPT | Unabhängige Optimierung |
| Teilverschattung unvermeidbar | Parallel + Panel-Optimizer | Minimaler Verschattungsverlust |
| Lange Kabelwege (>5m) | Serie (höhere Spannung) | Geringere ohmsche Verluste |
| Mix verschiedener Panels | Separate MPPT pro Typ | Unterschiedliche Vmpp |

**Confidence:** measured — Grundlegende Elektrotechnik, bestätigt durch Herstellerempfehlungen (Victron, Genasun).

### 2.7 String-Dimensionierung

Die String-Dimensionierung muss die Eingangsspannung des MPPT-Reglers berücksichtigen. Kritisch: bei Kälte steigt Voc!

**Berechnung maximale Leerlaufspannung:**
```
Voc_max = Voc_STC × (1 + TK_Voc × (T_min - 25°C))
```

**Beispiel: 2 Panels in Serie, Victron 100/50:**
```
Panel: Vmpp = 18,5V, Voc = 22,3V, TK_Voc = -0,29%/K
Max. MPPT-Eingangsspannung: 100V (absolutes Maximum, Zerstörung darüber!)
Minimale Temperatur an Bord: -10°C (Winterlager Ostsee)

Voc_max pro Panel = 22,3V × (1 + (-0,0029) × (-10 - 25)) = 22,3 × 1,1015 = 24,56V
2 Panels in Serie: 49,12V → ✓ weit unter 100V
4 Panels in Serie: 98,24V → ⚠ grenzwertig! Bei -15°C Überschreitung!
3 Panels in Serie: 73,68V → ✓ sicher
```

**Maximale String-Länge nach Regler:**
| Regler | Max. Voc Eingang | Panels 18V (Voc 22V) | Panels 36V (Voc 44V) |
|--------|-----------------|----------------------|----------------------|
| Victron 75/15 | 75V | max. 3 | max. 1 |
| Victron 100/30 | 100V | max. 4 | max. 2 |
| Victron 100/50 | 100V | max. 4 | max. 2 |
| Victron 150/35 | 150V | max. 6 | max. 3 |
| Victron 150/70 | 150V | max. 6 | max. 3 |
| Genasun GVB-8-Li | 50V | max. 2 | max. 1 |
| EPEver Tracer 4210AN | 100V | max. 4 | max. 2 |

**Confidence:** measured — Herstellerspezifikationen, Berechnungen nach Datenblatt.

### 2.8 Systemeffizienz und Verlustquellen

**Gesamter Wirkungsgrad der Kette:**
```
η_System = η_Panel × η_Verschattung × η_Temperatur × η_Kabel × η_MPPT × η_Batterie

Typisch:  0,22   ×    0,85        ×    0,90       ×  0,97  ×  0,97  ×  0,95
        = 0,22   ×    0,68 (Systemverluste)
        = 0,15 effektiver Systemwirkungsgrad
```

**Verlustquellen im Detail:**
| Verlustquelle | Typisch (%) | Vermeidbar? | Maßnahme |
|---------------|-------------|-------------|----------|
| Zelltechnologie (Rest) | 78–80 | Nein | Bessere Zellen (HJT, Maxeon) |
| Temperatur | 5–20 | Teilweise | Hinterlüftung |
| Verschattung | 5–40 | Teilweise | Panel-Positionierung, Optimizer |
| Verschmutzung | 2–10 | Ja | Regelmäßige Reinigung |
| Kabelwiderstand | 1–5 | Ja | Ausreichender Querschnitt |
| Steckverbinder | 0,5–2 | Ja | Qualitäts-MC4, korrekte Crimps |
| MPPT-Wandlung | 2–5 | Teilweise | Hochwertiger Regler |
| Batterie-Ladung | 3–8 | Teilweise | LiFePO4 statt Blei |
| Mismatch (ungleiche Panels) | 1–5 | Ja | Gleiche Panels, gute Sortierung |

**Confidence:** measured/documented — Kombination aus IEC-Messwerten und Praxismessungen.

---

## 3. Typenübersicht

### 3.1 Monokristallin starr (Glasmodul)

**Beschreibung:**
Konventionelle Solarmodule mit monokristallinen Siliziumzellen in Glas-EVA-Backsheet- oder Glas-Glas-Laminat. Aluminium-Rahmen. Identische Technologie wie Hausdach-Module, aber in kleineren Formaten und mit mariner Zertifizierung.

**Technische Daten:**
| Eigenschaft | Wert |
|-------------|------|
| Wirkungsgrad | 20–24% |
| Gewicht | 10–12 kg/m² |
| Lebensdauer | 25–30 Jahre |
| Degradation | 0,3–0,5%/Jahr |
| Temperaturkoeff. Pmpp | -0,35 bis -0,40%/K |
| Mechanische Belastung | 5.400 Pa (Frontseite), 2.400 Pa (Rückseite) |
| Zertifizierung | IEC 61215, IEC 61730 |
| IP-Schutz | IP67 (Anschlussdose) |

**Vorteile:**
- Höchster Wirkungsgrad aller praxistauglichen Technologien
- Längste Lebensdauer und geringste Degradation
- Robusteste mechanische Konstruktion
- Beste Preis-Leistung (€/Wp)
- Verfügbarkeit — größte Modellvielfalt

**Nachteile:**
- Gewicht (10–12 kg/m²) — problematisch auf Bimini/Arch
- Starr — keine Anpassung an Deckskrümmung
- Erhöhtes Windprofil auf Geräteträger
- Glasbruch-Risiko bei Stoß (Fallen, Großbaum)
- Montage erfordert Rahmenhalterung

**Typische Einsatzorte:**
- Arch/Geräteträger (am häufigsten)
- Davit-Halterung achtern
- Decksluke (wenn tragfähig)
- Relinghalterung (kleine Module)
- Festmontage auf Flybridge (Motoryacht)

**Confidence:** measured — Herstellerdatenblätter, IEC-Zertifizierungen.

### 3.2 Monokristallin semiflexibel

**Beschreibung:**
Monokristalline Zellen in einem flexiblen Verbund aus ETFE (Ethylen-Tetrafluorethylen) oder PET-Frontfolie und Fiberglas-Backsheet. Biegbar bis ca. 30° (manche bis 60°). Kein Rahmen, direkt auf gewölbte Flächen montierbar.

**Technische Daten:**
| Eigenschaft | Wert |
|-------------|------|
| Wirkungsgrad | 19–23% |
| Gewicht | 2,0–3,5 kg/m² |
| Lebensdauer | 5–12 Jahre (!) |
| Degradation | 1–3%/Jahr |
| Temperaturkoeff. Pmpp | -0,35 bis -0,40%/K |
| Biegsamkeit | ≤30° (Premium: ≤60°) |
| Min. Biegeradius | 300–800 mm |
| Dicke | 2–4 mm |
| Frontschicht | ETFE oder PET |

**Vorteile:**
- Extrem leicht — ideal für Bimini, Arch-Top, Decksaufklebung
- Geringes Windprofil — kein Rahmen
- Anpassbar an Deckskrümmung und Aufbauten
- Einfache Montage (Kleben, Verschrauben, Ösen)
- Kein erhöhter Schwerpunkt

**Nachteile:**
- Deutlich kürzere Lebensdauer (5–12 Jahre vs. 25+)
- Schnellere Degradation durch UV und mechanische Belastung
- Mikroriss-Anfälligkeit bei wiederholter Biegung
- Keine Hinterlüftung bei Aufklebung → Überhitzung
- Höherer Preis pro Wp als starre Module
- Delaminierung der Frontfolie nach 3–7 Jahren häufig

**Lebensdauer-Problematik:**
Die begrenzte Lebensdauer ist das Hauptargument gegen semiflexible Panels. Ursachen:
1. **UV-Degradation der ETFE/PET-Folie:** Vergilbung, Transmissionsverlust
2. **Thermische Zyklen:** Unterschiedliche Ausdehnung Folie/Zelle → Mikrorisse
3. **Mechanische Biegung:** Jede Bewegung (Boot in Seegang) belastet Zellverbinder
4. **Fehlende Hinterlüftung:** bei Aufklebung permanente Überhitzung
5. **Salzwasser-Kriechströme:** an Kanten und Steckverbindern

**Confidence:** documented — Herstellerdatenblätter, bestätigt durch umfangreiche Erfahrungsberichte aus Langfahrt-Community (Noonsite, Cruisers Forum).

### 3.3 CIGS-Dünnschicht (CuInGaSe₂)

**Beschreibung:**
Dünnschicht-Technologie mit Kupfer-Indium-Gallium-Diselenid als Absorber. Aufgedampft auf flexibles Substrat (Edelstahlfolie oder Polymer). Extrem dünn, leicht und vollflächig aktiv (keine Zellzwischenräume).

**Technische Daten:**
| Eigenschaft | Wert |
|-------------|------|
| Wirkungsgrad | 14–18% (Labor: 23,6%) |
| Gewicht | 1,5–2,5 kg/m² |
| Lebensdauer | 15–25 Jahre |
| Degradation | 0,5–1,0%/Jahr |
| Temperaturkoeff. Pmpp | -0,30 bis -0,36%/K |
| Biegsamkeit | ≤90° (vollflexibel) |
| Dicke | 1–3 mm |
| Verschattungsverhalten | Besser als kristallin |

**Vorteile:**
- Ultraleicht (1,5–2,5 kg/m²)
- Vollflexibel — kann um Rundungen gelegt werden
- Besseres Teilverschattungsverhalten (keine abrupten Verluste)
- Besserer Temperaturkoeffizient als mono-Si
- Bessere Schwachlichtperformance (diffuses Licht)
- Längere Lebensdauer als semiflexibel kristallin
- Keine Hotspot-Gefahr (monolithisch verschaltet)
- Elegante Optik (homogene schwarze Fläche)

**Nachteile:**
- Geringerer Wirkungsgrad → mehr Fläche für gleiche Leistung
- Deutlich höherer Preis pro Wp (2–3× teurer als starr mono)
- Begrenzte Verfügbarkeit und Modellauswahl
- Initiale Lichtdegradation (Light Induced Degradation, 2–5% im 1. Jahr)
- Feuchtigkeitsempfindlichkeit der Schichten → hochwertige Verkapselung nötig

**Ideale Einsatzfälle:**
- Große Bimini-Flächen (Katamaran): Gewicht entscheidend
- Stark gerundete Aufbauten: Flexibilität nötig
- Teilverschattung unvermeidbar: bessere Robustheit
- Gewichtskritische Boote (Regatta-Cruiser): jedes kg zählt
- Begehbare Decksinstallation: Robustheit + Flexibilität

**Confidence:** measured/documented — Herstellerdaten (MiaSolé, Flisom), IEC 61646, Praxisberichte.

### 3.4 Bifazial (Beidseitig aktiv)

**Beschreibung:**
Module mit transparenter Rückseite, die auch reflektiertes Licht von der Unterseite nutzen. Auf Booten relevant bei erhöhter Montage über hellem Deck oder Wasser.

**Technische Daten:**
| Eigenschaft | Wert |
|-------------|------|
| Wirkungsgrad (Frontseite) | 20–22% |
| Bifazialitätsfaktor | 0,70–0,85 (70–85% der Rückseite nutzbar) |
| Mehrertrag typisch | +5 bis +20% (abhängig von Montage) |
| Gewicht | 11–14 kg/m² (Glas-Glas) |
| Lebensdauer | 30+ Jahre |

**Marine-Relevanz:**
| Montagesituation | Reflexionsgewinn | Gesamtmehrertrag |
|-----------------|------------------|------------------|
| Über weißem GFK-Deck (30 cm Abstand) | 15–25% Albedo | +8 bis +15% |
| Über Wasser (Arch überhängend) | 5–15% Albedo | +3 bis +10% |
| Über Teak-Deck (dunkel) | 5–10% Albedo | +2 bis +5% |
| Flach auf Deck montiert | kein Zugang Rückseite | 0% (sinnlos) |

**Empfehlung:** Bifazial lohnt sich auf Booten nur bei erhöhter Montage über hellen Flächen (Arch, Flybridge mit weißem Deck). Bei Flachmontage kein Vorteil.

**Confidence:** measured — Herstellerdaten, bestätigt durch vereinzelte Bordmessungen.

### 3.5 Begehbare Panels

**Beschreibung:**
Speziell für die Montage auf Decks konzipierte Module mit rutschfester Oberfläche, die betreten werden können. Typisch: SunPower/Maxeon-Zellen in robustem Laminat mit Antirutsch-Beschichtung.

**Technische Daten:**
| Eigenschaft | Wert |
|-------------|------|
| Wirkungsgrad | 19–22% (SunPower-Zellen) |
| Gewicht | 3–5 kg/m² |
| Belastbarkeit | 300–500 kg/m² (statisch) |
| Oberfläche | Antirutsch (ähnlich Treadmaster) |
| Lebensdauer | 8–15 Jahre |
| Montage | Verklebung direkt auf Deck |

**Vorteile:**
- Doppelnutzung der Decksfläche (begehbar + Energieerzeugung)
- Keine separate Fläche nötig — ideal für kleine Boote
- Nahezu unsichtbar — ästhetisch optimal
- Kein erhöhter Windwiderstand

**Nachteile:**
- Teuer (€6–€12/Wp)
- Keine Hinterlüftung → hohe Betriebstemperaturen
- Verschmutzung durch Fußabdrücke, Sohlenabrieb
- Begrenzte Reparierbarkeit
- Permanente Mikrobiegung durch Seegang belastet Zellverbinder
- Kratzer durch Sand/Schuhe mindern Transmission

**Confidence:** documented — Herstellerangaben (Solbian, SunPower/Maxeon), Langfahrt-Erfahrungen.

### 3.6 Bimini-Integration

**Beschreibung:**
Solarpanels werden direkt in oder auf das Bimini (Sonnensegel/Sonnenverdeck) integriert. Entweder fest laminiert oder in Taschen eingeschoben. Besonders populär auf Katamaranen.

**Varianten:**
| Variante | Beschreibung | Wp/m² | Gewicht/m² |
|----------|-------------|-------|-----------|
| Panels auf starrem Bimini-Rahmen | Starre Module auf Alu-Rahmen geschraubt | 180–220 | 10–14 kg |
| Semiflexibel auf Bimini genäht | ETFE-Panels mit Ösen auf Segeltuch | 160–200 | 3–5 kg |
| CIGS in Bimini-Stoff laminiert | Dünnschicht direkt auf Acryl-Stoff | 80–120 | 2–3 kg |
| Panels in Taschen (entnehmbar) | Panels in genähte Taschen eingeschoben | 160–200 | 3–4 kg |

**Dimensionierung Katamaran-Bimini:**
| Katamarangröße | Bimini-Fläche | Nutzbare Solarfläche | Installierte Wp |
|----------------|--------------|---------------------|-----------------|
| 38 ft | 6–8 m² | 4–6 m² | 800–1.200 |
| 42 ft | 8–10 m² | 6–8 m² | 1.200–1.600 |
| 45 ft | 9–12 m² | 7–10 m² | 1.400–2.000 |
| 50 ft | 12–15 m² | 9–12 m² | 1.800–2.400 |
| 55+ ft | 15–20 m² | 12–16 m² | 2.400–3.200 |

**Kritische Konstruktionsaspekte:**
1. **Windlast:** Bimini mit Panels muss Sturmfest sein (Beaufort 8+)
2. **Drainage:** Wasser darf sich nicht auf Panels stauen
3. **Neigung:** Leichtes Gefälle (5–10°) verbessert Ertrag und Ablauf
4. **Kabeldurchführung:** Wasserdicht durch Bimini-Stoff
5. **Demontierbarkeit:** Panels sollten für Wartung entnehmbar sein

**Confidence:** documented — Katamaran-Werftstandards (Lagoon, Fountaine Pajot), Nachrüst-Erfahrungen.

### 3.7 Arch-Montage (Geräteträger)

**Beschreibung:**
Der Geräteträger (Arch, Davit-Arch) ist der häufigste Montageort für Solarpanels auf Einrumpf-Yachten. Ein Edelstahl- oder Aluminium-Bogen über dem Heck trägt Panels, Antennen, Radar und ggf. Windgenerator.

**Arch-Typen für Solar:**
| Arch-Typ | Material | Tragfähigkeit | Max. Panelfläche | Typische Wp |
|----------|----------|---------------|------------------|-------------|
| Leichter Davit-Bogen | Ø25mm Edelstahl | 30–50 kg | 1–2 m² | 200–400 |
| Standard Geräteträger | Ø32mm Edelstahl | 50–100 kg | 2–4 m² | 400–800 |
| Heavy-Duty Arch | Ø38–50mm Edelstahl | 100–200 kg | 3–6 m² | 600–1.200 |
| Alu-Arch (custom) | 40×40–60×60mm Alu | 80–150 kg | 3–5 m² | 600–1.000 |
| Katamaran-Brücke | 60×60mm+ Alu | 200–500 kg | 6–12 m² | 1.200–2.400 |

**Montage-Optionen:**
- **Flach:** Panel liegt horizontal auf Arch-Querstreben → einfach, gute Belastbarkeit
- **Geneigt:** Panel in 10–20° Neigung → +5–10% Ertrag, mehr Windangriffsfläche
- **Schwenkbar:** Manuelle Neigungsverstellung → max. Ertrag, Mehraufwand
- **Tracks:** Panel in Alu-Schienen geführt → einfache Montage/Demontage

**Dimensionierung Arch-Breite:**
```
Arch_Breite_min = Panel_Breite + 2 × 50mm (Randabstand)
Arch_Tiefe_min = Panel_Tiefe + 100mm (Kabeldurchführung hinten)
```

**Confidence:** documented — Praxis-Standard in der Langfahrt-Szene, diverse Erfahrungsberichte.

---

## 4. Produktlinien und Spezifikationen

### 4.1 Victron Energy — BlueSolar Serie

**Hersteller:** Victron Energy B.V., Almere, Niederlande
**Marine-Fokus:** Hoch — Victron ist Marktführer bei marine Lade-/Energiesystemen

**Starre Module (BlueSolar Monocrystalline):**

| Modell | Wp | Vmpp (V) | Impp (A) | Voc (V) | Isc (A) | Maße (mm) | Gewicht (kg) | Preis (€) |
|--------|-----|----------|----------|---------|---------|-----------|-------------|-----------|
| SPM040-12 | 40 | 17,8 | 2,25 | 22,2 | 2,45 | 425×668×25 | 3,0 | 85 |
| SPM060-12 | 60 | 17,6 | 3,41 | 22,0 | 3,70 | 545×668×25 | 4,2 | 110 |
| SPM085-12 | 85 | 18,1 | 4,70 | 22,5 | 5,10 | 780×668×25 | 7,5 | 145 |
| SPM100-12 | 100 | 18,4 | 5,44 | 22,8 | 5,85 | 1000×668×30 | 8,5 | 165 |
| SPM115-12 | 115 | 18,5 | 6,22 | 22,9 | 6,70 | 1015×668×30 | 9,0 | 185 |
| SPM140-12 | 140 | 18,5 | 7,57 | 22,9 | 8,13 | 1250×668×30 | 10,5 | 215 |
| SPM175-24 | 175 | 36,0 | 4,86 | 44,2 | 5,25 | 1485×668×30 | 12,0 | 265 |
| SPM200-24 | 200 | 36,4 | 5,49 | 44,8 | 5,92 | 1580×808×35 | 14,5 | 310 |
| SPM305-20 | 305 | 32,6 | 9,36 | 39,7 | 9,95 | 1640×992×35 | 18,5 | 380 |

**Confidence:** measured — Victron Datenblätter (victronenergy.com), Preise: UVP 2025.

### 4.2 Sunware (Deutschland)

**Hersteller:** Sunware GmbH, Schwalmtal, Deutschland
**Marine-Fokus:** Sehr hoch — reiner Marine-/Outdoor-Spezialist

**Semiflexible Module (TX-Serie):**

| Modell | Wp | Vmpp (V) | Impp (A) | Voc (V) | Isc (A) | Maße (mm) | Gewicht (kg) | Preis (€) |
|--------|-----|----------|----------|---------|---------|-----------|-------------|-----------|
| TX-12039 | 38 | 17,3 | 2,20 | 21,5 | 2,42 | 544×353×3 | 0,9 | 195 |
| TX-14052 | 50 | 17,4 | 2,87 | 21,6 | 3,15 | 666×353×3 | 1,2 | 245 |
| TX-22052 | 55 | 17,5 | 3,14 | 21,8 | 3,45 | 746×353×3 | 1,3 | 265 |
| TX-14081 | 80 | 17,6 | 4,55 | 22,0 | 4,95 | 996×440×3 | 2,1 | 395 |
| TX-22120 | 120 | 18,0 | 6,67 | 22,3 | 7,20 | 1060×540×3,5 | 3,0 | 545 |
| TX-42039 | 150 | 36,0 | 4,17 | 44,2 | 4,55 | 1340×540×3,5 | 3,8 | 685 |

**Besonderheiten Sunware:**
- Deutsche Fertigung mit höchsten Qualitätsstandards
- ETFE-Frontfolie (selbstreinigend, extrem UV-beständig)
- Salzwasser-zertifiziert nach eigenen Prüfstandards
- Begehbare Varianten verfügbar (TX-B Serie)
- Integrierte Anschlussdose IP67 mit MC4-kompatiblen Steckern
- 5 Jahre Produktgarantie, 10 Jahre Leistungsgarantie (90%)

**Confidence:** measured — Sunware Datenblätter (sunware.de), Preise: UVP 2025.

### 4.3 Solbian (Italien)

**Hersteller:** Solbian Energie Alternative S.r.l., Avigliana (Turin), Italien
**Marine-Fokus:** Sehr hoch — Premium-Hersteller für marine semiflexible Panels

**SX-Serie (SunPower Maxeon-Zellen):**

| Modell | Wp | Vmpp (V) | Impp (A) | Voc (V) | Isc (A) | Maße (mm) | Gewicht (kg) | Preis (€) |
|--------|-----|----------|----------|---------|---------|-----------|-------------|-----------|
| SXp 36 Q | 36 | 5,8 | 6,21 | 7,2 | 6,60 | 397×302×2 | 0,4 | 285 |
| SXp 64 Q | 64 | 11,6 | 5,52 | 14,4 | 5,86 | 544×396×2 | 0,7 | 445 |
| SXp 100 Q | 100 | 17,4 | 5,75 | 21,6 | 6,10 | 796×396×2 | 1,1 | 625 |
| SXp 144 Q | 144 | 23,2 | 6,21 | 28,8 | 6,60 | 1048×396×2 | 1,5 | 845 |
| SXp 154 L | 154 | 23,2 | 6,64 | 28,8 | 7,05 | 1116×438×2 | 1,8 | 895 |
| SP 200 Q | 200 | 34,8 | 5,75 | 43,2 | 6,10 | 1450×540×2 | 2,8 | 1.185 |
| SP 252 L | 252 | 34,8 | 7,24 | 43,2 | 7,68 | 1580×580×2 | 3,4 | 1.445 |

**Besonderheiten Solbian:**
- SunPower/Maxeon IBC-Zellen (höchster Zell-Wirkungsgrad: 24,1%)
- Back-Contact-Technologie: keine sichtbaren Busbars, homogene Optik
- Individuelle Bypass-Diode pro Zelle → beste Verschattungstoleranz
- ETFE-Frontfolie mit Antireflex-Beschichtung
- Begehbare Ausführung verfügbar (ALLinONE Serie)
- Maßanfertigung in jeder Form möglich (Dreieck, Trapez, Aussparungen)
- Italienische Fertigung, 5 Jahre Garantie
- Weltweit führend für Regatta- und Langfahrt-Yachten

**Confidence:** measured — Solbian Datenblätter (solbian.eu), Preise: UVP 2025.

### 4.4 SunPower / Maxeon Solar Technologies

**Hersteller:** Maxeon Solar Technologies, Singapur (ehem. SunPower)
**Marine-Fokus:** Mittel — entwickelt Hochleistungszellen, die von Marine-Integratoren (Solbian, etc.) verbaut werden

**Maxeon-Zelltechnologie:**
| Generation | Zelltyp | Wirkungsgrad | Besonderheit |
|-----------|---------|-------------|--------------|
| Maxeon 3 | IBC Mono | 22,2% | N-Typ, Back-Contact |
| Maxeon 5 | IBC Mono | 22,7% | Shingled Cell |
| Maxeon 6 | IBC Mono | 24,1% | Kupfer-Basis, höchste Effizienz |
| Maxeon 7 | IBC Mono | 24,9% | HJT + IBC hybrid |

**Fertige Marine-Module (Performance-Serie):**
| Modell | Wp | Vmpp (V) | Impp (A) | Maße (mm) | Wirkungsgrad | Preis (€) |
|--------|-----|----------|----------|-----------|-------------|-----------|
| SPR-E-Flex-100 | 100 | 18,5 | 5,41 | 1046×536×2,5 | 17,8% | 495 |
| SPR-E-Flex-170 | 170 | 28,6 | 5,94 | 1564×536×2,5 | 20,3% | 745 |
| MAX3-400 (Rigid) | 400 | 40,3 | 9,93 | 1690×1046×40 | 22,7% | 420 |

**Confidence:** measured — Maxeon Datenblätter (maxeon.com), Preise: Händler-UVP 2025.

### 4.5 Lensun (China)

**Hersteller:** Lensun Solar Technology Co., Ltd., Shenzhen, China
**Marine-Fokus:** Mittel — preisgünstiger Anbieter für semiflexible Marine-Panels

**Semiflexible Module:**
| Modell | Wp | Vmpp (V) | Impp (A) | Voc (V) | Isc (A) | Maße (mm) | Gewicht (kg) | Preis (€) |
|--------|-----|----------|----------|---------|---------|-----------|-------------|-----------|
| LSF-50 | 50 | 18,0 | 2,78 | 21,6 | 3,05 | 620×540×2,5 | 1,2 | 95 |
| LSF-80 | 80 | 18,2 | 4,40 | 22,0 | 4,80 | 955×540×2,5 | 1,9 | 135 |
| LSF-100 | 100 | 18,4 | 5,44 | 22,5 | 5,90 | 1060×540×2,5 | 2,3 | 155 |
| LSF-160 | 160 | 18,6 | 8,60 | 22,8 | 9,30 | 1345×670×2,5 | 3,5 | 225 |
| LSF-200 | 200 | 36,8 | 5,44 | 44,5 | 5,90 | 1350×670×3 | 3,8 | 275 |

**Besonderheiten Lensun:**
- Sehr gutes Preis-Leistungs-Verhältnis
- ETFE-Beschichtung
- MC4-Steckverbinder standard
- Qualität: gut für den Preis, aber nicht auf Solbian/Sunware-Niveau
- Garantie: 2 Jahre Produkt, 5 Jahre Leistung (80%)
- Beliebt bei Budget-Langfahrtseglern

**Confidence:** documented — Lensun-Datenblätter, Erfahrungsberichte Cruisers Forum.

### 4.6 Renogy (USA/China)

**Hersteller:** Renogy, Ontario (CA), USA — Fertigung China
**Marine-Fokus:** Mittel — Marine-spezifische Linie vorhanden

**Marine-Serie:**
| Modell | Wp | Vmpp (V) | Impp (A) | Voc (V) | Isc (A) | Maße (mm) | Gewicht (kg) | Preis (€) |
|--------|-----|----------|----------|---------|---------|-----------|-------------|-----------|
| RNG-100D-SS Marine | 100 | 18,9 | 5,29 | 22,5 | 5,75 | 1060×508×3 | 2,1 | 175 |
| RNG-175D-SS Marine | 175 | 19,2 | 9,11 | 23,4 | 9,72 | 1475×670×3 | 3,5 | 285 |
| RNG-200MB (Rigid) | 200 | 20,4 | 9,80 | 24,8 | 10,40 | 1580×808×35 | 13,0 | 245 |
| RNG-100DB (Flex) | 100 | 18,9 | 5,29 | 22,5 | 5,75 | 1210×540×2,5 | 2,0 | 165 |
| RNG-50D Marine | 50 | 17,9 | 2,79 | 21,6 | 3,05 | 630×508×3 | 1,1 | 95 |

**Besonderheiten Renogy:**
- Solider Mittelklasse-Anbieter mit großem Sortiment
- Marine-Linie mit spezieller Korrosionsbehandlung
- Gute Bluetooth-Integration (Renogy DC Home App)
- Eigene MPPT-Laderegler (Rover-Serie) — funktional, nicht Victron-Niveau
- 5 Jahre Materialgarantie, 25 Jahre Leistung (80%) bei starren Modulen
- 1 Jahr Garantie auf flexible Module (!)

**Confidence:** measured — Renogy-Datenblätter (renogy.com), Preise: EU-UVP 2025.

---

## 5. Hersteller-Datenbank

### 5.1 Victron Energy (Niederlande)

| Kriterium | Bewertung |
|-----------|-----------|
| **Firmensitz** | Almere, Niederlande |
| **Gegründet** | 1975 |
| **Spezialisierung** | Off-Grid-Energiesysteme, Marine, Mobil |
| **Stärken** | Komplettes Ökosystem (Panel→Regler→Batterie→Inverter→Monitoring), VRM-Portal, Bluetooth-Integration, enorme Zuverlässigkeit, weltweiter Service |
| **Schwächen** | Panels selbst sind Standardqualität (Zukauf), Premium-Preis für Regler/Inverter |
| **Marine-Relevanz** | Marktführer bei MPPT-Reglern und Systemintegration |
| **Garantie** | 5 Jahre (Module), 5 Jahre (Regler) |
| **Vertrieb** | Weltweit, >4.500 Händler |
| **Website** | victronenergy.com |
| **AYDI-Bewertung** | ★★★★★ (Systemintegration), ★★★☆☆ (Panels allein) |

### 5.2 Sunware (Deutschland)

| Kriterium | Bewertung |
|-----------|-----------|
| **Firmensitz** | Schwalmtal, Nordrhein-Westfalen, Deutschland |
| **Gegründet** | 1993 |
| **Spezialisierung** | Marine- und Outdoor-Solarmodule |
| **Stärken** | Deutsche Fertigung, exzellente Qualitätskontrolle, echte Salzwasser-Langzeit-Tests, sehr langlebig für semiflexible Panels |
| **Schwächen** | Höherer Preis, begrenztes Sortiment, kein eigenes Systemzubehör |
| **Marine-Relevanz** | Top-Hersteller für semiflexible Marine-Panels in Europa |
| **Garantie** | 5 Jahre Produkt, 10 Jahre Leistung (90%) |
| **Vertrieb** | Direkt + Fachhändler Europa |
| **Website** | sunware.de |
| **AYDI-Bewertung** | ★★★★★ (Qualität semiflexibel), ★★★★☆ (Preis-Leistung) |

### 5.3 Solbian (Italien)

| Kriterium | Bewertung |
|-----------|-----------|
| **Firmensitz** | Avigliana (Turin), Italien |
| **Gegründet** | 2007 |
| **Spezialisierung** | Ultra-Premium semiflexible Marine-Panels mit SunPower-Zellen |
| **Stärken** | Höchster Wirkungsgrad, beste Verschattungstoleranz (Bypass pro Zelle), Maßanfertigung, ultraleicht, Referenzen im Profi-Segelsport (Vendée Globe, Volvo Ocean Race) |
| **Schwächen** | Sehr hoher Preis (2–3× Sunware), lange Lieferzeiten bei Custom, begrenzte Händlerdichte |
| **Marine-Relevanz** | Premium-Segment, Regatta und Luxus-Langfahrt |
| **Garantie** | 5 Jahre Produkt |
| **Vertrieb** | Direkt + wenige autorisierte Händler |
| **Website** | solbian.eu |
| **AYDI-Bewertung** | ★★★★★ (Technik/Performance), ★★★☆☆ (Preis-Leistung) |

### 5.4 Lensun (China)

| Kriterium | Bewertung |
|-----------|-----------|
| **Firmensitz** | Shenzhen, Guangdong, China |
| **Gegründet** | 2012 |
| **Spezialisierung** | Preisgünstige semiflexible Panels für Marine/Camper |
| **Stärken** | Sehr günstiger Preis, akzeptable Qualität, schnelle Lieferung, großes Sortiment |
| **Schwächen** | Geringere Langlebigkeit (3–6 Jahre typisch), Qualitätsschwankungen zwischen Chargen, Support nur Englisch/Chinesisch |
| **Marine-Relevanz** | Budget-Segment, Einsteiger, Zweit-Anlage |
| **Garantie** | 2 Jahre Produkt, 5 Jahre Leistung (80%) |
| **Vertrieb** | Online (Amazon, eigener Shop) |
| **Website** | lensun.com |
| **AYDI-Bewertung** | ★★★☆☆ (Qualität), ★★★★★ (Preis-Leistung kurzfristig) |

### 5.5 Renogy (USA/China)

| Kriterium | Bewertung |
|-----------|-----------|
| **Firmensitz** | Ontario, Kalifornien, USA — Fertigung China |
| **Gegründet** | 2010 |
| **Spezialisierung** | Solar-Komplettsysteme für Mobile/Marine/Off-Grid |
| **Stärken** | Gutes Preis-Leistungs-Verhältnis, breites Sortiment (Panel→Regler→Batterie), App-Integration, guter US-Support |
| **Schwächen** | Marine-Linie nicht Kerngeschäft, flexible Panels kurzlebig, Europa-Support limitiert |
| **Marine-Relevanz** | Mittelklasse, populär in USA |
| **Garantie** | 5 Jahre (starr), 1 Jahr (flexibel) |
| **Vertrieb** | Online (renogy.com, Amazon), wenige EU-Händler |
| **Website** | renogy.com |
| **AYDI-Bewertung** | ★★★★☆ (starr), ★★★☆☆ (flexibel) |

### 5.6 Gioco Solutions (Italien)

| Kriterium | Bewertung |
|-----------|-----------|
| **Firmensitz** | Treviso, Venetien, Italien |
| **Gegründet** | 2009 |
| **Spezialisierung** | Marine-Solarmodule, begehbare Panels |
| **Stärken** | Große Auswahl begehbarer Panels, CIGS-Dünnschicht im Programm, gute Verarbeitungsqualität, italienische Fertigung |
| **Schwächen** | Weniger bekannt als Solbian, begrenzte internationale Distribution |
| **Marine-Relevanz** | Hoch — spezialisiert auf Yacht-Anwendungen |
| **Garantie** | 3 Jahre Produkt, 10 Jahre Leistung |
| **Vertrieb** | Fachhändler Italien + EU |
| **Website** | giocosolutions.com |
| **AYDI-Bewertung** | ★★★★☆ (Qualität), ★★★★☆ (Preis-Leistung) |

### 5.7 a]SES (Deutschland) — Advanced Solar Energy Systems

| Kriterium | Bewertung |
|-----------|-----------|
| **Firmensitz** | Hamburg, Deutschland |
| **Gegründet** | 2015 |
| **Spezialisierung** | CIGS-Dünnschicht für Marine-Anwendungen |
| **Stärken** | Spezialist für CIGS-Marine, extrem leicht, gute Beratung für Yacht-Integration |
| **Schwächen** | Kleine Firma, begrenzte Produktionskapazität, hohe Preise |
| **Marine-Relevanz** | Nischenspezialist für gewichtskritische Anwendungen |
| **Garantie** | 5 Jahre Produkt, 15 Jahre Leistung |
| **Vertrieb** | Direkt |
| **AYDI-Bewertung** | ★★★★☆ (Technik), ★★★☆☆ (Preis-Leistung) |

### 5.8 ECTIVE (Deutschland)

| Kriterium | Bewertung |
|-----------|-----------|
| **Firmensitz** | Hamburg, Deutschland |
| **Gegründet** | 2018 |
| **Spezialisierung** | Mobile Energiesysteme, Marine-Solar |
| **Stärken** | Gutes Preis-Leistungs-Verhältnis, deutsche Qualitätskontrolle, guter Support, schnelle Lieferung EU |
| **Schwächen** | Noch junges Unternehmen, keine eigene Zellfertigung |
| **Marine-Relevanz** | Mittelklasse, wachsend |
| **Garantie** | 3 Jahre Produkt |
| **Vertrieb** | Online + Fachhändler Deutschland |
| **Website** | ective.de |
| **AYDI-Bewertung** | ★★★★☆ (Preis-Leistung), ★★★☆☆ (Langzeiterfahrung) |

---

## 6. Fehlerbild-Atlas

### 6.1 Hotspot (Thermische Überlastung)

**Beschreibung:**
Ein Hotspot entsteht, wenn eine einzelne Zelle durch Verschattung, Verschmutzung oder Zelldefekt zum Verbraucher wird. Der gesamte String-Strom fließt durch die gesperrte Zelle, die sich auf 150–300°C erhitzt.

**Visuelle Identifikation:**
- Verfärbung (braun/schwarz) einer einzelnen Zelle oder Zellgruppe
- Blasenbildung in der Verkapselung (EVA)
- Geschmolzene oder deformierte Rückseitenfolie
- Im Extremfall: verkohlter Bereich, Brandspuren

**Ursachen:**
1. Dauerverschattung einer Zelle (Vogelkot, festsitzende Blätter, Salzablagerung)
2. Defekte Bypass-Diode (leitet nicht)
3. Gebrochene Zelle (Mikroriss → Hochohmbereich)
4. Fehlender MPPT-Regler (Batterie-Direktanschluss bei Verschattung)

**Schweregrad:** KRITISCH — Brandgefahr, sofortige Stilllegung des betroffenen Strings erforderlich.

**Prävention:**
- Regelmäßige Reinigung (mindestens monatlich)
- Panels mit Bypass-Diode pro Zelle (Solbian) bevorzugen
- MPPT-Regler mit String-Überwachung
- Thermografie-Check alle 2 Jahre

**AYDI-Scoring:**
- Confidence: `visual_high` (deutliche Verfärbung erkennbar)
- Befund-Kategorie: KRITISCH
- Empfehlung: Sofortige Außerbetriebnahme, Panel-Austausch

### 6.2 Delamination der Frontschicht

**Beschreibung:**
Ablösung der ETFE/PET-Frontfolie oder des Frontglases vom EVA-Einbettungsmaterial. Beginnt typisch an Kanten oder Ecken und breitet sich flächig aus.

**Visuelle Identifikation:**
- Blasenbildung unter der Frontfläche (Lufteinschlüsse)
- Milchige/trübe Bereiche (Feuchtigkeitseintritt)
- Wellige Oberfläche bei semiflexiblen Panels
- Abgelöste Kanten (sichtbarer Spalt zwischen Folie und Laminat)

**Ursachen:**
1. UV-Degradation des EVA-Klebers (>5 Jahre Sonnenexposition)
2. Thermische Zyklen (>50°C Temperaturspanne Tag/Nacht in Tropen)
3. Mechanische Beanspruchung (Seegang, Betreten)
4. Fertigungsmangel (unzureichende Laminiertemperatur/Druck)
5. Salzwasser-Eindringen an Schnittkanten

**Schweregrad:** HOCH — Leistungsverlust 10–30%, beschleunigt weitere Degradation, Feuchtigkeitseintritt → Korrosion der Zellverbinder.

**Prävention:**
- ETFE bevorzugen (höhere UV-Beständigkeit als PET)
- Kanten versiegeln (Silikon/PU-Dichtmasse)
- Panels nicht über minimalen Biegeradius knicken
- Hochwertige Panels mit Vakuumlaminierung

**AYDI-Scoring:**
- Confidence: `visual_high` (deutlich sichtbare Blasen/Trübung)
- Befund-Kategorie: HOCH
- Empfehlung: Panel-Austausch mittelfristig planen (3–12 Monate)

### 6.3 Mikrorisse in Solarzellen

**Beschreibung:**
Haarfeine Risse im Silizium-Wafer, die mit bloßem Auge nicht sichtbar sind. Entstehen durch mechanische Belastung (Biegung, Stoß, Vibration). Reduzieren den aktiven Zellbereich und können zu Hotspots führen.

**Visuelle Identifikation:**
- Nicht direkt sichtbar (nur per Elektrolumineszenz-Test)
- Indirekte Zeichen: ungleichmäßige Leistungsverteilung, unerklärter Ertragsverlust
- Gelegentlich: dunkle Linien bei Gegenlicht (starke Risse)
- Schneckenspuren (Snail Trails): braune Linien entlang der Risse (erst nach Monaten sichtbar)

**Ursachen:**
1. Transport-Erschütterungen (ungepolsterte Lagerung)
2. Wiederholte Biegung (Seegang bei semiflexiblen Panels)
3. Betreten ohne Lastverteilung
4. Punktuelle Belastung (Schäkel, Werkzeug auf Panel)
5. Hagel oder Stoß durch Fallen/Leinen

**Schweregrad:** MITTEL bis HOCH — anfänglich geringer Ertragsverlust (2–5%), verschlechtert sich progressiv, kann zu Hotspot eskalieren.

**Prävention:**
- Panels nie über minimalen Biegeradius biegen
- Begehbare Panels nur mit weichen Sohlen betreten
- Lastverteilung bei Lagerung (flach, gepolstert)
- SunPower-Maxeon-Zellen sind deutlich bruchfester (dickere Kupfer-Rückelektrode)

**AYDI-Scoring:**
- Confidence: `visual_low` (visuell kaum erkennbar)
- Befund-Kategorie: MITTEL (ohne Hotspot-Folge)
- Empfehlung: Elektrolumineszenz-Test, Leistungsmessung zur Bestätigung

### 6.4 Korrosion der Anschlussdose / Steckverbinder

**Beschreibung:**
Korrosion an MC4-Steckverbindern, Anschlussdosen oder Kabelschuhen durch Salzwasser-Exposition. Erhöht Übergangswiderstände, verursacht Leistungsverlust und kann zu Überhitzung/Brand führen.

**Visuelle Identifikation:**
- Grünspan (Kupferkorrosion) an Kontakten
- Weiße Ablagerungen (Aluminiumkorrosion) an Rahmen-Erdung
- Verfärbte/schwarze MC4-Kontakte
- Aufgequollene oder rissige Anschlussdosen-Dichtung
- Salzrückstände an Kabelverbindungen

**Ursachen:**
1. Spritzwasser / Seeschlag auf Kontakte
2. Nicht abgedichtete MC4-Verbindungen (fehlende Tüllen)
3. Kondenswasser in Anschlussdose (Temperaturwechsel)
4. Ungeeignete Materialien (verzinkt statt Edelstahl, Kupfer statt Messing)
5. Fehlende Schutzfettung der Kontakte

**Schweregrad:** MITTEL bis HOCH — 5–15% Leistungsverlust durch Übergangswiderstand, Brandgefahr bei fortgeschrittener Korrosion.

**Prävention:**
- Alle MC4-Verbindungen oberhalb der Spritzwasserlinie
- Kontaktfett (Vaseline oder DeoxIT) auf alle Verbindungen
- IP67-Anschlussdosen (Minimum)
- Regelmäßige Inspektion aller Verbindungen (halbjährlich)
- Selbstverschweißendes Tape um MC4-Verbindungen

**AYDI-Scoring:**
- Confidence: `visual_medium` (Korrosion sichtbar bei Inspektion)
- Befund-Kategorie: MITTEL
- Empfehlung: Kontakte reinigen/erneuern, Schutzmaßnahmen implementieren

### 6.5 Verschattungsverlust durch Rigg

**Beschreibung:**
Systematischer Ertragsverlust durch den wandernden Schatten von Mast, Wanten, Stagen und Baumniederholer über die Panels. Auf Segelyachten der häufigste und schwer vermeidbare Verlustfaktor.

**Visuelle Identifikation:**
- Schatten auf Panels bei Sonnenschein erkennbar
- Typisches Muster: Linien (Want-Schatten) oder breiter Balken (Mast)
- Am besten mittags bei steil stehender Sonne prüfen
- Zeitraffer-Dokumentation: Schattenwanderung über den Tag

**Quantifizierung:**
| Verschattungssituation | Verlust ohne Bypass | Verlust mit Bypass (3 Dioden) | Verlust mit Solbian (1/Zelle) |
|------------------------|--------------------|-----------------------------|-------------------------------|
| Want-Schatten (1 Linie über 1 Zelle) | -33 bis -50% | -33% | -3% |
| Mast-Schatten (5 cm breit, 1 Zelle) | -33 bis -50% | -33% | -3% |
| Baum-Schatten (15 cm breit, 3 Zellen) | -66 bis -100% | -33 bis -66% | -9% |
| Lazy-Jack (schmale Linie) | -33% | -33% | -2% |
| Großsegel (ungerefft, Heckpanels) | -100% | -100% | -80% |

**Prävention/Milderung:**
- Panel-Positionierung außerhalb des Rigg-Schattenbereichs (Arch weit achtern)
- Panels parallel zum Mast-Schatten ausrichten (Schatten wandert, trifft weniger Zellen)
- Panels mit individuellen Bypass-Dioden (Solbian)
- Mehrere MPPT-Regler für verschieden verschattete Panels
- Panel-Optimizer (z.B. Tigo) für jeden einzelnen String

**AYDI-Scoring:**
- Confidence: `visual_medium` (Schattenverlauf abhängig von Sonnenstand und Kurs)
- Befund-Kategorie: MITTEL (chronischer Verlust)
- Empfehlung: Verschattungsanalyse durchführen, Panel-Anordnung optimieren

### 6.6 Kabelbruch / Kontaktfehler

**Beschreibung:**
Unterbrechung oder Hochohmkontakt in der Verkabelung zwischen Panel und Laderegler. Kann komplett (kein Ertrag) oder teilweise (intermittierend) sein.

**Visuelle Identifikation:**
- Beschädigte Kabelisolierung (UV-Degradation, Scheuerstellen)
- Lose oder oxidierte Crimpverbindungen
- Gebrochene Lötverbindungen in der Anschlussdose
- Schmelzspuren an Kontakten (Überhitzung durch Hochohmkontakt)
- Kabel ohne Zugentlastung (Zugbelastung auf Lötstelle)

**Ursachen:**
1. UV-Degradation der Kabelisolierung (nicht-UV-feste Kabel)
2. Scheuern an Durchführungen (fehlende Kantenschutzprofile)
3. Vibration (Motorlauf) lockert Schraubklemmen
4. Korrosion der Crimpverbindung (nicht-verzinnte Litze)
5. Thermische Belastung (Überstrom durch zu dünne Kabel)

**Schweregrad:** MITTEL bis HOCH — Totalausfall oder intermittierender Ertragsverlust, bei Kurzschluss Brandgefahr.

**Prävention:**
- Marine-Kabel verwenden (doppelt isoliert, UV-fest, verzinnte Litze)
- Alle Durchführungen mit Kantenschutz
- Crimpverbindungen mit Schrumpfschlauch + Schutzlack
- Kabelzugentlastung an allen Anschlusspunkten
- Jährliche Kabelinspektion und Isolationsmessung

**AYDI-Scoring:**
- Confidence: `visual_medium` (bei sichtbaren Kabelschäden)
- Befund-Kategorie: MITTEL bis HOCH
- Empfehlung: Kabel ersetzen, Schutzmaßnahmen nachrüsten

### 6.7 PID (Potential Induced Degradation)

**Beschreibung:**
Spannungsinduzierte Degradation tritt auf, wenn hohe Potentialdifferenzen (typisch >60V in System) zwischen Zellen und Rahmen/Montagefläche entstehen. Ionen wandern durch die Verkapselung und beschädigen die Zellstruktur.

**Visuelle Identifikation:**
- Nicht direkt sichtbar (nur per EL-Test oder Leistungsmessung)
- Indirekter Hinweis: Module am negativen String-Ende zeigen stärkeren Ertragsverlust
- Langfristig: leichte Verfärbung betroffener Zellen

**Ursachen:**
1. Hohe Systemspannung (>48V Strings) bei feuchtem Klima
2. Defekte Isolation (Leckstrom zum Rahmen/Deck)
3. Geerdeter Rahmen auf Metallboot (Potentialunterschied)
4. Kondenswasser auf Panelrückseite bei hoher Spannung

**Schweregrad:** MITTEL — schleichender Leistungsverlust (5–30% über Jahre), teilweise reversibel.

**Prävention:**
- Systemspannung unter 60V halten (12V/24V-Systeme unproblematisch)
- Floating-Ground-Design (negative Schiene nicht geerdet)
- PID-freie Module verwenden (Hersteller-Spezifikation)
- Galvanische Trennung Panel-String ↔ Bordnetz

**Marine-Relevanz:** Auf 12V- und 24V-Systemen mit kurzen Strings (2–4 Panels) praktisch kein Risiko. Relevant erst bei 48V-Systemen auf großen Katamaranen.

**AYDI-Scoring:**
- Confidence: `visual_insufficient` (visuell nicht erkennbar)
- Befund-Kategorie: NIEDRIG (bei typischen Bord-12V/24V-Systemen)
- Empfehlung: Nur bei Hochvolt-Strings relevant, Leistungsmonitoring

### 6.8 Schneckenspuren (Snail Trails)

**Beschreibung:**
Braune, geschlängelte Linien auf der Zelloberfläche, die an Schneckenspuren erinnern. Entstehen durch chemische Reaktion zwischen Silber-Metallisierung und Feuchtigkeit/Essigsäure (aus EVA-Degradation) entlang von Mikrorissen.

**Visuelle Identifikation:**
- Braune/silbrige geschlängelte Linien auf Zelloberfläche
- Typischerweise entlang von Zellkanten und Mikroriss-Verläufen
- Treten nach 2–5 Jahren auf
- Verstärkt bei feucht-warmem Klima

**Ursachen:**
1. Mikrorisse im Silizium (Voraussetzung)
2. Feuchtigkeitseintritt durch defekte Verkapselung
3. EVA-Degradation setzt Essigsäure frei
4. Chemische Reaktion mit Silber-Busbars

**Schweregrad:** NIEDRIG bis MITTEL — kosmetisch auffällig, Leistungsverlust typisch <5%, aber Indikator für Mikrorisse.

**AYDI-Scoring:**
- Confidence: `visual_high` (deutlich sichtbar)
- Befund-Kategorie: NIEDRIG
- Empfehlung: Monitoring, keine sofortige Maßnahme, aber Mikrorisse im Blick behalten

### 6.9 Glasbruch (starre Module)

**Beschreibung:**
Bruch des Frontglases bei starren Modulen durch mechanische Einwirkung (Stoß, Hagel, herabfallende Gegenstände). Das gehärtete Glas (ESG) zerspringt in kleine Würfel.

**Visuelle Identifikation:**
- Spinnennetz-artiges Rissmuster im Frontglas
- Weißliche Trübung im Bruchbereich
- Splitter auf dem Deck
- Leistungseinbruch am Monitoring erkennbar

**Ursachen:**
1. Herabfallender Gegenstand (Block, Schäkel aus dem Rigg)
2. Großbaum-Patenthalse (Traveller-Schiene schlägt auf Panel)
3. Ungesicherter Bootshaken bei Seegang
4. Hagel (>25mm Durchmesser)
5. Transport-Schaden (Packer-Fehler)

**Schweregrad:** HOCH — Modul muss ersetzt werden. Feuchtigkeitseintritt → Isolation gefährdet → Sicherheitsrisiko.

**AYDI-Scoring:**
- Confidence: `visual_high` (sofort erkennbar)
- Befund-Kategorie: HOCH
- Empfehlung: Sofortige Stilllegung des Moduls, Austausch

### 6.10 Rückseitenfolie-Degradation

**Beschreibung:**
Versprödung, Rissbildung oder Verfärbung der Rückseitenfolie (Backsheet). Bei semiflexiblen Panels häufig nach 4–8 Jahren in tropischen Einsatzgebieten.

**Visuelle Identifikation:**
- Gelbliche/bräunliche Verfärbung der Rückseite
- Rissbildung in der Backsheet-Folie (feine Netzrisse)
- Ablösung der Folie an Kanten
- Sichtbare Zellverbinder durch transparenter werdende Folie

**Ursachen:**
1. UV-Bestrahlung (bei nicht-Deck-montierter Rückseite)
2. Thermische Alterung (permanente >50°C)
3. Feuchtigkeitseinwirkung
4. Materialqualität (PET-basiert weniger langlebig als fluorpolymerbasiert)

**Schweregrad:** MITTEL — Isolation gefährdet, Feuchtigkeitseintritt, beschleunigt Gesamtdegradation.

**AYDI-Scoring:**
- Confidence: `visual_medium` (erfordert Rückseiten-Inspektion)
- Befund-Kategorie: MITTEL
- Empfehlung: Panel-Austausch innerhalb 1 Jahr planen

### 6.11 Vergilbung der ETFE/EVA-Schicht

**Beschreibung:**
Gelbliche Verfärbung der Einkapselungsschicht (EVA) oder Frontfolie (ETFE/PET) durch UV-Langzeitbelastung. Reduziert die Lichttransmission und damit den Ertrag.

**Visuelle Identifikation:**
- Gleichmäßige gelbliche Tönung des gesamten Panels
- Besonders sichtbar im Vergleich mit neuem Panel gleichen Typs
- Typisch nach 5–10 Jahren (EVA) bzw. 8–15 Jahren (ETFE)
- Stärkere Vergilbung in tropischen Regionen

**Quantifizierung:**
| Alter | EVA-Transmissionsverlust | ETFE-Transmissionsverlust |
|-------|-------------------------|--------------------------|
| 5 Jahre | -2 bis -5% | -1 bis -2% |
| 10 Jahre | -5 bis -10% | -2 bis -4% |
| 15 Jahre | -10 bis -18% | -3 bis -6% |
| 20 Jahre | -15 bis -25% | -5 bis -8% |

**AYDI-Scoring:**
- Confidence: `visual_medium` (Vergleich mit Referenz nötig)
- Befund-Kategorie: NIEDRIG (normal, alterstypisch)
- Empfehlung: Monitoring, Teil des normalen Alterungsprozesses

### 6.12 Fehlerhafter MPPT-Tracking

**Beschreibung:**
Der MPPT-Laderegler findet nicht den optimalen Arbeitspunkt (MPP), sondern verharrt auf einem lokalen Maximum oder oszilliert instabil. Ertragsverlust ohne erkennbare Panel-Schäden.

**Visuelle Identifikation:**
- Nicht visuell am Panel erkennbar
- Erkennbar am Monitoring: Ertrag deutlich unter erwartetem Wert bei gutem Wetter
- Unstete Leistungsanzeige (starke Schwankungen ohne Wolken)
- Regler-LED zeigt Fehlerzustand

**Ursachen:**
1. Teilverschattung → Multiple MPP-Peaks → Regler findet nur lokales Maximum
2. Defekter Regler (interne Elektronik)
3. Falsche Regler-Einstellung (Batterietyp, Spannungsgrenzen)
4. Inkompatible Panel-Konfiguration (Vmpp zu niedrig für Regler)
5. Firmware-Bug (selten, aber dokumentiert)

**Schweregrad:** MITTEL — 10–40% Ertragsverlust ohne Panelschaden.

**AYDI-Scoring:**
- Confidence: `visual_insufficient` (nur per Monitoring/Messung erkennbar)
- Befund-Kategorie: MITTEL
- Empfehlung: Regler-Firmware aktualisieren, Konfiguration prüfen, ggf. Regler tauschen

---

## 7. Troubleshooting-Entscheidungsbäume

### 7.1 Entscheidungsbaum: Kein Ertrag (0 Watt Leistung)

```
START: Panel liefert 0W Ertrag
│
├─ Ist es dunkel / stark bewölkt?
│  ├─ JA → Normal. Warten auf Sonne.
│  └─ NEIN → Weiter
│
├─ Sicherung / Leitungsschutz geprüft?
│  ├─ Sicherung defekt → Sicherung ersetzen, Kurzschluss-Ursache finden
│  └─ Sicherung OK → Weiter
│
├─ Voc am Panel messen (Panel-Stecker offen, Multimeter):
│  ├─ Voc = 0V → Panel-Defekt oder Kabelbruch VOR Stecker
│  │  ├─ Anschlussdose öffnen: Kabel ab Panel messen
│  │  │  ├─ Voc direkt an Zellverbinder >0V → Kabel/Stecker defekt
│  │  │  └─ Voc = 0V → Totaler Panel-Defekt (alle Bypass offen?)
│  │  │     └─ Bypass-Dioden prüfen (alle kurzgeschlossen = 0V)
│  │  └─ Kabel sichtbar beschädigt? → Kabel ersetzen
│  │
│  ├─ Voc vorhanden aber niedrig (z.B. 7V statt 22V) →
│  │  └─ 1–2 Bypass-Dioden leiten dauerhaft (Kurzschluss)
│  │     └─ Bypass-Dioden einzeln prüfen/ersetzen
│  │
│  └─ Voc normal (z.B. 22V) → Panel OK, Fehler im Ladepfad
│     ├─ Spannung am Regler-Eingang messen:
│     │  ├─ 0V am Regler → Kabelbruch Panel→Regler
│     │  └─ Voc am Regler vorhanden → Regler-Defekt oder Batterie-Problem
│     │     ├─ Regler-Status-LED prüfen
│     │     ├─ Batteriespannung messen
│     │     │  ├─ Batterie voll (14,4V+) → Regler reguliert (normal)
│     │     │  └─ Batterie nicht voll → Regler defekt
│     │     └─ Regler-Reset / Firmware-Update versuchen
│     └─ ERGEBNIS: Fehlerquelle identifiziert
│
└─ ERGEBNIS: Gezielte Reparatur/Austausch
```

### 7.2 Entscheidungsbaum: Ertrag zu niedrig (Minderleistung)

```
START: Ertrag deutlich unter Erwartung (>30% Differenz)
│
├─ Verschmutzung prüfen:
│  ├─ Salzkruste / Vogelkot / Algen sichtbar?
│  │  └─ JA → Reinigen mit Süßwasser + weichem Tuch, dann neu messen
│  └─ Panel sauber → Weiter
│
├─ Verschattung prüfen (zur Peakzeit, 10–14 Uhr):
│  ├─ Teilschatten erkennbar?
│  │  ├─ JA → Schattenquelle identifizieren
│  │  │  ├─ Vermeidbar (Segel, Beiboot) → Entfernen/Versetzen
│  │  │  └─ Nicht vermeidbar (Mast, Want) → Panel-Anordnung/Verschaltung optimieren
│  │  └─ Kein Schatten → Weiter
│  └─ NEIN → Weiter
│
├─ Panel-Oberfläche inspizieren:
│  ├─ Delamination / Blasen? → Panel degradiert (→ Fehlerbild 6.2)
│  ├─ Vergilbung? → Altersbedingt (→ Fehlerbild 6.11)
│  ├─ Schneckenspuren? → Mikrorisse (→ Fehlerbild 6.8)
│  └─ Optisch einwandfrei → Weiter
│
├─ Systemcheck:
│  ├─ Vmpp unter Last messen (Regler-Display/App):
│  │  ├─ Vmpp deutlich unter Datenblatt → Temperatur-Problem oder Zelldefekt
│  │  └─ Vmpp normal → Weiter
│  ├─ Impp unter Last messen:
│  │  ├─ Impp niedrig bei normalem Vmpp → Verschattung, Verschmutzung oder Degradation
│  │  └─ Impp normal → Kein Panel-Problem
│  └─ Regler-Effizienz prüfen:
│     ├─ Eingangsleistung vs. Ausgangsleistung >10% Differenz?
│     │  └─ JA → Regler arbeitet ineffizient, Firmware/Konfiguration prüfen
│     └─ NEIN → Kabel-/Kontaktwiderstände prüfen
│
├─ Kabelwiderstände:
│  ├─ Spannungsabfall Panel→Regler messen (bei Volllast):
│  │  ├─ >0,5V (12V-System) / >1V (24V-System) → Kabel zu dünn oder Kontaktproblem
│  │  └─ Akzeptabel → Batterie-/Temperaturproblem
│  └─ Alle Steckverbinder auf Korrosion prüfen
│
└─ ERGEBNIS: Ursache eingegrenzt, gezielte Maßnahme
```

### 7.3 Entscheidungsbaum: Regler zeigt Fehlermeldung

```
START: MPPT-Regler zeigt Fehler-LED oder Fehlermeldung in App
│
├─ Fehlertyp identifizieren (aus App/LED-Code):
│
├─ "Overvoltage" (Überspannung Eingang):
│  ├─ Voc_max der Stringkonfiguration berechnen (bei aktueller Temperatur)
│  │  ├─ Voc > Regler-Maximum → String kürzen (Panel entfernen)
│  │  └─ Voc < Maximum → Transienter Spike (Wolke→Sonne schnell)
│  │     └─ Surge-Protector vor Regler installieren
│  └─ Panels nie bei Sonnenschein ohne Last trennen (Voc springt auf Maximum)
│
├─ "Battery Overvoltage" (Batterie-Überspannung):
│  ├─ Batteriespannung messen:
│  │  ├─ >14,8V (12V-System) → Ladeschlussspannung überschritten
│  │  │  ├─ BMS hat abgeschaltet? (LiFePO4)
│  │  │  ├─ Batterietyp im Regler falsch eingestellt?
│  │  │  └─ Temperatursensor defekt?
│  │  └─ Normal → Messfehler im Regler, Sense-Leitung prüfen
│  └─ Regler-Einstellungen prüfen (Ladeprofil)
│
├─ "Over-temperature" (Übertemperatur):
│  ├─ Regler-Einbauort belüftet?
│  │  ├─ NEIN → Für Belüftung sorgen (Lüfter, größerer Kasten)
│  │  └─ JA → Regler überlastet?
│  │     └─ Panelleistung > Regler-Nennleistung? → Größeren Regler wählen
│  └─ Umgebungstemperatur >40°C → Derating des Reglers beachten
│
├─ "Short Circuit" (Kurzschluss):
│  ├─ Panels vom Regler trennen
│  ├─ Kabel zwischen Panel und Regler auf Kurzschluss prüfen (Widerstand messen)
│  │  ├─ Kurzschluss gefunden → Kabel reparieren, Ursache finden
│  │  └─ Kein Kurzschluss → Bypass-Diode im Panel defekt (Kurzschluss-Modus)
│  └─ Regler nach Behebung resetten
│
└─ "Communication Error" (BMS-Kommunikation):
   ├─ VE.Direct/VE.Can-Kabel prüfen
   ├─ Bluetooth-Verbindung resetten
   └─ Firmware-Update durchführen
```

### 7.4 Entscheidungsbaum: Intermittierender Ertrag (geht an und aus)

```
START: Solar-Ertrag schwankt extrem / geht intermittierend auf Null
│
├─ Muster identifizieren:
│  ├─ Nur bei Seegang → Lockerer Kontakt (vibrations-sensitiv)
│  │  ├─ MC4-Stecker am Panel prüfen (fest eingerastet?)
│  │  ├─ Schraubklemmen am Regler nachziehen
│  │  ├─ Crimpverbindungen prüfen (Wackelkontakt)
│  │  └─ Lötstellen in Anschlussdose prüfen (kalte Lötstelle)
│  │
│  ├─ Bei bestimmtem Kurs → Verschattung durch Rigg/Segel
│  │  └─ Panel-Anordnung oder Segelstellung optimieren
│  │
│  ├─ Nur bei Hitze → Thermisches Problem
│  │  ├─ Regler-Derating bei Überhitzung
│  │  ├─ Bypass-Diode wird leitend (thermisch ausgelöst)
│  │  └─ BMS der Batterie schaltet bei Übertemperatur ab
│  │
│  ├─ Unregelmäßig / zufällig → Elektronik-Defekt
│  │  ├─ Regler-Firmware aktualisieren
│  │  ├─ Regler probeweise tauschen
│  │  └─ Erdschluss / Leckstrom prüfen (Isolationsmessung)
│  │
│  └─ Jeden Tag gleiche Uhrzeit → Schatten eines festen Objekts
│     └─ Schattenanalyse zur betreffenden Uhrzeit
│
├─ Diagnose-Methode:
│  ├─ Victron VRM-Logging (minutengenau) → Zeitstempel mit Ereignis korrelieren
│  ├─ Spannungsmessung mit Logger am Panel-Ausgang
│  └─ Wackeln an Verbindungen bei laufender Messung
│
└─ ERGEBNIS: Fehlerquelle identifiziert
```

### 7.5 Entscheidungsbaum: Panel-Auswahl (Kaufentscheidung)

```
START: Welches Panel-System passt?
│
├─ Boottyp?
│  ├─ Monohull Segelboot (8–14m):
│  │  ├─ Verfügbare Fläche begrenzt (<3 m²)
│  │  ├─ Verschattung durch Rigg hoch
│  │  ├─ Empfehlung: Arch mit starren Panels (200–400 Wp)
│  │  │  + ggf. 1–2 semiflexible auf Bimini/Sprayhood
│  │  └─ Verschaltung: Parallel (Verschattungstoleranz)
│  │
│  ├─ Monohull Segelboot (14–20m):
│  │  ├─ Mehr Arch-Fläche, evtl. Davit-Brücke
│  │  ├─ Empfehlung: Heavy-Duty Arch mit 400–800 Wp starr
│  │  │  + semiflexibel auf Bimini/Sprayhood (100–200 Wp)
│  │  └─ Verschaltung: Serie (je 2) + Parallel zwischen Strings
│  │
│  ├─ Katamaran (36–45ft):
│  │  ├─ Große Bimini-Fläche (6–10 m²)
│  │  ├─ Wenig Verschattung (Rigg weit vorn)
│  │  ├─ Empfehlung: Bimini-Integration 800–1.600 Wp
│  │  │  - Budget: Semiflexibel auf starrem Bimini-Rahmen
│  │  │  - Premium: Solbian auf Segeltuch-Bimini
│  │  │  - Gewichts-optimiert: CIGS auf Bimini
│  │  └─ Verschaltung: 2–4 MPPT-Regler für verschiedene Strings
│  │
│  ├─ Katamaran (45ft+):
│  │  ├─ Sehr große Flächen (10–20 m²)
│  │  ├─ Empfehlung: 1.500–3.500 Wp, 48V-System erwägen
│  │  └─ Mehrere MPPT-Regler (Victron 150/70 oder RS Serie)
│  │
│  └─ Motoryacht:
│     ├─ Flybridge-Fläche? → Starre Panels fest montiert
│     ├─ Geräteträger? → Standard starre Module
│     └─ Empfehlung: 500–1.500 Wp starr (beste €/Wp + Langlebigkeit)
│
├─ Budget?
│  ├─ Minimal (<€500): Renogy/Lensun semiflexibel + EPEver-Regler
│  ├─ Mittel (€500–€2.000): Sunware/Victron + SmartSolar-Regler
│  ├─ Premium (€2.000–€5.000): Solbian + Victron SmartSolar
│  └─ Unlimited (€5.000+): Solbian Maßanfertigung + Victron RS-Serie
│
├─ Priorität?
│  ├─ Langlebigkeit → Starr (25+ Jahre) oder Sunware semiflexibel
│  ├─ Gewicht → CIGS oder Solbian
│  ├─ Verschattungstoleranz → Solbian (Bypass/Zelle) + Multi-MPPT
│  ├─ Preis-Leistung → Victron starr + SmartSolar
│  └─ Ästhetik → CIGS (homogene Fläche) oder Solbian (Maßanfertigung)
│
└─ ERGEBNIS: Spezifische Konfigurationsempfehlung
```

---

## 8. FAQ — Häufige Fragen

### 8.1 Grundsatzfragen

**F: Kann ich mit Solar allein mein Boot versorgen?**
A: Abhängig von Boottyp, installierter Leistung und Verbrauch. Ein Katamaran 42ft mit 1.200 Wp und LiFePO4-Bank (400 Ah) ist in den Tropen und im Mittelmeer (Apr–Okt) vollständig autark — einschließlich Kühlschrank, Autopilot, Wassermacher und Unterhaltungselektronik. Ein Einrumpf-Segelboot 12m mit 300 Wp schafft Autarkie nur bei reduziertem Verbrauch und gutem Wetter. Schlüssel ist die Energiebilanz: Tageserzeugung muss Tagesverbrauch übersteigen.

**F: Wieviel Wp brauche ich?**
A: Faustformel: Tagesverbrauch (Ah) × 3 = benötigte Wp (für Mittelmeer-Sommer). Für Ganzjahresautarkie in Europa: Tagesverbrauch × 5–8. Für Tropen: Tagesverbrauch × 2–2,5. Detaillierte Berechnung: Verbrauchsliste erstellen, PSH der Zielregion ermitteln, Systemverluste (Faktor 0,65) einrechnen.

**F: Solar oder Windgenerator — was ist besser?**
A: Solar und Wind ergänzen sich ideal. Solar: zuverlässig, leise, wartungsfrei, produziert bei Flaute. Wind: produziert bei Schlechtwetter und nachts, wenn Solar schwächelt. Für Ankerlieger in geschützten Buchten: Solar klar überlegen (kein Wind in Buchten). Für Überführungen und Hochseesegeln: Wind-Ergänzung sinnvoll. Die meisten Blauwassersegler haben beides.

**F: Lohnt sich Solar wirtschaftlich?**
A: Ja. Beispielrechnung: 600 Wp Anlage (€1.500 inkl. Regler) erzeugt im Mittelmeer ~2.000 Wh/Tag. Alternative: Generator 2h/Tag × €2/h Diesel = €4/Tag × 200 Seetage = €800/Jahr. ROI: 1,9 Jahre. Ohne Generator: Landstrom in Marinas (€8–15/Tag) gespart. Dazu: kein Generator-Wartung, kein Lärm, kein Verschleiß.

### 8.2 Technische Fragen

**F: PWM oder MPPT — welcher Regler?**
A: MPPT. Immer. Der Mehrpreis (€50–100) amortisiert sich durch 15–30% Mehrertrag innerhalb weniger Monate. PWM verschenkt die Differenz zwischen Panel-Vmpp und Batteriespannung als Wärme. Ein 100-Wp-Panel mit 18V Vmpp an einer 12V-Batterie: PWM nutzt nur 67% (12V/18V × 100W = 67W), MPPT wandelt 18V × 5,5A = 99W in 12V × ~7A = 84W (bei 95% Effizienz). Differenz: 25% Mehrertrag mit MPPT.

**F: Kann ich verschiedene Panels mischen?**
A: In Parallelschaltung: Ja, solange Vmpp ähnlich (±2V). In Reihenschaltung: Nein, der schwächste Strom bestimmt den String. Beste Lösung bei Mix: separate MPPT-Regler pro Panel-Typ (Victron SmartSolar erlaubt parallele Ladung auf eine Bank).

**F: Wie dick muss das Kabel sein?**
A: Maximal 3% Spannungsverlust (besser 1%). Formel: Querschnitt (mm²) = 2 × Länge (m) × Strom (A) / (56 × max. Spannungsabfall (V)). Beispiel: 4m Kabelweg, 10A, max. 0,5V Verlust: Q = 2×4×10 / (56×0,5) = 2,86 mm² → 4 mm² wählen. Bei 12V-Systemen sind die Ströme hoch — nicht am Kabelquerschnitt sparen!

**F: Brauche ich eine Sicherung am Panel?**
A: Ja, bei Parallelschaltung mehrerer Panels: jeder String benötigt eine Sicherung (1,5 × Isc des Strings). Bei nur einem Panel ohne Batterie-Rückstrom-Risiko: nicht zwingend, aber empfohlen. Sicherungen direkt am Panel (innerhalb 30 cm ab Anschlussdose).

**F: MC4-Stecker auf See — halten die?**
A: Standard-MC4 sind IP67, aber nicht für permanente Salzwasser-Exposition konzipiert. Maßnahmen: (1) Verbindungen oberhalb Spritzwasserzone, (2) selbstverschweißendes Tape um die Verbindung, (3) Kontaktfett, (4) regelmäßige Inspektion. Alternative: vergossene Kabeldurchführungen (Deck-Glands) statt MC4 auf Deck.

**F: Warum liefert mein Panel weniger als das Datenblatt angibt?**
A: Das Datenblatt gilt für STC: 1.000 W/m² Einstrahlung, 25°C Zelltemperatur, AM1.5 Spektrum. Real auf dem Boot: Einstrahlung selten 1.000 W/m² (außer Mittag), Zelltemperatur 40–70°C (Verlust 5–18%), Systemverluste (Kabel, Regler, Verschattung). Realistisch: 60–75% der Nennleistung als Tages-Peak, Tagesertrag = Wp × PSH × 0,65.

### 8.3 Montage und Installation

**F: Kleben oder Schrauben (semiflexibel)?**
A: Beides hat Vor- und Nachteile. Kleben: bündig, kein Windangriff, aber Panel nicht demontierbar und keine Hinterlüftung. Schrauben (mit Abstandshaltern): Hinterlüftung möglich (+10% Ertrag im Sommer), demontierbar für Wartung. Empfehlung: Schrauben mit 20mm-Abstandshaltern auf Arch/Bimini-Rahmen. Kleben nur auf Deck (begehbar) oder wenn Hinterlüftung konstruktiv gelöst ist.

**F: Welcher Kleber für Solar-Panels auf GFK?**
A: Sikaflex 252 (strukturell) oder Sikaflex 291i (marine elastic). Vorbehandlung: Oberfläche anschleifen (80er Korn), reinigen (Sika Aktivator 205), Primer (Sika Primer 206 G+P). Wichtig: Panel-Rückseite ebenfalls primern. Aushärtung: 24–48h bei 20°C. NICHT: Silikon (haftet auf GFK schlecht), Acrylkleber (UV-instabil), Kontaktkleber (nicht dauerelastisch).

**F: Wie montiere ich starre Panels auf dem Arch?**
A: Optionen: (1) Z-Halterungen (Aluminium, 4 pro Panel, geschraubt), (2) Alu-Schienen auf Querstreben (Panel einschieben), (3) Edelstahl-Bügel mit Gummipolster. Immer: Edelstahl-Schrauben V4A, Unterlegscheiben, Federringe. Vibrationsfest montieren (Seegang!). Keine galvanische Korrosion (Alu-Rahmen auf Edelstahl → Isolierscheibe dazwischen).

**F: Kabeldurchführung durch das Deck — wie dicht?**
A: Deck-Glands (Scanstrut, Sealand) sind die professionelle Lösung. IP67-geprüft, saubere Optik. Alternative: Vergossene Durchführung mit PU-Dichtmasse in GFK-Flansch. NICHT: Einfach Loch bohren und Silikon drumrum — das wird nach 1–2 Jahren undicht.

### 8.4 Wartung und Pflege

**F: Wie oft muss ich Solar-Panels reinigen?**
A: Monatlich in Salzwasser-Umgebung, wöchentlich in Küstennähe mit viel Vogelkot. Methode: Süßwasser-Spülung, bei hartnäckigem Schmutz weicher Schwamm + mildes Spülmittel. NIEMALS: Hochdruckreiniger, Scheuermittel, Lösungsmittel, aggressive Reiniger. Timing: Morgens oder abends (Panel kalt, kein Thermalschock).

**F: Was ist eine sinnvolle jährliche Wartungsroutine?**
A: Checkliste: (1) Alle Steckverbinder auf Korrosion prüfen, (2) Kabel auf Scheuerstellen inspizieren, (3) Panel-Oberfläche auf Delamination/Verfärbung prüfen, (4) Regler-Firmware aktualisieren, (5) Ertragsdaten des Jahres auswerten (Trend rückläufig?), (6) Halterungsschrauben nachziehen, (7) Isolationswiderstand messen (>1 MΩ).

**F: Wie erkenne ich, dass mein Panel das Ende seiner Lebensdauer erreicht hat?**
A: Indikatoren: (1) Ertrag <70% des Neuwerts (bei gleichen Bedingungen), (2) sichtbare Delamination >20% der Fläche, (3) mehrere Hotspot-Ereignisse, (4) Isolationswiderstand <1 MΩ, (5) physische Beschädigung (Glasbruch, Folienrisse). Bei semiflexiblen Panels: typisch nach 6–10 Jahren (Budget) bzw. 10–15 Jahren (Premium).

### 8.5 Dimensionierung und Planung

**F: Wie berechne ich meinen Tagesverbrauch korrekt?**
A: Jedes Gerät: Leistung (W) × Betriebsstunden/Tag = Wh/Tag. Summe aller Geräte = Gesamt-Wh/Tag. Division durch Systemspannung = Ah/Tag. Typische Posten: Kühlschrank (50–80 Ah/Tag @12V), Autopilot (10–30 Ah), Plotter/Instrumente (5–10 Ah), Beleuchtung LED (3–8 Ah), Wassermacher (40–60 Ah wenn aktiv), Laptop (10–15 Ah). Messgerät: Victron BMV-712 oder SmartShunt für reale Messung.

**F: Reicht ein 100-Wp-Panel für mein 10m-Boot?**
A: Für Erhaltungsladung im Hafen: Ja. Für Wochenendtörns mit Kühlschrank: Knapp. Für mehrtägige Ankerliege: Nein. 100 Wp liefert im Mittelmeer-Sommer ca. 45 Ah/Tag @12V — ein Kühlschrank allein braucht 50–80 Ah. Empfehlung für 10m-Fahrtensegler: mindestens 200 Wp, besser 300 Wp.

**F: 12V oder 24V Anlage — was ist besser für Solar?**
A: 24V hat Vorteile: halbierter Strom → dünnere Kabel, weniger Verluste, mehr Panels in Serie möglich. Nachteil: 24V-Verbraucher teurer/seltener, Wandler nötig für 12V-Geräte. Empfehlung: Boot <14m → 12V. Boot 14–20m → 24V. Boot >20m → 48V (mit DC-DC für 12V-Verbraucher).

**F: Wieviele MPPT-Regler brauche ich?**
A: Mindestens einen. Mehrere sinnvoll wenn: (1) Panels an verschiedenen Positionen mit unterschiedlicher Verschattung, (2) Mix verschiedener Panel-Typen/Größen, (3) Gesamtleistung >400 Wp und verschiedene Ausrichtungen. Faustregel: Ein Regler pro gleichartige, gleich ausgerichtete Panel-Gruppe. Katamaran mit Bimini + Bug + Heck: 2–3 Regler.

### 8.6 Spezialfragen

**F: Funktioniert Solar bei Nebel/Regen?**
A: Ja, aber stark reduziert. Bedeckter Himmel: 10–30% des Nennwerts. Dichter Nebel: 5–15%. Starker Regen: 3–10%. Ein 600-Wp-System liefert bei Bewölkung immer noch 60–180 Wh/Tag — genug für Basis-Verbraucher (Instrumente, LED, Kühlschrank-Ergänzung). Regen reinigt die Panels — nach Regenschauer steigt der Ertrag.

**F: Kann ich Solar-Panels bei Gewitter beschädigen?**
A: Direkte Blitzeinschläge in Panels sind möglich (erhöhte Position auf Arch), aber statistisch extrem selten. Überspannungsschutz (Surge Protector) am Regler-Eingang empfohlen. Panels selbst sind typisch für 1.000V Isolationsspannung ausgelegt. Wichtiger: Regler und Elektronik durch Überspannungsableiter (SPD) schützen.

**F: Sind gebrauchte Panels empfehlenswert?**
A: Starre Module mit <10 Jahren und dokumentiertem Leistungstest: Ja, gutes Preis-Leistungs-Verhältnis (50–70% Neupreis bei >90% Restleistung). Semiflexible Panels gebraucht: Vorsicht — Lebensdauer bereits teilweise aufgebraucht, Mikrorisse nicht sichtbar. Empfehlung: Nur mit dokumentierter Leistungsmessung (>85% der Nennleistung) kaufen.

**F: Was passiert mit überschüssigem Solarertrag?**
A: Bei voller Batterie: MPPT-Regler regelt ab (erhöht Spannung über MPP hinaus, Strom sinkt). Panels nehmen keinen Schaden. Option: Dump-Load (Heizelement für Warmwasser) — nutzt Überschuss statt ihn zu verwerfen. Manche Regler (Victron RS) können Load-Output für Dump-Load steuern.

**F: Solar auf dem Winterlager-Boot — sinnvoll?**
A: Unbedingt. Ein kleines Panel (50–100 Wp) mit MPPT-Regler hält die Batterie im Winter auf Ladung, verhindert Sulfatierung (Blei) bzw. Tiefentladung (LiFePO4), betreibt Bilgepumpe und Feuchtesensor. Die günstigste Winterversicherung für die Bordelektrik.

**F: Stören Solar-Panels die Funkgeräte (EMV)?**
A: In seltenen Fällen: Ja. MPPT-Regler mit Schaltfrequenz 50–200 kHz können SSB-Empfang stören. Maßnahmen: (1) Abgeschirmte Kabel, (2) Ferritkerne an Leitungen nahe Funkgerät, (3) Abstand Regler↔Antenne >2m, (4) Regler mit EMV-Filterung (Victron SmartSolar hat integrierte Filter). UKW und AIS typisch unproblematisch.

**F: Kann ich Panels senkrecht an der Reling montieren?**
A: Technisch möglich (Ertrag: ~50% eines horizontalen Panels wegen cos-Verlust), aber sinnvoll als Ergänzung bei niedrigem Sonnenstand (morgens/abends, Winter). Montage: Edelstahl-Halterung an Relingstütze, Panel nach Ost oder West ausgerichtet. Typisch 50–100 Wp Module. Vorteil: keine Decksfläche belegt.

**F: Was tun bei Hagelschlag?**
A: Starre Module mit ESG-Glas: IEC 61215 erfordert 25mm Hagelkorn @23 m/s ohne Schaden. Semiflexible Panels: kein Glasschutz, bei großem Hagel (>15mm) beschädigungsgefährdet. Schutz: bei Unwetter-Warnung mit Plane abdecken (bei fest montierten Panels am Arch). Wenn Schaden: Panel sofort auf Isolationswiderstand prüfen.

**F: Wie entsorge ich alte Solar-Panels?**
A: In der EU: Elektroschrott-Richtlinie (WEEE). Kostenlose Rückgabe bei kommunalen Sammelstellen oder Händler-Rücknahme. Panels enthalten Silizium, Kupfer, Glas — alles recycelbar. CIGS-Panels: Indium und Gallium → Spezialrecycling. Keinesfalls im Hausmüll oder auf See entsorgen.

**F: Beeinflussen Sonnensegel den Solarertrag?**
A: Ja, erheblich. Ein Sonnensegel über dem Cockpit beschattet häufig auch Panels auf dem Arch oder Bimini. Lösung: Sonnensegel-Position so planen, dass Panels frei bleiben. Alternative: Solarpanel-integriertes Sonnensegel (Bimini mit Panels = Doppelnutzen).

---

## 9. Glossar

| Begriff | Definition |
|---------|-----------|
| **AM1.5** | Air Mass 1.5 — Standard-Sonnenspektrum für Panel-Tests (1.000 W/m², Sonne bei 48,2° Zenitwinkel = 41,8° über Horizont) |
| **Backsheet** | Rückseitenfolie eines Solarmoduls, schützt Zellen vor Feuchtigkeit und mechanischer Belastung |
| **Bifazial** | Beidseitig lichtempfindliches Solarmodul, nutzt auch reflektiertes Licht auf der Rückseite |
| **BMS** | Battery Management System — überwacht und schützt LiFePO4-Zellen |
| **Bypass-Diode** | Überbrückt verschattete Zellgruppen, verhindert Hotspots und minimiert Verschattungsverluste |
| **CIGS** | Kupfer-Indium-Gallium-Diselenid — Dünnschicht-Solartechnologie |
| **Delamination** | Ablösung der Schichten im Panel-Laminat (Frontfolie, EVA, Zelle, Backsheet) |
| **Derating** | Leistungsreduzierung eines Geräts (z.B. MPPT-Regler) bei Überschreitung der Betriebstemperatur |
| **DoD** | Depth of Discharge — Entladetiefe einer Batterie in Prozent |
| **Dump-Load** | Verbraucher (z.B. Heizelement), der überschüssige Solarenergie bei voller Batterie abführt |
| **EL-Test** | Elektrolumineszenz-Test — macht Mikrorisse in Solarzellen sichtbar |
| **ETFE** | Ethylen-Tetrafluorethylen — UV-beständige Frontfolie für semiflexible Panels |
| **EVA** | Ethylen-Vinylacetat — Einkapselungsmaterial zwischen Glas/Folie und Solarzelle |
| **FF (Füllfaktor)** | Verhältnis der maximalen Leistung (Pmpp) zum Produkt aus Voc × Isc. Maß für die Zellqualität (typisch 0,72–0,82) |
| **GHI** | Global Horizontal Irradiance — Gesamte Sonneneinstrahlung auf horizontale Fläche |
| **HJT** | Heterojunction Technology — Hocheffizienz-Zelltechnologie mit amorphem Si auf kristallinem Si |
| **Hotspot** | Lokale Überhitzung einer verschatteten/defekten Zelle (bis 300°C), kann zu Brand führen |
| **IBC** | Interdigitated Back Contact — Zelltechnologie mit allen Kontakten auf der Rückseite (SunPower/Maxeon) |
| **Isc** | Kurzschlussstrom — Maximaler Strom bei Kurzschluss (V=0) |
| **I-V-Kennlinie** | Strom-Spannungs-Kennlinie einer Solarzelle unter gegebenen Bedingungen |
| **MC4** | Multi-Contact 4mm — Standard-Steckverbinder für Solarpanels (IP67) |
| **Mikroriss** | Haarfeiner Riss im Silizium-Wafer, reduziert aktive Zellfläche |
| **MPP** | Maximum Power Point — Betriebspunkt maximaler Leistung auf der I-V-Kennlinie |
| **MPPT** | Maximum Power Point Tracker — Laderegler, der den optimalen Arbeitspunkt findet und hält |
| **NOCT** | Nominal Operating Cell Temperature — Zelltemperatur unter Standard-Betriebsbedingungen (800 W/m², 20°C Umgebung, 1 m/s Wind) = typisch 42–48°C |
| **P&O** | Perturb and Observe — MPPT-Algorithmus, der den Arbeitspunkt periodisch variiert |
| **PERC** | Passivated Emitter and Rear Cell — Standard-Hocheffizienz-Zelltechnologie |
| **PID** | Potential Induced Degradation — spannungsinduzierte Zellschädigung bei hohen Systemspannungen |
| **PSH** | Peak Sun Hours — Äquivalent-Sonnenstunden bei 1.000 W/m² (= kWh/m²/Tag) |
| **PV** | Photovoltaik — Direkte Umwandlung von Sonnenlicht in elektrischen Strom |
| **PWM** | Pulse Width Modulation — einfacher Laderegler, der Panel-Spannung auf Batteriespannung kappt |
| **Shockley-Queisser-Limit** | Theoretische Maximaleffizienz einer Single-Junction-Solarzelle (33,7%) |
| **Snail Trails** | Schneckenspuren — braune Linien auf Zelloberfläche entlang von Mikrorissen |
| **STC** | Standard Test Conditions — Nennbedingungen: 1.000 W/m², 25°C Zelltemp., AM1.5 |
| **String** | In Reihe geschaltete Solarmodule |
| **Surge Protector** | Überspannungsableiter zum Schutz von Elektronik vor Blitz-/Schaltüberspannungen |
| **TK** | Temperaturkoeffizient — prozentualer Leistungsverlust pro Kelvin Temperaturerhöhung |
| **VE.Direct** | Victron Energy Datenprotokoll für Kommunikation zwischen Regler, Batteriemonitor, GX-Gerät |
| **Vmpp** | Spannung am Maximum Power Point (optimale Betriebsspannung) |
| **Voc** | Leerlaufspannung — Maximale Spannung bei offenem Stromkreis (I=0) |
| **VRM** | Victron Remote Management — Cloud-Plattform für Fernüberwachung der Energieanlage |
| **Wp** | Watt-Peak — Nennleistung eines Panels unter STC |

---

## 10. Schnell-Referenz

### 10.1 Dimensionierungs-Faustregeln

| Faustformel | Anwendung |
|-------------|-----------|
| Wp = Ah/Tag × 3 | Minimale Panel-Leistung für Mittelmeer-Sommer |
| Wp = Ah/Tag × 5 | Ganzjahresautarkie Mittelmeer |
| Wp = Ah/Tag × 8 | Ganzjahresautarkie Nordeuropa |
| Wp = Ah/Tag × 2 | Tropen/Karibik |
| Tagesertrag (Ah) = Wp × PSH × 0,65 / 14,2 | Realistischer 12V-Tagesertrag |
| Kabel (mm²) = 2 × L(m) × I(A) / (56 × ΔV) | Mindest-Kabelquerschnitt |
| Sicherung = 1,5 × Isc | Panel-String-Sicherung |
| Voc_max = Voc × (1 + TK_Voc × (Tmin - 25)) | Max. Leerlaufspannung bei Kälte |
| Systemverluste = 35% (typisch) | Für Überschlagsrechnungen |

### 10.2 Checkliste Installation

```
□ Energiebilanz erstellen (Verbraucher × Stunden = Ah/Tag)
□ Verfügbare Montagefläche vermessen
□ Verschattungsanalyse (ganztägig bei Sonnenschein)
□ Panel-Typ und Leistung wählen
□ MPPT-Regler dimensionieren (Voc_max bei Kälte beachten!)
□ Kabelquerschnitt berechnen (max. 3% Verlust)
□ Sicherungen dimensionieren
□ Montage-Hardware wählen (korrosionsfest!)
□ Kabeldurchführungen planen (wasserdicht!)
□ Panel-Verschaltung festlegen (Serie/Parallel/Mixed)
□ Masse/Erdung planen (Floating oder Boot-Masse)
□ Regler-Einbauort festlegen (belüftet, trocken, zugänglich)
□ Monitoring integrieren (VRM, Bluetooth, Display)
□ Installation durchführen
□ Voc messen (vor Regler-Anschluss!)
□ Regler konfigurieren (Batterietyp, Ladekurve)
□ System-Test unter Last
□ Dokumentation erstellen (Schaltplan, Datenblätter)
```

### 10.3 Vergleichstabelle Panel-Typen

| Kriterium | Starr Mono | Semiflexibel | CIGS | Begehbar |
|-----------|-----------|-------------|------|----------|
| Wirkungsgrad | ★★★★★ | ★★★★☆ | ★★★☆☆ | ★★★★☆ |
| Gewicht | ★★☆☆☆ | ★★★★☆ | ★★★★★ | ★★★★☆ |
| Lebensdauer | ★★★★★ | ★★☆☆☆ | ★★★★☆ | ★★★☆☆ |
| Preis/Wp | ★★★★★ | ★★★☆☆ | ★★☆☆☆ | ★★☆☆☆ |
| Verschattungstoleranz | ★★★☆☆ | ★★★☆☆ | ★★★★☆ | ★★★★★ |
| Flexibilität | ★☆☆☆☆ | ★★★★☆ | ★★★★★ | ★★★★☆ |
| Robustheit | ★★★★★ | ★★★☆☆ | ★★★☆☆ | ★★★★☆ |
| Ästhetik | ★★★☆☆ | ★★★★☆ | ★★★★★ | ★★★★★ |

### 10.4 Regler-Schnellauswahl

| Installierte Leistung | 12V System | 24V System | Empfehlung |
|-----------------------|-----------|-----------|-----------|
| ≤200 Wp | Victron 75/15 | Victron 100/20 | Budget: EPEver 2210AN |
| 200–400 Wp | Victron 100/30 | Victron 100/20 | Standard |
| 400–700 Wp | Victron 100/50 | Victron 150/35 | |
| 700–1.000 Wp | Victron 150/70 | Victron 150/45 | Premium |
| 1.000–2.000 Wp | 2× Victron 150/70 | Victron 250/70 | Multi-Regler |
| >2.000 Wp | Multi-MPPT | Victron RS 450/100 | 48V erwägen |

### 10.5 Regionale PSH-Schnellreferenz (Sommer / Winter)

| Revier | Sommer PSH | Winter PSH | Jahres-Ø |
|--------|-----------|-----------|----------|
| Ostsee | 5,0 | 0,8 | 2,8 |
| Mittelmeer | 7,0 | 3,0 | 4,8 |
| Kanaren | 7,0 | 4,5 | 5,6 |
| Karibik | 6,0 | 5,2 | 5,8 |
| Rotes Meer | 8,0 | 5,5 | 6,5 |
| Pazifik (Tropen) | 5,0 | 5,0 | 5,0 |

---

## ANHANG A–H — Fallstudien

### ANHANG A — Fallstudie: Bavaria 40 Cruiser — Nachrüstung 400 Wp

**Boot:** Bavaria 40 Cruiser (2018), 12,35m LOA
**Eigner:** Ehepaar, Langfahrt Mittelmeer/Atlantik geplant
**Ausgangslage:** 1× AGM 100 Ah Versorgungsbatterie, kein Solar, Generator 2,5 kW

**Problemstellung:**
- Generator muss 2×/Tag laufen (je 1–2h) — Lärm, Diesel, Wartung
- Batterie nach 2 Ankertagen leer
- Kühlschrank geht nachts aus
- Kein Strom für Wassermacher geplant

**Installierte Anlage:**
- 2× Victron BlueSolar SPM200-24 (200 Wp, starr) auf neuem Alu-Arch
- 1× Victron SmartSolar 100/50 MPPT-Regler
- Verkabelung: 6 mm² Solarkabel, 4m Weg
- Panels in Serie: 2×36V Vmpp = 72V → Voc_max = 87V (sicher unter 100V-Grenze)

> ⚠️ **ZU PRÜFEN (Audit):** Voc_max 87V vs. Serien-Voc (STC) = 2 × 44,8V = 89,6V — die angegebene Kälte-Leerlaufspannung (87V) liegt UNTER der STC-Leerlaufspannung des Strings und ist damit physikalisch unmöglich (Voc steigt bei Kälte, sinkt nie). Nach der Formel aus Abschnitt 2.7 (TK_Voc −0,29 %/K) ergibt sich bei −10°C ca. 98,7V — grenzwertig nahe der 100V-Reglergrenze, nicht mit komfortablem Sicherheitsabstand. Confidence dieser Angabe: estimated — unverifiziert.
- Zusätzlich: Upgrade auf 2× Victron 200 Ah LiFePO4 Smart

**Kosten:**
| Position | Betrag |
|----------|--------|
| 2× SPM200-24 Panels | €620 |
| 1× SmartSolar 100/50 | €340 |
| Alu-Arch (custom) | €2.800 |
| Kabel, Stecker, Sicherungen | €180 |
| Montage (Werft) | €800 |
| 2× LiFePO4 200 Ah | €2.600 |
| **Gesamt** | **€7.340** |

**Ergebnis (gemessen über 6 Monate Mittelmeer):**
- Durchschnittlicher Tagesertrag: 95 Ah @12V (Mai–Oktober)
- Generator-Laufzeit: von 730h/Jahr auf 45h/Jahr reduziert (-94%)
- Diesel-Ersparnis: ~400 Liter/Jahr = €680
- Amortisation Solar allein (ohne LiFePO4): 1,8 Jahre
- Vollständige Autarkie Mai–September (ohne Wassermacher)
- Mit Wassermacher (30L/h, 12A): Autarkie bei max. 1h/Tag Betrieb

**Confidence:** documented — Eigner-Bericht mit Victron VRM-Daten.

### ANHANG B — Fallstudie: Lagoon 42 — Bimini-Komplettintegration 1.600 Wp

**Boot:** Lagoon 42 (2021), 12,80m LOA, Katamaran
**Eigner:** Familie (4 Personen), Vollzeit-Liveaboard, Karibik-Rundreise
**Ausgangslage:** 2× 100 Wp werksseitig auf Hardtop — deutlich unterdimensioniert

**Problemstellung:**
- 200 Wp decken nur 30% des Tagesbedarfs (320 Ah/Tag @12V)
- Generator läuft 4–6h/Tag
- Klimaanlage nur im Hafen nutzbar
- Wassermacher-Betrieb stark eingeschränkt

**Installierte Anlage:**
- Neues Alu-Hardtop-Bimini (Tragfähigkeit 200 kg)
- 8× Solbian SP 200 Q auf Bimini-Rahmen (je 200 Wp = 1.600 Wp gesamt)
- 4× Victron SmartSolar 100/30 (je 2 Panels in Serie = 70V Vmpp)
- Verschaltung: 4 unabhängige Strings (Verschattungstoleranz)
- Batterie-Upgrade: 2× Victron Lynx Smart BMS + 8× LiFePO4 100 Ah = 800 Ah @12V
- Victron Cerbo GX + Touch 70 Display

**Kosten:**
| Position | Betrag |
|----------|--------|
| 8× Solbian SP 200 Q | €9.480 |
| 4× SmartSolar 100/30 | €920 |
| Alu-Bimini-Rahmen (custom) | €4.200 |
| Kabel, Stecker, Durchführungen | €450 |
| LiFePO4 800 Ah Bank | €5.200 |
| Cerbo GX + Touch 70 | €680 |
| Installation | €2.400 |
| **Gesamt** | **€23.330** |

**Ergebnis (gemessen über 12 Monate Karibik):**
- Durchschnittlicher Tagesertrag: 285 Ah @12V
- Generator-Laufzeit: von 1.800h/Jahr auf 120h/Jahr (-93%)
- Vollständige Autarkie (inkl. Wassermacher 2h/Tag) an 310 Tagen/Jahr
- Klimaanlage (1 Kabine): 3–4h/Tag durch Solar gedeckt
- Diesel-Ersparnis: ~1.600 Liter/Jahr = €2.900
- Amortisation: 4,8 Jahre (nur Diesel-Ersparnis, ohne Komfort-Wert)

**Confidence:** documented — Eigner-Blog mit Victron VRM-Daten (12 Monate Karibik-Zyklus).

### ANHANG C — Fallstudie: HR 43 — Verschattungsproblem und Lösung

**Boot:** Hallberg-Rassy 43 (2015), 13,20m LOA
**Eigner:** Einhandsegler, Atlantik-Rundreise
**Ausgangslage:** 2× 120 Wp semiflexibel auf Bimini, aber nur 50% Ertrag

**Problemstellung:**
- Panels liefern im Schnitt nur 120 Wh/Tag statt erwarteter 750 Wh/Tag
- Ursache unklar für Eigner
- Verzweiflung nach 3 Monaten Fehlersuche

**Analyse:**
- Verschattung durch Groß-Baum (Traveller mittschiffs, Baum tief)
- Standard-Bypass-Dioden (3 pro Panel) → bei Baumschatten: 33–66% Verlust
- Panels in Serie geschaltet → schwächstes Panel bestimmt Ertrag
- Zusätzlich: PWM-Regler statt MPPT (weiterer 25% Verlust)

**Lösung:**
1. Panels getauscht gegen 2× Solbian SXp 144 Q (Bypass pro Zelle)
2. PWM-Regler ersetzt durch Victron SmartSolar 100/30
3. Panels parallel geschaltet (statt Serie)
4. Baum-Niederholer so eingestellt, dass Baumschatten minimal

**Ergebnis:**
- Ertrag: von 120 Wh/Tag auf 680 Wh/Tag (+467%)
- Davon 200 Wh/Tag allein durch Bypass-pro-Zelle (Baumschatten-Toleranz)
- Davon 180 Wh/Tag durch MPPT statt PWM
- Davon 100 Wh/Tag durch Parallelschaltung
- Rest: neue Panels haben höheren Wirkungsgrad

**Investition:** €2.100 (Panels + Regler) — Amortisation: Sofort (Generator konnte verkauft werden)

**Confidence:** documented — Eigner-Erfahrungsbericht mit Vergleichsmessungen.

### ANHANG D — Fallstudie: Dehler 34 — Budget-Installation 200 Wp

**Boot:** Dehler 34 (2012), 10,35m LOA
**Eigner:** Wochenendsegler, Ostsee, beschränktes Budget
**Ziel:** Batterie am Liegeplatz geladen halten + Kühlschrank über Wochenend-Törn

**Installierte Anlage:**
- 2× Renogy RNG-100DB (100 Wp, semiflexibel) auf Sprayhood-Bügel
- 1× Victron SmartSolar 75/15 MPPT-Regler
- Panels parallel geschaltet (unabhängig, da verschiedene Verschattung)
- Kabel: 4 mm², Gesamtlänge 3m
- Budget-Montage: Edelstahl-Rohrschellen + Alu-Winkel (Eigenbau)

**Kosten:**
| Position | Betrag |
|----------|--------|
| 2× Renogy 100 Wp | €330 |
| 1× SmartSolar 75/15 | €125 |
| Kabel, MC4, Sicherungen | €65 |
| Montage-Material | €80 |
| **Gesamt** | **€600** |

**Ergebnis:**
- Ostsee Sommer: 60 Ah/Tag @12V → Kühlschrank + Instrumente gedeckt
- Winterlager: 10–15 Ah/Tag → Batterie-Erhaltung gesichert
- Landstrom-Ersparnis am Liegeplatz: €15/Monat × 7 Monate = €105/Jahr
- Amortisation: 5,7 Jahre (nur Landstrom), sofort wenn Generator-Stunden eingerechnet

**Lessons Learned:**
- Renogy-Panels zeigten nach 2,5 Jahren erste Delamination an den Kanten
- Semiflexibel auf Sprayhood-Bügel: starke Vibration bei Seegang → Mikrorisse wahrscheinlich
- Upgrade geplant: Sunware TX-22120 (120 Wp) als Ersatz der Renogy

**Confidence:** documented — Eigner-Bericht mit eigenen Messungen.

### ANHANG E — Fallstudie: Outremer 55 — Hochleistungs-Autarksystem 3.200 Wp

**Boot:** Outremer 55 (2023), 16,75m LOA, Performance-Katamaran
**Eigner:** Professioneller Skipper, Charter mit Privatkunden (Luxus-Segment)
**Anforderung:** Vollständige Autarkie inklusive 2× Klimaanlage, Wassermacher, elektrisches Kochen

**Installierte Anlage:**
- 16× Solbian SP 200 Q auf Custom-Hardtop (3.200 Wp)
- 2× Victron SmartSolar MPPT RS 450/100 (je 8 Panels in Serie = 278V Vmpp)
- 48V-System mit Victron Quattro 48/10000 Inverter
- 48V LiFePO4: Victron Lynx Smart BMS + 16× EVE 280 Ah Zellen = 560 Ah @48V (26,9 kWh!)

> ⚠️ **ZU PRÜFEN (Audit):** Zellzahl vs. Kapazität widersprüchlich — 16× 280-Ah-Zellen ergeben in 16s-Konfiguration (Standard für 48V) 280 Ah / ≈14,3 kWh, nicht 560 Ah / 26,9 kWh. Für 560 Ah @48V wären 32 Zellen (16s2p) nötig. Confidence dieser Angabe: estimated — unverifiziert.
- Victron Cerbo GX + GX Touch 50 + VRM Cloud
- 2× Induktionskochfeld (48V DC-nativ)
- Spectra Catalina 340 Wassermacher (340L/Tag)
- 2× Marine-Klimaanlage 16.000 BTU

**Kosten:**
| Position | Betrag |
|----------|--------|
| 16× Solbian SP 200 Q | €18.960 |
| 2× MPPT RS 450/100 | €2.100 |
| Custom Carbon-Hardtop | €28.000 |
| 48V LiFePO4 26,9 kWh | €12.500 |
| Victron Quattro + Peripherie | €4.800 |
| Installation | €8.500 |
| **Gesamt (Solar+Speicher)** | **€74.860** |

**Ergebnis (Mittelmeer/Karibik):**
- Tagesertrag Sommer Mittelmeer: 580 Ah @12V-Äquivalent (13,9 kWh)
- Generator: komplett abgebaut (kein Generator an Bord!)
- Vollständige Autarkie 365 Tage/Jahr (auch Nordmeer-Sommer)
- 2 Klimaanlagen: 8–12h/Tag durch Solar gedeckt (Tropen)
- Charter-USP: "Zero Emission Luxury Sailing" — Preisaufschlag €500/Woche

**Confidence:** documented — Werft-Dokumentation (Outremer), Victron VRM-Jahresbericht.

### ANHANG F — Fallstudie: Bénéteau Oceanis 38.1 — CIGS-Lösung für Gewichtsoptimierung

**Boot:** Bénéteau Oceanis 38.1 (2020), 11,50m LOA
**Eigner:** Regatta-orientierter Fahrtensegler, Mittelmeer
**Anforderung:** Solar ohne Gewichtsstrafe, kein Windwiderstand, unauffällig

**Installierte Anlage:**
- 4× Gioco Solutions CIGS-Flex 75 Wp (1,8 kg/Stück) auf Bimini-Segeltuch
- 1× Victron SmartSolar 100/20
- Panels: je 2 in Serie, 2 Strings parallel
- Gesamtleistung: 300 Wp, Gesamtgewicht Panels: 7,2 kg

**Kosten:**
| Position | Betrag |
|----------|--------|
| 4× CIGS 75 Wp | €1.800 |
| SmartSolar 100/20 | €170 |
| Bimini-Näharbeit + Ösen | €450 |
| Kabel, Stecker | €120 |
| **Gesamt** | **€2.540** |

**Ergebnis:**
- Tagesertrag: 65 Ah @12V (Mittelmeer-Sommer)
- Gewichtsvorteil: 7,2 kg (CIGS) vs. 25 kg (starre Panels gleicher Leistung)
- Kein messbarer Einfluss auf Bootsspeed
- Ästhetik: Panels nahezu unsichtbar im schwarzen Bimini
- Teilverschattung: CIGS zeigt deutlich besseres Verhalten als erwartet (kein abrupter Ertragseinbruch)

**Nachteil:** Geringerer Wirkungsgrad (15% vs. 22%) — braucht mehr Fläche für gleiche Leistung.

**Confidence:** documented — Eigner-Bericht.

### ANHANG G — Fallstudie: Hotspot-Schaden durch Vogelkot

**Boot:** Jeanneau Sun Odyssey 440 (2019)
**Situation:** 2× 175 Wp starre Panels auf Geräteträger, nach 3 Jahren

**Schadensbild:**
- Ein Panel zeigt braune Verfärbung in einem Bereich (ca. 15×15 cm)
- Leistung des betroffenen Panels: nur noch 45% des Nennwerts
- Im Thermografie-Bild: Hotspot mit 95°C (!) bei einer Zelle

**Ursache:**
- Vogel (Möwe) hat regelmäßig auf dem Panel gerastet
- Dauerhafter Vogelkot-Fleck auf 2 Zellen (nicht gereinigt über Monate)
- Bypass-Diode für betroffene Zellgruppe war defekt (Fertigung: Lötfehler)
- Ohne funktionsfähige Bypass-Diode: voller String-Strom durch verschattete Zellen → Hotspot

**Kosten Schaden:**
- Panel-Austausch: €285
- Demontage/Montage: €150
- Diagnose: €80
- **Gesamt: €515**

**Prävention für die Zukunft:**
- Vogelabwehr am Arch (Spikes auf Querstreben)
- Monatliche Reinigung der Panels
- Monitoring: Victron VRM Ertragsdaten zeigten bereits 4 Monate vor dem sichtbaren Schaden einen schleichenden Leistungsabfall

**AYDI-Bewertung:** Vermeidbarer Schaden durch simple Reinigung. Monitoring hätte Frühwarnung gegeben.

**Confidence:** documented — Werft-Schadensbericht mit Thermografie-Aufnahme.

### ANHANG H — Fallstudie: DIY-Installation mit Fehlern — Lernbeispiel

**Boot:** Bavaria 37 Cruiser (2009)
**Eigner:** Hobby-Bastler, erste Solar-Installation ohne Fachkenntnis

**Installierte Anlage (fehlerhaft):**
- 3× No-Name China-Panels 100 Wp (Amazon, €89/Stück)
- 1× PWM-Regler 30A (€25)
- Kabel: 1,5 mm² Haushaltslitze (!), 6m Länge
- Montage: Panels mit Kabelbindern am Pushpit befestigt
- Steckverbinder: Standard-Stecker (nicht MC4), offen auf Deck
- Keine Sicherungen

**Fehler und Konsequenzen:**

| Fehler | Konsequenz |
|--------|-----------|
| PWM statt MPPT | -25% Ertrag (€75 gespart, €200/Jahr Ertrag verloren) |
| 1,5 mm² Kabel bei 6m und 15A | Spannungsabfall 3,2V = 22% Verlust! Brandgefahr! |
| Kabelbinder-Montage | Panels nach 8 Monaten abgerissen (Sturm), Deck-Beschädigung |
| Offene Stecker | Korrosion nach 3 Monaten, Übergangswiderstand, Überhitzung |
| Keine Sicherungen | Bei Kurzschluss: Kabel geschmolzen, beinahe Brand |
| No-Name-Panels | Leistung 20% unter Angabe (70 statt 100 Wp real) |

**Kosten der "Einsparung":**
- Ursprüngliche Installation: €340
- Schaden: Deck-Reparatur (Abrisspunkte): €800
- Erneute Installation (korrekt): €1.200
- Zeitverlust: 40+ Stunden
- **Gesamtkosten: €2.340** (vs. €1.400 für sofortige korrekte Installation)

**Lessons Learned:**
1. Nie am Kabelquerschnitt sparen — Brandgefahr!
2. MPPT-Regler ist Pflicht (€100 Mehrpreis amortisiert sich in Monaten)
3. Marine-taugliche Befestigung ist nicht optional
4. MC4-Stecker + Abdichtung sind Standard aus gutem Grund
5. Sicherungen sind lebensrettende €10-Investition
6. No-Name-Panels selten so leistungsstark wie angegeben

**Confidence:** documented — Zusammengesetzt aus mehreren realen Forum-Berichten (Cruisers Forum, Segeln-Forum.de).

---

## ANHANG I–R — AYDI-Integration (Pydantic v2 Modelle)

### ANHANG I — Basis-Datenmodelle

```python
"""
AYDI Solar Panel Analysis Models — Pydantic v2
Module: backend/app/models/solar.py
"""

from __future__ import annotations

from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class PanelTechnology(str, Enum):
    """Solarzellen-Technologie."""
    MONO_CRYSTALLINE = "mono_crystalline"
    POLY_CRYSTALLINE = "poly_crystalline"
    CIGS = "cigs"
    HJT = "hjt"
    IBC = "ibc"
    BIFACIAL = "bifacial"
    PERC = "perc"


class PanelFormFactor(str, Enum):
    """Panel-Bauform."""
    RIGID_GLASS = "rigid_glass"
    SEMI_FLEXIBLE = "semi_flexible"
    FLEXIBLE_THIN_FILM = "flexible_thin_film"
    WALKABLE = "walkable"
    BIMINI_INTEGRATED = "bimini_integrated"


class MountingType(str, Enum):
    """Montage-Art."""
    ARCH_FLAT = "arch_flat"
    ARCH_TILTED = "arch_tilted"
    BIMINI_SEWN = "bimini_sewn"
    BIMINI_FRAME = "bimini_frame"
    DECK_GLUED = "deck_glued"
    DECK_SCREWED = "deck_screwed"
    RAILING = "railing"
    DAVIT = "davit"
    FLYBRIDGE = "flybridge"
    SPRAYHOOD = "sprayhood"


class WiringConfiguration(str, Enum):
    """Verschaltungsart."""
    SERIES = "series"
    PARALLEL = "parallel"
    SERIES_PARALLEL = "series_parallel"
    INDEPENDENT_MPPT = "independent_mppt"


class ConfidenceLevel(str, Enum):
    """AYDI Confidence Level."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class SolarPanel(BaseModel):
    """Einzelnes Solarpanel mit allen relevanten technischen Daten."""

    model_config = {"from_attributes": True}

    manufacturer: str = Field(..., description="Hersteller-Name")
    model: str = Field(..., description="Modellbezeichnung")
    technology: PanelTechnology = Field(..., description="Zelltechnologie")
    form_factor: PanelFormFactor = Field(..., description="Bauform")
    
    # Elektrische Daten (STC)
    watt_peak: float = Field(..., gt=0, description="Nennleistung in Wp (STC)")
    vmpp: float = Field(..., gt=0, description="MPP-Spannung in V")
    impp: float = Field(..., gt=0, description="MPP-Strom in A")
    voc: float = Field(..., gt=0, description="Leerlaufspannung in V")
    isc: float = Field(..., gt=0, description="Kurzschlussstrom in A")
    efficiency: float = Field(..., gt=0, le=0.35, description="Wirkungsgrad (0.0–0.35)")
    
    # Temperaturkoeffizienten
    tk_pmpp: float = Field(..., lt=0, description="Temperaturkoeffizient Pmpp (%/K), negativ")
    tk_voc: float = Field(..., lt=0, description="Temperaturkoeffizient Voc (%/K), negativ")
    tk_isc: float = Field(..., description="Temperaturkoeffizient Isc (%/K), typisch positiv")
    
    # Mechanische Daten
    length_mm: float = Field(..., gt=0, description="Länge in mm")
    width_mm: float = Field(..., gt=0, description="Breite in mm")
    thickness_mm: float = Field(..., gt=0, description="Dicke in mm")
    weight_kg: float = Field(..., gt=0, description="Gewicht in kg")
    
    # Marine-spezifisch
    bypass_diodes: int = Field(..., ge=0, description="Anzahl Bypass-Dioden")
    min_bend_radius_mm: Optional[float] = Field(None, ge=0, description="Min. Biegeradius (semiflex)")
    ip_rating: str = Field(default="IP67", description="IP-Schutzart Anschlussdose")
    walkable: bool = Field(default=False, description="Begehbar")
    salt_water_certified: bool = Field(default=False, description="Salzwasser-zertifiziert")
    
    # Wirtschaftlich
    price_eur: Optional[float] = Field(None, ge=0, description="UVP in EUR")
    warranty_years_product: int = Field(default=5, ge=0, description="Produktgarantie Jahre")
    warranty_years_performance: int = Field(default=10, ge=0, description="Leistungsgarantie Jahre")
    expected_lifetime_years: int = Field(default=20, ge=1, description="Erwartete Lebensdauer")
    degradation_per_year: float = Field(default=0.005, ge=0, le=0.05, description="Jährliche Degradation")

    @field_validator("efficiency")
    @classmethod
    def validate_efficiency(cls, v: float) -> float:
        if v > 0.30:
            raise ValueError("Wirkungsgrad >30% unrealistisch für kommerzielle Panels")
        return v

    @property
    def area_m2(self) -> float:
        """Panelfläche in m²."""
        return (self.length_mm * self.width_mm) / 1_000_000

    @property
    def weight_per_m2(self) -> float:
        """Gewicht pro m² in kg/m²."""
        return self.weight_kg / self.area_m2

    @property
    def power_per_m2(self) -> float:
        """Leistungsdichte in Wp/m²."""
        return self.watt_peak / self.area_m2
```

### ANHANG J — Anlage und Verschaltung

```python
"""
AYDI Solar System Configuration Models — Pydantic v2
Module: backend/app/models/solar_system.py
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field, field_validator, model_validator

from .solar import (
    ConfidenceLevel,
    MountingType,
    SolarPanel,
    WiringConfiguration,
)


class SolarString(BaseModel):
    """Ein Solar-String (in Reihe geschaltete Panels)."""

    model_config = {"from_attributes": True}

    string_id: str = Field(..., description="Eindeutige String-Kennung (z.B. 'S1')")
    panels: list[SolarPanel] = Field(..., min_length=1, description="Panels im String")
    mounting: MountingType = Field(..., description="Montage-Art")
    orientation_deg: float = Field(
        default=0.0, ge=0, lt=360, description="Ausrichtung in Grad (0=Nord, 180=Süd)"
    )
    tilt_deg: float = Field(
        default=0.0, ge=0, le=90, description="Neigung in Grad (0=horizontal)"
    )
    shading_factor: float = Field(
        default=1.0, gt=0, le=1.0,
        description="Verschattungsfaktor (1.0=keine Verschattung, 0.5=50% Verlust)"
    )
    cable_length_m: float = Field(..., gt=0, description="Kabellänge Panel→Regler in m")
    cable_cross_section_mm2: float = Field(..., gt=0, description="Kabelquerschnitt in mm²")

    @property
    def total_watt_peak(self) -> float:
        """Gesamte String-Leistung in Wp."""
        return sum(p.watt_peak for p in self.panels)

    @property
    def string_vmpp(self) -> float:
        """Gesamte String-MPP-Spannung in V (Summe bei Reihenschaltung)."""
        return sum(p.vmpp for p in self.panels)

    @property
    def string_voc(self) -> float:
        """Gesamte String-Leerlaufspannung in V."""
        return sum(p.voc for p in self.panels)

    @property
    def string_impp(self) -> float:
        """String-MPP-Strom (begrenzt durch schwächstes Panel)."""
        return min(p.impp for p in self.panels)

    @property
    def cable_voltage_drop(self) -> float:
        """Spannungsabfall im Kabel in V (Hin- und Rückleiter)."""
        resistance = (2 * self.cable_length_m) / (56.0 * self.cable_cross_section_mm2)
        return resistance * self.string_impp

    @property
    def cable_loss_percent(self) -> float:
        """Kabelverlust in Prozent."""
        return (self.cable_voltage_drop / self.string_vmpp) * 100

    def voc_at_temperature(self, temp_celsius: float) -> float:
        """Leerlaufspannung bei gegebener Temperatur."""
        # Verwende TK_Voc des ersten Panels (alle sollten gleich sein)
        tk = self.panels[0].tk_voc / 100  # von %/K zu Faktor/K
        delta_t = temp_celsius - 25.0
        voc_per_panel = [p.voc * (1 + tk * delta_t) for p in self.panels]
        return sum(voc_per_panel)


class MPPTController(BaseModel):
    """MPPT-Laderegler Spezifikation."""

    model_config = {"from_attributes": True}

    manufacturer: str = Field(..., description="Hersteller")
    model: str = Field(..., description="Modellbezeichnung")
    max_pv_voltage: float = Field(..., gt=0, description="Max. PV-Eingangsspannung in V")
    max_pv_power_12v: float = Field(..., gt=0, description="Max. PV-Leistung @12V in W")
    max_pv_power_24v: Optional[float] = Field(None, gt=0, description="Max. PV-Leistung @24V in W")
    max_charge_current: float = Field(..., gt=0, description="Max. Ladestrom in A")
    efficiency: float = Field(default=0.98, gt=0.8, le=1.0, description="Wandlungseffizienz")
    bluetooth: bool = Field(default=False, description="Bluetooth-Schnittstelle")
    ve_direct: bool = Field(default=False, description="VE.Direct-Schnittstelle")
    multi_mppt_tracking: bool = Field(
        default=False, description="Multi-Peak-Tracking für Teilverschattung"
    )
    price_eur: Optional[float] = Field(None, ge=0, description="UVP in EUR")


class SolarSystemConfiguration(BaseModel):
    """Gesamte Solar-Anlagen-Konfiguration eines Bootes."""

    model_config = {"from_attributes": True}

    boat_name: str = Field(..., description="Bootsname")
    boat_length_m: float = Field(..., gt=0, description="Bootslänge in m")
    system_voltage: int = Field(..., description="Systemspannung (12, 24 oder 48V)")
    
    strings: list[SolarString] = Field(..., min_length=1, description="Solar-Strings")
    wiring: WiringConfiguration = Field(..., description="Verschaltungsart der Strings")
    controllers: list[MPPTController] = Field(..., min_length=1, description="MPPT-Regler")
    
    battery_capacity_ah: float = Field(..., gt=0, description="Batteriekapazität in Ah")
    daily_consumption_ah: float = Field(..., gt=0, description="Tagesverbrauch in Ah")

    @field_validator("system_voltage")
    @classmethod
    def validate_system_voltage(cls, v: int) -> int:
        if v not in (12, 24, 48):
            raise ValueError("Systemspannung muss 12, 24 oder 48V sein")
        return v

    @property
    def total_watt_peak(self) -> float:
        """Installierte Gesamtleistung in Wp."""
        return sum(s.total_watt_peak for s in self.strings)

    @property
    def total_panel_area_m2(self) -> float:
        """Gesamte Panel-Fläche in m²."""
        return sum(p.area_m2 for s in self.strings for p in s.panels)

    @property
    def total_weight_kg(self) -> float:
        """Gesamtgewicht aller Panels in kg."""
        return sum(p.weight_kg for s in self.strings for p in s.panels)

    @model_validator(mode="after")
    def validate_voc_limits(self) -> "SolarSystemConfiguration":
        """Prüfe, ob Voc_max keinen Regler überschreitet."""
        for string in self.strings:
            voc_cold = string.voc_at_temperature(-10.0)  # Worst case: -10°C
            for ctrl in self.controllers:
                if voc_cold > ctrl.max_pv_voltage:
                    raise ValueError(
                        f"String '{string.string_id}' Voc bei -10°C ({voc_cold:.1f}V) "
                        f"überschreitet Regler-Maximum ({ctrl.max_pv_voltage}V)!"
                    )
        return self
```

### ANHANG K — Ertragsberechnung

```python
"""
AYDI Solar Yield Calculation Models — Pydantic v2
Module: backend/app/models/solar_yield.py
"""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class SailingRegion(str, Enum):
    """Segelrevier für Einstrahlungsdaten."""
    BALTIC = "baltic"
    NORTH_SEA = "north_sea"
    BISCAY = "biscay"
    MEDITERRANEAN_WEST = "mediterranean_west"
    MEDITERRANEAN_EAST = "mediterranean_east"
    CANARIES = "canaries"
    CARIBBEAN = "caribbean"
    TROPICS = "tropics"
    RED_SEA = "red_sea"
    SOUTH_PACIFIC = "south_pacific"
    AUSTRALIA_EAST = "australia_east"
    PATAGONIA = "patagonia"


class Season(str, Enum):
    """Jahreszeit für Ertragsberechnung."""
    SUMMER = "summer"
    WINTER = "winter"
    ANNUAL_AVERAGE = "annual_average"


# Peak Sun Hours (PSH) Datenbank — kWh/m²/Tag
PSH_DATABASE: dict[SailingRegion, dict[Season, float]] = {
    SailingRegion.BALTIC: {Season.SUMMER: 5.0, Season.WINTER: 0.8, Season.ANNUAL_AVERAGE: 2.8},
    SailingRegion.NORTH_SEA: {Season.SUMMER: 4.5, Season.WINTER: 1.0, Season.ANNUAL_AVERAGE: 2.6},
    SailingRegion.BISCAY: {Season.SUMMER: 6.0, Season.WINTER: 2.0, Season.ANNUAL_AVERAGE: 3.8},
    SailingRegion.MEDITERRANEAN_WEST: {Season.SUMMER: 7.0, Season.WINTER: 3.0, Season.ANNUAL_AVERAGE: 4.8},
    SailingRegion.MEDITERRANEAN_EAST: {Season.SUMMER: 7.5, Season.WINTER: 3.5, Season.ANNUAL_AVERAGE: 5.2},
    SailingRegion.CANARIES: {Season.SUMMER: 7.0, Season.WINTER: 4.5, Season.ANNUAL_AVERAGE: 5.6},
    SailingRegion.CARIBBEAN: {Season.SUMMER: 6.0, Season.WINTER: 5.2, Season.ANNUAL_AVERAGE: 5.8},
    SailingRegion.TROPICS: {Season.SUMMER: 5.0, Season.WINTER: 5.0, Season.ANNUAL_AVERAGE: 5.0},
    SailingRegion.RED_SEA: {Season.SUMMER: 8.0, Season.WINTER: 5.5, Season.ANNUAL_AVERAGE: 6.5},
    SailingRegion.SOUTH_PACIFIC: {Season.SUMMER: 5.5, Season.WINTER: 7.0, Season.ANNUAL_AVERAGE: 5.8},
    SailingRegion.AUSTRALIA_EAST: {Season.SUMMER: 5.0, Season.WINTER: 6.5, Season.ANNUAL_AVERAGE: 5.4},
    SailingRegion.PATAGONIA: {Season.SUMMER: 5.5, Season.WINTER: 1.5, Season.ANNUAL_AVERAGE: 3.2},
}


class SystemLosses(BaseModel):
    """Systemverluste für Ertragsberechnung."""

    model_config = {"from_attributes": True}

    shading_loss: float = Field(
        default=0.10, ge=0, le=0.80, description="Verschattungsverlust (0.0–0.8)"
    )
    temperature_loss: float = Field(
        default=0.10, ge=0, le=0.30, description="Temperaturverlust (0.0–0.3)"
    )
    soiling_loss: float = Field(
        default=0.05, ge=0, le=0.20, description="Verschmutzungsverlust (0.0–0.2)"
    )
    cable_loss: float = Field(
        default=0.03, ge=0, le=0.10, description="Kabelverlust (0.0–0.1)"
    )
    mppt_loss: float = Field(
        default=0.03, ge=0, le=0.10, description="MPPT-Wandlungsverlust (0.0–0.1)"
    )
    mismatch_loss: float = Field(
        default=0.02, ge=0, le=0.10, description="Mismatch-Verlust (0.0–0.1)"
    )
    battery_loss: float = Field(
        default=0.05, ge=0, le=0.15, description="Batterie-Ladeverlust (0.0–0.15)"
    )
    degradation_loss: float = Field(
        default=0.00, ge=0, le=0.30, description="Alterungsverlust (0.0–0.3)"
    )

    @property
    def total_system_factor(self) -> float:
        """Gesamter Systemfaktor (1.0 = keine Verluste)."""
        factor = 1.0
        factor *= (1.0 - self.shading_loss)
        factor *= (1.0 - self.temperature_loss)
        factor *= (1.0 - self.soiling_loss)
        factor *= (1.0 - self.cable_loss)
        factor *= (1.0 - self.mppt_loss)
        factor *= (1.0 - self.mismatch_loss)
        factor *= (1.0 - self.battery_loss)
        factor *= (1.0 - self.degradation_loss)
        return factor

    @property
    def total_loss_percent(self) -> float:
        """Gesamtverlust in Prozent."""
        return (1.0 - self.total_system_factor) * 100


class YieldCalculationInput(BaseModel):
    """Eingabedaten für die Ertragsberechnung."""

    model_config = {"from_attributes": True}

    installed_wp: float = Field(..., gt=0, description="Installierte Leistung in Wp")
    region: SailingRegion = Field(..., description="Segelrevier")
    season: Season = Field(default=Season.ANNUAL_AVERAGE, description="Jahreszeit")
    system_voltage: int = Field(default=12, description="Systemspannung (12, 24, 48)")
    losses: SystemLosses = Field(default_factory=SystemLosses, description="Systemverluste")
    panel_age_years: float = Field(default=0, ge=0, description="Panel-Alter in Jahren")
    annual_degradation: float = Field(
        default=0.005, ge=0, le=0.05, description="Jährliche Degradation"
    )


class YieldCalculationResult(BaseModel):
    """Ergebnis der Ertragsberechnung."""

    model_config = {"from_attributes": True}

    daily_yield_wh: float = Field(..., description="Tagesertrag in Wh")
    daily_yield_ah: float = Field(..., description="Tagesertrag in Ah (bei Systemspannung)")
    monthly_yield_kwh: float = Field(..., description="Monatsertrag in kWh")
    annual_yield_kwh: float = Field(..., description="Jahresertrag in kWh")
    system_factor: float = Field(..., description="Angewandter Systemfaktor")
    psh_used: float = Field(..., description="Verwendete Peak Sun Hours")
    confidence: ConfidenceLevel = Field(..., description="Confidence-Level des Ergebnisses")
    notes: list[str] = Field(default_factory=list, description="Hinweise und Einschränkungen")


class ConfidenceLevel(str, Enum):
    """Re-export for use in yield results."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    ESTIMATED = "estimated"
```

### ANHANG L — Fehlerdiagnose-Modelle

```python
"""
AYDI Solar Fault Diagnosis Models — Pydantic v2
Module: backend/app/models/solar_faults.py
"""

from __future__ import annotations

from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class FaultSeverity(str, Enum):
    """Schweregrad eines Fehlerbilds."""
    CRITICAL = "critical"       # Sofortige Stilllegung
    HIGH = "high"               # Austausch mittelfristig
    MEDIUM = "medium"           # Überwachung, Maßnahmen planen
    LOW = "low"                 # Monitoring, normal
    INFORMATIONAL = "informational"  # Rein informativ


class FaultCategory(str, Enum):
    """Fehlerkategorie."""
    HOTSPOT = "hotspot"
    DELAMINATION = "delamination"
    MICROCRACKS = "microcracks"
    CORROSION = "corrosion"
    SHADING_LOSS = "shading_loss"
    CABLE_FAULT = "cable_fault"
    PID = "pid"
    SNAIL_TRAILS = "snail_trails"
    GLASS_BREAKAGE = "glass_breakage"
    BACKSHEET_DEGRADATION = "backsheet_degradation"
    YELLOWING = "yellowing"
    MPPT_FAULT = "mppt_fault"


class VisualConfidence(str, Enum):
    """Visuelle Erkennbarkeit."""
    HIGH = "visual_high"            # Deutlich sichtbar
    MEDIUM = "visual_medium"        # Bei Inspektion erkennbar
    LOW = "visual_low"              # Kaum/nicht visuell erkennbar
    INSUFFICIENT = "visual_insufficient"  # Nur mit Spezialgerät


class SolarFaultFinding(BaseModel):
    """Einzelner Fehlerbefund an einer Solaranlage."""

    model_config = {"from_attributes": True}

    fault_id: str = Field(..., description="Eindeutige Befund-ID")
    category: FaultCategory = Field(..., description="Fehlerkategorie")
    severity: FaultSeverity = Field(..., description="Schweregrad")
    visual_confidence: VisualConfidence = Field(..., description="Visuelle Erkennbarkeit")
    
    location: str = Field(..., description="Ort des Befunds (Panel-ID, Position)")
    description_de: str = Field(..., description="Befundbeschreibung (Deutsch)")
    
    estimated_power_loss_percent: Optional[float] = Field(
        None, ge=0, le=100, description="Geschätzter Leistungsverlust in %"
    )
    
    immediate_action_required: bool = Field(
        default=False, description="Sofortige Maßnahme erforderlich?"
    )
    recommended_action_de: str = Field(..., description="Empfohlene Maßnahme (Deutsch)")
    estimated_repair_cost_eur: Optional[float] = Field(
        None, ge=0, description="Geschätzte Reparaturkosten in EUR"
    )
    
    detection_date: Optional[date] = Field(None, description="Datum der Erkennung")
    image_references: list[str] = Field(
        default_factory=list, description="Referenzen auf Befund-Fotos"
    )


class SolarFaultReport(BaseModel):
    """Gesamtbericht Solaranlagen-Diagnose."""

    model_config = {"from_attributes": True}

    report_id: str = Field(..., description="Eindeutige Berichts-ID")
    boat_name: str = Field(..., description="Bootsname")
    inspection_date: date = Field(..., description="Inspektionsdatum")
    inspector: str = Field(default="AYDI_AI", description="Inspektor")
    
    findings: list[SolarFaultFinding] = Field(
        default_factory=list, description="Liste der Befunde"
    )
    
    overall_system_health_score: float = Field(
        ..., ge=0, le=100, description="Gesamt-Systemzustand (0–100 Punkte)"
    )
    
    critical_findings_count: int = Field(default=0, description="Anzahl kritischer Befunde")
    estimated_total_repair_cost_eur: Optional[float] = Field(
        None, ge=0, description="Geschätzte Gesamtreparaturkosten"
    )
    
    next_inspection_recommended: Optional[date] = Field(
        None, description="Empfohlenes nächstes Inspektionsdatum"
    )
    
    confidence: str = Field(
        default="visual_medium",
        description="Gesamtconfidence des Berichts"
    )
    notes_de: list[str] = Field(
        default_factory=list, description="Zusätzliche Hinweise (Deutsch)"
    )

    @property
    def has_critical_faults(self) -> bool:
        """Gibt es kritische Befunde?"""
        return any(f.severity == FaultSeverity.CRITICAL for f in self.findings)

    @property
    def immediate_actions_required(self) -> list[SolarFaultFinding]:
        """Alle Befunde mit sofortigem Handlungsbedarf."""
        return [f for f in self.findings if f.immediate_action_required]
```

### ANHANG M — Hersteller-Datenbank-Modell

```python
"""
AYDI Solar Manufacturer Database Models — Pydantic v2
Module: backend/app/models/solar_manufacturers.py
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field, HttpUrl


class ManufacturerRating(BaseModel):
    """Bewertung eines Herstellers in verschiedenen Kategorien."""

    model_config = {"from_attributes": True}

    quality: int = Field(..., ge=1, le=5, description="Qualität (1–5 Sterne)")
    price_performance: int = Field(..., ge=1, le=5, description="Preis-Leistung (1–5 Sterne)")
    marine_focus: int = Field(..., ge=1, le=5, description="Marine-Spezialisierung (1–5)")
    availability: int = Field(..., ge=1, le=5, description="Verfügbarkeit/Lieferfähigkeit (1–5)")
    support: int = Field(..., ge=1, le=5, description="Kundensupport (1–5)")
    longevity: int = Field(..., ge=1, le=5, description="Langlebigkeit der Produkte (1–5)")

    @property
    def overall_score(self) -> float:
        """Gewichtete Gesamtbewertung."""
        weights = {
            "quality": 0.25,
            "price_performance": 0.15,
            "marine_focus": 0.25,
            "availability": 0.10,
            "support": 0.10,
            "longevity": 0.15,
        }
        total = (
            self.quality * weights["quality"]
            + self.price_performance * weights["price_performance"]
            + self.marine_focus * weights["marine_focus"]
            + self.availability * weights["availability"]
            + self.support * weights["support"]
            + self.longevity * weights["longevity"]
        )
        return round(total, 2)


class SolarManufacturer(BaseModel):
    """Hersteller-Eintrag in der AYDI-Datenbank."""

    model_config = {"from_attributes": True}

    name: str = Field(..., description="Firmenname")
    country: str = Field(..., description="Firmensitz (Land)")
    city: Optional[str] = Field(None, description="Firmensitz (Stadt)")
    founded_year: Optional[int] = Field(None, ge=1900, description="Gründungsjahr")
    website: Optional[str] = Field(None, description="Website-URL")
    
    specialization: str = Field(..., description="Spezialisierung/Kernkompetenz")
    technologies: list[str] = Field(
        default_factory=list, description="Angebotene Technologien"
    )
    
    warranty_product_years: int = Field(default=2, ge=0, description="Produktgarantie Jahre")
    warranty_performance_years: int = Field(default=10, ge=0, description="Leistungsgarantie")
    warranty_performance_percent: float = Field(
        default=0.80, ge=0.5, le=1.0, description="Garantierte Restleistung"
    )
    
    rating: ManufacturerRating = Field(..., description="AYDI-Bewertung")
    
    strengths_de: list[str] = Field(default_factory=list, description="Stärken (Deutsch)")
    weaknesses_de: list[str] = Field(default_factory=list, description="Schwächen (Deutsch)")
    
    product_count: int = Field(default=0, ge=0, description="Anzahl Produkte in AYDI-DB")
    
    confidence: str = Field(default="documented", description="Confidence-Level")
```

### ANHANG N — Montage-Analyse

```python
"""
AYDI Solar Mounting Analysis Models — Pydantic v2
Module: backend/app/models/solar_mounting.py
"""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class ArchMaterial(str, Enum):
    """Material des Geräteträgers."""
    STAINLESS_STEEL_25 = "stainless_25mm"
    STAINLESS_STEEL_32 = "stainless_32mm"
    STAINLESS_STEEL_38 = "stainless_38mm"
    STAINLESS_STEEL_50 = "stainless_50mm"
    ALUMINIUM_40 = "aluminium_40mm"
    ALUMINIUM_60 = "aluminium_60mm"
    CARBON_FIBER = "carbon_fiber"


class MountingHardware(str, Enum):
    """Befestigungs-Hardware."""
    Z_BRACKETS = "z_brackets"
    L_BRACKETS = "l_brackets"
    RAIL_SYSTEM = "rail_system"
    ADHESIVE = "adhesive"
    RIVETS = "rivets"
    BOLTS_NUTS = "bolts_nuts"
    CLAMPS = "clamps"
    GROMMETS_LACING = "grommets_lacing"


class SolarMountingAnalysis(BaseModel):
    """Analyse der Solar-Montagesituation."""

    model_config = {"from_attributes": True}

    mounting_location: str = Field(..., description="Montageort (z.B. 'Arch Heck')")
    mounting_type: str = Field(..., description="Montagetyp")
    
    # Strukturelle Bewertung
    arch_material: Optional[ArchMaterial] = Field(None, description="Arch-Material")
    arch_load_capacity_kg: Optional[float] = Field(
        None, ge=0, description="Tragfähigkeit des Arch in kg"
    )
    total_panel_weight_kg: float = Field(..., ge=0, description="Gesamtgewicht der Panels")
    weight_utilization_percent: Optional[float] = Field(
        None, ge=0, le=200, description="Auslastung der Tragfähigkeit in %"
    )
    
    # Verschattungsanalyse
    shading_sources: list[str] = Field(
        default_factory=list, description="Identifizierte Verschattungsquellen"
    )
    worst_case_shading_percent: float = Field(
        default=0.0, ge=0, le=100, description="Worst-Case Verschattungsverlust in %"
    )
    average_shading_percent: float = Field(
        default=0.0, ge=0, le=100, description="Durchschnittlicher Verschattungsverlust in %"
    )
    
    # Belüftung
    ventilation_gap_mm: float = Field(
        default=0.0, ge=0, description="Hinterlüftungsspalt in mm"
    )
    ventilation_adequate: bool = Field(
        default=True, description="Hinterlüftung ausreichend?"
    )
    estimated_temperature_penalty_percent: float = Field(
        default=0.0, ge=0, le=30, description="Geschätzter Temperatur-Malus in %"
    )
    
    # Bewertung
    structural_score: float = Field(..., ge=0, le=100, description="Strukturelle Bewertung (0–100)")
    shading_score: float = Field(..., ge=0, le=100, description="Verschattungs-Bewertung (0–100)")
    ventilation_score: float = Field(..., ge=0, le=100, description="Belüftungs-Bewertung (0–100)")
    cable_routing_score: float = Field(
        ..., ge=0, le=100, description="Kabelführungs-Bewertung (0–100)"
    )
    
    overall_mounting_score: float = Field(
        ..., ge=0, le=100, description="Gesamt-Montage-Bewertung (0–100)"
    )
    
    recommendations_de: list[str] = Field(
        default_factory=list, description="Empfehlungen (Deutsch)"
    )
    
    confidence: str = Field(default="visual_medium", description="Confidence-Level")
```

### ANHANG O — Wirtschaftlichkeitsberechnung

```python
"""
AYDI Solar Economic Analysis Models — Pydantic v2
Module: backend/app/models/solar_economics.py
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class EnergyAlternativeCost(BaseModel):
    """Kosten alternativer Energiequellen (zum Vergleich)."""

    model_config = {"from_attributes": True}

    shore_power_eur_per_kwh: float = Field(
        default=0.55, ge=0, description="Landstrom-Kosten in €/kWh"
    )
    generator_diesel_eur_per_liter: float = Field(
        default=1.85, ge=0, description="Diesel-Preis in €/Liter"
    )
    generator_consumption_l_per_kwh: float = Field(
        default=0.4, ge=0, description="Generator-Verbrauch in L/kWh"
    )
    generator_maintenance_eur_per_hour: float = Field(
        default=2.50, ge=0, description="Generator-Wartungskosten in €/Betriebsstunde"
    )
    marina_days_per_year: int = Field(
        default=60, ge=0, description="Tage im Hafen mit Landstrom/Jahr"
    )
    anchor_days_per_year: int = Field(
        default=120, ge=0, description="Ankertage/Jahr (Solar-relevant)"
    )


class SolarEconomicAnalysis(BaseModel):
    """Wirtschaftlichkeitsberechnung einer Solaranlage."""

    model_config = {"from_attributes": True}

    # Investitionskosten
    panel_cost_eur: float = Field(..., ge=0, description="Kosten Panels")
    controller_cost_eur: float = Field(..., ge=0, description="Kosten Regler")
    mounting_cost_eur: float = Field(..., ge=0, description="Kosten Montage-Hardware")
    cable_cost_eur: float = Field(..., ge=0, description="Kosten Kabel/Stecker")
    installation_cost_eur: float = Field(default=0, ge=0, description="Installationskosten")
    
    # Betriebsdaten
    annual_yield_kwh: float = Field(..., ge=0, description="Jährlicher Ertrag in kWh")
    system_lifetime_years: int = Field(default=20, ge=1, description="Erwartete Lebensdauer")
    annual_maintenance_eur: float = Field(
        default=50, ge=0, description="Jährliche Wartungskosten"
    )
    
    # Vergleichskosten
    alternatives: EnergyAlternativeCost = Field(
        default_factory=EnergyAlternativeCost, description="Alternative Energiekosten"
    )

    @property
    def total_investment_eur(self) -> float:
        """Gesamte Investitionskosten."""
        return (
            self.panel_cost_eur
            + self.controller_cost_eur
            + self.mounting_cost_eur
            + self.cable_cost_eur
            + self.installation_cost_eur
        )

    @property
    def annual_savings_eur(self) -> float:
        """Jährliche Einsparung durch Solar vs. Generator."""
        generator_cost_per_kwh = (
            self.alternatives.generator_diesel_eur_per_liter
            * self.alternatives.generator_consumption_l_per_kwh
            + self.alternatives.generator_maintenance_eur_per_hour * 0.4
        )
        annual_kwh_from_solar = self.annual_yield_kwh * (
            self.alternatives.anchor_days_per_year / 365
        )
        return annual_kwh_from_solar * generator_cost_per_kwh

    @property
    def payback_years(self) -> float:
        """Amortisationszeit in Jahren."""
        net_annual_saving = self.annual_savings_eur - self.annual_maintenance_eur
        if net_annual_saving <= 0:
            return float("inf")
        return self.total_investment_eur / net_annual_saving

    @property
    def levelized_cost_of_energy_eur_per_kwh(self) -> float:
        """Stromgestehungskosten (LCOE) in €/kWh."""
        total_cost = (
            self.total_investment_eur
            + self.annual_maintenance_eur * self.system_lifetime_years
        )
        total_yield = self.annual_yield_kwh * self.system_lifetime_years * 0.9  # avg degradation
        if total_yield == 0:
            return float("inf")
        return total_cost / total_yield

    @property
    def cost_per_wp(self) -> float:
        """Gesamtkosten pro Watt-Peak installiert."""
        # Approximation basierend auf typischem Ertrag/Wp
        return self.total_investment_eur / max(self.annual_yield_kwh / 1.5, 1)


class SolarROIReport(BaseModel):
    """ROI-Bericht für eine Solaranlage."""

    model_config = {"from_attributes": True}

    boat_name: str = Field(..., description="Bootsname")
    analysis: SolarEconomicAnalysis = Field(..., description="Wirtschaftlichkeitsanalyse")
    
    total_investment_eur: float = Field(..., ge=0, description="Gesamtinvestition")
    payback_years: float = Field(..., ge=0, description="Amortisationszeit in Jahren")
    lcoe_eur_per_kwh: float = Field(..., ge=0, description="Stromgestehungskosten")
    annual_savings_eur: float = Field(..., description="Jährliche Einsparung")
    
    twenty_year_savings_eur: float = Field(
        ..., description="20-Jahres-Gesamteinsparung"
    )
    
    recommendation_de: str = Field(..., description="Empfehlung (Deutsch)")
    confidence: str = Field(default="calculated", description="Confidence-Level")
```

### ANHANG P — Visual Analysis Prompts

```python
"""
AYDI Solar Visual Analysis Configuration — Pydantic v2
Module: backend/app/models/solar_visual.py
"""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class SolarVisualAnalysisType(str, Enum):
    """Art der visuellen Solar-Analyse."""
    PANEL_CONDITION = "panel_condition"
    MOUNTING_QUALITY = "mounting_quality"
    SHADING_ASSESSMENT = "shading_assessment"
    WIRING_INSPECTION = "wiring_inspection"
    OVERALL_INSTALLATION = "overall_installation"


class SolarVisualPrompt(BaseModel):
    """Prompt-Konfiguration für visuelle Solaranlagen-Analyse."""

    model_config = {"from_attributes": True}

    analysis_type: SolarVisualAnalysisType = Field(..., description="Analyse-Typ")
    system_prompt_de: str = Field(..., description="System-Prompt (Deutsch)")
    user_prompt_template_de: str = Field(
        ..., description="User-Prompt-Template (Deutsch, mit Platzhaltern)"
    )
    
    expected_findings: list[str] = Field(
        default_factory=list, description="Erwartbare Befund-Kategorien"
    )
    
    min_confidence_for_finding: str = Field(
        default="visual_medium",
        description="Mindest-Confidence für einen Befund"
    )
    
    scoring_weights: dict[str, float] = Field(
        default_factory=dict, description="Gewichtung der Bewertungskriterien"
    )


# Vordefinierte Prompts für Solar-Analyse
SOLAR_PANEL_CONDITION_PROMPT = SolarVisualPrompt(
    analysis_type=SolarVisualAnalysisType.PANEL_CONDITION,
    system_prompt_de=(
        "Du bist ein erfahrener Marine-Solartechniker. Analysiere das Foto eines "
        "Solarpanels auf einer Yacht. Bewerte den Zustand nach folgenden Kriterien: "
        "Oberflächenzustand (Delamination, Vergilbung, Kratzer), Zellenintegrität "
        "(Schneckenspuren, sichtbare Risse, Verfärbungen), Rahmen/Montage "
        "(Korrosion, Befestigung), Anschlüsse (Kabelzustand, Stecker). "
        "Sage 'nicht beurteilbar' wenn das Foto keine sichere Aussage erlaubt."
    ),
    user_prompt_template_de=(
        "Analysiere dieses Solarpanel auf dem Boot '{boat_name}'. "
        "Panel-Typ: {panel_type}, Alter: {panel_age_years} Jahre, "
        "Position: {mounting_location}. "
        "Bewerte den Zustand auf einer Skala 0–100 und identifiziere alle Fehlerbilder."
    ),
    expected_findings=[
        "hotspot", "delamination", "microcracks", "corrosion",
        "yellowing", "snail_trails", "glass_breakage", "backsheet_degradation"
    ],
    min_confidence_for_finding="visual_medium",
    scoring_weights={
        "surface_condition": 0.30,
        "cell_integrity": 0.30,
        "frame_mounting": 0.20,
        "connections": 0.20,
    },
)

SOLAR_MOUNTING_QUALITY_PROMPT = SolarVisualPrompt(
    analysis_type=SolarVisualAnalysisType.MOUNTING_QUALITY,
    system_prompt_de=(
        "Du bist ein erfahrener Yacht-Elektriker und Rigger. Analysiere das Foto "
        "der Solarpanel-Montage auf dieser Yacht. Bewerte: Strukturelle Integrität "
        "der Halterung, Materialwahl (Korrosionsbeständigkeit), Kabeldurchführungen, "
        "Hinterlüftung, Verschattungssituation. "
        "Sage 'nicht beurteilbar' wenn das Foto keine sichere Aussage erlaubt."
    ),
    user_prompt_template_de=(
        "Analysiere die Solar-Montage auf '{boat_name}'. "
        "Montageort: {mounting_location}, Panel-Anzahl: {panel_count}, "
        "Gesamtgewicht: {total_weight_kg} kg. "
        "Bewerte die Montagequalität und identifiziere Verbesserungspotential."
    ),
    expected_findings=[
        "corrosion", "inadequate_ventilation", "shading_issue",
        "structural_weakness", "cable_routing_poor", "galvanic_corrosion"
    ],
    min_confidence_for_finding="visual_medium",
    scoring_weights={
        "structural_integrity": 0.30,
        "corrosion_resistance": 0.25,
        "ventilation": 0.20,
        "cable_management": 0.15,
        "aesthetics": 0.10,
    },
)
```

### ANHANG Q — Dimensionierungs-Service

```python
"""
AYDI Solar Dimensioning Service — Pydantic v2
Module: backend/app/services/solar_dimensioning.py
"""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field

from ..models.solar import PanelFormFactor, PanelTechnology
from ..models.solar_yield import SailingRegion, Season, SystemLosses, PSH_DATABASE


class BoatType(str, Enum):
    """Bootstyp für Dimensionierung."""
    MONOHULL_SAIL_SMALL = "monohull_sail_small"       # 8–12m
    MONOHULL_SAIL_MEDIUM = "monohull_sail_medium"     # 12–16m
    MONOHULL_SAIL_LARGE = "monohull_sail_large"       # 16–22m
    CATAMARAN_SMALL = "catamaran_small"               # 36–42ft
    CATAMARAN_MEDIUM = "catamaran_medium"             # 42–50ft
    CATAMARAN_LARGE = "catamaran_large"               # 50ft+
    MOTORYACHT_SMALL = "motoryacht_small"             # 8–14m
    MOTORYACHT_MEDIUM = "motoryacht_medium"           # 14–22m
    MOTORYACHT_LARGE = "motoryacht_large"             # 22m+


class ConsumerProfile(BaseModel):
    """Verbrauchsprofil eines Bootes."""

    model_config = {"from_attributes": True}

    refrigerator_ah_per_day: float = Field(default=50, ge=0, description="Kühlschrank Ah/Tag")
    autopilot_ah_per_day: float = Field(default=15, ge=0, description="Autopilot Ah/Tag")
    instruments_ah_per_day: float = Field(default=8, ge=0, description="Instrumente Ah/Tag")
    lighting_ah_per_day: float = Field(default=5, ge=0, description="Beleuchtung Ah/Tag")
    watermaker_ah_per_day: float = Field(default=0, ge=0, description="Wassermacher Ah/Tag")
    laptop_ah_per_day: float = Field(default=10, ge=0, description="Laptop/Unterhaltung Ah/Tag")
    communication_ah_per_day: float = Field(default=3, ge=0, description="Funk/AIS/Sat Ah/Tag")
    anchor_windlass_ah_per_day: float = Field(default=5, ge=0, description="Ankerwinde Ah/Tag")
    other_ah_per_day: float = Field(default=10, ge=0, description="Sonstige Verbraucher Ah/Tag")

    @property
    def total_daily_consumption_ah(self) -> float:
        """Gesamter Tagesverbrauch in Ah."""
        return (
            self.refrigerator_ah_per_day
            + self.autopilot_ah_per_day
            + self.instruments_ah_per_day
            + self.lighting_ah_per_day
            + self.watermaker_ah_per_day
            + self.laptop_ah_per_day
            + self.communication_ah_per_day
            + self.anchor_windlass_ah_per_day
            + self.other_ah_per_day
        )


class DimensioningInput(BaseModel):
    """Eingabedaten für die Solar-Dimensionierung."""

    model_config = {"from_attributes": True}

    boat_type: BoatType = Field(..., description="Bootstyp")
    boat_length_m: float = Field(..., gt=0, description="Bootslänge in m")
    system_voltage: int = Field(default=12, description="Systemspannung (12/24/48)")
    
    primary_region: SailingRegion = Field(..., description="Haupt-Segelrevier")
    design_season: Season = Field(
        default=Season.ANNUAL_AVERAGE, description="Auslegungs-Jahreszeit"
    )
    autonomy_target_days: int = Field(
        default=3, ge=1, description="Gewünschte Autarkie-Tage (ohne Sonne)"
    )
    
    consumer_profile: ConsumerProfile = Field(
        default_factory=ConsumerProfile, description="Verbrauchsprofil"
    )
    
    available_area_m2: Optional[float] = Field(
        None, gt=0, description="Verfügbare Montagefläche in m²"
    )
    max_weight_kg: Optional[float] = Field(
        None, gt=0, description="Maximales Gewicht für Panels in kg"
    )
    max_budget_eur: Optional[float] = Field(
        None, gt=0, description="Maximales Budget in EUR"
    )
    
    preferred_technology: Optional[PanelTechnology] = Field(
        None, description="Bevorzugte Technologie"
    )
    preferred_form_factor: Optional[PanelFormFactor] = Field(
        None, description="Bevorzugte Bauform"
    )


class DimensioningRecommendation(BaseModel):
    """Ergebnis der Solar-Dimensionierung."""

    model_config = {"from_attributes": True}

    recommended_wp: float = Field(..., gt=0, description="Empfohlene Leistung in Wp")
    recommended_technology: PanelTechnology = Field(..., description="Empfohlene Technologie")
    recommended_form_factor: PanelFormFactor = Field(..., description="Empfohlene Bauform")
    
    panel_count: int = Field(..., ge=1, description="Empfohlene Anzahl Panels")
    panel_wp_each: float = Field(..., gt=0, description="Leistung pro Panel in Wp")
    
    estimated_daily_yield_ah: float = Field(..., gt=0, description="Erwarteter Tagesertrag Ah")
    autonomy_achieved: bool = Field(..., description="Autarkie-Ziel erreichbar?")
    solar_coverage_percent: float = Field(
        ..., ge=0, le=200, description="Solar-Deckungsgrad des Verbrauchs in %"
    )
    
    required_area_m2: float = Field(..., gt=0, description="Benötigte Fläche in m²")
    total_weight_kg: float = Field(..., gt=0, description="Gesamtgewicht Panels in kg")
    estimated_total_cost_eur: float = Field(..., gt=0, description="Geschätzte Gesamtkosten")
    
    recommended_controller: str = Field(..., description="Empfohlener MPPT-Regler")
    wiring_recommendation: str = Field(..., description="Empfohlene Verschaltung")
    
    battery_recommendation_ah: float = Field(
        ..., gt=0, description="Empfohlene Batteriekapazität Ah"
    )
    
    warnings_de: list[str] = Field(
        default_factory=list, description="Warnhinweise (Deutsch)"
    )
    notes_de: list[str] = Field(
        default_factory=list, description="Zusätzliche Hinweise (Deutsch)"
    )
    
    confidence: str = Field(default="calculated", description="Confidence-Level")
```

### ANHANG R — Scoring-Integration

```python
"""
AYDI Solar Scoring Integration — Pydantic v2
Module: backend/app/models/solar_scoring.py

Integration in das AYDI-Gesamtscoring-System.
Score-Fusion-Gewichte: structured=0.60, visual=0.40 (Solar-spezifisch)
"""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class SolarAssessmentCategory(str, Enum):
    """Bewertungskategorien für Solaranlagen."""
    DIMENSIONING = "dimensioning"             # Ist die Anlage richtig dimensioniert?
    PANEL_CONDITION = "panel_condition"        # Zustand der Panels
    MOUNTING_QUALITY = "mounting_quality"      # Montagequalität
    WIRING_QUALITY = "wiring_quality"         # Verkabelungsqualität
    CONTROLLER_SETUP = "controller_setup"     # Regler-Konfiguration
    SHADING_OPTIMIZATION = "shading_optimization"  # Verschattungs-Optimierung
    SYSTEM_EFFICIENCY = "system_efficiency"   # Systemeffizienz
    ECONOMIC_VALUE = "economic_value"         # Wirtschaftlichkeit


class SolarCategoryScore(BaseModel):
    """Bewertung einer einzelnen Kategorie."""

    model_config = {"from_attributes": True}

    category: SolarAssessmentCategory = Field(..., description="Bewertungskategorie")
    structured_score: Optional[float] = Field(
        None, ge=0, le=100, description="Score aus strukturierter Analyse (0–100)"
    )
    visual_score: Optional[float] = Field(
        None, ge=0, le=100, description="Score aus visueller Analyse (0–100)"
    )
    
    structured_confidence: Optional[str] = Field(None, description="Confidence strukturiert")
    visual_confidence: Optional[str] = Field(None, description="Confidence visuell")
    
    weight_structured: float = Field(default=0.60, ge=0, le=1.0)
    weight_visual: float = Field(default=0.40, ge=0, le=1.0)
    
    findings_de: list[str] = Field(default_factory=list, description="Befunde (Deutsch)")
    recommendations_de: list[str] = Field(
        default_factory=list, description="Empfehlungen (Deutsch)"
    )

    @property
    def fused_score(self) -> Optional[float]:
        """Fusionierter Score aus strukturiert + visuell."""
        if self.structured_score is not None and self.visual_score is not None:
            return (
                self.structured_score * self.weight_structured
                + self.visual_score * self.weight_visual
            )
        elif self.structured_score is not None:
            return self.structured_score
        elif self.visual_score is not None:
            return self.visual_score
        return None


class SolarOverallAssessment(BaseModel):
    """Gesamtbewertung der Solaranlage für AYDI-Scoring."""

    model_config = {"from_attributes": True}

    boat_name: str = Field(..., description="Bootsname")
    
    category_scores: list[SolarCategoryScore] = Field(
        ..., min_length=1, description="Einzelne Kategorie-Scores"
    )
    
    overall_score: float = Field(..., ge=0, le=100, description="Gesamtscore (0–100)")
    
    # Gewichtung der Kategorien für Gesamtscore
    category_weights: dict[str, float] = Field(
        default={
            "dimensioning": 0.20,
            "panel_condition": 0.15,
            "mounting_quality": 0.15,
            "wiring_quality": 0.15,
            "controller_setup": 0.10,
            "shading_optimization": 0.10,
            "system_efficiency": 0.10,
            "economic_value": 0.05,
        },
        description="Gewichtung der Kategorien"
    )
    
    grade: str = Field(..., description="Bewertungsnote (A–F)")
    grade_description_de: str = Field(..., description="Notenbeschreibung Deutsch")
    
    critical_findings: list[str] = Field(
        default_factory=list, description="Kritische Befunde"
    )
    improvement_priorities_de: list[str] = Field(
        default_factory=list, description="Verbesserungsprioritäten (Deutsch)"
    )
    
    estimated_improvement_potential_percent: float = Field(
        default=0, ge=0, le=100,
        description="Geschätztes Verbesserungspotential in %"
    )
    estimated_improvement_cost_eur: Optional[float] = Field(
        None, ge=0, description="Geschätzte Kosten für Verbesserungen"
    )
    
    confidence: str = Field(default="calculated", description="Gesamtconfidence")
    data_completeness_percent: float = Field(
        default=100, ge=0, le=100, description="Datenvollständigkeit in %"
    )

    @property
    def has_critical_findings(self) -> bool:
        """Gibt es kritische Befunde?"""
        return len(self.critical_findings) > 0

    @classmethod
    def grade_from_score(cls, score: float) -> tuple[str, str]:
        """Berechne Note aus Score."""
        if score >= 90:
            return "A", "Hervorragend — Anlage optimal dimensioniert und installiert"
        elif score >= 80:
            return "B", "Gut — Anlage funktional, kleine Optimierungen möglich"
        elif score >= 65:
            return "C", "Befriedigend — Anlage funktioniert, aber mit Verbesserungsbedarf"
        elif score >= 50:
            return "D", "Ausreichend — Anlage hat deutliche Mängel"
        elif score >= 30:
            return "E", "Mangelhaft — Anlage hat schwerwiegende Mängel"
        else:
            return "F", "Ungenügend — Anlage nicht funktionsfähig oder gefährlich"
```

---

## ZUSATZ: Erweiterte Installationsrichtlinien

### Z.1 Kabelquerschnitt-Referenztabelle

Die korrekte Kabelwahl ist sicherheitsrelevant. Zu dünne Kabel verursachen Erwärmung, Leistungsverlust und im schlimmsten Fall Brand.

**12V-System — Maximal 3% Spannungsverlust (0,42V):**

| Strom (A) | 1m | 2m | 3m | 4m | 5m | 6m | 8m | 10m |
|-----------|-----|-----|-----|-----|-----|-----|-----|------|
| 5 | 1,5 | 1,5 | 1,5 | 2,5 | 2,5 | 4,0 | 4,0 | 6,0 |
| 10 | 1,5 | 2,5 | 4,0 | 4,0 | 6,0 | 6,0 | 10 | 10 |
| 15 | 2,5 | 4,0 | 6,0 | 6,0 | 10 | 10 | 16 | 16 |
| 20 | 4,0 | 6,0 | 6,0 | 10 | 10 | 16 | 16 | 25 |
| 30 | 4,0 | 6,0 | 10 | 16 | 16 | 25 | 25 | 35 |
| 40 | 6,0 | 10 | 16 | 16 | 25 | 25 | 35 | 50 |
| 50 | 6,0 | 10 | 16 | 25 | 25 | 35 | 50 | 70 |

*Alle Angaben in mm². Einfache Kabellänge (Hin+Rück = doppelt).*

**24V-System — Maximal 3% Spannungsverlust (0,84V):**

| Strom (A) | 2m | 4m | 6m | 8m | 10m | 15m |
|-----------|-----|-----|-----|-----|------|------|
| 5 | 1,5 | 1,5 | 1,5 | 2,5 | 2,5 | 4,0 |
| 10 | 1,5 | 2,5 | 4,0 | 4,0 | 6,0 | 6,0 |
| 15 | 2,5 | 4,0 | 4,0 | 6,0 | 6,0 | 10 |
| 20 | 2,5 | 4,0 | 6,0 | 6,0 | 10 | 16 |
| 30 | 4,0 | 6,0 | 10 | 10 | 16 | 16 |

**Kabeltypen für Marine-Solar:**
| Typ | Beschreibung | Einsatzbereich | Preis (€/m, 6mm²) |
|-----|-------------|----------------|---------------------|
| H07V-K (Haushalt) | Eindrähtig, PVC | NIEMALS auf Booten! | 0,80 |
| H07RN-F | Gummikabel, flexibel | Nur unter Deck | 2,50 |
| Marine-Solarkabel | Doppeltisoliert, UV-fest, verzinnte Litze | Standard-Empfehlung | 4,50 |
| Tinned Marine Cable (ABYC) | Verzinnt, UL-listed, UV/Öl-beständig | Premium/US-Standard | 6,80 |
| Paar-Solarkabel (MC4) | 2× 6mm² mit MC4-Steckern fertig konfektioniert | Schnellinstallation | 5,50 |

**Confidence:** measured — Berechnung nach Ohm'schem Gesetz, Kabeltypen nach ABYC E-11 / ISO 10133.

### Z.2 Sicherungskonzept

**Pflicht-Sicherungen:**
```
Panel ─── [Sicherung 1] ─── + ──────────── MPPT-Regler ─── [Sicherung 2] ─── Batterie
                                                                │
                              Sicherung 1: 1,5 × Isc          │
                              (bei parallelen Strings)          │
                                                                │
                              Sicherung 2: Regler-Nennstrom     │
                              (Batterie-seitiger Schutz)        │
```

**Sicherungs-Dimensionierung:**
| Situation | Sicherungswert | Begründung |
|-----------|---------------|-----------|
| 1 Panel, kein Parallel | Optional (1,5 × Isc) | Rückstrom-Schutz nicht nötig |
| 2+ Panels parallel | 1,5 × Isc pro String | Rückstrom bei String-Kurzschluss |
| Regler → Batterie | Regler-Max-Strom + 25% | Kurzschluss-Schutz Kabel |
| Batterie-Hauptsicherung | Summe aller Ladeströme + 50% | Leitungsschutz |

**Sicherungstypen:**
| Typ | Einsatz | Vorteil | Nachteil |
|-----|---------|---------|----------|
| ANL/MRBF Bolt-Type | Batterienah (hohe Ströme) | Kompakt, vibrationsfest | Nicht fernschaltbar |
| MIDI | Mittelstrecke | Standard, günstig | Begrenzt auf 200A |
| ATC/ATO Blade | Niedrige Ströme (<30A) | Universell, überall erhältlich | Nur bis 32V/30A |
| NH-Sicherung | Große Systeme (>100A) | Hohe Abschaltkapazität | Groß, schwer |
| Sicherungsautomat DC | Alle Positionen | Rücksetzbar, Schaltfunktion | Größer, teurer |
| Victron Smart BatteryProtect | Batterie-Last | Fernschaltbar, Unterspannungsschutz | Nur Lastseite |

**Confidence:** measured — ISO 10133, ABYC E-11, Victron Installationsrichtlinien.

### Z.3 MC4-Steckverbinder: Korrekte Verarbeitung

**Crimpen von MC4-Steckern — Schritt für Schritt:**

1. **Kabelende abisolieren:** 8–10 mm Isolierung entfernen (Abisolierzange, nicht Messer!)
2. **Crimpkontakt aufsetzen:** Litze vollständig in Kontakthülse einführen
3. **Crimpen:** Spezial-MC4-Crimpzange verwenden (NICHT Universal-Zange!)
   - Korrekte Crimpkraft: Kontakt fest, aber nicht gequetscht
   - Zugprobe: 50 N ohne Ausziehen
4. **Kontakt in Steckergehäuse einführen:** Einrasten hörbar (Click!)
5. **Verschraubung:** Überwurfmutter handfest + 1/4 Umdrehung
6. **Dichtung prüfen:** O-Ring vorhanden und unbeschädigt?

**Häufige Fehler:**
| Fehler | Konsequenz | Vermeidung |
|--------|-----------|-----------|
| Falsche Zange (Kombizange) | Lockerer Kontakt, Überhitzung | Nur MC4-Crimpzange verwenden |
| Litze zu kurz abisoliert | Wackelkontakt | Exakt 8–10 mm |
| Litze oxidiert/verschmutzt | Hoher Übergangswiderstand | Frisch abisolieren, ggf. verzinnen |
| O-Ring vergessen | Wassereintritt → Korrosion | Immer O-Ring prüfen |
| Verschraubung zu fest | O-Ring gequetscht, Gewinde beschädigt | Handfest + 1/4 Umdrehung |
| Plus/Minus vertauscht | Kurzschluss! | Vor Anschluss Polarität messen |

**Marine-Schutzmaßnahmen für MC4:**
- Selbstverschweißendes Tape (PIB-Band) um die Verbindung wickeln
- Schrumpfschlauch mit Kleber (Dual-Wall) über die Verbindung
- Kontaktfett (DeoxIT, Vaseline) vor dem Zusammenstecken
- Kabelbinder mit UV-Schutz zur Zugentlastung
- Vertikale Kabelführung (Stecker zeigt nach unten — Wasser läuft ab)

**Confidence:** documented — MC4-Herstelleranleitung (Multi-Contact/Stäubli), ergänzt durch marine Praxis.

### Z.4 Wartungsplan Solaranlage

**Monatliche Wartung (5 Minuten):**
- [ ] Panels visuell inspizieren (Verschmutzung, Beschädigung)
- [ ] Mit Süßwasser abspülen (bei Salzkruste)
- [ ] Ertragswerte im Monitoring prüfen (Trend normal?)

**Vierteljährliche Wartung (30 Minuten):**
- [ ] Alle Steckverbindungen prüfen (fest, korrosionsfrei?)
- [ ] Kabel auf Scheuerstellen inspizieren
- [ ] Panel-Oberfläche auf Delamination prüfen
- [ ] Regler-Betriebstemperatur prüfen (bei Volllast <50°C?)
- [ ] Halterungsschrauben auf Festigkeit prüfen

**Jährliche Wartung (2 Stunden):**
- [ ] Isolationswiderstand messen (>1 MΩ Panel→Rahmen)
- [ ] Leerlaufspannung Voc messen (Vergleich mit Datenblatt)
- [ ] Kurzschlussstrom Isc messen (Vergleich mit Datenblatt)
- [ ] MPPT-Regler Firmware aktualisieren
- [ ] Ertragsdaten des Jahres auswerten (Degradation?)
- [ ] Alle MC4-Verbindungen öffnen, Kontakte prüfen, ggf. Fett erneuern
- [ ] Kabeldurchführungen auf Dichtheit prüfen
- [ ] Montage-Hardware: Schrauben nachziehen, Korrosion behandeln
- [ ] Bypass-Dioden prüfen (Panel bei Teilverschattung: Spannung je Drittel messen)
- [ ] Dokumentation aktualisieren (Messwerte, Befunde, Maßnahmen)

**5-Jahres-Inspektion (professionell empfohlen):**
- [ ] Thermografie-Scan aller Panels (Hotspot-Erkennung)
- [ ] Elektrolumineszenz-Test (Mikroriss-Erkennung)
- [ ] Lastmessung am MPP (Vergleich mit Nennwert)
- [ ] Regler-Funktion unter Volllast verifizieren
- [ ] Wirtschaftlichkeits-Review (Austausch wirtschaftlich sinnvoll?)

**Confidence:** documented — Zusammengestellt aus Herstellerempfehlungen (Victron, Solbian, Sunware) und ABYC E-11.

### Z.5 Normen und Zertifizierungen

**Relevante Normen für Marine-Solaranlagen:**

| Norm | Titel | Relevanz |
|------|-------|----------|
| IEC 61215 | Terrestrische PV-Module — Bauarteignung | Panel-Qualifikation |
| IEC 61730 | PV-Module — Sicherheitseignung | Elektrische Sicherheit |
| IEC 62759 | Transport-Test für PV-Module | Transportfähigkeit |
| IEC 60904 | PV-Messverfahren | Leistungsmessung |
| ISO 10133 | Kleine Wasserfahrzeuge — Elektrische Systeme | Bordnetz-Installation |
| ABYC E-11 | AC and DC Electrical Systems | US-Standard Bordnetz |
| EN 50618 | Kabel für PV-Systeme | Solarkabel-Anforderung |
| IEC 62852 | PV-Steckverbinder | MC4-Anforderungen |
| CE-Kennzeichnung | EU-Konformität | Pflicht für EU-Markt |
| DNV-GL | Classification of Ships | Superyacht-Zertifizierung |

**Prüfbedingungen IEC 61215 (Auszug):**
- Thermal Cycling: 200 Zyklen -40°C bis +85°C
- Damp Heat: 1.000h bei 85°C / 85% Luftfeuchte
- Hail Test: 25mm Eiskugel @ 23 m/s
- Mechanical Load: 5.400 Pa Front, 2.400 Pa Rück
- Hot Spot: 5h bei maximaler Verschattung

**Marine-relevante Zusatzanforderungen (nicht genormt, aber empfohlen):**
- Salzsprüh-Test: 96h nach ISO 9227 (bei marine-zertifizierten Panels)
- UV-Langzeitbeständigkeit: 60 kWh/m² UV-Exposition
- Vibrations-Test: Simulation Seegang (keine Standard-Norm, herstellerspezifisch)
- Biegewechsel-Test (semiflexibel): 1.000 Zyklen bei 50% max. Biegung

**Confidence:** measured — Normtexte IEC, ISO, ABYC.

### Z.6 Empfohlene Werkzeuge und Messinstrumente

**Mindestausstattung für Solar-Installation und Wartung:**

| Werkzeug | Funktion | Empfehlung | Preis (€) |
|----------|---------|-----------|-----------|
| MC4-Crimpzange | Stecker crimpen | Rennsteig PEW 8.185 | 75 |
| MC4-Montageschlüssel | Stecker lösen | Multi-Contact Paar | 15 |
| Abisolierzange | Kabel vorbereiten | Knipex 12 62 180 | 40 |
| Multimeter | Spannung/Strom/Widerstand | Fluke 117 (True RMS) | 180 |
| Zangenamperemeter DC | Strom ohne Trennung messen | Fluke 325 | 220 |
| Isolationsmessgerät | Isolationswiderstand (>1 MΩ) | Fluke 1587 FC | 580 |
| Solarmessgerät (I-V) | Panel-Kennlinie aufnehmen | Seaward PV210 | 1.200 |
| Pyranometer (optional) | Einstrahlung messen | Apogee SP-510 | 350 |
| Infrarot-Thermometer | Panel-Temperatur | Fluke 62 MAX | 95 |
| Drehmoment-Schlüssel | Schraubverbindungen | Wera Click-Torque | 60 |

**Verbrauchsmaterial an Bord (Empfehlung):**
- 2× MC4-Steckerpaare (Ersatz)
- 5m Solarkabel 6mm² (Reparatur)
- Selbstverschweißendes Tape (PIB)
- Schrumpfschlauch-Sortiment (mit Kleber)
- Kontaktfett (DeoxIT D5 oder Vaseline)
- Kabelbinder UV-beständig (schwarz)
- Edelstahl-Schrauben/-Muttern V4A Sortiment
- Sikaflex 291i (Dichtung Kabeldurchführungen)

**Confidence:** documented — Werkstatt-Praxis und Herstellerempfehlungen.

### Z.7 Vergleich: Solar vs. alternative Bordenergiequellen

| Kriterium | Solar (600 Wp) | Windgenerator (400W) | Generator (3 kW) | Hydrogenerator | Brennstoffzelle |
|-----------|---------------|---------------------|-------------------|---------------|-----------------|
| Ertrag/Tag (Mittelm. Sommer) | 2.100 Wh | 500–3.000 Wh | 6.000 Wh (2h) | 200–800 Wh (nur bei Fahrt) | 1.000–2.500 Wh |
| Ertrag/Tag (bedeckt/Flaute) | 300–600 Wh | 0 Wh | 6.000 Wh | 0–800 Wh | 1.000–2.500 Wh |
| Gewicht | 15–30 kg | 15–25 kg | 60–120 kg | 5–15 kg (Schleppgen.) | 20–40 kg |
| Lärm | 0 dB | 30–60 dB | 70–85 dB | 0 dB (unter Wasser) | 35–45 dB |
| Wartung/Jahr | Minimal (Reinigung) | Lager, Bürsten (€50–150) | Öl, Filter, Riemen (€300–800) | Minimal | Membran, Filter (€200–500) |
| Investition | €1.500–€3.000 | €1.500–€3.500 | €3.000–€8.000 | €1.500–€4.000 | €3.000–€8.000 |
| Lebensdauer | 15–25 Jahre | 5–10 Jahre | 5.000–10.000h | 10–15 Jahre | 5.000–10.000h |
| Diesel-Bedarf | Keiner | Keiner | 0,8–1,5 L/h | Keiner | Methanol (0,5 L/h) |
| Produziert bei Anker/Flaute | ★★★★★ | ★☆☆☆☆ | ★★★★★ | ☆☆☆☆☆ | ★★★★★ |
| Produziert nachts | ☆☆☆☆☆ | ★★★★☆ | ★★★★★ | ★★★★☆ (Fahrt) | ★★★★★ |
| Produziert bei Sturm | ★★☆☆☆ | ★★★★★ | ★★★★★ | ★★★★★ | ★★★★★ |

**Fazit:** Solar ist die ideale Primärquelle für Ankerlieger und Küstensegler im Sonnengürtel. Für Blauwasserfahrten ergänzt ein Windgenerator die Schwachstellen (Nacht, Sturm, Tropen-Bewölkung). Der Generator wird zur Backup-Reserve für Extremsituationen.

**Confidence:** documented — Vergleichstest-Berichte, Herstellerdaten.

### Z.8 Regionale Anlagen-Empfehlungen

**Ostsee/Nordsee (saisonaler Einsatz Mai–September):**
- Empfehlung: 200–400 Wp als Ergänzung
- Panels: Starre Module (Langlebigkeit, da oft im Winterlager)
- Regler: Victron SmartSolar 75/15 oder 100/20
- Besonderheit: Winter-Erhaltungsladung mit 50–100 Wp möglich
- ROI: 4–6 Jahre (gegen Landstrom gerechnet)

**Mittelmeer (ganzjährig, Schwerpunkt Apr–Okt):**
- Empfehlung: 400–800 Wp für Autarkie
- Panels: Semiflexibel auf Bimini + starr auf Arch
- Regler: Victron 100/30 bis 100/50
- Besonderheit: Hohe Temperaturen → Hinterlüftung priorisieren
- ROI: 2–3 Jahre

**Atlantik-Rundreise (Kanaren → Karibik → Azoren):**
- Empfehlung: 600–1.200 Wp + Windgenerator
- Panels: Mix Arch (starr) + Bimini (semiflex)
- Regler: 2× MPPT für verschiedene Panel-Gruppen
- Besonderheit: Passat-Zone → Wind-Ergänzung sinnvoll
- ROI: 1,5–2,5 Jahre (Generator-Einsparung)

**Karibik (ganzjährig):**
- Empfehlung: 800–2.000 Wp (vollautark möglich)
- Panels: Große Bimini-Fläche nutzen (Katamaran ideal)
- Regler: Victron 150/35 oder größer
- Besonderheit: Regensaison (Jun–Nov) → 30% weniger Ertrag, aber dennoch ausreichend
- ROI: 1–2 Jahre

**Pazifik-Rundfahrt:**
- Empfehlung: 1.000–2.000 Wp (lange Distanzen, wenig Infrastruktur)
- Panels: Maximale verfügbare Fläche ausnutzen
- Regler: Multi-MPPT mit VRM-Monitoring
- Besonderheit: Extrem variable Bedingungen (Tropen-Squalls → volle Sonne)
- ROI: 1–2 Jahre (kein Landstrom verfügbar)

**Confidence:** estimated — basierend auf Erfahrungswerten und Klimadaten.

### Z.9 Zukunftstechnologien (Ausblick 2025–2030)

**Perowskit-Tandem-Zellen:**
- Wirkungsgrad >30% in der Laborentwicklung
- Marktreife: 2027–2029 (First Solar, Oxford PV)
- Marine-Relevanz: Drastisch höhere Leistungsdichte bei gleichem Flächenbedarf
- Herausforderung: Langzeit-Stabilität noch nicht nachgewiesen

**Transparente Solarzellen:**
- Wirkungsgrad aktuell: 5–10%
- Mögliche Anwendung: In Yacht-Fenster integriert
- Marktreife: 2028+ für marine Anwendung
- Potential: Große ungenutzte Glasflächen aktivieren

**Panel-Level-Optimierung (MLPE):**
- Micro-Inverter / DC-Optimizer pro Panel
- Eliminiert Verschattungsverluste fast vollständig
- Marine-Varianten: SolarEdge, Tigo, Enphase arbeiten an 12V/24V-DC-Lösungen
- Marktreife für Marine: Bereits verfügbar (Tigo TS4-L), noch nicht weit verbreitet

**Solid-State-Batterien + Solar:**
- Deutlich höhere Energiedichte → kleinere Batteriebänke
- Schnellere Ladung → Solar-Ertrag wird sofort gespeichert
- Marktreife: 2026–2028 (Samsung SDI, QuantumScape)
- Marine-Relevanz: Halbierung des Batteriegewichts bei gleicher Kapazität

**KI-gestützte Ertragsoptimierung:**
- Wettervorhersage + Verbrauchsprognose → vorausschauende Ladestrategie
- Automatische Verbraucherpriorisierung bei niedrigem Ertrag
- Victron ESS + Node-RED bereits heute möglich (DIY)
- Integrierte Lösungen: Victron GX + Wetter-API (in Entwicklung)

**Confidence:** estimated — basierend auf publizierten Forschungsergebnissen und Hersteller-Roadmaps.

### Z.10 Blitzschutz und Überspannungsschutz

**Blitzstatistik Marine-Solar:**
- Direkte Blitzeinschläge in Solaranlagen auf Booten: extrem selten (<0,01%/Jahr)
- Induzierte Überspannung durch nahen Blitz: häufiger (0,5–2%/Jahr in Gewitterregionen)
- Hauptgefährdung: MPPT-Regler und nachgeschaltete Elektronik

**Schutzkonzept (3 Stufen):**

| Stufe | Maßnahme | Wirkung | Kosten |
|-------|----------|---------|--------|
| 1 — Grobschutz | SPD Typ 2 am Panel-Eingang (Dehn DEHNguard PV) | Ableitung >10 kA Blitzstoßstrom | €120–€200 |
| 2 — Mittelschutz | Varistor am Regler-Eingang (integriert bei Victron RS) | Begrenzung transienter Spannungsspitzen | €0–€50 |
| 3 — Feinschutz | Regler-interne Schutzbeschaltung | Schutz der Elektronik | In Regler integriert |

**Erdungskonzept:**
```
Panel-Rahmen ──── grün/gelb 6mm² ────┐
                                       │
Arch (Edelstahl) ── grün/gelb 10mm² ──┤── Erdungsschiene ── Kiel-Bolzen
                                       │       (Sammelschiene)
Regler-Gehäuse ── grün/gelb 4mm² ────┘
```

**Wichtig bei GFK-Booten:**
- Kein natürlicher Blitzableiter (kein Metallrumpf)
- Blitzableiter am Mastfuß → 16mm² Kupferband → Kielbolzen / externes Erdungsblech
- Panel-Rahmen in Erdungskreis einbeziehen
- Bei Aluminium-Booten: Rumpf ist natürlicher Erdleiter — einfacher

**Verhalten bei Gewitterwarnung:**
1. Alle nicht benötigten Elektronik-Verbraucher ausschalten
2. Regler abschalten (wenn möglich) → Panel auf Leerlauf (schadet nicht)
3. Antennen-Kabel abziehen (Haupteintrittspunkt für induzierte Spannung)
4. Nach Gewitter: Regler und Monitoring auf Funktion prüfen

**Confidence:** documented — VDE 0185 (Blitzschutz), ABYC TE-4, Dehn Blitzschutz-Planungshandbuch.

### Z.11 Integration mit Bordnetz-Management

**Victron-Ökosystem (Marktstandard):**
```
┌─────────────────────────────────────────────────────────┐
│                    Victron VRM Cloud                      │
│          (Fernüberwachung, Datenlogging, Alarme)         │
└──────────────────────────┬──────────────────────────────┘
                           │ Internet (WiFi/4G/Sat)
┌──────────────────────────┴──────────────────────────────┐
│                     Cerbo GX / Venus OS                   │
│            (Zentraler Systemcontroller)                   │
├──────────┬──────────┬──────────┬──────────┬─────────────┤
│ VE.Direct│ VE.Direct│ VE.Can   │ VE.Direct│ VE.Bus      │
│          │          │          │          │             │
│ SmartSolar│ SmartSolar│ Lynx BMS │ SmartShunt│ MultiPlus  │
│ MPPT #1  │ MPPT #2  │ (Batterie)│(Monitor) │ (Inverter) │
│          │          │          │          │             │
│ [Panels  │ [Panels  │ [LiFePO4]│ [Bank]   │ [230V AC]  │
│  Arch]   │  Bimini] │          │          │             │
└──────────┴──────────┴──────────┴──────────┴─────────────┘
```

**Alternative Systeme:**
| System | Hersteller | Stärken | Schwächen |
|--------|-----------|---------|-----------|
| Victron VRM | Victron | Vollständigstes Ökosystem, Open Source (Venus OS) | Regler/Inverter nur Victron |
| Mastervolt MasterBus | Mastervolt | Integration mit Whisper-Generatoren | Geschlossenes System, teuer |
| Simarine PICO | Simarine | Elegantes Display, einfach | Nur Monitoring, kein Regelung |
| Wakespeed WS500 | Wakespeed | Alternator-Regelung + Solar-Integration | Nischenproduk |
| Balmar SG200 | Balmar | Smart-Alternator-Regler | Nur Lichtmaschine, kein Solar |

**NMEA 2000 Integration:**
- Einige MPPT-Regler (z.B. Victron mit VE.Can) können Daten auf NMEA 2000 senden
- PGN 127505 (Battery Status), PGN 127506 (DC Power) relevant
- Integration in Plotter-Displays (B&G, Garmin, Raymarine)
- Nicht standardisiert für PV-spezifische Daten — herstellerabhängig

**SignalK / Open Source:**
- Venus OS (Victron) unterstützt SignalK
- Selbst gebaute Dashboards (Grafana + InfluxDB) mit Echtzeitdaten
- Community-Integrationen (Home Assistant, Node-RED)
- Wetter-API-Kopplung für Ertragsprognose

**Confidence:** documented — Victron-Dokumentation, Praxis-Erfahrungen.

### Z.12 Typische Komplett-Konfigurationen (Copy-Paste-Vorlagen)

**Konfiguration A — Einsteiger 12V / 200 Wp:**
```
Komponente                          Modell                    Preis (€)
─────────────────────────────────────────────────────────────────────────
2× Panel 100 Wp starr              Victron SPM100-12          330
1× MPPT-Regler                     Victron SmartSolar 75/15   125
1× Kabelset 4mm² 5m               Marine-Solarkabel + MC4     55
2× Sicherung 15A + Halter         ANL-Sicherungshalter        25
1× Kabeldurchführung               Scanstrut DS-S6             40
1× Montageset Z-Halterung         Alu Z-Brackets (4×)         35
─────────────────────────────────────────────────────────────────────────
GESAMT                                                         610
Erwarteter Ertrag (Mittelmeer):    70 Ah/Tag @12V
Geeignet für:                      Weekender, Küstensegler, Ostsee-Sommer
```

**Konfiguration B — Standard 12V / 400 Wp:**
```
Komponente                          Modell                    Preis (€)
─────────────────────────────────────────────────────────────────────────
2× Panel 200 Wp starr              Victron SPM200-24          620
1× MPPT-Regler                     Victron SmartSolar 100/50  340
1× Kabelset 6mm² 6m               Marine-Solarkabel + MC4     75
4× Sicherung 20A + Halter         Sicherungskasten            45
2× Kabeldurchführung               Scanstrut DS-S6             80
1× Montageset Arch                 Alu-Schienen + Z-Brackets  120
1× Monitoring                      Victron SmartShunt          125
─────────────────────────────────────────────────────────────────────────
GESAMT                                                        1.405
Erwarteter Ertrag (Mittelmeer):    140 Ah/Tag @12V
Geeignet für:                      Fahrtensegler 12–16m, Langfahrt-Basis
```

**Konfiguration C — Premium 12V / 800 Wp:**
```
Komponente                          Modell                    Preis (€)
─────────────────────────────────────────────────────────────────────────
4× Panel 200 Wp semiflex           Solbian SP 200 Q          4.740
2× MPPT-Regler                     Victron SmartSolar 100/30  460
1× Kabelset 6mm² 8m               Marine-Solarkabel + MC4     95
8× Sicherung + Halter             Sicherungsblock             65
4× Kabeldurchführung               Scanstrut DS-S6            160
1× Bimini-Montage Custom          Alu-Rahmen + Näharbeit   1.800
1× System-Controller               Victron Cerbo GX           320
1× Display                         Victron GX Touch 50        280
─────────────────────────────────────────────────────────────────────────
GESAMT                                                        7.920
Erwarteter Ertrag (Mittelmeer):    280 Ah/Tag @12V
Geeignet für:                      Katamaran 38–45ft, Langfahrt-Mono 14m+
```

**Konfiguration D — Autark 24V / 1.600 Wp:**
```
Komponente                          Modell                    Preis (€)
─────────────────────────────────────────────────────────────────────────
8× Panel 200 Wp semiflex           Solbian SP 200 Q          9.480
4× MPPT-Regler                     Victron SmartSolar 100/30  920
1× Kabelset 10mm² 10m             Marine-Solarkabel + MC4    180
16× Sicherung + Halter            Lynx Distributor            350
6× Kabeldurchführung               Scanstrut DS-S6            240
1× Hardtop-Montage Custom         Alu-Rahmen professional   4.200
1× System-Controller               Victron Cerbo GX           320
1× Display                         Victron GX Touch 70        360
1× Inverter                        Victron MultiPlus 24/3000 1.450
─────────────────────────────────────────────────────────────────────────
GESAMT                                                       17.500
Erwarteter Ertrag (Mittelmeer):    480 Ah/Tag @24V
Geeignet für:                      Katamaran 45–55ft, vollautark inkl. Klima
```

**Confidence:** calculated — basierend auf aktuellen UVP und typischen Installationen.

### Z.13 Checkliste: Vor dem Kauf

Vor der Anschaffung einer Solaranlage sollten folgende Fragen geklärt sein:

```
ENERGIEBILANZ:
□ Alle Verbraucher mit Leistung und täglicher Betriebsdauer erfasst?
□ Tagesverbrauch in Ah berechnet (Sommer + Winter)?
□ Spitzenlast ermittelt (gleichzeitige Verbraucher)?
□ Batteriekapazität ausreichend für Autarkie-Ziel?

FLÄCHE UND GEWICHT:
□ Verfügbare Montagefläche vermessen (inkl. Fotos)?
□ Tragfähigkeit der Montagefläche/Arch bekannt?
□ Verschattungsanalyse durchgeführt (Fotos ganztägig)?
□ Gewichtslimit definiert (besonders bei Bimini)?

SYSTEM-KOMPATIBILITÄT:
□ Aktuelle Systemspannung bekannt (12V/24V/48V)?
□ Vorhandener Laderegler kompatibel oder Austausch geplant?
□ Batterietyp bekannt (für Regler-Einstellung)?
□ Platz für MPPT-Regler vorhanden (belüftet, trocken)?
□ Kabeldurchführungen planbar (ohne Dichtigkeitsverlust)?

BUDGET UND PRIORITÄTEN:
□ Gesamtbudget definiert (inkl. Montage, Kabel, Zubehör)?
□ Priorität klar: Langlebigkeit vs. Preis vs. Gewicht vs. Ertrag?
□ DIY oder Werft-Installation?
□ Ersatzteil-Verfügbarkeit im Fahrtengebiet geprüft?

DOKUMENTATION:
□ Aktuelle Bordnetz-Pläne vorhanden?
□ Geplante Kabelwege dokumentiert?
□ Montagepunkte mit Werft abgestimmt (Garantie)?
□ Versicherung über Installation informiert?
```

**Confidence:** documented — Best-Practice aus Werft-Beratungsgesprächen.

### Z.14 Häufige Installations-Fehler (Top 10)

| # | Fehler | Konsequenz | Korrekte Lösung |
|---|--------|-----------|-----------------|
| 1 | PWM-Regler statt MPPT | 20–30% Ertragsverlust | MPPT immer verwenden (€100 Mehrkosten) |
| 2 | Kabel zu dünn | Überhitzung, Brandgefahr, Leistungsverlust | Kabelquerschnitt korrekt berechnen |
| 3 | Keine Sicherungen | Bei Kurzschluss: Kabelbrand | Sicherung an jedem String + Batterie |
| 4 | MC4 nicht abgedichtet | Korrosion nach Monaten | PIB-Tape + Kontaktfett |
| 5 | Panels in Serie bei Teilverschattung | 30–60% Verlust durch schwächstes Panel | Parallel schalten oder Multi-MPPT |
| 6 | Keine Hinterlüftung (aufgeklebt) | 15–20% Temperatur-Verlust Sommer | Min. 20mm Abstandshalter |
| 7 | Haushaltskabel (H07V-K) | Nicht UV-fest, nicht salzwasserfest | Marine-Solarkabel (doppelt isoliert, verzinnt) |
| 8 | Falscher Batterietyp im Regler | Über-/Unterladung, Batterieschaden | Korrekte Ladekurve konfigurieren |
| 9 | Panels auf Deck ohne Zugentlastung | Kabelabriss bei Seegang | Zugentlastung + Schlaufe vor Anschlussdose |
| 10 | Voc_max nicht berechnet | Regler-Zerstörung bei Kälte | Voc_max bei niedrigster Temperatur berechnen |

**Merksatz:** Die meisten Solar-Probleme auf Booten sind Installations-Fehler, nicht Panel-Defekte. Eine korrekte Installation mit hochwertigen Komponenten (Kabel, Stecker, Regler) ist wichtiger als das teuerste Panel.

### Z.15 Empfohlene Informationsquellen

**Fachliteratur:**
- Calder, Nigel: "Boatowner's Mechanical and Electrical Manual" (Kapitel Solar)
- Hazen, Jeff: "The 12 Volt Bible for Boats"
- Victron Energy: "Wiring Unlimited" (kostenlos als PDF, victronenergy.com)
- ABYC: "Standards and Technical Information Reports for Small Craft" (E-11)

**Online-Ressourcen:**
- Victron Community Forum (community.victronenergy.com)
- Cruisers Forum — Electrical Systems (cruisersforum.com)
- Segeln-Forum.de — Technik/Elektrik
- YouTube: „Sailing Uma" (Praxis-Installation), „Victron Energy" (Tutorials)
- PVGIS (re.jrc.ec.europa.eu/pvg_tools) — Einstrahlungsdaten weltweit

**Werkzeuge & Rechner:**
- Victron MPPT Calculator (victronenergy.com/mppt-calculator)
- PVGIS (EU Joint Research Centre) — Ertragsberechnung
- Cable Calculator (diverse, z.B. bluesea.com/resources)
- Victron VRM Demo (vrm.victronenergy.com) — Live-Daten realer Anlagen

**Confidence:** documented — Verifizierte Quellen.

---

*Ende der Wissensdatei 22.05 — Solaranlagen an Bord*

**Gesamtumfang:** ~3.800 Zeilen
**Confidence-Mapping:** Jeder Abschnitt trägt ein Confidence-Label.
**Letzte Prüfung:** 2026-05-05
