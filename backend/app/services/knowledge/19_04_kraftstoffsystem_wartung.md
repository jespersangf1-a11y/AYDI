---
title: "Kraftstoffsystem Wartung und Troubleshooting"
kategorie: "19 Kraftstoffsystem"
unterkategorie: "04 Wartung und Troubleshooting"
version: "1.0.0"
datum: "2026-05-02"
autor: "AYDI Research"
status: "validated"
bereich: "Antrieb & Kraftstoff"
confidence_quellen:
  - measured: "Hersteller-TDS, Labormessungen, EN 590 Prüfberichte"
  - documented: "Hersteller-Kataloge, Service-Bulletins, Werft-Dokumentation"
  - estimated: "Erfahrungswerte Motorenmechaniker, Forum-Konsens"
  - benchmark: "Charterflotten-Statistiken, Versicherungsdaten"
tags:
  - kraftstoffsystem
  - wartung
  - troubleshooting
  - dieselpest
  - biozid
  - grotamar
  - tankpolieren
  - fuel_polishing
  - winterfestmachung
  - racor
  - filter
  - kraftstoffqualitaet
  - mikrobielle_kontamination
  - tankinspektion
  - langzeitlagerung
cross_references:
  - "06_04_kraftstoffschlaeuche.md"
  - "01_08_motordichtungen.md"
  - "07_04_seewasserfilter.md"
  - "07_05_schlauchverbindungen.md"
---

# 19.04 — Kraftstoffsystem Wartung und Troubleshooting: Gesamtsystem-Wartung, Dieselpest-Bekämpfung, Winterfestmachung, Systemdiagnose

> **AYDI Wissensdatei 19.04** — Kategorie 19: Kraftstoffsystem
> **Confidence-Quelle:** measured (Hersteller-TDS, Labormessungen), documented (Hersteller-Kataloge, Service-Bulletins), estimated (Erfahrungswerte)
> **Letzte Aktualisierung:** 2026-05-02

---

## Inhaltsverzeichnis

1. [Einführung und Übersicht](#1-einführung-und-übersicht)
2. [Grundlagen und Theorie](#2-grundlagen-und-theorie)
3. [Typenübersicht — Wartungsintervalle und Maßnahmen](#3-typenübersicht--wartungsintervalle-und-maßnahmen)
4. [Produktlinien und Spezifikationen](#4-produktlinien-und-spezifikationen)
5. [Hersteller-Datenbank](#5-hersteller-datenbank)
6. [Fehlerbild-Atlas](#6-fehlerbild-atlas)
7. [Troubleshooting-Entscheidungsbäume](#7-troubleshooting-entscheidungsbäume)
8. [FAQ](#8-faq)
9. [Glossar](#9-glossar)
10. [Schnell-Referenz](#10-schnell-referenz)
11. [Anhänge A–H — Fallstudien](#11-anhänge-ah--fallstudien)
12. [Anhänge I–R — Pydantic v2 Modelle](#12-anhänge-ir--pydantic-v2-modelle)

---

## 1. Einführung und Übersicht

### 1.1 Bedeutung der Kraftstoffsystem-Wartung

Das Kraftstoffsystem einer Yacht ist das zentrale Versorgungssystem für den Hauptantrieb und — bei vielen Booten — auch für den Generator. Kraftstoffprobleme sind die häufigste Ursache für Motorausfälle auf See. Im Gegensatz zum Automobil-Bereich, wo Tankstellen verlässlich sauberen Kraftstoff liefern und die Standzeiten zwischen Tankfüllungen kurz sind, muss das marine Kraftstoffsystem mit deutlich widrigeren Bedingungen umgehen: wechselnde Kraftstoffqualität internationaler Häfen, lange Standzeiten, permanente Feuchtigkeit, Temperaturschwankungen und die Kondensation von Wasser in teilgefüllten Tanks.

**Kernstatistiken zur Wartungsrelevanz (Confidence: benchmark):**

| Aspekt | Wert | Quelle |
|--------|------|--------|
| Motorausfälle durch Kraftstoffprobleme | 42–58 % | RNLI-Statistiken, ADAC Wassersport |
| Häufigste Ursache: verstopfte Filter | 31 % aller Kraftstoff-Ausfälle | Charterflotten-Analyse, 3.800 Fälle |
| Häufigste Ursache: Dieselpest | 24 % aller Kraftstoff-Ausfälle | Volvo Penta Service Data 2024 |
| Häufigste Ursache: Wassergehalt | 19 % aller Kraftstoff-Ausfälle | Yanmar Marine Service Report |
| Durchschnittliche Reparaturkosten (Einspritzsystem) | 2.500–8.500 EUR | Werft-Statistiken DACH 2024 |
| Durchschnittliche Wartungskosten (jährlich) | 120–380 EUR | AYDI Kalkulation |
| ROI jährlicher Systemwartung | 8:1 bis 22:1 | Lebensdauervergleich |
| Dieselpest-Sanierung (Komplett) | 1.800–6.500 EUR | Werft-Daten 2023–2025 |

### 1.2 Systemüberblick — Komponenten und Flussrichtung

Ein typisches marines Kraftstoffsystem besteht aus folgenden Hauptkomponenten in Flussrichtung:

```
Einfüllstutzen (Deck)
    │
    ▼
Einfüllleitung (ABYC H-33 / ISO 21487)
    │
    ▼
Kraftstofftank (Aluminium / Edelstahl / GFK / Polyethylen)
    │                          │
    ▼                          ▼
Tankentlüftung ◄──────── Sichtglas / Peiltab
    │
    ▼
Absperrventil (Tankauslass)
    │
    ▼
Vorfilter / Wasserabscheider (Racor, Separ, Delphi)
    │                          │
    ▼                          ▼
Primärfilter (10 µm)    Wassersammelglas
    │
    ▼
Kraftstoff-Förderpumpe (mechanisch oder elektrisch)
    │
    ▼
Sekundärfilter / Feinfilter (2–5 µm, am Motor)
    │
    ▼
Einspritzpumpe / Common-Rail-System
    │
    ▼
Einspritzdüsen
    │
    ▼
Rücklaufleitung
    │
    ▼
Kraftstofftank (Rücklauf)
```

### 1.3 Besondere Herausforderungen im Marinebetrieb

**Verglichen mit Straßenfahrzeugen:**

| Faktor | PKW | Yacht | Auswirkung |
|--------|-----|-------|------------|
| Standzeit Kraftstoff | Tage bis Wochen | Wochen bis Monate | Alterung, Wasseraufnahme, mikrobielle Kontamination |
| Tankfüllstand-Schwankung | Gering (häufiges Tanken) | Hoch (voll→leer→voll) | Kondensation an Tankwänden |
| Bewegung/Vibration | Straßenunebenheiten | Seegang, Rollen, Stampfen | Aufwirbeln von Sedimenten, Schlammbildung |
| Umgebungsfeuchtigkeit | 40–60 % rel. | 60–95 % rel. | Wasseraufnahme durch Tankbelüftung |
| Kraftstoffqualität | DIN EN 590 kontrolliert | International variabel | Verunreinigungen, abweichende Spezifikationen |
| Betriebstemperatur | Schnell Betriebstemp. | Lange Kaltlaufphasen | Unvollständige Verbrennung, Verkokung |
| Salzbelastung | Keine | Permanent | Korrosion aller metallischen Komponenten |
| Biodiesel-Anteil | B7 in DE (7 % FAME) | B0 bis B20+ (je nach Land) | Wasseraufnahme, Dichtungsverträglichkeit |

### 1.4 Kostenfolgen der Vernachlässigung

**Degradationsstufen eines vernachlässigten Kraftstoffsystems:**

**Stufe 1 — Schleichende Verschlechterung (0–12 Monate ohne Wartung):**
- Filter sättigt sich langsam
- Leichter Leistungsverlust (3–8 %) unter Volllast
- Erhöhter Kraftstoffverbrauch (5–12 %)
- Gelegentliches Rußen im Auspuff
- Geschätzte Zusatzkosten: 200–500 EUR/Saison (Mehrverbrauch)

**Stufe 2 — Funktionseinschränkung (12–24 Monate ohne Wartung):**
- Filter stark gesättigt, Druckdifferenz erhöht
- Spürbarer Leistungsverlust (10–25 %)
- Motor stottert bei hoher Last oder Seegang
- Erste mikrobielle Kontamination im Wasserabscheider sichtbar
- Geschätzte Zusatzkosten: 500–1.500 EUR (Filteraustausch + Reinigung)

**Stufe 3 — Akuter Ausfall (24–48 Monate ohne Wartung):**
- Motorausfall durch verstopften Filter bei Seegang
- Dieselpest hat Tank kontaminiert
- Einspritzdüsen verschmutzt oder beschädigt
- Rücklaufleitungen verklebt
- Geschätzte Reparaturkosten: 2.500–8.500 EUR

**Stufe 4 — Systemschaden (48+ Monate ohne Wartung):**
- Tankinnenwände korrodiert (bei Aluminium/Stahl)
- Einspritzpumpe beschädigt durch abrasive Partikel
- Common-Rail-System kompromittiert (Druckverlust)
- Kompletter Tanktausch und Motor-Einspritzsystem-Überholung
- Geschätzte Reparaturkosten: 8.000–25.000+ EUR

### 1.5 Geltungsbereich dieser Wissensdatei

Diese Wissensdatei behandelt:
- **Diesel-Kraftstoffsysteme** im Marinebetrieb (Segelboote, Motorboote, Superyachten)
- **Wartungsintervalle** nach Betriebsstunden und Kalenderzeit
- **Dieselpest** (mikrobielle Kontamination): Erkennung, Behandlung, Prävention
- **Winterfestmachung** und Langzeiteinlagerung
- **Fuel Polishing** (Kraftstoffaufbereitung)
- **Systemdiagnose** und Troubleshooting
- **Produkte und Hersteller** für Wartung und Behandlung

Nicht behandelt werden:
- Benzin-Kraftstoffsysteme (eigene Wissensdatei 19_05)
- LPG/CNG-Systeme (Wissensdatei 19_06)
- Tankbau und -installation (Wissensdatei 19_01)
- Kraftstoffleitungen und -schläuche im Detail (siehe 06_04_kraftstoffschlaeuche.md)

---

## 2. Grundlagen und Theorie

### 2.1 Dieselkraftstoff — Zusammensetzung und Normen

#### 2.1.1 EN 590 — Europäische Dieselnorm

Die europäische Norm EN 590 definiert die Mindestanforderungen an Dieselkraftstoff. Für den Marinebetrieb sind folgende Parameter besonders relevant:

**Schlüsselparameter EN 590:2022 (Confidence: measured):**

| Parameter | Grenzwert | Marine-Relevanz |
|-----------|-----------|-----------------|
| Cetanzahl | ≥ 51 | Kaltstart, Verbrennungsqualität |
| Dichte bei 15 °C | 820–845 kg/m³ | Einspritzmengenberechnung |
| Viskosität bei 40 °C | 2,0–4,5 mm²/s | Schmierung Einspritzpumpe |
| Flammpunkt | ≥ 55 °C | Sicherheit (ISO 9094) |
| Wassergehalt | ≤ 200 mg/kg (0,02 %) | Korrosion, Mikrobenwachstum |
| Gesamtverschmutzung | ≤ 24 mg/kg | Filterverstopfung |
| Schwefelgehalt | ≤ 10 mg/kg | Emissionen, Schmierung |
| FAME-Anteil (Biodiesel) | ≤ 7 % (B7) | Wasseraufnahme, Alterung |
| Oxidationsstabilität | ≥ 20 h (Rancimat) | Lagerfähigkeit |
| CFPP (Kältefilterverstopfung) | Saisonabhängig (-20 bis 0 °C) | Winterbetrieb |
| Schmierfähigkeit (HFRR) | ≤ 460 µm | Einspritzpumpenverschleiß |
| Aschegehalt | ≤ 0,01 % | Rußbildung |

#### 2.1.2 Biodiesel-Problematik (FAME — Fatty Acid Methyl Ester)

Seit der EU-Richtlinie 2009/28/EG ist Biodiesel-Beimischung in Europa Standard. Für den Marinebetrieb ist dies problematisch:

**Biodiesel-Anteile in europäischen Ländern (Confidence: documented, Stand 2025):**

| Land | Standard | Max. FAME | Besonderheit |
|------|----------|-----------|--------------|
| Deutschland | B7 | 7 % | Ganzjährig |
| Niederlande | B7 | 7 % | HVO als Alternative zunehmend |
| Frankreich | B7–B10 | 10 % (zunehmend) | B10 an Autobahntankstellen |
| Italien | B7 | 7 % | Qualität regional sehr unterschiedlich |
| Spanien | B7 | 7 % | Heizöl als Marine-Diesel verbreitet |
| Kroatien | B7 | 7 % | Hafentankstellen oft geringere Qualität |
| Griechenland | B7 | 7 % | Verunreinigungen in kleinen Häfen |
| Türkei | B0–B5 | 5 % | Kein einheitlicher Standard |
| Schweden | B7–B100 | Bis 100 % | HVO100 verbreitet (unproblematisch) |
| Norwegen | B7 | 7 % | Arktik-Diesel mit Additiven |

**Probleme durch Biodiesel im Marinebetrieb:**

1. **Hygroskopie**: FAME absorbiert 20–30× mehr Wasser als fossiler Diesel
   - Reiner Diesel: ~60 ppm Wasseraufnahme
   - B7: ~200 ppm Wasseraufnahme
   - B20: ~600 ppm Wasseraufnahme
   - B100: ~1.500 ppm Wasseraufnahme

2. **Oxidationsstabilität**: FAME oxidiert schneller als fossiler Diesel
   - Lagerfähigkeit B0: 12–18 Monate
   - Lagerfähigkeit B7: 6–12 Monate
   - Lagerfähigkeit B20: 3–6 Monate
   - Lagerfähigkeit B100: 2–4 Monate

3. **Dichtungsverträglichkeit**: FAME löst bestimmte Elastomere an
   - Nitril (NBR): bedingt verträglich (Quellung 5–15 %)
   - Viton (FKM): gut verträglich
   - EPDM: nicht verträglich (Quellung >30 %)
   - PTFE: voll verträglich

4. **Mikrobielle Anfälligkeit**: FAME bietet Nährstoff für Mikroorganismen
   - Fettsäuren als Kohlenstoffquelle
   - Höherer Wassergehalt als Lebensraum
   - Beschleunigtes Dieselpest-Risiko um Faktor 3–5

5. **Kälteprobleme**: FAME-Kristallisation bei niedrigen Temperaturen
   - CFPP von B7 ca. 2–5 °C höher als B0
   - Paraffinausflockung bei Temperaturabfall

#### 2.1.3 HVO — Hydrierte Pflanzenöle als Alternative

HVO-Diesel (EN 15940) bietet eine deutlich bessere Marine-Tauglichkeit als FAME-haltiger Diesel:

| Eigenschaft | EN 590 (B7) | HVO (EN 15940) | Vorteil Marine |
|-------------|-------------|----------------|----------------|
| Wasseraufnahme | ~200 ppm | ~50 ppm | Geringere Korrosion |
| Lagerfähigkeit | 6–12 Monate | 18–36 Monate | Ideal für Saisonbetrieb |
| Cetanzahl | 51–55 | 70–90 | Besserer Kaltstart |
| CFPP | -10 bis -20 °C | -25 bis -40 °C | Besserer Winterbetrieb |
| Mikrobielle Anfälligkeit | Mittel–Hoch | Sehr gering | Kaum Dieselpest |
| Dichtungsverträglichkeit | Prüfen bei >B7 | Volle Verträglichkeit | Keine Quellung |
| Geruch | Typisch Diesel | Nahezu geruchlos | Komfort unter Deck |

**Empfehlung (Confidence: documented):** Wo verfügbar, ist HVO-Diesel (z.B. Neste MY Renewable Diesel, Shell GTL Fuel) für Yachten die technisch überlegene Wahl.

### 2.2 Kraftstoffalterung — Mechanismen und Erkennung

#### 2.2.1 Chemische Alterungsmechanismen

Dieselkraftstoff ist ein komplexes Gemisch aus hunderten Kohlenwasserstoffverbindungen. Mit der Zeit laufen folgende Degradationsprozesse ab:

**1. Autoxidation (Hauptmechanismus):**
- Radikalkettenreaktion mit Luftsauerstoff
- Katalysiert durch Kupfer, Eisen, UV-Licht, Wärme
- Bildet Peroxide → Aldehyde → Carbonsäuren → polymere Ablagerungen
- Geschwindigkeit verdoppelt sich pro 10 °C Temperaturerhöhung (van't Hoff)
- Beginnt typisch nach 3–6 Monaten (B0) bzw. 2–4 Monaten (B7)

**2. Säurebildung:**
- Oxidationsprodukte reagieren zu organischen Säuren
- pH-Wert sinkt von ~7,0 auf 4,5–5,5
- Greift Kupfer-Dichtungen, Aluminium-Tanks und Einspritzkomponenten an
- Messbar als Total Acid Number (TAN) — kritisch ab >0,5 mg KOH/g

**3. Sedimentbildung (Gum & Lacquer):**
- Polymere Oxidationsprodukte fallen aus
- Bilden gummiartige, klebrige Ablagerungen
- Verstopfen Filter, Leitungen, Düsen
- Nicht rückgängig zu machen — nur mechanische Reinigung

**4. Wasseraufnahme und Phasentrennung:**
- Diesel nimmt Feuchtigkeit aus der Umgebungsluft auf
- Gelöst: ~60 ppm bei 20 °C (unsichtbar)
- Emulgiert: 60–500 ppm (Diesel wird trüb/milchig)
- Freies Wasser: >500 ppm (separiert sich am Tankboden)
- Emulgiertes und freies Wasser → Korrosion + Mikrobenwachstum

#### 2.2.2 Visuelle Beurteilung der Kraftstoffqualität

**Diagnosetabelle — Kraftstoff-Zustand nach optischer Bewertung (Confidence: estimated):**

| Erscheinung | Diagnosis | Maßnahme | Dringlichkeit |
|-------------|-----------|----------|---------------|
| Klar, bernsteinfarben | Kraftstoff in Ordnung | Keine | — |
| Leicht dunkel, klar | Beginnende Alterung | Stabilisator zugeben | Gering |
| Trüb, milchig | Wasser emulgiert | Wasserabscheider entleeren, Ursache finden | Mittel |
| Dunkelbraun, klar | Fortgeschrittene Oxidation | Fuel Polishing empfohlen | Mittel |
| Dunkelbraun, trüb | Oxidation + Wasser | Fuel Polishing + Wasserentfernung | Hoch |
| Schwarze Partikel schwimmend | Mikrobielle Kontamination (Dieselpest) | Biozid + Fuel Polishing + Tankreinigung | Hoch |
| Schwarzer Schleim/Gel am Filterglas | Dieselpest fortgeschritten | Komplette Systemreinigung | Sehr hoch |
| Wachsig, dickflüssig | Paraffin-Ausflockung (Kälte) | Aufwärmen, Kälte-Additiv | Hoch |
| Rötlich/Rosa | Heizöl-Beimischung | Prüfen ob zulässig, Motorverträglichkeit | Mittel |
| Geruch nach faulen Eiern | H₂S durch Sulfatreduzierer | Sofortige Tankreinigung, Biozid | Sehr hoch |

#### 2.2.3 Laboranalyse — Wann und Was

**Empfohlene Laboranalyse-Intervalle:**

| Situation | Analyseumfang | Kosten (ca.) | Turnaround |
|-----------|---------------|--------------|------------|
| Jährliche Routineprüfung | Basis (Wasser, Verschmutzung, Cetanzahl) | 45–80 EUR | 3–5 Werktage |
| Verdacht auf Kontamination | Erweitert (+ Mikrobientest, TAN) | 80–150 EUR | 5–7 Werktage |
| Nach Tanken im Ausland | Schnelltest (Wasser, Dichte, Flammpunkt) | 25–40 EUR | 1–3 Werktage |
| Vor Saisonstart nach Einlagerung | Vollanalyse | 120–250 EUR | 5–10 Werktage |
| Schadensfall/Reklamation | Forensische Analyse | 250–500 EUR | 7–14 Werktage |

**Empfohlene Labore für marine Kraftstoffanalyse (DACH):**
- SGS Hamburg — Maritimer Bereich, EN 590 Vollanalyse
- Intertek Lintorf — Marine Fuel Testing
- OELCHECK Brannenburg — Verschleißteilchenanalyse inklusive
- Spectro Scientific (Vertrieb: Ölüberwachung GmbH) — On-Site-Testgeräte

### 2.3 Mikrobielle Kontamination — Die Dieselpest

#### 2.3.1 Biologie der Dieselpest

Die sogenannte "Dieselpest" (englisch: Diesel Bug, Microbial Contamination) ist eine mikrobiologische Kontamination des Kraftstoffsystems durch Pilze, Hefen und Bakterien. Diese Organismen leben an der Grenzschicht zwischen Wasser und Diesel und nutzen Kohlenwasserstoffe als Nahrungsquelle.

**Primäre Organismen (Confidence: measured — mikrobiologische Studien):**

**1. Hormoconis resinae (früher Cladosporium resinae / Amorphotheca resinae):**
- **Typ:** Askomyzet (Schlauchpilz)
- **Erscheinung:** Dunkelbraune bis schwarze, fadenförmige Matten
- **Wachstumsrate:** Verdopplung alle 6–12 Stunden bei optimalen Bedingungen
- **Optimale Temperatur:** 25–35 °C (wächst aber auch bei 10–40 °C)
- **pH-Toleranz:** 3,0–8,5 (optimal 5,0–7,0)
- **Nährstoffbedarf:** Kohlenwasserstoffe C₉–C₃₆, bevorzugt Alkane
- **Wasseranforderung:** Mindestens ~200 ppm freies Wasser
- **Besonderheit:** Häufigster Organismus in Diesel-Systemen weltweit
- **Mycel:** Kann Metallteile durchdringen, Filtermembranen verstopfen
- **Säureproduktion:** Organische Säuren (pH-Senkung des Kraftstoffs)
- **Biofilm:** Bildet stabile, zähe Biofilme auf Tankwänden

**2. Cladosporium-Arten (C. cladosporioides, C. herbarum):**
- **Typ:** Deuteromyzet (Fungi imperfecti)
- **Erscheinung:** Olivgrüne bis dunkelbraune Kolonien
- **Wachstumsrate:** Langsamer als H. resinae, aber kältetolerant
- **Optimale Temperatur:** 18–28 °C (wächst bei 4–35 °C)
- **Besonderheit:** Häufig in nordeuropäischen Gewässern
- **Kann Dichtungsmaterialien angreifen**

**3. Yarrowia lipolytica (Hefe):**
- **Typ:** Askomyzeten-Hefe
- **Erscheinung:** Cremefarbene, schleimige Kolonien
- **Wachstumsrate:** Sehr schnell, Verdopplung alle 2–4 Stunden
- **Besonderheit:** Baut besonders effektiv FAME (Biodiesel) ab
- **Säureproduktion:** Zitronensäure, Isozitronensäure

**4. Pseudomonas aeruginosa (Bakterium):**
- **Typ:** Gram-negatives Stäbchenbakterium
- **Erscheinung:** Grünliche Verfärbung, fluoreszierend unter UV
- **Besonderheit:** Bildet Pyocyanin (bläulich-grün), extrem robust
- **Biofilm:** Einer der stärksten Biofilmbildner
- **Gesundheitsrisiko:** Opportunistisch pathogen — Handschuhe tragen!

**5. Desulfovibrio (Sulfatreduzierende Bakterien — SRB):**
- **Typ:** Gram-negatives, anaerobes Bakterium
- **Erscheinung:** Schwarze Verfärbung (Eisensulfid), H₂S-Geruch
- **Besonderheit:** Wächst anaerob unter dem Biofilm anderer Organismen
- **Korrosion:** Extrem aggressiv — Mikrobiell induzierte Korrosion (MIC)
- **Kann Aluminium-Tanks innerhalb weniger Jahre durchlöchern**

#### 2.3.2 Wachstumsbedingungen und Einflussfaktoren

**Voraussetzungen für Dieselpest-Wachstum:**

```
                    Nährstoffe
                   (Diesel / FAME)
                        │
                        ▼
    Wasser ────────► WACHSTUM ◄──────── Temperatur
  (≥200 ppm frei)      │               (10–40 °C)
                        ▼
                   Kontamination
                   (Inokulation)
```

**Einflussfaktoren-Matrix (Confidence: documented):**

| Faktor | Geringes Risiko | Mittleres Risiko | Hohes Risiko |
|--------|-----------------|-------------------|--------------|
| Kraftstofftyp | HVO, GTL | B0–B7 fossil | B10+ / reiner Biodiesel |
| Wassergehalt | <100 ppm | 100–500 ppm | >500 ppm / freies Wasser |
| Standzeit | <3 Monate | 3–6 Monate | >6 Monate |
| Tankfüllstand | >90 % | 50–90 % | <50 % (große Lufträume) |
| Temperatur | <10 °C konstant | 10–25 °C | 25–35 °C / stark wechselnd |
| Tankmaterial | Edelstahl 316L | GFK / Polyethylen | Aluminium (Korrosion!) |
| Vorgeschichte | Nie Dieselpest | Einmal behandelt | Wiederholt behandelt |
| Belüftung | Geschlossen mit Trockner | Standard-Entlüftung | Offene Entlüftung ohne Filter |

#### 2.3.3 Stadien der Dieselpest

**Stadium 1 — Latente Kontamination (Confidence: estimated):**
- Zeitraum: Monate 0–6 nach Inokulation
- Keimzahl: <10⁴ KBE/ml (Kolonie-bildende Einheiten)
- Optisch: Kraftstoff erscheint noch normal
- Filter: Normale Standzeit
- Diagnose: Nur durch Labortest erkennbar (z.B. FUELSTAT-Test)
- Maßnahme: Biozid-Prophylaxe, Wasserabscheider regelmäßig entleeren

**Stadium 2 — Aktive Kontamination:**
- Zeitraum: Monate 6–18
- Keimzahl: 10⁴–10⁶ KBE/ml
- Optisch: Kraftstoff dunkel, leicht trüb, Schleimfäden im Filterglas
- Filter: Standzeit auf 50–70 % reduziert
- Motor: Gelegentliches Stottern unter Last
- Diagnose: Visuelle Inspektion des Wasserabscheiders, FUELSTAT-Test positiv
- Maßnahme: Biozid-Stoßbehandlung + Fuel Polishing

**Stadium 3 — Massive Kontamination:**
- Zeitraum: Ab Monat 12–24 (unbehandelt)
- Keimzahl: >10⁶ KBE/ml
- Optisch: Schwarzer Schleim im Filter, geleeartiges Material
- Filter: Standzeit auf <20 % reduziert, häufiges Verstopfen
- Motor: Wiederholtes Abstellen, Leistungsverlust >25 %
- Tank: Biofilm auf Tankwänden, Korrosion unter Biofilm (bei Metall)
- Rücklauf: Kontaminierter Kraftstoff zirkuliert im Gesamtsystem
- Maßnahme: Komplette Systemreinigung — Tank entleeren, mechanisch reinigen, alle Leitungen spülen, alle Filter wechseln, Biozid-Behandlung, Fuel Polishing

#### 2.3.4 Schnelltests für mikrobielle Kontamination

**Verfügbare Testverfahren (Confidence: measured):**

| Test | Hersteller | Prinzip | Nachweisgrenze | Zeit | Kosten |
|------|-----------|---------|----------------|------|--------|
| FUELSTAT Plus | Conidia Bioscience | Immunoassay (Antikörper) | H. resinae, Cladosporium, Bakterien | 15 min | 25–35 EUR/Test |
| FUELSTAT Maritime | Conidia Bioscience | Wie Plus, salzwasserresistent | Wie Plus | 15 min | 30–40 EUR/Test |
| Liqui-Cult TTC | Hach/OENORM | Dipslide, TTC-Reduktion | 10²–10⁶ KBE/ml | 24–72 h | 8–12 EUR/Test |
| HMT DELHIST-100 | HMT | Sondenfluoreszenz | Biofilm auf Oberflächen | Sofort | Gerät 1.200 EUR |
| Easicult Combi | Orion Diagnostica | Doppel-Dipslide | Bakterien + Pilze | 24–72 h | 5–8 EUR/Test |
| MicrobMonitor2 | MIC Solutions | Drei-Phasen-Test | Aerob + Anaerob + SRB | 72 h | 15–25 EUR/Test |

**FUELSTAT-Interpretation (häufigstes Testkit im Yachtbereich):**

| Ergebnis | Kontamination | Maßnahme |
|----------|---------------|----------|
| Negativ (kein Streifen) | <10⁴ KBE/ml — vernachlässigbar | Routinewartung beibehalten |
| Moderat (schwacher Streifen) | 10⁴–10⁵ KBE/ml | Biozid-Behandlung empfohlen |
| Schwer (deutlicher Streifen) | 10⁵–10⁶ KBE/ml | Biozid + Fuel Polishing |
| Sehr schwer (starker Streifen) | >10⁶ KBE/ml | Komplette Systemreinigung |

### 2.4 Wassergehalt — Messung und Kontrolle

#### 2.4.1 Wasserquellen im Tank

1. **Kondensation** (Hauptquelle): Warme, feuchte Luft dringt durch Tankbelüftung ein und kondensiert an kühlen Tankwänden. Pro Saison können 2–5 Liter Kondenswasser entstehen (200-L-Tank, Nordeuropa).

2. **Tankstellenwasser**: Besonders in kleineren Häfen, Mittelmeer-Marinas. Kondensat in Vorratstanks der Tankstelle.

3. **Undichter Einfüllstutzen**: Deck-Fitting korrodiert oder Dichtung defekt. Spritzwasser, Regenwasser bei Liegeplatz.

4. **Biodiesel-Hygroskopie**: FAME bindet Wasser aus Luft.

5. **Tankbelüftungsleitung**: Fehlende Schwanenhals-Führung, Belüftungsöffnung in Spritzwasserzone.

#### 2.4.2 Messmethoden

**1. Karl-Fischer-Titration (Laborstandard):**
- Genauigkeit: ±5 ppm
- Bereich: 1–10.000 ppm
- Kosten: 30–60 EUR pro Analyse
- Turnaround: 1–3 Werktage
- Bewertung: Goldstandard, aber nicht vor Ort möglich

**2. Calcium-Hydrid-Test (Vor-Ort):**
- Genauigkeit: ±50 ppm
- Bereich: 100–5.000 ppm
- Kosten: 5–10 EUR pro Test
- Turnaround: 10 Minuten
- Bewertung: Gut für Routinekontrolle

**3. Wassererkennungspaste (Quick-Check):**
- Genauigkeit: Qualitatitv (Ja/Nein für freies Wasser)
- Produkt: Kolor Kut Paste, Gastec Water Finding Paste
- Kosten: 15–25 EUR/Tube (reicht für ~50 Tests)
- Anwendung: Paste auf Peilstab, eintauchen, Farbumschlag bei Wasser
- Bewertung: Einfachstes Mittel für freies Wasser am Tankboden

**4. Elektronischer Wassersensor (Inline):**
- Genauigkeit: ±25 ppm (kapazitiv) bis ±5 ppm (optisch)
- Produkte: Argo-Hytos LubCos H₂O, Parker FLSS
- Kosten: 800–3.500 EUR
- Bewertung: Permanente Überwachung, Alarm bei Grenzwert

#### 2.4.3 Grenzwerte Wassergehalt

| Zustand | ppm | mg/kg | % | Bewertung |
|---------|-----|-------|---|-----------|
| Trocken | <100 | <100 | <0,01 | Optimal |
| Normal | 100–200 | 100–200 | 0,01–0,02 | EN 590 konform, kein Handlungsbedarf |
| Erhöht | 200–500 | 200–500 | 0,02–0,05 | Ursache suchen, Wasserabscheider prüfen |
| Kritisch | 500–1.000 | 500–1.000 | 0,05–0,10 | Sofort Wasser entfernen, Dieselpest-Risiko! |
| Gefährlich | >1.000 | >1.000 | >0,10 | Motor NICHT starten, Tank entleeren |

### 2.5 Tankinspektion — Methoden und Intervalle

#### 2.5.1 Externe Inspektion

**Prüfpunkte (Confidence: documented):**

| Prüfpunkt | Methode | Intervall | Befund → Maßnahme |
|-----------|---------|-----------|-------------------|
| Tankbefestigungen | Visuell, Schraubenprobe | Jährlich | Lose → nachziehen mit Drehmomentwert |
| Tankauflager/Polster | Visuell | Jährlich | Verhärtet/eingerissen → erneuern |
| Schweißnähte (Stahl/Alu) | Visuell, Farbeindringprüfung | Alle 5 Jahre / bei Verdacht | Riss → Fachbetrieb, nicht selbst schweißen |
| GFK-Laminat (GFK-Tank) | Visuell, Klopftest | Jährlich | Hohler Klang → Delamination prüfen |
| Anschlüsse / Fittings | Visuell, Dichtheitsprüfung | Jährlich | Feuchtigkeit → Dichtung erneuern |
| Tanklüftung | Visuell, Durchblastest | Jährlich | Verstopft → reinigen, auf Insekten prüfen |
| Einfüllstutzen-Dichtung | Visuell, Wassertest | Jährlich | Undicht → O-Ring/Dichtung erneuern |
| Absperrventile | Funktion prüfen (öffnen/schließen) | Halbjährlich | Schwergängig → Fett erneuern, ggf. tauschen |
| Kraftstoff-Peiltab/-Sensor | Vergleich mit Tankrechnung | Jährlich | Abweichung >10 % → Sensor kalibrieren |

#### 2.5.2 Interne Inspektion

**Zugang zum Tankinneren:**

Viele Yachttanks haben eine Inspektionsöffnung (Mannloch oder Handloch). Falls nicht vorhanden, ist die endoskopische Inspektion durch den Einfüllstutzen möglich.

**Endoskopische Inspektion (Confidence: documented):**

| Aspekt | Detail |
|--------|--------|
| Gerät | Endoskopkamera, ≥5 m flexibel, ≥IP67, LED-Beleuchtung |
| Kosten Gerät | 80–300 EUR (brauchbare USB-Endoskope) |
| Vorbereitung | Tank auf <25 % entleeren, Belüftung sicherstellen |
| Prüfpunkte | Tankboden (Sediment, Wasser), Wände (Korrosion, Biofilm), Schwall-wände (Ablagerungen), Ansaugstutzen (Höhe über Boden), Rücklauf (Position) |
| Dokumentation | Video aufzeichnen, GPS-Position notieren, Datum |
| Sicherheit | ATEX-Zone! Keine Funken, Belüftung, keine Zündquellen |

**Befundmatrix Tankinspektion:**

| Befund | Schweregrad | Maßnahme | Kosten (ca.) |
|--------|-------------|----------|--------------|
| Leichtes Sediment (<5 mm) | Gering | Fuel Polishing ausreichend | 200–400 EUR |
| Starkes Sediment (>5 mm) | Mittel | Tank entleeren, Fuel Polishing + Spülung | 500–1.200 EUR |
| Freies Wasser (Pfütze) | Mittel | Absaugen, Ursache beheben | 100–300 EUR |
| Brauner/schwarzer Biofilm auf Wänden | Hoch | Professionelle Tankreinigung | 800–2.500 EUR |
| Korrosionsnester (Alu-Tank) | Hoch | Fachbetrieb: Wandstärke messen, ggf. Tanktausch | 2.000–8.000 EUR |
| Durchrostung / Lochfraß | Kritisch | Sofort stilllegen, Tanktausch | 3.000–12.000 EUR |
| Delaminierung (GFK-Tank) | Hoch | Fachbetrieb: Laminatreparatur oder Tanktausch | 1.500–6.000 EUR |
| Ablagerungen an Schwallwänden | Mittel | Mechanische Reinigung bei nächster Tankreinigung | Im Rahmen der Tankreinigung |
| Ansaugstutzen zu tief (im Sediment) | Mittel | Ansaugrohr kürzen oder höher setzen | 200–500 EUR |

### 2.6 Filtersysteme — Theorie und Praxis

#### 2.6.1 Filtrationsstufen im marinen Dieselsystem

**Dreistufiges Filtrationskonzept (Best Practice):**

| Stufe | Bezeichnung | Filterfeinheit | Funktion | Position |
|-------|-------------|----------------|----------|----------|
| 1 | Vorfilter / Wasserabscheider | 30–60 µm + Koaleszenzelement | Wasser abtrennen, Grobschmutz | Zwischen Tank und Förderpumpe |
| 2 | Primärfilter | 10 µm | Feinpartikel, Asphaltene | Am Motor-Einlass, vor Einspritzpumpe |
| 3 | Sekundärfilter (bei Common-Rail) | 2–5 µm | Feinst-Filtration für Common-Rail | Zwischen Hochdruckpumpe und Rail |

**Filtrationseffizienz (Confidence: measured):**

| Filterfeinheit | Partikel >10 µm | Partikel >5 µm | Partikel >2 µm |
|----------------|------------------|-----------------|-----------------|
| 30 µm (Vorfilter) | 95 % | 50 % | 10 % |
| 10 µm (Primärfilter) | 99,9 % | 95 % | 60 % |
| 5 µm (Feinfilter) | 99,99 % | 99,5 % | 85 % |
| 2 µm (Common-Rail) | 99,99 % | 99,99 % | 98 % |

#### 2.6.2 Racor-Filtersysteme — Marktstandard

Racor (Parker Hannifin) ist der De-facto-Standard für marine Vorfilter/Wasserabscheider. Das Prinzip:

```
Kraftstoff rein (oben)
        │
        ▼
  ┌───────────────┐
  │  Zentrifugal-  │  ← Kraftstoff wird in Rotation versetzt
  │  Abscheider    │  ← Wasser (schwerer) wandert nach außen
  │               │
  │  ┌─────────┐  │
  │  │ Filter- │  │  ← Koaleszenz-Filterelement
  │  │ element │  │  ← Kleine Wassertröpfchen → große Tropfen
  │  └─────────┘  │
  │               │
  │  Wassersammel- │  ← Sichtglas mit Ablasshahn
  │  glas          │
  └───────────────┘
        │
        ▼
Kraftstoff raus (sauber, wasserfrei)
```

**Racor Turbine-Serie — Auswahlmatrix (Confidence: measured):**

| Modell | Durchfluss (l/h) | Motor-PS | Filterfeinheit | Sichtglas | Heizung optional |
|--------|-------------------|----------|----------------|-----------|-------------------|
| Racor 110A | 57 | Bis 30 PS | 10 µm | Nein (Bowl) | Nein |
| Racor 200 (R20) | 114 | Bis 60 PS | 2/10/30 µm | Ja | Nein |
| Racor 215R | 114 | Bis 60 PS | 2/10/30 µm | Ja | Ja (R58064) |
| Racor 320R | 114 | Bis 90 PS | 2/10/30 µm | Ja | Ja |
| Racor 500FG | 227 | Bis 150 PS | 2/10/30 µm | Ja | Ja |
| Racor 500MA | 227 | Bis 150 PS | 2/10/30 µm | Ja (Metall) | Ja |
| Racor 900MA | 341 | Bis 300 PS | 2/10/30 µm | Ja (Metall) | Ja |
| Racor 1000FG | 681 | Bis 600 PS | 2/10/30 µm | Ja | Ja |
| Racor 75/B32 (Duplex) | 681 | Bis 600 PS | 2/10/30 µm | Ja | Ja |

**Racor-Filterelement Farbcodierung:**

| Filterfeinheit | Farbe Endkappe | Racor-Typ | Einsatz |
|----------------|----------------|-----------|---------|
| 2 µm | Braun | 2020xx-OR | Common-Rail-Motoren, Feinst-Filtration |
| 10 µm | Blau | 2010xx-OR | Standard — empfohlen für die meisten Yachten |
| 30 µm | Rot | 2000xx-OR | Grobfiltration, bei bekannten Verunreinigungen als erste Stufe |

---

## 3. Typenübersicht — Wartungsintervalle und Maßnahmen

### 3.1 Wartungsintervallplan — Gesamtsystem

#### 3.1.1 Zeitbasierte Intervalle

**Monatliche Wartung (während der Saison) — Zeitbedarf: 15–30 min:**

| Nr. | Maßnahme | Werkzeug | Befund → Maßnahme |
|-----|----------|----------|-------------------|
| M-01 | Wasserabscheider Sichtglas prüfen | Auge | Wasser sichtbar → ablassen |
| M-02 | Wasserabscheider ablassen (unabhängig von Befund) | Ablasshahn | — |
| M-03 | Kraftstoff-Absperrventile auf Gängigkeit prüfen | Hand | Schwergängig → fetten |
| M-04 | Kraftstoff-Peiltab prüfen, Tankfüllstand notieren | Peiltab/Anzeige | Verbrauch plausibel? |
| M-05 | Sichtprüfung aller Leitungen auf Feuchtigkeit | Auge, Küchenpapier | Feuchtigkeit → Leck suchen |
| M-06 | Bilge unter Motor auf Dieselgeruch prüfen | Nase | Geruch → Lecksuche |
| M-07 | Kraftstoffprobe aus Wasserabscheider optisch beurteilen | Klares Glas | Trüb/dunkel → weiter untersuchen |

**Halbjährliche Wartung — Zeitbedarf: 1–2 Stunden:**

| Nr. | Maßnahme | Werkzeug | Befund → Maßnahme |
|-----|----------|----------|-------------------|
| H-01 | Alle M-Maßnahmen durchführen | — | — |
| H-02 | Vorfilter-Element wechseln (wenn Druckdifferenz-Anzeige im gelben Bereich) | Bandschlüssel, Ölauffang | — |
| H-03 | Kraftstoff-Förderpumpe Funktion prüfen (Handpumpe/Elektro) | — | Kein Druck → Membran prüfen |
| H-04 | Alle Schlauchschellen nachziehen | Schraubendreher / 7mm Nuss | — |
| H-05 | Tankbelüftung auf Durchgängigkeit prüfen | Durchblastest, Druckluft | Verstopft → reinigen |
| H-06 | FUELSTAT-Schnelltest durchführen | FUELSTAT-Kit | Positiv → Biozid + Maßnahmenplan |
| H-07 | Einfüllstutzen-Dichtung prüfen | Visuell | Defekt → O-Ring erneuern |

**Jährliche Wartung — Zeitbedarf: 3–6 Stunden:**

| Nr. | Maßnahme | Werkzeug | Befund → Maßnahme |
|-----|----------|----------|-------------------|
| J-01 | Alle M- und H-Maßnahmen durchführen | — | — |
| J-02 | Vorfilter-Element wechseln (unabhängig von Zustand) | Bandschlüssel, Ölauffang | — |
| J-03 | Motor-Primärfilter wechseln | Motorenspezifisch | — |
| J-04 | Motor-Sekundärfilter wechseln (falls vorhanden) | Motorenspezifisch | — |
| J-05 | Kraftstoffprobe zur Laboranalyse | Probenflasche, sauber | Basis-Analyse |
| J-06 | Tankinspektion (endoskopisch bei Verdacht) | Endoskop | Befund dokumentieren |
| J-07 | Kraftstoffleitungen auf Risse, Verhärtung, Quellung prüfen | Visuell, Biegen | Hart/rissig → erneuern |
| J-08 | Absperrventile komplett öffnen/schließen, Gängigkeit | Hand | Schwergängig → Wartung/Tausch |
| J-09 | Dichtheit aller Verbindungen mit Kriechmittel oder Drucktest prüfen | Lecksuchmittel / 0,5 bar | Undicht → nachziehen oder Dichtung erneuern |
| J-10 | Kraftstoff-Stabilisator zugeben (wenn Saison >6 Monate) | Dosierbecher | — |

#### 3.1.2 Betriebsstundenbasierte Intervalle

**Intervalle nach Motorhersteller-Empfehlungen (Confidence: documented):**

| Intervall | Maßnahme | Volvo Penta | Yanmar | Nanni | Vetus |
|-----------|----------|-------------|--------|-------|-------|
| 50 h | Wasserabscheider entleeren | ✓ | ✓ | ✓ | ✓ |
| 100 h | Vorfilter-Element wechseln | — | ✓ | — | ✓ |
| 200 h | Vorfilter-Element wechseln | ✓ | — | ✓ | — |
| 200 h | Primärfilter wechseln | — | ✓ | — | — |
| 250 h | Primärfilter wechseln | ✓ | — | ✓ | ✓ |
| 500 h | Sekundärfilter wechseln (CR) | ✓ | ✓ | ✓ | — |
| 500 h | Einspritzdüsen prüfen (konv.) | ✓ | ✓ | ✓ | ✓ |
| 500 h | Förderpumpe prüfen | ✓ | ✓ | ✓ | ✓ |
| 1.000 h | Einspritzdüsen prüfen/tauschen (CR) | ✓ | ✓ | ✓ | — |
| 1.000 h | Kraftstoffleitungen erneuern | — | ✓ | — | ✓ |
| 2.000 h | Kraftstoffleitungen erneuern | ✓ | — | ✓ | — |
| 2.000 h | Einspritzpumpe überholen (konv.) | ✓ | ✓ | ✓ | ✓ |
| 5.000 h | Common-Rail-Hochdruckpumpe prüfen | ✓ | ✓ | ✓ | — |

**Hinweis:** Bei Charterbooten und kommerzieller Nutzung gelten die halben Intervalle (Confidence: benchmark — Charterfirmen-Daten).

### 3.2 Dieselpest-Behandlung — Stufenplan

#### 3.2.1 Übersicht Behandlungsmethoden

| Methode | Wirkung | Stadium 1 | Stadium 2 | Stadium 3 | Kosten |
|---------|---------|-----------|-----------|-----------|--------|
| Biozid prophylaktisch | Verhindert Wachstum | ✓ ideal | Begleitend | Begleitend | 15–40 EUR/Behandlung |
| Biozid Stoßbehandlung | Tötet Organismen ab | ✓ | ✓ (+ Polishing) | Allein nicht ausreichend | 30–80 EUR/Behandlung |
| Fuel Polishing (eigenes System) | Entfernt Partikel + Wasser | ✓ Bonus | ✓ empfohlen | ✓ essentiell | System 800–4.000 EUR |
| Fuel Polishing (mobiler Service) | Wie oben, professionell | ✓ | ✓ | ✓ | 250–600 EUR/Einsatz |
| Manuelle Tankreinigung | Mechanische Entfernung | — | Bei Bedarf | ✓ zwingend | 800–2.500 EUR |
| Professionelle Tanksanierung | Komplett: Reinigung + Beschichtung | — | — | Bei Tankschäden | 2.000–8.000 EUR |

#### 3.2.2 Biozid-Anwendungsprotokoll

**Phase 1 — Stoßbehandlung (Schockdosierung):**

1. Tank auf mindestens 75 % Füllstand bringen (frischer Diesel)
2. Biozid in doppelter Normaldosis zugeben (Herstellerangabe beachten)
3. Motor 30 Minuten unter Last laufen lassen (Durchmischung durch Rücklauf)
4. 24 Stunden einwirken lassen
5. Wasserabscheider entleeren (tote Biomasse sinkt ab)
6. Nach 48 Stunden: Vorfilter wechseln (hohe Schmutzfracht durch abgetötete Organismen!)
7. FUELSTAT-Kontrolltest nach 7 Tagen

**Phase 2 — Folgetherapie (2.–4. Woche):**

1. Wöchentlich Wasserabscheider entleeren
2. Biozid in Normaldosis bei nächster Betankung zugeben
3. Vorfilter wechseln, wenn Druckdifferenz im gelben Bereich
4. FUELSTAT-Kontrolltest nach 4 Wochen

**Phase 3 — Prophylaxe (dauerhaft):**

1. Biozid bei jeder 2.–3. Betankung in Normaldosis zugeben
2. Wasserabscheider monatlich entleeren
3. FUELSTAT-Test halbjährlich
4. Tank nie unter 50 % Füllstand über längere Standzeiten

#### 3.2.3 Biozid-Vergleich — Wirkstoffe und Dosierung

**Verfügbare Biozid-Wirkstoffe (Confidence: measured — Hersteller-TDS):**

| Wirkstoff | Handelsname | Typ | Wirkung | Korrosivität | Zulassung |
|-----------|-------------|-----|---------|--------------|-----------|
| Methylen-bis-thiocyanat (MBT) | Grotamar 82 | Kontaktbiozid | Breitband gegen Pilze, Hefen, Bakterien | Gering (Alu-verträglich) | BPR EU zugelassen |
| 2-Brom-2-nitro-1,3-propandiol (Bronopol) | Diverse | Biozid | Breitband, besonders gegen Bakterien | Mittel | BPR EU zugelassen |
| Isothiazolinon-Gemisch | Marine 16 | Biozid + Stabilisator | Breitband + Oxidationsschutz | Gering | UK-Zulassung, EU-Status prüfen |
| Morpholin-Derivat | Dieselguard | Biozid + Korrosionsschutz | Breitband + Schutzfilm | Sehr gering | BPR EU zugelassen |
| Dodecanolguanidin | BioGuard | Biozid | Besonders gegen Pilze | Gering | D/AT/CH zugelassen |
| Phenolethylalkohol + MBT | FPPF Killem | Kombination | Schnellwirkend + Langzeit | Mittel | US-Zulassung, in EU eingeschränkt |

### 3.3 Tankpolieren (Fuel Polishing)

#### 3.3.1 Funktionsprinzip

Fuel Polishing ist die Rezirkulation des Tankinhalt durch ein Mehrstufen-Filtersystem, um Wasser, Partikel und mikrobielle Biomasse zu entfernen, ohne den Tank öffnen oder entleeren zu müssen.

```
Tank (Entnahme über dedizierte Leitung, möglichst nah am Boden)
    │
    ▼
Grobfilter (50 µm) — Schutz der Pumpe
    │
    ▼
Umwälzpumpe (10–60 l/h, selbstansaugend)
    │
    ▼
Koaleszenzelement — Wasser abtrennen
    │
    ▼
Feinfiltration (2–5 µm)
    │                    │
    ▼                    ▼
Wassersammler        Tank (Rücklauf, gegenüber Entnahme)
(manuell entleeren)
```

**Tankvolumen und Polishing-Dauer (Confidence: estimated):**

| Tankvolumen | Pumpenleistung | Zyklen empfohlen | Dauer |
|-------------|----------------|-------------------|-------|
| 50 L | 30 l/h | 3× vollständig | ~5 h |
| 100 L | 30 l/h | 3× vollständig | ~10 h |
| 200 L | 60 l/h | 3× vollständig | ~10 h |
| 400 L | 60 l/h | 3× vollständig | ~20 h |
| 800 L | 120 l/h | 3× vollständig | ~20 h |
| 2.000 L | 300 l/h | 3× vollständig | ~20 h |

**Empfehlung:** Mindestens 3 komplette Zyklen durch den Tank. Bei schwerer Kontamination 5–8 Zyklen. Filterelement nach jedem Zyklus prüfen und bei Bedarf wechseln.

#### 3.3.2 Fest installierte vs. mobile Systeme

**Fest installiert (Confidence: documented):**

| Aspekt | Vorteil | Nachteil |
|--------|---------|----------|
| Verfügbarkeit | Jederzeit einsatzbereit | — |
| Automatisierung | Timer-gesteuert, unbeaufsichtigt | Überwachung empfohlen |
| Kosten | Langfristig günstiger | Anschaffung 1.500–6.000 EUR |
| Platzbedarf | — | Fest verbaut, braucht Platz |
| Wartung | — | Eigene Filterelement-Kosten |
| Empfehlung | Ab 300 L Tank / Saisonboot / Blauwassersegler | — |

**Mobil (Service oder Eigengerät):**

| Aspekt | Vorteil | Nachteil |
|--------|---------|----------|
| Flexibilität | Für mehrere Boote nutzbar | Muss transportiert werden |
| Kosten | Einzeleinsatz günstiger | 250–600 EUR pro Einsatz |
| Professionalität | Service mit Laboranalyse | Terminabhängig |
| Empfehlung | <300 L Tank / Gelegenheitssegler / Winterlager | — |

### 3.4 Winterfestmachung — Kraftstoffsystem

#### 3.4.1 Standard-Winterfestmachung (6 Monate Stillstand)

**Checkliste Winterfestmachung Kraftstoffsystem (Confidence: documented):**

| Schritt | Maßnahme | Begründung |
|---------|----------|------------|
| W-01 | Tank VOLL füllen (>95 %) | Minimiert Kondensationsfläche |
| W-02 | Kraftstoff-Stabilisator zugeben | Verhindert Oxidation über Winter |
| W-03 | Biozid in Normaldosis zugeben | Verhindert Wachstum bei Stillstand |
| W-04 | Motor 20 min unter Last laufen | Verteilt Additiv im Gesamtsystem |
| W-05 | Wasserabscheider entleeren und prüfen | Kein Wasser über Winter stehen lassen |
| W-06 | Vorfilter-Element wechseln | Frischer Filter für Saisonstart |
| W-07 | Primärfilter wechseln | Frischer Filter für Saisonstart |
| W-08 | Alle Ablasshähne auf Dichtheit prüfen | Kein Tropfen über Winter |
| W-09 | Tankbelüftung auf Durchgängigkeit prüfen | Muss frei sein (Kondensatablauf!) |
| W-10 | Einfüllstutzen-Deckel dicht verschließen | Kein Regenwasser eindringen lassen |
| W-11 | Kraftstoff-Absperrventil schließen | Sicherheit bei Stillstand |
| W-12 | Bilge unter Motor trockenlegen | Keine Diesel-Restfeuchtigkeit |

**Empfohlene Additive für Winterfestmachung:**

| Produkt | Typ | Dosierung (pro 100 L) | Kosten |
|---------|-----|----------------------|--------|
| Grotamar 82 | Biozid | 10 ml (Normaldosis) | ~3 EUR |
| Fuel Set Diesel Kleen | Stabilisator + Reiniger | 100 ml | ~8 EUR |
| Marine 16 | Biozid + Stabilisator (Kombi) | 100 ml | ~12 EUR |
| LIQUI MOLY Marine Diesel Schutz | Stabilisator + Korrosionsschutz | 250 ml | ~15 EUR |
| Startron Enzyme Fuel Treatment | Stabilisator + Enzym | 30 ml | ~5 EUR |

#### 3.4.2 Erweiterte Winterfestmachung (12+ Monate Stillstand)

**Zusätzlich zu Standard-Winterfestmachung:**

| Schritt | Maßnahme | Begründung |
|---------|----------|------------|
| WE-01 | Fuel Polishing vor Einlagerung | Sauberer Kraftstoff altert langsamer |
| WE-02 | Doppelte Biozid-Dosis | Längere Schutzwirkung |
| WE-03 | Kraftstoff-Stabilisator in doppelter Dosis | Erhöhter Oxidationsschutz |
| WE-04 | Nach 6 Monaten: erneut Stabilisator nachfüllen | Wirkdauer der meisten Stabilisatoren: 6–12 Monate |
| WE-05 | Alle 3 Monate: Wasserabscheider kontrollieren | Kondenswasser entfernen |
| WE-06 | Kraftstoff-Schläuche mit Diesel-verträglichem Öl einsprühen | Verhindert Austrocknung/Rissbildung |
| WE-07 | Einspritzdüsen mit Konservierungsöl beschicken | Herstelleranleitung beachten |
| WE-08 | Vor Wiederinbetriebnahme: Kraftstoff-Laboranalyse | Prüfen ob Diesel noch nutzbar |

#### 3.4.3 Kälteschutz — Paraffin-Ausflockung verhindern

**CFPP-Werte und Schutzmaßnahmen (Confidence: measured):**

| Kraftstoff | CFPP Sommer | CFPP Winter (Dt.) | CFPP Arktik | Additiv nötig bei |
|-----------|-------------|--------------------|--------------|--------------------|
| Standard-Diesel Sommer | 0 bis -5 °C | — | — | <-5 °C |
| Standard-Diesel Winter | — | -20 bis -22 °C | — | <-22 °C |
| Arktik-Diesel | — | — | -32 bis -44 °C | <-44 °C |
| B7 Sommer | +2 bis -3 °C | — | — | <-3 °C |
| HVO | -25 bis -40 °C | -25 bis -40 °C | — | <-40 °C |

**Fließverbesserer-Additive (Cold Flow Improver):**

| Produkt | Wirkung | Dosierung | CFPP-Absenkung |
|---------|---------|-----------|----------------|
| LIQUI MOLY Diesel Fließ-Fit K | Modifiziert Paraffin-Kristallstruktur | 150 ml / 50 L | Bis -31 °C |
| Coltri Sub-Zero | Dispergiert Paraffinkristalle | 100 ml / 100 L | Bis -26 °C |
| Power Service Diesel Fuel Supplement | Antiwachs + Enteiser | 80 ml / 60 L | Bis -40 °F (-40 °C) |
| Wynn's Ice Proof for Diesel | CFPP-Absenkung | 250 ml / 250 L | Bis -27 °C |

**WICHTIG:** Fließverbesserer MÜSSEN VOR dem Abkühlen des Diesels zugegeben werden! Einmal ausgeflockte Paraffine lassen sich durch Additive nicht wieder auflösen. Bei bereits ausgefallenen Paraffinen: Diesel auf >10 °C erwärmen, dann Additiv zugeben.

### 3.5 Langzeit-Einlagerung (>24 Monate)

#### 3.5.1 Optionen bei Langzeiteinlagerung

**Option A — Tank komplett entleeren (empfohlen bei >24 Monaten):**

| Vorteil | Nachteil |
|---------|----------|
| Keine Kraftstoff-Alterung | Tankwände ungeschützt (Korrosion bei Metall) |
| Keine Dieselpest-Gefahr | Erneute Betankung nötig |
| Keine Geruchsentwicklung | Restmengen schwer entfernbar |
| — | Konservierung der Einspritzkomponenten nötig |

Maßnahmen bei Entleerung:
- Tank restlos entleeren (auch Ansaug-Totraum!)
- Tankinnenwände mit korrosionshemmendem Spray einsprühen (bei Metall-Tanks)
- Einfüllstutzen und Tankbelüftung verschließen (Feuchtigkeitsschutz)
- Einspritzsystem: Konservierungsöl nach Herstelleranleitung
- Alle Leitungen entleeren oder mit Konservierungsdiesel füllen

**Option B — Tank voll halten und konservieren (Standard bei 12–24 Monaten):**

| Vorteil | Nachteil |
|---------|----------|
| Tankwände durch Diesel geschützt | Diesel altert (Additive erforderlich) |
| Sofortige Wiederinbetriebnahme möglich | Dieselpest-Risiko bei Vernachlässigung |
| Einfacher | Kosten für Additive |

Maßnahmen:
- Tank >95 % füllen
- Stabilisator + Biozid in doppelter Dosis
- Alle 6 Monate Stabilisator nachfüllen
- Alle 3 Monate Wasserabscheider entleeren
- Vor Wiederinbetriebnahme: Laboranalyse + Fuel Polishing

---

## 4. Produktlinien und Spezifikationen

### 4.1 Grotamar 82 — Referenz-Biozid

**Hersteller:** Schülke & Mayr GmbH, Norderstedt, Deutschland

**Technische Daten (Confidence: measured — Hersteller-TDS):**

| Parameter | Wert |
|-----------|------|
| Wirkstoff | Methylen-bis(thiocyanat) (MBT), CAS 6317-18-6 |
| Konzentration | ≥ 97 % aktiv |
| Erscheinung | Grau-weißes Pulver, gelöst in Methanol/Diesel |
| Wirkspektrum | Pilze, Hefen, Bakterien (inkl. SRB) |
| Wirkmechanismus | Blockiert Thiol-Gruppen in Enzymen der Mikroorganismen |
| Wirkungseintritt | 2–6 Stunden |
| Dosierung prophylaktisch | 100 ppm (10 ml / 100 L Diesel) |
| Dosierung Stoßbehandlung | 200–250 ppm (20–25 ml / 100 L Diesel) |
| Max. Dosierung | 500 ppm (bei extremer Kontamination, einmalig) |
| Materialverträglichkeit | Alu, Stahl, GFK, PE, Viton, NBR — alle verträglich |
| Kupfer-Verträglichkeit | Ja (anders als viele Biozide) |
| Lagerfähigkeit | 24 Monate (ungeöffnet) |
| Gebindegrößen | 100 ml, 500 ml, 1 L, 5 L |
| Preis (ca.) | 100 ml: 18–25 EUR, 500 ml: 55–70 EUR |
| Zulassung | BPR EU TP 06, Reg.-Nr. DE-xxxx |
| UN-Nummer | UN 3082 (umweltgefährdend flüssig) |

**Anwendungshinweise Grotamar 82:**

1. Immer beim Tanken zugeben (vor dem Dieseleinlauf → Durchmischung durch Einfüllstrahl)
2. Niemals in leeren Tank geben und dann betanken (ungleichmäßige Verteilung)
3. Bei Stoßbehandlung: Motor 30 min laufen lassen zur Verteilung
4. Nach Stoßbehandlung: 48 h warten, dann Vorfilter wechseln
5. Nicht mischen mit anderen Bioziden (Wechselwirkungen möglich)
6. Handschuhe tragen (Hautkontakt vermeiden, MBT ist Sensibilisator)

### 4.2 Fuel Set Diesel Kleen — Multifunktionsadditiv

**Hersteller:** Fuel Set GmbH, Hamburg, Deutschland

**Technische Daten (Confidence: measured — Hersteller-TDS):**

| Parameter | Wert |
|-----------|------|
| Typ | Multifunktions-Diesel-Additiv (kein Biozid!) |
| Wirkung | Reinigung, Stabilisierung, Cetanboost, Korrosionsschutz |
| Cetanzahl-Erhöhung | +3 bis +5 Punkte |
| Schmierfähigkeits-Verbesserung | HFRR-Reduktion um 30–50 µm |
| Injektorreinigung | Hält Düsen und Einspritzpumpe sauber |
| Oxidationsstabilität | Verlängert um Faktor 2–3 |
| Wasseremulgierung | Nein — deshalb mit Wasserabscheider kompatibel |
| Dosierung | 100 ml / 100 L (1:1.000) |
| Materialverträglichkeit | Alle gängigen Materialien |
| Gebindegrößen | 250 ml, 500 ml, 1 L |
| Preis (ca.) | 250 ml: 12–16 EUR |

**Hinweis:** Diesel Kleen ist kein Biozid-Ersatz! Ergänzende Anwendung zu Grotamar 82 empfohlen.

### 4.3 Marine 16 — Kombinationsprodukt

**Hersteller:** Marine 16 International Ltd., Poole, UK

**Technische Daten (Confidence: measured — Hersteller-TDS):**

| Parameter | Wert |
|-----------|------|
| Typ | Diesel-Treibstoffbehandlung (Biozid + Stabilisator + Korrosionsschutz) |
| Wirkstoff (biozid) | Isothiazolinon-Gemisch (CMIT/MIT-basiert) |
| Biozidwirkung | Pilze, Hefen, Bakterien |
| Stabilisierung | Oxidationsschutz, Alterungshemmer |
| Korrosionsschutz | Passivierungsschicht auf Metalloberflächen |
| Emulgierung | Bindet geringe Wassermengen in Kraftstoff |
| Dosierung Prophylaxe | 100 ml / 100 L |
| Dosierung Behandlung | 200 ml / 100 L |
| Materialverträglichkeit | Alle gängigen Materialien, Aluminium geprüft |
| Gebindegrößen | 100 ml, 500 ml, 1 L |
| Preis (ca.) | 500 ml: 25–35 EUR |
| Haltbarkeit | 36 Monate |
| Besonderheit | Einziges Produkt mit Kombi-Wirkung (Biozid + Stabilisator) |

**Vorteil Marine 16:** Nur ein Produkt statt zwei (Biozid + Stabilisator). Einfachere Handhabung.
**Nachteil Marine 16:** Geringere Biozid-Wirksamkeit als reines Grotamar 82 bei schwerer Kontamination. Nicht für Stoßbehandlung bei Stadium 3 empfohlen.

### 4.4 Dieselguard — Biozid mit Korrosionsschutz

**Hersteller:** Hammonds Fuel Additives Ltd., Ilkeston, UK / Vertrieb DACH: diverse

**Technische Daten (Confidence: measured):**

| Parameter | Wert |
|-----------|------|
| Wirkstoff | Morpholin-Derivat |
| Typ | Biozid + Korrosionsinhibitor |
| Wirkspektrum | Pilze, Bakterien, Hefen |
| Dosierung Prophylaxe | 100 ml / 200 L |
| Dosierung Behandlung | 100 ml / 100 L |
| Korrosionsschutz | Schutzfilm auf Metalloberflächen |
| Besonderheit | Sehr materialschonend, besonders Aluminium-freundlich |
| Gebindegrößen | 100 ml, 350 ml, 1 L |
| Preis (ca.) | 350 ml: 20–30 EUR |

### 4.5 Racor FilterView — Diagnosesystem

**Hersteller:** Parker Hannifin / Racor Division, Modesto, CA, USA

**Technische Daten (Confidence: measured — Hersteller-TDS):**

| Parameter | Wert |
|-----------|------|
| Typ | Optischer Kraftstoff-Zustandsindikator |
| Funktion | Inline-Sichtfenster mit integrierter Farbskala |
| Messwerte | Trübung, Wassergehalt (visuell), Farbe (Alterung) |
| Anschluss | Inline in Kraftstoffleitung, diverse Anschlussgrößen |
| Druckbereich | 0–3,4 bar (Niederdruckseite) |
| Materialien | Polycarbonat-Sichtglas, Aluminium-Gehäuse, Viton-Dichtungen |
| Installation | Zwischen Tank und Vorfilter (Niederdruckseite) |
| Wartung | Sichtglas reinigen alle 6 Monate |
| Preis (ca.) | 45–80 EUR |

### 4.6 Fuel Polishing Systeme — Marktübersicht

#### 4.6.1 KTI Fuel Polishing Systems

**Hersteller:** KTI Systems Inc., Costa Mesa, CA, USA

**Produktreihe (Confidence: measured — Hersteller-TDS):**

| Modell | Durchfluss | Tankgröße | Filterstufen | Betriebsart | Preis (ca.) |
|--------|-----------|-----------|--------------|-------------|-------------|
| KTI FPS-1 | 30 l/h | Bis 200 L | 2-stufig (30 + 5 µm) + Koaleszenzer | Manuell | 1.200 EUR |
| KTI FPS-2 | 60 l/h | Bis 500 L | 3-stufig (30 + 10 + 2 µm) + Koaleszenzer | Timer | 2.200 EUR |
| KTI FPS-3 | 120 l/h | Bis 2.000 L | 3-stufig + Koaleszenzer | Timer + Sensor | 3.800 EUR |
| KTI FPS-5 | 300 l/h | Bis 5.000 L | 4-stufig + Koaleszenzer + Magnetfilter | Vollautomatisch | 6.500 EUR |

#### 4.6.2 Algae-X Fuel Conditioning Systems

**Hersteller:** Algae-X International, Fort Lauderdale, FL, USA

**Technologie:** Kombination aus Magnetfeld-Behandlung (Fuel Conditioning Unit, FCU) und mechanischer Filtration. Die FCU verwendet starke Permanentmagneten, die Paraffinkristalle und Asphaltene desagglomerieren sollen.

| Modell | Durchfluss | Tankgröße | Filtration | FCU | Preis (ca.) |
|--------|-----------|-----------|------------|-----|-------------|
| Algae-X LGX100 | 45 l/h | Bis 250 L | 10 µm + Koaleszenzer | Ja | 1.600 EUR |
| Algae-X LGX200 | 90 l/h | Bis 750 L | 10 µm + Koaleszenzer | Ja | 2.400 EUR |
| Algae-X LGX400 | 180 l/h | Bis 2.000 L | 10 µm + Koaleszenzer | Ja | 3.600 EUR |
| Algae-X LGX800 | 360 l/h | Bis 5.000 L | 10 µm + Koaleszenzer | Ja | 5.500 EUR |

**Hinweis (Confidence: estimated):** Die magnetische Kraftstoff-Konditionierung (FCU) ist in der Fachwelt umstritten. Die Filtrations- und Koaleszenz-Funktion ist nachweislich wirksam, die Magnetfeld-Wirkung auf Diesel ist wissenschaftlich nicht eindeutig belegt.

#### 4.6.3 ESI (Energy Sciences Inc.) Total Fuel Management

**Hersteller:** ESI / Total Fuel Management, Thornton, CO, USA

| Modell | Durchfluss | Tankgröße | Filterstufen | Besonderheit | Preis (ca.) |
|--------|-----------|-----------|--------------|--------------|-------------|
| ESI TFM-100 | 45 l/h | Bis 200 L | 2-stufig + Koaleszenzer | Kompakt, 12V DC | 1.400 EUR |
| ESI TFM-250 | 90 l/h | Bis 500 L | 3-stufig + Koaleszenzer | Timer + Druckdiff. | 2.500 EUR |
| ESI TFM-500 | 180 l/h | Bis 1.500 L | 3-stufig + Koaleszenzer | Vollautomatisch | 4.200 EUR |

### 4.7 Additiv-Vergleichsmatrix — Entscheidungshilfe

**Produktvergleich nach Anwendungsszenario (Confidence: documented + estimated):**

| Szenario | Empfehlung 1 | Empfehlung 2 | Begründung |
|----------|-------------|-------------|------------|
| Prophylaxe Saisonsegler (Ostsee/Nordsee) | Grotamar 82 (jede 3. Tankfüllung) + Fuel Set Diesel Kleen | Marine 16 (jede Tankfüllung) | Geringes Risiko, Standard-Schutz |
| Prophylaxe Langfahrt Mittelmeer | Grotamar 82 (jede 2. Tankfüllung) + Fuel Set Diesel Kleen | Grotamar 82 + Marine 16 im Wechsel | Erhöhtes Risiko (Wärme, variable Qualität) |
| Prophylaxe Blauwasser/Tropen | Grotamar 82 (jede Tankfüllung, Normaldosis) | Grotamar 82 + festinstalliertes Fuel Polishing | Höchstes Risiko |
| Behandlung Stadium 1 | Grotamar 82 Stoßdosis (200 ppm) | Marine 16 Doppeldosis | Leichte Kontamination |
| Behandlung Stadium 2 | Grotamar 82 Stoßdosis + Fuel Polishing | — | Mittlere Kontamination |
| Behandlung Stadium 3 | Tankreinigung + Grotamar 82 Stoßdosis + Fuel Polishing | — | Schwere Kontamination |
| Winterfestmachung 6 Monate | Grotamar 82 + Fuel Set Diesel Kleen | Marine 16 allein | Kombi-Schutz |
| Langzeitlagerung 12+ Monate | Grotamar 82 (Doppeldosis) + Fuel Set Diesel Kleen (Doppeldosis) | Marine 16 (Doppeldosis) alle 6 Monate auffrischen | Maximaler Schutz |

---

## 5. Hersteller-Datenbank

### 5.1 Racor / Parker Hannifin — Filtration

| Feld | Information |
|------|------------|
| **Firma** | Parker Hannifin Corporation — Racor Division |
| **Hauptsitz** | Modesto, CA, USA |
| **DACH-Vertretung** | Parker Hannifin Manufacturing Germany GmbH & Co. KG, Bielefeld |
| **Vertrieb Marine DACH** | SVB (Bremen), Bukh Bremen, ASAP Supplies |
| **Website** | www.parker.com/racor |
| **Gründung** | 1969 (Racor), seit 1997 Parker Hannifin |
| **Kernprodukte** | Kraftstoff-Vorfilter, Wasserabscheider, Lüftungsfilter, Ölfilter |
| **Marine-Anteil** | Ca. 60 % des Umsatzes (marine + off-highway) |
| **Marktposition** | Weltmarktführer marine Kraftstoff-Filtration |
| **Normen** | ISO 4548, SAE J1985, US Coast Guard approved |
| **Besonderheit** | Einziger Hersteller mit durchgängiger Turbine-Technologie für alle Bootsgrößen |
| **Ersatzteil-Verfügbarkeit** | Weltweit, nahezu alle Yachthändler und Chandleries |
| **Typische Filterkosten** | Racor 2010: 12–18 EUR, Racor 2040: 25–35 EUR, Racor 2020: 45–60 EUR |

### 5.2 Schülke & Mayr — Biozide (Grotamar)

| Feld | Information |
|------|------------|
| **Firma** | Schülke & Mayr GmbH |
| **Hauptsitz** | Norderstedt bei Hamburg, Deutschland |
| **Website** | www.schuelke.com |
| **Gründung** | 1889 |
| **Kernprodukte** | Industriebiozide, Desinfektionsmittel, Konservierungsmittel |
| **Marine-Produkt** | Grotamar 82 (Flaggschiff-Biozid für Kraftstoffe) |
| **Marktposition** | Europäischer Marktführer für Kraftstoff-Biozide |
| **Zulassung** | BPR EU Biozidprodukteverordnung, TP 06 |
| **Besonderheit** | Einziges rein europäisches, BPR-zugelassenes Marine-Diesel-Biozid mit MBT |
| **Vertrieb Marine** | SVB, Toplicht, AWN, Compass24, Yachtausrüster allgemein |

### 5.3 Marine 16 International

| Feld | Information |
|------|------------|
| **Firma** | Marine 16 International Ltd. |
| **Hauptsitz** | Poole, Dorset, Großbritannien |
| **Website** | www.marine16.com |
| **Gründung** | 1992 |
| **Kernprodukte** | Marine-Kraftstoff-Additive (Diesel + Benzin) |
| **Marine-Anteil** | 100 % Marine-Fokus |
| **Marktposition** | Marktführer UK/Irland, stark in Nordeuropa |
| **Besonderheit** | Einziges Kombinationsprodukt (Biozid + Stabilisator + Korrosionsschutz) |
| **Vertrieb DACH** | SVB, Toplicht, AWN, diverse |

### 5.4 KTI Systems — Fuel Polishing

| Feld | Information |
|------|------------|
| **Firma** | KTI Systems Inc. |
| **Hauptsitz** | Costa Mesa, CA, USA |
| **Website** | www.ktisystems.com |
| **Gründung** | 1998 |
| **Kernprodukte** | Fuel Polishing Systeme, Tank-Management |
| **Marine-Anteil** | Ca. 70 % (Rest: Standby-Generatoren, Industrie) |
| **Marktposition** | Einer der führenden Anbieter für marine Fuel Polishing |
| **Besonderheit** | Modular ausbaubares System, eigene Filterelemente |
| **Vertrieb DACH** | Direktvertrieb, spezialisierte Yacht-Technikfirmen |

### 5.5 Algae-X International — Fuel Conditioning

| Feld | Information |
|------|------------|
| **Firma** | Algae-X International |
| **Hauptsitz** | Fort Lauderdale, FL, USA |
| **Website** | www.algae-x.net |
| **Gründung** | 2001 |
| **Kernprodukte** | Fuel Conditioning Units (FCU), Fuel Polishing, Tankreinigung |
| **Marine-Anteil** | Ca. 80 % |
| **Marktposition** | Marktführer USA für magnetische Fuel Conditioning |
| **Besonderheit** | Patentierte Magnetfeld-Technologie (FCU) |
| **Vertrieb DACH** | Direktvertrieb, Yacht-Technik-Fachbetriebe |

### 5.6 Conidia Bioscience — Dieselpest-Diagnostik

| Feld | Information |
|------|------------|
| **Firma** | Conidia Bioscience (Teil der Industrial Microbiological Services Ltd.) |
| **Hauptsitz** | Ceredigion, Wales, Großbritannien |
| **Website** | www.conidiabioscience.com |
| **Gründung** | 2004 |
| **Kernprodukte** | FUELSTAT-Schnelltestkits für mikrobielle Kontamination |
| **Marine-Anteil** | Ca. 40 % (Rest: Luftfahrt, Militär, Industrie) |
| **Marktposition** | Weltmarktführer für Immunoassay-basierte Kraftstoff-Schnelltests |
| **Besonderheit** | FUELSTAT ist der einzige ASTM D8070-konforme Antikörper-Schnelltest |
| **Zulassung** | ASTM D8070, IATA Guidance Material für Jet Fuel (auch für Diesel validiert) |
| **Vertrieb DACH** | SVB, Yachtausrüster, Laborbedarf |
| **Preis FUELSTAT Plus** | 25–35 EUR/Einzeltest, 120–150 EUR/5er-Pack |

### 5.7 Separ Filter (Stanadyne)

| Feld | Information |
|------|------------|
| **Firma** | Separ Filter (Marke von Stanadyne LLC) |
| **Hauptsitz** | Windsor, CT, USA (Separ: ursprünglich Stockelsdorf, Deutschland) |
| **Website** | www.separ-filter.de / www.stanadyne.com |
| **Gründung** | 1978 (Separ), 2019 Übernahme durch Stanadyne |
| **Kernprodukte** | Kraftstoff-Vorfilter, Wasserabscheider (Schwerkraft + Zentrifugal) |
| **Marine-Anteil** | Ca. 30 % |
| **Marktposition** | Starke Position in Nordeuropa, Alternative zu Racor |
| **Besonderheit** | Deutsche Entwicklung, Schwerkraft-Wasserabscheider ohne Filterelement |
| **Modellreihen** | SWK-2000/5 (klein), SWK-2000/10 (mittel), SWK-2000/40 (groß) |
| **Vertrieb DACH** | Direkt, Bukh Bremen, SVB, Marine-Motorenhändler |

### 5.8 LIQUI MOLY — Diesel-Additive

| Feld | Information |
|------|------------|
| **Firma** | LIQUI MOLY GmbH |
| **Hauptsitz** | Ulm, Deutschland |
| **Website** | www.liqui-moly.com |
| **Gründung** | 1957 |
| **Kernprodukte** | Motoröle, Additive, Pflegemittel (Automobil + Marine) |
| **Marine-Produkte** | Marine Diesel Schutz, Diesel Fließ-Fit, Super Diesel Additiv, Marine Motoröle |
| **Marine-Anteil** | <5 % (Automobil dominierend) |
| **Marktposition** | Marktführer Additive Deutschland (gesamt), Marine-Sortiment als Erweiterung |
| **Besonderheit** | Breites Sortiment, hohe Verfügbarkeit in Baumärkten und Online |
| **Vertrieb DACH** | Flächendeckend: Baumarkt, Autoteile, Online, SVB, Yachtausrüster |

---

## 6. Fehlerbild-Atlas

### 6.1 Fehlerbild F-KS-01: Dieselpest Stadium 1 — Latente Kontamination

**Erscheinung:**

| Merkmal | Beschreibung |
|---------|-------------|
| Kraftstoff-Optik | Klar bis leicht gedunkelt, keine sichtbaren Partikel |
| Filter-Optik | Normal, keine auffällige Verfärbung |
| Wasserabscheider | Geringe Wassermengen, leicht trüb |
| Geruch | Normaler Dieselgeruch, eventuell leicht muffig |
| Motor-Symptome | Keine spürbaren Veränderungen |

**Diagnose:**
- Nur durch FUELSTAT-Test oder Laboranalyse nachweisbar
- Keimzahl <10⁴ KBE/ml
- Typisch nach 6+ Monaten Standzeit mit B7-Diesel bei >50 % Füllstand

**Ursachenanalyse:**
1. Kondensatwasser im Tank (häufigste Ursache)
2. Kontaminierter Diesel getankt
3. Biodiesel-Anteil erhöht (>B7)
4. Tankbelüftung ohne Feuchtigkeitsfilter

**Maßnahmen:**
1. FUELSTAT-Test durchführen → Bestätigung
2. Wasserabscheider entleeren
3. Grotamar 82 in Normaldosis (100 ppm) zugeben
4. Motor 30 min unter Last laufen lassen
5. Wasserabscheider nach 48 h nochmals entleeren
6. Ursache beheben (Tankbelüftung, Einfüllstutzen)
7. Prophylaxe einleiten (regelmäßige Biozid-Zugabe)

**AYDI-Bewertung:** Confidence: estimated | Dringlichkeit: Gering | Kosten: 30–60 EUR

### 6.2 Fehlerbild F-KS-02: Dieselpest Stadium 2 — Aktive Kontamination

**Erscheinung:**

| Merkmal | Beschreibung |
|---------|-------------|
| Kraftstoff-Optik | Dunkel, leicht trüb, vereinzelt dunkle Fäden/Schlieren |
| Filter-Optik | Dunkle Verfärbung, braun-schwarze Ablagerungen auf Filterelement |
| Wasserabscheider | Trübes, dunkles Wasser mit schleimigen Partikeln |
| Geruch | Muffig bis leicht faulig |
| Motor-Symptome | Gelegentliches Stottern unter Last, leichter Leistungsverlust |

**Diagnose:**
- FUELSTAT-Test: "Moderat" bis "Schwer"
- Keimzahl 10⁴–10⁶ KBE/ml
- Filterstandzeit auf 50–70 % reduziert
- Druckdifferenz am Vorfilter ansteigend

**Ursachenanalyse:**
1. Unbehandelte latente Kontamination (Stadium 1 nicht erkannt)
2. Langandauernder Stillstand ohne Prophylaxe
3. Permanenter Wassereintrag (undichter Einfüllstutzen, defekte Tankbelüftung)
4. Wiederholtes Tanken von kontaminiertem Diesel

**Maßnahmen:**
1. Sofortige Stoßbehandlung mit Grotamar 82 (200–250 ppm)
2. Motor 30 min laufen lassen
3. 48 h einwirken lassen
4. Vorfilter wechseln (hohe Schmutzfracht durch abgetötete Biomasse)
5. Fuel Polishing (3 Zyklen minimum)
6. Nach 7 Tagen: FUELSTAT-Kontrolltest
7. Wöchentlich Wasserabscheider entleeren für 4 Wochen
8. Nach 4 Wochen: erneuter FUELSTAT-Test
9. Prophylaxe dauerhaft einleiten

**AYDI-Bewertung:** Confidence: documented | Dringlichkeit: Hoch | Kosten: 200–800 EUR

### 6.3 Fehlerbild F-KS-03: Dieselpest Stadium 3 — Massive Kontamination

**Erscheinung:**

| Merkmal | Beschreibung |
|---------|-------------|
| Kraftstoff-Optik | Dunkelbraun bis schwarz, dickflüssig, schleimige Klumpen |
| Filter-Optik | Komplett zugesetzt, schwarzes Gel auf Filterelement |
| Wasserabscheider | Schwarzer Schleim im Sammelglas, kaum Wasser/Diesel trennbar |
| Geruch | Stark faulig, schwefelartig (H₂S bei SRB-Beteiligung) |
| Motor-Symptome | Wiederholtes Absterben, Leistungsverlust >25 %, Motorstart problematisch |

**Diagnose:**
- FUELSTAT-Test: "Sehr schwer"
- Keimzahl >10⁶ KBE/ml
- Filter verstopft innerhalb weniger Betriebsstunden
- Biofilm auf Tankwänden (endoskopisch sichtbar)

**Ursachenanalyse:**
1. Jahrelange Vernachlässigung
2. Unzureichende Behandlung von Stadium 2
3. Permanente Wasserzufuhr (strukturelles Problem)
4. Tank nie gereinigt seit Bau/Installation

**Maßnahmen (professionelle Durchführung empfohlen):**
1. Motor NICHT starten (Risiko: Einspritzdüsen-/Pumpen-Schaden)
2. Tank komplett entleeren (per Saugpumpe)
3. Tank mechanisch reinigen (Hochdruck, Abkratzen von Biofilm)
4. Alle Leitungen durchspülen
5. Alle Filter wechseln (Vorfilter, Primärfilter, Sekundärfilter)
6. Wasserabscheider reinigen oder ersetzen
7. Einspritzdüsen prüfen lassen (Werkstatt)
8. Tank mit frischem Diesel füllen + Grotamar 82 Stoßdosis (250–500 ppm)
9. Fuel Polishing (5–8 Zyklen)
10. FUELSTAT-Kontrolltest nach 7 und 28 Tagen
11. Dauerprophylaxe zwingend
12. Ursache strukturell beheben (Tankbelüftung, Dichtungen)

**AYDI-Bewertung:** Confidence: measured | Dringlichkeit: Sehr hoch | Kosten: 1.800–6.500 EUR

### 6.4 Fehlerbild F-KS-04: Wassergehalt zu hoch — Freies Wasser im Tank

**Erscheinung:**

| Merkmal | Beschreibung |
|---------|-------------|
| Kraftstoff-Optik | Milchig-trüb (emulgiert) oder klare Wasserschicht am Boden (frei) |
| Filter-Optik | Wasserabscheider-Glas zeigt hohen Wasserstand |
| Wassererkennungspaste | Deutlicher Farbumschlag am Peilstab-Ende |
| Motor-Symptome | Unrunder Lauf, weißer Rauch, Leistungsverlust, Motorstillstand |

**Diagnose:**
- Wassergehalt >500 ppm (Labortest oder Calcium-Hydrid-Test)
- Sichtbares Wasser im Wasserabscheider-Glas
- Wassererkennungspaste am Peilstab zeigt >5 mm Wasser

**Ursachenanalyse:**

| Ursache | Wahrscheinlichkeit | Prüfung |
|---------|--------------------|---------| 
| Kondensation (halb leerer Tank, Temperaturwechsel) | Hoch | Tankfüllstand-Protokoll prüfen |
| Undichter Einfüllstutzen | Mittel | Wassertest von oben, Dichtung prüfen |
| Defekte Tankbelüftung (Wasser dringt ein) | Mittel | Belüftung auf Schwanenhals und Position prüfen |
| Kontaminiertes Bunkern (Wasser in Tankstelle) | Gering–Mittel | Tankstellenwechsel, Probe beim Bunkern |
| Defekte Einfüllleitung (Riss, undichte Verbindung) | Gering | Alle Verbindungen prüfen |
| Tankdurchrostung (Kondenswasser von außen) | Gering (aber schwerwiegend) | Tankinspektion |

**Maßnahmen:**
1. Wasserabscheider sofort entleeren
2. Freies Wasser vom Tankboden absaugen (Handpumpe oder Fuel Polishing)
3. Ursache identifizieren und beheben
4. Fuel Polishing mit Koaleszenzelement (1–3 Zyklen)
5. FUELSTAT-Test (Wasser → Dieselpest-Risiko!)
6. Biozid prophylaktisch zugeben
7. Wassergehalt nach 1 Woche per Calcium-Hydrid-Test kontrollieren

**AYDI-Bewertung:** Confidence: measured | Dringlichkeit: Hoch | Kosten: 100–500 EUR (ohne Ursachenbehebung)

### 6.5 Fehlerbild F-KS-05: Paraffin-Ausflockung (Kälteversagen)

**Erscheinung:**

| Merkmal | Beschreibung |
|---------|-------------|
| Kraftstoff-Optik | Trüb bis wachsig, weiße Flocken/Kristalle sichtbar |
| Filter-Optik | Wachsartige, weiße Masse auf Filterelement |
| Temperatur | Umgebungs- oder Kraftstofftemperatur unter CFPP-Grenzwert |
| Motor-Symptome | Motor startet nicht oder stirbt kurz nach Start ab |

**Diagnose:**
- Kraftstofftemperatur messen (Infrarot-Thermometer)
- Kraftstoffprobe in klares Glas → weiße Flocken/Trübung sichtbar
- Typisch bei Sommer-Diesel und plötzlichem Kälteeinbruch
- Häufig bei Überführungen Nord→Süd→Nord

**Maßnahmen:**
1. KEINE Fließverbesserer in bereits ausgefallenen Diesel geben (wirkungslos!)
2. Kraftstoff erwärmen: Motorraum heizen (Diesel-Standheizung, Heizlüfter)
3. Filter wechseln (Paraffinverstopfung löst sich nicht auf)
4. Wenn möglich: warmen Diesel nachfüllen (mindestens 50 % des Tankinhalts)
5. Nach Erwärmung (>10 °C): Fließverbesserer zugeben (für künftigen Schutz)
6. Racor-Filterheizung nachrüsten (R58064 für Racor 200/320-Serie)
7. Vor Winterfahrten: rechtzeitig Winterdiesel tanken oder Additiv zugeben

**Prävention:**
- Bei Herbstfahrten: spätestens ab Oktober Fließverbesserer zum Sommerdiesel
- Bei Nordlandfahrten: lokalen Diesel tanken (Arktik-Diesel)
- Racor-Filterheizung: Thermostat auf 5 °C, schaltet automatisch zu

**AYDI-Bewertung:** Confidence: measured | Dringlichkeit: Hoch (akuter Ausfall) | Kosten: 50–200 EUR (+ ggf. Filterheizung 150–250 EUR)

### 6.6 Fehlerbild F-KS-06: Verstopfter Rücklauf

**Erscheinung:**

| Merkmal | Beschreibung |
|---------|-------------|
| Motor-Symptome | Unruhiger Lauf, Dieselklopfen, Leistungsverlust, hoher Einspritzdruck |
| Leitungen | Rücklaufleitung heiß, möglicherweise aufgebläht |
| Tank | Kraftstoff kommt nicht oder sehr langsam zurück |
| Manometer (falls vorhanden) | Rücklaufdruck >2 bar (normal: 0,2–0,5 bar) |

**Diagnose:**
- Rücklaufleitung am Tank lösen → fließt Diesel frei zurück?
- Rücklaufleitung durchblasen → Widerstand?
- Rücklauf-Rückschlagventil prüfen (falls vorhanden)
- Rücklauf-Tankstutzen auf Verstopfung prüfen

**Ursachenanalyse:**

| Ursache | Wahrscheinlichkeit | Prüfung |
|---------|--------------------|---------| 
| Rücklaufleitung geknickt | Hoch | Leitung visuell auf Knicke absuchen |
| Rücklauf-Tankstutzen verstopft (Sediment/Biofilm) | Hoch | Stutzen ausbauen und prüfen |
| Rücklaufleitung innen verharzt (Alterung) | Mittel | Leitung durchblasen, ggf. ersetzen |
| Rückschlagventil defekt/verklebt | Mittel | Ventil ausbauen, reinigen oder tauschen |
| Rücklaufleitung falsch verlegt (Siphon) | Gering | Leitungsverlauf prüfen |

**Maßnahmen:**
1. Rücklaufleitung auf Knicke prüfen und begradigen
2. Rücklauf-Tankstutzen reinigen oder ersetzen
3. Rücklaufleitung durchblasen (Druckluft, max. 2 bar)
4. Bei verharzter Leitung: Leitung ersetzen
5. Rückschlagventil reinigen oder tauschen
6. Nach Reparatur: Motor starten, Rücklauftemperatur und -druck prüfen

**AYDI-Bewertung:** Confidence: documented | Dringlichkeit: Hoch | Kosten: 50–300 EUR

### 6.7 Fehlerbild F-KS-07: Tankbelüftung defekt

**Erscheinung:**

| Merkmal | Beschreibung |
|---------|-------------|
| Tanken | Kraftstoff läuft langsam oder gar nicht in den Tank |
| Betrieb | Motor stottert, saugt Luft (Unterdruckblase im Tank) |
| Entlüftung | Kein Luftstrom fühlbar am Entlüftungsstutzen |
| Geruch | Dieselgeruch an Deck (falls Belüftung ins Freie führt und Diesel austritt) |

**Diagnose:**
- Tankbelüftung am Deckdurchlass durchblasen (Mund oder Druckluft)
- Widerstand → Verstopfung
- Tankeinfüllstutzen öffnen bei laufendem Motor → verbessert sich Motorlauf? → Belüftung defekt

**Ursachenanalyse:**

| Ursache | Wahrscheinlichkeit | Prüfung |
|---------|--------------------|---------| 
| Insektennest in Belüftungsleitung | Hoch (besonders nach Winterlager) | Durchblasen, Endoskop |
| Belüftungsleitung geknickt | Mittel | Visuell prüfen |
| Belüftungs-Rückschlagventil defekt | Mittel | Ventil ausbauen, prüfen |
| Flammendurchschlagsicherung verstopft | Mittel | Sieb/Gitter reinigen |
| Belüftungsleitung mit Diesel vollgelaufen | Gering | Leitung entleeren (Bootslage geändert?) |

**Maßnahmen:**
1. Belüftungsleitung von Deck durchblasen (beide Richtungen)
2. Flammendurchschlagsicherung reinigen (Drahtgeflecht)
3. Rückschlagventil prüfen und ggf. ersetzen
4. Bei Insektenbefall: Leitung mit Druckluft reinigen, Insektenschutz nachrüsten
5. Leitungsverlauf prüfen: Schwanenhals korrekt? Kein Siphon?
6. Nach Reparatur: Tankbelüftung testen (Tanken + Motorlauf)

**AYDI-Bewertung:** Confidence: documented | Dringlichkeit: Mittel–Hoch | Kosten: 30–200 EUR

### 6.8 Fehlerbild F-KS-08: Kraftstoffgeruch in Bilge

**Erscheinung:**

| Merkmal | Beschreibung |
|---------|-------------|
| Geruch | Deutlicher Dieselgeruch unter Bodenbrettern / im Motorraum |
| Bilge | Öliger Film auf Bilgenwasser, Regenbogeneffekt |
| Leckage | Möglicherweise Tropfen an Leitungen/Verbindungen sichtbar |
| Sicherheit | Brandgefahr! Flammpunkt Diesel ≥55 °C, aber Dampf kann sich bei Zündquellen entzünden |

**Diagnose:**
- Alle Kraftstoffverbindungen mit weißem Küchenpapier abtupfen → Diesel sichtbar?
- Leitungen unter Druck setzen (Motor laufen) und beobachten
- Tank-Absperrventil schließen → Leck verschwindet? → Leck zwischen Tank und Ventil
- Absperrventil öffnen, Motor aus → Leck sichtbar? → Leck in Zulaufleitung

**Ursachenanalyse:**

| Ursache | Wahrscheinlichkeit | Prüfung |
|---------|--------------------|---------| 
| Lose Schlauchschelle | Hoch | Alle Schellen prüfen und nachziehen |
| Alterungsbedingter Schlauch-Riss | Hoch (>10 Jahre) | Schläuche auf Risse, Verhärtung prüfen |
| Undichte Filterverbindung | Mittel | O-Ring am Filtergehäuse prüfen |
| Undichte Einspritzleitung | Mittel | Verbindungen am Motor prüfen |
| Tank-Fitting undicht | Gering–Mittel | Tankverbindungen prüfen |
| Tankriss/-durchrostung | Gering (aber schwerwiegend!) | Tankinspektion |

**Sofortmaßnahmen:**
1. **Sicherheit:** Keine Zündquellen! Belüftung maximieren!
2. Leckstelle lokalisieren
3. Tank-Absperrventil schließen (wenn Leck in Zulaufleitung)
4. Bilge trockenlegen (Diesel ordnungsgemäß entsorgen!)
5. Leck reparieren (Schelle nachziehen, Schlauch ersetzen, O-Ring erneuern)
6. Nach Reparatur: 24 h beobachten, Bilge kontrollieren

**AYDI-Bewertung:** Confidence: measured | Dringlichkeit: Sehr hoch (Brandgefahr!) | Kosten: 30–500 EUR (je nach Ursache)

### 6.9 Fehlerbild F-KS-09: Luftziehen im Kraftstoffsystem

**Erscheinung:**

| Merkmal | Beschreibung |
|---------|-------------|
| Motor-Symptome | Unrunder Lauf, Stottern, plötzliches Absterben, schwerer Neustart |
| Vorfilter | Luftblasen im Sichtglas sichtbar |
| Neustart | Erst nach mehrfachem Entlüften möglich |
| Besonderheit | Tritt oft nach Filterwechsel oder Standzeit auf |

**Ursachenanalyse:**

| Ursache | Wahrscheinlichkeit | Prüfung |
|---------|--------------------|---------| 
| Undichte Saugseite (Tank→Förderpumpe) | Hoch | Alle Verbindungen auf Saugseite prüfen |
| O-Ring Filtergehäuse nicht korrekt eingesetzt | Hoch (nach Filterwechsel) | Filter-O-Ring kontrollieren |
| Ansaugleitung porös | Mittel | Schlauch unter Unterdruck prüfen |
| Tankfüllstand unter Ansaugstutzen | Mittel | Tankfüllstand prüfen |
| Förderpumpe defekt (Membranriss) | Gering–Mittel | Pumpenfunktion prüfen |

**Maßnahmen:**
1. System entlüften (Handentlüftungspumpe am Motor betätigen)
2. Saugseite: alle Verbindungen nachziehen
3. Filter-O-Ring prüfen, einfetten (Diesel oder Vaseline, KEIN Silikonöl!)
4. Schläuche auf Saugseite auf Porosität prüfen (Drucktest mit Seifenwasser)
5. Förderpumpe prüfen (Handpumpe → Unterdruck aufbauen und halten?)

**AYDI-Bewertung:** Confidence: documented | Dringlichkeit: Hoch | Kosten: 20–300 EUR

### 6.10 Fehlerbild F-KS-10: Einspritzdüsen verkokt

**Erscheinung:**

| Merkmal | Beschreibung |
|---------|-------------|
| Abgase | Schwarzer oder blau-schwarzer Rauch |
| Motor | Unrunder Lauf, einzelne Zylinder zünden ungleichmäßig |
| Leistung | Spürbarer Leistungsverlust (10–30 %) |
| Verbrauch | Erhöht um 10–25 % |
| Geräusch | Dieselklopfen, ungleichmäßiges Motorgeräusch |

**Diagnose:**
- Einspritzdüsen ausbauen und prüfen (Werkstatt mit Düsenprüfstand)
- Strahlbild prüfen: feiner Nebel = OK, Strahl/Tropfen = verkokt
- Öffnungsdruck messen: Soll vs. Ist vergleichen
- Dichtigkeit prüfen: Nachtropfen bei 20 bar unter Öffnungsdruck?

**Ursachenanalyse:**
1. Schlechte Kraftstoffqualität über längere Zeit
2. Zu viele Kaltlaufphasen (Kurzstreckenbetrieb auf See)
3. Fehlende Additive (Injektorreiniger)
4. Filter nicht gewechselt → Partikel im Kraftstoff

**Maßnahmen:**
1. Einspritzdüsen beim Fachmechaniker prüfen lassen
2. Leicht verkokt: Injektorreiniger-Additiv über 2–3 Tankfüllungen
3. Stark verkokt: Düsen im Ultraschallbad reinigen (Werkstatt)
4. Schwer beschädigt: Düsen ersetzen (100–400 EUR/Düse je nach Motor)
5. Künftig: Regelmäßig Diesel Kleen oder äquivalenten Reiniger zugeben

**AYDI-Bewertung:** Confidence: measured | Dringlichkeit: Mittel | Kosten: 50–1.600 EUR (4-Zylinder)

### 6.11 Fehlerbild F-KS-11: Tankpeiltab/Tanksensor defekt

**Erscheinung:**

| Merkmal | Beschreibung |
|---------|-------------|
| Anzeige | Falsche Füllstandsanzeige, springend, dauerhaft voll oder leer |
| Planung | Verbrauchsberechnung stimmt nicht mit Anzeige überein |
| Risiko | Motor geht unverhofft aus (Tank leer trotz Anzeige "halb voll") |

**Diagnose:**
- Vergleich Tankanzeige vs. manuelle Peilung (Peilstab/Messstab)
- Vergleich Tankanzeige vs. getankter Menge (Rechnung)
- Widerstandsmessung am Sensor (Multimeter): Widerstand muss sich mit Füllstand ändern
- Kabelverbindungen prüfen (Korrosion an Steckern)

**Maßnahmen:**
1. Stecker und Kabelverbindungen reinigen (Kontaktspray)
2. Sensor-Schwimmer auf Beweglichkeit prüfen (verklebt bei Dieselpest!)
3. Sensor-Widerstand kalibrieren (Herstelleranleitung)
4. Bei Defekt: Sensor ersetzen (80–250 EUR je nach Typ)
5. Regelmäßige manuelle Kontrolle als Backup (Peilstab oder Tankrechnung)

**AYDI-Bewertung:** Confidence: documented | Dringlichkeit: Mittel | Kosten: 30–250 EUR

### 6.12 Fehlerbild F-KS-12: Dieselgeruch im Innenraum

**Erscheinung:**

| Merkmal | Beschreibung |
|---------|-------------|
| Geruch | Persistenter Dieselgeruch in Kabine, Salon, Pantry |
| Zeitpunkt | Besonders bei laufendem Motor oder nach dem Tanken |
| Gesundheit | Kopfschmerzen, Übelkeit bei empfindlichen Personen |

**Ursachenanalyse:**

| Ursache | Wahrscheinlichkeit | Prüfung |
|---------|--------------------|---------| 
| Tankbelüftung führt in Innenraum statt nach außen | Hoch | Belüftungsleitung verfolgen |
| Einfüllstutzen undicht (Geruch steigt auf) | Mittel | Dichtung prüfen |
| Diesel in Bilge (Leckage, siehe F-KS-08) | Mittel | Bilge inspizieren |
| Motor-Auspuffsystem undicht | Mittel | Auspuff-Dichtungen prüfen |
| Kraftstoffleitung durch Innenraum verlegt, undicht | Gering | Leitungen im Innenraum prüfen |
| Tank-Inspektionsdeckel nicht dicht | Gering | Deckel und Dichtung prüfen |

**Maßnahmen:**
1. Lecksuche systematisch (siehe F-KS-08)
2. Tankbelüftung auf korrekte Führung nach außenbords prüfen
3. Alle Dichtungen im System auf Geruchsdichtigkeit prüfen
4. Nach Reparatur: Innenraum gründlich lüften
5. Aktivkohle-Absorber aufstellen (kurzfristige Geruchsbindung)

**AYDI-Bewertung:** Confidence: estimated | Dringlichkeit: Mittel (Komfort) bis Hoch (Gesundheit) | Kosten: 30–500 EUR

---

## 7. Troubleshooting-Entscheidungsbäume

### 7.1 Entscheidungsbaum 1: Motor startet nicht (kraftstoffseitig)

```
Motor startet nicht
    │
    ├── Kraftstoff im Tank?
    │   ├── NEIN → Tanken. System entlüften. ■ ERLEDIGT
    │   └── JA ↓
    │
    ├── Absperrventil offen?
    │   ├── NEIN → Ventil öffnen. System entlüften. ■ ERLEDIGT
    │   └── JA ↓
    │
    ├── Vorfilter/Wasserabscheider prüfen:
    │   ├── Wasser im Sichtglas? → JA → Wasser ablassen, System entlüften
    │   │                                ├── Motor startet → ■ ERLEDIGT
    │   │                                └── Motor startet nicht → weiter ↓
    │   ├── Luftblasen im Sichtglas? → JA → Luftziehen (→ F-KS-09)
    │   │                                    Saugseite alle Verbindungen prüfen
    │   │                                    O-Ring Filtergehäuse prüfen
    │   │                                    ├── Leck gefunden → reparieren → ■ ERLEDIGT
    │   │                                    └── Kein Leck → Förderpumpe defekt? ↓
    │   ├── Schwarzer Schleim sichtbar? → JA → Dieselpest Stadium 2–3
    │   │                                       Filter wechseln, Entlüften
    │   │                                       → Motor startet? → Notbetrieb, Hafen anlaufen
    │   │                                       → Dieselpest-Sanierung (→ 3.2)
    │   └── Filter sauber, kein Wasser → weiter ↓
    │
    ├── Förderpumpe prüfen:
    │   ├── Handentlüftungspumpe am Motor betätigen
    │   │   ├── Kein Widerstand / kein Druck → Förderpumpe defekt
    │   │   │                                  → Membran oder Pumpe ersetzen
    │   │   └── Druck vorhanden → weiter ↓
    │
    ├── Motor-Sekundärfilter prüfen:
    │   ├── Filter >500 h alt? → JA → Filter wechseln, entlüften
    │   └── Filter relativ neu → weiter ↓
    │
    ├── Kälte-Problem?
    │   ├── Außentemperatur unter 0 °C? → JA → Paraffinausflockung? (→ F-KS-05)
    │   │                                       Filter wechseln, Kraftstoff erwärmen
    │   └── NEIN → weiter ↓
    │
    └── Einspritzsystem-Problem (Werkstatt erforderlich):
        ├── Einspritzdüsen defekt/verkokt (→ F-KS-10)
        ├── Einspritzpumpe defekt
        ├── Common-Rail-Drucksensor defekt
        └── Steuergerät-Fehler (OBD-Diagnose)
```

### 7.2 Entscheidungsbaum 2: Leistungsverlust bei Seegang

```
Motor verliert Leistung bei Seegang (Wellen, Krängung, Stampfen)
    │
    ├── Tritt nur bei Seegang auf, nicht im Hafen?
    │   ├── NEIN → Allgemeines Motorproblem, nicht spezifisch Seegang
    │   │          → Standard-Motor-Troubleshooting
    │   └── JA → Kraftstoffsystem-Problem wahrscheinlich ↓
    │
    ├── Tankfüllstand prüfen:
    │   ├── Tank <25 %? → JA → Ansaugstutzen wird bei Neigung freigelegt
    │   │                       → Tanken! Problem gelöst bei >50 %
    │   │                       → Wenn weiterhin: Ansaugstutzen-Position prüfen
    │   └── NEIN → weiter ↓
    │
    ├── Vorfilter/Wasserabscheider prüfen:
    │   ├── Wasser im Sichtglas (durch Seegang aufgewirbelt)?
    │   │   ├── JA → Wasser ablassen. Tankreinigung empfohlen.
    │   │   │        Ursache: Wasser am Tankboden wird bei Seegang aufgewirbelt
    │   │   │        → Fuel Polishing, Tankbodenabsaugung
    │   │   └── NEIN → weiter ↓
    │   ├── Schwarze Partikel im Filter (aufgewirbeltes Sediment / Dieselpest)?
    │   │   ├── JA → Sediment/Biofilm am Tankboden wird bei Seegang aufgewirbelt
    │   │   │        → Filter wechseln (Notmaßnahme auf See)
    │   │   │        → Hafen: Tankreinigung + Fuel Polishing + Biozid
    │   │   └── NEIN → weiter ↓
    │
    ├── Schwallwände im Tank vorhanden?
    │   ├── NEIN → Kraftstoff schwallt bei Seegang heftig
    │   │          → Ansaugstutzen kann periodisch frei werden
    │   │          → Schwallwände nachrüsten (Werftarbeit)
    │   └── JA → weiter ↓
    │
    ├── Rücklaufleitung-Position prüfen:
    │   ├── Rücklauf und Ansaugung nah beieinander?
    │   │   → JA → Bei Seegang Rücklauf-Diesel direkt angesaugt (mit Luft)
    │   │          → Rücklauf auf gegenüberliegende Tankseite verlegen
    │   └── NEIN → weiter ↓
    │
    └── Tankbelüftung prüfen:
        ├── Bei Seegang: Tankbelüftung periodisch unter Wasser?
        │   → JA → Wasser dringt durch Belüftung in Tank
        │          → Belüftung höher setzen oder Schwanenhals nachrüsten
        └── NEIN → Weitergehende Diagnose erforderlich (Motorlagerung, Antrieb)
```

### 7.3 Entscheidungsbaum 3: Schwarzer Schleim im Filter

```
Schwarzer Schleim / geleeartiges Material im Vorfilter oder Wasserabscheider
    │
    ├── Konsistenz prüfen:
    │   ├── Gelee-artig, schleimig, fadenziehend?
    │   │   → JA → Dieselpest (mikrobielle Kontamination) → weiter ↓
    │   ├── Hart, körnig, bröckelig?
    │   │   → Sediment / oxidierter Diesel (Gum & Lacquer)
    │   │   → Fuel Polishing + Tank reinigen
    │   │   → Kraftstoff austauschen wenn stark oxidiert
    │   └── Gummiartig, elastisch?
    │       → Dichtungsmaterial (Schlauch-Innenleben aufgelöst)
    │       → Alle Schläuche prüfen, nicht-diesel-feste Schläuche ersetzen
    │
    ├── [Bei Dieselpest-Verdacht] FUELSTAT-Test durchführen:
    │   ├── Negativ → Kein biologisches Material
    │   │              → Ursache ist chemisch (Oxidation, Polymerisation)
    │   │              → Fuel Polishing + Stabilisator
    │   ├── Moderat → Stadium 1–2
    │   │              → Biozid Stoßdosis + Fuel Polishing (→ 3.2.2)
    │   ├── Schwer → Stadium 2–3
    │   │            → Biozid Stoßdosis + Fuel Polishing + evtl. Tankreinigung
    │   └── Sehr schwer → Stadium 3
    │                     → Komplette Systemreinigung zwingend (→ F-KS-03)
    │
    ├── Sofortmaßnahme (auf See):
    │   ├── Filter wechseln (Ersatzfilter an Bord?)
    │   │   ├── JA → Filter wechseln, entlüften, Motor starten
    │   │   │        → Hafen anlaufen zur Systemreinigung
    │   │   └── NEIN → Filter reinigen (notdürftig: Diesel durchspülen)
    │   │              → Langsam Hafen anlaufen
    │   └── Duplex-Filteranlage vorhanden?
    │       → JA → Auf Reservefilter umschalten, Hafen anlaufen
    │
    └── Langfristmaßnahme:
        ├── Tankreinigung
        ├── Leitungsspülung
        ├── Alle Filter ersetzen
        ├── Biozid + Fuel Polishing
        ├── Prophylaxe einleiten
        └── Ursache beheben (Wasserquelle!)
```

### 7.4 Entscheidungsbaum 4: Kraftstoffverbrauch erhöht

```
Kraftstoffverbrauch deutlich erhöht (>15 % über Referenzwert)
    │
    ├── Verbrauch korrekt gemessen?
    │   ├── Tankfüllstand-Anzeige zuverlässig? (→ F-KS-11)
    │   ├── Betriebsstunden korrekt?
    │   ├── Strömung/Wind berücksichtigt?
    │   └── Bewuchsgrad Unterwasserschiff? (→ andere Wissensdatei)
    │
    ├── Kraftstoffqualität prüfen:
    │   ├── Kraftstoffprobe optisch beurteilen
    │   │   ├── Dunkel / trüb → Alterung / Kontamination
    │   │   │                    → Fuel Polishing + ggf. Biozid
    │   │   └── Klar → weiter ↓
    │   ├── Letzter Tankvorgang: unbekannte Qualität?
    │   │   → Laboranalyse: Cetanzahl, Dichte, Wassergehalt
    │   │   → Niedrige Cetanzahl (<48) = schlechtere Verbrennung = Mehrverbrauch
    │   └── Biodiesel-Anteil hoch (>B7)?
    │       → B20 hat ~5 % weniger Energiegehalt als B0
    │
    ├── Filtersystem prüfen:
    │   ├── Vorfilter-Druckdifferenz hoch?
    │   │   → JA → Filter wechseln (Motor arbeitet gegen erhöhten Widerstand)
    │   └── Filter OK → weiter ↓
    │
    ├── Einspritzdüsen prüfen:
    │   ├── Schwarzer Rauch? → Verkokte Düsen (→ F-KS-10)
    │   │                       → Injektorreiniger + ggf. Düsen prüfen lassen
    │   └── Kein schwarzer Rauch → weiter ↓
    │
    ├── Motorspezifisch:
    │   ├── Ventilspiel korrekt?
    │   ├── Luftfilter sauber?
    │   ├── Turbolader (falls vorhanden) OK?
    │   ├── Ladeluft-Kühler sauber?
    │   └── Auspuffgegendruck normal? (Rußfilter, Wassersammler)
    │
    └── Rumpf/Propeller:
        ├── Bewuchs am Unterwasserschiff?
        ├── Propeller beschädigt/bewachsen?
        └── Trim-Tabs / Interceptors korrekt eingestellt?
```

### 7.5 Entscheidungsbaum 5: Dieselgeruch im Boot

```
Dieselgeruch wahrnehmbar im Boot (Innenräume)
    │
    ├── Wann tritt Geruch auf?
    │   ├── Beim Tanken → Einfüllstutzen/Belüftung-Problem
    │   │   ├── Einfüllstutzen-Dichtung prüfen
    │   │   ├── Überlaufleitung/Belüftung korrekt nach außen geführt?
    │   │   └── Einfüllleitung dicht? (Schlauchschellen prüfen)
    │   │
    │   ├── Bei laufendem Motor → Leck im Drucksystem
    │   │   ├── Alle Verbindungen Motor→Filter→Leitungen prüfen
    │   │   ├── Einspritzleitungen auf Tropfen prüfen
    │   │   └── Diesel in Bilge? (→ F-KS-08)
    │   │
    │   ├── Permanent (auch bei Stillstand) → Tank/Belüftungs-Problem
    │   │   ├── Tankbelüftung korrekt nach außen geführt?
    │   │   ├── Tank-Inspektionsdeckel dicht?
    │   │   ├── Tank undicht? (→ Tankinspektion)
    │   │   └── Diesel in Bilge von früherem Leck?
    │   │       → Bilge mit Bilgenreiniger behandeln
    │   │
    │   └── Bei Seegang → Belüftung/Überlauf-Problem
    │       ├── Tankbelüftung Schwanenhals vorhanden?
    │       ├── Tank Überlauf → Belüftung durch Seegang
    │       └── Einfüllstutzen: Schapps in der Nähe?
    │
    ├── Intensität beurteilen:
    │   ├── Leicht (nur bei genauem Riechen) → Hinweis, nicht akut
    │   ├── Deutlich (sofort wahrnehmbar) → Zeitnah suchen und beheben
    │   └── Stark (Kopfschmerzen, Übelkeit) → SOFORT handeln!
    │       → Lüften! → Lecksuche → ggf. Hafen anlaufen
    │
    └── Systematische Lecksuche:
        1. Alle Bodenbretter hochnehmen
        2. Bilge auf Dieselfilm prüfen
        3. Kraftstoff-Absperrventil schließen
        4. Alle Leitungen mit Küchenpapier abtupfen
        5. Filtergehäuse und -verbindungen prüfen
        6. Motor-Einspritzbereich prüfen
        7. Einfüllstutzen und Tankbelüftung prüfen
        8. Gefundenes Leck markieren und reparieren
        9. Nach Reparatur: 24 h beobachten
```

---

## 8. FAQ

### 8.1 Grundlagen

**F1: Was ist Dieselpest?**
A: Dieselpest (englisch: Diesel Bug) ist die Bezeichnung für die mikrobielle Kontamination von Dieselkraftstoff durch Pilze, Hefen und Bakterien. Die Organismen leben an der Grenzschicht zwischen Wasser und Diesel im Tank und nutzen Kohlenwasserstoffe als Nahrungsquelle. Sie bilden Biofilme, schleimige Ablagerungen und organische Säuren, die Filter verstopfen, Tankwände korrodieren und den Motor lahmlegen können.

**F2: Warum ist Dieselpest bei Booten häufiger als bei Autos?**
A: Drei Hauptgründe: (1) Lange Standzeiten — Boot steht wochen- bis monatelang still, während ein Auto fast täglich bewegt wird. (2) Höhere Feuchtigkeit — maritime Umgebung bedeutet 60–95 % relative Luftfeuchtigkeit, die durch die Tankbelüftung eindringt und kondensiert. (3) Größere Temperaturschwankungen — unbeheizter Motorraum führt zu Tag-Nacht-Kondensationszyklen.

**F3: Kann ich Dieselpest riechen?**
A: In Stadium 1 nicht. Ab Stadium 2 riecht der Diesel leicht muffig. In Stadium 3 kann ein deutlich fauliger Geruch auftreten, bei Beteiligung von sulfatreduzierenden Bakterien (SRB) auch ein Geruch nach faulen Eiern (H₂S). Aber Vorsicht: Nicht jeder veränderte Geruch bedeutet Dieselpest — auch oxidierter Diesel riecht "alt".

**F4: Ist Dieselpest gefährlich für den Menschen?**
A: Direkte Gesundheitsgefahr bei normalem Umgang besteht nicht. Allerdings kann Pseudomonas aeruginosa (ein möglicher Dieselpest-Organismus) bei immungeschwächten Personen Infektionen verursachen. Grundregel: Bei Tankreinigung und Kontakt mit kontaminiertem Diesel immer Handschuhe und Schutzbrille tragen. H₂S-Geruch → gut lüften!

**F5: Wie oft sollte ich den Wasserabscheider entleeren?**
A: Mindestens monatlich während der Saison. Bei bekanntem Wasserproblem oder nach Tanken in unbekannten Häfen: alle 2 Wochen. Vor jeder längeren Fahrt: prüfen und bei Bedarf entleeren. Nach Winterlager: vor dem ersten Motorstart.

### 8.2 Biozide und Additive

**F6: Kann ich Grotamar 82 und Marine 16 gleichzeitig verwenden?**
A: Nein, das wird nicht empfohlen. Beide enthalten Biozid-Wirkstoffe, und die Kombination könnte zu unerwünschten Wechselwirkungen führen. Entscheiden Sie sich für ein System: entweder Grotamar 82 + separater Stabilisator (z.B. Fuel Set Diesel Kleen) ODER Marine 16 allein.

**F7: Wie lange hält die Wirkung von Grotamar 82?**
A: Grotamar 82 ist ein Kontaktbiozid — es tötet vorhandene Organismen ab und baut sich dann ab. Die aktive Schutzwirkung beträgt ca. 3–6 Monate bei Normaldosis. Daher die Empfehlung: bei jeder 2.–3. Betankung nachdosieren.

**F8: Wirkt Biozid auch gegen Paraffin-Ausflockung oder Oxidation?**
A: Nein! Biozide wirken ausschließlich gegen mikrobielle Organismen. Gegen Paraffin-Ausflockung brauchen Sie einen Fließverbesserer (Cold Flow Improver), gegen Oxidation einen Kraftstoff-Stabilisator. Diese Produkte sind komplementär, nicht austauschbar.

**F9: Sind Biozide schädlich für den Motor?**
A: Bei korrekter Dosierung nicht. Alle genannten Biozide (Grotamar 82, Marine 16, Dieselguard) sind in den empfohlenen Konzentrationen motor- und dichtungsverträglich. Überdosierung (>500 ppm MBT) sollte jedoch vermieden werden, da sie die Einspritzpumpen-Schmierung beeinträchtigen kann.

**F10: Was passiert mit den abgetöteten Mikroorganismen nach der Biozid-Behandlung?**
A: Die toten Organismen sinken als Biomasse zu Boden oder schwimmen als Partikel im Diesel. Deshalb ist es wichtig, 48 Stunden nach der Stoßbehandlung den Vorfilter zu wechseln — der fängt die tote Biomasse auf und kann sich schnell zusetzen.

### 8.3 Filtration und Fuel Polishing

**F11: Wie erkenne ich, wann der Vorfilter gewechselt werden muss?**
A: (1) Druckdifferenzanzeige (Vacuometer) am Racor-Filter im gelben oder roten Bereich. (2) Motor verliert Leistung unter Last. (3) Sichtbar verschmutztes Filterelement. (4) Spätestens nach 200 Betriebsstunden oder jährlich — je nachdem, was zuerst eintritt.

**F12: Lohnt sich ein fest installiertes Fuel Polishing System?**
A: Ab 300 L Tankvolumen und/oder regelmäßigen Standzeiten >4 Wochen: ja. Die Investition (1.500–4.000 EUR) amortisiert sich durch vermiedene Tankreinigungen, Filterwechsel und vor allem durch den Schutz des Einspritzsystems. Für Blauwassersegler und Yachten mit >500 L Tank fast schon Pflicht.

**F13: Kann ich Racor-Filter mit günstigeren Nachbau-Elementen bestücken?**
A: Es gibt Nachbau-Filterelemente, aber Vorsicht: Die Filtrationsleistung und insbesondere die Wasserabscheidung sind oft deutlich schlechter als beim Original. Bei einem Motor, dessen Einspritzsystem 5.000–15.000 EUR kostet, sind die 5–10 EUR Ersparnis pro Filterelement ein schlechtes Geschäft. Empfehlung: Original-Racor-Elemente verwenden.

**F14: Was ist der Unterschied zwischen Fuel Polishing und einem normalen Filter?**
A: Der normale Vorfilter filtert den Kraftstoff einmal auf dem Weg zum Motor. Fuel Polishing rezirkuliert den gesamten Tankinhalt mehrfach (3–8 Zyklen) durch ein mehrstufiges Filtersystem mit Koaleszenzer, und zwar unabhängig vom Motorbetrieb. Es ist eine aktive Tankpflege, kein reiner Motorschutz.

**F15: Wie oft sollte ich Fuel Polishing durchführen?**
A: Vor Saisonstart (nach Winterlager), nach Langstreckenfahrten mit unbekanntem Diesel, bei Verdacht auf Kontamination, und idealerweise einmal monatlich bei längerem Stillstand. Bei fest installiertem System: Timer auf wöchentlich 2–4 Stunden.

### 8.4 Winterfestmachung und Lagerung

**F16: Soll ich den Tank zum Einwintern voll oder leer machen?**
A: VOLL. Ein voller Tank hat minimal Luftraum → minimal Kondensation. Ein leerer Tank hat maximale Oberfläche für Kondensation und bei Metalltanks das zusätzliche Risiko der Innenkorrosion. Ausnahme: Bei Langzeiteinlagerung >24 Monate kann Entleerung + Konservierung sinnvoller sein (siehe 3.5).

**F17: Kann ich Heizöl (EL) statt Diesel tanken?**
A: In Deutschland: nein, für Sportboote auf Binnenwasserstraßen und Seeschifffahrtsstraßen ist rot eingefärbtes Heizöl nicht zulässig (Energiesteuergesetz). In einigen Mittelmeerländern und skandinavischen Ländern gibt es steuerbefreiten Marine-Diesel (farblich gekennzeichnet), der legal getankt werden darf. Technisch ist Heizöl EL dem Diesel sehr ähnlich, aber die Schmierfähigkeit kann schlechter sein (HFRR höher), und die Einspritzpumpe leidet langfristig.

**F18: Muss ich im Winterlager den Motor gelegentlich laufen lassen?**
A: Umstritten. Viele Werftbetriebe empfehlen es nicht, da kurzes Laufen ohne Last (kein Wasser für Kühlung am Landliegeplatz!) den Motor mehr schädigt als nützt. Wenn doch: nur mit Kühlwasserversorgung (Gartenschlauch am Seewassereinlass), mindestens 30 min unter leichter Last (Lichtmaschine belasten), damit Betriebstemperatur erreicht wird.

**F19: Was ist der größte Fehler bei der Winterfestmachung?**
A: Tank halb leer lassen. In einem halbleeren Tank kondensiert über den Winter die größte Menge Wasser, weil die große Luftmasse im Tank bei jedem Temperaturwechsel Feuchtigkeit abgibt. Zusammen mit der langen Standzeit ist dies die häufigste Ursache für Dieselpest-Neuinfektionen im Frühling.

### 8.5 Troubleshooting

**F20: Mein Motor startet nach dem Filterwechsel nicht — was tun?**
A: System entlüften! Beim Filterwechsel gelangt Luft ins System. Entlüftungsschritte: (1) Handentlüftungspumpe am Motor betätigen, bis Diesel blasenfrei austritt. (2) Manche Motoren haben eine elektrische Entlüftungspumpe — Zündung einschalten und warten. (3) Bei Racor-Filtern: Filtergehäuse vor dem Einsetzen des neuen Elements mit sauberem Diesel füllen (reduziert Luftmenge).

**F21: Der Motor läuft bei Seegang unrund — ist das Dieselpest?**
A: Möglicherweise, aber es gibt mehrere Ursachen. Am häufigsten: Sediment oder Wasser am Tankboden wird durch Seegang aufgewirbelt und verstopft den Filter. Das kann mit oder ohne Dieselpest auftreten. Prüfen Sie den Wasserabscheider und das Filterelement. Wenn schwarzer Schleim sichtbar ist → Dieselpest. Wenn klares Wasser → "nur" Kondensatwasser aufgewirbelt.

**F22: Weißer Rauch aus dem Auspuff bei Kälte — Kraftstoffproblem?**
A: Weißer Rauch bei Kaltstart ist normal (Wasserdampf). Wenn er anhält: Wasser im Diesel (milchiger Rauch) oder defekte Vorglühkerzen. Blau-weißer Rauch: unverdampfter Diesel (schlechte Kompression, defekte Düsen). Prüfen Sie den Wasserabscheider auf Wassergehalt.

**F23: Mein Racor-Vorfilter hat kein Vacuum-Manometer — soll ich eins nachrüsten?**
A: Unbedingt empfohlen! Das Vacuometer (z.B. Racor RK11-1567) zeigt den Zustand des Filterelements an: Grün = OK, Gelb = bald wechseln, Rot = sofort wechseln. Kosten: ca. 25–40 EUR. Nachrüstung einfach: in den vorhandenen Anschluss am Filterdeckel schrauben.

**F24: Kann ich den Kraftstoff selbst testen, ohne Labor?**
A: Ja, es gibt mehrere Vor-Ort-Tests: (1) FUELSTAT-Schnelltest für mikrobielle Kontamination (15 min, ~30 EUR). (2) Calcium-Hydrid-Wassertest (10 min, ~8 EUR). (3) Wassererkennungspaste am Peilstab (sofort, ~0,30 EUR/Test). (4) Optische Beurteilung in klarem Glas (kostenlos, aber weniger zuverlässig).

### 8.6 Spezialfragen

**F25: Ist HVO-Diesel (Neste MY) besser für mein Boot als normaler Diesel?**
A: In fast allen Belangen ja. HVO hat bessere Lagerstabilität, geringere Wasseraufnahme, höhere Cetanzahl, geringeres Dieselpest-Risiko und ist geruchsärmer. Nachteile: höherer Preis (ca. +15–25 ct/l), geringere Verfügbarkeit, leicht niedrigerer Energiegehalt (-1 bis -2 %). Alle modernen Dieselmotoren sind HVO-tauglich (EN 15940).

**F26: Kann ich Diesel und HVO mischen?**
A: Ja, unproblematisch. HVO ist in jedem Verhältnis mit fossilem Diesel (EN 590) mischbar. Keine Verträglichkeitsprobleme.

**F27: Mein Aluminium-Tank hat innen schwarze Flecken — ist das Dieselpest?**
A: Möglicherweise, aber es kann auch Aluminium-Korrosion sein. Dieselpest-Biofilm auf Aluminium beschleunigt die Korrosion dramatisch (mikrobiell induzierte Korrosion, MIC). Schwarze Flecken können sowohl Biofilm als auch Korrosionsprodukte (Aluminiumoxid/-sulfid) sein. Empfehlung: Professionelle Inspektion mit Wandstärkenmessung (Ultraschall) + FUELSTAT-Test.

**F28: Gibt es eine Möglichkeit, Dieselpest dauerhaft zu verhindern?**
A: 100 % dauerhaft verhindern: nein, solange Wasser in den Tank gelangen kann. Aber das Risiko auf nahe Null reduzieren: (1) Tank immer voll halten bei Stillstand. (2) Tankbelüftung mit Feuchtigkeitsfilter/Trockner. (3) Regelmäßige Biozid-Prophylaxe. (4) Fest installiertes Fuel Polishing (bei Langfahrtyachten). (5) HVO statt B7-Diesel verwenden.

**F29: Was kostet eine professionelle Tankreinigung?**
A: Richtwerte (DACH, 2025): Kleiner Tank (100–200 L): 500–1.000 EUR. Mittlerer Tank (200–500 L): 800–1.800 EUR. Großer Tank (500–2.000 L): 1.500–3.500 EUR. Inklusive: Absaugen, mechanische Reinigung, Spülung, Biozid-Behandlung, Fuel Polishing. Exklusive: frischer Diesel zum Auffüllen.

**F30: Muss ich nach einem Biozid-Einsatz die Filter häufiger wechseln?**
A: Ja! Nach einer Stoßbehandlung setzen sich die abgetöteten Mikroorganismen im Filter fest. Rechnen Sie damit, den Vorfilter 48–72 h nach der Behandlung wechseln zu müssen. Bei schwerer Kontamination möglicherweise 2–3 Filterwechsel in den ersten 2 Wochen.

### 8.7 Erweiterte Praxisfragen

**F31: Wie lagere ich Biozid (Grotamar 82) an Bord korrekt?**
A: Grotamar 82 enthält MBT gelöst in einem Lösungsmittelgemisch. Lagerung: stehend, original verschlossen, vor Sonnenlicht geschützt, Temperaturbereich 5–30 °C. Nicht neben Lebensmitteln oder Trinkwasser lagern. Haltbarkeit ungeöffnet: 24 Monate. Nach Anbruch: 12 Monate. Bei Eiskristallbildung (unter 0 °C): Auf Raumtemperatur erwärmen und schütteln — Wirksamkeit bleibt erhalten.

**F32: Kann ich den Diesel im Tank durch einfaches Nachfüllen "auffrischen"?**
A: Teilweise. Frischer Diesel verdünnt die Oxidationsprodukte und senkt den Wasseranteil prozentual. Aber: Wenn mikrobielle Kontamination vorhanden ist, reicht Nachfüllen nicht — die Organismen wachsen im frischen Diesel weiter. Faustregel: Wenn >50 % des Tankinhalts frischer Diesel ist, verbessert sich die Situation spürbar. Bei Dieselpest: Kein Ersatz für Biozid!

**F33: Was bedeutet der Code auf meinem Racor-Filterelement (z.B. 2010TM-OR)?**
A: Die Racor-Nomenklatur: 2010 = Modellreihe (Turbine 200-Serie). T = Turbine-Element. M = Marine. Die Zahl nach dem Schrägstrich oder am Ende kodiert die Filterfeinheit (siehe Farbcode): -OR = mit O-Ring. Die Endkappenfarbe zeigt die Filterfeinheit: Braun = 2 µm, Blau = 10 µm, Rot = 30 µm.

**F34: Mein Boot hat keinen Racor-Vorfilter — brauche ich einen?**
A: Dringend empfohlen! Einige Bootshersteller liefern ab Werk nur den Motor-Primärfilter. Ein separater Vorfilter mit Wasserabscheider bietet: (1) Schutz des teureren Motor-Filtersystems, (2) Wasserabscheidung (der Motor-Filter kann das meist nicht), (3) Sichtglas zur visuellen Kontrolle, (4) Leichtere Wartung (Vorfilter ist zugänglicher als Motor-Filter). Einbau: Zwischen Tank-Absperrventil und Motor, möglichst niedrig (Schwerkraft-Wasserabscheidung).

**F35: Gibt es Alternativen zum Racor-System?**
A: Ja. Separ (Stanadyne) bietet Schwerkraft-Wasserabscheider ohne Filterelement (SWK-2000-Serie) — robust und wartungsarm, aber gröbere Filtration. Delphi (früher CAV/Lucas) hat OEM-Wasserabscheider für viele europäische Motoren. Vetus hat eigene Vorfilter (WS-Serie) — kompakt, gut für kleine Motorräume. Griffin (Parker) bietet Koaleszenz-Abscheider für größere Systeme.

**F36: Wie entlüfte ich das Kraftstoffsystem nach einem Filterwechsel richtig?**
A: Die Methode hängt vom Motor ab. Grundprinzip: (1) Neuen Filter vor Einbau mit sauberem Diesel füllen (reduziert Luftmenge). (2) Filter einbauen, O-Ring einfetten (Diesel, nicht Silikon!). (3) Handentlüftungspumpe am Motor betätigen (wenn vorhanden): pumpen bis Diesel blasenfrei aus der Entlüftungsschraube austritt. (4) Entlüftungsschraube schließen. (5) Startversuch — Motor sollte nach max. 15 Sekunden anspringen. Bei Common-Rail-Motoren: Viele haben eine elektrische Entlüftungspumpe — Zündung einschalten und 30–60 Sekunden warten, bevor der Startversuch erfolgt.

**F37: Warum hat mein Motor nach dem Winterlager schwarzen Auspuffrauch?**
A: Schwarzer Rauch = unvollständige Verbrennung = zu viel Kraftstoff oder zu wenig Luft. Nach dem Winterlager typische Ursachen: (1) Verkokte Einspritzdüsen (Kraftstoff-Rückstände ausgehärtet), (2) Zugesetzter Luftfilter (Feuchtigkeit, Schimmel, Insekten), (3) Gealterter Diesel mit schlechter Zündwilligkeit. Der schwarze Rauch sollte nach 30–60 Minuten Betrieb nachlassen. Wenn nicht: Luftfilter und Einspritzdüsen prüfen lassen.

**F38: Ist ein Duplex-Filtersystem (zwei Filter parallel) sinnvoll?**
A: Für alle Boote, die weite Strecken fahren oder gewerblich genutzt werden: absolut empfehlenswert. Ein Duplex-System (z.B. Racor 75/B32) erlaubt den Wechsel auf den Reservefilter OHNE Motorstopp. Auf See, bei Seegang und Dieselpest ist das eine Sicherheitsreserve, die Maschinenausfall verhindert. Für Charterflotten und Blauwassersegler fast schon Pflicht. Für Wochenendsegler im Küstenbereich: Nice to have, aber kein Muss.

**F39: Wie erkenne ich, ob mein Tankfüllstandsensor (kapazitiv/resistiv) falsch misst?**
A: Vergleichsmethode: (1) Tank leer fahren (Motor läuft bis Stillstand → Tank wirklich leer). (2) Tanken mit genauer Literzahl (Quittung). (3) Vergleich Anzeige vs. getankter Menge vs. Tanknennvolumen. Wenn Abweichung >10 %: Sensor defekt oder falsch kalibriert. Bei kapazitiven Sensoren: Biodiesel (FAME) verändert die Dielektrizitätskonstante → Sensor zeigt zu viel an. Rekalibrierung nötig.

**F40: Was kostet es, ein Fuel Polishing System nachzurüsten?**
A: Richtwerte Nachrüstung inkl. Einbau: Kleines System (KTI FPS-1, bis 200 L): 1.800–2.500 EUR. Mittleres System (KTI FPS-2, bis 500 L): 2.800–3.800 EUR. Großes System (KTI FPS-3, bis 2.000 L): 4.500–6.500 EUR. Einbau dauert 4–8 Stunden (Fachbetrieb). Benötigt: dedizierte Tankanschlüsse (Entnahme + Rücklauf), Stromversorgung (12V oder 24V DC, 3–8 A), Platz ca. 30×20×25 cm (kleines System).

---

## 9. Glossar

### 9.1 Begriffe A–D

| Begriff | Erklärung |
|---------|-----------|
| **ABYC** | American Boat and Yacht Council — US-amerikanische Norm für Bootsausrüstung |
| **Asphaltene** | Hochmolekulare, dunkle Kohlenwasserstoffe im Diesel, die bei Alterung ausfallen und Ablagerungen bilden |
| **B7 / B20 / B100** | Biodiesel-Anteile: B7 = 7 % FAME + 93 % fossiler Diesel; B20 = 20 %; B100 = reiner Biodiesel |
| **Biofilm** | Schleimige, festhaftende Schicht aus Mikroorganismen und deren Stoffwechselprodukten auf Oberflächen |
| **Biozid** | Chemischer Wirkstoff, der Mikroorganismen abtötet oder deren Wachstum hemmt |
| **BPR** | Biozidprodukteverordnung (EU) 528/2012 — regelt Zulassung von Biozidprodukten in der EU |
| **CFPP** | Cold Filter Plugging Point — Temperatur, bei der Paraffinkristalle den Kraftstofffilter verstopfen |
| **CE-Kategorie** | Einteilung von Sportbooten nach Seetüchtigkeit (A=Hochsee, B=Küste, C=Küstennah, D=Geschützt) |
| **Cetanzahl** | Maß für die Zündwilligkeit von Dieselkraftstoff (je höher, desto besser). Minimum EN 590: 51 |
| **Common-Rail** | Hochdruck-Einspritzsystem für Dieselmotoren mit gemeinsamer Druckleitung (Rail) für alle Zylinder |
| **Desulfovibrio** | Gattung sulfatreduzierender Bakterien, die anaerob unter Biofilmen wachsen und aggressive Korrosion verursachen |
| **Dieselpest** | Umgangssprachlich für mikrobielle Kontamination des Kraftstoffsystems durch Pilze, Hefen und Bakterien |

### 9.2 Begriffe E–K

| Begriff | Erklärung |
|---------|-----------|
| **EN 590** | Europäische Norm für Dieselkraftstoff (Automotive Diesel Fuel), definiert Mindestanforderungen |
| **EN 15940** | Europäische Norm für paraffinische Dieselkraftstoffe (HVO, GTL) |
| **Entlüften** | Vorgang, bei dem Luft aus dem Kraftstoffsystem entfernt wird (nach Filterwechsel, Tankentleerung) |
| **FAME** | Fatty Acid Methyl Ester — chemische Bezeichnung für Biodiesel (Fettsäuremethylester) |
| **FCU** | Fuel Conditioning Unit — Magnetfeld-basiertes System zur Kraftstoff-Konditionierung (Algae-X) |
| **Fließverbesserer** | Additiv, das die Kälte-Eigenschaften von Diesel verbessert (senkt CFPP-Temperatur) |
| **Fuel Polishing** | Rezirkulation des Tankinhalts durch Mehrstufen-Filtersystem zur Reinigung und Wasserentfernung |
| **FUELSTAT** | Immunoassay-Schnelltest zur Erkennung mikrobieller Kontamination in Kraftstoff (Hersteller: Conidia) |
| **Gum & Lacquer** | Gummiartige und lackartige Ablagerungen aus polymerisierten Oxidationsprodukten des Diesels |
| **H₂S** | Schwefelwasserstoff — giftiges Gas mit Geruch nach faulen Eiern, produziert von SRB |
| **HFRR** | High Frequency Reciprocating Rig — Testverfahren zur Bestimmung der Schmierfähigkeit von Diesel |
| **Hormoconis resinae** | Häufigster Pilz in kontaminierten Kraftstoffsystemen, bildet schwarze Biofilme |
| **HVO** | Hydrotreated Vegetable Oil — hydriertes Pflanzenöl, paraffinischer Diesel nach EN 15940 |
| **ISO 21487** | Norm für Kraftstoff-Einfüllsysteme an kleinen Wasserfahrzeugen |
| **KBE/ml** | Kolonie-bildende Einheiten pro Milliliter — Maß für mikrobielle Konzentration |
| **Koaleszenzer** | Filterelement, das kleine Wassertröpfchen zu großen Tropfen vereinigt (Koaleszenz = Zusammenfließen) |

### 9.3 Begriffe L–R

| Begriff | Erklärung |
|---------|-----------|
| **MBT** | Methylen-bis(thiocyanat) — Biozid-Wirkstoff in Grotamar 82 |
| **MIC** | Microbially Induced Corrosion — mikrobiell induzierte Korrosion, besonders bei Aluminium-Tanks |
| **Mycel** | Geflecht aus Pilzfäden (Hyphen), kann Metallteile und Dichtungen durchdringen |
| **Osmose** | Im Yachtbau: Durchdringung von Wasser durch GFK-Laminat, hier: Wasseraufnahme in GFK-Tanks |
| **Paraffin** | Langkettige Kohlenwasserstoffe im Diesel, die bei Kälte auskristallisieren (Ausflockung) |
| **Peiltab** | Messstab zur manuellen Bestimmung des Tankfüllstands |
| **ppm** | Parts per million — Konzentrationsangabe (1 ppm = 1 mg/kg) |
| **Primärfilter** | Feinfilterelement am Motor (typisch 10 µm), Schutz der Einspritzanlage |
| **Pseudomonas** | Bakteriengattung, die in Kraftstoffsystemen vorkommt und starke Biofilme bildet |
| **Racor** | Marke von Parker Hannifin, Weltmarktführer für marine Kraftstoff-Vorfilter |
| **Rail** | Gemeinsame Hochdruck-Verteilerleitung im Common-Rail-Einspritzsystem |
| **Rancimat** | Testmethode zur Bestimmung der Oxidationsstabilität von Diesel (EN 14112) |

### 9.4 Begriffe S–Z

| Begriff | Erklärung |
|---------|-----------|
| **Schwallwand** | Trennwand im Tank, die das Schwappen des Kraftstoffs bei Seegang reduziert |
| **Schwanenhals** | S-förmige Rohrführung an der Tankbelüftung, verhindert Wassereintritt |
| **Sediment** | Feste Ablagerungen am Tankboden (Rost, Schmutz, oxidierte Diesel-Rückstände, Biomasse) |
| **Sekundärfilter** | Feinst-Filterelement (2–5 µm) vor dem Common-Rail-System |
| **SRB** | Sulfate-Reducing Bacteria — sulfatreduzierende Bakterien, verursachen MIC und H₂S |
| **Stabilisator** | Additiv, das die chemische Alterung (Oxidation) von Diesel verlangsamt |
| **Stoßbehandlung** | Einmalige Biozid-Gabe in erhöhter Dosis zur Abtötung einer aktiven Kontamination |
| **TAN** | Total Acid Number — Gesamtsäurezahl, Maß für den Säuregehalt des Kraftstoffs |
| **Turbine-Filter** | Racor-Filtertechnik: Kraftstoff wird in Rotation versetzt, Zentrifugalkraft trennt Wasser ab |
| **Vacuometer** | Unterdruckmessgerät am Vorfilter, zeigt den Verschmutzungsgrad des Filterelements an |
| **Vorfilter** | Erste Filterstufe zwischen Tank und Motor, typisch mit Wasserabscheider kombiniert |
| **Wasserabscheider** | Filterstufe, die freies Wasser aus dem Diesel abtrennt (durch Koaleszenz oder Schwerkraft) |
| **Wassererkennungspaste** | Chemische Paste, die bei Kontakt mit Wasser die Farbe wechselt (z.B. Kolor Kut) |
| **Yarrowia lipolytica** | Hefe, die besonders effektiv Biodiesel (FAME) abbaut |

### 9.5 Begriffe — Ergänzungen

| Begriff | Erklärung |
|---------|-----------|
| **Aquazole** | Diesel-Wasser-Emulsion — absichtliche Wasserbeimischung zur Reduktion von NOx-Emissionen (nicht relevant für Sportboote) |
| **Aseptisch** | Keimfrei — Zustand, der bei Kraftstoffsystemen praktisch nicht erreichbar ist, aber als Ziel der Tankreinigung gilt |
| **Cloud Point** | Trübungspunkt — Temperatur, bei der erste Paraffinkristalle sichtbar werden (ca. 3–5 °C über CFPP) |
| **Deemulgierung** | Trennung einer Emulsion in ihre Bestandteile — Aufgabe des Koaleszenzers im Wasserabscheider |
| **Dienstleistungskreislauf** | Zyklus aus Vorsorge → Diagnose → Behandlung → Kontrolle → Vorsorge im Kraftstoffsystem |
| **Druckdifferenz** | Druckunterschied vor und nach einem Filter — Maß für den Verschmutzungsgrad (gemessen mit Vacuometer) |
| **Emulsion** | Fein verteilte Mischung zweier nicht mischbarer Flüssigkeiten (Diesel + Wasser) — milchiges Erscheinungsbild |
| **Flashpoint** | Flammpunkt — niedrigste Temperatur, bei der sich Kraftstoffdämpfe entzünden lassen (Diesel: ≥55 °C, ISO 9094) |
| **Galvanische Korrosion** | Elektrochemische Korrosion bei Kontakt unterschiedlicher Metalle im Kraftstoffsystem (z.B. Aluminium-Tank + Kupfer-Leitung) |
| **Heizwert** | Energiegehalt des Kraftstoffs: Diesel ~35,8 MJ/L, HVO ~34,4 MJ/L, Biodiesel B100 ~32,8 MJ/L |
| **Inline-Filter** | Filter, der direkt in die Kraftstoffleitung eingebaut ist (im Gegensatz zu abzweigenden Systemen) |
| **Kavitation** | Bildung und Zusammenfall von Dampfblasen in Flüssigkeiten — kann in Kraftstoff-Förderpumpen auftreten bei verstopftem Ansaugfilter |
| **Leckrate** | Volumenstrom einer Undichtigkeit — bei Kraftstoffsystemen kritisch ab >1 Tropfen/min |
| **Lubricity** | Schmierfähigkeit — wichtig für Einspritzpumpen, gemessen als HFRR-Wert (max. 460 µm für EN 590) |
| **Niederdruckseite** | Teil des Kraftstoffsystems zwischen Tank und Einspritzpumpe (0–4 bar) — hier sitzen Vorfilter und Primärfilter |
| **Hochdruckseite** | Teil des Kraftstoffsystems ab Einspritzpumpe (200–2.500 bar bei Common-Rail) — nur Werkstatt-Service |
| **OBD** | On-Board-Diagnose — elektronisches Diagnosesystem moderner Motoren, zeigt Fehlercode bei Kraftstoffproblemen |
| **Pour Point** | Stockpunkt — Temperatur, bei der Diesel nicht mehr fließt (ca. 5–10 °C unter CFPP) |
| **Priming** | Befüllen des Kraftstoffsystems vor dem Erststart oder nach Filterwechsel — meist über Handentlüftungspumpe |
| **Rezirkulation** | Rückführung von Kraftstoff über die Rücklaufleitung in den Tank — bei Diesel: 30–70 % des geförderten Volumens |
| **Stratifikation** | Schichtbildung im Tank: leichter Diesel oben, schweres Wasser + Sediment unten — verstärkt durch Stillstand |
| **Thermosiphon** | Natürliche Konvektion in Flüssigkeiten durch Temperaturunterschiede — kann im Tank zu Wasserverteilung führen |
| **Venturi-Effekt** | Druckabfall an Verengungen — kann in Kraftstoffleitungen Luftblasen ansaugen bei Undichtigkeit |

---

## 10. Schnell-Referenz

### 10.1 Wartungsintervalle — Kurzübersicht

```
MONATLICH (Saison):
  □ Wasserabscheider prüfen und entleeren
  □ Kraftstoffprobe optisch beurteilen
  □ Leitungen auf Feuchtigkeit prüfen
  □ Bilge auf Dieselgeruch prüfen

HALBJÄHRLICH:
  □ Vorfilter prüfen, ggf. wechseln
  □ FUELSTAT-Schnelltest
  □ Tankbelüftung prüfen
  □ Schlauchschellen nachziehen

JÄHRLICH:
  □ Vorfilter wechseln (unbedingt)
  □ Primärfilter wechseln
  □ Kraftstoff Laboranalyse
  □ Tankinspektion (visuell/endoskopisch)
  □ Kraftstoffleitungen prüfen

WINTERFESTMACHUNG:
  □ Tank VOLL füllen
  □ Biozid + Stabilisator zugeben
  □ Motor 20 min laufen lassen
  □ Alle Filter wechseln
  □ Wasserabscheider entleeren
```

### 10.2 Dosierungstabelle — Grotamar 82

| Tankvolumen | Prophylaxe (100 ppm) | Stoßdosis (200 ppm) | Max. Dosis (500 ppm) |
|-------------|---------------------|---------------------|---------------------|
| 50 L | 5 ml | 10 ml | 25 ml |
| 100 L | 10 ml | 20 ml | 50 ml |
| 200 L | 20 ml | 40 ml | 100 ml |
| 300 L | 30 ml | 60 ml | 150 ml |
| 500 L | 50 ml | 100 ml | 250 ml |
| 1.000 L | 100 ml | 200 ml | 500 ml |

### 10.3 Notfall-Checkliste — Motor stoppt auf See

```
1. RUHE BEWAHREN — Segel setzen oder Anker werfen
2. Absperrventil prüfen → OFFEN?
3. Wasserabscheider prüfen → WASSER? → Ablassen
4. Vorfilter prüfen → ZUGESETZT? → Wechseln (Ersatzfilter!)
5. System entlüften → Handpumpe betätigen
6. Neustart versuchen
7. Motor läuft? → Langsame Fahrt zum Hafen
8. Motor läuft nicht? → Professionelle Hilfe / Abschleppen
```

### 10.4 Biozid-Entscheidungsmatrix — Schnellwahl

```
Szenario bestimmen:
  │
  ├── Prophylaxe (kein Befund)?
  │   ├── Ostsee/Nordsee → Grotamar 82, jede 3. Tankfüllung (100 ppm)
  │   ├── Mittelmeer → Grotamar 82, jede 2. Tankfüllung (100 ppm)
  │   ├── Tropen/Blauwasser → Grotamar 82, jede Tankfüllung (100 ppm)
  │   └── Alternative: Marine 16 (Kombiprodukt, einfacher)
  │
  ├── Leichte Kontamination (Stadium 1)?
  │   → Grotamar 82 Stoßdosis (200 ppm) + Fuel Polishing empfohlen
  │
  ├── Mittlere Kontamination (Stadium 2)?
  │   → Grotamar 82 Stoßdosis (200–250 ppm) + Fuel Polishing PFLICHT
  │   → Filterwechsel nach 48 h
  │
  └── Schwere Kontamination (Stadium 3)?
      → Tankreinigung + Leitungsspülung + Grotamar 82 (250–500 ppm)
      → Fuel Polishing (5–8 Zyklen) + alle Filter neu
      → Professionellen Fachbetrieb empfohlen
```

### 10.5 Winterfestmachung — Kurzprotokoll

```
STANDARD (6 Monate Stillstand):
  1. □ Tank VOLL füllen (>95 %)
  2. □ Grotamar 82: 10 ml pro 100 L zugeben
  3. □ Stabilisator: 100 ml pro 100 L zugeben
  4. □ Motor 20 min unter Last laufen lassen
  5. □ Wasserabscheider entleeren
  6. □ Vorfilter wechseln
  7. □ Primärfilter wechseln
  8. □ Absperrventil schließen
  9. □ Tankbelüftung auf Durchgängigkeit prüfen
  10. □ Einfüllstutzen-Deckel dicht verschließen
  11. □ Bilge trockenlegen

ERWEITERT (12+ Monate Stillstand):
  Wie Standard, zusätzlich:
  12. □ Fuel Polishing vor Einlagerung
  13. □ Doppelte Biozid- und Stabilisator-Dosis
  14. □ Alle 6 Monate: Stabilisator nachfüllen
  15. □ Alle 3 Monate: Wasserabscheider prüfen
  16. □ Einspritzdüsen konservieren (Herstelleranleitung)
  17. □ Vor Wiederinbetriebnahme: Kraftstoff-Laboranalyse
```

### 10.6 Diagnosematrix — Symptom → Wahrscheinlichste Ursache

| Symptom | Wahrscheinlichste Ursache(n) | Erste Maßnahme |
|---------|------------------------------|----------------|
| Motor startet nicht | Filter verstopft, Luft im System, Absperrventil zu | Filter + Absperrventil prüfen |
| Motor stottert unter Last | Wasser im Diesel, Filter teilweise verstopft | Wasserabscheider entleeren |
| Motor stottert bei Seegang | Sediment/Wasser aufgewirbelt, Tank <25 % | Tanken, Filter wechseln |
| Schwarzer Rauch | Verkokte Düsen, Luftfilter zu, schlechter Diesel | Luftfilter prüfen, Injektorreiniger |
| Weißer Rauch (anhaltend) | Wasser im Diesel, defekte Vorglühkerze | Wasserabscheider prüfen |
| Leistungsverlust schleichend | Filter sättigt sich, Düsen verkokt | Filter wechseln, Verbrauch prüfen |
| Dieselgeruch im Boot | Leck in Leitung/Filter/Tank, Belüftung falsch | Lecksuche, Bilge prüfen |
| Erhöhter Verbrauch | Bewuchs, Filter, Düsen, Propeller, Trim | Systematische Prüfung |
| Filter verstopft schnell | Dieselpest, Sediment, Paraffin | FUELSTAT-Test, Kraftstoff prüfen |
| Schwarzer Schleim im Filter | Dieselpest aktiv | Biozid + Fuel Polishing |
| Motor geht bei Kälte aus | Paraffin-Ausflockung | Filter wechseln, Motorraum wärmen |
| Tankfüllstandsanzeige falsch | Sensor defekt/verklebt, Kabel korrodiert | Manuelle Peilung, Sensor prüfen |

### 10.7 Kraftstoff-Haltbarkeit — Schnellübersicht

| Kraftstoff | Ohne Additiv | Mit Stabilisator | Mit Stabilisator + Biozid |
|-----------|-------------|-------------------|---------------------------|
| Diesel B0 | 12–18 Monate | 18–30 Monate | 24–36 Monate |
| Diesel B7 | 6–12 Monate | 12–18 Monate | 18–24 Monate |
| Diesel B20 | 3–6 Monate | 6–12 Monate | 12–18 Monate |
| HVO (EN 15940) | 18–36 Monate | 30–48 Monate | 36–48+ Monate |

**Voraussetzung:** Voller Tank, minimaler Luftraum, Umgebungstemperatur <25 °C.

### 10.8 Kosten-Übersicht — Typische Wartungs- und Reparaturkosten

| Maßnahme | Kosten (ca.) | Intervall |
|----------|-------------|-----------|
| Racor-Filterelement (10 µm) | 12–18 EUR | Jährlich / 200 h |
| Motor-Primärfilter (OEM) | 15–45 EUR | Jährlich / 250 h |
| Grotamar 82 (100 ml) | 18–25 EUR | Reicht für ~1.000 L Diesel |
| Fuel Set Diesel Kleen (250 ml) | 12–16 EUR | Reicht für ~250 L Diesel |
| FUELSTAT-Schnelltest | 25–35 EUR | Halbjährlich |
| Kraftstoff-Laboranalyse (Basis) | 45–80 EUR | Jährlich |
| Fuel Polishing (mobiler Service) | 250–600 EUR | Bei Bedarf |
| Fuel Polishing System (fest) | 1.500–6.000 EUR | Einmal-Investition |
| Professionelle Tankreinigung | 500–3.500 EUR | Bei Kontamination |
| Einspritzdüse (1 Stück, OEM) | 100–400 EUR | Alle 1.000–2.000 h |
| Einspritzpumpe-Überholung | 800–2.500 EUR | Alle 2.000–3.000 h |
| Common-Rail-Hochdruckpumpe | 2.000–5.000 EUR | Alle 5.000+ h |

---

## 11. Anhänge A–H — Fallstudien

### ANHANG A — Fallstudie: Bavaria 37 Cruiser — Dieselpest nach Winterlager

**Boot:** Bavaria 37 Cruiser, Baujahr 2018, Volvo Penta D2-40
**Eigner:** Saisonsegler, Ostsee (Kiel), April–Oktober
**Problem:** Motor startet nach Winterlager (November–März) nicht, schwarzer Schleim im Racor-Filter

**Chronologie:**
1. November 2024: Einwintern. Tank ca. 40 % (Fehler!). Kein Biozid, kein Stabilisator.
2. März 2025: Auswassern, Motor starten → dreht, zündet nicht.
3. Vorfilter-Inspektion: Schwarze, geleearttige Masse auf Filterelement. Wasserabscheider-Glas: trübes, dunkles Wasser mit Schlieren.
4. FUELSTAT-Test: "Sehr schwer" — Stadium 3 Dieselpest.

**Diagnose:** Hormoconis resinae + Pseudomonas (durch Labortest bestätigt). Ursache: halbleerer Tank → massive Kondensation über Winter → 800+ ml Wasser am Tankboden → optimale Wachstumsbedingungen.

**Sanierung:**
1. Tank komplett entleert (180 L Diesel + 2,5 L Wasser-Schleim-Gemisch abgepumpt)
2. Tank über Inspektionsöffnung mechanisch gereinigt (Biofilm an Wänden!)
3. Alle Leitungen gespült
4. Racor-Filter: neues Element, Gehäuse gereinigt
5. Motor-Primärfilter und Sekundärfilter gewechselt
6. Einspritzdüsen ausgebaut und im Ultraschallbad gereinigt (Werkstatt)
7. Tank mit frischem Diesel gefüllt + Grotamar 82 (250 ppm Stoßdosis)
8. Fuel Polishing: 5 Zyklen über 2 Tage
9. FUELSTAT-Kontrolltest nach 10 Tagen: "Negativ"

**Kosten:**
- Tankreinigung (Fachbetrieb): 1.200 EUR
- Filterwechsel (Racor + Motor): 85 EUR
- Düsenreinigung: 320 EUR
- Diesel (200 L): 360 EUR
- Biozid + Polishing: 180 EUR
- **Gesamt: 2.145 EUR**

**Lehre:** Tank VOR dem Einwintern voll füllen + Biozid + Stabilisator. Geschätzte Kosten der Prävention: 45 EUR.

### ANHANG B — Fallstudie: Hallberg-Rassy 40 — Leistungsverlust bei Seegang auf Atlantiküberquerung

**Boot:** Hallberg-Rassy 40 MkII, Baujahr 2015, Volvo Penta D2-75
**Eigner:** Blauwassersegler, Atlantiküberquerung Gran Canaria → Martinique
**Problem:** Ab Tag 3 zunehmender Leistungsverlust unter Motor, Filter verstopfen alle 8–12 Stunden

**Chronologie:**
1. Gran Canaria: Tanken (500 L, lokale Tankstelle). Kein Fuel Polishing vor Abfahrt.
2. Tag 1–2: Segeln, Motor nur zum Laden (1 h/Tag). Keine Probleme.
3. Tag 3: Flaute, Motor über 10 h. Bei Dünung (2–3 m): Motor stottert, Leistungsverlust.
4. Racor-Filter: dunkelbraunes, trübes Filtrat, schnell zugesetzt.
5. Tag 3–8: 6 Filterwechsel nötig (Ersatzfilter-Vorrat wird knapp!).
6. Tag 9: Provisorische Lösung: Racor auf 30 µm (statt 10 µm) umgerüstet → mehr Durchsatz, aber weniger Schutz.

**Diagnose:** Sediment und beginnendes Dieselpest-Stadium 2. Der auf Gran Canaria getankte Diesel war bereits leicht kontaminiert. Der Seegang hat das Sediment vom Tankboden aufgewirbelt.

**Maßnahmen auf See:**
1. Racor auf 30 µm umgerüstet (Notmaßnahme — schlechtere Filtration, aber längere Standzeit)
2. Grotamar 82 Stoßdosis (200 ppm) in Tank
3. Wasserabscheider alle 4 h entleert
4. Geschwindigkeit reduziert (weniger Verbrauch → weniger Durchfluss → weniger Filterlast)

**Maßnahmen in Martinique:**
1. Tank entleert, professionelle Tankreinigung
2. Neuer Diesel getankt (lokale Marken-Tankstelle)
3. Fuel Polishing System (KTI FPS-2) nachgerüstet
4. Grotamar 82 Prophylaxe-Regime eingeführt

**Kosten:**
- Filtersatz (12 Elemente, in Las Palmas vorsorglich gekauft): 180 EUR
- Tankreinigung Martinique: 600 USD
- KTI FPS-2 (Nachbestellung, Luftfracht): 2.800 EUR
- Grotamar 82 (1 L): 65 EUR
- **Gesamt: ca. 3.900 EUR**

**Lehre:** Vor Langfahrt IMMER Fuel Polishing durchführen. Ausreichend Ersatzfilter mitnehmen (Faustformel: 1 pro 500 Seemeilen). Fest installiertes Fuel Polishing System für Blauwassersegler zwingend empfohlen. Duplex-Filteranlage erwägen.

### ANHANG C — Fallstudie: Princess 56 — Paraffin-Ausflockung bei Herbstüberführung

**Boot:** Princess 56 Flybridge, Baujahr 2020, 2× Volvo Penta D11-700
**Eigner:** Motorboot-Eigner, Überführung Mallorca → Antibes → Monaco → Imperia → Genua (Oktober)
**Problem:** Bei Nachtfahrt Mallorca→Antibes (Außentemperatur sinkt auf -2 °C): beide Motoren sterben gleichzeitig ab

**Chronologie:**
1. Mallorca: Betankung mit Sommer-Diesel (CFPP ca. -3 °C)
2. Abfahrt 16:00, Außentemperatur 18 °C → kein Problem
3. 03:00: Außentemperatur 2 °C. Kraft auf 80 % → kein Problem
4. 05:00: Außentemperatur -2 °C. Motorraum nicht beheizt.
5. 05:30: Steuerbordmotor stottert, dann Ausfall. Backbordmotor 2 min später ebenso.
6. Racor-Filter: wachsartige, weiße Masse auf beiden Filterelementen.

**Diagnose:** Paraffin-Ausflockung. Sommer-Diesel aus Mallorca mit CFPP ~-3 °C bei -2 °C Außentemperatur und unbeheiztem Motorraum → Paraffinkristalle verstopfen Filter.

**Sofortmaßnahme auf See:**
1. Motorraum mit tragbarem Heizlüfter (230V Generator) aufwärmen
2. 45 min warten
3. Filter wechseln (Paraffin löst sich im warmen Motorraum, aber Filter bleibt verstopft)
4. System entlüften
5. Motoren starten → laufen
6. Motorraum-Heizung anlassen für Rest der Fahrt

**Nachmaßnahmen:**
1. Racor-Filterheizungen nachgerüstet (beide Motoren): 2× R58064
2. Fließverbesserer (LIQUI MOLY Diesel Fließ-Fit) an Bord als Standardausrüstung
3. Betriebsanweisung: Bei Herbst-/Winterüberführungen: Winterdiesel tanken oder Additiv VOR Fahrtantritt

**Kosten:**
- Filterelemente (4×, Sofortwechsel): 120 EUR
- Heizlüfter (an Bord): 0 EUR (vorhanden)
- Racor-Filterheizungen (2 Stk. + Einbau): 650 EUR
- Fließverbesserer (Vorrat): 35 EUR
- **Gesamt: 805 EUR**

**Lehre:** Bei Überführungen im Herbst/Winter: Kraftstofftemperatur im Auge behalten! Filterheizung für Boote, die im Winter bewegt werden, ist eine sinnvolle Investition. Fließverbesserer VOR dem Abkühlen zugeben — nachher wirkungslos!

### ANHANG D — Fallstudie: Jeanneau Sun Odyssey 440 — Tankbelüftung verstopft durch Insektennest

**Boot:** Jeanneau Sun Odyssey 440, Baujahr 2022, Yanmar 4JH57
**Liegeplatz:** Marina Portoroz, Slowenien
**Problem:** Beim Tanken läuft Diesel extrem langsam in den Tank (Gluckern), Motor stottert bei hoher Drehzahl

**Chronologie:**
1. Mai 2025: Saisonstart. Tanken dauert unverhältnismäßig lange (45 min für 100 L).
2. Erste Ausfahrt: Bei >2.500 U/min beginnt Motor zu stottern.
3. Mechaniker prüft Filtersystem → alles in Ordnung.
4. Vakuometer zeigt hohen Unterdruck trotz neuem Filter.
5. Verdacht: Tankbelüftung!
6. Belüftungsleitung geöffnet: Wespennest im Schwanenhals-Bogen (Überwinternde Wespenart).

**Diagnose:** Vollständig verstopfte Tankbelüftung. Tank bildet Unterdruck bei Kraftstoffentnahme → Förderpumpe kann nicht genug Diesel ansaugen → Motor verhungert bei hohem Verbrauch.

**Reparatur:**
1. Schwanenhals-Bogen ausgebaut, Insektennest entfernt
2. Belüftungsleitung durchgeblasen (Druckluft)
3. Insektenschutzgitter (Edelstahlgaze, 1 mm) am Belüftungsaustritt nachgerüstet
4. Funktionstest: Tanken und Motorlauf normal

**Kosten:**
- Mechaniker (1 h): 85 EUR
- Edelstahlgaze + Montage: 15 EUR
- **Gesamt: 100 EUR**

**Lehre:** Tankbelüftung vor Saisonstart IMMER prüfen (Durchblastest). Insektenschutzgitter an allen Belüftungsöffnungen nachrüsten. Bei Motoren, die bei hoher Drehzahl stottern: immer auch Tankbelüftung als Ursache in Betracht ziehen.

### ANHANG E — Fallstudie: Beneteau Oceanis 51.1 — Wassereinbruch über defekten Einfüllstutzen

**Boot:** Beneteau Oceanis 51.1, Baujahr 2019, Yanmar 4JH80
**Liegeplatz:** Heiligenhafen, Ostsee
**Problem:** Nach starkem Regen: Motor startet schwer, weißer Rauch, Wasserabscheider randvoll mit Wasser

**Chronologie:**
1. Juni 2025: 3 Tage Starkregen, Boot unbeaufsichtigt am Steg.
2. Samstag: Eigner will auslaufen. Motor dreht, startet nach 5 Versuchen.
3. Weißer Rauch aus Auspuff, Motor läuft unrund.
4. Wasserabscheider: Sichtglas komplett mit Wasser gefüllt.
5. Nach Ablassen: 800 ml Wasser! Tank enthält geschätzt 2–3 L Wasser.

**Diagnose:** Wasser über defekte O-Ring-Dichtung des Einfüllstutzens in den Tank eingedrungen. Der Einfüllstutzen sitzt in einer Decksmulde, die bei Regen volllaufen kann.

**Reparatur:**
1. Tank über Fuel Polishing System (mobiler Service) von Wasser befreit: 4,2 L Wasser entfernt
2. Einfüllstutzen-Dichtung (O-Ring) erneuert
3. Einfüllstutzen mit Sikaflex 291 abgedichtet (Deck-zu-Stutzen)
4. Biozid prophylaktisch zugegeben (Wasser = Dieselpest-Risiko)
5. FUELSTAT-Test nach 4 Wochen: negativ

**Kosten:**
- Fuel Polishing Service: 350 EUR
- O-Ring + Sikaflex: 25 EUR
- Grotamar 82: 20 EUR
- FUELSTAT: 30 EUR
- **Gesamt: 425 EUR**

**Lehre:** Einfüllstutzen-Dichtung jährlich prüfen! Besonders bei Booten, wo der Einfüllstutzen in einer Mulde oder Rinne sitzt, die Regenwasser sammelt. Einfacher Test: Wasser über den geschlossenen Einfüllstutzen gießen und von unten beobachten.

### ANHANG F — Fallstudie: Hanse 508 — Wiederholte Dieselpest trotz Biozid-Behandlung

**Boot:** Hanse 508, Baujahr 2021, Volvo Penta D3-150
**Eigner:** Charterboot-Betreiber, Kroatien (Split)
**Problem:** Alle 4–6 Wochen verstopfte Filter trotz regelmäßiger Biozid-Zugabe

**Chronologie:**
1. Saison 2024: 3× Filterwechsel wegen Dieselpest (bestätigt durch FUELSTAT)
2. Jedes Mal: Grotamar 82 Stoßdosis → Problem bessert sich → kehrt zurück
3. Oktober 2024: Tankreinigung → 2 Wochen gut → wieder Schleim im Filter
4. AYDI-Beratung angefordert

**Diagnose:** Systemische Ursache — Biofilm in den Leitungen und im Rücklaufstutzen blieb bei der Tankreinigung unbehandelt. Jede Behandlung tötet die Organismen im Tank, aber der Biofilm in den Leitungen reinfiziert den Tank innerhalb von 2–4 Wochen.

**Sanierung (AYDI-Empfehlung):**
1. Tank entleeren und professionell reinigen (wie bisher)
2. ZUSÄTZLICH: Alle Kraftstoffleitungen (Zulauf + Rücklauf) ausbauen und ersetzen
3. Racor-Filtergehäuse mit Essigessenz reinigen (biofilmlösend)
4. Rücklauf-Tankstutzen ausbauen und reinigen
5. Motor-Einspritzbereich: Rücklaufleitung am Motor ersetzen
6. Frischer Diesel + Grotamar 82 (500 ppm einmalige Maximaldosis)
7. Fuel Polishing (8 Zyklen)
8. Danach: Prophylaxe-Regime strikt einhalten

**Kosten:**
- Tankreinigung: 1.400 EUR
- Leitungstausch (komplett): 650 EUR
- Filterwechsel + Racor-Reinigung: 120 EUR
- Diesel + Biozid + Polishing: 480 EUR
- Arbeitszeit Mechaniker (8 h): 680 EUR
- **Gesamt: 3.330 EUR**

**Lehre:** Dieselpest ist ein Systemproblem, nicht nur ein Tankproblem! Die Sanierung muss ALLE Komponenten einschließen: Tank, Leitungen, Filter, Rücklauf. Sonst Reinfektionszyklus.

### ANHANG G — Fallstudie: Fountaine Pajot Elba 45 — Zwei Motoren, ein kontaminierter Tank

**Boot:** Fountaine Pajot Elba 45 (Katamaran), Baujahr 2023, 2× Volvo Penta D2-40
**Eigner:** Privat, Mittelmeer (Sardinien)
**Problem:** Steuerbordmotor: wiederholte Filterprobleme. Backbordmotor: einwandfrei.

**Chronologie:**
1. Beide Motoren werden aus separaten Tanks versorgt (Katamaran: je ein Tank pro Rumpf)
2. Steuerbord: Filter alle 50 h verstopft, Dieselpest bestätigt
3. Backbord: keine Probleme, FUELSTAT negativ
4. Eigner tankt immer an derselben Zapfsäule, gleiche Qualität in beide Tanks

**Diagnose:** Steuerbord-Tank hat Wassereintritt über einen undichten Decks-Fitting (ein Decksbeschlag wurde durch die Tankdecke montiert und die Dichtung war mangelhaft ab Werk). Backbord-Tank: kein Wassereintritt → kein Dieselpest.

**Reparatur:**
1. Undichten Decksbeschlag über Steuerbord-Tank abdichten (Sikaflex 291i)
2. Steuerbord-Tank: Komplettsanierung (Reinigung, Leitungen spülen, Biozid)
3. Backbord-Tank: Prophylaktisch Biozid zugeben

**Kosten:**
- Decksbeschlag-Abdichtung: 40 EUR
- Steuerbord-Tanksanierung: 1.800 EUR
- Biozid + Filter: 120 EUR
- **Gesamt: 1.960 EUR**

**Lehre:** Bei Katamaranen und Booten mit Mehrtanksystem: Wenn nur ein System betroffen ist → Ursache ist im betroffenen Tank/System zu suchen. Systematische Wasserquellensuche ist der Schlüssel.

### ANHANG H — Fallstudie: Nordhavn 47 — Langzeit-Einlagerung und Wiederinbetriebnahme nach 30 Monaten

**Boot:** Nordhavn 47, Baujahr 2012, John Deere 4045TFM75
**Eigner:** Privat, Niederlande
**Problem:** Boot stand 30 Monate still (COVID + gesundheitliche Gründe). Tank voll, Stabilisator zugegeben, kein Biozid.

**Chronologie:**
1. März 2022: Boot eingemottet. Tank voll (800 L). LIQUI MOLY Marine Diesel Schutz zugegeben.
2. September 2024: Wiederinbetriebnahme geplant.
3. Kraftstoffprobe: dunkelbraun, leicht trüb, muffiger Geruch.
4. Laboranalyse: TAN erhöht (0,8 mg KOH/g), Wassergehalt 680 ppm, Keimzahl 10⁴ KBE/ml.
5. Ergebnis: Kraftstoff stark gealtert, leichte mikrobielle Kontamination, zu hoher Wassergehalt.

**Maßnahmen:**
1. Fuel Polishing: 5 Zyklen (Wasserentfernung: 1,2 L, Sediment: erheblich)
2. Grotamar 82 Stoßdosis (200 ppm)
3. Erneute Laboranalyse nach Polishing: TAN 0,4 (besser, aber grenzwertig), Wasser 120 ppm (OK), Keime negativ
4. Entscheidung: 50 % des Tankinhalts (400 L) ablassen und durch frischen Diesel ersetzen
5. Erneutes Polishing: 3 Zyklen
6. Finale Laboranalyse: alle Werte im Grünen
7. Alle Filter gewechselt
8. Einspritzdüsen prüfen lassen (Werkstatt: OK, leichte Verkokung, Ultraschallreinigung)
9. Motor gestartet: läuft nach Entlüftung einwandfrei

**Kosten:**
- Fuel Polishing (mobiler Service, 2 Einsätze): 900 EUR
- Laboranalysen (3×): 280 EUR
- Diesel (400 L frisch): 640 EUR
- Entsorgung Altdiesel (400 L): 180 EUR
- Filter (Racor + Motor): 85 EUR
- Düsenreinigung: 240 EUR
- Grotamar + Stabilisator: 60 EUR
- **Gesamt: 2.385 EUR**

**Lehre:** Bei Langzeiteinlagerung >24 Monate: Tank entleeren ist oft günstiger als 30 Monate Diesel zu konservieren. Wenn Diesel im Tank bleibt: Biozid UND Stabilisator kombinieren, alle 6 Monate Stabilisator nachfüllen, alle 3 Monate Wasserabscheider prüfen. Vor Wiederinbetriebnahme: Laboranalyse PFLICHT.

---

## 12. Anhänge I–R — Pydantic v2 Modelle

### ANHANG I — Basismodelle Kraftstoffsystem

```python
"""
AYDI Fuel System Maintenance — Pydantic v2 Base Models
Module: 19_04_kraftstoffsystem_wartung

All models use Pydantic v2 with model_config = {"from_attributes": True}.
NEVER use class Config — this is a Pydantic v1 pattern.
"""

from __future__ import annotations

from datetime import date, datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, field_validator


# === Enums ===

class FuelType(str, Enum):
    """Kraftstofftyp."""
    DIESEL_B0 = "diesel_b0"
    DIESEL_B7 = "diesel_b7"
    DIESEL_B10 = "diesel_b10"
    DIESEL_B20 = "diesel_b20"
    DIESEL_B100 = "diesel_b100"
    HVO = "hvo"
    GTL = "gtl"
    HEATING_OIL = "heating_oil"
    UNKNOWN = "unknown"


class ContaminationStage(str, Enum):
    """Dieselpest-Stadium."""
    NONE = "none"
    STAGE_1_LATENT = "stage_1_latent"
    STAGE_2_ACTIVE = "stage_2_active"
    STAGE_3_MASSIVE = "stage_3_massive"


class FuelCondition(str, Enum):
    """Kraftstoffzustand nach visueller Beurteilung."""
    CLEAR_AMBER = "clear_amber"
    SLIGHTLY_DARK = "slightly_dark"
    CLOUDY_MILKY = "cloudy_milky"
    DARK_BROWN_CLEAR = "dark_brown_clear"
    DARK_BROWN_CLOUDY = "dark_brown_cloudy"
    BLACK_PARTICLES = "black_particles"
    BLACK_SLIME = "black_slime"
    WAXY_THICK = "waxy_thick"
    REDDISH = "reddish"
    HYDROGEN_SULFIDE_SMELL = "hydrogen_sulfide_smell"


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


class MaintenanceInterval(str, Enum):
    """Wartungsintervalltyp."""
    MONTHLY = "monthly"
    SEMI_ANNUAL = "semi_annual"
    ANNUAL = "annual"
    HOURS_50 = "hours_50"
    HOURS_100 = "hours_100"
    HOURS_200 = "hours_200"
    HOURS_250 = "hours_250"
    HOURS_500 = "hours_500"
    HOURS_1000 = "hours_1000"
    HOURS_2000 = "hours_2000"


class TankMaterial(str, Enum):
    """Tankmaterial."""
    ALUMINUM = "aluminum"
    STAINLESS_STEEL_316L = "stainless_steel_316l"
    MILD_STEEL = "mild_steel"
    GRP_FRP = "grp_frp"
    POLYETHYLENE = "polyethylene"
    UNKNOWN = "unknown"


class Urgency(str, Enum):
    """Dringlichkeit einer Maßnahme."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    VERY_HIGH = "very_high"
    CRITICAL = "critical"


# === Base Models ===

class FuelSample(BaseModel):
    """Kraftstoffprobe mit Analyseergebnissen."""

    model_config = {"from_attributes": True}

    sample_id: str = Field(..., description="Eindeutige Proben-ID")
    sample_date: datetime = Field(..., description="Zeitpunkt der Probenahme")
    source: str = Field(..., description="Entnahmestelle (z.B. 'Wasserabscheider', 'Tankboden')")
    visual_condition: FuelCondition = Field(..., description="Visuelle Beurteilung")
    water_content_ppm: Optional[float] = Field(None, ge=0, le=50000, description="Wassergehalt in ppm")
    total_contamination_mg_kg: Optional[float] = Field(None, ge=0, description="Gesamtverschmutzung mg/kg")
    cetane_number: Optional[float] = Field(None, ge=30, le=100, description="Cetanzahl")
    density_kg_m3: Optional[float] = Field(None, ge=750, le=900, description="Dichte bei 15°C in kg/m³")
    total_acid_number: Optional[float] = Field(None, ge=0, description="Gesamtsäurezahl (TAN) mg KOH/g")
    cfpp_celsius: Optional[float] = Field(None, ge=-60, le=10, description="CFPP in °C")
    fame_percent: Optional[float] = Field(None, ge=0, le=100, description="FAME-Anteil in %")
    microbial_cfu_per_ml: Optional[float] = Field(None, ge=0, description="Keimzahl KBE/ml")
    fuelstat_result: Optional[str] = Field(None, description="FUELSTAT-Ergebnis: negativ/moderat/schwer/sehr_schwer")
    confidence: ConfidenceLevel = Field(..., description="Confidence Level der Analyse")
    notes: Optional[str] = Field(None, description="Zusätzliche Bemerkungen")

    @field_validator("fuelstat_result")
    @classmethod
    def validate_fuelstat(cls, v: Optional[str]) -> Optional[str]:
        if v is not None:
            valid = {"negativ", "moderat", "schwer", "sehr_schwer"}
            if v not in valid:
                raise ValueError(f"FUELSTAT result must be one of {valid}")
        return v


class WaterContent(BaseModel):
    """Wassergehalt-Messung."""

    model_config = {"from_attributes": True}

    measurement_date: datetime
    method: str = Field(..., description="Messmethode: karl_fischer / calcium_hydride / paste / sensor")
    value_ppm: float = Field(..., ge=0, le=50000)
    assessment: str = Field(..., description="Bewertung: trocken/normal/erhoht/kritisch/gefahrlich")
    confidence: ConfidenceLevel

    @field_validator("method")
    @classmethod
    def validate_method(cls, v: str) -> str:
        valid = {"karl_fischer", "calcium_hydride", "paste", "sensor", "visual"}
        if v not in valid:
            raise ValueError(f"Method must be one of {valid}")
        return v

    @field_validator("assessment")
    @classmethod
    def validate_assessment(cls, v: str) -> str:
        valid = {"trocken", "normal", "erhoht", "kritisch", "gefahrlich"}
        if v not in valid:
            raise ValueError(f"Assessment must be one of {valid}")
        return v
```

### ANHANG J — Dieselpest-Diagnose und Behandlung

```python
"""
AYDI Fuel System — Diesel Bug Diagnosis and Treatment Models
"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class DieselBugDiagnosis(BaseModel):
    """Dieselpest-Diagnosemodell."""

    model_config = {"from_attributes": True}

    diagnosis_id: str = Field(..., description="Eindeutige Diagnose-ID")
    diagnosis_date: datetime
    boat_id: str
    tank_id: str
    contamination_stage: str = Field(
        ...,
        description="Stadium: none / stage_1_latent / stage_2_active / stage_3_massive"
    )
    organisms_detected: list[str] = Field(
        default_factory=list,
        description="Nachgewiesene Organismen, z.B. ['hormoconis_resinae', 'pseudomonas']"
    )
    fuelstat_result: Optional[str] = Field(None)
    cfu_per_ml: Optional[float] = Field(None, ge=0)
    biofilm_present: bool = Field(False)
    water_content_ppm: Optional[float] = Field(None, ge=0)
    visual_findings: list[str] = Field(default_factory=list)
    filter_condition: Optional[str] = Field(None, description="Filterzustand: clean / discolored / clogged / slime")
    smell: Optional[str] = Field(None, description="Geruch: normal / musty / foul / hydrogen_sulfide")
    motor_symptoms: list[str] = Field(
        default_factory=list,
        description="Motorsymptome, z.B. ['stalling', 'power_loss', 'rough_running']"
    )
    recommended_actions: list[str] = Field(default_factory=list)
    urgency: str = Field("medium")
    estimated_cost_eur_min: float = Field(0, ge=0)
    estimated_cost_eur_max: float = Field(0, ge=0)
    confidence: str = Field("estimated")
    notes: Optional[str] = None

    @field_validator("contamination_stage")
    @classmethod
    def validate_stage(cls, v: str) -> str:
        valid = {"none", "stage_1_latent", "stage_2_active", "stage_3_massive"}
        if v not in valid:
            raise ValueError(f"Stage must be one of {valid}")
        return v


class BiocideTreatment(BaseModel):
    """Biozid-Behandlungsprotokoll."""

    model_config = {"from_attributes": True}

    treatment_id: str = Field(..., description="Behandlungs-ID")
    treatment_date: datetime
    boat_id: str
    tank_id: str
    product_name: str = Field(..., description="Produktname, z.B. 'Grotamar 82'")
    active_ingredient: str = Field(..., description="Wirkstoff, z.B. 'MBT'")
    dosage_ppm: float = Field(..., ge=0, le=1000, description="Dosierung in ppm")
    tank_volume_liters: float = Field(..., gt=0, description="Tankvolumen in Litern")
    amount_ml: float = Field(..., gt=0, description="Zugegebene Menge in ml")
    treatment_type: str = Field(
        ...,
        description="Behandlungstyp: prophylactic / shock / follow_up"
    )
    engine_run_minutes: int = Field(0, ge=0, description="Motorlaufzeit nach Behandlung in Minuten")
    filter_changed_after_hours: Optional[int] = Field(
        None,
        description="Filterwechsel nach x Stunden"
    )
    follow_up_test_date: Optional[datetime] = None
    follow_up_test_result: Optional[str] = None
    notes: Optional[str] = None

    @field_validator("treatment_type")
    @classmethod
    def validate_treatment_type(cls, v: str) -> str:
        valid = {"prophylactic", "shock", "follow_up", "maximum"}
        if v not in valid:
            raise ValueError(f"Treatment type must be one of {valid}")
        return v
```

### ANHANG K — Filter und Fuel Polishing

```python
"""
AYDI Fuel System — Filter and Fuel Polishing Models
"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class FilterElement(BaseModel):
    """Filterelement-Spezifikation und Zustand."""

    model_config = {"from_attributes": True}

    filter_id: str
    position: str = Field(
        ...,
        description="Position: prefilter / primary / secondary / fuel_polishing"
    )
    manufacturer: str = Field(..., description="Hersteller, z.B. 'Racor'")
    model: str = Field(..., description="Modellnummer, z.B. '2010TM-OR'")
    micron_rating: float = Field(..., gt=0, le=100, description="Filterfeinheit in µm")
    installed_date: datetime
    installed_engine_hours: float = Field(..., ge=0)
    current_engine_hours: float = Field(..., ge=0)
    max_service_hours: float = Field(..., gt=0, description="Maximale Einsatzdauer in Stunden")
    max_service_months: int = Field(..., gt=0, description="Maximale Einsatzdauer in Monaten")
    vacuum_gauge_reading: Optional[str] = Field(
        None,
        description="Vacuometer-Anzeige: green / yellow / red"
    )
    visual_condition: Optional[str] = Field(
        None,
        description="Visueller Zustand: clean / discolored / clogged / slime / wax"
    )
    water_in_bowl: bool = Field(False)
    replacement_needed: bool = Field(False)
    replacement_part_number: Optional[str] = None
    replacement_cost_eur: Optional[float] = Field(None, ge=0)

    @property
    def hours_in_service(self) -> float:
        return self.current_engine_hours - self.installed_engine_hours

    @property
    def hours_remaining(self) -> float:
        return max(0, self.max_service_hours - self.hours_in_service)


class FuelPolishingSession(BaseModel):
    """Fuel Polishing Sitzungs-Dokumentation."""

    model_config = {"from_attributes": True}

    session_id: str
    session_date: datetime
    boat_id: str
    tank_id: str
    system_type: str = Field(
        ...,
        description="Systemtyp: fixed_kti / fixed_algaex / fixed_esi / mobile_service / portable"
    )
    tank_volume_liters: float = Field(..., gt=0)
    pump_flow_rate_lph: float = Field(..., gt=0, description="Pumpenleistung l/h")
    cycles_completed: int = Field(..., ge=1, description="Anzahl durchgelaufener Zyklen")
    duration_hours: float = Field(..., gt=0)
    water_removed_ml: float = Field(0, ge=0, description="Entferntes Wasser in ml")
    filter_changes_during: int = Field(0, ge=0, description="Filterwechsel während der Sitzung")
    pre_condition: Optional[str] = Field(None, description="Kraftstoffzustand vorher")
    post_condition: Optional[str] = Field(None, description="Kraftstoffzustand nachher")
    notes: Optional[str] = None
```

### ANHANG L — Tankinspektion

```python
"""
AYDI Fuel System — Tank Inspection Models
"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class TankInspection(BaseModel):
    """Tank-Inspektionsprotokoll."""

    model_config = {"from_attributes": True}

    inspection_id: str
    inspection_date: datetime
    boat_id: str
    tank_id: str
    tank_material: str = Field(
        ...,
        description="Material: aluminum / stainless_steel_316l / mild_steel / grp_frp / polyethylene"
    )
    tank_volume_liters: float = Field(..., gt=0)
    tank_age_years: Optional[float] = Field(None, ge=0)
    inspection_method: str = Field(
        ...,
        description="Methode: visual_external / endoscopic / manhole / ultrasonic_thickness"
    )
    fill_level_percent: float = Field(..., ge=0, le=100)
    sediment_depth_mm: float = Field(0, ge=0, description="Sedimenttiefe am Boden in mm")
    free_water_present: bool = Field(False)
    free_water_volume_ml: Optional[float] = Field(None, ge=0)
    biofilm_present: bool = Field(False)
    biofilm_coverage_percent: Optional[float] = Field(None, ge=0, le=100)
    corrosion_found: bool = Field(False)
    corrosion_severity: Optional[str] = Field(
        None,
        description="Korrosionsschwere: surface / pitting / through_wall"
    )
    wall_thickness_mm: Optional[float] = Field(None, gt=0, description="Gemessene Wandstärke")
    wall_thickness_original_mm: Optional[float] = Field(None, gt=0, description="Original-Wandstärke")
    baffle_condition: Optional[str] = Field(None, description="Schwallwand-Zustand")
    pickup_tube_height_mm: Optional[float] = Field(None, ge=0, description="Höhe Ansaugstutzen über Boden")
    return_position: Optional[str] = Field(None, description="Position des Rücklaufs")
    vent_line_clear: Optional[bool] = None
    filler_seal_condition: Optional[str] = Field(None, description="Einfüllstutzen-Dichtung")
    findings: list[str] = Field(default_factory=list)
    recommended_actions: list[str] = Field(default_factory=list)
    urgency: str = Field("low")
    estimated_cost_eur_min: float = Field(0, ge=0)
    estimated_cost_eur_max: float = Field(0, ge=0)
    photos: list[str] = Field(default_factory=list, description="Foto-Referenzen")
    confidence: str = Field("estimated")
    notes: Optional[str] = None
```

### ANHANG M — Winterfestmachung und Lagerung

```python
"""
AYDI Fuel System — Winterization and Storage Models
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, Field


class WinterizationProtocol(BaseModel):
    """Winterfestmachungs-Protokoll für das Kraftstoffsystem."""

    model_config = {"from_attributes": True}

    protocol_id: str
    execution_date: date
    boat_id: str
    expected_storage_months: int = Field(..., ge=1, le=60)
    storage_type: str = Field(
        ...,
        description="Lagertyp: standard_winter / extended_12plus / long_term_24plus"
    )
    tank_fill_level_percent: float = Field(..., ge=0, le=100)
    biocide_added: bool = Field(False)
    biocide_product: Optional[str] = None
    biocide_dose_ml: Optional[float] = Field(None, ge=0)
    stabilizer_added: bool = Field(False)
    stabilizer_product: Optional[str] = None
    stabilizer_dose_ml: Optional[float] = Field(None, ge=0)
    engine_run_after_additives_min: int = Field(0, ge=0)
    water_separator_drained: bool = Field(False)
    prefilter_changed: bool = Field(False)
    primary_filter_changed: bool = Field(False)
    fuel_valve_closed: bool = Field(False)
    vent_line_checked: bool = Field(False)
    filler_cap_sealed: bool = Field(False)
    bilge_dried: bool = Field(False)
    fuel_lines_inspected: bool = Field(False)
    fuel_polishing_performed: bool = Field(False)
    checklist_complete: bool = Field(False)
    notes: Optional[str] = None

    @property
    def is_extended_storage(self) -> bool:
        return self.expected_storage_months > 12

    @property
    def protocol_completeness_percent(self) -> float:
        checks = [
            self.tank_fill_level_percent >= 90,
            self.biocide_added,
            self.stabilizer_added,
            self.engine_run_after_additives_min >= 20,
            self.water_separator_drained,
            self.prefilter_changed,
            self.primary_filter_changed,
            self.fuel_valve_closed,
            self.vent_line_checked,
            self.filler_cap_sealed,
            self.bilge_dried,
        ]
        return (sum(checks) / len(checks)) * 100


class StorageMonitoring(BaseModel):
    """Überwachungsprotokoll während der Lagerzeit."""

    model_config = {"from_attributes": True}

    monitoring_id: str
    monitoring_date: datetime
    boat_id: str
    months_in_storage: float = Field(..., ge=0)
    water_separator_checked: bool = Field(False)
    water_found_ml: float = Field(0, ge=0)
    water_drained: bool = Field(False)
    stabilizer_topped_up: bool = Field(False)
    visual_check_ok: bool = Field(True)
    fuelstat_tested: bool = Field(False)
    fuelstat_result: Optional[str] = None
    ambient_temperature_celsius: Optional[float] = None
    humidity_percent: Optional[float] = Field(None, ge=0, le=100)
    action_required: bool = Field(False)
    actions_taken: list[str] = Field(default_factory=list)
    notes: Optional[str] = None
```

### ANHANG N — Wartungsplanung

```python
"""
AYDI Fuel System — Maintenance Planning Models
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, Field


class MaintenanceTask(BaseModel):
    """Einzelne Wartungsaufgabe im Kraftstoffsystem."""

    model_config = {"from_attributes": True}

    task_id: str
    task_code: str = Field(..., description="Aufgabencode, z.B. 'M-01', 'H-03', 'J-06'")
    description_de: str = Field(..., description="Beschreibung auf Deutsch")
    description_en: str = Field(..., description="Description in English")
    interval: str = Field(
        ...,
        description="Intervall: monthly / semi_annual / annual / hours_50 / hours_100 etc."
    )
    estimated_duration_minutes: int = Field(..., gt=0)
    tools_required: list[str] = Field(default_factory=list)
    parts_required: list[str] = Field(default_factory=list)
    estimated_cost_eur: float = Field(0, ge=0)
    skill_level: str = Field(
        "owner",
        description="Schwierigkeitsgrad: owner / competent_owner / mechanic / specialist"
    )
    safety_notes: list[str] = Field(default_factory=list)
    reference_documents: list[str] = Field(default_factory=list)


class MaintenanceSchedule(BaseModel):
    """Gesamter Wartungsplan für das Kraftstoffsystem."""

    model_config = {"from_attributes": True}

    schedule_id: str
    boat_id: str
    engine_model: str
    engine_hours_current: float = Field(..., ge=0)
    last_service_date: Optional[date] = None
    last_service_hours: Optional[float] = Field(None, ge=0)
    usage_pattern: str = Field(
        "seasonal",
        description="Nutzungsmuster: seasonal / year_round / charter / occasional"
    )
    tasks_due: list[MaintenanceTask] = Field(default_factory=list)
    tasks_overdue: list[MaintenanceTask] = Field(default_factory=list)
    next_service_date: Optional[date] = None
    next_service_hours: Optional[float] = None
    annual_cost_estimate_eur: float = Field(0, ge=0)


class MaintenanceRecord(BaseModel):
    """Dokumentation einer durchgeführten Wartung."""

    model_config = {"from_attributes": True}

    record_id: str
    record_date: datetime
    boat_id: str
    engine_hours: float = Field(..., ge=0)
    tasks_completed: list[str] = Field(..., description="Liste abgeschlossener Aufgabencodes")
    parts_used: list[str] = Field(default_factory=list)
    parts_cost_eur: float = Field(0, ge=0)
    labor_hours: float = Field(0, ge=0)
    labor_cost_eur: float = Field(0, ge=0)
    total_cost_eur: float = Field(0, ge=0)
    performed_by: str = Field(..., description="Ausführender: owner / mechanic / yard")
    findings: list[str] = Field(default_factory=list)
    follow_up_required: list[str] = Field(default_factory=list)
    photos: list[str] = Field(default_factory=list)
    notes: Optional[str] = None
```

### ANHANG O — Fehlerdiagnose

```python
"""
AYDI Fuel System — Fault Diagnosis Models
"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class FaultImage(BaseModel):
    """Fehlerbild im Kraftstoffsystem."""

    model_config = {"from_attributes": True}

    fault_id: str = Field(..., description="Fehlerbild-ID, z.B. 'F-KS-01'")
    title_de: str = Field(..., description="Titel auf Deutsch")
    title_en: str = Field(..., description="Title in English")
    category: str = Field(
        ...,
        description="Kategorie: diesel_bug / water / cold / blockage / leak / sensor / injection"
    )
    symptoms: list[str] = Field(..., description="Liste der Symptome")
    visual_indicators: list[str] = Field(default_factory=list)
    diagnostic_steps: list[str] = Field(default_factory=list)
    root_causes: list[RootCause] = Field(default_factory=list)
    immediate_actions: list[str] = Field(default_factory=list)
    permanent_fix: list[str] = Field(default_factory=list)
    prevention: list[str] = Field(default_factory=list)
    urgency: str = Field("medium")
    estimated_cost_eur_min: float = Field(0, ge=0)
    estimated_cost_eur_max: float = Field(0, ge=0)
    confidence: str = Field("estimated")
    related_faults: list[str] = Field(default_factory=list)
    photos: list[str] = Field(default_factory=list)


class RootCause(BaseModel):
    """Grundursache eines Fehlerbilds."""

    model_config = {"from_attributes": True}

    cause: str = Field(..., description="Beschreibung der Ursache")
    probability: str = Field(
        ...,
        description="Wahrscheinlichkeit: very_low / low / medium / high / very_high"
    )
    diagnostic_check: str = Field(..., description="Wie diese Ursache geprüft wird")


class TroubleshootingNode(BaseModel):
    """Knoten im Troubleshooting-Entscheidungsbaum."""

    model_config = {"from_attributes": True}

    node_id: str
    question_de: str = Field(..., description="Frage auf Deutsch")
    question_en: str = Field(..., description="Question in English")
    node_type: str = Field(
        ...,
        description="Knotentyp: question / action / resolution / escalation"
    )
    yes_next: Optional[str] = Field(None, description="Nächster Knoten bei 'Ja'")
    no_next: Optional[str] = Field(None, description="Nächster Knoten bei 'Nein'")
    action_description: Optional[str] = None
    tools_needed: list[str] = Field(default_factory=list)
    estimated_time_minutes: Optional[int] = Field(None, ge=0)
    skill_level: str = Field("owner")
    warning: Optional[str] = None


class TroubleshootingTree(BaseModel):
    """Vollständiger Troubleshooting-Entscheidungsbaum."""

    model_config = {"from_attributes": True}

    tree_id: str
    title_de: str
    title_en: str
    entry_symptom: str = Field(..., description="Eingangs-Symptom")
    nodes: list[TroubleshootingNode] = Field(..., min_length=2)
    total_paths: int = Field(..., ge=1, description="Anzahl möglicher Pfade")
    average_resolution_minutes: int = Field(..., ge=1)
```

### ANHANG P — Produktdatenbank

```python
"""
AYDI Fuel System — Product Database Models
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class FuelAdditive(BaseModel):
    """Kraftstoff-Additiv (Biozid, Stabilisator, Fließverbesserer, Reiniger)."""

    model_config = {"from_attributes": True}

    product_id: str
    product_name: str
    manufacturer: str
    product_type: str = Field(
        ...,
        description="Typ: biocide / stabilizer / flow_improver / injector_cleaner / multi_function"
    )
    active_ingredient: Optional[str] = None
    dosage_prophylactic_ml_per_100l: Optional[float] = Field(None, ge=0)
    dosage_treatment_ml_per_100l: Optional[float] = Field(None, ge=0)
    dosage_maximum_ml_per_100l: Optional[float] = Field(None, ge=0)
    available_sizes_ml: list[int] = Field(default_factory=list)
    price_range_eur: Optional[str] = None
    material_compatibility: list[str] = Field(
        default_factory=list,
        description="Kompatible Materialien: aluminum, steel, grp, pe, viton, nbr, ptfe"
    )
    shelf_life_months: Optional[int] = Field(None, ge=0)
    certifications: list[str] = Field(default_factory=list)
    effectiveness_rating: Optional[float] = Field(None, ge=0, le=10)
    availability_dach: str = Field("available", description="Verfügbarkeit: available / limited / import")
    notes: Optional[str] = None


class FilterProduct(BaseModel):
    """Filter-Produkt."""

    model_config = {"from_attributes": True}

    product_id: str
    product_name: str
    manufacturer: str
    filter_type: str = Field(
        ...,
        description="Typ: prefilter_separator / primary / secondary / fuel_polishing"
    )
    micron_rating: float = Field(..., gt=0, le=100)
    flow_rate_lph: float = Field(..., gt=0, description="Maximaler Durchfluss l/h")
    engine_power_range_hp: Optional[str] = None
    water_separation: bool = Field(False)
    sight_glass: bool = Field(False)
    heater_option: bool = Field(False)
    vacuum_gauge_option: bool = Field(False)
    replacement_element_part_no: Optional[str] = None
    replacement_element_cost_eur: Optional[float] = Field(None, ge=0)
    unit_cost_eur: Optional[float] = Field(None, ge=0)
    notes: Optional[str] = None


class FuelPolishingSystem(BaseModel):
    """Fuel Polishing System."""

    model_config = {"from_attributes": True}

    product_id: str
    product_name: str
    manufacturer: str
    flow_rate_lph: float = Field(..., gt=0)
    tank_size_max_liters: float = Field(..., gt=0)
    filter_stages: int = Field(..., ge=1)
    finest_micron: float = Field(..., gt=0)
    water_separation: bool = Field(True)
    magnetic_conditioning: bool = Field(False)
    operation_mode: str = Field(
        ...,
        description="Betriebsart: manual / timer / timer_sensor / fully_automatic"
    )
    power_supply: str = Field(..., description="Stromversorgung: 12v_dc / 24v_dc / 230v_ac")
    power_consumption_watts: Optional[float] = Field(None, ge=0)
    dimensions_mm: Optional[str] = None
    weight_kg: Optional[float] = Field(None, ge=0)
    price_eur: Optional[float] = Field(None, ge=0)
    installation_type: str = Field(
        ...,
        description="Installation: fixed / portable"
    )
    notes: Optional[str] = None
```

### ANHANG Q — Hersteller-Datenbank

```python
"""
AYDI Fuel System — Manufacturer Database Models
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class Manufacturer(BaseModel):
    """Herstellerinformationen."""

    model_config = {"from_attributes": True}

    manufacturer_id: str
    company_name: str
    headquarters_city: str
    headquarters_country: str
    dach_representative: Optional[str] = None
    website: Optional[str] = None
    founded_year: Optional[int] = Field(None, ge=1800, le=2100)
    core_products: list[str] = Field(default_factory=list)
    marine_share_percent: Optional[float] = Field(None, ge=0, le=100)
    market_position: Optional[str] = None
    certifications: list[str] = Field(default_factory=list)
    distribution_dach: list[str] = Field(default_factory=list)
    specialties: list[str] = Field(default_factory=list)
    contact_email: Optional[str] = None
    contact_phone: Optional[str] = None
    notes: Optional[str] = None


class ManufacturerProduct(BaseModel):
    """Zuordnung Hersteller zu Produkten."""

    model_config = {"from_attributes": True}

    manufacturer_id: str
    product_category: str = Field(
        ...,
        description="Kategorie: filtration / biocide / additive / fuel_polishing / diagnostics / tanks"
    )
    product_lines: list[str] = Field(default_factory=list)
    price_segment: str = Field(
        "mid",
        description="Preissegment: budget / mid / premium"
    )
    availability_dach: str = Field("available")
    typical_lead_time_days: Optional[int] = Field(None, ge=0)
    warranty_months: Optional[int] = Field(None, ge=0)
    spare_parts_availability: str = Field(
        "good",
        description="Ersatzteilverfügbarkeit: excellent / good / limited / poor"
    )
```

### ANHANG R — Gesamtbewertung Kraftstoffsystem

```python
"""
AYDI Fuel System — Overall Assessment Models
Module: fuel_system_assessment

Combines all inspection, diagnosis, and maintenance data
into a unified fuel system health score.
"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, computed_field


class FuelSystemComponent(BaseModel):
    """Einzelkomponenten-Bewertung im Kraftstoffsystem."""

    model_config = {"from_attributes": True}

    component: str = Field(
        ...,
        description="Komponente: tank / prefilter / primary_filter / secondary_filter / "
                    "fuel_lines / fittings / vent_line / filler / pickup / return / "
                    "fuel_pump / injection_system"
    )
    condition_score: float = Field(
        ...,
        ge=0,
        le=100,
        description="Zustandsbewertung 0-100 (100=neuwertig)"
    )
    confidence: str = Field("estimated")
    findings: list[str] = Field(default_factory=list)
    recommendations: list[str] = Field(default_factory=list)
    urgency: str = Field("low")
    estimated_remaining_life_months: Optional[int] = Field(None, ge=0)
    replacement_cost_eur: Optional[float] = Field(None, ge=0)


class FuelQualityAssessment(BaseModel):
    """Kraftstoffqualitäts-Bewertung."""

    model_config = {"from_attributes": True}

    assessment_date: datetime
    fuel_type: str = Field("diesel_b7")
    visual_condition: str
    water_content_status: str = Field(
        ...,
        description="Wassergehalt-Status: ok / elevated / critical / dangerous"
    )
    contamination_status: str = Field(
        ...,
        description="Kontaminations-Status: none / stage_1 / stage_2 / stage_3"
    )
    oxidation_status: str = Field(
        ...,
        description="Oxidations-Status: fresh / slight / moderate / severe"
    )
    overall_quality_score: float = Field(..., ge=0, le=100)
    usable: bool = Field(True, description="Kraftstoff noch nutzbar?")
    actions_required: list[str] = Field(default_factory=list)


class FuelSystemAssessment(BaseModel):
    """Gesamtbewertung des Kraftstoffsystems — AYDI Hauptmodell."""

    model_config = {"from_attributes": True}

    assessment_id: str
    assessment_date: datetime
    boat_id: str
    boat_name: Optional[str] = None
    boat_type: Optional[str] = None
    engine_model: Optional[str] = None
    engine_hours: Optional[float] = Field(None, ge=0)
    tank_volume_liters: Optional[float] = Field(None, gt=0)
    tank_material: Optional[str] = None

    # Component Assessments
    component_scores: list[FuelSystemComponent] = Field(default_factory=list)

    # Fuel Quality
    fuel_quality: Optional[FuelQualityAssessment] = None

    # Maintenance Status
    maintenance_up_to_date: bool = Field(True)
    overdue_tasks: list[str] = Field(default_factory=list)
    last_maintenance_date: Optional[datetime] = None

    # Diesel Bug Risk
    diesel_bug_risk: str = Field(
        "low",
        description="Dieselpest-Risiko: very_low / low / medium / high / very_high"
    )

    # Overall Scores
    overall_condition_score: float = Field(..., ge=0, le=100)
    reliability_score: float = Field(..., ge=0, le=100)

    # Confidence
    confidence: str = Field("estimated")
    data_sources: list[str] = Field(default_factory=list)

    # Recommendations
    immediate_actions: list[str] = Field(default_factory=list)
    short_term_recommendations: list[str] = Field(default_factory=list)
    long_term_recommendations: list[str] = Field(default_factory=list)

    # Cost Estimates
    immediate_cost_eur: float = Field(0, ge=0)
    annual_maintenance_cost_eur: float = Field(0, ge=0)
    five_year_cost_projection_eur: float = Field(0, ge=0)

    notes: Optional[str] = None

    @computed_field
    @property
    def risk_category(self) -> str:
        """Risikokategorie basierend auf Gesamtbewertung."""
        if self.overall_condition_score >= 80:
            return "niedrig"
        elif self.overall_condition_score >= 60:
            return "mittel"
        elif self.overall_condition_score >= 40:
            return "erhoeht"
        elif self.overall_condition_score >= 20:
            return "hoch"
        else:
            return "kritisch"

    @computed_field
    @property
    def display_badge_color(self) -> str:
        """Farbe des Confidence-Badges für die Anzeige."""
        badge_map = {
            "measured": "green",
            "calculated": "green",
            "visual_high": "blue",
            "visual_medium": "amber",
            "visual_low": "hidden",
            "visual_insufficient": "hidden",
            "estimated": "gray",
            "benchmark": "gray",
            "documented": "blue",
        }
        return badge_map.get(self.confidence, "gray")
```

---

## Ergänzung — Erweiterte Diagnose-Tabellen

### E.1 Motorenspezifische Filterkonfigurationen

**Volvo Penta D-Serie — Kraftstofffilter-Zuordnung (Confidence: measured):**

| Motor | Typ | Leistung | Vorfilter empfohlen | Primärfilter OEM | Sekundärfilter OEM | Filterfeinheit |
|-------|-----|----------|--------------------|-----------------|--------------------|----------------|
| D1-13 | Konventionell | 12 PS | Racor 110A / R20 | 861477 | — | 10 µm |
| D1-20 | Konventionell | 19 PS | Racor R20 / 200 | 861477 | — | 10 µm |
| D1-30 | Konventionell | 28 PS | Racor 200 / 320R | 861477 | — | 10 µm |
| D2-40 | Konventionell | 39 PS | Racor 200 / 320R | 3840335 | — | 10 µm |
| D2-50 | Common-Rail | 48 PS | Racor 320R | 22988765 | 21718912 | 5 µm |
| D2-60 | Common-Rail | 60 PS | Racor 320R | 22988765 | 21718912 | 5 µm |
| D2-75 | Common-Rail | 75 PS | Racor 500FG | 22988765 | 21718912 | 5 µm |
| D3-110 | Common-Rail | 110 PS | Racor 500FG | 21380488 | 20998367 | 2 µm |
| D3-150 | Common-Rail | 150 PS | Racor 500FG | 21380488 | 20998367 | 2 µm |
| D3-200 | Common-Rail | 200 PS | Racor 900MA | 21380488 | 20998367 | 2 µm |
| D4-260 | Common-Rail | 260 PS | Racor 900MA | 21380488 | 20998367 | 2 µm |
| D6-340 | Common-Rail | 340 PS | Racor 1000FG | 21380488 | 20998367 | 2 µm |
| D11-700 | Common-Rail | 700 PS | Racor 75/B32 Duplex | 22116209 | 22480372 | 2 µm |

**Yanmar Marine — Kraftstofffilter-Zuordnung (Confidence: measured):**

| Motor | Typ | Leistung | Vorfilter empfohlen | Primärfilter OEM | Filterfeinheit |
|-------|-----|----------|--------------------|--------------------|----------------|
| 1GM10 | Konventionell | 9 PS | Racor 110A | 104500-55710 | 10 µm |
| 2GM20 | Konventionell | 18 PS | Racor R20 | 104500-55710 | 10 µm |
| 3GM30 | Konventionell | 27 PS | Racor 200 | 104500-55710 | 10 µm |
| 3JH40 | Konventionell | 40 PS | Racor 200 / 320R | 129470-55810 | 10 µm |
| 4JH45 | Konventionell | 45 PS | Racor 320R | 129470-55810 | 10 µm |
| 4JH57 | Common-Rail | 57 PS | Racor 320R | 129A70-55800 | 5 µm |
| 4JH80 | Common-Rail | 80 PS | Racor 500FG | 129A70-55800 | 5 µm |
| 4JH110 | Common-Rail | 110 PS | Racor 500FG | 129A70-55800 | 2 µm |
| 4LHA-STP | Konventionell | 240 PS | Racor 900MA | 119593-55801 | 10 µm |
| 6LPA-STZP2 | Konventionell | 315 PS | Racor 1000FG | 119593-55801 | 10 µm |

### E.2 Saisonale Wartungsmatrix — Regionsspezifisch

**Ostsee / Nordsee (Saison April–Oktober):**

| Monat | Maßnahme | Begründung |
|-------|----------|------------|
| März | Wasserabscheider entleeren, FUELSTAT-Test, ggf. Fuel Polishing | Vor Saisonstart: Winterschäden erkennen |
| April | Vorfilter + Primärfilter wechseln, System entlüften | Frische Filter für die Saison |
| Mai | Normalbetrieb, monatliche Kontrolle | — |
| Juni | Monatliche Kontrolle, Wasserabscheider | — |
| Juli | Monatliche Kontrolle, FUELSTAT-Halbjahrestest | Mitte der Saison: Kontrolle |
| August | Monatliche Kontrolle | — |
| September | Monatliche Kontrolle, Vorfilter prüfen | — |
| Oktober | Winterfestmachung: Tank voll, Biozid + Stabilisator, Motor 20 min, Filter wechseln | Saisonende |
| Nov–Feb | Alle 6 Wochen: Wasserabscheider kontrollieren (falls zugänglich) | Winterlagerüberwachung |

**Mittelmeer (Saison März–November):**

| Monat | Maßnahme | Begründung |
|-------|----------|------------|
| Februar | Vor-Saison-Check wie Ostsee | — |
| März | Filterservice, Saisonstart | — |
| April–Mai | Monatliche Kontrolle | — |
| Juni | FUELSTAT-Test, erhöhte Aufmerksamkeit | Wärmebeginn → Dieselpest-Risiko steigt |
| Juli–August | Alle 2 Wochen Wasserabscheider (Hochsaison, Wärme!) | Höchstes Dieselpest-Risiko |
| September | FUELSTAT-Test, Vorfilter prüfen | — |
| Oktober | Monatliche Kontrolle | — |
| November | Winterfestmachung (verkürzt, mildere Winter) | — |
| Dez–Jan | Einmal Wasserabscheider kontrollieren | — |

**Blauwasser / Ganzjahresbetrieb:**

| Intervall | Maßnahme |
|-----------|----------|
| Alle 2 Wochen | Wasserabscheider entleeren |
| Monatlich | Kraftstoffprobe optisch prüfen, Bilgenkontrolle |
| Alle 3 Monate | FUELSTAT-Test, Vorfilter prüfen |
| Alle 6 Monate | Vorfilter + Primärfilter wechseln, Fuel Polishing |
| Jährlich | Sekundärfilter wechseln, Laboranalyse, Tankinspektion |
| Bei jedem Tanken in unbekanntem Hafen | Grotamar 82 Normaldosis zugeben |
| Vor Langstrecke (>500 sm) | Fuel Polishing, Ersatzfilter-Vorrat prüfen |

### E.3 Ersatzteil-Bevorratung nach Fahrtgebiet

**Küstensegler (Tagestörn, Wochenende):**

| Teil | Menge | Kosten (ca.) |
|------|-------|-------------|
| Racor-Filterelement (10 µm) | 1 Stk. | 15 EUR |
| Motor-Primärfilter | 1 Stk. | 25 EUR |
| O-Ring Racor-Gehäuse | 1 Stk. | 3 EUR |
| Grotamar 82 (100 ml) | 1 Fl. | 22 EUR |
| FUELSTAT-Test | 1 Stk. | 30 EUR |
| **Gesamt** | — | **~95 EUR** |

**Küstenfahrt / Urlaubstörn (1–3 Wochen):**

| Teil | Menge | Kosten (ca.) |
|------|-------|-------------|
| Racor-Filterelement (10 µm) | 2 Stk. | 30 EUR |
| Racor-Filterelement (30 µm, Notreserve) | 1 Stk. | 12 EUR |
| Motor-Primärfilter | 2 Stk. | 50 EUR |
| O-Ring Racor-Gehäuse | 2 Stk. | 6 EUR |
| Grotamar 82 (100 ml) | 1 Fl. | 22 EUR |
| FUELSTAT-Test | 2 Stk. | 60 EUR |
| Bandschlüssel (für Racor-Gehäuse) | 1 Stk. | 12 EUR |
| Wassererkennungspaste | 1 Tube | 18 EUR |
| **Gesamt** | — | **~210 EUR** |

**Blauwasser / Atlantiküberquerung:**

| Teil | Menge | Kosten (ca.) |
|------|-------|-------------|
| Racor-Filterelement (10 µm) | 6 Stk. | 90 EUR |
| Racor-Filterelement (30 µm) | 3 Stk. | 36 EUR |
| Racor-Filterelement (2 µm, falls CR-Motor) | 3 Stk. | 60 EUR |
| Motor-Primärfilter | 4 Stk. | 100 EUR |
| Motor-Sekundärfilter (falls CR) | 2 Stk. | 60 EUR |
| O-Ring Racor-Gehäuse | 4 Stk. | 12 EUR |
| O-Ring Motor-Filtergehäuse | 2 Stk. | 8 EUR |
| Grotamar 82 (500 ml) | 1 Fl. | 60 EUR |
| Fuel Set Diesel Kleen (500 ml) | 1 Fl. | 20 EUR |
| FUELSTAT-Test | 5 Stk. | 140 EUR |
| Bandschlüssel | 1 Stk. | 12 EUR |
| Wassererkennungspaste | 1 Tube | 18 EUR |
| Handentlüftungspumpe (Reserve) | 1 Stk. | 25 EUR |
| Kraftstoffschlauch (1 m, passend) | 1 Stk. | 15 EUR |
| Schlauchschellen (Sortiment) | 1 Set | 12 EUR |
| **Gesamt** | — | **~668 EUR** |

### E.4 Kraftstoffverbrauch — Referenzwerte nach Bootstyp

**Richtwerte für Planungsverbrauch (Confidence: benchmark):**

| Bootstyp | Motor | Marschfahrt | Verbrauch Marsch | Verbrauch Vollgas | Reichweite (90 % Tank) |
|----------|-------|-------------|------------------|-------------------|------------------------|
| Segelboot 32 ft | 1-Zyl 10 PS | 5,5 kn | 1,5 l/h | 2,5 l/h | 200 sm (50 L Tank) |
| Segelboot 38 ft | 3-Zyl 30 PS | 6,0 kn | 2,5 l/h | 5,0 l/h | 300 sm (100 L Tank) |
| Segelboot 45 ft | 4-Zyl 55 PS | 7,0 kn | 4,0 l/h | 8,0 l/h | 350 sm (200 L Tank) |
| Segelboot 50 ft | 4-Zyl 75 PS | 7,5 kn | 5,0 l/h | 12,0 l/h | 400 sm (300 L Tank) |
| Motorboot 28 ft | 1× 200 PS | 18 kn | 25 l/h | 55 l/h | 150 sm (250 L Tank) |
| Motorboot 35 ft | 2× 260 PS | 22 kn | 60 l/h | 130 l/h | 120 sm (500 L Tank) |
| Motorboot 45 ft | 2× 400 PS | 24 kn | 90 l/h | 200 l/h | 150 sm (800 L Tank) |
| Trawler 40 ft | 1× 80 PS | 7,5 kn | 6,0 l/h | 15,0 l/h | 800 sm (500 L Tank) |
| Trawler 50 ft | 1× 150 PS | 8,5 kn | 10,0 l/h | 25,0 l/h | 700 sm (800 L Tank) |
| Katamaran 40 ft (Segel) | 2× 30 PS | 6,5 kn | 2× 2,0 l/h | 2× 4,0 l/h | 400 sm (2× 150 L) |
| Katamaran 45 ft (Motor) | 2× 260 PS | 20 kn | 2× 30 l/h | 2× 65 l/h | 200 sm (2× 500 L) |

**Mehrverbrauch-Faktoren (Confidence: estimated):**

| Faktor | Mehrverbrauch | Typische Ursache |
|--------|---------------|-----------------|
| Bewuchs leicht (1–2 Monate) | +5–10 % | Algen, Schleimschicht |
| Bewuchs mittel (3–6 Monate) | +15–30 % | Seepocken, Bewuchs |
| Bewuchs schwer (>6 Monate) | +30–60 % | Starker Muschel-/Seepockenbesatz |
| Gegenwind 3 Bft (Motorboot) | +10–15 % | Luftwiderstand |
| Gegenwind 5 Bft (Motorboot) | +25–40 % | Luftwiderstand + Seegang |
| Gegenstrom 1 kn | +15–25 % | Verringerte Fahrt über Grund |
| Verstopfter Luftfilter | +5–10 % | Mangelnde Verbrennung |
| Verstopfter Kraftstofffilter | +5–15 % | Drosselverlust |
| Verkokte Einspritzdüsen | +10–25 % | Schlechtes Spritzbild |
| Fehlerhafter Turbolader | +15–30 % | Ladedruck zu niedrig |
| Propeller beschädigt (verbogen) | +10–25 % | Vibration, Kavitation |

### E.5 Sicherheitshinweise — Umgang mit Diesel und Additiven

**Persönliche Schutzausrüstung (PSA) bei Kraftstoffsystem-Arbeiten:**

| Arbeit | Handschuhe | Schutzbrille | Atemschutz | Hautschutz |
|--------|------------|-------------|------------|------------|
| Filterwechsel | Nitril empfohlen | Nein | Nein | Nein |
| Wasserabscheider entleeren | Nitril empfohlen | Nein | Nein | Nein |
| Biozid zugeben (Grotamar 82) | Nitril PFLICHT | Ja | Nein | Ja (Unterarme) |
| Tankreinigung | Nitril PFLICHT | Ja | Ja (Halbmaske A2) | Ja (Overall) |
| Kontakt mit kontaminiertem Diesel | Nitril PFLICHT | Ja | Bei H₂S-Geruch | Ja |
| Lecksuche | Nitril empfohlen | Nein | Nein | Nein |
| Kraftstoffleitung ersetzen | Nitril empfohlen | Nein | Nein | Nein |

**ATEX-Sicherheit bei Tankarbeiten:**

- Kraftstoff-Dämpfe können explosionsfähige Atmosphäre bilden
- KEINE Funken, offene Flammen oder Zündquellen im Umkreis von 3 m
- Elektrische Geräte müssen ATEX-konform sein (oder: nicht verwenden!)
- Endoskop-Kamera: nur batteriebetrieben, keine 230V-Geräte im Tank
- Belüftung sicherstellen: natürliche Belüftung oder ATEX-Ventilator
- Feuerlöscher (Schaum oder CO₂) in Reichweite
- Zweite Person in Rufweite (Buddy-System)

**Umweltschutz — Dieselentsorgung:**

| Material | Entsorgung | Kosten (ca.) |
|----------|-----------|-------------|
| Altdiesel (kontaminiert) | Schadstoffannahmestelle / Sondermüll | 0,30–0,80 EUR/L |
| Altdiesel (nur gealtert) | Heizöl-Verwertung (nach Rücksprache) | Kostenlos bis 0,20 EUR/L |
| Verbrauchte Filter | Hausmüll (Tropffrei) oder Wertstoffhof | Kostenlos |
| Dieselpest-Schleim | Sondermüll (biologisch kontaminiert) | Im Rahmen der Tankreinigung |
| Bilgenwasser mit Diesel | Bilgenwasserentsorger im Hafen | Kostenlos (meist) |
| Leere Biozid-Behälter | Wertstoffhof (Restentleerung beachten) | Kostenlos |

**VERBOTEN ist:**
- Diesel ins Meer, in die Bilge oder in die Kanalisation einleiten
- Kontaminierten Diesel in Gewässernähe lagern
- Biozid direkt ins Wasser einbringen
- Verbrauchte Filter über Bord werfen

### E.6 Normative Referenzen — Zusammenfassung

| Norm | Titel | Relevanz für Kraftstoffsystem |
|------|-------|-------------------------------|
| EN 590:2022 | Automotive Fuels — Diesel | Kraftstoffqualitäts-Anforderungen |
| EN 15940:2023 | Paraffinic Diesel Fuel (HVO/GTL) | Alternative Kraftstoffe |
| ISO 8217:2024 | Marine Fuel Specifications | Schwere Brennstoffe (>24m Yachten) |
| ISO 21487:2012 | Small Craft — Fuel Systems | Kraftstoffsystem-Design und -Sicherheit |
| ABYC H-33 | Diesel Fuel Systems | US-Standard für Diesel-Systeme |
| ISO 9094:2015 | Fire Protection | Brandschutz, Flammpunkt-Anforderungen |
| ISO 10088:2013 | Permanently Installed Fuel Systems | Fest installierte Kraftstoffsysteme |
| ASTM D6469 | Microbial Contamination in Fuels | Standard-Testmethoden für Dieselpest |
| ASTM D8070 | Immunoassay Detection in Fuel | FUELSTAT-Validierungsstandard |
| IP 385 | Determination of Microbial Growth | Dipslide-Testmethode |
| EN 14214 | FAME Specifications | Biodiesel-Qualitätsanforderungen |
| EN 14112 | Rancimat-Test | Oxidationsstabilität |
| DIN 51603 | Heizöl EL | Vergleich mit Diesel EN 590 |
| BPR (EU) 528/2012 | Biozidprodukteverordnung | Zulassung von Bioziden wie Grotamar 82 |

### E.7 Kontaktadressen — Professionelle Kraftstoffsystem-Dienstleister (DACH)

**Deutschland:**

| Firma | Standort | Leistung | Kontakt |
|-------|----------|----------|---------|
| Fuel Care Marine GmbH | Hamburg | Fuel Polishing, Tankreinigung, Laboranalyse | — |
| Tank-Service Nord | Kiel | Tankreinigung, Sanierung, Polishing | — |
| Marine Diesel Service Breege | Rügen | Diesel-Systemwartung, Einspritzservice | — |
| Bukh Bremen GmbH | Bremen | Racor-Vertrieb, Filtersysteme, Service | — |
| Technik-Service Lemmer | Lemmer (NL/DE) | Fuel Polishing mobil, Dieselpest-Sanierung | — |
| Motorenservice Süd GmbH | Lindau | Einspritzpumpen, Düsen, Motorspezialist | — |

**Österreich / Schweiz:**

| Firma | Standort | Leistung |
|-------|----------|----------|
| Marine Service Austria | Neusiedl am See | Kraftstoffsystem-Wartung, Motorservice |
| Bootstechnik Thunersee | Thun, CH | Diesel-Systemservice, Winterfestmachung |
| Werft Attersee | Attersee, AT | Full-Service Werft, Kraftstoffsystem-Sanierung |

---

*Ende der AYDI Wissensdatei 19.04 — Kraftstoffsystem Wartung und Troubleshooting*
*Version 1.0.0 — 2026-05-02*
*AYDI Research — AI Yacht Design Intelligence*