---
title: "Navigation und Elektronik Grundlagen — Kartenplotter, GPS, AIS, Radar, NMEA 2000, Funkgeräte"
kategorie: "23 Navigation und Elektronik"
unterkategorie: "23.01 Grundlagen"
version: "1.0.0"
datum: "2026-05-13"
autor: "AYDI Research"
status: "validated"
confidence_quellen:
  - measured: "IMO-Normen, IEC 61162, ITU-R M.493, NMEA 2000 Spezifikation, CE-Zertifizierungen"
  - documented: "Hersteller-TDS, Installationsanleitungen, BSH-Richtlinien, Praxistests"
  - estimated: "Erfahrungswerte, Werft-Konsens, Charterflotten-Feedback, Regattaerfahrung"
---

# 23.01 — Navigation und Elektronik Grundlagen im Yachtbau: Vollständige Wissensreferenz

> **AYDI Wissensdatei 23.01** — Kategorie 23: Navigation und Elektronik
> **Confidence-Quelle:** measured (IMO/IEC/NMEA-Normen, Hersteller-Datenblätter), documented (Installationsanleitungen, BSH-Richtlinien), estimated (Erfahrungswerte, Werft-Konsens)
> **Letzte Aktualisierung:** 2026-05-13

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
11. [ANHANG A–H — Fallstudien](#anhang-a-h)
12. [ANHANG I–R — Pydantic v2 Modelle](#anhang-i-r)

---

## 1. Einführung und Übersicht

### 1.1 Definition und Abgrenzung

Navigationselektronik umfasst die Gesamtheit aller elektronischen Systeme an Bord einer Yacht, die der Positionsbestimmung, Kurssteuerung, Umgebungserfassung, Kommunikation und Informationsintegration dienen. Im Gegensatz zur traditionellen Navigation mit Seekarte, Zirkel und Sextant hat die elektronische Navigation in den letzten 40 Jahren eine vollständige Transformation der Brückenausrüstung bewirkt.

Diese Wissensdatei 23.01 bildet die Grundlagendatei für die gesamte Kategorie 23 (Navigation und Elektronik). Sie definiert:

1. **Physikalische und technische Grundlagen** — Signalausbreitung, Satellitennavigation, Radarphysik, digitale Datenbusse
2. **Normen und Regelwerk** — IEC 61162, NMEA 0183/2000, ITU-R Funkreglement, CE-Kennzeichnung
3. **Systemarchitektur** — Wie die einzelnen Komponenten (GPS, AIS, Radar, MFD, Funk) zusammenwirken
4. **Herstellerlandschaft** — Die sechs dominierenden Hersteller und ihre Produktphilosophien
5. **Fehlerbilder und Diagnose** — Systematische Fehlererfassung für die AYDI-Analysepipeline

### 1.2 Historische Entwicklung der Yachtnavigation

**Vor 1970 — Klassische Navigation:**
- Terrestrische Navigation: Kompass, Lot, Log, Peilscheibe
- Astronomische Navigation: Sextant, Nautisches Jahrbuch, Zeitzeichenempfänger
- Funknavigation ab 1940er: Decca, Loran-A, Consol
- Erste Echolote: Raytheon DE-711 (1948), Bendix DR-19
- Radaranlagen nur auf Handelsschiffen und Großyachten (>50 ft)

**1970–1985 — Erste Elektronifizierung:**
- 1972: Transit-Satellitennavigationssystem (Navy Navigation Satellite System) erstmals auf Yachten
- 1974: Loran-C wird Standardsystem für nordamerikanische Küstengewässer
- 1978: Erster GPS-Satellit (NAVSTAR Block I) im Orbit
- Erste digitale Echolote mit LCD-Anzeige
- B&G Hydra-System (1980): erstes integriertes Regattasystem mit analogem Datenbus
- Autohelm (später Raymarine) bringt bezahlbare Autopiloten für Yachten
- Furuno FCV-561 als erstes kompaktes Farb-Echolot

**1985–2000 — GPS-Revolution:**
- 1993: GPS-Vollkonstellation (24 Satelliten) erreicht
- 1995: SA (Selective Availability) begrenzt zivile Genauigkeit auf ~100m
- 2000-05-01: SA abgeschaltet — zivile Genauigkeit springt auf ~15m
- NMEA 0183 wird De-facto-Standard für Datenkommunikation
- Erste Kartenplotter: Raytheon RL-9 (1989), Raymarine Pathfinder (1997)
- DSC (Digital Selective Calling) wird für UKW-Funk eingeführt
- AIS-Konzept entsteht aus IMO-Anforderungen für SOLAS-Schiffe

**2000–2010 — Vernetzung und Integration:**
- 2003: NMEA 2000 (IEC 61162-3) veröffentlicht — CAN-Bus für Marine
- 2004: AIS Class B für Sportboote spezifiziert (ITU-R M.1371-5)
- Raymarine E-Series (2004): erstes weit verbreitetes MFD-Netzwerk
- Garmin steigt mit der GPSMap-Serie in den Marinemarkt ein
- Simrad (Navico) und B&G vereinen sich unter Navico-Dach
- Breitband-Radar (Navico, 2008): erstes Halbleiter-Radar ohne Magnetron
- WiFi-Anbindung an Mobilgeräte beginnt

**2010–2020 — Touchscreen und Cloud:**
- Kapazitive Touchscreens ersetzen resistive Displays
- Raymarine Axiom (2017): LightHouse 3 Betriebssystem
- Garmin GPSMAP 8400/8600 mit integriertem CHIRP-Sonar
- Simrad NSS evo3 / NSX mit Halo-Radarintegration
- B&G Zeus3 und Vulcan als Regatta-fokussierte MFDs
- Furuno NavNet TZtouch2/TZtouch3 für Premium-Segment
- AIS-Transponder werden in vielen europäischen Gewässern faktisch Standard
- SiriusXM/Navtex-Integration für Wetterinformationen

**2020–heute — KI-Unterstützung und Konsolidierung:**
- Garmin GPSMAP 9000 Serie (2024) mit AMOLED-Displays
- Raymarine Axiom 2 XL mit NVIDIA-basierter Objekterkennung
- Simrad NSX (2023) als nächste Generation
- NMEA OneNet (Ethernet-basiert) in Entwicklung
- Fusion von Navico (Simrad, B&G, Lowrance) unter Brunswick
- Iridium GO! exec und Starlink Maritime für Hochsee-Konnektivität
- Digitaler Zwilling (Digital Twin) für Navigationssystemplanung

### 1.3 Bedeutung im AYDI-Analysesystem

Im Kontext des AYDI-Analysesystems beeinflusst die Navigationselektronik folgende Module:

- **Ergonomie-Modul:** MFD-Positionierung, Blickwinkel, Bedienbarkeit am Steuerstand, Ablesbarkeit bei Sonnenlicht
- **Compliance-Modul:** Pflichtausrüstung nach Fahrtgebiet (SBF/SSS/SHS), CE-Kennzeichnung, Funkausstattung
- **Kosten-Modul:** Navigationselektronik typisch 8–25% der Gesamtausrüstungskosten (bootsklassenabhängig)
- **Produktions-Modul:** Kabelführung, NMEA-Backbone, Displayausschnitte, Antennenpositionierung
- **Gewichts-Modul:** Masttopp-Antennen, Radardom beeinflussen Schwerpunktlage
- **Materialien-Modul:** UV-Beständigkeit von Displays, Korrosionsschutz von Antennen und Steckern
- **Service-Modul:** Software-Updates, Kartenupdates, Kalibrierung, typische Ausfallmuster

### 1.4 Marktüberblick

Der globale Markt für Marine-Navigationselektronik wird auf ca. 3,5–4,2 Mrd. USD geschätzt (2025), mit einer jährlichen Wachstumsrate von 5–7%. Im Segment der Sportboot- und Yachtelektronik dominieren sechs Hersteller:

**Marktanteile Yacht-Navigationselektronik (geschätzt, 2025):**

| Hersteller | Konzern | Marktanteil | Kernkompetenz |
|------------|---------|-------------|---------------|
| Garmin | Garmin Ltd. | 28–32% | MFD, GPS, Sonar, Autopilot |
| Raymarine | FLIR/Teledyne | 18–22% | MFD, Radar, Autopilot, Kameras |
| Simrad | Navico/Brunswick | 12–16% | MFD, Radar, Sonar, Autopilot |
| B&G | Navico/Brunswick | 6–9% | Regattainstrumente, MFD |
| Furuno | Furuno Electric | 8–12% | Radar, MFD, Sonar (Premium) |
| Humminbird/Lowrance | Navico/Brunswick | 10–14% | Fishfinder, Einstiegssegment |
| Sonstige | — | 5–10% | Nischen, OEM, Regional |

**Preissegmente für typische MFD-Systeme (komplett installiert):**

| Bootsklasse | Einfach | Standard | Premium |
|-------------|---------|----------|---------|
| 8–10m Segelboot | 1.500–3.000 EUR | 3.000–6.000 EUR | 6.000–12.000 EUR |
| 10–14m Segelyacht | 3.000–6.000 EUR | 6.000–15.000 EUR | 15.000–35.000 EUR |
| 12–18m Motoryacht | 4.000–8.000 EUR | 8.000–20.000 EUR | 20.000–50.000 EUR |
| 18–24m Yacht | 8.000–18.000 EUR | 18.000–45.000 EUR | 45.000–120.000 EUR |
| 24m+ Superyacht | 20.000–50.000 EUR | 50.000–150.000 EUR | 150.000–500.000+ EUR |

---

## 2. Grundlagen und Theorie

### 2.1 Satellitennavigation (GNSS)

#### 2.1.1 Systeme im Überblick

GNSS (Global Navigation Satellite System) ist der Oberbegriff für alle satellitengestützten Positionsbestimmungssysteme:

**GPS (USA — NAVSTAR):**
- Betreiber: U.S. Space Force
- Konstellation: 31 aktive Satelliten auf 6 Orbitalebenen
- Orbitalhöhe: 20.200 km, Umlaufzeit 11h 58min
- Frequenzen: L1 (1575,42 MHz), L2 (1227,60 MHz), L5 (1176,45 MHz)
- Zivile Genauigkeit: 3–5m (95%), mit SBAS 1–2m
- Modernisierung: GPS III (ab 2018) mit L1C- und L5-Signal, verbesserte Störfestigkeit

**GLONASS (Russland):**
- Betreiber: Russische Streitkräfte / Roskosmos
- Konstellation: 24 aktive Satelliten auf 3 Orbitalebenen
- Orbitalhöhe: 19.100 km, Umlaufzeit 11h 15min
- Frequenzen: L1 (1602,0 MHz + k×0,5625), L2 (1246,0 MHz + k×0,4375)
- Zivile Genauigkeit: 5–10m (95%)
- Vorteil: Bessere Abdeckung in hohen Breitengraden (>60°N)

**Galileo (EU):**
- Betreiber: European GNSS Agency (EUSPA)
- Konstellation: 28 Satelliten (2025), Zielkonstellation 30
- Orbitalhöhe: 23.222 km, Umlaufzeit 14h 07min
- Frequenzen: E1 (1575,42 MHz), E5a (1176,45 MHz), E5b (1207,14 MHz), E6 (1278,75 MHz)
- Open Service Genauigkeit: 1–3m (95%)
- High Accuracy Service (HAS): 20cm horizontal mit PPP-Korrekturen (kostenlos ab 2023)
- Besonderheit: SAR-Rückkanal (Return Link Service) für Seenotsender

**BeiDou (China, BDS-3):**
- Betreiber: China Satellite Navigation Office
- Konstellation: 30 MEO + 3 GEO + 3 IGSO Satelliten
- Globale Abdeckung seit Juni 2020
- Genauigkeit: 3–5m global, <1m in Asien-Pazifik

#### 2.1.2 Multi-GNSS-Empfänger

Moderne Marineempfänger nutzen gleichzeitig GPS + GLONASS + Galileo (+ optional BeiDou), was die Zahl der sichtbaren Satelliten auf 40–60 erhöht. Vorteile:

- **Schnellere Erstortung (TTFF):** Cold Start 25–35s (statt 45–60s bei GPS only)
- **Bessere Genauigkeit:** 1–3m (statt 3–5m bei GPS only) durch verbesserte Geometrie (DOP-Werte)
- **Höhere Verfügbarkeit:** Auch in Häfen mit Abschattung durch Gebäude/Masten zuverlässig
- **Redundanz:** Ausfall eines Systems wird durch andere kompensiert

**Differenzkorrekturen (DGNSS/SBAS):**

| System | Region | Genauigkeit | Kosten |
|--------|--------|-------------|--------|
| EGNOS (SBAS) | Europa | 1–2m | Kostenlos |
| WAAS (SBAS) | Nordamerika | 1–2m | Kostenlos |
| MSAS (SBAS) | Japan | 1–2m | Kostenlos |
| Galileo HAS | Global | 0,2m | Kostenlos |
| RTK (NTRIP) | Küstennah | 0,02m | Abo 50–200 EUR/a |
| Marinestar | Global (Satellit) | 0,1m | Abo 500–2000 EUR/a |
| StarFix | Offshore | 0,05m | Abo (kommerziell) |

#### 2.1.3 GPS-Antennenpositionierung

Die Qualität der Positionsbestimmung hängt maßgeblich von der Antenneninstallation ab:

**Optimale Antennenposition:**
- Freie Sicht zum Horizont, 360° möglichst bis 5° Elevation
- Mindestabstand zu Radar-Scanner: 1,0m (Raymarine-Empfehlung: 1,5m)
- Mindestabstand zu UKW-Antenne: 1,0m
- Mindestabstand zu Iridium/Satcom: 0,5m
- Keine Metallstrukturen direkt unter der Antenne (Reflexionen)
- Möglichst nahe am Schiffsmittelpunkt (weniger Auswirkung von Rollbewegungen)

**Fehlerquellen bei der Positionsbestimmung:**

| Fehlerquelle | Auswirkung | Gegenmaßnahme |
|--------------|-----------|----------------|
| Atmosphärische Verzögerung (Ionosphäre) | 2–5m | Dual-Frequency-Empfänger (L1+L5) |
| Troposphärische Verzögerung | 0,5–2m | SBAS-Korrekturen |
| Mehrwegeausbreitung (Multipath) | 1–10m | Antennenposition optimieren, Choke-Ring-Antenne |
| Abschattung durch Segel/Rigg | Variable | Multi-GNSS, zwei Antennen |
| Satelliten-Geometrie (DOP) | Variable | Multi-GNSS erhöht Satellitenzahl |
| Empfängerrauschen | 0,3–1m | Hochwertiger Empfänger |

**Heading-Sensor (GPS-Kompass):**
Zwei GPS-Antennen in definiertem Abstand (typisch 0,5–2m) ermöglichen die Bestimmung der Vorauslinie ohne Magnetkompass:
- Genauigkeit: 0,5–1° (bei 1m Abstand), 0,1–0,3° (bei 2m Abstand)
- Vorteile: Keine Deviation, sofort korrekt, auch bei Strom/Drift
- Hersteller: Furuno SC-50/SC-70, Simrad HS80/HS90, Garmin GPS 24xd, Raymarine EV-400

### 2.2 Radar — Physikalische Grundlagen

#### 2.2.1 Radarfunktionsprinzip

Radar (RAdio Detection And Ranging) sendet kurze elektromagnetische Impulse aus und empfängt deren Reflexionen (Echos) von Objekten. Aus Laufzeit und Richtung des Echos werden Entfernung und Peilung des Ziels bestimmt.

**Grundgleichung (vereinfacht):**
```
Pr = (Pt × Gt × Gr × λ² × σ) / ((4π)³ × R⁴)

Pr = Empfangsleistung
Pt = Sendeleistung
Gt = Gewinn der Sendeantenne
Gr = Gewinn der Empfangsantenne
λ  = Wellenlänge
σ  = Radar-Rückstreuquerschnitt (RCS) des Ziels
R  = Entfernung zum Ziel
```

Die R⁴-Abhängigkeit bedeutet: Bei doppelter Entfernung sinkt die Empfangsleistung auf 1/16. Dies begrenzt die Reichweite grundsätzlich.

**Radarfrequenzen im Marineeinsatz:**

| Band | Frequenzbereich | Wellenlänge | Einsatz |
|------|----------------|-------------|---------|
| X-Band | 9,3–9,5 GHz | ~3 cm | Standard-Yachtradar, hohe Auflösung |
| S-Band | 2,9–3,1 GHz | ~10 cm | Großschiffe, bessere Regenunterdrückung |

Für Yachten ist ausschließlich das X-Band relevant (9,41 GHz ± 30 MHz nach ITU).

#### 2.2.2 Magnetron- vs. Halbleiter-Radar

**Magnetron-Radar (Pulse-Radar):**
- Sendeelement: Magnetron (Vakuumröhre) erzeugt Hochleistungsimpulse
- Typische Sendeleistung: 2–25 kW (Spitzenleistung)
- Impulsbreite: 50 ns – 1,2 µs
- PRF (Pulse Repetition Frequency): 800–3000 Hz
- Aufwärmzeit: 60–120 Sekunden
- Lebensdauer Magnetron: 3.000–10.000 Betriebsstunden
- Vorteile: Hohe Spitzenleistung, gute Langstreckenreichweite (>48 nm bei 25 kW)
- Nachteile: Aufwärmzeit, Magnetron-Verschleiß, Nahbereich-Blindzone, hoher Stromverbrauch

**Halbleiter-Radar (Solid-State / Broadband):**
- Sendeelement: GaN (Galliumnitrid) oder GaAs (Galliumarsenid) Transistoren
- Funktionsprinzip: FMCW (Frequency Modulated Continuous Wave) oder Pulskompressions-Radar
- Typische Sendeleistung: 20–50 W (Dauerleistung) — entspricht 2–4 kW Magnetron-Äquivalent
- Keine Aufwärmzeit: Sofort betriebsbereit
- Lebensdauer: >50.000 Stunden (praktisch wartungsfrei)
- Nahbereich: Exzellent, bis 6m Minimum-Reichweite
- Vorteile: Energieeffizient (15–30W vs. 50–150W), keine Hochspannung, sofort an, besser im Nahbereich
- Nachteile: Geringere Maximalreichweite (typisch 24–36 nm), höherer Anschaffungspreis

**Vergleichstabelle:**

| Parameter | Magnetron 4kW | Halbleiter FMCW |
|-----------|--------------|-----------------|
| Sendeleistung | 4 kW Peak | 25 W CW |
| Stromaufnahme | 50–80 W | 17–30 W |
| Aufwärmzeit | 90 s | 0 s |
| Min. Reichweite | 25–50 m | 6–20 m |
| Max. Reichweite | 48 nm | 24–36 nm |
| Auflösung Nahbereich | Mittel | Exzellent |
| Magnetron-Ersatz | Alle 5–8 Jahre | Entfällt |
| Gewicht Scanner | 6–12 kg | 3–7 kg |
| Preis (2025) | 1.500–4.000 EUR | 2.000–5.000 EUR |

#### 2.2.3 Radar-Antennentypen

**Radom (geschlossene Kuppel):**
- Durchmesser: 18" (45 cm), 24" (60 cm)
- Vorteile: Kompakt, sicher (keine rotierenden Teile exponiert), geringer Windwiderstand
- Nachteile: Geringere Richtwirkung (Strahlbreite 5–6°), begrenzte Reichweite
- Einsatz: Segelyachten bis 14m, Motorboote bis 12m

**Open-Array (offener Strahler):**
- Breite: 2 ft (60 cm), 3 ft (90 cm), 4 ft (120 cm), 6 ft (180 cm)
- Vorteile: Schmalere Strahlbreite (1,5–4°), höhere Zielauflösung, größere Reichweite
- Nachteile: Größer, schwerer, rotierende Teile, Gefahr bei Berührung (Magnetron: Mikrowellen-Exposition)
- Einsatz: Yachten ab 12m, Motorboote ab 10m, Offshore-Segler

**Strahlbreite und Antennenlänge:**
```
Horizontale Strahlbreite ≈ 70 × (λ / L)

λ = Wellenlänge (0,032 m bei X-Band)
L = Antennenlänge in Metern

Beispiel 4ft (1,22m): 70 × (0,032 / 1,22) = 1,8°
Beispiel 24" Radom (0,30m effektiv): 70 × (0,032 / 0,30) = 7,5°
```

#### 2.2.4 MARPA und Kollisionsverhütung

MARPA (Mini Automatic Radar Plotting Aid) ist die Yachtversion des ARPA-Systems der Berufsschifffahrt:

- Automatische Zielverfolgung (Target Tracking) von 10–30 Zielen gleichzeitig
- Berechnung von CPA (Closest Point of Approach) und TCPA (Time to CPA)
- Alarm bei CPA < eingestellter Schwellwert (typisch 0,5–1,0 nm)
- Berechnung von Kurs und Geschwindigkeit der verfolgten Ziele
- Voraussetzung: Heading-Sensor (Kompass) und Log (Geschwindigkeit über Grund oder durchs Wasser)

**Radar-Overlay auf Seekarte:**
Moderne MFDs können das Radarbild als transparente Schicht über die Seekarte legen. Voraussetzung:
- Heading-Sensor mit <1° Genauigkeit
- GPS-Position
- Korrekte Radar-Versatzwerte (Offset der Radarantenne zum GPS)

### 2.3 AIS — Automatic Identification System

#### 2.3.1 Funktionsprinzip

AIS sendet und empfängt automatisch Schiffsdaten über UKW-Funk (VHF) auf zwei dedizierten Frequenzen:
- **AIS 1:** 161,975 MHz (Kanal 87B)
- **AIS 2:** 162,025 MHz (Kanal 88B)

Das System verwendet TDMA (Time Division Multiple Access) — die verfügbare Sendezeit wird in 2.250 Zeitschlitze pro Minute aufgeteilt. Jedes Schiff belegt autonom einen oder mehrere Zeitschlitze.

**Übertragene Daten:**

| Datentyp | Inhalt | Aktualisierung |
|----------|--------|---------------|
| Statisch | MMSI, Name, Rufzeichen, IMO-Nr., Schiffstyp, Abmessungen | Alle 6 min / bei Änderung |
| Dynamisch | Position (GPS), SOG, COG, Heading, ROT, Nav-Status | 2s – 3min (geschwindigkeitsabhängig) |
| Reisebezogen | Tiefgang, Ladung, Zielhafen, ETA, Personen | Alle 6 min / bei Änderung |
| Sicherheit | Freitext-Sicherheitsnachrichten | Bei Bedarf |

#### 2.3.2 AIS-Geräteklassen

**Class A Transponder:**
- Pflicht für SOLAS-Schiffe (>300 BRT international, >500 BRT national)
- Sendeleistung: 12,5 W
- Sendeintervall: 2–10 Sekunden (fahrtabhängig)
- SOTDMA (Self-Organizing TDMA)
- Empfangspflicht: Ja
- Kosten: 2.000–5.000 EUR
- Für Yachten: Nur bei Fahrt in SOLAS-pflichtigen Gebieten oder >500 BRT

**Class B Transponder (Standard CS):**
- Freiwillig für Sportboote
- Sendeleistung: 2 W
- Sendeintervall: 30 Sekunden (>2 kn) bis 3 Minuten (<2 kn)
- CSTDMA (Carrier Sense TDMA) — nachrangig zu Class A
- Geringerer Datensatz (kein IMO-Nr., kein Tiefgang, kein Zielhafen)
- Kosten: 300–800 EUR
- Typisch für Segelyachten 8–15m

**Class B+ Transponder (SOTDMA für Sportboote):**
- Sendeleistung: 5 W
- Sendeintervall: 5–30 Sekunden (wie Class A, aber kürzerer Prioritätsrang)
- SOTDMA wie Class A — bessere Sichtbarkeit in dichten Verkehrsgebieten
- Erweiterter Datensatz gegenüber Standard Class B
- Kosten: 600–1.500 EUR
- Empfehlung für Yachten >12m und Kanalpassagen

**AIS-Empfänger (Receive Only):**
- Nur Empfang, kein Senden — Yacht ist für andere nicht sichtbar
- Kosten: 100–300 EUR
- Sinnvoll als Ergänzung, nicht als alleiniges AIS-Gerät

**AIS-SART (Search and Rescue Transmitter):**
- Seenotsender auf AIS-Basis
- Sendet AIS-Nachricht Typ 14 mit Position
- Reichweite: typisch 5–10 nm
- Batterielaufzeit: 96 Stunden
- Alternativer/Ergänzung zu Radar-SART
- Kosten: 200–500 EUR

#### 2.3.3 AIS-Integration in MFD-Systeme

Alle modernen MFDs können AIS-Ziele als Symbole auf der Seekarte darstellen:

**Standard-AIS-Symbole (IEC 62288):**
- Dreieck: AIS-Ziel mit Kursvektor
- Ausgefülltes Dreieck: Aktiviertes/selektiertes Ziel
- Kreis: Schlafendes Ziel (keine aktuelle Datenaktualisierung)
- Rotes Quadrat: Gefahrenziel (CPA-Alarm)
- Grün: Klasse B
- Blau: Klasse A
- Gelb: ATON (Navigationszeichen mit AIS-Transponder)
- Rot: SAR-Transponder

**CPA/TCPA-Berechnung:**
Das MFD berechnet für jedes AIS-Ziel:
- CPA: Geringste zu erwartende Annäherung unter Beibehaltung beider Kurse/Geschwindigkeiten
- TCPA: Zeitdauer bis zur engsten Annäherung
- Alarmschwellen konfigurierbar (typisch CPA < 0,5 nm UND TCPA < 15 min)

### 2.4 NMEA 0183 — Legacy-Datenbus

#### 2.4.1 Technische Spezifikation

NMEA 0183 (National Marine Electronics Association) ist seit den 1980er Jahren der Standard für serielle Datenkommunikation zwischen Marinegeräten:

**Physikalische Schicht:**
- Elektrisch: RS-422 (differenziell) oder RS-232 (single-ended)
- Baudrate: 4.800 Baud (Standard), 38.400 Baud (AIS, High Speed)
- Topologie: Ein Sender (Talker) → mehrere Empfänger (Listener)
- Unidirektional: Jede Leitung hat genau einen Sender
- Kabellänge: Max. 15m (RS-232), max. 300m (RS-422)

**Datenformat:**
```
$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,47.0,M,,*47

$ = Satzanfang
GP = Talker-ID (GP=GPS, GL=GLONASS, GN=Multi-GNSS, AI=AIS)
GGA = Satztyp (Global Positioning System Fix Data)
, = Feldtrenner
*47 = Prüfsumme (XOR aller Zeichen zwischen $ und *)
\r\n = Satzende
```

**Wichtige NMEA-0183-Sätze für die Yachtnavigation:**

| Satz | Inhalt | Quelle |
|------|--------|--------|
| GGA | GPS-Fix, Position, Qualität, Satellitenzahl | GPS |
| RMC | Recommended Minimum — Position, Kurs, Geschwindigkeit | GPS |
| GLL | Geographische Position (Lat/Lon) | GPS |
| VTG | Kurs und Geschwindigkeit über Grund | GPS |
| HDT | True Heading | Kompass |
| HDM | Magnetic Heading | Kompass |
| VHW | Geschwindigkeit durchs Wasser, Heading | Log/Kompass |
| MWV | Windgeschwindigkeit und -richtung (relativ/true) | Windmesser |
| DBT | Tiefe unter Geber | Echolot |
| DPT | Tiefe mit Offset | Echolot |
| MTW | Wassertemperatur | Echolot/Sensor |
| RSA | Ruderwinkel | Rudersensor |
| XTE | Cross Track Error | Plotter/Autopilot |
| APB | Autopilot-Steuerdaten | Plotter |
| VDM/VDO | AIS-Rohdaten (AIVDM/AIVDO) | AIS-Empfänger |
| DSC/DSE | DSC-Rufdaten | UKW-Funk |

#### 2.4.2 Grenzen von NMEA 0183

- **Ein-Sender-Prinzip:** Jedes Kabel hat genau einen Talker. Für N Geräte untereinander → N×(N-1) Verbindungen
- **Geringe Bandbreite:** 4.800 Baud ≈ 480 Zeichen/s — reicht für ~10 Sätze/Sekunde
- **Keine Geräteerkennung:** Geräte müssen manuell konfiguriert werden
- **Kein Plug-and-Play:** Kabelverbindungen physisch herstellen und Satzfilter setzen
- **Keine Standardisierung der Stecker:** Hersteller verwenden proprietäre Stecker oder offene Kabelenden

Trotz dieser Grenzen ist NMEA 0183 weiterhin relevant, da:
- Viele Autopiloten, Windmesser und Echolote noch NMEA 0183 ausgeben
- Ältere Funkgeräte nur NMEA 0183 für DSC-Position können
- Einfache Verdrahtung für einzelne Punkt-zu-Punkt-Verbindungen
- Gateways (NMEA 0183 → NMEA 2000) sind günstig (50–200 EUR)

### 2.5 NMEA 2000 — Moderner Datenbus

#### 2.5.1 Technische Spezifikation

NMEA 2000 (IEC 61162-3) basiert auf dem CAN-Bus (Controller Area Network, ISO 11898) und wurde speziell für die Marine-Datenkommunikation entwickelt:

**Physikalische Schicht:**
- Basis: CAN 2.0B mit 29-Bit-Identifiern
- Baudrate: 250 kbit/s
- Topologie: Linearer Bus (Backbone) mit Stichleitungen (Drop Lines)
- Maximale Backbone-Länge: 100m (Micro-C), 200m (Mid-Size)
- Maximale Drop-Line-Länge: 6m
- Maximale Geräte: 50 pro Netzwerk
- Abschlusswiderstand: 120 Ω an beiden Enden des Backbones
- Spannungsversorgung: 12V DC über den Bus (LEN = Load Equivalence Number, max. 30 LEN pro Netzteil)

**Steckersystem:**

| Typ | Bezeichnung | Pin-Anzahl | Einsatz |
|-----|------------|-----------|---------|
| Micro-C | DeviceNet Micro | 5-polig M12 | Standard für Yachten bis 24m |
| Mid-Size | DeviceNet Mini | 5-polig | Größere Yachten, dickeres Kabel |

**Pin-Belegung Micro-C:**

| Pin | Farbe | Funktion |
|-----|-------|----------|
| 1 | Weiß | Shield/Drain |
| 2 | Blau | CAN-L (NET-L) |
| 3 | Schwarz | GND (NET-C) |
| 4 | Rot | +12V (NET-S) |
| 5 | Gelb (oder Weiß) | CAN-H (NET-H) |

#### 2.5.2 Netzwerkarchitektur

```
[Terminierung 120Ω]---[Backbone]---[T-Stück]---[T-Stück]---...---[Terminierung 120Ω]
                                        |              |
                                   [Drop Line]    [Drop Line]
                                        |              |
                                    [GPS-Empf.]  [Windgeber]

Backbone: Durchgehende Kabelstrecke mit T-Stücken
Drop Line: Stichleitung vom T-Stück zum Gerät (max. 6m)
Terminierung: 120Ω an beiden Enden (genau 2 Stück!)
Power: Mindestens 1 Netzteil am Backbone
```

**Typisches NMEA-2000-Netzwerk einer 12m-Segelyacht:**

| Gerät | Funktion | LEN | PGN (Beispiele) |
|-------|----------|-----|-----------------|
| GPS-Empfänger | Position, COG, SOG | 1 | 129025, 129026, 126992 |
| Windgeber | AWS, AWA | 1 | 130306 |
| Triducer | Tiefe, Log, Temp | 1 | 128267, 128259, 130311 |
| Kompass/Heading | Heading, Pitch, Roll | 1 | 127250 |
| MFD (Plotter) | Anzeige, Routing | 2 | Viele (Empfänger) |
| Autopilot-Computer | Steuerung | 3 | 127237, 127245 |
| AIS-Transponder | Senden/Empfang | 2 | 129038, 129039, 129040 |
| Motordaten-Gateway | RPM, Temp, Öldruck | 1 | 127488, 127489 |
| Tankgeber × 2 | Füllstand | 1 | 127505 |
| Batteriemonitor | Spannung, Strom, SOC | 1 | 127508 |
| **Gesamt** | | **14 LEN** | |

#### 2.5.3 PGN — Parameter Group Numbers

Daten werden in PGNs (Parameter Group Numbers) organisiert, vergleichbar mit NMEA-0183-Satztypen:

**Wichtige PGNs:**

| PGN | Bezeichnung | Update-Rate | Daten |
|-----|------------|-------------|-------|
| 126992 | System Time | 1/s | Datum, Uhrzeit |
| 127250 | Vessel Heading | 10/s | Heading (True/Magnetic) |
| 127251 | Rate of Turn | 10/s | Drehrate |
| 127257 | Attitude | 10/s | Yaw, Pitch, Roll |
| 127488 | Engine Parameters, Rapid | 10/s | RPM |
| 127489 | Engine Parameters, Dynamic | 1/s | Öldruck, Temp, Stunden |
| 127505 | Fluid Level | 0,5/s | Tankinhalt |
| 127508 | Battery Status | 1/s | Spannung, Strom, SOC, Temp |
| 128259 | Speed, Water Referenced | 2/s | Geschwindigkeit durchs Wasser |
| 128267 | Water Depth | 2/s | Tiefe unter Geber |
| 129025 | Position, Rapid | 4/s | Latitude, Longitude |
| 129026 | COG/SOG, Rapid | 4/s | Kurs und Geschwindigkeit ü.G. |
| 129029 | GNSS Position Data | 1/s | Erweiterte GPS-Daten |
| 129038 | AIS Class A Report | Variabel | Class-A-Zieldaten |
| 129039 | AIS Class B Report | Variabel | Class-B-Zieldaten |
| 129540 | GNSS Sats in View | 1/s | Sichtbare Satelliten |
| 130306 | Wind Data | 2/s | Windgeschwindigkeit, -richtung |
| 130310 | Environmental Parameters | 0,5/s | Wassertemp, Lufttemp, Druck |
| 130311 | Environmental Parameters | 0,5/s | Temperatur, Feuchte |

#### 2.5.4 Herstellerkompatibilität und Zertifizierung

Jedes NMEA-2000-Gerät muss von der NMEA zertifiziert sein. Die Zertifizierung prüft:
- Korrekte Implementierung der PGNs
- Elektromagnetische Verträglichkeit (EMV)
- Elektrische Spezifikation (Busbelastung, Spannungsbereiche)
- Address-Claim-Verfahren

**Praxis-Kompatibilität:** Trotz Zertifizierung gibt es Inkompatibilitäten:
- Garmin-spezifische PGNs (z.B. proprietäre Sonar-Daten)
- Raymarine SeaTalkNG = NMEA 2000 mit proprietären Steckern (5-poliger runder Stecker, aber elektrisch kompatibel via Adapter)
- Simrad SimNet = NMEA 2000 mit proprietären Steckern (9-polig, Adapter erhältlich)
- B&G nutzt SimNet-Stecker (identisch mit Simrad)

**SeaTalkNG ↔ NMEA 2000:**
Raymarine SeaTalkNG ist physisch ein NMEA-2000-Netzwerk mit anderem Steckersystem. Alle Standard-PGNs werden korrekt übertragen. Adapterkabel (A06045, A06075) sind erhältlich. SeaTalkNG-spezifische Daten (z.B. erweiterte Autopilotdaten) funktionieren nur zwischen Raymarine-Geräten.

### 2.6 UKW-Seefunk (VHF Marine Radio)

#### 2.6.1 Grundlagen

UKW-Seefunk (VHF Marine Band) ist das primäre Kommunikationsmittel auf See im Küstenbereich:

**Frequenzbereich:** 156,000–174,000 MHz
**Reichweite:** Quasi-optisch, typisch 15–30 nm (abhängig von Antennenhöhe)
**Kanalraster:** 25 kHz (International) oder 12,5 kHz (einige Regionen)
**Modulationsarten:** FM (Analog), DSC (Digital), AIS (auf Sonderkanälen)

**Reichweitenberechnung (vereinfacht):**
```
Reichweite (nm) ≈ 2,2 × (√h₁ + √h₂)

h₁ = Antennenhöhe Sender (Meter)
h₂ = Antennenhöhe Empfänger (Meter)

Beispiel: Yacht (h₁=15m) ↔ Küstenfunkstelle (h₂=100m)
R ≈ 2,2 × (√15 + √100) = 2,2 × (3,87 + 10) = 30,5 nm
```

#### 2.6.2 DSC — Digital Selective Calling

DSC (Digitaler Selektivruf) ist ein digitales Rufsystem auf Kanal 70 (156,525 MHz), das automatisiert Notrufe, Einzelrufe und Gruppenrufe ermöglicht:

**Rufarten:**
- **Distress (Seenotfall):** Automatischer Notruf mit Position, MMSI, Notrufart → an alle Stationen
- **Urgency:** Dringende Meldung, aber kein unmittelbarer Seenotfall
- **Safety:** Sicherheitsbezogene Meldung (z.B. Treibgut, Wetterwarnung)
- **Routine:** Normaler Ruf an eine einzelne Station (MMSI)
- **Group Call:** Ruf an eine Gruppe (Gruppen-MMSI)

**DSC-Notruf-Sequenz:**
1. Taste "Distress" (rote Abdeckung) 5 Sekunden drücken
2. Funkgerät sendet automatisch: MMSI + Position (GPS) + Uhrzeit + Notrufart
3. Küstenfunkstelle empfängt und bestätigt (Acknowledgement)
4. Sprachkommunikation auf Kanal 16 (156,800 MHz)

**GPS-Anbindung des Funkgeräts:**
Kritisch! Ohne GPS-Anbindung enthält der DSC-Notruf keine Position. Verbindung über:
- NMEA 0183 (GGA- oder RMC-Satz) — bei den meisten Geräten
- NMEA 2000 (PGN 129029) — bei neueren Geräten
- Integrierter GPS-Empfänger — bei einigen aktuellen Modellen (z.B. Icom IC-M510, Standard Horizon GX6500)

#### 2.6.3 UKW-Antenneninstallation

**Antennentypen:**
- **Stabantenne (Whip):** 1,0–2,4m, Gewinn 3–6 dBi, Standard für Segelyachten am Masttopp
- **Kolinearantenne:** 0,5–1,0m, Gewinn 3 dBi, für Backstay- oder Geländermontage
- **Emergency-Antenne:** Kurze Notantenne (0,3m) für MOB-Situationen

**Montageempfehlungen:**
- Masttopp: Beste Reichweite (höchste Position), aber längste Kabelwege (Verluste)
- Pushpit/Heckkorb: Leicht zugänglich, aber geringe Höhe (7–12 nm Reichweite)
- Fly Bridge: Gut für Motorboote, mittlere Höhe

**Kabelverluste:**
| Kabeltyp | Verlust bei 156 MHz/10m | Max. empfohlene Länge |
|----------|------------------------|----------------------|
| RG-58 | 1,8 dB | 10m |
| RG-8X | 1,2 dB | 20m |
| RG-213 | 0,8 dB | 30m |
| Aircell 7 | 0,6 dB | 40m |
| LMR-400 | 0,4 dB | 50m |

**Faustregel:** Gesamtverlust Kabel + Stecker sollte <3 dB bleiben (halbe Leistung).

#### 2.6.4 Pflichtausrüstung nach Fahrtgebiet (Deutschland)

| Fahrtgebiet | Funkausrüstung Pflicht | Empfehlung |
|-------------|----------------------|------------|
| Binnenschifffahrt | UBI-Funkzeugnis, UKW Binnenfunk | — |
| Küste (SBF See) | Keine Funkpflicht für Sportboote <12m | UKW mit DSC dringend empfohlen |
| Küste (SKS/SSS) | UKW mit DSC (SRC-Zeugnis) empfohlen | UKW + AIS Class B |
| Hochsee (SHS) | UKW + GW/KW (LRC-Zeugnis) empfohlen | UKW + GW/KW + Satcom + EPIRB |

**Funkzeugnisse:**
- **SRC (Short Range Certificate):** UKW-Seefunk mit DSC, reichweitenabhängig
- **LRC (Long Range Certificate):** UKW + GW/KW + Satcom, Weltweite Kommunikation
- **UBI (UKW-Sprechfunkzeugnis Binnenschifffahrt):** Nur Binnenfunk

### 2.7 GMDSS — Global Maritime Distress and Safety System

#### 2.7.1 Seegebiete

Das GMDSS definiert vier Seegebiete, die die Pflichtausrüstung bestimmen:

| Seegebiet | Definition | Kommunikationsmittel |
|-----------|-----------|---------------------|
| A1 | UKW-Reichweite einer Küstenfunkstelle (20–30 nm) | UKW/DSC |
| A2 | GW-Reichweite einer Küstenfunkstelle (~150 nm) | UKW/DSC + GW/DSC |
| A3 | Inmarsat-Abdeckung (70°N – 70°S) | UKW + GW + Inmarsat/KW |
| A4 | Restgebiet (Polargebiete) | UKW + GW + KW |

**Für Sportboote relevant:**
- Meiste europäische Küstenreviere: A1 (UKW ausreichend)
- Kanalüberquerung, Biskaya, Mittelmeer-Überquerung: A1/A2
- Atlantiküberquerung: A3 (Satcom empfohlen)

#### 2.7.2 EPIRB und PLB

**EPIRB (Emergency Position Indicating Radio Beacon):**
- Frequenz: 406 MHz (Cospas-Sarsat-Satellit) + 121,5 MHz (Homing)
- Sendet MMSI/ID, Position (integriertes GPS), Notrufart
- Registrierung beim BSH (Deutschland) oder zuständiger Behörde Pflicht
- Batterielebensdauer: 48 Stunden Sendedauer, 10 Jahre Standby
- Automatische Auslösung bei Wasserkontakt (Hydrostatik) oder manuell
- Kosten: 400–1.200 EUR

**PLB (Personal Locator Beacon):**
- Wie EPIRB, aber personenbezogen (nicht schiffsbezogen)
- Kleiner, leichter, an Rettungsweste tragbar
- Sendezeit: 24 Stunden (kürzer als EPIRB)
- Keine automatische Auslösung
- Kosten: 250–500 EUR

### 2.8 Autopilot-Grundlagen

#### 2.8.1 Systemkomponenten

Ein Autopilot-System besteht aus:

1. **Steuercomputer (Course Computer):** Verarbeitet Sensordaten und berechnet Ruderkommandos
2. **Heading-Sensor:** Elektronischer Kompass (Fluxgate oder MEMS) mit Neigungskompensation
3. **Ruderrückmeldung (Rudder Feedback):** Potentiometer oder Hall-Sensor am Ruderschaft
4. **Antriebseinheit (Drive Unit):** Hydraulisch, elektrisch-linear, oder mechanisch (Tillersteuerung)
5. **Bedieneinheit (Control Head):** Bedienpanel mit Kursanzeige und Steuertasten

#### 2.8.2 Steuermodi

| Modus | Funktion | Eingabe | Anwendung |
|-------|----------|---------|-----------|
| Standby | Autopilot inaktiv | — | Handsteuerung |
| Auto (Kompasskurs) | Hält magnetischen/wahren Kurs | Heading-Sensor | Langstrecke, offenes Wasser |
| Wind | Hält scheinbaren Windwinkel (AWA) | Windgeber | Segeln am Wind/Raumschotskurs |
| Track (NAV) | Folgt Route/Kursversatz (XTE) | MFD/GPS | Routennavigation |
| NoDrift | Hält GPS-Kurs über Grund (COG) | GPS | Strom-/Windversatz-Korrektur |

#### 2.8.3 Dimensionierung

**Antriebsleistung nach Bootstyp:**

| Bootstyp | Verdrängung | Antriebstyp | Leistung |
|----------|-------------|-------------|----------|
| Segelboot 7–9m | 2–4 t | Tiller-Pilot | 50–100 W |
| Segelboot 9–12m | 4–10 t | Linear-Antrieb | 100–200 W |
| Segelboot 12–16m | 8–20 t | Linear oder Hydraulik | 200–400 W |
| Segelboot 16–22m | 15–40 t | Hydraulik | 400–1.000 W |
| Motorboot 8–12m | 3–8 t | Linear oder Hydraulik | 150–300 W |
| Motorboot 12–18m | 8–25 t | Hydraulik | 400–1.200 W |
| Motorboot 18–24m | 20–60 t | Hydraulik | 800–2.500 W |

**Ruder-Reaktionszeit:**
- Hart Backbord bis Hart Steuerbord: <8 Sekunden (Empfehlung)
- Zu langsam: Schiff läuft aus dem Ruder bei Welle/Böe
- Zu schnell: Übersteuern, hoher Energieverbrauch, Verschleiß

### 2.9 Echolot und Sonar

#### 2.9.1 Grundlagen

Echolote messen die Wassertiefe durch Aussenden eines Schallimpulses und Messung der Laufzeit des Echos vom Gewässergrund:

```
Tiefe = (Schallgeschwindigkeit × Laufzeit) / 2

Schallgeschwindigkeit in Seewasser: ~1.500 m/s (variiert mit Temperatur, Salzgehalt, Druck)
```

**Geberfrequenzen:**

| Frequenz | Strahlbreite | Eindringtiefe | Auflösung | Einsatz |
|----------|-------------|---------------|-----------|---------|
| 50 kHz | 40–60° | >1.000 m | Gering | Tiefwasser, Fischsuche |
| 83 kHz | 20–40° | 500–800 m | Mittel | Allzweck |
| 200 kHz | 10–20° | 200–400 m | Hoch | Flachwasser, Navigation |
| 455 kHz | 2–5° | 50–100 m | Sehr hoch | SideScan, DownScan |
| 800 kHz | 1–3° | 30–60 m | Extrem hoch | StructureScan |
| 1 MHz | 0,5–2° | 20–40 m | Extrem hoch | ForwardScan |

**CHIRP-Technologie:**
Konventionelle Echolote senden auf einer Festfrequenz. CHIRP (Compressed High-Intensity Radiated Pulse) variiert die Frequenz innerhalb eines Impulses (z.B. 150–250 kHz). Vorteile:
- Höhere Auflösung bei gleichzeitig größerer Reichweite
- Bessere Zielunterscheidung (Fisch vs. Grund)
- Geringere Sendeleistung erforderlich

#### 2.9.2 Geber-Typen und Installation

**Einbau-Varianten:**

| Typ | Beschreibung | Qualität | Eignung |
|-----|-------------|----------|---------|
| Transom-Mount | Außen am Spiegel | Gut, aber Luftblasen bei Fahrt | Motorboote bis 10m |
| Durchbruch (Thru-Hull) | Bronze-/Kunststoff-Durchbruch | Optimal | Segelyachten, Motorboote >10m |
| In-Hull (Shoot-Through) | Innenseite des Rumpfes eingeklebt | Akzeptabel bei GFK-Rumpf ohne Kern | Einfache Installation |
| Retractable | Versenkbar in Seekasten | Optimal + wartungsfreundlich | Performance-Segelyachten |

**Durchbruch-Materialien:**
- **Bronze:** Standard für GFK- und Holzrümpfe, langlebig, erfordert Opferanode
- **Kunststoff (Airmar TH-):** Für GFK-Rümpfe, kein Galvanikproblem, günstiger
- **Edelstahl:** Selten für Echolotgeber, eher für Speed-Logs
- **ACHTUNG:** Bei Aluminiumrümpfen NIEMALS Bronze-Durchbrüche (galvanische Korrosion!)

### 2.10 WiFi und Bluetooth an Bord

#### 2.10.1 WiFi-Anbindung von Mobilgeräten

Alle modernen MFDs bieten integriertes WiFi, das zwei Funktionen erfüllt:

**WiFi als Access Point (MFD → Tablet/Smartphone):**
- MFD spannt ein eigenes WiFi-Netzwerk auf
- Tablet/Smartphone verbindet sich und zeigt MFD-Daten über Hersteller-App an
- Raymarine: Raymarine App (iOS/Android) — Spiegelung des MFD-Bildschirms
- Garmin: ActiveCaptain App — Daten, Karten-Updates, Community
- Simrad/B&G: Simrad/B&G App — Daten, Remote-Steuerung
- Furuno: NavNet Remote App — Daten und Kartenansicht
- Reichweite: typisch 10–20m (innerhalb der Yacht)

**WiFi als Client (MFD → Marina-WiFi / Router):**
- MFD verbindet sich mit einem vorhandenen WiFi-Netzwerk
- Firmware-Updates herunterladen
- Karten-Updates herunterladen
- Cloud-Synchronisation (Routen, Wegpunkte)
- Wetterinformationen laden

**Typische WiFi-Architektur an Bord:**
```
[Marina WiFi / Starlink / 4G-Router]
            |
     [Marine Router (z.B. Pepwave, GL.iNet)]
            |
    +-------+-------+
    |       |       |
  [MFD]  [Tablet] [Laptop]
```

#### 2.10.2 Bluetooth-Verbindungen

Bluetooth wird im Marine-Bereich primär für Folgendes eingesetzt:
- **Funk-Windmesser:** B&G WS320, Garmin gWind Wireless → Bluetooth oder ANT+ zum MFD
- **Handfunkgerät-Headset:** Bluetooth-Headset an Icom IC-M94DE
- **Multimedia:** Fusion-Stereo-Steuerung über Bluetooth
- **Sensoren:** Temperatur-/Feuchte-Sensoren, Bilgenpumpe-Monitoring

Bluetooth ist KEIN Ersatz für NMEA 2000 — die Bandbreite und Latenz sind für Echtzeit-Navigation ungeeignet. Bluetooth wird ausschließlich für Komfort-Funktionen und nicht-sicherheitskritische Daten eingesetzt.

### 2.11 Ethernet-Vernetzung an Bord

#### 2.11.1 Marine-Ethernet

Moderne MFD-Systeme nutzen zusätzlich zu NMEA 2000 ein Ethernet-Netzwerk für datenintensive Anwendungen:

**Typische Ethernet-Verbindungen:**
- MFD ↔ MFD (Multidisplay-Konfigurationen)
- MFD ↔ Radar-Scanner
- MFD ↔ Black-Box-Sonar
- MFD ↔ IP-Kameras
- MFD ↔ Mediasystem (Fusion, Sonos Marine)
- Router/Switch ↔ WiFi-Bridge (für Tablet-Apps)

**Herstellerspezifische Implementierungen:**
- **Raymarine:** RayNet-Stecker (spezielles Ethernet-Kabel mit wasserdichtem Stecker), Switch HS5
- **Garmin:** Marine Network (proprietäre Stecker), GMS 10 Network Port Expander
- **Simrad/B&G:** Ethernet (Standard-RJ45 mit wasserdichter Tülle)
- **Furuno:** Ethernet (Standard-RJ45 oder proprietär je nach Modell)

**NMEA OneNet (in Entwicklung):**
- Basiert auf Ethernet (100 Mbit/s, perspektivisch 1 Gbit/s)
- Soll langfristig NMEA 2000 für datenintensive Anwendungen ergänzen
- UDP-basiert mit standardisierten PGN-Äquivalenten
- Unterstützt größere Datenmengen (Radar-Rohdaten, Videostreams)
- Erwartete Marktreife: 2026–2028
- Physikalisch: Standard-Ethernet (Cat5e/Cat6 Marine-Grade)
- Koexistenz mit NMEA 2000: OneNet ersetzt CAN-Bus NICHT, sondern ergänzt für Daten >250kBit/s

**Ethernet-Kabelempfehlungen für Marine-Einsatz:**

| Kabeltyp | Schirmung | Einsatz | Max. Länge |
|----------|----------|---------|-----------|
| Cat5e Marine (tinned) | S/FTP | Standard für MFD-Vernetzung | 100m |
| Cat6 Marine (tinned) | S/FTP | High-Performance, Radar-Daten | 100m |
| Herstellerspezifisch (RayNet, Garmin) | Integriert | Fertig konfektioniert mit Wasserdichtstecker | Bis 20m (Standardlängen) |

**Wichtig:** Standard-Land-Ethernet-Kabel (nicht verzinnt, nicht UV-beständig, nicht seewasserresistent) sind für den dauerhaften Einsatz an Bord NICHT geeignet. Marine-Grade-Kabel mit verzinnten Kupferleitern und UV-beständiger Ummantelung verwenden!

---

## 3. Typenübersicht

### 3.1 Kartenplotter / MFD

Siehe ausführlich Wissensdatei **23.02 — Kartenplotter und MFD**.

**Kurzübersicht Kategorien:**

| Kategorie | Displaygröße | Typische Yachtgröße | Preisbereich |
|-----------|-------------|---------------------|-------------|
| Einstieg | 5–7" | 6–9m | 500–1.500 EUR |
| Standard | 7–9" | 8–12m | 1.000–3.000 EUR |
| Premium | 9–12" | 10–16m | 2.500–6.000 EUR |
| Großformat | 12–16" | 14–22m | 4.000–12.000 EUR |
| Profi/Superyacht | 16–24" | 18m+ | 8.000–25.000 EUR |

### 3.2 Radar

Siehe ausführlich Wissensdatei **23.03 — Radar und AIS**.

**Kurzübersicht:**

| Typ | Leistung | Reichweite | Yachtgröße | Preis |
|-----|----------|-----------|------------|-------|
| Halbleiter-Radom 18" | 20 W | 24 nm | 8–12m | 1.500–3.000 EUR |
| Halbleiter-Radom 24" | 25 W | 36 nm | 10–16m | 2.500–5.000 EUR |
| Magnetron-Radom 24" | 4 kW | 48 nm | 10–16m | 1.500–3.500 EUR |
| Open-Array 3ft | 4–6 kW | 72 nm | 14–22m | 3.500–8.000 EUR |
| Open-Array 4ft | 6–12 kW | 96 nm | 18m+ | 5.000–15.000 EUR |
| Open-Array 6ft | 12–25 kW | 96+ nm | 24m+ | 10.000–30.000 EUR |

### 3.3 AIS-Transponder

| Typ | Sendeleistung | Intervall | Kosten | Empfehlung |
|-----|--------------|-----------|--------|------------|
| Empfänger (RX) | — | — | 100–300 EUR | Einstieg, Ergänzung |
| Class B (CS) | 2 W | 30 s | 300–800 EUR | Segelyachten 8–14m |
| Class B+ (SO) | 5 W | 5–30 s | 600–1.500 EUR | Yachten 12–20m, viel Berufsverkehr |
| Class A | 12,5 W | 2–10 s | 2.000–5.000 EUR | Yachten >20m, Charter, gewerblich |

### 3.4 UKW-Funkgeräte

| Typ | Sendeleistung | DSC | Besonderheit | Preis |
|-----|--------------|-----|-------------|-------|
| Handfunkgerät | 1/5/6 W | Nein (Ausnahme: Icom IC-M94DE) | Tragbar, wasserdicht | 80–300 EUR |
| Festeinbau Standard | 1/25 W | Klasse D | Basisstation | 200–600 EUR |
| Festeinbau Premium | 1/25 W | Klasse D | GPS integriert, AIS-Empfänger | 500–1.200 EUR |
| Festeinbau + AIS TX | 1/25 W | Klasse D | Integrierter AIS Class B Transponder | 800–2.000 EUR |
| GW/KW-Seefunk | 1–150 W | Klasse A/D | SSB-Funk für Langfahrt | 1.500–4.000 EUR |

### 3.5 Autopilot-Systeme

| Kategorie | Bootstyp | Antrieb | Preisbereich |
|-----------|----------|---------|-------------|
| Pinnen-Pilot | Segelboot 6–9m | Elektrisch, Tiller-Arm | 400–1.500 EUR |
| Innenbord-Linear | Segelboot 9–14m | Elektr. Linearantrieb | 1.500–4.000 EUR |
| Innenbord-Hydraulik | Segelboot 14–22m | Hydraulik-Pumpe | 4.000–12.000 EUR |
| Hydraulik Premium | Motor/Segel 18m+ | Hydraulik-Pumpe groß | 8.000–25.000 EUR |

### 3.6 Instrumente und Sensoren

Siehe Wissensdatei **23.05 — Instrumente und Sensoren**.

**Kurzübersicht Sensoren:**

| Sensor | Messgröße | Schnittstelle | Preis |
|--------|----------|---------------|-------|
| Windgeber (Masttopp) | AWA, AWS | NMEA 2000 / 0183 | 300–1.200 EUR |
| Triducer (Durchbruch) | Tiefe, Speed, Temp | NMEA 2000 / 0183 | 200–800 EUR |
| Kompass (Fluxgate) | Heading | NMEA 2000 / 0183 | 300–1.000 EUR |
| GPS-Kompass (Dual) | Heading, Position | NMEA 2000 | 1.500–5.000 EUR |
| Ruder-Referenz | Ruderwinkel | NMEA 2000 / Analog | 150–500 EUR |
| Barometer (digital) | Luftdruck | NMEA 2000 | 100–300 EUR |
| Motordaten-Gateway | RPM, Temp, Druck | NMEA 2000 (J1939/analog) | 200–800 EUR |

---

## 4. Produktlinien und Spezifikationen

### 4.1 Raymarine Axiom / Axiom 2

**Hersteller:** Raymarine (Teledyne FLIR, Großbritannien/USA)
**Produktfamilie:** Axiom, Axiom+, Axiom Pro, Axiom 2 XL
**Betriebssystem:** LightHouse 4 (Axiom 2), LightHouse 3 (Axiom/Axiom+)

**Axiom 2 Serie (2024):**

| Modell | Display | Auflösung | Helligkeit | Prozessor | Preis (ca.) |
|--------|---------|-----------|-----------|-----------|-------------|
| Axiom 2 XL 9 | 9" IPS | 1280×720 | 1.500 nit | Quad-Core | 2.200 EUR |
| Axiom 2 XL 12 | 12,1" IPS | 1280×800 | 1.500 nit | Quad-Core | 3.200 EUR |
| Axiom 2 XL 16 | 15,6" IPS | 1920×1080 | 1.500 nit | Quad-Core | 5.500 EUR |
| Axiom 2 Pro 9 | 9" IPS | 1280×720 | 1.500 nit | Quad-Core | 2.800 EUR |
| Axiom 2 Pro 12 | 12,1" IPS | 1280×800 | 1.500 nit | Quad-Core | 4.000 EUR |
| Axiom 2 Pro 16 | 15,6" IPS | 1920×1080 | 1.500 nit | Quad-Core | 6.500 EUR |

**Besonderheiten Raymarine:**
- LightHouse 4 mit intuitiver Bedienung, App-ähnliches Interface
- RealVision 3D Sonar (Axiom Pro/RV-Modelle)
- ClearCruise AR (Augmented Reality): Kamera-basierte Objekterkennung mit AIS-/Karten-Overlay
- Integration mit Raymarine Evolution Autopilot (SeaTalkNG/NMEA 2000)
- Quantum 2 Radar (CHIRP Halbleiter) und Magnum Radar (Open Array)
- Axiom 2 XL mit NVIDIA-basierter KI-Objekterkennung
- RayNet-Ethernet für MFD-Vernetzung und Radar

**Ökosystem:**
- Windgeber: Raymarine i60/i70s oder Tacktick-Funkwindmesser
- Autopilot: Evolution EV-100/EV-200/EV-400
- AIS: AIS700 (Class B+ Transponder)
- Funk: Ray63/73/90 (kein eigener VHF-Hersteller, aber nahtlose DSC-Integration)
- Kameras: CAM220/CAM210 IP-Kameras für AR-Overlay
- App: Raymarine App für iOS/Android (Remote-Anzeige und Steuerung)

### 4.2 Garmin GPSMAP Serie

**Hersteller:** Garmin Ltd. (USA/Schweiz)
**Produktfamilie:** GPSMAP 7x3, GPSMAP 9x3, GPSMAP 8x00, GPSMAP 9000
**Betriebssystem:** Garmin Marine OS (proprietär)

**GPSMAP 9000 Serie (2024):**

| Modell | Display | Auflösung | Helligkeit | Besonderheit | Preis (ca.) |
|--------|---------|-----------|-----------|-------------|-------------|
| GPSMAP 9x3 7" | 7" IPS | 1024×600 | 1.800 nit | AMOLED-Variante geplant | 1.600 EUR |
| GPSMAP 9x3 9" | 9" IPS | 1280×720 | 1.800 nit | — | 2.400 EUR |
| GPSMAP 9x3 12" | 12" IPS | 1280×800 | 1.800 nit | — | 3.600 EUR |
| GPSMAP 9x3 16" | 16" IPS | 1920×1080 | 1.800 nit | — | 6.000 EUR |
| GPSMAP 9019 | 19" IPS | 1920×1200 | 1.800 nit | Helm-Station | 9.000 EUR |

**Besonderheiten Garmin:**
- Höchste Display-Helligkeit im Markt (1.800 nit) — exzellent bei Sonnenlicht
- Integrierter GPS/GLONASS/Galileo-Empfänger in allen MFDs
- Garmin Marine Network (proprietäres Ethernet) für Radar, Sonar, Kameras
- ActiveCaptain App: Community-Daten (Hafen-Reviews, Ankerplätze, Updates)
- Garmin Fantom Radar: FMCW Solid-State mit MotionScope (Doppler-Erkennung)
- Panoptix LiveScope: Echtzeit-Sonar für Fischfinder und Forward-Looking
- GPSMAP 9000 mit SmartMode: Kontextbasierte Seitenvorlagen (Einfahrt, Offshore, Fischen, Segeln)
- OneHelm: Integration von Drittanbieter-Systemen (Mercury, Yamaha, Fusion, EmpirBus)

**Ökosystem:**
- Windgeber: gWind / gWind Wireless
- Autopilot: Reactor 40 / GHP 10/20/30 Hydraulik
- AIS: AIS 800 (Class B+ Transponder), GNT 10 (NMEA 2000 Gateway)
- Funk: VHF 115i / 215i / 315i (integrierter AIS-Empfänger in 215i/315i)
- Sonar: GT-Serie Geber (CHIRP, ClearVü, SideVü)
- App: ActiveCaptain für iOS/Android + Garmin Express für Desktop-Updates
- Kartenmaterial: Navionics (seit 2017 Garmin-Tochter), BlueChart g3/g3 Vision

### 4.3 Simrad NSX

**Hersteller:** Simrad Yachting (Navico / Brunswick Corporation, Norwegen)
**Produktfamilie:** NSX, NSS evo3S, GO XSE (Einstieg)
**Betriebssystem:** Simrad OS (basierend auf Navico-Plattform)

**NSX Serie (2023):**

| Modell | Display | Auflösung | Helligkeit | Besonderheit | Preis (ca.) |
|--------|---------|-----------|-----------|-------------|-------------|
| NSX 3007 | 7" IPS | 1024×600 | 1.500 nit | Ultraschnell, neues OS | 1.200 EUR |
| NSX 3009 | 9" IPS | 1280×720 | 1.500 nit | — | 1.800 EUR |
| NSX 3012 | 12" IPS | 1280×800 | 1.500 nit | — | 2.800 EUR |
| NSX 3016 | 16" IPS | 1920×1080 | 1.500 nit | — | 4.800 EUR |

**Besonderheiten Simrad:**
- Navico-Plattform (gemeinsam mit B&G und Lowrance) — größter Marine-Elektronik-Verbund
- Halo Radar Serie: FMCW + Puls-Hybrid, VelocityTrack (Doppler)
- ActiveTarget / ForwardScan: Echtzeit-Sonar mit Forward-Looking-Funktionalität
- SimNet / NMEA 2000 dual-kompatibel
- Deep Integration mit Continuum Autopilot (ehem. Robertson)
- Mercury VesselView Integration (direkte Motorsteuerung am MFD)
- SailSteer: Regatta-spezifische Anzeige (Laylines, Startlinie, Polarkurven)
- C-MAP Kartenmaterial (Navico-Tochter): Genesis (Community-Karten), Discover, Reveal

**Ökosystem:**
- Windgeber: Simrad IS42 + DST810/WS320 Wireless
- Autopilot: Simrad AP44/AC42/AC70 Autopilot-Computer
- AIS: Simrad AI50 (Class B Transponder)
- Funk: Simrad RS100 / RS100-B (mit integriertem AIS Class B)
- Sonar: Simrad TotalScan, StructureScan 3D, ActiveTarget
- App: Simrad App für iOS/Android

### 4.4 B&G Zeus / Vulcan

**Hersteller:** B&G (Navico / Brunswick Corporation, Großbritannien)
**Produktfamilie:** Zeus S, Zeus3 S, Vulcan (Einstieg)
**Betriebssystem:** B&G OS (Navico-Plattform, segeloptimiert)

**Zeus S Serie (2023):**

| Modell | Display | Auflösung | Helligkeit | Besonderheit | Preis (ca.) |
|--------|---------|-----------|-----------|-------------|-------------|
| Zeus S 7 | 7" IPS | 1024×600 | 1.500 nit | SailSteer, Laylines | 1.400 EUR |
| Zeus S 9 | 9" IPS | 1280×720 | 1.500 nit | — | 2.100 EUR |
| Zeus S 12 | 12" IPS | 1280×800 | 1.500 nit | — | 3.200 EUR |
| Zeus S 16 | 16" IPS | 1920×1080 | 1.500 nit | — | 5.200 EUR |

**Besonderheiten B&G (Regattafokus):**
- **SailSteer:** Exklusive Segelfunktion — zeigt Laylines, Polarkurven, optimalen VMG-Kurs, Wende-/Halsen-Empfehlungen in einer Ansicht
- **Stripchart:** Echtzeit-Performance-Daten als Zeitverlauf (Wind, Heel, VMG, Target-Speed)
- **Sailing-spezifische Autopilot-Algorithmen:** Wind-Modus mit Autohalse/Autowende
- **H5000-Integration:** Für Regattayachten — Prozessor-Modul mit 20 Hz Update-Rate für Wind/Performance
- **WTP-Daten:** Target-Speed, Polarkurven, VMG, Optimal-Wind-Angle basierend auf hinterlegten Polardiagrammen
- Gleiche Hardware-Basis wie Simrad NSX, aber mit Segel-optimierter Software

**Ökosystem:**
- Windgeber: B&G WS320 (Wireless, Masttopp), WS310 (kabelgebunden)
- Autopilot: B&G H5000 / Pilot Controller / NAC-3 Computer
- AIS: B&G V60-B / V100-B (VHF + AIS Class B Transponder)
- Funk: B&G V60 / V100 (DSC + optionaler AIS Class B)
- Instrumente: B&G Triton2 / Nemesis Displays
- App: B&G App für iOS/Android
- Kartenmaterial: C-MAP (wie Simrad)

### 4.5 Furuno NavNet TZtouch3

**Hersteller:** Furuno Electric Co., Ltd. (Japan)
**Produktfamilie:** NavNet TZtouch3, GP-39 (Stand-alone GPS)
**Betriebssystem:** TZtouch3 OS (proprietär)

**TZtouch3 Serie:**

| Modell | Display | Auflösung | Helligkeit | Besonderheit | Preis (ca.) |
|--------|---------|-----------|-----------|-------------|-------------|
| TZT9F | 9" IPS | 1280×720 | 1.000 nit | Multi-Touch | 2.500 EUR |
| TZT12F | 12,1" IPS | 1280×800 | 1.000 nit | Knopf- + Touch-Bedienung | 3.800 EUR |
| TZT16F | 15,6" IPS | 1920×1080 | 1.000 nit | — | 6.800 EUR |
| TZT19F | 19" IPS | 1920×1200 | 1.000 nit | Bridgestation | 9.500 EUR |

**Besonderheiten Furuno:**
- Höchste Radar-Reputation im Markt (aus der Berufsschifffahrt)
- DRS-Radar-Serie: Magnetron (DRS4D, DRS6A, DRS12A, DRS25A) und Solid-State (DRS4D-NXT)
- NXT-Radar: Doppler-Erkennung mit Target Analyzer und Fast Target Tracking
- ARPA bis 100 Ziele (weit mehr als MARPA anderer Hersteller)
- Dual-Range-Radar: Gleichzeitig Nah- und Fernbereich
- SC-50/SC-70 Satellite Compass: Premium-GPS-Kompass mit 0,4–0,5° Genauigkeit (SC-50: 0,5° RMS, SC-70: 0,4° RMS)
- TimeZero-Kartensoftware: Gleiche Kartendarstellung wie Profi-Schifffahrt
- Premium-Verarbeitung und höhere Betriebstemperaturbereiche
- Typischer Einsatz: Semi-Custom und Custom Yachten 14m+, Offshore-Fischereifahrzeuge

**Ökosystem:**
- Windgeber: Furuno FI-5002 (analog) mit Converter FI-5002C (NMEA 2000)
- Autopilot: Furuno NAVpilot 711C (300 Serie) — premium Autopilot
- AIS: Furuno FA-70 (Class B+ Transponder), FA-170 (Class A)
- Funk: Furuno FM-4800 (DSC + AIS-Empfänger integriert)
- Sonar: Furuno DFF3D (3D Multi-Beam), DFF1-UHD (CHIRP)
- Karten: TimeZero / C-MAP / Navionics
- Ethernet-Vernetzung: Furuno HUB-101 (Network Expander)

### 4.6 Weitere Hersteller

#### 4.6.1 Humminbird (APEX / SOLIX)

- Zugehörigkeit: Johnson Outdoors (USA)
- Kernmarkt: Sportfischerei, Süßwasser und Küste
- Stärke: MEGA Live Imaging, MEGA 360 (Echtzeit-Sonar rundum)
- APEX-Serie: 13–19" MFDs mit MEGA-Sonar-Integration
- Für Yachtnavigation: Begrenzt (kein Radar, eingeschränktes Routingmodul)
- Preisbereich: 800–5.000 EUR

#### 4.6.2 Vesper Marine (Cortex)

- Zugehörigkeit: Unabhängig (Neuseeland)
- Cortex M1: UKW-Funk + AIS Class B+ Transponder + Monitoring + Alarm in einem Hub
- Cortex H1: Handset mit Farbdisplay
- Besonderheit: Alarmanlage, Ankerwatch, Bilgenpumpe-Monitoring, Remote-Zugriff via Vesper-App
- Preis: 1.500–2.000 EUR (Hub + Handset)

#### 4.6.3 Icom (UKW-Funk)

- Zugehörigkeit: Icom Inc. (Japan)
- Weltmarktführer für Marine-UKW-Funkgeräte
- Modelle: IC-M510 (Premium Festeinbau, DSC, GPS), IC-M423 (Standard), IC-M94DE (Handfunkgerät mit DSC + AIS-RX)
- IC-M605EURO: Flaggschiff — OLED-Display, Dual-Watch, GPS, AIS-Empfänger
- IC-M803: GW/KW-Seefunkgerät für Langfahrt
- Preisbereich: 100–1.200 EUR (VHF), 1.500–3.000 EUR (SSB)

#### 4.6.4 Standard Horizon (UKW-Funk)

- Zugehörigkeit: Yaesu / Vertex Standard (Japan)
- GX6500: Premium-Festeinbau, integrierter GPS + AIS-RX, 25W, Matrix-Display
- GX2400: AIS-Empfänger integriert, DSC, GPS
- GX1400: Einstiegsmodell, kompakt
- HX890E: Premium-Handfunkgerät mit GPS + DSC
- Preisbereich: 100–500 EUR (VHF), 150–400 EUR (Handfunk)

---

## 5. Hersteller-Datenbank

### 5.1 Raymarine (Teledyne FLIR)

| Feld | Wert |
|------|------|
| **Vollständiger Name** | Raymarine UK Ltd (Teledyne FLIR) |
| **Gründung** | 1923 (als Kelvin Hughes), Marke Raymarine seit 2001 |
| **Hauptsitz** | Fareham, Hampshire, Großbritannien |
| **Mutterkonzern** | Teledyne Technologies (seit 2010 FLIR, seit 2021 Teledyne) |
| **Marktposition** | Nr. 2 global im Yacht-MFD-Segment |
| **Umsatz Marine-Elektronik** | ~250–300 Mio. USD (geschätzt, 2024) |
| **Produktbereiche** | MFD, Radar, Autopilot, Instrumente, Kameras, Thermografie |
| **Stärken** | LightHouse OS, ClearCruise AR, breites Ökosystem, guter Service-Netzwerk |
| **Schwächen** | SeaTalkNG-Stecker proprietär, Display-Helligkeit unter Garmin |
| **AYDI-Relevanz** | Häufig auf europäischen Segelyachten 10–18m, OEM bei Bavaria, Jeanneau (teils) |
| **Kompatibilität** | SeaTalkNG (= NMEA 2000 mit Adapter), NMEA 0183, RayNet Ethernet, WiFi |
| **Support Deutschland** | Raymarine Deutschland (Hamburg), Busse Yachtshop, SVB, Compass24 |
| **Garantie** | 2 Jahre (Standard), 3 Jahre (nach Registrierung) |

### 5.2 Garmin Ltd.

| Feld | Wert |
|------|------|
| **Vollständiger Name** | Garmin Ltd. |
| **Gründung** | 1989 (als ProNav) |
| **Hauptsitz** | Schaffhausen (Schweiz), Betrieb in Olathe, Kansas (USA) |
| **Mutterkonzern** | Eigenständig (börsennotiert, NASDAQ: GRMN) |
| **Marktposition** | Nr. 1 global im Yacht-MFD-Segment |
| **Umsatz Marine-Segment** | ~800–900 Mio. USD (2024, inkl. Navionics) |
| **Produktbereiche** | MFD, Radar, Autopilot, Sonar, Instrumente, Funk, Karten |
| **Stärken** | Höchste Displayhelligkeit, Navionics-Karten, ActiveCaptain Community, breites Sortiment |
| **Schwächen** | Proprietäres Garmin Marine Network, Sonar/Fischfinder-lastig, weniger Regatta-Features |
| **AYDI-Relevanz** | Dominiert bei Motorbooten 8–16m, zunehmend auch Segelyachten |
| **Kompatibilität** | NMEA 2000, NMEA 0183, Garmin Marine Network (proprietäres Ethernet), WiFi, ANT |
| **Support Deutschland** | Garmin Deutschland GmbH (Garching), umfangreiches Händlernetz |
| **Garantie** | 2 Jahre |

### 5.3 Navico (Simrad / B&G / Lowrance)

| Feld | Wert |
|------|------|
| **Vollständiger Name** | Navico Group (Brunswick Corporation) |
| **Gründung** | 2007 (als Navico, Zusammenschluss von Simrad, Lowrance, B&G) |
| **Hauptsitz** | Egersund (Simrad) / Tulsa, OK (Lowrance) / Romsey, UK (B&G) |
| **Mutterkonzern** | Brunswick Corporation (seit 2021, ~1,05 Mrd. USD Übernahme) |
| **Marktposition** | Nr. 1 nach Produktbreite (3 Marken), Nr. 2–3 nach MFD-Marktanteil |
| **Umsatz** | ~1,0–1,2 Mrd. USD (alle Marken, 2024) |
| **Marken** | Simrad (Motorboote/Yachten), B&G (Segelyachten), Lowrance (Fischerei) |
| **Stärken** | Gemeinsame Plattform (Kostensynergien), C-MAP-Karten, Halo-Radar, SailSteer (B&G) |
| **Schwächen** | SimNet-Stecker proprietär, drei Marken = Verwirrung, Software-Updates manchmal langsam |
| **AYDI-Relevanz** | B&G dominiert bei Regattayachten, Simrad stark bei skandinavischen Werften (Hallberg-Rassy, Najad) |
| **Kompatibilität** | SimNet (= NMEA 2000 mit Adapter), NMEA 0183, Ethernet, WiFi, Bluetooth |
| **Support Deutschland** | Navico Deutschland (Rellingen), Fachhandel (SVB, Busse, Toplicht) |
| **Garantie** | 2 Jahre |

### 5.4 Furuno Electric Co., Ltd.

| Feld | Wert |
|------|------|
| **Vollständiger Name** | Furuno Electric Co., Ltd. |
| **Gründung** | 1948 |
| **Hauptsitz** | Nishinomiya, Hyogo, Japan |
| **Mutterkonzern** | Eigenständig (TSE: 6814) |
| **Marktposition** | Nr. 1 bei Berufsschifffahrt-Radar, Nr. 4–5 bei Yacht-MFD |
| **Umsatz** | ~800–900 Mio. USD gesamt (2024), davon ~15% Freizeit/Yacht |
| **Produktbereiche** | MFD, Radar (Premium), Sonar/Echolot (Premium), Autopilot, AIS, Funk, Satelliten-Kompass |
| **Stärken** | Beste Radar-Qualität, Berufsschifffahrt-Erfahrung, SC-50/70 GPS-Kompass, Robustheit |
| **Schwächen** | Höchster Preis, konservatives UI-Design, geringere Displayhelligkeit, weniger App-Ökosystem |
| **AYDI-Relevanz** | Standard bei Custom-Yachten 18m+, Offshore-Fischer, Behördenfahrzeuge |
| **Kompatibilität** | NMEA 2000, NMEA 0183, Ethernet, WiFi |
| **Support Deutschland** | Furuno Deutschland GmbH (Rellingen), spezialisierte Fachhändler |
| **Garantie** | 2 Jahre (3 Jahre mit Registrierung bei einigen Produkten) |

### 5.5 Icom Inc.

| Feld | Wert |
|------|------|
| **Vollständiger Name** | Icom Incorporated |
| **Gründung** | 1954 |
| **Hauptsitz** | Osaka, Japan |
| **Mutterkonzern** | Eigenständig |
| **Marktposition** | Nr. 1 bei Marine-UKW-Funkgeräten weltweit |
| **Produktbereiche** | UKW-Seefunkgeräte, GW/KW-Seefunk, Handfunkgeräte, Satellitenkommunikation |
| **Stärken** | Beste Empfängerqualität, DSC-Zuverlässigkeit, robuste Bauweise, breites Sortiment |
| **Schwächen** | Kein MFD, kein Radar, kein Autopilot — reiner Funk-Spezialist |
| **AYDI-Relevanz** | Referenz für Funkausrüstung, häufig OEM-Empfehlung bei Neubauten |
| **Support Deutschland** | Icom Europe GmbH (Bad Soden), umfangreiches Servicenetz |
| **Garantie** | 2 Jahre |

### 5.6 Vesper Marine

| Feld | Wert |
|------|------|
| **Vollständiger Name** | Vesper Marine Ltd. |
| **Gründung** | 2007 |
| **Hauptsitz** | Auckland, Neuseeland |
| **Mutterkonzern** | Eigenständig |
| **Marktposition** | Innovationsführer im AIS/VHF-Kombisegment |
| **Produktbereiche** | AIS-Transponder, UKW-Funk, Monitoring/Alarm, Cortex-System |
| **Stärken** | Cortex-System (VHF + AIS + Monitoring in einem), hervorragende App, Fernüberwachung |
| **Schwächen** | Kleines Produktsortiment, Bekanntheit in Europa ausbaufähig |
| **AYDI-Relevanz** | Innovative Alternative für AIS/VHF-Kombination, Remote-Monitoring für Charteryachten |
| **Support Deutschland** | Über Fachhandel (SVB, Compass24) |
| **Garantie** | 2 Jahre |

---

## 6. Fehlerbild-Atlas

### 6.1 FB-NAV-001: GPS-Positionsverlust (Totalausfall)

**Schweregrad:** CRITICAL
**Betroffene Systeme:** GPS-Empfänger, MFD, Autopilot, AIS, DSC-Funk
**Häufigkeit:** Selten (1–3% aller Yacht-Servicefälle)

**Symptome:**
- MFD zeigt "Kein GPS-Signal" oder Position springt auf 0°/0°
- Autopilot wechselt in Standby
- AIS sendet keine Position mehr
- DSC-Notruf ohne Positionsdaten

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnoseweg |
|---------|-------------------|-------------|
| GPS-Antennenkabel defekt (Bruch, Korrosion) | 35% | Kabelwiderstand messen, visuell prüfen |
| GPS-Antennenanschluss korrodiert | 25% | Stecker inspizieren, Übergangswiderstände |
| GPS-Empfänger defekt | 15% | Austausch-Test mit bekanntem Empfänger |
| Elektromagnetische Störung (EMI) | 10% | Andere Geräte ausschalten, Position draußen testen |
| Mastfuß-Masseproblem | 5% | Masseverbindung prüfen |
| Satelliten-Abschattung (vorübergehend) | 5% | GNSS-Status prüfen (Satellitenzahl/DOP) |
| NMEA-2000-Netzwerkfehler | 5% | Bus-Spannung messen, Terminierung prüfen |

**Sofortmaßnahmen:**
1. NMEA-2000-Diagnosetool (z.B. Actisense NGT-1) anschließen → Wird PGN 129029 gesendet?
2. GPS-Antennenstecker am Empfänger lösen und reinigen (Kontaktreiniger, WD-40 Contact Cleaner)
3. Externes GPS mit bekannter Funktion anschließen (z.B. Garmin GPS 19x NMEA 2000 → direkt am Backbone)
4. Bei EMI-Verdacht: VHF-Funk, Ladegerät, Inverter nacheinander ausschalten

**AYDI-Bewertung:**
- Confidence: `measured` (Kabeltest) oder `visual_medium` (Korrosionsinspektion)
- Kostenrahmen Reparatur: 50–500 EUR (Kabel/Stecker), 300–1.500 EUR (Empfänger-Ersatz)
- Empfehlung: Redundantes GPS (Handheld oder zweiter NMEA-2000-Empfänger)

### 6.2 FB-NAV-002: GPS-Positionsabweichung (>50m)

**Schweregrad:** HIGH
**Betroffene Systeme:** Alle positionsabhängigen Systeme

**Symptome:**
- Position auf Seekarte weicht sichtbar von tatsächlicher Position ab
- Boot erscheint an Land oder im falschen Hafen
- AIS-Ziele und eigenes Boot passen nicht zusammen

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnoseweg |
|---------|-------------------|-------------|
| Multipath-Reflexionen (Hafen, Brücken) | 30% | Freifahrt auf offenes Wasser, Vergleich |
| Kartendatum falsch (WGS84 vs. anderes) | 20% | Einstellungen MFD prüfen |
| GPS-Antenne teilweise abgeschattet | 15% | Satellitenstatus prüfen (Azimut-Plot) |
| Alter Kartenstand | 15% | Kartendatum prüfen (Vermessungsjahr) |
| Ionosphärische Störung (Sonnensturm) | 10% | Space Weather prüfen, SBAS-Status |
| GPS-Empfänger Firmware veraltet | 5% | Firmware-Version prüfen, Update |
| GPS-Spoofing/Jamming | 5% | Ungewöhnliche Anzahl Satelliten, Position springt |

**AYDI-Bewertung:**
- Confidence: `estimated` (ohne Referenzmessung), `measured` (mit Vergleichsempfänger)
- Typische Korrektur: Kartendatum WGS84 setzen, Firmware-Update, Antennenposition optimieren

### 6.3 FB-NAV-003: NMEA-2000-Netzwerkfehler (Bus-Ausfall)

**Schweregrad:** CRITICAL
**Betroffene Systeme:** Alle NMEA-2000-Geräte

**Symptome:**
- Einzelne oder alle Geräte am NMEA-2000-Bus fallen aus
- MFD zeigt "Keine Daten" für Wind, Tiefe, GPS etc.
- Autopilot verliert Heading-Information
- Intermittierende Datenverluste

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnoseweg |
|---------|-------------------|-------------|
| Fehlende/defekte Terminierung | 25% | Widerstand zwischen CAN-H und CAN-L messen (soll 60Ω sein: 2×120Ω parallel) |
| Wassereinbruch in T-Stück/Stecker | 20% | Visuelle Inspektion aller Stecker und T-Stücke |
| Kabelbruch im Backbone | 15% | Durchgangsprüfung segmentweise |
| Überlastung Spannungsversorgung (>30 LEN) | 10% | LEN aller Geräte summieren, Spannung am Bus messen |
| Kurzschluss in einem Gerät | 10% | Geräte einzeln vom Bus trennen |
| Zu lange Drop-Lines (>6m) | 5% | Kabellängen messen |
| Backbone zu lang (>100m Micro-C) | 5% | Gesamtlänge messen |
| CAN-Bus-Adresskonflikt | 5% | Diagnosetool: doppelte Adressen? |
| Schirmungsproblem / EMI | 5% | Schirmung prüfen, Motor an/aus testen |

**Diagnoseverfahren mit Actisense NGT-1:**
1. NGT-1 an Backbone anschließen
2. NMEA Reader Software starten
3. Prüfen: Werden PGNs empfangen? Welche Geräte melden sich?
4. Bus-Spannung messen (soll 9–16V, typisch 12,6V)
5. Bus-Widerstand messen (beide Terminierungen drin → 60Ω)
6. Fehlerrate prüfen (CAN Error Frames → deutet auf Hardware-Problem)

**AYDI-Bewertung:**
- Confidence: `measured` (mit Diagnosetool)
- Kostenrahmen: 20–100 EUR (Stecker/T-Stück), 50–300 EUR (Kabel), 200–500 EUR (Arbeitszeit Fehlersuche)

### 6.4 FB-NAV-004: Radarausfall / Kein Radarbild

**Schweregrad:** HIGH
**Betroffene Systeme:** Radar, MFD (Radar-Overlay), MARPA

**Symptome:**
- Radar-Seite am MFD zeigt "Kein Radar" oder schwarzes Bild
- Radar-Scanner dreht nicht
- Radarbild extrem schwach (fast leer)

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnoseweg |
|---------|-------------------|-------------|
| Ethernet-/Signalkabel Radar-MFD unterbrochen | 25% | Kabelverbindungen prüfen, LEDs am Scanner |
| Radar-Scanner-Motor defekt | 15% | Dreht der Scanner? Geräusche? |
| Magnetron verbraucht (bei Pulse-Radar) | 15% | Sendeleistung messen (Service), Alter prüfen |
| Spannungsversorgung Scanner unzureichend | 15% | 12V am Scanner messen (unter Last) |
| Feuchtigkeit im Scanner-Gehäuse (Radom) | 10% | Radom öffnen, visuell prüfen |
| MFD-Software / Kompatibilität | 10% | Firmware-Versionen MFD und Scanner vergleichen |
| Wellenleiter-Defekt (bei Magnetron) | 5% | Service erforderlich |
| Drehgelenk (Slip Ring) verschlissen | 5% | Knackgeräusche, intermittierender Ausfall in bestimmten Winkeln |

**AYDI-Bewertung:**
- Confidence: `visual_medium` (optische Inspektion Scanner), `measured` (elektrische Messung)
- Kostenrahmen: 100–300 EUR (Kabel), 500–2.000 EUR (Magnetron-Ersatz), 2.000–5.000 EUR (Scanner-Ersatz)

### 6.5 FB-NAV-005: AIS — Eigene Position nicht sichtbar für andere

**Schweregrad:** HIGH
**Betroffene Systeme:** AIS-Transponder, Sicherheit

**Symptome:**
- Andere Schiffe / Hafenmeister können die Yacht nicht auf AIS sehen
- Marine Traffic / Vessel Finder zeigt das Schiff nicht
- AIS-Transponder zeigt "TX Error" oder "No GPS"

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnoseweg |
|---------|-------------------|-------------|
| Fehlende GPS-Position am Transponder | 25% | GPS-Status am AIS-Gerät prüfen |
| UKW-Antenne defekt oder nicht angeschlossen | 20% | SWR messen (<3:1 erforderlich), Antennenanschluss prüfen |
| MMSI nicht programmiert | 15% | Geräteeinstellungen prüfen |
| AIS-Transponder im Silent-Modus | 10% | Einstellungen prüfen (Sportboote: manchmal versehentlich deaktiviert) |
| Antennensplitter defekt | 10% | VHF separat über eigene Antenne testen |
| Transponder-Defekt (TX-Modul) | 10% | Diagnosemodus, LED-Status |
| TDMA-Slot-Probleme (überfüllter Kanal) | 5% | Nur in extremen Verkehrslagen (Einfahrt Rotterdam/Hamburg) |
| Sendeleistung zu gering (Class B = nur 2W) | 5% | Reichweite physikalisch begrenzt (~10nm bei 2W) |

**AYDI-Bewertung:**
- Confidence: `measured` (SWR-Messung, Diagnosemodus)
- Sofortmaßnahme: MMSI prüfen, GPS-Anbindung prüfen, Antennensplitter bypassen

### 6.6 FB-NAV-006: Autopilot — Kursabweichung / Gieren

**Schweregrad:** MEDIUM–HIGH
**Betroffene Systeme:** Autopilot, Ruderanlage

**Symptome:**
- Boot giert ständig um den Sollkurs (>10° Abweichung)
- Ruderbewegungen zu häufig und zu groß
- Autopilot "jagt" (oversteering)
- Kurs läuft langsam ab (konstante Abweichung einer Seite)

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnoseweg |
|---------|-------------------|-------------|
| Kompass nicht kalibriert (Deviation) | 25% | Deviation Table prüfen, Neukalibrierung |
| Autopilot-Parameter falsch eingestellt | 20% | Gain/Counter/Auto-Trim prüfen |
| Ruderrückmeldung (Feedback) defekt/dejustiert | 15% | Ruderwinkelanzeige vs. tatsächliche Ruderlage |
| Heading-Sensor-Montage falsch (nicht mittig, nicht in Flucht) | 10% | Einbaulage prüfen |
| Ruderanlage hat Spiel (mechanisch) | 10% | Ruderlager, Stevenrohr, Quadrant prüfen |
| Magnetische Störung am Kompass | 10% | Lautsprecher, Elektromotoren, Magnete in Nähe? |
| Antrieb zu schwach für Seezustand | 5% | Dimensionierung prüfen (Ruderdrehmoment) |
| Seegang/Wind jenseits der Systemkapazität | 5% | Verdrängung vs. Antriebsleistung |

**AYDI-Bewertung:**
- Confidence: `measured` (Kalibrierung, elektrische Tests)
- Empfehlung: Deviation-Tabelle regelmäßig prüfen (alle 2 Jahre oder nach Umbauten)

### 6.7 FB-NAV-007: MFD-Touchscreen reagiert nicht

**Schweregrad:** MEDIUM
**Betroffene Systeme:** MFD, alle darüber gesteuerten Systeme

**Symptome:**
- Touchscreen reagiert nicht auf Berührung
- Touchscreen reagiert nur in Teilbereichen
- Geisterberührungen (Phantom Touches)
- Display funktioniert, aber keine Touch-Eingabe

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnoseweg |
|---------|-------------------|-------------|
| Wassertropfen auf kapazitivem Screen | 25% | Display trocknen, Blende reinigen |
| Display-Schutzfolie beschädigt/abgelöst | 15% | Folie entfernen oder erneuern |
| Korrosion am Display-Rand (Salzwasser) | 15% | Visuell prüfen, reinigen |
| Software-Absturz (OS-Freeze) | 15% | Neustart (Hard Reset) |
| Display-Kabel intern lose | 10% | Service (Gerät öffnen) |
| UV-Schaden am Touch-Panel | 10% | Display-Abdeckung prüfen, UV-Exposition minimieren |
| Hardware-Defekt Touch-Controller | 10% | Nur durch Austausch diagnostizierbar |

**AYDI-Bewertung:**
- Confidence: `visual_medium` (optische Inspektion)
- Sofortmaßnahme: Hard Reset (Stromlos 30s), Display reinigen, Tasten-/Knopfbedienung (falls verfügbar)

### 6.8 FB-NAV-008: UKW-Funk — Geringe Reichweite

**Schweregrad:** MEDIUM–HIGH
**Betroffene Systeme:** UKW-Funk, DSC-Notruf, AIS (bei Antennensplitter)

**Symptome:**
- Reichweite deutlich unter Erwartung (<10 nm statt 20+ nm)
- Andere Schiffe hören die Yacht nicht
- Empfang gut, aber Senden schwach
- DSC-Rufe werden nicht bestätigt

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnoseweg |
|---------|-------------------|-------------|
| Antennenkabel-Verluste (alte/dünne Koaxleitung) | 25% | Kabeltyp prüfen (RG-58 → ersetzen durch RG-213/LMR-400) |
| Antennenstecker korrodiert | 20% | PL-259-Stecker inspizieren, Korrosion? |
| Antenne selbst defekt (Stabbruch, Wasser eingedrungen) | 15% | SWR messen (soll <1.5:1, akzeptabel <3:1) |
| Sendeleistung auf 1W statt 25W | 10% | Leistungseinstellung am Funkgerät prüfen |
| Antennensplitter defekt oder schlecht | 10% | VHF direkt an Antenne (ohne Splitter) testen |
| Koax-Stecker-Typ PL-259 vs. BNC vs. N falsch | 5% | Korrekte Adapter verwenden |
| Masttopp-Antennenkabel bei Rigganpassung geknickt | 10% | Kabelweg im Mast inspizieren |
| Funkgerät-Defekt (PA-Stufe) | 5% | Nur durch Servicemessung |

**SWR-Messung (Standing Wave Ratio):**
- Messgerät: SWR-Meter (z.B. Shakespeare ART-3) oder Antennenmessgerät (z.B. RigExpert AA-55)
- Messung auf Kanal 16 (156,800 MHz)
- SWR <1.5:1 = Exzellent, <2.0:1 = Gut, <3.0:1 = Akzeptabel, >3.0:1 = Problem
- SWR >5:1 = NICHT senden (Schaden am Funkgerät möglich!)

**AYDI-Bewertung:**
- Confidence: `measured` (SWR-Messung)
- Kostenrahmen: 20–50 EUR (Stecker), 50–200 EUR (Kabel), 100–400 EUR (Antenne)

### 6.9 FB-NAV-009: Echolot — Tiefenangabe falsch oder fehlend

**Schweregrad:** HIGH (Navigationsrelevant)
**Betroffene Systeme:** Echolot, Ankerfunktion, Autopilot (Flachwasseralarm)

**Symptome:**
- Tiefenangabe springt wild oder fällt auf "---"
- Tiefenangabe weicht stark von Kartentiefe ab
- Echolot verliert bei Fahrt das Signal (speed-abhängig)

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnoseweg |
|---------|-------------------|-------------|
| Bewuchs auf Geber (Muscheln, Algen) | 25% | Geber reinigen (aus dem Wasser oder Taucher) |
| Luftblasen am Geber (bei Fahrt) | 20% | Nur bei Fahrt? → Montagefehler, Transom-Mount zu hoch |
| Offset falsch eingestellt (Geber↔Wasserlinie) | 15% | Einstellung im MFD prüfen |
| In-Hull-Geber: Epoxidkopplung degradiert | 10% | Geber lösen, neu einkleben |
| Geber-Kabel beschädigt | 10% | Widerstand/Kapazität messen |
| Frequenz falsch für Tiefe | 5% | 200kHz für Flachwasser, 50kHz für Tiefwasser |
| Wassertemperatur-Schichtung (Sprungschicht) | 5% | Saisonabhängig, natürliches Phänomen |
| Geber-Defekt | 10% | Austausch-Test |

**AYDI-Bewertung:**
- Confidence: `measured` (Vergleich mit Kartentiefe und Lot)
- Wartungshinweis: Geber bei jedem Antifouling-Anstrich reinigen, NICHT mit Antifouling überstreichen (Ausnahme: spezielle Geber-Antifoulingfarbe)

### 6.10 FB-NAV-010: Windmesser — Fehlerhafte Windwerte

**Schweregrad:** MEDIUM (HIGH bei Regattaeinsatz)
**Betroffene Systeme:** Windgeber, Segeltrimm-Daten, Autopilot (Wind-Modus)

**Symptome:**
- Windrichtung stimmt nicht (z.B. zeigt Backbord an obwohl Wind von Steuerbord)
- Windgeschwindigkeit unplausibel (viel zu hoch oder zu niedrig)
- Windwerte springen oder fallen auf Null

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnoseweg |
|---------|-------------------|-------------|
| Windfahne/Schälchen blockiert (Vogelkot, Salzkristalle, Spinnengewebe) | 25% | Visuell prüfen (Fernglas zum Masttopp) |
| Masttopp-Offset nicht kalibriert | 20% | Auf Vorwindkurs: zeigt Geber 0° (±5°)? |
| Kabelfehler im Mast | 15% | Leitungsdurchgang messen |
| Ultraschall-Geber (Ultrasonic): Verschmutzung | 10% | Sensorflächen reinigen |
| Kabelgebundener Geber: Stecker am Mastfuß korrodiert | 10% | Stecker inspizieren |
| Wireless-Geber: Batterie leer oder Funkstörung | 10% | Batterie prüfen (B&G WS320: Solarzelle + Batterie) |
| Kalibrierfehler nach Riggarbeiten | 5% | Neukalibrierung durchführen |
| Geber-Defekt (Lager verschlissen, Encoder defekt) | 5% | Geber drehen — ruckelt? Schwergängig? |

**AYDI-Bewertung:**
- Confidence: `measured` (Vergleich mit Handwindmesser), `visual_medium` (optische Inspektion)
- Wartungshinweis: Mindestens 1× pro Saison Geber inspizieren, Lager prüfen, reinigen

### 6.11 FB-NAV-011: MFD — Software-Absturz / Boot-Schleife

**Schweregrad:** MEDIUM–HIGH
**Betroffene Systeme:** MFD und alle darüber gesteuerten Funktionen

**Symptome:**
- MFD startet nicht (bleibt beim Logo hängen)
- MFD startet immer wieder neu (Boot Loop)
- MFD friert ein (Freeze), reagiert auf keine Eingabe
- Schwarzer Bildschirm trotz Spannungsversorgung

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnoseweg |
|---------|-------------------|-------------|
| Firmware-Update fehlgeschlagen | 20% | War kürzlich ein Update? Recovery-Mode versuchen |
| SD-Karte defekt/korrupt | 15% | SD-Karte entfernen, ohne Karte starten |
| Speicher voll (Track-Log, Screenshots) | 10% | Daten löschen im Servicemodus |
| Spannungsversorgung instabil | 15% | 12V unter Last messen (Anlasser!) |
| Überhitzung (Display in praller Sonne) | 10% | Gerät abkühlen lassen |
| Hardware-Defekt (Mainboard, RAM) | 15% | Nur durch Hersteller-Service |
| NMEA-2000-Bus-Fehler belastet MFD | 10% | NMEA-2000-Bus trennen, MFD allein starten |
| Korrosion an Steckern (Rückseite MFD) | 5% | Stecker inspizieren, reinigen |

**Recovery-Prozeduren (herstellerspezifisch):**

| Hersteller | Recovery-Methode |
|-----------|-----------------|
| Raymarine | Firmware auf SD-Karte, beim Start Power+Button halten |
| Garmin | garmin-Ordner auf SD-Karte mit .gupdate-Datei |
| Simrad/B&G | Software auf microSD, Recovery-Modus über Tastenkombination |
| Furuno | Service-Modus über verstecktes Menü oder USB-Stick |

**AYDI-Bewertung:**
- Confidence: `estimated` (ohne Diagnosetool), `measured` (mit Hersteller-Servicetools)
- Empfehlung: Firmware-Updates nur bei stabiler Spannungsversorgung (Landstrom!), Backup der Routen/Wegpunkte vor Update

### 6.12 FB-NAV-012: Galvanische Korrosion an Elektronik-Durchbrüchen

**Schweregrad:** HIGH (Substanzschaden)
**Betroffene Systeme:** Echolot-Durchbrüche, Log-Geber, Erdungsplatten

**Symptome:**
- Grüne/weiße Korrosionsablagerungen an Bronze-Durchbrüchen
- Durchbruch wird undicht
- Umgebendes GFK zeigt Verfärbung/Delamination
- Tiefenmesswerte werden unzuverlässig

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnoseweg |
|---------|-------------------|-------------|
| Ungleiche Metalle ohne Isolation (Bronze-Geber + Edelstahl-Mutter) | 30% | Materialpaarung prüfen |
| Fehlende Opferanoden am Geber-Durchbruch | 25% | Anodenstatus prüfen |
| Landstrom-bedingte Galvanik (Marina) | 20% | Galvanic Isolator vorhanden? |
| Verbrauchte Opferanoden (Zink/Aluminium) | 15% | Anoden visuell prüfen (<50% = ersetzen) |
| Kunststoffgeber in ungeeignetem Umfeld (Aluminium-Rumpf) | 10% | Materialkompatibilität prüfen |

**AYDI-Bewertung:**
- Confidence: `visual_high` (deutlich sichtbare Korrosion), `measured` (Potentialmessung)
- Kostenrahmen: 100–500 EUR (Anoden + Dichtung), 500–2.000 EUR (Durchbruch ersetzen + Werftaufenthalt)

---

## 7. Troubleshooting-Entscheidungsbäume

### 7.1 Entscheidungsbaum: Kein GPS-Signal

```
START: MFD zeigt "Kein GPS-Signal"
│
├─ Frage 1: Ist ein externer GPS-Empfänger vorhanden?
│   ├─ JA → Weiter mit Frage 2
│   └─ NEIN (GPS im MFD integriert) → Frage 1b: Sieht das MFD überhaupt Satelliten?
│       ├─ JA (Satelliten sichtbar, aber kein Fix) → Abschattung/Multipath.
│       │   Aktion: MFD an Deck testen (freie Sicht). Wenn dort Fix → Einbauposition überdenken.
│       └─ NEIN (0 Satelliten) → Hardware-Defekt MFD oder interne Antenne.
│           Aktion: Factory Reset. Wenn kein Erfolg → Hersteller-Service.
│
├─ Frage 2: Ist der GPS-Empfänger per NMEA 2000 oder NMEA 0183 angebunden?
│   ├─ NMEA 2000 → Frage 3a: Sieht das MFD den GPS-Empfänger in der Geräteliste?
│   │   ├─ JA (Gerät sichtbar, aber "No Data") → GPS-Empfänger hat kein Sat-Signal.
│   │   │   Aktion: GPS-Antennenkabel prüfen, Antenne inspizieren.
│   │   └─ NEIN (Gerät nicht sichtbar) → NMEA-2000-Bus-Problem.
│   │       Aktion: → Entscheidungsbaum 7.3 (NMEA 2000 Diagnose)
│   │
│   └─ NMEA 0183 → Frage 3b: Kommen NMEA-0183-Sätze am MFD an?
│       ├─ JA (Sätze kommen, aber ohne Fix) → GPS-Empfänger hat kein Signal.
│       │   Aktion: Antenne/Kabel prüfen.
│       └─ NEIN (keine Sätze) → Verdrahtungsfehler.
│           Aktion: TX/RX-Zuordnung prüfen, Baudrate prüfen (4800 vs. 38400).
│
├─ Frage 4 (wenn GPS-Antenne extern): Kabel durchmessen
│   ├─ Durchgang OK → Stecker korrodiert? Reinigen. Wenn nein → Empfänger defekt.
│   └─ Kein Durchgang → Kabel ersetzen.
│
└─ ERGEBNIS:
    ├─ Kabel/Stecker-Problem → Reparatur 50–300 EUR
    ├─ GPS-Empfänger defekt → Ersatz 200–800 EUR
    ├─ NMEA-Bus-Problem → Entscheidungsbaum 7.3
    └─ MFD-internes GPS defekt → Hersteller-Service oder externer GPS-Empfänger nachrüsten
```

### 7.2 Entscheidungsbaum: Radar zeigt keine Ziele

```
START: Radarbild leer oder nahezu leer (kein Land, keine Schiffe)
│
├─ Frage 1: Dreht der Radar-Scanner?
│   ├─ JA → Frage 2
│   └─ NEIN → Frage 1b: Ist Spannung am Scanner?
│       ├─ JA (12V vorhanden) → Motor oder Steuerplatine defekt → Service.
│       └─ NEIN → Sicherung prüfen, Kabelverbindung Scanner.
│
├─ Frage 2: Erscheint auf dem MFD ein Radarbild (auch wenn leer)?
│   ├─ JA (Radar-Seite zeigt Rings, aber keine Echos) → Frage 3
│   └─ NEIN (Radar-Seite zeigt Fehler oder "Kein Radar") →
│       Frage 2b: Ethernet/Signalkabel prüfen.
│       Aktion: Kabel am Scanner und am MFD prüfen, ggf. tauschen.
│       Wenn Kabel OK → Firmware-Versionen kompatibel? Update durchführen.
│
├─ Frage 3: Sind STC/FTC-Regler (Sea Clutter / Rain Clutter) zu hoch eingestellt?
│   ├─ JA → Regler zurückdrehen, dann erneut prüfen.
│   └─ NEIN → Frage 4
│
├─ Frage 4: Radar-Typ?
│   ├─ Magnetron → Frage 4a: Wie alt ist das Magnetron?
│   │   ├─ >8 Jahre / >5.000 Stunden → Magnetron wahrscheinlich verbraucht.
│   │   │   Aktion: Magnetron ersetzen (Fachservice) — 500–2.000 EUR + Einbau.
│   │   └─ <8 Jahre → Wellenleiter oder HV-Versorgung prüfen (Fachservice).
│   │
│   └─ Halbleiter (FMCW/Broadband) → Frage 4b: Funktioniert Nahbereich (<1nm)?
│       ├─ JA (Nahbereich OK, Fernbereich leer) → Normal für Halbleiter, Reichweite begrenzt.
│       │   Erwartung: 24–36nm max. Wenn deutlich weniger → Service.
│       └─ NEIN (auch Nahbereich leer) → Sender-Modul defekt → Hersteller-Service.
│
└─ ERGEBNIS:
    ├─ Clutter-Einstellung → Kostenlos (Einstellung korrigieren)
    ├─ Kabel → 100–500 EUR
    ├─ Magnetron → 500–2.000 EUR + Arbeit
    ├─ Scanner-Motor → 300–1.000 EUR + Arbeit
    └─ Sender-Modul (Solid State) → 1.000–3.000 EUR (oft wirtschaftlicher Totalschaden)
```

### 7.3 Entscheidungsbaum: NMEA-2000-Netzwerk Diagnose

```
START: Ein oder mehrere Geräte liefern keine Daten über NMEA 2000
│
├─ Frage 1: Sind ALLE Geräte betroffen oder nur einzelne?
│   ├─ ALLE Geräte → Frage 2 (Gesamtnetzwerk-Problem)
│   └─ NUR EINZELNE → Frage 5 (Gerätespezifisch)
│
├─ Frage 2: Bus-Spannung messen (zwischen Pin 3 [GND] und Pin 4 [+12V])
│   ├─ 0V → Netzteil defekt oder Sicherung.
│   │   Aktion: Sicherung prüfen, Netzteil prüfen, Verpolungsschutz.
│   ├─ <9V → Unterspannung. Zu viele Verbraucher oder Kabel zu dünn.
│   │   Aktion: LEN summieren. Zweites Netzteil einsetzen.
│   └─ 9–16V (OK) → Frage 3
│
├─ Frage 3: Bus-Widerstand messen (Backbone vom Strom trennen, zwischen CAN-H und CAN-L)
│   ├─ ~60Ω → Beide Terminierungen korrekt → Frage 4
│   ├─ ~120Ω → Nur 1 Terminierung → Zweiten Terminator suchen/einsetzen!
│   ├─ >200Ω oder ∞ → Keine Terminierung oder Kabelbruch → Backbone segmentweise prüfen.
│   └─ <30Ω → Kurzschluss! Geräte einzeln trennen, bis Widerstand steigt.
│
├─ Frage 4: Mit Diagnosetool (Actisense NGT-1 oder Maretron USB100) am Bus:
│   ├─ PGNs werden empfangen, aber CAN-Error-Frames häufig (>1% Fehlerrate)?
│   │   → EMI-Problem oder defektes Gerät. Geräte einzeln trennen und Error-Rate beobachten.
│   └─ PGNs werden empfangen, niedrige Fehlerrate → Netzwerk grundsätzlich OK.
│       Problem liegt am MFD (konfigurieren) oder am spezifischen Gerät.
│
├─ Frage 5 (Einzelnes Gerät fällt aus):
│   ├─ Drop-Line-Kabel prüfen (Durchgang, Stecker)
│   ├─ Gerät an anderem T-Stück / Drop-Line versuchen
│   ├─ Geräte-Firmware aktuell?
│   ├─ Geräte-Address-Claim-Konflikt? (Diagnosetool: doppelte Adressen?)
│   └─ Wenn alles OK → Gerät defekt (NMEA-2000-Interface)
│
└─ ERGEBNIS:
    ├─ Terminierungsfehler → 10–30 EUR (Terminator kaufen)
    ├─ Kabelfehler → 30–200 EUR
    ├─ Steckerfehler → 20–80 EUR
    ├─ Netzteil → 50–200 EUR
    ├─ EMI-Problem → Kabelumverlegung 100–500 EUR
    └─ Gerätedefekt → je nach Gerät 200–3.000 EUR
```

### 7.4 Entscheidungsbaum: Autopilot steuert schlecht

```
START: Autopilot hält Kurs nicht oder steuert unruhig
│
├─ Frage 1: In welchem Modus tritt das Problem auf?
│   ├─ AUTO (Kompasskurs) → Frage 2
│   ├─ WIND → Frage 6
│   └─ TRACK/NAV → Frage 7
│
├─ Frage 2: Heading-Anzeige am Autopilot korrekt?
│   │   (Vergleich mit Handpeilkompass / GPS-COG bei gerader Fahrt ohne Strom)
│   ├─ Abweichung >5° → Kompass-Deviation oder magnetische Störung.
│   │   Aktion: Deviation-Kalibrierung durchführen (360°-Drehung, ruhiges Wasser).
│   │   Wenn nach Kalibrierung immer noch >5° → Kompassposition ändern.
│   │   Magnetische Störquellen: Lautsprecher, Elektro-Winschen, Eisen/Stahl in Nähe.
│   └─ Heading OK (±5°) → Frage 3
│
├─ Frage 3: Ruderrückmeldung (Feedback) korrekt?
│   │   (Am MFD Ruderwinkel ablesen, gleichzeitig Ruder visuell beobachten)
│   ├─ Anzeige stimmt nicht mit Ruder überein → Feedback-Sensor justieren.
│   │   Aktion: Mittelstellung einstellen, Endanschläge prüfen.
│   └─ Feedback stimmt → Frage 4
│
├─ Frage 4: Steuerbewegungen des Autopiloten beobachten:
│   ├─ Zu häufig, zu große Ausschläge (Hunting/Oversteering)
│   │   → Gain/Rudder-Empfindlichkeit zu hoch. Reduzieren.
│   │   → Counter-Rudder zu niedrig. Erhöhen.
│   ├─ Zu selten, Boot driftet ab bevor korrigiert wird
│   │   → Gain zu niedrig. Erhöhen.
│   │   → Deadband zu groß. Reduzieren.
│   └─ Korrekturen angemessen, aber Boot reagiert trotzdem schlecht → Frage 5
│
├─ Frage 5: Mechanisches Problem?
│   ├─ Ruderlager hat Spiel? → Lager ersetzen.
│   ├─ Seilzug-/Ketten-Steuerung: Lose? → Nachspannen.
│   ├─ Hydraulik: Öl-Leck? Luft im System? → Entlüften, Leck abdichten.
│   └─ Antrieb zu schwach (Boot >15t, aber kleiner Linearantrieb)?
│       → Größeren Antrieb / Hydraulik nachrüsten.
│
├─ Frage 6 (Wind-Modus-Probleme):
│   ├─ Wind-Daten prüfen → Windmesser OK? (→ Fehlerbild 6.10)
│   ├─ AWA-Kalibrierung korrekt? → Auf Bug-Wind prüfen (0° ± 3°)
│   └─ Autopilot-Windparameter anpassen (Response, Tack-Angle, Gust-Response)
│
├─ Frage 7 (Track/NAV-Modus-Probleme):
│   ├─ GPS-Position korrekt? → Vergleich mit Kartendarstellung
│   ├─ XTE-Daten vom MFD korrekt? → NMEA-Datenfluss prüfen
│   └─ Kurs-Änderungsgrenzen (Course Change Limit) zu restriktiv? → Erweitern
│
└─ ERGEBNIS:
    ├─ Kalibrierung → Kostenlos (Zeitaufwand 30–60 Min.)
    ├─ Parameter-Anpassung → Kostenlos
    ├─ Feedback-Justierung → 0–100 EUR
    ├─ Kompass-Position ändern → 100–500 EUR
    ├─ Mechanische Reparatur → 200–2.000 EUR
    └─ Antrieb-Upgrade → 1.000–5.000 EUR
```

### 7.5 Entscheidungsbaum: UKW-Funk DSC-Notruf funktioniert nicht

```
START: DSC-Notruf kann nicht ausgelöst werden oder wird nicht quittiert
│
├─ Frage 1: Ist eine MMSI im Funkgerät programmiert?
│   ├─ JA → Frage 2
│   └─ NEIN → MMSI programmieren! Ohne MMSI kein DSC möglich.
│       Hinweis: MMSI nur 1× programmierbar bei den meisten Geräten.
│       Bei Neuprogrammierung: Hersteller-Service oder BSH kontaktieren.
│       MMSI beantragen: BSH (Deutschland), BAKOM (Schweiz), OFCOM (Österreich via FMB).
│
├─ Frage 2: Empfängt das Funkgerät eine GPS-Position?
│   ├─ JA (Position im Display) → Frage 3
│   └─ NEIN → GPS-Anbindung herstellen!
│       ├─ NMEA-0183-Verbindung prüfen (GGA- oder RMC-Satz, 4800 Baud)
│       ├─ NMEA-2000-Verbindung prüfen (PGN 129029)
│       └─ Eingebautes GPS aktivieren (falls vorhanden)
│       KRITISCH: Ohne GPS-Position wird ein Notruf OHNE Koordinaten gesendet!
│       Küstenfunkstelle muss dann erst peilen → massive Verzögerung!
│
├─ Frage 3: DSC-Test durchführen (Testmodus, NICHT echter Notruf!)
│   │   Die meisten Geräte haben einen DSC-Testmodus:
│   │   Icom: Menu → DSC → DSC Test Call → Küstenfunkstelle-MMSI
│   │   Standard Horizon: Menu → DSC → Test Call
│   │   Warten auf Acknowledgement (bis zu 5 Min.)
│   ├─ Acknowledgement empfangen → System funktioniert!
│   │   Aktion: Keine. System OK. Ggf. regelmäßig testen (alle 3 Monate).
│   └─ Kein Acknowledgement → Frage 4
│
├─ Frage 4: Sendet das Funkgerät auf Kanal 70 (156,525 MHz)?
│   │   Prüfbar durch: LED/Display-Anzeige "TX" beim DSC-Senden
│   ├─ JA (TX aktiv) → Antennenproblem.
│   │   Aktion: → Fehlerbild 6.8 (UKW-Reichweite). SWR prüfen.
│   └─ NEIN (kein TX) → Funkgerät-Defekt oder Blockierung.
│       ├─ Kanal 70 blockiert? (Scan-Ausschlussliste prüfen)
│       ├─ Sendesperre aktiv? (z.B. nach Fehlbedienung)
│       └─ PA-Stufe defekt → Hersteller-Service
│
├─ Frage 5: Wurde die Küstenfunkstelle auf richtigem Weg kontaktiert?
│   ├─ DSC-Notruf geht an alle → Keine MMSI des Empfängers nötig
│   └─ DSC-Einzelruf → Korrekte MMSI des Empfängers eingegeben?
│
└─ ERGEBNIS:
    ├─ MMSI fehlt → Programmierung (kostenlos bei Neukauf, 50–100 EUR beim Service)
    ├─ GPS fehlt → Anbindung herstellen (0–200 EUR)
    ├─ Antenne → 50–400 EUR
    ├─ Funkgerät-Defekt → Reparatur 100–300 EUR oder Ersatz 200–800 EUR
    └─ System OK → Regelmäßige DSC-Tests empfehlen
```

---

## 8. FAQ

### 8.1 Grundlagen-Fragen

**F01: Was ist der Unterschied zwischen GPS und GNSS?**
GPS (Global Positioning System) ist das US-amerikanische Satellitennavigationssystem. GNSS (Global Navigation Satellite System) ist der Oberbegriff für alle Systeme: GPS (USA), GLONASS (Russland), Galileo (EU), BeiDou (China). Moderne Marineempfänger nutzen Multi-GNSS, also alle Systeme gleichzeitig, für bessere Genauigkeit und Verfügbarkeit.

**F02: Wie genau ist GPS auf dem Wasser?**
Standard-GPS: 3–5m (95% der Zeit). Mit SBAS/EGNOS (Europa): 1–2m. Mit Galileo HAS: ~0,2m. Für die meisten Navigationszwecke reichen 3–5m völlig aus. Für Anlegemanöver in engen Häfen oder präzise Ankerwache kann SBAS sinnvoll sein.

**F03: Brauche ich NMEA 2000 oder reicht NMEA 0183?**
Für ein einfaches System (GPS → MFD → Autopilot) kann NMEA 0183 ausreichen. Sobald mehr als 3–4 Geräte vernetzt werden sollen, ist NMEA 2000 die deutlich bessere Wahl: Plug-and-Play, Geräte erkennen sich automatisch, ein Kabel für alles, und bidirektionale Kommunikation.

**F04: Was ist der Unterschied zwischen einem Kartenplotter und einem MFD?**
Historisch war ein Kartenplotter ein reines Navigationsgerät (Karte + GPS). Ein MFD (Multi Function Display) integriert zusätzlich Radar, Echolot, AIS, Motorüberwachung etc. Heute sind die Begriffe faktisch synonym, da alle aktuellen Kartenplotter MFD-Funktionalität bieten.

**F05: Benötige ich eine Papier-Seekarte trotz Kartenplotter?**
Ja. In vielen Fahrtgebieten ist eine aktuelle Papier-Seekarte als Backup empfohlen oder vorgeschrieben. Elektronik kann ausfallen (Stromausfall, Defekt, Blitzschlag). Für Küstennavigation innerhalb der EU-Sportbootrichtlinie: Amtliche Seekarte des Fahrtgebiets wird empfohlen.

### 8.2 Geräte-Fragen

**F06: Wie groß sollte mein MFD-Display sein?**
Faustregel: Mindestens 7" für Boote bis 10m, 9–12" für 10–16m, 12–16" für 16–22m. Für Segelyachten mit offenem Cockpit sind helle Displays (>1.000 nit) wichtiger als Größe. Für Motorboote an der Brücke eher groß (12"+) wegen der Blickdistanz.

**F07: Was ist besser — Raymarine, Garmin, Simrad oder Furuno?**
Es gibt kein objektiv "bestes" System. Empfehlungen nach Einsatzprofil:
- **Regatta-Segler:** B&G (SailSteer, Polarkurven, H5000)
- **Fahrtensegler:** Raymarine (gutes Allround-System, ClearCruise AR) oder Garmin (beste Displayhelligkeit)
- **Motorboot/Fischer:** Garmin (Sonar-Integration, ActiveCaptain) oder Simrad (Halo-Radar)
- **Custom-Yacht 18m+:** Furuno (Premium-Radar, Berufsschifffahrt-Zuverlässigkeit)
- **Budget-bewusst:** Garmin oder Simrad (breiteste Preispalette)

**F08: Kann ich Geräte verschiedener Hersteller mischen?**
Über NMEA 2000: Ja, grundsätzlich problemlos. Ein Garmin-MFD kann Daten von einem Simrad-Windgeber oder einem Furuno-GPS anzeigen. Über proprietäre Netzwerke (Ethernet): Nein, Radar und Sonar müssen zum MFD-Hersteller passen. Autopilot: In der Regel herstellerintern (Ausnahme: NMEA-2000-basierte Autopiloten funktionieren grundsätzlich mit jedem MFD im NAV-Modus).

**F09: Brauche ich einen Antennensplitter für VHF und AIS?**
Wenn nur eine UKW-Antenne vorhanden ist (typisch bei Segelyachten mit Masttopp-Antenne): Ja, ein Antennensplitter teilt die Antenne zwischen VHF-Funk und AIS-Transponder. Qualitätssplitter (z.B. Vesper SP160, Shakespeare AIS-100) verursachen ~0,5 dB Verlust — akzeptabel. Besser, aber aufwendiger: Zwei separate Antennen.

**F10: Was ist ein Heading-Sensor und warum brauche ich ihn?**
Ein Heading-Sensor liefert die aktuelle Bugausrichtung (Vorauslinie) des Bootes. Ohne Heading-Sensor kann der Autopilot keinen Kurs halten, das Radar kein korrektes Overlay darstellen, und MARPA nicht funktionieren. Bei einfachen Systemen reicht ein Fluxgate-Kompass (300–500 EUR). Premium: GPS-Kompass mit Dual-Antenne (1.500–5.000 EUR) — keine Deviation, sofort korrekt.

### 8.3 AIS-Fragen

**F11: Class B oder Class B+ — was ist der Unterschied?**
Class B (CS/CSTDMA) sendet mit 2W und nachrangigem Kanalzugriff. In stark befahrenen Gewässern (Ärmelkanal, Elbe, Rotterdam) kann der Class-B-Sender von Class-A-Schiffen verdrängt werden. Class B+ (SOTDMA) sendet mit 5W und nutzt das gleiche Zugriffsverfahren wie Class A — deutlich bessere Sichtbarkeit. Empfehlung: Class B+ für Yachten >12m und Reviere mit dichtem Berufsverkehr.

**F12: Ist AIS Pflicht für Sportboote?**
In Deutschland/EU: Nein, AIS ist für Sportboote (noch) keine Pflicht. Aber: In der Praxis ist AIS quasi-Standard geworden. Viele Reviere (z.B. Wattenmeer, Kieler Förde, Sund) empfehlen AIS dringend. Für die Sicherheit ist ein AIS-Transponder eine der sinnvollsten Investitionen.

**F13: Kann ich AIS abschalten (Silent Mode)?**
Ja, die meisten Class-B-Transponder haben einen "Silent Mode". Gründe: Privatsphäre in der Marina, Segeltörn ohne Tracking. Bedenken: Im Silent Mode ist die Yacht für andere AIS-Nutzer und VTS-Stationen unsichtbar. Empfehlung: Silent Mode nur im Hafen, NIEMALS in Fahrwassern oder bei eingeschränkter Sicht.

### 8.4 Radar-Fragen

**F14: Halbleiter- oder Magnetron-Radar?**
Für Yachten bis 16m ist ein Halbleiter-Radar (Broadband/FMCW) fast immer die bessere Wahl: Sofort betriebsbereit, stromsparender, besser im Nahbereich, wartungsfrei. Magnetron-Radar nur noch für: Langstreckenüberquerungen (>36 nm Reichweite nötig), gewerbliche Fahrzeuge, bestehende Installationen.

**F15: Reicht ein 18"-Radom oder brauche ich ein 24"-Radom?**
18"-Radom: Ausreichend für Küstennavigation, Yachten 8–12m. Typische Strahlbreite ~6°. 24"-Radom: Bessere Zielunterscheidung (Strahlbreite ~4°), empfohlen ab 12m und für Offshore-Fahrten. Open Array: Erst ab 14m sinnvoll, wenn maximale Radarleistung benötigt wird.

**F16: Wie hoch muss das Radar montiert werden?**
So hoch wie sinnvoll möglich — aber es gibt Grenzen: Radar-Horizont = 2,2 × √(Höhe in m) in nm. Bei 4m Höhe: ~4,4 nm Horizont. Bei 10m Höhe: ~7,0 nm. Auf Segelyachten: Masttopp oder Saling (8–15m) ergibt 6–8,5 nm Horizont. Auf Motorbooten: Fly Bridge oder Mast (3–6m) ergibt 3,8–5,4 nm. ACHTUNG: Je höher, desto mehr Kippbewegung bei Seegang → Strahlbreite vertikal beachten.

### 8.5 Netzwerk-Fragen

**F17: Was ist ein NMEA-2000-Backbone?**
Das Backbone ist das zentrale Kabel, an dem alle NMEA-2000-Geräte über T-Stücke und Drop-Lines angeschlossen werden. Es hat genau zwei Enden, an denen je ein 120Ω-Terminierungswiderstand sitzt. Ohne korrekte Terminierung funktioniert der Bus nicht zuverlässig.

**F18: Wie viele Geräte kann ich an NMEA 2000 anschließen?**
Maximal 50 Geräte pro Netzwerk. In der Praxis: Typische 12m-Yacht hat 8–15 Geräte — weit unter dem Limit. Die Begrenzung kommt eher durch die elektrische Belastung (LEN): Max. 30 LEN pro Netzteil. Ein zweites Netzteil kann bei Bedarf hinzugefügt werden.

**F19: Warum brauche ich einen Gateway zwischen NMEA 0183 und NMEA 2000?**
Ältere Geräte (z.B. Autopilot, Windmesser, Echolot) haben oft nur NMEA-0183-Ausgang. Um diese in ein NMEA-2000-Netzwerk einzubinden, ist ein Gateway nötig (z.B. Actisense NGW-1, Garmin NMEA 2000 Gateway). Das Gateway übersetzt die Satzformate bidirektional.

**F20: Was ist der Unterschied zwischen SeaTalkNG und NMEA 2000?**
SeaTalkNG (Raymarine) ist elektrisch und protokollmäßig zu 100% NMEA-2000-kompatibel — es verwendet nur andere Stecker (runde 5-polige Stecker statt Micro-C). Mit einem Adapterkabel (Raymarine A06045/A06075) können beliebige NMEA-2000-Geräte an ein SeaTalkNG-Netzwerk angeschlossen werden und umgekehrt.

### 8.6 Installation und Wartung

**F21: Wie oft sollte die Navigations-Elektronik gewartet werden?**
Empfehlung: Jährlich (vor Saisonbeginn):
- Firmware-Updates für alle Geräte prüfen und installieren
- Kartenmaterial aktualisieren
- NMEA-2000-Stecker visuell inspizieren (Korrosion?)
- Antennenanschlüsse prüfen (UKW, GPS, Radar)
- Windmesser inspizieren (Gängigkeit, Verschmutzung)
- Echolot-Geber reinigen
- Autopilot-Kalibrierung prüfen (Deviation)
- AIS-Transponder-Test (Marine Traffic prüfen)
- Batterien in PLB/EPIRB prüfen (Ablaufdatum)

**F22: Wie schütze ich Elektronik vor Blitzschlag?**
Vollständiger Schutz ist unmöglich, aber Risikominderung:
- Blitzableiter am Masttopp mit ausreichendem Erdungskabel (min. 50mm² Kupfer) zur Erdungsplatte
- Erdungsplatte am Unterwasserschiff (min. 0,1 m² Kupfer)
- Überspannungsschutz an Spannungsversorgung der Elektronik
- Bei Gewitterwarnung: Alle abziehbaren Antennenstecker lösen, Geräte ausschalten
- AIS-SART und PLB als Backup (batteriebetrieben, nicht von Bordnetz abhängig)

**F23: Wie aktualisiere ich Seekarten?**
- **Navionics (Garmin):** Navionics+ Abo (~50 EUR/Jahr), Updates über WiFi oder SD-Karte
- **C-MAP (Simrad/B&G):** C-MAP Abo (~60 EUR/Jahr), Updates über SD-Karte oder App
- **Raymarine LightHouse Charts:** Abo oder Einzelkauf, Updates über WiFi oder SD-Karte
- **Furuno TimeZero Charts:** Über TimeZero App oder SD-Karte
- WICHTIG: Seekarten sollten mindestens jährlich aktualisiert werden — neue Tonnen, veränderte Fahrwasser, neue Tiefenmessungen

**F24: Muss ich mein Funkgerät registrieren?**
Ja. In Deutschland benötigt jede Seefunkstelle:
1. **Frequenzzuteilungsurkunde** der BNetzA (Bundesnetzagentur): Enthält MMSI und Rufzeichen
2. **Schiffsfunkstellengenehmigung**: Erlaubnis zum Betrieb
3. **Seefunkzeugnis** des Bedieners: SRC oder LRC
- Für reine Binnenschifffahrt: UBI + Frequenzzuteilungsurkunde Binnenfunk
- MMSI beantragen bei: BNetzA (Außenstelle Mülheim/Ruhr) oder BSH

**F25: Welche NMEA-2000-Kabel soll ich verwenden?**
Für Yachten bis 24m: **Micro-C** (auch "DeviceNet Micro" genannt). Empfohlene Hersteller:
- **Maretron:** Premium-Qualität, farbcodiert, verschiedene Längen ab Lager
- **Garmin NMEA 2000 Kabel:** Preisgünstig, gute Qualität
- **Ancor/Marinco:** Marine-Qualität, Steckersystem
- **Selbstbau:** Möglich mit DeviceNet-Micro-Steckern und 5-poligem geschirmtem Kabel — aber: Nicht NMEA-zertifiziert, bei Garantiefällen problematisch

### 8.7 Fortgeschrittene Fragen

**F26: Wie plane ich ein Navigationssystem von Grund auf?**
Vorgehensweise in 8 Schritten:
1. Bootstyp und Einsatzprofil definieren (Küste/Offshore/Langfahrt, Segel/Motor, Crew-Größe)
2. Pflichtausrüstung nach Fahrtgebiet ermitteln (Funk, EPIRB, AIS)
3. MFD-Hersteller wählen (Ökosystem-Entscheidung — Radar/Sonar müssen passen)
4. NMEA-2000-Backbone planen (Topologie, Kabellängen, Geräteanzahl)
5. Sensoren wählen (Wind, Tiefe, Speed, Heading)
6. Autopilot dimensionieren (Verdrängung, Rudertyp, Antriebsart)
7. Kommunikation planen (VHF, AIS, ggf. Satcom)
8. Installation durch qualifizierten Fachbetrieb oder sorgfältige Eigeninstallation

**F27: Was kostet ein komplettes Navigationssystem?**
Richtwerte (komplett installiert, inkl. Arbeit):
- Segelboot 8–10m, Küste: 4.000–8.000 EUR
- Segelyacht 10–14m, Offshore: 8.000–18.000 EUR
- Segelyacht 14–18m, Langfahrt: 15.000–35.000 EUR
- Motoryacht 10–14m: 6.000–15.000 EUR
- Motoryacht 14–20m: 15.000–40.000 EUR
- Superyacht 20m+: 40.000–200.000+ EUR

**F28: Wie integriere ich Starlink / Satelliten-Internet?**
Starlink Maritime / Starlink Mobility:
- Antenne: Flachantenne ~60cm, Montage auf Flybridge/Deckslevel, freie Sicht zum Himmel
- Daten: 50–200 Mbit/s Download, weltweit (außer hohe Breitengrade)
- Kosten: ~250–400 EUR/Monat (Starlink Mobility), Hardware ~2.500 EUR
- Integration: Ethernet → Marine-Router → WiFi-Netz an Bord
- NMEA-Integration: Nicht direkt, aber Wetter/Karten-Downloads über Internet
- Stromverbrauch: 50–100W (erheblich für Segelyacht!)

**F29: Was ist NMEA OneNet und wird es NMEA 2000 ersetzen?**
NMEA OneNet ist ein Ethernet-basiertes Protokoll (in Entwicklung), das NMEA 2000 für datenintensive Anwendungen ergänzen soll (Radar-Rohdaten, Video, Sonar). Es ersetzt NMEA 2000 nicht, sondern ergänzt es. NMEA 2000 bleibt für Sensoren (Wind, Tiefe, GPS, Motor) der Standard. OneNet richtet sich an die MFD-zu-MFD- und MFD-zu-Radar-Kommunikation.

**F30: Wie funktioniert Radar-Overlay auf der Seekarte?**
Das MFD überlagert das Radarbild als transparente Schicht über die Seekarte. Voraussetzungen: GPS-Position (um Seekarte und Radar zu positionieren), Heading-Sensor (um das Radarbild korrekt auszurichten), korrekte Radar-Offset-Werte (Abstand Radarantenne ↔ GPS-Antenne). Das Radar-Overlay ermöglicht den direkten Vergleich: "Stimmt das, was ich auf dem Radar sehe, mit der Karte überein?"

### 8.8 Spezialfragen — Langfahrt und Offshore

**F31: Welche Kommunikationsmittel brauche ich für eine Atlantiküberquerung?**
Mindestausrüstung (Empfehlung, nicht gesetzlich vorgeschrieben für Sportboote):
- UKW-Funk mit DSC (für Küstennähe und Schiff-zu-Schiff)
- GW/KW-Seefunk (SSB) mit Pactor-Modem (für E-Mail via Winlink, Wetterfax)
- Iridium GO! exec oder Iridium-Satellitentelefon (für Notruf, Positionsmeldungen, Wetter)
- EPIRB (406 MHz, registriert)
- PLB (mindestens 1 pro Person, an Rettungsweste)
- AIS Class B+ Transponder
- Optional, aber zunehmend beliebt: Starlink Maritime (Internet auf See, aber hoher Stromverbrauch)

**F32: Was ist ein Pactor-Modem und warum nutzen Langfahrtsegler es?**
Ein Pactor-Modem (z.B. SCS PTC-IIusb) verbindet den GW/KW-Seefunkempfänger mit einem Computer und ermöglicht den Empfang und Versand von E-Mails und Wetterdaten über das Winlink-Netzwerk (HF-Funk-E-Mail). Kosten: ~1.200–1.800 EUR für das Modem, keine laufenden Kosten (Winlink ist kostenlos). Bandbreite: ~2–3 kBit/s — ausreichend für Text-E-Mails, Wetterbriefings (GRIB-Dateien), und Positionsmeldungen.

**F33: Wie sichere ich meine Elektronik bei einem Blitzeinschlag?**
Vollständiger Schutz ist unmöglich. Risikominderung:
1. Blitzableiter am Masttopp mit durchgehendem Kupferkabel (min. 50mm²) zur Erdungsplatte
2. Erdungsplatte am Unterwasserschiff (min. 0,1m² Kupfer oder Bronzekiel)
3. Alle Antennen mit Überspannungsschutz (MOV/Gasentladungsableiter) versehen
4. Trennschalter für Elektronik-Hauptversorgung — bei Gewitter: Geräte ausschalten, Antennenstecker ziehen
5. Ersatzgeräte in einer Faraday-Tasche (z.B. Handheld-GPS, Handpeilkompass, Handfunkgerät)
6. Kabelschirmung konsequent erden (NMEA-2000-Schirm an einer Seite auflegen)
7. Versicherung: Marine-Elektronik-Versicherung deckt Blitzschlag ab (ca. 1–3% des Neuwerts p.a.)

**F34: Wie kalibriere ich einen Fluxgate-Kompass korrekt?**
Kalibrierungsvorgang (ähnlich bei allen Herstellern):
1. Ruhiges Wasser (Hafen/Bucht), kein Strom, wenig Wind
2. Alle bordtypischen Verbraucher einschalten (Autopilot, Funk, Ladegerät — erzeugen Magnetfelder!)
3. Kalibriermodus am Autopilot/MFD starten
4. Boot langsam (1–2 Knoten) in vollständigen 360°-Kreisen drehen (1–2 Umdrehungen)
5. Drehung gleichmäßig, nicht ruckartig — typisch 3–5 Minuten pro Umdrehung
6. Autopilot berechnet Deviation-Tabelle automatisch
7. Ergebnis prüfen: Maximale Deviation sollte <5° sein (ideal <2°)
8. Bei >10°: Kompass umpositionieren (weiter weg von Eisen/Stahl/Magneten/Lautsprechern)
9. Dokumentation: Deviation-Tabelle ausdrucken und am Steuerstand aufhängen

**F35: Was bedeutet "True Wind" vs. "Apparent Wind"?**
- **Apparent Wind (AWA/AWS):** Wind, den die Instrumente am Masttopp messen — die Vektorsumme aus wahrem Wind und Fahrtwind. Ändert sich mit der Bootsgeschwindigkeit.
- **True Wind (TWA/TWS):** Der tatsächliche Wind, korrigiert um die Bootsbewegung. Wird berechnet aus: AWA + AWS + SOG + COG + Heading.
- Für Segeltrimm relevant: AWA/AWS (was das Segel "sieht")
- Für Routenplanung/Polarkurven: TWA/TWS (wetterabhängig, bootsunabhängig)
- Voraussetzung für korrekte True-Wind-Berechnung: Kalibrierter Windgeber, kalibriertes Log, korrekter Heading-Sensor

**F36: Kann ich mein Smartphone als Backup-Kartenplotter verwenden?**
Ja, eingeschränkt. Empfohlene Apps:
- **Navionics (Garmin):** Beste Kartenabdeckung, Offline-Karten, AIS-Overlay (wenn externes AIS verbunden). Ca. 20 EUR/Jahr.
- **iSailor / SailGrib:** Gute Alternative mit offiziellen Seekarten
- **OpenCPN (Tablet/Laptop):** Open-Source-Navigationssoftware, kostenloses Kartenmaterial (ENC)
Einschränkungen: Smartphone-GPS weniger genau als Marine-GPS, Display bei Sonnenlicht kaum lesbar, Akkulaufzeit begrenzt, keine NMEA-Anbindung ohne Zusatzgerät. Fazit: Als Backup geeignet, NICHT als Primärsystem.

**F37: Was ist der Unterschied zwischen Vektor- und Rasterkarten?**
- **Vektorkarten:** Objekte als mathematische Elemente gespeichert (Linien, Flächen, Punkte). Frei zoombar ohne Qualitätsverlust. Abfragbare Objektinformationen (Klick auf Tonne zeigt Kennung). Beispiel: Navionics, C-MAP, BSH ENC.
- **Rasterkarten:** Gescannte Papierkarten als Bild. Beim Zoomen wird das Bild pixelig. Keine Objektabfrage. Gewohntes Papierkartenbild. Beispiel: BSH Sportbootkarten (digital), Admiralty Raster Chart Service.
- Empfehlung: Vektorkarten als Standard (besser für MFD-Navigation), Rasterkarten als Ergänzung (vertrautes Kartenbild, gelegentlich detailreicher in speziellen Revieren).

**F38: Wie teste ich mein NMEA-2000-Netzwerk ohne Spezialwerkzeug?**
Ohne Diagnosetool (Actisense/Maretron) sind folgende Prüfungen möglich:
1. Alle Geräte am MFD in der NMEA-2000-Geräteliste sichtbar? (Einstellungen → Netzwerk → Geräteliste)
2. Daten aller Sensoren plausibel? (Wind, Tiefe, GPS, Motordaten)
3. Multimeter: Widerstand CAN-H zu CAN-L am Backbone messen (Strom aus!) → Soll: ~60Ω
4. Multimeter: Spannung am Backbone messen (Strom an!) → Soll: 9–16V DC
5. Sichtprüfung: Alle Stecker und T-Stücke fest und trocken? Grünspan?
6. Stresstest: Alle Geräte gleichzeitig einschalten, 30 Min. laufen lassen, Ausfälle beobachten

**F39: Warum zeigt mein AIS Schiffe an, die nicht in Sichtweite sind?**
AIS hat eine deutlich größere Reichweite als die optische Sicht, besonders bei Class-A-Schiffen mit 12,5W Sendeleistung. AIS-Reichweite typisch 20–40 nm (abhängig von Antennenhöhe beider Stationen), optische Sicht auf See bei klarem Wetter ~12 nm für ein Großschiff. Zusätzlich: AIS kann über terrestrische Stationen (AIS-Repeater) und Satelliten-AIS (S-AIS) weitergeleitet werden — in der Nähe von Küstenstationen können AIS-Ziele aus viel größerer Entfernung angezeigt werden.

**F40: Wie lange hält die Elektronik auf einer Yacht?**
Erfahrungswerte (Lebenserwartung):
- MFD: 7–12 Jahre (Display-Alterung, Software-Support endet typisch nach 8–10 Jahren)
- Radar (Halbleiter): 12–20 Jahre (keine Verschleißteile)
- Radar (Magnetron): 8–15 Jahre (Magnetron-Ersatz alle 5–8 Jahre: 500–2.000 EUR)
- Autopilot: 10–20 Jahre (mechanische Teile: Antrieb, Pumpe nach 10–15 Jahren Service)
- Windgeber: 5–10 Jahre (Lager, UV-Alterung)
- Echolot-Geber: 10–20 Jahre (Bronze-Durchbruch: praktisch unbegrenzt)
- UKW-Funk: 10–20 Jahre (robust, wenig Verschleiß)
- AIS-Transponder: 10–15 Jahre
- NMEA-2000-Kabel/Stecker: 15–25 Jahre (wenn korrekt installiert)
- GPS-Empfänger: 10–15 Jahre (aber: Genauigkeit verbessert sich mit neueren Modellen)

Empfehlung: Nach 8–10 Jahren komplett evaluieren, nach 12–15 Jahren Kernsystem erneuern.

**F41: Was kostet die jährliche Wartung der Navigationselektronik?**
Richtwerte (ohne Reparaturen):
- Firmware-Updates: Kostenlos (Eigenarbeit) oder 100–200 EUR (Fachbetrieb)
- Kartenmaterial-Abo: 50–80 EUR/Jahr
- Windgeber-Inspektion/Reinigung: 50–150 EUR (wenn Maststeiger benötigt)
- Antennenstecker-Pflege: 20–50 EUR (Material)
- EPIRB-Batterie-Ersatz: 200–350 EUR (alle 5–10 Jahre → 30–50 EUR/Jahr anteilig)
- Gesamt: Typisch 200–500 EUR/Jahr für eine 12m-Yacht

---

## 9. Glossar

| Nr. | Begriff | Erklärung |
|-----|---------|-----------|
| G01 | **AIS** | Automatic Identification System — Automatisches Identifikationssystem, sendet/empfängt Schiffsdaten über UKW |
| G02 | **ARPA** | Automatic Radar Plotting Aid — Automatische Radar-Zielverfolgung auf Berufsschiffen |
| G03 | **AWA** | Apparent Wind Angle — Scheinbarer Windwinkel (relativ zum Bug) |
| G04 | **AWS** | Apparent Wind Speed — Scheinbare Windgeschwindigkeit |
| G05 | **Backbone** | Zentrales NMEA-2000-Kabel, an dem alle Geräte über T-Stücke angeschlossen werden |
| G06 | **Baudrate** | Datenübertragungsgeschwindigkeit in Bit/s (NMEA 0183: 4.800, NMEA 2000: 250.000) |
| G07 | **BeiDou (BDS)** | Chinesisches GNSS-Satellitennavigationssystem |
| G08 | **CAN-Bus** | Controller Area Network — Physikalische Basis von NMEA 2000 (ISO 11898) |
| G09 | **CHIRP** | Compressed High-Intensity Radiated Pulse — Breitband-Echolottechnik mit variabler Frequenz |
| G10 | **COG** | Course Over Ground — Kurs über Grund (GPS-basiert) |
| G11 | **CPA** | Closest Point of Approach — Geringste zu erwartende Annäherung an ein AIS/Radar-Ziel |
| G12 | **CSTDMA** | Carrier Sense TDMA — Kanalzugriffsverfahren für AIS Class B (Standard) |
| G13 | **DOP** | Dilution of Precision — Maß für die Geometrie der sichtbaren Satelliten (niedrig = gut) |
| G14 | **Drop Line** | Stichleitung vom NMEA-2000-Backbone zum Endgerät (max. 6m) |
| G15 | **DSC** | Digital Selective Calling — Digitaler Selektivruf auf UKW-Kanal 70 |
| G16 | **EGNOS** | European Geostationary Navigation Overlay Service — SBAS-Korrektursystem für Europa |
| G17 | **EPIRB** | Emergency Position Indicating Radio Beacon — Seenotsender auf 406 MHz (Cospas-Sarsat) |
| G18 | **FMCW** | Frequency Modulated Continuous Wave — Halbleiter-Radar-Sendemethode |
| G19 | **FLIR** | Forward Looking Infrared — Wärmebildkamera (Teledyne FLIR = Raymarine-Mutter) |
| G20 | **Galileo** | Europäisches GNSS-Satellitennavigationssystem |
| G21 | **GLONASS** | Globalnaja Nawigazionnaja Sputnikowaja Sistema — Russisches GNSS |
| G22 | **GMDSS** | Global Maritime Distress and Safety System — Weltweites Seenot- und Sicherheitsfunksystem |
| G23 | **GNSS** | Global Navigation Satellite System — Oberbegriff für alle Satellitennavigationssysteme |
| G24 | **GPS** | Global Positioning System — US-amerikanisches Satellitennavigationssystem (NAVSTAR) |
| G25 | **HDT** | Heading True — Wahre Vorauslinie (NMEA-0183-Satz) |
| G26 | **LEN** | Load Equivalence Number — Elektrische Belastungszahl eines NMEA-2000-Geräts (1 LEN = 50mA) |
| G27 | **LRC** | Long Range Certificate — Seefunkzeugnis für GW/KW und Satcom |
| G28 | **MARPA** | Mini Automatic Radar Plotting Aid — Yacht-Version der automatischen Radar-Zielverfolgung |
| G29 | **MFD** | Multi Function Display — Multifunktionsdisplay (Kartenplotter + Radar + Sonar + AIS etc.) |
| G30 | **MMSI** | Maritime Mobile Service Identity — 9-stellige Rufnummer eines Seefunkgeräts |
| G31 | **NMEA** | National Marine Electronics Association — US-Organisation, die Datenbusstandards definiert |
| G32 | **PGN** | Parameter Group Number — Datenobjekt-Kennung im NMEA-2000-Protokoll |
| G33 | **PLB** | Personal Locator Beacon — Personenbezogener Seenotsender |
| G34 | **PRF** | Pulse Repetition Frequency — Impulswiederholfrequenz eines Radars |
| G35 | **RCS** | Radar Cross Section — Radar-Rückstreuquerschnitt eines Ziels |
| G36 | **SBAS** | Satellite Based Augmentation System — Satelliten-gestützte Korrekturverfahren (EGNOS, WAAS) |
| G37 | **SOG** | Speed Over Ground — Geschwindigkeit über Grund (GPS-basiert) |
| G38 | **SOTDMA** | Self-Organizing TDMA — Kanalzugriffsverfahren für AIS Class A und Class B+ |
| G39 | **SRC** | Short Range Certificate — Beschränkt gültiges Seefunkzeugnis (UKW) |
| G40 | **SWR** | Standing Wave Ratio — Stehwellenverhältnis (Maß für Antennenanpassung) |
| G41 | **TCPA** | Time to Closest Point of Approach — Zeitdauer bis zur geringsten Annäherung |
| G42 | **TDMA** | Time Division Multiple Access — Zeitmultiplexverfahren (AIS-Kanalzugriff) |
| G43 | **Terminierung** | 120Ω-Abschlusswiderstand an beiden Enden des NMEA-2000-Backbones |
| G44 | **TTFF** | Time To First Fix — Zeit bis zur ersten Positionsbestimmung nach dem Einschalten |
| G45 | **TWA** | True Wind Angle — Wahrer Windwinkel (korrigiert um Bootsbewegung) |
| G46 | **TWS** | True Wind Speed — Wahre Windgeschwindigkeit |
| G47 | **VMG** | Velocity Made Good — Geschwindigkeitskomponente in Richtung Ziel/Wind |
| G48 | **VTS** | Vessel Traffic Service — Schiffsverkehrsdienst (Hafenradar, Verkehrsüberwachung) |
| G49 | **XTE** | Cross Track Error — Querabweichung vom geplanten Kurs (für Autopilot-Steuerung) |
| G50 | **DOP (HDOP/VDOP/PDOP)** | Horizontal/Vertical/Position Dilution of Precision — niedrigere Werte = bessere Satellitengeometrie. HDOP <2 = exzellent, <5 = gut, >10 = schlecht |
| G51 | **RTK** | Real-Time Kinematic — Echtzeit-Korrekturdaten via Internetstream (NTRIP) für cm-genaue Positionierung |
| G52 | **PPP** | Precise Point Positioning — Hochgenaue GNSS-Positionierung ohne lokale Referenzstation (z.B. Galileo HAS) |
| G53 | **ROT** | Rate of Turn — Drehrate des Schiffes in Grad pro Minute |
| G54 | **Deviation** | Ablenkung des Magnetkompasses durch schiffseigene Magnetfelder — kursabhängig, kalibrierbar |
| G55 | **Variation** | Missweisung — Differenz zwischen magnetisch Nord und geographisch Nord — ortsabhängig, zeitlich veränderlich |
| G56 | **Waypoint** | Wegpunkt — eine definierte geographische Position als Navigationsziel oder Routenpunkt |
| G57 | **Polarkurve (VPP)** | Velocity Prediction Program — Geschwindigkeitsvorhersage einer Segelyacht bei gegebener Windstärke und -richtung |
| G58 | **Layline** | Scheinbare Grenzlinie, die anzeigt, ab wann eine Kreuz (Aufkreuzen) den optimalen Kurs zum Luv-Ziel erreicht |
| G59 | **EBL/VRM** | Electronic Bearing Line / Variable Range Marker — Radar-Hilfsmittel zur Peilung und Entfernungsmessung |
| G60 | **Guard Zone** | Alarm-Zone auf dem Radar — löst Alarm aus, wenn ein Ziel in den definierten Bereich eintritt |

---

## 10. Schnell-Referenz

### 10.1 NMEA-2000-Netzwerk: Schnellcheck

```
1. Terminierung:     2 Stück × 120Ω = 60Ω gemessen zwischen CAN-H und CAN-L  ✓
2. Spannung:         9–16V DC zwischen GND und +12V am Backbone                ✓
3. Max. Backbone:    100m (Micro-C) / 200m (Mid-Size)                          ✓
4. Max. Drop-Line:   6m                                                          ✓
5. Max. Geräte:      50 pro Netzwerk                                             ✓
6. Max. LEN:         30 pro Netzteil (1 LEN = 50mA)                             ✓
7. Sicherung:        3A pro Netzteil (typisch)                                   ✓
```

### 10.2 UKW-Seefunk: Wichtigste Kanäle

| Kanal | Frequenz | Verwendung |
|-------|----------|-----------|
| 16 | 156,800 MHz | Not- und Anrufkanal (Pflichtabhörung) |
| 70 | 156,525 MHz | DSC (Digital Selective Calling) — nur digital, kein Sprechfunk |
| 06 | 156,300 MHz | Intership Safety (SAR-Koordination) |
| 09 | 156,450 MHz | Hafendienste, Schlepper, Lotsen |
| 10 | 156,500 MHz | Schiffsverkehrsdienst (VTS) in vielen Revieren |
| 12 | 156,600 MHz | Hafendienste, Port Control |
| 13 | 156,650 MHz | Bridge-to-Bridge (Schiffsverkehr) |
| 67 | 156,375 MHz | SAR (UK), Sicherheit |
| 72 | 156,625 MHz | Intership (frei wählbar für Segler) |
| 77 | 156,875 MHz | Intership (frei wählbar) |
| M1/M2 | — | Marina-Kanäle (regionsspezifisch) |

### 10.3 AIS: MMSI-Nummern verstehen

```
Aufbau einer MMSI: 211XXXXXX

211 = Deutschland (MID = Maritime Identification Digits)
    Erste 3 Ziffern = Landeskennung
    211 = Deutschland
    205 = Belgien
    209 = Zypern
    219 = Dänemark
    226/227/228 = Frankreich
    237 = Griechenland
    244/245/246 = Niederlande
    230/231 = Finnland
    265/266/267 = Schweden
    235/234 = Großbritannien
    247 = Italien
    256 = Malta

00 + 6 Ziffern = Gruppen-MMSI (z.B. 002111240 = MRCC Bremen)
970XXXXXX = AIS-SART
972XXXXXX = MOB-Gerät
974XXXXXX = EPIRB-AIS
```

### 10.4 Kompass-Deviation: Schnellprüfung

```
Methode: Vergleich Kompass vs. GPS-COG bei:
- Ruhigem Wasser (kein Strom, keine Welle)
- Konstantem Kurs (Autopilot oder sehr ruhiges Ruder)
- Mindestfahrt 3 Knoten (für stabilen COG)

8 Kurse fahren: N, NO, O, SO, S, SW, W, NW
Pro Kurs: 2 Minuten Geradeausfahrt
Differenz Heading (Kompass) – COG (GPS) = Deviation auf diesem Kurs

Akzeptable Deviation nach Kalibrierung: ±2° (Premium), ±5° (Standard)
Deviation >10° auf einzelnen Kursen: Magnetische Störquelle suchen!
```

### 10.5 Radar: Reichweite schnell abschätzen

```
Radar-Horizont (nm) = 2,2 × √(Höhe Scanner in Metern)

Scanner auf Geländerstütze (2,5m):  3,5 nm
Scanner auf Fly Bridge (4m):        4,4 nm
Scanner auf Saling (8m):            6,2 nm
Scanner auf Masttopp (15m):         8,5 nm

+ Zielhöhe des Objekts:
Radar sieht Küstenlinie (15m Klippe) in:
  8,5 + 2,2 × √15 = 8,5 + 8,5 = 17,0 nm

Radar sieht Segelboot-Mast (12m) in:
  8,5 + 2,2 × √12 = 8,5 + 7,6 = 16,1 nm

Radar sieht Boje (1m) in:
  8,5 + 2,2 × √1 = 8,5 + 2,2 = 10,7 nm
```

### 10.6 Verkabelung: Kabelquerschnitte für 12V-Systeme

| Gerät | Stromaufnahme | Max. Kabellänge bei 1,5mm² | Empfehlung |
|-------|-------------|---------------------------|-----------|
| MFD 7–9" | 1,5–3A | 8m | 2,5mm² |
| MFD 12–16" | 3–5A | 5m | 4mm² |
| Radar (Halbleiter) | 2–3A | 8m | 2,5mm² |
| Radar (Magnetron) | 5–12A | 3m | 6mm² |
| Autopilot-Computer | 1–2A | 10m | 1,5mm² |
| Autopilot-Antrieb (Linear) | 5–15A | 3m | 6mm² |
| Autopilot-Antrieb (Hydraulik) | 10–30A | 2m | 10–16mm² |
| UKW-Funk | 5–7A (TX) | 5m | 4mm² |
| AIS-Transponder | 0,5–2A | 10m | 1,5mm² |
| NMEA-2000-Netzteil | 1–3A | 8m | 2,5mm² |

### 10.7 Empfohlene Mindestausrüstung nach Fahrtgebiet

**Küstenreviere (Ostsee, Nordsee, Mittelmeer Küste):**
```
[Pflicht/Empfohlen]
✓ MFD/Kartenplotter (min. 7")
✓ GPS-Empfänger (integriert oder extern)
✓ Echolot
✓ UKW-Funk mit DSC (SRC-Zeugnis)
✓ AIS-Transponder (Class B)
✓ Kompass (magnetisch als Backup)
○ Radar (18" Radom) — empfohlen ab Nordsee
○ Autopilot — empfohlen ab 10m
○ EPIRB — empfohlen
```

**Offshore / Kanalüberquerung / Biskaya:**
```
[Pflicht/Empfohlen]
✓ MFD/Kartenplotter (min. 9", empfohlen 12")
✓ GPS-Empfänger (Multi-GNSS)
✓ Echolot
✓ UKW-Funk mit DSC
✓ AIS-Transponder (Class B+ empfohlen)
✓ Radar (min. 24" Radom)
✓ Autopilot
✓ EPIRB (registriert)
✓ PLB (min. 1 pro Person)
○ GW/KW-Funk (SSB) — empfohlen
○ Radarreflektor — empfohlen (wenn RCS < 10m²)
```

**Langfahrt / Atlantiküberquerung:**
```
[Pflicht/Empfohlen]
✓ MFD/Kartenplotter (min. 12", empfohlen Dual-Screen)
✓ GPS-Empfänger (Multi-GNSS, Backup-Handheld)
✓ Echolot
✓ UKW-Funk mit DSC
✓ GW/KW-Funk (SSB) mit Pactor-Modem
✓ AIS Class B+ Transponder
✓ Radar (24" Radom oder Open Array)
✓ Autopilot (Hydraulik empfohlen, Backup-System)
✓ EPIRB (registriert)
✓ PLB (1 pro Person)
✓ Satellitentelefon (Iridium)
✓ Papierseekarten (Backup)
✓ Sextant + Nautisches Jahrbuch (Notfall-Backup)
○ Starlink Maritime — optional (hoher Stromverbrauch)
○ Zweites MFD — empfohlen (Redundanz)
```

### 10.8 Firmware-Update-Checkliste

```
Vor dem Update:
□ Landstrom angeschlossen (stabile Spannungsversorgung!)
□ Batterie-Ladezustand >80%
□ Routen, Wegpunkte, Tracks exportieren (SD-Karte Backup)
□ Geräteeinstellungen notieren / Screenshot
□ Aktuelle Firmware-Version notieren
□ Neue Firmware-Version von Hersteller-Website herunterladen
□ Richtige Firmware für das exakte Modell? (Verwechslungsgefahr!)
□ Release Notes lesen (Breaking Changes?)

Während des Updates:
□ Gerät NICHT ausschalten!
□ Keine anderen Aktionen am Gerät
□ Update-Fortschritt beobachten
□ Typische Dauer: 5–15 Minuten

Nach dem Update:
□ Neustart erfolgreich?
□ Firmware-Version korrekt?
□ Alle Sensordaten vorhanden? (Wind, Tiefe, GPS)
□ NMEA-2000-Geräteliste vollständig?
□ Routen/Wegpunkte noch vorhanden? Ggf. reimportieren
□ Kartenmaterial korrekt angezeigt?
□ Autopilot-Funktionstest (Standby → Auto → Standby)
□ Radar-Funktionstest (wenn aktualisiert)
```

### 10.9 Notfall-Checkliste: Totalausfall Elektronik

```
SOFORTMASSNAHMEN bei Totalausfall der Navigationselektronik:

1. RUHE BEWAHREN — Yacht ist weiterhin seetüchtig
2. Handpeilkompass bereithalten (sollte IMMER an Bord sein)
3. Handfunkgerät einschalten (UKW Kanal 16)
4. Letzte bekannte Position notieren (aus Erinnerung/Logbuch)
5. EPIRB/PLB griffbereit haben (aber NUR bei Seenot auslösen!)
6. Smartphone-Navigation als Backup starten (Navionics App, Offline-Karten)
7. Handheld-GPS einschalten (sollte in Faraday-Tasche bereitliegen)
8. Papierseekarten ausbreiten
9. Terrestrische Navigation: Küstenlinien, Leuchtfeuer, Tonnen visuell identifizieren
10. Fehlerursache suchen: Hauptsicherung? Batteriehauptschalter? Batterie leer?

HÄUFIGSTE URSACHE für Totalausfall:
→ Sicherung durchgebrannt (50%)
→ Batterie leer / Laderegler defekt (25%)
→ Wassereinbruch in Schalttafel (10%)
→ Blitzschlag (5%)
→ Kabelbruch/Kurzschluss (10%)
```

### 10.10 Stecker- und Kabel-Referenz

| Verbindung | Steckertyp | Kabeltyp | Hinweis |
|-----------|-----------|----------|---------|
| NMEA 2000 (Standard) | Micro-C (M12, 5-pol) | DeviceNet Micro | Farbcode: Rot=+12V, Schwarz=GND, Blau=CAN-L, Weiß=Shield |
| NMEA 2000 (Raymarine) | SeaTalkNG (5-pol rund) | SeaTalkNG | Adapter A06045 auf Micro-C |
| NMEA 2000 (Simrad/B&G) | SimNet (9-pol) | SimNet | Adapter AT10-103 auf Micro-C |
| NMEA 0183 | Offen / proprietär | 2×2 geschirmt | TX+/TX- und RX+/RX- (RS-422) |
| UKW-Antenne | PL-259 (UHF) | RG-213 / LMR-400 | Verlust <3 dB Gesamtstrecke |
| GPS-Antenne | BNC oder TNC | RG-58 / RG-174 | Herstellerspezifisch |
| Radar (Raymarine) | RayNet | Cat5e Marine | Wasserdichter Ethernet-Stecker |
| Radar (Garmin) | Garmin Marine | Cat5e Marine | Proprietärer Stecker |
| Radar (Simrad/B&G) | RJ45 + Tülle | Cat5e Marine | Standard-Ethernet |
| Stromversorgung | Ringkabelschuh / Flachstecker | H07V-K Marine | Abgesichert, Querschnitt nach Tabelle 10.6 |

---

## ANHANG A–H — Fallstudien {#anhang-a-h}

### ANHANG A: Fallstudie — Bavaria C42 (2019), Komplette Navigationsmodernisierung

**Ausgangslage:**
- Segelyacht 12,80m (42 ft), Eigner seit 2019, Einsatz Ostsee + Mittelmeer
- Original-Ausrüstung: Raymarine eS78 (7" MFD, 2016-Generation), i70s Instrumente, Quantum Radar 18" Radom
- Problem: MFD-Touchscreen reagiert sporadisch nicht (FB-NAV-007), Kartenplotter langsam, Radar hat Ausfälle

**AYDI-Analyse:**
- Ergonomie-Modul: MFD-Position im Cockpit suboptimal (Sonnenlicht-Problem, seitlicher Blickwinkel)
- Compliance-Modul: AIS fehlt (nur Empfänger im eS78), keine DSC-GPS-Anbindung am Funkgerät
- Kosten-Modul: Upgrade-Budget des Eigners: 8.000–12.000 EUR

**Durchgeführte Maßnahmen:**
1. MFD: Upgrade auf Raymarine Axiom 2 XL 9" (LightHouse 4) — 2.200 EUR
2. Radar: Quantum 2 (18" CHIRP Halbleiter, Ersatz des defekten Quantum 1) — 1.800 EUR
3. AIS: Raymarine AIS700 Class B+ Transponder — 650 EUR
4. VHF: Icom IC-M510 mit integriertem GPS + NMEA-2000-Anbindung — 450 EUR
5. Autopilot: Firmware-Update Evolution EV-200, Neukalibrierung Kompass — 120 EUR (Arbeitszeit)
6. NMEA 2000: Bestehendes SeaTalkNG-Backbone geprüft, 2 korrodierte T-Stücke ersetzt — 80 EUR
7. Installation + Kabel: 2.500 EUR (Fachbetrieb, 2 Tage)
8. Kartenmaterial: Navionics+ Europa Abo — 80 EUR/Jahr

**Gesamtkosten:** ~7.880 EUR
**Ergebnis:** System deutlich verbessert, AIS-Pflichtempfehlung umgesetzt, Touchscreen-Problem gelöst, Radar sofort betriebsbereit (kein Aufwärmen), DSC-Notruf mit automatischer GPS-Position.

### ANHANG B: Fallstudie — Hallberg-Rassy 44 (2015), NMEA-2000-Netzwerkfehler

**Ausgangslage:**
- Segelyacht 13,49m, Langfahrt-Ausrüstung (Karibik-Saison + Nordeuropa)
- Simrad NSS evo3 12", B&G H5000 Prozessor, Simrad AP70 Autopilot, Halo24 Radar
- Problem: Intermittierende Datenverluste — Wind, Tiefe und GPS fallen gleichzeitig aus, kommen nach Minuten wieder

**AYDI-Analyse (Pipeline A — Strukturiert):**
- NMEA-2000-Netzwerk: 14 Geräte, Backbone-Länge 18m (Micro-C), SimNet-Stecker
- Diagnosetool (Actisense NGT-1): 3,2% CAN-Error-Frames — deutlich über Toleranz (<0,5%)
- Systematisches Abklemmen: Fehlerrate sinkt auf 0,1% wenn das Motordaten-Gateway (Yanmar NMEA 2000 Adapter) getrennt wird
- Root Cause: Yanmar-Gateway sendet fehlerhafte PGN 127489 (Engine Parameters) mit zu kurzer Update-Rate → Bus-Überlastung

**Durchgeführte Maßnahmen:**
1. Yanmar NMEA-2000-Gateway durch Actisense EMU-1 (Engine Monitoring Unit) ersetzt — 400 EUR
2. Firmware-Update auf allen Simrad/B&G-Geräten durchgeführt
3. Zwei oxidierte SimNet-T-Stücke ersetzt — 60 EUR
4. Zusätzlicher 120Ω-Terminator eingesetzt (fehlte am Heckende des Backbones!)
5. Arbeitszeit (Diagnose + Reparatur): 6 Stunden × 85 EUR = 510 EUR

**Gesamtkosten:** ~970 EUR
**Ergebnis:** CAN-Error-Rate <0,1%, keine Datenverluste mehr, Autopilot stabil.

### ANHANG C: Fallstudie — Beneteau Oceanis 51.1 (2021), Garmin-System Neuinstallation

**Ausgangslage:**
- Segelyacht 15,38m, Chartereinsatz Kroatien
- Vorbesitzer hatte Raymarine, Charterfirma wünscht Umstellung auf Garmin (Flotten-Standard)

**Installiertes System:**
1. Garmin GPSMAP 9x3 12" (Steuerstand) — 3.600 EUR
2. Garmin GPSMAP 9x3 9" (Kartentisch) — 2.400 EUR
3. Garmin GMR Fantom 24 (Halbleiter-Radar 24" Radom) — 3.200 EUR
4. Garmin Reactor 40 Autopilot + GHP 20 Hydraulik-Pumpe — 4.800 EUR
5. Garmin gWind Wireless (Funkwindmesser) — 650 EUR
6. Garmin GNX 20 Instrumente (3 Stück: Wind, Depth, Speed) — 900 EUR
7. Garmin GPS 19x NMEA 2000 (externer GPS-Empfänger) — 200 EUR
8. Garmin AIS 800 (Class B+ Transponder) — 700 EUR
9. Icom IC-M423 VHF + NMEA 2000 Gateway — 400 EUR
10. NMEA-2000-Backbone (Maretron Micro-C Komplettset, 15m + 12 Drop Lines) — 500 EUR
11. Navionics+ Mittelmeer Abo — 80 EUR/Jahr
12. Demontage alt + Installation + Kabel + Programmierung: 4.500 EUR (Fachbetrieb, 4 Tage)

**Gesamtkosten:** ~21.930 EUR
**AYDI-Bewertung:** Premium-System für Charter-Einsatz. Garmin gewählt wegen ActiveCaptain-Community (Charterkundenbewertungen), intuitive Bedienung für wechselnde Crews, höchste Displayhelligkeit (Kroatien: intensive Sonne).

### ANHANG D: Fallstudie — Jeanneau Sun Odyssey 440 (2022), AIS-Fehlersuche

**Ausgangslage:**
- Segelyacht 13,39m, Heimathafen Kiel, Einsatz Ostsee
- B&G V60-B (VHF mit integriertem AIS Class B Transponder)
- Problem: Yacht auf Marine Traffic nur sporadisch sichtbar (FB-NAV-005)

**Diagnose:**
1. AIS-Transponder zeigt "TX OK" — Senden scheint zu funktionieren
2. VHF-Reichweite subjektiv normal — Antennensplitter vorhanden (B&G ZG100)
3. SWR-Messung: 4,2:1 auf Kanal 87B (AIS-Frequenz) — deutlich zu hoch!
4. SWR auf Kanal 16: 1,8:1 — akzeptabel
5. Ursache: Antennensplitter ZG100 hat frequenzabhängig schlechte Entkopplung auf AIS-Frequenzen
6. Zusätzlich: Koaxkabel RG-58 über 22m (Masthöhe 19m + Verlegung) — hohe Verluste

**Durchgeführte Maßnahmen:**
1. Antennensplitter B&G ZG100 durch Vesper SP160 ersetzt — 180 EUR
2. Koaxkabel von RG-58 auf Aircell 7 getauscht — 250 EUR (inkl. Stecker)
3. PL-259-Stecker erneuert (alte Stecker zeigten Grünspan) — 30 EUR
4. SWR nach Maßnahme: 1,4:1 auf Kanal 87B — exzellent
5. Arbeitszeit (inkl. Kabel durch den Mast ziehen): 800 EUR

**Gesamtkosten:** ~1.260 EUR
**Ergebnis:** AIS-Sichtbarkeit auf Marine Traffic permanent, Reichweite VHF-Funk ebenfalls deutlich verbessert.

### ANHANG E: Fallstudie — Princess V50 (2018), Radar-Magnetron-Austausch

**Ausgangslage:**
- Motoryacht 15,60m, Heimathafen Mallorca, Einsatz Mittelmeer
- Raymarine Quantum (1. Generation, 2016), Axiom 12 MFD
- Problem: Radarreichweite stark nachgelassen, Ziele erst ab 2 nm sichtbar (früher 12+ nm)

**Diagnose:**
- Quantum 1 = Halbleiter-Radar (FMCW) — hat KEIN Magnetron
- Problem anders als zunächst angenommen: Kein Magnetron-Verschleiß möglich
- Ursache gefunden: Feuchtigkeit im Radom-Gehäuse (Dichtung am Radom-Deckel porös)
- Kondenswasser auf dem Sender-/Empfänger-Modul → Korrosion der Hochfrequenz-Platine
- Sekundärschaden: Lager des Drehgebers (Azimut-Encoder) oxidiert → ungenaue Richtungsbestimmung

**Durchgeführte Maßnahmen:**
1. Radom geöffnet: Deutliche Korrosionsspuren auf HF-Platine sichtbar
2. Reparatur nicht wirtschaftlich (Platine nicht einzeln lieferbar)
3. Upgrade auf Quantum 2 (aktuelle Generation) — 1.800 EUR
4. Radom-Dichtung bei Neumontage sorgfältig mit Siliconfett behandelt
5. Kabelanschluss mit selbstvulkanisierendem Band wasserdicht gemacht
6. Arbeitszeit: 3 Stunden, 350 EUR

**Gesamtkosten:** ~2.150 EUR
**Erkenntnis für AYDI:** Auch Halbleiter-Radar kann durch Feuchtigkeit ausfallen. Dichtungszustand des Radoms ist ein kritischer Inspektionspunkt. In die Fehlerbild-Datenbank aufgenommen.

### ANHANG F: Fallstudie — Dehler 38 SQ (2023), B&G Regattasystem-Optimierung

**Ausgangslage:**
- Segelyacht 11,64m, aktiver Regattasegler (ORC Club, Langstrecke)
- Ab Werk: B&G Zeus S 9", B&G Triton2 Instrumente, B&G NAC-3 Autopilot
- Wunsch: Optimierung der Segelperformance-Daten, präzisere Windwerte

**Installierte Upgrades:**
1. B&G H5000 CPU (Performance-Prozessor, 20Hz Update) — 2.800 EUR
2. B&G WS320 Wireless Windgeber (ersetzt kabelgebundenen Geber) — 850 EUR
3. B&G Precision-9 Kompass (9-Achsen, MEMS + GPS-stabilisiert) — 900 EUR
4. Zweites Triton2 Display (Mast-Position für Trimmer) — 350 EUR
5. Polarkurven-Import (ORC-VPP-Daten) in Zeus S — kostenlos (Software-Feature)
6. Kalibrierung + Seatrial: 2 Tage, 1.200 EUR (Spezialist für B&G H5000)

**Gesamtkosten:** ~6.100 EUR

**Performance-Verbesserung (AYDI-Messung):**
- Windwinkel-Genauigkeit: ±5° → ±1,5° (durch H5000-Kalibrierung + Precision-9)
- VMG-Optimierung: Segler erkennt optimalen Kurs in Echtzeit durch SailSteer
- Autopilot-Wind-Modus: Deutlich präziseres Segeln am Wind (weniger S-Kurse)
- Ergebnis erste Regatta: 12% besser in der bereinigten Zeit (ORC-Rating)

### ANHANG G: Fallstudie — Nordhavn 47 (2012), Furuno-Komplettüberholung für Langfahrt

**Ausgangslage:**
- Motorsegler/Trawler 14,33m, Langfahrtvorbereitung (Atlantik → Karibik → Pazifik)
- Original: Furuno NavNet TZtouch2 (TZT12), DRS4D Radar (Magnetron 4kW), FA-30 AIS
- Alter der Elektronik: 12 Jahre, Magnetron-Betriebsstunden: ~6.500h

**AYDI-Langfahrt-Analyse:**
- Compliance: GMDSS A3-Ausrüstung empfohlen (Atlantiküberquerung)
- Radar: Magnetron nahe Lebensdauerende, Ersatz-Magnetron für unterwegs mitnehmen?
- Kommunikation: UKW allein nicht ausreichend für offenen Atlantik
- Redundanz: Zweites GPS empfohlen, unabhängiger Kompass, Papierseekarten

**Durchgeführte Maßnahmen:**
1. MFD: Upgrade auf Furuno TZtouch3 TZT16F (16") — 6.800 EUR
2. Radar: Furuno DRS4D-NXT (Solid-State, Doppler) — 3.200 EUR
3. AIS: Furuno FA-70 (Class B+ SOTDMA) — 800 EUR
4. VHF: Furuno FM-4800 (DSC + AIS-RX integriert) — 600 EUR
5. SSB-Funk: Icom IC-M803 + AT-141 Tuner + Backstay-Antenne — 3.500 EUR
6. Satellitenkompass: Furuno SC-50 (GPS-Kompass, 0,5° Genauigkeit) — 3.200 EUR
7. EPIRB: Ocean Signal rescueME EPIRB1 — 400 EUR
8. PLB: Ocean Signal rescueME PLB1 × 2 (für Skipper + Crew) — 500 EUR
9. Iridium GO! exec (Satellitentelefon + Daten für Wetterbriefing) — 1.200 EUR + Abo
10. Starlink Maritime (Flachantenne + Router) — 2.500 EUR + 250 EUR/Monat
11. Papierseekarten (Admiralty) für Atlantik + Karibik — 400 EUR
12. NMEA-2000-Backbone komplett erneuert (Maretron) — 600 EUR
13. Installation + Konfiguration: 5 Tage Fachbetrieb — 5.000 EUR

**Gesamtkosten:** ~28.700 EUR (+ laufende Kosten Starlink + Iridium ~350 EUR/Monat)
**AYDI-Bewertung:** Umfassendes Langfahrt-System mit voller GMDSS-A3-Fähigkeit, Redundanz bei kritischen Systemen, Satellitenkommunikation für Wetter und Notfall. Furuno-Radar und SC-50-Kompass als Premiumwahl für Offshore gerechtfertigt.

### ANHANG H: Fallstudie — Azimut S6 (2023), Superyacht-Navigation 18m+

**Ausgangslage:**
- Motoryacht 18,27m, Einsatz Mittelmeer + Kanalinseln
- Neuinstallation ab Werk mit Garmin-System (OEM-Vereinbarung Azimut/Garmin)
- Besonderheit: Dual-Steuerstand (Fly Bridge + Lower Helm), 3 MFDs

**Installiertes System:**
1. Garmin GPSMAP 9019 (19") × 1 (Fly Bridge Hauptdisplay) — 9.000 EUR
2. Garmin GPSMAP 9x3 16" × 1 (Lower Helm) — 6.000 EUR
3. Garmin GPSMAP 9x3 12" × 1 (Fly Bridge Nebendisplay) — 3.600 EUR
4. Garmin GMR Fantom 56 Open Array (6ft, 50W Solid State, 72nm Reichweite) — 12.000 EUR
5. Garmin Reactor 40 Autopilot + GHP 30 Hydraulik (Dual-Station) — 8.000 EUR
6. Garmin AIS 800 (Class B+) — 700 EUR
7. Garmin VHF 315i (mit integriertem AIS-RX) × 2 (je 1 pro Steuerstand) — 1.400 EUR
8. Garmin MSC 10 Marine Satellite Compass — 4.000 EUR
9. Garmin GCV 20 Sonar Black Box + GT34UHD-TM Geber — 2.500 EUR
10. Garmin GRID 20 Remote Input Device (Lower Helm) — 500 EUR
11. Garmin GMS 10 Network Port Expander × 2 — 600 EUR
12. Garmin Fusion Apollo RA770 (Entertainment, NMEA 2000) — 800 EUR
13. FLIR M232 Wärmebildkamera — 5.000 EUR
14. NMEA-2000-Netzwerk (komplett, inkl. Motor-Interface Volvo Penta IPS) — 1.500 EUR
15. Installation + Programmierung + Seatrial: 8.000 EUR

**Gesamtkosten:** ~63.600 EUR
**AYDI-Bewertung:** Vollintegriertes Garmin-Ökosystem mit allen verfügbaren Funktionen. Garmin Marine Network verbindet alle drei MFDs + Radar + Sonar über Ethernet. NMEA 2000 für Sensoren, Motor (Volvo Penta IPS), Autopilot. FLIR-Wärmebildkamera als Sicherheitsfeature für Nachtfahrt.

---

## ANHANG I–R — Pydantic v2 Modelle {#anhang-i-r}

### ANHANG I: Basis-Enums und gemeinsame Typen

```python
"""
AYDI Navigation & Electronics — Pydantic v2 Models
Wissensdatei 23.01: Navigation und Elektronik Grundlagen

German domain content, English code.
Pydantic v2: model_config = {"from_attributes": True} — NEVER class Config.
"""

from __future__ import annotations

from datetime import date, datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, field_validator


# --- Confidence Levels ---


class ConfidenceLevel(str, Enum):
    """Confidence level for AYDI analysis results."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


# --- Severity Levels ---


class SeverityLevel(str, Enum):
    """Severity level for issues and findings."""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    MINOR = "minor"
    INFO = "info"


# --- Navigation System Enums ---


class GnssSystem(str, Enum):
    """GNSS satellite systems."""
    GPS = "gps"
    GLONASS = "glonass"
    GALILEO = "galileo"
    BEIDOU = "beidou"


class NmeaBusType(str, Enum):
    """NMEA data bus types."""
    NMEA_0183 = "nmea_0183"
    NMEA_2000 = "nmea_2000"
    SEATALKNG = "seatalkng"
    SIMNET = "simnet"
    ETHERNET = "ethernet"
    WIFI = "wifi"
    BLUETOOTH = "bluetooth"


class RadarType(str, Enum):
    """Radar technology types."""
    MAGNETRON_PULSE = "magnetron_pulse"
    SOLID_STATE_FMCW = "solid_state_fmcw"
    SOLID_STATE_PULSE_COMPRESSION = "solid_state_pulse_compression"
    HYBRID = "hybrid"


class RadarAntennaType(str, Enum):
    """Radar antenna form factor."""
    RADOM_18 = "radom_18_inch"
    RADOM_24 = "radom_24_inch"
    OPEN_ARRAY_2FT = "open_array_2ft"
    OPEN_ARRAY_3FT = "open_array_3ft"
    OPEN_ARRAY_4FT = "open_array_4ft"
    OPEN_ARRAY_6FT = "open_array_6ft"


class AisClass(str, Enum):
    """AIS device class."""
    RECEIVER_ONLY = "receiver_only"
    CLASS_B_CS = "class_b_cs"
    CLASS_B_PLUS_SO = "class_b_plus_so"
    CLASS_A = "class_a"


class VhfType(str, Enum):
    """VHF radio type."""
    HANDHELD = "handheld"
    FIXED_STANDARD = "fixed_standard"
    FIXED_PREMIUM = "fixed_premium"
    FIXED_AIS_INTEGRATED = "fixed_ais_integrated"
    SSB_HF = "ssb_hf"


class AutopilotDriveType(str, Enum):
    """Autopilot drive mechanism."""
    TILLER = "tiller"
    LINEAR_ELECTRIC = "linear_electric"
    HYDRAULIC = "hydraulic"
    MECHANICAL_WHEEL = "mechanical_wheel"


class AutopilotMode(str, Enum):
    """Autopilot steering modes."""
    STANDBY = "standby"
    AUTO_COMPASS = "auto_compass"
    WIND = "wind"
    TRACK_NAV = "track_nav"
    NO_DRIFT = "no_drift"


class MfdManufacturer(str, Enum):
    """MFD manufacturer brands."""
    RAYMARINE = "raymarine"
    GARMIN = "garmin"
    SIMRAD = "simrad"
    BG = "b_and_g"
    FURUNO = "furuno"
    HUMMINBIRD = "humminbird"
    LOWRANCE = "lowrance"


class EchosounderFrequency(str, Enum):
    """Echosounder operating frequency band."""
    LOW_50KHZ = "50khz"
    MEDIUM_83KHZ = "83khz"
    HIGH_200KHZ = "200khz"
    CHIRP_LOW = "chirp_low"
    CHIRP_MEDIUM = "chirp_medium"
    CHIRP_HIGH = "chirp_high"
    SIDESCAN_455KHZ = "sidescan_455khz"
    SIDESCAN_800KHZ = "sidescan_800khz"
    FORWARD_1MHZ = "forward_1mhz"


class TransducerMounting(str, Enum):
    """Echosounder transducer mounting type."""
    TRANSOM = "transom"
    THRU_HULL = "thru_hull"
    IN_HULL = "in_hull"
    RETRACTABLE = "retractable"


class SbasSystem(str, Enum):
    """SBAS correction systems."""
    EGNOS = "egnos"
    WAAS = "waas"
    MSAS = "msas"
    GALILEO_HAS = "galileo_has"
    RTK_NTRIP = "rtk_ntrip"


class FailurePatternCode(str, Enum):
    """Failure pattern codes from the Fehlerbild-Atlas."""
    FB_NAV_001 = "fb_nav_001_gps_totalausfall"
    FB_NAV_002 = "fb_nav_002_gps_abweichung"
    FB_NAV_003 = "fb_nav_003_nmea2000_busfehler"
    FB_NAV_004 = "fb_nav_004_radar_ausfall"
    FB_NAV_005 = "fb_nav_005_ais_unsichtbar"
    FB_NAV_006 = "fb_nav_006_autopilot_gieren"
    FB_NAV_007 = "fb_nav_007_mfd_touchscreen"
    FB_NAV_008 = "fb_nav_008_vhf_reichweite"
    FB_NAV_009 = "fb_nav_009_echolot_fehler"
    FB_NAV_010 = "fb_nav_010_windmesser_fehler"
    FB_NAV_011 = "fb_nav_011_mfd_software_absturz"
    FB_NAV_012 = "fb_nav_012_galvanische_korrosion"


class CeDesignCategory(str, Enum):
    """CE design category per EU Recreational Craft Directive."""
    A_OCEAN = "a_ocean"
    B_OFFSHORE = "b_offshore"
    C_INSHORE = "c_inshore"
    D_SHELTERED = "d_sheltered"


class RadioLicenseType(str, Enum):
    """Radio operator license types (Germany)."""
    SRC = "src"
    LRC = "lrc"
    UBI = "ubi"
```

### ANHANG J: GPS/GNSS-Empfänger-Modell

```python
# --- ANHANG J: GNSS Receiver Model ---


class GnssReceiverSpec(BaseModel):
    """Specification of a GNSS receiver for marine use."""
    model_config = {"from_attributes": True}

    manufacturer: MfdManufacturer = Field(
        ..., description="Hersteller des GNSS-Empfaengers"
    )
    model_name: str = Field(
        ..., min_length=1, max_length=100,
        description="Modellbezeichnung des GNSS-Empfaengers"
    )
    supported_systems: list[GnssSystem] = Field(
        ..., min_length=1,
        description="Unterstuetzte GNSS-Systeme (GPS, GLONASS, Galileo, BeiDou)"
    )
    channels: int = Field(
        ..., ge=12, le=400,
        description="Anzahl paralleler Empfangskanaele"
    )
    sbas_support: list[SbasSystem] = Field(
        default_factory=list,
        description="Unterstuetzte SBAS-Korrektursysteme"
    )
    update_rate_hz: float = Field(
        default=1.0, ge=0.1, le=50.0,
        description="Positionsaktualisierungsrate in Hz"
    )
    accuracy_m_95: float = Field(
        ..., ge=0.01, le=100.0,
        description="Positionsgenauigkeit in Metern (95% CEP)"
    )
    ttff_cold_s: float = Field(
        ..., ge=1.0, le=300.0,
        description="Time-To-First-Fix Cold Start in Sekunden"
    )
    ttff_warm_s: float = Field(
        ..., ge=0.5, le=60.0,
        description="Time-To-First-Fix Warm Start in Sekunden"
    )
    dual_frequency: bool = Field(
        default=False,
        description="Dual-Frequency-Empfaenger (L1+L5) fuer verbesserte Genauigkeit"
    )
    heading_capable: bool = Field(
        default=False,
        description="GPS-Kompass-Faehigkeit (Dual-Antenne)"
    )
    heading_accuracy_deg: Optional[float] = Field(
        default=None, ge=0.01, le=10.0,
        description="Heading-Genauigkeit in Grad (bei Dual-Antenne)"
    )
    nmea_interfaces: list[NmeaBusType] = Field(
        ..., min_length=1,
        description="Verfuegbare Datenschnittstellen"
    )
    power_consumption_w: float = Field(
        ..., ge=0.1, le=50.0,
        description="Leistungsaufnahme in Watt"
    )
    waterproof_rating: str = Field(
        default="IPX7",
        description="Wasserdichtigkeitsklasse (z.B. IPX6, IPX7, IPX8)"
    )
    price_eur: float = Field(
        ..., ge=0.0,
        description="Listenpreis in EUR"
    )
    confidence: ConfidenceLevel = Field(
        default=ConfidenceLevel.MEASURED,
        description="Konfidenz der Spezifikationsdaten"
    )
```

### ANHANG K: Radar-System-Modell

```python
# --- ANHANG K: Radar System Model ---


class RadarSystemSpec(BaseModel):
    """Specification of a marine radar system."""
    model_config = {"from_attributes": True}

    manufacturer: MfdManufacturer = Field(
        ..., description="Hersteller des Radarsystems"
    )
    model_name: str = Field(
        ..., min_length=1, max_length=100,
        description="Modellbezeichnung des Radars"
    )
    radar_type: RadarType = Field(
        ..., description="Radar-Technologietyp (Magnetron/Halbleiter/Hybrid)"
    )
    antenna_type: RadarAntennaType = Field(
        ..., description="Antennentyp (Radom/Open Array)"
    )
    peak_power_w: float = Field(
        ..., ge=1.0, le=30000.0,
        description="Spitzen-Sendeleistung in Watt"
    )
    frequency_ghz: float = Field(
        default=9.41, ge=9.3, le=9.5,
        description="Sendefrequenz in GHz (X-Band)"
    )
    beam_width_h_deg: float = Field(
        ..., ge=0.5, le=10.0,
        description="Horizontale Strahlbreite in Grad"
    )
    beam_width_v_deg: float = Field(
        ..., ge=10.0, le=40.0,
        description="Vertikale Strahlbreite in Grad"
    )
    max_range_nm: float = Field(
        ..., ge=4.0, le=120.0,
        description="Maximale Reichweite in Seemeilen"
    )
    min_range_m: float = Field(
        ..., ge=1.0, le=100.0,
        description="Minimale Reichweite in Metern"
    )
    range_resolution_m: float = Field(
        ..., ge=0.1, le=50.0,
        description="Entfernungsaufloesung in Metern"
    )
    rotation_speed_rpm: float = Field(
        ..., ge=12.0, le=48.0,
        description="Drehzahl der Antenne in Umdrehungen/Minute"
    )
    warmup_time_s: float = Field(
        ..., ge=0.0, le=180.0,
        description="Aufwaermzeit in Sekunden (0 bei Halbleiter)"
    )
    doppler_capable: bool = Field(
        default=False,
        description="Doppler-Geschwindigkeitserkennung (VelocityTrack etc.)"
    )
    marpa_targets: int = Field(
        default=10, ge=0, le=200,
        description="Maximale Anzahl MARPA/ARPA-Ziele"
    )
    dual_range: bool = Field(
        default=False,
        description="Gleichzeitige Nah- und Fernbereichsdarstellung"
    )
    power_consumption_w: float = Field(
        ..., ge=5.0, le=500.0,
        description="Leistungsaufnahme im Betrieb in Watt"
    )
    scanner_weight_kg: float = Field(
        ..., ge=1.0, le=50.0,
        description="Gewicht des Scanners in Kilogramm"
    )
    magnetron_life_hours: Optional[int] = Field(
        default=None, ge=0, le=20000,
        description="Erwartete Magnetron-Lebensdauer in Stunden (None bei Halbleiter)"
    )
    connection_type: NmeaBusType = Field(
        default=NmeaBusType.ETHERNET,
        description="Verbindungstyp zum MFD"
    )
    compatible_mfds: list[str] = Field(
        default_factory=list,
        description="Kompatible MFD-Modelle"
    )
    price_eur: float = Field(
        ..., ge=0.0,
        description="Listenpreis in EUR (nur Scanner)"
    )
    confidence: ConfidenceLevel = Field(
        default=ConfidenceLevel.MEASURED,
        description="Konfidenz der Spezifikationsdaten"
    )
```

### ANHANG L: AIS-Transponder-Modell

```python
# --- ANHANG L: AIS Transponder Model ---


class AisTransponderSpec(BaseModel):
    """Specification of an AIS transponder."""
    model_config = {"from_attributes": True}

    manufacturer: str = Field(
        ..., min_length=1, max_length=100,
        description="Hersteller des AIS-Transponders"
    )
    model_name: str = Field(
        ..., min_length=1, max_length=100,
        description="Modellbezeichnung"
    )
    ais_class: AisClass = Field(
        ..., description="AIS-Geraeteklasse"
    )
    tx_power_w: float = Field(
        ..., ge=0.0, le=15.0,
        description="Sendeleistung in Watt (0 bei Empfaenger)"
    )
    tx_interval_min_s: Optional[float] = Field(
        default=None, ge=0.0, le=300.0,
        description="Minimales Sendeintervall in Sekunden"
    )
    tx_interval_max_s: Optional[float] = Field(
        default=None, ge=0.0, le=300.0,
        description="Maximales Sendeintervall in Sekunden"
    )
    tdma_type: Optional[str] = Field(
        default=None,
        description="TDMA-Zugriffsverfahren (CSTDMA/SOTDMA)"
    )
    integrated_gps: bool = Field(
        default=False,
        description="Integrierter GPS-Empfaenger"
    )
    integrated_antenna_splitter: bool = Field(
        default=False,
        description="Integrierter VHF-Antennensplitter"
    )
    nmea_interfaces: list[NmeaBusType] = Field(
        ..., min_length=1,
        description="Verfuegbare Datenschnittstellen"
    )
    silent_mode: bool = Field(
        default=True,
        description="Silent-Mode (Senden deaktivierbar) verfuegbar"
    )
    target_capacity: int = Field(
        default=500, ge=0, le=5000,
        description="Maximale Anzahl gleichzeitig darstellbarer Ziele"
    )
    power_consumption_w: float = Field(
        ..., ge=0.0, le=25.0,
        description="Leistungsaufnahme in Watt"
    )
    waterproof_rating: str = Field(
        default="IPX7",
        description="Wasserdichtigkeitsklasse"
    )
    price_eur: float = Field(
        ..., ge=0.0,
        description="Listenpreis in EUR"
    )
    confidence: ConfidenceLevel = Field(
        default=ConfidenceLevel.MEASURED,
        description="Konfidenz der Spezifikationsdaten"
    )
```

### ANHANG M: UKW-Funkgerät-Modell

```python
# --- ANHANG M: VHF Radio Model ---


class VhfRadioSpec(BaseModel):
    """Specification of a marine VHF radio."""
    model_config = {"from_attributes": True}

    manufacturer: str = Field(
        ..., min_length=1, max_length=100,
        description="Hersteller des Funkgeraets"
    )
    model_name: str = Field(
        ..., min_length=1, max_length=100,
        description="Modellbezeichnung"
    )
    vhf_type: VhfType = Field(
        ..., description="Funkgeraetetyp"
    )
    tx_power_max_w: float = Field(
        ..., ge=0.5, le=150.0,
        description="Maximale Sendeleistung in Watt"
    )
    tx_power_levels: list[float] = Field(
        ..., min_length=1,
        description="Verfuegbare Sendeleistungsstufen in Watt"
    )
    dsc_class: Optional[str] = Field(
        default=None,
        description="DSC-Klasse (D, A, oder None)"
    )
    integrated_gps: bool = Field(
        default=False,
        description="Integrierter GPS-Empfaenger fuer DSC-Position"
    )
    integrated_ais_rx: bool = Field(
        default=False,
        description="Integrierter AIS-Empfaenger"
    )
    integrated_ais_tx: bool = Field(
        default=False,
        description="Integrierter AIS-Transponder"
    )
    ais_class_if_tx: Optional[AisClass] = Field(
        default=None,
        description="AIS-Klasse bei integriertem Transponder"
    )
    channels: int = Field(
        default=88, ge=1, le=200,
        description="Anzahl verfuegbarer Kanaele"
    )
    dual_watch: bool = Field(
        default=True,
        description="Dual-Watch-Funktion (Kanal 16 + Arbeitskanal)"
    )
    tri_watch: bool = Field(
        default=False,
        description="Tri-Watch-Funktion (Kanal 16 + 2 weitere)"
    )
    nmea_interfaces: list[NmeaBusType] = Field(
        default_factory=list,
        description="Verfuegbare Datenschnittstellen"
    )
    display_type: str = Field(
        default="LCD",
        description="Display-Typ (LCD, OLED, Matrix, None)"
    )
    waterproof_rating: str = Field(
        ..., description="Wasserdichtigkeitsklasse (IPX7, IPX8, etc.)"
    )
    float_capable: bool = Field(
        default=False,
        description="Schwimmfaehig (nur Handgeraete)"
    )
    battery_type: Optional[str] = Field(
        default=None,
        description="Batterietyp bei Handgeraeten (Li-Ion, AA, etc.)"
    )
    battery_life_hours: Optional[float] = Field(
        default=None, ge=0.0, le=72.0,
        description="Batterielaufzeit in Stunden (TX:RX:Standby = 5:5:90)"
    )
    power_consumption_w: float = Field(
        ..., ge=0.1, le=50.0,
        description="Leistungsaufnahme in Watt (max. TX)"
    )
    price_eur: float = Field(
        ..., ge=0.0,
        description="Listenpreis in EUR"
    )
    confidence: ConfidenceLevel = Field(
        default=ConfidenceLevel.MEASURED,
        description="Konfidenz der Spezifikationsdaten"
    )


class AntennaSpec(BaseModel):
    """Specification of a marine VHF or GPS antenna."""
    model_config = {"from_attributes": True}

    antenna_type: str = Field(
        ..., description="Antennentyp (vhf_whip, vhf_colinear, gps_patch, gps_helix, radar_radom, radar_open)"
    )
    manufacturer: str = Field(
        ..., description="Hersteller"
    )
    model_name: str = Field(
        ..., description="Modellbezeichnung"
    )
    frequency_range_mhz: tuple[float, float] = Field(
        ..., description="Frequenzbereich in MHz (min, max)"
    )
    gain_dbi: float = Field(
        ..., ge=-5.0, le=20.0,
        description="Antennengewinn in dBi"
    )
    length_m: float = Field(
        ..., ge=0.05, le=3.0,
        description="Laenge der Antenne in Metern"
    )
    connector_type: str = Field(
        ..., description="Steckertyp (PL-259, BNC, N, TNC, SMA, proprietary)"
    )
    cable_length_m: Optional[float] = Field(
        default=None, ge=0.0, le=50.0,
        description="Mitgeliefertes Kabel in Metern"
    )
    cable_type: Optional[str] = Field(
        default=None,
        description="Kabeltyp (RG-58, RG-213, LMR-400, Aircell 7, etc.)"
    )
    waterproof_rating: str = Field(
        default="IPX6",
        description="Wasserdichtigkeitsklasse"
    )
    price_eur: float = Field(
        ..., ge=0.0,
        description="Listenpreis in EUR"
    )
    confidence: ConfidenceLevel = Field(
        default=ConfidenceLevel.MEASURED,
        description="Konfidenz der Spezifikationsdaten"
    )
```

### ANHANG N: Autopilot-System-Modell

```python
# --- ANHANG N: Autopilot System Model ---


class AutopilotSystemSpec(BaseModel):
    """Specification of a marine autopilot system."""
    model_config = {"from_attributes": True}

    manufacturer: MfdManufacturer = Field(
        ..., description="Hersteller des Autopiloten"
    )
    model_name: str = Field(
        ..., min_length=1, max_length=100,
        description="Modellbezeichnung des Autopilot-Systems"
    )
    drive_type: AutopilotDriveType = Field(
        ..., description="Antriebstyp"
    )
    supported_modes: list[AutopilotMode] = Field(
        ..., min_length=1,
        description="Unterstuetzte Steuermodi"
    )
    max_displacement_kg: float = Field(
        ..., ge=500.0, le=500000.0,
        description="Maximale Verdrängung des Bootes in Kilogramm"
    )
    max_rudder_torque_nm: Optional[float] = Field(
        default=None, ge=0.0, le=50000.0,
        description="Maximales Ruderdrehmoment in Nm"
    )
    drive_power_w: float = Field(
        ..., ge=10.0, le=5000.0,
        description="Leistungsaufnahme des Antriebs in Watt (max.)"
    )
    hard_over_time_s: float = Field(
        ..., ge=1.0, le=30.0,
        description="Zeit Backbord-Anschlag zu Steuerbord-Anschlag in Sekunden"
    )
    heading_sensor_included: bool = Field(
        default=False,
        description="Heading-Sensor im Lieferumfang enthalten"
    )
    heading_sensor_type: str = Field(
        default="fluxgate",
        description="Kompasstyp (fluxgate, mems_9axis, gps_compass)"
    )
    rudder_feedback_included: bool = Field(
        default=False,
        description="Ruderfeedback-Sensor im Lieferumfang"
    )
    wind_mode_available: bool = Field(
        default=False,
        description="Wind-Steuermodus verfuegbar (fuer Segelboote)"
    )
    auto_tack: bool = Field(
        default=False,
        description="Automatische Wende (Tack) verfuegbar"
    )
    auto_gybe: bool = Field(
        default=False,
        description="Automatische Halse (Gybe) verfuegbar"
    )
    nmea_interfaces: list[NmeaBusType] = Field(
        ..., min_length=1,
        description="Verfuegbare Datenschnittstellen"
    )
    compatible_mfds: list[str] = Field(
        default_factory=list,
        description="Kompatible MFD-Modelle fuer Fernsteuerung"
    )
    suitable_boat_types: list[str] = Field(
        default_factory=list,
        description="Geeignete Bootstypen (sailboat, motorboat, trawler)"
    )
    price_eur: float = Field(
        ..., ge=0.0,
        description="Listenpreis in EUR (Komplettsystem)"
    )
    confidence: ConfidenceLevel = Field(
        default=ConfidenceLevel.MEASURED,
        description="Konfidenz der Spezifikationsdaten"
    )
```

### ANHANG O: NMEA-2000-Netzwerk-Modell

```python
# --- ANHANG O: NMEA 2000 Network Model ---


class Nmea2000Device(BaseModel):
    """A device connected to the NMEA 2000 network."""
    model_config = {"from_attributes": True}

    device_name: str = Field(
        ..., description="Geraetename (z.B. 'Garmin GPS 19x')"
    )
    manufacturer: str = Field(
        ..., description="Hersteller"
    )
    device_function: str = Field(
        ..., description="Funktion (gps, wind, depth, mfd, autopilot, ais, engine, tank, battery)"
    )
    nmea2000_address: Optional[int] = Field(
        default=None, ge=0, le=252,
        description="NMEA-2000-Netzwerkadresse (0-252)"
    )
    len_value: float = Field(
        ..., ge=0.1, le=10.0,
        description="Load Equivalence Number (1 LEN = 50mA)"
    )
    transmitted_pgns: list[int] = Field(
        default_factory=list,
        description="Liste der gesendeten PGN-Nummern"
    )
    received_pgns: list[int] = Field(
        default_factory=list,
        description="Liste der empfangenen PGN-Nummern"
    )
    firmware_version: Optional[str] = Field(
        default=None,
        description="Aktuelle Firmware-Version"
    )
    drop_line_length_m: float = Field(
        ..., ge=0.1, le=6.0,
        description="Laenge der Drop-Line in Metern"
    )
    status: str = Field(
        default="operational",
        description="Betriebsstatus (operational, error, offline)"
    )


class Nmea2000NetworkSpec(BaseModel):
    """Specification and status of a NMEA 2000 network."""
    model_config = {"from_attributes": True}

    yacht_id: str = Field(
        ..., description="Eindeutige Yacht-ID im AYDI-System"
    )
    cable_type: str = Field(
        default="micro_c",
        description="Kabeltyp (micro_c, mid_size)"
    )
    backbone_length_m: float = Field(
        ..., ge=1.0, le=250.0,
        description="Gesamtlaenge des Backbones in Metern"
    )
    backbone_max_allowed_m: float = Field(
        default=100.0, ge=50.0, le=250.0,
        description="Maximale erlaubte Backbone-Laenge in Metern"
    )
    terminator_count: int = Field(
        ..., ge=0, le=4,
        description="Anzahl installierter Terminierungswiderstaende (Soll: 2)"
    )
    measured_resistance_ohm: Optional[float] = Field(
        default=None, ge=0.0, le=1000.0,
        description="Gemessener Widerstand CAN-H zu CAN-L in Ohm (Soll: 60)"
    )
    bus_voltage_v: Optional[float] = Field(
        default=None, ge=0.0, le=20.0,
        description="Gemessene Bus-Spannung in Volt (Soll: 9-16)"
    )
    total_len: float = Field(
        ..., ge=0.0, le=100.0,
        description="Gesamt-LEN aller angeschlossenen Geraete"
    )
    max_len_per_supply: float = Field(
        default=30.0,
        description="Maximale LEN pro Netzteil"
    )
    power_supply_count: int = Field(
        ..., ge=1, le=5,
        description="Anzahl Netzteile am Backbone"
    )
    devices: list[Nmea2000Device] = Field(
        default_factory=list,
        description="Liste aller angeschlossenen Geraete"
    )
    can_error_rate_percent: Optional[float] = Field(
        default=None, ge=0.0, le=100.0,
        description="CAN-Error-Frame-Rate in Prozent (Soll: <0.5)"
    )
    detected_issues: list[str] = Field(
        default_factory=list,
        description="Erkannte Netzwerkprobleme"
    )
    overall_health: str = Field(
        default="unknown",
        description="Gesamtzustand (excellent, good, degraded, critical, unknown)"
    )
    confidence: ConfidenceLevel = Field(
        default=ConfidenceLevel.ESTIMATED,
        description="Konfidenz der Netzwerkbewertung"
    )

    @field_validator("terminator_count")
    @classmethod
    def check_terminator_count(cls, v: int) -> int:
        if v != 2:
            pass  # Issue will be flagged in detected_issues
        return v
```

### ANHANG P: Navigations-Gesamtsystem-Modell

```python
# --- ANHANG P: Complete Navigation System Model ---


class NavigationSystemInventory(BaseModel):
    """Complete inventory of navigation electronics on a yacht."""
    model_config = {"from_attributes": True}

    yacht_id: str = Field(
        ..., description="Eindeutige Yacht-ID im AYDI-System"
    )
    yacht_name: Optional[str] = Field(
        default=None, description="Name der Yacht"
    )
    yacht_loa_m: float = Field(
        ..., ge=2.5, le=100.0,
        description="Laenge ueber Alles in Metern"
    )
    yacht_type: str = Field(
        ..., description="Yachttyp (sailboat, motorboat, trawler, catamaran, superyacht)"
    )
    ce_category: CeDesignCategory = Field(
        ..., description="CE-Entwurfskategorie"
    )
    primary_cruising_area: str = Field(
        ..., description="Hauptfahrtgebiet (ostsee, nordsee, mittelmeer, atlantik, global)"
    )
    mfd_manufacturer: MfdManufacturer = Field(
        ..., description="Primaerer MFD-Hersteller (Oekosystem-Entscheidung)"
    )
    mfd_count: int = Field(
        ..., ge=1, le=10,
        description="Anzahl installierter MFDs"
    )
    mfd_models: list[str] = Field(
        default_factory=list,
        description="Liste der MFD-Modellbezeichnungen"
    )
    radar_installed: bool = Field(
        default=False,
        description="Radar installiert"
    )
    radar_model: Optional[str] = Field(
        default=None,
        description="Radar-Modellbezeichnung"
    )
    radar_type: Optional[RadarType] = Field(
        default=None,
        description="Radar-Technologietyp"
    )
    ais_installed: bool = Field(
        default=False,
        description="AIS installiert"
    )
    ais_class: Optional[AisClass] = Field(
        default=None,
        description="AIS-Geraeteklasse"
    )
    ais_model: Optional[str] = Field(
        default=None,
        description="AIS-Modellbezeichnung"
    )
    vhf_model: Optional[str] = Field(
        default=None,
        description="UKW-Funk-Modellbezeichnung"
    )
    vhf_dsc_capable: bool = Field(
        default=False,
        description="UKW-Funk mit DSC-Faehigkeit"
    )
    vhf_gps_connected: bool = Field(
        default=False,
        description="GPS-Position am UKW-Funk angebunden (fuer DSC-Notruf)"
    )
    ssb_installed: bool = Field(
        default=False,
        description="GW/KW-Seefunkgeraet installiert"
    )
    satcom_installed: bool = Field(
        default=False,
        description="Satellitenkommunikation installiert (Iridium, Starlink, etc.)"
    )
    autopilot_installed: bool = Field(
        default=False,
        description="Autopilot installiert"
    )
    autopilot_model: Optional[str] = Field(
        default=None,
        description="Autopilot-Modellbezeichnung"
    )
    autopilot_drive: Optional[AutopilotDriveType] = Field(
        default=None,
        description="Autopilot-Antriebstyp"
    )
    heading_sensor_type: Optional[str] = Field(
        default=None,
        description="Kompasstyp (fluxgate, mems, gps_compass)"
    )
    wind_sensor_model: Optional[str] = Field(
        default=None,
        description="Windgeber-Modell"
    )
    depth_sensor_model: Optional[str] = Field(
        default=None,
        description="Echolot-Geber-Modell"
    )
    speed_sensor_model: Optional[str] = Field(
        default=None,
        description="Geschwindigkeitsgeber-Modell (Paddlewheel, Ultraschall)"
    )
    nmea_2000_installed: bool = Field(
        default=False,
        description="NMEA-2000-Netzwerk installiert"
    )
    nmea_0183_devices: int = Field(
        default=0, ge=0, le=20,
        description="Anzahl Geraete mit NMEA-0183-Anschluss"
    )
    epirb_installed: bool = Field(
        default=False,
        description="EPIRB installiert"
    )
    plb_count: int = Field(
        default=0, ge=0, le=10,
        description="Anzahl PLBs an Bord"
    )
    radar_reflector_installed: bool = Field(
        default=False,
        description="Radarreflektor installiert"
    )
    chart_subscription: Optional[str] = Field(
        default=None,
        description="Aktives Kartenabonnement (navionics_plus, c_map_discover, etc.)"
    )
    total_system_age_years: float = Field(
        ..., ge=0.0, le=40.0,
        description="Alter des aeltesten Hauptgeraets in Jahren"
    )
    total_estimated_value_eur: float = Field(
        ..., ge=0.0,
        description="Geschaetzter Gesamtwert der Navigationselektronik in EUR"
    )
    last_firmware_update: Optional[date] = Field(
        default=None,
        description="Datum des letzten Firmware-Updates (irgendeines Geraets)"
    )
    radio_license_type: Optional[RadioLicenseType] = Field(
        default=None,
        description="Vorhandenes Funkzeugnis des Skippers"
    )
    mmsi: Optional[str] = Field(
        default=None, pattern=r"^\d{9}$",
        description="MMSI-Nummer (9 Ziffern)"
    )
    confidence: ConfidenceLevel = Field(
        default=ConfidenceLevel.ESTIMATED,
        description="Konfidenz der Bestandsaufnahme"
    )
```

### ANHANG Q: Fehlerbild-Analyse-Modell

```python
# --- ANHANG Q: Failure Analysis Model ---


class NavigationFailureAnalysis(BaseModel):
    """Analysis of a detected navigation electronics failure."""
    model_config = {"from_attributes": True}

    yacht_id: str = Field(
        ..., description="Eindeutige Yacht-ID im AYDI-System"
    )
    analysis_date: datetime = Field(
        ..., description="Zeitpunkt der Analyse"
    )
    failure_code: FailurePatternCode = Field(
        ..., description="Fehlerbild-Code aus dem Atlas"
    )
    failure_title_de: str = Field(
        ..., description="Fehlertitel auf Deutsch"
    )
    severity: SeverityLevel = Field(
        ..., description="Schweregrad des Fehlers"
    )
    affected_systems: list[str] = Field(
        ..., min_length=1,
        description="Betroffene Systeme (gps, radar, ais, autopilot, vhf, mfd, nmea2000, echosounder, wind)"
    )
    symptoms_de: list[str] = Field(
        ..., min_length=1,
        description="Beobachtete Symptome auf Deutsch"
    )
    probable_causes_de: list[str] = Field(
        ..., min_length=1,
        description="Wahrscheinliche Ursachen auf Deutsch (sortiert nach Wahrscheinlichkeit)"
    )
    cause_probabilities: list[float] = Field(
        default_factory=list,
        description="Wahrscheinlichkeiten der Ursachen (0.0-1.0, gleiche Reihenfolge)"
    )
    diagnostic_steps_de: list[str] = Field(
        ..., min_length=1,
        description="Empfohlene Diagnoseschritte auf Deutsch"
    )
    immediate_actions_de: list[str] = Field(
        default_factory=list,
        description="Sofortmassnahmen auf Deutsch"
    )
    repair_cost_min_eur: float = Field(
        ..., ge=0.0,
        description="Geschaetzte minimale Reparaturkosten in EUR"
    )
    repair_cost_max_eur: float = Field(
        ..., ge=0.0,
        description="Geschaetzte maximale Reparaturkosten in EUR"
    )
    estimated_repair_time_hours: float = Field(
        ..., ge=0.0, le=100.0,
        description="Geschaetzte Reparaturzeit in Stunden"
    )
    professional_service_required: bool = Field(
        default=False,
        description="Fachservice erforderlich (nicht DIY)"
    )
    safety_relevant: bool = Field(
        default=False,
        description="Sicherheitsrelevant (betrifft Seenotrettung/Kollisionsvermeidung)"
    )
    recommended_spares_de: list[str] = Field(
        default_factory=list,
        description="Empfohlene Ersatzteile auf Deutsch"
    )
    prevention_tips_de: list[str] = Field(
        default_factory=list,
        description="Praeventionshinweise auf Deutsch"
    )
    related_failure_codes: list[FailurePatternCode] = Field(
        default_factory=list,
        description="Verwandte Fehlerbilder (Folgefehler oder gemeinsame Ursache)"
    )
    confidence: ConfidenceLevel = Field(
        default=ConfidenceLevel.ESTIMATED,
        description="Konfidenz der Fehleranalyse"
    )

    @field_validator("repair_cost_max_eur")
    @classmethod
    def max_cost_gte_min_cost(cls, v: float, info) -> float:
        min_cost = info.data.get("repair_cost_min_eur", 0.0)
        if min_cost is not None and v < min_cost:
            raise ValueError(
                "repair_cost_max_eur must be >= repair_cost_min_eur"
            )
        return v
```

### ANHANG R: Service-Empfehlung-Modell

```python
# --- ANHANG R: Navigation Service Recommendation ---


class NavigationServiceRecommendation(BaseModel):
    """Service recommendation for navigation electronics."""
    model_config = {"from_attributes": True}

    yacht_id: str = Field(
        ..., description="Eindeutige Yacht-ID im AYDI-System"
    )
    assessment_date: date = Field(
        ..., description="Datum der Bewertung"
    )
    system_age_years: float = Field(
        ..., ge=0.0, le=40.0,
        description="Alter des aeltesten Hauptgeraets in Jahren"
    )
    mfd_manufacturer: MfdManufacturer = Field(
        ..., description="Primaerer MFD-Hersteller"
    )
    firmware_all_current: bool = Field(
        ..., description="Alle Geraete auf aktuellem Firmware-Stand"
    )
    charts_current: bool = Field(
        ..., description="Kartenmaterial aktuell"
    )
    nmea2000_health: str = Field(
        ..., description="NMEA-2000-Netzwerkzustand (excellent, good, degraded, critical)"
    )
    detected_issues: list[FailurePatternCode] = Field(
        default_factory=list,
        description="Erkannte Fehlerbilder"
    )
    missing_safety_equipment: list[str] = Field(
        default_factory=list,
        description="Fehlende Sicherheitsausruestung (ais, epirb, plb, dsc_gps, radar_reflector)"
    )
    service_actions_de: list[str] = Field(
        ..., min_length=1,
        description="Empfohlene Service-Aktionen auf Deutsch"
    )
    upgrade_suggestions_de: list[str] = Field(
        default_factory=list,
        description="Upgrade-Vorschlaege auf Deutsch"
    )
    estimated_service_cost_eur: float = Field(
        ..., ge=0.0,
        description="Geschaetzte Service-Kosten in EUR"
    )
    estimated_upgrade_cost_eur: float = Field(
        default=0.0, ge=0.0,
        description="Geschaetzte Upgrade-Kosten in EUR"
    )
    replacement_recommended: bool = Field(
        default=False,
        description="Komplettsystem-Erneuerung empfohlen"
    )
    replacement_reason_de: Optional[str] = Field(
        default=None,
        description="Begruendung fuer Erneuerungsempfehlung auf Deutsch"
    )
    replacement_budget_eur: Optional[float] = Field(
        default=None, ge=0.0,
        description="Geschaetztes Budget fuer Neuausruestung in EUR"
    )
    next_service_date: Optional[date] = Field(
        default=None,
        description="Empfohlenes naechstes Service-Datum"
    )
    urgency: SeverityLevel = Field(
        default=SeverityLevel.MINOR,
        description="Dringlichkeit der Service-Empfehlung"
    )
    safety_critical: bool = Field(
        default=False,
        description="Sicherheitskritische Maengel vorhanden"
    )
    confidence: ConfidenceLevel = Field(
        default=ConfidenceLevel.ESTIMATED,
        description="Konfidenz der Service-Empfehlung"
    )
```

---

**Ende der Wissensdatei 23.01 — Navigation und Elektronik Grundlagen**

> AYDI Wissensdatei 23.01 | Version 1.0.0 | 2026-05-13 | Status: validated
