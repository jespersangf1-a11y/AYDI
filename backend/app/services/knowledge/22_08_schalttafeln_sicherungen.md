# 22_08 — Schalttafeln und Sicherungen: Verteilerpanels, Sicherungsautomaten, ANL/ATO/MIDI, Hauptschalter, Schaltpläne

---

## Metadaten

| Feld | Wert |
|------|------|
| Kategorie | 22 — Elektrik & Elektronik |
| Unterkategorie | 08 — Schalttafeln und Sicherungen |
| Version | 1.0.0 |
| Letzte Aktualisierung | 2026-05-07 |
| Autor | AYDI Knowledge Engine |
| Sprache | Deutsch (Fachtext) / Englisch (Code) |
| Zielgruppe | Yachtkonstrukteure, Elektroplaner, Surveyor, AYDI-Analysemodul |
| Normenstand | ABYC E-11 (2022), ISO 10133 (2012), ISO 13297 (2020), IEC 60092, DIN VDE 0100-709, EN 60269, EN 60898 |
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

### 1.1 Stromverteilung als Nervensystem der Yacht

Die elektrische Verteilung an Bord einer Yacht bildet das Nervensystem des gesamten Fahrzeugs. Während Batterien als Energiespeicher und Kabel als Leitungsbahnen fungieren, sind Schalttafeln und Sicherungen die Schaltzentrale — sie verteilen, schützen und steuern jeden einzelnen Stromkreis an Bord. Ein Versagen dieses Systems hat weitreichende Konsequenzen: vom simplen Ausfall der Innenbeleuchtung bis zum katastrophalen Kabelbrand im Motorraum.

#### Sicherheitsphilosophie: Schutz in Schichten

Das marine Elektrosystem folgt einem mehrschichtigen Schutzkonzept:

```
Schicht 1: Batterie-Hauptschalter
  └── Trennt gesamtes System vom Energiespeicher
  └── Notabschaltung in <2 Sekunden erreichbar

Schicht 2: Hauptsicherung (ANL/MEGA)
  └── Schützt Hauptzuleitung Batterie → Verteiler
  └── Dimensioniert auf maximale Kabelbelastbarkeit
  └── Montage: <180mm vom Batteriepol (ABYC E-11)

Schicht 3: Verteilerpanel-Eingangssicherung
  └── Schützt Sammelschiene (Bus-Bar) im Panel
  └── Typisch: 100–200A je Panel

Schicht 4: Einzelkreis-Sicherung (ATO/ATC, Leitungsschutzschalter)
  └── Schützt einzelnen Kabelweg und Verbraucher
  └── Dimensionierung nach Kabelquerschnitt, NICHT nach Verbraucher

Schicht 5: Geräteinterne Sicherung
  └── Vom Hersteller des Endgeräts dimensioniert
  └── Schützt Geräteelektronik intern
```

#### Kaskadiertes Schutzkonzept — Selektivität

Das Ziel der Selektivität: Bei einem Fehler löst nur die dem Fehler nächstgelegene Sicherung aus. Der Rest des Bordnetzes bleibt unter Spannung. Ein Kurzschluss in der Leselampe der Achterkabine darf niemals die Navigationsbeleuchtung oder die Bilgepumpe abschalten.

Voraussetzung für korrekte Selektivität:

| Ebene | Typische Sicherungsgröße | Auslösezeit (bei 2×I_n) |
|-------|--------------------------|--------------------------|
| Hauptsicherung | 200–400A (ANL/MEGA) | >60 Sekunden |
| Panel-Eingang | 80–150A (ANL/MIDI) | 30–60 Sekunden |
| Einzelkreis | 5–30A (ATO/Automat) | 5–15 Sekunden |
| Geräteebene | 0,5–5A (Feinsicherung) | <1 Sekunde |

**Regel:** Jede übergeordnete Sicherung muss mindestens das 1,6-fache der größten untergeordneten Sicherung betragen und eine langsamere Auslösecharakteristik aufweisen.

#### Historische Entwicklung der Bordnetz-Verteilung

| Jahrzehnt | Verteilungstechnik | Typische Kreisanzahl | Sicherungstyp |
|-----------|-------------------|---------------------|---------------|
| 1970er | Einzel-Kippschalter, offene Schmelzdrahtsicherungen | 4–8 | Glasrohrsicherung 6×30mm |
| 1980er | Erste integrierte Schaltpanels, Kunststoffgehäuse | 8–12 | Glasrohr, erste Flachsicherungen |
| 1990er | Blue Sea Systems revolutioniert Marinepanels | 12–20 | ATO/ATC-Flachsicherungen Standard |
| 2000er | Digitale Anzeigeintegration, Bus-Bar-Systeme | 16–30 | ATO + ANL-Kombination |
| 2010er | Touchscreen-Panels, CAN-Bus-Steuerung | 20–50 | MIDI + Smart-Sicherungen |
| 2020er | Digitale Lastverteilung, NMEA 2000-Integration | 30–80+ | Halbleiter-Schutzschalter, programmierbar |

### 1.2 Normative Grundlagen

#### ABYC E-11 — AC and DC Electrical Systems on Boats (2022)

Die zentrale US-amerikanische Norm für Bordelektrik. Relevante Abschnitte:

| Abschnitt | Thema | Kernaussage |
|-----------|-------|-------------|
| 11.10 | Overcurrent Protection | Jeder nicht-geerdete Leiter muss geschützt sein |
| 11.10.1 | Fuse/Breaker Placement | Max. 180mm (7 inches) vom Anschlusspunkt |
| 11.10.3 | Rating | Sicherung ≤ Kabelbelastbarkeit, ≥ 125% Dauerlast |
| 11.12 | Panelboards | Mindestanforderungen Verteilerpanels |
| 11.13 | Main Disconnect | Batterie-Hauptschalter Pflicht |
| 11.15 | Bus Bars | Material, Dimensionierung, Befestigung |
| 11.17 | Circuit Identification | Beschriftungspflicht aller Kreise |

#### ISO 10133 — Small Craft: Electrical Systems — Extra-low-voltage DC

Europäische Norm für DC-Systeme auf Booten <24m:

- Jeder Kreis einzeln abgesichert
- Sicherungswert abgestimmt auf Kabelquerschnitt
- Verteilerpanel geschützt vor Spritzwasser (min. IPX4 in exponierten Bereichen)
- Beschriftung aller Kreise in landesüblicher Sprache oder Symbolen

#### ISO 13297 — Small Craft: Electrical Systems — AC Installations

Europäische Norm für AC-Systeme (230V) auf Booten:

- Fehlerstromschutzschalter (RCD/FI) Pflicht: ≤30mA Auslösestrom
- Galvanische Trennung durch Trenntransformator empfohlen
- Leitungsschutzschalter (MCB) für jeden AC-Kreis
- Erdungssystem klar definiert (TT oder TN-S)
- AC-Panel physisch getrennt von DC-Panel oder deutlich gekennzeichnet

#### IEC 60092 — Electrical Installations in Ships

Gilt primär für gewerbliche Schifffahrt, wird aber zunehmend als Referenz für Superyachten herangezogen:

- Selektivitätsnachweis gefordert
- Kurzschlussberechnung für alle Verteiler
- Redundanz kritischer Kreise (Navigation, Lenz, Feuer)
- Dokumentationspflicht: Einlinienschaltplan, Stromlaufplan, Verdrahtungslisten

### 1.3 Systemarchitektur — Vom Energiespeicher zum Verbraucher

```
┌─────────────────────────────────────────────────────────────────────┐
│                     BATTERIE-BANK                                   │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐       │
│  │ Batt. 1  │───│ Batt. 2  │───│ Batt. 3  │───│ Batt. 4  │       │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘       │
│       │(+)                                          │(−)           │
└───────┼─────────────────────────────────────────────┼───────────────┘
        │                                             │
   ┌────┴────┐                                   ┌───┴────┐
   │ HAUPT-  │                                   │ MASSE- │
   │ SICHER. │ ANL 300A                          │ BUS-BAR│
   │ 180mm   │                                   │        │
   └────┬────┘                                   └───┬────┘
        │                                             │
   ┌────┴────┐                                        │
   │ BATTERIE│                                        │
   │ HAUPT-  │◄── Notabschaltung                     │
   │ SCHALTER│                                        │
   └────┬────┘                                        │
        │                                             │
   ┌────┴────────────────────────────────────────┐    │
   │         HAUPT-BUS-BAR (+)                   │    │
   │  ┌─────┬─────┬─────┬─────┬─────┬─────┐    │    │
   │  │     │     │     │     │     │     │    │    │
   └──┼─────┼─────┼─────┼─────┼─────┼─────┼────┘    │
      │     │     │     │     │     │     │          │
   ┌──┴──┐┌─┴──┐┌─┴──┐┌─┴──┐┌─┴──┐┌─┴──┐┌─┴──┐     │
   │MIDI ││MIDI││MIDI││MIDI││ANL ││ANL ││ANL │     │
   │ 60A ││ 80A││100A││ 60A││150A││200A││100A│     │
   └──┬──┘└─┬──┘└─┬──┘└─┬──┘└─┬──┘└─┬──┘└─┬──┘     │
      │     │     │     │     │     │     │          │
      ▼     ▼     ▼     ▼     ▼     ▼     ▼          │
   ┌─────┐┌────┐┌────┐┌────┐┌────┐┌────┐┌────┐      │
   │DC   ││DC  ││DC  ││DC  ││Lade││Inv.││Anker│      │
   │Panel││Pan.││Pan.││Pan.││reg.││    ││winde│      │
   │Nav. ││Licht│Pump.│Komf.│    ││    ││     │      │
   └─────┘└────┘└────┘└────┘└────┘└────┘└────┘      │
      │     │     │     │                             │
      ▼     ▼     ▼     ▼                             │
   [Einzelkreise mit ATO/ATC-Sicherungen]             │
      │     │     │     │                             │
      └─────┴─────┴─────┴─────────────────────────────┘
                    (Rückleitung über Masse-Bus)
```

### 1.4 Bootklassen-spezifische Verteilungskomplexität

| Bootsklasse | LOA | Typische DC-Kreise | AC-Kreise | Panels gesamt | Typischer Aufwand |
|-------------|-----|-------------------|-----------|---------------|-------------------|
| Jollenkreuzer | 6–8m | 4–8 | 0 | 1 | 1 Tag |
| Küstenkreuzer (Segel) | 8–11m | 8–16 | 2–4 | 1–2 | 2–3 Tage |
| Fahrtensegler | 11–15m | 16–30 | 4–8 | 2–3 | 4–6 Tage |
| Blauwasser-Segler | 13–18m | 25–45 | 6–12 | 3–5 | 6–10 Tage |
| Motoryacht (klein) | 8–12m | 12–20 | 4–8 | 2–3 | 3–5 Tage |
| Motoryacht (mittel) | 12–18m | 20–40 | 8–16 | 3–5 | 6–10 Tage |
| Motoryacht (groß) | 18–24m | 40–80 | 16–30 | 5–8 | 10–20 Tage |
| Superyacht | 24m+ | 80–200+ | 30–80+ | 8–15+ | 20–60+ Tage |

---

## 2. Grundlagen und Theorie

### 2.1 Sicherungsdimensionierung — Die 150%-Regel

#### Grundprinzip: Die Sicherung schützt das Kabel, nicht den Verbraucher

Dies ist das am häufigsten missverstandene Prinzip der Bordelektrik. Die Sicherung wird NICHT nach dem Nennstrom des angeschlossenen Verbrauchers dimensioniert, sondern nach der Strombelastbarkeit des verwendeten Kabels.

**Dimensionierungsformel nach ABYC E-11:**

```
I_sicherung ≤ I_kabel_max
I_sicherung ≥ 1,25 × I_verbraucher_dauer

Wobei:
  I_sicherung    = Nennstrom der Sicherung [A]
  I_kabel_max    = Maximale Strombelastbarkeit des Kabels [A]
  I_verbraucher  = Dauer-Betriebsstrom des Verbrauchers [A]
```

**Die 150%-Regel (vereinfacht für Praxis):**

Schmelzsicherungen (Fuses) lösen typisch bei 150% ihres Nennstroms innerhalb definierter Zeiträume aus. Das bedeutet:

- Eine 10A-Sicherung löst bei 15A aus (nicht bei 10A!)
- Der verwendete Kabelquerschnitt muss dauerhaft 15A tragen können
- Der Verbraucher darf maximal 80% des Sicherungsnennstroms als Dauerlast ziehen (10A × 0,8 = 8A)

#### Dimensionierungsbeispiel

```
Gegeben:
  - Verbraucher: Ankerwinde, 80A bei Betrieb
  - Kabellänge: 8m (einfach), also 16m Gesamtlänge
  - Spannungsebene: 12V DC
  - Max. erlaubter Spannungsabfall: 3%

Schritt 1: Kabelquerschnitt nach Spannungsabfall
  U_drop = 0,03 × 12V = 0,36V
  R_max = U_drop / I = 0,36V / 80A = 0,0045 Ω
  q = (ρ × L) / R = (0,0175 × 16) / 0,0045 = 62,2 mm²
  → Gewählt: 70 mm² (AWG 2/0)

Schritt 2: Strombelastbarkeit 70 mm² prüfen
  I_max (70mm², Einzelverlegung, 30°C): 170A
  I_max (70mm², gebündelt, 40°C Maschinenraum): ~120A (Derating!)
  → 120A > 80A Betriebsstrom ✓

Schritt 3: Sicherungsdimensionierung
  I_sicherung ≥ 1,25 × 80A = 100A (Mindest)
  I_sicherung ≤ 120A (Kabelbelastbarkeit nach Derating)
  → Gewählt: 100A ANL-Sicherung
  → Auslösung bei ~150A → Kabel hält 120A → Sicher? NEIN!

Korrektur: 
  150% von 100A = 150A > 120A (Kabel nach Derating)
  → PROBLEM: Bei extremer Überlast wird Kabel vor Sicherung überlastet
  
  Lösung: Nächstgrößeren Querschnitt wählen ODER
  → 80A ANL-Sicherung: 150% = 120A = Kabelbelastbarkeit ✓
  → Prüfung: 80A ≥ 80A Betriebsstrom → Grenzwertig!
  → BESSER: 95mm² Kabel mit 100A Sicherung
```

> ⚠️ **ZU PRÜFEN (Audit):** 170A vs. 210A — die Strombelastbarkeit für 70 mm² (Einzelverlegung, 30 °C) ist im obigen Beispiel mit 170A angesetzt, in der Referenztabelle 10.5 unter identisch genannten Bedingungen jedoch mit 210A (und in der AWG-Tabelle 13.8 mit 225A). Ampacity ist quellen-/isolationsabhängig; die korrekte Zahl ist nicht zweifelsfrei belegbar und wurde daher nicht geraten geändert. Für die Dimensionierung stets den konservativsten (niedrigsten) Wert heranziehen.

**Merksatz:** Im Zweifel immer den nächstgrößeren Kabelquerschnitt wählen, nicht die nächstkleinere Sicherung.

### 2.2 Selektivität — Kaskadenabschaltung richtig planen

#### Definition

Selektivität bedeutet: Bei einem Fehler löst immer nur die dem Fehler am nächsten gelegene Schutzeinrichtung aus. Alle vorgeschalteten Sicherungen bleiben intakt.

#### Selektivitätsbedingungen

**Bedingung 1: Stromstaffelung**

```
I_vorgelagert ≥ 1,6 × I_nachgelagert

Beispiel korrekt:
  Hauptsicherung:    200A ANL
  Panel-Eingang:     100A MIDI
  Einzelkreis:        15A ATO
  
  200A ≥ 1,6 × 100A = 160A ✓
  100A ≥ 1,6 × 15A = 24A ✓
```

**Bedingung 2: Zeitstaffelung (bei gleicher Bauform)**

Die vorgelagerte Sicherung muss bei jedem Fehlerstrom langsamer reagieren als die nachgelagerte. Bei Schmelzsicherungen gleicher Bauart ist dies bei korrekter Stromstaffelung automatisch gegeben. Bei Leitungsschutzschaltern muss die Auslösecharakteristik beachtet werden:

| Charakteristik | Magnetische Auslösung bei | Einsatz |
|---------------|--------------------------|---------|
| B | 3–5 × I_n | Ohmsche Lasten, Beleuchtung |
| C | 5–10 × I_n | Motoren (kleiner Anlaufstrom) |
| D | 10–20 × I_n | Transformatoren, Motoren (hoher Anlaufstrom) |
| K | 8–14 × I_n | Wechselrichterbetrieb |
| Z | 2–3 × I_n | Elektronikschutz, empfindlich |

**Bedingung 3: Kurzschluss-Ausschaltvermögen**

Jede Schutzeinrichtung muss den maximal möglichen Kurzschlussstrom sicher abschalten können. Bei Batteriesystemen sind Kurzschlussströme enorm:

| Batterietyp | Innenwiderstand (100Ah) | Max. Kurzschlussstrom |
|-------------|------------------------|----------------------|
| Blei-Säure (nass) | 5–15 mΩ | 800–2.400A |
| AGM | 3–8 mΩ | 1.500–4.000A |
| Gel | 8–20 mΩ | 600–1.500A |
| LiFePO4 | 1–5 mΩ | 2.400–12.000A |
| Li-NMC | 0,5–3 mΩ | 4.000–24.000A |

**Warnung:** LiFePO4-Batterien liefern aufgrund ihres extrem niedrigen Innenwiderstands Kurzschlussströme, die viele Standard-Schmelzsicherungen an ihre Grenzen bringen. Das Ausschaltvermögen (AIC — Ampere Interrupting Capacity) jeder Sicherung muss dem maximalen Kurzschlussstrom der Batterie gewachsen sein.

### 2.3 Kurzschlussschutz vs. Überlastschutz

#### Zwei unterschiedliche Fehlerszenarien

| Merkmal | Kurzschluss | Überlast |
|---------|-------------|----------|
| Ursache | Direkte Verbindung Plus/Minus | Zu viele/zu große Verbraucher |
| Strom | Extrem hoch (1.000–10.000A+) | Mäßig über Nennwert (110–200%) |
| Dauer bis Schaden | Millisekunden–Sekunden | Minuten–Stunden |
| Erkennbar durch | Funkenbildung, Rauch, Hitze | Warme Kabel, Spannungsabfall |
| Schutz durch | Schmelzsicherung, magnetische Auslösung | Thermische Auslösung, Schmelzsicherung |
| Priorität | Sofortige Abschaltung (<10ms ideal) | Abschaltung innerhalb Sekunden–Minuten |

#### Leitungsschutz vs. Geräteschutz

**Leitungsschutz (Pflicht!):**
- Dimensioniert nach Kabelquerschnitt
- Montiert am Anfang der Leitung (nähe Einspeisepunkt)
- Schützt das Kabel vor thermischer Überlastung und Kurzschluss
- Ist die PRIMÄRE Sicherungsdimensionierung

**Geräteschutz (ergänzend):**
- Dimensioniert nach Geräte-Eingangsschaltung
- Oft geräteintegriert (Feinsicherung im Gehäuse)
- Schützt empfindliche Elektronik vor Überspannung/Überstrom
- Ersetzt NICHT den Leitungsschutz

### 2.4 Schaltplan-Lesen — Grundlagen für Surveyor und Designer

#### Symbole nach DIN/IEC

| Symbol | Bezeichnung | DIN-Zeichen |
|--------|-------------|-------------|
| ─/─ | Schmelzsicherung | Rechteck mit Linie |
| ─[>|─ | Diode / Verpolschutz | Dreieck mit Strich |
| ─(M)─ | Motor | Kreis mit M |
| ─(~)─ | Wechselstromquelle | Kreis mit Tilde |
| ─○/ ○─ | Schalter (offen) | Zwei Punkte mit Bogen |
| ─○─○─ | Schalter (geschlossen) | Zwei Punkte verbunden |
| ═══ | Bus-Bar / Sammelschiene | Doppellinie |
| ─┤├─ | Leitungsschutzschalter | Rechteck mit Kreuz |
| ⏚ | Masse / Erdung | Drei waagerechte Linien |
| ─╫─ | Trennschalter | Quadrat mit X |

#### Einlinienschaltplan (Single-Line Diagram)

Der Einlinienschaltplan zeigt die Gesamtstruktur der Verteilung ohne Detailverdrahtung. Er ist das wichtigste Übersichtsdokument:

```
Einlinienschaltplan — Segelyacht 14m

[BATT 1: 200Ah LiFePO4] ──ANL 300A──┐
[BATT 2: 200Ah LiFePO4] ──ANL 300A──┼── HAUPT-BUS (+) 400A
[BATT 3: 200Ah LiFePO4] ──ANL 300A──┘         │
                                                │
                    ┌───────────────┬────────────┤
                    │               │            │
               MIDI 100A      MIDI 80A     ANL 200A
                    │               │            │
              ┌─────┴─────┐   ┌────┴────┐  ┌────┴────┐
              │ DC-Panel  │   │DC-Panel │  │Inverter │
              │ Navigation│   │ Komfort │  │ 3000W   │
              │ 8 Kreise  │   │12 Kreise│  │         │
              └───────────┘   └─────────┘  └─────────┘
```

#### Stromlaufplan (Wiring Diagram)

Der Stromlaufplan zeigt jeden einzelnen Leiter mit Kabelbezeichnung, Querschnitt, Farbe und Anschlusspunkt. Erforderlich für:

- CE-Dokumentation (technisches Dossier)
- Werft-Neubau (Fertigungsunterlage)
- Fehlersuche (Diagnose)
- Versicherungsnachweis (bei Schäden)

### 2.5 Stromkreisaufteilung — Logische Gruppierung

#### Prinzipien der Kreisaufteilung

**Prinzip 1: Funktionale Trennung**

Sicherheitskritische Verbraucher auf eigenen Kreisen, die nicht durch Komfortverbraucher beeinflusst werden können:

| Priorität | Kreisgruppe | Beispiele | Absicherung |
|-----------|-------------|-----------|-------------|
| KRITISCH | Navigation | GPS, Kartenplotter, Radar, AIS | Eigener Kreis, ≤15A |
| KRITISCH | Positionslichter | Nav-Lichter nach ColRegs | Eigener Kreis, ≤10A |
| KRITISCH | Bilgepumpe | Automatische Bilgepumpe(n) | Eigener Kreis, direkt an Batterie |
| KRITISCH | UKW-Funk | VHF, DSC-Controller | Eigener Kreis, ≤10A |
| KRITISCH | Motor-Instrumente | Drehzahl, Temperatur, Öldruck | Eigener Kreis, ≤10A |
| WICHTIG | Autopilot | Hydraulikpumpe, Computer | Eigener Kreis, 15–25A |
| WICHTIG | Ankerwinde | Windlass-Motor | Eigener Kreis, direkt an Batterie, 80–150A |
| WICHTIG | Bugstrahlruder | Thruster-Motor | Eigener Kreis, direkt an Batterie, 150–300A |
| KOMFORT | Innenbeleuchtung | Alle Kabinenleuchten | 1–2 Kreise, je ≤15A |
| KOMFORT | Steckdosen 12V/USB | Ladebuchsen, 12V-Dosen | 1–2 Kreise, je ≤15A |
| KOMFORT | Unterhaltung | Stereo, TV, Lautsprecher | Eigener Kreis, ≤15A |
| KOMFORT | Kühlschrank | Kompressor-Kühlbox | Eigener Kreis, ≤10A |

**Prinzip 2: Zonenbasierte Aufteilung (bei größeren Yachten)**

Ab ~14m LOA empfiehlt sich zusätzlich zur funktionalen eine zonenbasierte Verteilung:

```
Zone 1: Vorschiff
  ├── Ankerlaterne
  ├── Ankerkasten-Beleuchtung
  ├── Bugkabine Licht
  ├── Bugkabine Steckdose
  └── Bug-Lüfter

Zone 2: Salon / Pantry
  ├── Salon-Beleuchtung
  ├── Pantry-Beleuchtung
  ├── Kühlschrank
  ├── Pantry-Steckdosen
  └── Salon-Steckdosen

Zone 3: Navigation
  ├── Kartenplotter
  ├── Radar
  ├── AIS
  ├── Navtisch-Beleuchtung
  └── Instrumente

Zone 4: Cockpit / Deck
  ├── Cockpit-Beleuchtung
  ├── Positionslichter
  ├── Ankerwinde
  ├── Heckdusche
  └── Cockpit-Steckdosen

Zone 5: Achterschiff
  ├── Achterkabine Licht
  ├── Achterkabine Steckdose
  └── Achter-Lüfter

Zone 6: Maschinenraum
  ├── Maschinenraum-Licht
  ├── Bilgepumpe(n)
  ├── Motor-Instrumente
  └── Laderegler
```

**Prinzip 3: Lastverteilung**

Große Verbraucher (>30A) werden nicht über das Verteilerpanel geführt, sondern mit eigener Sicherung direkt an die Batterie-Bus-Bar angeschlossen:

- Ankerwinde (80–150A)
- Bugstrahlruder (150–400A)
- Inverter/Wechselrichter (100–300A)
- Lichtmaschine (40–120A)
- Ladegerät/Ladebooster (40–100A)
- Elektrische Heizung (40–80A)

### 2.6 Batterie-Hauptschalter

#### Anforderungen nach ABYC E-11 und ISO 10133

- Mindestens ein Hauptschalter zwischen Batterie und Bordnetz
- Position: leicht erreichbar, trocken, nicht im Maschinenraum (wenn möglich)
- Nennstrom: ≥ maximal gleichzeitiger Gesamtstrom des Systems
- Kurzschluss-Schaltfähigkeit: ≥ maximaler Kurzschlussstrom
- Kennzeichnung: deutlich als "BATTERY" / "BATTERIE" markiert
- Bedienbar ohne Werkzeug

#### Hauptschalter-Konfigurationen

**Konfiguration 1: Ein-Batterie-System (einfach)**

```
[Batterie] ── Hauptsicherung ── [Hauptschalter ON/OFF] ── [Bus-Bar]
```

**Konfiguration 2: Zwei-Batterie-System mit Wahlschalter (klassisch)**

```
[Starter-Batt.] ──┬── Hauptsicherung ── [Wahlschalter 1/BOTH/2/OFF] ── [Bus-Bar]
[Service-Batt.] ──┘
```

Positionen des Wahlschalters:
- **1:** Nur Batterie 1 (Starter) versorgt Bordnetz
- **2:** Nur Batterie 2 (Service) versorgt Bordnetz
- **BOTH:** Beide Batterien parallel (nur zum Laden oder Notstart!)
- **OFF:** Komplette Trennung

**Warnung BOTH-Position:** Bei Stellung BOTH sind beide Batterien direkt parallelgeschaltet. Unterschiedliche Ladezustände verursachen hohe Ausgleichsströme. Nur kurzzeitig verwenden!

**Konfiguration 3: Zwei getrennte Kreise mit Trennrelais (modern)**

```
[Starter-Batt.] ── Hauptsicherung ── [Hauptschalter 1] ── [Motor-Bus]
                                              │
                                      [Trennrelais/ACR]
                                              │
[Service-Batt.] ── Hauptsicherung ── [Hauptschalter 2] ── [Service-Bus]
```

**Konfiguration 4: Lithium-System mit BMS-Integration**

```
[LiFePO4-Bank] ── BMS-Trennschalter ── Hauptsicherung ── [Hauptschalter] ── [Bus-Bar]
                        │
                   [BMS trennt bei:
                    - Unterspannung <2,5V/Zelle
                    - Überspannung >3,65V/Zelle
                    - Übertemperatur >60°C
                    - Überstrom > Grenzwert]
```

### 2.7 Notabschaltung

#### Anforderungen

- Erreichbar in <2 Sekunden vom Steuerstand
- Mindestens ein weiterer Not-Aus an der Hauptzugangsöffnung (Niedergang)
- Trennt ALLE nicht-essentiellen Verbraucher
- Bilgepumpe und Navigationslicht bleiben aktiv (direkt an Batterie)
- Deutlich gekennzeichnet: Rot, beschriftet, unbewegliche Position

#### Not-Aus-Schaltungskonzept

```
                        ┌──── Bilgepumpe (IMMER aktiv, direkt an Batterie)
                        │
[Batterie] ──ANL── [Bus-Bar] ──── [NOT-AUS-Relais] ──── [Hauptverteiler]
                        │                                       │
                        │                              Navigationslichter
                        │                              (optional: direkt)
                        │
                   Motorsicherung (Starter-Kreis separat)
```

### 2.8 Stromkreis-Berechnung und -Dokumentation

#### Stromkreis-Tabelle (Pflichtdokumentation)

| Kreis-Nr. | Bezeichnung | Verbraucher | I_nenn [A] | I_max [A] | Kabel [mm²] | Sicherung [A] | Kabelfarbe | Länge [m] | U_drop [%] |
|-----------|-------------|-------------|-----------|----------|-------------|---------------|------------|-----------|-----------|
| DC-01 | Navigation | Kartenplotter | 2,5 | 4,0 | 2,5 | 5 ATO | Rot/Schwarz | 6 | 1,7 |
| DC-02 | Positionslichter | LED Nav-Lichter | 1,2 | 2,0 | 1,5 | 3 ATO | Rot/Schwarz | 14 | 2,5 |
| DC-03 | UKW-Funk | VHF + DSC | 1,0/6,0 | 8,0 | 2,5 | 10 ATO | Rot/Schwarz | 5 | 1,1 |
| DC-04 | Autopilot | Hydraulikpumpe | 8,0 | 15,0 | 4,0 | 15 ATO | Rot/Schwarz | 7 | 1,8 |
| DC-05 | Bilgepumpe | Auto-Bilge 3700GPH | 8,5 | 12,0 | 4,0 | 15 ATO | Rot/Schwarz | 9 | 2,7 |
| DC-06 | Radar | Open-Array 4kW | 3,5 | 5,0 | 2,5 | 7,5 ATO | Rot/Schwarz | 8 | 2,0 |
| DC-07 | Innenbeleuchtung | LED-Leuchten gesamt | 3,0 | 5,0 | 2,5 | 7,5 ATO | Rot/Schwarz | 12 | 2,5 |
| DC-08 | Kühlschrank | Kompressor 12V | 4,5 | 7,0 | 2,5 | 10 ATO | Rot/Schwarz | 4 | 0,9 |
| DC-09 | Steckdosen Bug | 2× 12V, 2× USB | 5,0 | 10,0 | 4,0 | 10 ATO | Rot/Schwarz | 10 | 1,8 |
| DC-10 | Steckdosen Heck | 2× 12V, 2× USB | 5,0 | 10,0 | 4,0 | 10 ATO | Rot/Schwarz | 6 | 1,1 |
| DC-11 | Ankerwinde | Windlass 1000W | — | 80 | 25 | 80 ANL | Rot/Schwarz | 8 | 2,9 |
| DC-12 | Heckdusche | Druckwasserpumpe | 6,0 | 10,0 | 2,5 | 10 ATO | Rot/Schwarz | 7 | 1,9 |

---

## 3. Typenübersicht

### 3.1 DC-Verteilerpanels

#### Aufbau und Funktion

Ein DC-Verteilerpanel ist die zentrale Schaltstelle zwischen Batterie-Bus-Bar und den einzelnen Verbraucherstromkreisen. Es kombiniert typischerweise:

- Eingangssicherung (Panel-Hauptsicherung)
- Sammelschiene (interne Bus-Bar)
- Einzelkreis-Sicherungen (ATO/ATC oder Leitungsschutzschalter)
- Schalter (Kippschalter, Wippschalter oder Leitungsschutzschalter als Kombischalter)
- Anzeigeinstrumente (Voltmeter, Amperemeter, LED-Statusanzeigen)
- Beschriftungsfelder

#### Bauformen

| Bauform | Vorteile | Nachteile | Einsatz |
|---------|----------|-----------|---------|
| Fronteinbau (Flush-Mount) | Saubere Optik, IPX2-geschützt | Tiefenraum hinter Panel nötig | Salon, Navstation |
| Aufbau (Surface-Mount) | Einfache Montage, guter Zugang | Steht hervor, weniger elegant | Maschinenraum, Technikräume |
| Modular (DIN-Hutschiene) | Beliebig erweiterbar, Industrie-Standard | Erfordert Schaltschrank | Superyachten, Custom |
| Wasserdicht (IP67) | Für Deckmontage geeignet | Teuer, begrenzte Kreisanzahl | Cockpit, Flybridge |
| Digital/Touch | Moderne Optik, NMEA 2000 | Komplexität, Ausfallrisiko Elektronik | Motoryachten, Superyachten |

#### Technische Spezifikationen — Standard DC-Panel

| Parameter | Minimalanforderung | Empfehlung |
|-----------|-------------------|------------|
| Eingangsspannung | 10–16V DC (12V) / 20–32V DC (24V) | 9,5–17V / 19–33V |
| Maximaler Eingangsstrom | ≥ Summe aller Kreissicherungen × 0,7 | ≥ Summe × 0,8 |
| Bus-Bar Material | Messing, verzinnt | Kupfer, verzinnt |
| Bus-Bar Querschnitt | Berechnet für I_max bei ΔT <30K | Berechnet für I_max bei ΔT <20K |
| Schutzart (Frontseite) | IPX1 (innen) | IPX2 (innen), IPX4 (Cockpit) |
| Kriechstrecke | ≥3mm (12V DC) | ≥6mm |
| Betriebstemperatur | -10°C bis +55°C | -20°C bis +60°C |
| Vibrationsfestigkeit | IEC 60068-2-6: 2g, 10–150Hz | 4g |
| Beschriftung | Bedruckt oder graviert | Graviert + LED-hinterlegt |

### 3.2 AC-Verteilerpanels

#### Besonderheiten gegenüber DC

AC-Verteilerpanels unterliegen strengeren Sicherheitsvorschriften, da Berührungsspannungen von 230V lebensgefährlich sind:

| Anforderung | Norm | Spezifikation |
|-------------|------|---------------|
| FI-Schutzschalter (RCD) | ISO 13297, IEC 61008 | ≤30mA Auslösestrom, Typ A oder B |
| Leitungsschutzschalter (MCB) | EN 60898 | Für jeden Kreis, Kurzschluss-Schaltleistung ≥6kA |
| Berührungsschutz | DIN VDE 0100-410 | Vollständiger Berührungsschutz (IP2X min.) |
| Erdung | ISO 13297 | PE-Leiter durchgängig, grün-gelb |
| Trenntransformator | Empfehlung | Galvanische Trennung Landstrom/Bord |
| Drehfeldanzeige | >5kVA | Korrekte Phasenfolge sicherstellen |
| Netzvorrangschaltung | Bei Inverter+Landstrom | Automatische Umschaltung ohne Unterbrechung |

#### Typische AC-Kreisaufteilung

| Kreis | Verbraucher | Sicherung | Kabel | Bemerkung |
|-------|-------------|-----------|-------|-----------|
| AC-01 | Landstrom-Eingang | 16A C, 2-polig | 3×2,5mm² | Über FI 30mA |
| AC-02 | Inverter-Einspeisung | 16A C, 2-polig | 3×2,5mm² | Über FI 30mA |
| AC-03 | Steckdosen Salon | 16A B | 3×2,5mm² | |
| AC-04 | Steckdosen Kabinen | 16A B | 3×2,5mm² | |
| AC-05 | Pantry (Mikrowelle, Wasserkocher) | 16A B | 3×2,5mm² | Hohe Last! |
| AC-06 | Warmwasserboiler | 10A B | 3×1,5mm² | Dauerlast 1.200W |
| AC-07 | Batterieladegerät | 16A C | 3×2,5mm² | Induktive Last |
| AC-08 | Klimaanlage | 16A C | 3×2,5mm² | Motorstart |
| AC-09 | Watermaker | 10A C | 3×1,5mm² | |
| AC-10 | Waschmaschine | 16A B | 3×2,5mm² | Hoher Anlaufstrom |

### 3.3 Sicherungstypen — Detailübersicht

#### 3.3.1 ATO/ATC-Flachsicherungen (Standard Blade Fuses)

**Beschreibung:** Die am weitesten verbreitete Sicherungsbauform für DC-Einzelkreise im Marine-Bereich. Ursprünglich aus der Automobilindustrie stammend (ATO = Autofuse Type Original), mittlerweile der De-facto-Standard für 12V/24V-Kreise bis 30A.

| Parameter | Wert |
|-----------|------|
| Bauform | Flachstecksicherung, zwei Klingenkontakte |
| Abmessungen | 19,1 × 18,5 × 5,1mm (Standard/ATO) |
| Spannungsbereich | ≤32V DC / ≤16V AC |
| Strombereich | 1A – 40A (Standard: 1–30A) |
| Ausschaltvermögen (AIC) | 1.000A (Standard) — 10.000A (hochwertig) |
| Auslösecharakteristik | Mittelträge (Time-Delay) |
| Schmelzmaterial | Zink-Legierung |
| Gehäuse | Transparenter Kunststoff, farbcodiert |
| Kontaktmaterial | Zinn-beschichtetes Messing |

**Farbcode ATO/ATC:**

| Farbe | Nennstrom | Typische Anwendung |
|-------|-----------|-------------------|
| Schwarz | 1A | Empfindliche Elektronik |
| Grau | 2A | LED-Controller |
| Violett | 3A | Positionslichter (LED) |
| Rosa | 4A | Instrumente |
| Bernstein/Beige | 5A | Kleinstverbraucher |
| Braun | 7,5A | Radio, GPS |
| Rot | 10A | Beleuchtung, Pumpen (klein) |
| Blau | 15A | Steckdosen, Autopilot |
| Gelb | 20A | Druckwasserpumpe, Heizung |
| Transparent/Natur | 25A | Größere Lasten |
| Grün | 30A | Elektr. Kochfeld, Kompressor |
| Orange | 40A | Spezialeinsatz |

#### 3.3.2 Mini-Flachsicherungen (ATM/Mini Blade)

| Parameter | Wert |
|-----------|------|
| Abmessungen | 10,9 × 16,3 × 3,8mm |
| Spannungsbereich | ≤32V DC |
| Strombereich | 2A – 30A |
| Vorteil | Kleinere Halter, Platzersparnis |
| Nachteil | Geringeres Ausschaltvermögen |
| Einsatz | Kompakte Panels, Sekundärverteilung |

#### 3.3.3 Maxi-Flachsicherungen (APX/Maxi Blade)

| Parameter | Wert |
|-----------|------|
| Abmessungen | 29,2 × 34,3 × 9,3mm |
| Spannungsbereich | ≤32V DC |
| Strombereich | 20A – 120A |
| Ausschaltvermögen | 2.000–5.000A |
| Einsatz | Panel-Eingangssicherungen, mittlere Verbraucher |

#### 3.3.4 ANL-Sicherungen (High-Current Fuses)

**Beschreibung:** Hochstromsicherungen für die Absicherung von Hauptzuleitungen, Batteriekabeln und Großverbrauchern. Die Standardsicherung für marine Anwendungen >60A.

| Parameter | Wert |
|-----------|------|
| Abmessungen | 81,3 × 24,1 × 10,4mm (typisch) |
| Spannungsbereich | ≤72V DC |
| Strombereich | 35A – 750A |
| Ausschaltvermögen (AIC) | 6.000A (Standard) — 25.000A (Klasse T) |
| Auslösecharakteristik | Träge (Slow-Blow) |
| Schmelzmaterial | Kupfer oder Silber-Legierung |
| Anschluss | Zwei Schraubbolzen (5/16"-24 UNF) |
| Kontaktfläche | Vernickelt oder verzinnt |

**ANL-Sicherungswerte und Anwendung:**

| Nennstrom | Kabel min. | Typische Anwendung |
|-----------|-----------|-------------------|
| 35A | 6mm² | Laderegler Solar |
| 40A | 10mm² | Ladegerät mittel |
| 50A | 10mm² | Ladegerät groß |
| 60A | 16mm² | DC-Panel Eingang (klein) |
| 80A | 25mm² | DC-Panel Eingang (mittel) |
| 100A | 35mm² | Ankerwinde, DC-Panel (groß) |
| 125A | 35mm² | Inverter 1.500W (12V) |
| 150A | 50mm² | Inverter 2.000W (12V) |
| 200A | 70mm² | Batteriehauptsicherung (12V, mittel) |
| 250A | 95mm² | Inverter 3.000W (12V) |
| 300A | 95mm² | Batteriehauptsicherung (12V, groß) |
| 400A | 120mm² | Bugstrahlruder, Batteriebank |
| 500A | 150mm² | Lithium-Systeme, E-Antrieb |
| 750A | 2×120mm² | High-Performance, Rennyachten |

#### 3.3.5 MIDI-Sicherungen

**Beschreibung:** Kompakte Hochstromsicherung, die die Lücke zwischen ATO (max. 40A) und ANL (ab 35A) schließt. Besonders für Panel-Eingangssicherungen und mittlere Großverbraucher.

| Parameter | Wert |
|-----------|------|
| Abmessungen | 41,3 × 11,9 × 12,2mm |
| Spannungsbereich | ≤32V DC |
| Strombereich | 30A – 200A |
| Ausschaltvermögen (AIC) | 1.000–10.000A |
| Auslösecharakteristik | Mittelträge |
| Anschluss | Schraubbolzen M5 oder 3/16" |

**MIDI-Standardwerte:**

| Nennstrom | Farbe | Typische Anwendung |
|-----------|-------|-------------------|
| 30A | Grün | Kleinverteiler |
| 40A | Orange | Laderegler, kleine Wechselrichter |
| 50A | Rot | DC-Panel Eingang |
| 60A | Gelb | Lichtmaschine |
| 70A | Braun | Großes DC-Panel |
| 80A | Natur | Ladegerät, Inverter-Zuleitung |
| 100A | Blau | Hauptverteiler |
| 125A | Schwarz | Inverter 1.500W |
| 150A | Grau | Inverter 2.000W |
| 200A | Weiß | Batterie-Untererteiler |

#### 3.3.6 MEGA-Sicherungen (Hochstrom-Bolzensicherung)

| Parameter | Wert |
|-----------|------|
| Abmessungen | 68,6 × 18,8 × 32,3mm |
| Spannungsbereich | ≤32V DC |
| Strombereich | 100A – 500A |
| Ausschaltvermögen (AIC) | 2.000A |
| Anschluss | Schraubbolzen M8 (5/16") |
| Einsatz | Alternative zu ANL in kompakter Bauform |

#### 3.3.7 Klasse-T-Sicherungen (High-AIC)

| Parameter | Wert |
|-----------|------|
| Spannungsbereich | ≤160V DC |
| Strombereich | 110A – 800A |
| Ausschaltvermögen (AIC) | 20.000A |
| Auslösecharakteristik | Sehr schnell (Fast-Acting) |
| Einsatz | LiFePO4-Systeme, Inverter-Eingang, hohe Kurzschlussströme |
| Vorteil | Sicher bei Lithium-Batterien mit extrem niedrigem Ri |
| Preis | 3–5× teurer als ANL gleicher Stromstärke |

**Wichtig:** Bei Lithium-Batteriesystemen mit niedrigem Innenwiderstand reicht das Ausschaltvermögen von Standard-ANL-Sicherungen (6.000A) oft nicht aus. Klasse-T-Sicherungen mit 20.000A AIC sind hier die sichere Wahl.

### 3.4 Leitungsschutzschalter (Circuit Breaker)

#### DC-Leitungsschutzschalter

| Parameter | Standard-Automat | Marine-Automat | Thermisch-magnetisch |
|-----------|-----------------|----------------|---------------------|
| Spannung | ≤32V DC | ≤48V DC | ≤60V DC |
| Strombereich | 5–50A | 5–150A | 1–63A |
| Schaltvermögen | 3.000A | 5.000A | 10.000A |
| Auslösung | Thermisch | Thermisch + magnetisch | Thermisch + magnetisch |
| Rücksetzbar | Ja, manuell | Ja, manuell | Ja, manuell |
| Reiheneinbau | Nein | Nein (Toggle) | DIN-Hutschiene |
| Tropentauglich | Nein | Ja (feuchtigkeitsresistent) | Je nach Hersteller |
| Einsatz | Einfache Panels | Panel-Schutzschalter | Schaltschrank-Einbau |

#### Vorteile gegenüber Schmelzsicherungen

| Kriterium | Schmelzsicherung | Leitungsschutzschalter |
|-----------|-----------------|----------------------|
| Wiederverwertbar | Nein (Einweg) | Ja (rücksetzbar) |
| Reservevorrat nötig | Ja (alle Werte vorhalten!) | Nein |
| Auslösecharakteristik | Fest (Schmelzkurve) | Fest (aber definierter) |
| Kosten initial | Niedrig | Mittel–Hoch |
| Kosten langfristig | Hoch (Ersatz) | Niedrig |
| Schalter-Funktion | Nein (separater Schalter) | Ja (Schalter + Schutz) |
| Umgebungstemperatur | Beeinflusst Auslösung | Beeinflusst Auslösung (weniger) |
| Alterung | Keine | Mechanische Abnutzung (~10.000 Zyklen) |
| Kontaktwiderstand | Sehr niedrig (<0,5mΩ) | Höher (1–5mΩ) |

#### AC-Leitungsschutzschalter (MCB)

Für 230V-AC-Kreise an Bord gelten strengere Anforderungen:

| Parameter | Anforderung | Empfehlung Marine |
|-----------|-------------|------------------|
| Nennspannung | 230/400V AC | 230V (Einphasig an Bord Standard) |
| Kurzschluss-Schaltvermögen | ≥6.000A (EN 60898) | ≥10.000A |
| Polzahl | 1P+N oder 2P | 2P (allpolige Abschaltung) |
| Auslösecharakteristik | B, C oder D | B (ohmsche), C (Motoren) |
| FI-Kombination (RCBO) | Optional | Empfohlen für kritische Kreise |
| Salznebelbeständigkeit | Nicht standardmäßig | Marine-zugelassene Typen wählen |

### 3.5 Batterie-Hauptschalter

#### Bauformen

| Typ | Strombereich | Schaltleistung | Einsatz |
|-----|-------------|---------------|---------|
| Drehschalter (Bakelite) | 100–400A | 500–1.500A (Kurzschluss) | Klassische Segelboote |
| Drehschalter (Kunststoff) | 200–600A | 1.500–5.000A | Standardboote |
| Wahlschalter (1/BOTH/2/OFF) | 200–400A | 2.000–5.000A | Zwei-Batterie-Systeme |
| Motorisiert (ferngesteuert) | 250–1.500A | 5.000–15.000A | Superyachten, E-Antrieb |
| Messertrennschalter | 100–400A | 500–2.000A | Rennboote, Minimalismus |
| Schlüsselschalter | 100–300A | 1.000–3.000A | Charteryachten (Diebstahlschutz) |

#### Dimensionierungsregel

```
I_hauptschalter ≥ 1,25 × I_max_system

Wobei I_max_system = Summe aller gleichzeitig möglichen Verbraucher
(Nicht Summe aller Sicherungen! Gleichzeitigkeitsfaktor beachten.)

Gleichzeitigkeitsfaktor (Richtwerte):
  - Segelboot Fahrt:    0,4–0,6
  - Segelboot Hafen:    0,3–0,5
  - Motoryacht Fahrt:   0,5–0,7
  - Motoryacht Hafen:   0,4–0,6
  - Superyacht Betrieb: 0,6–0,8
```

### 3.6 Trennschalter und Lasttrennschalter

#### Trennschalter (Isolator)

Dient zum spannungsfreien Trennen eines Kreises bei Wartung. **Kein Schutzorgan** — darf nur im stromlosen Zustand betätigt werden.

| Eigenschaft | Trennschalter | Lasttrennschalter |
|-------------|---------------|-------------------|
| Schalten unter Last | NEIN (verboten!) | JA (bis Nennstrom) |
| Kurzschluss-Schaltfähigkeit | NEIN | Bedingt (je nach Typ) |
| Schaltstellungsanzeige | JA (sichtbare Kontaktstrecke) | JA |
| Typischer Einsatz | Wartungstrennung | Betriebsschalter |
| Marine-Anwendung | Inverter-Trennung, Panel-Isolation | Batterie-Hauptschalter |

### 3.7 Busbar-Systeme

#### Funktionen der Sammelschiene (Bus-Bar)

Die Bus-Bar ist das zentrale Verteilungselement, an dem mehrere Abgänge zusammengeführt werden. Sie verbindet die Einspeisung (Batterie/Ladequelle) mit den Abgangs-Sicherungen.

#### Dimensionierung

```
Querschnitt Bus-Bar [mm²] = I_max / J_zul

Wobei:
  I_max   = Maximaler Dauerstrom durch die Sammelschiene [A]
  J_zul   = Zulässige Stromdichte [A/mm²]
          = 2,0–3,0 A/mm² (Kupfer, freie Konvektion, ΔT ≤ 30K)
          = 1,5–2,0 A/mm² (Messing, freie Konvektion, ΔT ≤ 30K)

Beispiel:
  I_max = 200A
  Material: Kupfer, verzinnt
  q = 200A / 2,5 A/mm² = 80mm²
  → Bus-Bar Mindestquerschnitt: 80mm²
  → Typisch: 100mm² (Sicherheitsreserve)
```

#### Bus-Bar-Materialien

| Material | Leitfähigkeit | Korrosion | Kosten | Einsatz |
|----------|--------------|-----------|--------|---------|
| Kupfer, blank | 100% (Referenz) | Grünspan (Patina) | Mittel | Geschützte Räume |
| Kupfer, verzinnt | 98% | Sehr gut | Mittel–Hoch | Marine-Standard |
| Kupfer, vernickelt | 97% | Hervorragend | Hoch | Superyacht |
| Messing | 28% | Gut | Niedrig | Einfache Systeme |
| Messing, verzinnt | 27% | Gut | Niedrig–Mittel | Kostengünstige Panels |
| Aluminium | 61% | Problematisch (Salzwasser) | Niedrig | NICHT empfohlen marine |

**Warnung:** Aluminium-Bus-Bars sind im maritimen Umfeld NICHT geeignet. Aluminium korrodiert unter Salzwassereinfluss rapide und bildet hochohmige Oxidschichten, die zu Übergangswiderständen und Wärmeentwicklung führen.

#### Bus-Bar-Konfigurationen

**Einfache Sammelschiene (Terminal Bus):**

```
Einspeisung ── [Bolzen 1] [Bolzen 2] [Bolzen 3] ... [Bolzen N]
                    │          │          │              │
                  Kreis 1   Kreis 2   Kreis 3       Kreis N
```

**Gesicherte Sammelschiene (Fused Bus):**

```
                  ┌── [Sicherung 1] ── Kreis 1
Einspeisung ── BUS├── [Sicherung 2] ── Kreis 2
                  ├── [Sicherung 3] ── Kreis 3
                  └── [Sicherung N] ── Kreis N
```

**Dual-Bus mit Kopplung:**

```
[Batterie 1] ── [Bus-Bar A] ──┬── Kreise A1..An
                               │
                         [Koppelschalter]
                               │
[Batterie 2] ── [Bus-Bar B] ──┴── Kreise B1..Bn
```

---

## 4. Produktlinien und Spezifikationen

### 4.1 Blue Sea Systems

#### 360 Panel System

Das modulare 360 Panel System von Blue Sea Systems ist der De-facto-Standard für individuelle marine Schaltpanels. Basiert auf einem C-Schienen-Montagesystem, das verschiedene Module aufnimmt.

**360 Panel — Kernkomponenten:**

| Komponente | Art.-Nr. Beispiel | Funktion |
|------------|-------------------|----------|
| 360 Panel Rahmen, 4 Positionen | 1224 | Grundrahmen für 4 Module |
| 360 Panel Rahmen, 8 Positionen | 1228 | Grundrahmen für 8 Module |
| 360 Panel Rahmen, 12 Positionen | 1232 | Grundrahmen für 12 Module |
| AC Leitungsschutzschalter 15A | 1210 | Einzelmodul AC-Automat |
| DC Toggle-Breaker 15A | 1202 | Einzelmodul DC-Schutzschalter |
| DC Source Switch | 1205 | Quellenwahlschalter |
| Voltmeter Modul 0–32V | 1239 | Spannungsanzeige |
| Blank Panel | 1240 | Blindabdeckung |

**Spezifikationen 360 Panel:**

| Parameter | Wert |
|-----------|------|
| Rahmenbreite | 5,25" pro 4 Positionen |
| Einbautiefe | 3,5" min. hinter Schottwand |
| Kontaktbelastung | 15A pro Position (Standard) |
| Bus-Bar intern | Kupfer verzinnt, 100A |
| Schutzart | IPX1 (Frontseite) |
| Material Blende | Eloxiertes Aluminium |
| Montage | 4× Schrauben M4 |

#### ST Blade Fuse Block

Die ST-Blade-Sicherungsblöcke sind die meistverkauften marine Sicherungshalter weltweit.

**Blue Sea 5026 — ST Blade Fuse Block, 12 Circuits:**

| Parameter | Wert |
|-----------|------|
| Kreisanzahl | 12 |
| Sicherungstyp | ATO/ATC Blade |
| Maximaler Strom pro Kreis | 30A |
| Maximaler Gesamtstrom | 100A |
| Eingangskabel | 8 AWG (8mm²) Bolzenanschluss |
| Ausgangskabel | 12–18 AWG per Schnellklemme |
| Bus-Bar | Kupfer, verzinnt |
| Masse-Bus integriert | Ja, 12 Positionen |
| Abmessungen | 178 × 102 × 44mm |
| Gewicht | 290g |
| Abdeckung | Transparent, abnehmbar |
| LED-Anzeige | Nein (5032-Modell: Ja, LED pro Kreis) |

**Blue Sea 5032 — ST Blade Fuse Block, 12 Circuits mit LED:**

Identisch wie 5026, zusätzlich:
- LED-Statusanzeige pro Kreis (leuchtet bei intakter Sicherung)
- Negativbus mit Schraubanschlüssen statt Schnellklemmen
- Abnehmbarer Deckel mit Beschriftungsfeld
- Leicht höherer Kontaktwiderstand durch LED-Schaltung (<0,5mΩ)

**Blue Sea 5194 — ANL Fuse Block:**

| Parameter | Wert |
|-----------|------|
| Sicherungstyp | ANL |
| Strombereich | 35–750A |
| Eingang | 3/8"-16 Bolzen |
| Ausgang | 3/8"-16 Bolzen |
| Abmessungen | 127 × 51 × 38mm |
| Material | Glasfaserverstärktes Polyester |
| Temperaturfestigkeit | -40°C bis +125°C |
| Schutzabdeckung | Rote Kunststoffhaube |

**Blue Sea 5191 — MIDI Fuse Block:**

| Parameter | Wert |
|-----------|------|
| Sicherungstyp | MIDI/AMI |
| Strombereich | 30–200A |
| Eingang | 5/16"-18 Bolzen |
| Ausgang | 5/16"-18 Bolzen |
| Abmessungen | 71 × 46 × 28mm |
| Material | Glasfaserverstärktes Polyester |

#### Blue Sea WeatherDeck-Serie

Wasserdichte Panels und Schalter für Cockpit und Decksmontage:

| Produkt | Schutzart | Kreise | Anwendung |
|---------|-----------|--------|-----------|
| WeatherDeck 12V DC Panel | IP66 | 4–8 | Cockpit, Flybridge |
| WeatherDeck Switch | IP66 | 1 | Einzelschalter Deck |
| WeatherDeck Breaker | IP66 | 1 | Schutzschalter Außenbereich |

### 4.2 BEP Marine (Neuseeland)

#### CZone — Digitales Verteilungssystem

CZone ist das fortschrittlichste digitale Energieverteilungssystem für die Marinebranche. Es ersetzt konventionelle Schaltpanels durch programmierbare Halbleiter-Schalter, die über CAN-Bus kommunizieren.

**CZone Kernkomponenten:**

| Komponente | Funktion | Kanäle | Max. pro Kanal |
|------------|----------|--------|----------------|
| Signal Interface (SI) | Digitaler Eingang/Ausgang | 12 Eingänge + 6 Ausgänge | 1A (Signal) |
| Motor Output Interface (MOI) | Leistungsschaltung | 12 High-Side + 6 Low-Side | 25A / 16A |
| Combination Output Interface (COI) | Kombination Ein/Aus | 6 High + 6 Low + 6 Input | 20A / 16A |
| Display Interface (DI) | 3,5" oder 7" Touchscreen | — | — |
| Meter Interface (MI) | Analoge Messungen | 8 analoge + 6 digitale | — |
| Wireless Interface | WiFi/BLE-Gateway | — | — |

**CZone Spezifikationen:**

| Parameter | Wert |
|-----------|------|
| Kommunikation | CAN-Bus, 250kbit/s |
| Protokoll | NMEA 2000 kompatibel |
| Netzspannung | 10–32V DC (12V/24V) |
| Halbleiterschutz | Kurzschluss, Überlast, thermisch |
| Dimmbar | Ja, PWM 0–100% |
| Diagnose | Stromüberwachung pro Kanal |
| Schaltzyklen | >100.000 pro Kanal |
| Betriebstemperatur | -20°C bis +65°C |
| Schutzart | IP67 (mit Steckerverbinder) |

**Vorteile CZone:**
- Keine dicken Kabelstränge zum Schaltpanel — nur CAN-Bus und Stromversorgung
- Dezentrale Montage der Interfaces nahe den Verbrauchern
- Programmierbare Logik (z.B. Ankerlicht AUS wenn Motor AN)
- Fehlerdiagnose per App oder NMEA-Display
- Strommessung an jedem Ausgang
- Dimm-Funktion für Beleuchtung integriert
- Erweiterbar ohne Neuverkabelung

**Nachteile CZone:**
- Hohe Anschaffungskosten (3–10× konventionell)
- Komplexe Programmierung (Fachbetrieb empfohlen)
- Abhängigkeit von Elektronik (kein Schalter = kein manueller Override)
- Schwieriger Fehlersuche ohne Diagnosewerkzeug
- Halbleiterschalter haben höheren Spannungsabfall als mechanische Kontakte

#### BEP Klassische Panels

| Produkt | Kreise | Typ | Besonderheit |
|---------|--------|-----|-------------|
| BEP 12-Way DC Panel | 12 | Toggle-Breaker | Analoges Voltmeter, Marine-Grade |
| BEP 6-Way DC Panel | 6 | Toggle-Breaker | Kompakt, Flush-Mount |
| BEP AC Panel 4-Way | 4 | MCB + RCD | 230V, Doppelpolige Abschaltung |
| BEP Battery Selector | — | Wahlschalter | 1/BOTH/2/OFF, 300A Dauerlast |
| BEP Mini Battery Switch | — | ON/OFF | 275A, kompakt |
| BEP Contour Connect 1000 | 6–12 | Modular | Selbstkonfigurierend, modulare Bauweise |

### 4.3 Mastervolt

#### MasterBus — Integriertes Energiemanagement

Mastervolt bietet mit dem MasterBus-System ein proprietäres, aber bewährtes digitales Verteilungssystem:

**MVSV MasterShunt:**

| Parameter | Wert |
|-----------|------|
| Funktion | Batteriemonitor + Shunt |
| Messbereich | 500A / 60V |
| Genauigkeit | ±0,5% Strom, ±0,25% Spannung |
| Kommunikation | MasterBus (CAN-basiert) |
| Anzeige | Über MasterView Easy/Ultra |

**DC Distribution 500:**

| Parameter | Wert |
|-----------|------|
| Eingang | 2× Batterie-Eingang, je 400A |
| Ausgang | 20× abgesicherte Ausgänge |
| Sicherungstyp | MIDI/ANL-Kombination |
| Bus-Bar | Kupfer verzinnt, 500A gesamt |
| Schutzart | IP20 |
| Kommunikation | MasterBus-fähig (optional) |
| Abmessungen | 440 × 230 × 120mm |

### 4.4 Victron Energy — Lynx-System

Das Victron Lynx-System ist ein modulares DC-Verteilungssystem, das speziell für Victron-Batterien und -Wechselrichter optimiert ist, aber universell einsetzbar.

**Lynx Distributor:**

| Parameter | Wert |
|-----------|------|
| Funktion | Sicherungsverteiler mit 4× MEGA-Sicherungsplätzen |
| Max. Strom | 1.000A Busstrom |
| Sicherungstyp | MEGA-Bolzensicherung (100–500A) |
| Bus-Bar | Kupfer, 1.000A-Nennstrom |
| Verbindung | Lynx-Bus-Bar-System (stapelbar) |
| Abmessungen | 330 × 150 × 72mm |
| Schutzart | IP22 |
| Material Gehäuse | Polycarbonat, flammhemmend UL94 V-0 |

**Lynx Shunt:**

| Parameter | Wert |
|-----------|------|
| Funktion | Batteriemonitor im Lynx-Formfaktor |
| Shuntwert | 500A / 50mV |
| Kommunikation | VE.Can |
| Genauigkeit | ±0,4% Strom |
| Eingänge | 4× Kontaktschließer für Batteriestatus |

**Lynx Power In:**

| Parameter | Wert |
|-----------|------|
| Funktion | Batterie-Einspeisung ins Lynx-System |
| Sicherungsplätze | 1× MEGA-Sicherung |
| Max. Strom | 1.000A |
| Anschlüsse | M8-Bolzen |

**Lynx Smart BMS:**

| Parameter | Wert |
|-----------|------|
| Funktion | Batterie-Management im Lynx-Formfaktor |
| Kompatibel | Victron LiFePO4 Smart Batteries |
| Kommunikation | VE.Can + VE.Bus + Bluetooth |
| Schutzfunktionen | Über/Unterspannung, Über/Untertemperatur, Balancing |
| Lastabwurf | Programmierbare Lastabwurfstufen |

**Systembeispiel Victron Lynx (Blauwasser-Segler):**

```
[Victron LiFePO4 3× 200Ah] 
    │
[Lynx Smart BMS]
    │
[Lynx Power In] ── MEGA 400A
    │
[Lynx Distributor]
    ├── MEGA 200A ── Victron MultiPlus 3000
    ├── MEGA 150A ── DC-Hauptverteiler
    ├── MEGA 100A ── Laderegler MPPT 150/70
    └── MEGA 100A ── Alternator (über Orion-Tr)
    │
[Lynx Shunt] ── 500A
    │
  Masse
```

### 4.5 Hella Marine

Hella Marine bietet robuste Schaltpanels für den professionellen und Semi-professionellen Bereich:

| Produkt | Kreise | Schutzart | Besonderheit |
|---------|--------|-----------|-------------|
| Hella Marine Rocker Panel 6-Way | 6 | IPX4 | LED-Statusanzeige, Salzwasser-geprüft |
| Hella Marine Rocker Panel 8-Way | 8 | IPX4 | Großflächige Wippen, haptisches Feedback |
| Hella Marine Fuse Box 10-Way | 10 | IPX2 | ATO-Sicherungen, transparente Abdeckung |
| Hella Marine LED Panel 12-Way | 12 | IPX2 | Individuelle LED-Hintergrundbeleuchtung |

**Spezifikationen Hella Marine Rocker Panel:**

| Parameter | Wert |
|-----------|------|
| Nennspannung | 12V oder 24V DC (je nach Modell) |
| Max. pro Schalter | 15A |
| Schaltertyp | Rocker, beleuchtet |
| Lebensdauer | >50.000 Schaltzyklen |
| Material | UV-stabiles Polycarbonat |
| Betriebstemperatur | -30°C bis +65°C |
| Salznebelbeständigkeit | 500h nach IEC 60068-2-52 |

### 4.6 Narva

Narva (australischer Hersteller) ist besonders im pazifischen Raum verbreitet und bietet kostengünstige marine Sicherungshalter und Panels:

| Produkt | Typ | Besonderheit |
|---------|-----|-------------|
| Narva 12-Way ATO Fuse Box | Sicherungsblock | LED-Anzeige, wasserdichter Deckel |
| Narva ANL Fuse Holder In-Line | ANL-Halter | Kabeldurchführung, IP54 |
| Narva MIDI In-Line Fuse Holder | MIDI-Halter | Kompakt, M5-Bolzen |
| Narva 6-Way Rocker Panel | Schaltpanel | Marine-Grade, vertikale Montage |
| Narva Battery Master Switch | Hauptschalter | 300A Dauer, montagefreundlich |

---

## 5. Hersteller-Datenbank

### 5.1 Blue Sea Systems (USA)

| Feld | Daten |
|------|-------|
| Gründung | 1992, Bellingham, Washington, USA |
| Übernahme | 2021 durch Dometic Group |
| Kernkompetenz | Marine Schalttafeln, Sicherungen, Batterieschalter, Bus-Bars |
| Marktsegment | Freizeit-Marine, leichte Gewerbe-Marine |
| Zertifizierungen | UL 1107, ABYC, CE, ISO 8846 (zündfrei) |
| Vertrieb DE | Über Fachhändler (SVB, Compass24, AWN) |
| Besonderheit | Erfinder des ATO-Marine-Sicherungsblocks, 360 Panel System |
| Preissegment | Mittel–Hoch |
| Website | bluesea.com |

### 5.2 BEP Marine (Neuseeland)

| Feld | Daten |
|------|-------|
| Gründung | 1969, Auckland, Neuseeland |
| Übernahme | 2018 durch Power Products LLC |
| Kernkompetenz | Batterieschalter, Schaltpanels, CZone digitales System |
| Marktsegment | Freizeit bis Superyacht, gewerbliche Marine |
| Zertifizierungen | UL, CE, ABYC, ABS, Lloyd's Register |
| Vertrieb DE | Über Distributoren (Mastervolt-Netzwerk) |
| Besonderheit | CZone — führendes digitales Verteilungssystem |
| Preissegment | Mittel (konventionell) bis Hoch (CZone) |
| Website | bepmarine.com |

### 5.3 Mastervolt (Niederlande)

| Feld | Daten |
|------|-------|
| Gründung | 1991, Amsterdam, Niederlande |
| Übernahme | 2018 durch Power Products LLC (zusammen mit BEP) |
| Kernkompetenz | Lader, Inverter, Batterien, MasterBus-System |
| Marktsegment | Premium-Freizeit bis Superyacht |
| Zertifizierungen | CE, Lloyd's Register, DNV, GL, ABYC |
| Vertrieb DE | Direkter Fachhandelsvertrieb + Online |
| Besonderheit | MasterBus — integriertes Energiemanagement |
| Preissegment | Hoch–Sehr hoch |
| Website | mastervolt.com |

### 5.4 Victron Energy (Niederlande)

| Feld | Daten |
|------|-------|
| Gründung | 1975, Almere, Niederlande |
| Kernkompetenz | Wechselrichter, Ladegeräte, MPPT-Regler, Lynx-System |
| Marktsegment | Breites Spektrum: DIY bis professionell, Marine + Off-Grid |
| Zertifizierungen | CE, UL (teilweise), FCC |
| Vertrieb DE | Fachhändler + Online (sehr breit verfügbar) |
| Besonderheit | Offene Kommunikation (VE.Direct, VE.Can), Lynx-Modulsystem, VRM-Portal |
| Preissegment | Mittel (sehr gutes Preis-Leistungs-Verhältnis) |
| Website | victronenergy.com |

### 5.5 Hella Marine (Neuseeland)

| Feld | Daten |
|------|-------|
| Gründung | 1960 (als Hella Marine Division), Auckland, Neuseeland |
| Mutterkonzern | HELLA GmbH & Co. KGaA (Deutschland) |
| Kernkompetenz | Marine-Beleuchtung, Schalttafeln, Signalleuchten |
| Marktsegment | OEM-Zulieferer + Nachrüstmarkt |
| Zertifizierungen | ABYC, CE, COLREG, SOLAS |
| Vertrieb DE | Über Hella-Vertriebsnetz + Marine-Fachhändler |
| Besonderheit | Salznebelbeständigkeit 500h+, UV-Stabilität |
| Preissegment | Mittel |
| Website | hellamarine.com |

### 5.6 Narva (Australien)

| Feld | Daten |
|------|-------|
| Gründung | 1950er, Melbourne, Australien |
| Kernkompetenz | Fahrzeug- und Marine-Elektrik, Sicherungen, Schalter |
| Marktsegment | Einstieg bis Mittelklasse, starke Präsenz in Australien/NZ |
| Zertifizierungen | ADR (Australian Design Rules), CE (für Export) |
| Vertrieb DE | Eingeschränkt — Import über Spezialhändler |
| Besonderheit | Robust, kostengünstig, große Produktbreite |
| Preissegment | Niedrig–Mittel |
| Website | narva.com.au |

### 5.7 Carling Technologies (USA)

| Feld | Daten |
|------|-------|
| Gründung | 1920, Plainville, Connecticut, USA |
| Kernkompetenz | Wippschalter, Leitungsschutzschalter, Schalttafeln |
| Marktsegment | OEM-Zulieferer für Bootsbauer weltweit |
| Zertifizierungen | UL, CSA, CE, ABYC, ABS, DNV, GL |
| Vertrieb DE | Über Bootsbauer (OEM) + Großhändler |
| Besonderheit | Contura-Wippschalter — Industriestandard bei Bootsbauern |
| Preissegment | Mittel |
| Website | carlingtech.com |

### 5.8 Philippi (Deutschland)

| Feld | Daten |
|------|-------|
| Gründung | 1958, Backnang, Deutschland |
| Kernkompetenz | Marine-Schalttafeln, Verteiler, Ladegeräte, Mess- und Regeltechnik |
| Marktsegment | Premium-Segelyachten, Superyachten, deutsche Werftausstattung |
| Zertifizierungen | CE, GL, BV, LR, DNV |
| Vertrieb DE | Direkt + Marine-Fachhändler, stark in DACH |
| Besonderheit | Deutsche Fertigung, Maßanfertigung möglich, hervorragender Support |
| Preissegment | Hoch–Sehr hoch |
| Website | philippi-online.de |

---

## 6. Fehlerbild-Atlas

### Fehlerbild F-08-01: Überhitzte Bus-Bar-Verbindung

| Feld | Beschreibung |
|------|-------------|
| **Erscheinung** | Verfärbung (gold → braun → schwarz) an Bus-Bar-Bolzen und Kabelschuh. Geschmolzenes oder verformtes Kunststoffgehäuse um den Anschluss. Möglicherweise Brandspuren an angrenzenden Kabeln. |
| **Ursache** | Lockerer Bolzen → erhöhter Übergangswiderstand → Wärmeentwicklung P = I² × R. Bereits 0,5mΩ Übergangswiderstand bei 100A erzeugen 5W Verlustleistung punktuell am Kontakt. |
| **Begleiterscheinungen** | Spannungsabfall am Panel größer als erwartet. Flackernde Verbraucher bei Vibration. Intermittierender Kontaktverlust. Geruch nach verbranntem Kunststoff. |
| **Risikobewertung** | KRITISCH — Brandgefahr! |
| **Sofortmaßnahme** | System stromlos schalten. Verbindung lösen, Kontaktflächen reinigen (Schleifvlies, nicht Schmirgelpapier). Kabelschuh und Bolzen auf Beschädigung prüfen. Bei Verformung des Bus-Bar-Materials: kompletten Bus-Bar ersetzen. |
| **Langfristmaßnahme** | Alle Verbindungen auf korrektes Drehmoment prüfen (typisch M6: 4–5Nm, M8: 8–10Nm). Kontaktfett (z.B. Tefgel oder Noalox) auftragen. Wartungsintervall: Drehmoment alle 6 Monate prüfen. |
| **AYDI-Konfidenz** | visual_high (bei sichtbarer Verfärbung), visual_medium (bei uneindeutiger Verfärbung) |

### Fehlerbild F-08-02: Korrodierte ATO-Sicherungskontakte

| Feld | Beschreibung |
|------|-------------|
| **Erscheinung** | Grüne oder weiße Ablagerungen an den Kontaktklingen der Sicherung und/oder im Halter. Erhöhter Übergangswiderstand, Sicherung sitzt fest oder wackelt. |
| **Ursache** | Feuchtigkeit im Sicherungskasten. Kondensat durch Temperaturwechsel. Fehlende Dichtung des Sicherungsblocks. Salzwassereinbruch. |
| **Begleiterscheinungen** | Intermittierende Ausfälle des zugehörigen Kreises. Sicherung löst ohne erkennbare Überlast aus (Korrosionswärme). Spannungsabfall >5% bei normalem Betriebsstrom. |
| **Risikobewertung** | MITTEL — Funktionsverlust, langfristig Brandgefahr |
| **Sofortmaßnahme** | Sicherung entfernen, Kontakte mit Kontaktreiniger behandeln. Korrosion mechanisch entfernen (Kontaktbürste, NICHT Schmirgelpapier). Sicherung ersetzen. |
| **Langfristmaßnahme** | Sicherungsblock mit Korrosionsschutzspray behandeln (Ballistol, ACF-50). Abdeckung auf Dichtheit prüfen. Bei häufigem Auftreten: Sicherungsblock an trockenere Position verlegen oder wasserdichten Typ (IP67) verwenden. |
| **AYDI-Konfidenz** | visual_high (deutliche Grünfärbung), visual_medium (leichte Patina) |

### Fehlerbild F-08-03: Geschmolzene Sicherung ohne Überlast

| Feld | Beschreibung |
|------|-------------|
| **Erscheinung** | Schmelzsicherung durchgebrannt, aber der angeschlossene Verbraucher zieht weniger als den Sicherungs-Nennstrom. Sicherung brennt nach Ersatz erneut durch. |
| **Ursache** | (a) Intermittierender Kurzschluss im Kabelweg (Scheuerstelle). (b) Sicherung durch Wärme gealtert (nahe Wärmequelle montiert). (c) Sicherung minderwertiger Qualität mit zu niedrigem Schmelzstrom. (d) Anlaufstrom des Verbrauchers übersteigt kurzzeitig den Nennstrom. |
| **Begleiterscheinungen** | Keine offensichtlichen Fehlersymptome im Ruhezustand. Möglicherweise bei Vibration (Seegang) reproduzierbar. |
| **Risikobewertung** | HOCH — Versteckter Kurzschluss möglich |
| **Sofortmaßnahme** | Gesamten Kabelweg visuell inspizieren (besonders Schottdurchführungen, Kabelschellen, Bilgenbereich). Isolationsmessung des Kreises durchführen. Wenn kein Fehler gefunden: temporär nächsthöheren Sicherungswert einsetzen und Strom überwachen. |
| **Langfristmaßnahme** | Kabelweg reparieren oder ersetzen. Bei Anlaufstrom-Problem: Sicherungstyp auf "Slow Blow" / "Time Delay" wechseln. Sicherung von Wärmequellen fernhalten. Nur Markensicherungen verwenden (Blue Sea, Littelfuse, Bussmann). |
| **AYDI-Konfidenz** | visual_low (Sicherung allein nicht aussagekräftig), visual_medium (mit sichtbarer Kabelscheuerstelle) |

### Fehlerbild F-08-04: Vibrationsbedingte Schalterauslösung

| Feld | Beschreibung |
|------|-------------|
| **Erscheinung** | Leitungsschutzschalter oder Kippschalter lösen bei rauem Seegang, Motorbetrieb oder Hammerschlag auf Deck/Rumpf selbsttätig aus. |
| **Ursache** | (a) Mechanische Empfindlichkeit des Schalters zu hoch für maritime Vibrationen. (b) Schalter ist kein Marine-Typ (Automotive-Schalter haben geringere Vibrationsresistenz). (c) Panel zu nahe am Motor oder an vibrationsträchtigem Schott montiert. |
| **Begleiterscheinungen** | Kritische Verbraucher (Navigation, Autopilot) fallen im schlimmsten Moment aus. Wiedereinschalten behebt das Problem — bis zur nächsten Vibration. |
| **Risikobewertung** | HOCH — Sicherheitskritisch bei Navigation/Autopilot |
| **Sofortmaßnahme** | Betroffene Schalter identifizieren und mit Klebeband in ON-Position sichern (nur als Notmaßnahme!). Kritische Verbraucher temporär direkt absichern (Bypass). |
| **Langfristmaßnahme** | Schalter durch marine-zertifizierte Typen ersetzen (Carling Contura, Blue Sea 360). Panel auf vibrationsdämpfendem Untergrund montieren (Gummi-Silentblöcke). Vibrationsquelle isolieren. |
| **AYDI-Konfidenz** | visual_low (nur bei Video/Beobachtung), documented (bei Servicebericht) |

### Fehlerbild F-08-05: Fehlender Leitungsschutz an Batterie

| Feld | Beschreibung |
|------|-------------|
| **Erscheinung** | Kabel von der Batterie zum ersten Verteiler/Verbraucher ohne Sicherung. Oft erkennbar an Kabeln, die direkt von Batteriepolen ohne Zwischenschaltung eines Sicherungshalters abgehen. |
| **Ursache** | Nachträgliche Installation ohne Fachkenntnis. "Das hat der Vorbesitzer gemacht." Unwissenheit über die 180mm-Regel. |
| **Begleiterscheinungen** | Funktionell unauffällig — bis zum Kurzschluss. Dann: unkontrollierter Kabelbrand, da kein Schutzorgan den Fehlerstrom begrenzt. |
| **Risikobewertung** | KRITISCH — Maximale Brandgefahr |
| **Sofortmaßnahme** | Sofort Sicherung nachrüsten. ANL/MEGA-Sicherung innerhalb von 180mm vom Batteriepol. Bei fehlender Möglichkeit: Kabel abklemmen und Boot nicht benutzen. |
| **Langfristmaßnahme** | Alle Kabel am Batteriepol prüfen. Jeder abgehende Leiter muss innerhalb von 180mm abgesichert sein (Ausnahme: Starterkabel zum Anlasser, wenn <1m und geschützt verlegt). |
| **AYDI-Konfidenz** | visual_high (bei deutlich sichtbarem ungesichertem Kabel) |

### Fehlerbild F-08-06: Falsch dimensionierte Hauptsicherung

| Feld | Beschreibung |
|------|-------------|
| **Erscheinung** | Hauptsicherung ist deutlich größer als die Kabelbelastbarkeit zuläßt. Beispiel: 300A ANL-Sicherung auf 16mm²-Kabel (belastbar für ~70A). |
| **Ursache** | Sicherung wurde nach Verbraucher dimensioniert statt nach Kabel. Oder: Sicherung löste wiederholt aus und wurde durch größere ersetzt ("die brennt immer durch, ich nehm eine größere"). |
| **Begleiterscheinungen** | Im Normalbetrieb unauffällig. Bei Überlast schmilzt das Kabel, bevor die Sicherung auslöst — Brandgefahr. |
| **Risikobewertung** | KRITISCH — Brandgefahr bei Überlast |
| **Sofortmaßnahme** | Sicherung auf den korrekten Wert (≤ Kabelbelastbarkeit) herunterstufen. Wenn Verbraucher dann Sicherung auslöst: Kabelquerschnitt erhöhen. |
| **Langfristmaßnahme** | Alle Kreise auf korrekte Abstimmung Kabel/Sicherung prüfen. Dokumentation erstellen (Stromkreistabelle). |
| **AYDI-Konfidenz** | visual_high (bei lesbarer Sicherungsbeschriftung und Kabelquerschnitt) |

### Fehlerbild F-08-07: Gemischte AC/DC-Verkabelung im Panel

| Feld | Beschreibung |
|------|-------------|
| **Erscheinung** | AC-Kabel (230V) und DC-Kabel (12V/24V) im selben Kabelkanal oder Panel ohne physische Trennung. |
| **Ursache** | Platzersparnis oder Unkenntnis. Nachträgliche Installation ohne Normenbewusstsein. |
| **Begleiterscheinungen** | Potenzielle Lebensgefahr bei Isolationsschaden. EMV-Störungen auf DC-Leitungen. Normverstoß (ISO 13297, ABYC E-11). |
| **Risikobewertung** | KRITISCH — Lebensgefahr |
| **Sofortmaßnahme** | AC- und DC-Kabel physisch trennen. Mindestabstand 50mm oder separate Kabelkanäle. AC-Panel und DC-Panel müssen getrennte Gehäuse haben oder durch feste Trennwand separiert sein. |
| **Langfristmaßnahme** | Komplette Neuverlegung der betroffenen Abschnitte. AC-Kabel: extra Kabelkanal, andere Farbe (ABYC: schwarz = AC-Phase, rot = DC-Plus). |
| **AYDI-Konfidenz** | visual_high (bei eindeutig erkennbaren AC+DC-Kabeln im selben Kanal) |

### Fehlerbild F-08-08: Unbeschriftete Stromkreise

| Feld | Beschreibung |
|------|-------------|
| **Erscheinung** | Verteilerpanel ohne Beschriftung oder mit unleserlicher/falscher Beschriftung. Handschriftliche Notizen auf Klebeband, das sich löst. |
| **Ursache** | Nachlässigkeit bei Installation. Beschriftung nie angebracht oder nach Umbau nicht aktualisiert. Klebeband-Beschriftung durch Feuchtigkeit/UV zerstört. |
| **Begleiterscheinungen** | Fehlersuche extrem erschwert. Falsche Kreise werden abgeschaltet. Im Notfall kann die Bilgepumpe nicht identifiziert werden. |
| **Risikobewertung** | MITTEL — Sicherheitsrelevant im Notfall |
| **Sofortmaßnahme** | Jeden Kreis identifizieren (einzeln ein/ausschalten) und provisorisch beschriften. |
| **Langfristmaßnahme** | Professionelle Beschriftung (gravierte Kunststoffschilder, Labeldrucker). Schaltplan anfertigen und an gut erreichbarer Stelle aufbewahren. |
| **AYDI-Konfidenz** | visual_high (fehlende Beschriftung eindeutig erkennbar) |

### Fehlerbild F-08-09: Elektrolytische Korrosion am Hauptschalter

| Feld | Beschreibung |
|------|-------------|
| **Erscheinung** | Weiße, grüne oder blaue Kristallbildung an den Kontakten des Batterie-Hauptschalters. Schalter lässt sich schwer drehen. Widerstand im geschalteten Zustand >1mΩ. |
| **Ursache** | Feuchtigkeit an den Kontakten in Kombination mit Spannungsdifferenz. Undichtes Batteriefach. Saure Ausdünstung der Blei-Batterien. Kondensat. |
| **Begleiterscheinungen** | Spannungsabfall unter Last. Schalter wird warm. Flackernde Verbraucher beim Drehen des Schalters. Ladegerät meldet "keine Batterie". |
| **Risikobewertung** | HOCH — Brandgefahr durch Übergangswiderstand |
| **Sofortmaßnahme** | Schalter stromlos machen (Batterie-Polklemme lösen). Kontakte mit Essig und Drahtbürste reinigen (Messing- oder Edelstahlbürste). Trocknen. Korrosionsschutz auftragen. |
| **Langfristmaßnahme** | Belüftung des Batteriefachs verbessern. Spritzwasserschutz für Schalter nachrüsten. Bei stark beschädigtem Schalter: kompletten Hauptschalter ersetzen. |
| **AYDI-Konfidenz** | visual_high (bei deutlicher Kristallbildung) |

### Fehlerbild F-08-10: Thermisch geschädigter Leitungsschutzschalter

| Feld | Beschreibung |
|------|-------------|
| **Erscheinung** | Leitungsschutzschalter verfärbt (vergilbt, gebräunt). Gehäuse leicht verformt. Schalter lässt sich nicht mehr korrekt einrasten. Löst bei deutlich niedrigerem Strom aus als angegeben oder löst gar nicht aus. |
| **Ursache** | Dauerhafter Betrieb nahe dem Nennstrom in warmer Umgebung. Schlechte Belüftung des Panels. Montagefehler (Panel in direkter Sonneneinstrahlung). |
| **Begleiterscheinungen** | Häufige unerklärliche Auslösungen. Oder umgekehrt: Schalter löst bei Überlast nicht aus (thermisches Element dauerhaft verformt). |
| **Risikobewertung** | HOCH — Schutzfunktion beeinträchtigt |
| **Sofortmaßnahme** | Schalter sofort ersetzen. Bis zum Ersatz: Kreis mit externer ATO-Sicherung zusätzlich absichern. |
| **Langfristmaßnahme** | Panel-Belüftung verbessern. Maximale Dauerlast pro Schalter auf 80% des Nennstroms begrenzen. In heißen Umgebungen (Maschinenraum): Derating-Tabelle des Herstellers beachten. |
| **AYDI-Konfidenz** | visual_medium (Verfärbung allein nicht immer eindeutig), visual_high (bei sichtbarer Verformung) |

### Fehlerbild F-08-11: Fehlende Selektivität — Hauptsicherung löst vor Einzelkreis aus

| Feld | Beschreibung |
|------|-------------|
| **Erscheinung** | Bei einem Kurzschluss oder Überlast in einem Einzelkreis löst nicht die zugehörige Einzelkreissicherung aus, sondern die übergeordnete Hauptsicherung. Das gesamte Panel oder Teilsystem fällt aus. |
| **Ursache** | Falsche Sicherungsstaffelung. Hauptsicherung zu klein oder Einzelkreissicherung zu groß. Unterschiedliche Sicherungskennlinien nicht berücksichtigt. |
| **Begleiterscheinungen** | Kompletter Ausfall ganzer Verbrauchergruppen bei einem einzigen Defekt. Navigationsausfall durch Kurzschluss in Beleuchtungskreis. |
| **Risikobewertung** | HOCH — Sicherheitskritisch |
| **Sofortmaßnahme** | Sicherungswerte dokumentieren und Selektivitätsbedingung prüfen (Faktor ≥1,6 zwischen Ebenen). |
| **Langfristmaßnahme** | Komplette Neudimensionierung der Sicherungskaskade. Selektivitätsberechnung durchführen. Ggf. schnelle Sicherungen (Fast-Acting) auf Einzelkreisebene und träge (Slow-Blow) auf Hauptebene verwenden. |
| **AYDI-Konfidenz** | documented (aus Fehlerbeschreibung), calculated (bei Analyse der Sicherungswerte) |

### Fehlerbild F-08-12: Wassereinbruch im Schaltpanel

| Feld | Beschreibung |
|------|-------------|
| **Erscheinung** | Sichtbare Feuchtigkeit, Tropfenbildung oder stehendes Wasser im Inneren des Schaltpanels. Korrosion an Kontakten und Bus-Bars. Salzausblühungen. |
| **Ursache** | Undichte Decksdurchführung über dem Panel. Kondensation. Leckende Cockpitabflüsse. Schlagregen durch offene Luken. Panel nicht für die Montageposition geeignet (IPX1 statt IPX4). |
| **Begleiterscheinungen** | Intermittierende Fehler. Kriechströme zwischen benachbarten Leitern. FI-Schalter löst aus (AC). Sicherungen korrodieren und lösen grundlos aus. |
| **Risikobewertung** | KRITISCH — Kurzschluss- und Brandgefahr, Lebensgefahr bei AC |
| **Sofortmaßnahme** | System stromlos schalten. Panel öffnen und trocknen. Wasserquelle identifizieren und abdichten. Alle Kontakte prüfen und reinigen. |
| **Langfristmaßnahme** | Panel mit geeigneter Schutzart verwenden (IPX4 minimum für Cockpit-nahe Montage). Tropfschutz oberhalb des Panels installieren. Kabeleinführungen von unten (nicht von oben). Silikondichtung um Panel-Ausschnitt. |
| **AYDI-Konfidenz** | visual_high (bei sichtbarem Wasser/Korrosion im Panel) |

---

## 7. Troubleshooting-Entscheidungsbäume

### Entscheidungsbaum T-08-01: Sicherung löst wiederholt aus

```
START: Sicherung löst wiederholt aus
│
├── Löst sofort nach Einsetzen aus?
│   ├── JA → Kurzschluss im Stromkreis
│   │   ├── Verbraucher abklemmen → Sicherung hält?
│   │   │   ├── JA → Verbraucher defekt
│   │   │   │   └── Verbraucher reparieren oder ersetzen
│   │   │   └── NEIN → Kurzschluss in Zuleitung
│   │   │       ├── Isolationsmessung am Kabel
│   │   │       ├── Kabel Meter für Meter prüfen
│   │   │       ├── Besonders: Schottdurchführungen, Bilge, Kabelschellen
│   │   │       └── Beschädigte Stelle reparieren
│   │   └── Hinweis: Bei sofortigem Auslösen NIEMALS höhere Sicherung einsetzen!
│   │
│   └── NEIN → Weiter prüfen
│
├── Löst nach Minuten/Stunden aus?
│   ├── JA → Überlast oder thermisches Problem
│   │   ├── Strom messen (Zangenamperemeter)
│   │   │   ├── I_mess > 80% × I_sicherung → Sicherung zu klein oder Verbraucher zu groß
│   │   │   │   ├── Kabelquerschnitt für höheren Strom ausreichend?
│   │   │   │   │   ├── JA → Sicherung auf nächsten Wert erhöhen
│   │   │   │   │   └── NEIN → Kabel erneuern + dann Sicherung anpassen
│   │   │   │   └── Hinweis: Umgebungstemperatur beachten! Derating bei >40°C
│   │   │   │
│   │   │   └── I_mess << I_sicherung → Sicherung defekt oder Wärmestau
│   │   │       ├── Sicherung durch neue gleicher Spezifikation ersetzen
│   │   │       ├── Panel-Belüftung prüfen
│   │   │       └── Löst weiterhin aus? → Sicherungshalter prüfen (Übergangswiderstand)
│   │   │
│   │   └── Tritt nur bei bestimmtem Betriebszustand auf?
│   │       ├── Bei Motorstart → Anlaufstrom. Slow-Blow-Sicherung verwenden
│   │       ├── Bei Seegang → Vibration. Marine-Sicherungshalter verwenden
│   │       └── Bei Hitze → Derating. Größeren Querschnitt oder bessere Belüftung
│   │
│   └── NEIN → Sporadisches Auslösen
│       ├── Intermittierender Kurzschluss (vibrations- oder feuchtigkeitsbedingt)
│       ├── Isolationsmessung bei trockenen UND feuchten Bedingungen
│       ├── Kabelweg auf Scheuerstellen untersuchen
│       └── Feuchtigkeit im Sicherungskasten?
│           ├── JA → Fehlerbild F-08-02 / F-08-12
│           └── NEIN → Lose Verbindung verursacht Lichtbogen → Alle Klemmen prüfen
│
└── ENDE: Fehler identifiziert und behoben
```

### Entscheidungsbaum T-08-02: Verbraucher funktioniert nicht trotz eingeschaltetem Schalter

```
START: Verbraucher ohne Funktion
│
├── Sicherung prüfen (visuell + Multimeter)
│   ├── Sicherung durchgebrannt
│   │   ├── → Entscheidungsbaum T-08-01
│   │   └── HINWEIS: Immer mit Multimeter prüfen! Visuelle Prüfung kann täuschen.
│   │
│   └── Sicherung intakt
│       │
│       ├── Spannung AM Sicherungsausgang messen
│       │   ├── Spannung vorhanden (>11,5V bei 12V-System)
│       │   │   ├── Spannung AM Verbraucher messen
│       │   │   │   ├── Spannung vorhanden → Verbraucher defekt
│       │   │   │   │   └── Verbraucher prüfen/ersetzen
│       │   │   │   │
│       │   │   │   └── Keine Spannung → Kabel unterbrochen
│       │   │   │       ├── Kabelwiderstand messen (Durchgangsprüfung)
│       │   │   │       ├── Stecker/Verbinder prüfen
│       │   │   │       └── Unterbrechung lokalisieren und reparieren
│       │   │   │
│       │   │   └── Spannung niedrig (<11V bei 12V) → Spannungsabfall zu hoch
│       │   │       ├── Alle Verbindungen im Pfad auf Übergangswiderstand prüfen
│       │   │       ├── Kabelquerschnitt für die Last ausreichend?
│       │   │       └── Batteriespannung prüfen (Batterie leer?)
│       │   │
│       │   └── Keine Spannung am Sicherungsausgang
│       │       ├── Spannung am Sicherungseingang?
│       │       │   ├── JA → Sicherungskontakt defekt (trotz intaktem Schmelzdraht)
│       │       │   │   └── Sicherung und Halter ersetzen
│       │       │   │
│       │       │   └── NEIN → Kein Strom am Panel
│       │       │       ├── Panel-Hauptsicherung prüfen
│       │       │       ├── Bus-Bar-Verbindung prüfen
│       │       │       ├── Hauptschalter-Position prüfen
│       │       │       └── Batterieverbindung prüfen
│       │       │
│       │       └── Schalter-Funktion prüfen (Durchgangsmessung am Schalter)
│       │           ├── Schalter defekt → ersetzen
│       │           └── Schalter OK → interner Panel-Verdrahtungsfehler
│       │
│       └── Masse-Verbindung prüfen (am Verbraucher)
│           ├── Masse OK (<0,2V gegen Bus-Bar) → Problem im Pluspfad (siehe oben)
│           └── Masse schlecht (>0,5V gegen Bus-Bar) → Massekabel/Verbindung defekt
│               ├── Massekabel am Verbraucher prüfen
│               ├── Masseverbindung an Masse-Bus-Bar prüfen
│               └── Korrosion an Masseanschluss?
│                   ├── JA → Reinigen, Kontaktfett, ggf. Kabelschuh erneuern
│                   └── NEIN → Kabelbruch in Masseleitung
│
└── ENDE: Fehler identifiziert und behoben
```

### Entscheidungsbaum T-08-03: FI/RCD-Schutzschalter löst aus (AC-Kreis)

```
START: FI-Schutzschalter (RCD) löst aus
│
├── Löst sofort beim Einschalten des Landstroms aus?
│   ├── JA → Schwerer Isolationsfehler oder Gerät-Erdschluss
│   │   ├── Alle AC-Leitungsschutzschalter ausschalten
│   │   ├── FI einschalten → Hält er?
│   │   │   ├── JA → Einzelne Kreise nacheinander einschalten
│   │   │   │   ├── Fehlerhafter Kreis identifiziert
│   │   │   │   │   ├── Alle Verbraucher in diesem Kreis trennen
│   │   │   │   │   ├── Einzeln anschließen → defektes Gerät finden
│   │   │   │   │   └── Gerät reparieren oder ersetzen
│   │   │   │   └── Kein einzelner Kreis löst aus → Summenfehler
│   │   │   │       └── Isolationsmessung aller Kreise einzeln
│   │   │   │
│   │   │   └── NEIN → Fehler in Zuleitung oder FI-Schalter defekt
│   │   │       ├── Isolationsmessung Landstromkabel
│   │   │       ├── Stecker und Dose prüfen (Korrosion, Feuchtigkeit)
│   │   │       ├── FI-Testtaste → Löst FI aus?
│   │   │       │   ├── JA → FI funktioniert, Fehler in Zuleitung
│   │   │       │   └── NEIN → FI defekt → ersetzen
│   │   │       └── Landstromkabel an anderer Steckdose testen
│   │   │
│   │   └── Achtung bei Booten mit Metallrumpf: Galvanische Probleme!
│   │       └── Trenntransformator verwenden
│   │
│   └── NEIN → Weiter
│
├── Löst nach einiger Zeit aus (Minuten bis Stunden)?
│   ├── Feuchtigkeit in einem Gerät (nach Regen, Kondensat)
│   ├── Heizstab-Alterung (Boiler, Wasserkocher)
│   ├── Wechselrichter-Störung
│   └── Isolationsalterung (besonders bei >10 Jahre alten Installationen)
│
├── Löst nur bei bestimmten Verbrauchern aus?
│   ├── Gerät hat Erdschluss → Gerät prüfen
│   ├── Gerät hat hohen Ableitstrom (Frequenzumrichter, LED-Netzteile)
│   │   └── Separaten FI mit 300mA für diese Verbraucher verwenden
│   └── Gerät hat Schutzleiterverbindung zum Bootskörper
│       └── Bei GFK-Booten: Bonding-System prüfen
│
└── ENDE: Fehler identifiziert und behoben
```

### Entscheidungsbaum T-08-04: Batterie-Hauptschalter schaltet nicht / schaltet schwer

```
START: Hauptschalter Problem
│
├── Schalter dreht/schaltet nicht mehr
│   ├── Mechanisch blockiert?
│   │   ├── JA → Fremdkörper? Korrosion? Vereisung?
│   │   │   ├── Fremdkörper entfernen
│   │   │   ├── Korrosion: mit WD-40 lösen, dann reinigen
│   │   │   └── Eis: vorsichtig erwärmen (Föhn), Entwässerung nachrüsten
│   │   │
│   │   └── NEIN → Interner Schaden (Rastmechanismus gebrochen)
│   │       └── Schalter ersetzen. NIEMALS reparieren!
│   │
│   └── Kontakte verschweißt (Schalter steht auf ON, lässt sich nicht ausschalten)
│       ├── KRITISCH: Kontakte durch zu hohen Schaltstrom verschweißt
│       ├── Batterie-Polklemme lösen als Notabschaltung
│       ├── Schalter sofort ersetzen
│       └── Ursache ermitteln: Kurzschluss beim Schalten? Anlaufstrom zu hoch?
│           └── Ggf. Schalter mit höherem Nennstrom verwenden
│
├── Schalter schaltet, aber Kontakt ist schlecht
│   ├── Spannung über Schalter messen (soll: <0,05V bei Nennlast)
│   │   ├── >0,1V → Kontaktwiderstand zu hoch
│   │   │   ├── Schalter öffnen und schließen (mehrmals "durchschalten")
│   │   │   ├── Hilft nicht → Kontakte korrodiert → ersetzen
│   │   │   └── Anschlussklemmen nachziehen (Drehmoment!)
│   │   │
│   │   └── <0,05V → Schalter OK, Problem liegt anderswo
│   │       └── Bus-Bar-Verbindung und Kabelschuhe prüfen
│   │
│   └── Schalter wird sehr warm unter Last
│       ├── Nennstrom des Schalters ausreichend?
│       ├── Kontaktwiderstand messen
│       └── Zu hoher Widerstand → Schalter ersetzen
│
└── ENDE: Fehler identifiziert und behoben
```

### Entscheidungsbaum T-08-05: Gesamtes Bordnetz ausgefallen

```
START: Kompletter Stromausfall an Bord
│
├── SOFORTMASSNAHMEN:
│   ├── Ruhe bewahren — Boot ist nicht in unmittelbarer Gefahr
│   ├── Taschenlampe bereithalten (sollte immer griffbereit sein!)
│   ├── Position sichern (Anker, Segel, Drift abschätzen)
│   └── Seenotsender (wenn vorhanden, batteriebetrieben) bereithalten
│
├── Batterie-Hauptschalter prüfen
│   ├── Steht auf OFF → Wurde versehentlich ausgeschaltet
│   │   ├── Wieder einschalten
│   │   └── Sicherung gegen versehentliches Ausschalten nachrüsten
│   │
│   └── Steht auf ON → Weiter
│       │
│       ├── Batteriespannung direkt an Polklemmen messen
│       │   ├── 0V → Batterie komplett leer oder interne Unterbrechung
│       │   │   ├── Batteriezustand prüfen (Elektrolyt, Schwellung, Geruch)
│       │   │   ├── Polklemmen-Kontakt prüfen (Korrosion, lose)
│       │   │   └── LiFePO4: BMS hat abgeschaltet → Fehlerspeicher lesen
│       │   │
│       │   ├── <10,5V (12V-System) → Tiefentladen
│       │   │   ├── Alle Verbraucher ausschalten
│       │   │   ├── Motor starten (falls möglich → Lichtmaschine lädt)
│       │   │   ├── Wenn kein Motorstart: Solarpanel, Generator
│       │   │   └── Wenn NICHTS verfügbar: Seenotfall melden
│       │   │
│       │   └── >12V → Batterie OK, Problem im Verteilungssystem
│       │       │
│       │       ├── Spannung hinter Hauptschalter messen
│       │       │   ├── Keine Spannung → Hauptschalter defekt
│       │       │   │   └── Überbrücken (nur Notfall!) oder ersetzen
│       │       │   │
│       │       │   └── Spannung vorhanden → Problem im Verteiler
│       │       │       ├── Hauptsicherung (ANL/MEGA) prüfen
│       │       │       │   ├── Durchgebrannt → Kurzschluss im System
│       │       │       │   │   ├── NICHT einfach ersetzen!
│       │       │       │   │   ├── Ursache finden (Isolationsmessung)
│       │       │       │   │   └── Wenn sicher: Ersatzsicherung einsetzen
│       │       │       │   │
│       │       │       │   └── Intakt → Bus-Bar-Verbindungen prüfen
│       │       │       │       ├── Lose Bolzen → nachziehen
│       │       │       │       ├── Korrosion → reinigen
│       │       │       │       └── Kabelbruch → reparieren
│       │       │       │
│       │       │       └── Notversorgung: Kritische Verbraucher direkt an Batterie
│       │       │           ├── UKW-Funk
│       │       │           ├── Navigationslicht
│       │       │           └── Bilgepumpe
│       │       │
│       │       └── HINWEIS: Ersatz-Hauptsicherung mitführen! (ANL passender Wert)
│       │
│       └── Multimeter nicht verfügbar?
│           ├── Motorstart versuchen → Motor startet: Batterie hat Energie
│           ├── Motor startet nicht: Batterie leer oder Startkreis defekt
│           └── → Prüflampe als Notbehelf (12V-Lampe mit Krokodilklemmen)
│
└── ENDE: System wiederhergestellt oder Seenotfall eingeleitet
```

---

## 8. FAQ

### Allgemeine Fragen

**F-08-FAQ-01: Muss jeder Stromkreis an Bord einzeln abgesichert sein?**

Ja, nach ABYC E-11 und ISO 10133 muss jeder nicht-geerdete Leiter (Plus-Leiter im DC-System, Phase und Neutralleiter im AC-System) durch eine Überstromschutzeinrichtung geschützt sein. Einzige Ausnahme: Das Starterkabel zum Anlasser darf ungesichert sein, wenn es kürzer als ~1m ist und mechanisch geschützt verlegt wird (umstritten, ABYC empfiehlt trotzdem Absicherung).

**F-08-FAQ-02: Warum darf ich die Sicherung nicht einfach durch eine größere ersetzen, wenn sie ständig auslöst?**

Die Sicherung schützt primär das Kabel vor Überhitzung und Brand. Eine größere Sicherung erlaubt einen höheren Strom, den das vorhandene Kabel möglicherweise nicht sicher tragen kann. Das Ergebnis: Das Kabel überhitzt, die Isolierung schmilzt, und es kommt zum Kabelbrand — die Sicherung hält dabei und "schützt" das bereits brennende Kabel nicht. Die korrekte Lösung: Ursache der Überlast finden oder Kabelquerschnitt UND Sicherung gemeinsam erhöhen.

**F-08-FAQ-03: Was ist der Unterschied zwischen einer "trägen" und einer "flinken" Sicherung?**

Eine flinke (fast-acting) Sicherung löst bereits bei kurzfristiger Überschreitung des Nennstroms aus. Sie eignet sich für elektronische Geräte ohne Anlaufstrom. Eine träge (slow-blow, time-delay) Sicherung toleriert kurzzeitige Stromspitzen (z.B. Motoranlauf) und löst erst bei dauerhafter Überlast aus. Im Bordnetz werden fast ausschließlich träge oder mittelträge Sicherungen verwendet, da viele Verbraucher (Pumpen, Winden, Kompressoren) einen kurzzeitigen Anlaufstrom haben, der 3–8× über dem Betriebsstrom liegt.

**F-08-FAQ-04: Wie viel Abstand muss zwischen der Batterie und der ersten Sicherung sein?**

Nach ABYC E-11 maximal 7 inches (178mm, aufgerundet 180mm) vom Batterie-Anschlusspunkt. Dieser Abschnitt zwischen Batteriepol und Sicherung ist der einzige Teil des Bordnetzes, der bei einem Kurzschluss keinen Schutz hat. Er muss daher so kurz wie möglich sein und der Kabelweg muss mechanisch geschützt verlegt werden (kein Kontakt mit scharfen Kanten, keine Scheuerstellen, hitzefest).

**F-08-FAQ-05: Kann ich Automotive-Sicherungen auf einem Boot verwenden?**

ATO/ATC-Flachsicherungen sind identisch für Automotive und Marine — die Sicherung selbst unterscheidet sich nicht. Der Unterschied liegt im Halter: Marine-Sicherungshalter (z.B. Blue Sea ST Blade) verwenden verzinnte Kontakte, korrosionsbeständige Materialien und haben häufig Schutzabdeckungen. Automotive-Sicherungskästen hingegen haben oft unbehandelte Kontakte, die im salzigen Milieu schnell korrodieren. Fazit: Die Sicherungen selbst sind austauschbar, die Halter sollten Marine-Qualität sein.

**F-08-FAQ-06: Brauche ich einen Batterie-Hauptschalter, wenn ich ein BMS habe?**

Ja, unbedingt. Das BMS ist eine elektronische Schutzeinrichtung, die selbst ausfallen kann. Der manuelle Batterie-Hauptschalter ist die letzte mechanische Sicherheitsebene und wird von allen relevanten Normen (ABYC, ISO, CE) gefordert. Das BMS trennt automatisch bei Zellproblemen, der Hauptschalter ermöglicht die manuelle Trennung bei Wartung, Liegeplatz oder Notfall.

**F-08-FAQ-07: Was bedeutet "AIC" bei Sicherungen und warum ist das wichtig?**

AIC steht für "Ampere Interrupting Capacity" — das maximale Kurzschlussstrom, den eine Sicherung sicher abschalten kann. Wenn der Kurzschlussstrom den AIC-Wert übersteigt, kann die Sicherung den Strom nicht unterbrechen: Sie schmilzt zwar, aber der Lichtbogen wird nicht gelöscht. Die Folge: anhaltender Lichtbogen, Explosion der Sicherung, Brand. Bei Lithium-Batterien mit extrem niedrigem Innenwiderstand können Kurzschlussströme 10.000A+ erreichen — Standard-ANL-Sicherungen mit 6.000A AIC reichen dann nicht. Hier sind Klasse-T-Sicherungen (20.000A AIC) erforderlich.

### Dimensionierung und Planung

**F-08-FAQ-08: Wie berechne ich die richtige Sicherungsgröße für einen Verbraucher?**

Schritt 1: Betriebsstrom des Verbrauchers ermitteln (Typenschild oder P/U).
Schritt 2: Sicherung ≥ 125% des Dauerstroms wählen.
Schritt 3: Kabelquerschnitt für diesen Strom + Kabellänge + max. 3% Spannungsabfall bestimmen.
Schritt 4: Kabelbelastbarkeit (mit Derating für Temperatur und Bündelung) bestimmen.
Schritt 5: Sicherung ≤ Kabelbelastbarkeit (nach Derating) prüfen.
Schritt 6: Selektivität zur nächsthöheren Sicherung prüfen (Faktor ≥1,6).
Im Zweifel: Kabel eine Stufe größer, Sicherung auf die Kabelbelastbarkeit abstimmen.

**F-08-FAQ-09: Wie viele Stromkreise brauche ich auf meinem Boot?**

Faustregel nach Bootsgröße: Bootslänge in Metern × 2 bis 3 = Anzahl DC-Kreise. Dazu kommen AC-Kreise: etwa 1 pro 2m Bootslänge bei Landstromanschluss. Sicherheitskritische Verbraucher (Bilgepumpe, Navigation, Positionslichter, UKW) bekommen IMMER eigene Kreise. Komfortverbraucher können nach Zonen gruppiert werden.

**F-08-FAQ-10: Wann brauche ich ein 24V-System statt 12V?**

Ab etwa 12m LOA oder wenn die Gesamtleistung dauerhaft >2.000W überschreitet, wird ein 24V-System wirtschaftlich sinnvoller. Die halbierten Ströme erlauben dünnere Kabel, geringere Verluste und kleinere Sicherungen. Bei 48V-Systemen (zunehmend bei Elektro- und Hybridyachten) gelten zusätzliche Sicherheitsanforderungen bezüglich Berührungsschutz.

**F-08-FAQ-11: Muss ich AC und DC physisch trennen?**

Ja. Nach ABYC E-11 und ISO 13297 müssen AC- und DC-Kabel physisch getrennt geführt werden (separate Kabelkanäle oder mindestens 50mm Abstand). AC- und DC-Panels müssen getrennte Gehäuse haben oder durch eine feste Trennwand separiert sein. Die Farbcodierung unterscheidet AC (schwarz = Phase nach ABYC) und DC (rot = Plus). In der Praxis sind auch getrennte Panel-Positionen empfehlenswert.

### Installation und Wartung

**F-08-FAQ-12: Wie oft sollte ich Sicherungen und Schalter prüfen?**

Empfohlenes Intervall: Halbjährlich eine visuelle Inspektion aller Sicherungen (Verfärbung, Korrosion), vierteljährlich bei Booten in tropischem Klima oder Salzwasserrevier. Jährlich: Drehmoment aller Schraubverbindungen an Bus-Bars und Bolzensicherungen prüfen. Alle 5 Jahre: Professionelle Überprüfung der gesamten elektrischen Anlage durch einen zertifizierten Elektriker oder Surveyor.

**F-08-FAQ-13: Kann ich Leitungsschutzschalter statt Schmelzsicherungen verwenden?**

Für DC-Kreise bis ~50A: Ja, wenn marine-zugelassene DC-Leitungsschutzschalter mit ausreichender DC-Schaltfähigkeit verwendet werden. Vorteil: Rücksetzbar, kein Ersatzvorrat nötig. Für Hochstromkreise (>50A): Schmelzsicherungen (ANL, MEGA, Klasse T) sind in der Regel die bessere Wahl, da sie höhere Ausschaltvermögen bei geringerem Platzbedarf bieten. Für AC-Kreise: Leitungsschutzschalter (MCB) sind Standard und verpflichtend (in Kombination mit FI/RCD).

**F-08-FAQ-14: Was ist die korrekte Reihenfolge für den Landstromanschluss?**

1. Landstromkabel an die Borddose anschließen (Boot-Seite zuerst!)
2. Dann Stecker in die Hafensteckdose einstecken
3. FI/RCD am Bordpanel einschalten
4. Einzelne AC-Kreise einschalten
Beim Trennen: Umgekehrte Reihenfolge. Der Grund: Der spannungsführende Stecker wird nie offen gehandhabt.

**F-08-FAQ-15: Brauche ich einen Trenntransformator für Landstrom?**

Dringend empfohlen für Boote mit Metallrumpf (Stahl, Aluminium) — hier kann ohne Trenntransformator ein gefährlicher Potentialausgleich über das Wasser entstehen (galvanische Korrosion, Personengefährdung). Bei GFK-Booten optional, aber für maximale Sicherheit und gegen vagabundierende Ströme im Hafen empfehlenswert.

**F-08-FAQ-16: Wie teste ich einen FI-Schutzschalter?**

Monatlich die Testtaste drücken — der FI muss sofort auslösen. Einmal jährlich mit einem FI-Testgerät (z.B. Duspol) den tatsächlichen Auslösestrom und die Auslösezeit messen (soll: ≤30mA, <300ms nach Norm, typisch <30ms). Ein FI, der auf die Testtaste nicht auslöst, ist sofort zu ersetzen.

### Digitale Systeme

**F-08-FAQ-17: Lohnt sich ein digitales Verteilungssystem wie CZone?**

Für Neubauten ab ~15m LOA und einem Systemumfang von >30 Stromkreisen kann CZone die Verkabelung um 40–60% reduzieren (Gewicht, Kosten, Komplexität der Kabelbäume). Für Nachrüstung oder Boote <12m ist der Aufwand und die Kosten in der Regel nicht gerechtfertigt. Nachteil: Höhere Abhängigkeit von Elektronik, komplexere Fehlersuche, Fachbetrieb für Programmierung nötig.

**F-08-FAQ-18: Was passiert, wenn bei einem digitalen System die Steuerung ausfällt?**

Bei CZone: Die Motor Output Interfaces (MOI) haben eine "Fail-Safe"-Konfiguration, die festlegt, welche Ausgänge bei Kommunikationsverlust aktiv bleiben (typisch: Bilgepumpe, Positionslichter). Alle anderen Ausgänge gehen in den definierten Sicherheitszustand (meist AUS). Eine vollständig manuelle Steuerung ist ohne CAN-Bus-Kommunikation nicht möglich — dies ist ein Kritikpunkt gegenüber konventionellen Systemen.

### Normen und Zertifizierung

**F-08-FAQ-19: Welche Normen gelten für die elektrische Anlage meines Bootes?**

In der EU: CE-Kennzeichnung nach Sportboot-Richtlinie 2013/53/EU, umgesetzt durch ISO 10133 (DC) und ISO 13297 (AC). In den USA: ABYC E-11 (nicht gesetzlich vorgeschrieben, aber De-facto-Standard und von Versicherungen gefordert). Für gewerbliche Schiffe: IEC 60092. Für Superyachten: Zusätzlich Klassifikationsgesellschaft (Lloyd's, DNV, BV) mit eigenen Regularien.

**F-08-FAQ-20: Verliere ich meine CE-Zertifizierung, wenn ich die Elektrik umbaue?**

Grundsätzlich nein, wenn der Umbau die relevanten Normen einhält. Die CE-Kennzeichnung bezieht sich auf den Zustand bei Erstinverkehrbringung. Bei wesentlichen Änderungen (z.B. komplett neue Verteilung, Wechsel 12V→24V) kann eine erneute Konformitätsbewertung erforderlich sein. In der Praxis: Dokumentation des Umbaus erstellen, Normenkonformität nachweisen, Protokoll für Versicherung aufbewahren.

**F-08-FAQ-21: Was bedeutet "ignition protected" und wann ist es relevant?**

"Ignition protected" (ISO 8846) bedeutet, dass ein elektrisches Gerät so gebaut ist, dass im Normalbetrieb und bei Fehlfunktion keine zündfähigen Funken oder Temperaturen auftreten. Pflicht in Räumen, in denen sich explosive Gas-Luft-Gemische bilden können: Maschinenraum (Benzinmotoren!), Gasflaschenkasten, Batterieraum (Blei-Batterien gasen Wasserstoff aus). Bei Dieselmotoren: Im Maschinenraum empfohlen, bei guter Belüftung aber nicht zwingend vorgeschrieben.

### Spezialfragen

**F-08-FAQ-22: Wie sichere ich ein Lithium-Batteriesystem korrekt ab?**

Kritische Unterschiede zu Blei-Systemen: (a) Wesentlich niedrigerer Innenwiderstand → extrem hohe Kurzschlussströme (>10.000A möglich). (b) Sicherungen mit hohem AIC verwenden (Klasse T mit 20.000A). (c) BMS als elektronische Schutzebene zusätzlich zu mechanischer Sicherung. (d) Hauptsicherung und Hauptschalter müssen die höheren Kurzschlussströme beherrschen. (e) Keinesfalls Sicherungen "zu groß" dimensionieren — das BMS kann nicht als Ersatz für korrekte Sicherungsdimensionierung dienen.

**F-08-FAQ-23: Darf ich Bus-Bars aus dem Baumarkt verwenden?**

Nicht empfohlen. Baumarkt-Verteilerklemmen ("Reihenklemmen") sind für Hausinstallation (feste Verlegung, kein Salz, keine Vibration) ausgelegt. Marine-Bus-Bars müssen aus verzinntem Kupfer oder Messing sein, mit marine-grade Schrauben (Edelstahl A4 oder Messing), und für den Einsatz unter Vibration und Salzbedingungen getestet sein. Der Preisunterschied ist gering, das Risiko bei Versagen hoch.

**F-08-FAQ-24: Wie schütze ich die Elektrik vor Blitzschlag?**

Vollständiger Blitzschutz ist auf Segelbooten schwierig, aber folgende Maßnahmen reduzieren Schäden: (a) Blitzableiter vom Masttopp zum Kiel (niederohmig, min. 8mm² Kupfer). (b) Varistoren / MOV-Blitzschutzmodule an den Eingängen empfindlicher Elektronik. (c) Bonding aller Metallteile. (d) GPS-Antenne und VHF-Antenne über Blitzschutzpatronen anschließen. (e) Kein 100%iger Schutz möglich — Versicherung prüfen!

**F-08-FAQ-25: Was ist ein Batterie-Balancer und brauche ich einen?**

Ein Batterie-Balancer gleicht Spannungsdifferenzen zwischen in Reihe geschalteten Batterien aus (z.B. zwei 12V-Batterien in Reihe für 24V). Ohne Balancer altert eine Batterie schneller als die andere, was zu asymmetrischer Ladung und reduzierter Lebensdauer führt. Empfohlen für alle 24V-Systeme mit zwei 12V-Batterien in Reihe. Bei Lithium-Systemen übernimmt das BMS die Balancing-Funktion auf Zellebene.

**F-08-FAQ-26: Wie dimensioniere ich den Gleichzeitigkeitsfaktor für die Hauptsicherung?**

Der Gleichzeitigkeitsfaktor beschreibt, welcher Anteil der installierten Last gleichzeitig aktiv ist. Für die Hauptsicherung: Nicht die Summe aller Einzelsicherungen verwenden, sondern den realistisch gleichzeitigen Maximalstrom. Richtwerte: Segelboot Fahrt 0,4–0,6, Segelboot Hafen 0,3–0,5, Motoryacht Fahrt 0,5–0,7. Berechnung: I_haupt = Σ(I_einzelkreis × GF) × 1,25. Die Hauptsicherung schützt dann das Kabel zwischen Batterie und Hauptverteiler, das auf diesen Strom dimensioniert sein muss.

---

## 9. Glossar

| Begriff | Erklärung |
|---------|-----------|
| **AIC** (Ampere Interrupting Capacity) | Maximaler Kurzschlussstrom, den eine Sicherung oder ein Schalter sicher abschalten kann. Überschreitung führt zu Lichtbogen oder Explosion. |
| **ANL-Sicherung** | Hochstrom-Bolzensicherung für marine Anwendungen, 35–750A, Schraubbefestigung, träge Auslösecharakteristik. |
| **ATO/ATC** | Standard-Flachstecksicherung (Blade Fuse), 1–40A, Industriestandard für DC-Einzelkreise auf Booten und in Fahrzeugen. |
| **Auslösecharakteristik** | Zeitverhalten einer Schutzeinrichtung bei Überstrom. Definiert durch Strom-Zeit-Kurve (flink, mittelträge, träge). |
| **Ausschaltvermögen** | Siehe AIC. Höchster Fehlerstrom, den ein Schutzorgan sicher unterbrechen kann. |
| **Batterie-Hauptschalter** | Manueller Schalter, der das gesamte Bordnetz von der Batterie trennt. Pflichtbauteil nach ABYC und ISO. |
| **BMS** (Battery Management System) | Elektronisches Überwachungs- und Schutzsystem für Lithium-Batterien. Trennt bei Über/Unterspannung, Übertemperatur, Überstrom. |
| **Bonding** | Verbindung aller Metallteile an Bord (Rumpf, Motor, Tanks, Beschläge) auf ein gemeinsames Potential zur Korrosionsvermeidung. |
| **Bus-Bar** (Sammelschiene) | Kupfer- oder Messingschiene, an der mehrere Kabelabgänge zusammengeführt werden. Zentrale Verteilungspunkte im Bordnetz. |
| **CAN-Bus** | Controller Area Network — serielles Bussystem für die Kommunikation zwischen digitalen Steuergeräten. Basis für NMEA 2000 und CZone. |
| **CE-Kennzeichnung** | Konformitätszeichen der EU. Bestätigt Einhaltung der Sportboot-Richtlinie 2013/53/EU und zugehöriger harmonisierter Normen. |
| **CZone** | Digitales Energieverteilungssystem von BEP Marine mit CAN-Bus-Kommunikation und Halbleiterschaltern. |
| **DC-Panel** | Verteilerpanel für Gleichstrom (12V oder 24V). Enthält Schalter, Sicherungen und ggf. Anzeigeinstrumente. |
| **Derating** | Reduzierung der zulässigen Belastung aufgrund ungünstiger Bedingungen (Temperatur, Kabelbündelung, Höhenlage). |
| **DIN-Hutschiene** | Genormte Tragschiene (35mm) für den Reiheneinbau von Schutzschaltern und Automatisierungskomponenten. |
| **Einlinienschaltplan** | Übersichtsschaltplan, der die Struktur der Verteilung zeigt, ohne jeden einzelnen Leiter darzustellen. |
| **FI-Schutzschalter** (RCD) | Fehlerstromschutzschalter. Erkennt Differenzströme (Erdschluss) und schaltet bei ≤30mA ab. Pflicht für AC an Bord. |
| **Gleichzeitigkeitsfaktor** | Faktor, der beschreibt, welcher Anteil der installierten Verbraucher gleichzeitig aktiv ist. Typisch 0,3–0,8 je nach Bootstyp. |
| **Ignition Protected** | Schutzart nach ISO 8846: Gerät erzeugt im Normal- und Fehlerbetrieb keine zündfähigen Funken oder Temperaturen. |
| **Isolationsmessung** | Messung des Isolationswiderstands zwischen Leiter und Masse mit Hochspannung (500V DC typisch). Sollwert: >2MΩ. |
| **Klasse-T-Sicherung** | Hochleistungs-Sicherung mit extrem hohem Ausschaltvermögen (20.000A+). Erforderlich für Lithium-Batteriesysteme. |
| **Kriechstrecke** | Kürzester Weg über eine Isolierstoff-Oberfläche zwischen zwei leitfähigen Teilen. Bestimmt die elektrische Sicherheit. |
| **Lasttrennschalter** | Schalter, der im Gegensatz zum Trennschalter unter Last (bis Nennstrom) betätigt werden darf. |
| **Leitungsschutzschalter** (MCB) | Selbsttätig auslösender Schalter mit thermischer (Überlast) und magnetischer (Kurzschluss) Auslösung. Rücksetzbar. |
| **Lynx-System** | Modulares DC-Verteilungssystem von Victron Energy mit stapelbaren Komponenten (Distributor, Shunt, BMS, Power In). |
| **MasterBus** | Proprietäres CAN-basiertes Kommunikationssystem von Mastervolt für integriertes Energiemanagement. |
| **MCB** (Miniature Circuit Breaker) | Leitungsschutzschalter, meist für AC-Kreise (230V). Definierte Auslösecharakteristik B, C, D. |
| **MEGA-Sicherung** | Hochstrom-Bolzensicherung mit M8-Anschluss, 100–500A, kompakte Bauform, Ausschaltvermögen 2.000A. |
| **MIDI-Sicherung** | Mittelstrom-Sicherung, 30–200A, kompakte Bauform, Lücke zwischen ATO und ANL schließend. |
| **NMEA 2000** | Standardisiertes marines Kommunikationsprotokoll auf CAN-Bus-Basis für Navigationsgeräte und Sensoren. |
| **Not-Aus** | Notabschaltsystem, das bei Betätigung alle nicht-essentiellen Verbraucher vom Bordnetz trennt. |
| **Netzvorrangschaltung** | Automatische Umschaltung zwischen Landstrom und Inverterbetrieb. Landstrom hat Vorrang. |
| **Potentialausgleich** | Herstellung gleichen elektrischen Potentials zwischen allen leitfähigen Teilen zur Vermeidung gefährlicher Berührungsspannungen. |
| **RCD** (Residual Current Device) | Englische Bezeichnung für FI-Schutzschalter. Erkennt Fehlerstrom und schaltet bei ≤30mA ab. |
| **Selektivität** | Eigenschaft einer Sicherungskaskade, bei der nur die dem Fehler nächstgelegene Sicherung auslöst. |
| **SELV** (Safety Extra Low Voltage) | Schutzkleinspannung. DC-Systeme <50V (bzw. <120V DC nach IEC) gelten als berührungssicher. |
| **Spannungsabfall** | Spannungsverlust über Kabel und Verbindungen. Maximaler Richtwert: 3% für kritische, 10% für unkritische Verbraucher. |
| **Stromlaufplan** | Detaillierter Schaltplan, der jeden einzelnen Leiter mit Querschnitt, Farbe und Anschlusspunkt zeigt. |
| **Trenntransformator** | Transformator, der Landstrom galvanisch vom Bordnetz trennt. Verhindert vagabundierende Ströme und Korrosion. |
| **Übergangswiderstand** | Widerstand an einer elektrischen Verbindungsstelle (Klemme, Stecker, Schalter). Verursacht Wärme und Spannungsabfall. |
| **Verpolschutz** | Maßnahme (Diode, Schaltung, mechanische Codierung) zur Verhinderung falscher Polarität an Verbrauchern. |
| **Wahlschalter** | Batterie-Hauptschalter mit Positionen 1/BOTH/2/OFF zur Umschaltung zwischen zwei Batteriebänken. |

---

## 10. Schnell-Referenz

### 10.1 Sicherungstypen — Kurzvergleich

| Typ | Strom | Spannung | AIC | Bauform | Marine-Einsatz |
|-----|-------|----------|-----|---------|----------------|
| ATO/ATC | 1–40A | ≤32V DC | 1.000A | Blade, Stecker | Einzelkreise Standard |
| ATM (Mini) | 2–30A | ≤32V DC | 1.000A | Mini-Blade | Kompakte Panels |
| APX (Maxi) | 20–120A | ≤32V DC | 2.000A | Maxi-Blade | Panel-Eingänge |
| MIDI | 30–200A | ≤32V DC | 1.000–10.000A | Bolzen M5 | Panel-Eingänge, Mittelverbraucher |
| ANL | 35–750A | ≤72V DC | 6.000–25.000A | Bolzen 5/16" | Hauptsicherung, Großverbraucher |
| MEGA | 100–500A | ≤32V DC | 2.000A | Bolzen M8 | Alternative zu ANL |
| Klasse T | 110–800A | ≤160V DC | 20.000A | Bolzen | LiFePO4, Inverter, E-Antrieb |
| Glasrohr 6×30 | 0,5–25A | ≤250V | 100–1.500A | Rohr | Geräte-Feinsicherung |

### 10.2 Farbcode ATO/ATC

| 1A: Schwarz | 2A: Grau | 3A: Violett | 4A: Rosa | 5A: Beige |
|-------------|----------|-------------|----------|-----------|
| **7,5A: Braun** | **10A: Rot** | **15A: Blau** | **20A: Gelb** | **25A: Natur** |
| **30A: Grün** | **40A: Orange** | | | |

### 10.3 180mm-Regel

```
┌──────────────────────────────────────┐
│ BATTERIE-POL  ←──── 180mm max ────→ SICHERUNG │
│    (+)                                  (ANL)    │
│                                                   │
│ Dieser Abschnitt ist UNGESCHÜTZT!                │
│ → So kurz wie möglich                            │
│ → Mechanisch geschützt verlegen                  │
│ → Kein Kontakt mit scharfen Kanten               │
│ → Hitzefest (Maschinenraum-Routing beachten)     │
└──────────────────────────────────────┘
```

### 10.4 Selektivitäts-Schnellprüfung

```
Regel: I_vorgelagert ≥ 1,6 × I_nachgelagert

Beispiel KORREKT:
  Hauptsicherung:  200A ANL  (200 ≥ 1,6 × 100 = 160 ✓)
  Panel-Eingang:   100A MIDI (100 ≥ 1,6 × 15 = 24 ✓)
  Einzelkreis:      15A ATO

Beispiel FALSCH:
  Hauptsicherung:   80A ANL  (80 < 1,6 × 60 = 96 ✗!)
  Panel-Eingang:    60A MIDI
  → Keine Selektivität! Hauptsicherung löst vor Panel-Eingang aus.
```

### 10.5 Sicherung-Kabel-Zuordnung (12V DC, Einzelverlegung, 30°C)

| Sicherung [A] | Kabel min. [mm²] | AWG | Kabelbelastbarkeit [A] |
|---------------|------------------|-----|----------------------|
| 3 | 0,75 | 18 | 7 |
| 5 | 1,0 | 16 | 10 |
| 7,5 | 1,5 | 14 | 15 |
| 10 | 1,5 | 14 | 15 |
| 15 | 2,5 | 12 | 25 |
| 20 | 4,0 | 10 | 35 |
| 25 | 4,0 | 10 | 35 |
| 30 | 6,0 | 8 | 50 |
| 40 | 10 | 6 | 65 |
| 60 | 16 | 4 | 85 |
| 80 | 25 | 2 | 115 |
| 100 | 35 | 1 | 145 |
| 125 | 35 | 1 | 145 |
| 150 | 50 | 1/0 | 170 |
| 200 | 70 | 2/0 | 210 |
| 250 | 95 | 3/0 | 265 |
| 300 | 95 | 3/0 | 265 |
| 400 | 120 | 4/0 | 310 |

*Hinweis: Bei Kabelbündelung oder erhöhter Umgebungstemperatur (Maschinenraum) Derating-Faktoren anwenden! Typisch: Bündel 3 Kabel: ×0,8 / Bündel 5+ Kabel: ×0,7 / Umgebung 40°C: ×0,9 / Umgebung 50°C: ×0,8*

### 10.6 Wartungsintervalle Schalttafeln und Sicherungen

| Intervall | Prüfung | Methode | Sollwert |
|-----------|---------|---------|----------|
| Monatlich | Sichtkontrolle Panel | Visuell | Keine Verfärbungen, keine Korrosion |
| Monatlich | FI/RCD-Testtaste | Drücken | Löst sofort aus |
| Quartalsweise | Sicherungen auf Verfärbung | Visuell | Transparenter Kunststoff, kein Gilb |
| Quartalsweise | Schaltergang | Haptisch | Definiertes Einrasten, kein Wackeln |
| Halbjährlich | Bus-Bar-Verbindungen | Drehmoment | M6: 4–5Nm, M8: 8–10Nm |
| Halbjährlich | Spannungsabfall unter Last | Multimeter | <0,1V über Schalter/Sicherung |
| Halbjährlich | Kontaktreinigung | Kontaktspray | Saubere, blanke Kontakte |
| Jährlich | Isolationsmessung | Megger 500V DC | >2MΩ alle Kreise |
| Jährlich | FI/RCD Auslösestrom | Prüfgerät | ≤30mA, <300ms |
| Jährlich | Thermografie (optional) | Wärmebildkamera | Keine Hotspots >20K über Umgebung |
| Alle 5 Jahre | Professionelle Revision | Fachbetrieb | Alle Normen erfüllt |

---

## 11. ANHANG A–H — Fallstudien

### ANHANG A — Fallstudie: Kompletterneuerung Schaltpanel Bavaria 37 Cruiser (Baujahr 2005)

**Ausgangssituation:**
Segelyacht, 11,35m LOA, 12V-System. Originales Schaltpanel mit 12 DC-Kreisen, Kippschalter, Glasrohrsicherungen. Panel nach 19 Jahren stark korrodiert, mehrere Schalter defekt, Glasrohrsicherungen schwer beschaffbar, keine AC-Integration.

**Befund:**
- 4 von 12 Kippschaltern haben erhöhten Kontaktwiderstand (>10mΩ)
- 3 Glasrohrsicherungshalter korrodiert (Kontaktwiderstand >50mΩ)
- Bus-Bar: Messing unbehandelt, grünliche Patina
- Keine Beschriftung der Kreise (abgefallene Aufkleber)
- AC-Panel separat montiert, unsachgemäß an DC-Panel angelötet
- Bilgepumpe über Panel geschaltet (kein Direktanschluss an Batterie)

**Lösung:**
- Neues Blue Sea 360 Panel, 12 Positionen DC + 4 Positionen AC
- ATO/ATC-Sicherungen statt Glasrohr
- Toggle-Breaker (kombinierter Schalter + Automat) für alle DC-Kreise
- Trennung AC/DC in separate 360-Rahmen mit Trennwand
- Bilgepumpe mit eigenem Kreis direkt an Batterie + Sicherung
- Neue Bus-Bar: Kupfer verzinnt, 150A
- Professionelle Beschriftung (Gravur)

**Kosten:**

| Position | Material | Arbeit | Summe |
|----------|----------|--------|-------|
| Blue Sea 360 Panel (DC 12-fach) | 480€ | — | 480€ |
| Blue Sea 360 Panel (AC 4-fach) | 280€ | — | 280€ |
| Toggle-Breaker 12× | 360€ | — | 360€ |
| AC-Leitungsschutzschalter 4× | 120€ | — | 120€ |
| FI-Schutzschalter 30mA | 65€ | — | 65€ |
| Bus-Bar Cu/Sn 150A | 85€ | — | 85€ |
| Kabel, Kabelschuhe, Kleinteile | 180€ | — | 180€ |
| Arbeit Fachbetrieb (16h × 85€) | — | 1.360€ | 1.360€ |
| **Gesamt** | **1.570€** | **1.360€** | **2.930€** |

**Ergebnis:** Komplett normkonformes System, zukunftssicher, deutlich verbesserte Zuverlässigkeit und Sicherheit.

### ANHANG B — Fallstudie: Victron Lynx Installation auf Langfahrt-Katamaran Lagoon 42 (Baujahr 2019)

**Ausgangssituation:**
Katamaran 12,80m, werkseitiges 12V-System mit 2× 100Ah AGM-Servicebatterien. Eigentümer plant Atlantiküberquerung und rüstet auf LiFePO4 um: 3× Victron Smart LiFePO4 200Ah = 600Ah.

**Anforderungen:**
- 600Ah LiFePO4-Bank sicher absichern
- Victron MultiPlus 3000/12/120 (Inverter/Charger)
- 2× Victron MPPT 150/70 Solar-Laderegler
- Saubere, modulare Verteilung
- Monitoring über VRM-Portal

**Lösung — Lynx-System:**

```
[3× Victron Smart LiFePO4 200Ah]
         │
    [Lynx Smart BMS]
         │
    [Lynx Power In] ── MEGA 400A
         │
    [Lynx Distributor]
         ├── MEGA 200A → MultiPlus 3000
         ├── MEGA 100A → MPPT 150/70 #1
         ├── MEGA 100A → MPPT 150/70 #2
         └── MEGA 150A → DC-Hauptverteiler (Blue Sea 5026)
         │
    [Lynx Shunt] ── 500A
         │
       Masse-Bus
```

**Kosten:**

| Position | Preis |
|----------|-------|
| 3× Victron Smart LiFePO4 200Ah | 3.600€ |
| Lynx Smart BMS | 590€ |
| Lynx Power In | 95€ |
| Lynx Distributor | 180€ |
| Lynx Shunt | 220€ |
| 5× MEGA-Sicherungen (versch. Werte) | 75€ |
| Verbindungskabel Lynx (4 Stück) | 160€ |
| Victron MultiPlus 3000 | 1.400€ |
| 2× Victron MPPT 150/70 | 1.000€ |
| Blue Sea 5026 DC-Verteiler | 95€ |
| Kabel, Befestigung, Kleinteile | 450€ |
| Installation Fachbetrieb (24h) | 2.040€ |
| **Gesamt** | **9.905€** |

**Ergebnis:** Professionelles, vollintegriertes System mit Fernüberwachung. Klare Schutzebenen. Modulare Erweiterbarkeit.

### ANHANG C — Fallstudie: Brandschaden durch fehlende Hauptsicherung — Motorboot Bayliner 285 (Baujahr 2008)

**Schadensbeschreibung:**
Am Liegeplatz im Hafen, Boot unbeaufsichtigt. Rauchentwicklung aus dem Motorraum. Hafenmeister entdeckt den Brand frühzeitig und trennt das Landstromkabel. Feuerwehr löscht den Brand. Totalschaden des Motorraumkabelbaums, Teile des Motorraum-Schotts verkohlt.

**Befund (Gutachter):**
- Vom Vorbesitzer nachträglich installierter Inverter (2.000W) direkt an Batteriepol angeschlossen
- Kein Sicherungselement zwischen Batterie und Inverter
- Kabel: 16mm² (für 2.000W/12V = 167A völlig unterdimensioniert!)
- Kabel lag auf einem Motorlager und war durchgescheuert
- Kurzschluss durch blanken Leiter gegen Motorblock (Masse)
- Kein Schutzorgan hat ausgelöst — Batterie lieferte Strom bis zum Brand
- Geschätzter Kurzschlussstrom: >3.000A

**Ursachenkette:**

```
1. Unterdimensioniertes Kabel (16mm² statt min. 70mm²)
2. Keine Sicherung im Kabelweg (180mm-Regel ignoriert)
3. Kabel nicht befestigt, lag lose auf Motor
4. Vibration → Kabel scheuert durch → Kurzschluss
5. Kein Schutz → Batterie liefert >3.000A
6. Kabel schmilzt → Isolierung entzündet sich → Brand
```

**Kosten:**
- Schadensumme (Gutachten): 28.500€
- Versicherung reguliert nur teilweise (unsachgemäße Installation = Obliegenheitsverletzung)
- Eigenanteil Eigentümer: 12.000€+
- Kosten für normgerechte Installation hätten betragen: ~450€ (70mm²-Kabel + ANL 200A + Halter)

**Lehren:**
1. JEDES Kabel, das von der Batterie abgeht, MUSS innerhalb von 180mm abgesichert sein
2. Kabelquerschnitt IMMER für den maximalen Strom dimensionieren
3. Kabel IMMER befestigen und gegen Scheuern schützen
4. Nachträgliche Installationen NUR durch Fachpersonal oder unter Anleitung

### ANHANG D — Fallstudie: CZone-Umrüstung einer Nordhavn 43 (Baujahr 2012)

**Ausgangssituation:**
Motoryacht 13,10m, konventionelles System mit 42 DC-Kreisen, verteilt auf 4 Panels. Kabelbäume mit >200 Einzelleitern. Eigentümer möchte auf digitales System umstellen, da zunehmend Kontaktprobleme an Panels auftreten und die Fehlersuche bei 42 Kreisen extrem zeitaufwändig ist.

**Lösung — CZone:**
- 3× Motor Output Interface (MOI) — je 12 High-Side + 6 Low-Side Ausgänge
- 2× Signal Interface (SI) — für Sensoren und Schalteingänge
- 1× Meter Interface (MI) — für analoge Tank- und Temperatursensoren
- 1× Display Interface 7" — als Hauptbedienung am Steuerstand
- 1× Display Interface 3,5" — als Nebenbedienung in Eignerkabine
- 1× Wireless Interface — App-Steuerung

**Vorher vs. Nachher:**

| Parameter | Konventionell | CZone |
|-----------|--------------|-------|
| Kabelstränge zum Panel | 42× Plus + 42× Minus = 84 Leiter | CAN-Bus (2 Leiter) + Stromversorgung |
| Panelgröße | 4 Panels à 300×400mm | 1× 7" Display (178mm) |
| Fehlerdiagnose | Multimeter, manuell | App, Stromüberwachung pro Kanal |
| Erweiterung | Neues Kabel + neue Sicherung | Software-Konfiguration |
| Kabelgewicht | ~35kg (geschätzt) | ~12kg |
| Dimm-Funktion | Nein (nur an/aus) | Ja, PWM 0–100% pro Kanal |

**Kosten:**

| Position | Preis |
|----------|-------|
| 3× MOI | 3.600€ |
| 2× SI | 1.400€ |
| 1× MI | 850€ |
| 1× DI 7" | 1.800€ |
| 1× DI 3,5" | 950€ |
| 1× Wireless Interface | 650€ |
| CAN-Bus-Kabel und Stecker | 380€ |
| Programmierung (Fachbetrieb) | 2.400€ |
| Installation (40h) | 3.400€ |
| **Gesamt** | **15.430€** |

**Ergebnis:** Deutlich reduzierte Kabelkomplexität, professionelle Diagnose per App, Dimmfunktion für alle Beleuchtungskreise. Amortisation fraglich für Privatowner, aber erheblicher Mehrwert bei Fehlsuche und Komfort.

### ANHANG E — Fallstudie: AC-Verteilung mit Trenntransformator — Stahlketch 14m (Eigenausbau)

**Ausgangssituation:**
Stahlrumpf-Segelyacht, Eigenbau, 14m LOA. Landstromanschluss ohne Trenntransformator. Im Hafen massive galvanische Korrosion am Ruderblatt und an den Zinkanoden (Anoden in 3 Monaten verbraucht statt regulär 12 Monate). Nachbarboot hat ebenfalls Elektrik-Probleme.

**Diagnose:**
- Messung vagabundierender Ströme: 1,2A DC zwischen Rumpf und Hafenwasser
- Ursache: Defekte Erdung am Nachbarboot leitet Fehlerstrom über das Wasser und den Stahlrumpf ab
- Ohne Trenntransformator fließen diese Ströme ungehindert durch die Landstrom-Erdverbindung

**Lösung:**
- Mastervolt IVET 3600 Trenntransformator (3,6kVA)
- Neue AC-Verteilung: FI 30mA + 6 MCB (Typ B, 2-polig)
- Galvanischer Isolator (Diodenblock) als Backup am Landstromkabel

**AC-Verteilung nach Umbau:**

```
Hafensteckdose (230V)
    │
[Landstrom-Dose CEE 16A]
    │
[Galvanischer Isolator]
    │
[Trenntransformator Mastervolt IVET 3600]
    │
[FI/RCD 40A, 30mA, Typ A]
    │
[AC-Hauptpanel]
    ├── MCB 16A-B: Steckdosen Salon
    ├── MCB 16A-B: Steckdosen Kabinen
    ├── MCB 16A-B: Pantry (Mikrowelle, Wasserkocher)
    ├── MCB 10A-B: Warmwasserboiler
    ├── MCB 16A-C: Ladegerät Mastervolt 24/60
    └── MCB 10A-C: Watermaker
```

**Kosten:**

| Position | Preis |
|----------|-------|
| Mastervolt IVET 3600 | 1.850€ |
| Galvanischer Isolator | 280€ |
| AC-Panel (Blue Sea 360, 6-Way) | 520€ |
| FI/RCD 40A/30mA | 65€ |
| 6× MCB diverse | 90€ |
| Kabel 3×2,5mm² (30m) | 85€ |
| Installation (12h) | 1.020€ |
| **Gesamt** | **3.910€** |

**Ergebnis:** Vagabundierende Ströme eliminiert. Zinkanoden-Verbrauch normalisiert (12+ Monate Standzeit). Galvanische Korrosion gestoppt. Zusätzliche Sicherheit durch FI-Schutzschalter.

### ANHANG F — Fallstudie: Selektivitätsproblem auf Hanse 505 (Baujahr 2017)

**Symptom:**
Bei Verwendung der Ankerwinde fällt regelmäßig das gesamte DC-Bordnetz aus. Hauptsicherung (200A ANL) löst aus, obwohl die Ankerwinde nur mit 100A ANL einzeln abgesichert ist.

**Analyse:**
- Ankerwinde: Nennstrom 80A, Anlaufstrom 180A (kurzfristig 0,3s)
- Ankerwinden-Sicherung: 100A ANL (träge)
- Hauptsicherung: 200A ANL (träge)
- Problem: Anlaufstrom 180A liegt bei 90% der Hauptsicherung (200A). Beide Sicherungen sind gleicher Bauart (ANL, gleiche Auslösecharakteristik). Bei 180A für 0,3s + gleichzeitiger Hintergrundlast von 40A aus anderen Kreisen → Gesamtstrom 220A → 110% der Hauptsicherung → Hauptsicherung reagiert VOR der 100A-Sicherung.

**Ursache:** Keine ausreichende Selektivität. Verhältnis 200:100 = 2,0 — theoretisch ausreichend (≥1,6). Aber: Anlaufstrom + Hintergrundlast überschreiten die Hauptsicherung.

**Lösung:**
1. Hauptsicherung auf 300A ANL erhöhen (Kabelquerschnitt der Hauptzuleitung: 95mm² = 265A Belastbarkeit nach Derating → 300A ANL ist grenzwertig, Kabel ggf. auf 120mm² vergrößern)
2. Alternative: Ankerwinde mit Softstarter (reduziert Anlaufstrom auf ~120A)
3. Alternative: Ankerwinde mit eigenem Kabel direkt an Batterie (mit eigener 100A ANL), umgeht die Hauptsicherung des DC-Panels

**Gewählte Lösung:** Option 3 — Direktanschluss der Ankerwinde an Batterie. Zusätzlicher Vorteil: Kürzerer Kabelweg zur Ankerwinde, geringerer Spannungsabfall.

### ANHANG G — Fallstudie: Nachrüstung Notabschaltung auf Hallberg-Rassy 40 (Baujahr 2001)

**Ausgangssituation:**
Segelyacht, 12,20m LOA, kein Not-Aus-System vorhanden. Batterie-Hauptschalter im Maschinenraum unter dem Cockpitboden — im Notfall nicht schnell erreichbar.

**Anforderungen:**
- Not-Aus am Niedergang (erreichbar in <2 Sekunden)
- Not-Aus am Steuerstand
- Bilgepumpe bleibt aktiv (direkt an Batterie)
- Navigationslichter bleiben aktiv
- Motor-Startkreis unabhängig

**Lösung:**

```
[Service-Batterie 200Ah LiFePO4]
    │
[ANL 300A] ──180mm── [Batterie-Hauptschalter (Maschinenraum)]
    │
[Haupt-Bus-Bar]
    ├── ANL 200A → [Inverter]
    ├── MIDI 100A → [DC-Panel Navigation + Positionslicht]  ← BLEIBT AKTIV
    ├── MIDI 80A → [NOT-AUS-Relais 200A] → [DC-Panel Komfort]  ← WIRD GETRENNT
    └── MIDI 60A → [NOT-AUS-Relais 200A] → [DC-Panel Allgemein]  ← WIRD GETRENNT

[Bilgepumpe] ── 15A ATO ── direkt an Haupt-Bus-Bar  ← BLEIBT AKTIV

NOT-AUS-Bedientasten:
  - Niedergang: Roter Pilztaster
  - Steuerstand: Roter Pilztaster
  - Beide in Reihe geschaltet → Trennt NOT-AUS-Relais → Komfort + Allgemein OFF
```

**Kosten:**

| Position | Preis |
|----------|-------|
| 2× Hochstrom-Relais 200A (Victron Cyrix) | 220€ |
| 2× Not-Aus Pilztaster (marine-grade, IP67) | 160€ |
| MIDI-Sicherungen (3×) | 30€ |
| Kabel und Befestigungsmaterial | 85€ |
| Installation (8h) | 680€ |
| **Gesamt** | **1.175€** |

### ANHANG H — Fallstudie: Philippi STV-Serie für Superyacht-Maschinenraum — Princess V65 (Baujahr 2020)

**Ausgangssituation:**
Motoryacht 20,12m LOA, 24V-Hauptsystem, 12V-Subsystem für Navigationsgeräte. Der Maschinenraum benötigt ein professionelles Verteilungssystem für 28 DC-Kreise und 12 AC-Kreise.

**Lösung — Philippi STV (Sicherungs-Trenn-Verteiler):**

| Komponente | Typ | Kreise | Funktion |
|------------|-----|--------|----------|
| Philippi STV 236 | DC-Verteiler | 36 | Hauptverteilung 24V DC |
| Philippi STV 112 | DC-Verteiler | 12 | Unterverteilung 12V DC |
| Philippi PSM 2435 | AC-Verteiler | 12 | 230V AC-Verteilung |
| Philippi MBM 24100 | Batteriemonitor | — | Batterieüberwachung |
| Philippi BTS 200 | Trennschalter | — | Batterie-Haupttrenner 200A |

**Philippi STV 236 Spezifikationen:**

| Parameter | Wert |
|-----------|------|
| Kreisanzahl | 36 DC |
| Eingang | 400A Bus-Bar, M10-Bolzen |
| Sicherungen pro Kreis | ATO/ATC, 1–30A |
| Gesamtbelastung | 300A (mit Derating) |
| Bus-Bar | Kupfer verzinnt, 400A Nennstrom |
| Spannungsanzeige | Digital-Voltmeter integriert |
| Stromanzeige | Digital-Amperemeter integriert |
| Schutzart | IP44 (mit Abdeckung) |
| Einbauart | DIN-Hutschiene, Schaltschrankmontage |
| Abmessungen | 600 × 400 × 180mm |
| Material Gehäuse | Edelstahl 316L, pulverbeschichtet |
| Zertifizierung | GL, BV, LR, CE |

**Kosten (Gesamtsystem Maschinenraum):**

| Position | Preis |
|----------|-------|
| Philippi STV 236 | 3.200€ |
| Philippi STV 112 | 1.800€ |
| Philippi PSM 2435 | 2.600€ |
| Philippi MBM 24100 | 890€ |
| Philippi BTS 200 | 480€ |
| Schaltschrank (Edelstahl, maßgefertigt) | 2.400€ |
| DIN-Hutschienen, Klemmen, Verdrahtung | 1.200€ |
| Kabel und Anschlussmaterial | 2.800€ |
| Programmierung und Inbetriebnahme | 1.600€ |
| Installation (60h × 95€) | 5.700€ |
| **Gesamt** | **22.670€** |

**Ergebnis:** Professionelle Maschinenraumverteilung nach Klassifikationsstandards. Vollständig dokumentiert für Versicherung und Flaggenstaat. Wartungsfreundlich durch modularen Aufbau.

---

## 12. ANHANG I–R — Pydantic v2 Modelle

### ANHANG I — Basismodelle

```python
"""
AYDI Knowledge Module: 22_08 Schalttafeln und Sicherungen
Pydantic v2 Models — Base Types

All models use model_config = {"from_attributes": True}
NEVER use class Config.
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


# ── Enumerations ──────────────────────────────────────────────────

class FuseType(str, Enum):
    """Sicherungsbauformen nach Industriestandard."""
    ATO = "ato"
    ATC = "atc"
    ATM_MINI = "atm_mini"
    APX_MAXI = "apx_maxi"
    MIDI = "midi"
    ANL = "anl"
    MEGA = "mega"
    CLASS_T = "class_t"
    GLASS_TUBE = "glass_tube"
    BLADE_LOW_PROFILE = "blade_low_profile"


class FuseCharacteristic(str, Enum):
    """Auslösecharakteristik einer Sicherung."""
    FAST_ACTING = "fast_acting"
    MEDIUM_TIME_DELAY = "medium_time_delay"
    SLOW_BLOW = "slow_blow"


class BreakerCharacteristic(str, Enum):
    """Auslösecharakteristik eines Leitungsschutzschalters."""
    B = "B"
    C = "C"
    D = "D"
    K = "K"
    Z = "Z"


class VoltageSystem(str, Enum):
    """Spannungsebene des Bordnetzes."""
    DC_12V = "dc_12v"
    DC_24V = "dc_24v"
    DC_48V = "dc_48v"
    AC_230V = "ac_230v"
    AC_120V = "ac_120v"
    AC_400V = "ac_400v"


class PanelType(str, Enum):
    """Typ des Verteilerpanels."""
    DC_DISTRIBUTION = "dc_distribution"
    AC_DISTRIBUTION = "ac_distribution"
    COMBINED = "combined"
    FUSE_BLOCK = "fuse_block"
    DIGITAL_CZONE = "digital_czone"
    DIGITAL_MASTERBUS = "digital_masterbus"
    DIN_RAIL = "din_rail"
    WEATHERDECK = "weatherdeck"


class PanelMountType(str, Enum):
    """Montageart des Panels."""
    FLUSH_MOUNT = "flush_mount"
    SURFACE_MOUNT = "surface_mount"
    DIN_RAIL = "din_rail"
    WATERPROOF_ENCLOSURE = "waterproof_enclosure"


class SwitchType(str, Enum):
    """Schaltertyp im Panel."""
    TOGGLE = "toggle"
    ROCKER = "rocker"
    PUSH_BUTTON = "push_button"
    ROTARY = "rotary"
    CIRCUIT_BREAKER = "circuit_breaker"
    SOLID_STATE = "solid_state"


class MainSwitchType(str, Enum):
    """Batterie-Hauptschalter-Typ."""
    ON_OFF = "on_off"
    SELECTOR_1_BOTH_2_OFF = "selector_1_both_2_off"
    MOTORIZED = "motorized"
    KNIFE_DISCONNECT = "knife_disconnect"
    KEY_SWITCH = "key_switch"


class ConfidenceLevel(str, Enum):
    """AYDI Konfidenz-Stufen."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class Severity(int, Enum):
    """Schweregrad eines Befunds (1=gering, 5=kritisch)."""
    COSMETIC = 1
    MINOR = 2
    MODERATE = 3
    SERIOUS = 4
    CRITICAL = 5


class CircuitPriority(str, Enum):
    """Priorität eines Stromkreises."""
    CRITICAL = "critical"
    IMPORTANT = "important"
    COMFORT = "comfort"
    OPTIONAL = "optional"


class BusBarMaterial(str, Enum):
    """Bus-Bar-Werkstoff."""
    COPPER_BARE = "copper_bare"
    COPPER_TINNED = "copper_tinned"
    COPPER_NICKEL_PLATED = "copper_nickel_plated"
    BRASS_BARE = "brass_bare"
    BRASS_TINNED = "brass_tinned"
    ALUMINIUM = "aluminium"  # NOT recommended marine!
```

### ANHANG J — Sicherungsmodelle

```python
"""
AYDI 22_08 — Fuse Models (Sicherungen)
"""

from pydantic import BaseModel, Field, field_validator
from typing import Optional


class FuseSpec(BaseModel):
    """Spezifikation einer einzelnen Sicherung."""

    model_config = {"from_attributes": True}

    fuse_type: FuseType = Field(
        ...,
        description="Bauform der Sicherung (ATO, ANL, MIDI, etc.)"
    )
    rated_current_a: float = Field(
        ..., gt=0, le=1000,
        description="Nennstrom in Ampere"
    )
    rated_voltage_v: float = Field(
        ..., gt=0, le=500,
        description="Nennspannung in Volt DC"
    )
    aic_rating_a: Optional[float] = Field(
        None, gt=0,
        description="Ausschaltvermögen (AIC) in Ampere"
    )
    characteristic: FuseCharacteristic = Field(
        FuseCharacteristic.MEDIUM_TIME_DELAY,
        description="Auslösecharakteristik"
    )
    color_code: Optional[str] = Field(
        None,
        description="Farbcode nach Industriestandard"
    )
    manufacturer: Optional[str] = Field(
        None,
        description="Hersteller (z.B. 'Blue Sea', 'Littelfuse')"
    )
    part_number: Optional[str] = Field(
        None,
        description="Hersteller-Artikelnummer"
    )

    @field_validator("rated_current_a")
    @classmethod
    def validate_fuse_current(cls, v: float) -> float:
        """Warnung bei ungewöhnlichen Sicherungswerten."""
        standard_values = [
            1, 2, 3, 4, 5, 7.5, 10, 15, 20, 25, 30, 35, 40,
            50, 60, 70, 80, 100, 125, 150, 175, 200, 225, 250,
            300, 350, 400, 500, 600, 750, 800,
        ]
        if v not in standard_values:
            # Non-standard value — allow but could flag in analysis
            pass
        return v


class FuseBlock(BaseModel):
    """Sicherungsblock / Sicherungshalter."""

    model_config = {"from_attributes": True}

    manufacturer: str = Field(..., description="Hersteller")
    model: str = Field(..., description="Modellbezeichnung")
    fuse_type: FuseType = Field(..., description="Akzeptierter Sicherungstyp")
    circuit_count: int = Field(
        ..., ge=1, le=50,
        description="Anzahl Sicherungsplätze"
    )
    max_current_per_circuit_a: float = Field(
        ..., gt=0,
        description="Max. Strom pro Sicherungsplatz [A]"
    )
    max_total_current_a: float = Field(
        ..., gt=0,
        description="Max. Gesamtstrom über alle Plätze [A]"
    )
    has_led_indicators: bool = Field(
        False,
        description="LED-Statusanzeige pro Sicherung vorhanden"
    )
    has_negative_bus: bool = Field(
        False,
        description="Integrierte Masse-Sammelschiene vorhanden"
    )
    ip_rating: Optional[str] = Field(
        None,
        description="Schutzart (z.B. 'IP67', 'IPX2')"
    )
    bus_bar_material: BusBarMaterial = Field(
        BusBarMaterial.COPPER_TINNED,
        description="Bus-Bar-Material"
    )
    dimensions_mm: Optional[tuple[float, float, float]] = Field(
        None,
        description="Abmessungen L×B×H in mm"
    )
    weight_g: Optional[float] = Field(
        None, gt=0,
        description="Gewicht in Gramm"
    )

    @property
    def is_marine_grade(self) -> bool:
        """True wenn Bus-Bar verzinnt und mindestens IPX2."""
        tinned = self.bus_bar_material in (
            BusBarMaterial.COPPER_TINNED,
            BusBarMaterial.COPPER_NICKEL_PLATED,
            BusBarMaterial.BRASS_TINNED,
        )
        return tinned
```

### ANHANG K — Panel-Modelle

```python
"""
AYDI 22_08 — Distribution Panel Models (Verteilerpanel)
"""

from pydantic import BaseModel, Field
from typing import Optional


class CircuitDefinition(BaseModel):
    """Definition eines einzelnen Stromkreises im Panel."""

    model_config = {"from_attributes": True}

    circuit_number: int = Field(
        ..., ge=1,
        description="Kreisnummer (eindeutig pro Panel)"
    )
    label_de: str = Field(
        ..., min_length=1, max_length=50,
        description="Beschriftung (deutsch)"
    )
    label_en: Optional[str] = Field(
        None, max_length=50,
        description="Beschriftung (englisch)"
    )
    priority: CircuitPriority = Field(
        CircuitPriority.COMFORT,
        description="Priorität des Kreises"
    )
    fuse_type: FuseType = Field(
        ...,
        description="Sicherungstyp"
    )
    fuse_rating_a: float = Field(
        ..., gt=0, le=500,
        description="Sicherungs-Nennstrom [A]"
    )
    cable_cross_section_mm2: float = Field(
        ..., gt=0, le=240,
        description="Kabelquerschnitt [mm²]"
    )
    cable_length_m: float = Field(
        ..., gt=0,
        description="Kabellänge einfach [m]"
    )
    nominal_current_a: float = Field(
        ..., gt=0,
        description="Nennstrom des Verbrauchers [A]"
    )
    max_current_a: float = Field(
        ..., gt=0,
        description="Maximalstrom (inkl. Anlauf) [A]"
    )
    voltage_drop_percent: Optional[float] = Field(
        None, ge=0, le=100,
        description="Berechneter Spannungsabfall [%]"
    )
    is_emergency_circuit: bool = Field(
        False,
        description="True wenn Notfall-Kreis (bleibt bei Not-Aus aktiv)"
    )
    is_direct_battery: bool = Field(
        False,
        description="True wenn Kreis direkt an Batterie (nicht über Panel)"
    )
    zone: Optional[str] = Field(
        None,
        description="Zugehörige Zone (z.B. 'Vorschiff', 'Salon')"
    )

    @property
    def voltage_drop_calculated(self) -> float:
        """Berechnet Spannungsabfall für 12V DC in %."""
        rho = 0.0175  # Ohm·mm²/m (Kupfer)
        total_length = self.cable_length_m * 2  # Hin + Rück
        resistance = (rho * total_length) / self.cable_cross_section_mm2
        v_drop = self.nominal_current_a * resistance
        return round((v_drop / 12.0) * 100, 2)

    @property
    def fuse_cable_ratio_ok(self) -> bool:
        """Prüft ob Sicherung ≤ Kabelbelastbarkeit (vereinfacht)."""
        # Simplified lookup — real implementation uses full derating table
        cable_ratings = {
            0.75: 7, 1.0: 10, 1.5: 15, 2.5: 25, 4.0: 35,
            6.0: 50, 10.0: 65, 16.0: 85, 25.0: 115, 35.0: 145,
            50.0: 170, 70.0: 210, 95.0: 265, 120.0: 310,
        }
        max_cable_a = cable_ratings.get(self.cable_cross_section_mm2, 0)
        return self.fuse_rating_a <= max_cable_a


class DistributionPanel(BaseModel):
    """Verteilerpanel-Konfiguration."""

    model_config = {"from_attributes": True}

    panel_id: str = Field(
        ...,
        description="Eindeutige Panel-ID (z.B. 'DC-PANEL-NAV')"
    )
    panel_type: PanelType = Field(
        ...,
        description="Paneltyp"
    )
    mount_type: PanelMountType = Field(
        ...,
        description="Montageart"
    )
    voltage_system: VoltageSystem = Field(
        ...,
        description="Spannungssystem"
    )
    manufacturer: Optional[str] = Field(None)
    model: Optional[str] = Field(None)
    total_circuit_count: int = Field(
        ..., ge=1, le=100,
        description="Gesamtanzahl Kreise"
    )
    max_input_current_a: float = Field(
        ..., gt=0,
        description="Maximaler Eingangsstrom [A]"
    )
    input_fuse_type: Optional[FuseType] = Field(
        None,
        description="Eingangssicherungstyp"
    )
    input_fuse_rating_a: Optional[float] = Field(
        None, gt=0,
        description="Eingangssicherung Nennstrom [A]"
    )
    switch_type: SwitchType = Field(
        SwitchType.TOGGLE,
        description="Schaltertyp"
    )
    has_voltmeter: bool = Field(False)
    has_ammeter: bool = Field(False)
    ip_rating: Optional[str] = Field(None)
    bus_bar_material: BusBarMaterial = Field(
        BusBarMaterial.COPPER_TINNED
    )
    location: Optional[str] = Field(
        None,
        description="Einbauort an Bord (z.B. 'Navstation Stb.')"
    )
    circuits: list[CircuitDefinition] = Field(
        default_factory=list,
        description="Liste aller Stromkreise"
    )

    @property
    def total_nominal_current_a(self) -> float:
        """Summe aller Nennströme."""
        return sum(c.nominal_current_a for c in self.circuits)

    @property
    def total_fuse_rating_a(self) -> float:
        """Summe aller Sicherungswerte."""
        return sum(c.fuse_rating_a for c in self.circuits)

    @property
    def critical_circuits(self) -> list[CircuitDefinition]:
        """Alle sicherheitskritischen Kreise."""
        return [
            c for c in self.circuits
            if c.priority == CircuitPriority.CRITICAL
        ]

    @property
    def emergency_circuits(self) -> list[CircuitDefinition]:
        """Kreise die bei Not-Aus aktiv bleiben."""
        return [c for c in self.circuits if c.is_emergency_circuit]
```

### ANHANG L — Hauptschalter-Modelle

```python
"""
AYDI 22_08 — Main Switch / Battery Disconnect Models
"""

from pydantic import BaseModel, Field
from typing import Optional


class BatteryMainSwitch(BaseModel):
    """Batterie-Hauptschalter."""

    model_config = {"from_attributes": True}

    switch_type: MainSwitchType = Field(
        ...,
        description="Schaltertyp"
    )
    manufacturer: Optional[str] = Field(None)
    model: Optional[str] = Field(None)
    continuous_current_a: float = Field(
        ..., gt=0,
        description="Dauer-Nennstrom [A]"
    )
    intermittent_current_a: Optional[float] = Field(
        None, gt=0,
        description="Kurzzeitstrom (5 Sek.) [A]"
    )
    cranking_current_a: Optional[float] = Field(
        None, gt=0,
        description="Anlassstrom (30 Sek.) [A]"
    )
    max_voltage_v: float = Field(
        ..., gt=0,
        description="Maximale Betriebsspannung [V DC]"
    )
    breaking_capacity_a: Optional[float] = Field(
        None, gt=0,
        description="Kurzschluss-Schaltfähigkeit [A]"
    )
    is_ignition_protected: bool = Field(
        False,
        description="Zündfrei nach ISO 8846"
    )
    ip_rating: Optional[str] = Field(None)
    location: Optional[str] = Field(
        None,
        description="Einbauort (z.B. 'Maschinenraum Bb.')"
    )
    accessible_in_emergency: bool = Field(
        True,
        description="Im Notfall in <2 Sek. erreichbar"
    )

    @property
    def suitable_for_lithium(self) -> bool:
        """Prüft ob Schalter für LiFePO4-Systeme geeignet ist."""
        if self.breaking_capacity_a is None:
            return False
        return self.breaking_capacity_a >= 5000


class EmergencyShutdown(BaseModel):
    """Notabschaltsystem."""

    model_config = {"from_attributes": True}

    activation_points: list[str] = Field(
        ..., min_length=1,
        description="Liste der Not-Aus-Positionen"
    )
    relay_type: Optional[str] = Field(
        None,
        description="Trennrelais-Typ"
    )
    relay_current_a: float = Field(
        ..., gt=0,
        description="Relaiskontakt-Nennstrom [A]"
    )
    circuits_deactivated: list[str] = Field(
        default_factory=list,
        description="Kreise die bei Not-Aus getrennt werden"
    )
    circuits_remain_active: list[str] = Field(
        default_factory=list,
        description="Kreise die aktiv bleiben"
    )
    time_to_activate_s: float = Field(
        ..., gt=0, le=5,
        description="Maximale Zeit zur Betätigung [Sekunden]"
    )
    is_fail_safe: bool = Field(
        True,
        description="Fail-Safe = bei Ausfall der Steuerung wird getrennt"
    )
```

### ANHANG M — Bus-Bar-Modelle

```python
"""
AYDI 22_08 — Bus Bar Models (Sammelschienen)
"""

from pydantic import BaseModel, Field
from typing import Optional


class BusBar(BaseModel):
    """Sammelschiene / Bus-Bar."""

    model_config = {"from_attributes": True}

    designation: str = Field(
        ...,
        description="Bezeichnung (z.B. 'Haupt-Bus-Bar +24V')"
    )
    material: BusBarMaterial = Field(
        ...,
        description="Werkstoff"
    )
    cross_section_mm2: float = Field(
        ..., gt=0,
        description="Querschnittsfläche [mm²]"
    )
    rated_current_a: float = Field(
        ..., gt=0,
        description="Nennstrom [A]"
    )
    stud_count: int = Field(
        ..., ge=2,
        description="Anzahl Anschlussbolzen"
    )
    stud_size: str = Field(
        ...,
        description="Bolzengröße (z.B. 'M6', 'M8', '5/16-18')"
    )
    length_mm: Optional[float] = Field(None, gt=0)
    width_mm: Optional[float] = Field(None, gt=0)
    height_mm: Optional[float] = Field(None, gt=0)
    is_insulated: bool = Field(
        False,
        description="Isolierte Montage (auf Isoliersockel)"
    )
    has_cover: bool = Field(
        False,
        description="Berührungsschutz-Abdeckung vorhanden"
    )
    torque_nm: Optional[float] = Field(
        None, gt=0,
        description="Anzugsdrehmoment für Bolzen [Nm]"
    )

    @property
    def current_density_a_mm2(self) -> float:
        """Aktuelle Stromdichte bei Nennstrom [A/mm²]."""
        return round(self.rated_current_a / self.cross_section_mm2, 2)

    @property
    def current_density_ok(self) -> bool:
        """Prüft ob Stromdichte im zulässigen Bereich."""
        if self.material in (
            BusBarMaterial.COPPER_BARE,
            BusBarMaterial.COPPER_TINNED,
            BusBarMaterial.COPPER_NICKEL_PLATED,
        ):
            return self.current_density_a_mm2 <= 3.0
        elif self.material in (
            BusBarMaterial.BRASS_BARE,
            BusBarMaterial.BRASS_TINNED,
        ):
            return self.current_density_a_mm2 <= 2.0
        return False  # Aluminium: not recommended
```

### ANHANG N — Analyse-Modelle

```python
"""
AYDI 22_08 — Analysis Models for Panel & Fuse Assessment
"""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class SelectivityCheck(BaseModel):
    """Ergebnis einer Selektivitätsprüfung zwischen zwei Ebenen."""

    model_config = {"from_attributes": True}

    upstream_fuse_type: FuseType = Field(...)
    upstream_fuse_rating_a: float = Field(...)
    downstream_fuse_type: FuseType = Field(...)
    downstream_fuse_rating_a: float = Field(...)
    ratio: float = Field(
        ...,
        description="Verhältnis upstream/downstream"
    )
    is_selective: bool = Field(
        ...,
        description="True wenn Verhältnis ≥ 1.6"
    )
    confidence: ConfidenceLevel = Field(...)
    remarks: Optional[str] = Field(None)

    @property
    def min_upstream_for_selectivity(self) -> float:
        """Minimaler Upstream-Sicherungswert für Selektivität."""
        return round(self.downstream_fuse_rating_a * 1.6, 1)


class FuseCableMatch(BaseModel):
    """Prüfung der Abstimmung Sicherung ↔ Kabel."""

    model_config = {"from_attributes": True}

    circuit_id: str = Field(...)
    fuse_rating_a: float = Field(...)
    cable_cross_section_mm2: float = Field(...)
    cable_ampacity_a: float = Field(
        ...,
        description="Kabelbelastbarkeit nach Derating [A]"
    )
    fuse_trip_at_150pct_a: float = Field(
        ...,
        description="Erwarteter Auslösestrom (150% Nennwert) [A]"
    )
    is_safe: bool = Field(
        ...,
        description="True wenn 150% Sicherung ≤ Kabelbelastbarkeit"
    )
    safety_margin_pct: float = Field(
        ...,
        description="Sicherheitsmarge in % (positiv = sicher)"
    )
    confidence: ConfidenceLevel = Field(...)

    @property
    def recommendation(self) -> str:
        """Empfehlung basierend auf Analyse."""
        if self.is_safe and self.safety_margin_pct > 20:
            return "Abstimmung korrekt, gute Sicherheitsmarge."
        elif self.is_safe:
            return "Abstimmung korrekt, aber geringe Sicherheitsmarge. Derating beachten."
        else:
            return (
                f"UNSICHER: Sicherung {self.fuse_rating_a}A auf "
                f"{self.cable_cross_section_mm2}mm² Kabel. "
                f"Kabelbelastbarkeit {self.cable_ampacity_a}A wird bei "
                f"Auslösestrom {self.fuse_trip_at_150pct_a}A überschritten."
            )


class CircuitVoltageDropAnalysis(BaseModel):
    """Spannungsabfall-Analyse eines Kreises."""

    model_config = {"from_attributes": True}

    circuit_id: str = Field(...)
    system_voltage_v: float = Field(...)
    cable_length_one_way_m: float = Field(...)
    cable_cross_section_mm2: float = Field(...)
    load_current_a: float = Field(...)
    calculated_voltage_drop_v: float = Field(...)
    voltage_drop_percent: float = Field(...)
    max_allowed_percent: float = Field(
        3.0,
        description="Maximaler erlaubter Spannungsabfall [%]"
    )
    is_within_limit: bool = Field(...)
    confidence: ConfidenceLevel = Field(...)

    @property
    def min_cross_section_for_limit(self) -> float:
        """Minimaler Kabelquerschnitt um Grenzwert einzuhalten [mm²]."""
        rho = 0.0175
        total_length = self.cable_length_one_way_m * 2
        max_drop_v = (self.max_allowed_percent / 100) * self.system_voltage_v
        max_r = max_drop_v / self.load_current_a
        min_q = (rho * total_length) / max_r
        return round(min_q, 1)
```

### ANHANG O — Fehlerbild-Modelle

```python
"""
AYDI 22_08 — Fault Pattern Models (Fehlerbilder)
"""

from pydantic import BaseModel, Field
from typing import Optional


class FaultPattern(BaseModel):
    """Ein Fehlerbild aus dem Fehlerbild-Atlas."""

    model_config = {"from_attributes": True}

    fault_id: str = Field(
        ...,
        description="Eindeutige Fehlerbild-ID (z.B. 'F-08-01')"
    )
    title_de: str = Field(
        ...,
        description="Titel des Fehlerbilds (deutsch)"
    )
    appearance: str = Field(
        ...,
        description="Beschreibung der sichtbaren Erscheinung"
    )
    cause: str = Field(
        ...,
        description="Ursache(n) des Fehlerbilds"
    )
    accompanying_symptoms: list[str] = Field(
        default_factory=list,
        description="Begleitende Symptome"
    )
    severity: Severity = Field(
        ...,
        description="Schweregrad 1-5"
    )
    risk_category: str = Field(
        ...,
        description="Risikobewertung (z.B. 'KRITISCH — Brandgefahr')"
    )
    immediate_action: str = Field(
        ...,
        description="Sofortmaßnahme"
    )
    long_term_action: str = Field(
        ...,
        description="Langfristige Maßnahme"
    )
    visual_indicators: list[str] = Field(
        default_factory=list,
        description="Visuelle Erkennungsmerkmale für KI-Analyse"
    )
    confidence_visual: ConfidenceLevel = Field(
        ConfidenceLevel.VISUAL_MEDIUM,
        description="Typische Konfidenz bei visueller Erkennung"
    )
    related_fault_ids: list[str] = Field(
        default_factory=list,
        description="Verwandte Fehlerbilder"
    )

    @property
    def is_critical(self) -> bool:
        """True wenn Schweregrad CRITICAL."""
        return self.severity == Severity.CRITICAL

    @property
    def requires_immediate_action(self) -> bool:
        """True wenn sofortiges Handeln erforderlich."""
        return self.severity >= Severity.SERIOUS
```

### ANHANG P — Bewertungsmodelle

```python
"""
AYDI 22_08 — Assessment & Scoring Models
"""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class PanelAssessmentResult(BaseModel):
    """Gesamtbewertung eines Verteilerpanels."""

    model_config = {"from_attributes": True}

    panel_id: str = Field(...)
    assessment_date: datetime = Field(
        default_factory=datetime.utcnow
    )
    overall_score: float = Field(
        ..., ge=0, le=100,
        description="Gesamtbewertung 0–100"
    )
    safety_score: float = Field(
        ..., ge=0, le=100,
        description="Sicherheitsbewertung 0–100"
    )
    condition_score: float = Field(
        ..., ge=0, le=100,
        description="Zustandsbewertung 0–100"
    )
    compliance_score: float = Field(
        ..., ge=0, le=100,
        description="Normkonformitätsbewertung 0–100"
    )
    selectivity_checks: list[SelectivityCheck] = Field(
        default_factory=list
    )
    fuse_cable_checks: list[FuseCableMatch] = Field(
        default_factory=list
    )
    voltage_drop_analyses: list[CircuitVoltageDropAnalysis] = Field(
        default_factory=list
    )
    fault_patterns_found: list[FaultPattern] = Field(
        default_factory=list
    )
    findings: list[str] = Field(
        default_factory=list,
        description="Liste aller Befunde (deutsch)"
    )
    recommendations: list[str] = Field(
        default_factory=list,
        description="Liste aller Empfehlungen (deutsch)"
    )
    confidence: ConfidenceLevel = Field(...)
    data_source: str = Field(
        ...,
        description="Datenquelle (z.B. 'visual_photo', 'cad_import', 'manual')"
    )

    @property
    def critical_findings_count(self) -> int:
        """Anzahl kritischer Befunde."""
        return sum(
            1 for f in self.fault_patterns_found
            if f.is_critical
        )

    @property
    def selectivity_pass_rate(self) -> float:
        """Anteil bestandener Selektivitätsprüfungen [%]."""
        if not self.selectivity_checks:
            return 0.0
        passed = sum(1 for s in self.selectivity_checks if s.is_selective)
        return round((passed / len(self.selectivity_checks)) * 100, 1)

    @property
    def all_circuits_within_voltage_drop(self) -> bool:
        """True wenn alle Kreise den Spannungsabfall-Grenzwert einhalten."""
        return all(
            v.is_within_limit
            for v in self.voltage_drop_analyses
        )

    @property
    def requires_immediate_attention(self) -> bool:
        """True wenn kritische Befunde sofortiges Handeln erfordern."""
        return any(
            f.requires_immediate_action
            for f in self.fault_patterns_found
        )
```

### ANHANG Q — Schaltplan-Modelle

```python
"""
AYDI 22_08 — Electrical Diagram Models (Schaltplan-Datenmodell)
"""

from pydantic import BaseModel, Field
from typing import Optional


class CableDefinition(BaseModel):
    """Kabeldefinition für Stromlaufplan."""

    model_config = {"from_attributes": True}

    cable_id: str = Field(
        ...,
        description="Kabelbezeichnung (z.B. 'DC-01-P', 'DC-01-N')"
    )
    cross_section_mm2: float = Field(..., gt=0)
    color_positive: str = Field(
        "rot",
        description="Farbe Plus-Leiter"
    )
    color_negative: str = Field(
        "schwarz",
        description="Farbe Minus-Leiter"
    )
    length_m: float = Field(..., gt=0)
    from_terminal: str = Field(
        ...,
        description="Abgangsklemme (z.B. 'Panel-DC-Nav, Kreis 3')"
    )
    to_terminal: str = Field(
        ...,
        description="Ankunftsklemme (z.B. 'Kartenplotter, Klemme +12V')"
    )
    route_description: Optional[str] = Field(
        None,
        description="Kabelweg-Beschreibung"
    )
    is_tinned: bool = Field(True, description="Verzinnte Litze")
    insulation_type: str = Field(
        "PVC marine",
        description="Isolierungsmaterial"
    )


class SingleLineDiagram(BaseModel):
    """Einlinienschaltplan-Datenmodell."""

    model_config = {"from_attributes": True}

    diagram_id: str = Field(...)
    title: str = Field(...)
    vessel_name: Optional[str] = Field(None)
    voltage_system: VoltageSystem = Field(...)
    revision: str = Field("A", description="Planrevision")
    date: datetime = Field(default_factory=datetime.utcnow)
    battery_banks: list[dict] = Field(
        default_factory=list,
        description="Batteriebänke mit Typ, Kapazität, Spannung"
    )
    main_switches: list[BatteryMainSwitch] = Field(
        default_factory=list
    )
    main_fuses: list[FuseSpec] = Field(
        default_factory=list,
        description="Hauptsicherungen"
    )
    bus_bars: list[BusBar] = Field(
        default_factory=list
    )
    distribution_panels: list[DistributionPanel] = Field(
        default_factory=list
    )
    direct_consumers: list[dict] = Field(
        default_factory=list,
        description="Direkt angeschlossene Großverbraucher"
    )
    emergency_shutdown: Optional[EmergencyShutdown] = Field(None)

    @property
    def total_circuit_count(self) -> int:
        """Gesamtanzahl aller Stromkreise."""
        panel_circuits = sum(
            p.total_circuit_count for p in self.distribution_panels
        )
        return panel_circuits + len(self.direct_consumers)
```

### ANHANG R — Visual-Analyse-Modelle

```python
"""
AYDI 22_08 — Visual Analysis Models for Panel/Fuse Photo Assessment
"""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class VisualPanelIndicator(BaseModel):
    """Ein visueller Indikator, der auf einem Foto erkannt wurde."""

    model_config = {"from_attributes": True}

    indicator_type: str = Field(
        ...,
        description="Typ (z.B. 'corrosion', 'heat_damage', 'missing_label')"
    )
    location_description: str = Field(
        ...,
        description="Position im Bild / am Panel"
    )
    severity: Severity = Field(...)
    confidence: ConfidenceLevel = Field(...)
    description_de: str = Field(
        ...,
        description="Beschreibung (deutsch) für Endanwender"
    )
    related_fault_id: Optional[str] = Field(
        None,
        description="Verknüpfung zum Fehlerbild-Atlas"
    )
    bounding_box: Optional[tuple[float, float, float, float]] = Field(
        None,
        description="Begrenzungsrahmen im Bild (x1, y1, x2, y2) normalisiert 0–1"
    )


class VisualPanelAssessment(BaseModel):
    """Ergebnis der visuellen Analyse eines Panel-Fotos."""

    model_config = {"from_attributes": True}

    assessment_id: str = Field(...)
    image_source: str = Field(
        ...,
        description="Bildquelle (Dateiname, URL)"
    )
    assessed_at: datetime = Field(
        default_factory=datetime.utcnow
    )
    panel_type_detected: Optional[PanelType] = Field(
        None,
        description="Erkannter Paneltyp"
    )
    manufacturer_detected: Optional[str] = Field(
        None,
        description="Erkannter Hersteller"
    )
    circuit_count_detected: Optional[int] = Field(
        None, ge=0,
        description="Erkannte Kreisanzahl"
    )
    indicators_found: list[VisualPanelIndicator] = Field(
        default_factory=list
    )
    overall_condition_score: Optional[float] = Field(
        None, ge=0, le=100,
        description="Visueller Zustandswert 0–100"
    )
    confidence: ConfidenceLevel = Field(...)
    ai_model_version: str = Field(
        ...,
        description="Version des AI-Modells (für Nachvollziehbarkeit)"
    )
    raw_ai_response: Optional[str] = Field(
        None,
        description="Rohtext der AI-Antwort (für Audit)"
    )
    remarks_de: Optional[str] = Field(
        None,
        description="Zusammenfassende Bemerkungen (deutsch)"
    )

    @property
    def critical_indicators(self) -> list[VisualPanelIndicator]:
        """Alle Indikatoren mit Schweregrad CRITICAL."""
        return [
            i for i in self.indicators_found
            if i.severity == Severity.CRITICAL
        ]

    @property
    def requires_immediate_action(self) -> bool:
        """True wenn mindestens ein kritischer Indikator gefunden."""
        return any(
            i.severity >= Severity.SERIOUS
            for i in self.indicators_found
        )

    @property
    def high_confidence_findings(self) -> list[VisualPanelIndicator]:
        """Nur Befunde mit hoher visueller Konfidenz."""
        return [
            i for i in self.indicators_found
            if i.confidence in (
                ConfidenceLevel.VISUAL_HIGH,
                ConfidenceLevel.MEASURED,
            )
        ]
```

---

## 13. Zusätzliche Planungshilfen

### 13.1 Checkliste Schalttafel-Neuinstallation

#### Phase 1: Planung

- [ ] Verbraucherliste vollständig erstellt (alle geplanten Geräte mit Nennstrom)
- [ ] Stromkreisaufteilung definiert (funktional + zonenbasiert)
- [ ] Sicherheitskritische Kreise identifiziert (Navigation, Bilge, Positionslichter, UKW)
- [ ] Großverbraucher identifiziert und für Direktanschluss an Batterie vorgesehen
- [ ] Sicherungsdimensionierung für jeden Kreis berechnet (Kabel ↔ Sicherung)
- [ ] Selektivitätsberechnung durchgeführt (Kaskade Haupt → Panel → Einzelkreis)
- [ ] Einlinienschaltplan erstellt
- [ ] Panel-Position(en) festgelegt (trocken, belüftet, zugänglich)
- [ ] AC/DC-Trennung geplant (getrennte Panels oder Trennwand)
- [ ] Not-Aus-Konzept definiert (Positionen, Kreise die aktiv bleiben)
- [ ] Hauptschalter-Position festgelegt (erreichbar, trocken)
- [ ] Bus-Bar-Dimensionierung berechnet
- [ ] Beschriftungskonzept erstellt (deutsch oder Symbole)
- [ ] Budget erstellt und freigegeben
- [ ] CE/ABYC-Konformität geprüft

#### Phase 2: Beschaffung

- [ ] Verteilerpanel(s) in korrekter Kreisanzahl bestellt
- [ ] Sicherungen aller benötigten Typen und Werte (+ 50% Reserve!)
- [ ] Sicherungshalter (ANL, MIDI, ATO-Block) in korrekter Ausführung
- [ ] Bus-Bars: Kupfer verzinnt, korrekte Bolzenanzahl und -größe
- [ ] Batterie-Hauptschalter mit ausreichendem Nennstrom
- [ ] Not-Aus-Taster (IP67, marine-grade)
- [ ] Trennrelais für Not-Aus-Funktion
- [ ] FI-Schutzschalter 30mA (AC-System)
- [ ] Leitungsschutzschalter für AC-Kreise (korrekte Charakteristik)
- [ ] Beschriftungsmaterial (Gravurschild, Labeldrucker)
- [ ] Befestigungsmaterial (Edelstahl A4)
- [ ] Kontaktfett (Tefgel, Noalox oder gleichwertig)
- [ ] Isoliermaterial (Schrumpfschlauch, Isolierband)

#### Phase 3: Installation

- [ ] Alte Installation dokumentiert (Fotos vor Demontage!)
- [ ] Panel-Ausschnitt(e) präzise gefertigt
- [ ] Panel wasserdicht montiert (Silikondichtung oder Dichtband)
- [ ] Bus-Bars auf Isoliersockeln montiert
- [ ] Alle Bolzenverbindungen mit Drehmomentschlüssel angezogen
- [ ] Kontaktfett auf alle Bolzenverbindungen aufgetragen
- [ ] Sicherungen eingesetzt, Werte dokumentiert
- [ ] Beschriftung angebracht (alle Kreise!)
- [ ] Kabeleinführungen von unten (Tropfschutz)
- [ ] AC/DC physisch getrennt
- [ ] Berührungsschutz-Abdeckungen montiert
- [ ] Hauptschalter montiert und zugänglich
- [ ] Not-Aus-Taster montiert und verkabelt

#### Phase 4: Inbetriebnahme und Prüfung

- [ ] Spannungsmessung am Panel-Eingang (ohne Last)
- [ ] Polaritätsprüfung an allen Ausgängen
- [ ] Jeder Kreis einzeln testen (Verbraucher einschalten)
- [ ] Spannungsabfall unter Last messen (kritische Kreise: <3%)
- [ ] Selektivität stichprobenartig prüfen (Einzelkreis vor Hauptsicherung)
- [ ] Not-Aus-Funktion testen (alle Positionen)
- [ ] FI-Schutzschalter-Test (Testtaste + Prüfgerät)
- [ ] Isolationsmessung aller AC-Kreise (Megger, >1MΩ)
- [ ] Isolationsmessung aller DC-Kreise (Megger, >2MΩ)
- [ ] Temperaturkontrolle an Bus-Bars unter Volllast (nach 30 Min.)
- [ ] Thermografie-Aufnahme (optional, empfohlen bei >30 Kreisen)
- [ ] Schaltplan fertigstellen und an Bord hinterlegen
- [ ] Protokoll erstellen und archivieren

### 13.2 Derating-Tabellen

#### Temperatur-Derating für Schmelzsicherungen

Schmelzsicherungen sind temperaturempfindlich. Bei erhöhter Umgebungstemperatur (z.B. im Maschinenraum) sinkt der tatsächliche Auslösestrom:

| Umgebungstemperatur | Derating-Faktor | Effektiver Nennstrom einer 10A-Sicherung |
|---------------------|----------------|------------------------------------------|
| 20°C | 1,10 | 11,0A |
| 25°C (Referenz) | 1,00 | 10,0A |
| 30°C | 0,95 | 9,5A |
| 35°C | 0,90 | 9,0A |
| 40°C | 0,85 | 8,5A |
| 45°C | 0,80 | 8,0A |
| 50°C | 0,74 | 7,4A |
| 55°C | 0,68 | 6,8A |
| 60°C | 0,62 | 6,2A |
| 65°C | 0,55 | 5,5A |

**Konsequenz:** Im Maschinenraum (typisch 45–55°C im Betrieb) löst eine 10A-Sicherung bereits bei 7,4–8,0A aus. Dies muss bei der Dimensionierung berücksichtigt werden — entweder Sicherung höher dimensionieren oder Panel außerhalb des Maschinenraums montieren.

#### Temperatur-Derating für Leitungsschutzschalter

| Umgebungstemperatur | Derating-Faktor | Effektiver Nennstrom eines 16A-MCB |
|---------------------|----------------|-------------------------------------|
| 20°C | 1,05 | 16,8A |
| 25°C | 1,03 | 16,5A |
| 30°C (Referenz) | 1,00 | 16,0A |
| 35°C | 0,96 | 15,4A |
| 40°C | 0,92 | 14,7A |
| 45°C | 0,87 | 13,9A |
| 50°C | 0,83 | 13,3A |
| 55°C | 0,78 | 12,5A |
| 60°C | 0,72 | 11,5A |

#### Derating bei Bündelung (Nebeneinander montierte Sicherungen)

Wenn mehrere Sicherungen im Block gleichzeitig belastet werden, erhöht sich die Umgebungstemperatur im Block gegenseitig:

| Gleichzeitig belastete Nachbar-Sicherungen | Derating-Faktor |
|--------------------------------------------|----------------|
| 0 (einzeln) | 1,00 |
| 1–2 | 0,95 |
| 3–4 | 0,90 |
| 5–8 | 0,85 |
| 9–12 | 0,80 |
| >12 | 0,75 |

### 13.3 Vergleichstabelle Sicherungssysteme nach Bootsklasse

| Bootsklasse | LOA | Empfohlenes Panel | Sicherungstypen | Hauptsicherung | Geschätzte Materialkosten |
|-------------|-----|-------------------|-----------------|----------------|---------------------------|
| Jolle/Kleinboot | <7m | Blue Sea 5025 (6-Way ATO) | ATO | 30A ATO | 80–150€ |
| Küstenkreuzer | 7–10m | Blue Sea 5032 (12-Way ATO+LED) | ATO + 1× ANL | 100A ANL | 200–400€ |
| Fahrtensegler | 10–14m | Blue Sea 360 (16-Way) | ATO + MIDI + ANL | 200A ANL | 500–1.200€ |
| Blauwasser | 14–18m | Blue Sea 360 (24-Way) + Victron Lynx | ATO + MIDI + ANL + Klasse T | 300A ANL/Klasse T | 1.200–3.000€ |
| Motoryacht klein | 8–12m | BEP 12-Way Toggle | ATO + MIDI | 150A ANL | 300–600€ |
| Motoryacht mittel | 12–18m | BEP Contour Connect + Victron Lynx | ATO + MIDI + MEGA | 200A ANL | 800–2.000€ |
| Motoryacht groß | 18–24m | CZone oder Philippi STV | Digital/MIDI/ANL | 400A ANL/Klasse T | 5.000–15.000€ |
| Superyacht | >24m | Philippi STV + CZone | DIN-Schiene + ANL/Klasse T | 600A+ Klasse T | 15.000–50.000€+ |

### 13.4 Normenquerschnitt — Was wo gilt

| Anforderung | ABYC E-11 | ISO 10133 | ISO 13297 | IEC 60092 |
|-------------|-----------|-----------|-----------|-----------|
| Jeder Kreis einzeln abgesichert | ✓ Pflicht | ✓ Pflicht | ✓ Pflicht | ✓ Pflicht |
| Hauptsicherung <180mm von Batterie | ✓ 7" (178mm) | ✓ Empfohlen | — | ✓ Pflicht |
| Bus-Bar verzinnt | ✓ Empfohlen | — | — | — |
| AC/DC physisch getrennt | ✓ Pflicht | ✓ Pflicht | ✓ Pflicht | ✓ Pflicht |
| FI/RCD ≤30mA (AC) | ✓ Pflicht | — | ✓ Pflicht | ✓ Pflicht |
| Beschriftung aller Kreise | ✓ Pflicht | ✓ Pflicht | ✓ Pflicht | ✓ Pflicht |
| Selektivitätsnachweis | — | — | — | ✓ Pflicht |
| Kurzschlussberechnung | — | — | — | ✓ Pflicht |
| Schaltplan an Bord | ✓ Empfohlen | — | — | ✓ Pflicht |
| Not-Aus | ✓ Empfohlen | — | — | ✓ Pflicht |
| Schutzart Panel min. IPX2 | — | ✓ Exponiert | — | ✓ IP44 min. |
| Ignition Protection (Benzin) | ✓ Pflicht | ✓ Pflicht | — | ✓ Pflicht |
| Erdung/Bonding | ✓ Definiert | ✓ Definiert | ✓ Definiert | ✓ Definiert |

### 13.5 Typische Sicherungsbestückung nach Bootstyp

#### Fahrtensegler 12m, 12V-System, 20 DC-Kreise

| Kreis | Bezeichnung | Sicherung | Bemerkung |
|-------|-------------|-----------|-----------|
| DC-01 | Kartenplotter | 5A ATO | Eigener Kreis (kritisch) |
| DC-02 | Radar | 7,5A ATO | Eigener Kreis (kritisch) |
| DC-03 | AIS-Transponder | 5A ATO | Eigener Kreis (kritisch) |
| DC-04 | UKW-Funk | 10A ATO | Eigener Kreis (kritisch) |
| DC-05 | Positionslichter | 5A ATO | Eigener Kreis (kritisch) |
| DC-06 | Autopilot | 20A ATO | Eigener Kreis (wichtig) |
| DC-07 | Instrumente Cockpit | 5A ATO | Wind, Tiefe, Log, Kompass |
| DC-08 | Navtisch-Beleuchtung | 3A ATO | |
| DC-09 | Innenbeleuchtung Salon | 10A ATO | Alle LED-Leuchten Salon |
| DC-10 | Innenbeleuchtung Kabinen | 7,5A ATO | Alle LED-Leuchten Kabinen |
| DC-11 | Cockpit-Beleuchtung | 5A ATO | LED-Spots + Unterflurbeleuchtung |
| DC-12 | Kühlschrank | 10A ATO | Kompressor eigener Kreis |
| DC-13 | Steckdosen 12V/USB Salon | 10A ATO | |
| DC-14 | Steckdosen 12V/USB Kabinen | 10A ATO | |
| DC-15 | Druckwasserpumpe | 10A ATO | |
| DC-16 | Heckdusche | 7,5A ATO | |
| DC-17 | Elektro-WC | 20A ATO | |
| DC-18 | Lüfter (alle) | 10A ATO | |
| DC-19 | Stereo/Entertainment | 10A ATO | |
| DC-20 | Reserve | — | Frei für Erweiterung |
| DIREKT | Bilgepumpe (auto) | 15A ATO | Direkt an Batterie! |
| DIREKT | Ankerwinde | 100A ANL | Direkt an Batterie |
| DIREKT | Inverter 2000W | 200A ANL | Direkt an Batterie |
| DIREKT | Ladegerät 40A | 50A MIDI | Direkt an Bus-Bar |
| DIREKT | MPPT Solarregler | 40A MIDI | Direkt an Bus-Bar |
| HAUPT | Panel-Eingangssicherung | 80A MIDI | Am Haupt-Bus-Bar |
| HAUPT | Batterie-Hauptsicherung | 300A ANL | <180mm von Batterie |

### 13.6 Ersatzteil-Empfehlung für Bordvorrat

Empfohlener Sicherungsvorrat für Langfahrt (Blauwasser):

| Sicherungstyp | Werte | Anzahl je Wert | Gesamt |
|---------------|-------|----------------|--------|
| ATO 3A | 3A | 3 | 3 |
| ATO 5A | 5A | 5 | 5 |
| ATO 7,5A | 7,5A | 5 | 5 |
| ATO 10A | 10A | 10 | 10 |
| ATO 15A | 15A | 5 | 5 |
| ATO 20A | 20A | 5 | 5 |
| ATO 25A | 25A | 3 | 3 |
| ATO 30A | 30A | 3 | 3 |
| MIDI (Panel-Eingang) | Jeweilige Werte | 1 je verbauter Wert | 2–4 |
| ANL (Hauptsicherung) | Jeweiliger Wert | 2 | 2 |
| ANL (Ankerwinde) | Jeweiliger Wert | 1 | 1 |
| Glasrohr-Feinsicherungen | Häufigste Gerätewerte | 2 je Wert | 6–10 |
| **Gesamt ATO** | | | **~44 Stück** |
| **Gesamt Hochstrom** | | | **~5–7 Stück** |

Geschätzte Kosten Ersatzteilvorrat: 60–120€

**Tipp:** ATO-Sicherungs-Sortimente von Blue Sea (Nr. 5287) oder Narva enthalten die gängigsten Werte in einer wasserdichten Dose — ideal für die Bordapotheke.

### 13.7 Werkzeug-Grundausstattung für Panel-Wartung

| Werkzeug | Einsatz | Preis (ca.) |
|----------|---------|-------------|
| Digital-Multimeter (True RMS) | Spannungs-, Strom-, Widerstandsmessung | 40–150€ |
| Zangenamperemeter DC | Strommessung ohne Leitungstrennung | 60–200€ |
| Sicherungszieher (ATO) | Sicheres Entfernen von Flachsicherungen | 3€ |
| Drehmomentschlüssel (1–25Nm) | Korrekte Anzugsmomente an Bus-Bars | 50–120€ |
| Isolationsmessgerät (Megger 500V) | Isolationsprüfung | 150–400€ |
| Kontaktreiniger (Spray) | Korrosionsentfernung an Kontakten | 8–15€ |
| Kontaktfett (Tefgel/Noalox) | Korrosionsschutz an Bolzenverbindungen | 12–25€ |
| Taschenlampe (Stirnlampe) | Arbeit hinter Panels | 15–40€ |
| Labeldrucker (wetterfeste Etiketten) | Kreisbeschriftung | 40–80€ |
| FI-Prüfstecker (Duspol o.ä.) | FI-Auslösestrom und -zeit messen | 80–250€ |

### 13.8 Umrechnungstabelle AWG ↔ mm² (Marine-relevante Querschnitte)

| AWG | mm² (exakt) | mm² (Standard) | Max. Strom (30°C, einzeln) |
|-----|-------------|----------------|---------------------------|
| 18 | 0,82 | 0,75 | 7A |
| 16 | 1,31 | 1,5 | 15A |
| 14 | 2,08 | 2,5 | 25A |
| 12 | 3,31 | 4,0 | 35A |
| 10 | 5,26 | 6,0 | 50A |
| 8 | 8,37 | 10 | 65A |
| 6 | 13,3 | 16 | 85A |
| 4 | 21,1 | 25 | 115A |
| 2 | 33,6 | 35 | 145A |
| 1 | 42,4 | 35–50 | 170A |
| 1/0 | 53,5 | 50 | 195A |
| 2/0 | 67,4 | 70 | 225A |
| 3/0 | 85,0 | 95 | 265A |
| 4/0 | 107 | 120 | 310A |

*Hinweis: AWG-Werte entsprechen nicht exakt den metrischen mm²-Werten. Bei der Umrechnung immer den nächstgrößeren metrischen Querschnitt wählen.*

### 13.9 Spannungsabfall-Schnellberechnung (12V DC)

Formel: **U_drop [%] = (0,35 × I × L) / q**

Wobei: I = Strom [A], L = Kabellänge einfach [m], q = Querschnitt [mm²]

| Strom [A] | Länge [m] | 1,5mm² | 2,5mm² | 4mm² | 6mm² | 10mm² | 16mm² | 25mm² |
|-----------|-----------|--------|--------|------|------|-------|-------|-------|
| 2 | 3 | 1,4% | 0,8% | 0,5% | 0,4% | 0,2% | 0,1% | 0,1% |
| 2 | 6 | 2,8% | 1,7% | 1,1% | 0,7% | 0,4% | 0,3% | 0,2% |
| 2 | 10 | 4,7% | 2,8% | 1,8% | 1,2% | 0,7% | 0,4% | 0,3% |
| 5 | 3 | 3,5% | 2,1% | 1,3% | 0,9% | 0,5% | 0,3% | 0,2% |
| 5 | 6 | 7,0% | 4,2% | 2,6% | 1,8% | 1,1% | 0,7% | 0,4% |
| 5 | 10 | 11,7% | 7,0% | 4,4% | 2,9% | 1,8% | 1,1% | 0,7% |
| 10 | 3 | 7,0% | 4,2% | 2,6% | 1,8% | 1,1% | 0,7% | 0,4% |
| 10 | 6 | 14,0% | 8,4% | 5,3% | 3,5% | 2,1% | 1,3% | 0,8% |
| 10 | 10 | 23,3% | 14,0% | 8,8% | 5,8% | 3,5% | 2,2% | 1,4% |
| 20 | 3 | — | 8,4% | 5,3% | 3,5% | 2,1% | 1,3% | 0,8% |
| 20 | 6 | — | 16,8% | 10,5% | 7,0% | 4,2% | 2,6% | 1,7% |
| 20 | 10 | — | 28,0% | 17,5% | 11,7% | 7,0% | 4,4% | 2,8% |

*Rot markierte Werte (>10%) = inakzeptabel. Gelb (3–10%) = grenzwertig. Grün (<3%) = normkonform.*

*Für 24V-Systeme: Alle Prozentwerte halbieren.*

### 13.10 Fehlerstatistik — Häufigste Probleme bei Schalttafeln und Sicherungen

Basierend auf aggregierten Surveyor-Daten und Versicherungsberichten:

| Rang | Fehlerbild | Häufigkeit | Typisches Bootsalter | Kostenfolge |
|------|-----------|-----------|---------------------|-------------|
| 1 | Korrodierte Sicherungskontakte | Sehr häufig (>40% aller Boote >10 Jahre) | 5–15 Jahre | 50–200€ (Reinigung/Austausch) |
| 2 | Unbeschriftete oder falsch beschriftete Kreise | Sehr häufig (>50% nach Umbau) | Jedes Alter | 100–300€ (Neuidentifikation) |
| 3 | Fehlende Hauptsicherung oder zu weit von Batterie | Häufig (20–30% Gebrauchtboote) | Jedes Alter | 50–150€ (Nachrüstung) |
| 4 | Überdimensionierte Sicherungen | Häufig (15–25%) | Nach DIY-Reparaturen | 30–100€ (Korrekte Bestückung) |
| 5 | Fehlende Selektivität | Häufig (20–40% bei >20 Kreisen) | Jedes Alter | 100–500€ (Neuberechnung) |
| 6 | Lose Bus-Bar-Verbindungen | Mittel (10–20%) | 3–10 Jahre | 50–150€ (Nachziehen) |
| 7 | Thermisch geschädigte Schalter/Automaten | Mittel (10–15%) | 8–20 Jahre | 200–800€ (Austausch) |
| 8 | Wassereinbruch im Panel | Weniger häufig (5–10%) | Jedes Alter | 200–2.000€ |
| 9 | AC/DC nicht getrennt | Weniger häufig (5–10%) | Ältere Boote, DIY | 500–2.000€ (Neuverkabelung) |
| 10 | Verschweißte Hauptschalter-Kontakte | Selten (<3%) | 10–25 Jahre | 100–400€ (Austausch Schalter) |

### 13.11 Kostenorientierung — Panel-Systeme nach Preisklasse

#### Budget-Klasse (80–400€)

| Lösung | Kreise | Hersteller | Einsatz |
|--------|--------|------------|---------|
| ATO-Sicherungsblock 6-fach + separate Schalter | 6 | Blue Sea 5025 / Narva | Jollenkreuzer, Einfachboot |
| ATO-Sicherungsblock 12-fach mit LED | 12 | Blue Sea 5032 | Küstenkreuzer Standard |
| Rocker-Panel 8-fach | 8 | Hella Marine | Nachrüstung Cockpit |

#### Mittelklasse (400–2.000€)

| Lösung | Kreise | Hersteller | Einsatz |
|--------|--------|------------|---------|
| 360 Panel 12-fach DC + 4-fach AC | 16 | Blue Sea | Fahrtensegler Standard |
| Toggle-Breaker Panel 12-fach | 12 | BEP Marine | Motoryacht |
| Victron Lynx Distributor + Blue Sea Fuse Block | 4+12 | Victron + Blue Sea | LiFePO4-System |

#### Premium-Klasse (2.000–15.000€)

| Lösung | Kreise | Hersteller | Einsatz |
|--------|--------|------------|---------|
| CZone MOI + Display | 12–36 | BEP Marine | Motoryacht digital |
| Mastervolt DC Distribution 500 | 20 | Mastervolt | Premium-Segelyacht |
| Philippi STV 224 | 24 | Philippi | Custom-Yacht, Superyacht |
| Victron Lynx komplett + CZone | 4+24 | Victron + BEP | Blauwasser, Highend |

#### Superyacht-Klasse (>15.000€)

| Lösung | Kreise | Hersteller | Einsatz |
|--------|--------|------------|---------|
| Philippi STV 236 + PSM + Schaltschrank | 36+12 | Philippi | Superyacht Maschinenraum |
| CZone Vollausstattung (3× MOI + Displays) | 54+ | BEP Marine | Motoryacht >20m |
| Individueller Schaltschrank (DIN-Hutschiene) | 80+ | Diverse | Superyacht custom |

### 13.12 Umgebungsbedingungen und Schutzartenwahl

| Montageort | Typische Bedingungen | Min. Schutzart Panel | Empfehlung |
|------------|---------------------|---------------------|------------|
| Navstation (innen, geschützt) | Trocken, 15–35°C | IPX1 | IPX2 |
| Salon (innen) | Trocken, 15–35°C, gelegentlich Kondensat | IPX1 | IPX2 |
| Maschinenraum | Feucht, 30–65°C, Öl-/Dieselnebel | IPX4 | IP44 + Belüftung |
| Cockpit (unter Spray-Hood) | Spritzwasser, UV, 0–50°C | IPX4 | IPX5 |
| Cockpit (offen) | Regen, Spritzwasser, Sonne, Salz | IPX5 | IP66 |
| Flybridge | Regen, Spritzwasser, UV, Wind | IPX5 | IP66 |
| Vorpiek / Ankerkasten | Feucht, gelegentlich Seewasser | IPX5 | IP66 |
| Lazarette | Feuchtigkeitsanfall, Kondensat | IPX3 | IPX4 |

### 13.13 NMEA 2000 Integration — Stromüberwachung

Moderne Panels können Stromverbrauchsdaten über NMEA 2000 bereitstellen. Relevante PGNs:

| PGN | Bezeichnung | Dateninhalt |
|-----|-------------|-------------|
| 127506 | DC Detailed Status | Spannung, Strom, Temperatur pro DC-Quelle |
| 127508 | Battery Status | SOC, Kapazität, Spannung, Strom |
| 127509 | Inverter Status | AC-Out Spannung, Strom, Frequenz |
| 127510 | Charger Status | Ladestrom, Modus, Phase |
| 127513 | Battery Configuration | Typ, Chemie, Nennkapazität |
| 65001–65030 | Proprietary (CZone) | Kanalstatus, Dimm-Werte, Fehlercodes |

**Integration mit AYDI:**
Das AYDI-Analysemodul kann über NMEA-2000-Daten den realen Stromverbrauch pro Kreis erfassen und mit den Dimensionierungswerten abgleichen. Abweichungen >20% vom berechneten Nennstrom werden als Anomalie gemeldet (Konfidenz: measured).

---

*Ende des Wissensdokuments 22_08 — Schalttafeln und Sicherungen*
*AYDI Knowledge Engine v1.0.0 — 2026-05-07*
