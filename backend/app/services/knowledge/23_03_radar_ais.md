---
title: "Radar und AIS — Radartechnologie, AIS-Klassen, MARPA, Overlay, Antennen"
kategorie: "23 Elektronik und Navigation"
unterkategorie: "23.03 Radar und AIS"
version: "1.0.0"
datum: "2026-05-08"
autor: "AYDI Research"
status: "validated"
confidence_quellen:
  - measured: "Hersteller-TDS, IMO-Normen, ITU-Vorschriften, CE-Zertifizierungen"
  - documented: "Hersteller-Kataloge, IMO-SOLAS, COLREG, IEC 62388, IEC 62287"
  - estimated: "Erfahrungswerte, Seerevier-Praxis, Werft- und Installationsberichte"
---

# 23.03 — Radar und AIS im Yachtbau: Vollständige Wissensreferenz

> **AYDI Wissensdatei 23.03** — Kategorie 23: Elektronik und Navigation
> **Confidence-Quelle:** measured (Hersteller-TDS, IMO/ITU-Normen), documented (Hersteller-Kataloge, COLREG, SOLAS), estimated (Erfahrungswerte, Seerevier-Praxis)
> **Letzte Aktualisierung:** 2026-05-08

---

## Inhaltsverzeichnis

1. [Einführung und Übersicht](#1-einführung-und-übersicht)
2. [Grundlagen und Theorie](#2-grundlagen-und-theorie)
3. [Typenübersicht](#3-typenübersicht)
4. [Produktlinien und Spezifikationen](#4-produktlinien-und-spezifikationen)
5. [Hersteller-Datenbank](#5-hersteller-datenbank)
6. [Fehlerbild-Atlas](#6-fehlerbild-atlas)
7. [Troubleshooting-Entscheidungsbäume](#7-troubleshooting-entscheidungsbäume)
8. [FAQ](#8-faq)
9. [Glossar](#9-glossar)
10. [Schnell-Referenz](#10-schnell-referenz)
11. [ANHANG A–H — Fallstudien](#11-anhang-ah--fallstudien)
12. [ANHANG I–R — Pydantic v2 Modelle](#12-anhang-ir--pydantic-v2-modelle)

---

## 1. Einführung und Übersicht

### 1.1 Definition und Funktion

Radar (Radio Detection and Ranging) und AIS (Automatic Identification System) bilden zusammen die beiden Hauptpfeiler der elektronischen Kollisionsverhütung im maritimen Bereich. Während Radar als eigenständiges Sensorsystem Ziele durch elektromagnetische Reflexion erkennt — unabhängig davon, ob das Ziel kooperiert — ist AIS ein kooperatives Transpondersystem, bei dem Schiffe aktiv ihre Position, Kurs, Geschwindigkeit und Identifikationsdaten austauschen.

Für die Yachtnavigation ergänzen sich beide Systeme komplementär:

1. **Radar** — Erkennt alle reflektierenden Objekte (Schiffe, Land, Bojen, Regenfelder, Eisberge), unabhängig davon, ob das Ziel einen Transponder trägt
2. **AIS** — Liefert präzise Identifikation, Kurs- und Geschwindigkeitsdaten kooperierender Schiffe, auch bei Radarschatten oder Clutter
3. **Overlay** — Die Kombination beider Datenquellen auf einer Kartenanzeige ergibt ein umfassendes Lagebild

### 1.2 COLREG-Relevanz

Die Internationalen Regeln zur Verhütung von Zusammenstößen auf See (COLREGs, 1972/2003) definieren in Regel 5 die Pflicht zur gehörigen Ausguck:

> *"Jedes Fahrzeug hat jederzeit durch Sehen und Hören sowie durch jedes andere verfügbare Mittel, das den gegebenen Umständen und Bedingungen entspricht, einen gehörigen Ausguck zu halten..."*

Radar und AIS fallen explizit unter "jedes andere verfügbare Mittel". Regel 7 (Risiko der Kollision) verlangt die Nutzung des Radars:

- **Regel 7(a):** Jedes Fahrzeug muss alle verfügbaren Mittel nutzen, um festzustellen, ob ein Kollisionsrisiko besteht
- **Regel 7(b):** Radarausrüstung, soweit vorhanden, ist ordnungsgemäß zu nutzen, einschließlich Radar-Plotting/ARPA
- **Regel 8:** Manöver zur Vermeidung von Zusammenstößen müssen frühzeitig und entschlossen erfolgen

Für Yachten unter 24m besteht keine gesetzliche Pflicht zur Radarausstattung, jedoch wird die Nichtnutzung vorhandener Geräte im Schadensfall als Fahrlässigkeit gewertet.

### 1.3 Historische Entwicklung

**Radar-Geschichte in der Sportschifffahrt:**

| Zeitraum | Entwicklung | Bedeutung |
|----------|-------------|-----------|
| 1935–1945 | Militärische Radarentwicklung | Grundlagentechnologie |
| 1950–1960 | Erste Handelsschiff-Radare | Nur Großschiffe, >500 BRT |
| 1970–1980 | Erste Yachtradargeräte (Furuno, Raytheon) | 4 kW Pulsradar, Radome 18" |
| 1980–1990 | LCD-Displays ersetzen CRT | Kompaktere Anzeigen möglich |
| 1990–2000 | Digitale Signalverarbeitung, MARPA | Zieltracking auf Yachten |
| 2000–2010 | Breitband-Radar (Navico/Simrad), Ethernet-Vernetzung | Solid-State-Revolution beginnt |
| 2010–2020 | FMCW/Puls-Kompression, Doppler, WiFi-Anbindung | Simrad Halo, Garmin Fantom |
| 2020–heute | Dual-Range, Bird-Mode, VelocityTrack, NoDrift | Garmin Fantom 24x, Raymarine Quantum 2 |

**AIS-Geschichte:**

| Zeitraum | Entwicklung | Bedeutung |
|----------|-------------|-----------|
| 1990–2000 | ITU und IMO entwickeln AIS-Standard | SOTDMA-Protokoll definiert |
| 2002 | SOLAS-Pflicht für AIS Klasse A (>300 BRT) | Internationaler Rollout |
| 2006 | AIS Klasse B spezifiziert (IEC 62287) | CSTDMA für Sportschifffahrt |
| 2012 | AIS Klasse B+ (CS+) mit 5W Sendeleistung | Verbesserte Sichtbarkeit |
| 2014–2018 | AIS-SART und AIS-MOB-Geräte | Rettungstechnik |
| 2020–heute | AIS Klasse B+ 5W als Standard, Integration in MFDs | Breite Yacht-Adoption |

### 1.4 Bedeutung im AYDI-Analysesystem

Im Kontext des AYDI-Analysesystems beeinflusst die Radar/AIS-Installation folgende Module:

- **Compliance-Modul:** CE-Konformität der Antenneninstallation, EMV-Normen, Abstrahlsicherheit
- **Ergonomie-Modul:** Bedienerfreundlichkeit der MFD-Integration, Radarbildqualität bei verschiedenen Bedingungen
- **Kosten-Modul:** Systemkosten (Antenne + Anzeige + AIS + Verkabelung) typisch 3.000–25.000 EUR
- **Produktions-Modul:** Mastmontage vs. Archbogen, Kabelführung, Interferenzabstände
- **Gewichts-Modul:** Radarantenne im Mast beeinflusst Schwerpunkthöhe (2–12 kg in 15–20m Höhe)
- **Elektrik-Modul:** Stromaufnahme (20–50W Standby, 80–200W Senden bei Pulsradar)
- **Strukturmodul:** Verstärkung des Montageplatzes, Vibrationsbelastung bei Open-Array

### 1.5 Regulatorischer Rahmen

**Relevante Normen und Vorschriften:**

| Norm/Vorschrift | Inhalt | Anwendung |
|----------------|--------|-----------|
| IMO SOLAS V/19 | Pflichtausrüstung Navigation | >300 BRT, >500 BRT Schwellen |
| COLREG Regel 5, 7, 8 | Ausguck, Kollisionsrisiko | Alle Fahrzeuge |
| IEC 62388 (2013) | Schiffsradar-Leistungsanforderungen | Typzulassung Radar |
| IEC 62252 (2004) | Radar für Nicht-SOLAS-Fahrzeuge, Leistungsanforderungen | Typzulassung Yacht-/Sportbootradar |
| IEC 62287-1 (2017) | AIS Klasse B Anforderungen | Typzulassung AIS-B |
| IEC 62287-2 (2017) | AIS Klasse B+ (SOTDMA) | Typzulassung AIS-B+ |
| ITU-R M.1371-5 (2014) | AIS-Protokoll-Spezifikation | Technisches Protokoll |
| ETSI EN 300 338 | DSC-Ausrüstung (verwandt) | EMV-Anforderungen |
| ETSI EN 302 248 | Schiffsradar (Nicht-SOLAS) S/X-Band | EMV und Frequenzzuweisung |
| RED 2014/53/EU | Funkgeräte-Richtlinie | CE-Kennzeichnung |

**Frequenzzuweisungen für Yachtradar:**

| Band | Frequenz | Wellenlänge | Typische Nutzung |
|------|----------|-------------|------------------|
| X-Band | 9.300–9.500 MHz (9,41 GHz ±25 MHz) | ~3,2 cm | Standard-Yachtradar |
| S-Band | 2.900–3.100 MHz (3,05 GHz) | ~10 cm | Großyachten, Regenunterdrückung |
| AIS VHF | 161,975 MHz (AIS1), 162,025 MHz (AIS2) | ~1,85 m | AIS-Transponder |

---

## 2. Grundlagen und Theorie

### 2.1 Radar-Physik

#### 2.1.1 Elektromagnetische Wellen und Radargleichung

Die Radar-Grundgleichung (Radar Range Equation) beschreibt die Empfangsleistung eines Radarziels:

```
Pr = (Pt × Gt × Gr × λ² × σ) / ((4π)³ × R⁴)

wobei:
  Pr = empfangene Leistung [W]
  Pt = Sendeleistung [W]
  Gt = Gewinn der Sendeantenne [dimensionslos]
  Gr = Gewinn der Empfangsantenne [dimensionslos]
  λ  = Wellenlänge [m]
  σ  = Radarquerschnitt (RCS) des Ziels [m²]
  R  = Entfernung zum Ziel [m]
```

**Schlüsselerkenntnisse für die Yachtpraxis:**

1. **R⁴-Abhängigkeit:** Die Empfangsleistung sinkt mit der vierten Potenz der Entfernung. Doppelte Reichweite erfordert 16-fache Sendeleistung.
2. **λ²-Abhängigkeit:** Längere Wellenlängen (S-Band) benötigen mehr Sendeleistung für gleiche Reichweite, durchdringen aber Niederschlag besser.
3. **σ-Abhängigkeit:** Der Radarquerschnitt des Ziels variiert enorm (GFK-Segelboot 1–5 m², Containerschiff 10.000–50.000 m²).

#### 2.1.2 Wellenlänge und Auflösung

**Entfernungsauflösung (Range Resolution):**

```
ΔR = c × τ / 2

wobei:
  ΔR = minimaler Abstand zwischen zwei unterscheidbaren Zielen [m]
  c  = Lichtgeschwindigkeit (3 × 10⁸ m/s)
  τ  = Pulsdauer [s]
```

Beispiele:
- Kurzer Puls (0,05 µs): ΔR = 7,5 m
- Mittlerer Puls (0,25 µs): ΔR = 37,5 m
- Langer Puls (1,0 µs): ΔR = 150 m

**Azimutale Auflösung (Bearing Resolution):**

```
Δθ ≈ λ / D  [rad]   bzw.   Δθ ≈ 57,3 × λ / D  [°]

wobei:
  Δθ = Azimut-Strahlbreite (horizontal)
  λ  = Wellenlänge [m]
  D  = Antennenlänge (Apertur) [m]
```

Beispiele bei X-Band (λ = 0,032 m):
- 18" Radome (D ≈ 0,30 m): Δθ ≈ 6,1° — Hafennavigation, Nahbereich
- 24" Radome (D ≈ 0,45 m): Δθ ≈ 4,1° — Guter Kompromiss
- 3 ft Open-Array (D ≈ 0,91 m): Δθ ≈ 2,0° — Gute Zieltrennun
- 4 ft Open-Array (D ≈ 1,22 m): Δθ ≈ 1,5° — Exzellente Zieltrennun
- 6 ft Open-Array (D ≈ 1,83 m): Δθ ≈ 1,0° — Professionell

#### 2.1.3 Radarreichweite

Die maximale Radarreichweite wird begrenzt durch:

**1. Radarelektrische Reichweite** — bestimmt durch Sendeleistung, Antennengewinn und Empfängerempfindlichkeit

**2. Radaroptische Reichweite** — bestimmt durch Erdkrümmung und Antennenhöhe:

```
R_max [nm] ≈ 2,21 × (√h_A + √h_Z)

wobei:
  h_A = Antennenhöhe über Wasser [m]
  h_Z = Zielhöhe über Wasser [m]
```

Beispiele:
- Antenne am Mast (15 m), Frachtschiff (30 m): ≈ 20,6 nm
- Antenne am Archbogen (4 m), Segelboot (12 m): ≈ 11,9 nm
- Antenne am Geräteträger (3 m), kleines Boot (2 m): ≈ 6,6 nm

**3. Minimale Erfassungsentfernung** — wichtig im Nahbereich:
- Pulsradar: R_min = c × τ/2 + Totzeit (typisch 25–75 m)
- FMCW/Broadband: R_min typisch 6–20 m (deutlich besser)

#### 2.1.4 Radarquerschnitt (RCS) typischer Ziele

| Ziel | Typischer RCS [m²] | Anmerkung |
|------|--------------------:|-----------|
| GFK-Segelboot 8–10 m | 1–5 | Ohne Reflektor, sehr schwach |
| GFK-Segelboot mit Reflektor | 5–15 | Octahedral-Reflektor, abhängig von Qualität |
| GFK-Motoryacht 10–15 m | 5–25 | Geländer, Aufbauten reflektieren |
| Stahl-Segelboot 12 m | 15–50 | Gute Reflexion |
| Aluminium-Motoryacht 20 m | 50–200 | Sehr gute Reflexion |
| Fischerboot Stahl 15–25 m | 50–500 | Variable Aufbauten |
| Frachter 100 m | 3.000–10.000 | Massive Reflexion |
| Containerschiff 300 m | 10.000–50.000 | Dominantes Ziel |
| Boje Stahl (gross) | 10–50 | Stark richtungsabhängig |
| Boje Kunststoff (klein) | 0,1–1 | Schwer zu erkennen |
| Holzpfahl/Dalbe | 0,5–3 | Sehr schwaches Ziel |
| Schwimmendes Treibgut | 0,01–0,5 | Nahezu unsichtbar |
| Radarreflektor (Echomax) | 10–25 (spezifiziert) | Laborwert, Praxis oft weniger |
| RTE (Radar Target Enhancer) | Aktiv 15–25 dB Verstärkung | Elektronischer Verstärker |

### 2.2 Pulsradar vs. FMCW (Broadband/Solid-State)

#### 2.2.1 Pulsradar — Klassisches Verfahren

**Funktionsprinzip:**
Das klassische Pulsradar sendet kurze, intensive Hochfrequenzimpulse aus und misst die Laufzeit des reflektierten Signals. Die Entfernung ergibt sich aus:

```
R = c × t / 2

wobei:
  R = Entfernung [m]
  c = Lichtgeschwindigkeit [m/s]
  t = Signallaufzeit [s]
```

**Technische Merkmale:**

| Parameter | Typische Werte (Yacht) |
|-----------|----------------------|
| Sendeleistung (Spitze) | 2 kW, 4 kW, 12 kW, 25 kW |
| Pulswiederholfrequenz (PRF) | 800–3.000 Hz |
| Pulsdauer (kurz) | 0,05–0,12 µs |
| Pulsdauer (lang) | 0,5–1,2 µs |
| Aufwärmzeit | 60–120 Sekunden (Magnetron) |
| Lebensdauer Magnetron | 2.000–5.000 Betriebsstunden |
| Stromaufnahme (Senden) | 30–200 W |
| Gewicht Antenne | 5–25 kg (je nach Typ) |

**Vorteile:**
- Bewährte Technologie, jahrzehntelange Erfahrung
- Hohe Spitzen-Sendeleistung für maximale Reichweite
- Gute Regenunterdrückung bei hoher Leistung
- Günstigere Open-Array-Varianten verfügbar

**Nachteile:**
- Magnetron-Verschleiß (Austausch ca. alle 3.000–5.000 h)
- Aufwärmzeit 60–120 Sekunden
- Höhere Mindestentfernung (25–75 m)
- Höhere Strahlungsleistung (Sicherheitsabstände beachten)
- Höherer Stromverbrauch

#### 2.2.2 FMCW — Frequency Modulated Continuous Wave (Broadband/Solid-State)

**Funktionsprinzip:**
FMCW-Radar sendet ein kontinuierliches Signal mit linear ansteigender Frequenz (Chirp). Die Entfernung wird aus der Frequenzdifferenz zwischen Sende- und Empfangssignal ermittelt:

```
R = c × Δf / (2 × S)

wobei:
  R  = Entfernung [m]
  c  = Lichtgeschwindigkeit [m/s]
  Δf = Frequenzdifferenz zwischen Sende- und Empfangssignal [Hz]
  S  = Sweep-Rate (Frequenzänderung pro Zeiteinheit) [Hz/s]
```

**Technische Merkmale:**

| Parameter | Typische Werte (Yacht) |
|-----------|----------------------|
| Sendeleistung (mittlere) | 165 mW – 25 W |
| Bandbreite | 50–350 MHz |
| Sweep-Dauer | 1–100 µs |
| Aufwärmzeit | 0–5 Sekunden (sofort einsatzbereit) |
| Lebensdauer Sender | >10.000 h (kein Verschleißteil) |
| Stromaufnahme | 15–40 W |
| Gewicht Antenne | 2–8 kg |
| Mindestentfernung | 6–20 m |

**Vorteile:**
- Keine Aufwärmzeit — sofort betriebsbereit
- Extrem geringe Mindestentfernung (ab 6 m)
- Kein Magnetron-Verschleiß
- Deutlich geringerer Stromverbrauch
- Leichter (besonders relevant für Mastmontage auf Segelbooten)
- Geringere EMV-Abstrahlung
- Ermöglicht Doppler-Erkennung (bewegte Ziele farblich markieren)

**Nachteile:**
- Geringere effektive Reichweite bei extremen Bedingungen
- Neuere Technologie, weniger Langzeiterfahrung (seit 2009)
- Bei starkem Regen/See kann Clutter-Unterdrückung schwieriger sein
- Höherer Preis bei vergleichbarer Reichweite

#### 2.2.3 Puls-Kompression (Pulse Compression)

Moderne Radare kombinieren Vorteile beider Verfahren:

**Funktionsprinzip:**
Ein langer, frequenzmodulierter Puls (Chirp-Puls) wird gesendet. Im Empfänger wird das Signal mittels Matched-Filter komprimiert, was die Entfernungsauflösung eines kurzen Pulses bei der Energie eines langen Pulses ergibt.

```
Kompressionsverhältnis = Bandbreite × Pulsdauer = B × τ

Effektive Auflösung = c / (2 × B)
```

Beispiel: B = 50 MHz, τ = 10 µs → Kompression = 500:1, Auflösung = 3 m

Anwendung: Garmin Fantom-Serie, Simrad Halo-Serie (kombinieren Puls-Kompression mit FMCW).

### 2.3 Doppler-Radar und Bewegungserkennung

#### 2.3.1 Doppler-Effekt im Radar

```
f_d = 2 × v_r × f_0 / c

wobei:
  f_d  = Doppler-Frequenzverschiebung [Hz]
  v_r  = Radialgeschwindigkeit des Ziels relativ zum Radar [m/s]
  f_0  = Sendefrequenz [Hz]
  c    = Lichtgeschwindigkeit [m/s]
```

Bei X-Band (9,41 GHz):
- 1 kn (0,514 m/s) → f_d ≈ 32 Hz
- 10 kn (5,14 m/s) → f_d ≈ 322 Hz
- 30 kn (15,4 m/s) → f_d ≈ 966 Hz

#### 2.3.2 VelocityTrack / MotionScope / Doppler Target Trail

Moderne Solid-State-Radare nutzen den Doppler-Effekt zur farblichen Markierung:
- **Sich nähernde Ziele:** Rot dargestellt
- **Sich entfernende Ziele:** Grün/Blau dargestellt
- **Stationäre Ziele:** Normal dargestellt

**Implementierung nach Hersteller:**

| Hersteller | Bezeichnung | Verfügbar ab |
|------------|-------------|-------------|
| Garmin | MotionScope (Doppler) | Fantom-Serie |
| Simrad/B&G | VelocityTrack | Halo-Serie |
| Raymarine | Doppler Target Alert | Quantum 2 |
| Furuno | Target Analyzer | DRS-NXT-Serie |

#### 2.3.3 NoDrift-Modus / Ankerüberwachung

Fortschrittliche Radar-Doppler-Funktion zur Ankerüberwachung:
- Radar im stationären Modus, erkennt jede Bewegung
- Alarm bei Ankerdrift (Positionsveränderung >eingestellter Schwelle)
- Erkennung von Schiffen, die sich dem ankernden Boot nähern
- Implementiert bei Garmin (Anchor Drag Alert), Simrad/B&G (NoDrift)

### 2.4 MARPA und ARPA

#### 2.4.1 ARPA — Automatic Radar Plotting Aid

ARPA ist ein IMO-vorgeschriebenes System für Großschiffe (>10.000 BRT), das automatisch:
- Radarziele erfasst und trackt (mind. 20 Ziele gleichzeitig)
- CPA (Closest Point of Approach) und TCPA (Time to CPA) berechnet
- Alarm bei Unterschreitung eingestellter CPA/TCPA-Grenzen auslöst
- Zielkurs und -geschwindigkeit berechnet (True/Relative Motion)
- Trial-Manöver simuliert

Anforderungen gemäß IEC 62388:
- Automatische Zielerfassung in definierten Überwachungszonen
- Tracking-Genauigkeit: Kurs ±3°, Geschwindigkeit ±1 kn (nach 3 Minuten Tracking)
- CPA-Genauigkeit: ±0,3 nm
- TCPA-Genauigkeit: ±1 Minute

#### 2.4.2 MARPA — Mini-ARPA

MARPA ist die vereinfachte Version für Yachten und Kleinschiffe:

**Funktionsmerkmale:**

| Merkmal | ARPA | MARPA |
|---------|------|-------|
| Zielerfassung | Automatisch | Manuell (per Cursor) |
| Gleichzeitige Ziele | >20 (bis 100+) | Typisch 10–30 |
| Kursberechnung | True + Relative | True + Relative |
| CPA/TCPA | Ja, mit Alarm | Ja, mit Alarm |
| Trial-Manöver | Ja | Manchmal (herstellerabhängig) |
| Überwachungszonen | Ja | Selten |
| IMO-Konformität | Ja | Nein (nicht gefordert) |
| Genauigkeit | Höher (bessere Antenne) | Abhängig von Antenne |

**MARPA-Genauigkeit in der Praxis:**

Die Qualität der MARPA-Berechnung hängt ab von:
1. **Kompass-Genauigkeit:** Heading-Sensor muss <1° Genauigkeit haben (idealerweise Rate-Compass oder Satellitenkompass)
2. **GPS-Qualität:** Position und SOG/COG-Genauigkeit
3. **Radarbild-Qualität:** Clutter, Zielstärke, Mehrwegausbreitung
4. **Tracking-Dauer:** Mindestens 3 vollständige Antennenumdrehungen (ca. 1–3 Minuten)
5. **Eigenes Manöver:** Bei Kursänderung werden MARPA-Werte vorübergehend ungenau

**Empfohlene CPA/TCPA-Alarmschwellen:**

| Revier | CPA-Alarm | TCPA-Alarm |
|--------|-----------|------------|
| Offene See | 1,0–2,0 nm | 15–20 min |
| Küstengewässer | 0,5–1,0 nm | 10–15 min |
| Enge Fahrwasser | 0,2–0,5 nm | 5–10 min |
| Hafen/Ankerplatz | 0,1–0,2 nm | 3–5 min |

### 2.5 Radarziel-Eigenschaften

#### 2.5.1 Faktoren der Radarrückstrahlung

Die Erkennbarkeit eines Ziels im Radar hängt von folgenden Faktoren ab:

**Material:**
- Metall (Stahl, Aluminium): Exzellente Reflexion
- GFK/CFK: Sehr schwache Reflexion (durchlässig)
- Holz: Schwache bis moderate Reflexion (feuchtigkeitsabhängig)
- Beton: Moderate Reflexion

**Geometrie:**
- Senkrechte Flächen zum Radar: Starke Reflexion
- Ecken (Trihedral/Dihedral): Retroreflexion — sehr stark
- Gerundete Flächen: Streuen das Signal, schwache Reflexion
- Flache, geneigte Flächen: Reflektieren weg vom Radar

**Oberflächenbeschaffenheit:**
- Glatte metallische Oberfläche: Maximum-Reflexion
- Raue Oberfläche: Diffuse Streuung
- Beschichtete Oberfläche: Absorptionsverluste

**Aspektwinkel:**
- Bug/Heck eines Schiffes: Geringerer RCS als Seitenansicht
- Yachten mit breiter Seite: Deutlich besser erkennbar

#### 2.5.2 Radarreflektor-Typen für Yachten

| Typ | Prinzip | Typischer RCS | Gewicht | Preis |
|-----|---------|--------------|---------|-------|
| Octahedral (zusammenklappbar) | 8 Trihedrale | 1–10 m² (oft <5 m²) | 0,5–1,5 kg | 30–80 EUR |
| Zylindrischer Reflektor (Echomax) | Luneburg-Linse ähnlich | 7–24 m² | 1,5–4 kg | 150–500 EUR |
| Mobri Radarreflektor | Gestapelte Platten | 3–12 m² | 1–2 kg | 80–200 EUR |
| Radar Target Enhancer (RTE) | Aktiver Verstärker | 15–25 dB Gain | 2–4 kg | 600–2.500 EUR |
| Echomax Active-X | Aktiv + Passiv | 20+ m² äquivalent | 3–5 kg | 1.500–3.000 EUR |

**ISO 8729-1:2010 (passive Radarreflektoren):** Standard für Radarreflektoren — im X-Band Mindest-Rückstrahlfläche (RCS) ≥2,5 m² über einen Azimutwinkel von mind. 240° (aufrecht; ≥0,625 m² bei Krängung bis ±15°) sowie Spitzen-RCS ≥10 m². Confidence: documented (ISO 8729-1:2010; RYA/Echomax).

> ✅ Aufgelöst (Audit): ISO 8729-1:2010 fordert im X-Band ≥2,5 m² RCS über 240° Azimut (Spitze ≥10 m²), nicht 7,5 m² — der Wert 7,5 m² gehört zu aktiven Reflektoren nach ISO 8729-2. Quelle: RYA "Radar Reflectors" / Echomax Marine Regulations (ISO 8729-1:2010).

**Montagehinweise:**
- Mindesthöhe 4 m über Wasserlinie
- Freie Sicht 360°
- Bei Segelbooten: idealerweise am Achterstag oder Masthalter auf halber Masthöhe
- Octahedral-Reflektor in "catch rain"-Position (Öffnungen nach oben wie ein Trichter)

### 2.6 AIS-Protokoll — Technische Grundlagen

#### 2.6.1 VHF-Datenverbindung (VDL)

AIS nutzt zwei dedizierte VHF-Frequenzen im maritimen Band:
- **AIS 1:** 161,975 MHz (Kanal 87B)
- **AIS 2:** 162,025 MHz (Kanal 88B)

**Modulation:** GMSK (Gaussian Minimum Shift Keying) mit BT = 0,4
**Datenrate:** 9.600 bps
**Kanalzugriff:** TDMA (Time Division Multiple Access) — 2.250 Zeitschlitze pro Minute und Kanal

#### 2.6.2 SOTDMA vs. CSTDMA

**SOTDMA — Self-Organising Time Division Multiple Access:**
- Verwendet von AIS Klasse A und AIS Klasse B+ (CS)
- Jeder Transponder verwaltet seinen Zeitschlitz selbst
- Reservierung von Zeitschlitzen für zukünftige Übertragungen
- Deterministischer Zugriff — garantierte Übertragung
- Kann bis zu 4.500 Schiffe in einem Bereich verwalten
- Senderate abhängig von Geschwindigkeit und Kursänderung:

| Schiffszustand | Berichtsrate Klasse A | Berichtsrate Klasse B+ (SOTDMA) |
|---------------|---------------------|-------------------------------|
| Vor Anker / festgemacht | 3 Minuten | 3 Minuten |
| SOG 0–2 kn | 10 Sekunden | 30 Sekunden |
| SOG 0–2 kn, Kursänderung | 3,3 Sekunden | 30 Sekunden |
| SOG 2–14 kn | 10 Sekunden | 30 Sekunden |
| SOG 2–14 kn, Kursänderung | 3,3 Sekunden | 15 Sekunden |
| SOG 14–23 kn | 6 Sekunden | 15 Sekunden |
| SOG 14–23 kn, Kursänderung | 2 Sekunden | 5 Sekunden |
| SOG >23 kn | 2 Sekunden | 5 Sekunden |

**CSTDMA — Carrier Sense Time Division Multiple Access:**
- Verwendet von AIS Klasse B (Standard)
- Überprüft, ob Zeitschlitz frei ist, bevor gesendet wird
- Non-deterministisch — bei Überlastung können Nachrichten verloren gehen
- Klasse-B-Transponder haben niedrigere Priorität als Klasse A
- Feste Berichtsrate: alle 30 Sekunden (SOG >2 kn), alle 3 Minuten (vor Anker)

#### 2.6.3 AIS-Nachrichtentypen

| Msg-ID | Bezeichnung | Sender | Inhalt |
|--------|-------------|--------|--------|
| 1, 2, 3 | Positionsbericht (geplant/zugewiesen/interrogiert) | Klasse A | MMSI, Status, SOG, COG, Position, HDG, ROT |
| 4 | Basisstation Bericht | Basisstation | Datum/Uhrzeit, Position |
| 5 | Statische + Reisedaten | Klasse A | Schiffsname, Typ, Abmessungen, Tiefgang, Zielhafen, ETA |
| 6 | Adressierte binäre Nachricht | Alle | Punkt-zu-Punkt Nachricht |
| 7 | Binäre Empfangsbestätigung | Alle | Bestätigung für Msg 6 |
| 8 | Binäre Broadcastnachricht | Alle | Wetter, Gezeiten, etc. |
| 9 | SAR-Flugzeug Positionsbericht | SAR-Flugzeug | Position, Höhe, Geschwindigkeit |
| 10 | UTC/Datum-Anfrage | Alle | Zeitanfrage |
| 11 | UTC/Datum-Antwort | Basisstation | Zeitantwort |
| 12 | Adressierte Sicherheitsnachricht | Alle | Sicherheitsmeldung |
| 13 | Sicherheitsbestätigung | Alle | Bestätigung |
| 14 | Sicherheitsbroadcast | Alle | Allgemeine Sicherheitsmeldung |
| 15 | Interrogation | Alle | Datenabfrage |
| 16 | Zuweisungsmodus-Befehl | Basisstation | Zeitschlitz-Zuweisung |
| 17 | DGNSS Broadcastnachricht | Basisstation | Differenzkorrekturen |
| 18 | Positionsbericht Klasse B (Standard) | Klasse B | Position, SOG, COG |
| 19 | Erweiterter Positionsbericht Klasse B | Klasse B | Position + Statische Daten |
| 21 | AtoN-Bericht | Seezeichen | Position, Typ, Status |
| 24 | Statischer Datenbericht Klasse B | Klasse B | Name, Typ, Abmessungen |
| 27 | Langstrecken-Positionsbericht | Alle (Satellit) | Position für Satelliten-AIS |

#### 2.6.4 MMSI — Maritime Mobile Service Identity

Die MMSI ist eine weltweit eindeutige 9-stellige Kennung:

| MMSI-Bereich | Verwendung | Beispiel |
|-------------|------------|---------|
| 2XXNNNNNN | Küstenstationen | 211XXXXXX (Deutschland) |
| MIDxxxxxx | Schiffsstationen | 211XXXXXX (Deutschland) |
| 00MIDXXXX | Gruppenruf | 00211XXXX |
| 970XXYYYY | AIS-SART | 970XXYYYY |
| 972XXYYYY | MOB-AIS | 972XXYYYY |
| 974XXYYYY | EPIRB-AIS | 974XXYYYY |

**MID (Maritime Identification Digits) — Ausgewählte Länder:**

| MID | Land | | MID | Land |
|-----|------|-|-----|------|
| 211 | Deutschland | | 226/227 | Frankreich |
| 205 | Belgien | | 230 | Finnland |
| 209 | Zypern | | 231 | Färöer |
| 210 | Tschechien | | 235-237 | Großbritannien |
| 212 | Zypern | | 240 | Griechenland |
| 214 | Georgien | | 244-246 | Niederlande |
| 215 | Malta | | 255 | Portugal |
| 218 | Deutschland | | 256 | Malta |
| 219 | Dänemark | | 257 | Norwegen |
| 220 | Dänemark | | 258 | Barbados |
| 224 | Spanien | | 261 | Polen |
| 225 | Spanien | | 263 | Portugal |

**MMSI-Beantragung in Deutschland:**
- Über die Bundesnetzagentur (BNetzA)
- Voraussetzung: Gültiges UKW-Seefunkzeugnis (SRC, LRC, UBI)
- Wird zusammen mit dem Schiffsfunkstellenzeugnis vergeben
- Kosten: ca. 40–60 EUR

### 2.7 AIS-Antennentechnik

#### 2.7.1 VHF-Antennentypen für AIS

| Typ | Gewinn | Länge | Eignung |
|-----|--------|-------|---------|
| 1 dB (λ/4 Whip) | 1 dBi | 0,25 m | Nur Empfang, Notbehelf |
| 3 dB Standard-VHF | 3 dBi | 0,5–1,0 m | AIS + VHF kombiniert |
| 6 dB Hochgewinn | 6 dBi | 1,2–1,8 m | Motoryachten (stabiler) |
| 8 dB Ultra-Hochgewinn | 8 dBi | 2,0–2,5 m | Nur Motoryachten, sehr stabil |
| Dedizierte AIS-Antenne | 3 dBi | 0,3–0,5 m | Separate AIS-Antenne |

**Empfehlung für Segelyachten:** 3 dB Standard-VHF-Antenne (Krängungskompensation, breiterer Abstrahlwinkel). Bei 6 dB oder 8 dB Antennen wird der vertikale Abstrahlwinkel so eng, dass bei Krängung die Gegenstelle "verloren" geht.

#### 2.7.2 VHF-Splitter vs. Separate Antenne

**VHF-Splitter:**
- Erlaubt gemeinsame Nutzung einer VHF-Antenne für VHF-Funk und AIS
- Spart zweite Antenneninstallation
- Automatische Umschaltung: AIS wird stumm geschaltet wenn VHF sendet
- Einfügungsdämpfung typisch 0,5–1,5 dB
- Preis: 150–400 EUR

**Separate AIS-Antenne:**
- Keine Beeinträchtigung bei VHF-Sendung
- Gleichzeitiger AIS- und VHF-Betrieb möglich
- Zusätzliche Antenneninstallation erforderlich
- Mindestabstand zur VHF-Antenne: 1–2 m
- Empfohlen für Klasse-A-Transponder

**VHF-Splitter-Hersteller:**

| Hersteller | Modell | Kanäle | Preis ca. |
|------------|--------|--------|-----------|
| Vesper Marine | SP160 | VHF + AIS (Rx+Tx) | 250 EUR |
| Shakespeare | AIS-200 | VHF + AIS (Rx+Tx) | 200 EUR |
| Glomex | RA201 | VHF + AIS (Rx+Tx) | 180 EUR |
| Digital Yacht | SPL2000 | VHF + AIS (Rx+Tx) + FM | 300 EUR |
| em-trak | S300 | VHF + AIS (Rx+Tx) | 220 EUR |
| Raymarine | A80190 | VHF + AIS (Rx+Tx) | 200 EUR |

### 2.8 Radar-Clutter und Signalverarbeitung

#### 2.8.1 Clutter-Typen

**Sea Clutter (Seegangsclutter):**
- Radarreflexion von Wellen und Gischt
- Stärker bei rauem Seegang, Wind >15 kn
- Dominiert im Nahbereich (0–3 nm)
- Unterdrückung: STC (Sensitivity Time Control) / Sea Clutter Control
- FMCW-Radare: Doppler-basierte Unterdrückung effektiver

**Rain Clutter (Niederschlagsclutter):**
- Radarreflexion von Regentropfen, Hagel, Schnee
- Kann Ziele in Regenfeldern vollständig maskieren
- X-Band stärker betroffen als S-Band (kürzere Wellenlänge)
- Unterdrückung: FTC (Fast Time Constant) / Rain Clutter Control
- Doppelband-Anlagen (S+X) bieten beste Unterdrückung

**Land Clutter:**
- Radarreflexion von Küstenlinien, Bergen, Gebäuden
- Starke Reflexionen können schwächere Ziele maskieren
- Sidelobes der Antenne erzeugen falsche Landechos
- Unterdrückung: IR (Interference Rejection), Gain-Anpassung

**Bird Clutter:**
- Vogelschwärme erzeugen Radarechos
- Nutzbar als Feature: "Bird Mode" (Garmin) zum Erkennen von Fischschwärmen/Vogelaktivität
- Ansonsten: Doppler-Filter zur Unterdrückung

#### 2.8.2 Digitale Signalverarbeitung

**Moderne Radar-Signalverarbeitungsketten:**

```
Rohsignal → ADC → Pulskompression → Doppler-Filterung
    → CFAR-Detektion → Tracking → Darstellung

CFAR = Constant False Alarm Rate
  - Adaptiert Detektionsschwelle an lokale Störumgebung
  - Verhindert Falschziele durch Clutter
  - Varianten: CA-CFAR, OS-CFAR, GO-CFAR
```

**Herstellerspezifische Verarbeitungsnamen:**

| Hersteller | Bezeichnung | Funktion |
|------------|-------------|----------|
| Garmin | Auto Gain / Auto Sea | Automatische Clutter-Anpassung |
| Simrad | Noise Rejection / Sea State | Automatische Filterung |
| Raymarine | Auto Tune / Harbor Mode | Adaptive Signalverarbeitung |
| Furuno | Fast Target Tracking (FTT) | Beschleunigtes ARPA-Tracking |

---

## 3. Typenübersicht

### 3.1 Radar-Antennentypen

#### 3.1.1 Dome-Radar (Radome / geschlossene Antenne)

**Beschreibung:**
Geschlossene, runde Kunststoffkuppel mit integrierter Schlitzantenne und Sender/Empfänger-Elektronik. Die Kuppel schützt die rotierende Antenne vor Witterung und verhindert Berührung mit laufendem Gut.

**Technische Merkmale:**

| Parameter | Typische Werte |
|-----------|---------------|
| Durchmesser | 18" (45 cm), 24" (61 cm) |
| Strahlbreite horizontal | 4,2°–6,2° |
| Drehzahl | 24–48 U/min |
| Gewicht | 2–12 kg |
| Sendeleistung (Puls) | 2–4 kW Spitze |
| Sendeleistung (Solid-State) | 165 mW–25 W |
| Reichweite (typisch) | 24–48 nm |
| Nahbereich | 6–75 m (typ-abhängig) |

**Vorteile:**
- Kompakt, leicht, geringes Windprofil
- Sicher — keine offenliegenden rotierenden Teile
- Ideal für Segelyachten (unter Baum, am Mast oder Heckkorb)
- Geringere Montage-Anforderungen

**Nachteile:**
- Geringere azimutale Auflösung als Open-Array
- Kleinere Antennenapertur → breiterer Radarstrahl
- Kunststoffkuppel verursacht geringe Signaldämpfung

**Typische Anwendung:**
- Segelyachten 8–15 m
- Motoryachten bis 12 m
- Küsten- und Wochenend-Segler
- Zweitradar auf größeren Yachten

#### 3.1.2 Open-Array (offene Radar-Antenne / Scanner)

**Beschreibung:**
Offene, längliche Schlitzgruppen-Antenne (Slotted Waveguide Array) ohne Schutzverkleidung. Rotiert frei auf dem Sockel. Sendeleistung und Signalverarbeitung teilweise in separater Einheit unter Deck.

**Technische Merkmale:**

| Parameter | Typische Werte |
|-----------|---------------|
| Antennenlänge | 3 ft (0,9 m), 4 ft (1,2 m), 6 ft (1,8 m) |
| Strahlbreite horizontal | 1,0°–2,5° |
| Drehzahl | 24–48 U/min |
| Gewicht | 8–25 kg |
| Sendeleistung (Puls) | 4–25 kW Spitze |
| Sendeleistung (Solid-State) | 25–50 W |
| Reichweite (typisch) | 48–96+ nm |
| Nahbereich | 20–75 m (puls-abhängig) |

**Vorteile:**
- Deutlich bessere azimutale Auflösung
- Höhere Reichweite
- Bessere Zieldiskriminierung (Hafen, enge Gewässer)
- Professionellere Leistung

**Nachteile:**
- Schwerer, größer, höheres Windprofil
- Sicherheitsrisiko durch rotierende Antenne (Sicherheitszone beachten)
- Aufwändigere Montage (Mast-Plattform, Archbogen)
- Höherer Stromverbrauch

**Typische Anwendung:**
- Motoryachten >12 m
- Segelyachten >15 m (Langfahrt)
- Professionelle Fischer
- Superyachten (Primärradar)

#### 3.1.3 Solid-State/Broadband-Radar

**Beschreibung:**
Radar mit Halbleiter-Sender (keine Magnetron-Röhre). Kann als Dome oder Open-Array ausgeführt sein. Nutzt FMCW oder Puls-Kompression.

**Unterscheidungsmerkmale zu Magnetron-Radar:**

| Merkmal | Magnetron (Puls) | Solid-State (FMCW/Kompression) |
|---------|-----------------|-------------------------------|
| Sender | Magnetron-Röhre | GaN/GaAs-Halbleiter |
| Aufwärmzeit | 60–120 s | 0–5 s |
| Mindestentfernung | 25–75 m | 6–20 m |
| Verschleißteil | Magnetron (2.000–5.000 h) | Keines |
| Sendeleistung (Spitze) | 2–25 kW | 0,165–50 W |
| Strahlungsgefahr | Höher (Sicherheitsabstand) | Gering |
| Doppler-Fähigkeit | Nein (Ausnahmen) | Ja |
| Stromverbrauch | 30–200 W | 15–40 W |

### 3.2 AIS-Gerätetypen

#### 3.2.1 AIS Klasse A

**Beschreibung:**
Vollständiger AIS-Transponder gemäß IMO-Spezifikation, Pflichtausstattung für SOLAS-Schiffe. Höchste Sendeleistung und schnellste Berichtsraten.

**Technische Merkmale:**

| Parameter | Wert |
|-----------|------|
| Sendeleistung | 12,5 W |
| Zugangsverfahren | SOTDMA |
| Empfänger | 2× Empfang + 1× Senden |
| Berichtsrate (fahrend) | 2–10 Sekunden |
| Berichtsrate (vor Anker) | 3 Minuten |
| Nachrichtentypen | 1, 2, 3, 5 (+ weitere) |
| Display | Mindestanzeige vorgeschrieben |
| Norm | IEC 61993-2 |
| Preis (Yacht-Modelle) | 1.200–3.500 EUR |

**Vorgeschrieben für:**
- Alle SOLAS-Schiffe (internationale Fahrt >300 BRT, alle >500 BRT)
- Fahrgastschiffe (alle)
- In einigen Ländern: Fischereifahrzeuge >15 m

**Für Yachten relevant wenn:**
- Gewerbliche Yachten (Charter mit Passagieren)
- Yachten >500 BRT (Superyachten)
- Maximale Sichtbarkeit gewünscht (besonders in stark befahrenen Revieren)

#### 3.2.2 AIS Klasse B (Standard / CS)

**Beschreibung:**
Vereinfachter AIS-Transponder für die Sportschifffahrt, entwickelt gemäß IEC 62287-1.

**Technische Merkmale:**

| Parameter | Klasse B (CSTDMA) | Klasse B+ (SOTDMA) |
|-----------|-------------------|---------------------|
| Sendeleistung | 2 W | 5 W |
| Zugangsverfahren | CSTDMA | SOTDMA |
| Empfänger | 2× Empfang + 1× Senden | 2× Empfang + 1× Senden |
| Berichtsrate (fahrend) | 30 s | 5–30 s (geschwindigkeitsabhängig) |
| Berichtsrate (vor Anker) | 3 min | 3 min |
| Nachrichtentypen | 18, 19, 24 | 18, 19, 24 |
| Display | Optional | Optional |
| Norm | IEC 62287-1 | IEC 62287-2 |
| Preis | 200–500 EUR | 400–900 EUR |

**Unterschiede Klasse B vs. Klasse B+:**

| Merkmal | Klasse B (CSTDMA) | Klasse B+ (SOTDMA) |
|---------|-------------------|---------------------|
| Reichweite (typisch) | 5–10 nm | 10–25 nm |
| Sichtbarkeit auf Großschiffen | Eingeschränkt (kann gefiltert werden) | Wie Klasse A |
| Priorität bei Kanalüberlastung | Niedrig (wird verdrängt) | Hoch (garantiert) |
| Statische Daten | Alle 6 min | Alle 6 min |
| Empfang Msg 1-5 | Ja | Ja |
| Senden Sicherheitsmeldungen | Nein | Teilweise |
| Display-Vorschrift | Nein | Nein |

**Empfehlung AYDI:**
- Klasse B+ (SOTDMA, 5W) ist der **Mindeststandard** für Yachten auf See
- Klasse B (CSTDMA, 2W) nur für Binnenreviere oder reinen Küstenbetrieb
- In stark befahrenen Revieren (Englischer Kanal, Malakka-Straße, Singapur) ist Klasse A empfehlenswert

#### 3.2.3 AIS-Empfänger (Receive-Only)

**Beschreibung:**
Reiner Empfänger, kein Senden. Zeigt andere AIS-Teilnehmer an, eigenes Boot bleibt unsichtbar.

**Merkmale:**
- Preis: 80–250 EUR
- Stromverbrauch: 0,5–2 W
- Einfache Installation (nur Antenne + Daten-Anbindung)
- Kein VHF-Splitter nötig (nur Empfang)
- Datenausgabe über NMEA 0183 oder NMEA 2000 / WiFi / USB

**Einsatzgebiet:**
- Nachrüstung auf kleinen Booten
- Zusatz-Empfänger (z.B. für Tablet/Smartphone-Kartenplotter)
- Nicht als alleiniges AIS-System empfohlen (keine Sichtbarkeit!)

#### 3.2.4 AIS-MOB (Man-Over-Board)

**Beschreibung:**
Persönlich getragener AIS-Sender, der bei Aktivierung eine MOB-Alarmmeldung auf AIS sendet.

**Merkmale:**

| Parameter | Wert |
|-----------|------|
| Sendeleistung | 1 W |
| MMSI-Bereich | 972XXXXXXX |
| Nachrichtentyp | Msg 1 (mit MOB-Status) |
| Senderate | Alle 60 Sekunden |
| Batterielaufzeit | 24–96 Stunden |
| Aktivierung | Manuell oder Wasseraktiviert |
| Reichweite | 2–5 nm |
| GPS integriert | Ja (66-Kanal) |
| Preis | 150–350 EUR |
| Norm | IEC 62287-1 Annex G |

> ⚠️ **ZU PRÜFEN (Audit):** Norm-Referenz "IEC 62287-1 Annex G" für AIS-MOB unbelegt — AIS-MOB/MSLD-Geräte werden üblicherweise nach IEC 61097-14 zertifiziert (wie AIS-SART), nicht nach IEC 62287-1 (das die Klasse-B-CSTDMA-Anforderungen definiert). Confidence: estimated — unverifiziert.

**Hersteller:**
- Ocean Signal rescueME MOB1
- ACR Electronics AISLink MOB
- Kannad SafeLink R10
- Vesper Marine Cortex MOB

#### 3.2.5 AIS-SART (Search and Rescue Transponder)

**Beschreibung:**
AIS-basierter Such- und Rettungstransponder, Ersatz/Ergänzung zum Radar-SART.

| Parameter | Wert |
|-----------|------|
| Sendeleistung | 1 W |
| MMSI-Bereich | 970XXXXXXX |
| Nachrichtentyp | Msg 1 (SART-Status) |
| Senderate | Alle 60 Sekunden |
| Batterielaufzeit | >96 Stunden |
| Aktivierung | Manuell |
| GPS | Ja |
| Preis | 250–500 EUR |
| Norm | IEC 61097-14 |

### 3.3 Radar-Overlay

#### 3.3.1 Funktionsprinzip

Radar-Overlay kombiniert das Radarbild mit der elektronischen Seekarte (ENC/Rastercharte) auf dem MFD (Multi-Function Display):

**Voraussetzungen:**
1. Radar und Kartenplotter am gleichen Netzwerk (Ethernet/NMEA)
2. Präziser Heading-Sensor (magnetisch oder Satellit)
3. GPS-Position für georeferenzierte Overlay-Darstellung
4. Kompatible Geräte desselben Herstellers (oder kompatible Drittanbieter)

**Darstellungsmodi:**

| Modus | Orientierung | Vorteil |
|-------|-------------|---------|
| Head-Up | Eigener Kurs = oben | Intuitiv, wie Blick durch Windschutzscheibe |
| North-Up | Nord = oben | Konsistent mit Seekarte |
| Course-Up | COG = oben | Stabil bei Wind/Strom |
| True Motion | Eigenes Schiff bewegt sich | Realistischste Darstellung |

#### 3.3.2 Integrierte Darstellung: Radar + AIS + Chart

Die modernste Overlay-Darstellung kombiniert drei Datenquellen:

1. **Seekarte** als Basislayer — zeigt Küstenlinien, Untiefen, Seezeichen
2. **Radarbild** als transparenter Overlay — zeigt tatsächliche Reflexionen
3. **AIS-Symbole** als Informationslayer — zeigt identifizierte Schiffe mit Daten

**Vorteile der Kombination:**
- Radar-Ziel ohne AIS → möglicherweise kleines Boot, Treibgut, Regen
- AIS-Ziel ohne Radar-Echo → möglicherweise hinter Landmasse, fehlerhafter AIS
- Radar-Echo + AIS-Symbol → sicherer Abgleich, volle Information
- Landmasse auf Karte + Radar-Echo → Kartengenauigkeit verifiziert

**Einschränkungen:**
- Heading-Fehler verursacht Rotations-Offset des Radarbilds
- Timing-Unterschiede: Radar (Echtzeit) vs. AIS (bis 3 min alt)
- Position-Offset bei ungenauen GPS-Daten

---

## 4. Produktlinien und Spezifikationen

### 4.1 Raymarine — Quantum 2 Serie

#### 4.1.1 Übersicht

Raymarine (Teil von FLIR Systems / Teledyne Technologies) hat mit der Quantum-Serie 2014 den Einstieg in Solid-State-CHIRP-Radar für Yachten vollzogen. Die Quantum 2 (2019) ist die aktuelle Evolution.

**Quantum 2 CHIRP-Radar (Q24D):**

| Parameter | Wert |
|-----------|------|
| Typ | Solid-State CHIRP (Puls-Kompression) |
| Bauform | 18" Radome (46 cm) |
| Sendeleistung | 25 W |
| Reichweite max. | 24 nm |
| Mindestentfernung | 6 m |
| Strahlbreite horizontal | 5,2° |
| Strahlbreite vertikal | 25° |
| Drehzahl | 24 / 36 / 48 U/min |
| Stromaufnahme | 17 W (Standby), 22 W (Senden) |
| Gewicht Antenne | 4,9 kg |
| Anschluss | Wi-Fi + Ethernet (RayNet) |
| Doppler | Ja (Farbliche Zielklassifizierung) |
| MARPA | Ja (über kompatibles MFD) |
| Preis | ca. 1.900–2.200 EUR |

**Quantum 2 CHIRP-Radar mit Doppler (Q24C):**

| Parameter | Wert |
|-----------|------|
| Typ | Solid-State CHIRP + Doppler |
| Bauform | 24" Radome (61 cm) |
| Reichweite max. | 48 nm |
| Strahlbreite horizontal | 3,9° |
| Gewicht | 6,3 kg |
| Preis | ca. 2.800–3.200 EUR |

**Besondere Features:**
- **ATX (Advanced Target eXtraction):** Automatische Zielerkennung auch bei starkem Clutter
- **Wi-Fi + Ethernet:** Flexible Vernetzung, auch direkt mit LightHouse-App auf Tablet
- **Quantum Radar Stabilization:** Kompensiert Eigenbewegung bei Seegang
- **RealVision 3D Integration:** Kann auf Axiom-MFDs mit Sonar-Overlay kombiniert werden

#### 4.1.2 Raymarine Magnum Open-Array

Für größere Yachten bietet Raymarine die Magnum-Serie:

| Modell | Antenne | Leistung | Strahlbreite | Gewicht | Preis ca. |
|--------|---------|----------|-------------|---------|-----------|
| Magnum 4 kW | 4 ft Open-Array | 4 kW Puls | 1,8° | 12,5 kg | 3.500 EUR |
| Magnum 12 kW | 4 ft Open-Array | 12 kW Puls | 1,8° | 14,2 kg | 5.500 EUR |
| Magnum 4 ft Solid-State | 4 ft Open-Array | 50 W | 1,8° | 10,5 kg | 6.000 EUR |

### 4.2 Garmin — GMR Fantom Serie

#### 4.2.1 Übersicht

Garmin hat mit der Fantom-Serie ein vollständiges Solid-State-Radar-Portfolio mit Doppler-Technologie aufgebaut.

**Garmin GMR Fantom 18x (Radome):**

| Parameter | Wert |
|-----------|------|
| Typ | Solid-State (Puls-Kompression) |
| Bauform | 18" Radome (46 cm) |
| Sendeleistung | 40 W |
| Reichweite max. | 36 nm |
| Mindestentfernung | 6 m |
| Strahlbreite horizontal | 5,2° |
| Drehzahl | 24 / 36 / 48 U/min |
| Stromaufnahme | 27 W (typisch) |
| Gewicht | 5,4 kg |
| Anschluss | Ethernet (10/100 Mbit) |
| MotionScope (Doppler) | Ja |
| MARPA | Ja |
| Dual Range | Ja |
| Preis | ca. 2.000–2.300 EUR |

**Garmin GMR Fantom 24x (Radome):**

| Parameter | Wert |
|-----------|------|
| Bauform | 24" Radome (61 cm) |
| Sendeleistung | 50 W |
| Reichweite max. | 48 nm |
| Strahlbreite horizontal | 3,7° |
| Gewicht | 7,8 kg |
| Preis | ca. 3.200–3.600 EUR |

**Garmin GMR Fantom 54 / 56 (Open-Array):**

| Modell | Antenne | Leistung | Strahlbreite | Gewicht | Preis ca. |
|--------|---------|----------|-------------|---------|-----------|
| Fantom 54 | 4 ft Open-Array | 50 W | 1,7° | 12,7 kg | 5.500 EUR |
| Fantom 56 | 6 ft Open-Array | 50 W | 1,1° | 17,2 kg | 8.000 EUR |
| Fantom 254/256 | 4/6 ft | 120 W | 1,7°/1,1° | 13/18 kg | 8.000/12.000 EUR |

**Besondere Features:**
- **MotionScope (Doppler):** Sich nähernde Ziele rot, entfernende grün
- **Dual Range:** Gleichzeitig Nah- und Fernbereich anzeigen
- **Automatik Gain/Sea/Rain:** Selbstanpassende Clutter-Unterdrückung
- **Bird Mode:** Vogelschwärme anzeigen (für Sportfischer)
- **Anchor Drag Alert:** Ankerüberwachung via Doppler
- **Echo Trails:** Nachzeichnung der Zielbewegung (konfigurierbar 15 s – 10 min)

### 4.3 Simrad / B&G — Halo Serie

#### 4.3.1 Übersicht

Navico (Simrad, B&G, Lowrance) hat mit der Halo-Serie eine der am längsten etablierten Solid-State-Radar-Linien im Yacht-Segment.

**Simrad Halo20+ (Radome):**

| Parameter | Wert |
|-----------|------|
| Typ | Solid-State (Puls-Kompression) |
| Bauform | 20" Radome (51 cm) |
| Sendeleistung | 25 W |
| Reichweite max. | 36 nm |
| Mindestentfernung | 6 m |
| Strahlbreite horizontal | 5,3° |
| Drehzahl | 20 / 40 / 60 U/min |
| Stromaufnahme | 18 W (typisch) |
| Gewicht | 7,1 kg |
| Anschluss | Ethernet |
| VelocityTrack (Doppler) | Ja |
| MARPA | Ja |
| Dual Range | Ja |
| Preis | ca. 1.800–2.100 EUR |

**Simrad Halo24 (Radome):**

| Parameter | Wert |
|-----------|------|
| Bauform | 24" Radome (61 cm) |
| Sendeleistung | 25 W |
| Reichweite max. | 48 nm |
| Strahlbreite horizontal | 3,9° |
| Gewicht | 8,2 kg |
| Drehzahl | 20 / 40 / 60 U/min |
| Preis | ca. 2.800–3.200 EUR |

**Simrad Halo 3000/4000/6000 (Open-Array):**

| Modell | Antenne | Leistung | Strahlbreite | Gewicht | Preis ca. |
|--------|---------|----------|-------------|---------|-----------|
| Halo 3000 | 3 ft Open-Array | 25 W | 2,3° | 8,4 kg | 4.000 EUR |
| Halo 4000 | 4 ft Open-Array | 25 W | 1,7° | 10,5 kg | 5.500 EUR |
| Halo 6000 | 6 ft Open-Array | 25 W | 1,05° | 16,0 kg | 8.500 EUR |

**B&G Halo20+ / Halo24:**
Identische Hardware wie Simrad, jedoch mit B&G-spezifischer Software:
- **SailSteer-Integration:** Radar-Daten in B&G-Segeldarstellung
- **Regatta-Modus:** Optimiert für Startlinien-Erkennung und Ziel-Tracking unter Segeln

**Besondere Features:**
- **VelocityTrack (Doppler):** Farbliche Darstellung der Ziel-Radialgeschwindigkeit
- **NoDrift-Modus:** Ankerüberwachung
- **Dual Range:** Simultane Nah-/Fernbereichsdarstellung
- **60 U/min Schnell-Sweep:** Beste Update-Rate im Markt für Hafenmanöver
- **ZoneTrack:** Automatische MARPA-Erfassung in definierten Zonen
- **Wetter-Overlay:** Radar-basierte Niederschlagsdarstellung

### 4.4 Furuno — DRS-Serie

#### 4.4.1 Übersicht

Furuno ist der Weltmarktführer im professionellen Schiffsradar und bringt diese Expertise in den Yacht-Bereich ein.

**Furuno DRS4DL+ (Radome):**

| Parameter | Wert |
|-----------|------|
| Typ | Pulsradar (Magnetron) |
| Bauform | 19" Radome (48 cm) |
| Sendeleistung | 4 kW Spitze |
| Reichweite max. | 36 nm |
| Mindestentfernung | 25 m (kurzer Puls) |
| Strahlbreite horizontal | 4,4° |
| Drehzahl | 24 / 36 / 48 U/min |
| Stromaufnahme | 28 W (Senden) |
| Gewicht | 7,7 kg |
| Anschluss | Ethernet |
| ARPA | Ja (bis 30 Ziele) |
| Preis | ca. 1.500–1.800 EUR |

**Furuno DRS-NXT Serie (Solid-State):**

| Modell | Bauform | Leistung | Strahlbreite | Gewicht | Preis ca. |
|--------|---------|----------|-------------|---------|-----------|
| DRS2D-NXT | 19" Radome | 25 W | 4,4° | 5,5 kg | 1.800 EUR |
| DRS4D-NXT | 24" Radome | 25 W | 3,5° | 7,1 kg | 2.500 EUR |
| DRS6A-NXT | 3,5 ft Open-Array | 25 W | 2,4° | 9,5 kg | 4.000 EUR |
| DRS12A-NXT | 4 ft Open-Array | 25 W | 1,8° | 11,0 kg | 5.500 EUR |
| DRS25A-NXT | 6 ft Open-Array | 25 W | 1,05° | 16,5 kg | 9.000 EUR |

**Besondere Features:**
- **Target Analyzer (Doppler):** Sich nähernde/entfernende Ziele farblich markiert
- **Fast Target Tracking (FTT):** ARPA-ähnliches automatisches Tracking, das schneller als konventionelles ARPA arbeitet
- **RezBoost:** Digitale Auflösungsverbesserung durch Puls-Kompression
- **Rain Mode:** Fortschrittliche Regenfilterung für tropische Reviere
- **Bird Mode:** Vogelschwarm-Erkennung
- **ACE (Automatic Clutter Elimination):** KI-gestützte automatische Clutter-Unterdrückung

#### 4.4.2 Furuno Professionelle Radar-Linie (FAR-Serie)

Für Superyachten >30 m relevant:

| Modell | Band | Leistung | Antenne | Besonderheit |
|--------|------|----------|---------|-------------|
| FAR-1513 | X | 12 kW | 4/6 ft | IMO-zugelassen, Vollradar |
| FAR-1523 | X | 25 kW | 4/6/8 ft | IMO, TT mit 100+ Zielen |
| FAR-1518 | S | 30 kW | 6/8/12 ft | S-Band, Regenunterdrückung |
| FAR-2228 | S+X | 25+25 kW | Dual | Duales Band-System |

### 4.5 B&G — Radar für Segler

B&G als Navico-Marke speziell für Segler bietet die Halo-Radare mit seglerspezifischer Software:

**B&G Halo20+ Radar:**
- Identische Hardware zu Simrad Halo20+
- **SailSteer-Integration:** Radar-Overlay in der proprietären Segeldarstellung
- **Startlinien-Funktion:** Hilfe beim Regattastart mit Radar-gestützter Abstandsmessung
- **Wind-Integration:** Korrelation von Radar-Daten mit Wind-Sensoren

**B&G-spezifische Radar-Funktionen:**
- Automatische Guard-Zone-Anpassung bei Kurswechseln
- Wende-/Halsen-Alarme in Kombination mit Radar-Daten
- Layline-Berechnung mit Radar-gestützter Stromerkennung

### 4.6 AIS-Transponder — em-trak

#### 4.6.1 em-trak Produktlinie

em-trak (UK) ist einer der führenden AIS-Spezialisten:

**em-trak B954 (Klasse B+, SOTDMA):**

| Parameter | Wert |
|-----------|------|
| AIS-Klasse | B+ (SOTDMA) |
| Sendeleistung | 5 W |
| Empfänger | 2-Kanal parallel |
| GPS | 72-Kanal intern |
| Anschlüsse | NMEA 0183, NMEA 2000, USB |
| Wi-Fi | Ja |
| Stromaufnahme | 2 W (Empfang), 3,5 W (Senden) |
| Abmessungen | 130 × 110 × 30 mm |
| Gewicht | 280 g |
| Wasserdicht | IPX7 |
| Preis | ca. 600–700 EUR |

**em-trak B100 (Klasse B, CSTDMA):**

| Parameter | Wert |
|-----------|------|
| AIS-Klasse | B (CSTDMA) |
| Sendeleistung | 2 W |
| GPS | 66-Kanal intern |
| Anschlüsse | NMEA 0183, USB |
| Wi-Fi | Nein |
| Preis | ca. 300–400 EUR |

**em-trak A100 (Klasse A):**

| Parameter | Wert |
|-----------|------|
| AIS-Klasse | A (SOTDMA) |
| Sendeleistung | 12,5 W |
| Empfänger | 3 Kanäle (2 Rx + 1 Tx) |
| GPS | 72-Kanal intern |
| Display | Integriert (minimal) |
| NMEA 2000 | Ja |
| Preis | ca. 1.500–2.000 EUR |

**em-trak R300 (Empfänger):**

| Parameter | Wert |
|-----------|------|
| Typ | Dual-Kanal AIS-Empfänger |
| GPS | 72-Kanal intern |
| Anschlüsse | NMEA 0183, NMEA 2000, USB, WiFi |
| Stromaufnahme | 1 W |
| Preis | ca. 200–280 EUR |

**em-trak S300 (VHF-Splitter):**

| Parameter | Wert |
|-----------|------|
| Typ | VHF/AIS-Antennensplitter |
| Durchgangsdämpfung | <0,6 dB |
| Leistung | Bis 50 W VHF-Senden |
| Preis | ca. 200–250 EUR |

### 4.7 Vesper Marine

#### 4.7.1 Vesper Marine Cortex

Vesper Marine (Neuseeland) hat mit dem Cortex ein revolutionäres Hub-Konzept entwickelt:

**Vesper Marine Cortex V1:**

| Parameter | Wert |
|-----------|------|
| Typ | VHF + AIS Klasse B+ + Monitoring Hub |
| VHF | 25 W DSC-fähig |
| AIS | Klasse B+ (SOTDMA, 5 W) |
| GPS | Multi-GNSS (GPS, GLONASS, Galileo) |
| Sensoren | Barometer, Ankerwache, Bilge-Alarm |
| Konnektivität | Wi-Fi, NMEA 2000, NMEA 0183, USB |
| App-Steuerung | Ja (iOS/Android) |
| Monitoring | Fernüberwachung über Cloud |
| Preis | ca. 2.000–2.500 EUR |

**Vesper Marine Cortex M1 (Handset):**
- Fernbedienung für Cortex-Hub
- Vollfarbiges Display
- VHF-Funkbedienung
- AIS-Zielanzeige
- Preis: ca. 500 EUR (zusätzlich)

**Vesper Marine XB-8000 (AIS-Transponder):**

| Parameter | Wert |
|-----------|------|
| AIS-Klasse | B (CSTDMA, 2 W) |
| GPS | 50-Kanal |
| Anschlüsse | NMEA 0183, USB |
| Wi-Fi | Ja |
| Ankerwache | Ja (integriert) |
| Preis | ca. 350–450 EUR |

**Vesper Marine WatchMate Vision2:**

| Parameter | Wert |
|-----------|------|
| Typ | AIS-Transponder mit Display |
| AIS-Klasse | B (CSTDMA, 2 W) |
| Display | 5" Farb-Touchscreen |
| Kartenanzeige | Ja (integriert) |
| NMEA | 0183, USB |
| Wi-Fi | Ja |
| Preis | ca. 800–1.000 EUR |

### 4.8 Spezifikationsvergleich — Radar-Übersicht

#### 4.8.1 Dome-Radar Vergleich

| Modell | Typ | Leistung | Strahlbreite | Mindestentf. | Doppler | Gewicht | Preis ca. |
|--------|-----|----------|-------------|-------------|---------|---------|-----------|
| Raymarine Q24D | SS CHIRP | 25 W | 5,2° | 6 m | Ja | 4,9 kg | 2.000 EUR |
| Raymarine Q24C | SS CHIRP | 25 W | 3,9° | 6 m | Ja | 6,3 kg | 3.000 EUR |
| Garmin Fantom 18x | SS PC | 40 W | 5,2° | 6 m | Ja | 5,4 kg | 2.200 EUR |
| Garmin Fantom 24x | SS PC | 50 W | 3,7° | 6 m | Ja | 7,8 kg | 3.400 EUR |
| Simrad Halo20+ | SS PC | 25 W | 5,3° | 6 m | Ja | 7,1 kg | 2.000 EUR |
| Simrad Halo24 | SS PC | 25 W | 3,9° | 6 m | Ja | 8,2 kg | 3.000 EUR |
| Furuno DRS2D-NXT | SS PC | 25 W | 4,4° | 8 m | Ja | 5,5 kg | 1.800 EUR |
| Furuno DRS4D-NXT | SS PC | 25 W | 3,5° | 8 m | Ja | 7,1 kg | 2.500 EUR |
| Furuno DRS4DL+ | Magnetron | 4 kW | 4,4° | 25 m | Nein | 7,7 kg | 1.600 EUR |

*SS = Solid-State, PC = Puls-Kompression*

#### 4.8.2 Open-Array-Radar Vergleich

| Modell | Antenne | Typ | Leistung | Strahlbreite | Doppler | Gewicht | Preis ca. |
|--------|---------|-----|----------|-------------|---------|---------|-----------|
| Garmin Fantom 54 | 4 ft | SS | 50 W | 1,7° | Ja | 12,7 kg | 5.500 EUR |
| Garmin Fantom 56 | 6 ft | SS | 50 W | 1,1° | Ja | 17,2 kg | 8.000 EUR |
| Simrad Halo 3000 | 3 ft | SS | 25 W | 2,3° | Ja | 8,4 kg | 4.000 EUR |
| Simrad Halo 4000 | 4 ft | SS | 25 W | 1,7° | Ja | 10,5 kg | 5.500 EUR |
| Simrad Halo 6000 | 6 ft | SS | 25 W | 1,05° | Ja | 16,0 kg | 8.500 EUR |
| Furuno DRS6A-NXT | 3,5 ft | SS | 25 W | 2,4° | Ja | 9,5 kg | 4.000 EUR |
| Furuno DRS12A-NXT | 4 ft | SS | 25 W | 1,8° | Ja | 11,0 kg | 5.500 EUR |
| Raymarine Magnum SS | 4 ft | SS | 50 W | 1,8° | Nein | 10,5 kg | 6.000 EUR |

---

## 5. Hersteller-Datenbank

### 5.1 Raymarine (Teledyne FLIR)

| Feld | Detail |
|------|--------|
| **Vollständiger Name** | Raymarine (Teledyne FLIR LLC) |
| **Gründung** | 1923 (als Raytheon Marine) |
| **Hauptsitz** | Fareham, Hampshire, Großbritannien |
| **Muttergesellschaft** | Teledyne Technologies (seit 2021) |
| **Kernkompetenz** | Marine-Elektronik, MFD, Radar, Autopiloten, Kameras |
| **Radar-Linie** | Quantum 2 (Solid-State), Magnum (Puls + SS) |
| **AIS** | Integriert in MFDs, externe Module |
| **MFD-Ökosystem** | Axiom-Serie (LightHouse OS) |
| **Netzwerk** | RayNet (Ethernet), SeaTalkng (NMEA 2000) |
| **Support** | Weltweit, starkes Händlernetz in Europa |
| **AYDI-Relevanz** | Breit aufgestellt, gutes Preis-Leistungs-Verhältnis, starke Kartenintegration |
| **Website** | raymarine.com |

### 5.2 Garmin

| Feld | Detail |
|------|--------|
| **Vollständiger Name** | Garmin Ltd. |
| **Gründung** | 1989 |
| **Hauptsitz** | Olathe, Kansas, USA (Holding: Schaffhausen, Schweiz) |
| **Kernkompetenz** | GPS/GNSS, Outdoor, Aviation, Marine, Automotive |
| **Radar-Linie** | GMR Fantom (Solid-State), GMR xHD2/3 (Magnetron, auslaufend) |
| **AIS** | Integriert in GPSMAP-MFDs, GDL 52/52R AIS-Empfänger, AIS 800 Transponder |
| **MFD-Ökosystem** | GPSMAP-Serie (8400/8600/9000-Serie) |
| **Netzwerk** | Garmin Marine Network (Ethernet), NMEA 2000 |
| **Support** | Ausgezeichneter Kundendienst, weltweites Netz |
| **AYDI-Relevanz** | Technologieführer Doppler-Radar, sehr gute Automatik-Funktionen |
| **Website** | garmin.com |

### 5.3 Navico (Simrad / B&G / Lowrance)

| Feld | Detail |
|------|--------|
| **Vollständiger Name** | Navico Group (Brunswick Corporation) |
| **Gründung** | Simrad (1946), B&G (1956), Lowrance (1957) |
| **Hauptsitz** | Egersund, Norwegen (Simrad), Romsey, UK (B&G) |
| **Muttergesellschaft** | Brunswick Corporation (seit 2021) |
| **Kernkompetenz** | Simrad: Motorboot/Pro, B&G: Segel, Lowrance: Fischerei |
| **Radar-Linie** | Halo-Serie (Solid-State) für alle drei Marken |
| **AIS** | NAIS-400 (Klasse B), NAISo-500 (Klasse B+), AI50 |
| **MFD-Ökosystem** | Simrad NSX/NSO, B&G Zeus/Vulcan, Lowrance HDS |
| **Netzwerk** | Ethernet, NMEA 2000 (SimNet-Adapter) |
| **Support** | Gut in Europa, stark in Skandinavien |
| **AYDI-Relevanz** | Beste Segler-Integration (B&G), höchste Sweep-Rate (60 U/min) |
| **Website** | simrad-yachting.com / bandg.com |

### 5.4 Furuno

| Feld | Detail |
|------|--------|
| **Vollständiger Name** | Furuno Electric Co., Ltd. |
| **Gründung** | 1938 |
| **Hauptsitz** | Nishinomiya, Japan |
| **Kernkompetenz** | Professionelle Schiffselektronik, Fischereisonar, Radar |
| **Radar-Linie** | DRS-NXT (Solid-State), DRS (Magnetron), FAR (Professionell) |
| **AIS** | FA-170 (Klasse A), FA-50 (Klasse B) |
| **MFD-Ökosystem** | NavNet TZtouch3 (TZT-Serie) |
| **Netzwerk** | Ethernet, NMEA 2000, CAN-Bus |
| **Support** | Sehr gut, besonders in Asien und kommerzieller Schifffahrt |
| **AYDI-Relevanz** | Professionellste Radartechnik, beste ARPA-Implementation, Langlebigkeit |
| **Website** | furuno.com |

### 5.5 em-trak

| Feld | Detail |
|------|--------|
| **Vollständiger Name** | em-trak Marine Electronics Ltd. |
| **Gründung** | 2007 |
| **Hauptsitz** | London, Großbritannien |
| **Kernkompetenz** | AIS-Transponder, AIS-Zubehör |
| **Produktlinie** | A100 (Klasse A), B954 (Klasse B+), B100 (Klasse B), R300 (Empfänger), S300 (Splitter) |
| **Besonderheit** | Reiner AIS-Spezialist, sehr kompakte Geräte |
| **Support** | Global, guter Online-Support |
| **AYDI-Relevanz** | Preis-Leistungs-Tipp für AIS-Nachrüstung, breites Portfolio |
| **Website** | em-trak.com |

### 5.6 Vesper Marine

| Feld | Detail |
|------|--------|
| **Vollständiger Name** | Vesper Marine Ltd. |
| **Gründung** | 2007 |
| **Hauptsitz** | Auckland, Neuseeland |
| **Muttergesellschaft** | Unabhängig |
| **Kernkompetenz** | AIS, Remote-Monitoring, integrierte Kommunikation |
| **Produktlinie** | Cortex (VHF+AIS+Hub), XB-8000 (AIS-B), WatchMate Vision2 |
| **Besonderheit** | Innovativstes AIS-Konzept (Cortex = VHF+AIS+Monitoring+App) |
| **Support** | Gut, starke App-Community |
| **AYDI-Relevanz** | Zukunftsweisendes Hub-Konzept, beste App-Integration, Ankerwache |
| **Website** | vfrspermarine.com |

### 5.7 Digital Yacht

| Feld | Detail |
|------|--------|
| **Vollständiger Name** | Digital Yacht Ltd. |
| **Gründung** | 2009 |
| **Hauptsitz** | Hampshire, Großbritannien |
| **Kernkompetenz** | AIS, NMEA-WiFi-Server, Navigation-Server |
| **Produktlinie** | AIT5000 (Klasse B+), AIT2500 (Klasse B), iKommunicate (NMEA-Server) |
| **Besonderheit** | Starke NMEA-WiFi-Integration, Tablet-Navigation |
| **AYDI-Relevanz** | Gute Nachrüstlösungen, WiFi-Vernetzung |
| **Website** | digitalyacht.co.uk |

### 5.8 Weitere relevante Hersteller

| Hersteller | Sitz | Kernprodukt | Preis-Segment |
|------------|------|-------------|--------------|
| ICOM | Japan | VHF+AIS-Kombigeräte (IC-M510BB) | Mittel |
| Standard Horizon | Japan | VHF+AIS-Kombigeräte (GX6500) | Mittel |
| Ocean Signal | UK | AIS-MOB, EPIRB | Sicherheit |
| ACR Electronics | USA | AIS-MOB, PLB, EPIRB | Sicherheit |
| Kannad (Orolia) | Frankreich | AIS-SART, EPIRB | Sicherheit |
| True Heading | Schweden | AIS Klasse B+, Graphene-Serie | Mittel-Hoch |
| McMurdo (Orolia) | UK | AIS-SART, EPIRB, Distress | Sicherheit |

---

## 6. Fehlerbild-Atlas

### 6.1 Fehlerbild: Radar zeigt keine Ziele (Blindheit)

| Feld | Detail |
|------|--------|
| **Bezeichnung** | Radar-Blindheit — keine Zieldarstellung |
| **Symptom** | Display zeigt nur Grundrauschen oder leeres Bild, keine Echos |
| **Confidence** | visual_medium (Bildschirmfoto), measured (Signalanalyse) |
| **Mögliche Ursachen** | 1. Magnetron defekt (Pulsradar) — häufigste Ursache bei älteren Geräten |
|  | 2. Antennenkabel defekt/Wassereinbruch in Stecker |
|  | 3. Sende-Endstufe defekt (Solid-State) |
|  | 4. Antenne dreht nicht (Motor/Riemen defekt) |
|  | 5. Gain auf Minimum eingestellt |
|  | 6. Frequenz-Drift bei Magnetron (außerhalb Empfänger-Bandbreite) |
| **Diagnose** | Gain manuell erhöhen → Rauschen sichtbar? Wenn nein: Empfänger-Problem. Antennendrehung prüfen. Magnetron-Betriebsstunden prüfen (>4.000 h kritisch). |
| **Behebung** | Magnetron-Austausch (Fachbetrieb), Kabelprüfung, Stecker reinigen/ersetzen |
| **AYDI-Scoring** | Kritisch (Safety-relevant) — confidence: measured wenn Signalanalyse, visual_medium bei Bildschirmfoto |

### 6.2 Fehlerbild: Sektorblindheit (Radarschatten)

| Feld | Detail |
|------|--------|
| **Bezeichnung** | Sektorielle Blindheit — Radarschatten |
| **Symptom** | In bestimmten Richtungen fehlen Echos, während in anderen Richtungen alles normal erscheint |
| **Confidence** | visual_high (klar erkennbar im Radarbild) |
| **Mögliche Ursachen** | 1. Mast, Schornstein, Aufbauten im Strahlweg |
|  | 2. Segelfläche (bei Segelschiffen) blockiert Signal |
|  | 3. Radome-Gehäuse beschädigt/Riss |
|  | 4. Antennenmontage zu niedrig hinter Hindernissen |
| **Diagnose** | Blind-Sektor kartieren (auf leerer See drehen), mit Aufbauplan abgleichen |
| **Behebung** | Antenne höher montieren, Montageposition versetzen, Sektorblindheit dokumentieren und im Radar markieren |
| **AYDI-Scoring** | Hoch (eingeschränkte Sicherheit) — confidence: visual_high |

### 6.3 Fehlerbild: Übermäßiges Seegangsclutter

| Feld | Detail |
|------|--------|
| **Bezeichnung** | Seegangsclutter maskiert Ziele im Nahbereich |
| **Symptom** | Nahbereich (0–2 nm) durchgehend hell, kleine Ziele nicht erkennbar |
| **Confidence** | visual_medium |
| **Mögliche Ursachen** | 1. Sea-Clutter-Regler (STC) nicht korrekt eingestellt |
|  | 2. Antenne zu niedrig montiert (viel Wellenreflexion) |
|  | 3. Automatik-Funktion versagt bei extremen Bedingungen |
|  | 4. Veraltete Software ohne adaptive Filterung |
| **Diagnose** | Sea-Clutter manuell anpassen, automatische Filterung deaktivieren und manuell testen |
| **Behebung** | Manuelle STC-Einstellung trainieren, Software aktualisieren, bei chronischem Problem Antenne erhöhen |
| **AYDI-Scoring** | Hoch — confidence: visual_medium |

### 6.4 Fehlerbild: Falsche Echos (Geisterbilder/Sidelobes)

| Feld | Detail |
|------|--------|
| **Bezeichnung** | Falsche Radar-Echos durch Nebenkeulen oder Mehrwegausbreitung |
| **Symptom** | Zusätzliche Echos neben dem realen Ziel, typisch bogenförmig oder gespiegelt |
| **Confidence** | visual_medium |
| **Mögliche Ursachen** | 1. Sidelobe-Echos: starke Ziele (Brücken, Klippen) erzeugen Echos in Nebenkeulen |
|  | 2. Mehrwegausbreitung: Signal reflektiert an eigener Aufbauten |
|  | 3. Indirekter Weg: Signal → Ziel → eigener Mast → Empfänger |
|  | 4. Second-Trace-Echos: Signal von vorherigem Sendepuls |
| **Diagnose** | Entfernungsbereich ändern — falsche Echos verschwinden bei bestimmten Bereichen, echte bleiben |
| **Behebung** | IR (Interference Rejection) aktivieren, Gain reduzieren bei starken Zielen, Sidelobe-Unterdrückung kalibrieren |
| **AYDI-Scoring** | Mittel — confidence: visual_medium |

### 6.5 Fehlerbild: Radar-Interferenz (Spiralmuster)

| Feld | Detail |
|------|--------|
| **Bezeichnung** | Radar-zu-Radar-Interferenz |
| **Symptom** | Spiralförmige oder strahlenförmige Störmuster im Radarbild |
| **Confidence** | visual_high (eindeutiges Muster) |
| **Mögliche Ursachen** | 1. Anderes Radar in der Nähe sendet auf ähnlicher Frequenz |
|  | 2. Eigenes Zweitradar (bei Dual-Installation) |
|  | 3. Küstenradar-Station in der Nähe |
| **Diagnose** | IR (Interference Rejection) einschalten — Muster sollte verschwinden |
| **Behebung** | IR dauerhaft aktivieren (empfohlen), bei Dual-Installation Trigger-Synchronisation prüfen |
| **AYDI-Scoring** | Niedrig (einfach behebbar) — confidence: visual_high |

### 6.6 Fehlerbild: AIS empfängt keine Ziele

| Feld | Detail |
|------|--------|
| **Bezeichnung** | AIS-Empfangsausfall |
| **Symptom** | Keine AIS-Ziele auf dem Kartenplotter, obwohl bekannte AIS-Sender in der Nähe |
| **Confidence** | measured (Signalpegel-Analyse) |
| **Mögliche Ursachen** | 1. VHF-Antenne nicht angeschlossen oder defektes Kabel |
|  | 2. VHF-Splitter defekt oder falsch verkabelt |
|  | 3. NMEA-Verbindung zum Plotter unterbrochen |
|  | 4. AIS-Empfänger defekt |
|  | 5. Falscher NMEA-Port oder Baudrate am Plotter |
|  | 6. Starke lokale Störstrahlung (z.B. LED-Beleuchtung, Ladegerät) |
| **Diagnose** | USB an Laptop anschließen und mit AIS-Dekoder-Software prüfen. VHF-Splitter-LED prüfen. NMEA-Daten auf Terminal auslesen. |
| **Behebung** | Kabelverbindungen prüfen, Splitter-Verkabelung korrigieren, NMEA-Konfiguration am Plotter prüfen |
| **AYDI-Scoring** | Kritisch — confidence: measured |

### 6.7 Fehlerbild: AIS sendet nicht (eigenes Schiff unsichtbar)

| Feld | Detail |
|------|--------|
| **Bezeichnung** | AIS-Sendeausfall — eigenes Schiff nicht auf anderen AIS-Geräten sichtbar |
| **Symptom** | Andere Schiffe empfangen, aber eigenes Boot erscheint nicht auf deren AIS |
| **Confidence** | measured |
| **Mögliche Ursachen** | 1. VHF-Splitter schaltet nicht korrekt um (blockiert AIS-Senden) |
|  | 2. Antenne defekt / SWR zu hoch |
|  | 3. MMSI nicht programmiert |
|  | 4. GPS-Position nicht verfügbar → AIS sendet nicht |
|  | 5. Transponder im "Silent Mode" (Rx-only) |
|  | 6. Transponder-Endstufe defekt |
| **Diagnose** | Auf MarineTraffic.com oder VesselFinder.com eigene MMSI suchen. Transponder-Status-LED prüfen. GPS-Fix-Anzeige prüfen. |
| **Behebung** | Silent Mode deaktivieren, MMSI korrekt eingeben, GPS-Antenne prüfen/extern anbinden, Splitter testen |
| **AYDI-Scoring** | Kritisch (Sicherheit!) — confidence: measured |

### 6.8 Fehlerbild: Radar-Overlay versetzt

| Feld | Detail |
|------|--------|
| **Bezeichnung** | Radar-Overlay auf Seekarte versetzt |
| **Symptom** | Radarechos von Land stimmen nicht mit Kartenküstenlinie überein, Rotation oder Versatz |
| **Confidence** | visual_high |
| **Mögliche Ursachen** | 1. Heading-Sensor nicht kalibriert (häufigste Ursache!) |
|  | 2. Radar-Bearing-Offset nicht justiert |
|  | 3. GPS-Position ungenau oder mit Latenz |
|  | 4. Antennenmontage asymmetrisch zur Schiffslängsachse |
|  | 5. Kartengenauigkeit mangelhaft (alte Karten) |
| **Diagnose** | Heading-Sensor-Wert mit Kompass/GPS-COG vergleichen. Radar-Bild bei bekannter Landmarke mit Karte abgleichen. Bearing-Offset in Radareinstellungen justieren. |
| **Behebung** | Heading-Sensor-Kalibrierung durchführen (Deviationsausgleich), Radar Bearing-Offset einstellen, GPS-Antenne nahe Radar für geringen Positionsversatz |
| **AYDI-Scoring** | Hoch — confidence: visual_high |

### 6.9 Fehlerbild: MARPA-Werte springen / ungenau

| Feld | Detail |
|------|--------|
| **Bezeichnung** | MARPA-Tracking instabil — CPA/TCPA-Werte schwanken stark |
| **Symptom** | MARPA-Vektoren drehen sich, CPA wechselt ständig, Fehlalarme |
| **Confidence** | visual_medium |
| **Mögliche Ursachen** | 1. Heading-Sensor ungenau oder mit hoher Latenz |
|  | 2. GPS-Position springt (Multipath in Hafennähe) |
|  | 3. Schwaches Radarziel → Tracking verliert Ziel temporär |
|  | 4. Eigenes Manöver während Tracking |
|  | 5. Seegang zu stark → Zielecho schwankt in Position |
| **Diagnose** | Heading-Sensor-Typ prüfen (Fluxgate vs. Satellitenkompass). Rate-Gyro-Output prüfen. MARPA nur bei stabilem Kurs nutzen. |
| **Behebung** | Auf Satellitenkompass upgraden (Heading-Genauigkeit <0,5°), MARPA-Parameter (Smoothing) anpassen, Mindest-Tracking-Zeit abwarten |
| **AYDI-Scoring** | Mittel — confidence: visual_medium |

### 6.10 Fehlerbild: Radome dreht nicht

| Feld | Detail |
|------|--------|
| **Bezeichnung** | Radar-Antenne dreht nicht mehr |
| **Symptom** | Display zeigt "No Rotation" oder "Antenna Fault", keine Bilderneuerung |
| **Confidence** | measured |
| **Mögliche Ursachen** | 1. Motor defekt (Lager verschlissen, Spule durchgebrannt) |
|  | 2. Riemen gerissen (bei Riemenantrieb) |
|  | 3. Antenne mechanisch blockiert (Eiszapfen, verklemmtes Teil, Vogelkot) |
|  | 4. Stromversorgung Antenne unterbrochen |
|  | 5. Steuerplatine in Antenne defekt |
| **Diagnose** | Radome öffnen, manuelle Drehbarkeit prüfen. Spannungsversorgung am Antennensockel messen. Motor-Widerstand prüfen. |
| **Behebung** | Motor/Riemen tauschen (Fachbetrieb), mechanische Blockade entfernen, Kabelverbindungen prüfen |
| **AYDI-Scoring** | Kritisch — confidence: measured |

### 6.11 Fehlerbild: AIS zeigt falsche Position

| Feld | Detail |
|------|--------|
| **Bezeichnung** | AIS-Position des eigenen oder fremden Schiffes fehlerhaft |
| **Symptom** | Eigene Position auf MarineTraffic an Land oder versetzt; oder andere Schiffe an falscher Position |
| **Confidence** | measured |
| **Mögliche Ursachen (eigene Position)** | 1. GPS-Antenne ohne Empfang (unter Deck, Abschattung) |
|  | 2. GPS-Position übernommen, aber veraltet |
|  | 3. AIS-Antennenoffset falsch programmiert (GPS → AIS-Antenne Abstand) |
| **Mögliche Ursachen (fremde Position)** | 1. Fremdes Schiff hat GPS-Probleme (häufig!) |
|  | 2. AIS-Nachricht durch Übertragungsfehler korrumpiert |
|  | 3. Spoofing (selten, aber möglich in Krisengebieten) |
| **Diagnose** | Eigene GPS-Position mit Kartenplotter vergleichen. Interne vs. externe GPS-Quelle prüfen. |
| **Behebung** | Externe GPS-Antenne mit freier Sicht anschließen, Antennen-Offset korrekt eintragen |
| **AYDI-Scoring** | Hoch — confidence: measured |

### 6.12 Fehlerbild: EMV-Störungen durch Radar

| Feld | Detail |
|------|--------|
| **Bezeichnung** | Elektromagnetische Interferenz (EMI) durch Radar-Betrieb |
| **Symptom** | Störungen in VHF-Funk, AIS, GPS, Windmesser, Autopilot bei Radar-Sendung |
| **Confidence** | measured |
| **Mögliche Ursachen** | 1. Radar-Antenne zu nahe an VHF/GPS/Wind-Sensoren |
|  | 2. Unzureichende Schirmung der Signalkabel |
|  | 3. Erdungskonzept fehlerhaft |
|  | 4. Magnetron-Oberwellen (bei Pulsradar) |
|  | 5. Beschädigte Radome-Dichtung → Feuchte in Elektronik |
| **Diagnose** | Radar ein/aus schalten und andere Systeme beobachten. Abstände messen. Kabelschirmung prüfen. |
| **Behebung** | Mindestabstände einhalten (Radar zu GPS: >1 m, zu VHF: >1,5 m, zu Kompass: >2 m), Kabel mit Ferritkernen versehen, Erdungskonzept überarbeiten |
| **AYDI-Scoring** | Hoch — confidence: measured |

---

## 7. Troubleshooting-Entscheidungsbäume

### 7.1 Entscheidungsbaum: Radar zeigt keine Ziele

```
START: Radar zeigt keine Ziele
│
├── Ist das Display eingeschaltet und Radar im "Transmit"-Modus?
│   ├── NEIN → Display einschalten, Radar auf "Transmit" stellen → PRÜFEN
│   └── JA ↓
│
├── Dreht sich die Antenne? (Radome: Summgeräusch hörbar?)
│   ├── NEIN → Siehe Entscheidungsbaum 7.5 "Antenne dreht nicht"
│   └── JA ↓
│
├── Ist Rauschen auf dem Bildschirm sichtbar (bei Gain auf Maximum)?
│   ├── NEIN → Empfänger defekt ODER Antennenkabel unterbrochen
│   │         → Antennenkabel prüfen (Ohm-Messung, Wassereinbruch)
│   │         → Empfänger-Einheit prüfen lassen (Fachbetrieb)
│   └── JA → Sender arbeitet nicht korrekt ↓
│
├── Pulsradar oder Solid-State?
│   ├── PULSRADAR → Magnetron-Betriebsstunden prüfen
│   │   ├── >4.000 h → Wahrscheinlich Magnetron verschlissen → Tausch
│   │   └── <4.000 h → Hochspannung am Magnetron messen (FACHBETRIEB!)
│   │                  → Modulator/Trigger-Schaltung prüfen
│   └── SOLID-STATE → Firmware-Version prüfen und aktualisieren
│       → Factory Reset durchführen
│       → Endstufe defekt → Service-Center
│
├── Ist die Aufwärmzeit abgelaufen? (nur Magnetron: 60-120 s)
│   ├── NEIN → Warten bis Aufwärmung abgeschlossen
│   └── JA → Software-Reset, dann erneut prüfen
│
└── LÖSUNG NICHT GEFUNDEN → Hersteller-Service kontaktieren
    Dokumentieren: Modell, FW-Version, Betriebsstunden, Symptome, Fotos
```

### 7.2 Entscheidungsbaum: AIS empfängt/sendet nicht

```
START: AIS-Problem (Empfang und/oder Sendung)
│
├── Empfängt das AIS-Gerät Ziele?
│   ├── JA → Nur Sende-Problem → Springe zu "Sende-Diagnose" unten
│   └── NEIN → Empfangs-Problem ↓
│
├── Leuchtet die "Antenna/Status"-LED am AIS-Gerät?
│   ├── NEIN → Gerät hat keinen Strom oder ist defekt
│   │         → Spannungsversorgung prüfen (12V ±10%)
│   │         → Sicherung prüfen
│   └── JA ↓
│
├── Ist die VHF-Antenne angeschlossen?
│   ├── NEIN → Anschließen → PRÜFEN
│   └── JA ↓
│
├── Wird ein VHF-Splitter verwendet?
│   ├── JA → Splitter-LED prüfen (zeigt aktiv an?)
│   │   ├── NEIN → Splitter defekt oder Verkabelung falsch
│   │   │         → Antenne direkt an AIS anschließen (Test ohne Splitter)
│   │   └── JA → Splitter-Durchgangsdämpfung messen
│   │           → Kabelverbindungen am Splitter prüfen
│   └── NEIN (separate Antenne) → Kabel und Stecker prüfen
│       → Antenne auf Korrosion/Beschädigung prüfen
│
├── Werden NMEA-Daten am Plotter empfangen?
│   ├── NEIN → NMEA-Kabel prüfen (0183: Tx/Rx richtig? 2000: Backbone OK?)
│   │         → Baudrate prüfen (38.400 für AIS über NMEA 0183)
│   │         → Port-Zuordnung am Plotter prüfen
│   └── JA → AIS-Gerät empfängt, aber Plotter zeigt keine Symbole
│           → AIS-Anzeige am Plotter aktiviert? (Einstellungen prüfen)
│           → AIS-Filter prüfen (Entfernungsfilter, Klasse-B-Filter)
│
├── === SENDE-DIAGNOSE ===
│   ├── Ist MMSI programmiert?
│   │   ├── NEIN → MMSI eingeben → PRÜFEN
│   │   └── JA ↓
│   ├── Hat das Gerät GPS-Fix?
│   │   ├── NEIN → GPS-Antenne prüfen / externe GPS-Quelle anbinden
│   │   └── JA ↓
│   ├── Ist "Silent Mode" / "Rx-Only" aktiviert?
│   │   ├── JA → Deaktivieren → PRÜFEN
│   │   └── NEIN ↓
│   ├── Tx-LED blinkt beim Senden?
│   │   ├── NEIN → Endstufe defekt → Service-Center
│   │   └── JA → SWR der Antenne zu hoch → Antennensystem prüfen
│   │           → Auf MarineTraffic.com prüfen ob MMSI erscheint
│
└── LÖSUNG NICHT GEFUNDEN → Hersteller-Support kontaktieren
```

### 7.3 Entscheidungsbaum: Radar-Overlay stimmt nicht mit Karte überein

```
START: Radar-Overlay versetzt/verdreht
│
├── Ist der Versatz ein reiner Rotationsfehler (Bild gedreht)?
│   ├── JA → Heading-Sensor-Problem ↓
│   │   ├── Heading-Wert am MFD mit Handpeilkompass vergleichen
│   │   ├── Abweichung >3°?
│   │   │   ├── JA → Heading-Sensor-Kalibrierung durchführen
│   │   │   │       → Bei Fluxgate: Deviationsausgleich (Drehkreis fahren)
│   │   │   │       → Bei Satellitenkompass: Antennenabstand/Ausrichtung prüfen
│   │   │   └── NEIN → Radar Bearing-Offset in Radareinstellungen justieren
│   │   │             (2°–3° Abweichung können normal sein)
│   │   └── Heading-Sensor-Typ prüfen:
│   │       ├── Fluxgate → Empfindlich gegen Metall, E-Motoren
│   │       │              Min. 1m Abstand zu Eisen/Strom
│   │       ├── Satellitenkompass → Prüfe ob beide Antennen freie Sicht haben
│   │       └── Rate-Gyro-Compass → Initialisierung abwarten (5-15 min)
│   │
│   └── NEIN → Positionsversatz (Bild verschoben) ↓
│
├── Ist der Versatz ein Parallelversatz (gleichmäßig)?
│   ├── JA → GPS-Position-Problem
│   │   ├── GPS-Antenne Position prüfen (freie Sicht?)
│   │   ├── WAAS/EGNOS/MSAS aktiviert?
│   │   ├── GPS-Antennen-Offset im Plotter korrekt eingegeben?
│   │   └── Kartengenauigkeit prüfen (besonders ältere Raster-Karten)
│   └── NEIN → Unterschiedlicher Versatz in verschiedenen Richtungen
│       → Radar-Antennen-Montageposition vs. GPS-Position prüfen
│       → Offsets in Radareinstellungen korrekt eintragen
│       → Timing-Problem: Radar + GPS verschiedene Update-Raten
│
└── ERGEBNIS:
    ├── Heading-Offset >5° → Heading-Sensor tauschen/reparieren
    ├── Heading-Offset 2–5° → Kalibrieren + Radar-Bearing-Offset
    ├── Position-Offset >50m → GPS-Problem beheben
    └── Position-Offset <50m → Normal für Yacht-Installationen
```

### 7.4 Entscheidungsbaum: MARPA/Tracking instabil

```
START: MARPA-Ziele springen / ungenau
│
├── Springt nur EIN Ziel oder ALLE Ziele?
│   ├── EIN Ziel → Ziel-spezifisches Problem
│   │   ├── Schwaches Radarziel? (kleines Boot, GFK)
│   │   │   ├── JA → MARPA verliert Ziel temporär → Normal bei schwachen Zielen
│   │   │   │       → Gain leicht erhöhen, kürzere Distanz wählen
│   │   │   └── NEIN → Ziel macht häufige Kursänderungen
│   │   │               → Tracking braucht 3+ Umdrehungen nach Manöver
│   │   └── Ziel in Clutter-Zone? (Nahe Land, Wellen)
│   │       ├── JA → Clutter-Unterdrückung anpassen, manuelles Tracking bevorzugen
│   │       └── NEIN → Ziel erneut erfassen (Clear + Re-Acquire)
│   │
│   └── ALLE Ziele → Systemisches Problem ↓
│
├── Fährt das eigene Boot geradeaus?
│   ├── NEIN (Manöver) → MARPA wird bei Kursänderung ungenau → Normal!
│   │   → Nach Kursänderung 2-3 Minuten warten bis stabil
│   └── JA ↓
│
├── Heading-Sensor-Qualität prüfen:
│   ├── Heading-Wert stabil? (±1° bei ruhiger See)
│   │   ├── NEIN → Heading-Sensor-Problem → Siehe Baum 7.3
│   │   └── JA ↓
│   ├── Heading-Sensor-Typ?
│   │   ├── Fluxgate → Kann durch Seegang pendeln → Rate-Gyro-Upgrade erwägen
│   │   ├── Rate-Gyro → Sollte stabil sein → Kalibrierung prüfen
│   │   └── Satellitenkompass → Bester Typ für MARPA → Firmware prüfen
│
├── GPS-Qualität prüfen:
│   ├── HDOP <2?
│   │   ├── NEIN → GPS-Position zu ungenau → Antenne verbessern, SBAS aktivieren
│   │   └── JA → GPS ist OK ↓
│
├── Radar-Bildqualität prüfen:
│   ├── Tuning korrekt? (bei Magnetron-Radar)
│   │   ├── NEIN → Auto-Tune oder manuell nachstimmen
│   │   └── JA → Gain und Sea-Clutter optimieren
│
└── EMPFEHLUNG:
    ├── Für zuverlässiges MARPA: Satellitenkompass + 4ft Open-Array
    ├── Minimum: Rate-Gyro-Compass + 24" Radome
    └── Nicht empfohlen: Fluxgate-Kompass + 18" Dome für CPA-Entscheidungen
```

### 7.5 Entscheidungsbaum: Antenne dreht nicht

```
START: Radar-Antenne dreht nicht
│
├── Zeigt das Display eine Fehlermeldung?
│   ├── JA → Fehlermeldung notieren
│   │   ├── "No Scanner" / "Scanner not connected"
│   │   │   → Antennenkabel prüfen (Stecker, Wassereinbruch)
│   │   │   → Kabel am MFD-seitigen Stecker prüfen
│   │   │   → Bei Ethernet-Radar: Netzwerkverbindung prüfen
│   │   ├── "Scanner Fault" / "Hardware Error"
│   │   │   → Steuerplatine in Antenne defekt → Service-Center
│   │   └── "Scanner Overtemp"
│   │       → Antenne abkühlen lassen, Belüftung prüfen
│   │       → Dauerhafte Überhitzung → Service-Center
│   └── NEIN ↓
│
├── Ist die Antenne zugänglich? (Radome öffnen / Open-Array inspizieren)
│   ├── JA → Mechanische Inspektion ↓
│   │   ├── Lässt sich die Antenne von Hand drehen?
│   │   │   ├── NEIN → Mechanische Blockade
│   │   │   │   ├── Eis / Frost → Enteisen, nicht mit Gewalt drehen
│   │   │   │   ├── Fremdkörper → Entfernen
│   │   │   │   ├── Lager festgefressen → Motor/Lager tauschen
│   │   │   │   └── Riemen in Zahnrad verwickelt → Befreien/Tauschen
│   │   │   └── JA → Motor-/Antriebsproblem
│   │   │       ├── Riemenantrieb? → Riemen gerissen/locker?
│   │   │       │   ├── JA → Riemen tauschen (Ersatzteil beim Hersteller)
│   │   │       │   └── NEIN → Motor prüfen ↓
│   │   │       ├── Direktantrieb? → Motor prüfen ↓
│   │   │       └── Motor-Test:
│   │   │           ├── Spannung am Motor messen (12V/24V je nach Modell)
│   │   │           │   ├── Spannung vorhanden → Motor defekt → Tauschen
│   │   │           │   └── Keine Spannung → Steuerplatine / Kabel defekt
│   │   │           └── Motor-Widerstand messen (Herstellerangabe vergleichen)
│   └── NEIN → Nur externe Prüfung möglich
│       → Antennenkabel und Stecker prüfen
│       → Spannungsversorgung am Sockel messen
│       → Marinefachbetrieb beauftragen
│
└── SCHNELLTEST (vor Zerlegung):
    1. Radar aus/ein (Power Cycle)
    2. Alle Kabelverbindungen prüfen und nachziehen
    3. Spannungsversorgung messen (12,0–14,4V für 12V-System)
    4. Factory Reset des Radargeräts
    5. Firmware-Update prüfen und installieren
```

---

## 8. FAQ

### 8.1 Allgemein

**F1: Brauche ich Radar auf meiner Yacht?**
Gesetzlich vorgeschrieben ist Radar für Sportboote unter 24 m in den meisten Ländern nicht. Allerdings verlangt COLREG Regel 5, alle verfügbaren Mittel für den Ausguck zu nutzen. Für Nachtfahrten, Nebelnavigation und Offshore-Törns ist Radar ein essenzielles Sicherheitsgerät. In deutschen Küstengewässern (Nordsee, Ostsee) mit häufigem Nebel und dichtem Verkehr ist Radar dringend empfohlen ab 10 m Bootslänge.

**F2: Reicht AIS alleine als Ersatz für Radar?**
Nein. AIS zeigt nur kooperative Ziele, die einen AIS-Transponder tragen. Viele kleine Boote, Fischerboote, Treibgut, Eisberge, Landmassen und Regenfelder sind im AIS unsichtbar. AIS ergänzt Radar, ersetzt es nicht. Umgekehrt liefert AIS Informationen (Schiffsname, Zielhafen, Tiefgang), die Radar nicht bieten kann.

**F3: Solid-State oder Magnetron — was ist besser?**
Für die meisten Yachten ist Solid-State (FMCW/Puls-Kompression) heute die bessere Wahl: sofort betriebsbereit, kein Magnetron-Verschleiß, geringerer Strom, leichter, besserer Nahbereich, Doppler-Fähigkeit. Magnetron-Radar hat Vorteile bei maximaler Reichweite und extremen Wetterbedingungen (Offshore-Langfahrt, Polargebiete). Für Küstensegler und Wochenendtörns: Solid-State. Für Blauwasser-Langfahrt: ggf. leistungsstarkes Magnetron-Radar als Backup erwägen.

**F4: Welche Radome-Größe für meine Yacht?**
18" (46 cm) — für Segelboote 8–12 m, Küstensegeln. 24" (61 cm) — für Segelboote 12–16 m und Motoryachten 10–15 m, Offshore-fähig. 4 ft Open-Array — für Yachten >15 m oder professionelle Anforderungen. 6 ft Open-Array — für Superyachten und kommerzielle Nutzung.

**F5: Wie viel Strom verbraucht ein modernes Radar?**
Solid-State-Dome (18"–24"): typisch 15–30 W im Sendebetrieb, 5–10 W Standby. Magnetron-Radar (4 kW): typisch 30–80 W Senden, 15–25 W Standby. Open-Array (Solid-State): 25–50 W Senden. Für eine Segelyacht mit 400 Ah Batteriebank und Solarpanels ist ein Solid-State-Dome problemlos betreibbar.

### 8.2 Installation

**F6: Wo montiere ich die Radarantenne auf einer Segelyacht?**
Drei Optionen: (1) Am Mast — höchste Position, beste Reichweite, aber Mast-Schatten querab, schwieriger Service. (2) Am Achterstag-/Heckkorb — leicht zugänglich, aber niedrig (3–4 m), geringe Reichweite. (3) Am Radar-Arch/Geräteträger — guter Kompromiss, 3–5 m Höhe, guter Zugang, Kabellänge moderat.

**F7: Welche Mindestabstände muss ich bei der Radar-Installation einhalten?**
Radar zu Kompass (magnetisch): mindestens 2 m. Radar zu GPS-Antenne: mindestens 1 m. Radar zu VHF-Antenne: mindestens 1,5 m. Radar zu Wind-Sensor: mindestens 1 m. Radar zu Personenaufenthalt: Herstellerangabe beachten (typisch 0,5–2 m je nach Leistung). Solid-State-Radar hat deutlich geringere Sicherheitsabstände als Magnetron.

**F8: Brauche ich einen VHF-Splitter für AIS?**
Wenn Sie nur EINE VHF-Antenne haben (Standardfall auf den meisten Yachten): Ja, ein VHF-Splitter ist die einfachste Lösung. Alternative: zweite VHF-Antenne dediziert für AIS (mindestens 1 m Abstand zur Haupt-VHF). Empfehlung: VHF-Splitter für die meisten Yachten ausreichend und kostengünstiger als zweite Antenne mit Montage.

**F9: Kann ich Radar und AIS verschiedener Hersteller kombinieren?**
Ja, grundsätzlich. AIS kommuniziert über NMEA 0183 oder NMEA 2000, was herstellerunabhängig ist. Radar ist herstellergebunden (Simrad-Radar nur an Simrad/B&G/Lowrance-MFD, etc.). AIS eines beliebigen Herstellers funktioniert an jedem MFD mit NMEA-Eingang. Einzige Einschränkung: Volle Integration (AIS-Overlay auf Radar) funktioniert am besten innerhalb eines Hersteller-Ökosystems.

**F10: Wie lang darf das Radar-Antennenkabel sein?**
Abhängig vom Kabeltyp und der Schnittstelle: Ethernet-Verbindung (moderne Radar): bis 100 m (Cat5e). Koaxialkabel (Magnetron-Radar, Radome): Herstellerangabe, typisch 15–30 m (Standardkabel), bis 50 m mit verlustarmen Kabel. Bei Verlängerung: Immer gleichen Kabeltyp verwenden, keine Verbindungsstücke im Kabel (Signalverlust).

### 8.3 Betrieb

**F11: Was bedeuten die Farben bei Doppler-Radar?**
Sich nähernde Ziele werden typisch rot dargestellt, sich entfernende grün oder blau. Stationäre Ziele erscheinen in der normalen Radarfarbe. Achtung: Doppler zeigt nur die radiale Komponente — ein Schiff, das exakt quer kreuzt, zeigt keine Doppler-Verschiebung!

**F12: Wann nutze ich MARPA, wann reicht Doppler?**
Doppler gibt einen schnellen visuellen Eindruck: nähert sich etwas oder nicht? MARPA liefert quantitative Werte (CPA, TCPA, Kurs, Geschwindigkeit). Für eine fundierte Ausweich-Entscheidung gemäß COLREG ist MARPA unverzichtbar. Doppler ist ein ergänzendes Situationsbewusstseins-Tool, kein Ersatz für Tracking.

**F13: Wie interpretiere ich CPA und TCPA korrekt?**
CPA (Closest Point of Approach) = geringster Abstand, der zwischen den Schiffen eintreten wird, wenn beide Kurs und Geschwindigkeit beibehalten. TCPA (Time to CPA) = Zeit bis zum CPA-Punkt. Negative TCPA = der CPA-Punkt liegt bereits hinter uns (Schiff entfernt sich). CPA allein reicht nicht: CPA 0,1 nm in 30 Minuten ist anders zu bewerten als CPA 0,1 nm in 2 Minuten.

**F14: Wie stelle ich Gain, Sea-Clutter und Rain-Clutter korrekt ein?**
Grundregel: (1) Gain so hoch, dass Rauschen gerade sichtbar ist — nicht höher. (2) Sea-Clutter: langsam erhöhen, bis Nahbereich-Clutter verschwindet, aber Ziele noch sichtbar. (3) Rain-Clutter: nur aktivieren bei tatsächlichem Regen. In der Praxis: Automatik-Modi moderner Radare (Auto Gain, Auto Sea) funktionieren gut. Manuelle Einstellung in Extremsituationen üben.

**F15: Was ist Dual Range und wann nutze ich es?**
Dual Range zeigt zwei Entfernungsbereiche gleichzeitig auf gesplittetem Bildschirm: z.B. links 0,5 nm (Hafenmanöver) und rechts 12 nm (Verkehrsübersicht). Besonders nützlich beim Ein-/Auslaufen aus Häfen, in Engstellen, und bei Nachtfahrten. Verfügbar bei Garmin Fantom, Simrad Halo, Furuno DRS-NXT.

### 8.4 AIS-spezifisch

**F16: AIS Klasse B oder B+ — was soll ich kaufen?**
Klasse B+ (SOTDMA, 5W) ist die klare Empfehlung. Die höhere Sendeleistung (5W vs. 2W) und das SOTDMA-Protokoll garantieren, dass Großschiffe Ihr Boot sehen. Klasse B (CSTDMA, 2W) kann bei Überlastung verdrängt werden und hat geringere Reichweite. Der Preisunterschied (ca. 200 EUR) ist die Sicherheit wert.

**F17: Sehen mich Großschiffe mit AIS Klasse B?**
Klasse B (CSTDMA, 2W): Auf vielen Handelsschiff-ECDIS-Systemen werden Klasse-B-Ziele standardmäßig gefiltert oder nur ab einer bestimmten Entfernung angezeigt. Klasse B+ (SOTDMA, 5W): Wird wie Klasse A behandelt, immer angezeigt. Klasse A: Höchste Priorität, immer sichtbar. Fazit: Mit Klasse B sind Sie nicht garantiert sichtbar!

**F18: Muss ich eine MMSI beantragen?**
Ja, für jeden AIS-Transponder (nicht für reine Empfänger). In Deutschland über die Bundesnetzagentur. Die MMSI wird zusammen mit dem Schiffsfunkstellenzeugnis vergeben. Kosten ca. 40–60 EUR. Voraussetzung: gültiges Seefunkzeugnis (SRC, LRC oder UBI).

**F19: Kann ich den AIS-Transponder im Notfall abschalten?**
Ja, AIS hat einen "Silent Mode" / "Rx-Only"-Modus. In Piraterie-gefährdeten Gebieten kann dies sinnvoll sein. Achtung: In SOLAS-Gewässern ist das Abschalten für pflichtausgerüstete Schiffe nur in Ausnahmefällen erlaubt. Für Sportboote keine gesetzliche Pflicht zur Dauersendung, aber aus Sicherheitsgründen empfohlen.

**F20: Was ist AIS-MOB und lohnt sich das?**
AIS-MOB ist ein persönlich getragener Sender, der bei Wassereinbruch oder manueller Aktivierung eine MOB-Position auf AIS sendet. Reichweite 2–5 nm. Alle AIS-Empfänger in der Nähe zeigen den MOB-Alarm. Besonders sinnvoll für Einhandsegler und bei Nachtfahrten. Kosten 150–350 EUR — für die potenzielle Lebensrettung eine lohnende Investition.

### 8.5 Technisch vertieft

**F21: Was ist der Unterschied zwischen True Motion und Relative Motion?**
Relative Motion: Eigenes Schiff in der Mitte, alles bewegt sich relativ zu uns. Standard für die meisten Yacht-Situationen. True Motion: Eigenes Schiff bewegt sich über die Karte. Realistischer, aber ungewohnter. True Motion ist besser für die COLREG-Interpretation (echte Kurse direkt ablesbar).

**F22: Warum ist mein Heading-Sensor so wichtig für Radar?**
Der Heading-Sensor bestimmt die Ausrichtung des Radarbilds. Fehler von 3° bei einer Entfernung von 6 nm ergeben einen Seitwärts-Versatz von ca. 0,3 nm (556 m). Für MARPA und Radar-Overlay ist ein Heading-Sensor mit <1° Genauigkeit essenziell. Fluxgate-Kompasse liefern typisch 2–5° Genauigkeit, Satellitenkompasse <0,3°.

**F23: Kann ich Radar-Daten über NMEA 2000 übertragen?**
Nein. Radar-Bilddaten sind zu datenintensiv für NMEA 2000 (250 kbps). Radar nutzt Ethernet (10/100 Mbit) oder proprietäre Hochgeschwindigkeitsverbindungen. Über NMEA 2000 werden nur Steuerungsbefehle (Standby/Transmit) und MARPA-Zieldaten (PGN 129026, 129038) übertragen.

**F24: Was ist ein Radar Target Enhancer (RTE)?**
Ein RTE ist ein aktiver Radarreflektor, der eingehende Radarsignale verstärkt und zurücksendet. Effektiv 15–25 dB Verstärkung des Radarquerschnitts. Besonders sinnvoll für GFK-Segelboote, die sonst einen sehr geringen RCS haben. Hersteller: Echomax, Sea-Me. Kosten: 600–2.500 EUR. Stromverbrauch: 1–3 W.

**F25: Wie funktioniert Bird Mode und wofür?**
Bird Mode nutzt die Doppler-Fähigkeit des Radars, um Vogelschwärme zu erkennen und darzustellen. Für Sportfischer: Vogelschwärme markieren häufig Fischschwärme unter der Oberfläche. Für Segler weniger relevant, aber interessant zur Erkennung von Vogelschutzgebieten und Wetterveränderungen.

**F26: Kann AIS gefälscht werden (Spoofing)?**
Theoretisch ja, AIS-Signale sind unverschlüsselt und können gefälscht werden. In der Praxis selten bei Sportschifffahrt, aber dokumentiert in geopolitischen Konfliktzonen. Gegenmaßnahme: AIS-Daten immer mit Radarbild abgleichen. Wenn AIS-Ziel ohne Radar-Echo → verdächtig (oder außer Radar-Reichweite).

**F27: Welche Radar-Drehzahl brauche ich?**
24 U/min: Standard, ausreichend für die meisten Situationen. 36 U/min: Bessere Bildaktualisierung, empfohlen für engere Gewässer. 48 U/min: Schnell, gut für Hafenmanöver. 60 U/min (Simrad Halo): Sehr schnell, ideal für Regatten und Hafenmanöver mit engem Verkehr.

**F28: Was passiert wenn mein Radar in einem Regengebiet "blind" ist?**
X-Band-Radar (9,4 GHz) wird durch starken Regen deutlich gedämpft. Hinter einer schweren Regenfront können Ziele vollständig maskiert sein. Maßnahmen: Rain-Clutter reduzieren (nicht auf Maximum!), alternativ nur auf einer Seite des Regenfelds clutter-filtern. S-Band-Radar (3 GHz) durchdringt Regen deutlich besser — auf Superyachten wird daher oft ein Dual-Band-System (S+X) installiert.

**F29: Wie oft muss ich mein Radar warten lassen?**
Magnetron-Radar: Alle 2.000–3.000 Betriebsstunden Magnetron-Check, ggf. Austausch (ca. 300–800 EUR). Jährlich: Antennengehäuse auf Dichtheit prüfen, Stecker auf Korrosion, Kabel auf Knicke. Solid-State-Radar: Weniger wartungsintensiv, kein Magnetron-Verschleiß. Jährlich: Gehäusedichtung prüfen, Firmware aktualisieren, Steckverbindungen prüfen. Alle 5 Jahre: Professionelle Inspektion der Antenneneinheit.

**F30: Wie teste ich ob mein AIS korrekt funktioniert?**
(1) MarineTraffic.com oder VesselFinder.com aufrufen und eigene MMSI suchen — Position sollte aktuell sein. (2) Anderes Boot in der Nähe fragen, ob es Ihr AIS sieht. (3) Am AIS-Gerät: Tx-LED muss regelmäßig blinken. (4) NMEA-Daten auslesen — korrekte Sentences (AIVDM/AIVDO). (5) Bei Klasse B+: Berichtsrate prüfen (30 s fahrend, 3 min Anker).

---

## 9. Glossar

### 9.1 Radar-Begriffe (A–Z)

| Begriff | Erklärung |
|---------|-----------|
| **ARPA** | Automatic Radar Plotting Aid — automatisches Radar-Zieltracking gemäß IMO-Standard, berechnet CPA/TCPA |
| **Azimut** | Horizontale Richtung eines Radarziels, gemessen in Grad (0°–360°) |
| **Bearing** | Peilung — Richtung zu einem Ziel, relativ (zum Bug) oder true (zu Nord) |
| **Broadband** | Marketingbezeichnung für FMCW-Solid-State-Radar (Navico/Simrad 2009) |
| **CFAR** | Constant False Alarm Rate — adaptive Detektionsschwelle zur Unterdrückung von Falschzielen |
| **Chirp** | Puls mit linear ansteigender Frequenz, Grundlage der Puls-Kompression |
| **Clutter** | Unerwünschte Radarechos von Wellen (Sea), Regen (Rain) oder Land |
| **CPA** | Closest Point of Approach — geringster Abstand, der zwischen zwei Schiffen eintreten wird |
| **Doppler** | Frequenzverschiebung durch Relativbewegung Sender-Ziel, ermöglicht Geschwindigkeitserkennung |
| **EBL** | Electronic Bearing Line — elektronische Peilung auf dem Radarbild |
| **Echo** | Vom Ziel reflektiertes Radarsignal |
| **FMCW** | Frequency Modulated Continuous Wave — Dauerstrichradar mit Frequenzmodulation |
| **FTC** | Fast Time Constant — Signalverarbeitung zur Unterdrückung von Regenclutter |
| **Gain** | Verstärkung des Radar-Empfängers |
| **Guard Zone** | Überwachungsbereich im Radar, löst Alarm bei neuem Ziel aus |
| **Heading** | Kurs über Grund oder Kompasskurs des eigenen Schiffs |
| **IR** | Interference Rejection — Filter gegen Störung durch andere Radare |
| **Magnetron** | Vakuumröhre zur Erzeugung von Hochfrequenz-Impulsen im Pulsradar |
| **MARPA** | Mini-ARPA — vereinfachtes manuelles Radar-Zieltracking für Yachten |
| **MFD** | Multi-Function Display — Kombianzeige für Radar, Karte, Sonar etc. |
| **Nautische Meile** | 1 nm = 1.852 m, Standardmaß für Entfernungen auf See |
| **Open-Array** | Offene, längliche Radarantenne ohne Schutzgehäuse |
| **PRF** | Pulse Repetition Frequency — Pulswiederholfrequenz |
| **Radome** | Radar + Dome — geschlossenes Radarantennengehäuse (Kuppel) |
| **Range** | Entfernungsbereich der Radaranzeige |
| **RCS** | Radar Cross Section — Radarquerschnitt eines Ziels in m² |
| **RTE** | Radar Target Enhancer — aktiver Radarreflektor |
| **S-Band** | Radarfrequenzband 2,9–3,1 GHz, durchdringt Regen besser |
| **STC** | Sensitivity Time Control — entfernungsabhängige Empfindlichkeitssteuerung gegen Seegangsclutter |
| **TCPA** | Time to Closest Point of Approach — Zeit bis zum nächsten Annäherungspunkt |
| **Trail** | Nachleuchtende Spur eines Radarziels auf dem Display |
| **Tune** | Abstimmung des Radar-Empfängers auf die Sendefrequenz (bei Magnetron) |
| **VRM** | Variable Range Marker — einstellbarer Entfernungsring auf dem Radarbild |
| **X-Band** | Radarfrequenzband 9,3–9,5 GHz, Standard für Yacht-Radar |

### 9.2 AIS-Begriffe (A–Z)

| Begriff | Erklärung |
|---------|-----------|
| **AIS** | Automatic Identification System — automatisches Identifizierungssystem für Schiffe |
| **AIS-MOB** | Man-Over-Board-Sender mit AIS-Funktion |
| **AIS-SART** | Search and Rescue Transponder mit AIS-Technologie |
| **AtoN** | Aids to Navigation — Seezeichen mit AIS-Transponder (virtuelle oder physische) |
| **COG** | Course Over Ground — Kurs über Grund |
| **CSTDMA** | Carrier Sense TDMA — Kanalzugriffsverfahren für AIS Klasse B |
| **DSC** | Digital Selective Calling — Digitaler Selektivruf (verwandtes VHF-System) |
| **ECDIS** | Electronic Chart Display and Information System — elektronische Seekartenanzeige |
| **ETA** | Estimated Time of Arrival — voraussichtliche Ankunftszeit |
| **GMSK** | Gaussian Minimum Shift Keying — Modulationsverfahren für AIS |
| **HDOP** | Horizontal Dilution of Precision — Maß für GPS-Genauigkeit |
| **IMO** | International Maritime Organization — Internationale Seeschifffahrtsorganisation |
| **ITU** | International Telecommunication Union — Internationale Fernmeldeunion |
| **MID** | Maritime Identification Digits — Landeskennziffern in der MMSI |
| **MMSI** | Maritime Mobile Service Identity — 9-stellige maritime Funkkennung |
| **NMEA** | National Marine Electronics Association — Standard für Marinedaten-Kommunikation |
| **ROT** | Rate of Turn — Drehrate des Schiffs (°/min) |
| **SBAS** | Satellite-Based Augmentation System (WAAS/EGNOS) — Satellitengestützte Korrekturdaten |
| **SOG** | Speed Over Ground — Geschwindigkeit über Grund |
| **SOLAS** | Safety of Life at Sea — Internationales Übereinkommen zum Schutz des menschlichen Lebens auf See |
| **SOTDMA** | Self-Organising TDMA — Kanalzugriffsverfahren für AIS Klasse A und B+ |
| **TDMA** | Time Division Multiple Access — Zeitmultiplexverfahren |
| **VDL** | VHF Data Link — VHF-Datenverbindung für AIS |

---

## 10. Schnell-Referenz

### 10.1 Entscheidungshilfe: Radar-Auswahl nach Bootsklasse

```
Bootsklasse und Einsatz → Empfohlenes Radar

Segelyacht 8–10 m, Küste
  → 18" Solid-State-Dome (Garmin Fantom 18x / Simrad Halo20+ / Furuno DRS2D-NXT)
  → Budget: 1.800–2.200 EUR

Segelyacht 10–14 m, Küste/Offshore
  → 24" Solid-State-Dome (Garmin Fantom 24x / Simrad Halo24 / Furuno DRS4D-NXT)
  → Budget: 2.500–3.500 EUR

Segelyacht 14–18 m, Blauwasser
  → 4 ft Open-Array Solid-State (Garmin Fantom 54 / Simrad Halo 4000 / Furuno DRS12A-NXT)
  → Budget: 4.500–6.000 EUR
  → Optional: 4 kW Magnetron als Backup

Motoryacht 8–12 m, Küste
  → 18"–24" Solid-State-Dome
  → Budget: 1.800–3.500 EUR

Motoryacht 12–20 m, Offshore
  → 4 ft Open-Array Solid-State
  → Budget: 4.500–6.000 EUR

Superyacht 20–30 m
  → 6 ft Open-Array Solid-State (Garmin Fantom 56 / Simrad Halo 6000 / Furuno DRS25A-NXT)
  → Optional Dual-Band (S+X, Furuno)
  → Budget: 8.000–15.000 EUR

Superyacht >30 m
  → Professionelles IMO-Radar (Furuno FAR-Serie)
  → Dual-Band (S+X) empfohlen
  → Budget: 15.000–60.000 EUR
```

### 10.2 Entscheidungshilfe: AIS-Auswahl

```
Einsatz → Empfohlener AIS-Typ

Binnengewässer, gelegentlich
  → AIS-Empfänger (em-trak R300 / Digital Yacht) + Tablet-App
  → Budget: 200–300 EUR

Küstensegeln, Wochenende
  → AIS Klasse B+ (em-trak B954 / Vesper Marine XB-8000)
  → + VHF-Splitter
  → Budget: 600–1.000 EUR

Offshore / Langfahrt
  → AIS Klasse B+ (em-trak B954) oder Klasse A (em-trak A100)
  → + separate AIS-Antenne ODER guter Splitter
  → + AIS-MOB für alle Crew
  → Budget: 800–2.500 EUR

Gewerblich / Charter
  → AIS Klasse A (Pflicht bei Passagieren)
  → + separate AIS-Antenne
  → Budget: 1.500–3.500 EUR

Integrierte Lösung
  → Vesper Marine Cortex (VHF + AIS + Monitoring)
  → Budget: 2.000–3.000 EUR
```

### 10.3 Montage-Kurzreferenz

```
Radar-Montage — Checkliste:
□ Montageplatz freie 360°-Sicht (oder Blindsektoren dokumentieren)
□ Mindestabstand zu Personen (Herstellerangabe, typisch 0,5–2 m)
□ Mindestabstand zu Kompass: 2 m
□ Mindestabstand zu GPS: 1 m
□ Mindestabstand zu VHF-Antenne: 1,5 m
□ Montageplattform vibrationsfrei und tragfähig
□ Kabelführung wasserdicht, UV-geschützt
□ Stecker mit Selbstvulkanisierungsband abdichten
□ Erdung gemäß ABYC E-11 / ISO 10133
□ Bearing-Offset nach Montage einmessen

AIS-Installation — Checkliste:
□ VHF-Antenne mit freier Sicht 360° (min. 3 m über Wasser)
□ VHF-Splitter oder separate AIS-Antenne
□ GPS-Antenne (intern reicht meist, sonst extern)
□ MMSI programmiert und verifiziert
□ NMEA-Anbindung an Kartenplotter (0183 oder 2000)
□ Antennen-Offset (GPS-Position zu AIS-Antennenposition) eingegeben
□ Test: MarineTraffic.com → eigene MMSI sichtbar?
□ Test: Andere AIS-Ziele werden empfangen?
□ Stromversorgung über Bordnetz mit Sicherung
```

### 10.4 Sicherheitshinweise Kurzreferenz

```
RADAR — Sicherheit:
⚠ Magnetron-Radar: Niemals in die Antenne blicken bei Sendung
⚠ Sicherheitszone um rotierende Open-Array beachten
⚠ Hochspannung im Magnetron (>4.000 V) — nur Fachpersonal
⚠ Solid-State-Radar: Deutlich geringere Abstrahlgefahr
⚠ Radar niemals unter Abdeckung/Plane betreiben (Überhitzung)

AIS — Sicherheit:
⚠ AIS ist KEIN Ersatz für Radar-Ausguck
⚠ AIS-Daten können fehlerhaft sein (falsche MMSI, Position, Kurs)
⚠ Nicht alle Schiffe tragen AIS (kleine Boote, Militär, Fischer)
⚠ AIS-Spoofing in Krisengebieten möglich
⚠ Silent Mode nur in Piraterie-Gebieten aktivieren
```

---

## 11. ANHANG A–H — Fallstudien

### ANHANG A — Fallstudie: Segelyacht 12 m, Ostsee-Ausrüstung

**Yacht-Profil:**
- Typ: Segelyacht, GFK, 12,2 m LOA
- Revier: Ostsee (Kiel–Dänemark–Schweden), gelegentlich Nordsee
- Crew: 2 Personen, Langfahrt-Ambitionen
- Budget Navigation: 6.000 EUR
- Bestehendes System: Kartenplotter (Raymarine Axiom 9"), VHF-Funk, kein Radar, kein AIS

**Problemstellung:**
Die Ostsee ist ein Revier mit häufigem Nebel (besonders Mai–September), dichtem Verkehr (Fähren, Frachter in den Zugängen) und vielen kleinen Inseln. Die Yacht plant Überfahrten nach Dänemark und Schweden, auch nachts.

**AYDI-Analyse und Empfehlung:**

| Komponente | Empfehlung | Preis ca. |
|-----------|------------|-----------|
| Radar | Simrad Halo20+ (Kompatibel mit Raymarine über NMEA/Ethernet-Konverter) ODER Raymarine Quantum 2 Q24D (Direktintegration mit Axiom) | 1.900 EUR |
| AIS | em-trak B954 (Klasse B+, SOTDMA, 5W) | 650 EUR |
| VHF-Splitter | em-trak S300 | 220 EUR |
| Heading-Sensor | Raymarine EV-1 (Rate-Gyro) für MARPA | 650 EUR |
| AIS-MOB | 2× Ocean Signal rescueME MOB1 | 500 EUR |
| Kabel/Montage | Material + Arbeitszeit | 800 EUR |
| **Gesamt** | | **4.720 EUR** |

**Montagekonzept:**
- Radar: Am Heckkorb-Geräteträger, 3,5 m über Wasser
- Blindsektoren: ca. 10°–15° durch Mast querab — dokumentiert
- AIS-Antenne: VHF-Splitter an bestehender VHF-Antenne am Masttopp
- AIS-MOB: In Rettungswesten integriert

**Ergebnis:** Vollständige Kollisionsverhütung für Ostsee-Bedingungen. MARPA-fähig dank Rate-Gyro-Kompass. Radar-Overlay auf Axiom-Kartenplotter.

### ANHANG B — Fallstudie: Motoryacht 15 m, Mittelmeer

**Yacht-Profil:**
- Typ: Motoryacht, GFK, 15,3 m LOA, Flybridge
- Revier: Mittelmeer (Kroatien, Griechenland, Türkei)
- Crew: 2–4 Personen
- Budget Navigation: 10.000 EUR
- Bestehendes System: Garmin GPSMAP 8616 (16"), Garmin VHF 315i

**Problemstellung:**
Mittelmeer-Navigation erfordert gute Nahbereich-Auflösung (enge Häfen, Buchten) und Reichweite für die Überfahrt zwischen Inseln. Nachtfahrten regelmäßig, besonders im Sommer (Vermeidung der Mittagshitze).

**AYDI-Analyse und Empfehlung:**

| Komponente | Empfehlung | Preis ca. |
|-----------|------------|-----------|
| Radar | Garmin GMR Fantom 24x (24" Dome, 50 W, Doppler) | 3.400 EUR |
| AIS | Garmin AIS 800 (Klasse B+, integriert in Garmin-Netzwerk) | 800 EUR |
| VHF-Splitter | Garmin VHF-AIS Splitter | 200 EUR |
| Heading-Sensor | Garmin MSC 10 Kompass-Sensor | 250 EUR |
| AIS-MOB | 2× ACR AISLink MOB | 400 EUR |
| Montage Archbogen | Radar auf Flybridge-Archbogen, 5 m über Wasser | 600 EUR |
| Kabel/Material | Ethernet-Kabel, Stecker, Abdichtung | 400 EUR |
| **Gesamt** | | **6.050 EUR** |

**Besondere Merkmale:**
- Garmin-Ökosystem durchgängig → nahtlose Integration
- Dual Range: 0,25 nm + 12 nm gleichzeitig für Hafenmanöver
- MotionScope (Doppler): Farbliche Erkennung sich nähernder Boote in belebten Buchten
- Bird Mode: Für gelegentliches Angeln nutzbar
- Anchor Drag Alert: Ankerüberwachung in beliebten Ankerbuchten

### ANHANG C — Fallstudie: Blauwasser-Segelyacht 16 m

**Yacht-Profil:**
- Typ: Segelyacht, Aluminium, 16,4 m LOA, Ketch-Rigg
- Revier: Atlantik-Überquerung, Karibik, anschließend Pazifik
- Crew: 2 Personen, Langfahrt 3+ Jahre
- Budget Navigation: 15.000 EUR
- Bestehendes System: B&G Zeus3 12", B&G Triton T41, Hydra-Autopilot

**Problemstellung:**
Blauwasser-Langfahrt erfordert maximale Zuverlässigkeit, geringen Stromverbrauch (begrenzte Solarkapazität), gute Reichweite und die Fähigkeit, in allen Wetterbedingungen zuverlässig zu arbeiten. Radar muss auch bei tropischen Regenfällen funktionieren.

**AYDI-Analyse und Empfehlung:**

| Komponente | Empfehlung | Preis ca. |
|-----------|------------|-----------|
| Radar (primär) | B&G Halo 4000 (4 ft Open-Array, Solid-State, Doppler) | 5.500 EUR |
| Radar (backup) | B&G Halo20+ (20" Dome, Solid-State) | 2.000 EUR |
| AIS | em-trak A100 (Klasse A, 12,5 W — maximale Sichtbarkeit offshore) | 1.800 EUR |
| AIS-Antenne | Dedizierte Shakespeare 396-1 AIS-Antenne | 120 EUR |
| Heading-Sensor | B&G Precision-9 Compass (Satellit+Gyro) | 1.200 EUR |
| Radarreflektor | Echomax Active-XS Dual Band (aktiv) | 2.500 EUR |
| AIS-MOB | 2× Ocean Signal rescueME MOB1 | 500 EUR |
| AIS-SART | 1× Ocean Signal rescueME AIS-SART | 350 EUR |
| Montage/Kabel | Mastmontage Radome, Archbogen Open-Array | 1.200 EUR |
| **Gesamt** | | **15.170 EUR** |

**Besondere Überlegungen:**
- **Dual-Radar:** Redundanz auf Langfahrt essenziell. Dome am Mast (schnell verfügbar, Nahbereich), Open-Array am Archbogen (Reichweite, MARPA-Qualität)
- **AIS Klasse A:** Auf Hochsee maximale Sichtbarkeit nötig — Containerschiffe fahren oft mit AIS-Filter für Klasse B
- **Aktiver Radarreflektor:** Aluminium-Rumpf reflektiert gut, aber Echomax Active-XS als Zusatzsicherheit bei Nacht/Nebel
- **Stromverbrauch:** Halo 4000 = 25 W, Halo20+ = 18 W — beides vertretbar bei 800 W Solar
- **Ersatzteile:** Solid-State → keine Magnetron-Ersatzteile nötig

### ANHANG D — Fallstudie: Superyacht 28 m, gewerblicher Betrieb

**Yacht-Profil:**
- Typ: Motoryacht, Stahl/Aluminium, 28 m LOA, gewerblicher Charter
- Revier: Mittelmeer, gelegentlich Karibik
- Crew: 4 professionelle Besatzung + bis zu 12 Gäste
- Budget Navigation: 40.000 EUR
- Regulatorische Anforderungen: MCA Large Commercial Yacht Code, CE Kategorie A

**AYDI-Analyse und Empfehlung:**

| Komponente | Empfehlung | Preis ca. |
|-----------|------------|-----------|
| Radar (primär) | Furuno FAR-1513 (X-Band, 12 kW, IMO-zugelassen) | 12.000 EUR |
| Radar (sekundär) | Furuno DRS25A-NXT (6 ft Open-Array, Solid-State) | 9.000 EUR |
| AIS | Furuno FA-170 (Klasse A, IMO-konform) | 2.500 EUR |
| Heading-Sensor | Furuno SC-50 Satellitenkompass | 4.000 EUR |
| ECDIS-Integration | Furuno NavNet TZtouch3 Integration | 5.000 EUR |
| VDR-Schnittstelle | Voyage Data Recorder Interface | 3.000 EUR |
| AIS-MOB | 6× Kannad SafeLink R10 (für Crew + Gäste-Westen) | 1.500 EUR |
| AIS-SART | 2× McMurdo SmartFind S20 | 800 EUR |
| Montage/Kabel | Professionelle Installation, EMV-Messung | 4.000 EUR |
| **Gesamt** | | **41.800 EUR** |

**Regulatorische Besonderheiten:**
- MCA LY3 Code verlangt: Radar (mind. X-Band, 9 GHz), AIS Klasse A, ECDIS oder zugelassene Kartenanlage
- Crew muss über Radar-/ARPA-Zertifikate verfügen
- Jährliche Funktionsprüfung durch zugelassene Prüfstelle
- VDR (Voyage Data Recorder) für Schiffe >3.000 BRT — bei 28 m ggf. noch nicht pflicht, aber empfohlen

### ANHANG E — Fallstudie: Regattayacht 11 m, Inshore-Regatta

**Yacht-Profil:**
- Typ: Segelyacht, GFK/Carbon, 11,2 m LOA, Regattaboot
- Revier: Inshore-Regatten, Küste, gelegentlich Offshore-Regatten
- Crew: 6–8 Personen
- Budget Navigation: 3.000 EUR

**AYDI-Analyse und Empfehlung:**

| Komponente | Empfehlung | Preis ca. |
|-----------|------------|-----------|
| AIS | em-trak B954 (Klasse B+) — viele Regatten erfordern AIS | 650 EUR |
| VHF-Splitter | em-trak S300 | 220 EUR |
| AIS-MOB | 2× Ocean Signal rescueME MOB1 (für Offshore-Regatten) | 500 EUR |
| Radarreflektor | Echomax 230 (passiv, leicht, ISO 8729) | 350 EUR |
| **Gesamt** | | **1.720 EUR** |

**Begründung:**
- Radar ist auf einer 11-m-Regattayacht unüblich (Gewicht, Kosten, Windwiderstand)
- AIS wird bei vielen Offshore-Regatten (z.B. Fastnet, Sydney-Hobart, Bermuda Race) gefordert
- Klasse B+ statt B, damit Race Committee und SAR das Boot sicher identifizieren
- Passiver Radarreflektor reicht für Inshore-Regatten (Pflicht gemäß vieler Segelanweisungen)

### ANHANG F — Fallstudie: AIS-Nachrüstung Kleinsegler 8 m

**Yacht-Profil:**
- Typ: Segelyacht, GFK, 8,2 m LOA, Jollenkreuzer/Weekender
- Revier: Nordsee-Küste, Wattenmeer, Dänische Südsee
- Crew: 2 Personen, Wochenendtörns
- Budget: 500 EUR
- Bestehendes System: Tablet mit Navionics, tragbares VHF

**Problemstellung:**
Kleinstmögliches AIS-Setup für Sicherheit im Wattenmeer und an der Nordseeküste (dichter Frachterverkehr auf den Zufahrten).

**AYDI-Empfehlung:**

| Komponente | Empfehlung | Preis ca. |
|-----------|------------|-----------|
| AIS | em-trak B100 (Klasse B, CSTDMA, 2W) | 350 EUR |
| Antenne | Glomex RA111 AIS-Antenne (kurz, am Heckkorb) | 60 EUR |
| USB-Kabel | USB → Tablet für AIS-Anzeige | 20 EUR |
| **Gesamt** | | **430 EUR** |

**Einschränkung:** Klasse B (2W) als Budgetlösung. Für regelmäßige Nordsee-Fahrten wäre Klasse B+ (5W) besser, aber 200 EUR über Budget. AIS-Daten werden per USB an das Tablet übertragen und in Navionics angezeigt.

### ANHANG G — Fallstudie: Radar-Fehldiagnose und Lösung

**Situation:**
Eine Motoryacht (14 m, Volvo Penta D4) meldet nach Radar-Installation (Simrad Halo20+) massive Störungen: GPS springt, VHF-Funk brummt, Windmesser zeigt falsche Werte — alles nur bei eingeschaltetem Radar.

**Diagnose-Verlauf:**

1. **Verdacht:** EMV-Interferenz durch Radar
2. **Prüfung Montageabstände:**
   - Radar zu GPS-Antenne: 0,4 m → **zu nah!** (Minimum: 1 m)
   - Radar zu VHF-Antenne: 0,8 m → **zu nah!** (Minimum: 1,5 m)
   - Radar zu Windmesser: 0,3 m → **zu nah!** (Minimum: 1 m)
3. **Prüfung Kabelführung:**
   - Radar-Ethernet-Kabel parallel zum VHF-Koax in Kabelkanal → **Koppelung!**
   - GPS-Antennenkabel ohne Schirmung verlegt
4. **Prüfung Erdung:**
   - Radar-Erdung nicht auf gemeinsame Erdungsschiene geführt → **Erdschleife!**

**Lösung:**
- Radar auf Flybridge-Archbogen versetzt (2,5 m über GPS, 2 m zu VHF)
- Kabel getrennt verlegt (Radar-Kabel separat von Signalkabeln)
- GPS-Antennenkabel mit doppelt geschirmtem Kabel ersetzt
- Gemeinsame Erdungsschiene installiert
- Ferritkerne an GPS- und VHF-Kabel

**Kosten der Nacharbeit:** ca. 800 EUR (Material + 6 h Arbeitszeit)
**Lehre:** Montageabstände bei Radar-Installation IMMER vor der Montage planen!

### ANHANG H — Fallstudie: AIS-Ausfall in der Deutschen Bucht

**Situation:**
Segelyacht (13 m) auf dem Weg von Helgoland nach Cuxhaven. Nebel setzt ein (Sichtweite <200 m). AIS zeigt keine Ziele mehr, obwohl Schiffstraffic bekannt hörbar (Nebelhorn).

**Diagnose an Bord:**

1. **AIS-Gerät prüfen:** LED leuchtet, Statusanzeige "Receiving", aber 0 Ziele
2. **VHF-Funk prüfen:** Funktioniert (Kommunikation mit Cuxhaven Traffic möglich)
3. **VHF-Splitter prüfen:** Status-LED blinkt nicht (normalerweise Empfangsanzeige)
4. **Verdacht:** VHF-Splitter defekt — AIS erhält kein Antennensignal

**Sofortmaßnahme:**
- VHF-Antennenkabel direkt an AIS-Transponder anschließen (VHF-Funk temporär ohne Antenne)
- Ergebnis: AIS zeigt sofort 12+ Ziele — Splitter war die Ursache!
- VHF-Funk über Handfunkgerät weiter betrieben

**Nachträgliche Analyse:**
- VHF-Splitter (Marke unbenannt) hatte internen Relais-Defekt
- Splitter schaltete dauerhaft auf VHF-Durchgang, AIS-Pfad unterbrochen
- Kein Vorzeichen — Ausfall kam ohne Vorwarnung

**Lehren:**
1. Ersatz-Splitter oder Y-Kabel als Notlösung an Bord haben
2. AIS regelmäßig auf MarineTraffic.com prüfen (sendet das Boot?)
3. Bei VHF-Splitter-Modellen auf Qualitätsmarken setzen (em-trak, Vesper, Shakespeare)
4. Separate AIS-Antenne als sicherste Lösung für Offshore-Fahrten

---

## 12. ANHANG I–R — Pydantic v2 Modelle

### ANHANG I — Basis-Modelle: Radar-Spezifikation

```python
"""
AYDI Radar & AIS — Pydantic v2 Modelle
Modul: 23.03 Radar und AIS
Alle Modelle verwenden model_config = {"from_attributes": True}
NIEMALS class Config verwenden!
"""

from __future__ import annotations

import uuid
from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, field_validator


# ── Enums ──────────────────────────────────────────────────────────────

class RadarType(str, Enum):
    """Radar-Technologie-Typ."""
    MAGNETRON_PULSE = "magnetron_pulse"
    SOLID_STATE_FMCW = "solid_state_fmcw"
    SOLID_STATE_PULSE_COMPRESSION = "solid_state_pulse_compression"
    SOLID_STATE_CHIRP = "solid_state_chirp"
    DUAL_BAND = "dual_band"


class RadarFormFactor(str, Enum):
    """Radar-Antennenbauform."""
    RADOME_18 = "radome_18"
    RADOME_20 = "radome_20"
    RADOME_24 = "radome_24"
    OPEN_ARRAY_3FT = "open_array_3ft"
    OPEN_ARRAY_4FT = "open_array_4ft"
    OPEN_ARRAY_6FT = "open_array_6ft"
    OPEN_ARRAY_8FT = "open_array_8ft"


class RadarBand(str, Enum):
    """Radar-Frequenzband."""
    X_BAND = "x_band"
    S_BAND = "s_band"
    DUAL_BAND = "dual_band"


class AISClass(str, Enum):
    """AIS-Geräteklasse."""
    CLASS_A = "class_a"
    CLASS_B_CSTDMA = "class_b_cstdma"
    CLASS_B_PLUS_SOTDMA = "class_b_plus_sotdma"
    RECEIVER_ONLY = "receiver_only"
    AIS_MOB = "ais_mob"
    AIS_SART = "ais_sart"


class ConfidenceLevel(str, Enum):
    """AYDI Confidence Level für Bewertungen."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class MountPosition(str, Enum):
    """Montageposition der Radar-Antenne."""
    MAST_TOP = "mast_top"
    MAST_SPREADER = "mast_spreader"
    ARCH = "arch"
    FLYBRIDGE = "flybridge"
    POLE = "pole"
    STERN_RAIL = "stern_rail"
    WHEELHOUSE_TOP = "wheelhouse_top"


class HeadingSensorType(str, Enum):
    """Typ des Heading-Sensors."""
    FLUXGATE = "fluxgate"
    RATE_GYRO = "rate_gyro"
    SATELLITE_COMPASS = "satellite_compass"
    GPS_COG = "gps_cog"
    NONE = "none"


# ── Radar Specification ────────────────────────────────────────────────

class RadarSpecification(BaseModel):
    """Vollständige Radar-Spezifikation eines Geräts."""

    model_config = {"from_attributes": True}

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    manufacturer: str = Field(..., description="Hersteller des Radargeräts")
    model: str = Field(..., description="Modellbezeichnung")
    radar_type: RadarType = Field(..., description="Radar-Technologietyp")
    form_factor: RadarFormFactor = Field(..., description="Antennenbauform")
    band: RadarBand = Field(default=RadarBand.X_BAND, description="Frequenzband")

    # Leistung
    transmit_power_w: float = Field(
        ..., gt=0, description="Sendeleistung in Watt (Spitze bei Puls, mittlere bei SS)"
    )
    max_range_nm: float = Field(..., gt=0, description="Maximale Reichweite in Seemeilen")
    min_range_m: float = Field(..., ge=0, description="Minimale Erfassungsentfernung in Metern")

    # Antenne
    beam_width_horizontal_deg: float = Field(
        ..., gt=0, lt=20, description="Horizontale Strahlbreite in Grad"
    )
    beam_width_vertical_deg: Optional[float] = Field(
        None, gt=0, lt=60, description="Vertikale Strahlbreite in Grad"
    )
    rotation_speed_rpm: list[int] = Field(
        ..., description="Verfügbare Drehzahlen in U/min"
    )

    # Physisch
    weight_kg: float = Field(..., gt=0, description="Gewicht der Antenneneinheit in kg")
    diameter_mm: Optional[float] = Field(None, description="Durchmesser Radome in mm")
    length_mm: Optional[float] = Field(None, description="Länge Open-Array in mm")

    # Elektrisch
    power_consumption_transmit_w: float = Field(
        ..., gt=0, description="Stromaufnahme im Sendebetrieb in Watt"
    )
    power_consumption_standby_w: Optional[float] = Field(
        None, description="Stromaufnahme im Standby in Watt"
    )
    supply_voltage_v: str = Field(
        default="12-24", description="Versorgungsspannung (z.B. '12-24')"
    )

    # Features
    has_doppler: bool = Field(default=False, description="Doppler-Erkennung verfügbar")
    has_marpa: bool = Field(default=True, description="MARPA-Tracking verfügbar")
    has_arpa: bool = Field(default=False, description="Volles ARPA verfügbar")
    has_dual_range: bool = Field(default=False, description="Gleichzeitige Dual-Range-Anzeige")
    has_bird_mode: bool = Field(default=False, description="Vogelschwarm-Erkennung")
    has_anchor_watch: bool = Field(
        default=False, description="Radar-gestützte Ankerwache (Doppler)"
    )

    # Konnektivität
    interface: list[str] = Field(
        ..., description="Schnittstellen (z.B. ['ethernet', 'wifi'])"
    )
    compatible_mfd_brands: list[str] = Field(
        ..., description="Kompatible MFD-Marken"
    )

    # Kosten
    price_eur: Optional[float] = Field(
        None, ge=0, description="Listenpreis in EUR"
    )
    warmup_time_s: float = Field(
        default=0, ge=0, description="Aufwärmzeit in Sekunden"
    )
    magnetron_lifetime_h: Optional[float] = Field(
        None, description="Magnetron-Lebensdauer in Stunden (nur Pulsradar)"
    )

    @field_validator("rotation_speed_rpm")
    @classmethod
    def validate_rotation_speeds(cls, v: list[int]) -> list[int]:
        if not v:
            raise ValueError("Mindestens eine Drehzahl muss angegeben werden")
        for speed in v:
            if speed < 10 or speed > 80:
                raise ValueError(f"Drehzahl {speed} U/min außerhalb des gültigen Bereichs 10–80")
        return v
```

### ANHANG J — AIS-Transponder-Modell

```python
class AISTransponderSpec(BaseModel):
    """Vollständige AIS-Transponder-Spezifikation."""

    model_config = {"from_attributes": True}

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    manufacturer: str = Field(..., description="Hersteller")
    model: str = Field(..., description="Modellbezeichnung")
    ais_class: AISClass = Field(..., description="AIS-Geräteklasse")

    # Sende/Empfangsspezifikation
    transmit_power_w: Optional[float] = Field(
        None, ge=0, description="Sendeleistung in Watt (None bei reinem Empfänger)"
    )
    access_method: Optional[str] = Field(
        None, description="Kanalzugriffsverfahren (SOTDMA/CSTDMA)"
    )
    receiver_channels: int = Field(
        default=2, ge=1, description="Anzahl paralleler Empfangskanäle"
    )

    # GPS
    has_internal_gps: bool = Field(default=True, description="Integrierter GPS-Empfänger")
    gps_channels: Optional[int] = Field(None, description="Anzahl GPS-Kanäle")
    supports_external_gps: bool = Field(
        default=True, description="Externer GPS-Eingang möglich"
    )

    # Berichtsraten
    report_rate_moving_s: Optional[float] = Field(
        None, description="Berichtsrate fahrend in Sekunden"
    )
    report_rate_anchored_s: Optional[float] = Field(
        None, description="Berichtsrate vor Anker in Sekunden"
    )

    # Konnektivität
    has_nmea_0183: bool = Field(default=True, description="NMEA 0183 Ausgang")
    has_nmea_2000: bool = Field(default=False, description="NMEA 2000 Anbindung")
    has_usb: bool = Field(default=True, description="USB-Schnittstelle")
    has_wifi: bool = Field(default=False, description="WiFi-Anbindung")
    has_bluetooth: bool = Field(default=False, description="Bluetooth")
    has_display: bool = Field(default=False, description="Integrierte Anzeige")

    # Physisch
    weight_g: float = Field(..., gt=0, description="Gewicht in Gramm")
    dimensions_mm: str = Field(..., description="Abmessungen LxBxH in mm (z.B. '130x110x30')")
    waterproof_rating: str = Field(
        default="IPX7", description="Wasserdichtigkeitsklasse"
    )

    # Elektrisch
    power_consumption_rx_w: float = Field(
        ..., gt=0, description="Stromaufnahme nur Empfang in Watt"
    )
    power_consumption_tx_w: Optional[float] = Field(
        None, description="Stromaufnahme beim Senden in Watt"
    )
    supply_voltage_v: str = Field(
        default="12-24", description="Versorgungsspannung"
    )

    # Kosten
    price_eur: Optional[float] = Field(None, ge=0, description="Listenpreis in EUR")

    # Zulassung
    certification: list[str] = Field(
        default_factory=list, description="Zulassungen (z.B. ['CE', 'FCC', 'USCG'])"
    )
    iec_standard: Optional[str] = Field(
        None, description="Referenz-IEC-Norm (z.B. 'IEC 62287-2')"
    )

    @field_validator("ais_class")
    @classmethod
    def validate_transmit_power_for_class(cls, v: AISClass) -> AISClass:
        """Validierung: AIS-Klasse bestimmt erlaubte Sendeleistung."""
        # Detaillierte Validierung in Kombination mit transmit_power_w
        # erfolgt im model_validator
        return v
```

### ANHANG K — Radar-Installation und Montage

```python
class RadarMountingSpec(BaseModel):
    """Radar-Montage-Spezifikation für eine Yacht."""

    model_config = {"from_attributes": True}

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    yacht_id: str = Field(..., description="Referenz zur Yacht")
    radar_spec_id: str = Field(..., description="Referenz zur Radar-Spezifikation")

    # Montageposition
    mount_position: MountPosition = Field(
        ..., description="Position der Radarantenne"
    )
    height_above_waterline_m: float = Field(
        ..., gt=0, description="Antennenhöhe über Wasserlinie in Metern"
    )
    offset_from_centerline_mm: float = Field(
        default=0, description="Versatz zur Schiffslängsachse in mm (+ = Steuerbord)"
    )
    offset_forward_from_gps_mm: float = Field(
        default=0, description="Versatz in Schiffslängsrichtung zur GPS-Antenne in mm"
    )

    # Blindsektoren
    blind_sectors: list[BlindSector] = Field(
        default_factory=list, description="Dokumentierte Blindsektoren"
    )

    # Mindestabstände
    distance_to_compass_m: float = Field(
        ..., ge=0, description="Abstand zum Magnetkompass in Metern"
    )
    distance_to_gps_m: float = Field(
        ..., ge=0, description="Abstand zur GPS-Antenne in Metern"
    )
    distance_to_vhf_m: float = Field(
        ..., ge=0, description="Abstand zur VHF-Antenne in Metern"
    )
    distance_to_wind_sensor_m: float = Field(
        ..., ge=0, description="Abstand zum Windmesser in Metern"
    )
    distance_to_persons_m: float = Field(
        ..., ge=0, description="Abstand zum nächsten Aufenthaltsbereich in Metern"
    )

    # Kabelführung
    cable_length_m: float = Field(
        ..., gt=0, description="Kabellänge Antenne → MFD/Prozessor in Metern"
    )
    cable_type: str = Field(
        ..., description="Kabeltyp (z.B. 'ethernet_cat5e', 'coax_rg213')"
    )

    # Heading-Sensor
    heading_sensor_type: HeadingSensorType = Field(
        ..., description="Typ des angeschlossenen Heading-Sensors"
    )
    heading_accuracy_deg: Optional[float] = Field(
        None, ge=0, description="Heading-Genauigkeit in Grad"
    )

    # Bewertung
    installation_date: Optional[datetime] = None
    installer: Optional[str] = None
    notes: Optional[str] = None

    @field_validator("distance_to_compass_m")
    @classmethod
    def validate_compass_distance(cls, v: float) -> float:
        if v < 2.0:
            import warnings
            warnings.warn(
                f"Abstand zum Kompass ({v}m) unterschreitet Empfehlung von 2,0 m! "
                "Deviation des Kompasses wahrscheinlich."
            )
        return v

    @field_validator("distance_to_gps_m")
    @classmethod
    def validate_gps_distance(cls, v: float) -> float:
        if v < 1.0:
            import warnings
            warnings.warn(
                f"Abstand zur GPS-Antenne ({v}m) unterschreitet Empfehlung von 1,0 m! "
                "GPS-Störungen möglich."
            )
        return v


class BlindSector(BaseModel):
    """Ein Blindsektor der Radarinstallation."""

    model_config = {"from_attributes": True}

    start_bearing_deg: float = Field(
        ..., ge=0, lt=360, description="Anfangspeilung des Blindsektors in Grad (relativ)"
    )
    end_bearing_deg: float = Field(
        ..., ge=0, lt=360, description="Endpeilung des Blindsektors in Grad (relativ)"
    )
    cause: str = Field(
        ..., description="Ursache des Blindsektors (z.B. 'Mast', 'Schornstein')"
    )
    severity: str = Field(
        default="partial", description="Schwere: 'total' oder 'partial'"
    )

    @property
    def width_deg(self) -> float:
        """Breite des Blindsektors in Grad."""
        if self.end_bearing_deg >= self.start_bearing_deg:
            return self.end_bearing_deg - self.start_bearing_deg
        return 360 - self.start_bearing_deg + self.end_bearing_deg
```

### ANHANG L — MARPA-Tracking und Zielanalyse

```python
class MARPATarget(BaseModel):
    """Ein MARPA/ARPA-verfolgtes Radar-Ziel."""

    model_config = {"from_attributes": True}

    target_id: int = Field(..., ge=0, description="Ziel-ID (fortlaufend)")
    timestamp: datetime = Field(
        default_factory=datetime.utcnow, description="Zeitstempel der Messung"
    )

    # Position relativ
    bearing_deg: float = Field(
        ..., ge=0, lt=360, description="Peilung zum Ziel in Grad (True)"
    )
    range_nm: float = Field(..., gt=0, description="Entfernung zum Ziel in Seemeilen")

    # Berechnete Werte
    course_deg: Optional[float] = Field(
        None, ge=0, lt=360, description="Berechneter Kurs des Ziels in Grad"
    )
    speed_kn: Optional[float] = Field(
        None, ge=0, description="Berechnete Geschwindigkeit des Ziels in Knoten"
    )
    cpa_nm: Optional[float] = Field(
        None, description="Closest Point of Approach in Seemeilen"
    )
    tcpa_min: Optional[float] = Field(
        None, description="Time to CPA in Minuten (negativ = bereits passiert)"
    )

    # Tracking-Qualität
    tracking_stable: bool = Field(
        default=False, description="Tracking stabil (>3 Umdrehungen)"
    )
    tracking_duration_s: float = Field(
        default=0, ge=0, description="Tracking-Dauer in Sekunden"
    )

    # AIS-Korrelation
    ais_correlated: bool = Field(
        default=False, description="Mit AIS-Ziel korreliert"
    )
    ais_mmsi: Optional[str] = Field(
        None, description="MMSI des korrelierten AIS-Ziels"
    )

    # Alarm
    cpa_alarm: bool = Field(
        default=False, description="CPA-Alarm ausgelöst"
    )
    tcpa_alarm: bool = Field(
        default=False, description="TCPA-Alarm ausgelöst"
    )

    @property
    def is_approaching(self) -> bool:
        """Nähert sich das Ziel?"""
        return self.tcpa_min is not None and self.tcpa_min > 0

    @property
    def threat_level(self) -> str:
        """Bedrohungsstufe basierend auf CPA/TCPA."""
        if self.cpa_nm is None or self.tcpa_min is None:
            return "unknown"
        if self.tcpa_min <= 0:
            return "passed"
        if self.cpa_nm < 0.2 and self.tcpa_min < 5:
            return "critical"
        if self.cpa_nm < 0.5 and self.tcpa_min < 10:
            return "warning"
        if self.cpa_nm < 1.0 and self.tcpa_min < 15:
            return "caution"
        return "safe"


class MARPAAlarmSettings(BaseModel):
    """MARPA/ARPA-Alarm-Einstellungen."""

    model_config = {"from_attributes": True}

    cpa_alarm_nm: float = Field(
        default=1.0, gt=0, description="CPA-Alarmschwelle in Seemeilen"
    )
    tcpa_alarm_min: float = Field(
        default=15.0, gt=0, description="TCPA-Alarmschwelle in Minuten"
    )
    guard_zone_1_enabled: bool = Field(default=False)
    guard_zone_1_inner_nm: Optional[float] = Field(None, ge=0)
    guard_zone_1_outer_nm: Optional[float] = Field(None, gt=0)
    guard_zone_1_start_deg: Optional[float] = Field(None, ge=0, lt=360)
    guard_zone_1_end_deg: Optional[float] = Field(None, ge=0, lt=360)
    guard_zone_2_enabled: bool = Field(default=False)
    guard_zone_2_inner_nm: Optional[float] = Field(None, ge=0)
    guard_zone_2_outer_nm: Optional[float] = Field(None, gt=0)
    guard_zone_2_start_deg: Optional[float] = Field(None, ge=0, lt=360)
    guard_zone_2_end_deg: Optional[float] = Field(None, ge=0, lt=360)
```

### ANHANG M — AIS-Nachrichtenmodelle

```python
class AISPositionReport(BaseModel):
    """AIS-Positionsbericht (Msg 1, 2, 3, 18)."""

    model_config = {"from_attributes": True}

    mmsi: str = Field(
        ..., min_length=9, max_length=9, description="9-stellige MMSI"
    )
    message_type: int = Field(
        ..., ge=1, le=27, description="AIS-Nachrichtentyp"
    )
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    # Navigation
    navigational_status: Optional[int] = Field(
        None, ge=0, le=15,
        description="Navigationsstatus (0=under way using engine, 1=at anchor, ...)"
    )
    rate_of_turn_deg_per_min: Optional[float] = Field(
        None, description="Drehrate in Grad/min"
    )
    speed_over_ground_kn: Optional[float] = Field(
        None, ge=0, le=102.2, description="SOG in Knoten"
    )
    course_over_ground_deg: Optional[float] = Field(
        None, ge=0, lt=360, description="COG in Grad"
    )
    true_heading_deg: Optional[float] = Field(
        None, ge=0, lt=360, description="Richtungsweisender Kurs in Grad"
    )

    # Position
    latitude: float = Field(
        ..., ge=-90, le=90, description="Breitengrad"
    )
    longitude: float = Field(
        ..., ge=-180, le=180, description="Längengrad"
    )
    position_accuracy: bool = Field(
        default=False, description="True = DGPS oder besser"
    )

    # Qualität
    raim_flag: bool = Field(
        default=False, description="RAIM in Betrieb"
    )

    @field_validator("mmsi")
    @classmethod
    def validate_mmsi(cls, v: str) -> str:
        if not v.isdigit():
            raise ValueError("MMSI muss nur aus Ziffern bestehen")
        return v


class AISStaticData(BaseModel):
    """AIS Statische und Reisedaten (Msg 5, 24)."""

    model_config = {"from_attributes": True}

    mmsi: str = Field(..., min_length=9, max_length=9, description="9-stellige MMSI")
    message_type: int = Field(..., description="AIS-Nachrichtentyp (5 oder 24)")
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    # Schiffsdaten
    imo_number: Optional[str] = Field(None, description="IMO-Nummer (7-stellig)")
    call_sign: Optional[str] = Field(None, max_length=7, description="Rufzeichen")
    vessel_name: Optional[str] = Field(
        None, max_length=20, description="Schiffsname"
    )
    ship_type: Optional[int] = Field(
        None, ge=0, le=99, description="Schiffstyp-Code"
    )

    # Abmessungen (Offset von AIS-Antenne)
    dim_bow_m: Optional[float] = Field(
        None, ge=0, description="Abstand Bug zur AIS-Antenne in Metern"
    )
    dim_stern_m: Optional[float] = Field(
        None, ge=0, description="Abstand Heck zur AIS-Antenne in Metern"
    )
    dim_port_m: Optional[float] = Field(
        None, ge=0, description="Abstand Backbord zur AIS-Antenne in Metern"
    )
    dim_starboard_m: Optional[float] = Field(
        None, ge=0, description="Abstand Steuerbord zur AIS-Antenne in Metern"
    )

    # Reisedaten (nur Msg 5)
    draught_m: Optional[float] = Field(
        None, ge=0, description="Tiefgang in Metern"
    )
    destination: Optional[str] = Field(
        None, max_length=20, description="Zielhafen"
    )
    eta: Optional[datetime] = Field(None, description="ETA")

    @property
    def length_m(self) -> Optional[float]:
        """Berechnete Schiffslänge."""
        if self.dim_bow_m is not None and self.dim_stern_m is not None:
            return self.dim_bow_m + self.dim_stern_m
        return None

    @property
    def beam_m(self) -> Optional[float]:
        """Berechnete Schiffsbreite."""
        if self.dim_port_m is not None and self.dim_starboard_m is not None:
            return self.dim_port_m + self.dim_starboard_m
        return None
```

### ANHANG N — Radar-Analyse und Bewertung

```python
class RadarPerformanceAnalysis(BaseModel):
    """Analyse der Radar-Leistungsfähigkeit einer Installation."""

    model_config = {"from_attributes": True}

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    yacht_id: str = Field(..., description="Referenz zur Yacht")
    radar_spec_id: str = Field(..., description="Referenz zur Radar-Spezifikation")
    mounting_spec_id: str = Field(..., description="Referenz zur Montage-Spezifikation")
    analysis_date: datetime = Field(default_factory=datetime.utcnow)
    confidence: ConfidenceLevel = Field(..., description="Confidence-Level der Analyse")

    # Reichweiten-Analyse
    radar_optical_range_nm: float = Field(
        ..., gt=0, description="Radaroptische Reichweite (Horizontberechnung) in nm"
    )
    effective_range_small_target_nm: float = Field(
        ..., gt=0,
        description="Effektive Reichweite für kleines Ziel (5 m² RCS) in nm"
    )
    effective_range_large_target_nm: float = Field(
        ..., gt=0,
        description="Effektive Reichweite für großes Ziel (1000 m² RCS) in nm"
    )
    min_detection_range_m: float = Field(
        ..., ge=0, description="Minimale Erfassungsentfernung in Metern"
    )

    # Auflösungs-Analyse
    range_resolution_m: float = Field(
        ..., gt=0, description="Entfernungsauflösung in Metern"
    )
    bearing_resolution_deg: float = Field(
        ..., gt=0, description="Azimutale Auflösung in Grad"
    )
    bearing_resolution_at_1nm_m: float = Field(
        ..., gt=0,
        description="Azimutale Auflösung in Metern bei 1 nm Entfernung"
    )

    # Blindsektor-Bewertung
    total_blind_sector_deg: float = Field(
        default=0, ge=0, lt=360,
        description="Gesamter Blindsektor in Grad"
    )
    blind_sector_rating: str = Field(
        default="excellent",
        description="Bewertung: excellent (<5°), good (<15°), acceptable (<30°), poor (>30°)"
    )

    # MARPA-Eignung
    marpa_suitable: bool = Field(
        ..., description="Für MARPA-Tracking geeignet"
    )
    marpa_heading_quality: str = Field(
        ..., description="Heading-Qualität für MARPA: excellent/good/marginal/insufficient"
    )

    # Gesamtbewertung
    overall_score: float = Field(
        ..., ge=0, le=100, description="Gesamtbewertung 0–100"
    )
    findings: list[RadarFinding] = Field(
        default_factory=list, description="Einzelbefunde"
    )
    recommendations: list[str] = Field(
        default_factory=list, description="Empfehlungen"
    )


class RadarFinding(BaseModel):
    """Einzelbefund der Radar-Analyse."""

    model_config = {"from_attributes": True}

    category: str = Field(..., description="Kategorie (z.B. 'reichweite', 'montage', 'emv')")
    severity: str = Field(
        ..., description="Schwere: 'info', 'hinweis', 'warnung', 'kritisch'"
    )
    title_de: str = Field(..., description="Titel auf Deutsch")
    description_de: str = Field(..., description="Beschreibung auf Deutsch")
    suggestion_de: Optional[str] = Field(
        None, description="Verbesserungsvorschlag auf Deutsch"
    )
    confidence: ConfidenceLevel = Field(..., description="Confidence-Level")
    location: Optional[str] = Field(None, description="Betroffener Bereich/Zone")
```

### ANHANG O — AIS-Analyse und Bewertung

```python
class AISInstallationAnalysis(BaseModel):
    """Analyse der AIS-Installation."""

    model_config = {"from_attributes": True}

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    yacht_id: str = Field(..., description="Referenz zur Yacht")
    ais_spec_id: str = Field(..., description="Referenz zur AIS-Spezifikation")
    analysis_date: datetime = Field(default_factory=datetime.utcnow)
    confidence: ConfidenceLevel = Field(..., description="Confidence-Level")

    # Klassen-Eignung
    ais_class_appropriate: bool = Field(
        ..., description="Ist die AIS-Klasse für das Einsatzprofil angemessen?"
    )
    ais_class_recommendation: Optional[AISClass] = Field(
        None, description="Empfohlene AIS-Klasse (falls Upgrade nötig)"
    )
    ais_class_rationale_de: Optional[str] = Field(
        None, description="Begründung der Empfehlung auf Deutsch"
    )

    # Antennen-Analyse
    antenna_type: str = Field(
        ..., description="Antennentyp (shared_splitter / dedicated_ais / combined_vhf)"
    )
    antenna_height_m: Optional[float] = Field(
        None, description="Antennenhöhe über Wasser in Metern"
    )
    splitter_model: Optional[str] = Field(
        None, description="VHF-Splitter-Modell (falls vorhanden)"
    )
    estimated_range_nm: float = Field(
        ..., gt=0, description="Geschätzte AIS-Reichweite in nm"
    )

    # NMEA-Integration
    nmea_connection_type: str = Field(
        ..., description="NMEA-Verbindungstyp (0183 / 2000 / usb / wifi)"
    )
    plotter_integration: bool = Field(
        ..., description="Korrekt in Kartenplotter integriert"
    )
    overlay_available: bool = Field(
        ..., description="AIS-Overlay auf Radar/Karte möglich"
    )

    # Sichtbarkeit
    verified_on_marine_traffic: bool = Field(
        default=False, description="Auf MarineTraffic.com verifiziert"
    )
    mmsi_correct: bool = Field(
        ..., description="MMSI korrekt programmiert"
    )

    # Gesamtbewertung
    overall_score: float = Field(
        ..., ge=0, le=100, description="Gesamtbewertung 0–100"
    )
    findings: list[AISFinding] = Field(
        default_factory=list, description="Einzelbefunde"
    )
    recommendations: list[str] = Field(
        default_factory=list, description="Empfehlungen"
    )


class AISFinding(BaseModel):
    """Einzelbefund der AIS-Analyse."""

    model_config = {"from_attributes": True}

    category: str = Field(
        ..., description="Kategorie (z.B. 'klasse', 'antenne', 'integration', 'sicherheit')"
    )
    severity: str = Field(
        ..., description="Schwere: 'info', 'hinweis', 'warnung', 'kritisch'"
    )
    title_de: str = Field(..., description="Titel auf Deutsch")
    description_de: str = Field(..., description="Beschreibung auf Deutsch")
    suggestion_de: Optional[str] = Field(
        None, description="Verbesserungsvorschlag auf Deutsch"
    )
    confidence: ConfidenceLevel = Field(..., description="Confidence-Level")
```

### ANHANG P — Radar/AIS-Systemkonfiguration

```python
class RadarAISSystemConfig(BaseModel):
    """Gesamtkonfiguration Radar + AIS einer Yacht."""

    model_config = {"from_attributes": True}

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    yacht_id: str = Field(..., description="Referenz zur Yacht")
    yacht_loa_m: float = Field(..., gt=0, description="Länge über alles in Metern")
    yacht_type: str = Field(
        ..., description="Yachttyp (sail/motor/catamaran/trawler/superyacht)"
    )
    operating_area: str = Field(
        ..., description="Einsatzgebiet (coastal/offshore/bluewater/inland)"
    )
    ce_category: Optional[str] = Field(
        None, description="CE-Design-Kategorie (A/B/C/D)"
    )

    # Radar-Konfiguration
    primary_radar: Optional[RadarSpecification] = Field(
        None, description="Primäres Radar"
    )
    secondary_radar: Optional[RadarSpecification] = Field(
        None, description="Sekundäres Radar (Backup/Ergänzung)"
    )
    primary_radar_mounting: Optional[RadarMountingSpec] = Field(
        None, description="Montage Primärradar"
    )
    secondary_radar_mounting: Optional[RadarMountingSpec] = Field(
        None, description="Montage Sekundärradar"
    )

    # AIS-Konfiguration
    ais_transponder: Optional[AISTransponderSpec] = Field(
        None, description="AIS-Transponder"
    )
    ais_antenna_type: str = Field(
        default="shared_splitter",
        description="AIS-Antennentyp (shared_splitter / dedicated / combined)"
    )
    vhf_splitter: Optional[str] = Field(
        None, description="VHF-Splitter-Modell"
    )

    # Heading-Sensor
    heading_sensor_type: HeadingSensorType = Field(
        ..., description="Heading-Sensor-Typ"
    )
    heading_sensor_model: Optional[str] = Field(
        None, description="Heading-Sensor-Modell"
    )
    heading_accuracy_deg: Optional[float] = Field(
        None, description="Heading-Genauigkeit in Grad"
    )

    # MOB-Ausrüstung
    ais_mob_count: int = Field(
        default=0, ge=0, description="Anzahl AIS-MOB-Geräte"
    )
    ais_mob_model: Optional[str] = Field(None, description="AIS-MOB-Modell")
    ais_sart_present: bool = Field(
        default=False, description="AIS-SART an Bord"
    )

    # Radarreflektor
    radar_reflector_type: Optional[str] = Field(
        None, description="Radarreflektor-Typ (passive / active_rte / none)"
    )
    radar_reflector_model: Optional[str] = Field(
        None, description="Radarreflektor-Modell"
    )

    # MFD-Integration
    mfd_brand: str = Field(..., description="Kartenplotter-Marke")
    mfd_model: str = Field(..., description="Kartenplotter-Modell")
    radar_overlay_enabled: bool = Field(
        default=True, description="Radar-Overlay auf Karte aktiviert"
    )
    ais_overlay_enabled: bool = Field(
        default=True, description="AIS-Overlay auf Karte aktiviert"
    )

    # Kosten
    total_system_cost_eur: Optional[float] = Field(
        None, ge=0, description="Gesamtkosten des Systems in EUR"
    )
    installation_cost_eur: Optional[float] = Field(
        None, ge=0, description="Installationskosten in EUR"
    )

    @property
    def has_radar(self) -> bool:
        """Mindestens ein Radar vorhanden."""
        return self.primary_radar is not None

    @property
    def has_ais(self) -> bool:
        """AIS-Transponder vorhanden."""
        return self.ais_transponder is not None

    @property
    def has_dual_radar(self) -> bool:
        """Dual-Radar-Installation."""
        return (
            self.primary_radar is not None
            and self.secondary_radar is not None
        )

    @property
    def collision_avoidance_rating(self) -> str:
        """Bewertung der Kollisionsverhütungsausstattung."""
        score = 0
        if self.primary_radar:
            score += 30
            if self.primary_radar.has_doppler:
                score += 10
            if self.primary_radar.has_marpa:
                score += 10
        if self.secondary_radar:
            score += 10
        if self.ais_transponder:
            if self.ais_transponder.ais_class == AISClass.CLASS_A:
                score += 20
            elif self.ais_transponder.ais_class == AISClass.CLASS_B_PLUS_SOTDMA:
                score += 15
            elif self.ais_transponder.ais_class == AISClass.CLASS_B_CSTDMA:
                score += 10
            elif self.ais_transponder.ais_class == AISClass.RECEIVER_ONLY:
                score += 5
        if self.heading_sensor_type == HeadingSensorType.SATELLITE_COMPASS:
            score += 10
        elif self.heading_sensor_type == HeadingSensorType.RATE_GYRO:
            score += 5
        if self.ais_mob_count > 0:
            score += 5
        if self.radar_reflector_type:
            score += 5

        if score >= 80:
            return "excellent"
        elif score >= 60:
            return "good"
        elif score >= 40:
            return "adequate"
        elif score >= 20:
            return "basic"
        return "insufficient"
```

### ANHANG Q — Fehlerbild-Modelle

```python
class RadarFaultPattern(BaseModel):
    """Radar-Fehlerbild für den Fehlerbild-Atlas."""

    model_config = {"from_attributes": True}

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    fault_code: str = Field(
        ..., description="Eindeutiger Fehlercode (z.B. 'RDR-001')"
    )
    title_de: str = Field(..., description="Fehlertitel auf Deutsch")
    description_de: str = Field(..., description="Symptom-Beschreibung auf Deutsch")
    confidence: ConfidenceLevel = Field(..., description="Confidence-Level")

    # Klassifikation
    severity: str = Field(
        ..., description="Schwere: 'kritisch', 'hoch', 'mittel', 'niedrig'"
    )
    category: str = Field(
        ..., description="Kategorie: 'sender', 'empfaenger', 'antenne', 'montage', "
                         "'emv', 'software', 'kabel'"
    )
    affects_safety: bool = Field(
        ..., description="Beeinträchtigt die Sicherheit"
    )

    # Diagnose
    possible_causes: list[str] = Field(
        ..., min_length=1, description="Mögliche Ursachen"
    )
    diagnostic_steps: list[str] = Field(
        ..., min_length=1, description="Diagnoseschritte"
    )
    visual_indicators: list[str] = Field(
        default_factory=list, description="Visuelle Erkennungsmerkmale"
    )

    # Behebung
    fix_steps: list[str] = Field(
        ..., min_length=1, description="Behebungsschritte"
    )
    requires_professional: bool = Field(
        ..., description="Erfordert professionellen Service"
    )
    estimated_repair_cost_eur: Optional[str] = Field(
        None, description="Geschätzte Reparaturkosten (z.B. '200-500 EUR')"
    )
    estimated_repair_time: Optional[str] = Field(
        None, description="Geschätzte Reparaturdauer (z.B. '2-4 Stunden')"
    )

    # Prävention
    prevention_measures: list[str] = Field(
        default_factory=list, description="Vorbeugende Maßnahmen"
    )
    inspection_interval: Optional[str] = Field(
        None, description="Empfohlenes Inspektionsintervall"
    )

    # AYDI-Scoring
    aydi_module_impact: list[str] = Field(
        default_factory=list,
        description="Betroffene AYDI-Module (z.B. ['compliance', 'ergonomics'])"
    )
    score_deduction: float = Field(
        ..., ge=0, le=100,
        description="Score-Abzug bei diesem Fehlerbild (0–100)"
    )


class AISFaultPattern(BaseModel):
    """AIS-Fehlerbild für den Fehlerbild-Atlas."""

    model_config = {"from_attributes": True}

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    fault_code: str = Field(
        ..., description="Eindeutiger Fehlercode (z.B. 'AIS-001')"
    )
    title_de: str = Field(..., description="Fehlertitel auf Deutsch")
    description_de: str = Field(..., description="Symptom-Beschreibung auf Deutsch")
    confidence: ConfidenceLevel = Field(..., description="Confidence-Level")

    # Klassifikation
    severity: str = Field(
        ..., description="Schwere: 'kritisch', 'hoch', 'mittel', 'niedrig'"
    )
    category: str = Field(
        ..., description="Kategorie: 'empfang', 'sendung', 'antenne', 'integration', "
                         "'konfiguration', 'splitter'"
    )
    affects_safety: bool = Field(
        ..., description="Beeinträchtigt die Sicherheit"
    )

    # Diagnose
    possible_causes: list[str] = Field(
        ..., min_length=1, description="Mögliche Ursachen"
    )
    diagnostic_steps: list[str] = Field(
        ..., min_length=1, description="Diagnoseschritte"
    )

    # Behebung
    fix_steps: list[str] = Field(
        ..., min_length=1, description="Behebungsschritte"
    )
    requires_professional: bool = Field(
        ..., description="Erfordert professionellen Service"
    )
    estimated_repair_cost_eur: Optional[str] = Field(
        None, description="Geschätzte Reparaturkosten"
    )

    # Prävention
    prevention_measures: list[str] = Field(
        default_factory=list, description="Vorbeugende Maßnahmen"
    )

    # AYDI-Scoring
    score_deduction: float = Field(
        ..., ge=0, le=100,
        description="Score-Abzug bei diesem Fehlerbild (0–100)"
    )
```

### ANHANG R — Radar-Reichweiten-Berechnung und Hilfsfunktionen

```python
import math
from typing import Optional

from pydantic import BaseModel, Field


class RadarRangeCalculation(BaseModel):
    """Berechnung der theoretischen Radar-Reichweite."""

    model_config = {"from_attributes": True}

    antenna_height_m: float = Field(
        ..., gt=0, description="Antennenhöhe über Wasser in Metern"
    )
    target_height_m: float = Field(
        default=5.0, gt=0, description="Zielhöhe über Wasser in Metern"
    )
    transmit_power_w: float = Field(
        ..., gt=0, description="Sendeleistung in Watt"
    )
    antenna_gain_dbi: float = Field(
        default=20.0, description="Antennengewinn in dBi"
    )
    target_rcs_m2: float = Field(
        default=10.0, gt=0, description="Radarquerschnitt des Ziels in m²"
    )
    frequency_ghz: float = Field(
        default=9.41, gt=0, description="Sendefrequenz in GHz"
    )
    receiver_sensitivity_dbm: float = Field(
        default=-100.0, description="Empfängerempfindlichkeit in dBm"
    )

    @property
    def optical_range_nm(self) -> float:
        """Radaroptische Reichweite in Seemeilen (Horizont-Berechnung)."""
        return 2.21 * (
            math.sqrt(self.antenna_height_m) + math.sqrt(self.target_height_m)
        )

    @property
    def wavelength_m(self) -> float:
        """Wellenlänge in Metern."""
        return 0.3 / self.frequency_ghz

    @property
    def range_resolution_m(self) -> Optional[float]:
        """Entfernungsauflösung — nur berechenbar wenn Pulsdauer bekannt."""
        return None  # Benötigt Pulsdauer als zusätzlichen Parameter

    @property
    def bearing_resolution_deg(self) -> float:
        """Azimutale Auflösung basierend auf Antennengewinn (Näherung)."""
        # Näherung: Strahlbreite ≈ 70 × λ / D
        # Antennengewinn G ≈ 4π × A_eff / λ²
        # Für Schlitzantenne: G ≈ 26000 / (θ_h × θ_v)
        # Vereinfachte Rückrechnung für horizontal beam width
        gain_linear = 10 ** (self.antenna_gain_dbi / 10)
        vertical_beam = 25.0  # Typischer Wert für Yachtradar
        horizontal_beam = 26000.0 / (gain_linear * vertical_beam)
        return max(horizontal_beam, 0.5)  # Minimum 0,5°


class RadarOpticalRangeTable(BaseModel):
    """Tabelle der radaroptischen Reichweiten für verschiedene Szenarien."""

    model_config = {"from_attributes": True}

    antenna_height_m: float = Field(..., gt=0)

    @property
    def range_to_small_boat_nm(self) -> float:
        """Reichweite zu kleinem Boot (Zielhöhe 2 m)."""
        return 2.21 * (math.sqrt(self.antenna_height_m) + math.sqrt(2.0))

    @property
    def range_to_sailboat_nm(self) -> float:
        """Reichweite zu Segelyacht (Zielhöhe 12 m Masttop)."""
        return 2.21 * (math.sqrt(self.antenna_height_m) + math.sqrt(12.0))

    @property
    def range_to_freighter_nm(self) -> float:
        """Reichweite zu Frachter (Zielhöhe 30 m Brücke)."""
        return 2.21 * (math.sqrt(self.antenna_height_m) + math.sqrt(30.0))

    @property
    def range_to_container_ship_nm(self) -> float:
        """Reichweite zu Containerschiff (Zielhöhe 50 m)."""
        return 2.21 * (math.sqrt(self.antenna_height_m) + math.sqrt(50.0))

    def to_summary_dict(self) -> dict:
        """Zusammenfassung als Dictionary."""
        return {
            "antenna_height_m": self.antenna_height_m,
            "range_to_small_boat_nm": round(self.range_to_small_boat_nm, 1),
            "range_to_sailboat_nm": round(self.range_to_sailboat_nm, 1),
            "range_to_freighter_nm": round(self.range_to_freighter_nm, 1),
            "range_to_container_ship_nm": round(
                self.range_to_container_ship_nm, 1
            ),
        }


class EMVComplianceCheck(BaseModel):
    """EMV-Konformitätsprüfung der Radar/AIS-Installation."""

    model_config = {"from_attributes": True}

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    yacht_id: str = Field(..., description="Referenz zur Yacht")
    check_date: datetime = Field(default_factory=datetime.utcnow)

    # Abstands-Checks
    radar_to_compass_m: float = Field(..., ge=0)
    radar_to_compass_ok: bool = Field(default=False)
    radar_to_gps_m: float = Field(..., ge=0)
    radar_to_gps_ok: bool = Field(default=False)
    radar_to_vhf_m: float = Field(..., ge=0)
    radar_to_vhf_ok: bool = Field(default=False)
    radar_to_wind_m: float = Field(..., ge=0)
    radar_to_wind_ok: bool = Field(default=False)
    radar_to_persons_m: float = Field(..., ge=0)
    radar_to_persons_ok: bool = Field(default=False)

    # Kabelführung
    signal_cables_separated: bool = Field(
        ..., description="Signal- und Leistungskabel getrennt verlegt"
    )
    cables_shielded: bool = Field(
        ..., description="Signalkabel ausreichend geschirmt"
    )
    ferrite_cores_installed: bool = Field(
        default=False, description="Ferritkerne an kritischen Kabeln"
    )

    # Erdung
    common_ground_bus: bool = Field(
        ..., description="Gemeinsame Erdungsschiene vorhanden"
    )
    radar_grounded: bool = Field(
        ..., description="Radar-Antenne ordnungsgemäß geerdet"
    )
    ais_grounded: bool = Field(
        ..., description="AIS-Transponder ordnungsgemäß geerdet"
    )

    # Ergebnis
    overall_pass: bool = Field(
        ..., description="Gesamtergebnis: bestanden"
    )
    issues: list[str] = Field(
        default_factory=list, description="Festgestellte Mängel"
    )
    recommendations: list[str] = Field(
        default_factory=list, description="Empfehlungen"
    )

    def evaluate(self) -> None:
        """Bewertet die EMV-Konformität und setzt die *_ok Felder."""
        self.radar_to_compass_ok = self.radar_to_compass_m >= 2.0
        self.radar_to_gps_ok = self.radar_to_gps_m >= 1.0
        self.radar_to_vhf_ok = self.radar_to_vhf_m >= 1.5
        self.radar_to_wind_ok = self.radar_to_wind_m >= 1.0
        self.radar_to_persons_ok = self.radar_to_persons_m >= 0.5

        self.issues = []
        if not self.radar_to_compass_ok:
            self.issues.append(
                f"Radar-Kompass-Abstand {self.radar_to_compass_m}m < 2,0m Minimum"
            )
        if not self.radar_to_gps_ok:
            self.issues.append(
                f"Radar-GPS-Abstand {self.radar_to_gps_m}m < 1,0m Minimum"
            )
        if not self.radar_to_vhf_ok:
            self.issues.append(
                f"Radar-VHF-Abstand {self.radar_to_vhf_m}m < 1,5m Minimum"
            )
        if not self.radar_to_wind_ok:
            self.issues.append(
                f"Radar-Wind-Abstand {self.radar_to_wind_m}m < 1,0m Minimum"
            )
        if not self.radar_to_persons_ok:
            self.issues.append(
                f"Radar-Personen-Abstand {self.radar_to_persons_m}m < 0,5m Minimum"
            )
        if not self.signal_cables_separated:
            self.issues.append("Signal- und Leistungskabel nicht getrennt verlegt")
        if not self.common_ground_bus:
            self.issues.append("Keine gemeinsame Erdungsschiene")

        self.overall_pass = len(self.issues) == 0
```

---

*Ende der AYDI Wissensdatei 23.03 — Radar und AIS*
*Version 1.0.0 | 2026-05-08 | AYDI Research*
