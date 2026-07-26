# 20.02 — Hydraulische Steuerung (Hydraulikzylinder, Pumpen, Leitungen, Dimensionierung, Wartung)

> **Dokumentversion:** 2.0
> **Letzte Aktualisierung:** 2026-05-02
> **Autor:** AYDI Knowledge Engineering
> **Geltungsbereich:** Hydraulische Steueranlagen auf Yachten 8–60 m (Ruderanlagen, Autopilot-Integration, Notsteuerung, Zweikreis-Systeme)
> **Sprache Fachtext:** Deutsch | **Code:** Englisch
> **Maßeinheiten:** mm, bar, cm³, l/min, Nm, kN, °C, EUR, Scores 0–100

---

## Inhaltsverzeichnis

1. [Einfuehrung und Uebersicht](#1-einfuehrung-und-uebersicht)
2. [Grundlagen und Theorie](#2-grundlagen-und-theorie)
3. [Typenuebersicht](#3-typenuebersicht)
4. [Produktlinien und Spezifikationen](#4-produktlinien-und-spezifikationen)
5. [Hersteller-Datenbank](#5-hersteller-datenbank)
6. [Fehlerbild-Atlas](#6-fehlerbild-atlas)
7. [Troubleshooting-Entscheidungsbaeume](#7-troubleshooting-entscheidungsbaeume)
8. [FAQ](#8-faq)
9. [Glossar](#9-glossar)
10. [Schnell-Referenz](#10-schnell-referenz)
11. [ANHANG A–H: Fallstudien](#11-anhang-a-h-fallstudien)
12. [ANHANG I–R: Pydantic v2 Modelle](#12-anhang-i-r-pydantic-v2-modelle)

---

## 1. Einfuehrung und Uebersicht

### 1.1 Warum Hydraulische Steuerung?

Die hydraulische Steuerung ist das Rueckgrat der Manoevrierfaehigkeit auf Yachten ab ca. 12 m Laenge und/oder mit Ruderkraeften ueber 30 kN. Ab dieser Schwelle werden mechanische Seilzug- und Gestaegesysteme unpraktikabel: Die auftretenden Kraefte wuerden massive Hebeluebersetzungen, schwere Ketten oder uebermaessig dicke Seilzuege erfordern, deren Gewicht, Reibung und Platzbedarf den Nutzen bei weitem uebersteigen.

#### Vorteile der Hydraulik gegenueber anderen Systemen

| Kriterium | Mechanisch (Seilzug) | Hydraulisch | Elektromechanisch |
|-----------|----------------------|-------------|-------------------|
| Maximale Ruderkraft | ~15 kN | >200 kN | ~80 kN |
| Leitungsfuehrung | Starre Rohre/Seile, enge Radien problematisch | Flexible Schlaeuche, beliebige Routenfuehrung | Kabel, flexibel |
| Rueckmeldung am Steuer | Direkt, aber hart bei hoher Last | Progressiv, daempfend | Simuliert (Force Feedback) |
| Redundanz | Schwierig | Zweikreis-Systeme moeglich | Dual-Motor moeglich |
| Autopilot-Integration | Aufwendig | Standard (T-Stueck/Bypass) | Nativ |
| Wartungsintervall | 500–1.000 h | 200–500 h (Oelwechsel) | 1.000–2.000 h |
| Ausfallverhalten | Steif (blockiert) | Weich (Drift moeglich) | Stromlos = keine Lenkung |
| Typischer Einsatz | <12 m Segelboot | 12–60 m Segel/Motor | <18 m, moderne Motorboote |

#### Einsatzbereiche nach Bootskategorie

**Segelyachten 12–18 m:**
- Ruderkraefte typisch 8–35 kN (je nach Lateralplan, Geschwindigkeit, Seegang)
- Handpumpen-System reicht oft bis 14 m, darueber Power-Assist erforderlich
- Autopilot-Integration ueber hydraulisches T-Stueck mit Solenoidventil

**Segelyachten 18–30 m:**
- Ruderkraefte 30–120 kN
- Motorpumpe obligatorisch, Handpumpe als Notsteuerung
- Zweikreis-Systeme ab 24 m empfohlen (Klasse-Anforderung ab 24 m bei DNV-GL)
- Proportionalventile fuer feinfuehlige Steuerung bei Leichtwind

**Motoryachten 12–24 m:**
- Ruderkraefte 15–80 kN (hoehere Geschwindigkeit, aber kleinere Ruderflaeche)
- Power-Assist oder vollelektrisch-hydraulisch Standard
- Oft kombiniert mit Bugstrahlruder-Hydraulik (gemeinsames Aggregat)

**Motoryachten 24–60 m (Superyacht-Segment):**
- Ruderkraefte 50–250+ kN
- Zweikreis-Pflichtsystem mit automatischer Umschaltung
- Redundante Pumpen, Oelkuehler, automatische Entlueftung
- Integration mit Dynamic Positioning (DP), Stabilisatoren, Interceptoren

### 1.2 Sicherheitsrelevanz

Die hydraulische Steuerung ist gemaess CE-Richtlinie 2013/53/EU ein **wesentliches Sicherheitsbauteil der Kategorie I**. Ein Totalausfall der Ruderanlage fuehrt unmittelbar zum Verlust der Manoevrierfaehigkeit — ein Szenario, das unter SOLAS (Safety of Life at Sea) als Worst-Case klassifiziert wird.

#### Regulatorischer Rahmen

**CE-Richtlinie 2013/53/EU (Recreational Craft Directive):**
- Anhang I, Abschnitt 3.3: Steuersysteme muessen unter allen vorhersehbaren Betriebsbedingungen funktionsfaehig bleiben
- Anhang I, Abschnitt 5.1.3: Hydrauliksysteme muessen gegen Ueberdruck geschuetzt sein
- Redundanzanforderung Kat. A/B: Yachten >12 m LOA mit Hydrauliksteuerung benoetigen Notsteuerung

**ISO-Normen fuer Steueranlagen:**

| Norm | Titel | Kerninhalt |
|------|-------|------------|
| ISO 25197:2020 | Small craft — Electrical/electronic control systems for steering, shift and throttle | Elektronische Steuerintegration |
| ISO 8847:2021 | Small craft — Steering gear — Cable and pulley systems | Mechanische Steuerung (Referenz) |
| ISO 8848:2020 | Small craft — Remote mechanical steering systems | Mechanische Fernsteuerung (Referenz) |
| ISO 10592:2008 | Small craft — Hydraulic steering systems | **Hauptnorm Hydrauliksteuerung** |
| ISO 23411:2020 | Small craft — Steering wheels | Steuerrad-Anforderungen (Konstruktion, Pruefung) |

**ISO 10592:2008 — Kernanforderungen:**
1. Maximaler Betriebsdruck: 70 bar (Handpumpen), 140 bar (Motorpumpen)
2. Berstdruck: min. 4× Betriebsdruck
3. Ruderausschlag: min. ±35° bei Handpumpen, ±70° bei Motorpumpen
4. Steuerzeit Hart-ueber-Hart: max. 5 Sekunden (Motorpumpen bei Hoechstfahrt)
5. Dichtheit: keine sichtbare Leckage nach 10.000 Lastwechseln
6. Temperaturbereich: -10°C bis +80°C (Hydraulikoel)

**Klassifikationsgesellschaften:**

| Organisation | Regelwerk | Anforderung |
|--------------|-----------|-------------|
| DNV-GL | Rules Pt.3 Ch.13 Sec.2 | Zweikreis-Pflicht >24 m, Notsteuerung 100% aller Groessen |
| Lloyd's Register | SSC Rules Pt.10 | Automatische Zweikreis-Umschaltung ab 500 GT |
| RINA | Rules for Pleasure Yachts | Notsteuerung Pflicht ab 15 m |
| BV (Bureau Veritas) | NR 500 | Redundanz ab 24 m, Oelkuehlung ab 30 m |
| ABS | Guide for Building and Classing Motor Pleasure Yachts | Dual-Pumpen ab 24 m |

**ABYC-Standards (American Boat & Yacht Council):**

| Standard | Titel | Kerninhalt |
|----------|-------|------------|
| ABYC P-21 | Manual and Assisted Hydraulic Steering Systems | Hydraulik-Dimensionierung, Leitungsfuehrung |
| ABYC H-30 | Hydraulic Systems | Allgemeine Hydraulik-Installation |
| ABYC P-17 | Manual and Assisted Mechanical Steering Systems | Mechanische Steuerung (Referenz) |

> ✅ Aufgeloest (Audit): ABYC P-21 = "Manual and Assisted Hydraulic Steering Systems" (Steueranlage), **ABYC H-30** = "Hydraulic Systems" (allgemeine Hydraulik, korrigiert von faelschlich "H-32"), **ABYC P-17** = "Manual and Assisted Mechanical Steering Systems" (mechanische Steuerung, korrigiert von faelschlich "Hoses, Fittings and Clamps"). ABYC H-32 ist "Ventilation of Boats Using Diesel Fuel". Marine-Hydraulikschlaeuche regelt SAE J1942 (im Dokument zitiert). — Quelle: ABYC Standards List (abycinc.org/standards-list) sowie ANSI Webstore Preview-Seiten ABYC H-30-2017, P-17-2018, P-21-2017, H-32-2013.

### 1.3 Systemuebersicht — Komponenten einer Hydrauliksteuerung

```
┌─────────────────────────────────────────────────────────────────┐
│                    HYDRAULISCHE STEUERANLAGE                     │
│                                                                 │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   │
│  │ STEUERRAD│──>│  PUMPE   │──>│LEITUNGEN │──>│ ZYLINDER │   │
│  │(Eingabe) │   │(Druck-   │   │(Transport│   │(Aktor am │   │
│  │          │   │erzeuger) │   │  medium)  │   │  Ruder)  │   │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘   │
│                       │                             │           │
│                  ┌────┴────┐                   ┌────┴────┐     │
│                  │RESERVOIR│                   │ RUDER-  │     │
│                  │(Vorrats-│                   │ KOKER   │     │
│                  │behaelt.)│                   │         │     │
│                  └─────────┘                   └─────────┘     │
│                                                                 │
│  Optionale Erweiterungen:                                       │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐      │
│  │AUTOPILOT │  │POWER-    │  │ENTLUEF-  │  │OELKUEHLER│      │
│  │(Solenoid)│  │ASSIST    │  │TUNG      │  │          │      │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘      │
└─────────────────────────────────────────────────────────────────┘
```

#### Funktionsprinzip

1. **Steuerrad** wird gedreht → **Pumpenkolben** bewegt sich
2. Pumpe drueckt Hydraulikoel durch **Druckleitung** zum Zylinder
3. **Zylinderkolben** faehrt aus → Ruderhebel wird bewegt → Ruder dreht
4. Gegenueberliegende Seite: Oel wird zurueck zur Pumpe gedrueckt (geschlossener Kreislauf)
5. **Entlueftung** stellt sicher, dass keine Luftblasen im System sind (Luft = kompressibel = schwammiges Steuer)

### 1.4 AYDI-Bewertungsrahmen fuer Hydrauliksteuerungen

AYDI bewertet hydraulische Steueranlagen in folgenden Dimensionen:

| Dimension | Gewichtung | Score-Bereich | Beschreibung |
|-----------|------------|---------------|-------------|
| Dimensionierung | 25% | 0–100 | Ist das System korrekt fuer Boot und Einsatzzweck ausgelegt? |
| Zustand | 25% | 0–100 | Aktueller technischer Zustand (Leckagen, Oelqualitaet, Verschleiss) |
| Sicherheit | 20% | 0–100 | Redundanz, Notsteuerung, Ueberdruckschutz |
| Installation | 15% | 0–100 | Leitungsfuehrung, Befestigung, Zugaenglichkeit |
| Wartungszustand | 15% | 0–100 | Wartungshistorie, Oelwechselintervalle, Dichtungszustand |

**Gesamtscore:**
```
Gesamt = 0.25×Dimensionierung + 0.25×Zustand + 0.20×Sicherheit
       + 0.15×Installation + 0.15×Wartungszustand
```

**Score-Schwellenwerte:**

| Bereich | Bewertung | AYDI-Aktion |
|---------|-----------|-------------|
| 85–100 | Ausgezeichnet | Gruenes Badge, keine Massnahmen |
| 70–84 | Gut | Gruenes Badge, Optimierungsvorschlaege |
| 50–69 | Akzeptabel | Gelbes Badge, Wartungsempfehlungen |
| 30–49 | Maengel | Rotes Badge, Instandsetzung empfohlen |
| 0–29 | Kritisch | Rotes Badge + Warnung, sofortige Massnahme |

---

## 2. Grundlagen und Theorie

### 2.1 Das Pascalsche Prinzip

Die gesamte Hydraulik beruht auf dem Prinzip von Blaise Pascal (1647): **Ein Druck, der auf eine eingeschlossene Fluessigkeit ausgeuet wird, breitet sich gleichmaessig in alle Richtungen aus.**

**Mathematische Formulierung:**

```
p = F / A

wobei:
  p = Druck [Pa] = [N/m²] = [bar × 10⁵]
  F = Kraft [N]
  A = Flaeche [m²]
```

**Hydraulische Uebersetzung:**

```
F₁ / A₁ = F₂ / A₂

→ F₂ = F₁ × (A₂ / A₁)

Kraft am Zylinder = Kraft an der Pumpe × (Zylinderflaeche / Pumpenflaeche)
```

**Volumen-Gleichgewicht (inkompressible Fluessigkeit):**

```
V₁ = V₂
A₁ × s₁ = A₂ × s₂

→ s₂ = s₁ × (A₁ / A₂)

Hub am Zylinder = Hub an der Pumpe × (Pumpenflaeche / Zylinderflaeche)
```

**Konsequenz:** Kraft und Weg verhalten sich reziprok. Groessere Kraftuebersetzung bedeutet kleineren Zylinderweg pro Pumpenweg → mehr Steuerradumdrehungen fuer denselben Ruderausschlag.

### 2.2 Druckberechnung fuer Ruderanlagen

#### Ruderkraft — Grundgleichung

Die hydrodynamische Kraft auf ein Ruderblatt:

```
F_ruder = 0.5 × ρ × v² × A_ruder × Cₗ

wobei:
  ρ = Dichte Seewasser ≈ 1.025 kg/m³
  v = Anstroemgeschwindigkeit am Ruder [m/s]
  A_ruder = Ruderfläche [m²]
  Cₗ = Auftriebsbeiwert des Ruderprofils (typisch 0.8–1.4 bei 15° Ruderwinkel)
```

**Typische Ruderkraefte nach Bootskategorie:**

| Bootskategorie | LOA [m] | v_max [kn] | A_ruder [m²] | F_ruder [kN] | Drehmoment am Schaft [Nm] |
|----------------|---------|------------|--------------|-------------|---------------------------|
| Segelyacht Serienbau | 10–14 | 7–8 | 0.15–0.30 | 3–12 | 200–800 |
| Segelyacht Performance | 12–16 | 8–12 | 0.20–0.40 | 8–25 | 600–2.000 |
| Fahrtensegler | 14–20 | 7–9 | 0.25–0.50 | 10–35 | 800–3.500 |
| Motoryacht Gleiter | 10–16 | 25–35 | 0.08–0.15 | 8–30 | 400–2.000 |
| Motoryacht Verdraenger | 14–24 | 8–12 | 0.20–0.50 | 12–50 | 1.000–5.000 |
| Superyacht | 24–60 | 12–18 | 0.40–1.20 | 40–200 | 4.000–30.000 |

#### Zylinderauslegung

**Zylinderkraft:**

```
F_zylinder = p × A_kolben

wobei:
  p = Systemdruck [bar]
  A_kolben = Kolbenflaeche [cm²] = π/4 × d²
  
→ d = √(4 × F_zylinder / (π × p))
```

**Umrechnung: Ruderkraft → Zylinderkraft:**

```
F_zylinder = M_ruder / L_hebel

wobei:
  M_ruder = Drehmoment am Ruderschaft [Nm]
  L_hebel = Effektive Hebellaenge am Ruderquadranten [m]
```

**Dimensionierungsbeispiel — Segelyacht 16 m:**

```
Gegeben:
  M_ruder = 2.500 Nm (bei 8 kn, 15° Ruderwinkel, Seegang 4 Bft)
  L_hebel = 0.15 m (Ruderquadrant Radius)
  Systemdruck = 55 bar (typisch Jefa HSC-Serie)

Berechnung:
  F_zylinder = 2.500 / 0.15 = 16.667 N ≈ 16,7 kN

  A_kolben = F_zylinder / p = 16.667 / (55 × 10⁵) = 3.03 × 10⁻³ m²
           = 30,3 cm²

  d_kolben = √(4 × 30,3 / π) = √(38,6) = 6,2 cm → waehle 65 mm Kolbendurchmesser

  Tatsaechliche Kraft: 55 × 10⁵ × π/4 × 0.065² = 18.242 N = 18,2 kN
  Sicherheitsfaktor: 18,2 / 16,7 = 1,09

  ACHTUNG: Sicherheitsfaktor zu gering! ISO 10592 fordert mindestens 1,5.
  → Waehle 75 mm oder erhoehe Systemdruck auf 70 bar.
```

**Sicherheitsfaktoren nach Norm:**

| Komponente | Mindest-SF | Empfohlen | Quelle |
|-----------|-----------|-----------|--------|
| Zylinder (statisch) | 1.5 | 2.0 | ISO 10592 |
| Zylinder (dynamisch) | 2.0 | 2.5 | DNV-GL Pt.3 Ch.13 |
| Leitungen | 4.0 | 6.0 | ISO 10592 / SAE J1942 |
| Pumpengehaeuse | 2.0 | 2.5 | ISO 10592 |
| Fittings | 4.0 | 6.0 | ISO 10592 / SAE J1942 |

> ✅ Aufgeloest (Audit): Quelle korrigiert von faelschlich "ABYC H-32" (= "Ventilation of Boats Using Diesel Fuel", nicht Hydraulik) auf ISO 10592 / SAE J1942 — dieselbe Basis wie die identischen SF-Werte 4,0 / 6,0 der Zeile "Leitungen". Der einschlaegige ABYC-Standard fuer allgemeine Hydraulik waere H-30. — Quelle: ANSI Webstore Preview ABYC H-32-2013 (Diesel-Belueftung) und ABYC H-30-2017 (Hydraulic Systems).

#### Zylindervolumen und Pumpengroesse

```
V_zylinder = A_kolben × Hub

Hub = 2 × L_hebel × sin(α_max)

wobei:
  α_max = maximaler Ruderausschlag (typisch 35°)

V_gesamt = V_zylinder + V_leitungen + V_totvolumen

Pumpengroesse = V_gesamt / n_umdrehungen_hart_ueber_hart
```

**Dimensionierungstabelle — Pumpenzuordnung:**

| Ruder-Drehmoment [Nm] | Zylinderbohrung [mm] | Hub [mm] | V_zylinder [cm³] | Pumpe [cm³/Umdr.] | Umdrehungen H-u-H |
|------------------------|---------------------|----------|-------------------|--------------------|--------------------|
| 500–1.000 | 40 | 120 | 150 | 14 | 3,5 |
| 1.000–2.000 | 50 | 150 | 295 | 16 | 4,0 |
| 2.000–3.500 | 65 | 180 | 598 | 22 | 4,5 |
| 3.500–6.000 | 80 | 200 | 1.005 | 28 | 5,0 |
| 6.000–10.000 | 100 | 250 | 1.963 | 36 | 5,5 |
| 10.000–20.000 | 125 | 300 | 3.681 | 50 | 6,0 |
| 20.000–40.000 | 150 | 350 | 6.185 | 70 | 6,5 |

### 2.3 Hydraulikoel — Spezifikationen und Auswahl

#### Oeltypen nach ISO-Viskositaetsklasse

| ISO VG Klasse | Kinematische Viskositaet bei 40°C [mm²/s] | Einsatz | Typische Marken |
|---------------|-------------------------------------------|---------|-----------------|
| VG 10 | 9,0–11,0 | Leichte Handpumpen, Autopilot-Systeme | — |
| VG 15 | 13,5–16,5 | **Standard Yacht-Hydraulik (Handpumpen)** | Jefa HO-15, SeaStar HA5430 |
| VG 22 | 19,8–24,2 | Uebergangsbereich, kaeltere Reviere | Total Azolla ZS 22 |
| VG 32 | 28,8–35,2 | **Standard Yacht-Hydraulik (Motorpumpen)** | Shell Tellus S2 M 32, Mobil DTE 24 |
| VG 46 | 41,4–50,6 | Hochlast-Systeme, Superyachten, warme Reviere | Shell Tellus S2 M 46, Mobil DTE 25 |
| VG 68 | 61,2–74,8 | Schwere Industriehydraulik, selten Yacht | — |

#### Oeleigenschaften fuer Marine-Einsatz

**Anforderungen an Marine-Hydraulikoel:**

1. **Wassertoleranz**: Marine-Oele muessen min. 500 ppm Wassergehalt vertragen ohne Eigenschaftsverlust. Standard-Industrieoele versagen oft bei <200 ppm.

2. **Korrosionsschutz**: Additivierung muss 316L-Edelstahl, Bronze, verchromte Kolbenstangen und Aluminium-Gehaeuse schuetzen.

3. **Dichtungsvertraeglichkeit**: Kompatibilitaet mit NBR (Nitril-Butadien-Kautschuk), FKM (Viton), PTFE und Polyurethan-Dichtungen.

4. **Temperaturstabilitaet**: Viskositaetsindex (VI) min. 100, besser >130 fuer wechselnde Klimazonen.

5. **Schaumverhalten**: Geringes Schaumbildungspotential (ASTM D892 Seq. I: max. 100/0 ml).

6. **Luftabscheideung**: Schnelle Entlueftung (ASTM D3427: max. 5 Minuten bei 50°C).

**Oel-Wechselintervalle:**

| System | Intervall (Stunden) | Intervall (Jahre) | Kriterium |
|--------|---------------------|--------------------|-----------| 
| Handpumpe Segelyacht | — | 3–5 Jahre | Verfaerbung, Wassergehalt |
| Motorpumpe Segelyacht | 500 h | 2–3 Jahre | Was zuerst eintritt |
| Motorpumpe Motoryacht | 250–500 h | 1–2 Jahre | Was zuerst eintritt |
| Superyacht (Klasse) | 200 h | 1 Jahr | Was zuerst eintritt |
| Autopilot (geschlossen) | — | 5 Jahre | Hersteller-Empfehlung |

**Oel-Analyse — Grenzwerte:**

| Parameter | Gut | Akzeptabel | Kritisch | Methode |
|-----------|-----|------------|----------|---------|
| Wassergehalt [ppm] | <200 | 200–500 | >500 | Karl-Fischer-Titration |
| Partikelzahl (>4µm) [/ml] | <5.000 | 5.000–20.000 | >20.000 | ISO 4406 |
| Viskositaet (±% vom Neuzustand) | <5% | 5–15% | >15% | ASTM D445 |
| Saeurezahl [mg KOH/g] | <0,5 | 0,5–1,0 | >1,0 | ASTM D664 |
| Kupfergehalt [ppm] | <15 | 15–30 | >30 | ICP-OES |
| Eisengehalt [ppm] | <25 | 25–75 | >75 | ICP-OES |

### 2.4 Leitungsdimensionierung

#### Grundlagen der Leitungsberechnung

**Innendurchmesser nach Durchflussmenge:**

```
d = √(4 × Q / (π × v))

wobei:
  d = Innendurchmesser [m]
  Q = Volumenstrom [m³/s]
  v = Stroemungsgeschwindigkeit [m/s]
```

**Zulaessige Stroemungsgeschwindigkeiten:**

| Leitungstyp | v_max [m/s] | Bemerkung |
|-------------|-------------|-----------|
| Druckleitung (>50 bar) | 4,0 | Standard |
| Druckleitung (>100 bar) | 3,0 | Reduziert wegen Druckverlust |
| Ruecklaufleitung | 2,0 | Niederdruck |
| Saugleitung | 1,0 | Kavitationsgefahr! |

**Druckverlust in Leitungen (Hagen-Poiseuille fuer laminare Stroemung):**

```
Δp = (128 × η × L × Q) / (π × d⁴)

wobei:
  Δp = Druckverlust [Pa]
  η = Dynamische Viskositaet [Pa·s]
  L = Leitungslaenge [m]
  Q = Volumenstrom [m³/s]
  d = Innendurchmesser [m]
```

**Faustregel:** Druckverlust in Leitungen sollte max. 5% des Systemdrucks betragen.

#### Leitungsdimensionierungstabelle

| Pumpengroesse [cm³/Umdr.] | Max. Volumenstrom [l/min] | Druckleitung d_innen [mm] | Rueckleitung d_innen [mm] | Saugleitung d_innen [mm] |
|---------------------------|--------------------------|---------------------------|---------------------------|--------------------------|
| 10–16 | 1,5–2,5 | 6 (1/4") | 8 (5/16") | 10 (3/8") |
| 16–22 | 2,5–4,0 | 8 (5/16") | 10 (3/8") | 12 (1/2") |
| 22–36 | 4,0–8,0 | 10 (3/8") | 12 (1/2") | 16 (5/8") |
| 36–50 | 8,0–15,0 | 12 (1/2") | 16 (5/8") | 20 (3/4") |
| 50–80 | 15,0–25,0 | 16 (5/8") | 20 (3/4") | 25 (1") |

#### Materialien fuer Leitungen

**Schlauchleitungen:**

| Typ | Druck_max [bar] | Temp_max [°C] | Biegeradius | Einsatz |
|-----|-----------------|---------------|-------------|---------|
| SAE 100R7 (Thermoplast) | 210 | 100 | Eng (3× d_aussen) | Standard Yacht-Hydraulik |
| SAE 100R8 (Thermoplast HP) | 350 | 100 | Eng (3× d_aussen) | Hochdruck-Systeme |
| SAE 100R1 (1SN Drahtgeflecht) | 160–250 | 100 | Mittel (6× d_aussen) | Groessere Systeme |
| SAE 100R2 (2SN Drahtgeflecht) | 250–400 | 100 | Mittel (8× d_aussen) | Superyacht-Systeme |
| PTFE-Innenseele + Stahlgeflecht | 210 | 200 | Eng (4× d_aussen) | Maschinenraum (Hitze) |

**Rohrleitungen (Festverlegung):**

| Material | Druck_max [bar] | Einsatz | Verbindung |
|----------|-----------------|---------|------------|
| Edelstahl 316L nahtlos | 400+ | Maschinenraum, Festverlegung | Schnaeidring, Schweisstechnik |
| Kupfer-Nickel CuNi 90/10 | 200 | Alternative zu Edelstahl | Loettechnik, Schnaeidring |
| Aluminium 5083 | 150 | Gewichtsoptimiert (Racing) | Spezial-Fittings |
| Kunststoff (Nylon 12) | 100 | Segelyachten, Niederdruckseite | Steckverbinder |

### 2.5 Entlueftung — Theorie und Praxis

#### Warum Entlueftung kritisch ist

Luft in einem Hydrauliksystem ist der haeufigste Grund fuer schwammiges, unpraezises Steuergefuehl. Waehrend Hydraulikoel nahezu inkompressibel ist (Kompressionsmodul ~1.500 MPa), ist Luft ca. 20.000× leichter komprimierbar.

**Auswirkung von Lufteinschluss:**

| Luftanteil im Oel [Vol.%] | Effektive Kompressibilitaet | Steuergefuehl | Bewertung |
|----------------------------|----------------------------|---------------|-----------|
| 0 | Normal (1.500 MPa) | Praezise, direkt | Optimal |
| 0,5 | +15% kompressibler | Leicht schwammig | Akzeptabel |
| 1,0 | +30% kompressibler | Deutlich schwammig | Entlueftung noetig |
| 2,0 | +60% kompressibler | Sehr schwammig, Ruderverlust bei schnellem Lenken | Kritisch |
| 5,0 | +150% kompressibler | Kaum Ruderwirkung, Kavitationsgefahr | Gefaehrlich |

#### Entlueftungsverfahren

**Methode 1 — Schwerkraftentlueftung (Standard bei Handpumpen):**

1. Reservoir am hoechsten Punkt oeffnen
2. Entlueftungsschraube am Zylinder oeffnen (tiefster Punkt = Zylinder)
3. Oel langsam am Reservoir nachgiessen
4. Warten, bis blasenfreies Oel aus Entlueftungsschraube fliesst
5. Entlueftungsschraube schliessen
6. Steuer mehrfach von Anschlag zu Anschlag drehen
7. Schritte 3–6 wiederholen, bis Steuer sofort anspricht

**Methode 2 — Druckentlueftung (bei Motorpumpen):**

1. Druckentlueftungsadapter am Reservoir anschliessen (0,5–1,0 bar)
2. Entlueftungsschrauben sequentiell oeffnen (Pumpe → naechster Punkt → Zylinder)
3. Oel unter Druck drueckt Luft heraus
4. Schliessen, wenn blasenfrei
5. Druckentlueftung entfernen, Oelstand pruefen

**Methode 3 — Vakuumentlueftung (professionell):**

1. Vakuumpumpe an Entlueftungsschraube anschliessen
2. Oel wird durch Unterdruck angesaugt
3. Schnellste Methode, minimaler Oelverlust
4. Erforderlich bei langen Leitungswegen (>10 m)

**Methode 4 — Automatische Entlueftung (Superyacht):**

- Automatischer Entluefter im Reservoir mit Schwimmerventil
- Mikroblasen werden kontinuierlich abgeschieden
- Hersteller: Parker Hannifin, Eaton, Vetus

#### Entlueftungshaeufigkeit

| Anlass | Entlueftung erforderlich? | Methode |
|--------|--------------------------|---------|
| Erstinstallation | Ja, immer | Vakuum oder Druck empfohlen |
| Oelwechsel | Ja, immer | Schwerkraft oder Druck |
| Schlauchtausch | Ja, immer | Nach Umfang Schwerkraft/Druck |
| Zylindertausch | Ja, immer | Druck oder Vakuum |
| Saisonstart | Ja, pruefen | Schwerkraft (kurz) |
| Nach Luft im System (schwammig) | Ja, sofort | Schwerkraft |
| Oelverlust >10% nachgefuellt | Ja, immer | Schwerkraft oder Druck |

### 2.6 Thermische Auslegung

#### Waermeeintrag und -abfuhr

Jedes Hydrauliksystem erzeugt Waerme durch:
1. **Drosselungsverluste** an Ventilen und Fittings
2. **Leckagen** an Pumpe und Zylinder (interne Leckage)
3. **Reibung** in Lagern, Dichtungen, Leitungen

**Waermeberechnung:**

```
P_waerme = Q × Δp_verlust

wobei:
  P_waerme = Waermeleistung [W]
  Q = Volumenstrom [l/min] → [m³/s]
  Δp_verlust = Druckverlust im System [Pa]
```

**Kuehlung erforderlich ab:**

| System | Dauerbetrieb_max [min] | Oel-Temperatur_max [°C] | Kuehlung ab |
|--------|------------------------|--------------------------|-------------|
| Handpumpe Segelyacht | Unbegrenzt (geringe Leistung) | 50 | Nicht noetig |
| Power-Assist Segelyacht | 30 | 65 | Selten noetig |
| Motorpumpe Motoryacht | 15 (Manoever) | 70 | Bei Hafen-Manoevern |
| Superyacht-System | Dauerbetrieb | 55 (mit Kuehler) | Immer installiert |

**Kuehlverfahren:**

1. **Passive Kuehlung:** Oelreservoir mit grosser Oberflaeche, Aluminiumgehaeuse
2. **Luft-Oel-Kuehler:** Rippenkuehler mit Luefter (typisch 0,5–2 kW Kuehlleistung)
3. **Wasser-Oel-Kuehler:** Seewasser-Waermetauscher (typisch 2–10 kW, Standard bei Superyachten)
4. **Thermostatventil:** Oeffnet Kuehlerkreis ab 55–65°C, schliesst unter 45°C

### 2.7 Dynamische Belastungsanalyse

#### Lastprofile fuer Steueranlagen

**Segelyacht — Typisches Lastprofil:**

| Phase | Dauer [%] | Last [% F_max] | Beschreibung |
|-------|-----------|-----------------|-------------|
| Kurshalten | 60 | 5–15 | Kleine Korrekturen |
| Manoevrieren (Hafen) | 10 | 30–50 | Niedrige Geschwindigkeit, viel Ruder |
| Wende/Halse | 5 | 40–80 | Kurzzeitig hohe Last |
| Schwerer Seegang | 15 | 50–100 | Dauerhafte hohe Last |
| Notmanoever | <1 | 100 | Voller Ruderausschlag unter Hoechstlast |
| Leerlauf | 9 | 0 | Keine Belastung |

**Motoryacht — Typisches Lastprofil:**

| Phase | Dauer [%] | Last [% F_max] | Beschreibung |
|-------|-----------|-----------------|-------------|
| Kurshalten (Fahrt) | 50 | 10–25 | Leichte Korrekturen bei hoher Fahrt |
| Kurshalten (langsam) | 15 | 5–10 | Geringe Ruderkraft |
| Manoevrieren (Hafen) | 15 | 30–60 | Langsame Fahrt, voller Ruderausschlag |
| Ankerauf/-ab-Manoever | 5 | 20–40 | Kurz, mittlere Last |
| Schwerer Seegang | 10 | 60–100 | Hohe Lasten |
| Notmanoever | <1 | 100 | Maximale Last |
| Leerlauf | 4 | 0 | Keine Belastung |

#### Ermuedungsberechnung fuer Zylinder

**Lebensdauer-Abschaetzung (nach DNV-GL):**

```
N_zulaessig = N_test × (p_test / p_betrieb)^m

wobei:
  N_zulaessig = Zulaessige Lastwechsel
  N_test = Im Test erreichte Lastwechsel (typisch 100.000 bei p_test)
  p_test = Pruefruck [bar]
  p_betrieb = Betriebsdruck [bar]
  m = Woehler-Exponent (3–5 fuer Stahl, 5–8 fuer Aluminium)
```

**Typische Lebensdauer-Erwartung:**

| Komponente | Lastwechsel (zulaessig) | Betriebsjahre (typisch) |
|-----------|------------------------|------------------------|
| Edelstahl-Zylinder 316L | >500.000 | 20–30 |
| Aluminium-Zylinder | >200.000 | 10–15 |
| Dichtungssatz | 50.000–100.000 | 3–7 |
| Hochdruckschlauch SAE 100R7 | 200.000 | 5–8 |
| Pumpe (Kolbenringe) | 100.000–300.000 | 5–15 |

---

## 3. Typenuebersicht

### 3.1 Handpumpen (Manual Helm Pumps)

#### Funktionsprinzip

Handpumpen werden direkt vom Steuerrad angetrieben. Jede Umdrehung des Steuerrads erzeugt ein definiertes Foerdervolumen. Es gibt zwei Grundbauarten:

**Kolbenpumpe (Piston Pump):**
- Linearer Kolben, angetrieben durch Exzenter am Steuerrad
- Foerdervolumen: 7–50 cm³ pro Umdrehung
- Druckbereich: 30–80 bar
- Vorteil: Hoher Druck moeglich, kompakt
- Nachteil: Pulsierender Volumenstrom

**Rotationspumpe (Rotary Vane Pump):**
- Fluegelzellenpumpe, direkt mit Steuerradwelle verbunden
- Foerdervolumen: 10–30 cm³ pro Umdrehung
- Druckbereich: 20–55 bar
- Vorteil: Gleichmaessiger Volumenstrom, weiches Steuergefuehl
- Nachteil: Niedrigerer Maximaldruck, groessere Bauform

#### Einsatzbereich

| Parameter | Empfohlener Bereich |
|-----------|-------------------|
| Bootslaenge (LOA) | 8–16 m |
| Ruderkraft max. | 30 kN |
| Drehmoment am Schaft | bis 2.500 Nm |
| Steuerumdrehungen H-u-H | 3–6 |
| Autopilot-Integration | Moeglich (ueber Bypass-Ventil) |
| Notsteuerung | Ist die Hauptsteuerung |

#### Auswahlkriterien

```
Handpumpen-Dimensionierung:

1. Ruderkraft F_ruder bestimmen (aus Lateralplan, v_max, Ruderflaeche)
2. Drehmoment M = F_ruder × e (Exzentrizitaet Ruderschaft)
3. Zylinder waehlen: F_zylinder = M / L_hebel, A_kolben = F_zylinder / p
4. Pumpenvolumen: V_pump = V_zylinder / n_max (max. Umdrehungen H-u-H)
5. Pumpe aus Katalog waehlen: naechstgroesseres Foerdervolumen
6. Druckverluste in Leitungen beruecksichtigen (+10–20%)
7. Sicherheitsfaktor pruefen (min. 1,5)
```

### 3.2 Motorpumpen (Power Steering Pumps)

#### Funktionsprinzip

Motorpumpen bestehen aus einem elektrischen oder motorgetriebenen Hydraulikaggregat, das den Volumenstrom unabhaengig vom Steuerrad erzeugt. Das Steuerrad betaetigt lediglich ein Steuerventil (Proportional- oder Schaltventil), das die Oelrichtung zum Zylinder bestimmt.

**Zahnradpumpe (Gear Pump):**
- Einfach, robust, kostenguenstig
- Foerdervolumen: 1–20 l/min
- Druckbereich: 50–200 bar
- Wirkungsgrad: 80–90%
- Einsatz: Motoryachten, Superyachten (Niederdruck-Seite)

**Fluegelzellenpumpe (Vane Pump):**
- Geraeuscharm, gleichmaessiger Volumenstrom
- Foerdervolumen: 2–30 l/min
- Druckbereich: 50–175 bar
- Wirkungsgrad: 85–92%
- Einsatz: Superyachten (Komfort-Anforderung)

**Axialkolbenpumpe (Axial Piston Pump):**
- Hoechster Wirkungsgrad, regelbar
- Foerdervolumen: 5–100 l/min
- Druckbereich: 100–400 bar
- Wirkungsgrad: 90–95%
- Einsatz: Grosse Superyachten, Multi-Verbraucher-Systeme

#### Einsatzbereich

| Parameter | Empfohlener Bereich |
|-----------|-------------------|
| Bootslaenge (LOA) | ab 14 m (Segelyacht), ab 10 m (Motoryacht) |
| Ruderkraft max. | 200+ kN |
| Drehmoment am Schaft | bis 40.000 Nm |
| Steuerzeit H-u-H | 3–8 Sekunden |
| Autopilot-Integration | Standard (gemeinsame Pumpe oder separate AP-Pumpe) |
| Notsteuerung | Handpumpe als Backup erforderlich |

#### Antriebsarten

| Antrieb | Leistung [kW] | Vorteile | Nachteile | Einsatz |
|---------|---------------|----------|-----------|---------|
| 12V DC Motor | 0,3–1,5 | Einfach, standard | Leistungsbegrenzung | 10–20 m Boote |
| 24V DC Motor | 0,5–3,0 | Hoehere Leistung | Standard 24V-Bordnetz noetig | 14–30 m |
| 230V AC Motor | 1,0–5,0 | Hohe Dauerleistung | Generator laeuft | 20–40 m |
| 400V AC Motor | 3,0–15,0 | Maximale Leistung | 3-Phasen-Bordnetz | 30–60 m |
| Keilriemen ab Motor | 2,0–10,0 | Immer verfuegbar | Nur bei laufendem Motor | Motoryachten |

### 3.3 Power-Assist-Systeme

#### Funktionsprinzip

Power-Assist kombiniert eine Handpumpe mit einer Motorpumpe. Bei niedriger Last (Kurshalten) arbeitet die Handpumpe allein. Bei hoher Last (Manoevrieren, schwerer Seegang) schaltet sich die Motorpumpe automatisch zu.

**Umschaltmechanismen:**

1. **Druckabhaengig**: Druckschalter bei 20–30 bar aktiviert Motorpumpe
2. **Drehzahlabhaengig**: Drehzahlsensor am Steuerrad — schnelles Drehen = hohe Last
3. **Manuell**: Schalter am Steuerstand (veraltet, aber einfach)
4. **Intelligent**: Kombination aus Druck und Drehzahl mit Mikroprozessor

#### Einsatzbereich

| Parameter | Empfohlener Bereich |
|-----------|-------------------|
| Bootslaenge (LOA) | 12–22 m (Segelyacht), 10–18 m (Motoryacht) |
| Ruderkraft max. | 80 kN |
| Besondere Eignung | Langfahrt-Segler (Energieautark bei Leichtwind, Power bei schwerer See) |
| Autopilot-Integration | Standard |
| Notsteuerung | Handpumpe allein = Notsteuerung |

#### Systemarchitektur Power-Assist

```
┌──────────┐     ┌──────────┐     ┌──────────┐
│STEUERRAD │────>│ HAND-    │────>│ STEUER-  │
│          │     │ PUMPE    │     │ VENTIL   │
└──────────┘     └──────────┘     └─────┬────┘
                                        │
                 ┌──────────┐           │
                 │ MOTOR-   │──────────>│
                 │ PUMPE    │           │
                 └─────┬────┘     ┌─────┴────┐
                       │         │ ZYLINDER  │
                 ┌─────┴────┐    └──────────┘
                 │ DRUCK-   │
                 │ SCHALTER │
                 └──────────┘
```

### 3.4 Vollelektrisch-Hydraulische Systeme

#### Funktionsprinzip

Vollelektrisch-hydraulische Systeme verwenden ein elektronisches Steuerrad (Encoder) ohne mechanische Verbindung zum Hydrauliksystem. Das Steuerrad-Signal wird elektronisch an ein Steuergeraet uebertragen, das die Hydraulikpumpe und -ventile ansteuert.

**Steer-by-Wire mit Hydraulik-Aktuator:**

```
Steuerrad (Encoder) → CAN-Bus → Steuergeraet (ECU) → Proportionalventil → Zylinder
                                        ↓
                                  Pumpe (Dauerlauf oder On-Demand)
                                        ↓
                                  Feedback: Ruderwinkel-Sensor → CAN-Bus → Force-Feedback-Motor am Steuerrad
```

**Vorteile:**
- Beliebige Steuerstandpositionen ohne Hydraulikleitungen zum Steuerrad
- Programmierbares Steuergefuehl (Uebersetzung, Daempfung, Rueckholkraft)
- Einfache Autopilot-Integration (gleiche ECU)
- Mehrere Steuerstaende ohne zusaetzliche Pumpen

**Nachteile:**
- Komplexitaet (mehr Fehlerquellen)
- Stromabhaengigkeit (kein Strom = kein Lenken)
- Redundanz zwingend erforderlich (Dual-ECU, Dual-Encoder, Dual-Pumpe)
- Hohe Kosten (10.000–80.000 EUR je nach Groesse)

#### Einsatzbereich

| Parameter | Empfohlener Bereich |
|-----------|-------------------|
| Bootslaenge (LOA) | ab 16 m (Premium-Segler), ab 14 m (Motoryacht), Standard ab 24 m |
| Ruderkraft max. | 250+ kN |
| Mehrere Steuerstaende | Ideal (Flybridge + Salon + Cockpit) |
| Autopilot-Integration | Nativ (gleiche ECU) |
| Notsteuerung | Separate Handpumpe mit Bypass PFLICHT |
| Zertifizierung | NMEA 2000, CANopen Maritime, ISO 25197 |

### 3.5 Zweikreis-Systeme (Dual Circuit)

#### Regulatorische Anforderung

Gemaess DNV-GL Rules Pt.3 Ch.13 Sec.2 muessen Yachten >24 m ueber ein redundantes Steuersystem verfuegen. Lloyd's Register fordert dies ab 500 GT. Die CE-Richtlinie 2013/53/EU fordert fuer Kategorie A/B eine Notsteuerungmoeglichkeit, ohne explizit Zweikreis zu verlangen — die meisten Klassifikationsgesellschaften interpretieren dies jedoch als Zweikreis-Erfordernis ab bestimmten Groessen.

#### Architektur-Varianten

**Variante A — Zwei unabhaengige Kreise, ein Zylinder (Standard ab 24 m):**

```
Kreis 1: Pumpe 1 → Ventilblock → Zylinderport A/B
Kreis 2: Pumpe 2 → Ventilblock → Zylinderport C/D (gleicher Zylinder, getrennte Kammern)

Umschaltung: Automatisch bei Druckabfall in Kreis 1
Notsteuerung: Jeder Kreis kann allein 100% Ruderfunktion liefern
```

**Variante B — Zwei unabhaengige Kreise, zwei Zylinder (Superyacht):**

```
Kreis 1: Pumpe 1 → Zylinder 1 (Steuerbord)
Kreis 2: Pumpe 2 → Zylinder 2 (Backbord)

Normalbetrieb: Beide Kreise arbeiten zusammen (doppelte Kraft)
Ausfallmodus: Ein Kreis genuegt fuer 100% Ruderfunktion (ggf. langsamer)
```

**Variante C — Aktiv/Standby (Kostenoptimiert):**

```
Kreis 1: Pumpe 1 (Hauptpumpe) → Zylinder
Kreis 2: Pumpe 2 (Standby, laeuft nicht) → gleicher Zylinder ueber Umschaltventil

Umschaltung: Manuell oder automatisch bei Druckabfall
Nachteil: Umschaltzeit 2–5 Sekunden
```

#### Anforderungen an Zweikreis-Systeme

| Anforderung | DNV-GL | Lloyd's | BV |
|-------------|--------|---------|-----|
| Getrennte Stromleitungen | Ja | Ja | Ja |
| Getrennte Hydraulikleitungen | Ja | Ja | Ja |
| Getrennte Oelreservoirs | Empfohlen | Ja | Empfohlen |
| Automatische Umschaltung | Ja (ab 30 m) | Ja | Ja (ab 30 m) |
| Umschaltzeit max. | 10 s | 15 s | 10 s |
| Pruefung beider Kreise | Monatlich | Monatlich | Woechentlich (>40 m) |
| Getrennte Sicherungen | Ja | Ja | Ja |

### 3.6 Autopilot-Hydraulik

#### Integration in bestehende Steueranlagen

**Methode 1 — Autopilot-Pumpe in den Hauptkreis (Standard bei Segelyachten):**

```
Handpumpe ←─→ T-Stueck ←─→ Zylinder
                  ↕
           Autopilot-Pumpe
           (Solenoid-Bypass)
```

- Autopilot-Pumpe foerdert bei Bedarf in den Hauptkreis
- Solenoid-Bypass-Ventil oeffnet den Handpumpen-Kreislauf (sonst sperrt die Handpumpe)
- Handsteuerung: Solenoid schliesst → Handpumpe direkt am Zylinder
- Autopilot-Steuerung: Solenoid oeffnet → AP-Pumpe uebernimmt

**Methode 2 — Separate Autopilot-Pumpe mit eigenem Zylinder (Superyacht):**

```
Hauptpumpe → Hauptzylinder (gross, Hauptsteuerung)
AP-Pumpe → AP-Zylinder (klein, nur fuer Kurshalten)

Vorteil: Keine Interferenz, AP-Zylinder optimiert fuer kleine, schnelle Korrekturen
Nachteil: Doppelte Hydraulikinstallation, hoehere Kosten
```

**Methode 3 — Proportionalventil-Steuerung (moderne Motorpumpen):**

```
Steuerrad-Encoder → ECU → Proportionalventil → Zylinder
Autopilot-Signal → ECU → Proportionalventil → gleicher Zylinder

ECU entscheidet, ob Steuerrad oder Autopilot Prioritaet hat
```

#### Autopilot-Pumpen — Dimensionierung

| Bootsgroesse [m] | Zylinder-Volumen [cm³] | AP-Pumpe Foerdervolumen [cm³/s] | Rudergeschwindigkeit [°/s] | Leistung [W] |
|-------------------|------------------------|-------------------------------|---------------------------|-------------|
| 8–12 | 50–150 | 5–15 | 8–12 | 50–150 |
| 12–16 | 150–400 | 15–30 | 5–10 | 100–300 |
| 16–22 | 400–1.000 | 30–60 | 4–8 | 200–600 |
| 22–30 | 1.000–2.500 | 60–150 | 3–6 | 400–1.500 |
| 30–45 | 2.500–5.000 | 150–300 | 2–5 | 1.000–3.000 |

#### Autopilot-Hydraulik — Haeufige Probleme

| Problem | Ursache | Loesung |
|---------|---------|---------|
| AP "kaempft" gegen Handpumpe | Solenoid-Bypass schliesst nicht vollstaendig | Solenoid pruefen, ggf. tauschen |
| Ruder driftet bei AP-Betrieb | Interne Leckage im AP-Zylinder | Dichtungen pruefen |
| AP-Pumpe laeuft staendig | Druck im System faellt ab (Leckage) | Hauptsystem auf Leckage pruefen |
| Ruckartige Ruder-Bewegungen | Luft im AP-Kreis | AP-Kreis separat entlueften |
| Uebersteuerung durch AP | AP-Pumpe zu gross fuer Zylinder | Volumenstrom am AP reduzieren |

---

## 4. Produktlinien und Spezifikationen

### 4.1 Jefa Steering (Daenemark)

#### HSC-Serie (Hydraulic Steering Cylinder)

Jefa ist der fuehrende Hersteller fuer Segelyacht-Steueranlagen im Performance- und Cruiser-Segment. Die HSC-Serie umfasst Hydraulikzylinder fuer Yachten von 8 bis 30 m.

| Modell | Bohrung [mm] | Hub [mm] | Ruderkraft_max [kN] | Volumen [cm³] | Druck_max [bar] | Gewicht [kg] | Einsatz |
|--------|-------------|----------|---------------------|---------------|-----------------|-------------|---------|
| HSC 40-100 | 40 | 100 | 8,8 | 126 | 70 | 2,1 | 8–11 m Segelyacht |
| HSC 40-120 | 40 | 120 | 8,8 | 151 | 70 | 2,3 | 9–12 m Segelyacht |
| HSC 50-130 | 50 | 130 | 13,7 | 255 | 70 | 3,4 | 11–14 m Segelyacht |
| HSC 50-160 | 50 | 160 | 13,7 | 314 | 70 | 3,8 | 12–16 m Segelyacht |
| HSC 65-160 | 65 | 160 | 23,2 | 531 | 70 | 5,6 | 14–18 m Segelyacht |
| HSC 65-200 | 65 | 200 | 23,2 | 663 | 70 | 6,4 | 15–20 m Segelyacht |
| HSC 80-200 | 80 | 200 | 35,2 | 1.005 | 70 | 9,2 | 18–24 m Segelyacht |
| HSC 80-250 | 80 | 250 | 35,2 | 1.257 | 70 | 10,8 | 20–26 m Segelyacht |
| HSC 100-250 | 100 | 250 | 55,0 | 1.963 | 70 | 15,4 | 22–30 m Segelyacht |
| HSC 100-300 | 100 | 300 | 55,0 | 2.356 | 70 | 17,2 | 24–30 m Segelyacht |

#### HPC-Serie (High Performance Cylinder)

Fuer Racing und High-Performance-Segelyachten mit hoeherem Betriebsdruck.

| Modell | Bohrung [mm] | Hub [mm] | Ruderkraft_max [kN] | Druck_max [bar] | Gewicht [kg] | Besonderheit |
|--------|-------------|----------|---------------------|-----------------|-------------|-------------|
| HPC 40-100 | 40 | 100 | 14,0 | 112 | 2,5 | Aluminium-Gehaeuse |
| HPC 50-130 | 50 | 130 | 22,0 | 112 | 4,0 | Aluminium-Gehaeuse |
| HPC 65-160 | 65 | 160 | 37,0 | 112 | 6,8 | Edelstahl-Kolbenstange |
| HPC 80-200 | 80 | 200 | 56,0 | 112 | 11,5 | Edelstahl-Kolbenstange |

#### Jefa Handpumpen

| Modell | Foerdervolumen [cm³/Umdr.] | Druck_max [bar] | Passend fuer Zylinder | Gewicht [kg] |
|--------|---------------------------|-----------------|----------------------|-------------|
| HP 14 | 14 | 80 | HSC 40/50 | 2,8 |
| HP 16 | 16 | 80 | HSC 50/65 | 3,1 |
| HP 22 | 22 | 80 | HSC 65/80 | 3,8 |
| HP 28 | 28 | 70 | HSC 80 | 4,2 |
| HP 36 | 36 | 70 | HSC 100 | 5,1 |

#### Jefa Oel-Spezifikation

Jefa schreibt ISO VG 15 Hydraulikoel vor fuer alle HSC/HPC-Systeme. Empfohlen: Jefa HO-15 (eigene Marke) oder vergleichbares DIN 51524 Part 2 HLP-Oel.

### 4.2 Kobelt Manufacturing (Kanada)

#### 7004-Serie (Compact Helm Pump)

| Modell | Foerdervolumen [cm³/Umdr.] | Druck_max [bar] | Steuerrad-Anschluss | Einsatz |
|--------|---------------------------|-----------------|---------------------|---------|
| 7004-101 | 10 | 105 | 3/4"-18 Tapered | Sportboote 8–12 m |
| 7004-201 | 14 | 105 | 3/4"-18 Tapered | Segelyachten 10–14 m |
| 7004-301 | 18 | 105 | 3/4"-18 Tapered | Segelyachten 12–16 m |
| 7004-401 | 22 | 105 | 1"-14 Tapered | Motoryachten 12–18 m |
| 7004-501 | 28 | 105 | 1"-14 Tapered | Motoryachten 14–20 m |

#### 7012-Serie (Power-Assist Helm Pump)

| Modell | Foerdervolumen [cm³/Umdr.] | Druck_max [bar] | Power-Assist | Motor |
|--------|---------------------------|-----------------|-------------|-------|
| 7012-101 | 14 | 140 | Integriert | 12V DC, 200 W |
| 7012-201 | 18 | 140 | Integriert | 12V DC, 350 W |
| 7012-301 | 22 | 140 | Integriert | 24V DC, 500 W |
| 7012-401 | 28 | 140 | Integriert | 24V DC, 750 W |
| 7012-501 | 36 | 140 | Integriert | 24V DC, 1.000 W |

#### Kobelt Zylinder

| Modell | Bohrung [mm] | Hub [mm] | Ruderkraft_max [kN] | Anschluss | Material |
|--------|-------------|----------|---------------------|-----------|----------|
| 7050-110 | 50 | 127 | 18,5 | 3/8" SAE | Aluminium eloxiert |
| 7050-120 | 63 | 152 | 29,2 | 3/8" SAE | Aluminium eloxiert |
| 7050-130 | 76 | 178 | 42,5 | 1/2" SAE | Aluminium eloxiert |
| 7050-140 | 89 | 203 | 58,2 | 1/2" SAE | Edelstahl 316 |
| 7050-150 | 102 | 229 | 76,5 | 3/4" SAE | Edelstahl 316 |

### 4.3 Lewmar (Vereinigtes Koenigreich)

#### Continuum-Serie (Elektro-Hydraulisch)

Die Lewmar Continuum-Serie ist ein vollelektrisch-hydraulisches System mit integriertem Autopilot-Interface.

| Modell | Ruderkraft_max [kN] | Zylinder-Bohrung [mm] | Pumpe | Motor | Einsatz |
|--------|---------------------|----------------------|-------|-------|---------|
| Continuum 500 | 15 | 50 | Zahnrad, 2,5 l/min | 12V, 250 W | 10–14 m Segelyacht |
| Continuum 800 | 25 | 65 | Zahnrad, 4,0 l/min | 12V, 400 W | 12–18 m Segelyacht |
| Continuum 1200 | 40 | 80 | Zahnrad, 6,0 l/min | 24V, 600 W | 16–22 m Segelyacht |
| Continuum 2000 | 65 | 100 | Zahnrad, 10,0 l/min | 24V, 1.200 W | 20–28 m Segelyacht |
| Continuum 3000 | 100 | 125 | Fluegelzelle, 15,0 l/min | 24V, 2.000 W | 26–36 m Motoryacht |

**Besonderheiten der Continuum-Serie:**
- Integriertes NMEA 2000 Interface
- Programmierbares Force-Feedback am Steuerrad
- Automatische Ruderbegrenzung (Soft-Stop bei max. Ruderausschlag)
- Integrierte Entlueftung (Auto-Bleed)
- Oeltemperatur-Ueberwachung mit Alarm

#### Lewmar Handpumpen (Classic-Serie)

| Modell | Foerdervolumen [cm³/Umdr.] | Druck_max [bar] | Gewicht [kg] |
|--------|---------------------------|-----------------|-------------|
| Classic HP10 | 10 | 70 | 2,1 |
| Classic HP14 | 14 | 70 | 2,5 |
| Classic HP20 | 20 | 70 | 3,2 |
| Classic HP28 | 28 | 70 | 4,0 |

### 4.4 Vetus (Niederlande)

#### HTP-Serie (Hydraulic Tilt & Power)

Vetus bietet komplette Hydrauliksysteme fuer Motoryachten, einschliesslich Trimmklappen-Integration.

| Modell | Ruderkraft_max [kN] | Zylinder | Pumpe | Motor | Features |
|--------|---------------------|----------|-------|-------|----------|
| HTP 20 | 20 | 50×130 mm | Zahnrad | 12V, 300 W | Basis |
| HTP 30 | 30 | 63×152 mm | Zahnrad | 12V, 450 W | + Trimmklappen-Anschluss |
| HTP 42 | 42 | 76×178 mm | Zahnrad | 24V, 600 W | + Autopilot-Interface |
| HTP 60 | 60 | 89×203 mm | Fluegelzelle | 24V, 1.000 W | + NMEA 2000 |
| HTP 80 | 80 | 102×229 mm | Fluegelzelle | 24V, 1.500 W | + Oelkuehler |
| HTP 120 | 120 | 125×279 mm | Fluegelzelle | 24V, 2.500 W | + Zweikreis-Option |

#### Vetus Zubehoer

| Artikel | Bezeichnung | Preis (ca.) |
|---------|-------------|-------------|
| HTP-SET1 | Entlueftungs-Kit (Spritze + Adapter) | 45 EUR |
| HTP-OIL5 | Hydraulikoel VG 15, 5 Liter | 38 EUR |
| HTP-OIL20 | Hydraulikoel VG 15, 20 Liter | 125 EUR |
| HTP-FILTER | Oelfilter-Element (10µm) | 22 EUR |
| HTP-COOL | Wasser-Oel-Kuehler, 2 kW | 380 EUR |
| HTP-BYPASS | Autopilot-Bypass-Ventil (12V Solenoid) | 195 EUR |

### 4.5 Hynautic (USA, Teil von Teleflex/SeaStar)

#### Hynautic Steueranlagen

Hynautic war ein Pionier der Yacht-Hydrauliksteuerung und ist heute Teil der Dometic/SeaStar-Gruppe. Altanlagen sind noch weit verbreitet.

| Modell | Typ | Foerdervolumen [cm³/Umdr.] | Druck_max [bar] | Einsatz |
|--------|-----|---------------------------|-----------------|---------|
| H-50 | Handpumpe | 10 | 70 | Klassiker, 8–12 m |
| H-60 | Handpumpe | 14 | 70 | Klassiker, 10–14 m |
| H-70 | Handpumpe | 20 | 70 | Klassiker, 12–16 m |
| H-80 | Power-Assist | 14 | 105 | Mit 12V Motor |
| H-90 | Power-Assist | 20 | 105 | Mit 12V Motor |

**Hinweis fuer AYDI-Bewertung:**
Hynautic-Systeme sind seit den 1970er-Jahren verbaut. Bei aelteren Booten (>20 Jahre) ist die Dichtungsmaterial-Vertraeglichkeit mit modernen Oelen zu pruefen. Original-Hynautic-Oel (Type A) wird nicht mehr hergestellt — Ersatz: ISO VG 15, kompatibel mit NBR-Dichtungen.

### 4.6 Teleflex/SeaStar (USA/Kanada, Dometic-Gruppe)

#### SeaStar Solutions — BayStar/SeaStar/Optimus

| Serie | Modell | Typ | Ruderkraft_max [kN] | Einsatz | Preis (ca.) |
|-------|--------|-----|---------------------|---------|-------------|
| BayStar | HK4200A-3 | Handpumpe | 10 | Aussenborder bis 150 PS | 650 EUR |
| BayStar Plus | HK4300A-3 | Handpumpe | 15 | Aussenborder bis 300 PS | 850 EUR |
| SeaStar | HK6400A-3 | Handpumpe | 20 | Innenborder/Aussenborder bis 14 m | 1.100 EUR |
| SeaStar Pro | HK7500A-3 | Power-Assist | 35 | Motoryachten 12–18 m | 2.400 EUR |
| Optimus EPS | — | Vollelektrisch | 60 | Elektro-Hydraulisch, 14–24 m | 8.500 EUR |
| Optimus 360 | — | Joystick | 60 | Joystick + Autopilot, Multi-Engine | 12.000 EUR |

#### SeaStar Zylinder

| Modell | Bohrung [mm] | Hub [mm] | Ruderkraft_max [kN] | Einsatz |
|--------|-------------|----------|---------------------|---------|
| HC5345-3 | 50 | 130 | 15,0 | BayStar, SeaStar |
| HC5348-3 | 63 | 160 | 25,0 | SeaStar, SeaStar Pro |
| HC5370-3 | 76 | 190 | 38,0 | SeaStar Pro |
| HC6750 | 89 | 215 | 52,0 | Optimus |
| HC6850 | 102 | 250 | 68,0 | Optimus 360 |

### 4.7 Preisvergleich nach Systemkategorie

| Kategorie | System | Preisspanne (EUR) | Typische Konfiguration |
|-----------|--------|-------------------|----------------------|
| Basis Handpumpe | Handpumpe + Zylinder + Leitungen | 800–2.500 | SeaStar BayStar, Vetus Basic |
| Mittel Handpumpe | Hochwertige Handpumpe + Zylinder | 2.500–5.000 | Jefa HSC, Kobelt 7004 |
| Power-Assist | Handpumpe + Motorpumpe + Zylinder | 3.500–8.000 | Kobelt 7012, SeaStar Pro |
| Elektro-Hydraulisch | Komplettsystem mit ECU | 6.000–15.000 | Lewmar Continuum, Optimus EPS |
| Superyacht Einkreis | Motorpumpe + Grosszylinder | 12.000–30.000 | Kobelt + Vetus HTP 120 |
| Superyacht Zweikreis | Dual-System mit Umschaltung | 25.000–80.000 | Individuelle Auslegung |

### 4.8 Ersatzteil-Verfuegbarkeit und Kompatibilitaet

#### Kreuz-Kompatibilitaet zwischen Herstellern

**WARNUNG:** Hydraulische Steuerkomponenten verschiedener Hersteller sind in der Regel NICHT direkt kompatibel. Auch wenn die Anschlussmasse (SAE-Fittings) identisch sind, unterscheiden sich:

1. **Systemdruecke**: Jefa HSC arbeitet bei 70 bar, Kobelt 7050 bei 105 bar → unterschiedliche Dichtungsauslegung
2. **Oelspezifikation**: Jefa empfiehlt VG 15, manche SeaStar-Systeme verwenden VG 32 → Mischung kann Dichtungen schaedigen
3. **Foerdervolumen pro Umdrehung**: Muss zum Zylinder passen → falsche Pumpe = zu viele/wenige Umdrehungen H-u-H
4. **Bypass-Ventile**: AP-Bypass-Ventile sind oft herstellerspezifisch (Steuerdruck, Durchfluss)

**Kompatibilitaetsmatrix — Pumpe ↔ Zylinder:**

| Pumpe \ Zylinder | Jefa HSC | Kobelt 7050 | Vetus HTP | SeaStar HC | Lewmar |
|------------------|----------|-------------|-----------|-----------|--------|
| Jefa HP | ✓ | ⚠ Druck | ⚠ Druck | ⚠ Druck | ✗ |
| Kobelt 7004 | ⚠ Volumen | ✓ | ⚠ Volumen | ✓ | ✗ |
| Vetus | ✗ System | ✗ System | ✓ | ✗ System | ✗ |
| SeaStar | ⚠ Volumen | ✓ | ⚠ Volumen | ✓ | ✗ |
| Lewmar Cont. | ✗ System | ✗ System | ✗ System | ✗ System | ✓ |

✓ = Kompatibel | ⚠ = Bedingt kompatibel (Pruefung erforderlich) | ✗ = Nicht kompatibel

**Empfehlung AYDI:** Immer Komponenten vom gleichen Hersteller verwenden. Bei Mischinstallation: Systemdruck, Oel-Kompatibilitaet und Volumenstrom-Abstimmung durch Fachbetrieb pruefen lassen.

#### Ersatzteil-Kritische Komponenten

| Komponente | Verfuegbarkeit | Lieferzeit typisch | Empfehlung Bordvorrat |
|-----------|----------------|--------------------|-----------------------|
| Dichtungssatz Zylinder | Gut (alle Hersteller) | 3–10 Tage | JA — immer an Bord |
| Dichtungssatz Pumpe | Gut | 5–14 Tage | JA — bei Langfahrt |
| Hydraulikoel (1 Liter) | Ueberall erhaeltlich | Sofort | JA — immer an Bord |
| Ersatzschlauch (fertig konfektioniert) | Mittel | 5–20 Tage | Empfohlen bei Langfahrt |
| Bypass-Solenoid (AP) | Eingeschraenkt | 10–30 Tage | Bei Langfahrt empfohlen |
| Ueberdruckventil | Eingeschraenkt | 14–30 Tage | Nein (selten defekt) |
| Druckschalter (Motorpumpe) | Gut | 3–10 Tage | Bei Langfahrt empfohlen |
| Kolbenstange | Herstellerspezifisch | 20–60 Tage | Nein |
| ECU (Elektro-Hydraulik) | Herstellerspezifisch | 14–60 Tage | Nein (teuer, selten defekt) |

#### Langfahrt-Ersatzteilpaket — Empfehlung AYDI

**Basispaket (alle Yachten mit Hydrauliksteuerung, Langfahrt >500 sm):**
- 1× Dichtungssatz Zylinder (komplett)
- 1× Hydraulikoel, 1 Liter (gleicher Typ wie im System!)
- 1× Entlueftungsspritze mit Schlauch
- 2× O-Ringe fuer jeden Fitting-Typ im System
- 1× PTFE-Gewindedichtband
- Lappen, Auffangschale

**Erweitertes Paket (Langfahrt >2.000 sm, transozeanisch):**
- Alles aus Basispaket, plus:
- 1× Dichtungssatz Pumpe
- 1× Ersatzschlauch (laengster Schlauch im System, fertig konfektioniert)
- 1× Bypass-Solenoid (wenn AP vorhanden)
- 1× Druckschalter (wenn Motorpumpe vorhanden)
- 2 Liter Hydraulikoel zusaetzlich

### 4.9 Installationsstandards und Best Practices

#### Leitungsfuehrung — Dos and Don'ts

**Richtig:**
- Leitungen in Schellen mit Gummieinlage befestigen (alle 500 mm bei Schlauch, 300 mm bei Rohr)
- Biegevorrat lassen (min. 50 mm mehr als Mindestbiegeradius)
- Schlaeuche mit Drallschutz verlegen (Markierungslinie auf Schlauch beachten)
- Schotdurchfuehrungen mit Gummituelle oder Schott-Verschraubung
- Leitungen abseits von heissen Teilen fuehren (min. 100 mm zu Abgaskruemmer)
- Niederdruckseite (Ruecklauf) mit groesserem Querschnitt als Druckseite

**Falsch:**
- Schlaeuche unter Spannung montieren (→ Fitting-Ermuedung)
- Schlaeuche zu eng biegen (→ Innenseele knickt, Stroemungswiderstand steigt)
- Leitungen durch Bilgenwasser fuehren (→ Korrosion Fittings, Schlauchversproeung)
- Schlaeuche als Fussstuetze/Haltegriff missbrauchen (→ Abrieb, Knicke)
- Kupferleitungen direkt an Aluminium-Fittings (→ galvanische Korrosion)
- Schlaeuche mit Kabelbindern statt Rohrschellen fixieren (→ Einschnuerung, Abrieb)

#### Inbetriebnahme-Protokoll

**Checkliste Erstinbetriebnahme Hydrauliksteuerung:**

| Schritt | Pruefung | Kriterium | ✓/✗ |
|---------|----------|-----------|------|
| 1 | Alle Fittings handfest + definiertes Anzugsdrehmoment | Herstellerangabe | |
| 2 | Oelreservoir gefuellt (korrekte Oelsorte!) | Markierung erreicht | |
| 3 | Entlueftung durchgefuehrt (Vakuum- oder Druckmethode) | Blasenfreies Oel an Entlueftung | |
| 4 | Steuer von Anschlag zu Anschlag | Gleichmaessig, kein Ruckeln | |
| 5 | Umdrehungen H-u-H zaehlen | Herstellerangabe ±0,5 | |
| 6 | Ruderendanschlaege erreicht | Beide Seiten symmetrisch | |
| 7 | Leckage-Sichtkontrolle aller Fittings | Trocken | |
| 8 | Druckhaltetest 30 min bei Betriebsdruck | Druckverlust <2% | |
| 9 | Oelstand nach Entlueftung nochmals pruefen | Im Markierungsbereich | |
| 10 | Motorpumpe: Anlauf und Abschaltung | Schaltet bei Solldruck ab | |
| 11 | Autopilot-Bypass: Funktion pruefen | Solenoid schaltet, Bypass oeffnet | |
| 12 | Notsteuerung: Funktion pruefen | Pinne/Handpumpe lenkt Ruder | |
| 13 | Ruderwinkelanzeige: Kalibrierung | Anzeige stimmt mit tatsaechlichem Winkel | |
| 14 | Dokumentation: Seriennummern, Oeltyp, Datum | Eingetragen in Bordhandbuch | |

---

## 5. Hersteller-Datenbank

### 5.1 Jefa Steering A/S

| Feld | Wert |
|------|------|
| **Land** | Daenemark |
| **Gruendung** | 1979 |
| **Spezialisierung** | Segelyacht-Steueranlagen, Performance-Ruderanlagen |
| **Produktpalette** | Hydraulikzylinder (HSC/HPC), Handpumpen (HP), Ruderschaftlager, Quadranten |
| **Bootsgroesse** | 8–35 m Segelyachten |
| **Zertifizierung** | CE, ISO 10592, DNV-GL Typzulassung |
| **Vertrieb** | Weltweit ueber Fachhhandel und Werften |
| **Besonderheit** | Marktfuehrer bei Performance-Segelyachten, OEM fuer Hallberg-Rassy, Najad, Swan |
| **Website** | www.jefa.com |
| **Typische Lieferzeit** | 2–4 Wochen (Standardmodelle), 6–10 Wochen (Sonderanfertigungen) |
| **Garantie** | 5 Jahre auf Zylinder, 3 Jahre auf Pumpen |
| **AYDI-Qualitaetsscore** | 92/100 |

**Staerken:** Hoechste Verarbeitungsqualitaet, praezise Toleranzen (<0,01 mm am Kolben), ausgezeichneter Korrosionsschutz (vollstaendig 316L), breites Ersatzteilprogramm.

**Schwaechen:** Hoher Preis (~30% ueber Wettbewerb), begrenzte Motoryacht-Loesungen, keine Elektro-Hydraulik-Systeme.

### 5.2 Kobelt Manufacturing Ltd.

| Feld | Wert |
|------|------|
| **Land** | Kanada (British Columbia) |
| **Gruendung** | 1962 |
| **Spezialisierung** | Hydraulische Steuer- und Antriebssteuerungen, Industrie-Marine |
| **Produktpalette** | Handpumpen (7004), Power-Assist (7012), Zylinder (7050), Throttle Controls |
| **Bootsgroesse** | 10–45 m Segel- und Motoryachten, kommerzielle Schiffe |
| **Zertifizierung** | CE, ISO 10592, Transport Canada, ABYC P-21 |
| **Vertrieb** | Nordamerika direkt, Europa ueber Distributor |
| **Besonderheit** | Sehr robuste Bauweise, bewahrt in rauer Umgebung (Fischerei, Arbeitsboote), auch fuer Yachten geeignet |
| **Website** | www.kobelt.com |
| **Typische Lieferzeit** | 3–6 Wochen |
| **Garantie** | 3 Jahre |
| **AYDI-Qualitaetsscore** | 88/100 |

**Staerken:** Extrem robust, bewahrt bei kommerziellen Anwendungen, gutes Preis-Leistungs-Verhaeltnis, breite Power-Assist-Palette.

**Schwaechen:** Weniger Feinschliff als Jefa, Aluminium-Gehaeuse (Galvanik-Risiko bei Salzwasser), kanadische Gewindemasse (teilweise Zoll-Masse).

### 5.3 Lewmar Ltd.

| Feld | Wert |
|------|------|
| **Land** | Vereinigtes Koenigreich |
| **Gruendung** | 1946 |
| **Spezialisierung** | Deck-Hardware, Winschen, Luken, Steueranlagen |
| **Produktpalette** | Continuum-Serie (Elektro-Hydraulisch), Classic Handpumpen, Ankerwinschen-Hydraulik |
| **Bootsgroesse** | 10–40 m Segel- und Motoryachten |
| **Zertifizierung** | CE, ISO 10592, ISO 25197, NMEA 2000 zertifiziert |
| **Vertrieb** | Weltweit ueber Fachhhandel |
| **Besonderheit** | Einziger Hersteller mit vollintegriertem NMEA 2000 Elektro-Hydraulik-System im Mittelklasse-Segment |
| **Website** | www.lewmar.com |
| **Typische Lieferzeit** | 2–4 Wochen (Standardmodelle) |
| **Garantie** | 3 Jahre |
| **AYDI-Qualitaetsscore** | 86/100 |

**Staerken:** Innovative Elektronik-Integration, gute Software-Updates, breites Zubehoerprogramm, guter After-Sales.

**Schwaechen:** Elektronik-Komplexitaet (mehr potentielle Fehlerquellen), Preis im oberen Segment, Ersatzteil-Verfuegbarkeit bei aelteren Modellen eingeschraenkt.

### 5.4 Vetus B.V.

| Feld | Wert |
|------|------|
| **Land** | Niederlande |
| **Gruendung** | 1951 |
| **Spezialisierung** | Marine-Antriebe, Bugstrahlruder, Hydrauliksysteme, Komfort-Systeme |
| **Produktpalette** | HTP-Serie (Komplettsysteme), Hydraulikpumpen, Bugstrahlruder-Hydraulik |
| **Bootsgroesse** | 8–30 m, Schwerpunkt Motoryachten |
| **Zertifizierung** | CE, ISO 10592, DNV-GL (ausgewaehlte Modelle) |
| **Vertrieb** | Europa direkt, weltweit ueber Distributor |
| **Besonderheit** | Komplettsystem-Anbieter (Steuerung + Bugstrahlruder + Trimmklappen aus einer Hand), gutes Preis-Leistungs-Verhaeltnis |
| **Website** | www.vetus.com |
| **Typische Lieferzeit** | 1–3 Wochen (Standard), 4–8 Wochen (Sonderanfertigung) |
| **Garantie** | 2 Jahre (Standard), 5 Jahre (registriert) |
| **AYDI-Qualitaetsscore** | 82/100 |

**Staerken:** Gutes Preis-Leistungs-Verhaeltnis, Komplettsystem aus einer Hand, breite Verfuegbarkeit in Europa, einfache Installation.

**Schwaechen:** Mittlere Verarbeitungsqualitaet (akzeptabel, nicht Premium), Aluminium-Gehaeuse standard, Oelkuehlung erst ab HTP 80.

### 5.5 Dometic Marine / SeaStar Solutions

| Feld | Wert |
|------|------|
| **Land** | USA/Kanada (Dometic-Gruppe, Schweden) |
| **Gruendung** | 1970 (als Teleflex Marine) |
| **Spezialisierung** | Hydraulische und mechanische Steueranlagen fuer Freizeit-Boote |
| **Produktpalette** | BayStar, SeaStar, Optimus EPS/360, Hynautic-Ersatzteile |
| **Bootsgroesse** | 6–24 m, Schwerpunkt Aussenborder- und Motoryachten |
| **Zertifizierung** | CE, ISO 10592, ABYC P-21, NMEA 2000 (Optimus) |
| **Vertrieb** | Weltweit, groesstes Netzwerk im Steueranlagen-Markt |
| **Besonderheit** | Marktfuehrer bei Aussenborder-Hydraulik, Optimus 360 Joystick-System |
| **Website** | www.dometic.com/marine |
| **Typische Lieferzeit** | 1–2 Wochen (Standard), 3–5 Wochen (Optimus) |
| **Garantie** | 3 Jahre (BayStar/SeaStar), 5 Jahre (Optimus) |
| **AYDI-Qualitaetsscore** | 80/100 |

**Staerken:** Groesstes Vertriebsnetz weltweit, einfache Ersatzteilbeschaffung, umfangreiche Dokumentation, gute Optimus-Technologie.

**Schwaechen:** Massenprodukt-Qualitaet (fuer Segelyacht-Enthusiasten unzureichend), Plastik-Komponenten in Basis-Serien, Service nur ueber Haendler.

### 5.6 Hydrive Engineering Pty Ltd.

| Feld | Wert |
|------|------|
| **Land** | Australien |
| **Gruendung** | 1989 |
| **Spezialisierung** | Hydraulische Steueranlagen fuer Segel- und Motoryachten, Admiral-Serie fuer Superyachten |
| **Produktpalette** | Handpumpen (Commander), Power-Assist (Admiral), Zylinder, Komplettloesungen |
| **Bootsgroesse** | 8–45 m |
| **Zertifizierung** | CE, ISO 10592, ABYC P-21, AS 1210 |
| **Vertrieb** | Australien/Neuseeland direkt, weltweit ueber Distributor |
| **Besonderheit** | Spezialist fuer Twin-Engine Motoryachten, ausgezeichnete korrosionsbestaendige Materialien (Haertetest Tropik) |
| **Website** | www.hydrive.com.au |
| **Typische Lieferzeit** | 4–8 Wochen (Versand ex Australien) |
| **Garantie** | 3 Jahre |
| **AYDI-Qualitaetsscore** | 84/100 |

**Staerken:** Sehr gute Korrosionsbestaendigkeit, robuste Bauweise fuer tropische Reviere, gute Twin-Engine-Loesungen.

**Schwaechen:** Lange Lieferzeiten nach Europa, eingeschraenktes Haendlernetz in Europa, Ersatzteile schwer verfuegbar.

### 5.7 Hersteller-Vergleichsmatrix

| Kriterium | Jefa | Kobelt | Lewmar | Vetus | SeaStar | Hydrive |
|-----------|------|--------|--------|-------|---------|---------|
| Segelyacht-Eignung | ★★★★★ | ★★★★☆ | ★★★★☆ | ★★★☆☆ | ★★☆☆☆ | ★★★★☆ |
| Motoryacht-Eignung | ★★☆☆☆ | ★★★★☆ | ★★★★☆ | ★★★★★ | ★★★★★ | ★★★★★ |
| Verarbeitungsqualitaet | ★★★★★ | ★★★★☆ | ★★★★☆ | ★★★☆☆ | ★★★☆☆ | ★★★★☆ |
| Preis-Leistung | ★★★☆☆ | ★★★★☆ | ★★★☆☆ | ★★★★★ | ★★★★★ | ★★★★☆ |
| Ersatzteil-Verfuegbarkeit | ★★★★☆ | ★★★☆☆ | ★★★★☆ | ★★★★★ | ★★★★★ | ★★☆☆☆ |
| Elektronik-Integration | ★★☆☆☆ | ★★★☆☆ | ★★★★★ | ★★★★☆ | ★★★★★ | ★★★☆☆ |
| Korrosionsschutz | ★★★★★ | ★★★☆☆ | ★★★★☆ | ★★★☆☆ | ★★★☆☆ | ★★★★★ |

---

## 6. Fehlerbild-Atlas

### 6.1 Fehlerbild F-HS-01: Externe Leckage an Zylinderabdichtung

**Beschreibung:** Oelfilm oder Tropfen an der Zylinderkolbenstange, typisch an der Kolbenstangendichtung (Abstreifer/Stangendichtung).

**Visuelle Merkmale (fuer Pipeline B — Bildanalyse):**
- Oelansammlung am Zylindergehaeuse, tropfenfoermig nach unten laufend
- Glatter Oelfilm auf der Kolbenstange (sichtbar bei ausgefahrenem Zylinder)
- Verfaerbung/Kristallisation am Gehaeuse durch altes, eingetrocknetes Oel
- Im Extremfall: Oelpfuetze unter dem Zylinder

**Schweregrade:**

| Grad | Beschreibung | Oelverlust | AYDI-Score-Abzug |
|------|-------------|-----------|------------------|
| Leicht | Oelfilm, kein Tropfen | <5 ml/Woche | -5 |
| Mittel | Gelegentliche Tropfen | 5–50 ml/Woche | -15 |
| Schwer | Regelmaessiges Tropfen | 50–200 ml/Woche | -30 |
| Kritisch | Staendiger Oelverlust, Oelstand im Reservoir sinkt sichtbar | >200 ml/Woche | -50 |

**Ursachen:**
1. Alterung der Stangendichtung (NBR-Verhaertung nach 5–8 Jahren)
2. Kratzer auf der Kolbenstange (Korrosion, Beschaedigung)
3. Falsche Oelviskositaet (zu duenn → kriecht durch Dichtlippe)
4. Uebermaessiger Seitendruck (Fehlausrichtung Zylinder/Quadrant)
5. Temperatur-Extreme (Frost → Dichtung schrumpft, Hitze → Oel duennfluessiger)

**Massnahmen:**
| Schweregrad | Massnahme | Dringlichkeit | Kosten (ca.) |
|-------------|-----------|---------------|-------------|
| Leicht | Beobachten, Oelstand kontrollieren | Naechste Wartung | 0 EUR |
| Mittel | Dichtungssatz tauschen | Innerhalb 4 Wochen | 80–200 EUR |
| Schwer | Dichtungssatz + Kolbenstange pruefen | Innerhalb 1 Woche | 200–500 EUR |
| Kritisch | Zylinder-Ueberholung oder -Austausch | Sofort | 500–2.000 EUR |

### 6.2 Fehlerbild F-HS-02: Interne Leckage (Zylinder-Drift)

**Beschreibung:** Das Ruder wandert langsam von der eingestellten Position weg, obwohl das Steuerrad feststeht. Keine aeussere Leckage sichtbar.

**Symptome:**
- Boot laeuft langsam aus dem Kurs
- Steuerrad muss regelmaessig nachkorrigiert werden
- Autopilot arbeitet staendig (erhoehter Stromverbrauch)
- Im Extremfall: Ruder schlaegt bei Fahrt langsam nach einer Seite aus

**Ursachen:**
1. Verschlissene Kolbendichtung → Oel fliesst intern von einer Kammer zur anderen
2. Verschlissener Zylinderlaufflaeche (Riefen, Korrosion innen)
3. Defektes Rueckschlagventil in der Pumpe
4. Undichtes Bypass-Ventil (Autopilot-Solenoid leckt)

**Diagnose-Verfahren:**

```
Drift-Test:
1. Boot im Wasser, Motor aus, Ruder mittig
2. Steuerrad loslassen, Position markieren
3. 10 Minuten warten
4. Ruderbewegung messen

Ergebnis:
  <1° Drift in 10 min → Normal
  1–3° Drift in 10 min → Beginnende interne Leckage
  3–10° Drift in 10 min → Deutliche interne Leckage → Dichtungstausch
  >10° Drift in 10 min → Schwere interne Leckage → Zylinder-Ueberholung
```

**AYDI-Score-Abzug:**

| Drift [°/10min] | Score-Abzug | Bewertung |
|------------------|-------------|-----------|
| <1 | 0 | Normal |
| 1–3 | -10 | Beobachten |
| 3–10 | -25 | Reparatur planen |
| >10 | -45 | Sofortige Reparatur |

### 6.3 Fehlerbild F-HS-03: Schwammiges Steuer (Luft im System)

**Beschreibung:** Das Steuerrad fuehlt sich weich, federnd, schwammig an. Direktes Ansprechen des Ruders fehlt. In Extremfaellen: Steuerrad laesst sich fast ohne Widerstand drehen, ohne dass sich das Ruder bewegt.

**Symptome:**
- Steuerrad hat "toten Bereich" um die Mitte
- Ruder reagiert verzoegert auf Steuerbewegung
- Steuergefuehl veraendert sich mit Temperatur (Luft dehnt sich bei Waerme)
- Bei schnellem Lenken: Kavitationsgeraeusche (Klicken, Blubbern)

**Ursachen:**
1. Unvollstaendige Entlueftung nach Wartung/Installation
2. Lufteintritt ueber undichte Fittings (Niederdruckseite)
3. Oelstand im Reservoir zu niedrig → Luft wird angesaugt
4. Kavitation in der Pumpe (Saugleitung zu eng oder verstopft)
5. Thermische Entgasung (Oel gibt bei hoher Temperatur geloeste Luft frei)

**Diagnose:**

```
1. Oelstand im Reservoir pruefen (muss im Markierungsbereich sein)
2. Alle Fittings auf Dichtheit pruefen (besonders Niederdruckseite)
3. Entlueftung durchfuehren (Schwerkraft-Methode)
4. Steuer auf Besserung pruefen
5. Falls keine Besserung: Druckentlueftung oder Vakuumentlueftung
6. Falls weiterhin schwammig: Pumpe auf interne Leckage pruefen
```

**AYDI-Score-Abzug:**

| Schwere | Beschreibung | Score-Abzug |
|---------|-------------|-------------|
| Leicht | Minimal schwammig, nur bei Aufmerksamkeit bemerkbar | -5 |
| Mittel | Deutlich schwammig, Ruder reagiert verzoegert | -20 |
| Schwer | Stark schwammig, Ruderwirkung eingeschraenkt | -40 |
| Kritisch | Kaum Ruderwirkung, Sicherheitsrisiko | -60 |

### 6.4 Fehlerbild F-HS-04: Schwergaengiges Steuer

**Beschreibung:** Das Steuerrad laesst sich nur mit erhoehtem Kraftaufwand drehen. Kann einseitig (nur in eine Richtung) oder beidseitig auftreten.

**Symptome:**
- Erhoehter Kraftaufwand am Steuerrad
- Steuer "klemmt" an bestimmten Positionen
- Geraeusche beim Lenken (Knirschen, Quietschen)
- Ungleichmaessiges Steuergefuehl

**Ursachen:**

| Ursache | Symptom | Pruefung |
|---------|---------|----------|
| Zu dickfluessiges Oel (falscher VG-Grad) | Beidseitig schwer, temperaturabhaengig | Oel-Viskositaet messen |
| Luftmangel im Reservoir (Unterdruck) | Beidseitig schwer, verschlimmert sich | Reservoir-Belueftung pruefen |
| Ruderschaftlager verschlissen | Einseitig schwerer, Geraeusche | Lagerung pruefen (Spiel, Korrosion) |
| Zylinder fehlausgerichtet | Klemmt in Endposition | Zylinder-Ausrichtung pruefen |
| Oel veraltet (Additive verbraucht) | Langsam zunehmend | Oel-Analyse |
| Pumpe verschlissen | Beidseitig, auch ohne Fahrt | Pumpe pruefen (Kolbenringe) |

**AYDI-Score-Abzug:**

| Schwere | Zusatz-Kraft | Score-Abzug |
|---------|-------------|-------------|
| Leicht | +20% Normalkraft | -5 |
| Mittel | +50% Normalkraft | -15 |
| Schwer | +100% (doppelte Kraft) | -30 |
| Kritisch | Einhaaendig nicht lenkbar | -50 |

### 6.5 Fehlerbild F-HS-05: Dichtungsversagen am Pumpengehaeuse

**Beschreibung:** Oelverlust an der Pumpe, typisch an Gehaeusedichtung, Wellenabdichtung oder Anschluessen.

**Visuelle Merkmale:**
- Oelfilm oder Tropfen am Pumpengehaeuse
- Oel am Steuerstandfuss (Pumpe ist meist direkt unter dem Steuerrad)
- Verfaerbung/Schmutzansammlung am Pumpengehaeuse durch Oelfilm

**Ursachen:**
1. Alterung der Gehaeusedichtung (O-Ring, Flachdichtung)
2. Verschleiss der Wellendichtung (Pumpenwelle zum Steuerrad)
3. Ueberdruck im System (defektes Druckbegrenzungsventil)
4. Vibration hat Fittings geloest
5. Frost-Schaeden (Wassereinschluss im Oel gefroren)

**Massnahmen:**

| Leckage-Ort | Massnahme | Kosten (ca.) |
|-------------|-----------|-------------|
| Fitting/Anschluss | Nachziehen, ggf. neuer O-Ring | 5–20 EUR |
| Gehaeusedichtung | Pumpe oeffnen, Dichtungssatz tauschen | 50–150 EUR |
| Wellendichtung | Wellendichtring tauschen (Spezialist) | 100–300 EUR |
| Gehaeuse gerissen | Pumpe austauschen | 500–2.000 EUR |

### 6.6 Fehlerbild F-HS-06: Oelverlust ohne sichtbare Leckage

**Beschreibung:** Oelstand im Reservoir sinkt, aber keine sichtbare Leckage an Zylinder, Pumpe oder Leitungen.

**Moegliche Ursachen:**
1. **Mikrobe Leckage an Fittings**: Oel kriecht entlang der Gewindeflanken und verdunstet
2. **Leckage in unzugaenglichem Bereich**: Zylinder hinter Verkleidung, Leitung unter Boden
3. **Interne Leckage in den Bilgenraum**: Oel sammelt sich in der Bilge
4. **Schlauch-Diffusion**: Sehr alte Thermoplast-Schlaeuche werden oeldurchlaessig
5. **Reservoir-Deckel undicht**: Oel verdunstet oder tritt an der Einfuelloeffnung aus

**Diagnose:**
1. Bilge auf Oelspuren pruefen
2. Alle Verkleidungen entfernen, Leitungen sichtbar machen
3. UV-Additiv ins Oel geben, nach 24 h mit UV-Lampe Leckage suchen
4. Druckhaltetest: System auf Betriebsdruck bringen, 30 min beobachten

### 6.7 Fehlerbild F-HS-07: Korrosion an Zylindergehaeuse

**Beschreibung:** Korrosionserscheinungen am Zylindergehaeuse, besonders an Aluminium-Zylindern in Salzwasser-Umgebung.

**Visuelle Merkmale:**
- Weisse, pulverfoermige Ablagerungen (Aluminiumoxid) am Gehaeuse
- Lochfrass-Korrosion (Pitting) an der Oberflaeche
- Galvanische Korrosion an Kontaktstellen zu anderen Metallen
- Aufquellung/Abloesung der Eloxalschicht

**Schweregrade:**

| Grad | Beschreibung | AYDI-Score-Abzug |
|------|-------------|------------------|
| 1 — Oberflaechlich | Leichte Verfaerbung, Oxidation | -3 |
| 2 — Maessig | Deutliche Oxidation, beginnender Pitting | -10 |
| 3 — Fortgeschritten | Tiefer Pitting, Materialabtrag messbar | -25 |
| 4 — Schwer | Strukturelle Integritaet gefaehrdet | -50 |

**Praevention:**
1. Anoden pruefen (Zinkanode am Zylinder, wo vorhanden)
2. Galvanische Isolation: Edelstahl-Fitting ←→ Aluminium-Gehaeuse mit Kunststoff-Buchse
3. Regemaessige Suesswasser-Spuelung des Aussenbereichs
4. Anti-Korrosions-Spray (ACF-50, Corrosion Block) auf ungeschuetzte Flaechen

### 6.8 Fehlerbild F-HS-08: Pumpen-Kavitation

**Beschreibung:** Die Pumpe erzeugt Geraeusche (Klackern, metallisches Klopfen, Pfeifen) und foerdert reduziert oder mit Luftblasen.

**Symptome:**
- Geraeusche bei schnellem Lenken
- Ruder "springt" statt sich gleichmaessig zu bewegen
- Schaumbildung im Reservoir
- Erhoehte Oeltemperatur

**Ursachen:**
1. Saugleitung zu eng (Innendurchmesser unterdimensioniert)
2. Saugleitung geknickt oder verstopft (Filtersieb im Reservoir zugesetzt)
3. Oelstand im Reservoir zu niedrig
4. Oel zu dickfluessig (falscher VG-Grad oder kaltes Oel)
5. Pumpendrehzahl zu hoch (bei Motorpumpen)
6. Luft im Saugsystem (undichte Verbindung vor Pumpe)

**Massnahmen:**
| Ursache | Massnahme | Prioritaet |
|---------|-----------|-----------|
| Saugleitung zu eng | Groesseren Durchmesser waehlen | Hoch |
| Leitung geknickt | Leitungsfuehrung korrigieren | Sofort |
| Filtersieb verstopft | Filter reinigen/tauschen | Hoch |
| Oelstand zu niedrig | Oel nachfuellen, Leckage suchen | Sofort |
| Falsches Oel | Oelwechsel mit korrektem VG-Grad | Mittel |

### 6.9 Fehlerbild F-HS-09: Ruder-Flattern (Rudder Flutter)

**Beschreibung:** Schnelle Schwingungen des Ruders bei hoher Fahrt, die sich als Vibrationen am Steuerrad bemerkbar machen.

**Symptome:**
- Vibrationen am Steuerrad bei Geschwindigkeit >10 kn
- Flatterndes Geraeusch aus dem Unterwasserbereich
- Ruder "schlaegt" gegen Anschlag bei hoher Fahrt
- Im Extremfall: Zylinderanschluesse loesen sich durch Vibration

**Ursachen (hydraulikseitig):**
1. Zylinder zu klein → System zu nachgiebig bei hoher Ruderlast
2. Luft im System → erhoehte Kompressibilitaet → Schwingungsneigung
3. Schlaeuche zu lang/weich → Volumenaufnahme unter Druck (Schlauchdehnung)
4. Zylinder-Befestigung lose → mechanisches Spiel

**Ursachen (ruderblatt-seitig, nicht Hydraulik):**
5. Ruderblatt-Profil ungeeignet (Stroemungsabriss)
6. Ruderschaftlager verschlissen (Spiel >1 mm)
7. Ruderblatt beschaedigt (Laminatschaden, Wassereinbruch)

**Massnahmen (Hydraulik):**
1. Entlueftung durchfuehren (Schwammigkeit beseitigen)
2. Schlaeuche durch Stahlrohre ersetzen (wo moeglich)
3. Groesseren Zylinder waehlen (hoehere Steifigkeit)
4. Zylinderhalterung pruefen und ggf. verstaerken
5. Druckspeicher einbauen (daempft Schwingungen)

### 6.10 Fehlerbild F-HS-10: Geraeuschentwicklung im System

**Beschreibung:** Unerwartete Geraeusche aus dem Hydrauliksystem — Pfeifen, Klopfen, Summen, Quietschen.

**Geraeusch-Diagnose:**

| Geraeusch | Typische Quelle | Ursache |
|-----------|-----------------|---------|
| Pfeifen/Zischen | Drosselstelle, Fitting, Ventil | Zu hohe Stroemungsgeschwindigkeit, Verengung |
| Klopfen/Klackern | Pumpe | Kavitation, Verschleiss, lose Teile |
| Summen/Brummen | Motorpumpe | Motor-Vibration, lose Befestigung |
| Quietschen | Kolbenstange, Lager | Trockenlauf, fehlende Schmierung |
| Knacken | Fitting, Rohr | Thermische Ausdehnung, Druckwechsel |
| Blubbern | Reservoir, Entlueftung | Luft im System, Kavitation |

### 6.11 Fehlerbild F-HS-11: Ueberdruckventil spricht an

**Beschreibung:** Das Ueberdruckventil (Druckbegrenzungsventil, Relief Valve) oeffnet sich waehrend des Betriebs. Erkennbar an ploetzlichem Nachlassen des Steuerwiderstands und ggf. Geraeusch.

**Symptome:**
- Steuer wird ploetzlich leicht (Druck faellt ab)
- Zischgeraeausch am Ventil
- Oeltemperatur steigt (Oel wird ueber Ventil entspannt → Waerme)
- Bei dauerhaftem Ansprechen: Oel schaeaumt, System ueberhitzt

**Ursachen:**
1. Zylinder/Ruder mechanisch blockiert → Druck steigt ueber Ansprechdruck
2. Ansprechdruck zu niedrig eingestellt
3. Ventil defekt (Feder gebrochen, Sitz verschmutzt)
4. System unterdimensioniert → Normaler Betriebsdruck nahe am Ansprechdruck

**Massnahmen:**
1. Ruder auf mechanische Blockierung pruefen (Fremdkoerper, Anschlag)
2. Ueberdruckventil-Einstellung pruefen (Herstellerangabe, typisch 1,5× Betriebsdruck)
3. Ventil reinigen oder tauschen
4. Systemdruck-Profil aufnehmen (Drucksensor + Logger)

### 6.12 Fehlerbild F-HS-12: Elektrische Stoerung bei Motorpumpen/Elektro-Hydraulik

**Beschreibung:** Motorpumpe laeuft nicht an, laeuft staendig, oder zeigt Fehlermeldungen.

**Fehlerkatalog Elektrik:**

| Symptom | Ursache | Pruefung | Massnahme |
|---------|---------|----------|-----------|
| Pumpe laeuft nicht | Sicherung defekt | Sicherungskasten pruefen | Sicherung tauschen |
| Pumpe laeuft nicht | Relais defekt | Relais bruecken (Test) | Relais tauschen |
| Pumpe laeuft nicht | Motor defekt | Spannung am Motor messen | Motor tauschen |
| Pumpe laeuft staendig | Druckschalter defekt | Schalter bruecken/trennen | Schalter tauschen |
| Pumpe laeuft staendig | Interne Leckage → Druck faellt | Druckabfalltest | Dichtungen tauschen |
| Pumpe dreht langsam | Spannung zu niedrig | Spannung unter Last messen | Kabelquerschnitt/Batterie |
| ECU Fehlermeldung | Software-/Hardware-Fehler | Fehlercode auslesen | Hersteller-Service |
| CAN-Bus Fehler | Kabelbruch, Terminierung | CAN-Bus-Diagnose | Kabel/Terminierung |

---

## 7. Troubleshooting-Entscheidungsbaeume

### 7.1 Entscheidungsbaum: Schwammiges Steuer

```
START: Steuer fuehlt sich schwammig an
│
├─ Oelstand im Reservoir pruefen
│  ├─ Zu niedrig → Oel nachfuellen + Entlueften
│  │  ├─ Besserung? → JA → Leckage suchen (Ursache fuer Oelverlust)
│  │  └─ Besserung? → NEIN → Weiter ↓
│  └─ Normal → Weiter ↓
│
├─ Entlueftung durchfuehren (Schwerkraft-Methode)
│  ├─ Besserung? → JA → Fertig (Luft war die Ursache)
│  └─ Besserung? → NEIN → Weiter ↓
│
├─ Druckentlueftung durchfuehren
│  ├─ Besserung? → JA → Fertig (eingeschlossene Luft war tiefer im System)
│  └─ Besserung? → NEIN → Weiter ↓
│
├─ Schlaeuche pruefen: Aufblaehung unter Druck?
│  ├─ JA → Schlaeuche tauschen (Innenseele delaminiert)
│  └─ NEIN → Weiter ↓
│
├─ Zylinder-Drift-Test durchfuehren
│  ├─ Drift >3°/10min → Interne Zylinder-Leckage → Dichtungssatz tauschen
│  └─ Drift <3°/10min → Weiter ↓
│
├─ Pumpe pruefen: Interne Leckage?
│  ├─ JA → Pumpe ueberholen oder tauschen
│  └─ NEIN → Weiter ↓
│
└─ Bypass-Ventil (Autopilot-Solenoid) pruefen
   ├─ Undicht → Solenoid-Ventil tauschen
   └─ Dicht → Systemauslegung ueberpruefen (Unterdimensionierung?)
```

### 7.2 Entscheidungsbaum: Steuer schwergaengig

```
START: Steuer laesst sich nur schwer drehen
│
├─ Schwergaengig in BEIDE Richtungen?
│  ├─ JA → Weiter ↓ (System-Problem)
│  └─ NEIN → Nur EINE Richtung schwer
│     ├─ Zylinderausrichtung pruefen → Fehlausrichtung? → Korrigieren
│     ├─ Ruderschaftlager pruefen → Verschlissen/blockiert? → Lager tauschen
│     └─ Zylinder-Endanschlag pruefen → Erreicht? → Hub/Anschlag einstellen
│
├─ Oel-Viskositaet pruefen (temperaturabhaengig?)
│  ├─ Oel zu dickfluessig (falscher VG-Grad) → Oelwechsel mit korrektem Grad
│  └─ Oel korrekt → Weiter ↓
│
├─ Oelstand im Reservoir pruefen
│  ├─ Zu hoch → Oel ablassen (Ueberdruck durch thermische Ausdehnung)
│  └─ Normal → Weiter ↓
│
├─ Reservoir-Belueftung pruefen (Entlueftungsbohrung im Deckel)
│  ├─ Verstopft → Reinigen (Unterdruck beim Pumpen war die Ursache)
│  └─ Frei → Weiter ↓
│
├─ Leitungen auf Knicke/Quetschungen pruefen
│  ├─ Gefunden → Leitung ersetzen
│  └─ OK → Weiter ↓
│
├─ Pumpe pruefen: Spielt, Geraeusche?
│  ├─ Verschlissen → Pumpe ueberholen/tauschen
│  └─ OK → Weiter ↓
│
└─ Ruderanlage mechanisch pruefen (ohne Hydraulik):
   ├─ Ruder schwer drehbar → Mechanisches Problem (Lager, Koker, Bewuchs)
   └─ Ruder leicht drehbar → Hydraulik-Problem nicht identifiziert → Fachbetrieb
```

### 7.3 Entscheidungsbaum: Oelverlust

```
START: Oelstand im Reservoir sinkt
│
├─ Sichtbare Leckage?
│  ├─ JA → Leckage lokalisieren
│  │  ├─ Am Zylinder → F-HS-01 (Externe Leckage Zylinder)
│  │  ├─ An der Pumpe → F-HS-05 (Pumpen-Leckage)
│  │  ├─ An Fittings → Nachziehen, O-Ringe pruefen
│  │  └─ Am Schlauch → Schlauch tauschen (SOFORT bei Riss/Blase)
│  │
│  └─ NEIN → Keine sichtbare Leckage
│     ├─ UV-Additiv einfuellen, 24 h warten, UV-Lampe nutzen
│     │  ├─ Leckage gefunden → Siehe oben
│     │  └─ Keine Leckage gefunden → Weiter ↓
│     │
│     ├─ Bilge auf Oel pruefen
│     │  ├─ Oel in Bilge → Versteckte Leckage an unzugaenglicher Stelle
│     │  └─ Keine Oel-Spuren → Weiter ↓
│     │
│     ├─ Druckhaltetest: System auf Betriebsdruck, 30 min messen
│     │  ├─ Druck faellt → Interne Leckage (Zylinder oder Pumpe)
│     │  └─ Druck stabil → Weiter ↓
│     │
│     └─ Reservoir-Deckel und Belueftung pruefen
│        ├─ Deckel undicht → Abdichten
│        └─ Schlauch-Diffusion bei sehr alten Schlaeuchen → Schlaeuche tauschen
```

### 7.4 Entscheidungsbaum: Motorpumpe funktioniert nicht

```
START: Motorpumpe laeuft nicht oder nicht korrekt
│
├─ Pumpe laeuft GAR NICHT
│  ├─ Spannung am Pumpenmotor messen
│  │  ├─ Keine Spannung → Sicherung pruefen → defekt? → Tauschen → laeuft?
│  │  │  ├─ JA → Ursache fuer Sicherungsausfall suchen (Kurzschluss?)
│  │  │  └─ NEIN → Relais pruefen → defekt? → Tauschen
│  │  │     ├─ JA → Fertig
│  │  │     └─ NEIN → Steuergeraet/Schalter pruefen
│  │  │
│  │  └─ Spannung vorhanden → Motor defekt
│  │     ├─ Motor dreht nicht → Buersten/Wicklung defekt → Motor tauschen
│  │     └─ Motor brummt, dreht nicht → Blockiert (Pumpe fest) → Pumpe pruefen
│  │
│  └─ Bei Elektro-Hydraulik: ECU Fehlercodes auslesen
│     ├─ CAN-Bus Fehler → Kabel und Terminierung pruefen
│     ├─ Sensor-Fehler → Ruderwinkel-Sensor pruefen
│     └─ Interner ECU-Fehler → Hersteller-Service
│
├─ Pumpe laeuft STAENDIG (schaltet nicht ab)
│  ├─ Druckschalter pruefen (sollte bei Erreichen des Solldrucks abschalten)
│  │  ├─ Druckschalter defekt → Tauschen
│  │  └─ Druckschalter OK → Weiter ↓
│  │
│  ├─ System erreicht keinen Druck → Leckage im System
│  │  ├─ Grosse Leckage → Sofort abstellen, Leckage suchen
│  │  └─ Kleine Leckage → Dichtungen, Fittings pruefen
│  │
│  └─ Ueberdruckventil oeffnet staendig → Einstellung pruefen
│
└─ Pumpe laeuft LANGSAM
   ├─ Spannung unter Last messen
   │  ├─ <10,5V (12V-System) → Batterie/Kabel → Aufladen, Kabelquerschnitt pruefen
   │  └─ Spannung OK → Motor-Buersten verschlissen → Motor ueberholen
   └─ Oel zu dickfluessig (Kaltstart) → Oel-Viskositaet pruefen
```

### 7.5 Entscheidungsbaum: Autopilot-Probleme

```
START: Autopilot steuert nicht korrekt
│
├─ AP steuert gar nicht
│  ├─ AP-Pumpe laeuft? 
│  │  ├─ NEIN → Siehe 7.4 (Motorpumpe funktioniert nicht)
│  │  └─ JA → Weiter ↓
│  │
│  ├─ Solenoid-Bypass-Ventil oeffnet?
│  │  ├─ NEIN → Solenoid pruefen (Spannung, Magnetspule, mechanisch verklemmt)
│  │  └─ JA → Weiter ↓
│  │
│  └─ AP-Pumpe foerdert? (Oelfluess am Zylinder pruefen)
│     ├─ NEIN → AP-Pumpe defekt (Kupplung, Kolben) → Tauschen
│     └─ JA → Hydraulik OK → AP-Elektronik pruefen (Kompass, Sensor, ECU)
│
├─ AP steuert ruckartig
│  ├─ Luft im AP-Kreis → AP-Kreis separat entlueften
│  ├─ AP-Pumpe zu gross → Volumenstrom am AP reduzieren (Drosselventil)
│  └─ Ruderwinkel-Sensor defekt → Sensor kalibrieren oder tauschen
│
├─ AP haelt Kurs nicht (Ruder driftet)
│  ├─ Solenoid-Bypass leckt → Solenoid tauschen
│  ├─ AP-Zylinder undicht → Dichtungen tauschen
│  └─ Interne Leckage Hauptzylinder → Hauptzylinder-Dichtungen pruefen
│
└─ AP "kaempft" gegen Handsteuerung
   ├─ Solenoid schliesst nicht richtig → Solenoid tauschen
   ├─ Rueckschlagventil in AP-Leitung defekt → Ventil tauschen
   └─ AP-Software: Handsteuer-Erkennung deaktiviert → Konfiguration pruefen
```

---

## 8. FAQ — Haeufig gestellte Fragen

### 8.1 Grundlagen

**F1: Ab welcher Bootsgroesse ist eine hydraulische Steuerung sinnvoll?**
A: Als Faustregel: ab 12 m LOA bei Segelyachten und ab 10 m LOA bei schnellen Motoryachten (>25 kn). Entscheidend ist nicht nur die Laenge, sondern die Ruderkraft. Uebersteigt diese 15 kN (was bei 10–12 m Booten bei Seegang und hoher Fahrt durchaus moeglich ist), wird Hydraulik empfohlen. Bei langsameren Verdraengern kann mechanische Steuerung bis 14 m funktionieren.

**F2: Was ist der Unterschied zwischen einer Handpumpe und einer Motorpumpe?**
A: Eine Handpumpe wird direkt vom Steuerrad angetrieben — jede Umdrehung erzeugt Oeldruck. Eine Motorpumpe hat einen Elektromotor (12V/24V/230V), der die Hydraulikpumpe antreibt. Das Steuerrad betaetigt nur ein Ventil, das die Richtung bestimmt. Handpumpen sind einfacher, wartungsaermer und energieautark. Motorpumpen sind leistungsfaehiger und ermoeglichen groessere Ruderkraefte.

**F3: Wie viele Umdrehungen Hart-ueber-Hart sind normal?**
A: Das haengt vom Pumpfoerdervolumen und Zylindervolumen ab. Typische Werte: 3–4 Umdrehungen bei Sportbooten, 4–5 bei Fahrtenseglern, 5–6 bei groesseren Yachten. Weniger Umdrehungen = schnelleres Ansprechen, aber hoehere Steuerradkraft. Mehr Umdrehungen = leichteres Steuer, aber langsameres Ansprechen.

**F4: Kann ich mein mechanisches Steuersystem auf Hydraulik umbauen?**
A: Ja, das ist einer der haeufigsten Umbauten. Erforderlich: Hydraulik-Zylinder am Ruderquadranten (statt Seilzugrollen), Handpumpe am Steuerstand, Leitungen dazwischen. Der Ruderquadrant muss oft getauscht oder angepasst werden. Kosten: 2.500–6.000 EUR je nach Bootsgroesse und Aufwand. Empfohlen: Fachbetrieb beauftragen.

**F5: Brauche ich eine Notsteuerung?**
A: Gemaess CE Kategorie A/B: Ja, fuer Yachten >12 m mit Hydrauliksteuerung. Auch ohne Klasse-Anforderung ist eine Notsteuerung dringend empfohlen. Optionen: Pinne direkt am Ruderschaft (setzt zugaenglichen Ruderkoker voraus), zweite Handpumpe am Hecksteuerstand, oder Zweikreis-System. AYDI bewertet das Fehlen einer Notsteuerung mit -30 Punkten im Sicherheits-Score.

### 8.2 Oel und Fluessigkeiten

**F6: Welches Oel soll ich verwenden?**
A: Immer die Hersteller-Empfehlung befolgen! Die meisten Segelyacht-Systeme (Jefa, Lewmar Classic, SeaStar) verwenden ISO VG 15. Motorpumpen-Systeme verwenden oft ISO VG 32 oder VG 46. Niemals verschiedene Oele mischen! Niemals ATF (Automatikgetriebe-Oel) verwenden, es sei denn, der Hersteller schreibt es explizit vor (einige aeltere Hynautic-Systeme).

**F7: Wie oft muss ich das Oel wechseln?**
A: Bei reinen Handpumpen-Systemen auf Segelyachten: alle 3–5 Jahre oder bei sichtbarer Verfaerbung. Bei Motorpumpen-Systemen: alle 250–500 Betriebsstunden oder 1–2 Jahre. Bei klassifizierten Yachten: jaehrlich. Eine Oel-Analyse (ca. 50 EUR im Labor) kann den optimalen Zeitpunkt bestimmen.

**F8: Kann ich normales Hydraulikoel aus dem Baumarkt verwenden?**
A: Technisch ja, wenn die ISO VG-Klasse stimmt und das Oel DIN 51524 Part 2 (HLP) entspricht. Marine-Hydraulikoele haben jedoch bessere Wassertoleranz und Korrosionsschutz-Additive. Fuer Yachten in Salzwasser-Revieren ist Marine-Oel empfohlen (Preisunterschied: ca. +30–50% gegenueber Standard-Industrieoel).

**F9: Mein Oel ist trueb/milchig — was bedeutet das?**
A: Truebung/Milchigkeit deutet auf Wassereinschluss hin (Emulsion). Ursachen: Kondensation im Reservoir (besonders bei grossen Temperaturunterschieden), undichte Dichtung an der Pumpen- oder Zylinderwelle, undichter Reservoir-Deckel. Massnahme: Sofortiger Oelwechsel. Oel mit >1.000 ppm Wasser schaedigt Dichtungen und foerdert Korrosion.

**F10: Mein Oel ist dunkel/schwarz — ist das schlimm?**
A: Leichte Dunkelfaerbung nach 1–2 Jahren ist normal (Additivabbau, Oxidation). Schwarzes Oel deutet auf starke Verunreinigung hin: metallischer Abrieb (Pumpe/Zylinder verschlissen), thermische Schaedigung (Ueberhitzung) oder extremes Alter. Eine Oel-Analyse klaert die Ursache. Im Zweifelsfall: Oelwechsel.

### 8.3 Entlueftung

**F11: Wie merke ich, dass Luft im System ist?**
A: Typische Zeichen: Schwammiges Steuergefuehl, Steuer hat "toten Bereich" (Weg ohne Ruderbewegung), Blubbern/Gurgeln im Reservoir, bei Motorpumpen: Schaumbildung. Im Extremfall: Steuerrad laesst sich drehen, ohne dass sich das Ruder bewegt.

**F12: Wie oft muss ich entlueften?**
A: Nach jeder Arbeit am System (Oelwechsel, Schlauchtausch, Zylindertausch): immer. Zum Saisonstart: empfohlen (kurze Schwerkraftentlueftung). Bei schwammigem Steuer: sofort. Bei einem dichten, unbeschaedigten System, das nie geoeffnet wurde: theoretisch nie.

**F13: Ich habe entlueftet, aber das Steuer ist immer noch schwammig — was nun?**
A: Moegliche Ursachen: Luft in einer "Tasche" (Hochpunkt in der Leitung), die durch Schwerkraft nicht erreichbar ist → Druckentlueftung versuchen. Alternativ: Schlaeuche haben sich gedehnt (Innenseele delaminiert) → Schlaeuche pruefen/tauschen. Oder: Interne Leckage in Zylinder/Pumpe → Drift-Test durchfuehren.

### 8.4 Installation und Dimensionierung

**F14: Wie lang duerfen die Leitungen sein?**
A: Theoretisch unbegrenzt, aber: Laengere Leitungen = mehr Oel im System = mehr Entlueftungsaufwand + hoeherer Druckverlust + langsameres Ansprechen. Faustregel: Druckleitung max. 15 m (Handpumpe), max. 25 m (Motorpumpe). Ruecklaufleitung: max. 20 m. Bei laengeren Wegen: Rohrleitung statt Schlauch (steifer, weniger Dehnung).

**F15: Kann ich Schlaeuche und Stahlrohre mischen?**
A: Ja, das ist Standard. Typische Installation: Stahlrohr fuer feste Strecken (entlang Rumpf, Schott-Durchfuehrungen), Schlauch fuer flexible Verbindungen (Zylinder-Anschluss, Pumpen-Anschluss, Uebergaenge mit Bewegung). Adapter: Schnaeidringverschraubung (Rohr) auf SAE-Fitting (Schlauch).

**F16: Welchen Querschnitt brauche ich fuer die Leitungen?**
A: Abhaengig vom Pumpen-Volumenstrom. Faustregel: 6 mm ID fuer kleine Handpumpen (bis 16 cm³/Umdr.), 8 mm ID fuer mittlere (16–28 cm³), 10 mm ID fuer grosse (28–50 cm³). Bei Motorpumpen: 10–16 mm ID. Die Ruecklaufleitung sollte eine Groesse groesser sein als die Druckleitung.

**F17: Darf ich die Leitung durch den Maschinenraum fuehren?**
A: Ja, aber mit Auflagen: Mindestabstand 100 mm zu heissen Teilen (Abgaskruemmer, Turbolader), Feuerschutzummantelung bei <200 mm Abstand, PTFE-Schlaeuche bei hoher Temperatur. Stahlrohr bevorzugt im Maschinenraum (Schlauch-Lebensdauer reduziert sich durch Hitze um 30–50%).

### 8.5 Wartung und Pflege

**F18: Was muss ich bei der jaehrlichen Wartung pruefen?**
A: Checkliste: (1) Oelstand und -farbe pruefen, (2) Alle Fittings auf Dichtheit sichtpruefen, (3) Schlaeuche auf Risse, Aufblaehung, Abrieb pruefen, (4) Kolbenstange auf Kratzer/Korrosion pruefen, (5) Pumpe auf Leckage pruefen, (6) Steuer auf Schwammigkeit testen, (7) Notsteuerung testen, (8) Bei Motorpumpen: Motor-Funktion und Drehzahl pruefen.

**F19: Wie lagere ich das Boot mit Hydrauliksteuerung ueber Winter?**
A: (1) Oelstand pruefen und ggf. auffuellen (nie mit niedrigem Stand ueberwintern → Kondensation). (2) Steuer in Mittelposition bringen (gleiche Belastung beider Seiten). (3) Zylinder-Kolbenstange mit duennem Oelfilm schuetzen (gegen Korrosion). (4) Reservoir-Belueftung gegen Feuchtigkeit schuetzen (nicht verschliessen, sondern Filter/Trockenmittel). (5) Bei Frost: Oel auf Wassergehalt pruefen (Wasser gefriert → Dichtungsschaden).

**F20: Wie lange halten die Komponenten?**
A: Typische Lebensdauer: Zylinder (Edelstahl): 20–30 Jahre. Zylinder (Aluminium): 10–15 Jahre. Handpumpe: 15–25 Jahre. Motorpumpe: 8–15 Jahre (Motor), 15–20 Jahre (Pumpenkoerper). Schlaeuche: 5–10 Jahre. Dichtungen: 3–7 Jahre. Oel: 1–5 Jahre (je nach System).

### 8.6 Kosten und Wirtschaftlichkeit

**F21: Was kostet eine komplett neue Hydrauliksteuerung?**
A: Abhaengig von Bootsgroesse und System: Basis-Handpumpe (10–14 m Segelboot): 1.500–3.500 EUR. Hochwertige Handpumpe (12–18 m Segelboot, Jefa): 3.000–6.000 EUR. Power-Assist (14–22 m): 5.000–10.000 EUR. Elektro-Hydraulisch (16–30 m): 8.000–20.000 EUR. Superyacht Zweikreis (24–60 m): 25.000–100.000+ EUR. Alle Preise inkl. Zylinder, Pumpe, Leitungen, Fittings, Oel, ohne Einbau.

**F22: Was kostet der Einbau durch eine Werft?**
A: Typische Arbeitszeiten: Handpumpen-System: 8–16 Stunden. Power-Assist: 16–24 Stunden. Elektro-Hydraulisch: 24–40 Stunden. Bei einem Stundensatz von 80–120 EUR ergibt sich: 640–4.800 EUR Einbaukosten. Dazu kommen Borddurchfuehrungen, Halterungen und Kleinmaterial.

**F23: Lohnt sich eine Ueberholung oder ein Neukauf?**
A: Faustregel: Wenn Ueberholungskosten >60% des Neusystems betragen → Neukauf. Ueberholung (Dichtungssatz, Oel, ggf. Kolbenstange polieren): 200–800 EUR. Neuer Zylinder: 500–3.000 EUR. Neue Pumpe: 400–2.500 EUR. Bei Zylindern >15 Jahre (Aluminium) oder >25 Jahre (Edelstahl): Neukauf empfohlen.

### 8.7 Spezialfragen

**F24: Kann ich meine Hydrauliksteuerung mit einem Joystick-System kombinieren?**
A: Ja, moderne Systeme wie SeaStar Optimus 360, Humphree, oder ZF-Mathers bieten Joystick-Steuerung mit Hydraulik-Aktuatoren. Voraussetzung: Proportionalventil-Steuerung (kein einfaches Schaltventil). Die Nachruestung an bestehende Systeme ist moeglich, erfordert aber eine ECU und kompatible Ventile.

**F25: Wie integriere ich Stabilisatoren in die Steuerhydraulik?**
A: Stabilisatoren (Flossenstabilisatoren) haben typischerweise ein eigenes Hydrauliksystem, das getrennt von der Steuerung laeuft. Grund: Stabilisatoren benoetigen hohe Volumenströme (50–100 l/min) bei moderatem Druck, die Steuerung benoetigt niedrige Volumenströme (2–15 l/min) bei hoeherem Druck. Bei Superyachten koennen beide Systeme ueber ein zentrales Hydraulik-Powerpack versorgt werden, mit getrennten Druckkreisen.

**F26: Was passiert bei einem Stromausfall mit meiner Elektro-Hydraulik-Steuerung?**
A: Bei Steer-by-Wire-Systemen ist ein Stromausfall ein kritisches Ereignis. ISO 25197 und alle Klassifikationsgesellschaften fordern: (a) unterbrechungsfreie Umschaltung auf Backup-Stromversorgung (UPS, Batterie), (b) manuelle Notsteuerung (Handpumpe mit Bypass). Die meisten Systeme (Lewmar Continuum, Optimus) haben integrierte Batterieueberbrueckung fuer min. 30 Minuten.

**F27: Wie teste ich mein System auf korrekte Funktion?**
A: Funktionstest vor jeder Ausfahrt: (1) Oelstand kontrollieren (Sichtglas/Peilstab), (2) Steuer von Anschlag zu Anschlag drehen — gleichmaessig, ohne Ruckeln, (3) Ruder-Endanschlag erreicht → Steuer wird fest (Anschlagdaempfung), (4) Steuer loslassen: Ruder bleibt in Position (kein Drift), (5) Bei Motorpumpe: Pumpe laeuft an, schaltet ab.

**F28: Kann ich mein System selbst warten?**
A: Ja, viele Wartungsarbeiten sind fuer versierte Eigner machbar: Oelstand pruefen/nachfuellen, Entlueften (Schwerkraft-Methode), Sichtkontrolle aller Komponenten, Oelwechsel. Komplexere Arbeiten (Dichtungstausch Zylinder, Pumpen-Ueberholung, Druckentlueftung) erfordern Spezialwerkzeug und Erfahrung — hier wird ein Fachbetrieb empfohlen.

### 8.8 Sonderthemen

**F29: Gibt es umweltfreundliche Hydraulikoele fuer Yachten?**
A: Ja, biologisch abbaubare Hydraulikoele auf Basis synthetischer Ester (z.B. Shell Naturelle HF-E, Panolin HLP SYNTH) sind erhaeltlich. Sie sind teurer (+50–100%) und haben teilweise eingeschraenkte Dichtungsvertraeglichkeit (FKM-Dichtungen statt NBR erforderlich). Fuer Binnengewaesser und Naturschutzgebiete empfehlenswert.

**F30: Was ist der Unterschied zwischen Helm Pump, Power Assist und Full Power?**
A: Helm Pump = reine Handpumpe, alle Kraft kommt vom Steuermann. Power Assist = Handpumpe + Motorpumpe, Motor unterstuetzt bei hoher Last. Full Power = Motorpumpe arbeitet allein, Steuerrad betaetigt nur ein Ventil. Die Uebergaenge sind fliessend — manche Power-Assist-Systeme arbeiten bei geringer Last wie eine Handpumpe und bei hoher Last wie Full Power.

**F31: Wie pruefe ich, ob mein System den korrekten Druck aufbaut?**
A: Fuer eine Druckmessung wird ein Manometer (0–100 bar, Anschluss 1/4" oder 3/8" SAE) am T-Stueck zwischen Pumpe und Zylinder angeschlossen. Steuer langsam bis zum Anschlag drehen — der Druck steigt. Bei Handpumpen sollte der Maximaldruck 60–80% des Nenndrucks der Pumpe betragen. Bei Motorpumpen: Druck sollte den Abschaltdruck des Druckschalters erreichen. Liegt der Druck deutlich unter dem Sollwert: interne Leckage (Pumpe oder Zylinder) oder Ueberdruckventil oeffnet zu frueh.

**F32: Was bedeutet "Bypass-Ventil" und wann brauche ich eines?**
A: Ein Bypass-Ventil ist ein Ventil, das einen Hydraulikkreis umgeht ("ueberbrueckt"). Es gibt verschiedene Einsaetze: (a) **Autopilot-Bypass**: Oeffnet den Handpumpenkreis, damit der AP den Zylinder ansteuern kann. (b) **Not-Bypass**: Ermoeglicht Handsteuerung, wenn Motorpumpe ausfaellt. (c) **Freilauf-Bypass**: Ermoeglicht freie Ruderbewegung zum Schleppen oder bei Motorausfall. Jedes System mit Autopilot benoetigt ein Bypass-Ventil.

**F33: Kann Frost mein Hydrauliksystem schaedigen?**
A: Ja, indirekt. Reines Hydraulikoel gefriert erst bei ca. -30 bis -50°C (je nach VG-Grad), aber: Wenn Wasser im System ist (Kondensation), kann dieses Wasser ab 0°C gefrieren und Dichtungen von innen beschaedigen. Bei Frostgefahr: Oelstand pruefen (vollstaendiges System = weniger Kondensation), Oelanalyse auf Wasser durchfuehren, ggf. Oelwechsel. Zusaetzlich: Dickfluessiges Oel bei Kaelte = erhoehte Steuerkraefte. VG 15 bleibt bis ca. -15°C gut pumpbar, VG 46 kann ab 0°C problematisch werden.

**F34: Mein Boot hat zwei Steuerstaende — wie funktioniert das hydraulisch?**
A: Zwei Steuerstaende mit jeweils einer Handpumpe, verbunden durch Leitungen zum gleichen Zylinder. Wenn an einem Stand gesteuert wird, muss das Oel durch die andere Pumpe hindurchfliessen — das erfordert ein **Helm-Bypass-Ventil** (auch "Cross-over Valve") an jeder Pumpe. Dieses oeffnet, wenn die Pumpe nicht aktiv gedreht wird, und laesst das Oel passieren. Ohne Helm-Bypass: Das zweite Steuerrad blockiert das System. Bei Motorpumpen und Elektro-Hydraulik ist Dual-Station einfacher: Beide Steuerraeder senden nur Steuersignale an die ECU.

**F35: Wie hoch ist der Stromverbrauch einer Motorpumpe?**
A: Abhaengig von Groesse und Einsatz. Typische Werte: 12V-Systeme (10–18 m): 15–50 A bei Betaetigung, 0 A im Standby. 24V-Systeme (16–30 m): 10–40 A bei Betaetigung. Die Pumpe laeuft nicht dauerhaft, sondern nur bei Steuerbewegung. Typischer Durchschnittsverbrauch auf Fahrt: 2–10 Ah/Stunde (Motoryacht), 0,5–3 Ah/Stunde (Segelyacht). Fuer die 24V-Bordnetz-Dimensionierung: Spitzenstrom der Pumpe als Dauerverbraucher fuer 15 Minuten (Hafenmanoever) einrechnen.

---

## 9. Glossar

### 9.1 Begriffe A–Z

| Nr. | Begriff | Erklaerung |
|-----|---------|------------|
| 1 | **Abstreifer (Wiper Seal)** | Dichtring an der Kolbenstange, der Schmutz und Wasser fernhaelt |
| 2 | **Ansprechdruck** | Druck, bei dem ein Ueberdruckventil oeffnet |
| 3 | **Autopilot-Bypass** | Solenoidventil, das den Handpumpen-Kreislauf oefffnet, wenn der AP aktiv ist |
| 4 | **Berstdruck (Burst Pressure)** | Druck, bei dem eine Komponente zerstoert wird — Sicherheitsfaktor = Berstdruck / Betriebsdruck |
| 5 | **Betriebsdruck (Working Pressure)** | Maximaler Dauerdruck im Normalbetrieb |
| 6 | **Bypass-Ventil** | Ventil, das einen Kreislauf umgeht (z.B. fuer Autopilot oder Notsteuerung) |
| 7 | **CAN-Bus** | Controller Area Network — Datennetzwerk fuer maritime Steuergeraete |
| 8 | **Dichtungslippe** | Aktive Dichtflaeche eines Radialwellendichtrings |
| 9 | **Druckbegrenzungsventil (Relief Valve)** | Begrenzt den Maximaldruck im System zum Schutz vor Ueberlastung |
| 10 | **Druckhaltetest** | Pruefung der Dichtheit: System unter Druck setzen und Druckverlauf messen |
| 11 | **Druckverlust (Pressure Drop)** | Druckabfall durch Reibung in Leitungen und Fittings |
| 12 | **Entlueftung (Bleeding)** | Entfernen von Lufteinschluessen aus dem Hydrauliksystem |
| 13 | **FKM (Viton)** | Fluorelastomer-Dichtungsmaterial, temperaturbest. bis 200°C |
| 14 | **Fluegelzellenpumpe (Vane Pump)** | Pumpe mit rotierenden Fluegeln in einem exzentrischen Gehaeuse |
| 15 | **Force Feedback** | Kuenstliche Rueckmeldung am Steuerrad bei Steer-by-Wire-Systemen |
| 16 | **Hart-ueber-Hart (Lock to Lock)** | Voller Ruderausschlag von einem Extrem zum anderen |
| 17 | **Helm Pump** | Steuerradpumpe — Handpumpe direkt am Steuerrad |
| 18 | **HLP-Oel** | Hydraulikoel mit Hochdruck-Additiven gemaess DIN 51524 Part 2 |
| 19 | **Hub (Stroke)** | Maximaler Verfahrweg des Zylinderkolbens |
| 20 | **Hydraulikzylinder (Actuator)** | Wandelt Oeldruck in mechanische Linearbewegung am Ruder um |
| 21 | **ISO VG (Viskositaetsgrad)** | Klassifikation der Oelviskositaet nach ISO 3448 |
| 22 | **Kavitation** | Bildung und Zusammenfall von Dampfblasen durch lokalen Unterdruck in der Fluessigkeit |
| 23 | **Kolbenstange (Piston Rod)** | Verbindungselement zwischen Kolben und Ruderquadrant/Ruderarm |
| 24 | **Kompressibilitaet** | Mass fuer die Zusammendrueckbarkeit einer Fluessigkeit (Oel: gering, Luft: hoch) |
| 25 | **Lateralplan** | Projizierte Unterwasserflaeche eines Bootes in Seitenansicht |
| 26 | **NBR (Nitrilkautschuk)** | Standard-Dichtungsmaterial fuer Hydraulik, oelbestaendig, -30 bis +100°C |
| 27 | **NMEA 2000** | Marinespezifisches Datennetzwerk (CAN-Bus-basiert) fuer Navigations- und Steuergeraete |
| 28 | **Notsteuerung (Emergency Steering)** | Redundantes Steuersystem fuer den Ausfall der Hauptsteuerung |
| 29 | **O-Ring** | Dichtring mit kreisrundem Querschnitt (statische oder dynamische Abdichtung) |
| 30 | **Pascalsches Prinzip** | Druck breitet sich in einer eingeschlossenen Fluessigkeit gleichmaessig in alle Richtungen aus |
| 31 | **Power-Assist** | Kombination aus Hand- und Motorpumpe mit automatischer Zuschaltung |
| 32 | **Proportionalventil** | Ventil, das den Oelstrom stufenlos regelt (im Gegensatz zu Schaltventil: nur auf/zu) |
| 33 | **PTFE (Teflon)** | Polytetrafluorethylen — Dichtungs- und Fuehrungsmaterial, extrem reibungsarm |
| 34 | **Quadrant (Tiller Arm)** | Hebel am Ruderschaft, an dem der Zylinder angreift |
| 35 | **Ruderkoker (Rudder Trunk)** | Rohrdurchfuehrung des Ruderschafts durch den Rumpfboden |
| 36 | **Ruderschaft (Rudder Stock)** | Vertikale Welle, die das Ruderblatt traegt und die Drehbewegung uebertraegt |
| 37 | **SAE J1942** | Marine-spezifische Norm fuer Hydraulikschlaeuche und -verbindungen |
| 38 | **Schnaeidringverschraubung** | Leitungsverbindung mit konischem Schneidring (DIN 2353/ISO 8434) |
| 39 | **Solenoid-Ventil** | Elektrisch betaetigtes Magnetventil (auf/zu oder proportional) |
| 40 | **Steer-by-Wire** | Elektronische Steuerung ohne mechanische Verbindung Steuerrad→Ruder |
| 41 | **Totvolumen** | Oelvolumen in Leitungen und Fittings zwischen Pumpe und Zylinder |
| 42 | **Viskositaetsindex (VI)** | Mass fuer die Temperaturabhaengigkeit der Oelviskositaet (hoch = stabil) |
| 43 | **Volumenstrom (Flow Rate)** | Oelmenge pro Zeiteinheit [l/min oder cm³/s] |
| 44 | **Zweikreis-System (Dual Circuit)** | Redundantes System mit zwei unabhaengigen Hydraulikkreisen |
| 45 | **Zylinderbohrung (Bore)** | Innendurchmesser des Zylinderrohrs — bestimmt die Kolbenflaeche und damit die Kraft |
| 46 | **Druckspeicher (Accumulator)** | Speichert Druckenergie und daempft Druckspitzen im Hydrauliksystem |
| 47 | **Edelstahl 316L** | Austenitischer Chrom-Nickel-Molybdaen-Stahl, Standardmaterial fuer marine Hydraulikzylinder |
| 48 | **Exzenter** | Nocken an der Pumpenwelle, der die Drehbewegung in eine Kolbenbewegung umsetzt |
| 49 | **Filtersieb (Strainer)** | Grobfilter im Reservoir, verhindert Partikelansaugung in die Pumpe |
| 50 | **Galvanische Korrosion** | Elektrochemische Korrosion an der Kontaktstelle verschiedener Metalle in Elektrolyt (Salzwasser) |
| 51 | **Hagen-Poiseuille-Gleichung** | Berechnung des Druckverlustes in laminarer Rohrstroemung |
| 52 | **ISO 10592** | Internationale Norm fuer hydraulische Steueranlagen auf Sportbooten |
| 53 | **Kolbendichtung (Piston Seal)** | Dichtring zwischen Kolben und Zylinderrohr, trennt die beiden Oelkammern |
| 54 | **Leckoel** | Oel, das durch interne Spalte von der Hochdruckseite zur Niederdruckseite uebergeht |
| 55 | **Manometer** | Druckmessgeraet zur Pruefung des Systemdrucks |
| 56 | **Nennweite (DN)** | Normierte Groessenbezeichnung fuer Rohre und Fittings (z.B. DN6 = ca. 6 mm ID) |
| 57 | **Oelkuehler (Oil Cooler)** | Waermetauscher zur Kuehlung des Hydraulikoels (Luft-Oel oder Wasser-Oel) |
| 58 | **Rueckschlagventil (Check Valve)** | Ventil, das Oelfluss nur in eine Richtung zulaesst |
| 59 | **Sicherheitsfaktor (Safety Factor)** | Verhaeltnis von maximal zulaessiger Last zu tatsaechlicher Last — min. 1,5 bei Zylindern |
| 60 | **Woehler-Kurve** | Zusammenhang zwischen Lastwechselzahl und zulaessiger Spannungsamplitude (Ermuedungsberechnung) |

### 9.2 Abkuerzungen

| Abkuerzung | Bedeutung |
|-----------|-----------|
| AP | Autopilot |
| ABYC | American Boat & Yacht Council |
| BV | Bureau Veritas |
| CAN | Controller Area Network |
| CE | Conformité Européenne |
| DNV-GL | Det Norske Veritas — Germanischer Lloyd |
| ECU | Electronic Control Unit |
| FKM | Fluorkautschuk (Viton) |
| GFK | Glasfaserverstaerkter Kunststoff |
| H-u-H | Hart-ueber-Hart (Lock to Lock) |
| HLP | Hydraulikoel mit Hochdruck-Additiven (DIN 51524) |
| HP | Handpumpe (Helm Pump) |
| HPC | High Performance Cylinder |
| HSC | Hydraulic Steering Cylinder |
| HTP | Hydraulic Tilt & Power |
| ID | Innendurchmesser |
| ISO | International Organization for Standardization |
| LOA | Length Overall (Laenge ueber alles) |
| LR | Lloyd's Register |
| MP | Motorpumpe |
| NBR | Acrylnitril-Butadien-Kautschuk (Nitrilkautschuk) |
| NMEA | National Marine Electronics Association |
| OD | Aussendurchmesser |
| PA | Power-Assist |
| PTFE | Polytetrafluorethylen (Teflon) |
| RINA | Registro Italiano Navale |
| SAE | Society of Automotive Engineers |
| SF | Sicherheitsfaktor (Safety Factor) |
| VG | Viskositaetsgrad (ISO 3448) |
| VI | Viskositaetsindex |

---

## 10. Schnell-Referenz

### 10.1 Schnell-Dimensionierung nach Bootsgroesse

| LOA [m] | Typ | Ruderkraft_max [kN] | Empfohlener Zylinder | Empfohlene Pumpe | Leitungs-ID [mm] | Oel |
|---------|-----|---------------------|---------------------|------------------|-------------------|-----|
| 8–10 | Segel | 8 | 40×100 mm | 14 cm³/U | 6 | VG 15 |
| 10–12 | Segel | 12 | 40×120 mm | 14 cm³/U | 6 | VG 15 |
| 12–14 | Segel | 18 | 50×130 mm | 16 cm³/U | 8 | VG 15 |
| 14–16 | Segel | 25 | 50×160 mm | 22 cm³/U | 8 | VG 15 |
| 16–18 | Segel | 35 | 65×160 mm | 22 cm³/U | 10 | VG 15 |
| 18–22 | Segel | 50 | 65×200 mm | 28 cm³/U + PA | 10 | VG 15/32 |
| 22–26 | Segel | 70 | 80×200 mm | 36 cm³/U + MP | 12 | VG 32 |
| 26–30 | Segel | 100 | 100×250 mm | MP 8 l/min | 12 | VG 32 |
| 10–14 | Motor | 20 | 50×130 mm | 16 cm³/U + PA | 8 | VG 15 |
| 14–18 | Motor | 40 | 65×160 mm | MP 4 l/min | 10 | VG 32 |
| 18–24 | Motor | 65 | 80×200 mm | MP 8 l/min | 12 | VG 32 |
| 24–35 | Motor | 120 | 100×300 mm | MP 15 l/min | 16 | VG 46 |
| 35–45 | Motor | 200 | 125×350 mm | MP 25 l/min | 16 | VG 46 |
| 45–60 | Motor | 250+ | 150×400 mm | MP 40 l/min | 20 | VG 46 |

*PA = Power-Assist, MP = Motorpumpe*

### 10.2 Wartungsintervall-Schnellreferenz

| Komponente | Pruefen | Warten | Tauschen |
|-----------|---------|--------|----------|
| Oelstand | Vor jeder Fahrt | — | — |
| Oelqualitaet | Saisonstart | Oelwechsel alle 1–5 J. | Bei Verunreinigung |
| Zylinder-Dichtung | Jaehrlich (Sicht) | — | Alle 5–8 Jahre |
| Kolbenstange | Jaehrlich (Sicht) | Einfetten bei Winterlager | Bei Korrosion/Kratzer |
| Schlaeuche | Halbjährlich | — | Alle 5–8 Jahre |
| Fittings | Jaehrlich | Nachziehen | Bei Korrosion |
| Pumpe | Jaehrlich (Funktion) | — | Alle 10–20 Jahre |
| Entlueftung | Saisonstart | Nach jeder Systemarbeit | — |
| Notsteuerung | Halbjährlich (Test) | — | — |
| Autopilot-Bypass | Jaehrlich (Funktion) | — | Alle 8–12 Jahre |

### 10.3 Umrechnungstabelle

| Von | Nach | Faktor |
|-----|------|--------|
| bar | Pa | × 100.000 |
| bar | psi | × 14,504 |
| psi | bar | × 0,0689 |
| kN | kgf | × 101,97 |
| Nm | kgf·m | × 0,10197 |
| l/min | cm³/s | × 16,667 |
| cm³ | in³ | × 0,06102 |
| mm | inch | × 0,03937 |

### 10.4 Oelvergleichstabelle

| Hersteller | VG 15 | VG 32 | VG 46 |
|-----------|-------|-------|-------|
| Shell | Tellus S2 M 15 | Tellus S2 M 32 | Tellus S2 M 46 |
| Mobil | DTE 21 | DTE 24 | DTE 25 |
| Total | Azolla ZS 15 | Azolla ZS 32 | Azolla ZS 46 |
| Castrol | Hyspin AWH-M 15 | Hyspin AWH-M 32 | Hyspin AWH-M 46 |
| BP | Bartran HV 15 | Bartran HV 32 | Bartran HV 46 |
| Fuchs | Renolin MR 15 | Renolin MR 32 | Renolin MR 46 |
| Jefa | HO-15 | — | — |
| SeaStar | HA5430 (≈VG 15) | — | — |

### 10.5 Normen-Schnellreferenz

| Norm | Kurzbezeichnung | Wesentlicher Inhalt |
|------|-----------------|---------------------|
| ISO 10592 | Hydraulische Steueranlagen | Hauptnorm: Druck, Hub, Dichtheit, Materialien |
| ISO 25197 | Elektronische Steuersysteme | Steer-by-Wire, ECU, Redundanz |
| ISO 12217 | Stabilitaet | Gewichtsverteilung (beeinflusst Zylinder-Platzierung) |
| ISO 9094 | Brandschutz | Mindestabstaende Hydraulikleitung↔Waermequelle |
| SAE J1942 | Marine-Hydraulikschlaeuche | Schlauch-Spezifikation fuer Salzwasser-Umgebung |
| DIN 51524-2 | HLP-Hydraulikoel | Mindestanforderung an Hydraulikoel |
| ABYC P-21 | Manual and Assisted Hydraulic Steering Systems | US-Norm fuer hydraulische Steueranlagen |
| ABYC H-30 | Hydraulic Systems | US-Norm fuer allgemeine Hydraulik |

---

## 11. ANHANG A–H: Fallstudien

### ANHANG A — Fallstudie: Bavaria 46 Cruiser — Umruestung mechanisch auf hydraulisch

**Ausgangslage:**
- Boot: Bavaria 46 Cruiser, Baujahr 2008, LOA 14,27 m
- Originalsystem: Whitlock Cobra mechanische Steuerung (Seilzug + Kette)
- Problem: Steuer schwergaengig, Seilzug gedehnt, Kette verschlissen
- Eigner wuenscht Autopilot-Integration (Raymarine Evolution EV-400)

**Analyse durch AYDI:**
- Ruderkraft berechnet: 22 kN bei 7 kn, 15° Ruderwinkel
- Ruder-Drehmoment: 1.800 Nm
- Ruderquadrant-Radius: 120 mm (Whitlock-Quadrant passt fuer Hydraulik)
- Erforderliche Zylinderkraft: 15.000 N → Jefa HSC 50-130 (13,7 kN bei 70 bar)
- Sicherheitsfaktor: 13.700 × 0,120 / 1.800 = 0,91 → UNZUREICHEND
- Korrektur: Jefa HSC 65-160 (23,2 kN bei 70 bar) → SF = 23.200 × 0,120 / 1.800 = 1,55 → OK

**Gewaehlt:**
| Komponente | Modell | Preis |
|-----------|--------|-------|
| Zylinder | Jefa HSC 65-160 | 1.850 EUR |
| Pumpe | Jefa HP 22 | 980 EUR |
| Leitungs-Kit | 2× 8 mm SAE 100R7, je 6 m | 320 EUR |
| Fittings | Diverse Schnaeidring + SAE | 180 EUR |
| Oel | Jefa HO-15, 5 Liter | 42 EUR |
| Quadrant-Adapter | Jefa QA-65 | 280 EUR |
| AP-Bypass | Jefa ABV-12 (12V Solenoid) | 195 EUR |
| **Gesamt Material** | | **3.847 EUR** |
| Einbau (Werft, 14 h × 95 EUR) | | 1.330 EUR |
| **Gesamtkosten** | | **5.177 EUR** |

**AYDI-Bewertung nach Umruestung:**
| Dimension | Score | Bemerkung |
|-----------|-------|-----------|
| Dimensionierung | 88 | Gut dimensioniert, SF 1,55 |
| Zustand | 100 | Neuinstallation |
| Sicherheit | 72 | Notsteuerung fehlt (Empfehlung: Notpinne) |
| Installation | 90 | Fachgerechte Leitungsfuehrung |
| Wartungszustand | 100 | Neu |
| **Gesamt** | **90** | |

### ANHANG B — Fallstudie: Hallberg-Rassy 48 — Routinewartung nach 8 Jahren

**Ausgangslage:**
- Boot: Hallberg-Rassy 48 Mk II, Baujahr 2016, LOA 14,98 m
- Originalsystem: Jefa HSC 65-200 + HP 22 + Raymarine Type 1 AP-Pumpe
- Einsatz: 400 Seemeilen/Jahr, Ostsee + Mittelmeer
- Letzte Wartung: 3 Jahre her (Oelwechsel)

**Befunde bei Inspektion:**
1. Oelfarbe: Leicht bernsteinfarben (normal nach 3 Jahren)
2. Oelstand: 5 mm unter Maximum (minimal, akzeptabel)
3. Kolbenstange: Leichte Verfaerbung, kein Pitting, kein Kratzer
4. Schlaeuche: Keine Risse, keine Aufblaehung, leicht staubig
5. Fittings: Trocken, keine Leckage
6. Steuergefuehl: Leicht schwammig (Luft nach 3 Jahren plausibel)
7. Drift-Test: 0,8° in 10 Minuten (normal)
8. AP-Solenoid: Schaltet sauber, keine Leckage

**Massnahmen:**
| Massnahme | Dringlichkeit | Kosten |
|-----------|---------------|--------|
| Oelwechsel (VG 15, 3 Liter) | Empfohlen | 35 EUR |
| Entlueftung (Schwerkraft) | Empfohlen | 0 EUR (Eigenleistung) |
| Kolbenstange reinigen + duenn oelen | Optional | 5 EUR |
| — | — | — |
| Naechste planmaessige Wartung: Dichtungssatz in 2–3 Jahren | Planen | 180 EUR |

**AYDI-Bewertung:**
| Dimension | Score | Bemerkung |
|-----------|-------|-----------|
| Dimensionierung | 92 | Original Jefa, korrekt fuer Boot |
| Zustand | 85 | Leichte Schwammigkeit, sonst gut |
| Sicherheit | 78 | Notpinne vorhanden (Standard HR 48) |
| Installation | 95 | Werftinstallation HR |
| Wartungszustand | 80 | Oelwechsel 1 Jahr ueberfaellig |
| **Gesamt** | **86** | |

### ANHANG C — Fallstudie: Beneteau Oceanis 51.1 — Leckage am Zylinder

**Ausgangslage:**
- Boot: Beneteau Oceanis 51.1, Baujahr 2019, LOA 15,99 m
- System: Jefa HSC 65-160 + HP 22
- Symptom: Oelfleck unter dem Zylinder, Oelstand sinkt alle 2 Wochen um 10 mm

**AYDI-Diagnose:**
- Fehlerbild F-HS-01 (Externe Leckage Zylinder), Schweregrad "Mittel"
- Kolbenstange sichtbar: Duenner Oelfilm, beginnende Tropfenbildung
- Ursache: Kolbenstangendichtung verhaertet (Boot stand 2 Jahre ungenutzt waehrend Pandemie → NBR altert schneller ohne Oel-Kontakt)
- Drift-Test: 2,1° in 10 min → Beginnende interne Leckage

**Massnahmen:**
| Massnahme | Durchfuehrung | Kosten |
|-----------|---------------|--------|
| Zylinder ausbauen | Werft | Inkl. |
| Dichtungssatz komplett tauschen (Stangendichtung + Kolbendichtung) | Werft | 165 EUR (Jefa Seal Kit HSC-65) |
| Kolbenstange pruefen (Oberflaeche, Rundlauf) | Werft | Inkl. |
| Kolbenstange polieren (leichte Oxidation) | Werft | 80 EUR |
| Oelwechsel mit Entlueftung | Werft | 55 EUR |
| Arbeitszeit (6 h × 95 EUR) | Werft | 570 EUR |
| **Gesamt** | | **870 EUR** |

**AYDI-Bewertung nach Reparatur:**
| Dimension | Score |
|-----------|-------|
| Dimensionierung | 90 |
| Zustand | 95 |
| Sicherheit | 68 (keine Notsteuerung dokumentiert) |
| Installation | 88 |
| Wartungszustand | 90 |
| **Gesamt** | **87** |

### ANHANG D — Fallstudie: Sunseeker Manhattan 60 — Zweikreis-Upgrade

**Ausgangslage:**
- Boot: Sunseeker Manhattan 60, Baujahr 2014, LOA 19,15 m
- Originalsystem: Einzelkreis-Motorpumpe (Hydraulik-Powerpack Vetus HTP 80)
- Anforderung: DNV-GL Klassierung geplant → Zweikreis erforderlich

**Systemdesign:**

```
Kreis 1 (Original):
  Pumpe: Vetus HTP 80 (bleibt)
  Zylinder: Vetus 89×203 mm (bleibt, Port A/B)

Kreis 2 (Neu):
  Pumpe: Vetus HTP 60 (neu)
  Anschluss: Ueber Umschaltventil an gleichen Zylinder (Port C/D, neue Ports)

Umschaltlogik:
  Druckwachter an Kreis 1: <20 bar → Kreis 2 aktiviert (automatisch)
  Manuelle Umschaltung am Hauptsteuerstand moeglich
  Umschaltzeit: <3 Sekunden
```

**Kosten:**
| Position | Kosten |
|----------|--------|
| Vetus HTP 60 (komplett) | 4.200 EUR |
| Umschaltventilblock (Sonderanfertigung) | 2.800 EUR |
| Leitungen Kreis 2 (12 mm, 2×15 m) | 680 EUR |
| Druckwaechter + Steuerung | 950 EUR |
| Zweites Oelreservoir + Halterung | 380 EUR |
| Einbau (Werft, 32 h × 110 EUR) | 3.520 EUR |
| DNV-GL Abnahme | 2.200 EUR |
| **Gesamt** | **14.730 EUR** |

**AYDI-Bewertung nach Upgrade:**
| Dimension | Score |
|-----------|-------|
| Dimensionierung | 85 |
| Zustand | 78 (Kreis 1 ist 10 Jahre alt) |
| Sicherheit | 95 (Zweikreis + automatische Umschaltung) |
| Installation | 88 |
| Wartungszustand | 82 |
| **Gesamt** | **86** |

### ANHANG E — Fallstudie: Dehler 46 SQ — Performance-Steuerung mit Autopilot

**Ausgangslage:**
- Boot: Dehler 46 SQ, Baujahr 2021, LOA 14,38 m
- Anforderung: Praezise Steuerung fuer Regatta + Langfahrt-Autopilot
- System: Jefa HPC 50-130 + HP 16 + B&G Pilot Hydraulikpumpe

**Besonderheiten:**
- HPC-Zylinder (High Performance): Hoehere Druckstufe (112 bar) fuer direkteres Ansprechverhalten
- Weniger Hub = schnelleres Ruderlegen (Regatta-Optimierung)
- B&G Pilot Pump Type 2: Foerdervolumen 30 cm³/s, optimiert fuer schnelle kleine Korrekturen
- Ruder-Feedback-Einheit: B&G RF45 am Ruderquadranten → praezise Ruderwinkel-Anzeige

**AYDI-Bewertung:**
| Dimension | Score |
|-----------|-------|
| Dimensionierung | 95 (Performance-optimiert) |
| Zustand | 100 (Neu) |
| Sicherheit | 70 (keine separate Notsteuerung) |
| Installation | 93 |
| Wartungszustand | 100 |
| **Gesamt** | **92** |

### ANHANG F — Fallstudie: Oyster 745 — Langfahrt-Hydraulik nach 12 Jahren

**Ausgangslage:**
- Boot: Oyster 745, Baujahr 2012, LOA 22,55 m
- System: Jefa HSC 80-250 + HP 28 (Handpumpe) + Lecomble & Schmitt Motorpumpe (Power-Assist) + Autopilot
- Einsatz: 3.500 sm/Jahr, transatlantisch, tropische Reviere
- Letzter Oelwechsel: 2 Jahre her, letzter Dichtungstausch: nie

**AYDI-Befunde:**

| Befund | Fehlerbild | Schwere | Score-Abzug |
|--------|-----------|---------|-------------|
| Oelfarbe dunkelbraun, Saeurezahl 0,8 mg KOH/g | Oel gealtert | Mittel | -8 |
| Kolbenstange: Leichter Pitting (tropische Feuchtigkeit) | F-HS-07 Korrosion | Grad 2 | -10 |
| Steuergefuehl: Leicht schwammig | F-HS-03 Luft | Leicht | -5 |
| Schlaeuche: Einer zeigt leichte Aufblaehung (12 Jahre alt) | Alterung | Mittel | -12 |
| Dichtungsring Pumpe: Minimaler Oelfilm | F-HS-05 | Leicht | -3 |
| Notsteuerung (Notpinne): Vorhanden, funktioniert | — | — | 0 |

**Empfehlungen:**
1. **Sofort:** Oelwechsel + Entlueftung (35 + 0 EUR)
2. **Innerhalb 3 Monate:** Schlaeuche tauschen (beide, 12 Jahre alt → Lebensdauer ueberschritten) (380 EUR)
3. **Innerhalb 6 Monate:** Dichtungssatz Zylinder + Pumpe tauschen (280 EUR)
4. **Planen:** Kolbenstange polieren lassen oder Zylinder tauschen wenn Pitting zunimmt (800–2.200 EUR)

**AYDI-Bewertung:**
| Dimension | Score |
|-----------|-------|
| Dimensionierung | 92 (Oyster-Werft, korrekt ausgelegt) |
| Zustand | 62 (Multiple Verschleisserscheinungen) |
| Sicherheit | 85 (Notpinne vorhanden, Power-Assist) |
| Installation | 94 (Werftinstallation) |
| Wartungszustand | 55 (Schlaeuche + Oel + Dichtungen ueberfaellig) |
| **Gesamt** | **77** |

### ANHANG G — Fallstudie: Princess 75 Motor Yacht — Korrosion an Aluminium-Zylindern

**Ausgangslage:**
- Boot: Princess 75, Baujahr 2010, LOA 23,17 m
- System: Twin Hydraulikzylinder (Aluminium, OEM Princess/Kobelt-basiert) + Motorpumpe 24V
- Liegeplatz: Mallorca (Salzwasser, hohe Luftfeuchtigkeit)
- Symptom: Weisses Pulver an Zylinder-Gehaeuse, Oelverlust

**AYDI-Diagnose:**
- Fehlerbild F-HS-07 (Korrosion), Schweregrad 3 (fortgeschritten)
- Galvanische Korrosion: Aluminium-Zylinder direkt an Edelstahl-316L-Halterung → Spannungsreihe 0,6V → aggressive Korrosion
- Zusaetzlich: Kondenswasser in der Steueranlage (keine Belueftung im Fach)
- Oelverlust durch korrosionsbedingte Dichtflaechen-Schaedigung

**Massnahmen:**

| Massnahme | Kosten |
|-----------|--------|
| Beide Zylinder durch Edelstahl-316L ersetzen (Spezialanfertigung) | 6.400 EUR |
| Galvanische Isolation (PTFE-Buchsen, Isolierplatten) | 280 EUR |
| Belueftung Steuerungsfach installieren (Luefter + Thermostat) | 450 EUR |
| Oelwechsel + vollstaendige Entlueftung | 120 EUR |
| Einbau (Werft, 18 h × 120 EUR) | 2.160 EUR |
| **Gesamt** | **9.410 EUR** |

**Lehre fuer AYDI-Bewertung:** Aluminium-Zylinder in Salzwasser-Umgebung erhalten automatisch -10 Punkte im Installations-Score, wenn keine galvanische Isolation dokumentiert ist.

### ANHANG H — Fallstudie: Contest 57CS — Autopilot-Integration in bestehendes Jefa-System

**Ausgangslage:**
- Boot: Contest 57CS, Baujahr 2018, LOA 17,45 m
- System: Jefa HSC 80-200 + HP 28
- Anforderung: NKE Autopilot-Hydraulik nachrüsten (Performance-Regatta + Langfahrt)

**Systemerweiterung:**

```
Bestand:
  HP 28 → Leitung 10 mm → HSC 80-200

Erweiterung:
  HP 28 → T-Stueck → Leitung 10 mm → HSC 80-200
              ↕
     Jefa ABV-24 (Bypass-Solenoid, 24V)
              ↕
     NKE Hydraulikpumpe HP3 (30 cm³/s, 24V, 350 W)
```

**Komponenten:**
| Komponente | Modell | Preis |
|-----------|--------|-------|
| AP-Pumpe | NKE HP3 | 2.800 EUR |
| Bypass-Solenoid | Jefa ABV-24 | 245 EUR |
| T-Stueck + Fittings | Jefa Kit | 120 EUR |
| Oelzusatz (0,5 l VG 15) | Jefa HO-15 | 12 EUR |
| Ruderwinkel-Sensor | NKE Rudder Angle | 380 EUR |
| NKE Pilot-Prozessor | NKE Gyropilot 3 | 3.200 EUR |
| Einbau (12 h × 100 EUR) | | 1.200 EUR |
| **Gesamt** | | **7.957 EUR** |

**AYDI-Bewertung nach Integration:**
| Dimension | Score |
|-----------|-------|
| Dimensionierung | 91 |
| Zustand | 95 |
| Sicherheit | 76 (Notpinne vorhanden, Bypass redundant) |
| Installation | 92 |
| Wartungszustand | 95 |
| **Gesamt** | **90** |

---

## 12. ANHANG I–R: Pydantic v2 Modelle

All models use `model_config = {"from_attributes": True}` — NEVER `class Config`.

### ANHANG I — Basis-Datenmodelle

```python
"""
AYDI v6 — Hydraulische Steuerung: Pydantic v2 Datenmodelle
Module: 20_02_hydraulische_steuerung

All models use model_config = {"from_attributes": True} — NEVER class Config.
German UI labels, English code. Scores 0–100. Dimensions in mm, pressures in bar.
"""

from __future__ import annotations

from datetime import date, datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, field_validator


# ── Enums ────────────────────────────────────────────────────────────────────

class SteeringSystemType(str, Enum):
    """Type of hydraulic steering system."""
    MANUAL_HELM = "manual_helm"
    POWER_ASSIST = "power_assist"
    FULL_POWER = "full_power"
    ELECTRO_HYDRAULIC = "electro_hydraulic"
    DUAL_CIRCUIT = "dual_circuit"


class PumpType(str, Enum):
    """Hydraulic pump mechanism type."""
    PISTON = "piston"
    ROTARY_VANE = "rotary_vane"
    GEAR = "gear"
    VANE = "vane"
    AXIAL_PISTON = "axial_piston"


class CylinderMaterial(str, Enum):
    """Cylinder body material."""
    STAINLESS_316L = "stainless_316l"
    ALUMINIUM_ANODIZED = "aluminium_anodized"
    ALUMINIUM_COATED = "aluminium_coated"
    BRONZE = "bronze"


class OilGrade(str, Enum):
    """ISO VG oil viscosity grade."""
    VG_10 = "vg_10"
    VG_15 = "vg_15"
    VG_22 = "vg_22"
    VG_32 = "vg_32"
    VG_46 = "vg_46"
    VG_68 = "vg_68"


class HoseType(str, Enum):
    """Hydraulic hose classification."""
    SAE_100R7 = "sae_100r7"
    SAE_100R8 = "sae_100r8"
    SAE_100R1 = "sae_100r1"
    SAE_100R2 = "sae_100r2"
    PTFE_BRAIDED = "ptfe_braided"
    STEEL_TUBE = "steel_tube"
    CUNIFE_TUBE = "cunife_tube"
    NYLON_TUBE = "nylon_tube"


class ConfidenceLevel(str, Enum):
    """AYDI confidence level for assessment results."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class FaultSeverity(str, Enum):
    """Fault severity classification."""
    NONE = "none"
    LIGHT = "light"
    MEDIUM = "medium"
    SEVERE = "severe"
    CRITICAL = "critical"


class CorrosionGrade(int, Enum):
    """Corrosion severity grade (1-4)."""
    SURFACE = 1
    MODERATE = 2
    ADVANCED = 3
    SEVERE = 4


class BoatType(str, Enum):
    """Boat type classification."""
    SAIL_PRODUCTION = "sail_production"
    SAIL_PERFORMANCE = "sail_performance"
    SAIL_CRUISER = "sail_cruiser"
    SAIL_BLUEWATER = "sail_bluewater"
    MOTOR_PLANING = "motor_planing"
    MOTOR_DISPLACEMENT = "motor_displacement"
    MOTOR_SEMIDISPLACEMENT = "motor_semidisplacement"
    SUPERYACHT = "superyacht"


class MaintenanceUrgency(str, Enum):
    """Urgency classification for maintenance actions."""
    IMMEDIATE = "immediate"
    WITHIN_1_WEEK = "within_1_week"
    WITHIN_4_WEEKS = "within_4_weeks"
    WITHIN_3_MONTHS = "within_3_months"
    NEXT_MAINTENANCE = "next_maintenance"
    PLAN_AHEAD = "plan_ahead"
    OPTIONAL = "optional"
```

### ANHANG J — Zylinder- und Pumpenmodelle

```python
# ── Cylinder Specification ───────────────────────────────────────────────────

class CylinderDimensions(BaseModel):
    """Physical dimensions of a hydraulic steering cylinder."""

    model_config = {"from_attributes": True}

    bore_mm: float = Field(..., gt=0, le=300, description="Kolbenbohrung in mm")
    stroke_mm: float = Field(..., gt=0, le=500, description="Kolbenhub in mm")
    rod_diameter_mm: float = Field(..., gt=0, le=150, description="Kolbenstangendurchmesser in mm")
    overall_length_mm: float = Field(..., gt=0, description="Gesamtlaenge eingefahren in mm")
    mounting_centers_mm: Optional[float] = Field(None, description="Befestigungsabstand in mm")
    weight_kg: float = Field(..., gt=0, le=200, description="Gewicht in kg")

    @property
    def piston_area_cm2(self) -> float:
        """Calculate piston area in cm²."""
        import math
        return math.pi / 4 * (self.bore_mm / 10) ** 2

    @property
    def volume_cm3(self) -> float:
        """Calculate cylinder volume in cm³."""
        return self.piston_area_cm2 * (self.stroke_mm / 10)


class CylinderSpecification(BaseModel):
    """Complete specification of a hydraulic steering cylinder."""

    model_config = {"from_attributes": True}

    manufacturer: str = Field(..., description="Hersteller")
    model: str = Field(..., description="Modellbezeichnung")
    dimensions: CylinderDimensions
    material: CylinderMaterial
    max_pressure_bar: float = Field(..., gt=0, le=500, description="Maximaler Betriebsdruck in bar")
    burst_pressure_bar: Optional[float] = Field(None, gt=0, description="Berstdruck in bar")
    max_rudder_force_kn: float = Field(..., gt=0, description="Maximale Ruderkraft in kN")
    port_size: str = Field(..., description="Anschlussmass (z.B. 3/8 SAE)")
    seal_material: str = Field(default="NBR", description="Dichtungsmaterial")
    temperature_range_min_c: float = Field(default=-10, description="Minimale Betriebstemperatur")
    temperature_range_max_c: float = Field(default=80, description="Maximale Betriebstemperatur")
    certification: list[str] = Field(default_factory=list, description="Zertifizierungen (CE, DNV-GL, etc.)")
    suitable_boat_length_min_m: float = Field(..., ge=0, description="Geeignet ab Bootslaenge in m")
    suitable_boat_length_max_m: float = Field(..., ge=0, description="Geeignet bis Bootslaenge in m")
    price_eur: Optional[float] = Field(None, ge=0, description="Listenpreis in EUR")


class PumpSpecification(BaseModel):
    """Complete specification of a hydraulic steering pump."""

    model_config = {"from_attributes": True}

    manufacturer: str = Field(..., description="Hersteller")
    model: str = Field(..., description="Modellbezeichnung")
    pump_type: PumpType
    displacement_cm3_per_rev: Optional[float] = Field(
        None, gt=0, description="Foerdervolumen pro Umdrehung (Handpumpe) in cm³"
    )
    flow_rate_lpm: Optional[float] = Field(
        None, gt=0, description="Volumenstrom (Motorpumpe) in l/min"
    )
    max_pressure_bar: float = Field(..., gt=0, le=500, description="Maximaler Betriebsdruck in bar")
    motor_voltage_v: Optional[int] = Field(None, description="Motorspannung in V (None bei Handpumpe)")
    motor_power_w: Optional[float] = Field(None, ge=0, description="Motorleistung in W")
    weight_kg: float = Field(..., gt=0, description="Gewicht in kg")
    port_size: str = Field(..., description="Anschlussmass")
    steering_wheel_connection: Optional[str] = Field(None, description="Steuerrad-Anschluss")
    has_autopilot_bypass: bool = Field(default=False, description="Integriertes AP-Bypass-Ventil")
    certification: list[str] = Field(default_factory=list)
    price_eur: Optional[float] = Field(None, ge=0)
```

### ANHANG K — Oelanalyse und Leitungsmodelle

```python
# ── Oil Analysis ─────────────────────────────────────────────────────────────

class OilAnalysisResult(BaseModel):
    """Results of a hydraulic oil laboratory analysis."""

    model_config = {"from_attributes": True}

    sample_date: date
    oil_grade: OilGrade
    oil_brand: Optional[str] = None
    oil_age_years: Optional[float] = Field(None, ge=0, description="Alter des Oels in Jahren")
    water_content_ppm: float = Field(..., ge=0, description="Wassergehalt in ppm")
    particle_count_4um_per_ml: int = Field(..., ge=0, description="Partikelzahl >4µm pro ml")
    viscosity_deviation_percent: float = Field(..., description="Viskositaetsabweichung vom Neuzustand in %")
    acid_number_mg_koh_per_g: float = Field(..., ge=0, description="Saeurezahl in mg KOH/g")
    copper_content_ppm: float = Field(default=0, ge=0, description="Kupfergehalt in ppm")
    iron_content_ppm: float = Field(default=0, ge=0, description="Eisengehalt in ppm")
    appearance: str = Field(default="klar", description="Optische Erscheinung (klar, trueb, milchig, dunkel)")

    @property
    def water_status(self) -> str:
        if self.water_content_ppm < 200:
            return "gut"
        elif self.water_content_ppm < 500:
            return "akzeptabel"
        return "kritisch"

    @property
    def particle_status(self) -> str:
        if self.particle_count_4um_per_ml < 5000:
            return "gut"
        elif self.particle_count_4um_per_ml < 20000:
            return "akzeptabel"
        return "kritisch"

    @property
    def overall_oil_condition(self) -> str:
        critical_count = sum([
            self.water_content_ppm > 500,
            self.particle_count_4um_per_ml > 20000,
            abs(self.viscosity_deviation_percent) > 15,
            self.acid_number_mg_koh_per_g > 1.0,
            self.iron_content_ppm > 75,
        ])
        if critical_count > 0:
            return "kritisch"
        acceptable_count = sum([
            self.water_content_ppm > 200,
            self.particle_count_4um_per_ml > 5000,
            abs(self.viscosity_deviation_percent) > 5,
            self.acid_number_mg_koh_per_g > 0.5,
            self.iron_content_ppm > 25,
        ])
        if acceptable_count >= 2:
            return "akzeptabel"
        return "gut"


class HoseSpecification(BaseModel):
    """Specification of a hydraulic hose or tube."""

    model_config = {"from_attributes": True}

    hose_type: HoseType
    inner_diameter_mm: float = Field(..., gt=0, le=50, description="Innendurchmesser in mm")
    outer_diameter_mm: float = Field(..., gt=0, le=80, description="Aussendurchmesser in mm")
    max_pressure_bar: float = Field(..., gt=0, description="Maximaler Betriebsdruck in bar")
    burst_pressure_bar: float = Field(..., gt=0, description="Berstdruck in bar")
    min_bend_radius_mm: float = Field(..., gt=0, description="Minimaler Biegeradius in mm")
    temperature_range_min_c: float = Field(default=-40, description="Minimale Temperatur")
    temperature_range_max_c: float = Field(default=100, description="Maximale Temperatur")
    length_m: Optional[float] = Field(None, gt=0, description="Installierte Laenge in m")
    age_years: Optional[float] = Field(None, ge=0, description="Alter in Jahren")
    fitting_type: str = Field(default="SAE", description="Fitting-Typ (SAE, Schnaeidring, etc.)")

    @property
    def safety_factor(self) -> float:
        return self.burst_pressure_bar / self.max_pressure_bar

    @property
    def end_of_life_reached(self) -> bool:
        if self.age_years is None:
            return False
        if self.hose_type in (HoseType.SAE_100R7, HoseType.SAE_100R8):
            return self.age_years > 8
        if self.hose_type in (HoseType.SAE_100R1, HoseType.SAE_100R2):
            return self.age_years > 10
        if self.hose_type == HoseType.PTFE_BRAIDED:
            return self.age_years > 12
        return self.age_years > 15  # Steel/CuNi tubes last longer


class HydraulicLineRun(BaseModel):
    """A complete hydraulic line run from pump to cylinder."""

    model_config = {"from_attributes": True}

    line_id: str = Field(..., description="Eindeutige Leitungskennung")
    from_component: str = Field(..., description="Startkomponente (z.B. 'Pumpe BB')")
    to_component: str = Field(..., description="Endkomponente (z.B. 'Zylinder Port A')")
    total_length_m: float = Field(..., gt=0, description="Gesamtlaenge in m")
    segments: list[HoseSpecification] = Field(default_factory=list, description="Leitungssegmente")
    fitting_count: int = Field(default=0, ge=0, description="Anzahl Fittings/Verbindungen")
    passes_engine_room: bool = Field(default=False, description="Fuehrt durch Maschinenraum")
    fire_protection: bool = Field(default=False, description="Feuerschutzummantelung vorhanden")
    estimated_pressure_drop_bar: Optional[float] = Field(None, ge=0, description="Geschaetzter Druckverlust")
```

### ANHANG L — Fehlerbild-Modelle

```python
# ── Fault Diagnosis ──────────────────────────────────────────────────────────

class FaultFinding(BaseModel):
    """A single fault finding during inspection or analysis."""

    model_config = {"from_attributes": True}

    fault_code: str = Field(..., pattern=r"^F-HS-\d{2}$", description="Fehlerbild-Code (z.B. F-HS-01)")
    fault_name_de: str = Field(..., description="Fehlerbezeichnung (Deutsch)")
    fault_name_en: str = Field(..., description="Fault name (English)")
    severity: FaultSeverity
    location: str = Field(..., description="Ort des Fehlers (z.B. 'Zylinder Steuerbord, Kolbenstange')")
    description_de: str = Field(..., description="Beschreibung des Befunds (Deutsch)")
    confidence: ConfidenceLevel
    score_deduction: int = Field(..., ge=0, le=100, description="Score-Abzug (0–100)")
    photo_reference: Optional[str] = Field(None, description="Referenz auf Foto/Bild")
    measurement_value: Optional[float] = Field(None, description="Messwert (z.B. Drift in °/10min)")
    measurement_unit: Optional[str] = Field(None, description="Einheit des Messwerts")
    recommended_action_de: str = Field(..., description="Empfohlene Massnahme (Deutsch)")
    urgency: MaintenanceUrgency
    estimated_cost_eur_min: Optional[float] = Field(None, ge=0)
    estimated_cost_eur_max: Optional[float] = Field(None, ge=0)


class LeakageAssessment(BaseModel):
    """Assessment of a hydraulic leakage."""

    model_config = {"from_attributes": True}

    location: str = Field(..., description="Leckage-Ort")
    leak_type: str = Field(..., description="external oder internal")
    oil_loss_ml_per_week: Optional[float] = Field(None, ge=0, description="Oelverlust in ml/Woche")
    severity: FaultSeverity
    cause_suspected: str = Field(..., description="Vermutete Ursache")
    confidence: ConfidenceLevel
    seal_age_years: Optional[float] = Field(None, ge=0, description="Alter der Dichtung in Jahren")

    @field_validator("leak_type")
    @classmethod
    def validate_leak_type(cls, v: str) -> str:
        if v not in ("external", "internal"):
            raise ValueError("leak_type must be 'external' or 'internal'")
        return v


class DriftTestResult(BaseModel):
    """Result of a cylinder drift test."""

    model_config = {"from_attributes": True}

    test_date: date
    test_duration_minutes: int = Field(default=10, ge=1, le=60)
    initial_rudder_angle_deg: float = Field(default=0.0, description="Ausgangs-Ruderwinkel")
    final_rudder_angle_deg: float = Field(..., description="End-Ruderwinkel nach Testdauer")
    water_temperature_c: Optional[float] = Field(None, description="Wassertemperatur")
    boat_loaded: bool = Field(default=True, description="Boot beladen (im Wasser)")

    @property
    def drift_deg(self) -> float:
        return abs(self.final_rudder_angle_deg - self.initial_rudder_angle_deg)

    @property
    def drift_per_10min(self) -> float:
        return self.drift_deg / self.test_duration_minutes * 10

    @property
    def assessment(self) -> str:
        d = self.drift_per_10min
        if d < 1.0:
            return "normal"
        elif d < 3.0:
            return "beginnende_leckage"
        elif d < 10.0:
            return "deutliche_leckage"
        return "schwere_leckage"

    @property
    def score_deduction(self) -> int:
        d = self.drift_per_10min
        if d < 1.0:
            return 0
        elif d < 3.0:
            return 10
        elif d < 10.0:
            return 25
        return 45


class CorrosionAssessment(BaseModel):
    """Assessment of corrosion on hydraulic components."""

    model_config = {"from_attributes": True}

    component: str = Field(..., description="Betroffene Komponente")
    material: CylinderMaterial
    grade: CorrosionGrade
    area_affected_percent: float = Field(..., ge=0, le=100, description="Betroffene Flaeche in %")
    depth_mm: Optional[float] = Field(None, ge=0, description="Korrosionstiefe in mm")
    galvanic_cause: bool = Field(default=False, description="Galvanische Korrosion vermutet")
    galvanic_partner: Optional[str] = Field(None, description="Galvanischer Partner (z.B. 'Edelstahl 316L')")
    environment: str = Field(default="salzwasser", description="Umgebung (salzwasser, suesswasser, tropisch)")
    confidence: ConfidenceLevel

    @property
    def score_deduction(self) -> int:
        return {1: 3, 2: 10, 3: 25, 4: 50}[self.grade.value]
```

### ANHANG M — Systemdimensionierung

```python
# ── System Sizing ────────────────────────────────────────────────────────────

class RudderForceCalculation(BaseModel):
    """Calculation of hydrodynamic rudder force."""

    model_config = {"from_attributes": True}

    boat_type: BoatType
    loa_m: float = Field(..., gt=0, le=80, description="Laenge ueber alles in m")
    beam_m: float = Field(..., gt=0, le=20, description="Breite in m")
    draft_m: float = Field(..., gt=0, le=8, description="Tiefgang in m")
    displacement_t: Optional[float] = Field(None, gt=0, description="Verdraengung in t")
    max_speed_kn: float = Field(..., gt=0, le=50, description="Hoechstgeschwindigkeit in kn")
    rudder_area_m2: float = Field(..., gt=0, le=3, description="Ruderfläche in m²")
    rudder_type: str = Field(default="spade", description="Rudertyp (spade, skeg, balanced)")
    rudder_angle_max_deg: float = Field(default=35, gt=0, le=70, description="Maximaler Ruderausschlag")
    rudder_stock_offset_mm: float = Field(
        default=0, ge=0, description="Ruderschaft-Exzentrizitaet in mm"
    )
    lift_coefficient: float = Field(default=1.0, gt=0, le=2.0, description="Auftriebsbeiwert Cₗ")
    seawater_density_kg_m3: float = Field(default=1025, description="Dichte Seewasser")

    @property
    def max_speed_ms(self) -> float:
        return self.max_speed_kn * 0.5144

    @property
    def rudder_force_n(self) -> float:
        """Hydrodynamic rudder force at max speed and max angle."""
        return (
            0.5
            * self.seawater_density_kg_m3
            * self.max_speed_ms ** 2
            * self.rudder_area_m2
            * self.lift_coefficient
        )

    @property
    def rudder_force_kn(self) -> float:
        return self.rudder_force_n / 1000

    @property
    def rudder_torque_nm(self) -> float:
        """Torque at rudder stock."""
        if self.rudder_stock_offset_mm > 0:
            return self.rudder_force_n * (self.rudder_stock_offset_mm / 1000)
        # Estimate offset as 15% of rudder chord
        import math
        chord_estimate_m = math.sqrt(self.rudder_area_m2 / 2.5)  # aspect ratio ~2.5
        offset_m = chord_estimate_m * 0.15
        return self.rudder_force_n * offset_m


class CylinderSizing(BaseModel):
    """Cylinder sizing calculation."""

    model_config = {"from_attributes": True}

    rudder_torque_nm: float = Field(..., gt=0, description="Drehmoment am Ruderschaft in Nm")
    quadrant_radius_mm: float = Field(..., gt=0, le=500, description="Quadrantradius in mm")
    system_pressure_bar: float = Field(..., gt=0, le=500, description="Systemdruck in bar")
    safety_factor: float = Field(default=1.5, ge=1.0, le=5.0, description="Sicherheitsfaktor")
    max_rudder_angle_deg: float = Field(default=35, gt=0, le=70, description="Max. Ruderausschlag")

    @property
    def required_cylinder_force_n(self) -> float:
        return self.rudder_torque_nm / (self.quadrant_radius_mm / 1000)

    @property
    def required_piston_area_cm2(self) -> float:
        return (self.required_cylinder_force_n * self.safety_factor) / (self.system_pressure_bar * 1e5) * 1e4

    @property
    def required_bore_mm(self) -> float:
        import math
        return math.sqrt(4 * self.required_piston_area_cm2 / math.pi) * 10

    @property
    def required_stroke_mm(self) -> float:
        import math
        return 2 * (self.quadrant_radius_mm) * math.sin(math.radians(self.max_rudder_angle_deg))

    @property
    def required_cylinder_volume_cm3(self) -> float:
        import math
        actual_area = math.pi / 4 * (self.required_bore_mm / 10) ** 2
        return actual_area * (self.required_stroke_mm / 10)


class PumpSizing(BaseModel):
    """Pump sizing based on cylinder requirements."""

    model_config = {"from_attributes": True}

    cylinder_volume_cm3: float = Field(..., gt=0, description="Zylindervolumen in cm³")
    line_volume_cm3: float = Field(default=0, ge=0, description="Leitungsvolumen in cm³")
    dead_volume_cm3: float = Field(default=0, ge=0, description="Totvolumen in cm³")
    max_turns_lock_to_lock: float = Field(
        default=5, gt=0, le=10, description="Max. Umdrehungen Hart-ueber-Hart"
    )
    target_steering_time_s: Optional[float] = Field(
        None, gt=0, description="Ziel-Steuerzeit Hart-ueber-Hart in s (Motorpumpe)"
    )

    @property
    def total_volume_cm3(self) -> float:
        return self.cylinder_volume_cm3 + self.line_volume_cm3 + self.dead_volume_cm3

    @property
    def required_displacement_cm3_per_rev(self) -> float:
        """Required pump displacement for manual helm pump."""
        return self.total_volume_cm3 / self.max_turns_lock_to_lock

    @property
    def required_flow_rate_lpm(self) -> Optional[float]:
        """Required flow rate for motor pump."""
        if self.target_steering_time_s is None:
            return None
        return (self.total_volume_cm3 / self.target_steering_time_s) * 60 / 1000


class SystemDimensioning(BaseModel):
    """Complete system dimensioning result."""

    model_config = {"from_attributes": True}

    rudder_force: RudderForceCalculation
    cylinder_sizing: CylinderSizing
    pump_sizing: PumpSizing
    recommended_system_type: SteeringSystemType
    recommended_cylinder: Optional[CylinderSpecification] = None
    recommended_pump: Optional[PumpSpecification] = None
    recommended_oil_grade: OilGrade
    recommended_hose_type: HoseType
    recommended_hose_id_mm: float = Field(..., gt=0, description="Empfohlener Leitungs-ID in mm")
    notes: list[str] = Field(default_factory=list, description="Anmerkungen zur Dimensionierung")
    confidence: ConfidenceLevel
```

### ANHANG N — Hersteller-Datenbank-Modelle

```python
# ── Manufacturer Database ────────────────────────────────────────────────────

class ManufacturerContact(BaseModel):
    """Contact information for a manufacturer."""

    model_config = {"from_attributes": True}

    company_name: str
    country: str
    founded_year: Optional[int] = None
    website: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    distributor_europe: Optional[str] = None
    distributor_americas: Optional[str] = None


class ManufacturerProductLine(BaseModel):
    """A product line from a steering system manufacturer."""

    model_config = {"from_attributes": True}

    line_name: str = Field(..., description="Produktlinien-Name (z.B. 'HSC-Serie')")
    product_type: str = Field(..., description="Produkttyp (cylinder, pump, system)")
    boat_size_min_m: float = Field(..., ge=0)
    boat_size_max_m: float = Field(..., ge=0)
    price_range_eur_min: Optional[float] = Field(None, ge=0)
    price_range_eur_max: Optional[float] = Field(None, ge=0)
    models: list[str] = Field(default_factory=list, description="Modellnummern")
    specialization: str = Field(default="", description="Besondere Eignung")


class SteeringManufacturer(BaseModel):
    """Complete manufacturer profile for the AYDI database."""

    model_config = {"from_attributes": True}

    contact: ManufacturerContact
    specialization: str = Field(..., description="Spezialisierung")
    product_lines: list[ManufacturerProductLine] = Field(default_factory=list)
    certifications: list[str] = Field(default_factory=list)
    boat_size_range_min_m: float = Field(..., ge=0)
    boat_size_range_max_m: float = Field(..., ge=0)
    typical_lead_time_weeks: str = Field(default="2-4", description="Typische Lieferzeit")
    warranty_years: int = Field(default=3, ge=0)
    aydi_quality_score: int = Field(..., ge=0, le=100, description="AYDI-Qualitaetsscore 0–100")
    strengths: list[str] = Field(default_factory=list, description="Staerken")
    weaknesses: list[str] = Field(default_factory=list, description="Schwaechen")
    sail_suitability: int = Field(..., ge=0, le=5, description="Eignung Segelyacht 0–5")
    motor_suitability: int = Field(..., ge=0, le=5, description="Eignung Motoryacht 0–5")
    build_quality: int = Field(..., ge=0, le=5, description="Verarbeitungsqualitaet 0–5")
    price_performance: int = Field(..., ge=0, le=5, description="Preis-Leistung 0–5")
    parts_availability: int = Field(..., ge=0, le=5, description="Ersatzteil-Verfuegbarkeit 0–5")
    electronics_integration: int = Field(..., ge=0, le=5, description="Elektronik-Integration 0–5")
    corrosion_protection: int = Field(..., ge=0, le=5, description="Korrosionsschutz 0–5")
```

### ANHANG O — Inspektions- und Wartungsmodelle

```python
# ── Inspection and Maintenance ───────────────────────────────────────────────

class SteeringInspectionItem(BaseModel):
    """A single inspection item in a steering system check."""

    model_config = {"from_attributes": True}

    item_id: str = Field(..., description="Pruefpunkt-ID")
    item_name_de: str = Field(..., description="Pruefpunkt (Deutsch)")
    category: str = Field(..., description="Kategorie (zylinder, pumpe, leitung, oel, allgemein)")
    result: str = Field(..., description="Ergebnis (ok, warnung, mangel, kritisch, nicht_geprueft)")
    finding_de: Optional[str] = Field(None, description="Befund-Beschreibung (Deutsch)")
    fault: Optional[FaultFinding] = Field(None, description="Zugeordneter Fehler (wenn vorhanden)")
    photo_ids: list[str] = Field(default_factory=list, description="Zugeordnete Foto-IDs")
    confidence: ConfidenceLevel


class SteeringInspectionReport(BaseModel):
    """Complete inspection report for a hydraulic steering system."""

    model_config = {"from_attributes": True}

    report_id: str = Field(..., description="Berichts-ID")
    inspection_date: date
    inspector: str = Field(..., description="Pruefer/Gutachter")
    boat_name: str
    boat_type: BoatType
    loa_m: float = Field(..., gt=0)
    system_type: SteeringSystemType
    system_manufacturer: str
    system_model: str
    system_age_years: Optional[float] = Field(None, ge=0)
    items: list[SteeringInspectionItem] = Field(default_factory=list)
    faults: list[FaultFinding] = Field(default_factory=list)
    oil_analysis: Optional[OilAnalysisResult] = None
    drift_test: Optional[DriftTestResult] = None
    overall_condition_de: str = Field(..., description="Gesamtzustand (Deutsch)")
    recommendations_de: list[str] = Field(default_factory=list, description="Empfehlungen (Deutsch)")

    @property
    def fault_count_by_severity(self) -> dict[str, int]:
        counts: dict[str, int] = {}
        for f in self.faults:
            sev = f.severity.value
            counts[sev] = counts.get(sev, 0) + 1
        return counts

    @property
    def has_critical_faults(self) -> bool:
        return any(f.severity == FaultSeverity.CRITICAL for f in self.faults)


class MaintenanceTask(BaseModel):
    """A maintenance task for a hydraulic steering system."""

    model_config = {"from_attributes": True}

    task_id: str
    task_name_de: str = Field(..., description="Aufgabe (Deutsch)")
    task_name_en: str = Field(..., description="Task name (English)")
    category: str = Field(..., description="Kategorie")
    urgency: MaintenanceUrgency
    estimated_duration_hours: float = Field(..., ge=0, description="Geschaetzte Dauer in Stunden")
    estimated_cost_eur_min: float = Field(..., ge=0)
    estimated_cost_eur_max: float = Field(..., ge=0)
    requires_specialist: bool = Field(default=False, description="Fachbetrieb erforderlich")
    parts_needed: list[str] = Field(default_factory=list, description="Benoetigte Ersatzteile")
    description_de: str = Field(default="", description="Beschreibung (Deutsch)")
    triggered_by_fault: Optional[str] = Field(None, description="Ausgeloest durch Fehlerbild-Code")


class MaintenanceSchedule(BaseModel):
    """Maintenance schedule for a hydraulic steering system."""

    model_config = {"from_attributes": True}

    boat_name: str
    system_type: SteeringSystemType
    system_age_years: float = Field(..., ge=0)
    last_oil_change: Optional[date] = None
    last_seal_change: Optional[date] = None
    last_hose_change: Optional[date] = None
    last_full_service: Optional[date] = None
    operating_hours_since_last_service: Optional[float] = Field(None, ge=0)
    upcoming_tasks: list[MaintenanceTask] = Field(default_factory=list)
    overdue_tasks: list[MaintenanceTask] = Field(default_factory=list)

    @property
    def oil_change_overdue(self) -> bool:
        if self.last_oil_change is None:
            return True
        from datetime import date as d
        age_days = (d.today() - self.last_oil_change).days
        if self.system_type in (
            SteeringSystemType.FULL_POWER,
            SteeringSystemType.ELECTRO_HYDRAULIC,
            SteeringSystemType.DUAL_CIRCUIT,
        ):
            return age_days > 730  # 2 years for motor systems
        return age_days > 1825  # 5 years for manual systems
```

### ANHANG P — Score-Berechnung

```python
# ── Score Calculation ────────────────────────────────────────────────────────

class SteeringDimensioningScore(BaseModel):
    """Score for steering system dimensioning adequacy."""

    model_config = {"from_attributes": True}

    rudder_force_kn: float = Field(..., ge=0, description="Berechnete Ruderkraft in kN")
    cylinder_force_kn: float = Field(..., ge=0, description="Zylinderkraft in kN")
    safety_factor: float = Field(..., ge=0, description="Tatsaechlicher Sicherheitsfaktor")
    system_type_adequate: bool = Field(..., description="Systemtyp fuer Bootskategorie angemessen")
    pump_size_adequate: bool = Field(..., description="Pumpengroesse angemessen")
    line_size_adequate: bool = Field(..., description="Leitungsgroesse angemessen")
    turns_lock_to_lock: Optional[float] = Field(None, ge=0)
    steering_time_s: Optional[float] = Field(None, ge=0)
    confidence: ConfidenceLevel

    @property
    def score(self) -> int:
        base = 100
        if self.safety_factor < 1.5:
            base -= 40
        elif self.safety_factor < 2.0:
            base -= 10
        if not self.system_type_adequate:
            base -= 20
        if not self.pump_size_adequate:
            base -= 15
        if not self.line_size_adequate:
            base -= 10
        if self.turns_lock_to_lock and self.turns_lock_to_lock > 6:
            base -= 5
        if self.steering_time_s and self.steering_time_s > 8:
            base -= 10
        return max(0, min(100, base))


class SteeringConditionScore(BaseModel):
    """Score for current steering system condition."""

    model_config = {"from_attributes": True}

    faults: list[FaultFinding] = Field(default_factory=list)
    oil_analysis: Optional[OilAnalysisResult] = None
    drift_test: Optional[DriftTestResult] = None
    corrosion: Optional[CorrosionAssessment] = None
    confidence: ConfidenceLevel

    @property
    def score(self) -> int:
        base = 100
        for fault in self.faults:
            base -= fault.score_deduction
        if self.oil_analysis:
            if self.oil_analysis.overall_oil_condition == "kritisch":
                base -= 15
            elif self.oil_analysis.overall_oil_condition == "akzeptabel":
                base -= 5
        if self.drift_test:
            base -= self.drift_test.score_deduction
        if self.corrosion:
            base -= self.corrosion.score_deduction
        return max(0, min(100, base))


class SteeringSafetyScore(BaseModel):
    """Score for steering system safety features."""

    model_config = {"from_attributes": True}

    has_emergency_steering: bool = Field(..., description="Notsteuerung vorhanden")
    emergency_steering_tested: bool = Field(default=False, description="Notsteuerung getestet")
    has_dual_circuit: bool = Field(default=False, description="Zweikreis-System")
    has_pressure_relief: bool = Field(default=True, description="Ueberdruckventil vorhanden")
    has_rudder_stops: bool = Field(default=True, description="Ruderanschlaege vorhanden")
    has_rudder_indicator: bool = Field(default=False, description="Ruderwinkelanzeige vorhanden")
    meets_ce_requirements: bool = Field(default=True, description="CE-Anforderungen erfuellt")
    meets_class_requirements: Optional[bool] = Field(None, description="Klasse-Anforderungen erfuellt")
    loa_m: float = Field(..., gt=0)
    confidence: ConfidenceLevel

    @property
    def score(self) -> int:
        base = 100
        if not self.has_emergency_steering:
            base -= 30
        elif not self.emergency_steering_tested:
            base -= 10
        if self.loa_m > 24 and not self.has_dual_circuit:
            base -= 25
        if not self.has_pressure_relief:
            base -= 15
        if not self.has_rudder_stops:
            base -= 10
        if not self.has_rudder_indicator and self.loa_m > 16:
            base -= 5
        if not self.meets_ce_requirements:
            base -= 20
        if self.meets_class_requirements is False:
            base -= 15
        return max(0, min(100, base))


class SteeringInstallationScore(BaseModel):
    """Score for steering system installation quality."""

    model_config = {"from_attributes": True}

    cylinder_alignment: str = Field(..., description="Zylinderausrichtung (gut, akzeptabel, schlecht)")
    hose_routing: str = Field(..., description="Leitungsfuehrung (gut, akzeptabel, schlecht)")
    hose_support: bool = Field(default=True, description="Leitungen korrekt befestigt/gestuetzt")
    fittings_accessible: bool = Field(default=True, description="Fittings zugaenglich")
    cylinder_accessible: bool = Field(default=True, description="Zylinder zugaenglich")
    pump_accessible: bool = Field(default=True, description="Pumpe zugaenglich")
    reservoir_accessible: bool = Field(default=True, description="Reservoir zugaenglich")
    engine_room_protection: bool = Field(default=True, description="Maschinenraum-Schutz (wenn zutreffend)")
    galvanic_isolation: bool = Field(default=True, description="Galvanische Isolation (wenn noetig)")
    labeling_adequate: bool = Field(default=False, description="Beschriftung vorhanden")
    confidence: ConfidenceLevel

    @property
    def score(self) -> int:
        base = 100
        alignment_deduction = {"gut": 0, "akzeptabel": -5, "schlecht": -20}
        base += alignment_deduction.get(self.cylinder_alignment, -10)
        routing_deduction = {"gut": 0, "akzeptabel": -5, "schlecht": -15}
        base += routing_deduction.get(self.hose_routing, -10)
        if not self.hose_support:
            base -= 10
        if not self.fittings_accessible:
            base -= 5
        if not self.cylinder_accessible:
            base -= 10
        if not self.pump_accessible:
            base -= 5
        if not self.reservoir_accessible:
            base -= 10
        if not self.engine_room_protection:
            base -= 10
        if not self.galvanic_isolation:
            base -= 10
        if not self.labeling_adequate:
            base -= 3
        return max(0, min(100, base))


class SteeringMaintenanceScore(BaseModel):
    """Score for steering system maintenance state."""

    model_config = {"from_attributes": True}

    oil_change_overdue: bool = Field(default=False)
    seal_age_years: Optional[float] = Field(None, ge=0)
    hose_age_years: Optional[float] = Field(None, ge=0)
    last_full_service_years_ago: Optional[float] = Field(None, ge=0)
    documentation_available: bool = Field(default=False, description="Wartungsdokumentation vorhanden")
    spare_parts_on_board: bool = Field(default=False, description="Ersatzteile an Bord")
    confidence: ConfidenceLevel

    @property
    def score(self) -> int:
        base = 100
        if self.oil_change_overdue:
            base -= 15
        if self.seal_age_years is not None and self.seal_age_years > 8:
            base -= 20
        elif self.seal_age_years is not None and self.seal_age_years > 5:
            base -= 8
        if self.hose_age_years is not None and self.hose_age_years > 8:
            base -= 20
        elif self.hose_age_years is not None and self.hose_age_years > 5:
            base -= 8
        if self.last_full_service_years_ago is not None and self.last_full_service_years_ago > 5:
            base -= 15
        if not self.documentation_available:
            base -= 5
        if not self.spare_parts_on_board:
            base -= 3
        return max(0, min(100, base))
```

### ANHANG Q — Gesamt-Bewertung

```python
# ── Overall Assessment ───────────────────────────────────────────────────────

class SteeringSystemAssessment(BaseModel):
    """Complete AYDI assessment of a hydraulic steering system."""

    model_config = {"from_attributes": True}

    assessment_id: str = Field(..., description="Bewertungs-ID")
    assessment_date: datetime
    boat_name: str
    boat_type: BoatType
    loa_m: float = Field(..., gt=0)

    # System identification
    system_type: SteeringSystemType
    cylinder: Optional[CylinderSpecification] = None
    pump: Optional[PumpSpecification] = None
    oil_grade: Optional[OilGrade] = None
    system_age_years: Optional[float] = Field(None, ge=0)

    # Sub-scores
    dimensioning_score: SteeringDimensioningScore
    condition_score: SteeringConditionScore
    safety_score: SteeringSafetyScore
    installation_score: SteeringInstallationScore
    maintenance_score: SteeringMaintenanceScore

    # Weights
    weight_dimensioning: float = Field(default=0.25, ge=0, le=1)
    weight_condition: float = Field(default=0.25, ge=0, le=1)
    weight_safety: float = Field(default=0.20, ge=0, le=1)
    weight_installation: float = Field(default=0.15, ge=0, le=1)
    weight_maintenance: float = Field(default=0.15, ge=0, le=1)

    # Results
    inspection_report: Optional[SteeringInspectionReport] = None
    maintenance_schedule: Optional[MaintenanceSchedule] = None
    faults: list[FaultFinding] = Field(default_factory=list)
    recommendations_de: list[str] = Field(default_factory=list)
    notes: list[str] = Field(default_factory=list)

    # Confidence
    overall_confidence: ConfidenceLevel

    @property
    def overall_score(self) -> float:
        return (
            self.weight_dimensioning * self.dimensioning_score.score
            + self.weight_condition * self.condition_score.score
            + self.weight_safety * self.safety_score.score
            + self.weight_installation * self.installation_score.score
            + self.weight_maintenance * self.maintenance_score.score
        )

    @property
    def overall_score_rounded(self) -> int:
        return round(self.overall_score)

    @property
    def rating_de(self) -> str:
        s = self.overall_score
        if s >= 85:
            return "Ausgezeichnet"
        elif s >= 70:
            return "Gut"
        elif s >= 50:
            return "Akzeptabel"
        elif s >= 30:
            return "Maengel"
        return "Kritisch"

    @property
    def badge_color(self) -> str:
        s = self.overall_score
        if s >= 70:
            return "green"
        elif s >= 50:
            return "amber"
        return "red"

    @property
    def has_critical_issues(self) -> bool:
        return (
            any(f.severity == FaultSeverity.CRITICAL for f in self.faults)
            or self.overall_score < 30
        )

    @property
    def sub_scores_summary(self) -> dict[str, int]:
        return {
            "dimensionierung": self.dimensioning_score.score,
            "zustand": self.condition_score.score,
            "sicherheit": self.safety_score.score,
            "installation": self.installation_score.score,
            "wartungszustand": self.maintenance_score.score,
            "gesamt": self.overall_score_rounded,
        }
```

### ANHANG R — Hilfsmodelle und Konstanten

```python
# ── Constants and Utility Models ─────────────────────────────────────────────

class HydraulicSteeringConstants:
    """Constants for hydraulic steering calculations and assessments."""

    # Seawater density
    SEAWATER_DENSITY_KG_M3 = 1025.0

    # Standard safety factors (ISO 10592)
    SF_CYLINDER_STATIC = 1.5
    SF_CYLINDER_DYNAMIC = 2.0
    SF_LINES = 4.0
    SF_PUMP = 2.0
    SF_FITTINGS = 4.0

    # Maximum operating pressures (ISO 10592)
    MAX_PRESSURE_MANUAL_BAR = 70
    MAX_PRESSURE_POWER_BAR = 140

    # Burst pressure ratio
    BURST_PRESSURE_RATIO = 4.0

    # Maximum steering time lock-to-lock (ISO 10592)
    MAX_STEERING_TIME_POWER_S = 5.0

    # Maximum allowable flow velocities [m/s]
    MAX_FLOW_VELOCITY_PRESSURE = 4.0
    MAX_FLOW_VELOCITY_RETURN = 2.0
    MAX_FLOW_VELOCITY_SUCTION = 1.0

    # Maximum pressure drop as fraction of system pressure
    MAX_PRESSURE_DROP_FRACTION = 0.05

    # Oil analysis limits
    OIL_WATER_GOOD_PPM = 200
    OIL_WATER_ACCEPTABLE_PPM = 500
    OIL_PARTICLES_GOOD = 5000
    OIL_PARTICLES_ACCEPTABLE = 20000
    OIL_VISCOSITY_DEVIATION_GOOD = 5.0
    OIL_VISCOSITY_DEVIATION_ACCEPTABLE = 15.0
    OIL_ACID_NUMBER_GOOD = 0.5
    OIL_ACID_NUMBER_ACCEPTABLE = 1.0

    # Drift test limits [deg/10min]
    DRIFT_NORMAL = 1.0
    DRIFT_BEGINNING = 3.0
    DRIFT_SIGNIFICANT = 10.0

    # Score weights
    WEIGHT_DIMENSIONING = 0.25
    WEIGHT_CONDITION = 0.25
    WEIGHT_SAFETY = 0.20
    WEIGHT_INSTALLATION = 0.15
    WEIGHT_MAINTENANCE = 0.15

    # Score thresholds
    SCORE_EXCELLENT = 85
    SCORE_GOOD = 70
    SCORE_ACCEPTABLE = 50
    SCORE_DEFICIENT = 30

    # Hose replacement age [years]
    HOSE_MAX_AGE_THERMOPLAST = 8
    HOSE_MAX_AGE_BRAIDED = 10
    HOSE_MAX_AGE_PTFE = 12
    HOSE_MAX_AGE_STEEL = 25

    # Seal replacement age [years]
    SEAL_MAX_AGE_NBR = 8
    SEAL_MAX_AGE_FKM = 12

    # Oil change intervals [days]
    OIL_CHANGE_MANUAL_DAYS = 1825  # 5 years
    OIL_CHANGE_POWER_DAYS = 730  # 2 years
    OIL_CHANGE_CLASS_DAYS = 365  # 1 year


class UnitConversion(BaseModel):
    """Utility model for common unit conversions in hydraulic steering."""

    model_config = {"from_attributes": True}

    @staticmethod
    def bar_to_psi(bar: float) -> float:
        return bar * 14.504

    @staticmethod
    def psi_to_bar(psi: float) -> float:
        return psi * 0.0689

    @staticmethod
    def kn_to_ms(knots: float) -> float:
        return knots * 0.5144

    @staticmethod
    def kn_to_kgf(kn: float) -> float:
        return kn * 101.97

    @staticmethod
    def nm_to_kgfm(nm: float) -> float:
        return nm * 0.10197

    @staticmethod
    def lpm_to_cm3s(lpm: float) -> float:
        return lpm * 16.667

    @staticmethod
    def mm_to_inch(mm: float) -> float:
        return mm * 0.03937

    @staticmethod
    def cm3_to_in3(cm3: float) -> float:
        return cm3 * 0.06102

    @staticmethod
    def bore_to_area_cm2(bore_mm: float) -> float:
        """Calculate piston area from bore diameter."""
        import math
        return math.pi / 4 * (bore_mm / 10) ** 2

    @staticmethod
    def area_to_bore_mm(area_cm2: float) -> float:
        """Calculate bore diameter from piston area."""
        import math
        return math.sqrt(4 * area_cm2 / math.pi) * 10

    @staticmethod
    def force_at_pressure(bore_mm: float, pressure_bar: float) -> float:
        """Calculate cylinder force in kN from bore and pressure."""
        import math
        area_m2 = math.pi / 4 * (bore_mm / 1000) ** 2
        return pressure_bar * 1e5 * area_m2 / 1000


class QuickSizingLookup(BaseModel):
    """Quick sizing lookup table entry for AYDI Level 1 (Schnellanalyse)."""

    model_config = {"from_attributes": True}

    boat_type: BoatType
    loa_min_m: float = Field(..., ge=0)
    loa_max_m: float = Field(..., ge=0)
    typical_rudder_force_kn: float = Field(..., ge=0)
    recommended_cylinder_bore_mm: float = Field(..., gt=0)
    recommended_cylinder_stroke_mm: float = Field(..., gt=0)
    recommended_pump_displacement_cm3: Optional[float] = Field(None, gt=0)
    recommended_pump_flow_lpm: Optional[float] = Field(None, gt=0)
    recommended_line_id_mm: float = Field(..., gt=0)
    recommended_oil_grade: OilGrade
    recommended_system_type: SteeringSystemType
    confidence: ConfidenceLevel = ConfidenceLevel.BENCHMARK


# ── Quick Sizing Data ────────────────────────────────────────────────────────

QUICK_SIZING_TABLE: list[dict] = [
    {
        "boat_type": "sail_cruiser",
        "loa_min_m": 8,
        "loa_max_m": 10,
        "typical_rudder_force_kn": 8,
        "recommended_cylinder_bore_mm": 40,
        "recommended_cylinder_stroke_mm": 100,
        "recommended_pump_displacement_cm3": 14,
        "recommended_pump_flow_lpm": None,
        "recommended_line_id_mm": 6,
        "recommended_oil_grade": "vg_15",
        "recommended_system_type": "manual_helm",
    },
    {
        "boat_type": "sail_cruiser",
        "loa_min_m": 10,
        "loa_max_m": 12,
        "typical_rudder_force_kn": 12,
        "recommended_cylinder_bore_mm": 40,
        "recommended_cylinder_stroke_mm": 120,
        "recommended_pump_displacement_cm3": 14,
        "recommended_pump_flow_lpm": None,
        "recommended_line_id_mm": 6,
        "recommended_oil_grade": "vg_15",
        "recommended_system_type": "manual_helm",
    },
    {
        "boat_type": "sail_cruiser",
        "loa_min_m": 12,
        "loa_max_m": 14,
        "typical_rudder_force_kn": 18,
        "recommended_cylinder_bore_mm": 50,
        "recommended_cylinder_stroke_mm": 130,
        "recommended_pump_displacement_cm3": 16,
        "recommended_pump_flow_lpm": None,
        "recommended_line_id_mm": 8,
        "recommended_oil_grade": "vg_15",
        "recommended_system_type": "manual_helm",
    },
    {
        "boat_type": "sail_cruiser",
        "loa_min_m": 14,
        "loa_max_m": 16,
        "typical_rudder_force_kn": 25,
        "recommended_cylinder_bore_mm": 50,
        "recommended_cylinder_stroke_mm": 160,
        "recommended_pump_displacement_cm3": 22,
        "recommended_pump_flow_lpm": None,
        "recommended_line_id_mm": 8,
        "recommended_oil_grade": "vg_15",
        "recommended_system_type": "manual_helm",
    },
    {
        "boat_type": "sail_cruiser",
        "loa_min_m": 16,
        "loa_max_m": 18,
        "typical_rudder_force_kn": 35,
        "recommended_cylinder_bore_mm": 65,
        "recommended_cylinder_stroke_mm": 160,
        "recommended_pump_displacement_cm3": 22,
        "recommended_pump_flow_lpm": None,
        "recommended_line_id_mm": 10,
        "recommended_oil_grade": "vg_15",
        "recommended_system_type": "manual_helm",
    },
    {
        "boat_type": "sail_bluewater",
        "loa_min_m": 18,
        "loa_max_m": 22,
        "typical_rudder_force_kn": 50,
        "recommended_cylinder_bore_mm": 65,
        "recommended_cylinder_stroke_mm": 200,
        "recommended_pump_displacement_cm3": 28,
        "recommended_pump_flow_lpm": None,
        "recommended_line_id_mm": 10,
        "recommended_oil_grade": "vg_15",
        "recommended_system_type": "power_assist",
    },
    {
        "boat_type": "sail_bluewater",
        "loa_min_m": 22,
        "loa_max_m": 26,
        "typical_rudder_force_kn": 70,
        "recommended_cylinder_bore_mm": 80,
        "recommended_cylinder_stroke_mm": 200,
        "recommended_pump_displacement_cm3": 36,
        "recommended_pump_flow_lpm": 8,
        "recommended_line_id_mm": 12,
        "recommended_oil_grade": "vg_32",
        "recommended_system_type": "full_power",
    },
    {
        "boat_type": "motor_planing",
        "loa_min_m": 10,
        "loa_max_m": 14,
        "typical_rudder_force_kn": 20,
        "recommended_cylinder_bore_mm": 50,
        "recommended_cylinder_stroke_mm": 130,
        "recommended_pump_displacement_cm3": 16,
        "recommended_pump_flow_lpm": None,
        "recommended_line_id_mm": 8,
        "recommended_oil_grade": "vg_15",
        "recommended_system_type": "power_assist",
    },
    {
        "boat_type": "motor_displacement",
        "loa_min_m": 14,
        "loa_max_m": 18,
        "typical_rudder_force_kn": 40,
        "recommended_cylinder_bore_mm": 65,
        "recommended_cylinder_stroke_mm": 160,
        "recommended_pump_displacement_cm3": None,
        "recommended_pump_flow_lpm": 4,
        "recommended_line_id_mm": 10,
        "recommended_oil_grade": "vg_32",
        "recommended_system_type": "full_power",
    },
    {
        "boat_type": "motor_displacement",
        "loa_min_m": 18,
        "loa_max_m": 24,
        "typical_rudder_force_kn": 65,
        "recommended_cylinder_bore_mm": 80,
        "recommended_cylinder_stroke_mm": 200,
        "recommended_pump_displacement_cm3": None,
        "recommended_pump_flow_lpm": 8,
        "recommended_line_id_mm": 12,
        "recommended_oil_grade": "vg_32",
        "recommended_system_type": "full_power",
    },
    {
        "boat_type": "superyacht",
        "loa_min_m": 24,
        "loa_max_m": 35,
        "typical_rudder_force_kn": 120,
        "recommended_cylinder_bore_mm": 100,
        "recommended_cylinder_stroke_mm": 300,
        "recommended_pump_displacement_cm3": None,
        "recommended_pump_flow_lpm": 15,
        "recommended_line_id_mm": 16,
        "recommended_oil_grade": "vg_46",
        "recommended_system_type": "dual_circuit",
    },
    {
        "boat_type": "superyacht",
        "loa_min_m": 35,
        "loa_max_m": 60,
        "typical_rudder_force_kn": 250,
        "recommended_cylinder_bore_mm": 150,
        "recommended_cylinder_stroke_mm": 400,
        "recommended_pump_displacement_cm3": None,
        "recommended_pump_flow_lpm": 40,
        "recommended_line_id_mm": 20,
        "recommended_oil_grade": "vg_46",
        "recommended_system_type": "dual_circuit",
    },
]
```

---

---

### Zusaetzliche Hinweise fuer AYDI-Integration

#### Visuelle Analyse (Pipeline B) — Erkennbare Merkmale

AYDI Pipeline B (Visual Analysis via Claude Vision) kann folgende hydraulikbezogene Merkmale in Fotos erkennen:

| Merkmal | Erkennbarkeit | Confidence | Hinweis |
|---------|--------------|-----------|---------|
| Oelleckage am Zylinder | Hoch (Oelfilm/Tropfen sichtbar) | visual_high | Bei guter Beleuchtung |
| Korrosion Zylindergehaeuse | Hoch (weisse Ablagerungen) | visual_high | Insbesondere Aluminium |
| Schlauchzustand (Risse, Knicke) | Mittel | visual_medium | Oberflaechenrisse erkennbar |
| Fitting-Zustand | Mittel | visual_medium | Korrosion, Leckspuren |
| Oelfarbe im Reservoir (Sichtglas) | Niedrig–Mittel | visual_low bis visual_medium | Nur bei klarem Sichtglas |
| Schlauch-Aufblaehung | Niedrig | visual_low | Nur im Vergleich mit Referenz |
| Interne Leckage | Nicht erkennbar | visual_insufficient | Nur durch Drift-Test |
| Dichtungszustand | Nicht erkennbar | visual_insufficient | Verdeckt |
| Oelqualitaet (Wasser, Partikel) | Nicht erkennbar | visual_insufficient | Laboranalyse noetig |

#### Pipeline-A-Integration (Structured Data)

Wenn CAD-Daten oder Herstellerangaben vorliegen, kann AYDI folgende Berechnungen automatisiert durchfuehren:

1. **Ruderkraft-Berechnung** aus Rumpf-CAD (Lateralplan-Ableitung, Ruderflaeche, Profildaten)
2. **Zylinder-Dimensionierungspruefung** (ist der verbaute Zylinder ausreichend?)
3. **Leitungsdimensionierung** (stimmen die Querschnitte zum Volumenstrom?)
4. **Wartungs-Zeitberechnung** (wann steht die naechste Wartung an, basierend auf Betriebsstunden und Alter?)
5. **Kosten-Abschaetzung** fuer Wartung und Reparatur (parametrisch aus Bootskategorie)

Confidence bei vorhandenen CAD-Daten: `measured` oder `calculated`.
Confidence bei reiner Schnellanalyse (Level 1): `estimated` oder `benchmark`.

#### Pipeline-C-Integration (Text Data)

Aus Service-Berichten, Gutachten und Logbuechern kann AYDI folgende Informationen extrahieren:

- Letztes Oelwechsel-Datum und Oel-Typ
- Dokumentierte Leckagen, Reparaturen, Dichtungstausch
- Symptom-Beschreibungen (schwammiges Steuer, Geraeusche, Drift)
- Betriebsstunden und Fahrtenmeilenangaben
- Werft-Empfehlungen und offene Punkte

Confidence: `documented`.

---

*Ende des Wissensdokuments 20.02 — Hydraulische Steuerung*
*AYDI v6 Knowledge Engineering — Stand 2026-05-02*
