---
title: "Kartenplotter und MFD — Raymarine Axiom, Garmin GPSMAP, Simrad NSX, B&G Zeus, Furuno NavNet"
kategorie: "23 Navigation und Elektronik"
unterkategorie: "23.02 Kartenplotter und MFD"
version: "1.0.0"
datum: "2026-05-08"
autor: "AYDI Research"
status: "validated"
confidence_quellen:
  - measured: "Hersteller-Datenblätter, CE-Zertifizierungen, IEC-Normen"
  - documented: "Hersteller-Kataloge, Installationsanleitungen, Praxistests"
  - estimated: "Erfahrungswerte, Werft-Konsens, Charterflotten-Feedback"
---

# 23.02 — Kartenplotter und MFD im Yachtbau: Vollständige Wissensreferenz

> **AYDI Wissensdatei 23.02** — Kategorie 23: Navigation und Elektronik
> **Confidence-Quelle:** measured (Hersteller-Datenblätter, IEC/NMEA-Normen), documented (Installationsanleitungen, Praxistests), estimated (Erfahrungswerte, Werft-Konsens)
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
11. [ANHANG A–H — Fallstudien](#anhang-a-h)
12. [ANHANG I–R — Pydantic v2 Modelle](#anhang-i-r)

---

## 1. Einführung und Übersicht

### 1.1 Definition und Funktion

Ein Kartenplotter (engl. chartplotter) ist ein elektronisches Navigationsgerät, das die aktuelle GPS-Position auf einer digitalen Seekarte anzeigt. Ein Multifunktionsdisplay (MFD, Multi-Function Display) erweitert diese Grundfunktion um die Integration weiterer Bordsysteme: Echolot/Fishfinder, Radar, AIS, Motorüberwachung, Autopilot-Steuerung, Wetterinformationen und Entertainment. In der modernen Yachtnavigation sind die Begriffe weitgehend austauschbar geworden, da praktisch alle aktuellen Kartenplotter als MFD ausgelegt sind.

Die zentrale Funktion eines MFD umfasst fünf Kernbereiche:

1. **Positionsbestimmung und Kartenanzeige** — GPS/GNSS-Empfang mit Darstellung auf georeferenzierten Seekarten (Vektor oder Raster)
2. **Sensorintegration** — Zusammenführung von Echolot, Radar, AIS, Wind, Tiefe, Geschwindigkeit, Motor- und Tankdaten
3. **Routenplanung und Navigation** — Wegpunkt-Management, Routenberechnung, Kursversatz-Anzeige (XTE), Ankunftszeiten
4. **Systemsteuerung** — Autopilot-Interface, Motorüberwachung, Licht- und Pumpensteuerung über NMEA 2000 oder proprietäre Busse
5. **Kommunikation** — Wi-Fi/Bluetooth-Anbindung an Mobilgeräte, Cloud-Synchronisation, App-Fernsteuerung

### 1.2 Historische Entwicklung

**Vor 1990 — Vordigitale Ära:**
- Papierseekarten als alleiniges Navigationsmittel
- Erste Sat-Nav-Empfänger (Transit-System, ab 1964) liefern nur Positionspunkte, keine Kartendarstellung
- Loran-C-Empfänger mit Gitterkarten-Overlay auf Papier
- Decca-Navigator-System in Nordeuropa (1946–2000)
- Raytheon und Furuno als Pioniere der marinen Elektronik

**1990–2000 — Erste Kartenplotter:**
- 1989: GPS-Vollausbau beginnt, erste zivile GPS-Empfänger
- 1990: Garmin GPS 100 — erster kompakter Marine-GPS-Empfänger
- 1991: Raytheon (später Raymarine) RC520 als einer der ersten dedizierten Kartenplotter
- 1993: Furuno GP-1600 mit integrierter Kartenanzeige auf CRT-Bildschirm
- 1996: Navionics und C-MAP etablieren sich als Kartendatenanbieter
- 1998: Erste Farbdisplay-Kartenplotter, Displaygrößen 5–7"
- 2000: US-Regierung schaltet Selective Availability ab — GPS-Genauigkeit springt von 100m auf 10–15m

**2000–2010 — MFD-Konvergenz:**
- 2002: Raymarine C-Series als erste echte MFD-Generation — Radar, Echolot, Karten in einem Gerät
- 2003: Garmin GPSMAP 2010 mit Farbdisplay und externer Sensorik
- 2005: Simrad NSE (Network System Explorer) setzt auf offene Netzwerkarchitektur
- 2006: NMEA 2000 (IEC 61162-3) wird zum Standard für Bord-Vernetzung
- 2007: B&G Zeus als erstes segelspezifisches MFD mit Segelrechnerfunktionen
- 2008: Furuno NavNet 3D — erste 3D-Kartendarstellung mit Satellitenfoto-Overlay
- 2009: Erste Touchscreen-MFDs kommen auf den Markt, parallel zu Tastengeräten

**2010–2020 — Touchscreen-Revolution:**
- 2012: Raymarine a-Series als erste günstige Touchscreen-MFDs
- 2013: Garmin GPSMAP 7400/7600 mit Full-HD-IPS-Displays
- 2014: Simrad NSS evo2 mit SolarMAX-Display (1.500 nits)
- 2015: B&G Zeus 3 mit SailSteer-Integration und ForwardScan
- 2016: Furuno TZT2 mit TimeZero-Software und 3D-Kartendarstellung
- 2017: Raymarine Axiom erscheint — LightHouse 3 OS, Quad-Core-Prozessor
- 2018: Wi-Fi-Integration und App-Steuerung werden Standard
- 2019: CHIRP-Echolot-Integration in allen Premium-MFDs

**2020–heute — KI und Cloud-Integration:**
- 2021: Garmin GPSMAP 84xx/86xx mit BlueChart g4 und ActiveCaptain Community
- 2022: Raymarine Axiom 2 Pro mit AI-gestützter Objekterkennung (ClearCruise AR)
- 2023: Simrad NSX mit C-MAP Discover X und neuer Hardware-Plattform
- 2024: Furuno TZT3 mit TimeZero V6 und Cloud-Routing
- 2025: B&G Zeus S mit dediziertem Sailing-Prozessor und Layline-Berechnung
- 2026: Integration von Satellite-AIS, eSIM-Konnektivität, Edge-KI für Wetterrouting

### 1.3 Bedeutung im modernen Yachtdesign

Im Kontext des AYDI-Analysesystems sind Kartenplotter und MFDs ein Design-relevanter Parameter, der folgende Module beeinflusst:

- **Ergonomie-Modul:** Displaygröße, Positionierung, Blickwinkel, Bedienbarkeit unter Wetterbedingungen bestimmen Cockpit-Design
- **Compliance-Modul:** Pflichtausrüstung nach Bootsführerschein-Verordnungen, CE-Kategorie-Anforderungen an Navigationsausrüstung
- **Kosten-Modul:** MFD-Systeme umfassen typisch 3–12% der Gesamtkosten der Elektronikausrüstung
- **Produktions-Modul:** Ausschnittmaße, Kabelführung, Busverkabelung, Montageverstärkung am Steuerstand
- **Elektrik-Modul:** Stromversorgung (12V/24V), Sicherungskonzept, EMV-Verträglichkeit
- **Service-Modul:** Software-Update-Zyklen, Kartendaten-Aktualisierung, Displayalterung

### 1.4 Marktüberblick und wirtschaftliche Bedeutung

Der weltweite Markt für marine Kartenplotter und MFDs wird auf ca. 2,1–2,6 Mrd. USD geschätzt (2025), mit einer jährlichen Wachstumsrate von 5–8%. Die Marktstruktur ist oligopolistisch mit zwei dominierenden Konzernen:

**Marktanteile (geschätzt, 2025):**

| Hersteller | Marktanteil | Kernmarkt |
|------------|------------|-----------|
| Garmin | 28–33% | Global, Freizeit + Fischerei |
| Navico-Gruppe (Simrad, B&G, Lowrance) | 22–28% | Global, Segler + Fischer |
| Raymarine (FLIR/Teledyne) | 15–20% | Europa, Freizeit + Charter |
| Furuno | 10–14% | Asien, Berufsschifffahrt + Premium-Yachten |
| Humminbird (Johnson Outdoors) | 5–8% | Nordamerika, Süßwasserfischerei |
| Sonstige (Xinuo, Onwa, Matsutec) | 5–10% | Asien, Einstiegssegment |

**Preisentwicklung:** Trotz stetig steigender Leistungsfähigkeit sind die Durchschnittspreise relativ stabil geblieben. Ein 9"-MFD der Mittelklasse kostet 2025 ca. 1.200–2.200 EUR — vergleichbar mit 2018-Preisen bei deutlich besserer Hardware.

**Trends:**
- Displaygrößen wachsen: 12" und 16" werden zum Standard, wo früher 7–9" genügten
- Touchscreen verdrängt Tastenbedienung fast vollständig (Ausnahme: Berufsschifffahrt)
- Cloud-Konnektivität: Routen, Wegpunkte, Software-Updates, Kartendaten online
- Augmented Reality (AR): Kamerabasierte Objekterkennung überlagert Live-Bild mit Navigationsdaten
- Segelsoftware-Integration: B&G und Expedition/Adrena als integrierte Segelcomputer
- Open-Source-Alternativen: OpenCPN und Signal K gewinnen bei DIY-Seglern an Bedeutung

### 1.5 Normative Grundlagen

Für die Zulassung und Prüfung von Kartenplottern und MFDs im Yachtbereich sind folgende Normen relevant:

| Norm | Geltungsbereich | Relevanz für MFD |
|------|----------------|-----------------|
| IEC 61174 (ECDIS) | Berufsschifffahrt | Referenz für Kartendarstellungsstandards |
| IEC 62288 | Darstellung von Navigationsinformationen | Symbolik, Farben, Alarme |
| IEC 61162-1/2 (NMEA 0183) | Serieller Datenbus | Legacy-Schnittstelle, noch weit verbreitet |
| IEC 61162-3 (NMEA 2000) | CAN-basierter Datenbus | Standard für moderne Vernetzung |
| IEC 60945 | Allgemeine Anforderungen Marine-Elektronik | EMV, Vibration, Wasserdichtheit |
| IP67/IP68 | Schutzart | Wasserbeständigkeit des Displays |
| IEC 60945 (Kompass-Sicherheitsabstand) | Magnetkompass-Sicherheitsabstand | Mindestabstand MFD zu Kompass |

---

## 2. Grundlagen und Theorie

### 2.1 Displaytechnologie

Die Displaytechnologie ist der zentrale Qualitätsfaktor eines MFD. Auf See gelten besondere Anforderungen: direkte Sonneneinstrahlung, wechselnde Blickwinkel, Salzwasserbenetzung, Vibrationen, Temperaturextreme.

#### 2.1.1 Panel-Typen

**TFT (Thin Film Transistor):**
- Basis-Technologie für alle LCD-Displays
- Verschiedene Panel-Subtypen: TN, VA, IPS
- TN-Panels (Twisted Nematic) in Einstiegsgeräten: enger Blickwinkel (±40°), günstig
- VA-Panels (Vertical Alignment) als Mittelklasse: besserer Kontrast als IPS, aber engerer Blickwinkel

**IPS (In-Plane Switching):**
- Premium-Standard in allen aktuellen MFDs ab Mittelklasse
- Blickwinkelstabilität: ±178° horizontal und vertikal
- Farbtreue bleibt über den gesamten Blickwinkelbereich erhalten
- Etwas höherer Stromverbrauch als TN/VA
- Leicht reduzierter Schwarzwert gegenüber VA (typisch 1000:1 vs. 3000:1 Kontrast)
- Alle aktuellen Premium-MFDs (Raymarine Axiom 2 Pro, Garmin 8600, Simrad NSX, B&G Zeus S, Furuno TZT3) verwenden IPS

**OLED / MicroLED:**
- Bisher nicht im Marine-MFD-Segment etabliert
- Probleme: Einbrennen bei statischen Kartenbildern, Helligkeit unter direkter Sonne noch unzureichend
- Potential für zukünftige Generationen, insbesondere bei flexiblen Displays

#### 2.1.2 Bonding-Technologie

Optisches Bonding bezeichnet das lückenlose Verkleben der Glasoberfläche mit dem LCD-Panel, wodurch der Luftspalt eliminiert wird.

**Vorteile von Optical Bonding:**
- Reduktion von Reflexionen um 30–50% durch Wegfall der Glas-Luft-Grenzfläche
- Verbesserte Sonnenlichtablesbarkeit (1 Reflexionsschicht weniger)
- Erhöhte mechanische Stabilität (Glas und Panel bilden eine Einheit)
- Kein Beschlagen zwischen Glas und Panel bei Temperaturschwankungen
- Bessere Wärmeableitung vom Panel

**Status bei aktuellen MFDs:**
- Raymarine Axiom 2 Pro / XL: Optically Bonded IPS
- Garmin GPSMAP 84xx/86xx: Optically Bonded
- Simrad NSX: Optically Bonded (SolarMAX IPS)
- B&G Zeus S: Optically Bonded
- Furuno TZT3: Optically Bonded
- Einstiegsgeräte (Garmin echoMAP, Raymarine Element): teilweise noch ohne Bonding

#### 2.1.3 Helligkeit und Sonnenlichtablesbarkeit

Die Displayhelligkeit wird in Nits (cd/m²) gemessen. Für Marine-Anwendungen ist hohe Helligkeit essenziell:

| Helligkeitsstufe | Nits | Einsatztauglichkeit |
|-------------------|------|-------------------|
| < 500 nits | Niedrig | Nur für Innenbereich (Navigationstisch unter Deck) |
| 500–800 nits | Mittel | Unter Bimini/Sprayhood lesbar, bei direkter Sonne eingeschränkt |
| 800–1.200 nits | Gut | Außencockpit bei bewölktem Himmel und Dämmerung gut lesbar |
| 1.200–1.800 nits | Sehr gut | Direkte Sonneneinstrahlung, gute Ablesbarkeit |
| 1.800–3.000 nits | Exzellent | Volle Lesbarkeit auch bei Gegenlicht und nasser Displayoberfläche |

**Helligkeitswerte aktueller MFDs (typisch/maximal):**

| Modell | Typische Helligkeit | Maximale Helligkeit |
|--------|-------------------|-------------------|
| Raymarine Axiom 2 Pro 9" | 1.200 nits | 1.500 nits |
| Raymarine Axiom 2 XL 16" | 1.500 nits | 2.000 nits |
| Garmin GPSMAP 8616xsv | 1.800 nits | 1.800 nits |
| Simrad NSX 3009 | 2.000 nits | 2.500 nits |
| B&G Zeus S 9" | 1.500 nits | 2.000 nits |
| Furuno TZT3 12" | 1.000 nits | 1.200 nits |
| Garmin GPSMAP 1243xsv | 1.200 nits | 1.500 nits |

**Hinweis:** Die Helligkeitswerte beziehen sich auf die maximale Stufe bei aktivem Automatik-Dimmer. Im Nachtmodus reduzieren alle MFDs auf 1–5 nits, um die Nachtsicht der Crew nicht zu beeinträchtigen.

#### 2.1.4 Anti-Reflexions-Beschichtung

Alle Marine-MFDs verwenden mehrschichtige Anti-Reflexions-Beschichtungen:
- **AR-Coating (Anti-Reflective):** Reduziert Spiegelungen auf der Glasoberfläche
- **AG-Coating (Anti-Glare):** Matte Oberfläche streut einfallendes Licht, reduziert Blendung bei punktueller Sonneneinstrahlung
- **Oleophobe Beschichtung:** Reduziert Fingerabdrücke und erleichtert Bedienung mit nassen Händen
- Kombination aus AR + AG + oleophob ist bei Premium-Geräten Standard

### 2.2 Touchscreen vs. Tastenbedienung

#### 2.2.1 Touchscreen-Technologien im Marine-Bereich

**Projiziert-kapazitiv (PCAP):**
- Standard bei allen aktuellen Marine-Touchscreens
- Multi-Touch-Fähigkeit (Pinch-to-Zoom, Zwei-Finger-Rotation)
- Funktioniert mit dünnen Handschuhen (kapazitiv leitend)
- Problematisch bei starkem Regen oder Wasserfilm auf dem Display (Phantom-Touches)
- Alle Premium-MFDs verwenden PCAP mit marine-spezifischer Firmware zur Unterdrückung von Regen-/Spritzwasser-Fehlbedienungen

**Resistiv:**
- Veraltete Technologie, nur noch in wenigen Einstiegsgeräten
- Funktioniert mit allen Handschuhtypen und bei nassem Display
- Keine Multi-Touch-Fähigkeit
- Geringere optische Klarheit (zusätzliche Folien reduzieren Helligkeit)

#### 2.2.2 Hybride Bedienkonzepte

Die ideale Bedienung eines Marine-MFD variiert je nach Situation:

| Situation | Optimale Bedienung | Begründung |
|-----------|-------------------|------------|
| Ruhiges Wetter, Hafen | Touchscreen | Intuitive, schnelle Bedienung |
| Seegang (Beaufort 3–5) | Tasten + Drehgeber | Haptisches Feedback, Stützen am Gerät |
| Schwerer Seegang (Beaufort 6+) | Dedizierte Tasten | Eindeutige Betätigung auch ohne Blickkontakt |
| Regen, Gischt | Tasten oder kapazitive Tasten | Touchscreen-Fehlbedienung durch Wassertropfen |
| Nachtnavigation | Tasten mit Hintergrundbeleuchtung | Vermeidung versehentlicher Bildschirmberührung |
| Schnelle Kursänderung | Drehgeber/Joystick | Präzise inkrementelle Eingabe |

**Hersteller-Ansätze:**
- Raymarine Axiom 2 Pro: Reiner Touchscreen, optionale RMK-10 Remote-Tastatur
- Garmin GPSMAP 86xx: Touchscreen + dedizierte Tasten am Gehäuserand
- Simrad NSX: Reiner Touchscreen, System-Controller OP50 als Fernbedienung
- B&G Zeus S: Reiner Touchscreen + dedizierte ZC2-Fernsteuerung mit Drehgeber
- Furuno TZT3: Touchscreen + optionales MCU-006 Remote mit Joystick

#### 2.2.3 Fernbedienungsoptionen

Für Steuerstand-Installationen, bei denen das MFD außer Reichweite ist, bieten alle Hersteller Fernbedienungen an:

| Hersteller | Fernbedienung | Typ | Schnittstelle | Preis (ca.) |
|------------|--------------|------|--------------|------------|
| Raymarine | RMK-10 | Keypad + Drehgeber | Ethernet | 350 EUR |
| Garmin | GRID 20 | Joystick + Tasten | NMEA 2000 | 280 EUR |
| Simrad | OP50 | Drehgeber + Tasten | Ethernet | 400 EUR |
| B&G | ZC2 | Drehgeber + Tasten | Ethernet | 450 EUR |
| Furuno | MCU-006 | Joystick + Tasten | Ethernet | 500 EUR |

### 2.3 Kartenmaterial und Kartenformate

#### 2.3.1 Vektor- vs. Rasterkarten

**Vektorkarten:**
- Seekarteninhalte als geometrische Objekte (Punkte, Linien, Flächen) gespeichert
- Stufenlos zoombar ohne Qualitätsverlust
- Objekte sind abfragbar (Tippen auf Tonne zeigt deren Eigenschaften)
- Karteninhalte können nach Relevanz ein-/ausgeblendet werden
- Geringerer Speicherbedarf pro Kartenblatt
- Standard für alle modernen MFDs: C-MAP, Navionics, Garmin BlueChart

**Rasterkarten:**
- Gescannte Papierseekarten (offiziell: RNC — Raster Navigational Charts)
- Vertrautes Erscheinungsbild der offiziellen Papierseekarte
- Qualität abhängig von der Scan-Auflösung
- Beim Zoomen: Pixelbildung bei hoher Vergrößerung
- Keine interaktiven Objektinformationen
- Zunehmend durch hochauflösende Vektorkarten verdrängt

#### 2.3.2 Kartenanbieter und Kompatibilität

Die Kartendatenlandschaft ist fragmentiert und herstellergebunden:

**C-MAP (Navico/Lowrance/Simrad/B&G):**
- Eigentum von Navico (Jetzt Teil der Brunswick Corporation)
- Kartenebenen: Discover (Basis), Reveal (Premium mit Bathymetrie), Discover X (neueste Generation)
- Kartenmaterial: S-57-basierte Vektorkarten, satellitengestützte Bathymetrie
- Kompatibel mit: Simrad, B&G, Lowrance, Raymarine (über Kompatibilitätsmodus)
- Abdeckung: Weltweit, Schwerpunkt Nordamerika und Europa
- Update-Modell: Einmalkauf oder Jahresabo (Discover X: ca. 100–250 EUR/Jahr)

**Navionics (Garmin):**
- Seit 2017 Eigentum von Garmin
- Kartenebenen: Navionics+ (Standard), Platinum+ (Premium mit Satellitenfoto)
- Kartenmaterial: Vektorkarten mit Community-Tiefendaten (SonarChart)
- Kompatibel mit: Garmin, Raymarine, Humminbird, diverse Drittanbieter
- Abdeckung: Weltweit, exzellente Abdeckung für Küstennavigation
- Update-Modell: Jahresabo (Navionics+: ca. 80–120 EUR/Jahr)
- Besonderheit: Navionics Boating App als Companion-App für Smartphone

**Garmin BlueChart (exklusiv Garmin):**
- Garmin-eigenes Kartenformat
- BlueChart g4 (seit 2021) mit Auto Guidance und Relief Shading
- Nur auf Garmin-Geräten verwendbar
- Integriert ActiveCaptain Community-Daten (Hafen-Reviews, Gefahrenmeldungen)
- Besonderheit: Auto Guidance berechnet kartenbasierte Routen unter Berücksichtigung von Tiefe und Hindernissen

**Furuno TZ Maps:**
- Exklusiv für Furuno TZT-Serie (TimeZero-basiert)
- Basierend auf MaxSea TimeZero-Kartentechnologie
- 3D-Bodentopographie als Alleinstellungsmerkmal
- Abdeckung: Global, mit besonderer Stärke im Pazifikraum
- Update: Jahresabo (TZ Maps: ca. 120–200 EUR/Jahr)

**Offizielle elektronische Seekarten (ENC):**
- S-57/S-63 Format (IHO-Standard)
- Herausgegeben von nationalen Hydrographischen Diensten (BSH für Deutschland)
- Pflicht für Berufsschifffahrt (ECDIS), optional für Sportboote
- Zunehmend direkt in MFDs importierbar
- OpenCPN und Signal K verwenden primär offizielle ENCs

#### 2.3.3 Kartendaten-Genauigkeit und Einschränkungen

**Grundsätzliche Limitierungen aller digitalen Seekarten:**
- Seekarten sind keine vermessungstechnischen Dokumente — sie enthalten generalisierte Tiefenwerte
- Vermessungsstand kann Jahrzehnte alt sein (besonders in wenig befahrenen Gebieten)
- Tiefenangaben beziehen sich auf Kartennull (Chart Datum), nicht auf aktuellen Wasserstand
- Digitalkarten ersetzen NICHT die Pflicht zur sorgfältigen Wache und Papierkarten-Backup

**Genauigkeitsvergleich:**

| Datentyp | Genauigkeit | Quelle |
|----------|------------|--------|
| GPS-Position (GNSS) | 2–5 m (95%) | GNSS-Empfänger im MFD |
| GPS-Position + WAAS/EGNOS | 1–2 m (95%) | Korrekturservice (kostenlos) |
| Vektorkarte Küstenbereich | 5–25 m | Abhängig vom Vermessungsstand |
| Vektorkarte Offshore | 50–200 m | Abhängig vom Vermessungsstand |
| Navionics SonarChart | 0,5–2 m (Tiefe) | Community-basierte Echolotdaten |
| Satellitenbathymetrie | 10–50 m (Position), ±2 m (Tiefe) | Satellitengestützte Schätzung |

### 2.4 Vernetzung und Protokolle

#### 2.4.1 NMEA 2000 (IEC 61162-3)

**Grundprinzip:**
NMEA 2000 ist ein CAN-basierter (Controller Area Network) Datenbus nach IEC 61162-3, der alle Bordsensoren und -geräte über ein gemeinsames Netzwerk verbindet. Jedes Gerät sendet und empfängt standardisierte Datenpakete (PGNs — Parameter Group Numbers).

**Technische Eckdaten:**
- Busgeschwindigkeit: 250 kBit/s (CAN 2.0B)
- Maximale Buslänge: 100 m (Backbone)
- Maximale Stichleitungslänge: 6 m (Drop-Cable)
- Maximale Geräteanzahl: 50 pro Netzwerk
- Stromversorgung: über den Bus (12V, max. 3A pro Gerät via LEN-System)
- Steckertyp: Micro-C (5-polig, M12) als Standard, Mini-C für größere Geräte
- Terminierung: 120-Ohm-Widerstände an beiden Bus-Enden erforderlich

**Typische PGN-Zuordnungen für MFDs:**

| PGN | Datentyp | Sender |
|-----|----------|--------|
| 127250 | Vessel Heading (Magnetkompass) | Kompass-Sensor |
| 128259 | Speed (Logge) | Geschwindigkeitssensor |
| 128267 | Water Depth (Echolot) | Geber/Transducer |
| 130306 | Wind Data | Windmesser |
| 129025 | Position (Rapid Update) | GPS-Empfänger |
| 129026 | COG/SOG (Rapid Update) | GPS-Empfänger |
| 127488 | Engine Parameters (Rapid Update) | Motor-Gateway |
| 127489 | Engine Parameters (Dynamic) | Motor-Gateway |
| 129038/039 | AIS Class A/B Reports | AIS-Transponder |
| 130310 | Environmental Parameters | Umgebungssensoren |
| 65280–65535 | Herstellerspezifische PGNs | Diverse |

#### 2.4.2 NMEA 0183 (Legacy)

**Grundprinzip:**
NMEA 0183 ist ein älteres serielles Datenprotokoll (RS-422), das nach wie vor weit verbreitet ist, insbesondere für die Kommunikation mit älteren Geräten.

**Technische Eckdaten:**
- Baudrate: 4.800 Baud (Standard), 38.400 Baud (High Speed für AIS)
- Punkt-zu-Punkt oder 1-Sender/mehrere-Empfänger (Talker/Listener)
- ASCII-basierte Datensätze (Sentences), lesbar mit Terminalprogramm
- Max. 1 Talker, bis zu 3 Listener pro Anschluss
- Keine Stromversorgung über den Bus

**Wichtige NMEA-0183-Sentences:**

| Sentence | Inhalt |
|----------|--------|
| $GPGGA | GPS Fix Data (Position, Qualität, Satellitenanzahl) |
| $GPRMC | Recommended Minimum (Position, Kurs, Geschwindigkeit) |
| $GPVTG | Course Over Ground / Speed Over Ground |
| $SDDBT | Depth Below Transducer |
| $WIMWV | Wind Speed and Angle |
| $HCHDG | Heading (Magnetkompass) |
| $GPAPB | Autopilot Sentence B (Kursabweichung) |
| !AIVDM | AIS-Nachricht |

#### 2.4.3 Ethernet-Vernetzung

Moderne MFDs nutzen Ethernet (100 Mbit/s oder 1 Gbit/s) für die Hochgeschwindigkeits-Datenübertragung:

**Anwendungen:**
- Radar-Daten (hochauflösend, hohe Datenrate)
- Display-Synchronisation (mehrere MFDs zeigen gleiche Ansicht)
- IP-Kameras (ONVIF-kompatibel bei einigen Herstellern)
- Software-Updates über das Netzwerk
- Integration externer Rechner (z.B. Expedition auf PC)

**Hersteller-Netzwerke:**
- Raymarine: SeaTalkng (NMEA-2000-kompatibel) + Ethernet (RayNet)
- Garmin: Garmin Marine Network (proprietäres Ethernet)
- Simrad/B&G: SimNet (NMEA-2000-kompatibel) + Ethernet
- Furuno: Furuno CAN bus + Ethernet (NavNet-Netzwerk)

#### 2.4.4 Drahtlose Konnektivität

**Wi-Fi:**
- Standard bei allen aktuellen MFDs (802.11 b/g/n, zunehmend ac)
- Nutzung: App-Fernsteuerung, Kartenupdates, Cloud-Sync
- Reichweite: typisch 15–30 m (ausreichend für Bordnutzung)
- Sicherheit: WPA2-PSK Standard

**Bluetooth:**
- Bluetooth 4.2 LE oder 5.0 in aktuellen Geräten
- Nutzung: Musik-Streaming (über angeschlossene Verstärker), Sensor-Kopplung, Headset
- Begrenzte Nutzung für Navigationsdaten (Bandbreite, Zuverlässigkeit)

**Companion-Apps der Hersteller:**

| Hersteller | App | Plattform | Funktionsumfang |
|------------|-----|-----------|----------------|
| Raymarine | RayControl | iOS/Android | Volle MFD-Fernsteuerung |
| Garmin | ActiveCaptain | iOS/Android | Kartenupdate, Community, Routing |
| Simrad | Simrad App | iOS/Android | Fernsteuerung, Updates |
| B&G | B&G App | iOS/Android | Segeldaten, Karten, Fernsteuerung |
| Furuno | TZ iBoat | iOS/Android | Kartenanzeige, Routing |

### 2.5 GPS/GNSS-Technologie in MFDs

#### 2.5.1 GNSS-Systeme

Aktuelle MFDs empfangen Signale von mehreren Satellitennavigationssystemen gleichzeitig:

| System | Betreiber | Satelliten | Status |
|--------|----------|-----------|--------|
| GPS | USA | 31 aktiv | Voll operativ |
| GLONASS | Russland | 24 aktiv | Voll operativ |
| Galileo | EU | 28 aktiv | Voll operativ seit 2024 |
| BeiDou | China | 35 aktiv | Voll operativ |

**Multi-GNSS-Empfang:** Alle aktuellen Premium-MFDs empfangen GPS + GLONASS + Galileo. Der Vorteil: mehr sichtbare Satelliten = bessere Genauigkeit, schnellerer Fix, bessere Abdeckung in schwierigen Umgebungen (enge Häfen, hohe Berge, Brücken).

#### 2.5.2 Genauigkeitsklassen

| Methode | Genauigkeit (95%) | Verfügbarkeit |
|---------|-------------------|---------------|
| Standard GPS (L1) | 3–5 m | Global |
| Multi-GNSS (L1) | 2–3 m | Global |
| WAAS/EGNOS (L1 + Korrektursignal) | 0,5–1,5 m | Nordamerika / Europa |
| Multi-Frequenz (L1 + L5) | 0,3–1 m | In neuesten Empfängern |
| DGNSS (Korrektursignal terrestrisch) | 0,5–2 m | Küstenbereich |
| PPP (Precise Point Positioning) | 0,1–0,3 m | Kommerzieller Dienst |

#### 2.5.3 Interner vs. externer GPS-Empfänger

**Interner GPS-Empfänger (im MFD eingebaut):**
- Vorteil: Kein zusätzliches Gerät, kein Kabel, sofort einsatzbereit
- Nachteil: Position der GPS-Antenne ist Display-abhängig, oft unter Bimini oder hinter Scheibe → reduzierter Empfang
- Nachteil: GPS-Position entspricht Display-Position, nicht dem Schiffsmittelpunkt

**Externer GPS-Empfänger (separate Antenne + Empfänger):**
- Vorteil: Antenne am höchsten Punkt montierbar (Mast, Geräteträger) → optimaler Empfang
- Vorteil: Position kann auf Schiffsmittelpunkt kalibriert werden
- Vorteil: Multi-GNSS und Multi-Frequenz oft erst in externen Empfängern verfügbar
- Nachteil: Zusätzliche Kosten (150–600 EUR), Kabelführung, Montage

**Empfehlung nach Bootstyp:**

| Bootstyp | GPS-Empfehlung | Begründung |
|----------|---------------|------------|
| Sportboot < 8 m | Intern ausreichend | Kurze Distanzen, freie Sicht |
| Segelyacht 8–15 m | Extern empfohlen | Mast-/Geräteträgermontage, stabiler Fix |
| Motoryacht 10–20 m | Intern + Extern als Backup | Flybridge bietet gute Interne Position |
| Blauwasseryacht > 12 m | Extern + Backup | Redundanz für Langfahrt essenziell |
| Regattayacht | Extern zwingend | Maximale Genauigkeit für Taktik |

### 2.6 Echolot-Integration

#### 2.6.1 Geber-Technologien

Moderne MFDs integrieren Echolot-Funktionen direkt — entweder über eingebaute Echolot-Module oder über externe Blackbox-Echolote im Netzwerk.

**Transducer-Typen und Eignung:**

| Technologie | Frequenz | Tiefe max. | Auflösung | Eignung |
|-------------|----------|-----------|-----------|---------|
| Standard (Single-Freq.) | 50 kHz oder 200 kHz | 300–600 m | Gering | Kreuzfahrt, Tiefenmessung |
| Dual-Frequenz | 50 + 200 kHz | 600 m | Mittel | Allround, Standard-Fischfinder |
| CHIRP (Compressed High-Intensity Radar Pulse) | 28–210 kHz (Sweep) | 900 m | Hoch | Premium-Echolot, Fischortung |
| DownScan / StructureScan | 455/800 kHz | 60–90 m | Sehr hoch | Bodenstruktur-Darstellung |
| SideScan | 455/800 kHz | 60–90 m seitlich | Sehr hoch | Bodenstruktur seitlich |
| ForwardScan | 180 kHz | 90 m voraus | Mittel | Grundberührungs-Warnung (voraus) |
| 3D / RealVision | Multi-Element | 90 m | 3D-Darstellung | Wrack-/Riffdarstellung |

#### 2.6.2 ForwardScan-Technologie (B&G / Simrad)

ForwardScan ist eine von Simrad/B&G entwickelte Sonar-Technologie, die den Meeresboden voraus des Bootes erfasst:

**Funktionsweise:**
- Spezieller Transducer sendet nach vorn gerichteten Sonarstrahl aus
- Erfasst Boden und Hindernisse bis 90 m voraus
- Darstellung als farbcodierte Voraus-Karte auf dem MFD
- Alarm bei Tiefe unter definiertem Schwellwert

**Technische Parameter:**
- Frequenz: 180 kHz
- Reichweite voraus: bis 90 m (abhängig von Tiefe und Geschwindigkeit)
- Optimal bei: Geschwindigkeit < 8 kn, Tiefe < 30 m
- Transducer: dedizierter ForwardScan-Geber (separate Montage, nicht kombinierbar mit Standard-Echolot)
- Kompatible MFDs: Simrad NSX, NSO Evo3, NSS Evo3; B&G Zeus S, Zeus 3, Vulcan

### 2.7 Radar-Integration

#### 2.7.1 Radar-Typen für Yachten

| Typ | Sendeleistung | Reichweite | Auflösung | Eignung |
|-----|--------------|-----------|-----------|---------|
| Puls-Radar (Magnetron) | 2–4 kW | 24–48 nm | Mittel | Offshore, bewährt, günstig |
| Puls-Kompression (Solid-State) | 25–50 W (Spitze) | 36–72 nm | Hoch | Premium, energiesparend |
| Broadband (FMCW) | < 5 W | 24–36 nm | Sehr hoch (Nahbereich) | Nahbereich, Kollisionsvermeidung |
| Doppler (mit Zielklassifizierung) | Variabel | 36–96 nm | Hoch + Bewegungserkennung | Premium, MARPA + |

**Aktuelle Radar-Modelle der MFD-Hersteller:**

| Hersteller | Radar-Serie | Typ | Besonderheit |
|------------|------------|------|-------------|
| Raymarine | Quantum 2 | CHIRP Pulse Compression | Doppler-Zielklassifizierung |
| Garmin | GMR Fantom | Solid-State Pulse Compression | MotionScope Doppler |
| Simrad | HALO | Pulse Compression | Dual-Range-Darstellung |
| B&G | HALO (gleich wie Simrad) | Pulse Compression | VelocityTrack |
| Furuno | DRS | Solid-State + Magnetron | NXT als Kompakt-Broadband |

### 2.8 AIS-Integration (Automatic Identification System)

#### 2.8.1 AIS-Klassen und MFD-Darstellung

| AIS-Klasse | Funktion | Pflicht für | MFD-Darstellung |
|------------|----------|------------|----------------|
| Klasse A | Senden + Empfangen | Berufsschifffahrt > 300 GT | Dreieck mit Kursvektor + MMSI |
| Klasse B | Senden + Empfangen (reduziert) | Freiwillig für Sportboote | Dreieck mit Kursvektor + MMSI |
| Klasse B+ (SOTDMA) | Senden + Empfangen (verbessert) | Freiwillig | Wie Klasse A, mit Priorität |
| Nur-Empfänger | Nur Empfangen | — | Anzeige anderer Schiffe |

**MFD-Funktionen mit AIS:**
- Overlay auf Seekarte: AIS-Ziele als Dreiecke mit Kursvektor und CPA/TCPA
- CPA-Alarm (Closest Point of Approach): Warnung bei Annäherung unter definierten Abstand
- TCPA-Alarm (Time to CPA): Zeitwarnung
- Zieldetails: Schiffsname, MMSI, Kurs, Geschwindigkeit, Zielhafen, Ladung
- Buddy-Tracking: markierte Schiffe hervorheben (z.B. Regattafeld)
- MOB-AIS: Empfang von AIS-SART und AIS-MOB-Sendern

---

## 3. Typenübersicht

### 3.1 Entry-Level MFDs (7", Einstiegsklasse)

**Typische Spezifikationen:**
- Displaygröße: 7" (17,8 cm Diagonale)
- Auflösung: 800 × 480 px (WVGA) bis 1024 × 600 px (WSVGA)
- Helligkeit: 500–1.000 nits
- GPS: intern, GPS + GLONASS
- Echolot: oft integriert (CHIRP + DownScan/ClearVü)
- Kartenmaterial: vorinstallierte Basiskarte, optionale Premiumkarten
- Vernetzung: NMEA 0183, teilweise NMEA 2000, Wi-Fi
- Preis: 500–1.200 EUR

**Typische Vertreter:**
- Garmin echoMAP UHD2 72sv (799 EUR)
- Raymarine Element 7 HV (649 EUR)
- Lowrance Eagle 7 (599 EUR)
- Simrad Cruise 7 (549 EUR)

**Einsatzgebiet:**
- Tagesausflügler, Anglerboote, kleine Segelboote
- Binnenreviere, Küstennah
- Retrofit auf älteren Booten als günstiges Upgrade
- Zweitdisplay am Navigationstisch

**Limitierungen:**
- Eingeschränkte Netzwerkfähigkeit (kein Ethernet bei den meisten Modellen)
- Kein Radar-Anschluss oder nur eingeschränkt
- Oft kein Autopilot-Interface
- Display bei direkter Sonneneinstrahlung eingeschränkt lesbar
- Prozessorleistung für komplexe Routing-Aufgaben begrenzt

### 3.2 Mid-Range MFDs (9–12", Mittelklasse)

**Typische Spezifikationen:**
- Displaygröße: 9" (22,9 cm) oder 12" (30,5 cm)
- Auflösung: 1280 × 720 px (HD) bis 1920 × 1080 px (Full HD)
- Helligkeit: 1.000–2.000 nits
- GPS: intern + externe Antenne empfohlen
- Echolot: optional intern oder extern (CHIRP, StructureScan, SideScan)
- Kartenmaterial: Premium-Karten vorinstalliert oder optional
- Vernetzung: NMEA 2000, NMEA 0183, Ethernet, Wi-Fi, Bluetooth
- Radar: Radar-fähig (über Ethernet)
- Autopilot: volle AP-Steuerung über NMEA 2000 oder proprietären Bus
- Preis: 1.200–3.500 EUR

**Typische Vertreter:**
- Raymarine Axiom 2 Pro 9" / 12" (1.899 / 2.499 EUR)
- Garmin GPSMAP 923xsv / 1223xsv (1.599 / 2.299 EUR)
- Simrad NSX 3009 / 3012 (1.699 / 2.399 EUR)
- B&G Zeus S 9" / 12" (2.099 / 2.799 EUR)
- Furuno TZT3 9" / 12" (2.299 / 2.999 EUR)

**Einsatzgebiet:**
- Segelyachten 8–15 m, Motoryachten 8–14 m
- Küsten- und Offshore-Navigation
- Einhand-Segler (großes Display von Cockpit aus lesbar)
- Haupt-MFD am Steuerstand
- Integration von Radar, Echolot, AIS, Autopilot

**Stärken:**
- Optimales Preis-Leistungs-Verhältnis
- Volle Netzwerkfähigkeit
- Ausreichende Bildschirmgröße für Splitscreen (Karte + Echolot)
- Gute Sonnenlichtablesbarkeit
- Alle Hersteller bieten 9"- und 12"-Modelle als Kernprodukt

### 3.3 High-End MFDs (16"+, Premiumklasse)

**Typische Spezifikationen:**
- Displaygröße: 16" (40,6 cm), 19" (48,3 cm), 22" (55,9 cm), 24" (61 cm)
- Auflösung: 1920 × 1080 px (Full HD) bis 3840 × 2160 px (4K)
- Helligkeit: 1.500–3.000 nits
- GPS: extern empfohlen (intern als Backup)
- Echolot: immer extern (Black-Box-Echolot über Ethernet)
- Kartenmaterial: Premiumkarten, Multi-Chart-Fähigkeit
- Vernetzung: Dual Ethernet, NMEA 2000, NMEA 0183, Wi-Fi, Bluetooth
- Preis: 3.500–12.000 EUR

**Typische Vertreter:**
- Raymarine Axiom 2 XL 16" / 19" / 22" (3.999 / 5.999 / 8.499 EUR)
- Garmin GPSMAP 8616xsv / 8622xsv (4.299 / 6.799 EUR)
- Simrad NSO Evo3S 16" / 19" / 24" (4.999 / 7.499 / 10.999 EUR)
- Furuno TZT2BB + Monitor (Blackbox-Konzept, ab 5.499 EUR)

**Einsatzgebiet:**
- Motoryachten > 14 m, Segelyachten > 15 m
- Superyachten (Brücke, Flybridge)
- Mehrdisplay-Installationen (2–6 Bildschirme vernetzt)
- Berufsschifffahrt (Fischerei, Arbeitsboote)
- Regatta-Yachten mit hohem Informationsbedarf

**Besonderheiten:**
- Multi-Display-Synchronisation über Ethernet
- Video-Eingänge für IP-Kameras, Unterwasserkameras, Thermal-Kameras
- Integration externer PCs (Expedition, Adrena, MaxSea)
- Dedizierte Prozessoren für Radar, Echolot, Karte parallel
- Glasbrücken-Konzept: MFDs ersetzen analoge Instrumente vollständig

### 3.4 Blackbox-Systeme (Prozessor + separater Monitor)

**Konzept:**
Statt eines integrierten MFDs wird ein lüfterloser Prozessor (Blackbox) unter dem Navigationsstand eingebaut und mit einem oder mehreren externen Monitoren verbunden. Dies ermöglicht flexible Displaygrößen und -positionen.

**Typische Vertreter:**
- Furuno TZT2BB / TZT3BB: Blackbox mit HDMI-Ausgang, bis 2 Monitore, ab 3.499 EUR
- Simrad NSO Evo3S: Prozessor mit Display-Optionen von 16" bis 24"
- Raymarine Axiom 2 Pro als MFD nutzbar, alternativ Axiom XL als Blackbox-Variante

**Vorteile:**
- Beliebige Monitorgröße (bis 32" oder größer)
- Austausch des Monitors unabhängig vom Prozessor
- Bessere Wärmeableitung (Prozessor an belüftetem Ort)
- Flexible Positionierung (Monitor am Steuerstand, Prozessor im Elektronikschrank)

**Nachteile:**
- Höhere Gesamtkosten (Prozessor + Monitor + Kabel)
- Komplexere Installation (mehr Kabel, mehr Montageorte)
- Monitor-Kompatibilitätsprobleme (Auflösung, HDMI-Timing)
- Zusätzlicher Fehlerpunkt (Kabelverbindung Prozessor↔Monitor)

### 3.5 Segelsoftware-Integration

#### 3.5.1 B&G SailSteer und Segelfunktionen

B&G (Navico/Brunswick) ist der einzige MFD-Hersteller mit nativem Segelfokus. Die SailSteer-Darstellung fasst alle segelrelevanten Daten in einem intuitiven Polardiagramm zusammen:

**SailSteer-Funktionen:**
- Windrose mit TWA (True Wind Angle) und AWA (Apparent Wind Angle)
- Layline-Darstellung für optimalen Kurs zum Wendepunkt
- Segelvorschlag (welches Segel bei welchem Wind)
- Strömungsvektor-Overlay auf der Karte
- Halsen-/Wende-Timer
- Performance-Prozent (VMG vs. Polardaten)
- Startlinien-Funktion für Regatta

**Polardaten-Integration:**
- Import von Polardaten (VPP — Velocity Prediction Program)
- Vergleich Ist-Geschwindigkeit vs. Soll-Geschwindigkeit
- Performance-Prozent als Kernmetrik
- ORC/IRC-Polardaten können importiert werden

#### 3.5.2 Expedition / Adrena / qtVlm — PC-basierte Segelsoftware

Für ambitionierte Regattasegler reichen MFD-eigene Segelfunktionen oft nicht aus. Professionelle PC-basierte Software bietet mehr:

| Software | Plattform | Preis | Stärken |
|----------|----------|-------|---------|
| Expedition | Windows | ab 1.200 EUR | Regatta-Standard, vollständiges Routing, Wetter-Overlay |
| Adrena | Windows | ab 800 EUR | Performance-Analyse, GRIB-Integration |
| qtVlm | Windows/Mac/Linux | Kostenlos | Open-Source, Wetter-Routing, Polardaten |
| SailGrib | Android/iOS | ab 30 EUR | Mobiles Wetter-Routing, Polardaten |

**Integration in MFD-System:**
- Expedition/Adrena laufen auf separatem PC am Navigationstisch
- Datenfluss: NMEA 2000/0183 → PC → Routing-Berechnung → Anzeige auf MFD oder separatem Monitor
- Einige MFDs (Simrad NSO, Furuno TZT2BB) erlauben die Anzeige von externen Video-Quellen (HDMI-In)

### 3.6 Spezial-MFDs für besondere Anwendungen

#### 3.6.1 Flybridge-Installation (Motoryacht)

**Anforderungen:**
- Maximale Sonnenlichtablesbarkeit (Freiluft-Helm)
- Wasserdichtheit IP67 oder besser
- Großes Display (mindestens 12", besser 16"+)
- Spiegelung mit Unterdeck-MFD (gleiche Daten, unabhängige Bedienung)
- Sonnenschutz/Cover für Langzeitschutz

**Typische Konfiguration:**
- Flybridge: 16" MFD (Hauptdisplay) + Instrumenten-Displays
- Steuerstand Unterdeck: 12" MFD (Backup) + Radar-/Echolot-Anzeige
- Salon: 9" MFD (Übersicht, Entertainment-Integration)
- Netzwerk: Ethernet-Switch verbindet alle MFDs, Radar, Echolot

#### 3.6.2 Cockpit-Installation (Segelyacht)

**Anforderungen:**
- Ablesbarkeit aus verschiedenen Blickwinkeln (stehend, sitzend, liegend bei Lage)
- Bedienbarkeit mit Segelhandschuhen
- Spritzwasserfest (IP67)
- Blendfreie Positionierung (nicht direkt in Sonnenlichtreflektion)
- Integration mit Autopilot, Wind, Logge

**Typische Konfiguration:**
- Cockpit-Säule/Pod: 9" oder 12" MFD als Haupt-Navigationsdisplay
- Instrumenten-Pod: Dedizierte Wind-/Geschwindigkeits-/Tiefendisplays
- Navigationstisch unter Deck: 12" MFD oder Laptop mit Navigation
- Netzwerk: NMEA 2000 Backbone + Ethernet für Radar/MFD-Sync

---

## 4. Produktlinien und Spezifikationen

### 4.1 Raymarine — Axiom-Familie

#### 4.1.1 Unternehmenshintergrund

Raymarine, gegründet 1923 als Raytheon Marine, ist seit 2010 Teil der FLIR Systems (jetzt Teledyne FLIR). Hauptsitz: Fareham, Hampshire, UK. Raymarine ist einer der führenden Hersteller mariner Elektronik mit besonderer Stärke im europäischen Markt und bei Charterflotten.

#### 4.1.2 Axiom 2 Pro — Mid-Range MFD

**Verfügbare Größen und Preise (UVP 2025/2026):**

| Modell | Display | Auflösung | Preis (nur MFD) | Preis (mit Echolot) |
|--------|---------|-----------|----------------|-------------------|
| Axiom 2 Pro 7 | 7" IPS | 1024 × 600 | 999 EUR | 1.299 EUR |
| Axiom 2 Pro 9 | 9" IPS | 1280 × 720 | 1.499 EUR | 1.899 EUR |
| Axiom 2 Pro 12 | 12" IPS | 1280 × 800 | 1.999 EUR | 2.499 EUR |

**Technische Spezifikationen (Axiom 2 Pro 9):**

| Parameter | Wert |
|-----------|------|
| Display | 9" IPS, Optically Bonded |
| Auflösung | 1280 × 720 px |
| Helligkeit | 1.200 nits (max. 1.500 nits) |
| Touchscreen | Kapazitiv, Multi-Touch |
| Prozessor | Quad-Core ARM Cortex-A72, 1.8 GHz |
| RAM | 4 GB |
| Speicher | 32 GB intern + microSD-Slot |
| Betriebssystem | LightHouse 4 |
| GPS | Intern, 10 Hz, GPS + GLONASS + Galileo |
| Echolot (RV-Variante) | RealVision 3D CHIRP (optional) |
| NMEA 2000 | 1× Micro-C Anschluss |
| NMEA 0183 | 2× (RS-422) |
| Ethernet | 1× RayNet (100 Mbit/s) |
| Wi-Fi | 802.11 b/g/n/ac, Dual-Band |
| Bluetooth | 5.0 LE |
| Video-In | — (nur über Netzwerk-Kamera) |
| Stromversorgung | 12 V DC (10–32 V) |
| Leistungsaufnahme | 14 W (typisch), 22 W (max.) |
| Abmessungen (B×H×T) | 275 × 168 × 72 mm |
| Gewicht | 1,4 kg |
| Schutzart | IP67 (Front), IP54 (Rückseite) |
| Betriebstemperatur | -15°C bis +55°C |

**LightHouse 4 — Betriebssystem-Features:**
- ClearCruise AR (Augmented Reality): Kamera-basierte Objekterkennung mit Navigations-Overlay
- Axiom+ LightHouse Charts (Navionics-basiert, vorinstalliert)
- Raymarine Element-Echolot-Netzwerkintegration
- Splitscreen bis 4 Fenster
- Autopilot-Vollsteuerung (Evolution-Serie)
- Radar-Overlay auf Karte (Quantum 2)
- OTA-Updates über Wi-Fi

#### 4.1.3 Axiom 2 XL — High-End MFD

**Verfügbare Größen und Preise (UVP 2025/2026):**

| Modell | Display | Auflösung | Preis |
|--------|---------|-----------|-------|
| Axiom 2 XL 16 | 15,6" IPS | 1920 × 1080 | 3.999 EUR |
| Axiom 2 XL 19 | 18,5" IPS | 1920 × 1080 | 5.999 EUR |
| Axiom 2 XL 22 | 21,5" IPS | 1920 × 1080 | 8.499 EUR |

**Technische Spezifikationen (Axiom 2 XL 16):**

| Parameter | Wert |
|-----------|------|
| Display | 15,6" IPS, Optically Bonded |
| Auflösung | 1920 × 1080 px (Full HD) |
| Helligkeit | 1.500 nits (max. 2.000 nits) |
| Touchscreen | Kapazitiv, Multi-Touch, 10-Punkt |
| Prozessor | Quad-Core ARM Cortex-A73, 2.2 GHz |
| RAM | 8 GB |
| Speicher | 64 GB intern + microSD-Slot |
| Betriebssystem | LightHouse 4 |
| GPS | Intern, 10 Hz, GPS + GLONASS + Galileo + BeiDou |
| Echolot | Kein internes Modul (extern über Netzwerk) |
| NMEA 2000 | 2× Micro-C Anschluss |
| NMEA 0183 | 2× (RS-422) |
| Ethernet | 2× RayNet (100 Mbit/s) |
| Wi-Fi | 802.11 ac, Dual-Band |
| Bluetooth | 5.0 LE |
| Video-In | 1× HDMI (Eingang für externe Quelle) |
| Stromversorgung | 12 V DC (10–32 V) |
| Leistungsaufnahme | 24 W (typisch), 38 W (max.) |
| Abmessungen (B×H×T) | 420 × 270 × 85 mm |
| Gewicht | 3,8 kg |
| Schutzart | IP67 (Front), IP56 (Rückseite) |
| Betriebstemperatur | -15°C bis +55°C |

**Besonderheiten der XL-Serie:**
- ClearCruise AR mit erweiterter KI-Objekterkennung (unterscheidet Bojen, Schiffe, Felsen, Badende)
- HDMI-Eingang für Integration externer Quellen (PC, Kamera, Thermal)
- Dual-Ethernet für gleichzeitige Radar- und MFD-Netzwerk-Verbindung
- Glasbrücken-fähig: Bis zu 6 Axiom XL können synchron arbeiten
- Marine-Grade Aluminium-Gehäuse mit passiver Kühlung

### 4.2 Garmin — GPSMAP-Familie

#### 4.2.1 Unternehmenshintergrund

Garmin Ltd., gegründet 1989 in Lenexa, Kansas, USA (jetzt Olathe, KS). Weltweit größter Hersteller von GPS-Navigationsgeräten. Marine-Sparte profitiert von Garmin-Kompetenz in GPS-Technologie, Kartografie und Consumer-Elektronik. Übernahme von Navionics (2017) und Fusion Audio stärkt das Marine-Ökosystem.

#### 4.2.2 GPSMAP 84xx / 86xx — Mittelklasse und Premium

**GPSMAP 84xx Serie (Mittelklasse mit Tasten):**

| Modell | Display | Auflösung | Bedienung | Preis |
|--------|---------|-----------|-----------|-------|
| GPSMAP 843xsv | 7" IPS | 1024 × 600 | Tasten + Touch | 1.199 EUR |
| GPSMAP 843 | 7" IPS | 1024 × 600 | Tasten + Touch | 899 EUR |

**GPSMAP 86xx Serie (Premium Touch):**

| Modell | Display | Auflösung | Helligkeit | Preis |
|--------|---------|-----------|-----------|-------|
| GPSMAP 8610xsv | 10" IPS | 1280 × 800 | 1.800 nits | 2.699 EUR |
| GPSMAP 8612xsv | 12" IPS | 1280 × 800 | 1.800 nits | 3.299 EUR |
| GPSMAP 8616xsv | 15,4" IPS | 1920 × 1080 | 1.800 nits | 4.299 EUR |
| GPSMAP 8622xsv | 22" IPS | 1920 × 1200 | 1.500 nits | 6.799 EUR |

**Technische Spezifikationen (GPSMAP 8616xsv):**

| Parameter | Wert |
|-----------|------|
| Display | 15,4" IPS, Optically Bonded |
| Auflösung | 1920 × 1080 px (Full HD) |
| Helligkeit | 1.800 nits |
| Touchscreen | Kapazitiv, Multi-Touch |
| Prozessor | Quad-Core, 2.0 GHz (Garmin-eigen) |
| RAM | 4 GB |
| Speicher | 32 GB intern + 2× microSD-Slot |
| Betriebssystem | Garmin Marine OS |
| GPS | Intern, 10 Hz, GPS + GLONASS + Galileo |
| Echolot | Internes CHIRP-Modul (1 kW), ClearVü, SideVü |
| NMEA 2000 | 1× (Garmin-Connector, Adapter auf Micro-C) |
| NMEA 0183 | 2× (In/Out) |
| Ethernet | 2× Garmin Marine Network (100 Mbit/s) |
| Wi-Fi | 802.11 b/g/n |
| Bluetooth | 4.2 |
| Video-In | HDMI (bei 22"-Modell) |
| Stromversorgung | 12 V DC (10–32 V) |
| Leistungsaufnahme | 28 W (typisch) |
| Abmessungen (B×H×T) | 413 × 260 × 76 mm |
| Gewicht | 3,1 kg |
| Schutzart | IPX7 (Front und Gesamt) |
| Betriebstemperatur | -15°C bis +50°C |

**Garmin-Ökosystem — Besonderheiten:**
- ActiveCaptain Community: Hafenbewertungen, Gefahrenmeldungen, Routenvorschläge
- BlueChart g4: Auto Guidance berechnet kartenbasierte Routen unter Berücksichtigung von Tiefe
- Garmin Quickdraw Contours: Automatische Erstellung eigener Tiefenkarten
- OneHelm: Integration von Drittanbieter-Systemen (Fusion Audio, Mercury VesselView)
- SmartMode: Kontextabhängige Startseite je nach Aktivität (Cruising, Fishing, Docking)

#### 4.2.3 GPSMAP 1243xsv — Neueste Generation (2024/2025)

| Parameter | Wert |
|-----------|------|
| Display | 12" IPS, Optically Bonded |
| Auflösung | 1280 × 800 px |
| Helligkeit | 1.200 nits (max. 1.500 nits) |
| Touchscreen | Kapazitiv, Multi-Touch |
| GPS | Intern, GPS + GLONASS + Galileo + BeiDou |
| Echolot | Integriertes CHIRP 600W + ClearVü + SideVü |
| NMEA 2000 | 1× |
| Ethernet | 1× Garmin Marine Network |
| Wi-Fi | 802.11 b/g/n/ac |
| Kartenmaterial | BlueChart g4 + Navionics+ vorinstalliert |
| Preis | 2.299 EUR |

### 4.3 Simrad — NSX und NSO-Familie

#### 4.3.1 Unternehmenshintergrund

Simrad (Simonsen Radio) wurde 1947 in Horten, Norwegen, gegründet und ist traditionell stark in der Berufsschifffahrt. Seit 2007 Teil der Navico-Gruppe (zusammen mit B&G und Lowrance), die wiederum seit 2022 zu Brunswick Corporation gehört. Simrad ist die Premium-Marke der Navico-Gruppe für Motorboote und Sportfischer.

#### 4.3.2 NSX — Neue Generation (2023+)

**Verfügbare Größen und Preise:**

| Modell | Display | Auflösung | Helligkeit | Preis |
|--------|---------|-----------|-----------|-------|
| NSX 3007 | 7" IPS | 1024 × 600 | 1.500 nits | 999 EUR |
| NSX 3009 | 9" IPS | 1280 × 720 | 2.000 nits | 1.699 EUR |
| NSX 3012 | 12" IPS | 1280 × 800 | 2.000 nits | 2.399 EUR |

**Technische Spezifikationen (NSX 3012):**

| Parameter | Wert |
|-----------|------|
| Display | 12" IPS, SolarMAX IPS, Optically Bonded |
| Auflösung | 1280 × 800 px |
| Helligkeit | 2.000 nits (max. 2.500 nits) |
| Touchscreen | Kapazitiv, Multi-Touch |
| Prozessor | Quad-Core ARM, 2.0 GHz |
| RAM | 4 GB |
| Speicher | 32 GB intern + microSD-Slot |
| Betriebssystem | Simrad OS (Linux-basiert) |
| GPS | Intern, 10 Hz, GPS + GLONASS + Galileo |
| Echolot | Optional: Active Imaging 3-in-1 |
| NMEA 2000 | 1× Micro-C |
| NMEA 0183 | 2× (RS-422) |
| Ethernet | 1× (100 Mbit/s) |
| Wi-Fi | 802.11 ac, Dual-Band |
| Bluetooth | 5.0 LE |
| Kartenmaterial | C-MAP Discover X vorinstalliert |
| Stromversorgung | 12 V DC (10–32 V) |
| Leistungsaufnahme | 16 W (typisch), 28 W (max.) |
| Abmessungen (B×H×T) | 314 × 212 × 65 mm |
| Gewicht | 2,0 kg |
| Schutzart | IPX7 |
| Betriebstemperatur | -15°C bis +55°C |

**NSX-Besonderheiten:**
- SolarMAX IPS: Branchenweit höchste Helligkeit (2.000–2.500 nits)
- C-MAP Discover X: Neueste Kartengeneration mit hochauflösender Bathymetrie
- Active Imaging: Kombinierter Geber (CHIRP + SideScan + DownScan) in einem Transducer
- HALO-Radar-Integration über Ethernet
- Simrad Autopilot (NAC-Serie) volle Steuerung
- ForwardScan-fähig

#### 4.3.3 GO XSE — Einstiegsserie

| Modell | Display | Auflösung | Preis |
|--------|---------|-----------|-------|
| GO XSE 7 | 7" IPS | 800 × 480 | 649 EUR |
| GO XSE 9 | 9" IPS | 1024 × 600 | 999 EUR |
| GO XSE 12 | 12" IPS | 1280 × 800 | 1.499 EUR |

#### 4.3.4 NSO Evo3S — Profi-/Glasbrücken-Serie

| Modell | Display | Auflösung | Preis |
|--------|---------|-----------|-------|
| NSO Evo3S 16 | 15,6" IPS | 1920 × 1080 | 4.999 EUR |
| NSO Evo3S 19 | 18,5" IPS | 1920 × 1080 | 7.499 EUR |
| NSO Evo3S 24 | 23,5" IPS | 1920 × 1200 | 10.999 EUR |

**NSO Evo3S Besonderheiten:**
- Modulare Glasbrücke: bis zu 12 Displays synchron
- Dual-Ethernet + NMEA 2000
- C-MAP MAX-N+ und Navionics Platinum+
- Mercury VesselView, Yamaha Helm Master Integration
- Video-4-Input-Modul für IP-Kameras

### 4.4 B&G — Zeus und Vulcan-Familie

#### 4.4.1 Unternehmenshintergrund

B&G (Brookes & Gatehouse), gegründet 1956 in Lymington, Hampshire, UK. Traditioneller Hersteller von Segelinstrumenten (Windmesser, Loggen, Tiefenmesser). Seit 2009 Teil der Navico-Gruppe. B&G ist die einzige MFD-Marke mit dediziertem Segelfokus — alle Produkte werden von Seglern für Segler entwickelt.

#### 4.4.2 Zeus S — Premium-Segel-MFD (2025)

**Verfügbare Größen und Preise:**

| Modell | Display | Auflösung | Helligkeit | Preis |
|--------|---------|-----------|-----------|-------|
| Zeus S 7 | 7" IPS | 1024 × 600 | 1.500 nits | 1.399 EUR |
| Zeus S 9 | 9" IPS | 1280 × 720 | 1.500 nits | 2.099 EUR |
| Zeus S 12 | 12" IPS | 1280 × 800 | 1.500 nits | 2.799 EUR |
| Zeus S 16 | 15,6" IPS | 1920 × 1080 | 1.500 nits | 4.499 EUR |

**Technische Spezifikationen (Zeus S 9):**

| Parameter | Wert |
|-----------|------|
| Display | 9" IPS, Optically Bonded |
| Auflösung | 1280 × 720 px |
| Helligkeit | 1.500 nits (max. 2.000 nits) |
| Touchscreen | Kapazitiv, Multi-Touch |
| Prozessor | Quad-Core ARM, 2.0 GHz + dedizierter Sailing-Coprozessor |
| RAM | 4 GB |
| Speicher | 32 GB intern + microSD-Slot |
| Betriebssystem | B&G OS (Navico-Basis) |
| GPS | Intern, 10 Hz, GPS + GLONASS + Galileo |
| Segelfunktionen | SailSteer, Laylines, Polardaten, Startlinie, Halsen-Timer |
| Echolot | Optional: ForwardScan + Active Imaging |
| NMEA 2000 | 1× Micro-C |
| NMEA 0183 | 2× (RS-422) |
| Ethernet | 1× (100 Mbit/s) |
| Wi-Fi | 802.11 ac |
| Bluetooth | 5.0 LE |
| Kartenmaterial | C-MAP Discover X |
| Stromversorgung | 12 V DC (10–32 V) |
| Leistungsaufnahme | 16 W (typisch), 26 W (max.) |
| Schutzart | IPX7 |

**Zeus S Segelfunktionen im Detail:**

| Funktion | Beschreibung |
|----------|-------------|
| SailSteer | Polar-basierte Darstellung mit TWA, Laylines, VMG, Performance% |
| Layline-Berechnung | Automatische Berechnung der optimalen Wende-/Halsen-Punkte auf Basis von Wind und Strömung |
| Polardaten-Import | VPP-Daten (ORC, IRC) importierbar, Vergleich Ist vs. Soll |
| Startlinien-Tool | Entfernung/Winkel zur Startlinie, Timer, favorisiertes Ende |
| Halsen-/Wende-Timer | Taktische Zeitnahme für Manöver |
| ForwardScan | Unterwasser-Vorausschau für Segler in flachen Gewässern |
| Strömungsvektor | Stromrichtung/-stärke auf Karte (bei externem Geber) |
| Wind-Grafik | Historische Windentwicklung (TWS, TWD über Zeit) |
| Race-Panel | Kompaktdarstellung aller Regatta-relevanten Daten |

#### 4.4.3 Vulcan — Einstieg-Segel-MFD

| Modell | Display | Auflösung | Preis |
|--------|---------|-----------|-------|
| Vulcan 7R | 7" IPS | 800 × 480 | 649 EUR |
| Vulcan 9R | 9" IPS | 1024 × 600 | 999 EUR |
| Vulcan 12R | 12" IPS | 1280 × 800 | 1.499 EUR |

**Vulcan vs. Zeus S — Kernunterschiede:**
- Vulcan: kein Sailing-Coprozessor, vereinfachte SailSteer-Version
- Vulcan: geringere Helligkeit (1.000 nits vs. 1.500 nits)
- Vulcan: kein Dual-Band Wi-Fi
- Zeus S: erweiterte Polardaten-Analyse, detailliertere Laylines
- Zeus S: dedizierter Sailing-Prozessor für Echtzeit-Berechnungen

### 4.5 Furuno — TZT-Familie (TimeZero Technology)

#### 4.5.1 Unternehmenshintergrund

Furuno Electric Co., Ltd., gegründet 1948 in Nishinomiya, Japan. Weltmarktführer in der Berufsschifffahrt (Radar, Echolot, ECDIS). Furuno bringt diese professionelle Expertise in die Yachtelektronik ein und ist bekannt für höchste Zuverlässigkeit und Verarbeitungsqualität.

#### 4.5.2 TZT3 — Aktuelle MFD-Generation (2024+)

**Verfügbare Größen und Preise:**

| Modell | Display | Auflösung | Preis |
|--------|---------|-----------|-------|
| TZT3 9F | 9" IPS | 1280 × 720 | 2.299 EUR |
| TZT3 12F | 12" IPS | 1280 × 800 | 2.999 EUR |
| TZT3 16F | 15,6" IPS | 1920 × 1080 | 4.799 EUR |

**Technische Spezifikationen (TZT3 12F):**

| Parameter | Wert |
|-----------|------|
| Display | 12,1" IPS, Optically Bonded |
| Auflösung | 1280 × 800 px |
| Helligkeit | 1.000 nits (max. 1.200 nits) |
| Touchscreen | Kapazitiv, Multi-Touch |
| Prozessor | Quad-Core Intel Atom, 1.6 GHz |
| RAM | 4 GB |
| Speicher | 32 GB SSD + microSD-Slot |
| Betriebssystem | TimeZero V6 (Windows Embedded) |
| GPS | Intern, 10 Hz, GPS + GLONASS + Galileo |
| Echolot | Optional: DFF-3D Multibeam oder DFF1-UHD |
| NMEA 2000 | 1× Micro-C |
| NMEA 0183 | 4× (RS-422, 2 In / 2 Out) |
| Ethernet | 2× (100 Mbit/s / 1 Gbit/s) |
| Wi-Fi | 802.11 ac |
| Bluetooth | 5.0 LE |
| Kartenmaterial | TZ Maps (TimeZero) + C-MAP-kompatibel |
| USB | 2× USB 2.0 (für Maus, Tastatur, Updates) |
| Video-In | 1× DVI (bei 16"-Modell) |
| Stromversorgung | 12/24 V DC (10–35 V) |
| Leistungsaufnahme | 22 W (typisch), 35 W (max.) |
| Abmessungen (B×H×T) | 328 × 226 × 118 mm |
| Gewicht | 3,5 kg |
| Schutzart | IP56 (Front), IP22 (Rückseite) |
| Betriebstemperatur | -15°C bis +55°C |

**TZT3 / TimeZero-Besonderheiten:**
- TimeZero V6: PC-basierte Software-Plattform, extrem flexibel und leistungsfähig
- 3D-Kartendarstellung: Bathymetrie als 3D-Gelände, Satellitenfoto-Overlay
- Cloud-Routing: Online-optimierte Routenberechnung mit Wetterintegration
- DFF-3D Multibeam: Einzigartiges 3D-Echolot für Unterwasser-Darstellung
- RezBoost: KI-gestützte Echolot-Auflösungsverbesserung
- USB-Anschlüsse für Maus und Tastatur (Windows-basiert)
- Automatische Kartenaktualisierung über Cloud

#### 4.5.3 TZT2BB — Blackbox-System

| Parameter | Wert |
|-----------|------|
| Typ | Blackbox-Prozessor (kein eigenes Display) |
| Ausgang | HDMI (1920 × 1080 oder 1920 × 1200) |
| Monitore | Bis zu 2 gleichzeitig (über HDMI-Splitter oder 2. Ausgang) |
| Prozessor | Quad-Core Intel, 2.0 GHz |
| RAM | 8 GB |
| Speicher | 64 GB SSD |
| Ethernet | 3× |
| NMEA 2000 | 2× |
| USB | 4× |
| Preis | 3.499 EUR (ohne Monitor) |

**Einsatz des TZT2BB:**
- Großyachten mit Custom-Monitoren (24", 32" oder größer)
- Integration in bestehende Glasbrücken
- Kombination mit Marine-Grade-Monitoren von NEC, Samsung, Hatteland
- Ideal für Retrofits, bei denen nur der Prozessor aktualisiert wird

### 4.6 Preisvergleich nach Displaygröße

#### 4.6.1 7"-Klasse (Einstieg)

| Modell | Preis | Echolot | Besonderheit |
|--------|-------|---------|-------------|
| Simrad Cruise 7 | 549 EUR | Optional | Basisfunktion |
| Raymarine Element 7 HV | 649 EUR | CHIRP + HyperVision | Guter Einstieg |
| B&G Vulcan 7R | 649 EUR | Optional | Segelfunktionen |
| Garmin echoMAP UHD2 72sv | 799 EUR | Integriert | Starkes Echolot |
| Raymarine Axiom 2 Pro 7 | 999 EUR | Optional | LightHouse 4 |
| Simrad NSX 3007 | 999 EUR | Optional | SolarMAX-Display |
| B&G Zeus S 7 | 1.399 EUR | Optional | Sailing-Prozessor |

#### 4.6.2 9"-Klasse (Standard)

| Modell | Preis | Echolot | Besonderheit |
|--------|-------|---------|-------------|
| Simrad GO XSE 9 | 999 EUR | Optional | Basisnetzwerk |
| B&G Vulcan 9R | 999 EUR | Optional | Basisfunktion Segeln |
| Raymarine Axiom 2 Pro 9 | 1.499 EUR | Optional | ClearCruise AR |
| Garmin GPSMAP 923xsv | 1.599 EUR | Integriert | ActiveCaptain |
| Simrad NSX 3009 | 1.699 EUR | Optional | 2.000 nits Display |
| B&G Zeus S 9 | 2.099 EUR | Optional | Vollständiges Segeltool |
| Furuno TZT3 9F | 2.299 EUR | Optional | TimeZero V6 |

#### 4.6.3 12"-Klasse (Komfort)

| Modell | Preis | Echolot | Besonderheit |
|--------|-------|---------|-------------|
| Simrad GO XSE 12 | 1.499 EUR | Optional | Basisnetzwerk |
| B&G Vulcan 12R | 1.499 EUR | Optional | Basisfunktion Segeln |
| Raymarine Axiom 2 Pro 12 | 1.999 EUR | Optional | ClearCruise AR |
| Garmin GPSMAP 1223xsv | 2.299 EUR | Integriert | BlueChart g4 |
| Garmin GPSMAP 1243xsv | 2.299 EUR | Integriert | Neueste Gen. |
| Simrad NSX 3012 | 2.399 EUR | Optional | SolarMAX IPS |
| B&G Zeus S 12 | 2.799 EUR | Optional | Segelfunktionen |
| Furuno TZT3 12F | 2.999 EUR | Optional | TimeZero V6 |

#### 4.6.4 16"+-Klasse (Premium)

| Modell | Preis | Besonderheit |
|--------|-------|-------------|
| Raymarine Axiom 2 XL 16 | 3.999 EUR | ClearCruise AR, HDMI-In |
| Garmin GPSMAP 8616xsv | 4.299 EUR | 1.800 nits, Echolot integriert |
| B&G Zeus S 16 | 4.499 EUR | Sailing-Prozessor, SailSteer |
| Furuno TZT3 16F | 4.799 EUR | TimeZero, 3D-Karten |
| Simrad NSO Evo3S 16 | 4.999 EUR | Glasbrücke |
| Raymarine Axiom 2 XL 19 | 5.999 EUR | Glasbrücke |
| Garmin GPSMAP 8622xsv | 6.799 EUR | 22", Full HD+ |
| Simrad NSO Evo3S 19 | 7.499 EUR | Glasbrücke |
| Raymarine Axiom 2 XL 22 | 8.499 EUR | Glasbrücke |
| Simrad NSO Evo3S 24 | 10.999 EUR | 24", Glasbrücke |

---

## 5. Hersteller-Datenbank

### 5.1 Raymarine (Teledyne FLIR)

| Attribut | Details |
|----------|---------|
| Vollständiger Name | Raymarine (Teledyne FLIR Marine Division) |
| Gründung | 1923 (als Raytheon Marine) |
| Hauptsitz | Fareham, Hampshire, Vereinigtes Königreich |
| Muttergesellschaft | Teledyne Technologies (NYSE: TDY) |
| Kernprodukte | MFDs, Radar, Echolot, Autopilot, Kameras, Instrumente |
| MFD-Produktlinien | Axiom 2 Pro, Axiom 2 XL, Element |
| Betriebssystem | LightHouse 4 |
| Kartenformat | LightHouse Charts (Navionics-basiert), C-MAP, Navionics |
| Netzwerkprotokoll | SeaTalkng (NMEA 2000), RayNet (Ethernet) |
| Service-Netzwerk | Global, ca. 3.000 Händler, starke Präsenz in Europa und Nordamerika |
| Garantie | 2 Jahre Standard, 3 Jahre bei Online-Registrierung |
| Website | www.raymarine.com |
| Stärken | Augmented Reality (ClearCruise), integriertes Ökosystem, Charterflotten-Marktführer |
| Schwächen | Helligkeitswerte unter Simrad-Niveau, proprietärer RayNet-Stecker |

### 5.2 Garmin

| Attribut | Details |
|----------|---------|
| Vollständiger Name | Garmin Ltd. |
| Gründung | 1989 |
| Hauptsitz | Olathe, Kansas, USA |
| Börse | NYSE / NASDAQ: GRMN |
| Kernprodukte | GPS-Navigation (Marine, Aviation, Automotive, Outdoor, Fitness) |
| MFD-Produktlinien | GPSMAP 84xx, GPSMAP 86xx, GPSMAP 12xx, echoMAP UHD2 |
| Betriebssystem | Garmin Marine OS (proprietär) |
| Kartenformat | BlueChart g4, Navionics (eigene Tochter), LakeVü |
| Netzwerkprotokoll | Garmin Marine Network (proprietäres Ethernet), NMEA 2000 |
| Service-Netzwerk | Global, ca. 5.000+ Händler, stärkstes Netzwerk weltweit |
| Garantie | 2 Jahre |
| Website | www.garmin.com |
| Stärken | Kartenmaterial (BlueChart + Navionics), ActiveCaptain Community, Preis-Leistung, Ökosystem |
| Schwächen | Proprietäres Netzwerk (nur Garmin-Geräte), eingeschränkte Segelfunktionen |

### 5.3 Simrad (Navico / Brunswick)

| Attribut | Details |
|----------|---------|
| Vollständiger Name | Simrad Yachting (Navico Group) |
| Gründung | 1947 (als Simonsen Radio) |
| Hauptsitz | Egersund, Norwegen |
| Muttergesellschaft | Brunswick Corporation (NYSE: BC), via Navico Group |
| Kernprodukte | MFDs, Radar, Echolot, Autopilot |
| MFD-Produktlinien | NSX, NSO Evo3S, GO XSE, Cruise |
| Betriebssystem | Simrad OS |
| Kartenformat | C-MAP (eigene Schwestergesellschaft) |
| Netzwerkprotokoll | SimNet (NMEA 2000), Ethernet |
| Service-Netzwerk | Global, ca. 2.500 Händler |
| Garantie | 2 Jahre |
| Website | www.simrad-yachting.com |
| Stärken | Displayhelligkeit (SolarMAX), Radar-Kompetenz (HALO), Berufsschifffahrt-Heritage |
| Schwächen | Komplexes Produktportfolio (Überschneidung mit Lowrance), Software-Updates manchmal verzögert |

### 5.4 B&G (Navico / Brunswick)

| Attribut | Details |
|----------|---------|
| Vollständiger Name | B&G (Brookes & Gatehouse) |
| Gründung | 1956 |
| Hauptsitz | Lymington, Hampshire, Vereinigtes Königreich |
| Muttergesellschaft | Brunswick Corporation (NYSE: BC), via Navico Group |
| Kernprodukte | Segel-MFDs, Segel-Instrumente, Autopilot, Wind-/Logge-Systeme |
| MFD-Produktlinien | Zeus S, Vulcan |
| Betriebssystem | B&G OS (Navico-Basis, segel-optimiert) |
| Kartenformat | C-MAP (Schwestergesellschaft) |
| Netzwerkprotokoll | SimNet (NMEA 2000), Ethernet |
| Service-Netzwerk | Global, ca. 1.500 Händler, Schwerpunkt Segelzentren |
| Garantie | 2 Jahre |
| Website | www.bandg.com |
| Stärken | Einziger MFD-Hersteller mit echtem Segelfokus, SailSteer, Laylines, Polardaten, Regattapartner |
| Schwächen | Kleineres Händlernetz als Garmin/Raymarine, höhere Preise als vergleichbare Simrad-Modelle |

### 5.5 Furuno

| Attribut | Details |
|----------|---------|
| Vollständiger Name | Furuno Electric Co., Ltd. |
| Gründung | 1948 |
| Hauptsitz | Nishinomiya, Hyogo, Japan |
| Börse | TSE: 6814 |
| Kernprodukte | Marine-Radar, Echolot, ECDIS, Sat-Comm, Autopilot, MFDs |
| MFD-Produktlinien | TZT3 (All-in-One), TZT2BB (Blackbox), NavNet TZtouch |
| Betriebssystem | TimeZero V6 (Windows Embedded) |
| Kartenformat | TZ Maps (TimeZero), C-MAP-kompatibel |
| Netzwerkprotokoll | Furuno CAN Bus, Ethernet (NavNet) |
| Service-Netzwerk | Global, ca. 2.000 Händler, besonders stark in Asien und Berufsschifffahrt |
| Garantie | 2 Jahre (3 Jahre in einigen Märkten) |
| Website | www.furuno.com |
| Stärken | Berufsschifffahrt-Zuverlässigkeit, TimeZero-Software, 3D-Echolot (DFF-3D), Verarbeitungsqualität |
| Schwächen | Höhere Preise, geringere Helligkeit als Wettbewerb, IP-Schutzart niedriger als Mitbewerber |

### 5.6 Humminbird (Johnson Outdoors)

| Attribut | Details |
|----------|---------|
| Vollständiger Name | Humminbird (Johnson Outdoors Marine Electronics) |
| Gründung | 1971 |
| Hauptsitz | Eufaula, Alabama, USA |
| Muttergesellschaft | Johnson Outdoors (NASDAQ: JOUT) |
| Kernprodukte | Fischfinder, Kartenplotter, Trolling-Motoren (Minn Kota) |
| MFD-Produktlinien | APEX, SOLIX, HELIX |
| Kartenformat | Navionics, LakeMaster, AutoChart |
| Netzwerkprotokoll | Ethernet, NMEA 2000 |
| Stärken | MEGA Imaging (hochauflösendes SideScan), Süßwasser-Kartografie, Preis-Leistung |
| Schwächen | Wenig Salzwasser-/Offshore-Fokus, kleines internationales Händlernetz |
| Website | www.humminbird.com |

### 5.7 Xinuo / Matsutec / Onwa — Asiatische Hersteller

| Attribut | Details |
|----------|---------|
| Hersteller | Xinuo (Shenzhen), Matsutec (Guangzhou), Onwa (Shenzhen) |
| Herkunft | China |
| Preissegment | 200–800 EUR (deutlich unter westlichen Herstellern) |
| Kartenformat | C-MAP-kompatibel (Xinuo), eigenes Format (Onwa) |
| Stärken | Extrem niedrige Preise, Basis-Navigation für Budgetboote |
| Schwächen | Eingeschränkte Software-Updates, geringere Verarbeitungsqualität, limitierter Support |
| Relevanz für AYDI | Gering — Nutzerbasis primär außerhalb Europas, für Bewertung selten relevant |

### 5.8 Open-Source-Alternativen

| System | Typ | Plattform | Kosten | Stärke |
|--------|-----|-----------|--------|--------|
| OpenCPN | Kartenplotter-Software | Windows/Mac/Linux/Raspberry Pi | Kostenlos | Offene ENCs, Plugin-System, aktive Community |
| Signal K | Daten-Hub/Server | Node.js (Raspberry Pi etc.) | Kostenlos | NMEA-2000-zu-Web-Gateway, Dashboard, offene API |
| AvNav | Kartenplotter | Raspberry Pi + Android | Kostenlos | Deutsche Entwicklung, NMEA-Integration |
| Freeboard | Web-basierter Plotter | Browser-basiert | Kostenlos | Signal-K-Frontend, Kartenanzeige |

---

## 6. Fehlerbild-Atlas

### 6.1 Systematik

Fehlerbilder werden mit dem Prefix `MFD-F` codiert und nach Schweregrad (1–5) klassifiziert:

| Schweregrad | Bedeutung | Beispiel |
|-------------|-----------|---------|
| 1 — Kosmetisch | Optischer Mangel, keine Funktionseinschränkung | Pixelfehler im Display |
| 2 — Gering | Leichte Funktionseinschränkung | Reduzierte Touchscreen-Empfindlichkeit |
| 3 — Moderat | Deutliche Funktionseinschränkung | GPS-Empfang intermittierend |
| 4 — Erheblich | Sicherheitsrelevante Einschränkung | Radar-Overlay-Versatz > 50 m |
| 5 — Kritisch | Totalausfall oder falsche Sicherheitsinformation | GPS-Position springt > 500 m |

### 6.2 MFD-F01 — Display-Delamination (Bonding-Versagen)

| Attribut | Details |
|----------|---------|
| Code | MFD-F01 |
| Schweregrad | 3 — Moderat |
| Betroffene Systeme | Alle MFDs mit Optical Bonding, besonders ältere Generationen |
| Erscheinungsbild | Dunkle Flecken oder Regenbogen-Muster unter dem Displayglas, typisch an Rändern beginnend |
| Ursache | UV-Degradation des Bonding-Klebstoffs, Temperaturwechsel (Kälte/Hitze-Zyklen), mechanische Beanspruchung |
| Auswirkung | Eingeschränkte Ablesbarkeit im betroffenen Bereich, Feuchtigkeitseintritt möglich |
| Häufigkeit | 3–5% nach 5+ Jahren (bei Premium-Geräten <1%) |
| Erkennung visuell | Dunkle oder regenbogenfarbene Bereiche, besonders sichtbar bei weißem Kartenhintergrund |
| Erkennung AYDI | Visual Pipeline: Unregelmäßige Verfärbungen auf Display-Fotos |
| Behebung | Austausch des Display-Moduls (Werkstatt), kein Field-Repair möglich |
| Prävention | Sonnenschutzabdeckung bei Nichtgebrauch, UV-Schutzhülle |
| Kosten Reparatur | 400–1.200 EUR je nach Displaygröße |

### 6.3 MFD-F02 — Touchscreen-Fehleingaben (Ghost Touches)

| Attribut | Details |
|----------|---------|
| Code | MFD-F02 |
| Schweregrad | 3 — Moderat |
| Betroffene Systeme | Kapazitive Touchscreens aller Hersteller |
| Erscheinungsbild | Ungewollte Touch-Eingaben, Cursor springt, Menüs öffnen sich spontan |
| Ursache | Salzwasserfilm auf Display, defekte Touchscreen-Folie, EMV-Störung, Feuchtigkeitseintritt am Displayrand |
| Auswirkung | Unzuverlässige Bedienung, unbeabsichtigte Kursänderungen am Autopilot, Routenänderungen |
| Häufigkeit | 5–10% temporär (bei Regen/Gischt), 1–2% permanent (Hardware-Defekt) |
| Erkennung | Nutzer-Report, sichtbare Wassertropfen, erratisches MFD-Verhalten |
| Erkennung AYDI | Service-Pipeline: Keyword-Analyse in Service-Berichten |
| Behebung (temporär) | Display reinigen und trocknen, Display-Lock aktivieren |
| Behebung (permanent) | Touchscreen-Kalibrierung, Firmware-Update, Austausch Touchscreen-Panel |
| Prävention | Sprayhood/Bimini über Steuerstand, Fernbedienung als Backup |
| Kosten Reparatur | 200–800 EUR |

### 6.4 MFD-F03 — GPS-Positionssprünge (Multipath-Effekt)

| Attribut | Details |
|----------|---------|
| Code | MFD-F03 |
| Schweregrad | 4 — Erheblich |
| Betroffene Systeme | Alle MFDs mit internem GPS-Empfänger, besonders unter Bimini/Hardtop |
| Erscheinungsbild | Positionsmarker springt um 10–500 m, Kursvektor zeigt in falsche Richtung, SOG-Anzeige unrealistisch hoch |
| Ursache | Multipath-Reflexion von GPS-Signalen an Metall (Rigg, Mast, Hardtop-Struktur), mangelhafter Antennenstandort |
| Auswirkung | Falsche Positionsanzeige, Autopilot steuert Korrekturkurse, AIS-CPA-Berechnung fehlerhaft |
| Häufigkeit | 10–20% temporär (in Häfen mit hohen Kaimauern), 3–5% permanent (Montagefehler) |
| Erkennung | Vergleich GPS-Position mit visueller Position, HDOP-Wert (>3 = kritisch), Track springt auf Karte |
| Erkennung AYDI | Strukturanalyse: Metall-Abschirmung über MFD-Position erkennbar |
| Behebung | Externe GPS-Antenne am Masttopp oder Geräteträger montieren |
| Prävention | Bei Installation: externe GPS-Antenne mit freier Sicht zu 360° Horizont |
| Kosten Behebung | 150–400 EUR (externe Antenne + Montage) |

### 6.5 MFD-F04 — Netzwerkausfall NMEA 2000

| Attribut | Details |
|----------|---------|
| Code | MFD-F04 |
| Schweregrad | 4 — Erheblich |
| Betroffene Systeme | Alle NMEA-2000-vernetzten MFDs |
| Erscheinungsbild | Datenverlust einzelner oder aller Sensoren (Wind, Tiefe, Geschwindigkeit, Motor), Strich-Anzeige (---) |
| Ursache | Korrodierter T-Stück-Kontakt, fehlender/defekter Terminierungswiderstand, Wassereinbruch in Stecker, Kabelbruch, überlasteter Bus (>3A LEN) |
| Auswirkung | Verlust von Navigationsdaten, Autopilot fällt in Standby, Motorüberwachung nicht verfügbar |
| Häufigkeit | 8–15% nach 3+ Jahren (korrosionsbedingt), 2–3% Installationsfehler |
| Erkennung | MFD zeigt fehlende Datenquellen an, NMEA-2000-Netzwerk-Diagnose im MFD-Menü |
| Erkennung AYDI | Service-Pipeline: NMEA-Fehler-Keywords, Strukturanalyse: Steckerposition in Nassbereich |
| Behebung | Systematische Prüfung: Terminierung (120 Ohm an jedem Bus-Ende), Stecker auf Korrosion prüfen, T-Stücke tauschen |
| Prävention | Marine-Grade-Stecker, Gel-gefüllte T-Stücke, Kabelführung in trockenen Bereichen |
| Kosten Behebung | 50–300 EUR (Stecker/T-Stücke), 200–600 EUR (bei komplettem Backbone-Tausch) |

### 6.6 MFD-F05 — Radar-Overlay-Versatz

| Attribut | Details |
|----------|---------|
| Code | MFD-F05 |
| Schweregrad | 4 — Erheblich |
| Betroffene Systeme | Alle MFDs mit Radar-Overlay-Funktion |
| Erscheinungsbild | Radar-Echos sind gegenüber der Seekarte verschoben (typisch 20–200 m), Tonnen erscheinen neben ihrer Kartenposition |
| Ursache | Falsche Heading-Quelle (Magnetkompass statt Fluxgate), Kompass-Deviation nicht kalibriert, Radar-Antenna-Offset falsch konfiguriert |
| Auswirkung | Fehleinschätzung von Objektpositionen, falsche Kollisionsberechnung |
| Erkennung | Vergleich Radar-Echo mit Karten-Objekt (Tonne, Hafenmole), Versatz bei Kursänderung |
| Erkennung AYDI | Visuelle Analyse: Foto vom Radar-Overlay mit erkennbarem Versatz |
| Behebung | Heading-Sensor kalibrieren (Deviation-Tabelle), Radar-Antenna-Offset im MFD korrekt einstellen |
| Prävention | Bei Installation: Heading-Sensor mindestens 1 m von ferromagnetischen Massen entfernt |
| Kosten Behebung | 100–400 EUR (Kalibrierung, ggf. neuer Heading-Sensor) |

### 6.7 MFD-F06 — Echolot-Störungen (Luftblasen / Bewuchs am Geber)

| Attribut | Details |
|----------|---------|
| Code | MFD-F06 |
| Schweregrad | 3 — Moderat |
| Betroffene Systeme | Alle MFDs mit Echolot-Funktion |
| Erscheinungsbild | Tiefenwert springt, "Signal Lost"-Anzeige, starkes Rauschen im Echolot-Bild, Messwerte nur bei geringer Geschwindigkeit |
| Ursache | Luftblasenbildung am Transducer (Kavitation bei hoher Fahrt), Bewuchs auf Geberfläche, Geber nicht lotrecht montiert |
| Auswirkung | Unzuverlässige Tiefenmessung, fehlende Untiefen-Warnung, ForwardScan-Ausfall |
| Häufigkeit | 15–25% saisonal (Bewuchs), 5–10% permanent (Montagefehler) |
| Erkennung | Tiefenwert-Ausfall bei Geschwindigkeit > 6 kn, Echolot-Bild zeigt nur Rauschen |
| Erkennung AYDI | Service-Pipeline: Echolot-Ausfall-Muster in Berichten |
| Behebung | Transducer reinigen (Bewuchs), Montageposition optimieren (vor Kavitationszone), Antifouling auf Geber |
| Prävention | Transducer-Antifouling, Montage gemäß Herstelleranweisung, jährliche Reinigung |
| Kosten Behebung | 50–200 EUR (Reinigung), 300–800 EUR (Neumontage) |

### 6.8 MFD-F07 — Software-Freeze / Absturz

| Attribut | Details |
|----------|---------|
| Code | MFD-F07 |
| Schweregrad | 3 — Moderat (bis 5 — Kritisch bei Offshore) |
| Betroffene Systeme | Alle MFDs, besonders nach fehlerhaften Updates |
| Erscheinungsbild | MFD reagiert nicht auf Eingaben (Freeze), Neustart erforderlich, Bootloop, Schwarzbild |
| Ursache | Software-Bug, korruptes Update, voller Speicher (zu viele Tracks/Wegpunkte), Überhitzung |
| Auswirkung | Temporärer Verlust aller Navigationsdaten, Autopilot fällt in Standby |
| Häufigkeit | 5–10% pro Saison (temporär), 1–2% permanent (korruptes System) |
| Erkennung | MFD reagiert nicht auf Touch oder Tasten, schwarzes Display trotz Stromversorgung |
| Erkennung AYDI | Service-Pipeline: Crash/Freeze-Keywords |
| Behebung | Soft-Reset (Stromabschaltung 30 s), Hard-Reset (Werkseinstellungen), Firmware-Neuinstallation via SD-Karte |
| Prävention | Regelmäßige Firmware-Updates, Speicher aufräumen, ausreichende Belüftung |
| Kosten Behebung | 0 EUR (Selbsthilfe) bis 200 EUR (Werkstatt-Service) |

### 6.9 MFD-F08 — Korrosion an Steckverbindungen

| Attribut | Details |
|----------|---------|
| Code | MFD-F08 |
| Schweregrad | 3 — Moderat |
| Betroffene Systeme | Alle MFDs, besonders Rückseitenverbindungen (Strom, NMEA, Ethernet) |
| Erscheinungsbild | Grünliche oder weiße Ablagerungen an Steckern, intermittierender Datenverlust, Wackelkontakt |
| Ursache | Salzwasser-Exposition, unzureichende Abdichtung der Steckerverbindungen, Kondenswasser |
| Auswirkung | Intermittierende Datenverluste, Spannungseinbrüche, MFD-Neustarts |
| Häufigkeit | 10–20% nach 3+ Jahren (offene Installationen), <5% bei korrekter Installation |
| Erkennung | Sichtbare Korrosion, intermittierende Ausfälle bei Seegang (Vibrationen lösen Kontakt) |
| Erkennung AYDI | Visuell: Korrosionsspuren auf Rückseitenfotos; Service: intermittierende Fehlermuster |
| Behebung | Stecker reinigen (Kontaktspray), Korrosionsschutz auftragen, ggf. Stecker tauschen |
| Prävention | Marine-Grade-Stecker, Schrumpfschlauch über Verbindungen, wasserdichte Steckergehäuse, ACF-50-Korrosionsschutz |
| Kosten Behebung | 30–200 EUR |

### 6.10 MFD-F09 — Backlight-Ausfall (LED-Hintergrundbeleuchtung)

| Attribut | Details |
|----------|---------|
| Code | MFD-F09 |
| Schweregrad | 4 — Erheblich |
| Betroffene Systeme | Alle LCD-basierten MFDs nach Alterung |
| Erscheinungsbild | Display wird zunehmend dunkler, ungleichmäßige Ausleuchtung, Bereiche ohne Hintergrundbeleuchtung, Totalausfall |
| Ursache | LED-Alterung (typisch nach 30.000–50.000 Betriebsstunden), Überhitzung durch mangelnde Belüftung, Feuchtigkeit im LED-Bereich |
| Auswirkung | Eingeschränkte bis keine Ablesbarkeit, besonders bei Sonnenlicht |
| Häufigkeit | 2–5% nach 7+ Jahren Betrieb |
| Erkennung | Vergleich der aktuellen Helligkeit mit Neuzustand, dunkle Ecken/Ränder |
| Erkennung AYDI | Visuell: ungleichmäßige Display-Helligkeit auf Fotos |
| Behebung | LED-Modul-Austausch (Werkstatt), bei älteren Geräten wirtschaftlich oft Totalersatz |
| Prävention | Helligkeit nicht dauerhaft auf Maximum, ausreichende Hinterlüftung |
| Kosten Behebung | 300–1.000 EUR (LED-Modul) oder Neugerät |

### 6.11 MFD-F10 — Kartendaten veraltet / nicht aktualisiert

| Attribut | Details |
|----------|---------|
| Code | MFD-F10 |
| Schweregrad | 3 — Moderat (bis 5 bei Untiefen-Änderungen) |
| Betroffene Systeme | Alle MFDs mit Kartenmaterial |
| Erscheinungsbild | Neue Hafeninfrastruktur nicht dargestellt, Betonnung entspricht nicht Realität, Tiefenangaben veraltet |
| Ursache | Karten-Abonnement abgelaufen, Updates nicht durchgeführt, Wi-Fi-Konfiguration verhindert Auto-Update |
| Auswirkung | Navigation auf Basis veralteter Information, Grundberührungs-Risiko |
| Häufigkeit | 30–50% bei Nicht-Abo-Nutzern (geschätzt) |
| Erkennung | Kartenversion prüfen, Vergleich mit aktuellem NfM (Nachrichten für Seefahrer) |
| Erkennung AYDI | Service-Pipeline: Kartenversions-Check |
| Behebung | Kartenabo verlängern, Updates via Wi-Fi oder SD-Karte installieren |
| Prävention | Automatische Kartenaktualisierung aktivieren, jährliches Abo |
| Kosten Behebung | 80–250 EUR/Jahr (Kartenabo) |

### 6.12 MFD-F11 — Überhitzung und thermisches Throttling

| Attribut | Details |
|----------|---------|
| Code | MFD-F11 |
| Schweregrad | 3 — Moderat |
| Betroffene Systeme | Alle MFDs mit hoher Displayhelligkeit, besonders > 12" in Sonneneinstrahlung |
| Erscheinungsbild | Automatische Helligkeitsreduktion, Leistungsdrosselung (langsame Reaktion), Warnmeldung "Temperatur", in Extremfällen: automatische Abschaltung |
| Ursache | Direkte Sonneneinstrahlung + maximale Helligkeit, mangelnde Hinterlüftung, Einbau in geschlossener Konsole ohne Luftzirkulation |
| Auswirkung | Reduzierte Displayhelligkeit und Rechenleistung, MFD wird gerade dann dunkler, wenn hellstes Display benötigt wird |
| Häufigkeit | 10–20% bei Sommer-Bedingungen (Mittelmeer, Tropen) |
| Erkennung | Temperaturwarnung im MFD, fühlbar heißes Gehäuse |
| Erkennung AYDI | Strukturanalyse: Einbausituation, Belüftung, Klimazone |
| Behebung | Belüftung verbessern (Lüftungsschlitze in Konsole), Sonnenschutz installieren, bei Nichtgebrauch Cover nutzen |
| Prävention | Bei Installation: Mindestens 25 mm Freiraum hinter MFD, Belüftungsöffnungen in Konsole, keine Montage hinter Windschutzscheibe (Treibhauseffekt) |
| Kosten Behebung | 50–300 EUR (Konsolenmodifikation) |

### 6.13 MFD-F12 — Wassereintritt durch Montagedichtung

| Attribut | Details |
|----------|---------|
| Code | MFD-F12 |
| Schweregrad | 4 — Erheblich |
| Betroffene Systeme | Alle Flush-Mount-MFDs |
| Erscheinungsbild | Kondenswasser hinter dem Display, Korrosion an internen Platinen, sporadische Fehlfunktionen, Totalausfall |
| Ursache | Alterung der Einbaudichtung, zu starkes oder zu schwaches Anziehen der Montageschrauben, UV-Degradation des Dichtungsmaterials |
| Auswirkung | Korrosion der Elektronik, Kurzschlüsse, irreparabler Totalausfall |
| Häufigkeit | 5–10% nach 5+ Jahren (bei Flush-Mount-Installation) |
| Erkennung | Kondenswasser sichtbar hinter Displayglas, Korrosionsspuren an Kabeldurchführungen |
| Erkennung AYDI | Visuell: Kondenswasser hinter Display; Service: Feuchteschäden-Keywords |
| Behebung | MFD ausbauen, Dichtung erneuern, trocknen, ggf. Platine reinigen lassen |
| Prävention | Dichtung bei Einbau mit Sikaflex/Butylband verstärken, jährlich Sichtprüfung, Bracket-Mount statt Flush-Mount in Spritzwasserbereich |
| Kosten Behebung | 100–500 EUR (Dichtungserneuerung), Totalschaden bei Platinen-Korrosion |

---

## 7. Troubleshooting-Entscheidungsbäume

### 7.1 Entscheidungsbaum: MFD startet nicht / schwarzes Display

```
START: MFD zeigt schwarzes Display
│
├─ Schritt 1: Stromversorgung prüfen
│  ├─ Spannung am MFD-Stecker messen → < 10V?
│  │  ├─ JA → Batteriespannung und Sicherung prüfen
│  │  │  ├─ Sicherung defekt → Sicherung tauschen, Ursache suchen
│  │  │  ├─ Batterie leer → Batterie laden
│  │  │  └─ Spannung am Verteiler OK, am MFD nicht → Kabelbruch/Korrosion
│  │  └─ NEIN (Spannung OK > 10V) → weiter Schritt 2
│  │
├─ Schritt 2: Power-Button prüfen
│  ├─ Power-Button lang drücken (5 s) → MFD reagiert?
│  │  ├─ JA → MFD war nur im Standby
│  │  └─ NEIN → weiter Schritt 3
│  │
├─ Schritt 3: Hard-Reset durchführen
│  ├─ Stromversorgung trennen (30 s warten), wieder anschließen
│  │  ├─ MFD startet → Software-Problem, ggf. Firmware-Update
│  │  └─ MFD startet NICHT → weiter Schritt 4
│  │
├─ Schritt 4: LED-Indikatoren prüfen
│  ├─ Status-LED am MFD leuchtet?
│  │  ├─ JA (LED an, Display schwarz) → Backlight-Ausfall (MFD-F09)
│  │  │  oder Display-Kabel intern lose → Werkstatt
│  │  └─ NEIN (keine LED) → Hardware-Defekt (Netzteil-Platine, Hauptplatine)
│  │  → Werkstatt oder Austausch
│  │
└─ ERGEBNIS: Werkstatt-Reparatur oder Gerätetausch erforderlich
```

### 7.2 Entscheidungsbaum: Keine GPS-Position

```
START: MFD zeigt keine GPS-Position / "Searching for Satellites"
│
├─ Schritt 1: Interner oder externer GPS?
│  ├─ INTERN → weiter Schritt 2
│  └─ EXTERN → weiter Schritt 5
│
├─ Schritt 2: Standort prüfen
│  ├─ MFD unter Metall-Hardtop, Bimini mit Metallrahmen, unter Deck?
│  │  ├─ JA → Abschirmung. Externe GPS-Antenne installieren (MFD-F03)
│  │  └─ NEIN (freie Sicht) → weiter Schritt 3
│  │
├─ Schritt 3: Cold Start vs. Warm Start
│  ├─ MFD war länger als 2 Wochen ausgeschaltet oder > 500 km transportiert?
│  │  ├─ JA → Cold Start kann 5–15 Minuten dauern. Warten.
│  │  └─ NEIN → weiter Schritt 4
│  │
├─ Schritt 4: Firmware-Version prüfen
│  ├─ Firmware aktuell?
│  │  ├─ NEIN → Update durchführen, bekannte GPS-Bugs prüfen
│  │  └─ JA → Hardware-Defekt GPS-Modul → Werkstatt
│  │
├─ Schritt 5: Externe GPS-Antenne prüfen
│  ├─ NMEA-2000-GPS: Gerät im Netzwerk sichtbar?
│  │  ├─ NEIN → T-Stück, Kabel, Terminierung prüfen (MFD-F04)
│  │  └─ JA → GPS-Antenne hat Sicht? Kabel-Integrität?
│  │     ├─ Kabeltest (Widerstand) → defekt → Kabel tauschen
│  │     └─ Kabel OK → GPS-Empfänger defekt → tauschen
│
└─ ERGEBNIS: Externe GPS-Antenne installieren oder tauschen
```

### 7.3 Entscheidungsbaum: Echolot zeigt keine Tiefe

```
START: MFD zeigt keine Tiefenwerte / "No Depth Data"
│
├─ Schritt 1: Echolot-Quelle identifizieren
│  ├─ Internes Modul → Schritt 2
│  └─ Externes Modul (Netzwerk) → Schritt 5
│
├─ Schritt 2: Transducer-Kabel prüfen
│  ├─ Stecker am MFD fest und korrosionsfrei?
│  │  ├─ NEIN → Reinigen und fest anschließen
│  │  └─ JA → weiter Schritt 3
│  │
├─ Schritt 3: Geschwindigkeitsabhängig?
│  ├─ Tiefe OK bei < 3 kn, Ausfall bei > 6 kn?
│  │  ├─ JA → Luftblasen-Problem (Kavitation) → MFD-F06
│  │  │  Transducer-Position prüfen, ggf. Fairing Block
│  │  └─ NEIN → weiter Schritt 4
│  │
├─ Schritt 4: Transducer-Zustand
│  ├─ Boot an Land: Geberfläche prüfen
│  │  ├─ Bewuchs → Reinigen + Antifouling
│  │  ├─ Geber lose / schief → Neumontage
│  │  ├─ Geber beschädigt → Tauschen
│  │  └─ Geber optisch OK → Echolot-Modul defekt → Werkstatt
│  │
├─ Schritt 5: Netzwerk-Echolot
│  ├─ Echolot im MFD-Netzwerk sichtbar?
│  │  ├─ NEIN → Ethernet-Verbindung prüfen, IP-Konfiguration prüfen
│  │  └─ JA → Echolot-Modul senden Daten? → Diagnose im Echolot-Menü
│  │     ├─ Kein Signal → Transducer-Kabel am Echolot-Modul prüfen
│  │     └─ Signal OK → MFD-Firmware-Bug? → Update
│
└─ ERGEBNIS: Transducer reinigen/tauschen oder Netzwerkfehler beheben
```

### 7.4 Entscheidungsbaum: NMEA-2000-Netzwerk instabil

```
START: Intermittierender Datenverlust im NMEA-2000-Netzwerk
│
├─ Schritt 1: Welche Daten fehlen?
│  ├─ ALLE Daten → Bus-Gesamtausfall → Schritt 2
│  └─ EINZELNE Sensoren → Schritt 4
│
├─ Schritt 2: Terminierung prüfen
│  ├─ Genau 2 Terminierungswiderstände (120 Ω) im Netzwerk?
│  │  ├─ NEIN → Korrektur: Genau je 1 Terminator an jedem Backbone-Ende
│  │  └─ JA → weiter Schritt 3
│  │
├─ Schritt 3: Backbone-Integrität
│  ├─ Widerstand Backbone messen (beide Terminatoren entfernt) → Durchgang?
│  │  ├─ NEIN (Unterbrechung) → Kabelbruch lokalisieren (halber Bus, Viertel etc.)
│  │  └─ JA (Durchgang OK) → Kurzschluss? (Widerstand < 30 Ω = Kurzschluss)
│  │     ├─ JA → Defektes T-Stück oder Gerät findet → systematisch entfernen
│  │     └─ NEIN → weiter Schritt 3b
│  │
├─ Schritt 3b: Buslast prüfen
│  ├─ LEN (Load Equivalency Number) aller Geräte addieren → > 50?
│  │  ├─ JA → Bus überlastet, zweites Netzsegment mit Power-T anlegen
│  │  └─ NEIN → EMV-Störung? Kabel parallel zu Stromkabeln oder nahe Lichtmaschine?
│  │     ├─ JA → Kabelführung ändern, geschirmtes NMEA-2000-Kabel verwenden
│  │     └─ NEIN → Sporadischer Hardware-Defekt eines Geräts → systematisch trennen
│  │
├─ Schritt 4: Einzelner Sensor fehlt
│  ├─ Sensor im MFD-Geräteliste sichtbar?
│  │  ├─ NEIN → Drop-Cable und T-Stück des Sensors prüfen
│  │  │  ├─ Korrosion → Reinigen oder tauschen
│  │  │  └─ Kabel OK → Sensor defekt → tauschen
│  │  └─ JA (sichtbar aber keine Daten) → PGN-Konfiguration prüfen
│  │     ├─ Richtige Datenquelle im MFD ausgewählt?
│  │     └─ Sensor-Firmware aktuell?
│
└─ ERGEBNIS: Terminierung, Stecker oder defekten Sensor ersetzen
```

### 7.5 Entscheidungsbaum: Touchscreen reagiert nicht korrekt

```
START: Touchscreen-Probleme (nicht reagierend, falsche Position, Phantom-Touches)
│
├─ Schritt 1: Art des Problems klassifizieren
│  ├─ A) Touchscreen reagiert GAR NICHT → Schritt 2
│  ├─ B) Touch versetzt (Finger drückt hier, Reaktion woanders) → Schritt 4
│  └─ C) Phantom-Touches (ungewollte Eingaben) → Schritt 5
│
├─ Schritt 2: Touchscreen reagiert gar nicht
│  ├─ Display zeigt Bild an?
│  │  ├─ JA → Touch-Digitizer defekt oder Software-Freeze
│  │  │  ├─ Soft-Reset (Power off/on) → Problem gelöst?
│  │  │  │  ├─ JA → Einmaliger Software-Fehler
│  │  │  │  └─ NEIN → Digitizer-Hardware defekt → Werkstatt
│  │  │  └─ Fernbedienung (falls vorhanden) funktioniert? → MFD-Touchscreen defekt
│  │  └─ NEIN → Siehe Entscheidungsbaum 7.1 (MFD startet nicht)
│  │
├─ Schritt 4: Touch versetzt
│  ├─ Touchscreen-Kalibrierung im Service-Menü durchführen
│  │  ├─ Problem behoben → Kalibrierungsdrift (normal nach Temperaturwechsel)
│  │  └─ Problem bleibt → Displayfolie beschädigt oder Digitizer defekt → Werkstatt
│  │
├─ Schritt 5: Phantom-Touches
│  ├─ Tritt bei Regen/Gischt auf?
│  │  ├─ JA → Wasser auf Display verursacht kapazitive Fehlsignale (MFD-F02)
│  │  │  ├─ Display trocknen → Problem weg?
│  │  │  │  ├─ JA → Normal bei kapazitiven Displays. Fernbedienung oder Rain-Mode nutzen
│  │  │  │  └─ NEIN → Wasser im Displayrand eingedrungen → Dichtung prüfen
│  │  └─ NEIN → Tritt bei eingeschalteter Lichtmaschine/Landstrom auf?
│  │     ├─ JA → EMV-Störung → Kabelschirmung verbessern, Ferritkerne auf Stromkabel
│  │     └─ NEIN → Digitizer-Hardware-Defekt → Werkstatt
│
└─ ERGEBNIS: Kalibrierung, Trocknung, EMV-Abhilfe oder Werkstatt-Reparatur
```

---

## 8. FAQ

### 8.1 Grundlagen und Kaufberatung

**F01: Welche Displaygröße brauche ich für mein Boot?**
Faustregel: Je größer das Boot und je länger die Törns, desto größer das Display. Sportboot < 8 m: 7" genügt. Segelyacht 8–12 m: 9" Minimum, 12" empfohlen. Motoryacht 10–16 m: 12" Minimum, 16" am Flybridge. Offshore > 15 m: 16"+ am Hauptsteuerstand. Für Splitscreen-Nutzung (Karte + Echolot) sollte das Display mindestens 12" sein.

**F02: Touchscreen oder Tasten — was ist besser auf See?**
Beides hat Berechtigung. Touchscreen ist intuitiver und schneller in ruhigem Wasser. Tasten sind verlässlicher bei Seegang und Regen. Die beste Lösung ist ein Touchscreen-MFD mit optionaler Fernbedienung (Drehgeber + Tasten). Reine Touchscreen-Geräte sind bei allen Herstellern der Standard geworden.

**F03: Muss ich Karten-Abos bezahlen, oder gibt es Einmalkauf?**
Die meisten Kartenanbieter (Navionics, C-MAP, TZ Maps) sind auf Abo-Modelle umgestiegen (ca. 80–250 EUR/Jahr). Garmin BlueChart g4 ist oft beim Gerät inklusive. Grundkarten (BlueChart Basis, C-MAP Discover Basis) sind bei vielen MFDs vorinstalliert und reichen für Grundnavigation. Offizielle ENCs sind über nationale Hydrographische Dienste verfügbar (teils kostenlos).

**F04: Kann ich Karten verschiedener Anbieter auf einem MFD nutzen?**
In der Regel nicht frei wechselbar. Garmin nutzt primär BlueChart und Navionics. Simrad/B&G nutzen primär C-MAP, können aber auch Navionics lesen. Raymarine unterstützt LightHouse Charts (Navionics-basiert) und C-MAP. Furuno nutzt TZ Maps. Immer vorab die Kompatibilitätsliste des MFD-Herstellers prüfen.

**F05: Was ist der Unterschied zwischen C-MAP, Navionics und BlueChart?**
Alle drei sind hochwertige Vektorkarten. C-MAP (Navico/Brunswick) ist Standard für Simrad/B&G. Navionics (Garmin) bietet SonarChart Community-Tiefendaten. BlueChart (Garmin exklusiv) hat Auto Guidance und ActiveCaptain-Integration. Die Qualität ist vergleichbar — die Wahl wird oft durch das MFD bestimmt.

**F06: Brauche ich NMEA 2000, oder reicht NMEA 0183?**
NMEA 2000 ist der aktuelle Standard und wird für Neuinstallationen empfohlen. Es bietet: ein Kabel für alle Geräte (Bus), Plug-and-Play-Konfiguration, bidirektionale Kommunikation, Stromversorgung über den Bus. NMEA 0183 ist ausreichend für einfache Installationen (GPS → Plotter → Autopilot), aber bei mehr als 3–4 Geräten wird NMEA 2000 deutlich einfacher.

**F07: Wie verbinde ich mein MFD mit dem Smartphone?**
Alle aktuellen MFDs haben Wi-Fi. Die Verbindung erfolgt über die Hersteller-App (RayControl, ActiveCaptain, Simrad App, B&G App, TZ iBoat). Damit lässt sich das MFD fernsteuern, Kartenupdates einspielen, Routen synchronisieren und die Kartenanzeige auf dem Smartphone spiegeln.

### 8.2 Installation und Montage

**F08: Flush-Mount oder Bracket-Mount — wann was?**
Flush-Mount (bündig in Konsole eingebaut) sieht eleganter aus und ist Standard bei festen Steuerständen. Bracket-Mount (Bügelmontage, aufgesetzt) ist flexibler, einfacher zu installieren, vermeidet Dichtungsprobleme und erlaubt einfachen Gerätetausch. Empfehlung: Bracket-Mount in Spritzwasserbereichen (Cockpit-Säule), Flush-Mount in geschützten Bereichen (Instrumentenkonsole, Flybridge unter Hardtop).

**F09: Welchen Ausschnitt muss ich für ein Flush-Mount-MFD fräsen?**
Jeder Hersteller gibt in der Installationsanleitung eine Ausschnittschablone (Template) vor. Typische Ausschnittmaße (B × H): 7"-MFD: 175 × 112 mm, 9"-MFD: 230 × 138 mm, 12"-MFD: 302 × 190 mm, 16"-MFD: 392 × 242 mm. Immer das herstellerspezifische Template verwenden — Maße variieren zwischen Herstellern.

**F10: Wie verkable ich NMEA 2000 korrekt?**
Backbone-Kabel von Bug nach Heck verlegen. T-Stücke in die Backbone-Leitung einsetzen, von jedem T-Stück geht ein Drop-Cable (max. 6 m) zum Gerät. An beiden Backbone-Enden je 1 Terminierungswiderstand (120 Ohm) einsetzen. Stromversorgung über Power-T an einem zentralen Punkt einspeisen. Backbone max. 100 m, Drop-Cables max. 6 m.

**F11: Welchen Abstand muss das MFD zum Magnetkompass haben?**
Nach IEC 60945 mindestens den vom Gerätehersteller angegebenen Kompass-Sicherheitsabstand. Typische Werte: MFD 7" = 0,3–0,5 m, MFD 12" = 0,5–0,8 m, MFD 16" = 0,8–1,2 m. Dieser Abstand gilt für Standard-Magnetkompasse. Fluxgate-Kompasse sind weniger empfindlich.

**F12: Mein MFD wird in der Sonne extrem heiß — was tun?**
Hinter dem MFD mindestens 25 mm Freiraum für Luftzirkulation lassen. Belüftungsöffnungen in der Konsole vorsehen. Sonnenschutzcover verwenden, wenn nicht in Betrieb. Nicht hinter Windschutzscheibe montieren (Treibhauseffekt). Hersteller-Spezifikation für max. Betriebstemperatur beachten (typisch +55°C).

### 8.3 Betrieb und Segelfunktionen

**F13: Was ist SailSteer bei B&G?**
SailSteer ist eine B&G-exklusive Bildschirmdarstellung, die alle segelrelevanten Daten in einem Polardiagramm zusammenfasst: True Wind Angle, Apparent Wind Angle, Laylines zum Wegpunkt, VMG (Velocity Made Good), Segelvorschlag, Performance-Prozent gegenüber Polardaten. Es ist das Kernfeature, das B&G von anderen MFD-Herstellern unterscheidet.

**F14: Was sind Laylines und warum sind sie wichtig?**
Laylines zeigen den optimalen Kurs zum Zielwegpunkt unter Berücksichtigung des aktuellen Windes. Für Segler auf Kreuzgang zeigen sie, wo gewendet/gehalst werden muss, um den Zielpunkt direkt anzulaufen. Laylines berücksichtigen Windrichtung, Strömung und Boot-Polardaten. B&G berechnet sie in Echtzeit.

**F15: Kann ich Polardaten meines Bootes ins MFD importieren?**
Bei B&G Zeus S: Ja, VPP-Polardaten können importiert werden (gängige Formate). Das MFD vergleicht dann die aktuelle Geschwindigkeit mit dem theoretischen Optimum. Andere Hersteller (Garmin, Raymarine, Simrad) bieten diese Funktion nicht nativ — hier ist ein externer Segelcomputer (Expedition, Adrena) erforderlich.

**F16: Was ist ClearCruise AR bei Raymarine?**
ClearCruise AR (Augmented Reality) nutzt eine Kamera am Bug oder Mast, um das Live-Bild mit Navigationsinformationen zu überlagern: AIS-Ziele werden mit Name und Kursvektor markiert, Bojen und Landmarken werden identifiziert, Untiefen und Gefahrenzonen werden im Bild markiert. In der neuesten Version (Axiom 2 Pro/XL) wird KI-basierte Objekterkennung verwendet.

**F17: Was ist ForwardScan und brauche ich das?**
ForwardScan ist ein vorausschauendes Sonar von Simrad/B&G. Es zeigt den Meeresgrund vor dem Boot (bis 90 m voraus). Essenziell für: Segler in Flachwasserrevieren (Ostsee, Wattenmeer), Langfahrt in wenig vermessenen Gebieten, Ankerplatzsuche. Für Motoryachten im Tiefwasser weniger relevant.

### 8.4 Karten und Navigation

**F18: Wie genau ist die GPS-Position auf meinem MFD?**
Standard-GPS (interner Empfänger): 2–5 m Genauigkeit (95% der Zeit). Mit WAAS/EGNOS-Korrektur: 0,5–1,5 m. Mit externem Multi-GNSS-Empfänger: 1–3 m. Wichtig: Die Seekarte selbst kann eine Ungenauigkeit von 5–50 m haben — die GPS-Position ist oft genauer als die Karte.

**F19: Was ist der Unterschied zwischen SOG und STW?**
SOG (Speed Over Ground) wird vom GPS gemessen und zeigt die tatsächliche Geschwindigkeit über Grund (inklusive Strömungseinfluss). STW (Speed Through Water) wird von der Logge/Paddel-Sensor gemessen und zeigt die Geschwindigkeit durchs Wasser. Differenz SOG – STW = Strömungseinfluss.

**F20: Kann ich mein MFD als ECDIS nutzen (Berufsschifffahrt)?**
Nein. Kein Yacht-MFD erfüllt die IEC-61174-Anforderungen für ECDIS (Electronic Chart Display and Information System). ECDIS erfordert zertifizierte Hardware, Type-Approved-Karten (S-63), Redundanz und regelmäßige Zertifizierung. Yacht-MFDs sind explizit nur Navigationshilfen, keine ECDIS-Ersatzgeräte.

**F21: Mein MFD zeigt eine Wassertiefe, die nicht mit der Karte übereinstimmt — was stimmt?**
Beide können korrekt sein. Kartentiefen beziehen sich auf Kartennull (LAT — Lowest Astronomical Tide), das Echolot misst die aktuelle Tiefe ab Transducer. Bei Flut oder Hochwasser ist die echte Tiefe größer als die Kartenangabe. Zudem: der Geber misst ab Transducer, nicht ab Kiel — Tiefe unter Kiel = Echolot minus Kiel-Offset (im MFD einzustellen).

### 8.5 Wartung und Fehlersuche

**F22: Wie oft soll ich die Firmware meines MFD updaten?**
Mindestens 1× pro Saison (vor Saisonstart). Kritische Sicherheitsupdates sofort. Updates beheben Bugs, verbessern Performance und fügen Funktionen hinzu. Vor dem Update: Wegpunkte/Routen sichern (Export auf SD-Karte).

**F23: Mein MFD hat Pixelfehler — ist das ein Garantiefall?**
Einzelne Pixelfehler (1–3 tote Pixel) gelten bei den meisten Herstellern als innerhalb der Toleranz und sind kein Garantiefall. Pixel-Cluster (> 3 benachbarte tote Pixel) oder leuchtende Pixel (Stuck Pixels) in der Displaymitte werden in der Regel als Garantiefall anerkannt. Immer beim Hersteller anfragen.

**F24: Wie reinige ich das MFD-Display richtig?**
Nur mit weichem, feuchtem Mikrofasertuch und klarem Süßwasser. Keine Scheiben-/Glasreiniger (können Anti-Reflexions-Beschichtung beschädigen). Kein Isopropanol auf der Displayoberfläche. Salzrückstände mit Süßwasser abspülen, nicht trocken reiben. Optional: Marine-Display-Reiniger (z.B. Raymarine Display Cleaner).

**F25: Mein MFD ist außerhalb der Garantie defekt — reparieren oder neu kaufen?**
Faustregel: Display-Reparatur lohnt ab 16" (Neupreis > 4.000 EUR). Bei 7–9" MFDs ist Reparatur selten wirtschaftlich (Reparatur 400–800 EUR vs. Neugerät 600–1.500 EUR). Blackbox-Systeme (Furuno TZT2BB) sind günstiger zu reparieren, da nur Prozessor oder Monitor getauscht wird.

**F26: Wie lange hält ein Marine-MFD typischerweise?**
Typische Lebensdauer: 7–12 Jahre bei sachgemäßer Installation und Pflege. Limitierende Faktoren: Display-Alterung (Helligkeit nimmt ab), Software-Support-Ende (typisch 5–8 Jahre nach Markteinführung), Touchscreen-Degradation, Batterie (bei Modellen mit interner Backup-Batterie).

**F27: Kann ich ein altes NMEA-0183-Gerät an mein neues NMEA-2000-MFD anschließen?**
Ja, mit einem NMEA-0183-zu-NMEA-2000-Gateway. Empfohlene Gateways: Actisense NGW-1 (ca. 160 EUR), Yacht Devices YDNG-02 (ca. 120 EUR), Maretron IPG100 (ca. 350 EUR). Das Gateway wandelt die seriellen NMEA-0183-Sentences in NMEA-2000-PGNs um.

### 8.6 Spezialfragen

**F28: Welches MFD-System empfehlt sich für Blauwassersegler?**
Redundanz ist Trumpf. Empfehlung: 2 unabhängige MFDs (verschiedene Stromkreise), externes GPS mit eigenem Backup, Papierseekarten als ultimatives Backup. B&G Zeus S für Segelfunktionen oder Raymarine Axiom 2 Pro für ClearCruise AR. Furuno TZT3 für maximale Zuverlässigkeit.

**F29: Wie integriere ich Starlink-Internet mit meinem MFD?**
Starlink liefert Internet über Ethernet oder Wi-Fi zum Bordnetzwerk. Die meisten MFDs können über das Bord-Wi-Fi (Router) auf Internet zugreifen für: Kartenaktualisierungen, Wetterdaten (GRIB-Files), Cloud-Synchronisation, App-Fernsteuerung von Land. Direkte Starlink-zu-MFD-Verbindung ist nicht nötig — ein Bordrouter vermittelt.

**F30: Was ist Signal K und lohnt sich das für mein Boot?**
Signal K ist ein offenes, JSON-basiertes Datenprotokoll für die Vernetzung von Bordgeräten. Es fungiert als universeller Übersetzer zwischen NMEA 2000, NMEA 0183 und Web-Technologien. Lohnt sich für: technikaffine Eigner, die eigene Dashboards (Grafana, InfluxDB) aufbauen, OpenCPN-Nutzer, Home-Automation-Enthusiasten. Nicht notwendig für Standardinstallationen mit einem Hersteller-Ökosystem.

---

## 9. Glossar

### A

**ActiveCaptain** — Garmin-Community-Plattform für Hafenbewertungen, Gefahrenmeldungen, Routenvorschläge und Kartenupdates. Kostenlos nutzbar über die ActiveCaptain-App.

**AIS (Automatic Identification System)** — Automatisches Identifikationssystem für Schiffe. Sendet und empfängt Positions-, Kurs- und Identifikationsdaten per UKW-Funk. Pflicht für Berufsschifffahrt, optional für Sportboote.

**AR (Augmented Reality)** — Erweiterte Realität. Im MFD-Kontext: Überlagerung des Kamera-Livebilds mit Navigationsinformationen (AIS-Ziele, Bojen, Untiefen).

**Auto Guidance** — Garmin-Funktion zur kartenbasierten Routenberechnung unter Berücksichtigung von Wassertiefen und Hindernissen. Kein Autopilot, nur Routenvorschlag.

**AWA (Apparent Wind Angle)** — Scheinbarer Windwinkel. Der Winkel, unter dem der Wind relativ zur Bootslängsachse an Bord wahrgenommen wird (Kombination aus wahrem Wind und Fahrtwind).

### B

**Backbone** — Hauptkabel des NMEA-2000-Netzwerks, an das über T-Stücke die einzelnen Geräte angeschlossen werden. Maximale Länge: 100 m.

**Blackbox** — Prozessoreinheit ohne eigenes Display, die über HDMI oder andere Videoanschlüsse mit externen Monitoren verbunden wird (z.B. Furuno TZT2BB).

**BlueChart** — Garmin-eigenes digitales Seekartenformat. Aktuelle Version: BlueChart g4 mit Auto Guidance, Relief Shading und ActiveCaptain-Integration.

**Bonding (Optical)** — Fertigungsverfahren, bei dem Displayglas und LCD-Panel lückenlos verklebt werden, um den Luftspalt zu eliminieren. Verbessert Sonnenlichtablesbarkeit und mechanische Stabilität.

### C

**CHIRP (Compressed High-Intensity Radar Pulse)** — Echolot-Technologie, die statt einer einzelnen Frequenz einen Frequenzsweep sendet (z.B. 50–200 kHz). Ergebnis: höhere Auflösung und bessere Zielunterscheidung.

**C-MAP** — Digitaler Seekartenanbieter, Schwesterunternehmen von Navico (Simrad, B&G, Lowrance). Kartenebenen: Discover, Reveal, Discover X.

**COG (Course Over Ground)** — Kurs über Grund. Die Richtung, in die sich das Schiff tatsächlich bewegt, gemessen vom GPS. Unterschied zum Heading: COG berücksichtigt Strömung und Abtrift.

**CPA (Closest Point of Approach)** — Nächster Annäherungspunkt. Die geringste Entfernung, die ein anderes Schiff bei gleichbleibendem Kurs und Geschwindigkeit erreichen wird. Zentrale AIS-Sicherheitsfunktion.

### D

**DFF (Digital Fish Finder)** — Furuno-Bezeichnung für ihre Echolot-Module. DFF-3D ist das Multibeam-3D-Echolot-Modul.

**DGNSS (Differential GNSS)** — Korrektursignal, das die GPS-Genauigkeit auf 0,5–2 m verbessert. Wird von terrestrischen Referenzstationen ausgestrahlt.

**Drop-Cable** — Stichleitungskabel im NMEA-2000-Netzwerk, das ein Gerät mit dem Backbone verbindet. Maximale Länge: 6 m.

### E

**ECDIS (Electronic Chart Display and Information System)** — Zertifiziertes elektronisches Seekartenanzeige- und Informationssystem für die Berufsschifffahrt nach IEC 61174. Yacht-MFDs sind kein ECDIS-Ersatz.

**EGNOS (European Geostationary Navigation Overlay Service)** — Europäisches Korrektursignal für GPS/GNSS, das die Positionsgenauigkeit auf 0,5–1,5 m verbessert. Kostenlos empfangbar.

**ENC (Electronic Navigational Chart)** — Offizielle digitale Seekarte nach IHO-Standard S-57/S-63, herausgegeben von nationalen Hydrographischen Diensten.

### F

**FMCW (Frequency Modulated Continuous Wave)** — Radartechnologie mit kontinuierlicher Frequenzmodulation statt einzelner Pulse. Basis für Broadband-Radar mit hoher Nahbereichsauflösung.

**ForwardScan** — Simrad/B&G-Technologie für vorausschauendes Sonar. Erfasst den Meeresgrund bis 90 m voraus des Bootes.

**Flush-Mount** — Einbauart, bei der das MFD bündig in eine Konsolenöffnung eingesetzt wird. Erfordert präzisen Ausschnitt.

### G

**Galileo** — Europäisches Satellitennavigationssystem (EU). Seit 2024 voll operativ mit 28 aktiven Satelliten. Ergänzt GPS für bessere Genauigkeit.

**GLONASS** — Russisches Satellitennavigationssystem. 24 aktive Satelliten. Multi-GNSS-Empfang (GPS + GLONASS) verbessert die Positionsgenauigkeit.

**GNSS (Global Navigation Satellite System)** — Oberbegriff für alle Satellitennavigationssysteme (GPS, GLONASS, Galileo, BeiDou).

**GRIB (GRIdded Binary)** — Standardformat für Wetterdaten (Wind, Wellen, Druck) in der Seenavigation. Wird für Wetter-Routing verwendet.

### H

**HDOP (Horizontal Dilution of Precision)** — Maß für die geometrische Qualität der Satellitenverteilung am Himmel. HDOP < 1,5 = exzellent, 1,5–3,0 = gut, > 3,0 = schlecht.

**Heading** — Kurs, in den der Bug des Schiffes zeigt. Gemessen vom Kompass (magnetisch oder elektronisch). Unterschied zu COG: Heading zeigt Bugrichtung, COG die tatsächliche Bewegungsrichtung.

### I

**IPS (In-Plane Switching)** — LCD-Panel-Technologie mit weitem Blickwinkel (±178°) und guter Farbtreue. Standard bei allen aktuellen Premium-Marine-MFDs.

**IP67/IPX7** — Schutzart nach IEC 60529. IP67: staubdicht, Schutz gegen zeitweiliges Untertauchen (30 min, 1 m Tiefe). IPX7: nur Wasserschutz (ohne Staubschutz-Angabe).

### L

**Layline** — Gedachte Linie, die den optimalen Kreuzungskurs (am Wind) zum Zielpunkt darstellt. Wird von B&G MFDs in Echtzeit berechnet.

**LEN (Load Equivalency Number)** — Kennzahl für den Stromverbrauch eines NMEA-2000-Geräts. 1 LEN = 50 mA. Maximale Buslast: 50 LEN (2,5 A).

**LightHouse** — Betriebssystem der Raymarine MFDs. Aktuelle Version: LightHouse 4.

### M

**MARPA (Mini Automatic Radar Plotting Aid)** — Automatische Zielverfolgung im Radar. Berechnet CPA und TCPA für manuell markierte Ziele.

**MFD (Multi-Function Display)** — Multifunktionsdisplay. Zentrales Navigationsgerät, das Kartenplotter, Echolot, Radar, AIS und weitere Funktionen vereint.

**MMSI (Maritime Mobile Service Identity)** — Neunstellige Kennung, die jedem Schiff mit Funkanlage/AIS zugeordnet ist. Wie eine Telefonnummer für Schiffe.

### N

**Navionics** — Digitaler Seekartenanbieter (seit 2017 Garmin-Tochter). Bietet Navionics+ und Platinum+ Karten. SonarChart: Community-basierte Tiefenkarten.

**NMEA 0183** — Serielles Datenprotokoll (RS-422, 4.800 Baud) für Marine-Elektronik. Älterer Standard, noch weit verbreitet. ASCII-basiert.

**NMEA 2000** — CAN-basierter Datenbus (250 kBit/s) für Marine-Elektronik nach IEC 61162-3. Moderner Standard mit Plug-and-Play-Konfiguration.

**Nits** — Einheit der Leuchtdichte (cd/m²). Je höher der Nits-Wert, desto heller das Display. Marine-Standard: > 1.000 nits für Außenbereich.

### P

**PGN (Parameter Group Number)** — Datenpaketnummer im NMEA-2000-Protokoll. Jede PGN definiert einen bestimmten Datentyp (z.B. PGN 128267 = Wassertiefe).

**Polardaten** — Diagramm, das die theoretische Bootsgeschwindigkeit in Abhängigkeit von Windwinkel und Windstärke darstellt. Wird für Performance-Analyse bei B&G MFDs verwendet.

### R

**RNC (Raster Navigational Chart)** — Gescannte Papierseekarte als digitale Rasterkarte. Wird zunehmend durch Vektorkarten (ENC) ersetzt.

### S

**SailSteer** — B&G-exklusive Darstellungsform, die alle segelrelevanten Daten in einem Polardiagramm zusammenfasst (TWA, Laylines, VMG, Performance%).

**SeaTalkng** — Raymarine-Implementierung des NMEA-2000-Standards. Physisch und elektrisch kompatibel mit NMEA 2000, nutzt aber spezielle Stecker (SeaTalkng-Stecker).

**Signal K** — Offenes, JSON-basiertes Datenprotokoll für die Vernetzung von Bordgeräten. Universeller Übersetzer zwischen NMEA und Web-Technologien.

**SOG (Speed Over Ground)** — Geschwindigkeit über Grund, gemessen vom GPS. Beinhaltet Strömungseinfluss.

**STW (Speed Through Water)** — Geschwindigkeit durchs Wasser, gemessen von der Logge/Paddel-Sensor. Ohne Strömungseinfluss.

### T

**TCPA (Time to Closest Point of Approach)** — Zeitdauer bis zum nächsten Annäherungspunkt (CPA). Zentrale AIS-Sicherheitsberechnung.

**Terminierung** — 120-Ohm-Widerstand an den beiden Enden eines NMEA-2000-Backbones zur Vermeidung von Signalreflexionen. Genau 2 Terminatoren pro Netzwerk.

**TimeZero** — Kartenplotter-Software von Furuno, basierend auf MaxSea-Technologie. Bekannt für 3D-Kartendarstellung und fortschrittliches Routing.

**TZ Maps** — Furuno/TimeZero-eigenes Kartenformat mit 3D-Bathymetrie. Exklusiv für TZT-Serie.

**TWA (True Wind Angle)** — Wahrer Windwinkel. Der tatsächliche Winkel zwischen Windrichtung und Bootslängsachse, bereinigt um den Fahrtwindeinfluss.

### V

**VMG (Velocity Made Good)** — Geschwindigkeitskomponente in Richtung des Ziels. Wichtigste Metrik beim Kreuzen: die effektive Geschwindigkeit zum Ziel.

**VPP (Velocity Prediction Program)** — Software zur Berechnung der theoretischen Bootsgeschwindigkeit in Abhängigkeit von Windstärke und -richtung. Ergebnis: Polardaten.

### W

**WAAS (Wide Area Augmentation System)** — US-amerikanisches Korrektursignal für GPS. Verbessert die Genauigkeit auf 0,5–1,5 m. Kostenlos in Nordamerika.

### X

**XTE (Cross Track Error)** — Querabweichung von der geplanten Route. Wird vom MFD berechnet und an den Autopilot übermittelt, der den Kurs korrigiert.

---

## 10. Schnell-Referenz

### 10.1 Kaufentscheidung — Schnellvergleich nach Einsatzzweck

| Einsatzzweck | Empfehlung 1 | Empfehlung 2 | Begründung |
|-------------|-------------|-------------|------------|
| Segelyacht Küste (8–12 m) | B&G Zeus S 9" | Raymarine Axiom 2 Pro 9" | Segelfunktionen / AR |
| Segelyacht Offshore (12+ m) | B&G Zeus S 12" | Furuno TZT3 12F | SailSteer / Zuverlässigkeit |
| Motoryacht Küste (8–12 m) | Simrad NSX 3009 | Garmin GPSMAP 923xsv | Helligkeit / Preis-Leistung |
| Motoryacht Offshore (12+ m) | Garmin GPSMAP 8616xsv | Raymarine Axiom 2 XL 16 | Ökosystem / AR |
| Anglerboot | Garmin GPSMAP 1243xsv | Simrad NSX 3012 | Echolot / Fischfinder |
| Regattayacht | B&G Zeus S 12" + Expedition PC | B&G Zeus S 16" | SailSteer + Profisoftware |
| Superyacht / Glasbrücke | Simrad NSO Evo3S 16–24" | Furuno TZT2BB + Monitor | Skalierbar / Professionell |
| Budget (< 700 EUR) | Garmin echoMAP UHD2 72sv | Lowrance Eagle 7 | Gutes Echolot / Basisnavigation |

### 10.2 Displaygrößen-Referenz

| Boot-Länge | Empfehlung Cockpit/Flybridge | Empfehlung Unter Deck | Kommentar |
|------------|------------------------------|----------------------|-----------|
| < 8 m | 7" | — | 1 MFD genügt |
| 8–10 m | 9" | — | Optional 7" am Navitisch |
| 10–13 m | 9" oder 12" | 9" | 2 MFDs empfohlen |
| 13–16 m | 12" oder 16" | 12" | 2–3 MFDs |
| 16–20 m | 16" | 12" | 2–4 MFDs |
| > 20 m | 16" oder 19" | 16" | 3–6 MFDs, Glasbrücke |

### 10.3 Stromverbrauch — Planungshilfe

| Displaygröße | Typischer Verbrauch (12V) | Max. Verbrauch (12V) |
|--------------|--------------------------|---------------------|
| 7" | 8–12 W (0,7–1,0 A) | 15 W (1,3 A) |
| 9" | 12–16 W (1,0–1,3 A) | 22 W (1,8 A) |
| 12" | 16–22 W (1,3–1,8 A) | 30 W (2,5 A) |
| 16" | 22–30 W (1,8–2,5 A) | 40 W (3,3 A) |
| 19" | 30–38 W (2,5–3,2 A) | 50 W (4,2 A) |
| 22" | 35–45 W (2,9–3,8 A) | 60 W (5,0 A) |

### 10.4 Ausschnittmaße (Flush-Mount, Richtwerte)

| Displaygröße | Raymarine (B×H mm) | Garmin (B×H mm) | Simrad (B×H mm) | Furuno (B×H mm) |
|-------------|-------------------|----------------|----------------|----------------|
| 7" | 178 × 110 | 183 × 114 | 175 × 108 | 182 × 112 |
| 9" | 232 × 138 | 237 × 142 | 228 × 136 | 236 × 140 |
| 12" | 305 × 192 | 310 × 196 | 302 × 188 | 308 × 194 |
| 16" | 398 × 248 | 404 × 252 | 395 × 244 | 402 × 250 |

**Hinweis:** Immer das herstellerspezifische Template verwenden. Diese Richtwerte dienen nur der Vorplanung.

### 10.5 NMEA-2000-Verkabelung — Schnellübersicht

```
[Terminierung 120Ω] ── Backbone ──┬── Backbone ──┬── Backbone ── [Terminierung 120Ω]
                                   │              │
                              [T-Stück]      [T-Stück]
                                   │              │
                             Drop-Cable      Drop-Cable
                             (max. 6 m)      (max. 6 m)
                                   │              │
                               [MFD]        [Wind-Sensor]

Regeln:
- Backbone max. 100 m
- Drop-Cable max. 6 m
- Genau 2 Terminatoren (je 1 pro Ende)
- Power-T für Stromeinspeisung
- Max. 50 Geräte, max. 50 LEN (2,5 A)
```

### 10.6 Wartungsintervalle

| Tätigkeit | Intervall | Aufwand |
|-----------|-----------|---------|
| Display reinigen (Süßwasser + Mikrofasertuch) | Monatlich | 5 min |
| Steckerverbindungen Sichtprüfung | Halbjährlich | 15 min |
| NMEA-2000-Stecker auf Korrosion prüfen | Jährlich | 30 min |
| Firmware-Update | Jährlich (vor Saison) | 20 min |
| Kartenaktualisierung | Jährlich | 15 min |
| Transducer reinigen (Bewuchs) | Jährlich (Antifouling) | 15 min |
| GPS-Antennen-Kabel Sichtprüfung | Jährlich | 10 min |
| Sonnenschutzabdeckung erneuern | Alle 3–5 Jahre | 10 min |
| Einbaudichtung prüfen (Flush-Mount) | Alle 3–5 Jahre | 30 min |
| Backup-Batterie tauschen (falls vorhanden) | Alle 5 Jahre | Werkstatt |

---

## ANHANG A–H — Fallstudien

### ANHANG A — Fallstudie: Bavaria C42 — Elektronik-Upgrade von Raymarine C80 auf Axiom 2 Pro 12

**Ausgangssituation:**
- Boot: Bavaria C42 (Baujahr 2008), 12,8 m Segelyacht
- Bestehendes System: Raymarine C80 (8" MFD, 2007), ST60+ Instrumente, ST6001+ Autopilot, Pathfinder Radar
- Problem: C80 EOL (End-of-Life), keine Firmware-Updates mehr, Display dunkel und schwer lesbar, keine Wi-Fi-Anbindung, Karten veraltet
- Budget: ca. 5.000 EUR für komplettes Elektronik-Upgrade

**Planung:**
- Neues Haupt-MFD: Raymarine Axiom 2 Pro 12 RV (2.499 EUR)
- Neue Instrumente: Raymarine i70s Wind/Speed/Depth (3× 349 EUR = 1.047 EUR)
- Bestehender Autopilot (Evolution EV-1) bleibt, neuer ACU-100 Kurscomputer (699 EUR)
- NMEA-2000-Backbone neu (250 EUR Kabel + T-Stücke)
- Installation: Eigenleistung + 4h Elektriker (400 EUR)

**Durchführung:**
1. NMEA-2000-Backbone verlegen (Maschinenraum → Steuerstand → Mast)
2. Axiom 2 Pro 12 im bestehenden Ausschnitt montieren (C80-Ausschnitt nur 5 mm kleiner → Adapterplatte)
3. SeaTalkng-Instrumente anschließen
4. Evolution-Autopilot auf NMEA 2000 migrieren
5. Radar Quantum 2 als zukünftiges Upgrade vorbereitet (Ethernet-Kabel zum Mast gelegt)

**Ergebnis:**
- Gesamtkosten: 4.895 EUR
- Vollfunktionales modernes Navigationssystem mit Wi-Fi, App-Steuerung, aktuellen Karten
- Autopilot-Integration über NMEA 2000 deutlich zuverlässiger als alte SeaTalk-Verbindung
- ClearCruise AR als Bonus (Kamera nachgerüstet)

**AYDI-Bewertung:**
- Ergonomie: 82/100 (12" Display am Steuerstand, guter Blickwinkel)
- Compliance: 90/100 (aktuelle Karten, AIS-Integration)
- Kosten: 75/100 (gutes Preis-Leistungs-Verhältnis für Mittelklasse-Segelyacht)
- Confidence: documented (Installations-Dokumentation, Herstellerempfehlung)

### ANHANG B — Fallstudie: Hanse 548 — B&G Vollausstattung für Offshore-Segeln

**Ausgangssituation:**
- Boot: Hanse 548 (Baujahr 2022), 16,2 m Performance-Cruiser
- Anforderung: Komplette B&G-Ausstattung für Atlantiküberquerung
- Budget: 18.000 EUR (Elektronik gesamt)

**Konfiguration:**
- Cockpit: B&G Zeus S 16" als Haupt-MFD (4.499 EUR)
- Cockpit-Säule: B&G Zeus S 9" als Zweitdisplay (2.099 EUR)
- Navigationstisch: B&G Zeus S 12" (2.799 EUR)
- Instrumente: B&G Triton2 Displays (4× 449 EUR = 1.796 EUR)
- Wind: B&G WS320 Wireless Windgeber (449 EUR)
- Autopilot: B&G NAC-3 + Hydraulikpumpe (3.199 EUR)
- Radar: HALO 20+ Dome (2.199 EUR)
- ForwardScan: ForwardScan Transducer (799 EUR)
- AIS: B&G V60-B VHF mit AIS (699 EUR)
- NMEA 2000: Backbone-Kit (350 EUR)

**Segelfunktionen-Konfiguration:**
- Polardaten der Hanse 548 importiert (ORC-Daten)
- SailSteer als Hauptdarstellung auf 16"-MFD
- Laylines + Strömungsvektoren aktiv
- ForwardScan im Cockpit-9" als dedizierte Untiefen-Warnung
- Startlinien-Tool für gelegentliche Regatten konfiguriert

**Ergebnis:**
- Gesamtkosten: 18.888 EUR
- Vollintegriertes Segelsystem mit Performance-Analyse
- 3 synchrone MFDs mit unterschiedlichen Darstellungen (Cockpit: SailSteer, Säule: Karte+ForwardScan, Navitisch: Radar+Karte)
- Wi-Fi-Sync aller Wegpunkte und Routen zwischen allen MFDs

**AYDI-Bewertung:**
- Ergonomie: 92/100 (3 Displays, optimale Positionierung)
- Compliance: 95/100 (AIS, Radar, aktuelle Karten, ForwardScan)
- Kosten: 70/100 (Premiumpreis, aber Funktionsumfang rechtfertigt Investition)
- Confidence: measured (vollständige Herstellerdokumentation)

### ANHANG C — Fallstudie: Prestige 520 — Garmin Flybridge + Unterdeck

**Ausgangssituation:**
- Boot: Prestige 520 (Baujahr 2023), 15,8 m Motoryacht mit Flybridge
- Anforderung: Dual-Steuerstand-Ausstattung, einfache Bedienung, gutes Echolot
- Budget: 12.000 EUR

**Konfiguration:**
- Flybridge: Garmin GPSMAP 8616xsv 16" (4.299 EUR)
- Unterdeck: Garmin GPSMAP 8612xsv 12" (3.299 EUR)
- Radar: Garmin GMR Fantom 24 Dome (2.199 EUR)
- Autopilot: Garmin Reactor 40 + GHP 20 (1.999 EUR)
- Audio: Garmin Fusion Apollo RA770 (599 EUR)
- NMEA 2000: Backbone-Kit (350 EUR)

**Besonderheiten:**
- SmartMode: Kontextabhängige Startseite (Cruising, Docking, Fishing)
- ActiveCaptain Community: Hafenbewertungen für Mittelmeer-Touring
- Garmin Quickdraw Contours: Automatische Tiefenkarten-Erstellung
- OneHelm: Mercury VesselView-Integration für Motorüberwachung
- Musik-Steuerung direkt über MFD (Fusion-Integration)

**Ergebnis:**
- Gesamtkosten: 12.745 EUR
- Zwei synchrone MFDs mit identischer Bedienung
- Intuitives Garmin-Ökosystem, minimale Einarbeitungszeit
- Echolot-Qualität (CHIRP + ClearVü + SideVü) hervorragend

**AYDI-Bewertung:**
- Ergonomie: 88/100 (großes Display am Flybridge, gute Ablesbarkeit)
- Compliance: 88/100 (Radar, AIS über VHF-Integration)
- Kosten: 82/100 (gutes Preis-Leistungs-Verhältnis)
- Confidence: documented (Garmin-Systemdokumentation)

### ANHANG D — Fallstudie: Jeanneau Sun Odyssey 440 — Budget-Elektronik mit Simrad NSX

**Ausgangssituation:**
- Boot: Jeanneau Sun Odyssey 440 (Baujahr 2024), 13,3 m Fahrtensegler
- Anforderung: Grundausstattung für Küstennavigation Mittelmeer, möglichst günstig
- Budget: 3.500 EUR

**Konfiguration:**
- Cockpit: Simrad NSX 3009 9" (1.699 EUR)
- Instrumente: Simrad IS42 Digital Display (2× 399 EUR = 798 EUR)
- Autopilot: Simrad NAC-1 + TP22 Pinnenpilot (899 EUR)
- NMEA 2000: Basis-Backbone (200 EUR)

**Ergebnis:**
- Gesamtkosten: 3.596 EUR
- Solides Grundsystem mit bestem Display am Markt (2.000 nits)
- C-MAP Discover X vorinstalliert — Mittelmeerabdeckung komplett
- Erweiterbar um Radar, ForwardScan, AIS in späteren Saisons

**AYDI-Bewertung:**
- Ergonomie: 78/100 (9" ausreichend für Cockpit-Säule, kein Zweit-MFD)
- Compliance: 72/100 (kein Radar, kein AIS — für Küste CE-konform)
- Kosten: 92/100 (hervorragendes Preis-Leistungs-Verhältnis)
- Confidence: documented (Simrad-Installationsanleitung)

### ANHANG E — Fallstudie: Hallberg-Rassy 44 — Furuno TZT3 für Langfahrt

**Ausgangssituation:**
- Boot: Hallberg-Rassy 44 (Baujahr 2020), 13,4 m Blauwasser-Cruiser
- Anforderung: Maximale Zuverlässigkeit, professionelle Kartenqualität, Langfahrt-tauglich
- Budget: 15.000 EUR

**Konfiguration:**
- Navigationstisch: Furuno TZT3 12F als Haupt-MFD (2.999 EUR)
- Cockpit: Furuno TZT3 9F als Zweit-MFD (2.299 EUR)
- Radar: Furuno DRS4DL+ Radome (2.499 EUR)
- Echolot: Furuno DFF1-UHD Schwarzbox + Transducer (1.899 EUR)
- AIS: Furuno FA-70 Class-B+ Transponder (999 EUR)
- Autopilot: Furuno NavPilot 711C (2.799 EUR)
- GPS: Furuno GP-39 externer Empfänger (599 EUR)
- NMEA 2000: Backbone (350 EUR)

**Besonderheiten:**
- TimeZero V6: 3D-Kartendarstellung für unbekannte Gewässer besonders wertvoll
- Cloud-Routing: Wetteroptimierte Routenberechnung für Ozeanüberquerungen
- RezBoost: KI-gestützte Echolot-Auflösung für Ankerplatzsuche in unbekannten Buchten
- Furuno-Zuverlässigkeit: Berufsschifffahrt-Heritage als Vertrauensfaktor
- USB-Maus am TZT3 für PC-ähnliche Bedienung am Navigationstisch

**Ergebnis:**
- Gesamtkosten: 14.443 EUR
- Professionelles System mit Berufsschifffahrt-Qualität
- Externe GPS-Antenne für maximale Positionsgenauigkeit
- Furuno NavPilot mit adaptivem Lernen für Offshore-Steuerung

**AYDI-Bewertung:**
- Ergonomie: 85/100 (2 MFDs, USB-Maus am Navitisch)
- Compliance: 95/100 (AIS, Radar, externes GPS, aktuelle Karten)
- Kosten: 68/100 (Premium-Preis, gerechtfertigt durch Zuverlässigkeit)
- Confidence: measured (Furuno-Systemdokumentation, Berufsschifffahrt-Zertifizierungen)

### ANHANG F — Fallstudie: Beneteau Gran Turismo 36 — Problemlösung NMEA-2000-Netzwerkfehler

**Ausgangssituation:**
- Boot: Beneteau GT 36 (Baujahr 2021), 11,2 m Sportmotorboot
- Problem: Intermittierender Datenverlust — Tiefe, Geschwindigkeit und Motorparameter fallen sporadisch aus
- Bestehendes System: Simrad NSS12 evo3, NMEA-2000-Netzwerk mit Motor-Gateway, Echolot, Wind, GPS

**Diagnose (AYDI-Fehlerbild MFD-F04):**
1. MFD-Netzwerkdiagnose: 6 von 8 Geräten nur intermittierend sichtbar
2. Terminierung: Nur 1 Terminator statt 2 → sofort ergänzt
3. Visuell: Grünliche Korrosion an 2 T-Stücken im Maschinenraum (Kondenswasser)
4. Messung: Backbone-Widerstand schwankt bei Vibration → lockerer T-Stück-Kontakt identifiziert

**Behebung:**
- 2 korrodierte T-Stücke durch gel-gefüllte Marine-T-Stücke ersetzt (Ancor)
- Fehlenden Terminator ergänzt
- Drop-Cable des Motor-Gateways getauscht (Oxidation am Stecker)
- Alle Stecker mit ACF-50 Korrosionsschutz behandelt
- Kabelführung aus feuchtem Maschinenraum-Bereich in trockene Bilge umgelegt

**Ergebnis:**
- Gesamtkosten Reparatur: 180 EUR (Material) + 2h Arbeit
- Netzwerk stabil, alle 8 Geräte permanent sichtbar
- Problem bestand seit 18 Monaten — korrekte Diagnose löst es in 3 Stunden

**AYDI-Bewertung:**
- Fehlerklasse: MFD-F04 (NMEA-2000-Netzwerkausfall), Schweregrad 4
- Root Cause: Installation (fehlender Terminator) + Umgebung (Kondenswasser)
- Confidence: documented (Fehler reproduzierbar dokumentiert)

### ANHANG G — Fallstudie: Lagoon 42 — Katamaran-Doppelsteuerstand mit Raymarine

**Ausgangssituation:**
- Boot: Lagoon 42 (Baujahr 2023), 12,8 m Fahrtenkatamaran
- Anforderung: Doppelsteuerstand (BB + StB) mit synchronen Displays, Chartertauglichkeit
- Budget: 8.000 EUR

**Konfiguration:**
- Steuerstand BB: Raymarine Axiom 2 Pro 9" (1.499 EUR)
- Steuerstand StB: Raymarine Axiom 2 Pro 9" (1.499 EUR)
- Navigationstisch: Raymarine Axiom 2 Pro 9" (1.499 EUR)
- Autopilot: Raymarine Evolution EV-200 Hydraulik (1.899 EUR)
- AIS: Raymarine AIS700 Class-B+ (799 EUR)
- NMEA 2000: Backbone mit 6 T-Stücken (350 EUR)

**Besonderheiten:**
- 3 identische MFDs — minimaler Schulungsaufwand für wechselnde Charter-Crews
- Display-Synchronisation: Jedes MFD zeigt unabhängige Ansicht, aber teilt alle Daten
- ClearCruise AR auf Haupt-MFD (BB) aktiviert
- LightHouse Charts vorinstalliert — kein separates Kartenabo nötig

**Ergebnis:**
- Gesamtkosten: 7.545 EUR
- Charter-optimiertes System: einfach, redundant, identische Bedienung an jedem Steuerstand
- Raymarine-Vorteil: LightHouse Charts kostenlos vorinstalliert

**AYDI-Bewertung:**
- Ergonomie: 85/100 (3× 9" optimal verteilt auf Katamaran-Layout)
- Compliance: 88/100 (AIS, Autopilot, aktuelle Karten)
- Kosten: 80/100 (solides Preis-Leistungs-Verhältnis)
- Confidence: documented (Raymarine-Charterflotten-Konfiguration)

### ANHANG H — Fallstudie: Contest 57CS — Superyacht-Glasbrücke mit Simrad NSO Evo3S

**Ausgangssituation:**
- Boot: Contest 57CS (Baujahr 2025), 17,3 m Custom-Segelyacht
- Anforderung: Glasbrücken-Integration im geschlossenen Deckshaus, professionelle Navigation
- Budget: 45.000 EUR (Elektronik gesamt, ohne Kommunikation)

**Konfiguration:**
- Steuerstand: 2× Simrad NSO Evo3S 19" (2× 7.499 EUR)
- Navigationsecke: 1× Simrad NSO Evo3S 16" (4.999 EUR)
- Instrumente: 6× Simrad IS42 + AP44 Autopilot-Controller
- Radar: Simrad HALO 3000 Open Array (6.499 EUR)
- Echolot: Simrad S5100 CHIRP Module + ForwardScan (3.499 EUR)
- Autopilot: Simrad AP70 MK2 + RPU300 Hydraulik (5.999 EUR)
- AIS: Simrad AI70 Class-B+ (999 EUR)
- Wind/Logge: B&G H5000 CPU + Sensoren (2.999 EUR)
- GPS: Simrad HS75 GPS Compass (1.599 EUR)

**Besonderheiten:**
- Glasbrücke: Alle 3 NSO Evo3S vollständig synchronisiert
- B&G H5000 als Sailing-Prozessor parallel zu Simrad MFDs
- HALO 3000 Open Array: Regatta-taugliche Radar-Auflösung
- GPS-Kompass (HS75): Heading-Referenz ohne Magnetkompass-Fehler
- Dual-Ethernet-Backbone mit Managed Switch
- Expedition-PC als vierter Bildschirm am Navigationstisch

**Ergebnis:**
- Gesamtkosten: ca. 42.000 EUR
- Professionelle Glasbrücke auf Superyacht-Niveau
- Redundanz: Jedes MFD kann alle Funktionen übernehmen
- Hybride Nutzung: Simrad für Navigation, B&G H5000 für Segeldaten, Expedition für Routing

**AYDI-Bewertung:**
- Ergonomie: 95/100 (3 große Displays, perfekte Positionierung)
- Compliance: 98/100 (Radar, AIS, GPS-Kompass, ForwardScan, redundante Systeme)
- Kosten: 65/100 (Premiumpreis, aber Schiffsgröße rechtfertigt Investition)
- Confidence: measured (vollständige Systemdokumentation, Werftinstallation)

---

## ANHANG I–R — Pydantic v2 Modelle

Datenmodelle für die Kartenplotter/MFD-Analyse im AYDI-System. Alle Modelle verwenden Pydantic v2 mit `model_config = {"from_attributes": True}`.

```python
"""
AYDI MFD / Chartplotter Analysis Models — Pydantic v2
Wissensdatei: 23.02 Kartenplotter und MFD
"""

from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


# --- ANHANG I: Enums ---


class MfdManufacturer(str, Enum):
    """Hersteller von Kartenplottern und MFDs."""
    RAYMARINE = "raymarine"
    GARMIN = "garmin"
    SIMRAD = "simrad"
    BG = "bg"
    FURUNO = "furuno"
    HUMMINBIRD = "humminbird"
    LOWRANCE = "lowrance"
    OTHER = "other"
    UNKNOWN = "unknown"


class MfdCategory(str, Enum):
    """MFD-Kategorie nach Displaygröße und Funktionsumfang."""
    ENTRY_LEVEL = "entry_level"          # 7", Basisnavigation
    MID_RANGE = "mid_range"              # 9-12", volle Netzwerkfähigkeit
    HIGH_END = "high_end"                # 16"+, Glasbrücke
    BLACKBOX = "blackbox"                # Prozessor ohne Display
    INSTRUMENT = "instrument"            # Dediziertes Instrumentendisplay


class DisplayTechnology(str, Enum):
    """Displaytechnologie des MFD."""
    TFT_TN = "tft_tn"
    TFT_VA = "tft_va"
    IPS = "ips"
    IPS_BONDED = "ips_bonded"
    OLED = "oled"


class TouchscreenType(str, Enum):
    """Touchscreen-Technologie."""
    CAPACITIVE = "capacitive"
    RESISTIVE = "resistive"
    NONE = "none"


class CartographyProvider(str, Enum):
    """Kartenanbieter."""
    CMAP = "cmap"
    NAVIONICS = "navionics"
    BLUECHART = "bluechart"
    TZ_MAPS = "tz_maps"
    ENC_S57 = "enc_s57"
    OPENCPN = "opencpn"
    OTHER = "other"


class NetworkProtocol(str, Enum):
    """Netzwerkprotokoll."""
    NMEA_2000 = "nmea_2000"
    NMEA_0183 = "nmea_0183"
    ETHERNET = "ethernet"
    WIFI = "wifi"
    BLUETOOTH = "bluetooth"
    SEATALKNG = "seatalkng"
    SIMNET = "simnet"
    GARMIN_MARINE = "garmin_marine"
    FURUNO_CAN = "furuno_can"


class GnssSystem(str, Enum):
    """GNSS-Satellitennavigationssystem."""
    GPS = "gps"
    GLONASS = "glonass"
    GALILEO = "galileo"
    BEIDOU = "beidou"


class EcholotType(str, Enum):
    """Echolot-Technologie."""
    STANDARD = "standard"
    DUAL_FREQ = "dual_frequency"
    CHIRP = "chirp"
    DOWNSCAN = "downscan"
    SIDESCAN = "sidescan"
    FORWARDSCAN = "forwardscan"
    REALVISION_3D = "realvision_3d"
    MULTIBEAM = "multibeam"


class MountingType(str, Enum):
    """Montageart des MFD."""
    FLUSH_MOUNT = "flush_mount"
    BRACKET_MOUNT = "bracket_mount"
    TRUNNION = "trunnion"
    SURFACE_MOUNT = "surface_mount"


class ConfidenceLevel(str, Enum):
    """Konfidenz-Stufe der Analyse."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class SeverityLevel(int, Enum):
    """Schweregrad-Stufe (1-5)."""
    COSMETIC = 1
    MINOR = 2
    MODERATE = 3
    SIGNIFICANT = 4
    CRITICAL = 5


class FailurePatternCode(str, Enum):
    """Fehlerbild-Codes gemaess Fehlerbild-Atlas."""
    F01_DISPLAY_DELAMINATION = "MFD-F01"
    F02_GHOST_TOUCHES = "MFD-F02"
    F03_GPS_MULTIPATH = "MFD-F03"
    F04_NMEA_NETWORK_FAILURE = "MFD-F04"
    F05_RADAR_OVERLAY_OFFSET = "MFD-F05"
    F06_ECHOLOT_AIR_BUBBLES = "MFD-F06"
    F07_SOFTWARE_FREEZE = "MFD-F07"
    F08_CONNECTOR_CORROSION = "MFD-F08"
    F09_BACKLIGHT_FAILURE = "MFD-F09"
    F10_CHART_DATA_OUTDATED = "MFD-F10"
    F11_THERMAL_THROTTLING = "MFD-F11"
    F12_WATER_INGRESS_SEAL = "MFD-F12"


class InstallationLocation(str, Enum):
    """Einbauort des MFD auf der Yacht."""
    COCKPIT_PEDESTAL = "cockpit_pedestal"
    COCKPIT_CONSOLE = "cockpit_console"
    FLYBRIDGE = "flybridge"
    NAV_STATION = "nav_station"
    SALON = "salon"
    HELM_INTERNAL = "helm_internal"
    MAST = "mast"


# --- ANHANG J: MFD-Spezifikation ---


class MfdDisplaySpec(BaseModel):
    """Displayspezifikation eines MFD."""
    model_config = {"from_attributes": True}

    size_inches: float = Field(
        ..., ge=5.0, le=32.0,
        description="Displaydiagonale in Zoll"
    )
    resolution_x: int = Field(
        ..., ge=480, le=3840,
        description="Horizontale Aufloesung in Pixeln"
    )
    resolution_y: int = Field(
        ..., ge=320, le=2160,
        description="Vertikale Aufloesung in Pixeln"
    )
    technology: DisplayTechnology = Field(
        ..., description="Displaytechnologie (IPS, TFT, etc.)"
    )
    brightness_nits_typical: int = Field(
        ..., ge=100, le=5000,
        description="Typische Helligkeit in Nits (cd/m2)"
    )
    brightness_nits_max: int = Field(
        ..., ge=100, le=5000,
        description="Maximale Helligkeit in Nits (cd/m2)"
    )
    optical_bonding: bool = Field(
        default=False,
        description="Optisches Bonding vorhanden"
    )
    touchscreen: TouchscreenType = Field(
        default=TouchscreenType.CAPACITIVE,
        description="Touchscreen-Typ"
    )
    anti_glare: bool = Field(
        default=True,
        description="Anti-Glare-Beschichtung vorhanden"
    )


class MfdNetworkSpec(BaseModel):
    """Netzwerkspezifikation eines MFD."""
    model_config = {"from_attributes": True}

    nmea_2000_ports: int = Field(
        default=0, ge=0, le=4,
        description="Anzahl NMEA-2000-Anschluesse"
    )
    nmea_0183_ports: int = Field(
        default=0, ge=0, le=4,
        description="Anzahl NMEA-0183-Anschluesse"
    )
    ethernet_ports: int = Field(
        default=0, ge=0, le=4,
        description="Anzahl Ethernet-Anschluesse"
    )
    wifi_standard: Optional[str] = Field(
        default=None,
        description="Wi-Fi-Standard (z.B. '802.11ac')"
    )
    bluetooth_version: Optional[str] = Field(
        default=None,
        description="Bluetooth-Version (z.B. '5.0 LE')"
    )
    hdmi_in: bool = Field(
        default=False,
        description="HDMI-Eingang vorhanden"
    )
    usb_ports: int = Field(
        default=0, ge=0, le=4,
        description="Anzahl USB-Anschluesse"
    )


class MfdGnssSpec(BaseModel):
    """GNSS-Spezifikation eines MFD."""
    model_config = {"from_attributes": True}

    internal_receiver: bool = Field(
        default=True,
        description="Interner GPS-Empfaenger vorhanden"
    )
    gnss_systems: list[GnssSystem] = Field(
        default_factory=lambda: [GnssSystem.GPS, GnssSystem.GLONASS],
        description="Unterstuetzte GNSS-Systeme"
    )
    update_rate_hz: int = Field(
        default=1, ge=1, le=20,
        description="GPS-Update-Rate in Hz"
    )
    waas_egnos: bool = Field(
        default=True,
        description="WAAS/EGNOS-Korrektur unterstuetzt"
    )
    external_antenna_recommended: bool = Field(
        default=False,
        description="Externe GPS-Antenne empfohlen"
    )


class MfdSpec(BaseModel):
    """Vollstaendige technische Spezifikation eines MFD/Kartenplotters."""
    model_config = {"from_attributes": True}

    manufacturer: MfdManufacturer
    model_name: str = Field(
        ..., description="Modellbezeichnung, z.B. 'Axiom 2 Pro 9'"
    )
    category: MfdCategory
    display: MfdDisplaySpec
    network: MfdNetworkSpec
    gnss: MfdGnssSpec
    operating_system: str = Field(
        ..., description="Betriebssystem, z.B. 'LightHouse 4'"
    )
    cartography_providers: list[CartographyProvider] = Field(
        default_factory=list,
        description="Kompatible Kartenanbieter"
    )
    echolot_types: list[EcholotType] = Field(
        default_factory=list,
        description="Unterstuetzte Echolot-Technologien"
    )
    radar_capable: bool = Field(
        default=False,
        description="Radar-Integration moeglich"
    )
    autopilot_control: bool = Field(
        default=False,
        description="Autopilot-Steuerung moeglich"
    )
    sailing_features: bool = Field(
        default=False,
        description="Dedizierte Segelfunktionen (SailSteer, Laylines)"
    )
    forwardscan_capable: bool = Field(
        default=False,
        description="ForwardScan-Integration moeglich"
    )
    power_consumption_w_typical: float = Field(
        ..., ge=1.0, le=100.0,
        description="Typischer Stromverbrauch in Watt"
    )
    power_consumption_w_max: float = Field(
        ..., ge=1.0, le=150.0,
        description="Maximaler Stromverbrauch in Watt"
    )
    voltage_range_v: str = Field(
        default="10-32",
        description="Eingangsspannungsbereich in Volt"
    )
    ip_rating: str = Field(
        ..., description="Schutzart, z.B. 'IP67' oder 'IPX7'"
    )
    operating_temp_min_c: int = Field(
        default=-15, ge=-30, le=0,
        description="Minimale Betriebstemperatur in Grad Celsius"
    )
    operating_temp_max_c: int = Field(
        default=55, ge=40, le=70,
        description="Maximale Betriebstemperatur in Grad Celsius"
    )
    width_mm: float = Field(
        ..., ge=50.0, le=700.0,
        description="Geraetebreite in mm"
    )
    height_mm: float = Field(
        ..., ge=50.0, le=500.0,
        description="Geraetehoehe in mm"
    )
    depth_mm: float = Field(
        ..., ge=20.0, le=200.0,
        description="Geraetetiefe in mm"
    )
    weight_kg: float = Field(
        ..., ge=0.2, le=15.0,
        description="Gewicht in kg"
    )
    price_eur: Optional[float] = Field(
        default=None, ge=0.0,
        description="UVP in EUR"
    )
    release_year: Optional[int] = Field(
        default=None, ge=2000, le=2030,
        description="Markteinfuehrungsjahr"
    )
    warranty_years: int = Field(
        default=2, ge=1, le=5,
        description="Garantiedauer in Jahren"
    )


# --- ANHANG K: Installationsbewertung ---


class MfdInstallation(BaseModel):
    """Bewertung einer MFD-Installation auf einer Yacht."""
    model_config = {"from_attributes": True}

    mfd_spec: MfdSpec
    location: InstallationLocation
    mounting: MountingType
    cutout_width_mm: Optional[float] = Field(
        default=None, ge=100.0, le=600.0,
        description="Ausschnittbreite in mm (nur Flush-Mount)"
    )
    cutout_height_mm: Optional[float] = Field(
        default=None, ge=80.0, le=400.0,
        description="Ausschnitthoehe in mm (nur Flush-Mount)"
    )
    ventilation_gap_mm: Optional[float] = Field(
        default=None, ge=0.0, le=100.0,
        description="Freiraum hinter MFD fuer Belueftung in mm"
    )
    compass_safe_distance_mm: Optional[float] = Field(
        default=None, ge=0.0, le=2000.0,
        description="Abstand zum Magnetkompass in mm"
    )
    sun_exposure: str = Field(
        default="partial",
        description="Sonnenexposition: 'full', 'partial', 'shaded'"
    )
    spray_exposure: str = Field(
        default="moderate",
        description="Spritzwasserexposition: 'heavy', 'moderate', 'light', 'none'"
    )
    viewing_angle_standing_deg: Optional[float] = Field(
        default=None, ge=-90.0, le=90.0,
        description="Blickwinkel im Stehen in Grad (0 = frontal)"
    )
    viewing_angle_seated_deg: Optional[float] = Field(
        default=None, ge=-90.0, le=90.0,
        description="Blickwinkel im Sitzen in Grad (0 = frontal)"
    )
    external_gps_installed: bool = Field(
        default=False,
        description="Externe GPS-Antenne installiert"
    )
    remote_control_installed: bool = Field(
        default=False,
        description="Fernbedienung installiert"
    )
    sun_cover_present: bool = Field(
        default=False,
        description="Sonnenschutzabdeckung vorhanden"
    )


# --- ANHANG L: Netzwerkbewertung ---


class Nmea2000NetworkAssessment(BaseModel):
    """Bewertung eines NMEA-2000-Netzwerks."""
    model_config = {"from_attributes": True}

    backbone_length_m: float = Field(
        ..., ge=0.0, le=150.0,
        description="Backbone-Laenge in Metern"
    )
    device_count: int = Field(
        ..., ge=1, le=80,
        description="Anzahl angeschlossener Geraete"
    )
    total_len: float = Field(
        ..., ge=0.0, le=100.0,
        description="Gesamte LEN (Load Equivalency Number) des Netzwerks"
    )
    terminator_count: int = Field(
        ..., ge=0, le=4,
        description="Anzahl Terminierungswiderstaende"
    )
    connector_type: str = Field(
        default="micro_c",
        description="Steckertyp: 'micro_c', 'mini_c', 'devicenet'"
    )
    gel_filled_connectors: bool = Field(
        default=False,
        description="Gel-gefuellte Stecker verwendet"
    )
    backbone_routing_dry: bool = Field(
        default=True,
        description="Backbone in trockener Umgebung verlegt"
    )
    drop_cable_max_length_m: float = Field(
        default=6.0, ge=0.0, le=10.0,
        description="Laengste Drop-Cable-Verbindung in Metern"
    )
    power_supply_location: str = Field(
        default="central",
        description="Stromeinspeisung: 'central', 'distributed'"
    )
    shielded_cable: bool = Field(
        default=False,
        description="Geschirmtes NMEA-2000-Kabel verwendet"
    )

    @property
    def is_backbone_length_compliant(self) -> bool:
        """Backbone-Laenge innerhalb der NMEA-2000-Spezifikation."""
        return self.backbone_length_m <= 100.0

    @property
    def is_termination_correct(self) -> bool:
        """Korrekte Terminierung: genau 2 Widerstaende."""
        return self.terminator_count == 2

    @property
    def is_bus_load_compliant(self) -> bool:
        """Buslast innerhalb der Spezifikation (max. 50 LEN)."""
        return self.total_len <= 50.0

    @property
    def is_drop_cable_compliant(self) -> bool:
        """Drop-Cable-Laenge innerhalb der Spezifikation (max. 6 m)."""
        return self.drop_cable_max_length_m <= 6.0


# --- ANHANG M: Fehlerbild-Modell ---


class MfdFailurePattern(BaseModel):
    """Dokumentiertes Fehlerbild eines MFD/Kartenplotters."""
    model_config = {"from_attributes": True}

    code: FailurePatternCode
    severity: SeverityLevel
    affected_manufacturer: Optional[MfdManufacturer] = Field(
        default=None,
        description="Betroffener Hersteller (None = herstelleruebergreifend)"
    )
    affected_model: Optional[str] = Field(
        default=None,
        description="Betroffenes Modell (None = modelluebergreifend)"
    )
    description_de: str = Field(
        ..., description="Beschreibung des Fehlerbilds auf Deutsch"
    )
    root_cause: str = Field(
        ..., description="Ursache des Fehlers"
    )
    visual_indicators: list[str] = Field(
        default_factory=list,
        description="Visuell erkennbare Merkmale"
    )
    repair_action: str = Field(
        ..., description="Empfohlene Reparaturmaßnahme"
    )
    prevention: str = Field(
        ..., description="Praeventive Massnahme"
    )
    estimated_repair_cost_eur_min: float = Field(
        ..., ge=0.0,
        description="Geschaetzte Reparaturkosten Minimum in EUR"
    )
    estimated_repair_cost_eur_max: float = Field(
        ..., ge=0.0,
        description="Geschaetzte Reparaturkosten Maximum in EUR"
    )
    frequency_percent: float = Field(
        ..., ge=0.0, le=100.0,
        description="Haeufigkeit in Prozent der installierten Basis"
    )
    confidence: ConfidenceLevel = Field(
        default=ConfidenceLevel.DOCUMENTED,
        description="Konfidenz-Stufe der Fehlerbild-Daten"
    )


# --- ANHANG N: Analyse-Ergebnis ---


class MfdAnalysisResult(BaseModel):
    """Ergebnis der MFD/Kartenplotter-Analyse fuer ein Modul."""
    model_config = {"from_attributes": True}

    yacht_id: str = Field(
        ..., description="Eindeutige Yacht-ID im AYDI-System"
    )
    zone: str = Field(
        ..., description="Zone der Yacht (z.B. 'cockpit', 'nav_station', 'flybridge')"
    )
    mfd_installations: list[MfdInstallation] = Field(
        default_factory=list,
        description="Liste aller MFD-Installationen in dieser Zone"
    )
    network_assessment: Optional[Nmea2000NetworkAssessment] = Field(
        default=None,
        description="Bewertung des NMEA-2000-Netzwerks"
    )
    detected_failures: list[MfdFailurePattern] = Field(
        default_factory=list,
        description="Erkannte Fehlerbilder"
    )
    score_display_quality: float = Field(
        ..., ge=0.0, le=100.0,
        description="Bewertung der Display-Qualitaet (0-100)"
    )
    score_network_integrity: float = Field(
        ..., ge=0.0, le=100.0,
        description="Bewertung der Netzwerk-Integritaet (0-100)"
    )
    score_redundancy: float = Field(
        ..., ge=0.0, le=100.0,
        description="Bewertung der Systemredundanz (0-100)"
    )
    score_ergonomics: float = Field(
        ..., ge=0.0, le=100.0,
        description="Bewertung der ergonomischen Positionierung (0-100)"
    )
    score_overall: float = Field(
        ..., ge=0.0, le=100.0,
        description="Gesamtbewertung (0-100)"
    )
    confidence: ConfidenceLevel
    findings_de: list[str] = Field(
        default_factory=list,
        description="Befunde auf Deutsch"
    )
    suggestions_de: list[str] = Field(
        default_factory=list,
        description="Verbesserungsvorschlaege auf Deutsch"
    )
    analysis_date: date = Field(
        ..., description="Datum der Analyse"
    )
    ai_model_version: str = Field(
        ..., description="Version des verwendeten KI-Modells"
    )


# --- ANHANG O: Kartenplotter-Vergleich ---


class MfdComparison(BaseModel):
    """Vergleich mehrerer MFDs fuer eine Kaufempfehlung."""
    model_config = {"from_attributes": True}

    yacht_type: str = Field(
        ..., description="Yacht-Typ (z.B. 'segelyacht_12m', 'motoryacht_15m')"
    )
    use_case: str = Field(
        ..., description="Einsatzzweck (z.B. 'kuestennavigation', 'blauwasser', 'regatta')"
    )
    budget_eur: Optional[float] = Field(
        default=None, ge=0.0,
        description="Budget in EUR"
    )
    candidates: list[MfdSpec] = Field(
        ..., min_length=2,
        description="MFD-Kandidaten fuer den Vergleich (mind. 2)"
    )
    recommended_model: str = Field(
        ..., description="Empfohlenes Modell"
    )
    recommendation_reason_de: str = Field(
        ..., description="Begruendung der Empfehlung auf Deutsch"
    )
    score_per_candidate: dict[str, float] = Field(
        default_factory=dict,
        description="Score pro Kandidat (model_name -> Score 0-100)"
    )
    confidence: ConfidenceLevel = Field(
        default=ConfidenceLevel.ESTIMATED,
        description="Konfidenz der Empfehlung"
    )


# --- ANHANG P: Hersteller-Referenz ---


class MfdManufacturerInfo(BaseModel):
    """Hersteller-Informationen fuer die MFD-Datenbank."""
    model_config = {"from_attributes": True}

    manufacturer: MfdManufacturer
    full_name: str = Field(
        ..., description="Vollstaendiger Firmenname"
    )
    founded_year: int = Field(
        ..., ge=1900, le=2030,
        description="Gruendungsjahr"
    )
    headquarters_country: str = Field(
        ..., description="Land des Hauptsitzes"
    )
    parent_company: Optional[str] = Field(
        default=None,
        description="Muttergesellschaft (falls vorhanden)"
    )
    market_share_percent: Optional[float] = Field(
        default=None, ge=0.0, le=100.0,
        description="Geschaetzter Marktanteil in Prozent"
    )
    operating_system: str = Field(
        ..., description="Betriebssystem der MFDs"
    )
    primary_cartography: CartographyProvider = Field(
        ..., description="Primaerer Kartenanbieter"
    )
    warranty_years_standard: int = Field(
        default=2, ge=1, le=5,
        description="Standard-Garantiedauer in Jahren"
    )
    service_network_size: Optional[int] = Field(
        default=None, ge=0,
        description="Ungefaehre Anzahl Haendler/Servicepartner weltweit"
    )
    website: str = Field(
        ..., description="Website-URL"
    )
    strengths_de: list[str] = Field(
        default_factory=list,
        description="Staerken auf Deutsch"
    )
    weaknesses_de: list[str] = Field(
        default_factory=list,
        description="Schwaechen auf Deutsch"
    )


# --- ANHANG Q: Karten-Abonnement ---


class CartographySubscription(BaseModel):
    """Karten-Abonnement-Information."""
    model_config = {"from_attributes": True}

    provider: CartographyProvider
    tier_name: str = Field(
        ..., description="Abo-Stufe, z.B. 'Navionics+', 'C-MAP Discover X'"
    )
    annual_cost_eur: float = Field(
        ..., ge=0.0,
        description="Jaehrliche Kosten in EUR"
    )
    coverage_region: str = Field(
        ..., description="Abgedeckte Region, z.B. 'Europa', 'Mittelmeer', 'Weltweit'"
    )
    includes_bathymetry: bool = Field(
        default=False,
        description="Bathymetrie-Daten enthalten"
    )
    includes_satellite_overlay: bool = Field(
        default=False,
        description="Satellitenbilder-Overlay enthalten"
    )
    auto_update: bool = Field(
        default=True,
        description="Automatische Updates ueber Wi-Fi"
    )
    community_data: bool = Field(
        default=False,
        description="Community-basierte Daten enthalten (z.B. SonarChart)"
    )
    compatible_manufacturers: list[MfdManufacturer] = Field(
        default_factory=list,
        description="Kompatible MFD-Hersteller"
    )


# --- ANHANG R: Service-Empfehlung ---


class MfdServiceRecommendation(BaseModel):
    """Service-Empfehlung fuer ein MFD-System."""
    model_config = {"from_attributes": True}

    yacht_id: str = Field(
        ..., description="Eindeutige Yacht-ID im AYDI-System"
    )
    mfd_model: str = Field(
        ..., description="MFD-Modellbezeichnung"
    )
    mfd_age_years: float = Field(
        ..., ge=0.0, le=30.0,
        description="Alter des MFD in Jahren"
    )
    firmware_current: bool = Field(
        ..., description="Firmware auf aktuellem Stand"
    )
    firmware_version: Optional[str] = Field(
        default=None,
        description="Aktuelle Firmware-Version"
    )
    charts_current: bool = Field(
        ..., description="Kartenmaterial auf aktuellem Stand"
    )
    chart_subscription_active: bool = Field(
        ..., description="Karten-Abonnement aktiv"
    )
    detected_issues: list[FailurePatternCode] = Field(
        default_factory=list,
        description="Erkannte Fehlerbilder"
    )
    service_actions_de: list[str] = Field(
        default_factory=list,
        description="Empfohlene Service-Aktionen auf Deutsch"
    )
    estimated_service_cost_eur: float = Field(
        ..., ge=0.0,
        description="Geschaetzte Service-Kosten in EUR"
    )
    replacement_recommended: bool = Field(
        default=False,
        description="Geraetetausch empfohlen (statt Reparatur)"
    )
    replacement_model_suggestion: Optional[str] = Field(
        default=None,
        description="Vorgeschlagenes Ersatzmodell"
    )
    replacement_estimated_cost_eur: Optional[float] = Field(
        default=None, ge=0.0,
        description="Geschaetzte Kosten fuer Ersatzgeraet in EUR"
    )
    urgency: SeverityLevel = Field(
        default=SeverityLevel.MINOR,
        description="Dringlichkeit der Service-Empfehlung"
    )
    confidence: ConfidenceLevel = Field(
        default=ConfidenceLevel.ESTIMATED,
        description="Konfidenz der Service-Empfehlung"
    )
    next_service_date: Optional[date] = Field(
        default=None,
        description="Empfohlenes naechstes Service-Datum"
    )
```

---

**Ende der Wissensdatei 23.02 — Kartenplotter und MFD**

> AYDI Wissensdatei 23.02 | Version 1.0.0 | 2026-05-08 | Status: validated
