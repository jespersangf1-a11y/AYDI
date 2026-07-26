---
title: "NMEA 2000 Vernetzung und Datennetzwerke — Backbone-Design, PGN, Gateways, WiFi, SignalK, Open-Source"
kategorie: "23 Navigation und Elektronik"
unterkategorie: "23.06 NMEA 2000 Vernetzung und Datennetzwerke"
version: "1.0.0"
datum: "2026-05-13"
autor: "AYDI Research"
status: "validated"
confidence_quellen:
  - measured: "NMEA-Spezifikationen, IEC 61162-3, CAN-Bus-Messtechnik, Hersteller-Datenblätter"
  - documented: "Installationsanleitungen, Hersteller-Whitepapers, Praxistests, Werft-Dokumentation"
  - estimated: "Erfahrungswerte, Werft-Konsens, Charterflotten-Feedback, Refit-Statistiken"
---

# 23.06 — NMEA 2000 Vernetzung und Datennetzwerke im Yachtbau: Vollständige Wissensreferenz

> **AYDI Wissensdatei 23.06** — Kategorie 23: Navigation und Elektronik
> **Confidence-Quelle:** measured (NMEA-Spezifikationen, IEC 61162-3, CAN-Bus-Messtechnik), documented (Installationsanleitungen, Praxistests), estimated (Erfahrungswerte, Werft-Konsens)
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

### 1.1 Definition und Funktion

NMEA 2000 (kurz: N2K) ist ein standardisiertes, serielles Datennetzwerk für die marine Bordelektronik, das auf dem Controller Area Network (CAN-Bus) basiert und durch die National Marine Electronics Association (NMEA) spezifiziert wird. Es ermöglicht die Echtzeit-Kommunikation zwischen Navigationsgeräten, Sensoren, Motorsteuerungen, Tankgebern, Autopiloten und weiteren Bordgeräten über ein einziges physikalisches Buskabel.

Im Gegensatz zum Vorgängerstandard NMEA 0183, der als serielles Punkt-zu-Punkt-Protokoll konzipiert war, arbeitet NMEA 2000 als echtes Multi-Master-Netzwerk. Jedes Gerät kann Daten senden und empfangen, ohne dass eine zentrale Steuereinheit erforderlich ist. Die Kommunikation erfolgt über Parameter Group Numbers (PGN), die standardisierte Datenpakete definieren.

Die zentrale Funktion eines NMEA-2000-Netzwerks umfasst sechs Kernbereiche:

1. **Sensordaten-Verteilung** — GPS-Position, Tiefe, Windgeschwindigkeit/-richtung, Bootsspeed, Heading, Temperatur, Druck werden von Sensoren erfasst und allen angeschlossenen Geräten zur Verfügung gestellt
2. **Motorüberwachung** — Drehzahl, Kühlwassertemperatur, Öldruck, Ladedruck, Kraftstoffverbrauch, Betriebsstunden werden vom Motorsteuergerät auf den Bus gelegt
3. **Tank- und Flüssigkeitsmanagement** — Füllstände von Kraftstoff, Wasser, Fäkalien, Grauwasser werden zentral überwacht
4. **Autopilot-Integration** — Kurssteuerung mit Feedback-Schleifen zwischen GPS, Kompass, Ruderlagegeber und Hydraulikpumpe
5. **Alarmsystem** — Bilgenpumpen-Status, Batteriespannung, Rauchmelder, Gasmelder werden netzwerkweit kommuniziert
6. **Systemdiagnose** — Netzwerkstatus, Geräte-Heartbeats, Fehlercodes und Softwareversionen sind remote abfragbar

### 1.2 Historische Entwicklung

**Vor 1983 — Vorstandard-Ära:**
- Jeder Hersteller proprietäres Datenformat
- Kein herstellerübergreifender Datenaustausch möglich
- Analoge Signalübertragung (4–20 mA, 0–10V) für Instrumente
- Raymarine (damals Autohelm/Raytheon) SeaTalk als frühes proprietäres Netzwerk
- Furuno mit eigenem NavNet-Vorläufer

**1983–2000 — NMEA 0183:**
- 1983: NMEA 0183 veröffentlicht — erster standardisierter Datenbus für Marine-Elektronik
- RS-232/RS-422 basiert, seriell, maximal 4.800 Baud (Standard), später 38.400 Baud (HS)
- Punkt-zu-Punkt: ein Talker, mehrere Listener
- ASCII-basierte Sentences (z.B. $GPGGA, $IIMWV, $SDDBT)
- Verdrahtung: geschirmte Zweidrahtleitung pro Verbindung
- Problem: jede Verbindung benötigt eigenes Kabel → Kabelbäume werden komplex
- Problem: keine bidirektionale Kommunikation ohne proprietäre Erweiterungen
- Problem: begrenzte Datenrate für wachsende Datenmenge (AIS, Radar-Overlay)

**2000–2006 — NMEA 2000 Entwicklung:**
- 2000: NMEA 2000 Version 1.0 veröffentlicht, basierend auf SAE J1939 (CAN-Bus aus der Nutzfahrzeugtechnik)
- 2001: Erste Hersteller beginnen N2K-Geräte zu entwickeln
- 2003: IEC 61162-3 übernimmt NMEA 2000 als internationale Norm
- 2004: Maretron als erster Hersteller mit dediziertem NMEA-2000-Komponentenprogramm
- 2005: Garmin, Simrad/Navico, Furuno implementieren N2K in neue MFD-Generationen
- 2006: Micro-C-Steckverbinder (M12 5-polig) wird zum de-facto-Standard für Backbones bis 20m

**2006–2015 — Marktdurchdringung:**
- 2007: Raymarine implementiert N2K in der a/c/e-Serie
- 2008: Yamaha, Mercury, Volvo Penta, Yanmar integrieren N2K in Motorsteuerungen
- 2009: Actisense etabliert sich als führender Gateway-Hersteller (NGW-1, W2K-1)
- 2010: Yacht Devices (Lettland) bringt kostengünstige N2K-Sensoren auf den Markt
- 2011: NMEA 2000 Appendix B definiert erweiterte PGN-Gruppen für Entertaiment und Beleuchtung
- 2012: Maretron N2KView als erstes dediziertes Monitoring-System für N2K-Netzwerke
- 2013: Digital Yacht als Pionier für WiFi-zu-NMEA-Gateways
- 2014: Erste SignalK-Prototypen als Open-Source-Alternative
- 2015: NMEA OneNet (Ethernet-basiert) wird angekündigt

**2015–2020 — Konvergenz und Erweiterung:**
- 2016: SignalK Version 1.0 veröffentlicht — offenes Datenformat, JSON/REST/WebSocket
- 2017: Victron Energy integriert N2K in Energiemanagement-Systeme (Cerbo GX)
- 2018: Yacht Devices YDWG-02 als kompakter WiFi-Gateway wird zum Bestseller
- 2019: Actisense W2K-1 WiFi-Gateway mit NMEA 2000 und NMEA 0183
- 2020: NMEA OneNet Version 1.0 auf Ethernet-Basis verabschiedet (NMEA-eigener Standard auf Basis IEEE 802.3 Ethernet / IPv6 — nicht IEC 61162-460)
- 2020: Raspberry Pi + SignalK als DIY-Lösung gewinnt Community-Traktion

**2020–heute — Offene Standards und Edge-Computing:**
- 2021: SignalK 2.0 mit Plugin-Architektur, App Store, Dashboard
- 2022: Navico (Lowrance/Simrad/B&G) integriert SignalK-Kompatibilität
- 2023: NMEA OneNet-Geräte von Maretron und Furuno erscheinen
- 2024: CAN FD (Flexible Data-rate) als Zukunftsoption diskutiert (bis 8 Mbit/s)
- 2025: Edge-Computing auf NMEA-Gateways: lokale KI-Analyse, Predictive Maintenance
- 2026: WiFi 6E-Gateways, Mesh-Netzwerke an Bord, Integration von Starlink-Terminals

### 1.3 Bedeutung im modernen Yachtdesign

Im Kontext des AYDI-Analysesystems ist das NMEA-2000-Netzwerk ein zentraler Design-Parameter, der folgende Module beeinflusst:

- **Ergonomie-Modul:** Instrumentenpositionierung, Display-Anordnung, Bedienplätze (Steuerstand, Navigationstisch, Cockpit) müssen Netzwerkzugriff haben
- **Compliance-Modul:** Pflichtausrüstung nach Bootsführerschein-Verordnung, CE-Kategorie-Anforderungen an Navigationsausrüstung, SOLAS-Anforderungen bei Charteryachten
- **Kosten-Modul:** N2K-Netzwerk-Infrastruktur umfasst typisch 8–18% der Gesamtkosten der Elektronikausrüstung (Kabel, Stecker, Gateways, Terminatoren)
- **Produktions-Modul:** Backbone-Kabelführung, Steckerpositionen, Drop-Kabel-Längen, Zugänglichkeit für Service
- **Elektrik-Modul:** Stromversorgung des Netzwerks (LEN-Berechnung), Massekonzept, EMV-Verträglichkeit, Blitzschutz
- **Service-Modul:** Diagnose-Zugang, Firmware-Updates, Gerätetausch ohne Netzwerk-Neudesign, Erweiterbarkeit
- **Strukturmodul:** Kabelkanäle, Durchbrüche, Vibrationsdämpfung bei Motorgeräten

### 1.4 Marktüberblick und wirtschaftliche Bedeutung

Der weltweite Markt für marine Datennetzwerk-Komponenten (NMEA 2000, Gateways, WiFi-Multiplexer) wird auf ca. 380–520 Mio. USD geschätzt (2025), mit einer jährlichen Wachstumsrate von 9–14%.

**Marktanteile Netzwerk-Infrastruktur (geschätzt, 2025):**

| Hersteller | Marktanteil | Kernprodukte |
|------------|------------|--------------|
| Maretron | 18–22% | Premium-Backbone, Sensoren, Monitoring |
| Actisense | 15–20% | Gateways, Diagnostik, Multiplexer |
| Garmin | 12–16% | Backbone-Kits, Sensoren (über Gerätekauf) |
| Navico (Simrad/B&G/Lowrance) | 10–14% | Integrierte Netzwerke, Backbone-Kits |
| Yacht Devices | 8–12% | Budget-Gateways, Sensoren, WiFi |
| Digital Yacht | 5–8% | WiFi-Gateways, AIS-Integration |
| Sonstige (Furuno, Raymarine, Victron, DIY) | 15–25% | Diverse Speziallösungen |

**Kostenstruktur eines typischen N2K-Netzwerks:**

| Bootsklasse | Geräte am Bus | Backbone-Kosten | Gateway-Kosten | Gesamtkosten Netzwerk |
|-------------|--------------|-----------------|----------------|----------------------|
| 8–10m Segelyacht | 6–10 | 180–350 € | 150–400 € | 800–2.500 € |
| 10–14m Fahrtenyacht | 10–18 | 300–600 € | 300–800 € | 2.500–6.000 € |
| 14–20m Blauwasseryacht | 15–30 | 500–1.200 € | 600–1.500 € | 5.000–15.000 € |
| 20–30m Motoryacht | 20–45 | 800–2.000 € | 1.000–3.000 € | 10.000–35.000 € |
| 30m+ Superyacht | 40–100+ | 2.000–8.000 € | 3.000–12.000 € | 30.000–120.000 € |

### 1.5 Normative Referenzen

| Norm/Spezifikation | Bezeichnung | Relevanz |
|---------------------|-------------|----------|
| IEC 61162-1 | Maritime Navigation — NMEA 0183 | Vorgängerprotokoll, Bridging |
| IEC 61162-3 | Maritime Navigation — NMEA 2000 | Kern-Netzwerkspezifikation |
| IEC 61162-450 | Maritime Navigation — Ethernet (Lightweight) | Ethernet-Transport |
| IEC 61162-460 | Maritime Navigation — Ethernet-Interconnection: Safety & Security | Sicherheits-/Security-Ergänzung zu IEC 61162-450 (NICHT identisch mit NMEA OneNet) |
| SAE J1939 | CAN-Bus für Nutzfahrzeuge | Physikalische Basis von N2K |
| ISO 11783 | ISOBUS (Landwirtschaft) | Verwandtes CAN-Protokoll |
| ISO 11898-1/2 | CAN-Bus Spezifikation | Physikalische Schicht |
| IEC 60945 | Maritime Navigation — Allgemeine Anforderungen | EMV, Umwelt, Vibration |
| IEC 62402 | Obsoleszenz-Management | Langzeit-Verfügbarkeit |
| EN ISO 13297 | Elektrische Systeme — Gleich- und Wechselstrom | Elektrische Installation |

---

## 2. Grundlagen und Theorie

### 2.1 CAN-Bus-Grundlagen

#### 2.1.1 Physikalische Schicht (Physical Layer)

NMEA 2000 basiert auf CAN 2.0B (Controller Area Network) mit 29-Bit Extended Identifier. Die physikalische Übertragung erfolgt als differenzielles Signal auf zwei Leitern (CAN_H und CAN_L) mit einer Nominalspannung von:

- **Rezessiver Zustand (logisch 1):** CAN_H = CAN_L = 2,5V (Differenz ≈ 0V)
- **Dominanter Zustand (logisch 0):** CAN_H ≈ 3,5V, CAN_L ≈ 1,5V (Differenz ≈ 2V)

**Datenrate:** 250 kbit/s (fest, nicht konfigurierbar)

**Kabellängen und Topologie:**

| Parameter | Micro-C (M12) | Mini-C (Devicenet) | Mid-C |
|-----------|---------------|-------------------|-------|
| Max. Backbone-Länge | 100m | 200m | 200m |
| Max. Drop-Kabel | 6m | 6m | 6m |
| Max. kumulative Drop-Länge | 78m | 78m | 78m |
| Max. Geräte am Bus | 50 (LEN-abhängig) | 50 | 50 |
| Kabelquerschnitt Backbone | 0,82 mm² (18 AWG) | 1,31 mm² (16 AWG) | 2,08 mm² (14 AWG) |
| Kabelquerschnitt Drop | 0,34 mm² (22 AWG) | 0,82 mm² (18 AWG) | 0,82 mm² (18 AWG) |
| Abschirmung | Ja, 360° Schirm | Ja, 360° Schirm | Ja, 360° Schirm |

**Kabelaufbau (5 Leiter + Schirm):**

| Ader | Farbe (DeviceNet) | Farbe (Micro-C) | Funktion |
|------|-------------------|-----------------|----------|
| 1 | Weiß | Blau | CAN_H (Daten High) |
| 2 | Blau | Weiß | CAN_L (Daten Low) |
| 3 | Schwarz | Schwarz | Masse (Shield/GND) |
| 4 | Rot | Rot | +12V Versorgung (NET-S) |
| 5 | Bare/Drain | Bare/Drain | Schirm/Drain Wire |

**Hinweis zur Stromversorgung:** Das NMEA-2000-Netzwerk transportiert neben Daten auch eine 12V-Versorgungsspannung (NET-S, Net Supply). Diese versorgt Geräte mit geringem Strombedarf direkt über den Bus. Geräte mit höherem Strombedarf (z.B. MFDs, Radar) haben eigene Stromversorgung und nutzen nur die Datenleitungen.

#### 2.1.2 LEN (Load Equivalency Number)

Jedes NMEA-2000-Gerät hat eine LEN (Load Equivalency Number), die seinen Stromverbrauch aus dem Netzwerk angibt. Eine LEN entspricht 50 mA bei 12V.

**LEN-Berechnung für das Gesamtnetzwerk:**

```
Gesamt-LEN = Summe aller Geräte-LEN
Max. LEN bei Micro-C Backbone: 50 LEN (2,5 A bei 12V)
Max. LEN bei Mini-C/DeviceNet: 80 LEN (4,0 A bei 12V)
```

**Typische LEN-Werte:**

| Gerätetyp | LEN | Strombedarf |
|-----------|-----|-------------|
| GPS-Antenne (extern) | 1 | 50 mA |
| Windgeber | 1 | 50 mA |
| Tiefenmesser/Echolot | 1–2 | 50–100 mA |
| Tankgeber | 1 | 50 mA |
| Temperatursensor | 1 | 50 mA |
| Batteriemonitor | 1–2 | 50–100 mA |
| Autopilot-Computer | 3–4 | 150–200 mA |
| NMEA-2000-Gateway | 1–3 | 50–150 mA |
| WiFi-Gateway | 2–4 | 100–200 mA |
| Kartenplotter (klein, 5–7") | 2–4 | 100–200 mA |
| Kartenplotter (groß, 12–16") | Extern | Eigene Versorgung |
| Motorsteuerung | Extern | Eigene Versorgung |

**Spannungsabfall-Berechnung:**

Der Spannungsabfall über die Backbone-Leitung muss berücksichtigt werden. Am entferntesten Gerät darf die Spannung nicht unter 9V fallen (Mindestbetriebsspannung der meisten N2K-Geräte).

```
U_drop = I × R × L × 2
wobei:
  I = Gesamtstrom hinter dem Messpunkt
  R = Widerstand pro Meter (abhängig vom Querschnitt)
  L = Länge in Metern
  ×2 = Hin- und Rückleiter

Micro-C (0,82 mm²): R ≈ 0,021 Ω/m
Mini-C (1,31 mm²): R ≈ 0,013 Ω/m
Mid-C (2,08 mm²): R ≈ 0,008 Ω/m
```

#### 2.1.3 Terminierung

Jeder CAN-Bus benötigt an beiden physikalischen Enden des Backbones einen Abschlusswiderstand (Terminator) von 120 Ω zwischen CAN_H und CAN_L. Die parallele Schaltung beider Terminatoren ergibt die nominale Bus-Impedanz von 60 Ω.

**Kritische Regeln:**
- **Exakt zwei Terminatoren** — nicht mehr, nicht weniger
- Terminatoren sitzen an den physikalischen Enden des Backbones, NICHT an Drop-Kabeln
- Fehlende Terminierung: Signalreflexionen, sporadische Datenfehler, Geräteausfälle
- Zu viele Terminatoren: Bus-Impedanz zu niedrig, Signalpegel zu schwach, Bus-Off-Zustand
- Terminatoren sind geschlechtsspezifisch: ein Male-Terminator, ein Female-Terminator (an den jeweiligen offenen Enden)

**Messung der Terminierung:**
- Bus stromlos, alle Geräte getrennt → zwischen CAN_H und CAN_L messen
- Korrekt: 60 Ω (±5%)
- Nur ein Terminator: 120 Ω
- Kein Terminator: >10 kΩ (offen)
- Drei oder mehr Terminatoren: <40 Ω

### 2.2 NMEA 2000 Protokoll-Architektur

#### 2.2.1 Schichtenmodell

NMEA 2000 implementiert ein vereinfachtes OSI-Schichtenmodell:

| OSI-Schicht | NMEA-2000-Implementierung |
|-------------|--------------------------|
| 7 — Application | PGN-Definitionen, Datenfelder |
| 6 — Presentation | Skalierung, Einheiten, Datentypen |
| 5 — Session | n/a (verbindungslos) |
| 4 — Transport | Fast-Packet-Protokoll, Transport-Protokoll (TP) |
| 3 — Network | Adressvergabe (Address Claim) |
| 2 — Data Link | CAN 2.0B Frames |
| 1 — Physical | CAN-Transceiver, Kabel, Stecker |

#### 2.2.2 CAN-Frame-Struktur

Ein NMEA-2000-Telegramm besteht aus einem CAN 2.0B Extended Frame:

```
| SOF | 29-Bit Identifier | RTR | IDE | r0 | DLC | Data (0–8 Bytes) | CRC | ACK | EOF |
  1b    29 bits              1b   1b   1b   4b    0–64 bits          15b   2b    7b
```

**Der 29-Bit-Identifier kodiert:**

| Bits | Feld | Bedeutung |
|------|------|-----------|
| 28–26 | Priority | Priorität (0–7, 0 = höchste) |
| 25–16 | PGN (MSB) | Parameter Group Number (obere 10 Bits) |
| 15–8 | PGN (LSB) / Dest | PGN untere 8 Bits ODER Zieladresse |
| 7–0 | Source Address | Quelladresse des sendenden Geräts |

**Prioritäten:**

| Priorität | Typische Verwendung | Beispiel-PGN |
|-----------|--------------------|----|
| 0–1 | Netzwerk-Management | Address Claim, ISO Request |
| 2 | Sicherheitskritisch | Alarme, Mann-über-Bord |
| 3 | Navigation | GPS-Position, Heading, Tiefe |
| 4 | Motor/Energie | Motordaten, Batteriestatus |
| 5 | Instrumente | Wind, Geschwindigkeit, Temperatur |
| 6 | Informationen | AIS, Wegpunkte, Routen |
| 7 | Standard/Default | Hersteller-spezifisch |

#### 2.2.3 Parameter Group Numbers (PGN)

PGNs sind die zentrale Dateninhalts-Definition von NMEA 2000. Jede PGN beschreibt ein konkretes Datenpaket mit definierten Feldern, Skalierungen und Einheiten.

**Wichtige PGN-Gruppen für Yachten:**

| PGN | Name | Inhalt | Update-Rate |
|-----|------|--------|------------|
| 59392 | ISO Acknowledgment | Bestätigung/Fehler | Auf Anfrage |
| 59904 | ISO Request | Datenanforderung | Auf Anfrage |
| 60928 | ISO Address Claim | Geräteadresse | Bei Netzwerkstart |
| 126992 | System Time | UTC Datum/Zeit | 1 Hz |
| 126993 | Heartbeat | Geräte-Lebenszeichen | 1 Hz |
| 126996 | Product Information | Hersteller, Modell, SW-Version | Auf Anfrage |
| 127245 | Rudder | Ruderwinkel, Richtung | 10 Hz |
| 127250 | Vessel Heading | Kurs (magnetisch/wahr) | 10 Hz |
| 127251 | Rate of Turn | Drehrate | 10 Hz |
| 127257 | Attitude | Pitch, Roll, Yaw | 10 Hz |
| 127488 | Engine Parameters (Rapid) | Drehzahl, Trim, Tilt | 10 Hz |
| 127489 | Engine Parameters (Dynamic) | Temperatur, Öldruck, Spannung | 0,5 Hz |
| 127493 | Transmission Parameters | Gang, Öldruck, Temperatur | 10 Hz |
| 127501 | Binary Switch Bank | Schalterzustände (28 Kanäle) | Auf Änderung |
| 127505 | Fluid Level | Tankfüllstand, Typ, Kapazität | 2,5 Hz |
| 127508 | Battery Status | Spannung, Strom, Temperatur, SoC | 1,5 Hz |
| 128259 | Speed (Water) | Fahrt durchs Wasser | 2 Hz |
| 128267 | Water Depth | Wassertiefe, Offset | 2 Hz |
| 129025 | Position (Rapid) | Lat/Lon | 4 Hz |
| 129026 | COG/SOG (Rapid) | Kurs/Geschwindigkeit über Grund | 4 Hz |
| 129029 | GNSS Position | Position, HDOP, Satelliten, Methode | 1 Hz |
| 129038 | AIS Class A Report | MMSI, Position, COG, SOG, Heading | variabel |
| 129039 | AIS Class B Report | MMSI, Position, COG, SOG | variabel |
| 129283 | Cross Track Error | Querabweichung vom Kurs | 1 Hz |
| 129284 | Navigation Data | Distanz, Bearing, ETA zum Wegpunkt | 1 Hz |
| 130306 | Wind Data | Windgeschwindigkeit, -winkel, Referenz | 2 Hz |
| 130310 | Environmental Parameters | Wassertemperatur, Lufttemperatur, Druck | 0,5 Hz |
| 130311 | Environmental Parameters | Temperatur, Feuchtigkeit, Druck | 0,5 Hz |
| 130312 | Temperature | Temperaturquelle, Wert | 0,5 Hz |
| 130316 | Temperature (Extended) | Erweiterte Temperatur | 0,5 Hz |
| 130567 | Watermaker Input | Produktionsrate, Salzgehalt, Druck | 0,5 Hz |

**PGN-Datentypen und Skalierung:**

| Datentyp | Bytes | Bereich | Beispiel |
|----------|-------|---------|---------|
| Latitude | 4 | ±90° | Resolution: 1×10⁻⁷ ° |
| Longitude | 4 | ±180° | Resolution: 1×10⁻⁷ ° |
| Temperature | 2 | 0–655,35 K | Resolution: 0,01 K |
| Pressure | 4 | 0–4.294.967,295 Pa | Resolution: 0,1 Pa |
| Speed | 2 | 0–655,35 m/s | Resolution: 0,01 m/s |
| Angle | 2 | 0–360° oder ±180° | Resolution: 0,0001 rad |
| Distance | 4 | 0–4.294.967.295 m | Resolution: 0,01 m |
| Voltage | 2 | 0–655,35 V | Resolution: 0,01 V |
| Current | 2 | 0–655,35 A | Resolution: 0,1 A |
| Volume | 4 | 0–4.294.967,295 L | Resolution: 0,001 L |

#### 2.2.4 Adressvergabe (Address Claim Protocol)

Jedes NMEA-2000-Gerät erhält eine eindeutige 8-Bit-Adresse (0–251). Die Adressvergabe erfolgt automatisch beim Netzwerkstart über das ISO Address Claim Protocol (PGN 60928):

1. Gerät sendet Address Claim mit seiner gewünschten Adresse und seinem NAME (64-Bit eindeutig)
2. Bei Adresskonflikt: Gerät mit niedrigerem NAME (höhere Priorität) behält die Adresse
3. Verlierer sucht neue freie Adresse und wiederholt den Claim
4. Adresse 252 = „Cannot Claim" (Gerät kann nicht teilnehmen)
5. Adresse 253 = reserviert
6. Adresse 254 = Broadcast
7. Adresse 255 = Global (alle Geräte)

**NAME-Feld (64 Bit, PGN 60928):**

| Bits | Feld | Bedeutung |
|------|------|-----------|
| 0 | Arbitrary Address Capable | 1 = kann Adresse ändern |
| 1–3 | Industry Group | 4 = Marine |
| 4–7 | Vehicle System Instance | Instanznummer |
| 8–14 | Vehicle System | Systemtyp |
| 15 | Reserved | 0 |
| 16–23 | Function | Gerätefunktion |
| 24–28 | Function Instance | Funktionsinstanz |
| 29–31 | ECU Instance | ECU-Instanz |
| 32–42 | Manufacturer Code | NMEA-Herstellercode |
| 43–63 | Unique Number | Eindeutige Seriennummer |

#### 2.2.5 Fast-Packet-Protokoll

PGNs mit mehr als 8 Bytes Nutzdaten (bis 223 Bytes) werden im Fast-Packet-Protokoll übertragen. Die Daten werden in Frames à 8 Bytes aufgeteilt:

- **Frame 0:** Byte 0 = Sequenz-Counter (Bits 7–5) + Frame-Counter 0 (Bits 4–0), Byte 1 = Gesamtlänge, Bytes 2–7 = Daten (6 Bytes)
- **Frame 1–N:** Byte 0 = Sequenz-Counter + Frame-Counter (1–31), Bytes 1–7 = Daten (7 Bytes)

Beispiel: PGN 129029 (GNSS Position Data) = 43 Bytes → 7 CAN-Frames

#### 2.2.6 Transport-Protokoll (ISO 11783-3)

Für Nachrichten >223 Bytes (bis 1785 Bytes) wird das Transport-Protokoll verwendet:

1. **BAM (Broadcast Announce Message):** Sender kündigt Multi-Frame-Nachricht an
2. **TP.DT (Transfer Data):** Datenpakete à 7 Bytes Nutzdaten
3. **TP.CM (Connection Management):** Flusskontrolle bei Peer-to-Peer

### 2.3 NMEA 0183 und Bridging

#### 2.3.1 NMEA 0183 Grundlagen

NMEA 0183 bleibt relevant, weil viele ältere Geräte (und einige aktuelle) nur dieses Protokoll unterstützen. Ein Gateway übersetzt bidirektional zwischen NMEA 0183 und NMEA 2000.

**NMEA 0183 Technische Daten:**

| Parameter | Standard | High-Speed |
|-----------|----------|------------|
| Baudrate | 4.800 Baud | 38.400 Baud |
| Signalstandard | RS-422 (differenziell) | RS-422 |
| Topologie | 1 Talker → N Listener | 1 Talker → N Listener |
| Max. Listener | 4 (elektrisch) | 4 |
| Kabel | Geschirmte Zweidrahtleitung | Geschirmte Zweidrahtleitung |
| Max. Kabellänge | Nicht spezifiziert, praxisüblich ≤30m | ≤30m |
| Datenformat | ASCII, CR+LF terminiert | ASCII, CR+LF terminiert |
| Checksumme | XOR über alle Zeichen zwischen $ und * | XOR |
| Max. Sentence-Länge | 82 Zeichen (inkl. $ und CR+LF) | 82 Zeichen |

**Wichtige NMEA-0183-Sentences:**

| Sentence | Talker | Inhalt | N2K-Äquivalent (PGN) |
|----------|--------|--------|--------------------|
| GGA | GP/GN | GPS-Fix, Position, HDOP | 129029 |
| GLL | GP/GN | Lat/Lon, Status | 129025 |
| GSA | GP/GN | Satellitenstatus, DOP | 129539, 129540 |
| GSV | GP/GN | Satelliten in Sicht | 129540 |
| HDG | HC/HE | Heading, Deviation, Variation | 127250 |
| HDT | HC/HE | True Heading | 127250 |
| MWV | II/WI | Wind Speed/Angle | 130306 |
| RMC | GP/GN | Recommended Minimum (Pos, COG, SOG) | 129025, 129026 |
| RSA | -- | Rudder Sensor Angle | 127245 |
| VHW | II/VW | Water Speed/Heading | 128259 |
| VTG | GP/GN | Track Made Good, Ground Speed | 129026 |
| DBT | SD | Depth Below Transducer | 128267 |
| DPT | SD | Depth | 128267 |
| MTW | -- | Water Temperature | 130310 |
| VDM | AI | AIS VHF Datalink Message | 129038, 129039 |
| XTE | -- | Cross-Track Error | 129283 |
| APB | -- | Autopilot Sentence B | 129284 |
| RMB | -- | Recommended Minimum (Navigation) | 129284 |

#### 2.3.2 Bridging-Strategien

**Unidirektionale Bridges:**
- NMEA 0183 → NMEA 2000: Legacy-Sensoren (z.B. alter Windgeber) in N2K-Netzwerk einbinden
- NMEA 2000 → NMEA 0183: N2K-Daten an Legacy-Geräte (z.B. alter Autopilot) weiterleiten

**Bidirektionale Gateways:**
- Übersetzung in beide Richtungen
- PGN-zu-Sentence-Mapping konfigurierbar
- Filterung: nicht alle PGN/Sentences werden übersetzt (Bandbreite NMEA 0183 limitiert)
- Priorität: bei mehreren Datenquellen für gleiche Information → Quellenpriorität konfigurieren

**Häufige Bridging-Probleme:**

| Problem | Ursache | Lösung |
|---------|---------|--------|
| Datenrate-Flaschenhals | 0183 @ 4.800 Baud ≈ 10 Sentences/s | HS-0183 verwenden oder Filterung |
| Doppelte Daten | Sensor sendet auf 0183 UND N2K | Eine Quelle deaktivieren |
| Source-Konflikte | Mehrere GPS-Quellen | Talker-ID-Filterung am Gateway |
| Fehlende Sentences | Gateway kennt proprietäre Sentences nicht | Firmware-Update, manuelles Mapping |
| Zeichensatzkonflikte | Umlaute in Wegpunktnamen | ASCII-Only verwenden |

### 2.4 NMEA OneNet (Ethernet-basiert)

#### 2.4.1 Überblick

NMEA OneNet ist die Ethernet-basierte Erweiterung des NMEA-Standards — ein NMEA-eigener Standard auf Basis von IEEE 802.3 Ethernet und IPv6 (nicht identisch mit IEC 61162-450/460, kann aber mit diesen auf derselben Ethernet-Infrastruktur koexistieren). Es transportiert NMEA-2000-PGNs über Ethernet/IP und ermöglicht:

- Höhere Datenraten (100 Mbit/s bis 1 Gbit/s)
- Mehr Geräte (keine 50-Geräte-Beschränkung)
- Längere Kabelwege (100m pro Segment bei Cat5e/Cat6)
- Integration von Video, Radar-Rohbildern, IP-Kameras
- Koexistenz mit Standard-IT-Geräten (NAS, Computer)
- Deterministische Übertragung via TSN (Time-Sensitive Networking)

**Technische Eckdaten:**

| Parameter | NMEA 2000 | NMEA OneNet |
|-----------|-----------|-------------|
| Physik | CAN-Bus 250 kbit/s | Ethernet 100M/1G |
| Max. Geräte | 50 | 250+ |
| Max. Segmentlänge | 100–200m | 100m (Kupfer) |
| Datenformat | CAN-Frames, PGN | PGN über UDP/IP |
| Echtzeitfähigkeit | Ja (CAN-Arbitration) | Ja (TSN/PTP) |
| Steckverbinder | M12 (Micro-C) | M12 X-kodiert (8-polig) |
| Topologie | Linearer Bus | Stern, Daisy-Chain, Ring |
| Stromversorgung | 12V über Bus (NET-S) | PoE (Power over Ethernet) |
| Protokoll-Stack | CAN 2.0B / NMEA 2000 | UDP/IP / NMEA OneNet |
| Time Sync | Keine (asynchron) | IEEE 1588 (PTP) < 1μs |
| Discovery | Address Claim | mDNS/DNS-SD |

#### 2.4.2 Koexistenz mit N2K

NMEA OneNet ersetzt NMEA 2000 nicht, sondern erweitert es. Typische Architektur:

```
[Sensoren/Geber] ←→ [NMEA 2000 Backbone] ←→ [N2K-zu-OneNet Gateway] ←→ [Ethernet Switch] ←→ [MFD, Server, Kameras]
```

Gründe für Koexistenz:
- N2K-Sensoren sind bewährt, günstig, robust
- OneNet bietet Bandbreite für Video, Radar, große Datenmengen
- Schrittweise Migration möglich (kein Alles-oder-Nichts)

### 2.5 WiFi-Multiplexer und drahtlose Vernetzung

#### 2.5.1 Funktionsprinzip

Ein WiFi-Multiplexer (oder WiFi-Gateway) verbindet das kabelgebundene NMEA-Netzwerk mit drahtlosen Endgeräten (Tablets, Smartphones, Laptops). Er stellt die Daten typischerweise in einem oder mehreren Formaten bereit:

- **TCP/UDP-Server** mit NMEA-0183-Sentences (Port 10110, 2000, 39150 etc.)
- **WebSocket-Server** mit JSON-formatierten Daten
- **HTTP-REST-API** für Konfiguration und Abfrage
- **SignalK-Server** (integriert oder als Ziel)

**Typische Architektur:**

```
[NMEA 2000 Bus] → [WiFi-Gateway] → WiFi AP → [Tablet App: iSailor, Navionics, etc.]
                                             → [Laptop: OpenCPN, Expedition, etc.]
                                             → [Smartphone: Anchor Watch, etc.]

[NMEA 0183 Geräte] → [WiFi-Multiplexer] → WiFi AP → [Apps/Software]
```

#### 2.5.2 Betriebsmodi

| Modus | Beschreibung | Anwendung |
|-------|-------------|-----------|
| Access Point (AP) | Gateway erzeugt eigenes WLAN | Standalone, kein Router nötig |
| Client (STA) | Gateway verbindet sich mit vorhandenem WLAN | Integration in Bord-Netzwerk |
| AP + Client | Beides gleichzeitig | Bord-WLAN + Internet-Durchleitung |
| Bridge | Transparent zwischen WLAN und LAN | Ethernet-Geräte drahtlos anbinden |

#### 2.5.3 Sicherheitsaspekte

- WiFi-Gateways senden standardmäßig Positionsdaten → **WPA2/WPA3-Verschlüsselung Pflicht**
- SSID-Name sollte keine Bootsinformationen enthalten (kein „SY_Moonshine_Nav")
- Separate VLANs für Navigation und Entertainment empfohlen
- Port-Filterung: nur notwendige Ports öffnen (10110, 2000 TCP/UDP)
- Firmware-Updates regelmäßig einspielen
- Gastnetz für Chartergäste ohne Zugriff auf Navigationsdaten

### 2.6 SignalK — Open-Source Marine Data Standard

#### 2.6.1 Überblick und Philosophie

SignalK ist ein offenes, communitygetriebenes Datenformat und Server-Framework für die marine Datenvernetzung. Im Gegensatz zu NMEA 2000 (proprietäre Spezifikation, Lizenzgebühren) ist SignalK vollständig quelloffen (Apache 2.0 Lizenz).

**Kernkonzepte:**

1. **JSON-basiertes Datenmodell:** Alle Daten als hierarchischer JSON-Baum
2. **REST-API:** HTTP-Zugriff auf alle Datenpunkte
3. **WebSocket-Streaming:** Echtzeit-Daten-Push an Clients
4. **Plugin-Architektur:** Erweiterbar durch Node.js-Plugins
5. **Herstellerunabhängig:** Offenes Format, keine Lizenzgebühren

**SignalK Datenmodell (Auszug):**

```json
{
  "vessels": {
    "urn:mrn:imo:mmsi:211000001": {
      "name": "SY Nordlicht",
      "mmsi": "211000001",
      "navigation": {
        "position": {
          "value": {"latitude": 54.3233, "longitude": 10.1394},
          "timestamp": "2026-05-13T14:30:00Z",
          "source": {"label": "GPS1", "type": "NMEA2000", "pgn": 129029}
        },
        "courseOverGroundTrue": {
          "value": 3.1415,
          "timestamp": "2026-05-13T14:30:00Z"
        },
        "speedOverGround": {
          "value": 3.6,
          "timestamp": "2026-05-13T14:30:00Z"
        },
        "headingTrue": {"value": 3.14},
        "headingMagnetic": {"value": 3.12}
      },
      "environment": {
        "wind": {
          "speedApparent": {"value": 8.5},
          "angleApparent": {"value": 0.785}
        },
        "depth": {
          "belowTransducer": {"value": 12.3}
        },
        "water": {
          "temperature": {"value": 289.15}
        }
      },
      "propulsion": {
        "main": {
          "revolutions": {"value": 35.0},
          "temperature": {"value": 353.15},
          "oilPressure": {"value": 350000},
          "runTime": {"value": 1850400}
        }
      },
      "tanks": {
        "fuel": {
          "main": {
            "currentLevel": {"value": 0.72},
            "capacity": {"value": 0.400}
          }
        }
      },
      "electrical": {
        "batteries": {
          "house": {
            "voltage": {"value": 12.8},
            "current": {"value": -5.2},
            "stateOfCharge": {"value": 0.85}
          }
        }
      }
    }
  }
}
```

**Einheiten in SignalK (SI-Basis):**

| Größe | Einheit | Beispiel |
|-------|---------|---------|
| Position | Dezimalgrad | 54.3233° |
| Geschwindigkeit | m/s | 3.6 m/s = 7.0 kn |
| Winkel | Radiant | 3.14159 rad = 180° |
| Temperatur | Kelvin | 289.15 K = 16°C |
| Druck | Pascal | 101325 Pa = 1 atm |
| Volumen | m³ | 0.400 m³ = 400 L |
| Distanz | Meter | 1852 m = 1 NM |
| Strom | Ampere | -5.2 A (negativ = Entladung) |
| Spannung | Volt | 12.8 V |
| Drehzahl | Hz (1/s) | 35.0 Hz = 2100 rpm |
| Zeit | Sekunden | 1850400 s ≈ 514 h |

#### 2.6.2 SignalK Server (Node.js)

Der SignalK-Server ist die Referenzimplementierung in Node.js. Er läuft auf Linux (Raspberry Pi, NUC, Server), macOS oder Windows.

**Architektur:**

```
[NMEA 2000] → [USB-Gateway: Actisense NGT-1 / Yacht Devices YDNU-02] → [SignalK Server]
[NMEA 0183] → [USB-Serial-Adapter] → [SignalK Server]
[Seatalk1] → [USB-Serial + Konverter] → [SignalK Server]

SignalK Server:
  ├── REST API (HTTP GET/PUT)       → http://localhost:3000/signalk/v1/api/
  ├── WebSocket Stream              → ws://localhost:3000/signalk/v1/stream
  ├── Plugin System                 → Autopilot, Anchor Watch, Alarms, etc.
  ├── Web App (Dashboard)           → http://localhost:3000/
  ├── NMEA 0183 TCP Output          → Port 10110
  └── Data Store (InfluxDB/SQLite)  → Historische Daten
```

**Wichtige SignalK-Plugins:**

| Plugin | Funktion |
|--------|----------|
| signalk-autopilot | Autopilot-Steuerung über Web-Interface |
| signalk-anchor-alarm | Ankerwache mit Push-Benachrichtigung |
| signalk-venusOS | Victron Energy Integration |
| signalk-dashboard | Konfigurierbares Instrumenten-Dashboard |
| signalk-derived-data | Berechnete Werte (True Wind, VMG, etc.) |
| signalk-to-influxdb | Datenlogging in InfluxDB |
| signalk-zones | Alarmzonen für Werte (z.B. Tiefe < 3m) |
| signalk-polar | Polar-Diagramm und Performance |
| signalk-raspberry-pi-monitoring | System-Monitoring (CPU, Temperatur) |
| freeboard-sk | Vollständige Navigationsanwendung |

#### 2.6.3 SignalK auf Raspberry Pi

Die populärste DIY-Lösung für marine Datenvernetzung ist ein Raspberry Pi mit SignalK Server. Die typische Hardware-Konfiguration:

**Hardware-BOM (Bill of Materials):**

| Komponente | Modell | Kosten (ca.) |
|------------|--------|-------------|
| Raspberry Pi | Pi 4 Model B (4 GB) oder Pi 5 | 60–90 € |
| Gehäuse | Aluminium-Gehäuse, passiv gekühlt | 15–25 € |
| Netzteil | 12V→5V/3A DC-DC-Wandler (Victron Orion, etc.) | 20–35 € |
| SD-Karte | Industrial 32 GB (SanDisk Industrial, Transcend) | 15–25 € |
| N2K-USB-Gateway | Actisense NGT-1-USB oder Yacht Devices YDNU-02 | 180–280 € |
| NMEA-0183-Adapter | USB-Serial (FTDI-basiert) | 15–30 € |
| WiFi-Antenne | Externe Antenne mit Pigtail (optional, Pi hat WLAN) | 10–20 € |
| **Gesamt** | | **315–505 €** |

**Software-Installation (Kurzreferenz):**

```bash
# Raspberry Pi OS Lite (64-Bit) installieren
# SSH aktivieren, Hostname setzen (z.B. "signalk")

# Node.js 18 LTS installieren
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs

# SignalK Server installieren
sudo npm install -g signalk-server
sudo signalk-server-setup

# Systemd-Service aktivieren
sudo systemctl enable signalk
sudo systemctl start signalk

# Web-Interface: http://signalk.local:3000
```

### 2.7 Backbone-Design-Grundlagen

#### 2.7.1 Topologie-Regeln

Das NMEA-2000-Netzwerk ist als **linearer Bus** konzipiert. Sternförmige oder ringförmige Topologien sind NICHT zulässig.

```
KORREKT — Linearer Bus:
[Term-M] ──── [T-Stück] ── [T-Stück] ── [T-Stück] ── [T-Stück] ── [Term-F]
                  │             │             │             │
               [Drop]        [Drop]        [Drop]        [Drop]
                  │             │             │             │
              [Gerät 1]    [Gerät 2]    [Gerät 3]    [Gerät 4]

FALSCH — Stern:
                [Gerät 1]
                    │
                 [Drop]
                    │
[Gerät 2] ── [Hub/Switch] ── [Gerät 3]
                    │
                 [Drop]
                    │
                [Gerät 4]

FALSCH — Ring:
[Gerät 1] ── [Gerät 2] ── [Gerät 3] ── [Gerät 4] ── [Gerät 1]
```

#### 2.7.2 Zonierung des Backbones

Bei größeren Yachten wird das Netzwerk in Zonen unterteilt:

**Zone A — Steuerstand/Cockpit:**
- Kartenplotter, Instrumentendisplays, Autopilot-Controller
- Kurze Drop-Kabel (0,5–2m)
- Hohe Signalqualität erforderlich (Echtzeit-Navigation)

**Zone B — Maschinenraum:**
- Motorsteuerung, Tankgeber, Bilgenpumpen-Sensor
- Vibrations- und EMV-Belastung hoch
- Kabel in Wellrohr, Stecker mit Sicherung gegen Vibrationslockerung
- Abstand zu Lichtmaschine und Startermotor einhalten (min. 30 cm)

**Zone C — Unterdeck/Salon:**
- Instrumente-Repeater, Klimasteuerung, Beleuchtungsbus
- Moderate Umgebungsbedingungen
- Ästhetische Kabelführung (hinter Vertäfelungen)

**Zone D — Mast/Rigg (Segelyachten):**
- Windgeber, Masttoplaterne
- Extrem lange Drop-Kabel (Mastlänge bis 25m!)
- ACHTUNG: Max. Drop-Kabel = 6m → Lösung: Backbone bis Mastfuß führen, dort T-Stück, dann separates Drop-Kabel im Mast mit N2K-Repeater/Extender oder proprietärer Mastkabel-Lösung
- Alternative: Windgeber mit eigenem NMEA-0183-Ausgang, am Mastfuß Gateway auf N2K

**Zone E — Bug:**
- Bugstrahlruder-Steuerung, Ankerwinde, Ankerlaterne
- Lange Backbone-Strecke (bei 15m-Yacht ca. 12–15m vom Steuerstand)
- Spannungsabfall berechnen!

#### 2.7.3 Powerkonzept

**Zentrale Stromversorgung (empfohlen):**
- Ein dedizierter Stromversorger (Power-T, Power Inserter) speist 12V in den Backbone
- Absicherung: 3A Sicherung (Micro-C) oder 5A (Mini-C)
- Position: möglichst mittig im Backbone (minimaler Spannungsabfall)

**Dezentrale Stromversorgung:**
- Mehrere Power Inserter bei langen Backbones
- ACHTUNG: Potenzialausgleich beachten! Alle Inserter müssen am selben Batterie-Minuspol hängen
- Nie Inserter an verschiedenen Batteriebänken ohne galvanische Trennung

**Sicherungskonzept:**

| Backbone-Typ | Sicherung | Kabelquerschnitt | Max. Strom |
|--------------|-----------|-------------------|-----------|
| Micro-C (leicht) | 3A flink | 0,82 mm² | 2,5 A |
| Micro-C (standard) | 5A flink | 0,82 mm² | 2,5 A (begrenzt durch Kabel) |
| Mini-C / DeviceNet | 5A flink | 1,31 mm² | 4,0 A |
| Mid-C | 8A flink | 2,08 mm² | 6,0 A |

#### 2.7.4 EMV-Maßnahmen (Elektromagnetische Verträglichkeit)

- Backbone-Kabel immer geschirmt verwenden (360°-Schirmung)
- Mindestabstand zu Stromkabeln: 10 cm (Gleichstrom), 30 cm (Wechselstrom/Inverter)
- Mindestabstand zu Sendern (VHF, SSB, Radar): 1m
- Schirm einseitig erden (üblicherweise am Power-Inserter-Ende auf Bordmasse)
- Ferritkerne an Motorsteuerungs-Drop-Kabeln (EMV vom Anlasser/Lichtmaschine)
- CAN-Bus-Leitungen NICHT parallel zu PWM-gesteuerten Leitungen (LED-Dimmer, Motorcontroller)

---

## 3. Typenübersicht

### 3.1 Systematik der NMEA-2000-Netzwerkkomponenten

#### 3.1.1 Klassifikation nach Funktion

**Typ A — Passive Infrastruktur (Backbone-Komponenten)**

| Komponente | Funktion | Varianten |
|------------|----------|-----------|
| Backbone-Kabel | Daten- und Stromtransport | Micro-C, Mini-C, Mid-C; Längen 0,5–25m |
| T-Stück (Tee) | Backbone-Abzweigung für Drop | Male-Female-Female, Female-Male-Male |
| Drop-Kabel | Verbindung T-Stück ↔ Gerät | Micro-C, 0,3–6m |
| Terminator (Male) | Abschlusswiderstand 120Ω | Am offenen Male-Ende |
| Terminator (Female) | Abschlusswiderstand 120Ω | Am offenen Female-Ende |
| Power-T / Inserter | 12V-Einspeisung in Backbone | Mit/ohne Sicherung integriert |
| Verlängerungskabel | Backbone-Verlängerung | Micro-C Male-Female, diverse Längen |
| Adapter | Steckersystem-Wechsel | Micro-C ↔ DeviceNet, Micro-C ↔ Mini-C |

**Typ B — Aktive Netzwerkgeräte (Gateways und Bridges)**

| Komponente | Funktion | Richtung |
|------------|----------|----------|
| NMEA-0183-zu-N2K-Gateway | Protokollkonvertierung | 0183 → N2K, N2K → 0183, bidirektional |
| WiFi-Gateway / Multiplexer | Drahtloser Datenzugang | N2K/0183 → WiFi, bidirektional |
| Ethernet-Gateway | IP-Netzwerk-Anbindung | N2K ↔ Ethernet (TCP/UDP) |
| USB-Gateway | PC/Server-Anbindung | N2K ↔ USB (Diagnose, SignalK) |
| SeaTalk-Gateway | Raymarine-Legacy-Anbindung | SeaTalk1 ↔ N2K |
| SignalK-Server | Offene Datenplattform | N2K/0183 → JSON/REST/WebSocket |
| NMEA OneNet Bridge | CAN ↔ Ethernet | N2K ↔ OneNet |

**Typ C — Sensoren und Geber mit N2K-Interface**

| Sensor | Messgröße | PGN |
|--------|-----------|-----|
| GPS-Empfänger | Position, COG, SOG | 129025, 129026, 129029 |
| Kompass (Fluxgate) | Heading magnetisch/wahr | 127250 |
| Windgeber | Windgeschwindigkeit/-winkel | 130306 |
| Echolot/Tiefengeber | Wassertiefe | 128267 |
| Log/Speedgeber | Fahrt durchs Wasser | 128259 |
| Tankgeber (kapazitiv/Ultraschall) | Füllstand Kraftstoff/Wasser | 127505 |
| Batteriemonitor | Spannung, Strom, SoC | 127508 |
| Temperatursensor | Wasser, Luft, Motor | 130312 |
| Barometer | Luftdruck | 130314 |
| Neigungssensor (IMU) | Pitch, Roll, Yaw | 127257 |
| Ruderlagegeber | Ruderwinkel | 127245 |
| Motor-Interface | Drehzahl, Temp, Öldruck | 127488, 127489 |
| AIS-Transponder | AIS-Meldungen | 129038, 129039 |

**Typ D — Diagnose- und Monitoring-Werkzeuge**

| Werkzeug | Funktion | Typ |
|----------|----------|-----|
| Maretron N2KAnalyzer | PC-Software, PGN-Decode, Logging | Software (Win) |
| Actisense NMEA Reader | PGN-Decode, Diagnose | Software (Win/Mac) |
| Yacht Devices Voyage Recorder | Datenaufzeichnung auf SD | Hardware |
| CANable / PEAK PCAN-USB | Generischer CAN-Bus-Adapter | Hardware + Software |
| Maretron N2KView | Grafisches Monitoring | Software (Win) |
| OpenSkipper | Open-Source-N2K-Reader | Software (Win/Linux) |
| CANboat (Open Source) | PGN-Dekodierung, Logging | Software (Linux/Mac) |
| SignalK Dashboard | Web-basiertes Monitoring | Software (Browser) |

### 3.2 Klassifikation nach Bootsklasse

#### 3.2.1 Netzwerk-Ausbaustufen

**Stufe 1 — Basis (8–10m Segelyacht / Trailer-Motorboot):**

```
Geräte: 4–8
Backbone: 3–6m Micro-C
Drop-Kabel: 3–6 Stück, je 0,5–2m
Terminatoren: 2× Micro-C
Power: 1× Power-T
Gateway: 0–1 (optional WiFi)
Budget: 600–1.800 €

Typische Konfiguration:
  GPS-Antenne → N2K
  Windgeber → N2K (Segler)
  Echolot → N2K
  Kartenplotter (1×) → N2K
  Motorinterface → N2K (wenn Motor N2K-fähig)
  Optional: WiFi-Gateway für Tablet
```

**Stufe 2 — Mittel (10–14m Fahrtenyacht / Motoryacht):**

```
Geräte: 10–18
Backbone: 8–15m Micro-C oder Mini-C
Drop-Kabel: 8–15 Stück, je 0,5–4m
Terminatoren: 2× 
Power: 1–2× Power-Inserter
Gateways: 1–2 (NMEA 0183 + WiFi)
Budget: 2.000–6.000 €

Typische Konfiguration:
  GPS-Antenne → N2K
  Windgeber → N2K
  Echolot → N2K
  Kartenplotter (2×, Cockpit + Navi-Tisch) → N2K
  Autopilot-Computer → N2K
  Motorinterface → N2K
  Batteriemonitor → N2K
  Tankgeber Fuel (2×) → N2K
  Tankgeber Wasser (1×) → N2K
  AIS-Transponder → N2K
  WiFi-Gateway → N2K + Tablet
  NMEA 0183 Gateway → Legacy-Geräte
```

**Stufe 3 — Erweitert (14–20m Blauwasseryacht):**

```
Geräte: 15–30
Backbone: 15–25m Mini-C oder Mid-C
Drop-Kabel: 15–25 Stück
Terminatoren: 2×
Power: 2–3× Power-Inserter
Gateways: 2–4 (0183, WiFi, Ethernet, SignalK)
Budget: 5.000–15.000 €

Zusätzlich zu Stufe 2:
  Fluxgate-Kompass → N2K
  Neigungssensor (IMU) → N2K
  Ruderlagegeber → N2K
  Tankgeber Fäkalien → N2K
  Tankgeber Grauwasser → N2K
  Barometer → N2K
  Temperatursensoren (Motor, Abgas, Seekiste) → N2K
  Victron Cerbo GX → N2K (Energiemanagement)
  SignalK Server (Raspberry Pi) → USB-Gateway
  Radar → Ethernet (mit N2K-Steuerung)
  2. Motorinterface (wenn Doppelmotor)
```

**Stufe 4 — Professionell (20m+ Motoryacht / Superyacht):**

```
Geräte: 30–100+
Backbone: Dual-Backbone oder Backbone + OneNet
Drop-Kabel: 30–80+ Stück
Terminatoren: 2× pro Backbone-Segment
Power: 3–6× Power-Inserter mit redundanter Versorgung
Gateways: 5–10+ (0183, WiFi, Ethernet, SignalK, proprietär)
Budget: 15.000–120.000 €

Zusätzlich zu Stufe 3:
  Dual-Backbone (Redundanz, Maschinenraum + Brücke)
  NMEA OneNet Ethernet-Backbone für Video/Radar
  Mehrere GPS-Empfänger (Primär + Backup)
  Dynamic Positioning Sensoren
  Beleuchtungssteuerung über N2K
  HVAC-Integration
  Überwachungskameras (IP) über OneNet
  Zentrale Monitoring-Station (Maretron N2KView oder gleichwertig)
  Redundante Server (SignalK + proprietär)
  Satellitenkommunikation-Integration
```

---

## 4. Produktlinien und Spezifikationen

### 4.1 Actisense

**Firmenprofil:** Britischer Hersteller (Poole, Dorset), gegründet 2002, spezialisiert auf NMEA-Gateways, -Diagnostik und -Multiplexer. Marktführer bei professionellen Gateways.

#### 4.1.1 Gateways und Multiplexer

**NGW-1 — NMEA 2000 Gateway:**

| Parameter | Wert |
|-----------|------|
| Funktion | Bidirektionaler NMEA 0183 ↔ NMEA 2000 Gateway |
| NMEA 0183 | 1× Eingang (Listener), 1× Ausgang (Talker), RS-422 |
| NMEA 2000 | Micro-C (M12), LEN 1 |
| Baudrate 0183 | 4.800 / 38.400 Baud (konfigurierbar) |
| PGN-Unterstützung | 80+ PGN ↔ 40+ Sentences |
| Konfiguration | PC-Software (Actisense NMEA Reader) |
| Stromversorgung | Über N2K-Bus (12V, 50 mA) |
| Abmessungen | 100 × 55 × 25 mm |
| Schutzklasse | IP54 |
| Temperaturbereich | -15°C bis +55°C |
| Preis (UVP) | 195–230 € |

**NGT-1 — NMEA 2000 USB Gateway:**

| Parameter | Wert |
|-----------|------|
| Funktion | N2K ↔ USB-Adapter für PC/Mac |
| USB | USB 2.0 Full Speed |
| NMEA 2000 | Micro-C, LEN 1 |
| Software-Kompatibilität | Actisense NMEA Reader, Maretron N2KAnalyzer, CANboat, SignalK, OpenCPN |
| Treiber | Windows, macOS, Linux |
| Durchsatz | Alle PGN, bidirektional, Echtzeit |
| Stromversorgung | Über USB |
| Abmessungen | 90 × 50 × 20 mm |
| Preis (UVP) | 210–260 € |

**W2K-1 — WiFi Gateway:**

| Parameter | Wert |
|-----------|------|
| Funktion | N2K + NMEA 0183 → WiFi |
| NMEA 2000 | Micro-C, LEN 2 |
| NMEA 0183 | 2× Eingang, 1× Ausgang, RS-422 |
| WiFi | 802.11 b/g/n, 2,4 GHz, AP + Client |
| Protokolle | TCP/UDP Server (Port 2000, 10110), HTTP API |
| Max. Clients | 7 gleichzeitig |
| Konfiguration | Web-Interface, iOS/Android App |
| Stromversorgung | 9–32V DC (eigenes Netzteil) + N2K |
| Abmessungen | 110 × 70 × 30 mm |
| Schutzklasse | IP42 (Innenraum) |
| Preis (UVP) | 390–470 € |

**EMU-1 — Engine Monitoring Unit:**

| Parameter | Wert |
|-----------|------|
| Funktion | Analoge Motorsignale → NMEA 2000 |
| Eingänge | 9 analoge Eingänge (Temperatur, Druck, Spannung) + RPM |
| NMEA 2000 | Micro-C, LEN 2 |
| Kalibrierung | PC-Software, individuelle Skalierung pro Kanal |
| Motortypen | Yanmar, Volvo Penta, Nanni, Beta, etc. (vorkonfiguriert) |
| Preis (UVP) | 380–450 € |

#### 4.1.2 Diagnose-Werkzeuge

**PRO-BUF-1 — Professional NMEA 2000 Buffer:**

| Parameter | Wert |
|-----------|------|
| Funktion | Puffer/Verteiler für NMEA 0183-Signale |
| Eingänge | 4× NMEA 0183 (RS-422) |
| Ausgänge | 7× NMEA 0183 (isoliert, RS-422) |
| Funktionen | Signal-Isolierung, Pegelregenerierung, Multiplexing |
| Preis (UVP) | 310–380 € |

### 4.2 Yacht Devices

**Firmenprofil:** Lettischer Hersteller (Riga), gegründet 2010, bekannt für kompakte, kostengünstige NMEA-2000-Gateways und -Sensoren. Starke DIY- und Open-Source-Community-Anbindung.

#### 4.2.1 Gateways

**YDWG-02 — WiFi Gateway NMEA 2000:**

| Parameter | Wert |
|-----------|------|
| Funktion | N2K → WiFi (TCP/UDP NMEA 0183 oder RAW N2K) |
| NMEA 2000 | Micro-C (DeviceNet Male), LEN 1 |
| WiFi | 802.11 b/g/n, 2,4 GHz, AP (Standard) + Client |
| Protokolle | TCP-Server (Port 6464), UDP-Broadcast, NMEA 0183 Output |
| Max. Clients | 6–8 gleichzeitig |
| PGN-Konvertierung | 60+ PGN → NMEA 0183 Sentences |
| Konfiguration | Web-Interface |
| Stromversorgung | Über N2K-Bus, 50 mA |
| Abmessungen | 70 × 30 × 20 mm (extrem kompakt) |
| Schutzklasse | IP42 |
| Preis (UVP) | 165–210 € |
| Besonderheit | Preis-Leistungs-Sieger, sehr populär bei DIY-Community |

**YDNU-02 — USB Gateway NMEA 2000:**

| Parameter | Wert |
|-----------|------|
| Funktion | N2K ↔ USB für PC/Mac/Linux/Raspberry Pi |
| NMEA 2000 | Micro-C, LEN 1 |
| USB | USB 2.0 |
| Protokoll | RAW CAN-Frames + NMEA 0183 Konvertierung |
| Software | CANboat, SignalK, OpenCPN, Actisense NMEA Reader (kompatibel) |
| Treiber | Windows (CDC), macOS, Linux (nativ) |
| Preis (UVP) | 95–130 € |
| Besonderheit | Günstigste USB-Gateway-Option, ideal für SignalK/Raspberry Pi |

**YDNR-02 — NMEA 0183 ↔ NMEA 2000 Gateway:**

| Parameter | Wert |
|-----------|------|
| Funktion | Bidirektionaler 0183 ↔ N2K Gateway |
| NMEA 0183 | 2× Eingang, 2× Ausgang, RS-422 |
| NMEA 2000 | Micro-C, LEN 1 |
| Baudrate | 4.800 / 38.400 Baud |
| Konfiguration | Web-Interface (via WiFi-Gateway) oder USB |
| Preis (UVP) | 135–175 € |

#### 4.2.2 Sensoren

**YDTC-13 — Thermoelement-Interface:**

| Parameter | Wert |
|-----------|------|
| Funktion | Temperaturmessung → N2K |
| Eingänge | 1× Typ-K Thermoelement |
| Bereich | -50°C bis +1100°C |
| Genauigkeit | ±2°C |
| PGN | 130312, 130316 |
| Preis (UVP) | 85–110 € |

**YDBM-01 — Batteriemonitor:**

| Parameter | Wert |
|-----------|------|
| Funktion | Batteriespannung/-strom → N2K |
| Spannung | 7–38V DC |
| Strom | Via externem Shunt (500A typ.) |
| PGN | 127508 |
| Preis (UVP) | 95–125 € |

**YDVR-04 — Voyage Recorder:**

| Parameter | Wert |
|-----------|------|
| Funktion | N2K-Datenaufzeichnung auf SD-Karte |
| Speicher | microSD bis 32 GB |
| Format | NMEA 0183 Sentences (konvertiert) oder RAW N2K |
| Aufzeichnungsdauer | >10.000 Stunden bei typischer Datenmenge |
| Wiedergabe | PC-Software, kompatibel mit OpenCPN |
| Preis (UVP) | 125–160 € |

### 4.3 Maretron

**Firmenprofil:** US-amerikanischer Hersteller (Phoenix, Arizona), gegründet 2001, Premium-Segment. Vollständiges N2K-Ökosystem von Backbone über Sensoren bis Monitoring-Software.

#### 4.3.1 Backbone-Komponenten

**Micro-C Backbone-System:**

| Komponente | Artikelnummer | Länge/Typ | Preis (UVP) |
|------------|--------------|-----------|-------------|
| Backbone-Kabel | NM-BG1-xx | 0,5m–25m | 25–180 € |
| T-Stück | NM-BT1 | Male-Female-Female | 38–48 € |
| Power-T | NM-PT1 | Mit Sicherungshalter | 55–68 € |
| Terminator Male | NM-TM1 | 120 Ω | 22–28 € |
| Terminator Female | NM-TF1 | 120 Ω | 22–28 € |
| Drop-Kabel | NM-NG1-xx | 0,3m–6m, Micro-C | 20–65 € |

**Mid-C Backbone-System (für große Yachten):**

| Komponente | Artikelnummer | Spezifikation | Preis (UVP) |
|------------|--------------|---------------|-------------|
| Mid-Kabel | NM-BG2-xx | 2,08 mm², bis 200m Backbone | 45–320 € |
| Mid-T-Stück | NM-BT2 | Robuster als Micro-C | 65–85 € |
| Mid-Terminator | NM-TM2/TF2 | 120 Ω, vergoldete Kontakte | 35–45 € |

#### 4.3.2 Sensoren und Interfaces

**DSM410 — Multi-Function Vessel Monitoring Color Display:**

| Parameter | Wert |
|-----------|------|
| Display | 5,7" TFT, 640×480, 1.000 nits |
| Funktion | Anzeige aller N2K-Daten, konfigurierbare Seiten |
| Alarme | Konfigurierbare Schwellwerte, akustisch + visuell |
| NMEA 2000 | Micro-C, LEN 4 |
| Preis (UVP) | 1.600–2.100 € |

**TMP100 — Temperatursensor:**

| Parameter | Wert |
|-----------|------|
| Bereich | -40°C bis +90°C (Umgebung), -40°C bis +300°C (Oberfl.) |
| Genauigkeit | ±0,5°C |
| Anschluss | Micro-C |
| LEN | 1 |
| Preis (UVP) | 240–310 € |

**FPM100 — Fuel Flow Monitor:**

| Parameter | Wert |
|-----------|------|
| Messbereich | 3–380 L/h |
| Genauigkeit | ±1% |
| PGN | 127489 (Verbrauch), 127497 (Trip) |
| Preis (UVP) | 680–850 € |

**USB100 — USB Gateway:**

| Parameter | Wert |
|-----------|------|
| Funktion | N2K ↔ USB für PC (N2KAnalyzer, N2KView) |
| Treiber | Windows, macOS |
| Preis (UVP) | 310–380 € |

#### 4.3.3 Software

**N2KAnalyzer:**
- PGN-Dekodierung aller Standard- und herstellerspezifischen PGN
- Busauslastungs-Analyse
- Fehlerrate-Monitoring (Error Frames)
- Datenlogging mit Zeitstempel
- Kostenlos mit Maretron USB-Gateway

**N2KView:**
- Grafisches Vessel-Monitoring-System
- Konfigurierbare Dashboards (Instrumente, Tanks, Motor, Navigation)
- Alarmmanagement mit E-Mail-Benachrichtigung
- Historische Datenauswertung
- Lizenz: ca. 390–550 € (je nach Funktionsumfang)

### 4.4 Digital Yacht

**Firmenprofil:** Britischer Hersteller (Hampshire), gegründet 2010, spezialisiert auf WiFi-Integration, AIS und digitale Vernetzung. Starker Fokus auf Tablet/Smartphone-Integration.

#### 4.4.1 WiFi-Gateways

**iKonvert — NMEA 2000 zu USB/WiFi Gateway:**

| Parameter | Wert |
|-----------|------|
| Varianten | USB-Version, WiFi-Version |
| NMEA 2000 | Micro-C, bidirektional |
| WiFi | 802.11 b/g/n, AP + Client |
| Kompatibilität | OpenCPN, Expedition, iSailor, Navionics, SignalK |
| Preis (UVP) | USB: 170–210 €, WiFi: 280–340 € |

**NavLink2 — NMEA to WiFi Server:**

| Parameter | Wert |
|-----------|------|
| NMEA 0183 | 2× Eingang (RS-422), 1× Ausgang |
| WiFi | 802.11 b/g/n, AP + Client |
| Protokoll | TCP-Server (10110), UDP |
| Max. Clients | 8 |
| Besonderheit | Kompakt, günstig, weit verbreitet |
| Preis (UVP) | 180–240 € |

**Aqua Pro — Marine WiFi Router + NMEA Multiplexer:**

| Parameter | Wert |
|-----------|------|
| WiFi | Dual-Band 802.11ac (WiFi 5), bis 867 Mbit/s |
| NMEA 2000 | Integrierter Gateway |
| NMEA 0183 | 2× Eingang |
| Ethernet | 4× LAN-Ports |
| Besonderheit | Kombination aus Internet-Router und NMEA-Gateway |
| Preis (UVP) | 580–720 € |

### 4.5 Navico-Gruppe (Simrad, B&G, Lowrance)

**Konzernstruktur:** Navico (gehört zu Brunswick Corp.) vereint die Marken Simrad (professionelle Schifffahrt), B&G (Segel), Lowrance (Freizeit/Angeln). Alle nutzen gemeinsame Netzwerk-Infrastruktur.

#### 4.5.1 Backbone-Kits

**Simrad/B&G/Lowrance N2K Starter-Kit:**

| Inhalt | Spezifikation |
|--------|--------------|
| Backbone-Kabel | 4,5m Micro-C |
| T-Stücke | 4× |
| Drop-Kabel | 2× 2m |
| Terminatoren | 2× (Male + Female) |
| Power-T | 1× |
| Preis (UVP) | 180–240 € |

**SimNet-zu-N2K-Adapter:**

Ältere Simrad/B&G-Geräte verwenden das proprietäre SimNet (physikalisch kompatibel mit Micro-C, aber anderer Stecker). Adapter sind erhältlich:

| Adapter | Funktion | Preis |
|---------|----------|-------|
| SimNet-zu-Micro-C Male | SimNet-Gerät an N2K-Backbone | 25–35 € |
| SimNet-zu-Micro-C Female | N2K-Gerät an SimNet-Backbone | 25–35 € |

#### 4.5.2 Gateways

**Navico NMEA 0183 Gateway:**

| Parameter | Wert |
|-----------|------|
| Funktion | Bidirektional 0183 ↔ N2K |
| NMEA 0183 | 2× Eingang, 1× Ausgang |
| NMEA 2000 | Micro-C / SimNet |
| Preis (UVP) | 140–190 € |

**B&G H5000 — Segelprozessor:**

| Parameter | Wert |
|-----------|------|
| Funktion | Datenverarbeitung für Segler (TWS, TWA, VMG, Laylines) |
| NMEA 2000 | Integriert |
| NMEA 0183 | 4× Eingang, 3× Ausgang |
| Ethernet | 1× für MFD-Netzwerk |
| Besonderheit | Berechnet True Wind, VMG, Polar-Performance |
| Preis (UVP) | 1.200–1.600 € |

### 4.6 Weitere relevante Hersteller

#### 4.6.1 Garmin

**Backbone-Kits und Sensoren im Garmin-Ökosystem:**

| Produkt | Funktion | Preis (UVP) |
|---------|----------|-------------|
| NMEA 2000 Backbone/Drop-Kabel | Standard Micro-C | 15–90 € |
| NMEA 2000 Starter-Kit | Backbone + T-Stücke + Terminatoren | 120–160 € |
| GNT 10 | Gateway 0183 ↔ N2K | 180–240 € |
| GST 43 | Speed/Temperature Sensor N2K | 90–130 € |
| GDT 43 | Depth/Temperature Sensor N2K | 90–130 € |
| GWS 10 | Wireless Wind Sensor | 380–480 € |
| GMI 20 | Instrumentendisplay N2K | 380–480 € |

#### 4.6.2 Raymarine

**SeaTalkng (Raymarine-Variante von NMEA 2000):**

SeaTalkng ist physikalisch und elektrisch kompatibel mit NMEA 2000 (Micro-C-Stecker, gleiches CAN-Protokoll), verwendet aber einen eigenen Markennamen und eigene Kabelfarben:

| SeaTalkng | NMEA 2000 (DeviceNet) | Funktion |
|-----------|----------------------|----------|
| Blau | Weiß | CAN_H |
| Weiß | Blau | CAN_L |
| Schwarz | Schwarz | GND |
| Rot | Rot | +12V |
| Schirm | Schirm | Shield |

**ACHTUNG:** SeaTalkng-Kabel und N2K-Kabel dürfen gemischt werden, wenn die Farbkodierung beachtet wird. Standardmäßig sind die Stecker kompatibel (M12 5-polig).

**SeaTalkng ist NICHT dasselbe wie SeaTalk1** (älteres proprietäres RS-485-basiertes Protokoll von Autohelm/Raymarine).

| Produkt | Funktion | Preis (UVP) |
|---------|----------|-------------|
| SeaTalkng Backbone-Kabel | Micro-C, diverse Längen | 20–120 € |
| E22158 SeaTalk1 ↔ ng Konverter | Legacy-Anbindung | 95–130 € |
| E70196 SeaTalkng ↔ 0183 Gateway (VHF) | Bidirektional | 140–190 € |
| A06049 SeaTalkng Power Cable | 12V-Einspeisung | 25–35 € |

#### 4.6.3 Furuno

| Produkt | Funktion | Preis (UVP) |
|---------|----------|-------------|
| IF-NMEAFI | NMEA 0183 ↔ N2K Gateway | 220–290 € |
| IF-NMEA2K2 | Dual-Port NMEA 2000 Interface | 310–400 € |
| Backbone-Kabel (Micro-C) | Standard Micro-C | 25–150 € |

#### 4.6.4 Victron Energy

Victron Energy ist kein klassischer Marine-Elektronik-Hersteller, aber durch den Cerbo GX ein wichtiger Akteur in der N2K-Integration:

| Produkt | Funktion | Preis (UVP) |
|---------|----------|-------------|
| Cerbo GX | Energiemanagement-Hub mit N2K-Integration | 250–320 € |
| VE.Can-zu-NMEA2000 Kabel | Victron-Bus ↔ N2K-Backbone | 30–45 € |
| GX Tank 140 | 4-Kanal-Tankgeber → N2K/VRM | 110–150 € |
| SmartShunt | Batteriemonitor → Cerbo GX → N2K | 75–95 € |

---

## 5. Hersteller-Datenbank

### 5.1 Actisense

| Feld | Wert |
|------|------|
| Firma | Active Research Ltd. (Handelsname: Actisense) |
| Gründung | 2002 |
| Hauptsitz | Poole, Dorset, Vereinigtes Königreich |
| Mitarbeiter | 25–40 (geschätzt) |
| Kernkompetenz | NMEA-Gateways, -Diagnostik, -Multiplexer |
| Segment | Mid-Range bis Professional |
| Qualitätsniveau | Hoch, Referenz für Gateway-Zuverlässigkeit |
| Garantie | 3 Jahre |
| Zertifizierungen | NMEA 2000 Certified, CE, FCC |
| Website | www.actisense.com |
| Support | E-Mail, umfangreiche Knowledge Base, Firmware-Downloads |
| AYDI-Bewertung | Referenz-Hersteller für Gateways. Solide Firmware, zuverlässige Konvertierung. NGT-1 de-facto-Standard für PC/SignalK-Anbindung. W2K-1 WiFi-Gateway leistungsfähig aber teurer als Alternativen. |
| Stärken | Firmware-Qualität, PGN-Abdeckung, professioneller Support |
| Schwächen | Höherer Preis als Yacht Devices, keine eigenen Sensoren |

### 5.2 Yacht Devices

| Feld | Wert |
|------|------|
| Firma | Yacht Devices Ltd. |
| Gründung | 2010 |
| Hauptsitz | Riga, Lettland |
| Mitarbeiter | 10–20 (geschätzt) |
| Kernkompetenz | Kompakte, kostengünstige N2K-Gateways und -Sensoren |
| Segment | Budget bis Mid-Range |
| Qualitätsniveau | Gut, gelegentlich Firmware-Bugs bei neuen Produkten |
| Garantie | 2 Jahre |
| Zertifizierungen | NMEA 2000 Certified, CE |
| Website | www.yachtd.com |
| Support | E-Mail, Forum, aktive Community |
| AYDI-Bewertung | Preis-Leistungs-Sieger. YDWG-02 WiFi-Gateway extrem populär. YDNU-02 USB-Gateway ideal für SignalK/Raspberry Pi. Firmware-Updates regelmäßig, Community-getrieben. |
| Stärken | Preis-Leistung, Kompaktheit, breites Sortiment, Community |
| Schwächen | Dokumentation teilweise lückenhaft, IP-Schutzklasse niedrig (IP42) |

### 5.3 Maretron

| Feld | Wert |
|------|------|
| Firma | Maretron, LLC |
| Gründung | 2001 |
| Hauptsitz | Phoenix, Arizona, USA |
| Mitarbeiter | 20–35 (geschätzt) |
| Kernkompetenz | Premium-N2K-Ökosystem (Backbone, Sensoren, Monitoring) |
| Segment | Premium / Professional / Superyacht |
| Qualitätsniveau | Sehr hoch, Referenz für Superyacht-Installationen |
| Garantie | 3 Jahre (Backbone), 2 Jahre (Elektronik) |
| Zertifizierungen | NMEA 2000 Certified, CE, FCC, UL |
| Website | www.maretron.com |
| Support | Telefon + E-Mail, technische Applikationsberatung |
| AYDI-Bewertung | Premium-Hersteller, teuerste Lösung, aber höchste Qualität. N2KView Monitoring-Software de-facto-Standard für professionelle Installationen. Backbone-Qualität ausgezeichnet. |
| Stärken | Qualität, vollständiges Ökosystem, professionelle Monitoring-Software |
| Schwächen | Hoher Preis (2–3× Yacht Devices), geschlossenes Ökosystem |

### 5.4 Digital Yacht

| Feld | Wert |
|------|------|
| Firma | Digital Yacht Ltd. |
| Gründung | 2010 |
| Hauptsitz | Hampshire, Vereinigtes Königreich |
| Mitarbeiter | 15–25 (geschätzt) |
| Kernkompetenz | WiFi-Gateways, AIS, digitale Vernetzung |
| Segment | Mid-Range |
| Qualitätsniveau | Gut |
| Garantie | 2 Jahre |
| Zertifizierungen | NMEA 2000 Certified, CE, FCC |
| Website | www.digitalyacht.co.uk |
| Support | E-Mail, gute Dokumentation |
| AYDI-Bewertung | Starker Fokus auf Tablet/App-Integration. NavLink2 weit verbreitet. Aqua Pro interessante Kombination aus Router und NMEA-Gateway. |
| Stärken | WiFi-Integration, Tablet-Kompatibilität, AIS-Produkte |
| Schwächen | Weniger Sensoren als Maretron/Yacht Devices |

### 5.5 Navico (Simrad/B&G/Lowrance)

| Feld | Wert |
|------|------|
| Firma | Navico Group (Teil von Brunswick Corporation) |
| Gründung | Navico 2006 (Zusammenschluss Simrad + Lowrance), Brunswick-Übernahme 2021 |
| Hauptsitz | Tulsa, Oklahoma, USA (Lowrance) / Egersund, Norwegen (Simrad) |
| Mitarbeiter | 2.000+ (global, alle Marken) |
| Kernkompetenz | MFDs, Echolote, Autopiloten, Radar — mit N2K-Backbone |
| Segment | Alle (Lowrance=Budget, B&G=Segel, Simrad=Premium) |
| Qualitätsniveau | Gut bis sehr gut |
| Garantie | 2 Jahre |
| Zertifizierungen | NMEA 2000 Certified, CE, FCC |
| Website | www.simrad-yachting.com, www.bandg.com, www.lowrance.com |
| AYDI-Bewertung | Größter Konzern im Marine-Elektronik-Bereich. SimNet/N2K-Backbone-Kits günstig und zuverlässig. B&G H5000 ist Referenz für Regattasegler. Eigene Gateways funktional, aber nicht so flexibel wie Actisense. |
| Stärken | Breites Sortiment, Integration mit eigenen MFDs, Preis-Leistung |
| Schwächen | Proprietäre Tendenzen (SimNet-Ära), Gateway-Funktionalität begrenzt |

### 5.6 Victron Energy

| Feld | Wert |
|------|------|
| Firma | Victron Energy B.V. |
| Gründung | 1975 |
| Hauptsitz | Almere-Haven, Niederlande |
| Mitarbeiter | 500+ |
| Kernkompetenz | Energiemanagement (Wechselrichter, Ladegeräte, Batteriemonitore) |
| Segment | Mid-Range bis Professional |
| Qualitätsniveau | Sehr gut |
| Garantie | 5 Jahre |
| Zertifizierungen | CE, FCC, diverse marine Zertifizierungen |
| Website | www.victronenergy.com |
| AYDI-Bewertung | Kein klassischer N2K-Hersteller, aber durch Cerbo GX de-facto-Standard für Energie-Integration in N2K-Netzwerke. Offene API (VRM Portal), SignalK-Plugin verfügbar. Exzellente Dokumentation. |
| Stärken | Energie-Integration, offene API, VRM-Cloud, SignalK-Kompatibilität |
| Schwächen | Kein vollständiges N2K-Sensorprogramm, VE.Can ≠ N2K (benötigt Adapter) |

### 5.7 Open-Source / Community

| Feld | Wert |
|------|------|
| Projekt | SignalK (signalk.org) |
| Gründung | 2014 |
| Lizenz | Apache 2.0 |
| Kernkompetenz | Offenes Marines Datenformat + Server |
| Community | 5.000+ aktive Nutzer (geschätzt), 200+ Plugins |
| Plattform | Node.js auf Raspberry Pi, Linux, macOS, Windows |
| AYDI-Bewertung | Wichtigste Open-Source-Plattform für marine Datenvernetzung. Raspberry Pi + SignalK + Yacht Devices YDNU-02 ist die populärste DIY-Lösung. Plugin-Ökosystem wächst stetig. Für professionelle Installationen als Ergänzung (nicht Ersatz) zu N2K empfohlen. |
| Stärken | Kostenlos, erweiterbar, aktive Community, herstellerunabhängig |
| Schwächen | Keine NMEA-Zertifizierung, Stabilität abhängig von Hardware/Plugins, kein kommerzieller Support |

---

## 6. Fehlerbild-Atlas

### 6.1 FB-N2K-01: Sporadische Datenausfälle einzelner Geräte

| Feld | Beschreibung |
|------|-------------|
| **Symptom** | Ein oder mehrere Geräte zeigen zeitweise „Keine Daten" oder „---" an. Ausfälle treten unregelmäßig auf, oft unter Motorlauf oder bei Seegang. |
| **Betroffene Geräte** | Typischerweise Geräte am Ende des Backbones oder mit langen Drop-Kabeln |
| **Häufigkeit** | Sehr häufig (35% aller N2K-Probleme) |
| **Ursache 1** | Lose Steckverbindung am Micro-C-Stecker (Vibrationen, mangelhaftes Einrasten) |
| **Ursache 2** | Korrosion an Steckerkontakten (Salzluft, Feuchtigkeit) |
| **Ursache 3** | Spannungsabfall am Backbone-Ende bei hoher Buslast |
| **Ursache 4** | EMV-Störungen durch Lichtmaschine, Inverter oder VHF-Sender |
| **Diagnose** | 1. Alle Stecker prüfen (Sitz, Korrosion). 2. Spannung am betroffenen Gerät messen (>9V?). 3. Fehler-Frame-Rate mit N2KAnalyzer prüfen. 4. EMV-Quelle identifizieren (Motor an/aus vergleichen). |
| **Lösung** | 1. Stecker reinigen (Kontaktspray), nachziehen. 2. Bei Korrosion: Stecker ersetzen. 3. Bei Spannungsabfall: Power-Inserter näher am Gerät. 4. Bei EMV: Ferritkerne, Kabelführung ändern. |
| **Kosten** | 0–50 € (Reinigung) / 30–150 € (Stecker/Kabel ersetzen) / 50–200 € (Power-Inserter) |
| **AYDI-Confidence** | visual_medium (Steckerkorrosion sichtbar), measured (Spannungsmessung) |

### 6.2 FB-N2K-02: Komplett-Ausfall des Netzwerks

| Feld | Beschreibung |
|------|-------------|
| **Symptom** | Kein Gerät am N2K-Bus kommuniziert. Alle Displays zeigen „Keine Daten". |
| **Häufigkeit** | Mittel (12% aller N2K-Probleme) |
| **Ursache 1** | Fehlende oder defekte Terminierung (beide Terminatoren fehlen/defekt) |
| **Ursache 2** | Kurzschluss auf dem Backbone (Kabelbruch, Wassereintritt in Stecker) |
| **Ursache 3** | Keine Stromversorgung (Sicherung durchgebrannt, Power-Inserter defekt) |
| **Ursache 4** | CAN-Bus im Bus-Off-Zustand (zu viele Fehler, alle Controller abgeschaltet) |
| **Diagnose** | 1. Versorgungsspannung am Power-Inserter messen. 2. Sicherung prüfen. 3. Terminierungswiderstand messen (60Ω zwischen CAN_H und CAN_L). 4. Segmentweise Geräte abtrennen und Bus testen. |
| **Lösung** | Je nach Ursache: Terminatoren ersetzen, Kurzschluss lokalisieren und beheben, Sicherung/Inserter ersetzen. |
| **Kosten** | 10–50 € (Terminatoren/Sicherung) / 50–300 € (Kabelreparatur) |
| **AYDI-Confidence** | measured (Widerstandsmessung), estimated (Segmentierung) |

### 6.3 FB-N2K-03: Doppelte oder widersprüchliche Daten

| Feld | Beschreibung |
|------|-------------|
| **Symptom** | MFD zeigt zwei verschiedene Werte für gleiche Messgröße (z.B. zwei verschiedene Geschwindigkeiten). Oder: Werte springen hin und her. |
| **Häufigkeit** | Häufig (18% aller N2K-Probleme) |
| **Ursache 1** | Zwei Geräte senden dieselbe PGN (z.B. GPS im MFD + externer GPS-Empfänger) |
| **Ursache 2** | Gateway spiegelt Daten: N2K→0183→N2K-Schleife |
| **Ursache 3** | Instanz-Konflikte (z.B. zwei Tankgeber mit gleicher Instanznummer) |
| **Diagnose** | 1. PGN-Liste aller Geräte prüfen (welches Gerät sendet welche PGN?). 2. Gateway-Konfiguration auf Schleifen prüfen. 3. Instanznummern aller Sensoren gleichen Typs vergleichen. |
| **Lösung** | 1. Datenquelle am MFD priorisieren (Source-Auswahl). 2. PGN-Filter am Gateway konfigurieren. 3. Instanznummern eindeutig vergeben. 4. Unnötige Datenquellen deaktivieren. |
| **Kosten** | 0 € (Konfiguration) |
| **AYDI-Confidence** | measured (PGN-Analyse mit N2KAnalyzer) |

### 6.4 FB-N2K-04: WiFi-Gateway verliert Verbindung

| Feld | Beschreibung |
|------|-------------|
| **Symptom** | Tablet/Smartphone verliert regelmäßig Verbindung zum WiFi-Gateway. App zeigt alte oder keine Daten. Verbindung kommt nach Neuverbindung zurück. |
| **Häufigkeit** | Häufig (15% aller WiFi-bezogenen Probleme) |
| **Ursache 1** | Schwaches WiFi-Signal (Gateway unter Deck, Tablet im Cockpit, Metallrumpf als Abschirmung) |
| **Ursache 2** | WiFi-Kanalüberlappung (Marinas mit vielen WLANs) |
| **Ursache 3** | Gateway-Firmware-Bug (bekannt bei älteren YDWG-02-Versionen) |
| **Ursache 4** | Zu viele gleichzeitige Clients (Charterboot, Crew + Gäste) |
| **Diagnose** | 1. Signalstärke prüfen (WiFi Analyzer App). 2. WiFi-Kanal manuell setzen (1, 6 oder 11). 3. Firmware-Version prüfen. 4. Client-Anzahl reduzieren. |
| **Lösung** | 1. Externe WiFi-Antenne installieren. 2. Gateway-Position optimieren (höher, zentraler). 3. Firmware-Update. 4. WiFi-Kanal festlegen (kein Auto). 5. Bei Metallrumpf: Gateway mit externer Antenne im Cockpit. |
| **Kosten** | 0 € (Konfiguration) / 15–40 € (externe Antenne) / 50–200 € (Gateway-Repositionierung) |
| **AYDI-Confidence** | measured (Signalstärkemessung), estimated (Positionsoptimierung) |

### 6.5 FB-N2K-05: Motorsteuerung sendet keine Daten

| Feld | Beschreibung |
|------|-------------|
| **Symptom** | Motor-RPM, Kühlwassertemperatur, Öldruck fehlen auf dem MFD, obwohl Motor läuft und N2K-Kabel am Motorsteuergerät angeschlossen ist. |
| **Häufigkeit** | Mittel (10% aller N2K-Probleme bei Neuinstallationen) |
| **Ursache 1** | Motorsteuerung nicht für N2K konfiguriert (ab Werk deaktiviert bei manchen Herstellern) |
| **Ursache 2** | Falscher Motordaten-Gateway (z.B. Yanmar-Motor braucht Yanmar-N2K-Interface, nicht generischen Gateway) |
| **Ursache 3** | CAN-Bus-Adresskonflikt zwischen Motor-ECU und anderen Geräten |
| **Ursache 4** | Proprietäres Motor-CAN-Protokoll (nicht J1939-kompatibel) |
| **Diagnose** | 1. Motor-ECU auf N2K-Ausgang prüfen (Herstellerdokumentation). 2. PGN-Scan mit Analysesoftware. 3. Motorhersteller-Support kontaktieren. |
| **Lösung** | 1. Motor-ECU konfigurieren (Händler/Werft). 2. Herstellerspezifischen Gateway verwenden. 3. Bei proprietärem Protokoll: Actisense EMU-1 als Analogbrücke. |
| **Kosten** | 0 € (Konfiguration) / 200–500 € (Gateway) / 350–500 € (EMU-1) |
| **AYDI-Confidence** | documented (Motorhersteller-Dokumentation), measured (PGN-Scan) |

### 6.6 FB-N2K-06: Signalstörungen durch Inverter/Charger

| Feld | Beschreibung |
|------|-------------|
| **Symptom** | Datenverluste oder korrupte Daten auf dem N2K-Bus, korreliert mit Betrieb des Wechselrichters (Inverter) oder Ladegeräts. Typisch: hohe Error-Frame-Rate im CAN-Bus-Log. |
| **Häufigkeit** | Mittel (8% aller N2K-Probleme) |
| **Ursache** | EMV-Störungen durch PWM-Schaltfrequenz des Inverters/Chargers koppeln über Strom- oder Masseleitung in den CAN-Bus ein |
| **Diagnose** | 1. Inverter ein/aus → Fehlerrate vergleichen. 2. Error-Frame-Counter in N2K-Analysetool. 3. Kabelführung prüfen (N2K parallel zu Inverter-Kabeln?). |
| **Lösung** | 1. N2K-Backbone physisch von Inverter-Kabeln trennen (min. 30 cm). 2. Ferritkerne auf N2K-Power-Leitung am Power-Inserter. 3. Separate Masseleitung für N2K (direkt zur Batterie, nicht über gemeinsame Sammelschiene). 4. EMV-Filter am Inverter-Ausgang. |
| **Kosten** | 10–30 € (Ferritkerne) / 50–200 € (Kabelverlegung) / 50–100 € (EMV-Filter) |
| **AYDI-Confidence** | measured (Error-Frame-Rate), estimated (EMV-Maßnahmen) |

### 6.7 FB-N2K-07: Tankgeber zeigen falsche Füllstände

| Feld | Beschreibung |
|------|-------------|
| **Symptom** | Tankfüllstand springt, zeigt >100% oder <0%, oder weicht signifikant vom tatsächlichen Füllstand ab. Besonders bei Seegang. |
| **Häufigkeit** | Häufig (20% aller Tankgeber-Probleme) |
| **Ursache 1** | Tankgeber nicht kalibriert (ab Werk linear, Tank aber nicht rechteckig) |
| **Ursache 2** | Schwappeffekte bei Seegang (kapazitiver Geber reagiert auf Bewegung) |
| **Ursache 3** | Instanznummer falsch → MFD zeigt falschen Tank |
| **Ursache 4** | Tankform nicht im Geber hinterlegt (Schlauchtank, V-Form) |
| **Diagnose** | 1. Instanznummer und Tanktyp prüfen. 2. Bei Ruhe kalibrieren (Tank voll, halb, leer). 3. Dämpfung/Filterung am Geber oder MFD aktivieren. |
| **Lösung** | 1. Kalibierung durchführen (Herstelleranleitung). 2. Dämpfungszeit erhöhen (30–120 Sekunden). 3. Ultraschall-Geber statt kapazitiv (weniger Schwapp-empfindlich). 4. Bei Schlauchtanks: Multi-Punkt-Kalibrierung. |
| **Kosten** | 0 € (Kalibrierung) / 0 € (Konfiguration Dämpfung) / 150–400 € (Geber-Tausch) |
| **AYDI-Confidence** | measured (Kalibriermessung), estimated (Schwappeffekt-Kompensation) |

### 6.8 FB-N2K-08: Gateway-Schleife (Data Loop)

| Feld | Beschreibung |
|------|-------------|
| **Symptom** | Daten werden dupliziert, Werte erscheinen mehrfach, Bus-Auslastung steigt an, vereinzelt Bus-Überlastung mit Datenverlust. |
| **Häufigkeit** | Mittel (7% aller N2K-Probleme) |
| **Ursache** | Bidirektionaler Gateway leitet empfangene Daten zurück auf denselben Bus. Beispiel: N2K-GPS sendet PGN 129029 → Gateway konvertiert zu $GPGGA → zweiter Gateway konvertiert $GPGGA zurück zu PGN 129029 → Duplikat auf N2K-Bus |
| **Diagnose** | 1. PGN-Quellen analysieren: gleiche PGN von verschiedenen Source-Adressen? 2. Gateway-Konfigurationen auf bidirektionale Konvertierung prüfen. 3. Bus-Auslastung messen (>50% kritisch). |
| **Lösung** | 1. PGN-Filter am Gateway: nur benötigte PGN/Sentences konvertieren. 2. Einbahnstraßen-Prinzip: pro PGN nur eine Konvertierungsrichtung. 3. Gateway-Konfiguration dokumentieren! |
| **Kosten** | 0 € (Konfiguration) |
| **AYDI-Confidence** | measured (Bus-Analyse), documented (Gateway-Konfiguration) |

### 6.9 FB-N2K-09: Autopilot reagiert verzögert oder gar nicht

| Feld | Beschreibung |
|------|-------------|
| **Symptom** | Autopilot folgt dem Kurs nicht korrekt, reagiert verzögert auf Kursänderungen, oder ignoriert Wegpunkt-Daten vom GPS. |
| **Häufigkeit** | Mittel (9% der Autopilot-bezogenen N2K-Probleme) |
| **Ursache 1** | Autopilot empfängt Heading von falscher Quelle (z.B. GPS-COG statt Fluxgate-Heading) |
| **Ursache 2** | PGN-Priorität: ein Gerät mit niedrigerer Priorität überschreibt die korrekte Quelle |
| **Ursache 3** | Heading-Sensor und GPS auf unterschiedlichen Instanzen |
| **Ursache 4** | Hohe Bus-Latenz durch Überlastung → Regelkreis zu langsam |
| **Diagnose** | 1. Source-Adresse des Heading-Signals am Autopilot prüfen. 2. PGN 127250 (Heading) und 129026 (COG) differenzieren. 3. Bus-Auslastung messen. 4. Heading-Sensor-Instanz prüfen. |
| **Lösung** | 1. Am Autopilot die korrekte Heading-Quelle auswählen. 2. Unnötige PGN-Quellen filtern. 3. Bus-Auslastung reduzieren (Update-Raten anpassen). |
| **Kosten** | 0 € (Konfiguration) / 0–100 € (ggf. zusätzlicher Fluxgate-Kompass) |
| **AYDI-Confidence** | measured (PGN-Analyse), documented (Autopilot-Konfiguration) |

### 6.10 FB-N2K-10: AIS-Daten erscheinen nicht auf MFD

| Feld | Beschreibung |
|------|-------------|
| **Symptom** | AIS-Transponder ist eingebaut und funktioniert (LED aktiv), aber MFD zeigt keine AIS-Ziele auf der Karte an. |
| **Häufigkeit** | Mittel (8% bei Neuinstallationen) |
| **Ursache 1** | AIS-Transponder sendet über NMEA 0183 ($AIVDM), kein Gateway zu N2K vorhanden |
| **Ursache 2** | AIS-Daten werden als PGN 129038/129039 gesendet, aber MFD-AIS-Overlay ist deaktiviert |
| **Ursache 3** | AIS-Transponder sendet auf N2K, aber mit falscher Instanz oder deaktiviertem N2K-Ausgang |
| **Diagnose** | 1. AIS-Transponder-Ausgänge prüfen (N2K und/oder 0183?). 2. N2K-PGN-Liste scannen (129038, 129039 vorhanden?). 3. MFD-Einstellungen prüfen (AIS-Overlay aktiviert?). |
| **Lösung** | 1. Bei 0183-only AIS: Gateway NGW-1 oder gleichwertig installieren. 2. Am AIS N2K-Ausgang aktivieren. 3. Am MFD AIS-Overlay aktivieren, Quellgerät auswählen. |
| **Kosten** | 0 € (Konfiguration) / 150–250 € (Gateway falls nötig) |
| **AYDI-Confidence** | measured (PGN-Scan), documented (Konfiguration) |

### 6.11 FB-N2K-11: SignalK-Server zeigt keine N2K-Daten

| Feld | Beschreibung |
|------|-------------|
| **Symptom** | SignalK-Dashboard ist leer oder zeigt nur veraltete Werte. N2K-Netzwerk funktioniert ansonsten normal (MFDs haben Daten). |
| **Häufigkeit** | Häufig bei DIY-Installationen (25%) |
| **Ursache 1** | USB-Gateway (NGT-1, YDNU-02) nicht korrekt eingerichtet (falsche Serial-Port-Konfiguration) |
| **Ursache 2** | Berechtigungsproblem unter Linux (User nicht in dialout-Gruppe) |
| **Ursache 3** | CANboat-Plugin nicht installiert oder falsch konfiguriert |
| **Ursache 4** | USB-Gateway hat keinen Strom (USB-Kabel defekt, Hub ohne Stromversorgung) |
| **Diagnose** | 1. `dmesg | grep ttyUSB` → USB-Gerät erkannt? 2. `ls -la /dev/ttyUSB0` → Berechtigungen? 3. SignalK Server-Log prüfen. 4. LED am USB-Gateway prüfen (Aktivität?). |
| **Lösung** | 1. Serial-Port in SignalK-Konfiguration korrekt einstellen. 2. `sudo usermod -aG dialout $USER` + Neustart. 3. @signalk/nmea2000-provider installieren. 4. USB-Kabel/Hub prüfen, ggf. direkt an Raspberry Pi anschließen. |
| **Kosten** | 0 € (Konfiguration) / 10–30 € (USB-Kabel/Hub) |
| **AYDI-Confidence** | documented (Logs), measured (dmesg/ls) |

### 6.12 FB-N2K-12: Netzwerk instabil nach Hinzufügen neuer Geräte

| Feld | Beschreibung |
|------|-------------|
| **Symptom** | Nach Installation eines neuen Geräts am N2K-Bus treten Ausfälle bei bestehenden Geräten auf. Bus war vorher stabil. |
| **Häufigkeit** | Mittel (10% nach Nachrüstungen) |
| **Ursache 1** | LEN-Budget überschritten (neues Gerät überlastet Stromversorgung) |
| **Ursache 2** | Neues Gerät hat CAN-Fehler und stört den Bus (defektes Gerät, falsche Baudrate) |
| **Ursache 3** | Backbone-Topologie verletzt (Stern statt linear durch Y-Kabel) |
| **Ursache 4** | Adresskonflikt mit bestehendem Gerät |
| **Ursache 5** | Terminierung gestört (Terminator versehentlich entfernt oder 3. Terminator eingebaut) |
| **Diagnose** | 1. Neues Gerät abtrennen → Bus stabil? 2. LEN-Budget berechnen. 3. Terminierungswiderstand messen. 4. Topologie visuell prüfen. 5. Error-Frame-Rate mit Analysetool. |
| **Lösung** | 1. LEN prüfen und ggf. Power-Inserter hinzufügen. 2. Defektes Gerät identifizieren und ersetzen. 3. Topologie korrigieren (linear!). 4. Terminierung korrigieren. |
| **Kosten** | 0–50 € (Konfiguration) / 50–200 € (Power-Inserter) / variabel (Gerätetausch) |
| **AYDI-Confidence** | measured (LEN-Berechnung, Widerstandsmessung), estimated (Geräte-Isolation) |

---

## 7. Troubleshooting-Entscheidungsbäume

### 7.1 Entscheidungsbaum: Keine Daten auf MFD

```
START: MFD zeigt "Keine Daten" für alle Sensoren
│
├── Nur ein Sensor betroffen?
│   ├── JA → Gehe zu Baum 7.2 (Einzelner Sensor)
│   └── NEIN → Weiter
│
├── Alle Geräte am Bus betroffen?
│   ├── JA → Komplettausfall
│   │   ├── Versorgungsspannung am Power-Inserter messen
│   │   │   ├── 0V → Sicherung prüfen → Sicherung defekt? → Ersetzen
│   │   │   │                        → Sicherung OK? → Power-Inserter defekt → Ersetzen
│   │   │   └── 10–16V → Weiter
│   │   │
│   │   ├── Terminierungswiderstand messen (CAN_H ↔ CAN_L)
│   │   │   ├── >10 kΩ → Keine Terminatoren → Beide installieren
│   │   │   ├── 120 Ω → Nur ein Terminator → Zweiten finden/installieren
│   │   │   ├── 60 Ω (±5%) → Terminierung OK → Weiter
│   │   │   ├── <40 Ω → Zu viele Terminatoren → Überschüssige entfernen
│   │   │   └── <10 Ω → Kurzschluss → Segmentweise isolieren
│   │   │
│   │   └── Bus segmentweise prüfen
│   │       ├── Alle Geräte abtrennen, einzeln wieder anschließen
│   │       └── Defektes Gerät oder Kabel identifizieren
│   │
│   └── NEIN → Teilausfall
│       ├── Betroffene Geräte alle in einer Zone? → Lokales Problem (Kabel, Stecker)
│       └── Zufällig verteilt? → Busüberlastung, EMV-Problem → Fehler-Frame-Rate messen
```

### 7.2 Entscheidungsbaum: Einzelner Sensor ohne Daten

```
START: Ein Sensor sendet keine Daten auf den N2K-Bus
│
├── Sensor hat Power-LED?
│   ├── LED aus → Kein Strom
│   │   ├── Drop-Kabel prüfen (Stecker fest, Kabel intakt?)
│   │   ├── T-Stück prüfen (Kontakte korrodiert?)
│   │   └── LEN prüfen (Backbone überlastet?)
│   └── LED an → Strom vorhanden
│
├── Sensor erscheint im Netzwerk-Scan (Gerätliste am MFD)?
│   ├── NEIN → Sensor kommuniziert nicht
│   │   ├── Firmware-Update prüfen
│   │   ├── Sensor zurücksetzen (Factory Reset)
│   │   └── Sensor mit anderem Drop-Kabel testen
│   └── JA → Sensor kommuniziert, aber MFD zeigt keine Daten
│       ├── PGN-Scan: Sensor sendet erwartete PGN?
│       │   ├── NEIN → Sensor falsch konfiguriert → Konfiguration prüfen
│       │   └── JA → MFD empfängt PGN nicht → MFD-Quellenauswahl prüfen
│       └── Instanznummer korrekt?
│           ├── Duplikat → Instanznummer ändern
│           └── OK → MFD-Konfiguration prüfen
```

### 7.3 Entscheidungsbaum: WiFi-Gateway-Probleme

```
START: Tablet/App verbindet sich nicht zum WiFi-Gateway
│
├── WiFi-Netzwerk des Gateways sichtbar?
│   ├── NEIN → Gateway-Strom prüfen
│   │   ├── Kein Strom → Versorgung prüfen (N2K-Bus oder externes Netzteil)
│   │   └── Strom OK → Gateway neu starten, Factory Reset, Firmware prüfen
│   └── JA → Weiter
│
├── Tablet verbindet sich zum WLAN?
│   ├── NEIN → Passwort prüfen (Default: siehe Handbuch)
│   │   ├── Falsches Passwort → Zurücksetzen
│   │   └── Richtiges Passwort → Max. Clients erreicht? Anderen Client trennen
│   └── JA → Weiter
│
├── App erhält Daten?
│   ├── NEIN → Port-Konfiguration prüfen
│   │   ├── TCP/UDP Port stimmt? (Standard: 10110, 2000, 6464 je nach Gateway)
│   │   ├── Protokoll stimmt? (TCP vs. UDP)
│   │   └── Gateway hat N2K-Daten? → Gateway-Webinterface prüfen
│   └── JA, aber unvollständig → PGN-Filter am Gateway prüfen
│
└── Verbindung bricht immer wieder ab?
    ├── Signalstärke prüfen (WiFi Analyzer)
    │   ├── Schwach (<-70 dBm) → Position optimieren, externe Antenne
    │   └── Stark (>-50 dBm) → Kanalüberlappung? Kanal manuell setzen
    └── Firmware-Update prüfen
```

### 7.4 Entscheidungsbaum: SignalK zeigt keine/falsche Daten

```
START: SignalK-Dashboard leer oder Daten fehlerhaft
│
├── SignalK-Server läuft?
│   ├── NEIN → sudo systemctl status signalk → Fehlermeldung?
│   │   ├── Service nicht gefunden → Installation prüfen
│   │   └── Service failed → Log lesen: journalctl -u signalk -n 50
│   └── JA → Weiter
│
├── Datenquelle konfiguriert?
│   ├── NEIN → Server Settings → Data Connections → Add
│   │   ├── USB-Gateway → Serial Port, Baud Rate, Input Type (NMEA2000)
│   │   └── WiFi-Gateway → TCP/UDP Client, IP:Port
│   └── JA → Weiter
│
├── Daten im Server sichtbar? (Data Browser: /signalk/v1/api/vessels/self)
│   ├── NEIN → Connection-Log prüfen
│   │   ├── "Permission denied" → User zu dialout-Gruppe hinzufügen
│   │   ├── "Device not found" → USB-Gerät nicht erkannt → dmesg prüfen
│   │   └── "Connection refused" → TCP-Verbindung fehlgeschlagen → IP/Port prüfen
│   └── JA, Daten vorhanden → Dashboard-Problem
│       ├── Dashboard nicht konfiguriert → Widgets hinzufügen, Pfade auswählen
│       └── Daten veraltet (timestamp alt) → Quelle liefert nicht → Quelle prüfen
│
└── Daten falsch/unplausibel?
    ├── Einheiten prüfen (SignalK nutzt SI: Kelvin, Radiant, m/s, Pascal)
    ├── Sensor-Offset/Kalibrierung prüfen
    └── Plugin-Konfiguration prüfen (signalk-derived-data etc.)
```

### 7.5 Entscheidungsbaum: Netzwerk nach Refit instabil

```
START: N2K-Netzwerk nach Refit/Nachrüstung instabil
│
├── Was wurde geändert?
│   ├── Neues Gerät hinzugefügt → FB-N2K-12 (Abschnitt 6.12)
│   ├── Kabel verlegt/verlängert
│   │   ├── Backbone-Gesamtlänge prüfen (max. 100m Micro-C, 200m Mini-C)
│   │   ├── Kumulative Drop-Länge prüfen (max. 78m)
│   │   └── Topologie prüfen (linear, keine Sterne, keine Ringe)
│   ├── Gerät getauscht (Upgrade)
│   │   ├── Neues Gerät korrekt konfiguriert?
│   │   ├── Altes Gerät vollständig entfernt (kein verwaister Stub)?
│   │   └── Instanznummern übernommen?
│   └── Stromversorgung geändert
│       ├── Neuer Batteriebank → Massekonzept prüfen
│       ├── Neuer Inverter/Charger → EMV (FB-N2K-06)
│       └── Sicherungswert geändert → LEN-Budget prüfen
│
├── Terminierung noch korrekt?
│   ├── Messen: 60Ω? → OK
│   └── Nicht 60Ω → Terminatoren lokalisieren und korrigieren
│
└── Systematische Prüfung
    ├── Alle Geräte abtrennen
    ├── Nur Backbone + Terminatoren + Power → Bus-Grundzustand prüfen
    ├── Geräte einzeln wieder anschließen
    └── Nach jedem Gerät: Fehler-Frame-Rate prüfen
```

---

## 8. FAQ

### 8.1 Grundlagen

**F1: Was ist der Unterschied zwischen NMEA 0183 und NMEA 2000?**

NMEA 0183 ist ein serielles Punkt-zu-Punkt-Protokoll (ein Sender, mehrere Empfänger) mit ASCII-Datensätzen bei 4.800 oder 38.400 Baud. NMEA 2000 ist ein CAN-Bus-basiertes Multi-Master-Netzwerk mit 250 kbit/s, bei dem alle Geräte gleichberechtigt senden und empfangen können. NMEA 2000 ist schneller, einfacher zu verdrahten (ein Bus statt viele Einzelkabel) und unterstützt deutlich mehr Datenpunkte. NMEA 0183 bleibt relevant für Legacy-Geräte.

**F2: Kann ich NMEA 0183 und NMEA 2000 gleichzeitig betreiben?**

Ja, über einen Gateway (z.B. Actisense NGW-1, Yacht Devices YDNR-02). Der Gateway übersetzt bidirektional zwischen beiden Protokollen. Es ist sogar die empfohlene Lösung, wenn Legacy-Geräte (alter Autopilot, AIS) im Einsatz sind.

**F3: Wie viele Geräte passen an einen NMEA-2000-Bus?**

Theoretisch bis zu 252 (Adressraum), praktisch maximal 50 Geräte wegen der LEN-Beschränkung (Strombudget) und physikalischer Bus-Limitierungen. Bei großen Yachten: separate Backbone-Segmente mit Bridge verwenden.

**F4: Was passiert, wenn ich die Terminatoren vergesse?**

Ohne Terminierung entstehen Signalreflexionen am offenen Kabelende. Dies führt zu sporadischen Datenfehlern, die sich als zeitweilige Ausfälle einzelner Geräte oder als korrupte Datenwerte zeigen. Der Bus kann instabil werden und in den Bus-Off-Zustand gehen.

**F5: Muss ich proprietäre Kabel desselben Herstellers wie mein MFD verwenden?**

Nein. NMEA 2000 ist ein offener Standard. Micro-C-Stecker (M12 5-polig) sind genormt und herstellerübergreifend kompatibel. Maretron-, Garmin-, Simrad- und Drittanbieter-Kabel sind untereinander kompatibel. Ausnahme: Raymarine SeaTalkng hat leicht andere Farbkodierung (identischer Stecker), was bei Mischinstallationen beachtet werden muss.

### 8.2 Installation

**F6: Wo platziere ich den Power-Inserter am besten?**

Ideal ist die Mitte des Backbones, um den Spannungsabfall zu beiden Seiten gleichmäßig zu verteilen. In der Praxis oft in der Nähe der Hauptschalttafel, da dort die 12V-Versorgung am einfachsten abgegriffen wird. Bei langen Backbones: zwei Power-Inserter verwenden.

**F7: Wie lang darf ein Drop-Kabel sein?**

Maximal 6 Meter. Die kumulative Gesamtlänge aller Drop-Kabel darf 78 Meter nicht überschreiten. Für Geräte, die weiter als 6m vom Backbone entfernt sind (z.B. Windgeber am Masttop): Backbone bis zum Gerät verlängern, nicht das Drop-Kabel.

**F8: Kann ich das Backbone-Kabel durch das Schott führen?**

Ja, aber es muss wasserdicht durchgeführt werden. Spezielle Schottdurchführungen für Micro-C-Kabel sind erhältlich (z.B. Maretron NM-NG1-BHD). Alternativ: Kabel mit ausreichend Länge durch das Schott führen und die Steckverbindung auf der trockenen Seite lassen.

**F9: Wie schütze ich das N2K-Netzwerk vor Blitzschlag?**

Vollständiger Schutz ist nicht möglich, aber Schadensbegrenzung: (1) Backbone-Schirm einseitig auf Bordmasse legen. (2) CAN-Bus-Überspannungsableiter (TVS-Dioden) am Power-Inserter. (3) Sensoren am Masttopp über eigenes Erdungskabel zum Kiel leiten. (4) Alle Geräte über denselben Massepunkt verbinden.

**F10: Welchen Kabelquerschnitt brauche ich für mein Boot?**

Micro-C (0,82 mm²) reicht für die meisten Yachten bis 15m mit Backbones bis 100m und bis 50 LEN. Mini-C/DeviceNet (1,31 mm²) für größere Yachten (15–25m) mit bis 200m Backbone und 80 LEN. Mid-C (2,08 mm²) für Superyachten oder besonders lange Backbone-Strecken mit hoher Geräteanzahl.

### 8.3 Gateways und WiFi

**F11: Welcher WiFi-Gateway ist der beste Einstieg?**

Für Budget und DIY: Yacht Devices YDWG-02 (ca. 180 €). Kompakt, zuverlässig, reicht für die meisten Tablet-Apps. Für mehr Funktionalität (bidirektional, NMEA 0183 zusätzlich): Actisense W2K-1 (ca. 430 €). Für Internet-Integration: Digital Yacht Aqua Pro (ca. 650 €, kombiniert Router + NMEA-Gateway).

**F12: Kann ich mein iPad/Tablet als Kartenplotter verwenden?**

Ja, über einen WiFi-Gateway. Apps wie Navionics Boating, iSailor, Aqua Map empfangen N2K-Daten (konvertiert zu NMEA 0183 via TCP) über WiFi. Einschränkungen: Tablet ist nicht wasser-/stoßfest wie ein dediziertes MFD, Akkulaufzeit begrenzt, Sonnenlicht-Ablesbarkeit geringer. Als Backup oder Ergänzung zum MFD empfohlen, nicht als alleiniges System.

**F13: Was ist der Unterschied zwischen TCP und UDP bei WiFi-Gateways?**

TCP (Transmission Control Protocol) garantiert die Zustellung jedes Datenpakets in der richtigen Reihenfolge — zuverlässig, aber bei Verbindungsproblemen kommen Daten verzögert an (Wiederholungen). UDP (User Datagram Protocol) sendet ohne Bestätigung — bei Paketverlust fehlen Daten, aber es gibt keine Verzögerung. Für Echtzeit-Navigation ist UDP oft besser geeignet (aktuelle Position wichtiger als lückenlose Historie).

**F14: Kann ich über WiFi auch den Autopilot steuern?**

Technisch ja (bei bidirektionalem Gateway + entsprechender App/Software wie SignalK Autopilot Plugin). Aber: WiFi-Verbindungen sind nicht zuverlässig genug für sicherheitskritische Steuerung. Autopilot-Kommandos sollten immer über kabelgebundenes N2K erfolgen. WiFi-Steuerung nur als Komfortfunktion bei gutem Wetter und aktiver Überwachung.

### 8.4 SignalK und Open-Source

**F15: Was ist SignalK und brauche ich das?**

SignalK ist ein offenes Datenformat und Server-Framework für Bootsdaten. Es ist KEIN Ersatz für NMEA 2000, sondern eine Ergänzung: Der SignalK-Server empfängt N2K-Daten über einen USB-Gateway und stellt sie als JSON-Daten über HTTP/WebSocket bereit. Vorteile: offenes Format, kostenlos, erweiterbar durch Plugins (Ankerwache, Autopilot-Web-Interface, Datenlogging). Empfohlen für technikaffine Eigner, die ihr System selbst erweitern möchten.

**F16: Welche Hardware brauche ich für SignalK?**

Minimal: Raspberry Pi 4 (60 €) + Yacht Devices YDNU-02 USB-Gateway (110 €) + 12V→5V-Wandler (25 €) = ca. 195 €. Damit laufen SignalK-Server, Dashboard und alle Plugins. Für höhere Zuverlässigkeit: Raspberry Pi im Aluminium-Gehäuse, Industrial-SD-Karte, externe WiFi-Antenne.

**F17: Ist SignalK zuverlässig genug für den Dauerbetrieb?**

SignalK-Server auf Raspberry Pi läuft bei vielen Eignern seit Jahren stabil. Aber: die Zuverlässigkeit hängt von der Hardware (Industrial-SD-Karte, gute Stromversorgung) und den installierten Plugins ab. Kein NMEA-Zertifizierungsprozess wie bei kommerziellen Geräten. Empfehlung: als Ergänzung verwenden, nicht als einzige Datenquelle für sicherheitskritische Systeme (Navigation, Autopilot). Für Monitoring, Logging, Alarmierung und Komfortfunktionen exzellent geeignet.

**F18: Kann ich SignalK-Daten über das Internet abrufen?**

Ja, über VPN oder Port-Forwarding (mit Sicherheitsbedenken). Besser: Plugins wie signalk-cloud oder Tailscale-Integration für sicheren Remote-Zugriff. Victron VRM Portal bietet ähnliche Funktionalität für Energiedaten. Remote-Monitoring von Batterie, Bilge, Position ist ein häufiger Anwendungsfall.

**F19: Welche SignalK-Plugins sind am nützlichsten?**

Top 5 für Fahrtensegler: (1) signalk-anchor-alarm (Ankerwache mit Push), (2) signalk-to-influxdb + Grafana (Datenlogging + Dashboards), (3) signalk-derived-data (True Wind, VMG), (4) signalk-venusOS (Victron-Integration), (5) signalk-zones (Alarmzonen für Tiefe, Spannung, Temperatur).

### 8.5 Diagnose und Wartung

**F20: Wie kann ich die Busauslastung meines N2K-Netzwerks prüfen?**

Mit einem USB-Gateway (Actisense NGT-1, Yacht Devices YDNU-02) und Analysesoftware (Maretron N2KAnalyzer, Actisense NMEA Reader, CANboat). Die Busauslastung sollte unter 50% liegen (entspricht ca. 125 kbit/s). Werte über 70% führen zu spürbaren Latenzen.

**F21: Wie oft muss ich das N2K-Netzwerk warten?**

Jährlich: alle Steckverbindungen auf Korrosion prüfen (visuell), Terminierungswiderstand messen (60Ω), Versorgungsspannung messen, Firmware-Versionen notieren. Alle 3–5 Jahre: Dichtigkeit der Schottdurchführungen prüfen, Kabel auf Abrieb/Knicke untersuchen, Stecker mit Korrosionsschutz behandeln.

**F22: Kann ein defektes Gerät den gesamten Bus lahmlegen?**

Ja. Wenn ein Gerät dauerhaft dominante Bits auf den Bus legt (CAN-Fehler), kann es alle anderen Geräte in den Bus-Off-Zustand treiben. Lösung: Gerät segmentweise isolieren (Drop-Kabel abziehen). Professionelle Installation: CAN-Bus-Isolatoren zwischen kritischen Segmenten verwenden.

### 8.6 Spezialthemen

**F23: Wie integriere ich einen älteren Yanmar/Volvo-Diesel ohne N2K?**

Über einen Analog-zu-N2K-Konverter wie Actisense EMU-1. Dieser liest die analogen Sensorsignale des Motors (Öldruck, Temperatur, Drehzahl) und wandelt sie in NMEA-2000-PGN um. Alternativ: herstellerspezifische Gateways (Yanmar YD25, Volvo Penta EVC Gateway).

**F24: Was ist NMEA OneNet und muss ich jetzt umrüsten?**

NMEA OneNet ist die Ethernet-basierte Erweiterung von NMEA 2000. Stand 2026 sind erst wenige OneNet-Geräte verfügbar (Maretron, Furuno). Umrüstung ist NICHT notwendig — OneNet erweitert N2K, ersetzt es nicht. Für Neubauten ab 2027 kann ein OneNet-fähiger Switch eingeplant werden, aber der N2K-Backbone bleibt für Sensoren die sinnvollste Lösung.

**F25: Wie dimensioniere ich das Netzwerk für eine Charterflotte?**

Charterboote haben spezielle Anforderungen: (1) Robuste Stecker (mit Schraubverriegelung, nicht nur Snap-in). (2) Keine Drop-Kabel an zugänglichen Stellen (Chartergäste trennen unbeabsichtigt Geräte). (3) WiFi-Gateway mit Gastnetz (Navigation getrennt von Entertainment). (4) Voyage Recorder für Schadensrekonstruktion. (5) Monitoring-System mit Alarmierung an Flottenbetreiber.

**F26: Wie sichere ich N2K-Daten für die langfristige Analyse?**

(1) Yacht Devices YDVR-04 Voyage Recorder (autark, SD-Karte). (2) SignalK + InfluxDB (auf Raspberry Pi, Datenbank lokal). (3) Maretron N2KView mit Logging (auf Windows-PC). (4) Cloud-basiert: SignalK → InfluxDB Cloud oder Grafana Cloud. Empfehlung für AYDI: SignalK + InfluxDB, da offenes Format und leicht exportierbar.

**F27: Was kostet ein typisches N2K-Netzwerk für eine 12m-Fahrtenyacht?**

Backbone-Komponenten (Kabel, T-Stücke, Terminatoren, Power): ca. 350–600 €. Gateway (NMEA 0183 bidirektional): ca. 150–250 €. WiFi-Gateway: ca. 180–450 €. SignalK-Server (Raspberry Pi + USB-Gateway): ca. 200–350 €. Sensoren (je nachdem, was schon N2K-fähig ist): 0–2.000 €. Arbeitszeit (Werft, 8–16h): 800–2.400 €. Gesamtschätzung: 1.700–6.000 € (ohne MFD und Autopilot, die eigene Budgetposten sind).

---

## 9. Glossar

### 9.1 Begriffe A–G

| Begriff | Erklärung |
|---------|-----------|
| **ACK (Acknowledge)** | Bestätigungssignal im CAN-Bus-Protokoll, das den fehlerfreien Empfang eines Frames signalisiert |
| **Address Claim** | Automatisches Verfahren zur Adressvergabe im NMEA-2000-Netzwerk (PGN 60928) |
| **AP (Access Point)** | WiFi-Betriebsmodus, bei dem das Gerät ein eigenes WLAN-Netzwerk erzeugt |
| **AIS (Automatic Identification System)** | System zur automatischen Identifikation und Ortung von Schiffen, übertragen über VHF und N2K |
| **Backbone** | Hauptkabel des NMEA-2000-Netzwerks, an das über T-Stücke und Drop-Kabel die Geräte angeschlossen werden |
| **BAM (Broadcast Announce Message)** | Ankündigung einer Multi-Frame-Nachricht im Transport-Protokoll |
| **Baudrate** | Datenübertragungsgeschwindigkeit in Bits pro Sekunde (NMEA 0183: 4.800/38.400 Baud, NMEA 2000: 250.000 Baud) |
| **Bridge** | Gerät zur Protokollübersetzung zwischen zwei unterschiedlichen Bussystemen |
| **Bus-Off** | Fehlerzustand des CAN-Controllers, bei dem das Gerät sich vom Bus trennt (nach 256+ Fehlern) |
| **CAN (Controller Area Network)** | Serielles Bussystem, ursprünglich für die Automobilindustrie entwickelt (Robert Bosch, 1983), Basis von NMEA 2000 |
| **CAN 2.0B** | CAN-Spezifikation mit 29-Bit Extended Identifier, verwendet von NMEA 2000 |
| **CAN FD** | CAN Flexible Data-rate, Erweiterung mit bis zu 8 Mbit/s und 64 Byte Nutzdaten pro Frame |
| **CAN_H / CAN_L** | Die beiden Signalleitungen des CAN-Bus (High und Low), die das Differenzsignal tragen |
| **CANboat** | Open-Source-Software zur Dekodierung von NMEA-2000-CAN-Frames unter Linux/macOS |
| **CE (Conformité Européenne)** | EU-Konformitätskennzeichnung, Pflicht für in der EU verkaufte Elektronik |
| **Cerbo GX** | Energiemanagement-Zentralgerät von Victron Energy mit N2K-Integration |
| **COG (Course Over Ground)** | Kurs über Grund, berechnet aus GPS-Positionsänderungen |
| **CRC (Cyclic Redundancy Check)** | Prüfsumme zur Fehlererkennung in CAN-Frames |
| **DeviceNet** | Industrielles CAN-Bus-Steckersystem (M12 5-polig), verwendet für NMEA 2000 Mini-C |
| **Dominant** | Buszustand im CAN-Bus (logisch 0), bei dem CAN_H > CAN_L (Differenz ≈ 2V) |
| **DOP (Dilution of Precision)** | Maß für die geometrische Güte der GPS-Satellitenkonstellation |
| **Drop-Kabel** | Abzweigkabel vom Backbone zum einzelnen Gerät, max. 6m Länge |
| **ECU (Electronic Control Unit)** | Elektronisches Steuergerät (typisch: Motorsteuerung) |
| **EMV (Elektromagnetische Verträglichkeit)** | Fähigkeit eines Geräts, in seiner elektromagnetischen Umgebung störungsfrei zu funktionieren |
| **Error Frame** | Spezieller CAN-Frame, der einen erkannten Übertragungsfehler signalisiert |
| **Fast-Packet** | NMEA-2000-Übertragungsverfahren für Nachrichten mit 9–223 Bytes Nutzdaten |
| **FTDI** | Chiphersteller für USB-zu-Serial-Wandler, Standard für marine USB-Adapter |
| **Gateway** | Gerät zur Protokollkonvertierung (z.B. NMEA 0183 ↔ NMEA 2000) |
| **GNSS (Global Navigation Satellite System)** | Oberbegriff für GPS, GLONASS, Galileo, BeiDou |

### 9.2 Begriffe H–N

| Begriff | Erklärung |
|---------|-----------|
| **HDOP** | Horizontal Dilution of Precision, Maß für die horizontale GPS-Genauigkeit |
| **Heartbeat** | Periodisches Lebenszeichen-Signal eines N2K-Geräts (PGN 126993) |
| **HS-0183** | High-Speed NMEA 0183 bei 38.400 Baud (statt Standard 4.800 Baud) |
| **IEC 61162** | Internationale Norm für maritime Navigationskommunikation (NMEA-Standards) |
| **InfluxDB** | Zeitreihen-Datenbank, häufig für Logging von Bootsdaten mit SignalK |
| **Instanznummer** | Eindeutige Kennung gleichartiger Geräte am N2K-Bus (z.B. Motor 1, Motor 2; Tank Fuel 0, Tank Fuel 1) |
| **IP42/IP54/IP67** | Schutzklasse gegen Fremdkörper und Wasser (IP42: tropfsicher, IP67: untertauchbar) |
| **J1939** | SAE-Standard für CAN-Bus in Nutzfahrzeugen, technische Basis von NMEA 2000 |
| **JSON (JavaScript Object Notation)** | Leichtgewichtiges Datenaustauschformat, Basis von SignalK |
| **LEN (Load Equivalency Number)** | Maß für den Strombedarf eines N2K-Geräts aus dem Bus (1 LEN = 50 mA bei 12V) |
| **M12** | Industrieller Rundsteckverbinder mit 12mm Gewindedurchmesser, Standard für Micro-C |
| **mDNS** | Multicast-DNS, Diensterkennung im lokalen Netzwerk (verwendet von NMEA OneNet) |
| **Micro-C** | Kompakter NMEA-2000-Steckverbinder (M12 5-polig), Standard für Yachten bis 20m |
| **Mid-C** | Verstärkter NMEA-2000-Steckverbinder (M12 5-polig, dickere Kabel), für Superyachten |
| **Mini-C** | Mittlerer NMEA-2000-Steckverbinder (DeviceNet), für größere Yachten |
| **MMSI (Maritime Mobile Service Identity)** | 9-stellige Kennnummer für Seefunkstellen, verwendet in AIS und DSC |
| **MFD (Multi-Function Display)** | Multifunktions-Anzeigegerät für Navigation, Radar, Echolot etc. |
| **NAME** | 64-Bit eindeutiger Identifier eines NMEA-2000-Geräts (für Address Claim) |
| **NET-S (Network Supply)** | 12V-Stromversorgung über den NMEA-2000-Backbone |
| **N2K** | Kurzform für NMEA 2000 |
| **NMEA (National Marine Electronics Association)** | US-amerikanischer Verband für marine Elektronik, Herausgeber der NMEA-Standards |
| **Node.js** | JavaScript-Laufzeitumgebung, Plattform für SignalK-Server |

### 9.3 Begriffe O–Z

| Begriff | Erklärung |
|---------|-----------|
| **OneNet** | NMEA-eigener Standard für Ethernet-basierte marine Datennetzwerke (IEEE 802.3 / IPv6; nicht IEC 61162-460) |
| **OpenCPN** | Open-Source-Kartenplotter-Software für PC/Raspberry Pi |
| **PGN (Parameter Group Number)** | Eindeutige Kennung eines Datenpakets im NMEA-2000-Protokoll |
| **PoE (Power over Ethernet)** | Stromversorgung über Ethernet-Kabel (IEEE 802.3af/at/bt) |
| **Power Inserter / Power-T** | Gerät zur Einspeisung der 12V-Versorgungsspannung in den N2K-Backbone |
| **PTP (Precision Time Protocol)** | IEEE 1588, Zeitsynchronisation im Netzwerk (<1μs Genauigkeit) |
| **REST (Representational State Transfer)** | HTTP-basiertes API-Design, verwendet von SignalK |
| **Rezessiv** | Buszustand im CAN-Bus (logisch 1), CAN_H = CAN_L ≈ 2,5V |
| **RS-422** | Differenzieller serieller Schnittstellenstandard, verwendet von NMEA 0183 |
| **SAE (Society of Automotive Engineers)** | US-amerikanischer Ingenieurverband, Herausgeber von J1939 |
| **SeaTalk1** | Älteres proprietäres Bussystem von Autohelm/Raymarine (RS-485-basiert, 3-adrig) |
| **SeaTalkng** | Raymarine-Markenname für NMEA 2000 (kompatibel, andere Kabelfarben) |
| **Sentence** | Ein Datensatz in NMEA 0183, beginnt mit $ oder !, endet mit CR+LF |
| **Shunt** | Präzisionswiderstand zur Strommessung (für Batteriemonitore) |
| **SignalK** | Offenes, JSON-basiertes Datenformat und Serverframework für marine Daten |
| **SimNet** | Proprietäres Netzwerk von Simrad/Navico, physikalisch kompatibel mit N2K Micro-C |
| **SOG (Speed Over Ground)** | Geschwindigkeit über Grund, berechnet aus GPS-Positionsänderungen |
| **SoC (State of Charge)** | Ladezustand einer Batterie in Prozent |
| **Source Address** | 8-Bit-Adresse (0–251) eines Geräts auf dem NMEA-2000-Bus |
| **T-Stück (Tee)** | Y-förmiger Steckverbinder zur Abzweigung vom Backbone |
| **TCP (Transmission Control Protocol)** | Verbindungsorientiertes Transportprotokoll mit Zustellgarantie |
| **Terminator** | Abschlusswiderstand (120Ω) an den physikalischen Enden des N2K-Backbones |
| **TP (Transport Protocol)** | ISO-11783-Protokoll für N2K-Nachrichten >223 Bytes |
| **TSN (Time-Sensitive Networking)** | Ethernet-Erweiterung für deterministische Echtzeit-Kommunikation |
| **TVS-Diode** | Transient Voltage Suppressor, Überspannungsschutz |
| **UDP (User Datagram Protocol)** | Verbindungsloses Transportprotokoll ohne Zustellgarantie |
| **VE.Can** | Victron-Energy-eigener CAN-Bus, kompatibel mit N2K (mit Adapter) |
| **VMG (Velocity Made Good)** | Geschwindigkeitskomponente in Richtung Ziel/Wind |
| **VRM (Victron Remote Management)** | Cloud-Portal von Victron Energy für Fernüberwachung |
| **WebSocket** | Vollduplex-Kommunikationsprotokoll über TCP, für Echtzeit-Streaming (SignalK) |
| **WPA2/WPA3** | WiFi-Verschlüsselungsstandards (WiFi Protected Access) |
| **XTE (Cross Track Error)** | Querabweichung von der geplanten Route |

---

## 10. Schnell-Referenz

### 10.1 NMEA 2000 Backbone auf einen Blick

```
MICRO-C BACKBONE (Standard, 80% aller Yachten):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Max. Backbone:        100m
Max. Drop:            6m
Max. Drop kumulativ:  78m
Max. Geräte:          50
Max. LEN:             50 (= 2,5A)
Kabelquerschnitt:     0,82 mm² (18 AWG)
Stecker:              M12 5-polig, A-kodiert
Terminierung:         2× 120Ω → 60Ω parallel
Datenrate:            250 kbit/s
Versorgungsspannung:  9–16V DC (nominal 12V)
```

### 10.2 Checkliste: N2K-Netzwerk-Installation

```
□ Backbone-Route planen (linear, keine Sterne/Ringe)
□ Gesamtlänge berechnen (Backbone < 100m für Micro-C)
□ LEN-Budget berechnen (Summe aller Geräte-LEN)
□ Drop-Kabel-Längen planen (jeweils < 6m)
□ Kumulative Drop-Länge berechnen (< 78m)
□ Power-Inserter positionieren (möglichst mittig)
□ Sicherung dimensionieren (3A für Micro-C)
□ Terminatoren an beiden Enden (1× Male, 1× Female)
□ Schirmung einseitig erden (am Power-Inserter)
□ EMV-Abstände einhalten (10cm DC, 30cm AC/Inverter, 1m VHF)
□ Kabelführung: Wellrohr im Maschinenraum, Kabelbinder an Schotten
□ Stecker mit Kontaktfett/Korrosionsschutz behandeln
□ Terminierung messen (60Ω zwischen CAN_H und CAN_L)
□ Versorgungsspannung am entferntesten Gerät messen (>9V)
□ Geräte-Scan am MFD: alle Geräte sichtbar?
□ PGN-Quellen priorisieren (bei mehreren GPS, etc.)
□ Instanznummern eindeutig vergeben (Tanks, Motoren, Batterien)
□ Gateway-Filter konfigurieren (keine Datenschleifen)
□ Dokumentation erstellen (Netzwerk-Diagramm, LEN-Tabelle, IP-Adressen)
```

### 10.3 PGN Quick-Reference (Die 20 wichtigsten)

```
PGN     | Name                    | Bytes | Rate  | Typ
--------|-------------------------|-------|-------|-----
060928  | ISO Address Claim       |   8   | Start | Single
126992  | System Time             |   8   | 1 Hz  | Single
126993  | Heartbeat               |   8   | 1 Hz  | Single
126996  | Product Information     |  ~50  | Req.  | Fast
127245  | Rudder                  |   8   | 10 Hz | Single
127250  | Vessel Heading          |   8   | 10 Hz | Single
127488  | Engine Params (Rapid)   |   8   | 10 Hz | Single
127489  | Engine Params (Dynamic) |  26   | 0.5Hz | Fast
127505  | Fluid Level             |   8   | 2.5Hz | Single
127508  | Battery Status          |   8   | 1.5Hz | Single
128259  | Speed (Water)           |   6   | 2 Hz  | Single
128267  | Water Depth             |   5   | 2 Hz  | Single
129025  | Position (Rapid)        |   8   | 4 Hz  | Single
129026  | COG/SOG (Rapid)         |   8   | 4 Hz  | Single
129029  | GNSS Position Data      |  43   | 1 Hz  | Fast
129038  | AIS Class A Report      |  27   | Var.  | Fast
129283  | Cross Track Error       |   6   | 1 Hz  | Single
129284  | Navigation Data         |  34   | 1 Hz  | Fast
130306  | Wind Data               |   6   | 2 Hz  | Single
130312  | Temperature             |   8   | 0.5Hz | Single
```

### 10.4 Steckverbinder-Zuordnung

```
MALE (Stift) = Stromführende Seite (vom Power-Inserter weg)
FEMALE (Buchse) = Empfangende Seite (zum Power-Inserter hin)

BACKBONE-RICHTUNG:
[Term-M] ←MALE━━━━FEMALE→ [T-Stück] ←MALE━━━━FEMALE→ [T-Stück] ←MALE━━━━FEMALE→ [Term-F]

MERKSATZ: "Male links, Female rechts" (wenn man in Backbone-Richtung schaut)

T-STÜCK-AUSRICHTUNG:
  Backbone-Eingang (Female) ← Backbone → Backbone-Ausgang (Male)
                                │
                          Drop (Female)
                                │
                          Gerät (Male)
```

### 10.5 Spannungsabfall-Schnellberechnung

```
Micro-C (0,82 mm²): 42 mΩ/m (Hin + Rück)
Mini-C  (1,31 mm²): 26 mΩ/m
Mid-C   (2,08 mm²): 16 mΩ/m

Beispiel: 15m Micro-C Backbone, 2A Gesamtlast
U_drop = 0,042 Ω/m × 15m × 2A = 1,26V
Am Ende: 12,8V - 1,26V = 11,54V ✓ (>9V Minimum)

Beispiel: 25m Micro-C Backbone, 2,5A Gesamtlast
U_drop = 0,042 Ω/m × 25m × 2,5A = 2,63V
Am Ende: 12,8V - 2,63V = 10,17V ✓ (knapp, besser Mini-C oder 2. Inserter)

Beispiel: 40m Micro-C Backbone, 2,5A Last
U_drop = 0,042 × 40 × 2,5 = 4,20V
Am Ende: 12,8V - 4,20V = 8,60V ✗ (unter 9V!) → Mini-C oder 2. Inserter verwenden!
```

---

## ANHANG A–H — Fallstudien {#anhang-a-h}

### ANHANG A — Fallstudie: Bavaria C42 Fahrtenyacht — Kompletter N2K-Refit

**Ausgangssituation:**
- Bavaria C42, Baujahr 2018, 12,80m Segelyacht
- Bestehendes System: Raymarine SeaTalkng (kompatibel mit N2K), 8 Geräte
- Problem: kein WiFi-Zugriff auf Daten, älterer Autopilot ohne N2K, kein Energiemonitoring

**Zielsetzung:**
- WiFi-Zugang für iPad mit Navionics
- Integration des Autopiloten (Raymarine ST4000+, SeaTalk1)
- Victron-Energiemanagement in N2K integrieren
- SignalK-Server für Langzeitdatenlogging

**Netzwerk vor dem Refit:**

```
[Term-M] ── [Wind] ── [GPS] ── [MFD Axiom 9] ── [Echolot] ── [MFD Axiom 7] ── [Term-F]
```

6 Geräte, Backbone 8m, LEN: 12

**Netzwerk nach dem Refit:**

```
[Term-M] ── [Wind] ── [GPS] ── [MFD Axiom 9] ── [Echolot] ── [MFD Axiom 7]
          ── [SeaTalk1-Gateway] ── [Victron Cerbo GX] ── [YDWG-02 WiFi]
          ── [Tankgeber Diesel] ── [Tankgeber Wasser] ── [YDNU-02 USB→RasPi]
          ── [Term-F]
```

12 Geräte, Backbone 12m, LEN: 22

**Komponentenliste:**

| Komponente | Modell | Kosten |
|------------|--------|--------|
| SeaTalk1 → N2K Gateway | Raymarine E22158 | 115 € |
| WiFi-Gateway | Yacht Devices YDWG-02 | 185 € |
| USB-Gateway | Yacht Devices YDNU-02 | 115 € |
| Raspberry Pi 4 + Gehäuse + Netzteil | — | 105 € |
| Victron Cerbo GX | — | 285 € |
| VE.Can-zu-N2K Kabel | Victron | 38 € |
| Tankgeber Diesel (kapazitiv) | Yacht Devices YDLV-04 | 155 € |
| Tankgeber Wasser (kapazitiv) | Yacht Devices YDLV-04 | 155 € |
| Backbone-Verlängerung 4m | Micro-C | 35 € |
| T-Stücke (4 Stück) | Micro-C | 80 € |
| Drop-Kabel (4× 1m, 2× 2m) | Micro-C | 90 € |
| **Gesamt Material** | | **1.358 €** |
| Arbeitszeit (Werft, 12h) | | 1.440 € |
| **Gesamtkosten** | | **2.798 €** |

**Ergebnis:**
- Alle Navigationsdaten auf iPad (Navionics) über YDWG-02
- Autopilot ST4000+ funktioniert über SeaTalk1-Gateway
- Victron Energiedaten (Batterie-SoC, Solarertrag, Verbrauch) auf allen MFDs
- SignalK-Server mit Ankerwache, Datenlogging (InfluxDB), Grafana-Dashboard
- Gesamtauslastung N2K-Bus: ~18% (unkritisch)

### ANHANG B — Fallstudie: Hallberg-Rassy 44 — Blauwasser-Netzwerk mit Redundanz

**Ausgangssituation:**
- Hallberg-Rassy 44, Baujahr 2022, 13,49m Segelyacht
- Neuinstallation für Weltumsegelung, höchste Zuverlässigkeitsanforderung
- Anforderung: redundante Navigation, Satellitenanbindung, vollständiges Monitoring

**Netzwerk-Architektur (Dual-Path):**

```
PRIMARY BACKBONE (Cockpit/Navigation):
[Term-M] ── [GPS-1 Garmin 19x] ── [MFD B&G Zeus S 12"] ── [MFD B&G Zeus S 9"]
          ── [Wind B&G WS320] ── [Autopilot B&G H5000] ── [Kompass Fluxgate]
          ── [AIS Vesper Cortex M1] ── [Ruderlagegeber]
          ── [NGW-1 Gateway → SSB-Modem]
          ── [Term-F]

SECONDARY BACKBONE (Maschinenraum/Monitoring):
[Term-M] ── [GPS-2 Garmin 19x] ── [Victron Cerbo GX]
          ── [Motor Volvo D2-40 Interface] ── [Tankgeber Diesel 1]
          ── [Tankgeber Diesel 2] ── [Tankgeber Wasser 1] ── [Tankgeber Wasser 2]
          ── [Tankgeber Fäkalien] ── [Echolot B&G ForwardScan]
          ── [IMU/Neigungssensor] ── [Temperatur Seekiste] ── [Temperatur Abgas]
          ── [Bridge → Primary Backbone]
          ── [Term-F]

SIGNALK + WIFI:
Secondary Backbone → [YDNU-02 USB] → [Raspberry Pi 5 + SignalK]
                                       ├── WiFi AP (Crew-Netz)
                                       ├── InfluxDB + Grafana
                                       ├── Anchor Alarm
                                       ├── Victron Plugin
                                       └── Iridium GO! Plugin (Positions-Tracking)
```

**Netzwerk-Kennzahlen:**

| Parameter | Primary | Secondary |
|-----------|---------|-----------|
| Geräte | 10 | 14 |
| Backbone-Länge | 14m | 16m |
| LEN | 26 | 22 |
| Backbone-Typ | Mini-C | Mini-C |
| Power-Inserter | 2 | 2 |

**Gesamtkosten:**

| Posten | Kosten |
|--------|--------|
| Backbone-Infrastruktur (beide Pfade) | 1.850 € |
| Gateways und Bridges | 980 € |
| Sensoren (Tanks, Temp, IMU) | 1.640 € |
| SignalK-Hardware | 420 € |
| Arbeitszeit (Werft, 40h) | 5.200 € |
| **Gesamt** | **10.090 €** |

### ANHANG C — Fallstudie: Beneteau Oceanis 34.1 — Budget-N2K für Wochenendsegler

**Ausgangssituation:**
- Beneteau Oceanis 34.1, Baujahr 2021, 10,34m
- Vorhandenes System: Simrad Cruise 7 MFD (N2K), B&G Triton2 Instrumente, Windgeber
- Budget: maximal 500 € für WiFi-Anbindung

**Minimale Erweiterung:**

```
Bestehend: [Term-M] ── [Wind] ── [MFD Cruise 7] ── [Triton2] ── [Echolot] ── [Term-F]

Hinzugefügt: [YDWG-02 WiFi-Gateway] (ein weiteres T-Stück + Drop-Kabel)
```

**Kosten:**

| Komponente | Kosten |
|------------|--------|
| Yacht Devices YDWG-02 | 185 € |
| T-Stück Micro-C | 20 € |
| Drop-Kabel 1m Micro-C | 15 € |
| Selbstmontage | 0 € |
| **Gesamt** | **220 €** |

**Ergebnis:**
- iPad mit Navionics zeigt Karte + Position + Wind + Tiefe
- Bester ROI aller Nachrüstungen: 220 € für vollständigen Tablet-Zugriff
- Keine Werftkosten (Selbstmontage in 30 Minuten: T-Stück in Backbone einsetzen, Drop-Kabel anschließen, fertig)

### ANHANG D — Fallstudie: Sunseeker Manhattan 66 — Motoryacht mit umfangreichem Monitoring

**Ausgangssituation:**
- Sunseeker Manhattan 66, Baujahr 2019, 20,27m Motoryacht
- Zwei MAN V8-1000 Motoren mit N2K-Interface
- Umfangreiche Bordelektrik (Generator, Klimaanlage, Hydraulik)
- Anforderung: zentrales Vessel-Monitoring mit Remote-Zugriff für den Eigner

**Netzwerk-Architektur:**

```
MAIN BACKBONE (Mid-C, 35m):
[Term-M] ── [GPS Furuno GP-39] ── [MFD Garmin 8616 (Flybridge)]
          ── [MFD Garmin 8612 (Lower Helm)] ── [Radar Garmin GMR Fantom 24]
          ── [Autopilot Garmin GHP Reactor] ── [AIS Garmin AIS 800]
          ── [Motor BB MAN V8 ECU] ── [Motor StB MAN V8 ECU]
          ── [Generator Kohler N2K Interface]
          ── [Maretron DSM410 (Engine Room)]
          ── [Tankgeber Diesel BB] ── [Tankgeber Diesel StB]
          ── [Tankgeber Diesel Day Tank] ── [Tankgeber Wasser]
          ── [Tankgeber Fäkalien Bb] ── [Tankgeber Fäkalien StB]
          ── [Tankgeber Grauwasser]
          ── [Bilge Bb] ── [Bilge StB] ── [Bilge Midship]
          ── [Temp Maschinenraum Bb] ── [Temp Maschinenraum StB]
          ── [Temp Abgas Bb] ── [Temp Abgas StB]
          ── [Batterie Service] ── [Batterie Generator]
          ── [Victron Quattro → Cerbo GX]
          ── [Maretron USB100 → PC mit N2KView]
          ── [WiFi-Gateway Actisense W2K-1]
          ── [Term-F]

MONITORING-PC (stationär im Maschinenraum):
  Maretron N2KView
  ├── 6 Dashboard-Seiten (Motor, Tanks, Elektrik, Navigation, Alarm, Übersicht)
  ├── Alarmierung per E-Mail (Bilge, Temperatur, Spannung)
  └── Datenlogging (kontinuierlich, 30-Tage-Speicher)
```

**Netzwerk-Kennzahlen:**

| Parameter | Wert |
|-----------|------|
| Geräte am Bus | 32 |
| Backbone-Länge | 35m |
| Backbone-Typ | Mid-C (2,08 mm²) |
| LEN | 38 (inkl. externe Versorgung für MFDs) |
| Power-Inserter | 3 (Flybridge, Salon, Maschinenraum) |
| Bus-Auslastung | ~35% |
| Gesamtkosten N2K-Infrastruktur | ~28.000 € (inkl. alle Sensoren, Gateways, Monitoring-PC, N2KView-Lizenz) |

### ANHANG E — Fallstudie: Catana OC50 — Katamaran-spezifische Herausforderungen

**Katamaran-spezifische Probleme:**
- Zwei Rümpfe = zwei Maschinenräume = lange Kabelwege
- Backbone muss von Rumpf zu Rumpf über die Brücke (Bridgedeck)
- Vibration im Bridgedeck-Bereich (Seeschlag bei Seegang)
- Doppelmotor mit separaten ECUs

**Lösung:**
- Mini-C Backbone (200m max.) über beide Rümpfe
- Vibrationsgedämpfte Stecker im Bridgedeck-Durchgang
- Backbone-Route: StB-Rumpf → Bridgedeck → Bb-Rumpf (Gesamtlänge: 28m)
- Zwei Power-Inserter (je einer pro Rumpf)
- Motorinstanzen korrekt zugeordnet (Motor 0 = Backbord, Motor 1 = Steuerbord)

### ANHANG F — Fallstudie: Contest 42CS — SignalK-Integration mit bestehender B&G-Installation

**Ausgangssituation:**
- Contest 42CS, Baujahr 2020, 12,50m
- Vollständiges B&G-System (Zeus3, H5000 Processor, WS320 Wind)
- Eigner möchte: Langzeit-Datenlogging, Remote-Ankerwache, Grafana-Dashboards

**Hardware-Erweiterung:**

| Komponente | Kosten |
|------------|--------|
| Raspberry Pi 4 (4 GB) | 65 € |
| Gehäuse Aluminium passiv | 20 € |
| Victron Orion 12/5-3 | 28 € |
| Yacht Devices YDNU-02 | 115 € |
| Industrial SD 32GB | 18 € |
| **Gesamt** | **246 €** |

**Software-Stack:**

```
SignalK Server v2.x
├── signalk-to-influxdb2 → InfluxDB 2.0 (lokal, 32GB SD)
├── signalk-anchor-alarm → Push-Notifications über Telegram Bot
├── signalk-venusOS → Victron-Daten (Cerbo GX bereits vorhanden)
├── signalk-derived-data → True Wind, VMG, Set/Drift
├── signalk-zones → Alarmzonen (Tiefe <3m, Spannung <12.0V)
└── Grafana → Dashboard über WiFi (http://signalk.local:3001)
```

**Ergebnis:**
- 246 € für vollständiges Datenlogging, Ankerwache und Dashboards
- Alle Daten der B&G-Installation werden erfasst und langfristig gespeichert
- Grafana-Dashboards auf iPad im Cockpit
- Telegram-Benachrichtigung bei Anker-Alarm (auch nachts an Land)

### ANHANG G — Fallstudie: Hanse 460 Charterflotte — Standardisiertes N2K für 6 Boote

**Anforderung:**
- 6× Hanse 460 in Charterflotte (Kroatien)
- Standardisierte Installation für einfache Wartung
- Flottenmonitoring (Position, Motorbetrieb, Bilge) durch Charterfirma
- Gäste-WiFi ohne Zugriff auf Navigationsdaten
- Voyage-Recording für Schadensdokumentation

**Standard-Netzwerk pro Boot:**

```
[Term-M] ── [GPS] ── [MFD Simrad NSX 12] ── [MFD Simrad NSX 9 (Cockpit)]
          ── [Wind B&G WS310] ── [Echolot] ── [Autopilot Simrad NAC-2]
          ── [Motor Yanmar N2K] ── [Tankgeber Diesel] ── [Tankgeber Wasser]
          ── [YDWG-02 WiFi (Crew, verschlüsselt)]
          ── [YDVR-04 Voyage Recorder]
          ── [YDNU-02 USB → Raspberry Pi]
          ── [Term-F]

Raspberry Pi:
├── SignalK Server
├── Tailscale VPN → Flottenmanagement-Server (Onshore)
├── signalk-to-influxdb → lokales Logging
└── Position-Tracking → Flottenmanagement-Dashboard
```

**Kosten pro Boot (nur N2K-Erweiterung, MFDs/Sensoren bereits vorhanden):**

| Komponente | Kosten |
|------------|--------|
| WiFi-Gateway YDWG-02 | 185 € |
| Voyage Recorder YDVR-04 | 145 € |
| USB-Gateway YDNU-02 | 115 € |
| Raspberry Pi + Zubehör | 110 € |
| Backbone-Erweiterung | 120 € |
| Installation (3h) | 360 € |
| **Gesamt pro Boot** | **1.035 €** |
| **Gesamt 6 Boote** | **6.210 €** |

### ANHANG H — Fallstudie: Swan 65 Refit — Migration von NMEA 0183 zu NMEA 2000

**Ausgangssituation:**
- Nautor's Swan 65, Baujahr 2005, vollständige Refit 2025
- Altes System: ausschließlich NMEA 0183 (Raymarine SeaTalk1 + 0183)
- 12 Geräte mit 0183, Kabelspaghetti mit 14 einzelnen Zweidrahtleitungen
- Anforderung: komplette Migration auf N2K mit Legacy-Kompatibilität

**Migrations-Strategie:**
1. Neuen N2K-Backbone installieren (Mini-C, 22m)
2. Alle N2K-fähigen Geräte direkt anschließen
3. Legacy-Geräte (SeaTalk1 Autopilot, alter Windgeber) über Gateways einbinden
4. Nach Migration: Legacy-Geräte schrittweise ersetzen

**Phasen der Migration:**

Phase 1 (Tag 1–2): Backbone verlegen, Terminatoren, Power-Inserter
Phase 2 (Tag 3–4): MFDs, GPS, AIS direkt an N2K
Phase 3 (Tag 5): Gateways installieren (SeaTalk1→N2K, 0183→N2K)
Phase 4 (Tag 6): Legacy-Geräte über Gateways einbinden
Phase 5 (Tag 7): Test, Kalibrierung, Dokumentation

**Ergebnis:**
- 14 Einzelkabel → 1 Backbone + Drop-Kabel
- Kabelgewicht reduziert um ca. 8 kg
- Installationszeit für Gerätewechsel: von 4h (0183-Verdrahtung) auf 15min (Drop-Kabel anstecken)
- Alle Daten auf allen Displays verfügbar (vorher: nur wenn Kabel vorhanden)
- Gesamtkosten Refit Netzwerk: ca. 14.500 € (inkl. neue MFDs)

---

## ANHANG I–R — Pydantic v2 Modelle {#anhang-i-r}

### ANHANG I — Backbone-Netzwerk-Modelle

```python
"""
AYDI NMEA 2000 Network Models — Backbone and Infrastructure
Pydantic v2 with model_config = {"from_attributes": True}
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class ConnectorType(str, Enum):
    """NMEA 2000 connector types."""
    MICRO_C = "micro_c"
    MINI_C = "mini_c"
    MID_C = "mid_c"
    SIMNET = "simnet"
    SEATALKNG = "seatalkng"
    DEVICENET = "devicenet"


class BackboneSegment(BaseModel):
    """A single backbone cable segment."""

    model_config = {"from_attributes": True}

    segment_id: str = Field(..., description="Unique segment identifier")
    connector_type: ConnectorType = Field(
        default=ConnectorType.MICRO_C,
        description="Connector type of the backbone segment",
    )
    length_m: float = Field(
        ..., gt=0, le=200, description="Segment length in meters"
    )
    cross_section_mm2: float = Field(
        ..., gt=0, description="Cable cross-section in mm²"
    )
    resistance_per_m_ohm: float = Field(
        ..., gt=0, description="Resistance per meter (round trip) in Ohm/m"
    )
    zone: str = Field(
        default="unknown",
        description="Installation zone (cockpit, engine_room, mast, etc.)",
    )
    is_shielded: bool = Field(default=True, description="Cable is shielded")
    condition: str = Field(
        default="good",
        description="Physical condition: good, fair, poor, corroded",
    )


class DropCable(BaseModel):
    """A drop cable connecting a device to the backbone."""

    model_config = {"from_attributes": True}

    drop_id: str = Field(..., description="Unique drop cable identifier")
    length_m: float = Field(
        ..., gt=0, le=6.0, description="Drop cable length in meters (max 6m)"
    )
    connector_type: ConnectorType = Field(default=ConnectorType.MICRO_C)
    connected_device_id: Optional[str] = Field(
        default=None, description="Device connected via this drop"
    )
    tee_position_m: float = Field(
        ..., ge=0, description="Position of T-piece on backbone in meters from start"
    )


class PowerInserter(BaseModel):
    """Power inserter feeding 12V into the backbone."""

    model_config = {"from_attributes": True}

    inserter_id: str = Field(..., description="Unique inserter identifier")
    position_m: float = Field(
        ..., ge=0, description="Position on backbone in meters from start"
    )
    fuse_rating_a: float = Field(
        ..., gt=0, description="Fuse rating in Amperes"
    )
    supply_voltage_v: float = Field(
        default=12.0, ge=9.0, le=16.0, description="Supply voltage in Volts"
    )
    battery_bank: str = Field(
        default="service", description="Connected battery bank"
    )
    has_integrated_fuse: bool = Field(default=True)


class Terminator(BaseModel):
    """Bus termination resistor."""

    model_config = {"from_attributes": True}

    terminator_id: str = Field(..., description="Unique terminator identifier")
    position: str = Field(
        ..., description="Position: 'start' or 'end' of backbone"
    )
    gender: str = Field(
        ..., description="Connector gender: 'male' or 'female'"
    )
    resistance_ohm: float = Field(
        default=120.0, description="Termination resistance in Ohm"
    )
    is_present: bool = Field(default=True, description="Terminator is installed")
    measured_resistance_ohm: Optional[float] = Field(
        default=None, description="Measured resistance (if tested)"
    )


class BackboneTopology(BaseModel):
    """Complete NMEA 2000 backbone topology."""

    model_config = {"from_attributes": True}

    backbone_id: str = Field(..., description="Unique backbone identifier")
    name: str = Field(..., description="Backbone name (e.g. 'Primary', 'Engine Room')")
    connector_type: ConnectorType = Field(default=ConnectorType.MICRO_C)
    segments: list[BackboneSegment] = Field(default_factory=list)
    drop_cables: list[DropCable] = Field(default_factory=list)
    power_inserters: list[PowerInserter] = Field(default_factory=list)
    terminators: list[Terminator] = Field(default_factory=list)
    total_length_m: float = Field(
        default=0.0, ge=0, description="Total backbone length in meters"
    )
    total_drop_length_m: float = Field(
        default=0.0, ge=0, description="Cumulative drop cable length in meters"
    )
    max_backbone_length_m: float = Field(
        default=100.0,
        description="Maximum allowed backbone length for this connector type",
    )
    max_cumulative_drop_m: float = Field(
        default=78.0,
        description="Maximum allowed cumulative drop cable length",
    )

    @property
    def is_length_compliant(self) -> bool:
        return self.total_length_m <= self.max_backbone_length_m

    @property
    def is_drop_compliant(self) -> bool:
        return self.total_drop_length_m <= self.max_cumulative_drop_m

    @property
    def termination_count(self) -> int:
        return sum(1 for t in self.terminators if t.is_present)

    @property
    def is_termination_correct(self) -> bool:
        return self.termination_count == 2
```

### ANHANG J — Geräte- und LEN-Modelle

```python
"""
AYDI NMEA 2000 Network Models — Device and LEN Management
Pydantic v2 with model_config = {"from_attributes": True}
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class DeviceCategory(str, Enum):
    """NMEA 2000 device categories."""
    SENSOR = "sensor"
    DISPLAY = "display"
    GATEWAY = "gateway"
    AUTOPILOT = "autopilot"
    ENGINE_INTERFACE = "engine_interface"
    TANK_SENDER = "tank_sender"
    BATTERY_MONITOR = "battery_monitor"
    AIS = "ais"
    WIFI_GATEWAY = "wifi_gateway"
    USB_GATEWAY = "usb_gateway"
    DIAGNOSTIC = "diagnostic"
    SIGNALK_SERVER = "signalk_server"
    ENERGY_MANAGER = "energy_manager"
    OTHER = "other"


class N2KDevice(BaseModel):
    """A device on the NMEA 2000 network."""

    model_config = {"from_attributes": True}

    device_id: str = Field(..., description="Unique device identifier")
    name: str = Field(..., description="Device name (e.g. 'GPS Garmin 19x')")
    manufacturer: str = Field(..., description="Manufacturer name")
    model: str = Field(..., description="Model designation")
    category: DeviceCategory = Field(..., description="Device category")
    source_address: Optional[int] = Field(
        default=None, ge=0, le=251, description="N2K source address (0-251)"
    )
    len_value: float = Field(
        ..., ge=0, description="Load Equivalency Number"
    )
    has_external_power: bool = Field(
        default=False,
        description="Device has its own power supply (not from N2K bus)",
    )
    firmware_version: Optional[str] = Field(
        default=None, description="Current firmware version"
    )
    serial_number: Optional[str] = Field(default=None)
    installation_date: Optional[datetime] = Field(default=None)
    pgn_transmitted: list[int] = Field(
        default_factory=list, description="List of PGNs this device transmits"
    )
    pgn_received: list[int] = Field(
        default_factory=list, description="List of PGNs this device receives"
    )
    instance_number: Optional[int] = Field(
        default=None,
        description="Instance number for multi-device setups (e.g. engine 0, engine 1)",
    )
    drop_cable_id: Optional[str] = Field(
        default=None, description="Connected drop cable ID"
    )
    zone: str = Field(
        default="unknown",
        description="Installation zone (cockpit, engine_room, mast, etc.)",
    )
    is_online: bool = Field(default=True, description="Device is currently online")
    last_heartbeat: Optional[datetime] = Field(
        default=None, description="Timestamp of last heartbeat (PGN 126993)"
    )


class LENBudget(BaseModel):
    """Load Equivalency Number budget calculation for a backbone."""

    model_config = {"from_attributes": True}

    backbone_id: str = Field(..., description="Backbone identifier")
    connector_type: str = Field(
        default="micro_c", description="Connector type determines max LEN"
    )
    max_len: float = Field(
        default=50.0,
        description="Maximum LEN for this connector type (50 for Micro-C, 80 for Mini-C)",
    )
    devices: list[N2KDevice] = Field(default_factory=list)

    @property
    def total_len(self) -> float:
        return sum(
            d.len_value for d in self.devices if not d.has_external_power
        )

    @property
    def total_current_a(self) -> float:
        return self.total_len * 0.05

    @property
    def len_utilization_pct(self) -> float:
        if self.max_len == 0:
            return 0.0
        return (self.total_len / self.max_len) * 100.0

    @property
    def is_within_budget(self) -> bool:
        return self.total_len <= self.max_len

    @property
    def remaining_len(self) -> float:
        return max(0.0, self.max_len - self.total_len)
```

### ANHANG K — PGN-Analyse-Modelle

```python
"""
AYDI NMEA 2000 Network Models — PGN Analysis and Data Quality
Pydantic v2 with model_config = {"from_attributes": True}
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel, Field


class PGNType(str, Enum):
    """PGN frame types."""
    SINGLE = "single"
    FAST_PACKET = "fast_packet"
    TRANSPORT = "transport"


class PGNDefinition(BaseModel):
    """Definition of a Parameter Group Number."""

    model_config = {"from_attributes": True}

    pgn: int = Field(..., ge=0, description="Parameter Group Number")
    name: str = Field(..., description="PGN name (English)")
    name_de: str = Field(..., description="PGN name (German)")
    description: str = Field(default="", description="PGN description")
    pgn_type: PGNType = Field(..., description="Frame type")
    data_length_bytes: int = Field(
        ..., ge=0, description="Data length in bytes"
    )
    default_priority: int = Field(
        default=6, ge=0, le=7, description="Default CAN priority (0=highest)"
    )
    update_rate_hz: Optional[float] = Field(
        default=None, description="Typical update rate in Hz"
    )
    is_broadcast: bool = Field(
        default=True,
        description="True if broadcast, False if peer-to-peer",
    )
    nmea_0183_equivalent: Optional[str] = Field(
        default=None,
        description="Equivalent NMEA 0183 sentence(s)",
    )


class PGNDataField(BaseModel):
    """A single data field within a PGN."""

    model_config = {"from_attributes": True}

    field_name: str = Field(..., description="Field name")
    field_name_de: str = Field(..., description="Field name (German)")
    bit_offset: int = Field(..., ge=0, description="Bit offset in PGN data")
    bit_length: int = Field(..., ge=1, description="Field length in bits")
    data_type: str = Field(
        ...,
        description="Data type: unsigned, signed, float, lookup, string",
    )
    resolution: Optional[float] = Field(
        default=None, description="Resolution per LSB"
    )
    offset_value: float = Field(
        default=0.0, description="Offset (physical = raw × resolution + offset)"
    )
    unit: Optional[str] = Field(
        default=None, description="Physical unit (SI)"
    )
    unit_display: Optional[str] = Field(
        default=None,
        description="Display unit for UI (e.g. °C instead of K)",
    )
    min_value: Optional[float] = Field(default=None)
    max_value: Optional[float] = Field(default=None)
    description: str = Field(default="")


class PGNSourceEntry(BaseModel):
    """Tracking which device sends which PGN."""

    model_config = {"from_attributes": True}

    pgn: int = Field(..., description="Parameter Group Number")
    source_address: int = Field(
        ..., ge=0, le=251, description="Source device address"
    )
    device_name: str = Field(default="", description="Device name")
    update_rate_actual_hz: Optional[float] = Field(
        default=None, description="Measured actual update rate"
    )
    is_primary_source: bool = Field(
        default=False,
        description="True if this is the preferred source for this PGN",
    )
    last_seen: Optional[datetime] = Field(default=None)
    message_count: int = Field(default=0, ge=0)
    error_count: int = Field(default=0, ge=0)


class BusLoadAnalysis(BaseModel):
    """NMEA 2000 bus load analysis result."""

    model_config = {"from_attributes": True}

    backbone_id: str = Field(..., description="Backbone identifier")
    measurement_timestamp: datetime = Field(
        ..., description="When the measurement was taken"
    )
    measurement_duration_s: float = Field(
        ..., gt=0, description="Measurement duration in seconds"
    )
    total_frames: int = Field(default=0, ge=0, description="Total CAN frames")
    error_frames: int = Field(default=0, ge=0, description="Error frames")
    bus_load_pct: float = Field(
        default=0.0, ge=0, le=100, description="Bus utilization in percent"
    )
    frames_per_second: float = Field(
        default=0.0, ge=0, description="Average frames per second"
    )
    peak_load_pct: float = Field(
        default=0.0, ge=0, le=100, description="Peak bus load in percent"
    )
    error_rate_pct: float = Field(
        default=0.0, ge=0, le=100, description="Error frame rate in percent"
    )
    unique_pgn_count: int = Field(
        default=0, ge=0, description="Number of unique PGNs observed"
    )
    unique_source_count: int = Field(
        default=0, ge=0, description="Number of unique source addresses"
    )
    pgn_sources: list[PGNSourceEntry] = Field(default_factory=list)

    @property
    def is_load_acceptable(self) -> bool:
        return self.bus_load_pct < 50.0

    @property
    def is_load_warning(self) -> bool:
        return 50.0 <= self.bus_load_pct < 70.0

    @property
    def is_load_critical(self) -> bool:
        return self.bus_load_pct >= 70.0

    @property
    def is_error_rate_acceptable(self) -> bool:
        return self.error_rate_pct < 0.1
```

### ANHANG L — Gateway-Konfigurationsmodelle

```python
"""
AYDI NMEA 2000 Network Models — Gateway Configuration
Pydantic v2 with model_config = {"from_attributes": True}
"""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class GatewayType(str, Enum):
    """Types of NMEA gateways."""
    N2K_TO_0183 = "n2k_to_0183"
    ZERO183_TO_N2K = "0183_to_n2k"
    BIDIRECTIONAL = "bidirectional"
    WIFI = "wifi"
    USB = "usb"
    ETHERNET = "ethernet"
    SEATALK1_TO_N2K = "seatalk1_to_n2k"
    SIGNALK = "signalk"
    ONENET_BRIDGE = "onenet_bridge"


class ConversionDirection(str, Enum):
    """Data conversion direction."""
    N2K_TO_0183 = "n2k_to_0183"
    ZERO183_TO_N2K = "0183_to_n2k"
    BOTH = "both"


class PGNFilter(BaseModel):
    """Filter rule for PGN conversion."""

    model_config = {"from_attributes": True}

    pgn: int = Field(..., description="PGN to filter")
    direction: ConversionDirection = Field(
        ..., description="Conversion direction"
    )
    is_enabled: bool = Field(
        default=True, description="Filter is active"
    )
    source_address_filter: Optional[int] = Field(
        default=None,
        description="Only convert from this source address (None = all)",
    )
    nmea_0183_sentence: Optional[str] = Field(
        default=None,
        description="Target NMEA 0183 sentence (e.g. 'GGA', 'MWV')",
    )
    talker_id: Optional[str] = Field(
        default=None,
        description="NMEA 0183 talker ID (e.g. 'GP', 'II')",
    )


class SentenceFilter(BaseModel):
    """Filter rule for NMEA 0183 sentence conversion."""

    model_config = {"from_attributes": True}

    sentence: str = Field(
        ..., description="NMEA 0183 sentence type (e.g. 'GGA', 'MWV')"
    )
    direction: ConversionDirection = Field(
        default=ConversionDirection.ZERO183_TO_N2K,
    )
    is_enabled: bool = Field(default=True)
    target_pgn: Optional[int] = Field(
        default=None, description="Target PGN for conversion"
    )
    input_port: Optional[int] = Field(
        default=None,
        description="NMEA 0183 input port number (for multi-port gateways)",
    )


class GatewayConfig(BaseModel):
    """Complete gateway configuration."""

    model_config = {"from_attributes": True}

    gateway_id: str = Field(..., description="Unique gateway identifier")
    gateway_type: GatewayType = Field(..., description="Gateway type")
    manufacturer: str = Field(..., description="Manufacturer")
    model: str = Field(..., description="Model name")
    firmware_version: Optional[str] = Field(default=None)
    n2k_source_address: Optional[int] = Field(
        default=None, ge=0, le=251
    )
    nmea_0183_baudrate: int = Field(
        default=4800, description="NMEA 0183 baud rate"
    )
    nmea_0183_ports_in: int = Field(
        default=1, ge=0, description="Number of NMEA 0183 input ports"
    )
    nmea_0183_ports_out: int = Field(
        default=1, ge=0, description="Number of NMEA 0183 output ports"
    )
    pgn_filters: list[PGNFilter] = Field(default_factory=list)
    sentence_filters: list[SentenceFilter] = Field(default_factory=list)
    has_data_loop_risk: bool = Field(
        default=False,
        description="True if bidirectional config could cause data loops",
    )
    notes: str = Field(default="", description="Configuration notes")


class WiFiGatewayConfig(BaseModel):
    """WiFi-specific gateway configuration."""

    model_config = {"from_attributes": True}

    gateway_id: str = Field(..., description="Reference to GatewayConfig")
    ssid: str = Field(default="N2K_WiFi", description="WiFi network name")
    password: str = Field(default="", description="WiFi password (WPA2)")
    wifi_mode: str = Field(
        default="ap",
        description="WiFi mode: 'ap', 'client', 'ap_client'",
    )
    wifi_channel: int = Field(default=6, ge=1, le=13)
    tcp_port: int = Field(
        default=10110, ge=1, le=65535, description="TCP server port"
    )
    udp_port: Optional[int] = Field(
        default=None, ge=1, le=65535, description="UDP broadcast port"
    )
    max_clients: int = Field(default=7, ge=1, le=32)
    protocol: str = Field(
        default="nmea_0183_tcp",
        description="Output protocol: nmea_0183_tcp, nmea_0183_udp, raw_n2k, signalk",
    )
    encryption: str = Field(
        default="wpa2", description="WiFi encryption: open, wpa2, wpa3"
    )
```

### ANHANG M — Fehlerbild-Modelle

```python
"""
AYDI NMEA 2000 Network Models — Fault Diagnosis
Pydantic v2 with model_config = {"from_attributes": True}
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class FaultSeverity(str, Enum):
    """Severity levels for network faults."""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


class FaultCategory(str, Enum):
    """Categories of NMEA 2000 network faults."""
    PHYSICAL = "physical"
    ELECTRICAL = "electrical"
    PROTOCOL = "protocol"
    CONFIGURATION = "configuration"
    EMC = "emc"
    FIRMWARE = "firmware"
    ENVIRONMENTAL = "environmental"


class N2KFault(BaseModel):
    """A diagnosed fault in the NMEA 2000 network."""

    model_config = {"from_attributes": True}

    fault_id: str = Field(..., description="Unique fault identifier")
    fault_code: str = Field(
        ..., description="Fault code (e.g. 'FB-N2K-01')"
    )
    severity: FaultSeverity = Field(..., description="Fault severity")
    category: FaultCategory = Field(..., description="Fault category")
    title: str = Field(..., description="Short fault title (German)")
    title_en: str = Field(..., description="Short fault title (English)")
    description: str = Field(
        ..., description="Detailed fault description (German)"
    )
    symptoms: list[str] = Field(
        default_factory=list, description="Observable symptoms (German)"
    )
    probable_causes: list[str] = Field(
        default_factory=list, description="Probable causes ranked by likelihood"
    )
    diagnostic_steps: list[str] = Field(
        default_factory=list, description="Step-by-step diagnostic procedure"
    )
    solutions: list[str] = Field(
        default_factory=list, description="Recommended solutions"
    )
    affected_devices: list[str] = Field(
        default_factory=list, description="Affected device IDs"
    )
    affected_zone: Optional[str] = Field(
        default=None, description="Affected installation zone"
    )
    estimated_repair_cost_eur: Optional[float] = Field(
        default=None, ge=0, description="Estimated repair cost in EUR"
    )
    estimated_repair_time_h: Optional[float] = Field(
        default=None, ge=0, description="Estimated repair time in hours"
    )
    confidence: str = Field(
        default="estimated",
        description="Confidence level: measured, calculated, visual_high, visual_medium, estimated",
    )
    detected_at: Optional[datetime] = Field(default=None)
    resolved_at: Optional[datetime] = Field(default=None)
    is_resolved: bool = Field(default=False)


class TerminationDiagnosis(BaseModel):
    """Result of backbone termination measurement."""

    model_config = {"from_attributes": True}

    backbone_id: str = Field(..., description="Backbone identifier")
    measured_resistance_ohm: float = Field(
        ..., ge=0, description="Measured resistance between CAN_H and CAN_L"
    )
    expected_resistance_ohm: float = Field(
        default=60.0, description="Expected resistance (2× 120Ω parallel)"
    )
    tolerance_pct: float = Field(
        default=5.0, description="Acceptable tolerance in percent"
    )
    measurement_timestamp: datetime = Field(
        ..., description="When measurement was taken"
    )
    bus_powered_during_measurement: bool = Field(
        default=False,
        description="Was the bus powered during measurement? (should be False)",
    )

    @property
    def is_correct(self) -> bool:
        tolerance = self.expected_resistance_ohm * (self.tolerance_pct / 100)
        return abs(
            self.measured_resistance_ohm - self.expected_resistance_ohm
        ) <= tolerance

    @property
    def diagnosis(self) -> str:
        r = self.measured_resistance_ohm
        if r > 10000:
            return "Keine Terminatoren installiert"
        if 110 <= r <= 130:
            return "Nur ein Terminator (120Ω)"
        if 55 <= r <= 65:
            return "Terminierung korrekt (60Ω)"
        if 35 <= r <= 45:
            return "Drei Terminatoren (40Ω) — einen entfernen"
        if r < 35:
            return "Kurzschluss oder zu viele Terminatoren"
        return f"Unerwarteter Wert: {r}Ω — Kabel und Terminatoren prüfen"


class VoltageDropDiagnosis(BaseModel):
    """Voltage drop analysis along the backbone."""

    model_config = {"from_attributes": True}

    backbone_id: str = Field(..., description="Backbone identifier")
    supply_voltage_v: float = Field(
        ..., description="Voltage at power inserter"
    )
    measurement_points: list[VoltagePoint] = Field(default_factory=list)
    min_acceptable_voltage_v: float = Field(
        default=9.0, description="Minimum acceptable voltage at any device"
    )

    @property
    def min_measured_voltage_v(self) -> float:
        if not self.measurement_points:
            return self.supply_voltage_v
        return min(p.voltage_v for p in self.measurement_points)

    @property
    def max_voltage_drop_v(self) -> float:
        return self.supply_voltage_v - self.min_measured_voltage_v

    @property
    def is_voltage_sufficient(self) -> bool:
        return self.min_measured_voltage_v >= self.min_acceptable_voltage_v


class VoltagePoint(BaseModel):
    """Voltage measurement at a specific point on the backbone."""

    model_config = {"from_attributes": True}

    position_m: float = Field(
        ..., ge=0, description="Position on backbone in meters"
    )
    voltage_v: float = Field(
        ..., ge=0, description="Measured voltage in Volts"
    )
    device_at_point: Optional[str] = Field(
        default=None, description="Device located at this point"
    )
```

### ANHANG N — SignalK-Integrationsmodelle

```python
"""
AYDI NMEA 2000 Network Models — SignalK Integration
Pydantic v2 with model_config = {"from_attributes": True}
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel, Field


class SignalKConnectionType(str, Enum):
    """Types of SignalK data connections."""
    USB_N2K = "usb_n2k"
    USB_0183 = "usb_0183"
    TCP_CLIENT = "tcp_client"
    UDP_LISTENER = "udp_listener"
    WEBSOCKET = "websocket"
    CANBUS_DIRECT = "canbus_direct"


class SignalKDataConnection(BaseModel):
    """A data connection to the SignalK server."""

    model_config = {"from_attributes": True}

    connection_id: str = Field(..., description="Unique connection identifier")
    connection_type: SignalKConnectionType = Field(
        ..., description="Connection type"
    )
    device_path: Optional[str] = Field(
        default=None,
        description="Serial device path (e.g. '/dev/ttyUSB0')",
    )
    host: Optional[str] = Field(
        default=None, description="Host for TCP/WebSocket connections"
    )
    port: Optional[int] = Field(
        default=None, ge=1, le=65535, description="Port number"
    )
    baudrate: Optional[int] = Field(
        default=None, description="Serial baud rate"
    )
    is_enabled: bool = Field(default=True)
    is_connected: bool = Field(default=False)
    messages_received: int = Field(default=0, ge=0)
    last_message_at: Optional[datetime] = Field(default=None)
    error_count: int = Field(default=0, ge=0)


class SignalKPlugin(BaseModel):
    """A SignalK server plugin."""

    model_config = {"from_attributes": True}

    plugin_id: str = Field(..., description="Plugin package name")
    name: str = Field(..., description="Display name")
    version: str = Field(default="", description="Installed version")
    is_enabled: bool = Field(default=False)
    is_running: bool = Field(default=False)
    description: str = Field(default="")
    category: str = Field(
        default="other",
        description="Plugin category: navigation, monitoring, alarm, logging, integration",
    )
    config: dict[str, Any] = Field(
        default_factory=dict, description="Plugin configuration"
    )


class SignalKServerConfig(BaseModel):
    """SignalK server configuration."""

    model_config = {"from_attributes": True}

    server_id: str = Field(..., description="Unique server identifier")
    hostname: str = Field(
        default="signalk.local", description="Server hostname"
    )
    http_port: int = Field(default=3000, ge=1, le=65535)
    vessel_name: str = Field(default="", description="Vessel name")
    vessel_mmsi: Optional[str] = Field(default=None, description="MMSI number")
    signalk_version: str = Field(default="", description="SignalK server version")
    node_version: str = Field(default="", description="Node.js version")
    platform: str = Field(
        default="linux",
        description="Platform: linux, macos, windows",
    )
    hardware: str = Field(
        default="raspberry_pi_4",
        description="Hardware platform",
    )
    connections: list[SignalKDataConnection] = Field(default_factory=list)
    plugins: list[SignalKPlugin] = Field(default_factory=list)
    uptime_s: int = Field(default=0, ge=0, description="Server uptime in seconds")
    data_points_count: int = Field(
        default=0, ge=0,
        description="Number of active data points in the data model",
    )


class SignalKDataPoint(BaseModel):
    """A single SignalK data point with metadata."""

    model_config = {"from_attributes": True}

    path: str = Field(
        ...,
        description="SignalK path (e.g. 'navigation.position')",
    )
    value: Any = Field(..., description="Current value")
    timestamp: datetime = Field(..., description="Value timestamp")
    source_label: str = Field(
        default="", description="Source device label"
    )
    source_type: str = Field(
        default="", description="Source type (NMEA2000, NMEA0183, etc.)"
    )
    source_pgn: Optional[int] = Field(
        default=None, description="Source PGN (if NMEA 2000)"
    )
    unit_si: Optional[str] = Field(
        default=None, description="SI unit"
    )
    unit_display: Optional[str] = Field(
        default=None, description="Display unit (e.g. °C, kn, ft)"
    )
    conversion_factor: Optional[float] = Field(
        default=None,
        description="Factor to convert SI to display unit",
    )
```

### ANHANG O — Netzwerk-Scoring-Modelle

```python
"""
AYDI NMEA 2000 Network Models — Network Quality Scoring
Pydantic v2 with model_config = {"from_attributes": True}
"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class NetworkScoreComponent(BaseModel):
    """A single component of the network quality score."""

    model_config = {"from_attributes": True}

    component_name: str = Field(
        ..., description="Score component name (e.g. 'termination', 'len_budget')"
    )
    component_name_de: str = Field(
        ..., description="German component name"
    )
    score: float = Field(
        ..., ge=0, le=100, description="Component score (0-100)"
    )
    weight: float = Field(
        ..., ge=0, le=1, description="Weight factor for overall score"
    )
    confidence: str = Field(
        default="estimated",
        description="Confidence level of this score",
    )
    findings: list[str] = Field(
        default_factory=list,
        description="Findings/issues found (German)",
    )
    suggestions: list[str] = Field(
        default_factory=list,
        description="Improvement suggestions (German)",
    )


class NetworkQualityScore(BaseModel):
    """Overall NMEA 2000 network quality assessment."""

    model_config = {"from_attributes": True}

    assessment_id: str = Field(
        ..., description="Unique assessment identifier"
    )
    backbone_id: str = Field(..., description="Assessed backbone ID")
    assessment_date: datetime = Field(
        ..., description="Assessment timestamp"
    )
    overall_score: float = Field(
        ..., ge=0, le=100, description="Overall network quality score (0-100)"
    )
    components: list[NetworkScoreComponent] = Field(default_factory=list)
    total_devices: int = Field(default=0, ge=0)
    total_faults: int = Field(default=0, ge=0)
    critical_faults: int = Field(default=0, ge=0)
    overall_confidence: str = Field(
        default="estimated",
        description="Overall assessment confidence",
    )
    summary_de: str = Field(
        default="",
        description="Executive summary in German",
    )
    recommendations_de: list[str] = Field(
        default_factory=list,
        description="Prioritized recommendations (German)",
    )

    @property
    def grade(self) -> str:
        if self.overall_score >= 90:
            return "A"
        if self.overall_score >= 80:
            return "B"
        if self.overall_score >= 65:
            return "C"
        if self.overall_score >= 50:
            return "D"
        return "F"

    @property
    def grade_label_de(self) -> str:
        grade_map = {
            "A": "Ausgezeichnet",
            "B": "Gut",
            "C": "Befriedigend",
            "D": "Mangelhaft",
            "F": "Ungenügend",
        }
        return grade_map.get(self.grade, "Unbekannt")
```

### ANHANG P — WiFi-Netzwerk-Modelle

```python
"""
AYDI NMEA 2000 Network Models — WiFi Network Integration
Pydantic v2 with model_config = {"from_attributes": True}
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class WiFiStandard(str, Enum):
    """WiFi standards."""
    WIFI_4 = "802.11n"
    WIFI_5 = "802.11ac"
    WIFI_6 = "802.11ax"
    WIFI_6E = "802.11ax_6ghz"


class WiFiClient(BaseModel):
    """A client connected to the marine WiFi network."""

    model_config = {"from_attributes": True}

    client_id: str = Field(..., description="Client identifier")
    mac_address: str = Field(default="", description="MAC address")
    device_type: str = Field(
        default="unknown",
        description="Device type: tablet, phone, laptop, mfd, instrument",
    )
    app_name: Optional[str] = Field(
        default=None,
        description="Navigation app (e.g. 'Navionics', 'iSailor', 'OpenCPN')",
    )
    signal_strength_dbm: Optional[float] = Field(
        default=None, description="WiFi signal strength in dBm"
    )
    is_connected: bool = Field(default=True)
    connected_since: Optional[datetime] = Field(default=None)
    data_received_bytes: int = Field(default=0, ge=0)
    protocol: str = Field(
        default="tcp",
        description="Communication protocol: tcp, udp, websocket",
    )
    port: int = Field(
        default=10110, ge=1, le=65535, description="Connection port"
    )


class MarineWiFiNetwork(BaseModel):
    """Complete marine WiFi network configuration and status."""

    model_config = {"from_attributes": True}

    network_id: str = Field(
        ..., description="Unique network identifier"
    )
    gateway_model: str = Field(..., description="WiFi gateway model")
    wifi_standard: WiFiStandard = Field(default=WiFiStandard.WIFI_4)
    ssid_navigation: str = Field(
        default="Boat_Nav", description="Navigation SSID"
    )
    ssid_guest: Optional[str] = Field(
        default=None, description="Guest SSID (no nav data access)"
    )
    channel: int = Field(default=6, ge=1, le=165)
    encryption: str = Field(default="wpa2")
    max_clients: int = Field(default=8, ge=1)
    connected_clients: list[WiFiClient] = Field(default_factory=list)
    has_internet_bridge: bool = Field(
        default=False,
        description="Gateway bridges to internet (marina WiFi, cellular, satellite)",
    )
    internet_source: Optional[str] = Field(
        default=None,
        description="Internet source: marina_wifi, cellular_4g, cellular_5g, starlink, iridium",
    )
    antenna_type: str = Field(
        default="internal",
        description="Antenna type: internal, external_omni, external_directional",
    )
    antenna_position: Optional[str] = Field(
        default=None,
        description="Antenna position on vessel",
    )
    data_protocols: list[str] = Field(
        default_factory=lambda: ["nmea_0183_tcp"],
        description="Available data protocols",
    )

    @property
    def active_client_count(self) -> int:
        return sum(1 for c in self.connected_clients if c.is_connected)
```

### ANHANG Q — Installations-Planungsmodelle

```python
"""
AYDI NMEA 2000 Network Models — Installation Planning
Pydantic v2 with model_config = {"from_attributes": True}
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class InstallationType(str, Enum):
    """Types of network installation."""
    NEW_BUILD = "new_build"
    REFIT_COMPLETE = "refit_complete"
    REFIT_EXTENSION = "refit_extension"
    SINGLE_DEVICE = "single_device"
    MIGRATION_0183_TO_N2K = "migration_0183_to_n2k"


class BoatNetworkTier(str, Enum):
    """Network complexity tiers by boat class."""
    TIER_1_BASIC = "tier_1_basic"
    TIER_2_MEDIUM = "tier_2_medium"
    TIER_3_EXTENDED = "tier_3_extended"
    TIER_4_PROFESSIONAL = "tier_4_professional"


class NetworkPlanDevice(BaseModel):
    """A device planned for the network installation."""

    model_config = {"from_attributes": True}

    device_name: str = Field(..., description="Device name")
    manufacturer: str = Field(default="")
    model: str = Field(default="")
    category: str = Field(default="sensor")
    len_value: float = Field(default=1.0, ge=0)
    has_external_power: bool = Field(default=False)
    planned_zone: str = Field(default="cockpit")
    planned_drop_length_m: float = Field(default=1.0, gt=0, le=6.0)
    estimated_cost_eur: float = Field(default=0.0, ge=0)
    is_existing: bool = Field(
        default=False, description="Device already installed"
    )
    requires_gateway: bool = Field(
        default=False, description="Device needs a gateway (e.g. 0183-only)"
    )
    notes: str = Field(default="")


class NetworkInstallationPlan(BaseModel):
    """Complete network installation plan."""

    model_config = {"from_attributes": True}

    plan_id: str = Field(..., description="Unique plan identifier")
    vessel_name: str = Field(default="")
    vessel_loa_m: float = Field(
        ..., gt=0, description="Length overall in meters"
    )
    vessel_type: str = Field(
        default="sailboat",
        description="Vessel type: sailboat, motorboat, catamaran, trawler",
    )
    installation_type: InstallationType = Field(...)
    network_tier: BoatNetworkTier = Field(...)
    planned_connector_type: str = Field(default="micro_c")
    planned_backbone_length_m: float = Field(..., gt=0)
    planned_devices: list[NetworkPlanDevice] = Field(default_factory=list)
    planned_power_inserter_count: int = Field(default=1, ge=1)
    include_wifi_gateway: bool = Field(default=True)
    include_0183_gateway: bool = Field(default=False)
    include_signalk: bool = Field(default=False)
    include_voyage_recorder: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    notes: str = Field(default="")

    @property
    def total_planned_len(self) -> float:
        return sum(
            d.len_value for d in self.planned_devices if not d.has_external_power
        )

    @property
    def total_planned_drop_length_m(self) -> float:
        return sum(d.planned_drop_length_m for d in self.planned_devices)

    @property
    def total_device_count(self) -> int:
        return len(self.planned_devices)

    @property
    def new_device_count(self) -> int:
        return sum(1 for d in self.planned_devices if not d.is_existing)

    @property
    def estimated_material_cost_eur(self) -> float:
        device_cost = sum(
            d.estimated_cost_eur
            for d in self.planned_devices
            if not d.is_existing
        )
        backbone_cost = self.planned_backbone_length_m * 8.0
        tee_cost = self.total_device_count * 20.0
        drop_cost = sum(d.planned_drop_length_m * 12.0 for d in self.planned_devices)
        terminator_cost = 50.0
        inserter_cost = self.planned_power_inserter_count * 55.0
        return (
            device_cost
            + backbone_cost
            + tee_cost
            + drop_cost
            + terminator_cost
            + inserter_cost
        )

    @property
    def estimated_labor_hours(self) -> float:
        base_hours = 4.0
        per_device = 0.75
        return base_hours + self.new_device_count * per_device
```

### ANHANG R — NMEA-OneNet- und Zukunftsmodelle

```python
"""
AYDI NMEA 2000 Network Models — OneNet and Future Technologies
Pydantic v2 with model_config = {"from_attributes": True}
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel, Field


class OneNetDeviceClass(str, Enum):
    """NMEA OneNet device classes."""
    SENSOR = "sensor"
    DISPLAY = "display"
    GATEWAY = "gateway"
    CAMERA = "camera"
    RADAR = "radar"
    SERVER = "server"
    SWITCH = "switch"
    ROUTER = "router"


class EthernetSpeed(str, Enum):
    """Ethernet connection speeds."""
    FAST_ETHERNET = "100mbps"
    GIGABIT = "1gbps"
    TWO_POINT_FIVE_GBE = "2.5gbps"
    TEN_GBE = "10gbps"


class OneNetDevice(BaseModel):
    """An NMEA OneNet device on the Ethernet network."""

    model_config = {"from_attributes": True}

    device_id: str = Field(..., description="Unique device identifier")
    name: str = Field(..., description="Device name")
    manufacturer: str = Field(default="")
    model: str = Field(default="")
    device_class: OneNetDeviceClass = Field(...)
    ip_address: Optional[str] = Field(default=None, description="IPv4 address")
    mac_address: Optional[str] = Field(default=None, description="MAC address")
    ethernet_speed: EthernetSpeed = Field(default=EthernetSpeed.FAST_ETHERNET)
    supports_poe: bool = Field(
        default=False, description="Supports Power over Ethernet"
    )
    poe_power_w: Optional[float] = Field(
        default=None, description="PoE power consumption in Watts"
    )
    supports_tsn: bool = Field(
        default=False, description="Supports Time-Sensitive Networking"
    )
    ptp_capable: bool = Field(
        default=False,
        description="Supports Precision Time Protocol (IEEE 1588)",
    )
    pgn_served: list[int] = Field(
        default_factory=list,
        description="PGNs served over OneNet",
    )
    mdns_service_name: Optional[str] = Field(
        default=None, description="mDNS/DNS-SD service name"
    )
    firmware_version: Optional[str] = Field(default=None)
    is_online: bool = Field(default=True)


class OneNetSwitch(BaseModel):
    """An Ethernet switch in the OneNet network."""

    model_config = {"from_attributes": True}

    switch_id: str = Field(..., description="Unique switch identifier")
    manufacturer: str = Field(default="")
    model: str = Field(default="")
    port_count: int = Field(..., ge=2, description="Number of Ethernet ports")
    managed: bool = Field(
        default=False, description="Managed (VLAN, QoS) or unmanaged"
    )
    supports_poe: bool = Field(default=False)
    max_poe_budget_w: Optional[float] = Field(
        default=None, description="Total PoE power budget in Watts"
    )
    supports_tsn: bool = Field(default=False)
    vlan_config: list[dict[str, Any]] = Field(
        default_factory=list, description="VLAN configuration"
    )
    is_marine_rated: bool = Field(
        default=False,
        description="Marine-rated (IP rated, wide temp, vibration)",
    )
    operating_temp_min_c: float = Field(default=-20.0)
    operating_temp_max_c: float = Field(default=60.0)
    power_consumption_w: float = Field(default=0.0, ge=0)


class OneNetTopology(BaseModel):
    """Complete NMEA OneNet network topology."""

    model_config = {"from_attributes": True}

    topology_id: str = Field(
        ..., description="Unique topology identifier"
    )
    switches: list[OneNetSwitch] = Field(default_factory=list)
    devices: list[OneNetDevice] = Field(default_factory=list)
    n2k_bridges: list[str] = Field(
        default_factory=list,
        description="Device IDs of N2K-to-OneNet bridges",
    )
    total_poe_consumption_w: float = Field(default=0.0, ge=0)
    has_internet_gateway: bool = Field(default=False)
    vlan_navigation: Optional[int] = Field(
        default=None, description="VLAN ID for navigation data"
    )
    vlan_entertainment: Optional[int] = Field(
        default=None, description="VLAN ID for entertainment/guest"
    )
    vlan_management: Optional[int] = Field(
        default=None, description="VLAN ID for management"
    )


class NetworkEvolutionAssessment(BaseModel):
    """Assessment of network readiness for future technologies."""

    model_config = {"from_attributes": True}

    assessment_id: str = Field(
        ..., description="Unique assessment identifier"
    )
    vessel_name: str = Field(default="")
    current_n2k_backbone: bool = Field(default=True)
    current_onenet: bool = Field(default=False)
    current_signalk: bool = Field(default=False)
    current_wifi_gateway: bool = Field(default=False)
    onenet_readiness_score: float = Field(
        default=0.0, ge=0, le=100,
        description="Readiness for OneNet migration (0-100)",
    )
    signalk_readiness_score: float = Field(
        default=0.0, ge=0, le=100,
        description="Readiness for SignalK integration (0-100)",
    )
    wifi6_readiness_score: float = Field(
        default=0.0, ge=0, le=100,
        description="Readiness for WiFi 6/6E upgrade (0-100)",
    )
    can_fd_readiness_score: float = Field(
        default=0.0, ge=0, le=100,
        description="Readiness for CAN FD migration (0-100)",
    )
    recommended_upgrades_de: list[str] = Field(
        default_factory=list,
        description="Recommended upgrade steps (German)",
    )
    estimated_upgrade_cost_eur: float = Field(
        default=0.0, ge=0,
        description="Total estimated upgrade cost in EUR",
    )
    assessment_date: datetime = Field(default_factory=datetime.utcnow)
    confidence: str = Field(default="estimated")
```

---

*Ende der Wissensdatei 23.06 — NMEA 2000 Vernetzung und Datennetzwerke*
*AYDI Research, Stand: 2026-05-13*
