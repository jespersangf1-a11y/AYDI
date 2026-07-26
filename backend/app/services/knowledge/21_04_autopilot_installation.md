# 21.04 — Autopilot Installation und Kalibrierung: Einbau, Verkabelung, NMEA 2000, Kalibrierung, Kompass-Deviation

> **AYDI Wissensdatei 21.04** — Kategorie 21: Autopiloten und Kurssteuerung
> **Confidence-Quelle:** measured (Hersteller-Datenblätter, ISO-Normen), documented (Installations-Handbücher, Fachliteratur, Werft-Praxis), estimated (Erfahrungswerte Werft/Eigner)
> **Letzte Aktualisierung:** 2026-05-03

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

### 1.1 Warum professionelle Installation entscheidend ist

Ein Autopilot ist nur so gut wie seine Installation. Das teuerste System der Welt wird versagen, wenn:

- Der Kompass neben dem Lautsprecher-Magneten montiert ist
- Das Stromkabel zu dünn dimensioniert ist und bei Volllast 3 V abfallen
- Der Rudersensor mechanisches Spiel hat
- Der NMEA-2000-Bus kein korrektes Backbone besitzt
- Die Hydraulikleitungen Luft enthalten

**Statistik aus der Werft-Praxis (documented, Erfahrungswerte 2015–2025):**

| Fehlerursache | Anteil an Autopilot-Reklamationen |
|---------------|----------------------------------|
| Fehlerhafte Elektrik / Kabelquerschnitt | 28 % |
| Kompass-Deviation / Störquellen | 22 % |
| Rudersensor-Fehlkalibrierung | 18 % |
| NMEA-2000/SeaTalk-Busfehler | 14 % |
| Mechanische Einbaufehler (Antrieb) | 10 % |
| Software-/Firmware-Konfiguration | 5 % |
| Defekte Komponenten (ab Werk) | 3 % |

**Kernaussage:** Über 90 % aller Autopilot-Probleme sind Installationsfehler — nicht Gerätedefekte. Die Investition in eine professionelle Installation spart langfristig Zeit, Geld und Nerven.

### 1.2 Geltungsbereich dieser Wissensdatei

Diese Datei behandelt ausschließlich die **Installation und Kalibrierung** von Autopilot-Systemen. Für Grundlagen (Funktionsprinzip, Regelungstechnik, PID-Regler) siehe 21.01, für Hersteller-Vergleiche siehe 21.02, für Windfahnen-Selbststeueranlagen siehe 21.03, für Wartung siehe 21.05.

**Abgedeckte Themen:**
- Mechanischer Einbau aller Antriebstypen (hydraulisch, linear, Radsteuerung, Pinne)
- Elektrische Verkabelung inkl. Leiterquerschnitt-Berechnung und Spannungsabfall
- NMEA 2000 Backbone-Aufbau und SeaTalk-NG/SeaTalk1-Integration
- Kompass-Aufstellung, magnetische Störquellen, Kompass-Deviation
- Kalibrierung: Compass-Swing, Rudersensor, Seatrial-Abstimmung
- Retrofit-Spezifika: Nachrüstung in bestehende Boote
- Fehlermuster bei der Installation und deren Vermeidung

### 1.3 Relevante Normen und Standards

| Norm | Titel | Relevanz für Installation |
|------|-------|--------------------------|
| ISO 11674:2019 | Autopiloten (Heading Control Systems) — Prüfung und Anforderungen | Mindestanforderungen an Antriebsleistung, Ansprechzeit |
| NMEA 2000 / IEC 61162-3 | Maritime Datennetze | Bus-Topologie, Kabelspezifikation, Terminierung |
| ABYC E-11 | AC und DC Elektrische Systeme | Leiterquerschnitte, Absicherung, Spannungsabfall |
| ISO 10133:2012 | Elektrische Gleichstromsysteme ≤50V | Kabelführung, Absicherung, Erdung |
| ISO 13297:2014 | Elektrische Systeme Wechselstrom | Relevant bei 24V-Systemen mit Ladegeräten |
| ISO 11812:2020 | Cockpits | Durchführungen für Kabel durch wasserdichte Schotten |
| IEC 60945:2002 | Maritime Navigationsausrüstung — Allgemein | EMV-Anforderungen, Kompass-Sicherheitsabstand |
| ISO 694:2000 | Kompass-Sicherheitsabstände | Mindestabstände elektrischer Geräte zum Magnetkompass |

### 1.4 Installations-Planungsphasen

Eine professionelle Autopilot-Installation folgt einem strukturierten Prozess:

**Phase 1 — Bestandsaufnahme (2–4 Stunden)**
- Boot vermessen: Ruderlager-Position, Quadrant/Tiller-Geometrie, verfügbarer Platz
- Bestehendes Steuerungssystem dokumentieren: Hydraulik oder mechanisch, Seilzug oder Gestänge
- Elektrisches System bewerten: Batterie-Kapazität, verfügbare Absicherung, Kabelwege
- NMEA-Netzwerk prüfen: vorhandene Sensoren, Bus-Topologie, freie Anschlüsse
- Magnetische Vermessung: Störquellen identifizieren, Kompass-Standort evaluieren

**Phase 2 — Systemauswahl (1–2 Stunden)**
- Antriebstyp basierend auf Steuerungssystem und Bootsgröße
- Kompass-Typ basierend auf Einbauort und Störumgebung
- Controller und Bedieneinheiten basierend auf Cockpit-Layout
- NMEA-2000-Komponenten (Backbone, T-Stücke, Terminatoren)

**Phase 3 — Mechanische Installation (4–12 Stunden)**
- Antrieb montieren und ausrichten
- Rudersensor installieren
- Kompass montieren
- Bedieneinheiten einbauen

**Phase 4 — Elektrische Installation (4–8 Stunden)**
- Stromversorgung: Kabel, Sicherungen, Hauptschalter
- NMEA-2000-Bus aufbauen oder erweitern
- Sensorverkabelung
- Steuerleitungen

**Phase 5 — Kalibrierung und Seatrial (3–6 Stunden)**
- Rudersensor kalibrieren
- Compass-Swing durchführen
- PID-Parameter Grundeinstellung
- Seatrial unter verschiedenen Bedingungen

**Phase 6 — Dokumentation (1–2 Stunden)**
- Installationsprotokoll
- Schaltplan
- Kalibrierungswerte
- Einweisung des Eigners

**Gesamtzeitaufwand:** 15–34 Stunden je nach Komplexität und Bootstyp.

---

## 2. Grundlagen und Theorie

### 2.1 NMEA 2000 — Das Rückgrat des modernen Autopiloten

#### 2.1.1 Bus-Topologie

NMEA 2000 ist ein Controller Area Network (CAN-Bus) nach ISO 11783-5. Das Grundprinzip:

```
Terminator ──── Backbone ──── T-Stück ──── T-Stück ──── T-Stück ──── Terminator
                                 │              │              │
                              Drop-Kabel     Drop-Kabel     Drop-Kabel
                                 │              │              │
                              Gerät 1        Gerät 2        Gerät 3
```

**Backbone-Regeln (NMEA 2000 Standard):**

| Parameter | Spezifikation | Anmerkung |
|-----------|---------------|-----------|
| Max. Backbone-Länge | 100 m (Micro) / 200 m (Mid) | Micro = DeviceNet Micro, häufigster Standard |
| Max. Drop-Kabel-Länge | 6 m (Micro) | Von T-Stück bis Gerät |
| Max. Geräte pro Netzwerk | 50 | Praktisch selten >25 auf Yachten |
| Datenrate | 250 kbit/s | CAN 2.0B Standard |
| Terminierung | 120 Ω an beiden Enden | Ohne Terminierung: Bus-Fehler |
| Stromversorgung | 9–16 V DC über Bus | Max. 3 A gesamt |
| Kabeltyp Backbone | 5-adriges geschirmtes Kabel | Shield, NET-S (Strom), NET-C (Masse), CAN-H, CAN-L |
| Kabeltyp Drop | 5-adriges geschirmtes Kabel | Dünnerer Querschnitt als Backbone erlaubt |

**Kritische Installationsregeln:**

1. **Stern-Topologie ist verboten.** NMEA 2000 ist ein linearer Bus (Daisy-Chain). Sternförmige Abzweige verursachen Reflexionen und Busfehler.
2. **Beide Enden müssen terminiert sein.** Ein fehlender Terminator verursacht intermittierende Kommunikationsfehler — das tückischste aller NMEA-2000-Probleme.
3. **Backbone-Kabel nicht knicken.** Minimaler Biegeradius: 50 mm. Knicke beschädigen den Schirm und verursachen EMV-Probleme.
4. **Drop-Kabel so kurz wie möglich.** Lange Drop-Kabel (>3 m) verursachen Signalqualitätsprobleme.
5. **Schirm nur an einem Punkt erden.** Mehrfacherdung des Schirms erzeugt Erdschleifen und EMV-Störungen.

#### 2.1.2 NMEA 2000 PGN-Nummern für Autopilot-Systeme

| PGN | Name | Beschreibung | Sender | Empfänger |
|-----|------|-------------|--------|-----------|
| 127245 | Rudder | Aktuelle Ruderposition in Grad | Rudersensor | Autopilot-Controller |
| 127250 | Vessel Heading | Magnetischer / wahrer Kurs | Kompass / IMU | Autopilot-Controller |
| 127251 | Rate of Turn | Drehrate in °/s | IMU / Ratekompass | Autopilot-Controller |
| 127257 | Attitude | Roll, Pitch, Yaw | IMU | Autopilot-Controller |
| 127258 | Magnetic Variation | Ortsmissweisung | GPS / Kartenplotter | Autopilot-Controller |
| 128259 | Speed, Water Referenced | Fahrt durchs Wasser | Log / Paddelrad | Autopilot-Controller |
| 129025 | Position, Rapid Update | Lat/Lon @ 10 Hz | GPS | Autopilot-Controller |
| 129026 | COG & SOG, Rapid Update | Kurs/Geschwindigkeit über Grund | GPS | Autopilot-Controller |
| 129283 | Cross Track Error | Querabweichung vom Kurs | GPS / Plotter | Autopilot-Controller |
| 129284 | Navigation Data | Wegpunkt-Informationen | Plotter | Autopilot-Controller |
| 065379 | Autopilot Command | Kursbefehl an Antrieb | Controller | Drive-Unit |
| 126208 | NMEA Request/Command | Steuerkommandos | Diverse | Diverse |
| 126720 | Proprietary (Fast) | Herstellerspezifisch (z.B. Raymarine EV) | Diverse | Diverse |

#### 2.1.3 SeaTalk-NG vs. NMEA 2000

SeaTalk-NG (Raymarine) ist physisch kompatibel mit NMEA 2000, nutzt aber proprietäre PGNs für erweiterte Funktionen:

| Merkmal | NMEA 2000 Standard | SeaTalk-NG | Kompatibilität |
|---------|-------------------|------------|----------------|
| Physischer Anschluss | DeviceNet Micro | Eigenes Stecksystem | Adapter A06045 erforderlich |
| Backbone-Kabel | Standard NMEA 2000 | SeaTalk-NG Backbone-Kabel | Kompatibel (5-adrig geschirmt) |
| Standard-PGNs | Ja | Ja | Vollständig |
| Erweiterte Funktionen | Nein | Proprietäre PGNs (126720) | Nur Raymarine-Geräte |
| Stromversorgung über Bus | Ja (max. 3A) | Ja (LEN-basiert) | Kompatibel |
| T-Stücke | DeviceNet Micro | SeaTalk-NG T-Stücke | Adapter erforderlich |

**Praxisempfehlung:** Bei Raymarine-Systemen SeaTalk-NG als Backbone nutzen und NMEA-2000-Fremdgeräte über Adapter A06045/A06075 einbinden. Bei Mischsystemen (z.B. Garmin Plotter + Raymarine Autopilot) reinen NMEA-2000-Backbone verwenden.

#### 2.1.4 NMEA 2000 Stromversorgung

Der NMEA-2000-Bus liefert 12V DC über das Backbone-Kabel. Geräte werden über den Bus gespeist, sofern ihr LEN (Load Equivalence Number) im Budget liegt:

- 1 LEN = 50 mA
- Max. Bus-Strom: 3 A = 60 LEN
- Typische LEN-Werte: GPS (4 LEN), Kompass (2 LEN), Rudersensor (1 LEN), Plotter (8 LEN)

**Achtung:** Autopilot-Controller und Drive-Units werden NICHT über den NMEA-2000-Bus gespeist. Sie benötigen eine eigene, dedizierte Stromversorgung direkt von der Batterie.

### 2.2 Elektrische Verkabelung

#### 2.2.1 Spannungsabfall-Berechnung

Der Spannungsabfall in der Zuleitung zum Autopilot-Antrieb ist der häufigste Installationsfehler. Die Formel:

```
U_drop = (2 × L × I × ρ) / A

Wobei:
  U_drop = Spannungsabfall in Volt
  L      = einfache Kabellänge in Metern (Hin- ODER Rückleitung)
  I      = Strom in Ampere
  ρ      = spezifischer Widerstand Kupfer = 0,0178 Ω·mm²/m bei 20°C
  A      = Leiterquerschnitt in mm²
  Faktor 2 = Hin- und Rückleitung
```

**Maximaler zulässiger Spannungsabfall nach ABYC E-11:**

| Anwendung | Max. Spannungsabfall | Bei 12V = | Bei 24V = |
|-----------|---------------------|-----------|-----------|
| Kritische Systeme (Navigation, Autopilot) | 3 % | 0,36 V | 0,72 V |
| Allgemeine Systeme | 10 % | 1,20 V | 2,40 V |

**Berechnungsbeispiel:**
- Autopilot-Antrieb: 20 A Peak, 12V-System
- Kabellänge: 8 m (einfach, von Batterie bis Antrieb)
- Gewählter Querschnitt: 10 mm²

```
U_drop = (2 × 8 × 20 × 0,0178) / 10
U_drop = (5,696) / 10
U_drop = 0,57 V = 4,75 % → ZU HOCH!
```

Lösung: 16 mm² verwenden:
```
U_drop = (2 × 8 × 20 × 0,0178) / 16
U_drop = 0,356 V = 2,97 % → OK (knapp unter 3 %)
```

**Empfehlung:** Immer eine Querschnittsstufe größer wählen als die Minimalberechnung ergibt.

#### 2.2.2 Leiterquerschnitt-Tabelle für Autopilot-Antriebe

| Antriebsstrom (Peak) | Kabellänge 4m | 6m | 8m | 10m | 12m | 15m |
|-----------------------|---------------|-----|-----|------|------|------|
| 10 A | 4 mm² | 6 mm² | 6 mm² | 10 mm² | 10 mm² | 16 mm² |
| 15 A | 6 mm² | 10 mm² | 10 mm² | 16 mm² | 16 mm² | 25 mm² |
| 20 A | 10 mm² | 10 mm² | 16 mm² | 16 mm² | 25 mm² | 25 mm² |
| 25 A | 10 mm² | 16 mm² | 16 mm² | 25 mm² | 25 mm² | 35 mm² |
| 30 A | 16 mm² | 16 mm² | 25 mm² | 25 mm² | 35 mm² | 35 mm² |
| 40 A | 16 mm² | 25 mm² | 25 mm² | 35 mm² | 35 mm² | 50 mm² |
| 50 A | 25 mm² | 25 mm² | 35 mm² | 50 mm² | 50 mm² | 70 mm² |
| 60 A (hydraulisch) | 25 mm² | 35 mm² | 50 mm² | 50 mm² | 70 mm² | 70 mm² |

*Werte basierend auf max. 3 % Spannungsabfall bei 12V. Bei 24V-Systemen können die Querschnitte um eine Stufe reduziert werden. (confidence: calculated)*

#### 2.2.3 Absicherung

| Komponente | Sicherungstyp | Dimensionierung | Position |
|------------|--------------|-----------------|----------|
| Autopilot-Antrieb | ANL-Sicherung (träge) | 150 % des Nennstroms | Max. 200 mm von Batterie |
| Autopilot-Controller | Blade-Sicherung | 10–15 A (je nach Modell) | Schaltpanel oder eigene Halterung |
| NMEA-2000-Bus | Blade-Sicherung | 3–5 A | Eigene Halterung am Stromeingang |
| Bedieneinheiten | Über Controller gespeist | — | — |
| Rudersensor | Über NMEA-2000-Bus | — | — |

**Wichtig:** Die Sicherung am Antrieb muss **träge** (slow-blow / time-delay) sein. Beim Anlaufen zieht der Motor kurzzeitig das 3–5-fache des Nennstroms. Eine flinke Sicherung löst bei jedem Kurskorrektur-Impuls aus.

#### 2.2.4 Kabel-Spezifikationen

| Parameter | Anforderung | Anmerkung |
|-----------|-------------|-----------|
| Leitertyp | Mehrdrähtiger Kupferleiter (feindrähtig) | Keine Massivleiter auf Booten (Vibration!) |
| Verzinnung | Verzinntes Kupfer | Pflicht im Marinebereich (Korrosionsschutz) |
| Isolierung | PVC oder XLPE, 90°C-beständig | Motorraum: 105°C-beständig |
| Farbe | Rot = Plus, Schwarz/Gelb = Masse | ABYC-Farbcode beachten |
| Kabelenden | Ringkabelschuhe, gecrimpt + verlötet | Schraubklemmen nur mit Kabelschuhen |
| Crimpen | Professionelle Crimp-Zange (hexagonal) | Zangencrimpen ist nicht normgerecht |
| Schrumpfschlauch | Klebend, mit Kleber ausgefüttert | Über jede Crimp-Verbindung |
| Kabelführung | Befestigt alle 300 mm, Biegeradius >8× Durchmesser | Keine freihängenden Kabel |
| Kabeldurchführung | Wasserdichte Kabelverschraubung (IP67+) | An jedem Schott und Decksdurchbruch |

#### 2.2.5 Erdung und EMV

**Erdungskonzept für Autopilot-Installation:**

```
Batterie (–) ──── Hauptmassesammelschiene ──── Autopilot-Antrieb (–)
                        │                             │
                        ├── Motor-Masse               ├── Controller (–)
                        │                             │
                        ├── NMEA-2000 Power (–)        ├── Schirmung (1 Punkt!)
                        │
                        └── Bonding-System (SSM)
```

**EMV-Maßnahmen:**

1. **Getrennte Kabelwege:** Starkstrom-Kabel (Antrieb) und Signal-Kabel (NMEA, Kompass) mind. 200 mm Abstand oder kreuzend bei 90°
2. **Schirmung:** NMEA-2000-Kabel nur einseitig erden (am Stromeingang des Bus)
3. **Ferritkerne:** Bei EMV-Problemen Ferritkerne auf die Antriebskabel (3 Windungen)
4. **Keine gemeinsamen Kabelwege:** Autopilot-Kabel nicht im gleichen Bündel wie UKW-Funk oder SSB-Kabel
5. **Motorstörungen:** Entstörfilter am Autopilot-Antrieb, wenn Motor-Lichtmaschine Störungen verursacht

### 2.3 Kompass-Aufstellung und magnetische Störquellen

#### 2.3.1 Grundprinzip der Kompass-Aufstellung

Der Heading-Sensor (Kompass) ist die kritischste Komponente der Autopilot-Installation. Ein um 5° fehlerhafter Kompass führt dazu, dass der Autopilot permanent 5° daneben steuert — und vergeblich versucht, den Kurs zu halten, indem er permanent Ruder legt.

**Anforderungen an den Kompass-Standort:**

| Kriterium | Minimum | Ideal | Anmerkung |
|-----------|---------|-------|-----------|
| Abstand zu Lautsprechern | 1,0 m | 2,0 m | Permanentmagneten! Stärkste Störquelle an Bord |
| Abstand zu Elektromotoren | 1,0 m | 1,5 m | Anlasser, Winschen, Bugstrahlruder |
| Abstand zu Stahl/Eisen | 0,5 m | 1,0 m | Keel-Bolzen, Kette, Werkzeug, Konserven |
| Abstand zu DC-Kabeln (>10A) | 0,3 m | 0,5 m | Magnetfeld proportional zum Strom |
| Abstand zu VHF/SSB-Antenne | 1,0 m | 2,0 m | EMV-Strahlung bei Sendebetrieb |
| Abstand zum eigenen Antriebskabel | 0,5 m | 1,0 m | Das eigene Antriebskabel stört den Kompass! |
| Montagefläche | Fest, vibrationsfrei | GFK-Schott | Keine flexible Fläche, kein Holzschott |
| Ausrichtung | ±2° zur Schiffslängsachse | ±0,5° | Markierung auf Sensor und Boot |
| Neigung | ±5° Krängung tolerierbar | Waagerecht | Gimbal-Kompasse tolerieren bis ±25° |

#### 2.3.2 Magnetische Störquellen — Systematische Übersicht

**Kategorie 1: Permanentmagneten (stärkste Störung, konstant)**

| Quelle | Typische Feldstärke | Sicherheitsabstand | Häufigkeit |
|--------|--------------------|--------------------|------------|
| Lautsprecher (20 W) | 50–200 mT am Magneten | 1,5–2,0 m | Sehr häufig |
| Lautsprecher (100 W Subwoofer) | 200–500 mT | 2,5–3,0 m | Häufig auf Motoryachten |
| Magnetverschlüsse (Schränke) | 10–50 mT | 0,3–0,5 m | Sehr häufig, oft übersehen |
| Tablet/Smartphone-Hülle | 5–30 mT | 0,2–0,3 m | Häufig, temporär |
| Kühlschrank-Kompressor | 20–100 mT | 1,0–1,5 m | Häufig |
| Werkzeug (magnetisiert) | Variabel | 0,5–1,0 m | Gelegentlich, temporär |
| Magnetische Bildhalter | 10–30 mT | 0,3–0,5 m | Oft übersehen |

**Kategorie 2: Ferromagnetische Materialien (konstante Deviation)**

| Quelle | Typische Auswirkung | Sicherheitsabstand | Anmerkung |
|--------|--------------------|--------------------|-----------|
| Ballastkiel (Gusseisen) | 2–15° Deviation | Sensor möglichst hoch montieren | Nicht vermeidbar, wird kompensiert |
| Ankerkette (Stahl) | 3–10° | 2,0 m | Variiert mit Kettenmenge im Kasten |
| Eiserne Kielbolzen | 2–8° | 1,0 m | Konstant, gut kompensierbar |
| Gasflaschen (Stahl) | 1–5° | 1,0 m | Variiert mit Füllstand! |
| Konservendosen-Lager | 1–3° | 0,5 m | Variiert mit Menge → schlecht kompensierbar |
| Stahlschäkel/-Blöcke | 0,5–2° | 0,3 m | Oft vergessen |
| Motorblock (Stahl/Guss) | 5–20° | 2,0 m | Starke, konstante Quelle |

**Kategorie 3: Elektromagnetische Felder (variable Störung, am tückischsten)**

| Quelle | Typische Auswirkung | Sicherheitsabstand | Anmerkung |
|--------|--------------------|--------------------|-----------|
| Lichtmaschine (laufender Motor) | 1–5° | 2,0 m | Stört nur bei laufendem Motor |
| Bugstrahlruder-Kabel (>100 A) | 3–10° | 1,0 m | Stört nur bei Betrieb — kurzzeitig |
| Ankerwinde-Kabel (>50 A) | 2–5° | 0,5 m | Stört nur bei Betrieb |
| LED-Dimmer (PWM) | 0,5–3° | 0,3 m | Hochfrequente Störung |
| SSB-Funk (Sendebetrieb) | 2–10° | 2,0 m | Stört nur bei Sendebetrieb |
| VHF-Funk (25 W) | 0,5–2° | 1,0 m | Stört nur bei Sendebetrieb |
| Kühlschrank (Ein/Aus) | 0,5–2° | 1,0 m | Schaltstrom Kompressor |
| Wechselrichter | 1–5° | 1,0 m | Starke EMV-Quelle |

#### 2.3.3 Kompass-Deviation — Theorie

**Definition:** Deviation ist die Differenz zwischen dem vom Kompass angezeigten Kurs und dem tatsächlichen magnetischen Kurs. Sie variiert mit dem Steuerkurs und wird durch magnetische Störquellen am Boot verursacht.

**Mathematisches Modell (Fourier-Reihe):**

```
δ(θ) = A + B·sin(θ) + C·cos(θ) + D·sin(2θ) + E·cos(2θ)

Wobei:
  δ(θ) = Deviation bei Kompass-Kurs θ
  A    = Konstanter Fehler (Fehlausrichtung des Sensors)
  B    = Halbkreis-Deviation durch längsschiffs-unsymmetrisches Weicheisen
  C    = Halbkreis-Deviation durch querschiffs-unsymmetrisches Weicheisen
  D    = Viertelkreis-Deviation durch längsschiffs/querschiffs Weicheisen
  E    = Viertelkreis-Deviation durch diagonales Weicheisen
```

**Koeffizienten und ihre Ursachen:**

| Koeffizient | Periode | Ursache | Kompensation |
|-------------|---------|---------|-------------|
| A | Konstant | Sensor-Fehlausrichtung, unsymmetrische Hartmagnet-Materialien | Mechanische Ausrichtung |
| B | 360° (Sinus) | Längsschiffs Permanentmagnet-Effekt | Elektronische Kompensation |
| C | 360° (Cosinus) | Querschiffs Permanentmagnet-Effekt | Elektronische Kompensation |
| D | 180° (Sinus) | Induzierter Magnetismus längsschiffs | Elektronische Kompensation |
| E | 180° (Cosinus) | Induzierter Magnetismus querschiffs | Elektronische Kompensation |

**Akzeptable Restdeviation nach Kompensation:**

| Kompass-Typ | Max. Restdeviation | Typisch erreichbar |
|-------------|-------------------|-------------------|
| Fluxgate (Standard) | ±5° | ±2–3° |
| Fluxgate (hochwertig) | ±3° | ±1–2° |
| Solid-State IMU (9-Achsen) | ±2° | ±0,5–1° |
| GPS-Kompass (Dual-Antenne) | ±1° | ±0,3–0,5° |

#### 2.3.4 Compass-Swing — Kalibrierungsverfahren

**Vorbereitung:**
1. Boot muss schwimmen (nicht am Steg mit Metallpollern!)
2. Motor aus (sofern im Betrieb nicht laufen wird — ansonsten Motor AN)
3. Alle Elektrik in Betriebszustand (Navigation, Instrumente, Beleuchtung AN)
4. Lose Metallgegenstände in Normalposition (Werkzeug, Gasflaschen, Konserven)
5. Keine Elektronikgeräte auf/neben dem Kompass (Handy, Tablet)
6. Wind <15 kn, keine Strömung >1 kn, ruhiges Wasser
7. Bekannte Landmarken oder GPS-COG als Referenz

**Verfahren — Automatischer Compass-Swing (moderne Systeme):**

1. Kalibrierungsmodus im Controller aktivieren
2. Boot langsam im Kreis drehen (360°), gleichmäßig, ohne Unterbrechung
3. Geschwindigkeit: 1 kompletter Kreis in 90–180 Sekunden
4. System sammelt Messpunkte über alle Richtungen
5. Algorithmus berechnet Kompensationskoeffizienten A–E
6. Restdeviation wird angezeigt
7. Bei Restdeviation >5°: Störquelle suchen und beseitigen, erneut kalibrieren

**Verfahren — Manueller Compass-Swing (ältere Systeme oder Validierung):**

| Kurs (mag.) | Boot auf Kurs bringen | Kompass ablesen | Deviation berechnen |
|-------------|----------------------|-----------------|---------------------|
| 000° (N) | Nach Landmarke oder GPS-COG | z.B. 003° | +3° (Ost) |
| 030° | — | z.B. 032° | +2° |
| 060° | — | z.B. 061° | +1° |
| 090° (E) | — | z.B. 088° | -2° |
| 120° | — | z.B. 118° | -2° |
| 150° | — | z.B. 149° | -1° |
| 180° (S) | — | z.B. 182° | +2° |
| 210° | — | z.B. 213° | +3° |
| 240° | — | z.B. 242° | +2° |
| 270° (W) | — | z.B. 268° | -2° |
| 300° | — | z.B. 298° | -2° |
| 330° | — | z.B. 329° | -1° |

**Auswertung:** Deviation in Deviationstabelle eintragen. Max. Abweichung >±5° → Kompass-Standort überprüfen. Unsymmetrisches Muster (z.B. nur auf 90° stark) → gezielte Störquellensuche in dieser Richtung.

#### 2.3.5 Rudersensor-Kalibrierung

**Sensortypen:**

| Typ | Prinzip | Genauigkeit | Lebensdauer | Anmerkung |
|-----|---------|-------------|-------------|-----------|
| Potentiometer (Drehgeber) | Widerstandsänderung bei Drehung | ±1–2° | 5–10 Jahre | Verschleiß durch Kontaktabrieb |
| Induktiver Sensor (RVDT) | Induktive Kopplung, berührungslos | ±0,5° | 15+ Jahre | Kein Verschleiß, teurer |
| Magnetischer Sensor (Hall) | Hall-Effekt, berührungslos | ±0,5–1° | 15+ Jahre | Empfindlich gegen Fremdmagnete |
| Mechanischer Hebelsensor | Hebel mit Potentiometer | ±2–3° | 5–8 Jahre | Mechanisches Spiel im Gestänge |

**Kalibrierungsverfahren (alle Systeme ähnlich):**

1. **Mittellage (Ruderlage 0°):**
   - Ruder exakt in Mittelposition bringen (Wasserstrahl-Methode oder Augenmaß auf Kiel-Mittelachse)
   - Sensor auf Mittelposition kalibrieren (je nach System: Taster oder Menü)
   - **Genauigkeit hier ist entscheidend!** 2° Offset in der Mitte → Autopilot steuert permanent 2° daneben

2. **Endanschläge (Port/Steuerbord):**
   - Ruder voll Backbord drehen → Backbord-Endanschlag setzen
   - Ruder voll Steuerbord drehen → Steuerbord-Endanschlag setzen
   - System kennt jetzt den vollen Ruderausschlag

3. **Linearitätsprüfung:**
   - Ruder auf 10°, 20°, 30° stellen und mit Anzeige vergleichen
   - Bei >2° Abweichung: mechanisches Spiel in der Sensoranlenkung prüfen

4. **Totband (Deadband):**
   - Das Totband definiert, ab welcher Kursabweichung der Autopilot reagiert
   - Standard: ±1–3° (Segeln: eher 3°, Motoren: eher 1°)
   - Zu klein: permanentes Rudern, hoher Stromverbrauch
   - Zu groß: Boot giert stark, schlechter Kurs

### 2.4 Spannungsabfall in der Praxis — Worst-Case-Szenarien

#### 2.4.1 12V-System unter Last

Ein typisches 12V-System auf einer 40-Fuß-Segelyacht im Seegang:

```
Batteriespannung (Ruhezustand): 12,8 V
Innenwiderstand Batterie unter Last: -0,2 V → 12,6 V
Hauptschalter-Kontaktwiderstand: -0,05 V → 12,55 V
Sicherungshalter-Kontaktwiderstand: -0,05 V → 12,50 V
Kabel (8m, 10mm², 25A Peak): -0,71 V → 11,79 V
Antriebsmotor erhält: 11,79 V (= 7,9 % Spannungsabfall!)
```

**Folgen:** Der Motor liefert nur noch ~85 % seiner Nennleistung. In schwerem Seegang reicht die Kraft nicht, das Boot giert aus, der Autopilot gibt Alarm oder schaltet ab.

**Lösung:** 16 mm²-Kabel reduziert den Kabelabfall auf 0,445 V → 12,05 V am Motor (5,9 %). Besser: 25 mm² → 0,285 V → 12,22 V (4,6 %). Ideal: 24V-System halbiert alle Ströme.

#### 2.4.2 24V-System — Vorteile

| Parameter | 12V-System | 24V-System | Vorteil 24V |
|-----------|-----------|-----------|------------|
| Strom bei 500W Last | 41,7 A | 20,8 A | Halber Strom |
| Kabelquerschnitt (8m, 3%) | 35 mm² | 10 mm² | 1/3 des Querschnitts |
| Kabelgewicht (8m) | 5,6 kg | 1,6 kg | 71 % leichter |
| Kabelkosten | ~120 € | ~40 € | 67 % günstiger |
| Spannungsabfall (absolut, 10mm²) | Unzureichend | 0,59 V (2,5 %) | Akzeptabel |
| Kontaktwiderstände | Relevant bei 40A | Vernachlässigbar bei 20A | Zuverlässiger |

### 2.4.3 Energiebilanz-Berechnung für Autopilot-Betrieb

Vor jeder Installation muss die Energiebilanz geprüft werden. Der Autopilot ist einer der größten Einzelverbraucher an Bord:

**Typische Stromverbräuche (Durchschnitt, 12V-System):**

| Antriebstyp | Ruhige See | Mäßiger Seegang (BF 4) | Schwerer Seegang (BF 6) | 24h-Verbrauch (geschätzt) |
|-------------|-----------|------------------------|------------------------|--------------------------|
| Tiller-Pilot | 1,0 A | 2,0 A | 3,5 A | 24–48 Ah |
| Linearantrieb (klein) | 1,5 A | 3,0 A | 5,0 A | 36–72 Ah |
| Linearantrieb (mittel) | 2,0 A | 4,0 A | 7,0 A | 48–96 Ah |
| Linearantrieb (groß) | 3,0 A | 6,0 A | 10,0 A | 72–144 Ah |
| Hydraulikpumpe (klein) | 2,0 A | 5,0 A | 10,0 A | 48–120 Ah |
| Hydraulikpumpe (mittel) | 3,0 A | 7,0 A | 15,0 A | 72–180 Ah |
| Hydraulikpumpe (groß) | 5,0 A | 10,0 A | 20,0 A | 120–240 Ah |

*Werte geschätzt aus Herstellerangaben und Praxiserfahrung. Tatsächlicher Verbrauch hängt stark von Boot-Balance, Seegang, PID-Einstellung und Ruderwiderstand ab. (confidence: estimated)*

**Energiebilanz-Beispiel: 40-ft-Segelyacht auf 24h-Passage**

| Verbraucher | Strom (A) | Betriebsdauer (h) | Verbrauch (Ah) |
|------------|-----------|-------------------|----------------|
| Autopilot (Linear, mittel) | 4,0 | 20 | 80 |
| Kartenplotter | 1,5 | 24 | 36 |
| Instrumente (Wind, Depth, Log) | 0,8 | 24 | 19 |
| Positionslichter | 2,0 | 12 | 24 |
| Ankerlicht | 0,3 | 0 | 0 |
| AIS-Transponder | 0,5 | 24 | 12 |
| VHF-Funk (Standby) | 0,3 | 24 | 7 |
| Kühlschrank | 4,0 | 10 | 40 |
| Beleuchtung Innen | 1,5 | 6 | 9 |
| Diverse (USB-Laden, etc.) | 1,0 | 12 | 12 |
| **Summe Verbrauch** | | | **239 Ah** |

| Erzeuger | Strom (A) | Ladezeit (h) | Erzeugung (Ah) |
|----------|-----------|-------------|----------------|
| Lichtmaschine (80A) | 50 (effektiv) | 3 | 150 |
| Solar (200 Wp) | 7 (Durchschnitt) | 8 | 56 |
| Windgenerator (optional) | 5 (Durchschnitt) | 12 | 60 |
| **Summe Erzeugung** | | | **206–266 Ah** |

**Bewertung:** Ohne Windgenerator: 206 Ah Erzeugung vs. 239 Ah Verbrauch → **Negativ!** Batterie verliert täglich ~33 Ah. Bei 200 Ah Kapazität (50% nutzbar = 100 Ah): nach 3 Tagen kritisch.

**Lösungen:**
1. Motor 1h länger laufen (+50 Ah)
2. Solar aufrüsten (300 Wp → +28 Ah)
3. Windgenerator installieren (+60 Ah)
4. Auf 24V umstellen (Autopilot-Verbrauch sinkt um 20–30%)
5. AP-Einstellung optimieren (Gain reduzieren, Totband vergrößern → 20% weniger Verbrauch)

### 2.5 Hydraulik-Grundlagen für Autopilot-Installation

#### 2.5.1 Hydrauliksystem-Architektur

```
                    Bypass-Ventil
                    ┌──[BV]──┐
                    │         │
Autopilot-     ────┤         ├──── Steuer-
Pumpe               │         │     zylinder
(reversibel)  ────┤         ├────
                    │         │
                    └─────────┘
                    
                    Helm-Pumpe
                    (manuell)
```

**Komponenten:**

| Komponente | Funktion | Einbauort |
|------------|----------|-----------|
| Autopilot-Pumpe | Erzeugt Hydraulikdruck zum Ruderdrehen | Nah am Steuerzylinder |
| Steuerzylinder | Wandelt Hydraulikdruck in Ruderbewegung | Am Ruderquadranten/Tillerhebel |
| Helm-Pumpe | Manuelle Steuerung durch den Rudergänger | Am Steuerrad |
| Bypass-Ventil | Trennt AP-Pumpe von manuellem System | Nahe AP-Pumpe |
| Hydraulikleitungen | Verbinden Pumpe ↔ Zylinder | Kürzestmöglicher Weg |
| Vorratsbehälter | Hydraulikölreservoir | Höchster Punkt im System |
| Entlüftungsventil | Entfernt Luft aus dem System | Am Zylinder (höchster Punkt) |

#### 2.5.2 Hydraulikflüssigkeit

| Typ | Anwendung | Farbe | Mischbar | Temperaturbereich |
|-----|-----------|-------|----------|-------------------|
| Mineral-Hydrauliköl (HLP 15/22) | Teleflex/SeaStar, Vetus | Klar/gelb | Nur gleicher Typ | -20°C bis +80°C |
| ATF (Automatic Transmission Fluid) | Manche Hynautic-Systeme | Rot | Nein | -30°C bis +100°C |
| Synthetisches Hydrauliköl | Lecomble & Schmitt | Variabel | Nein | -40°C bis +100°C |

**Kritisch:** NIEMALS verschiedene Hydrauliköle mischen! Führt zu Dichtungsquellung, Viskositätsveränderung und Systemausfall. Bei Unsicherheit: System komplett spülen und mit dem vom Hersteller vorgeschriebenen Öl neu befüllen.

#### 2.5.3 Hydraulik-Entlüftung

Luft im Hydrauliksystem ist der häufigste Grund für „weiches Ruder" und Autopilot-Fehlfunktion:

**Symptome von Luft im System:**
- Ruder fühlt sich schwammig an
- Autopilot schwingt über (Overshoot)
- Geräusche (Blubbern) bei Ruderbewegung
- Rudersensor zeigt korrekte Position, aber Boot reagiert nicht

**Entlüftungsverfahren:**
1. Vorratsbehälter bis Maximum füllen
2. Entlüftungsventil am Zylinder öffnen (Auffangbehälter unterstellen)
3. Langsam von Anschlag zu Anschlag steuern (manuell!)
4. Warten bis nur noch blasenfreies Öl austritt
5. Entlüftungsventil schließen
6. Vorratsbehälter nachfüllen
7. Vorgang 3–5 mal wiederholen
8. Abschließend: Autopilot-Testlauf im Hafen

### 2.6 Firmware-Konfiguration und Netzwerk-Adressierung

#### 2.6.1 NMEA-2000-Geräteadressen und Instanznummern

Jedes Gerät im NMEA-2000-Netzwerk hat eine eindeutige Adresse (0–253). Die Adresszuweisung erfolgt automatisch (Address Claiming Protocol), kann aber manuell geändert werden bei Konflikten:

| Symptom | Ursache | Lösung |
|---------|---------|--------|
| Zwei Geräte zeigen identische Daten | Gleiche Geräteinstanz | Instanznummer eines Geräts ändern |
| Plotter zeigt "2× GPS" | Zwei GPS-Quellen ohne Priorisierung | Datenquelle-Priorität im Plotter festlegen |
| AP ignoriert GPS-Daten | AP hört auf falsches GPS | Datenquelle im AP-Controller festlegen |
| Rudersensor-Daten fehlen | Adresskonflikt | Netzwerk-Scan, Adresse manuell zuweisen |

#### 2.6.2 Datenquellen-Priorisierung

Wenn mehrere Geräte den gleichen Datentyp liefern (z.B. zwei GPS-Empfänger oder GPS + Kartenplotter), muss der Autopilot-Controller wissen, welche Quelle er verwenden soll:

**Heading-Priorisierung (empfohlen):**
1. Priorität 1: GNSS-Kompass (falls vorhanden, höchste Genauigkeit)
2. Priorität 2: Solid-State IMU / AHRS (z.B. EV-1, Precision-9)
3. Priorität 3: Fluxgate-Kompass (Legacy)

**GPS-Priorisierung (empfohlen):**
1. Priorität 1: Externer GPS-Empfänger (beste Antenne, höchste Update-Rate)
2. Priorität 2: Kartenplotter-internes GPS
3. Priorität 3: AIS-Transponder GPS (oft geringere Update-Rate)

**Wind-Priorisierung (für Segel-Autopilot):**
1. Priorität 1: Ultraschall-Windgeber (keine beweglichen Teile)
2. Priorität 2: Mechanischer Windgeber (Becher/Flügel)

#### 2.6.3 Firmware-Updates bei der Installation

Bei jeder Neuinstallation: Firmware aller Geräte auf den neuesten Stand bringen BEVOR die Kalibrierung durchgeführt wird:

| Hersteller | Update-Methode | Typische Dauer | Anmerkung |
|------------|---------------|----------------|-----------|
| Raymarine | Lighthouse-App oder SD-Karte | 10–20 min/Gerät | Alle Geräte gleichzeitig aktualisieren |
| B&G | B&G-App oder USB | 5–15 min/Gerät | H5000 benötigt separaten Update-Prozess |
| Garmin | Garmin Express oder SD-Karte | 10–15 min/Gerät | ActiveCaptain-App für drahtloses Update |
| Simrad | Simrad-App oder SD-Karte | 10–20 min/Gerät | Gleiche Plattform wie B&G |
| Furuno | SD-Karte oder USB | 15–30 min/Gerät | Nur über PC-Software |

**Achtung:** Nach einem Firmware-Update können Kalibrierungswerte verloren gehen! Immer ERST updaten, DANN kalibrieren. Kalibrierungswerte vorher notieren.

### 2.7 Seatrial-Protokoll — Systematische Abstimmung auf dem Wasser

#### 2.7.1 Vorbereitung

| Bedingung | Mindestanforderung | Ideal |
|-----------|-------------------|-------|
| Wetter | <20 kn Wind, <BF 5 | 8–12 kn, BF 3–4 |
| Seegang | <1,5m Wellenhöhe | <0,5m |
| Strömung | <2 kn | <0,5 kn |
| Verkehr | Genügend Seeraum | Freies Wasser, kein Verkehr |
| Dauer | Mindestens 2 Stunden | 3–4 Stunden |
| Kraftstoff | Mindestens halber Tank | Voller Tank (realistische Trimmlage) |
| Besatzung | Min. 2 Personen | 2–3 Personen |

#### 2.7.2 Seatrial-Ablauf

**Phase 1: Grundfunktionstest (30 min)**
1. AP aktivieren, gerader Kurs unter Motor, ruhiges Wasser
2. ±10°-Kursänderungen per Tastendruck, Reaktion beobachten
3. ±30°-Kursänderungen, Overshoot beobachten
4. Track-Modus testen (Wegpunkt voraus setzen)
5. Antriebsrichtung verifizieren (StB-Taste → Boot dreht nach StB)

**Phase 2: PID-Optimierung unter Motor (30 min)**
1. Gain auf 50% starten
2. Kurs geradeaus, Boot-Verhalten beobachten:
   - Schwingt das Boot hin und her? → Gain reduzieren
   - Reagiert der AP träge auf Wind/Strömung? → Gain erhöhen
3. Counter-Rudder auf 50% starten
4. 90°-Kursänderung durchführen:
   - Überschwinger >10°? → Counter-Rudder erhöhen
   - Boot braucht >15s für 90°? → Counter-Rudder reduzieren
5. Auto-Tune durchführen (wenn verfügbar)

**Phase 3: Segeltest (60 min, nur Segelyachten)**
1. Auf Am-Wind-Kurs gehen (40–50° zum wahren Wind)
2. AP in Kompass-Modus: Boot-Verhalten bei Böen beobachten
3. AP in Wind-Modus umschalten: konstanter scheinbarer Windwinkel?
4. Halse unter AP durchführen (wenn System dies unterstützt)
5. Sea State Filter schrittweise erhöhen bei Seegang
6. Raumschots-Kurs: Totband auf 3–5° erweitern

**Phase 4: Grenzbedingungen (30 min)**
1. Volle Kraft voraus unter Motor: AP bei Höchstgeschwindigkeit
2. Langsamste Fahrt: AP bei Mindestgeschwindigkeit (Steuerbarkeitsgrenze)
3. Manuell überraschend Gegenruder geben: AP reagiert?
4. Alarm-Test: NMEA-2000-Kabel kurz abziehen → Alarm?
5. Not-Aus: AP manuell abschalten → sofortige manuelle Steuerung möglich?

#### 2.7.3 Seatrial-Protokollvorlage

```
SEATRIAL-PROTOKOLL
━━━━━━━━━━━━━━━━━
Boot: _________________ Datum: __________
System: _______________ Firmware: ________
Techniker: ____________ Eigner: __________

WETTERBEDINGUNGEN:
Wind: ___kn aus ___ | See: ___m | Strömung: ___kn

KOMPASS-SWING:
Restdeviation max.: ±___° | Status: □ OK □ Wiederholen

RUDERSENSOR:
Mittellage-Offset: ___° | Spiel: ___° | Status: □ OK □ Nacharbeiten

PID-PARAMETER (Endergebnis):
Gain: ___% | Counter-Rudder: ___% | Totband: ___°
Sea State: ___% | Auto-Tune: □ Ja □ Nein

TEST-ERGEBNISSE:
Kursgenauigkeit Motor: ±___° | Segel: ±___°
Overshoot 90°-Wende: ___° | Reaktionszeit: ___s
Max. Seegang getestet: BF ___ | Ergebnis: □ OK □ Grenzwertig

STROMVERBRAUCH:
Motor ruhig: ___A | Motor Seegang: ___A | Segeln: ___A

PROBLEME / ANMERKUNGEN:
_______________________________________________

UNTERSCHRIFTEN:
Techniker: ____________ Eigner: ____________
```

---

## 3. Typenübersicht — Einbauarten nach Antriebstyp

### 3.1 Hydraulik-Einbau (Zylinder + Pumpe + Bypass)

#### 3.1.1 Anwendungsbereich

Hydraulische Autopilot-Antriebe sind Standard bei:
- Motoryachten ab 35 Fuß mit hydraulischer Steueranlage
- Segelyachten ab 40–45 Fuß mit hydraulischer Steueranlage
- Allen Booten mit bestehender hydraulischer Rudermaschine
- Superyachten (grundsätzlich hydraulisch)

#### 3.1.2 Einbau-Schritt für Schritt

**Schritt 1: Pumpenauswahl und -positionierung**

| Bootslänge | Verdrängung | Empfohlene Pumpengröße | Typisches Modell |
|------------|-------------|----------------------|------------------|
| 30–38 ft | 5–10 t | 80–120 cm³/rev | Raymarine Type 1 |
| 38–45 ft | 10–20 t | 120–200 cm³/rev | Raymarine Type 2 |
| 45–55 ft | 20–40 t | 200–350 cm³/rev | Raymarine Type 3 |
| 55–70 ft | 40–80 t | 350+ cm³/rev | Separate hydraulische Steuerpumpe |

**Schritt 2: Leitungsverlegung**

- Hydraulikleitungen: Nylon-Rohr (SAE J844) oder Kupfer-Nickel (CuNi 90/10)
- Mindest-Innendurchmesser: 10 mm (bis 40 ft), 13 mm (bis 55 ft), 16 mm (>55 ft)
- Leitungslänge: So kurz wie möglich. Jeder Meter zusätzliche Leitung reduziert die Reaktionszeit
- Biegeradien: Min. 5× Außendurchmesser
- Befestigung: Alle 500 mm mit gummigepufferten Schellen (Vibrationsentkopplung)
- Anschlüsse: JIC/SAE-Fittings mit Dichtring, kein Teflonband auf geraden Hydraulikanschlüssen

**Schritt 3: Bypass-Ventil**

Das Bypass-Ventil ist die Schnittstelle zwischen Autopilot und manueller Steuerung:
- **Offen:** Manuelle Steuerung aktiv, AP-Pumpe druckfrei. Hydrauliköl fließt frei durch.
- **Geschlossen:** AP-Pumpe steuert, manuelle Helm-Pumpe gesperrt (oder zusätzliches Rückschlagventil)

| Bypass-Typ | Betätigung | Vorteile | Nachteile |
|------------|-----------|----------|-----------|
| Manuell (Kugelhahn) | Handhebel im Maschinenraum | Einfach, zuverlässig | Muss manuell umgeschaltet werden |
| Solenoid (elektr.) | Automatisch bei AP-Aktivierung | Komfortabel, sicher | Komplexer, kann kleben |
| Integriert in AP-Pumpe | Automatisch | Kompaktes System | Nicht nachrüstbar |

**Schritt 4: Zylinder-Anbindung**

Der Autopilot-Hydraulikzylinder wird parallel zum bestehenden Steuerzylinder angeschlossen:

```
               ┌── AP-Pumpe ──── AP-Zylinder ──┐
               │                                 │
Helm-Pumpe ────┤                                 ├── Steuerquadrant
               │                                 │
               └── Bypass ─── Helm-Zylinder ────┘
```

Alternative bei integriertem System:
```
               ┌── AP-Pumpe ──┐
               │    (Bypass)   │
Helm-Pumpe ────┤              ├── Steuerzylinder ── Ruder
               │              │
               └──────────────┘
```

#### 3.1.3 Typische Fehler beim Hydraulik-Einbau

| Fehler | Auswirkung | Vermeidung |
|--------|-----------|-----------|
| Leitungen zu lang | Verzögerte Reaktion, Überschwinger | Kürzeste Route planen |
| Luft im System | Schwammiges Ruder, Overshoot | Sorgfältige Entlüftung, 5× wiederholen |
| Falsches Hydrauliköl | Dichtungsschäden, Systemausfall | Hersteller-Vorgabe prüfen |
| Bypass nicht korrekt | AP steuert gegen Helm-Pumpe | Bypass-Logik vor Inbetriebnahme prüfen |
| Zu geringer Leitungsquerschnitt | Druckverlust, geringe Rudergeschwindigkeit | Herstellervorgabe einhalten |
| Undichte Anschlüsse | Ölverlust, Lufteintritt | JIC-Fittings korrekt anziehen |

### 3.1.4 Hydraulik-Dimensionierung nach Bootsgröße

**Ruderdrehmoment-Berechnung (Näherung für Verdrängungsyachten):**

```
M_rudder = 0,5 × ρ × v² × A_rudder × C_r × r_rudder

Wobei:
  ρ        = Dichte Seewasser = 1025 kg/m³
  v        = Bootsgeschwindigkeit in m/s (1 kn = 0,5144 m/s)
  A_rudder = Ruderfläche in m²
  C_r      = Ruderbeiwert ≈ 1,0–1,5 (abhängig von Profil und Anstellwinkel)
  r_rudder = Abstand Druckpunkt zum Ruderschaft in m (typisch 25–35% der Ruderbreite)
```

**Typische Ruderdrehmomente nach Bootsklasse:**

| Bootsklasse | Verdrängung | Ruderfläche | Max. Drehmoment | Empfohlener Zylinder |
|-------------|-------------|-------------|-----------------|---------------------|
| Segelyacht 32 ft | 5.000 kg | 0,15 m² | 200 Nm | 60mm Bohrung, 200mm Hub |
| Segelyacht 40 ft | 9.000 kg | 0,25 m² | 500 Nm | 80mm Bohrung, 250mm Hub |
| Segelyacht 50 ft | 18.000 kg | 0,40 m² | 1.200 Nm | 100mm Bohrung, 300mm Hub |
| Motoryacht 38 ft | 10.000 kg | 0,20 m² | 400 Nm | 70mm Bohrung, 200mm Hub |
| Motoryacht 48 ft | 20.000 kg | 0,35 m² | 1.000 Nm | 90mm Bohrung, 250mm Hub |
| Motoryacht 60 ft | 40.000 kg | 0,50 m² | 2.500 Nm | 120mm Bohrung, 350mm Hub |

*Hinweis: Angaben geschätzt. Exakte Berechnung erfordert CFD-Analyse oder Messung. (confidence: estimated)*

**Pumpendimensionierung:**

Die Pumpenverdrängung bestimmt, wie schnell das Ruder bewegt werden kann:

```
Ruderdrehgeschwindigkeit = (Q_pump × 60) / (A_zylinder × 2π × r_quadrant)

Wobei:
  Q_pump      = Pumpenfördermenge in cm³/s = Verdrängung × Drehzahl
  A_zylinder  = Kolbenfläche in cm²
  r_quadrant  = Quadrant-Radius in cm
```

**Ziel:** Mindestens 3°/s Ruderdrehgeschwindigkeit für Segelyachten, 5°/s für Motoryachten.

### 3.1.5 Hydraulik-Leitungsverlegung — Detailplanung

| Kriterium | Anforderung | Anmerkung |
|-----------|-------------|-----------|
| Leitungsmaterial | Nylon SAE J844 oder CuNi 90/10 | Kein PVC, kein Gartenschlauch! |
| Innendurchmesser | Min. Herstellervorgabe, eher eine Stufe größer | Zu klein = Druckverlust, langsames Ruder |
| Biegeradius | Min. 5× Außendurchmesser | Knicke = Druckverlust + Leitungsbruch |
| Befestigung | Gummigepufferte Schellen alle 500mm | Vibration entkoppeln, Scheuern vermeiden |
| Leitungsführung | Kürzester Weg Pumpe↔Zylinder | Jeder Meter kostet Reaktionszeit |
| Leitungslänge | Beide Leitungen (Vor/Rücklauf) gleich lang | Sonst asymmetrische Reaktion BB/StB |
| Anschlüsse | JIC 37° (SAE J514) mit O-Ring | KEIN Teflonband auf JIC-Gewinden! |
| Scheuerschutz | Leitungen dürfen nirgends am GFK scheuern | Vibration verursacht Abrieb → Leitungsbruch |
| Temperatur | Leitungen nicht an Motor/Auspuff entlangführen | Wärme verändert Ölviskosität, Nylon wird weich |

**Leitungsplan-Beispiel (Segelyacht 40 ft):**

```
                Maschinenraum            Achterschiff/Lazarette
    ┌────────────────┐           ┌──────────────────┐
    │ Helm-Pumpe     │           │ Steuerzylinder   │
    │ (am Pedestal)  │           │ (am Quadranten)  │
    │    │     │     │           │    │        │    │
    │    │P    │R    │           │    │P       │R   │
    │    │     │     │           │    │        │    │
    └────┼─────┼─────┘           └────┼────────┼────┘
         │     │                      │        │
         │     │    ┌──────────────┐  │        │
         │     ├────┤ AP-Pumpe     ├──┤        │
         │     │    │ + Bypass     │  │        │
         │     │    └──────────────┘  │        │
         │     │                      │        │
         └─────┼──────────────────────┼────────┘
               │      Leitungslänge   │
               │      max. 3m ideal   │
               │      max. 6m akzeptabel
               P = Druckleitung (Vorlauf)
               R = Rücklaufleitung
```

### 3.2 Linear-Einbau (Quadrant-Antrieb)

#### 3.2.1 Anwendungsbereich

Lineare Autopilot-Antriebe (Linearaktuatoren) sind der häufigste Typ auf Segelyachten von 28–50 Fuß mit mechanischer Steueranlage (Seilzug oder Gestänge):

- **Typische Boote:** Bavaria, Jeanneau, Beneteau, Hanse, Hallberg-Rassy 30–50 ft
- **Steuerungstyp:** Seilzug vom Rad über Quadrant zum Ruderschaft
- **Einbauort:** Unterer Heckspiegel, Lazarette oder Backskiste — dort wo der Ruderquadrant sitzt

#### 3.2.2 Geometrie und Hebelarm

```
                    Ruderschaft
                        │
               ┌────────┼────────┐
               │    Quadrant     │
               │   (Halbkreis)   │
               └───────┬─────────┘
                       │← Hebelarm r →│
                       │               │
                       │    ┌──────────┤
                       │    │  Linear- │
                       │    │  Antrieb │
                       │    └──────────┤
                       │               │
                       └───── Montage- │
                              Punkt    │
                              (Boot)   │
```

**Hebelarm-Berechnung:**

```
F_linear = M_rudder / r

Wobei:
  F_linear  = benötigte Linearkraft in Newton
  M_rudder  = Ruder-Drehmoment in Nm (abhängig von Bootsgröße, Geschwindigkeit, Ruderfläche)
  r         = Abstand vom Ruderschaft-Zentrum zum Angriffspunkt am Quadranten in Metern
```

**Empfohlene Hebelarm-Längen:**

| Quadrant-Radius | Hebelarm (Angriffspunkt) | Anmerkung |
|-----------------|--------------------------|-----------|
| 150 mm | 100–120 mm | Kleiner Quadrant, hohe Kraft nötig |
| 200 mm | 140–170 mm | Standard Segelyacht 32–38 ft |
| 250 mm | 170–210 mm | Standard Segelyacht 38–45 ft |
| 300 mm | 200–250 mm | Große Segelyacht 45–55 ft |

**Wichtig:** Zu nahe am Ruderschaftzentrum → braucht mehr Kraft, kann den Antrieb überlasten. Zu weit außen → mehr Hub nötig, kann mechanische Endanschläge erreichen.

#### 3.2.3 Montage-Schritte

**Schritt 1: Antrieb ausrichten**
- Antrieb parallel zur Ruderschaft-Achse montieren (nicht schräg!)
- Kolbenstange muss bei Rudermittellage auf 50 % Hub stehen (±5 mm)
- Montageplatte fest mit Rumpfstruktur verschrauben (nicht mit GFK-Haut allein — Kernholz oder Sperrholz-Verstärkung!)

**Schritt 2: Quadrant-Anbindung**
- Gabelkopf am Quadranten mit Bolzen befestigen
- Bolzen: rostfreier Stahl A4-80 (AISI 316), Sicherungssplint
- Keine Hülsenklemmen oder Kabelbinder als Befestigung!
- Spiel im Gabelkopf: <0,5 mm. Mehr Spiel → Geräusche, ungenaue Steuerung

**Schritt 3: Endanschläge**
- Mechanische Endanschläge prüfen: Kolbe darf bei vollem Ruderausschlag nicht anschlagen
- Software-Endanschläge im Controller 5° vor mechanischem Anschlag setzen
- Achtung: Manche Quadranten haben asymmetrische Anschläge (z.B. 35° BB, 40° StB)

#### 3.2.4 Linear-Einbau Spezifika nach Bootsgröße

| Bootsklasse | Verdrängung | Empfohlene Kraft | Empfohlener Hub | Typische Modelle |
|-------------|-------------|------------------|-----------------|------------------|
| 28–32 ft Segel | 3–5 t | 800–1.200 N | 150–200 mm | Raymarine Type 1 Linear, B&G NAC-1 |
| 32–38 ft Segel | 5–8 t | 1.200–2.000 N | 200–250 mm | Raymarine Type 2 Linear, Garmin GHP Compact Reactor |
| 38–45 ft Segel | 8–15 t | 2.000–3.500 N | 250–350 mm | Raymarine Type 2/3 Linear, Simrad NAC-2 |
| 45–55 ft Segel | 15–25 t | 3.500–5.000 N | 300–400 mm | Raymarine Type 3 Linear, B&G NAC-3 |

### 3.3 Wheel-Drive-Einbau (Radsteuerung)

#### 3.3.1 Anwendungsbereich

Wheel-Drives greifen direkt am Steuerrad an und sind typisch für:
- Nachrüstungen auf Booten ohne Zugang zum Ruderquadranten
- Kleinere Segelyachten (25–35 ft) ohne Platz für Linearantrieb
- Provisorische Installationen (Charter, Überführungen)
- Backup-Systeme als Zweitantrieb

#### 3.3.2 Einbau-Prinzip

```
                Steuerrad
               ╭─────────╮
              │           │
              │   Nabe    │── Wheel-Drive-Motor
              │           │   (Reibrad oder Kette)
               ╰─────────╯
                    │
              Steuer-Pedestal
```

**Antriebsarten:**

| Typ | Prinzip | Vorteile | Nachteile |
|-----|---------|----------|-----------|
| Reibrad (Friction) | Gummirolle auf Radflansch | Einfacher Einbau, abnehmbarer | Rutscht bei Nässe/Fett, begrenztes Drehmoment |
| Kettenantrieb | Kette auf Ritzel an Radnabe | Kein Rutschen, höheres Drehmoment | Aufwendigerer Einbau, nicht abnehmbar |
| Riemenantrieb | Zahnriemen auf Radnabe | Leise, wartungsarm | Begrenztes Drehmoment |
| Schneckengetriebe | Schneckenwelle auf Wellen-Ritzel | Sehr hohes Drehmoment, selbsthemmend | Teuer, aufwendiger Einbau |

#### 3.3.3 Einbau-Schritte (Reibrad-Typ)

1. **Montageplatte am Pedestal** befestigen (Schrauben M6/M8 in Pedestal-Gehäuse)
2. **Motor-Einheit** auf Montageplatte montieren, Reibrad muss mittig auf Radflansch drücken
3. **Federspannung** einstellen: fest genug gegen Rutschen, locker genug für manuelle Übersteuerung
4. **Kabel** durch Pedestal-Inneres zum Cockpit-Boden verlegen
5. **Endanschlags-Erkennung:** Stromaufnahme-basiert (Motor zieht mehr Strom am Anschlag)

#### 3.3.4 Wheel-Drive Limitationen

| Parameter | Typischer Wert | Anmerkung |
|-----------|---------------|-----------|
| Max. Bootsgröße | 30–35 ft (Reibrad), 40–45 ft (Kette) | Drehmoment-limitiert |
| Max. Verdrängung | 5–8 t (Reibrad), 12–15 t (Kette) | Bei schwerem Wetter deutlich weniger |
| Max. Seegang | BF 5–6 (Reibrad), BF 6–7 (Kette) | Bei BF 7+ oft unzureichend |
| Lebensdauer Reibrad | 3–5 Jahre | UV, Salzwasser, Abrieb |
| Geräuschpegel | 55–65 dB(A) | Deutlich hörbar im Cockpit |
| Reaktionszeit | 0,5–1,5 s | Langsamer als Direkt-Antrieb |

### 3.4 Pinnen-Einbau (Tiller-Pilot)

#### 3.4.1 Anwendungsbereich

Tiller-Piloten sind die einfachsten Autopilot-Antriebe:
- Segelyachten bis 30–35 Fuß mit Pinnensteuerung
- Budget-Lösung für Einsteiger
- Backup-System für größere Boote
- Ideal für Langfahrt-Segelyachten mit Pinne (geringe Komplexität = hohe Zuverlässigkeit)

#### 3.4.2 Einbau-Geometrie

```
        Pinne (Tillerhebel)
        ═══════════════════╗
                           ║
        ┌──────────────────╫── Ruderschaft
        │   Tiller-Pilot   ║
        │   [====≡====]    ║
        │                  ║
        └── Montagewinkel ─╝
            (Cockpit-Boden/Süll)
```

**Montage-Winkel:**

| Winkel Pinne—Pilot | Effektivität | Anmerkung |
|--------------------|-------------|-----------|
| 90° | 100 % | Ideal, aber selten realisierbar |
| 75–85° | 95 % | Sehr gut |
| 60–75° | 85–95 % | Akzeptabel |
| 45–60° | 70–85 % | Grenzwertig, mehr Kraft nötig |
| <45° | <70 % | Nicht empfohlen |

#### 3.4.3 Montage-Schritte

1. **Montagepunkt am Cockpit-Boden oder Süll:**
   - Muss fest sein (Sperrholz-Unterlage, nicht nur GFK-Haut)
   - Position so wählen, dass Pilot-Achse möglichst senkrecht zur Pinne steht
   - Edelstahl-Augplatte (A4-80) oder Aluminium-Montageplatte

2. **Angriffspunkt an der Pinne:**
   - Pin-/Bolzenverbindung, Kugelkopf oder Gabelkopf
   - So weit vom Ruderschaft entfernt wie möglich (=maximaler Hebelarm)
   - Typisch: 400–600 mm vom Ruderschaft

3. **Pilotlänge einstellen:**
   - Bei Rudermittellage: Pilot auf ~50 % Hub
   - Voller Ruderausschlag darf Pilot nicht an Endanschlag bringen
   - Genug Reserve für Seegang (Ruder schlägt kurzzeitig über den normalen Bereich)

4. **Stromversorgung:**
   - Direkt von Batterie, nicht über Schaltpanel (Spannungsabfall!)
   - Kabelquerschnitt: mind. 4 mm² (bis 10A), 6 mm² (bis 15A)
   - Eigene Sicherung: träge, 150 % des Nennstroms

#### 3.4.4 Tiller-Pilot Modell-Übersicht

| Hersteller | Modell | Max. Kraft | Hub | Max. Boot | Preis (ca.) |
|------------|--------|-----------|------|-----------|------------|
| Raymarine | ST1000+ | 400 N (30 kg) | 305 mm | 6,7 m / 2,5 t | 950 € |
| Raymarine | ST2000+ | 530 N (54 kg) | 305 mm | 10 m / 5 t | 1.250 € |
| Simrad | TP10 | 400 N | 280 mm | 7 m / 3 t | 890 € |
| Simrad | TP22 | 530 N | 305 mm | 10 m / 5 t | 1.180 € |
| Simrad | TP32 | 800 N | 356 mm | 12 m / 8 t | 1.450 € |
| Garmin | GHP Reactor Tiller | 530 N | 305 mm | 10 m / 5 t | 1.350 € |
| NauticAlert | NA-400 | 400 N | 250 mm | 7 m / 3 t | 750 € |

### 3.5 Retrofit in bestehende Boote

#### 3.5.1 Herausforderungen bei der Nachrüstung

| Herausforderung | Häufigkeit | Lösungsansatz |
|----------------|-----------|---------------|
| Kein Zugang zum Quadranten | 40 % | Inspektionsluke einbauen oder Wheel-Drive |
| Kein NMEA 2000 vorhanden | 35 % | NMEA-2000-Starter-Kit installieren |
| Unzureichende Batterie-Kapazität | 30 % | Batterie aufrüsten oder Verbrauchsanalyse |
| Kein Platz für Kompass | 25 % | Kompakte IMU-Sensoren nutzen |
| Hydraulik-Inkompatibilität | 20 % | Adapter-Fittings oder Bypass-Lösung |
| Korrodierte Kabel | 15 % | Neue Kabelwege legen |
| Veraltetes SeaTalk1 | 15 % | SeaTalk1-zu-NMEA-2000-Konverter |

#### 3.5.2 SeaTalk1-zu-NMEA-2000-Migration

Viele ältere Raymarine-Systeme nutzen SeaTalk1 (proprietärer 3-Draht-Bus). Bei einer Nachrüstung muss entweder:

**Option A: Konverter verwenden**
- Raymarine E22158 SeaTalk1-zu-SeaTalkNG Konverter
- Actisense NGW-1 NMEA 0183/SeaTalk1-zu-NMEA-2000 Gateway
- Sinnvoll wenn noch viele SeaTalk1-Geräte an Bord sind

**Option B: Vollständig auf NMEA 2000 umstellen**
- Alle Sensoren (GPS, Log, Wind, Kompass) durch NMEA-2000-Modelle ersetzen
- Langfristig sauberer, aber teurer
- Empfohlen bei >5 Jahre alten SeaTalk1-Geräten

#### 3.5.3 Retrofit-Checkliste

```
□ Steuerungssystem identifizieren (hydraulisch / mechanisch / Pinne)
□ Zugang zum Quadranten / Tiller prüfen
□ Vorhandenes NMEA-Netzwerk dokumentieren
□ Batterie-Kapazität und Ladeleistung bewerten
□ Kabelwege identifizieren (Strom + Signal)
□ Kompass-Standort evaluieren (Magnetik-Test)
□ Rudersensor-Montageposition finden
□ Materialstärke an Montagepunkten prüfen (Kernverstärkung?)
□ Budget für Gesamtsystem inkl. aller Adapter kalkulieren
□ Probefahrt-Termin für Kalibrierung planen
```

#### 3.5.4 Installationskosten-Vergleich nach Antriebstyp (Retrofit)

| Antriebstyp | Material (ca.) | Arbeitszeit | Gesamtkosten (ca.) | Schwierigkeitsgrad |
|-------------|---------------|-------------|--------------------|--------------------|
| Tiller-Pilot | 900–1.500 € | 4–6 h | 1.300–2.000 € | Einfach (Selbsteinbau möglich) |
| Wheel-Drive | 1.500–2.500 € | 6–10 h | 2.000–3.500 € | Mittel |
| Linearantrieb (mit NMEA 2000) | 2.500–5.000 € | 12–20 h | 3.500–7.000 € | Anspruchsvoll |
| Hydraulik (in bestehendes System) | 3.000–6.000 € | 16–24 h | 4.500–8.500 € | Anspruchsvoll |
| Hydraulik (neues System inkl. Leitungen) | 5.000–10.000 € | 24–35 h | 7.500–13.500 € | Sehr anspruchsvoll |
| GNSS-Kompass-Upgrade (zusätzlich) | 2.000–3.500 € | 3–5 h | +2.500–4.000 € | Mittel |

*Arbeitszeit berechnet mit 85 €/h (Werft-Durchschnitt Deutschland 2025). (confidence: estimated)*

#### 3.5.5 Empfehlungsmatrix: Welches System für welches Boot?

| Bootstyp | Steuerung | Empfohlener Antrieb | Empfohlenes System | Budget (ca.) |
|----------|-----------|--------------------|--------------------|-------------|
| Segelyacht 25–30 ft, Pinne | Pinne | Tiller-Pilot | Raymarine EV-100 Tiller / Simrad TP22 | 1.200–2.000 € |
| Segelyacht 28–35 ft, Rad | Seilzug | Wheel-Drive oder Linear | Raymarine EV-100 Wheel / Garmin Reactor Compact | 2.500–4.000 € |
| Segelyacht 35–45 ft, Rad | Seilzug | Linearantrieb | Raymarine EV-200 / B&G NAC-2 | 4.000–7.000 € |
| Segelyacht 45–55 ft, Rad | Hydraulik oder Seilzug | Linear (Seilzug) oder Hydraulik | Raymarine EV-300 / B&G NAC-3 | 6.000–12.000 € |
| Segelyacht 55+ ft | Hydraulik | Hydraulik | B&G NAC-3 + HPR2012 | 10.000–18.000 € |
| Motoryacht 30–38 ft | Hydraulik | Hydraulik | Garmin GHP 20 / Simrad AC12N | 3.000–6.000 € |
| Motoryacht 38–50 ft | Hydraulik | Hydraulik | Simrad AC42N / Garmin GHP 30 | 5.000–10.000 € |
| Motoryacht 50–70 ft | Hydraulik | Hydraulik | Simrad AC70 / Furuno NAVpilot 700 | 10.000–25.000 € |
| Katamaran 38–50 ft | Hydraulik (2× Ruder) | 2× Hydraulik oder Koppelstange | Simrad AC70 Dual / B&G NAC-3 | 12.000–20.000 € |
| Regatta-Yacht 30–45 ft | Seilzug | Linearantrieb | B&G NAC-2/NAC-3 / NKE Gyropilot | 5.000–15.000 € |

#### 3.5.6 Werkzeug und Material für eine typische Installation

**Werkzeugliste:**

| Kategorie | Werkzeug | Anmerkung |
|-----------|----------|-----------|
| Elektrik | Multimeter (True RMS) | Spannungs-/Strom-/Widerstandsmessung |
| Elektrik | Crimp-Zange (hexagonal) | Für verzinnte Ringkabelschuhe |
| Elektrik | Abisolierzange | Für marine Kabel 1,5–16 mm² |
| Elektrik | Heißluftfön | Für Schrumpfschlauch |
| Elektrik | Lötkolben 60W | Nur als Zusatzsicherung (Crimp reicht) |
| Mechanik | Bohrmaschine + HSS-Bohrer | Für Montagelöcher |
| Mechanik | Stufenbohrer | Für Kabeldurchführungen |
| Mechanik | Schraubenschlüssel-Satz (metrisch) | 8–19 mm |
| Mechanik | Drehmomentschlüssel | Für Montagebolzen |
| Mechanik | Gewindeschneider M6/M8 | Für Montagewinkel |
| Hydraulik | Hydraulik-Entlüftungsset | Schlauch, Auffangbehälter, Ventilschlüssel |
| Hydraulik | Hydraulik-Schlüssel (JIC) | Für JIC-Verschraubungen |
| Allgemein | Kabelbinder (UV-beständig) | Marine-Qualität (schwarz) |
| Allgemein | Sikaflex 291i | Für Decksdurchbrüche |
| Allgemein | Kontaktfett (Caig DeoxIT) | Für NMEA-2000-Stecker |
| Allgemein | Schrumpfschlauch (klebend) | Verschiedene Durchmesser |
| Messung | Inklinometer / Wasserwaage | Für Sensor-Ausrichtung |
| Messung | Handkompass (Peilkompass) | Für magnetische Vermessung |
| Messung | Maßband 5m | Für Abstands-/Kabelmessung |

**Verbrauchsmaterial (typischer Bedarf):**

| Material | Menge (ca.) | Kosten (ca.) |
|----------|-------------|-------------|
| Marinekabel 10mm² rot | 10 m | 35 € |
| Marinekabel 10mm² schwarz | 10 m | 35 € |
| Marinekabel 2,5mm² (div. Farben) | 20 m | 30 € |
| Ringkabelschuhe (sortiert) | 30 Stück | 15 € |
| Schrumpfschlauch (klebend, sortiert) | 2 m | 12 € |
| Kabelverschraubungen IP67 M16/M20 | 6 Stück | 25 € |
| Kabelbinder 200mm schwarz | 100 Stück | 8 € |
| ANL-Sicherung + Halter | 1 Set | 25 € |
| Blade-Sicherungen (5A, 10A, 15A) | je 2 | 5 € |
| Sikaflex 291i Kartusche | 1 Stück | 15 € |
| Kontaktfett Spray | 1 Dose | 12 € |
| Sperrholz-Verstärkung 18mm | 0,5 m² | 15 € |
| Edelstahl-Schrauben A4-80 (sortiert) | 30 Stück | 20 € |
| **Summe Verbrauchsmaterial** | | **ca. 250 €** |

---

## 4. Produktlinien und Spezifikationen

### 4.1 Raymarine Einbaukits

#### 4.1.1 Raymarine Evolution Autopilot-System — Komponentenübersicht

| Komponente | Modell | Art-Nr. | Beschreibung |
|------------|--------|---------|-------------|
| Controller/Prozessor | EV-1 Sensor Core | T70096 | 9-Achsen-IMU, AHRS, kein separater Kompass nötig |
| Controller/Prozessor | EV-2 Autopilot-Prozessor | T70156 | Vollständiger AP-Controller mit NMEA 2000 |
| Antrieb Linear Typ 1 | Type 1 / 12V | M81130 | 460 N, 229 mm Hub, bis 8 t |
| Antrieb Linear Typ 1 | Type 1 / 24V | M81121 | 460 N, 229 mm Hub, bis 8 t |
| Antrieb Linear Typ 2 | Type 2 / 12V (kurz) | M81131 | 1.100 N, 305 mm Hub, bis 15 t |
| Antrieb Linear Typ 2 | Type 2 / 24V (kurz) | M81133 | 1.100 N, 305 mm Hub, bis 15 t |
| Antrieb Linear Typ 3 | Type 3 / 12V | M81140 | 2.500 N, 400 mm Hub, bis 25 t |
| Antrieb Linear Typ 3 | Type 3 / 24V | M81141 | 2.500 N, 400 mm Hub, bis 25 t |
| Hydraulikpumpe Typ 1 | Type 1 / 12V | M81120 | 80 cm³/rev, bis 10 t |
| Hydraulikpumpe Typ 2 | Type 2 / 12V | M81202 | 150 cm³/rev, bis 20 t |
| Hydraulikpumpe Typ 3 | Type 3 / 12V | M81203 | 250 cm³/rev, bis 40 t |
| Bedieneinheit | p70s (Segel) | E22166 | Vollfarb-LCD, Wind-/Kompass-Modus |
| Bedieneinheit | p70Rs (Segel, Drehknopf) | E22167 | Mit Drehknopf für Kursänderung |
| Bedieneinheit | p70 (Motor) | E22165 | Vollfarb-LCD, Motoryacht-Modus |
| Rudersensor | Rudersensor lang | E22078 | Potentiometer, 150 mm Hebel |
| Rudersensor | Rudersensor kurz | E22079 | Potentiometer, 100 mm Hebel |
| Kabel SeaTalkNG | SeaTalkNG Backbone 5m | A06036 | SeaTalk-NG Backbone-Kabel |
| Adapter | STNG zu NMEA2000 (m) | A06045 | SeaTalk-NG auf DeviceNet Micro (m) |
| Adapter | STNG zu NMEA2000 (f) | A06075 | SeaTalk-NG auf DeviceNet Micro (f) |
| Terminator | SeaTalkNG Terminator | A06031 | 120 Ω Abschlusswiderstand |

> ✅ **Aufgeloest (Audit):** Doppelvergabe von M81120 behoben. Verifiziert: **M81120 = Type-1-Hydraulikpumpe 12V** (Hydraulikpumpen-Zeile bleibt korrekt); **Type-1-Linearantrieb 12V = M81130**; **Type-2-Linearantrieb 12V (kurz) = M81131**; **Type-2-Linearantrieb 24V (kurz) = M81133** (Type-2 lang: M81132 / M81134). Quelle: raymarine.com (Type-1/Type-2 Linear- und Hydraulik-Drive-Produktseiten) sowie Fachhandel (Defender Marine, West Marine, Fisheries Supply, MAURIPRO, Hodges Marine). Confidence dieser Zeilen: documented.
>
> ⚠️ **Rest-Hinweis (nicht verifiziert):** Type-1-Linearantrieb **24V (M81121)** sowie **Typ-3-Linearantrieb (M81140/M81141)** liessen sich nicht am Raymarine-Datenblatt bestaetigen (Type 3 wird ueblicherweise als Hydraulik-Linear, z.B. M81203/24V, gefuehrt). Diese Zeilen bleiben estimated — vor Nutzung gegen Raymarine-Datenblatt pruefen.

#### 4.1.2 Raymarine Komplett-Kits

| Kit-Name | Art-Nr. | Inhalt | Zielgruppe |
|----------|---------|--------|-----------|
| EV-100 Wheel | T70152 | EV-1, ACU-100, Wheel-Drive, p70s | Segelyacht 25–33 ft, Radsteuerung |
| EV-100 Tiller | T70161 | EV-1, ACU-100, Tiller-Antrieb, p70s | Segelyacht bis 30 ft, Pinne |
| EV-200 Linear | T70154 | EV-2, ACU-200, Type 1 Linear, p70s | Segelyacht 33–40 ft |
| EV-200 Hydraulik | T70153 | EV-2, ACU-200, Type 1 Hydraulik, p70 | Motoryacht 30–38 ft |
| EV-300 Linear | T70160 | EV-2, ACU-400, Type 2 Linear, p70s | Segelyacht 40–50 ft |
| EV-300 Hydraulik | T70162 | EV-2, ACU-400, Type 2 Hydraulik, p70 | Motoryacht 38–50 ft |
| EV-400 Sail Pack | T70163 | EV-2, ACU-400, Type 3 Linear, p70Rs | Segelyacht 50–60 ft |

### 4.2 B&G NAC Packages

#### 4.2.1 B&G Autopilot-Komponenten

| Komponente | Modell | Art-Nr. | Beschreibung |
|------------|--------|---------|-------------|
| Controller | NAC-1 Autopilot Computer | 000-13337-001 | Für Boote bis 10 t |
| Controller | NAC-2 Autopilot Computer | 000-13338-001 | Für Boote bis 20 t |
| Controller | NAC-3 Autopilot Computer | 000-13250-001 | Für Boote bis 40+ t |
| Kompass | Precision-9 Compass | 000-12607-001 | Solid-State, 9-Achsen |
| Rudersensor | RF25N Rudder Feedback | 000-13914-001 | NMEA 2000, berührungslos |
| Rudersensor | RF300 Rudder Feedback | 000-11544-001 | Analog, potentiometrisch |
| Antrieb | SD10 Linear Drive | 000-15954-001 | 12V, bis 8 t |
| Antrieb | SD12 Linear Drive | 000-15955-001 | 12V, bis 15 t |
| Hydraulikpumpe | HP1 Hydraulic Pump | 000-15956-001 | 12V, 80 cm³ |
| Hydraulikpumpe | HPR2012 Hydraulic Pump | 000-15957-001 | 12V, 150 cm³ |
| Bedieneinheit | Triton² Pilot Controller | 000-13294-001 | Dedizierte AP-Steuerung |
| Bedieneinheit | H5000 Pilot Controller | 000-11542-001 | High-Performance Regatta |

#### 4.2.2 B&G Komplett-Pakete

| Paket | Art-Nr. | Inhalt | Zielgruppe |
|-------|---------|--------|-----------|
| NAC-1 Pilot Pack | 000-15043-001 | NAC-1, Precision-9, RF25N, Triton² | Cruiser bis 10 t |
| NAC-2 Pilot Pack | 000-15044-001 | NAC-2, Precision-9, RF25N, Triton² | Cruiser 10–20 t |
| NAC-3 Pilot Pack | 000-15045-001 | NAC-3, Precision-9, RF25N, H5000 | Bluewater/Performance |
| NAC-3 Hydraulic Pack | 000-15046-001 | NAC-3, Precision-9, RF25N, HPR2012 | Große Motoryachten |

### 4.3 Garmin GHP Kits

#### 4.3.1 Garmin Reactor Autopilot-Komponenten

| Komponente | Modell | Art-Nr. | Beschreibung |
|------------|--------|---------|-------------|
| Controller | Reactor 40 ECU | 010-11053-00 | Für Steer-by-Wire, bis 6 t |
| Controller | GHP Reactor ECU | 010-11054-00 | Universal, NMEA 2000 |
| Heading-Sensor | GHP Smart Heading Sensor | 010-11747-00 | Solid-State, 9-Achsen |
| Rudersensor | GRF 10 Rudder Feedback | 010-11745-00 | NMEA 2000, potentiometrisch |
| Antrieb Hydraulik | GHP 20 Hydraulic Pump | 010-11097-00 | 12V, bis 10 t |
| Antrieb Hydraulik | GHP 30 Hydraulic Pump | 010-12414-00 | 12V, bis 25 t |
| Antrieb Linear | GHP Compact Reactor | 010-11053-10 | 12V, 800 N, bis 8 t |
| Antrieb Linear | GHP 12 Linear Drive | 010-12417-00 | 12V, 1.200 N, bis 15 t |
| Bedieneinheit | GHC 20 Marine Autopilot | 010-01141-00 | Vollfarb-Touchscreen |
| Bedieneinheit | GHC 50 Autopilot Display | 010-02435-00 | 5" Touchscreen, NMEA 2000 |

#### 4.3.2 Garmin Komplett-Kits

| Kit-Name | Art-Nr. | Inhalt | Zielgruppe |
|----------|---------|--------|-----------|
| GHP Reactor Starter Pack (Hydraulik) | 010-11053-01 | ECU, GHP 20, GHC 20, Heading Sensor | Motoryacht bis 10 t |
| GHP Reactor Steer-by-Wire | 010-11053-21 | Reactor 40, GHC 20, Heading Sensor | Steer-by-Wire-Boote |
| GHP 30 Pack | 010-12414-10 | ECU, GHP 30, GHC 50, Heading Sensor | Motoryacht 15–25 t |
| GHP Compact Reactor Sail Pack | 010-11053-30 | ECU, Compact Reactor, GHC 20, Heading Sensor, GRF 10 | Segelyacht bis 8 t |

### 4.4 Simrad AP Packs

#### 4.4.1 Simrad Autopilot-Komponenten

| Komponente | Modell | Art-Nr. | Beschreibung |
|------------|--------|---------|-------------|
| Controller | AC12N | 000-10186-001 | Für Boote bis 10 t |
| Controller | AC42N | 000-10187-001 | Für Boote bis 20 t |
| Controller | AC70 | 000-10188-001 | Für Boote bis 45 t |
| Kompass | HS75 GNSS Compass | 000-16143-001 | GPS-Kompass, ±0,3° |
| Kompass | HS60 Heading Sensor | 000-14139-001 | Solid-State, NMEA 2000 |
| Rudersensor | RF45X Rudder Feedback | 000-14138-001 | NMEA 2000, berührungslos |
| Antrieb | SD10 Linear Drive | 000-15954-001 | (identisch mit B&G) |
| Hydraulikpumpe | HPR-1 | 000-15960-001 | 12V, 80 cm³ |
| Hydraulikpumpe | HPR-2 | 000-15961-001 | 12V, 160 cm³ |
| Bedieneinheit | AP44 Autopilot Controller | 000-13289-001 | Touchscreen, NMEA 2000 |
| Bedieneinheit | IS42 Digital Display | 000-14479-001 | Multifunction, AP-fähig |
| Tiller-Pilot | TP10 | 000-15892-001 | 400 N, bis 7 m |
| Tiller-Pilot | TP22 | 000-15893-001 | 530 N, bis 10 m |
| Tiller-Pilot | TP32 | 000-15894-001 | 800 N, bis 12 m |

#### 4.4.2 Simrad Komplett-Pakete

| Paket | Art-Nr. | Inhalt | Zielgruppe |
|-------|---------|--------|-----------|
| AP Pilot Pack Motor S | 000-15895-001 | AC12N, SD10, AP44, HS60, RF45X | Motorboot bis 10 t |
| AP Pilot Pack Motor M | 000-15896-001 | AC42N, HPR-1, AP44, HS60, RF45X | Motoryacht 10–20 t |
| AP Pilot Pack Motor L | 000-15897-001 | AC70, HPR-2, AP44, HS75, RF45X | Motoryacht 20–45 t |
| AP Pilot Pack Sail S | 000-15898-001 | AC12N, SD10, AP44, HS60, RF45X | Segelyacht bis 10 t |
| AP Pilot Pack Sail M | 000-15899-001 | AC42N, SD12, AP44, HS60, RF45X | Segelyacht 10–20 t |

---

## 5. Hersteller-Datenbank

### 5.1 Raymarine (FLIR Systems / Teledyne FLIR)

| Merkmal | Information |
|---------|------------|
| **Hauptsitz** | Fareham, Hampshire, UK |
| **Muttergesellschaft** | Teledyne FLIR (seit 2021) |
| **Gegründet** | 1923 (als Kelvin Hughes), Marke Raymarine seit 2001 |
| **Marktsegment** | Freizeit-Yachten, 25–80 ft |
| **Autopilot-Serie** | Evolution (EV-100 bis EV-400) |
| **Alleinstellungsmerkmal** | EV-1 Sensor Core: 9-Achsen-AHRS, kein separater Kompass nötig. Adaptive Algorithmen (AI-gestütztes Seegangslernen). SeaTalk-NG-Ökosystem. |
| **Stärken** | Breites Produktportfolio, gute Dokumentation, weltweit Servicenetzwerk, intuitive Bedienung |
| **Schwächen** | SeaTalk-NG-Lock-in (Adapter für NMEA 2000 nötig), Premium-Preise, Ersatzteil-Verfügbarkeit teils eingeschränkt |
| **Kompatibilität** | SeaTalk-NG (proprietär, NMEA-2000-kompatibel über Adapter), SeaTalk1 (Legacy) |
| **Typische Preisspanne** | 2.500–15.000 € (Komplettsystem) |
| **Garantie** | 2 Jahre Standard, 3 Jahre bei Registrierung |
| **Support** | Tel., E-Mail, Online-Wissensdatenbank, YouTube-Kanal |
| **Website** | www.raymarine.com |

### 5.2 B&G (Navico / Brunswick)

| Merkmal | Information |
|---------|------------|
| **Hauptsitz** | Fareham, Hampshire, UK |
| **Muttergesellschaft** | Navico Group (Brunswick Corporation, seit 2021) |
| **Gegründet** | 1956 (Brookes & Gatehouse) |
| **Marktsegment** | Performance-Segelyachten, Regatta und Bluewater |
| **Autopilot-Serie** | NAC-1, NAC-2, NAC-3 mit Precision-9 Compass |
| **Alleinstellungsmerkmal** | Optimiert für Segeln: Wind-Modus, Segel-Algorithmen, Layline-Berechnung. H5000-Integration für Performance-Segler. |
| **Stärken** | Beste Segel-Algorithmen, Performance-Daten-Integration, Regatta-Modus, leichte und kompakte Hardware |
| **Schwächen** | Kleines Händlernetz außerhalb UK/ANZ/US, teuer, begrenzte Motor-Optimierung |
| **Kompatibilität** | NMEA 2000 nativ, kein proprietärer Bus |
| **Typische Preisspanne** | 3.000–18.000 € (Komplettsystem) |
| **Garantie** | 2 Jahre |
| **Website** | www.bandg.com |

### 5.3 Garmin (Marine Division)

| Merkmal | Information |
|---------|------------|
| **Hauptsitz** | Olathe, Kansas, USA |
| **Gegründet** | 1989 |
| **Marktsegment** | Breit: von 20 ft Sportbooten bis 60 ft Motoryachten |
| **Autopilot-Serie** | GHP Reactor (40, Compact, 12, 20, 30) |
| **Alleinstellungsmerkmal** | Shadow Drive: AP deaktiviert sich bei manueller Radsteuerung automatisch. Tiefe Integration mit Garmin-Plottern. Steer-by-Wire-Unterstützung. |
| **Stärken** | Größtes Händlernetz weltweit, intuitive Touchscreen-Bedienung, Shadow Drive, exzellente Plotter-Integration |
| **Schwächen** | Segler-Algorithmen weniger ausgereift als B&G, weniger Modelle für große Yachten, Garmin-Ökosystem-Lock-in |
| **Kompatibilität** | NMEA 2000 nativ |
| **Typische Preisspanne** | 2.000–12.000 € (Komplettsystem) |
| **Garantie** | 2 Jahre |
| **Website** | www.garmin.com/marine |

### 5.4 Simrad (Navico / Brunswick)

| Merkmal | Information |
|---------|------------|
| **Hauptsitz** | Egersund, Norwegen |
| **Muttergesellschaft** | Navico Group (Brunswick Corporation) |
| **Gegründet** | 1946 (Simonsen Elektro AS) |
| **Marktsegment** | Motoryachten, Fischer-/Arbeitsboote, professionelle Schifffahrt |
| **Autopilot-Serie** | AC12N, AC42N, AC70 + AP44/IS42 Bedienung |
| **Alleinstellungsmerkmal** | HS75 GNSS-Kompass mit ±0,3° Genauigkeit. Professionelle Heritage (kommerzielle Schifffahrt). Robuste Hydraulikpumpen. |
| **Stärken** | Professionelle Qualität, exzellente Hydraulik-Systeme, HS75 bester Heading-Sensor im Segment, gute Motor-Algorithmen |
| **Schwächen** | Segel-Modus weniger entwickelt als B&G, Bedienkonzept eher funktional als intuitiv |
| **Kompatibilität** | NMEA 2000 nativ, SimNet (Legacy-kompatibel) |
| **Typische Preisspanne** | 2.500–20.000 € (Komplettsystem) |
| **Garantie** | 2 Jahre |
| **Website** | www.simrad-yachting.com |

### 5.5 Furuno (Japan)

| Merkmal | Information |
|---------|------------|
| **Hauptsitz** | Nishinomiya, Hyogo, Japan |
| **Gegründet** | 1948 |
| **Marktsegment** | Professionelle Schifffahrt, Fischerei, gehobene Motoryachten |
| **Autopilot-Serie** | NAVpilot 300, NAVpilot 700 |
| **Alleinstellungsmerkmal** | Fantum-Feedback: AI-basierte adaptive Regelung, die Seegang und Boot-Verhalten lernt. Professionelle Qualität japanischer Fertigung. GNSS-Kompass SC-33/SC-50. |
| **Stärken** | Höchste Verarbeitungsqualität, professionelle Zuverlässigkeit, exzellente Sensoren, langfristig verfügbare Ersatzteile |
| **Schwächen** | Hoher Preis, wenig Segel-spezifische Funktionen, kleineres Händlernetz für Freizeitboote |
| **Kompatibilität** | NMEA 2000, NMEA 0183, CAN-Bus proprietär |
| **Typische Preisspanne** | 5.000–25.000 € (Komplettsystem) |
| **Garantie** | 2 Jahre (3 Jahre bei Registrierung) |
| **Website** | www.furuno.com |

### 5.6 Lecomble & Schmitt (Frankreich)

| Merkmal | Information |
|---------|------------|
| **Hauptsitz** | Lorient, Bretagne, Frankreich |
| **Gegründet** | 1861 |
| **Marktsegment** | Professionelle Steueranlagen, OEM-Zulieferer für Werften |
| **Autopilot-Serie** | Hydraulische Steueranlagen mit AP-Integration |
| **Alleinstellungsmerkmal** | OEM-Lieferant für Beneteau, Jeanneau, Dufour, Lagoon. Komplette hydraulische Steuerungssysteme inkl. AP-Vorbereitung. Made in France seit über 160 Jahren. |
| **Stärken** | Höchste hydraulische Qualität, direkte Integration in Neuboot-Steueranlagen, lange Lebensdauer (25+ Jahre), breite OEM-Verbreitung |
| **Schwächen** | Kein eigener Autopilot-Controller (nur Hydraulik-Komponenten), schwer als Aftermarket zu beziehen, wenig Endkunden-Support |
| **Kompatibilität** | Kompatibel mit Raymarine, B&G, Simrad AP-Pumpen über Standard-Hydraulikanschlüsse |
| **Typische Preisspanne** | 800–5.000 € (nur Hydraulik-Komponenten) |
| **Website** | www.lecomble-schmitt.com |

### 5.7 NKE Marine Electronics (Frankreich)

| Merkmal | Information |
|---------|------------|
| **Hauptsitz** | Hennebont, Bretagne, Frankreich |
| **Gegründet** | 1984 |
| **Marktsegment** | Hochleistungs-Segelyachten, Regatta, Offshore-Rennen |
| **Autopilot-Serie** | Gyropilot 2, Gyropilot 3 |
| **Alleinstellungsmerkmal** | Entwickelt von Regattaseglern für Regattasegler. Gyropilot gewinnt regelmäßig beim Vendée Globe und Mini Transat. Schnellste Regelung im Markt. |
| **Stärken** | Schnellste Reaktionszeit, beste Performance bei schwerem Wetter, leichteste Hardware, Regatta-erprobt |
| **Schwächen** | Nischen-Hersteller, kleines Händlernetz, hoher Preis, wenig Komfort-Features |
| **Kompatibilität** | NMEA 2000, proprietärer NKE-Bus |
| **Typische Preisspanne** | 4.000–15.000 € |
| **Website** | www.nke-marine-electronics.com |

### 5.8 Hersteller-Vergleichsmatrix — Installationsrelevant

| Kriterium | Raymarine | B&G | Garmin | Simrad | Furuno | NKE |
|-----------|-----------|-----|--------|--------|--------|-----|
| NMEA 2000 nativ | Adapter | Ja | Ja | Ja | Ja | Adapter |
| Kompass integriert | EV-1 (exzellent) | Precision-9 | Smart Heading | HS60/HS75 | SC-33 | Eigener |
| Auto-Compass-Swing | Ja | Ja | Ja | Ja | Ja | Ja |
| Rudersensor inkl. | Separat | Separat | Separat | Separat | Separat | Separat |
| Installations-Doku | ★★★★★ | ★★★★ | ★★★★★ | ★★★★ | ★★★★ | ★★★ |
| Retrofit-Eignung | ★★★★★ | ★★★★ | ★★★★★ | ★★★★ | ★★★ | ★★★ |
| Segel-Optimierung | ★★★★ | ★★★★★ | ★★★ | ★★★ | ★★ | ★★★★★ |
| Motor-Optimierung | ★★★★ | ★★★ | ★★★★★ | ★★★★★ | ★★★★★ | ★★ |
| Preis-Leistung | ★★★★ | ★★★ | ★★★★★ | ★★★★ | ★★★ | ★★★ |

---

## 6. Fehlerbild-Atlas

### 6.0 Fehlerbild-Übersicht

| ID | Bezeichnung | Häufigkeit | Schwere | Kategorie |
|----|-------------|-----------|---------|-----------|
| F-INS-01 | Falscher Kompass-Standort | Sehr häufig (25%) | HIGH | compass |
| F-INS-02 | Kabelquerschnitt zu klein | Häufig (20%) | HIGH | electrical |
| F-INS-03 | Rudersensor falsch kalibriert | Häufig (18%) | MEDIUM | calibration |
| F-INS-04 | NMEA-2000-Bus-Fehler | Häufig (14%) | HIGH | network |
| F-INS-05 | Magnetische Störung durch Lautsprecher | Häufig (15%) | MEDIUM | compass |
| F-INS-06 | Hydrauliksystem nicht entlüftet | Häufig (30% bei Hydraulik) | MEDIUM | hydraulic |
| F-INS-07 | Falsche Antriebsrichtung | Mittel (8%) | HIGH | mechanical |
| F-INS-08 | Unzureichende Batterie-Kapazität | Mittel (10%) | MEDIUM | electrical |
| F-INS-09 | Mechanisches Spiel im Antriebsgestänge | Mittel (8%) | MEDIUM | mechanical |
| F-INS-10 | Falsche Hydraulikflüssigkeit | Selten (3%) | CRITICAL | hydraulic |
| F-INS-11 | Kompass-Interferenz durch Wechselrichter | Mittel (10%) | MEDIUM | compass |
| F-INS-12 | Drop-Kabel zu lang / Stern-Topologie | Mittel (10%) | MEDIUM | network |

**Visuelle Erkennungsmerkmale für AYDI-Bildanalyse:**

| Fehlerbild | Visuell erkennbar? | Indikatoren für Fotoanalyse |
|------------|-------------------|----------------------------|
| F-INS-01 | JA (visual_medium) | Kompass-Position relativ zu Lautsprechern/Motor sichtbar |
| F-INS-02 | JA (visual_medium) | Kabelquerschnitt visuell schätzbar, Kabelbeschriftung lesbar |
| F-INS-03 | NEIN (visual_insufficient) | Kalibrierung nicht visuell beurteilbar |
| F-INS-04 | JA (visual_low) | Topologie teilweise sichtbar, Terminatoren erkennbar |
| F-INS-05 | JA (visual_high) | Lautsprecher und Kompass auf einem Foto: Abstand messbar |
| F-INS-06 | NEIN (visual_insufficient) | Luft im System nicht visuell erkennbar |
| F-INS-07 | NEIN (visual_insufficient) | Richtung nur im Betrieb prüfbar |
| F-INS-08 | JA (visual_low) | Batterie-Größe/Typ visuell schätzbar |
| F-INS-09 | JA (visual_medium) | Spiel an Gabelkopf/Bolzen visuell erkennbar |
| F-INS-10 | JA (visual_medium) | Hydrauliköl-Farbe erkennbar (klar vs. rot vs. trüb) |
| F-INS-11 | JA (visual_medium) | Wechselrichter-Position relativ zu Kompass sichtbar |
| F-INS-12 | JA (visual_low) | Kabel-Topologie teilweise sichtbar |

### 6.1 Fehlerbild F-INS-01: Falscher Kompass-Standort

| Attribut | Beschreibung |
|----------|-------------|
| **Bezeichnung** | Kompass neben magnetischer Störquelle montiert |
| **Häufigkeit** | Sehr häufig (25 % aller Installationsfehler) |
| **Symptome** | Autopilot steuert dauerhaft einen falschen Kurs; Kursabweichung variiert mit der Richtung (Deviation); Autopilot „jagt" — permanent Kurskorrekturen ohne ruhig zu laufen; Nach Compass-Swing: Restdeviation >±8° |
| **Typische Ursachen** | Lautsprecher (Permanentmagnet) innerhalb 1m; Motorblock zu nah; Stahlkette im Ankerkasten direkt unter Kompass; Magnetische Schrankverschlüsse in der Nähe; Wechselrichter oder Ladegerät direkt neben Kompass |
| **Diagnose** | 1. Compass-Swing durchführen und Deviationstabelle erstellen; 2. Deviation >±5° auf einzelnen Kursen → gerichtete Störquelle; 3. Handkompass um Sensorposition kreisen und Abweichung notieren; 4. Verdächtige Geräte einzeln ein/ausschalten und Kompass-Anzeige beobachten |
| **Behebung** | Sensor an anderen Standort versetzen (mind. 1m von Störquelle); Alternativ: Störquelle entfernen (z.B. Lautsprecher umsetzen); Erneuter Compass-Swing |
| **Prävention** | Vor der Installation magnetische Vermessung des Einbauorts; Herstellerangaben zu Mindestabständen einhalten; Kompass-Standort als erstes bestimmen, bevor alles andere montiert wird |
| **AYDI-Confidence** | visual_medium (Standort-Fotos), documented (Deviationstabelle) |

### 6.2 Fehlerbild F-INS-02: Kabelquerschnitt zu klein

| Attribut | Beschreibung |
|----------|-------------|
| **Bezeichnung** | Unzureichender Leiterquerschnitt der Antriebsstromversorgung |
| **Häufigkeit** | Häufig (20 % aller Installationsfehler) |
| **Symptome** | Autopilot funktioniert bei ruhiger See, versagt bei Seegang; Antrieb „brummt" aber bewegt das Ruder nicht; „Low Voltage"-Alarm am Controller; Sicherung löst bei starken Ruderbewegungen aus; Motor wird ungewöhnlich heiß |
| **Typische Ursachen** | Standardkabel 2,5mm² für einen 25A-Antrieb verwendet; Lange Kabelwege nicht berücksichtigt (>8m einfach); Billig-Kabel ohne Verzinnung (Korrosion → höherer Widerstand); Übergangswiderstände an Klemmstellen (schlechte Crimps) |
| **Diagnose** | 1. Spannung direkt an der Batterie messen: z.B. 12,6V; 2. Spannung am Antrieb messen bei Volllast: z.B. 10,8V; 3. Differenz = Spannungsabfall: 1,8V = 14,3% → viel zu hoch!; 4. Einzelne Streckenabschnitte messen (Batterie→Sicherung→Schalter→Antrieb) |
| **Behebung** | Kabel durch korrekten Querschnitt ersetzen (Tabelle Abschnitt 2.2.2); Alle Crimp-Verbindungen erneuern; Kabelweg verkürzen wenn möglich; Auf 24V-System umrüsten (halber Strom) |
| **Prävention** | Spannungsabfall-Berechnung VOR der Installation; Kabelquerschnitt immer eine Stufe größer als Minimum; Nur verzinntes Marinekabel verwenden; Professionell crimpen (hexagonal) |
| **AYDI-Confidence** | measured (Spannungsmessung), calculated (Querschnittsberechnung) |

### 6.3 Fehlerbild F-INS-03: Rudersensor falsch kalibriert

| Attribut | Beschreibung |
|----------|-------------|
| **Bezeichnung** | Fehlerhafte Rudersensor-Kalibrierung oder mechanisches Spiel |
| **Häufigkeit** | Häufig (18 % aller Installationsfehler) |
| **Symptome** | Boot steuert dauerhaft leicht Backbord oder Steuerbord; Autopilot „pumpt" — rhythmisches Hin- und Herruddern; Angezeigte Ruderlage stimmt nicht mit tatsächlicher überein; Autopilot gibt „Rudder Limit"-Alarm obwohl noch Weg frei ist |
| **Typische Ursachen** | Mittellage nicht exakt kalibriert (Offset 2–5°); Endanschläge nicht korrekt gesetzt; Mechanisches Spiel in der Sensoranlenkung (>2°); Sensor-Hebel verrutscht (Klemmschraube locker); Korrosion am Potentiometer (Widerstandssprünge) |
| **Diagnose** | 1. Ruder mechanisch in Mittelstellung bringen; 2. Rudersensor-Anzeige ablesen → Differenz = Offset; 3. Ruder langsam von BB nach StB drehen und Anzeige beobachten (Sprünge?); 4. Sensorhebel bei fixiertem Ruder bewegen → Spiel erkennbar; 5. Sensor-Widerstand mit Multimeter messen (bei Poti-Typ): gleichmäßig ansteigend? |
| **Behebung** | Neukalibrierung: Mittelstellung + Endanschläge; Mechanisches Spiel beseitigen (Klemmschraube, Gabelkopf, Bolzen); Bei Poti-Verschleiß: Sensor ersetzen; Upgrade auf berührungslosen Sensor (Hall/RVDT) |
| **Prävention** | Kalibrierung auf dem Wasser (nicht an Land mit aufgebocktem Boot); Kalibrierung nach jeder Ruder-/Steuerungsarbeit wiederholen; Berührungslose Sensoren bevorzugen (kein Verschleiß) |
| **AYDI-Confidence** | measured (Sensordaten), visual_medium (Einbaufotos) |

### 6.4 Fehlerbild F-INS-04: NMEA-2000-Bus-Fehler

| Attribut | Beschreibung |
|----------|-------------|
| **Bezeichnung** | Fehlerhafte NMEA-2000-Bus-Installation |
| **Häufigkeit** | Häufig (14 % aller Installationsfehler) |
| **Symptome** | Intermittierender Datenverlust (Heading, GPS, Ruderlage); Autopilot verliert plötzlich den Kurs und gibt Alarm; Geräte erscheinen und verschwinden auf dem Netzwerk; „No Data" auf einzelnen Instrumenten; Autopilot funktioniert mal, mal nicht (wetterabhängig → Feuchtigkeit) |
| **Typische Ursachen** | Fehlender Terminator (eines oder beide Enden); Stern-Topologie statt Backbone; Drop-Kabel >6m; Schirm an mehreren Punkten geerdet (Erdschleife); Korrodierte Stecker (nicht wasserdicht montiert); Überlastung der Bus-Stromversorgung (>3A / >60 LEN) |
| **Diagnose** | 1. Bus-Widerstand messen (beide Terminatoren angeschlossen): soll 60 Ω (2×120 Ω parallel); 2. Nur ein Terminator: 120 Ω; 3. Kein Terminator: ∞; 4. Bus-Spannung messen: soll 9–16V DC; 5. Geräte-Scan am Plotter: alle Geräte sichtbar?; 6. Drop-Kabel nacheinander entfernen und Bus beobachten |
| **Behebung** | Terminatoren überprüfen und ggf. ergänzen; Topologie korrigieren (linear, nicht Stern); Drop-Kabel kürzen (<6m); Schirm-Erdung auf einen Punkt reduzieren; Korrodierte Stecker ersetzen und mit Fett schützen |
| **Prävention** | Bus vor Installation planen (Zeichnung mit Backbone-Route); Hochwertige Stecker und Kabelverschraubungen verwenden; Bus-Widerstand nach jeder Änderung messen; Schirm nur am Stromeingang erden |
| **AYDI-Confidence** | measured (Bus-Messung), documented (Netzwerk-Scan) |

### 6.5 Fehlerbild F-INS-05: Magnetische Störung durch Lautsprechermagnet

| Attribut | Beschreibung |
|----------|-------------|
| **Bezeichnung** | Permanentmagnet eines Lautsprechers verursacht Kompass-Deviation |
| **Häufigkeit** | Häufig (15 % aller Kompass-Probleme) |
| **Symptome** | Konstante Deviation auf bestimmten Kursen; Deviation ändert sich wenn Stereoanlage ein/ausgeschaltet wird (bei Elektromagneten); Deviation verschwindet wenn Lautsprecher temporär entfernt wird; Auffällige Halbkreis-Deviation (Koeffizient B oder C dominant) |
| **Typische Ursachen** | Lautsprecher im Achterschiff, 50 cm vom Heading-Sensor entfernt; Subwoofer unter der Sitzbank nahe Kompass-Position; Bluetooth-Lautsprecher temporär neben Kompass abgelegt |
| **Diagnose** | 1. Handkompass neben jeden Lautsprecher halten: Ablenkung messbar?; 2. Lautsprecher temporär entfernen und Compass-Swing vergleichen; 3. Deviation mit und ohne Musik vergleichen (bei Elektromagnet-Anteilen) |
| **Behebung** | Lautsprecher umsetzen (mind. 1,5m Abstand); Alternativ: Kompass umsetzen; Auf Neodym-freie Lautsprecher umrüsten (marine-spezifisch); Nach Umbau: erneuter Compass-Swing |
| **Prävention** | Lautsprecherposition in der Installationsplanung berücksichtigen; Marine-Lautsprecher mit abgeschirmten Magneten verwenden; Kompass-Standort-Evaluation vor Lautsprecher-Einbau |
| **AYDI-Confidence** | measured (Deviationsmessung), visual_high (Standort-Fotos mit Abstandsmessung) |

### 6.6 Fehlerbild F-INS-06: Hydrauliksystem nicht entlüftet

| Attribut | Beschreibung |
|----------|-------------|
| **Bezeichnung** | Luft im Hydrauliksystem nach Autopilot-Installation |
| **Häufigkeit** | Häufig bei Hydraulik-Neuinstallation (30 % aller Hydraulik-Einbauten) |
| **Symptome** | Ruder reagiert verzögert auf AP-Kommandos; Überschwinger (Overshoot) bei Kursänderungen; Ruder fühlt sich „schwammig" an bei manueller Steuerung; Blubbernde Geräusche bei Ruderbewegung; AP pumpt hin und her ohne stabilen Kurs |
| **Diagnose** | 1. Manuell steuern: fühlt sich das Ruder fest oder schwammig an?; 2. Hydraulikflüssigkeits-Niveau prüfen (gesunken = Luft im System); 3. Entlüftungsventil öffnen: Blasen sichtbar?; 4. Bei transparenten Leitungen: Blasen sichtbar? |
| **Behebung** | Komplette Entlüftung (siehe Abschnitt 2.5.3); Vorratsbehälter nachfüllen; Leitungsanschlüsse auf Dichtheit prüfen (Lufteintritt); 3–5 Entlüftungszyklen durchführen |
| **Prävention** | Leitungen vor Befüllung mit Druckluft auf Dichtheit prüfen; Sorgfältige Erstbefüllung (langsam, Öl blasenfrei einfüllen); 5 Entlüftungszyklen als Minimum nach Neuinstallation |
| **AYDI-Confidence** | measured (Ölstand, Drucktest), visual_medium (Blasen sichtbar) |

### 6.7 Fehlerbild F-INS-07: Falsche Antriebsrichtung

| Attribut | Beschreibung |
|----------|-------------|
| **Bezeichnung** | Autopilot-Antrieb steuert in die falsche Richtung |
| **Häufigkeit** | Mittel (8 % aller Installationsfehler) |
| **Symptome** | Boot dreht bei Kurskorrektur in die falsche Richtung; Autopilot „dreht sich im Kreis" (positive Rückkopplung statt Regelung); Sofortiges Ausbrechen nach Autopilot-Aktivierung; Controller gibt „Drive Error" oder „Off Course"-Alarm |
| **Diagnose** | 1. Autopilot aktivieren, Kurs um 10° nach Steuerbord ändern; 2. Beobachten: dreht das Ruder nach Steuerbord (korrekt) oder Backbord (falsch)?; 3. Im Menü „Rudder Direction" oder „Drive Direction" prüfen |
| **Behebung** | Im Controller-Menü: „Reverse Drive" oder „Drive Direction" umschalten; Alternative: Motorkabel (Plus/Minus) am Antrieb tauschen; Bei Hydraulik: Leitungen am Zylinder tauschen |
| **Prävention** | Antriebsrichtung als ERSTEN Test nach Installation durchführen; Controller-Einrichtungsassistent korrekt durchlaufen (Frage nach Antriebsrichtung) |
| **AYDI-Confidence** | measured (Beobachtung Ruderbewegung) |

### 6.8 Fehlerbild F-INS-08: Unzureichende Batterie-Kapazität

| Attribut | Beschreibung |
|----------|-------------|
| **Bezeichnung** | Batterie-System kann Autopilot-Verbrauch nicht decken |
| **Häufigkeit** | Mittel (10 % aller Installations-Probleme, insbesondere bei Retrofit) |
| **Symptome** | Autopilot funktioniert 2–4 Stunden, dann „Low Voltage"-Alarm; Bordspannung fällt unter 11,5V bei AP-Betrieb; Nach Nachtfahrt: Batterie leer, kein Motorstart möglich; Autopilot schaltet sich bei Bugstrahlruder-Betrieb ab (Spannungseinbruch) |
| **Diagnose** | 1. Stromverbrauch des AP über 24h berechnen (Ø 3–8A je nach System/See); 2. Verfügbare Batterie-Kapazität: Ah × 50% (nur 50% entladen!); 3. Ladebilanz erstellen: Verbrauch vs. Erzeugung (Lichtmaschine, Solar, Wind); 4. Spannung unter Last messen (AP + Plotter + Instrumente + Beleuchtung gleichzeitig) |
| **Behebung** | Batterie-Kapazität erhöhen (zusätzliche Batterie); Ladeleistung verbessern (Solar, höhere Lichtmaschine); Dedizierte AP-Batterie (separater Batteriekreis); Auf 24V umstellen (halbierter Strom = geringere Verluste) |
| **Prävention** | Energiebilanz VOR der Installation erstellen; Faustregel: min. 200 Ah Kapazität für AP-Betrieb (12V, Langfahrt); Ladebilanz muss positiv sein über 24h-Zyklus |
| **AYDI-Confidence** | measured (Spannungs-/Strommessung), calculated (Energiebilanz) |

### 6.9 Fehlerbild F-INS-09: Mechanisches Spiel im Antriebsgestänge

| Attribut | Beschreibung |
|----------|-------------|
| **Bezeichnung** | Spiel in der mechanischen Verbindung zwischen Antrieb und Ruder |
| **Häufigkeit** | Mittel (8 %, zunehmend mit Alter der Installation) |
| **Symptome** | Klackende Geräusche bei jeder Kurskorrektur; Autopilot „jagt" — hochfrequentes Hin-und-Her-Ruddern; Rudersensor zeigt Bewegung, Boot reagiert nicht (Spiel wird „verbraucht"); Kurs weicht langsam ab, dann plötzliche heftige Korrektur |
| **Diagnose** | 1. Antrieb fixieren, Quadrant von Hand bewegen: >1° Spiel = zu viel; 2. Gabelkopf-Bolzen prüfen: Spiel sichtbar/fühlbar?; 3. Linearantrieb-Kolbenstange: Seitenspiel?; 4. Quadrant-Klemmung auf Ruderschaft: Rutscht der Quadrant? |
| **Behebung** | Gabelkopf-Bolzen ersetzen (korrekter Durchmesser); Gabelkopf mit geringerem Spiel einsetzen; Quadrant-Klemmung nachziehen; Bei Seilzug: Seilspannung nachjustieren; Bei Hydraulik: Zylinder-Aufhängung prüfen |
| **Prävention** | Hochwertige Gabelköpfe und Bolzen (A4-80, passgenau); Spiel jährlich prüfen (Winterlager-Checkliste); Seilspannung alle 6 Monate kontrollieren |
| **AYDI-Confidence** | measured (Spielmessung in Grad), visual_high (Spiel sichtbar bei Inspektion) |

### 6.10 Fehlerbild F-INS-10: Falsche Hydraulikflüssigkeit

| Attribut | Beschreibung |
|----------|-------------|
| **Bezeichnung** | Verwendung der falschen oder gemischten Hydraulikflüssigkeit |
| **Häufigkeit** | Selten aber schwerwiegend (3 %, fast immer bei Retrofit) |
| **Symptome** | Ruder wird zunehmend schwergängig (Dichtungsquellung); Hydrauliköl-Leckage an Zylinder-Dichtungen; Trübe oder verklumpte Hydraulikflüssigkeit; Steuerung versagt vollständig (GAU) |
| **Diagnose** | 1. Hydrauliköl-Typ anhand Farbe und Geruch identifizieren; 2. Hersteller-Spezifikation prüfen (Steueranlage UND AP-Pumpe); 3. Öl-Probe entnehmen: klar oder trüb? Partikel sichtbar? |
| **Behebung** | System komplett spülen (3-faches Volumen durchspülen); Alle Dichtungen inspizieren (gequollen?); Korrekte Flüssigkeit einfüllen; Entlüften; Im schlimmsten Fall: Zylinder-Überholung mit neuen Dichtungen |
| **Prävention** | Hydrauliköl-Typ auf dem Vorratsbehälter notieren; Ersatz-Öl nur vom Steueranlagen-Hersteller beziehen; Niemals „irgendein Hydrauliköl" verwenden; Vor Mischen: Kompatibilität prüfen (NIEMALS mischen im Zweifel!) |
| **AYDI-Confidence** | measured (Ölanalyse), visual_medium (Leckage, Farbe) |

### 6.11 Fehlerbild F-INS-11: Kompass-Interferenz durch Wechselrichter

| Attribut | Beschreibung |
|----------|-------------|
| **Bezeichnung** | Elektromagnetische Störung des Kompasses durch Wechselrichter oder Ladegerät |
| **Häufigkeit** | Mittel (10 % aller Kompass-Probleme, zunehmend mit Wechselrichter-Verbreitung) |
| **Symptome** | Kompass springt bei Wechselrichter-Einschaltung; Kurs-Rauschen nimmt zu wenn Wechselrichter unter Last; Deviation ändert sich mit Wechselrichter-Last; Periodische Kurs-Schwankungen im Takt der Wechselrichter-Frequenz |
| **Diagnose** | 1. Wechselrichter aus → Kompass-Verhalten beobachten; 2. Wechselrichter ein (ohne Last) → Kompass beobachten; 3. Wechselrichter ein (mit Last) → Kompass beobachten; 4. EMV-Feld mit Handkompass nahe Wechselrichter messen |
| **Behebung** | Wechselrichter oder Kompass umsetzen (mind. 1,5m Abstand); Wechselrichter-Kabel verdrillen; Ferritkerne auf Wechselrichter-Kabel; EMV-Abschirmung um Wechselrichter; Geschirmtes Kompass-Kabel verwenden |
| **Prävention** | Wechselrichter-Position bei Kompass-Standortwahl berücksichtigen; Hochwertigen Wechselrichter mit geringer EMV-Abstrahlung wählen (reiner Sinus); Wechselrichter-Kabel nicht parallel zum Kompass-Kabel |
| **AYDI-Confidence** | measured (Deviationsmessung mit/ohne Wechselrichter) |

### 6.12 Fehlerbild F-INS-12: Drop-Kabel zu lang / Stern-Topologie

| Attribut | Beschreibung |
|----------|-------------|
| **Bezeichnung** | NMEA-2000-Netzwerk mit fehlerhafter Topologie oder zu langen Drop-Kabeln |
| **Häufigkeit** | Mittel (10 % aller NMEA-2000-Probleme) |
| **Symptome** | Intermittierender Datenverlust bei hoher Bus-Last; Einzelne Geräte fallen sporadisch vom Bus; Bus-Fehlerrate steigt bei Seegang (Kabel bewegen sich); Plotter zeigt „NMEA 2000 Error" oder Geräte verschwinden temporär |
| **Diagnose** | 1. Netzwerk-Topologie zeichnen: ist es ein linearer Bus oder ein Stern?; 2. Drop-Kabel-Längen messen: >6m?; 3. Bus-Scan: alle Geräte sichtbar?; 4. Bus-Widerstand: 60 Ω an beiden Enden? |
| **Behebung** | Topologie korrigieren: Stern → linearer Bus; Drop-Kabel kürzen: alle ≤6m; Backbone-Kabel ggf. verlängern um Geräte näher ans Backbone zu bringen; T-Stücke umsetzen |
| **Prävention** | NMEA-2000-Bus vor Installation auf Papier planen; Backbone-Route durch das Boot festlegen (Bug→Heck); T-Stücke an Gerätepositionen verteilen; Drop-Kabel maximal 3m planen (Reserve für 6m) |
| **AYDI-Confidence** | measured (Bus-Messung), documented (Topologie-Zeichnung) |

---

## 7. Troubleshooting-Entscheidungsbäume

### 7.1 Entscheidungsbaum 1: Autopilot steuert falschen Kurs

```
START: Autopilot steuert dauerhaft einen falschen Kurs
│
├─ Ist die Abweichung konstant auf allen Kursen?
│   ├─ JA → Kompass-Fehlausrichtung
│   │   ├─ Sensor-Ausrichtung prüfen (±2° zur Schiffslängsachse?)
│   │   ├─ Heading-Offset im Controller-Menü prüfen
│   │   └─ Kompass neu ausrichten und Compass-Swing wiederholen
│   │
│   └─ NEIN → Deviation (richtungsabhängig)
│       ├─ Ist die Deviation sinusförmig über 360°?
│       │   ├─ JA → Permanentmagnet in der Nähe
│       │   │   ├─ Lautsprecher prüfen (Abstand?)
│       │   │   ├─ Magnetverschlüsse prüfen
│       │   │   ├─ Kühlschrank-Kompressor prüfen
│       │   │   └─ Störquelle entfernen/versetzen → Compass-Swing
│       │   │
│       │   └─ NEIN → Ist die Deviation auf 2 gegenüberliegenden Kursen?
│       │       ├─ JA → Weicheisen-Deviation (Quadrantaldeviation)
│       │       │   ├─ Ferromagnetisches Material nahe Kompass?
│       │       │   ├─ Kiel-Bolzen, Motorblock in der Nähe?
│       │       │   └─ Compass-Swing sollte dies kompensieren
│       │       │       ├─ Kompensation erfolgreich? → OK
│       │       │       └─ Kompensation nicht erfolgreich → Sensor umsetzen
│       │       │
│       │       └─ NEIN → Variable Deviation
│       │           ├─ Ändert sich die Deviation mit ein/aus von Geräten?
│       │           │   ├─ JA → EMV-Störung
│       │           │   │   ├─ Wechselrichter?
│       │           │   │   ├─ Lichtmaschine?
│       │           │   │   ├─ LED-Dimmer?
│       │           │   │   └─ Störquelle identifizieren → Abstand/Schirmung
│       │           │   │
│       │           │   └─ NEIN → Veränderliche Eisenmassen?
│       │           │       ├─ Ankerkette (Menge variiert)
│       │           │       ├─ Gasflaschen (Füllstand variiert)
│       │           │       └─ Konserven-Vorräte (Menge variiert)
│       │           │           └─ Sensor weiter von variablen Quellen entfernen
│       │           │
│       └─ Rudersensor-Offset?
│           ├─ Rudermittellage prüfen (Sensor vs. tatsächlich)
│           ├─ Offset >2° → Rudersensor neu kalibrieren
│           └─ Offset <2° → Nicht die Ursache
│
└─ ENDE: Kurs korrekt nach Maßnahme
```

### 7.2 Entscheidungsbaum 2: Autopilot reagiert nicht / kein Antrieb

```
START: Autopilot aktiviert, aber Ruder bewegt sich nicht
│
├─ Anzeige am Controller vorhanden?
│   ├─ NEIN → Stromversorgung prüfen
│   │   ├─ Sicherung Controller intakt?
│   │   │   ├─ NEIN → Sicherung ersetzen, Ursache für Auslösung suchen
│   │   │   └─ JA → Spannung am Controller messen
│   │   │       ├─ 0V → Kabelbruch oder Schalter aus
│   │   │       ├─ <10V → Batterie leer oder Kabel zu dünn
│   │   │       └─ 12–14V → Controller defekt
│   │   │
│   └─ JA → Controller hat Strom
│       ├─ Zeigt Controller Fehlermeldung?
│       │   ├─ „No Drive" → NMEA-Bus-Problem oder Antriebskabel
│       │   │   ├─ NMEA-2000-Verbindung Controller↔Antrieb prüfen
│       │   │   ├─ Antrieb-Sicherung prüfen
│       │   │   ├─ Antrieb-Stecker kontrollieren
│       │   │   └─ Antrieb direkt mit 12V versorgen: läuft er?
│       │   │       ├─ JA → NMEA-2000 oder Controller-Problem
│       │   │       └─ NEIN → Antrieb defekt
│       │   │
│       │   ├─ „No Heading" → Kompass-Problem
│       │   │   ├─ Kompass auf NMEA-2000-Bus sichtbar?
│       │   │   │   ├─ NEIN → Kompass-Kabel, Kompass-Stromversorgung
│       │   │   │   └─ JA → Kompass sendet keine Daten (PGN 127250)
│       │   │   │       ├─ Kompass kalibriert?
│       │   │   │       └─ Kompass defekt? (Sensor-Selbsttest)
│       │   │   │
│       │   ├─ „No Rudder" → Rudersensor-Problem
│       │   │   ├─ Rudersensor auf NMEA-2000-Bus sichtbar?
│       │   │   ├─ Rudersensor-Kabel intakt?
│       │   │   ├─ Rudersensor kalibriert?
│       │   │   └─ Rudersensor defekt?
│       │   │
│       │   └─ „Off Course" → Bereits vor Fehler aktiv
│       │       ├─ Antrieb hat Kraft, aber Boot folgt nicht
│       │       ├─ Mechanisches Problem: Bypass offen? Seilzug gerissen?
│       │       └─ Antrieb zu schwach für Bedingungen
│       │
│       └─ Keine Fehlermeldung, aber kein Antrieb
│           ├─ Autopilot wirklich aktiviert? (Standby vs. Auto)
│           ├─ Kurs-Vorgabe vorhanden? (Heading-Modus vs. Track-Modus)
│           └─ Totband-Einstellung prüfen (zu groß?)
│
└─ ENDE: Antrieb funktioniert nach Maßnahme
```

### 7.3 Entscheidungsbaum 3: NMEA-2000-Netzwerkprobleme

```
START: Geräte fallen vom NMEA-2000-Bus / intermittierender Datenverlust
│
├─ Bus-Widerstand messen (beide Terminatoren angeschlossen)
│   ├─ ∞ (unendlich) → Kein Terminator angeschlossen
│   │   └─ Beide Terminatoren (120Ω) einsetzen → soll 60Ω ergeben
│   │
│   ├─ 120 Ω → Nur ein Terminator
│   │   └─ Zweiten Terminator am anderen Backbone-Ende einsetzen
│   │
│   ├─ 60 Ω → Korrekt terminiert, Problem liegt woanders
│   │   ├─ Bus-Spannung messen
│   │   │   ├─ <9V → Stromversorgung unzureichend
│   │   │   │   ├─ Bus-Sicherung prüfen
│   │   │   │   ├─ Bus-Stromquelle prüfen
│   │   │   │   └─ LEN-Budget berechnen (>60 LEN = überlastet)
│   │   │   │
│   │   │   ├─ 9–16V → Spannung OK
│   │   │   │   ├─ Problem tritt nur bei bestimmtem Gerät auf?
│   │   │   │   │   ├─ JA → Gerät oder dessen Drop-Kabel defekt
│   │   │   │   │   │   ├─ Drop-Kabel tauschen
│   │   │   │   │   │   ├─ Gerät an anderem T-Stück testen
│   │   │   │   │   │   └─ Gerät einzeln am Bus testen
│   │   │   │   │   │
│   │   │   │   │   └─ NEIN → Allgemeines Bus-Problem
│   │   │   │   │       ├─ Topologie prüfen (Stern-Abzweige?)
│   │   │   │   │       ├─ Backbone-Stecker einzeln prüfen (Korrosion?)
│   │   │   │   │       ├─ Backbone-Kabel auf Knicke prüfen
│   │   │   │   │       └─ Drop-Kabel-Längen prüfen (alle <6m?)
│   │   │   │   │
│   │   │   └─ >16V → Überspannung (selten, Laderegler-Problem)
│   │   │       └─ Bus-Stromversorgung stabilisieren
│   │   │
│   ├─ <60 Ω → Kurzschluss oder zu viele Terminatoren
│   │   ├─ Mehr als 2 Terminatoren im Netz? → Überzählige entfernen
│   │   └─ Kurzschluss in einem Kabel? → Backbone abschnittsweise prüfen
│   │
│   └─ >120 Ω → Unterbrechung im Backbone
│       └─ Backbone abschnittsweise auf Durchgang prüfen
│
└─ ENDE: Bus stabil, alle Geräte sichtbar
```

### 7.4 Entscheidungsbaum 4: Autopilot „pumpt" / Overshoot

```
START: Autopilot macht permanente Kurskorrekturen, Boot giert hin und her
│
├─ Ist das Problem bei ALLEN Bedingungen oder nur bei Seegang?
│   ├─ NUR bei Seegang → PID-Abstimmung (Seegangsfilter)
│   │   ├─ Counter-Rudder / Sea State Einstellung erhöhen
│   │   ├─ Rudder Gain reduzieren
│   │   ├─ Totband vergrößern (2–5° bei Seegang)
│   │   └─ Bei modernen Systemen: Auto-Seegangsfilter aktivieren
│   │
│   └─ BEI ALLEN Bedingungen → Mechanisches oder Kalibrierungsproblem
│       ├─ Mechanisches Spiel prüfen
│       │   ├─ Gabelkopf-Bolzen: Spiel >1mm?
│       │   │   ├─ JA → Bolzen/Gabelkopf ersetzen
│       │   │   └─ NEIN → Weiter
│       │   ├─ Seilzug: Lose?
│       │   │   ├─ JA → Nachspannen
│       │   │   └─ NEIN → Weiter
│       │   └─ Hydraulik: Luft im System?
│       │       ├─ JA → Entlüften (Abschnitt 2.5.3)
│       │       └─ NEIN → Weiter
│       │
│       ├─ Rudersensor-Kalibrierung prüfen
│       │   ├─ Mittellage korrekt?
│       │   │   ├─ NEIN → Neu kalibrieren
│       │   │   └─ JA → Weiter
│       │   ├─ Endanschläge korrekt?
│       │   │   ├─ NEIN → Neu kalibrieren
│       │   │   └─ JA → Weiter
│       │   └─ Linearität prüfen (10°, 20°, 30° → stimmt Anzeige?)
│       │       ├─ NEIN → Sensor defekt oder Anlenkung verbogen
│       │       └─ JA → Weiter
│       │
│       ├─ PID-Parameter prüfen
│       │   ├─ Rudder Gain zu hoch? → Reduzieren (Start: 50%)
│       │   ├─ Counter-Rudder zu niedrig? → Erhöhen
│       │   ├─ Rudder Damping (D-Anteil) aktiv? → Aktivieren/Erhöhen
│       │   └─ Auto-Tune verfügbar? → Durchführen (ruhige See, geradeaus)
│       │
│       └─ Kompass-Problem?
│           ├─ Kompass-Rauschen prüfen (Heading-Anzeige stabil?)
│           ├─ EMV-Störung? (Geräte ein/ausschalten)
│           └─ Compass-Swing wiederholen
│
└─ ENDE: Stabiler Kurs nach Maßnahme
```

### 7.5 Entscheidungsbaum 5: Spannungsabfall-Diagnose

```
START: Verdacht auf Spannungsabfall in der Autopilot-Versorgung
│
├─ Schritt 1: Spannung an der Batterie messen (unter Last)
│   └─ Notieren: V_batterie = ___V (soll: 12,5–14,4V / 25–28,8V)
│
├─ Schritt 2: Spannung am Hauptschalter-Ausgang messen
│   ├─ Differenz zu V_batterie >0,1V?
│   │   ├─ JA → Schalter-Kontaktwiderstand zu hoch
│   │   │   └─ Schalter reinigen oder ersetzen
│   │   └─ NEIN → OK, weiter
│
├─ Schritt 3: Spannung am Sicherungshalter-Ausgang messen
│   ├─ Differenz zum Schalter >0,1V?
│   │   ├─ JA → Sicherungshalter korrodiert
│   │   │   └─ Kontakte reinigen, Halter ggf. ersetzen
│   │   └─ NEIN → OK, weiter
│
├─ Schritt 4: Spannung am Antrieb messen (unter Volllast!)
│   ├─ Gesamter Spannungsabfall berechnen: V_batterie - V_antrieb = V_drop
│   ├─ V_drop < 3% (0,36V bei 12V / 0,72V bei 24V)? 
│   │   ├─ JA → Spannung OK, Problem liegt woanders
│   │   └─ NEIN → Kabel zu dünn oder zu lang
│   │       ├─ Kabelquerschnitt messen/prüfen
│   │       ├─ Kabellänge messen
│   │       ├─ Berechnung: Soll-Querschnitt (Tabelle 2.2.2)
│   │       ├─ Ist < Soll → Kabel ersetzen
│   │       └─ Ist ≥ Soll → Übergangswiderstände suchen
│   │           ├─ Crimp-Verbindungen einzeln prüfen
│   │           ├─ Korrodierte Klemmen?
│   │           └─ Schadhafte Isolierung (Feuchtigkeit)?
│
├─ Schritt 5: Masse-Rückleitung prüfen
│   ├─ Masse am Antrieb gegen Masse an Batterie messen
│   ├─ >0,1V Differenz? → Masse-Problem
│   │   ├─ Masse-Kabel gleicher Querschnitt wie Plus?
│   │   ├─ Masse-Verbindung an Sammelschiene fest?
│   │   └─ Korrosion an Masseklemmen?
│   └─ <0,1V → Masse OK
│
└─ ENDE: Spannungsabfall im Toleranzbereich nach Maßnahme
```

### 7.6 Entscheidungsbaum 6: Hydraulik-Probleme

```
START: Hydraulik-Autopilot funktioniert nicht korrekt
│
├─ Ruder bewegt sich gar nicht bei AP-Aktivierung?
│   ├─ JA → Mechanisches/Hydraulisches Problem
│   │   ├─ Bypass-Ventil prüfen: offen oder geschlossen?
│   │   │   ├─ OFFEN → Bypass schließen (manuell oder Solenoid-Steuerung prüfen)
│   │   │   └─ GESCHLOSSEN → Weiter
│   │   ├─ Hydraulikflüssigkeits-Stand prüfen
│   │   │   ├─ LEER/NIEDRIG → Auffüllen, Leckage suchen, Entlüften
│   │   │   └─ OK → Weiter
│   │   ├─ AP-Pumpe läuft hörbar?
│   │   │   ├─ NEIN → Elektrisches Problem (Sicherung, Kabel, Motor)
│   │   │   └─ JA → Pumpe läuft aber kein Druck
│   │   │       ├─ Internes Bypass in der Pumpe defekt?
│   │   │       ├─ Hydraulikleitung abgeknickt?
│   │   │       ├─ Leckage an Fittings?
│   │   │       └─ Pumpe verschlissen (kein Druckaufbau)?
│   │   │
│   └─ NEIN → Ruder bewegt sich, aber schlecht
│       ├─ Ruder reagiert verzögert
│       │   ├─ Luft im System? → Entlüften
│       │   ├─ Leitungen zu lang? → Kürzere Route
│       │   └─ Hydrauliköl-Viskosität falsch? → Spezifikation prüfen
│       │
│       ├─ Ruder bewegt sich ruckartig
│       │   ├─ Luft im System (große Blasen) → Entlüften
│       │   ├─ Solenoid-Ventil flattert → Elektrik prüfen
│       │   └─ Pumpe verschlissen (intermittierend) → Pumpe tauschen
│       │
│       └─ Ruder bewegt sich nur in eine Richtung
│           ├─ Magnetventil klemmt (eine Seite) → Ventil reinigen/tauschen
│           ├─ Hydraulikleitung verstopft → Leitungen durchspülen
│           └─ Pumpe intern defekt (ein Kanal) → Pumpe tauschen
│
└─ ENDE: Hydraulik funktioniert nach Maßnahme
```

### 7.7 Entscheidungsbaum 7: Kompass-Kalibrierung fehlgeschlagen

```
START: Compass-Swing wird vom System abgelehnt / hohe Restdeviation
│
├─ System meldet "Calibration Failed"
│   ├─ Wurde das Boot komplett 360° gedreht?
│   │   ├─ NEIN → Erneut versuchen, vollständige Drehung
│   │   └─ JA → Weiter
│   ├─ War die Drehung gleichmäßig (90–180 Sekunden pro Umdrehung)?
│   │   ├─ NEIN → Langsamer und gleichmäßiger drehen
│   │   └─ JA → Weiter
│   ├─ War das Boot während des Swings in Fahrt (min. 2 kn)?
│   │   ├─ NEIN → Einige Systeme benötigen Fahrt → unter Motor drehen
│   │   └─ JA → Weiter
│   ├─ Magnetische Störung zu stark
│   │   ├─ Handkompass-Test am Sensorstandort: >10° Ablenkung?
│   │   │   ├─ JA → Sensor umsetzen, dann erneut kalibrieren
│   │   │   └─ NEIN → Weiter
│   │   ├─ Variable Störquelle während Swing aktiv?
│   │   │   ├─ Bugstrahlruder genutzt zum Drehen? → NUR Ruder verwenden!
│   │   │   ├─ Lichtmaschine-Last schwankend? → Konstante Last sicherstellen
│   │   │   └─ Andere EMV-Quellen? → Ausschalten
│   │
│   └─ Sensor-Hardware-Problem
│       ├─ Sensor korrekt befestigt (vibrationsfrei)?
│       ├─ Sensor-Kabel intakt (NMEA-2000-Verbindung stabil)?
│       └─ Sensor defekt? → Factory Reset, dann erneut versuchen
│
├─ Kalibrierung abgeschlossen, aber Restdeviation >±5°
│   ├─ Deviation gleichmäßig über alle Kurse?
│   │   ├─ JA → Sehr starke aber konstante Quelle → Sensor umsetzen
│   │   └─ NEIN → Gerichtete Störung
│   │       ├─ Auf welchen Kursen ist die Deviation maximal?
│   │       ├─ In dieser Richtung nach Störquellen suchen
│   │       ├─ Systematisch Störquellen entfernen/versetzen
│   │       └─ Nach jeder Änderung: erneuter Compass-Swing
│
└─ ENDE: Restdeviation ≤±3° nach Maßnahme
```

---

## 8. FAQ — Häufige Fragen

### 8.1 Allgemeine Installation

**F1: Kann ich den Autopilot selbst einbauen oder brauche ich eine Werft?**
A: Ein technisch versierter Eigner kann einen Tiller-Piloten oder Wheel-Drive selbst einbauen. Linear- und Hydraulik-Systeme erfordern fundierte Kenntnisse in Elektrik, Mechanik und idealerweise NMEA 2000. Fehler bei der Installation sind die Hauptursache für Autopilot-Probleme. Eine professionelle Installation kostet 800–2.000 € (je nach Komplexität) und ist in der Regel gut investiert. **(confidence: estimated)**

**F2: Wie lange dauert eine professionelle Autopilot-Installation?**
A: Tiller-Pilot: 4–6 Stunden. Wheel-Drive: 6–8 Stunden. Linearantrieb mit NMEA 2000: 12–20 Stunden. Hydraulik mit neuem Leitungssystem: 16–30 Stunden. Plus 3–6 Stunden für Kalibrierung und Seatrial. **(confidence: documented)**

**F3: Muss der Kompass separat gekauft werden?**
A: Bei modernen Systemen (Raymarine Evolution, B&G NAC mit Precision-9, Garmin Reactor) ist der Heading-Sensor im Lieferumfang der Komplettkits enthalten. Bei Einzelkomponenten-Kauf muss er separat bestellt werden. Der Heading-Sensor ist die kritischste Komponente — hier nicht sparen! **(confidence: documented)**

**F4: Kann ich meinen bestehenden Raymarine SeaTalk1-Autopiloten mit einem neuen NMEA-2000-Plotter verbinden?**
A: Ja, über einen Konverter (Raymarine E22158 oder Actisense NGW-1). Allerdings ist die Datenübertragung auf Standard-PGNs beschränkt — erweiterte Funktionen wie Track-Modus oder Wegpunkt-Steuerung funktionieren möglicherweise nicht. Bei einem System älter als 8–10 Jahre empfiehlt sich der komplette Austausch. **(confidence: documented)**

**F5: Kann ich einen B&G-Autopiloten mit einem Garmin-Plotter betreiben?**
A: Grundsätzlich ja, über NMEA 2000. Standard-Funktionen (Heading-Hold, Track-Modus) funktionieren herstellerübergreifend. Erweiterte Funktionen (z.B. Route-Tracking mit automatischem Wenden) erfordern möglicherweise Geräte des gleichen Herstellers. Testen Sie die gewünschten Funktionen vor dem Kauf. **(confidence: documented)**

### 8.2 NMEA 2000

**F6: Muss ich für den Autopiloten ein komplettes NMEA-2000-Netzwerk aufbauen?**
A: Ja, moderne Autopiloten kommunizieren ausschließlich über NMEA 2000 (oder SeaTalk-NG). Ein minimales Netzwerk besteht aus: Backbone-Kabel, 2 Terminatoren, Stromversorgung, T-Stücke für jedes Gerät. Starter-Kits gibt es für ca. 150–300 €. **(confidence: documented)**

**F7: Wie messe ich, ob mein NMEA-2000-Bus korrekt terminiert ist?**
A: Bus stromlos machen. Multimeter auf Widerstandsmessung. An den beiden CAN-H und CAN-L Pins messen (Pin 4 und 5 am DeviceNet-Micro-Stecker). Soll-Wert: 60 Ω (zwei 120-Ω-Terminatoren parallel). 120 Ω = ein Terminator fehlt. ∞ = kein Terminator. **(confidence: measured)**

**F8: Kann ich SeaTalk-NG und NMEA 2000 mischen?**
A: Ja, über Adapter (Raymarine A06045/A06075). SeaTalk-NG ist physisch kompatibel mit NMEA 2000, nutzt aber einen anderen Steckertyp. Das Backbone kann entweder SeaTalk-NG oder NMEA-2000-Kabel sein (beides funktioniert). Proprietäre SeaTalk-NG-Funktionen sind nur zwischen Raymarine-Geräten verfügbar. **(confidence: documented)**

**F9: Mein NMEA-2000-Bus verliert sporadisch Geräte. Was tun?**
A: Systematisch vorgehen: 1. Terminierung prüfen (60 Ω). 2. Bus-Spannung prüfen (9–16V). 3. Drop-Kabel-Längen prüfen (<6m). 4. Topologie prüfen (linear, kein Stern). 5. Stecker auf Korrosion prüfen. 6. Schirm nur an einem Punkt geerdet? 7. Geräte einzeln abklemmen und beobachten. **(confidence: documented)**

### 8.3 Kompass und Kalibrierung

**F10: Wie oft muss ich den Compass-Swing wiederholen?**
A: Mindestens einmal jährlich (Saisonbeginn). Zusätzlich nach jeder Änderung in der Nähe des Kompasses: neuer Lautsprecher, neue Elektronik, Kielbolzen-Austausch, Motorwechsel, Umstellung auf LED-Beleuchtung. Auch nach einem Blitzschlag. **(confidence: estimated)**

**F11: Mein Autopilot „jagt" — was bedeutet das?**
A: „Jagen" bedeutet, der Autopilot macht permanente Kurskorrekturen ohne einen stabilen Kurs zu finden. Ursachen: zu hoher Rudder Gain, mechanisches Spiel, Kompass-Rauschen, Luft in der Hydraulik, oder falsch kalibrierter Rudersensor. Siehe Entscheidungsbaum 4 (Abschnitt 7.4). **(confidence: documented)**

**F12: Kann ich den Kompass im Motorraum montieren?**
A: Grundsätzlich nein. Der Motorblock ist die stärkste einzelne Störquelle an Bord (5–20° Deviation). Ausnahme: GPS-Kompasse (Dual-Antenne) sind unempfindlich gegen magnetische Störungen und können überall montiert werden — allerdings benötigen sie freie GPS-Sicht (Decksmontage). **(confidence: documented)**

**F13: Was ist besser: Fluxgate-Kompass oder Solid-State-IMU?**
A: Solid-State-IMU (9-Achsen) ist in fast allen Belangen überlegen: schnellere Reaktion, geringeres Rauschen, kein mechanischer Verschleiß, integrierte Roll/Pitch-Kompensation. Fluxgate hat Vorteile bei extremer Kälte (<-20°C) und bei sehr starken magnetischen Störungen (weniger sensitiv = weniger gestört). Für 99 % der Yachten ist eine IMU die bessere Wahl. **(confidence: documented)**

**F14: Mein Kompass zeigt 5° Deviation auf Nordkurs. Ist das normal?**
A: Vor der Kompensation (Compass-Swing): ja, durchaus normal. Nach der Kompensation: nein, 5° Restdeviation ist zu viel. Ursache suchen: Permanentmagnet in der Nähe? Ferromagnetisches Material? Fehlausrichtung des Sensors? Ziel: <±2° nach Kompensation. **(confidence: documented)**

### 8.4 Antrieb und Mechanik

**F15: Hydraulik oder Linear — was ist besser?**
A: Wenn das Boot bereits eine hydraulische Steueranlage hat: Hydraulik-Autopilot (einfacherer Einbau, nutzt vorhandene Infrastruktur). Bei mechanischer Steueranlage (Seilzug/Gestänge): Linearantrieb. Hydraulik ist kraftvoller und langlebiger, aber komplexer. Linear ist einfacher und wartungsärmer, aber weniger kräftig bei großen Booten. **(confidence: estimated)**

**F16: Wie viel Strom verbraucht ein Autopilot im Durchschnitt?**
A: Tiller-Pilot: 1–3 A (12V). Linearantrieb: 2–5 A Durchschnitt, 15–25 A Peak. Hydraulikpumpe: 3–8 A Durchschnitt, 25–60 A Peak. Durchschnittlicher 24h-Verbrauch bei Segeln: 40–80 Ah (12V). Der Verbrauch hängt stark vom Seegang, der Boot-Balance und der PID-Einstellung ab. **(confidence: estimated)**

**F17: Brauche ich einen separaten Rudersensor?**
A: Ja, für alle nicht-Tiller-Systeme. Der Rudersensor teilt dem Controller die aktuelle Ruderposition mit — ohne ihn kann der Autopilot nicht regeln. Tiller-Piloten messen die Kolbenposition intern. Manche hydraulischen Steueranlage-Hersteller (z.B. Lecomble & Schmitt) bieten integrierte Rudersensoren. **(confidence: documented)**

**F18: Mein Linearantrieb macht klackende Geräusche. Normal?**
A: Leichtes Klicken bei Richtungswechsel ist normal (Getriebespiel). Lautes Klacken deutet auf mechanisches Spiel in der Anlenkung hin: Gabelkopf-Bolzen ausgeschlagen, Quadrant-Klemmung locker, oder Seilzug-Nachstellung nötig. Prüfung: Antrieb fixieren, Quadrant von Hand bewegen. Spiel >1° → beheben. **(confidence: documented)**

### 8.5 Retrofit und Aufrüstung

**F19: Kann ich meinen 15 Jahre alten Raymarine ST4000+ durch ein Evolution-System ersetzen?**
A: Ja, aber es ist fast eine Neuinstallation. Der ST4000+ nutzt SeaTalk1, analoge Sensoren und einen proprietären Antrieb. Ein Evolution-System braucht SeaTalk-NG/NMEA 2000, digitale Sensoren und ggf. einen neuen Antrieb. Der mechanische Antrieb (Type 1/2/3) kann eventuell weiterverwendet werden, wenn er noch funktionsfähig ist und die Kabelstecker passen. **(confidence: documented)**

**F20: Mein Boot hat keinen NMEA-2000-Anschluss. Was kostet ein Netzwerk?**
A: Ein NMEA-2000-Starter-Kit (Backbone 10m, 2 Terminatoren, Stromversorgung, 5 T-Stücke, 5 Drop-Kabel) kostet ca. 200–400 €. Der Einbau durch eine Werft: 3–5 Stunden = 300–500 €. Gesamtkosten: 500–900 €. Empfehlung: gleich großzügig planen (genug T-Stücke für spätere Erweiterungen). **(confidence: estimated)**

**F21: Kann ich einen Garmin-Autopiloten auf einem Boot mit Teleflex-Hydraulik installieren?**
A: Ja, Garmin GHP Hydraulik-Pumpen sind kompatibel mit Standard-Hydraulikanschlüssen (JIC-Fittings). Wichtig: gleiche Hydraulikflüssigkeit verwenden wie im Teleflex-System (typisch: Mineral-Hydrauliköl HLP 15). Die Garmin-Pumpe wird parallel angeschlossen. **(confidence: documented)**

### 8.6 Kalibrierung und Abstimmung

**F22: Mein Autopilot übersteuert bei Kursänderungen. Wie stelle ich ihn ein?**
A: „Rudder Gain" oder „Helm Gain" reduzieren. Der Gain bestimmt, wie aggressiv der Autopilot auf Kursabweichungen reagiert. Zu hoch = Überschwinger. Empfehlung: bei 50 % starten und in 10%-Schritten erhöhen, bis der Kurs stabil ist ohne zu schwingen. **(confidence: documented)**

**F23: Was ist „Counter-Rudder" und wann brauche ich es?**
A: Counter-Rudder (oder „Rudder Damping") ist der D-Anteil im PID-Regler. Er bremst das Ruder ab, bevor der Sollkurs erreicht ist — verhindert Überschwinger. Besonders wichtig bei schweren Booten mit Trägheit. Höherer Counter-Rudder = sanftere Kursänderungen. **(confidence: documented)**

**F24: Soll ich die Auto-Tune-Funktion verwenden?**
A: Ja, als Ausgangspunkt. Auto-Tune fährt das Boot in definierten Manövern und misst die Bootsdynamik. Die ermittelten Parameter sind ein guter Startpunkt, können aber manuell nachoptimiert werden. Auto-Tune bei ruhiger See und Geradeausfahrt durchführen, dann unter realen Bedingungen fein-tunen. **(confidence: documented)**

**F25: Wie kalibriere ich den Rudersensor wenn das Boot an Land steht?**
A: Nur die Mittellage und Endanschläge lassen sich an Land kalibrieren. Die Feinkalibrierung muss auf dem Wasser erfolgen, da die tatsächliche Rudermittellage (Boot fährt geradeaus ohne Ruderdruck) erst im Wasser ermittelt werden kann. An Land: Ruder optisch auf Mittelachse ausrichten. **(confidence: documented)**

**F26: Mein Autopilot steuert bei Segeln viel schlechter als unter Motor. Warum?**
A: Segeln erzeugt dynamische Kräfte (Krängung, Luvgierigkeit, Winddrehungen), die den Autopiloten vor eine viel komplexere Aufgabe stellen. Lösungen: 1. Segel-Modus aktivieren (andere PID-Parameter). 2. Boot ausbalancieren (Segelwahl, Trimm). 3. Wind-Modus verwenden (steuert nach scheinbarem Wind statt Kompasskurs). 4. Bei modernen Systemen: Segel-spezifische Algorithmen aktivieren (B&G, Raymarine EV). **(confidence: documented)**

**F27: Kann ich die Kalibrierungswerte exportieren und sichern?**
A: Je nach Hersteller: Raymarine — ja, über Raymarine-App/SD-Karte. B&G — ja, über H5000/B&G-App. Garmin — teilweise (Geräte-Backup). Simrad — über NSO/NSS-Plotter. Empfehlung: Kalibrierungswerte immer zusätzlich handschriftlich notieren und im Bordbuch aufbewahren. **(confidence: documented)**

### 8.7 Spezialfälle und fortgeschrittene Themen

**F28: Mein Boot hat ein Steer-by-Wire-System. Welchen Autopilot brauche ich?**
A: Steer-by-Wire-Systeme (z.B. ZF MicroCommander, Volvo EPS) benötigen einen speziellen Autopiloten, der direkt mit dem Steer-by-Wire-Controller kommuniziert statt einen eigenen Antrieb zu nutzen. Garmin Reactor 40 unterstützt Steer-by-Wire nativ. Für andere Hersteller: Prüfen Sie die Kompatibilitätsliste. In keinem Fall einen mechanischen Antrieb nachträglich an ein Steer-by-Wire-System anbauen! **(confidence: documented)**

**F29: Wie installiere ich einen Autopiloten auf einem Katamaran mit zwei Rudern?**
A: Katamarane benötigen entweder: (a) Zwei synchronisierte Antriebe (je einer pro Ruder), gesteuert von einem Controller — dies erfordert einen leistungsfähigen Controller wie Simrad AC70 oder B&G NAC-3. Oder (b) eine Koppelstange zwischen beiden Rudern und einen einzelnen Antrieb. Lösung (b) ist einfacher und günstiger, reduziert aber die Manövrierfähigkeit bei Hafenmanövern. **(confidence: documented)**

**F30: Kann ich den Autopiloten an mein bestehendes Garmin/Furuno/Raymarine MFD-Netzwerk anschließen?**
A: Wenn das MFD NMEA 2000 unterstützt (fast alle aktuellen Modelle): ja. Der Autopilot-Controller wird über NMEA 2000 mit dem Plotter verbunden. Track-Modus (Wegpunkt-Steuerung) funktioniert herstellerübergreifend über Standard-PGNs. Erweiterte Features (z.B. Route-Änderung am Plotter → AP folgt automatisch) funktionieren am zuverlässigsten mit Geräten desselben Herstellers. **(confidence: documented)**

**F31: Was passiert bei einem Blitzschlag mit dem Autopiloten?**
A: Blitzschläge können alle elektronischen Komponenten zerstören. Am häufigsten betroffen: Heading-Sensor (MEMS-Elemente), NMEA-2000-Bus (CAN-Transceiver), Controller-Platine. Schutzmaßnahmen: Blitzableiter-System (SSM/Bonding), Überspannungsschutz am NMEA-2000-Bus (z.B. Maretron NF-NM2-CF), bei Gewitter: Geräte wenn möglich abschalten. Nach Blitzschlag: komplettem System-Check durchführen, Compass-Swing wiederholen. **(confidence: documented)**

**F32: Mein Autopilot funktioniert gut unter Motor, aber versagt bei Segeln unter Spinnaker. Was tun?**
A: Unter Spinnaker erzeugen Rollbewegungen permanente Kurskorrekturen, die den Autopiloten überfordern. Maßnahmen: 1. Sea State Filter maximieren. 2. Totband auf 5–7° vergrößern. 3. Counter-Rudder erhöhen. 4. Wind-Modus verwenden (scheinbarer Windwinkel statt Kompasskurs). 5. Segel-Balance optimieren (Vang, Barberholer). 6. Bei extremen Bedingungen: manuell steuern (AP als Assistenz, nicht als Alleinsteuerung). **(confidence: estimated)**

**F33: Welche Wartung braucht eine Autopilot-Installation jährlich?**
A: Jährliche Wartung (Saisonbeginn): 1. Alle Kabelverbindungen auf Korrosion prüfen. 2. NMEA-2000-Stecker kontrollieren (Grünspan?). 3. Rudersensor-Kalibrierung prüfen. 4. Compass-Swing wiederholen. 5. Hydraulikflüssigkeits-Stand kontrollieren. 6. Gabelkopf-Bolzen auf Spiel prüfen. 7. Antrieb unter Last testen (Ruder von Anschlag zu Anschlag). 8. Software-/Firmware-Update prüfen. Zeitaufwand: 2–4 Stunden. **(confidence: documented)**

**F34: Kann ich zwei Autopilot-Controller an einem Antrieb betreiben (z.B. innen und außen)?**
A: Die meisten Hersteller unterstützen mehrere Bedieneinheiten an einem Controller: Raymarine (mehrere p70/p70R), B&G (mehrere Triton²), Garmin (mehrere GHC), Simrad (mehrere AP44). Die Bedieneinheiten werden einfach per NMEA 2000 angeschlossen — keine zusätzliche Konfiguration nötig. Nur EIN Controller steuert den Antrieb. **(confidence: documented)**

**F35: Mein Boot hat einen Klapptrieb (Saildrive). Beeinflusst das die Autopilot-Installation?**
A: Der Saildrive selbst beeinflusst die Autopilot-Installation nicht direkt. Allerdings: Saildrive-Boote haben oft weniger Platz im Heckbereich → Linearantrieb-Montage sorgfältig planen. Der Saildrive-Motor (z.B. Yanmar/Volvo) ist eine magnetische Störquelle wie jeder Motor → Kompass-Abstand einhalten. **(confidence: documented)**

**F36: Mein Autopilot-Display zeigt "Heading Sensor Lost" alle paar Minuten. Das Problem tritt nur bei Seegang auf.**
A: Häufigste Ursache: lockerer NMEA-2000-Stecker am Heading-Sensor oder am nächsten T-Stück. Bei Seegang bewegt sich das Boot, und ein nicht richtig eingerasteter Stecker verliert kurzzeitig Kontakt. Lösung: Alle NMEA-2000-Stecker auf festen Sitz prüfen. Drop-Kabel mit Kabelbinder sichern (Zugentlastung). Bei DeviceNet-Micro-Steckern: Überwurfmutter nachziehen. **(confidence: documented)**

**F37: Welchen Einfluss hat die Wassertemperatur auf die Autopilot-Performance?**
A: Direkt keinen. Indirekt: In kalten Gewässern (<5°C) wird Hydraulikflüssigkeit zähflüssiger → Pumpe braucht mehr Strom, Reaktion langsamer. Lösung: Hydrauliköl mit niedrigerer Viskosität verwenden (HLP 15 statt HLP 22). Bei elektronischen Kompassen: Temperaturkompensation ist eingebaut (kein Problem). Bei extremer Kälte (<-20°C): Fluxgate-Kompasse können zuverlässiger sein als MEMS-IMUs. **(confidence: estimated)**

**F38: Kann ich meinen Autopiloten mit einem AIS-System koppeln, um Kollisionen zu vermeiden?**
A: Nein, kein kommerziell erhältlicher Yacht-Autopilot führt automatische Ausweichmanöver basierend auf AIS-Daten durch. AIS-Daten können auf dem Plotter angezeigt werden, und der Rudergänger kann den AP-Kurs manuell ändern. Automatische Kollisionsvermeidung ist Gegenstand aktueller Forschung, aber noch nicht marktverfügbar (Stand 2026). **(confidence: documented)**

**F39: Mein Boot hat ein Flettner-Ruder (Servo-Pendel-Ruder). Kann ich dort einen Autopilot anschließen?**
A: Bei Flettner-Ruder-Systemen (z.B. Aries, Monitor) wird ein kleines Hilfsruder gesteuert, das wiederum das Hauptruder bewegt. Ein elektronischer Autopilot wird in der Regel am Hauptruder-Quadranten installiert (normaler Linearantrieb). Die Windfahnensteuerung ist dann ein separates, unabhängiges System — ideal als Backup. Nicht den Autopilot am Flettner-Ruder selbst betreiben! **(confidence: documented)**

**F40: Wie schütze ich die Autopilot-Elektronik vor Feuchtigkeit?**
A: 1. Controller und Kompass in trockenen, belüfteten Bereichen montieren (nicht im Bilge-Bereich). 2. Alle Kabelverbindungen mit Schrumpfschlauch (klebend) schützen. 3. NMEA-2000-Stecker mit Kontaktfett (z.B. Caig DeoxIT) behandeln. 4. Kabeldurchführungen durch Schotten mit IP67-Kabelverschraubungen. 5. Bei Spray-Exposition (Cockpit): wasserdichte Bedieneinheiten verwenden (alle modernen Modelle sind IPX6/IPX7). 6. Silica-Gel-Beutel in geschlossenen Elektronik-Gehäusen. **(confidence: documented)**

**F41: Mein Autopilot funktioniert, aber der Stromverbrauch ist doppelt so hoch wie erwartet. Was stimmt nicht?**
A: Hoher Stromverbrauch deutet auf ständige Ruderkorrekturen hin. Ursachen: 1. Boot schlecht balanciert (Luvgierigkeit → permanente Gegenruder). 2. Rudersensor-Offset (AP steuert dauerhaft leicht gegen). 3. Mechanisches Spiel (AP korrigiert ständig). 4. Gain zu hoch eingestellt. 5. Kompass-Rauschen (EMV). 6. Verschmutzter Rumpf (höherer Widerstand → mehr Kraft nötig). 7. Hydraulik: interne Leckage der Pumpe (Öl fließt intern zurück). **(confidence: documented)**

**F42: Gibt es eine maximale Umgebungstemperatur für Autopilot-Komponenten?**
A: Ja. Die meisten Autopilot-Controller und Heading-Sensoren sind für -15°C bis +55°C Umgebungstemperatur spezifiziert. Im Maschinenraum kann es im Sommer (Mittelmeer, Karibik) 60–70°C heiß werden → Controller und Kompass NICHT direkt am Motor oder in unbelüfteten Maschinenräumen montieren! Linearantriebe sind bis +70°C spezifiziert. Hydraulikpumpen bis +80°C. **(confidence: documented)**

---

## 9. Glossar

| Nr. | Begriff | Erklärung |
|-----|---------|-----------|
| 1 | **AHRS** | Attitude and Heading Reference System — kombiniert Beschleunigungs-, Drehraten- und Magnetsensoren zu einer stabilen Lage- und Kursreferenz |
| 2 | **Backbone** | Hauptkabel des NMEA-2000-Netzwerks, linearer Bus von Terminator zu Terminator |
| 3 | **Bypass-Ventil** | Ventil, das den Autopilot-Hydraulikkreis vom manuellen Steuerkreis trennt oder verbindet |
| 4 | **CAN-Bus** | Controller Area Network — Basis-Protokoll von NMEA 2000, 250 kbit/s |
| 5 | **Compass-Swing** | Kalibrierungsverfahren: Boot dreht 360° während Kompass Messpunkte sammelt |
| 6 | **Counter-Rudder** | D-Anteil (Differenzial) im PID-Regler, bremst Ruderbewegung vor Erreichen des Sollkurses |
| 7 | **Cross Track Error (XTE)** | Querabweichung des Bootes vom geplanten Kurs (in m oder nm) |
| 8 | **Deadband / Totband** | Kursabweichung, innerhalb derer der Autopilot nicht reagiert (typisch 1–5°) |
| 9 | **Deviation** | Ablenkung des Kompasses durch bordeigende magnetische Störquellen, kursabhängig |
| 10 | **DeviceNet Micro** | Steckerstandard für NMEA 2000, 5-polig, M12-ähnlich |
| 11 | **Drive Unit** | Der Antrieb des Autopiloten (Motor, Pumpe, Aktuator) |
| 12 | **Drop-Kabel** | Verbindung vom NMEA-2000-T-Stück zum einzelnen Gerät, max. 6m |
| 13 | **EMV** | Elektromagnetische Verträglichkeit — Fähigkeit von Geräten, sich nicht gegenseitig zu stören |
| 14 | **Fluxgate-Kompass** | Magnetfeldsensor mit zwei Spulen, misst Erdmagnetfeld zur Kursbestimmung |
| 15 | **Gain** | Verstärkungsfaktor (P-Anteil im PID-Regler), bestimmt Aggressivität der Kurskorrektur |
| 16 | **Gabelkopf** | Mechanisches Verbindungselement am Linearantrieb, verbindet Kolbenstange mit Quadrant |
| 17 | **Helm-Pumpe** | Manuelle Hydraulikpumpe am Steuerrad zur Handsteuerung |
| 18 | **Hub (Stroke)** | Maximaler linearer Weg des Autopilot-Kolbens in mm |
| 19 | **Hydraulikflüssigkeit** | Druckübertragungsmedium im hydraulischen Steuersystem (Mineralöl, ATF oder synthetisch) |
| 20 | **IMU** | Inertial Measurement Unit — Kombination aus Beschleunigungs- und Drehratensensoren |
| 21 | **JIC-Fitting** | Joint Industry Council Standard-Hydraulikanschluss, 37°-Flanke |
| 22 | **Krängung** | Seitliche Neigung des Bootes (Roll), beeinflusst Kompassmessung |
| 23 | **LEN** | Load Equivalence Number — Maß für den Stromverbrauch eines NMEA-2000-Geräts (1 LEN = 50 mA) |
| 24 | **Linearantrieb** | Elektromechanischer Antrieb mit Spindelgetriebe, erzeugt lineare Kraft |
| 25 | **Luvgierigkeit** | Tendenz eines Segelboots, in den Wind zu drehen (Weather Helm) |
| 26 | **Magnetische Variation** | Differenz zwischen magnetischem und geographischem Nordpol, ortsabhängig |
| 27 | **Missweisung** | Deutsches Synonym für magnetische Variation |
| 28 | **NMEA 2000** | National Marine Electronics Association Standard 2000 — digitales Datennetzwerk für Schiffselektronik |
| 29 | **Overshoot** | Überschwinger — Boot dreht über den Sollkurs hinaus bevor es zurückkorrigiert |
| 30 | **PGN** | Parameter Group Number — Datentelegramm-Kennung im NMEA-2000-Protokoll |
| 31 | **PID-Regler** | Proportional-Integral-Differenzial-Regler — Kern-Algorithmus der Kursregelung |
| 32 | **Quadrant** | Halbkreisförmiger Hebel auf dem Ruderschaft, an dem Steuerseil und Linearantrieb angreifen |
| 33 | **Rudersensor** | Sensor, der die aktuelle Ruderlage misst und an den Autopilot-Controller meldet |
| 34 | **RVDT** | Rotary Variable Differential Transformer — berührungsloser Drehwinkelsensor |
| 35 | **Sea State Filter** | Algorithmus, der Seegangs-induzierte Kursschwankungen filtert, um unnötige Ruderbewegungen zu vermeiden |
| 36 | **SeaTalk-NG** | Raymarine-proprietäres Netzwerk, physisch NMEA-2000-kompatibel, eigener Steckertyp |
| 37 | **SeaTalk1** | Älteres Raymarine-Netzwerk (3-Draht, proprietär), nicht NMEA-2000-kompatibel |
| 38 | **Shadow Drive** | Garmin-Funktion: AP deaktiviert sich automatisch bei manueller Radsteuerung |
| 39 | **Solenoid-Ventil** | Elektromagnetisch betätigtes Ventil (z.B. Bypass im Hydrauliksystem) |
| 40 | **Spannungsabfall** | Spannungsverlust in der Zuleitung durch Kabellängenwiderstand und Kontaktwiderstände |
| 41 | **Terminator** | 120-Ω-Abschlusswiderstand an beiden Enden des NMEA-2000-Backbones |
| 42 | **Tiller-Pilot** | Kompakter Autopilot-Antrieb für Pinnensteuerung, direkt zwischen Cockpit und Pinne |
| 43 | **Verzinnung** | Beschichtung von Kupferleitern mit Zinn zum Schutz vor Salzwasserkorrosion |
| 44 | **Wheel-Drive** | Autopilot-Antrieb, der direkt am Steuerrad angreift (Reibrad, Kette oder Riemen) |
| 45 | **XTE** | Cross Track Error — Querabweichung vom geplanten Kurs (= Cross Track Error) |
| 46 | **Bonding** | Elektrische Verbindung aller metallischen Teile des Boots zum Potentialausgleich |
| 47 | **SSM** | Single Side Band Marine — Seefunk-System, starke EMV-Quelle bei Sendebetrieb |
| 48 | **Ferritkern** | Ringförmiger Kern aus Ferritmaterial, reduziert hochfrequente EMV-Störungen auf Kabeln |
| 49 | **Erdschleife** | Unbeabsichtigte Stromschleife durch mehrfache Erdungspunkte, verursacht EMV-Störungen |
| 50 | **JIC** | Joint Industry Council — Standard für Hydraulik-Rohrverschraubungen mit 37°-Konus |
| 51 | **ANL-Sicherung** | Großformatige Schmelzsicherung für Hochstrom-Anwendungen (Autopilot-Antrieb) |
| 52 | **Crimp-Verbindung** | Mechanische Kabelverbindung durch Verpressen eines Kabelschuhs, Standard im Marinebereich |
| 53 | **Hexagonal-Crimp** | Professionelles Crimpprofil (6-eckig), gasdicht, geringster Übergangswiderstand |
| 54 | **Kabelschuh** | Endstück für Kabelanschlüsse: Ringkabelschuh (geschlossen) oder Gabelkabelschuh (offen) |
| 55 | **IP67** | Schutzart: staubdicht + Schutz gegen zeitweiliges Untertauchen (30 min, 1m) |
| 56 | **Seatrial** | Probefahrt zur Abstimmung und Verifizierung der Autopilot-Installation |
| 57 | **PID-Parameter** | Die drei Stellgrößen des PID-Reglers: Proportional (Gain), Integral (Reset), Differenzial (Counter-Rudder) |
| 58 | **Track-Modus** | Autopilot folgt einer GPS-Route (Wegpunkt zu Wegpunkt) statt einem Kompasskurs |
| 59 | **Wind-Modus** | Autopilot hält einen konstanten Windwinkel (scheinbar oder wahr) statt eines Kompasskurses |
| 60 | **VMG** | Velocity Made Good — Geschwindigkeitskomponente direkt zum Ziel (Luv oder Lee) |
| 61 | **Luvgierigkeit** | Tendenz eines Segelboots, in den Wind zu drehen — Autopilot muss permanent gegenhalten |
| 62 | **Leegierigkeit** | Tendenz eines Segelboots, vom Wind abzufallen — seltener, ebenfalls AP-relevant |
| 63 | **Ruderquadrant** | Halbkreisförmiger Hebel auf dem Ruderschaft zur Übertragung der Steuerkräfte |
| 64 | **Kolbenstange** | Bewegliches Element des Linearantriebs, überträgt die Kraft auf den Quadranten |
| 65 | **Druckverformungsrest** | Bleibende Verformung nach Druckbelastung (relevant für Hydraulik-Dichtungen) |
| 66 | **SAE J844** | Standard für Nylon-Hydraulikleitungen im Marinebereich |
| 67 | **CuNi 90/10** | Kupfer-Nickel-Legierung (90% Cu, 10% Ni) für korrosionsbeständige Hydraulikleitungen |
| 68 | **Fantum-Feedback** | Furuno-Technologie: AI-basierte adaptive Regelung, lernt Bootsdynamik |
| 69 | **MEMS** | Micro-Electro-Mechanical Systems — Miniatur-Sensortechnologie (Beschleunigung, Drehrate) |
| 70 | **Neodym** | Seltene-Erden-Magnet, extrem stark, verbaut in Lautsprechern — stärkste Kompass-Störquelle |

---

## 10. Schnell-Referenz

### 10.1 Installations-Checkliste (Kurzform)

```
MECHANIK
□ Antriebstyp passend zum Steuersystem gewählt
□ Antrieb korrekt ausgerichtet und verschraubt
□ Montageplatte auf Rumpfstruktur (nicht nur GFK-Haut)
□ Gabelkopf/Bolzen passgenau, Spiel <0,5mm
□ Kolbenstange bei Rudermittellage auf 50% Hub
□ Endanschläge 5° vor mechanischem Limit
□ Rudersensor montiert und anlenkungsfrei

ELEKTRIK
□ Leiterquerschnitt berechnet (max. 3% Spannungsabfall)
□ Verzinntes Marinekabel verwendet
□ Alle Crimps hexagonal, mit Schrumpfschlauch
□ Sicherung träge, 150% Nennstrom, max. 200mm von Batterie
□ Getrennte Kabelwege Starkstrom / Signal (min. 200mm)
□ Alle Durchführungen wasserdicht (IP67+)

NMEA 2000
□ Linearer Backbone (kein Stern)
□ 2 Terminatoren (120Ω je Ende)
□ Bus-Widerstand = 60Ω
□ Drop-Kabel alle <6m
□ Bus-Spannung 9–16V DC
□ LEN-Budget <60
□ Schirm nur 1× geerdet

KOMPASS
□ Mindestabstände eingehalten (Tabelle 2.3.1)
□ Sensor ±2° zur Schiffslängsachse ausgerichtet
□ Montage vibrationsfrei auf festem Untergrund
□ Compass-Swing durchgeführt
□ Restdeviation <±3°

KALIBRIERUNG
□ Rudersensor: Mittellage, Endanschläge, Linearität
□ Antriebsrichtung korrekt (StB-Kommando → StB-Ruder)
□ Totband eingestellt (Segeln: 3°, Motor: 1°)
□ Seatrial durchgeführt (ruhige See + Seegang)
□ PID-Parameter fein-justiert
```

### 10.2 Schnelldiagnose-Tabelle

| Symptom | Wahrscheinlichste Ursache | Erste Maßnahme |
|---------|--------------------------|----------------|
| AP steuert falschen Kurs | Kompass-Deviation | Compass-Swing wiederholen |
| AP reagiert nicht | Sicherung, Kabel, NMEA-Bus | Sicherung + Spannung prüfen |
| AP „pumpt" hin und her | Mech. Spiel oder Gain zu hoch | Spiel prüfen, Gain reduzieren |
| AP schaltet bei Seegang ab | Spannungsabfall | Spannung unter Last messen |
| Ruder schwammig (Hydraulik) | Luft im System | Entlüften |
| Rudder Limit Alarm | Rudersensor-Endanschläge | Endanschläge neu kalibrieren |
| NMEA-Geräte verschwinden | Terminierung / Stecker | Bus-Widerstand messen |
| No Heading Alarm | Kompass-Kabel / Kompass defekt | Kompass auf Bus sichtbar? |
| Boot dreht in falsche Richtung | Antriebsrichtung invertiert | Drive Reverse im Menü |
| Low Voltage Alarm | Kabelquerschnitt / Batterie | Spannung am Antrieb messen |

### 10.3 Leiterquerschnitt-Schnellreferenz (12V, max. 3% Spannungsabfall)

```
Strom × einfache Kabellänge → Querschnitt

10A × 4m  =  4 mm²     |  20A × 4m  = 10 mm²     |  30A × 4m  = 16 mm²
10A × 6m  =  6 mm²     |  20A × 6m  = 10 mm²     |  30A × 6m  = 16 mm²
10A × 8m  =  6 mm²     |  20A × 8m  = 16 mm²     |  30A × 8m  = 25 mm²
10A × 10m = 10 mm²     |  20A × 10m = 16 mm²     |  30A × 10m = 25 mm²
10A × 12m = 10 mm²     |  20A × 12m = 25 mm²     |  30A × 12m = 35 mm²
```

### 10.4 Kompass-Mindestabstände (Kurzform)

```
PERMANENTMAGNETE:
  Lautsprecher (Standard)........... 1,5 m
  Lautsprecher (Subwoofer).......... 2,5 m
  Magnetverschlüsse................. 0,5 m
  Kühlschrank-Kompressor............ 1,5 m

FERROMAGNETISCHE MATERIALIEN:
  Motorblock........................ 2,0 m
  Ankerkette (Kasten)............... 2,0 m
  Eiserne Kielbolzen................ 1,0 m
  Gasflaschen (Stahl)............... 1,0 m

ELEKTROMAGNETISCHE QUELLEN:
  Wechselrichter.................... 1,5 m
  Lichtmaschine..................... 2,0 m
  Bugstrahlruder-Kabel.............. 1,0 m
  SSB-Funk-Antenne.................. 2,0 m
  VHF-Funk-Antenne.................. 1,0 m
  LED-Dimmer........................ 0,5 m
  Eigene AP-Antriebskabel........... 1,0 m
```

### 10.5 Hydraulikflüssigkeits-Kompatibilität

```
NIEMALS MISCHEN! Verschiedene Typen sind NICHT kompatibel.

Teleflex/SeaStar...... Mineral HLP 15/22 (klar/gelb)
Vetus................. Mineral HLP 15 (klar)
Whitlock/Jefa......... Mineral HLP 15 (klar)
Lecomble & Schmitt.... Synthetisch (Hersteller-spezifisch)
Hynautic (manche)..... ATF (rot)

Bei Unsicherheit: Hersteller kontaktieren oder komplett spülen!
```

### 10.6 Sicherungsgrößen-Schnellreferenz

```
Tiller-Pilot (bis 10A)...... 15A träge (Blade)
Linear Typ 1 (bis 15A)...... 20A träge (Blade/ANL)
Linear Typ 2 (bis 25A)...... 35A träge (ANL)
Linear Typ 3 (bis 35A)...... 50A träge (ANL)
Hydraulik Typ 1 (bis 20A)... 30A träge (ANL)
Hydraulik Typ 2 (bis 40A)... 60A träge (ANL)
Hydraulik Typ 3 (bis 60A)... 80A träge (ANL)
Controller................... 10–15A flink (Blade)
NMEA-2000-Bus................ 3–5A flink (Blade)

IMMER: Sicherung max. 200mm von der Batterie!
IMMER: Träge (slow-blow) für Antriebsmotoren!
```

### 10.7 NMEA-2000-Bus Schnelltest

```
1. Bus stromlos schalten
2. Multimeter auf Ω (Widerstand)
3. An Backbone-Ende messen: CAN-H zu CAN-L
   → 60 Ω = OK (beide Terminatoren)
   → 120 Ω = Ein Terminator fehlt
   → ∞ = Kein Terminator
   → <60 Ω = Kurzschluss oder zu viele Terminatoren
4. Bus einschalten
5. Spannung CAN-H/CAN-L gegen Masse messen
   → 9–16V = OK
   → <9V = Stromversorgung prüfen
```

---

## ANHANG A–H — Fallstudien

### ANHANG A — Fallstudie: Bavaria 40 Cruiser — Linearantrieb Erstinstallation

**Boot:** Bavaria 40 Cruiser, Baujahr 2019, mechanische Steueranlage (Seilzug über Quadrant)
**System:** Raymarine EV-200 Linear (T70154)
**Aufwand:** 18 Stunden (2 Tage)

**Ausgangssituation:**
- Boot wurde ohne Autopilot ausgeliefert (Werftoption nicht gewählt)
- Steueranlage: Jefa-Lenkung mit 250mm-Quadrant
- Elektrisches System: 12V, 2×105Ah AGM, 80A-Lichtmaschine
- Kein NMEA-2000-Netzwerk vorhanden (nur Raymarine-Plotter mit eigenem GPS)

**Installation:**

*Tag 1 (10 Stunden):*
1. Bestandsaufnahme: Quadrant-Zugang über Achterkajüte (Backskiste), ausreichend Platz für Type-1-Linearantrieb
2. Magnetische Vermessung: Optimaler Kompass-Standort = unter Cockpit-Bank, 1,2m vom Motorblock, 0,8m von Lautsprechern
3. NMEA-2000-Backbone verlegt: Heck (Autopilot-Bereich) bis Plotter-Position (6m Backbone)
4. SeaTalk-NG-Adapter für Raymarine-Plotter montiert
5. Type-1-Linearantrieb montiert: Sperrholz-Verstärkung (18mm Birke) auf GFK-Innenhaut, Edelstahl-Montagewinkel
6. Gabelkopf an Quadrant bei 170mm Radius befestigt
7. EV-1 Sensor Core unter Cockpit-Bank montiert (Kabelbinder auf GFK-Schott, Kork-Unterlage als Vibrationsdämpfung)
8. Rudersensor montiert (Hebel direkt auf Ruderschaft-Verlängerung)

*Tag 2 (8 Stunden):*
9. Stromversorgung: 10mm² Marinekabel von Batterie (8m einfach), ANL-Sicherung 25A (träge) an Batterie
10. NMEA-2000 fertigverdrahtet, Terminatoren gesetzt, Stromversorgung 3A-Sicherung
11. System-Inbetriebnahme: alle Geräte erkannt
12. Rudersensor kalibriert (Mittelstellung, Endanschläge ±35°)
13. Compass-Swing im Hafen (unter Motor, langsame 360°-Drehung)
14. Restdeviation: max. ±2,5° → akzeptabel
15. Antriebsrichtung geprüft → korrekt (kein Reverse nötig)
16. Seatrial: 1 Stunde unter Motor (ruhige See), PID-Optimierung
17. Seatrial: 1,5 Stunden unter Segel (10–15 kn Wind), Segel-Modus optimiert
18. Dokumentation: Schaltplan, Kalibrierungswerte, Eigner-Einweisung

**Ergebnis:**
- Kursgenauigkeit unter Motor: ±1° (ruhige See), ±3° (Seegang BF 4)
- Kursgenauigkeit unter Segel: ±3° (Wind-Modus, 10–15 kn)
- Stromverbrauch: Ø 2,5A unter Motor, Ø 4A unter Segel
- Eigner-Zufriedenheit: Sehr hoch

**Lessons Learned:**
- Bavaria-Quadrant hat asymmetrische Anschläge (33° BB, 37° StB) → Software-Limit auf 30° gesetzt
- Lautsprecher in der Achterkajüte mussten 30cm weiter nach vorne versetzt werden (ursprünglich nur 50cm vom EV-1)
- 10mm² Kabel war ausreichend für Type 1 (12A Peak), aber bei Type 2 wäre 16mm² nötig gewesen

**Kostenübersicht:**

| Position | Kosten |
|----------|--------|
| Raymarine EV-200 Kit (T70154) | 3.200 € |
| NMEA-2000-Starter-Kit | 280 € |
| SeaTalk-NG-Adapter | 45 € |
| Kabel, Sicherungen, Kleinteile | 180 € |
| Sperrholz, Montagewinkel, Bolzen | 65 € |
| Arbeitszeit Werft (18h × 85 €) | 1.530 € |
| **Gesamt** | **5.300 €** |

### ANHANG B — Fallstudie: Hallberg-Rassy 43 — Hydraulik-Retrofit

**Boot:** Hallberg-Rassy 43 Mk II, Baujahr 2008, hydraulische Steueranlage (Whitlock/Jefa Hydraulik)
**Altsystem:** Raymarine ST6002+ mit SPX-10 Hydraulikpumpe (SeaTalk1)
**Neusystem:** B&G NAC-3 mit HPR2012 Hydraulikpumpe
**Aufwand:** 24 Stunden (3 Tage)

**Ausgangssituation:**
- Bestehende Raymarine SPX-10 Hydraulikpumpe versagt zunehmend (Getriebegeräusche)
- SeaTalk1-System veraltet, kein Support mehr
- Eigner möchte auf NMEA 2000 umstellen (neuer B&G Zeus³-Plotter bereits installiert)
- Bestehendes Hydrauliksystem (Whitlock) in gutem Zustand
- 24V-Bordnetz

**Installation:**

*Tag 1 (8 Stunden):*
1. Altsystem dokumentiert und deinstalliert (SeaTalk1-Kabel markiert, nicht entfernt)
2. NMEA-2000-Backbone verlegt (12m, Bug bis Heck), T-Stücke an 8 Positionen
3. B&G Precision-9 Compass unter Cockpit-Boden montiert (Position: 1,8m vom Motor, 1,5m von Lautsprechern)
4. RF25N Rudersensor montiert (NMEA 2000, berührungslos, am Ruderschaft)

*Tag 2 (10 Stunden):*
5. Alte SPX-10-Pumpe deinstalliert (Hydrauliksystem abgesperrt, Öl aufgefangen)
6. Neue HPR2012-Pumpe montiert (gleiche Befestigungspunkte, JIC-Anschlüsse kompatibel)
7. Hydraulikleitungen umgeschlossen: neue Pumpe parallel zur Helm-Pumpe
8. Solenoid-Bypass-Ventil installiert (automatische Umschaltung)
9. Hydrauliksystem befüllt und entlüftet (5 Zyklen, 1,5 Stunden)
10. NAC-3-Controller installiert (wasserdichtes Gehäuse im Maschinenraum)
11. Stromversorgung: 6mm² von 24V-Batterie (5m einfach), ANL-Sicherung 30A

*Tag 3 (6 Stunden):*
12. Verkabelung abgeschlossen, System-Inbetriebnahme
13. Rudersensor kalibriert
14. Compass-Swing (unter Motor, Hafenbecken)
15. Restdeviation: max. ±1,5° → sehr gut (HR43 hat wenig Stahl im Heckbereich)
16. Seatrial unter Motor (2 Stunden): PID-Optimierung
17. Seatrial unter Segel (2 Stunden): Wind-Modus, verschiedene Kurse
18. Dokumentation und Eigner-Einweisung
19. Zeus³-Plotter-Integration: AP-Steuerung direkt vom Plotter

**Ergebnis:**
- Dramatische Verbesserung gegenüber Altsystem (ST6002+)
- Kursgenauigkeit unter Motor: ±0,5° (ruhige See)
- Wind-Modus segelt VMG-optimiert
- 24V-System: nur 3A Durchschnitt (vs. 6A beim alten 12V-System)
- Hydraulik spürbar schneller (HPR2012 höhere Verdrängung)

**Kostenübersicht:**

| Position | Kosten |
|----------|--------|
| B&G NAC-3 Pilot Pack (000-15045-001) | 5.800 € |
| HPR2012 Hydraulikpumpe (000-15957-001) | 1.850 € |
| Solenoid-Bypass-Ventil | 320 € |
| NMEA-2000-Backbone + Zubehör | 350 € |
| Hydraulikflüssigkeit + Entlüftungsmaterial | 85 € |
| Kabel, Sicherungen, Kleinteile | 120 € |
| Arbeitszeit Werft (24h × 95 €) | 2.280 € |
| **Gesamt** | **10.805 €** |

### ANHANG C — Fallstudie: Jeanneau Sun Odyssey 349 — Tiller-Pilot

**Boot:** Jeanneau Sun Odyssey 349, Baujahr 2021, Pinnensteuerung
**System:** Raymarine EV-100 Tiller (T70161)
**Aufwand:** 6 Stunden

**Ausgangssituation:**
- Pinnensteuerung (Standard bei SO 349)
- Eigner fährt einhand, braucht Autopiloten für Segelmanöver und Pausen
- Budget-orientiert, einfache Installation bevorzugt
- 12V-System, 1×100Ah Lithium

**Installation (1 Tag, 6 Stunden):**
1. EV-1 Sensor Core unter Cockpit-Sitzbank montiert (GFK-Schott, Kabelbinder + Kork)
2. Montagepunkt Cockpit-Boden: Edelstahl-Augplatte, 4× M8 durch GFK mit Sperrholz-Verstärkung
3. Tiller-Antrieb zwischen Augplatte und Pinne (500mm vom Ruderschaft)
4. Stromversorgung: 6mm² direkt von Lithium-Batterie (4m), 15A-Sicherung (träge)
5. SeaTalk-NG-Kabel zum Plotter (Axiom 7, bereits vorhanden)
6. Compass-Swing (unter Motor im Hafen)
7. Rudersensor-Kalibrierung (interner Kolbensensor des Tiller-Piloten)
8. Seatrial: 1,5 Stunden unter Segel

**Ergebnis:**
- Kursgenauigkeit: ±4° unter Segel (akzeptabel für 34-Fuß-Pinnenboot)
- Stromverbrauch: Ø 1,5A (Lithium hält >50 Stunden)
- Einhand-Segeln problemlos möglich
- Gesamtkosten: 1.650 € (inkl. Einbau-Eigenmontage, nur Material)

### ANHANG D — Fallstudie: Beneteau Oceanis 51.1 — NMEA-2000-Busfehler-Diagnose

**Boot:** Beneteau Oceanis 51.1, Baujahr 2020, B&G NAC-2 Autopilot
**Problem:** Autopilot verliert sporadisch den Kompass (No Heading Alarm), 2–3× pro Stunde

**Diagnose-Verlauf:**
1. Kompass (Precision-9) überprüft: Sensor funktioniert einwandfrei (Standalone-Test)
2. Drop-Kabel Kompass gemessen: 8,5 m lang (!) → Über Maximum von 6m
3. Bus-Widerstand: 55 Ω → Leicht unter 60 Ω (zusätzlicher Widerstand irgendwo)
4. Bus-Topologie aufgezeichnet: Stern-Abzweig am Navstation-Verteiler gefunden
5. Ein T-Stück mit Grünspan an den Kontakten entdeckt

**Lösung:**
1. Drop-Kabel Kompass gekürzt auf 4m (Kompass näher ans Backbone verlegt)
2. Stern-Abzweig eliminiert (Backbone-Route korrigiert)
3. Korrodiertes T-Stück ersetzt, alle Stecker mit Kontaktfett behandelt
4. Zusätzlicher „dritter Terminator" entfernt (vom Vorbesitzer falsch eingebaut)

**Ergebnis:** Keine Ausfälle mehr nach 2.000 Seemeilen.

**Kosten:** 180 € Material + 4 Stunden Werft = 540 € gesamt

### ANHANG E — Fallstudie: Hanse 548 — Kompass-Deviation durch Subwoofer

**Boot:** Hanse 548, Baujahr 2022, Garmin GHP Reactor Autopilot
**Problem:** Autopilot steuert auf Ostkurs systematisch 8° zu weit nach Norden

**Diagnose-Verlauf:**
1. Compass-Swing ergibt: 0° → +2°, 90° → +8°, 180° → +1°, 270° → -7°
2. Klassisches Halbkreis-Deviationsmuster (Koeffizient B dominant) → Permanentmagnet in Ost-West-Achse
3. Kompass-Position: unter Cockpit-Bank, Steuerbord
4. 60cm entfernt: Fusion-Subwoofer (Neodym-Magnet, 150W)
5. Subwoofer temporär entfernt → Deviation sinkt auf max. ±1,5°

**Lösung:**
Subwoofer 1,5m weiter nach vorne versetzt (unter Salon-Settee). Erneuter Compass-Swing: Restdeviation max. ±1°.

**Kosten:** 3 Stunden Werft = 285 €

**Detaillierte Deviationstabelle vor und nach Umbau:**

| Kurs (mag.) | Deviation VOR Umbau | Deviation NACH Umbau |
|-------------|--------------------|--------------------|
| 000° (N) | +2° | +1° |
| 030° | +4° | +1° |
| 060° | +6° | +0,5° |
| 090° (E) | +8° | +1° |
| 120° | +6° | +0,5° |
| 150° | +3° | 0° |
| 180° (S) | +1° | -0,5° |
| 210° | -2° | -0,5° |
| 240° | -5° | -1° |
| 270° (W) | -7° | -1° |
| 300° | -5° | -0,5° |
| 330° | -1° | 0° |

**Analyse:** Klassisches Halbkreismuster mit Maximum auf 90° und Minimum auf 270° — Permanentmagnet querschiffs Steuerbord (= Subwoofer). Nach Versetzung: maximale Restdeviation ±1° — ausgezeichnet.

### ANHANG F — Fallstudie: Catana 53 — Dual-Ruder-Installation

**Boot:** Catana 53 (Katamaran), Baujahr 2017, 2× Ruder (Backbord + Steuerbord)
**System:** Simrad AC70 + 2× HPR-2 Hydraulikpumpen
**Besonderheit:** Katamaran mit zwei unabhängigen Rudern erfordert synchronisierten Dual-Antrieb

**Installation:**
1. AC70 steuert beide Pumpen synchron über separaten Ausgang
2. Zwei Rudersensoren (RF45X), einer pro Ruder
3. HS75 GNSS-Kompass auf Dach (kein magnetisches Problem auf GFK-Katamaran)
4. Dual-Kalibrierung: beide Ruder unabhängig kalibriert, dann Synchronisation geprüft

**Ergebnis:**
- Exzellente Kursgenauigkeit (±0,5° unter Motor) dank GPS-Kompass
- Dual-Ruder ermöglicht agilere Steuerung bei weniger Energieverbrauch
- Gesamtkosten: 18.500 €

### ANHANG G — Fallstudie: Contest 42CS — Migration SeaTalk1 → NMEA 2000

**Boot:** Contest 42CS, Baujahr 2005, komplettes Raymarine SeaTalk1-System
**Altsystem:** Raymarine ST7002+ Controller, Type 2 Linear Drive, ST80 Kompass
**Neusystem:** Raymarine Evolution EV-300 Linear (T70160)

**Herausforderung:**
- 12 SeaTalk1-Geräte an Bord (Plotter, Wind, Log, Tiefe, AP, Instrumente)
- Schrittweise Migration gewünscht (nicht alles auf einmal)
- Bestehender Type-2-Linearantrieb mechanisch in Ordnung

**Lösung: Hybrides Netzwerk**
1. NMEA-2000-Backbone installiert (parallel zu SeaTalk1)
2. SeaTalk1-zu-SeaTalkNG-Konverter (E22158) für Legacy-Geräte
3. EV-2 Controller und EV-1 Sensor auf SeaTalk-NG/NMEA 2000
4. Bestehender Type-2-Antrieb weiterverwendet (Kabelstecker kompatibel!)
5. Neuer RF25N Rudersensor (NMEA 2000) ersetzt alten analogen Sensor
6. Alte SeaTalk1-Instrumente bleiben vorerst, empfangen Daten über Konverter

**Ergebnis:**
- Migration gelungen ohne kompletten Systemtausch
- SeaTalk1-Geräte werden schrittweise ersetzt (bei Defekt oder Wunsch)
- Antrieb-Weiterverwendung spart 1.200 €
- Gesamtkosten: 4.800 € (statt ca. 8.000 € bei Komplettaustausch)

### ANHANG H — Fallstudie: Oyster 575 — Professionelle Hydraulik-Installation mit GNSS-Kompass

**Boot:** Oyster 575, Baujahr 2023, Neuinstallation ab Werft
**System:** B&G NAC-3, HPR2012, HS75 GNSS-Kompass, H5000 Pilot Controller, Triton²-Displays
**Aufwand:** 32 Stunden (Werft, integriert in Neubau-Prozess)

**Besonderheit: GNSS-Kompass**
Der Simrad/B&G HS75 nutzt zwei GPS-Antennen zur Kursbestimmung — völlig unabhängig vom Erdmagnetfeld:

| Vorteil | Auswirkung |
|---------|-----------|
| Keine magnetische Deviation | Kein Compass-Swing nötig (!) |
| Keine Störung durch Bordmagnetismus | Kein Abstand zu Lautsprechern/Motor nötig |
| ±0,3° Genauigkeit | 3–10× genauer als Fluxgate/IMU |
| Liefert auch SOG und COG | Reduziert Sensoranzahl |

**Nachteile:**
- Benötigt freie GPS-Sicht → Decksmontage oder Radomontage
- Kein Heading bei GPS-Ausfall (Backup-IMU empfohlen)
- Höherer Preis (ca. 2.000–3.500 €)
- Antennen-Abstand min. 500mm für gute Genauigkeit

**Installation:**
1. HS75-Antennen auf Geräteträger am Heck montiert (1m Abstand, freie Sicht 360°)
2. NAC-3 im Maschinenraum (wasserdichtes Gehäuse)
3. HPR2012 parallel zur Whitlock-Hydraulikanlage
4. H5000 Pilot Controller am Steuerstand + Triton² im Niedergang
5. NMEA-2000-Backbone über ganzes Schiff (22m, 15 T-Stücke)
6. 24V-System: 10mm²-Kabel, 6m, ANL 40A

**Ergebnis:**
- Kursgenauigkeit: ±0,3° unter Motor, ±1° unter Segel
- Kein Compass-Swing nötig
- Kein magnetisches Problem trotz Stahlkiel
- H5000 liefert Performance-Daten (Polar, VMG, Laylines) direkt an AP
- Gesamtkosten: 16.200 € (exkl. Arbeitszeit Werft, in Neubau integriert)

---

## ANHANG I–R — Pydantic v2 Modelle

### ANHANG I — Grundlegende Enumerationen

```python
"""
AYDI Autopilot Installation & Calibration Models — Pydantic v2
Wissensdatei 21.04 — Autopilot Installation und Kalibrierung

All models use model_config = {"from_attributes": True} (Pydantic v2).
NEVER use class Config (Pydantic v1 pattern).
German domain terms in docstrings, English code.
"""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Enumerations
# ---------------------------------------------------------------------------

class AutopilotDriveType(str, Enum):
    """Type of autopilot drive unit."""
    HYDRAULIC = "hydraulic"
    LINEAR = "linear"
    WHEEL = "wheel"
    TILLER = "tiller"


class AutopilotManufacturer(str, Enum):
    """Supported autopilot manufacturers."""
    RAYMARINE = "raymarine"
    BG = "bg"          # B&G (Brookes & Gatehouse)
    GARMIN = "garmin"
    SIMRAD = "simrad"
    FURUNO = "furuno"
    LECOMBLE_SCHMITT = "lecomble_schmitt"
    NKE = "nke"
    OTHER = "other"


class CompassType(str, Enum):
    """Heading sensor technology."""
    FLUXGATE = "fluxgate"
    SOLID_STATE_IMU = "solid_state_imu"
    GNSS_COMPASS = "gnss_compass"
    RATE_COMPASS = "rate_compass"


class RudderSensorType(str, Enum):
    """Rudder position sensor technology."""
    POTENTIOMETER = "potentiometer"
    INDUCTIVE_RVDT = "inductive_rvdt"
    MAGNETIC_HALL = "magnetic_hall"
    MECHANICAL_LEVER = "mechanical_lever"


class NetworkProtocol(str, Enum):
    """Marine data network protocol."""
    NMEA_2000 = "nmea_2000"
    SEATALK_NG = "seatalk_ng"
    SEATALK_1 = "seatalk_1"
    NMEA_0183 = "nmea_0183"
    SIMNET = "simnet"
    NKE_BUS = "nke_bus"
    CAN_PROPRIETARY = "can_proprietary"


class InstallationType(str, Enum):
    """Installation scenario."""
    NEW_BUILD = "new_build"
    RETROFIT = "retrofit"
    UPGRADE = "upgrade"
    REPLACEMENT = "replacement"


class HydraulicFluidType(str, Enum):
    """Type of hydraulic fluid."""
    MINERAL_HLP15 = "mineral_hlp15"
    MINERAL_HLP22 = "mineral_hlp22"
    ATF = "atf"
    SYNTHETIC = "synthetic"


class ConfidenceLevel(str, Enum):
    """AYDI confidence classification."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class SeverityLevel(str, Enum):
    """Fault severity classification."""
    CRITICAL = "critical"      # Safety risk, immediate action
    HIGH = "high"              # System non-functional
    MEDIUM = "medium"          # Degraded performance
    LOW = "low"                # Cosmetic or minor
    INFO = "info"              # Informational only
```

### ANHANG J — Installations-Spezifikation und Verkabelung

```python
class VoltageDropCalculation(BaseModel):
    """Berechnung des Spannungsabfalls in der Autopilot-Versorgungsleitung."""

    model_config = {"from_attributes": True}

    cable_length_m: float = Field(
        ..., ge=0.5, le=50,
        description="Einfache Kabellänge in Metern (Batterie → Antrieb)"
    )
    current_peak_a: float = Field(
        ..., ge=1, le=150,
        description="Spitzenstrom des Antriebs in Ampere"
    )
    cable_cross_section_mm2: float = Field(
        ..., ge=1.5, le=120,
        description="Leiterquerschnitt in mm²"
    )
    system_voltage_v: float = Field(
        ..., ge=10, le=48,
        description="Nennspannung des Bordsystems in V DC"
    )
    copper_resistivity: float = Field(
        default=0.0178,
        description="Spezifischer Widerstand Kupfer bei 20°C in Ω·mm²/m"
    )
    voltage_drop_v: Optional[float] = Field(
        None,
        description="Berechneter Spannungsabfall in Volt (Ergebnis)"
    )
    voltage_drop_percent: Optional[float] = Field(
        None,
        description="Berechneter Spannungsabfall in Prozent (Ergebnis)"
    )
    is_acceptable: Optional[bool] = Field(
        None,
        description="True wenn Spannungsabfall ≤ 3 %"
    )
    recommended_cross_section_mm2: Optional[float] = Field(
        None,
        description="Empfohlener Mindest-Leiterquerschnitt in mm²"
    )
    confidence: ConfidenceLevel = ConfidenceLevel.CALCULATED


class CableSpecification(BaseModel):
    """Spezifikation eines Installationskabels."""

    model_config = {"from_attributes": True}

    purpose: str = Field(
        ..., min_length=1, max_length=200,
        description="Zweck des Kabels (z.B. 'Antrieb Stromversorgung Plus')"
    )
    cross_section_mm2: float = Field(..., ge=0.5, le=120)
    length_m: float = Field(..., ge=0.1, le=100)
    conductor_type: str = Field(
        default="tinned_copper_stranded",
        description="Leitertyp (verzinntes Kupfer, feindrähtig)"
    )
    insulation_rating_c: int = Field(
        default=90, ge=60, le=200,
        description="Isolierung Temperaturbeständigkeit in °C"
    )
    color: Optional[str] = Field(
        None, max_length=30,
        description="Kabelfarbe nach ABYC-Standard"
    )
    fuse_rating_a: Optional[float] = Field(
        None, ge=0.5, le=200,
        description="Zugehörige Sicherung in Ampere"
    )
    fuse_type: Optional[str] = Field(
        None, max_length=50,
        description="Sicherungstyp (z.B. 'ANL träge', 'Blade flink')"
    )


class NMEA2000BusSpecification(BaseModel):
    """Spezifikation des NMEA-2000-Netzwerks."""

    model_config = {"from_attributes": True}

    backbone_length_m: float = Field(
        ..., ge=0.5, le=200,
        description="Gesamtlänge des Backbone-Kabels in Metern"
    )
    num_t_connectors: int = Field(
        ..., ge=2, le=50,
        description="Anzahl T-Stücke im Netzwerk"
    )
    num_devices: int = Field(
        ..., ge=1, le=50,
        description="Anzahl angeschlossener Geräte"
    )
    total_len: float = Field(
        ..., ge=0, le=60,
        description="Gesamte LEN-Last im Netzwerk"
    )
    max_drop_cable_length_m: float = Field(
        ..., ge=0, le=6,
        description="Längtes Drop-Kabel im Netzwerk in Metern"
    )
    terminators_count: int = Field(
        default=2, ge=0, le=4,
        description="Anzahl Terminatoren (soll = 2)"
    )
    measured_resistance_ohm: Optional[float] = Field(
        None, ge=0, le=1000,
        description="Gemessener Bus-Widerstand in Ohm (Soll: 60)"
    )
    bus_voltage_v: Optional[float] = Field(
        None, ge=0, le=20,
        description="Gemessene Bus-Spannung in V DC (Soll: 9–16)"
    )
    topology_is_linear: bool = Field(
        default=True,
        description="True wenn Backbone linear (kein Stern)"
    )
    shield_grounded_once: bool = Field(
        default=True,
        description="True wenn Schirm nur an einem Punkt geerdet"
    )
    is_compliant: Optional[bool] = Field(
        None,
        description="True wenn alle NMEA-2000-Anforderungen erfüllt"
    )
    issues: list[str] = Field(
        default_factory=list,
        description="Liste gefundener Probleme"
    )
    confidence: ConfidenceLevel = ConfidenceLevel.MEASURED
```

### ANHANG K — Kompass und Deviation

```python
class MagneticDisturbanceSource(BaseModel):
    """Dokumentation einer magnetischen Störquelle in Kompass-Nähe."""

    model_config = {"from_attributes": True}

    source_name: str = Field(
        ..., min_length=1, max_length=200,
        description="Bezeichnung der Störquelle (z.B. 'Fusion Subwoofer Steuerbord')"
    )
    source_category: str = Field(
        ...,
        description="Kategorie: permanent_magnet, ferromagnetic, electromagnetic"
    )
    distance_to_compass_m: float = Field(
        ..., ge=0, le=20,
        description="Gemessener Abstand zum Heading-Sensor in Metern"
    )
    required_distance_m: float = Field(
        ..., ge=0, le=10,
        description="Erforderlicher Mindestabstand in Metern"
    )
    estimated_deviation_deg: Optional[float] = Field(
        None, ge=0, le=180,
        description="Geschätzte maximale Deviation durch diese Quelle in Grad"
    )
    is_variable: bool = Field(
        default=False,
        description="True wenn Störung variabel (z.B. Wechselrichter nur bei Last)"
    )
    is_removable: bool = Field(
        default=False,
        description="True wenn Quelle versetzbar/entfernbar"
    )
    is_compliant: Optional[bool] = Field(
        None,
        description="True wenn Abstand ≥ Mindestabstand"
    )
    confidence: ConfidenceLevel = ConfidenceLevel.MEASURED


class DeviationMeasurement(BaseModel):
    """Einzelne Deviationsmessung bei einem bestimmten Kurs."""

    model_config = {"from_attributes": True}

    magnetic_course_deg: float = Field(
        ..., ge=0, lt=360,
        description="Magnetischer Referenzkurs in Grad"
    )
    compass_reading_deg: float = Field(
        ..., ge=0, lt=360,
        description="Kompass-Anzeige bei diesem Kurs in Grad"
    )
    deviation_deg: Optional[float] = Field(
        None, ge=-180, le=180,
        description="Berechnete Deviation (+ = Ost, - = West)"
    )
    confidence: ConfidenceLevel = ConfidenceLevel.MEASURED


class CompassSwingResult(BaseModel):
    """Ergebnis eines kompletten Compass-Swing (Deviationsermittlung)."""

    model_config = {"from_attributes": True}

    measurements: list[DeviationMeasurement] = Field(
        ..., min_length=4, max_length=72,
        description="Einzelmessungen (min 4: N/E/S/W, ideal 12 oder 36)"
    )
    coefficient_a_deg: Optional[float] = Field(
        None, description="Konstanter Fehler (Fehlausrichtung) in Grad"
    )
    coefficient_b_deg: Optional[float] = Field(
        None, description="Halbkreis-Deviation (Sinus) in Grad"
    )
    coefficient_c_deg: Optional[float] = Field(
        None, description="Halbkreis-Deviation (Cosinus) in Grad"
    )
    coefficient_d_deg: Optional[float] = Field(
        None, description="Viertelkreis-Deviation (Sinus) in Grad"
    )
    coefficient_e_deg: Optional[float] = Field(
        None, description="Viertelkreis-Deviation (Cosinus) in Grad"
    )
    max_deviation_deg: Optional[float] = Field(
        None, ge=0, le=180,
        description="Maximale Deviation über alle Kurse in Grad"
    )
    max_residual_deviation_deg: Optional[float] = Field(
        None, ge=0, le=180,
        description="Maximale Restdeviation nach Kompensation in Grad"
    )
    is_acceptable: Optional[bool] = Field(
        None,
        description="True wenn Restdeviation ≤ ±3° (Fluxgate) oder ≤ ±2° (IMU)"
    )
    motor_running: bool = Field(
        default=False,
        description="True wenn Motor bei Messung lief"
    )
    electronics_on: bool = Field(
        default=True,
        description="True wenn Bordelektrik bei Messung eingeschaltet"
    )
    wind_speed_kn: Optional[float] = Field(
        None, ge=0, le=60,
        description="Windstärke während Compass-Swing in Knoten"
    )
    disturbance_sources: list[MagneticDisturbanceSource] = Field(
        default_factory=list,
        description="Dokumentierte Störquellen in der Nähe"
    )
    confidence: ConfidenceLevel = ConfidenceLevel.MEASURED
```

### ANHANG L — Rudersensor-Kalibrierung

```python
class RudderSensorCalibration(BaseModel):
    """Kalibrierungsdaten des Rudersensors."""

    model_config = {"from_attributes": True}

    sensor_type: RudderSensorType
    sensor_manufacturer: str = Field(..., min_length=1, max_length=120)
    sensor_model: str = Field(..., min_length=1, max_length=120)

    center_position_raw: Optional[float] = Field(
        None,
        description="Rohwert des Sensors bei Rudermittellage"
    )
    port_limit_raw: Optional[float] = Field(
        None,
        description="Rohwert des Sensors bei vollem Backbord-Ruder"
    )
    starboard_limit_raw: Optional[float] = Field(
        None,
        description="Rohwert des Sensors bei vollem Steuerbord-Ruder"
    )
    port_limit_deg: float = Field(
        ..., ge=-60, le=0,
        description="Maximaler Ruderausschlag Backbord in Grad (negativ)"
    )
    starboard_limit_deg: float = Field(
        ..., ge=0, le=60,
        description="Maximaler Ruderausschlag Steuerbord in Grad (positiv)"
    )
    software_limit_port_deg: Optional[float] = Field(
        None, ge=-55, le=0,
        description="Software-Endanschlag Backbord (5° vor mech. Anschlag)"
    )
    software_limit_starboard_deg: Optional[float] = Field(
        None, ge=0, le=55,
        description="Software-Endanschlag Steuerbord (5° vor mech. Anschlag)"
    )
    center_offset_deg: Optional[float] = Field(
        None, ge=-10, le=10,
        description="Offset der Mittellage in Grad (soll: 0)"
    )
    linearity_error_max_deg: Optional[float] = Field(
        None, ge=0, le=15,
        description="Maximale Linearitätsabweichung in Grad"
    )
    mechanical_play_deg: Optional[float] = Field(
        None, ge=0, le=10,
        description="Mechanisches Spiel in der Sensoranlenkung in Grad"
    )
    deadband_deg: float = Field(
        default=2.0, ge=0.5, le=10,
        description="Totband-Einstellung in Grad"
    )
    is_acceptable: Optional[bool] = Field(
        None,
        description="True wenn Offset <2°, Linearität <2°, Spiel <1°"
    )
    issues: list[str] = Field(
        default_factory=list,
        description="Gefundene Probleme bei der Kalibrierung"
    )
    confidence: ConfidenceLevel = ConfidenceLevel.MEASURED
```

### ANHANG M — Installations-Assessment

```python
class InstallationComponent(BaseModel):
    """Bewertung einer einzelnen Installationskomponente."""

    model_config = {"from_attributes": True}

    component_name: str = Field(
        ..., min_length=1, max_length=200,
        description="Name der Komponente (z.B. 'Linearantrieb Type 2')"
    )
    manufacturer: AutopilotManufacturer
    model_name: str = Field(..., min_length=1, max_length=200)
    part_number: Optional[str] = Field(None, max_length=50)
    installation_location: str = Field(
        ..., min_length=1, max_length=300,
        description="Einbauort auf dem Boot"
    )
    is_correctly_installed: Optional[bool] = None
    issues: list[str] = Field(default_factory=list)
    recommendations: list[str] = Field(default_factory=list)
    score: Optional[float] = Field(
        None, ge=0, le=100,
        description="Bewertungsscore 0–100"
    )
    confidence: ConfidenceLevel = ConfidenceLevel.VISUAL_MEDIUM


class AutopilotInstallationAssessment(BaseModel):
    """Gesamtbewertung einer Autopilot-Installation durch AYDI."""

    model_config = {"from_attributes": True}

    boat_name: Optional[str] = Field(None, max_length=200)
    boat_type: str = Field(..., min_length=1, max_length=200)
    boat_length_m: float = Field(..., ge=5, le=80)
    boat_displacement_kg: Optional[float] = Field(None, ge=500, le=500000)
    steering_type: str = Field(
        ..., description="Steuerungstyp: hydraulic, cable, rod, tiller"
    )

    installation_type: InstallationType
    drive_type: AutopilotDriveType
    system_manufacturer: AutopilotManufacturer
    system_voltage_v: float = Field(..., ge=10, le=48)

    # Sub-assessments
    components: list[InstallationComponent] = Field(default_factory=list)
    voltage_drop: Optional[VoltageDropCalculation] = None
    nmea_bus: Optional[NMEA2000BusSpecification] = None
    compass_swing: Optional[CompassSwingResult] = None
    rudder_calibration: Optional[RudderSensorCalibration] = None
    disturbance_sources: list[MagneticDisturbanceSource] = Field(
        default_factory=list
    )

    # Overall scores
    mechanical_score: Optional[float] = Field(
        None, ge=0, le=100,
        description="Bewertung mechanische Installation (0–100)"
    )
    electrical_score: Optional[float] = Field(
        None, ge=0, le=100,
        description="Bewertung elektrische Installation (0–100)"
    )
    network_score: Optional[float] = Field(
        None, ge=0, le=100,
        description="Bewertung NMEA-2000-Netzwerk (0–100)"
    )
    compass_score: Optional[float] = Field(
        None, ge=0, le=100,
        description="Bewertung Kompass-Installation und Kalibrierung (0–100)"
    )
    calibration_score: Optional[float] = Field(
        None, ge=0, le=100,
        description="Bewertung Gesamtkalibrierung (0–100)"
    )
    overall_score: Optional[float] = Field(
        None, ge=0, le=100,
        description="Gesamtbewertung der Installation (0–100)"
    )

    findings: list[str] = Field(
        default_factory=list,
        description="Zusammenfassung der Befunde"
    )
    critical_issues: list[str] = Field(
        default_factory=list,
        description="Kritische Probleme, die sofort behoben werden müssen"
    )
    recommendations: list[str] = Field(
        default_factory=list,
        description="Verbesserungsvorschläge"
    )

    confidence: ConfidenceLevel = ConfidenceLevel.VISUAL_MEDIUM
```

### ANHANG N — Fehlerbild-Modelle

```python
class InstallationFaultCause(BaseModel):
    """Einzelne Ursache eines Installations-Fehlerbilds."""

    model_config = {"from_attributes": True}

    cause: str = Field(..., min_length=1, max_length=500)
    probability: float = Field(
        ..., ge=0, le=1,
        description="Wahrscheinlichkeit (0–1) dass dies die Ursache ist"
    )
    diagnostic_steps: list[str] = Field(
        default_factory=list,
        description="Diagnoseschritte zur Bestätigung dieser Ursache"
    )
    remediation: str = Field(
        ..., min_length=1, max_length=1000,
        description="Behebungsmaßnahme"
    )


class InstallationFaultPattern(BaseModel):
    """Fehlerbild bei der Autopilot-Installation."""

    model_config = {"from_attributes": True}

    fault_id: str = Field(
        ..., pattern=r"^F-INS-\d{2}$",
        description="Fehlerbild-ID (z.B. F-INS-01)"
    )
    title: str = Field(..., min_length=1, max_length=200)
    category: str = Field(
        ...,
        description="Kategorie: compass, electrical, mechanical, network, hydraulic, calibration"
    )
    severity: SeverityLevel
    frequency: str = Field(
        ...,
        description="Häufigkeit: sehr_haeufig, haeufig, mittel, selten"
    )
    symptoms: list[str] = Field(
        ..., min_length=1,
        description="Beobachtbare Symptome"
    )
    causes: list[InstallationFaultCause] = Field(
        ..., min_length=1,
        description="Mögliche Ursachen mit Wahrscheinlichkeit"
    )
    prevention: list[str] = Field(
        default_factory=list,
        description="Präventionsmaßnahmen"
    )
    visual_indicators: list[str] = Field(
        default_factory=list,
        description="Visuelle Indikatoren für Foto-Analyse"
    )
    confidence: ConfidenceLevel = ConfidenceLevel.DOCUMENTED
```

### ANHANG O — Troubleshooting-Entscheidungsbaum

```python
class DecisionTreeNode(BaseModel):
    """Knoten im Troubleshooting-Entscheidungsbaum."""

    model_config = {"from_attributes": True}

    node_id: str = Field(
        ..., min_length=1, max_length=30,
        description="Eindeutige Knoten-ID (z.B. 'N1', 'N2a', 'N3b_yes')"
    )
    question: Optional[str] = Field(
        None, max_length=500,
        description="Frage an den Techniker (None bei Endknoten)"
    )
    action: Optional[str] = Field(
        None, max_length=1000,
        description="Empfohlene Aktion (bei Endknoten oder Zwischenschritt)"
    )
    measurement: Optional[str] = Field(
        None, max_length=500,
        description="Auszuführende Messung (z.B. 'Spannung am Antrieb messen')"
    )
    expected_value: Optional[str] = Field(
        None, max_length=200,
        description="Erwarteter Messwert (z.B. '60 Ω')"
    )
    yes_node_id: Optional[str] = Field(
        None, max_length=30,
        description="Nächster Knoten bei 'Ja'"
    )
    no_node_id: Optional[str] = Field(
        None, max_length=30,
        description="Nächster Knoten bei 'Nein'"
    )
    is_terminal: bool = Field(
        default=False,
        description="True wenn dies ein Endknoten ist"
    )


class TroubleshootingTree(BaseModel):
    """Kompletter Troubleshooting-Entscheidungsbaum."""

    model_config = {"from_attributes": True}

    tree_id: str = Field(
        ..., min_length=1, max_length=50,
        description="Eindeutige Baum-ID (z.B. 'TS-INS-01')"
    )
    title: str = Field(..., min_length=1, max_length=200)
    description: str = Field(..., min_length=1, max_length=1000)
    entry_symptom: str = Field(
        ..., min_length=1, max_length=500,
        description="Eingangssymptom, das den Baum auslöst"
    )
    nodes: list[DecisionTreeNode] = Field(
        ..., min_length=2,
        description="Alle Knoten des Entscheidungsbaums"
    )
    root_node_id: str = Field(
        ..., min_length=1, max_length=30,
        description="ID des Startknotens"
    )
    estimated_diagnosis_time_min: Optional[int] = Field(
        None, ge=5, le=480,
        description="Geschätzte Diagnosezeit in Minuten"
    )
    tools_required: list[str] = Field(
        default_factory=list,
        description="Benötigte Werkzeuge/Messgeräte"
    )
    confidence: ConfidenceLevel = ConfidenceLevel.DOCUMENTED
```

### ANHANG P — Produktkatalog-Modelle

```python
class AutopilotKitComponent(BaseModel):
    """Einzelkomponente eines Autopilot-Einbaukits."""

    model_config = {"from_attributes": True}

    component_type: str = Field(
        ...,
        description="Typ: controller, drive, compass, rudder_sensor, display, cable, adapter, terminator"
    )
    manufacturer: AutopilotManufacturer
    model_name: str = Field(..., min_length=1, max_length=200)
    part_number: str = Field(..., min_length=1, max_length=50)
    description_de: str = Field(
        ..., min_length=1, max_length=500,
        description="Deutsche Beschreibung"
    )
    price_eur: Optional[float] = Field(None, ge=0, le=50000)
    weight_kg: Optional[float] = Field(None, ge=0, le=50)
    voltage_v: Optional[float] = Field(None, ge=10, le=48)
    max_current_a: Optional[float] = Field(None, ge=0, le=150)
    network_protocol: Optional[NetworkProtocol] = None
    len_value: Optional[float] = Field(
        None, ge=0, le=20,
        description="NMEA 2000 LEN (Load Equivalence Number)"
    )
    confidence: ConfidenceLevel = ConfidenceLevel.DOCUMENTED


class AutopilotKit(BaseModel):
    """Komplettes Autopilot-Einbaukit eines Herstellers."""

    model_config = {"from_attributes": True}

    kit_name: str = Field(..., min_length=1, max_length=200)
    manufacturer: AutopilotManufacturer
    part_number: str = Field(..., min_length=1, max_length=50)
    drive_type: AutopilotDriveType
    target_boat_type: str = Field(
        ...,
        description="Zielgruppe: sail, motor, catamaran, trawler"
    )
    min_boat_length_m: Optional[float] = Field(None, ge=5, le=80)
    max_boat_length_m: Optional[float] = Field(None, ge=5, le=80)
    max_displacement_kg: Optional[float] = Field(None, ge=500, le=500000)
    system_voltage_v: float = Field(..., ge=10, le=48)
    components: list[AutopilotKitComponent] = Field(
        ..., min_length=1,
        description="Enthaltene Komponenten"
    )
    kit_price_eur: Optional[float] = Field(None, ge=0, le=50000)
    additional_required: list[str] = Field(
        default_factory=list,
        description="Zusätzlich benötigte Komponenten (nicht im Kit)"
    )
    installation_time_hours: Optional[float] = Field(
        None, ge=1, le=80,
        description="Geschätzte Installationszeit in Stunden"
    )
    confidence: ConfidenceLevel = ConfidenceLevel.DOCUMENTED
```

### ANHANG Q — Hydraulik-Spezifikation

```python
class HydraulicSystemSpec(BaseModel):
    """Spezifikation des hydraulischen Autopilot-Systems."""

    model_config = {"from_attributes": True}

    pump_manufacturer: AutopilotManufacturer
    pump_model: str = Field(..., min_length=1, max_length=200)
    pump_displacement_cc: float = Field(
        ..., ge=10, le=2000,
        description="Pumpenverdrängung in cm³/Umdrehung"
    )
    operating_pressure_bar: float = Field(
        ..., ge=10, le=500,
        description="Betriebsdruck in bar"
    )
    fluid_type: HydraulicFluidType
    fluid_volume_l: Optional[float] = Field(
        None, ge=0.1, le=50,
        description="Hydraulikflüssigkeits-Volumen im System in Litern"
    )
    line_inner_diameter_mm: float = Field(
        ..., ge=6, le=25,
        description="Leitungs-Innendurchmesser in mm"
    )
    line_material: str = Field(
        ...,
        description="Leitungsmaterial: nylon_sae_j844, copper_nickel_90_10, stainless_316"
    )
    line_length_total_m: Optional[float] = Field(
        None, ge=0.5, le=30,
        description="Gesamtlänge der Hydraulikleitungen in Metern"
    )
    bypass_valve_type: str = Field(
        ...,
        description="Bypass-Ventil: manual_ball, solenoid, integrated"
    )
    cylinder_bore_mm: Optional[float] = Field(
        None, ge=20, le=200,
        description="Zylinder-Bohrung in mm"
    )
    cylinder_stroke_mm: Optional[float] = Field(
        None, ge=50, le=500,
        description="Zylinder-Hub in mm"
    )
    is_bled: Optional[bool] = Field(
        None,
        description="True wenn System entlüftet ist"
    )
    bleed_cycles_performed: Optional[int] = Field(
        None, ge=0, le=20,
        description="Anzahl durchgeführter Entlüftungszyklen"
    )
    fluid_level_ok: Optional[bool] = Field(
        None,
        description="True wenn Flüssigkeitsstand im Sollbereich"
    )
    leaks_detected: list[str] = Field(
        default_factory=list,
        description="Erkannte Leckagen"
    )
    confidence: ConfidenceLevel = ConfidenceLevel.MEASURED
```

### ANHANG R — Installations-Kostenkalkulation

```python
class InstallationCostItem(BaseModel):
    """Einzelposten der Installations-Kostenkalkulation."""

    model_config = {"from_attributes": True}

    item_name: str = Field(..., min_length=1, max_length=200)
    category: str = Field(
        ...,
        description="Kategorie: hardware, cable, consumable, labor, calibration"
    )
    quantity: float = Field(..., ge=0, le=1000)
    unit: str = Field(
        ..., max_length=20,
        description="Einheit: stück, meter, stunde, liter"
    )
    unit_price_eur: float = Field(..., ge=0, le=50000)
    total_price_eur: Optional[float] = Field(
        None, ge=0, le=100000,
        description="Gesamtpreis (quantity × unit_price)"
    )
    is_optional: bool = Field(
        default=False,
        description="True wenn Position optional"
    )
    note: Optional[str] = Field(None, max_length=500)


class AutopilotInstallationCostEstimate(BaseModel):
    """Gesamte Kostenkalkulation für eine Autopilot-Installation."""

    model_config = {"from_attributes": True}

    boat_type: str = Field(..., min_length=1, max_length=200)
    boat_length_m: float = Field(..., ge=5, le=80)
    installation_type: InstallationType
    drive_type: AutopilotDriveType
    system_manufacturer: AutopilotManufacturer
    system_voltage_v: float = Field(default=12, ge=10, le=48)

    items: list[InstallationCostItem] = Field(
        ..., min_length=1,
        description="Einzelposten der Kalkulation"
    )
    hardware_total_eur: Optional[float] = Field(
        None, ge=0, le=100000,
        description="Summe Hardware-Kosten"
    )
    labor_total_eur: Optional[float] = Field(
        None, ge=0, le=50000,
        description="Summe Arbeitskosten"
    )
    consumables_total_eur: Optional[float] = Field(
        None, ge=0, le=5000,
        description="Summe Verbrauchsmaterial"
    )
    grand_total_eur: Optional[float] = Field(
        None, ge=0, le=200000,
        description="Gesamtkosten inkl. MwSt."
    )
    vat_rate: float = Field(
        default=0.19,
        description="Mehrwertsteuersatz (Standard DE: 0.19)"
    )
    estimated_installation_hours: Optional[float] = Field(
        None, ge=1, le=100,
        description="Geschätzte Installationszeit gesamt in Stunden"
    )
    labor_rate_eur_per_hour: float = Field(
        default=85, ge=30, le=250,
        description="Stundensatz Werft in EUR"
    )
    price_date: Optional[str] = Field(
        None, max_length=10,
        description="Datum der Preiserhebung (YYYY-MM-DD)"
    )
    notes: list[str] = Field(
        default_factory=list,
        description="Anmerkungen zur Kalkulation"
    )
    confidence: ConfidenceLevel = ConfidenceLevel.ESTIMATED
```

### ANHANG R.2 — Typische Kostenkalkulationen nach Bootsklasse

**Kalkulation 1: Segelyacht 35 ft — Linearantrieb Neuinstallation**

| Position | Kategorie | Menge | Einzelpreis | Gesamt |
|----------|-----------|-------|-------------|--------|
| Raymarine EV-200 Kit (T70154) | hardware | 1 | 3.200 € | 3.200 € |
| NMEA-2000-Starter-Kit (Backbone 10m, T-Stücke, Terminatoren) | hardware | 1 | 280 € | 280 € |
| Rudersensor E22078 | hardware | 1 | 220 € | 220 € |
| Marinekabel 10mm² (rot + schwarz) | cable | 20 m | 3,50 €/m | 70 € |
| Marinekabel 2,5mm² (diverse) | cable | 15 m | 1,50 €/m | 23 € |
| ANL-Sicherung 25A + Halter | consumable | 1 | 25 € | 25 € |
| Kabelverschraubungen IP67 | consumable | 6 | 4 € | 24 € |
| Ringkabelschuhe, Schrumpfschlauch | consumable | 1 Set | 30 € | 30 € |
| Sperrholz-Verstärkung 18mm | consumable | 0,3 m² | 35 €/m² | 11 € |
| Edelstahl-Montagewinkel + Bolzen A4-80 | consumable | 1 Set | 45 € | 45 € |
| Sikaflex 291i | consumable | 1 | 15 € | 15 € |
| Kabelbinder, Kontaktfett, Kleinteile | consumable | 1 Set | 30 € | 30 € |
| Installation mechanisch | labor | 6 h | 85 € | 510 € |
| Installation elektrisch/NMEA | labor | 5 h | 85 € | 425 € |
| Kalibrierung + Seatrial | calibration | 4 h | 85 € | 340 € |
| Dokumentation + Eigner-Einweisung | labor | 1,5 h | 85 € | 128 € |
| **GESAMT (netto)** | | | | **5.376 €** |
| **MwSt. 19%** | | | | **1.021 €** |
| **GESAMT (brutto)** | | | | **6.397 €** |

**Kalkulation 2: Motoryacht 45 ft — Hydraulik-Retrofit**

| Position | Kategorie | Menge | Einzelpreis | Gesamt |
|----------|-----------|-------|-------------|--------|
| Simrad AC42N Controller | hardware | 1 | 1.800 € | 1.800 € |
| Simrad HPR-1 Hydraulikpumpe | hardware | 1 | 1.200 € | 1.200 € |
| Simrad HS60 Heading Sensor | hardware | 1 | 650 € | 650 € |
| Simrad RF45X Rudersensor | hardware | 1 | 380 € | 380 € |
| Simrad AP44 Bedieneinheit | hardware | 1 | 750 € | 750 € |
| NMEA-2000-Erweiterungskit | hardware | 1 | 180 € | 180 € |
| Solenoid-Bypass-Ventil | hardware | 1 | 320 € | 320 € |
| Marinekabel 16mm² (rot + schwarz) | cable | 16 m | 5,50 €/m | 88 € |
| Marinekabel 2,5mm² (diverse) | cable | 20 m | 1,50 €/m | 30 € |
| Hydraulikflüssigkeit HLP 15 | consumable | 2 l | 18 €/l | 36 € |
| Hydraulik-Fittings JIC | consumable | 4 | 12 € | 48 € |
| Nylon-Rohr SAE J844 10mm | cable | 3 m | 8 €/m | 24 € |
| ANL-Sicherung 40A + Halter | consumable | 1 | 28 € | 28 € |
| Verbrauchsmaterial (Kabelschuhe etc.) | consumable | 1 Set | 60 € | 60 € |
| Demontage Altsystem | labor | 3 h | 95 € | 285 € |
| Installation mechanisch + Hydraulik | labor | 8 h | 95 € | 760 € |
| Installation elektrisch/NMEA | labor | 5 h | 95 € | 475 € |
| Hydraulik-Entlüftung | labor | 2 h | 95 € | 190 € |
| Kalibrierung + Seatrial | calibration | 5 h | 95 € | 475 € |
| Dokumentation + Eigner-Einweisung | labor | 1,5 h | 95 € | 143 € |
| **GESAMT (netto)** | | | | **7.922 €** |
| **MwSt. 19%** | | | | **1.505 €** |
| **GESAMT (brutto)** | | | | **9.427 €** |

**Kalkulation 3: Segelyacht 28 ft — Tiller-Pilot Selbsteinbau**

| Position | Kategorie | Menge | Einzelpreis | Gesamt |
|----------|-----------|-------|-------------|--------|
| Simrad TP22 Tiller-Pilot | hardware | 1 | 1.180 € | 1.180 € |
| SeaTalk-NG-Kabel 3m | cable | 1 | 35 € | 35 € |
| Marinekabel 6mm² (rot + schwarz) | cable | 10 m | 2,50 €/m | 25 € |
| Sicherung 15A träge + Halter | consumable | 1 | 12 € | 12 € |
| Edelstahl-Augplatte A4-80 | consumable | 1 | 18 € | 18 € |
| Montage-Bolzen M8 A4-80 | consumable | 4 | 2 € | 8 € |
| Schrumpfschlauch + Kabelschuhe | consumable | 1 Set | 15 € | 15 € |
| Sperrholz-Verstärkung | consumable | 1 Stück | 8 € | 8 € |
| Sikaflex 291i | consumable | 1 | 15 € | 15 € |
| **GESAMT (netto)** | | | | **1.316 €** |
| **MwSt. 19%** | | | | **250 €** |
| **GESAMT (brutto)** | | | | **1.566 €** |

*Kein Arbeitskosten bei Selbsteinbau. Zeitaufwand: ca. 5–7 Stunden. (confidence: estimated)*

### ANHANG R.3 — Vergleich Installationskosten: Selbsteinbau vs. Werft

| Tätigkeit | Selbsteinbau (Zeitaufwand) | Werft (Zeitaufwand) | Risiko bei Selbsteinbau |
|-----------|--------------------------|--------------------|-----------------------|
| Mechanische Montage Antrieb | 4–8 h (unerfahren) | 2–4 h | Mittel: Montagefehler, falsche Verschraubung |
| Sperrholz-Verstärkung | 2–4 h | 1–2 h | Niedrig: handwerklich machbar |
| Stromkabel verlegen | 3–6 h | 2–3 h | Hoch: falscher Querschnitt, schlechte Crimps |
| NMEA-2000-Bus aufbauen | 2–4 h | 1–2 h | Mittel: Topologie-Fehler, fehlende Terminierung |
| Kompass montieren | 1–2 h | 0,5–1 h | Hoch: falscher Standort → Deviation |
| Rudersensor montieren | 1–3 h | 0,5–1 h | Mittel: mechanisches Spiel |
| Hydraulik anschließen | 4–8 h (unerfahren) | 2–4 h | Sehr hoch: Luft, falsches Öl, Leckage |
| Compass-Swing | 1–2 h | 0,5–1 h | Mittel: nur bei ruhigen Bedingungen |
| Seatrial + PID-Abstimmung | 3–6 h (ohne Erfahrung) | 2–3 h | Hoch: suboptimale Einstellung |
| **Gesamt** | **21–43 h** | **12–21 h** | |

**Empfehlung nach System-Komplexität:**

| System | Selbsteinbau empfohlen? | Begründung |
|--------|------------------------|-----------|
| Tiller-Pilot | Ja (bei techn. Grundkenntnissen) | Einfach, reversibel, geringes Risiko |
| Wheel-Drive | Bedingt | Elektrik erfordert Sorgfalt, Mechanik einfach |
| Linearantrieb (ohne NMEA) | Bedingt | Mechanik anspruchsvoll, Elektrik kritisch |
| Linearantrieb (mit NMEA 2000) | Eher nein | NMEA-2000-Bus-Aufbau erfordert Erfahrung |
| Hydraulik (in bestehendes System) | Nein | Hydraulik-Fehler können Steuerungsausfall verursachen |
| Hydraulik (neues System) | Definitiv nein | Sicherheitsrelevant, professionelle Installation Pflicht |

**Kostenvergleich Gesamt (Linearantrieb 40 ft):**

| Variante | Material | Arbeit | Gesamt | Risiko |
|----------|---------|--------|--------|--------|
| Selbsteinbau komplett | 3.900 € | 0 € (Eigenleistung) | 3.900 € | Hoch |
| Selbsteinbau Mechanik + Werft Elektrik/Kalibrierung | 3.900 € | 680 € (8h) | 4.580 € | Mittel |
| Werft komplett | 3.900 € | 1.445 € (17h) | 5.345 € | Niedrig |
| Werft Premium (inkl. Dokumentation, erweitert. Seatrial) | 3.900 € | 1.870 € (22h) | 5.770 € | Sehr niedrig |

*Werft-Stundensatz: 85 €/h. (confidence: estimated)*

### ANHANG R.4 — Häufigste Fehler bei der Selbstinstallation (Top 10)

| Rang | Fehler | Konsequenz | Vermeidung |
|------|--------|-----------|-----------|
| 1 | Kabel zu dünn (2,5mm² für 20A-Antrieb) | AP versagt bei Seegang, Low Voltage | Spannungsabfall-Tabelle nutzen (Abschn. 2.2.2) |
| 2 | Kompass neben Lautsprecher | Permanente Fehlsteuerung | Magnetische Vermessung VOR Montage |
| 3 | Kein Compass-Swing durchgeführt | Unbekannte Deviation, falscher Kurs | Compass-Swing ist Pflicht (Abschn. 2.3.4) |
| 4 | NMEA-2000 ohne Terminatoren | Intermittierende Ausfälle | Beide 120Ω-Terminatoren einbauen |
| 5 | Rudersensor-Mittellage nicht kalibriert | Boot steuert ständig schief | Kalibrierung auf dem Wasser (Abschn. 2.3.5) |
| 6 | Sicherung zu nah am Panel statt an Batterie | Brandgefahr bei Kurzschluss | ABYC E-11: max. 200mm von Batterie |
| 7 | Stromkabel über Schaltpanel statt direkt | Zusätzlicher Spannungsabfall | Dedizierte Leitung direkt von Batterie |
| 8 | Hydraulik nicht vollständig entlüftet | Schwammiges Ruder, Overshoot | 5 Entlüftungszyklen minimum |
| 9 | Montageplatte nur auf GFK-Haut | Platte reißt bei Belastung aus | Immer Sperrholz-/Kernverstärkung |
| 10 | Firmware nicht aktualisiert vor Kalibrierung | Kalibrierung ggf. nach Update verloren | Erst Firmware updaten, dann kalibrieren |

### ANHANG R.5 — Garantie und Haftung bei Eigeninstallation

| Hersteller | Garantie bei Eigeninstallation | Garantie bei Werft-Installation | Anmerkungen |
|------------|-------------------------------|--------------------------------|-------------|
| Raymarine | 2 Jahre (3 bei Registrierung) | 2 Jahre (3 bei Registrierung) | Keine Unterscheidung, aber Installationsfehler sind kein Garantiefall |
| B&G | 2 Jahre | 2 Jahre | Garantie erlischt bei nachweislich falscher Installation |
| Garmin | 2 Jahre | 2 Jahre | Installationsfehler ausgeschlossen |
| Simrad | 2 Jahre | 2 Jahre | Wie B&G (gleicher Konzern) |
| Furuno | 2 Jahre (3 bei Registrierung) | 2 Jahre (3 bei Registrierung) | Empfiehlt zertifizierte Installateure |

**Haftungsaspekte Deutschland:**
- **Eigeninstallation:** Eigner haftet für Schäden durch Installationsfehler selbst
- **Werft-Installation:** Werft haftet für Installationsfehler (Gewährleistung 2 Jahre)
- **Versicherung:** Die meisten Kaskoversicherungen akzeptieren Eigeninstallation, aber bei Schäden durch nachweisliche Installationsfehler kann die Leistung gekürzt werden
- **CE-Konformität:** Bei professioneller Nachrüstung muss die CE-Konformitätserklärung des Boots ggf. aktualisiert werden. In der Praxis bei Autopilot-Nachrüstung selten relevant, aber formell erforderlich.

### ANHANG R.6 — Ressourcen und weiterführende Informationen

**Hersteller-Installations-Handbücher (Download-Links):**

| Hersteller | Dokument | Seitenanzahl | Sprache |
|------------|----------|-------------|---------|
| Raymarine | EV-1/EV-2 Installation Guide (81370-3) | 64 Seiten | EN, DE, FR |
| Raymarine | Evolution Autopilot Owner's Handbook | 128 Seiten | EN, DE, FR |
| B&G | NAC-1/2/3 Installation Manual | 48 Seiten | EN |
| B&G | Precision-9 Compass Installation Guide | 12 Seiten | EN |
| Garmin | GHP Reactor Installation Instructions | 52 Seiten | EN, DE |
| Simrad | AC12N/AC42N/AC70 Installation Manual | 56 Seiten | EN |
| Simrad | HS75 GNSS Compass Installation Guide | 24 Seiten | EN |
| Furuno | NAVpilot 300/700 Installation Manual | 96 Seiten | EN |

**Empfohlene Fachliteratur:**

| Titel | Autor | Relevanz |
|-------|-------|----------|
| Boatowner's Mechanical and Electrical Manual | Nigel Calder | Standardwerk Bordelektrik, NMEA 2000 Grundlagen |
| Marine Electrical and Electronics Bible | John C. Payne | Vertiefung Elektrik, EMV, Erdung |
| The Sailor's Book of Small Cruising Sailboats | Steve Henkel | Praxiswissen Autopilot-Nachrüstung |
| NMEA 2000 Explained | Maretron | Offizielle Dokumentation NMEA 2000 |

**Online-Ressourcen:**

| Ressource | URL | Inhalt |
|-----------|-----|--------|
| Panbo (Marine Electronics) | panbo.com | Unabhängige Tests, NMEA-2000-Praxis |
| Compass Marine DIY | marinehowto.com | Elektrik-Anleitungen, Spannungsabfall |
| Cruisers Forum | cruisersforum.com | Eigner-Erfahrungen, Troubleshooting |
| Sailing Anarchy | sailinganarchy.com | Performance-Autopilot-Diskussionen |
| YouTube: Steve on Sailing | youtube.com | Raymarine EV Installation Walkthrough |
| YouTube: Sailing Uma | youtube.com | B&G NAC Retrofit-Dokumentation |

### ANHANG R.7 — Installations-Normen Zusammenfassung

| Norm / Standard | Kernanforderung für AP-Installation | Konsequenz bei Nichteinhaltung |
|-----------------|-------------------------------------|-------------------------------|
| ABYC E-11 | Max. 3% Spannungsabfall für kritische Systeme | AP-Antrieb zu schwach, Low-Voltage-Alarm |
| ABYC E-11 | Sicherung max. 200mm von Batterie | Brandgefahr bei Kurzschluss |
| NMEA 2000 | Linearer Bus, 2 Terminatoren (120Ω) | Intermittierende Kommunikationsfehler |
| NMEA 2000 | Drop-Kabel max. 6m | Signalqualitätsverlust |
| NMEA 2000 | Backbone max. 100m (Micro) | Signal-Degradation |
| IEC 60945 | EMV-Sicherheitsabstände | Kompass-Deviation, Sensorstörung |
| ISO 694 | Kompass-Sicherheitsabstände | Nicht-kompensierbare Deviation |
| ISO 10133 | Kabelführung, Absicherung, Erdung | Sicherheitsrisiko, Versicherungsprobleme |
| ISO 11674 | Autopilot-Mindestleistung, Ansprechzeit | System unterdimensioniert |
| CE/RCD | Konformität der Installation | CE-Zertifizierung des Boots ungültig |

### ANHANG R.4 — Checkliste für die Übergabe an den Eigner

```
ÜBERGABE-CHECKLISTE AUTOPILOT-INSTALLATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DOKUMENTATION ÜBERGEBEN:
□ Schaltplan der Installation (inkl. Kabelquerschnitte, Sicherungen)
□ NMEA-2000-Netzwerkplan (Topologie, Geräteadressen)
□ Kalibrierungswerte (Rudersensor, Kompass-Deviation)
□ PID-Parameter (Gain, Counter-Rudder, Sea State, Totband)
□ Seatrial-Protokoll
□ Hersteller-Handbücher (Controller, Antrieb, Sensoren)
□ Garantie-Registrierung durchgeführt
□ Firmware-Versionen notiert

EIGNER-EINWEISUNG DURCHGEFÜHRT:
□ Ein/Ausschalten des Autopiloten
□ Moduswechsel (Heading, Track, Wind)
□ Kursänderung per Tastendruck
□ Track-Modus vom Plotter (Wegpunkt-Steuerung)
□ Not-Aus / sofortige manuelle Übernahme
□ Alarm-Meldungen verstehen (No Heading, No Rudder, Off Course)
□ Bypass-Ventil Bedienung (bei Hydraulik)
□ Rudersensor: was tun bei "Rudder Limit"-Alarm
□ Wann den Autopiloten NICHT verwenden (Mann-über-Bord, enger Hafen)
□ Jährliche Wartung: was der Eigner selbst prüfen kann
□ Wann die Werft kontaktieren

TESTLAUF MIT EIGNER:
□ Eigner hat Autopilot unter Motor bedient (mind. 15 min)
□ Eigner hat Autopilot unter Segel bedient (wenn Segelyacht)
□ Eigner hat manuelle Übersteuerung getestet
□ Eigner hat Alarm-Situation simuliert erlebt

UNTERSCHRIFT:
Techniker: _________________ Datum: __________
Eigner:    _________________ Datum: __________
```

### ANHANG R.9 — NMEA-2000-PGN-Referenz für Autopilot-Diagnostik

| PGN | Name | Richtung | Diagnostischer Wert |
|-----|------|----------|---------------------|
| 127245 | Rudder | Sensor → Controller | Ruderlage live prüfen: stimmt Anzeige mit Realität? |
| 127250 | Vessel Heading | Kompass → Controller | Heading stabil? Rauschen? Sprünge? |
| 127251 | Rate of Turn | IMU → Controller | Drehrate plausibel? Noise-Level? |
| 127257 | Attitude | IMU → Controller | Roll/Pitch-Werte korrekt? Sensor-Drift? |
| 127258 | Magnetic Variation | GPS → Controller | Korrekte Missweisung für Revier? |
| 128259 | Speed Water | Log → Controller | Fahrt durchs Wasser: Log-Sensor defekt? |
| 129025 | Position Rapid | GPS → Controller | GPS-Fix vorhanden? Genauigkeit? |
| 129026 | COG/SOG Rapid | GPS → Controller | Kurs/Geschwindigkeit über Grund plausibel? |
| 129283 | Cross Track Error | Plotter → Controller | XTE-Wert im Track-Modus: konvergiert der AP? |
| 129284 | Navigation Data | Plotter → Controller | Wegpunkt-Daten korrekt übertragen? |
| 059904 | ISO Request | Diverse | Geräte-Identifikation, Netzwerk-Scan |
| 060928 | ISO Address Claim | Diverse | Adresskonflikte erkennen |
| 126996 | Product Information | Diverse | Hersteller, Modell, Firmware-Version |
| 126998 | Configuration Info | Diverse | Installations-Parameter des Geräts |

**Diagnostik-Tools:**

| Tool | Hersteller | Funktion | Preis (ca.) |
|------|-----------|----------|------------|
| Maretron N2KAnalyzer | Maretron | Vollständige NMEA-2000-Bus-Analyse am PC | 300 € |
| Actisense NGT-1 | Actisense | USB-zu-NMEA-2000-Gateway für PC-Analyse | 250 € |
| Yacht Devices YDNR | Yacht Devices | Netzwerk-Router + Diagnostik über WiFi | 200 € |
| Digital Yacht NavLink2 | Digital Yacht | WiFi-Gateway + NMEA-Diagnostik | 250 € |
| Maretron USB100 | Maretron | USB-Gateway für N2KAnalyzer | 280 € |
| Eingebauter Plotter-Scan | Diverse | Geräteliste + Datenstatus | 0 € (im Plotter) |

---

*Ende der Wissensdatei 21.04 — Autopilot Installation und Kalibrierung*
*AYDI v6 — AI Yacht Design Intelligence*
