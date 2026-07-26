---
title: "Steueranlagen Grundlagen und Typen"
kategorie: "14 Steueranlagen und Autopilot"
unterkategorie: "14.01 Grundlagen und Typen"
version: "1.0.0"
datum: "2026-04-26"
autor: "AYDI Research"
status: "validated"
confidence_quellen:
  - measured: "Hersteller-TDS, ISO 8847/10592, ABYC P-21, CE-Zertifizierungen"
  - documented: "Hersteller-Kataloge, Werftunterlagen, Montageleitfaeden"
  - estimated: "Erfahrungswerte, Regatta-/Fahrtensegel-Praxis, Werft-Konsens"
---

# 14.01 — Steueranlagen Grundlagen und Typen im Yachtbau: Vollstaendige Wissensreferenz

> **AYDI Wissensdatei 14.01** — Kategorie 14: Steueranlagen und Autopilot
> **Confidence-Quelle:** measured (Hersteller-TDS, ISO-Normen), documented (Hersteller-Kataloge, Werftunterlagen), estimated (Erfahrungswerte, Praxis)
> **Letzte Aktualisierung:** 2026-04-26

---

## Inhaltsverzeichnis

1. [Einfuehrung und Uebersicht](#1-einfuehrung-und-uebersicht)
2. [Grundlagen und Theorie](#2-grundlagen-und-theorie)
3. [Typenuebersicht](#3-typenuebersicht)
4. [Dimensionierung und Auslegung](#4-dimensionierung-und-auslegung)
5. [Produktlinien und Hersteller](#5-produktlinien-und-hersteller)
6. [Normen und Vorschriften](#6-normen-und-vorschriften)
7. [Fehlerbild-Atlas](#7-fehlerbild-atlas)
8. [Troubleshooting](#8-troubleshooting)
9. [FAQ — Haeufig gestellte Fragen](#9-faq--haeufig-gestellte-fragen)
10. [Glossar](#10-glossar)
11. [Schnell-Referenz](#11-schnell-referenz)
12. [ANHANG A–R](#12-anhang-ar)

---

## 1. Einfuehrung und Uebersicht

### 1.1 Definition und Funktion

Steueranlagen (engl. steering systems) bilden die mechanische, hydraulische oder elektrische Verbindung zwischen der Ruderbedienung (Pinne, Steuerrad) und dem Ruderblatt. Sie sind ein sicherheitskritisches System: Ein Versagen der Steueranlage fuehrt unmittelbar zum Verlust der Manoevrierbarkeit und stellt eine ernste Gefahr fuer Schiff und Besatzung dar.

Die grundlegende Funktion einer Steueranlage umfasst vier Elemente:

1. **Kraftuebertragung** — Umsetzung der Bedienungskraft (Hand/Fuss) in ein Drehmoment am Ruderschaft
2. **Untersetzung** — Mechanische, hydraulische oder elektrische Verstaerkung der Eingangskraft auf das erforderliche Ruderschaftmoment
3. **Rueckmeldung (Feedback)** — Uebermittlung des Ruderdrucks (Ruderfeedback) an den Steuermann als taktile Information
4. **Lagesicherung** — Halten des eingeschlagenen Ruderwinkels gegen hydrodynamische Kraefte

Im AYDI-Analysesystem zaehlen Steueranlagen zu den Tier-2-Modulen (parallel mit Produktion, Material, Struktur) und beeinflussen direkt:

- **Ergonomie-Modul:** Steuerkraefte, Radposition, Sichtlinien
- **Compliance-Modul:** ISO 8847/10592, CE-Kategorie-Anforderungen
- **Strukturmodul:** Ruderlager, Koker-Abdichtung, Quadrantenaufnahme
- **Kosten-Modul:** Steueranlagen betragen typisch 3–8 % der Gesamtkosten Decksausruestung
- **Sicherheitsmodul:** Notsteuerung, Redundanz, Versagensmodi

### 1.2 Historische Entwicklung

**Vor 1900 — Pinne und Kolderstock:**
- Direkte Pinnensteuerung auf allen Segelfahrzeugen unter ca. 15 m
- Kolderstock (vertikale Hebelverlaengerung) fuer groessere Schiffe
- Steuerraeder mit Seil- oder Kettentrieb auf Grossseglern
- Steuermannsstand achtern, oft ungeschuetzt

**1900–1950 — Fruehe mechanische Systeme:**
- Schneckentrieb-Steuerungen auf Motoryachten
- Erste Wurmgetriebe-Rudermaschinen fuer groessere Yachten
- Bowdenzug-Steuerungen fuer kleine Motorboote
- Edson Corporation (USA, gegr. 1859) als aeltester bestehender Hersteller

**1950–1970 — Draht- und Kettensteuerung wird Standard:**
- Draht-Kettensteuerung (Wire-over-Sheave) dominiert den Segelboot-Markt
- Teleflex (heute SeaStar Solutions) entwickelt Push-Pull-Kabelsteuerung fuer Motorboote
- Hydraulische Systeme fuer Yachten ab ca. 15 m
- Whitlock (UK, gegr. 1970er) und Jefa (DK, gegr. 1981) spezialisieren sich auf Segelyacht-Steuerungen

**1970–1990 — Hydraulik und Autopilot-Integration:**
- Hydraulische Steuerungen werden Standard ab 40 Fuss (12 m)
- Autopilot-Integration erfordert elektrohydraulische Schnittstellen
- Lewmar expandiert in den Steueranlagen-Markt
- Kobelt (Kanada) etabliert sich im Motorboot-/Superyacht-Segment
- Edson perfektioniert die Pedestal-Steuerung (Steuerstandsaeule)

**1990–2010 — Praezision und Ergonomie:**
- Jefa Ruderlager mit kugelgelagerten Systemen erhoehen Praezision
- Whitlock Cobra/Mamba-Serie: kompakte Untersetzungsgetriebe
- Lecomble & Schmitt (Frankreich) fuehrt proportionale Hydrauliksteuerungen ein
- Elektromechanische Steuerungen fuer Kleinboote
- CAN-Bus-Integration bei Superyachten

**2010–heute — Digitalisierung und Fly-by-Wire:**
- ZF Marine und Humphree: Fly-by-Wire-Steuerungen fuer Motoryachten
- Jefa mit komplett ueberarbeitetem Ruderlager-Programm
- Steer-by-Wire-Systeme im Superyacht-Segment
- Integration in Multi-Funktionsdisplays (Garmin, Simrad, Raymarine)
- Zunehmende Autopilot-Integration als primaerer Steuerungsmodus
- Joystick-Steuerung fuer Manoevrieren im Hafen (IPS, Zeus, Axius)

### 1.3 Systemueberblick

Eine vollstaendige Steueranlage besteht aus folgenden Hauptkomponenten:

```
Steuerrad/Pinne (Bedienungselement)
  |
  v
Steuerstandsaeule / Pedestal (ggf.)
  |
  v
Primaeres Uebertragungselement:
  - Seil/Kette (Drahtsteuerung)
  - Hydraulikleitung (Hydrauliksteuerung)
  - Push-Pull-Kabel (Kabelsteuerung)
  - Zahnstange (Zahnstangensteuerung)
  - Elektrisches Signal (Fly-by-Wire)
  |
  v
Umlenkungen / Fuehrungen:
  - Umlenkrollen (Sheaves)
  - Kettenraeder (Sprockets)
  - Hydraulikventile
  |
  v
Ruderschaft-Anbindung:
  - Quadrant (Seilsteuerung)
  - Ruderhebel / Tiller-Arm (diverse)
  - Hydraulikzylinder
  - Linearer Aktuator
  |
  v
Ruderschaft mit Lagern:
  - Oberes Lager (im Koker)
  - Unteres Lager (Skeg/Ruderblatt)
  |
  v
Ruderblatt
```

### 1.4 Marktueberblick und wirtschaftliche Bedeutung

Der weltweite Markt fuer Yacht-Steueranlagen wird auf ca. 120–160 Mio. USD geschaetzt (2025), mit einer jaehrlichen Wachstumsrate von 2–4 %.

**Marktsegmente:**

| Segment | Anteil | Primaerer Steuerungstyp |
|---------|--------|------------------------|
| Segelyachten < 12 m | 35 % | Seil-/Kettensteuerung, Pinne |
| Segelyachten 12–20 m | 20 % | Seil-/Kettensteuerung, Hydraulik |
| Segelyachten > 20 m | 10 % | Hydraulik, Fly-by-Wire |
| Motorboote < 10 m | 15 % | Kabelsteuerung (Push-Pull) |
| Motorboote 10–20 m | 12 % | Hydraulik |
| Motoryachten > 20 m | 8 % | Hydraulik, Fly-by-Wire |

**Wichtigste Hersteller nach Segment:**

| Hersteller | Herkunft | Staerke | Preissegment |
|------------|----------|---------|-------------|
| Jefa | Daenemark | Ruderlager, Segelyacht-Steuerungen | Mittel–Hoch |
| Whitlock (Lewmar) | UK | Seil-/Kettensteuerungen, Getriebe | Mittel |
| Lewmar | UK | Hydraulik, Komplettsysteme | Mittel–Hoch |
| Edson | USA | Steuerstaender, Radsteuerung | Mittel–Hoch |
| Kobelt | Kanada | Motorboot-Hydraulik, Controls | Hoch |
| Lecomble & Schmitt | Frankreich | Hydraulik, Autopilot-Integration | Mittel–Hoch |
| SeaStar Solutions | USA/CAN | Kabelsteuerung, Hydraulik Motorboote | Niedrig–Mittel |
| ZF Marine | Deutschland | Superyacht, Fly-by-Wire | Hoch |
| Hynautic (Teleflex) | USA | Hydraulik Motorboote | Mittel |

### 1.5 Bedeutung fuer AYDI-Analyse

Steueranlagen-Analyse im AYDI-System liefert Befunde in folgenden Kategorien:

- **Dimensionierung:** Ist die Steueranlage fuer das Boot korrekt ausgelegt? (Confidence: measured/estimated)
- **Zustand:** Verschleissbewertung mechanischer/hydraulischer Komponenten (Confidence: visual_high bis visual_insufficient)
- **Compliance:** Entspricht die Anlage den geltenden Normen? (Confidence: measured/documented)
- **Ergonomie:** Steuerkraefte, Radposition, Feedback-Qualitaet (Confidence: measured/visual_medium)
- **Redundanz:** Notsteuerung vorhanden und funktional? (Confidence: documented/visual_medium)
- **Wartungszustand:** Schmierung, Seilspannung, Hydraulikfluessigkeit (Confidence: visual_medium/documented)

---

## 2. Grundlagen und Theorie

### 2.1 Ruderkraft und Rudermoment

Das Verstaendnis der auf das Ruder wirkenden Kraefte ist die Grundlage jeder Steueranlagen-Dimensionierung.

#### 2.1.1 Hydrodynamische Ruderkraft

Die Gesamtkraft auf ein Ruderblatt ergibt sich aus der hydrodynamischen Druckverteilung:

```
F_ruder = 0.5 * rho * V^2 * A_ruder * C_N

Wobei:
  F_ruder  = Ruderkraft [N]
  rho      = Dichte des Wassers [kg/m^3] (Seewasser: 1025, Suesswasser: 1000)
  V        = Anstroemgeschwindigkeit [m/s]
  A_ruder  = Ruderblattflaeche [m^2]
  C_N      = Normalkraftbeiwert [-] (abhaengig von Ruderprofil und Anstellwinkel)
```

**Typische C_N-Werte bei verschiedenen Anstellwinkeln (NACA 0012/0015-Profil):**

| Anstellwinkel [Grad] | C_N (NACA 0012) | C_N (NACA 0015) | C_N (Flachprofil) |
|----------------------|-----------------|-----------------|-------------------|
| 5 | 0.35 | 0.38 | 0.30 |
| 10 | 0.70 | 0.75 | 0.55 |
| 15 | 1.00 | 1.05 | 0.75 |
| 20 | 1.20 | 1.25 | 0.88 |
| 25 | 1.30 | 1.35 | 0.95 |
| 30 | 1.25 | 1.30 | 0.98 |
| 35 (Stroemungsabriss) | 0.90 | 0.95 | 0.95 |

**Hinweis:** Stroemungsabriss (Stall) tritt bei Profilrudern typisch ab 25–35 Grad auf, bei Flachrudern spaeter. Nach dem Stall faellt die Ruderwirkung dramatisch ab.

#### 2.1.2 Ruderschaftmoment (Steering Torque)

Das fuer die Steueranlage dimensionierungsrelevante Moment am Ruderschaft:

```
M_schaft = F_ruder * (x_cp - x_schaft)

Wobei:
  M_schaft  = Ruderschaftmoment [Nm]
  F_ruder   = Ruderkraft [N]
  x_cp      = Abstand Anstroemkante bis Druckpunkt [m]
  x_schaft  = Abstand Anstroemkante bis Schaftachse [m]

Druckpunkt-Lage (typisch):
  x_cp / c_ruder = 0.24–0.28 (symmetrisches NACA-Profil, kleine Winkel)
  x_cp / c_ruder = 0.30–0.35 (grosse Anstellwinkel, nahe Stall)
  x_cp / c_ruder = 0.25     (Faustregel fuer Auslegung)

  c_ruder = Ruderblatt-Tiefe (Chord) [m]
```

**Balancegrad (Balance Ratio):**

Der Balancegrad definiert den Anteil der Ruderblattflaeche vor der Schaftachse:

```
B = A_vor / A_gesamt

Wobei:
  B       = Balancegrad [-]
  A_vor   = Ruderblattflaeche vor dem Schaft [m^2]
  A_gesamt = Gesamte Ruderblattflaeche [m^2]

Typische Balancegrade:
  Spatenruder ohne Skeg:    B = 0.15–0.20
  Spatenruder mit Skeg:     B = 0.10–0.15
  Halbbalanciertes Ruder:   B = 0.20–0.30
  Vollbalanciertes Ruder:   B = 0.35–0.50
  Pinne (Langkiel):         B = 0.05–0.10
```

**Wirkung des Balancegrads:** Ein hoeherer Balancegrad reduziert das erforderliche Steuermoment, verringert aber die Stabilitaet des Ruders (Tendenz zum Schlagen). Balancegrade ueber 0.25 erfordern in der Regel eine Steueranlage mit Daempfung.

#### 2.1.3 Berechnungsbeispiel: Rudermoment

**Beispiel: Bavaria 46 Cruiser**
```
Gegebene Daten:
  V       = 8 kn = 4.12 m/s
  A_ruder = 0.52 m^2
  c_ruder = 0.45 m
  x_schaft = 0.15 * c_ruder = 0.0675 m (Schaftachse bei 15% Tiefe)
  x_cp     = 0.25 * c_ruder = 0.1125 m (Druckpunkt bei 25% Tiefe)

Berechnung:
  F_ruder = 0.5 * 1025 * 4.12^2 * 0.52 * 1.05
           = 0.5 * 1025 * 16.97 * 0.52 * 1.05
           = 4741 N

  M_schaft = 4741 * (0.1125 - 0.0675)
           = 4741 * 0.045
           = 213 Nm

Sicherheitsfaktor (Boe, Wellengang): 1.5–2.0
  M_auslegung = 213 * 1.75 = 373 Nm
```

### 2.2 Helmbalance (Lee-/Luv-Gierigkeit)

#### 2.2.1 Physikalische Grundlage

Die Helmbalance beschreibt die Tendenz eines Segelboots, ohne Rudereingriff in eine bestimmte Richtung zu drehen:

- **Luvgierigkeit (Weather Helm):** Boot dreht zum Wind hin — Druckpunkt (CE) des Segelplans liegt hinter dem Lateralpunkt (CLR) des Unterwasserschiffs. Leichter Ruderdruck nach Lee erforderlich. **Erstrebenswert:** 3–5 Grad Ruderwinkel bei Normalfahrt.

- **Leegierigkeit (Lee Helm):** Boot dreht vom Wind weg — Druckpunkt liegt vor dem Lateralpunkt. Ruderdruck nach Luv erforderlich. **Unerwuenscht und gefaehrlich:** Bei Boe kein selbstaendiges Anluven.

- **Neutrales Ruder:** Kein permanenter Ruderdruck. In der Praxis nahezu nie erreichbar und auch nicht erstrebenswert, da eine leichte Luvgierigkeit als Sicherheitsmechanismus gilt.

```
Lead = CE - CLR [m]

Wobei:
  Lead  = Abstand zwischen Segeldruck- und Lateralpunkt [m]
  CE    = Centre of Effort (Schwerpunkt der Segelflaechenprojektion)
  CLR   = Centre of Lateral Resistance (Lateralpunkt)

Empfohlene Lead-Werte:
  Langkiel-Segelyacht:     10–15 % der Wasserlinienlaenge (LWL)
  Kurzkiel-Segelyacht:     8–12 % der LWL
  Fin-Kiel mit Spatenruder: 5–10 % der LWL
  Mehrrumpfboot:            3–7 % der LWL
```

#### 2.2.2 Einflussfaktoren auf die Helmbalance

| Faktor | Wirkung auf Helmbalance |
|--------|------------------------|
| Kraengung | Zunehmende Luvgierigkeit bei mehr Lage |
| Genuagroesse | Groessere Genua verschiebt CE nach vorne -> weniger Luvgierigkeit |
| Grosssegeltrimm | Offeneres Achterlik -> weniger Luvgierigkeit |
| Mastfall | Mehr Mastfall nach achtern -> mehr Luvgierigkeit |
| Trimmgewicht | Hecklastig -> mehr Luvgierigkeit |
| Seegang | Unregulierter Wechsel -> erhoehte Steuerkraefte |
| Geschwindigkeit | Hoehere Geschwindigkeit -> ueberproportional mehr Ruderkraft |

#### 2.2.3 Auswirkung auf die Steueranlage

Die Helmbalance bestimmt die Dauer-Steuerlast:

```
Dauerbelastung:
  Luvgierigkeit 3-5 Grad -> Dauer-Rudermoment ca. 10-20% des Maximalmoments
  Luvgierigkeit >8 Grad  -> Dauer-Rudermoment ca. 30-50% des Maximalmoments
                             -> Erhoehter Verschleiss an Seilen, Lagern, Hydraulik
                             -> Autopilot wird ueberlastet

AYDI-Bewertung:
  Luvgierigkeit 2-5 Grad:  "Ideal" (Score 90-100)
  Luvgierigkeit 5-8 Grad:  "Akzeptabel" (Score 60-80)
  Luvgierigkeit >8 Grad:   "Problematisch" (Score 20-50)
  Leegierigkeit jegliche:  "Kritisch" (Score 0-20)
```

### 2.3 Steuerungsverhaeltnis und mechanischer Vorteil

#### 2.3.1 Steuerungsverhaeltnis (Steering Ratio)

Das Steuerungsverhaeltnis gibt an, wie viele Radumdrehungen fuer den vollen Ruderausschlag erforderlich sind:

```
Steering_Ratio = Umdrehungen_Rad / Ruderausschlag_gesamt [Umdrehungen/Grad]

Typische Werte:
  Segelyacht < 10 m, Seilsteuerung:    2.5–3.5 Umdrehungen fuer 70 Grad
  Segelyacht 10–15 m, Seilsteuerung:   3.0–4.5 Umdrehungen fuer 70 Grad
  Segelyacht > 15 m, Hydraulik:        3.5–5.0 Umdrehungen fuer 70 Grad
  Motorboot < 10 m, Kabel:             3.0–4.0 Umdrehungen (Anschlag zu Anschlag)
  Motoryacht > 15 m, Hydraulik:        4.0–6.0 Umdrehungen (Anschlag zu Anschlag)
```

**Wichtig:** Ein niedrigeres Steuerungsverhaeltnis bedeutet schnellere Reaktion, aber hoehere Steuerkraefte. Rennboote bevorzugen direktere Steuerung (2.0–3.0), Fahrtenyachten indirekteren (3.5–5.0).

#### 2.3.2 Mechanischer Vorteil (Mechanical Advantage)

```
MA_gesamt = MA_rad * MA_getriebe * MA_quadrant

Wobei:
  MA_rad      = Radius Steuerrad / Radius Steuerradnabe (Kette/Seil)
               = R_rad / R_kettenrad
  MA_getriebe = Untersetzung im Pedestal-Getriebe (falls vorhanden)
  MA_quadrant = Radius des Quadranten am Ruderschaft [m]

Beispiel Whitlock Mamba Getriebe:
  MA_getriebe = 3.5:1
  R_rad       = 0.45 m (900 mm Rad)
  R_kettenrad = 0.035 m (70 mm Kettenrad)
  -> MA_rad   = 0.45 / 0.035 = 12.86
  -> MA_gesamt = 12.86 * 3.5 * R_quadrant

Fuer R_quadrant = 0.15 m (300 mm Quadrant):
  MA_gesamt    = 12.86 * 3.5 * (1/0.15)  [... vereinfacht]

Ergaenzende Berechnung der Steuerkraft:
  F_hand = M_schaft / (MA_rad * MA_getriebe * R_quadrant)
  F_hand = 373 Nm / (12.86 * 3.5 * 0.15)
  F_hand = 373 / 6.75
  F_hand = 55.3 N (ca. 5.6 kgf)
```

**Ergonomische Grenzwerte fuer Steuerkraefte (ISO 8847):**

| Betriebszustand | Max. Steuerkraft am Rad |
|----------------|------------------------|
| Normalfahrt (Dauer) | ≤ 25 N (2.5 kgf) |
| Boeen / Manoevrieren | ≤ 80 N (8 kgf) |
| Maximum (Not) | ≤ 150 N (15 kgf) |
| Pinnensteuerung Dauer | ≤ 30 N |
| Pinnensteuerung Max | ≤ 100 N |

### 2.4 Hydraulische Grundlagen

#### 2.4.1 Hydraulisches Prinzip (Pascal)

```
Druck p = F_pumpe / A_pumpe = F_zylinder / A_zylinder

F_zylinder = F_pumpe * (A_zylinder / A_pumpe)

Wobei:
  p            = Systemdruck [bar, Pa]
  F_pumpe      = Pumpenkraft (aus Raddrehen) [N]
  A_pumpe      = Kolbenflaeche Pumpe [cm^2]
  F_zylinder   = Zylinderkraft am Ruderhebel [N]
  A_zylinder   = Kolbenflaeche Zylinder [cm^2]
```

**Typische Systemdruecke:**

| Anwendung | Systemdruck | Bemerkung |
|-----------|------------|-----------|
| Kleinboot-Hydraulik | 20–40 bar | Hynautic/SeaStar Helm |
| Segelyacht 30–50 ft | 40–80 bar | Lecomble & Schmitt, Jefa |
| Motoryacht 40–60 ft | 60–120 bar | Kobelt, Lewmar |
| Superyacht | 80–200 bar | ZF Marine, professionell |

#### 2.4.2 Hydraulikfluid

**Spezifikationen:**

| Eigenschaft | Anforderung | Typisches Produkt |
|-------------|-------------|-------------------|
| Typ | Mineraloelbasiert oder synthetisch | Seastar/Teleflex Fluid, Total Fluide LDS |
| Viskositaet | ISO VG 15–32 bei 40 Grad C | — |
| Frostschutz | Bis -30 Grad C | — |
| Dichtungsvertraeglichkeit | NBR, FKM (Viton) | — |
| Mischbarkeit | Nur gleicher Typ/Hersteller | NIEMALS verschiedene mischen |
| Wechselintervall | Alle 2–3 Jahre oder 500 Betriebsstunden | — |

**Warnung:** Das Mischen verschiedener Hydraulikfluids kann zu Dichtungsquellung, Viskositaetsaenderung und Systemversagen fuehren. AYDI-Befund-Schwere: CRITICAL.

#### 2.4.3 Hydraulikzylinder-Typen

**Einfachwirkend (Single-Acting):**
- Kolben wird in eine Richtung hydraulisch bewegt
- Rueckstellung durch Feder oder Ruderdruck
- Einfacher, guenstiger, aber ungleichmaessiges Steuergefuehl
- Verwendung: Autopilot-Antriebe, Beiboot

**Doppeltwirkend (Double-Acting):**
- Hydraulikdruck in beide Richtungen
- Gleichmaessiges Steuergefuehl in beide Richtungen
- Standard fuer alle Yacht-Hauptsteuerungen
- Ausfuehrung: Linear-Zylinder oder Drehkolben (Rotary Vane)

**Drehkolben (Rotary Vane Actuator):**
- Direkte Drehbewegung ohne Umlenkung
- Kompakte Bauform, weniger mechanische Verschleisskomponenten
- Verwendung: Lecomble & Schmitt, Jefa Direct Drive

### 2.5 Feedback-Systeme

#### 2.5.1 Mechanisches Feedback

Bei Seil-/Kettensteuerungen ist das Feedback intrinsisch: Die starre mechanische Verbindung uebertragaet Ruderkraefte direkt an das Steuerrad. Der Steuermann spuert jede Veraenderung der Ruderlast unmittelbar.

**Vorteile:** Natuerliches, proportionales Gefuehl, keine zusaetzlichen Komponenten
**Nachteile:** Friction (Reibung) in Umlenkungen daempft Feedback, Drahtdehnung bei langen Wegen

#### 2.5.2 Hydraulisches Feedback

Hydraulische Systeme koennen mit oder ohne Feedback-Mechanismus ausgefuehrt werden:

**Ohne Feedback (Non-Follow-Up, NFU):**
- Fester Pumpenhub pro Radumdrehung
- Kein Rueckmeldung der Ruderlast ans Rad
- Einfacher, aber unkomfortabel
- Verwendung: Einfache Motorboot-Steuerungen, Autopilot-Betrieb

**Mit Feedback (Follow-Up, FU):**
- Helm-Pumpe mit integriertem Bypass/Feedback-Ventil
- Proportionale Rueckmeldung der Ruderlast
- Ruderfeedback ueber Systemdruck spuerbar
- Standard fuer Segelyacht-Hydraulik

**Aktives Feedback:**
- Elektronisch gesteuerter Widerstand am Steuerrad
- Programmierbare Feedback-Kurve (Fly-by-Wire-Systeme)
- Simulation des Rudergefuehls bei Joystick-Steuerung
- Verwendung: Superyachten, Hightech-Motorboote

#### 2.5.3 Feedback-Bewertung im AYDI-System

```
Feedback-Qualitaets-Score (0–100):

  Mechanisch, gut gewartet:          85–100
  Mechanisch, Reibung erhoeht:       60–80
  Hydraulisch mit FU, gut:           75–95
  Hydraulisch mit FU, Luft im System: 40–60
  Hydraulisch NFU:                    20–40
  Fly-by-Wire, kalibriert:          80–95
  Fly-by-Wire, unkalibriert:        30–50
```

### 2.6 Reibung und Effizienz

Die Gesamteffizienz einer Steueranlage bestimmt, wie viel der eingebrachten Steuerkraft tatsaechlich am Ruder ankommt:

```
eta_gesamt = eta_lager * eta_uebertragung * eta_umlenkung^n

Wobei:
  eta_lager         = Wirkungsgrad Ruderlager (0.90–0.98)
  eta_uebertragung  = Wirkungsgrad Uebertragungsmechanismus
                      Seil/Kette: 0.88–0.95
                      Hydraulik:  0.80–0.92
                      Zahnstange: 0.90–0.95
  eta_umlenkung     = Wirkungsgrad pro Umlenkrolle (0.95–0.98)
  n                 = Anzahl der Umlenkrollen

Beispiel Seilsteuerung mit 4 Umlenkrollen:
  eta_gesamt = 0.95 * 0.92 * 0.97^4
           = 0.95 * 0.92 * 0.885
           = 0.773 (77.3% Wirkungsgrad)

-> Bedeutet: 22.7% der Steuerkraft gehen durch Reibung verloren
-> Bedeutet auch: 22.7% weniger Ruderfeedback am Steuerrad
```

**Reibungsquellen und Abhilfe:**

| Quelle | Typischer Verlust | Abhilfe |
|--------|------------------|---------|
| Umlenkrollen, trocken | 3–8 % pro Rolle | Kugelgelagerte Rollen, Schmierung |
| Umlenkrollen, kugelgelagert | 1–3 % pro Rolle | Regelmaeassige Wartung |
| Kabel in Fuehrungsrohr | 5–15 % gesamt | Korrekte Biegeradien, Schmierung |
| Ruderlager, Gleitlager | 5–12 % | Austausch gegen Kugellager |
| Ruderlager, Kugellager | 2–5 % | Jefa-Kugellager |
| Koker-Dichtung | 2–8 % | Korrekte Vorspannung, PTFE-Lippen |
| Hydraulikreibung | 8–20 % | Korrekte Leitungsdimensionierung |

### 2.7 Ruderblatt-Typen und deren Einfluss auf die Steuerung

| Rudertyp | Steuerkraft | Feedback | Sicherheit | Verbreitung |
|----------|------------|----------|------------|-------------|
| Langkiel-Ruder (angehaengt) | Gering | Sehr gut | Hoch (geschuetzt) | Traditionsyachten |
| Skeg-Ruder (halbbalanciert) | Mittel | Gut | Hoch (Skeg-gestuetzt) | Fahrtenyachten |
| Spatenruder (freihaengend) | Hoch | Gut | Mittel (exponiert) | Moderne Cruiser/Racer |
| Doppelruder (Twin Rudder) | Hoch (pro Ruder geringer) | Gut | Hoch (Redundanz) | Performance Cruiser |
| Transom-Ruder (aufgesetzt) | Gering | Sehr gut | Mittel | Kleinboote, Folkboote |

### 2.8 Dynamische Ruderkraefte und Extrembelastungen

#### 2.8.1 Seegangseinfluss

Im Seegang wirken zusaetzliche dynamische Kraefte auf das Ruder, die ueber die stationaere Ruderkraft hinausgehen:

```
F_dynamisch = F_stationaer * k_seegang

Wobei k_seegang:
  Glatte See (CE Kat D):       k = 1.0
  Leichter Seegang (CE Kat C): k = 1.25
  Mittlerer Seegang (CE Kat B): k = 1.5
  Schwerer Seegang (CE Kat A):  k = 2.0
  Extremer Seegang (Notfall):   k = 2.5–3.0
```

#### 2.8.2 Schockbelastungen

Besondere Belastungsfaelle, die in der Dimensionierung beruecksichtigt werden muessen:

| Belastungsfall | Faktor | Beschreibung |
|---------------|--------|-------------|
| Grundberuehrung | 3–5× | Ruder trifft Hindernis bei Fahrt |
| Treibgut | 2–4× | Ruder wird von Treibgut getroffen |
| Rueckwaertsfahrt Hart | 2× | Voller Ruderausschlag bei Rueckwaertsfahrt |
| Surfendes Boot | 2–3× | Hohe Geschwindigkeit auf der Welle |
| Ruderschlagen (Hydraulik-Ausfall) | 3× | Ruder schlaegt frei hin und her |

#### 2.8.3 Ermuedung und Dauerfestigkeit

Die Steueranlage muss nicht nur Spitzenlasten aushalten, sondern auch Dauerbetrieb:

```
Typische Lastkollektive (Steuerseil):
  70% der Zeit:  0-20% der Max.-Last (Normalfahrt)
  20% der Zeit: 20-50% der Max.-Last (aktives Steuern)
   8% der Zeit: 50-80% der Max.-Last (Boeen, Manoevrieren)
   2% der Zeit: 80-100% der Max.-Last (Extremsituationen)

Lebensdauer-Berechnung:
  Seilsteuerung: Min. 100.000 Vollausschlaege (ISO 8847)
  Hydraulik:     Min. 200.000 Vollausschlaege (ISO 10592)
  Ruderlager:    Min. 500.000 Drehzyklen
```

### 2.9 Temperatureinfluss auf Steueranlagen

| Komponente | Temperaturbereich | Kritisch bei |
|-----------|-------------------|-------------|
| Steuerseile (Edelstahl) | -40 bis +200 Grad C | Unkritisch |
| Umlenkrollen (Delrin) | -30 bis +80 Grad C | > 60 Grad C: Erweichung |
| Hydraulikfluid | -30 bis +80 Grad C | < -20 Grad C: zu viskos |
| Hydraulikdichtungen (NBR) | -25 bis +100 Grad C | > 80 Grad C: Alterung |
| Hydraulikdichtungen (FKM) | -20 bis +200 Grad C | Besser als NBR |
| Nylon-Leitungen | -20 bis +60 Grad C | > 50 Grad C: Erweichung |
| Kupfer-Leitungen | -40 bis +200 Grad C | Unkritisch |

**AYDI-Pruefpunkt:** Hydraulikleitungen durch Maschinenraum: Temperaturbelastung beachten. Nylon-Leitungen im Maschinenraum = Score-Malus -20.

### 2.10 Korrosionsschutz-Systematik

| Material | Korrosionsrisiko Seewasser | Schutzmassnahme | Lebensdauer |
|----------|--------------------------|----------------|-------------|
| Edelstahl 316L | Gering (Spaltkorrosion!) | Opferanoden, galvanische Trennung | 25–40 Jahre |
| Edelstahl 304 | Mittel-Hoch | NICHT empfohlen fuer Seewasser | 5–15 Jahre |
| Bronze (Rotguss) | Gering | Keine Massnahme noetig | 30–50 Jahre |
| Aluminium (6061-T6) | Mittel | Eloxierung, Opferanoden | 15–25 Jahre |
| Kupfer (Leitungen) | Gering | Keine Massnahme noetig | 20–30 Jahre |
| Stahl (verzinkt) | Hoch | NICHT fuer Seewasser | 3–8 Jahre |
| Delrin/PTFE | Keine Korrosion | — | 10–20 Jahre |
| Carbon (CFK) | Keine Korrosion | Galvanische Trennung zu Metall! | 20+ Jahre |

**Galvanische Spannungsreihe (Auszug, relevant fuer Steueranlagen):**

```
Edler (kathodisch):
  Titan              +0.06 V
  Edelstahl 316L (passiv) -0.05 V
  Bronze              -0.31 V
  Kupfer               -0.36 V
  Edelstahl 304 (aktiv) -0.46 V
  Aluminium 6061       -0.64 V
  Zink (Opferanode)    -1.03 V
Unedler (anodisch)

Regel: Materialien mit > 0.25 V Differenz galvanisch trennen oder Opferanoden verwenden.
```

---

## 3. Typenuebersicht

### 3.1 Pinnensteuerung (Tiller Steering)

#### 3.1.1 Beschreibung und Prinzip

Die Pinne (engl. tiller) ist die einfachste und direkteste Steuerung: ein Hebel, der am Ruderkopf befestigt ist und direkt den Ruderschaft dreht. Keine Zwischenelemente, keine Kraftverstaerkung.

**Kraftberechnung:**
```
F_hand = M_schaft / L_pinne

Wobei:
  F_hand   = Handkraft [N]
  M_schaft = Ruderschaftmoment [Nm]
  L_pinne  = Wirksame Pinnenlaenge [m]

Beispiel: M_schaft = 120 Nm, L_pinne = 1.0 m
  F_hand = 120 / 1.0 = 120 N (12.2 kgf)
```

#### 3.1.2 Pinnen-Typen

| Typ | Material | Laenge | Boot-Laenge | Preisniveau |
|-----|----------|--------|-------------|-------------|
| Holzpinne, gerade | Teak, Esche, Iroko | 0.6–1.2 m | 5–10 m | 80–300 EUR |
| Holzpinne, geschwungen | Teak, laminiert | 0.8–1.5 m | 8–12 m | 200–600 EUR |
| Aluminium-Pinne | 6061-T6, eloxiert | 0.6–1.5 m | 5–14 m | 150–500 EUR |
| Carbon-Pinne | CFK-Rohr | 0.8–1.8 m | 8–15 m | 400–1500 EUR |
| Klapp-Pinne (Faltpinne) | Alu + Edelstahl | 0.5–1.2 m | 6–10 m | 200–600 EUR |
| Pinnenverlaengerung (Hiker) | Alu, Carbon | 0.6–1.2 m | 3–8 m | 50–350 EUR |

#### 3.1.3 Pinnen-Armaturen

- **Ruderkopf-Anschluss:** Konus (Taper) oder Klemme (Clamp). Konus nach ISO-Kegelpassung, Klemme fuer Nachruestung.
- **Universalgelenk:** Bei Pinnenverlaengerung erforderlich. Kugelkopf oder Kardangelenk.
- **Pinnen-Pilot-Adapter:** Aufsatz zur Montage von Pinnenpiloten (Autopilot). Rohr- oder Klemmbefestigung.
- **Notpinne:** Auf Radsteuerungs-Yachten als Notsystem am Ruderschaft. Quadratprofil oder Sechskant-Aufnahme.

#### 3.1.4 Vor- und Nachteile

**Vorteile:**
- Direktestes Rudergefuehl aller Steuerungsarten
- Geringster mechanischer Aufwand, wenige Verschleissteile
- Niedrigste Kosten
- Leichtestes Gewicht
- Einfachste Wartung
- Zuverlaessigste Steuerungsart (wenige Fehlermodi)

**Nachteile:**
- Begrenzte Bootgroesse (praktisch bis ca. 12 m, Ruderkraft wird zu hoch)
- Steuermann muss achtern sitzen (Sichteinschraenkung)
- Ermuedendes Steuern bei starkem Wind
- Einschraenkung des Cockpits (Pinne schwenkt)
- Pinnen-Autopilot weniger leistungsfaehig als Radsteuerungs-Autopilot

#### 3.1.5 AYDI-Bewertungskriterien fuer Pinnensteuerung

| Kriterium | Score 90–100 | Score 50–70 | Score 0–30 |
|-----------|-------------|-------------|------------|
| Steuerkraft Normalfahrt | < 20 N | 20–60 N | > 60 N |
| Pinnenlaenge vs. Cockpit | Passt ohne Einschraenkung | Leicht eingeschraenkt | Blockiert Cockpit |
| Ruderfeedback | Direkt, proportional | Leicht ruckelig | Schwergaengig |
| Notpinne (wenn Rad) | Vorhanden, zugaenglich | Vorhanden, schwer zugaenglich | Nicht vorhanden |

### 3.2 Radsteuerung — Seil-/Kettensteuerung (Cable/Chain Steering)

#### 3.2.1 Prinzip

Die Seil-/Kettensteuerung (engl. cable-and-chain steering, wire-over-sheave) ist der am weitesten verbreitete Steuerungstyp fuer Segelyachten von 8–18 m. Ein Steuerrad dreht ueber eine Kette oder ein Seil ein Kettenrad im Pedestal, das ueber Drahtseile und Umlenkrollen einen Quadranten am Ruderschaft bewegt.

**Aufbau:**
```
Steuerrad
  |
Radwelle im Pedestal
  |
Kettenrad (Sprocket) oder Trommel
  |
Kette (ca. 30–50 cm) -> Uebergang auf Drahtseil (3–7 mm)
  |
Umlenkrollen (2–6 Stueck, je nach Routing)
  |
Quadrant (200–450 mm Radius) am Ruderschaft
```

#### 3.2.2 Komponenten im Detail

**Steuerrad:**

| Durchmesser | Bootgroesse | Grifftyp | Material |
|-------------|------------|----------|----------|
| 600–700 mm | 7–9 m | Glatt oder Knob | Edelstahl/Teak |
| 800–900 mm | 9–12 m | Teak-Griffe | Edelstahl 316L/Teak |
| 1000–1100 mm | 12–15 m | Teak-Griffe, Leder | Edelstahl/Carbon |
| 1200–1400 mm | 15–20 m | Leder, Carbon | Carbon/Edelstahl |

**Pedestal (Steuerstandsaeule):**
- Edelstahl 316L, gegossen oder geschweisst
- Innenleben: Kettenrad, Lager, ggf. Getriebe (Whitlock-Typ)
- Zusaetzliche Funktionen: Kompassaufnahme, Instrumentenhalter, Bremse
- Hersteller: Edson, Lewmar, Jefa

**Drahtseil:**

| Durchmesser | Max. Bruchlast | Einsatz |
|-------------|---------------|---------|
| 3 mm (1×19) | 620 kg | Boote bis 8 m |
| 4 mm (1×19) | 1080 kg | Boote 8–11 m |
| 5 mm (1×19) | 1680 kg | Boote 11–14 m |
| 6 mm (1×19) | 2400 kg | Boote 14–18 m |
| 7 mm (1×19) | 3200 kg | Boote 18–22 m |

**Material:** 1×19 Edelstahl AISI 316, alternativ 7×19 fuer hoehere Flexibilitaet bei engeren Umlenkradien.

**Quadrant:**

| Radius | Ruderschaft-Dm | Bootgroesse | Material |
|--------|---------------|-------------|----------|
| 200 mm | 25–30 mm | 7–9 m | Aluminium/Delrin |
| 250 mm | 30–35 mm | 9–11 m | Aluminium |
| 300 mm | 35–45 mm | 11–14 m | Aluminium/Bronze |
| 350 mm | 40–50 mm | 14–17 m | Bronze/Edelstahl |
| 400 mm | 50–60 mm | 17–20 m | Bronze |
| 450 mm | 55–70 mm | 20–24 m | Bronze/Edelstahl |

**Alternativen zum Quadrant:**
- **Radial-Antrieb (Radial Drive):** Hebelarm mit Seilbefestigung, kompakter als Quadrant, oft bei Nachruestung
- **Tiller-Arm:** Einzelhebel mit Seilanschluss, einfachster Ansatz

#### 3.2.3 Umlenkrollen (Sheaves/Turning Blocks)

| Rollendurchmesser | Min. Seil-Dm | Lagertyp | Lebensdauer |
|-------------------|-------------|----------|-------------|
| 50–65 mm | 3–4 mm | Gleitlager (Delrin) | 3000–5000 h |
| 65–80 mm | 4–5 mm | Kugelgelagert | 8000–12000 h |
| 80–100 mm | 5–6 mm | Kugelgelagert | 10000–15000 h |
| 100–130 mm | 6–7 mm | Kugelgelagert, gedichtet | 12000–20000 h |

**Montageregeln:**
- Mindestwinkel: 5 Grad Ablenkung pro Rolle (sonst rutscht Seil ab)
- Maximaler Ablenkwinkel: 170 Grad (Seil darf nicht zuruecklaufen)
- Rollen muessen in einer Ebene mit dem Seilzug stehen
- Abstand Rolle zu Quadrant: mindestens 4× Quadrantenradius

#### 3.2.4 Seilspannung und Wartung

**Korrekte Seilspannung:** Wenn das Seil in der Mitte des laengsten freien Stuecks mit Daumendruck (ca. 5 kg) gedrueckt wird, sollte die Auslenkung 10–15 mm betragen.

**Wartungsintervalle:**

| Massnahme | Intervall |
|-----------|----------|
| Seilspannung pruefen | Alle 3 Monate |
| Umlenkrollen schmieren | Alle 6 Monate |
| Kette schmieren (Kettenfett) | Alle 6 Monate |
| Seil auf Kinkung/Bruch pruefen | Alle 6 Monate |
| Quadrant-Klemmung pruefen | Jaehrlich |
| Pedestal-Lager pruefen/fetten | Jaehrlich |
| Seil komplett erneuern | Alle 5–7 Jahre oder bei erstem Bruch |

### 3.3 Radsteuerung — Zahnstangensteuerung (Rack-and-Pinion Steering)

#### 3.3.1 Prinzip

Ein Ritzel (Zahnrad) am Steuerrad treibt eine Zahnstange, die ueber Verbindungsstangen den Ruderschaft dreht. Kompaktes, spielfreies System.

**Aufbau:**
```
Steuerrad
  |
Ritzel (Zahnrad)
  |
Zahnstange (linear beweglich)
  |
Verbindungsstange (Drag Link)
  |
Hebel am Ruderschaft (Tiller Arm)
```

#### 3.3.2 Einsatzbereich

| Parameter | Wert |
|-----------|------|
| Bootlaenge | 5–12 m (Motorboote), 6–10 m (Segelboote) |
| Max. Rudermoment | Ca. 250 Nm |
| Uebersetzung | Fest, abhaengig von Ritzel/Zahnstangenkombination |
| Radmittendrehungen | Typisch 1.5–3.0 (Anschlag zu Anschlag) |

#### 3.3.3 Vor- und Nachteile

**Vorteile:**
- Spielfrei (kein Seil, das sich dehnt)
- Kompakt, wenig Platzbedarf
- Direktes Steuergefuehl
- Wenig Wartung

**Nachteile:**
- Begrenzte Reichweite (Abstand Steuerrad zu Ruder)
- Nicht fuer grosse Boote geeignet
- Korrosion der Zahnstange in feuchter Umgebung
- Begrenzte Ruderwinkel

### 3.4 Radsteuerung — Hydrauliksteuerung (Hydraulic Steering)

#### 3.4.1 Prinzip

Eine handbetriebene Hydraulikpumpe (Helm Pump) am Steuerrad erzeugt Druck, der ueber Leitungen einen Hydraulikzylinder oder Drehkolben am Ruderschaft antreibt.

**Aufbau:**
```
Steuerrad
  |
Helm-Pumpe (Verdraengerpumpe im Pedestal oder Konsole)
  |
Hydraulikleitungen (Kupfer, Nylon oder Edelstahl)
  |
Hydraulikzylinder oder Drehkolben am Ruderschaft
  |
Ruderhebel / Tiller-Arm
  |
Ruderschaft
```

#### 3.4.2 Helm-Pumpen-Typen

**Konstantpumpe (Fixed Displacement):**
- Fester Foerderhub pro Radumdrehung
- Einfach, robust, kostenguenstig
- Steuerungsverhaeltnis nicht einstellbar
- Hersteller: SeaStar/Teleflex, Hynautic

**Proportionalpumpe (Variable Displacement):**
- Stufenlos einstellbare Foerdermenge
- Einstellbares Steuerungsverhaeltnis
- Besseres Steuergefuehl
- Hersteller: Lecomble & Schmitt, Jefa, Kobelt

#### 3.4.3 Zylinder-Typen und Zuordnung

| Zylinder-Typ | Hub | Kraftbereich | Einsatz |
|--------------|-----|-------------|---------|
| Compact Cylinder | 100–200 mm | 500–3000 N | Boote 8–12 m |
| Standard Cylinder | 150–300 mm | 2000–8000 N | Boote 12–18 m |
| Heavy Duty Cylinder | 200–450 mm | 5000–20000 N | Boote 18–25 m |
| Rotary Vane Actuator | n/a (Drehwinkel) | 200–2000 Nm | Boote 10–25 m |
| Ram Type Cylinder | 300–600 mm | 10000–50000 N | Boote > 25 m |

#### 3.4.4 Leitungsmaterial

| Material | Innendurchmesser | Max. Druck | Einsatz |
|----------|-----------------|-----------|---------|
| Nylon (SeaFlex) | 4–6 mm | 50 bar | Kleinboote, kurze Wege |
| Kupfer (geglueht) | 6–10 mm | 100 bar | Standard Yacht, mittlere Wege |
| Edelstahl 316L | 6–12 mm | 200 bar | Langlebig, Superyacht |
| Hydraulikschlauch | 6–16 mm | 200+ bar | Flexible Abschnitte, Motoryacht |

**Verlegeregeln:**
- Kupfer: Min. Biegeradius = 6× Aussendurchmesser
- Kupfer: Vibrationsentkopplung durch flexible Stuecke an Motor/Ruder
- Nylon: Nicht in Maschinenraum (Temperatur), nicht in UV-Exposition
- Alle: Entlueftungsventil am hoechsten Punkt installieren

#### 3.4.5 Doppelsteuerstand-Hydraulik

Bei zwei Steuerpositionen (z.B. Cockpit + Flybridge) werden zwei Helm-Pumpen parallel geschaltet:

```
Helm-Pumpe 1 (Cockpit)  ----+---- Hydraulikzylinder
                              |
Helm-Pumpe 2 (Flybridge) ---+

Wichtig: 
  - Lock-Ventil am inaktiven Stand
  - Oder Bypass-Ventil fuer freies Mitdrehen
  - Jefa/Lewmar bieten integrierte Loesungen
```

### 3.5 Radsteuerung — Elektrische Steuerung (Electric/Electromechanical Steering)

#### 3.5.1 Prinzip

Ein Elektromotor (Servo, Stepper oder Brushless DC) treibt den Ruderschaft ueber ein Getriebe an. Die Eingabe erfolgt ueber Steuerrad mit Sensor, Joystick oder digital.

**Aufbau Steer-by-Wire:**
```
Steuerrad mit Drehgeber (Encoder)
  |
Steuerungseinheit (ECU)
  |
Elektrischer Aktuator (Motor + Getriebe) am Ruderschaft
  |
Ruderwinkelsensor (Feedback)
  |
Optional: Haptic-Feedback-Motor am Steuerrad
```

#### 3.5.2 Einsatzbereiche

| Typ | Einsatz | Leistung | Hersteller |
|-----|---------|----------|------------|
| Elektromechanisch direkt | Kleinboote 4–8 m | 50–200 W | SeaStar Optimus |
| Steer-by-Wire | Motoryachten > 12 m | 200–2000 W | ZF Marine, Humphree |
| Elektrisch-hydraulisch | Segelyachten > 15 m | 200–1000 W | Jefa, Lewmar |
| Joystick-System | Manoevrieren | 100–500 W | Volvo IPS, Mercury Zeus |

#### 3.5.3 Vor- und Nachteile

**Vorteile:**
- Flexible Platzierung des Steuerrades (kein mechanischer Durchgang)
- Programmierbare Kennlinien (Empfindlichkeit, Geschwindigkeit)
- Einfache Integration von Autopilot
- Keine Hydraulikleitungen, kein Fluid
- Joystick-Docking moeglich

**Nachteile:**
- Abhaengigkeit von Stromversorgung (CRITICAL: Redundanz erforderlich)
- Kuenstliches Feedback (muss simuliert werden)
- Hoehere Komplexitaet der Elektronik
- EMV-Empfindlichkeit in Marineumgebung
- Weniger erprobt als mechanisch/hydraulisch
- Reparatur im Feld schwieriger

#### 3.5.4 Sicherheitsanforderungen Fly-by-Wire

| Anforderung | Umsetzung |
|-------------|-----------|
| Redundante Stromversorgung | Zwei getrennte Batteriekreise |
| Redundanter Datenbus | Doppelter CAN-Bus oder Ethernet |
| Fail-Safe-Modus | Ruder geht in Nullstellung bei Ausfall |
| Notsteuerung | Mechanischer Bypass zwingend |
| Ruderwinkelbegrenzung | Hardwareseitige Endschalter + Software-Limits |
| Diagnosesystem | Permanente Ueberwachung, Alarmmeldung |

### 3.6 Kabelsteuerung (Push-Pull Cable / Bowdenzug)

#### 3.6.1 Prinzip

Ein starre-flexibler Bowdenzug (Push-Pull-Kabel) verbindet die Steuerrad-Mechanik direkt mit dem Ruderhebel. Der Innenzug (Draht oder Stab) kann sowohl ziehen als auch druecken.

**Einsatzbereich:** Vorwiegend Motorboote bis ca. 12 m, Aussenbordmotoren, Innenbord-Z-Antriebe.

#### 3.6.2 Kabeltypen

| Typ | Hub | Max. Kraft (Push) | Max. Kraft (Pull) | Laenge |
|-----|-----|-------------------|-------------------|--------|
| Standard (SSC61/62) | 100–200 mm | 300 N | 600 N | 2–8 m |
| Heavy Duty (SSC134) | 150–250 mm | 800 N | 1200 N | 2–10 m |
| Dual Cable | 2× Standard | 2× 300 N | 2× 600 N | 2–8 m |
| Rotary (M66) | n/a (Drehung) | n/a | n/a | 2–12 m |

#### 3.6.3 Limitierungen

- Maximale Kabellaeange: Ca. 8–12 m (Reibung!)
- Nicht fuer Segelyachten mit Luvgierigkeit (Dauerlast auf Kabel)
- Kein Einsatz bei Rudermoment > ca. 300 Nm
- Min. Biegeradius: 200 mm (Standard), 300 mm (Heavy Duty)

### 3.7 Doppelsteueranlage (Dual Helm / Twin Wheel)

#### 3.7.1 Beschreibung

Zwei Steuerraeder (backbord und steuerbord), synchron verbunden, ermoeglichen Steuerung von beiden Cockpitseiten. Standard auf Yachten ab ca. 14 m.

**Varianten:**

| Variante | Verbindung | Einsatz |
|----------|-----------|---------|
| Doppelrad, mechanisch | Gemeinsame Welle oder Synchronseil | Segelyachten 12–18 m |
| Doppelrad, hydraulisch | Zwei Helm-Pumpen, ein Zylinder | Segelyachten 15–25 m |
| Cockpit + Flybridge | Zwei Helm-Pumpen, Lock-Ventile | Motoryachten 12–25 m |
| Cockpit + Innensteuerstd. | Hydraulik mit Umschaltventil | Motoryachten > 15 m |

#### 3.7.2 Synchronisation

**Mechanisch:** Zwei Raeder auf einer durchgehenden Welle oder ueber Synchronseil. Immer exakt synchron, aber aufwaendige Welleninstallation.

**Hydraulisch:** Jede Helm-Pumpe arbeitet auf denselben Zylinder. Wenn ein Rad gedreht wird, dreht das andere passiv mit. Komfort: Bypass-Ventil fuer leichtgaengiges Mitdrehen.

### 3.8 Notsteuerung (Emergency Steering)

#### 3.8.1 Anforderungen

- **CE-Kategorien A und B:** Notsteuerung zwingend vorgeschrieben
- **CE-Kategorien C und D:** Empfohlen, nicht zwingend
- **ISO 8847:** Notsteuerung muss ohne Werkzeug aktivierbar sein
- **Zeitvorgabe:** Umstellung auf Notsteuerung in max. 5 Minuten

#### 3.8.2 Notsteuerungs-Typen

| Typ | Beschreibung | Komplexitaet | Wirksamkeit |
|-----|-------------|-------------|-------------|
| Notpinne auf Ruderschaft | Steckpinne auf Sechskant/Quadrat-Kopf | Einfach | Hoch |
| Hilfssteuerrad | Zweites Rad direkt am Ruderschaft | Mittel | Hoch |
| Notruder (aufgesetzt) | Achtern montiertes Hilfsruder | Komplex | Mittel |
| Stroemungsruder (Drogue) | Schleppwiderstand zum Steuern | Einfach | Gering |
| Autopilot als Backup | Wenn Hauptsteuerung ausfaellt, Pilot steuert | Einfach | Hoch (wenn E-Versorgung) |

#### 3.8.3 Notpinne — Anforderungen

- Laenge: Mindestens 600 mm (besser 800–1000 mm fuer ausreichenden Hebelarm)
- Material: Edelstahl 316L oder hochfestes Aluminium
- Aufnahme: Muss ohne Spezialwerkzeug auf Ruderschaftkopf passen
- Zugang: Ruderschaftkopf muss zugaenglich sein (Cockpit-Locker oder Achterdeck)
- Kennzeichnung: Aufbewahrungsort muss klar gekennzeichnet sein
- Uebung: Crew sollte Umstellung jaehrlich ueben

---

## 4. Dimensionierung und Auslegung

### 4.1 Uebersicht Dimensionierungsparameter

Die Dimensionierung einer Steueranlage haengt von folgenden Hauptparametern ab:

| Parameter | Einheit | Einfluss |
|-----------|---------|----------|
| Bootlaenge (LOA) | m | Primaerer Skalierungsfaktor |
| Verdraengung | kg / t | Bestimmt Ruderblattgroesse |
| Ruderblattflaeche | m^2 | Direkt proportional zur Ruderkraft |
| Ruderblatttiefe (Chord) | m | Bestimmt Druckpunkt-Abstand |
| Balancegrad | - | Bestimmt Ruderschaftmoment |
| Max. Geschwindigkeit | kn | Quadratisch in Ruderkraft |
| Bootstyp | - | Segel vs. Motor, Fahrt vs. Regatta |
| CE-Kategorie | A/B/C/D | Normanforderungen, Sicherheitsfaktor |

### 4.2 Faustregeln zur Schnellauslegung

#### 4.2.1 Ruderblattflaeche nach Bootgroesse

```
Segelyacht (Spatenruder):
  A_ruder = LWL * T_max * k_ruder

  Wobei:
    LWL    = Wasserlinienlaenge [m]
    T_max  = Max. Tiefgang (Kiel) [m]
    k_ruder = 0.015–0.020 (Fahrt), 0.012–0.015 (Regatta)

Motorboot:
  A_ruder = LWL * T_prop * k_motor

  Wobei:
    T_prop  = Eintauchtiefe Propeller [m]
    k_motor = 0.025–0.035 (Verdraengerboot), 0.015–0.020 (Gleiter)
```

#### 4.2.2 Ruderschaftdurchmesser

```
d_schaft = k * (M_max / sigma_zul)^(1/3)

Vereinfachte Faustregel (Edelstahl 316L):
  Bootlaenge 6–8 m:    d = 25–30 mm
  Bootlaenge 8–10 m:   d = 30–35 mm
  Bootlaenge 10–12 m:  d = 35–40 mm
  Bootlaenge 12–15 m:  d = 40–50 mm
  Bootlaenge 15–18 m:  d = 50–60 mm
  Bootlaenge 18–22 m:  d = 60–75 mm
  Bootlaenge 22–28 m:  d = 75–90 mm
```

#### 4.2.3 Steuerungstyp nach Bootgroesse

| Bootlaenge | Segelboot | Motorboot |
|-----------|-----------|-----------|
| < 6 m | Pinne | Kabelsteuerung |
| 6–9 m | Pinne oder Rad (Seil) | Kabelsteuerung |
| 9–12 m | Rad (Seil/Kette) | Kabelsteuerung oder Hydraulik |
| 12–16 m | Rad (Seil) oder Hydraulik | Hydraulik |
| 16–20 m | Hydraulik | Hydraulik |
| 20–30 m | Hydraulik | Hydraulik oder Fly-by-Wire |
| > 30 m | Hydraulik + Autopilot | Fly-by-Wire |

### 4.3 Detaillierte Dimensionierung nach Herstellervorgaben

#### 4.3.1 Jefa Sizing Guide

Jefa (Daenemark) bietet das umfangreichste Dimensionierungssystem fuer Segelyacht-Steuerungen:

**Ruderlager-Auswahl nach Ruderschaftdurchmesser:**

| Jefa Lager-Serie | Schaftdurchmesser | Max. Rudermoment | Boot-Groesse |
|-----------------|-------------------|------------------|-------------|
| Jefa 20 | 20 mm | 80 Nm | 5–7 m |
| Jefa 25 | 25 mm | 140 Nm | 7–9 m |
| Jefa 30 | 30 mm | 250 Nm | 8–10 m |
| Jefa 35 | 35 mm | 400 Nm | 10–12 m |
| Jefa 40 | 40 mm | 600 Nm | 12–14 m |
| Jefa 45 | 45 mm | 850 Nm | 13–16 m |
| Jefa 50 | 50 mm | 1200 Nm | 15–18 m |
| Jefa 55 | 55 mm | 1600 Nm | 17–20 m |
| Jefa 60 | 60 mm | 2100 Nm | 19–23 m |
| Jefa 70 | 70 mm | 3200 Nm | 22–28 m |
| Jefa 80 | 80 mm | 4500 Nm | 26–32 m |
| Jefa 90 | 90 mm | 6000 Nm | 30–38 m |
| Jefa 100 | 100 mm | 8000 Nm | 35–45 m |

**Quadrant-Zuordnung:**

| Quadrant-Serie | Schaftdurchmesser | Radius | Material |
|---------------|-------------------|--------|----------|
| Jefa QU-200 | 20–30 mm | 200 mm | Aluminium hart-eloxiert |
| Jefa QU-250 | 25–35 mm | 250 mm | Aluminium hart-eloxiert |
| Jefa QU-300 | 30–40 mm | 300 mm | Aluminium hart-eloxiert |
| Jefa QU-350 | 35–50 mm | 350 mm | Aluminium hart-eloxiert |
| Jefa QU-400 | 40–55 mm | 400 mm | Aluminium hart-eloxiert |
| Jefa QU-450 | 50–70 mm | 450 mm | Bronze |

#### 4.3.2 Whitlock/Lewmar Sizing Guide

Whitlock (jetzt Teil von Lewmar) bietet Getriebe-Steuerungen fuer Segelyachten:

**Getriebe-Auswahl:**

| Getriebe | Untersetzung | Max. Rudermoment | Boot-Groesse | Kompatibel mit |
|----------|-------------|------------------|-------------|---------------|
| Whitlock Cobra 14 | 2.0:1 | 200 Nm | 8–11 m | Seilsteuerung |
| Whitlock Cobra 18 | 2.5:1 | 350 Nm | 10–13 m | Seilsteuerung |
| Whitlock Mamba 18 | 3.5:1 | 500 Nm | 12–15 m | Seilsteuerung |
| Whitlock Mamba 24 | 4.0:1 | 800 Nm | 14–18 m | Seilsteuerung |
| Whitlock Mamba 30 | 5.0:1 | 1200 Nm | 17–22 m | Seilsteuerung |

**Steuerseil-Dimensionierung (Whitlock):**

| Boot-Groesse | Seil-Dm | Ketten-Gliederlaenge | Quadrant-Radius |
|-------------|---------|---------------------|----------------|
| 8–10 m | 4 mm | 3/16" (4.8 mm) | 200–250 mm |
| 10–13 m | 5 mm | 1/4" (6.4 mm) | 250–300 mm |
| 13–16 m | 5 mm | 1/4" (6.4 mm) | 300–350 mm |
| 16–20 m | 6 mm | 5/16" (7.9 mm) | 350–400 mm |
| 20–24 m | 7 mm | 3/8" (9.5 mm) | 400–450 mm |

#### 4.3.3 Lewmar Hydraulik-Dimensionierung

| System | Verdrängung | Zylinder | Boot-Groesse | Max. Rudermoment |
|--------|-----------|---------|-------------|------------------|
| Lewmar Hydro 1 | 12 cm^3/Umdr. | Compact 150 | 10–13 m | 400 Nm |
| Lewmar Hydro 2 | 18 cm^3/Umdr. | Standard 200 | 13–16 m | 800 Nm |
| Lewmar Hydro 3 | 28 cm^3/Umdr. | Standard 250 | 16–20 m | 1400 Nm |
| Lewmar Hydro 4 | 40 cm^3/Umdr. | HD 300 | 20–26 m | 2500 Nm |
| Lewmar Hydro 5 | 60 cm^3/Umdr. | HD 400 | 26–35 m | 4500 Nm |

### 4.4 Dimensionierungsrechnung — Vollstaendiges Beispiel

**Aufgabe: Steueranlage fuer eine 13 m Fahrtensegelyacht (Beneteau Oceanis 43)**

```
Schritt 1: Basisdaten
  LOA     = 13.27 m
  LWL     = 11.75 m
  B_max   = 4.20 m
  T_max   = 2.10 m
  Depl.   = 9800 kg
  V_max   = 8.5 kn = 4.37 m/s
  CE-Kat  = A (Ozean)

Schritt 2: Ruderblattflaeche (Validierung)
  Gegeben: A_ruder = 0.48 m^2, c_ruder = 0.42 m
  Prüfung: A_check = LWL * T_max * 0.017
                    = 11.75 * 2.10 * 0.017
                    = 0.42 m^2
  -> Tatsaechlich etwas groesser, OK (mehr Ruderwirkung)

Schritt 3: Max. Ruderkraft
  F_max = 0.5 * 1025 * 4.37^2 * 0.48 * 1.10
        = 0.5 * 1025 * 19.10 * 0.48 * 1.10
        = 5166 N
  (C_N = 1.10 fuer NACA-Profil bei 20 Grad)

Schritt 4: Ruderschaftmoment
  Balancegrad B = 0.17 (Spatenruder mit Mini-Skeg)
  x_schaft = B * c_ruder = 0.17 * 0.42 = 0.071 m
  x_cp     = 0.26 * c_ruder = 0.26 * 0.42 = 0.109 m
  M_schaft = 5166 * (0.109 - 0.071) = 5166 * 0.038 = 196 Nm

Schritt 5: Sicherheitsfaktor (CE Kat A)
  SF = 2.0 (Kategorie A, Sturmboeen, Wellengang)
  M_auslegung = 196 * 2.0 = 392 Nm

Schritt 6: Komponentenwahl
  Ruderschaft:  40 mm Edelstahl 316L (Jefa 40, max. 600 Nm -> OK)
  Quadrant:     Jefa QU-300 (Radius 300 mm, fuer 30-40 mm Schaft)
  Getriebe:     Whitlock Mamba 18 (max. 500 Nm -> OK)
  Steuerrad:    1000 mm Durchmesser
  Seil:         5 mm 1×19 Edelstahl 316
  Kette:        1/4" (6.4 mm)

Schritt 7: Steuerkraft-Verifikation
  F_hand = M_auslegung / (MA_rad * MA_getriebe * R_quadrant)
  MA_rad = R_rad / R_kettenrad = 0.50 / 0.035 = 14.3
  F_hand = 392 / (14.3 * 3.5 * 0.30)
         = 392 / 15.02
         = 26.1 N (2.66 kgf)
  -> Unter 80 N Boeen-Grenzwert: OK
  -> Normalfahrt ca. 50% = 13 N: Unter 25 N Dauergrenze: OK

Schritt 8: AYDI-Bewertung
  Dimensionierung Score: 92/100 (korrekt dimensioniert, leichte Reserve)
  Confidence: "calculated"
```

### 4.5 Vergleich: Seilsteuerung vs. Hydraulik — Entscheidungsmatrix

Fuer die Praxis-Entscheidung zwischen Seilsteuerung und Hydraulik:

| Kriterium | Gewichtung | Seilsteuerung Score | Hydraulik Score |
|-----------|-----------|-------------------|-----------------|
| Ruderfeedback | 20% | 90 | 75 |
| Max. Bootgroesse | 15% | 60 | 100 |
| Installationsaufwand | 10% | 70 | 50 |
| Wartungsaufwand | 10% | 65 | 80 |
| Zuverlaessigkeit | 15% | 85 | 85 |
| Kosten | 10% | 90 | 50 |
| Autopilot-Integration | 10% | 60 | 95 |
| Flexibilitaet Verlegung | 5% | 60 | 90 |
| Doppelsteuerstand | 5% | 50 | 95 |

**Ergebnis (gewichtet):**
- Seilsteuerung: 74 Punkte — optimal bis ca. 14 m Segelyacht
- Hydraulik: 79 Punkte — optimal ab ca. 14 m oder bei Doppelsteuerstand

**Grenzbereich 12–16 m:** Beide Systeme moeglich. Entscheidungsfaktoren:
- Budget knapp -> Seilsteuerung
- Doppelsteuerstand gewuenscht -> Hydraulik
- Autopilot-Performance kritisch -> Hydraulik
- Traditionelles Steuergefuehl wichtig -> Seilsteuerung
- Offshore-Einsatz (CE Kat A) -> Seilsteuerung (einfachere Notsteuerung/Reparatur)

### 4.6 Dimensionierung der Notsteuerung

Die Notpinne muss so dimensioniert sein, dass das Boot bei reduzierter Geschwindigkeit steuerbar ist:

```
Auslegungsannahmen fuer Notpinne:
  Geschwindigkeit: 50% der Max.-Geschwindigkeit
  Rudermoment:     25% des Max.-Moments (quadratisch mit v)
  Max. Handkraft:  150 N (Notfall-Grenzwert)

Erforderliche Pinnenlaenge:
  L_notpinne = M_not / F_hand_max
  L_notpinne = 0.25 * M_auslegung / 150

Beispiel fuer M_auslegung = 400 Nm:
  L_notpinne = 0.25 * 400 / 150 = 0.667 m

-> Mindestens 700 mm Pinnenlaenge
-> Empfehlung: 800–1000 mm fuer komfortablere Bedienung
```

**Notpinnen-Aufnahme am Ruderschaft:**

| Aufnahme-Typ | Beschreibung | Sicherheit | Verbreitung |
|-------------|-------------|------------|-------------|
| Sechskant (SW) | Standardaufnahme, definierter Sitz | Hoch | Am haeufigsten |
| Vierkant | Aeltere Boote, einfache Herstellung | Hoch | Mittelhaeufig |
| Steckbolzen | Bolzen durch Schaft und Pinne | Sehr hoch | Superyachten |
| Flansch | Schraubbefestigung an Schaftplatte | Hoch | Motoryachten |
| Adapter-Aufnahme | Universaladapter fuer verschiedene Schafte | Mittel | Nachruestung |

### 4.7 Sonderfall Doppelruder (Twin Rudder)

Bei Doppelruder-Anlagen (verbreitet bei Performance-Cruisern wie z.B. Hallberg-Rassy, Beneteau First) gelten besondere Dimensionierungsregeln:

```
Pro Ruder:
  A_ruder_single = A_ruder_gesamt / 2
  M_schaft_single = M_schaft_gesamt * 0.55  (nicht exakt 50% wegen Interaktion)

Steueranlage:
  - Synchronisation beider Ruder zwingend (mechanisch oder hydraulisch)
  - Jefa bietet Twin-Rudder-Pakete mit Synchronwelle
  - Quadranten beider Ruder ueber Synchronseil oder -stange verbunden
  - ACHTUNG: Spiel in der Synchronisation fuehrt zu ungleichem Ruderwinkel
    -> AYDI-Befund-Schwere: SIGNIFICANT
```

---

## 5. Produktlinien und Hersteller

### 5.1 Jefa (Jefa Rudder Systems, Daenemark)

**Firmenportrait:**
- Gegruendet: 1981 in Aarhus, Daenemark
- Spezialisierung: Ruderlager, Ruderanlagen, Steuerungssysteme fuer Segelyachten
- Staerke: Kugelgelagerte Ruderlager, massgeschneiderte Systeme
- Marktposition: Premium-Segment, OEM fuer viele europaeische Werften
- Website: jfrb.com

#### 5.1.1 Ruderlager-Programm

| Produkt | Art.-Nr. | Schaft-Dm | Lager-Typ | Material | Preis (ca.) |
|---------|----------|-----------|-----------|----------|-------------|
| Jefa Ruderlager Standard 25 | JF-STD-25 | 25 mm | Gleitlager (PTFE) | Edelstahl 316L | 280 EUR |
| Jefa Ruderlager Standard 30 | JF-STD-30 | 30 mm | Gleitlager (PTFE) | Edelstahl 316L | 320 EUR |
| Jefa Ruderlager Standard 35 | JF-STD-35 | 35 mm | Gleitlager (PTFE) | Edelstahl 316L | 380 EUR |
| Jefa Ruderlager Standard 40 | JF-STD-40 | 40 mm | Gleitlager (PTFE) | Edelstahl 316L | 440 EUR |
| Jefa Ruderlager Standard 50 | JF-STD-50 | 50 mm | Gleitlager (PTFE) | Edelstahl 316L | 560 EUR |
| Jefa Ruderlager Kugel 25 | JF-BB-25 | 25 mm | Kugelgelagert | Edelstahl 316L | 520 EUR |
| Jefa Ruderlager Kugel 30 | JF-BB-30 | 30 mm | Kugelgelagert | Edelstahl 316L | 580 EUR |
| Jefa Ruderlager Kugel 35 | JF-BB-35 | 35 mm | Kugelgelagert | Edelstahl 316L | 660 EUR |
| Jefa Ruderlager Kugel 40 | JF-BB-40 | 40 mm | Kugelgelagert | Edelstahl 316L | 740 EUR |
| Jefa Ruderlager Kugel 45 | JF-BB-45 | 45 mm | Kugelgelagert | Edelstahl 316L | 860 EUR |
| Jefa Ruderlager Kugel 50 | JF-BB-50 | 50 mm | Kugelgelagert | Edelstahl 316L | 980 EUR |
| Jefa Ruderlager Kugel 55 | JF-BB-55 | 55 mm | Kugelgelagert | Edelstahl 316L | 1140 EUR |
| Jefa Ruderlager Kugel 60 | JF-BB-60 | 60 mm | Kugelgelagert | Edelstahl 316L | 1380 EUR |
| Jefa Ruderlager Kugel 70 | JF-BB-70 | 70 mm | Kugelgelagert | Edelstahl 316L | 1780 EUR |
| Jefa Ruderlager Kugel 80 | JF-BB-80 | 80 mm | Kugelgelagert | Edelstahl 316L | 2340 EUR |
| Jefa Ruderlager Kugel 90 | JF-BB-90 | 90 mm | Kugelgelagert | Edelstahl 316L | 3100 EUR |
| Jefa Ruderlager Kugel 100 | JF-BB-100 | 100 mm | Kugelgelagert | Edelstahl 316L | 4200 EUR |

#### 5.1.2 Quadranten und Hebel

| Produkt | Art.-Nr. | Schaft-Dm | Radius | Material | Preis (ca.) |
|---------|----------|-----------|--------|----------|-------------|
| Jefa Quadrant QU-200 | JF-QU200 | 20–30 mm | 200 mm | Alu hart-eloxiert | 195 EUR |
| Jefa Quadrant QU-250 | JF-QU250 | 25–35 mm | 250 mm | Alu hart-eloxiert | 240 EUR |
| Jefa Quadrant QU-300 | JF-QU300 | 30–40 mm | 300 mm | Alu hart-eloxiert | 295 EUR |
| Jefa Quadrant QU-350 | JF-QU350 | 35–50 mm | 350 mm | Alu hart-eloxiert | 360 EUR |
| Jefa Quadrant QU-400 | JF-QU400 | 40–55 mm | 400 mm | Alu hart-eloxiert | 440 EUR |
| Jefa Quadrant QU-450 | JF-QU450-BZ | 50–70 mm | 450 mm | Bronze | 680 EUR |
| Jefa Tiller Arm TA-200 | JF-TA200 | 20–35 mm | 200 mm | Edelstahl 316L | 165 EUR |
| Jefa Tiller Arm TA-250 | JF-TA250 | 25–40 mm | 250 mm | Edelstahl 316L | 195 EUR |
| Jefa Tiller Arm TA-300 | JF-TA300 | 30–50 mm | 300 mm | Edelstahl 316L | 240 EUR |
| Jefa Tiller Arm TA-350 | JF-TA350 | 35–55 mm | 350 mm | Edelstahl 316L | 295 EUR |
| Jefa Tiller Arm TA-400 | JF-TA400 | 40–70 mm | 400 mm | Edelstahl 316L | 380 EUR |

#### 5.1.3 Steuerungspakete

| Paket | Art.-Nr. | Boot-Groesse | Inhalt | Preis (ca.) |
|-------|----------|-------------|--------|-------------|
| Jefa Cable Steering Kit 30 | JF-CSK-30 | 8–10 m | Lager 30 + QU-250 + Seil + Rollen | 1200 EUR |
| Jefa Cable Steering Kit 35 | JF-CSK-35 | 10–12 m | Lager 35 + QU-300 + Seil + Rollen | 1550 EUR |
| Jefa Cable Steering Kit 40 | JF-CSK-40 | 12–14 m | Lager 40 + QU-350 + Seil + Rollen | 1950 EUR |
| Jefa Cable Steering Kit 50 | JF-CSK-50 | 15–18 m | Lager 50 + QU-400 + Seil + Rollen | 2800 EUR |
| Jefa Hydraulic Kit 40 | JF-HYD-40 | 12–15 m | Lager 40 + Zylinder + Pumpe + Leitungen | 3800 EUR |
| Jefa Hydraulic Kit 50 | JF-HYD-50 | 15–20 m | Lager 50 + Zylinder + Pumpe + Leitungen | 5200 EUR |
| Jefa Hydraulic Kit 60 | JF-HYD-60 | 20–25 m | Lager 60 + Zylinder + Pumpe + Leitungen | 7500 EUR |
| Jefa Twin Rudder Kit 35 | JF-TRK-35 | 10–13 m | 2× Lager + Synchro + Quadranten | 3200 EUR |
| Jefa Twin Rudder Kit 40 | JF-TRK-40 | 13–16 m | 2× Lager + Synchro + Quadranten | 4100 EUR |
| Jefa Twin Rudder Kit 50 | JF-TRK-50 | 16–20 m | 2× Lager + Synchro + Quadranten | 5800 EUR |

#### 5.1.4 Koker-Dichtungen und Zubehoer

| Produkt | Art.-Nr. | Schaft-Dm | Typ | Preis (ca.) |
|---------|----------|-----------|-----|-------------|
| Jefa Koker-Dichtung Lippe 25 | JF-KS-L25 | 25 mm | Lippendichtung | 45 EUR |
| Jefa Koker-Dichtung Lippe 30 | JF-KS-L30 | 30 mm | Lippendichtung | 52 EUR |
| Jefa Koker-Dichtung Lippe 35 | JF-KS-L35 | 35 mm | Lippendichtung | 58 EUR |
| Jefa Koker-Dichtung Lippe 40 | JF-KS-L40 | 40 mm | Lippendichtung | 65 EUR |
| Jefa Koker-Dichtung Lippe 50 | JF-KS-L50 | 50 mm | Lippendichtung | 78 EUR |
| Jefa Koker-Dichtung Lippe 60 | JF-KS-L60 | 60 mm | Lippendichtung | 95 EUR |
| Jefa PSS-Typ Koker 30 | JF-PSS-30 | 30 mm | Gleitringdichtung | 185 EUR |
| Jefa PSS-Typ Koker 40 | JF-PSS-40 | 40 mm | Gleitringdichtung | 220 EUR |
| Jefa PSS-Typ Koker 50 | JF-PSS-50 | 50 mm | Gleitringdichtung | 280 EUR |

### 5.2 Whitlock / Lewmar (Grossbritannien)

**Firmenportrait:**
- Whitlock: Gegruendet in den 1970er Jahren, seit ca. 2010 Teil von Lewmar
- Lewmar: Gegruendet 1946 in Havant, Hampshire, UK
- Spezialisierung: Komplette Decksausruestung, Steuergetriebe, Hydraulik
- Marktposition: Breitester Produktkatalog, OEM-Lieferant Nr. 1
- Website: lewmar.com

#### 5.2.1 Whitlock Getriebe-Steuerungen

| Produkt | Art.-Nr. | Untersetzung | Max. Moment | Boot-Groesse | Preis (ca.) |
|---------|----------|-------------|-------------|-------------|-------------|
| Whitlock Cobra 14 | WH-COB14 | 2.0:1 | 200 Nm | 8–11 m | 680 EUR |
| Whitlock Cobra 18 | WH-COB18 | 2.5:1 | 350 Nm | 10–13 m | 820 EUR |
| Whitlock Mamba 18 | WH-MAM18 | 3.5:1 | 500 Nm | 12–15 m | 1050 EUR |
| Whitlock Mamba 24 | WH-MAM24 | 4.0:1 | 800 Nm | 14–18 m | 1350 EUR |
| Whitlock Mamba 30 | WH-MAM30 | 5.0:1 | 1200 Nm | 17–22 m | 1780 EUR |
| Whitlock Mamba 36 | WH-MAM36 | 6.0:1 | 1800 Nm | 20–26 m | 2400 EUR |

#### 5.2.2 Lewmar Steuerraeder

| Produkt | Art.-Nr. | Durchmesser | Material | Griffe | Preis (ca.) |
|---------|----------|-------------|----------|--------|-------------|
| Lewmar Folding Wheel 24" | LW-FW24 | 610 mm | Edelstahl 316L | Gummi | 420 EUR |
| Lewmar Power Grip 28" | LW-PG28 | 711 mm | Edelstahl 316L | Gummi-Grip | 520 EUR |
| Lewmar Power Grip 32" | LW-PG32 | 813 mm | Edelstahl 316L | Gummi-Grip | 580 EUR |
| Lewmar Power Grip 36" | LW-PG36 | 914 mm | Edelstahl 316L | Gummi-Grip | 660 EUR |
| Lewmar Power Grip 40" | LW-PG40 | 1016 mm | Edelstahl 316L | Gummi-Grip | 780 EUR |
| Lewmar Teak Wheel 32" | LW-TK32 | 813 mm | Edelstahl/Teak | Teak-Griffe | 780 EUR |
| Lewmar Teak Wheel 36" | LW-TK36 | 914 mm | Edelstahl/Teak | Teak-Griffe | 880 EUR |
| Lewmar Teak Wheel 40" | LW-TK40 | 1016 mm | Edelstahl/Teak | Teak-Griffe | 1020 EUR |
| Lewmar Teak Wheel 48" | LW-TK48 | 1219 mm | Edelstahl/Teak | Teak-Griffe | 1350 EUR |
| Lewmar Carbon Wheel 36" | LW-CB36 | 914 mm | Carbon/Edelstahl | Leder | 2200 EUR |
| Lewmar Carbon Wheel 40" | LW-CB40 | 1016 mm | Carbon/Edelstahl | Leder | 2800 EUR |

#### 5.2.3 Lewmar Hydraulik-Systeme

| Produkt | Art.-Nr. | Verdr. | Max. Druck | Boot-Groesse | Preis (ca.) |
|---------|----------|--------|-----------|-------------|-------------|
| Lewmar Helm Pump H1 | LW-HP-H1 | 12 cm^3 | 60 bar | 10–13 m | 780 EUR |
| Lewmar Helm Pump H2 | LW-HP-H2 | 18 cm^3 | 80 bar | 13–16 m | 950 EUR |
| Lewmar Helm Pump H3 | LW-HP-H3 | 28 cm^3 | 100 bar | 16–20 m | 1250 EUR |
| Lewmar Helm Pump H4 | LW-HP-H4 | 40 cm^3 | 120 bar | 20–26 m | 1650 EUR |
| Lewmar Cylinder C150 | LW-CYL-150 | Hub 150 mm | 80 bar | 10–13 m | 580 EUR |
| Lewmar Cylinder C200 | LW-CYL-200 | Hub 200 mm | 100 bar | 13–16 m | 720 EUR |
| Lewmar Cylinder C250 | LW-CYL-250 | Hub 250 mm | 120 bar | 16–20 m | 920 EUR |
| Lewmar Cylinder C350 | LW-CYL-350 | Hub 350 mm | 150 bar | 20–28 m | 1380 EUR |
| Lewmar Cylinder C450 | LW-CYL-450 | Hub 450 mm | 200 bar | 28–38 m | 2100 EUR |

#### 5.2.4 Lewmar Steuerseile und Zubehoer

| Produkt | Art.-Nr. | Spezifikation | Preis (ca.) |
|---------|----------|--------------|-------------|
| Lewmar Steuerseil 4 mm, 10 m | LW-WR4-10 | 1×19 Edelstahl 316 | 45 EUR |
| Lewmar Steuerseil 5 mm, 10 m | LW-WR5-10 | 1×19 Edelstahl 316 | 58 EUR |
| Lewmar Steuerseil 6 mm, 10 m | LW-WR6-10 | 1×19 Edelstahl 316 | 72 EUR |
| Lewmar Umlenkrolle 65 mm | LW-SH65 | Kugelgelagert, Edelstahl | 42 EUR |
| Lewmar Umlenkrolle 80 mm | LW-SH80 | Kugelgelagert, Edelstahl | 56 EUR |
| Lewmar Umlenkrolle 100 mm | LW-SH100 | Kugelgelagert, Edelstahl | 78 EUR |
| Lewmar Kettenrad 3/16" | LW-SP316 | Edelstahl 316L | 38 EUR |
| Lewmar Kettenrad 1/4" | LW-SP14 | Edelstahl 316L | 45 EUR |
| Lewmar Kette 3/16", 1 m | LW-CH316 | Edelstahl 316L | 22 EUR |
| Lewmar Kette 1/4", 1 m | LW-CH14 | Edelstahl 316L | 28 EUR |

### 5.3 Edson (USA)

**Firmenportrait:**
- Gegruendet: 1859 in New Bedford, Massachusetts, USA
- Aeltester bestehender Hersteller von Yacht-Steueranlagen
- Spezialisierung: Pedestal-Steuerstaender, Radsteuerung, Guards
- Marktposition: Nordamerika-Marktfuehrer, OEM fuer US-Werften
- Website: edsonmarine.com

#### 5.3.1 Edson Pedestals (Steuerstaender)

| Produkt | Art.-Nr. | Typ | Schaftaufnahme | Boot-Groesse | Preis (ca.) |
|---------|----------|-----|---------------|-------------|-------------|
| Edson 335 Pedestal | ED-335 | Standard, ohne Getriebe | 1" (25.4 mm) | 7–10 m | 1200 USD |
| Edson 336 Pedestal | ED-336 | Standard, ohne Getriebe | 1.25" (31.8 mm) | 9–12 m | 1350 USD |
| Edson 337 Pedestal | ED-337 | Standard, mit Bremse | 1.25" (31.8 mm) | 10–13 m | 1600 USD |
| Edson 340 Pedestal | ED-340 | Heavy Duty | 1.5" (38.1 mm) | 12–16 m | 2100 USD |
| Edson 345 Pedestal | ED-345 | Heavy Duty | 1.75" (44.5 mm) | 15–20 m | 2800 USD |
| Edson 350 Pedestal | ED-350 | Super Heavy | 2.0" (50.8 mm) | 18–24 m | 3600 USD |
| Edson 360 Pedestal | ED-360 | Offshore | 2.0" (50.8 mm) | 20–28 m | 4500 USD |

#### 5.3.2 Edson Steuerraeder

| Produkt | Art.-Nr. | Durchmesser | Material | Preis (ca.) |
|---------|----------|-------------|----------|-------------|
| Edson Classic Teak 24" | ED-CL24 | 610 mm | Edelstahl/Teak | 850 USD |
| Edson Classic Teak 28" | ED-CL28 | 711 mm | Edelstahl/Teak | 950 USD |
| Edson Classic Teak 32" | ED-CL32 | 813 mm | Edelstahl/Teak | 1100 USD |
| Edson Classic Teak 36" | ED-CL36 | 914 mm | Edelstahl/Teak | 1250 USD |
| Edson Classic Teak 40" | ED-CL40 | 1016 mm | Edelstahl/Teak | 1450 USD |
| Edson Ultra Teak 36" | ED-UL36 | 914 mm | Edelstahl/Teak (schlank) | 1400 USD |
| Edson Ultra Teak 40" | ED-UL40 | 1016 mm | Edelstahl/Teak (schlank) | 1650 USD |
| Edson PowerWheel 28" | ED-PW28 | 711 mm | Edelstahl/Composite | 650 USD |
| Edson PowerWheel 32" | ED-PW32 | 813 mm | Edelstahl/Composite | 750 USD |
| Edson Comfort Grip 32" | ED-CG32 | 813 mm | Edelstahl/Gummi | 580 USD |
| Edson Comfort Grip 36" | ED-CG36 | 914 mm | Edelstahl/Gummi | 680 USD |

#### 5.3.3 Edson Quadranten und Zubehoer

| Produkt | Art.-Nr. | Spezifikation | Preis (ca.) |
|---------|----------|--------------|-------------|
| Edson Quadrant 10" | ED-QD10 | 254 mm, Aluminium | 280 USD |
| Edson Quadrant 12" | ED-QD12 | 305 mm, Aluminium | 340 USD |
| Edson Quadrant 14" | ED-QD14 | 356 mm, Aluminium/Bronze | 420 USD |
| Edson Quadrant 16" | ED-QD16 | 406 mm, Bronze | 560 USD |
| Edson Quadrant 18" | ED-QD18 | 457 mm, Bronze | 720 USD |
| Edson Wire Kit 3/16" | ED-WK316 | Komplett-Set mit Klemmen | 120 USD |
| Edson Wire Kit 1/4" | ED-WK14 | Komplett-Set mit Klemmen | 145 USD |
| Edson Sheave Kit (2 Stk) | ED-SK65 | 65 mm kugelgelagert | 95 USD |
| Edson Sheave Kit (2 Stk) | ED-SK80 | 80 mm kugelgelagert | 115 USD |
| Edson Emergency Tiller | ED-ET | Universal, Edelstahl | 180 USD |

### 5.4 Kobelt Manufacturing (Kanada)

**Firmenportrait:**
- Gegruendet: 1962 in Surrey, British Columbia, Kanada
- Spezialisierung: Hochleistungs-Hydrauliksteuerungen, Motorenkontrollen
- Marktposition: Premium-Segment fuer Motorboote und Arbeitsschiffe
- Website: kobeltmfg.com

#### 5.4.1 Kobelt Hydraulik-Steuerungen

| Produkt | Art.-Nr. | Verdr./Umdr. | Max. Druck | Einsatz | Preis (ca.) |
|---------|----------|-------------|-----------|---------|-------------|
| Kobelt 7003 | KB-7003 | 1.5 cu.in. | 1000 psi | Motorboote 8–12 m | 850 USD |
| Kobelt 7004 | KB-7004 | 2.0 cu.in. | 1500 psi | Motorboote 10–15 m | 1100 USD |
| Kobelt 7005 | KB-7005 | 3.0 cu.in. | 1500 psi | Motorboote 12–18 m | 1400 USD |
| Kobelt 7006 | KB-7006 | 5.0 cu.in. | 2000 psi | Yachten 15–22 m | 1900 USD |
| Kobelt 7008 | KB-7008 | 8.0 cu.in. | 2000 psi | Yachten 20–30 m | 2600 USD |
| Kobelt 7012 | KB-7012 | 12.0 cu.in. | 2500 psi | Superyachten > 25 m | 3800 USD |
| Kobelt 7080 Power Assist | KB-7080 | Elektro-Hydraulisch | 2000 psi | Yachten > 18 m | 4500 USD |

#### 5.4.2 Kobelt Zylinder

| Produkt | Art.-Nr. | Bohrung/Hub | Max. Kraft | Einsatz | Preis (ca.) |
|---------|----------|------------|-----------|---------|-------------|
| Kobelt 2010 | KB-2010 | 2.0"/6" | 4400 lbs | Boote 8–12 m | 520 USD |
| Kobelt 2012 | KB-2012 | 2.5"/8" | 7400 lbs | Boote 12–16 m | 720 USD |
| Kobelt 2014 | KB-2014 | 3.0"/10" | 10600 lbs | Boote 16–22 m | 980 USD |
| Kobelt 2016 | KB-2016 | 3.5"/12" | 14500 lbs | Boote 22–30 m | 1350 USD |
| Kobelt 2020 | KB-2020 | 4.0"/14" | 18900 lbs | Boote > 28 m | 1850 USD |

### 5.5 Lecomble & Schmitt (Frankreich)

**Firmenportrait:**
- Gegruendet: 1872 in Boulogne-sur-Mer, Frankreich
- Spezialisierung: Hydraulische Steueranlagen und Autopilot-Antriebe
- Staerke: Proportional-Hydraulik, kompakte Bauweise, Autopilot-Integration
- Marktposition: Frankreich und Mittelmeer, OEM fuer Beneteau/Jeanneau
- Website: lecomble-schmitt.com

#### 5.5.1 Lecomble & Schmitt Helm-Pumpen

| Produkt | Art.-Nr. | Verdr./Umdr. | Max. Druck | Boot-Groesse | Preis (ca.) |
|---------|----------|-------------|-----------|-------------|-------------|
| L&S HP 60 | LS-HP60 | 6 cm^3 | 60 bar | 8–10 m | 480 EUR |
| L&S HP 100 | LS-HP100 | 10 cm^3 | 80 bar | 10–13 m | 620 EUR |
| L&S HP 150 | LS-HP150 | 15 cm^3 | 100 bar | 13–16 m | 780 EUR |
| L&S HP 200 | LS-HP200 | 20 cm^3 | 120 bar | 16–20 m | 980 EUR |
| L&S HP 300 | LS-HP300 | 30 cm^3 | 150 bar | 20–26 m | 1350 EUR |
| L&S HP 400 | LS-HP400 | 40 cm^3 | 150 bar | 26–35 m | 1800 EUR |

#### 5.5.2 Lecomble & Schmitt Drehkolben-Aktuatoren

| Produkt | Art.-Nr. | Max. Drehmoment | Drehwinkel | Schaft-Dm | Preis (ca.) |
|---------|----------|----------------|-----------|-----------|-------------|
| L&S RV 120 | LS-RV120 | 120 Nm | ±35° | 25–30 mm | 680 EUR |
| L&S RV 250 | LS-RV250 | 250 Nm | ±35° | 30–40 mm | 880 EUR |
| L&S RV 500 | LS-RV500 | 500 Nm | ±35° | 35–50 mm | 1200 EUR |
| L&S RV 1000 | LS-RV1000 | 1000 Nm | ±35° | 45–60 mm | 1800 EUR |
| L&S RV 2000 | LS-RV2000 | 2000 Nm | ±35° | 55–80 mm | 2800 EUR |
| L&S RV 3000 | LS-RV3000 | 3000 Nm | ±35° | 70–100 mm | 4200 EUR |

#### 5.5.3 Lecomble & Schmitt Komplettsysteme

| Paket | Art.-Nr. | Inhalt | Boot-Groesse | Preis (ca.) |
|-------|----------|--------|-------------|-------------|
| L&S Kit Sail 100 | LS-KS100 | HP 100 + RV 250 + Leitungen | 10–13 m | 1650 EUR |
| L&S Kit Sail 200 | LS-KS200 | HP 200 + RV 500 + Leitungen | 13–18 m | 2400 EUR |
| L&S Kit Sail 300 | LS-KS300 | HP 300 + RV 1000 + Leitungen | 18–24 m | 3800 EUR |
| L&S Kit Motor 100 | LS-KM100 | HP 100 + Zylinder + Leitungen | 8–12 m | 1450 EUR |
| L&S Kit Motor 200 | LS-KM200 | HP 200 + Zylinder + Leitungen | 12–18 m | 2200 EUR |
| L&S Kit Motor 300 | LS-KM300 | HP 300 + Zylinder + Leitungen | 18–25 m | 3500 EUR |

#### 5.5.4 Lecomble & Schmitt Autopilot-Antriebe

| Produkt | Art.-Nr. | Typ | Leistung | Kompatibel | Preis (ca.) |
|---------|----------|-----|----------|-----------|-------------|
| L&S AP Drive 60 | LS-AP60 | Hydraulik-Pumpe | 12V/80W | Raymarine, Simrad, B&G | 1200 EUR |
| L&S AP Drive 120 | LS-AP120 | Hydraulik-Pumpe | 12V/120W | Raymarine, Simrad, B&G | 1650 EUR |
| L&S AP Drive 250 | LS-AP250 | Hydraulik-Pumpe | 24V/250W | Raymarine, Simrad, B&G | 2400 EUR |
| L&S AP Drive 500 | LS-AP500 | Hydraulik-Pumpe | 24V/500W | Alle Systeme | 3800 EUR |

### 5.6 SeaStar Solutions / Teleflex Marine (USA/Kanada)

**Firmenportrait:**
- SeaStar Solutions (ehemals Teleflex Marine): Groesster Hersteller fuer Motorboot-Steuerungen weltweit
- Marken: SeaStar, BayStar, Hynautic, Teleflex
- Spezialisierung: Kabelsteuerungen, Hydraulik fuer Motorboote, Aussenborder
- Marktposition: Massenmarkt-Fuehrer, OEM fuer fast alle US-Motorbootwerften
- Website: seastarsolutions.com

#### 5.6.1 SeaStar Kabelsteuerungen

| Produkt | Art.-Nr. | Typ | Max. Motor-PS | Laenge | Preis (ca.) |
|---------|----------|-----|-------------|--------|-------------|
| Teleflex SSC61 Safe-T | SS-SSC61 | Rotary Cable, Standard | 55 HP | 8–20 ft | 35–80 USD |
| Teleflex SSC62 Safe-T | SS-SSC62 | Rotary Cable, Quick-Connect | 55 HP | 8–20 ft | 40–90 USD |
| Teleflex SSC134 Safe-T QC | SS-SSC134 | Rotary Cable, Heavy Duty | 150 HP | 8–24 ft | 55–120 USD |
| Teleflex M66 Dual Cable | SS-M66 | Rack & Pinion Dual | 300 HP | 10–28 ft | 120–200 USD |
| SeaStar NFB (No-Feedback) | SS-NFB | Rotary NFB | 300 HP | 10–28 ft | 80–150 USD |

#### 5.6.2 SeaStar Hydraulik-Systeme

| Produkt | Art.-Nr. | Zylinder | Motor-Bereich | Boot-Groesse | Preis (ca.) |
|---------|----------|---------|-------------|-------------|-------------|
| BayStar Standard | SS-BAY-STD | Compact | 150 HP / 1 Motor | 5–8 m | 650 USD |
| BayStar Plus | SS-BAY-PLS | Standard | 300 HP / 1 Motor | 7–10 m | 850 USD |
| SeaStar 1.0 | SS-SS10 | Front Mount | 300 HP / 2 Motoren | 8–12 m | 1200 USD |
| SeaStar 1.7 | SS-SS17 | Front Mount HD | 600 HP / 2 Motoren | 10–14 m | 1650 USD |
| SeaStar 2.0 | SS-SS20 | Front Mount XHD | 800 HP / 3 Motoren | 12–18 m | 2400 USD |

#### 5.6.3 SeaStar Optimus (Steer-by-Wire)

| Produkt | Art.-Nr. | Typ | Einsatz | Preis (ca.) |
|---------|----------|-----|---------|-------------|
| Optimus 360 | SS-OPT360 | Joystick + Steer-by-Wire | Motorboote mit Pod/Stern | 8000 USD |
| Optimus EPS | SS-OPTEPS | Electronic Power Steering | Motorboote bis 12 m | 3500 USD |

### 5.7 Weitere Hersteller

#### 5.7.1 Edson Notpinne und Spezialartikel

| Produkt | Art.-Nr. | Beschreibung | Preis (ca.) |
|---------|----------|-------------|-------------|
| Edson Universal Emergency Tiller | ED-UET | Fuer 1"–2" Schaft, Edelstahl | 180 USD |
| Edson Quadrant Guard | ED-QG | Schutzring fuer Quadrant | 85 USD |
| Edson Cable Clamp Kit | ED-CCK | Klemmgarnitur fuer Steuerseil | 35 USD |
| Edson Pedestal Brake Kit | ED-PBK | Radbremse nachruestbar | 220 USD |

#### 5.7.2 Spinlock (Steuerrad-Zubehoer)

| Produkt | Art.-Nr. | Beschreibung | Preis (ca.) |
|---------|----------|-------------|-------------|
| Spinlock Wheel Grip Pair | SPL-WG | Nachruestbare Teak-Griffe | 95 EUR |

#### 5.7.3 Ultraflex (Italien)

| Produkt | Art.-Nr. | Typ | Einsatz | Preis (ca.) |
|---------|----------|-----|---------|-------------|
| Ultraflex T67 Helm | UF-T67 | Mechanische Radsteuerung | Motorboote 4–8 m | 120 EUR |
| Ultraflex T85 Helm | UF-T85 | Mechanische Radsteuerung | Motorboote 6–10 m | 180 EUR |
| Ultraflex GOTECH Hydraulik | UF-GOTECH | Hydraulik-Komplettset | Motorboote 8–12 m | 950 EUR |
| Ultraflex UC128 Kabel | UF-UC128 | Push-Pull Steuerkabel | Motorboote | 25–60 EUR |

#### 5.7.4 ZF Marine (Deutschland)

| Produkt | Art.-Nr. | Typ | Einsatz | Preis (ca.) |
|---------|----------|-----|---------|-------------|
| ZF SteerCommand | ZF-SC | Fly-by-Wire | Motoryachten > 15 m | Ab 15000 EUR |
| ZF ProSteer | ZF-PS | Elektro-Hydraulisch | Motoryachten > 20 m | Ab 20000 EUR |

#### 5.7.5 Humphree (Schweden)

| Produkt | Art.-Nr. | Typ | Einsatz | Preis (ca.) |
|---------|----------|-----|---------|-------------|
| Humphree EPS | HU-EPS | Electronic Power Steering | Motoryachten 10–20 m | Ab 6000 EUR |
| Humphree Interceptor Steering | HU-IS | Interceptor + Steuerung | Motoryachten > 12 m | Ab 12000 EUR |
| Humphree Lightning | HU-LGT | Stabilisierung + Steuerung | Motoryachten > 15 m | Ab 25000 EUR |

#### 5.7.6 Solimar / Goiot (Frankreich)

| Produkt | Art.-Nr. | Typ | Einsatz | Preis (ca.) |
|---------|----------|-----|---------|-------------|
| Goiot Steuerrad Teak 800 | GO-TK800 | Steuerrad | Segelyachten 8–12 m | 420 EUR |
| Goiot Steuerrad Teak 1000 | GO-TK1000 | Steuerrad | Segelyachten 12–16 m | 580 EUR |
| Goiot Steuerrad Teak 1200 | GO-TK1200 | Steuerrad | Segelyachten 16–20 m | 780 EUR |

#### 5.7.7 Vetus (Niederlande)

| Produkt | Art.-Nr. | Typ | Einsatz | Preis (ca.) |
|---------|----------|-----|---------|-------------|
| Vetus Hydraulik-Set HTP20 | VT-HTP20 | Komplett-Hydraulik | Motorboote 8–12 m | 1100 EUR |
| Vetus Hydraulik-Set HTP30 | VT-HTP30 | Komplett-Hydraulik | Motorboote 10–14 m | 1450 EUR |
| Vetus Hydraulik-Set HTP42 | VT-HTP42 | Komplett-Hydraulik HD | Motorboote 12–18 m | 1950 EUR |
| Vetus Steuerrad V60 schwarz | VT-V60B | Rad, Kunststoff | Motorboote 5–10 m | 85 EUR |
| Vetus Steuerrad V80 Edelstahl | VT-V80S | Rad, Edelstahl/Griff | Motorboote 7–12 m | 220 EUR |

### 5.8 Hersteller-Vergleichsmatrix

| Eigenschaft | Jefa | Whitlock/Lewmar | Edson | Kobelt | L&S | SeaStar |
|-------------|------|----------------|-------|--------|-----|---------|
| Ruderlager | ★★★★★ | ★★★ | ★★ | — | — | — |
| Seilsteuerung | ★★★★ | ★★★★★ | ★★★★ | — | — | ★★ |
| Hydraulik | ★★★★ | ★★★★ | ★★ | ★★★★★ | ★★★★★ | ★★★★ |
| Steuerraeder | ★★★ | ★★★★ | ★★★★★ | — | — | ★★ |
| Fly-by-Wire | — | ★★ | — | ★★★ | — | ★★★★ |
| Preis/Leistung | ★★★★ | ★★★★ | ★★★ | ★★★ | ★★★★ | ★★★★★ |
| OEM-Verfuegbarkeit | ★★★★ | ★★★★★ | ★★★ | ★★★ | ★★★★ | ★★★★★ |
| Ersatzteil-Verfuegbarkeit | ★★★★ | ★★★★★ | ★★★★ | ★★★ | ★★★ | ★★★★★ |
| Dokumentation/Support | ★★★★★ | ★★★★ | ★★★★ | ★★★ | ★★★ | ★★★★ |

**Legende:** ★ = grundlegend, ★★★ = gut, ★★★★★ = marktfuehrend, — = nicht im Programm

### 5.9 Ersatzteil-Verfuegbarkeit und Austauschbarkeit

Ein haeufiges Problem bei aelteren Steueranlagen ist die Ersatzteil-Beschaffung. Hier eine Uebersicht der Kompatibilitaet:

| Original-Hersteller | Ersatz durch | Kompatibilitaet | Bemerkung |
|---------------------|-------------|-----------------|-----------|
| Whitlock (alt) | Lewmar (aktuell) | Hoch | Lewmar fuehrt Whitlock-Ersatzteile weiter |
| Edson (alt) | Edson (aktuell) | Hoch | Edson pflegt Rueckwaerts-Kompatibilitaet |
| Teleflex Marine | SeaStar Solutions | Vollstaendig | Namensaenderung, gleiche Produkte |
| Hynautic | SeaStar Solutions | Hoch | Uebernommen, Teile weiterhin lieferbar |
| Enkes (NL) | Jefa | Mittel | Anpassung erforderlich |
| Goiot (alt) | Lewmar/Jefa | Gering | Meist Neukonstruktion erforderlich |
| Merriman (USA, hist.) | Edson | Gering | Historisch, Sonderanfertigung |

**AYDI-Pruefpunkt:** Bei Booten aelter als 20 Jahre Ersatzteil-Verfuegbarkeit als Risikofaktor bewerten (Score-Malus -5 bis -15 wenn Hersteller nicht mehr existent).

---

## 6. Normen und Vorschriften

### 6.1 ISO 8847:2021 — Kleine Wasserfahrzeuge — Steueranlagen — Seil- und Flaschenzugsysteme

#### 6.1.1 Anwendungsbereich

Gilt fuer Steueranlagen mit Seil-, Ketten- und Flaschenzugsystemen auf Booten bis 24 m Rumpflaenge. Betrifft sowohl Segel- als auch Motorboote.

#### 6.1.2 Wesentliche Anforderungen

| Anforderung | Spezifikation |
|-------------|--------------|
| Seilbruchlast | Min. 6× Betriebslast |
| Klemmenbruchlast | Min. 4× Betriebslast |
| Umlenkrollen-Bruchlast | Min. 4× Betriebslast |
| Quadranten-Befestigung | Formschluessig + Klemmung, min. 4× Betriebslast |
| Seilspannung | Muss einstellbar sein (Spannschloss oder Spanner) |
| Freigaengigkeit | Voller Ruderausschlag ohne Blockierung moeglich |
| Endanschlaege | Mechanische Begrenzung des Ruderausschlags |
| Notsteuerung | Fuer CE Kat A und B zwingend |
| Korrosionsschutz | Alle Teile min. Edelstahl 304 oder gleichwertig |
| Mindest-Seil-Dm | 3.2 mm (1/8") fuer Boote unter 8 m |
| Mindest-Seil-Dm | 4.8 mm (3/16") fuer Boote 8–15 m |
| Mindest-Seil-Dm | 6.4 mm (1/4") fuer Boote ueber 15 m |

#### 6.1.3 Pruefanforderungen

| Pruefung | Methode | Akzeptanzkriterium |
|----------|---------|-------------------|
| Statische Last | 2× Betriebslast fuer 15 Min. | Keine bleibende Verformung |
| Dynamische Last | 100.000 Zyklen bei Betriebslast | Keine Ermuedungsbrueche |
| Korrosionspruefung | Salzspruehtest 500 h (ISO 9227) | Keine Funktionsbeeintraechtigung |
| Temperaturtest | -10 Grad C bis +65 Grad C | Volle Funktion |

### 6.2 ISO 10592:2022 — Kleine Wasserfahrzeuge — Steueranlagen — Fernbetaetigte Hydrauliksteuerungen

#### 6.2.1 Anwendungsbereich

Gilt fuer hydraulische Steueranlagen auf Booten bis 24 m. Umfasst Helm-Pumpen, Leitungen, Zylinder, Aktuatoren.

#### 6.2.2 Wesentliche Anforderungen

| Anforderung | Spezifikation |
|-------------|--------------|
| Berstdruck | Min. 4× Arbeitsdruck |
| Pruedruck | 1.5× Arbeitsdruck fuer 5 Minuten |
| Leckage | Max. 1 Tropfen/Min. bei Arbeitsdruck |
| Steuerkraft (Rad) | Max. 28 daN (280 N) unter ungünstigsten Bedingungen |
| Steuerkraft (Dauer) | Max. 12 daN (120 N) bei Normalfahrt |
| Entlueftung | System muss vollstaendig entlueftbar sein |
| Reservoir | Ausdehnung bei Temperatur muss kompensiert werden |
| Notsteuerung | Fuer CE Kat A/B zwingend, bypass moeglich |
| Leitungsmaterial | Kupfer, Edelstahl oder zugelassener Schlauch |
| Min. Leitungs-ID | 6 mm (1/4") |
| Fluid-Kompatibilitaet | Alle Dichtungen kompatibel mit spezifiziertem Fluid |

#### 6.2.3 Hydraulik-Spezifische Pruefungen

| Pruefung | Methode | Akzeptanzkriterium |
|----------|---------|-------------------|
| Berstdruck-Pruefung | Hydrostatisch bis 4× AP | Kein Bruch |
| Dichtheitspruefung | 1.5× AP, 5 Min. | Keine Leckage |
| Impulspruefung | 200.000 Zyklen, 0 bis AP | Keine Ermuedung |
| Vibrationspruefung | Nach ISO 8846 | Keine Lockerung |
| Feuer-Resistance | 2.5 Min. offene Flamme (Schlaeuche) | Kein Bruch |

> ⚠️ **ZU PRÜFEN (Audit):** Vibrationspruefung "Nach ISO 8846" — ISO 8846 regelt "Kleine Wasserfahrzeuge — Elektrische Geraete — Schutz gegen Entzuendung umgebender brennbarer Gase" (Zuendschutz elektrischer Geraete), NICHT die Vibrationspruefung von Hydrauliksteuerungen. Die tatsaechlich zutreffende Vibrations-Pruefnorm ist nicht zweifelsfrei bestimmbar — Normnummer unverifiziert (estimated — unverifiziert).

### 6.3 ABYC P-21 — Hydraulic Steering Systems (US-Standard)

#### 6.3.1 Anwendungsbereich

ABYC P-21 ist der US-amerikanische Freiwilligstandard fuer (manuelle und servounterstuetzte) hydraulische Steueranlagen. Wird von der US Coast Guard als Referenz herangezogen. (Hinweis: ABYC P-23 betrifft dagegen mechanische Steuer- und Antriebsbedienung von Jetbooten, nicht Hydrauliksteuerungen.)

#### 6.3.2 Wesentliche Unterschiede zu ISO

| Parameter | ISO 10592 | ABYC P-21 |
|-----------|----------|-----------|
| Berstdruck | 4× AP | 4× AP (gleich) |
| Pruedruck | 1.5× AP | 2× AP (strenger) |
| Steuerkraft | 28 daN | 30 lbs (133 N, strenger) |
| Leitungsmaterial | Cu, SS, Schlauch | Cu, SS, Schlauch (gleich) |
| Fluidspezifikation | Herstellervorgabe | MIL-H-5606 oder aequivalent |
| Temperaturbereich | -10 bis +65 Grad C | -18 bis +60 Grad C (kaelter) |

### 6.4 CE-Kategorien und Steueranlagen

| CE-Kategorie | Notsteuerung | Redundanz | Zusaetzliche Anforderungen |
|-------------|-------------|-----------|---------------------------|
| A (Ozean) | Pflicht | Empfohlen | Seegangs-Sicherheitsfaktor 2.0 |
| B (Offshore) | Pflicht | Empfohlen | Sicherheitsfaktor 1.75 |
| C (Inshore) | Empfohlen | Optional | Sicherheitsfaktor 1.5 |
| D (Geschuetzt) | Optional | Optional | Sicherheitsfaktor 1.25 |

### 6.5 Klassifikationsgesellschaften

Fuer Yachten ueber 24 m und gewerbliche Yachten gelten Klasse-Vorschriften:

| Klasse | Regelwerk | Besonderheit |
|--------|----------|-------------|
| Lloyd's Register | SSC Rules | Redundante Steuerung ab 500 GT |
| DNV-GL | RU-HSLC | Fly-by-Wire: 2-Fehler-Toleranz |
| Bureau Veritas | NR467 | Automatische Rueckkehr auf Mitte bei Ausfall |
| RINA | Rules for Yachts | Doppelte Steuerung ab 35 m |
| ABS | ABS Rules for Yachts | Notsteuerung mit max. 60 s Aktivierung |

### 6.6 Nationale Vorschriften

| Land | Vorschrift | Besonderheit |
|------|-----------|-------------|
| Deutschland | See-BG, SportSee-ZuSt | CE-Konformitaet, Notsteuerung |
| UK | MCA LY3 (>24m) | Redundante Steuerung fuer Charter |
| Frankreich | Division 240/245 | Notsteuerung fuer Kat. 1–3 |
| USA | USCG 33 CFR | ABYC als Referenz |
| Australien | NSCV Part C5 | Aehnlich ISO, nationale Abweichungen |

---

## 7. Fehlerbild-Atlas

### 7.1 Systematik

Der Fehlerbild-Atlas verwendet den Code **STEER-Fxx** fuer alle Steueranlagen-Fehlerbilder. Die Codierung folgt dem AYDI-Standard:

```
STEER-F01 bis STEER-F12: Mechanische Steuerungen
STEER-F13 bis STEER-F18: Hydraulische Steuerungen (spaetere Erweiterung)
```

### 7.2 STEER-F01 — Steuerseildehnung / Seillaengung

| Attribut | Wert |
|----------|------|
| Code | STEER-F01 |
| Bezeichnung | Steuerseildehnung / Seillaengung |
| Schwere | MODERATE (3) |
| Confidence (visuell) | visual_medium |
| Haeufigkeit | 25 % aller Seilsteuerungen > 5 Jahre |
| Betroffene Systeme | Seil-/Kettensteuerungen |

**Symptome:**
- Uebermaeassiges Spiel am Steuerrad (Totgang > 5 Grad)
- Seil liegt lose auf den Umlenkrollen
- Ungleichmaessige Seilspannung (eine Seite schlaff)

**Ursachen:**
- Normales Setzen des Seils in den ersten 1–2 Jahren (Konstruktionsdehnung)
- Uebermaessige Belastung (Boen, harter Ruderdruck)
- Korrosion der Einzeldraehte (Festigkeitsverlust)
- Spannschloss/Spanner am Anschlag

**Massnahmen:**
1. Seilspannung pruefen und nachstellen (Spannschloss)
2. Bei Spannschloss am Anschlag: Seil kuerzen oder erneuern
3. Seil auf Litzenbrueche pruefen (Handschuh-Test)
4. Umlenkrollen auf freien Lauf pruefen

**AYDI-Score-Einfluss:** -10 bis -25 Punkte auf Steueranlagen-Score

### 7.3 STEER-F02 — Seil-Litzenbruch / Kinkung

| Attribut | Wert |
|----------|------|
| Code | STEER-F02 |
| Bezeichnung | Seil-Litzenbruch / Kinkung |
| Schwere | SIGNIFICANT (4) bis CRITICAL (5) |
| Confidence (visuell) | visual_high |
| Haeufigkeit | 10 % aller Seilsteuerungen > 10 Jahre |
| Betroffene Systeme | Seil-/Kettensteuerungen |

**Symptome:**
- Sichtbare gebrochene Einzeldraehte (Fischhaken)
- Knick im Seil (Kinkung)
- Seilquerschnitt sichtbar reduziert
- Raues Steuergefuehl (Seil hakt in Rolle)

**Ursachen:**
- Ermuedung durch wiederholte Biegung ueber zu kleine Umlenkrollen
- Korrosion (insbesondere im Bereich Koker/Bilge)
- Mechanische Beschaedigung
- Falscher Seiltyp (7×19 statt 1×19 oder umgekehrt)

**Massnahmen:**
1. Seil SOFORT erneuern (bei Litzenbruch am tragenden Querschnitt: CRITICAL)
2. Umlenkrollen auf korrekten Durchmesser pruefen (min. 12× Seil-Dm)
3. Ursache der Korrosion beseitigen (Entwaesserung, Ventilation)
4. Korrekten Seiltyp waehlen

**AYDI-Score-Einfluss:** -30 bis -60 Punkte, bei mehreren Bruechen: CRITICAL-Befund

### 7.4 STEER-F03 — Quadranten-Lockerung

| Attribut | Wert |
|----------|------|
| Code | STEER-F03 |
| Bezeichnung | Quadranten-Lockerung am Ruderschaft |
| Schwere | SIGNIFICANT (4) |
| Confidence (visuell) | visual_medium |
| Haeufigkeit | 8 % aller Quadranten-Steuerungen > 8 Jahre |
| Betroffene Systeme | Seil-/Ketten- und Hydrauliksteuerungen mit Quadrant |

**Symptome:**
- Klickgeraeusch beim Richtungswechsel
- Totgang am Steuerrad (Rad dreht, Ruder nicht)
- Sichtbare Relativbewegung Quadrant/Schaft

**Ursachen:**
- Klemmschrauben locker (Vibration)
- Keil/Nut-Verbindung ausgeschlagen
- Konischer Sitz oxidiert (Passungsrost)
- Falsche Passung Quadrant/Schaft

**Massnahmen:**
1. Klemmschrauben mit Drehmomentschluessel nachziehen (Hersteller-Spec)
2. Keil/Nut pruefen, ggf. Keil erneuern
3. Konischen Sitz reinigen und mit Anti-Seize einfetten (NIE Schmierung bei Konuspassung!)
4. Loctite 648 (Fuegeverbindung) als Sicherung

**AYDI-Score-Einfluss:** -25 bis -45 Punkte

### 7.5 STEER-F04 — Umlenkrollen-Verschleiss

| Attribut | Wert |
|----------|------|
| Code | STEER-F04 |
| Bezeichnung | Umlenkrollen verschlissen/blockiert |
| Schwere | MODERATE (3) |
| Confidence (visuell) | visual_high |
| Haeufigkeit | 15 % aller Seilsteuerungen > 7 Jahre |
| Betroffene Systeme | Seil-/Kettensteuerungen |

**Symptome:**
- Schwergaengige Steuerung
- Quietschen oder Knirschen beim Steuern
- Sichtbarer Rollenverschleiss (Rille, Abflachung)
- Seil laeuft nicht mittig auf Rolle

**Ursachen:**
- Lagerschaden durch Salzwasser/fehlende Schmierung
- Ueberlast (falsche Rollengroesse)
- Korrosion der Lagerachse
- Alter (Gleitlager aus Delrin abgenutzt)

**Massnahmen:**
1. Umlenkrollen erneuern (komplett, nicht nur Lager)
2. Kugelgelagerte Rollen verwenden (laengere Lebensdauer)
3. Regelmaessige Schmierung einplanen
4. Korrekten Rollendurchmesser waehlen (min. 12× Seil-Dm)

**AYDI-Score-Einfluss:** -15 bis -30 Punkte

### 7.6 STEER-F05 — Pedestal-Getriebe-Verschleiss

| Attribut | Wert |
|----------|------|
| Code | STEER-F05 |
| Bezeichnung | Getriebeverschleiss im Pedestal |
| Schwere | MODERATE (3) bis SIGNIFICANT (4) |
| Confidence (visuell) | visual_low (intern, schlecht einsehbar) |
| Haeufigkeit | 5 % aller Pedestal-Steuerungen > 10 Jahre |
| Betroffene Systeme | Radsteuerungen mit Pedestal-Getriebe |

**Symptome:**
- Spiel am Steuerrad (Hin-und-Her-Wackeln)
- Mahlende Geraeusche beim Steuern
- Erschwerte Radbewegung in bestimmten Positionen

**Ursachen:**
- Fehlende Schmierung ueber Jahre
- Korrosion der Zahnraeder
- Normaler Verschleiss (Lebensdauer: 15–25 Jahre bei korrekter Wartung)

**Massnahmen:**
1. Pedestal oeffnen, Getriebe inspizieren
2. Schmierung erneuern (Hersteller-spezifisches Fett)
3. Zahnraeder pruefen (Zahnflanken-Verschleiss, Pittings)
4. Bei starkem Verschleiss: Getriebe-Revision oder Austausch

**AYDI-Score-Einfluss:** -20 bis -40 Punkte

### 7.7 STEER-F06 — Ruderlager-Verschleiss

| Attribut | Wert |
|----------|------|
| Code | STEER-F06 |
| Bezeichnung | Ruderlager verschlissen |
| Schwere | SIGNIFICANT (4) |
| Confidence (visuell) | visual_medium (Radialspiel prufbar) |
| Haeufigkeit | 12 % aller Yachten > 12 Jahre |
| Betroffene Systeme | Alle Steuerungstypen |

**Symptome:**
- Spiel am Ruderblatt (wackelt seitlich)
- Klopfgeraeusche bei Seegang
- Wasser tritt verstaerkt am Koker aus
- Schwammiges Steuergefuehl

**Ursachen:**
- Normaler Verschleiss der Gleitlagerbuchse
- Korrosion am Ruderschaft (Spaltkorrosion im Lagerbereich)
- Fehlende Schmierung
- Schockbelastung (Grundberuehrung, Treibgut)

**Massnahmen:**
1. Radialspiel messen (max. 0.5 mm bei neuen Lagern, Austausch bei > 1.5 mm)
2. Gleitlager erneuern (Boot muss meist aus dem Wasser)
3. Schaft im Lagerbereich pruefen (Korrosion, Unebenheiten)
4. Upgrade auf Jefa Kugellager erwaegen (langlebiger)

**AYDI-Score-Einfluss:** -25 bis -50 Punkte

### 7.8 STEER-F07 — Hydraulikleckage

| Attribut | Wert |
|----------|------|
| Code | STEER-F07 |
| Bezeichnung | Hydraulikfluid-Leckage |
| Schwere | MODERATE (3) bis CRITICAL (5) |
| Confidence (visuell) | visual_high |
| Haeufigkeit | 18 % aller Hydrauliksteuerungen > 5 Jahre |
| Betroffene Systeme | Hydraulische Steuerungen |

**Symptome:**
- Oelflecken unter Zylinder oder an Leitungen
- Fluessigkeitsstand im Reservoir sinkt
- Schwammiges Steuergefuehl (Luft im System durch Fluidverlust)
- Steuerkraft erhoet sich

**Ursachen:**
- Dichtungsverschleiss an Zylinder (O-Ringe, Lippendichtungen)
- Verschraubungen lose (Vibration)
- Leitungskorrosion (Kupfer: Gruenspan, Lochfrass)
- Schlauchalterung (UV, Waerme im Maschinenraum)

**Massnahmen:**
1. Leckagequelle lokalisieren (Papiertest: weisses Papier unterlegen)
2. Verschraubungen nachziehen (ACHTUNG: Kupfer nicht ueberdrehen!)
3. Dichtungen erneuern (nur Original-Ersatzteile verwenden)
4. Schlaeuche alle 7–10 Jahre praeventiv erneuern
5. System entlueften und Fluid nachfuellen

**AYDI-Score-Einfluss:** -15 (Schwitzen) bis -60 (aktiver Fluid-Verlust)

### 7.9 STEER-F08 — Luft in Hydrauliksystem

| Attribut | Wert |
|----------|------|
| Code | STEER-F08 |
| Bezeichnung | Luft in Hydrauliksystem |
| Schwere | MODERATE (3) bis SIGNIFICANT (4) |
| Confidence (visuell) | visual_low (nicht sichtbar, nur spuerbar) |
| Haeufigkeit | 20 % aller Hydrauliksteuerungen (intermittierend) |
| Betroffene Systeme | Hydraulische Steuerungen |

**Symptome:**
- Schwammiges, undefniertes Steuergefuehl
- Steuerrad muss weiter gedreht werden fuer gleichen Ruderausschlag
- Geraeusche (Gurgeln) in Leitungen
- Wechselnder Widerstand beim Steuern

**Ursachen:**
- Ungenuegend entlueftet (nach Fluidwechsel/Reparatur)
- Schleichende Leckage (Fluid-Verlust -> Luft gezogen)
- Temperaturwechsel (Luft expandiert -> Blasenbildung)
- Pumpen-Wellendichtring defekt (Luft gesaugt)

**Massnahmen:**
1. System vollstaendig entlueften (Entlueftungsschraube oeffnen, Rad drehen)
2. Fluid nachfuellen (nur spezifizierter Typ!)
3. Leckage suchen und beseitigen
4. Nach Entlueftung: Probefahrt, nochmals pruefen

**AYDI-Score-Einfluss:** -20 bis -40 Punkte

### 7.10 STEER-F09 — Korrosion am Ruderschaft

| Attribut | Wert |
|----------|------|
| Code | STEER-F09 |
| Bezeichnung | Ruderschaft-Korrosion |
| Schwere | SIGNIFICANT (4) bis CRITICAL (5) |
| Confidence (visuell) | visual_medium |
| Haeufigkeit | 8 % aller Yachten > 15 Jahre |
| Betroffene Systeme | Alle Steuerungstypen |

**Symptome:**
- Sichtbare Korrosion (Lochfrass, Flaechen-Korrosion) am Schaft
- Verfaerbung/Rost an Schaftdurchfuehrung
- Schwergaengige Ruderbewegung (Schaft sitzt fest im Lager)
- Im Extremfall: Ruderblatt-Verlust!

**Ursachen:**
- Galvanische Korrosion (fehlende/verbrauchte Opferanoden)
- Spaltkorrosion im Lagerbereich
- Edelstahl 304 statt 316L verwendet
- Fehlende Schmierung im Koker-Bereich

**Massnahmen:**
1. Schaft visuell und per Ultraschall-Dickenmessung pruefen
2. Bei Materialverlust > 10%: Schaft erneuern (CRITICAL)
3. Opferanoden pruefen/erneuern
4. Korrekte Materialauswahl sicherstellen (316L oder Duplex)
5. Galvanischen Trennschutz installieren

**AYDI-Score-Einfluss:** -30 bis -80 Punkte (je nach Materialverlust)

### 7.11 STEER-F10 — Autopilot-Steuerungskonflikt

| Attribut | Wert |
|----------|------|
| Code | STEER-F10 |
| Bezeichnung | Autopilot-Steuerungskonflikt |
| Schwere | MODERATE (3) |
| Confidence (visuell) | visual_low |
| Haeufigkeit | 10 % aller Yachten mit Autopilot |
| Betroffene Systeme | Alle Steuerungen mit Autopilot-Integration |

**Symptome:**
- Autopilot kaempft gegen Handsteuerung
- Steuerrad dreht sich unerwartet
- Erhoehter Stromverbrauch im Autopilot-Betrieb
- Unruhige Kurssteuerung

**Ursachen:**
- Fehlende Kupplung/Bypass zwischen Autopilot und Handsteuerung
- Autopilot-Einstellungen falsch (Gain, Counter-Rudder)
- Rudersensor defekt oder falsch kalibriert
- Hydraulik-Bypass-Ventil defekt

**Massnahmen:**
1. Bypass-/Kupplungsmechanismus pruefen
2. Rudersensor kalibrieren
3. Autopilot-Parameter anpassen (Sea State, Response, Gain)
4. Hydraulik-Bypass-Ventil pruefen (Funktion und Dichtheit)

**AYDI-Score-Einfluss:** -15 bis -30 Punkte

### 7.12 STEER-F11 — Koker-Undichtigkeit

| Attribut | Wert |
|----------|------|
| Code | STEER-F11 |
| Bezeichnung | Steuerkoker undicht |
| Schwere | MODERATE (3) bis SIGNIFICANT (4) |
| Confidence (visuell) | visual_high |
| Haeufigkeit | 15 % aller Yachten > 10 Jahre |
| Betroffene Systeme | Alle Steuerungen mit Koker-Durchfuehrung |

**Symptome:**
- Wasser im Ruderkasten/Achterpiek
- Tropfen am Koker-Rohr sichtbar
- Korrosion an umgebenden Metallteilen
- Bei Seegang: Spritzwasser aus Koker

**Ursachen:**
- Dichtung verschlissen (Lippendichtung, Stopfbuchse)
- Koker-Rohr in Laminat undicht (GFK-Anbindung)
- Ruderschaft-Oberflaechenschaden im Dichtungsbereich
- Falsche Dichtungsart fuer Anwendung

**Massnahmen:**
1. Dichtung erneuern (Typ beachten: Stopfbuchse vs. Lippendichtung vs. PSS)
2. Schaft-Oberflaeche im Dichtungsbereich pruefen (Riefen, Korrosion)
3. GFK-Anbindung Koker/Rumpf pruefen
4. Upgrade auf Jefa PSS-Typ Dichtung erwaegen

**AYDI-Score-Einfluss:** -15 bis -35 Punkte

### 7.13 STEER-F12 — Steuerrad-Nabe/Konusverbindung

| Attribut | Wert |
|----------|------|
| Code | STEER-F12 |
| Bezeichnung | Steuerrad-Nabe lose / Konuspassung defekt |
| Schwere | MODERATE (3) bis SIGNIFICANT (4) |
| Confidence (visuell) | visual_high |
| Haeufigkeit | 6 % aller Radsteuerungen > 8 Jahre |
| Betroffene Systeme | Radsteuerungen |

**Symptome:**
- Steuerrad wackelt auf der Welle
- Klickgeraeusch bei Richtungswechsel
- Rad rutscht durch (kann drehen ohne Ruderausschlag!)

**Ursachen:**
- Mutter locker (fehlende Sicherung)
- Konussitz ausgeschlagen (Passungsrost)
- Keil gebrochen oder fehlend
- Falsches Rad fuer Wellenkegelform

**Massnahmen:**
1. Mutter nachziehen und mit Splint/Sicherungsmutter sichern
2. Konusflaechen reinigen, pruefen, ggf. Kegel nachschleifen
3. Keil erneuern (Originalabmessung!)
4. Herstellervorgabe fuer Rad/Welle-Kombination pruefen

**AYDI-Score-Einfluss:** -20 bis -45 Punkte

---

## 8. Troubleshooting

### 8.1 Entscheidungsbaum 1: Schwergaengige Steuerung

```
SYMPTOM: Steuerung schwergaengig
|
+-- Radsteuerung (Seil/Kette)?
|   |
|   +-- Seilspannung zu hoch?
|   |   -> Spannung reduzieren (Spannschloss)
|   |
|   +-- Umlenkrollen schwergaengig?
|   |   -> Rollen pruefen/erneuern, schmieren
|   |   -> STEER-F04
|   |
|   +-- Pedestal-Getriebe schwergaengig?
|   |   -> Getriebe oeffnen, schmieren
|   |   -> STEER-F05
|   |
|   +-- Ruderlager schwergaengig?
|       -> Lager pruefen (Spiel, Korrosion)
|       -> STEER-F06
|
+-- Hydrauliksteuerung?
|   |
|   +-- Fluid-Stand niedrig?
|   |   -> Nachfuellen, Leckage suchen
|   |   -> STEER-F07
|   |
|   +-- Luft im System?
|   |   -> Entlueften
|   |   -> STEER-F08
|   |
|   +-- Bypass-Ventil offen?
|   |   -> Ventil schliessen
|   |
|   +-- Zylinder schwergaengig?
|       -> Zylinder pruefen (interne Dichtung)
|
+-- Kabelsteuerung?
    |
    +-- Kabel knickt?
    |   -> Biegeradien pruefen, Kabel erneuern
    |
    +-- Kabel korrodiert?
        -> Kabel erneuern, Ursache beseitigen
```

### 8.2 Entscheidungsbaum 2: Spiel am Steuerrad (Totgang)

```
SYMPTOM: Spiel / Totgang am Steuerrad
|
+-- Seilsteuerung?
|   |
|   +-- Seil lose?
|   |   -> Seilspannung nachstellen
|   |   -> STEER-F01
|   |
|   +-- Quadrant lose?
|   |   -> Klemmung nachziehen
|   |   -> STEER-F03
|   |
|   +-- Kettenrad/Kette verschlissen?
|       -> Kette und Kettenrad erneuern (immer zusammen!)
|
+-- Hydrauliksteuerung?
|   |
|   +-- Luft im System?
|   |   -> Entlueften
|   |   -> STEER-F08
|   |
|   +-- Interne Leckage im Zylinder?
|       -> Zylinderdichtungen erneuern
|
+-- Alle Typen:
    |
    +-- Ruderlager verschlissen?
    |   -> Spiel am Ruderblatt pruefen
    |   -> STEER-F06
    |
    +-- Steuerrad-Nabe lose?
        -> Mutter, Keil, Konus pruefen
        -> STEER-F12
```

### 8.3 Entscheidungsbaum 3: Hydraulik-Probleme

```
SYMPTOM: Hydraulik funktioniert nicht korrekt
|
+-- Kein Ruderausschlag bei Raddrehung?
|   |
|   +-- Fluid leer?
|   |   -> Leckage! Sofort reparieren
|   |   -> STEER-F07 (CRITICAL)
|   |
|   +-- Bypass-Ventil offen?
|   |   -> Ventil schliessen
|   |
|   +-- Pumpe defekt?
|       -> Pumpe pruefen (interne Dichtung)
|
+-- Langsamer Ruderausschlag?
|   |
|   +-- Fluid niedrig?
|   |   -> Nachfuellen, Leckage suchen
|   |
|   +-- Luft im System?
|   |   -> Entlueften
|   |   -> STEER-F08
|   |
|   +-- Leitung verengt?
|       -> Leitungen pruefen (Knicke, Ablagerungen)
|
+-- Ungleichmaessig (eine Richtung schwerer)?
    |
    +-- Zylinderdichtung einseitig defekt?
    |   -> Zylinder ueberholen
    |
    +-- Leitung einseitig blockiert?
        -> Beide Leitungen pruefen
```

### 8.4 Entscheidungsbaum 4: Geraeusche beim Steuern

```
SYMPTOM: Ungewoehnliche Geraeusche beim Steuern
|
+-- Quietschen / Knirschen?
|   |
|   +-- Umlenkrollen?
|   |   -> Schmierung, ggf. Austausch
|   |   -> STEER-F04
|   |
|   +-- Ruderlager?
|   |   -> Lager pruefen
|   |   -> STEER-F06
|   |
|   +-- Koker-Dichtung?
|       -> Dichtung pruefen, ggf. locker/trocken
|
+-- Klicken / Klopfen?
|   |
|   +-- Bei Richtungswechsel?
|   |   -> Quadrant lose oder Kette verschlissen
|   |   -> STEER-F03
|   |
|   +-- Bei Seegang?
|       -> Ruderlager-Spiel
|       -> STEER-F06
|
+-- Gurgeln (Hydraulik)?
    -> Luft im System
    -> STEER-F08
```

### 8.5 Entscheidungsbaum 5: Kurs laeuft weg

```
SYMPTOM: Boot haelt Kurs nicht / driftet
|
+-- Pinnensteuerung?
|   |
|   +-- Helm-Balance pruefen (Luvgierigkeit?)
|   |   -> Segelstellung, Trimm anpassen
|   |
|   +-- Ruderblatt beschaedigt?
|       -> Unterwasser-Inspektion
|
+-- Radsteuerung?
|   |
|   +-- Totgang vorhanden?
|   |   -> Siehe Entscheidungsbaum 2
|   |
|   +-- Autopilot-Konflikt?
|   |   -> STEER-F10
|   |
|   +-- Ruderblatt-Problem?
|       |
|       +-- Bewuchs am Ruder?
|       |   -> Reinigung
|       |
|       +-- Deformation/Delaminierung?
|           -> Unterwasser-Inspektion, ggf. Reparatur
|
+-- Alle Typen:
    +-- Ruder zeigt Flattern (fluttering)?
        -> Ruderlager-Spiel, Ruderblatt-Deformation
        -> STEER-F06, Strukturpruefung
```

---

## 9. FAQ — Haeufig gestellte Fragen

### Frage 1: Wann sollte man von Pinne auf Radsteuerung umruesten?

**Antwort:** Eine Umruestung von Pinne auf Radsteuerung ist sinnvoll, wenn:
- Die Steuerkraefte bei Normalfahrt dauerhaft ueber 30 N liegen (Ermüdung)
- Das Boot laenger als 10–11 m ist und viel Hochseefahrt gemacht wird
- Ein leistungsfaehiger Autopilot integriert werden soll
- Mehrere Personen steuern und unterschiedliche Koerperkraft haben

**Kosten:** Ca. 2500–5000 EUR fuer komplette Seilsteuerung inkl. Pedestal und Montage.
**Nachteile:** Gewichtszunahme (15–25 kg), Wartungsaufwand steigt, direktes Rudergefuehl geht teilweise verloren.
**AYDI-Bewertung Confidence:** estimated

### Frage 2: Wie oft muss eine Seilsteuerung komplett erneuert werden?

**Antwort:** Steuerseile sollten alle 5–7 Jahre praeventiv erneuert werden, auch wenn kein sichtbarer Schaden vorliegt. Leitfaden:
- Jaehrliche Inspektion auf Litzenbrueche (Handschuhtest: mit Stoffhandschuh ueber Seil fahren)
- Sofortiger Austausch bei erstem sichtbaren Litzenbruch
- Kette alle 8–10 Jahre (weniger Verschleiss, da weniger Biegung)
- Umlenkrollen alle 10–15 Jahre oder bei feststellbarem Lagerschaden
**AYDI-Bewertung Confidence:** documented

### Frage 3: Hydraulik oder Seilsteuerung — was ist besser?

**Antwort:** Keine generelle Ueberlegenheit. Entscheidungskriterien:

| Kriterium | Seilsteuerung | Hydraulik |
|-----------|--------------|-----------|
| Feedback | Besser (direkt) | Gut (mit FU-Pumpe) |
| Wartung | Regelmaessig (Seilspannung) | Weniger haeufig, aber aufwaendiger |
| Zuverlaeigkeit | Hoch (einfach) | Hoch (weniger Verschleissteile) |
| Kosten Erstausruestung | Niedriger | Hoeher |
| Doppelsteuerstand | Aufwaendig | Einfach (Leitung verlegen) |
| Autopilot-Integration | Moeglich (Linear/Rotary) | Einfacher (Hydraulikpumpe) |
| Max. Bootgroesse | Ca. 20 m | Unbegrenzt |
| Flexibilitaet Verlegung | Mittel (Umlenkrollen) | Hoch (Leitung biegbar) |

**Empfehlung:** Bis 14 m Segelyacht: Seilsteuerung. 14–20 m: beides moeglich. Ueber 20 m: Hydraulik.
**AYDI-Bewertung Confidence:** benchmark

### Frage 4: Was ist ein Whitlock-Getriebe und brauche ich eines?

**Antwort:** Ein Whitlock-Getriebe (Cobra oder Mamba) ist ein Untersetzungsgetriebe, das im Pedestal zwischen Steuerrad und Seilantrieb sitzt. Es vervielfacht die Steuerkraft und ermoeglicht kleinere Steuerraeder bei gleicher Kraftwirkung. Erforderlich ab ca. 11–12 m Bootlaenge oder wenn die Steuerkraefte ohne Getriebe zu hoch sind (>80 N bei Boeen).
**AYDI-Bewertung Confidence:** measured

### Frage 5: Kann ich Hydraulikfluid verschiedener Hersteller mischen?

**Antwort:** NEIN. Niemals verschiedene Hydraulikfluids mischen. Auch Fluids des gleichen Typs verschiedener Hersteller koennen unterschiedliche Additive enthalten, die miteinander reagieren und zu Dichtungsschaeden, Viskositaetsveraenderungen und Systemversagen fuehren. Immer nur das vom Steueranlagen-Hersteller spezifizierte Fluid verwenden. Bei Unsicherheit: System komplett spuelen und mit einem einzigen Fluid befuellen.
**AYDI-Bewertung Confidence:** measured

### Frage 6: Wie erkenne ich, ob mein Ruderlager verschlissen ist?

**Antwort:** Am Ruderblatt anfassen (bei herausgenommenem Boot) und seitlich bewegen. Spiel ueber 1.5 mm ist ein klares Zeichen. Im Wasser: Klopfgeraeusche bei Seegang, schwammiges Steuergefuehl, sichtbarer Wasseraustritt am Koker. Messung mit Messuhr am Schaft am aussagekraeftigsten.
**AYDI-Bewertung Confidence:** visual_medium (Hand-Test), measured (Messuhr)

### Frage 7: Was kostet ein Ruderlager-Wechsel?

**Antwort:** Material: 200–1200 EUR (je nach Lager-Typ und Groesse). Arbeit: 800–2500 EUR (Boot muss raus, Ruder muss raus, ggf. Koker bearbeiten). Gesamtkosten typisch: 1500–4000 EUR. Bei Gelegenheit (Winterlager, Osmosesanierung) sind die Kosten deutlich geringer, da das Boot ohnehin aus dem Wasser ist.
**AYDI-Bewertung Confidence:** benchmark

### Frage 8: Mein Autopilot arbeitet sehr unruhig. Liegt das an der Steueranlage?

**Antwort:** Moeglich. Haeufige Ursachen in der Steueranlage:
1. Zu viel Spiel (Totgang) — Autopilot muss uebersteuern -> Pendeln
2. Zu viel Reibung — Autopilot erreicht Ruderstellung nicht -> Nachsteuern
3. Rudersensor falsch positioniert oder kalibriert
4. Hydraulik: Bypass-Ventil schleicht (Autopilot verliert Ruderdruck)
5. Helmbalance schlecht (staendige Korrektur noetig)

**Erste Massnahme:** Spiel und Reibung in der Steueranlage reduzieren (>50 % der Faelle!).
**AYDI-Bewertung Confidence:** documented

### Frage 9: Brauche ich eine Notsteuerung?

**Antwort:** Fuer CE-Kategorie A (Ozean) und B (Offshore): JA, zwingend vorgeschrieben. Fuer Kategorie C und D: dringend empfohlen. Eine Notpinne kostet 100–300 EUR und kann im Ernstfall Leben retten. Sie muss auf den Ruderschaftkopf passen und ohne Werkzeug montierbar sein. Jaehrliches Probemanöver ist Pflicht (CE Kat A/B) bzw. empfohlen.
**AYDI-Bewertung Confidence:** measured (CE-Vorschrift)

### Frage 10: Was bedeutet "Steering Ratio" und welches ist optimal?

**Antwort:** Das Steering Ratio gibt die Radumdrehungen pro Grad Ruderausschlag an. Niedrige Ratio = direkt (wenige Umdrehungen fuer vollen Ausschlag, hohe Steuerkraefte). Hohe Ratio = indirekt (viele Umdrehungen, niedrige Steuerkraefte). Optimal:
- Regattasegler: 2.5–3.5 Umdrehungen (Anschlag zu Anschlag)
- Fahrtensegler: 3.5–5.0 Umdrehungen
- Motorboot (langsam): 3.0–4.0 Umdrehungen
- Motorboot (schnell): 2.0–3.0 Umdrehungen
**AYDI-Bewertung Confidence:** benchmark

### Frage 11: Kann ich ein groesseres Steuerrad nachrüsten, um leichter zu steuern?

**Antwort:** Ja, ein groesseres Rad erhoet den mechanischen Vorteil und reduziert die Steuerkraft. Die Kraft sinkt proportional zum Radiuszuwachs. Beispiel: Von 800 mm auf 1000 mm = 25% weniger Kraft. Aber: Groesseres Rad braucht mehr Platz, kann den Cockpit-Durchgang behindern, und das Steuerungsverhaeltnis wird indirekter (mehr Umdrehungen fuer gleichen Ruderausschlag).
**AYDI-Bewertung Confidence:** calculated

### Frage 12: Wie entlueftet man eine Hydrauliksteuerung richtig?

**Antwort:** Schrittweise Anleitung:
1. Reservoir auffuellen (korrektes Fluid!)
2. Entlueftungsschraube am Zylinder leicht oeffnen
3. Steuerrad langsam Anschlag-zu-Anschlag drehen (beide Richtungen)
4. Wenn Fluid blasenfrei aus Entlueftungsschraube kommt: schliessen
5. Schritt 2–4 fuer andere Seite wiederholen
6. Reservoir nochmals pruefen und auffuellen
7. Entlueftungsschraube am Zylinder FEST schliessen
8. Probefahrt, nach 30 Min. nochmals pruefen
**AYDI-Bewertung Confidence:** documented

### Frage 13: Wie bemerke ich, dass mein Steuerseil bald bricht?

**Antwort:** Warnzeichen:
- Einzelne abstehende Drahte (Fischhaken) — visuell mit Handschuhtest
- Seil ist im Bereich der Umlenkrollen duenner als anderswo
- Erhoehter Totgang trotz korrekter Spannung (Seil hat sich permanent gelaengt)
- Rost/Verfaerbung (korrodierte Drahte brechen frueher)
- Kinkung (bleibender Knick) — Seil sofort ersetzen
**AYDI-Bewertung Confidence:** visual_high

### Frage 14: Ist eine elektrische Steuerung fuer Segelyachten empfehlenswert?

**Antwort:** Stand 2026 eher nicht fuer reine Segelyachten unter 20 m. Gruende:
- Abhaengigkeit von Stromversorgung (auf langer Fahrt kritisch)
- Kuenstliches Feedback (Segler schaetzen natuerliches Rudergefuehl)
- Weniger erprobt im Offshore-Bereich
- Reparatur im Feld schwieriger

Fuer Motoryachten und Superyachten ab 15 m ist Steer-by-Wire dagegen zunehmend Standard (integrierbar mit Joystick-Docking, Autopilot, Dynamic Positioning).
**AYDI-Bewertung Confidence:** benchmark

### Frage 15: Was ist der Unterschied zwischen einem Quadranten und einem Tiller-Arm?

**Antwort:** Beide dienen als Hebel am Ruderschaft fuer die Seil-/Ketten-Anbindung:
- **Quadrant:** Halbkreisfoermig (ca. 140–160 Grad), Seil laeuft in einer Nut. Erlaubt groessere Ruderwinkel, gleichmaessigere Kraftuebertragung.
- **Tiller-Arm:** Einzelner gerader Hebel, Seil-Anbindung an einem Punkt. Einfacher, kompakter, aber begrenzterer Ruderwinkel und ungleichmaessigere Kraftuebertragung (Sinusfunktion).

Empfehlung: Quadrant fuer Dauerinstallation, Tiller-Arm fuer Nachruestung oder wenn Platz begrenzt ist.
**AYDI-Bewertung Confidence:** measured

### Frage 16: Wie pruefe ich die korrekte Seilspannung?

**Antwort:** Am laengsten freien Seilstueck (zwischen zwei Umlenkrollen) mit Daumendruck (ca. 5 kgf = 50 N) druecken. Die Auslenkung sollte 10–15 mm betragen. Zu straff: erhoehte Reibung, vorzeitiger Verschleiss. Zu locker: Totgang, Seil kann von Rollen springen. Spannung bei Geradeaus-Ruder pruefen.
**AYDI-Bewertung Confidence:** documented

### Frage 17: Warum tropft Wasser aus meinem Steuerkoker?

**Antwort:** Der Steuerkoker ist die Rohr-Durchfuehrung des Ruderschafts durch den Rumpf. Wasser tritt aus, wenn:
1. Die Koker-Dichtung (Stopfbuchse, Lippendichtung) verschlissen ist -> erneuern
2. Der Ruderschaft im Dichtungsbereich beschaedigt/korrodiert ist -> Schaft im Bereich polieren oder erneuern
3. Das Koker-Rohr selbst undicht ist (GFK-Anbindung an Rumpf gerissen) -> GFK-Reparatur erforderlich
4. Die Dichtung falsch eingestellt ist (zu locker) -> nachstellen

**Prioritaet:** Koker-Undichtigkeit ist kein Notfall (Boot sinkt nicht sofort), aber muss zeitnah behoben werden, da dauerhafter Wassereinbruch zu Korrosion und Schimmel fuehrt.
**AYDI-Bewertung Confidence:** visual_high

### Frage 18: Kann ich meine Steueranlage selbst warten?

**Antwort:** Einfache Wartungsarbeiten koennen von technisch versierten Eignern selbst durchgefuehrt werden:
- Seilspannung pruefen und nachstellen
- Umlenkrollen schmieren (Teflonoel oder Silikonfett)
- Pedestal-Getriebe nachschmieren (alle 2 Jahre, Hersteller-Fett)
- Kette reinigen und fetten (Kettenfett oder Teflonfett)
- Hydraulikfluid-Stand pruefen und nachfuellen

**Professionell ausfuehren lassen:**
- Seilwechsel (korrekte Konfektionierung der Presshuelsen)
- Ruderlager-Wechsel (Boot muss raus, korrekte Passung)
- Hydraulik-Reparatur (Entlueftung, Dichtungswechsel)
- Ruderschaft-Pruefung (Ultraschall)
**AYDI-Bewertung Confidence:** documented

### Frage 19: Was ist Weather Helm und warum beeinflusst es meine Steueranlage?

**Antwort:** Weather Helm (Luvgierigkeit) ist die Tendenz eines Segelboots, zum Wind zu drehen. Sie erzeugt eine permanente Ruderlast: Der Steuermann muss staendig nach Lee gegenhalten. 3–5 Grad Ruderwinkel sind normal und erstrebenswert (Sicherheitsfunktion). Ueber 8 Grad wird die Dauerbelastung fuer Seile, Lager und Autopilot kritisch und reduziert die Lebensdauer aller Steuerungskomponenten erheblich (Faktor 2–3 kuerzere Lebensdauer bei 10+ Grad).
**AYDI-Bewertung Confidence:** calculated

### Frage 20: Welchen Ruderschaftdurchmesser braucht mein Boot?

**Antwort:** Faustregel nach Bootlaenge (Segelyacht, Edelstahl 316L):
- 7 m: 25 mm
- 9 m: 30 mm
- 11 m: 35 mm
- 13 m: 40 mm
- 15 m: 50 mm
- 18 m: 60 mm
- 22 m: 75 mm
- 28 m: 90 mm

Diese Werte sind Richtwerte. Die exakte Berechnung haengt ab von Ruderfläche, Geschwindigkeit, Balancegrad und CE-Kategorie. Ein Fachbetrieb oder die AYDI-Analyse kann dies praezise berechnen.
**AYDI-Bewertung Confidence:** estimated (Faustregel), measured (berechnet)

### Frage 21: Wie funktioniert ein Doppelsteuerstand auf einer Segelyacht?

**Antwort:** Zwei Steuerraeder (Backbord/Steuerbord) sind mechanisch synchronisiert:
- **Mechanisch:** Durchgehende Welle oder Synchronseil verbindet beide Pedestals. Beide Raeder drehen immer synchron.
- **Hydraulisch:** Beide Helm-Pumpen arbeiten auf denselben Zylinder. Wenn ein Rad gedreht wird, dreht das andere passiv mit.
Vorteile: Bessere Sicht nach Luv (Steuermann sitzt auf der Hohen Seite), Redundanz.
**AYDI-Bewertung Confidence:** measured

### Frage 22: Was passiert, wenn meine Hydraulikleitung platzt?

**Antwort:** Totaler Steuerverlust. Das Steuerrad dreht sich widerstandslos, das Ruder wird von der Stroemung bewegt. Sofortmassnahmen:
1. Notsteuerung (Notpinne) aktivieren
2. Segel bergen / Maschine auf Leerlauf
3. Leckstelle identifizieren und wenn moeglich provisorisch abdichten
4. Seenotsignal vorbereiten, wenn keine Kontrolle wiederhergestellt werden kann

**Praevention:** Leitungen regelmaessig auf Korrosion/Schamfil pruefen, Schlaeuche alle 7–10 Jahre praeventiv ersetzen, Kupferleitungen auf Vibrationsrisse pruefen.
**AYDI-Bewertung Confidence:** measured

### Frage 23: Welches Steuerseil — 1x19 oder 7x19?

**Antwort:**
- **1×19 (Monolitzenseil):** 19 Einzeldraehte in einer Schicht. Steifer, geringere Dehnung, hoehere Bruchlast pro Querschnitt. Standard fuer Steuerseile.
- **7×19 (Drahtseil):** 7 Litzen a 19 Draehte. Flexibler, kann ueber kleinere Rollen gefuehrt werden, aber hoehere Dehnung.

**Empfehlung:** 1×19 ist Standard fuer Steueranlagen. 7×19 nur verwenden, wenn sehr enge Umlenkradien unvermeidlich sind (Biegeradius < 12× Seil-Dm).
**AYDI-Bewertung Confidence:** measured

### Frage 24: Kann ich die Ruderbegrenzung (Endanschlaege) verstellen?

**Antwort:** Ja, die meisten Steueranlagen haben einstellbare mechanische Endanschlaege am Quadranten oder Zylinder. Der maximale Ruderausschlag betraegt typisch 35 Grad je Seite (70 Grad gesamt). Weniger als 30 Grad reduziert die Manövrierbarkeit, mehr als 40 Grad bringt keinen Vorteil (Stroemungsabriss) und erhoeht die Belastung der Steueranlage.

**Achtung:** Endanschlaege nie ohne Abstimmung mit Autopilot-Einstellungen veraendern! Der Autopilot muss die neuen Endanschlaege kennen (Ruderkalibrierung).
**AYDI-Bewertung Confidence:** documented

### Frage 25: Mein Segelboot hat leichten Lee-Helm. Ist die Steueranlage schuld?

**Antwort:** Nein, Lee-Helm ist kein Steueranlagen-Problem, sondern ein Segelplan-/Trimm-Problem. Der Schwerpunkt der Segelflaeche (CE) liegt zu weit vorne relativ zum Lateralpunkt (CLR). Moegliche Massnahmen:
- Mastfall vergroessern (Mast weiter nach achtern)
- Grosssegel trimmen (Achterlik oeffnen)
- Weniger Vorsegel (kleinere Fock)
- Gewichtsverteilung prüfen (zu viel Gewicht im Bug?)
- In schweren Faellen: Segelplan aendern (Rigger konsultieren)

Lee-Helm ist sicherheitskritisch: Bei einer Boe luvt das Boot nicht selbstaendig an, sondern wird weiter abgedreht. Dringend korrigieren!
**AYDI-Bewertung Confidence:** measured (Segelphysik)

### Frage 26: Wie gross sollte der Quadrant fuer mein Boot sein?

**Antwort:** Die Quadrantengroesse wird durch Ruderschaftdurchmesser und erforderlichen Hebelarm bestimmt:
- Schaftdurchmesser 25–30 mm: Quadrant 200 mm Radius
- Schaftdurchmesser 30–35 mm: Quadrant 250 mm Radius
- Schaftdurchmesser 35–40 mm: Quadrant 300 mm Radius
- Schaftdurchmesser 40–50 mm: Quadrant 350 mm Radius
- Schaftdurchmesser 50–55 mm: Quadrant 400 mm Radius
- Schaftdurchmesser 55–70 mm: Quadrant 450 mm Radius

Groesserer Quadrant = geringere Seilkraft, aber mehr Platzbedarf und groesserer Seilweg.
**AYDI-Bewertung Confidence:** measured

### Frage 27: Was ist der Unterschied zwischen Follow-Up (FU) und Non-Follow-Up (NFU) Hydraulik?

**Antwort:** 
- **Follow-Up (FU):** Die Helm-Pumpe hat einen integrierten Feedback-Mechanismus. Der Steuermann spuert den Ruderdruck proportional am Steuerrad. Standard fuer Hauptsteuerung auf Segelyachten.
- **Non-Follow-Up (NFU):** Fester Pumpenhub pro Radumdrehung, kein Feedback der Ruderlast. Das Rad dreht sich immer gleich leicht/schwer, unabhaengig von der tatsaechlichen Ruderlast. Verwendet fuer Autopilot-Betrieb und einfache Motorboot-Steuerungen.

FU ist komfortabler und sicherer, NFU ist einfacher und guenstiger.
**AYDI-Bewertung Confidence:** measured

### Frage 28: Wie stelle ich fest, ob mein Ruderblatt beschaedigt ist?

**Antwort:** Anzeichen fuer Ruderblattschaeden:
1. **Visuell (bei herausgenommenem Boot):** Risse, Delaminierung, Blasenbildung, fehlende Beschichtung
2. **Im Wasser:** Ungewoehnliche Vibrationen beim Steuern (Flattern), Kurs laeuft weg trotz korrekter Steueranlage
3. **Klopftest:** Auf das Ruderblatt klopfen — matter Klang deutet auf Wassereinbruch/Delaminierung hin
4. **Feuchtesensor:** Professionelle Feuchtemessung bei Verdacht auf Wassereinbruch

Ruderblattschaeden sind NICHT Gegenstand der Steueranlagen-Bewertung im engeren Sinn, werden aber als Einflussfaktor im Strukturmodul bewertet.
**AYDI-Bewertung Confidence:** visual_medium

### Frage 29: Kann ich einen Autopilot an jede Steueranlage anschliessen?

**Antwort:** Grundsaetzlich ja, aber die Integrationsmethode variiert:
- **Pinne:** Pinnenpilot (Linearantrieb an der Pinne). Einfach, aber begrenzte Leistung (bis ca. 10 m).
- **Seilsteuerung:** Linearantrieb am Quadrant oder Radantrieb am Steuerrad. Mittlere Komplexitaet.
- **Hydraulik:** Elektrohydraulische Pumpe parallel zur Helm-Pumpe. Eleganteste Loesung, beste Performance.
- **Fly-by-Wire:** Software-Integration, keine zusaetzliche Hardware. Einfachste Integration.

Wichtig: Rudersensor (Winkelgeber) muss immer am Ruderschaft montiert werden, nicht an der Steuerung (Spiel!).
**AYDI-Bewertung Confidence:** documented

### Frage 30: Was bedeutet "mechanischer Vorteil" bei Steueranlagen?

**Antwort:** Der mechanische Vorteil (Mechanical Advantage, MA) beschreibt, um welchen Faktor die eingebrachte Handkraft am Steuerrad verstaerkt wird. Er ergibt sich aus dem Zusammenspiel von:
1. **Radradius vs. Kettenradradius** (typisch 8:1 bis 15:1)
2. **Getriebe-Untersetzung** (wenn vorhanden, typisch 2:1 bis 6:1)
3. **Quadrantenradius** (je groesser, desto geringere Seilkraft noetig)

Gesamt-MA von 30:1 bis 100:1 sind typisch. Hoeherer MA = leichtere Steuerung, aber mehr Radumdrehungen fuer gleichen Ruderausschlag.
**AYDI-Bewertung Confidence:** calculated

### Frage 31: Warum hat mein Boot manchmal ploetzlich starke Ruderkraefte?

**Antwort:** Ploetzliche Steuerkraft-Spitzen koennen folgende Ursachen haben:
1. **Boe trifft:** Windkraft erhoeht schlagartig, Luvgierigkeit steigt sprunghaft
2. **Welle trifft Ruder seitlich:** Querkraft auf Ruderblatt
3. **Stroemungsabriss und Wiederanlegen:** Bei grossen Ruderwinkeln (>25 Grad) kann die Stroemung abreissen und beim Zurueckdrehen schlagartig wieder anlegen
4. **Propellereffekt:** Bei Motorfahrt erzeugt der Propeller einen asymmetrischen Wasserstrom am Ruder
5. **Ruderflattern:** Resonanzschwingung des Ruderblatts bei bestimmten Geschwindigkeiten — ein Zeichen fuer Lagerspiel (STEER-F06)

**AYDI-Bewertung Confidence:** calculated

### Frage 32: Welche Lebensdauer hat eine typische Steueranlage?

**Antwort:** Bei korrekter Wartung:
- **Seilsteuerung (Seile):** 5–7 Jahre (praeventiv), bis 10 Jahre moeglich
- **Seilsteuerung (Kette, Rollen, Quadrant):** 15–25 Jahre
- **Pedestal-Getriebe:** 15–25 Jahre
- **Ruderlager (Gleitlager):** 8–15 Jahre
- **Ruderlager (Kugellager, Jefa):** 15–25 Jahre
- **Hydraulikzylinder:** 15–20 Jahre (Dichtungen: 5–8 Jahre)
- **Hydraulikpumpe:** 15–20 Jahre
- **Hydraulikleitungen (Kupfer):** 20–30 Jahre
- **Hydraulikschlaeuche:** 7–10 Jahre
- **Ruderschaft (316L):** 25–40 Jahre (wenn Opferanoden gewartet)

**AYDI-Bewertung Confidence:** benchmark

### Frage 33: Mein Steuerrad hat "Einrastpunkte" — ist das normal?

**Antwort:** Nein. Ein Steuerrad sollte sich ueber den gesamten Bereich gleichmaessig drehen. "Einrastpunkte" (fuhlbare Raststellung) deuten auf:
1. Beschaedigte oder verschlissene Zahnraeder im Getriebe (STEER-F05)
2. Korrodierte Stellen im Kettenrad/Ketten-System
3. Verformte Umlenkrollen
4. Kinkung im Steuerseil (STEER-F02)
5. Fehlende Schmierung an einer bestimmten Stelle

**Massnahme:** Sofortige Inspektion, da Einrastpunkte die Praezision der Steuerung beeintraechtigen und auf fortschreitenden Verschleiss hinweisen.
**AYDI-Bewertung Confidence:** visual_medium

### Frage 34: Wie viel kostet eine komplette Steueranlage?

**Antwort:** Richtwerte fuer komplette Systeme inkl. Einbau:

| Bootgroesse | Pinne | Seilsteuerung | Hydraulik |
|-------------|-------|--------------|-----------|
| 7 m Segel | 200–500 EUR | 1500–2500 EUR | — |
| 10 m Segel | 300–800 EUR | 2500–4000 EUR | 3500–5500 EUR |
| 13 m Segel | — | 3500–6000 EUR | 5000–8000 EUR |
| 16 m Segel | — | — | 7000–12000 EUR |
| 20 m Segel | — | — | 12000–20000 EUR |
| 10 m Motor | — | — | 2000–4000 EUR |
| 15 m Motor | — | — | 5000–10000 EUR |
| 20 m Motor | — | — | 10000–25000 EUR |

Fly-by-Wire fuer Motoryachten ab 15 m: 15000–50000+ EUR.
**AYDI-Bewertung Confidence:** benchmark

### Frage 35: Was muss ich beim Kauf einer Gebrauchtyacht bezueglich der Steueranlage pruefen?

**Antwort:** Checkliste fuer Gebrauchtyacht-Kaeufer:
1. **Totgang pruefen:** Steuerrad drehen — mehr als 5 Grad Leerlauf? Problem!
2. **Steuerkraft pruefen:** Muss ungewoehnlich viel Kraft aufgewendet werden?
3. **Geraeusche:** Quietschen, Klicken, Klopfen beim Steuern?
4. **Hydraulik:** Oelflecken unter Zylinder/Leitungen? Fluid-Stand im Reservoir?
5. **Seil visuell:** Sichtbare Litzenbrueche oder Korrosion?
6. **Ruderlager:** Am Ruderblatt wackeln (bei Boot aus dem Wasser)
7. **Koker:** Wasser im Achterschiff/Ruderkasten?
8. **Notpinne:** Vorhanden und passend?
9. **Alter der Komponenten:** Letzte Wartung/Erneuerung dokumentiert?
10. **Autopilot-Test:** Steuert der Autopilot ruhig oder pendelt er?

Eine professionelle Begutachtung durch einen Gutachter ist bei Booten ueber 10 m immer empfehlenswert.
**AYDI-Bewertung Confidence:** documented

---

## 10. Glossar

### A

**Aktuator (Actuator):** Antriebselement, das Energie (hydraulisch, elektrisch) in Bewegung umsetzt. Im Steuerungskontext: der Zylinder oder Motor, der den Ruderschaft dreht.

**Anstellwinkel (Angle of Attack):** Winkel zwischen Ruderblatt-Nulllage und Anstroemrichtung. Bestimmt die Ruderkraft.

### B

**Balancegrad (Balance Ratio):** Anteil der Ruderblattflaeche vor der Ruderschaftachse. Beeinflusst das Ruderschaftmoment. Typisch 0.10–0.30.

**Bypass-Ventil (Bypass Valve):** Ventil in der Hydraulikleitung, das bei Oeffnung die freie Ruderbewegung ermoeglicht (z.B. fuer Autopilot oder Notbetrieb).

**Bowdenzug (Push-Pull Cable):** Flexibles Uebertragungselement mit starrem Innenzug, der sowohl Zug- als auch Druckkraefte uebertragen kann.

### C

**Capstan-Effekt:** Kraftverstaerkung durch Seilreibung auf einer zylindrischen Trommel. Grundprinzip aller Seilwinschen.

**CE-Kategorie (Design Category):** EU-Klassifikation fuer Sportboote (A/B/C/D) gemaess Richtlinie 2013/53/EU. Bestimmt Anforderungen an Steueranlage und Notsteuerung.

**CLR (Centre of Lateral Resistance):** Lateralpunkt — Drehpunkt des Unterwasserschiffs. Bestimmt zusammen mit CE die Helmbalance.

**CE (Centre of Effort):** Druckpunkt des Segelplans. Die geometrische Position, an der die Windkraft auf die Segel zusammengefasst werden kann.

### D

**Drehkolben (Rotary Vane Actuator):** Hydraulischer Aktuator, der Druck direkt in Drehbewegung umsetzt (ohne Linearzylinder). Kompakt, wenig Verschleissteile.

**Doppelsteuerstand (Dual Helm):** Zwei Steuerraeder (oder ein Rad + eine Pinne), die synchron arbeiten und die Steuerung von zwei Positionen aus ermoeglichen.

**Drag Link:** Verbindungsstange zwischen Zahnstange/Zylinder und Ruderhebel.

### E

**Endanschlag (Rudder Stop):** Mechanische Begrenzung des maximalen Ruderausschlags. Schuetzt Steueranlage und Ruder vor Ueberlastung.

**Entlueftung (Bleeding):** Verfahren zum Entfernen von Luft aus einem Hydrauliksystem. Kritisch fuer korrekte Funktion.

### F

**Feedback (Ruderfeedback):** Die taktile Rueckmeldung der Ruderkraefte an den Steuermann. Wichtig fuer praezises Steuern und Erkennung von Veraenderungen.

**Fly-by-Wire:** Elektronische Steuersignaluebertragung ohne mechanische Verbindung zwischen Steuerrad und Ruder.

**Follow-Up (FU):** Hydraulik-Steuerungsmodus, bei dem der Steuermann proportionales Feedback der Ruderlast erhaelt.

### G

**Getriebe (Gearbox):** Mechanisches Untersetzungselement im Pedestal (z.B. Whitlock Cobra/Mamba). Multipliziert die Steuerkraft.

### H

**Helm-Pumpe (Helm Pump):** Handbetriebene Hydraulikpumpe, typisch im Pedestal oder an der Konsole montiert.

**Helmbalance (Helm Balance):** Gleichgewicht zwischen Segeldruck und Lateralwiderstand. Bestimmt die Dauer-Steuerlast.

### K

**Kettenrad (Sprocket):** Zahnrad, das die Kette im Pedestal fuehrt. Verbindet Steuerradwelle mit Seilsystem.

**Kinkung:** Bleibender Knick in einem Drahtseil. Seil ist nicht mehr einsetzbar und muss sofort ersetzt werden.

**Koker (Rudder Tube):** Rohrdurchfuehrung des Ruderschafts durch den Rumpf. Muss abgedichtet sein.

### L

**Lead:** Abstand zwischen CE (Segeldruck) und CLR (Lateralpunkt). Bestimmt Luvgierigkeit. Positiver Lead = Luvgierigkeit.

**Leegierigkeit (Lee Helm):** Tendenz des Bootes, vom Wind abzudrehen. Unerstrebenswert und sicherheitskritisch.

**Lippendichtung (Lip Seal):** Dichtung am Koker mit elastischer Lippe, die den Ruderschaft umschliesst.

**Litzenbruch (Wire Break):** Bruch einzelner Draehte in einem Steuerseil. Erster Litzenbruch = sofortiger Austausch des Seils.

**Luvgierigkeit (Weather Helm):** Tendenz des Bootes, zum Wind zu drehen. Leicht erstrebenswert (3–5 Grad) als Sicherheitsmechanismus.

### M

**Mechanischer Vorteil (Mechanical Advantage):** Verhaeltnis von Abtriebskraft zu Eingangskraft in einem mechanischen System.

### N

**NFU (Non-Follow-Up):** Hydraulik-Steuerungsmodus ohne proportionales Feedback. Fester Pumpenhub pro Radumdrehung.

**Notpinne (Emergency Tiller):** Steckpinne fuer den Notfall, die direkt auf den Ruderschaftkopf gesteckt wird. Pflicht bei CE Kat A/B.

**Notsteuerung (Emergency Steering):** Alternative Steuerungsmoeglichkeit bei Ausfall der Hauptsteuerung.

### O

**Opferanode (Sacrificial Anode):** Zinkanode am Ruder oder Schaft, die durch galvanische Korrosion den Ruderschaft schuetzt.

### P

**Pedestal (Steuerstandsaeule):** Saeule, die das Steuerrad traegt und die mechanische Uebertragung (Kette, Getriebe) beherbergt.

**Proportionalpumpe (Variable Displacement Pump):** Helm-Pumpe mit einstellbarer Foerdermenge pro Umdrehung.

### Q

**Quadrant:** Halbkreisfoermiger Hebel am Ruderschaft, der das Steuerseil fuehrt. Standard-Anbindung bei Seilsteuerungen.

### R

**Radialspiel (Radial Play):** Seitliches Spiel des Ruderschafts im Ruderlager. Mass fuer den Lagerverschleiss.

**Ruderhebel (Tiller Arm):** Gerader Hebel am Ruderschaft als Alternative zum Quadrant.

**Ruderkoker:** Siehe Koker.

**Rudermoment (Steering Torque):** Drehmoment um die Ruderschaftachse, das die Steueranlage ueberwinden muss.

### S

**Spatenruder (Spade Rudder):** Freihaengendes Ruder ohne Skeg-Stuetzung. Standard bei modernen Segelyachten.

**Spannschloss (Turnbuckle):** Vorrichtung zum Spannen des Steuerseils. Muss gesichert werden (Splint, Draht).

**Steering Ratio (Steuerungsverhaeltnis):** Radumdrehungen pro Grad Ruderausschlag. Niedrig = direkt, hoch = indirekt.

**Steer-by-Wire:** Elektronische Steuersignaluebertragung. Synonym fuer Fly-by-Wire im Marinebereich.

**Stroemungsabriss (Stall):** Abloesen der Stroemung vom Ruderblatt bei zu grossem Anstellwinkel. Ruderwirkung bricht dramatisch ein.

**Synchronisation:** Gleichlauf zweier Steuerraeder oder Ruder (Doppelruder, Doppelsteuerstand).

### T

**Tiller (Pinne):** Direkter Steuerhebel am Ruderkopf. Einfachste Form der Steuerung.

**Totgang (Backlash/Play):** Leerer Weg am Steuerrad, in dem sich das Ruder nicht bewegt. Soll < 5 Grad sein.

### U

**Umlenkrolle (Sheave/Turning Block):** Rolle, die das Steuerseil um eine Ecke fuehrt. Kugelgelagerte Ausfuehrung bevorzugt.

**Untersetzung (Gear Ratio):** Verhaeltnis von Eingangs- zu Ausgangsdrehzahl. Hoehere Untersetzung = mehr Kraft, weniger Geschwindigkeit.

### V

**Verdraengung (Displacement):** Verdraenung eines Schiffes, bestimmt Groesse und Kraeft auf Ruderblatt.

### W

**Weather Helm:** Siehe Luvgierigkeit.

### W (Forts.)

**Wirkungsgrad (Efficiency):** Verhaeltnis von Nutzleistung zu eingebrachter Leistung in einer Steueranlage. Typisch 70–95 % je nach Typ und Zustand. Niedrigerer Wirkungsgrad bedeutet hoehere Steuerkraefte und weniger Ruderfeedback.

### Z

**Zahnstange (Rack):** Lineares Zahnelement, das mit einem Ritzel (Zahnrad) zusammenwirkt. Verwendet in Rack-and-Pinion-Steuerungen fuer kleinere Boote.

**Zylinder (Cylinder):** Hydraulischer Linearantrieb, der Druck in eine geradlinige Bewegung umwandelt. Einfach- oder doppeltwirkend. Verbindet ueber Ruderhebel mit dem Ruderschaft.

**Zweikreis-Hydraulik (Dual Circuit Hydraulics):** System mit zwei unabhaengigen Hydraulikkreisen fuer maximale Redundanz. Vorgeschrieben auf gewerblichen Yachten und Superyachten ab bestimmter Groesse. Beide Kreise koennen das Ruder unabhaengig voneinander ansteuern.

### Fachbegriffe Englisch-Deutsch Schnellreferenz

| Englisch | Deutsch |
|----------|---------|
| Autopilot | Selbststeueranlage |
| Bearing | Lager |
| Cable steering | Seilsteuerung |
| Centre of effort (CE) | Segelschwerpunkt |
| Centre of lateral resistance (CLR) | Lateralpunkt |
| Chain | Kette |
| Cylinder | Zylinder |
| Emergency steering | Notsteuerung |
| Emergency tiller | Notpinne |
| Feedback | Rueckmeldung |
| Follow-up (FU) | Mitfuehrend |
| Fly-by-wire | Elektronische Steuersignaluebertragung |
| Gear ratio | Untersetzungsverhaeltnis |
| Helm | Steuerstand |
| Helm pump | Steuerpumpe |
| Hydraulic fluid | Hydraulikfluessigkeit |
| Lee helm | Leegierigkeit |
| Mechanical advantage | Mechanischer Vorteil |
| Pedestal | Steuerstandsaeule |
| Quadrant | Quadrant |
| Rack and pinion | Zahnstange und Ritzel |
| Rudder | Ruder(blatt) |
| Rudder shaft / stock | Ruderschaft / Ruderkoenig |
| Rudder tube | Ruderkoker |
| Sheave | Umlenkrolle |
| Sprocket | Kettenrad |
| Stall (rudder) | Stroemungsabriss |
| Steering ratio | Steuerungsverhaeltnis |
| Tiller | Pinne |
| Tiller arm | Ruderhebel |
| Torque | Drehmoment |
| Weather helm | Luvgierigkeit |
| Wheel | Steuerrad |
| Wire | Drahtseil / Steuerseil |

---

## 11. Schnell-Referenz

### 11.1 Steuerungstyp nach Bootgroesse (Schnellauswahl)

```
+----+------+------+------+------+------+------+------+------+
|Boot| 5-7m | 7-9m | 9-12 |12-15 |15-20 |20-25 |25-35 | >35  |
+----+------+------+------+------+------+------+------+------+
|Seg.| Pin  |Pin/  | Seil | Seil/| Hydr | Hydr | Hydr | Hydr |
|    |      |Seil  |      | Hydr |      |      | /FbW | /FbW |
+----+------+------+------+------+------+------+------+------+
|Mot.| Kab  | Kab  | Kab/ | Hydr | Hydr | Hydr | Hydr | FbW  |
|    |      |      | Hydr |      |      | /FbW | /FbW |      |
+----+------+------+------+------+------+------+------+------+

Pin = Pinne, Seil = Seil/Kette, Kab = Kabelsteuerung
Hydr = Hydraulik, FbW = Fly-by-Wire
```

### 11.2 Ruderschaftdurchmesser-Schnellreferenz

```
Bootlaenge [m]:  7   9  11  13  15  18  22  28  35
Schaft [mm]:    25  30  35  40  50  60  75  90 100
Jefa Lager:     25  30  35  40  50  60  70  90 100
```

### 11.3 Steuerseil-Schnellreferenz

```
Bootlaenge [m]:    <8    8-11  11-14  14-18  18-24
Seil-Dm [mm]:       3      4      5      6      7
Kette:           3/16"  3/16"  1/4"   1/4"  5/16"
Quadrant [mm]:    200    250    300    350    400
```

### 11.4 Hydraulik-Schnellreferenz

```
Bootlaenge [m]:   10-13  13-16  16-20  20-26  26-35
Pumpe [cm3/U]:      12     18     28     40     60
Zylinder-Hub:      150    200    250    350    450
Max. Moment [Nm]:  400    800   1400   2500   4500
```

### 11.5 Wartungsintervalle

```
Massnahme                           Intervall
-----------                         ---------
Seilspannung pruefen                3 Monate
Umlenkrollen schmieren              6 Monate
Kette schmieren                     6 Monate
Seil auf Litzenbruch pruefen        6 Monate
Hydraulik-Fluedstand pruefen        3 Monate
Pedestal-Getriebe schmieren         12 Monate
Ruderlager-Spiel pruefen            12 Monate
Koker-Dichtung pruefen              12 Monate
Steuerseil erneuern (praeventiv)    5-7 Jahre
Hydraulikfluid wechseln             2-3 Jahre
Hydraulikschlaeuche erneuern        7-10 Jahre
```

---

## 12. ANHANG A–R

### ANHANG A — Fallstudie: Seilsteuerung Bavaria 42 Ocean (BJ 2005)

**Ausgangslage:**
- Boot: Bavaria 42 Ocean, Bj. 2005, LOA 12.99 m
- Steuerung: Whitlock Cobra 18 Getriebe, Doppelrad, Seil 4 mm
- Problem: Zunehmender Totgang, schwergaengig bei Manoevrieren

**Untersuchung:**
1. Seilspannung: Auslenkung 25 mm (Soll: 10–15 mm) -> zu locker (STEER-F01)
2. Spannschloss: Am Anschlag, nicht mehr nachstellbar
3. Visuell: Zwei Litzenbrueche im Bereich Umlenkrolle Steuerbord (STEER-F02)
4. Umlenkrollen: Steuerbord achtern schwergaengig (STEER-F04)
5. Quadrant: Leichtes Spiel, aber im Toleranzbereich
6. Ruderlager: Kein messbares Spiel -> OK

**Massnahmen:**
1. Steuerseil komplett erneuert: 5 mm (Upgrade von 4 mm, korrekt fuer 12 m)
2. Umlenkrolle Steuerbord achtern erneuert (kugelgelagert)
3. Alle anderen Rollen geschmiert und auf Leichtlauf geprueft
4. Kette und Kettenrad inspiziert: Verschleiss minimal -> weiterverwendet
5. Seilspannung korrekt eingestellt

**Kosten:**
- Seil 5 mm, 14 m: 85 EUR
- Presshuelsen (4 Stk): 24 EUR
- Umlenkrolle kugelgelagert: 58 EUR
- Arbeitszeit (4 Stunden): 320 EUR
- **Gesamt: 487 EUR**

**Lehre fuer AYDI:**
- Bavaria 42 Bj. 2003–2008 hat systematisch zu duennes Seil ab Werk (4 mm statt 5 mm)
- Confidence: documented (Werkstatt-Erfahrung mit > 20 Booten dieser Serie)
- Seilalter > 5 Jahre bei 4 mm: AYDI-Score-Malus -15

### ANHANG B — Fallstudie: Hydraulik-Umruestung Hallberg-Rassy 43 (BJ 2001)

**Ausgangslage:**
- Boot: Hallberg-Rassy 43, Bj. 2001, LOA 13.10 m
- Steuerung: Original Whitlock Mamba 18 Seilsteuerung, Einfachrad
- Problem: Steuerkraefte bei Starkwind zu hoch, Autopilot-Performance schlecht

**Dimensionierung (Hydraulik):**
```
Ruderblatt: A = 0.55 m^2, Chord = 0.44 m, Balancegrad 0.18
V_max = 9 kn = 4.63 m/s
F_ruder = 0.5 * 1025 * 4.63^2 * 0.55 * 1.10 = 6685 N
M_schaft = 6685 * (0.26 - 0.18) * 0.44 = 6685 * 0.035 = 234 Nm
M_auslegung = 234 * 2.0 (CE Kat A) = 468 Nm
```

**Gewahlte Komponenten:**
- Lecomble & Schmitt HP 150 Helm-Pumpe (15 cm^3/Umdr., 100 bar)
- Lecomble & Schmitt RV 500 Drehkolben-Aktuator (500 Nm max)
- Kupferleitung 8 mm, ca. 6 m
- Lecomble & Schmitt AP Drive 60 (fuer Raymarine EV-200)

**Kosten:**
- Material (L&S Kit Sail 200): 2400 EUR
- Kupferleitungen + Fittings: 280 EUR
- Autopilot-Antrieb (AP Drive 60): 1200 EUR
- Arbeitszeit (18 Stunden): 1800 EUR
- **Gesamt: 5680 EUR**

**Ergebnis:** Steuerkraft reduziert von ca. 60 N auf ca. 18 N. Autopilot-Stromverbrauch um 30% gesunken.

**Lehre fuer AYDI:**
- HR 43 mit Originalsteuerung: Ergonomie-Score typisch 55–65 (zu hohe Steuerkraefte)
- Nach Hydraulik-Umbau: Ergonomie-Score 85–92
- Confidence: calculated + documented

### ANHANG C — Fallstudie: Ruderlager-Schaden Beneteau Oceanis 393 (BJ 2006)

**Ausgangslage:**
- Boot: Beneteau Oceanis 393, Bj. 2006, LOA 11.89 m
- Steuerung: Seilsteuerung mit Whitlock Cobra 14
- Problem: Klopfgeraeusche achtern bei Seegang, Wasser im Achterschiff

**Untersuchung:**
1. Ruderblatt-Spiel: 3 mm radial (Soll max. 1.5 mm) -> STEER-F06
2. Koker: Wasser tropft permanent -> STEER-F11
3. Ruderschaft: Oberflaechliche Korrosion im Lagerbereich -> STEER-F09 (leicht)
4. Gleitlagerbuchse: Vollstaendig verschlissen, Schaft laeuft auf Koker-Rohr

**Massnahmen:**
1. Boot gekrant, Ruder ausgebaut
2. Ruderschaft im Lagerbereich poliert (kein Materialverlust, nur Oberflaechenkorrosion)
3. Neue Gleitlagerbuchse (Jefa Standard 35) eingebaut
4. Koker-Dichtung erneuert (Jefa Lippendichtung 35 mm)
5. Opferanode am Ruder erneuert

**Kosten:**
- Jefa Ruderlager Standard 35: 380 EUR
- Jefa Koker-Dichtung 35: 58 EUR
- Opferanode: 25 EUR
- Kran (2x): 400 EUR
- Arbeitszeit (12 Stunden): 1200 EUR
- **Gesamt: 2063 EUR**

**Lehre fuer AYDI:**
- Beneteau Oceanis 390/393: Bekanntes Problem mit zu kleinem Original-Lager
- Upgrade von 30 mm auf 35 mm Lager empfohlen bei Gelegenheit
- Confidence: documented

### ANHANG D — Fallstudie: Doppelruder-Synchronisation Jeanneau Sun Odyssey 440 (BJ 2019)

**Ausgangslage:**
- Boot: Jeanneau Sun Odyssey 440, Bj. 2019, LOA 13.39 m
- Steuerung: Doppelruder, Doppelrad, Seilsteuerung mit Jefa Twin Rudder Kit
- Problem: Ungleichmaessiger Ruderausschlag, Boot zieht leicht nach Backbord

**Untersuchung:**
1. Synchronseil zwischen beiden Quadranten: 2 mm Laengung -> ungleicher Ruderwinkel
2. Steuerbord-Ruder: +1.5 Grad mehr Ausschlag als Backbord
3. Alle Lager und Dichtungen: OK (Boot erst 5 Jahre alt)
4. Quadranten-Klemmung: Fest, kein Spiel

**Massnahmen:**
1. Synchronseil erneuert und korrekt gespannt
2. Beide Ruder auf gleichen Ausschlag kalibriert (Winkelmessung mit Neigungsmesser)
3. Endanschlaege synchronisiert

**Kosten:**
- Synchronseil: 45 EUR
- Arbeitszeit (3 Stunden): 300 EUR
- **Gesamt: 345 EUR**

**Lehre fuer AYDI:**
- Doppelruder-Synchronisation: Pruefroutine alle 12 Monate empfohlen
- 1 Grad Differenz = akzeptabel. > 2 Grad: AYDI-Score-Malus -15
- Confidence: measured

### ANHANG E — Fallstudie: Fly-by-Wire Installation Princess V65 (BJ 2022)

**Ausgangslage:**
- Boot: Princess V65, Bj. 2022, LOA 20.42 m
- Steuerung: ZF SteerCommand Fly-by-Wire
- Problem: Intermittierender Steuerverlust (Fehlermeldung auf MFD)

**Untersuchung:**
1. Fehlerspeicher: CAN-Bus Kommunikationsfehler zwischen Helm-ECU und Aktuator
2. Kabelpruefung: Korrosion an Steckerverbindung im Maschinenraum
3. System-Update: Firmware veraltet (V2.1, aktuell V3.4)

**Massnahmen:**
1. Steckerverbindung gereinigt und mit Kontaktfett versehen
2. Stecker durch vergoldete Marinestecker ersetzt
3. Firmware auf V3.4 aktualisiert
4. CAN-Bus-Terminierung ueberpreuft

**Kosten:**
- Steckerersatz (4 Stk): 120 EUR
- Kontaktfett: 15 EUR
- Firmware-Update (Haendler): 350 EUR
- Arbeitszeit (6 Stunden): 900 EUR
- **Gesamt: 1385 EUR**

**Lehre fuer AYDI:**
- Fly-by-Wire: CAN-Bus-Verbindungen als Schwachstelle identifizieren
- Vibrationsumgebung Maschinenraum: Stecker grundsaetzlich als Risikopunkt bewerten
- Confidence: documented

### ANHANG F — Fallstudie: Notsteuerung Ovni 445 (Aluminium-Expeditionsyacht)

**Ausgangslage:**
- Boot: Ovni 445, Bj. 2012, LOA 13.50 m, Aluminium, CE Kat A
- Steuerung: Hydraulik (Lecomble & Schmitt HP 200 + RV 500)
- Situation: Nordatlantik-Ueberquerung, Hydraulikleitung gebrochen (Vibrations-Ermuedungsriss)

**Ablauf:**
1. Sofortiger Steuerverlust, Steuerrad drehte widerstandslos
2. Crew aktivierte Notpinne in 3 Minuten (regelmaessig geuebt!)
3. Notpinne: 900 mm Edelstahl, Sechskant-Aufnahme am Ruderschaftkopf
4. Steuerung mit Notpinne fuer 48 Stunden bis zum naechsten Hafen

**Reparatur:**
1. Gebrochene Kupferleitung durch Edelstahlrohr 10 mm ersetzt
2. Flexible Verbindungsstuecke an Motorraum-Uebergaengen installiert
3. Alle Kupferleitungen auf Vibrationsrisse geprueft (keine weiteren Schaeden)

**Kosten:**
- Edelstahlrohr + Fittings: 180 EUR
- Flexible Schlauchabschnitte (2 Stk): 120 EUR
- Arbeitszeit (8 Stunden): 640 EUR
- **Gesamt: 940 EUR**

**Lehre fuer AYDI:**
- Kupferleitungen in Maschinenraumnaehe: Ermuedungsrisiko durch Vibration
- Notsteuerung rettet Leben — regelmaessige Uebung unverzichtbar
- AYDI-Pruefpunkt: Notpinne vorhanden + zugaenglich = Pflicht fuer CE Kat A/B
- Confidence: documented

### ANHANG G — Fallstudie: Korrosion Ruderschaft Dehler 38 (BJ 1998)

**Ausgangslage:**
- Boot: Dehler 38, Bj. 1998, LOA 11.50 m
- Steuerung: Seilsteuerung, Whitlock Cobra 14
- Problem: Bei Routine-Winterlager Ruderblatt "wackelt" stark

**Untersuchung:**
1. Radialspiel: 4 mm (Soll max. 1.5 mm) -> STEER-F06 (CRITICAL)
2. Ruderschaft ausgebaut: Starke Spaltkorrosion im Bereich oberes Lager
3. Ultraschall-Dickenmessung: Materialverlust 25 % am Ruderschaft im Lagerbereich (STEER-F09, CRITICAL)
4. Ursache: Opferanoden seit Jahren nicht erneuert, Edelstahl 304 (!) statt 316L

**Massnahmen:**
1. Neuer Ruderschaft aus Edelstahl 316L, 35 mm (Upgrade von 30 mm)
2. Neues Jefa Kugellager 35 (Upgrade von Original-Gleitlager)
3. Neue Koker-Dichtung
4. Zinkanode am Ruder installiert
5. Galvanischer Trennschutz (isolierende Buchse)

**Kosten:**
- Neuer Ruderschaft (316L, gefraest): 1800 EUR
- Jefa Kugellager 35: 660 EUR
- Koker-Dichtung: 58 EUR
- Zinkanode: 35 EUR
- Kran (2x): 400 EUR
- Arbeitszeit (20 Stunden): 2000 EUR
- **Gesamt: 4953 EUR**

**Lehre fuer AYDI:**
- Dehler 34/38 Bj. 1995–2002: Bekanntes Edelstahl-304-Problem bei einigen Serien
- Material-Check (304 vs. 316L) als AYDI-Pruefpunkt fuer Boote dieser Aera
- Opferanoden: Jaehrliche Pruefung als zwingender Wartungspunkt
- Confidence: documented

### ANHANG H — Fallstudie: Autopilot-Integration Oyster 575 (BJ 2015)

**Ausgangslage:**
- Boot: Oyster 575, Bj. 2015, LOA 17.40 m
- Steuerung: Jefa Hydraulik Kit 50, Doppelrad
- Problem: Autopilot (B&G Pilot Hydraulic) kaempft gegen Steuerung, hoher Stromverbrauch

**Untersuchung:**
1. Autopilot-Paramenter: Gain zu hoch, Counter-Rudder zu aggressiv
2. Rudersensor: 3 Grad Offset (falsch kalibriert nach Service)
3. Hydraulik-Bypass-Ventil: Leicht undicht (Autopilot verliert Ruderdruck)
4. Helmbalance: 8 Grad Luvgierigkeit bei 15 kn Wind -> Dauerlast auf Autopilot

**Massnahmen:**
1. Rudersensor neu kalibriert
2. Autopilot-Parameter optimiert (Gain von 8 auf 5, Response "Economy")
3. Bypass-Ventil-Dichtung erneuert
4. Segelberater: Grosssegel-Trimm optimiert, Luvgierigkeit auf 5 Grad reduziert

**Kosten:**
- Bypass-Ventil Dichtung: 35 EUR
- Autopilot-Kalibrierung (Techniker): 350 EUR
- Segelberatung: 200 EUR
- Arbeitszeit (5 Stunden): 500 EUR
- **Gesamt: 1085 EUR**

**Ergebnis:** Autopilot-Stromverbrauch von 7 A auf 3.5 A reduziert (halbiert!). Kurssteuerung deutlich ruhiger.

**Lehre fuer AYDI:**
- Autopilot-Performance haengt zu > 50 % von der Steueranlage und Helmbalance ab
- Byass-Ventil-Zustand als Autopilot-Performance-Faktor erkennen
- Confidence: documented

### ANHANG H2 — Installationshinweise fuer Steueranlagen

#### Grundregeln fuer die Installation von Seilsteuerungen

1. **Seilverlegung:** Steuerseile muessen in moeglichst gerader Linie zwischen Pedestal und Quadrant verlegt werden. Jede Umlenkung reduziert den Wirkungsgrad und erhoet den Verschleiss.

2. **Mindestbiegeradius:** Der Biegeradius an Umlenkrollen muss mindestens dem 12-fachen des Seildurchmessers entsprechen (z.B. 5 mm Seil: min. 60 mm Rollendurchmesser).

3. **Seilspannung:** Nach der Erstinstallation setzt sich das Seil innerhalb der ersten 50 Betriebsstunden. Seilspannung nach dieser Einlaufphase nochmals pruefen und nachstellen.

4. **Fuehrungsrohre:** Wenn Seile durch Fuehrungsrohre laufen (z.B. unter dem Cockpitboden), muessen die Rohre weit genug sein (min. 3× Seildurchmesser ID) und duerfen keine scharfen Knicke haben. Innendurchmesser und Biegeradien direkt mit Hersteller abstimmen.

5. **Seil-Enden:** Seilenden muessen mit Presshuelsen (Nicopress) oder Spleisskauschen befestigt werden. NIEMALS Seilklemmen (Buegel-Klemmen) fuer Steuerseile verwenden — Sicherheitsrisiko!

6. **Spannvorrichtung:** Immer ein Spannschloss (Turnbuckle) oder aehnliche Spannvorrichtung vorsehen. Gegensicherung durch Splint oder Kontermutter.

7. **Kettenubergang:** Die Kette muss exakt auf das Kettenrad passen (Teilung pruefen). Kette und Kettenrad immer vom gleichen Hersteller.

#### Grundregeln fuer die Installation von Hydrauliksteuerungen

1. **Leitungsfuehrung:** Leitungen so kurz wie moeglich. Jeder zusaetzliche Meter erhoet das Fluid-Volumen und vergroessert den Totgang.

2. **Entlueftungspunkte:** Entlueftungsventile an den hoechsten Punkten des Systems installieren.

3. **Leitungsbefestigung:** Alle 300–500 mm mit gepolsterten Schellen befestigen. Kein direkter Kontakt Metall auf Metall (Scheuerstelle!).

4. **Flexibilitaet:** An vibrationsfuehrenden Stellen (Motor, Ruder) flexible Schlauchabschnitte verwenden, nie starre Leitungen.

5. **Berstscheibe / Druckentlastung:** Bei geschlossenen Systemen Ueberdruckventil vorsehen (Thermische Ausdehnung bei Sonneneinstrahlung!).

6. **Fluid-Befuellung:** System von der tiefsten Stelle befuellen, um Luftblasen nach oben zu druecken. Mehrfach entlueften.

7. **Dokumentation:** Schema der Leitungsfuehrung an Bord aufbewahren (fuer Reparatur und Notfaelle).

---

### ANHANG I — Uebersicht Fehlerbild-Codes (Schnellreferenz)

| Code | Bezeichnung | Schwere | Visuell erkennbar |
|------|------------|---------|-------------------|
| STEER-F01 | Steuerseildehnung | 3 | Mittel |
| STEER-F02 | Seil-Litzenbruch | 4–5 | Hoch |
| STEER-F03 | Quadranten-Lockerung | 4 | Mittel |
| STEER-F04 | Umlenkrollen-Verschleiss | 3 | Hoch |
| STEER-F05 | Pedestal-Getriebe-Verschleiss | 3–4 | Niedrig |
| STEER-F06 | Ruderlager-Verschleiss | 4 | Mittel |
| STEER-F07 | Hydraulikleckage | 3–5 | Hoch |
| STEER-F08 | Luft in Hydrauliksystem | 3–4 | Niedrig |
| STEER-F09 | Ruderschaft-Korrosion | 4–5 | Mittel |
| STEER-F10 | Autopilot-Steuerungskonflikt | 3 | Niedrig |
| STEER-F11 | Koker-Undichtigkeit | 3–4 | Hoch |
| STEER-F12 | Steuerrad-Nabe lose | 3–4 | Hoch |

---

### ANHANG J — Materialkompatibilitaet Ruderschaft

| Schaft-Material | Lager-Material | Koker-Material | Galv. Risiko | Empfehlung |
|----------------|---------------|---------------|-------------|------------|
| Edelstahl 316L | PTFE-Buchse | GFK | Gering | Standard |
| Edelstahl 316L | Bronze-Buchse | GFK | Mittel | Opferanode erforderlich |
| Edelstahl 316L | Jefa Kugellager | GFK | Gering | Premium |
| Edelstahl 304 | PTFE-Buchse | GFK | Hoch(!) | Schaft-Upgrade auf 316L |
| Bronze | Bronze-Buchse | Bronze/GFK | Gering | Traditionelle Methode |
| Carbon/Titan | Keramik/PEEK | GFK/Carbon | Minimal | Superyacht/Rennyacht |

---

### ANHANG K — Hydraulikfluid-Verträglichkeitsmatrix

| Hersteller | Spezifiziertes Fluid | Alternative | NICHT kompatibel |
|------------|---------------------|------------|-----------------|
| Lewmar | Lewmar Hydraulic Oil | Total LHM+ | DOT Bremsfluessigkeit |
| Lecomble & Schmitt | Total Fluide LDS | Dexron ATF (lt. Hersteller) | DOT, Silikonoel |
| SeaStar/Teleflex | SeaStar HA5430 | Dexron III ATF | DOT, Pflanzenoel |
| Kobelt | SAE 10W Hydraulikoel | MIL-H-5606 | ATF, DOT |
| Jefa (Hydraulik) | ISO VG 15 Hydraulikoel | Total Azolla ZS 15 | DOT, Silikonoel |

**AYDI-Pruefpunkt:** Falsches Hydraulikfluid = Befundschwere SIGNIFICANT bis CRITICAL

---

### ANHANG L — Werkzeugliste fuer Steueranlagen-Wartung

| Werkzeug | Einsatz | Erforderlich fuer |
|----------|---------|-------------------|
| Neigungsmesser / Winkelmesser | Ruderausschlag messen | Kalibrierung, Synchronisation |
| Messuhr (0.01 mm) | Ruderlager-Spiel messen | Lagerpruefung |
| Drehmomentschluessel | Quadrant, Radnabe | Montage |
| Seilschneider | Steuerseile | Seilwechsel |
| Presszange | Seilklemmen/Presshuelsen | Seilwechsel |
| Entlueftungsschluessel | Hydraulik-Entlueftung | Hydraulik-Wartung |
| Auffangbehaelter | Hydraulikfluid auffangen | Hydraulik-Wartung |
| Spritze (Fluid-Nachfuellen) | Reservoir befuellen | Hydraulik-Wartung |
| Multimeter | Elektrische Pruefung | Autopilot, Fly-by-Wire |
| Ultraschall-Dickenmesser | Schaft-Wandstaerke | Korrosionspruefung |

---

### ANHANG M — Saisonale Wartungscheckliste

**Fruehjahrsinbetriebnahme:**
- [ ] Seilspannung pruefen und einstellen
- [ ] Ruderlager-Spiel pruefen (vor dem Kranen, Ruder zugaenglich)
- [ ] Koker-Dichtung auf Leckage pruefen
- [ ] Hydraulik: Fluid-Stand pruefen
- [ ] Alle Umlenkrollen auf Leichtlauf pruefen
- [ ] Notpinne lokalisieren und Passung testen
- [ ] Endanschlaege pruefen (voller Ruderausschlag moeglich?)
- [ ] Steuerrad auf festen Sitz pruefen

**Herbst-Winterlager:**
- [ ] Steuerseile komplett inspizieren (Handschuhtest)
- [ ] Kette reinigen und fetten
- [ ] Pedestal-Getriebe nachschmieren
- [ ] Umlenkrollen schmieren
- [ ] Hydraulikfluid: Farbe/Klarheit pruefen (trueb = Wechsel!)
- [ ] Opferanoden am Ruder pruefen
- [ ] Ruderbeschichtung pruefen
- [ ] Koker-Bereich auf Korrosion inspizieren

---

### ANHANG N — AYDI Score-Gewichtung Steueranlage

| Pruefpunkt | Max. Score | Gewichtung |
|------------|-----------|------------|
| Dimensionierung korrekt | 100 | 20 % |
| Zustand mechanisch | 100 | 25 % |
| Zustand Ruderlager | 100 | 15 % |
| Compliance (Normen) | 100 | 15 % |
| Notsteuerung vorhanden | 100 | 10 % |
| Feedback-Qualitaet | 100 | 5 % |
| Autopilot-Kompatibilitaet | 100 | 5 % |
| Wartungszustand | 100 | 5 % |
| **Gesamt** | **100** | **100 %** |

---

### ANHANG O — Haeufige Hersteller-spezifische Probleme

| Hersteller/Modell | Bekanntes Problem | Betroffene Jahre | AYDI-Code |
|-------------------|-------------------|-------------------|-----------|
| Whitlock Cobra 14 | Getriebe-Spiel nach 8–10 Jahren | Alle | STEER-F05 |
| Edson 335 Pedestal | Kettenrad-Verschleiss bei Chromkette | Vor 2010 | STEER-F05 |
| Bavaria (diverse) | Zu duenres Steuerseil ab Werk | 2000–2010 | STEER-F01 |
| Beneteau Oceanis 393 | Zu kleines Ruderlager | 2004–2008 | STEER-F06 |
| Dehler 34/38 | Edelstahl 304 Ruderschaft | 1995–2002 | STEER-F09 |
| SeaStar BayStar | Helm-Pumpen-Dichtung Ausfall | 2015–2018 | STEER-F07 |
| Jeanneau SO 440 | Synchronseil-Laengung Doppelruder | 2018–2021 | STEER-F01 |
| Lecomble & Schmitt RV 250 | O-Ring-Alterung (NBR) | Vor 2014 | STEER-F07 |

---

### ANHANG P — Normen-Querverweismatrix

| AYDI-Pruefpunkt | ISO 8847 | ISO 10592 | ABYC P-21 | CE-Richtlinie |
|----------------|----------|----------|-----------|---------------|
| Seilbruchlast | 6× BL | — | — | 2013/53/EU |
| Berstdruck Hydraulik | — | 4× AP | 4× AP | 2013/53/EU |
| Steuerkraft max. | — | 28 daN | 30 lbs | — |
| Notsteuerung | Ja (Kat A/B) | Ja (Kat A/B) | Empf. | Kat A/B Pflicht |
| Korrosionsschutz | 500h SST | 500h SST | — | — |
| Temperaturbereich | -10/+65 | -10/+65 | -18/+60 | — |
| Dynamische Pruefung | 100k Zyklen | 200k Zyklen | — | — |

---

### ANHANG Q — Berechnungsformeln Zusammenfassung

```python
"""
Steering System Formulas — Quick Reference
"""

# Ruderkraft [N]
def rudder_force(rho: float, v: float, a_rudder: float, c_n: float) -> float:
    """Hydrodynamische Ruderkraft."""
    return 0.5 * rho * v**2 * a_rudder * c_n

# Rudermoment [Nm]
def rudder_torque(f_rudder: float, x_cp: float, x_shaft: float) -> float:
    """Ruderschaftmoment."""
    return f_rudder * (x_cp - x_shaft)

# Steuerkraft am Rad [N]
def helm_force(torque: float, r_wheel: float, gear_ratio: float, r_quadrant: float) -> float:
    """Erforderliche Handkraft am Steuerrad."""
    ma_wheel = r_wheel / 0.035  # Annahme 70mm Kettenrad
    return torque / (ma_wheel * gear_ratio * r_quadrant)

# Balancegrad [-]
def balance_ratio(a_forward: float, a_total: float) -> float:
    """Ruder-Balancegrad."""
    return a_forward / a_total

# Hydraulik-Zylinderkraft [N]
def hydraulic_cylinder_force(pump_force: float, a_cyl: float, a_pump: float) -> float:
    """Hydraulische Kraftuebersetzung."""
    return pump_force * (a_cyl / a_pump)

# Gesamteffizienz [-]
def steering_efficiency(eta_bearing: float, eta_transmission: float,
                        eta_sheave: float, n_sheaves: int) -> float:
    """Gesamtwirkungsgrad der Steueranlage."""
    return eta_bearing * eta_transmission * (eta_sheave ** n_sheaves)
```

---

### ANHANG R — Pydantic v2 Modelle

Datenmodelle fuer die Steueranlagen-Analyse im AYDI-System. Alle Modelle verwenden Pydantic v2 mit `model_config = {"from_attributes": True}`.

```python
"""
AYDI Steering System Analysis Models — Pydantic v2
Wissensdatei: 14.01 Steueranlagen Grundlagen
"""

from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class SteeringType(str, Enum):
    """Steuerungstyp."""
    TILLER = "tiller"
    CABLE_CHAIN = "cable_chain"
    RACK_AND_PINION = "rack_and_pinion"
    HYDRAULIC = "hydraulic"
    ELECTRIC = "electric"
    FLY_BY_WIRE = "fly_by_wire"
    PUSH_PULL_CABLE = "push_pull_cable"


class RudderType(str, Enum):
    """Ruderblatt-Typ."""
    LONG_KEEL = "long_keel"
    SKEG_HUNG = "skeg_hung"
    SPADE = "spade"
    TWIN_SPADE = "twin_spade"
    TRANSOM_HUNG = "transom_hung"
    OUTBOARD_MOTOR = "outboard_motor"


class SteeringManufacturer(str, Enum):
    """Hersteller der Steueranlage."""
    JEFA = "jefa"
    WHITLOCK = "whitlock"
    LEWMAR = "lewmar"
    EDSON = "edson"
    KOBELT = "kobelt"
    LECOMBLE_SCHMITT = "lecomble_schmitt"
    SEASTAR = "seastar"
    ZF_MARINE = "zf_marine"
    ULTRAFLEX = "ultraflex"
    OTHER = "other"
    UNKNOWN = "unknown"


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
    F01_CABLE_STRETCH = "STEER-F01"
    F02_WIRE_BREAK = "STEER-F02"
    F03_QUADRANT_LOOSE = "STEER-F03"
    F04_SHEAVE_WEAR = "STEER-F04"
    F05_PEDESTAL_GEAR_WEAR = "STEER-F05"
    F06_RUDDER_BEARING_WEAR = "STEER-F06"
    F07_HYDRAULIC_LEAK = "STEER-F07"
    F08_HYDRAULIC_AIR = "STEER-F08"
    F09_SHAFT_CORROSION = "STEER-F09"
    F10_AUTOPILOT_CONFLICT = "STEER-F10"
    F11_TUBE_SEAL_LEAK = "STEER-F11"
    F12_WHEEL_HUB_LOOSE = "STEER-F12"


class HelmBalanceRating(str, Enum):
    """Helmbalance-Bewertung."""
    IDEAL = "ideal"
    ACCEPTABLE = "acceptable"
    PROBLEMATIC = "problematic"
    CRITICAL_LEE_HELM = "critical_lee_helm"


class SteeringSpec(BaseModel):
    """Spezifikation einer Steueranlage."""

    model_config = {"from_attributes": True}

    boat_name: Optional[str] = Field(None, description="Bootsname oder -kennung")
    boat_length_m: float = Field(..., ge=2.0, le=100.0, description="Bootlaenge in Metern")
    boat_displacement_kg: Optional[float] = Field(None, ge=100, description="Verdraengung in kg")
    boat_type: str = Field(..., description="Segelyacht, Motorboot, etc.")
    ce_category: Optional[str] = Field(None, pattern="^[A-D]$", description="CE-Kategorie A/B/C/D")

    steering_type: SteeringType = Field(..., description="Steuerungstyp")
    manufacturer: SteeringManufacturer = Field(default=SteeringManufacturer.UNKNOWN)
    model_name: Optional[str] = Field(None, description="Modellbezeichnung der Steueranlage")

    rudder_type: RudderType = Field(..., description="Ruderblatt-Typ")
    rudder_area_m2: Optional[float] = Field(None, ge=0.01, le=10.0, description="Ruderblattflaeche in m^2")
    rudder_chord_m: Optional[float] = Field(None, ge=0.05, le=2.0, description="Ruderblatttiefe in m")
    rudder_balance_ratio: Optional[float] = Field(None, ge=0.0, le=0.5, description="Balancegrad")
    shaft_diameter_mm: Optional[float] = Field(None, ge=10, le=200, description="Ruderschaftdurchmesser in mm")
    shaft_material: Optional[str] = Field(None, description="Schaftmaterial, z.B. 316L, 304, Bronze")
    twin_rudder: bool = Field(default=False, description="Doppelruder ja/nein")

    wheel_diameter_mm: Optional[float] = Field(None, ge=200, le=2000, description="Raddurchmesser in mm")
    dual_helm: bool = Field(default=False, description="Doppelsteuerstand ja/nein")
    gear_model: Optional[str] = Field(None, description="Getriebemodell, z.B. Whitlock Mamba 18")
    gear_ratio: Optional[float] = Field(None, ge=1.0, le=10.0, description="Getriebeuntersetzung")

    cable_diameter_mm: Optional[float] = Field(None, ge=2, le=10, description="Steuerseildurchmesser in mm")
    quadrant_radius_mm: Optional[float] = Field(None, ge=100, le=600, description="Quadrantenradius in mm")
    n_sheaves: Optional[int] = Field(None, ge=0, le=12, description="Anzahl Umlenkrollen")

    hydraulic_pump_displacement_cm3: Optional[float] = Field(None, description="Pumpenverdr. in cm^3/Umdr.")
    hydraulic_max_pressure_bar: Optional[float] = Field(None, description="Max. Systemdruck in bar")
    hydraulic_cylinder_stroke_mm: Optional[float] = Field(None, description="Zylinderhub in mm")

    emergency_tiller: bool = Field(default=False, description="Notpinne vorhanden")
    autopilot_integrated: bool = Field(default=False, description="Autopilot-Integration")
    autopilot_model: Optional[str] = Field(None, description="Autopilot-Modell")


class SteeringCondition(BaseModel):
    """Zustandsbewertung einer Steueranlage."""

    model_config = {"from_attributes": True}

    inspection_date: date = Field(..., description="Datum der Inspektion")
    inspector: Optional[str] = Field(None, description="Name des Inspektors")

    overall_score: int = Field(..., ge=0, le=100, description="Gesamtscore 0-100")
    dimensioning_score: int = Field(..., ge=0, le=100, description="Dimensionierung korrekt")
    mechanical_score: int = Field(..., ge=0, le=100, description="Mechanischer Zustand")
    bearing_score: int = Field(..., ge=0, le=100, description="Ruderlager-Zustand")
    compliance_score: int = Field(..., ge=0, le=100, description="Normenkonformitaet")
    emergency_score: int = Field(..., ge=0, le=100, description="Notsteuerung")
    feedback_score: int = Field(..., ge=0, le=100, description="Feedback-Qualitaet")
    autopilot_score: int = Field(..., ge=0, le=100, description="Autopilot-Kompatibilitaet")
    maintenance_score: int = Field(..., ge=0, le=100, description="Wartungszustand")

    confidence: ConfidenceLevel = Field(..., description="Konfidenz-Stufe")
    notes: Optional[str] = Field(None, description="Freitextbemerkungen")


class SteeringFinding(BaseModel):
    """Einzelbefund an einer Steueranlage."""

    model_config = {"from_attributes": True}

    finding_id: str = Field(..., description="Eindeutige Befund-ID")
    failure_code: FailurePatternCode = Field(..., description="Fehlerbild-Code")
    severity: SeverityLevel = Field(..., description="Schweregrad 1-5")
    confidence: ConfidenceLevel = Field(..., description="Konfidenz der Erkennung")
    location: str = Field(..., description="Ort am Boot, z.B. 'Umlenkrolle Steuerbord achtern'")
    description_de: str = Field(..., description="Beschreibung auf Deutsch")
    suggestion_de: str = Field(..., description="Handlungsempfehlung auf Deutsch")
    score_impact: int = Field(..., ge=-100, le=0, description="Score-Auswirkung (negativ)")
    photo_reference: Optional[str] = Field(None, description="Referenz auf Foto/Bild")
    requires_professional: bool = Field(default=False, description="Fachbetrieb erforderlich?")


class SteeringTorqueCalculation(BaseModel):
    """Berechnetes Rudermoment."""

    model_config = {"from_attributes": True}

    boat_speed_kn: float = Field(..., ge=0, le=50, description="Geschwindigkeit in Knoten")
    water_density_kg_m3: float = Field(default=1025.0, description="Wasserdichte")
    rudder_area_m2: float = Field(..., ge=0.01, description="Ruderblattflaeche in m^2")
    c_n: float = Field(..., ge=0, le=2.0, description="Normalkraftbeiwert")
    rudder_chord_m: float = Field(..., ge=0.05, description="Ruderblatttiefe")
    balance_ratio: float = Field(..., ge=0.0, le=0.5, description="Balancegrad")
    cp_position_ratio: float = Field(default=0.25, description="Druckpunkt-Position (Anteil Chord)")
    safety_factor: float = Field(default=1.75, ge=1.0, le=3.0, description="Sicherheitsfaktor")

    # Berechnete Ergebnisse
    rudder_force_n: Optional[float] = Field(None, description="Berechnete Ruderkraft in N")
    shaft_torque_nm: Optional[float] = Field(None, description="Berechnetes Rudermoment in Nm")
    design_torque_nm: Optional[float] = Field(None, description="Auslegungsmoment inkl. SF in Nm")
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.CALCULATED)


class HelmBalanceAssessment(BaseModel):
    """Bewertung der Helmbalance."""

    model_config = {"from_attributes": True}

    weather_helm_deg: Optional[float] = Field(None, description="Gemessene Luvgierigkeit in Grad")
    rating: HelmBalanceRating = Field(..., description="Bewertung")
    score: int = Field(..., ge=0, le=100, description="Score 0-100")
    continuous_load_percent: Optional[float] = Field(None, description="Dauer-Rudermoment in % des Max.")
    autopilot_impact: Optional[str] = Field(None, description="Auswirkung auf Autopilot")
    suggestion_de: Optional[str] = Field(None, description="Empfehlung auf Deutsch")
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.ESTIMATED)


class SteeringAnalysisResult(BaseModel):
    """Gesamtergebnis der Steueranlagen-Analyse."""

    model_config = {"from_attributes": True}

    spec: SteeringSpec = Field(..., description="Spezifikation der Steueranlage")
    condition: SteeringCondition = Field(..., description="Zustandsbewertung")
    torque_calc: Optional[SteeringTorqueCalculation] = Field(None, description="Moment-Berechnung")
    helm_balance: Optional[HelmBalanceAssessment] = Field(None, description="Helmbalance-Bewertung")
    findings: list[SteeringFinding] = Field(default_factory=list, description="Liste der Befunde")
    critical_findings: int = Field(default=0, ge=0, description="Anzahl kritischer Befunde")
    overall_score: int = Field(..., ge=0, le=100, description="Gesamtscore")
    overall_confidence: ConfidenceLevel = Field(..., description="Gesamt-Konfidenz")
    analysis_version: str = Field(default="1.0.0", description="Version des Analyse-Algorithmus")
    analysis_date: date = Field(..., description="Analysedatum")
    summary_de: str = Field(..., description="Zusammenfassung auf Deutsch")


class SteeringMaintenanceSchedule(BaseModel):
    """Wartungsplan fuer eine Steueranlage."""

    model_config = {"from_attributes": True}

    steering_type: SteeringType = Field(..., description="Steuerungstyp")
    boat_length_m: float = Field(..., description="Bootlaenge")
    tasks: list[dict] = Field(
        ...,
        description="Liste der Wartungsaufgaben mit 'task', 'interval_months', 'professional_required'"
    )
    next_service_date: Optional[date] = Field(None, description="Naechster Service-Termin")
    estimated_annual_cost_eur: Optional[float] = Field(None, description="Geschaetzte jaehrliche Kosten")
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.BENCHMARK)
```

---

---

### ANHANG R2 — Visuelle Analyse-Leitfaden fuer AYDI Pipeline B

Folgende Merkmale koennen durch visuelle Analyse (Fotos) erkannt werden:

| Merkmal | Confidence | Erkennungsmethode |
|---------|-----------|-------------------|
| Steuerungstyp (Pinne/Rad) | visual_high | Direktes Erkennen |
| Hersteller Steuerrad | visual_medium | Logo, Bauform |
| Doppelsteuerstand | visual_high | Zwei Raeder sichtbar |
| Seilsteuerung (Quadrant sichtbar) | visual_medium | Quadrant im Achterbereich |
| Hydraulikzylinder sichtbar | visual_medium | Zylinder am Ruderschaft |
| Notpinne vorhanden | visual_medium | Pinne am Ruderschaftkopf oder in Halterung |
| Koker-Undichtigkeit | visual_high | Wasserflecken, Korrosion |
| Seil-Litzenbrueche | visual_high | Abstehende Draehte sichtbar |
| Hydraulikleckage | visual_high | Oelflecken, Verfaerbungen |
| Umlenkrollen-Zustand | visual_medium | Korrosion, Schraeglauf |
| Ruderblatt-Zustand (UW-Foto) | visual_medium | Risse, Delaminierung, Bewuchs |
| Steuerrad-Material/Zustand | visual_high | Teak-Verwitterung, Korrosion |
| Pedestal-Zustand | visual_medium | Korrosion, Beschaedigung |
| Notpinnen-Zugaenglichkeit | visual_low | Lager-/Verstauposition |

**Prompt-Hinweise fuer Claude Vision (Pipeline B):**
- Steueranlage immer im Kontext des Gesamtboots bewerten
- Alter des Bootes aus Gesamteindruck schaetzen
- Wartungszustand aus Korrosion/Verschmutzung ableiten
- Bei Unterdeck-Fotos: Seilspannung aus Durchhang visuell schaetzen
- Hydraulikleitungen: Farbveraenderung des Fluids als Indikator (klar = gut, trueb/dunkel = alt)

---

*Ende der Wissensdatei 14.01 — Steueranlagen Grundlagen und Typen*
*AYDI Research, Version 1.0.0, Stand: 2026-04-26*
