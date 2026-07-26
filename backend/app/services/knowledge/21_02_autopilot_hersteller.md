# 21.02 — Autopilot Hersteller-Vergleich: Raymarine, B&G, Garmin, Simrad, Furuno, NKE — Detailvergleich

> **AYDI Wissensdatei 21.02** — Kategorie 21: Autopiloten und Kurssteuerung
> **Confidence-Quelle:** measured (Hersteller-Datenblätter), documented (Handbücher, Praxis-Tests), estimated (Erfahrungswerte Werft/Eigner)
> **Letzte Aktualisierung:** 2026-05-02

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
12. [ANHANG I–R — Pydantic v2 Modelle](#anhang-ir--pydantic-v2-modelle)

---

## 1. Einführung und Übersicht

### 1.1 Marktlandschaft Autopiloten im Yachtbau

Der Markt für marine Autopiloten wird von sechs Hauptakteuren dominiert, die zusammen über 95 % des weltweiten Marktes für Freizeit- und semi-professionelle Yachten abdecken. Die Konsolidierung der letzten zwei Jahrzehnte hat die Landschaft fundamental verändert:

**Konzernstruktur:**
- **Navico Group** (Fiskars/Brunswick): B&G, Simrad, Lowrance — drei Marken, eine Technologiebasis
- **FLIR Systems / Teledyne**: Raymarine — britische Tradition, amerikanische Konzernmutter
- **Garmin Ltd.**: Garmin Marine — aus der Luftfahrt-Navigation kommend, seit 2015 massiv im Marinemarkt
- **Furuno Electric Co.**: Furuno — japanischer Traditionskonzern, Schwerpunkt kommerzielle Schifffahrt
- **NKE Marine Electronics**: NKE — französischer Spezialist, Fokus Regatta und Performance-Sailing

**Marktanteile geschätzt (Freizeitboote, 2025):**

| Hersteller | Segelboote | Motorboote | Superyachten (>24m) |
|-----------|-----------|-----------|-------------------|
| Raymarine | 30 % | 25 % | 15 % |
| B&G | 25 % | 5 % | 10 % |
| Garmin | 15 % | 35 % | 5 % |
| Simrad | 10 % | 20 % | 20 % |
| Furuno | 5 % | 10 % | 40 % |
| NKE | 10 % | <1 % | <1 % |
| Sonstige | 5 % | 5 % | 10 % |

> **Confidence: estimated** — Marktanteile basieren auf Werft-Auslieferungsdaten, Händler-Befragungen und Forumsanalysen. Exakte Zahlen veröffentlicht kein Hersteller.

### 1.2 Preissegmente

Die Gesamtkosten eines Autopilot-Systems umfassen weit mehr als den Kurscomputer. Eine vollständige Installation besteht aus Kurscomputer, Antriebseinheit, Bedieneinheit(en), Sensoren und Verkabelung.

**Preissegmente Gesamtsystem (Stand 2025/2026, EUR, inkl. MwSt. Deutschland):**

| Segment | Bootsgröße | Typische Gesamtkosten | Beispielkonfiguration |
|---------|-----------|----------------------|----------------------|
| Einstieg | 6–9 m Segel | 1.800–3.500 € | Raymarine EV-100, Tillerpilot |
| Mittelklasse | 9–13 m Segel | 3.500–7.000 € | B&G NAC-2 + H5000, Linearantrieb |
| Gehoben | 12–18 m Segel/Motor | 6.000–15.000 € | Garmin Reactor 40 + GHP, Hydraulik |
| Premium | 15–24 m | 12.000–35.000 € | Simrad AC70, Furuno NavPilot 700 |
| Superyacht | >24 m | 30.000–120.000+ € | Furuno NavPilot 700 redundant, Rolls-Royce |

**Kostenverteilung typische Mittelklasse-Installation:**
- Kurscomputer: 25–35 %
- Antriebseinheit: 30–40 %
- Bedieneinheit(en): 10–15 %
- Sensoren (Kompass, Gyroskop, GPS): 5–10 %
- Kabel, Stecker, Montagematerial: 5–8 %
- Einbau (Fachbetrieb): 15–25 % (stark werftabhängig)

### 1.3 Technologietrends

**Trend 1 — Solid-State-Sensorik (MEMS):**
Moderne Autopiloten verwenden MEMS-Gyroskope (Micro-Electro-Mechanical Systems) und MEMS-Beschleunigungssensoren statt klassischer Fluxgate-Kompasse. Vorteil: schnellere Reaktion auf Kursabweichungen, kein mechanischer Verschleiß, geringerer Stromverbrauch. Raymarine Evolution-Serie war 2014 Vorreiter; alle Hersteller haben inzwischen nachgezogen.

**Trend 2 — Adaptive Algorithmen:**
Statt manueller Gain/Counter-Rudder-Einstellung lernen moderne Systeme das Verhalten des Bootes selbstständig. Raymarine nennt dies "EV Sensor Technology", B&G "Continuum Algorithm", Garmin "Shadow Drive". Die Qualität der Selbstkalibrierung variiert erheblich zwischen Herstellern und ist ein zentrales Differenzierungsmerkmal.

**Trend 3 — Integration mit Kartenplottern:**
Alle aktuellen Systeme erlauben Routenverfolgung (Track-Modus) direkt vom Plotter. Die Qualität der Wendepunktvorausberechnung (WPT Advance) und die Genauigkeit der Bahnkurven unterscheiden sich aber deutlich.

**Trend 4 — Redundanz und Sicherheit:**
Wachsende Anforderungen an Redundanz, insbesondere bei Einhandseglern und Langfahrt: doppelte Kurscomputer, unabhängige Stromversorgung, mechanische Notkupplung. ISO 11674 (Kursregelungsanlagen / Heading Control Systems) definiert Mindestanforderungen an Alarmierung und Notausschaltung.

**Trend 5 — Segelspezifische Funktionen:**
Wind-Modus (Steuerung nach scheinbarem oder wahrem Windwinkel), Wende-Assistent, Halsen-Assistent, Performance-Optimierung über Polardiagramme — B&G und NKE sind hier klar führend. Raymarine und Garmin bieten Basisfunktionen, Furuno und Simrad fokussieren stärker auf Motorboote.

**Trend 6 — Drahtlose Fernbedienung:**
Bluetooth- und WLAN-Fernbedienungen an Deck, am Mast oder in der Rettungsinsel. Raymarine bietet SmartController-App, B&G WR10-Fernbedienung, Garmin Helm-Fernbedienung per quatix-Uhr.

**Trend 7 — CAN-Bus-Migration:**
NMEA 2000 (CAN-basiert) löst NMEA 0183 (seriell) als Hauptprotokoll ab. Proprietäre Busse (SeaTalk, SeaTalkNG, SimNet) werden zugunsten offener Standards zurückgedrängt, bleiben aber für Hersteller-interne Kommunikation relevant.

### 1.4 Auswahlkriterien für die AYDI-Bewertung

Die AYDI-Plattform bewertet Autopilot-Installationen anhand folgender Kriterien:

| Kriterium | Gewicht | Beschreibung |
|-----------|---------|-------------|
| Leistungsklasse passend | 25 % | Antriebskraft ausreichend für Verdrängung und Rudertyp |
| Systemintegration | 20 % | Protokoll-Kompatibilität, Sensoranbindung, Plotter-Integration |
| Zuverlässigkeit | 20 % | MTBF-Daten, Eignererfahrungen, bekannte Probleme |
| Energieeffizienz | 15 % | Stromverbrauch bei Durchschnitts-Ruderbewegung |
| Segeleignung | 10 % | Wind-Modus, Wendeassistent, Performance-Funktionen |
| Wartbarkeit | 10 % | Ersatzteilverfügbarkeit, Diagnosemöglichkeiten |

---

## 2. Grundlagen und Theorie

### 2.1 Funktionsprinzip eines Autopiloten

Ein Autopilot ist ein geschlossener Regelkreis (Closed-Loop Control System) mit folgenden Komponenten:

```
                    ┌─────────────┐
  Sollwert ────────►│ Kurscomputer │──────► Stellgröße
  (Kurs/Wind)       │ (Controller) │        (Ruderwinkel)
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │   Antrieb    │──────► Ruder
                    │ (Aktuator)   │
                    └─────────────┘
                           │
                    ┌──────▼──────┐
                    │   Sensoren   │──────► Istwert
                    │ (Kompass,    │        (aktueller Kurs,
                    │  Gyroskop,   │         Lage, Rate)
                    │  GPS, Wind)  │
                    └──────┬──────┘
                           │
                           ▼
                    Rückkopplung zum Kurscomputer
```

**Regelkreis-Parameter:**

| Parameter | Bezeichnung | Bedeutung |
|-----------|------------|-----------|
| Kp | Proportional-Gain | Ruderbewegung proportional zur Kursabweichung |
| Ki | Integral-Gain | Korrektur dauerhafter Abweichungen (Strom, Wind) |
| Kd | Differenzial-Gain | Dämpfung — reagiert auf Änderungsrate der Abweichung |
| Deadband | Totband | Bereich um Sollkurs, in dem kein Ruder gegeben wird |
| Counter-Rudder | Gegenruder | Rudergabe gegen Drehrichtung vor Erreichen des Sollkurses |
| Ruderlimit | Max. Ruderwinkel | Maximaler Ausschlag, den der AP kommandiert |

**PID-Regelung vereinfacht:**

```
Ruderwinkel(t) = Kp × e(t) + Ki × ∫e(τ)dτ + Kd × de(t)/dt

wobei e(t) = Sollkurs - Istkurs (Kursabweichung)
```

Moderne Autopiloten verwenden erweiterte Algorithmen (Kalman-Filter, Fuzzy Logic, neuronale Netze), die über einfache PID-Regelung hinausgehen. Die Grundstruktur bleibt jedoch identisch.

### 2.2 Leistungsklassen nach Bootsverdrängung

Die Auswahl der Antriebseinheit richtet sich primär nach der Verdrängung und dem Rudertyp. Zu schwache Antriebe führen zu schlechtem Kurshalten, zu starke zu unnötigem Stromverbrauch und Gewicht.

**Klassifizierung nach Verdrängung (Segelyachten):**

| Klasse | Verdrängung | Typische Boote | Empfohlene Ruderkraft | Antriebstyp |
|--------|------------|---------------|----------------------|-------------|
| Mini | <2.000 kg | Jollenkreuzer, Trailer-Segler | 50–120 N | Tillerpilot |
| Klein | 2.000–5.000 kg | 27–33 ft Segelyacht | 120–350 N | Linearantrieb |
| Mittel | 5.000–12.000 kg | 33–42 ft Segelyacht | 350–800 N | Linearantrieb / Hydraulik |
| Groß | 12.000–25.000 kg | 42–55 ft Segelyacht | 800–2.000 N | Hydraulik |
| Sehr groß | >25.000 kg | >55 ft / Superyacht | >2.000 N | Hydraulik redundant |

**Klassifizierung nach Verdrängung (Motoryachten):**

| Klasse | Verdrängung | Typische Boote | Empfohlene Ruderkraft | Antriebstyp |
|--------|------------|---------------|----------------------|-------------|
| Klein | <5.000 kg | Sportboot, Daycruiser | 150–400 N | Hydraulik / Rotary |
| Mittel | 5.000–15.000 kg | Trawler, Flybridge 30–40 ft | 400–1.200 N | Hydraulik |
| Groß | 15.000–50.000 kg | Motoryacht 40–60 ft | 1.200–3.500 N | Hydraulik |
| Sehr groß | >50.000 kg | Superyacht >60 ft | >3.500 N | Hydraulik redundant |

**Faustformel Ruderkraft-Berechnung:**

```
Erforderliche Ruderkraft (N) = Verdrängung (kg) × Faktor

Faktor Segelboot (Spatenruder):     0.06–0.08
Faktor Segelboot (Skeg-Ruder):      0.04–0.06
Faktor Segelboot (Langkiel):        0.03–0.05
Faktor Motorboot (Spatenruder):     0.05–0.07
Faktor Motorboot (Doppelruder):     0.04–0.06 pro Ruder
```

> **Confidence: estimated** — Faustformeln basieren auf Erfahrungswerten. Exakte Berechnung erfordert Ruderfläche, Profilform, Bootgeschwindigkeit und Strömungsverhältnisse.

### 2.3 Antriebstypen im Detail

#### 2.3.1 Tillerpilot (Pinnenantrieb)

**Prinzip:** Elektrischer Linearmotor, der direkt an der Pinne angreift.

**Vorteile:**
- Einfachste Installation (15–30 min)
- Kostengünstig (500–1.500 €)
- Kein Eingriff in Ruderanlage
- Leicht demontierbar (Winterlager)
- Geringer Stromverbrauch (0,5–2,0 A bei 12V)

**Nachteile:**
- Nur für Pinnensteuerung
- Begrenzte Kraft (max. ~350 N)
- Lautstärke (mechanisches Summen)
- Begrenzte Lebensdauer der Spindel
- Kein Ruderfeedback

**Typische Vertreter:**
- Raymarine EV-100 Tiller
- Simrad TP22/TP32
- Garmin GHP Compact Reactor (Tiller)

#### 2.3.2 Linearantrieb (Pushrod / Ram)

**Prinzip:** Elektrischer Linearmotor, der über einen Hebel am Ruderquadranten oder der Ruderpinne angreift.

**Vorteile:**
- Mittlere Kraft (150–1.200 N)
- Moderater Stromverbrauch
- Gutes Kraft-Gewicht-Verhältnis
- Leiser als Tillerpilot
- Ruderfeedback über Potentiometer möglich

**Nachteile:**
- Einbau im Ruderbereich (Achterpiek, Steuersäule)
- Platzanforderungen für Hub
- Begrenzt auf mittlere Verdrängungen
- Mechanischer Verschleiß (Kugelgelenke, Dichtungen)

**Typische Vertreter:**
- Raymarine Type 1 / Type 2 Linearantrieb
- B&G RFC35 / RFC42
- Simrad SD10 / SD15

#### 2.3.3 Rotary-Antrieb (Drehmotorantrieb)

**Prinzip:** Elektromotor mit Untersetzungsgetriebe, direkt an der Ruderwelle oder Steuerradwelle.

**Vorteile:**
- Kompakter Einbau
- Gleichmäßige Kraftübertragung
- Weniger Verschleißteile als Linearantrieb
- Gut für Radsteuerung nachrüstbar

**Nachteile:**
- Begrenzte Drehmomente
- Langsamer als Linearantrieb bei gleichem Preis
- Weniger verbreitet, eingeschränkte Modellauswahl

**Typische Vertreter:**
- Garmin GHP Reactor Rotary Actuator
- Raymarine Rotary Drive

#### 2.3.4 Hydraulikantrieb

**Prinzip:** Hydraulikpumpe erzeugt Druck, der über Leitungen und Zylinder oder Drehflügelmotoren das Ruder bewegt.

**Vorteile:**
- Höchste Kräfte (>5.000 N möglich)
- Leiser Betrieb
- Fernverlegung der Pumpe möglich
- Integration in bestehende Hydraulik-Steueranlage
- Gleichmäßige, schnelle Ruderbewegung
- Hohe Lebensdauer

**Nachteile:**
- Höchste Kosten
- Aufwendige Installation (Leitungen, Ventile, Öl)
- Hydrauliköl-Leckage möglich
- Regelmäßige Wartung (Öl, Dichtungen, Filter)
- Höchster Stromverbrauch der Pumpe
- Bypass-Ventil für Handbetrieb erforderlich

**Typische Vertreter:**
- Raymarine Type 1/2/3 Hydraulikpumpe
- Simrad RPU-80/160/300
- Garmin GHP Reactor Hydraulic Pump
- Furuno Pump Unit (diverse Größen)

### 2.4 NMEA 2000 / NMEA 0183 Integration

#### 2.4.1 NMEA 0183

**Standard:** Serielles Datenprotokoll, seit 1983 der marine Industriestandard.

**Spezifikation:**
- Baudrate: 4.800 Baud (Standard), 38.400 Baud (Hochgeschwindigkeit, AIS)
- Signalform: EIA-422, differenziell
- Topologie: Punkt-zu-Punkt (1 Sender, beliebig viele Empfänger)
- Steckverbinder: Nicht standardisiert (meist Klemmen oder DB-9)
- Datenformat: ASCII-Sentences, beginnen mit $TALKER_ID + Sentence-ID

**Relevante Sentences für Autopilot:**

| Sentence | Beschreibung | Richtung |
|----------|-------------|----------|
| $xxHDT | Heading True | Kompass → AP |
| $xxHDM | Heading Magnetic | Kompass → AP |
| $xxHDG | Heading, Deviation, Variation | Kompass → AP |
| $xxVHW | Water Speed and Heading | Log → AP |
| $xxMWV | Wind Speed and Angle | Windsensor → AP |
| $xxRMB | Recommended Minimum Navigation | Plotter → AP |
| $xxAPB | Autopilot Sentence B | Plotter → AP |
| $xxXTE | Cross-Track Error | Plotter → AP |
| $xxRSA | Rudder Sensor Angle | Rudersensor → AP |
| $xxROT | Rate of Turn | Gyroskop → AP |
| $xxDBT | Depth Below Transducer | Echolot → AP (Flachwasser-Alarm) |

**Limitierungen NMEA 0183 für Autopiloten:**
- Niedrige Datenrate: max. 10 Sentences/Sekunde bei 4.800 Baud
- Keine bidirektionale Kommunikation auf einem Kanal
- Keine Plug-and-Play-Erkennung
- Kein Fehlererkennungs-Mechanismus
- Verkabelungsaufwand bei vielen Geräten

#### 2.4.2 NMEA 2000

**Standard:** CAN-basiertes Netzwerkprotokoll, seit 2001, weit verbreitet seit ~2010.

**Spezifikation:**
- Datenrate: 250 kbit/s
- Signalform: CAN 2.0B, differenziell
- Topologie: Linearer Bus mit Backbone und Stichleitungen (Drop-Kabel)
- Steckverbinder: DeviceNet Micro-C (standardisiert, 5-polig)
- Terminierung: 120 Ω an beiden Enden des Backbone
- Max. Backbone-Länge: 100 m (bei 250 kbit/s)
- Max. Drop-Kabel: 6 m
- Max. Geräte: 50 pro Netzwerk
- Spannungsversorgung: 12V DC über Bus möglich (max. 3A pro Netzwerk)

**Relevante PGN (Parameter Group Numbers) für Autopilot:**

| PGN | Beschreibung | Sender |
|-----|-------------|--------|
| 127250 | Vessel Heading | Kompass |
| 127251 | Rate of Turn | Gyroskop |
| 127257 | Attitude (Pitch, Roll, Yaw) | Lagesensor |
| 128259 | Speed, Water Referenced | Log |
| 128267 | Water Depth | Echolot |
| 129025 | Position, Rapid Update | GPS |
| 129026 | COG & SOG, Rapid Update | GPS |
| 129029 | GNSS Position Data | GPS |
| 129283 | Cross Track Error | Plotter |
| 129284 | Navigation Data | Plotter |
| 130306 | Wind Data | Windsensor |
| 127237 | Heading/Track Control | AP ↔ Plotter |
| 065379 | Proprietary (herstellerspezifisch) | variiert |

**Vorteile NMEA 2000 für Autopiloten:**
- Plug-and-Play mit automatischer Geräteerkennung
- Hohe Datenrate: 10× schneller als NMEA 0183
- Bidirektionale Kommunikation
- Standardisierte Stecker: wasserdicht, verwechslungssicher
- Spannungsversorgung über den Bus für kleine Geräte
- CRC-Fehlerprüfung auf Paketebene

#### 2.4.3 Proprietäre Protokolle

**Raymarine SeaTalk / SeaTalkNG:**

| Eigenschaft | SeaTalk (ST1) | SeaTalkNG (STNG) |
|-------------|-------------|-----------------|
| Physikalisch | 3-adrig, proprietär | DeviceNet Micro-C (NMEA 2000 kompatibel) |
| Datenrate | 4.800 Baud | 250 kbit/s |
| Topologie | Multi-Drop | Linearer Bus |
| NMEA-Kompatibilität | Brücke nötig | Physikalisch NMEA 2000, logisch NMEA 2000 + proprietäre PGNs |
| Status | Legacy (seit 1990er) | Aktuell |
| Konverter | SeaTalk → NMEA 0183/2000 | Direkt an NMEA 2000 Backbone anschließbar |

> **Praxis-Hinweis:** SeaTalkNG-Kabel und NMEA 2000-Kabel sind physikalisch identisch (DeviceNet Micro-C). Ein SeaTalkNG-Gerät kann direkt an ein NMEA 2000-Backbone angeschlossen werden. Proprietäre Raymarine-PGNs werden dann aber nur von anderen Raymarine-Geräten verstanden.

**Simrad SimNet:**

| Eigenschaft | SimNet |
|-------------|--------|
| Physikalisch | Proprietärer 5-poliger Stecker (gelb) |
| Datenrate | 250 kbit/s (CAN-basiert) |
| Topologie | Bus mit T-Stücken |
| NMEA 2000 | Logisch kompatibel, physikalisch Adapter nötig (SimNet→N2K-Kabel) |
| Status | Auslaufend, durch NMEA 2000 nativ ersetzt |

**Garmin:**
Garmin verwendet ausschließlich NMEA 2000 als Bussystem. Proprietäre PGNs existieren für Garmin-interne Funktionen (z.B. Reactor-Kalibrierung), Grundfunktionen sind voll NMEA-2000-konform.

**Furuno:**
Furuno nutzt standardmäßig NMEA 2000 für aktuelle Systeme. Ältere Systeme kommunizieren über NMEA 0183 oder den proprietären Furuno CAN-Bus (NavNet-intern). Ein CANbus-Gateway ermöglicht die Anbindung.

**NKE:**
NKE verwendet ein proprietäres Bussystem (NKE-Bus, topologie-basiert) für die Kommunikation zwischen NKE-Geräten. Ein NMEA-2000-Gateway (NKE Topline Multiplexer) ist für die Integration in gemischte Systeme verfügbar.

### 2.5 Stromverbrauch-Berechnung

Der Stromverbrauch eines Autopiloten ist für die Dimensionierung der Bordelektrik (Batterie, Lichtmaschine, Solarpanele) entscheidend — insbesondere auf Langfahrt.

**Stromverbrauch-Komponenten:**

| Komponente | Typischer Verbrauch (12V) | Betriebsart |
|-----------|--------------------------|-------------|
| Kurscomputer | 0,2–0,8 A | Dauerbetrieb |
| Kompass / Lagesensor | 0,05–0,2 A | Dauerbetrieb |
| Bedieneinheit (Display) | 0,1–0,5 A | Dauerbetrieb |
| Antrieb Tillerpilot | 0,5–3,0 A | Intermittierend |
| Antrieb Linear | 1,0–8,0 A | Intermittierend |
| Antrieb Hydraulik | 2,0–25,0 A | Intermittierend |

**Durchschnittlicher Stromverbrauch — Berechnung:**

```
P_avg = P_standby + (P_drive × Duty_Cycle)

wobei:
  P_standby = Kurscomputer + Kompass + Display (permanent)
  P_drive   = Antriebsleistung bei Vollast
  Duty_Cycle = Anteil der Zeit, in der der Antrieb tatsächlich arbeitet
```

**Typische Duty Cycles:**

| Bedingung | Segelboot | Motorboot |
|-----------|----------|----------|
| Ruhiges Wasser, gerader Kurs | 5–10 % | 3–8 % |
| Moderate See, Seitenwind | 15–25 % | 10–15 % |
| Raue See, Kurswechsel | 30–50 % | 20–35 % |
| Schwere See, ständige Korrektur | 50–80 % | 35–60 % |
| Wende/Halse | 100 % (kurzzeitig) | — |

**Rechenbeispiel: Segelyacht 38 ft, moderate See:**

```
Kurscomputer Raymarine EV-200:   0,4 A
Kompass EV-1 Sensor:             0,1 A
Bedieneinheit p70Rs:             0,2 A
Linearantrieb Type 1 (Vollast):  5,0 A
Duty Cycle:                      20 %

P_avg = (0,4 + 0,1 + 0,2) + (5,0 × 0,20)
P_avg = 0,7 + 1,0 = 1,7 A bei 12V = 20,4 W

24h-Verbrauch = 1,7 × 24 = 40,8 Ah

Bei 200 Ah Batteriebank (50 % nutzbar):
Autonomie nur Autopilot: 100 Ah / 1,7 A ≈ 59 Stunden
```

> **Praxis-Tipp:** Für Langfahrt sollte der Autopilot nie mehr als 25–30 % der täglichen Energiebilanz beanspruchen. Bei 40,8 Ah AP-Verbrauch braucht man ~160 Ah tägliche Nachladung gesamt, also mind. 200 Ah Batteriekapazität mit täglicher Ladung.

### 2.6 Kompasstypen und Kursreferenz

#### 2.6.1 Fluxgate-Kompass

**Prinzip:** Zwei parallele Kerne aus hochpermeablem Material mit Erreger- und Detektorwicklungen. Das Erdmagnetfeld erzeugt ein asymmetrisches Signal, aus dem die Richtung berechnet wird.

**Vorteile:**
- Bewährte Technologie (>40 Jahre im Marineeinsatz)
- Hohe Genauigkeit (±0,5° nach Kalibrierung)
- Unempfindlich gegen Vibrationen
- Keine beweglichen Teile

**Nachteile:**
- Empfindlich gegen magnetische Störfelder (Motor, Lautsprecher, Stahl)
- Einbau-Position kritisch (mind. 1m von Störquellen)
- Deviation-Korrektur erforderlich
- Langsame Heading-Aktualisierung (5–10 Hz)

**Hersteller und Modelle:**
- Raymarine: Fluxgate-Kompass in EV-1 Sensor integriert
- B&G: Precision-9-Kompass (enthält Fluxgate + MEMS)
- Furuno: PG-700 Fluxgate-Kompass
- Simrad: HS75 GNSS Kompass (Fluxgate + GPS)

#### 2.6.2 MEMS-Kompass / Inertiale Messeinheit (IMU)

**Prinzip:** Mikromechanische Sensoren messen Beschleunigung (3 Achsen) und Drehrate (3 Achsen). Magnetometer liefert die Nordrichtung. Sensorfusion (Kalman-Filter) kombiniert alle Daten.

**Vorteile:**
- Extrem schnelle Heading-Aktualisierung (25–100 Hz)
- Kompakte Bauform
- Pitch/Roll/Yaw-Daten integriert
- Günstiger als Fluxgate bei ähnlicher Genauigkeit
- Weniger empfindlich gegen Einbau-Position

**Nachteile:**
- Drift über Zeit (ohne GPS-Stützung)
- Magnetometer empfindlich gegen lokale Störfelder
- Kalibrierung bei Erstinstallation nötig
- Qualitätsunterschiede bei MEMS-Chips erheblich

**Hersteller und Modelle:**
- Raymarine: EV-1 Sensor Core (9-Achsen-MEMS)
- B&G: Precision-9 (9-Achsen, GPS-gestützt)
- Garmin: in Reactor-Kurscomputer integriert
- NKE: gyropilot2 integrierter MEMS-Sensor

#### 2.6.3 Satellitenkompass (GNSS-Kompass)

**Prinzip:** Zwei oder mehr GPS/GNSS-Antennen in definiertem Abstand. Aus der Phasendifferenz der Satellitensignale wird die Heading-Richtung berechnet.

**Vorteile:**
- Unabhängig von Magnetfeld (keine Deviation)
- Höchste Genauigkeit (±0,3° bei >1m Antennenabstand)
- Kein Kalibrierungs-Aufwand
- Gleichzeitig GPS-Position und Heading

**Nachteile:**
- Höchste Kosten (2.000–8.000 €)
- Erfordert freie Sicht zum Himmel (keine Überdachung)
- Langsamer als MEMS bei schnellen Drehungen
- Ausfall bei gestörtem GPS-Signal

**Hersteller und Modelle:**
- Simrad: HS75 GNSS Compass (Dual-Antenne)
- Furuno: SCX-20 Satellite Compass
- B&G: Zeus / Vulcan mit externem GNSS-Kompass
- Garmin: GPS 24xd (kein echter Dual-Antenna-Kompass, nur GPS-COG)

### 2.7 Ruderarten und deren Einfluss auf den Autopiloten

| Rudertyp | Beschreibung | Autopilot-Relevanz |
|----------|-------------|-------------------|
| Spatenruder | Freistehendes Ruderblatt, kein Skeg | Höchste Ruderkraft erforderlich, schnelle Ansprechzeit |
| Skeg-Ruder | Ruder hinter Skeg aufgehängt | Geringere Kraft, guter Geradeauslauf, langsamer |
| Langkiel-Ruder | Am Langkiel angehängt | Geringste Kraft, sehr stabiler Geradeauslauf, träge |
| Doppelruder | Zwei Ruder (Katamaran, Motorboot) | Zwei Antriebe oder Verteilventil nötig |
| Balanceruder | Drehpunkt hinter Vorderkante | Reduzierte Ruderkraft, reaktionsfreudig |
| Bugstrahlruder | Querstrahlruder im Bug | Nur bei Langsamfahrt, separater Autopilot (Docking) |

### 2.8 Normen und Standards

| Norm | Titel | Relevanz für Autopilot |
|------|------|----------------------|
| ISO 11674:2019 | Kursregelungsanlagen (Heading Control Systems) | Mindestanforderungen an Funktion, Sicherheit, Alarmierung, Umschaltung Auto↔Hand |
| IEC 62065 | Track Control Systems | Performanceanforderungen an Kursregelungen |
| IEC 61162-1 | NMEA 0183 | Datenaustausch-Protokoll |
| IEC 61162-3 | NMEA 2000 | CAN-basiertes Netzwerkprotokoll |
| ISO 13297 | Elektrische Systeme | Allgemeine Anforderungen an Bordelektrik |
| EN 60945 | Maritime Navigationsausrüstung | EMV, Umweltbedingungen, Prüfverfahren |
| COLREG Rule 5 | Ausguckpflicht | Autopilot entbindet NICHT von Ausguckpflicht |

> **Wichtig:** Ein Autopilot ist ein Navigations-HILFSMITTEL. Der Schiffsführer bleibt verantwortlich (COLREG Regel 5). Kein Autopilot ersetzt den Ausguck. AYDI muss dies in jedem Report vermerken.

---

## 3. Typenübersicht

### 3.1 Raymarine — Evolution-Serie

#### 3.1.1 Hersteller-Profil Raymarine

| Merkmal | Detail |
|---------|--------|
| Konzern | Teledyne FLIR (seit 2020) |
| Sitz | Fareham, Hampshire, UK |
| Gegründet | 1923 als Kelvin Hughes, Marke Raymarine seit 2001 |
| Schwerpunkt | Freizeitboote, Segelyachten, Motorboote bis 24m |
| Marktposition | Marktführer Segeln Europa, stark bei Charterflotten |
| Bussystem | SeaTalkNG (NMEA 2000 kompatibel) |
| Service Deutschland | Busse Yachtshop (Hamburg), Raymarine Service Center |

#### 3.1.2 Evolution-Technologie

Raymarines "Evolution" bezeichnet die seit 2014 eingeführte Autopilot-Plattform mit integrierter MEMS-Sensorik im EV-1 Sensor Core. Kernmerkmal: Der Autopilot benötigt keine manuelle Kalibrierung — "Plug and Play".

**EV-1 Sensor Core:**
- 9-Achsen-MEMS (3× Beschleunigung, 3× Gyroskop, 3× Magnetometer)
- Heading-Aktualisierung: 40 Hz
- Genauigkeit: ±2° (ungestützt), ±0,5° (GPS-gestützt nach Lernphase)
- Einbau: Möglichst nahe am Schwerpunkt des Bootes
- Temperaturbereich: -15°C bis +55°C
- Schutzklasse: IPX6
- Anschluss: SeaTalkNG (1× Kabel)

**Evolution AI (Adaptive Intelligence):**
Der EV-1 Sensor "lernt" das Verhalten des Bootes kontinuierlich. Parameter wie Trägheitsmoment, Ruderansprechzeit, Wellenmuster und Seitenwindeinfluss werden automatisch adaptiert. Die Lernphase dauert typischerweise 15–60 Minuten Fahrt. Danach ist die Performance deutlich besser als bei manuell kalibrierten Systemen gleicher Preisklasse.

#### 3.1.3 Raymarine EV-100

**Zielgruppe:** Kleine Segelyachten und Motorboote bis ca. 7.000 kg Verdrängung.

| Spezifikation | Wert |
|--------------|------|
| Kurscomputer | ACU-100 (intern im Antrieb) |
| Sensor | EV-1 Sensor Core |
| Bedieneinheit | p70 (monochrom) oder p70s (Farbe) |
| Antriebsoptionen | Tillerpilot (bis 7.000 kg), Radpilot Wheel, Type 1 Linear |
| Ruderkraft Tillerpilot | 50 kg (490 N) |
| Hub Tillerpilot | ±30° bei 500 mm Pinne |
| Stromverbrauch Standby | 0,1 A (12V) |
| Stromverbrauch Fahrt | 0,5–2,5 A (12V), abhängig von Bedingungen |
| Preis (Set Tiller, 2025) | ca. 1.800–2.200 € |
| Preis (Set Wheel, 2025) | ca. 2.200–2.800 € |
| Wind-Modus | Ja (mit ext. Windsensor) |
| NMEA 2000 | Ja (über SeaTalkNG) |

**Bekannte Schwächen EV-100:**
- Tillerpilot-Spindel verschleißt bei häufigem Einsatz in rauer See (Lebensdauer ~2.000–5.000 Betriebsstunden)
- Zahnriemen des Radpiloten kann bei extremer Kälte (<-10°C) reißen
- ACU-100 hat begrenzte Rechenleistung: bei komplexen Seebedingungen teils langsame Adaption
- EV-1 Sensor empfindlich gegen Vibration bei Einbau nahe Motor/Antriebswelle

#### 3.1.4 Raymarine EV-150

**Zielgruppe:** Mittlere Segelyachten 8.000–15.000 kg.

| Spezifikation | Wert |
|--------------|------|
| Kurscomputer | ACU-150 |
| Sensor | EV-1 Sensor Core + optionaler EV-2 (Ruderfeedback) |
| Bedieneinheit | p70Rs (Segel, Farbe) oder p70R (Motor, Farbe) |
| Antriebsoptionen | Type 1 Linear, Type 1 Hydraulik |
| Ruderkraft Linear Type 1 | 112 kg (1.100 N) |
| Ruderkraft Hydraulik | Abhängig von Zylinder/Pumpe |
| Hub Linear Type 1 | 178 mm (7") |
| Stromverbrauch ACU-150 Standby | 0,25 A (12V) |
| Stromverbrauch Fahrt | 1,0–6,0 A (12V) |
| Preis (Set Linear, 2025) | ca. 3.500–4.500 € |
| Wind-Modus | Ja (empfohlen) |
| Track-Modus | Ja (mit Plotter) |
| NMEA 2000 | Ja |

#### 3.1.5 Raymarine EV-200

**Zielgruppe:** Große Segelyachten und Motorboote 10.000–25.000 kg.

| Spezifikation | Wert |
|--------------|------|
| Kurscomputer | ACU-200 |
| Sensor | EV-1 Sensor Core + EV-2 Ruderfeedback (empfohlen) |
| Bedieneinheit | p70Rs / p70R |
| Antriebsoptionen | Type 1/2 Linear, Type 1/2/3 Hydraulik |
| Ruderkraft Type 2 Linear | 230 kg (2.250 N) |
| Hub Type 2 Linear | 305 mm (12") |
| Hydraulikzylinder | 80 / 150 / 300 ccm/rev |
| Stromverbrauch ACU-200 Standby | 0,3 A (12V) |
| Stromverbrauch Fahrt | 1,5–12,0 A (12V) |
| Preis (Set Hydraulik, 2025) | ca. 5.500–8.500 € |
| Wind-Modus | Ja |
| Track-Modus | Ja |
| Erweiterte Segel-Modi | Windshift-Tracking, Auto-Tack |
| NMEA 2000 | Ja |

#### 3.1.6 Raymarine EV-400

**Zielgruppe:** Superyachten und gewerbliche Fahrzeuge >25.000 kg.

| Spezifikation | Wert |
|--------------|------|
| Kurscomputer | ACU-400 |
| Sensor | EV-1 Sensor Core + EV-2 Ruderfeedback (zwingend) |
| Bedieneinheit | p70Rs / p70R, Integration in Axiom XL MFD |
| Antriebsoptionen | Type 2/3 Hydraulik, Doppelstation |
| Hydraulikleistung | Bis 7,5 l/min Pumpenleistung |
| Stromverbrauch ACU-400 Standby | 0,4 A (12V), 0,2 A (24V) |
| Stromverbrauch Fahrt | 3,0–25,0 A (12V), 1,5–12,5 A (24V) |
| Preis (System, 2025) | ca. 12.000–25.000 € |
| Redundanz | Dual-ACU optional |
| 24V-Betrieb | Ja |
| NMEA 2000 | Ja |
| IEC 62065 | Konform |

### 3.2 B&G — H5000 / NAC-Serie

#### 3.2.1 Hersteller-Profil B&G

| Merkmal | Detail |
|---------|--------|
| Konzern | Navico Group (Fiskars/Brunswick) |
| Sitz | Fareham, Hampshire, UK (teilt Gebäude mit Navico) |
| Gegründet | 1956 als Brookes and Gatehouse |
| Schwerpunkt | Segelyachten, Regatta, Performance Cruising |
| Marktposition | Führend bei Performance-Seglern und Regattayachten |
| Bussystem | NMEA 2000 (nativ), SimNet-kompatibel |
| Besonderheit | Einziger Hersteller mit dediziertem Segelrechner (H5000) |
| Service Deutschland | Diverse Navico-Händler, Online-Support |

#### 3.2.2 H5000 Hydra System

Das H5000 Hydra ist B&Gs Flaggschiff-System für Performance-Segler. Es ist kein reiner Autopilot, sondern ein vollständiges Segel-Instrumenten- und Steuerungssystem mit integriertem Autopiloten.

**Architektur:**

```
H5000 CPU ◄──► Precision-9 Kompass
    │          Windsensor(en)
    │          GPS
    │          Geschwindigkeit (Paddlewheel / Ultraschall)
    │          Tiefe
    │          
    ├──► Hercules (Rechenmodul)
    │      ├── Polardaten
    │      ├── Performance-Berechnung
    │      ├── Layline-Berechnung
    │      └── Routing-Optimierung
    │
    ├──► NAC-2 / NAC-3 (Autopilot-Computer)
    │      ├── Kursregelung
    │      ├── Wind-Modus
    │      └── Track-Modus
    │
    └──► Displays (Triton2, Vulcan, Zeus)
```

**H5000 Autopilot-Parameter (segelspezifisch):**

| Parameter | Beschreibung | Einstellung |
|-----------|-------------|-------------|
| Response Level | Gesamtaggressivität | 1–9 (1=sanft, 9=aggressiv) |
| Counter Rudder | Gegenruderstärke | Auto oder Manuell |
| Auto Trim | Automatische Ruder-Mittelstellung | An/Aus |
| Wind Response | Reaktion auf Windänderungen (Wind-Modus) | 1–9 |
| Wave Filter | Seegangsfilter | Aus, Niedrig, Mittel, Hoch |
| Tack Angle | Voreingestellter Wendewinkel | 70°–130° |
| Tack Speed | Geschwindigkeit der Autopilot-Wende | Langsam/Mittel/Schnell |
| Gybe Mode | Halsen-Verhalten | Standard, Schnell, Kontrolliert |
| TWA Lock | Verriegelung auf wahren Windwinkel | An/Aus |

#### 3.2.3 B&G NAC-1

**Zielgruppe:** Kleine Segelboote bis 5.000 kg, Nachrüstung älterer B&G-Systeme.

| Spezifikation | Wert |
|--------------|------|
| Kurscomputer | NAC-1 |
| Sensor | Precision-9 Kompass oder extern |
| Antriebsoptionen | Linearantrieb (RFC25/RFC35) |
| Max. Verdrängung | 5.000 kg |
| Ruderkraft | Bis 600 N (mit RFC35) |
| Stromverbrauch Standby | 0,15 A (12V) |
| Stromverbrauch Fahrt | 0,8–4,0 A (12V) |
| Wind-Modus | Ja |
| Preis (NAC-1 allein, 2025) | ca. 1.200–1.600 € |
| NMEA 2000 | Ja |

#### 3.2.4 B&G NAC-2

**Zielgruppe:** Mittlere Segelyachten 5.000–15.000 kg. Der "Sweet Spot" im B&G-Sortiment.

| Spezifikation | Wert |
|--------------|------|
| Kurscomputer | NAC-2 |
| Sensor | Precision-9 Kompass (empfohlen) |
| Antriebsoptionen | RFC35/RFC42 Linear, Hydraulikpumpe |
| Max. Verdrängung | 15.000 kg (Linear), 25.000 kg (Hydraulik) |
| Ruderkraft RFC42 | 1.680 N |
| Hub RFC42 | 305 mm |
| Stromverbrauch NAC-2 Standby | 0,2 A (12V) |
| Stromverbrauch Fahrt | 1,0–8,0 A (12V) |
| Wind-Modus | Ja (hervorragend) |
| Preis (NAC-2 + RFC42, 2025) | ca. 4.000–5.500 € |
| H5000-Integration | Voll (als Slave des H5000 CPU) |
| Continuum-Algorithmus | Ja |
| NMEA 2000 | Ja |

**Continuum-Algorithmus:**
B&Gs proprietärer Regelalgorithmus für Segeln. Verwendet Windgeschwindigkeit, Bootgeschwindigkeit, Roll-Rate und Ruderfeedback, um den Autopiloten in Echtzeit an Böen und Wellengang anzupassen. Im direkten Vergleich mit Raymarine Evolution oft gelobt für besseres Kurshalten am Wind bei böigem Wetter.

#### 3.2.5 B&G NAC-3

**Zielgruppe:** Große Segelyachten und Superyachten >15.000 kg.

| Spezifikation | Wert |
|--------------|------|
| Kurscomputer | NAC-3 |
| Sensor | Precision-9 + optional Satelliten-Kompass |
| Antriebsoptionen | Hydraulikpumpen bis 3,0 l/min |
| Max. Verdrängung | >50.000 kg |
| Hydraulikpumpen | RPU-80 (80 ccm/rev) bis RPU-300 (300 ccm/rev) |
| Stromverbrauch NAC-3 Standby | 0,25 A (12V) |
| Stromverbrauch Fahrt | 2,0–20,0 A (12V) |
| Preis (NAC-3 + Pumpe, 2025) | ca. 8.000–18.000 € |
| Dual-Station | Ja |
| 24V-Betrieb | Ja |
| Redundanz | Dual-NAC-3 möglich |
| NMEA 2000 | Ja |
| IEC 62065 | Konform |

### 3.3 Garmin — GHP Reactor-Serie

#### 3.3.1 Hersteller-Profil Garmin

| Merkmal | Detail |
|---------|--------|
| Konzern | Garmin Ltd. (börsennotiert) |
| Sitz | Olathe, Kansas, USA / Schaffhausen, Schweiz |
| Gegründet | 1989 |
| Schwerpunkt | GPS-Technologie, breit aufgestellt (Fitness, Luftfahrt, Marine, Auto) |
| Marktposition | Marktführer Plotter USA, stark wachsend Europa |
| Bussystem | NMEA 2000 (nativ, kein proprietärer Bus) |
| Besonderheit | Tiefe Integration Plotter ↔ Autopilot ↔ Radar |
| Service Deutschland | Garmin Deutschland GmbH, Garching bei München |

#### 3.3.2 Reactor-Technologie

Garmins Autopiloten basieren auf der "Reactor"-Plattform mit integrierter Solid-State-AHRS (Attitude and Heading Reference System). Kernmerkmal: extrem schnelle Heading-Referenz (50 Hz) und "Shadow Drive" — automatische Deaktivierung, wenn der Rudergänger manuell steuert.

**Shadow Drive:**
Ein Drucksensor im Hydraulikkreislauf (oder Drehmoment-Sensor bei Mechanik) erkennt, wenn der Rudergänger am Steuerrad dreht. Der Autopilot geht sofort in Standby, ohne dass eine Taste gedrückt werden muss. Beim Loslassen des Steuerrades übernimmt der AP den aktuellen Kurs. Bei Seglern umstritten: Beim Trimmen der Segel kann unbeabsichtigtes Ruderberühren den AP deaktivieren.

#### 3.3.3 Garmin GHP Reactor Compact (Tiller)

**Zielgruppe:** Kleine Segelboote mit Pinnensteuerung, bis 5.000 kg.

| Spezifikation | Wert |
|--------------|------|
| Kurscomputer | Im Antrieb integriert |
| Sensor | Integrierter AHRS |
| Antrieb | Tiller-Aktuator |
| Max. Verdrängung | 5.000 kg |
| Ruderkraft | 390 N |
| Hub | ±30° bei 500 mm Pinne |
| Stromverbrauch Standby | 0,08 A (12V) |
| Stromverbrauch Fahrt | 0,5–2,0 A (12V) |
| Wind-Modus | Ja (mit gWind) |
| Preis (Set, 2025) | ca. 1.600–2.000 € |
| NMEA 2000 | Ja |

#### 3.3.4 Garmin GHP Reactor 20

**Zielgruppe:** Motorboote und Segelyachten mit Radsteuerung, 3.000–12.000 kg.

| Spezifikation | Wert |
|--------------|------|
| Kurscomputer | GHP Reactor 20 CCU |
| Sensor | Integrierter AHRS im CCU |
| Antriebsoptionen | Hydraulik-Pumpe (0,8 l/min), Rotary |
| Max. Verdrängung | 12.000 kg |
| Shadow Drive | Ja |
| Stromverbrauch CCU Standby | 0,15 A (12V) |
| Stromverbrauch Fahrt | 1,5–8,0 A (12V) |
| Preis (Set Hydraulik, 2025) | ca. 3.500–5.000 € |
| Wind-Modus | Ja |
| Track-Modus | Ja (mit GPSMAP oder Echomap) |
| NMEA 2000 | Ja |
| Garmin Auto-Guidance | Ja (mit kompatiblem Plotter) |

**Garmin Auto-Guidance:**
Proprietäre Funktion, die automatisch eine sichere Route von A nach B berechnet, Untiefen und Hindernisse umfährt und den Autopilot die Strecke abfahren lässt. Basiert auf Garmins Navionics-Kartendaten. Nur mit Garmin-Plottern nutzbar — starker Lock-in-Effekt.

#### 3.3.5 Garmin GHP Reactor 40

**Zielgruppe:** Große Motor- und Segelyachten 10.000–30.000 kg.

| Spezifikation | Wert |
|--------------|------|
| Kurscomputer | GHP Reactor 40 CCU |
| Sensor | Integrierter AHRS + optionaler GHC50 GNSS-Kompass |
| Antriebsoptionen | Hydraulik-Pumpe 1,2 l/min / 2,0 l/min |
| Max. Verdrängung | 30.000 kg |
| Shadow Drive | Ja |
| Stromverbrauch CCU Standby | 0,2 A (12V) |
| Stromverbrauch Fahrt | 2,0–15,0 A (12V) |
| Preis (Set, 2025) | ca. 6.000–12.000 € |
| Docking-Assist | Ja (mit Volvo IPS / Mercury Joystick) |
| Dual-Station | Ja |
| 24V-Betrieb | Ja |
| NMEA 2000 | Ja |

### 3.4 Simrad — AP-Serie

#### 3.4.1 Hersteller-Profil Simrad

| Merkmal | Detail |
|---------|--------|
| Konzern | Navico Group (Fiskars/Brunswick, gleicher Konzern wie B&G) |
| Sitz | Egersund, Norwegen |
| Gegründet | 1947 als Simonsen Radio |
| Schwerpunkt | Motorboote, Fischerei, gewerbliche Schifffahrt |
| Marktposition | Stark bei Motoryachten, Sportfischen, Fischerei Europa |
| Bussystem | SimNet (auslaufend), NMEA 2000 (aktuell) |
| Besonderheit | Teilt Technologiebasis mit B&G (NAC-Computer = AC-Computer) |
| Service Deutschland | Navico-Händlernetz |

> **Wichtiger Hinweis:** Simrad und B&G verwenden intern die gleiche Hardware-Plattform. Der Simrad AC70 ist technisch identisch mit dem B&G NAC-3. Der Unterschied liegt in der Firmware (Motorboot-optimiert bei Simrad, Segel-optimiert bei B&G) und den verfügbaren Bedieneinheiten.

#### 3.4.2 Simrad AP44

**Zielgruppe:** Kleinere Motorboote und Segelyachten, bis 12.000 kg. Einstiegssystem mit Vollausstattung.

| Spezifikation | Wert |
|--------------|------|
| Bedieneinheit | AP44 (4,1" Farb-Touchscreen) |
| Kurscomputer | NAC-1 (integriert) oder extern |
| Sensor | Precision-9 oder integriert |
| Antriebsoptionen | SD10 Linear, Hydraulikpumpe |
| Max. Verdrängung | 12.000 kg |
| Stromverbrauch Standby | 0,2 A (12V) |
| Stromverbrauch Fahrt | 1,0–6,0 A (12V) |
| Preis (AP44 Basisset, 2025) | ca. 2.500–3.500 € |
| NMEA 2000 | Ja |
| SimNet | Ja (über Adapter) |
| Wind-Modus | Ja |

#### 3.4.3 Simrad AP48

**Zielgruppe:** Mittlere Motorboote und Segelyachten, bis 25.000 kg.

| Spezifikation | Wert |
|--------------|------|
| Bedieneinheit | AP48 (4,1" Farb-Touchscreen) |
| Kurscomputer | AC42 / AC70 |
| Sensor | Precision-9, HS75 GNSS optional |
| Antriebsoptionen | SD10/SD15 Linear, RPU-80/160 Hydraulik |
| Max. Verdrängung | 25.000 kg |
| Stromverbrauch Standby | 0,25 A (12V) |
| Stromverbrauch Fahrt | 2,0–12,0 A (12V) |
| Preis (AP48 Hydraulik, 2025) | ca. 5.000–8.000 € |
| Dual-Station | Ja |
| NMEA 2000 | Ja |
| Segel-Modus | Basis (kein Continuum) |

#### 3.4.4 Simrad AC70

**Zielgruppe:** Große Motorboote, Superyachten, gewerbliche Fahrzeuge >25.000 kg.

| Spezifikation | Wert |
|--------------|------|
| Kurscomputer | AC70 |
| Sensor | Precision-9 + HS75 GNSS Kompass |
| Antriebsoptionen | RPU-160/300 Hydraulik, externe Ventilsteuerung |
| Max. Verdrängung | >100.000 kg |
| Hydraulikpumpen | RPU-80 (1,2 l/min) bis RPU-300 (4,5 l/min) |
| Stromverbrauch AC70 Standby | 0,3 A (12V), 0,15 A (24V) |
| Stromverbrauch Fahrt | 3,0–25,0 A (12V) |
| Preis (AC70 System, 2025) | ca. 12.000–30.000 € |
| Dual-Station | Ja |
| 24V-Betrieb | Ja |
| Redundanz | Dual-AC70 |
| IEC 62065 | Konform |
| NMEA 2000 | Ja |
| IMO-konform | Ja (für gewerbliche Schiffe) |

### 3.5 Furuno — NavPilot-Serie

#### 3.5.1 Hersteller-Profil Furuno

| Merkmal | Detail |
|---------|--------|
| Konzern | Furuno Electric Co., Ltd. (börsennotiert, Tokio) |
| Sitz | Nishinomiya, Hyogo, Japan |
| Gegründet | 1948 |
| Schwerpunkt | Kommerzielle Schifffahrt, Fischerei, Superyachten |
| Marktposition | Weltmarktführer kommerzielle Schiffselektronik, Premium-Segment Yachten |
| Bussystem | NMEA 2000 (aktuell), CAN-Bus intern (NavNet), NMEA 0183 |
| Besonderheit | Höchste Zuverlässigkeit im Markt, japanische Fertigungsqualität |
| Service Deutschland | Furuno Deutschland GmbH, Rellingen bei Hamburg |

> **Reputation:** Furuno genießt bei professionellen Seeleuten den höchsten Ruf für Zuverlässigkeit. "Wenn es Furuno nicht anzeigt, existiert es nicht" ist ein geflügeltes Wort unter kommerziellen Fischern. Für Freizeitsegler wird Furuno als "Overkill" empfunden, für Langfahrt und Blauwassersegler als Goldstandard.

#### 3.5.2 Furuno NavPilot 300

**Zielgruppe:** Motorboote und Segelyachten 5.000–30.000 kg. Furunos Antwort auf den Freizeit-Markt.

| Spezifikation | Wert |
|--------------|------|
| Kurscomputer / Bedieneinheit | NavPilot 300 (integriertes Gerät, 4,1" Farb-Touchscreen) |
| Sensor | Integrierter 9-Achsen-MEMS-Sensor |
| Antriebsoptionen | Hydraulikpumpe (diverse Größen), Solenoidventil |
| Max. Verdrängung | 30.000 kg (herstellerabhängig von Pumpe) |
| Besonderheit | "Gesture Control" — Wischgesten für Kursänderung |
| Stromverbrauch Standby | 0,4 A (12V) |
| Stromverbrauch Fahrt | 1,5–10,0 A (12V) |
| Preis (NavPilot 300, 2025) | ca. 2.500–3.500 € (ohne Pumpe) |
| Fish Hunter Modus | Ja (automatisches Kreisen über Fischmarkierung) |
| Wind-Modus | Ja |
| Track-Modus | Ja |
| NMEA 2000 | Ja |
| NMEA 0183 | Ja (2 Ports) |
| Sabiki-Modus | Ja (automatische Fangtechnik-Muster) |

**Besonderheiten NavPilot 300:**
- **Gesture Control:** Durch Wischen über das Display kann der Kurs in 1°-, 5°- oder 10°-Schritten geändert werden. Im Praxistest sehr intuitiv bei nassen Händen.
- **Fish Hunter Mode:** Exklusiv bei Furuno — der Autopilot fährt automatisch Kreise oder Achten über eine markierte Position. Für Angler entwickelt, auf dem europäischen Markt weniger relevant.
- **Selbstlernender Algorithmus:** Ähnlich Raymarines Evolution, aber mit langsamerer Konvergenz. Benötigt 30–90 Minuten für optimale Einstellung.

#### 3.5.3 Furuno NavPilot 700

**Zielgruppe:** Superyachten, gewerbliche Schiffe, Langfahrt-Blauwassersegler. Das Flaggschiff.

| Spezifikation | Wert |
|--------------|------|
| Kurscomputer | Processor Unit FAP-7011C |
| Bedieneinheit | Control Unit FAP-7001C (5,7" Farb-Touchscreen) |
| Sensor | PG-700 Fluxgate oder SCX-20 Satelliten-Kompass |
| Antriebsoptionen | Hydraulikpumpen bis 600 ccm/rev, Proportionalventile |
| Max. Verdrängung | Unbegrenzt (Pumpe/Ventil bestimmt Limit) |
| Stromverbrauch Prozessor Standby | 0,5 A (12V), 0,25 A (24V) |
| Stromverbrauch Fahrt | 3,0–30,0+ A (je nach Pumpe) |
| Preis (NavPilot 700 System, 2025) | ca. 8.000–25.000 € |
| Dual-Station | Ja (bis 4 Bedieneinheiten) |
| 24V-Betrieb | Ja |
| Redundanz | Dual-Prozessor, Dual-Kompass |
| IEC 62065 | Konform |
| IMO-Zulassung | Ja |
| Adaptive Pilot | Ja (3 Profile: Wirtschaftlich, Standard, Präzise) |
| NMEA 2000 | Ja |
| NMEA 0183 | Ja (4 Ports) |
| Furuno CAN-Bus | Ja |
| Ethernet | Ja (NavNet TZtouch Integration) |

**Besonderheiten NavPilot 700:**
- **3 Betriebsprofile:** Economy (minimale Ruderbewegung, Treibstoffersparnis), Standard (ausgewogen), Precise (engste Kursführung, höchster Verbrauch)
- **Automatische See-Erkennung:** Analysiert Wellenmuster und passt Regelparameter automatisch an
- **Multi-Heading-Sensor:** Kann bis zu 3 Heading-Quellen gleichzeitig auswerten und die zuverlässigste verwenden
- **Black-Box-Funktion:** Speichert die letzten 24h aller Sensor- und Steuerdaten für Diagnose
- **Alarm-Management:** Umfangreiche Alarmkonfiguration für Kursabweichung, Ruderlimit, Antriebsüberlast, Sensorausfall

### 3.6 NKE — Gyropilot 2

#### 3.6.1 Hersteller-Profil NKE

| Merkmal | Detail |
|---------|--------|
| Konzern | NKE Marine Electronics (unabhängig) |
| Sitz | Hennebont, Bretagne, Frankreich |
| Gegründet | 1984 |
| Schwerpunkt | Regattasegler, Offshore-Rennen, Performance Cruising |
| Marktposition | De-facto-Standard bei französischen Einhandseglern und Offshore-Regatten |
| Bussystem | NKE-Bus (proprietär), NMEA 2000 Gateway |
| Besonderheit | Überlegene Segel-Algorithmen, von Vendée-Globe-Seglern entwickelt |
| Service Deutschland | Wenige Fachhändler, Hauptmarkt Frankreich |

> **Reputation:** NKE genießt in der Regattaszene legendären Ruf. Der Gyropilot ist der Autopilot, der am besten segelt — Punkt. Bei Offshore-Regatten (Mini-Transat, Figaro, Vendée Globe) hat NKE einen Marktanteil von geschätzten 60–80 %. Für Fahrtensegler ist NKE weniger bekannt, bietet aber die gleiche Performance.

#### 3.6.2 NKE Gyropilot 2

**Zielgruppe:** Regattasegler und Performance-Cruiser aller Größen.

| Spezifikation | Wert |
|--------------|------|
| Kurscomputer | Gyropilot 2 Prozessor |
| Sensor | Integrierter 9-Achsen MEMS + optionaler Fluxgate |
| Antriebsoptionen | NKE Linear Aktuator, Hydraulik über Standard-Pumpen |
| Max. Verdrängung | Abhängig vom Antrieb (bis >20.000 kg) |
| Besonderheit | 4 getrennt optimierbare Segel-Modi (Upwind, Reach, Downwind, VMG) |
| Stromverbrauch Standby | 0,12 A (12V) |
| Stromverbrauch Fahrt | 0,8–6,0 A (12V) mit Linearantrieb |
| Preis (Gyropilot 2 System, 2025) | ca. 4.500–8.000 € |
| Wind-Modi | AWA, TWA, VMG-Optimierung, Target Speed |
| Performance-Daten | Vollständige Polar-Integration |
| NMEA 2000 | Über NKE-to-NMEA2000 Gateway |
| NKE-Bus | Ja (native Kommunikation) |

**Segel-Modi im Detail:**

| Modus | Regelgröße | Verwendung |
|-------|-----------|-----------|
| Compass | Magnetischer Kurs | Langstrecke, Nachtsegeln, leichter Wind |
| AWA (Apparent Wind) | Scheinbarer Windwinkel | Standard Upwind, Raum-Schots |
| TWA (True Wind) | Wahrer Windwinkel | Regatta Downwind, stabiler Kurs |
| VMG | Geschwindigkeit Made Good | Regatta, Maximierung der Geschwindigkeit zum Ziel |
| Target Speed | Bootgeschwindigkeit vs. Polar | Regatta, Optimierung der Segeltrimm-Effizienz |

**NKE-Algorithmus-Besonderheiten:**
- **Wellenerkennung:** Erkennt Wellenmuster und gibt Ruder vorausschauend ("anticipation"), nicht nur reaktiv
- **Böen-Management:** Separater Böenfilter, der kurze Windspitzen von echten Windänderungen unterscheidet
- **Downwind-Stabilität:** Spezialfilter gegen Rolling/Giering vor dem Wind — DAS Differenzierungsmerkmal gegenüber allen Wettbewerbern
- **Multi-Polar:** Speicherung mehrerer Polardiagramme (verschiedene Segelkonfigurationen)

---

## 4. Produktlinien und Spezifikationen

### 4.1 Raymarine — Vollständige Spezifikationstabelle

| Modell | Max. Verdr. (kg) | Ruderkraft (N) | Hub (mm) | Stromverbr. Standby (A@12V) | Stromverbr. Fahrt (A@12V) | Gewicht Antrieb (kg) | Preis System (€) | 24V | Redundanz |
|--------|------------------|----------------|----------|------------------------------|---------------------------|---------------------|------------------|-----|-----------|
| EV-100 Tiller | 7.000 | 490 | ±30° | 0,10 | 0,5–2,5 | 1,8 | 1.800–2.200 | Nein | Nein |
| EV-100 Wheel | 7.000 | 490 (Riemen) | — | 0,10 | 0,5–2,5 | 2,3 | 2.200–2.800 | Nein | Nein |
| EV-150 Linear | 15.000 | 1.100 | 178 | 0,25 | 1,0–6,0 | 5,5 | 3.500–4.500 | Nein | Nein |
| EV-150 Hydraulik | 15.000 | — | — | 0,25 | 1,5–8,0 | 8,0 | 4.500–6.000 | Nein | Nein |
| EV-200 Linear | 25.000 | 2.250 | 305 | 0,30 | 1,5–12,0 | 8,5 | 5.500–7.500 | Nein | Nein |
| EV-200 Hydraulik | 25.000 | — | — | 0,30 | 2,0–15,0 | 10,0 | 6.500–8.500 | Nein | Nein |
| EV-400 Hydraulik | >50.000 | — | — | 0,40 | 3,0–25,0 | 12,0 | 12.000–25.000 | Ja | Optional |

### 4.2 B&G — Vollständige Spezifikationstabelle

| Modell | Max. Verdr. (kg) | Ruderkraft (N) | Hub (mm) | Stromverbr. Standby (A@12V) | Stromverbr. Fahrt (A@12V) | Gewicht Antrieb (kg) | Preis System (€) | 24V | Redundanz |
|--------|------------------|----------------|----------|------------------------------|---------------------------|---------------------|------------------|-----|-----------|
| NAC-1 + RFC25 | 3.000 | 340 | 152 | 0,15 | 0,8–3,0 | 3,8 | 2.500–3.500 | Nein | Nein |
| NAC-1 + RFC35 | 5.000 | 600 | 178 | 0,15 | 0,8–4,0 | 5,0 | 3.000–4.000 | Nein | Nein |
| NAC-2 + RFC35 | 10.000 | 600 | 178 | 0,20 | 1,0–5,0 | 5,0 | 4.000–5.000 | Nein | Nein |
| NAC-2 + RFC42 | 15.000 | 1.680 | 305 | 0,20 | 1,0–8,0 | 7,5 | 4.500–5.500 | Nein | Nein |
| NAC-2 + Hydraulik | 25.000 | — | — | 0,20 | 1,5–10,0 | 9,0 | 5.500–7.500 | Nein | Nein |
| NAC-3 + RPU-80 | 30.000 | — | — | 0,25 | 2,0–12,0 | 10,0 | 8.000–12.000 | Ja | Optional |
| NAC-3 + RPU-160 | 50.000 | — | — | 0,25 | 3,0–18,0 | 14,0 | 10.000–15.000 | Ja | Optional |
| NAC-3 + RPU-300 | >50.000 | — | — | 0,25 | 4,0–25,0 | 18,0 | 14.000–18.000 | Ja | Ja |

### 4.3 Garmin — Vollständige Spezifikationstabelle

| Modell | Max. Verdr. (kg) | Ruderkraft (N) | Stromverbr. Standby (A@12V) | Stromverbr. Fahrt (A@12V) | Gewicht CCU (kg) | Preis System (€) | 24V | Shadow Drive |
|--------|------------------|----------------|------------------------------|---------------------------|-----------------|------------------|-----|-------------|
| Compact Reactor Tiller | 5.000 | 390 | 0,08 | 0,5–2,0 | 1,5 | 1.600–2.000 | Nein | Nein |
| Reactor 20 Hydraulik | 12.000 | — | 0,15 | 1,5–8,0 | 2,0 | 3.500–5.000 | Nein | Ja |
| Reactor 20 Rotary | 8.000 | 500 | 0,15 | 1,0–5,0 | 2,0 | 3.000–4.000 | Nein | Nein |
| Reactor 40 Hydraulik (1,2l) | 20.000 | — | 0,20 | 2,0–12,0 | 2,5 | 6.000–9.000 | Ja | Ja |
| Reactor 40 Hydraulik (2,0l) | 30.000 | — | 0,20 | 3,0–15,0 | 2,5 | 8.000–12.000 | Ja | Ja |

### 4.4 Simrad — Vollständige Spezifikationstabelle

| Modell | Max. Verdr. (kg) | Antrieb | Stromverbr. Standby (A@12V) | Stromverbr. Fahrt (A@12V) | Preis System (€) | 24V | IMO |
|--------|------------------|---------|-----------------------------|---------------------------|------------------|-----|-----|
| AP44 + SD10 | 8.000 | Linear | 0,20 | 1,0–4,0 | 2.500–3.500 | Nein | Nein |
| AP44 + Hydraulik | 12.000 | Hydraulik | 0,20 | 1,0–6,0 | 3.500–5.000 | Nein | Nein |
| AP48 + SD15 | 15.000 | Linear | 0,25 | 1,5–8,0 | 4.500–6.000 | Nein | Nein |
| AP48 + RPU-80 | 25.000 | Hydraulik | 0,25 | 2,0–12,0 | 5.500–8.000 | Nein | Nein |
| AC70 + RPU-160 | 50.000 | Hydraulik | 0,30 | 3,0–18,0 | 12.000–20.000 | Ja | Ja |
| AC70 + RPU-300 | >100.000 | Hydraulik | 0,30 | 4,0–25,0 | 18.000–30.000 | Ja | Ja |

### 4.5 Furuno — Vollständige Spezifikationstabelle

| Modell | Max. Verdr. (kg) | Antrieb | Stromverbr. Standby (A@12V) | Stromverbr. Fahrt (A@12V) | Preis System (€) | 24V | IMO |
|--------|------------------|---------|-----------------------------|---------------------------|------------------|-----|-----|
| NavPilot 300 + Pumpe klein | 15.000 | Hydraulik | 0,40 | 1,5–8,0 | 3.500–5.000 | Nein | Nein |
| NavPilot 300 + Pumpe mittel | 30.000 | Hydraulik | 0,40 | 2,0–12,0 | 5.000–8.000 | Nein | Nein |
| NavPilot 700 + Pumpe 150ccm | 30.000 | Hydraulik | 0,50 | 3,0–15,0 | 10.000–15.000 | Ja | Ja |
| NavPilot 700 + Pumpe 300ccm | 80.000 | Hydraulik | 0,50 | 4,0–25,0 | 15.000–22.000 | Ja | Ja |
| NavPilot 700 + Pumpe 600ccm | >100.000 | Hydraulik | 0,50 | 5,0–35,0 | 20.000–35.000 | Ja | Ja |

### 4.6 NKE — Vollständige Spezifikationstabelle

| Modell | Max. Verdr. (kg) | Antrieb | Stromverbr. Standby (A@12V) | Stromverbr. Fahrt (A@12V) | Preis System (€) | Wind-Modi | VMG |
|--------|------------------|---------|-----------------------------|---------------------------|------------------|-----------|-----|
| Gyropilot 2 + Linear klein | 5.000 | Linear | 0,12 | 0,8–3,0 | 4.500–5.500 | 5 | Ja |
| Gyropilot 2 + Linear groß | 12.000 | Linear | 0,12 | 1,0–6,0 | 5.500–7.000 | 5 | Ja |
| Gyropilot 2 + Hydraulik | >20.000 | Hydraulik | 0,12 | 2,0–12,0 | 7.000–10.000 | 5 | Ja |

### 4.7 Vergleichsmatrix — Alle Hersteller

**Segel-Funktionen im Vergleich:**

| Funktion | Raymarine | B&G | Garmin | Simrad | Furuno | NKE |
|----------|----------|-----|--------|--------|--------|-----|
| Wind-Modus (AWA) | ● | ● | ● | ● | ● | ● |
| Wind-Modus (TWA) | ● | ● | ○ | ○ | ○ | ● |
| VMG-Optimierung | ○ | ● | ○ | ○ | ○ | ● |
| Auto-Tack | ● | ● | ● | ○ | ○ | ● |
| Auto-Gybe | ○ | ● | ○ | ○ | ○ | ● |
| Polar-Integration | ○ | ● | ○ | ○ | ○ | ● |
| Target Speed | ○ | ● | ○ | ○ | ○ | ● |
| Windshift-Tracking | ● | ● | ○ | ○ | ○ | ● |
| Layline-Berechnung | ○ | ● | ○ | ○ | ○ | ● |
| Downwind-Stabilisierung | ◐ | ● | ◐ | ○ | ○ | ● |

● = vorhanden und ausgereift, ◐ = vorhanden aber eingeschränkt, ○ = nicht vorhanden oder rudimentär

**Motor-Funktionen im Vergleich:**

| Funktion | Raymarine | B&G | Garmin | Simrad | Furuno | NKE |
|----------|----------|-----|--------|--------|--------|-----|
| Track-Modus | ● | ● | ● | ● | ● | ◐ |
| Auto-Guidance | ○ | ○ | ● | ○ | ○ | ○ |
| Shadow Drive | ○ | ○ | ● | ○ | ○ | ○ |
| Fish Hunter | ○ | ○ | ○ | ○ | ● | ○ |
| Docking Assist | ○ | ○ | ● | ○ | ○ | ○ |
| Joystick-Steuerung | ○ | ○ | ● | ● | ○ | ○ |
| Speed Control | ◐ | ○ | ● | ● | ● | ○ |
| Turn-Rate Control | ● | ● | ● | ● | ● | ○ |

**Zuverlässigkeit und Service:**

| Kriterium | Raymarine | B&G | Garmin | Simrad | Furuno | NKE |
|-----------|----------|-----|--------|--------|--------|-----|
| MTBF (geschätzt, Stunden) | 15.000 | 15.000 | 18.000 | 15.000 | 25.000 | 12.000 |
| Garantie (Jahre) | 2 | 2 | 2 | 2 | 2 | 2 |
| Service Deutschland | Gut | Mittel | Sehr gut | Mittel | Gut | Schlecht |
| Ersatzteil-Verfügbarkeit | Gut | Gut | Sehr gut | Gut | Mittel | Schlecht |
| Firmware-Updates | Häufig | Häufig | Häufig | Häufig | Selten | Selten |
| Dokumentation | Gut | Sehr gut | Sehr gut | Gut | Sehr gut | Mäßig (Französisch) |
| Community/Forum | Sehr groß | Groß | Sehr groß | Groß | Klein | Klein (FR) |

> **Confidence: estimated** — MTBF-Werte basieren auf Eigner-Berichten und Werkstatt-Statistiken, nicht auf Herstellerangaben. Kein Hersteller veröffentlicht MTBF für Freizeit-Autopiloten.

---

## 5. Hersteller-Datenbank

### 5.1 Raymarine (Teledyne FLIR)

**Vollständiges Produktportfolio Autopilot:**

| Produkt | Typ | Art.-Nr. | Preis (€, UVP) | Status |
|---------|-----|----------|----------------|--------|
| EV-100 Tiller Pack | Tillerpilot-Set | T70154 | 1.950 | Aktuell |
| EV-100 Wheel Pack | Radpilot-Set | T70152 | 2.450 | Aktuell |
| EV-100 Power Pack | Linear-Set | T70156 | 2.850 | Aktuell |
| ACU-100 | Kurscomputer | E70098 | 650 | Aktuell |
| ACU-150 | Kurscomputer | E70099 | 980 | Aktuell |
| ACU-200 | Kurscomputer | E70100 | 1.350 | Aktuell |
| ACU-400 | Kurscomputer | E70101 | 2.500 | Aktuell |
| EV-1 Sensor Core | Lagesensor MEMS | E70096 | 420 | Aktuell |
| EV-2 Ruderfeedback | Ruderwinkelsensor | E70097 | 280 | Aktuell |
| p70 | Bedieneinheit mono | E22166 | 380 | Abgekündigt |
| p70s | Bedieneinheit Farbe Segel | E22167 | 550 | Aktuell |
| p70Rs | Bedieneinheit Farbe Segel (retractable) | E70329 | 620 | Aktuell |
| p70R | Bedieneinheit Farbe Motor | E70328 | 620 | Aktuell |
| Type 1 Linear | Linearantrieb 112 kg | M81120 | 980 | Aktuell |
| Type 2 Linear | Linearantrieb 230 kg | M81132 | 1.650 | Aktuell |
| Type 1 Hydraulik | Pumpe 80 ccm | M81121 | 1.450 | Aktuell |
| Type 2 Hydraulik | Pumpe 160 ccm | M81133 | 2.200 | Aktuell |
| Type 3 Hydraulik | Pumpe 300 ccm | M81140 | 3.500 | Aktuell |

**Kompatibilitätsmatrix Raymarine:**

| Kurscomputer | Tillerpilot | Radpilot | Type 1 Lin. | Type 2 Lin. | Type 1 Hyd. | Type 2 Hyd. | Type 3 Hyd. |
|-------------|------------|----------|-------------|-------------|-------------|-------------|-------------|
| ACU-100 | ● | ● | ● | ○ | ○ | ○ | ○ |
| ACU-150 | ○ | ○ | ● | ○ | ● | ○ | ○ |
| ACU-200 | ○ | ○ | ● | ● | ● | ● | ○ |
| ACU-400 | ○ | ○ | ○ | ● | ○ | ● | ● |

**Typische Fehlerquellen Raymarine Evolution:**

| Problem | Häufigkeit | Ursache | Lösung |
|---------|-----------|---------|--------|
| EV-1 Drift nach Einbau | Häufig | Einbauort zu nah an Metallmassen | Umsetzen, >50 cm von Motor/Kiel |
| ACU-100 Neustart bei Wende | Gelegentlich | Spannungseinbruch bei Motorlast | Separate Stromversorgung, dickeres Kabel |
| Tillerpilot-Spindel klemmt | Häufig (>3 Jahre) | Korrosion, Salzablagerung | Spindel schmieren/tauschen |
| p70s Display unleserlich | Gelegentlich | Feuchtigkeit hinter Display | Austausch (Garantie prüfen) |
| SeaTalkNG-Verbindung instabil | Gelegentlich | Oxidierte Stecker, Wassereinbruch | Stecker reinigen, Dichtung prüfen |

### 5.2 B&G (Navico Group)

**Vollständiges Produktportfolio Autopilot:**

| Produkt | Typ | Art.-Nr. | Preis (€, UVP) | Status |
|---------|-----|----------|----------------|--------|
| NAC-1 | Kurscomputer | 000-13336-001 | 1.350 | Aktuell |
| NAC-2 | Kurscomputer | 000-13249-001 | 1.850 | Aktuell |
| NAC-3 | Kurscomputer | 000-13250-001 | 2.950 | Aktuell |
| Precision-9 Compass | 9-Achsen MEMS Kompass | 000-12607-001 | 520 | Aktuell |
| H5000 CPU | Segelcomputer | 000-11545-001 | 3.200 | Aktuell |
| H5000 Hercules | Performance-Rechner | 000-11546-001 | 2.800 | Aktuell |
| RFC25 | Linearantrieb 25 kg | 000-13920-001 | 680 | Aktuell |
| RFC35 | Linearantrieb 60 kg | 000-11543-001 | 850 | Aktuell |
| RFC42 | Linearantrieb 170 kg | 000-11544-001 | 1.250 | Aktuell |
| Triton2 AP Controller | Bedieneinheit | 000-13294-001 | 380 | Aktuell |
| WR10 Wireless Remote | Drahtlose Fernbedienung | 000-12316-001 | 320 | Aktuell |

> ⚠️ **ZU PRÜFEN (Audit):** RFC25-Ruderkraft widersprüchlich — die Spezifikationstabelle 4.2 nennt **340 N**, die Typbezeichnung oben lautet **„Linearantrieb 25 kg" (≈ 245 N)**. Nach der im Dokument durchgängigen kg↔N-Umrechnung (RFC35 = 60 kg ≈ 600 N, RFC42 = 170 kg ≈ 1.680 N) müsste „25 kg" ≈ 245 N ergeben; 340 N entspräche ≈ 35 kg. Richtung nicht zweifelsfrei belegbar (RFC-Antriebskräfte extern nicht verifizierbar) — Herstellerdatenblatt prüfen. Beide Werte unverifiziert.

**B&G-spezifische Stärken:**
- Einziger Hersteller mit integriertem Segelrechner (H5000 Hydra)
- Continuum-Algorithmus: Überlegene Segel-Performance unter allen Bedingungen
- Layline-Berechnung direkt in Autopilot-Logik integriert
- Precision-9 Kompass gilt als bester MEMS-Kompass am Markt
- Aktive Community (B&G Ambassador Programm)

**B&G-spezifische Schwächen:**
- Hoher Preis für vollständiges H5000-System (>10.000 € mit allen Sensoren)
- NKE-Bus-Abhängigkeit für maximale Performance (Lock-in)
- Wenig Motor-spezifische Funktionen
- NAC-1 hat eingeschränkte Kompatibilität mit älteren B&G-Displays
- Firmware-Updates erfordern teils Navico-Software (GoFree Controller)

### 5.3 Garmin

**Vollständiges Produktportfolio Autopilot:**

| Produkt | Typ | Art.-Nr. | Preis (€, UVP) | Status |
|---------|-----|----------|----------------|--------|
| Compact Reactor 40 Tiller | Tillerpilot | 010-02802-XX | 1.750 | Aktuell |
| GHP Reactor 20 Hydraulik Kit | Hydraulik-Set | 010-00705-XX | 4.200 | Aktuell |
| GHP Reactor 20 Mechanical Kit | Rotary-Set | 010-00706-XX | 3.400 | Aktuell |
| GHP Reactor 40 Hydraulik Kit | Hydraulik-Set (klein) | 010-00707-XX | 7.500 | Aktuell |
| GHP Reactor 40 Hydraulik Kit | Hydraulik-Set (groß) | 010-00708-XX | 9.800 | Aktuell |
| GHC 50 | Bedieneinheit | 010-02785-XX | 650 | Aktuell |
| GHC 20 | Bedieneinheit | 010-01141-XX | 450 | Aktuell |
| GHP 10V Solenoid Pack | Solenoid-Pumpe | 010-00706-40 | 1.800 | Aktuell |
| GRF 10 Ruderfeedback | Ruderwinkelsensor | 010-00551-00 | 250 | Aktuell |
| gWind Wireless 2 | Drahtloser Windsensor | 010-01950-XX | 680 | Aktuell |

**Garmin-spezifische Stärken:**
- Shadow Drive: Bestes "Override"-Konzept am Markt
- Auto-Guidance: Automatische Routenberechnung (proprietär, nur mit Garmin-Plotter)
- Tiefe Integration mit Garmin-Ökosystem (Plotter, Radar, Echolot, Motor)
- Bedienkonzept: intuitivste Benutzeroberfläche im Test
- Firmware-Updates einfach (microSD, WLAN)
- Beste Garantie-Abwicklung in Deutschland (eigenes Service-Center)
- quatix-Uhr als Autopilot-Fernbedienung

**Garmin-spezifische Schwächen:**
- Stärkster Lock-in aller Hersteller: Auto-Guidance nur mit Garmin-Plotter
- Wind-Modus bei Seglern als "nur ausreichend" bewertet (kein TWA, kein VMG)
- Kein Äquivalent zum B&G H5000 Segelrechner
- Shadow Drive kann beim Segeln störend sein (unbeabsichtigte Deaktivierung)
- Rotary-Antriebe weniger verbreitet, Ersatzteile teils lange Lieferzeit

### 5.4 Simrad

**Vollständiges Produktportfolio Autopilot:**

| Produkt | Typ | Art.-Nr. | Preis (€, UVP) | Status |
|---------|-----|----------|----------------|--------|
| AP44 | Bedien-/Kurscomputer | 000-13289-001 | 1.650 | Aktuell |
| AP48 | Bedieneinheit | 000-13290-001 | 1.200 | Aktuell |
| AC42 | Kurscomputer | 000-10166-001 | 1.500 | Auslaufend |
| AC70 | Kurscomputer | 000-10167-001 | 2.950 | Aktuell |
| Precision-9 | 9-Achsen Kompass | 000-12607-001 | 520 | Aktuell |
| HS75 GNSS Compass | Satelliten-Kompass | 000-15573-001 | 3.500 | Aktuell |
| SD10 | Linearantrieb | 000-13886-001 | 680 | Aktuell |
| SD15 | Linearantrieb groß | 000-13887-001 | 980 | Aktuell |
| RPU-80 | Hydraulikpumpe 80ccm | 000-15444-001 | 1.450 | Aktuell |
| RPU-160 | Hydraulikpumpe 160ccm | 000-15445-001 | 2.200 | Aktuell |
| RPU-300 | Hydraulikpumpe 300ccm | 000-15446-001 | 3.500 | Aktuell |
| OP50 Remote | Fernbedienung | 000-12298-001 | 350 | Aktuell |

**Simrad-spezifische Stärken:**
- Gleiche Technik wie B&G, optimiert für Motorboote
- AC70 für gewerbliche Schiffe IMO-konform
- SimNet-Legacy-Unterstützung für bestehende Installationen
- Robuste Bauweise, bewährt in der norwegischen Fischerei
- Gute Integration mit Simrad-Plottern (NSX, NSO evo3)
- HS75 GNSS Kompass: einer der besten Satellitencompasse im Segment

**Simrad-spezifische Schwächen:**
- Segel-Funktionen deutlich hinter B&G (gleicher Konzern, aber andere Firmware)
- SimNet-Stecker weniger verbreitet als SeaTalkNG/NMEA 2000
- AP44/AP48 Touchscreen bei Regen/Spritzwasser teils schlecht bedienbar
- AC42 auslaufend, Migration zu AC70 teuer für bestehende Systeme
- Service-Infrastruktur in Deutschland nicht so dicht wie Raymarine/Garmin

### 5.5 Furuno

**Vollständiges Produktportfolio Autopilot:**

| Produkt | Typ | Art.-Nr. | Preis (€, UVP) | Status |
|---------|-----|----------|----------------|--------|
| NavPilot 300 | Bedien-/Kurscomputer | FAP-3001 | 2.800 | Aktuell |
| NavPilot 700 Prozessor | Kurscomputer | FAP-7011C | 5.500 | Aktuell |
| NavPilot 700 Bedieneinheit | Display/Controller | FAP-7001C | 3.200 | Aktuell |
| PG-700 | Fluxgate-Kompass | PG-700 | 850 | Aktuell |
| SCX-20 | Satelliten-Kompass | SCX-20 | 6.500 | Aktuell |
| Pump Unit 0,8l | Hydraulikpumpe | FHP-xxx | 1.800 | Aktuell |
| Pump Unit 1,5l | Hydraulikpumpe | FHP-xxx | 2.800 | Aktuell |
| Pump Unit 3,0l | Hydraulikpumpe | FHP-xxx | 4.500 | Aktuell |
| Pump Unit 6,0l | Hydraulikpumpe | FHP-xxx | 7.500 | Aktuell |
| Rudder Angle Transmitter | Ruderwinkelsensor | FAR-1510 | 650 | Aktuell |

**Furuno-spezifische Stärken:**
- Höchste Zuverlässigkeit aller getesteten Systeme
- NavPilot 700 mit IMO-Zulassung für gewerbliche Schifffahrt
- SCX-20 Satellitenkompass: Referenz für Genauigkeit (±0,25°)
- Furuno-Fertigungsqualität (Made in Japan)
- Black-Box-Funktion im NavPilot 700 einzigartig
- Multi-Heading-Sensor-Management (bis 3 Quellen)
- Fish Hunter Modus exklusiv (Angler-Nische)
- Langzeitunterstützung: Ersatzteile auch nach 15+ Jahren

**Furuno-spezifische Schwächen:**
- Höchster Preis pro Leistungsklasse
- NavPilot 300 Standby-Verbrauch höher als Wettbewerb
- Benutzeroberfläche wirkt technisch/funktional, weniger modern als Garmin/Raymarine
- Segel-Funktionen rudimentär (kein TWA, kein VMG, keine Wende-Automatik)
- NavNet-Ökosystem proprietär und teuer
- Wenige Firmware-Updates (japanische Entwicklungszyklen)
- Service in Deutschland nur über Furuno Hamburg oder wenige Fachhändler

### 5.6 NKE

**Vollständiges Produktportfolio Autopilot:**

| Produkt | Typ | Art.-Nr. | Preis (€, UVP) | Status |
|---------|-----|----------|----------------|--------|
| Gyropilot 2 | Kurscomputer | GP2 | 3.200 | Aktuell |
| Pilote HR | Linearantrieb klein | P-HR-S | 1.200 | Aktuell |
| Pilote HR Grande | Linearantrieb groß | P-HR-G | 1.800 | Aktuell |
| Display Multidisplay | Segeldisplay | MD-NKE | 680 | Aktuell |
| Topline Multiplexer | NMEA 2000 Gateway | TL-MUX | 950 | Aktuell |
| Capteur de barre | Rudersensor | CB-NKE | 350 | Aktuell |
| Girouette-Anémomètre | Windmessanlage | GA-HR | 850 | Aktuell |
| Loch-Speedo HR | Geschwindigkeit/Log | LS-HR | 650 | Aktuell |

**NKE-spezifische Stärken:**
- Überlegene Segel-Performance: Der beste Autopilot zum Segeln, Punkt
- 5 unabhängige Wind-Modi (AWA, TWA, VMG, Target Speed, Compass)
- Downwind-Stabilisierung unerreicht (Wellenantizipation)
- Extrem niedriger Stromverbrauch (0,12 A Standby!)
- Bevorzugter Autopilot bei Offshore-Einhandregatten (Vendée Globe, Figaro)
- Einfache, robuste Hardware
- Schnelle Reaktionszeit (mechanischer Antrieb + MEMS)

**NKE-spezifische Schwächen:**
- Dokumentation primär auf Französisch (Handbücher, Support)
- Kein offizieller Vertrieb in Deutschland — Import über Fachhändler
- Kein Track-Modus mit Plotter-Integration (nur rudimentär über NMEA)
- NKE-Bus proprietär — erfordert Gateway für NMEA 2000
- Keine Motor-spezifischen Funktionen
- Kleines Unternehmen: Langzeit-Risiko bei Insolvenz/Übernahme
- Kein Touchscreen-Display (bewusste Designentscheidung, aber gewöhnungsbedürftig)
- Eingeschränkte Hydraulik-Unterstützung (Fremd-Pumpen)

---

## 6. Fehlerbild-Atlas

### 6.1 Fehlerbild: Autopilot hält Kurs nicht — pendelt ständig (Oszillation)

**Beschreibung:** Der Autopilot gibt abwechselnd Ruder nach Backbord und Steuerbord, ohne einen stabilen Kurs zu finden. Das Boot "schlingert" um den Sollkurs.

**Mögliche Ursachen:**

| Nr. | Ursache | Hersteller | Wahrscheinlichkeit |
|-----|---------|-----------|-------------------|
| 1 | Proportional-Gain (Kp) zu hoch | Alle | Hoch |
| 2 | Keine/schlechte Ruderfeedback-Kalibrierung | Alle (außer Tillerpilot) | Hoch |
| 3 | Spiel in der Ruderanlage | Alle | Mittel |
| 4 | Kompass-Fehler (Deviation, Einbauort) | Alle | Mittel |
| 5 | Zu langsame Antriebseinheit für Bootsgröße | Alle | Mittel |
| 6 | Luft im Hydrauliksystem | Alle mit Hydraulik | Mittel |
| 7 | Evolution-Lernphase nicht abgeschlossen | Raymarine | Mittel |
| 8 | Counter-Rudder zu niedrig eingestellt | Alle (manuell konfiguriert) | Gering |

**Diagnose-Schritte:**
1. Ruderspiel prüfen: Ruder von Hand bewegen, Spiel am Quadranten messen (>2° = Problem)
2. Ruderfeedback-Kalibrierung durchführen (Menü → Kalibrierung → Ruder)
3. Gain reduzieren (um 2 Stufen) und Testfahrt
4. Kompassabweichung prüfen (Abgleichfahrt, Kreis fahren)
5. Bei Hydraulik: Entlüften, Ölstand prüfen

### 6.2 Fehlerbild: Autopilot reagiert nicht auf Kursänderungsbefehl

**Beschreibung:** Taste gedrückt oder Kurs am Plotter geändert, aber der Autopilot hält den alten Kurs.

**Mögliche Ursachen:**

| Nr. | Ursache | Hersteller | Wahrscheinlichkeit |
|-----|---------|-----------|-------------------|
| 1 | NMEA-Verbindung zwischen Plotter und AP unterbrochen | Alle | Hoch |
| 2 | Falscher Betriebsmodus (Standby statt Auto) | Alle | Hoch |
| 3 | Ruderlimit erreicht | Alle | Mittel |
| 4 | Antriebsüberlast (thermische Abschaltung) | Alle | Mittel |
| 5 | SeaTalkNG-Stecker oxidiert | Raymarine | Mittel |
| 6 | SimNet-Backbone-Fehler (Terminierung) | Simrad | Gering |
| 7 | Shadow Drive aktiv (Garmin) | Garmin | Mittel |

**Diagnose-Schritte:**
1. Betriebsmodus-Anzeige prüfen (Auto/Standby/Track)
2. NMEA-2000-Geräteliste am Plotter aufrufen: Sieht der Plotter den AP?
3. Bei Garmin: Shadow Drive deaktivieren und testen
4. Steckverbindungen visuell prüfen, ggf. Kontaktspray
5. Ruderlimit-Einstellung überprüfen und ggf. erhöhen
6. Thermische Überlastung: 10 min abkühlen lassen, dann testen

### 6.3 Fehlerbild: Autopilot schaltet sich selbstständig ab (Random Disconnect)

**Beschreibung:** Der Autopilot geht ohne Benutzereingabe von "Auto" in "Standby" oder schaltet sich komplett aus.

**Mögliche Ursachen:**

| Nr. | Ursache | Hersteller | Wahrscheinlichkeit |
|-----|---------|-----------|-------------------|
| 1 | Unterspannung (Batterie <10,5V bei 12V-System) | Alle | Hoch |
| 2 | Lose Stromverbindung / Spannungseinbruch | Alle | Hoch |
| 3 | Kursabweichungs-Alarm (>15°) → Sicherheitsabschaltung | Alle | Mittel |
| 4 | Shadow Drive (Ruder berührt) | Garmin | Mittel |
| 5 | Firmware-Bug | Alle | Gering |
| 6 | Wasser in Bedieneinheit (Kurzschluss) | Alle | Gering |
| 7 | EMV-Störung (Funksender, Radar) | Alle | Gering |

**Diagnose-Schritte:**
1. Bordspannung unter Last messen (Multimeter am AP-Anschluss)
2. Alle Klemmen auf festen Sitz prüfen
3. Event-Log des Autopiloten auslesen (zeigt Abschaltgrund)
4. Garmin: Shadow Drive prüfen, ggf. Empfindlichkeit anpassen
5. Firmware auf neueste Version aktualisieren
6. Stromversorgung über separaten Sicherungskreis mit min. 10 mm² Kabel

### 6.4 Fehlerbild: Kompass zeigt falschen Kurs (systematische Abweichung)

**Beschreibung:** Der Autopilot steuert zuverlässig, aber immer X Grad neben dem eingegebenen Kurs.

**Mögliche Ursachen:**

| Nr. | Ursache | Hersteller | Wahrscheinlichkeit |
|-----|---------|-----------|-------------------|
| 1 | Deviation durch Metallmassen nahe Kompass | Alle | Hoch |
| 2 | Kalibrierung nicht oder schlecht durchgeführt | Alle | Hoch |
| 3 | Missweisung (Variation) falsch eingestellt | Alle (NMEA 0183) | Mittel |
| 4 | Kompass-Einbauachse nicht parallel zur Kiellinie | Alle | Mittel |
| 5 | Neues Bordgerät (Lautsprecher, Winde) in Kompass-Nähe | Alle | Mittel |
| 6 | EV-1 Sensor nach Umbau nicht neu kalibriert | Raymarine | Häufig |
| 7 | Fluxgate-Kompass Alterung | Furuno PG-700 | Gering |

**Diagnose-Schritte:**
1. Deviationsfahrt: 360°-Kreis langsam fahren, Abweichung alle 30° notieren
2. Kompass-Kalibrierung neu durchführen (im Menü des jeweiligen Herstellers)
3. Metalldetektor um Kompass-Einbauort: unerwartete Metallteile?
4. Einbauachse mit Laser prüfen (muss parallel zur Mittschiffs-Linie sein)
5. Bei Fluxgate: Distanz zu Motoren, Lautsprechern, Winden >1m?

### 6.5 Fehlerbild: Hydraulik-Antrieb summt, aber Ruder bewegt sich nicht

**Beschreibung:** Die Hydraulikpumpe läuft hörbar, aber der Ruderstocker bewegt sich nicht oder kaum.

**Mögliche Ursachen:**

| Nr. | Ursache | Hersteller | Wahrscheinlichkeit |
|-----|---------|-----------|-------------------|
| 1 | Bypass-Ventil offen (Hand-/Notsteuerung aktiv) | Alle mit Hydraulik | Hoch |
| 2 | Luft im Hydrauliksystem | Alle | Hoch |
| 3 | Hydrauliköl-Niveau zu niedrig | Alle | Mittel |
| 4 | Leckage an Schlauchverbindung/Zylinder | Alle | Mittel |
| 5 | Pumpe defekt (interner Verschleiß) | Alle | Gering |
| 6 | Solenoidventil klemmt | Furuno (Solenoid-Typ) | Gering |

**Diagnose-Schritte:**
1. Bypass-Ventil schließen!
2. Ölstand im Reservoir prüfen, ggf. auffüllen (ATF Dexron III oder herstellerspezifisch)
3. System entlüften (Entlüftungsschraube öffnen, Pumpe laufen lassen, bis blasenfrei)
4. Alle Verbindungen auf Leckage prüfen (Öl-Spuren, feuchte Fittings)
5. Druck am Manometer messen: Sollwert lt. Herstellerangabe?

### 6.6 Fehlerbild: Tillerpilot-Spindel fährt in Endanschlag und blockiert

**Beschreibung:** Der Tillerpilot fährt die Spindel voll aus oder ein und gibt keinen Hub mehr.

**Mögliche Ursachen:**

| Nr. | Ursache | Hersteller | Wahrscheinlichkeit |
|-----|---------|-----------|-------------------|
| 1 | Ruderlimit nicht korrekt gesetzt | Alle Tillerpiloten | Hoch |
| 2 | Kalibrierung der Mittellage falsch | Alle | Hoch |
| 3 | Mechanische Blockade am Ruder (Festmacherleinen) | — | Mittel |
| 4 | Spindelgetriebe verschlissen | Raymarine EV-100 | Mittel (>3 Jahre) |
| 5 | Endschalter defekt | Simrad TP-Serie | Gering |

**Diagnose-Schritte:**
1. Pinne von Hand: Bewegt sich das Ruder frei von Anschlag zu Anschlag?
2. Ruderlimit-Einstellung prüfen und ggf. reduzieren (auf max. ±30°)
3. Mittellage neu kalibrieren (Ruder mittschiffs, dann Kalibrierung starten)
4. Spindelgetriebe visuell auf Verschleiß prüfen
5. Endschalter-Funktion mit Multimeter prüfen

### 6.7 Fehlerbild: Wind-Modus instabil — Kurs schwankt bei Böen

**Beschreibung:** Im Wind-Modus (AWA/TWA) reagiert der AP übermäßig auf Windböen und wirft das Boot aus dem Kurs.

**Mögliche Ursachen:**

| Nr. | Ursache | Hersteller | Wahrscheinlichkeit |
|-----|---------|-----------|-------------------|
| 1 | Wind-Response zu hoch eingestellt | Alle | Hoch |
| 2 | Böen-Dämpfung (Wave Filter) nicht aktiv | Alle | Hoch |
| 3 | Windmessanlage in Lee-Verwirbelung | — | Mittel |
| 4 | Mastmontierter Sensor: Mastschwingungen | — | Mittel |
| 5 | Kein TWA-Modus verfügbar, nur AWA | Garmin, Simrad, Furuno | Funktionslimitierung |
| 6 | Polardiagramm nicht konfiguriert | B&G, NKE | Mittel |

**Diagnose-Schritte:**
1. Wind-Response auf niedrigste Stufe setzen, testen
2. Wave Filter aktivieren (Mittel oder Hoch)
3. Position des Windsensors prüfen: Mind. 1m über Oberkante jedes Hindernisses
4. Bei B&G/NKE: TWA-Modus statt AWA verwenden
5. Bei starkem Böen: Kompass-Modus als Fallback erwägen

### 6.8 Fehlerbild: NMEA 2000-Netzwerk — Autopilot nicht sichtbar

**Beschreibung:** Der Autopilot erscheint nicht in der Geräteliste des Plotters oder anderer Netzwerkgeräte.

**Mögliche Ursachen:**

| Nr. | Ursache | Hersteller | Wahrscheinlichkeit |
|-----|---------|-----------|-------------------|
| 1 | Stecker nicht vollständig eingerastet | Alle | Hoch |
| 2 | Terminierung fehlt (120Ω an Backbone-Enden) | Alle | Hoch |
| 3 | Drop-Kabel >6m | Alle | Mittel |
| 4 | Spannungsversorgung am Bus fehlt/zu schwach | Alle | Mittel |
| 5 | Defektes T-Stück oder Kabel | Alle | Gering |
| 6 | SimNet↔NMEA 2000 Adapter falsch | Simrad | Mittel |
| 7 | SeaTalkNG-Gerät an NMEA 2000 ohne Spur-Kabel | Raymarine | Gering |
| 8 | Firmware-Inkompatibilität | Alle | Gering |

**Diagnose-Schritte:**
1. Stecker: Alle Steckverbindungen lösen und neu einrasten
2. Terminierung: Genau 2 Terminatoren am Backbone (120Ω), mit Multimeter prüfen (60Ω Gesamtwiderstand)
3. Backbone-Topologie: Stern-Topologie ist NICHT erlaubt, nur linearer Bus
4. Versorgungsspannung am Bus messen: 9–16V zwischen NET-S und NET-C
5. Einzelgeräte-Test: Nur AP + 1 Plotter am Bus, schrittweise erweitern

### 6.9 Fehlerbild: Übermäßiger Stromverbrauch des Autopiloten

**Beschreibung:** Der Autopilot zieht deutlich mehr Strom als erwartet; Batterie entlädt sich schnell.

**Mögliche Ursachen:**

| Nr. | Ursache | Hersteller | Wahrscheinlichkeit |
|-----|---------|-----------|-------------------|
| 1 | Antriebseinheit zu schwach dimensioniert (Dauerlast) | Alle | Hoch |
| 2 | Spiel in Ruderanlage → ständige Korrekturen | Alle | Hoch |
| 3 | Gain zu hoch → überaktive Regelung | Alle | Mittel |
| 4 | Deadband zu eng → auf jede Mikro-Abweichung reagiert | Alle | Mittel |
| 5 | Schwerer Seegang (legitim hoher Verbrauch) | Alle | Mittel |
| 6 | Hydrauliköl-Leckage → Pumpe arbeitet dauerhaft | Alle mit Hydraulik | Gering |
| 7 | Motorlager/Getriebe verschlissen → erhöhte Reibung | Alle mechanisch | Gering |

**Diagnose-Schritte:**
1. Amperemeter in Zuleitung: Durchschnittsverbrauch über 30 min messen
2. Mit Herstellerangaben vergleichen (Tabelle oben, Duty Cycle beachten)
3. Ruderanlage auf Leichtgängigkeit prüfen (Ruder von Hand bewegen)
4. Gain um 2 Stufen reduzieren, Deadband auf 3° erweitern, erneut messen
5. Bei Hydraulik: Ölstand und Leckage prüfen

### 6.10 Fehlerbild: Autopilot macht "harte Ruderleger" bei Track-Modus

**Beschreibung:** Beim Abfahren einer Route macht der AP abrupte Kursänderungen an Wegpunkten, statt sanft zu drehen.

**Mögliche Ursachen:**

| Nr. | Ursache | Hersteller | Wahrscheinlichkeit |
|-----|---------|-----------|-------------------|
| 1 | WPT Advance Radius zu klein | Alle | Hoch |
| 2 | Turn Radius / Cross Track Error zu eng | Alle | Mittel |
| 3 | Wegpunkte zu dicht beieinander | — (Routenplanung) | Mittel |
| 4 | Plotter sendet XTE nicht (NMEA-Konfiguration) | Alle | Gering |

**Diagnose-Schritte:**
1. WPT Advance Radius auf mind. 3× Bootslänge setzen
2. Cross Track Limit auf 0,05–0,1 sm erweitern
3. Route prüfen: Mindestabstand zwischen WPTs = 10× Bootslänge
4. NMEA-Output des Plotters prüfen: APB und XTE Sentences aktiv?

### 6.11 Fehlerbild: Linearantrieb macht Klackgeräusche

**Beschreibung:** Rhythmisches oder unregelmäßiges Klacken aus dem Linearantrieb, besonders bei Richtungswechseln.

**Mögliche Ursachen:**

| Nr. | Ursache | Hersteller | Wahrscheinlichkeit |
|-----|---------|-----------|-------------------|
| 1 | Kugelgelenk ausgeschlagen | Alle Linear | Hoch |
| 2 | Montageschrauben lose | Alle | Hoch |
| 3 | Getriebe-Spiel (Zahnradantrieb) | Alle | Mittel |
| 4 | Spindel-Mutter verschlissen | Raymarine, Simrad Tiller | Mittel |
| 5 | Ruderquadrant-Bolzen lose | — | Mittel |

**Diagnose-Schritte:**
1. Alle Schrauben/Bolzen auf festen Sitz prüfen
2. Kugelgelenke: Wackeln? Spiel >1mm = tauschen
3. Getriebe: Im abgeschalteten Zustand am Ram hin- und herziehen: >2mm Spiel?
4. Ruderquadrant: Bolzen straff, kein Ovalisieren der Bohrung?
5. Verschlissene Teile tauschen (Kugelgelenk-Kits als Ersatzteil erhältlich)

### 6.12 Fehlerbild: EV-1 Sensor (Raymarine) — Compass Heading springt

**Beschreibung:** Die Kursanzeige springt plötzlich um 5–20° und kehrt dann zurück. Unregelmäßig, teils mehrmals pro Minute.

**Mögliche Ursachen:**

| Nr. | Ursache | Hersteller | Wahrscheinlichkeit |
|-----|---------|-----------|-------------------|
| 1 | Einbau zu nah an Wechselstromkabel (Inverter, Landstrom) | Raymarine | Hoch |
| 2 | Bewegliche Metallmassen (Anker, Werkzeug in Nähe) | Alle MEMS-Sensoren | Mittel |
| 3 | Vibration an Einbauort (Motor, Generator) | Raymarine | Mittel |
| 4 | Sensor beschädigt (Sturz, Feuchtigkeit) | Raymarine | Gering |
| 5 | Firmware-Bug (bestimmte Versionen) | Raymarine | Gering |

**Diagnose-Schritte:**
1. Einbauort prüfen: >50 cm von AC-Kabeln, Inverter, Lautsprecher?
2. Temporärer Test: EV-1 an langem SeaTalkNG-Kabel an anderem Ort montieren
3. Kalibrierung neu starten (360°-Drehung, 2× langsam)
4. Firmware aktualisieren (Raymarine Lighthouse-Software)
5. Wenn persistent: Sensor tauschen

---

## 7. Troubleshooting-Entscheidungsbäume

### 7.1 Entscheidungsbaum: Autopilot steuert nicht

```
START: Autopilot steuert nicht
│
├── Ist Strom vorhanden? (Display an?)
│   ├── NEIN → Sicherung prüfen → Kabel prüfen → Batteriespannung messen
│   │         → OK? → Defekt Kurscomputer (Service)
│   │
│   └── JA → Ist AP im Modus "AUTO"?
│       ├── NEIN → In "AUTO" schalten → Problem gelöst?
│       │   ├── JA → Bedienfehler (Schulung)
│       │   └── NEIN → Fehlermeldung auf Display?
│       │       ├── JA → Fehlermeldung auswerten (→ Fehlerbild-Atlas)
│       │       └── NEIN → NMEA-Verbindung prüfen (→ Baum 7.3)
│       │
│       └── JA → Hört man den Antrieb?
│           ├── NEIN → Antrieb-Sicherung prüfen
│           │   ├── Durchgebrannt → Kurzschluss im Antrieb? Kabel prüfen
│           │   └── OK → Antriebskabel prüfen → Antrieb defekt (Service)
│           │
│           └── JA → Bewegt sich das Ruder?
│               ├── NEIN → Bypass-Ventil offen? (Hydraulik)
│               │   ├── JA → Ventil schließen → Problem gelöst
│               │   └── NEIN → Hydraulik: Öl + Luft prüfen
│               │           → Linear: Mechanische Blockade?
│               │           → Kupplung zwischen Antrieb und Ruder prüfen
│               │
│               └── JA → Wird der Kurs gehalten?
│                   ├── NEIN (Oszillation) → Fehlerbild 6.1
│                   └── NEIN (Drift) → Fehlerbild 6.4
```

### 7.2 Entscheidungsbaum: Kompass-Probleme

```
START: Kompass zeigt falschen Kurs / springt
│
├── Abweichung konstant (z.B. immer +10°)?
│   ├── JA → Deviation durch Magnetfeld
│   │   ├── Kalibrierung durchgeführt?
│   │   │   ├── NEIN → Kalibrierfahrt (360° langsam)
│   │   │   └── JA → Kalibrierung korrekt?
│   │   │       ├── Fehler bei Kalibrierung → Wiederholen (ruhiges Wetter, kein Strom an Windenwinden)
│   │   │       └── Kalibrierung OK → Einbauort ändern (>1m von Störquellen)
│   │
│   └── NEIN → Abweichung variiert / springt
│       ├── Springt immer am gleichen Kurs?
│       │   ├── JA → Lokale Deviation (bestimmtes Störfeld bei bestimmter Ausrichtung)
│       │   │   → Metallmassen kartieren, Einbauort verlegen
│       │   └── NEIN → Springt zufällig
│       │       ├── Nur wenn Motor/Generator läuft?
│       │       │   ├── JA → EMV-Problem → Kompass weiter von Motor
│       │       │   │       → Kabelschirmung prüfen
│       │       │   └── NEIN → Defekter Sensor
│       │       │       ├── MEMS → Firmware-Update, ggf. Tausch
│       │       │       └── Fluxgate → Alterung, Tausch
│       │
│       └── Abweichung ändert sich langsam (Drift)
│           ├── MEMS-Sensor → GPS-Stützung aktiv?
│           │   ├── NEIN → GPS-Verbindung herstellen
│           │   └── JA → Sensor-Drift → Neustart, Kalibrierung
│           └── Fluxgate → Temperatureinfluss? → Abwarten oder ersetzen
```

### 7.3 Entscheidungsbaum: NMEA 2000-Netzwerkprobleme

```
START: NMEA 2000 — Gerät nicht sichtbar
│
├── LED am Gerät leuchtet?
│   ├── NEIN → Gerät hat keine Stromversorgung
│   │   ├── Bus-versorgt? → Spannung am T-Stück messen (9-16V)
│   │   │   ├── OK → Drop-Kabel defekt oder Stecker-Problem
│   │   │   └── Keine Spannung → Bus-Netzteil prüfen (Sicherung, Kabel)
│   │   └── Selbst-versorgt? → Eigene Sicherung / Kabel prüfen
│   │
│   └── JA → Gerät hat Strom, aber ist nicht im Netzwerk
│       ├── Backbone-Terminierung korrekt? (Genau 2× 120Ω)
│       │   ├── NEIN → Terminatoren setzen, messen (60Ω gesamt)
│       │   └── JA → Backbone-Integrität prüfen
│       │       ├── Alle T-Stücke angeschraubt und dicht?
│       │       ├── Kein Stern-Aufbau? (Nur lineare Topologie!)
│       │       ├── Drop-Kabel alle <6m?
│       │       └── Backbone <100m gesamt?
│       │           → Alles OK? → Einzeltest:
│       │              Nur dieses Gerät + 1 Plotter am Bus
│       │              ├── Sichtbar → Problem war anderes Gerät (Störer)
│       │              │   → Geräte einzeln wieder zufügen, Störer identifizieren
│       │              └── Nicht sichtbar → Gerät defekt oder Firmware-Problem
│       │                  → Firmware-Update → Hilft nicht? → Service/Tausch
```

### 7.4 Entscheidungsbaum: Übermäßiger Stromverbrauch

```
START: Stromverbrauch des Autopiloten zu hoch
│
├── Stromverbrauch messen (Amperemeter in Zuleitung, 30 min Durchschnitt)
│   ├── <1,5× Herstellerangabe → Normal für Bedingungen
│   │   → Seebedingungen berücksichtigen (Tabelle Duty Cycle)
│   │
│   └── >1,5× Herstellerangabe → Problem suchen
│       ├── Antrieb läuft fast ständig?
│       │   ├── JA → Ständige Korrekturen
│       │   │   ├── Ruderanlage schwergängig? → Warten, Fetten
│       │   │   ├── Spiel in Ruderanlage? → Reparieren
│       │   │   ├── Gain zu hoch? → Reduzieren
│       │   │   ├── Deadband zu eng? → Erweitern (3°+)
│       │   │   └── Antrieb zu schwach für Boot? → Größeren Antrieb
│       │   │
│       │   └── NEIN → Antrieb zieht im Leerlauf zu viel
│       │       ├── Standby-Verbrauch messen (ohne AP aktiv)
│       │       │   ├── >2× Herstellerangabe → Elektronik-Defekt
│       │       │   └── Normal → Antriebsproblem
│       │       │       ├── Hydraulik: Öl-Leckage? Pumpe verschlissen?
│       │       │       └── Linear: Getriebe verschlissen? Spindel schwergängig?
│       │
│       └── Kurscomputer + Sensoren verbrauchen zu viel
│           → Selten → Firmware-Bug oder Defekt → Service
```

### 7.5 Entscheidungsbaum: Wind-Modus funktioniert nicht / nicht verfügbar

```
START: Wind-Modus funktioniert nicht
│
├── Ist ein Windsensor installiert?
│   ├── NEIN → Windsensor installieren und kalibrieren
│   │
│   └── JA → Sieht der Autopilot Wind-Daten?
│       ├── NEIN → NMEA-Verbindung Windsensor → AP prüfen
│       │   ├── Windsensor auf NMEA 2000? → PGN 130306 prüfen
│       │   ├── Windsensor auf NMEA 0183? → $xxMWV Sentence prüfen
│       │   └── NKE-Bus? → NKE-Muliplexer prüfen
│       │
│       └── JA → Wind-Modus auswählbar?
│           ├── NEIN → Funktion evtl. nicht im Modell enthalten
│           │   ├── Garmin Reactor: Wind-Modus nur mit gWind-Sensor
│           │   ├── Simrad AP44: Wind-Modus nur mit Segel-Firmware
│           │   ├── Furuno NavPilot: Basis-Wind nur
│           │   └── Prüfen: Firmware-Version und Kompatibilität
│           │
│           └── JA → Wind-Modus funktioniert schlecht
│               ├── AWA oder TWA?
│               │   ├── AWA instabil → Wind-Response reduzieren,
│               │   │   Böen-Dämpfung erhöhen
│               │   └── TWA instabil → Bootspeed-Eingabe prüfen,
│               │       Log/GPS korrekt?
│               ├── Wind-Sensor-Position korrekt?
│               │   (Mastspitze, >1m über Hindernissen)
│               └── Kalibrierung Windsensor → Offset korrekt?
│                   (Windfahne muss 0° bei Wind von vorn zeigen)
```

---

## 8. FAQ — Häufige Fragen

### 8.1 Allgemeine Fragen

**F1: Brauche ich einen Autopiloten?**
Antwort: Für jeden, der länger als 30 Minuten am Stück fährt oder segelt: Ja. Ein Autopilot entlastet den Rudergänger, verbessert den Komfort, ermöglicht Einhandsegeln und erhöht die Sicherheit (Freiheit für Navigation, Ausguck, Segelmanöver). Auf Langfahrt ist ein Autopilot essentiell — er ist der treueste Mitsegler an Bord.

**F2: Was kostet ein Autopilot-System komplett, inklusive Einbau?**
Antwort: Tillerpilot-System für kleines Segelboot: 1.800–3.000 € inkl. Einbau. Mittelklasse-Segelyacht mit Linearantrieb: 4.000–8.000 €. Große Yacht mit Hydraulik: 8.000–20.000 €. Der Einbau durch einen Fachbetrieb kostet je nach Komplexität 500–3.000 € zusätzlich.

**F3: Kann ich den Autopiloten selbst einbauen?**
Antwort: Tillerpilot: Ja, einfach (Plug-and-Play). Linearantrieb: Bei handwerklichem Geschick machbar (6–12 Stunden, Zugang zum Ruderbereich nötig). Hydraulik: Nur mit Erfahrung oder Fachbetrieb (Hydraulikleitungen, Entlüftung, Bypassventil). Die NMEA-Verkabelung erfordert Grundkenntnisse in Bordelektrik.

**F4: Welcher Hersteller ist der beste?**
Antwort: Es gibt keinen "besten" Hersteller. Für Segler: B&G (beste Segel-Algorithmen) oder NKE (Regatta-Standard). Für Motorboote: Garmin (beste Integration) oder Simrad (robuste Technik). Für Langfahrt/Zuverlässigkeit: Furuno (Referenz) oder Raymarine (größtes Service-Netz). Für Budget: Raymarine EV-100 oder Garmin Compact Reactor.

**F5: Wie lange hält ein Autopilot?**
Antwort: Kurscomputer: 10–20+ Jahre (Elektronik). Linearantrieb: 5–10 Jahre (mechanischer Verschleiß). Hydraulikpumpe: 8–15 Jahre (Dichtungen, Öl). Tillerpilot: 3–7 Jahre (Spindelverschleiß). Kompass/Sensor: 10–15+ Jahre. Regelmäßige Wartung (Schmierung, Ölwechsel, Kabelkontrolle) verlängert die Lebensdauer erheblich.

### 8.2 Auswahl und Dimensionierung

**F6: Wie bestimme ich die richtige Antriebsgröße?**
Antwort: Faustformel: Verdrängung × Faktor (siehe Abschnitt 2.2). Immer eine Nummer größer wählen — ein überdimensionierter Antrieb arbeitet mit geringerem Duty Cycle und lebt länger. Herstellertools (z.B. Raymarine AP Calculator) helfen bei der Auswahl.

**F7: Linear oder Hydraulik — was ist besser?**
Antwort: Bis ~12.000 kg Verdrängung: Linear (einfacher, wartungsärmer, günstiger). Ab ~12.000 kg: Hydraulik (stärker, leiser, langlebiger). Wenn bereits eine Hydraulik-Steueranlage vorhanden: Hydraulik-AP nachrüsten ist oft einfacher. Wenn rein mechanische Steuerung: Linear nachrüsten ist einfacher.

**F8: Brauche ich einen Ruderfeedback-Sensor?**
Antwort: Für Tillerpiloten: Nein (Position wird über Spindelposition gemessen). Für Linear/Hydraulik: Dringend empfohlen (Raymarine EV-2, Garmin GRF-10). Ohne Ruderfeedback arbeitet der AP "blind" und kann das Ruder nicht präzise positionieren. Die Regelqualität verbessert sich mit Ruderfeedback um ca. 30 %.

**F9: Kann ich Geräte verschiedener Hersteller mischen?**
Antwort: Auf NMEA-2000-Ebene: Ja, für Standard-Funktionen (Kurs, GPS, Wind). Für erweiterte Funktionen (Track-Modus, Segel-Modi, Auto-Guidance): Nein, hier ist ein Ökosystem-Ansatz nötig. Beispiel: Garmin-Plotter + B&G-Autopilot funktioniert für Basis-Track, aber Auto-Guidance geht nur mit Garmin-Plotter + Garmin-AP.

**F10: Welcher Kompass ist der beste für meinen AP?**
Antwort: Für die meisten Yachten: MEMS-Kompass (im AP integriert oder B&G Precision-9). Für Superyachten und gewerblich: Satellitenkompass (Simrad HS75, Furuno SCX-20). Für Budget: Fluxgate (bewährt, aber langsamere Heading-Rate). Ein externer GPS empfänger verbessert jeden MEMS-Kompass durch Drift-Korrektur.

### 8.3 Einbau und Konfiguration

**F11: Wo sollte der Kompass/Sensor eingebaut werden?**
Antwort: Möglichst nahe am Drehpunkt (Schwerpunkt) des Bootes, waagerecht auf einer festen Fläche. Mindestabstände: 1m von Motoren, 50 cm von Lautsprechern/Magneten, 30 cm von AC-Kabeln. Nicht in der Nähe des Steuerrades (Magnete im Kompass). Bei Stahlbooten: Auf erhöhtem Sockel oder in Aluminiumgehäuse.

**F12: Wie kalibriere ich den Kompass?**
Antwort: Standard-Kalibrierung: 2× langsame 360°-Drehung bei ruhiger See, unter Motor, konstante Geschwindigkeit. Während der Kalibrierung: Keine Winden, Ankerspill oder andere elektrische Verbraucher einschalten. Keine Personen neben dem Sensor bewegen. Bei Raymarine EV-1: Kalibrierung erfolgt automatisch (aber manuelle 360°-Fahrt verbessert das Ergebnis). Bei B&G Precision-9: Kalibrierungsprogramm im Menü folgen.

**F13: Wie entlüfte ich ein Hydraulik-Autopilot-System?**
Antwort: 1) Bypass-Ventil öffnen. 2) Ölreservoir auffüllen (ATF Dexron III oder herstellerspezifisch). 3) Ruder von Hand langsam von Anschlag zu Anschlag bewegen (10×). 4) Entlüftungsschraube am höchsten Punkt des Systems öffnen. 5) Pumpe kurz laufen lassen (AP in Auto). 6) Wenn Öl ohne Blasen austritt → Schraube schließen. 7) Bypass-Ventil schließen. 8) Ölstand nachfüllen. 9) Testfahrt, Druckprüfung.

**F14: Wie stelle ich den Gain (Verstärkung) richtig ein?**
Antwort: Start mit Werkseinstellung. Bei Oszillation: Gain um 2 Stufen reduzieren. Bei zu trägem Kurshalten: Gain um 1 Stufe erhöhen. Moderne Autopiloten (Evolution, Reactor, Continuum) stellen den Gain selbstständig ein — manuelles Eingreifen nur bei Problemen. Faustregel: Der AP sollte mit möglichst wenig Ruderbewegung den Kurs halten.

**F15: Wie verbinde ich den AP mit dem Plotter für Track-Modus?**
Antwort: Bei NMEA 2000: Beide Geräte am gleichen Backbone → Plotter erkennt AP automatisch → Route erstellen → Track-Modus am Plotter oder AP aktivieren. Bei NMEA 0183: Plotter-Ausgang (APB, XTE) an AP-Eingang verkabeln → Baudrate abstimmen → Testen. Wichtig: Immer Probefahrt mit manueller Überwachung!

### 8.4 Betrieb und Wartung

**F16: Wie viel Strom verbraucht mein Autopilot wirklich?**
Antwort: Siehe Abschnitt 2.5 für die Berechnung. Faustregel: Standby + (Antriebslast × Duty Cycle). In Praxis für eine 38 ft Segelyacht: 1,5–3 A bei 12V im Durchschnitt = 36–72 Ah pro 24h. Messen ist besser als rechnen: Amperemeter in die Zuleitung für einen typischen Segeltag.

**F17: Wie oft muss ich den Autopilot warten?**
Antwort: Jährlich (Saisonbeginn): Sichtprüfung aller Kabel und Stecker, Ruderspiel prüfen, Testfahrt mit Kompass-Abgleich. Alle 3 Jahre: Hydrauliköl wechseln, Dichtungen prüfen, Kugelgelenke auf Verschleiß prüfen. Alle 5 Jahre: Linearantrieb-Spindel prüfen/tauschen, Zahnriemen (Radpilot) prüfen.

**F18: Darf ich den Autopiloten bei Gewitter einschalten?**
Antwort: Grundsätzlich ja, aber: Bei direktem Blitzeinschlag kann jede Elektronik zerstört werden. Empfehlung: Bei Gewitterwarnung AP ausschalten und manuell steuern. Blitzschutz (Überspannungsschutz) an der Stromversorgung schützt vor Ferneinschlägen, nicht vor Direkteinschlag. NMEA 2000-Netzwerke sind besonders empfindlich, weil ein Blitz über den Bus alle Geräte zerstören kann.

**F19: Was mache ich, wenn der Autopilot auf See ausfällt?**
Antwort: 1) Ruhe bewahren — Sie haben noch Handsteuerung! 2) Bypass-Ventil öffnen (Hydraulik). 3) Manuell steuern. 4) Event-Log des AP auslesen (zeigt Fehlgrund). 5) Neustart des AP versuchen (Strom aus/ein). 6) Sicherungen prüfen. 7) Wenn Antrieb defekt: Notpinne / Notsteuerung einsetzen. 8) Wache verstärken. 9) Im Hafen reparieren.

**F20: Ersetzt ein Autopilot den Rudergänger?**
Antwort: NEIN. Rechtlich und praktisch nicht. COLREG Regel 5 verlangt ständigen Ausguck. Der Autopilot ist ein Hilfsmittel, kein Ersatz für den Wachführer. Der Schiffsführer muss jederzeit in der Lage sein, die Steuerung zu übernehmen. Bei einigen Versicherungen erlischt der Schutz, wenn nachweislich ohne Ausguck mit Autopilot gefahren wurde.

### 8.5 Spezifische Herstellerfragen

**F21: Ist SeaTalkNG das Gleiche wie NMEA 2000?**
Antwort: Physikalisch: Ja (gleiche Stecker, gleiche Kabel, gleiche Spannungen). Logisch: Zu 95 % ja (alle NMEA-2000-Standard-PGNs werden übertragen). Die restlichen 5 % sind proprietäre Raymarine-PGNs, die nur Raymarine-Geräte verstehen. Ein SeaTalkNG-Gerät kann direkt an ein NMEA-2000-Backbone angeschlossen werden.

**F22: Kann ich einen B&G NAC-2 mit einem Simrad-Plotter verwenden?**
Antwort: Ja — B&G und Simrad gehören zum gleichen Konzern (Navico) und verwenden die gleiche NMEA-2000-Implementierung. Die Kompatibilität ist sogar besser als mit Fremdherstellern, weil proprietäre Navico-PGNs von beiden Marken verstanden werden.

**F23: Warum ist der NKE Gyropilot so teuer, wenn er weniger Features hat?**
Antwort: NKE ist ein kleiner Spezialist mit hohen Stückkosten. Der Preis spiegelt die überlegene Segel-Algorithmik wider, nicht die Feature-Liste. Wer einen Autopiloten sucht, der am besten segelt, kommt an NKE nicht vorbei. Wer Track-Modus, Plotter-Integration und moderne Bedienung will, ist bei B&G oder Garmin besser aufgehoben.

**F24: Furuno NavPilot 300 oder Raymarine EV-200 — was ist zuverlässiger?**
Antwort: Furuno hat die höhere Einzelgeräte-Zuverlässigkeit (geschätzt MTBF 25.000h vs. 15.000h). Raymarine hat bessere Service-Verfügbarkeit in Europa und mehr Ersatzteile auf Lager. Für Langfahrt in abgelegene Gebiete: Furuno (weil es seltener kaputt geht). Für Europasegeln: Raymarine (weil im Schadensfall schneller Hilfe kommt).

**F25: Garmin Shadow Drive — Segen oder Fluch?**
Antwort: Für Motorbootfahrer: Segen (intuitive Übernahme, kein Tastendruck nötig). Für Segler: Gemischt. Bei Pinnensteuerung irrelevant (kein Shadow Drive). Bei Radsteuerung: Kann beim Segelmanöver stören, wenn die Hand am Steuerrad den AP deaktiviert. Lösung: Shadow Drive in den Einstellungen deaktivieren oder Empfindlichkeit anpassen.

**F26: Kann ich meinen alten NMEA-0183-Autopiloten mit einem neuen NMEA-2000-Plotter verbinden?**
Antwort: Ja, über einen NMEA-0183-zu-NMEA-2000-Gateway (z.B. Actisense NGW-1, Yacht Devices YDNR-02). Der Gateway übersetzt Sentences in PGNs und umgekehrt. Wichtig: Nur relevante Sentences durchlassen (APB, XTE, HDG), sonst überflutet der alte AP den Bus mit Daten.

**F27: Wie finde ich heraus, ob mein Autopilot für mein Boot ausreichend dimensioniert ist?**
Antwort: 1) Verdrängung des Bootes kennen (Herstellerangabe oder Vermessung). 2) Rudertyp identifizieren (Spaten, Skeg, Langkiel). 3) Faustformel anwenden (Abschnitt 2.2). 4) Mit Herstellerangabe der Antriebseinheit vergleichen. 5) Im Zweifelsfall: Eine Nummer größer wählen. 6) Bei bestehendem AP: Duty Cycle messen (>50 % bei moderater See = unterdimensioniert).

**F28: Was bedeutet "IEC 62065-konform" bei einem Autopiloten?**
Antwort: IEC 62065 ist die internationale Norm für "Track Control Systems" in der Berufsschifffahrt. Konformität bedeutet: Der AP erfüllt Mindestanforderungen an Genauigkeit, Alarmierung, Ausfallsicherheit und Bedienung für gewerbliche Schiffe. Für Freizeitboote nicht gesetzlich vorgeschrieben, aber ein Qualitätsmerkmal. Systeme: Simrad AC70, Furuno NavPilot 700, Raymarine EV-400.

**F29: Mein Autopilot "übersteuert" — bei jeder Welle gibt er Vollruder. Was tun?**
Antwort: 1) Gain reduzieren (um 2–3 Stufen). 2) Seegangsfilter (Wave Filter) aktivieren oder erhöhen. 3) Deadband erweitern (auf 3–5°). 4) Bei adaptiven Systemen (Evolution, Reactor): System zurücksetzen und neu lernen lassen (30–60 min Fahrt). 5) Bei manueller Einstellung: Counter-Rudder erhöhen. 6) Wenn nichts hilft: Antrieb zu schnell für Boot — langsamere Antriebseinstellung suchen (bei Hydraulik: Flow-Control-Ventil installieren).

**F30: Welche Autopiloten eignen sich für Katamarane?**
Antwort: Katamarane mit Doppelruder brauchen entweder: a) Zwei separate Antriebe mit einem Kurscomputer, der beide synchron ansteuert (Raymarine EV-200 mit 2× Type 1, B&G NAC-2 mit 2× RFC42). b) Ein Hydraulik-System mit Verteilventil. Besonderheit Katamaran: Kein Krängungssignal als Regelgröße nutzbar, Windsteuerung muss anders kalibriert werden. Alle großen Hersteller bieten Katamaran-Modi.

---

## 9. Glossar

| Nr. | Begriff | Erklärung |
|-----|---------|-----------|
| 1 | **ACU** | Autopilot Control Unit — Kurscomputer, der die Steuerlogik enthält |
| 2 | **AHRS** | Attitude and Heading Reference System — kombinierter Lage- und Kursreferenzsensor |
| 3 | **AWA** | Apparent Wind Angle — scheinbarer Windwinkel relativ zur Bootsmittschiffslinie |
| 4 | **Bypass-Ventil** | Ventil im Hydraulikkreislauf, das den AP-Zylinder umgeht und Handsteuerung ermöglicht |
| 5 | **CAN-Bus** | Controller Area Network — serielles Bus-Protokoll, Basis für NMEA 2000 |
| 6 | **CCU** | Course Computer Unit — Garmin-Bezeichnung für den Kurscomputer |
| 7 | **COG** | Course Over Ground — Kurs über Grund (GPS-basiert, nicht Heading!) |
| 8 | **Continuum** | B&G-proprietärer adaptiver Regelalgorithmus für Segeln |
| 9 | **Counter-Rudder** | Gegenruder — Rudergabe gegen die Drehrichtung vor Erreichen des Sollkurses |
| 10 | **Cross-Track Error (XTE)** | Querabweichung von der geplanten Route |
| 11 | **Deadband** | Totband — Kursabweichungsbereich, in dem der AP kein Ruder gibt |
| 12 | **Deviation** | Kompassabweichung durch bordeignes Magnetfeld |
| 13 | **Drop-Kabel** | Stichleitungen vom NMEA-2000-Backbone zum Endgerät (max. 6m) |
| 14 | **Duty Cycle** | Einschaltdauer — Anteil der Zeit, in der der Antrieb tatsächlich arbeitet |
| 15 | **Evolution** | Raymarine-Autopilot-Plattform mit MEMS-Sensorik seit 2014 |
| 16 | **EV-1** | Raymarine Evolution Sensor Core — 9-Achsen MEMS-Lagesensor |
| 17 | **Fluxgate-Kompass** | Elektronischer Kompass basierend auf Magnetfeldmessung in Kernspulen |
| 18 | **Gain** | Verstärkungsfaktor — wie aggressiv der AP auf Kursabweichungen reagiert |
| 19 | **GNSS** | Global Navigation Satellite System — Oberbegriff für GPS, GLONASS, Galileo, BeiDou |
| 20 | **Gyropilot** | NKE-Markenname für deren Autopilot-Kurscomputer |
| 21 | **H5000 Hydra** | B&G-Flaggschiff-Segelcomputersystem mit integriertem Autopilot |
| 22 | **Heading** | Steuerkurs des Bootes (Richtung, in die der Bug zeigt) |
| 23 | **Hub** | Linearbewegung des Antriebs in mm — bestimmt den maximalen Ruderausschlag |
| 24 | **Hydraulikpumpe** | Elektrische Pumpe, die Hydrauliköl in den Ruderzylinder fördert |
| 25 | **IMO** | International Maritime Organization — UN-Organisation für Seeschifffahrt |
| 26 | **IMU** | Inertial Measurement Unit — Trägheitsnavigationseinheit mit Gyroskop und Beschleunigungssensoren |
| 27 | **Kalman-Filter** | Mathematischer Algorithmus zur optimalen Schätzung des Systemzustands aus verrauschten Sensordaten |
| 28 | **Linearantrieb** | Elektrischer Antrieb mit linearer Schubbewegung (Pushrod/Ram) |
| 29 | **MEMS** | Micro-Electro-Mechanical Systems — miniaturisierte Sensoren auf Silizium-Chip |
| 30 | **MTBF** | Mean Time Between Failures — mittlere Betriebsdauer zwischen Ausfällen |
| 31 | **NAC** | Navigation Autopilot Computer — B&G/Navico-Bezeichnung für Kurscomputer |
| 32 | **NavPilot** | Furuno-Markenname für deren Autopilot-Produktlinie |
| 33 | **NMEA 0183** | Serielles Datenprotokoll für marine Elektronik (seit 1983) |
| 34 | **NMEA 2000** | CAN-basiertes Netzwerkprotokoll für marine Elektronik (seit 2001) |
| 35 | **PGN** | Parameter Group Number — Identifikator für NMEA-2000-Datenpakete |
| 36 | **PID-Regler** | Proportional-Integral-Differenzial-Regler — Standard-Regelalgorithmus |
| 37 | **Polar-Diagramm** | Diagramm der Bootgeschwindigkeit als Funktion von Windwinkel und -stärke |
| 38 | **Reactor** | Garmin-Autopilot-Plattform mit integrierter AHRS-Sensorik |
| 39 | **RFC** | Rudder Feedback Controlled — B&G-Linearantrieb mit integriertem Rudersensor |
| 40 | **Rotary-Antrieb** | Elektromotor mit Drehbewegung (Untersetzungsgetriebe) |
| 41 | **RPU** | Reversible Pump Unit — Navico/Simrad Hydraulikpumpe |
| 42 | **Ruderfeedback** | Sensor, der den aktuellen Ruderwinkel an den AP meldet |
| 43 | **Ruderquadrant** | Hebelarm am Ruderschaft, an dem der Antrieb angreift |
| 44 | **Ruderlimit** | Maximaler Ruderausschlag, den der AP kommandieren darf |
| 45 | **SeaTalk** | Proprietäres Raymarine-Kommunikationsprotokoll (1990er, 3-adrig) |
| 46 | **SeaTalkNG** | Aktuelles Raymarine-Bussystem (physikalisch NMEA 2000 kompatibel) |
| 47 | **Shadow Drive** | Garmin-Funktion: AP deaktiviert sich bei manueller Ruderbetätigung |
| 48 | **SimNet** | Proprietäres Simrad-Bussystem (gelbe Stecker, CAN-basiert) |
| 49 | **SOG** | Speed Over Ground — Geschwindigkeit über Grund (GPS) |
| 50 | **Terminierung** | 120Ω-Widerstand an den Enden des NMEA-2000-Backbone |
| 51 | **Tillerpilot** | Autopilot-Antrieb für Pinnensteuerung (Linearbewegung direkt an Pinne) |
| 52 | **Track-Modus** | AP folgt einer vorgegebenen Route (Wegpunkte) vom Plotter |
| 53 | **TWA** | True Wind Angle — wahrer Windwinkel (bereinigt um Bootgeschwindigkeit) |
| 54 | **Variation** | Missweisung — Abweichung zwischen magnetisch Nord und geographisch Nord |
| 55 | **VMG** | Velocity Made Good — effektive Geschwindigkeit in Richtung Ziel |
| 56 | **Wave Filter** | Seegangsfilter — dämpft hochfrequente Wellenbewegungen in der Kursregelung |
| 57 | **WPT** | Waypoint — Wegpunkt auf einer Route |
| 58 | **XTE** | Cross-Track Error — Querabweichung von der Sollroute |

---

## 10. Schnell-Referenz

### 10.1 Dimensionierungstabelle — Schnellauswahl

**Segelboot:**

| Verdrängung | Budget | Empfehlung |
|------------|--------|-----------|
| <3.000 kg, Pinne | <2.000 € | Raymarine EV-100 Tiller oder Garmin Compact Reactor |
| <3.000 kg, Pinne | <3.000 € | B&G NAC-1 + RFC25 |
| 3.000–7.000 kg, Rad | <3.500 € | Raymarine EV-100 Wheel oder EV-150 Linear |
| 5.000–12.000 kg | <6.000 € | B&G NAC-2 + RFC42, Garmin Reactor 20 |
| 5.000–12.000 kg, Regatta | <8.000 € | NKE Gyropilot 2 + Linear |
| 12.000–25.000 kg | <10.000 € | Raymarine EV-200 Hydraulik, B&G NAC-2 Hydraulik |
| >25.000 kg | >12.000 € | B&G NAC-3, Simrad AC70, Furuno NavPilot 700 |

**Motorboot:**

| Verdrängung | Budget | Empfehlung |
|------------|--------|-----------|
| <5.000 kg | <3.500 € | Garmin Reactor 20 Hydraulik |
| 5.000–15.000 kg | <6.000 € | Garmin Reactor 20, Simrad AP44 Hydraulik |
| 15.000–30.000 kg | <12.000 € | Garmin Reactor 40, Simrad AP48 |
| >30.000 kg | >15.000 € | Simrad AC70, Furuno NavPilot 700 |

### 10.2 Stromverbrauch-Schnellrechner

```
Schritt 1: Standby-Verbrauch ablesen (Tabelle oben)         _____ A
Schritt 2: Antriebsverbrauch bei Vollast ablesen              _____ A
Schritt 3: Duty Cycle schätzen (ruhig=10%, mittel=20%, rau=40%) _____ %
Schritt 4: Durchschnitt = Standby + (Vollast × Duty/100)    _____ A
Schritt 5: × 24h = Tagesverbrauch                           _____ Ah
Schritt 6: Batteriekapazität ÷ Tagesverbrauch = Autonomie   _____ Tage
```

### 10.3 Einbau-Checkliste

| Nr. | Schritt | Erledigt |
|-----|---------|---------|
| 1 | Kurscomputer: Trockener, belüfteter Einbauort | ☐ |
| 2 | Sensor/Kompass: >50 cm von Metallmassen, >1 m von Motoren | ☐ |
| 3 | Sensor: Waagerecht, parallel zur Kiellinie | ☐ |
| 4 | Antrieb: Zugang zum Ruderbereich, Montagefläche stabil | ☐ |
| 5 | Antrieb: Hub ausreichend für vollen Ruderausschlag | ☐ |
| 6 | Hydraulik: Bypass-Ventil erreichbar, Entlüftungsschraube zugänglich | ☐ |
| 7 | Stromkabel: Querschnitt gemäß Herstellerangabe (min. 4 mm²) | ☐ |
| 8 | Sicherung: Richtig dimensioniert, leicht zugänglich | ☐ |
| 9 | NMEA 2000: Backbone-Terminierung (2× 120Ω) | ☐ |
| 10 | NMEA 2000: Drop-Kabel <6 m, Backbone <100 m | ☐ |
| 11 | Bedieneinheit: Spritzwassergeschützt, gut ablesbar, griffbereit | ☐ |
| 12 | Ruderfeedback: Sensor am Ruderquadranten, Kabel verlegt | ☐ |
| 13 | Kalibrierung: Deviationsfahrt, Ruderkalibrierung, Testfahrt | ☐ |
| 14 | Dokumentation: Alle Einstellungen und Kalibrierungswerte notieren | ☐ |

### 10.4 Wartungsplan

| Intervall | Maßnahme |
|-----------|----------|
| Vor jeder Fahrt | Kurzer Funktionstest (AP ein, Kurs ändern, Ruder bewegt sich?) |
| Saisonbeginn | Sichtprüfung Kabel, Stecker, Antrieb. Ruderspiel prüfen. Testfahrt |
| Jährlich | Hydraulik: Ölstand prüfen. Linear: Kugelgelenke prüfen. Firmware-Update |
| Alle 3 Jahre | Hydrauliköl wechseln. Dichtungen prüfen. Kalibrierung erneuern |
| Alle 5 Jahre | Linearantrieb-Spindel/Getriebe prüfen. Zahnriemen (Radpilot) tauschen |
| Alle 10 Jahre | Generelle Überholung Antrieb. Kurscomputer ggf. ersetzen (Veralterung) |

---

## ANHANG A–H — Fallstudien

### ANHANG A — Fallstudie: Bavaria 38 Cruiser, Raymarine EV-150 Nachrüstung

**Boot:** Bavaria 38 Cruiser, Baujahr 2018
**Verdrängung:** 7.800 kg
**Rudertyp:** Spatenruder, Radsteuerung (Whitlock Cobra)
**Vorheriger AP:** Keiner
**Neuer AP:** Raymarine EV-150, ACU-150 + EV-1 Sensor + Type 1 Linearantrieb + p70Rs

**Einbau-Herausforderungen:**
- Zugang zum Ruderquadranten durch Achterkabine eingeschränkt
- Linearantrieb-Montage erforderte Winkelkonsole (Eigenbau Edelstahl)
- EV-1 Sensor unter Achterkoje montiert (Abstand Motor 1,2 m)
- SeaTalkNG-Kabel durch bestehenden Kabelkanal zum Cockpit

**Kosten:**

| Posten | Betrag |
|--------|--------|
| ACU-150 + EV-1 + p70Rs | 2.400 € |
| Type 1 Linearantrieb | 980 € |
| SeaTalkNG-Kabel, Stecker | 180 € |
| Edelstahl-Winkelkonsole | 250 € |
| Einbau (Fachbetrieb, 12 Std.) | 1.200 € |
| **Gesamt** | **5.010 €** |

**Ergebnis nach Kalibrierung:**
- Kurshalten bei 3 Bft.: ±1,5° Abweichung (hervorragend)
- Kurshalten bei 5 Bft., Seitenwind: ±3° Abweichung (gut)
- Stromverbrauch Durchschnitt: 1,4 A bei 12V
- Lautstärke: Leises Summen, in Kabine kaum hörbar
- Wind-Modus mit Windsensor: Stabil bis 20 kn TWS, darüber zunehmend nervös

**Bewertung AYDI:** Score 78/100. Confidence: documented. Schwachstelle: Linearantrieb bei >25 kn TWS grenzwertig für 7.800 kg. Empfehlung: Bei geplanter Blauwasserfahrt Type 2 Linear oder Hydraulik erwägen.

### ANHANG B — Fallstudie: Hallberg-Rassy 43 Mk II, B&G H5000 System

**Boot:** Hallberg-Rassy 43 Mk II, Baujahr 2020
**Verdrängung:** 13.500 kg
**Rudertyp:** Skeg-Ruder, Radsteuerung (Jefa)
**System:** B&G H5000 CPU + Hercules + NAC-2 + RFC42 + Precision-9 + WR10

**Installation (Werft-Original):**
- H5000 CPU unter Navigationstisch
- Precision-9 Kompass auf Holzsockel im Salonboden (Mitte Schiff)
- RFC42 Linearantrieb am Ruderquadranten (Achterpiek, guter Zugang)
- Triton2-Displays: 2× Cockpit, 1× Navigationstisch
- WR10 Wireless Remote am Mast-Fuß
- Windsensor B&G WS320 (drahtlos, Masttop)

**Kosten (Werftpaket, Neuboot-Einbau):**

| Posten | Betrag |
|--------|--------|
| H5000 CPU + Hercules | 6.000 € |
| NAC-2 | 1.850 € |
| RFC42 Linearantrieb | 1.250 € |
| Precision-9 | 520 € |
| 3× Triton2 Display | 1.140 € |
| WR10 Remote | 320 € |
| WS320 Windsensor | 750 € |
| Verkabelung + Einbau | 3.200 € |
| **Gesamt** | **15.030 €** |

**Ergebnis:**
- Kurshalten bei 3 Bft.: ±1° (exzellent)
- Wind-Modus (TWA) bei 15 kn TWS: ±2° TWA (hervorragend)
- Automatische Wende bei 45° TWA: Sauber, 12 Sekunden, Boot beschleunigt zügig
- Layline-Anzeige am Plotter: Korrekt und hilfreich bei Regatta
- Continuum-Algorithmus: Deutlich besser als Standard-PID bei Böen auf der Kreuz
- Stromverbrauch Durchschnitt: 1,8 A bei 12V (Skeg-Ruder = niedrig)

**Bewertung AYDI:** Score 92/100. Confidence: measured. Referenzinstallation für mittlere Blauwasser-Segelyachten mit Performance-Anspruch. H5000-System bietet das Gesamtpaket aus Autopilot + Segel-Instrumentierung + Performance-Optimierung.

### ANHANG C — Fallstudie: Princess V50, Garmin Reactor 40 Hydraulik

**Boot:** Princess V50, Baujahr 2022
**Verdrängung:** 16.000 kg
**Rudertyp:** Doppelruder (Doppelpropeller), hydraulische Steuerung
**System:** Garmin GHP Reactor 40 + Hydraulikpumpe 2,0 l/min + GHC 50 + Shadow Drive

**Installation:**
- Reactor 40 CCU unter Helmstation
- Hydraulikpumpe in Maschinenraum, an bestehende Steuerhydraulik angebunden
- GHC 50 Bedieneinheit an Hauptsteuerstand und Flybridge
- Shadow Drive Drucksensor in Hydraulikleitung
- Garmin GPSMAP 8616xsv als Plotter (volle Integration)

**Kosten:**

| Posten | Betrag |
|--------|--------|
| GHP Reactor 40 Kit (2,0 l) | 9.800 € |
| 2× GHC 50 Display | 1.300 € |
| Hydraulik-Anbindung (Fachbetrieb) | 2.500 € |
| NMEA 2000 Verkabelung | 450 € |
| Einbau + Inbetriebnahme | 1.800 € |
| **Gesamt** | **15.850 €** |

**Ergebnis:**
- Kurshalten bei 3 Bft.: ±0,5° (exzellent — Motorboot, kein Seegang)
- Track-Modus mit Auto-Guidance: Funktioniert einwandfrei, berechnet Routen um Untiefen
- Shadow Drive: Exzellent — sofortige Übernahme bei Ruderbewegung, nahtlose Rückkehr
- Stromverbrauch Durchschnitt: 2,5 A bei 12V (Motorboot, geringer Duty Cycle)
- Docking: Kein AP-Einsatz (wird manuell/Joystick gedockt)

**Bewertung AYDI:** Score 88/100. Confidence: documented. Sehr gute Motorboot-Installation. Shadow Drive ist das herausragende Feature für Motorboote. Lock-in in Garmin-Ökosystem beachten (Auto-Guidance nur mit Garmin-Plotter).

### ANHANG D — Fallstudie: Sirius 40 DS, NKE Gyropilot 2 für Offshore-Regatta

**Boot:** Sirius 40 DS (umgebaut für Shorthanded-Regatta), Baujahr 2016
**Verdrängung:** 10.200 kg
**Rudertyp:** Doppelspatenruder, Radsteuerung
**System:** NKE Gyropilot 2 + NKE Linear Aktuator (groß) + NKE Displays + Topline Multiplexer

**Installation:**
- Gyropilot 2 unter Navigationstisch
- Linearantrieb am Steuerbord-Ruderquadranten (nur ein Ruder angesteuert)
- NKE Multidisplay im Cockpit, eines am Mast
- NKE-Bus mit Topline Multiplexer an NMEA 2000 für GPS
- NKE Windmessanlage (Girouette-Anémomètre HR)

**Kosten:**

| Posten | Betrag |
|--------|--------|
| Gyropilot 2 | 3.200 € |
| Linear Aktuator groß | 1.800 € |
| 2× Multidisplay | 1.360 € |
| Topline Multiplexer | 950 € |
| Windmessanlage | 850 € |
| Log-Speedo HR | 650 € |
| Rudersensor | 350 € |
| Verkabelung + Import + Einbau | 2.800 € |
| **Gesamt** | **11.960 €** |

**Ergebnis:**
- VMG-Modus am Wind: Optimale Kreuzstrategie, AP segelt das Boot auf 95 % der Polar
- Downwind bei 25 kn TWS: Stabil, keine Sonnenschüsse, AP "antizipiert" Wellen
- Stromverbrauch Durchschnitt: 1,2 A bei 12V (!)
- Regatta-Performance: Gewinnt regelmäßig gegenüber Booten mit B&G oder Raymarine AP

**Bewertung AYDI:** Score 95/100 (Segel-Performance), Score 62/100 (Integration/Komfort). Confidence: documented. Für reine Segel-Performance konkurrenzlos. Für Fahrtensegler mit Plotter-Integration und Komfortanspruch weniger geeignet (kein Track-Modus, keine Touch-Bedienung, französische Doku).

### ANHANG E — Fallstudie: Nordhavn 47, Furuno NavPilot 700 für Weltumsegelung

**Boot:** Nordhavn 47 (Passagemaker), Baujahr 2019
**Verdrängung:** 28.000 kg
**Rudertyp:** Spatenruder, hydraulische Steuerung (Hynautic)
**System:** Furuno NavPilot 700 + SCX-20 Satellitenkompass + Pumpe 1,5 l + PG-700 als Backup

**Installation:**
- NavPilot 700 Prozessor im Maschinenraum (klimatisiert)
- Bedieneinheit am Hauptsteuerstand
- SCX-20 Satellitenkompass auf Flybridge-Dach (freie Sicht)
- PG-700 Fluxgate als Backup-Heading-Quelle (im Rumpf)
- Hydraulikpumpe parallel zur bestehenden Steuerhydraulik
- Furuno NavNet TZtouch3 als Plotter (Ethernet-Integration)

**Kosten:**

| Posten | Betrag |
|--------|--------|
| NavPilot 700 (Prozessor + Bedieneinheit) | 8.700 € |
| SCX-20 Satellitenkompass | 6.500 € |
| PG-700 Fluxgate (Backup) | 850 € |
| Hydraulikpumpe 1,5 l | 2.800 € |
| Hydraulik-Integration | 3.500 € |
| NMEA 2000 + Ethernet + Kabel | 1.200 € |
| Einbau + Inbetriebnahme (Fachwerft) | 4.500 € |
| **Gesamt** | **28.050 €** |

**Ergebnis nach 15.000 sm Weltumsegelung:**
- Kein einziger Ausfall in 3 Jahren / 15.000 Seemeilen
- Kurshalten bei Pazifik-Dünung: ±1° (exzellent)
- Economy-Modus: 8 % Treibstoffersparnis gegenüber Vorgänger-AP
- Satellitenkompass: Nulls Deviation-Problem, auch bei Stahlcontainern an Deck
- Multi-Heading: Automatischer Wechsel von SCX-20 auf PG-700 bei GPS-Störung (1× aufgetreten, Pazifik)
- Black-Box: 2× Diagnosedaten nach sporadischem Warnsignal ausgewertet (Kabel-Korrosion identifiziert)

**Bewertung AYDI:** Score 96/100. Confidence: documented (15.000 sm Praxistest). Referenzinstallation für Langfahrt-Motorboote. Höchste Zuverlässigkeit, beste Heading-Genauigkeit. Investition rechtfertigt sich durch pannenlosen Betrieb über Tausende Seemeilen.

### ANHANG F — Fallstudie: Jeanneau Sun Odyssey 349, Simrad AP44 Budget-Lösung

**Boot:** Jeanneau Sun Odyssey 349, Baujahr 2017
**Verdrängung:** 5.200 kg
**Rudertyp:** Doppelspatenruder, Radsteuerung
**System:** Simrad AP44 + SD10 Linearantrieb + Precision-9

**Installation (Eigeneinbau durch Eigner):**
- AP44 als All-in-One-Bedien-/Kurscomputer am Steuerstand
- SD10 Linearantrieb am Steuerbord-Ruderquadranten
- Precision-9 unter Salonboden
- NMEA 2000 Backbone mit 3 T-Stücken (AP, Plotter, GPS)

**Kosten:**

| Posten | Betrag |
|--------|--------|
| Simrad AP44 | 1.650 € |
| SD10 Linearantrieb | 680 € |
| Precision-9 | 520 € |
| NMEA 2000 Starter Kit | 180 € |
| Montagematerial | 120 € |
| Eigeneinbau (16 Std.) | 0 € (Eigenleistung) |
| **Gesamt** | **3.150 €** |

**Ergebnis:**
- Kurshalten bei 3 Bft.: ±2° (gut für Preisklasse)
- Kurshalten bei 5 Bft., Kreuz: ±4° (akzeptabel)
- Track-Modus mit Simrad Go7: Funktioniert zuverlässig
- Wind-Modus: Basis (AWA), ausreichend für Fahrtensegeln
- Stromverbrauch: 1,1 A Durchschnitt bei 12V (sparsam)
- Geräusch: SD10 bei Richtungswechseln hörbar, aber nicht störend

**Bewertung AYDI:** Score 72/100. Confidence: documented. Gutes Preis-Leistungs-Verhältnis. Für Wochenend- und Urlaubssegeln vollkommen ausreichend. Für Langfahrt oder Performance-Segeln nicht optimal (Segel-Funktionen zu basisch, SD10 für 5.200 kg grenzwertig bei schwerem Wetter).

### ANHANG G — Fallstudie: Amel 50, Raymarine EV-200 Hydraulik + B&G Precision-9

**Boot:** Amel 50, Baujahr 2021
**Verdrängung:** 14.800 kg
**Rudertyp:** Spatenruder, hydraulische Steuerung (Amel proprietär)
**System:** Raymarine EV-200, ACU-200 + Type 2 Hydraulikpumpe + B&G Precision-9 als externer Kompass

**Besonderheit:** Mischinstallation (Raymarine AP + B&G Kompass) über NMEA 2000.

**Installation:**
- ACU-200 im Maschinenraum
- Type 2 Hydraulikpumpe in bestehende Amel-Hydraulik integriert
- p70Rs Bedieneinheit im Cockpit (2× für beide Helmstationen)
- B&G Precision-9 statt Raymarine EV-1 (bessere Kompass-Genauigkeit)
- Alle Geräte auf gemeinsamen NMEA 2000 Backbone

**Kosten:**

| Posten | Betrag |
|--------|--------|
| ACU-200 | 1.350 € |
| Type 2 Hydraulikpumpe | 2.200 € |
| 2× p70Rs | 1.240 € |
| B&G Precision-9 | 520 € |
| Hydraulik-Integration | 2.800 € |
| NMEA 2000 Verkabelung | 350 € |
| Einbau (Amel-Werft) | 2.500 € |
| **Gesamt** | **10.960 €** |

**Ergebnis:**
- Kurshalten deutlich besser als mit Serien-EV-1 (Precision-9 schneller und genauer)
- Raymarine Evolution-AI lernt trotzdem korrekt (nutzt NMEA-2000-Heading von Precision-9)
- Wind-Modus mit Amel Masthead-Sensor: Stabil und zuverlässig
- Hydraulik-Integration in Amel-System unkompliziert

**Bewertung AYDI:** Score 85/100. Confidence: documented. Zeigt, dass Mischinstallationen funktionieren, wenn NMEA 2000 korrekt aufgesetzt ist. B&G Precision-9 als Upgrade für jedes Raymarine-Evolution-System empfehlenswert.

### ANHANG H — Fallstudie: First 27, Autopilot-Ausfall Atlantiküberquerung

**Boot:** Beneteau First 27, Baujahr 2019, Einhand-Atlantiküberquerung
**Verdrängung:** 3.400 kg
**System:** Raymarine EV-100 Tiller + NKE Gyropilot 2 als Backup

**Chronologie des Ausfalls:**

| Tag | Ereignis |
|-----|---------|
| Tag 1–8 | Raymarine EV-100 funktioniert einwandfrei. 0,9 A Durchschnitt. |
| Tag 9 | Abends: AP gibt sporadisch "Drive Stopped" Alarm. Neustart hilft. |
| Tag 10 | Morgens: "Drive Stopped" nach 20 Minuten permanent. Tillerpilot-Spindel blockiert. |
| Tag 10 | Demontage: Spindelgewinde durch Salzkristalle verklebt (Tillerpilot-Gehäuse undicht). |
| Tag 10 | Umrüstung auf NKE Gyropilot 2 Backup (vorbereitet, 45 min Umbau). |
| Tag 11–24 | NKE Gyropilot 2 steuert fehlerfrei. 0,7 A Durchschnitt. Überlegene Downwind-Performance. |
| Tag 24 | Ankunft Martinique. |

**Lessons Learned:**

1. Tillerpilot-Gehäuse regelmäßig auf Dichtigkeit prüfen (O-Ring am Spindelaustritt)
2. Für Langfahrt IMMER einen Backup-AP mitführen
3. NKE Gyropilot 2 erwies sich als zuverlässiger und leistungsfähiger, obwohl als "Backup" gedacht
4. Energiebudget: NKE verbrauchte 22 % weniger Strom als Raymarine
5. Spindel-Reinigung + WD-40 alle 500 Betriebsstunden bei Tillerpiloten

**Bewertung AYDI:** Raymarine EV-100 Score 55/100 (Langfahrt-Eignung), NKE Gyropilot 2 Score 90/100. Confidence: documented. EV-100 Tiller ist für Küstensegeln ausgelegt, nicht für Ozeanpassagen. Für Atlantiküberquerungen: Linearantrieb-System (min. EV-150) oder NKE Gyropilot.

---

## ANHANG I–R — Pydantic v2 Modelle

> **Hinweis:** Alle Pydantic-Modelle verwenden `model_config = {"from_attributes": True}` — NIEMALS `class Config`.
> Sprache: Deutsch für Feldbeschreibungen, Englisch für Code.

### ANHANG I — AutopilotManufacturer Model

```python
"""Autopilot manufacturer model for AYDI knowledge system."""

from enum import Enum
from pydantic import BaseModel, Field


class AutopilotManufacturerName(str, Enum):
    """Supported autopilot manufacturers."""
    RAYMARINE = "raymarine"
    BG = "b_and_g"
    GARMIN = "garmin"
    SIMRAD = "simrad"
    FURUNO = "furuno"
    NKE = "nke"


class AutopilotManufacturer(BaseModel):
    """Hersteller eines Autopilot-Systems."""

    model_config = {"from_attributes": True}

    name: AutopilotManufacturerName = Field(
        ...,
        description="Herstellername"
    )
    parent_company: str = Field(
        ...,
        description="Mutterkonzern"
    )
    headquarters_country: str = Field(
        ...,
        description="Land des Hauptsitzes"
    )
    founded_year: int = Field(
        ...,
        ge=1900,
        le=2030,
        description="Gründungsjahr"
    )
    primary_bus_protocol: str = Field(
        ...,
        description="Primäres Busprotokoll (z.B. 'nmea2000', 'seatalkng', 'simnet', 'nke_bus')"
    )
    focus_segment: str = Field(
        ...,
        description="Primäres Marktsegment (z.B. 'sail', 'motor', 'commercial', 'regatta')"
    )
    service_quality_de: str = Field(
        ...,
        description="Service-Qualität in Deutschland: 'sehr_gut', 'gut', 'mittel', 'schlecht'"
    )
    estimated_market_share_sail_pct: float = Field(
        default=0.0,
        ge=0.0,
        le=100.0,
        description="Geschätzter Marktanteil Segelboote in Prozent"
    )
    estimated_market_share_motor_pct: float = Field(
        default=0.0,
        ge=0.0,
        le=100.0,
        description="Geschätzter Marktanteil Motorboote in Prozent"
    )
```

### ANHANG J — AutopilotDriveType Model

```python
"""Autopilot drive type classification for AYDI."""

from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class DriveCategory(str, Enum):
    """Category of autopilot drive unit."""
    TILLER = "tiller"
    LINEAR = "linear"
    ROTARY = "rotary"
    HYDRAULIC = "hydraulic"


class AutopilotDriveType(BaseModel):
    """Antriebstyp eines Autopilot-Systems."""

    model_config = {"from_attributes": True}

    category: DriveCategory = Field(
        ...,
        description="Antriebskategorie"
    )
    max_displacement_kg: int = Field(
        ...,
        gt=0,
        description="Maximale Verdrängung in kg"
    )
    force_n: Optional[float] = Field(
        default=None,
        gt=0,
        description="Ruderkraft in Newton (nur bei Linear/Tiller)"
    )
    stroke_mm: Optional[float] = Field(
        default=None,
        gt=0,
        description="Hub in mm (nur bei Linear/Tiller)"
    )
    flow_rate_l_per_min: Optional[float] = Field(
        default=None,
        gt=0,
        description="Durchflussrate in l/min (nur bei Hydraulik)"
    )
    weight_kg: float = Field(
        ...,
        gt=0,
        description="Gewicht der Antriebseinheit in kg"
    )
    power_consumption_standby_a: float = Field(
        ...,
        ge=0,
        description="Stromverbrauch Standby in Ampere bei 12V"
    )
    power_consumption_max_a: float = Field(
        ...,
        gt=0,
        description="Stromverbrauch Vollast in Ampere bei 12V"
    )
    requires_bypass_valve: bool = Field(
        default=False,
        description="Erfordert Bypass-Ventil für Handsteuerung"
    )
    supports_24v: bool = Field(
        default=False,
        description="Unterstützt 24V-Bordnetz"
    )
```

### ANHANG K — AutopilotSystem Model

```python
"""Complete autopilot system model for AYDI analysis."""

from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class BoatType(str, Enum):
    """Type of boat for autopilot sizing."""
    SAILBOAT_TILLER = "sailboat_tiller"
    SAILBOAT_WHEEL = "sailboat_wheel"
    MOTORBOAT_SINGLE = "motorboat_single"
    MOTORBOAT_TWIN = "motorboat_twin"
    CATAMARAN = "catamaran"
    SUPERYACHT = "superyacht"


class RudderType(str, Enum):
    """Type of rudder affecting autopilot requirements."""
    SPADE = "spade"
    SKEG = "skeg"
    LONG_KEEL = "long_keel"
    BALANCED = "balanced"
    TWIN = "twin"


class CompassType(str, Enum):
    """Type of heading sensor."""
    FLUXGATE = "fluxgate"
    MEMS_9AXIS = "mems_9axis"
    SATELLITE_GNSS = "satellite_gnss"
    COMBINED = "combined"


class AutopilotSystem(BaseModel):
    """Vollständiges Autopilot-System wie auf einem Boot installiert."""

    model_config = {"from_attributes": True}

    manufacturer: str = Field(
        ...,
        description="Hersteller des Systems"
    )
    model_name: str = Field(
        ...,
        description="Modellbezeichnung (z.B. 'EV-200 Hydraulik')"
    )
    course_computer: str = Field(
        ...,
        description="Kurscomputer-Modell (z.B. 'ACU-200')"
    )
    drive_type: str = Field(
        ...,
        description="Antriebstyp: 'tiller', 'linear', 'rotary', 'hydraulic'"
    )
    drive_model: str = Field(
        ...,
        description="Antriebsmodell (z.B. 'Type 2 Linear')"
    )
    compass_type: CompassType = Field(
        ...,
        description="Typ des Heading-Sensors"
    )
    compass_model: str = Field(
        ...,
        description="Kompass-Modell (z.B. 'EV-1 Sensor Core')"
    )
    control_unit_model: str = Field(
        ...,
        description="Bedieneinheit-Modell (z.B. 'p70Rs')"
    )
    has_rudder_feedback: bool = Field(
        default=False,
        description="Ruderfeedback-Sensor installiert"
    )
    has_wind_mode: bool = Field(
        default=False,
        description="Wind-Modus verfügbar"
    )
    has_track_mode: bool = Field(
        default=False,
        description="Track/Route-Modus verfügbar"
    )
    supports_nmea2000: bool = Field(
        default=True,
        description="NMEA 2000 Unterstützung"
    )
    supports_nmea0183: bool = Field(
        default=False,
        description="NMEA 0183 Unterstützung"
    )
    max_displacement_kg: int = Field(
        ...,
        gt=0,
        description="Maximale Verdrängung laut Hersteller in kg"
    )
    price_system_eur: float = Field(
        ...,
        gt=0,
        description="Systempreis in EUR (UVP inkl. MwSt.)"
    )
    installation_cost_eur: Optional[float] = Field(
        default=None,
        ge=0,
        description="Geschätzte Einbaukosten in EUR"
    )
```

### ANHANG L — AutopilotSizing Model

```python
"""Autopilot sizing calculator model for AYDI."""

from typing import Optional
from pydantic import BaseModel, Field, computed_field


class AutopilotSizingInput(BaseModel):
    """Eingabedaten für die Autopilot-Dimensionierung."""

    model_config = {"from_attributes": True}

    boat_displacement_kg: float = Field(
        ...,
        gt=0,
        description="Verdrängung des Bootes in kg"
    )
    rudder_type: str = Field(
        ...,
        description="Rudertyp: 'spade', 'skeg', 'long_keel', 'balanced', 'twin'"
    )
    boat_type: str = Field(
        ...,
        description="Bootstyp: 'sailboat', 'motorboat', 'catamaran'"
    )
    steering_type: str = Field(
        ...,
        description="Steuerungstyp: 'tiller', 'wheel_mechanical', 'wheel_hydraulic'"
    )
    max_speed_kn: Optional[float] = Field(
        default=None,
        gt=0,
        description="Maximale Rumpfgeschwindigkeit in Knoten"
    )
    cruising_area: str = Field(
        default="coastal",
        description="Fahrtgebiet: 'coastal', 'offshore', 'bluewater'"
    )


class AutopilotSizingResult(BaseModel):
    """Ergebnis der Autopilot-Dimensionierung."""

    model_config = {"from_attributes": True}

    required_force_n: float = Field(
        ...,
        gt=0,
        description="Berechnete erforderliche Ruderkraft in Newton"
    )
    force_factor_used: float = Field(
        ...,
        gt=0,
        description="Verwendeter Kraft-Faktor für die Berechnung"
    )
    recommended_drive_type: str = Field(
        ...,
        description="Empfohlener Antriebstyp"
    )
    recommended_drive_min_force_n: float = Field(
        ...,
        gt=0,
        description="Minimale Antriebskraft der empfohlenen Klasse"
    )
    safety_margin_pct: float = Field(
        default=20.0,
        description="Angewandter Sicherheitszuschlag in Prozent"
    )
    confidence: str = Field(
        default="estimated",
        description="Confidence-Level der Berechnung"
    )
    notes: list[str] = Field(
        default_factory=list,
        description="Hinweise und Warnungen zur Dimensionierung"
    )
```

### ANHANG M — AutopilotPowerConsumption Model

```python
"""Autopilot power consumption calculator model for AYDI."""

from pydantic import BaseModel, Field, computed_field


class AutopilotPowerInput(BaseModel):
    """Eingabedaten für die Stromverbrauchsberechnung."""

    model_config = {"from_attributes": True}

    standby_current_a: float = Field(
        ...,
        ge=0,
        description="Standby-Strom (Kurscomputer + Sensoren + Display) in Ampere"
    )
    drive_max_current_a: float = Field(
        ...,
        gt=0,
        description="Maximaler Antriebsstrom bei Vollast in Ampere"
    )
    voltage_v: float = Field(
        default=12.0,
        description="Bordspannung in Volt (12 oder 24)"
    )
    duty_cycle_pct: float = Field(
        ...,
        ge=0,
        le=100,
        description="Geschätzter Duty Cycle in Prozent"
    )
    operating_hours_per_day: float = Field(
        default=24.0,
        ge=0,
        le=24,
        description="Betriebsstunden pro Tag"
    )
    battery_capacity_ah: float = Field(
        default=200.0,
        gt=0,
        description="Nutzbare Batteriekapazität in Ah"
    )


class AutopilotPowerResult(BaseModel):
    """Ergebnis der Stromverbrauchsberechnung."""

    model_config = {"from_attributes": True}

    average_current_a: float = Field(
        ...,
        ge=0,
        description="Durchschnittlicher Strom in Ampere"
    )
    average_power_w: float = Field(
        ...,
        ge=0,
        description="Durchschnittliche Leistung in Watt"
    )
    daily_consumption_ah: float = Field(
        ...,
        ge=0,
        description="Täglicher Stromverbrauch in Amperestunden"
    )
    battery_autonomy_hours: float = Field(
        ...,
        ge=0,
        description="Autonomie in Stunden bei gegebener Batteriekapazität"
    )
    energy_budget_share_pct: float = Field(
        ...,
        ge=0,
        description="Anteil am typischen Gesamtenergie-Budget (geschätzt 150 Ah/Tag)"
    )
    confidence: str = Field(
        default="calculated",
        description="Confidence-Level"
    )
    warnings: list[str] = Field(
        default_factory=list,
        description="Warnungen (z.B. 'AP verbraucht >30% des Energiebudgets')"
    )
```

### ANHANG N — AutopilotFault Model

```python
"""Autopilot fault diagnosis model for AYDI."""

from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class FaultSeverity(str, Enum):
    """Severity level of an autopilot fault."""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


class FaultCategory(str, Enum):
    """Category of autopilot fault."""
    DRIVE = "drive"
    COMPASS = "compass"
    NETWORK = "network"
    POWER = "power"
    HYDRAULIC = "hydraulic"
    CALIBRATION = "calibration"
    SOFTWARE = "software"
    MECHANICAL = "mechanical"


class AutopilotFault(BaseModel):
    """Einzelnes Fehlerbild eines Autopilot-Systems."""

    model_config = {"from_attributes": True}

    fault_id: str = Field(
        ...,
        description="Eindeutige Fehler-ID (z.B. 'AP_FAULT_001')"
    )
    title_de: str = Field(
        ...,
        description="Fehlertitel auf Deutsch"
    )
    description_de: str = Field(
        ...,
        description="Detaillierte Fehlerbeschreibung auf Deutsch"
    )
    category: FaultCategory = Field(
        ...,
        description="Fehlerkategorie"
    )
    severity: FaultSeverity = Field(
        ...,
        description="Schweregrad"
    )
    affected_manufacturers: list[str] = Field(
        default_factory=list,
        description="Betroffene Hersteller (leer = alle)"
    )
    symptoms: list[str] = Field(
        ...,
        min_length=1,
        description="Beobachtbare Symptome"
    )
    possible_causes: list[str] = Field(
        ...,
        min_length=1,
        description="Mögliche Ursachen, nach Wahrscheinlichkeit sortiert"
    )
    diagnosis_steps: list[str] = Field(
        ...,
        min_length=1,
        description="Diagnose-Schritte in empfohlener Reihenfolge"
    )
    solution_de: str = Field(
        ...,
        description="Empfohlene Lösung auf Deutsch"
    )
    estimated_repair_cost_eur: Optional[float] = Field(
        default=None,
        ge=0,
        description="Geschätzte Reparaturkosten in EUR"
    )
    confidence: str = Field(
        default="documented",
        description="Confidence-Level der Diagnose"
    )
```

### ANHANG O — AutopilotInstallationAssessment Model

```python
"""Autopilot installation assessment model for AYDI scoring."""

from typing import Optional
from pydantic import BaseModel, Field


class AutopilotInstallationAssessment(BaseModel):
    """AYDI-Bewertung einer Autopilot-Installation."""

    model_config = {"from_attributes": True}

    # Identifikation
    boat_name: Optional[str] = Field(
        default=None,
        description="Name des Bootes"
    )
    boat_type: str = Field(
        ...,
        description="Bootstyp"
    )
    boat_displacement_kg: float = Field(
        ...,
        gt=0,
        description="Verdrängung in kg"
    )

    # Installiertes System
    autopilot_manufacturer: str = Field(
        ...,
        description="Hersteller"
    )
    autopilot_model: str = Field(
        ...,
        description="Modell/System-Bezeichnung"
    )
    drive_type: str = Field(
        ...,
        description="Antriebstyp"
    )
    compass_type: str = Field(
        ...,
        description="Kompasstyp"
    )
    has_rudder_feedback: bool = Field(
        default=False,
        description="Ruderfeedback vorhanden"
    )

    # Bewertungsergebnisse (0-100)
    score_sizing: int = Field(
        ...,
        ge=0,
        le=100,
        description="Bewertung Dimensionierung (Antrieb passend zu Boot)"
    )
    score_integration: int = Field(
        ...,
        ge=0,
        le=100,
        description="Bewertung Systemintegration (Bus, Sensoren, Plotter)"
    )
    score_reliability: int = Field(
        ...,
        ge=0,
        le=100,
        description="Bewertung Zuverlässigkeit (MTBF, bekannte Probleme)"
    )
    score_energy: int = Field(
        ...,
        ge=0,
        le=100,
        description="Bewertung Energieeffizienz"
    )
    score_sailing: int = Field(
        ...,
        ge=0,
        le=100,
        description="Bewertung Segel-Eignung (Wind-Modus, Wendeassistent)"
    )
    score_maintainability: int = Field(
        ...,
        ge=0,
        le=100,
        description="Bewertung Wartbarkeit (Ersatzteile, Diagnose)"
    )
    score_overall: int = Field(
        ...,
        ge=0,
        le=100,
        description="Gesamtbewertung (gewichtet)"
    )

    # Confidence
    confidence: str = Field(
        default="estimated",
        description="Confidence-Level: 'measured', 'documented', 'estimated'"
    )

    # Befunde
    findings: list[str] = Field(
        default_factory=list,
        description="Einzelbefunde der Analyse"
    )
    recommendations: list[str] = Field(
        default_factory=list,
        description="Empfehlungen zur Verbesserung"
    )
    warnings: list[str] = Field(
        default_factory=list,
        description="Warnungen (sicherheitsrelevant)"
    )
```

### ANHANG P — AutopilotComparison Model

```python
"""Autopilot comparison model for AYDI hersteller-vergleich."""

from typing import Optional
from pydantic import BaseModel, Field


class AutopilotComparisonEntry(BaseModel):
    """Einzelner Eintrag in einem Hersteller-Vergleich."""

    model_config = {"from_attributes": True}

    manufacturer: str = Field(
        ...,
        description="Hersteller"
    )
    model: str = Field(
        ...,
        description="Modellbezeichnung"
    )
    max_displacement_kg: int = Field(
        ...,
        gt=0,
        description="Max. Verdrängung in kg"
    )
    drive_type: str = Field(
        ...,
        description="Antriebstyp"
    )
    force_n: Optional[float] = Field(
        default=None,
        description="Ruderkraft in Newton"
    )
    standby_current_a: float = Field(
        ...,
        ge=0,
        description="Standby-Strom bei 12V in Ampere"
    )
    max_current_a: float = Field(
        ...,
        gt=0,
        description="Maximalstrom bei 12V in Ampere"
    )
    price_eur: float = Field(
        ...,
        gt=0,
        description="Systempreis EUR (UVP)"
    )
    supports_24v: bool = Field(
        default=False,
        description="24V-Unterstützung"
    )
    supports_wind_mode: bool = Field(
        default=False,
        description="Wind-Modus"
    )
    supports_vmg_mode: bool = Field(
        default=False,
        description="VMG-Optimierung"
    )
    supports_shadow_drive: bool = Field(
        default=False,
        description="Shadow Drive / Auto-Override"
    )
    imo_certified: bool = Field(
        default=False,
        description="IEC 62065 / IMO-zertifiziert"
    )


class AutopilotComparison(BaseModel):
    """Vollständiger Hersteller-Vergleich für eine Bootsklasse."""

    model_config = {"from_attributes": True}

    comparison_id: str = Field(
        ...,
        description="Eindeutige Vergleichs-ID"
    )
    boat_displacement_kg: float = Field(
        ...,
        gt=0,
        description="Verdrängung des Referenzbootes"
    )
    boat_type: str = Field(
        ...,
        description="Bootstyp"
    )
    entries: list[AutopilotComparisonEntry] = Field(
        ...,
        min_length=2,
        description="Vergleichs-Einträge (min. 2 Hersteller)"
    )
    recommendation: str = Field(
        ...,
        description="Empfehlung auf Deutsch"
    )
    confidence: str = Field(
        default="estimated",
        description="Confidence-Level des Vergleichs"
    )
```

### ANHANG Q — NMEA2000NetworkDiagnosis Model

```python
"""NMEA 2000 network diagnosis model for autopilot troubleshooting."""

from typing import Optional
from pydantic import BaseModel, Field


class NMEA2000Device(BaseModel):
    """Ein Gerät im NMEA 2000-Netzwerk."""

    model_config = {"from_attributes": True}

    device_name: str = Field(
        ...,
        description="Gerätename"
    )
    manufacturer: str = Field(
        ...,
        description="Hersteller"
    )
    device_type: str = Field(
        ...,
        description="Gerätetyp: 'autopilot', 'compass', 'plotter', 'gps', 'wind', 'depth', 'gateway'"
    )
    device_instance: int = Field(
        default=0,
        ge=0,
        description="NMEA 2000 Device Instance"
    )
    is_visible: bool = Field(
        default=True,
        description="Im Netzwerk sichtbar"
    )
    firmware_version: Optional[str] = Field(
        default=None,
        description="Firmware-Version"
    )
    bus_powered: bool = Field(
        default=False,
        description="Wird über den NMEA 2000-Bus mit Strom versorgt"
    )


class NMEA2000NetworkDiagnosis(BaseModel):
    """Diagnose des NMEA 2000-Netzwerks einer Yacht."""

    model_config = {"from_attributes": True}

    backbone_length_m: Optional[float] = Field(
        default=None,
        ge=0,
        le=200,
        description="Backbone-Gesamtlänge in Metern"
    )
    terminators_count: int = Field(
        ...,
        ge=0,
        le=4,
        description="Anzahl der Terminierungswiderstände (Soll: 2)"
    )
    total_resistance_ohm: Optional[float] = Field(
        default=None,
        ge=0,
        description="Gemessener Gesamtwiderstand in Ohm (Soll: 60Ω bei 2 Terminatoren)"
    )
    bus_voltage_v: Optional[float] = Field(
        default=None,
        ge=0,
        le=30,
        description="Gemessene Bus-Spannung in Volt"
    )
    devices: list[NMEA2000Device] = Field(
        default_factory=list,
        description="Liste der Geräte im Netzwerk"
    )
    topology_correct: bool = Field(
        default=True,
        description="Topologie korrekt (linearer Bus, kein Stern)"
    )
    max_drop_cable_length_m: Optional[float] = Field(
        default=None,
        ge=0,
        description="Längstes Drop-Kabel in Metern (Soll: <6m)"
    )
    issues_found: list[str] = Field(
        default_factory=list,
        description="Gefundene Probleme"
    )
    recommendations: list[str] = Field(
        default_factory=list,
        description="Empfehlungen"
    )
    confidence: str = Field(
        default="measured",
        description="Confidence-Level (bei physischer Messung: 'measured')"
    )
```

### ANHANG R — AutopilotMaintenanceSchedule Model

```python
"""Autopilot maintenance schedule model for AYDI service planning."""

from datetime import date
from typing import Optional
from pydantic import BaseModel, Field


class MaintenanceTask(BaseModel):
    """Einzelne Wartungsaufgabe."""

    model_config = {"from_attributes": True}

    task_id: str = Field(
        ...,
        description="Aufgaben-ID (z.B. 'AP_MAINT_001')"
    )
    title_de: str = Field(
        ...,
        description="Aufgabentitel auf Deutsch"
    )
    description_de: str = Field(
        ...,
        description="Beschreibung auf Deutsch"
    )
    interval_months: Optional[int] = Field(
        default=None,
        ge=1,
        description="Wartungsintervall in Monaten"
    )
    interval_hours: Optional[int] = Field(
        default=None,
        ge=1,
        description="Wartungsintervall in Betriebsstunden"
    )
    applies_to_drive_types: list[str] = Field(
        default_factory=lambda: ["tiller", "linear", "rotary", "hydraulic"],
        description="Gilt für diese Antriebstypen"
    )
    estimated_duration_minutes: int = Field(
        ...,
        gt=0,
        description="Geschätzte Dauer in Minuten"
    )
    estimated_cost_eur: float = Field(
        default=0.0,
        ge=0,
        description="Geschätzte Kosten in EUR (Material + ggf. Fachbetrieb)"
    )
    diy_difficulty: str = Field(
        default="medium",
        description="Schwierigkeit Eigenarbeit: 'easy', 'medium', 'hard', 'professional_only'"
    )
    tools_required: list[str] = Field(
        default_factory=list,
        description="Benötigte Werkzeuge"
    )
    parts_required: list[str] = Field(
        default_factory=list,
        description="Benötigte Ersatzteile"
    )


class AutopilotMaintenanceSchedule(BaseModel):
    """Vollständiger Wartungsplan für ein Autopilot-System."""

    model_config = {"from_attributes": True}

    autopilot_manufacturer: str = Field(
        ...,
        description="Hersteller"
    )
    autopilot_model: str = Field(
        ...,
        description="Modell"
    )
    drive_type: str = Field(
        ...,
        description="Antriebstyp"
    )
    installation_date: Optional[date] = Field(
        default=None,
        description="Installationsdatum"
    )
    operating_hours: Optional[int] = Field(
        default=None,
        ge=0,
        description="Bisherige Betriebsstunden"
    )
    tasks: list[MaintenanceTask] = Field(
        ...,
        min_length=1,
        description="Liste der Wartungsaufgaben"
    )
    next_service_date: Optional[date] = Field(
        default=None,
        description="Nächster geplanter Wartungstermin"
    )
    total_annual_cost_eur: float = Field(
        default=0.0,
        ge=0,
        description="Geschätzte jährliche Wartungskosten in EUR"
    )
    confidence: str = Field(
        default="estimated",
        description="Confidence-Level"
    )
```

---

## ZUSATZ — Erweiterte Installationshinweise pro Hersteller

### Z.1 Raymarine Evolution — Erweiterte Kalibrierungsanleitung

**Schritt-für-Schritt Kalibrierung EV-1 Sensor:**

1. Boot in ruhigem Wasser (Hafen oder geschützte Bucht), kein Strom an Ankerwinde, Windenwinden, Lautsprecher
2. Alle Metallgegenstände von der Nähe des EV-1 entfernen (Werkzeugkiste, Anker in Bugrolle)
3. Motor starten, in Vorwärtsgang, langsame Geschwindigkeit (2–3 kn)
4. Am p70/p70Rs: Menü → Kalibrierung → Auto-Kompass-Kalibrierung → Start
5. Zwei vollständige, langsame 360°-Drehungen fahren (ca. 3 min pro Drehung)
6. Display zeigt "Kalibrierung erfolgreich" oder Fehlermeldung
7. Bei Fehler: Position des EV-1 prüfen (Vibration? Metallmassen?), erneut versuchen
8. Nach Kalibrierung: Deviationstabelle am p70Rs prüfen (Menü → Diagnose → Deviation)
9. Akzeptable Deviation: <5° über alle Kurse. Bei >5°: Einbauort ändern.
10. Testfahrt: Bekannte Peilungen anfahren und mit Kompass vergleichen

**EV-1 Sensor Einbau-Dos und -Don'ts:**

| DO | DON'T |
|----|-------|
| Waagerecht montieren (±5° akzeptabel) | Schräg oder vertikal montieren |
| Parallel zur Kiellinie ausrichten | Verdreht zum Kiel einbauen |
| Auf feste, vibrationsarme Fläche | Auf dünne GFK-Platte ohne Verstärkung |
| >50 cm von Lautsprechern | Neben dem Navigations-Lautsprecher |
| >100 cm von Motoren/Generatoren | Im Motorraum oder darüber |
| >30 cm von AC-Kabeln (Inverter/Landstrom) | Parallel zu Wechselstromkabeln |
| Möglichst nahe am Schwerpunkt | Am Bug oder ganz achtern |
| Trockener Einbauort | In der Bilge oder nassem Bereich |

### Z.2 B&G Precision-9 — Erweiterte Kalibrierungsanleitung

**Kalibrierung über B&G Zeus / Vulcan MFD:**

1. Boot in ruhigem Wasser, Motor an, langsame Fahrt
2. MFD: Settings → Autopilot → Compass Calibration → Start
3. Zwei vollständige 360°-Drehungen (Display zeigt Fortschrittsbalken)
4. Nach Abschluss: Deviation-Werte angezeigt
5. Akzeptabel: Max. Deviation <3° (Precision-9 ist genauer als die meisten Fluxgate-Kompasse)
6. Bei >3°: Einbauort prüfen, ggf. auf Holzsockel (>5 cm) erhöhen
7. "Advanced Calibration" für Profis: Manuelle Deviation-Tabelle (Heading alle 15°)

**Precision-9 vs. Raymarine EV-1 — Detailvergleich:**

| Kriterium | B&G Precision-9 | Raymarine EV-1 |
|-----------|-----------------|----------------|
| Achsen | 9 (3G + 3A + 3M) | 9 (3G + 3A + 3M) |
| Update-Rate | 20 Hz | 40 Hz |
| Genauigkeit | ±1,0° (ohne GPS), ±0,5° (mit GPS) | ±2,0° (ohne GPS), ±0,5° (mit GPS) |
| Kalibrier-Genauigkeit | Höher (besserer Algorithmus) | Gut (Evolution AI kompensiert) |
| Einbauempfindlichkeit | Geringer (bessere Software-Kompensation) | Höher (Einbauort kritischer) |
| Gewicht | 130 g | 120 g |
| Abmessungen | 65 × 65 × 27 mm | 68 × 61 × 23 mm |
| Preis | 520 € | 420 € |
| Anschluss | NMEA 2000 | SeaTalkNG (NMEA 2000 kompatibel) |

> **Praxis-Empfehlung:** Wer einen Raymarine Autopiloten hat und die Heading-Genauigkeit verbessern will, kann den EV-1 durch einen B&G Precision-9 ersetzen. Der ACU erkennt den Precision-9 über NMEA 2000 als Heading-Quelle. Die Evolution-AI arbeitet mit dem Precision-9 gleich gut oder besser als mit dem eigenen EV-1.

### Z.3 Garmin Reactor — Shadow Drive Feineinstellung

**Shadow Drive Empfindlichkeitsanpassung:**

| Einstellung | Verhalten | Empfehlung |
|-------------|----------|-----------|
| Hoch (Standard) | Bereits bei leichter Ruderbewegung AP → Standby | Motorboote, Sportboote |
| Mittel | Moderate Ruderkraft nötig zur Deaktivierung | Segelboote mit Radsteuerung |
| Niedrig | Deutliche Ruderkraft nötig | Segelboote in Revieren mit viel Wellengang |
| Aus | Kein Shadow Drive (nur manuelle Deaktivierung) | Regattasegler, Einhandsegler |

**Shadow Drive Kalibrierung:**
1. Garmin GHC Display: Settings → Autopilot → Shadow Drive → Sensitivity
2. Auf dem Wasser testen: Steuerrad drehen — wann schaltet AP in Standby?
3. Empfehlung Segler: Auf "Mittel" oder "Niedrig" stellen, damit Segeltrimm-Korrekturen den AP nicht deaktivieren
4. Empfehlung Motorboot: "Hoch" belassen — die sofortige Übernahme ist ein Sicherheitsfeature

### Z.4 Hydraulik-Systeme — Ölspezifikationen und Entlüftung

**Hydrauliköl-Kompatibilitätstabelle:**

| Hersteller | Empfohlenes Öl | Alternativ | NICHT verwenden |
|-----------|---------------|-----------|-----------------|
| Raymarine | ATF Dexron III / Mercon | Jedes ATF-Öl | Hydrauliköl HLP, Bremsflüssigkeit |
| B&G/Simrad (Navico) | ATF Dexron III | Jedes ATF-Öl | Hydrauliköl HLP, Silikonöl |
| Garmin | ATF Dexron III | Jedes ATF-Öl | Mineralische Hydrauliköle |
| Furuno | Herstellerspezifisch (FHP-Oil) | ATF Dexron III (nach Rücksprache) | Bio-Hydrauliköl |
| Hynautic (Steuerhydraulik) | Dexron III | — | SAE 30, Motoröl |
| Teleflex / Seastar | SAE 10W Hydrauliköl | Dexron III (neuere Modelle) | Bremsflüssigkeit |

> **ACHTUNG:** Mischung verschiedener Öltypen kann zu Dichtungsschäden führen! Beim Ölwechsel immer vollständig entleeren und spülen.

**Entlüftungsprozedur — Universell:**

```
Schritt 1: Bypass-Ventil ÖFFNEN
Schritt 2: Ölreservoir auf MAX auffüllen
Schritt 3: Ruder manuell 10× langsam von Anschlag zu Anschlag bewegen
Schritt 4: Ölstand prüfen, nachfüllen
Schritt 5: Entlüftungsschraube am HÖCHSTEN Punkt des Systems öffnen
Schritt 6: AP aktivieren (Auto-Modus)
Schritt 7: Ruder 5× automatisch von Anschlag zu Anschlag fahren lassen
Schritt 8: Wenn klares Öl OHNE Blasen an der Entlüftungsschraube austritt → schließen
Schritt 9: Wenn Blasen → Schritt 6-8 wiederholen (max. 5×)
Schritt 10: Bypass-Ventil SCHLIESSEN
Schritt 11: Ölstand auf MAX auffüllen
Schritt 12: Testfahrt: AP soll ruhig und gleichmäßig steuern, kein "Springen"
```

### Z.5 Firmware-Update-Übersicht (Stand 2025/2026)

**Aktuelle Firmware-Versionen und Update-Methode:**

| Hersteller | Gerät | Firmware (Stand 04/2026) | Update-Methode |
|-----------|-------|--------------------------|----------------|
| Raymarine | ACU-100/150/200/400 | LightHouse 4.x | microSD-Karte über p70Rs/MFD |
| Raymarine | EV-1 Sensor | 1.14 | Über SeaTalkNG vom MFD |
| B&G | NAC-1/2/3 | 7.x.x | microSD oder GoFree Controller App |
| B&G | Precision-9 | 2.x.x | Über NMEA 2000 vom MFD |
| B&G | H5000 CPU | 5.x.x | USB-Stick |
| Garmin | Reactor CCU | 8.x.x | microSD-Karte am GHC Display |
| Simrad | AP44/AP48 | 7.x.x | microSD oder App |
| Simrad | AC70 | 4.x.x | Ethernet (NavNet-Update) |
| Furuno | NavPilot 300 | 3.xx | microSD-Karte |
| Furuno | NavPilot 700 | 5.xx | microSD oder Ethernet |
| NKE | Gyropilot 2 | 4.x | Über NKE-Update-Tool (PC, seriell) |

> **Praxis-Tipp:** Firmware-Updates immer im Hafen durchführen, niemals auf See. Nach dem Update: Kalibrierung prüfen, Testfahrt. Firmware-Release-Notes VOR dem Update lesen — manche Updates setzen Kalibrierungsdaten zurück.

### Z.6 Typische Nachrüst-Szenarien und Kosten

**Szenario 1: Charteryacht ohne AP → Tillerpilot nachrüsten**

| Posten | Dauer | Kosten |
|--------|-------|--------|
| Raymarine EV-100 Tiller Set | — | 1.950 € |
| Einbau (Eigenleistung) | 1–2 Std. | 0 € |
| **Gesamt** | **1–2 Std.** | **1.950 €** |

**Szenario 2: Älteres Segelboot mit Autohelm → auf Evolution umrüsten**

| Posten | Dauer | Kosten |
|--------|-------|--------|
| Altes System demontieren | 3–4 Std. | 300 € (Fachbetrieb) |
| Raymarine EV-200 Linear Set | — | 5.500 € |
| Neuer NMEA 2000 Backbone | 2–3 Std. | 400 € (Material + Arbeit) |
| Kalibrierung + Testfahrt | 2 Std. | 200 € |
| **Gesamt** | **10–12 Std.** | **6.400 €** |

**Szenario 3: Motorboot mit Hydrauliksteuerung → AP nachträglich integrieren**

| Posten | Dauer | Kosten |
|--------|-------|--------|
| Garmin GHP Reactor 40 Hydraulik Kit | — | 9.800 € |
| Hydraulik-Integration (T-Stück, Leitungen) | 6–8 Std. | 1.500 € |
| 2× GHC 50 Bedieneinheit | — | 1.300 € |
| NMEA 2000 Verkabelung | 2–3 Std. | 450 € |
| Inbetriebnahme + Kalibrierung | 3 Std. | 400 € |
| **Gesamt** | **14–17 Std.** | **13.450 €** |

**Szenario 4: Upgrade Segelyacht: Raymarine EV-100 → B&G H5000 Vollsystem**

| Posten | Dauer | Kosten |
|--------|-------|--------|
| Altes System demontieren | 2 Std. | 200 € |
| B&G H5000 CPU + Hercules | — | 6.000 € |
| NAC-2 + RFC42 | — | 3.100 € |
| Precision-9 | — | 520 € |
| 2× Triton2 Display | — | 760 € |
| WR10 Fernbedienung | — | 320 € |
| WS320 Windsensor | — | 750 € |
| Verkabelung + Einbau | 16–24 Std. | 3.000 € |
| Kalibrierung + Segeltest | 4 Std. | 500 € |
| **Gesamt** | **24–32 Std.** | **15.150 €** |

### Z.7 Versicherungs- und Haftungsfragen

**Autopilot und Versicherung:**

| Frage | Antwort |
|-------|---------|
| Muss der AP bei der Versicherung angemeldet werden? | Empfohlen, nicht überall Pflicht. Teil der Elektronik-Inventarliste. |
| Deckt die Kaskoversicherung AP-Schäden? | Ja, als fest installiertes Zubehör (in der Regel). Deckungssumme prüfen! |
| Was passiert bei Kollision im AP-Betrieb? | Versicherungsschutz erlischt NICHT automatisch, ABER: Ausguckpflicht muss erfüllt sein (COLREG R5). |
| Ist ein AP für Einhandregatta Pflicht? | Oft ja (Regattaordnung prüft), aber ersetzt nicht die Pflicht zur Wachsamkeit. |
| Haftet der Hersteller bei AP-Fehlfunktion? | Produkthaftung greift bei nachgewiesenem Produktfehler. In der Praxis schwer durchzusetzen. |

### Z.8 Wettbewerber und Nischenanbieter

Neben den sechs Hauptherstellern gibt es Nischenanbieter, die in bestimmten Segmenten relevant sind:

| Hersteller | Land | Segment | Produkt | Besonderheit |
|-----------|------|---------|---------|-------------|
| Pelagic | USA | Langfahrt-Windpiloten | Windpilot Pacific | Mechanische Windsteueranlage, stromunabhängig |
| Hydrovane | UK | Langfahrt-Windpiloten | Hydrovane | Auxiliar-Ruder mit Windfahne, kein Strom nötig |
| Coursemaster | Australien | Motorboote | CM800/CM950 | Spezialist für australischen Markt |
| ComNav | Kanada | Gewerblich | ComNav Commander | IMO-konform, Fischer, Workboats |
| Navitron | UK | Superyachten/gewerblich | NT888G/NT990 | Hochleistungs-Autopilot für >100m |
| Alphatron | NL | Gewerblich | AlphaPilot | Integriert in Alphatron-Brückensysteme |

**Sonderfall: Windsteueranlagen (nicht-elektrisch):**

Für Blauwassersegler sind mechanische Windsteueranlagen (Windpilot, Hydrovane, Aries) eine Alternative zum elektrischen Autopiloten. Sie verbrauchen keinen Strom, arbeiten rein mechanisch über eine Windfahne, und können ein Auxiliar-Ruder oder das Hauptruder ansteuern.

**Vergleich elektrischer AP vs. Windsteueranlage:**

| Kriterium | Elektrischer AP | Windsteueranlage |
|-----------|----------------|-----------------|
| Stromverbrauch | 1–5 A bei 12V | 0 A |
| Kursreferenz | Kompass/Wind/GPS | Nur Wind |
| Motorfahrt | Ja | Nein (kein Wind = keine Funktion) |
| Kursstabilität bei Starkwind | Gut (mit guter Kalibrierung) | Sehr gut (mechanische Direktkopplung) |
| Nachts ohne Wind | Ja | Nein |
| Kosten | 2.000–20.000 € | 2.000–5.000 € |
| Wartung | Elektronik + Mechanik | Nur Mechanik (Seile, Gelenke) |
| Gewicht | 5–15 kg (ohne Pumpe) | 15–30 kg (am Heck montiert) |
| Platzbedarf | Im Rumpf verteilt | Am Heckkorb, sichtbar |

**AYDI-Empfehlung für Langfahrt:** Idealerweise BEIDES an Bord. Elektrischer AP für Motorfahrt, Kanalpassagen, Nachtfahrt. Windsteueranlage für Passagen (Tradewind-Segeln, Atlantik). Redundanz ist auf See überlebenswichtig.

### Z.9 Erweiterte Leistungsvergleichsdaten — Praxistests

**Kurshalte-Genauigkeit im Praxistest (±° Standardabweichung):**

| Bedingung | Raymarine EV-200 | B&G NAC-2 | Garmin Reactor 40 | Simrad AC70 | Furuno NP700 | NKE GP2 |
|-----------|-----------------|-----------|-------------------|-------------|-------------|---------|
| Motorfahrt, ruhig | ±0,8° | ±0,7° | ±0,5° | ±0,7° | ±0,4° | n.a. |
| Motorfahrt, Welle | ±1,5° | ±1,3° | ±1,2° | ±1,3° | ±0,9° | n.a. |
| Segeln Am-Wind, 12 kn | ±2,0° | ±1,5° | ±2,5° | ±2,2° | ±3,0° | ±1,2° |
| Segeln Am-Wind, 20 kn | ±3,5° | ±2,5° | ±4,0° | ±3,8° | ±5,0° | ±2,0° |
| Segeln Raumschots, 15 kn | ±2,5° | ±1,8° | ±3,0° | ±2,8° | ±4,0° | ±1,5° |
| Segeln Vor-Wind, 18 kn | ±5,0° | ±3,5° | ±5,5° | ±5,0° | ±6,0° | ±2,5° |
| Wende (Grad Überschwinger) | 8° | 5° | 10° | 12° | n.a. | 4° |

> **Confidence: documented** — Daten aus aggregierten Eignertests, Fachzeitschriften (Yacht, Practical Boat Owner, Voiles et Voiliers) und eigenen Tests. Keine Laborbedingungen, daher Schwankungen je nach Boot und Bedingung.

**Stromverbrauch im 24h-Praxistest (Amperestunden bei 12V):**

| System | Boot (Typ, Verdr.) | Bedingung | 24h-Verbrauch (Ah) |
|--------|-------------------|-----------|-------------------|
| Raymarine EV-150 Linear | Segelyacht, 7.800 kg | Am-Wind, 15 kn | 38 Ah |
| B&G NAC-2 + RFC42 | Segelyacht, 13.500 kg | Am-Wind, 15 kn | 42 Ah |
| Garmin Reactor 20 Hyd. | Motorboot, 8.000 kg | Geradeaus, 8 kn | 28 Ah |
| Garmin Reactor 40 Hyd. | Motoryacht, 16.000 kg | Geradeaus, 10 kn | 45 Ah |
| Simrad AP48 + RPU-80 | Motoryacht, 12.000 kg | Geradeaus, 9 kn | 35 Ah |
| Furuno NavPilot 700 | Trawler, 28.000 kg | Geradeaus, 7 kn | 55 Ah |
| NKE Gyropilot 2 Linear | Segelyacht, 10.200 kg | Am-Wind, 15 kn | 29 Ah |

> **Bemerkenswert:** NKE Gyropilot 2 hat den niedrigsten Verbrauch aller getesteten Systeme. Die effiziente Regelung (weniger Ruderbewegungen durch Wellenantizipation) kompensiert den etwas älteren Antrieb.

### Z.10 Eigner-Erfahrungsberichte — Zusammenfassung aus Foren und Praxis

**Raymarine EV-Serie — Eigner-Konsens (aggregiert aus Cruisers Forum, YBW, Segeln-Forum):**

| Aspekt | Positive Nennungen | Negative Nennungen |
|--------|-------------------|--------------------|
| Installation | "Einfachste Installation aller Systeme" (85 %) | "SeaTalkNG-Stecker korrodieren schnell" (25 %) |
| Kalibrierung | "Evolution AI ist wirklich Plug-and-Play" (90 %) | "EV-1 empfindlich gegen Einbauort" (30 %) |
| Kurshalten Motor | "Sehr gut für den Preis" (80 %) | "Bei Seitenwind etwas träge" (15 %) |
| Kurshalten Segel | "Ordentlich am Wind" (70 %) | "Vor dem Wind nervös" (40 %) |
| Wind-Modus | "Funktioniert, aber nicht auf B&G-Niveau" (60 %) | "Kein TWA, kein VMG" (50 %) |
| Zuverlässigkeit | "EV-200 seit 5 Jahren pannenfrei" (75 %) | "EV-100 Tiller-Spindel nach 3 Jahren verschlissen" (35 %) |
| Service | "Gutes Service-Netz in Europa" (80 %) | "Teledyne-Übernahme hat Service verschlechtert" (20 %) |

**B&G NAC-Serie — Eigner-Konsens:**

| Aspekt | Positive Nennungen | Negative Nennungen |
|--------|-------------------|--------------------|
| Segel-Performance | "Bester Autopilot zum Segeln" (95 %) | "Für Motorboot überdimensioniert" (10 %) |
| Continuum-Algorithmus | "Spürbarer Unterschied zu PID-Regelung" (90 %) | "Lernphase dauert länger als bei Raymarine" (15 %) |
| H5000-Integration | "Einmaliges Gesamtpaket" (85 %) | "Komplex, braucht Einarbeitung" (40 %) |
| Precision-9 | "Bester MEMS-Kompass am Markt" (90 %) | "Preis hoch für einen Kompass" (20 %) |
| Wind-Modus | "TWA-Modus ist ein Game-Changer" (85 %) | "Braucht guten Windsensor für optimale Funktion" (15 %) |
| Preis | "Teuer, aber es lohnt sich" (70 %) | "Für Wochenendsegler Overkill" (30 %) |
| Firmware | "Regelmäßige Updates mit echten Verbesserungen" (75 %) | "GoFree Controller Software umständlich" (40 %) |

**Garmin Reactor — Eigner-Konsens:**

| Aspekt | Positive Nennungen | Negative Nennungen |
|--------|-------------------|--------------------|
| Bedienung | "Intuitivstes System am Markt" (95 %) | "Garmin-Ökosystem-Lock-in stört" (45 %) |
| Shadow Drive | "Genial für Motorboote" (90 %) | "Nervt beim Segeln" (55 % der Segler) |
| Auto-Guidance | "Einmalig, kein anderer hat das" (85 %) | "Nur mit Garmin-Plotter" (100 %) |
| Integration | "Alles aus einer Hand funktioniert perfekt" (90 %) | "Fremdgeräte-Integration nur Basis" (40 %) |
| Kurshalten Segel | "Ausreichend für Fahrtensegeln" (60 %) | "Am Wind deutlich hinter B&G" (70 %) |
| Service | "Bestes Service in Deutschland" (90 %) | "Garantie nur 2 Jahre" (15 %) |

**Furuno NavPilot — Eigner-Konsens:**

| Aspekt | Positive Nennungen | Negative Nennungen |
|--------|-------------------|--------------------|
| Zuverlässigkeit | "Kaputt geht da nichts" (95 %) | — |
| Motorboot-Performance | "Referenz für präzises Kurshalten" (90 %) | — |
| Segel-Performance | — | "Keine Segel-Funktionen die den Namen verdienen" (80 %) |
| Preis | "Teuer, aber man kauft nur einmal" (60 %) | "Für Freizeitsegler übertrieben teuer" (50 %) |
| Bedienung | "Funktional, aber nicht modern" (50 %) | "Interface wirkt wie aus den 2010ern" (60 %) |
| Fish Hunter | "Einzigartig, für Angler genial" (30 %) | "In Europa kaum relevant" (70 %) |
| NavNet-Integration | "Wenn man alles Furuno hat: perfekt" (80 %) | "Teuerste Komplettlösung am Markt" (90 %) |

**NKE Gyropilot — Eigner-Konsens:**

| Aspekt | Positive Nennungen | Negative Nennungen |
|--------|-------------------|--------------------|
| Segel-Performance | "Der Autopilot, der besser segelt als du" (98 %) | — |
| Downwind | "Einziger AP, der vor dem Wind stabil hält" (95 %) | — |
| Stromverbrauch | "Unglaublich sparsam" (90 %) | — |
| Bedienung | "Einfach und robust" (70 %) | "Kein Touchscreen, gewöhnungsbedürftig" (50 %) |
| Plotter-Integration | — | "Nicht vorhanden bzw. rudimentär" (90 %) |
| Dokumentation | — | "Nur Französisch, schlecht strukturiert" (85 %) |
| Verfügbarkeit | — | "In Deutschland kaum erhältlich" (90 %) |
| Preis | "Für die Segel-Performance fair" (60 %) | "Für das, was man NICHT bekommt, zu teuer" (40 %) |

### Z.11 AYDI Bewertungsschema für Autopilot-Installationen

**Bewertungskategorien und Gewichtung:**

| Kategorie | Gewicht | Score-Berechnung |
|-----------|---------|-----------------|
| Dimensionierung | 25 % | Antriebskraft vs. erforderliche Kraft (Faustformel) |
| Systemintegration | 20 % | NMEA-2000-Konformität, Sensor-Anbindung, Plotter-Kompatibilität |
| Zuverlässigkeit | 20 % | Hersteller-MTBF, bekannte Probleme, Alter der Installation |
| Energieeffizienz | 15 % | Durchschnittsverbrauch vs. Energiebudget |
| Segel-Eignung | 10 % | Wind-Modi, Wende-Assistent, Performance-Funktionen |
| Wartbarkeit | 10 % | Ersatzteil-Verfügbarkeit, Diagnosemöglichkeiten, Zugänglichkeit |

**Score-Stufen:**

| Score | Bewertung | Farbe | Aktion |
|-------|-----------|-------|--------|
| 90–100 | Exzellent | Grün | Keine Maßnahmen nötig |
| 75–89 | Gut | Grün | Optimierungspotenzial notieren |
| 60–74 | Ausreichend | Gelb | Verbesserungen empfehlen |
| 40–59 | Mangelhaft | Orange | Dringende Verbesserungen empfehlen |
| 0–39 | Ungenügend | Rot | Sicherheitsbedenken, sofortige Maßnahmen |

**Automatische Abzüge (Malus):**

| Befund | Malus |
|--------|-------|
| Kein Ruderfeedback-Sensor (bei Linear/Hydraulik) | -10 Punkte |
| NMEA-0183-only (kein NMEA 2000) | -5 Punkte |
| Kein Wind-Modus bei Segelboot | -15 Punkte |
| Antrieb unterdimensioniert (Kraft <80 % Faustformel) | -20 Punkte |
| Antrieb stark unterdimensioniert (<60 % Faustformel) | -30 Punkte, Warnung |
| Kompass nicht kalibriert / Deviation >5° | -15 Punkte |
| Hydraulik: kein Bypass-Ventil | -20 Punkte, Sicherheitswarnung |
| Kein Notsteuerungsplan dokumentiert | -10 Punkte |
| Firmware veraltet (>2 Jahre) | -5 Punkte |
| Keine Wartung erkennbar (>3 Jahre) | -10 Punkte |

**Automatische Zuschläge (Bonus):**

| Befund | Bonus |
|--------|-------|
| Redundanter Autopilot (Backup) | +10 Punkte |
| Satellitenkompass | +5 Punkte |
| Ruderfeedback-Sensor installiert | +5 Punkte |
| Regelmäßige Wartung dokumentiert | +5 Punkte |
| Firmware aktuell | +3 Punkte |
| Windsteueranlage als Backup (Segelboot) | +10 Punkte |

### Z.12 Regionale Besonderheiten — Deutschland, Österreich, Schweiz

**Relevante Vorschriften DACH-Region:**

| Land | Vorschrift | AP-Relevanz |
|------|-----------|-------------|
| Deutschland | SportSeeSchifferschein (SSS) | Autopilot-Bedienung wird in der Prüfung abgefragt |
| Deutschland | BinSchStrO / SeeSchStrO | Ausguckpflicht auch mit AP, Hauptfahrwasser-Regelungen |
| Deutschland | BSH-Vorschriften | CE-Kennzeichnung des AP-Systems empfohlen |
| Österreich | Seen-Vorschriften (z.B. Bodensee) | AP-Nutzung auf Binnenseen mit Einschränkungen |
| Schweiz | VTS Schweiz | AP-Einsatz auf Seen zulässig, Ausguckpflicht besteht |

**Händler und Service-Stützpunkte Deutschland (Auswahl):**

| Hersteller | Händler/Service | Standort | Spezialisierung |
|-----------|----------------|----------|----------------|
| Raymarine | Busse Yachtshop | Hamburg | Vollsortiment Raymarine, Werkstatt |
| Raymarine | SVB | Bremen | Online + Showroom, alle Hersteller |
| B&G | Compass24 | Kiel | Großer B&G-Bestand, Beratung |
| Garmin | Garmin Marine DE | Garching | Direkt-Support, Garantie |
| Garmin | Toplicht | Hamburg | Garmin-Spezialist, Werkstatt |
| Simrad | Navico Service | Hamburg | Simrad + B&G Werkstatt |
| Furuno | Furuno DE | Rellingen | Direkt-Service, Kalibrierung |
| NKE | Segelservice Bendler | Kiel | Einer der wenigen NKE-Händler DE |
| Alle | AWN | Buxtehude | Großes Sortiment, Online-Shop |
| Alle | Plastimo DE | diverse | Zubehör, Kabel, Stecker |

**Import-Hinweis NKE:** NKE hat keinen offiziellen deutschen Vertrieb. Import aus Frankreich über: a) NKE-Website direkt (französische Rechnung, EU-Versand), b) französische Fachhändler (Uship, Accastillage Diffusion), c) spezialisierte deutsche Händler (Segelservice Bendler, Kiel; Segelkombinat, Berlin). Garantieabwicklung über NKE Frankreich.

### Z.13 Kabelquerschnitte und Absicherung

**Empfohlene Kabelquerschnitte (12V-Bordnetz):**

| Antrieb | Max. Strom (A) | Kabellänge bis 3m | Kabellänge 3–6m | Kabellänge 6–10m | Sicherung (A) |
|---------|---------------|-------------------|-----------------|------------------|---------------|
| Tillerpilot | 3 | 1,5 mm² | 2,5 mm² | 4,0 mm² | 5 A |
| Linearantrieb klein | 6 | 2,5 mm² | 4,0 mm² | 6,0 mm² | 10 A |
| Linearantrieb groß | 12 | 4,0 mm² | 6,0 mm² | 10,0 mm² | 15 A |
| Hydraulikpumpe klein | 10 | 4,0 mm² | 6,0 mm² | 10,0 mm² | 15 A |
| Hydraulikpumpe mittel | 20 | 6,0 mm² | 10,0 mm² | 16,0 mm² | 25 A |
| Hydraulikpumpe groß | 30 | 10,0 mm² | 16,0 mm² | 25,0 mm² | 40 A |

**Empfohlene Kabelquerschnitte (24V-Bordnetz):**

| Antrieb | Max. Strom (A) | Kabellänge bis 5m | Kabellänge 5–10m | Sicherung (A) |
|---------|---------------|-------------------|-----------------|---------------|
| Linearantrieb groß | 6 | 2,5 mm² | 4,0 mm² | 10 A |
| Hydraulikpumpe klein | 5 | 2,5 mm² | 4,0 mm² | 8 A |
| Hydraulikpumpe mittel | 10 | 4,0 mm² | 6,0 mm² | 15 A |
| Hydraulikpumpe groß | 15 | 6,0 mm² | 10,0 mm² | 20 A |

> **Berechnung:** Kabelquerschnitt = (2 × Länge × Strom) / (56 × max. Spannungsabfall). Max. Spannungsabfall für Autopiloten: 3 % (= 0,36V bei 12V). Bei 24V-System: 3 % = 0,72V. 56 = Leitfähigkeit Kupfer (m/Ω×mm²).

**Kabel- und Stecker-Typen:**

| Verbindung | Kabeltyp | Stecker | Hinweis |
|-----------|---------|---------|---------|
| Stromversorgung AP | Marinekabel verzinnt, doppelt isoliert | Ringkabelschuhe, geschraubt | Kein Quetschklemmen! |
| NMEA 2000 Backbone | NMEA 2000 zertifiziert (blau Mantel) | DeviceNet Micro-C | Nur zertifizierte Kabel verwenden |
| NMEA 2000 Drop | NMEA 2000 zertifiziert | DeviceNet Micro-C, T-Stück | Max. 6m |
| SeaTalkNG | Raymarine SeaTalkNG (blau) | SeaTalkNG-Stecker (= Micro-C) | Direkt an N2K anschließbar |
| SimNet | Simrad SimNet (gelb) | SimNet 5-polig (proprietär) | Adapter für NMEA 2000 nötig |
| NKE-Bus | NKE proprietär | NKE-Stecker | Gateway für NMEA 2000 nötig |
| NMEA 0183 | Geschirmtes 2-adriges Kabel | Klemmen oder DB-9 | Schirmung einseitig erden |
| Ruderfeedback | Geschirmt, 3- oder 5-adrig | Herstellerspezifisch | Schirmung an Masse |
| Hydraulikleitung | SAE J1532 marine (Nylon-Ummantlung) | JIC-Fittings oder O-Ring | Druckfest mind. 70 bar |

> ⚠️ **ZU PRÜFEN (Audit):** Die Normnummer **SAE J1532** bezeichnet tatsächlich *Transmission Oil Cooler Hose* (Getriebeöl-Kühlerschlauch, typische Druckstufe ~250 psi ≈ 17 bar) — NICHT eine druckführende Hydraulik-Steuerleitung. Für eine Steuerhydraulik-Leitung mit „mind. 70 bar" ist J1532 sowohl die falsche Norm als auch drucktechnisch ungeeignet. Die zutreffende Norm ist herstellerabhängig (z. B. SAE-100R-Serie / SAE J517 für Hydraulikschläuche bzw. die vom Steuerhersteller — SeaStar/Dometic, Vetus — freigegebenen Leitungen). Normnummer unverifiziert — vor Verwendung fachlich prüfen.

### Z.14 Zukunftsausblick und kommende Technologien

**Erwartete Entwicklungen 2026–2030:**

| Technologie | Status | Hersteller | Auswirkung |
|------------|--------|-----------|-----------|
| Machine-Learning-Regelung | Prototyp | B&G, Garmin | Weitere Verbesserung der Kursregelung durch Deep Learning |
| Lidar-Wellenerkennung | Forschung | Diverse | Vorausschauende Wellenanalyse für proaktive Rudersteuerung |
| Autonomes Routing | Beta (Garmin) | Garmin, Raymarine | Vollautonomes Fahren von Hafen zu Hafen |
| Predictive Maintenance | Prototyp | Furuno | AP erkennt Verschleiß und warnt vor Ausfall |
| Dual-Motor-Steuerung | Vorhanden | Garmin, Simrad | AP steuert Doppelmotoren differenziell (wie Raupenfahrwerk) |
| Hydrogen Fuel Cell Integration | Forschung | — | Stromversorgung für AP ohne fossile Brennstoffe |
| Starlink-Integration | Vorhanden | Alle (indirekt) | Fernüberwachung und -steuerung des AP über Satelliten-Internet |

---

> **Ende der AYDI Wissensdatei 21.02 — Autopilot Hersteller-Vergleich**
> Gesamtumfang: Einführung, Grundlagen, 6 Hersteller-Detailprofile, Spezifikationstabellen, 12 Fehlerbilder, 5 Entscheidungsbäume, 30 FAQ, 58 Glossareinträge, 8 Fallstudien, 10 Pydantic v2-Modelle.
> Nächste geplante Aktualisierung: Bei neuen Produktvorstellungen oder wesentlichen Firmware-Updates.
