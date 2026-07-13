---
title: "Autopilot-Systeme im Yachtbau"
kategorie: "14 Steueranlagen und Autopilot"
unterkategorie: "14.05 Autopilot-Systeme"
version: "1.0.0"
datum: "2026-04-26"
autor: "AYDI Research"
status: "validated"
confidence_quellen:
  - measured: "Hersteller-TDS, ISO 25197, IEC 62065, NMEA2000-Standard, CE-Zertifizierungen"
  - documented: "Hersteller-Kataloge, Installationshandbuecher, Werftunterlagen, Seatrials"
  - estimated: "Erfahrungswerte, Fahrtensegel-/Regatta-Praxis, Werft-Konsens, Nutzerberichte"
---

# 14.05 — Autopilot-Systeme im Yachtbau: Vollstaendige Wissensreferenz

> **AYDI Wissensdatei 14.05** — Kategorie 14: Steueranlagen und Autopilot
> **Confidence-Quelle:** measured (Hersteller-TDS, ISO-Normen), documented (Hersteller-Kataloge, Installationshandbuecher), estimated (Erfahrungswerte, Praxis)
> **Letzte Aktualisierung:** 2026-04-26

---

## Inhaltsverzeichnis

1. [Einfuehrung und Uebersicht](#1-einfuehrung-und-uebersicht)
2. [Grundlagen und Theorie](#2-grundlagen-und-theorie)
3. [Typenuebersicht](#3-typenuebersicht)
4. [Produktlinien und Hersteller](#4-produktlinien-und-hersteller)
5. [Dimensionierung und Auslegung](#5-dimensionierung-und-auslegung)
6. [NMEA2000/SeaTalk Integration](#6-nmea2000seatalk-integration)
7. [Fehlerbild-Atlas](#7-fehlerbild-atlas)
8. [Troubleshooting](#8-troubleshooting)
9. [FAQ — Haeufig gestellte Fragen](#9-faq--haeufig-gestellte-fragen)
10. [Glossar](#10-glossar)
11. [Schnell-Referenz](#11-schnell-referenz)
12. [ANHANG A–R](#12-anhang-ar)

---

## 1. Einfuehrung und Uebersicht

### 1.1 Definition und Funktion

Ein Autopilot ist ein elektronisch-mechanisches System, das ein Boot oder eine Yacht selbsttaetig auf einem vorgegebenen Kurs haelt, ohne dass ein Steuermann aktiv das Ruder bedienen muss. Der Autopilot ersetzt die menschliche Regelschleife (Kursabweichung erkennen, Ruder korrigieren, Ergebnis ueberwachen) durch einen geschlossenen elektronischen Regelkreis.

Die Kernfunktion eines Autopilots umfasst fuenf Elemente:

1. **Kurserfassung** — Ermittlung des aktuellen Steuerkurses ueber Kompasssensoren (Fluxgate, GPS, Ratenkreisel)
2. **Sollwert-Vorgabe** — Festlegung des gewuenschten Kurses durch den Bediener oder ein Navigationssystem
3. **Regelung** — Berechnung der erforderlichen Ruderbewegung durch den Kurscomputer (PID-Regler)
4. **Antrieb** — Umsetzung des Stellsignals in eine mechanische Ruderbewegung (Antriebseinheit)
5. **Rueckmeldung** — Messung der tatsaechlichen Ruderposition (Ruderfeedback-Sensor) und Rueckfuehrung in den Regelkreis

Im AYDI-Analysesystem zaehlen Autopiloten zu den Tier-2-Modulen (parallel mit Produktion, Material, Struktur) und beeinflussen direkt:

- **Ergonomie-Modul:** Einhandtauglichkeit, Wachbesetzung, Ermuedungsreduktion
- **Compliance-Modul:** ISO 25197 (elektrische/elektronische Anlagen), IEC 62065 (Track-Control)
- **Strukturmodul:** Rudermoment-Belastung, Antriebsbefestigung, Ruderlagerbeanspruchung
- **Kosten-Modul:** Autopiloten betragen typisch 5–15 % der Elektronikkosten, 2–6 % der Gesamtausruestung
- **Sicherheitsmodul:** MOB-Funktion, Ausfall-Szenarien, Redundanz bei langen Toerns

### 1.2 Bedeutung fuer die Yachtnavigation

Der Autopilot ist nach dem Motor und der Steueranlage das drittwichtigste funktionale System an Bord einer Fahrtenyacht. Seine Bedeutung hat in den letzten Jahrzehnten stetig zugenommen:

**Sicherheitsrelevanz:**
- Ermuedungsreduktion auf langen Wachen: ein erschoepfter Steuermann ist ein Sicherheitsrisiko
- Einhandsegler sind ohne Autopilot kaum in der Lage, sicher Segel zu setzen oder zu bergen
- MOB-Funktion (automatische Wende zum Mann-ueber-Bord-Punkt)
- Stabiler Kurs bei schwerem Wetter entlastet die Crew physisch und psychisch

**Komfortrelevanz:**
- Freihaendiges Segeln erhoecht den Fahrgenuss erheblich
- Ermoeglicht Navigation, Segeltrimm und Bordarbeiten waehrend der Fahrt
- Reduziert Crew-Anforderung fuer Langfahrt auf ein Minimum (Einhandtauglichkeit)

**Leistungsrelevanz:**
- Autopilot steuert in der Regel gerader als ein Mensch (weniger Schlangenlinien)
- Wind-Modus haelt konstanten Scheinwindwinkel, optimiert Segeltrimm
- Routenfuehrung ueber Wegpunkte ohne manuelles Eingreifen

### 1.3 Historische Entwicklung

**1920–1950 — Erste mechanische Autosteuer:**
- Elmer Sperry entwickelt den Schiffs-Gyroskop-Kompass und ersten mechanischen Autopilot
- "Iron Mike" fuer grosse Handelsschiffe, rein mechanisch mit pneumatischer Stellkraft
- Fuer Yachten nicht verfuegbar (zu gross, zu teuer)

**1950–1965 — Mechanische Windsteueranlagen fuer Yachten:**
- Blondie Hasler entwickelt fuer die erste OSTAR 1960 eine Windfahnen-Selbststeueranlage
- Hilfssegel-Typ und Pendelruder-Typ werden erprobt
- Keine Stromversorgung erforderlich — ideal fuer Langfahrt
- Aries, Atoms und Hasler Systeme dominieren die fruehe Langfahrtszene

**1965–1980 — Erste elektrische Yachtautopiloten:**
- Neco (UK) und Robertson (Norwegen) bringen erste kompakte elektrische Yachtautopiloten
- Fluxgate-Kompass als Richtungssensor wird Standard
- Einfache Ein/Aus-Regelung (Bang-Bang-Regler)
- Hoher Stromverbrauch, maessige Kursgenauigkeit
- Tillermaster (UK) als erste kompakte Pinnensteuerung

**1980–1995 — PID-Regelung und Mikroprozessoren:**
- Autohelm (spaeter Raymarine) revolutioniert mit dem ST 4000 den Markt
- Erste PID-Regelung in bezahlbaren Yachtautopiloten
- Autohelm 800 als erste einarmige Pinnenanlage wird Kultobjekt
- Robertson wird zu Simrad, spaeter zu Navico
- SeaTalk-Bus (Raymarine) als erstes proprietaeres Datennetzwerk
- B&G (Brookes & Gatehouse) fuer Racing-Segelyachten
- NKE (Frankreich) spezialisiert sich auf Regatta-Autopiloten

**1995–2010 — Digitalisierung und Netzwerkintegration:**
- NMEA 2000 als offener Standard etabliert sich
- Alle Hersteller integrieren GPS-Kopplung fuer Track-Modus (Wegpunktsteuerung)
- Raymarine SPX-Serie mit adaptiver Regelung
- Simrad AP Serie mit Precision-9-Kompass
- B&G Hydra/H3000 fuer Superyachten und Racing
- Garmin steigt mit Reactor-Serie in den Autopilot-Markt ein
- Stromverbrauch sinkt um ca. 40 % gegenueber frueheren Generationen
- Hydraulische Antriebseinheiten werden kompakter

**2010–heute — Adaptive Algorithmen und Solid-State-Sensoren:**
- Raymarine Evolution mit EV-Sensorkern (Solid-State, kalibrierungsfrei)
- Simrad Continuum mit 9-Achsen-Sensor
- B&G NAC-Kurscomputer mit H5000 fuer Regatta
- Garmin Reactor 40 mit Shadow-Drive-Technologie
- NKE Gyropilot 3 mit konkurrenzloser Regelguete im Racing
- MEMS-Sensoren (Micro-Electro-Mechanical-Systems) ersetzen mechanische Kreisel
- KI-gestuetzte adaptive Regelung in Premium-Systemen
- Drahtlose Fernbedienungen als Standard

### 1.4 Systemarchitektur — Uebersicht

```
                    +-----------------------+
                    |  Bedienelement         |
                    |  (Control Head /       |
                    |   Fernbedienung /      |
                    |   MFD / App)           |
                    +-----------+-----------+
                                |
                    Soll-Kurs / Modus
                                |
                    +-----------v-----------+
                    |  Kurscomputer          |
                    |  (Course Computer)     |
                    |  - PID-Regler          |
                    |  - Adaptive Algorithmen|
                    |  - NMEA2000-Interface  |
                    +-----------+-----------+
                         |           |
              +----------+           +----------+
              |                                 |
    +---------v--------+             +----------v---------+
    |  Sensoren         |             |  Antriebseinheit    |
    |  - Kompass         |             |  (Drive Unit)       |
    |  - Ratenkreisel    |             |  - Tiller Pilot     |
    |  - GPS-Heading     |             |  - Wheel Pilot      |
    |  - Neigungssensor  |             |  - Linear Drive     |
    |  - Windsensor      |             |  - Rotary Drive     |
    +-------------------+             |  - Hydraulic Drive   |
                                      +---------+----------+
                                                |
                                      +---------v----------+
                                      |  Ruderfeedback-     |
                                      |  Sensor              |
                                      |  (Ruderlagemeldung)  |
                                      +---------------------+
```

### 1.5 Abgrenzung zu mechanischen Windsteueranlagen

Elektrische Autopiloten und mechanische Windsteueranlagen (Windvane Self-Steering) loesen beide das Problem der automatischen Kurssteuerung, unterscheiden sich aber fundamental:

| Merkmal | Elektrischer Autopilot | Windsteueranlage |
|---------|----------------------|------------------|
| Energiequelle | 12V/24V Bordnetz | Windenergie (keine Elektrik) |
| Referenz | Kompass / GPS | Scheinbarer Wind |
| Kurshalten bei Winddrehung | Haelt Kompasskurs | Folgt der Winddrehung |
| Optimaler Einsatz | Motor, Raumer, leichter Wind | Amwindkurse, Passatwind |
| Stromverbrauch | 1–12 A je nach System | 0 A |
| Wartung | Elektronik, Mechanik, Dichtungen | Nur Mechanik |
| Kursgenauigkeit | +-2 Grad (gute Systeme) | +-5-10 Grad (windabhaengig) |
| Wegpunktsteuerung | Ja | Nein |
| Kosten (typisch) | EUR 1.500–15.000 | EUR 2.500–6.000 |
| Gewicht | 3–25 kg | 15–35 kg |
| Montage | Innenraum / Steuersaeule | Heckkorb / Spiegel |

In dieser Wissensdatei werden beide Systeme behandelt, da beide im AYDI-Kontext als "automatische Kurssteuerung" relevant sind und oft kombiniert eingesetzt werden (Windsteueranlage fuer Langfahrt, Autopilot fuer Manoevrieren und Motorfahrt).

---

## 2. Grundlagen und Theorie

### 2.1 Regelungstechnische Grundlagen

#### 2.1.1 Der geschlossene Regelkreis

Ein Autopilot arbeitet als geschlossener Regelkreis (Closed-Loop Control). Die Grundstruktur folgt dem klassischen Regelkreismodell:

```
                    Stoerung (Wind, Wellen, Stroemung)
                                |
                                v
  Sollkurs --->(+)---> Regler ---> Stellglied ---> Strecke ---> Istkurs
       ^         |      (PID)      (Rudermaschine)  (Yacht)        |
       |         |                                                  |
       |         +<------------ Rueckkopplung <--------------------+
       |                        (Kompass, Feedback)
       |
       +---- Vergleichsstelle (Soll - Ist = Regelabweichung)
```

**Strecke (Plant):** Die Yacht als dynamisches System mit Traegheit, Daempfung und stoerenden Einfluessen. Die Strecke ist hochgradig nichtlinear und zeitvariant (Seegang, Wind, Geschwindigkeit, Beladung aendern sich).

**Stellglied (Actuator):** Die Antriebseinheit, die das Ruder bewegt. Charakterisiert durch maximale Ruderkraft, Stellgeschwindigkeit und Totzone (Mindest-Ansteuerung).

**Sensor (Measurement):** Primaer der Kompass (Fluxgate, MEMS, GPS-Heading), ergaenzt durch Ratenkreisel (Drehgeschwindigkeitssensor) und Ruderfeedback-Sensor.

**Regler (Controller):** Der Kurscomputer, der aus der Regelabweichung (Soll minus Ist) das Stellsignal berechnet. Moderne Systeme verwenden PID-Regler mit adaptiven Anpassungen.

#### 2.1.2 PID-Regelung im Detail

Der PID-Regler (Proportional-Integral-Differential) ist der Kernalgorithmus jedes modernen Yachtautopiloten.

**Proportional-Anteil (P):**
```
u_P(t) = Kp * e(t)

wobei:
  Kp = Proportional-Verstaerkung (Gain)
  e(t) = Regelabweichung (Soll-Kurs minus Ist-Kurs) zum Zeitpunkt t
  u_P(t) = Proportionaler Stellanteil
```

- Hoher Kp: schnelle Reaktion, aber Schwingneigung (Hunting)
- Niedriger Kp: traege Reaktion, bleibende Regelabweichung bei konstanter Stoerung
- Im Yachtkontext: Kp bestimmt, wie stark das Ruder bei einer gegebenen Kursabweichung eingeschlagen wird

**Integral-Anteil (I):**
```
u_I(t) = Ki * integral(e(tau) d_tau, 0, t)

wobei:
  Ki = Integral-Verstaerkung
  integral = Summe aller vergangenen Regelabweichungen
```

- Eliminiert bleibende Regelabweichungen (Offset durch konstante Stoerung wie Stroemung oder Windversatz)
- Zu hoher Ki: Ueberschwingen, "Aufschaukeln", traege Reaktion nach Richtungsaenderung
- Im Yachtkontext: Ki kompensiert den Seitenversatz durch Wind oder Stroemung (Korrektur des "Lee-Drifts")

**Differential-Anteil (D):**
```
u_D(t) = Kd * de(t)/dt

wobei:
  Kd = Differentialverstaerkung
  de(t)/dt = Aenderungsgeschwindigkeit der Regelabweichung
```

- Reagiert auf die Geschwindigkeit der Kursaenderung, nicht auf den absoluten Fehler
- Daempft Schwingungen, bremst das Ruder rechtzeitig ab
- Zu hoher Kd: Nervoeser Autopilot, haeufige kleine Ruderbewegungen, hoher Stromverbrauch
- Im Yachtkontext: Kd ist der wichtigste Parameter fuer die "Ruhe" der Steuerung bei Seegang

**Gesamt-Stellsignal:**
```
u(t) = Kp * e(t) + Ki * integral(e(tau) d_tau) + Kd * de(t)/dt

In diskreter Form (wie im Kurscomputer implementiert):
u[n] = Kp * e[n] + Ki * sum(e[k] * dt, k=0..n) + Kd * (e[n] - e[n-1]) / dt
```

#### 2.1.3 Erweiterte Regelungsalgorithmen

Moderne Yachtautopiloten gehen ueber den einfachen PID-Regler hinaus:

**Adaptive Regelung (Self-Learning):**
- Der Autopilot aendert Kp, Ki, Kd automatisch basierend auf:
  - Bootgeschwindigkeit (hoehere Geschwindigkeit = mehr Rudereffekt = weniger Gain noetig)
  - Seegang (hoher Seegang = hoehere Daempfung, niedrigerer P-Anteil)
  - Windstaerke (mehr Wind = mehr Stoerung = mehr D-Anteil)
- Raymarine Evolution: "Autolearn" erkennt Bootstyp und Dynamik in der Einlernphase
- Simrad Continuum: Seegangs-Erkennung passt Ruderbewegungen automatisch an

**Vorsteuerung (Feed-Forward):**
```
u(t) = PID_output(t) + K_ff * stoerung_geschaetzt(t)
```
- Nutzt Windsensor-Daten oder Ratenkreisel-Signal als Vorsteuerung
- Reagiert auf eine Boe, bevor die Kursabweichung eintritt
- Besonders wichtig bei Segelyachten mit hoher Gierdynamik bei Boen

**Totzone (Deadband):**
- Kleine Kursabweichungen (z.B. unter 1-3 Grad) werden ignoriert
- Reduziert Ruderaktivitaet und Stromverbrauch
- Breite der Totzone seegangsabhaengig: bei ruhigem Wasser eng, bei Seegang weit
- Einstellbar als "Kursbreite" oder "Response Level" an vielen Autopiloten

**Ruderlimitierung:**
- Maximaler Ruderausschlag wird begrenzt (typisch 15-30 Grad)
- Verhindert extreme Ruderbewegungen, die das Boot bremsen
- Bei Seegang oft enger begrenzt als bei ruhigem Wasser
- Schuetzt die Antriebseinheit vor Ueberlastung

#### 2.1.4 Betriebsmodi

Jeder moderne Autopilot bietet mehrere Betriebsmodi:

**Standby-Modus:**
- Autopilot ist eingeschaltet, aber nicht aktiv
- Sensordaten werden erfasst und angezeigt
- Kompassanzeige aktiv, Kurscomputer bereit
- Minimaler Stromverbrauch (typisch 0,1–0,5 A)

**Heading-Hold (Kompasskurs halten):**
- Grundmodus: Yacht wird auf einen festen Kompasskurs gehalten
- Soll-Kurs wird beim Einschalten oder manuell uebernommen
- Kursaenderung ueber +1/+10/-1/-10-Grad-Tasten oder Drehknopf
- Kompensiert Wind und Stroemung automatisch (I-Anteil)
- Genauigkeit: +-1 bis +-3 Grad (je nach System und Seegang)

**Wind-Modus (Apparent Wind Steering):**
- Haelt konstanten Scheinwindwinkel statt Kompasskurs
- Erfordert angeschlossenen Windsensor (Mastspitze oder Bugsprit)
- Yacht dreht mit Winddrehungen mit — ideal fuer Amwind-Segeln
- Keine Kompensation von Stroemungsversatz (kein fester Kompasskurs)
- Genauigkeit: +-2 bis +-5 Grad Windwinkel

**Track-Modus (Navigation / GPS-Steering):**
- Yacht folgt einer GPS-Route (Kette von Wegpunkten)
- Kurscomputer erhaelt Bahn-Sollwert vom Kartenplotter via NMEA2000
- Cross-Track-Error (XTE) wird als zusaetzlicher Regelgroesse einbezogen
- Automatische Kurswechsel an Wegpunkten (mit Sicherheitsbestaetigung)
- Kompensiert Stroemungsversatz und Abdrift automatisch
- IEC 62065: Vorschrift fuer Track-Control-Systeme (Warnung bei Kursaenderung >30 Grad)

**NoDrift-Modus (bei einigen Herstellern):**
- Kombination aus Heading-Hold und GPS-Track
- Haelt Kompasskurs, korrigiert aber GPS-Abdrift
- Nuetzlich bei starker Querstroemung ohne definierte Route

**Power-Steer / Manual Override:**
- Bediener steuert manuell ueber Autopilot-Tasten (Port/Starboard)
- Antriebseinheit folgt den Tasten-Befehlen proportional
- Nuetzlich fuer Manoevrieren im Hafen oder Annaeherung an MOB

### 2.2 Kompasssysteme

#### 2.2.1 Fluxgate-Kompass

Der Fluxgate-Kompass war jahrzehntelang der Standardsensor fuer Yachtautopiloten und ist in vielen Systemen weiterhin im Einsatz.

**Funktionsprinzip:**
- Zwei Spulen auf hochpermeablen Ferritkernen im Push-Pull-Modus
- Erregerspule treibt die Kerne periodisch in Saettigung
- Erdmagnetfeld erzeugt eine asymmetrische Saettigung → messbare Oberwelle
- Phasen- und Amplitudenauswertung ergibt die Richtung des Erdmagnetfelds
- Aufloesung: typisch 0,1 Grad
- Genauigkeit: +-1 Grad nach Kalibrierung (ohne Stoerfelder)

**Montagehinweise:**
- Horizontale Montage (Kompassebene parallel zur Wasserlinie)
- Mindestabstand zu Stoerquellen:
  - Lautsprecher: 0,5 m
  - Elektromotoren: 1,0 m
  - Eisenteile (Kielbolzen, Motorblock): 1,5 m
  - Starkstromkabel: 0,3 m
- Kalibrierung durch langsames Drehen des Bootes um 360 Grad (mindestens 2 Umdrehungen)
- Deviation (Restfehler nach Kalibrierung): sollte <3 Grad sein

**Vorteile:**
- Bewaehrte Technologie, seit 40+ Jahren im Einsatz
- Keine beweglichen Teile, langlebig
- Unabhaengig von GPS-Signal

**Nachteile:**
- Empfindlich gegen Magnetfeldstoerugen (Lautsprecher, Motoren, Eisen)
- Deviation durch Bordmagnetismus erfordert Kompensation
- Beschleunigungsfehler bei Schraglage (Heel-Fehler bei Segelyachten)
- Kalibrierung bei Systemwechsel oder Aenderungen im Schiffsmagnetismus erforderlich

#### 2.2.2 GPS-Kompass (Zweifrequenz / Dual-Antenna)

GPS-Kompasssysteme nutzen zwei oder mehr GPS-Antennen in definiertem Abstand, um die Orientierung des Schiffes zu bestimmen.

**Funktionsprinzip:**
- Zwei GPS-Antennen im Abstand von typisch 0,5–2,0 m
- Phasendifferenz der GPS-Signale ergibt den Richtungswinkel
- Kein Einfluss durch Magnetfelder
- Genauigkeit: +-0,5 Grad (bei 1 m Antennenabstand)

**Relevante Produkte:**
- Simrad HS80A (Dual-Antenna, NMEA2000)
- Furuno SC-50/SC-70 (Satellitenkompass)
- Garmin GPS 24xd (Single-Antenna, nur COG, kein Heading)

**Vorteile:**
- Keine Deviation, kein Magnetfeldproblem
- Keine Kalibrierung erforderlich
- Hohe Genauigkeit unabhaengig von Stoerfeldern
- Liefert True Heading (rechtweisend), nicht Magnetic Heading

**Nachteile:**
- Erfordert freie Sicht zu GPS-Satelliten (Abschattung durch Mast, Segel)
- Latenz: ca. 0,1–0,2 Sekunden (zu langsam fuer alleinige Regelung)
- Bei niedrigen Geschwindigkeiten oder im Stand: COG ungenau, True Heading aber korrekt (Dual-Antenna)
- Teurer als Fluxgate (EUR 1.000–4.000 fuer Dual-Antenna)

#### 2.2.3 MEMS-Sensoren und Solid-State-Systeme

Moderne Autopiloten verwenden zunehmend MEMS-basierte Multisensor-Module, die mehrere Sensorprinzipien kombinieren.

**Funktionsprinzip:**
- MEMS-Magnetometer (3-Achsen): misst Erdmagnetfeld wie Fluxgate, aber auf Halbleiterbasis
- MEMS-Beschleunigungssensor (3-Achsen): misst Neigung und Beschleunigung
- MEMS-Gyroskop (3-Achsen): misst Drehraten um alle Achsen
- Sensor-Fusion: Kalman-Filter kombiniert alle 9 Messwerte zu einer robusten Lagebestimmung (AHRS — Attitude and Heading Reference System)

**Relevante Produkte:**
- Raymarine EV-1 (Evolution-Sensorkern, 9-Achsen-AHRS)
- Simrad Precision-9 (9-Achsen-AHRS, NMEA2000)
- B&G Precision-9 (identisch zu Simrad)
- Garmin MSC 10 (Heading-Sensor, MEMS)

**Vorteile:**
- Sehr kompakt und leicht (EV-1: ca. 100 g)
- Schnelle Datenrate (bis 40 Hz) fuer ueberlegene Regelguete
- 3-Achsen-Kompensation: Heel-Fehler wird automatisch korrigiert
- Ratenkreisel-Funktion integriert: erkennt Gierbewegung vor Kursaenderung
- Oft kalibrierungsfrei (Raymarine Evolution: "AI calibration")

**Nachteile:**
- MEMS-Magnetometer hat aehnliche Stoerfeldempfindlichkeit wie Fluxgate
- Drift des MEMS-Gyroskops (Bias-Drift): erfordert staendige Korrektur durch Magnetometer/GPS
- Guenstige MEMS-Sensoren weniger genau als hochwertige Fluxgate-Kompasse
- Langzeitstabilitaet geringer als mechanische Kreisel

#### 2.2.4 Ratenkreisel (Rate Gyro)

Der Ratenkreisel misst die Drehgeschwindigkeit (Gierrate) der Yacht um die Hochachse.

**Funktionsprinzip:**
- Mechanisch: rotierender Kreisel mit Praezessionsmessung (kaum noch im Einsatz)
- MEMS: Coriolis-Effekt auf eine schwingende Masse (Standard in modernen Systemen)
- Faseroptisch (FOG): Sagnac-Effekt in Glasfaserspule (Superyachten, Marineschiffe)
- Ausgang: Grad pro Sekunde (deg/s), typisch +-100 deg/s Messbereich

**Bedeutung fuer Autopiloten:**
- Der Ratenkreisel ist der entscheidende Sensor fuer die Regelqualitaet
- Er erkennt eine Kursaenderung, bevor der Kompass sie als Kursabweichung meldet
- Ergibt den D-Anteil (Differentialanteil) des PID-Reglers direkt
- Ohne Ratenkreisel: Autopilot reagiert erst auf Kursabweichung (zu spaet)
- Mit Ratenkreisel: Autopilot reagiert auf Gierbeschleunigung (praediktiv)

**Montagehinweise:**
- Muss in der Bootsmitte montiert sein (minimale Hebelarme bei Rollbewegung)
- Orientierung: Mess-Achse senkrecht zum Deck (Gieren um Hochachse)
- Vibrationsdaempfung bei Motorbooten empfohlen

### 2.3 Ruderfeedback-Sensor

Der Ruderfeedback-Sensor meldet die aktuelle Ruderposition an den Kurscomputer zurueck. Er ist ein essenzielles Element des Regelkreises.

#### 2.3.1 Typen

**Potentiometer (Widerstandsgeber):**
- Drehpotentiometer am Ruderschaft oder Quadranten
- Analoges Signal (0–5V oder widerstandsproportional)
- Einfach, guenstig, aber verschleissanfaellig
- Lebensdauer: ca. 5–10 Jahre bei normaler Nutzung
- Typisch fuer Seriensysteme bis 14 m

**Hallsensor (kontaktlos):**
- Magnetischer Halleffekt-Sensor mit rotierendem Magneten
- Kontaktlos, verschleissfrei
- Genauigkeit: +-0,5 Grad
- Typisch fuer hochwertige Systeme und Nachruestung

**Linearer Wegsensor:**
- An linearen Antriebseinheiten integriert
- Misst den Hub des Linearantriebs
- Wird in Ruderwinkel umgerechnet (Hebelgesetz)

**NMEA2000-Rudersensor:**
- Digitaler Sensor mit eigenem NMEA2000-Anschluss
- PGN 127245 (Rudder Position)
- Keine Kalibrierung am Kurscomputer noetig
- Magellan RSA (Rudder Sensor Assembly) und Octopus RSAT als Beispiele

#### 2.3.2 Montage und Kalibrierung

- Sensor muss den vollen Ruderausschlag abdecken (typisch +-35 Grad)
- Mechanische Verbindung spielfrei und ohne Totgang
- Kalibrierung: Ruder Mittschiffs → Nullpunkt setzen, dann BB/StB Vollanschlag
- Regelmassige Pruefung: Ruderfeedback-Anzeige mit tatsaechlicher Ruderlage vergleichen
- Fehlerhafte Kalibrierung fuehrt zu asymmetrischer Steuerung (mehr Ausschlag nach einer Seite)

### 2.4 Antriebsprinzipien

#### 2.4.1 Elektromechanische Antriebe

**Prinzip:**
- Gleichstrommotor (12V oder 24V) treibt ueber Getriebe eine mechanische Verbindung zum Ruder
- Getriebe: Schnecke, Stirnrad, Planetengetriebe
- Selbsthemmung: Schneckengetriebe sperren im stromlosen Zustand (das Ruder bleibt stehen)
- Nicht-selbsthemmend: Stirnrad/Planeten erlauben manuelles Steuern ohne Kupplung

**Varianten:**
- Tiller-Pilot: Linearantrieb greift direkt an der Pinne an
- Wheel-Pilot: Reibrad oder Riemen treibt das Steuerrad an
- Below-Deck Linear: Linearantrieb am Ruderquadranten oder Tillerarm unter Deck
- Below-Deck Rotary: Drehantrieb direkt auf dem Ruderschaft

#### 2.4.2 Hydraulische Antriebe

**Prinzip:**
- Elektrische Pumpe (Zahnrad- oder Kolbenpumpe) erzeugt Hydraulikdruck
- Hydraulikzylinder (Linear) oder Hydraulikmotor (Rotary) bewegt das Ruder
- Magnetventile oder Proportionalventile steuern Richtung und Geschwindigkeit
- Hydraulikfluid: meist Dexron ATF oder spezielles Marine-Hydraulikoel

**Varianten:**
- Linear-Zylinder: fuer Seil-/Ketten-Steuerungen, greift am Quadranten an
- Rotary-Vane-Aktuator: kompakter Drehantrieb direkt am Ruderschaft
- Reversible Pumpe: Druckumkehr ohne Magnetventile (leiser, weniger Verschleiss)

**Vorteile Hydraulik:**
- Hohe Kraefte/Momente moeglich (ab ca. 45 Fuss / 14 m erforderlich)
- Kein Getriebe-Verschleiss im Antrieb
- Manuelle Steuerung moeglich bei stromlosen Ventilen (keine Kupplung noetig bei offenen Bypass-Ventilen)
- Geraeuscharmer Betrieb (Pumpe kann schallgedaemmt montiert werden)

**Nachteile Hydraulik:**
- Leckagegefahr (Dichtungen, Schlauchverbindungen)
- Wartungsaufwaendiger (Fluessigkeitsstand, Filter, Entlueftung)
- Temperaturempfindlich (Viskositaetsschwankung bei Kaelte)
- Hoehere Installationskosten

### 2.5 Energieverbrauch und -management

Der Stromverbrauch des Autopiloten ist auf Segelyachten eine kritische Groesse, da er oft den groessten Einzelverbraucher an Bord darstellt.

**Typische Verbrauchswerte (12V-Systeme):**

| Bootsklasse | Antriebstyp | Durchschnitt | Spitze | 24h-Verbrauch |
|-------------|-------------|-------------|--------|---------------|
| 7–9 m Segel | Tiller-Pilot | 0,5–1,5 A | 4 A | 15–30 Ah |
| 9–12 m Segel | Linear u.D. | 1,0–3,0 A | 8 A | 30–60 Ah |
| 12–16 m Segel | Linear/Hydraulik | 2,0–5,0 A | 15 A | 50–100 Ah |
| 16–20 m Segel | Hydraulik | 3,0–8,0 A | 25 A | 80–160 Ah |
| 20+ m Segel | Hydraulik | 5,0–15 A | 40 A | 120–300 Ah |
| 8–12 m Motor | Linear u.D. | 1,5–3,0 A | 10 A | 30–60 Ah |
| 12–18 m Motor | Hydraulik | 2,5–6,0 A | 20 A | 50–120 Ah |

**Einflussfaktoren auf den Verbrauch:**
- Seegang: rauer Seegang verdoppelt bis verdreifacht den Verbrauch
- Segeltrimm: schlecht getrimmtes Boot mit Lee-/Luvgierigkeit erhoecht Verbrauch drastisch
- Bootgeschwindigkeit: hoehere Geschwindigkeit = hoehere Ruderkraefte
- Regelguete: ueberkompensierender Autopilot (Hunting) verschwendet Strom
- Deadband-Einstellung: engere Kursbreite = mehr Ruderbewegungen = mehr Verbrauch
- Ruderanlagen-Zustand: schwergaengige Ruderlager erhoehen den Verbrauch

**Energieoptimierung:**
- Segeltrimm optimieren: neutrale Helmbalance reduziert Autopilot-Arbeit um 30–50 %
- Deadband bei Seegang vergroessern
- Response-Level auf niedrigster akzeptabler Stufe fahren
- Solarpanel/Windgenerator dimensionieren: Mindestens Autopilot-Durchschnittsverbrauch abdecken
- 24V-System halbiert den Strom bei gleicher Leistung (duennere Kabel, weniger Verluste)

---

## 3. Typenuebersicht

### 3.1 Tiller-Pilot (Pinnenautopilot)

#### 3.1.1 Bauform und Funktionsprinzip

Der Tiller-Pilot ist ein kompakter, eigenstaendiger Autopilot, der als Linearantrieb direkt an der Pinne (Ruderpinne) angreift. Kurscomputer, Sensoren und Antrieb sind in einem einzigen Gehaeuese integriert.

**Aufbau:**
```
  +--[Bedientasten/Display]--+
  |  Kurscomputer + Kompass  |
  |  Motorcontroller         |
  |  12V DC Anschluss        |
  +---[Linearmotor]----------+====[Stange]===[Pinnenanschluss]
```

**Typische Spezifikationen:**
- Hub: 150–300 mm
- Kraft: 30–60 kg (300–600 N)
- Stellgeschwindigkeit: 10–20 mm/s
- Eigengewicht: 2–4 kg
- Stromverbrauch: 0,5–4 A (12V)
- Max. Bootlaenge: 7–10 m (herstellerabhaengig)
- Max. Verdraengung: 3.000–6.000 kg

**Montagepunkte:**
- Pinne: ueber Universalgelenk oder Pin-Adapter
- Cockpitwand: Montagebuegel oder Saugnapf (nur fuer leichte Modelle)
- Einige Modelle: Wandhalterung mit Schnellentriegelung

#### 3.1.2 Vor- und Nachteile

**Vorteile:**
- Einfachste Installation (Plug & Play, oft unter 30 Minuten)
- Guenstigster Autopilot-Typ (EUR 500–1.800)
- Keine Unterdeck-Arbeiten, kein Ruderfeedback-Sensor noetig
- Leicht zu demontieren (Diebstahlschutz, Winterlager)
- Kein Eingriff in die bestehende Steueranlage
- Manuelles Steuern durch Ausklinken sofort moeglich

**Nachteile:**
- Begrenzte Kraft (nur fuer kleine Boote bis ca. 10 m / 5 t)
- Langsame Stellgeschwindigkeit im Vergleich zu Unterdeck-Systemen
- Im Cockpit montiert: Stolpergefahr, Platzverbrauch, UV-Exposition
- Mechanische Verbindung zur Pinne kann klappern
- Kein Ruderfeedback: Regelguete schlechter als bei Unterdeck-Systemen
- Begrenzte Lebensdauer der Linearspindel (Verschleiss)

#### 3.1.3 Konkrete Tiller-Pilot Modelle

| Hersteller | Modell | Kraft | Hub | Max. Boot | ca. Preis |
|------------|--------|-------|-----|-----------|-----------|
| Raymarine | EV-100 Tiller (Type 1) | 50 kg (490 N) | 230 mm | 10 m / 5 t | EUR 1.800 (Paket) |
| Simrad | Tiller Pilot TP10 | 45 kg (440 N) | 200 mm | 9 m / 4 t | EUR 900 |
| Simrad | Tiller Pilot TP32 | 60 kg (590 N) | 250 mm | 11 m / 6 t | EUR 1.400 |
| Garmin | Reactor 40 Tiller Kit | 50 kg (490 N) | 230 mm | 10 m / 5 t | EUR 1.600 |
| Nasa Marine | Clipper Tiller Pilot | 30 kg (290 N) | 150 mm | 7 m / 2,5 t | EUR 500 |

**Montagehinweise Tiller-Pilot:**
- Pinnenadapter muss zum Pinnenquerschnitt passen (rund, oval, flach)
- Mindestens 2 Montagepunkte fuer den Antrieb (Cockpitwand/Bodenbeschlag)
- Kabel so verlegen, dass Cockpitablauf nicht blockiert wird
- UV-Schutz: Bei Nichtbenutzung abdecken oder abnehmen (UV schaedigt Gehaeuse)
- Wasserdichtigkeit: IPX6 Standard, aber Langzeit-UV schwaeacht Dichtungen
- Sicherungsleine: Tiller-Pilot mit Leine sichern (gegen Verlust bei Kenterung)
- Pinnenausschlag pruefen: Tiller-Pilot darf den vollen Pinnenausschlag nicht begrenzen

**Typische Fehlerquellen bei Tiller-Piloten:**
- Universalgelenk am Pinnenanschluss: wird locker, erzeugt Klappern und Regelungenauigkeit
- Stange verbiegt sich bei Ueberbelastung (schwerer Seegang, zu grosses Boot)
- Gehaeuse-Riss durch UV und Schlagbelastung nach 5–8 Jahren Ausseneinsatz
- Interner Kompass wird durch nahes Metallgelaender oder Edelstahl-Pinne gestoert
- Stromversorgung ueber Cockpit-Steckdose: Kontaktprobleme durch Korrosion und Feuchtigkeit

#### 3.1.4 Geeignete Boote

- Segelyachten 6–10 m mit Pinnensteuerung
- Verdraengung bis ca. 5.000 kg (leichte Modelle: 3.000 kg)
- Tagessegler, Kuestenfahrt, gelegentliche Ueberfahrten
- Nicht geeignet fuer: Hochseeyachten, schweres Wetter, Verdraengung >5 t
- Ideal als Zweit-/Backup-System fuer groessere Boote mit Pinnenoption

### 3.2 Wheel-Pilot (Radautopilot)

#### 3.2.1 Bauform und Funktionsprinzip

Der Wheel-Pilot greift am Steuerrad an und treibt es ueber einen Reibrad-Mechanismus oder Riementrieb an. Er ist die einfachste Autopilot-Loesung fuer Boote mit Radsteuerung.

**Aufbau:**
```
  Steuerrad
     |
     v
  +--[Reibrad/Antriebsrolle]--+
  |  Motor + Getriebe          |
  |  Kurscomputer + Kompass    |
  |  Bedientasten/Display      |
  +---[Montagearm]---[Steuersaeule/Pedestal]
```

**Typische Spezifikationen:**
- Drehmoment: 5–20 Nm am Steuerrad
- Stellgeschwindigkeit: 15–40 Grad/s Steuerrad-Drehung
- Max. Steuerrad-Durchmesser: 600–1.000 mm
- Eigengewicht: 3–6 kg
- Stromverbrauch: 1–5 A (12V)
- Max. Bootlaenge: 8–14 m
- Max. Verdraengung: 3.000–10.000 kg

#### 3.2.2 Vor- und Nachteile

**Vorteile:**
- Installation am Steuerrad ohne Unterdeck-Arbeiten (30–60 Minuten)
- Manuelle Steuerung jederzeit moeglich (Rad dreht mit)
- Sichtbare Ruderbewegung: Steuermann sieht, was der Autopilot macht
- Guenstiger als Unterdeck-Systeme (EUR 1.200–3.500)
- Kein Eingriff in Steueranlage oder Ruderschaft

**Nachteile:**
- Reibrad kann bei Naesse rutschen (Schlupf)
- Traege Reaktion durch Lose im Steuerungssystem (Spiel in Kette/Seil)
- Hoehere Geraeuschentwicklung als Unterdeck-Systeme
- Platzbedarf am Steuerstand
- Nur fuer Einzel-Steuerraeder (Doppelrad erfordert Adapter)
- Bei Doppelruder-Anlagen: nur ein Rad angetrieben

#### 3.2.3 Konkrete Wheel-Pilot Modelle

| Hersteller | Modell | Drehmoment | Max. Rad | Max. Boot | ca. Preis |
|------------|--------|-----------|----------|-----------|-----------|
| Raymarine | EV-100 Wheel (Type 1) | 15 Nm | 914 mm (36") | 12 m / 8 t | EUR 2.200 (Paket) |
| Simrad | WP20 Wheel Pilot | 12 Nm | 800 mm (32") | 10 m / 6 t | EUR 1.500 |
| Simrad | WP30 Wheel Pilot | 20 Nm | 1.000 mm (40") | 14 m / 10 t | EUR 2.200 |
| Garmin | Reactor 40 Wheel Kit | 15 Nm | 914 mm (36") | 12 m / 8 t | EUR 2.500 |

**Montagehinweise Wheel-Pilot:**
- Reibrad muss mit gleichmaessigem Druck auf dem Steuerrad aufliegen
- Steuerrad-Oberflaeche muss sauber und trocken sein (kein Oel, kein Wachs)
- Bei Teak-Steuerrad: Reibrad auf lackierte oder blanke Stelle setzen (nicht auf Teak-Kante)
- Montagearm: stabil befestigt an Pedestal oder Steuersaeule, kein Wackeln
- Kabelverlegung: spritzwassergeschuetzt, mit Zugentlastung
- Bei Doppelrad: nur ein Rad angetrieben, das andere dreht passiv mit

**Typische Fehlerquellen bei Wheel-Piloten:**
- Reibrad-Verschleiss: Gummierung verschleisst nach 2–4 Jahren, Ersatz noetig
- Schlupf bei Naesse: Reibrad rutscht bei Regen oder Spritzwasser
- Montagearm loest sich: Vibrationen lockern die Befestigung
- Spiel in Steueranlage: Kette/Seil-Lose wird vom Wheel-Pilot nicht kompensiert
- Geraeusch: Motor-Getriebe-Geraeusch kann bei Nachtfahrt stoerend sein

#### 3.2.4 Geeignete Boote

- Segelyachten 8–14 m mit Radsteuerung
- Motorboote 7–12 m mit mechanischer Steuerung
- Verdraengung bis ca. 8.000 kg
- Charter- und Fahrtenyachten, Kuestenfahrt, moderate Offshore-Toerns
- Als Uebergangsloesung vor einem spaeteren Unterdeck-System

### 3.3 Below-Deck Linear Drive (Linearantrieb unter Deck)

#### 3.3.1 Bauform und Funktionsprinzip

Der Linearantrieb ist ein elektromechanischer Zylinder, der unter Deck am Ruderquadranten, Tillerarm oder einer Anlenkung am Ruderschaft angreift. Er ist die haeufigste Autopilot-Antriebsform fuer Segelyachten von 9–18 m.

**Aufbau:**
```
  Ruderschaft (von oben betrachtet)
       |
       v
  +----+----+  Quadrant / Tillerarm
  |         |
  |    +----+--[Gelenkpunkt]--[Linearantrieb]--[fester Montagepunkt]
  |         |
  +----+----+
```

Der Linearantrieb wandelt die Drehbewegung eines Elektromotors ueber ein Getriebe (Schnecke, Kugelgewindespindel oder Trapezgewindespindel) in eine lineare Hubbewegung um. Die Endpunkte des Antriebs sind ueber Kugelgelenke mit dem Quadranten/Tillerarm und dem Befestigungspunkt am Rumpf verbunden.

**Typische Spezifikationen:**

| Klasse | Hub | Kraft | Geschwindigkeit | Geeignet fuer |
|--------|-----|-------|-----------------|---------------|
| Light | 150–230 mm | 50–80 kg | 12–18 mm/s | 8–12 m, bis 6 t |
| Medium | 200–305 mm | 80–150 kg | 15–22 mm/s | 11–16 m, bis 15 t |
| Heavy | 250–380 mm | 150–250 kg | 18–28 mm/s | 14–20 m, bis 25 t |

#### 3.3.2 Vor- und Nachteile

**Vorteile:**
- Geschuetzt unter Deck (kein UV, kein Salzwasser direkt)
- Kraftvoller als Tiller-/Wheel-Pilot
- Kein Platzbedarf im Cockpit
- Mit Ruderfeedback-Sensor: ueberlegene Regelguete
- Selbsthemmend (Schneckengetriebe): Ruder bleibt bei Stromausfall in Position
- Wartungsarm (alle 2–5 Jahre Schmierung)

**Nachteile:**
- Aufwaendigere Installation (Unterdeck-Montage, Befestigungspunkte, Kabelverlegung)
- Ruderfeedback-Sensor erforderlich (zusaetzliche Installation)
- Kurscomputer und Bedieneinheit separat (mehr Komponenten)
- Bei Stromausfall: Ruder blockiert (Kupplung oder Bypass erforderlich)
- Geraeusche unter Deck hoeher als ueber Deck
- Kosten: EUR 2.500–8.000 (Antrieb + Computer + Sensoren + Bedieneinheit)

#### 3.3.3 Kupplungssysteme

Da selbsthemmende Linearantriebe das Ruder bei Stromausfall blockieren, sind Kupplungssysteme unverzichtbar:

**Elektromagnetische Kupplung:**
- Im Antrieb integriert
- Loest bei Autopilot-Abschaltung automatisch aus
- Manuelles Steuern sofort moeglich
- Standard bei Raymarine Type 1/2/3, Simrad SD-Serie

**Mechanische Schnellentriegelung:**
- Hebel oder Knopf am Antrieb
- Manuelles Auskuppeln in Notsituation
- Redundant zur elektromagnetischen Kupplung

**Bypass-Ventil (bei Hydraulik-Steuerung):**
- Nicht am Autopilot-Antrieb, sondern an der Hydrauliksteuerung
- Oeffnen des Bypass-Ventils entkoppelt den Autopilot-Zylinder

### 3.4 Below-Deck Rotary Drive (Drehantrieb unter Deck)

#### 3.4.1 Bauform und Funktionsprinzip

Der Drehantrieb sitzt direkt auf dem Ruderschaft und dreht ihn ueber ein Untersetzungsgetriebe. Er ist die kompakteste Unterdeck-Loesung und wird bevorzugt eingesetzt, wenn am Ruderschaft ein Montageflansch vorhanden ist.

**Aufbau:**
```
  Ruderschaft
       |
       v
  +----+----+
  | Drehantrieb |
  | Motor +     |
  | Getriebe    |
  +----+----+
       |
  Befestigung am Ruderschaft-Flansch
```

**Typische Spezifikationen:**
- Drehmoment: 10–80 Nm
- Stellgeschwindigkeit: 3–8 Grad/s Ruderausschlag
- Ruderwinkel: typisch +-35 Grad
- Eigengewicht: 3–10 kg
- Stromverbrauch: 1,5–8 A (12V)
- Max. Ruderschaftdurchmesser: 40–75 mm

#### 3.4.2 Vor- und Nachteile

**Vorteile:**
- Direktantrieb: kein Spiel, keine Hebelarme, keine Lose
- Sehr kompakt (kein langer Linearzylinder)
- Integrierter Ruderfeedback (Drehwinkel = Ruderwinkel)
- Ideal bei beengten Platzverhaeltnissen im Achterbereich
- Gleichmaessiges Drehmoment ueber den gesamten Ruderausschlag

**Nachteile:**
- Erfordert kompatiblen Ruderschaft-Flansch
- Montage komplexer (Ausrichtung auf Ruderschaft)
- Schwieriger nachzuruesten als Linearantrieb
- Begrenzte Auswahl am Markt
- Bei Stromausfall: Blockade des Ruders (Kupplung erforderlich)

### 3.5 Hydraulic Drive (Hydraulischer Autopilotantrieb)

#### 3.5.1 Bauform und Funktionsprinzip

Hydraulische Autopilot-Antriebe nutzen eine Elektro-Hydraulik-Pumpe, die ueber Hydraulikleitungen einen Zylinder oder Motor am Ruder ansteuert. Sie sind Standard fuer Yachten ab ca. 14 m (45 Fuss) und fuer alle Boote mit hydraulischer Steueranlage.

**Aufbau (Linear-Hydraulik):**
```
  Kurscomputer
       |
       v
  Pumpeneinheit (Reversible Pump)
       |
  Hydraulikleitungen (Hochdruck)
       |
       v
  Hydraulikzylinder --- Quadrant/Tillerarm --- Ruderschaft
```

**Aufbau (Rotary-Hydraulik):**
```
  Kurscomputer
       |
       v
  Pumpeneinheit
       |
  Hydraulikleitungen
       |
       v
  Rotary-Vane-Aktuator --- direkt am Ruderschaft
```

**Typische Spezifikationen:**

| Klasse | Zylinder | Druck | Pumpenleistung | Geeignet fuer |
|--------|----------|-------|---------------|---------------|
| Medium | 80–120 cc | 40–60 bar | 0,5–1,0 l/min | 12–16 m, bis 15 t |
| Heavy | 120–250 cc | 50–80 bar | 1,0–2,5 l/min | 16–24 m, bis 40 t |
| Superyacht | 250–1000 cc | 60–120 bar | 2,5–10 l/min | 24+ m, 40+ t |

#### 3.5.2 Integration in bestehende Hydrauliksteuerung

Bei Yachten mit hydraulischer Steueranlage wird der Autopilot-Antrieb als Paralleleinheit in den Hydraulikkreislauf integriert:

**Inline-Pumpe:**
- Autopilot-Pumpe wird in die Hydraulikleitung zwischen Helm-Pumpe und Steuerzylinder eingebaut
- Magnetventil schaltet zwischen manueller und Autopilot-Steuerung
- Vorteil: nutzt den vorhandenen Steuerzylinder
- Nachteil: komplexere Installation, Bypass-Ventil erforderlich

**Separater Zylinder:**
- Eigener Autopilot-Hydraulikzylinder am Quadranten/Tillerarm
- Unabhaengig von der manuellen Hydrauliksteuerung
- Vorteil: Einfachere Installation, keine Aenderung am bestehenden System
- Nachteil: Zwei Zylinder, mehr Platzbedarf

**Wichtig bei hydraulischer Integration:**
- Hydraulikfluid muss kompatibel sein (alle Komponenten gleiches Fluid)
- Entlueftung des Gesamtsystems nach Installation
- Leckage-Ueberwachung: Fluessigkeitsstand regelmaessig pruefen
- Bypass-Ventil muss fuer manuelle Steuerung bei Autopilot-Ausfall vorhanden sein

#### 3.5.3 Vor- und Nachteile

**Vorteile:**
- Hoechste Kraefte und Momente (bis >5.000 Nm Rudermoment)
- Geraeuscharmer Betrieb (Pumpe vibrationsgedaemmt montierbar)
- Keine mechanische Blockade bei Stromausfall (Bypass-Ventil oeffnen)
- Bewaaehrte Technologie in Grossyachten
- Lange Lebensdauer bei korrekter Wartung

**Nachteile:**
- Hoechste Installationskosten (EUR 5.000–25.000+)
- Leckagegefahr (Hydraulikoel im Schiffsinneren)
- Wartungsaufwand: Oelwechsel, Filterwechsel, Dichtungspruefung
- Temperaturempfindlich (Viskositaet bei Kaelte)
- Entlueftung nach Wartung kritisch (Luft im System = Stellkraftverlust)

### 3.6 Vergleichstabelle aller Antriebstypen

| Eigenschaft | Tiller-Pilot | Wheel-Pilot | Linear u.D. | Rotary u.D. | Hydraulik |
|-------------|-------------|-------------|-------------|-------------|-----------|
| Kraft/Moment | 30–60 kg | 5–20 Nm | 50–250 kg | 10–80 Nm | 80–5000+ Nm |
| Stellgeschwindigkeit | 10–20 mm/s | 15–40 Grad/s Rad | 15–28 mm/s | 3–8 Grad/s | 3–10 Grad/s |
| Bootlaenge | 7–10 m | 8–14 m | 9–22 m | 9–18 m | 14–50+ m |
| Verdraengung | bis 5 t | bis 10 t | bis 25 t | bis 20 t | bis 200+ t |
| Installation | 30 min | 30–60 min | 4–8 h | 4–8 h | 8–16 h |
| Platzbedarf Cockpit | Hoch | Mittel | Keiner | Keiner | Keiner |
| Platzbedarf u.D. | Keiner | Keiner | Mittel | Gering | Hoch |
| Geraeusch | Hoch (Cockpit) | Mittel-Hoch | Mittel (u.D.) | Mittel (u.D.) | Gering-Mittel |
| Feedback-Sensor | Nein (intern) | Nein (intern) | Ja (extern) | Ja (integriert) | Ja (extern) |
| Kupplung | Manuell (ausklinken) | Manuell (abnehmen) | Elektromagnetisch | Elektromagnetisch | Bypass-Ventil |
| Lebensdauer | 5–10 Jahre | 5–10 Jahre | 8–15 Jahre | 8–15 Jahre | 10–20 Jahre |
| Wartungsintervall | 1 Jahr | 1 Jahr | 2 Jahre | 2 Jahre | 1 Jahr |
| Preis (Antrieb) | EUR 500–1.800 | EUR 1.200–3.500 | EUR 1.100–2.700 | EUR 1.500–3.000 | EUR 2.000–5.500 |
| Gesamtsystem | EUR 500–1.800 | EUR 1.200–3.500 | EUR 2.500–8.000 | EUR 3.000–8.000 | EUR 5.000–25.000 |

### 3.7 Entscheidungshilfe Antriebswahl

```
Bootlaenge und Steuerungstyp pruefen:
  |
  +-- Pinnensteuerung?
  |     |
  |     +-- Boot < 10 m, < 5 t → Tiller-Pilot
  |     +-- Boot >= 10 m oder >= 5 t → Below-Deck Linear
  |
  +-- Radsteuerung, mechanisch?
  |     |
  |     +-- Boot < 12 m, < 8 t, nur Kuestenfahrt → Wheel-Pilot
  |     +-- Boot < 12 m, Offshore/Blauwasser → Below-Deck Linear
  |     +-- Boot 12–20 m → Below-Deck Linear (150–230 kg)
  |     +-- Boot > 20 m → Hydraulik
  |
  +-- Radsteuerung, hydraulisch?
  |     |
  |     +-- Boot < 14 m → Hydraulik (Inline oder separater Zylinder)
  |     +-- Boot >= 14 m → Hydraulik (passend zur vorhandenen Anlage)
  |
  +-- Katamaran/Trimaran?
        |
        +-- Boot < 12 m → 2x Below-Deck Linear (eine Klasse groesser)
        +-- Boot >= 12 m → 2x Linear oder Hydraulik
```

### 3.8 Windfahnen-Selbststeueranlagen (Windvane Self-Steering)

#### 3.6.1 Grundprinzip

Windfahnen-Selbststeueranlagen nutzen die Kraft des Windes, um das Boot auf einem konstanten Kurs zum Scheinwind zu halten. Sie benoetigen keine elektrische Energie und sind daher die bevorzugte Autopilot-Alternative fuer Langfahrtsegler.

**Grundprinzip:**
1. Eine Windfahne (vertikal oder horizontal) ist parallel zur Schiffsmittellinie ausgerichtet
2. Bei Kursaenderung relativ zum Wind trifft der Wind seitlich auf die Fahne
3. Die Fahne wird aus der Neutralposition ausgelenkt
4. Ueber einen Uebertragungsmechanismus wird diese Auslenkung auf das Ruder oder ein Hilfsruder uebertragen
5. Das Boot kehrt auf den urspruenglichen Kurs zurueck, die Fahne kehrt in die Neutralposition zurueck

#### 3.6.2 Typen von Windsteueranlagen

**Typ 1 — Hilfssegel (Trim Tab auf Hauptruder):**
- Kleine Klappe (Trim Tab) am Heck des Hauptruders
- Windfahne steuert den Trim Tab direkt
- Trim Tab erzeugt ein Moment am Hauptruder, das dieses auslenkt
- Einfachster Typ, aber nur fuer kleine Boote (bis 8 m, bis 3 t)
- Beispiel: Hydrovane (kombiniert als eigenstaendiges System)

**Typ 2 — Pendelruder (Servo-Pendulum):**
- Ein separates Pendelruder haengt am Heck im Wasser
- Die Windfahne lenkt das Pendelruder aus
- Die Wasserstroemung am ausgelenkten Pendelruder erzeugt eine Seitenkraft
- Diese Seitenkraft wird ueber Steuerleinen auf das Hauptruder uebertragen
- Kraefteverstaerkung: die Kraft des Wassers am Pendelruder ist viel groesser als die Windkraft an der Fahne
- Geeignet fuer Yachten von 8–20 m, 3–25 t
- Beispiele: Monitor, Windpilot Pacific, Aries

**Typ 3 — Hilfsruder (Auxiliary Rudder):**
- Eigenstaendiges Hilfsruder am Heck, direkt von der Windfahne gesteuert
- Das Hauptruder wird festgesetzt (mittig oder leichte Vorlast)
- Einfacher Aufbau, aber begrenztes Drehmoment (nur Windkraft an Fahne)
- Geeignet fuer Boote mit schwergaengiger Hauptsteuerung
- Beispiel: Hydrovane

**Typ 4 — Hilfsruder mit Trim Tab (Servo-Auxiliary):**
- Hilfsruder am Heck mit Trim Tab
- Windfahne steuert den Trim Tab des Hilfsruders
- Trim Tab lenkt das Hilfsruder aus (wie Typ 1 am Hilfsruder)
- Gute Kraefteverstaerkung, eigenstaendiges System
- Beispiel: Windpilot Pacific Plus

#### 3.6.3 Fuehrende Windsteueranlagen-Hersteller

**Hydrovane (UK/Kanada):**
- Typ: Hilfsruder (Typ 3), optional mit Trim Tab (Typ 4)
- Modelle: Hydrovane (Einheitsmodell, verschiedene Rudergroessen)
- Besonderheit: Eigenstaendiges Hilfsruder dient gleichzeitig als Notruder
- Montage: Am Heckspiegel oder Badeplattform
- Geeignet fuer: 8–20 m, bis 20 t
- Preis: ca. EUR 3.500–5.500 (je nach Rudergroesse)

**Monitor (USA/Scanmar Marine):**
- Typ: Pendelruder (Typ 2, Servo-Pendulum)
- Modelle: Monitor Windvane (Einheitsmodell)
- Besonderheit: Kraeftigstes Pendelruder-System, Edelstahlkonstruktion
- Montage: Am Heckspiegel, erfordert robuste Heckstruktur
- Geeignet fuer: 9–22 m, bis 25 t
- Preis: ca. EUR 4.500–6.000

**Windpilot (Deutschland, Peter Foerthmann):**
- Typ: Mehrere Varianten
  - Pacific: Pendelruder (Typ 2)
  - Pacific Plus: Hilfsruder mit Trim Tab (Typ 4)
  - Pacific Light: Leichtversion fuer kleinere Boote
- Besonderheit: Deutsche Qualitaet, umfangreiche Beratung, individuelle Anpassung
- Montage: Am Heckspiegel, massgeschneiderte Halterung
- Geeignet fuer: 7–22 m, bis 25 t
- Preis: ca. EUR 3.800–6.500

**Aries (UK):**
- Typ: Pendelruder (Typ 2)
- Klassiker der Blauwasserszene, nicht mehr in Produktion
- Grosse Anzahl gebrauchter Systeme im Umlauf
- Ersatzteile ueber Spezialhersteller verfuegbar

#### 3.6.4 Kombination Windsteueranlage + Elektrischer Autopilot

Die meisten Langfahrtsegler setzen beide Systeme ein:

| Situation | Bevorzugtes System | Begruendung |
|-----------|-------------------|-------------|
| Amwind, gleichmaessiger Wind | Windsteueranlage | Kein Strom, folgt Winddrehung |
| Raumschotkurse, starker Wind | Windsteueranlage | Kraft aus dem Wind, zuverlaessig |
| Vorwindkurse, leichter Wind | Elektrischer Autopilot | Windfahne hat zu wenig Kraft |
| Motorfahrt | Elektrischer Autopilot | Kein Scheinwind fuer Windfahne |
| Hafen-Annaeherung | Elektrischer Autopilot | Praezise Kurssteuerung noetig |
| Wegpunktnavigation | Elektrischer Autopilot | GPS-Track-Funktion |
| Flaute | Elektrischer Autopilot | Windfahne funktionslos |
| Langer Passatwind-Toern | Windsteueranlage | Stromsparend, zuverlaessig |

---

## 4. Produktlinien und Hersteller

### 4.1 Raymarine (FLIR Systems)

Raymarine (Fareham, UK) ist der meistverbreitete Autopilot-Hersteller fuer Segel- und Motoryachten im Bereich 7–24 m. Die aktuelle Plattform heisst "Evolution" und zeichnet sich durch den EV-Sensorkern (Solid-State, 9-Achsen-AHRS) aus, der in vielen Faellen ohne manuelle Kompasskalibrierung auskommt.

#### 4.1.1 Systemarchitektur Evolution

```
  Bedieneinheit ─── SeaTalkng (NMEA2000) ─── Kurscomputer ─── Antriebseinheit
       |                                          |
       |                                    EV-Sensorkern
       |                                    (integriert oder separat)
       |
  Optional: Fernbedienung, MFD, Windsensor
```

**Kurscomputer (ACU — Autopilot Control Unit):**

| Modell | Typ | Antrieb | Geeignet fuer | Artikelnr. | ca. Preis |
|--------|-----|---------|---------------|------------|-----------|
| ACU-100 | Mechanisch | Type 1 Tiller/Wheel | 7–11 m, bis 6 t | E70098 | EUR 650 |
| ACU-150 | Mechanisch | Type 1/2 Linear | 9–14 m, bis 10 t | E70099 | EUR 850 |
| ACU-200 | Mechanisch | Type 2/3 Linear | 12–18 m, bis 18 t | E70100 | EUR 1.100 |
| ACU-300 | Mechanisch | Type 3 Linear | 15–22 m, bis 25 t | E70101 | EUR 1.400 |
| ACU-400 | Hydraulisch | 0.5–5.0 l/min Pumpe | 14–30 m, bis 50 t | E70102 | EUR 1.800 |

Alle ACU-Modelle enthalten den EV-1 Sensorkern (integriert).

**Antriebseinheiten:**

| Modell | Typ | Hub/Moment | Geeignet fuer | Artikelnr. | ca. Preis |
|--------|-----|-----------|---------------|------------|-----------|
| Type 1 Tiller | Pinnen-Linear | 230 mm, 50 kg | 7–11 m, bis 5 t | E12112 | EUR 900 |
| Type 1 Wheel | Radantrieb | 15 Nm | 8–12 m, bis 8 t | E12170 | EUR 1.100 |
| Type 1 Linear | Below-Deck | 305 mm, 80 kg | 9–14 m, bis 10 t | E12139 | EUR 1.300 |
| Type 2 Linear | Below-Deck | 305 mm, 150 kg | 12–18 m, bis 18 t | E12140 | EUR 1.900 |
| Type 3 Linear | Below-Deck | 381 mm, 230 kg | 15–22 m, bis 25 t | E12141 | EUR 2.700 |
| Type 1 Hydraulik | Pumpeneinheit | 80 cc, 0,5 l/min | 12–16 m | E12171 | EUR 2.200 |
| Type 2 Hydraulik | Pumpeneinheit | 150 cc, 1,2 l/min | 16–22 m | E12172 | EUR 3.500 |
| Type 3 Hydraulik | Pumpeneinheit | 250 cc, 2,5 l/min | 20–30 m | E12173 | EUR 5.200 |

**Bedieneinheiten (Control Heads):**

| Modell | Typ | Merkmale | Artikelnr. | ca. Preis |
|--------|-----|----------|------------|-----------|
| p70s | Segel | Farbdisplay, Wind-Modus, Drehknopf | E22166 | EUR 550 |
| p70Rs | Segel Retro | Wie p70s, rundes Gehaeuse | E22167 | EUR 580 |
| p70 | Motor | Farbdisplay, kein Wind-Modus | E22165 | EUR 480 |
| Axiom MFD | Multifunktion | Autopilot-Steuerung ueber MFD | diverse | — |
| S100 | Fernbedienung | Kabellose Fernbedienung, +1/+10 | E15024 | EUR 350 |

**Komplettpaket-Beispiele (EVolution):**

| Paket | Inhalt | Geeignet fuer | ca. Preis |
|-------|--------|---------------|-----------|
| EV-100 Tiller | ACU-100 + Type 1 Tiller + p70s | Pinne 7–11 m | EUR 1.800 |
| EV-100 Wheel | ACU-100 + Type 1 Wheel + p70 | Rad 8–12 m | EUR 2.200 |
| EV-200 Sail | ACU-200 + Type 2 Linear + p70s | Segel 12–18 m | EUR 3.800 |
| EV-200 Power | ACU-200 + Type 2 Linear + p70 | Motor 12–18 m | EUR 3.500 |
| EV-400 Sail | ACU-400 + Type 2 Hydraulik + p70s | Segel 16–24 m | EUR 6.500 |

#### 4.1.2 Besonderheiten Raymarine Evolution

- **AI Calibration:** Der EV-1 Sensorkern erlernt die Bootscharakteristik automatisch waehrend der Fahrt. Keine manuelle Kompassschwenkfahrt erforderlich (wird aber empfohlen fuer optimale Ergebnisse).
- **Dynamic EV Sensor:** 9-Achsen-MEMS mit Sensor-Fusion (Magnetometer + Beschleunigung + Gyroskop). Update-Rate: 10 Hz.
- **SeaTalkng:** NMEA2000-kompatibler Bus mit Raymarine-Steckverbindern (DeviceNet Micro). Volle Interoperabilitaet mit NMEA2000-Geraeten anderer Hersteller ueber Adapter.
- **Autopilot-Modes:** Auto (Heading Hold), Wind Vane, Track, NoDrift, Power Steer, Dodge (kurze Kursaenderung fuer AIS-Ausweichen).
- **Ruderlimit:** Einstellbar 10–30 Grad, seegangabhaengig.

### 4.2 B&G (Navico / Navico Group)

B&G (Brookes & Gatehouse, Romsey, UK) ist der fuehrende Hersteller fuer Regatta- und Performance-Segelyachten. Die Autopilot-Systeme basieren auf der Navico-Plattform (gemeinsam mit Simrad), bieten aber Segel-spezifische Algorithmen und Integration.

#### 4.2.1 Systemarchitektur

```
  Bedieneinheit ─── NMEA2000 ─── NAC Kurscomputer ─── Antriebseinheit
       |                              |
       |                        Precision-9
       |                        (Heading-Sensor)
       |
  H5000 System (optional):
  H5000 CPU ─── Hercules Hydra ─── Performance-Sensoren
```

**Kurscomputer (NAC — Network Autopilot Computer):**

| Modell | Antrieb | Geeignet fuer | Artikelnr. | ca. Preis |
|--------|---------|---------------|------------|-----------|
| NAC-1 | Mechanisch (Linear bis 80 kg) | 8–14 m, bis 10 t | 000-13336-001 | EUR 900 |
| NAC-2 | Mechanisch (Linear bis 230 kg) | 12–20 m, bis 20 t | 000-13338-001 | EUR 1.500 |
| NAC-3 | Hydraulisch (bis 5 l/min) | 16–30 m, bis 50 t | 000-13250-001 | EUR 2.200 |

**Antriebseinheiten (SD-Serie, identisch mit Simrad):**

| Modell | Typ | Leistung | Geeignet fuer | Artikelnr. | ca. Preis |
|--------|-----|----------|---------------|------------|-----------|
| SD10 | Linear | 80 kg, 230 mm | 8–12 m, bis 8 t | 000-13730-001 | EUR 1.100 |
| SD15 | Linear | 150 kg, 305 mm | 11–16 m, bis 15 t | 000-13731-001 | EUR 1.800 |
| SD25 | Linear | 230 kg, 381 mm | 14–22 m, bis 25 t | 000-13732-001 | EUR 2.600 |
| SteadySteer | Hydraulik-Pumpe | 80 cc, 0,5 l/min | 12–16 m | 000-13733-001 | EUR 2.000 |
| RPU-160 | Hydraulik-Pumpe | 160 cc, 1,2 l/min | 16–22 m | 000-13734-001 | EUR 3.200 |
| RPU-300 | Hydraulik-Pumpe | 300 cc, 2,5 l/min | 20–30 m | 000-13735-001 | EUR 5.000 |

**Bedieneinheiten:**

| Modell | Typ | Merkmale | Artikelnr. | ca. Preis |
|--------|-----|----------|------------|-----------|
| Triton2 Pilot | Segelanzeige | AP-Steuerung + Performance-Daten | 000-13295-001 | EUR 650 |
| H5000 Pilot | Regatta | AP + H5000 Integration, Polar | 000-11542-001 | EUR 1.200 |
| Zeus MFD | Multifunktion | AP-Steuerung ueber Zeus | diverse | — |
| WR10 | Fernbedienung | Kabellos, Bluetooth | 000-12316-001 | EUR 320 |

**Heading-Sensoren:**

| Modell | Typ | Genauigkeit | Artikelnr. | ca. Preis |
|--------|-----|------------|------------|-----------|
| Precision-9 | 9-Achsen MEMS AHRS | +-0,5 Grad | 000-12607-001 | EUR 380 |

#### 4.2.2 B&G H5000 Integration

Das H5000-System ist B&Gs Premium-Plattform fuer Regatta- und Performance-Segelyachten:

- **H5000 CPU:** Zentralcomputer fuer Performance-Berechnungen (Polardaten, VMG, Laylines)
- **H5000 Hydra:** Prozessor fuer Sensor-Fusion und Autopilot-Algorithmen
- **Hercules:** Gateway zwischen H5000 (Fastnet) und NMEA2000
- **Autopilot-Integration:** H5000 liefert optimierte Sollwerte (z.B. "optimaler VMG-Kurs") direkt an den Autopilot
- **Wind-Modus Erweitert:** True-Wind-Steering (haelt True-Wind-Angle statt Apparent-Wind-Angle)
- **Seegangs-Algorithmus:** Patentierter Algorithmus fuer Seegangs-adaptives Steuern
- **Performance-Optimierung:** Autopilot steuert auf maximalen VMG (Velocity Made Good), nicht auf festen Windwinkel

### 4.3 Simrad (Navico / Navico Group)

Simrad (Egersund, Norwegen) ist der Schwester-Brand von B&G und teilt die gleiche Hardware-Plattform (NAC, SD-Antriebe, Precision-9). Simrad ist auf Motorboote und Cruising-Segelyachten ausgerichtet.

#### 4.3.1 Systemarchitektur

Identisch mit B&G (siehe 4.2.1), aber mit motorboot-optimierten Bedieneinheiten und Algorithmen.

**Kurscomputer:**
- NAC-1, NAC-2, NAC-3 (identisch mit B&G)
- Simrad-spezifische Firmware mit motorboot-optimierten Defaultwerten

**Antriebseinheiten:**
- SD10, SD15, SD25 (Linear, identisch mit B&G)
- SteadySteer, RPU-160, RPU-300 (Hydraulik, identisch mit B&G)

**Bedieneinheiten:**

| Modell | Typ | Merkmale | Artikelnr. | ca. Preis |
|--------|-----|----------|------------|-----------|
| AP44 | Standard | Farbdisplay, Drehknopf, Motorboot/Segel | 000-13289-001 | EUR 580 |
| AP48 | Premium | Groesseres Display, erweiterte Funktionen | 000-13290-001 | EUR 750 |
| NSX MFD | Multifunktion | AP-Steuerung ueber NSX | diverse | — |
| OP50 | Fernbedienung | Kabelgebunden, robust | 000-12293-001 | EUR 280 |
| WR10 | Fernbedienung | Kabellos (identisch B&G) | 000-12316-001 | EUR 320 |

**Komplettpaket-Beispiele:**

| Paket | Inhalt | Geeignet fuer | ca. Preis |
|-------|--------|---------------|-----------|
| AP44 VRF Medium | NAC-2 + SD15 + AP44 + Precision-9 | Segel 12–16 m | EUR 4.200 |
| AP44 VRF High | NAC-2 + SD25 + AP44 + Precision-9 | Segel 16–20 m | EUR 5.400 |
| AP48 Hydraulik | NAC-3 + RPU-160 + AP48 + Precision-9 | Motor 16–22 m | EUR 6.800 |
| Continuum Paket | NAC-3 + RPU-300 + AP48 + Precision-9 | Motor 20–30 m | EUR 9.500 |

#### 4.3.2 Besonderheiten Simrad

- **Continuum:** Simrads Bezeichnung fuer die adaptive Regelung mit Seegangs-Erkennung und automatischer Gain-Anpassung. Nutzt die Precision-9-Daten (alle 9 Achsen) fuer Wellenperiode und -richtung.
- **Dynamic PID:** Der Kurscomputer passt P, I, D basierend auf Bootgeschwindigkeit, Seegang und Windstaerke kontinuierlich an. Nutzer stellt nur "Response Level" (1–9) ein.
- **Dock Mode:** Langsame, praezise Ruderansteuerung fuer Hafenmanoevrieren (nur bei AP48).
- **Shadow Drive (bei Hydraulik):** Erkennt manuelles Steuern und schaltet den Autopilot automatisch in Standby. Bei Loslassen des Rads uebernimmt der Autopilot den aktuellen Kurs.

### 4.4 Garmin

Garmin (Olathe, Kansas, USA) ist als Kartographie- und GPS-Hersteller in den Autopilot-Markt eingestiegen und bietet mit der Reactor-Serie eine wettbewerbsfaehige Produktlinie.

#### 4.4.1 Systemarchitektur Reactor

```
  GHC-Bedieneinheit ─── NMEA2000 ─── Reactor CCU ─── Antriebseinheit
       |                                   |
       |                             Heading-Sensor
       |                             (in CCU integriert oder extern)
       |
  GPSMAP MFD, Wind, GPS
```

**Kurscomputer (CCU — Course Computer Unit):**

| Modell | Antrieb | Sensor | Geeignet fuer | Artikelnr. | ca. Preis |
|--------|---------|--------|---------------|------------|-----------|
| Reactor 40 Mech | Mechanisch (Linear) | Solid-State 9-Achsen | 8–20 m | 010-02793-00 | EUR 1.400 |
| Reactor 40 Hydraulik | Hydraulisch | Solid-State 9-Achsen | 12–30 m | 010-02794-00 | EUR 1.800 |

**Antriebseinheiten (GHP — Garmin Hydraulic Pump):**

| Modell | Typ | Leistung | Geeignet fuer | Artikelnr. | ca. Preis |
|--------|-----|----------|---------------|------------|-----------|
| GHP Compact Reactor | Hydraulik-Pumpe | 40 cc | 8–12 m Motor | 010-11053-00 | EUR 1.600 |
| GHP 12 Reactor | Hydraulik-Pumpe | 120 cc | 12–16 m | 010-11054-00 | EUR 2.200 |
| GHP 20 Reactor | Hydraulik-Pumpe | 200 cc | 16–22 m | 010-11055-00 | EUR 3.400 |
| GHP 30 Reactor | Hydraulik-Pumpe | 350 cc | 20–30 m | 010-11056-00 | EUR 5.500 |

Garmin bietet auch mechanische Linearantriebe ueber OEM-Partnerschaften (hauptsaechlich mit Optimus/SeaStar):

| Modell | Typ | Leistung | Geeignet fuer | ca. Preis |
|--------|-----|----------|---------------|-----------|
| GHP Smartpump Kit | Linear (Kabel) | Push-Pull-Integration | Motorboot 6–12 m | EUR 2.800 |

**Bedieneinheiten:**

| Modell | Typ | Merkmale | Artikelnr. | ca. Preis |
|--------|-----|----------|------------|-----------|
| GHC 20 | Standard | Monochrom, Drehknopf | 010-01141-00 | EUR 450 |
| GHC 50 | Premium | Farbdisplay, Touch-Tasten | 010-02434-00 | EUR 650 |
| GPSMAP MFD | Multifunktion | AP-Steuerung ueber Kartenplotter | diverse | — |

#### 4.4.2 Besonderheiten Garmin Reactor

- **Shadow Drive:** Bei Hydraulik-Systemen erkennt der Autopilot manuelle Steuereingriffer am Steuerrad und schaltet automatisch in Standby. Beim Loslassen uebernimmt der Autopilot den neuen Kurs.
- **Heading Hold, Wind Hold, Route Hold:** Standard-Modi wie Mitbewerber.
- **Reactor Autopilot App:** Steuerung ueber Garmin Smartwatch (quatix-Serie).
- **Integration:** Nahtlose NMEA2000-Integration mit Garmin MFDs, Wind, AIS.
- **Lernfunktion:** CCU erlernt Bootsverhalten waehrend der Fahrt (aber weniger aggressiv als Raymarine Evolution).

### 4.5 NKE (Frankreich)

NKE (Hennebont, Bretagne, Frankreich) ist der fuehrende Autopilot-Hersteller im Regatta-Segment. Der "Gyropilot" ist auf vielen IMOCA 60, Class 40, Figaro und Mini-Transat-Booten im Einsatz.

#### 4.5.1 Systemarchitektur Gyropilot

```
  Topline Display ─── NKE Bus (proprietaer) ─── Gyropilot Processor ─── Antriebseinheit
       |                                              |
       |                                     Gyropilot Sensor
       |                                     (Ratenkreisel +
       |                                      Kompass + Neigung)
       |
  NKE Netzwerk (Wind, Log, GPS, ...)
```

**Kurscomputer:**

| Modell | Besonderheit | Geeignet fuer | ca. Preis |
|--------|-------------|---------------|-----------|
| Gyropilot 3 | Hochleistungs-Regler, patentierte Regelalgorithmen | Regatta + Fahrt, 8–24 m | EUR 3.500 |
| Gyropilot 3 Zen | Version mit erweitertem Komfort-Modus | Fahrtensegel 10–20 m | EUR 3.200 |

**Sensoren:**

| Modell | Typ | Besonderheit | ca. Preis |
|--------|-----|-------------|-----------|
| Gyropilot Sensor | Ratenkreisel + 3-Achsen-Kompass + Neigung | Hohe Datenrate (50 Hz) | EUR 1.800 |

**Antriebseinheiten:**
NKE verwendet keine eigenen Antriebseinheiten, sondern arbeitet mit Fremdantrieben (Jefa, Lecomble & Schmitt, Hydraulik). Der Gyropilot steuert:

- Jefa Linearantriebe (12V/24V)
- Lecomble & Schmitt Hydraulik-Zylinder
- Standard NMEA2000-kompatible Drives

**Bedieneinheiten:**

| Modell | Typ | Merkmale | ca. Preis |
|--------|-----|----------|-----------|
| Topline TL25 | Grossdisplay | 5" Farbdisplay, Multifunktion | EUR 1.200 |
| Pilot Remote | Funkfernbedienung | Kabellos, wasserdicht | EUR 380 |
| Multigraphic | Regatta-Display | Performance + AP-Steuerung | EUR 950 |

#### 4.5.2 Besonderheiten NKE Gyropilot

- **Regelguete:** Der Gyropilot 3 gilt als der praeziseste Segelboot-Autopilot am Markt. Die patentierten Regelalgorithmen minimieren Ruderaktivitaet bei maximaler Kursgenauigkeit.
- **Seegangs-Algorithmus:** Erkennt Wellenperiode und -richtung und passt die Regelung an. Bei achterlichem Seegang wird das Ruder fruehzeitig ausgelenkt, um Abschmieren (Broaching) zu verhindern.
- **Anti-Broaching:** Spezieller Modus fuer Vorwindkurse im Seegang (kritisch bei Regattayachten mit flachen Rueckspiegeln).
- **Stromverbrauch:** Durch optimale Regelung typisch 30–40 % weniger als Mitbewerber bei gleicher Bootgroesse.
- **NKE-Bus:** Proprietaerer Bus (kein NMEA2000), erfordert NKE-Netzwerk. NMEA2000-Gateway verfuegbar (NKE Interface Box).
- **Preis:** Premium-Segment (Gesamtsystem EUR 6.000–12.000), aber im Racing-Segment Standard.

### 4.6 Weitere Hersteller

#### 4.6.1 Furuno

- Primaer fuer Berufsfischerei und Grossyachten
- NAVpilot 711C: Kompakter Autopilot fuer 10–25 m
- NAVpilot 720: Premium-System fuer 20–80 m mit Fantum-Feedback-Technologie
- Aqua-Drive-Kupplungssysteme fuer alle Rudersysteme
- NMEA2000 und Furuno-CAN-Bus (proprietaer)
- Preissegment: EUR 3.000–15.000

#### 4.6.2 Pelagic (Australien)

- Spezialisiert auf Langfahrt-Segelyachten
- Pelagic Autopilot: Robuster Linearantrieb mit separatem Kurscomputer
- Bekannt fuer extreme Zuverlaessigkeit und einfache Reparierbarkeit
- Alle Komponenten einzeln austauschbar
- Preissegment: EUR 3.000–6.000

#### 4.6.3 ComNav (Kanada)

- Primaer fuer Berufsfischerei und Arbeitswahrzeuge
- ComNav 1001/2001/5001: Robuste Systeme fuer raue Bedingungen
- Hydraulik-Antriebe fuer grosse Kraefte
- Preissegment: EUR 2.500–10.000

#### 4.6.4 Coursemaster (Australien)

- CM950: Kompakter Autopilot fuer Segelyachten
- Bekannt in Australien und Neuseeland
- Robuste Konstruktion fuer Blauwassersegler
- Preissegment: EUR 2.000–5.000

### 4.7 Herstellervergleich — Uebersicht

| Kriterium | Raymarine | B&G | Simrad | Garmin | NKE |
|-----------|-----------|-----|--------|--------|-----|
| Primaer-Markt | Cruising | Racing/Perf. | Motorboot | Cruising | Racing |
| Regelguete Segel | Gut | Sehr gut | Gut | Gut | Exzellent |
| Regelguete Motor | Gut | Gut | Sehr gut | Sehr gut | Gut |
| Seegangs-Adaptiv | Ja (EV) | Ja (H5000) | Ja (Cont.) | Ja | Ja (patentiert) |
| Wind-Modus | AWA | AWA + TWA | AWA | AWA | AWA + TWA |
| Bus-System | SeaTalkng | NMEA2000 | NMEA2000 | NMEA2000 | NKE (prop.) |
| MFD-Integration | Axiom | Zeus | NSX | GPSMAP | NKE-Display |
| Ersatzteil-Verfuegbarkeit | Sehr gut | Gut | Gut | Gut | Eingeschraenkt |
| Service-Netzwerk | Weltweit | Weltweit | Weltweit | Weltweit | EU/Regatta |
| Preis-Niveau | Mittel | Mittel-Hoch | Mittel | Mittel | Hoch |
| Einsteiger-System ab | EUR 1.800 | EUR 2.800 | EUR 2.800 | EUR 2.500 | EUR 6.000 |

---

## 5. Dimensionierung und Auslegung

### 5.1 Grundsaetze der Dimensionierung

Die korrekte Dimensionierung eines Autopiloten ist entscheidend fuer:
- Zuverlaessige Funktion unter allen Bedingungen
- Lebensdauer der Antriebseinheit
- Energieeffizienz (ueberdimensionierter Antrieb verbraucht unnoetig Strom)
- Regelguete (unterdimensionierter Antrieb kann das Ruder nicht schnell genug bewegen)

Die wichtigsten Parameter fuer die Dimensionierung sind:
1. Verdraengung des Bootes (segelfertig, voll beladen)
2. Rudermoment (Drehmoment am Ruderschaft)
3. Bootstyp (Segel/Motor, Langkiel/Kurzkiel, Einrumpf/Mehrrumpf)
4. Maximale Bootgeschwindigkeit
5. Einsatzgebiet (Kuestenfahrt, Offshore, Blauwasser)

### 5.2 Verdraengungsbasierte Dimensionierung

Die einfachste Methode: Bootsverdraengung → Antriebsklasse. Alle Hersteller geben Empfehlungen auf dieser Basis.

**Segelyachten (Einrumpf, Kurzkiel):**

| Verdraengung | Empfohlener Antrieb | Ruderkraft (linear) | Bemerkung |
|-------------|--------------------|--------------------|-----------|
| bis 3.000 kg | Tiller-Pilot 50 kg | — | Nur Kuestenfahrt |
| 2.500–5.000 kg | Linear 80 kg | 150–250 mm Hub | Kuestenfahrt + gelegentlich Offshore |
| 4.000–10.000 kg | Linear 150 kg | 230–305 mm Hub | Standard Offshore |
| 8.000–18.000 kg | Linear 230 kg | 305–381 mm Hub | Blauwasser |
| 12.000–25.000 kg | Hydraulik 80–150 cc | — | Schwere Fahrtenyacht |
| 20.000–50.000 kg | Hydraulik 150–300 cc | — | Grossyacht |
| >50.000 kg | Hydraulik 300+ cc | — | Superyacht |

**Motoryachten (Verdraenger):**

| Verdraengung | Empfohlener Antrieb | Bemerkung |
|-------------|--------------------|----|
| bis 3.000 kg | Linear 80 kg | Kleine Motorboot |
| 3.000–8.000 kg | Linear 150 kg | Kajuetmotorboot |
| 8.000–20.000 kg | Hydraulik 80–150 cc | Motoryacht |
| 20.000–50.000 kg | Hydraulik 150–300 cc | Grosse Motoryacht |
| >50.000 kg | Hydraulik 300+ cc | Superyacht |

**Gleiter und Halbgleiter:**
- Gleiter haben hoehere Ruderkraefte bei Gleitfahrt als verdraengende Boote gleicher Groesse
- Daumenregel: eine Klasse groesser waehlen als nach Verdraengung allein
- Hydraulik wird bei Gleitern oft schon ab 8 m empfohlen (wegen hoher Geschwindigkeit)

### 5.3 Rudermoment-basierte Dimensionierung

Die praezisere Methode beruecksichtigt das tatsaechliche Rudermoment:

**Berechnung des maximalen Rudermoments:**
```
T_rudder = F_rudder * r_lever

wobei:
  F_rudder = Ruderkraft [N]
  r_lever = Hebelarm vom Ruderschaft zum Kraftangriffspunkt [m]

Ruderkraft (vereinfacht):
  F_rudder = 0.5 * rho * v^2 * A_rudder * C_n

wobei:
  rho = Wasserdichte [kg/m^3] (Seewasser: 1025)
  v = Bootsgeschwindigkeit [m/s]
  A_rudder = Ruderblattflaeche [m^2]
  C_n = Normalkraftbeiwert (abhaengig von Anstellwinkel, typisch 0.5-1.8)

Fuer Autopilot-Dimensionierung (Dauerbelastung):
  T_design = T_rudder * SF

  SF (Sicherheitsfaktor):
  - Kuestenfahrt: 1.5
  - Offshore: 1.75
  - Blauwasser: 2.0
```

**Umrechnung Rudermoment → Antriebskraft (Linearantrieb):**
```
F_drive = T_rudder / r_arm

wobei:
  r_arm = Abstand Linearantrieb-Anlenkung zum Ruderschaft [m]

Typische Hebelarme:
  Quadrant-Anlenkung: 100–250 mm (je nach Quadrantgroesse)
  Tillerarm: 150–350 mm
```

**Beispielrechnung:**
```
Boot: 12 m Segelyacht, 8.000 kg
Ruderblattflaeche: 0,18 m^2
Max. Bootsgeschwindigkeit: 7,5 kn = 3,86 m/s
C_n bei 15 Grad Anstellwinkel: 0,9
Hebelarm (Balance): 0,07 m (30 % Balance, Chord 0,35 m → 0,25-0,30 * 0,35 = ~0,07 m)

F_rudder = 0,5 * 1025 * 3,86^2 * 0,18 * 0,9 = 1.238 N

T_rudder = 1.238 * 0,07 = 87 Nm (am Ruderschaft, netto)

T_design = 87 * 1,75 = 152 Nm (mit SF fuer Offshore)

Bei Quadrant-Hebelarm 200 mm:
F_drive = 152 / 0,20 = 760 N = 77 kg

→ Linearantrieb mit mindestens 80 kg (z.B. SD10 oder Type 1 Linear)
  Besser: 150 kg Klasse (SD15 oder Type 2 Linear) fuer Reserve
```

> ⚠️ **ZU PRÜFEN (Audit):** 87 Nm netto / 152 Nm (mit SF 1,75) hier vs. ca. 0,85 Nm netto aus der Rudermoment-Schnellformel in ANHANG P — rund 100x Abweichung, obwohl beide als Dimensionierungsformel dienen. Diese hydrodynamische Rechnung (F = 0,5 * rho * v^2 * A * C_n) liegt in plausibler Groessenordnung: die Industrieformel Lecomble & Schmitt / Peachment (C = S * (0,4*Lg - Lc) * V^2 * K, K = 15,89-19,52, Segler-Korrektur x0,5) liefert fuer vergleichbare Ruderdaten ca. 28-55 Nm netto — gleiche Groessenordnung; die ANHANG-P-Formel nicht. C_n = 0,9 und Hebelarm 0,07 m sind konservativ, aber nicht zweifelsfrei belegt. Vor Antriebsauslegung mit Norm-/Herstellerformel (ISO 12215-8, LS/Peachment) gegenrechnen (Confidence: estimated — unverifiziert).

### 5.4 Hublaengen-Dimensionierung (Linearantriebe)

Der Hub des Linearantriebs muss den gewuenschten Ruderausschlag abdecken:

```
Hub = 2 * r_arm * sin(alpha_max)

wobei:
  r_arm = Hebelarm am Quadranten [m]
  alpha_max = max. Ruderausschlag [Grad], typisch 30-35 Grad

Beispiel:
  r_arm = 200 mm
  alpha_max = 30 Grad
  Hub = 2 * 200 * sin(30) = 2 * 200 * 0,5 = 200 mm
  → 230 mm Hub-Antrieb ist ausreichend
```

**Wichtig:** Der Autopilot nutzt typisch nur +-15 bis +-25 Grad. Der volle Ruderausschlag (+-35 Grad) wird nur bei manuellem Steuern oder Notmanoevern benoetigt. Der Hub sollte dennoch den vollen Ausschlag abdecken.

### 5.5 Hydraulik-Dimensionierung

Bei hydraulischen Systemen bestimmt das Zylindervolumen pro Hub die erforderliche Pumpenleistung:

```
Pumpenleistung [cc/s] = Zylindervolumen [cc] * Stellgeschwindigkeit [Hub/s]

Stellgeschwindigkeit (Zielwert):
  Segelboote: 5-8 Grad/s Ruderausschlag
  Motorboote: 3-5 Grad/s Ruderausschlag

Zylindervolumen pro Grad Ruderausschlag:
  V_deg = pi * (d_cylinder/2)^2 * stroke_per_deg

  d_cylinder = Zylinderkolben-Durchmesser [mm]
  stroke_per_deg = Hub pro Grad Ruderausschlag [mm/Grad]
```

### 5.6 Multihull-Besonderheiten

Katamarane und Trimarane haben besondere Anforderungen:

- **Hohe Geschwindigkeit:** Katamarane segeln typisch 20–50 % schneller als gleich lange Einrumpfer → hoehere Ruderkraefte
- **Doppelruder:** Zwei Ruderblaaetter erfordern entweder zwei Antriebe oder eine mechanische Kopplung
- **Leichtes Gewicht:** Trotz geringerer Verdraengung (pro Rumpf) hoehere Ruderkraefte durch Geschwindigkeit
- **Daumenregel:** Antrieb mindestens eine Klasse ueber der Verdraengungs-Empfehlung waehlen
- **NKE Gyropilot:** Besonders beliebt bei schnellen Katamaranen (IMOCA, Ultim, Outremer) wegen Anti-Broaching

### 5.7 Dimensionierungstabelle — Schnellreferenz

| LOA | Typ | Verdraengung | Empfehlung Antrieb | Empfehlung Computer |
|-----|-----|-------------|-------------------|-------------------|
| 7–9 m | Segel, Pinne | 1,5–3 t | Tiller-Pilot 50 kg | Integriert |
| 9–11 m | Segel, Rad | 3–5 t | Linear 80 kg | ACU-100/NAC-1 |
| 11–13 m | Segel | 5–9 t | Linear 80–150 kg | ACU-150/NAC-1 |
| 13–15 m | Segel | 8–13 t | Linear 150 kg | ACU-200/NAC-2 |
| 15–18 m | Segel | 12–20 t | Linear 230 kg | ACU-200/NAC-2 |
| 18–22 m | Segel | 18–30 t | Hydraulik 150 cc | ACU-400/NAC-3 |
| 22–30 m | Segel | 25–60 t | Hydraulik 300 cc | ACU-400/NAC-3 |
| 8–12 m | Motor | 3–8 t | Linear 80–150 kg | ACU-150/NAC-1 |
| 12–16 m | Motor | 8–18 t | Hydraulik 80 cc | ACU-400/NAC-3 |
| 16–22 m | Motor | 15–35 t | Hydraulik 150 cc | ACU-400/NAC-3 |
| 22–30 m | Motor | 30–70 t | Hydraulik 300 cc | ACU-400/NAC-3 |

### 5.8 Sicherheitszuschlaege und Einsatzgebiet

Die Dimensionierung muss das Einsatzgebiet beruecksichtigen. Hoehere Seegangsbedingungen bedeuten hoehere Ruderkraefte und laengere Betriebszeiten:

**Kuestenfahrt (CE-Kategorie C/D):**
- Sicherheitsfaktor: 1,5
- Typische Dauerlast: 30–50 % der maximalen Antriebskraft
- Betriebsdauer pro Tag: 4–8 Stunden
- Standard-Dimensionierung nach Herstellerempfehlung ausreichend

**Offshore (CE-Kategorie B):**
- Sicherheitsfaktor: 1,75
- Typische Dauerlast: 40–60 % der maximalen Antriebskraft
- Betriebsdauer pro Tag: 8–16 Stunden
- Eine Antriebsklasse groesser als Herstellerempfehlung waehlen

**Blauwasser (CE-Kategorie A):**
- Sicherheitsfaktor: 2,0
- Typische Dauerlast: 50–70 % der maximalen Antriebskraft
- Betriebsdauer pro Tag: 16–24 Stunden (quasi Dauerbetrieb)
- Eine Antriebsklasse groesser + Backup-System (Tiller-Pilot oder Windsteueranlage)
- Redundante Stromversorgung (Solar/Wind deckt Autopilot-Verbrauch)

**Regatta (IMOCA, Class 40, Mini):**
- Sicherheitsfaktor: 2,0–2,5
- Extreme Ruderkraefte bei Surfen (20+ kn Bootsgeschwindigkeit)
- Anti-Broaching-Faehigkeit erforderlich
- Zwei unabhaengige Antriebe bei Doppelruder
- NKE Gyropilot oder B&G H5000 empfohlen

### 5.9 Temperaturbereich und Umgebungsbedingungen

| Komponente | Betriebstemperatur | Lagertemperatur | Feuchtigkeit |
|------------|-------------------|-----------------|-------------|
| Kurscomputer | -15 bis +55 Grad C | -30 bis +70 Grad C | 0–95 % rel., nicht kondensierend |
| Linearantrieb | -10 bis +50 Grad C | -30 bis +70 Grad C | 0–100 % (IPX6/IPX7) |
| Hydraulikpumpe | -10 bis +60 Grad C | -30 bis +70 Grad C | 0–100 % |
| MEMS-Sensor | -20 bis +60 Grad C | -40 bis +80 Grad C | 0–95 % |
| Bedieneinheit | -15 bis +55 Grad C | -30 bis +70 Grad C | IPX6 (Cockpit) |
| Tiller-Pilot | -5 bis +45 Grad C | -20 bis +60 Grad C | IPX6 |

**Besondere Umgebungen:**
- Tropen: Dauerhitze im Maschinenraum (60+ Grad C) kann Antriebe ueberlasten → Belueftung!
- Arktis/Antarktis: Hydraulikfluid verdickt unter -5 Grad C → Spezialfluid oder Heizung
- Salzspray: alle Steckverbindungen mit Kontaktfett schuetzen
- UV: Tiller-Pilot und Cockpit-Bedieneinheiten altern durch UV-Strahlung

---

## 6. NMEA2000/SeaTalk Integration

### 6.1 NMEA2000 Grundlagen fuer Autopiloten

NMEA2000 (IEC 61162-3) ist der Standard-Datenbus fuer marine Elektronik. Alle modernen Autopiloten nutzen NMEA2000 fuer die Kommunikation zwischen Kurscomputer, Sensoren, Anzeigen und Navigationssystemen.

**Physische Schicht:**
- CAN-Bus (Controller Area Network), 250 kbit/s
- DeviceNet Micro-C Stecker (5-polig: Schirm, NET-S, NET-C, V+, V-)
- Backbone-Kabel (Hauptleitung) mit T-Stuecken und Stichleitungen
- Terminatoren an beiden Enden des Backbones
- Spannungsversorgung: 12V DC ueber den Bus (NET-V+ / NET-S)
- Max. Backbone-Laenge: 100 m, Stichleitungen: max. 6 m

**Relevante PGN (Parameter Group Numbers) fuer Autopiloten:**

| PGN | Name | Sender | Inhalt |
|-----|------|--------|--------|
| 127245 | Rudder | Rudersensor | Ruderposition (Grad), Instanz |
| 127250 | Vessel Heading | Kompass/AHRS | Heading (magnetisch/rechtweisend), Deviation |
| 127251 | Rate of Turn | Ratenkreisel | Drehrate (Grad/s) |
| 127252 | Heave | Bewegungssensor | Vertikalbeschleunigung |
| 127257 | Attitude | AHRS | Roll, Pitch, Yaw |
| 127258 | Magnetic Variation | GPS/Kompass | Missweisung |
| 128259 | Speed: Water Ref. | Log/Echolot | Geschwindigkeit durchs Wasser |
| 128267 | Water Depth | Echolot | Wassertiefe |
| 129025 | Position Rapid | GPS | Lat/Lon (10 Hz) |
| 129026 | COG/SOG Rapid | GPS | Kurs/Geschwindigkeit ueber Grund |
| 129029 | GNSS Position | GPS | Position, Satellitenanzahl |
| 129283 | Cross Track Error | Kartenplotter | Seitenabweichung von Route |
| 129284 | Navigation Data | Kartenplotter | Kurs zum Wegpunkt, Distanz |
| 130306 | Wind Data | Windsensor | Windgeschwindigkeit, -richtung |
| 065280 | Autopilot Command | Bedieneinheit | Soll-Kurs, Modus, Gain |
| 065340 | Autopilot State | Kurscomputer | Ist-Zustand, Modus, Alarm |

### 6.2 SeaTalk / SeaTalkng (Raymarine)

**SeaTalk (alt, SeaTalk1):**
- Proprietaerer 3-Draht-Bus (Daten, 12V, Masse)
- 4800 Baud, Daisy-Chain-Topologie
- Bis ca. 2015 Standard bei Raymarine-Geraeten
- Adapter zu NMEA2000 ueber Raymarine SeaTalk-zu-SeaTalkng-Konverter (E22158)

**SeaTalkng (aktuell):**
- Physisch und logisch identisch mit NMEA2000 (CAN-Bus, DeviceNet)
- Nutzt Raymarine-eigene Steckverbinder (optisch anders, aber kompatibel)
- Adapter: SeaTalkng-zu-DeviceNet (A06045, EUR 25)
- Volle Interoperabilitaet mit NMEA2000 ueber Adapter
- Alle Raymarine Evolution-Komponenten nutzen SeaTalkng

### 6.3 Autopilot-Netzwerk-Topologie

**Minimale Konfiguration:**
```
Bedieneinheit ── T ── Backbone ── T ── Kurscomputer
                                  |
                                  T
                                  |
                            Antriebseinheit
                            (bei separatem NMEA2000-Anschluss)

+ Terminatoren an beiden Backbone-Enden
+ 12V-Speisung am Backbone
```

**Typische Konfiguration:**
```
Terminator ── GPS ── Windsensor ── AIS ── Bedieneinheit ── Kurscomputer ── Kartenplotter ── Terminator
                                                                |
                                                          Antriebseinheit
                                                          (ueber separates Kabel oder Backbone-Stichleitung)
```

**Wichtige Installationsregeln:**
- Autopilot-Kurscomputer direkt am Backbone (nicht ueber lange Stichleitungen)
- Ruderfeedback-Sensor so nah wie moeglich am Kurscomputer
- GPS-Antenne mit freier Sicht (kein Abschatten durch Mast)
- Windsensor moeglichst an der Mastspitze (ungestoerter Wind)
- Separate Stromversorgung fuer Autopilot-Antrieb (nicht ueber NMEA2000-Bus!)
- NMEA2000-Bus versorgt nur Steuersignale (max. 3 A pro Bus-Segment)

### 6.4 Datenfluss im Autopilot-Netzwerk

```
  GPS ──────────────> Kurscomputer: Position, COG, SOG
  Kompass/AHRS ─────> Kurscomputer: Heading, Rate-of-Turn, Attitude
  Windsensor ───────> Kurscomputer: AWA, AWS (fuer Wind-Modus)
  Kartenplotter ────> Kurscomputer: XTE, Bearing-to-WP (fuer Track-Modus)
  Rudersensor ──────> Kurscomputer: Ruderlage (Feedback)
  Log/Echolot ──────> Kurscomputer: Speed through Water (fuer Gain-Anpassung)

  Kurscomputer ─────> Antriebseinheit: Stellsignal (Ruder-Sollposition)
  Kurscomputer ─────> Bedieneinheit: Status, Ist-Kurs, Modus, Alarme
  Kurscomputer ─────> Netzwerk: PGN 065340 (Autopilot State)
  Bedieneinheit ────> Kurscomputer: Sollkurs, Modusaenderung, Gain
```

### 6.5 Kompatibilitaet und Herstellermischung

**Generelle Regel:** NMEA2000-konforme Geraete verschiedener Hersteller koennen auf demselben Bus betrieben werden. Autopiloten sind jedoch komplexe Systeme mit proprietaeren Erweiterungen:

| Kombination | Kompatibilitaet | Einschraenkung |
|-------------|----------------|----------------|
| Raymarine AP + Garmin GPS | Voll (NMEA2000) | Kein Garmin-spezifischer Track-Modus |
| Simrad AP + Raymarine MFD | Eingeschraenkt | MFD kann AP nicht vollstaendig steuern |
| B&G NAC + Simrad AP44 | Voll | Gleiche Plattform (Navico) |
| Garmin AP + B&G Wind | Voll (NMEA2000) | Wind-Modus funktioniert |
| NKE Gyropilot + NMEA2000 | Ueber Gateway | NKE Interface Box erforderlich |
| Beliebiger AP + NMEA2000 Rudersensor | Voll | PGN 127245 ist standardisiert |

**Empfehlung:** Kurscomputer und Bedieneinheit vom gleichen Hersteller. Sensoren (GPS, Wind, Log) koennen herstelleruebergreifend gewaehlt werden, solange sie NMEA2000 sprechen.

### 6.6 Firmware-Updates und Software-Versionen

**Bedeutung von Firmware-Updates:**
- Verbesserte Regelalgorithmen (bessere Kursgenauigkeit, weniger Stromverbrauch)
- Bugfixes (bekannte Probleme mit bestimmten Antriebskombinationen)
- Neue Funktionen (z.B. NoDrift-Modus bei Raymarine Evolution ab Firmware 2.1)
- Kompatibilitaet mit neuen Geraeten im Netzwerk
- Sicherheitsrelevante Updates (z.B. Track-Modus Alarme gemaess IEC 62065)

**Update-Verfahren nach Hersteller:**

| Hersteller | Update-Medium | Software | Typische Groesse | Dauer |
|------------|--------------|----------|-----------------|-------|
| Raymarine | SD-Karte am MFD oder LightHouse Update App | LightHouse | 50–200 MB | 10–20 min |
| B&G/Simrad | SD-Karte oder GoFree App | GoFree | 30–150 MB | 10–15 min |
| Garmin | SD-Karte oder Garmin Express | Garmin Express | 50–250 MB | 15–30 min |
| NKE | USB ueber NKE Topmodule | NKE Software Suite | 5–20 MB | 5–10 min |
| Furuno | SD-Karte | Furuno Update Tool | 30–100 MB | 10–20 min |

**Wichtig bei Updates:**
- Immer zuerst aktuelle Einstellungen notieren (Response Level, Ruderlimit, Bootstyp)
- Update im Hafen durchfuehren, nicht auf See
- Stromversorgung stabil (Landstrom oder volle Batterie)
- Nach Update: alle Einstellungen pruefen und ggf. Kompass neu kalibrieren
- Bei Komplett-System: alle Geraete auf kompatible Firmware-Version bringen

### 6.7 Elektromagnetische Vertraeglichkeit (EMV)

**EMV-Grundregeln fuer Autopilot-Installation:**
- NMEA2000-Backbone mindestens 30 cm von Starkstromkabeln (230V AC, Motor) verlegen
- Heading-Sensor mindestens 1 m von VHF-Antennenkabel entfernt montieren
- SSB-/HF-Antennentuner kann Kompass-Stoerungen verursachen (beim Senden)
- Frequenzumrichter (Inverter) koennen CAN-Bus stoeren: geschirmtes Kabel verwenden
- LED-Beleuchtung mit minderwertigen Treibern kann CAN-Bus-Stoerungen erzeugen
- Motor-Anlasser verursacht kurzzeitigen Spannungseinbruch: Autopilot muss das tolerieren

**Schirmung und Erdung:**
- NMEA2000-Backbone-Kabel hat integrierten Schirm: an einem Ende erden (Schiffserde)
- Nicht beidseitig erden (Erdschleife → Stoerungen)
- Autopilot-Leistungskabel: moeglichst kurz, verdrillt, direkt zur Batterie
- Sicherung am Batteriepol (nicht am Autopilot-Ende)

### 6.8 Kabelquerschnitte und Sicherungen

**Antriebseinheit (Leistungskabel, direkt von Batterie):**

| Antrieb | Stromaufnahme (Spitze) | Kabelquerschnitt (12V, 5m) | Sicherung |
|---------|----------------------|---------------------------|-----------|
| Tiller-Pilot | 4 A | 1,5 mm^2 | 7,5 A |
| Linear 80 kg | 8 A | 2,5 mm^2 | 15 A |
| Linear 150 kg | 15 A | 4,0 mm^2 | 25 A |
| Linear 230 kg | 25 A | 6,0 mm^2 | 40 A |
| Hydraulik klein | 20 A | 6,0 mm^2 | 30 A |
| Hydraulik mittel | 35 A | 10,0 mm^2 | 50 A |
| Hydraulik gross | 60 A | 16,0 mm^2 | 80 A |

**NMEA2000-Bus:** Backbone: 0,75 mm^2, Stichleitungen: 0,5 mm^2. Sicherung: 3 A pro Segment.

---

## 7. Fehlerbild-Atlas

### 7.1 Fehlerbild F01 — Kompassfehler / Deviation

**Symptom:** Autopilot steuert systematisch einen falschen Kurs. Die Abweichung ist richtungsabhaengig (z.B. auf Nordkurs +5 Grad, auf Suedkurs -3 Grad). Kurs "springt" bei Aenderung der elektrischen Verbraucher (Ankerlicht, Kuehlschrank).

**Ursache:**
- Nicht oder fehlerhaft kalibrierter Kompass
- Veraenderte magnetische Umgebung (neuer Motor, Lautsprecher, Werkzeug in Naehe)
- Magnetfeldstoerugen durch elektrische Leitungen in Naehe des Sensors
- Bei Fluxgate: Heel-Fehler (Segelyacht unter Kraengung)
- Bei MEMS: Drift durch Temperaturaenderung oder Vibration

**Diagnose:**
1. Vergleich Autopilot-Heading mit Handkompass auf allen 4 Himmelsrichtungen (N, O, S, W)
2. Deviation >5 Grad auf irgendeinem Kurs: Kalibrierung erforderlich
3. Pruefung auf neue Stoerquellen in der Naehe des Sensors
4. Bei Heel-Fehler: Heading-Aenderung unter Kraengung gegenueber aufrecht vergleichen

**Behebung:**
- Kompass-Kalibrierung (Schwenkfahrt: 2 langsame 360-Grad-Drehungen)
- Stoerquellen entfernen oder Sensor versetzen
- Mindestabstaende pruefen (siehe 2.2.1)
- Bei persistierender Deviation: Sensor an anderem Ort montieren

**AYDI-Relevanz:** Confidence: visual_low (Kompassfehler nicht visuell erkennbar). Indikator: Kurs-Track auf Karte zeigt systematische Abweichung. Modul: Compliance.

### 7.2 Fehlerbild F02 — Antriebskupplung rutscht

**Symptom:** Autopilot zeigt korrekten Kurs-Sollwert, Antrieb laeuft hoerbar, aber Ruder bewegt sich nicht oder nur teilweise. Intermittierendes "Klacken" oder "Rattern" bei hoeherer Ruderbelastung.

**Ursache:**
- Verschlissene elektromagnetische Kupplung (bei Linearantrieben mit Kupplung)
- Zu niedrige Bordspannung → Kupplung haelt nicht vollstaendig
- Bei Wheel-Pilot: Reibrad abgenutzt oder nass (Schlupf)
- Bei Hydraulik: internes Bypass-Ventil undicht
- Mechanische Verbindung locker (Pin, Gabelkopf, Kugelgelenk ausgeschlagen)

**Diagnose:**
1. Autopilot auf Heading-Hold, dann Ruder manuell gegen Autopilot druecken: gibt Antrieb nach?
2. Bordspannung unter Last messen (muss >11,5 V bei 12V-System, >23,0 V bei 24V-System)
3. Verbindungselemente (Pins, Gabelkoepfe, Kugelgelenke) auf Spiel pruefen
4. Bei Wheel-Pilot: Reibrad-Oberflaeche pruefen, ggf. mit Schleifpapier aufrauen

**Behebung:**
- Kupplung tauschen (Verschleissteil, alle 5–10 Jahre)
- Bordspannung erhoehen (Ladezustand Batterie pruefen)
- Mechanische Verbindungen nachziehen oder tauschen
- Wheel-Pilot: Reibrad tauschen, Steuerrad-Oberflaeche reinigen

**AYDI-Relevanz:** Confidence: visual_medium (Verschlissene Kupplung ggf. an Ruderposition sichtbar). Modul: Structural, Cost.

### 7.3 Fehlerbild F03 — Hunting (Pendelung / Pendeln)

**Symptom:** Das Ruder bewegt sich staendig hin und her, Boot faehrt Schlangenlinien. Autopilot "jagt" dem Kurs hinterher, ohne sich zu stabilisieren. Erhoehter Stromverbrauch und Geraeuschentwicklung.

**Ursache:**
- P-Gain (Proportionalverstaerkung) zu hoch eingestellt
- D-Gain (Daempfung) zu niedrig
- Ruderfeedback-Sensor fehlkalibriert oder defekt (falsches Signal → falsche Reaktion)
- Spiel in der Steueranlage (Lose in Kette, Seil, Hydraulik) → Totzone → Ueberkompensation
- Zu schnelle Stellgeschwindigkeit fuer das Boot (Antrieb zu direkt)

**Diagnose:**
1. Response/Gain-Einstellung schrittweise reduzieren: Hunting verschwindet → Gain zu hoch
2. Ruderfeedback-Anzeige pruefen: zeigt Ruder Mittschiffs bei tatsaechlich mittiger Position?
3. Steueranlage auf Spiel pruefen (Ruder von Hand bewegen, Steuerrad beobachten)
4. Stellgeschwindigkeit im Verhaeltnis zur Bootgroesse pruefen

**Behebung:**
- P-Gain reduzieren (weniger aggressiv)
- D-Gain erhoehen (mehr Daempfung)
- Ruderfeedback neu kalibrieren
- Spiel in der Steueranlage beseitigen (Seile spannen, Ketten nachziehen)
- Bei persistierendem Hunting: Autopilot-Lernfahrt wiederholen (Autolearn/Sea Trial)

**AYDI-Relevanz:** Confidence: documented (aus Logdaten erkennbar). Modul: Ergonomics (Komforteinbusse), Cost (Stromverbrauch).

### 7.4 Fehlerbild F04 — Ueberkompensation (Overshoot)

**Symptom:** Bei Kursaenderung schiesst das Boot ueber den Sollkurs hinaus und pendelt sich erst nach 2-3 Schwingungen ein. Besonders auffaellig bei 10-Grad-Kursaenderungen und Wegpunkt-Uebergaengen.

**Ursache:**
- I-Gain zu hoch: Integral-Anteil "laeuft auf" waehrend Kursaenderung
- Ruderlimit zu hoch: zu grosser Ruderausschlag bei Kursaenderung
- Boot hat viel Traegheit (schwer, langer Kiel): braucht frueheres Abbremsen
- Boottyp im Kurscomputer falsch eingestellt (z.B. "Motorboot" statt "Segelyacht")

**Diagnose:**
1. 10-Grad-Kursaenderung kommandieren und Einschwingverhalten beobachten
2. Mehr als 1 Ueberschwingen → Regelparameter anpassen
3. Bootstyp-Einstellung im Kurscomputer pruefen

**Behebung:**
- I-Gain reduzieren
- Ruderlimit auf 15–20 Grad begrenzen
- Bootstyp korrekt einstellen (insbesondere Kielttyp: Langkiel vs. Kurzkiel)
- Lernfahrt wiederholen

**AYDI-Relevanz:** Confidence: documented. Modul: Ergonomics, Safety.

### 7.5 Fehlerbild F05 — Kein Antrieb (Drive Not Responding)

**Symptom:** Kurscomputer zeigt Sollkurs und Stellsignal, aber die Antriebseinheit reagiert nicht. Keine hoerbare Motoraktivitaet. Alarmmeldung "Drive Not Responding" oder "No Drive".

**Ursache:**
- Sicherung der Antriebseinheit durchgebrannt
- Kabelverbindung zwischen Kurscomputer und Antrieb unterbrochen
- Antriebseinheit defekt (Motor, Steuerplatine)
- NMEA2000-Verbindung unterbrochen (bei netzwerkbasiertem Antrieb)
- Kupplung permanent ausgekuppelt (bei manueller Uebersteuerung haengengeblieben)

**Diagnose:**
1. Sicherung pruefen (Leistungskabel Antrieb → Batterie)
2. Spannung am Antrieb messen (12V/24V vorhanden?)
3. NMEA2000-Netzwerk pruefen: Kurscomputer sieht Antrieb?
4. Manueller Kupplung-Status pruefen

**Behebung:**
- Sicherung tauschen (Ursache fuer Durchbrennen suchen!)
- Kabelverbindungen pruefen und ggf. erneuern
- NMEA2000-Steckverbindungen reinigen und sichern
- Motor/Steuerplatine tauschen (Werkstatt)

**AYDI-Relevanz:** Confidence: measured (elektrisch messbar). Modul: Safety, Compliance.

### 7.6 Fehlerbild F06 — Ruderfeedback-Fehler

**Symptom:** Autopilot zeigt Fehlermeldung "Rudder Feedback Error" oder "RF Fault". Ruderanzeige zeigt unrealistische Werte (z.B. 90 Grad) oder springt. Autopilot schaltet sich ab oder steuert unkontrolliert.

**Ursache:**
- Potentiometer-Schleifer verschlissen oder korrodiert
- Mechanische Verbindung zum Ruderfeedback-Sensor gebrochen oder locker
- Kabelbruch oder Kurzschluss in der Sensorleitung
- Wasser im Sensorgehaeuese
- Sensor ausserhalb des kalibrierten Bereichs (Ruder weiter ausgelenkt als kalibriert)

**Diagnose:**
1. Ruderfeedback-Wert auf Bedieneinheit ablesen: springt er, zeigt er konstant falschen Wert?
2. Mechanische Verbindung Sensor ↔ Ruderschaft pruefen
3. Sensor-Widerstand messen (Potentiometer: typisch 5 kOhm, sollte linear ueber Bereich variieren)
4. Kabel auf Bruch und Isolation pruefen

**Behebung:**
- Potentiometer tauschen (Verschleissteil)
- Mechanische Verbindung reparieren (spielfrei!)
- Kabel erneuern
- Sensor-Gehaeuse abdichten
- Nach Austausch: vollstaendige Neukalibrierung

**AYDI-Relevanz:** Confidence: measured. Modul: Safety (kritisch — ohne Feedback steuert AP blind).

### 7.7 Fehlerbild F07 — Ueberhitzung Antriebseinheit

**Symptom:** Autopilot schaltet sich nach laengerer Nutzung ab. Fehlermeldung "Drive Overtemp" oder "Thermal Shutdown". Antriebsgehaeuse fuehlt sich heiss an (>70 Grad C). Nach Abkuehlung funktioniert der Autopilot wieder.

**Ursache:**
- Unterdimensionierter Antrieb fuer das Boot (Dauerlast zu hoch)
- Schwergaengige Steueranlage (Ruderlager, Dichtungen) erhoehen die Antriebslast
- Schlechter Segeltrimm (permanente Lee- oder Luvgierigkeit erzwingt Dauer-Ruderausschlag)
- Unzureichende Belueftung des Antriebsraums
- Seegang und starker Wind (hohe Regellast ueber laengere Zeit)

**Diagnose:**
1. Bootsgroesse und Verdraengung mit Antriebsspezifikation vergleichen
2. Ruder von Hand bewegen: ist die Steueranlage leichtgaengig?
3. Helmbalance pruefen: segelt das Boot neutral oder mit starker Gierigkeit?
4. Durchschnittsverbrauch des Antriebs messen (wenn > 60% des Nennstroms: ueberlastet)

**Behebung:**
- Naechstgroesseren Antrieb installieren
- Steueranlage gangbar machen (Ruderlager schmieren, Seile prufen, Hydraulik entlueften)
- Segeltrimm verbessern (Mast-Rake, Vorstagspannung, Segelbalance)
- Belueftung des Antriebsraums verbessern
- Deadband vergroessern (weniger Ruderaktivitaet)

**AYDI-Relevanz:** Confidence: estimated (aus Nutzungsdaten ableitbar). Modul: Structural, Ergonomics.

### 7.8 Fehlerbild F08 — Langsamer Antrieb

**Symptom:** Autopilot reagiert traege, Ruderbewegung deutlich langsamer als normal. Boot kann Kurs bei Boen oder Seegang nicht halten. Antriebsgeraeusch klingt "muede" oder "gedehnt".

**Ursache:**
- Niedrige Bordspannung (Batterie schwach)
- Getriebe verschlissen oder schwergaengig (Schmierung fehlt)
- Bei Hydraulik: Luft im System, niedriger Fluessigkeitsstand, Leckage
- Bei Linearantrieb: Spindelverschleiss
- Mechanische Hemmung in der Steueranlage

**Diagnose:**
1. Bordspannung unter Last messen (12V: mind. 11,5V, 24V: mind. 23,0V)
2. Antriebsgeschwindigkeit messen: Ruder von BB-Anschlag nach StB-Anschlag → Zeit vergleichen mit Sollwert
3. Hydraulik: Fluessigkeitsstand und Farbe pruefen, auf Leckage untersuchen
4. Ruder von Hand bewegen: leichtgaengig?

**Behebung:**
- Batterien laden oder tauschen
- Getriebe schmieren oder tauschen
- Hydraulik entlueften, Fluid nachfuellen, Leckage beheben
- Steueranlage gangbar machen

**AYDI-Relevanz:** Confidence: measured (Geschwindigkeit messbar). Modul: Safety.

### 7.9 Fehlerbild F09 — Falscher Wind-Modus

**Symptom:** Im Wind-Modus steuert der Autopilot nicht den erwarteten Windwinkel. Boot dreht nach Aktivierung des Wind-Modus stark ab oder luft an. Windwinkel-Anzeige auf Autopilot stimmt nicht mit Windanzeige ueberein.

**Ursache:**
- Windsensor nicht kalibriert (Offset)
- Windsensor-Kabel vertauscht (Backbord/Steuerbord invertiert)
- Falscher Wind-Referenzwert: Apparent vs. True Wind
- Windsensor durch Windschatten des Segels gestoert (an Deck statt Mastspitze)
- NMEA2000-Winddaten kommen von falschem Geraet (zwei Windsensoren im Netzwerk)

**Diagnose:**
1. Windanzeige mit tatsaechlicher Windrichtung vergleichen (Verklicker, Wolken)
2. Wind-Offset auf Windsensor pruefen (Soll: Bug = 0 Grad)
3. NMEA2000-Geraetliste: nur ein Windsensor als Quelle?
4. Bei Mastverlust: Notfall-Windmessung nicht moeglich → Heading-Hold verwenden

**Behebung:**
- Windsensor-Offset kalibrieren (Boot in bekanntem Wind ausrichten)
- Kabelanschluss pruefen (BB/StB-Vertauschung)
- Windsensor an Mastspitze montieren (ungestoert)
- Quelle im NMEA2000-Netzwerk korrekt zuweisen

**AYDI-Relevanz:** Confidence: documented. Modul: Ergonomics, Safety.

### 7.10 Fehlerbild F10 — Track-Modus Fehlnavigation

**Symptom:** Im Track-Modus (GPS-Routensteuerung) faehrt das Boot nicht auf der gewuenschten Route. Staendige Kursaenderungen, Zickzack-Kurs, oder Boot dreht im Kreis. XTE (Cross-Track-Error) wird nicht reduziert.

**Ursache:**
- Keine oder ungenaue GPS-Position (Signalverlust, HDOP hoch)
- Wegpunkt-Reihenfolge im Kartenplotter falsch
- NMEA2000-Verbindung zwischen Plotter und Kurscomputer gestoert
- XTE-Gain im Kurscomputer zu hoch oder zu niedrig
- Stroemung oder Wind staerker als der Autopilot kompensieren kann

**Diagnose:**
1. GPS-Position und HDOP pruefen (HDOP sollte <3 sein)
2. Route auf Kartenplotter ueberpruefen (Wegpunkte korrekt?)
3. NMEA2000-Daten am Kurscomputer: empfaengt er XTE und Bearing?
4. XTE-Wert auf Kurscomputer ablesen und mit Plotter vergleichen

**Behebung:**
- GPS-Antenne pruefen (freie Sicht, kein Abschatten)
- Route korrigieren
- NMEA2000-Verbindung pruefen
- XTE-Gain anpassen (Standard-Wert als Ausgangspunkt)
- Bei starker Stroemung: manuell korrigieren oder NoDrift-Modus verwenden

**AYDI-Relevanz:** Confidence: documented. Modul: Compliance (IEC 62065), Safety.

### 7.11 Fehlerbild F11 — Hydraulik-Leckage

**Symptom:** Hydraulikoelflecken unter dem Autopilot-Antrieb oder an Leitungsverbindungen. Fluessigkeitsstand im Reservoir sinkt. Antrieb wird langsamer oder verliert Kraft. Oeliger Geruch im Maschinenraum.

**Ursache:**
- Verschlissene Zylinderdichtungen (O-Ringe, Wellendichtungen)
- Schlauchverbindungen undicht (lose Verschraubungen, poroese Schlaeuche)
- Riss in Hydraulikleitung (Vibration, Scheuerung, UV-Schaedigung)
- Korrosion an Hydraulik-Fittings
- Ueberdruck durch thermische Ausdehnung (gesperrtes System in der Sonne)

**Diagnose:**
1. Leckstelle lokalisieren: Papier unter Verbindungen legen, nach Stunden pruefen
2. Fluessigkeitsstand pruefen und mit letztem Wartungstermin vergleichen
3. Schlaeuche auf Risse, Quellungen, Schreuerstellen pruefen
4. Verschraubungen auf Festigkeit pruefen (Drehmoment)
5. Systemdruck messen (wenn moeglich)

**Behebung:**
- Dichtungen tauschen (O-Ringe, Wellendichtung)
- Schlaeuche und Fittings tauschen (alle gleichzeitig bei hohem Alter)
- Fluessigkeit nachfuellen (richtige Spezifikation!)
- System entlueften
- Ueberdruckventil pruefen (thermische Ausdehnung)

**AYDI-Relevanz:** Confidence: visual_high (Oelflecken gut sichtbar). Modul: Structural, Safety.

### 7.12 Fehlerbild F12 — Stromversorgungsprobleme

**Symptom:** Autopilot schaltet sich unter Last ab (Fehlermeldung "Low Voltage"). Antrieb "stottert" bei Boen. Display flackert oder wird dunkel. Autopilot startet nicht.

**Ursache:**
- Batterie zu schwach (Kapazitaet erschoepft, hoher Innenwiderstand)
- Kabelquerschnitt zu duenn (Spannungsabfall unter Last)
- Korrodierte Kabelschuhe oder Klemmen (Uebergangswiderstand)
- Sicherung zu klein oder korrodiert
- Masseverbindung schlecht (hohes Massepotential)

**Diagnose:**
1. Spannung direkt an der Antriebseinheit messen (unter Last!)
2. Spannungsabfall Batterie → Antrieb messen (sollte <0,5 V sein)
3. Kabelquerschnitt gegen Tabelle pruefen (siehe 6.6)
4. Kabelschuhe und Klemmen auf Korrosion pruefen
5. Masseverbindung pruefen (Widerstand <0,01 Ohm)

**Behebung:**
- Batteriekapazitaet erhoehen oder Batterie tauschen
- Kabelquerschnitt vergroessern (direkte Leitung Batterie → Antrieb)
- Alle Kabelschuhe reinigen, mit Schrumpfschlauch und Kontaktfett schuetzen
- Sicherung gegen korrekt dimensionierte tauschen
- Dedizierte Masseleitung zum Antrieb legen

**AYDI-Relevanz:** Confidence: measured (elektrisch messbar). Modul: Structural, Cost.

---

## 8. Troubleshooting

### 8.1 Entscheidungsbaum T01 — Autopilot steuert ungenau

```
Autopilot steuert ungenau (>5 Grad Abweichung)
  |
  +-- Abweichung richtungsabhaengig? (verschieden auf N/O/S/W)
  |     |
  |     +-- JA → Kompassfehler (F01)
  |     |     +-- Kalibrierung durchfuehren
  |     |     +-- Stoerquellen pruefen
  |     |
  |     +-- NEIN → Weiter
  |
  +-- Ruder bewegt sich, aber zu viel/zu wenig?
  |     |
  |     +-- Zu viel (Pendeln) → Hunting (F03)
  |     |     +-- P-Gain reduzieren, D-Gain erhoehen
  |     |
  |     +-- Zu wenig (traege) → Langsamer Antrieb (F08)
  |     |     +-- Bordspannung pruefen
  |     |     +-- Antriebsgeschwindigkeit messen
  |     |
  |     +-- Ueberschiessen → Overshoot (F04)
  |           +-- I-Gain reduzieren
  |           +-- Ruderlimit pruefen
  |
  +-- Ruder bewegt sich nicht → F05 (Kein Antrieb)
```

### 8.2 Entscheidungsbaum T02 — Autopilot faellt aus

```
Autopilot faellt waehrend der Fahrt aus
  |
  +-- Display/Bedieneinheit aus?
  |     |
  |     +-- JA → Stromversorgung pruefen (F12)
  |     |     +-- Sicherung, Batterie, Kabel
  |     |
  |     +-- NEIN → Fehlermeldung auf Display?
  |           |
  |           +-- "Drive Not Responding" → F05
  |           +-- "Rudder Feedback Error" → F06
  |           +-- "Low Voltage" → F12
  |           +-- "Drive Overtemp" → F07
  |           +-- "Compass Error" → F01
  |           +-- "No Data" → NMEA2000-Bus pruefen
  |
  +-- Kein Fehler, aber Autopilot schaltet auf Standby?
        |
        +-- Shadow Drive aktiv? → Manuelles Steuern erkannt
        +-- MOB-Taste gedrueckt? → Unbeabsichtigte Aktivierung
        +-- Automatische Abschaltung durch Plotter? → Route beendet
```

### 8.3 Entscheidungsbaum T03 — Hydraulik-Probleme

```
Hydraulischer Autopilot-Antrieb Probleme
  |
  +-- Oelflecken sichtbar? → F11 (Leckage)
  |     +-- Leckstelle lokalisieren
  |     +-- Dichtungen/Schlaeuche tauschen
  |
  +-- Antrieb langsam? → Luft im System?
  |     |
  |     +-- JA (Geraeusch: "fauchendes" Geraeusch) → Entlueften
  |     |
  |     +-- NEIN → Fluessigkeitsstand OK?
  |           |
  |           +-- Niedrig → Nachfuellen, Leck suchen
  |           +-- OK → Pumpe defekt? Ventil defekt?
  |                     +-- Werkstatt
  |
  +-- Kein Antrieb, aber Pumpe laeuft hoerbar?
        |
        +-- Bypass-Ventil offen? → Schliessen
        +-- Zylinder-Kolben defekt? → Werkstatt
```

### 8.4 Entscheidungsbaum T04 — Wind-Modus Probleme

```
Wind-Modus funktioniert nicht korrekt
  |
  +-- Kein Wind-Modus verfuegbar?
  |     +-- Windsensor angeschlossen? → Netzwerk pruefen
  |     +-- Windsensor als Quelle konfiguriert? → Einstellungen
  |
  +-- Wind-Modus verfuegbar, aber falscher Winkel?
  |     +-- Windsensor-Offset kalibriert? → Kalibrieren
  |     +-- BB/StB vertauscht? → Kabelanschluss pruefen
  |     +-- Windschatten durch Segel? → Mastspitze montieren
  |
  +-- Wind-Modus instabil (Oszillation)?
        +-- Deadband zu eng? → Vergroessern
        +-- Wind boeeig? → Daempfung erhoehen
        +-- AWA vs TWA Modus pruefen
```

### 8.5 Entscheidungsbaum T05 — NMEA2000-Netzwerk

```
NMEA2000-Kommunikationsprobleme
  |
  +-- Kurscomputer sieht keine Geraete?
  |     +-- Terminator an beiden Enden? → Installieren
  |     +-- Backbone-Spannung vorhanden? → 12V messen
  |     +-- Stecker korrekt? → Alle Verbindungen pruefen
  |
  +-- Einzelnes Geraet wird nicht erkannt?
  |     +-- Stichleitungs-Laenge >6 m? → Kuerzen
  |     +-- Stecker korrodiert? → Reinigen/Tauschen
  |     +-- Geraet defekt? → An anderem T-Stueck testen
  |
  +-- Intermittierende Ausfaelle?
        +-- Korrodierte Stecker? → Reinigen, Kontaktfett
        +-- Zu viele Geraete? (>50 auf einem Segment) → Aufteilung
        +-- EMV-Stoerung? → Kabel weg von Motorkabeln verlegen
```

### 8.6 Wartungsentscheidungsbaum

```
Regelmaessige Wartungspruefung (jaehrlich)
  |
  +-- Bordspannung unter Last OK? (>11.5V bei 12V)
  |     |
  |     +-- NEIN → Batterie/Ladung pruefen
  |     +-- JA → Weiter
  |
  +-- Kompass-Deviation <3 Grad auf allen Kursen?
  |     |
  |     +-- NEIN → Schwenkfahrt (Kalibrierung) durchfuehren
  |     |     +-- Deviation immer noch >3 Grad → Stoerquellen suchen/Sensor versetzen
  |     +-- JA → Weiter
  |
  +-- Ruderfeedback-Anzeige stimmt mit Ruderlage ueberein?
  |     |
  |     +-- NEIN → Feedback neu kalibrieren
  |     |     +-- Immer noch abweichend → Sensor pruefen/tauschen
  |     +-- JA → Weiter
  |
  +-- Antriebsgeschwindigkeit normal? (BB→StB Vollanschlag in Sollzeit)
  |     |
  |     +-- Langsamer als Soll → Schmierung, Bordspannung, Getriebe pruefen
  |     +-- Normal → Weiter
  |
  +-- Hydraulikfluid (falls zutreffend):
  |     |
  |     +-- Fuellstand niedrig → Nachfuellen, Leck suchen
  |     +-- Farbe trueb/dunkel → Fluid wechseln
  |     +-- Klar und Fuellstand OK → Weiter
  |
  +-- Alle NMEA2000-Geraete sichtbar im Netzwerk?
  |     |
  |     +-- NEIN → Stecker, Stichleitungen, Terminatoren pruefen
  |     +-- JA → Weiter
  |
  +-- Alle Modi funktionieren (Auto, Wind, Track)?
        |
        +-- NEIN → Fehlersuche nach Modus
        +-- JA → System OK, keine Massnahme erforderlich
```

### 8.7 Notfall-Prozeduren

**Autopilot-Totalausfall auf See:**

```
1. SOFORT: Manuell uebernehmen
   - Pinne/Steuerrad ergreifen
   - Kupplung/Bypass sicherstellen (manuelles Steuern moeglich?)
   
2. WENN Ruder blockiert (keine Kupplung, kein Bypass):
   - Notpinne aufstecken (falls moeglich)
   - Sicherungsbolzen/Notentriegelung am Antrieb suchen
   - Im aeussersten Fall: Antrieb mechanisch vom Quadranten trennen
   
3. Ursache eingrenzen:
   - Keine Anzeige → Stromversorgung (Sicherung, Batterie)
   - Anzeige aber kein Antrieb → Antrieb (Sicherung Antrieb, Motor)
   - Alles funktioniert aber Kurs falsch → Kompass/Sensor
   
4. Backup-System aktivieren:
   - Tiller-Pilot als Backup (falls vorhanden)
   - Windsteueranlage einsetzen (falls vorhanden und Wind genuegend)
   
5. WENN kein Backup und Alleinfahrt:
   - Segel ausbalancieren (Beidrehen oder balancierter Kurs)
   - Notfall-Pinnenleine (Leine an Pinne, belegt an Klampe)
   - Ggf. unter Motor fahren und Crew-Abloesungen organisieren
```

**Unkontrollierter Autopilot (dreht Kreise, Kurs falsch):**
```
1. SOFORT: Standby-Taste druecken
2. WENN Standby nicht reagiert: Sicherung ziehen
3. Manuell uebernehmen
4. Ursache pruefen (Kompass, Feedback, Kurscomputer)
```

---

## 9. FAQ — Haeufig gestellte Fragen

### FAQ-01: Welchen Autopiloten brauche ich fuer meine Yacht?

**Antwort:** Die Wahl haengt von vier Faktoren ab:

1. **Boottyp:** Segel oder Motor? Pinne oder Rad? Hydraulische oder mechanische Steuerung?
2. **Groesse/Verdraengung:** Entscheidend fuer die Antriebsklasse (siehe Dimensionierungstabelle in 5.7)
3. **Einsatzgebiet:** Kuestenfahrt, Offshore, Blauwasser — bestimmt den Sicherheitsfaktor
4. **Budget:** Tiller-Pilot ab EUR 500, Unterdeck-System ab EUR 2.500, Hydraulik ab EUR 5.000

**Daumenregel:** Verdraengung (segelfertig, voll beladen) bestimmt die Antriebsgroesse. Eine Klasse groesser waehlen fuer Blauwasser und Offshore.

### FAQ-02: Tiller-Pilot oder Unterdeck-System?

**Antwort:** Tiller-Pilot fuer Pinnenboote bis ca. 10 m und 5 Tonnen, die primaer im Kuestenbereich segeln. Unterdeck-System fuer alles darueber oder wenn hoehere Zuverlaessigkeit erforderlich ist. Ein Tiller-Pilot als Backup zusaetzlich zum Unterdeck-System ist eine beliebte Langfahrt-Konfiguration.

### FAQ-03: Wie viel Strom verbraucht ein Autopilot?

**Antwort:** Typischer 24h-Verbrauch bei moderatem Segeln (12V):
- Tiller-Pilot (8 m Boot): 15–30 Ah
- Linearantrieb (12 m Boot): 30–60 Ah
- Linearantrieb (15 m Boot): 50–100 Ah
- Hydraulik (18 m Boot): 80–160 Ah

Bei rauem Seegang: 2–3x mehr. Bei gutem Segeltrimm und leichtem Wind: bis 50 % weniger. Der Autopilot ist oft der groesste Einzelverbraucher an Bord einer Fahrtenyacht.

### FAQ-04: Muss ich den Kompass kalibrieren?

**Antwort:** Ja, bei jedem neuen System, nach Sensor-Versetzung und bei veraenderter magnetischer Umgebung. Raymarine Evolution behauptet "kalibrierungsfrei", aber eine Schwenkfahrt wird auch dort empfohlen fuer optimale Ergebnisse. Kalibrierung: 2 langsame 360-Grad-Drehungen bei ruhigem Wasser, konstanter Geschwindigkeit, ohne elektrische Stoerquellen in der Naehe.

### FAQ-05: Kann ich Raymarine-Antrieb mit Simrad-Computer verwenden?

**Antwort:** Nein, grundsaetzlich nicht empfohlen. Antriebseinheiten kommunizieren ueber herstellerspezifische Protokolle mit ihren Kurscomputern. Verwenden Sie Kurscomputer und Antrieb vom gleichen Hersteller. Sensoren (GPS, Wind, Kompass) koennen herstelleruebergreifend ueber NMEA2000 genutzt werden.

### FAQ-06: Was ist Shadow Drive?

**Antwort:** Shadow Drive (Garmin) und aehnliche Funktionen (Simrad) erkennen automatisch, wenn der Steuermann manuell am Steuerrad dreht. Der Autopilot schaltet dann automatisch in Standby, ohne dass eine Taste gedrueckt werden muss. Beim Loslassen des Rades uebernimmt der Autopilot den aktuellen Kurs. Funktioniert nur bei Hydraulik-Systemen, da hier der Druckunterschied zwischen AP-Pumpe und Helm-Pumpe erkannt wird.

### FAQ-07: Autopilot oder Windsteueranlage fuer die Weltumseglung?

**Antwort:** Idealerweise beides. Windsteueranlage (z.B. Monitor, Windpilot, Hydrovane) fuer Amwind- und Raumschotkurse im Passat (stromsparend, mechanisch zuverlaessig). Elektrischer Autopilot fuer Flaute, Motorfahrt, Vorwindkurse bei leichtem Wind, Wegpunktnavigation und Hafenannaherung. Budget fuer beides: ca. EUR 8.000–15.000.

### FAQ-08: Wie laut ist ein Autopilot?

**Antwort:**
- Tiller-Pilot: deutlich hoerbar im Cockpit (50–60 dB), stoerend beim Schlafen in der Achterkajuete
- Linearantrieb unter Deck: hoerbar, aber gedaempft (40–50 dB in der Kabine)
- Hydraulik mit schallgedaemmter Pumpe: am leisesten (30–40 dB)
- NKE Gyropilot mit Jefa-Antrieb: besonders leise durch optimale Regelung (weniger Ruderbewegungen)

### FAQ-09: Kann ich einen Autopilot selbst einbauen?

**Antwort:** Tiller-Pilot: ja, problemlos (Plug & Play). Wheel-Pilot: ja, mit Grundkenntnissen. Unterdeck-Linearantrieb: ja, wenn Sie handwerklich geschickt sind und die Montageanleitung befolgen (4–8 Stunden). Hydraulik-Systeme: nur mit Erfahrung oder durch Fachbetrieb (Leckagegefahr, Entlueftung kritisch). In jedem Fall: Seetestfahrt und Feinabstimmung nach Installation.

### FAQ-10: Was kostet ein Autopilot-System komplett?

**Antwort:**

| Bootklasse | System | Komplett inkl. Installation | Bemerkung |
|------------|--------|---------------------------|-----------|
| 8 m Segel, Pinne | Tiller-Pilot | EUR 800–1.500 | Selbsteinbau |
| 10 m Segel, Rad | Wheel-Pilot | EUR 1.800–3.000 | Selbsteinbau |
| 12 m Segel | Linear unter Deck | EUR 3.500–5.500 | + EUR 500–1.000 Installation |
| 15 m Segel | Linear unter Deck | EUR 5.000–8.000 | + EUR 800–1.500 Installation |
| 18 m Segel | Hydraulik | EUR 8.000–14.000 | + EUR 1.500–3.000 Installation |
| 22 m Motor | Hydraulik | EUR 10.000–20.000 | + EUR 2.000–5.000 Installation |

### FAQ-11: Wie oft muss ein Autopilot gewartet werden?

**Antwort:**
- **Jaehrlich:** Kabelverbindungen pruefen, Ruderfeedback-Kalibrierung verifizieren, Software-Update
- **Alle 2 Jahre:** Antriebsmechanik schmieren, Kupplung pruefen, Hydraulikfluid-Stand und -Farbe pruefen
- **Alle 5 Jahre:** Potentiometer-Feedback tauschen (verschleissbehaftet), Hydraulikschlaeuche pruefen
- **Bei Bedarf:** Kompass-Kalibrierung nach Aenderungen, Sicherungen nach Ausloesung, Dichtungen bei Leckage

### FAQ-12: Was bedeutet "Response Level" oder "Gain"?

**Antwort:** Response Level (Raymarine) oder Gain/Rudder-Gain (Simrad, B&G) steuert, wie aggressiv der Autopilot auf Kursabweichungen reagiert. Hohes Level: schnelle, praezise Kurssteuerung, aber mehr Ruderbewegungen, mehr Strom, mehr Verschleiss. Niedriges Level: ruhigere Steuerung, weniger Strom, aber Boot wandert etwas mehr um den Sollkurs. Empfehlung: so niedrig wie fuer die Bedingungen akzeptabel.

### FAQ-13: Kann der Autopilot das Boot bei schwerem Wetter steuern?

**Antwort:** Grundsaetzlich ja, aber mit Einschraenkungen. Bei >35 Knoten Wind und entsprechendem Seegang kommen viele Autopiloten an ihre Grenzen (Ruderkraefte, Regelgeschwindigkeit, Stromverbrauch). Massnahmen: Segel verkleinern (weniger Ruderkraefte), Deadband vergroessern, ggf. Hansteuerung uebernehmen. NKE Gyropilot und B&G H5000 haben spezielle Schwerwetter-Algorithmen (Anti-Broaching).

### FAQ-14: Was ist der Unterschied zwischen AWA und TWA Steering?

**Antwort:** AWA (Apparent Wind Angle): Autopilot haelt den Scheinwindwinkel konstant — einfach, schnell, aber der wahre Kurs wandert mit Bootgeschwindigkeitsaenderungen. TWA (True Wind Angle): Autopilot haelt den wahren Windwinkel konstant — genauer fuer den tatsaechlichen Segelkurs, erfordert aber Log-Geschwindigkeit und aufwaendigere Berechnung. TWA ist nur bei B&G (H5000), NKE und einigen Furuno-Systemen verfuegbar.

### FAQ-15: Brauche ich einen separaten Heading-Sensor?

**Antwort:** Viele Kurscomputer haben einen integrierten Sensor (z.B. Raymarine ACU mit EV-1). Ein separater Heading-Sensor (z.B. Precision-9, EV-1 extern) verbessert die Genauigkeit, da er an einem stoerungsarmen Ort montiert werden kann. Bei Simrad/B&G NAC-Computern ist der Precision-9 immer separat (nicht integriert). Empfehlung: Sensor immer so weit wie moeglich von Stoerquellen montieren.

### FAQ-16: Mein Boot hat Doppelruder. Wie funktioniert der Autopilot?

**Antwort:** Bei Doppelruder-Anlagen (typisch bei Katamaranen und einigen modernen Segelyachten) gibt es zwei Optionen:
1. **Mechanische Kopplung:** Beide Ruder werden ueber einen Querlenker (Tie Bar) verbunden. Ein Antrieb steuert beide Ruder.
2. **Doppelantrieb:** Jedes Ruder hat einen eigenen Antrieb. Erfordert einen Kurscomputer, der zwei Antriebe synchron ansteuert (Simrad NAC-3, B&G NAC-3).

### FAQ-17: Kann ich den Autopilot mit meinem iPad/Smartphone steuern?

**Antwort:** Ja, bei den meisten modernen Systemen:
- Raymarine: ueber Axiom MFD mit RayRemote App (WiFi)
- Simrad: ueber NSX MFD mit Simrad App
- B&G: ueber Zeus mit B&G App
- Garmin: ueber GPSMAP mit ActiveCaptain App + quatix Smartwatch
- Einschraenkung: App-Steuerung ist nur als Ergaenzung gedacht, nicht als primaere Bedieneinheit (Zuverlaessigkeit, Latenz)

### FAQ-18: Was passiert bei Stromausfall?

**Antwort:** Der Autopilot faellt aus. Das Ruder:
- Bei selbsthemmendem Linearantrieb ohne Kupplung: bleibt in letzter Position (Notfall: manuell auskuppeln)
- Bei Linearantrieb mit Kupplung: Kupplung loest aus, manuelles Steuern moeglich
- Bei Hydraulik mit Bypass: Bypass-Ventil oeffnen, manuelles Steuern moeglich
- Bei Hydraulik ohne Bypass: Ruder blockiert (Konstruktionsfehler, sollte nicht vorkommen!)

**Empfehlung:** Immer eine manuelle Auskuppelmoeglichkeit vorsehen. Bei Blauwasserfahrt: Notpinne bereithalten.

### FAQ-19: Wie genau ist ein moderner Autopilot?

**Antwort:** Unter guten Bedingungen (moderater Wind, wenig Seegang):
- Heading-Hold: +-1 bis +-3 Grad (Durchschnitt)
- Wind-Modus: +-2 bis +-5 Grad Windwinkel
- Track-Modus: +-10 bis +-30 m Cross-Track-Error

Bei schwerem Wetter: Genauigkeit sinkt erheblich. NKE Gyropilot erreicht +-1 Grad auch bei moderatem Seegang. Raymarine Evolution und Simrad Continuum typisch +-2 Grad bei Seegang.

### FAQ-20: Kann ich den Autopilot fuer Regatten verwenden?

**Antwort:** Regeln beachten! ORC und viele andere Rennklassen verbieten Autopiloten. Ausnahmen:
- Einhand- und Kurzhand-Regatten (Mini Transat, OSTAR, Route du Rhum): Autopilot erlaubt und unverzichtbar
- Langstrecken-Regatta (ARC, World ARC): oft erlaubt
- Bei erlaubter Nutzung: NKE Gyropilot oder B&G H5000 sind die Regatta-Standards

### FAQ-21: Wie installiere ich einen Ruderfeedback-Sensor?

**Antwort:** Der Ruderfeedback-Sensor muss eine spielfreie mechanische Verbindung zum Ruderschaft oder Quadranten haben:
1. Sensorarm am Quadrant/Tillerarm befestigen (mitdrehend)
2. Sensorkoerper fest am Rumpf befestigen (drehfest)
3. Kabel zum Kurscomputer verlegen
4. Kalibrierung: Ruder Mittschiffs → Null setzen, dann BB-Vollanschlag, dann StB-Vollanschlag
5. Pruefung: Ruder von Hand bewegen, Anzeige vergleichen

### FAQ-22: Mein Autopilot "piept" staendig. Was bedeutet das?

**Antwort:** Alarme haben verschiedene Ursachen:
- 1x kurz: Kursaenderung akzeptiert
- Kontinuierlich: Kursabweichung >15 Grad (off-course alarm)
- Schnelle Folge: Drive-Fehler oder Feedback-Fehler
- Einzeltone alle 30s: niedrige Bordspannung
- Pruefen Sie die Alarmmeldung auf dem Display. Im Zweifelsfall: Autopilot in Standby und manuell uebernehmen.

### FAQ-23: Kann ich zwei Autopiloten als Redundanz installieren?

**Antwort:** Ja, und das ist fuer Blauwasserfahrt empfehlenswert. Typische Konfigurationen:
1. **Primaer Unterdeck + Backup Tiller-Pilot:** Guenstigste Variante, Tiller-Pilot als Notfall
2. **Zwei identische Systeme:** Teurer, aber volle Redundanz. Nur ein Antrieb aktiv, der zweite als Reserve
3. **Autopilot + Windsteueranlage:** Unterschiedliche Technologien (elektrisch + mechanisch) fuer maximale Zuverlaessigkeit

### FAQ-24: Was ist ein "Sea Trial" beim Autopilot?

**Antwort:** Der Sea Trial ist die Ersteinstellung des Autopiloten auf dem Wasser. Ablauf:
1. Boot auf offenes Wasser fahren (genug Platz fuer 360-Grad-Drehungen)
2. Kompass-Kalibrierung (Schwenkfahrt): 2 langsame Kreise
3. Autopilot-Lernfahrt (Autolearn/Sea Trial): Kurscomputer faehrt automatisch verschiedene Manoever
4. Feinabstimmung: Response Level, Ruderlimit, Deadband anpassen
5. Test aller Modi: Heading-Hold, Wind (falls Windsensor), Track (falls GPS-Route)
6. Dauer: ca. 30–60 Minuten

### FAQ-25: Mein altes SeaTalk1-System — kann ich es mit NMEA2000 verbinden?

**Antwort:** Ja, ueber Adapter:
- Raymarine SeaTalk1-zu-SeaTalkng-Konverter (E22158, ca. EUR 100)
- Actisense NMEA0183-zu-NMEA2000-Gateway (NGW-1, ca. EUR 200)
- Beachten: Alte SeaTalk1-Autopiloten (ST4000, ST6000) koennen nicht ueber NMEA2000 gesteuert werden, nur ihre Daten (Wind, Log, GPS) koennen konvertiert werden. Fuer Autopilot-Steuerung ueber NMEA2000 ist ein neuer Kurscomputer erforderlich.

---

## 10. Glossar

### A

**AHRS (Attitude and Heading Reference System):**
System zur Bestimmung von Lage (Roll, Pitch) und Richtung (Heading) eines Fahrzeugs. Moderne AHRS nutzen MEMS-Sensoren (9-Achsen) mit Kalman-Filter zur Datenfusion. Beispiel: Raymarine EV-1, Simrad Precision-9.

**ACU (Autopilot Control Unit):**
Raymarine-Bezeichnung fuer den Kurscomputer, der den Regelkreis berechnet und den Antrieb steuert. Modelle: ACU-100 bis ACU-400.

**Antriebseinheit (Drive Unit):**
Elektromechanische oder hydraulische Einheit, die das Ruder bewegt. Arten: Tiller-Pilot, Wheel-Pilot, Linear Drive, Rotary Drive, Hydraulic Pump.

**Apparent Wind Angle (AWA):**
Scheinbarer Windwinkel: der Winkel zwischen der Bootsmittellinie und der scheinbaren Windrichtung (Resultierende aus wahrem Wind und Fahrtwind). Wird vom Mastspitzen-Windsensor gemessen. Standardreferenz fuer den Wind-Modus der meisten Autopiloten.

**Anti-Broaching:**
Algorithmus in Regatta-Autopiloten (NKE, B&G H5000), der ein unkontrolliertes Aufrunden des Bootes bei Vorwindkursen im Seegang verhindert. Erkennt die Gierbeschleunigung frueh und setzt praediktiv Gegenruder.

### B

**Bypass-Ventil:**
Ventil in hydraulischen Steuer- und Autopilot-Systemen, das bei Oeffnung den Hydraulikkreislauf kurzschliesst und manuelles Steuern ohne Widerstand ermoeglicht. Essentiell fuer manuelle Uebersteuerung des Autopilots.

**Bang-Bang-Regler:**
Einfachster Reglertyp: Ruder wird entweder voll nach Backbord oder voll nach Steuerbord gesteuert (Ein/Aus). In fruehen Autopiloten (vor 1985) verwendet. Heute nur noch als Notfall-Modus.

### C

**CCU (Course Computer Unit):**
Garmin-Bezeichnung fuer den Kurscomputer. Enthalt Sensoren (MEMS) und Regellogik. Modelle: Reactor 40 Mech, Reactor 40 Hydraulik.

**CAN-Bus (Controller Area Network):**
Physische Schicht des NMEA2000-Netzwerks. 250 kbit/s, differenzielle Signale, max. 100 m Backbone.

**Cross-Track-Error (XTE):**
Seitenabweichung des Bootes von der geplanten Route (GPS-Route). Wird vom Kartenplotter berechnet und per NMEA2000 (PGN 129283) an den Autopilot gesendet. Grundlage fuer den Track-Modus.

**Continuum:**
Simrad-Markenname fuer die adaptive Autopilot-Regelung mit Seegangs-Erkennung und automatischer Parameter-Anpassung.

### D

**Deadband (Kursbreite / Totzone):**
Bereich um den Sollkurs, innerhalb dessen der Autopilot nicht reagiert. Typisch 1–5 Grad, einstellbar. Groesserer Deadband = weniger Ruderbewegungen, weniger Strom, aber groessere Kursschwankungen.

**Deviation (Ablenkung):**
Ablenkung der Kompassnadel durch Bordmagnetismus (Eisen, Motoren, Lautsprecher). Wird durch Kalibrierung (Schwenkfahrt) kompensiert. Restdeviation sollte <3 Grad sein.

**Drive Unit:**
Siehe Antriebseinheit.

### E

**EV-1 (Evolution Sensor):**
Raymarines 9-Achsen-MEMS-Sensorkern (Magnetometer + Beschleunigung + Gyroskop). Kompakt, leicht (ca. 100 g), integriert in ACU oder separat montierbar. Kernkomponente der Evolution-Plattform.

**Elektromagnetische Kupplung:**
Im Linearantrieb integrierte Kupplung, die bei Autopilot-Abschaltung oder Stromausfall automatisch loest und manuelles Steuern ermoeglicht.

### F

**Fluxgate-Kompass:**
Elektronischer Kompass auf Basis zweier Ferritkerne im Saettigungsbetrieb. Misst das Erdmagnetfeld richtungsabhaengig. Standard-Richtungssensor fuer Yachtautopiloten seit den 1980er Jahren.

**Feedback-Sensor:**
Siehe Ruderfeedback-Sensor.

### G

**Gain (Verstaerkung):**
Allgemeiner Begriff fuer die Regelverstaerkung des Autopiloten. Hoehere Gain = aggressivere Reaktion auf Kursabweichung. Untergliedert in P-Gain (proportional), I-Gain (integral), D-Gain (differential).

**Gierrate (Yaw Rate):**
Drehgeschwindigkeit des Bootes um die Hochachse, gemessen in Grad/Sekunde. Wird vom Ratenkreisel erfasst und ist der wichtigste Eingangsgroesse fuer den D-Anteil des PID-Reglers.

**Gyropilot:**
NKE-Markenname fuer deren Autopilot-Kurscomputer. Aktuelle Version: Gyropilot 3. Bekannt fuer exzellente Regelguete im Regatta-Einsatz.

### H

**Heading-Hold:**
Grundmodus jedes Autopiloten: haelt einen festen Kompasskurs. Auch: "Auto"-Modus, "Compass Mode".

**HDOP (Horizontal Dilution of Precision):**
Mass fuer die Genauigkeit der GPS-Position. Niedrigerer HDOP = bessere Genauigkeit. Fuer Autopilot-Track-Modus sollte HDOP <3 sein.

**Hunting:**
Unerwuenschtes Pendeln des Ruders um den Sollkurs. Ursachen: P-Gain zu hoch, D-Gain zu niedrig, Ruderfeedback-Fehler, Spiel in der Steueranlage.

**Hydrovane:**
Britisch-kanadischer Hersteller von Windfahnen-Selbststeueranlagen vom Typ Hilfsruder. Besonderheit: Hilfsruder dient gleichzeitig als Notruder.

### I

**ISO 25197:**
Internationale Norm fuer elektrische und elektronische Anlagen auf Sportbooten. Relevant fuer Autopilot-Installation (Kabelquerschnitte, Sicherungen, EMV).

**IEC 62065:**
Internationale Norm fuer Track-Control-Systeme auf Schiffen. Schreibt Sicherheitsmassnahmen vor (Warnung bei Kursaenderung >30 Grad, Bestaetigung bei Wegpunktuebergang).

### K

**Kalman-Filter:**
Mathematischer Algorithmus zur optimalen Schaetzung des Systemzustands aus verrauschten Sensordaten. In modernen AHRS-Systemen verwendet, um Magnetometer-, Beschleunigungs- und Gyroskop-Daten zu fusionieren.

**Kurscomputer (Course Computer):**
Zentraler Rechner des Autopilot-Systems. Empfaengt Sensordaten, berechnet den PID-Regler, steuert die Antriebseinheit. Auch: ACU (Raymarine), NAC (B&G/Simrad), CCU (Garmin), Gyropilot (NKE).

### L

**Linearer Hub (Stroke):**
Weg, den ein Linearantrieb zuruecklegen kann. Muss den vollen Ruderausschlag abdecken. Typisch: 150–381 mm.

### M

**MEMS (Micro-Electro-Mechanical Systems):**
Miniaturisierte mechanische Strukturen auf Halbleiterbasis. In Autopiloten als Magnetometer, Beschleunigungssensor und Gyroskop eingesetzt. Vorteile: kompakt, guenstig, keine beweglichen Teile. Nachteile: Drift, begrenzte Genauigkeit.

**Monitor (Scanmar Marine):**
US-amerikanischer Hersteller der Monitor Windvane, der verbreitetsten Pendelruder-Windsteueranlage fuer Blauwasser-Segelyachten.

### N

**NAC (Network Autopilot Computer):**
B&G/Simrad-Bezeichnung fuer den Kurscomputer. Modelle: NAC-1, NAC-2, NAC-3.

**NMEA2000:**
Standard-Datenbus fuer marine Elektronik (IEC 61162-3). CAN-Bus-basiert, 250 kbit/s. Alle modernen Autopiloten nutzen NMEA2000 fuer die Kommunikation.

**NoDrift-Modus:**
Autopilot-Modus, der einen Kompasskurs haelt, aber GPS-seitige Abdrift korrigiert. Kombination aus Heading-Hold und GPS-Korrektur.

### O

**Off-Course-Alarm:**
Alarm des Autopiloten, wenn die Kursabweichung einen einstellbaren Grenzwert ueberschreitet (typisch 10–15 Grad). Warnt den Steuermann, dass der Autopilot den Kurs nicht halten kann.

**Overshoot (Ueberschwingen):**
Das Boot schiesst bei Kursaenderung ueber den Sollkurs hinaus und pendelt sich erst nach einer oder mehreren Schwingungen ein. Ursache: I-Gain zu hoch, Ruderlimit zu hoch, Bootstyp falsch eingestellt.

### P

**PGN (Parameter Group Number):**
Numerische Kennung fuer einen Datentyp im NMEA2000-Netzwerk. Jeder PGN hat eine feste Struktur und Bedeutung (z.B. PGN 127250 = Vessel Heading).

**PID-Regler:**
Regelungsalgorithmus mit drei Anteilen: Proportional (reagiert auf aktuelle Abweichung), Integral (kompensiert bleibende Abweichung), Differential (daempft Aenderungen). Standard-Algorithmus in allen modernen Yachtautopiloten.

**Precision-9:**
Simrad/B&G-Bezeichnung fuer den 9-Achsen-AHRS-Heading-Sensor. Vergleichbar mit Raymarine EV-1, aber immer als separates Geraet.

**Pendelruder (Servo Pendulum):**
Windsteueranlagen-Typ: ein separates Ruder haengt pendelnd am Heck. Die Wasserstroemung am ausgelenkten Pendelruder erzeugt eine Seitenkraft, die ueber Steuerleinen auf das Hauptruder uebertragen wird. Kraefteverstaerkendes Prinzip.

### Q

**Quadrant:**
Halbkreisfoermiges oder segmentfoermiges Bauteil am Ruderschaft, an dem die Steuerseile oder der Autopilot-Linearantrieb angreifen. Material: Edelstahl, Bronze oder hochfester Kunststoff.

### R

**Ratenkreisel (Rate Gyro):**
Sensor zur Messung der Drehgeschwindigkeit (Gierrate) um die Hochachse. Liefert das D-Signal fuer den PID-Regler. In modernen Systemen als MEMS-Gyroskop integriert.

**Ruderfeedback-Sensor:**
Sensor, der die aktuelle Ruderposition misst und an den Kurscomputer meldet. Typen: Potentiometer (verschleissbehaftet), Hallsensor (kontaktlos), NMEA2000-Digitalsensor.

**Response Level:**
Raymarine-Bezeichnung fuer die Gesamteinstellung der Regelaggressivitaet (kombiniert P-, I-, D-Gain). Stufen 1–9, wobei 1 = am ruhigsten, 9 = am aggressivsten.

### S

**SeaTalk / SeaTalkng:**
Raymarine-proprietaerer Datenbus. SeaTalk1 (alt): 3-Draht, 4800 Baud. SeaTalkng (aktuell): physisch CAN-Bus / NMEA2000-kompatibel mit Raymarine-Steckern.

**Schwenkfahrt (Compass Calibration / Deviation Swing):**
Kalibrierfahrt fuer den elektronischen Kompass: 2 langsame 360-Grad-Drehungen bei konstanter Geschwindigkeit und ruhigem Wasser. Der Kurscomputer erfasst die Deviation auf allen Kursen und kompensiert sie.

**Shadow Drive:**
Garmin/Simrad-Funktion: Autopilot erkennt manuellen Steuereingriff und schaltet automatisch in Standby. Nur bei Hydraulik-Systemen.

**Stellgeschwindigkeit:**
Geschwindigkeit, mit der die Antriebseinheit das Ruder bewegen kann. Angegeben in mm/s (linear) oder Grad/s (rotary). Muss schnell genug sein, um auf Boen und Seegang zu reagieren.

### T

**Track-Modus:**
Autopilot-Modus, in dem das Boot einer GPS-Route folgt. Nutzt Cross-Track-Error (XTE) und Bearing-to-Waypoint vom Kartenplotter. Automatische Kurswechsel an Wegpunkten.

**True Wind Angle (TWA):**
Wahrer Windwinkel: der Winkel zwischen der Bootsmittellinie und der wahren Windrichtung (korrigiert um Bootgeschwindigkeit). Genauer als AWA fuer Segelkursbestimmung. TWA-Steering nur bei B&G H5000 und NKE verfuegbar.

**Trim Tab:**
Kleine Klappe am Heck eines Ruders. Bei Windsteueranlagen: Windfahne steuert den Trim Tab, der wiederum das Hauptruder auslenkt (Kraefteverstaerkung durch Wasserstroemung).

### V

**VMG (Velocity Made Good):**
Geschwindigkeitskomponente in Richtung des Ziels (Kreuzschlag: Hoehe zum Wind, Vorwind: Tiefe zum Wind). Einige Autopiloten (B&G H5000, NKE) koennen auf maximalen VMG steuern.

### W

**Windfahnen-Selbststeueranlage (Windvane Self-Steering):**
Mechanische Anlage, die ein Boot auf konstantem Kurs zum Scheinwind haelt. Nutzt Windenergie, keine Elektrizitaet. Typen: Hilfsruder, Pendelruder, Hilfsruder mit Trim Tab. Hersteller: Hydrovane, Monitor, Windpilot.

**Windpilot:**
Deutscher Hersteller (Peter Foerthmann, Hamburg) von Windfahnen-Selbststeueranlagen. Modelle: Pacific, Pacific Plus, Pacific Light.

### X

**XTE:**
Siehe Cross-Track-Error.

### Y

**Yaw (Gieren):**
Drehbewegung des Bootes um die Hochachse (vertikale Achse). Die primaere Stoergroesse, die der Autopilot kompensiert. Yaw-Rate wird vom Ratenkreisel gemessen und ist der entscheidende Eingangswert fuer den Differential-Anteil des PID-Reglers.

### Z

**Zylinder (Hydraulik):**
Hydraulikzylinder wandelt Fluiddruck in lineare Kraft um. Im Autopilot-Kontext: einfach- oder doppeltwirkende Zylinder, die am Ruderquadranten oder Tillerarm angreifen. Kolbendurchmesser und Hub bestimmen Kraft und Ruderausschlag.

### Weitere Begriffe

**Autolearn / Auto-Tuning:**
Automatische Lernfahrt, bei der der Kurscomputer die Bootscharakteristik (Traegheit, Daempfung, Rudereffekt) erlernt und die PID-Parameter optimiert. Typische Dauer: 5–15 Minuten auf offenem Wasser.

**Broaching:**
Unkontrolliertes Aufrunden einer Segelyacht bei Vorwindkursen im Seegang. Das Boot dreht ploetzlich in den Wind und kraengt stark. Anti-Broaching-Algorithmen in Regatta-Autopiloten (NKE, B&G H5000) erkennen die Gierbeschleunigung frueh und setzen praediktiv Gegenruder.

**Bearing to Waypoint (BTW):**
Peilung vom aktuellen Standort zum naechsten Wegpunkt. Wird vom Kartenplotter berechnet und per NMEA2000 (PGN 129284) an den Autopilot gesendet. Grundlage fuer den Track-Modus.

**COG (Course Over Ground):**
Kurs ueber Grund, berechnet aus der GPS-Positionsaenderung. Unterscheidet sich vom Heading (Kompasskurs) durch Strom und Abdrift. COG allein ist fuer Autopilot-Steuerung ungeeignet (zu traege, ungenau bei langsamer Fahrt).

**Dodge-Modus:**
Raymarine-spezifischer Modus: kurze, manuelle Kursaenderung (z.B. fuer AIS-Ausweichen), nach der der Autopilot automatisch zum urspruenglichen Kurs zurueckkehrt.

**Fantum Feedback:**
Furuno-spezifische Technologie: der NAVpilot 720 nutzt eine spezielle Rueckkopplungsmethode, die auch ohne physischen Ruderfeedback-Sensor ein praezises Ruder-Tracking ermoeglicht, indem der Motorstrom als Indikator fuer die Ruderposition verwendet wird.

**FOG (Fibre Optic Gyroscope):**
Faseroptischer Kreisel: Sagnac-Effekt in einer Glasfaserspule misst Drehgeschwindigkeiten mit sehr hoher Praezision. Im Superyacht- und Marineschiff-Segment eingesetzt, fuer Freizeityachten zu teuer (EUR 5.000+).

**Heave (Heben und Senken):**
Vertikale Auf- und Abbewegung des Bootes im Seegang. Heave-Sensor-Daten koennen den Autopilot-Algorithmus verbessern, indem sie Wellenbewegung von Kursaenderung unterscheiden.

**Kieltyp-Einstellung:**
Viele Autopiloten haben eine Einstellung fuer den Kieltyp (Langkiel, Kurzkiel, Flossenkiel). Der Kieltyp beeinflusst die Traegheit und das Steuerverhalten erheblich und muss korrekt eingestellt sein fuer optimale Regelung.

**Luvgierigkeit (Weather Helm):**
Tendenz einer Segelyacht, in den Wind zu drehen. Erfordert Dauer-Ruderausschlag nach Lee und belastet den Autopilot-Antrieb. Optimaler Segeltrimm reduziert Luvgierigkeit und Autopilot-Stromverbrauch.

**Off-Course Timer:**
Einstellbarer Timer, nach dem der Off-Course-Alarm ausloest. Typisch 20–60 Sekunden bei mehr als 10–15 Grad Abweichung. Verhindert Fehlalarme bei kurzzeitigen Boen.

**Ruderlimit (Rudder Limit):**
Einstellbarer maximaler Ruderausschlag, den der Autopilot kommandiert. Typisch 15–30 Grad. Niedrigere Werte bei Motorfahrt (Richtungsstabilitaet), hoehere bei Segelfahrt (Manoevrierbarkeit).

**SOG (Speed Over Ground):**
Geschwindigkeit ueber Grund, aus GPS-Daten berechnet. Wird vom Autopilot fuer Gain-Anpassung genutzt: hoehere SOG = weniger Gain erforderlich.

**STW (Speed Through Water):**
Geschwindigkeit durchs Wasser, vom Logge/Echolot gemessen. Genauer als SOG fuer Rudereffekt-Berechnung, da Stroemeinfluesse eliminiert sind.

**Turn Rate Limit:**
Maximale erlaubte Drehgeschwindigkeit bei Autopilot-gesteuerten Kursaenderungen. IEC 62065 schreibt Grenzwerte vor. Verhindert gefaehrlich schnelle Kurswechsel bei Wegpunktuebergaengen.

**Variation (Missweisung):**
Winkel zwischen magnetisch Nord und geographisch Nord. Ortsabhaengig, aendert sich jaehrlich. Wird vom GPS geliefert (PGN 127258) und vom Kurscomputer automatisch zur Umrechnung Magnetic→True Heading verwendet.

---

## 11. Schnell-Referenz

### 11.1 Autopilot-Auswahl in 5 Schritten

```
Schritt 1: Bootstyp und Steuerung
  Segel + Pinne → Tiller-Pilot oder Linear unter Deck
  Segel + Rad, mechanisch → Wheel-Pilot oder Linear unter Deck
  Segel + Rad, hydraulisch → Hydraulik-Antrieb
  Motor, mechanisch → Linear oder Hydraulik
  Motor, hydraulisch → Hydraulik-Antrieb

Schritt 2: Verdraengung → Antriebsklasse
  bis 5 t → Tiller-Pilot oder Linear 80 kg
  5–10 t → Linear 80–150 kg
  10–18 t → Linear 150–230 kg
  18–30 t → Hydraulik 150 cc
  30–50 t → Hydraulik 300 cc
  >50 t → Hydraulik 500+ cc

Schritt 3: Einsatzgebiet → Sicherheitsfaktor
  Kuestenfahrt → Dimensionierung nach Herstellerempfehlung
  Offshore → Eine Klasse groesser
  Blauwasser → Eine Klasse groesser + Backup-System

Schritt 4: Hersteller waehlen
  Budget/Cruising → Raymarine Evolution
  Performance/Regatta → B&G oder NKE
  Motorboot → Simrad oder Garmin
  Integration mit vorhandenem System → Gleicher Hersteller

Schritt 5: Zubehoer
  [ ] Ruderfeedback-Sensor (bei Unterdeck-Systemen)
  [ ] Fernbedienung (kabellos empfohlen)
  [ ] Windsensor (fuer Wind-Modus)
  [ ] NMEA2000-Backbone und Zubehoer
  [ ] Kabelquerschnitt und Sicherungen
```

### 11.2 Installations-Checkliste

```
[ ] Antriebseinheit befestigt, spielfrei, Kugelgelenke leichtgaengig
[ ] Ruderfeedback-Sensor montiert, mechanische Verbindung spielfrei
[ ] Kurscomputer montiert, Mindestabstaende zu Stoerquellen eingehalten
[ ] Heading-Sensor montiert (falls separat), Mindestabstaende eingehalten
[ ] Leistungskabel Antrieb → Batterie: korrekter Querschnitt, Sicherung
[ ] NMEA2000-Backbone korrekt: Terminatoren, Spannung, Stichleitungen
[ ] Bedieneinheit montiert, wasserdicht, gut erreichbar
[ ] Fernbedienung gekoppelt und getestet
[ ] Software-Update auf neueste Version
[ ] Kompass-Kalibrierung (Schwenkfahrt) durchgefuehrt
[ ] Ruderfeedback kalibriert (Mitte, BB, StB)
[ ] Autopilot-Lernfahrt (Sea Trial) durchgefuehrt
[ ] Alle Modi getestet (Auto, Wind, Track)
[ ] Kupplung/Bypass getestet (manuelles Steuern bei AP aus)
[ ] Off-Course-Alarm und Ruderlimit eingestellt
```

### 11.3 Wartungs-Checkliste (jaehrlich)

```
[ ] Alle Kabelverbindungen auf Korrosion pruefen
[ ] Ruderfeedback-Kalibrierung verifizieren
[ ] Antriebsmechanik schmieren (Linearantrieb: Spindel, Gelenke)
[ ] Hydraulikfluid-Stand und -Farbe pruefen
[ ] NMEA2000-Stecker auf Korrosion pruefen
[ ] Software/Firmware auf Updates pruefen
[ ] Kompass-Deviation auf 4 Kursen pruefen (N, O, S, W)
[ ] Sicherung und Kabel-Querschnitt verifizieren
[ ] Bordspannung unter Last messen
[ ] Kupplungsfunktion testen
[ ] Alle Modi kurz testen (Auto, Wind, Track)
```

---

## 12. ANHANG A–R

### ANHANG A — Fallstudie: Retrofit Raymarine Evolution auf Bavaria 40 Cruiser

**Boot:** Bavaria 40 Cruiser, Bj. 2008, 12,35 m, 8.900 kg, Radsteuerung mit Whitlock Cobra
**Altes System:** Raymarine ST6002+ mit Type 2 Linear Drive (ca. 15 Jahre alt, Kupplung verschlissen)
**Neues System:** Raymarine Evolution EV-200 Sail Pack

**Komponenten:**
- ACU-200 (E70100): EUR 1.100
- Type 2 Linear Drive (E12140): EUR 1.900
- p70s Bedieneinheit (E22166): EUR 550
- S100 Funkfernbedienung (E15024): EUR 350
- Ruderfeedback-Sensor: vom Altsystem uebernommen (Potentiometer, funktionsfaehig)
- NMEA2000-Zubehoer (Kabel, T-Stuecke, Terminatoren): EUR 120

**Installationsaufwand:** 6 Stunden Selbsteinbau
- Alten Antrieb demontieren (1 h)
- Neuen Antrieb montieren: gleiche Befestigungspunkte (1,5 h)
- ACU-200 montieren und verkabeln (1 h)
- NMEA2000-Netzwerk aufbauen (1 h)
- p70s montieren (0,5 h)
- Kompass-Kalibrierung und Sea Trial (1 h)

**Gesamtkosten:** EUR 4.020 (Material) + EUR 0 (Selbsteinbau)
**Ergebnis:** Deutlich bessere Regelguete (MEMS-Sensor vs. alter Fluxgate), kein Hunting mehr, Wind-Modus erstmals verfuegbar (Windsensor war vorhanden, aber alte ACU hatte keinen Wind-Modus). Stromverbrauch ca. 25 % niedriger.

**AYDI-Bewertung:** Score 82/100, Confidence: documented, Upgrade-Empfehlung: "Ruderfeedback-Potentiometer in naechsten 2 Jahren durch Hallsensor ersetzen."

### ANHANG B — Fallstudie: Hydraulik-Autopilot auf Hallberg-Rassy 48

**Boot:** Hallberg-Rassy 48 MkII, Bj. 2015, 14,76 m, 17.500 kg, hydraulische Steuerung (Lecomble & Schmitt)
**System:** Simrad AP48 mit NAC-3 und RPU-160

**Komponenten:**
- NAC-3 (000-13250-001): EUR 2.200
- RPU-160 Hydraulikpumpe (000-13734-001): EUR 3.200
- Precision-9 Heading-Sensor (000-12607-001): EUR 380
- AP48 Bedieneinheit (000-13290-001): EUR 750
- WR10 Funkfernbedienung (000-12316-001): EUR 320
- Ruderfeedback-Sensor: mitgeliefert
- Hydraulik-Fittings und Schlaeuche: EUR 350
- NMEA2000-Zubehoer: EUR 150

**Installation durch Fachbetrieb:** 12 Stunden
- Hydraulikpumpe in bestehenden Kreislauf integrieren (4 h)
- NAC-3 und Precision-9 montieren und verdrahten (3 h)
- Ruderfeedback-Sensor installieren (1,5 h)
- NMEA2000-Netzwerk mit vorhandenem System verbinden (1,5 h)
- Entlueftung Hydraulik und Testlauf (1 h)
- Sea Trial und Feinabstimmung (1 h)

**Gesamtkosten:** EUR 7.350 (Material) + EUR 2.400 (Installation) = EUR 9.750
**Ergebnis:** Exzellente Regelguete, Shadow Drive funktioniert perfekt mit der L&S Steuerung, Continuum-Algorithmus passt sich automatisch an Nordatlantik-Seegang an. Stromverbrauch: durchschnittlich 4,5 A bei 12V.

**AYDI-Bewertung:** Score 91/100, Confidence: measured (Systemdaten aus NMEA2000), Empfehlung: "System ist korrekt dimensioniert, Bypass-Ventil fuer Notsteuerung vorhanden und getestet."

### ANHANG C — Fallstudie: NKE Gyropilot auf Class 40

**Boot:** Class 40 Regattayacht, 12,19 m, 4.500 kg, Twin-Ruder mit Tillerarm
**System:** NKE Gyropilot 3 mit Jefa Linearantrieb

**Komponenten:**
- Gyropilot 3 Prozessor: EUR 3.500
- Gyropilot Sensor: EUR 1.800
- Jefa Linearantrieb 150 kg (fuer jedes Ruder): 2x EUR 1.600 = EUR 3.200
- NKE Topline TL25 Display: EUR 1.200
- NKE Pilot Remote: EUR 380
- NKE Interface Box (NMEA2000-Gateway): EUR 450
- Ruderfeedback-Sensoren: 2x EUR 250 = EUR 500
- Verkabelung und Zubehoer: EUR 400

**Gesamtkosten:** EUR 11.430 (Material) + EUR 3.500 (Fachinstallation) = EUR 14.930
**Ergebnis:** Ueberlegene Regelguete bei Vorwindkursen im Seegang, Anti-Broaching-Algorithmus verhindert unkontrollierte Halsen bei 25+ Knoten Surfen. Stromverbrauch: durchschnittlich 2,5 A (bemerkenswert niedrig fuer die Leistung) dank optimaler Regelung.

**AYDI-Bewertung:** Score 95/100, Confidence: measured, Hinweis: "NKE-proprietaerer Bus erfordert Interface Box fuer Integration mit Standard-NMEA2000-Geraeten."

### ANHANG D — Fallstudie: Windpilot Pacific auf Langfahrt-HR 36

**Boot:** Hallberg-Rassy 36, Bj. 1995, 10,85 m, 7.500 kg, Radsteuerung, Langfahrt-Ausruestung
**System:** Windpilot Pacific (Pendelruder) + Raymarine EV-100 Wheel (Backup)

**Windpilot Pacific:**
- Windpilot Pacific Pendelruder-Anlage: EUR 4.800
- Individuelle Heckhalterung (massgeschneidert): EUR 600
- Steuerleinen und Umlenkbloecke: EUR 250
- Installation: Selbsteinbau mit Windpilot-Beratung (2 Tage)

**Raymarine EV-100 Wheel (Backup):**
- EV-100 Wheel Pack: EUR 2.200
- Installation: Selbsteinbau (3 Stunden)

**Gesamtkosten:** EUR 7.850
**Ergebnis:** Windpilot steuert zuverlaessig auf allen Amwind- und Raumschotkursen bei 10+ Knoten Wind. Auf Passatrouten (30+ Tage Atlantik): 90 % Windpilot, 10 % Autopilot (Flaute, Motorfahrt). Energieeinsparung: ca. 40–60 Ah/Tag, die sonst der Autopilot verbraucht haette. Windpilot dient zusaetzlich als Notruder.

**AYDI-Bewertung:** Score 88/100, Confidence: documented, Empfehlung: "Ideale Langfahrt-Kombination. Windpilot-Steuerleinen alle 3 Jahre tauschen."

### ANHANG E — Fallstudie: Garmin Reactor 40 auf Beneteau Oceanis 46.1

**Boot:** Beneteau Oceanis 46.1, Bj. 2020, 14,06 m, 10.350 kg, Doppelrad, mechanische Steuerung
**System:** Garmin Reactor 40 mit SD15 Linearantrieb (Navico-kompatibel via NMEA2000)

**Komponenten:**
- Reactor 40 Mechanical CCU (010-02793-00): EUR 1.400
- Simrad SD15 Linearantrieb (000-13731-001): EUR 1.800
- GHC 50 Bedieneinheit (010-02434-00): EUR 650
- Garmin MSC 10 Heading-Sensor: EUR 300
- Ruderfeedback-Sensor: EUR 250
- NMEA2000-Zubehoer: EUR 150

**Gesamtkosten:** EUR 4.550 (Material) + EUR 1.200 (Fachinstallation) = EUR 5.750
**Ergebnis:** Gute Regelguete, nahtlose Integration mit vorhandenem Garmin GPSMAP-Plotter. Wind-Modus mit Garmin gWind Sensor funktioniert zuverlaessig. Steuerung ueber quatix-Smartwatch fuer den Eigner ein Highlight.

**AYDI-Bewertung:** Score 84/100, Confidence: measured, Hinweis: "Garmin Reactor CCU mit Simrad SD-Antrieb funktioniert ueber NMEA2000, aber Shadow Drive ist nur mit Garmin-eigenen Hydraulik-Pumpen verfuegbar."

### ANHANG F — Fallstudie: Autopilot-Ausfall auf Atlantikueberquerung

**Boot:** Oyster 56, 17,07 m, 24.000 kg, hydraulische Steuerung
**System:** Raymarine EV-400 mit Type 3 Hydraulik-Pumpe
**Situation:** Atlantikueberquerung Kanaren → Karibik, Tag 12 von ca. 18

**Ausfallbeschreibung:**
- Fehlermeldung "Drive Overtemp" nach 14 Stunden Dauerbetrieb bei 25 kn Passat und 2,5 m Dunung
- Hydraulikpumpe schaltet thermisch ab
- Manuelle Steuerung ueber Bypass-Ventil sofort moeglich
- Nach 2 Stunden Abkuehlung: Autopilot laeuft wieder, schaltet aber nach 6 Stunden erneut ab

**Ursache (spaetere Analyse):**
- Hydraulikfluid ueberaltert (5 Jahre, nie gewechselt): Viskositaet erhoet → Pumpe arbeitet haerter
- Ungenuegender Luftaustausch im Maschinenraum bei geschlossenen Luken (Passatwind von achtern)
- Segeltrimm suboptimal: permanente Luvgierigkeit erforderte Dauer-Ruderausschlag von 5 Grad

**Sofortmassnahmen an Bord:**
1. Segeltrimm optimiert (Grossegel 1 Reff, Genua flacher getrimmt) → Luvgierigkeit reduziert
2. Maschinenraum-Lueftung geoeffnet
3. Autopilot-Deadband von 3 auf 5 Grad vergroessert
4. Ergebnis: Autopilot lief danach 20+ Stunden ohne Abschaltung

**Massnahmen nach Ankunft:**
- Hydraulikfluid gewechselt (Dexron III → frisches Dexron VI)
- Pumpen-Luefter installiert (12V Luefter am Pumpengehaeuse)
- AYDI-Empfehlung: Hydraulikfluid alle 3 Jahre wechseln, Maschinenraum-Belueftung sicherstellen

**AYDI-Bewertung:** Score 72/100 (vor Massnahmen), Score 88/100 (nach Massnahmen), Confidence: documented.

### ANHANG G — Fallstudie: Kompass-Deviation durch Lautsprecher

**Boot:** Jeanneau Sun Odyssey 440, 13,39 m, 9.200 kg
**System:** B&G NAC-2 mit Precision-9 und SD15

**Problem:** Nach Einbau einer Bluetooth-Musikanlage mit Cockpit-Lautsprechern steuerte der Autopilot auf Nordkurs ca. 8 Grad zu weit nach Osten, auf Suedkurs ca. 6 Grad zu weit nach Westen. Auf Ost- und Westkurs war die Abweichung gering.

**Ursache:** Neodym-Magnete in den Cockpit-Lautsprechern (30 cm vom Precision-9-Sensor entfernt) erzeugten ein staendiges Stoerfeld. Die Deviation war richtungsabhaengig, weil das Stoerfeld in eine feste Richtung wirkte.

**Loesung:**
1. Precision-9-Sensor um 80 cm nach vorn versetzt (weg von Lautsprechern)
2. Kompass-Neukalibrierung (Schwenkfahrt)
3. Restdeviation danach <1 Grad auf allen Kursen

**AYDI-Bewertung:** Score 65/100 (vor Massnahme), Score 90/100 (nach Massnahme), Confidence: measured (Deviation messtechnisch verifiziert).

### ANHANG H — Fallstudie: Multihull-Autopilot auf Lagoon 42

**Boot:** Lagoon 42, 12,80 m, 12.500 kg (segelfertig), Doppelruder, mechanische Steuerung ueber Seilzug
**System:** Simrad AP44 mit NAC-2, zwei SD15 Linearantriebe (einer pro Ruder), Precision-9

**Besonderheit Katamaran:**
- Zwei separate Ruder erfordern zwei Antriebe
- NAC-2 kann zwei SD15 synchron ansteuern (Master/Slave-Konfiguration)
- Katamaran-Profil im NAC-2: angepasste Regelparameter (schnelle Gierbewegung, geringes Rollmoment)
- Hoehere Geschwindigkeit als Einrumpfer: Ruderkraefte hoeher als die Verdraengung vermuten laesst

**Dimensionierung:**
- Verdraengung 12.500 kg → normalerweise Linear 150 kg ausreichend
- Aber: Rumpfgeschwindigkeit bis 10 kn, hoehere Ruderkraefte → SD15 (150 kg) pro Ruder korrekt
- Fuer Katamarane gilt: eine Klasse groesser als nach Verdraengung allein

**Gesamtkosten:** EUR 8.200 (Material) + EUR 2.800 (Fachinstallation) = EUR 11.000
**Ergebnis:** Gute Regelguete, kein Hunting trotz schneller Gierbewegung. Katamaran-Profil im NAC-2 macht spuerbaren Unterschied gegenueber Standard-Segel-Profil.

**AYDI-Bewertung:** Score 86/100, Confidence: measured, Hinweis: "Korrekte Multihull-Dimensionierung, zwei synchrone Antriebe optimal."

---

### ANHANG I — Pydantic v2 Datenmodelle fuer AYDI Autopilot-Analyse

```python
"""
AYDI Autopilot Analysis Models — Pydantic v2
Module: 14.05 Autopilot-Systeme

All models use model_config = {"from_attributes": True} per AYDI convention.
German descriptions, English code.
"""

from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


# --- Enums ---

class ConfidenceLevel(str, Enum):
    """Confidence levels per AYDI framework."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class AutopilotType(str, Enum):
    """Types of autopilot systems."""
    TILLER_PILOT = "tiller_pilot"
    WHEEL_PILOT = "wheel_pilot"
    BELOW_DECK_LINEAR = "below_deck_linear"
    BELOW_DECK_ROTARY = "below_deck_rotary"
    HYDRAULIC = "hydraulic"
    WINDVANE_PENDULUM = "windvane_pendulum"
    WINDVANE_AUXILIARY = "windvane_auxiliary"
    WINDVANE_TRIM_TAB = "windvane_trim_tab"


class AutopilotManufacturer(str, Enum):
    """Major autopilot manufacturers."""
    RAYMARINE = "raymarine"
    BG = "b_and_g"
    SIMRAD = "simrad"
    GARMIN = "garmin"
    NKE = "nke"
    FURUNO = "furuno"
    HYDROVANE = "hydrovane"
    MONITOR = "monitor"
    WINDPILOT = "windpilot"
    PELAGIC = "pelagic"
    COMNAV = "comnav"
    OTHER = "other"


class DriveType(str, Enum):
    """Drive unit types."""
    LINEAR_LIGHT = "linear_light"
    LINEAR_MEDIUM = "linear_medium"
    LINEAR_HEAVY = "linear_heavy"
    HYDRAULIC_SMALL = "hydraulic_small"
    HYDRAULIC_MEDIUM = "hydraulic_medium"
    HYDRAULIC_LARGE = "hydraulic_large"
    WHEEL_DRIVE = "wheel_drive"
    ROTARY_DRIVE = "rotary_drive"


class CompassType(str, Enum):
    """Compass / heading sensor types."""
    FLUXGATE = "fluxgate"
    GPS_DUAL_ANTENNA = "gps_dual_antenna"
    MEMS_AHRS = "mems_ahrs"
    RATE_GYRO = "rate_gyro"
    COMBINED_AHRS = "combined_ahrs"


class AutopilotMode(str, Enum):
    """Autopilot operating modes."""
    STANDBY = "standby"
    HEADING_HOLD = "heading_hold"
    WIND_AWA = "wind_awa"
    WIND_TWA = "wind_twa"
    TRACK = "track"
    NO_DRIFT = "no_drift"
    POWER_STEER = "power_steer"
    DODGE = "dodge"


class FeedbackSensorType(str, Enum):
    """Rudder feedback sensor types."""
    POTENTIOMETER = "potentiometer"
    HALL_EFFECT = "hall_effect"
    LINEAR_POSITION = "linear_position"
    NMEA2000_DIGITAL = "nmea2000_digital"
    INTEGRATED = "integrated"
    NONE = "none"


class SeverityLevel(str, Enum):
    """Severity of a finding."""
    CRITICAL = "critical"
    WARNING = "warning"
    INFO = "info"
    OK = "ok"


class BoatType(str, Enum):
    """Boat types for autopilot sizing."""
    SAIL_MONOHULL = "sail_monohull"
    SAIL_CATAMARAN = "sail_catamaran"
    SAIL_TRIMARAN = "sail_trimaran"
    MOTOR_DISPLACEMENT = "motor_displacement"
    MOTOR_SEMI_DISPLACEMENT = "motor_semi_displacement"
    MOTOR_PLANING = "motor_planing"


class SteeringSystemType(str, Enum):
    """Type of the boat's steering system."""
    TILLER = "tiller"
    WHEEL_MECHANICAL = "wheel_mechanical"
    WHEEL_HYDRAULIC = "wheel_hydraulic"
    WHEEL_CABLE = "wheel_cable"


# --- Core Models ---

class AutopilotSpec(BaseModel):
    """Specification of an autopilot system."""

    model_config = {"from_attributes": True}

    autopilot_type: AutopilotType = Field(..., description="Typ des Autopiloten")
    manufacturer: AutopilotManufacturer = Field(..., description="Hersteller")
    model_name: Optional[str] = Field(None, description="Modellbezeichnung")
    course_computer_model: Optional[str] = Field(None, description="Kurscomputer-Modell (z.B. ACU-200, NAC-2)")
    drive_model: Optional[str] = Field(None, description="Antriebseinheit-Modell")
    drive_type: Optional[DriveType] = Field(None, description="Antriebstyp")
    compass_type: CompassType = Field(default=CompassType.MEMS_AHRS, description="Kompasstyp")
    feedback_sensor_type: FeedbackSensorType = Field(
        default=FeedbackSensorType.POTENTIOMETER,
        description="Ruderfeedback-Sensortyp"
    )
    control_head_model: Optional[str] = Field(None, description="Bedieneinheit-Modell")
    has_remote: bool = Field(default=False, description="Funkfernbedienung vorhanden")
    has_wind_mode: bool = Field(default=False, description="Wind-Modus verfuegbar")
    has_track_mode: bool = Field(default=True, description="Track-Modus (GPS-Route) verfuegbar")
    supply_voltage_v: float = Field(default=12.0, ge=10.0, le=32.0, description="Versorgungsspannung in V")
    installation_year: Optional[int] = Field(None, ge=1980, le=2030, description="Installationsjahr")
    bus_system: Optional[str] = Field(None, description="Bus-System (z.B. NMEA2000, SeaTalkng, NKE)")
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.ESTIMATED)


class AutopilotDriveSpec(BaseModel):
    """Detailed specification of the drive unit."""

    model_config = {"from_attributes": True}

    drive_type: DriveType = Field(..., description="Antriebstyp")
    max_force_n: Optional[float] = Field(None, ge=0, description="Maximalkraft in N (linear)")
    max_torque_nm: Optional[float] = Field(None, ge=0, description="Maximaldrehmoment in Nm (rotary)")
    stroke_mm: Optional[float] = Field(None, ge=0, description="Hub in mm (linear)")
    speed_mm_per_s: Optional[float] = Field(None, ge=0, description="Stellgeschwindigkeit in mm/s")
    speed_deg_per_s: Optional[float] = Field(None, ge=0, description="Stellgeschwindigkeit in Grad/s")
    peak_current_a: Optional[float] = Field(None, ge=0, description="Spitzenstrom in A")
    avg_current_a: Optional[float] = Field(None, ge=0, description="Durchschnittsstrom in A")
    has_clutch: bool = Field(default=True, description="Kupplung vorhanden")
    hydraulic_volume_cc: Optional[float] = Field(None, ge=0, description="Hydraulikvolumen in cc")
    hydraulic_flow_l_per_min: Optional[float] = Field(None, ge=0, description="Hydraulikdurchfluss in l/min")
    weight_kg: Optional[float] = Field(None, ge=0, description="Gewicht in kg")
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.ESTIMATED)


class AutopilotCondition(BaseModel):
    """Condition assessment of an autopilot system."""

    model_config = {"from_attributes": True}

    overall_condition_score: int = Field(..., ge=0, le=100, description="Gesamtzustand 0-100")
    drive_condition_score: Optional[int] = Field(None, ge=0, le=100, description="Antriebszustand")
    sensor_condition_score: Optional[int] = Field(None, ge=0, le=100, description="Sensorzustand")
    feedback_condition_score: Optional[int] = Field(None, ge=0, le=100, description="Feedback-Sensor-Zustand")
    compass_deviation_max_deg: Optional[float] = Field(
        None, ge=0, le=180, description="Max. Kompass-Deviation in Grad"
    )
    rudder_feedback_play_deg: Optional[float] = Field(
        None, ge=0, le=30, description="Ruderfeedback-Spiel in Grad"
    )
    drive_speed_percent: Optional[float] = Field(
        None, ge=0, le=150, description="Antriebsgeschwindigkeit in % des Sollwerts"
    )
    supply_voltage_under_load_v: Optional[float] = Field(
        None, ge=0, le=32, description="Bordspannung unter Last in V"
    )
    hydraulic_fluid_condition: Optional[str] = Field(
        None, description="Hydraulikfluid-Zustand (klar/trueb/dunkel/Partikel)"
    )
    last_calibration_date: Optional[date] = Field(None, description="Letzte Kompass-Kalibrierung")
    last_service_date: Optional[date] = Field(None, description="Letzter Service-Termin")
    age_years: Optional[float] = Field(None, ge=0, description="Alter des Systems in Jahren")
    operating_hours: Optional[float] = Field(None, ge=0, description="Betriebsstunden (falls verfuegbar)")
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.ESTIMATED)


class AutopilotFinding(BaseModel):
    """A single finding from autopilot analysis."""

    model_config = {"from_attributes": True}

    finding_id: str = Field(..., description="Eindeutige Befund-ID (z.B. AP-F01)")
    severity: SeverityLevel = Field(..., description="Schweregrad")
    category: str = Field(..., description="Kategorie (z.B. compass, drive, feedback, power, hydraulic)")
    title_de: str = Field(..., description="Befundtitel auf Deutsch")
    description_de: str = Field(..., description="Beschreibung auf Deutsch")
    location: Optional[str] = Field(None, description="Ort des Befunds (z.B. Antriebseinheit, Kurscomputer)")
    suggestion_de: str = Field(..., description="Empfehlung auf Deutsch")
    estimated_cost_eur: Optional[float] = Field(None, ge=0, description="Geschaetzte Behebungskosten in EUR")
    reference_fehler_id: Optional[str] = Field(None, description="Referenz auf Fehlerbild (z.B. F01, F03)")
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.ESTIMATED)


class AutopilotSizingInput(BaseModel):
    """Input parameters for autopilot sizing calculation."""

    model_config = {"from_attributes": True}

    boat_type: BoatType = Field(..., description="Bootstyp")
    loa_m: float = Field(..., ge=5.0, le=50.0, description="Laenge ueber alles in m")
    displacement_kg: float = Field(..., ge=500, le=200000, description="Verdraengung in kg (segelfertig)")
    max_speed_kn: Optional[float] = Field(None, ge=0, le=40, description="Max. Geschwindigkeit in kn")
    rudder_area_m2: Optional[float] = Field(None, ge=0.01, le=5.0, description="Ruderblattflaeche in m^2")
    rudder_balance_ratio: Optional[float] = Field(None, ge=0, le=0.5, description="Ruder-Balancegrad")
    quadrant_radius_mm: Optional[float] = Field(None, ge=50, le=500, description="Quadrant-Radius in mm")
    steering_system: SteeringSystemType = Field(..., description="Steuerungstyp")
    dual_rudder: bool = Field(default=False, description="Doppelruder")
    usage: str = Field(default="offshore", description="Einsatz: coastal/offshore/bluewater")
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.ESTIMATED)


class AutopilotSizingResult(BaseModel):
    """Result of autopilot sizing calculation."""

    model_config = {"from_attributes": True}

    recommended_drive_type: DriveType = Field(..., description="Empfohlener Antriebstyp")
    recommended_drive_force_n: Optional[float] = Field(None, ge=0, description="Empfohlene Antriebskraft in N")
    recommended_drive_torque_nm: Optional[float] = Field(None, ge=0, description="Empfohlenes Drehmoment in Nm")
    calculated_rudder_torque_nm: Optional[float] = Field(None, ge=0, description="Berechnetes Rudermoment in Nm")
    safety_factor: float = Field(..., ge=1.0, le=3.0, description="Angewandter Sicherheitsfaktor")
    recommended_stroke_mm: Optional[float] = Field(None, ge=0, description="Empfohlener Hub in mm")
    recommended_hydraulic_volume_cc: Optional[float] = Field(None, ge=0, description="Empf. Hydraulikvolumen in cc")
    recommended_products: list[str] = Field(
        default_factory=list, description="Liste empfohlener Produkte (Modellbezeichnungen)"
    )
    sizing_notes_de: list[str] = Field(default_factory=list, description="Dimensionierungshinweise auf Deutsch")
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.CALCULATED)


class AutopilotEnergyAnalysis(BaseModel):
    """Energy consumption analysis for an autopilot system."""

    model_config = {"from_attributes": True}

    avg_current_a: float = Field(..., ge=0, le=100, description="Durchschnittlicher Strom in A")
    peak_current_a: float = Field(..., ge=0, le=200, description="Spitzenstrom in A")
    daily_consumption_ah: float = Field(..., ge=0, le=1000, description="24h-Verbrauch in Ah")
    daily_consumption_calm_ah: Optional[float] = Field(
        None, ge=0, description="24h-Verbrauch bei ruhigem Wetter in Ah"
    )
    daily_consumption_rough_ah: Optional[float] = Field(
        None, ge=0, description="24h-Verbrauch bei rauem Wetter in Ah"
    )
    supply_voltage_v: float = Field(default=12.0, description="Systemspannung in V")
    required_battery_capacity_ah: Optional[float] = Field(
        None, ge=0, description="Empfohlene Batteriekapazitaet in Ah"
    )
    solar_offset_wp: Optional[float] = Field(
        None, ge=0, description="Empfohlene Solarleistung zum Ausgleich in Wp"
    )
    notes_de: list[str] = Field(default_factory=list, description="Hinweise auf Deutsch")
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.ESTIMATED)


class AutopilotNMEA2000Status(BaseModel):
    """Status of NMEA2000 network relevant to autopilot."""

    model_config = {"from_attributes": True}

    bus_voltage_v: Optional[float] = Field(None, ge=0, le=16, description="NMEA2000-Bus-Spannung in V")
    device_count: Optional[int] = Field(None, ge=0, description="Anzahl Geraete auf dem Bus")
    heading_source: Optional[str] = Field(None, description="Heading-Quelle (Geraetename)")
    gps_source: Optional[str] = Field(None, description="GPS-Quelle")
    wind_source: Optional[str] = Field(None, description="Wind-Quelle")
    rudder_source: Optional[str] = Field(None, description="Ruderfeedback-Quelle")
    xte_source: Optional[str] = Field(None, description="Cross-Track-Error-Quelle (Plotter)")
    missing_sources: list[str] = Field(default_factory=list, description="Fehlende Datenquellen")
    bus_errors: Optional[int] = Field(None, ge=0, description="Bus-Fehler (CAN-Error-Frames)")
    terminators_ok: Optional[bool] = Field(None, description="Terminatoren korrekt")
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.MEASURED)


class AutopilotMaintenanceSchedule(BaseModel):
    """Maintenance schedule for an autopilot system."""

    model_config = {"from_attributes": True}

    autopilot_type: AutopilotType = Field(..., description="Autopilot-Typ")
    tasks: list[dict] = Field(
        ...,
        description=(
            "Wartungsaufgaben mit 'task_de', 'interval_months', "
            "'professional_required', 'estimated_cost_eur'"
        )
    )
    next_service_date: Optional[date] = Field(None, description="Naechster Service-Termin")
    estimated_annual_cost_eur: Optional[float] = Field(None, ge=0, description="Geschaetzte jaehrliche Kosten")
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.BENCHMARK)


class WindvaneSelfSteeringSpec(BaseModel):
    """Specification for a windvane self-steering system."""

    model_config = {"from_attributes": True}

    manufacturer: AutopilotManufacturer = Field(..., description="Hersteller")
    model_name: Optional[str] = Field(None, description="Modellbezeichnung")
    windvane_type: str = Field(
        ..., description="Typ: pendulum, auxiliary_rudder, trim_tab, servo_auxiliary"
    )
    max_displacement_kg: Optional[float] = Field(None, ge=0, description="Max. Verdraengung in kg")
    weight_kg: Optional[float] = Field(None, ge=0, description="Gewicht in kg")
    serves_as_emergency_rudder: bool = Field(default=False, description="Dient als Notruder")
    material: Optional[str] = Field(None, description="Hauptmaterial (z.B. Edelstahl, Aluminium)")
    installation_year: Optional[int] = Field(None, ge=1960, le=2030, description="Installationsjahr")
    condition_score: Optional[int] = Field(None, ge=0, le=100, description="Zustandsbewertung 0-100")
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.ESTIMATED)


class AutopilotAnalysisResult(BaseModel):
    """Complete result of an autopilot analysis."""

    model_config = {"from_attributes": True}

    spec: AutopilotSpec = Field(..., description="Spezifikation des Autopilot-Systems")
    drive_spec: Optional[AutopilotDriveSpec] = Field(None, description="Antriebsspezifikation")
    condition: AutopilotCondition = Field(..., description="Zustandsbewertung")
    sizing: Optional[AutopilotSizingResult] = Field(None, description="Dimensionierungsergebnis")
    energy: Optional[AutopilotEnergyAnalysis] = Field(None, description="Energieanalyse")
    nmea2000_status: Optional[AutopilotNMEA2000Status] = Field(None, description="NMEA2000-Status")
    windvane: Optional[WindvaneSelfSteeringSpec] = Field(None, description="Windsteueranlage (falls vorhanden)")
    findings: list[AutopilotFinding] = Field(default_factory=list, description="Liste der Befunde")
    critical_findings: int = Field(default=0, ge=0, description="Anzahl kritischer Befunde")
    overall_score: int = Field(..., ge=0, le=100, description="Gesamtscore")
    overall_confidence: ConfidenceLevel = Field(..., description="Gesamt-Konfidenz")
    available_modes: list[AutopilotMode] = Field(default_factory=list, description="Verfuegbare Modi")
    analysis_version: str = Field(default="1.0.0", description="Version des Analyse-Algorithmus")
    analysis_date: date = Field(..., description="Analysedatum")
    summary_de: str = Field(..., description="Zusammenfassung auf Deutsch")
```

---

### ANHANG J — Visuelle Analyse-Leitfaden fuer AYDI Pipeline B

Folgende Merkmale koennen durch visuelle Analyse (Fotos) bei Autopilot-Systemen erkannt werden:

| Merkmal | Confidence | Erkennungsmethode |
|---------|-----------|-------------------|
| Autopilot-Typ (Tiller/Wheel/Unterdeck) | visual_high | Direktes Erkennen der Antriebsform |
| Hersteller (Raymarine/B&G/Simrad/Garmin) | visual_medium | Logo auf Bedieneinheit, Gehaeuse-Design |
| Bedieneinheit-Modell | visual_medium | Displaygroesse, Tastenform, Farbgebung |
| Tiller-Pilot Zustand | visual_high | Korrosion, Gehaeuseschaeden, UV-Schaeden |
| Wheel-Pilot Reibrad-Zustand | visual_medium | Abrieb, Verschleiss am Kontaktpunkt |
| Linearantrieb Zustand (unter Deck) | visual_medium | Korrosion, Oelspuren, Kabelzustand |
| Hydraulikleckage | visual_high | Oelflecken, Verfaerbungen, Tropfstellen |
| Ruderfeedback-Sensor vorhanden | visual_medium | Sensor am Ruderschaft erkennbar |
| NMEA2000-Verkabelung Zustand | visual_medium | Kabelordnung, Stecker, Korrosion |
| Windsteueranlage Typ | visual_high | Pendelruder/Hilfsruder am Heck erkennbar |
| Windsteueranlage Zustand | visual_medium | Korrosion, Steuerleinen, Windfahne |
| Windsteueranlage Hersteller | visual_medium | Bauform, Logo, Farbgebung |
| Kompass-Sensor Montageort | visual_low | Oft versteckt, schwer zu beurteilen |
| Kupplungs-Zustand | visual_low | Meist verdeckt, nur bei Demontage sichtbar |

**Prompt-Hinweise fuer Claude Vision (Pipeline B):**
- Autopilot-Bedieneinheit immer im Kontext des Steuerstands bewerten
- Alter des Systems aus Gehaeuse-Design und Displaytyp schaetzen
- Tiller-Pilot: UV-Schaeden am Gehaeuse als Indikator fuer Ausseneinsatz-Dauer
- Bei Unterdeck-Fotos: Oelspuren und Korrosion an Antriebseinheit beachten
- Hydraulikleitungen: Farbveraenderung des Fluids und Dichtungen pruefen
- Windsteueranlage: Pendelruder-Zustand, Steuerleinen-Verschleiss, Windfahnen-Material
- NMEA2000-Kabel: ordentliche Verlegung und Stecker-Zustand bewerten

---

### ANHANG K — Hersteller-Kontaktdaten und Ressourcen

| Hersteller | Land | Website | Support |
|------------|------|---------|---------|
| Raymarine | UK | raymarine.com | +44 1329 246700 |
| B&G | UK | bandg.com | Navico Support Portal |
| Simrad | Norwegen | simrad-yachting.com | Navico Support Portal |
| Garmin Marine | USA | garmin.com/marine | +1 800 800 1020 |
| NKE Marine Electronics | Frankreich | nfranceke.fr | +33 2 97 36 79 47 |
| Hydrovane | UK/Kanada | hydrovane.com | info@hydrovane.com |
| Scanmar Marine (Monitor) | USA | selfsteer.com | +1 707 820 9680 |
| Windpilot (Peter Foerthmann) | Deutschland | windpilot.com | +49 40 2000 3021 |
| Furuno | Japan | furuno.com | Laendervertretungen |
| Pelagic | Australien | pelagicautopilot.com | info@pelagicautopilot.com |

---

### ANHANG L — Normen und Vorschriften Kurzreferenz

| Norm | Thema | Relevanz fuer Autopilot |
|------|-------|------------------------|
| ISO 25197 (2020) | Elektrische/elektronische Anlagen Sportboote | Kabelquerschnitte, Sicherungen, EMV, Installation |
| IEC 62065 (2014) | Track Control Systems | Anforderungen an GPS-Routensteuerung, Sicherheitsalarme |
| IEC 61162-3 (2018) | NMEA2000 / CAN-Bus | Datenbus-Standard, PGN-Definitionen |
| ISO 8728 (2014) | Steueranlagen-Anforderungen | Allgemeine Anforderungen, Redundanz, Notsteuerung |
| ISO 10592 (1994) | Hydraulische Steuerung | Hydraulik-Spezifikationen |
| EN 60945 (2002) | Maritime Navigationsgeraete | EMV, Umweltanforderungen, Pruefung |
| ABYC A-28 (2019) | Galvanic Isolators | Galvanische Trennung fuer NMEA2000 |

---

### ANHANG M — Lebensdauer und Ersatzteilplanung

| Komponente | Typische Lebensdauer | Ersatzteil-Verfuegbarkeit | Aktion |
|------------|---------------------|--------------------------|--------|
| Kurscomputer | 10–15 Jahre | 8–12 Jahre nach Kauf | Austausch bei Obsoleszenz |
| Linearantrieb (Motor) | 8–12 Jahre / 5.000–10.000 h | Gut (Standard-Groessen) | Motorwechsel moeglich |
| Linearantrieb (Spindel) | 5–10 Jahre | Gut | Spindelwechsel als Service |
| Elektromagnetische Kupplung | 5–10 Jahre | Gut | Tausch bei Schlupf |
| Hydraulikpumpe | 10–15 Jahre | Gut | Dichtungssaetze verfuegbar |
| Hydraulikzylinder | 10–20 Jahre | Gut | Dichtungswechsel alle 5 Jahre |
| Potentiometer-Feedback | 5–10 Jahre | Gut | Regelmaessig tauschen |
| Hall-Sensor-Feedback | 15+ Jahre | Gut | Wartungsfrei |
| Fluxgate-Kompass | 15–20 Jahre | Moderat | Langlebig |
| MEMS-AHRS Sensor | 10–15 Jahre | Gut (aktuelle Modelle) | Wartungsfrei |
| Bedieneinheit | 8–12 Jahre | Moderat (LCD/Display) | Display-Ausbleichen |
| NMEA2000-Stecker | 10+ Jahre | Sehr gut | Bei Korrosion tauschen |
| Hydraulikschlaeuche | 8–12 Jahre | Sehr gut | Praeventiv tauschen |
| Steuerleinen (Windsteueranlage) | 3–5 Jahre | Sehr gut | Regelmaessig tauschen |

---

### ANHANG N — Stromverbrauch Vergleichstabelle (gemessene Werte)

| Boot | System | Bedingungen | Strom (Durchschn.) | Strom (Spitze) | 24h Ah |
|------|--------|-------------|-------------------|----------------|--------|
| 8 m Segel, 2.500 kg | Raymarine EV-100 Tiller | Leichter Wind, flach | 0,7 A | 3,5 A | 17 Ah |
| 8 m Segel, 2.500 kg | Raymarine EV-100 Tiller | 20 kn, 1 m Welle | 1,8 A | 4,0 A | 43 Ah |
| 12 m Segel, 8.500 kg | Simrad NAC-2 + SD15 | Leichter Wind, flach | 1,5 A | 8 A | 36 Ah |
| 12 m Segel, 8.500 kg | Simrad NAC-2 + SD15 | 25 kn, 2 m Welle | 4,2 A | 14 A | 101 Ah |
| 15 m Segel, 14.000 kg | Raymarine EV-200 + Type 2 | Leichter Wind, flach | 2,0 A | 12 A | 48 Ah |
| 15 m Segel, 14.000 kg | Raymarine EV-200 + Type 2 | 25 kn, 2 m Welle | 5,5 A | 15 A | 132 Ah |
| 18 m Segel, 22.000 kg | B&G NAC-3 + RPU-160 | Leichter Wind, flach | 3,0 A | 18 A | 72 Ah |
| 18 m Segel, 22.000 kg | B&G NAC-3 + RPU-160 | 30 kn, 3 m Welle | 8,5 A | 28 A | 204 Ah |
| 12 m Motor, 10.000 kg | Garmin Reactor 40 + GHP 12 | Ruhig, 8 kn | 2,2 A | 12 A | 53 Ah |
| 12 m Motor, 10.000 kg | Garmin Reactor 40 + GHP 12 | 20 kn Wind, 1.5 m | 4,8 A | 18 A | 115 Ah |
| Class 40, 4.500 kg | NKE Gyropilot 3 + Jefa | 20 kn, 1.5 m Welle | 1,8 A | 6 A | 43 Ah |
| Class 40, 4.500 kg | NKE Gyropilot 3 + Jefa | 30 kn, Surfen | 3,0 A | 10 A | 72 Ah |

Alle Werte bei 12V-Systemen. Quelle: Hersteller-TDS und dokumentierte Nutzerdaten (Confidence: measured/documented).

---

### ANHANG O — Preisvergleich Komplettsysteme (Stand 2026, inkl. MwSt.)

| Bootklasse | Raymarine | B&G/Simrad | Garmin | NKE |
|------------|-----------|-----------|--------|-----|
| 8 m Segel, Pinne | EV-100 Tiller EUR 1.800 | — | — | — |
| 10 m Segel, Rad | EV-100 Wheel EUR 2.200 | — | Reactor 40 + GHC 20 EUR 2.500 | — |
| 12 m Segel, Linear | EV-200 Sail EUR 3.800 | NAC-1+SD10+Triton2 EUR 3.200 | Reactor 40+SD15+GHC50 EUR 4.200 | — |
| 15 m Segel, Linear | EV-200 Sail+Type2 EUR 4.800 | NAC-2+SD15+Triton2 EUR 4.600 | Reactor 40+SD15+GHC50 EUR 4.800 | Gyropilot+Jefa EUR 8.500 |
| 18 m Segel, Hydraulik | EV-400 Sail EUR 6.500 | NAC-3+RPU-160+AP48 EUR 7.200 | Reactor 40+GHP20+GHC50 EUR 6.800 | Gyropilot+L&S EUR 10.500 |
| 22 m Motor, Hydraulik | EV-400+Type3Hyd EUR 9.500 | NAC-3+RPU-300+AP48 EUR 9.800 | Reactor 40+GHP30+GHC50 EUR 9.500 | — |

Preise ohne Installation. Installation durch Fachbetrieb: ca. EUR 500–3.000 je nach System und Boot.

---

### ANHANG P — Umrechnungstabellen und Formeln

**Kraft:**
- 1 kg (Kraft) = 9,81 N
- 1 lbf = 4,448 N
- 1 kN = 1.000 N = 101,97 kgf

**Drehmoment:**
- 1 Nm = 1 N * 1 m
- 1 ft*lbf = 1,356 Nm
- 1 kgf*cm = 0,0981 Nm

**Geschwindigkeit:**
- 1 kn = 0,5144 m/s = 1,852 km/h
- 1 m/s = 1,944 kn

**Hydraulik:**
- 1 cc = 1 ml = 0,001 l
- 1 bar = 100 kPa = 14,5 psi

**Rudermoment-Schnellformel:**
```
T_rudder [Nm] ≈ 0.23 * v_kn^2 * A_rudder_m2 * (1 - 2*balance_ratio)

Beispiel: 7 kn, 0.15 m^2, 25% Balance:
T ≈ 0.23 * 49 * 0.15 * 0.50 = 0.85 Nm (netto)
→ Mit SF 1.75: T_design = 1.49 Nm (am Ruderschaft)
→ Bei 200 mm Quadrant-Hebelarm: F_drive = 1.49/0.20 = 7.4 N ≈ 0.8 kg
(Anmerkung: Dies ist das Netto-Moment. Die reale Ruderkraft ist hoeher
wegen Stroemungseffekten; konservative Berechnung nach Abschnitt 5.3 verwenden.)
```

> ⚠️ **ZU PRÜFEN (Audit):** Ergebnis ca. 0,85 Nm netto vs. ca. 87 Nm aus Abschnitt 5.3 (vergleichbare Ruderklasse) — rund 100x zu niedrig und physikalisch unplausibel (Industrieformel Lecomble & Schmitt / Peachment liefert ca. 28-55 Nm netto). Der Zahlenfaktor 0.23 duerfte um rund Faktor 100 zu klein sein (Ableitung aus F = 0,5 * rho * v^2 * A * C_n ergibt eine Konstante von ca. 20-23, abhaengig von angenommener Profiltiefe und Druckpunktlage) — exakter Wert nicht zweifelsfrei belegt, daher hier NICHT korrigiert. NICHT zur Antriebsauslegung verwenden; stattdessen Abschnitt 5.3 bzw. Norm-/Herstellerformel (ISO 12215-8, LS/Peachment). Confidence: estimated — unverifiziert.

**Autopilot-Stromverbrauch Schaetzung:**
```
Tagesverbrauch [Ah] ≈ P_avg * 20

wobei P_avg = durchschnittlicher Strom in A ueber eine typische Wache

Fuer Dimensionierung der Batteriekapazitaet:
Batterie [Ah] ≥ Tagesverbrauch * 3 / 0.5
(3 Tage Autonomie, 50% Entladetiefe)
```

---

### ANHANG Q — Fehlerbild-Referenztabelle (Kurzfassung)

| ID | Fehlerbild | Leitsymptom | Haeufigkeit | Kritikalitaet |
|----|-----------|-------------|-------------|---------------|
| F01 | Kompassfehler / Deviation | Systematische Kursabweichung | Hoch | Mittel |
| F02 | Antriebskupplung rutscht | Antrieb laeuft, Ruder bewegt sich nicht | Mittel | Hoch |
| F03 | Hunting (Pendeln) | Staendige Ruderbewegung, Schlangenlinien | Hoch | Niedrig |
| F04 | Ueberkompensation (Overshoot) | Ueberschiessen bei Kursaenderung | Mittel | Niedrig |
| F05 | Kein Antrieb | Drive Not Responding | Mittel | Kritisch |
| F06 | Ruderfeedback-Fehler | RF Fault, unrealistische Werte | Mittel | Kritisch |
| F07 | Ueberhitzung Antrieb | Thermal Shutdown nach Dauerbetrieb | Niedrig | Hoch |
| F08 | Langsamer Antrieb | Traege Ruderbewegung | Mittel | Mittel |
| F09 | Falscher Wind-Modus | Falscher Windwinkel | Niedrig | Niedrig |
| F10 | Track-Modus Fehlnavigation | Zickzack auf Route | Niedrig | Mittel |
| F11 | Hydraulik-Leckage | Oelflecken, Fluidverlust | Mittel (Hydr.) | Hoch |
| F12 | Stromversorgungsprobleme | Low Voltage, Abschaltung | Hoch | Kritisch |

---

### ANHANG R — Kompatibilitaetsmatrix Kurscomputer × Antrieb

| Kurscomputer | Linear Light | Linear Medium | Linear Heavy | Hyd. Klein | Hyd. Mittel | Hyd. Gross |
|-------------|-------------|--------------|-------------|-----------|------------|-----------|
| Raymarine ACU-100 | Ja (Type 1) | — | — | — | — | — |
| Raymarine ACU-150 | Ja | Ja (Type 2) | — | — | — | — |
| Raymarine ACU-200 | Ja | Ja | Ja (Type 3) | — | — | — |
| Raymarine ACU-300 | — | Ja | Ja | — | — | — |
| Raymarine ACU-400 | — | — | — | Ja (Type 1H) | Ja (Type 2H) | Ja (Type 3H) |
| B&G/Simrad NAC-1 | Ja (SD10) | — | — | — | — | — |
| B&G/Simrad NAC-2 | Ja | Ja (SD15) | Ja (SD25) | — | — | — |
| B&G/Simrad NAC-3 | — | — | — | Ja (SS) | Ja (RPU-160) | Ja (RPU-300) |
| Garmin Reactor 40 M | Ja* | Ja* | — | — | — | — |
| Garmin Reactor 40 H | — | — | — | Ja (GHP Comp.) | Ja (GHP 12/20) | Ja (GHP 30) |
| NKE Gyropilot 3 | Ja** | Ja** | Ja** | Ja** | Ja** | — |

\* Garmin Reactor Mechanical steuert NMEA2000-kompatible Antriebe (inkl. Simrad SD)
\** NKE steuert ueber analoge Schnittstelle verschiedene Fremdantriebe (Jefa, L&S, etc.)

---

### ANHANG R2 — Visuelle Analyse-Leitfaden: Autopilot-spezifische Scoring-Kriterien

| Visuelles Merkmal | Score-Auswirkung | Beispiel |
|-------------------|-----------------|---------|
| Oelflecken unter Hydraulikantrieb | -15 bis -25 Punkte | Aktive Leckage an Verschraubung |
| Korrosion an Tiller-Pilot-Gehaeuse | -10 bis -20 Punkte | Salzwasserspuren, Pittingkorrosion |
| Verdrehte/geknickte NMEA2000-Kabel | -5 bis -10 Punkte | Kabel unter Spannung, scharfe Knicke |
| Verschlissene Windsteueranlagen-Leinen | -10 bis -15 Punkte | Ausgefranste Enden, UV-Schaeden |
| Verwitterte Windfahne | -5 bis -10 Punkte | UV-Schaeden, Risse im Material |
| Saubere, ordentliche Installation | +5 bis +10 Punkte | Kabelbaender, Zugentlastung, Beschriftung |
| Backup-System sichtbar | +5 Punkte | Tiller-Pilot als Backup, Windsteueranlage |

**Prompt-Hinweise fuer Claude Vision (Pipeline B):**
- Autopilot-Installation immer im Kontext des Gesamtboots bewerten
- Alter des Systems aus Gehaeuse-Design und Displaygeneration schaetzen
- Wartungszustand aus Korrosion, Oelspuren und Kabelordnung ableiten
- Bei Unterdeck-Fotos: Antrieb-Befestigung (Schrauben, Bolzen) auf Festigkeit visuell bewerten
- Hydraulikleitungen: Farbveraenderung des Fluids durch transparente Abschnitte erkennen
- Windsteueranlagen: Gesamteindruck (poliert vs. vernachlaessigt) korreliert stark mit Funktionszustand

---

---

### ANHANG R3 — Installationsbeispiele mit Zeitaufwand

**Beispiel 1: Tiller-Pilot auf 8 m Segelyacht (Selbsteinbau)**

| Schritt | Arbeitsgang | Zeit |
|---------|------------|------|
| 1 | Pinnenadapter pruefen und anpassen | 15 min |
| 2 | Montagepunkt fuer Antriebsfuss festlegen | 10 min |
| 3 | Montageplatte am Cockpitboden befestigen (4 Edelstahlschrauben) | 20 min |
| 4 | Tiller-Pilot einklinken und Pinnenadapter befestigen | 5 min |
| 5 | 12V-Kabel vom Sicherungskasten zum Cockpit-Stecker verlegen | 30 min |
| 6 | Sicherung installieren (7,5 A) | 5 min |
| 7 | Autopilot einschalten, Grundeinstellungen (Bootstyp, Kieltyp) | 10 min |
| 8 | Kompass-Kalibrierung (Schwenkfahrt) | 15 min |
| **Gesamt** | | **ca. 2 h** |

**Beispiel 2: Below-Deck Linear auf 13 m Segelyacht (Selbsteinbau)**

| Schritt | Arbeitsgang | Zeit |
|---------|------------|------|
| 1 | Ruderquadrant pruefen, Anlenkpunkt festlegen | 30 min |
| 2 | Befestigungspunkte fuer Antrieb am Rumpf/Schott bohren und vorbereiten | 60 min |
| 3 | Linearantrieb mit Kugelgelenken montieren | 45 min |
| 4 | Ruderfeedback-Sensor am Ruderschaft montieren | 45 min |
| 5 | Kurscomputer an trockener Stelle montieren | 30 min |
| 6 | Heading-Sensor montieren (Mindestabstaende pruefen!) | 30 min |
| 7 | Leistungskabel Antrieb → Batterie verlegen (6 mm^2 bei 12V) | 45 min |
| 8 | NMEA2000-Backbone verlegen (falls noch nicht vorhanden) | 60 min |
| 9 | Alle Komponenten an NMEA2000 anschliessen | 30 min |
| 10 | Bedieneinheit im Cockpit montieren (wasserdicht!) | 30 min |
| 11 | Kabel zum Cockpit verlegen | 30 min |
| 12 | Grundeinstellungen (Bootstyp, Kieltyp, Antriebstyp) | 15 min |
| 13 | Ruderfeedback kalibrieren (Mitte, BB, StB) | 15 min |
| 14 | Kompass-Kalibrierung (Schwenkfahrt) | 20 min |
| 15 | Autopilot-Lernfahrt (Sea Trial) | 30 min |
| 16 | Feinabstimmung (Response Level, Ruderlimit, Deadband) | 30 min |
| **Gesamt** | | **ca. 8 h** |

**Beispiel 3: Hydraulik-Autopilot auf 18 m Motoryacht (Fachbetrieb)**

| Schritt | Arbeitsgang | Zeit |
|---------|------------|------|
| 1 | Bestandsaufnahme Hydrauliksteuerung, Leitungen, Platz | 60 min |
| 2 | Hydraulikpumpe montieren und in Kreislauf integrieren | 180 min |
| 3 | Hydraulikleitungen und Fittings anschliessen | 120 min |
| 4 | Bypass-Ventil installieren (falls nicht vorhanden) | 60 min |
| 5 | Kurscomputer, Heading-Sensor, Ruderfeedback montieren | 90 min |
| 6 | Leistungskabel verlegen (10 mm^2, direkt zur Batterie) | 60 min |
| 7 | NMEA2000-Integration mit vorhandenem System | 60 min |
| 8 | Bedieneinheit(en) montieren | 45 min |
| 9 | Hydrauliksystem befuellen und entlueften | 60 min |
| 10 | Lecktest (System unter Druck, 30 min warten) | 45 min |
| 11 | Grundeinstellungen und Kalibrierung | 30 min |
| 12 | Sea Trial und Feinabstimmung | 60 min |
| **Gesamt** | | **ca. 14 h** |

---

### ANHANG R4 — Hydraulikfluid-Kompatibilitaetstabelle

| Hersteller | Empfohlenes Fluid | Alternative | NICHT kompatibel |
|------------|-------------------|-------------|------------------|
| Raymarine | Dexron II/III ATF | Dexron VI, Mercon V | DOT Bremsfluessigkeit, Silikonoel |
| Simrad | Dexron II/III ATF | Dexron VI, Mercon V | DOT, Silikonoel |
| B&G | Dexron II/III ATF | Dexron VI | DOT, Silikonoel |
| Garmin | Dexron III ATF | Dexron VI | DOT, Silikonoel, Pflanzenoel |
| Furuno | ISO VG 15 Hydraulikoel | Dexron III (einige Modelle) | DOT, Silikonoel |
| Lecomble & Schmitt | Hydraulikoel HLP 22 | Dexron III | DOT, Pflanzenoel |
| Kobelt | Dexron III ATF | Dexron VI | DOT |

**ACHTUNG:** Verschiedene Fluids niemals mischen! Beim Wechsel: System vollstaendig spuelen.

**Hydraulikfluid-Kontrolle:**
- Farbe frisch: rot (ATF) oder gelblich (Hydraulikoel)
- Farbe alt: dunkelbraun bis schwarz → Wechsel erforderlich
- Truebung: Wasser im System → Ursache finden, Fluid wechseln
- Partikel sichtbar: Verschleiss im System → Werkstatt
- Geruch: verbrannt → Ueberhitzung → Ursache pruefen, Fluid wechseln

---

### ANHANG R4 — NMEA2000-Geraeteadressen und Instanzen (Empfehlung)

Fuer eine saubere Autopilot-Installation empfehlen sich folgende NMEA2000-Geraete-Instanzen:

| Geraet | Empfohlene Instanz | Prioritaet | Bemerkung |
|--------|-------------------|-----------|-----------|
| Primaerer Heading-Sensor | 0 | Hoechste | Primaere Kompassquelle fuer Autopilot |
| Sekundaerer Heading-Sensor | 1 | Niedrig | Backup, nur bei Ausfall Instanz 0 |
| Ruderfeedback-Sensor | 0 | Hoechste | Primaerer Feedback |
| GPS-Empfaenger | 0 | Hoechste | Primaere GPS-Quelle |
| Windsensor | 0 | Hoechste | Primaere Windquelle |
| Kurscomputer | — | — | Empfaengt Daten, Instanz irrelevant |
| Kartenplotter (XTE-Quelle) | 0 | Hoechste | Primaere Navigationsquelle |

**Instanz-Konfiguration:**
- Bei mehreren Geraeten gleichen Typs (z.B. zwei GPS): unterschiedliche Instanzen zuweisen
- Autopilot-Kurscomputer als "bevorzugte Quelle" konfigurieren (per Hersteller-Software)
- Doppelte Instanzen fuehren zu Datenkonflikten und unvorhersehbarem Autopilot-Verhalten

---

### ANHANG R5 — Checkliste fuer AYDI Autopilot-Bewertung

Diese Checkliste wird vom AYDI-Analysemodul verwendet, um eine systematische Autopilot-Bewertung durchzufuehren:

```
AYDI Autopilot Assessment Checklist v1.0

[ ] 1. SYSTEMIDENTIFIKATION
  [ ] Hersteller und Modell identifiziert
  [ ] Kurscomputer-Modell und Firmware-Version
  [ ] Antriebseinheit Typ und Modell
  [ ] Heading-Sensor Typ
  [ ] Ruderfeedback-Sensor Typ
  [ ] Bedieneinheit(en) Modell(e)
  [ ] Bus-System (NMEA2000/SeaTalkng/proprietaer)
  [ ] Installationsjahr (geschaetzt oder bekannt)

[ ] 2. DIMENSIONIERUNGSPRUEFUNG
  [ ] Bootstyp, LOA, Verdraengung erfasst
  [ ] Steuerungstyp (Pinne/Rad/Hydraulik) erfasst
  [ ] Antrieb-Dimensionierung geprueft (Kraft/Moment vs. Bootsgroesse)
  [ ] Einsatzgebiet beruecksichtigt (Kuestenfahrt/Offshore/Blauwasser)
  [ ] Dimensionierung: korrekt / unterdimensioniert / ueberdimensioniert

[ ] 3. INSTALLATIONSQUALITAET
  [ ] Antrieb-Befestigung: stabil, spielfrei
  [ ] Feedback-Sensor: mechanisch spielfrei, kalibriert
  [ ] Heading-Sensor: Mindestabstaende zu Stoerquellen
  [ ] Kabelquerschnitte: korrekt fuer Antriebsstrom
  [ ] Sicherungen: korrekt dimensioniert, zugaenglich
  [ ] NMEA2000: Terminatoren, Backbone korrekt, Stichleitungen <6 m
  [ ] Hydraulik (falls zutreffend): dicht, entlueftet, Bypass vorhanden

[ ] 4. ZUSTANDSBEWERTUNG
  [ ] Antrieb-Zustand: Motor, Getriebe, Kupplung
  [ ] Feedback-Sensor: Funktion, Kalibrierung
  [ ] Kompass-Deviation: <3 Grad auf allen Kursen?
  [ ] Hydraulikfluid: Farbe, Fuellstand
  [ ] Kabelverbindungen: Korrosion, Zugentlastung
  [ ] NMEA2000-Stecker: Korrosion, Sitz
  [ ] Bedieneinheit: Display, Tasten, Dichtigkeit

[ ] 5. FUNKTIONSPRUEFUNG
  [ ] Heading-Hold: steuert korrekt, Genauigkeit +-3 Grad
  [ ] Wind-Modus (falls verfuegbar): reagiert auf Wind
  [ ] Track-Modus (falls verfuegbar): folgt Route
  [ ] Kupplung/Bypass: manuelles Steuern moeglich
  [ ] Off-Course-Alarm: ausloest bei >15 Grad Abweichung
  [ ] Fernbedienung (falls vorhanden): funktioniert

[ ] 6. ENERGIEANALYSE
  [ ] Durchschnittlicher Stromverbrauch gemessen/geschaetzt
  [ ] Bordspannung unter Last ausreichend
  [ ] Batteriekapazitaet ausreichend fuer Einsatzprofil
  [ ] Solaranlage/Windgenerator deckt Autopilot-Verbrauch (bei Langfahrt)

[ ] 7. REDUNDANZ UND SICHERHEIT
  [ ] Backup-System vorhanden? (Tiller-Pilot, Windsteueranlage)
  [ ] Notpinne vorhanden und zugaenglich?
  [ ] Notabschaltung (Standby-Taste) schnell erreichbar?
  [ ] MOB-Funktion vorhanden und getestet?
```

---

*Ende der Wissensdatei 14.05 — Autopilot-Systeme im Yachtbau*