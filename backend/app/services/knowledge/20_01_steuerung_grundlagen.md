---
title: "Steueranlagen Grundlagen — Ruderanlage, Steuerungsprinzipien, Bauarten"
kategorie: "20 Steueranlagen"
unterkategorie: "20.01 Grundlagen und Bauarten"
version: "1.0.0"
datum: "2026-05-02"
autor: "AYDI Research"
status: "validated"
confidence_quellen:
  - measured: "Hersteller-TDS, ISO-Normen, CE-Zertifizierungen, Klassifikationsgesellschaften"
  - documented: "Hersteller-Kataloge, Werftunterlagen, Montageleitfäden, Surveyberichte"
  - estimated: "Erfahrungswerte, Werft-Konsens, Sachverständigen-Praxis"
---

# 20.01 — Steueranlagen Grundlagen: Ruderanlage, Steuerungsprinzipien, Bauarten im Yachtbau

> **AYDI Wissensdatei 20.01** — Kategorie 20: Steueranlagen und Ruderanlagen
> **Confidence-Quelle:** measured (Hersteller-TDS, ISO-Normen), documented (Hersteller-Kataloge, Werftunterlagen), estimated (Erfahrungswerte, Werft-Konsens)
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
8. [FAQ](#8-faq)
9. [Glossar](#9-glossar)
10. [Schnell-Referenz](#10-schnell-referenz)
11. [ANHANG A–H — Fallstudien](#11-anhang-a–h-fallstudien)
12. [ANHANG I–R — Pydantic v2 Modelle](#12-anhang-i–r-pydantic-v2-modelle)

---

## 1. Einführung und Übersicht

### 1.1 Definition und Funktion der Steueranlage

Die Steueranlage einer Yacht umfasst die Gesamtheit aller mechanischen, hydraulischen und/oder elektrischen Komponenten, die die vom Rudergänger am Steuerrad oder an der Pinne eingebrachte Steuerbewegung auf das Ruderblatt übertragen. Sie ist das sicherheitskritischste System an Bord — ein Totalausfall der Steueranlage auf See stellt eine unmittelbare Gefahr für Schiff und Besatzung dar.

Die Steueranlage erfüllt drei Kernfunktionen:

1. **Kurssteuerung** — Übertragung des Steuerwunsches vom Bedienelement (Steuerrad, Pinne) auf das Ruderblatt zur gezielten Kursänderung oder Kurshaltung
2. **Rückmeldung (Feedback)** — Rückübertragung der am Ruderblatt wirkenden hydrodynamischen Kräfte an den Rudergänger, damit dieser das Verhalten des Schiffes spürt (Ruderdruck, Strömungsabriss)
3. **Haltefunktion** — Fixierung des Ruders in einer bestimmten Stellung, insbesondere bei Autopilot-Betrieb oder unter Windfahnensteuerung

### 1.2 Sicherheitsrelevanz

Die Steueranlage gehört gemäß allen gängigen Klassifikationsgesellschaften (Lloyd's, GL/DNV, BV, RINA, ABS) zu den **sicherheitskritischen Systemen der Kategorie 1**. Dies bedeutet:

- **Redundanzanforderung:** Auf Yachten ab 24 m LH (Rumpflänge) schreiben die meisten Klassifikationsgesellschaften ein Notruder oder eine redundante Steuerung vor
- **Materialanforderungen:** Alle tragenden Komponenten der Steueranlage müssen aus korrosionsbeständigen Werkstoffen gefertigt und für die erwarteten Maximallasten dimensioniert sein
- **Inspektionsintervalle:** Jährliche Sichtprüfung, alle 5 Jahre Detailinspektion mit Ausbau kritischer Komponenten (Ruderschaft, Lager, Quadrant)
- **Notsteuerung:** Jede Yacht sollte eine Möglichkeit zur Notsteuerung haben — bei Segelyachten typischerweise eine Notpinne, die direkt auf den Ruderkopf aufgesetzt wird

**Unfallstatistik (MAIB, BSU, USCG zusammengefasst):**

| Kategorie | Anteil an Steuerversagern |
|-----------|--------------------------|
| Seilzugriss/Kettenbruch | 28 % |
| Hydraulikleck | 22 % |
| Ruderlagerschaden | 18 % |
| Ruderblattabriss | 12 % |
| Steuerrad-Kopplungsfehler | 8 % |
| Korrosionsversagen | 7 % |
| Sonstige | 5 % |

### 1.3 Normative Grundlagen

**ISO 10592:1994 — Small craft — Hydraulic steering systems**
Definiert Anforderungen an hydraulische Steuersysteme für Sportboote bis 24 m. Umfasst Drucktests, Leckraten, Zylinderauslegung und Schlauchspezifikationen.

**ISO 8847:2004 — Small craft — Steering gear — Wire rope and pulley steering systems**
Regelt Seilzugsteuerungen: minimale Seilstärken, Umlenkrollendurchmesser, Endverbindungen, Federrückstellung.

**ISO 8848:2020 — Small craft — Remote steering systems**
Übergreifende Norm für alle ferngesteuerten Steueranlagen. Definiert maximale Ruderkräfte am Steuerrad, Rückfallebenen und Prüfverfahren.

**ISO 25197:2020 — Small craft — Electrical/electronic control systems for steering, shift and throttle**
Spezifisch für elektrische und elektronische Steuersysteme: Redundanz, Fehlertoleranz, Rückfallmodi.

**CE-Kennzeichnung (Richtlinie 2013/53/EU):**
Steueranlagen fallen unter die grundlegenden Sicherheitsanforderungen der EU-Sportbootrichtlinie. Der Hersteller muss die Konformität mit den einschlägigen harmonisierten Normen nachweisen.

### 1.4 Historische Entwicklung

**Vor 1850 — Pinne als Urform:**
- Direkte Verbindung Rudergänger → Ruderblatt über Pinne (Helmstock)
- Auf großen Schiffen: Kolderstock (vertikale Hebelvorrichtung unter Deck)
- Steuerruder als Heckruder seit dem 12. Jahrhundert in Europa nachweisbar
- Seitenruder bei Wikingerschiffen und antiken Mittelmeerfahrern

**1850–1920 — Mechanisierung:**
- Erste Seilzugsteuerungen auf Großseglern (Drahtseile über Umlenkrollen)
- Dampfschiffe: Dampfsteuermaschinen (Steam Steering Engines)
- Erstes Patent für Zahnstangensteuerung (Rack-and-Pinion) für Yachten um 1890
- Kettensteuerungen dominieren im Bereich 10–25 m

**1920–1960 — Hydraulik hält Einzug:**
- Erste hydraulische Steueranlagen auf Motoryachten ab ca. 1930
- Wagner (Heidenheim) und MacTaggart Scott als Pioniere
- Manuelle hydraulische Pumpen als Standardlösung für Motoryachten >12 m
- Edson Corporation (USA) begründet 1859, wird zum führenden Anbieter mechanischer Steuerungen

**1960–1990 — Moderne Yachtsteuerung:**
- 1968: Whitlock Steering (UK) entwickelt die Cobra-Serie für Segelyachten
- 1972: Jefa Marine (Dänemark) gegründet — spezialisiert auf Segelyacht-Steuerungen
- 1975: Hynautic (USA) bringt kompakte hydraulische Steuersysteme für Motorboote
- Teleflex Marine (später SeaStar/Dometic) etabliert Seilzugsteuerungen als Massenprodukt
- Kobelt Manufacturing (Kanada) spezialisiert sich auf schwere hydraulische Steuerungen

**1990–heute — Elektronik und Integration:**
- Fly-by-Wire-Steuerung auf Superyachten
- Joystick-Steuerung (Volvo IPS, Zeus, Axius)
- Integration von Autopilot und manueller Steuerung in ein System
- Elektrohydraulische Systeme als Standard auf Motoryachten >15 m
- Jefa Marine wird zum europäischen Marktführer für Segelyacht-Steuerungen

### 1.5 Systemübersicht: Komponenten einer Steueranlage

Eine vollständige Steueranlage besteht aus folgenden Hauptkomponenten:

```
BEDIENELEMENT                    ÜBERTRAGUNG                     RUDEREINHEIT
┌─────────────┐                ┌──────────────────┐             ┌──────────────┐
│ Steuerrad    │                │ Seilzug/Kette    │             │ Quadrant     │
│ oder Pinne   │───Steuer──────│ Zahnstange       │─────────────│ Tillerarm    │
│ oder Joystick│   säule       │ Hydraulikleitung  │             │ Ruderschaft  │
│              │                │ Elektrische       │             │ Ruderlager   │
│              │                │ Signalleitung     │             │ Ruderblatt   │
└─────────────┘                └──────────────────┘             └──────────────┘
```

**Bedienelement:**
- Steuerrad (Radsteuerung): Standard auf Yachten >8 m, Durchmesser 600–1200 mm
- Pinne (Tillersteuerung): Standard auf Yachten <9 m, Länge 800–1500 mm
- Joystick: Ergänzend bei Motorbooten mit IPS/Pod-Antrieb
- Tiller-Pilot (Pinnenpilot): Elektrischer Linearantrieb auf Pinne

**Steuersäule (Pedestal):**
- Trägt das Steuerrad und enthält die Steuergetriebe-Einheit
- Materialien: Edelstahl 316L, Aluminium (eloxiert), GFK, Carbon
- Enthält bei Radsteuerung die Kettenrad/Ritzel-Einheit
- Optional: Kompass-Aufnahme, Instrumenten-Pod, Motorhebel-Integration

**Übertragung:**
- Seilzug: Edelstahl-Drahtseil 6×19 oder 7×19, ∅3–6 mm, mit Umlenkrollen
- Kette: Geall/Morse-Kette, Teilung 3/8" oder 1/2"
- Zahnstange: Rack-and-Pinion-Getriebe, gehärteter Stahl
- Hydraulik: Ölleitung mit Pumpe und Zylinder
- Elektrisch: Signal- und Leistungskabel

**Rudereinheit:**
- Quadrant: Alu/Edelstahl-Segment, 90°–120° Bogen, auf Ruderkopf montiert
- Tillerarm (Ruderhebel): Gerade oder gekröpft, Stahl/Alu
- Ruderschaft: Edelstahl 316L oder Aquamet 22, ∅25–80 mm
- Ruderlager: Oben (Kokerrohr), Unten (Skeg oder freihängend)
- Ruderblatt: GFK, CFK, Schaum- oder Balsakeern, Edelstahl-Innengerüst

### 1.6 Klassifizierung nach Bootstyp

| Bootstyp | Typische Steuerung | Rückfall-Ebene |
|----------|-------------------|----------------|
| Jolle (<6 m) | Pinne direkt | Paddel |
| Daysailer (6–8 m) | Pinne direkt | Notpaddel/Hilfsruder |
| Fahrtensegler (8–12 m) | Seilzug- oder Kettensteuerung | Notpinne |
| Fahrtensegler (12–16 m) | Kette oder Hydraulik | Notpinne + ggf. Notpumpe |
| Fahrtensegler (16–24 m) | Hydraulisch | Notpinne + Handpumpe |
| Blauwasser (>16 m) | Hydraulisch, redundant | Notpinne + zweite Pumpe |
| Motorboot (<8 m) | Seilzug oder Zahnstange | Außenborder-Lenkung |
| Motorboot (8–14 m) | Hydraulisch | Notsteuerung achtern |
| Motoryacht (14–24 m) | Elektrohydraulisch | Handpumpe + Notsteuerung |
| Superyacht (>24 m) | Elektrohydraulisch, redundant | Zweites System, Notpumpe |

---

## 2. Grundlagen und Theorie

### 2.1 Ruderhydrodynamik

Das Ruderblatt ist ein Strömungskörper (Profil), der — wenn aus der Mittschiffsebene ausgelenkt — eine seitliche Kraft erzeugt. Diese Kraft wirkt als Drehmoment um die Hochachse des Schiffes und bewirkt eine Kursänderung.

**Grundlegende Strömungsmechanik am Ruder:**

Die Strömung am Ruderblatt folgt den Gesetzen der Tragflügeltheorie. Das Ruderblatt ist ein symmetrisches Profil (typisch NACA 0012, NACA 0015 oder NACA 0018), das bei Auslenkung (Anstellwinkel α) eine Auftriebskraft (Lift) senkrecht zur Anströmung und eine Widerstandskraft (Drag) parallel zur Anströmung erzeugt.

**Auftriebsbeiwert C_L:**

```
C_L = dC_L/dα × α     (im linearen Bereich, α < ~15°)
```

Für typische Ruderprofile:
- NACA 0012: dC_L/dα ≈ 0,068 pro Grad (bei Re = 1×10⁶)
- NACA 0015: dC_L/dα ≈ 0,065 pro Grad
- NACA 0018: dC_L/dα ≈ 0,060 pro Grad

**Widerstandsbeiwert C_D:**

```
C_D = C_D0 + C_L² / (π × AR × e)
```

Wobei:
- C_D0 = Profilwiderstand bei α=0° (typisch 0,006–0,012)
- AR = Aspektverhältnis (Ruderhöhe² / Ruderfläche)
- e = Oswald-Effizienzfaktor (typisch 0,7–0,9)

**Strömungsabriss (Stall):**

Bei Überschreiten des kritischen Anstellwinkels (typisch 15°–20° für Yachtruder) reißt die Strömung auf der Saugseite ab. Folgen:
- Schlagartiger Verlust der Ruderkraft
- Am Steuerrad spürbar als plötzliches Leichtwerden des Ruders
- Im Extremfall: Kavitation und Vibration

**Einfluss der Propellerströmung:**

Bei Motoryachten befindet sich das Ruder typischerweise im Propellerstrahl. Dies hat weitreichende Auswirkungen:
- Erhöhte Anströmgeschwindigkeit am Ruder → mehr Ruderkraft bei niedrigen Bootsgeschwindigkeiten
- Drall des Propellerstrahls → asymmetrische Rudercharakteristik (unterschiedliche Ruderwirkung Bb/Stb)
- Bei Wellenanlage mit hohem P/D-Verhältnis (Steigung/Durchmesser): deutlicher Radeffekt

### 2.2 Ruderkräfte-Berechnung

Die Berechnung der am Ruderblatt angreifenden Kräfte ist fundamental für die Dimensionierung der gesamten Steueranlage.

**Ruderkraft (Querkraft am Ruder):**

```
F_R = 0,5 × ρ × v² × A_R × C_L
```

Wobei:
- F_R = Ruderkraft [N]
- ρ = Dichte des Wassers [kg/m³] (Seewasser: 1025 kg/m³)
- v = Anströmgeschwindigkeit am Ruder [m/s]
- A_R = Ruderfläche [m²]
- C_L = Auftriebsbeiwert bei gegebenem Anstellwinkel [-]

**Praktische Überschlagsformel für Yachten (nach Larsson/Eliasson):**

```
F_R = 580 × A_R × v² × sin(α)     [N]
```

Wobei:
- A_R in m²
- v in m/s (Bootsgeschwindigkeit, nicht Anströmgeschwindigkeit)
- α = Ruderwinkel in Grad

**Rechenbeispiel — 12 m Fahrtensegler:**

```
Ruderfläche A_R = 0,35 m²
Rumpfgeschwindigkeit v = 7 kn = 3,6 m/s
Ruderwinkel α = 35° (Maximalausschlag)

F_R = 580 × 0,35 × 3,6² × sin(35°)
F_R = 580 × 0,35 × 12,96 × 0,574
F_R ≈ 1.510 N ≈ 154 kgf
```

**Rechenbeispiel — 15 m Motoryacht:**

```
Ruderfläche A_R = 0,25 m² (kleinere Ruder durch Propellerstrahl)
Geschwindigkeit v = 18 kn = 9,26 m/s
Ruderwinkel α = 35°

F_R = 580 × 0,25 × 9,26² × 0,574
F_R = 580 × 0,25 × 85,75 × 0,574
F_R ≈ 7.145 N ≈ 729 kgf
```

Dieses Beispiel zeigt, warum Motoryachten deutlich stärkere (hydraulische) Steuerungen benötigen als Segelyachten gleicher Länge.

### 2.3 Drehmoment am Ruderschaft

Das entscheidende Maß für die Dimensionierung der Steueranlage ist nicht die Ruderkraft selbst, sondern das Drehmoment am Ruderschaft — also die Kraft, die die Steueranlage aufbringen muss, um das Ruder gegen den Wasserdruck zu bewegen.

**Drehmoment T_R:**

```
T_R = F_R × (x_CP - x_Schaft) × c
```

Wobei:
- T_R = Drehmoment am Ruderschaft [Nm]
- F_R = Ruderkraft [N]
- x_CP = Abstand des Druckmittelpunkts von der Rudervorderkante [m]
- x_Schaft = Abstand der Schaftachse von der Rudervorderkante [m]
- c = Rudertiefe (Chord) [m]

**Druckmittelpunkt (Center of Pressure):**

Der Druckmittelpunkt wandert mit dem Anstellwinkel:
- α = 0°: x_CP ≈ 0,25 × c (Viertelpunkt)
- α = 10°: x_CP ≈ 0,28 × c
- α = 20°: x_CP ≈ 0,32 × c
- α = 35°: x_CP ≈ 0,38 × c

**Balancierung des Ruders:**

Die Position des Ruderschafts relativ zum Druckmittelpunkt bestimmt das Steuermoment. Durch Vorverlagerung von Ruderfläche vor den Schaft (Balancierung) wird das Moment reduziert:

| Balance-Grad | Schaftposition | Effekt |
|-------------|---------------|--------|
| 0 % (unbalanciert) | Rudervorderkante | Maximales Moment, starke Rückmeldung |
| 15–18 % | 15–18 % hinter VK | Moderate Reduktion, gute Rückmeldung |
| 20–25 % (Standard) | 20–25 % hinter VK | Optimaler Kompromiss Kraft/Rückmeldung |
| 30–35 % | 30–35 % hinter VK | Stark reduziertes Moment, schwache Rückmeldung |
| >38 % (überbalanciert) | >38 % hinter VK | GEFAHR: Ruder schlägt unkontrolliert aus |

> ⚠️ **ZU PRÜFEN (Audit):** Gefahrenschwelle Überbalancierung >38 % (diese Tabelle) vs. >35 % (Abschnitt 8, F20, und Pydantic-Validator `warn_overbalanced` in Anhang I, der bei >35 % einen Fehler wirft) — widersprüchlicher Grenzwert für einen sicherheitsrelevanten Zustand (Kontrollverlust). Richtung nicht zweifelsfrei belegbar, Quelle nicht verifizierbar. Confidence measured → estimated (unverifiziert).

**Typische Balance-Grade:**
- Segelyacht-Spatenruder: 17–22 %
- Segelyacht-Skeg-Ruder: 8–15 % (weniger Balance nötig durch Skeg-Stützung)
- Langkiel-Ruder: 0–10 %
- Motoryacht-Ruder: 20–28 % (höhere Kräfte → mehr Balance)
- Rennboot-Ruder: 15–20 % (mehr Rückmeldung erwünscht)

**Rechenbeispiel — Drehmoment 12 m Fahrtensegler (Spatenruder):**

```
F_R = 1.510 N (aus Abschnitt 2.2)
Rudertiefe c = 0,55 m
Schaft bei 20 % hinter VK → x_Schaft = 0,20 × 0,55 = 0,11 m
Druckmittelpunkt bei α=35°: x_CP = 0,38 × 0,55 = 0,209 m
Hebelarm = 0,209 - 0,11 = 0,099 m

T_R = 1.510 × 0,099
T_R ≈ 150 Nm
```

**Rechenbeispiel — Drehmoment 15 m Motoryacht:**

```
F_R = 7.145 N (aus Abschnitt 2.2)
Rudertiefe c = 0,40 m
Schaft bei 25 % hinter VK → x_Schaft = 0,25 × 0,40 = 0,10 m
Druckmittelpunkt bei α=35°: x_CP = 0,38 × 0,40 = 0,152 m
Hebelarm = 0,152 - 0,10 = 0,052 m

T_R = 7.145 × 0,052
T_R ≈ 371 Nm
```

### 2.4 Steuerübersetzung und Hebelwirkung

Die Steuerübersetzung ist das Verhältnis zwischen der Drehbewegung am Steuerrad und der resultierenden Ruderbewegung. Sie bestimmt, wie viele Umdrehungen des Steuerrads nötig sind, um das Ruder von Hartbackbord nach Hartsteuerbord zu bewegen (Lock-to-Lock).

**Gesamtübersetzung:**

```
i_ges = i_Getriebe × i_Übertragung × i_Quadrant
```

Wobei:
- i_Getriebe = Übersetzung im Steuergetriebe (Pedestal)
- i_Übertragung = Übersetzungsverhältnis in der Übertragungskette
- i_Quadrant = Verhältnis Quadrant-Radius zu Ruderblatt-Hebelarm

**Lock-to-Lock-Umdrehungen:**

```
n_LL = (2 × α_max) / (360° / i_ges)
```

Typische Werte:
- Segelyacht 8–10 m: 2,5–3,5 Umdrehungen Lock-to-Lock
- Segelyacht 10–14 m: 3,0–4,5 Umdrehungen
- Segelyacht 14–20 m: 3,5–5,0 Umdrehungen
- Motoryacht <12 m: 3,0–4,0 Umdrehungen
- Motoryacht 12–18 m: 4,0–6,0 Umdrehungen
- Motoryacht >18 m: 5,0–8,0 Umdrehungen (Power-Assist)

**Handkraft am Steuerrad:**

Die maximal akzeptable Handkraft am Steuerrad ist durch ISO 8848 geregelt:

| Betriebsbedingung | Max. Handkraft |
|-------------------|---------------|
| Normalbetrieb | 15 N (Felgenkraft) |
| Notsteuerung | 35 N (Felgenkraft) |
| Dauerbetrieb (>30 min) | 10 N |

**Zusammenhang Handkraft — Ruderdrehmoment:**

```
F_Hand × r_Rad × i_ges × η = T_Ruder
```

Wobei:
- F_Hand = Kraft an der Radfelge [N]
- r_Rad = Radius des Steuerrads [m]
- i_ges = Gesamtübersetzung [-]
- η = Gesamtwirkungsgrad der Übertragung (typisch 0,55–0,85)
- T_Ruder = erforderliches Drehmoment am Ruderschaft [Nm]

**Wirkungsgrade verschiedener Übertragungen:**

| Übertragungstyp | Wirkungsgrad η |
|-----------------|---------------|
| Seilzug (gut gewartet) | 0,70–0,80 |
| Seilzug (schlecht gewartet) | 0,45–0,60 |
| Kette (gut gewartet) | 0,75–0,85 |
| Kette (schlecht gewartet) | 0,55–0,70 |
| Zahnstange | 0,80–0,90 |
| Hydraulik (manuell) | 0,50–0,65 |
| Hydraulik (Power-Assist) | n/a (Kraft durch Pumpe) |

### 2.5 Ruderwinkel und Ruderlage

**Maximaler Ruderausschlag:**

Der maximale Ruderausschlag (Ruderlage) wird durch mechanische Anschläge begrenzt:

| Bootstyp | Max. Ruderlage | Anmerkung |
|----------|---------------|-----------|
| Segelyacht (Fahrt) | ±35° | Standard, ISO-konform |
| Segelyacht (Regatta) | ±40° | Mehr Manövrierfähigkeit, höhere Lasten |
| Motoryacht (Verdränger) | ±35° | Standard |
| Motoryacht (Gleiter) | ±30° | Bei Gleitfahrt weniger Ausschlag nötig |
| Katamaran | ±35° pro Ruder | Beide Ruder synchron oder unabhängig |
| Superyacht | ±35° | Redundante Systeme |

**Ruderlage vs. Querkraft:**

Die Ruderkraft steigt nicht linear mit dem Ruderwinkel — sie folgt der sin-Funktion des Anstellwinkels bis zum Strömungsabriss:

```
Relative Ruderkraft (% der Maximalkraft):

α =  5°  →  14 %
α = 10°  →  28 %
α = 15°  →  42 %
α = 20°  →  55 %
α = 25°  →  68 %
α = 30°  →  80 %
α = 35°  →  92 %
α = 40°  → ~95 % (nahe Stall, abhängig vom Profil)
α = 45°  → Strömungsabriss, Kraft fällt ab
```

**Neutrale Ruderlage:**

Die „Mittschiffs"-Stellung des Ruders ist definiert als 0° Ruderlage. In der Praxis weicht die neutrale Ruderlage häufig leicht ab:
- Propeller-Radeffekt: 1–3° Offset bei Einschrauber
- Trimm des Schiffes: Veränderliche Neutrallage bei unterschiedlicher Beladung
- Segelboot unter Segeln: Luvgierigkeit erzeugt permanenten Ruderwinkel (typisch 3–5°)

### 2.6 Rückmeldung (Steering Feedback)

Das Steuergefühl (Feedback) ist ein zentrales Qualitätsmerkmal einer Steueranlage. Der Rudergänger muss die am Ruder wirkenden Kräfte spüren, um Geschwindigkeit, Abdrift und Strömungszustand intuitiv erfassen zu können.

**Arten der Rückmeldung:**

| Rückmeldungstyp | Beschreibung | Bewertung |
|-----------------|-------------|-----------|
| Direkte mechanische | Kraft vom Ruder wird 1:1 (abzüglich Übersetzung) an Rad/Pinne übertragen | Beste Rückmeldung (Pinne, Kette) |
| Gedämpfte mechanische | Kraft wird mit Reibungsverlusten übertragen | Gut (Seilzug) |
| Hydraulische | Ruderdruck wird durch Öl an Pumpe rückübertragen | Moderat (Helm-Pumpe) |
| Keine | Power-Steuerung ohne Rückstellkraft | Schlecht (Fly-by-Wire ohne Feedback-Motor) |

**Feedback bei verschiedenen Steuerungssystemen:**

- **Pinne:** 100 % direktes Feedback, der Rudergänger spürt jede Böe und jede Welle am Ruder. Ermüdend bei schwerem Wetter, aber unübertroffenes Steuergefühl.
- **Kettensteuerung:** 85–90 % Feedback-Übertragung. Kette und Quadrant haben geringe Reibung. Leichtes Spiel möglich.
- **Seilzugsteuerung:** 60–75 % Feedback. Seilzüge haben inherente Reibung an Umlenkrollen, die das Feedback dämpft. Längung der Seile kann Spiel verursachen.
- **Zahnstangensteuerung:** 70–80 % Feedback. Gut definierte Mechanik, aber Zahnspiel möglich.
- **Hydraulische Steuerung (ohne Servo):** 30–50 % Feedback. Hydrauliköl überträgt Druck, aber Kompressibilität und Reibung in Dichtungen dämpfen stark.
- **Hydraulische Steuerung (mit Servo):** 0–10 % Feedback. Fast ausschließlich durch elektronische Simulation.
- **Elektrische Steuerung (Fly-by-Wire):** 0 % natürliches Feedback. Muss durch Feedback-Motoren simuliert werden.

### 2.7 Ruderkraft-Diagramme (Qualitative Darstellung)

**Ruderkraft über Geschwindigkeit (bei konstant α=20°):**

```
Kraft [N]
  3000 ┤                                            ╭──
       │                                       ╭────╯
  2500 ┤                                  ╭────╯
       │                             ╭────╯
  2000 ┤                        ╭────╯
       │                   ╭────╯
  1500 ┤              ╭────╯
       │         ╭────╯
  1000 ┤    ╭────╯
       │╭───╯
   500 ┤╯
       │
     0 ┼────┬────┬────┬────┬────┬────┬────┬────→ v [kn]
       0    2    4    6    8   10   12   14

  ——— Ruderkraft steigt quadratisch mit der Geschwindigkeit!
```

**Ruderkraft über Ruderwinkel (bei konstant v=6 kn):**

```
Kraft [N]
  1800 ┤                                    ╭─── ← Stall-Beginn
       │                               ╭────╯
  1500 ┤                          ╭─────╯
       │                     ╭────╯
  1200 ┤                ╭────╯
       │           ╭────╯
   900 ┤      ╭────╯
       │  ╭───╯
   600 ┤──╯
       │╭╯
   300 ┤╯
       │
     0 ┼──┬──┬──┬──┬──┬──┬──┬──┬──→ α [°]
       0  5 10 15 20 25 30 35 40

  ——— Annähernd sinusförmiger Anstieg bis zum Strömungsabriss
```

### 2.8 Dimensionierungsrichtlinien

**Ruderflächen-Faustformeln:**

| Bootstyp | Ruderfläche | Basis |
|----------|-----------|-------|
| Segelyacht (Spatenruder) | 1,5–2,5 % der LWL × T_c | LWL = Wasserlinienlänge, T_c = Tiefgang |
| Segelyacht (Skeg-Ruder) | 2,0–3,0 % der LWL × T_c | Skeg-Anteil mitgerechnet |
| Segelyacht (Langkiel) | 3,0–4,5 % des Lateralplans | Gesamte Ruderfläche inkl. Kielende |
| Motoryacht (Verdränger) | 1,5–2,0 % der LWL × T | T = Tiefgang |
| Motoryacht (Gleiter) | 1,0–1,5 % der LWL × T | Kleinere Ruder durch Hochgeschwindigkeit |

**Ruderschaft-Dimensionierung (Vereinfachte Berechnung nach GL):**

```
d_min = k × ∛(T_R_max)     [mm]
```

Wobei:
- d_min = minimaler Schaftdurchmesser [mm]
- k = Materialfaktor (Edelstahl 316L: 4,8; Aquamet 22: 4,2; Bronze: 5,5)
- T_R_max = maximales Drehmoment [Nm]

**Rechenbeispiel:**

```
T_R_max = 150 Nm (12 m Segelyacht)
Material: Edelstahl 316L → k = 4,8

d_min = 4,8 × ∛150 = 4,8 × 5,31 = 25,5 mm

→ Nächste Standardgröße: ∅30 mm (mit Sicherheitsfaktor)
```

**Typische Ruderschaftdurchmesser:**

| Bootslänge | Segelyacht | Motoryacht |
|-----------|-----------|-----------|
| 8 m | ∅25 mm | ∅25 mm |
| 10 m | ∅30 mm | ∅30 mm |
| 12 m | ∅35 mm | ∅35–40 mm |
| 14 m | ∅40 mm | ∅45 mm |
| 16 m | ∅45 mm | ∅50 mm |
| 18 m | ∅50 mm | ∅55–60 mm |
| 20 m | ∅55 mm | ∅65 mm |
| 24 m | ∅60–65 mm | ∅70–80 mm |

### 2.9 Ruderprofile im Vergleich

**NACA 0012 (12 % Dicke):**
- Schlankes Profil mit geringem Widerstand
- Strömungsabriss bei ca. 16° Anstellwinkel
- Geeignet für: schnelle Yachten, Rennboote, Multihulls
- Nachteil: Früher Stall, weniger Reservekraft

**NACA 0015 (15 % Dicke):**
- Standardprofil für die meisten Yacht-Ruder
- Strömungsabriss bei ca. 18° Anstellwinkel
- Geeignet für: universeller Einsatz, Fahrtensegler, Motoryachten
- Bester Kompromiss zwischen Widerstand und maximaler Ruderkraft

**NACA 0018 (18 % Dicke):**
- Dickes Profil mit hoher Maximalkraft
- Strömungsabriss bei ca. 20° Anstellwinkel
- Geeignet für: schwere Fahrtenyachten, Langfahrt, Langkiel-Boote
- Nachteil: Höherer Profilwiderstand

**Keilprofil (Flat Plate + Trailing Edge):**
- Einfachstes Profil: abgeflachte Platte mit Hinterkante
- Geringste Leistung, aber billig herzustellen
- Nur für kleine Boote, Ruderboote, Beiboote

**Göttinger Profil (GOE 795 u.ä.):**
- Historische Profile aus den Göttinger Profilkatalogen
- Teilweise auf älteren Yachten verwendet
- Weitgehend durch NACA-Profile abgelöst

### 2.10 Rudertypen nach Lagerung

**Spatenruder (Spade Rudder):**
- Nur oben am Schaft gelagert (freitragend)
- Maximale Manövrierfähigkeit durch freie Anströmung
- Empfindlich gegen Grundberührung und Treibgut
- Standard auf modernen Segelyachten
- Schaft muss für Biegemoment dimensioniert werden (Kragarm)
- Hohe Lagerbelastung im Kokerbereich

**Skeg-Ruder (Skeg-Hung Rudder):**
- Oben am Koker, unten am Skeg gelagert (zweifach gelagert)
- Skeg schützt Ruder vor Treibgut und gibt Seitenführung
- Reduzierte Ruderwirkung bei kleinen Winkeln (Skeg ist Strömungshindernis)
- Standard auf Fahrtenyachten der robusten Bauart
- Geringere Lagerbelastung durch zweifache Lagerung

**Langkiel-Ruder (Full Keel Rudder):**
- Am Achterkanten des Langkiels angelenkt
- Robusteste Bauform, sehr gut geschützt
- Schlechteste Ruderwirkung bei niedrigen Geschwindigkeiten
- Typisch für traditionelle Bauart, Blauwasseryachten, Arbeitssegel
- Ruder kann nicht abfallen (kein Ruderblattverlust möglich)

**Zwillingsruder (Twin Rudders):**
- Zwei Ruder, seitlich versetzt, typisch bei breiten Hecks
- Jedes Ruder im Propellerstrahl (Katamaran) oder im ablösenden Strom
- Unter Krängung: Leeruder tief im Wasser → bessere Ruderwirkung bei Lage
- Standard auf modernen Breitheckyachten (z.B. Jeanneau, Beneteau)
- Erfordert Synchronisation beider Ruder

**Flossenruder (Flap Rudder / Becker Rudder):**
- Hauptruder mit angelenkter Hinterkante (Flap)
- Deutlich höhere Seitenkraft bei gleichem Anstellwinkel
- Einsatz auf Superyachten, Fähren, kommerziellen Schiffen
- Komplexere Mechanik, höhere Kosten

### 2.11 Autopilot-Integration

Die Integration eines Autopiloten stellt besondere Anforderungen an die Steueranlage:

**Hydraulische Integration:**
- Autopilot-Pumpe wird parallel zur manuellen Pumpe an den Steuerzylinder angeschlossen
- Bypass-Ventil ermöglicht Umschaltung manuell/Autopilot
- Ölvolumen muss für beide Systeme ausreichen
- Druckverluste in der Leitung müssen berücksichtigt werden

**Mechanische Integration (Linear Drive):**
- Linearantrieb greift am Quadranten oder Tillerarm an
- Bei Seilzugsteuerung: Antrieb über eigene Verbindung zum Quadranten
- Mechanische Entkopplung bei manuellem Betrieb (Kupplung oder Freilauf)

**Elektrische Integration:**
- Bei Fly-by-Wire: Autopilot gibt direkt elektrische Signale an Ruderaktuator
- Keine mechanische Umschaltung nötig
- Redundante Signalwege erforderlich

**Autopilot-Ruderkraft-Anforderung:**

| Bootslänge | Verdrängung | Empfohlenes Drehmoment Autopilot |
|-----------|-------------|--------------------------------|
| 8 m | 3 t | 500–800 Nm |
| 10 m | 5 t | 800–1.500 Nm |
| 12 m | 8 t | 1.500–2.500 Nm |
| 14 m | 12 t | 2.500–4.000 Nm |
| 16 m | 18 t | 4.000–6.000 Nm |
| 20 m | 30 t | 8.000–12.000 Nm |

---

## 3. Typenübersicht

### 3.1 Seilzugsteuerung (Wire Rope Steering)

#### 3.1.1 Funktionsprinzip

Die Seilzugsteuerung überträgt die Drehbewegung des Steuerrads über Edelstahl-Drahtseile zum Quadranten auf dem Ruderkopf. Das Grundprinzip:

1. Steuerrad dreht ein Kettenrad (Sprocket) im Pedestal
2. Kette treibt über kurze Strecke (im Pedestal) ein Seilrad an
3. Zwei Drahtseile (Steuerbord und Backbord) laufen von der Seiltrommel über Umlenkrollen zum Quadranten
4. Quadrant dreht den Ruderschaft und damit das Ruderblatt
5. Rückholfedern sorgen für definierte Rückstellkraft

#### 3.1.2 Komponenten im Detail

**Pedestal (Steuersäule):**
- Edelstahl 316L oder Aluminium (seewasserbeständig eloxiert)
- Enthält Kettenrad, Seiltrommel, Lager, ggf. Bremse
- Höhen: 700–1100 mm (Standard 850–950 mm)
- Radaufnahme: Konische Nabe mit Keilnut (Morse-Taper) oder Flansch

**Drahtseile:**
- Material: Edelstahl 316 (korrosionsbeständig) oder verzinkter Stahl (preiswerter, kürzere Lebensdauer)
- Konstruktion: 7×19 (flexibel, Standard) oder 6×19 (steifer, langlebiger)
- Durchmesser: ∅3 mm (Boote <8 m), ∅4 mm (8–12 m), ∅5 mm (12–16 m), ∅6 mm (>16 m)
- Bruchlast (7×19, ∅4 mm, 316 SS): ca. 9,8 kN
- Sicherheitsfaktor: min. 4:1 (ISO 8847)

**Umlenkrollen (Sheaves/Pulleys):**
- Material: Aluminium (eloxiert), Bronze, Edelstahl, Nylon (günstig)
- Minimaldurchmesser: 12× Seildurchmesser (ISO 8847)
- Lager: Kugelgelagert (Standard) oder Gleitlager (günstig, höhere Reibung)
- Seilrillenwinkel: 30°–45° V-Rille
- Befestigung: Decksmontage, Schottmontage oder Decksdurchführung

**Quadrant:**
- Material: Aluminium-Druckguss oder Edelstahl-Schweißkonstruktion
- Bogenwinkel: typisch 90° (±45° Ruderlage) oder 120° (±60°)
- Radius: 100–250 mm (abhängig von Bootsgröße und gewünschter Übersetzung)
- Befestigung: Konus + Keilnut auf Ruderkopf, gesichert mit Krönungsmutter
- Seilbefestigung: Gabelterminal mit Gabelbolzen oder Toggleterminal

**Rückholfedern:**
- Zweck: Definiertes Rückstellmoment, Vermeidung von Seillose
- Bauart: Zugfedern an Quadrant oder Tellerfedern im Pedestal
- Federkraft: Muss Seilgewicht + Reibung überwinden, aber nicht die Rückmeldung überlagern

**Seilspanner (Turnbuckle):**
- Eingebaut in den Seilzug zur Nachspannung
- Spannung: Seil soll handwarm gespannt sein (ca. 5–10 % der Bruchlast als Vorspannung)
- Regelmäßige Nachspannung nötig (Seillängung, Temperatur)

#### 3.1.3 Auslegungsdaten

| Parameter | Wert |
|-----------|------|
| Maximales Drehmoment (12 m Segelyacht) | 100–200 Nm |
| Seilzugkraft bei 150 Nm, Quadrant-Radius 150 mm | 1.000 N |
| Seildurchmesser für 1.000 N (SF=4) | ∅4 mm (BL 9.800 N) |
| Lock-to-Lock | 3,0–4,5 Umdrehungen |
| Wirkungsgrad | 70–80 % |
| Lebensdauer Seile | 5–8 Jahre (Fahrtensegler), 2–4 Jahre (Regatta) |

#### 3.1.4 Vor- und Nachteile

**Vorteile:**
- Bewährte, einfache Technik
- Gutes Feedback (Rückmeldung)
- Leicht und kompakt
- Preisgünstig
- Einfache Installation (Seile um Umlenkrollen)
- Flexible Leitungsführung (Seile können um Ecken geführt werden)

**Nachteile:**
- Seile längen sich (regelmäßiges Nachspannen)
- Seilbruch = Totalausfall (kein Fail-Safe)
- Reibung an Umlenkrollen reduziert Feedback
- Begrenzt auf moderate Ruderdrehmomente (<350 Nm)
- Nicht geeignet für Boote >14 m (zu hohe Kräfte)
- Korrosion der Seile in salzhaltiger Atmosphäre

#### 3.1.5 Wartung

| Intervall | Maßnahme |
|-----------|---------|
| Monatlich | Sichtprüfung Seile auf Litzenbrüche, Knicke |
| Vierteljährlich | Seilspannung prüfen, ggf. nachspannen |
| Halbjährlich | Umlenkrollen auf Leichtgängigkeit prüfen, ggf. schmieren |
| Jährlich | Alle Verbindungen prüfen (Gabelbolzen, Splinte, Schäkel) |
| Alle 5 Jahre | Seile erneuern (oder bei >3 Litzenbrüchen pro 30 cm) |
| Alle 5 Jahre | Umlenkrollen-Lager prüfen/erneuern |

### 3.2 Kettensteuerung (Chain Steering)

#### 3.2.1 Funktionsprinzip

Die Kettensteuerung ersetzt die Drahtseile teilweise oder vollständig durch Rollenketten. Die Kraft wird vom Steuerrad über ein Kettenrad (Sprocket) im Pedestal über eine oder zwei Ketten zum Quadranten übertragen.

Zwei Varianten:
1. **Vollkettensteuerung:** Kette läuft vom Pedestal direkt zum Quadranten (kurze Distanzen)
2. **Ketten-Seil-Kombination:** Kette im Pedestal und am Quadranten, Drahtseile dazwischen (lange Distanzen)

Die Ketten-Seil-Kombination ist die häufigste Bauform auf Segelyachten 9–16 m.

#### 3.2.2 Komponenten

**Kette:**
- Typ: Rollenkette nach DIN 8187 / ISO 606 oder Geall-Kette (proprietär, speziell für Steuerungen)
- Teilung: 3/8" (9,525 mm) für Boote <12 m, 1/2" (12,7 mm) für 12–20 m
- Material: Edelstahl 316 oder verzinkter Stahl (in geschützten Bereichen)
- Geall-Kette: Spezialkette mit flachen Seitenplatten, minimales Spiel

**Kettenrad (Sprocket):**
- Im Pedestal: Zähnezahl typisch 10–15
- Am Quadranten: Als Segment-Zahnkranz (halbes Kettenrad, 90°–120°)
- Teilung muss exakt zur Kette passen

**Übergangs-Stücke (Kette→Seil):**
- Standardisierte Verbindungsglieder
- Seil wird mit Nicopress-Presshülse oder Gabelklemme befestigt
- Kritischer Punkt: Korrosion an der Übergangsstelle

#### 3.2.3 Auslegungsdaten

| Parameter | Wert |
|-----------|------|
| Max. Drehmoment | 150–400 Nm |
| Kettenbruchlast (3/8" Edelstahl) | ca. 12 kN |
| Kettenbruchlast (1/2" Edelstahl) | ca. 22 kN |
| Lock-to-Lock | 3,5–5,0 Umdrehungen |
| Wirkungsgrad | 75–85 % |
| Lebensdauer Kette | 8–15 Jahre |

#### 3.2.4 Vor- und Nachteile

**Vorteile:**
- Kein Nachspannen (Kette längt sich kaum)
- Höhere Belastbarkeit als reine Seilzugsteuerung
- Gutes Feedback
- Langlebiger als Seilzüge
- Formschlüssige Verbindung (kein Schlupf)

**Nachteile:**
- Schwerer als Seilzug
- Teurer als Seilzug
- Kette kann bei Korrosion steif werden
- Kettenbruch = Totalausfall
- Führung der Kette erfordert genaue Ausrichtung
- Geräuschentwicklung bei Seegang

### 3.3 Zahnstangensteuerung (Rack-and-Pinion Steering)

#### 3.3.1 Funktionsprinzip

Bei der Zahnstangensteuerung wird die Drehbewegung des Steuerrads über ein Ritzel (Zahnrad) in eine lineare Bewegung einer Zahnstange umgewandelt. Die Zahnstange ist über Schubstangen (Push-Pull-Kabel oder starre Gestänge) mit dem Tillerarm oder Quadranten verbunden.

Dieses System ist der Standard für:
- Motorboote <10 m mit Außenbordmotor
- Motorboote mit Z-Antrieb (Sterndrive)
- RIBs und kleinere Sportboote
- Jetski und PWC

#### 3.3.2 Komponenten

**Steuergetriebe (Helm Unit):**
- Kompakte Einheit: Ritzel + Zahnstange in einem Gehäuse
- Befestigung: Schottwand-Montage oder Konsolenmontage
- Eingangsdrehung: Steuerrad direkt auf Ritzelwelle
- Ausgang: Zahnstange mit Kugelkopf oder Gabelauge

**Steuerkabel (Push-Pull-Kabel):**
- Bowdenzugartige Kabel mit starrem Kern und flexibler Hülle
- Kernmaterial: Edelstahl, Kunststoffummantelt
- Hülle: Kunststoff, UV-beständig, mit Führungsrille
- Längen: 3–30 ft (0,9–9,1 m) in 1-ft-Schritten
- Maximale Schubkraft: 300–600 N (Standardkabel), bis 1.500 N (Heavy-Duty)

**Tillerarm am Motor:**
- Gerade oder gebogen, Edelstahl oder Aluminium
- Befestigung: Klemmung auf Motorhalterung
- Anschluss: Kugelkopf-Aufnahme für Steuerkabel

#### 3.3.3 Auslegungsdaten

| Parameter | Wert |
|-----------|------|
| Max. Drehmoment | 50–150 Nm (NFB), bis 300 Nm (SSB) |
| Lock-to-Lock | 3,0–4,0 Umdrehungen |
| Wirkungsgrad | 80–90 % |
| Lebensdauer | 10–15 Jahre |
| Max. Motorgröße (Standard) | 150 PS (NFB), 350 PS (SSB) |

**Typen nach Rückstellverhalten:**

| Kürzel | Bezeichnung | Funktion |
|--------|-------------|---------|
| NFB | No Feedback | Kein Ruderdruck am Steuerrad (Reibungsbremse im Getriebe) |
| SSB | Safe Steering Back | Kontrollierter Rücklauf (Rückfederung) |
| FB | Full Feedback | Volle Rückmeldung (nur für sehr kleine Motoren) |

#### 3.3.4 Vor- und Nachteile

**Vorteile:**
- Extrem kompakt
- Einfache Installation (ein Kabel, ein Getriebe)
- NFB-Eigenschaft (kein Ruderratten bei schneller Fahrt)
- Preisgünstig
- Standardisiert (breite Austauschbarkeit)
- Zuverlässig bei korrekter Installation

**Nachteile:**
- Begrenzt auf kleine bis mittlere Motorkräfte
- Kein oder wenig natürliches Feedback
- Push-Pull-Kabel haben begrenzte Biegungsradien (min. 200 mm)
- Bei langen Kabelwegen: erhöhte Reibung, schwere Steuerung
- Kabel kann durch UV und Feuchtigkeit degradieren
- Nicht für Segelyachten geeignet (kein Feedback)

### 3.4 Hydraulische Steuerung (Hydraulic Steering)

#### 3.4.1 Funktionsprinzip

Die hydraulische Steuerung wandelt die mechanische Drehbewegung am Steuerrad in Hydraulikdruck um, der über Leitungen zu einem Steuerzylinder am Ruder übertragen wird. Der Zylinder bewegt den Tillerarm oder Quadranten.

**Kernkomponenten:**

1. **Helm-Pumpe (Steuerpumpe):** Am Steuerrad, wandelt Drehbewegung in Ölstrom
2. **Hydraulikleitung:** Druckfeste Schläuche oder Rohre verbinden Pumpe und Zylinder
3. **Steuerzylinder:** Am Ruder, wandelt Ölstrom in lineare oder rotatorische Bewegung
4. **Ölreservoir:** Ausgleichsbehälter für thermische Ausdehnung und Leckverluste
5. **Bypass-Ventil (optional):** Ermöglicht Autopilot-Integration oder Notsteuerung

#### 3.4.2 Hydraulische Grundlagen

**Druckübertragung (Pascal'sches Gesetz):**

```
p = F₁/A₁ = F₂/A₂

→ F₂ = F₁ × (A₂/A₁)
```

Die Hydraulik ermöglicht Kraftverstärkung durch unterschiedliche Kolbenflächen.

**Fördervolumen der Helm-Pumpe:**

```
V_Pumpe = A_Zylinder × Hub / n_Umdrehungen
```

Wobei:
- V_Pumpe = Fördervolumen pro Umdrehung [cm³/U]
- A_Zylinder = Kolbenfläche des Steuerzylinders [cm²]
- Hub = Gesamthub des Zylinders [cm]
- n_Umdrehungen = Anzahl Umdrehungen Lock-to-Lock

**Systemdruck:**

| Anwendung | Betriebsdruck | Maximaldruck |
|-----------|--------------|-------------|
| Motorboot <10 m | 30–50 bar | 70 bar |
| Motoryacht 10–18 m | 50–100 bar | 150 bar |
| Motoryacht >18 m | 80–150 bar | 200 bar |
| Segelyacht <14 m | 30–50 bar | 70 bar |
| Segelyacht >14 m | 50–100 bar | 150 bar |
| Superyacht | 100–200 bar | 300 bar |

#### 3.4.3 Helm-Pumpen-Typen

**Drehkolbenpumpe (Rotary Vane Pump):**
- Häufigster Typ für manuelle Hydrauliksteuerung
- 1–2 Umdrehungen pro Hub-Zyklus
- Fördervolumen: 10–35 cm³/U
- Vorteil: Kompakt, einfach
- Nachteil: Begrenzter Druck (max. 100 bar)
- Hersteller: SeaStar/Dometic, Vetus, Ultraflex

**Axialkolbenpumpe (Piston Pump):**
- Für höhere Drücke und Fördervolumina
- Mehrere Kolben (3, 5 oder 7) in Zylinderblock
- Fördervolumen: 15–80 cm³/U
- Vorteil: Höherer Druck (bis 250 bar), langlebiger
- Nachteil: Teurer, größer
- Hersteller: Kobelt, Jastram, Hynautic

**Zahnradpumpe (Gear Pump):**
- Meist als Power-Assist-Pumpe (elektrisch angetrieben)
- Nicht als manuelle Helm-Pumpe gebräuchlich
- Konstantes Fördervolumen bei gegebener Drehzahl
- Hersteller: Parker, Bosch Rexroth

#### 3.4.4 Steuerzylinder-Typen

**Linear-Zylinder (Ram Cylinder):**
- Doppeltwirkend (Druck in beide Richtungen)
- Kolbenstange greift über Kugelkopf am Tillerarm an
- Hubwege: 100–400 mm
- Kolbendurchmesser: 40–120 mm
- Häufigster Typ für Motorboote und Motoryachten

**Rotationszylinder (Rotary Actuator):**
- Direkt auf Ruderkopf montiert (kein Tillerarm nötig)
- Drehwinkel typisch 70°–90°
- Drehmoment: 200–50.000 Nm
- Kompakter als Linear-Zylinder + Tillerarm
- Teurer, aber eleganter
- Hersteller: Jefa, Kobelt, Lewmar

**Schottdurchführungs-Zylinder (Bulkhead Mount):**
- Durchdringt ein Schott und überträgt die Kraft axial
- Kompakte Installation in beengten Räumen
- Typisch bei Segelyachten

#### 3.4.5 Hydrauliköl

| Eigenschaft | Anforderung |
|-------------|-------------|
| Typ | Mineralöl (ISO VG 15–32) oder synthetisch |
| Viskositätsindex | >150 (temperaturstabil) |
| Temperaturbereich | -20 °C bis +80 °C |
| Frostschutz | Zwingend für Überwinterung in kalten Regionen |
| Dichtungsverträglichkeit | Muss mit NBR- und Viton-Dichtungen kompatibel sein |
| Korrosionsschutz | Inhibitoren gegen Rost und Buntmetallkorrosion |
| Wechselintervall | Alle 3–5 Jahre oder bei Verfärbung/Verschmutzung |

**ACHTUNG:** Mischung verschiedener Öltypen ist VERBOTEN — kann Dichtungsquellen, Schlammbildung und Systemausfall verursachen. Immer herstellerspezifisches Öl verwenden.

Empfohlene Hydrauliköle:
- SeaStar/Dometic: HA5430 (Universal-Lenkungsöl)
- Vetus: HF15 Hydrauliköl
- Ultraflex: OL150 (ISO VG 15)
- Kobelt: Dexron III/Mercon ATF (bei bestimmten Modellen)

#### 3.4.6 Hydraulikleitungen

| Leitungstyp | Anwendung | Max. Druck | Biegeradius |
|------------|-----------|-----------|-------------|
| Nylon-Rohr (PA) | Motorboote <12 m | 70 bar | 100 mm |
| Kupferrohr | Motoryachten, fest verlegt | 150 bar | 5× Durchmesser |
| Edelstahlrohr | Superyachten, fest verlegt | 300 bar | 5× Durchmesser |
| Hydraulikschlauch (SAE J1942) | Flexible Verbindungen | 200 bar | Je nach DN |

- Innendurchmesser: 8–16 mm (DN8–DN16)
- Anschlüsse: JIC 37° Flare (SAE J514), O-Ring Boss (ORB), BSP
- Leitungslänge: Maximale Gesamtlänge begrenzt durch Ölvolumen und Druckverlust
- Entlüftung: System muss nach Installation vollständig entlüftet werden

#### 3.4.7 Vor- und Nachteile

**Vorteile:**
- Hohe Kräfte übertragbar (praktisch unbegrenzt skalierbar)
- Flexible Leitungsführung (Schläuche um Hindernisse)
- Einfache Mehrfachsteuerung (zwei Steuerplätze parallel)
- Autopilot-Integration leicht möglich
- Kein Seilbruch/Kettenbruch-Risiko
- Power-Assist nachrüstbar

**Nachteile:**
- Gedämpftes Feedback (wenig Rückmeldung vom Ruder)
- Leckage möglich (Umweltgefährdung, Systemausfall)
- Luftblasen im System → Schwammige Steuerung
- Temperaturabhängig (Ölviskosität)
- Wartungsintensiver als mechanische Systeme
- Höheres Gewicht (Öl, Zylinder, Leitungen)

#### 3.4.8 Wartung

| Intervall | Maßnahme |
|-----------|---------|
| Monatlich | Ölstand im Reservoir prüfen |
| Vierteljährlich | Leitungen auf Leck prüfen (Sichtprüfung) |
| Halbjährlich | Anschlüsse auf Dichtheit prüfen, nachziehen |
| Jährlich | Systemdruck prüfen (Druckabfalltest) |
| Alle 3 Jahre | Hydraulikschläuche prüfen (Alterung, Risse) |
| Alle 5 Jahre | Hydrauliköl wechseln |
| Alle 8 Jahre | Hydraulikschläuche erneuern |
| Alle 10 Jahre | Zylinderdichtungen erneuern |

### 3.5 Elektrische Steuerung (Electric/Electronic Steering)

#### 3.5.1 Funktionsprinzip

Die elektrische Steuerung ersetzt die mechanische oder hydraulische Kraftübertragung teilweise oder vollständig durch elektrische Komponenten. Es gibt drei Abstufungen:

1. **Elektrohydraulisch:** Elektrische Pumpe liefert Hydraulikdruck → Hydraulikzylinder bewegt Ruder
2. **Elektrisch-mechanisch:** Elektromotor + Getriebe bewegt Ruder direkt
3. **Fly-by-Wire:** Steuersignal rein elektrisch, keine mechanische Verbindung

#### 3.5.2 Elektrohydraulische Steuerung

Dies ist der häufigste Typ elektrischer Steuerung auf Yachten >14 m.

**Komponenten:**
- **Steuersensor:** Am Steuerrad (Drehgeber, Potentiometer oder NMEA-Signal)
- **Steuercomputer (ECU):** Wertet Steuersignal aus, steuert Pumpe an
- **Elektrische Hydraulikpumpe:** 12V/24V/230V, Fördervolumen 0,5–5 l/min
- **Magnetventile:** Steuern Ölflussrichtung
- **Steuerzylinder:** Wie bei rein hydraulischer Steuerung
- **Rückmeldungsgeber:** Ruderlage-Sensor am Ruderschaft

**Power-Assist-Systeme:**
- Kombination aus manueller Helm-Pumpe und elektrischer Zusatzpumpe
- Bei niedrigen Geschwindigkeiten (Hafen): Power-Assist aktiv
- Bei Fahrt: Manuell, Power-Assist als Reserve
- Umschaltung: Automatisch (druckgesteuert) oder manuell

**Leistungsaufnahme:**

| Bootslänge | Pumpenleistung | Stromaufnahme (24V) |
|-----------|---------------|-------------------|
| 12–14 m | 0,5–1,0 kW | 20–40 A |
| 14–18 m | 1,0–2,0 kW | 40–80 A |
| 18–24 m | 2,0–4,0 kW | 80–160 A |
| >24 m | 4,0–10,0 kW | 160–400 A |

#### 3.5.3 Elektromechanische Steuerung

Direkte elektrische Betätigung des Ruders ohne Hydraulik.

**Komponenten:**
- **Elektromotor:** Bürstenloser DC-Motor (BLDC) oder Servomotor
- **Getriebe:** Planetengetriebe oder Schneckengetriebe
- **Linearantrieb oder Rotationsantrieb:** Direkt auf Tillerarm oder Ruderkopf
- **Steuerung:** Elektronische Regelung mit Positionsrückmeldung

**Vorteile gegenüber Hydraulik:**
- Kein Öl (keine Leckgefahr)
- Schnellere Reaktion (kein Ölkompression)
- Geringere Wartung
- Kompakter bei kleinen Drehmomenten

**Nachteile:**
- Begrenzt auf kleinere Drehmomente (bis ca. 5.000 Nm wirtschaftlich)
- Stromverbrauch im Dauerbetrieb
- Hitzeentwicklung bei Dauerlast
- Redundanz schwieriger darstellbar

#### 3.5.4 Fly-by-Wire

Vollständig elektronische Signalübertragung ohne mechanische Verbindung zwischen Steuerrad und Ruder.

**Architektur:**

```
Steuerrad ──→ Drehgeber ──→ Steuercomputer ──→ Ruderaktuator
    ↑              │              │                    │
    │              │         Redundanz-            Ruderlage-
    │              │         Computer              Sensor
    │              │              │                    │
    └──── Feedback-Motor ←────────┴────────────────────┘
```

**Anforderungen nach ISO 25197:**
- Mindestens zwei unabhängige Signalwege (CAN-Bus A + B)
- Automatische Fehlererkennung und -meldung
- Definierter Rückfallmodus bei Ausfall eines Systems
- Redundante Stromversorgung
- Watchdog-Timer auf allen Controllern

**Einsatz:**
- Superyachten >30 m (Standard)
- Motoryachten mit Joystick-Steuerung (Volvo IPS, Mercury Zeus, Yamaha Helm Master)
- Rennboote mit Hochleistungs-Aktuatoren

#### 3.5.5 Vor- und Nachteile elektrischer Systeme

**Vorteile:**
- Unbegrenzte Steuerplatz-Anzahl (nur Kabel, keine Leitungen)
- Einfache Autopilot-Integration
- Programmierbare Steuercharakteristik
- Joystick-Integration möglich
- Datenlogging und Diagnose
- Kein Ölwechsel, keine Seilnachspannung

**Nachteile:**
- Komplexe Elektronik (Fehlersuche schwieriger)
- Stromabhängig (Batterieausfall = Steuerungsausfall)
- Elektromagnetische Verträglichkeit (EMV) kritisch
- Kein natürliches Feedback (muss simuliert werden)
- Höhere Anschaffungskosten
- Weniger Fachleute für Reparatur verfügbar

### 3.6 Pinnensteuerung (Tiller Steering)

#### 3.6.1 Funktionsprinzip

Die Pinne (Tiller) ist die älteste und einfachste Form der Steuerung: Ein starrer Hebel (die Pinne) ist direkt mit dem Ruderkopf verbunden. Der Rudergänger lenkt das Ruder durch seitliches Bewegen der Pinne.

#### 3.6.2 Bauformen

**Gerade Pinne:**
- Einfachste Form: gerader Holz- oder Metallhebel
- Befestigung: Konus + Keilnut auf Ruderkopf
- Länge: 800–1500 mm
- Material: Hartholz (Teak, Eiche), Aluminium (eloxiert), Carbon, GFK

**Geknickter Pinnenausleger (Hiking Stick):**
- Verlängerung der Pinne über ein Gelenk
- Ermöglicht Ruderbedienung beim Ausreiten oder vom Seitendeck
- Typisch: Jollen, Sportboote, kleine Kielboote
- Material: Aluminium, Carbon

**Klapp-Pinne:**
- Pinne lässt sich hochklappen (Platzersparnis im Cockpit)
- Federmechanismus oder Arretierung in Fahrposition
- Typisch: Fahrtensegler mit Heckcockpit

**Notpinne (Emergency Tiller):**
- Kurze Pinne, die auf den Ruderkopf aufgesetzt wird
- Für den Fall eines Totalausfalls der regulären Steuerung
- Muss zu jeder Radsteuerung mitgeführt werden
- Verstauung: Zugänglich, trocken, klar beschriftet
- ISAF/World Sailing: Pflichtausrüstung für Offshore-Regatten

#### 3.6.3 Vor- und Nachteile

**Vorteile:**
- 100 % direktes Feedback (unübertroffenes Steuergefühl)
- Maximale Zuverlässigkeit (kein Übertragungselement)
- Geringstes Gewicht
- Geringste Kosten
- Keine Wartung (außer gelegentliches Fetten des Ruderlagers)
- Sofortige Reaktion

**Nachteile:**
- Physisch anstrengend bei schwerem Wetter
- Pinne blockiert Cockpit-Mitte
- Nicht geeignet für Boote >10 m (zu hohe Ruderkräfte)
- Rudergänger muss achtern stehen (ungünstige Sicht auf Vorschiff)
- Nicht kombinierbar mit Rad-Autopilot (nur Tiller-Pilot)

#### 3.6.4 Dimensionierung

**Pinnenlänge:**

```
L_Pinne ≈ T_Ruder_max / F_Hand_max
```

Wobei:
- L_Pinne = effektive Pinnenlänge [m]
- T_Ruder_max = maximales Ruderdrehmoment [Nm]
- F_Hand_max = maximale akzeptable Handkraft (ca. 50–80 N)

**Rechenbeispiel — 8 m Segelyacht:**

```
T_Ruder_max = 80 Nm
F_Hand_max = 60 N

L_Pinne = 80 / 60 = 1,33 m → Pinne mindestens 1,35 m lang
```

---

## 4. Produktlinien und Spezifikationen

### 4.1 Jefa Marine (Dänemark)

Jefa Marine A/S, gegründet 1972 in Barrit, Dänemark, ist der führende europäische Spezialist für Segelyacht-Steuerungen. Jefa liefert an die meisten großen europäischen Segelyachtwerften (Hallberg-Rassy, Najad, Malo, Swan, X-Yachts, Contest).

#### 4.1.1 Ruderlager und Ruderschaft-Systeme

**Jefa Rudder Bearings (Standard-Reihe):**

| Modell | Schaftdurchmesser | Max. Drehmoment | Bootsklasse |
|--------|-------------------|----------------|------------|
| Jefa 25 | ∅25 mm | 120 Nm | 7–9 m |
| Jefa 30 | ∅30 mm | 200 Nm | 9–11 m |
| Jefa 35 | ∅35 mm | 350 Nm | 11–13 m |
| Jefa 40 | ∅40 mm | 550 Nm | 13–15 m |
| Jefa 45 | ∅45 mm | 800 Nm | 15–17 m |
| Jefa 50 | ∅50 mm | 1.200 Nm | 17–20 m |
| Jefa 55 | ∅55 mm | 1.800 Nm | 20–23 m |
| Jefa 60 | ∅60 mm | 2.500 Nm | 23–26 m |
| Jefa 70 | ∅70 mm | 4.000 Nm | 26–30 m |
| Jefa 80 | ∅80 mm | 6.000 Nm | 30–35 m |

**Lagerbuchsen-Material:** PTFE/GFK-Verbundwerkstoff (selbstschmierend), wartungsfrei
**Schaftmaterial:** Aquamet 22 (Standard), Edelstahl 316L (Budget), Nitronic 50 (High-Performance)
**Dichtungen:** Doppel-Lippendichtung mit Fettfüllung, zusätzliche Quadring-Dichtung

**Jefa Tiller-Arm-Reihe:**

| Modell | Schaftdurchmesser | Armlänge | Material |
|--------|-------------------|---------|---------|
| TA-25 | ∅25 mm | 200–300 mm | Aluminium 6082-T6 |
| TA-30 | ∅30 mm | 200–350 mm | Aluminium 6082-T6 |
| TA-35 | ∅35 mm | 250–400 mm | Aluminium 6082-T6 |
| TA-40 | ∅40 mm | 250–400 mm | Aluminium 6082-T6 |
| TA-45 | ∅45 mm | 300–450 mm | Edelstahl 316L |
| TA-50 | ∅50 mm | 300–500 mm | Edelstahl 316L |

#### 4.1.2 Jefa Steuersäulen (Pedestals)

**Jefa CSC-Serie (Cable Steering Column):**

| Modell | Höhe | Radgröße | Max. Drehmoment | Typ |
|--------|------|---------|----------------|-----|
| CSC-500 | 500 mm | 600–800 mm | 150 Nm | Seilzug |
| CSC-700 | 700 mm | 700–900 mm | 200 Nm | Seilzug |
| CSC-900 | 900 mm | 800–1050 mm | 250 Nm | Seilzug/Kette |
| CSC-1000 | 1000 mm | 900–1200 mm | 350 Nm | Kette |

**Material:** Edelstahl 316L (poliert oder satiniert)
**Optionen:** Kompass-Aufnahme, Instrumenten-Pod, Motorgashebel-Integration, Dual-Rad

**Jefa HSC-Serie (Hydraulic Steering Column):**

| Modell | Verdrängung/U | Systemdruck | Max. Drehmoment | Bootsklasse |
|--------|-------------|------------|----------------|------------|
| HSC-12 | 12 cm³/U | 60 bar | 400 Nm | 12–15 m |
| HSC-20 | 20 cm³/U | 80 bar | 800 Nm | 15–18 m |
| HSC-28 | 28 cm³/U | 100 bar | 1.500 Nm | 18–22 m |
| HSC-40 | 40 cm³/U | 120 bar | 3.000 Nm | 22–28 m |

### 4.2 Whitlock/Lewmar (UK)

Whitlock Marine wurde 1968 in Portsmouth gegründet und ist seit 2007 Teil der Lewmar-Gruppe. Die Whitlock-Steuerungssysteme bilden die Standardausrüstung vieler britischer und französischer Serienyachten (Oyster, Moody, Dufour, Jeanneau).

#### 4.2.1 Whitlock Cobra-System

Das Cobra-System ist das verbreitetste Seilzug-Steuerungssystem für Segelyachten weltweit.

**Cobra Pedestal-Reihe:**

| Modell | Höhe (mm) | Radgröße (mm) | Max. Drehmoment (Nm) | Bootsklasse |
|--------|-----------|--------------|---------------------|------------|
| Cobra 15 | 749 | 600–700 | 100 | 7–9 m |
| Cobra 20 | 838 | 700–800 | 130 | 8–10 m |
| Cobra 30 | 838 | 700–900 | 190 | 9–12 m |
| Cobra 40 | 940 | 800–1050 | 250 | 11–14 m |
| Cobra 50 | 940 | 900–1200 | 350 | 13–16 m |

**Cobra Seilzug-Kits:**
- Seildurchmesser: ∅4 mm (7×19, 316 SS)
- Umlenkrollen: Nylon mit Edelstahl-Lager, ∅50 mm
- Quadranten: Aluminium, 90° Bogen, Radien 100/125/150/175/200 mm
- Seilspanner: Edelstahl-Spannschloss mit Kontermutter
- Federsatz: Zugfedern für Seilrückstellung

**Lewmar Steuerräder:**

| Modell | Durchmesser | Material | Gewicht |
|--------|------------|---------|--------|
| Lewmar Commodore | 600–1000 mm | Edelstahl + Leder | 2,8–5,5 kg |
| Lewmar Navigator | 700–1200 mm | Edelstahl + Teak | 3,5–7,0 kg |
| Lewmar Power Grip | 600–900 mm | Edelstahl + PU | 2,5–4,5 kg |
| Lewmar Evolution | 800–1200 mm | Carbon + Leder | 1,8–3,2 kg |
| Lewmar Folding | 600–800 mm | Edelstahl + Teak | 3,0–5,0 kg |

#### 4.2.2 Lewmar Hydraulische Steuerungen

**Lewmar Continuum-Serie:**

| Modell | Verdrängung | Systemdruck | Bootsklasse |
|--------|-----------|------------|------------|
| Continuum 08 | 8 cm³/U | 50 bar | 10–13 m Segel |
| Continuum 12 | 12 cm³/U | 65 bar | 13–16 m Segel |
| Continuum 20 | 20 cm³/U | 80 bar | 16–20 m Segel |
| Continuum 30 | 30 cm³/U | 100 bar | 20–25 m Segel |

### 4.3 Edson (USA)

Edson International, gegründet 1859 in New Bedford, Massachusetts, ist der älteste und führende US-amerikanische Hersteller von Yacht-Steuerungen. Edson liefert an die meisten US-Werften (Sabre, Hinckley, Tartan, Morris, Pacific Seacraft).

#### 4.3.1 Edson Pedestals

**Edson Pedestal-Reihe (aktuelle Generation):**

| Modell | Höhe | Radgröße | Max. Drehmoment | Besonderheit |
|--------|------|---------|----------------|-------------|
| Edson 335 | 33,5" (851 mm) | 24–36" | 180 Nm | Kompakt, Boote 8–11 m |
| Edson 340 | 34" (864 mm) | 28–42" | 250 Nm | Standard, Boote 10–13 m |
| Edson 407 | 40,7" (1034 mm) | 32–48" | 350 Nm | Groß, Boote 12–16 m |
| Edson 540 | 54" (1372 mm) | 36–48" | 450 Nm | XL, Boote 15–20 m |

**Material:** Aluminium 6061-T6, anodisiert (Standard) oder Edelstahl 316 (optional)
**Guard:** Edelstahl 316 Bügel, integriert oder abnehmbar
**Binnacle:** Optionale Kompass-Aufnahme (Ritchie oder Danforth-kompatibel)

#### 4.3.2 Edson Seilzug-Systeme

**Edson Radial Drive System:**

| Modell | Seilzugkraft | Quadrant-Radius | Seildurchmesser |
|--------|-------------|----------------|----------------|
| RadialDrive 336 | 2.200 N | 6" (152 mm) | 3/16" (4,8 mm) |
| RadialDrive 448 | 3.500 N | 8" (203 mm) | 1/4" (6,4 mm) |
| RadialDrive 560 | 5.000 N | 10" (254 mm) | 1/4" (6,4 mm) |

**Edson Umlenkrollen:**
- Modell 404: Standard-Umlenkrolle, Nylon, ∅3" (76 mm), für ∅3/16"–1/4" Seil
- Modell 416: Heavy-Duty, Bronze, ∅4" (102 mm), für ∅1/4" Seil
- Modell 432: Decksdurchführung, Edelstahl, für ∅3/16"–1/4" Seil
- Modell 446: Kugellager-Umlenkrolle, Edelstahl, ∅3,5" (89 mm)

#### 4.3.3 Edson Steuerräder

| Modell | Durchmesser | Material | Besonderheit |
|--------|------------|---------|-------------|
| Edson Classic | 24"–48" | Edelstahl + Teak | Traditionelles Design |
| Edson Comfort Grip | 28"–42" | Edelstahl + PU-Schaum | Weicher Griff |
| Edson PowerKnob | 32"–48" | Edelstahl + Leder | Mit Drehknauf |
| Edson Ultra | 30"–42" | Carbon + Leder | Leichtbau |
| Edson Folding | 28"–36" | Edelstahl + Teak | Klappbar |

### 4.4 Kobelt Manufacturing (Kanada)

Kobelt Manufacturing Co. Ltd., gegründet 1962 in Surrey, British Columbia, ist spezialisiert auf schwere hydraulische Steuer- und Antriebssysteme für kommerzielle Schiffe und große Yachten.

#### 4.4.1 Kobelt Hydraulische Helm-Pumpen

**Kobelt 7003-Serie (Standard):**

| Modell | Verdrängung | Druck max. | Anwendung |
|--------|-----------|-----------|----------|
| 7003-AL | 3,6 in³/U (59 cm³/U) | 1.500 PSI (103 bar) | Motoryacht 12–18 m |
| 7003-AN | 4,9 in³/U (80 cm³/U) | 1.500 PSI (103 bar) | Motoryacht 15–22 m |
| 7003-AP | 6,4 in³/U (105 cm³/U) | 1.500 PSI (103 bar) | Motoryacht 20–28 m |

**Kobelt 7004-Serie (Heavy-Duty):**

| Modell | Verdrängung | Druck max. | Anwendung |
|--------|-----------|-----------|----------|
| 7004-AL | 3,6 in³/U | 2.000 PSI (138 bar) | Motoryacht 14–20 m |
| 7004-AN | 4,9 in³/U | 2.000 PSI (138 bar) | Motoryacht 18–25 m |
| 7004-AP | 6,4 in³/U | 2.000 PSI (138 bar) | Motoryacht 22–30 m |
| 7004-AR | 8,2 in³/U | 2.000 PSI (138 bar) | Motoryacht >28 m |

#### 4.4.2 Kobelt Steuerzylinder

**Kobelt 2020-Serie (Linear):**

| Modell | Kolben-∅ | Hub | Max. Druck | Kraft |
|--------|---------|-----|-----------|------|
| 2020-30 | 3,0" (76 mm) | 6"–12" | 1.500 PSI | 6.800 N |
| 2020-40 | 4,0" (102 mm) | 8"–16" | 1.500 PSI | 12.100 N |
| 2020-50 | 5,0" (127 mm) | 10"–20" | 1.500 PSI | 18.900 N |
| 2020-60 | 6,0" (152 mm) | 12"–24" | 1.500 PSI | 27.200 N |

> ⚠️ **ZU PRÜFEN (Audit):** Die Kraftspalte der 2020-Serie ist inkonsistent mit Bohrung und Druck. Beispiel 2020-30: ∅76 mm bei 1.500 PSI (103 bar) ergibt rechnerisch F = A × p ≈ 46.900 N, angegeben sind 6.800 N (Faktor ~6,9 zu niedrig — entspricht ~15 bar statt 103 bar). Alle vier Zeilen betroffen (gleicher Faktor). Zum Vergleich rechnen die Ultraflex-Tabelle (4.5.4) und die Vetus-Tabelle (4.6.1) in derselben Datei F = A × p korrekt. Der wahre Herstellerwert (Bohrung oder Kraft?) ist ohne Kobelt-TDS nicht zweifelsfrei bestimmbar — daher nicht korrigiert, sondern markiert. Confidence measured → estimated (unverifiziert).

**Kobelt 2024-Serie (Rotary):**

| Modell | Drehmoment | Drehwinkel | Schaftgröße |
|--------|-----------|-----------|------------|
| 2024-060 | 600 Nm | ±35° | ∅40 mm |
| 2024-120 | 1.200 Nm | ±35° | ∅50 mm |
| 2024-250 | 2.500 Nm | ±35° | ∅60 mm |
| 2024-500 | 5.000 Nm | ±35° | ∅70 mm |
| 2024-1000 | 10.000 Nm | ±35° | ∅90 mm |

### 4.5 Ultraflex (Italien)

Ultraflex S.p.A., gegründet 1971 in Campodarsego (Padua), gehört zur Lecomble & Schmitt Gruppe und ist einer der weltweit führenden Hersteller von Bootssteuerungen, insbesondere für Motorboote und Außenborder.

#### 4.5.1 Ultraflex Zahnstangensteuerungen

**Ultraflex T-67 (Standard NFB):**
- Typ: Rack-and-Pinion, No Feedback
- Max. Motorleistung: 55 PS (Einzelmotor), 2×40 PS (Doppelmotor)
- Lock-to-Lock: 3,2 Umdrehungen
- Montage: Schott- oder Konsolenmontage
- Kabel: M58 (Standard) oder M66 (Heavy-Duty)

**Ultraflex T-71FC (Heavy-Duty NFB):**
- Typ: Rack-and-Pinion, No Feedback, Tilt-Montage
- Max. Motorleistung: 150 PS (Einzelmotor), 2×115 PS (Doppelmotor)
- Lock-to-Lock: 3,4 Umdrehungen
- Montage: Konsolenmontage mit Neigungswinkel
- Kabel: M66 (empfohlen)

**Ultraflex T-85 (Front Mount NFB):**
- Typ: Rack-and-Pinion, NFB, Frontmontage
- Max. Motorleistung: 300 PS (Einzelmotor)
- Lock-to-Lock: 4,0 Umdrehungen
- Montage: Schottwandmontage
- Kabel: M66 oder M90

#### 4.5.2 Ultraflex Steuerkabel

| Modell | Typ | Max. Schubkraft | Biegeradius min. | Anwendung |
|--------|-----|----------------|-----------------|----------|
| M58 | Standard | 300 N | 200 mm | Boote <6 m, <55 PS |
| M66 | Heavy-Duty | 600 N | 200 mm | Boote 6–10 m, <300 PS |
| M90 | X-HD Mach Zero | 900 N | 250 mm | Boote 8–12 m, <400 PS |

**Kabellängen:** 6–30 ft in 1-ft-Schritten

#### 4.5.3 Ultraflex Hydraulische Steuerungen

**Ultraflex UC128-OBF (Außenborder, Frontmontage):**
- Verdrängung: 12,8 cm³/U
- Systemdruck: max. 55 bar
- Lock-to-Lock: 4,0 Umdrehungen
- Max. Motorleistung: 300 PS (mit Zylinder UC128-OBF)
- Anschlüsse: 3/8" JIC

**Ultraflex UP28 (Innenborder):**
- Verdrängung: 28 cm³/U
- Systemdruck: max. 80 bar
- Lock-to-Lock: 3,5 Umdrehungen
- Empfohlen für: Boote 10–16 m
- Anschlüsse: 3/8" JIC

**Ultraflex UP39 (Heavy-Duty Innenborder):**
- Verdrängung: 39 cm³/U
- Systemdruck: max. 100 bar
- Lock-to-Lock: 4,0 Umdrehungen
- Empfohlen für: Boote 14–20 m
- Anschlüsse: 1/2" JIC

#### 4.5.4 Ultraflex Steuerzylinder

| Modell | Kolben-∅ | Hub | Max. Druck | Kraft |
|--------|---------|-----|-----------|------|
| UC94-OBF | 50 mm | 167 mm | 55 bar | 10.800 N |
| UC128-OBF | 60 mm | 184 mm | 55 bar | 15.600 N |
| UC215-I | 80 mm | 213 mm | 80 bar | 40.200 N |
| UC215-II | 90 mm | 213 mm | 80 bar | 50.900 N |

### 4.6 Vetus (Niederlande)

Vetus B.V., gegründet 1964 in Schiedam, ist ein führender Lieferant von Bootszubehör, einschließlich Steuerungssystemen für Motor- und Segelboote.

#### 4.6.1 Vetus Hydraulische Steuerungen

**Vetus HTP-Serie (Helm-Pumpen):**

| Modell | Verdrängung | Max. Druck | Anwendung |
|--------|-----------|-----------|----------|
| HTP20 | 20 cm³/U | 65 bar | Motorboot 8–12 m |
| HTP30 | 30 cm³/U | 80 bar | Motoryacht 10–15 m |
| HTP42 | 42 cm³/U | 100 bar | Motoryacht 13–18 m |

**Vetus Steuerzylinder:**

| Modell | Kolben-∅ | Hub | Max. Druck | Kraft |
|--------|---------|-----|-----------|------|
| MTC52 | 52 mm | 200 mm | 80 bar | 17.000 N |
| MTC72 | 72 mm | 250 mm | 100 bar | 40.700 N |
| MTC88 | 88 mm | 300 mm | 100 bar | 60.800 N |
| MTC125 | 125 mm | 400 mm | 100 bar | 122.700 N |

#### 4.6.2 Vetus Elektrohydraulische Systeme

**Vetus EHP-Serie (Elektrohydraulische Power Packs):**

| Modell | Pumpenleistung | Fördermenge | Versorgung | Bootsklasse |
|--------|---------------|-----------|-----------|------------|
| EHP10 | 1,0 kW | 2,5 l/min | 12V DC | 10–14 m |
| EHP15 | 1,5 kW | 3,5 l/min | 24V DC | 13–18 m |
| EHP25 | 2,5 kW | 5,0 l/min | 24V DC | 17–22 m |
| EHP40 | 4,0 kW | 8,0 l/min | 24V DC | 20–28 m |

#### 4.6.3 Vetus Zahnstangensteuerungen

**Vetus MT-Serie:**

| Modell | Typ | Max. Motor | Lock-to-Lock |
|--------|-----|-----------|-------------|
| MT30 | NFB | 30 PS | 3,0 Umdrehungen |
| MT52 | NFB | 55 PS | 3,2 Umdrehungen |
| MT72 | SSB | 150 PS | 3,5 Umdrehungen |

---

## 5. Hersteller-Datenbank

### 5.1 Jefa Marine A/S

| Attribut | Wert |
|----------|------|
| **Gründung** | 1972 |
| **Sitz** | Barrit, Jütland, Dänemark |
| **Spezialgebiet** | Segelyacht-Steuerungen, Ruderlager, Ruderschaftsysteme |
| **Bootsgrößenbereich** | 7–35 m |
| **Steuerungstypen** | Seilzug, Kette, Hydraulisch |
| **OEM-Kunden** | Hallberg-Rassy, Najad, Malo, Swan (Nautor), X-Yachts, Contest, Arcona, Dehler |
| **Zertifizierungen** | ISO 9001, GL/DNV-Typgenehmigung, Lloyd's |
| **Vertrieb** | Weltweit über Fachhändlernetz, direkt an Werften |
| **Website** | jefa.com |
| **Besonderheit** | Aquamet-22-Ruderschäfte als Standard, PTFE/GFK-Lagerbuchsen, individuell gefertigte Ruderanlagen |
| **Preissegment** | Mittel bis Hoch (€500–€15.000 je nach System) |

### 5.2 Lewmar/Whitlock

| Attribut | Wert |
|----------|------|
| **Gründung** | Lewmar: 1946, Whitlock: 1968 (Übernahme 2007) |
| **Sitz** | Havant, Hampshire, UK |
| **Spezialgebiet** | Segelyacht-Steuerungen, Steuerräder, Pedestals |
| **Bootsgrößenbereich** | 7–25 m |
| **Steuerungstypen** | Seilzug (Cobra), Kette, Hydraulisch (Continuum) |
| **OEM-Kunden** | Oyster, Moody, Dufour, Jeanneau, Bavaria, Hanse |
| **Zertifizierungen** | ISO 9001, ISO 14001, CE |
| **Vertrieb** | Weltweit, starkes Händlernetz |
| **Website** | lewmar.com |
| **Besonderheit** | Cobra-System als meistverbreitete Seilzugsteuerung weltweit, breites Steuerrad-Sortiment |
| **Preissegment** | Mittel (€300–€8.000) |

### 5.3 Edson International

| Attribut | Wert |
|----------|------|
| **Gründung** | 1859 |
| **Sitz** | New Bedford, Massachusetts, USA |
| **Spezialgebiet** | Pedestals, Steuerräder, Seilzugsysteme für Segelyachten |
| **Bootsgrößenbereich** | 7–24 m |
| **Steuerungstypen** | Seilzug (Radial Drive), Kette |
| **OEM-Kunden** | Sabre, Hinckley, Tartan, Morris, Pacific Seacraft, Island Packet |
| **Zertifizierungen** | ABYC, NMMA, CE |
| **Vertrieb** | Primär Nordamerika, international über Fachhändler |
| **Website** | edsonmarine.com |
| **Besonderheit** | Ältester Steueranlagen-Hersteller der Welt, starke US-Marktposition, exzellenter Aftermarket-Support |
| **Preissegment** | Mittel bis Hoch (USD 400–USD 12.000) |

### 5.4 Kobelt Manufacturing

| Attribut | Wert |
|----------|------|
| **Gründung** | 1962 |
| **Sitz** | Surrey, British Columbia, Kanada |
| **Spezialgebiet** | Schwere hydraulische Steueranlagen, Gashebelsteuerungen |
| **Bootsgrößenbereich** | 12–50 m |
| **Steuerungstypen** | Hydraulisch (manuell, Power-Assist, vollelektrisch) |
| **OEM-Kunden** | Nordhavn, Fleming, Grand Banks, Kadey-Krogen, Selene |
| **Zertifizierungen** | ISO 9001, USCG, Transport Canada, ABS, Lloyd's |
| **Vertrieb** | Weltweit, Schwerpunkt Nordamerika |
| **Website** | kobelt.com |
| **Besonderheit** | Industriequalität, extrem robust, Standard auf Trawler-Yachten und schweren Motoryachten |
| **Preissegment** | Hoch (USD 2.000–USD 30.000) |

### 5.5 Ultraflex (Lecomble & Schmitt Gruppe)

| Attribut | Wert |
|----------|------|
| **Gründung** | 1971 |
| **Sitz** | Campodarsego (Padua), Italien |
| **Spezialgebiet** | Motorboot-Steuerungen (mechanisch und hydraulisch), Steuerkabel |
| **Bootsgrößenbereich** | 3–20 m |
| **Steuerungstypen** | Zahnstange (NFB/SSB), Hydraulisch, Seilzug |
| **OEM-Kunden** | Bayliner, Four Winns, Sealine, Quicksilver, Zodiac, BWA |
| **Zertifizierungen** | ISO 9001, CE, IMCI |
| **Vertrieb** | Weltweit, sehr breites Händlernetz |
| **Website** | ultraflex.it |
| **Besonderheit** | Breitstes Sortiment an Zahnstangensteuerungen, marktführend bei Motorboot-Steuerungen in Europa |
| **Preissegment** | Niedrig bis Mittel (€80–€3.000) |

### 5.6 Vetus B.V.

| Attribut | Wert |
|----------|------|
| **Gründung** | 1964 |
| **Sitz** | Schiedam, Niederlande |
| **Spezialgebiet** | Bootszubehör breit, inkl. Steuerungen |
| **Bootsgrößenbereich** | 5–22 m |
| **Steuerungstypen** | Zahnstange, Hydraulisch, Elektrohydraulisch |
| **OEM-Kunden** | Linssen, Aquanaut, Pedro, diverse kleinere europäische Werften |
| **Zertifizierungen** | ISO 9001, CE |
| **Vertrieb** | Weltweit, eigenes Händlernetz |
| **Website** | vetus.com |
| **Besonderheit** | Komplettanbieter (Motor, Bugstrahlruder, Steuerung aus einer Hand), exzellente Dokumentation |
| **Preissegment** | Mittel (€150–€5.000) |

### 5.7 Weitere Hersteller (Kurzprofile)

**SeaStar Solutions (Dometic Marine):**
- Sitz: Richmond, BC, Kanada (jetzt Dometic, Schweden)
- Spezialgebiet: Hydraulische Steuerungen für Motorboote, Helm-Pumpen
- Modelle: SeaStar Pro, BayStar, BayStar Plus
- Marktführer bei hydraulischen Außenborder-Steuerungen in Nordamerika
- Bootsgrößen: 5–20 m

**Jastram Engineering (Kanada):**
- Sitz: Vancouver, BC
- Spezialgebiet: Schwere hydraulische und elektrohydraulische Steuerungen
- Bootsgrößen: 20–100 m (Superyachten, kommerzielle Schiffe)
- Zertifizierungen: DNV, Lloyd's, ABS, BV

**Hy-Pro-Drive (Niederlande):**
- Sitz: Waalwijk, Niederlande
- Spezialgebiet: Hydraulische Steuerungen für europäische Binnenfahrt und Yachten
- Bootsgrößen: 8–30 m
- Besonderheit: Starke Position im Binnenfahrt-Segment

**Teleflex Marine (jetzt SeaStar/Dometic):**
- Historisch bedeutend als Erfinder des Rack-and-Pinion-Steuersystems für Boote
- Teleflex-Steuerkabel und -Getriebe sind nach wie vor der de-facto-Standard
- Kompatibilität: Ultraflex und Teleflex Kabel/Getriebe sind weitgehend austauschbar

---

## 6. Fehlerbild-Atlas

### 6.1 Fehlerbild: Spiel im Steuerrad (Ruderspiel)

**Beschreibung:**
Das Steuerrad kann um einen merklichen Winkel (>3°) gedreht werden, ohne dass sich das Ruder bewegt. Der Rudergänger bemerkt eine „tote Zone" in der Mittellage.

**Symptome:**
- Steuerrad lässt sich in Mittellage leicht hin- und herbewegen
- Kurshalten erfordert ständige Korrekturen
- „Klackern" oder „Rattern" bei Seegang
- Autopilot arbeitet unruhig (ständiges Nachsteuern)

**Ursachen (nach Wahrscheinlichkeit):**

| Rang | Ursache | Häufigkeit | Steuerungstyp |
|------|--------|-----------|--------------|
| 1 | Seilzug gelängt | 35 % | Seilzug |
| 2 | Kettenrad-Verschleiß | 20 % | Kette |
| 3 | Quadrant-Bolzen ausgeschlagen | 15 % | Seilzug/Kette |
| 4 | Ruderschaft-Konus lose | 10 % | Alle |
| 5 | Ruderlager ausgeschlagen | 8 % | Alle |
| 6 | Zahnspiel im Getriebe | 7 % | Zahnstange |
| 7 | Hydraulik — Luft im System | 5 % | Hydraulisch |

**Diagnoseschritte:**
1. Ruder manuell fixieren, Steuerrad drehen → Spiel in Übertragung lokalisieren
2. Seilzug: Seile auf Spannung prüfen, Seilspanner nachstellen
3. Kette: Kettenrad und Kette auf Verschleiß prüfen (Zahnprofil)
4. Quadrant: Bolzenverbindungen prüfen, Konus-Sitz am Ruderkopf prüfen
5. Ruderlager: Ruder seitlich bewegen (nicht drehen) → Lagerspiel erkennen

**Behebung:**
- Seilzug nachspannen oder erneuern
- Kette/Kettenrad austauschen
- Bolzen/Buchsen austauschen
- Konusmutter nachziehen (Drehmoment beachten!)
- Ruderlager erneuern

**Confidence:** measured (Hersteller-Wartungsanleitungen)

### 6.2 Fehlerbild: Schwergängigkeit (Heavy Helm)

**Beschreibung:**
Die Steuerung erfordert ungewöhnlich hohe Kraft am Steuerrad. Das Drehen fühlt sich zäh, schwerfällig oder ruckend an.

**Symptome:**
- Steuerrad lässt sich nur mit beiden Händen drehen
- Ruckende Bewegung statt gleichmäßigem Drehen
- Unterschiedliche Schwere in verschiedenen Bereichen des Ruderwegs
- Ermüdung des Rudergängers

**Ursachen:**

| Rang | Ursache | Häufigkeit | Steuerungstyp |
|------|--------|-----------|--------------|
| 1 | Umlenkrollen klemmen/korrodiert | 25 % | Seilzug |
| 2 | Ruderlager korrodiert/beschädigt | 20 % | Alle |
| 3 | Steuerkoker-Dichtung zu stramm | 15 % | Alle |
| 4 | Seilzug-Führung falsch verlegt | 12 % | Seilzug |
| 5 | Hydrauliköl verdickt (Kälte) | 10 % | Hydraulisch |
| 6 | Bewuchs am Ruderblatt | 8 % | Alle |
| 7 | Ruderschaft verbogen | 5 % | Alle |
| 8 | Pedestal-Getriebe verschlissen | 5 % | Seilzug/Kette |

**Diagnoseschritte:**
1. Boot aus dem Wasser (Trailer/Kran): Ruder ohne Wasserwiderstand drehen → mechanische Ursache isolieren
2. Einzelkomponenten von der Übertragung trennen und einzeln prüfen
3. Umlenkrollen einzeln auf Leichtgängigkeit prüfen
4. Ruderlager: Ruder bei ausgehängtem Seilzug per Hand drehen

**Behebung:**
- Umlenkrollen schmieren oder erneuern
- Ruderlager erneuern
- Steuerkoker-Dichtung mit korrektem Drehmoment einstellen
- Seilzugführung optimieren (Mindestradien einhalten)
- Hydrauliköl wechseln (korrekte Viskosität)
- Bewuchs am Ruderblatt entfernen, Antifouling erneuern

**Confidence:** measured (Hersteller-TDS, Surveyberichte)

### 6.3 Fehlerbild: Seilzugriss (Wire Rope Failure)

**Beschreibung:**
Einer oder beide Drahtseile der Seilzugsteuerung reißen. Totalausfall der Steuerung.

**Symptome:**
- Plötzliches „Wegdrehen" des Steuerrads (kein Widerstand mehr)
- Steuerrad dreht frei durch
- Ruder schlägt unkontrolliert aus (Wind/Strömung)
- Metallisches Knacken/Knallen beim Bruch

**Ursachen:**

| Rang | Ursache | Häufigkeit |
|------|--------|-----------|
| 1 | Ermüdung durch Biegewechsel an Umlenkrollen | 35 % |
| 2 | Korrosion (Chlorid-Angriff) | 25 % |
| 3 | Überlastung (Grundberührung, Treibgut) | 15 % |
| 4 | Knicke im Seil (falsche Verlegung) | 12 % |
| 5 | Fehlerhafte Endverbindung (Presshülse, Gabelterminal) | 8 % |
| 6 | UV-Degradation der Kunststoffummantelung | 5 % |

**Vorbeugende Maßnahmen:**
- Seilzug alle 5–8 Jahre erneuern (unabhängig vom Zustand)
- Monatliche Sichtprüfung auf Litzenbrüche (>3 Litzenbrüche/30 cm → sofort tauschen)
- Umlenkrollen-Durchmesser mindestens 12× Seildurchmesser
- Keine Knicke, keine scharfen Kanten an Seilführungen
- 316er Edelstahl-Seile verwenden (nicht 304)

**Sofortmaßnahme bei Bruch auf See:**
1. Notpinne aufsetzen (muss jederzeit zugänglich sein!)
2. Geschwindigkeit reduzieren
3. Segel reduzieren (Segelyacht)
4. Seilrest sichern (kann sich im Ruder verfangen)
5. Provisorische Reparatur: Seilklemmen (Bulldog-Klemmen) als Notverbindung

**Confidence:** measured (Unfallberichte MAIB, BSU)

### 6.4 Fehlerbild: Hydraulikleck (Hydraulic Leak)

**Beschreibung:**
Hydrauliköl tritt aus dem Steuersystem aus — an Anschlüssen, Schläuchen, Pumpe oder Zylinder.

**Symptome:**
- Ölspuren unter dem Pedestal oder am Steuerzylinder
- Langsam zunehmende Schwergängigkeit
- „Schwammiges" Steuergefühl (Luft dringt ein)
- Ölstand im Reservoir sinkt
- Im Extremfall: Steuerung fällt aus (kein Öl mehr im System)

**Ursachen:**

| Rang | Ursache | Häufigkeit |
|------|--------|-----------|
| 1 | Schlauchverbindung undicht (locker, O-Ring defekt) | 30 % |
| 2 | Hydraulikschlauch gealtert/porös | 25 % |
| 3 | Zylinderdichtung verschlissen | 20 % |
| 4 | Pumpen-Wellendichtring defekt | 12 % |
| 5 | Korrosion an Leitungsanschlüssen | 8 % |
| 6 | Mechanische Beschädigung (Scheuerstelle) | 5 % |

**Diagnoseschritte:**
1. Ölstand prüfen → Reservoirpegel dokumentieren
2. Alle Anschlüsse visuell prüfen (sauberes Papier unterlegen)
3. Schlauchoberfläche auf Risse, Schwellungen, Scheuerstellen prüfen
4. Zylinderstange auf Ölfilm prüfen (zeigt Dichtungsverschleiß an)
5. Drucktest: System unter Druck setzen, Druck über 15 min beobachten

**Behebung:**
- Anschlüsse nachziehen (Drehmoment beachten!)
- O-Ringe und Dichtungen erneuern
- Schläuche bei Alterung komplett tauschen
- Zylinder-Dichtungssatz wechseln
- System nach Reparatur entlüften und Ölstand auffüllen

**ACHTUNG:** Hydrauliköl ist umweltgefährdend. Austretendes Öl auffangen. Bilgenöl ordnungsgemäß entsorgen.

**Confidence:** measured (Hersteller-Wartungsanleitungen)

### 6.5 Fehlerbild: Ruderlagerschaden (Rudder Bearing Failure)

**Beschreibung:**
Die Lagerbuchsen des Ruderschafts (oben im Kokerrohr, unten im Skeg) sind verschlissen, korrodiert oder gebrochen.

**Symptome:**
- Klopfendes Geräusch bei Ruderbewegung
- Seitliches Spiel am Ruderblatt (Ruder „wackelt")
- Wassereinbruch durch den Steuerkoker
- Steigende Schwergängigkeit
- Punktuell erhöhte Reibung im Ruderweg

**Ursachen:**

| Rang | Ursache | Häufigkeit |
|------|--------|-----------|
| 1 | Normaler Verschleiß (Lebensdauer überschritten) | 35 % |
| 2 | Mangelhafte Schmierung | 25 % |
| 3 | Fehlende Wellendichtung → Salzwasser im Lager | 20 % |
| 4 | Grundberührung/Schlag → Schaftverbiegung → asymmetrischer Verschleiß | 12 % |
| 5 | Falsches Lagermaterial | 8 % |

**Lebensdauer typischer Lagermaterialien:**

| Lagermaterial | Lebensdauer | Schmierung |
|--------------|-----------|-----------|
| Bronze | 8–15 Jahre | Fett (regelmäßig) |
| PTFE/GFK (Jefa-Typ) | 15–25 Jahre | Wartungsfrei |
| Delrin/POM | 5–10 Jahre | Wartungsfrei, aber empfindlich gegen Sand |
| Gummi (Cutless-Typ) | 8–12 Jahre | Wassergeschmiert |

**Diagnoseschritte:**
1. Ruder von außen seitlich belasten → Lagerspiel fühlen
2. Taucher: Ruder unter Wasser bewegen, Spiel am Skeg/Koker beobachten
3. Innen: Ruderschaft-Austrittspunkt am Koker auf Auslaufen prüfen
4. Ruder ausbauen: Lagerbuchsen visuell und haptisch prüfen

**Behebung:**
- Lagerbuchsen austauschen (erfordert meist Ruderausbau)
- Bei PTFE/GFK-Lagern: Buchse herauspressen, neue einpressen
- Schaftoberfläche prüfen (Riefen → Schaft erneuern oder nachschleifen)
- Dichtungssystem erneuern (Lippendichtung + PSS/Packung)

**Confidence:** measured (GL/DNV-Surveyberichte, Jefa-TDS)

### 6.6 Fehlerbild: Steuerrad blockiert (Locked Helm)

**Beschreibung:**
Das Steuerrad lässt sich nicht oder nur mit extremer Kraft drehen. Totale Blockade.

**Symptome:**
- Steuerrad dreht nicht
- Knackendes Geräusch beim Versuch zu drehen
- Plötzliches Auftreten (nicht graduell)

**Ursachen:**

| Rang | Ursache | Häufigkeit |
|------|--------|-----------|
| 1 | Fremdkörper im Getriebe/Quadrant | 25 % |
| 2 | Seil von Rolle gesprungen → verklemmt | 20 % |
| 3 | Kette von Kettenrad gesprungen | 15 % |
| 4 | Hydraulik-Ventil geschlossen (Bypass vergessen) | 15 % |
| 5 | Treibgut am Ruder (Netz, Leine, Plastik) | 15 % |
| 6 | Ruderlager gefressen (Festfressen) | 10 % |

**Sofortmaßnahme:**
1. Keine Gewalt am Steuerrad! (kann Getriebe zerstören)
2. Ursache lokalisieren: Blockade an Steuerrad oder Ruder?
3. Notpinne aufsetzen (wenn Ruder selbst nicht blockiert)
4. Treibgut prüfen (Taucher oder Rückwärtsfahren)

**Confidence:** documented (Surveyberichte, Herstellersupport-Daten)

### 6.7 Fehlerbild: Ruderblattabriss (Rudder Loss)

**Beschreibung:**
Das Ruderblatt trennt sich vollständig oder teilweise vom Ruderschaft. Katastrophaler Steuerverlust.

**Symptome:**
- Schlagartige Steuerungslosigkeit
- Lauter Knall oder Schlag (Bruchmoment)
- Ruderblatt treibt neben dem Boot (oder sinkt)
- Bei Teilabriss: Flattern und Vibration

**Ursachen:**

| Rang | Ursache | Häufigkeit |
|------|--------|-----------|
| 1 | Grundberührung → Schaft knickt → Blatt reißt ab | 30 % |
| 2 | Materialermüdung (Schaft/Blatt-Verbindung) | 25 % |
| 3 | Delaminierung des Ruderblatts (GFK) | 20 % |
| 4 | Korrosion des Schaft-Innengerüsts | 15 % |
| 5 | Fehlerhaftes Design/Unterdimensionierung | 10 % |

**Vorbeugende Maßnahmen:**
- Regelmäßige Ultraschall-Prüfung des Ruderschafts (alle 5–10 Jahre)
- Klopftest am Ruderblatt (hohl = Delaminierung oder Wassereinbruch)
- Gewichtskontrolle des Ruderblatts (Zunahme = Wassereinbruch)
- Endoskopie durch Inspektionsbohrung

**Notsteuerung nach Ruderverlust:**
1. Geschwindigkeit reduzieren
2. Notsteuerung aus Spinnaker-Baum + Paddel/Brett improvisieren
3. Schleppleine achtern als Richtungsstabilisator (Schleppbremse)
4. Segel: Vorsegel-Balance (Fock/Genua für Kursänderungen)
5. Seenotfall melden (wenn nötig)

**Confidence:** measured (Unfallberichte MAIB, BSU, USCG)

### 6.8 Fehlerbild: Autopilot-Steuerungskonflikt

**Beschreibung:**
Autopilot und manuelle Steuerung arbeiten gegeneinander oder der Autopilot übersteuert ungewollt.

**Symptome:**
- Boot fährt nicht den gewünschten Kurs trotz manuellem Eingriff
- Steuerrad bewegt sich bei aktivem Autopilot (korrekt) aber auch bei deaktiviertem (Fehler)
- Ruckartige Ruderbewegungen
- Autopilot meldet „Drive Error" oder „Low Fluid"

**Ursachen:**

| Rang | Ursache | Häufigkeit |
|------|--------|-----------|
| 1 | Bypass-Ventil falsch eingestellt | 30 % |
| 2 | Autopilot nicht korrekt desaktiviert | 25 % |
| 3 | Ruderlage-Sensor falsch kalibriert | 20 % |
| 4 | Hydraulikleck im Autopilot-Kreis | 15 % |
| 5 | Elektromagnetisches Störsignal (EMV) | 10 % |

**Diagnoseschritte:**
1. Autopilot vollständig ausschalten (nicht nur Standby)
2. Bypass-Ventil-Stellung prüfen (offen = manuell, geschlossen = AP)
3. Ruderlage-Sensor kalibrieren (nach Herstelleranleitung)
4. Hydraulikkreis des AP auf Leck prüfen

**Confidence:** documented (Herstellersupport-Daten)

### 6.9 Fehlerbild: Korrosion am Ruderschaft

**Beschreibung:**
Der Ruderschaft zeigt Anzeichen von Korrosion — Lochfraß (Pitting), Spaltkorrosion oder interkristalline Korrosion.

**Symptome:**
- Sichtbare Korrosionsspuren am freiliegenden Schaftbereich
- Rostbraune Ablagerungen im Kokerbereich
- Schaftdurchmesser-Reduktion (messbar)
- Im Extremfall: Schaftbruch

**Ursachen:**

| Rang | Ursache | Häufigkeit |
|------|--------|-----------|
| 1 | Falsches Material (304 statt 316L) | 30 % |
| 2 | Galvanische Korrosion (fehlende Isolierung zu Bronzelagern) | 25 % |
| 3 | Spaltkorrosion im Lagerbereich | 20 % |
| 4 | Fehlende/erschöpfte Opferanoden | 15 % |
| 5 | Streustrom-Korrosion | 10 % |

**Vorbeugende Maßnahmen:**
- Ausschließlich 316L oder besser Aquamet 22 verwenden
- Opferanoden an der Ruderanlage korrekt dimensionieren
- Galvanische Trennung zwischen Schaft und Bronze-/Stahlteilen
- Regelmäßige Ultraschall-Dickenmessung (alle 5 Jahre)

**Confidence:** measured (Materialprüfberichte, GL/DNV-Vorschriften)

### 6.10 Fehlerbild: Steuerkoker-Leck (Rudder Tube Leak)

**Beschreibung:**
Wasser dringt durch den Steuerkoker (das Rohr, durch das der Ruderschaft ins Boot geführt wird) ins Innere ein.

**Symptome:**
- Feuchtigkeit/Tropfen im Bereich des Steuerkokers
- Wasseransammlung in der Bilge achtern
- Korrosion an umliegenden Metallteilen
- Schimmelbildung im Stauraum

**Ursachen:**

| Rang | Ursache | Häufigkeit |
|------|--------|-----------|
| 1 | Lippendichtung verschlissen | 35 % |
| 2 | Packung (Stopfbuchse) trocken/verhärtet | 25 % |
| 3 | Kokerrohr gerissen (GFK-Laminat) | 15 % |
| 4 | Kokerrohr-Flansch undicht | 15 % |
| 5 | Schaftoberfläche beschädigt (Riefen) | 10 % |

**Behebung:**
- Lippendichtung erneuern (Boot muss aus dem Wasser)
- Packung erneuern/nachziehen (kann oft im Wasser erfolgen)
- Kokerrohr-Laminat reparieren (Epoxid + Glasgewebe)
- PSS-Wellendichtung (Premium Solution) nachrüsten

**Confidence:** measured (Jefa-TDS, Surveyberichte)

### 6.11 Fehlerbild: Vibration im Steuerrad (Helm Vibration)

**Beschreibung:**
Das Steuerrad vibriert spürbar, insbesondere bei bestimmten Geschwindigkeiten oder Ruderwinkeln.

**Symptome:**
- Spürbares Zittern am Steuerrad
- Dröhnendes Geräusch im Steuerbereich
- Geschwindigkeitsabhängig (resonanzartig)
- Ggf. ruderwinkelabhängig

**Ursachen:**

| Rang | Ursache | Häufigkeit |
|------|--------|-----------|
| 1 | Kavitation am Ruderblatt | 25 % |
| 2 | Ruderblatt beschädigt (Delle, Riss) | 20 % |
| 3 | Propeller-Unwucht übertragen | 20 % |
| 4 | Ruderlager-Verschleiß | 15 % |
| 5 | Seilzug-Resonanz | 10 % |
| 6 | Loser Quadrant | 10 % |

**Diagnoseschritte:**
1. Vibration geschwindigkeitsabhängig? → Kavitation oder Propeller
2. Vibration ruderwinkelabhängig? → Ruderblatt-Schaden
3. Vibration bei allen Geschwindigkeiten? → Mechanisches Problem (Lager, Quadrant)

**Confidence:** estimated (Erfahrungswerte, Werft-Konsens)

### 6.12 Fehlerbild: Falsche Ruderanzeige (Rudder Indicator Error)

**Beschreibung:**
Die Ruderlageanzeige am Steuerplatz zeigt eine andere Ruderlage an, als tatsächlich vorhanden ist.

**Symptome:**
- Ruderanzeige zeigt Mittschiffs, Boot dreht aber
- Anzeige und tatsächliche Ruderlage weichen ab
- Autopilot steuert falsch (basiert auf falscher Ruderlage)

**Ursachen:**

| Rang | Ursache | Häufigkeit |
|------|--------|-----------|
| 1 | Ruderlage-Sensor nicht kalibriert | 35 % |
| 2 | Sensor-Gestänge lose/verbogen | 25 % |
| 3 | Sensor defekt (Potentiometer verschlissen) | 20 % |
| 4 | Kabelbruch/Kontaktproblem | 15 % |
| 5 | Magnetischer Sensor durch Metallteile gestört | 5 % |

**Behebung:**
- Sensor kalibrieren (Mittschiffs-Nullpunkt + Endausschlag)
- Gestänge fixieren/erneuern
- Sensor austauschen
- Kabelverbindungen prüfen

**Confidence:** documented (Herstellersupport)

---

## 7. Troubleshooting-Entscheidungsbäume

### 7.1 Entscheidungsbaum: Steuerung reagiert nicht

```
SYMPTOM: Steuerrad dreht sich, Ruder bewegt sich nicht
│
├─ Ist die Steuerung mechanisch (Seilzug/Kette)?
│   ├─ JA → Seilzug/Kette gebrochen?
│   │   ├─ JA → Seilzug/Kette erneuern. Ursache klären (Korrosion? Überlast?)
│   │   │         → NOTPINNE AUFSETZEN
│   │   └─ NEIN → Seil von Rolle gesprungen?
│   │       ├─ JA → Seil wieder einlegen, Rollenführung prüfen
│   │       └─ NEIN → Quadrant-Verbindung gebrochen?
│   │           ├─ JA → Bolzen/Gabelkopf erneuern → NOTPINNE
│   │           └─ NEIN → Konus am Ruderkopf durchrutscht?
│   │               ├─ JA → Konusmutter festziehen (Schaft/Quadrant)
│   │               └─ NEIN → Pedestal-Getriebe defekt → Fachmann
│   │
│   └─ NEIN → Hydraulische Steuerung?
│       ├─ JA → Ölstand prüfen
│       │   ├─ LEER → Leck suchen und beheben → auffüllen, entlüften
│       │   └─ OK → Luft im System?
│       │       ├─ JA → System entlüften
│       │       └─ NEIN → Bypass-Ventil offen (AP-Modus)?
│       │           ├─ JA → Bypass schließen für manuellen Betrieb
│       │           └─ NEIN → Pumpe defekt → Fachmann / NOTPINNE
│       │
│       └─ NEIN → Elektrische Steuerung?
│           ├─ JA → Stromversorgung prüfen
│           │   ├─ KEIN STROM → Sicherung prüfen, Batterie prüfen
│           │   └─ STROM OK → Fehlermeldung am Display?
│           │       ├─ JA → Fehlercode auslesen → Herstellersupport
│           │       └─ NEIN → Steuer-ECU defekt → Fachmann / NOTPINNE
│           └─ NEIN → Unbekannter Steuerungstyp → Fachmann
```

### 7.2 Entscheidungsbaum: Steuerung schwergängig

```
SYMPTOM: Steuerrad lässt sich nur schwer drehen
│
├─ Bei welcher Fahrt? Nur unter Last oder auch im Hafen?
│   ├─ NUR UNTER LAST → Ruder normal, Problem = zu viel Ruderkraft
│   │   ├─ Geschwindigkeit reduzieren → besser?
│   │   │   ├─ JA → Ruder ggf. überbalanciert oder zu groß. Dimensionierung prüfen.
│   │   │   └─ NEIN → Ruderlager prüfen (Taucher: Ruder seitlich belasten)
│   │   │       ├─ SPIEL → Ruderlager erneuern
│   │   │       └─ KEIN SPIEL → Bewuchs am Ruder? → Reinigen
│   │
│   └─ AUCH IM HAFEN (ohne Fahrt) → Mechanisches Problem
│       ├─ Seilzug: Umlenkrollen einzeln prüfen
│       │   ├─ Rolle klemmt → Rolle erneuern/schmieren
│       │   └─ Rollen OK → Seilführung zu eng? → Radien vergrößern
│       │
│       ├─ Kette: Kettenglieder auf Leichtgängigkeit prüfen
│       │   ├─ Steife Glieder → Kette reinigen, schmieren oder erneuern
│       │   └─ Kette OK → Kettenrad-Ausrichtung prüfen
│       │
│       ├─ Hydraulik: Öl-Viskosität korrekt?
│       │   ├─ NEIN → Ölwechsel mit korrektem Öl
│       │   └─ JA → Zylinder-Dichtungen geprüft?
│       │       ├─ Schwergängiger Zylinder → Dichtungssatz erneuern
│       │       └─ Zylinder OK → Pumpe verschlissen → erneuern
│       │
│       └─ Steuerkoker-Dichtung zu stramm?
│           ├─ JA → Dichtung lösen, korrekt einstellen
│           └─ NEIN → Pedestal-Getriebe → öffnen, inspizieren
```

### 7.3 Entscheidungsbaum: Hydrauliksystem — Luft im System

```
SYMPTOM: Steuerung fühlt sich „schwammig" an (hydraulisch)
│
├─ Ölstand prüfen
│   ├─ NIEDRIG → Auffüllen → Leck suchen (siehe 6.4)
│   │   └─ Nach Auffüllen: System entlüften
│   │
│   └─ NORMAL → War das System kürzlich geöffnet?
│       ├─ JA → System wurde nicht korrekt entlüftet
│       │   └─ ENTLÜFTUNGSPROZEDUR:
│       │       1. Reservoir öffnen
│       │       2. Steuerrad langsam Lock-to-Lock drehen (10×)
│       │       3. Entlüftungsschraube am Zylinder öffnen (Öl-Luft-Gemisch ablassen)
│       │       4. Schließen wenn blasenfrei
│       │       5. Ölstand nachfüllen
│       │       6. Wiederhole bis keine Blasen mehr
│       │
│       └─ NEIN → Luft dringt an einer Stelle ein
│           ├─ Saugseite der Pumpe prüfen (Verbindungen, O-Ringe)
│           ├─ Kolbenstangen-Dichtung prüfen (Luft kann bei Rückhub eingesaugt werden)
│           └─ Leitungsanschlüsse prüfen (besonders nach Vibrationsbelastung)
```

### 7.4 Entscheidungsbaum: Steuerrad hat Spiel

```
SYMPTOM: Steuerrad hat tote Zone in Mittellage
│
├─ Wie groß ist das Spiel?
│   ├─ <5° → Normal für die meisten Systeme
│   ├─ 5°–15° → Korrektur empfohlen
│   │   ├─ Seilzug: Nachspannen
│   │   ├─ Kette: Kettenspannung prüfen, Verschleiß prüfen
│   │   └─ Hydraulik: Entlüften, Ölstand prüfen
│   │
│   └─ >15° → Dringend beheben
│       ├─ Ruder fixieren, Steuerrad drehen → Spiel in Übertragung?
│       │   ├─ JA → Spiel ist in der Übertragung
│       │   │   ├─ Seilzug: Seile gelängt → erneuern (Nachspannen reicht oft nicht mehr)
│       │   │   ├─ Kette: Kettenverschleiß → Kette + Kettenrad erneuern
│       │   │   └─ Zahnstange: Zahnspiel → Getriebe erneuern
│       │   │
│       │   └─ NEIN → Spiel ist am Ruder
│       │       ├─ Quadrant lose? → Konusmutter prüfen
│       │       ├─ Ruderlager ausgschlagen? → Lager erneuern
│       │       └─ Schaft-Konus aufgeweitet? → Schaft/Konus prüfen
│       │
│       └─ Autopilot aktiv? → AP produziert Totzone?
│           ├─ JA → AP desaktivieren, Bypass öffnen → Spiel weg?
│           │   ├─ JA → AP-Hydraulik hat Leckage → AP-Service
│           │   └─ NEIN → Problem liegt im Hauptsystem
│           └─ NEIN → weiter oben
```

### 7.5 Entscheidungsbaum: Kursinstabilität bei Autopilot

```
SYMPTOM: Autopilot hält Kurs nicht stabil (pendelt, überschießt)
│
├─ Mechanisches Problem oder Einstellungsproblem?
│   ├─ MECHANISCH prüfen:
│   │   ├─ Ruderspiel >10°? → Beheben (siehe 7.4)
│   │   ├─ Ruderlage-Sensor korrekt kalibriert? → Nachkalibrieren
│   │   ├─ Hydraulikleck im AP-Kreis? → Beheben
│   │   └─ AP-Antrieb hat zu wenig Kraft? → AP-Dimensionierung prüfen
│   │
│   └─ EINSTELLUNG prüfen:
│       ├─ Rudder Gain zu hoch? → Reduzieren (weniger Ruderausschlag pro ° Kursabweichung)
│       ├─ Counter Rudder zu niedrig? → Erhöhen (früher gegensteuern)
│       ├─ Deadband zu eng? → Vergrößern (kleine Kursabweichungen ignorieren)
│       ├─ Response time zu schnell? → Verlangsamen
│       └─ Sea State Filter korrekt? → Anpassen an aktuelle Bedingungen
│
├─ Nur bei bestimmten Kursen?
│   ├─ Nur bei achterlichem Wind → AP hat Probleme mit Gieren (Broachen)
│   │   → Segelfläche reduzieren, AP-Modus auf „Downwind" stellen
│   │
│   └─ Nur bei bestimmter Geschwindigkeit → Resonanzproblem
│       → Speed-abhängige Gain-Anpassung aktivieren (wenn verfügbar)
│
└─ Kompass-Problem?
    ├─ Kompass korrekt kalibriert? → Deviation prüfen, Compass Swing durchführen
    ├─ Magnetische Störung? → Neue Elektronik in der Nähe des Fluxgate?
    └─ GPS-Kopfrichtung statt Kompass? → GPS-COG ist träge → Kompass bevorzugen
```

---

## 8. FAQ

### 8.1 Allgemeine Fragen

**F1: Wie oft muss eine Steueranlage gewartet werden?**
A: Mindestens jährlich eine Sichtprüfung aller Komponenten. Seilzugsteuerungen: vierteljährlich Seilspannung prüfen. Hydraulik: monatlich Ölstand prüfen. Detailinspektion alle 5 Jahre mit Ausbau kritischer Komponenten.

**F2: Welche Steuerung ist die beste für eine 12 m Segelyacht?**
A: Standard ist eine Ketten-Seilzug-Kombination (z.B. Whitlock Cobra 40 oder Jefa CSC-900). Für höchste Qualität und Langlebigkeit: Jefa-Vollkettensystem. Hydraulisch nur, wenn Autopilot-Integration zwingend oder Ruderkräfte sehr hoch.

**F3: Kann ich eine Seilzugsteuerung auf Hydraulik umrüsten?**
A: Ja, technisch möglich. Erfordert: Hydraulik-Helm-Pumpe im Pedestal, Steuerzylinder am Ruder, Leitungen, Ölbehälter. Kosten: €2.000–€5.000 (Material) plus Einbau. Verlust des direkten Feedbacks beachten.

**F4: Was ist eine Notpinne und brauche ich eine?**
A: Eine Notpinne ist ein Kurzhebel, der direkt auf den Ruderkopf aufgesetzt wird, wenn die reguläre Steuerung ausfällt. Jede Yacht mit Radsteuerung sollte eine Notpinne mitführen. Bei Offshore-Regatten (ISAF/World Sailing) ist sie Pflicht.

**F5: Wie erkenne ich, dass meine Seilzüge erneuert werden müssen?**
A: Erneuerung bei: >3 gebrochene Litzen pro 30 cm, sichtbare Korrosion, Knicke, Verformung, Alter >8 Jahre (Fahrt) oder >5 Jahre (Regatta). Regelmäßige Prüfung: Handschuhe anziehen, Seil langsam durch die Hand ziehen — gebrochene Litzen stechen.

### 8.2 Hydraulik-Fragen

**F6: Welches Hydrauliköl soll ich verwenden?**
A: Immer das vom Hersteller spezifizierte Öl. Im Zweifelsfall: ISO VG 15 Hydrauliköl. SeaStar: HA5430. Vetus: HF15. Kobelt: Je nach Modell Dexron III oder Hydrauliköl. NIE verschiedene Öle mischen!

**F7: Wie entlüfte ich eine hydraulische Steuerung?**
A: 1) Ölstand auf Maximum füllen. 2) Steuerrad langsam Lock-to-Lock drehen (20–30 Mal). 3) Entlüftungsschraube(n) am Zylinder öffnen, bis blasenfreies Öl kommt. 4) Ölstand nachfüllen. 5) Wiederholen bis kein Schwammgefühl mehr.

**F8: Meine hydraulische Steuerung verliert Öl — ist das gefährlich?**
A: Ja, potentiell gefährlich. Ölverlust führt zu: 1) Luft im System → schwammige Steuerung. 2) Weiterem Ölverlust → Totalausfall. Sofort Ursache finden und beheben. Auf See: Ölstand regelmäßig prüfen, Reserveöl mitführen.

**F9: Kann ich einen zweiten Steuerplatz nachrüsten (Flybridge)?**
A: Bei hydraulischer Steuerung: Ja, relativ einfach. Zweite Helm-Pumpe parallel anschließen. Ölvolumen muss angepasst werden. Bei mechanischer Steuerung: Sehr aufwändig (zweites Seil-/Kettensystem).

**F10: Was bedeutet „Lock-to-Lock"?**
A: Die Anzahl der Steuerrad-Umdrehungen, um das Ruder von Hartbackbord (maximaler Ausschlag links) zu Hartsteuerbord (maximaler Ausschlag rechts) zu drehen. Typisch: 3–5 Umdrehungen bei Segelyachten.

### 8.3 Mechanik-Fragen

**F11: Wie spanne ich Steuerseile nach?**
A: Seilspanner (Turnbuckle) im Seilzug um gleiche Umdrehungszahl auf beiden Seiten drehen. Korrekte Spannung: Seil soll sich in der Mitte des Verlaufs ca. 10–15 mm seitlich drücken lassen (Daumenprobe). Zu stramm = erhöhte Reibung, zu lose = Spiel.

**F12: Mein Steuerrad klackert bei Seegang — was tun?**
A: Ursache ist meist Spiel in der Steueranlage. Prüfen: 1) Seilspannung. 2) Kettenspannung. 3) Quadrant-Befestigung. 4) Pedestal-Getriebespiel. 5) Ruderlager. Systematisch von einem Ende zum anderen prüfen.

**F13: Welchen Quadranten-Radius soll ich wählen?**
A: Größerer Radius = mehr Übersetzung = leichtere Steuerung, aber mehr Umdrehungen Lock-to-Lock. Kleinerer Radius = direktere Steuerung, aber schwerer am Rad. Faustregel: Quadrant so groß wie der Raum es zulässt.

**F14: Was ist der Unterschied zwischen Geall-Kette und Rollenkette?**
A: Geall-Kette hat flache Seitenplatten und minimales Spiel — speziell für Steuerungen entwickelt. Rollenkette (DIN 8187) ist universell, hat aber mehr inherentes Spiel. Für Steuerungen ist Geall-Kette vorzuziehen.

**F15: Kann ich Edelstahl-Seile durch Dyneema/PBO ersetzen?**
A: Nein, nicht empfohlen. Textilseile haben zu viel Dehnung unter Wechsellast und sind anfällig gegen UV und Knickbelastung an Umlenkrollen. Drahtseile aus Edelstahl bleiben Standard für Steuerungen.

### 8.4 Ruder-Fragen

**F16: Was ist der Unterschied zwischen Spatenruder und Skeg-Ruder?**
A: Spatenruder = nur oben gelagert, freitragend → maximale Ruderwirkung, aber empfindlich gegen Grundberührung. Skeg-Ruder = oben und unten gelagert, Skeg schützt → robuster, aber etwas weniger Ruderwirkung.

**F17: Mein Ruder hat Spiel — wie schlimm ist das?**
A: Axiales Spiel (auf/ab): bis 1 mm akzeptabel. Radiales Spiel (seitlich): bis 0,5 mm akzeptabel. Darüber: Lagerverschleiß → baldmöglichst erneuern. Starkes Spiel (>2 mm) = Sicherheitsrisiko, sofort handeln.

**F18: Welches Material für den Ruderschaft?**
A: Empfehlung in aufsteigender Qualität: 1) Edelstahl 316L (Standard, ausreichend für die meisten Yachten). 2) Aquamet 22 (höhere Festigkeit, besser korrosionsbeständig — Jefa-Standard). 3) Nitronic 50 (höchste Festigkeit, Regatta/Superyacht).

**F19: Kann ich mein Ruderblatt reparieren, wenn es Wasser gezogen hat?**
A: Ja, wenn keine strukturelle Schädigung: 1) Ruder ausbauen. 2) Inspektionsbohrungen setzen. 3) Über Winter kopfüber trocknen lassen. 4) Epoxid-Harz injizieren. 5) Bohrungen verschließen. 6) Oberfläche neu laminieren. Bei schwerer Schädigung: Neues Ruderblatt.

**F20: Wie viel Balance sollte mein Ruder haben?**
A: Standard Segelyacht-Spatenruder: 17–22 % der Rudertiefe vor dem Schaft. Mehr Balance = leichtere Steuerung, weniger Feedback. Weniger Balance = schwerere Steuerung, besseres Feedback. Nie über 35 % — Gefahr der Überbalancierung (unkontrolliertes Ausschlagen).

### 8.5 Elektrische und Autopilot-Fragen

**F21: Brauche ich eine spezielle Steuerung für einen Autopiloten?**
A: Für hydraulische Autopiloten: Die Steueranlage muss hydraulisch sein oder ein hydraulisches Interface haben. Für Linear-Drive-Autopiloten: Mechanische Kopplung an Quadrant oder Tillerarm. Die Steueranlage muss das zusätzliche Gewicht und die Antriebskräfte aufnehmen können.

**F22: Was ist Fly-by-Wire und brauche ich das?**
A: Fly-by-Wire = rein elektronische Steuerung ohne mechanische Verbindung. Nur relevant für Superyachten >30 m oder Spezialanwendungen (Joystick-Steuerung mit IPS/Pod). Für normale Yachten nicht empfohlen — zu komplex, zu teuer, zu wenig Redundanz.

**F23: Mein Autopilot „jagt" (pendelt stark) — ist die Steuerung schuld?**
A: Möglicherweise. Häufige Ursachen: 1) Zu viel Spiel in der Steueranlage (Totzone). 2) Ruderlage-Sensor nicht kalibriert. 3) Hydraulikleck im AP-Kreis. 4) AP-Parameter falsch eingestellt (Gain zu hoch). Mechanik zuerst prüfen, dann Einstellungen.

**F24: Kann ich einen elektrischen Autopiloten mit einer Seilzugsteuerung verwenden?**
A: Ja. Linear-Drive-Autopiloten (z.B. Raymarine Type 1/2, B&G/Simrad) greifen direkt am Quadranten oder Tillerarm an. Der Autopilot arbeitet parallel zur Seilzugsteuerung. Bei Seilzug + Hydraulik-AP: separater hydraulischer Steuerzylinder nötig.

**F25: Welche Stromversorgung braucht eine elektrische Steuerung?**
A: Abhängig von Bootsgröße: 12–14 m: 12V, 20–40 A Dauerleistung. 14–18 m: 24V, 40–80 A. >18 m: 24V, 80–160 A. Separate Batteriebank empfohlen. USV (unterbrechungsfreie Stromversorgung) für Fly-by-Wire zwingend.

### 8.6 Spezial-Fragen

**F26: Was ist bei Zwillingsrudern anders?**
A: Zwei Ruder müssen synchron bewegt werden. Mechanisch: Verbindungsstange (Tie Rod) zwischen beiden Quadranten. Hydraulisch: Ein Zylinder pro Ruder, hydraulisch gekoppelt. Die Gesamtruderfläche ist größer, aber jedes Einzelruder kleiner. Unter Krängung arbeitet das Leeruder effektiver.

**F27: Wie dimensioniere ich eine Steuerung für einen Katamaran?**
A: Katamarane haben typischerweise zwei Ruder. Jedes Ruder ist kleiner als bei einem vergleichbaren Einrumpfboot. Die Steueranlage muss beide Ruder synchron bewegen. Hydraulisch ist Standard ab 12 m. Die Ruderkräfte sind durch die höheren Geschwindigkeiten (weniger Rumpfwiderstand) oft höher als erwartet.

**F28: Was tun, wenn die Steuerung auf See ausfällt?**
A: 1) Notpinne aufsetzen (sofort!). 2) Geschwindigkeit reduzieren (Motor drosseln / Segel bergen). 3) Seeraum schaffen. 4) Ursache diagnostizieren. 5) Provisorische Reparatur versuchen. 6) Wenn nicht reparierbar: Seenotfall melden (wenn Position kritisch), nächsten Hafen anlaufen.

**F29: Brauche ich einen Ruderlageanzeiger?**
A: Nicht zwingend für kleine Segelyachten (Pinne gibt direkte Rückmeldung). Empfohlen für alle Yachten >10 m und alle Motoryachten. Für Autopilot-Betrieb: unbedingt erforderlich (Autopilot braucht Ruderlage-Signal). Anzeige am Steuerplatz und (bei Motoryachten) am Flybridge.

**F30: Wie lagere ich die Steuerung richtig für den Winter ein?**
A: Seilzug: Seile auf Korrosion prüfen, leicht fetten (Ballistol oder Teflonspray). Hydraulik: Ölstand auf Maximum, Frostschutz beachten (ggf. Winteröl). Alle Systeme: Steuerrad in Mittstellung fixieren, Ruder sichern (Ruderstopper). Bei Auswasserung: Ruderblatt auf Schäden prüfen.

---

## 9. Glossar

### Deutsch-Englisch Fachbegriffe Steueranlagen

| Nr. | Deutsch | Englisch | Definition |
|-----|---------|----------|-----------|
| 1 | Anstellwinkel | Angle of Attack (AoA) | Winkel zwischen Ruderblatt-Profilsehne und Anströmrichtung. Bestimmt Ruderkraft und -moment. |
| 2 | Autopilot | Autopilot | Elektronisches System zur automatischen Kurssteuerung. Greift hydraulisch, elektrisch oder mechanisch in die Steueranlage ein. |
| 3 | Balancierung | Balance (Rudder) | Anteil der Ruderfläche vor der Schaftachse, in % der Rudertiefe. Reduziert das erforderliche Drehmoment. |
| 4 | Bypass-Ventil | Bypass Valve | Ventil in hydraulischen Steuerungen, das den Ölkreis umleitet — z.B. zur Umschaltung zwischen manueller Steuerung und Autopilot. |
| 5 | Drehmoment | Torque | Drehkraft am Ruderschaft [Nm]. Bestimmendes Maß für die Dimensionierung der gesamten Steueranlage. |
| 6 | Druckmittelpunkt | Center of Pressure (CP) | Punkt auf dem Ruderblatt, an dem die resultierende Ruderkraft angreift. Wandert mit dem Anstellwinkel. |
| 7 | Entlüften | Bleeding/Purging | Entfernen von Luftblasen aus dem hydraulischen Steuersystem durch gezieltes Ablassen von Öl-Luft-Gemisch. |
| 8 | Flossenruder | Flap Rudder | Ruder mit angelenkter Hinterkante (Klappe) für erhöhte Seitenkraft. Auch: Becker-Ruder. |
| 9 | Geall-Kette | Geall Chain | Spezialkette mit flachen Seitenplatten für Steuerungsanwendungen. Minimales Spiel, formschlüssig. |
| 10 | Hardover | Hardover / Hard Rudder | Maximaler Ruderausschlag (Hartsteuerbord oder Hartbackbord). Typisch ±35°. |
| 11 | Helm-Pumpe | Helm Pump | Hydraulikpumpe am Steuerplatz, die durch Drehen des Steuerrads Öldruck erzeugt. |
| 12 | Hydrauliköl | Hydraulic Fluid | Spezialöl für hydraulische Steuersysteme. ISO VG 15–32. Muss mit Dichtungsmaterialien kompatibel sein. |
| 13 | Kavitation | Cavitation | Bildung und Kollaps von Dampfblasen am Ruderblatt bei hoher Geschwindigkeit/starkem Ausschlag. Verursacht Vibration und Erosion. |
| 14 | Kokerrohr | Rudder Tube / Rudder Trunk | Rohr, durch das der Ruderschaft ins Bootsinnere geführt wird. Enthält Lager und Dichtungen. |
| 15 | Langkiel | Full Keel | Kielform, bei der der Kiel über fast die gesamte Unterwasserlänge reicht. Ruder am Kielende angelenkt. |
| 16 | Lock-to-Lock | Lock-to-Lock | Anzahl der Steuerrad-Umdrehungen von Hartbackbord bis Hartsteuerbord. Typisch 3–5 für Segelyachten. |
| 17 | Luvgierigkeit | Weather Helm | Tendenz eines Segelboots, in den Wind zu drehen. Erfordert permanenten Gegenruder-Winkel. Wünschenswert: 3–5° Ruderlage. |
| 18 | NFB (No Feedback) | No Feedback | Steuergetriebe-Typ, der keine Ruderkräfte an das Steuerrad zurückleitet. Standard bei Motorboot-Zahnstangensteuerungen. |
| 19 | Notpinne | Emergency Tiller | Kurzer Hebel, der bei Ausfall der regulären Steuerung direkt auf den Ruderkopf aufgesetzt wird. Pflichtausrüstung. |
| 20 | Pedestal | Pedestal / Steering Column | Steuersäule, die das Steuerrad trägt und das Steuergetriebe enthält. |
| 21 | Pinne | Tiller | Direkter Hebel vom Ruderkopf zum Rudergänger. Älteste und einfachste Steuerform. |
| 22 | Propellerstrahl | Propeller Wash / Prop Wash | Wasserstrahl hinter dem Propeller. Erhöht die Anströmgeschwindigkeit am Ruder. |
| 23 | Quadrant | Quadrant | Bogensegment (90°–120°) auf dem Ruderkopf, an dem Seile oder Ketten angreifen. Wandelt Linearbewegung in Rotation um. |
| 24 | Radeffekt | Paddle Wheel Effect | Seitwärtskraft des Propellers durch asymmetrische Anströmung. Beeinflusst die neutrale Ruderlage. |
| 25 | Rückmeldung | Feedback / Helm Feel | Übertragung der am Ruder wirkenden Kräfte zurück an das Steuerrad oder die Pinne. Wichtig für intuitives Steuern. |
| 26 | Ruderlage | Rudder Angle / Helm Position | Aktueller Winkel des Ruderblatts relativ zur Mittschiffsebene. Angezeigt auf dem Ruderlage-Anzeiger. |
| 27 | Ruderlageanzeiger | Rudder Angle Indicator (RAI) | Instrument, das die aktuelle Ruderlage am Steuerplatz anzeigt. Essentiell für Autopilot-Betrieb. |
| 28 | Ruderschaft | Rudder Stock / Rudder Post | Vertikale Welle, die das Ruderblatt mit dem Steuergetriebe verbindet. Material: 316L, Aquamet 22, Nitronic 50. |
| 29 | Seilzug | Wire Rope / Steering Cable | Edelstahl-Drahtseil (7×19) zur Kraftübertragung vom Pedestal zum Quadranten. |
| 30 | Skeg | Skeg | Feststehender Anhang vor dem Ruder, der als Strömungsleitfläche und untere Lagerstütze dient. |
| 31 | Spatenruder | Spade Rudder | Freihängendes Ruder, nur am Schaft im Koker gelagert. Maximale Ruderwirkung, minimaler Schutz. |
| 32 | Steuerkoker | Rudder Port / Rudder Gland | Durchführung des Ruderschafts durch den Rumpf. Enthält Dichtungen und oberes Lager. |
| 33 | Steuerübersetzung | Steering Ratio / Gear Ratio | Verhältnis zwischen Steuerrad-Drehung und resultierender Ruderbewegung. Bestimmt Lock-to-Lock und Handkraft. |
| 34 | Steuerzylinder | Steering Cylinder / Ram | Hydraulikzylinder, der den Tillerarm oder Quadranten bewegt. Linear (Kolben) oder rotatorisch. |
| 35 | Strömungsabriss | Stall | Ablösung der Strömung auf der Saugseite des Ruderblatts bei Überschreiten des kritischen Anstellwinkels (~15–20°). |
| 36 | Tillerarm | Tiller Arm / Rudder Arm | Hebel am Ruderkopf, an dem der Steuerzylinder oder Linearantrieb angreift. Gerade oder gekröpft. |
| 37 | Umlenkrolle | Sheave / Pulley / Fairlead | Rolle zur Richtungsänderung des Steuerseils. Kugelgelagert, min. 12× Seildurchmesser. |
| 38 | Zahnstange | Rack (Rack-and-Pinion) | Gerade verzahnte Stange, die durch ein Ritzel linear bewegt wird. Standard bei Motorboot-Steuerungen. |
| 39 | Zwillingsruder | Twin Rudders | Zwei seitlich versetzte Ruder, typisch bei Breitheckyachten und Katamaranen. Synchron gesteuert. |
| 40 | Aquamet 22 | Aquamet 22 | Hochfeste, korrosionsbeständige Edelstahllegierung (Carpenter Technology) für Ruderschäfte. Höhere Festigkeit als 316L. |
| 41 | Backbord | Port | Linke Seite des Schiffes (in Fahrtrichtung gesehen). |
| 42 | Steuerbord | Starboard | Rechte Seite des Schiffes (in Fahrtrichtung gesehen). |
| 43 | Totzone | Deadband / Dead Zone | Bereich am Steuerrad, in dem keine Ruderbewegung erfolgt (Spiel). |
| 44 | Wellendichtung | Shaft Seal | Dichtung am Ruderschaft-Durchgang, verhindert Wassereinbruch. Typen: Lippendichtung, Stopfbuchse, PSS. |
| 45 | Windfahnensteuerung | Wind Vane Self-Steering | Mechanische Selbststeuerung durch Windfahne auf dem Achterdeck. Nutzt Windkraft zur Ruderverstellung. Keine Elektrik nötig. |

---

## 10. Schnell-Referenz

### 10.1 Steuerungstyp-Auswahl nach Bootsgröße

```
                 Seilzug    Kette    Zahnstange    Hydraulik    Elektrisch
Boot <6m:        ────       ────     ████████████   ────         ────
Boot 6–8m:       ████████   ────     ████████████   ████         ────
Boot 8–10m:      ████████   ████████ ████████       ████████     ────
Boot 10–14m:     ████████   ████████ ────           ████████     ████
Boot 14–18m:     ████       ████████ ────           ████████████ ████████
Boot 18–24m:     ────       ────     ────           ████████████ ████████
Boot >24m:       ────       ────     ────           ████████████ ████████████

████████████ = Standard/empfohlen
████████     = Möglich/häufig
████         = Selten/nur in Ausnahmen
────         = Nicht geeignet
```

### 10.2 Drehmoment-Tabelle (Richtwerte)

| Bootslänge (m) | Segelyacht (Nm) | Motoryacht (Nm) |
|----------------|-----------------|-----------------|
| 7 | 50–80 | 40–60 |
| 8 | 60–100 | 50–80 |
| 9 | 80–130 | 70–110 |
| 10 | 100–170 | 100–160 |
| 11 | 130–220 | 140–220 |
| 12 | 150–280 | 200–350 |
| 13 | 200–350 | 280–450 |
| 14 | 250–450 | 350–600 |
| 15 | 300–550 | 450–800 |
| 16 | 400–700 | 600–1.100 |
| 18 | 550–1.000 | 900–1.800 |
| 20 | 750–1.400 | 1.300–2.800 |
| 24 | 1.200–2.200 | 2.500–5.000 |

### 10.3 Seilzug-Verschleißindikatoren

| Zustand | Bewertung | Maßnahme |
|---------|----------|---------|
| Keine Litzenbrüche, glatte Oberfläche | ✅ Gut | Weiter nutzen |
| 1–2 Litzenbrüche pro 30 cm | ⚠️ Verschleiß beginnt | Beobachten, planen |
| 3–5 Litzenbrüche pro 30 cm | 🔴 Erneuerung nötig | Baldmöglichst tauschen |
| >5 Litzenbrüche pro 30 cm | ⛔ Sofort tauschen | Sicherheitsrisiko! |
| Sichtbare Korrosion | 🔴 Erneuerung nötig | Tauschen |
| Knicke oder Verformung | ⛔ Sofort tauschen | Kann jederzeit brechen |

### 10.4 Hydrauliköl-Kompatibilitätsmatrix

| Hersteller | Empfohlenes Öl | ISO-Klasse | Dichtungstyp |
|------------|---------------|-----------|-------------|
| SeaStar/Dometic | HA5430 | VG 15 | NBR |
| Vetus | HF15 | VG 15 | NBR |
| Ultraflex | OL150 | VG 15 | NBR |
| Kobelt | Dexron III (bestimmte Modelle) | ATF | Viton |
| Kobelt | ISO VG 32 (andere Modelle) | VG 32 | NBR |
| Jefa | ISO VG 15–22 | VG 15–22 | NBR/PTFE |
| Lewmar | ISO VG 15 | VG 15 | NBR |

### 10.5 Notfall-Checkliste: Steuerungsausfall auf See

```
□ 1. RUHE BEWAHREN
□ 2. Geschwindigkeit reduzieren (Motor drosseln / Segel bergen)
□ 3. Notpinne aufsetzen (Zugang: __________________)
□ 4. Besatzung informieren
□ 5. Seeraum sichern (Position, Verkehr)
□ 6. Ursache diagnostizieren
□ 7. Provisorische Reparatur versuchen
□ 8. Wenn Reparatur nicht möglich:
   □ 8a. Position festhalten
   □ 8b. Nächster sicherer Hafen bestimmen
   □ 8c. Ggf. Seenotruf (Mayday/Pan-Pan)
□ 9. Unter Notsteuerung nächsten Hafen anlaufen
□ 10. Vorfall dokumentieren (Logbuch)
```

### 10.6 Wartungsplan Jahresübersicht

| Monat | Seilzug | Hydraulik | Alle |
|-------|---------|----------|------|
| Jan | — | Frostschutz prüfen | — |
| Mrz | Seile prüfen | Ölstand prüfen | Saisonstart-Check |
| Apr | Spannung prüfen | Leitungen prüfen | Ruderlager prüfen |
| Jun | Sichtprüfung | Ölstand prüfen | — |
| Aug | Spannung prüfen | Anschlüsse prüfen | Ruderbewuchs |
| Sep | Sichtprüfung | Ölstand prüfen | — |
| Okt | Rollen schmieren | Druck prüfen | Saisonende-Check |
| Nov | Seile fetten | Ölstand max. | Winterlagerung |

---

## 11. ANHANG A–H — Fallstudien

### ANHANG A: Seilzugriss auf Atlantiküberquerung — Hallberg-Rassy 42

**Boot:** Hallberg-Rassy 42 (Baujahr 2008), Ketten-Seilzug-Steuerung (Whitlock Cobra 50)
**Situation:** Tag 14 der Atlantiküberquerung, 850 nm westlich Kanaren, Wind NE 25 kn, See 2–3 m
**Vorfall:** Backbord-Steuerseil reißt beim Halsen

**Ursache:**
- Steuerseil ∅4 mm, 7×19, 316 SS, Alter: 9 Jahre (1 Jahr über empfohlener Lebensdauer)
- Bruchstelle an Umlenkrolle unter dem Cockpitboden
- Ermüdungsbruch durch Biegewechselbelastung
- 3 Litzenbrüche bei letzter Inspektion dokumentiert, aber nicht gehandelt

**Sofortmaßnahme:**
1. Notpinne aufgesetzt (3 Minuten nach Ausfall)
2. Segel geborgen (nur Fock)
3. Gerissenes Seil gesichert

**Provisorische Reparatur:**
- Seilende mit Bulldog-Klemmen (3 Stück) provisorisch verbunden
- Reduzierter Seilquerschnitt → nur für moderate Bedingungen nutzbar
- Backup: Notpinne permanent griffbereit

**Fahrt:** 1.200 nm unter provisorischer Steuerung + Notpinne nach Barbados
**Reparatur im Hafen:** Beide Steuerseile erneuert (∅5 mm statt ∅4 mm), alle Umlenkrollen geprüft und zwei erneuert

**Lessons Learned:**
- Steuerseile NICHT über empfohlene Lebensdauer hinaus nutzen
- Bei 3 Litzenbrüchen SOFORT tauschen
- Bulldog-Klemmen als Notfallmaterial mitführen (min. 6 Stück, passend zur Seilstärke)
- Zweites Seilset als Ersatzteil auf Langfahrt mitführen

**AYDI-Bewertung:** Confidence measured, Fehlerkategorie: Wartungsversäumnis, Schweregrad: HOCH

### ANHANG B: Hydraulikleck auf Nordsee-Überführung — Bavaria 46

**Boot:** Bavaria 46 (Baujahr 2015), Hydraulische Steuerung (Jefa HSC-12)
**Situation:** Überführung Kiel → Ijmuiden, Deutsche Bucht, Wind W 30 kn, See 2–3 m, Nacht
**Vorfall:** Steuerung wird zunehmend schwammig über 2 Stunden

**Ursache:**
- Hydraulikschlauch (SAE J1942, 3/8") an Steuerzylinder-Anschluss undicht
- O-Ring im JIC-Anschluss verhärtet (Alter: 7 Jahre, Material: NBR)
- Langsamer Ölverlust: ca. 50 ml/Stunde
- Lufteinsaugung an der undichten Stelle

**Diagnoseschritte (auf See):**
1. Schwammige Steuerung bemerkt
2. Ölstand im Reservoir: 40 % unter Minimum
3. Sichtprüfung: Ölfilm am Steuerzylinder-Anschluss

**Sofortmaßnahme:**
1. Anschluss mit Bordmitteln nachgezogen (Gabelschlüssel 19 mm)
2. Hydrauliköl nachgefüllt (500 ml Reserveöl an Bord)
3. System entlüftet (10 Minuten Lock-to-Lock drehen)
4. Alle 30 Minuten Ölstand kontrolliert

**Ergebnis:** Leck stark reduziert (Tropfenweise), Fahrt fortgesetzt, Reparatur in Ijmuiden
**Reparatur:** Alle O-Ringe im System erneuert (8 Stück), Hydrauliköl gewechselt

**Lessons Learned:**
- Mindestens 1 Liter Reserveöl mitführen (gleicher Typ!)
- O-Ringe haben begrenzte Lebensdauer (5–8 Jahre bei NBR)
- Gabelschlüssel in der richtigen Größe griffbereit haben
- Regelmäßige Ölstandskontrolle (monatlich)

**AYDI-Bewertung:** Confidence measured, Fehlerkategorie: Alterung, Schweregrad: MITTEL

### ANHANG C: Ruderlagerversagen — Najad 440

**Boot:** Najad 440 (Baujahr 2003), Skeg-Ruder, Jefa-Ruderlager
**Situation:** Mittelmeer-Kreuzfahrt, 3. Saison nach letzter Lagerinspektion
**Vorfall:** Zunehmend klopfendes Geräusch am Heck, Spiel am Ruder

**Ursache:**
- Unteres Ruderlager (Skeg) verschlissen — Delrin-Buchse abgenutzt
- Ursache des vorzeitigen Verschleißes: Sand-Eintrag durch defekte Dichtung
- Normaler Verschleiß wäre nach 15+ Jahren zu erwarten, trat hier nach 10 Jahren ein

**Diagnoseschritte:**
1. Taucher: Ruder seitlich belastet → deutliches Spiel am Skeg-Lager
2. Oberes Lager (Koker): kein Spiel → nur unteres Lager betroffen
3. Boot aus dem Wasser: Ruder ausgebaut → Delrin-Buchse sichtbar oval verschlissen

**Reparatur:**
1. Ruder ausgebaut (Skeg-Bolzen, Kokerverbindung)
2. Alte Buchse ausgepresst
3. Neue PTFE/GFK-Buchse (Jefa-Original) eingepresst
4. Schaftoberfläche geprüft (leichte Riefen → geschliffen, poliert)
5. Neue Dichtungssätze oben und unten
6. Ruder eingebaut, Spiel kontrolliert

**Kosten:** Material ca. €450, Arbeit ca. €1.800 (3 Werft-Tage inkl. Kranen)

**AYDI-Bewertung:** Confidence measured, Fehlerkategorie: Verschleiß + Dichtungsdefekt, Schweregrad: MITTEL

### ANHANG D: Zahnstangensteuerung — Kabelbruch bei Gleiter

**Boot:** Bayliner VR6 (Baujahr 2018), 200 PS Mercury Außenborder, Ultraflex T-71FC Zahnstangensteuerung
**Situation:** Freizeitfahrt auf Bodensee, Gleitfahrt ca. 30 kn
**Vorfall:** Plötzlicher Steuerverlust bei Kurvenfahrt

> ⚠️ **ZU PRÜFEN (Audit):** Motorleistung 200 PS vs. Ultraflex T-71FC max. 150 PS (Einzelmotor) laut Abschnitt 4.5.1 — Steuerung unter der Motornennleistung betrieben (sicherheitsrelevant; vermutlich war die Baureihe T-85 mit max. 300 PS gemeint). Richtung nicht zweifelsfrei belegbar, daher nicht korrigiert. Confidence measured → estimated (unverifiziert).

**Ursache:**
- Steuerkabel M66 gebrochen — Stahlkern durchtrennt
- Bruchstelle: Kabeldurchführung durch Transom (scharfe Kante am Bohrloch)
- Scheuerbelastung über 4 Saisons hat den Kabelmantel und dann den Kern zerstört

**Sofortmaßnahme:**
1. Gas wegnehmen (sofort!)
2. Not-Kill-Switch gezogen (Motorstop)
3. Boot mit Langsamfahrt und Gewichtsverlagerung in den Hafen manövriert

**Reparatur:**
- Neues Steuerkabel M66 (korrekte Länge)
- Transom-Durchführung mit Nylon-Buchse versehen (Scheuerschutz)
- Kabelführung geprüft und optimiert (Biegeradien)

**Lessons Learned:**
- Kabeldurchführungen IMMER mit Scheuerschutz versehen
- Steuerkabel bei jährlicher Inspektion auf Scheuerstellen prüfen
- Bei Gleitbooten höhere mechanische Belastung durch Stöße

**AYDI-Bewertung:** Confidence documented, Fehlerkategorie: Installationsmangel, Schweregrad: HOCH

### ANHANG E: Elektrohydraulische Steuerung — Sensorausfall auf Motoryacht

**Boot:** Princess 62 (Baujahr 2012), Elektrohydraulische Steuerung, 2× Ruderzylinder
**Situation:** Einlaufmanöver Hafen Palma de Mallorca, querab anströmender Wind 15 kn
**Vorfall:** Steuerung fällt in „Notbetrieb" — Ruderbewegung langsam und unsensibel

**Ursache:**
- Ruderlage-Sensor (Potentiometer, am Steuerbord-Ruderschaft) ausgefallen
- Steuercomputer (ECU) hat auf Rückfall-Modus geschaltet (reduzierte Leistung)
- Potentiometer-Schleifer durch Feuchtigkeit korrodiert

**Sofortmaßnahme:**
1. Hafenmanöver unter Notbetrieb fortgesetzt (langsam, mit Bugstrahlruder)
2. Sicher angelegt
3. Servicetechniker gerufen

**Reparatur:**
- Ruderlage-Sensor (beide Seiten) durch berührungslose Sensoren ersetzt (Hall-Effekt)
- Kabelverbindungen auf Feuchtigkeitsschutz geprüft
- ECU-Firmware aktualisiert

**Kosten:** Material ca. €800 (2× Sensor), Arbeit ca. €600

**AYDI-Bewertung:** Confidence documented, Fehlerkategorie: Bauteilausfall (Umwelteinfluss), Schweregrad: MITTEL

### ANHANG F: Ruderblattabriss — Beneteau Oceanis 45

**Boot:** Beneteau Oceanis 45 (Baujahr 2013), Zwillingsruder (Spatenruder)
**Situation:** Mittelmeer-Kreuzfahrt bei Mistral, 35 kn Wind, 3–4 m See
**Vorfall:** Backbord-Ruderblatt bricht am Schaftansatz ab

**Ursache:**
- Ermüdungsriss an der Schaft-Ruderblatt-Verbindung (GFK-Edelstahl-Übergang)
- Vorschädigung durch Grundberührung 2 Saisons zuvor (wurde visuell inspiziert, aber nicht per Ultraschall)
- Wassereinbruch in den Ruderblatt-Kern (Klopftest hätte erhöhtes Gewicht gezeigt)

**Sofortmaßnahme:**
1. Steuerbord-Ruder funktionsfähig → eingeschränkte Manövrierfähigkeit
2. Geschwindigkeit reduziert
3. Nächsten Hafen (Port Camargue) angelaufen
4. Bruchstelle am Koker gesichert (kein weiterer Wassereinbruch)

**Reparatur:**
- Neues Ruderblatt (Werft-Sonderanfertigung): €4.500
- Neuer Ruderschaft (Aquamet 22, ∅40 mm): €1.200
- Neue Lager und Dichtungen: €350
- Einbau und Ausrichtung: €2.000
- Gesamtkosten: ca. €8.050

**Lessons Learned:**
- Nach JEDER Grundberührung: Ultraschall-Prüfung des Ruderschafts
- Jährlich: Klopftest am Ruderblatt (Gewichtsveränderung → Wassereinbruch)
- Beneteau Oceanis 40–50: Bekanntes Problem mit Schaft-Blatt-Verbindung — Inspektionsintervall verkürzen

**AYDI-Bewertung:** Confidence measured (Survey + Schadensanalyse), Fehlerkategorie: Vorschädigung + Materialermüdung, Schweregrad: KRITISCH

### ANHANG G: Korrosion am Ruderschaft — Ältere Swan 48

**Boot:** Nautor Swan 48 (Baujahr 1995), Spatenruder, Schaftmaterial: Edelstahl 316
**Situation:** Routinemäßige 5-Jahres-Inspektion durch Surveyor
**Befund:** Pitting-Korrosion am Ruderschaft im Bereich des unteren Lagers

**Ursache:**
- Spaltkorrosion im Bereich des Lagersitzes (Edelstahl 316 in Sauerstoffarmem Spalt)
- Fehlende galvanische Trennung zwischen Edelstahl-Schaft und Bronze-Skeg-Buchse
- Opferanode am Ruder verbraucht (nicht erneuert)

**Befund:**
- Pitting-Tiefe: max. 0,8 mm (Ultraschallmessung)
- Schaftdurchmesser: Sollwert 45 mm, Istwert 43,4 mm an der dünnsten Stelle
- Festigkeitsreduktion: ca. 12 % → noch im sicheren Bereich, aber Handlungsbedarf

**Maßnahmen:**
1. Schaft ausgebaut, Pitting-Stellen geschliffen und poliert
2. Neue PTFE/GFK-Lagerbuchse (galvanische Trennung)
3. Neue Zink-Opferanode (0,5 kg) am Ruder
4. Kontrollintervall auf 2 Jahre verkürzt
5. Langfristig: Schaftersatz durch Aquamet 22 empfohlen

**Kosten:** Inspektion + Reparatur: ca. €3.500

**AYDI-Bewertung:** Confidence measured (Ultraschall-Dickenmessung), Fehlerkategorie: Korrosion, Schweregrad: MITTEL (erhöht auf HOCH ohne Maßnahme)

### ANHANG H: Autopilot-Nachrüstung — Contest 42CS

**Boot:** Contest 42CS (Baujahr 2019), Jefa Kettensteuerung, Nachrüstung Raymarine Evolution Autopilot
**Situation:** Autopilot-Integration in bestehende mechanische Steuerung
**Ziel:** Hydraulischer Autopilot-Antrieb parallel zur Kettensteuerung

**Lösung:**
1. Hydraulischer Steuerzylinder (Jefa, passend zum Tillerarm)
2. Raymarine EV-200 Sail Evolution Autopilot
3. Hydraulikpumpe (Typ 2, für Ruder-Drehmoment bis 1.000 Nm)
4. Ruderlage-Sensor (lineares Potentiometer am Quadrant)
5. Bypass-Ventil (manuell/AP umschaltbar)
6. Hydraulikleitungen (Nylon, 3/8", 2× 3 m)
7. Ölreservoir (250 ml)

**Installation:**
- Zylinder am Tillerarm montiert (zusätzlicher Bolzen)
- Pumpe in Backskiste unter Cockpitboden
- Leitungen durch vorhandene Kabeldurchführungen
- Ruderlage-Sensor am Quadrant
- Entlüftung: 45 Minuten
- Kalibrierung: 30 Minuten (Sea Trial)

**Kosten:**
- Autopilot (EV-200 Sail + Display): €2.800
- Hydraulik-Kit (Pumpe + Zylinder + Leitungen): €1.400
- Ruderlage-Sensor: €180
- Installation (Werft): €1.200
- Gesamt: ca. €5.580

**Ergebnis:** Autopilot arbeitet einwandfrei parallel zur manuellen Steuerung. Bypass-Ventil ermöglicht sofortige Umschaltung. Kein spürbarer Einfluss auf das Steuergefühl im manuellen Betrieb.

**AYDI-Bewertung:** Confidence measured, Kategorie: Nachrüstung, Schweregrad: n/a (Verbesserung)

---

## 12. ANHANG I–R — Pydantic v2 Modelle

### ANHANG I: Basis-Modelle

```python
"""
AYDI Steering System Models — Pydantic v2
Module: 20_01 Steueranlagen Grundlagen

All models use Pydantic v2 with model_config = {"from_attributes": True}.
NEVER use class Config — always model_config dict.
German UX text, English code. Units: mm, Nm, bar, N.
"""

from __future__ import annotations

from datetime import date, datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, field_validator


# ── Enums ──────────────────────────────────────────────────────────────

class SteeringType(str, Enum):
    """Type of steering system."""
    WIRE_ROPE = "wire_rope"
    CHAIN = "chain"
    CHAIN_WIRE = "chain_wire"
    RACK_AND_PINION = "rack_and_pinion"
    HYDRAULIC_MANUAL = "hydraulic_manual"
    HYDRAULIC_POWER = "hydraulic_power"
    ELECTROHYDRAULIC = "electrohydraulic"
    ELECTROMECHANICAL = "electromechanical"
    FLY_BY_WIRE = "fly_by_wire"
    TILLER = "tiller"


class RudderType(str, Enum):
    """Type of rudder configuration."""
    SPADE = "spade"
    SKEG_HUNG = "skeg_hung"
    FULL_KEEL = "full_keel"
    TWIN_SPADE = "twin_spade"
    TWIN_SKEG = "twin_skeg"
    FLAP = "flap"


class RudderProfile(str, Enum):
    """Rudder blade profile type."""
    NACA_0012 = "naca_0012"
    NACA_0015 = "naca_0015"
    NACA_0018 = "naca_0018"
    FLAT_PLATE = "flat_plate"
    GOETTINGEN = "goettingen"
    CUSTOM = "custom"


class ShaftMaterial(str, Enum):
    """Material of the rudder stock."""
    STAINLESS_316L = "ss_316l"
    AQUAMET_22 = "aquamet_22"
    NITRONIC_50 = "nitronic_50"
    BRONZE = "bronze"
    CARBON_STEEL = "carbon_steel"


class BearingMaterial(str, Enum):
    """Material of the rudder bearing."""
    PTFE_GFK = "ptfe_gfk"
    DELRIN = "delrin"
    BRONZE = "bronze"
    RUBBER_CUTLESS = "rubber_cutless"


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


class FeedbackType(str, Enum):
    """Type of steering feedback."""
    NFB = "no_feedback"
    SSB = "safe_steering_back"
    FB = "full_feedback"


class Severity(str, Enum):
    """Severity classification for findings."""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


# ── Base Models ────────────────────────────────────────────────────────

class SteeringSystemBase(BaseModel):
    """Base model for a yacht steering system."""

    model_config = {"from_attributes": True}

    boat_name: Optional[str] = Field(None, description="Name des Bootes")
    boat_length_m: float = Field(..., gt=0, le=100, description="Bootslänge in Metern (LH)")
    boat_beam_m: Optional[float] = Field(None, gt=0, le=20, description="Bootsbreite in Metern")
    displacement_kg: Optional[float] = Field(None, gt=0, description="Verdrängung in kg")
    boat_type: str = Field(..., description="Bootstyp: sailboat, motorboat, catamaran, etc.")
    steering_type: SteeringType = Field(..., description="Typ der Steueranlage")
    rudder_type: RudderType = Field(..., description="Typ des Ruders")
    year_built: Optional[int] = Field(None, ge=1900, le=2030, description="Baujahr")
    manufacturer: Optional[str] = Field(None, description="Hersteller der Steueranlage")
    model: Optional[str] = Field(None, description="Modellbezeichnung der Steueranlage")


class RudderSpecification(BaseModel):
    """Detailed rudder specification."""

    model_config = {"from_attributes": True}

    rudder_type: RudderType = Field(..., description="Rudertyp")
    rudder_count: int = Field(1, ge=1, le=4, description="Anzahl Ruder")
    rudder_area_m2: Optional[float] = Field(None, gt=0, le=5.0, description="Ruderfläche in m²")
    rudder_span_mm: Optional[float] = Field(None, gt=0, description="Ruderhöhe (Span) in mm")
    rudder_chord_mm: Optional[float] = Field(None, gt=0, description="Rudertiefe (Chord) in mm")
    aspect_ratio: Optional[float] = Field(None, gt=0, le=10, description="Aspektverhältnis (Span²/Area)")
    profile: RudderProfile = Field(RudderProfile.NACA_0015, description="Ruderprofil")
    profile_thickness_pct: Optional[float] = Field(None, gt=0, le=30, description="Profildicke in % der Chord")
    balance_pct: Optional[float] = Field(None, ge=0, le=45, description="Balancierung in % der Chord")
    max_rudder_angle_deg: float = Field(35.0, ge=15, le=60, description="Max. Ruderausschlag in Grad")

    @field_validator("balance_pct")
    @classmethod
    def warn_overbalanced(cls, v: Optional[float]) -> Optional[float]:
        if v is not None and v > 35:
            raise ValueError(
                "Balancierung > 35 % ist überbalanciert und gefährlich. "
                "Ruder kann unkontrolliert ausschlagen."
            )
        return v


class RudderStockSpecification(BaseModel):
    """Rudder stock (shaft) specification."""

    model_config = {"from_attributes": True}

    material: ShaftMaterial = Field(..., description="Schaftmaterial")
    diameter_mm: float = Field(..., gt=0, le=200, description="Schaftdurchmesser in mm")
    length_mm: Optional[float] = Field(None, gt=0, description="Schaftlänge in mm")
    bearing_material_upper: BearingMaterial = Field(
        BearingMaterial.PTFE_GFK, description="Material oberes Lager"
    )
    bearing_material_lower: Optional[BearingMaterial] = Field(
        None, description="Material unteres Lager (nur bei Skeg-Ruder)"
    )
    seal_type: Optional[str] = Field(None, description="Dichtungstyp: lip_seal, pss, packing")
    last_inspection_date: Optional[date] = Field(None, description="Letzte Inspektion")
```

### ANHANG J: Kraft- und Drehmoment-Modelle

```python
class RudderForceCalculation(BaseModel):
    """Calculation of rudder forces and torques."""

    model_config = {"from_attributes": True}

    # Input parameters
    rudder_area_m2: float = Field(..., gt=0, description="Ruderfläche in m²")
    boat_speed_kn: float = Field(..., ge=0, description="Bootsgeschwindigkeit in Knoten")
    rudder_angle_deg: float = Field(..., ge=0, le=60, description="Ruderwinkel in Grad")
    water_density_kg_m3: float = Field(1025.0, description="Wasserdichte in kg/m³")

    # Rudder geometry
    chord_mm: float = Field(..., gt=0, description="Rudertiefe (Chord) in mm")
    balance_pct: float = Field(20.0, ge=0, le=45, description="Balancierung in %")
    shaft_position_pct: Optional[float] = Field(
        None, ge=0, le=50,
        description="Schaftposition in % hinter Vorderkante"
    )

    # Calculated results
    rudder_force_n: Optional[float] = Field(None, ge=0, description="Ruderkraft (Querkraft) in N")
    rudder_torque_nm: Optional[float] = Field(None, description="Drehmoment am Schaft in Nm")
    center_of_pressure_pct: Optional[float] = Field(
        None, description="Druckmittelpunkt in % der Chord"
    )
    lever_arm_mm: Optional[float] = Field(None, description="Hebelarm in mm")
    confidence: ConfidenceLevel = Field(
        ConfidenceLevel.CALCULATED, description="Confidence-Level"
    )

    def calculate(self) -> "RudderForceCalculation":
        """Calculate rudder force and torque using simplified formula."""
        import math

        v_ms = self.boat_speed_kn * 0.5144  # kn to m/s
        alpha_rad = math.radians(self.rudder_angle_deg)

        # Simplified rudder force (Larsson/Eliasson)
        self.rudder_force_n = 580.0 * self.rudder_area_m2 * v_ms ** 2 * math.sin(alpha_rad)

        # Center of pressure (moves aft with angle)
        # Linear approximation: 0.25 at 0°, 0.38 at 35°
        self.center_of_pressure_pct = 25.0 + (self.rudder_angle_deg / 35.0) * 13.0
        self.center_of_pressure_pct = min(self.center_of_pressure_pct, 42.0)

        # Shaft position
        shaft_pos = self.shaft_position_pct or self.balance_pct
        chord_m = self.chord_mm / 1000.0

        cp_m = (self.center_of_pressure_pct / 100.0) * chord_m
        shaft_m = (shaft_pos / 100.0) * chord_m
        self.lever_arm_mm = (cp_m - shaft_m) * 1000.0

        # Torque
        self.rudder_torque_nm = self.rudder_force_n * (cp_m - shaft_m)

        return self


class SteeringRatioCalculation(BaseModel):
    """Calculation of steering ratios and helm force."""

    model_config = {"from_attributes": True}

    # Input: mechanical parameters
    wheel_diameter_mm: float = Field(..., gt=0, description="Steuerrad-Durchmesser in mm")
    lock_to_lock_turns: float = Field(..., gt=0, le=12, description="Umdrehungen Lock-to-Lock")
    max_rudder_angle_deg: float = Field(35.0, description="Max. Ruderwinkel in Grad")
    rudder_torque_nm: float = Field(..., description="Max. Ruderdrehmoment in Nm")
    transmission_efficiency: float = Field(
        0.75, gt=0, le=1.0, description="Wirkungsgrad der Übertragung (0–1)"
    )

    # Calculated results
    overall_ratio: Optional[float] = Field(None, description="Gesamtübersetzung")
    helm_force_n: Optional[float] = Field(None, description="Handkraft an der Radfelge in N")
    iso_compliant: Optional[bool] = Field(None, description="ISO 8848 konform (<15 N normal)")
    confidence: ConfidenceLevel = Field(ConfidenceLevel.CALCULATED)

    def calculate(self) -> "SteeringRatioCalculation":
        """Calculate steering ratio and resulting helm force."""
        import math

        # Overall ratio
        total_rudder_travel_deg = 2 * self.max_rudder_angle_deg
        self.overall_ratio = (self.lock_to_lock_turns * 360.0) / total_rudder_travel_deg

        # Helm force
        wheel_radius_m = (self.wheel_diameter_mm / 2.0) / 1000.0
        if wheel_radius_m > 0 and self.overall_ratio > 0 and self.transmission_efficiency > 0:
            self.helm_force_n = self.rudder_torque_nm / (
                wheel_radius_m * self.overall_ratio * self.transmission_efficiency
            )
        else:
            self.helm_force_n = None

        # ISO compliance
        if self.helm_force_n is not None:
            self.iso_compliant = self.helm_force_n <= 15.0

        return self
```

### ANHANG K: Komponentenmodelle

```python
class WireRopeSpec(BaseModel):
    """Wire rope specification for cable steering."""

    model_config = {"from_attributes": True}

    diameter_mm: float = Field(..., gt=0, le=12, description="Seildurchmesser in mm")
    construction: str = Field("7x19", description="Seilkonstruktion (z.B. 7x19, 6x19)")
    material: str = Field("ss_316", description="Material: ss_316, ss_304, galvanized")
    breaking_load_n: Optional[float] = Field(None, gt=0, description="Bruchlast in N")
    working_load_n: Optional[float] = Field(None, gt=0, description="Arbeitslast in N (BL/SF)")
    safety_factor: float = Field(4.0, ge=3.0, le=8.0, description="Sicherheitsfaktor")
    length_m: Optional[float] = Field(None, gt=0, description="Gesamtlänge pro Seite in m")
    age_years: Optional[float] = Field(None, ge=0, description="Alter in Jahren")
    broken_strands_per_30cm: int = Field(0, ge=0, description="Litzenbrüche pro 30 cm")
    condition: Optional[str] = Field(None, description="Zustand: good, wear, replace, critical")

    @field_validator("condition", mode="before")
    @classmethod
    def assess_condition(cls, v, info):
        if v is not None:
            return v
        data = info.data
        broken = data.get("broken_strands_per_30cm", 0)
        age = data.get("age_years")
        if broken > 5:
            return "critical"
        if broken >= 3 or (age is not None and age > 8):
            return "replace"
        if broken >= 1 or (age is not None and age > 5):
            return "wear"
        return "good"


class QuadrantSpec(BaseModel):
    """Steering quadrant specification."""

    model_config = {"from_attributes": True}

    material: str = Field("aluminium", description="Material: aluminium, stainless_steel")
    radius_mm: float = Field(..., gt=0, le=400, description="Quadrant-Radius in mm")
    arc_deg: float = Field(90.0, ge=60, le=180, description="Bogenlänge in Grad")
    shaft_diameter_mm: float = Field(..., gt=0, description="Schaftdurchmesser-Aufnahme in mm")
    connection_type: str = Field("taper_keyway", description="Verbindungstyp: taper_keyway, flange, clamp")


class HydraulicHelmPump(BaseModel):
    """Hydraulic helm pump specification."""

    model_config = {"from_attributes": True}

    manufacturer: str = Field(..., description="Hersteller")
    model: str = Field(..., description="Modellbezeichnung")
    displacement_cc_per_rev: float = Field(
        ..., gt=0, le=200, description="Fördervolumen in cm³/Umdrehung"
    )
    max_pressure_bar: float = Field(..., gt=0, le=400, description="Max. Systemdruck in bar")
    lock_to_lock_turns: Optional[float] = Field(
        None, gt=0, le=12, description="Umdrehungen Lock-to-Lock"
    )
    port_size: Optional[str] = Field(None, description="Anschlussgröße: 3/8_jic, 1/2_jic, etc.")
    mounting: Optional[str] = Field(None, description="Montage: pedestal, bulkhead, console")


class HydraulicCylinder(BaseModel):
    """Hydraulic steering cylinder specification."""

    model_config = {"from_attributes": True}

    manufacturer: str = Field(..., description="Hersteller")
    model: str = Field(..., description="Modellbezeichnung")
    cylinder_type: str = Field(..., description="Typ: linear, rotary")
    bore_mm: Optional[float] = Field(None, gt=0, description="Kolbendurchmesser in mm (linear)")
    stroke_mm: Optional[float] = Field(None, gt=0, description="Hub in mm (linear)")
    max_torque_nm: Optional[float] = Field(None, gt=0, description="Max. Drehmoment in Nm (rotary)")
    max_angle_deg: Optional[float] = Field(None, description="Max. Drehwinkel in Grad (rotary)")
    max_pressure_bar: float = Field(..., gt=0, description="Max. Druck in bar")
    max_force_n: Optional[float] = Field(None, gt=0, description="Max. Zylinderkraft in N (linear)")
    shaft_diameter_mm: Optional[float] = Field(
        None, gt=0, description="Schaftdurchmesser-Aufnahme in mm (rotary)"
    )
    port_size: Optional[str] = Field(None, description="Anschlussgröße")


class HydraulicFluid(BaseModel):
    """Hydraulic fluid specification."""

    model_config = {"from_attributes": True}

    product_name: str = Field(..., description="Produktbezeichnung")
    iso_viscosity_grade: int = Field(..., description="ISO VG Klasse (z.B. 15, 22, 32)")
    viscosity_index: Optional[int] = Field(None, description="Viskositätsindex")
    temp_range_min_c: Optional[float] = Field(None, description="Min. Betriebstemperatur in °C")
    temp_range_max_c: Optional[float] = Field(None, description="Max. Betriebstemperatur in °C")
    seal_compatibility: list[str] = Field(
        default_factory=list, description="Kompatible Dichtungsmaterialien"
    )
    compatible_with: list[str] = Field(
        default_factory=list, description="Kompatible Steueranlagen-Hersteller"
    )
```

### ANHANG L: Befund- und Diagnosemodelle

```python
class SteeringFinding(BaseModel):
    """A single finding from steering system inspection."""

    model_config = {"from_attributes": True}

    finding_id: str = Field(..., description="Eindeutige Befund-ID")
    category: str = Field(..., description="Fehlerkategorie aus Fehlerbild-Atlas (6.1–6.12)")
    title_de: str = Field(..., description="Befundtitel (Deutsch)")
    title_en: Optional[str] = Field(None, description="Finding title (English)")
    description_de: str = Field(..., description="Befundbeschreibung (Deutsch)")
    severity: Severity = Field(..., description="Schweregrad")
    location: Optional[str] = Field(None, description="Ort am Boot (z.B. 'Steuerkoker', 'Quadrant Bb')")
    component: Optional[str] = Field(
        None, description="Betroffene Komponente (z.B. 'Seilzug Bb', 'Helm-Pumpe')"
    )
    confidence: ConfidenceLevel = Field(..., description="Confidence-Level der Bewertung")
    recommendation_de: str = Field(..., description="Empfehlung (Deutsch)")
    estimated_cost_eur: Optional[float] = Field(None, ge=0, description="Geschätzte Kosten in EUR")
    urgency_days: Optional[int] = Field(
        None, ge=0,
        description="Empfohlene Handlungsfrist in Tagen (0=sofort, None=kein Zeitdruck)"
    )
    photos: list[str] = Field(default_factory=list, description="Foto-Referenzen")
    created_at: datetime = Field(default_factory=datetime.utcnow)


class SteeringInspectionReport(BaseModel):
    """Complete steering system inspection report."""

    model_config = {"from_attributes": True}

    report_id: str = Field(..., description="Report-ID")
    boat_name: str = Field(..., description="Bootsname")
    boat_length_m: float = Field(..., gt=0)
    inspection_date: date = Field(..., description="Inspektionsdatum")
    inspector: Optional[str] = Field(None, description="Prüfer/Surveyor")
    steering_system: SteeringSystemBase = Field(..., description="Steueranlagen-Beschreibung")
    rudder_spec: Optional[RudderSpecification] = Field(None, description="Ruder-Spezifikation")
    stock_spec: Optional[RudderStockSpecification] = Field(None, description="Ruderschaft-Spezifikation")
    findings: list[SteeringFinding] = Field(default_factory=list, description="Befunde")
    overall_condition: str = Field(
        ..., description="Gesamtzustand: excellent, good, fair, poor, critical"
    )
    overall_score: Optional[float] = Field(
        None, ge=0, le=100, description="AYDI-Gesamtscore (0–100)"
    )
    next_inspection_date: Optional[date] = Field(None, description="Nächste empfohlene Inspektion")
    notes_de: Optional[str] = Field(None, description="Anmerkungen (Deutsch)")
    confidence: ConfidenceLevel = Field(..., description="Gesamt-Confidence des Berichts")


class SteeringMaintenanceRecord(BaseModel):
    """Record of a steering system maintenance action."""

    model_config = {"from_attributes": True}

    record_id: str = Field(..., description="Wartungs-ID")
    boat_name: str = Field(...)
    maintenance_date: date = Field(...)
    performed_by: Optional[str] = Field(None, description="Ausführende Person/Werft")
    action_type: str = Field(
        ...,
        description="Art der Wartung: inspection, repair, replacement, overhaul, upgrade"
    )
    description_de: str = Field(..., description="Beschreibung der Maßnahme (Deutsch)")
    components_affected: list[str] = Field(
        default_factory=list, description="Betroffene Komponenten"
    )
    parts_replaced: list[str] = Field(
        default_factory=list, description="Ersetzte Teile"
    )
    cost_eur: Optional[float] = Field(None, ge=0, description="Kosten in EUR")
    next_due_date: Optional[date] = Field(None, description="Nächster Wartungstermin")
    notes: Optional[str] = Field(None, description="Anmerkungen")
```

### ANHANG M: Hersteller-Datenbankmodell

```python
class SteeringManufacturer(BaseModel):
    """Manufacturer database entry for steering systems."""

    model_config = {"from_attributes": True}

    manufacturer_id: str = Field(..., description="Eindeutige Hersteller-ID")
    name: str = Field(..., description="Herstellername")
    country: str = Field(..., description="Land (ISO 3166-1 alpha-2)")
    founded_year: Optional[int] = Field(None, ge=1800, description="Gründungsjahr")
    headquarters: Optional[str] = Field(None, description="Firmensitz")
    website: Optional[str] = Field(None, description="Website-URL")
    specialization: list[str] = Field(
        default_factory=list,
        description="Spezialisierung: sailboat, motorboat, superyacht, commercial"
    )
    steering_types: list[SteeringType] = Field(
        default_factory=list, description="Angebotene Steuerungstypen"
    )
    boat_size_range_m: tuple[float, float] = Field(
        ..., description="Bootsgrößenbereich (min, max) in Metern"
    )
    oem_clients: list[str] = Field(
        default_factory=list, description="OEM-Kunden (Werftliste)"
    )
    certifications: list[str] = Field(
        default_factory=list, description="Zertifizierungen (ISO, CE, etc.)"
    )
    price_segment: str = Field(
        ..., description="Preissegment: low, medium, high, premium"
    )
    notes_de: Optional[str] = Field(None, description="Anmerkungen (Deutsch)")


class SteeringProduct(BaseModel):
    """Specific steering product entry."""

    model_config = {"from_attributes": True}

    product_id: str = Field(..., description="Eindeutige Produkt-ID")
    manufacturer_id: str = Field(..., description="Hersteller-ID")
    manufacturer_name: str = Field(..., description="Herstellername")
    model_name: str = Field(..., description="Modellbezeichnung")
    product_type: str = Field(
        ...,
        description="Produkttyp: pedestal, helm_pump, cylinder, wheel, cable, quadrant, bearing"
    )
    steering_type: Optional[SteeringType] = Field(None, description="Steuerungstyp")
    boat_size_range_m: Optional[tuple[float, float]] = Field(
        None, description="Empfohlener Bootsgrößenbereich"
    )
    max_torque_nm: Optional[float] = Field(None, description="Max. Drehmoment in Nm")
    max_pressure_bar: Optional[float] = Field(None, description="Max. Druck in bar")
    displacement_cc: Optional[float] = Field(None, description="Fördervolumen in cm³/U")
    material: Optional[str] = Field(None, description="Hauptmaterial")
    weight_kg: Optional[float] = Field(None, ge=0, description="Gewicht in kg")
    price_eur: Optional[float] = Field(None, ge=0, description="Richtpreis in EUR")
    datasheet_url: Optional[str] = Field(None, description="Link zum Datenblatt")
    notes_de: Optional[str] = Field(None, description="Anmerkungen (Deutsch)")
```

### ANHANG N: Analyse- und Scoring-Modelle

```python
class SteeringAnalysisInput(BaseModel):
    """Input for AYDI steering system analysis."""

    model_config = {"from_attributes": True}

    boat_length_m: float = Field(..., gt=0, le=100)
    boat_beam_m: Optional[float] = Field(None, gt=0)
    displacement_kg: Optional[float] = Field(None, gt=0)
    boat_type: str = Field(...)
    max_speed_kn: Optional[float] = Field(None, gt=0, le=60)
    steering_type: Optional[SteeringType] = Field(None)
    rudder_type: Optional[RudderType] = Field(None)
    rudder_area_m2: Optional[float] = Field(None, gt=0)
    rudder_chord_mm: Optional[float] = Field(None, gt=0)
    rudder_balance_pct: Optional[float] = Field(None, ge=0, le=45)
    shaft_diameter_mm: Optional[float] = Field(None, gt=0)
    shaft_material: Optional[ShaftMaterial] = Field(None)
    bearing_material: Optional[BearingMaterial] = Field(None)
    system_age_years: Optional[float] = Field(None, ge=0)
    last_maintenance_date: Optional[date] = Field(None)
    autopilot_installed: Optional[bool] = Field(None)
    has_emergency_tiller: Optional[bool] = Field(None)
    photos: list[str] = Field(default_factory=list, description="Photo references for visual analysis")


class SteeringAnalysisResult(BaseModel):
    """Result of AYDI steering system analysis."""

    model_config = {"from_attributes": True}

    # Scores (0–100)
    overall_score: float = Field(..., ge=0, le=100, description="AYDI-Gesamtscore Steueranlage")
    dimensioning_score: float = Field(
        ..., ge=0, le=100, description="Score: Dimensionierung (Schaft, Ruder, Übersetzung)"
    )
    condition_score: float = Field(
        ..., ge=0, le=100, description="Score: Zustand (Verschleiß, Korrosion)"
    )
    safety_score: float = Field(
        ..., ge=0, le=100, description="Score: Sicherheit (Redundanz, Notsteuerung)"
    )
    maintenance_score: float = Field(
        ..., ge=0, le=100, description="Score: Wartungszustand"
    )

    # Calculated values
    estimated_rudder_torque_nm: Optional[float] = Field(
        None, description="Geschätztes max. Ruderdrehmoment in Nm"
    )
    estimated_helm_force_n: Optional[float] = Field(
        None, description="Geschätzte Handkraft am Steuerrad in N"
    )
    iso_8848_compliant: Optional[bool] = Field(
        None, description="ISO 8848 konform (Handkraft <15 N)"
    )
    shaft_adequately_sized: Optional[bool] = Field(
        None, description="Schaftdurchmesser ausreichend dimensioniert"
    )

    # Findings
    findings: list[SteeringFinding] = Field(
        default_factory=list, description="Befunde"
    )
    recommendations_de: list[str] = Field(
        default_factory=list, description="Empfehlungen (Deutsch)"
    )

    # Confidence
    confidence: ConfidenceLevel = Field(..., description="Gesamt-Confidence")
    data_completeness_pct: float = Field(
        ..., ge=0, le=100, description="Datenvollständigkeit in %"
    )

    # Metadata
    analysis_version: str = Field("1.0.0", description="Analyse-Modulversion")
    analysis_timestamp: datetime = Field(default_factory=datetime.utcnow)
```

### ANHANG O: Fehler-Atlas-Modelle

```python
class FaultPattern(BaseModel):
    """Fault pattern from the Fehlerbild-Atlas."""

    model_config = {"from_attributes": True}

    fault_id: str = Field(..., description="Fehler-ID (z.B. 'F6.1')")
    title_de: str = Field(..., description="Fehlertitel (Deutsch)")
    title_en: Optional[str] = Field(None, description="Fault title (English)")
    description_de: str = Field(..., description="Beschreibung (Deutsch)")
    symptoms: list[str] = Field(default_factory=list, description="Symptome (Deutsch)")
    causes: list[FaultCause] = Field(default_factory=list, description="Ursachen mit Wahrscheinlichkeit")
    affected_steering_types: list[SteeringType] = Field(
        default_factory=list, description="Betroffene Steuerungstypen"
    )
    severity: Severity = Field(..., description="Schweregrad")
    diagnostic_steps: list[str] = Field(
        default_factory=list, description="Diagnoseschritte"
    )
    remediation_steps: list[str] = Field(
        default_factory=list, description="Behebungsschritte"
    )
    prevention_measures: list[str] = Field(
        default_factory=list, description="Vorbeugende Maßnahmen"
    )
    estimated_repair_cost_eur: Optional[tuple[float, float]] = Field(
        None, description="Geschätzte Reparaturkosten (min, max) in EUR"
    )
    confidence: ConfidenceLevel = Field(...)


class FaultCause(BaseModel):
    """A single cause within a fault pattern."""

    model_config = {"from_attributes": True}

    rank: int = Field(..., ge=1, description="Rang nach Wahrscheinlichkeit")
    cause_de: str = Field(..., description="Ursache (Deutsch)")
    probability_pct: float = Field(..., ge=0, le=100, description="Wahrscheinlichkeit in %")
    affected_types: list[SteeringType] = Field(
        default_factory=list, description="Betroffene Steuerungstypen"
    )
```

### ANHANG P: Troubleshooting-Modelle

```python
class TroubleshootingNode(BaseModel):
    """A single node in a troubleshooting decision tree."""

    model_config = {"from_attributes": True}

    node_id: str = Field(..., description="Knoten-ID")
    question_de: str = Field(..., description="Frage oder Anweisung (Deutsch)")
    node_type: str = Field(
        ..., description="Knotentyp: question, action, result, branch"
    )
    yes_node_id: Optional[str] = Field(None, description="Nächster Knoten bei JA")
    no_node_id: Optional[str] = Field(None, description="Nächster Knoten bei NEIN")
    children: list[str] = Field(
        default_factory=list,
        description="Kind-Knoten-IDs (für Mehrfachverzweigung)"
    )
    action_de: Optional[str] = Field(None, description="Empfohlene Maßnahme (Deutsch)")
    severity: Optional[Severity] = Field(None, description="Schweregrad des Ergebnisses")


class TroubleshootingTree(BaseModel):
    """Complete troubleshooting decision tree."""

    model_config = {"from_attributes": True}

    tree_id: str = Field(..., description="Baum-ID (z.B. 'T7.1')")
    title_de: str = Field(..., description="Titel (Deutsch)")
    symptom_de: str = Field(..., description="Ausgangssymptom (Deutsch)")
    root_node_id: str = Field(..., description="Wurzel-Knoten-ID")
    nodes: list[TroubleshootingNode] = Field(
        default_factory=list, description="Alle Knoten des Baums"
    )
    applicable_steering_types: list[SteeringType] = Field(
        default_factory=list, description="Anwendbare Steuerungstypen"
    )
```

### ANHANG Q: Wartungsplanungs-Modelle

```python
class MaintenanceScheduleItem(BaseModel):
    """A single maintenance schedule item."""

    model_config = {"from_attributes": True}

    item_id: str = Field(..., description="Wartungspunkt-ID")
    task_de: str = Field(..., description="Wartungsaufgabe (Deutsch)")
    interval_months: Optional[int] = Field(
        None, ge=1, description="Intervall in Monaten"
    )
    interval_hours: Optional[int] = Field(
        None, ge=1, description="Intervall in Betriebsstunden"
    )
    applicable_types: list[SteeringType] = Field(
        default_factory=list, description="Anwendbare Steuerungstypen"
    )
    skill_level: str = Field(
        ..., description="Erforderliches Können: owner, technician, specialist"
    )
    estimated_duration_min: Optional[int] = Field(
        None, ge=0, description="Geschätzte Dauer in Minuten"
    )
    parts_needed: list[str] = Field(
        default_factory=list, description="Benötigte Teile/Materialien"
    )
    tools_needed: list[str] = Field(
        default_factory=list, description="Benötigtes Werkzeug"
    )
    reference_section: Optional[str] = Field(
        None, description="Referenz-Abschnitt in dieser Wissensdatei"
    )


class MaintenanceSchedule(BaseModel):
    """Complete maintenance schedule for a steering system."""

    model_config = {"from_attributes": True}

    schedule_id: str = Field(...)
    steering_type: SteeringType = Field(...)
    boat_length_m: float = Field(..., gt=0)
    items: list[MaintenanceScheduleItem] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    notes_de: Optional[str] = Field(None)
```

### ANHANG R: Schnellanalyse-Modelle (Level 1)

```python
class SteeringQuickAnalysisInput(BaseModel):
    """Input for Level 1 quick analysis (Schnellanalyse) — no login required."""

    model_config = {"from_attributes": True}

    boat_length_m: float = Field(..., gt=2, le=50, description="Bootslänge in Metern")
    boat_type: str = Field(
        ..., description="Bootstyp: sailboat, motorboat, catamaran, multihull"
    )
    steering_type: Optional[SteeringType] = Field(
        None, description="Steuerungstyp (wenn bekannt)"
    )
    rudder_type: Optional[RudderType] = Field(
        None, description="Rudertyp (wenn bekannt)"
    )
    system_age_years: Optional[float] = Field(
        None, ge=0, description="Alter der Steueranlage in Jahren"
    )
    reported_symptoms: list[str] = Field(
        default_factory=list,
        description="Vom Nutzer gemeldete Symptome (Deutsch oder Englisch)"
    )
    photos: list[str] = Field(
        default_factory=list,
        description="Hochgeladene Fotos (URLs oder Dateireferenzen)"
    )


class SteeringQuickAnalysisResult(BaseModel):
    """Result of Level 1 quick analysis."""

    model_config = {"from_attributes": True}

    # Estimated specifications (Level 1 — always estimated)
    estimated_steering_type: SteeringType = Field(
        ..., description="Geschätzter Steuerungstyp"
    )
    estimated_rudder_torque_nm: float = Field(
        ..., description="Geschätztes Ruderdrehmoment in Nm"
    )
    estimated_shaft_diameter_mm: float = Field(
        ..., description="Geschätzter Schaftdurchmesser in mm"
    )

    # Quick scores
    estimated_overall_score: float = Field(
        ..., ge=0, le=100, description="Geschätzter AYDI-Gesamtscore"
    )

    # Key findings (top 3)
    top_findings: list[SteeringFinding] = Field(
        default_factory=list, max_length=5,
        description="Wichtigste Befunde (max. 5)"
    )

    # Recommendations
    recommendations_de: list[str] = Field(
        default_factory=list, description="Empfehlungen (Deutsch)"
    )
    upgrade_to_level2_reasons: list[str] = Field(
        default_factory=list,
        description="Gründe für Upgrade auf Level 2 (Profi-Werkzeug)"
    )

    # Confidence — always 'estimated' for Level 1
    confidence: ConfidenceLevel = Field(
        ConfidenceLevel.ESTIMATED,
        description="Immer 'estimated' für Level 1"
    )
    data_completeness_pct: float = Field(
        ..., ge=0, le=100, description="Datenvollständigkeit in %"
    )

    # Metadata
    analysis_level: int = Field(1, description="Analyselevel (1=Schnellanalyse)")
    disclaimer_de: str = Field(
        default="Diese Schnellanalyse basiert auf geschätzten Werten und Durchschnittsdaten. "
        "Für eine zuverlässige Bewertung empfehlen wir die Profi-Analyse (Level 2) "
        "mit exakten Messdaten.",
        description="Haftungsausschluss"
    )
```

---

## Ergänzende Referenztabellen

### Tabelle R1: Vollständige Steuerungskompatibilitätsmatrix

| Steuerungstyp | Autopilot Hydraulisch | Autopilot Linear | Autopilot Rotary | Windfahne | Joystick | Zweitsteuerplatz |
|--------------|----------------------|-----------------|-----------------|----------|---------|-----------------|
| Pinne | — | ✅ (Tillerpilot) | — | ✅ | — | — |
| Seilzug | ✅ (sep. Zylinder) | ✅ (am Quadrant) | — | ✅ (über Pendel) | — | Aufwändig |
| Kette | ✅ (sep. Zylinder) | ✅ (am Quadrant) | — | ✅ (über Pendel) | — | Aufwändig |
| Zahnstange | — | — | — | — | — | — |
| Hydraulik manuell | ✅ (parallel) | — | ✅ | — | — | ✅ (2. Pumpe) |
| Elektrohydraulisch | ✅ (integriert) | — | ✅ | — | ✅ | ✅ (beliebig) |
| Fly-by-Wire | ✅ (integriert) | — | ✅ | — | ✅ | ✅ (beliebig) |

### Tabelle R2: Dichtungssysteme am Steuerkoker

| Dichtungstyp | Funktionsprinzip | Wartung | Lebensdauer | Kosten |
|-------------|-----------------|---------|-------------|--------|
| Stopfbuchse (Packung) | Komprimiertes Packungsmaterial um Schaft | Nachziehen alle 6–12 Monate | 3–5 Jahre (Packung) | €30–€80 |
| Lippendichtung | Elastomer-Lippe gleitet auf Schaftoberfläche | Keine (wartungsfrei) | 5–10 Jahre | €50–€150 |
| PSS (Pacific Seals) | Gleitring-Dichtung (Rotor + Stator) | Keine (wartungsfrei) | 10–20 Jahre | €200–€500 |
| Doppel-Lippendichtung + Fett | Zwei Lippen mit Fettfüllung dazwischen | Fett nachpressen 1×/Jahr | 8–15 Jahre | €100–€250 |
| O-Ring-Dichtung | Nur für geringe Drücke, nicht für Rotation | Nicht geeignet | n/a | n/a |

### Tabelle R3: Materialvergleich Ruderschäfte

| Eigenschaft | Edelstahl 316L | Aquamet 22 | Nitronic 50 | Bronze (Mn-Bronze) |
|-------------|---------------|-----------|------------|-------------------|
| Zugfestigkeit (MPa) | 485 | 862 | 827 | 450 |
| Streckgrenze (MPa) | 170 | 586 | 380 | 170 |
| Dauerfestigkeit in Seewasser (MPa) | 95 | 270 | 240 | 80 |
| Korrosionsbeständigkeit | Gut | Sehr gut | Sehr gut | Gut (aber galv. Probleme) |
| E-Modul (GPa) | 193 | 193 | 193 | 100 |
| Dichte (g/cm³) | 7,98 | 7,86 | 7,88 | 8,30 |
| Relative Kosten | 1,0× | 2,5× | 3,0× | 0,8× |
| Verfügbarkeit | Sehr gut | Gut (Fachhandel) | Eingeschränkt | Gut |
| Magnetisch | Leicht (nach Kaltverformung) | Nein | Nein | Nein |
| Empfehlung | Budget, Boote <14 m | Standard für Qualitätsyachten | Regatta, Superyacht | Historisch, Restaurierung |

### Tabelle R4: Steueranlagen-Checkliste für Yacht-Survey

```
STEUERANLAGEN-SURVEY CHECKLISTE
═══════════════════════════════════════════════════

Boot: _________________________  Datum: ___________
Surveyor: _____________________  Typ: _____________

A. STEUERRAD / PEDESTAL
□ Steuerrad sitzt fest, kein Spiel auf der Nabe
□ Pedestal-Befestigung fest (Bolzen, Mutter, Unterlegscheiben)
□ Pedestal-Gehäuse ohne Risse, Korrosion
□ Kompass-Aufnahme intakt (wenn vorhanden)
□ Motorgashebel leichtgängig (wenn vorhanden)
□ Steuerrad-Material: □ Edelstahl □ Alu □ Carbon □ Holz
□ Zustand Radgriff: □ Gut □ Verschlissen □ Lose

B. ÜBERTRAGUNG (SEILZUG/KETTE)
□ Seilzug: Zustand Seile (Litzenbrüche, Korrosion)
   Litzenbrüche pro 30 cm: ___ (>3 = Austausch)
□ Seilspannung korrekt (Daumenprobe)
□ Alle Umlenkrollen leichtgängig
□ Umlenkrollen-Befestigung fest
□ Kette: Zustand (Verschleiß, Korrosion, steife Glieder)
□ Kettenrad: Zahnprofil intakt
□ Quadrant-Befestigung fest (Konus, Keilnut, Mutter)
□ Seilbefestigung am Quadrant (Gabelbolzen, Splinte)
□ Rückholfedern vorhanden und funktionsfähig

C. HYDRAULIK (wenn vorhanden)
□ Ölstand im Reservoir
□ Ölfarbe und -zustand (klar = gut, trüb/dunkel = wechseln)
□ Alle Leitungsanschlüsse dicht
□ Schlauchzustand (Risse, Schwellungen, Alter)
□ Zylinder-Kolbenstange: Ölfilm? Korrosion?
□ Bypass-Ventil funktionsfähig
□ Helm-Pumpe leichtgängig
□ Druckabfalltest (10 min bei Volllast): ___ bar Verlust

D. RUDER UND RUDERLAGER
□ Ruderblatt: optischer Zustand (Risse, Dellen, Bewuchs)
□ Ruderblatt: Klopftest (hohl = Wassereinbruch)
□ Ruderlager oben: Spiel prüfen (Ruder seitlich belasten)
   Spiel: ___ mm (>0,5 mm = handeln)
□ Ruderlager unten (Skeg): Spiel prüfen
□ Ruderschaft: sichtbare Korrosion?
□ Steuerkoker: Wassereinbruch? Feuchtigkeit?
□ Steuerkoker-Dichtung: Zustand
□ Notpinne vorhanden und passend

E. ELEKTRISCH / AUTOPILOT
□ Autopilot-Integration: □ Hydraulisch □ Linear □ Keiner
□ Ruderlage-Sensor korrekt kalibriert
□ Bypass-Ventil korrekt markiert und bedienbar
□ Kabelverbindungen intakt, korrosionsfrei
□ Sicherungen korrekt dimensioniert

F. FUNKTIONSTEST
□ Steuerrad von Anschlag zu Anschlag drehen
   Lock-to-Lock Umdrehungen: ___
□ Spiel in Mittellage: ___ Grad
□ Schwergängigkeit? □ Nein □ Ja, wo: ___________
□ Rückmeldung (Feedback) spürbar? □ Ja □ Eingeschränkt □ Nein
□ Ungewöhnliche Geräusche? □ Nein □ Ja: ___________
□ Autopilot-Funktionstest (wenn vorhanden):
   □ Kurshalten □ Kurswechsel □ Umschaltung manuell/AP

G. GESAMTBEWERTUNG
□ Steueranlage: □ Gut □ Befriedigend □ Mangelhaft □ Kritisch
□ Nächste Inspektion empfohlen: ___________
□ Dringende Maßnahmen: ___________
```

### Tabelle R5: Ersatzteil-Bevorratung für Langfahrt

| Komponente | Empfehlung Langfahrt | Gewicht ca. | Kosten ca. |
|-----------|---------------------|-------------|-----------|
| Steuerseile (kompletter Satz) | ✅ Pflicht | 1–2 kg | €80–€200 |
| Seilklemmen (Bulldog, 6 Stk.) | ✅ Pflicht | 0,3 kg | €15–€30 |
| Umlenkrollen (2 Stk.) | ✅ Empfohlen | 0,5 kg | €40–€80 |
| Seilspanner (1 Stk.) | ✅ Empfohlen | 0,2 kg | €20–€40 |
| Gabelbolzen + Splinte (Sortiment) | ✅ Pflicht | 0,3 kg | €15–€25 |
| Hydrauliköl (1 Liter) | ✅ Pflicht (bei Hydraulik) | 0,9 kg | €15–€30 |
| O-Ring-Sortiment | ✅ Empfohlen (bei Hydraulik) | 0,1 kg | €10–€20 |
| Ruderlager-Dichtungssatz | 🔄 Optional | 0,2 kg | €30–€80 |
| Notpinne | ✅ Pflicht (bei Radsteuerung) | 1–3 kg | €80–€300 |
| Packungsmaterial (Stopfbuchse) | ✅ Empfohlen | 0,1 kg | €10–€20 |
| Schlauchschellen (Sortiment) | ✅ Empfohlen | 0,2 kg | €10–€15 |

### Tabelle R6: Normen-Referenz kompakt

| Norm | Titel | Relevanz | Letzte Ausgabe |
|------|-------|---------|---------------|
| ISO 8847 | Wire rope and pulley steering | Seilzugsteuerungen | 2004 |
| ISO 8848 | Remote steering systems | Alle Fernsteuerungen | 2020 |
| ISO 10592 | Hydraulic steering systems | Hydraulische Steuerungen | 1994 |
| ISO 25197 | Electrical/electronic control | Elektrische Steuerungen | 2020 |
| ISO 12217 | Stability and buoyancy | Gewichtsverteilung Steueranlage | 2022 |
| ISO 15085 | Man-overboard prevention | Cockpit-Gestaltung, Steuerstand | 2003 |
| ISO 11812 | Cockpits | Cockpit-Anordnung, Steuerplatz | 2020 |
| 2013/53/EU | Sportbootrichtlinie | CE-Kennzeichnung, Grundanforderungen | 2013 |
| ABYC P-17 | Steering systems (US) | Amerikanischer Standard | 2022 |
| GL Rules | Yachts ≤24m | Klassifikation Steueranlagen | 2023 |

### Tabelle R7: Typische Ausfallraten nach Steuerungstyp

| Steuerungstyp | MTBF (Jahre) | Häufigster Ausfall | Typische Reparaturkosten |
|--------------|-------------|-------------------|------------------------|
| Pinne | >30 | Ruderlager | €200–€500 |
| Seilzug | 6–10 (Seile) | Seilriss | €150–€400 |
| Kette | 12–18 | Kettenrad-Verschleiß | €200–€600 |
| Zahnstange | 10–15 | Kabelbruch | €100–€300 |
| Hydraulik (manuell) | 8–12 | Dichtungsleck | €300–€800 |
| Hydraulik (Power) | 6–10 | Pumpe/Magnetventil | €500–€2.000 |
| Elektrohydraulisch | 5–8 | Sensorausfall | €400–€1.500 |
| Fly-by-Wire | 4–7 | Elektronik/Software | €1.000–€5.000 |

### Tabelle R8: Steueranlagen-Kosten nach Bootsgröße (Neuinstallation, komplett)

| Bootslänge | Seilzug | Kette | Hydraulik (manuell) | Elektrohydraulisch |
|-----------|---------|-------|--------------------|--------------------|
| 8 m | €800–€1.500 | €1.200–€2.000 | €2.000–€3.500 | — |
| 10 m | €1.000–€2.000 | €1.500–€2.500 | €2.500–€4.500 | — |
| 12 m | €1.200–€2.500 | €1.800–€3.500 | €3.500–€6.000 | €6.000–€10.000 |
| 14 m | €1.500–€3.000 | €2.500–€4.500 | €4.500–€8.000 | €8.000–€14.000 |
| 16 m | — | €3.000–€5.500 | €6.000–€11.000 | €10.000–€18.000 |
| 18 m | — | — | €8.000–€15.000 | €14.000–€25.000 |
| 20 m | — | — | €10.000–€20.000 | €18.000–€35.000 |
| 24 m | — | — | €15.000–€30.000 | €25.000–€50.000 |

*Preise inkl. Pedestal, Übertragung, Quadrant/Zylinder, Steuerrad, Installation. Ohne Ruder/Schaft.*

### Tabelle R9: Sicherheitsfaktoren nach Klassifikationsgesellschaft

| Gesellschaft | Ruderschaft (Biegung) | Ruderschaft (Torsion) | Steuerseile | Hydraulikleitung |
|-------------|----------------------|----------------------|-------------|-----------------|
| GL/DNV | 3,5 | 3,0 | 4,0 | 4,0 (Burst) |
| Lloyd's | 3,5 | 3,0 | 4,0 | 4,0 |
| BV | 3,0 | 2,5 | 4,0 | 3,5 |
| RINA | 3,0 | 2,5 | 3,5 | 3,5 |
| ABS | 3,5 | 3,0 | 4,0 | 4,0 |
| ISO 8847 (Sportboot) | — | — | 4,0 | — |
| ISO 10592 (Sportboot) | — | — | — | 4,0 |
| ABYC (US) | 3,5 | 3,0 | 4,0 | 4,0 |

### Tabelle R10: Umrechnungsfaktoren für Steueranlagen

| Von | Nach | Faktor |
|----|------|--------|
| Knoten (kn) | m/s | × 0,5144 |
| Knoten (kn) | km/h | × 1,852 |
| PSI | bar | × 0,06895 |
| bar | PSI | × 14,504 |
| Zoll (in) | mm | × 25,4 |
| Fuß (ft) | m | × 0,3048 |
| kgf | N | × 9,81 |
| N | kgf | × 0,102 |
| Nm | ft·lbf | × 0,7376 |
| ft·lbf | Nm | × 1,3558 |
| in³ | cm³ | × 16,387 |
| cm³ | in³ | × 0,06102 |
| Grad (°) | Radiant (rad) | × π/180 |
| Gallone (US) | Liter | × 3,785 |
| Kubikinch/U | cm³/U | × 16,387 |

### Referenzen und Quellen

**Bücher:**
- Larsson, L. & Eliasson, R.: *Principles of Yacht Design*, 4. Auflage, Adlard Coles, 2014
- Marchaj, C.A.: *Aero-Hydrodynamics of Sailing*, 3. Auflage, Adlard Coles, 2000
- Kinney, F.S.: *Skene's Elements of Yacht Design*, 8. Auflage, Dodd Mead, 1981
- Gerr, D.: *The Nature of Boats*, International Marine, 1992
- Gerr, D.: *The Elements of Boat Strength*, International Marine, 2000
- Nicolson, I.: *Surveying Small Craft*, 4. Auflage, Adlard Coles, 2004
- Calder, N.: *Boatowner's Mechanical and Electrical Manual*, 4. Auflage, International Marine, 2015

**Normen:**
- ISO 8847:2004 — Small craft — Steering gear — Wire rope and pulley steering systems
- ISO 8848:2020 — Small craft — Remote steering systems
- ISO 10592:1994 — Small craft — Hydraulic steering systems
- ISO 25197:2020 — Small craft — Electrical/electronic control systems
- EU-Richtlinie 2013/53/EU — Sportboote und Wassermotorräder

**Hersteller-Dokumentation:**
- Jefa Marine: Product Catalogue 2025, Installation Manuals
- Lewmar/Whitlock: Cobra Installation Guide, Continuum Technical Manual
- Edson International: Product Catalogue 2025, Rigging Guide
- Kobelt Manufacturing: Technical Bulletins, Installation Manuals
- Ultraflex: Product Catalogue 2025, Steering Systems Guide
- Vetus: Master Catalogue 2025, Hydraulic Steering Manual
- SeaStar Solutions/Dometic: Technical Reference Guide

**Unfallberichte:**
- MAIB (UK Marine Accident Investigation Branch): Datenbank Steuerversager 2010–2025
- BSU (Bundesstelle für Seeunfalluntersuchung): Jahresberichte 2015–2025
- USCG (US Coast Guard): Boating Accident Reports Database

---

*Ende der Wissensdatei 20.01 — Steueranlagen Grundlagen*
*AYDI Research — Version 1.0.0 — 2026-05-02*
