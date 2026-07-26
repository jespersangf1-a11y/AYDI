# 22_01 — Bordnetz Grundlagen: DC 12V/24V Systeme, Spannungsebenen, Energiebilanz, Verbraucheranalyse, Bordnetz-Architektur

---

## Metadaten

| Feld | Wert |
|------|------|
| Kategorie | 22 — Elektrik & Elektronik |
| Unterkategorie | 01 — Bordnetz Grundlagen |
| Version | 1.0.0 |
| Letzte Aktualisierung | 2026-05-05 |
| Autor | AYDI Knowledge Engine |
| Sprache | Deutsch (Fachtext) / Englisch (Code) |
| Zielgruppe | Yachtkonstrukteure, Elektroplaner, Surveyor, AYDI-Analysemodul |
| Normenstand | ABYC E-11 (2022), ISO 13297 (2020), ISO 10133 (2012), IEC 60092, DIN VDE 0100-710 |
| Konfidenz-Profil | measured / calculated / benchmark |

---

## INHALTSVERZEICHNIS

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
11. [ANHANG A–H — Fallstudien](#11-anhang-a-h--fallstudien)
12. [ANHANG I–R — Pydantic v2 Modelle](#12-anhang-i-r--pydantic-v2-modelle)

---

## 1. Einführung und Übersicht

### 1.1 Elektrische Bordnetze als Lebensader moderner Yachten

Das elektrische Bordnetz ist das zentrale Nervensystem jeder Yacht. Es versorgt Navigation, Kommunikation, Beleuchtung, Antrieb, Komfortsysteme und Sicherheitseinrichtungen mit Energie. Ein Ausfall des Bordnetzes bedeutet im schlimmsten Fall den Verlust von Navigation, Beleuchtung und Kommunikation — auf See ein potenziell lebensbedrohliches Szenario.

#### Historische Entwicklung

Die Elektrifizierung von Yachten hat sich in den letzten 50 Jahren fundamental gewandelt:

- **1970er:** Minimale Elektrik — Positionslichter, Motorstarter, einfaches UKW
- **1980er:** Erste Navigationsgeräte, Kühlschrank, Autopilot
- **1990er:** GPS, Kartenplotter, elektrische Ankerwinde, Inverterbetrieb
- **2000er:** Netzwerke (NMEA 2000), Watermaker, Klimaanlage
- **2010er:** Lithium-Batterien, LED-Revolution, Touchscreen-Steuerung
- **2020er:** Hybrid/Elektroantrieb, IoT-Integration, DC-Bus-Systeme, Lastmanagement

#### Aktuelle Herausforderungen

| Herausforderung | Auswirkung | Lösungsansatz |
|----------------|------------|---------------|
| Steigende Verbraucheranzahl | Höherer Energiebedarf | Effiziente Komponenten, Energiemanagement |
| Lithium-Technologie | Neue Sicherheitsanforderungen | BMS, thermische Überwachung |
| Hybrid-Antriebe | Komplexe Leistungselektronik | DC-Bus-Architektur |
| IoT/Vernetzung | Cybersecurity, EMV | Galvanische Trennung, Schirmung |
| Gewichtsoptimierung | Dünnere Kabel bei gleicher Last | Spannungsanhebung 24V/48V |
| Regulatorik | Strengere Zulassungsverfahren | Normenkonforme Planung |

### 1.2 Spannungsebenen im Vergleich: 12V vs 24V

#### 12V-Systeme

**Einsatzbereich:** Boote bis ~12m LOA, einfache Segelboote, Motorboote der Einstiegsklasse

**Vorteile:**
- Breite Komponentenverfügbarkeit (Automotive-Markt)
- Niedrige Kosten für Standardkomponenten
- Einfache Fehlersuche mit Standard-Multimeter
- Berührungssicher (SELV — Safety Extra Low Voltage)
- Große Auswahl an Verbrauchern direkt verfügbar

**Nachteile:**
- Hohe Ströme bei großen Verbrauchern → dicke, schwere Kabel
- Signifikanter Spannungsabfall bei langen Leitungen
- Begrenzte Gesamtleistung wirtschaftlich sinnvoll
- Höhere Verlustleistung in Übergangswiderständen
- Maximale wirtschaftliche Systemleistung: ~3.000W

**Typische Kennwerte:**

| Parameter | Wert | Toleranz |
|-----------|------|----------|
| Nennspannung | 12,0 V DC | — |
| Betriebsspannung (Blei) | 12,0–12,8 V | Ruhend |
| Betriebsspannung (LiFePO4) | 12,8–13,6 V | Ruhend |
| Ladespannung (Blei) | 14,2–14,8 V | Bulk/Absorption |
| Ladespannung (LiFePO4) | 14,2–14,6 V | CC/CV |
| Maximaler Spannungsabfall | 3% (kritisch) / 10% (unkritisch) | ABYC E-11 |
| Typische Absicherung | 5A – 200A | Je nach Verbraucher |

#### 24V-Systeme

**Einsatzbereich:** Yachten ab ~12m LOA, alle Fahrtenyachten für Langfahrt, Motoryachten

**Vorteile:**
- Halbierte Ströme bei gleicher Leistung → dünnere Kabel
- Geringerer Spannungsabfall über gleiche Distanz
- Wirtschaftliche Systemleistung bis ~10.000W
- Bessere Effizienz bei Ladern, Invertern, Konvertern
- Standard bei professioneller Seefahrt

**Nachteile:**
- Geringere direkte Komponentenverfügbarkeit im Einstiegsbereich
- DC/DC-Konverter notwendig für 12V-Verbraucher
- Höherer Planungsaufwand
- Lichtbogengefahr bei Kurzschluss höher als bei 12V

**Typische Kennwerte:**

| Parameter | Wert | Toleranz |
|-----------|------|----------|
| Nennspannung | 24,0 V DC | — |
| Betriebsspannung (Blei) | 24,0–25,6 V | Ruhend |
| Betriebsspannung (LiFePO4) | 25,6–27,2 V | Ruhend |
| Ladespannung (Blei) | 28,4–29,6 V | Bulk/Absorption |
| Ladespannung (LiFePO4) | 28,4–29,2 V | CC/CV |
| Maximaler Spannungsabfall | 3% (kritisch) / 10% (unkritisch) | ABYC E-11 |
| Typische Absicherung | 2A – 100A | Je nach Verbraucher |

#### 48V-Systeme (Emerging)

**Einsatzbereich:** Superyachten, Hybrid-/Elektroantriebe, DC-Bus-Architekturen

**Vorteile:**
- Nochmals halbierte Ströme gegenüber 24V
- Optimale Effizienz für Antriebssysteme 5–50 kW
- Noch unter SELV-Grenze (< 50V DC als sicher eingestuft)
- Zukunftssicher für Elektrifizierung

**Nachteile:**
- Eingeschränkte Komponentenverfügbarkeit
- Höhere Anforderungen an Isolationsüberwachung
- Spezielles Wissen bei Wartungspersonal erforderlich
- Noch keine vollständige Normierung im Freizeitbootbereich

### 1.3 Sicherheitsaspekte elektrischer Bordnetze

#### Gefahrenquellen

| Gefahr | Ursache | Schutzmaßnahme |
|--------|---------|----------------|
| Brand | Überhitzung durch Überlast, Kurzschluss | Dimensionierung, Absicherung |
| Explosion | Knallgasentwicklung Bleibatterien | Belüftung, Funkenvermeidung |
| Elektrolyse | Kriechströme im Wasser | Galvanischer Isolator, Anodenprüfung |
| Korrosion | Galvanische Elemente an Verbindungen | Richtige Materialwahl, Versiegelung |
| Personenschaden | Berührung von 230V AC | FI/RCD, Isolationsüberwachung |
| Lichtbogen | Lose Verbindungen unter Last | Drehmomentanzug, Vibrationssicherung |

#### Normative Sicherheitsanforderungen

**ABYC E-11 (AC & DC Electrical Systems on Boats):**
- Maximaler Spannungsabfall: 3% für kritische Verbraucher (Navigation, Lichter)
- Maximaler Spannungsabfall: 10% für unkritische Verbraucher (Komfort)
- Absicherung jedes ungeerdeten Leiters innerhalb 180mm der Stromquelle
- Farbcode: Rot = positiv, Gelb/Schwarz = negativ, Grün = Erdung/Bonding
- Kabelführung: Mindestens 50mm über Bilgenstand, geschützt vor Scheuern

**ISO 13297 (Electrical Systems — Alternating current installations):**
- Fehlerstrom-Schutzschalter (RCD) ≤ 30 mA für alle AC-Kreise
- Galvanische Trennung Landstrom / Bordnetz durch Trenntransformator oder Isolator
- Erdungskonzept: TN-S an Bord, IT-System möglich mit Isolationsüberwachung

**ISO 10133 (Electrical Systems — Extra-low-voltage DC installations):**
- Kabelquerschnitte nach Strombelastbarkeit und Umgebungstemperatur
- Schutz gegen Kurzschluss und Überlast in jedem Stromkreis
- Batterien: belüftete Aufstellung, säurebeständige Wanne, Funkenvermeidung

#### Schutzklassen und Schutzarten (IP-Code)

| Einbauort | Mindest-IP | Begründung |
|-----------|-----------|------------|
| Innenraum trocken | IP20 | Berührungsschutz |
| Pantry / Head | IP44 | Spritzwasser |
| Cockpit / Deck | IP56 | Strahlwasser |
| Maschinenraum | IP55 | Strahlwasser + Öl |
| Unterwasser / Bilge | IP68 | Dauerhafte Überflutung |
| Mastspitze / Außen | IP67 | Zeitweiliges Untertauchen |

---

## 2. Grundlagen und Theorie

### 2.1 Ohmsches Gesetz — Angewandt auf maritime Bordnetze

#### Grundformeln

```
U = R × I         Spannung [V] = Widerstand [Ω] × Strom [A]
P = U × I         Leistung [W] = Spannung [V] × Strom [A]
P = I² × R        Verlustleistung [W] = Strom² [A²] × Widerstand [Ω]
P = U² / R        Leistung [W] = Spannung² [V²] / Widerstand [Ω]
```

#### Leiterwiderstand

```
R = ρ × L / A

  R = Widerstand [Ω]
  ρ = spezifischer Widerstand [Ω·mm²/m]
      Kupfer bei 20°C: 0,0175 Ω·mm²/m
      Kupfer bei 45°C: 0,0193 Ω·mm²/m (marine-relevant!)
      Kupfer bei 60°C: 0,0206 Ω·mm²/m (Maschinenraum!)
  L = Leitungslänge [m] — ACHTUNG: Hin- UND Rückleiter!
  A = Querschnitt [mm²]
```

**Maritime Besonderheit:** Die Leitungslänge im Bordnetz ist IMMER die Gesamtlänge Hin- und Rückleiter. Bei einem Verbraucher 8m von der Batterie entfernt beträgt die relevante Leitungslänge 16m.

#### Temperatureinfluss auf Leiterwiderstand

```
R_T = R_20 × [1 + α × (T - 20)]

  α (Kupfer) = 0,00393 /°C
  
  Beispiel Maschinenraum 60°C:
  R_60 = R_20 × [1 + 0,00393 × 40] = R_20 × 1,157
  → 15,7% höherer Widerstand als bei Raumtemperatur!
```

### 2.2 Spannungsabfall-Berechnung

#### ABYC E-11 Anforderungen

| Verbraucherklasse | Maximaler Spannungsabfall | Beispiele |
|-------------------|--------------------------|-----------|
| Kritisch (3%) | 0,36V bei 12V / 0,72V bei 24V | Navigationslichter, UKW, GPS, Bilgepumpe |
| Unkritisch (10%) | 1,2V bei 12V / 2,4V bei 24V | Innenbeleuchtung, USB-Laden, Lüfter |
| Motor-Start | 10% zulässig | Anlasser, Bugstrahlruder (kurzzeitig) |

#### Berechnungsformel

```
ΔU = (2 × L × I × ρ) / A

  ΔU = Spannungsabfall [V]
  L  = einfache Leitungslänge [m] (Faktor 2 berücksichtigt Rückleiter)
  I  = Betriebsstrom [A]
  ρ  = spez. Widerstand Kupfer [Ω·mm²/m] — temperaturkorrigiert!
  A  = Leiterquerschnitt [mm²]
```

#### Erforderlicher Querschnitt

```
A_min = (2 × L × I × ρ) / ΔU_max

  Beispiel: Ankerwinde 80A, Entfernung 12m, 12V-System, 3% erlaubt:
  ΔU_max = 12V × 0,03 = 0,36V
  A_min = (2 × 12 × 80 × 0,0175) / 0,36 = 93,3 mm²
  → Nächster Normquerschnitt: 95 mm²
  
  Gleiche Winde bei 24V-System:
  I = 40A (halbiert bei doppelter Spannung)
  ΔU_max = 24V × 0,03 = 0,72V
  A_min = (2 × 12 × 40 × 0,0175) / 0,72 = 23,3 mm²
  → Nächster Normquerschnitt: 25 mm²
  
  Gewichtsersparnis: ~70% weniger Kupfer!
```

#### Normquerschnitte (AWG / metrisch)

| AWG | mm² | Typische Anwendung | Max. Strom (30°C) |
|-----|-----|-------------------|-------------------|
| 18 | 0,75 | Signalleitungen, Sensoren | 5A |
| 16 | 1,0 | LED-Beleuchtung, Instrumente | 10A |
| 14 | 1,5 | Innenbeleuchtung, kleine Pumpen | 15A |
| 12 | 2,5 | Steckdosen, Antennen | 20A |
| 10 | 4,0 | Kühlschrank, Wasserpumpe | 30A |
| 8 | 6,0 | Lüftungsgebläse, Ladegeräte | 40A |
| 6 | 10 | Windlass (klein), DC/DC-Konverter | 55A |
| 4 | 16 | Windlass, Bugstrahlruder (klein) | 70A |
| 2 | 25 | Windlass (groß), Inverter | 95A |
| 1 | 35 | Hauptverteilung, Inverter | 125A |
| 1/0 | 50 | Batterieverbindung, Anlasser | 150A |
| 2/0 | 70 | Hauptsicherung, Batterie-Bus | 175A |
| 3/0 | 85 | Schwere Lasten, Parallelbatterien | 200A |
| 4/0 | 95–120 | Hauptversorgungsleitung | 225A |

**Hinweis:** Strombelastbarkeit variiert mit:
- Umgebungstemperatur (Reduktionsfaktor!)
- Bündelverlegung (Reduktionsfaktor 0,7–0,8 bei 3+ Leitungen)
- Kabeltyp (eindrähtig vs. feindrähtig)
- Isolationsmaterial (PVC vs. XLPE vs. Silikon)

#### Reduktionsfaktoren Temperatur

| Umgebungstemperatur | Reduktionsfaktor |
|--------------------|-----------------|
| 30°C | 1,00 |
| 35°C | 0,94 |
| 40°C | 0,87 |
| 45°C | 0,79 |
| 50°C | 0,71 |
| 55°C | 0,61 |
| 60°C | 0,50 |
| 65°C | 0,35 |
| 70°C | NICHT ZULÄSSIG |

### 2.3 Energiebilanz-Erstellung

#### Methodik

Die Energiebilanz ist das fundamentale Planungswerkzeug für jedes Bordnetz. Sie bestimmt:
- Erforderliche Batteriekapazität
- Dimensionierung der Ladesysteme
- Autonomiezeit ohne Ladequelle
- Wirtschaftlichkeit verschiedener Energiequellen

#### Verbraucherklassen

| Klasse | Beschreibung | Beispiele | Priorität |
|--------|-------------|-----------|-----------|
| K1 — Sicherheit | Lebensnotwendig, darf NIE ausfallen | Navigationslichter, UKW, Bilgepumpe, AIS | Höchste |
| K2 — Navigation | Seefahrtsrelevant | GPS, Kartenplotter, Radar, Autopilot | Hoch |
| K3 — Betrieb | Für Schiffsbetrieb notwendig | Ankerwinde, Bugstrahlruder, Motorsteuerung | Hoch |
| K4 — Versorgung | Grundversorgung Crew | Wasserpumpe, Kühlschrank, Kocher | Mittel |
| K5 — Komfort | Komfortsysteme | Klimaanlage, Heizung, Entertainment | Niedrig |
| K6 — Luxus | Nice-to-have | Hydraulikplattform, Sauna, Jacuzzi | Niedrigste |

#### Lastprofil-Erstellung

**Methodik nach Betriebszustand:**

##### Profil: Hafen (Landstrom verfügbar)

| Verbraucher | Leistung [W] | Einschaltdauer [%] | Mittlere Last [W] |
|-------------|-------------|--------------------|--------------------|
| Kühlschrank | 60 | 35 | 21 |
| Beleuchtung (Abend) | 80 | 30 | 24 |
| Ladegeräte (Handy/Laptop) | 100 | 40 | 40 |
| Wasserpumpe | 40 | 5 | 2 |
| Klimaanlage | 1.500 | 60 | 900 |
| Batterie-Ladeerhaltung | 50 | 20 | 10 |
| **Gesamt** | | | **~997 W** |

##### Profil: Nachtfahrt (Motor)

| Verbraucher | Leistung [W] | Einschaltdauer [%] | Mittlere Last [W] |
|-------------|-------------|--------------------|--------------------|
| Navigationslichter | 25 | 100 | 25 |
| Kartenplotter | 30 | 100 | 30 |
| Radar | 45 | 100 | 45 |
| AIS | 5 | 100 | 5 |
| UKW-Radio (Standby) | 3 | 100 | 3 |
| Autopilot | 60 | 80 | 48 |
| Instrumentierung | 15 | 100 | 15 |
| Cockpitbeleuchtung | 10 | 50 | 5 |
| Kühlschrank | 60 | 35 | 21 |
| Heizung | 200 | 40 | 80 |
| Lichtmaschine | −840 | 100 | −840 |
| **Gesamt (netto)** | | | **−563 W (Überschuss)** |

##### Profil: Ankern Tag (kein Motor, kein Landstrom)

| Verbraucher | Leistung [W] | Einschaltdauer [%] | Mittlere Last [W] |
|-------------|-------------|--------------------|--------------------|
| Kühlschrank | 60 | 45 | 27 |
| Wasserpumpe | 40 | 10 | 4 |
| Beleuchtung | 30 | 10 | 3 |
| Ankerlaterne | 10 | 0 | 0 |
| Instrumente (Standby) | 8 | 100 | 8 |
| Ladegeräte | 100 | 30 | 30 |
| Watermaker | 80 | 25 | 20 |
| **Gesamt** | | | **~92 W** |

##### Profil: Ankern Nacht

| Verbraucher | Leistung [W] | Einschaltdauer [%] | Mittlere Last [W] |
|-------------|-------------|--------------------|--------------------|
| Ankerlaterne | 10 | 100 | 10 |
| Kühlschrank | 60 | 30 | 18 |
| Beleuchtung (Abend) | 60 | 40 | 24 |
| Heizung/Lüftung | 150 | 30 | 45 |
| Instrumente (Standby) | 5 | 100 | 5 |
| AIS (Standby) | 3 | 100 | 3 |
| Ankeralarm | 2 | 100 | 2 |
| **Gesamt** | | | **~107 W** |

##### Profil: Segeln Tag

| Verbraucher | Leistung [W] | Einschaltdauer [%] | Mittlere Last [W] |
|-------------|-------------|--------------------|--------------------|
| Kartenplotter | 30 | 100 | 30 |
| Autopilot | 80 | 90 | 72 |
| Windmesser/Instrumente | 10 | 100 | 10 |
| AIS | 5 | 100 | 5 |
| UKW (Standby) | 3 | 100 | 3 |
| Kühlschrank | 60 | 40 | 24 |
| Wasserpumpe | 40 | 5 | 2 |
| Elektrische Winsch | 500 | 5 | 25 |
| **Gesamt** | | | **~171 W** |

#### Autonomieberechnung

```
Autonomie [h] = (Batteriekapazität [Ah] × Nennspannung [V] × DoD × η_system) / P_mittel [W]

  DoD = Depth of Discharge
    Blei-Säure: 50% (optimal) / 80% (Notfall)
    AGM: 50% (optimal) / 70% (Notfall)  
    LiFePO4: 80% (optimal) / 95% (Notfall)
    
  η_system = Systemeffizienz (Wandler, Leitungen)
    Typisch: 0,85–0,92

Beispiel: 400 Ah LiFePO4, 12V, Ankerprofil Nacht (107W):
  Autonomie = (400 × 12 × 0,80 × 0,90) / 107 = 32,3 Stunden
```

#### Ladebilanz

```
Ladezeit [h] = (Entnommene_Energie [Ah] × 1,15) / Ladestrom_effektiv [A]

  Faktor 1,15 = Ladeeffizienz (Wärme, Absorption)
  
  Ladestrom_effektiv bei Blei:
    Bulk-Phase: C/5 bis C/3 (80–100 Ah: 20–33A)
    Absorption: abnehmend von C/5 auf C/20
    Float: C/100
    
  Ladestrom_effektiv bei LiFePO4:
    CC-Phase: C/2 bis 1C (effektiv ~95%)
    CV-Phase: abnehmend (kurz, da schmale CV-Range)
```

### 2.4 Bordnetz-Topologie

#### Bus-Topologie

```
Batterie ─── Hauptsicherung ─── Hauptverteiler (Bus-Bar)
                                     │
                    ┌────────────────┼────────────────┐
                    │                │                │
              Steuerbord-Bus   Backbord-Bus    Maschinenraum-Bus
                    │                │                │
                  ┌─┼─┐          ┌─┼─┐          ┌─┼─┐
                  V V V          V V V          V V V
```

**Vorteile:**
- Einfache Erweiterung
- Kurze Stichleitungen zu Verbrauchern
- Übersichtliche Fehlersuche

**Nachteile:**
- Single Point of Failure am Hauptbus
- Lange Hauptleitung muss für Gesamtlast dimensioniert sein
- Bei Kurzschluss am Bus fällt alles aus

#### Stern-Topologie (Radial)

```
                         Batterie
                           │
                     Hauptsicherung
                           │
                   Sicherungsverteiler
                  /    |    |    |    \
                 V1   V2   V3   V4   V5
```

**Vorteile:**
- Jeder Kreis individuell abgesichert
- Fehler betrifft nur einen Verbraucher
- Einfache Fehlersuche durch Ausschluss

**Nachteile:**
- Mehr Kabel, mehr Gewicht
- Größerer Verteiler nötig
- Höhere Kosten bei vielen Kreisen

#### Ring-Topologie (Redundant)

```
Batterie 1 ──── Verteiler A ──── Verteiler B ──── Batterie 2
    │                                                    │
    └──────────────── Ring-Verbindung ───────────────────┘
```

**Vorteile:**
- Redundanz: Versorgung von zwei Seiten
- Kein Single Point of Failure
- Für sicherheitskritische Systeme

**Nachteile:**
- Doppelte Kabelführung
- Komplexere Absicherung (Richtungserkennung)
- Teure Schaltgeräte

#### Hybrid-Topologie (Praxis-Standard)

Die meisten professionellen Yachten nutzen eine Kombination:
- **Ring** für sicherheitskritische Verbraucher (Navigation, Bilge)
- **Stern** für Hauptverteiler zu Unterverteilern
- **Bus** innerhalb von Zonen (z.B. alle Kabinenlichter an einem Bus)

```
┌─────────────────────────────────────────────────────────┐
│                    HAUPT-BUS-BAR                         │
│  ┌────┐  ┌────┐  ┌────┐  ┌────┐  ┌────┐  ┌────┐      │
│  │Bat1│  │Bat2│  │LiMa│  │Solar│ │Shore│  │Inv │      │
│  └──┬─┘  └──┬─┘  └──┬─┘  └──┬─┘  └──┬─┘  └──┬─┘      │
│     │       │       │       │       │       │          │
│  ═══╪═══════╪═══════╪═══════╪═══════╪═══════╪════════  │
│     │                                                   │
│  ┌──┴──────────────┐    ┌──────────────────┐           │
│  │  DC-Verteiler   │    │  AC-Verteiler    │           │
│  │  (gesichert)    │    │  (über Inverter) │           │
│  └─┬──┬──┬──┬──┬──┘    └─┬──┬──┬──┬──┬──┘           │
│    │  │  │  │  │          │  │  │  │  │               │
│   Nav Licht Pumpen Inst Komf  Steckd Klima WM Kocher   │
└─────────────────────────────────────────────────────────┘
```

### 2.5 Erdung und Massekonzept

#### Begriffe

| Begriff | Bedeutung | Farbe |
|---------|-----------|-------|
| Masse (DC-Rückleiter) | Negativer Pol, Stromrückführung | Gelb oder Schwarz |
| Erdung (Bonding) | Schutzverbindung metallischer Teile | Grün oder Grün/Gelb |
| Schiffsmasse (Ground Plate) | Verbindung zum Seewasser über Erdungsplatte | — |

#### Erdungskonzept (Bonding System)

**Zweck:**
1. Personenschutz: Potentialausgleich aller berührbaren Metallteile
2. Blitzschutz: Ableitung von Blitzströmen
3. Korrosionsschutz: Definiertes Potential für Zinkanoden
4. EMV: Schirmung und Entstörung

**ABYC E-11 Bonding-Anforderungen:**
- Alle metallischen Borddurchlässe verbinden
- Motor, Getriebe, Welle verbinden
- Stevenrohr, Ruderschaft verbinden
- Shrouds/Wantenspanner optional (Blitzschutz)
- Minimum Querschnitt Bonding-Leiter: 6 mm² (AWG 8)

**Sternförmige Masseführung:**
```
                    Bonding-Bus-Bar (zentral)
                    /    |    |    |    \
                   /     |    |    |     \
            Motor  Welle  BD1  BD2  Tank  Ruder
```

**WICHTIG — Galvanische Korrosion vermeiden:**
- NIEMALS DC-Masse und Bonding-System verbinden (außer an EINEM definierten Punkt)
- Landstrom-Schutzleiter über galvanischen Isolator oder Trenntransformator
- Bonding-Leiter isoliert verlegen (kein Kontakt zu Bilgenwasser)

### 2.6 Kabeltypen und -auswahl

#### Marine-zugelassene Kabeltypen

| Typ | Bezeichnung | Einsatz | Temperatur | Besonderheit |
|-----|-------------|---------|-----------|-------------|
| Marinekabel verzinnt | LIYCY-TP-OZ/NYMHY-J | Standard Bordnetz | -30..+70°C | Verzinnte Litzen, UV-beständig |
| FLRY-B | KFZ-Leitung | Motorraum, Signal | -40..+105°C | Dünnwandig, ölbeständig |
| NSGAFÖU | Schweißkabel | Batterie-Verbindung | -25..+80°C | Hochflexibel, kurzschlussfest |
| H07RN-F | Gummikabel | AC-Installation | -25..+60°C | Nassraum, mechanisch robust |
| LiYCY | Geschirmt | Signalkabel, Sensoren | -30..+70°C | EMV-geschirmt |
| Koaxial RG213 | Antennenkabel | UKW, Radar | -40..+85°C | 50Ω, salzwasserresistent |
| Cat6 STP | Netzwerk | Ethernet, NMEA-Ethernet | -20..+60°C | Geschirmt, marinisiert |

#### Kabel-Derating bei Bündelverlegung

| Anzahl Leiter im Bündel | Derating-Faktor |
|--------------------------|-----------------|
| 1–3 | 1,00 |
| 4–6 | 0,80 |
| 7–10 | 0,70 |
| 11–20 | 0,60 |
| >20 | 0,50 |

#### Verbindungstechnik

| Methode | Anwendung | Qualität | Widerstand |
|---------|-----------|----------|-----------|
| Crimpverbindung (richtig) | Standard, alle Querschnitte | Sehr gut | <0,1 mΩ |
| Schraubklemme (verzinnt) | Verteiler, Sicherungen | Gut | <0,5 mΩ |
| Lötverbindung + Schrumpf | Signalleitungen, Reparatur | Gut (wenn korrekt) | <0,1 mΩ |
| Löten OHNE Schrumpf | VERBOTEN | Schlecht | variabel |
| Wagoklemme | NUR trockener Innenraum | Bedingt | <0,5 mΩ |
| Quetschverbinder (billig) | VERBOTEN auf Booten | Unzureichend | >1 mΩ |

**Crimp-Qualitätskriterien:**
- Richtige Hülsengröße für Querschnitt
- Crimp-Werkzeug mit Ratsche (definierte Kraft)
- Leiter vollständig in Hülse, keine freien Litzen
- Isolationsabschnitt der Hülse greift auf Kabelmantel
- Schrumpfschlauch mit Kleber über Verbindungsstelle
- Zugprüfung nach Norm (kein Herausziehen bei definierter Kraft)

---

## 3. Typenübersicht

### 3.1 Einrumpf-Segelboot 12V (8–12m)

#### Systembeschreibung

**Typische Vertreter:** Dehler 34, Bavaria C38, Jeanneau Sun Odyssey 349

**Architektur:**
- Eine Batterie-Bank Service (1–2 × 12V Bleibatterien, 100–220 Ah)
- Separate Starterbatterie (70–100 Ah)
- Lichtmaschine Motor (12V, 80–120A)
- Optionaler Laderegler für Solar (50–150 Wp)
- Sicherungsverteiler mit 8–14 Kreisen
- Landstrom-Ladegerät (12V, 20–40A)

**Energiebilanz:**

| Betriebszustand | Mittlere Last [W] | Autonomie (200 Ah, Blei, 50% DoD) |
|----------------|-------------------|-------------------------------------|
| Hafen (ohne Klima) | 85 | ~14 h |
| Tagessegeln | 140 | ~8,5 h |
| Nachtfahrt | 220 | ~5,5 h |
| Ankern Tag | 65 | ~18,5 h |
| Ankern Nacht | 90 | ~13,3 h |

**Typischer Kabelplan:**

```
Starterbatterie 12V/80Ah ─── [200A ANL] ─── Motorstarter
         │
    [Batterie-Trennrelais Cyrix-i]
         │
Servicebatterie 12V/200Ah ─── [150A ANL] ─── Hauptverteiler
         │                                         │
    Lichtmaschine 12V/90A                    ┌─────┼─────┐─────┐
         │                                   │     │     │     │
    [Laderegler extern]               Nav  Licht Pumpen Inst Komfort
                                      10A   10A   15A   5A   15A
    Solar 100Wp ─── [Solarregler MPPT]
         │
    Landstrom 230V ─── [Ladegerät 12V/30A]
```

**Besonderheiten:**
- Gesamtkabellänge: 80–150m
- Gesamtgewicht Elektrik: 15–30 kg
- Hauptproblem: Spannungsabfall zum Bug (Ankerwinde!)
- Mastverkabelung über Stecker (Empfehlung: vergoldete Kontakte)

### 3.2 Fahrtenyacht 24V (12–16m)

#### Systembeschreibung

**Typische Vertreter:** Hallberg-Rassy 44, Oyster 495, Swan 48

**Architektur:**
- Haupt-Service-Bank 24V (LiFePO4, 400–800 Ah)
- Starterbatterie 24V (AGM, 100 Ah)
- DC/DC-Konverter 24V→12V für Legacy-Geräte (30–60A)
- Lichtmaschine 24V (100–175A) mit externem Regler
- Solar-Array 500–1200 Wp mit MPPT-Reglern
- Windgenerator 24V (200–400W)
- Inverter/Charger 24V/3000W
- Landstrom-Anschluss 230V/16A oder 32A
- Digitaler Sicherungsverteiler (16–24 Kreise)
- Batterie-Monitor (Shunt-basiert)

**Energiebilanz:**

| Betriebszustand | Mittlere Last [W] | Autonomie (600 Ah LiFePO4, 24V, 80% DoD) |
|----------------|-------------------|---------------------------------------------|
| Hafen (Komfort) | 350 | ~33 h |
| Tagessegeln | 250 | ~46 h |
| Nachtfahrt (Motor) | 380 | ~30 h (+ LiMa Überschuss) |
| Ankern Tag | 180 | ~64 h |
| Ankern Nacht | 150 | ~77 h |
| Passage (24h Schnitt) | 280 | ~41 h |

**Erweiterte Architektur:**

```
┌─────────────────────────────────────────────────────────────┐
│                    24V HAUPT-BUS                             │
│                                                             │
│  ┌──────┐  ┌──────┐  ┌──────┐  ┌─────┐  ┌──────┐         │
│  │LiFePO│  │Start │  │LiMa  │  │Solar│  │Wind  │         │
│  │600Ah │  │ AGM  │  │24V   │  │MPPT │  │Gen   │         │
│  │ 24V  │  │100Ah │  │150A  │  │     │  │24V   │         │
│  └──┬───┘  └──┬───┘  └──┬───┘  └──┬──┘  └──┬───┘         │
│     │         │         │         │        │              │
│  ══╪═════════╪═════════╪═════════╪════════╪═══════════    │
│     │                                                      │
│  ┌──┴─────────────────────────┐  ┌─────────────────┐      │
│  │   24V DC-Verteiler         │  │  DC/DC 24→12V   │      │
│  │   (Digital/Programmierbar) │  │  30A / 60A      │      │
│  └─┬──┬──┬──┬──┬──┬──┬──┬───┘  └──┬──────────────┘      │
│    │  │  │  │  │  │  │  │          │                      │
│   Nav AP Anker Pumpen WM Hzg Lüft DC│  ┌──────────────┐   │
│                                      │  │ 12V-Verteiler│   │
│                                      │  └┬──┬──┬──┬───┘   │
│  ┌────────────────┐                  │   │  │  │  │       │
│  │Inverter/Charger│                  │  UKW GPS AIS Inst  │
│  │24V DC → 230V AC│                  │                     │
│  │3000W / 120A Lad│                  │                     │
│  └──┬─────────────┘                  │                     │
│     │                                │                     │
│  ┌──┴─────────────┐  ┌─────────┐    │                     │
│  │ AC-Verteiler   │  │Landstrom│    │                     │
│  │ (FI/RCD)       │←─┤230V/16A │    │                     │
│  └─┬──┬──┬──┬────┘  └─────────┘    │                     │
│    │  │  │  │                        │                     │
│  Steckd Boiler Klima Wasserkocher    │                     │
└─────────────────────────────────────────────────────────────┘
```

### 3.3 Motoryacht 24V + 230V (14–22m)

#### Systembeschreibung

**Typische Vertreter:** Princess 62, Azimut 55, Sunseeker Manhattan 60

**Architektur:**
- Haupt-Service-Bank 24V (AGM oder LiFePO4, 800–1600 Ah)
- Starterbatterien 2×24V (je Motor ein Satz)
- Generator 230V/400V, 8–20 kVA
- Landstrom 230V/63A oder 400V/32A (Drehstrom)
- Inverter/Charger 24V/5000–8000W
- Klimaanlage: eigener AC-Kreis, direkt vom Generator
- Stabilisatoren: eigener Hydraulik-Kreis
- Digital Switching System (CAN-Bus basiert)
- Touchscreen-Steuerung aller Kreise
- DC/DC 24V→12V für Entertainment und 12V-Geräte

**Energiebilanz:**

| Betriebszustand | Mittlere Last [W] | Quelle |
|----------------|-------------------|--------|
| Hafen (Landstrom) | 3.500 | Landstrom 230V |
| Fahrt Tag | 1.200 (DC) + 4.000 (AC/Generator) | LiMa + Generator |
| Ankern Tag (Generator) | 800 (DC) + 3.000 (AC) | Generator 2h + Batterie |
| Ankern Nacht | 400 (DC) + 1.500 (AC via Inverter) | Batterie |

**Besonderheiten Motoryacht:**
- Doppelte Redundanz für alle sicherheitskritischen Systeme
- Separate Stromkreise für Flybridge und Hauptdeck
- Stabilisatoren benötigen eigene 24V-Versorgung (Hydraulikpumpe)
- Entertainment-System mit eigenem 12V-Kreis und Masse
- Kameraüberwachung (IP) über PoE-Switch
- Tankfüllstandsmessung über CAN-Bus integriert

### 3.4 Katamaran Dual-Bus (12–18m)

#### Systembeschreibung

**Typische Vertreter:** Lagoon 46, Fountaine Pajot Elba 45, Leopard 45

**Architektur:**
- Zwei unabhängige Batterie-Bänke (Backbord / Steuerbord)
- Cross-Connect mit manuellem oder automatischem Umschalter
- Jeder Rumpf autark lauffähig (Redundanz!)
- Brücken-Verteiler im Salon/Cockpit
- Zwei Lichtmaschinen (je Motor)
- Solar auf Bimini/Dach: Aufteilung auf beide Bänke oder MPPT mit Dual-Output

**Dual-Bus-Architektur:**

```
┌───── BACKBORD-RUMPF ─────┐     ┌───── STEUERBORD-RUMPF ─────┐
│                           │     │                             │
│  Batterie BB 24V/400Ah   │     │  Batterie SB 24V/400Ah     │
│         │                 │     │         │                   │
│    ┌────┴────┐            │     │    ┌────┴────┐              │
│    │BB-Verteil│            │     │    │SB-Verteil│              │
│    └────┬────┘            │     │    └────┬────┘              │
│         │                 │     │         │                   │
│  BB-Motor, BB-Kabinen     │     │  SB-Motor, SB-Kabinen      │
│  BB-Licht, BB-Pumpen      │     │  SB-Licht, SB-Pumpen       │
│                           │     │                             │
└────────────┬──────────────┘     └──────────────┬──────────────┘
             │                                    │
             └──────── CROSS-CONNECT ─────────────┘
                    (ACR / Manuell-Schalter)
                           │
                  ┌────────┴────────┐
                  │ Salon-Verteiler │
                  │ (Brückenlasten) │
                  └─┬──┬──┬──┬──┬──┘
                    │  │  │  │  │
                  Nav AP Plotter Inv Entertainment
```

**Besonderheiten Katamaran:**
- Galvanische Trennung zwischen den Rümpfen bei GFK-Booten nicht zwingend nötig
- Bei Alu-Katamaranen: strikte Trennung mit DC/DC-Isolator
- Solarfläche auf Kat deutlich größer als bei Einrumpf (20–40 m² Dachfläche)
- Typische Solar-Leistung: 1500–3000 Wp
- Langfahrt-Kats oft mit großem LiFePO4-System (800–1600 Ah @ 24V)
- AC oft über Inverter betrieben, Generator nur als Backup

### 3.5 Superyacht Multi-Bus (24m+)

#### Systembeschreibung

**Typische Vertreter:** Lürssen, Feadship, Amels, Heesen (individuell geplant)

**Architektur:**
- Hauptnetz 400V AC (Drehstrom) vom Generator
- DC-Bus 48V oder 700V (Hybrid-Antrieb)
- Transformatoren auf 230V für Verbraucher
- USV (Unterbrechungsfreie Stromversorgung) für kritische Systeme
- Batteriespeicher (Lithium) für Null-Emissions-Betrieb
- Power Management System (PMS) mit automatischer Lastverteilung
- Mehrere Generatoren (2–4) mit automatischer Zuschaltung
- Landstromanschluss 400V/125A oder höher
- Separates Notversorgungsnetz (Emergency Switchboard)

**Multi-Bus-Architektur:**

```
┌─────────────────────────────────────────────────────────────────┐
│                    MAIN SWITCHBOARD (MSB)                         │
│                    400V AC / 50Hz / 3-Phase                       │
│                                                                   │
│  ┌─────┐  ┌─────┐  ┌─────┐  ┌────────┐  ┌─────────────────┐   │
│  │Gen 1│  │Gen 2│  │Gen 3│  │Shore   │  │Battery System  │   │
│  │200kW│  │200kW│  │100kW│  │400V/125A│  │700V DC / 200kWh│   │
│  └──┬──┘  └──┬──┘  └──┬──┘  └───┬────┘  └───────┬─────────┘   │
│     │        │        │         │                │              │
│  ═══╪════════╪════════╪═════════╪════════════════╪═══════════   │
│     │                                                            │
│  ┌──┴──────────────────────────────────────────────────────┐    │
│  │              POWER MANAGEMENT SYSTEM (PMS)                │    │
│  │  - Automatische Lastverteilung                            │    │
│  │  - Generator Start/Stopp                                  │    │
│  │  - Lastabwurf (Priority Shedding)                        │    │
│  │  - Peak Shaving (Batterie)                               │    │
│  │  - Nullemissionsbetrieb (Silent Mode)                    │    │
│  └──┬────────┬──────────┬──────────┬───────────┬───────────┘    │
│     │        │          │          │           │                │
│  ┌──┴──┐ ┌──┴──┐   ┌──┴──┐   ┌──┴──┐   ┌──┴──┐              │
│  │Prop │ │HVAC │   │Hotel│   │Deck │   │Nav  │              │
│  │Bus  │ │Bus  │   │Bus  │   │Bus  │   │Bus  │              │
│  │     │ │     │   │     │   │     │   │(USV)│              │
│  └─────┘ └─────┘   └─────┘   └─────┘   └─────┘              │
│                                                                   │
│  EMERGENCY SWITCHBOARD (ESB)                                     │
│  - Automatische Umschaltung bei Hauptnetzausfall                 │
│  - USV-gestützt (min. 18h Notbetrieb)                           │
│  - Notbeleuchtung, Navigationslichter, UKW, Feuerlöschpumpe     │
└─────────────────────────────────────────────────────────────────┘
```

**Besonderheiten Superyacht:**
- Klassifikationsgesellschaft (Lloyd's, DNV, BV) vorgeschrieben
- Redundanzklasse: Verlust eines Generators darf nicht zum Blackout führen
- Kabelbrandschutz: Halogenfreie, flammwidrige Kabel (IEC 60332)
- Kabeltrassen feuerbeständig (A60-Schott-Durchführungen)
- Isolationsüberwachung (IMD) auf allen DC-Kreisen
- Automatische Feuerlöschung im Maschinenraum entkoppelt Elektrik
- Mindestens 2 unabhängige Bilgepumpen-Kreise
- Gesamt-Kabelgewicht: 5.000–20.000 kg bei 30–60m Yachten!

---

## 4. Produktlinien und Spezifikationen

### 4.1 Victron Energy

**Herkunft:** Niederlande, Almere
**Spezialisierung:** Energiesysteme für mobile und maritime Anwendungen
**Besonderheit:** Offenes Protokoll (VE.Direct, VE.Bus, VE.Can), umfangreiches Ökosystem

#### Batterieladegeräte

| Modell | Eingangsspannung | Ausgangsspannung | Ladestrom | Phasen | Besonderheit |
|--------|-----------------|-----------------|-----------|--------|-------------|
| Blue Smart IP67 12/25 | 180–265V AC | 12V | 25A | 3-stufig + BT | Wasserdicht IP67, Bluetooth |
| Blue Smart IP22 24/16 | 180–265V AC | 24V | 16A | 3-stufig + BT | Wandmontage, DIP-Switch |
| Centaur 12/60 | 90–265V AC | 12V | 60A | 3 Ausgänge | Robust, ohne Elektronik-Schnick |
| Centaur 24/30 | 90–265V AC | 24V | 30A | 3 Ausgänge | Robust, ohne Elektronik-Schnick |
| Skylla-IP65 24/35 | 180–265V AC | 24V | 35A | VE.Can, IP65 | Parallel-fähig |
| Phoenix Smart IP43 24/25 | 180–265V AC | 24V | 25A | 5-stufig | Adaptives Profil |

#### Inverter und Inverter/Charger

| Modell | DC-Eingang | AC-Ausgang | Dauerleistung | Spitze | Besonderheit |
|--------|-----------|-----------|--------------|--------|-------------|
| Phoenix 12/1200 | 12V | 230V/50Hz | 1.200W | 2.400W | Reiner Sinus |
| Phoenix 24/3000 | 24V | 230V/50Hz | 3.000W | 6.000W | Reiner Sinus |
| MultiPlus-II 24/3000/70 | 24V | 230V/50Hz | 3.000W | 6.000W | Inverter + Charger + Transfer |
| MultiPlus-II 48/5000/70 | 48V | 230V/50Hz | 5.000W | 10.000W | Parallel bis 6 Geräte |
| Quattro 24/5000/120 | 24V | 230V/50Hz | 5.000W | 10.000W | 2× AC-Eingang, programmierbarer Ausgang |
| Quattro 48/10000/140 | 48V | 230V/50Hz | 10.000W | 20.000W | Für große Systeme |

#### MPPT-Solarladeregler

| Modell | Max PV-Spannung | Max Ladestrom | Batteriespannung | Besonderheit |
|--------|----------------|--------------|-----------------|-------------|
| SmartSolar 75/15 | 75V | 15A | 12/24V | BT, klein |
| SmartSolar 100/30 | 100V | 30A | 12/24V | BT, VE.Direct |
| SmartSolar 150/45 | 150V | 45A | 12/24/48V | BT, VE.Direct |
| SmartSolar 250/70 | 250V | 70A | 12/24/48V | VE.Can, BT |
| SmartSolar 250/100 | 250V | 100A | 12/24/48V | VE.Can, BT, Tr-Version |

#### Batterie-Monitore

| Modell | Messmethode | Genauigkeit | Anzeige | Konnektivität |
|--------|------------|-------------|---------|---------------|
| BMV-712 Smart | Shunt 500A | ±0,5% | LCD + BT App | VE.Direct, BT |
| SmartShunt 500A | Shunt 500A | ±0,5% | Nur App | VE.Direct, BT |
| Lynx Smart BMS | Integriert | ±1% | — | VE.Can, VE.Bus |

#### Systemintegration

| Produkt | Funktion | Protokoll |
|---------|----------|-----------|
| Cerbo GX | System-Gateway, Monitoring | VE.Can, VE.Bus, VE.Direct, NMEA 2000, WiFi, BT |
| GX Touch 50/70 | Touchscreen-Display | — (am Cerbo GX) |
| VRM Portal | Cloud-Monitoring & -Steuerung | HTTPS/MQTT |

### 4.2 Mastervolt

**Herkunft:** Niederlande, Amsterdam (Teil der Navico-Gruppe)
**Spezialisierung:** Premium-Bordnetzsysteme, Superyacht-Segment
**Besonderheit:** MasterBus Netzwerk, vollintegrierte Systeme

#### Ladegeräte

| Modell | Eingangsspannung | Ausgang | Ladestrom | Besonderheit |
|--------|-----------------|--------|-----------|-------------|
| ChargeMaster Plus 24/40 | 90–265V AC | 24V | 40A | 3 Ausgänge, CZone-ready |
| ChargeMaster Plus 12/75 | 90–265V AC | 12V | 75A | 3 Ausgänge, CZone-ready |
| Mass 24/50 | 90–265V AC | 24V | 50A | MasterBus, DNV-zertifiziert |
| Mass 24/100 | 90–265V AC | 24V | 100A | MasterBus, Superyacht |

#### Inverter und Kombigeräte

| Modell | DC-Eingang | AC-Ausgang | Dauerleistung | Besonderheit |
|--------|-----------|-----------|--------------|-------------|
| Mass Sine 24/2500 | 24V | 230V | 2.500W | Reiner Sinus, MasterBus |
| Mass Combi Ultra 24/3500 | 24V | 230V | 3.500W | Inverter+Charger 100A |
| Mass Combi Pro 24/4000 | 24V | 230V | 4.000W | MasterBus, 120A Charger |

#### CZone Digital Switching

| Komponente | Funktion | Kanäle | Bus |
|------------|----------|--------|-----|
| CZone Output Interface (COI) | Schaltausgang | 12 × 20A | CAN |
| CZone Motor Output Interface (MOI) | H-Brücke | 6 × 20A | CAN |
| CZone Signal Interface (SI) | Analogeingänge | 12 Kanäle | CAN |
| CZone Combination Output Interface (CLOI) | Mix Schalt + Signal | 6+6 | CAN |
| CZone Display Interface | Touchscreen | — | CAN |
| CZone Wireless Interface | WiFi-Gateway | — | CAN + WiFi |

### 4.3 Blue Sea Systems

**Herkunft:** USA, Bellingham WA
**Spezialisierung:** Stromverteilung, Sicherungen, Schalter, Panels
**Besonderheit:** Branchenstandard für Verteiler und Sicherungspanels in Nordamerika

#### Sicherungs- und Verteilersysteme

| Produktlinie | Typ | Nennstrom | Besonderheit |
|-------------|-----|-----------|-------------|
| ST Blade Fuse Block | ATO/ATC Sicherung | 5–30A pro Kreis | 6/12 Kreise, negative Bus-Bar |
| MRBF Terminal Fuse | Bolzensicherung | 30–300A | Direkt auf Batterie, kompakt |
| ANL Fuse Block | ANL-Sicherung | 35–750A | Hauptsicherung, Inverterschutz |
| Class T Fuse | Hochleistung | 110–400A | Kurzschlussschutz für Inverter |
| ML-Series Panels | Thermisch + Magnetisch | 5–50A | Selbstrückstellend, DIN-Schiene |

#### Bus-Bars und Verteiler

| Modell | Pole | Max. Strom | Material | Besonderheit |
|--------|------|-----------|----------|-------------|
| PowerBar 1000 | 4–12 Anschlüsse | 1.000A gesamt | Verzinntes Kupfer | Modularer Aufbau |
| DualBus Plus 150A | 2 × Bus | 150A je Bus | Verzinntes Kupfer | + und − kombiniert |
| Common 150A BusBar | 20 Anschlüsse | 150A | Tin-plated Copper | Schienenmontage |
| Battery Terminal Mount | 2 Bolzen | 500A | — | Direktmontage Batteriepol |

#### Batterie-Management

| Produkt | Funktion | Kapazität | Protokoll |
|---------|----------|-----------|-----------|
| m-LVD | Low Voltage Disconnect | 65A | Analog |
| ML-ACR | Automatic Charging Relay | 500A | VSR + Timer |
| SI-ACR | Automatic Charging Relay | 120A | VSR |
| Add-A-Battery | Dual-Bank Isolation | 65A | Dioden-frei |

### 4.4 BEP Marine

**Herkunft:** Neuseeland (Teil der Navico-Gruppe)
**Spezialisierung:** Batterieschalter, Stromverteilung, Gasdetektoren
**Besonderheit:** AIS-Zertifiziert, bekannt für robuste mechanische Schalter

#### Batterieschalter

| Modell | Kapazität | Pole | Besonderheit |
|--------|-----------|------|-------------|
| 701 Medium Duty | 275A cont. / 455A int. | 1 Batterie | Standardschalter |
| 720 Heavy Duty | 350A cont. / 500A int. | 2 Batterien + Both | Dual-Bank |
| 721 Dual Operation | 500A cont. / 750A int. | Parallel | Motor-geeignet |
| 772-DBC | 500A | 1 Bank | Fernbedienbar (Motorraumschalter) |

#### Gasdetektoren

| Modell | Detektiert | Sensoren | Alarm |
|--------|-----------|---------|-------|
| BEP 600-GD | LPG, Benzin | 1 Sensor | Optisch + Akustisch |
| BEP 600-GDL | LPG, Benzin | 2 Sensoren | + Schaltausgang (Magnetventil) |

### 4.5 Marinco / ProMariner

**Herkunft:** USA
**Spezialisierung:** Landstrom-Anschlüsse, Steckverbinder, Ladegeräte
**Besonderheit:** De-facto-Standard für Landstrom-Stecker (30A/50A)

#### Landstrom-Steckverbinder

| Typ | Strom | Spannung | Norm | Farbe |
|-----|-------|---------|------|-------|
| 16A CEE | 16A | 230V 1P | IEC 60309 | Blau |
| 32A CEE | 32A | 230V 1P | IEC 60309 | Blau |
| 63A CEE | 63A | 230V 1P | IEC 60309 | Blau |
| 32A CEE 3P | 32A | 400V 3P | IEC 60309 | Rot |
| 125A CEE 3P | 125A | 400V 3P | IEC 60309 | Rot |
| 30A NEMA L5-30 | 30A | 120V | NEMA | — (US) |
| 50A NEMA SS2-50 | 50A | 120/240V | NEMA | — (US) |

#### Galvanische Isolatoren

| Modell | Strom | Funktion | Norm |
|--------|-------|----------|------|
| ProSafe 1 (30A) | 30A | Galvanischer Isolator | ABYC A-28 |
| ProSafe 2 (50A) | 50A | Galvanischer Isolator | ABYC A-28 |
| ProSafe FS30 | 30A | Isolator + Fehlstromwarnung | ABYC A-28 |

### 4.6 Hella Marine

**Herkunft:** Neuseeland (Teil der HELLA Gruppe, Deutschland)
**Spezialisierung:** Marine-LED-Beleuchtung, Positionslichter
**Besonderheit:** COLREG-zertifiziert, höchste optische Qualität

#### Positionslichter (COLREG/72)

| Modell | Typ | Sichtweite | Leistung | Besonderheit |
|--------|-----|-----------|---------|-------------|
| NaviLED PRO | Topp | 3 sm | 2,1W | Multivolt 9–33V |
| NaviLED PRO | Seite (rot/grün) | 2 sm | 1,2W | Multivolt 9–33V |
| NaviLED PRO | Heck | 2 sm | 0,8W | Multivolt 9–33V |
| NaviLED PRO | Dampfer (Topp+Heck) | 3 sm | 3,5W | Combo, ab 12m |
| NaviLED PRO | Dreifarben-Mast | 2 sm | 2,5W | Segelboot <20m |
| NaviLED PRO | Anker | 2 sm | 0,5W | 360° weiß |

#### Innenbeleuchtung

| Serie | Typ | Leistung | Lumen | Farbtemperatur |
|-------|-----|---------|-------|---------------|
| EuroLED 75 | Deckeneinbau | 4W | 350 lm | 3000K warm |
| EuroLED 150 | Deckeneinbau | 10W | 900 lm | 3000/5000K | 
| Warm White Strip | LED-Streifen | 4,8 W/m | 400 lm/m | 2700K |
| Sea Hawk R | Unterwasser | 6W | 520 lm | Blau/Weiß |

---

## 5. Hersteller-Datenbank

### 5.1 Victron Energy B.V.

| Feld | Wert |
|------|------|
| Sitz | Almere, Niederlande |
| Gründung | 1975 |
| Segment | Energiesysteme (Marine, Mobile, Off-Grid) |
| Zertifizierungen | CE, FCC, RCM, DNV-GL (ausgewählte Produkte) |
| Vertrieb | Weltweit über Fachhändler |
| Support | 5 Jahre Garantie (Standard), Community-Forum |
| Integration | VE.Direct, VE.Bus, VE.Can, NMEA 2000, Modbus TCP |
| AYDI-Relevanz | Batterie-Monitoring, Laderegler, Inverter — automatische Datenerfassung über VRM API |
| Stärke | Offene Protokolle, große Community, guter Support |
| Schwäche | Kunststoffgehäuse (nicht immer IP67), chinesische Fertigung (Qualitätsschwankung) |

### 5.2 Mastervolt (Navico Group)

| Feld | Wert |
|------|------|
| Sitz | Amsterdam, Niederlande |
| Gründung | 1991 |
| Segment | Premium-Bordnetz, Superyacht |
| Zertifizierungen | CE, DNV-GL, Lloyd's, BV, RINA |
| Vertrieb | Werftenstandardlieferant, Fachhandel |
| Support | 2 Jahre Garantie (erweiterbar), OEM-Support |
| Integration | MasterBus, CZone (CAN), NMEA 2000 |
| AYDI-Relevanz | CZone-Integration für automatische Kreisbeschreibung und Lasterfassung |
| Stärke | Klassifikation, DNV-Zulassung, vollintegriertes System |
| Schwäche | Proprietäres Ökosystem, hohe Preise, weniger DIY-freundlich |

### 5.3 Blue Sea Systems

| Feld | Wert |
|------|------|
| Sitz | Bellingham, WA, USA |
| Gründung | 1992 |
| Segment | Stromverteilung, Sicherungstechnik |
| Zertifizierungen | UL, ABYC, CE, ISO 8846 (ignition protected) |
| Vertrieb | Weltweit, stark in Nordamerika |
| Support | Lebenslange Garantie auf viele Produkte |
| Integration | ML-ACR analog, einfache Integration |
| AYDI-Relevanz | Standardkomponenten für Absicherung und Verteilung — Referenz für Dimensionierung |
| Stärke | Qualität, Garantie, breites Sortiment, ABYC-konform |
| Schwäche | Primär US-Markt (AWG-basiert), wenig digital/CAN |

### 5.4 BEP Marine (Navico Group)

| Feld | Wert |
|------|------|
| Sitz | Auckland, Neuseeland |
| Gründung | 1969 |
| Segment | Batterieschalter, Verteiler, Gasdetektoren |
| Zertifizierungen | CE, ISO 8846, ABYC, NMMA |
| Vertrieb | Weltweit, OEM-Zulieferer |
| Support | 2 Jahre Garantie |
| Integration | CZone-kompatibel (Navico-Gruppe) |
| AYDI-Relevanz | Batterieschalter-Dimensionierung, Absicherungsplanung |
| Stärke | Robuste mechanische Qualität, langjährige Erfahrung |
| Schwäche | Kleines Sortiment, wenig Innovation |

### 5.5 Marinco (Power Products LLC)

| Feld | Wert |
|------|------|
| Sitz | Menomonee Falls, WI, USA |
| Gründung | 1975 |
| Segment | Landstromanschluss, Steckverbinder |
| Zertifizierungen | UL, CE, ABYC, IEC 60309 |
| Vertrieb | Weltweit, OEM + Aftermarket |
| Support | Standardgarantie |
| Integration | Passive Komponenten, kein Netzwerk |
| AYDI-Relevanz | Landstrom-Dimensionierung, Anschlusstyp-Bestimmung |
| Stärke | De-facto-Standard, breite Verfügbarkeit |
| Schwäche | Primär passive Komponenten |

### 5.6 Hella Marine (HELLA GmbH & Co. KGaA)

| Feld | Wert |
|------|------|
| Sitz | Auckland, Neuseeland (Mutter: Lippstadt, Deutschland) |
| Gründung | Marine-Division seit 1990er |
| Segment | Marine-LED-Beleuchtung, Positionslichter |
| Zertifizierungen | COLREG 72, CE, ABYC, USCG |
| Vertrieb | Weltweit, OEM + Fachhandel |
| Support | 5 Jahre Garantie |
| Integration | Multivolt 9–33V, einfache 2-Draht-Installation |
| AYDI-Relevanz | Beleuchtungsplanung, COLREG-Compliance, Energiebilanz (geringe LED-Lasten) |
| Stärke | Optische Qualität, COLREG-Zertifizierung, Langlebigkeit |
| Schwäche | Premium-Preis, kleines Nicht-Beleuchtungssortiment |

### 5.7 Sterling Power Products

| Feld | Wert |
|------|------|
| Sitz | Berkshire, Großbritannien |
| Gründung | 1991 |
| Segment | Ladegeräte, DC/DC-Konverter, Batteriesplitter |
| Zertifizierungen | CE, RoHS |
| Vertrieb | Europa, Australien |
| Support | 2 Jahre Garantie |
| Integration | Analoge Steuerung, einige mit Remote-Panel |
| AYDI-Relevanz | DC/DC-Konverter-Auswahl, Lichtmaschinenregler |
| Stärke | Preis-Leistung, kompakte Bauform |
| Schwäche | Weniger bekannt, eingeschränkter Support außerhalb UK |

### 5.8 Whisper Power

| Feld | Wert |
|------|------|
| Sitz | Drachten, Niederlande |
| Gründung | 2004 |
| Segment | Generatoren, Inverter, Lithium-Systeme |
| Zertifizierungen | CE, EMC, DNV-GL (Generatoren) |
| Vertrieb | Europa, wachsend international |
| Support | OEM-Partnerschaften, Werftensupport |
| Integration | CAN-Bus, proprietäres Monitoring |
| AYDI-Relevanz | Generator-Dimensionierung, Hybrid-Systeme |
| Stärke | Leise Generatoren, integrierte Systemlösungen |
| Schwäche | Kleiner Hersteller, eingeschränktes Händlernetz |

---

## 6. Fehlerbild-Atlas

### 6.1 Fehlerbild: Übermäßiger Spannungsabfall

| Feld | Beschreibung |
|------|-------------|
| **Symptom** | Verbraucher funktionieren nur eingeschränkt (Lichter dimmen, Pumpen langsam, Autopilot-Fehler) |
| **Visuelle Indikatoren** | Warme/heiße Kabel, verfärbte Klemmen, Verbraucher flackern unter Last |
| **Messbare Abweichung** | >3% Spannungsabfall bei kritischen / >10% bei unkritischen Verbrauchern |
| **Ursachen** | Unterdimensionierter Querschnitt, zu lange Leitungen, korrodierte Verbindungen, lose Klemmen |
| **Risikoklasse** | MITTEL (Funktionsverlust) bis HOCH (bei Navigation/Sicherheit) |
| **Prüfmethode** | Spannung am Verbraucher unter Last messen, gleichzeitig Spannung an Batterie. Differenz = Gesamtabfall. Systematisch halbieren (Mitte der Leitung messen) um Problemstelle einzugrenzen |
| **Sofortmaßnahme** | Alle Verbindungen reinigen und nachziehen, Übergangswiderstand messen |
| **Dauerhafte Lösung** | Kabelquerschnitt erhöhen, Leitungsweg verkürzen, Verbindungen erneuern |
| **AYDI-Score-Impact** | Elektrik-Score −15 bis −30 je nach Schwere |
| **Konfidenz** | measured (bei Messung) / visual_medium (bei Sichtprüfung Verfärbung) |

### 6.2 Fehlerbild: Korrosion an Klemmen und Verbindungen

| Feld | Beschreibung |
|------|-------------|
| **Symptom** | Grüne/weiße Ablagerungen an Klemmen, intermittierende Kontaktprobleme |
| **Visuelle Indikatoren** | Grünspan (Kupferkorrosion), weißer Belag (Aluminium/Zink-Korrosion), aufgequollene Isolation |
| **Messbare Abweichung** | Übergangswiderstand >1 mΩ (normal: <0,1 mΩ bei Crimpverbindung) |
| **Ursachen** | Feuchtigkeit + Salz, ungeeignetes Material (blankes Kupfer statt verzinnt), fehlende Abdichtung, galvanische Korrosion (verschiedene Metalle) |
| **Risikoklasse** | MITTEL bis HOCH (schleichende Verschlechterung bis Totalausfall) |
| **Prüfmethode** | Sichtprüfung, Widerstandsmessung an jeder Verbindung, Thermografie unter Last |
| **Sofortmaßnahme** | Korrosion mechanisch entfernen (Schleifvlies, nicht Schleifpapier), Kontaktspray, provisorische Abdichtung |
| **Dauerhafte Lösung** | Verzinnte Kabelschuhe verwenden, Schrumpfschlauch mit Kleber, Kontaktfett (Vaseline/Lithiumfett), Verbindungen über Bilge-Stand verlegen |
| **AYDI-Score-Impact** | Material-Score −20, Elektrik-Score −15 |
| **Konfidenz** | visual_high (grünliche Verfärbung eindeutig erkennbar) |

### 6.3 Fehlerbild: Massefehler (Ground Fault)

| Feld | Beschreibung |
|------|-------------|
| **Symptom** | Mehrere Verbraucher gleichzeitig betroffen, Sicherung am Massepol löst nicht aus, Kriechströme messbar |
| **Visuelle Indikatoren** | Korrosion an Borddurchlässen, erhöhter Zinkanoden-Verbrauch, Elektrolyseschäden am Unterwasserschiff |
| **Messbare Abweichung** | Strom zwischen Bordmasse und Seewasser >50 mA (Grenzwert: 0 mA im Idealfall) |
| **Ursachen** | Beschädigte Isolation, Feuchtigkeit in Kabelkanal, falsches Massekonzept (DC-Masse mit Bonding verbunden), defekter Landstrom-Schutzleiter |
| **Risikoklasse** | HOCH (Elektrolyse zerstört Unterwasserteile, Personengefährdung im Wasser) |
| **Prüfmethode** | Isolationsmessung (Megger) aller Kreise gegen Schiffsmasse, Kriechstrom-Messung mit Zangenamperemeter am Landstrom-Schutzleiter |
| **Sofortmaßnahme** | Landstrom trennen, alle Kreise einzeln prüfen, Fehlerstrom lokalisieren |
| **Dauerhafte Lösung** | Galvanischen Isolator installieren, Massekonzept überarbeiten, beschädigte Kabel ersetzen, Isolationsüberwachung (IMD) einbauen |
| **AYDI-Score-Impact** | Sicherheit-Score −40, Elektrik-Score −30 |
| **Konfidenz** | measured (bei Isolationsmessung) |

### 6.4 Fehlerbild: Kurzschluss

| Feld | Beschreibung |
|------|-------------|
| **Symptom** | Sicherung löst sofort aus bei Einschalten, Rauchentwicklung, verschmorte Isolation |
| **Visuelle Indikatoren** | Geschmolzene Sicherung (durchgebrannt), verfärbte/geschmolzene Kabelisolation, Brandspuren |
| **Messbare Abweichung** | Widerstand <1Ω zwischen Plus und Minus eines Kreises (bei abgeklemmtem Verbraucher: unendlich erwartet) |
| **Ursachen** | Scheuerstellen (Kabel an scharfer Kante), gequetschte Kabel (unter Bodenplatte), Nagetierfrass, Feuchtigkeit in Steckverbinder, defekter Verbraucher |
| **Risikoklasse** | KRITISCH (Brandgefahr!) |
| **Prüfmethode** | Widerstandsmessung im spannungslosen Zustand, systematisches Halbieren der Leitung, Sichtprüfung gesamter Kabelweg |
| **Sofortmaßnahme** | Kreis abschalten (Sicherung NICHT überbrücken!), Kabelweg visuell inspizieren |
| **Dauerhafte Lösung** | Defekte Stelle identifizieren und erneuern, Kabelschutz (Wellrohr, Kantenschutz) anbringen, Kabelverlegung optimieren |
| **AYDI-Score-Impact** | Sicherheit-Score −50, Compliance-Score −30 |
| **Konfidenz** | measured (Widerstandsmessung) / visual_high (Brandspuren) |

### 6.5 Fehlerbild: Überlastung / Thermische Schädigung

| Feld | Beschreibung |
|------|-------------|
| **Symptom** | Sicherung löst nach einiger Zeit aus (nicht sofort wie Kurzschluss), Kabel spürbar warm, Isolation weich/verfärbt |
| **Visuelle Indikatoren** | Bräunlich verfärbte Isolation, verformte Klemmengehäuse, geschmolzene Kabelbinder neben dem Kabel |
| **Messbare Abweichung** | Kabeltemperatur >60°C unter Last, Strom >80% der Sicherung über längere Zeit |
| **Ursachen** | Unterdimensionierte Sicherung (zu hoch), unterdimensionierter Kabelquerschnitt, zu viele Verbraucher auf einem Kreis, keine Berücksichtigung von Derating (Bündel, Temperatur) |
| **Risikoklasse** | HOCH (Isolation degradiert → Kurzschluss → Brand) |
| **Prüfmethode** | Thermografie oder Temperaturmessung unter Volllast, Strommessung vs. Kabel-Nennstrom, Derating-Faktoren prüfen |
| **Sofortmaßnahme** | Last reduzieren (Verbraucher umverteilen), Sicherungswert prüfen |
| **Dauerhafte Lösung** | Kabelquerschnitt erhöhen, Last aufteilen, Sicherung auf korrekten Wert ändern (schützt Kabel, NICHT Verbraucher!) |
| **AYDI-Score-Impact** | Sicherheit-Score −30, Elektrik-Score −25 |
| **Konfidenz** | visual_medium (Verfärbung), measured (Temperaturmessung) |

### 6.6 Fehlerbild: Kriechstrom / Parasitäre Entladung

| Feld | Beschreibung |
|------|-------------|
| **Symptom** | Batterie entladen nach Standzeit (Tage/Wochen), kein offensichtlicher Verbraucher aktiv |
| **Visuelle Indikatoren** | Keine visuellen Anzeichen (heimtückisch!) |
| **Messbare Abweichung** | Ruhestrom >50 mA (Ziel: <20 mA), oft 200–500 mA durch versteckte Verbraucher |
| **Ursachen** | Standby-Verbraucher (Ladegerät, CO-Melder, Uhr), vergessener Schalter, Feuchtigkeitsbrücke auf Leiterplatte, defekte Diode in Lichtmaschine |
| **Risikoklasse** | NIEDRIG (kein Sicherheitsrisiko) bis MITTEL (Batterieschädigung durch Tiefentladung) |
| **Prüfmethode** | Zangenamperemeter am Batteriekabel (DC-Modus!), systematisches Abklemmen von Sicherungen zur Eingrenzung |
| **Sofortmaßnahme** | Batterie-Hauptschalter öffnen bei Nichtbenutzung |
| **Dauerhafte Lösung** | Kriechstrom-Quelle identifizieren und eliminieren, Stand-by-Verbraucher über Hauptschalter schaltbar machen |
| **AYDI-Score-Impact** | Elektrik-Score −10, Service-Score Warnung |
| **Konfidenz** | measured (Strommessung) |

### 6.7 Fehlerbild: EMV-Störung (Elektromagnetische Verträglichkeit)

| Feld | Beschreibung |
|------|-------------|
| **Symptom** | Störgeräusche im UKW-Funk, Kartenplotter zeigt Artefakte, AIS-Empfang gestört, Autopilot-Fehler bei Motor-Drehzahländerung |
| **Visuelle Indikatoren** | Fehlende Schirmung an Kabeln, unverdrillte Signalleitungen parallel zu Leistungskabeln |
| **Messbare Abweichung** | Störpegel im Funkbereich >CISPR 25 Grenzwerte |
| **Ursachen** | LED-Treiber ohne EMV-Filter, PWM-Laderegler, Schaltnetzteil-Inverter, fehlende Kabeltrennung (Signal/Leistung), fehlende Ferritkerne |
| **Risikoklasse** | MITTEL (Funktionseinschränkung Navigation/Kommunikation) |
| **Prüfmethode** | UKW auf leerer Frequenz, Motor/Verbraucher einzeln ein-/ausschalten, Störquelle identifizieren |
| **Sofortmaßnahme** | Störquelle abschalten oder Ferritkern auf Versorgungsleitung |
| **Dauerhafte Lösung** | EMV-gefiltertes Gerät verwenden, Kabelführung Signal/Leistung trennen (min. 50mm Abstand), Schirmung einseitig erden, Ferritkerne an Störquelle |
| **AYDI-Score-Impact** | Elektrik-Score −15, Compliance-Score −10 (EMV-Norm) |
| **Konfidenz** | measured (mit Spektrumanalysator) / estimated (Sichtprüfung Kabelführung) |

### 6.8 Fehlerbild: Lichtmaschinen-Defekt

| Feld | Beschreibung |
|------|-------------|
| **Symptom** | Batterie lädt nicht bei Motorlauf, Ladekontrollleuchte an/aus, Spannung bei Motor AN gleich wie bei Motor AUS |
| **Visuelle Indikatoren** | Verschlissener Keilriemen (Risse, Glasur), heiße Lichtmaschine, verbrannter Geruch |
| **Messbare Abweichung** | Keine Spannungserhöhung bei Motordrehzahl >1500 rpm (erwartet: +2–3V über Ruhespannung) |
| **Ursachen** | Kohlen verschlissen, Regler defekt, Diodenplatte defekt (eine Phase aus), Keilriemen rutscht, Erregerkabel unterbrochen |
| **Risikoklasse** | MITTEL (keine Ladung → irgendwann Batterieausfall) |
| **Prüfmethode** | Ladespannung bei 1500 rpm messen (Soll: 14,2–14,8V bei 12V / 28,4–29,6V bei 24V), Ripple messen (>0,5V AC = Diode defekt), Keilriemen-Schlupf prüfen |
| **Sofortmaßnahme** | Keilriemen spannen/erneuern, Verbindungen prüfen |
| **Dauerhafte Lösung** | Lichtmaschine revidieren (Kohlen, Lager, Dioden), externen Regler nachrüsten, Hochleistungs-LiMa einbauen |
| **AYDI-Score-Impact** | Elektrik-Score −20, Zuverlässigkeit −15 |
| **Konfidenz** | measured (Spannungsmessung) |

### 6.9 Fehlerbild: Batterie-Sulfatierung (Blei)

| Feld | Beschreibung |
|------|-------------|
| **Symptom** | Kapazitätsverlust, schnelle Ladung (akzeptiert keinen Strom), schnelle Entladung |
| **Visuelle Indikatoren** | Weiße Kristalle auf Platten (bei offener Batterie), aufgeblähtes Gehäuse (fortgeschritten) |
| **Messbare Abweichung** | Innenwiderstand >50% über Neuwertwert, Kapazitätstest <60% Nennkapazität |
| **Ursachen** | Chronische Unterladung, Tiefentladung, Standzeit im entladenen Zustand, zu niedrige Ladespannung (nie Gasungsphase erreicht) |
| **Risikoklasse** | NIEDRIG (Funktionsverlust, kein Sicherheitsrisiko bei intaktem Gehäuse) |
| **Prüfmethode** | Kapazitätstest (Entladung mit C/20 bis 10,5V/Zelle), Innenwiderstandsmessung, Spezifisches Gewicht (offene Batterie) |
| **Sofortmaßnahme** | Ausgleichsladung (Equalization) mit erhöhter Spannung (nur offene Nassbatterie!) |
| **Dauerhafte Lösung** | Batterie ersetzen, Ladeprofil optimieren (IUoU), regelmäßige Vollladung sicherstellen, bei Langzeit-Nichtnutzung: Erhaltungsladung |
| **AYDI-Score-Impact** | Elektrik-Score −15, Kosten-Warnung (Ersatz nötig) |
| **Konfidenz** | measured (Kapazitätstest) |

### 6.10 Fehlerbild: Batteriezellen-Unbalance (Lithium)

| Feld | Beschreibung |
|------|-------------|
| **Symptom** | BMS schaltet vorzeitig ab (bei scheinbar nicht voller/leerer Batterie), reduzierte nutzbare Kapazität |
| **Visuelle Indikatoren** | BMS-Fehler-LED, Smartphone-App zeigt Zellenspannungsdifferenz |
| **Messbare Abweichung** | Zellenspannungsdifferenz >50 mV (Soll: <20 mV) |
| **Ursachen** | Zellen unterschiedlicher Alterung, Temperaturgradient im Pack, defektes Balancing im BMS, eine schwache Zelle |
| **Risikoklasse** | MITTEL (Kapazitätsverlust) bis HOCH (bei Überladung einzelner Zellen: Thermal Runaway) |
| **Prüfmethode** | Einzelzellen-Spannung über BMS auslesen, Top-Balancing durchführen (volle Ladung, lange Absorptionsphase) |
| **Sofortmaßnahme** | Top-Balancing: Batterie vollständig laden und 4–8h auf Absorptionsspannung halten |
| **Dauerhafte Lösung** | Defekte Zelle identifizieren und ersetzen, BMS-Balancing-Funktion prüfen, Temperaturmanagement verbessern |
| **AYDI-Score-Impact** | Elektrik-Score −20, Sicherheit-Score −15 (bei hoher Differenz) |
| **Konfidenz** | measured (BMS-Daten) |

### 6.11 Fehlerbild: Landstrom-Erdschluss / RCD-Auslösung

| Feld | Beschreibung |
|------|-------------|
| **Symptom** | FI-Schutzschalter löst wiederholt aus bei Landstromanschluss, teilweise erst nach Erwärmung |
| **Visuelle Indikatoren** | Feuchtigkeit im Stecker/Kupplung, Korrosion an AC-Klemmen, verfärbte Kabelisolation |
| **Messbare Abweichung** | Isolationswiderstand <1 MΩ (Soll: >2 MΩ gemäß IEC 60364) |
| **Ursachen** | Feuchtigkeit im Boiler-Anschluss, defekter Warmwasserboiler (Heizstab), nasse AC-Steckdosen im Cockpit, Kapazitiver Ableitstrom EMV-Filter (summiert bei vielen Geräten) |
| **Risikoklasse** | HOCH (Personenschutz, der RCD arbeitet korrekt — das Problem liegt wo anders) |
| **Prüfmethode** | Systematische Isolationsmessung aller AC-Kreise gegen PE, kapazitiven Ableitstrom aller angeschlossenen Geräte prüfen |
| **Sofortmaßnahme** | Einzelne AC-Kreise trennen bis RCD hält, Feuchtigkeitsquellen trocknen |
| **Dauerhafte Lösung** | Defekten Verbraucher ersetzen, AC-Installation regelmäßig auf Isolation prüfen, bei kapazitivem Problem: selektiven RCD (300 mA für Hauptleitung + 30 mA für Einzelkreise) |
| **AYDI-Score-Impact** | Sicherheit-Score −25, Compliance-Score −20 |
| **Konfidenz** | measured (Isolationsmessung) |

### 6.12 Fehlerbild: CAN-Bus-Kommunikationsfehler

| Feld | Beschreibung |
|------|-------------|
| **Symptom** | Geräte im NMEA-2000-Netzwerk zeitweise unsichtbar, Datenlücken, Fehlermeldungen auf Displays |
| **Visuelle Indikatoren** | Fehlende Terminierungswiderstände, T-Stücke mit Korrosion, Kabelknick |
| **Messbare Abweichung** | Bus-Spannung außerhalb 9–16V, Wellenwiderstand ≠120Ω (Terminierung), Error-Frames >1% |
| **Ursachen** | Fehlende/doppelte Terminierung (genau 2× 120Ω am Leitungsende!), zu langes Backbone (>100m), Stichleitungen >6m, defektes Gerät (Bus-Kurzschluss), Spannungsversorgung des Bus zu schwach |
| **Risikoklasse** | MITTEL (Datenverlust Navigation) |
| **Prüfmethode** | Terminierung messen (Bus-Ende: 60Ω zwischen CAN-H und CAN-L), Backbone-Länge prüfen, systematisch Geräte abklemmen |
| **Sofortmaßnahme** | Terminierungswiderstände prüfen, verdächtiges Gerät abklemmen |
| **Dauerhafte Lösung** | Netzwerktopologie korrigieren (Daisy-Chain, nicht Stern!), Stichleitungen kürzen, Backbone <100m, Versorgungsspannung stabilisieren |
| **AYDI-Score-Impact** | Elektrik-Score −15, Navigation-Score −20 |
| **Konfidenz** | measured (Oszilloskop-Messung Bus-Signale) |

---

## 7. Troubleshooting-Entscheidungsbäume

### 7.1 Entscheidungsbaum: Batterie lädt nicht

```
START: Batterie lädt nicht bei Motorlauf
│
├─ Ladekontrollleuchte AUS bei Motor AN?
│   ├─ JA → Lichtmaschine produziert KEINEN Strom
│   │   ├─ Keilriemen intakt und gespannt?
│   │   │   ├─ NEIN → Keilriemen ersetzen/spannen
│   │   │   └─ JA → Erregerspannung an LiMa-Klemme D+ messen
│   │   │       ├─ 0V → Erregerstromkreis unterbrochen
│   │   │       │   ├─ Sicherung Erreger OK?
│   │   │       │   │   ├─ NEIN → Sicherung ersetzen, Ursache suchen
│   │   │       │   │   └─ JA → Kabelbruch oder Regler defekt
│   │   │       │   └─ Regler/Kohlen prüfen lassen
│   │   │       └─ Spannung vorhanden → Lichtmaschine intern defekt
│   │   │           └─ Werkstatt: Diodenplatte, Stator, Rotor prüfen
│   │   │
│   └─ NEIN (Leuchte AN bei Motor AN) → LiMa erregt, aber Problem:
│       ├─ Spannung an LiMa B+ messen (bei 2000 rpm)
│       │   ├─ Korrekte Ladespannung (14,2-14,8V / 28,4-29,6V)?
│       │   │   ├─ JA → LiMa OK! Problem liegt zwischen LiMa und Batterie
│       │   │   │   ├─ Spannungsabfall LiMa → Batterie messen
│       │   │   │   │   ├─ >0,5V → Kabel/Verbindung defekt
│       │   │   │   │   └─ <0,5V → Batterie-Trennrelais prüfen
│       │   │   │   │       ├─ Relais schaltet? (Klick hörbar)
│       │   │   │   │       │   ├─ NEIN → Relais-Versorgung/Steuerung prüfen
│       │   │   │   │       │   └─ JA → Kontakte verschlissen → ersetzen
│       │   │   │   │       └─ Cyrix/VSR: Spannungsschwelle korrekt?
│       │   │   └─ NEIN (zu niedrig) → Regler-Problem
│       │   │       ├─ Externer Regler vorhanden?
│       │   │       │   ├─ JA → Regler-Einstellung prüfen
│       │   │       │   └─ NEIN → Interner Regler defekt → Austausch
│       │   │       └─ Alternativ: Masseanschluss LiMa-Gehäuse prüfen
│       │   └─ Zu hoch (>15,5V / >31V) → GEFAHR!
│       │       └─ Regler defekt → Motor SOFORT abstellen!
│       │           └─ Batterie auf Überladung prüfen (Gasung, Erwärmung)
│
└─ ERGEBNIS: Fehlerquelle identifiziert → Reparatur planen
```

### 7.2 Entscheidungsbaum: Sicherung löst wiederholt aus

```
START: Sicherung löst wiederholt aus
│
├─ Wann löst die Sicherung aus?
│   ├─ SOFORT bei Einschalten → Kurzschluss
│   │   ├─ Verbraucher abklemmen, Sicherung erneut einsetzen
│   │   │   ├─ Sicherung hält OHNE Verbraucher?
│   │   │   │   ├─ JA → Kurzschluss IM VERBRAUCHER
│   │   │   │   │   └─ Verbraucher extern prüfen / ersetzen
│   │   │   │   └─ NEIN → Kurzschluss IN DER LEITUNG
│   │   │   │       ├─ Widerstandsmessung: Plus gegen Masse
│   │   │   │       │   ├─ <1Ω → Kurzer bestätigt
│   │   │   │       │   │   ├─ Kabelweg systematisch prüfen
│   │   │   │       │   │   ├─ Scheuerstellen an Schotten/Kanten
│   │   │   │       │   │   ├─ Steckverbinder auf Feuchtigkeit
│   │   │   │       │   │   └─ Halbierungsmethode zur Lokalisierung
│   │   │   │       │   └─ >100Ω → Intermittierender Fehler
│   │   │   │       │       └─ Kabel bei Vibration/Bewegung bewegen
│   │   │   │       │           → Fehler provozieren
│   │   │   │       └─ Isolation visuell prüfen (gesamter Weg)
│   │   │   │
│   ├─ NACH EINIGER ZEIT (Minuten) → Überlast
│   │   ├─ Strom im Betrieb messen (Zangenamperemeter)
│   │   │   ├─ Strom > 80% Sicherungswert?
│   │   │   │   ├─ JA → Überlast bestätigt
│   │   │   │   │   ├─ Sicherungswert korrekt für Kabelquerschnitt?
│   │   │   │   │   │   ├─ NEIN → Sicherung anpassen (Kabelschutz!)
│   │   │   │   │   │   └─ JA → Last zu hoch für diesen Kreis
│   │   │   │   │   │       ├─ Verbraucher auf 2 Kreise aufteilen
│   │   │   │   │   │       └─ ODER: Kabelquerschnitt erhöhen
│   │   │   │   └─ NEIN → Thermisches Problem
│   │   │   │       ├─ Kabeltemperatur messen (IR-Thermometer)
│   │   │   │       ├─ Bündelverlegung? → Derating berechnen
│   │   │   │       └─ Umgebungstemperatur am Sicherungshalter?
│   │   │   │           └─ >50°C → Sicherung kann bei Nennstrom auslösen!
│   │   │   │
│   └─ ZUFÄLLIG / INTERMITTIEREND → Wackelkontakt oder Vibration
│       ├─ Lose Verbindung im Kreis? (nachziehen, alle Klemmen!)
│       ├─ Vibration am Motor? (Kabel fixieren)
│       └─ Feuchtigkeit? (Wetter-/Seegangsabhängig?)
│
└─ ERGEBNIS: Ursache → Maßnahme
```

### 7.3 Entscheidungsbaum: Gesamtsystem spannungslos

```
START: Kein Strom an Bord (Totalausfall)
│
├─ Batterie-Hauptschalter ON?
│   ├─ NEIN → Einschalten. Problem gelöst?
│   │   ├─ JA → Bedienfehler (Hinweis an Crew)
│   │   └─ NEIN → Schalter defekt? Brücken zum Test (Vorsicht!)
│   │
│   └─ JA → Batteriespannung direkt an Batteriepolen messen
│       ├─ 0V → Batterie komplett tot oder abgeklemmt
│       │   ├─ Polklemmen fest?
│       │   │   ├─ NEIN → Anziehen, Korrosion entfernen
│       │   │   └─ JA → Batterie tiefentladen oder defekt
│       │   │       ├─ Ladegerät direkt an Batterie anschließen
│       │   │       │   ├─ Nimmt Ladung an? → Aufladen, Kapazität testen
│       │   │       │   └─ Kein Ladestrom → Batterie defekt (Zellschluss)
│       │   │       └─ Bei LiFePO4: BMS hat abgeschaltet
│       │   │           └─ BMS-Reset prüfen (je nach Hersteller)
│       │   │
│       ├─ Korrekte Spannung vorhanden (>12V / >24V)
│       │   ├─ Spannung am Hauptschalter-Ausgang messen
│       │   │   ├─ 0V → Hauptschalter defekt oder Hauptsicherung
│       │   │   │   ├─ Hauptsicherung (ANL/MRBF) prüfen
│       │   │   │   │   ├─ Durchgebrannt → Ersetzen + Ursache suchen!
│       │   │   │   │   └─ OK → Schalter intern defekt
│       │   │   │   └─ Schalter brücken zum Test → Schalter ersetzen
│       │   │   │
│       │   │   └─ Spannung OK → Problem am Verteiler
│       │   │       ├─ Spannung am Verteilerbusbar messen
│       │   │       │   ├─ 0V → Leitung Hauptschalter→Verteiler prüfen
│       │   │       │   └─ OK → Einzelsicherungen am Verteiler prüfen
│       │   │       │       └─ Alle durchgebrannt? → Schwerer Fehler!
│       │   │       │           └─ NICHT alle wieder einsetzen!
│       │   │       │               → Kreise einzeln prüfen
│       │   │
│       └─ Niedrige Spannung (<10,5V / <21V) → Batterie entladen
│           ├─ Ursache: Kriechstrom? Verbraucher vergessen?
│           ├─ Sofort: Laden (wenn Quelle verfügbar)
│           └─ Prüfen: Warum entladen? (→ Baum 7.1)
│
└─ ERGEBNIS: Stromversorgung wiederhergestellt oder Fehler lokalisiert
```

### 7.4 Entscheidungsbaum: Inverter-Fehler

```
START: Inverter liefert kein 230V AC
│
├─ Inverter eingeschaltet? (LED/Display prüfen)
│   ├─ NEIN → Einschalten / Fernschalter prüfen
│   │   └─ Geht nicht an → DC-Versorgung prüfen
│   │       ├─ DC-Sicherung am Inverter OK?
│   │       ├─ Kabellänge und Querschnitt ausreichend?
│   │       └─ Batteriespannung unter Mindestspannung?
│   │           (Typisch: <10V bei 12V / <20V bei 24V = Unterspannungsabschaltung)
│   │
│   └─ JA, aber kein AC-Ausgang
│       ├─ Fehlermeldung auf Display?
│       │   ├─ "Overload" → Last zu hoch
│       │   │   ├─ Aktuelle Last prüfen (Zangenamperemeter AC)
│       │   │   ├─ Anlaufstrom des Verbrauchers zu hoch?
│       │   │   │   ├─ Klimakompressor, große Pumpe? → Softstarter
│       │   │   │   └─ Verbraucher einzeln zuschalten
│       │   │   └─ Inverter-Leistung reicht nicht → größeren wählen
│       │   │
│       │   ├─ "Low Battery" → Batterie entladen
│       │   │   └─ Batteriekapazität prüfen, laden
│       │   │
│       │   ├─ "High Temperature" → Überhitzung
│       │   │   ├─ Belüftung blockiert?
│       │   │   ├─ Umgebungstemperatur zu hoch?
│       │   │   └─ Lüfter des Inverters defekt?
│       │   │
│       │   ├─ "Short Circuit" → AC-seitiger Kurzschluss
│       │   │   ├─ Alle AC-Verbraucher trennen
│       │   │   ├─ Inverter neu starten
│       │   │   ├─ Verbraucher einzeln wieder anschließen
│       │   │   └─ Defekten Verbraucher identifizieren
│       │   │
│       │   └─ "Ground Fault" → Erdschluss AC-seitig
│       │       └─ AC-Isolationsmessung aller Kreise
│       │
│       └─ Keine Fehlermeldung, aber kein Ausgang
│           ├─ AC-Sicherung am Ausgang prüfen
│           ├─ Transfer-Switch in Position "Shore"?
│           │   └─ Auf "Inverter" umschalten
│           └─ Inverter intern defekt → Service
│
└─ ERGEBNIS: Inverter-Betrieb wiederhergestellt oder Reparatur nötig
```

### 7.5 Entscheidungsbaum: NMEA 2000 / CAN-Bus-Probleme

```
START: NMEA 2000 Gerät nicht im Netzwerk sichtbar
│
├─ Nur EIN Gerät betroffen oder ALLE?
│   ├─ ALLE Geräte ausgefallen → Bus-Problem
│   │   ├─ Versorgungsspannung am Backbone messen
│   │   │   ├─ 0V → Versorgung unterbrochen
│   │   │   │   ├─ Bus-Sicherung OK?
│   │   │   │   ├─ Versorgungskabel zum Backbone prüfen
│   │   │   │   └─ Power-T-Stück korrekt angeschlossen?
│   │   │   │
│   │   │   ├─ <9V → Unterspannung
│   │   │   │   ├─ Zu viele Geräte am Bus? (LEN > verfügbar)
│   │   │   │   ├─ Spannungsabfall auf Backbone?
│   │   │   │   └─ Zweiten Power-Knoten hinzufügen
│   │   │   │
│   │   │   └─ 9–16V → Spannung OK, Bus-Signal prüfen
│   │   │       ├─ Terminierung vorhanden? (2× 120Ω an den Enden)
│   │   │       │   ├─ Messung: 60Ω zwischen CAN-H und CAN-L
│   │   │       │   │   ├─ Unendlich → Keine Terminierung!
│   │   │       │   │   │   └─ Terminierungs-Widerstände einsetzen
│   │   │       │   │   ├─ 120Ω → Nur eine Terminierung
│   │   │       │   │   │   └─ Zweite am anderen Ende hinzufügen
│   │   │       │   │   ├─ 60Ω → Korrekt (2× parallel = 60Ω)
│   │   │       │   │   └─ <40Ω → Zu viele Terminierungen oder Kurzschluss
│   │   │       │   └─ T-Stücke auf Feuchtigkeit/Korrosion prüfen
│   │   │       └─ Backbone-Integrität prüfen (Durchgang CAN-H, CAN-L, Shield)
│   │   │
│   └─ NUR EIN Gerät → Geräte-spezifisch
│       ├─ Gerät bekommt Strom? (LED am Gerät)
│       │   ├─ NEIN → Versorgung am Drop-Kabel prüfen
│       │   │   ├─ T-Stück Kontakte korrodiert?
│       │   │   ├─ Drop-Kabel defekt? (Ersatz testen)
│       │   │   └─ Gerät selbst defekt (Eingangsschutz?)
│       │   │
│       │   └─ JA, Gerät hat Strom, kommuniziert aber nicht
│       │       ├─ Gerät korrekt konfiguriert? (Instanznummer, Device-ID)
│       │       ├─ Firmware-Update nötig? (Kompatibilität)
│       │       ├─ Gerät am anderen T-Stück/Position testen
│       │       │   ├─ Funktioniert dort → Vorheriger Anschluss defekt
│       │       │   └─ Funktioniert nicht → Gerät defekt
│       │       └─ Drop-Kabel-Länge prüfen (<6m!)
│
└─ ERGEBNIS: Netzwerk wiederhergestellt
```

---

## 8. FAQ

### 8.1 Grundlagen

**F1: Ab welcher Bootsgröße lohnt sich der Umstieg auf 24V?**
Ab ca. 12m LOA oder wenn die installierte Leistung 2.000W übersteigt. Entscheidend sind nicht nur die aktuellen Verbraucher, sondern auch geplante Erweiterungen. Eine Fahrtenyacht mit Watermaker, Autopilot, elektrischer Winde und umfangreicher Elektronik profitiert deutlich von 24V durch geringere Kabelquerschnitte und bessere Effizienz.

**F2: Kann ich ein 12V-System nachträglich auf 24V umrüsten?**
Technisch ja, aber aufwändig. Alle Verbraucher müssen 24V-tauglich sein oder über DC/DC-Konverter versorgt werden. Empfehlung: Bei ohnehin anstehender Kompletterneuerung der Elektrik sinnvoll. Schrittweise Umrüstung mit 24V-Haupt-Bus und 12V-Unterverteilung über Konverter ist der pragmatische Weg.

**F3: Was bedeutet "SELV" und warum ist das für Boote relevant?**
SELV = Safety Extra Low Voltage (Schutzkleinspannung). Spannungen unter 50V DC gelten als berührungssicher für trockene Bedingungen. Auf Booten (feuchte Umgebung) sind Spannungen bis 32V DC ohne zusätzlichen Berührungsschutz zulässig. Darüber (z.B. 48V-Systeme) sind zusätzliche Schutzmaßnahmen erforderlich.

**F4: Warum sind verzinnte Kabel auf Booten vorgeschrieben?**
Blankes Kupfer oxidiert im salzhaltigen Klima. Die Oxidschicht erhöht den Übergangswiderstand an Verbindungen. Verzinnte Litzen schützen vor Korrosion und gewährleisten langfristig niedrige Übergangswiderstände. ABYC und ISO verlangen verzinntes Kupfer für marine Installationen.

**F5: Was passiert bei Verpolung im Bordnetz?**
Die meisten modernen Elektronikgeräte haben einen Verpolungsschutz (Diode oder MOSFET). Allerdings: Einige Ladegeräte, Inverter und Motoren können sofort zerstört werden. Bleibatterien erzeugen Kurzschluss-Ströme bei Verpolung. IMMER Polarität vor Anschluss prüfen, IMMER mit Plus beginnen.

### 8.2 Dimensionierung

**F6: Wie dimensioniere ich die Hauptsicherung?**
Die Hauptsicherung schützt das Kabel von der Batterie zum Verteiler, NICHT die Summe der Verbraucher. Regel: Sicherungswert ≤ Kabel-Nennstrom. Beispiel: Kabel 35 mm² (Nennstrom 125A) → Hauptsicherung 100–125A. Die Sicherung muss innerhalb 180mm (7 Zoll) von der Batterie sitzen.

**F7: Wie viel Batteriekapazität brauche ich?**
Grundformel: Tagesverbrauch [Ah] / DoD × Sicherheitsfaktor. Beispiel: 150 Ah Tagesverbrauch bei LiFePO4 (80% DoD): 150 / 0,8 × 1,2 = 225 Ah Mindestkapazität. Der Sicherheitsfaktor (1,2–1,5) berücksichtigt Alterung und unvorhergesehenen Verbrauch.

**F8: Wie groß muss mein Inverter sein?**
Summe der gleichzeitig betriebenen AC-Verbraucher + Anlaufstrom des größten Verbrauchers. Beispiel: Wasserkocher 2000W + Laptop 60W + Licht 20W = 2080W → Inverter 2500W (Reserve). Achtung: Klimakompressor hat 3–5× Anlaufstrom!

**F9: Wie dimensioniere ich den Solarregler?**
MPPT-Regler: PV-Leistung / Batteriespannung × 1,1 = erforderlicher Ladestrom. PV-Leerlaufspannung × 1,1 = erforderliche max. Eingangsspannung. Beispiel: 800 Wp Solar, 24V-System → 800W / 24V × 1,1 = 37A → SmartSolar 150/45.

**F10: Wie wähle ich den richtigen DC/DC-Konverter?**
Summe aller 12V-Verbraucher (gleichzeitig) + 20% Reserve. Typisch für Fahrtenyacht: UKW (5A) + GPS/AIS (2A) + Instrumente (3A) + Beleuchtung (5A) = 15A → DC/DC-Konverter 24V→12V/20A.

### 8.3 Sicherheit

**F11: Warum löst mein FI-Schalter beim Einstecken des Landstroms aus?**
Häufigste Ursachen: 1) Feuchtigkeit in einer AC-Steckdose (besonders Cockpit), 2) Defekter Warmwasserboiler (Heizelement undicht), 3) Kumulierter kapazitiver Ableitstrom aller EMV-Filter (bei vielen Geräten). Systematisch: AC-Sicherungen einzeln ausschalten bis FI hält → fehlerhaften Kreis identifiziert.

**F12: Brauche ich einen galvanischen Isolator?**
JA, wenn Landstrom ohne Trenntransformator angeschlossen wird. Der Schutzleiter des Landstroms verbindet sonst alle Boote im Hafen galvanisch — das Boot mit dem "edleren" Metall wird zur Opferanode für alle anderen! Ein galvanischer Isolator blockiert DC-Kriechströme bei <1,2V und leitet nur AC-Fehlerströme.

**F13: Wie schütze ich die Elektrik vor Blitzschlag?**
Blitzschutz auf Yachten ist komplex und umstritten. Minimum: Ableiter vom Masttopp über dickste verfügbare Leitung (mind. 35 mm²) zur Erdungsplatte am Unterwasserschiff. Überspannungsableiter (Varistoren) an empfindlicher Elektronik. Alle Geräte mit gemeinsamer Bezugserde (Bonding-System).

**F14: Darf ich Kabel im Maschinenraum mit Kabelbindern befestigen?**
Ja, aber NUR UV- und ölbeständige Kabelbinder (schwarzes Nylon oder Edelstahlband). Standard-Kabelbinder werden spröde und brechen nach 2–3 Jahren. Empfehlung: Edelstahl-Kabelbinder oder Adel-Clamps (Gummierte P-Clips) auf Schienen verschraubt.

**F15: Wann muss ich eine Isolationsüberwachung (IMD) einbauen?**
Bei ungeerdeten DC-Systemen (IT-System) über 50V empfohlen, bei Systemen >120V DC vorgeschrieben. Für 12V/24V-Systeme nicht erforderlich, aber für Langfahrtboote mit LiFePO4 sinnvoll (frühzeitige Erkennung von Isolationsfehlern). Bei 48V-Systemen: dringend empfohlen.

### 8.4 Lithium-Batterien

**F16: Was muss ich bei der Umrüstung auf LiFePO4 beachten?**
1) BMS zwingend erforderlich, 2) Ladeprofile aller Ladequellen anpassen (14,2–14,6V bei 12V), 3) Temperaturschutz (<5°C kein Laden!), 4) Lichtmaschinen-Regler austauschen (LiFePO4 verträgt keinen Bulk-Ladestrom ohne Strombegrenzung), 5) Hauptschalter NICHT unter Last öffnen (BMS-Kontakte können verschweißen).

**F17: Können LiFePO4-Batterien explodieren?**
LiFePO4 ist die sicherste Lithium-Chemie. Thermal Runaway ist extrem unwahrscheinlich (Onset >270°C vs. ~150°C bei NMC). Das BMS schützt vor Über-/Unterspannung und Übertemperatur. Dennoch: Nur marine-zertifizierte LiFePO4 mit integriertem BMS verwenden (kein Eigenbau aus Zellen ohne professionelles BMS).

**F18: Wie lange halten LiFePO4-Batterien?**
Bei korrekter Behandlung: 3.000–5.000 Zyklen bei 80% DoD, oder 8–15 Jahre kalendarische Lebensdauer. Im Vergleich: AGM 400–600 Zyklen, Gel 500–800 Zyklen. Lebensdauer-Killer: Lagerung bei Extremtemperaturen, dauerhaftes Laden auf 100%, Tiefentladung unter BMS-Schwelle.

### 8.5 Solar und alternative Energie

**F19: Wie viel Solar-Leistung bekomme ich realistisch auf eine Yacht?**
Faustformel: Verfügbare Fläche [m²] × 170–200 W/m² (Modul-Effizienz) × 0,7 (Ausrichtung, Verschattung). Realistische Erträge: Mittelmeer Sommer: 5–6 kWh/kWp/Tag, Nordeuropa Sommer: 3–4 kWh/kWp/Tag, Tropen: 4–5 kWh/kWp/Tag. Praxis: 400 Wp liefern im Mittelmeer ~1.800–2.400 Wh/Tag.

**F20: MPPT vs. PWM-Solarregler — wann lohnt sich MPPT?**
MPPT lohnt sich IMMER bei: >100 Wp installiert, Module mit Vmp > 18V (60-Zeller), langen Kabelwegen (höhere Spannung = weniger Verlust), Teilverschattung. PWM nur akzeptabel bei: <100 Wp, 36-Zellen-Module direkt für 12V, sehr kurze Kabel. Mehrertrag MPPT: 15–30%.

### 8.6 Praxis und Wartung

**F21: Wie oft sollte ich die Bordelektrik prüfen lassen?**
Professionelle Prüfung alle 3–5 Jahre (Surveyor mit Isolationsmessgerät). Eigenerinspektion jährlich: Alle Verbindungen sichten, Batteriezustand messen, Korrosion prüfen, Sicherungen auf Verfärbung prüfen. Nach jedem schweren Wetter: Mastverkabelung kontrollieren.

**F22: Was ist der häufigste Elektrikfehler auf Booten?**
Korrodierte Verbindungen. Besonders an: Batteriepolen, Massepunkten, Mastfuß-Steckern, Bilgen-nahen Klemmen. Lösung: Regelmäßige Sichtprüfung, Kontaktfett, verzinnte Kabelschuhe, Schrumpfschlauch mit Kleber.

**F23: Darf ich automotive Sicherungen auf dem Boot verwenden?**
ATO/ATC Blade-Sicherungen sind marinezugelassen (Blue Sea Systems ST Blade Fuse Block). Standard-KFZ-Sicherungshalter aus dem Baumarkt NICHT — sie sind nicht vibrationsfest und nicht korrosionsgeschützt. ANL- und MRBF-Sicherungen für Hauptkreise sind marine-spezifisch.

**F24: Wie schütze ich die Elektrik bei Nichtbenutzung über den Winter?**
1) Hauptschalter AUS, 2) Landstrom-Ladegerät auf Erhaltungsladung (oder Batterie ausbauen und warm lagern), 3) Alle Stecker-Verbindungen mit Kontaktspray behandeln, 4) Feuchtigkeitsabsorber im Boot, 5) Belüftung sicherstellen (Schimmel!), 6) Bei LiFePO4: auf 50–60% SOC lagern.

**F25: Was kostet eine komplette Bordelektrik-Erneuerung?**
Grobe Richtwerte (Material + Arbeit): 8–10m Segelboot: 5.000–12.000€, 12–14m Fahrtenyacht: 15.000–35.000€, 16–20m Motoryacht: 40.000–80.000€. Hauptkostentreiber: Batterien (30–40%), Kabel und Arbeit (30%), Elektronik/Inverter (20–30%).

**F26: Wie messe ich den Zustand meiner Batteriebank?**
Vier Methoden: 1) Ruhespannungsmessung (nach 4h ohne Last/Ladung), 2) Kapazitätstest (definierte Entladung bis Endspannung), 3) Innenwiderstandsmessung (Vergleich mit Neuwert), 4) Peukert-korrigierte SOC-Messung über Shunt-Monitor (z.B. Victron BMV-712).

**F27: Warum dimmen meine LED-Lichter bei eingeschaltetem Kühlschrank?**
Spannungsabfall durch gemeinsame Leitung oder zu dünnen Querschnitt. Der Kompressor des Kühlschranks zieht beim Anlauf 3–5× Nennstrom (5–15A für wenige Sekunden). Lösung: Separate Leitungen für Kühlschrank und Beleuchtung ab Verteiler, Querschnitt des Kühlschrank-Kabels prüfen.

**F28: Ist ein Wechselrichter oder ein Generator wirtschaftlicher?**
Für gelegentlichen AC-Bedarf (<500 Wh/Tag): Inverter + größere Batterie. Für dauerhaften AC-Bedarf (>2 kWh/Tag): Generator (Klimaanlage, Kochen, Watermaker). Hybrid: Inverter für Normalbetrieb + Generator für Spitzenlasten. Dieselverbrauch Generator: 0,3–0,5 l/kWh.

### 8.7 Normen und Zulassung

**F29: Welche Norm gilt für mein Boot — ABYC oder ISO?**
EU/EWR: ISO 10133 (DC), ISO 13297 (AC). Nordamerika: ABYC E-11. Die Anforderungen sind sehr ähnlich, Hauptunterschied: AWG vs. mm²-Querschnitte, Farbcodes (ABYC: Gelb=Negativ vs. ISO: Schwarz/Blau=Negativ). Für CE-Kennzeichnung: ISO zwingend.

**F30: Muss die Bordelektrik von einem Sachverständigen abgenommen werden?**
Für CE-Zertifizierung bei Neubauten: ja (Benannte Stelle oder Modul A). Für Bestandsboote: keine gesetzliche Pflicht in DE. Empfohlen: Prüfung durch zertifizierten Marine-Elektriker nach Umbauten, besonders bei Lithium-Umrüstung und AC-Änderungen. Für Versicherung oft relevant!

---

## 9. Glossar

| Nr. | Begriff | Erklärung |
|-----|---------|-----------|
| 1 | **ABYC** | American Boat and Yacht Council — US-Normungsgremium für Bootstechnik |
| 2 | **AGM** | Absorbent Glass Mat — Blei-Säure-Batterie mit Glasvlies, wartungsfrei |
| 3 | **Ah** | Amperestunde — Einheit der Batteriekapazität |
| 4 | **ANL-Sicherung** | Bolzensicherung für hohe Ströme (35–750A), marine-Standard |
| 5 | **BMS** | Battery Management System — Überwachung und Schutz von Lithium-Batterien |
| 6 | **Bonding** | Schutzleiter-Verbindung aller metallischen Teile zur Potentialausgleich |
| 7 | **Bulk-Ladung** | Erste Ladephase: Konstantstrom bis ~80% SOC |
| 8 | **CAN-Bus** | Controller Area Network — serielles Kommunikationsprotokoll (NMEA 2000 basiert auf CAN 2.0B) |
| 9 | **COLREG** | Convention on the International Regulations for Preventing Collisions at Sea — Regelwerk für Positionslichter |
| 10 | **Crimp** | Kaltpressverbindung zwischen Kabel und Kabelschuh/Hülse |
| 11 | **Cyrix** | Victron-Produktname für spannungsgesteuerte Batterie-Trennrelais |
| 12 | **DC/DC-Konverter** | Gleichspannungswandler (z.B. 24V→12V) |
| 13 | **Derating** | Reduzierung der zulässigen Belastung bei erhöhter Temperatur oder Bündelverlegung |
| 14 | **DoD** | Depth of Discharge — Entladetiefe in Prozent der Nennkapazität |
| 15 | **EMV** | Elektromagnetische Verträglichkeit — Störaussendung und Störfestigkeit |
| 16 | **FI/RCD** | Fehlerstrom-Schutzschalter / Residual Current Device — Personenschutz bei AC |
| 17 | **Float** | Erhaltungsladung — niedrige Spannung zum Ausgleich der Selbstentladung |
| 18 | **Galvanischer Isolator** | Blockiert DC-Kriechströme über Landstrom-Schutzleiter (Diodenpaar) |
| 19 | **GFK** | Glasfaserverstärkter Kunststoff — Bootsbaumaterial (elektrisch isolierend) |
| 20 | **IMD** | Insulation Monitoring Device — Isolationsüberwachung für ungeerdete Systeme |
| 21 | **Inverter** | Wechselrichter — wandelt DC in AC (z.B. 24V DC → 230V AC) |
| 22 | **IP-Schutzart** | Ingress Protection — Schutz gegen Fremdkörper und Wasser (z.B. IP67) |
| 23 | **ISO 10133** | Norm für DC-Bordnetze auf Sportbooten |
| 24 | **ISO 13297** | Norm für AC-Installationen auf Sportbooten |
| 25 | **LEN** | Load Equivalency Number — Lastäquivalenz für NMEA 2000 Bus-Belastung |
| 26 | **LiFePO4** | Lithium-Eisenphosphat — sicherste Lithium-Batterie-Chemie für Marine |
| 27 | **Lichtmaschine (LiMa)** | Generator am Dieselmotor, typisch 80–200A |
| 28 | **MPPT** | Maximum Power Point Tracking — optimiert Solarertrag durch Impedanzanpassung |
| 29 | **MRBF-Sicherung** | Marine Rated Battery Fuse — kompakte Bolzensicherung für Batteriepol |
| 30 | **Megger** | Isolationsmessgerät (misst mit hoher Prüfspannung) |
| 31 | **NMEA 2000** | National Marine Electronics Association — Standard für Marinedaten-Netzwerk |
| 32 | **Peukert-Effekt** | Kapazitätsreduktion von Bleibatterien bei hohen Entladeströmen |
| 33 | **SELV** | Safety Extra Low Voltage — Berührungssichere Kleinspannung (<50V DC) |
| 34 | **Shunt** | Präzisionswiderstand zur Strommessung (Spannungsabfall proportional zu Strom) |
| 35 | **SOC** | State of Charge — Ladezustand der Batterie in Prozent |
| 36 | **Spannungsabfall** | Spannungsverlust über Kabel und Verbindungen (U = I × R) |
| 37 | **Trennrelais** | Automatisches Relais zur Batterietrennung (VSR / ACR) |
| 38 | **USV** | Unterbrechungsfreie Stromversorgung — überbrückt Netzausfall |
| 39 | **VE.Direct** | Victron-Kommunikationsprotokoll (seriell, proprietär) |
| 40 | **VSR** | Voltage Sensitive Relay — spannungsgesteuertes Trennrelais |
| 41 | **Wellrohr** | Flexibles Schutzrohr für Kabelführung |
| 42 | **Zangenamperemeter** | Strommessung ohne Leitungsauftrennung (Hall-Sensor) |
| 43 | **Zinkanode** | Opferanode zum Schutz edlerer Metalle vor galvanischer Korrosion |
| 44 | **Absorption** | Zweite Ladephase: Konstantspannung mit abnehmenden Strom |

---

## 10. Schnell-Referenz

### 10.1 Spannungsabfall-Schnelltabelle 12V-System (3% = 0,36V max.)

| Strom [A] | 2m | 4m | 6m | 8m | 10m | 12m | 15m |
|-----------|-----|-----|-----|-----|------|------|------|
| 5A | 0,75 | 1,0 | 1,5 | 1,5 | 2,5 | 2,5 | 2,5 |
| 10A | 1,5 | 2,5 | 2,5 | 4,0 | 4,0 | 6,0 | 6,0 |
| 15A | 2,5 | 2,5 | 4,0 | 6,0 | 6,0 | 6,0 | 10 |
| 20A | 2,5 | 4,0 | 6,0 | 6,0 | 10 | 10 | 10 |
| 30A | 4,0 | 6,0 | 10 | 10 | 16 | 16 | 16 |
| 50A | 6,0 | 10 | 16 | 16 | 25 | 25 | 35 |
| 80A | 10 | 16 | 25 | 35 | 35 | 50 | 50 |
| 100A | 16 | 25 | 35 | 35 | 50 | 50 | 70 |
| 150A | 16 | 35 | 50 | 50 | 70 | 70 | 95 |

*Werte in mm² — nächster verfügbarer Normquerschnitt, Leitungslänge = einfach (×2 intern berechnet)*

### 10.2 Spannungsabfall-Schnelltabelle 24V-System (3% = 0,72V max.)

| Strom [A] | 2m | 4m | 6m | 8m | 10m | 12m | 15m |
|-----------|-----|-----|-----|-----|------|------|------|
| 5A | 0,75 | 0,75 | 0,75 | 1,0 | 1,0 | 1,5 | 1,5 |
| 10A | 0,75 | 1,0 | 1,5 | 2,5 | 2,5 | 2,5 | 4,0 |
| 15A | 1,0 | 1,5 | 2,5 | 2,5 | 4,0 | 4,0 | 4,0 |
| 20A | 1,5 | 2,5 | 2,5 | 4,0 | 4,0 | 6,0 | 6,0 |
| 30A | 2,5 | 4,0 | 4,0 | 6,0 | 6,0 | 6,0 | 10 |
| 50A | 4,0 | 6,0 | 6,0 | 10 | 10 | 16 | 16 |
| 80A | 6,0 | 10 | 10 | 16 | 16 | 25 | 25 |
| 100A | 6,0 | 10 | 16 | 16 | 25 | 25 | 35 |
| 150A | 10 | 16 | 25 | 25 | 35 | 35 | 50 |

### 10.3 Batterie-Ruhespannung → SOC

#### Blei-Säure / AGM (12V-Zelle):

| SOC | 12V-System | 24V-System |
|-----|-----------|-----------|
| 100% | 12,73V | 25,46V |
| 90% | 12,62V | 25,24V |
| 80% | 12,50V | 25,00V |
| 70% | 12,37V | 24,74V |
| 60% | 12,24V | 24,48V |
| 50% | 12,10V | 24,20V |
| 40% | 11,96V | 23,92V |
| 30% | 11,81V | 23,62V |
| 20% | 11,66V | 23,32V |
| 10% | 11,51V | 23,02V |
| 0% (Endspannung) | 10,50V | 21,00V |

#### LiFePO4 (12V / 4S-Pack):

| SOC | 12V-System (4S) | 24V-System (8S) | Zellspannung |
|-----|----------------|----------------|-------------|
| 100% | 14,40V | 28,80V | 3,60V |
| 90% | 13,36V | 26,72V | 3,34V |
| 80% | 13,28V | 26,56V | 3,32V |
| 50% | 13,20V | 26,40V | 3,30V |
| 20% | 13,04V | 26,08V | 3,26V |
| 10% | 12,80V | 25,60V | 3,20V |
| 0% (BMS-Abschaltung) | 10,00V | 20,00V | 2,50V |

**Hinweis:** LiFePO4 hat eine extrem flache Entladekurve zwischen 20–80% SOC. Spannungsmessung allein ist daher ungenau — Coulomb-Counting (Shunt-Monitor) ist bei LiFePO4 zwingend empfohlen!

### 10.4 Sicherungszuordnung — Kabelschutz

| Kabelquerschnitt [mm²] | Maximale Sicherung [A] | Umgebung 30°C | Umgebung 50°C |
|------------------------|----------------------|---------------|---------------|
| 0,75 | 6A | 5A | 4A |
| 1,0 | 10A | 8A | 6A |
| 1,5 | 15A | 12A | 9A |
| 2,5 | 20A | 16A | 12A |
| 4,0 | 30A | 25A | 18A |
| 6,0 | 40A | 35A | 25A |
| 10 | 55A | 45A | 35A |
| 16 | 70A | 60A | 45A |
| 25 | 95A | 80A | 60A |
| 35 | 125A | 100A | 80A |
| 50 | 150A | 130A | 95A |
| 70 | 175A | 150A | 110A |
| 95 | 225A | 190A | 140A |

### 10.5 Farbcode Bordnetz

| Farbe | ABYC E-11 | ISO 10133 | Funktion |
|-------|-----------|-----------|----------|
| Rot | DC Positiv (Hauptleitung) | DC Positiv | +12V / +24V |
| Gelb | DC Negativ (Rückleiter) | — | Masse DC |
| Schwarz | — | DC Negativ (Rückleiter) | Masse DC (ISO) |
| Grün | Bonding/Erdung | Grün/Gelb | Schutzleiter |
| Braun | Zündungsgeschaltet | — | Geschaltetes Plus |
| Orange | — | — | Landstrom L1 (AC) |
| Blau | — | Neutral AC | AC Nullleiter |
| Weiß | — | — | Vielfältig (nicht festgelegt) |
| Violett | Zündung/Instrumente | — | Tachometer, Sensoren |
| Hellblau | Öldruckwarnung | — | — |
| Hellbraun/Tan | Wassertempwarnung | — | — |
| Pink | Tankgeber | — | — |

---

## 11. ANHANG A–H — Fallstudien

### ANHANG A: Fallstudie — Segelboot 10m, Komplette Bordnetz-Neuplanung (12V)

#### Ausgangssituation

**Boot:** Dufour 34 Classic, Baujahr 2005, 10,20m LOA
**Problem:** Originale Bordelektrik stark korrodiert, mehrfach improvisiert erweitert, kein Energiemanagement, Batterie immer leer.
**Ziel:** Komplette Neuinstallation für Wochenend-Segeln + 2 Wochen Sommerurlaub (Kroatien).

#### Bestandsaufnahme

- 2× Varta 95 Ah Nassbatterie (2018), eine defekt (Zellschluss)
- Lichtmaschine 55A original, kein externer Regler
- 10 Sicherungskreise, 4 nicht beschriftet, 2 nicht angeschlossen
- Kabel teilweise ohne Schrumpfschlauch, blanke Litzen an Klemmen
- Solar: 50W Panel mit PWM-Regler (Leitung 4m, Querschnitt 1,5mm²!)
- Beleuchtung: 3× Halogen (20W je!), rest unbekannt
- Gesamtzustand: MANGELHAFT, Sicherheitsrelevant!

#### Planung

**Verbraucherliste:**

| Verbraucher | Leistung [W] | Kreis | Priorität |
|-------------|-------------|-------|-----------|
| Navigationslichter (LED) | 15 | 1 | K1 |
| UKW-Funk DSC | 25 (Senden) / 3 (Standby) | 2 | K1 |
| GPS/Kartenplotter | 20 | 3 | K2 |
| AIS Transponder | 5 | 3 | K2 |
| Autopilot (Tiller) | 40 | 4 | K2 |
| Innenbeleuchtung LED | 30 (gesamt) | 5 | K4 |
| Cockpitbeleuchtung LED | 10 | 6 | K4 |
| Ankerwinde | 600 (kurzzeitig) | 7 | K3 |
| Kühlschrank (neue Kompressor-Box) | 45 | 8 | K4 |
| Wasserpumpe | 30 | 9 | K4 |
| USB-Ladebuchsen (4×) | 40 | 10 | K5 |
| Solar 200W (neu) | −200 (Ertrag) | — | Ladequelle |

**Energiebilanz Urlaubstag (Ankern):**

| Phase | Dauer [h] | Mittlere Last [W] | Verbrauch [Wh] |
|-------|-----------|-------------------|----------------|
| Nacht (22:00–06:00) | 8 | 60 | 480 |
| Morgen (06:00–10:00) | 4 | 90 | 360 |
| Tag (10:00–18:00) | 8 | 75 | 600 |
| Abend (18:00–22:00) | 4 | 100 | 400 |
| **Tagesverbrauch** | 24 | — | **1.840 Wh = 153 Ah** |

**Solar-Ertrag (Kroatien, Juli):** 200 Wp × 5,5h × 0,75 = 825 Wh = 69 Ah
**Defizit:** 153 − 69 = 84 Ah/Tag → Motor 1h/Tag (LiMa 90A mit externem Regler: ~70 Ah netto)

#### Gewählte Konfiguration

| Komponente | Produkt | Kosten |
|-----------|---------|--------|
| Service-Batterie | Victron LiFePO4 Smart 12V/200Ah | 1.400€ |
| Starter-Batterie | Varta Professional AGM 12V/95Ah | 180€ |
| Solarregler | Victron SmartSolar 100/20 | 150€ |
| Solarpanel | 2× 100W semiflexibel (Bimini) | 400€ |
| Lichtmaschine | Balmar AT-Series 12V/100A + MC-614 Regler | 900€ |
| Batterie-Monitor | Victron SmartShunt 500A | 120€ |
| Trennrelais | Victron Cyrix-Li-ct 12/24-230 | 95€ |
| Sicherungspanel | Blue Sea ST Blade 12-Circuit | 180€ |
| Hauptsicherung | Blue Sea MRBF 150A + Halter | 45€ |
| Landstrom-Ladegerät | Victron Blue Smart IP22 12/30 | 180€ |
| Kabel + Kleinmaterial | Diverse (verzinntes Marinekabel) | 500€ |
| Einbau (Fachbetrieb) | 20h × 85€ | 1.700€ |
| **Gesamt** | | **~5.850€** |

#### Ergebnis

- Autonomie beim Ankern: 3–4 Tage ohne Motorlauf (bei Sonnenschein)
- Gewichtsersparnis: ~25 kg (Blei → LiFePO4)
- AYDI-Elektrik-Score: 92/100 (vorher: 28/100)
- Compliance: ISO 10133 konform, ABYC E-11 entsprechend

---

### ANHANG B: Fallstudie — Fahrtenyacht 14m, Umrüstung 12V→24V

#### Ausgangssituation

**Boot:** Hallberg-Rassy 43 Mk II, Baujahr 2008, 13,60m LOA
**Problem:** 12V-System am Limit (2800W installiert), Spannungsabfall zu Ankerwinde am Bug kritisch, Kabelbrand-Incident an Masse-Bus-Bar (überhitzt).
**Ziel:** Umrüstung auf 24V für Langfahrt (Atlantik-Runde, 2–3 Jahre).

#### Herausforderungen

1. Viele 12V-Geräte (UKW, GPS, AIS, Autopilot-Pumpe) müssen weiterlaufen
2. Ankerwinde: aktuell 12V/100A = 1200W → bei 24V nur 50A nötig
3. Bestehende Kabelinfrastruktur teilweise nutzbar (Querschnitte reichen für 24V)
4. Budget: 20.000€ Material + Eigenleistung

#### Lösung: Hybrid 24V-Haupt / 12V-Unter

**Hauptbus 24V:**
- Service: Victron LiFePO4 Smart 24V/200Ah (2× 12V/200Ah in Serie, intern balanciert)
- Ankerwinde: Maxwell RC8-8 24V/500W (neuer Motor)
- Autopilot: Raymarine EV-200 24V
- Watermaker: Schenker Zen 30 24V
- Heizung: Webasto Airtop 2000ST 24V
- Inverter/Charger: Victron MultiPlus-II 24/3000/70

**12V-Bus (über DC/DC):**
- Victron Orion-Tr Smart 24/12-30 (360W Dauerleistung)
- UKW Icom IC-M510
- GPS/AIS: Vesper Cortex M1
- Instrumente: B&G Triton2
- Innenbeleuchtung (LED, Multivolt 10–30V bereits!)
- USB-Ladebuchsen

**Ergebnis:**
- Kabelquerschnitt Ankerwinde: von 70 mm² auf 25 mm² reduziert (−64%)
- Gewichtsersparnis Kabel gesamt: ~15 kg
- Spannungsabfall Winde: von 8,2% auf 2,8% (NORM KONFORM!)
- Gesamt-Autonomie: 4,5 Tage ankern (Tropen, mit Solar 1200W + Wind 300W)
- AYDI-Elektrik-Score: 95/100

---

### ANHANG C: Fallstudie — Motoryacht 18m, Generatorintegration und Lastmanagement

#### Ausgangssituation

**Boot:** Princess V58, Baujahr 2015, 18,10m LOA
**Problem:** Generator läuft 18h/Tag im Mittelmeer-Sommer (Klimaanlage). Kraftstoffverbrauch Generator: 4,5 l/h. Eigner möchte Betriebskosten senken.

#### Analyse

**Verbraucherprofil im Hafen (Sommer):**
- Klimaanlage: 3× 16.000 BTU = 4.500W Spitze, 2.800W Mittel
- Kühlschrank + Gefrierer: 300W
- Beleuchtung: 200W (Abend)
- Entertainment: 500W
- Diverse: 200W
- Gesamt: ~4.000W Mittel, 5.500W Spitze

**Aktuell:** Generator 8 kVA läuft durchgehend bei 50% Last (ineffizient!)

#### Lösung: Hybrid mit Lithium-Puffer

| Komponente | Spezifikation | Funktion |
|-----------|--------------|----------|
| Lithium-Bank | Mastervolt MLI Ultra 24/5000 (5 kWh) | Pufferspeicher |
| Inverter/Charger | Mastervolt Mass Combi Ultra 24/3500 × 2 (parallel) | 7 kW AC, 200A Laden |
| Landstrom-Upgrade | 63A CEE Anschluss + Mastervolt ChargeMaster 24/100 | Schnellladen |
| Power-Management | Mastervolt CZone + MasterBus | Automatische Laststeuerung |
| Solar (Flybridge) | 6× 200W = 1.200 Wp, Victron 150/45 | Solarertrag |

**Betriebskonzept:**
1. Landstrom verfügbar → Klimaanlage direkt vom Netz, Batterien laden
2. Ohne Landstrom, Tag → Solar + Batterie → Inverter → Klimaanlage
3. Batterie <30% SOC → Generator Start (automatisch via CZone)
4. Generator lädt mit 200A → Batterie voll in 2h → Generator Stopp
5. Zyklus: 4h Batterie / 2h Generator statt 18h durchgehend

**Ergebnis:**
- Generator-Laufzeit: von 18h auf 6h/Tag reduziert (−67%)
- Dieselverbrauch: von 81 l/Tag auf 27 l/Tag (−67%)
- Einsparung: ~81€/Tag bei 1,5€/Liter (Mittelmeer Diesel Yachthafen)
- ROI: ~18 Monate (Material 35.000€, Einbau 12.000€)
- AYDI-Score: Effizienz 88/100, Elektrik 94/100

---

### ANHANG D: Fallstudie — Katamaran 42ft, Solardach-Optimierung

#### Ausgangssituation

**Boot:** Lagoon 42, Baujahr 2020, 12,80m LOA
**Problem:** Solaranlage liefert nur 60% des theoretischen Ertrags. Eigner plant Langfahrt und benötigt maximale Energieautarkie.

#### Analyse (AYDI Visual + Structural Pipeline)

**Installiert:** 6× 100W Monokristallin auf Bimini-Dach (flach)
**Theoretisch:** 600 Wp × 5h (Mittelmeer) = 3.000 Wh/Tag
**Gemessen:** Ø 1.800 Wh/Tag

**Identifizierte Probleme:**
1. PWM-Regler statt MPPT (Verlust: ~20%)
2. Alle 6 Module in Serie → eine Verschattung reduziert alles (Boom-Schatten nachmittags!)
3. Kabelquerschnitt 2,5 mm² über 8m → Verlust 7% bei Volllast
4. Module flach → keine Neigung zur Sonne

#### Lösung

| Maßnahme | Verbesserung |
|----------|-------------|
| MPPT-Regler (Victron 150/45) | +20% Ertrag |
| 3 Strings à 2 Module (Verschattungstoleranz) | +15% bei Teilverschattung |
| Kabelquerschnitt 6mm² | +5% (weniger Verlust) |
| 2 zusätzliche Module (gesamt 800 Wp) | +33% Kapazität |
| Neigbarer Rahmen (15° manuell) | +10% im Winter/Übergangsmonate |

**Ergebnis:**
- Neuer Ertrag: Ø 3.800 Wh/Tag (Mittelmeer Sommer)
- Tagesverbrauch Langfahrt-Modus: 3.200 Wh/Tag
- Bilanz: +600 Wh/Tag Überschuss → Generator nur alle 5–7 Tage für Wäsche/Watermaker
- Investition: 2.800€ (Material + Arbeit)
- AYDI-Score Solar: 91/100 (vorher: 58/100)

---

### ANHANG E: Fallstudie — Kriechstrom-Diagnose auf Blauwasseryacht

#### Ausgangssituation

**Boot:** Amel 54, Baujahr 2012, 16,50m LOA
**Problem:** Batterie verliert 80 Ah in 48h Standzeit (Hafen, alles ausgeschaltet). Eigner bemerkt verstärkten Zinkanoden-Verbrauch.

#### Diagnose-Protokoll

**Schritt 1: Ruhestrom-Messung**
- Zangenamperemeter (DC) am Batterie-Pluskabel: 3,2A Ruhestrom!
- Erwartet: <0,5A (Standby-Geräte: BMS, CO-Melder, Bilge-Float)
- Defizit: 2,7A unerklärter Strom

**Schritt 2: Systematische Eingrenzung**
- Alle Sicherungen einzeln entfernt und Strom gemessen:
  - Kreis "Salon" entfernt: Strom sinkt um 0,3A (Standby-Geräte)
  - Kreis "Maschinenraum" entfernt: Strom sinkt um 0,8A (!!)
  - Kreis "AC-Charger" entfernt: Strom sinkt um 1,5A (!!!)
  - Rest: 0,6A (BMS, CO, Bilge-Float = korrekt)

**Schritt 3: Ursachenanalyse**
- Maschinenraum 0,8A: Bilgepumpe-Relais zieht dauerhaft an (Float-Schalter Kontaktfehler → klebt in ON)
- AC-Charger 1,5A: Ladegerät hat INTERNEN Fehler → zieht aus Batterie statt zu laden (Rückstrom durch defekte Diode!)

**Schritt 4: Elektrolyse-Check**
- Silber/Silberchlorid-Referenzelektrode ins Wasser neben dem Boot
- Messung: −820 mV → AKTIVE KORROSION (Ziel: −800 bis −1050 mV)
- Kriechstrom über Schutzleiter (Landstrom PE) zum Nachbarboot: 450 mA gemessen!

#### Lösung

| Problem | Maßnahme | Kosten |
|---------|----------|--------|
| Float-Schalter | Austausch gegen neuen Bilge-Float | 45€ |
| Ladegerät Rückstrom | Gerät ersetzen (Victron Blue Smart) | 280€ |
| Elektrolyse Landstrom | Galvanischer Isolator (ProSafe FS30) | 350€ |
| Gesamtkosten | | 675€ |

**Ergebnis:**
- Ruhestrom: 0,4A (Norm-konform)
- Zinkanoden-Verbrauch normalisiert
- Batterie-Autonomie: 48h → keine messbare Entladung mehr in 48h
- AYDI-Score: +35 Punkte (Sicherheit + Elektrik)

---

### ANHANG F: Fallstudie — Superyacht 30m, Notfall-Blackout-Analyse

#### Ausgangssituation

**Boot:** Custom Motoryacht 30m, Alu, Baujahr 2018
**Vorfall:** Totaler Blackout bei Nachtfahrt auf See. Backup-Generator startete nicht. Crew 12 Minuten ohne jegliche Stromversorgung (Navigation, Lichter, Funk).

#### Root Cause Analysis

**Auslöser-Kette:**
1. Generator 1 (laufend): Kühlwasser-Alarm → automatische Abschaltung (korrekt)
2. Power Management System (PMS): Sendet Start-Signal an Generator 2
3. Generator 2: Starter dreht, zündet nicht (Luft im Kraftstoffsystem!)
4. PMS: 3× Startversuch, dann Fehler-Meldung "Gen 2 Start Fail"
5. Emergency Switchboard (ESB): Sollte auf Batterie-USV umschalten
6. ESB: Batterie-Kontaktschütz zieht NICHT an → Steuerspule korrodiert!
7. BLACKOUT TOTAL — 12 Minuten bis manuelles Eingreifen

**Identifizierte Schwachstellen:**

| Schwachstelle | Sollzustand | Istzustand |
|-------------|-----------|-----------|
| Gen-2-Kraftstoff | Entlüftet, startbereit | Luft im System (Tank leergefahren + nicht entlüftet) |
| ESB-Kontaktschütz | Funktionsprüfung monatlich | Nicht geprüft seit 8 Monaten, Korrosion |
| USV-Batterie | Kapazitätstest quartalsweise | Letzter Test: 14 Monate her |
| Alarm "Gen 2 nicht startbereit" | Vorab-Warnung wenn Kraftstoff <20% | Nicht implementiert |
| Redundanz-Test | Blackout-Drill halbjährlich | Nie durchgeführt |

#### Empfehlungen

1. **Monatlich:** ESB-Umschalttest (Last auf Batterie → zurück)
2. **Quartalsweise:** USV-Batteriekapazitätstest
3. **Software:** Vorab-Warnung wenn Backup-Generator nicht startbereit
4. **Hardware:** Zweites ESB-Kontaktschütz parallel (redundant)
5. **Prozedur:** Blackout-Drill für Crew alle 6 Monate
6. **AYDI-Alert:** Kritischer Sicherheitsbefund, Score 0/100 bis behoben

---

### ANHANG G: Fallstudie — Elektromagnetische Störung eines Autopilot-Systems

#### Ausgangssituation

**Boot:** Bavaria C42, Baujahr 2021, 12,80m LOA
**Problem:** Autopilot (Raymarine EV-150) fährt bei Motorbetrieb >2000 rpm wild hin und her, unter Segeln einwandfrei.

#### Diagnose

**Test 1:** Motor auf Neutral, 2500 rpm → Autopilot spinnt → Motor ist Störquelle
**Test 2:** Alle Verbraucher aus, nur Autopilot + Motor → Problem bleibt → Keine Interaktion mit anderen Verbrauchern
**Test 3:** Neue LED-Positionslichter (billig, Amazon) abgeklemmt → Problem VERSCHWUNDEN!

**Ursache:** Die LED-Positionslichter haben einen PWM-Treiber ohne EMV-Filter. Bei Motorbetrieb führt die höhere Versorgungsspannung (14,2V statt 12,8V) zu einem anderen PWM-Muster, das exakt im Frequenzbereich des Fluxgate-Kompass-Signals liegt!

**Beweis:** Oszilloskop am Versorgungskabel der LED-Lichter: 40 mV Peak-to-Peak Störung bei 10 kHz — genau die Empfindlichkeitsfrequenz des Kompass-Sensors.

#### Lösung

| Maßnahme | Wirkung | Kosten |
|----------|---------|--------|
| LED-Lichter ersetzen (Hella Marine NaviLED PRO) | Eliminiert Störquelle | 280€ |
| Ferritkern auf alte Lichter (Provisorium) | Reduziert um 80% | 8€ |
| Separate Masseführung Autopilot (sternförmig) | Verhindert Einstreuung über Masse | 50€ (Kabel) |

**AYDI-Lesson:** Billige LED-Beleuchtung ohne CE-EMV-Zertifikat ist eine der häufigsten Störquellen auf modernen Booten! IMMER marine-zertifizierte Leuchtmittel verwenden.

---

### ANHANG H: Fallstudie — LiFePO4-BMS-Abschaltung bei Kälte

#### Ausgangssituation

**Boot:** Hallberg-Rassy 340, Baujahr 2010, 10,40m LOA, nachgerüstet mit LiFePO4
**Problem:** Boot in Norwegen, Herbsttörn. Morgens um 06:00 nach kalter Nacht (Kabine 5°C): Motor springt nicht an, alle Systeme tot. BMS hat abgeschaltet.

#### Analyse

**Batterie:** Victron Smart LiFePO4 12V/200Ah (mit integriertem BMS)
**BMS-Einstellung:** Lade-Cutoff bei <5°C Zellentemperatur
**Problem:** Die Nachttemperatur sank auf 2°C in der Backskiste (Batteriestandort). Das BMS schaltet ALLES ab — nicht nur Laden, auch Entladen! (Sicherheitsfunktion: bei <0°C kann auch Entladung Lithium-Plating verursachen, je nach BMS-Konfiguration)

#### Warum das ein Problem ist

- Starterbatterie: War AUCH LiFePO4 (Fehler bei Umrüstung!)
- Keine Heizmatte an Batterie
- Kein externer Bypass für Notstart

#### Lösung

| Maßnahme | Begründung |
|----------|-----------|
| Starterbatterie: AGM 12V/80Ah | AGM funktioniert auch bei −20°C |
| Heizmatte an Service-LiFePO4 | 30W Silikonheizmatte mit Thermostat |
| BMS-Konfiguration: Entladung bis −10°C erlauben | Nur Laden ist bei Kälte kritisch |
| Batterie-Kasten isoliert | 40mm XPS-Schaum rundum |
| Temperaturüberwachung via Cerbo GX | Alarm bei <8°C Zellentemperatur |

**AYDI-Regel:** Bei LiFePO4-Umrüstung IMMER klären: Was passiert bei Kälte? Starterbatterie MUSS kältetauglich bleiben (AGM/Blei). LiFePO4-BMS-Abschaltung kann katastrophal sein, wenn keine Alternative vorhanden.

---

## 12. ANHANG I–R — Pydantic v2 Modelle

### ANHANG I: Basis-Datenmodelle Bordnetz

```python
"""
AYDI Electrical System Base Models
Bordnetz-Grundmodelle für DC-Systeme, Energiebilanz und Verbraucheranalyse.
"""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class VoltageLevel(str, Enum):
    """Supported voltage levels for yacht electrical systems."""
    DC_12V = "12v"
    DC_24V = "24v"
    DC_48V = "48v"
    AC_230V = "230v_ac"
    AC_400V = "400v_ac_3phase"


class BatteryChemistry(str, Enum):
    """Battery chemistry types used in marine applications."""
    LEAD_ACID_WET = "lead_acid_wet"
    LEAD_ACID_AGM = "agm"
    LEAD_ACID_GEL = "gel"
    LIFEPO4 = "lifepo4"
    LI_NMC = "li_nmc"
    LI_TITANATE = "lto"


class ConsumerPriority(str, Enum):
    """Consumer priority classes K1-K6 for load shedding."""
    K1_SAFETY = "k1_safety"
    K2_NAVIGATION = "k2_navigation"
    K3_OPERATION = "k3_operation"
    K4_SUPPLY = "k4_supply"
    K5_COMFORT = "k5_comfort"
    K6_LUXURY = "k6_luxury"


class ConfidenceLevel(str, Enum):
    """Confidence level for electrical assessments."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class OperatingProfile(str, Enum):
    """Operating profiles for energy balance calculation."""
    HARBOR_SHORE_POWER = "harbor_shore_power"
    HARBOR_NO_SHORE = "harbor_no_shore"
    ANCHORING_DAY = "anchoring_day"
    ANCHORING_NIGHT = "anchoring_night"
    SAILING_DAY = "sailing_day"
    SAILING_NIGHT = "sailing_night"
    MOTORING_DAY = "motoring_day"
    MOTORING_NIGHT = "motoring_night"
    PASSAGE_24H = "passage_24h"


class CableType(str, Enum):
    """Marine-approved cable types."""
    MARINE_TINNED = "marine_tinned"
    FLRY_B = "flry_b"
    NSGAFOEU = "nsgafoeu"
    H07RN_F = "h07rn_f"
    LIYCY_SHIELDED = "liycy_shielded"
    COAXIAL_RG213 = "coaxial_rg213"


class FuseType(str, Enum):
    """Fuse types used in marine electrical systems."""
    ATO_ATC_BLADE = "ato_atc_blade"
    ANL_BOLT = "anl_bolt"
    MRBF_TERMINAL = "mrbf_terminal"
    CLASS_T = "class_t"
    THERMAL_MAGNETIC = "thermal_magnetic"
    MIDI = "midi"


class NetworkTopology(str, Enum):
    """Electrical network topology types."""
    BUS = "bus"
    STAR = "star"
    RING = "ring"
    HYBRID = "hybrid"


class ElectricalConsumer(BaseModel):
    """A single electrical consumer on the yacht."""

    model_config = {"from_attributes": True}

    name: str = Field(..., description="Consumer name (German)")
    name_en: str = Field(..., description="Consumer name (English)")
    nominal_power_w: float = Field(..., ge=0, description="Nominal power in Watts")
    nominal_voltage_v: float = Field(..., description="Nominal operating voltage")
    nominal_current_a: float = Field(..., ge=0, description="Nominal current in Amps")
    inrush_factor: float = Field(
        default=1.0, ge=1.0, le=10.0,
        description="Inrush current multiplier (e.g. 5.0 for compressor)"
    )
    duty_cycle_percent: float = Field(
        ..., ge=0, le=100,
        description="Average duty cycle in percent"
    )
    priority: ConsumerPriority = Field(..., description="Load shedding priority")
    circuit_number: Optional[int] = Field(None, description="Assigned circuit number")
    cable_length_m: float = Field(..., ge=0, description="One-way cable length in meters")
    cable_cross_section_mm2: Optional[float] = Field(
        None, ge=0.5,
        description="Installed cable cross-section in mm²"
    )
    fuse_rating_a: Optional[float] = Field(None, description="Installed fuse rating in Amps")
    location_zone: Optional[str] = Field(None, description="Installation zone on yacht")

    @field_validator("nominal_current_a", mode="before")
    @classmethod
    def calculate_current_if_zero(cls, v, info):
        """Auto-calculate current from power and voltage if not provided."""
        if v == 0 and info.data.get("nominal_power_w") and info.data.get("nominal_voltage_v"):
            return info.data["nominal_power_w"] / info.data["nominal_voltage_v"]
        return v

    @property
    def average_power_w(self) -> float:
        """Average power considering duty cycle."""
        return self.nominal_power_w * (self.duty_cycle_percent / 100.0)

    @property
    def peak_current_a(self) -> float:
        """Peak current including inrush."""
        return self.nominal_current_a * self.inrush_factor


class BatteryBank(BaseModel):
    """Battery bank specification."""

    model_config = {"from_attributes": True}

    name: str = Field(..., description="Battery bank identifier")
    chemistry: BatteryChemistry
    nominal_voltage_v: float = Field(..., description="Nominal bank voltage")
    capacity_ah: float = Field(..., gt=0, description="Nominal capacity in Ah at C/20")
    cells_in_series: int = Field(..., gt=0)
    strings_in_parallel: int = Field(default=1, gt=0)
    max_dod_percent: float = Field(
        ..., gt=0, le=100,
        description="Maximum depth of discharge in percent"
    )
    max_charge_current_a: float = Field(..., gt=0)
    max_discharge_current_a: float = Field(..., gt=0)
    has_bms: bool = Field(default=False)
    temperature_min_charge_c: float = Field(
        default=-20.0,
        description="Minimum temperature for charging in Celsius"
    )
    temperature_min_discharge_c: float = Field(
        default=-30.0,
        description="Minimum temperature for discharging in Celsius"
    )
    weight_kg: float = Field(..., gt=0)
    cycle_life_80dod: Optional[int] = Field(
        None,
        description="Expected cycles at 80% DoD"
    )
    year_installed: Optional[int] = Field(None)

    @property
    def usable_capacity_ah(self) -> float:
        """Usable capacity considering max DoD."""
        return self.capacity_ah * (self.max_dod_percent / 100.0)

    @property
    def usable_energy_wh(self) -> float:
        """Usable energy in Wh."""
        return self.usable_capacity_ah * self.nominal_voltage_v


class ChargingSource(BaseModel):
    """A charging source for the electrical system."""

    model_config = {"from_attributes": True}

    name: str = Field(..., description="Charging source name")
    source_type: str = Field(
        ...,
        description="Type: alternator, solar, wind, shore_charger, generator, hydro"
    )
    max_output_current_a: float = Field(..., gt=0)
    output_voltage_v: float = Field(..., gt=0)
    efficiency_percent: float = Field(default=85.0, ge=50, le=100)
    availability_hours_per_day: Optional[float] = Field(
        None, ge=0, le=24,
        description="Expected hours of availability per day"
    )
    peak_power_w: Optional[float] = Field(None, gt=0)
    notes: Optional[str] = Field(None)

    @property
    def max_output_power_w(self) -> float:
        """Maximum output power in Watts."""
        return self.max_output_current_a * self.output_voltage_v

    @property
    def daily_energy_wh(self) -> Optional[float]:
        """Estimated daily energy output if availability is known."""
        if self.availability_hours_per_day is not None:
            return (
                self.max_output_power_w
                * self.availability_hours_per_day
                * (self.efficiency_percent / 100.0)
            )
        return None
```

### ANHANG J: Spannungsabfall-Berechnung

```python
"""
AYDI Voltage Drop Calculator
Spannungsabfall-Berechnung nach ABYC E-11 und ISO 10133.
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field, computed_field


# Copper resistivity at different temperatures [Ohm·mm²/m]
COPPER_RESISTIVITY = {
    20: 0.01750,
    25: 0.01784,
    30: 0.01819,
    35: 0.01853,
    40: 0.01888,
    45: 0.01922,
    50: 0.01956,
    55: 0.01991,
    60: 0.02025,
    65: 0.02059,
    70: 0.02094,
}

# Standard cable cross-sections in mm² (metric norm series)
STANDARD_CROSS_SECTIONS_MM2 = [
    0.5, 0.75, 1.0, 1.5, 2.5, 4.0, 6.0, 10.0,
    16.0, 25.0, 35.0, 50.0, 70.0, 95.0, 120.0, 150.0, 185.0, 240.0,
]

# Derating factors for bundled cables
BUNDLE_DERATING = {
    (1, 3): 1.00,
    (4, 6): 0.80,
    (7, 10): 0.70,
    (11, 20): 0.60,
    (21, 999): 0.50,
}


class VoltageDropInput(BaseModel):
    """Input parameters for voltage drop calculation."""

    model_config = {"from_attributes": True}

    system_voltage_v: float = Field(..., description="System nominal voltage (12 or 24)")
    current_a: float = Field(..., gt=0, description="Load current in Amps")
    cable_length_one_way_m: float = Field(
        ..., gt=0,
        description="One-way cable length in meters (function doubles for return)"
    )
    cable_cross_section_mm2: Optional[float] = Field(
        None, gt=0,
        description="Cable cross-section. If None, minimum is calculated."
    )
    ambient_temperature_c: float = Field(
        default=30.0, ge=-10, le=70,
        description="Ambient temperature for resistivity correction"
    )
    is_critical_consumer: bool = Field(
        default=True,
        description="True=3% max drop (ABYC critical), False=10% max drop"
    )
    cables_in_bundle: int = Field(
        default=1, ge=1,
        description="Number of cables in the same bundle/conduit"
    )
    max_voltage_drop_percent_override: Optional[float] = Field(
        None, gt=0, le=20,
        description="Override max voltage drop percent (instead of 3%/10% rule)"
    )


class VoltageDropResult(BaseModel):
    """Result of voltage drop calculation."""

    model_config = {"from_attributes": True}

    voltage_drop_v: float = Field(..., description="Calculated voltage drop in Volts")
    voltage_drop_percent: float = Field(..., description="Voltage drop as percentage")
    max_allowed_drop_percent: float = Field(..., description="Maximum allowed drop (ABYC)")
    max_allowed_drop_v: float = Field(..., description="Maximum allowed drop in Volts")
    is_compliant: bool = Field(..., description="True if within ABYC limits")
    cable_cross_section_mm2: float = Field(..., description="Used cable cross-section")
    minimum_cross_section_mm2: float = Field(
        ..., description="Minimum required cross-section for compliance"
    )
    recommended_cross_section_mm2: float = Field(
        ..., description="Next standard cross-section above minimum"
    )
    power_loss_w: float = Field(..., description="Power dissipated in cable")
    cable_resistance_ohm: float = Field(..., description="Total cable resistance (both ways)")
    temperature_corrected_resistivity: float = Field(
        ..., description="Copper resistivity at given temperature"
    )
    derating_factor: float = Field(..., description="Applied bundle derating factor")
    notes: list[str] = Field(default_factory=list, description="Warnings and notes")


def get_resistivity_at_temperature(temp_c: float) -> float:
    """Get copper resistivity at given temperature using linear interpolation."""
    alpha = 0.00393  # Temperature coefficient for copper
    rho_20 = 0.01750
    return rho_20 * (1 + alpha * (temp_c - 20))


def get_bundle_derating(cables_in_bundle: int) -> float:
    """Get derating factor based on number of cables in bundle."""
    for (low, high), factor in BUNDLE_DERATING.items():
        if low <= cables_in_bundle <= high:
            return factor
    return 0.50


def next_standard_cross_section(minimum_mm2: float) -> float:
    """Find the next standard cross-section equal to or above the minimum."""
    for cs in STANDARD_CROSS_SECTIONS_MM2:
        if cs >= minimum_mm2:
            return cs
    return STANDARD_CROSS_SECTIONS_MM2[-1]


def calculate_voltage_drop(params: VoltageDropInput) -> VoltageDropResult:
    """
    Calculate voltage drop for a DC circuit per ABYC E-11.

    The calculation uses the total round-trip cable length (2× one-way)
    and applies temperature correction to copper resistivity.
    """
    # Temperature-corrected resistivity
    rho = get_resistivity_at_temperature(params.ambient_temperature_c)

    # Maximum allowed drop
    if params.max_voltage_drop_percent_override:
        max_drop_pct = params.max_voltage_drop_percent_override
    else:
        max_drop_pct = 3.0 if params.is_critical_consumer else 10.0

    max_drop_v = params.system_voltage_v * (max_drop_pct / 100.0)

    # Bundle derating
    derating = get_bundle_derating(params.cables_in_bundle)

    # Calculate minimum required cross-section
    total_length = 2 * params.cable_length_one_way_m
    min_cs = (total_length * params.current_a * rho) / max_drop_v
    recommended_cs = next_standard_cross_section(min_cs)

    # Use provided cross-section or recommended
    used_cs = params.cable_cross_section_mm2 or recommended_cs

    # Calculate actual voltage drop with used cross-section
    cable_resistance = (total_length * rho) / used_cs
    voltage_drop_v = params.current_a * cable_resistance
    voltage_drop_pct = (voltage_drop_v / params.system_voltage_v) * 100.0
    power_loss = params.current_a ** 2 * cable_resistance

    # Compliance check
    is_compliant = voltage_drop_pct <= max_drop_pct

    # Generate notes
    notes = []
    if not is_compliant:
        notes.append(
            f"NICHT KONFORM: {voltage_drop_pct:.1f}% > {max_drop_pct:.1f}% "
            f"(ABYC E-11). Mindestquerschnitt: {recommended_cs} mm²"
        )
    if params.ambient_temperature_c > 50:
        notes.append(
            f"WARNUNG: Hohe Umgebungstemperatur ({params.ambient_temperature_c}°C). "
            f"Kabelbelastbarkeit um {(1-derating)*100:.0f}% reduziert."
        )
    if params.cables_in_bundle > 3:
        notes.append(
            f"Bündelverlegung ({params.cables_in_bundle} Leiter): "
            f"Derating-Faktor {derating:.2f} angewandt."
        )
    if power_loss > 10:
        notes.append(
            f"Verlustleistung {power_loss:.1f}W — Kabelerwärmung beachten!"
        )

    return VoltageDropResult(
        voltage_drop_v=round(voltage_drop_v, 4),
        voltage_drop_percent=round(voltage_drop_pct, 2),
        max_allowed_drop_percent=max_drop_pct,
        max_allowed_drop_v=round(max_drop_v, 4),
        is_compliant=is_compliant,
        cable_cross_section_mm2=used_cs,
        minimum_cross_section_mm2=round(min_cs, 2),
        recommended_cross_section_mm2=recommended_cs,
        power_loss_w=round(power_loss, 2),
        cable_resistance_ohm=round(cable_resistance, 6),
        temperature_corrected_resistivity=round(rho, 5),
        derating_factor=derating,
        notes=notes,
    )
```

### ANHANG K: Energiebilanz-Modell

```python
"""
AYDI Energy Balance Calculator
Energiebilanz-Berechnung für verschiedene Betriebsprofile.
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field, computed_field

from .base_models import (
    BatteryBank,
    BatteryChemistry,
    ChargingSource,
    ConsumerPriority,
    ElectricalConsumer,
    ConfidenceLevel,
    OperatingProfile,
)


class OperatingPhase(BaseModel):
    """A single operating phase within a profile (e.g., night, day)."""

    model_config = {"from_attributes": True}

    name: str = Field(..., description="Phase name (e.g., 'Nacht', 'Tag')")
    duration_hours: float = Field(..., gt=0, le=24)
    active_consumers: list[str] = Field(
        ..., description="List of consumer names active in this phase"
    )
    charging_sources_active: list[str] = Field(
        default_factory=list,
        description="Charging sources active in this phase"
    )


class EnergyBalanceInput(BaseModel):
    """Input for complete energy balance calculation."""

    model_config = {"from_attributes": True}

    yacht_name: str = Field(..., description="Yacht identifier")
    system_voltage_v: float = Field(..., description="System voltage (12 or 24)")
    consumers: list[ElectricalConsumer] = Field(
        ..., min_length=1, description="All electrical consumers"
    )
    battery_banks: list[BatteryBank] = Field(
        ..., min_length=1, description="All battery banks"
    )
    charging_sources: list[ChargingSource] = Field(
        default_factory=list, description="Available charging sources"
    )
    operating_profile: OperatingProfile = Field(
        ..., description="Selected operating profile"
    )
    phases: list[OperatingPhase] = Field(
        ..., min_length=1, description="Operating phases within the profile"
    )
    system_efficiency: float = Field(
        default=0.90, ge=0.5, le=1.0,
        description="Overall system efficiency (converters, wiring losses)"
    )
    safety_factor: float = Field(
        default=1.2, ge=1.0, le=2.0,
        description="Safety factor for capacity planning"
    )


class PhaseResult(BaseModel):
    """Energy balance result for a single operating phase."""

    model_config = {"from_attributes": True}

    phase_name: str
    duration_hours: float
    total_consumption_wh: float = Field(..., description="Total energy consumed")
    total_charging_wh: float = Field(..., description="Total energy charged")
    net_energy_wh: float = Field(
        ..., description="Net energy (negative = discharge, positive = charge)"
    )
    average_load_w: float
    peak_load_w: float
    consumer_breakdown: dict[str, float] = Field(
        ..., description="Consumption per consumer [Wh]"
    )


class EnergyBalanceResult(BaseModel):
    """Complete energy balance result."""

    model_config = {"from_attributes": True}

    yacht_name: str
    operating_profile: OperatingProfile
    system_voltage_v: float
    confidence: ConfidenceLevel

    # Per-phase results
    phase_results: list[PhaseResult]

    # Daily totals
    total_daily_consumption_wh: float
    total_daily_consumption_ah: float
    total_daily_charging_wh: float
    total_daily_charging_ah: float
    net_daily_balance_wh: float
    net_daily_balance_ah: float

    # Autonomy
    total_usable_battery_wh: float
    total_usable_battery_ah: float
    autonomy_hours: float = Field(
        ..., description="Hours of autonomy without any charging"
    )
    autonomy_days: float

    # Sizing recommendations
    minimum_battery_ah: float = Field(
        ..., description="Minimum recommended battery capacity"
    )
    minimum_charging_w: float = Field(
        ..., description="Minimum charging power to sustain profile"
    )
    is_sustainable: bool = Field(
        ..., description="True if charging exceeds consumption over 24h"
    )

    # Warnings
    warnings: list[str] = Field(default_factory=list)
    recommendations: list[str] = Field(default_factory=list)


def calculate_energy_balance(params: EnergyBalanceInput) -> EnergyBalanceResult:
    """
    Calculate complete energy balance for given operating profile.
    Returns detailed per-phase results and overall sustainability assessment.
    """
    phase_results = []
    total_consumption_wh = 0.0
    total_charging_wh = 0.0

    for phase in params.phases:
        # Calculate consumption for this phase
        phase_consumption = {}
        phase_total_w = 0.0
        phase_peak_w = 0.0

        for consumer in params.consumers:
            if consumer.name in phase.active_consumers:
                avg_power = consumer.average_power_w
                phase_consumption[consumer.name] = avg_power * phase.duration_hours
                phase_total_w += avg_power
                phase_peak_w += consumer.nominal_power_w

        phase_consumption_wh = phase_total_w * phase.duration_hours

        # Calculate charging for this phase
        phase_charge_wh = 0.0
        for source in params.charging_sources:
            if source.name in phase.charging_sources_active:
                source_power = source.max_output_power_w * (source.efficiency_percent / 100.0)
                phase_charge_wh += source_power * phase.duration_hours

        net = phase_charge_wh - phase_consumption_wh

        phase_results.append(PhaseResult(
            phase_name=phase.name,
            duration_hours=phase.duration_hours,
            total_consumption_wh=round(phase_consumption_wh, 1),
            total_charging_wh=round(phase_charge_wh, 1),
            net_energy_wh=round(net, 1),
            average_load_w=round(phase_total_w, 1),
            peak_load_w=round(phase_peak_w, 1),
            consumer_breakdown=phase_consumption,
        ))

        total_consumption_wh += phase_consumption_wh
        total_charging_wh += phase_charge_wh

    # Account for system efficiency
    total_consumption_wh_corrected = total_consumption_wh / params.system_efficiency
    total_consumption_ah = total_consumption_wh_corrected / params.system_voltage_v

    total_charging_ah = total_charging_wh / params.system_voltage_v
    net_balance_wh = total_charging_wh - total_consumption_wh_corrected
    net_balance_ah = net_balance_wh / params.system_voltage_v

    # Battery autonomy
    total_usable_wh = sum(b.usable_energy_wh for b in params.battery_banks)
    total_usable_ah = sum(b.usable_capacity_ah for b in params.battery_banks)

    avg_load_w = total_consumption_wh_corrected / 24.0 if total_consumption_wh_corrected > 0 else 1
    autonomy_hours = total_usable_wh / avg_load_w if avg_load_w > 0 else 0
    autonomy_days = autonomy_hours / 24.0

    # Sizing recommendations
    min_battery_ah = total_consumption_ah * params.safety_factor
    min_charging_w = total_consumption_wh_corrected / 24.0  # Average needed over 24h

    is_sustainable = net_balance_wh >= 0

    # Generate warnings
    warnings = []
    recommendations = []

    if not is_sustainable:
        deficit_ah = abs(net_balance_ah)
        warnings.append(
            f"Energiedefizit: {deficit_ah:.0f} Ah/Tag. "
            f"Ohne zusaetzliche Ladequelle ist das System nicht nachhaltig."
        )
        recommendations.append(
            f"Empfehlung: Zusätzliche Ladeleistung von mindestens "
            f"{abs(net_balance_wh):.0f} Wh/Tag erforderlich "
            f"(z.B. {abs(net_balance_wh)/5:.0f} Wp Solar bei 5h Ertrag)."
        )

    if autonomy_hours < 24:
        warnings.append(
            f"Autonomie nur {autonomy_hours:.1f}h — weniger als 24h. "
            f"Batteriekapazitaet erhoehen oder Verbrauch reduzieren."
        )

    if total_usable_ah < min_battery_ah:
        recommendations.append(
            f"Batteriekapazitaet ({total_usable_ah:.0f} Ah nutzbar) unter "
            f"empfohlenem Minimum ({min_battery_ah:.0f} Ah). "
            f"Erweiterung um {min_battery_ah - total_usable_ah:.0f} Ah empfohlen."
        )

    # Determine confidence
    confidence = ConfidenceLevel.CALCULATED

    return EnergyBalanceResult(
        yacht_name=params.yacht_name,
        operating_profile=params.operating_profile,
        system_voltage_v=params.system_voltage_v,
        confidence=confidence,
        phase_results=phase_results,
        total_daily_consumption_wh=round(total_consumption_wh_corrected, 0),
        total_daily_consumption_ah=round(total_consumption_ah, 1),
        total_daily_charging_wh=round(total_charging_wh, 0),
        total_daily_charging_ah=round(total_charging_ah, 1),
        net_daily_balance_wh=round(net_balance_wh, 0),
        net_daily_balance_ah=round(net_balance_ah, 1),
        total_usable_battery_wh=round(total_usable_wh, 0),
        total_usable_battery_ah=round(total_usable_ah, 0),
        autonomy_hours=round(autonomy_hours, 1),
        autonomy_days=round(autonomy_days, 1),
        minimum_battery_ah=round(min_battery_ah, 0),
        minimum_charging_w=round(min_charging_w, 0),
        is_sustainable=is_sustainable,
        warnings=warnings,
        recommendations=recommendations,
    )
```

### ANHANG L: Bordnetz-Bewertungsmodell

```python
"""
AYDI Electrical System Assessment Model
Bewertungsmodell für das elektrische Bordnetz.
"""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class ElectricalRiskLevel(str, Enum):
    """Risk classification for electrical findings."""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


class ElectricalFinding(BaseModel):
    """A single finding from electrical system assessment."""

    model_config = {"from_attributes": True}

    finding_id: str = Field(..., description="Unique finding identifier")
    title_de: str = Field(..., description="Finding title in German")
    title_en: str = Field(..., description="Finding title in English")
    description_de: str = Field(..., description="Detailed description in German")
    risk_level: ElectricalRiskLevel
    location: str = Field(..., description="Location on yacht")
    affected_system: str = Field(..., description="Affected subsystem")
    measurement_value: Optional[float] = Field(None, description="Measured value")
    measurement_unit: Optional[str] = Field(None, description="Unit of measurement")
    threshold_value: Optional[float] = Field(None, description="Threshold/norm value")
    norm_reference: Optional[str] = Field(
        None, description="Reference norm (e.g., ABYC E-11 Section 11.4)"
    )
    recommendation_de: str = Field(..., description="Recommended action in German")
    estimated_cost_eur: Optional[float] = Field(
        None, ge=0, description="Estimated repair cost"
    )
    confidence: str = Field(..., description="Confidence level of this finding")
    photo_reference: Optional[str] = Field(
        None, description="Reference to supporting photo"
    )
    score_impact: float = Field(
        ..., ge=-100, le=0,
        description="Score impact (negative value)"
    )


class ElectricalSystemScore(BaseModel):
    """Overall electrical system score."""

    model_config = {"from_attributes": True}

    overall_score: float = Field(..., ge=0, le=100)
    safety_score: float = Field(..., ge=0, le=100)
    compliance_score: float = Field(..., ge=0, le=100)
    efficiency_score: float = Field(..., ge=0, le=100)
    condition_score: float = Field(..., ge=0, le=100)
    capacity_score: float = Field(..., ge=0, le=100)

    findings: list[ElectricalFinding] = Field(default_factory=list)
    critical_count: int = Field(default=0, ge=0)
    high_count: int = Field(default=0, ge=0)
    medium_count: int = Field(default=0, ge=0)
    low_count: int = Field(default=0, ge=0)

    confidence: str = Field(default="estimated")
    assessment_notes: list[str] = Field(default_factory=list)

    @property
    def has_critical_findings(self) -> bool:
        """True if any critical findings exist."""
        return self.critical_count > 0

    @property
    def is_seaworthy(self) -> bool:
        """Basic seaworthiness assessment based on electrical system."""
        return self.safety_score >= 60 and self.critical_count == 0
```

### ANHANG M: Kabel-Dimensionierungs-Modell

```python
"""
AYDI Cable Sizing Model
Kabeldimensionierung nach ABYC E-11 / ISO 10133.
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from .base_models import CableType, FuseType


class CableSizingInput(BaseModel):
    """Input for cable sizing calculation."""

    model_config = {"from_attributes": True}

    circuit_name: str = Field(..., description="Circuit identifier")
    system_voltage_v: float = Field(..., description="System voltage")
    max_continuous_current_a: float = Field(..., gt=0)
    cable_length_one_way_m: float = Field(..., gt=0)
    is_critical: bool = Field(default=True, description="3% vs 10% drop limit")
    ambient_temperature_c: float = Field(default=30.0)
    cables_in_bundle: int = Field(default=1, ge=1)
    cable_type: CableType = Field(default=CableType.MARINE_TINNED)
    installation_area: str = Field(
        default="interior",
        description="interior, engine_room, deck, mast, bilge"
    )


class CableSizingResult(BaseModel):
    """Result of cable sizing calculation."""

    model_config = {"from_attributes": True}

    circuit_name: str
    required_cross_section_mm2: float = Field(
        ..., description="Minimum cross-section for voltage drop"
    )
    required_for_ampacity_mm2: float = Field(
        ..., description="Minimum cross-section for current capacity"
    )
    selected_cross_section_mm2: float = Field(
        ..., description="Selected standard cross-section (larger of both)"
    )
    recommended_fuse_a: float = Field(
        ..., description="Recommended fuse rating"
    )
    fuse_type: FuseType
    voltage_drop_percent: float
    voltage_drop_v: float
    is_compliant: bool
    cable_type_recommendation: CableType
    ip_rating_required: str = Field(
        ..., description="Minimum IP rating for installation area"
    )
    total_cable_weight_kg: float = Field(
        ..., description="Estimated weight of cable run (both directions)"
    )
    notes: list[str] = Field(default_factory=list)


# Cable weight per meter for standard cross-sections [kg/m]
CABLE_WEIGHT_PER_METER = {
    0.75: 0.012,
    1.0: 0.015,
    1.5: 0.021,
    2.5: 0.032,
    4.0: 0.048,
    6.0: 0.065,
    10.0: 0.105,
    16.0: 0.155,
    25.0: 0.240,
    35.0: 0.330,
    50.0: 0.470,
    70.0: 0.650,
    95.0: 0.890,
    120.0: 1.100,
}

# IP rating requirements by installation area
IP_REQUIREMENTS = {
    "interior": "IP20",
    "pantry": "IP44",
    "head": "IP44",
    "engine_room": "IP55",
    "cockpit": "IP56",
    "deck": "IP56",
    "mast": "IP67",
    "bilge": "IP68",
    "underwater": "IP68",
}

# Fuse type selection by current range
FUSE_TYPE_BY_CURRENT = {
    (0, 30): FuseType.ATO_ATC_BLADE,
    (30, 60): FuseType.MIDI,
    (60, 200): FuseType.ANL_BOLT,
    (200, 400): FuseType.CLASS_T,
    (400, 800): FuseType.CLASS_T,
}


def select_fuse_type(current_a: float) -> FuseType:
    """Select appropriate fuse type based on current rating."""
    for (low, high), fuse_type in FUSE_TYPE_BY_CURRENT.items():
        if low <= current_a < high:
            return fuse_type
    return FuseType.CLASS_T
```

### ANHANG N: Fehlerbild-Datenmodell

```python
"""
AYDI Electrical Fault Pattern Models
Fehlerbild-Modelle für die elektrische Diagnose.
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from .base_models import ConfidenceLevel


class FaultSymptom(BaseModel):
    """Observable symptom of an electrical fault."""

    model_config = {"from_attributes": True}

    description_de: str = Field(..., description="Symptom description in German")
    observable_by: str = Field(
        ...,
        description="How observed: visual, measurement, functional_test, smell, touch"
    )
    severity: int = Field(..., ge=1, le=5, description="Severity 1-5")


class FaultPattern(BaseModel):
    """A known electrical fault pattern for diagnostic matching."""

    model_config = {"from_attributes": True}

    fault_id: str = Field(..., description="Unique fault pattern identifier")
    name_de: str = Field(..., description="Fault name in German")
    name_en: str = Field(..., description="Fault name in English")
    category: str = Field(
        ...,
        description="Category: voltage_drop, corrosion, short_circuit, "
                    "overload, ground_fault, parasitic_drain, emv, "
                    "battery, charging, communication"
    )
    symptoms: list[FaultSymptom] = Field(..., min_length=1)
    root_causes: list[str] = Field(..., min_length=1)
    risk_level: str = Field(..., description="critical, high, medium, low")
    diagnostic_steps: list[str] = Field(
        ..., description="Ordered diagnostic steps"
    )
    immediate_action_de: str = Field(
        ..., description="Immediate action in German"
    )
    permanent_fix_de: str = Field(
        ..., description="Permanent solution in German"
    )
    affected_systems: list[str] = Field(default_factory=list)
    visual_indicators: list[str] = Field(
        default_factory=list,
        description="Visual indicators detectable by image analysis"
    )
    measurement_criteria: dict[str, str] = Field(
        default_factory=dict,
        description="Measurement name -> pass/fail criteria"
    )
    estimated_repair_hours: float = Field(
        default=0, ge=0,
        description="Estimated repair time in hours"
    )
    estimated_parts_cost_eur: float = Field(
        default=0, ge=0,
        description="Estimated parts cost in EUR"
    )
    score_impact: dict[str, float] = Field(
        default_factory=dict,
        description="Score impacts per category (e.g., {'safety': -30, 'electrical': -20})"
    )
    confidence_when_visual: ConfidenceLevel = Field(
        default=ConfidenceLevel.VISUAL_MEDIUM,
        description="Confidence level when diagnosed from photos"
    )
    confidence_when_measured: ConfidenceLevel = Field(
        default=ConfidenceLevel.MEASURED,
        description="Confidence level when diagnosed from measurements"
    )
    related_norms: list[str] = Field(
        default_factory=list,
        description="Related norms (e.g., 'ABYC E-11 Section 11.4.3')"
    )
```

### ANHANG O: Hersteller- und Produktdatenbank-Modell

```python
"""
AYDI Electrical Products Database Models
Hersteller- und Produktdatenbank-Modelle.
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class Manufacturer(BaseModel):
    """Electrical component manufacturer."""

    model_config = {"from_attributes": True}

    manufacturer_id: str = Field(..., description="Unique manufacturer ID")
    name: str = Field(..., description="Company name")
    country: str = Field(..., description="Country of origin")
    founded_year: Optional[int] = Field(None)
    specialization: list[str] = Field(
        ..., description="Product specializations"
    )
    certifications: list[str] = Field(
        default_factory=list,
        description="Held certifications (CE, DNV, ABYC, etc.)"
    )
    website: Optional[str] = Field(None)
    warranty_years: int = Field(default=2, ge=0)
    integration_protocols: list[str] = Field(
        default_factory=list,
        description="Supported communication protocols"
    )
    market_segment: str = Field(
        ..., description="production, semi_custom, superyacht, all"
    )
    distribution: str = Field(
        ..., description="worldwide, europe, north_america, regional"
    )
    notes: Optional[str] = Field(None)


class ElectricalProduct(BaseModel):
    """An electrical product/component for marine use."""

    model_config = {"from_attributes": True}

    product_id: str = Field(..., description="Unique product ID")
    manufacturer_id: str = Field(..., description="Reference to manufacturer")
    model_name: str = Field(..., description="Product model name/number")
    product_type: str = Field(
        ...,
        description="Type: charger, inverter, inverter_charger, mppt, "
                    "battery_monitor, dc_dc_converter, fuse_panel, "
                    "bus_bar, battery_switch, cable, led_light, "
                    "position_light, shore_connector, isolator"
    )
    input_voltage_range: Optional[str] = Field(
        None, description="Input voltage range (e.g., '180-265V AC')"
    )
    output_voltage_v: Optional[float] = Field(None)
    output_current_a: Optional[float] = Field(None)
    continuous_power_w: Optional[float] = Field(None)
    peak_power_w: Optional[float] = Field(None)
    efficiency_percent: Optional[float] = Field(None, ge=50, le=100)
    ip_rating: Optional[str] = Field(None)
    weight_kg: Optional[float] = Field(None, gt=0)
    dimensions_mm: Optional[str] = Field(
        None, description="LxWxH in mm"
    )
    operating_temp_range_c: Optional[str] = Field(
        None, description="Operating temperature range"
    )
    communication_protocol: list[str] = Field(
        default_factory=list,
        description="Supported protocols"
    )
    certifications: list[str] = Field(default_factory=list)
    list_price_eur: Optional[float] = Field(None, ge=0)
    typical_application: Optional[str] = Field(None)
    compatible_battery_types: list[str] = Field(default_factory=list)
    notes: Optional[str] = Field(None)
```

### ANHANG P: Bordnetz-Architektur-Modell

```python
"""
AYDI Electrical Architecture Model
Bordnetz-Architektur und Topologie-Modell.
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from .base_models import NetworkTopology, VoltageLevel


class ElectricalBus(BaseModel):
    """An electrical bus (power distribution rail)."""

    model_config = {"from_attributes": True}

    bus_id: str = Field(..., description="Unique bus identifier")
    name: str = Field(..., description="Bus name (e.g., 'Main DC Bus', 'Nav Bus')")
    voltage_level: VoltageLevel
    nominal_voltage_v: float
    max_current_a: float = Field(..., gt=0)
    bus_bar_type: str = Field(
        ..., description="copper_bar, terminal_strip, digital_switch"
    )
    location: str = Field(..., description="Physical location on yacht")
    is_redundant: bool = Field(default=False)
    backup_source: Optional[str] = Field(
        None, description="Backup bus or source in case of failure"
    )
    connected_sources: list[str] = Field(
        default_factory=list, description="Connected power sources"
    )
    connected_consumers: list[str] = Field(
        default_factory=list, description="Connected consumer circuits"
    )


class CircuitBreaker(BaseModel):
    """A circuit breaker or fuse in the system."""

    model_config = {"from_attributes": True}

    circuit_id: str = Field(..., description="Unique circuit identifier")
    circuit_number: int = Field(..., description="Panel position number")
    name_de: str = Field(..., description="Circuit label in German")
    rating_a: float = Field(..., gt=0)
    fuse_type: str = Field(..., description="Fuse/breaker type")
    upstream_bus: str = Field(..., description="Connected bus ID")
    cable_cross_section_mm2: float = Field(..., gt=0)
    cable_length_m: float = Field(..., gt=0)
    is_essential: bool = Field(
        default=False,
        description="True if circuit is on emergency/essential panel"
    )
    max_voltage_drop_percent: float = Field(default=3.0)


class ElectricalArchitecture(BaseModel):
    """Complete electrical architecture of the yacht."""

    model_config = {"from_attributes": True}

    yacht_name: str
    yacht_loa_m: float = Field(..., gt=0)
    yacht_type: str = Field(
        ..., description="sailboat, motoryacht, catamaran, superyacht"
    )
    primary_voltage: VoltageLevel
    secondary_voltage: Optional[VoltageLevel] = Field(None)
    topology: NetworkTopology
    buses: list[ElectricalBus] = Field(..., min_length=1)
    circuits: list[CircuitBreaker] = Field(default_factory=list)
    has_generator: bool = Field(default=False)
    generator_power_kva: Optional[float] = Field(None)
    has_shore_power: bool = Field(default=True)
    shore_power_amps: Optional[float] = Field(None)
    has_solar: bool = Field(default=False)
    solar_peak_wp: Optional[float] = Field(None)
    has_wind_generator: bool = Field(default=False)
    has_hydro_generator: bool = Field(default=False)
    has_digital_switching: bool = Field(default=False)
    digital_switching_system: Optional[str] = Field(None)
    total_installed_power_w: float = Field(default=0, ge=0)
    total_cable_weight_kg: Optional[float] = Field(None)
    total_cable_length_m: Optional[float] = Field(None)
    year_installed: Optional[int] = Field(None)
    last_survey_year: Optional[int] = Field(None)
    notes: list[str] = Field(default_factory=list)

    @property
    def is_dual_voltage(self) -> bool:
        """True if system uses two DC voltage levels."""
        return self.secondary_voltage is not None
```

### ANHANG Q: Compliance-Prüfmodell

```python
"""
AYDI Electrical Compliance Check Model
Normenprüfung für elektrische Bordnetze (ABYC E-11, ISO 10133, ISO 13297).
"""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field

from .base_models import ConfidenceLevel


class ComplianceStatus(str, Enum):
    """Status of a single compliance check item."""
    PASS = "pass"
    FAIL = "fail"
    WARNING = "warning"
    NOT_APPLICABLE = "not_applicable"
    NOT_ASSESSED = "not_assessed"


class ComplianceCheckItem(BaseModel):
    """A single compliance check item."""

    model_config = {"from_attributes": True}

    check_id: str = Field(..., description="Unique check identifier")
    norm_reference: str = Field(
        ..., description="Norm and section (e.g., 'ABYC E-11 §11.4.3')"
    )
    requirement_de: str = Field(..., description="Requirement in German")
    requirement_en: str = Field(..., description="Requirement in English")
    category: str = Field(
        ...,
        description="Category: wiring, protection, grounding, battery, "
                    "shore_power, emergency, labeling, ventilation"
    )
    status: ComplianceStatus
    measured_value: Optional[str] = Field(None, description="What was found")
    required_value: Optional[str] = Field(None, description="What is required")
    deviation_description: Optional[str] = Field(
        None, description="Description of non-compliance"
    )
    corrective_action_de: Optional[str] = Field(
        None, description="Required corrective action"
    )
    confidence: ConfidenceLevel
    severity_if_fail: str = Field(
        default="medium",
        description="Severity if non-compliant: critical, high, medium, low"
    )


class ComplianceReport(BaseModel):
    """Complete electrical compliance report."""

    model_config = {"from_attributes": True}

    yacht_name: str
    assessment_date: str = Field(..., description="ISO date of assessment")
    norms_checked: list[str] = Field(
        ..., description="List of norms assessed"
    )
    assessor: Optional[str] = Field(None)

    checks: list[ComplianceCheckItem] = Field(..., min_length=1)

    total_checks: int = Field(..., ge=0)
    passed_count: int = Field(..., ge=0)
    failed_count: int = Field(..., ge=0)
    warning_count: int = Field(..., ge=0)
    not_assessed_count: int = Field(..., ge=0)

    compliance_percentage: float = Field(
        ..., ge=0, le=100,
        description="Percentage of passed checks vs. applicable checks"
    )
    overall_status: ComplianceStatus
    critical_failures: list[str] = Field(
        default_factory=list,
        description="List of critical non-compliances"
    )
    recommendations: list[str] = Field(default_factory=list)
    estimated_remediation_cost_eur: Optional[float] = Field(None, ge=0)
    confidence: ConfidenceLevel

    @property
    def is_compliant(self) -> bool:
        """True if no failures exist."""
        return self.failed_count == 0
```

### ANHANG R: Visuelle Analyse-Modell für Elektrik

```python
"""
AYDI Visual Analysis Model for Electrical Systems
Modell für die visuelle Analyse elektrischer Bordnetz-Komponenten.
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from .base_models import ConfidenceLevel


class VisualElectricalIndicator(BaseModel):
    """A visual indicator detected in electrical system photos."""

    model_config = {"from_attributes": True}

    indicator_id: str = Field(..., description="Unique indicator ID")
    indicator_type: str = Field(
        ...,
        description="Type: corrosion, discoloration, melting, loose_connection, "
                    "improper_splice, missing_strain_relief, cable_damage, "
                    "water_ingress, overloaded_panel, improper_routing, "
                    "missing_labeling, non_marine_component, "
                    "insufficient_cable_support, missing_chafe_protection"
    )
    location_description: str = Field(
        ..., description="Where on the photo / yacht this was detected"
    )
    severity: int = Field(..., ge=1, le=5, description="1=cosmetic, 5=dangerous")
    description_de: str = Field(..., description="Description in German")
    bounding_box: Optional[list[float]] = Field(
        None,
        description="[x_min, y_min, x_max, y_max] normalized 0-1"
    )
    confidence: ConfidenceLevel
    associated_fault_pattern: Optional[str] = Field(
        None, description="Matching fault pattern ID from atlas"
    )
    recommendation_de: str = Field(..., description="Recommendation in German")


class VisualElectricalAssessment(BaseModel):
    """Complete visual assessment of electrical system from photos."""

    model_config = {"from_attributes": True}

    photo_count: int = Field(..., ge=1)
    areas_assessed: list[str] = Field(
        ...,
        description="Areas visible: battery_compartment, main_panel, "
                    "wiring_runs, connections, engine_room_electrical, "
                    "mast_wiring, deck_connections"
    )
    indicators_found: list[VisualElectricalIndicator] = Field(
        default_factory=list
    )
    overall_visual_condition: str = Field(
        ...,
        description="excellent, good, fair, poor, critical"
    )
    overall_confidence: ConfidenceLevel
    visual_score: float = Field(
        ..., ge=0, le=100,
        description="Visual condition score 0-100"
    )
    areas_not_visible: list[str] = Field(
        default_factory=list,
        description="Areas that could not be assessed from provided photos"
    )
    photo_quality_notes: list[str] = Field(
        default_factory=list,
        description="Notes about photo quality limitations"
    )
    further_investigation_needed: list[str] = Field(
        default_factory=list,
        description="Items requiring physical inspection"
    )

    # Integration with structured assessment
    structured_score_weight: float = Field(
        default=0.95,
        description="Weight for structured (measured) data in fusion"
    )
    visual_score_weight: float = Field(
        default=0.05,
        description="Weight for visual assessment in fusion (electrical = low visual weight)"
    )

    @property
    def requires_immediate_action(self) -> bool:
        """True if any severity-5 indicators found."""
        return any(i.severity >= 5 for i in self.indicators_found)
```

---

## 13. Zusätzliche Planungshilfen

### 13.1 Checkliste Bordnetz-Neuinstallation

#### Phase 1: Planung (vor Kauf jeglicher Materialien)

- [ ] Spannungsebene festgelegt (12V / 24V / Hybrid)
- [ ] Vollständige Verbraucherliste erstellt (alle geplanten Geräte)
- [ ] Energiebilanz für alle Betriebsprofile berechnet
- [ ] Batteriekapazität dimensioniert (mit Sicherheitsfaktor 1,3–1,5)
- [ ] Ladequellen dimensioniert (Solar, LiMa, Landstrom, Generator)
- [ ] Autonomie-Ziel definiert und erreichbar bestätigt
- [ ] Kabelquerschnitte für alle Kreise berechnet (Spannungsabfall!)
- [ ] Sicherungsplan erstellt (jeder Kreis einzeln abgesichert)
- [ ] Massekonzept definiert (sternförmig, ein Massepunkt)
- [ ] Kabelwege geplant (Vermeidung Bilge, Scheuerstellen)
- [ ] Normenkonformität geprüft (ABYC E-11 oder ISO 10133)
- [ ] Budget erstellt und freigegeben

#### Phase 2: Beschaffung

- [ ] Marine-zertifizierte Kabel bestellt (verzinnt, richtige Querschnitte)
- [ ] Alle Sicherungen und Halter in korrekter Größe
- [ ] Bus-Bars und Verteiler passend für Gesamtstrom
- [ ] Batterieschalter mit ausreichender Kontaktbelastbarkeit
- [ ] Crimp-Werkzeug mit Ratsche (NICHT Zange aus dem Baumarkt!)
- [ ] Schrumpfschlauch mit Kleber in allen benötigten Größen
- [ ] Kabelbefestigungsmaterial (P-Clips, Edelstahl-Binder, Wellrohr)
- [ ] Kontaktfett / Korrosionsschutz
- [ ] Beschriftungsmaterial (Kabelnummern, Verteilerbeschriftung)
- [ ] Prüfmittel (Multimeter, Zangenamperemeter, Isolationsmessgerät)

#### Phase 3: Installation

- [ ] Alte Installation dokumentiert (Fotos vor Demontage!)
- [ ] Kabelwege vorbereitet (Durchführungen, Schottdurchbrüche abgedichtet)
- [ ] Batterien fest montiert (säurebeständige Wanne, Gurtbefestigung)
- [ ] Hauptbus-Bar installiert und gesichert
- [ ] Kabel verlegt (Signal getrennt von Leistung, min. 50mm Abstand)
- [ ] Alle Verbindungen gecrimpt (Ratschenwerkzeug, Zugprüfung!)
- [ ] Schrumpfschlauch über alle Verbindungen
- [ ] Kabel beschriftet (an beiden Enden!)
- [ ] Massebus-Bar installiert, Bonding-System angeschlossen
- [ ] Sicherungen eingesetzt, Werte dokumentiert

#### Phase 4: Inbetriebnahme und Prüfung

- [ ] Spannungsmessung an allen Kreisen (ohne Last)
- [ ] Polaritätsprüfung an allen Steckdosen/Verbrauchern
- [ ] Spannungsabfallmessung unter Last (kritische Kreise: <3%)
- [ ] Isolationsmessung (Megger, >2 MΩ gegen Masse)
- [ ] Funktionstest aller Verbraucher einzeln
- [ ] Gleichzeitiger Betrieb aller Verbraucher (Lasttest)
- [ ] Temperaturkontrolle an Sicherungen und Bus-Bars unter Volllast
- [ ] Batterie-Monitor kalibriert und getestet
- [ ] Ladung getestet (alle Quellen: LiMa, Solar, Landstrom)
- [ ] Protokoll erstellt und archiviert

### 13.2 Wartungsintervalle Bordelektrik

| Intervall | Prüfung | Methode | Sollwert |
|-----------|---------|---------|----------|
| Monatlich | Batteriespannung (Ruhe) | Multimeter | >12,6V (12V) / >25,2V (24V) |
| Monatlich | Sichtkontrolle Batteriepole | Visuell | Keine Korrosion |
| Monatlich | Bilgepumpe Funktionstest | Manuell auslösen | Pumpt zuverlässig |
| Quartalsweise | Alle Klemmen auf Festsitz | Drehmoment / Hand | Kein Spiel |
| Quartalsweise | Sicherungen Sichtkontrolle | Visuell | Keine Verfärbung |
| Quartalsweise | Batterie-Kapazitätscheck | Monitor SOC-Reset | >80% Nennkapazität |
| Halbjährlich | Isolationsmessung DC | Megger 500V | >2 MΩ |
| Halbjährlich | Spannungsabfall unter Last | Multimeter | <3% kritisch |
| Halbjährlich | Landstrom FI/RCD Test | Testtaste | Löst in <30ms aus |
| Halbjährlich | Zinkanoden Kontrolle | Visuell + Messen | >50% Material vorhanden |
| Jährlich | Professionelle Prüfung | Surveyor / Elektriker | Protokoll |
| Jährlich | Lichtmaschinen-Leistungstest | Strommessung bei 2000 rpm | >80% Nennstrom |
| Jährlich | Solar-Ertragscheck | Vergleich mit Vorjahr | ±10% |
| Alle 3 Jahre | AC-Isolationsmessung | Megger | >1 MΩ (230V-Kreise) |
| Alle 5 Jahre | Komplette Revision | Fachbetrieb | Alle Normen |

### 13.3 Typische Installationsfehler (Top 15)

| Nr. | Fehler | Häufigkeit | Konsequenz | Lösung |
|-----|--------|-----------|-----------|--------|
| 1 | Unterdimensionierter Querschnitt | Sehr häufig | Spannungsabfall, Überhitzung | Berechnung VOR Installation |
| 2 | Fehlende Schrumpfschläuche | Sehr häufig | Korrosion, Kurzschluss | Immer mit Kleber-Schrumpf |
| 3 | Kabel in Bilge verlegt | Häufig | Korrosion, Kurzschluss | Min. 50mm über Bilgenstand |
| 4 | Massestern nicht konsequent | Häufig | Masseschleifen, EMV | Ein zentraler Massepunkt |
| 5 | Falsche Sicherungsgröße | Häufig | Kein Kabelschutz oder Fehlauslösung | Sicherung schützt KABEL |
| 6 | Ungeeignete Kabelbinder | Häufig | Bruch nach 2 Jahren | UV/ölbeständig oder Edelstahl |
| 7 | Nicht-marine Komponenten | Mittel | Vorzeitiger Ausfall, Korrosion | Nur marine-zertifiziert |
| 8 | Löten statt Crimpen | Mittel | Kalte Lötstelle, Bruch bei Vibration | Crimpen mit Ratschenwerkzeug |
| 9 | Signal neben Leistungskabel | Mittel | EMV-Probleme | Min. 50mm Abstand |
| 10 | Batteriepol ohne Abdeckung | Mittel | Kurzschluss bei Werkzeugfall | Isolierte Polabdeckungen |
| 11 | Hauptsicherung zu weit von Batterie | Weniger häufig | Kabelschutz nicht gegeben | <180mm von Batterie (ABYC) |
| 12 | DC-Masse mit Bonding verbunden | Weniger häufig | Elektrolyse, Korrosion | Strikte Trennung! |
| 13 | Keine Beschriftung | Häufig | Fehlersuche unmöglich | Beide Kabelenden + Panel |
| 14 | Falsche Kabelfarben | Mittel | Verwirrung, Verpolung | ABYC/ISO Farbcode einhalten |
| 15 | Kabel an scharfen Kanten | Häufig | Scheuerstelle → Kurzschluss | Wellrohr, Kantenschutz, Tüllen |

### 13.4 Energiequellen-Vergleichstabelle

| Energiequelle | Leistung typisch | Verfügbarkeit | Kosten/kWh | Gewicht/kW | Geräusch | Wartung |
|--------------|-----------------|---------------|-----------|-----------|---------|---------|
| Lichtmaschine (Motor) | 1.000–3.500W | Nur bei Motorlauf | 0,80–1,50€ (Diesel) | gering (am Motor) | Motor-Geräusch | Keilriemen, Kohlen |
| Solar (fest) | 100–400W/m² | Tageslicht, wetterabhängig | 0€ (nach Amortisation) | 6–8 kg/kWp | Keine | Reinigung |
| Solar (flexibel) | 80–200W/m² | Tageslicht, wetterabhängig | 0€ (nach Amortisation) | 3–4 kg/kWp | Keine | Reinigung, Lebensdauer kürzer |
| Windgenerator | 100–600W | Windabhängig (>12 kt) | 0€ (nach Amortisation) | 15–25 kg | Stark bei Starkwind | Lager jährlich |
| Hydrogenerator | 200–500W | Nur bei Fahrt >5 kt | 0€ (nach Amortisation) | 5–10 kg | Minimal | Propeller-Check |
| Generator (Diesel) | 3.000–20.000W | Jederzeit (Kraftstoff) | 0,50–0,80€ | 50–100 kg/kW | Laut (55–75 dB) | 250h-Service |
| Landstrom | Unbegrenzt | Nur im Hafen | 0,30–0,80€ | — | Keine | Stecker-Prüfung |
| Brennstoffzelle (EFOY) | 80–210W | Jederzeit (Methanol) | 2,00–3,50€ | 10–15 kg | Minimal | Patronen-Wechsel |

### 13.5 Entscheidungshilfe: Welches Ladesystem für mein Boot?

```
START: Welches Ladesystem brauche ich?
│
├─ Fahrtgebiet?
│   ├─ Nur Wochenende / Küste (Hafen jede Nacht)
│   │   └─ Landstrom-Ladegerät ausreichend + LiMa
│   │       ├─ Batteriegröße: Tagesverbrauch × 1,5
│   │       └─ Solar optional (50–150 Wp als Erhaltung)
│   │
│   ├─ Küstenfahrt / 1–2 Wochen Urlaub
│   │   └─ LiMa (evtl. Upgrade) + Solar (200–400 Wp) + Landstrom
│   │       ├─ Batteriegröße: 2× Tagesverbrauch
│   │       └─ Generator: nur bei Klimaanlage oder >3000W AC-Bedarf
│   │
│   ├─ Langfahrt / Blauwasser (Wochen ohne Landstrom)
│   │   └─ Große LiMa (extern geregelt) + Solar (600–1500 Wp)
│   │       + Wind/Hydro + evtl. Generator
│   │       ├─ Batteriegröße: 3–5× Tagesverbrauch (LiFePO4!)
│   │       ├─ Solar MUSS Tagesverbrauch decken können
│   │       └─ Generator als Backup für Schlechtwetter-Perioden
│   │
│   └─ Motoryacht (Generator immer verfügbar)
│       └─ Generator + Landstrom + Inverter/Charger
│           ├─ Batteriegröße: 4–8h Inverterbetrieb ohne Generator
│           ├─ Solar: Ergänzung zur Generator-Reduktion
│           └─ Ziel: Generator nur 4–6h/Tag statt durchgehend
│
└─ Budget-Priorität?
    ├─ Minimal: LiMa + Landstrom (Basisausstattung)
    ├─ Mittel: + Solar 200–400 Wp + MPPT
    ├─ Komfort: + größere Batterie (LiFePO4) + Inverter
    └─ Premium: + Generator + Digital Switching + Monitoring
```

---

## Quellenverzeichnis

| Quelle | Beschreibung |
|--------|-------------|
| ABYC E-11 (2022) | AC & DC Electrical Systems on Boats |
| ISO 10133:2012 | Small craft — Electrical systems — Extra-low-voltage DC installations |
| ISO 13297:2020 | Small craft — Electrical systems — Alternating current installations |
| IEC 60092 | Electrical Installations in Ships |
| DIN VDE 0100-710 | Errichten von Niederspannungsanlagen — Medizinische Bereiche (analog marine) |
| COLREG 72 | International Regulations for Preventing Collisions at Sea |
| EU RCD 2013/53/EU | Recreational Craft Directive |
| Calder, Nigel | Boatowner's Mechanical and Electrical Manual, 4th Ed. |
| Victron Energy | Technische Dokumentation, Blue Paper Series |
| Mastervolt | System Design Guide |
| Blue Sea Systems | Marine Electrical Standards Reference |

---

*Dokument-Ende — 22_01_elektrik_grundlagen.md*
*AYDI Knowledge Engine v1.0.0 — Generiert 2026-05-05*
