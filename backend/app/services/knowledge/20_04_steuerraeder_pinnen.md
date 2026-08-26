---
title: "Steuerräder und Pinnen — Materialien, Größen, Ergonomie, Hersteller, Montage"
kategorie: "20 Steueranlagen"
unterkategorie: "20.04 Steuerräder und Pinnen"
version: "1.0.0"
datum: "2026-05-02"
autor: "AYDI Research"
status: "validated"
confidence_quellen:
  - measured: "Hersteller-TDS, ISO-Normen, CE-Zertifizierungen, Klassifikationsgesellschaften"
  - documented: "Hersteller-Kataloge, Werftunterlagen, Montageleitfäden, Surveyberichte"
  - estimated: "Erfahrungswerte, Werft-Konsens, Sachverständigen-Praxis, Regatta-Erfahrung"
---

# 20.04 — Steuerräder und Pinnen: Materialien, Größen, Ergonomie, Hersteller, Montage im Yachtbau

> **Paralleldokument beachten.** Zum Thema „Steuerräder und Pinnen" existiert im Korpus ein
> zweites, **unabhängig geschriebenes** Dokument: [14_07_steuerraeder_pinnen.md](14_07_steuerraeder_pinnen.md).
> Beide sind je rund 3.800 Zeilen lang und teilen nur etwa 2 % ihrer Zeilen — sie
> ergänzen einander, driften aber auseinander (nachgewiesen an der DIN-766-Teilung
> in den Ankerketten-Dokumenten). Bei widersprüchlichen Angaben: beide lesen und
> gegen Hersteller-/Normdaten prüfen, statt einer Zahl zu vertrauen.


> **AYDI Wissensdatei 20.04** — Kategorie 20: Steueranlagen und Ruderanlagen
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
11. [ANHANG A–H — Fallstudien](#11-anhang-ah--fallstudien)
12. [ANHANG I–R — Pydantic v2 Modelle](#12-anhang-ir--pydantic-v2-modelle)

---

## 1. Einführung und Übersicht

### 1.1 Definition und Funktion

Steuerräder und Pinnen bilden die primäre Mensch-Maschine-Schnittstelle der Ruderanlage einer Yacht. Sie übertragen die Steuerbefehle des Rudergängers über mechanische, hydraulische oder elektromechanische Zwischenglieder auf das Ruderblatt. Die Wahl zwischen Steuerrad und Pinne ist eine der grundlegendsten Designentscheidungen im Yachtbau und beeinflusst Cockpit-Layout, Ergonomie, Segeleigenschaften, Sicherheit und die gesamte Nutzungsphilosophie des Bootes.

**Steuerrad (Helm Wheel):**
Ein kreisförmiges oder teilkreisförmiges Handrad, das über eine Steuersäule (Pedestal) und ein Getriebe (typischerweise Kettenzug, Seilzug oder Direktantrieb) den Ruderschaft dreht. Der Rudergänger steht oder sitzt hinter dem Rad und steuert durch Drehung in die gewünschte Richtung. Das Steuerrad ermöglicht feinfühlige Korrekturen über einen großen Drehbereich und bietet dem Rudergänger eine stabile Stehposition durch die Möglichkeit, sich am Rad festzuhalten.

**Pinne (Tiller):**
Ein Hebelarm, der direkt am Ruderschaft oder Ruderkopf befestigt ist und die Drehbewegung des Ruderblatts durch seitliche Auslenkung steuert. Die Pinne bietet direktes taktiles Feedback des Ruderdrucks — ein wesentlicher Vorteil für erfahrene Segler. Die Steuerrichtung ist gegenläufig: Pinne nach Backbord bewegt das Heck nach Backbord und den Bug nach Steuerbord.

### 1.2 Historischer Kontext

**Frühgeschichte bis 18. Jahrhundert:**
Die Pinne ist das älteste Steuerinstrument der Seefahrt. Bereits in der Wikingerzeit (8.–11. Jh.) wurden Pinnen verwendet, zunächst als Hebelarm am Seitenruder, später am Heckruder. Die Kolderstock-Steuerung (Whipstaff) des 15.–17. Jahrhunderts war eine vertikale Hebelverlängerung der Pinne, die es ermöglichte, vom erhöhten Quarterdeck aus zu steuern.

**18.–19. Jahrhundert — Das Steuerrad entsteht:**
Das Steuerrad (Ship's Wheel) wurde im frühen 18. Jahrhundert für große Segelschiffe entwickelt, als die zunehmende Schiffsgröße Ruderdrücke erzeugte, die mit einer einfachen Pinne nicht mehr beherrschbar waren. Die Übertragung erfolgte über Seilzüge (Steering Ropes) oder Ketten (Chain Steering), die das Rad über Quadrant oder Trommel mit dem Ruderschaft verbanden. Auf der HMS Victory (1765) war ein doppeltes Steuerrad mit Kettenzug installiert, das von bis zu vier Rudergängern gleichzeitig bedient werden konnte.

**20. Jahrhundert — Differenzierung im Yachtbau:**
Mit der Demokratisierung des Segelsports nach dem Zweiten Weltkrieg differenzierten sich die Steuerungskonzepte:
- **Jollenklasse und Kielboote bis ~8m:** Pinne blieb Standard wegen Gewicht, Einfachheit und direktem Feedback
- **Fahrtenyachten ab ~9m:** Steuerrad setzte sich durch wegen steigender Ruderdrücke und Komfort
- **Regattayachten:** Koexistenz beider Systeme, abhängig von Klasse und Philosophie
- **Motoryachten:** Steuerrad universell, zunehmend mit hydraulischer Unterstützung

**21. Jahrhundert — Aktuelle Trends:**
- Doppelrad-Anlagen als Standard auf Fahrtenyachten ab 12m
- Carbon-Steuerräder im Regattabereich und Premiumsegment
- Joystick-Steuerung für Motoryachten (Hafen-Manöver)
- Tillerpilot und Pinnenautomat als Interface zwischen Autopilot und Pinne
- Folding Wheels (Faltsteuerräder) für beengte Cockpits
- Ergonomische Pinnenausleger (Tiller Extensions) für Regattasegler

### 1.3 Steuerrad vs. Pinne — Grundsätzliche Abwägung

| Kriterium | Steuerrad | Pinne |
|-----------|-----------|-------|
| **Bootsgröße** | Ab ~8m üblich, ab ~11m quasi Standard | Bis ~12m praktikabel, bis ~9m ideal |
| **Ruderdruck** | Hoch — Übersetzung nötig | Niedrig bis mittel — direkt beherrschbar |
| **Feedback** | Gedämpft durch Getriebe | Direkt und ungefiltert |
| **Cockpit-Platz** | Pedestal nimmt Raum ein, Passage eingeschränkt | Pinn-Schwenkbereich blockiert Cockpit-Mitte |
| **Gewicht** | 8–35 kg (Rad + Pedestal + Getriebe) | 1–5 kg (Pinne + Beschläge) |
| **Kosten** | €800–€15.000+ | €100–€2.500 |
| **Wartung** | Kette/Seil, Getriebe, Lager | Minimal — Bolzen, Buchse |
| **Autopilot-Anbindung** | Radpilot am Pedestal oder hydraulisch | Tillerpilot direkt an Pinne |
| **Langfahrt-Komfort** | Hoch — stehende Position, Instrumentierung am Pedestal | Mittel — sitzende Position, Pinnenautomat nötig |
| **Regatta-Performance** | Gut — sichere Position bei Krängung | Sehr gut — schnellere Korrekturen, weniger Totgang |
| **Notsteuerung** | Komplex — Notpinne als Backup nötig | Einfach — System ist die Notsteuerung |
| **Sichtlinien** | Eingeschränkt durch Pedestal und Bimini | Frei — niedriger Schwerpunkt des Rudergängers |
| **Krängungskomfort** | Sehr gut — Rad als Haltepunkt | Mäßig — freie Hand nötig zum Festhalten |

### 1.4 Relevanz im AYDI-Analysesystem

Im Kontext des AYDI-Analysesystems beeinflusst die Steuerrad/Pinnen-Konfiguration folgende Module:

- **Ergonomie-Modul:** Steuerposition, Griffhöhe, Sichtlinien, Bedienkräfte, Krängungskomfort
- **Compliance-Modul:** ISO 8847 (Steueranlagen), ISO 11591 (Sichtfeld), CE-Konformität
- **Kosten-Modul:** Beschaffung, Installation, Lebensdauer-Kosten
- **Produktions-Modul:** Pedestal-Montage, Cockpit-Sole-Verstärkung, Kabel-/Seilführung
- **Emotional-Modul:** Designanspruch, Haptik, Materialwirkung (Teak, Carbon, Leder)
- **Material-Modul:** Korrosion, UV-Beständigkeit, Verschleiß der Griffmaterialien
- **Brand-DNA-Modul:** Hersteller-typische Steuerungsphilosophie (z.B. Hallberg-Rassy → Pinne bis 42 Fuß)

### 1.5 Normative Grundlagen

Die Auslegung und Installation von Steuerrädern und Pinnen unterliegt folgenden Normen und Richtlinien:

| Norm | Titel | Relevanz |
|------|-------|----------|
| **ISO 8847:2021** | Steueranlagen — Anforderungen und Prüfungen | Hauptnorm für Steuersysteme |
| **ISO 11591:2020** | Sichtfeld vom Steuerstand | Sichtlinien über/um das Steuerrad |
| **ISO 13929:2001** | Steueranlagen — Zahnrad-gekoppelte Systeme (Geared Link) | Anforderungen an zahnradgekoppelte Steuerungen |
| **ISO 10592:1994** | Steueranlagen — Hydraulisch | Anforderungen an hydraulische Steuerungen |
| **ISO 15085:2003** | Mann-über-Bord-Verhütung | Haltegriffe am Steuerrad |
| **ISO 11812:2020** | Cockpits — Wasserdichtheit | Pedestal-Durchbruch als potenzielle Leckstelle |
| **ISO 12217:2022** | Stabilität | Gewicht und Position des Steuerstands |
| **RCD 2013/53/EU** | Sportboot-Richtlinie | CE-Kennzeichnung, Designkategorie-Abhängigkeit |
| **ABYC P-20** | Steueranlagen (US-Standard) | US-Markt-Anforderungen |

### 1.6 Begriffsdefinition: Steueranlage im Kontext

```
┌─────────────────────────────────────────────────────────────────┐
│                      STEUERANLAGE                                │
│                                                                  │
│  ┌──────────┐   ┌──────────────┐   ┌────────────┐   ┌────────┐ │
│  │ Steuerrad│──▶│  Steuersäule │──▶│ Übertragung│──▶│ Ruder- │ │
│  │ oder     │   │  (Pedestal)  │   │ (Kette/    │   │ schaft │ │
│  │ Pinne    │   │  oder        │   │  Seil/     │   │        │ │
│  │          │   │  Ruderkopf   │   │  Hydraulik)│   │        │ │
│  └──────────┘   └──────────────┘   └────────────┘   └────────┘ │
│       ▲                                                   │      │
│       │              ┌──────────────┐                    ▼      │
│       │              │  Autopilot   │──────────────▶ Ruder-    │
│       └──────────────│  (optional)  │               blatt     │
│                      └──────────────┘                          │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. Grundlagen und Theorie

### 2.1 Steuerrad-Durchmesser-Berechnung

Die Wahl des richtigen Steuerrad-Durchmessers ist ein Zusammenspiel aus Ergonomie, Ruderdruck und Cockpit-Abmessungen. Es gibt keine einzelne Formel, sondern ein System von Randbedingungen, die gleichzeitig erfüllt sein müssen.

#### 2.1.1 Ergonomische Grundregel

Der Rad-Durchmesser muss so bemessen sein, dass der Rudergänger bequem die obere Hälfte des Rades greifen kann, ohne die Arme übermäßig anzuheben oder zu strecken:

```
D_optimal = 2 × (H_schulter - H_achse) × 0.85

Wobei:
  D_optimal    = Optimaler Raddurchmesser [mm]
  H_schulter   = Schulterhöhe des Rudergängers über Cockpit-Sole [mm]
  H_achse      = Höhe der Radachse über Cockpit-Sole [mm]
  0.85         = Ergonomie-Korrekturfaktor (leicht gebeugte Arme)
```

**Typische Werte:**
- Schulterhöhe stehend: 1.350–1.450 mm (europäischer Durchschnitt)
- Achshöhe über Sole: 850–1.050 mm (Pedestal-abhängig)
- Ergebnis: D_optimal ≈ 510–1.020 mm → Standardbereich 600–1.000 mm

#### 2.1.2 Ruderdruck-basierte Dimensionierung

Der Ruderdruck bestimmt die Mindestkraft, die der Rudergänger aufbringen muss. Der Rad-Durchmesser beeinflusst das Drehmoment am Rad:

```
M_rad = F_hand × (D/2)

Wobei:
  M_rad    = Drehmoment am Steuerrad [Nm]
  F_hand   = Handkraft des Rudergängers [N]
  D        = Raddurchmesser [m]

Auflösung nach D:
  D_min = 2 × M_ruder / (F_hand_max × i_getriebe)

Wobei:
  M_ruder       = Ruderdrehmoment [Nm]
  F_hand_max    = Max. zulässige Handkraft [N] — Norm: 100 N (Dauerbelastung), 200 N (kurzzeitig)
  i_getriebe    = Getriebeübersetzung (Pedestal + Quadrant)
```

**Ruderdrehmoment-Schätzung nach Bootsklasse:**

| Bootsklasse | LOA [m] | Ruderfläche [m²] | M_ruder bei 6 kn [Nm] | M_ruder bei Böe [Nm] |
|-------------|---------|-------------------|------------------------|----------------------|
| Daysailer | 6–8 | 0.05–0.10 | 15–40 | 30–80 |
| Fahrtenyacht klein | 8–10 | 0.10–0.18 | 40–100 | 80–200 |
| Fahrtenyacht mittel | 10–13 | 0.15–0.28 | 80–200 | 160–400 |
| Fahrtenyacht groß | 13–16 | 0.25–0.40 | 150–350 | 300–700 |
| Performance Cruiser | 12–16 | 0.20–0.35 | 100–250 | 200–500 |
| Superyacht | 16–24 | 0.35–0.80 | 250–800 | 500–1.600 |
| Motoryacht (Verdränger) | 10–15 | 0.15–0.35 | 100–300 | 200–600 |
| Motoryacht (Gleiter) | 8–12 | 0.08–0.18 | 50–150 | 100–300 |

#### 2.1.3 Übersetzungsverhältnis und Umdrehungen

Das Gesamtübersetzungsverhältnis bestimmt, wie viele Radumdrehungen für den vollen Ruderausschlag nötig sind:

```
n_umdrehungen = α_ruder_gesamt / (360° / i_gesamt)

Typische Werte:
  α_ruder_gesamt = Gesamter Ruderausschlag (typisch ±35° = 70° gesamt)
  i_gesamt       = Gesamtübersetzung aus Getriebe × Quadrant

Empfohlene Umdrehungen (Lock-to-Lock):
  Segelboot Fahrt:    2.5 – 3.5 Umdrehungen
  Segelboot Regatta:  1.5 – 2.5 Umdrehungen
  Motoryacht langsam: 3.0 – 4.0 Umdrehungen
  Motoryacht schnell: 2.0 – 3.0 Umdrehungen
  Superyacht:         3.5 – 5.0 Umdrehungen (hydraulisch unterstützt)
```

**Faustregel:** Weniger Umdrehungen = schnelleres Ansprechen, aber höhere Bedienkräfte. Mehr Umdrehungen = feinfühligere Steuerung bei geringeren Kräften.

#### 2.1.4 Cockpit-Randbedingungen

```
Mindestabstände (gemäß Ergonomie-Praxis):

  Radkante — Steuerstand-Sitz:     min. 350 mm (stehend), min. 250 mm (sitzend)
  Radkante — Cockpit-Süll:          min. 100 mm (Freigang Hände)
  Radkante — Laufgang-Kante:        min. 600 mm (Passage bei Krängung)
  Rad-Unterkante — Cockpit-Sole:    min. 200 mm (Beinfreiheit, Ablauf)
  Rad-Oberkante — Sichtlinie:       max. auf Augenhöhe sitzend (ca. 1.100–1.200 mm)
```

#### 2.1.5 Standard-Durchmesser nach Bootslänge

| LOA [m] | Empfohlener Durchmesser [mm] | Typischer Bereich [mm] | Bemerkung |
|---------|------------------------------|------------------------|-----------|
| 6–8 | — (Pinne) | — | Steuerrad untypisch |
| 8–9 | 600–700 | 560–750 | Destroyer-Wheel möglich |
| 9–10 | 700–800 | 650–850 | Standardbereich |
| 10–12 | 800–900 | 750–950 | Meistverkaufter Bereich |
| 12–14 | 900–1.000 | 850–1.050 | Oft Doppelrad |
| 14–16 | 1.000–1.100 | 950–1.150 | Doppelrad Standard |
| 16–20 | 1.100–1.200 | 1.050–1.250 | Superyacht-Bereich |
| 20–24 | 1.200–1.400 | 1.100–1.500 | Hydraulisch unterstützt |

### 2.2 Griffkräfte und Ergonomie

#### 2.2.1 Handkraft-Normwerte

Die zulässigen Bedienkräfte am Steuerrad sind in ISO 8847 und ergonomischer Literatur definiert:

| Bediensituation | Max. Handkraft [N] | Max. Drehmoment bei D=900mm [Nm] | Anmerkung |
|-----------------|--------------------|------------------------------------|-----------|
| Dauerbetrieb (Fahrt) | 30–50 N | 13,5–22,5 | Ermüdungsfreies Steuern über Stunden |
| Normalbetrieb (Manöver) | 50–100 N | 22,5–45 | Wenden, Halsen, Hafenmanöver |
| Kurzzeitbelastung | 100–200 N | 45–90 | Böen, Notmanöver |
| Notsteuerung | bis 350 N | bis 157,5 | Absolute Grenze, beidhändig |
| ISO 8847 Grenze Dauersteuerung | ≤80 N | ≤36 | Normative Anforderung |
| ISO 8847 Grenze Notsteuerung | ≤280 N | ≤126 | Normative Anforderung |

#### 2.2.2 Griffdurchmesser und Griffformen

| Griffdurchmesser [mm] | Eignung | Anmerkung |
|------------------------|---------|-----------|
| 20–25 | Zu dünn | Schnelle Ermüdung, einschneidend bei Last |
| 25–30 | Regatta-Griff | Dünner Griff für schnelles Umgreifen |
| 30–35 | **Optimaler Bereich** | Beste Kraftübertragung und Komfort |
| 35–40 | Komfort-Griff | Gut für große Hände, etwas träger |
| 40–50 | Zu dick | Ermüdend, schwer zu umschließen |

**Griffformen:**

- **Rund (Teak/Edelstahl):** Klassisch, universell, drehbar in der Hand → gut für schnelles Umgreifen
- **Oval (ergonomisch):** Anatomisch angepasst, höhere Kraftübertragung, aber orientierungsgebunden
- **Flachoval (Leder umwickelt):** Kombination aus Griffigkeit und Orientierung
- **Knauf-Griff (Fingertip Knob):** Am Radkranz montiert, für Einhand-Steuerung bei Motoryachten — bei Segelbooten unüblich und teilweise gefährlich (Handgelenkverletzung bei Rückschlag)

#### 2.2.3 Griffmaterialien — Haptik und Funktion

| Material | Griffigkeit trocken | Griffigkeit nass | UV-Beständigkeit | Temperatur-Komfort | Pflege |
|----------|--------------------|-----------------|--------------------|--------------------:|--------|
| Teak (natur geölt) | ★★★★★ | ★★★★☆ | ★★★★☆ | ★★★★★ | Jährlich ölen |
| Teak (lackiert) | ★★★★☆ | ★★★☆☆ | ★★★☆☆ | ★★★★★ | 2-jährlich nachlackieren |
| Leder (genäht) | ★★★★★ | ★★★☆☆ | ★★☆☆☆ | ★★★★☆ | 6-monatlich pflegen |
| Edelstahl 316L | ★★★☆☆ | ★★☆☆☆ | ★★★★★ | ★☆☆☆☆ (heiß/kalt) | Minimal |
| Carbon (klar) | ★★★☆☆ | ★★☆☆☆ | ★★★★★ (mit UV-Coat) | ★★★★☆ | Minimal |
| Carbon (Teak-Inlay) | ★★★★★ | ★★★★☆ | ★★★★★ | ★★★★★ | Jährlich Teak ölen |
| Kork | ★★★★★ | ★★★★★ | ★★★☆☆ | ★★★★★ | Jährlich versiegeln |
| Gummi/TPE | ★★★★☆ | ★★★★★ | ★★☆☆☆ | ★★★★☆ | Austausch bei Verhärtung |
| Aluminium eloxiert | ★★★☆☆ | ★★☆☆☆ | ★★★★★ | ★★☆☆☆ (heiß/kalt) | Minimal |

### 2.3 Steuerübersetzung und Getriebebauarten

#### 2.3.1 Seilzug-Steuerung (Cable Steering)

Das älteste und einfachste Übertragungsprinzip für Radsteuerungen:

```
Aufbau:
  Steuerrad → Kettenrad (Sprocket) → Kette → Seilzug (Wire Rope) → Quadrant/Radial-Drive

Komponenten:
  - Kettenrad: Ø 100–200 mm, gehärteter Stahl oder Bronze
  - Kette:     DIN 8187, Teilung 6,35 mm (1/4") oder 9,525 mm (3/8")
  - Seilzug:   1×19 oder 7×7 Edelstahl, Ø 3–6 mm
  - Umlenkrollen: Sheaven Ø 60–150 mm, Nylon oder Bronze-Buchse
  - Spannschloss: Zum Einstellen der Seilvorspannung

Übersetzung:
  i_seil = D_quadrant / D_kettenrad

  Beispiel:
    D_quadrant = 350 mm (Radius Quadrant)
    D_kettenrad = 100 mm (Radius Sprocket)
    i_seil = 350/100 = 3,5:1
```

**Vorteile:** Einfach, bewährt, wartbar, kostengünstig, leicht zugänglich
**Nachteile:** Seil-Dehnung (Totgang), regelmäßige Nachspannung nötig, Korrosionsanfällig, Umlenkrollen als Verschleißteile

**Spezifikation Seilvorspannung:**
- Handprobe: Seil soll sich bei Daumendruck ca. 10–15 mm seitlich auslenken lassen
- Zu straff: erhöhter Verschleiß, schwergängiges Ruder
- Zu lose: Totgang, verzögertes Ansprechen, Seil kann von Umlenkrolle springen

#### 2.3.2 Kettenzug-Steuerung (Chain & Wire)

```
Aufbau:
  Steuerrad → Kettentrommel → Kette (direkt zum Quadrant, ohne Seil)

Verwendet bei:
  - Einfache Steuerungen kleiner Boote
  - Notsteuerung als Backup
  - Historische Yachten

Übersetzung:
  Direkt über Trommel-Ø und Quadrant-Radius
```

#### 2.3.3 Schneckengetriebe (Worm Drive)

```
Aufbau:
  Steuerrad → Schnecke (Worm) → Schneckenrad (Worm Wheel) → Ruderschaft direkt

Eigenschaften:
  - Hohe Übersetzung in einem Schritt (typisch 15:1 bis 40:1)
  - Selbsthemmend bei niedrigen Steigungswinkeln → Ruder bleibt stehen ohne Festhalten
  - Kompakter Aufbau, kein externer Quadrant nötig
  - Höhere Reibungsverluste als Seilzug

Anwendung:
  - Lewmar Commodore-Pedestal (intern Schneckengetriebe)
  - Edson Worm-Gear-Steuerungen
  - Motoryachten mit Innensteuerpult
```

#### 2.3.4 Zahnstangengetriebe (Rack & Pinion)

```
Aufbau:
  Steuerrad → Ritzel (Pinion) → Zahnstange (Rack) → Steuerseil oder Gestänge

Eigenschaften:
  - Lineare Umsetzung der Drehbewegung
  - Geringer Totgang bei korrekter Einstellung
  - Typisch für Motoryachten (direkt vom Innensteuerstand)

Hersteller:
  - Teleflex/SeaStar (Dominant im Motorboot-Segment)
  - Uflex
  - Ultraflex
```

#### 2.3.5 Hydraulische Steuerung

```
Aufbau:
  Steuerrad → Hydraulikpumpe (Helm Pump) → Leitungen → Hydraulikzylinder → Ruderschaft

Typenunterscheidung:
  a) Manuell-hydraulisch: Handkraft dreht Pumpe, Zylinder bewegt Ruder
  b) Power-Assist: Handkraft + Servopumpe
  c) Voll-hydraulisch: Elektrische Servopumpe, Rad als Sensor

Vorteile:
  - Kein mechanischer Totgang
  - Flexible Leitungsführung (keine geraden Wege nötig)
  - Mehrere Steuerstände einfach realisierbar
  - Autopilot-Integration über Hydraulikventil
  - Rückwirkungsdämpfung (kein Rückschlag bei Wellengang)

Nachteile:
  - Kein direktes Ruderfeedback (→ Feedback-Ventil nötig)
  - Leckage-Risiko
  - Regelmäßiger Ölwechsel
  - Höhere Kosten (€2.000–€15.000 je nach Größe)
```

### 2.4 Cockpit-Ergonomie und Steuerstand-Layout

#### 2.4.1 Steuerstand-Geometrie bei Radsteuerung

```
Optimale Dimensionen (stehender Rudergänger, 50. Perzentil):

                    ┌─────────────────┐
                    │    Instrumente   │
                    │    H = 1100mm    │
                    └────────┬────────┘
                             │
                    ┌────────┴────────┐
                    │   Steuerrad      │
                    │   Mitte bei      │
                    │   H = 950mm      │  ◄── Achshöhe über Sole
                    │   D = 900mm      │
                    └────────┬────────┘
                             │
                ├────────────┤
                   450mm       ◄── Abstand Sole-Vorderkante des Pedestal
                             │
    ───────────────┴──────────────────
           Cockpit-Sole (0 mm)

  Fußposition:    350–500 mm vor Radachse
  Armwinkel:      Ellbogen 90°–120° bei Griff der Rad-Oberkante
  Kopffreiheit:   Min. 1.900 mm unter Bimini/Sprayhood
  Sichtlinie:     Über Radkranz auf Vorschiff-Horizont
```

#### 2.4.2 Doppelrad-Anordnung (Twin Wheel)

```
Standardmaße für Doppelrad-Installation:

  ┌────────────────────────────────────────────┐
  │              Cockpit-Breite                 │
  │     ┌──────┐         ┌──────┐             │
  │     │ Rad  │◄──Ab──▶│ Rad  │             │
  │     │  BB  │  stand  │  StB │             │
  │     └──────┘         └──────┘             │
  │                                            │
  │     Passage-Breite:  min. 500 mm           │
  │     (Zwischen Rädern, Cockpit-Mitte)       │
  │                                            │
  │     Abstand Radmitte – Radmitte:           │
  │       D + 500mm bis D + 800mm              │
  │       Bei D=900mm: 1.400–1.700 mm          │
  └────────────────────────────────────────────┘
```

**Vorteile Doppelrad:**
- Passage in der Cockpit-Mitte bleibt frei
- Rudergänger kann auf der Luvseite steuern (bessere Sicht, weniger Krängung)
- Zweiter Steuerplatz für Gäste/Co-Skipper
- Instrumentenpanel in der Mitte zwischen den Rädern

**Nachteile Doppelrad:**
- Doppelte Kosten (zwei Räder, zwei Pedestals oder geteilter Pedestal)
- Mehr Gewicht
- Komplexere Mechanik (Zwischenwelle oder Seilverbindung)
- Kein zentraler Steuerplatz möglich

#### 2.4.3 Pinnen-Ergonomie

```
Optimale Pinnen-Dimensionen:

  Pinnenlänge L:    LOA × 0.12 bis LOA × 0.18
                    Minimum: 700 mm
                    Maximum: 1.400 mm (bei Segelbooten bis 12m)

  Griffhöhe H:      400–700 mm über Cockpit-Sole (sitzender Rudergänger)
  Seitlicher Ausschlag:  ±30°–±45° ab Mittellinie
  Griffposition:    Letzte 30% der Pinnenlänge

  Beispiel Fahrtenyacht 10m:
    L = 10.000 mm × 0.15 = 1.500 mm → gewählt 1.200 mm (Cockpit-Breite begrenzt)
    H = 550 mm über Sole
    Ausschlag: ±35° → Seitlicher Hub am Griff: ±35° × sin(35°) × 1.200 mm ≈ ±690 mm

  Pinnenverlängerung (Tiller Extension):
    Zusätzlich 500–1.200 mm, ausklappbar/teleskopierbar
    Universal-Gelenk (Kugelkopf) am Pinnenanschluss
    Winkel: 0° (gerade) bis 90° (seitlich) einstellbar
```

### 2.5 Sichtlinien vom Steuerstand

#### 2.5.1 ISO 11591 — Sichtfeld-Anforderungen

```
Anforderungen für Sportboote:

  Voraussicht:    Min. 360° im Umkreis, wobei direkte Voraussicht
                  (Bereich ±22,5° von der Mittschiffsachse) nicht
                  länger als 2× LOA unterbrochen sein darf.

  Vertikaler Sichtwinkel:
    - Obere Grenze: min. 20° über Horizontale
    - Untere Grenze: min. 10° unter Horizontale (bei Steuerstand im Rumpf)
    - Wasserlinie: sichtbar bei max. 1.5× LOA Entfernung voraus

  Seitensicht:
    - Min. 112,5° nach jeder Seite (= 225° Gesamtbogen)
    - Achterliche Sicht: empfohlen 360° (nicht immer normativ gefordert)
```

#### 2.5.2 Sichtlinienanalyse bei verschiedenen Steuerrad-Konfigurationen

```
Szenario 1: Einzelrad, zentral
  + Symmetrische Sicht
  − Bimini-Unterkante kann Vorsegel verdecken
  − Rad-Oberkante bei niedrigem Pedestal in Sichtlinie

Szenario 2: Doppelrad
  + Rudergänger Luvseite: exzellente Sicht Lee-Segel
  + Cockpit-Mitte frei → gute Achtervision
  − Radgestell und Instrumente als Sichthindernis

Szenario 3: Pinne
  + Niedrigster Augenpunkt → beste Sicht unter Segeln hindurch
  + Kein Pedestal als Hindernis
  − Rudergänger sitzt → eingeschränkte Horizontsicht in Lee

Szenario 4: Steuerstand innen (Motoryacht)
  + Windschutz, Instrumentierung direkt vor Augen
  − Scheiben, Rahmen, A-Säulen als Sichtbehinderung
  − Beschlag, Spiegelung bei Sonne
```

### 2.6 Materialien — Vertiefung

#### 2.6.1 Edelstahl 316L / 316Ti

**Anwendung:** Radkranz, Speichen, Nabe, Pedestal-Gehäuse, Pinnen-Beschläge

**Spezifikation:**
- Werkstoffnummer: 1.4404 (316L) / 1.4571 (316Ti)
- Zugfestigkeit: 500–700 MPa
- Streckgrenze: 200–300 MPa
- Bruchdehnung: 40–50%
- Dichte: 8,0 g/cm³
- Korrosionsbeständigkeit: PREN ≥ 24 (316L), ≥ 25 (316Ti)
- Oberflächengüte: Ra ≤ 0,4 µm (poliert) für maximale Korrosionsbeständigkeit
- Magnetismus: austenitisch = im Idealfall nicht magnetisch (aber: Kaltverformung kann Ferrit erzeugen)

**Verarbeitungshinweise:**
- WIG-Schweißen (TIG) mit Argon-Schutzgas, Zusatzwerkstoff 316LSi
- Beizen und Passivieren nach dem Schweißen (Salpeter-/Flusssäure-Gemisch oder Beizpaste)
- NIEMALS mit Werkzeug bearbeiten, das vorher für Normalstahl verwendet wurde (Fremdrost)
- Oberflächenpolitur: #4 (Satiniert, matt, industriell) bis #8 (Spiegelhochglanz, Marine-Standard)

**Typische Probleme im Yachteinsatz:**
- Spaltkorrosion unter Beschlägen, in Gewindebohrungen
- Lochfraß (Pitting) bei chloridbelasteter Atmosphäre, ungenügender Politur
- Spannungsrisskorrosion bei gleichzeitiger mechanischer Belastung und Salzwasser
- "Tea Staining": Braune Verfärbung durch atmosphärische Korrosion in Küstennähe, kosmetisch aber nicht strukturell

#### 2.6.2 Carbon (CFK — Kohlefaserverstärkter Kunststoff)

**Anwendung:** Radkranz, Speichen, Pinnen (High-Performance, Racing, Superyacht)

**Spezifikation (typisch für Steuerrad-Laminat):**
- Fasertyp: T700 oder T800 (High Tenacity), 12K-Rovings
- Harzmatrix: Epoxid (z.B. HexPly M56, Gurit SE 84)
- Laminataufbau: ±45°/0°/90° quasi-isotrop oder gewickelt
- Zugfestigkeit: 600–1.200 MPa (laminatabhängig)
- E-Modul: 70–150 GPa (laminatabhängig)
- Dichte: 1,5–1,6 g/cm³ (= 80% leichter als Edelstahl)
- Wandstärke Radkranz: typisch 3–6 mm
- Finish: Klarlack (UV-beständig, z.B. 2K-PU mit UV-Absorber) oder lackiert

**Qualitätsmerkmale (sichtbar):**
- Gleichmäßiges Gewebe-Bild, keine Harzansammlungen oder Lufteinschlüsse
- Hochglanz-Oberfläche (Klarlack) oder perfekte Lackierung
- Keine Delaminationsstellen an Kanten
- Präzise Einpassung der Teak-Inlays (falls vorhanden)

**Typische Probleme:**
- UV-Degradation ohne Schutzlackierung (Vergilbung, Faserabzeichnung)
- Delaminierung durch Schlagbelastung (Tools, Schot-Enden)
- Feuchtigkeit in Mikrorissen → Frostschäden
- Galvanische Korrosion an Edelstahl-Übergängen (ohne Isolation)

#### 2.6.3 Teak (Tectona grandis)

**Anwendung:** Griffsegmente am Radkranz, Pinnen, Griffe, Speichen-Ummantelung

**Spezifikation:**
- Sorte: Burma-Teak Grad A (FSC-zertifiziert) — Goldstandard
- Plantagen-Teak: Möglich, aber geringere natürliche Ölsättigung
- Dichte: 630–720 kg/m³ (lufttrocken)
- Biegebruchfestigkeit: 97–115 MPa
- Natürlicher Ölgehalt: 3–5% (Burma A), 1–3% (Plantage)
- Schwindmaß: 2,5% tangential, 1,5% radial (= sehr formstabil)
- Dauerhaftigkeitsklasse: 1 (sehr dauerhaft, EN 350)

**Verarbeitung für Steuerräder:**
- Auswahl: Kernholz (Heartwood), gleichmäßige goldbraune Farbe, keine Splintholzanteile
- Maserungsrichtung: Längsfaser entlang des Radkranzes (Biegefestigkeit!)
- Segmentbauweise: 4–8 Teak-Segmente pro Kranz, Fingerzinken-Verleimung oder Edelstahl-Stifte
- Oberflächenbehandlung:
  - Option A: Teak-Öl (Sikkens Cetol Marine, Semco, Boracol) — natürliches Finish, regelmäßige Pflege
  - Option B: Marine-Klarlack (Epifanes, International) — glänzend, weniger Pflege, weniger Grip nass
  - Option C: Unbehandelt → vergraut (Patina-Look), akzeptabel aber Schmutzeinlagerung

**Typische Probleme:**
- Schwarze Flecken: Gerbsäure-Reaktion mit Edelstahl bei Feuchtigkeit → Isolierung durch Teflon-Buchsen
- UV-Vergrauung: Ohne Pflege silbergrau in 6–12 Monaten
- Rissbildung (Checking): Trocknungsrisse bei extremer Sonneneinstrahlung
- Ölverlust: Natürliches Öl verdampft → Holz wird spröde und rau

#### 2.6.4 Leder

**Anwendung:** Radkranz-Umwicklung, Pinnengriff, Premium-Optik

**Spezifikation:**
- Lederart: Vollnarbiges Rindsleder (Full Grain Cowhide) oder Ziegenleder
- Stärke: 0,8–1,2 mm
- Gerbung: Chromgerbung (Standard) oder pflanzlich gegerbt (Premium, historischer Look)
- Behandlung: Marine-Imprägnierung (z.B. Leder-Wachs, Neatsfoot Oil)
- Farbe: Natur (hellbraun), dunkelbraun, schwarz, weiß (Superyacht)
- Naht: Kreuznaht (Turk's Head) oder Baseball-Naht, gewachstes Segelgarn (Or.Nr. 8–12)

**Wickeltechnik — Turk's Head (Schmuck-Endknoten):**
Ein 3-Lead × 5-Bight Turk's Head wird an den Übergangsstellen Leder/Edelstahl als Abschluss gesetzt. Traditionelle Seemannsarbeit, wird von spezialisierten Werkstätten ausgeführt.

**Typische Probleme:**
- Schimmelbildung in tropischem Klima → regelmäßige Belüftung und Fungizid-Behandlung
- UV-Ausbleichung → Bimini als UV-Schutz, UV-Lederpflege
- Salzwasser-Steifheit → Süßwasser-Abspülung nach Salzwasserkontakt
- Naht-Auflösung → gewachstes Garn, UV-beständig

#### 2.6.5 Aluminium (für Pinnen)

**Anwendung:** Pinnen (hohlprofiliert), Pinnenverlängerungen, Tiller-Köpfe

**Spezifikation:**
- Legierung: 6082-T6 (AlMgSi1, EN AW-6082)
- Zugfestigkeit: 310–340 MPa
- Streckgrenze: 260–290 MPa
- Bruchdehnung: 10–12%
- Dichte: 2,7 g/cm³
- Korrosionsbeständigkeit: Gut, aber Eloxierung empfohlen
- Eloxierung: Hart-Eloxal (Typ III, 25–50 µm) für Marine-Einsatz
- Alternativ: Pulverbeschichtung (RAL 9005 schwarz oder RAL 9010 weiß)

**Typische Probleme:**
- Galvanische Korrosion bei Kontakt mit Edelstahl oder Bronze → Isolation (PTFE, Nylon)
- Lochfraß unter Ablagerungen (Salzwasser, stehend)
- Ermüdungsrisse bei Schwingbelastung → periodische Sichtprüfung

#### 2.6.6 GFK/FRP (Glasfaserverstärkter Kunststoff)

**Anwendung:** Pinnen (Fahrtenyachten, Serienproduktion), Ruderkopf-Abdeckungen

**Spezifikation:**
- Aufbau: Rohr-Profil aus E-Glas/Polyester oder E-Glas/Vinylester
- Wandstärke: 4–8 mm (abhängig von Querschnitt und Belastung)
- Typisch: Hohlprofil Ø 40–60 mm, oft mit Holzkern oder Schaumkern
- Oberfläche: Gelcoat weiß oder Farbe der Yacht

**Typische Probleme:**
- UV-Kreidung des Gelcoats
- Osmose bei Vinylester-freien Laminaten (selten bei Pinnen)
- Ermüdung bei Dauerschwingbelastung → Rissbildung am Ansatz

### 2.7 Kraftfluss und Belastungsberechnung

#### 2.7.1 Belastungsfall Steuerrad

```
Belastungsfall 1: Normaler Segelbetrieb
  F_hand = 50 N (einhand)
  M_rad = F_hand × D/2 = 50 × 0.45 = 22,5 Nm (bei D=900mm)

Belastungsfall 2: Böe (Segelboot)
  F_hand = 150 N (beidhändig)
  M_rad = 150 × 0.45 = 67,5 Nm

Belastungsfall 3: Sturzbelastung (Person fällt auf Rad)
  F_sturz = 1.500 N (äquivalent ~150 kg Schock)
  M_sturz = 1.500 × 0.45 = 675 Nm → Speichen und Nabe müssen dies aushalten

Belastungsfall 4: Prüflast nach ISO 8847
  Rad: 3× Betriebslast oder min. 500 N am Radkranz, 5 min gehalten
  Pinne: 3× Betriebslast am Griffende, 5 min gehalten
```

#### 2.7.2 Belastungsfall Pinne

```
Biegebelastung:
  M_biege = F_ruderdruck × L_pinne

  Beispiel:
    F_ruderdruck = 200 N (Böe, 10m Segelyacht)
    L_pinne = 1.000 mm
    M_biege = 200 × 1,0 = 200 Nm

  Querschnitt:
    Erforderliches Widerstandsmoment W = M / σ_zul
    Für Teak: σ_zul ≈ 35 MPa (Biegung, Sicherheitsfaktor 3)
    W = 200.000 / 35 = 5.714 mm³
    → Ovalprofil ca. 50×70 mm ausreichend

    Für Carbon-Rohr: σ_zul ≈ 200 MPa (mit SF 4)
    W = 200.000 / 200 = 1.000 mm³
    → Rohr Ø 40×3 mm ausreichend (W_rohr ≈ 2.800 mm³)
```

#### 2.7.3 Ermüdungsbetrachtung

```
Zyklische Belastung am Steuerrad:
  Typische Belastungszyklen pro Stunde Segeln:  200–500 (Korrekturbewegungen)
  Belastungszyklen pro Saison (500h):           100.000–250.000
  Lebensdauer 20 Jahre:                          2.000.000–5.000.000 Zyklen

  Edelstahl 316L:  Dauerfestigkeit bei ca. 250 MPa (10^7 Zyklen) → im Normalfall unkritisch
  Aluminium 6082:  KEINE Dauerfestigkeitsgrenze → Ermüdungsrissbildung theoretisch immer möglich
  Carbon:          Ermüdungsfestigkeit ≈ 60–70% der statischen Festigkeit bei 10^6 Zyklen
  Teak:            Ermüdung ist bei Holz kein typisches Versagensmuster (eher Faserdegradation)
```

### 2.8 Montage und Installation

#### 2.8.1 Pedestal-Montage

```
Montagereihenfolge:

1. Positionsbestimmung:
   - Mittschiffslinie markieren
   - Achsabstand zu Ruderquadrant/Steuerseilen prüfen
   - Sichtlinien-Check (ISO 11591)

2. Durchbruch Cockpit-Sole:
   - Bohrschablone des Herstellers verwenden
   - GFK-Laminat mit Diamant-Lochsäge durchbohren
   - Schnittkanten mit Epoxid versiegeln (Feuchtigkeitsschutz)

3. Unterdeck-Verstärkung:
   - Backing Plate: Edelstahl 316L, Stärke min. 5 mm, Fläche min. 200×200 mm
   - ALTERNATIV: GFK-Laminat-Verstärkung (4–6 Lagen UD-Glas)
   - Lastverteilung berechnen: Punktlast des Pedestals auf Schalenfläche verteilen

4. Dichtung:
   - Flansch-Dichtring (EPDM oder Butyl)
   - Sikaflex 291/295 oder 3M 4200 als Dichtstoff unter dem Flansch
   - NIEMALS Silikon verwenden (keine Haftung auf GFK)

5. Befestigung:
   - Schrauben: M10 oder M12 Edelstahl A4-80 (316, Festigkeitsklasse 80)
   - Anzugsmoment: M10 = 35–45 Nm, M12 = 55–70 Nm
   - Sicherung: Nyloc-Mutter oder Loctite 243

6. Steuerseile/Kette anschließen:
   - Seilspannung einstellen
   - Rudermittellage prüfen (Ruder gerade → Rad gerade)
   - Endanschläge (Stops) prüfen
```

#### 2.8.2 Pinnen-Montage

```
Montagereihenfolge:

1. Ruderkopf prüfen:
   - Profilform (flach, rund, konisch)
   - Befestigungsart (Klemm-Pinne, Steck-Pinne, verschraubt)
   - Kerbverzahnung vorhanden?

2. Pinne aufschieben:
   - Orientierung prüfen (Sweep-Winkel, falls vorhanden)
   - Klemmbolzen oder Madenschraube handfest anziehen

3. Befestigung:
   - Klemmbolzen: M8–M12, Edelstahl A4
   - Anzugsmoment: gemäß Herstellerangabe (typisch 15–30 Nm)
   - Sicherung: Splint, Sicherungsblech oder Loctite

4. Funktionsprüfung:
   - Voller Ruderausschlag (hart Backbord → hart Steuerbord)
   - Freigängigkeit prüfen (keine Kollision mit Achterlieks, Backstagen, Bimini)
   - Pinnenverlängerung montieren und Gelenk prüfen

5. Endanschläge:
   - Ruder-Endanschläge (am Ruderschaft oder Quadrant) prüfen
   - Sicherstellen, dass Pinne nicht über Endanschlag hinaus bewegt werden kann
```

---

## 3. Typenübersicht

### 3.1 Destroyer-Wheel (Zerstörer-Rad)

#### 3.1.1 Beschreibung

Das Destroyer-Wheel ist der verbreitetste Steuerrad-Typ im modernen Yachtbau. Benannt nach den markanten Steuerrädern auf Kriegsschiffen (Destroyers) des frühen 20. Jahrhunderts, zeichnet es sich durch einen durchgehenden Radkranz mit mindestens 4 Speichen und einer zentralen Nabe aus.

#### 3.1.2 Konstruktionsmerkmale

```
Aufbau:
  - Radkranz: Edelstahl-Rohr Ø 22–32 mm, gebogen (oder Carbon)
  - Speichen: Edelstahl-Rohr Ø 16–25 mm, verschweißt oder verschraubt
  - Nabe: Edelstahl-Guss oder CNC-gefräst, konische Aufnahme (1:10 Konus)
  - Griff-Segmente: Teak, Leder, Kork oder Carbon (auf Radkranz aufgeklebt/geschraubt)

Standard-Speichenanzahl:
  - 3 Speichen: Modern-Design, optisch leicht, weniger Griffoptionen
  - 4 Speichen: Sehr häufig, gute Balance aus Design und Funktion
  - 5 Speichen: Standard für Fahrtenyachten, maximale Griffoptionen
  - 6 Speichen: Klassisch, Superyacht-Segment
  - 8+ Speichen: Historisch (Ship's Wheel), restaurierte Klassik-Yachten

Durchmesser-Bereich: 600–1.500 mm
Gewicht: 4–18 kg (Edelstahl), 2–8 kg (Carbon)
```

#### 3.1.3 Varianten

**a) Classic Destroyer (Teak & Edelstahl):**
Polierter Edelstahl-Radkranz mit Teak-Griffsegmenten zwischen den Speichen. Höchster Wiedererkennungswert, "Yacht-Look" schlechthin. Hersteller: Lewmar, Edson, Jefa, Stazo.

**b) All-Stainless Destroyer:**
Komplett aus poliertem oder satiniertem Edelstahl. Pflegeleicht, industrielles Erscheinungsbild. Typisch für Performance-Cruiser und Charter-Yachten.

**c) Carbon Destroyer:**
Radkranz und Speichen aus Carbon, Nabe Edelstahl oder Titan. 50–70% Gewichtsersparnis. Sichtbares Carbon-Gewebe oder lackiert. Hersteller: Carbonautica, Edson (Talon Carbon), Lewmar (Carbon Corsair).

**d) Leather-Wrapped Destroyer:**
Edelstahl-Grundstruktur mit Lederumwicklung am gesamten Radkranz. Klassisch-elegantes Erscheinungsbild, hervorragende Haptik. Typisch für Superyachten, klassische Yachten.

### 3.2 Speichenrad (Spoke Wheel)

#### 3.2.1 Beschreibung

Das Speichenrad unterscheidet sich vom Destroyer-Wheel durch dünnere, stabförmige Speichen (statt Rohr), die oft Turk's-Head-Knoten oder Leder-Umwicklung tragen. Historisch ist es der ältere Typ, der direkt vom Schiffssteuerrad des 18. Jahrhunderts abstammt.

#### 3.2.2 Konstruktionsmerkmale

```
Aufbau:
  - Radkranz: Teak-Vollholz (traditionell) oder Edelstahl mit Teak
  - Speichen: Edelstahl-Rundstab Ø 12–20 mm oder Teak-Rundstab Ø 25–40 mm
  - Nabe: Bronze-Guss (traditionell) oder Edelstahl
  - Besonderheit: Speichen oft mit gedrechselten Griffen (Handles) versehen

Speichenanzahl: 6–12 (typisch 8)
Durchmesser: 700–1.200 mm
Gewicht: 5–15 kg
```

#### 3.2.3 Anwendung

- Klassische Yachten (Holzboote, Repliken)
- Traditionelle Fahrtenyachten im "Bristol-Stil"
- Restaurierungsprojekte
- Superyachten mit klassischem Interior

### 3.3 Faltrad (Folding Wheel)

#### 3.3.1 Beschreibung

Das Faltrad ist eine platzsparende Sonderform, bei der der Radkranz oder die Speichen zusammenklappbar sind. Im gefalteten Zustand reduziert sich der Platzbedarf um 40–60%, was die Passage im Cockpit erheblich verbessert.

#### 3.3.2 Konstruktionsmerkmale

```
Varianten:

a) Klappbare Speichen (Lewmar Folding):
   - Speichen mit Scharniergelenk an der Nabe
   - Radkranz aus flexiblem Material oder segmentiert
   - Fixierung: Arretierbolzen oder Federmechanismus
   - Nachteil: Spiel an den Gelenken, geringere Steifigkeit

b) Teilbarer Radkranz (Edson Folding):
   - Radkranz in 2–3 Segmenten, Scharniere an Speichen-Anschlüssen
   - Zusammenklappen nach innen (zur Nabe hin)
   - Vorteil: Steife Konstruktion im ausgeklappten Zustand

c) Entfernbarer Radkranz (Quick-Release):
   - Radkranz wird komplett abgenommen und verstaut
   - Schnellverschluss (Quarter-Turn oder Bajonett)
   - Vorteil: Keine Kompromisse bei Steifigkeit
   - Nachteil: Loser Radkranz muss sicher verstaut werden

Durchmesser: 600–900 mm (typisch kleiner als Standard-Destroyer)
Gewicht: 3–8 kg
Falt-Dimension: 50–60% des aufgeklappten Durchmessers
```

#### 3.3.3 Anwendung

- Kleinere Yachten mit beengtem Cockpit (8–10m)
- Yachten mit Achter-Cockpit und Heckpassage
- Boote mit sowohl Innen- als auch Außensteuerstand
- Charteryachten (Platz für Badeplattform-Zugang)

### 3.4 Doppelrad (Twin Wheel)

#### 3.4.1 Beschreibung

Zwei Steuerräder, symmetrisch links und rechts der Cockpit-Mittellinie angeordnet, verbunden über eine gemeinsame Steuermechanik. Seit den 2000er Jahren Standard auf Fahrtenyachten ab 12m.

#### 3.4.2 Konstruktionsmerkmale

```
Verbindung der zwei Räder:

a) Gemeinsamer Pedestal mit Zwischenwelle:
   - Ein zentraler Pedestal mit zwei Radanschlüssen
   - Mechanische Kopplung über Welle und Kegelräder
   - Hersteller: Jefa, Whitlock

b) Getrennte Pedestals mit Seilverbindung:
   - Zwei unabhängige Pedestals, über Steuerseil synchronisiert
   - Flexiblere Positionierung
   - Hersteller: Lewmar, Edson

c) Hydraulisch gekoppelt:
   - Jedes Rad treibt eine eigene Hydraulikpumpe
   - Gemeinsamer Hydraulikzylinder am Ruder
   - Perfekte Synchronisation ohne mechanischen Verschleiß
   - Hersteller: Jefa, Lecomble & Schmitt

Standard-Durchmesser: Meist 800–1.000 mm (kleiner als Einzelrad derselben Bootsgröße)
Abstand Mitte-Mitte: 1.200–1.800 mm
Passagebreite dazwischen: min. 400–600 mm
```

#### 3.4.3 Besondere Designaspekte

- **Instrumenten-Pod:** Zwischen den Rädern auf der Pedestal-Brücke montiert
- **Traveller-Integration:** Großschot-Traveller oft direkt hinter den Pedestals
- **Autopilot:** Radpilot an einem der beiden Räder oder hydraulisch
- **Klappbare Variante:** Innenliegendes Rad klappbar für Passage (z.B. Lewmar)

### 3.5 Pinne — Holz

#### 3.5.1 Beschreibung

Die klassische Holzpinne ist ein Massivholz-Hebelarm, der direkt auf dem Ruderkopf sitzt. In der traditionellen Ausführung aus einem Stück Hartholz gefertigt, bei modernen Yachten oft laminiert.

#### 3.5.2 Konstruktionsmerkmale

```
Holzarten:

a) Teak (Standard):
   - Dichte: 630–720 kg/m³
   - Biegebruchfestigkeit: 97–115 MPa
   - Vorteil: Optimal für Marine-Einsatz, natürlich ölig
   - Querschnitt: Oval 50×70 bis 60×90 mm

b) Eiche (Klassisch):
   - Dichte: 670–760 kg/m³
   - Biegebruchfestigkeit: 80–105 MPa
   - Vorteil: Hart, schöne Maserung
   - Nachteil: Gerbsäure reagiert mit Edelstahl → schwarze Flecken
   - Querschnitt: Oval 55×80 bis 65×95 mm

c) Esche/Hickory (Regatta):
   - Dichte: 690–750 kg/m³
   - Biegebruchfestigkeit: 100–130 MPa
   - Vorteil: Sehr zäh, elastisch, gute Schlagfestigkeit
   - Nachteil: Nicht dauerhaft gegen Feuchtigkeit → guter Schutzanstrich nötig
   - Querschnitt: Rund Ø 40–55 mm oder oval 45×60 mm

d) Iroko (Teak-Ersatz):
   - Dichte: 630–690 kg/m³
   - Biegebruchfestigkeit: 75–95 MPa
   - Vorteil: Günstiger als Teak, ähnliche Beständigkeit
   - Querschnitt: Oval 55×75 bis 60×90 mm

e) Mahagoni (Sipo):
   - Dichte: 560–640 kg/m³
   - Biegebruchfestigkeit: 70–95 MPa
   - Vorteil: Schöne Optik (Klassik-Yachten)
   - Nachteil: Mäßige Witterungsbeständigkeit
   - Querschnitt: Oval 55×80 mm

Formgebung:
  - Gerade Pinne: Einfach, effektiv, üblich bis 10m
  - Geschwungene Pinne (Swan-Neck): Angehobener Griff für Sitzposition
  - S-förmig: Ruderkopf tief, Griff auf Cockpit-Süll-Höhe
  - Laminiert (Streifen-Verleimung): Stärker als Massivholz, formbar
```

#### 3.5.3 Typische Qualitätskriterien (AYDI-Bewertung)

| Merkmal | Premium | Standard | Mangelhaft |
|---------|---------|----------|------------|
| Holzqualität | Kernholz, makellos | Leichte Äste erlaubt | Splintholz, Risse |
| Maserung | Langfaser durchgehend | Leichte Abweichung | Kurzfasrig, Fehlstellen |
| Oberfläche | Spiegelglatt, geölt/lackiert | Leicht rau, geölt | Rau, unbehandelt |
| Passform Ruderkopf | Spielfrei, präzise | Minimal Spiel | Wackelt, Korrosion sichtbar |
| Beschläge | 316L, sauber verarbeitet | 316L, funktional | 304, Rostspuren |

### 3.6 Pinne — Carbon

#### 3.6.1 Beschreibung

Carbon-Pinnen sind Hochleistungskomponenten für den Regatta- und Performance-Cruising-Bereich. Sie bieten eine extreme Gewichtsersparnis bei hoher Steifigkeit.

#### 3.6.2 Konstruktionsmerkmale

```
Aufbau:
  - Rohr-Profil: Ø 35–60 mm, Wandstärke 2–5 mm
  - Laminat: Uni-Direktional (0°) für Biegesteifigkeit + ±45° für Torsion
  - Endstück: Eingeklebte Edelstahl- oder Titan-Buchse für Ruderkopf-Anschluss
  - Griffbereich: Aufgerauter Carbon oder Kork/Gummi-Griff
  - Optional: Teak-Inlay im Griffbereich

Gewichtsvergleich (Pinne 1.000 mm, vergleichbare Festigkeit):
  Teak massiv:     1.200–1.800 g
  Aluminium-Rohr:    600–900 g
  Carbon-Rohr:       200–450 g

Kosten:
  €300–€800 (Standard-Rohr, Universalanschluss)
  €800–€2.500 (Maßanfertigung, Sichtcarbon, Teak-Inlay)
```

#### 3.6.3 Hersteller

- **Carbonautica** (Italien): Maßanfertigung, Premium-Segment
- **CST Composites** (Australien): Standard-Rohre und Maßanfertigung
- **Forte Carbon** (Niederlande): Regatta-Fokus
- **C-Tech** (UK): Pinnen und Pinnenverlängerungen
- **Southern Spars** (Neuseeland): Custom für Superyachten

### 3.7 Pinne — Aluminium

#### 3.7.1 Beschreibung

Aluminium-Pinnen sind der Standard im Regattabereich (Jollenklassen, Kielboote) und kommen auch auf einfachen Fahrtenyachten vor. Sie bieten ein gutes Verhältnis von Festigkeit, Gewicht und Kosten.

#### 3.7.2 Konstruktionsmerkmale

```
Aufbau:
  - Rohr-Profil: Ø 30–50 mm, Wandstärke 2–4 mm
  - Legierung: 6082-T6 oder 6061-T6 (Marine-tauglich)
  - Oberfläche: Hart-eloxiert (Typ III, 25–50 µm) oder Pulverbeschichtung
  - Endstück: Angeschweißte Gabel oder eingeklebte Buchse
  - Griffbereich: EVA-Schaumstoff oder Gummi-Griff aufgezogen
  - Optional: Teleskop-Verlängerung integriert

Standard-Maße:
  Jolle (Laser, 420):  Ø 25×2 mm, L=1.000 mm, 200–350 g
  Kielboot (J/24):     Ø 32×2,5 mm, L=900 mm, 350–500 g
  Fahrtenyacht 8–10m:  Ø 40×3 mm, L=1.100 mm, 500–800 g
  Fahrtenyacht 10–12m: Ø 45×3,5 mm, L=1.200 mm, 700–1.100 g
```

### 3.8 Pinnenverlängerung (Tiller Extension / Hiking Stick)

#### 3.8.1 Beschreibung

Die Pinnenverlängerung (auch Hiking Stick oder Tiller Extension) ist ein Hebelarm, der am Pinnenende über ein Universalgelenk befestigt wird und es dem Rudergänger ermöglicht, aus der Ausreitposition (Hiking) oder vom seitlichen Cockpitsitz aus zu steuern.

#### 3.8.2 Konstruktionsmerkmale

```
Typen:

a) Feste Verlängerung:
   - Starres Rohr mit Universalgelenk (Kugelkopf oder Gummi-Gelenk)
   - Länge: 500–1.200 mm
   - Material: Carbon (80–200 g), Aluminium (150–350 g)
   - Gelenk: Wichard Snap-Shackle, Ronstan, Allen Brothers

b) Teleskop-Verlängerung:
   - Ausziehbar von ca. 600 auf 1.000 mm
   - Klemmung: Drehklemme, Federklemme oder Twist-Lock
   - Vorteil: Anpassbar an Situation (Cockpit vs. Ausreiten)
   - Nachteil: Etwas schwerer, Klemmung als Schwachpunkt

c) Klapp-Verlängerung:
   - Faltbar in der Mitte (Scharnier mit Arretierung)
   - Verstauen bei Nichtgebrauch
   - Typisch für Fahrtenyachten

Universalgelenk-Typen:
  - Kugelkopf (Ball Joint): ±30° in alle Richtungen, Standard
  - Gummi-Gelenk: Preiswert, begrenzte Lebensdauer
  - Doppel-Kardangelenk: Maximale Freiheit, Regatta-Standard
  - Snap-on: Werkzeugfreie Montage/Demontage
```

#### 3.8.3 Auswahl nach Bootsgröße

| Klasse | Verlängerungs-Länge [mm] | Material | Gelenk-Typ | Gewicht [g] |
|--------|--------------------------|----------|-------------|-------------|
| Optimist | 500–600 | Alu | Gummi | 100–150 |
| Laser/ILCA | 750–1.000 | Carbon/Alu | Kugelkopf | 120–250 |
| 420/470 | 600–900 | Carbon | Kugelkopf | 100–200 |
| J/24 | 700–1.000 | Carbon | Doppel-Kardan | 150–280 |
| Fahrtenyacht 8m | 600–800 | Alu | Kugelkopf | 200–400 |
| Fahrtenyacht 10m | 700–1.000 | Alu/Carbon | Kugelkopf | 250–500 |
| Fahrtenyacht 12m | 800–1.200 | Carbon | Kugelkopf | 300–600 |

### 3.9 Joystick-Steuerung

#### 3.9.1 Beschreibung

Die Joystick-Steuerung ist ein modernes Eingabegerät, das primär bei Motoryachten für Hafenmanöver und Positionierung eingesetzt wird. Sie ersetzt nicht das Steuerrad, sondern ergänzt es für Niedriggeschwindigkeits-Manöver.

#### 3.9.2 Konstruktionsmerkmale

```
Funktionsprinzip:
  - Proportionale Steuerung von Ruder + Antrieb(en) in X/Y/R-Achse
  - X = Vorwärts/Rückwärts
  - Y = Seitlich (seitliche Bugstrahlruder + Heckstrahlruder)
  - R = Rotation (Drehung auf der Stelle)

  Verarbeitung:
    Joystick-Position → Controller (ECU) → Verteilt Befehle an:
      - Hauptantrieb(e) (Vorwärts/Rückwärts)
      - Bugstrahlruder
      - Heckstrahlruder (falls vorhanden)
      - Ruder

Hersteller-Systeme:
  - Volvo Penta IPS Joystick (für IPS-Antriebe)
  - Mercury Joystick Piloting (für Zeus/Bravo-Antriebe)
  - Yamaha Helm Master EX
  - Yanmar JC20 Joystick
  - ZF Mathers MicroCommander (Großyachten)
  - Side-Power (Sleipner) Joystick

Montageposition:
  - Neben dem Steuerrad (Handbreit erreichbar)
  - Am Flybridge-Steuerstand
  - An der Reling (Walk-Around-Joystick für Anlegemanöver)
  - Kabellos (Funkfernbedienung, z.B. Volvo Penta EVC-E)

Kosten:
  - Einfach (Bugstrahlruder-only): €500–€1.500
  - Vollintegriert (Dual-Engine + Bug/Heck-Thruster): €5.000–€25.000
  - Dynamic Positioning (GPS-gestützt): €15.000–€50.000
```

#### 3.9.3 Bewertung im AYDI-Kontext

| Aspekt | Bewertung | Kommentar |
|--------|-----------|-----------|
| Ergonomie | ★★★★★ | Intuitive Bedienung, geringe Lernkurve |
| Sicherheit | ★★★★☆ | Fail-Safe-Modi, aber Ausfall bei Elektronikdefekt |
| Wartung | ★★★☆☆ | Elektronik-Intensiv, Software-Updates nötig |
| Kosten | ★★☆☆☆ | Hohe Anschaffung und Integration |
| Einhand-Manöver | ★★★★★ | Der eigentliche Zweck |
| Segel-Eignung | ☆☆☆☆☆ | Nicht für Segelboote relevant |

---

## 4. Produktlinien und Spezifikationen

### 4.1 Lewmar Steuerräder

Lewmar (Havant, UK, gegründet 1946) ist einer der weltweit größten Hersteller von Decksbeschlägen und dominiert den Steuerrad-Markt im Fahrtenyacht-Segment.

#### 4.1.1 Lewmar Commodore-Serie

**Positionierung:** Integriertes Steuerrad-Pedestal-System für Fahrtenyachten 9–16m. Beinhaltet Pedestal, Getriebe, Kompass-Aufnahme und Steuerrad.

**Modellübersicht:**

| Modell | Pedestal-Höhe [mm] | Radgrößen [mm] | Getriebe | Bootsklasse |
|--------|---------------------|-----------------|----------|-------------|
| Commodore 400 | 760 | 610, 700, 810 | Schnecke | 8–10m |
| Commodore 500 | 840 | 700, 810, 910 | Schnecke | 9–12m |
| Commodore 600 | 920 | 810, 910, 1010 | Schnecke | 11–14m |
| Commodore 700 | 1.000 | 910, 1010, 1110 | Schnecke | 13–16m |

**Technische Daten Commodore 500 (Beispiel-Detaillierung):**
- Pedestal-Material: Edelstahl 316L, poliert oder satiniert
- Getriebe: Schneckengetriebe, Übersetzung 14:1
- Lock-to-Lock: 2,8 Umdrehungen (bei ±35° Ruderausschlag)
- Max. Ruderdrehmoment: 280 Nm
- Kompass-Aufnahme: Plastimo Contest 101 oder Ritchie Navigator
- Ketten-Typ: 3/8" Einfach-Rollenkette (DIN 8187)
- Seilzug: 7×7 Edelstahl Ø 4 mm
- Gewicht Pedestal (ohne Rad): 12,5 kg
- Zubehör-Aufnahmen: Einhand-Instrument-Halter, Getränkehalter, Guard (Bügel)

**Rad-Optionen Commodore:**
| Radtyp | Durchmesser | Material | Griff | Gewicht | Preis (ca.) |
|--------|-------------|----------|-------|---------|-------------|
| Destroyer | 810 mm | SS 316L | Teak-Segmente | 5,8 kg | €650 |
| Destroyer | 910 mm | SS 316L | Teak-Segmente | 7,2 kg | €780 |
| All-Stainless | 810 mm | SS 316L | poliert | 5,2 kg | €520 |
| Leather-Wrap | 910 mm | SS 316L | Leder schwarz | 6,1 kg | €850 |

#### 4.1.2 Lewmar Corsair-Serie

**Positionierung:** Leichtes, modernes Steuerrad ohne integriertes Getriebe, für Nachrüstung oder bei separatem Steuergetriebe.

**Modellübersicht:**

| Modell | Durchmesser [mm] | Speichen | Material Kranz | Material Griff | Gewicht [kg] |
|--------|-------------------|----------|----------------|----------------|--------------|
| Corsair 3-Spoke | 610 | 3 | SS 316L | — | 2,8 |
| Corsair 3-Spoke | 700 | 3 | SS 316L | Teak | 3,4 |
| Corsair 5-Spoke | 810 | 5 | SS 316L | Teak | 5,1 |
| Corsair 5-Spoke | 910 | 5 | SS 316L | Teak | 6,3 |
| Corsair 5-Spoke | 1010 | 5 | SS 316L | Teak | 7,6 |
| Corsair Carbon 3 | 700 | 3 | Carbon | Carbon/Teak | 1,8 |
| Corsair Carbon 3 | 810 | 3 | Carbon | Carbon/Teak | 2,3 |

**Naben-Standard:** Lewmar verwendet konische Naben (1:10 Konus) mit Kerbverzahnung. Passend für Lewmar-Pedestal und Jefa-Schäfte (Adapter verfügbar).

#### 4.1.3 Lewmar Evolution-Serie

**Positionierung:** Premium-Steuerrad mit ergonomisch optimiertem Design, leicht geschwungene Speichen, verbesserte Griffergonomie.

**Innovationen:**
- Ergonomisch geformter Radkranz: Leichter Oval-Querschnitt statt Kreisrund
- Teak-Segmente mit verbesserter Befestigung (verdeckte Schrauben)
- Nabe mit integrierter Kompass-Aufnahme
- Optional: Beleuchtete Nabe (LED)

| Modell | Durchmesser [mm] | Speichen | Kranz | Griff | Gewicht [kg] | Preis (ca.) |
|--------|-------------------|----------|-------|-------|--------------|-------------|
| Evolution Classic | 810 | 5 | SS 316L | Teak | 5,4 | €890 |
| Evolution Classic | 910 | 5 | SS 316L | Teak | 6,8 | €1.050 |
| Evolution Classic | 1010 | 5 | SS 316L | Teak | 8,1 | €1.220 |
| Evolution Carbon | 810 | 5 | Carbon | Carbon/Teak | 2,6 | €2.400 |
| Evolution Carbon | 910 | 5 | Carbon | Carbon/Teak | 3,2 | €2.900 |
| Evolution Power | 910 | 5 | SS 316L | Leder | 7,0 | €1.150 |
| Evolution Power | 1010 | 5 | SS 316L | Leder | 8,5 | €1.380 |

### 4.2 Edson Steuerräder

Edson International (New Bedford, MA, USA, gegründet 1859) ist der älteste noch aktive Hersteller von Marine-Steueranlagen weltweit und dominiert den nordamerikanischen Markt.

#### 4.2.1 Edson PowerWheel

**Positionierung:** Edelstahl-Destroyer-Wheel mit patentiertem "ComfortGrip" — ein ergonomisch geformter Teak-Griff mit leichter Vertiefung für die Fingerauflage.

| Modell | Durchmesser [in/mm] | Speichen | Griff | Nabe | Gewicht [kg] | Preis (ca.) |
|--------|---------------------|----------|-------|------|--------------|-------------|
| PowerWheel 24 | 24" / 610 | 5 | ComfortGrip Teak | Standard | 4,5 | $780 |
| PowerWheel 28 | 28" / 710 | 5 | ComfortGrip Teak | Standard | 5,5 | $890 |
| PowerWheel 32 | 32" / 810 | 5 | ComfortGrip Teak | Standard | 6,8 | $1.020 |
| PowerWheel 36 | 36" / 915 | 5 | ComfortGrip Teak | Standard | 8,2 | $1.180 |
| PowerWheel 40 | 40" / 1015 | 5 | ComfortGrip Teak | Standard | 9,5 | $1.360 |
| PowerWheel 44 | 44" / 1120 | 5 | ComfortGrip Teak | Standard | 11,0 | $1.580 |

**Edson-Naben-System:**
- Standard-Bohrung: 3/4" (19,05mm) oder 1" (25,4mm) Tapered
- Kerbverzahnung: Edson-proprietär (13-Zahn)
- Adapter verfügbar für Lewmar, Whitlock, Jefa, Yacht Specialties

#### 4.2.2 Edson Talon-Serie

**Positionierung:** High-Performance-Steuerrad mit Carbon-Struktur und minimalistischem Design.

| Modell | Durchmesser [in/mm] | Speichen | Material | Griff | Gewicht [kg] | Preis (ca.) |
|--------|---------------------|----------|----------|-------|--------------|-------------|
| Talon Carbon 28 | 28" / 710 | 3 | Full Carbon | Carbon | 1,5 | $2.800 |
| Talon Carbon 32 | 32" / 810 | 3 | Full Carbon | Carbon/Teak | 1,9 | $3.400 |
| Talon Carbon 36 | 36" / 915 | 3 | Full Carbon | Carbon/Teak | 2,4 | $4.100 |
| Talon Carbon 40 | 40" / 1015 | 3 | Full Carbon | Carbon/Teak | 2,9 | $4.800 |
| Talon Carbon 44 | 44" / 1120 | 3 | Full Carbon | Carbon/Teak | 3,5 | $5.600 |

**Besonderheiten Talon:**
- Gewickelte Carbon-Rohre (Filament Wound) für maximale Steifigkeit
- Titan-Nabe (Grade 5, Ti-6Al-4V) als Leichtbau-Option
- UV-beständiger 2K-Klarlack (mit Keramik-Nanopartikeln)
- Optionale Heizung im Griffbereich (12V, 20W pro Seite)

#### 4.2.3 Edson Pedestal-Systeme

| Modell | Höhe [mm] | Max. Ruderdrehmoment [Nm] | Getriebe | Boot | Preis (ca.) |
|--------|-----------|---------------------------|----------|------|-------------|
| Edson 335 | 740 | 200 | Schnecke | 8–10m | $1.800 |
| Edson 336 | 840 | 300 | Schnecke | 10–12m | $2.200 |
| Edson 337 | 960 | 450 | Schnecke | 12–14m | $2.800 |
| Edson 338 | 1.060 | 600 | Schnecke | 14–17m | $3.500 |
| Edson 665 | 840 | 350 | Doppel-Schnecke | 11–14m Twin | $4.200 |
| Edson 667 | 960 | 550 | Doppel-Schnecke | 14–18m Twin | $5.800 |

### 4.3 Jefa Steueranlagen

Jefa Steering (Rudkøbing, Dänemark, gegründet 1956) ist spezialisiert auf komplette Steueranlagen und liefert an führende Werften wie Hallberg-Rassy, Najad, X-Yachts, Arcona, Dehler.

#### 4.3.1 Jefa Steuerrad-Portfolio

| Modell | Durchmesser [mm] | Speichen | Material | Besonderheit | Preis (ca.) |
|--------|-------------------|----------|----------|--------------|-------------|
| Jefa Classic | 700–1.100 | 5 | SS 316L + Teak | Klassisches Destroyer | €600–€1.100 |
| Jefa Modern | 700–1.100 | 3 | SS 316L | Minimalistisch, poliert | €500–€900 |
| Jefa Carbon | 700–1.000 | 3 | Carbon + SS Nabe | Sichtcarbon | €1.800–€3.200 |
| Jefa Leather | 700–1.100 | 5 | SS 316L + Leder | Handgenähtes Leder | €800–€1.400 |

#### 4.3.2 Jefa Pedestal- und Steuersysteme

Jefa ist bekannt für seine kompletten Steueranlagen "von Rad bis Ruder":

**Jefa Direct-Drive System:**
- Schneckengetriebe direkt am Ruderschaft (kein Quadrant, keine Seile)
- Minimaler Totgang
- Ideal für Neubauten (weit verbreitet bei skandinavischen Werften)
- Verfügbar für Ruderdrehmomente von 100 bis 1.200 Nm

**Jefa Cable-Drive System:**
- Seilzug-Steuerung mit Jefa-eigenem Quadrant
- Edelstahl-Seilzug Ø 4 oder 5 mm
- Nylon-Umlenkrollen mit versiegelten Lagern
- Lock-to-Lock: einstellbar 2,0–4,5 Umdrehungen

**Jefa Hydraulic System:**
- Manuell-hydraulisch für Boote 12–24m
- Jefa HHI-Serie (Hand Hydraulic Inboard)
- Volumenpumpe: 6–15 cm³/Umdrehung
- Zylinder: Ø 50–90 mm
- Autopilot-Ventil integrierbar

#### 4.3.3 Jefa Twin-Wheel-Lösungen

Jefa ist Marktführer bei Doppelrad-Steueranlagen für skandinavische Yachten:

```
Jefa Twin-Pedestal System:
  - Zwei separate Pedestals, verbunden über Zwischenwelle
  - Welle: Edelstahl Ø 25 mm, in PTFE-Buchsen gelagert
  - Länge: individuell (typisch 1.200–1.600 mm)
  - Verkleidung: GFK-Halbschalen, Teak-Auflagen

Jefa "Invisible" Twin:
  - Getriebe unter der Cockpit-Sole verborgen
  - Nur zwei kurze Steuersäulen (Ø 60mm) ragen heraus
  - Minimaler visueller Fußabdruck
  - Eingesetzt bei: Hallberg-Rassy 40+, Arcona, Najad
```

### 4.4 Goiot Steuerräder

Goiot (Nantes, Frankreich, gegründet 1920) ist ein traditionsreicher französischer Hersteller, bekannt für Luken, Fenster und Steuerräder. Goiot-Steuerräder finden sich auf vielen Beneteau-, Jeanneau- und Dufour-Yachten.

#### 4.4.1 Goiot Steuerrad-Portfolio

| Serie | Durchmesser [mm] | Speichen | Material | Zielmarkt | Preis (ca.) |
|-------|-------------------|----------|----------|-----------|-------------|
| Goiot Atlantique | 600–900 | 5 | SS 316L + Teak | Serienproduktion | €350–€650 |
| Goiot Pacifique | 700–1.000 | 5 | SS 316L + Teak Premium | Fahrtenyacht | €550–€900 |
| Goiot Carbone | 700–900 | 3 | Carbon + SS | Performance | €1.200–€2.200 |
| Goiot Prestige | 800–1.100 | 5 | SS 316L + Leder | Superyacht | €900–€1.500 |
| Goiot Tradition | 700–1.000 | 8 | Teak + Bronze | Klassisch | €1.500–€2.800 |

#### 4.4.2 Goiot OEM-Integration

Goiot liefert als OEM-Zulieferer an große Serienwerften:

| Werft | Modelle | Goiot-Rad | Durchmesser |
|-------|---------|-----------|-------------|
| Beneteau | Oceanis 34–51 | Atlantique | 700–900 mm |
| Jeanneau | Sun Odyssey 349–490 | Atlantique/Pacifique | 700–1.000 mm |
| Dufour | Dufour 360–530 | Pacifique | 800–1.000 mm |
| Lagoon | Lagoon 40–52 | Pacifique Twin | 800 mm (×2) |
| Fountaine Pajot | Astrea/Samana | Pacifique Twin | 800 mm (×2) |

### 4.5 Carbonautica

Carbonautica (Treviso, Italien, gegründet 2005) ist ein spezialisierter Hersteller von Carbon-Steuerrädern und -Pinnen im Premium- und Superyacht-Segment.

#### 4.5.1 Carbonautica Steuerrad-Portfolio

| Modell | Durchmesser [mm] | Speichen | Gewicht [kg] | Besonderheit | Preis (ca.) |
|--------|-------------------|----------|--------------|--------------|-------------|
| Racing 3S | 600–900 | 3 | 1,0–2,2 | Minimalistisch, Regatta | €2.500–€4.500 |
| Racing 5S | 700–1.000 | 5 | 1,5–3,0 | Mehr Griffoptionen | €3.000–€5.500 |
| Cruising Teak | 700–1.100 | 3 oder 5 | 1,8–3,8 | Carbon + Teak-Inlays | €3.500–€6.500 |
| Cruising Leather | 700–1.100 | 3 oder 5 | 1,6–3,5 | Carbon + Leder | €4.000–€7.000 |
| Superyacht Custom | 900–1.500 | 3–6 | 2,5–6,0 | Maßanfertigung | €6.000–€25.000 |
| Tiller Straight | 800–1.400 | — | 0,2–0,6 | Carbon-Pinne gerade | €400–€1.200 |
| Tiller Swan-Neck | 800–1.400 | — | 0,3–0,8 | Carbon-Pinne gebogen | €600–€1.600 |

#### 4.5.2 Carbonautica Fertigungsverfahren

```
Autoklav-Verfahren (Pre-Preg):
  1. Carbon-Prepreg zuschneiden (CNC-Cutter)
  2. Auf Aluminium-Kern wickeln/legen
  3. Vakuumsack + Autoklav (120°C, 3 bar, 2h)
  4. Entformen, Kern entfernen
  5. CNC-Fräsen der Nabenaufnahme
  6. Teak-Inlays einpassen und verkleben (Epoxid)
  7. Klarlack (2K-PU mit UV-Filter, 3–5 Schichten)
  8. Politur (Hochglanz oder Satin-Matt)

Qualitätsmerkmale:
  - Fasergerad: ±2° Abweichung
  - Wandstärke: ±0,3 mm Toleranz
  - Oberfläche: Ra ≤ 0,2 µm (nach Politur)
  - Gewichtstoleranz: ±5%
  - Jedes Rad individuell nummeriert mit Zertifikat
```

### 4.6 Weitere Hersteller — Übersicht

#### 4.6.1 Stazo (Niederlande)

```
Spezialisierung: Edelstahl-Steuerräder, Marine-Armaturen
Gegründet: 1928
Sitz: Ridderkerk, Niederlande
Vertrieb: Europa, weltweit

Produktlinien:
  - Stazo Type 01: Classic Destroyer, SS + Teak, 600–1.100 mm
  - Stazo Type 07: Modern 3-Spoke, SS poliert, 500–900 mm
  - Stazo Type 11: Flat-Bottom Spoke, für niedrige Pedestals
  - Stazo PowerKnob: Einhand-Steuerknauf für Motoryachten
  - Stazo Pedestal: Eigene Pedestal-Linie für Motorboote

Qualitätsmerkmale: Vollständig in Europa gefertigt, 316L, Hochglanzpolitur
Preisniveau: €350–€1.200 (Räder), €800–€2.500 (Pedestals)
```

#### 4.6.2 Kobelt (Kanada)

```
Spezialisierung: Steueranlagen für Motoryachten und Arbeitsboote
Gegründet: 1962
Sitz: Surrey, British Columbia, Kanada

Produktlinien:
  - Kobelt Model 2024: Mechanische Steueranlage bis 20m
  - Kobelt Model 7004: Hydraulische Steuerung
  - Kobelt Model 2040: Elektronische Servo-Steuerung
  - Kobelt Steuerräder: SS-Destroyer 500–900 mm
  - Kobelt Joystick-Systeme

Zielmarkt: Motoryachten 8–25m, Fischereiboote, Arbeitsboote
Preisniveau: $600–$3.000 (Räder), $2.000–$15.000 (Komplettsysteme)
```

#### 4.6.3 Ultraflex / Teleflex Marine (Italien / USA)

```
Spezialisierung: Steueranlagen für Motorboote (Zahnstange, Hydraulik)
Gegründet: 1968 (Ultraflex) / 1946 (Teleflex)
Sitz: Campodarsego (IT) / Sellersville, PA (USA)
Anmerkung: 2007 durch Dometic (SeaStar Solutions) übernommen

Produktlinien Ultraflex:
  - Ultraflex V67: Mechanische Kabelsteuerung für Außenborder
  - Ultraflex HYCO: Hydraulische Steuerung für Motorboote
  - Ultraflex Steuerräder: Polyurethan, SS, 280–400 mm (Motorboot-Bereich)
  
Produktlinien SeaStar/Teleflex:
  - SeaStar Pro: Hydraulische Steuerung für Außenborder
  - SeaStar Optimus 360: Joystick + EPS (Electronic Power Steering)
  - BayStar: Hydraulische Steuerung Einstiegsbereich
  - Steuerräder: 320–400 mm, Polyurethan/SS, Motorboot-typisch

Zielmarkt: Motorboote 5–15m, Sportboote, Außenborder-Anwendungen
Preisniveau: €200–€1.500 (Räder), €500–€5.000 (Komplettsysteme)
```

---

## 5. Hersteller-Datenbank

### 5.1 Lewmar

| Feld | Daten |
|------|-------|
| **Vollständiger Name** | Lewmar Limited |
| **Sitz** | Southmoor Lane, Havant, Hampshire PO9 1JJ, UK |
| **Gegründet** | 1946 |
| **Eigentümer** | Lippert Components (USA), seit 2019 |
| **Mitarbeiter** | ca. 350 |
| **Website** | www.lewmar.com |
| **Produktbereich Steuerung** | Pedestals, Steuerräder, Quadranten, Steuerseile |
| **OEM-Kunden** | Bavaria, Hanse, Hallberg-Rassy (teilweise), Moody, Oyster |
| **Zertifizierungen** | ISO 9001, ISO 14001, Lloyd's Register |
| **Garantie** | 5 Jahre auf Structural Components |
| **Service-Netz** | Weltweit, über 60 Länder, autorisierte Service-Partner |
| **Teileverfügbarkeit** | Ersatzteile ab Lager für Modelle der letzten 20 Jahre |
| **Stärken** | Breites Sortiment, hohe Verfügbarkeit, OEM-Standard vieler Werften |
| **Schwächen** | Premium-Preis, Carbon-Bereich weniger etabliert als Spezialisten |

### 5.2 Edson International

| Feld | Daten |
|------|-------|
| **Vollständiger Name** | Edson International Inc. |
| **Sitz** | 460 Industrial Park Road, New Bedford, MA 02745, USA |
| **Gegründet** | 1859 |
| **Eigentümer** | Familienunternehmen (Will Keene, 5. Generation) |
| **Mitarbeiter** | ca. 60 |
| **Website** | www.edsonmarine.com |
| **Produktbereich Steuerung** | Steuerräder, Pedestals, Steuergetriebe, Guards, Zubehör |
| **OEM-Kunden** | Hinckley, Sabre, Morris, J/Boats, Tartan, Pacific Seacraft |
| **Zertifizierungen** | ABYC P-20 Compliance, NMMA Certified |
| **Garantie** | 10 Jahre (Structural), Lifetime auf Teak |
| **Service-Netz** | Primär Nordamerika, Vertrieb in 40+ Ländern |
| **Teileverfügbarkeit** | Ersatzteile für Modelle ab 1960 noch lieferbar |
| **Stärken** | Tradition, Qualität, US-Marktführer, exzellenter Ersatzteil-Support |
| **Schwächen** | Begrenzte Präsenz in Europa, US-Maßsystem (Inch) |

### 5.3 Jefa Steering

| Feld | Daten |
|------|-------|
| **Vollständiger Name** | Jefa Rudder & Steering Systems ApS |
| **Sitz** | Spodsbjergvej 26B, 5900 Rudkøbing, Dänemark |
| **Gegründet** | 1956 |
| **Eigentümer** | Privatunternehmen |
| **Mitarbeiter** | ca. 30 |
| **Website** | www.jefa.com |
| **Produktbereich Steuerung** | Komplette Steueranlagen, Ruderanlagen, Ruderlager, Räder |
| **OEM-Kunden** | Hallberg-Rassy, X-Yachts, Najad, Arcona, Dehler, Contest |
| **Zertifizierungen** | ISO 9001, DNV GL Type Approval |
| **Garantie** | 5 Jahre auf mechanische Komponenten |
| **Service-Netz** | Europa-fokussiert, Vertrieb weltweit |
| **Teileverfügbarkeit** | Ersatzteile für alle jemals produzierten Systeme |
| **Stärken** | Komplettsystem-Anbieter, skandinavische Qualität, direkte Werft-Zusammenarbeit |
| **Schwächen** | Kleine Firma, lange Lieferzeiten bei Custom-Anlagen |

### 5.4 Goiot

| Feld | Daten |
|------|-------|
| **Vollständiger Name** | Goiot S.A. (Groupe Alliance Marine) |
| **Sitz** | Zone Industrielle, 44210 Pornic, Frankreich |
| **Gegründet** | 1920 |
| **Eigentümer** | Alliance Marine Group |
| **Mitarbeiter** | ca. 120 (Gesamt-Gruppe) |
| **Website** | www.goiot.com |
| **Produktbereich Steuerung** | Steuerräder, Luken, Fenster, Lüfter |
| **OEM-Kunden** | Beneteau, Jeanneau, Dufour, Lagoon, Fountaine Pajot, Catana |
| **Zertifizierungen** | ISO 9001, CE-konform |
| **Garantie** | 3 Jahre |
| **Service-Netz** | Frankreich und Mittelmeer gut abgedeckt, international über Groupe Beneteau |
| **Teileverfügbarkeit** | Gute Verfügbarkeit für aktuelle Modelle, begrenzt für Altmodelle >15 Jahre |
| **Stärken** | OEM-Volumenproduzent, günstige Preise, breites Sortiment |
| **Schwächen** | Weniger Premium-Positionierung, Service außerhalb Frankreichs begrenzt |

### 5.5 Carbonautica

| Feld | Daten |
|------|-------|
| **Vollständiger Name** | Carbonautica S.r.l. |
| **Sitz** | Via dell'Artigianato 15, 31030 Casier (TV), Italien |
| **Gegründet** | 2005 |
| **Eigentümer** | Privatunternehmen |
| **Mitarbeiter** | ca. 15 |
| **Website** | www.carbonautica.com |
| **Produktbereich Steuerung** | Carbon-Steuerräder, Carbon-Pinnen, Custom-Carbon-Komponenten |
| **OEM-Kunden** | Wally, Baltic Yachts, Southern Wind, Grand Soleil, ICE Yachts |
| **Zertifizierungen** | ISO 9001, RINA Type Approval |
| **Garantie** | 5 Jahre auf Struktur, 2 Jahre auf Oberfläche |
| **Service-Netz** | Italien, Mittelmeer, weltweit über Vertriebspartner |
| **Teileverfügbarkeit** | Maßanfertigung, Nachbestellung innerhalb 4–8 Wochen |
| **Stärken** | Carbon-Spezialist, leichteste Räder am Markt, exzellente Verarbeitung |
| **Schwächen** | Nischen-Anbieter, Premium-Preise, keine Pedestals/Getriebe im Programm |

### 5.6 Stazo Marine Equipment

| Feld | Daten |
|------|-------|
| **Vollständiger Name** | Stazo Marine Equipment B.V. |
| **Sitz** | Handelsweg 12, 2988 DC Ridderkerk, Niederlande |
| **Gegründet** | 1928 |
| **Eigentümer** | Privatunternehmen |
| **Mitarbeiter** | ca. 40 |
| **Website** | www.stazo.com |
| **Produktbereich Steuerung** | Steuerräder (SS), Pedestals, Marine-Hardware |
| **OEM-Kunden** | Linssen, Aquanaut, Pedro, Vri-Jon (niederländische Motoryacht-Werften) |
| **Zertifizierungen** | ISO 9001, CE-konform |
| **Garantie** | 3 Jahre |
| **Service-Netz** | Benelux und Nordeuropa, international über Händler |
| **Teileverfügbarkeit** | Gute Lagerhaltung für Standard-Modelle |
| **Stärken** | Solide niederländische Qualität, breites Motorboot-Sortiment, faire Preise |
| **Schwächen** | Begrenzte Bekanntheit außerhalb Benelux, Segelboot-Bereich unterrepräsentiert |

### 5.7 Kobelt Manufacturing

| Feld | Daten |
|------|-------|
| **Vollständiger Name** | Kobelt Manufacturing Co. Ltd. |
| **Sitz** | 8225 130th Street, Surrey, BC V3W 7X4, Kanada |
| **Gegründet** | 1962 |
| **Eigentümer** | Privatunternehmen |
| **Mitarbeiter** | ca. 80 |
| **Website** | www.kobelt.com |
| **Produktbereich Steuerung** | Steuerungen (mechanisch, hydraulisch, elektronisch), Steuerräder, Joysticks |
| **OEM-Kunden** | Nordhavn, Grand Banks, Fleming, Kadey-Krogen (Trawler-Segment) |
| **Zertifizierungen** | ISO 9001, Transport Canada, USCG, ABS, Lloyd's |
| **Garantie** | 5 Jahre |
| **Service-Netz** | Nordamerika, weltweit über Marine-Systemintegratoren |
| **Teileverfügbarkeit** | Exzellent, eigene Fertigung, schnelle Lieferung |
| **Stärken** | Robuste Industriequalität, Komplettanbieter, exzellenter Service |
| **Schwächen** | Primär Motorboot/Arbeitsboot, keine Segel-Expertise |

### 5.8 Lecomble & Schmitt

| Feld | Daten |
|------|-------|
| **Vollständiger Name** | Lecomble & Schmitt S.A.S. |
| **Sitz** | Z.I. du Bois Joli, 85340 Olonne-sur-Mer, Frankreich |
| **Gegründet** | 1962 |
| **Eigentümer** | Privatunternehmen |
| **Mitarbeiter** | ca. 50 |
| **Website** | www.lecomble-schmitt.com |
| **Produktbereich Steuerung** | Hydraulische Steueranlagen, Autopiloten, Antriebssteuerungen |
| **OEM-Kunden** | Beneteau, Jeanneau, Lagoon (Hydraulik-Systeme) |
| **Zertifizierungen** | ISO 9001, Bureau Veritas, RINA |
| **Garantie** | 3 Jahre |
| **Stärken** | Hydraulik-Spezialist, OEM für große französische Werften |
| **Schwächen** | Keine eigenen Steuerräder, reiner Systemanbieter |

---

## 6. Fehlerbild-Atlas

### 6.1 Fehlerbild: Totgang / Spiel im Steuerrad

```
Fehlerbild-ID:     FB-20.04-001
Bezeichnung:        Totgang / Spiel im Steuerrad (Steering Play / Backlash)
Schweregrad:        MITTEL bis HOCH (je nach Ausmaß)
Bootsklassen:       Alle mit Radsteuerung

Symptome:
  - Steuerrad dreht 5–30° ohne Ruderreaktion
  - Rudergänger muss "über den Totgang hinweg" drehen
  - Kurs wird unruhig, Autopilot-Probleme (ständige Korrekturen)

Mögliche Ursachen:
  1. Seilzug zu lose        → Spannen über Spannschrauben
  2. Seil gelängt (Dehnung) → Seil ersetzen
  3. Kette verschlissen     → Kette + Kettenrad prüfen/ersetzen
  4. Schneckengetriebe verschlissen → Getriebe-Inspektion, ggf. Austausch
  5. Quadrant-Verbindung lose       → Klemmbolzen nachziehen
  6. Ruderlager ausgeschlagen       → Ruderlager prüfen (siehe 20.03)
  7. Universalgelenk (bei Twin)     → Verschleiß der Zwischenwelle-Lager

Prüfmethode:
  1. Ruder am Ruderblatt fixieren (Helfer hält am Heck)
  2. Steuerrad langsam drehen, dabei Spiel messen
  3. Akzeptabel: <5° am Rad (= ca. 1–2° am Ruder)
  4. Grenzwert: >10° am Rad → Ursachenforschung

Fotodokumentation (AYDI Visual):
  - Nahaufnahme Kettenrad/Seilverbindung
  - Quadrant-Klemmung
  - Seilspannung (Durchhang sichtbar?)

Confidence: measured (bei physischer Prüfung), visual_medium (bei Fotoanalyse)
```

### 6.2 Fehlerbild: Schwergängigkeit

```
Fehlerbild-ID:     FB-20.04-002
Bezeichnung:        Schwergängigkeit des Steuerrades (Stiff Steering)
Schweregrad:        MITTEL
Bootsklassen:       Alle mit Radsteuerung

Symptome:
  - Steuerrad erfordert ungewöhnlich hohe Kraft zum Drehen
  - Asymmetrisch: In eine Richtung schwerer als in die andere
  - Knirschende oder kratzende Geräusche

Mögliche Ursachen:
  1. Seilzug zu stramm gespannt      → Spannung reduzieren
  2. Seil geknickt / gebrochen       → Seil ersetzen (Litzenbruch)
  3. Umlenkrollen festgesessen       → Lager schmieren oder Rolle ersetzen
  4. Schneckengetriebe trocken       → Schmieren (Getriebefett, NICHT WD-40)
  5. Ruderlager korrodiert/verquollen→ Ruderlager prüfen (siehe 20.03)
  6. Ruderblatt blockiert (Fremdkörper, Bewuchs) → Unterwasser prüfen
  7. Pedestal-Lager trocken          → Schmieren (PTFE-Fett)
  8. Kette verrostet                  → Kette erneuern, Edelstahl-Kette verwenden

Prüfmethode:
  1. Ruder komplett freidrehen (Boot an Land oder im Wasser)
  2. Rad drehen — ist es am Rad oder am Ruder schwergängig?
  3. Seil aushängen → Rad separat drehen (nur Getriebe prüfen)
  4. Ruder ohne Steueranlage drehen (nur Ruderlager prüfen)

Confidence: measured (bei physischer Prüfung), visual_low (visuell kaum beurteilbar)
```

### 6.3 Fehlerbild: Korrosion am Steuerrad

```
Fehlerbild-ID:     FB-20.04-003
Bezeichnung:        Korrosion am Steuerrad (Wheel Corrosion)
Schweregrad:        NIEDRIG bis MITTEL (kosmetisch bis strukturell)
Bootsklassen:       Alle

Symptome:
  - Braune Flecken (Tea Staining) auf Edelstahl
  - Lochfraß (Pitting) an Schweißnähten
  - Weiße Pulver-Ablagerungen (Aluminium-Korrosion)
  - Schwarze Flecken an Teak-Edelstahl-Übergängen

Mögliche Ursachen:
  1. Material nicht 316L sondern 304       → Austausch
  2. Spaltkorrosion an Übergängen          → Abdichten, Redesign
  3. Kontamination (Normalstahl-Werkzeug)  → Beizen + Passivieren
  4. Salzablagerungen (nicht regelmäßig gespült) → Regelmäßige Süßwasserspülung
  5. Galvanische Korrosion (Al-SS Kontakt) → Isolation, Opferanoden
  6. Gerbsäure-Reaktion Eiche-SS           → Teak verwenden statt Eiche

Prüfmethode:
  1. Visuelle Inspektion: Nahaufnahme aller Schweißnähte und Übergänge
  2. Magnettest: 316L ist nicht-magnetisch (Ausnahme: kaltverformt)
  3. Tropfentest: Molybdän-Schnelltest für 316 vs 304 (z.B. Koslow N-75)

Fotodokumentation (AYDI Visual):
  - Nahaufnahmen der Korrosionsstellen
  - Übersicht des gesamten Rades
  - Detailaufnahme Schweißnähte
  - Übergang Teak/Metall

Confidence: visual_high (Korrosion gut fotografisch erkennbar)
```

### 6.4 Fehlerbild: Teak-Degradation am Steuerrad

```
Fehlerbild-ID:     FB-20.04-004
Bezeichnung:        Teak-Degradation am Steuerrad
Schweregrad:        NIEDRIG (kosmetisch) bis MITTEL (Griffigkeit)
Bootsklassen:       Alle mit Teak-Griffen

Symptome:
  - Silbergraue Verfärbung (UV-Vergrauung)
  - Schwarze Flecken (Schimmel oder Gerbsäure)
  - Rissbildung (Checks) entlang der Faser
  - Raue, splittrige Oberfläche
  - Loslösung der Teak-Segmente vom Radkranz

Mögliche Ursachen:
  1. Fehlende UV-Pflege (kein Öl, kein Schutz)     → Reinigen + Ölen
  2. Extremer Sonneneinsatz ohne Bimini/Abdeckung   → Radabdeckung verwenden
  3. Schimmelbefall durch stehende Feuchtigkeit      → Fungizid, trocknen, ölen
  4. Teak-Qualität minderwertig (Plantagenholz)      → Austausch bei Bedarf
  5. Klebung versagt (Segment löst sich)             → Nachkleben (Epoxid)
  6. Schrauben der Segmente korrodiert               → Edelstahl-Schrauben ersetzen

Prüfmethode:
  1. Visuell: Farbe, Oberflächenzustand, Rissmuster
  2. Tastprobe: Glatt (OK) vs. rau/splittrig (Pflege nötig)
  3. Klopfprobe: Hohl/dumpf → Segment gelöst, fest/hell → gut verklebt
  4. Feuchtemessung: Holzfeuchte >20% → Trocknungsbedarf

Fotodokumentation (AYDI Visual):
  - Makroaufnahme der Teak-Oberfläche
  - Detailaufnahme Risse und Verfärbungen
  - Übergangsstelle Teak-Metall

Confidence: visual_high (Teak-Zustand gut visuell beurteilbar)
```

### 6.5 Fehlerbild: Seilzugbruch / Kettenbruch

```
Fehlerbild-ID:     FB-20.04-005
Bezeichnung:        Seilzug- oder Kettenbruch (Cable/Chain Failure)
Schweregrad:        KRITISCH (Steuerungsverlust)
Bootsklassen:       Alle mit Seilzug-/Kettensteuerung

Symptome:
  - Plötzlicher Steuerungsverlust
  - Steuerrad dreht frei (kein Widerstand)
  - Metallisches Klirren/Rasseln im Pedestal

Mögliche Ursachen:
  1. Seil-Ermüdungsbruch (Litzenbruch → Totalversagen)
  2. Kette verschlissen, Bolzen ausgeschlagen
  3. Spannschloss versagt (Gewinde gerissen)
  4. Umlenkrolle gebrochen → Seil entgleist
  5. Seil-Endklemme versagt (Presshülse, Spleiß)

Prävention:
  1. Jährliche Sichtprüfung des kompletten Seilzugs
  2. Handprobe: Seil über die Finger ziehen → Litzenbruch spürbar (Piekser)
  3. Seil-Lebensdauer: max. 10 Jahre oder bei erstem Litzenbruch ersetzen
  4. Kette: bei sichtbarem Verschleiß (Längung >2%) ersetzen
  5. Spannschrauben: Schraubensicherung (Loctite 243 oder Kontermutter)

NOTMASSNAHME bei Seilbruch:
  → Notpinne montieren (muss an Bord sein!)
  → ISO 8847 schreibt Notsteuerung vor

Confidence: measured (bei Inspektion), visual_medium (bei Foto des Seilzugs)
```

### 6.6 Fehlerbild: Pedestal-Undichtigkeit

```
Fehlerbild-ID:     FB-20.04-006
Bezeichnung:        Wasser-Eintritt am Pedestal-Durchbruch
Schweregrad:        MITTEL (Feuchtigkeitsschaden, Korrosion unter Deck)
Bootsklassen:       Alle mit Radsteuerung und Cockpit-Pedestal

Symptome:
  - Feuchtigkeit/Wasserflecken unter der Cockpit-Sole am Pedestal
  - Korrosion an Befestigungsschrauben
  - Schimmelgeruch aus dem Achterraum

Mögliche Ursachen:
  1. Dichtring am Flansch defekt/veraltet   → Neuen Dichtring einsetzen
  2. Dichtstoff (Sikaflex etc.) gerissen     → Alten Dichtstoff entfernen, neu abdichten
  3. Schrauben lose (thermische Bewegung)    → Nachziehen + Dichtstoff
  4. GFK-Kante am Durchbruch nicht versiegelt → Epoxid-Versiegelung nachholen
  5. Pedestal-Gehäuse gerissen               → Schweißen oder Austausch

Prüfmethode:
  1. Wasser auf Cockpit-Sole → unter Deck auf Eintritt prüfen
  2. Schrauben-Festigkeit prüfen (Drehmoment-Kontrolle)
  3. Dichtstoff-Zustand visuell beurteilen (Risse, Ablösung)

Confidence: visual_medium (feuchte Stellen erkennbar), measured (bei Wassertest)
```

### 6.7 Fehlerbild: Leder-Degradation

```
Fehlerbild-ID:     FB-20.04-007
Bezeichnung:        Leder-Degradation am Steuerrad (Leather Deterioration)
Schweregrad:        NIEDRIG (kosmetisch/Komfort)
Bootsklassen:       Yachten mit Leder-Umwicklung

Symptome:
  - Ausbleichung (UV-Farbverlust)
  - Verhärtung und Rissbildung
  - Naht löst sich auf
  - Schimmelflecken (grünlich-weiß)
  - Klebrigkeit bei Hitze

Mögliche Ursachen:
  1. UV-Exposition ohne Abdeckung    → Bimini/Radcover verwenden
  2. Fehlende Lederpflege            → 3-monatlich pflegen (Leder-Balsam)
  3. Salzwasser-Exposition           → Süßwasser-Spülung nach jedem Segeltag
  4. Tropisches Klima (Feuchtigkeit) → Belüftung sicherstellen, Anti-Schimmel-Mittel
  5. Minderwertige Lederqualität     → Bei Austausch auf Marine-Grade achten

Lebensdauer Leder-Umwicklung:
  - Mediterran (intensiv genutzt): 2–4 Jahre
  - Nordeuropa (saisonal):         4–8 Jahre
  - Mit Abdeckung und Pflege:      6–12 Jahre

Confidence: visual_high (Leder-Zustand exzellent visuell beurteilbar)
```

### 6.8 Fehlerbild: Knacken/Knarren bei Ruderlage

```
Fehlerbild-ID:     FB-20.04-008
Bezeichnung:        Geräusche beim Steuern (Knacken, Knarren, Quietschen)
Schweregrad:        NIEDRIG bis MITTEL (Verschleißindikator)
Bootsklassen:       Alle

Symptome:
  - Knackendes Geräusch bei Richtungswechsel
  - Kontinuierliches Knarren während des Steuerns
  - Quietschen bei bestimmten Ruderwinkeln
  - Ruckartiges Ruder (Stick-Slip-Effekt)

Mögliche Ursachen:
  1. Kette auf Kettenrad: Verschlissene Glieder → Kette + Kettenrad prüfen
  2. Schneckengetriebe: Trockenlauf → Schmieren (Spezialfett)
  3. Umlenkrollen: Lager trocken → Schmieren oder ersetzen
  4. Ruderlager: Buchse verschlissen → Ruderlager erneuern (siehe 20.03)
  5. Pedestal-Lager: Trocken → Schmieren
  6. Quadrant-Klemmung: Lose → Nachziehen
  7. Holzpinne im Ruderkopf: Holz quillt/schwindet → Buchse einsetzen

Prüfmethode:
  Stethoskop-Methode: Schraubendreher auf verschiedene Komponenten halten,
  Geräusch-Quelle lokalisieren.

Confidence: visual_low (Geräusche nicht visuell diagnostizierbar), documented (bei Bericht)
```

### 6.9 Fehlerbild: Fehlausrichtung Rad-zu-Ruder

```
Fehlerbild-ID:     FB-20.04-009
Bezeichnung:        Fehlausrichtung Steuerrad zu Ruderblatt (Misalignment)
Schweregrad:        NIEDRIG (Komfort) bis MITTEL (Sicherheit bei Nacht)
Bootsklassen:       Alle mit Radsteuerung

Symptome:
  - Ruder steht gerade, aber Speiche zeigt nicht nach oben (bei 5-Spoke)
  - Geradeauskurs erfordert dauerhaft leicht gedrehtes Rad
  - Ruderlage-Anzeige (falls vorhanden) stimmt nicht mit Radposition überein

Mögliche Ursachen:
  1. Rad falsch aufgesetzt (Kerbverzahnung um einen Zahn versetzt)
  2. Quadrant nicht mittig auf Ruderschaft
  3. Seil gerutscht (Endklemme hat nachgegeben)
  4. Schneckengetriebe nicht auf Mittellage eingestellt
  5. Ruder tatsächlich nicht gerade (Ruder verbogen, Lager verschoben)

Korrektur:
  1. Ruder auf gerade Mittellage stellen (Helfer am Ruderblatt)
  2. Rad lösen (Kerbverzahnung)
  3. Rad in gewünschte Position drehen (Referenzspeiche oben)
  4. Rad wieder aufsetzen und festziehen
  5. Probefahrt: Geradeauslauf prüfen

Confidence: visual_medium (Speichenposition im Foto erkennbar)
```

### 6.10 Fehlerbild: Pinnenverlängerung-Gelenk defekt

```
Fehlerbild-ID:     FB-20.04-010
Bezeichnung:        Defektes Gelenk der Pinnenverlängerung
Schweregrad:        NIEDRIG (Komfort) bis MITTEL (Steuerungsverlust bei Regatta)
Bootsklassen:       Segelboote mit Pinne

Symptome:
  - Verlängerung hängt schlaff herunter (Gelenk ohne Widerstand)
  - Verlängerung blockiert (Gelenk festgegangen)
  - Gelenk bricht (Kugelkopf löst sich)
  - Exzessives Spiel im Gelenk

Mögliche Ursachen:
  1. Gummi-Gelenk gealtert (UV, Kälte)     → Ersetzen (alle 2–3 Saisons)
  2. Kugelkopf verschlissen                  → Ersetzen
  3. Federclip fehlt/gebrochen               → Sicherung ersetzen
  4. Korrosion am Gelenk-Bolzen              → Bolzen ersetzen, SS verwenden
  5. Überbelastung (Sturz auf Verlängerung)  → Komplettaustausch

Confidence: visual_medium (Gelenkzustand teils sichtbar)
```

### 6.11 Fehlerbild: Carbon-Delamination an Steuerrad/Pinne

```
Fehlerbild-ID:     FB-20.04-011
Bezeichnung:        Carbon-Delamination (CFK-Ablösung)
Schweregrad:        MITTEL bis HOCH (strukturelle Schwächung)
Bootsklassen:       Yachten mit Carbon-Steuerrad oder -Pinne

Symptome:
  - Sichtbare weiße Linien (Faserablösung) unter der Klarlackschicht
  - Hohles Klopfgeräusch an betroffener Stelle
  - Oberfläche leicht erhaben (Blase)
  - Klarlack-Risse mit Feuchtigkeitseintritt

Mögliche Ursachen:
  1. Schlagbelastung (Werkzeug, Schotende, Anlegemanöver)
  2. UV-Degradation des Harzsystems (mangelhafter UV-Schutz)
  3. Feuchtigkeit + Frost (Wasser in Mikroriss → Eisbildung → Delamination)
  4. Fertigungsdefekt (Lufteinschlüsse, unzureichende Aushärtung)

Prüfmethode:
  1. Klopftest: Gesund = hell/hart, delaminiert = dumpf/hohl
  2. Visuelle Inspektion mit Lupe: Haarrisse, Faserverlauf-Störungen
  3. Instrumentell: Ultraschall (bei Verdacht auf großflächige Delamination)

Reparatur:
  - Kleine Stelle (<20mm): Klarlack entfernen, Epoxid injizieren, neu lackieren
  - Große Stelle (>20mm): An Hersteller senden oder Carbon-Fachbetrieb
  - Strukturell kritisch: Austausch empfohlen

Confidence: visual_medium (sichtbare Anzeichen teils erkennbar), measured (bei Klopf-/Ultraschalltest)
```

### 6.12 Fehlerbild: Pinne gebrochen / gerissen

```
Fehlerbild-ID:     FB-20.04-012
Bezeichnung:        Pinnenbruch oder -riss
Schweregrad:        KRITISCH (Steuerungsverlust)
Bootsklassen:       Segelboote mit Pinne

Symptome:
  - Pinne bricht ab (meist am Ansatz / Ruderkopf-Klemmung)
  - Sichtbarer Riss im Holz oder Carbon
  - Pinne "weich" / biegeschlaff (innere Faser gebrochen)

Mögliche Ursachen:
  1. Holz: Kurzfasriger Bereich (Asteinschluss, Faserverlauf quer)
  2. Holz: Alterung, UV-Degradation, Feuchtigkeitsschäden
  3. Carbon: Schlagschaden, Delamination, Fertigungsdefekt
  4. Aluminium: Ermüdungsriss (zyklische Belastung über Jahre)
  5. Überlast: Böe bei blockiertem Ruder, Person steht auf Pinne
  6. Korrosion am Befestigungspunkt (Holz-in-Metall-Verbindung)

Prävention:
  1. Jährliche Sichtprüfung des Pinnenansatzes
  2. Bei Holzpinnen: Oberfläche pflegen (Rissbildung verhindern)
  3. Ersatzpinne an Bord haben (ISO 8847 → Notsteuerung)
  4. Kein Sitzen oder Stehen auf der Pinne

NOTMASSNAHME bei Pinnenbruch:
  → Notpinne montieren (stets mitgeführt!)
  → Behelfsmäßig: Rohrlänge oder Schraubenschlüssel auf Ruderkopf klemmen

Confidence: visual_high (Bruch/Riss klar erkennbar), measured (bei Materialprüfung)
```

---

## 7. Troubleshooting-Entscheidungsbäume

### 7.1 Entscheidungsbaum: Steuerrad hat Spiel

```
START: Steuerrad hat Spiel (Totgang)
│
├─ Wie viel Spiel?
│  ├─ <5° am Rad → AKZEPTABEL (beobachten, jährlich prüfen)
│  ├─ 5–15° am Rad → HANDLUNGSBEDARF
│  │  │
│  │  ├─ Ruder fixieren (Helfer am Heck), Spiel am Rad messen
│  │  │
│  │  ├─ Seil aushängen → dreht Rad immer noch frei?
│  │  │  ├─ JA → Getriebe-Problem
│  │  │  │  ├─ Schneckengetriebe → Fachservice (Getriebe-Austausch)
│  │  │  │  └─ Seilkettenrad → Kettenrad prüfen, Kette prüfen
│  │  │  │
│  │  │  └─ NEIN → Problem in Seil/Kette/Quadrant
│  │  │     ├─ Seil prüfen: zu lose?
│  │  │     │  ├─ JA → Spannschrauben nachstellen
│  │  │     │  └─ NEIN → weiter
│  │  │     │
│  │  │     ├─ Seil auf Litzenbruch prüfen
│  │  │     │  ├─ Litzenbruch gefunden → SEIL ERSETZEN
│  │  │     │  └─ NEIN → weiter
│  │  │     │
│  │  │     ├─ Quadrant-Klemmung prüfen
│  │  │     │  ├─ Lose → Klemmbolzen nachziehen
│  │  │     │  └─ Fest → weiter
│  │  │     │
│  │  │     └─ Umlenkrollen prüfen
│  │  │        ├─ Rolle dreht sich frei (Lager ausgeschlagen) → ROLLE ERSETZEN
│  │  │        └─ Rollen OK → Ruderlager prüfen (→ 20.03)
│  │  │
│  └─ >15° am Rad → SOFORTIGER HANDLUNGSBEDARF
│     └─ Komplette Steueranlage inspizieren (alle obigen Punkte)
│        └─ Bis zur Reparatur: Notpinne bereithalten
│
ENDE
```

### 7.2 Entscheidungsbaum: Steuerrad schwergängig

```
START: Steuerrad schwergängig
│
├─ Seit wann?
│  ├─ Plötzlich → AKUTE URSACHE
│  │  ├─ Ruder blockiert? (Fremdkörper, Grundberührung)
│  │  │  ├─ JA → Unterwasser prüfen, Fremdkörper entfernen
│  │  │  └─ NEIN → weiter
│  │  │
│  │  ├─ Seil eingeklemmt / verknotet?
│  │  │  ├─ JA → Seil frei machen / ersetzen
│  │  │  └─ NEIN → weiter
│  │  │
│  │  └─ Kette von Kettenrad gesprungen?
│  │     ├─ JA → Kette wieder auflegen, Spannung prüfen
│  │     └─ NEIN → Ruderlager prüfen (→ 20.03)
│  │
│  ├─ Schleichend (über Wochen/Monate) → VERSCHLEISS
│  │  ├─ Seil isoliert prüfen (aushängen)
│  │  │  ├─ Rad dreht leicht ohne Seil → Problem im Seilzug
│  │  │  │  ├─ Umlenkrollen schmieren/ersetzen
│  │  │  │  ├─ Seil auf Knicke prüfen
│  │  │  │  └─ Seilspannung reduzieren (falls zu stramm)
│  │  │  │
│  │  │  └─ Rad dreht auch ohne Seil schwer → Getriebe/Pedestal
│  │  │     ├─ Pedestal-Lager schmieren (PTFE-Fett)
│  │  │     ├─ Getriebe schmieren (Zahnradfett)
│  │  │     └─ Falls keine Besserung → Fachservice
│  │  │
│  │  └─ Asymmetrisch (eine Richtung schwerer)?
│  │     ├─ JA → Umlenkrolle auf einer Seite defekt
│  │     │       oder Seil auf einer Seite eingeklemmt
│  │     └─ NEIN → Allgemeiner Verschleiß
│  │
│  └─ Saisonal (nach Winterlager) → KORROSION/FESTSITZEN
│     ├─ Alles durchschmieren
│     ├─ Seil bewegen (durch Umlenkrollen ziehen)
│     └─ Ruderlager lösen (Ruder von Hand drehen)
│
ENDE
```

### 7.3 Entscheidungsbaum: Steuerrad-Auswahl für Neubau/Nachrüstung

```
START: Steuerrad-Auswahl
│
├─ Bootslänge (LOA)?
│  ├─ <8m → PINNE EMPFOHLEN (Steuerrad nur bei speziellem Wunsch)
│  │
│  ├─ 8–10m → Einzelrad ODER Pinne
│  │  ├─ Einsatz?
│  │  │  ├─ Regatta → Pinne (schnelleres Feedback, leichter)
│  │  │  ├─ Fahrt → Rad (Komfort, Autopilot-Anbindung)
│  │  │  └─ Gemischt → Persönliche Präferenz
│  │  ├─ Rad-Durchmesser: 600–800 mm
│  │  └─ Typ: Destroyer 3-Spoke oder 5-Spoke
│  │
│  ├─ 10–13m → Einzelrad ODER Doppelrad
│  │  ├─ Cockpit-Breite >2.200mm → Doppelrad möglich
│  │  ├─ Cockpit-Breite <2.200mm → Einzelrad
│  │  ├─ Rad-Durchmesser: 800–1.000 mm
│  │  └─ Budget: Einzelrad ab €800, Doppelrad ab €2.500 (komplett)
│  │
│  ├─ 13–16m → DOPPELRAD EMPFOHLEN
│  │  ├─ Rad-Durchmesser: 900–1.100 mm
│  │  ├─ Steuerung: Seilzug oder Hydraulik
│  │  └─ Hydraulik bei LOA >14m empfohlen
│  │
│  └─ >16m → DOPPELRAD + HYDRAULIK
│     ├─ Rad-Durchmesser: 1.000–1.400 mm
│     ├─ Power-Assist oder Voll-Hydraulik
│     └─ Joystick-Ergänzung für Hafenmanöver
│
├─ Material-Wahl?
│  ├─ Budget → All-Stainless (Goiot Atlantique, ab €350)
│  ├─ Standard → SS + Teak (Lewmar Corsair/Commodore, €600–€1.000)
│  ├─ Performance → Carbon (Carbonautica, Edson Talon, €2.500–€5.000)
│  └─ Luxus → SS + Leder oder Carbon + Teak (€1.500–€7.000)
│
├─ Naben-Kompatibilität prüfen!
│  ├─ Lewmar-Pedestal → Lewmar-Nabe (1:10 Konus, Kerbverzahnung)
│  ├─ Edson-Pedestal → Edson-Nabe (1:10 Konus, 13-Zahn)
│  ├─ Jefa-Pedestal → Jefa-Nabe (kompatibel mit Lewmar durch Adapter)
│  └─ Whitlock-Pedestal → Whitlock-Nabe (Adapter für Lewmar/Edson verfügbar)
│
ENDE
```

### 7.4 Entscheidungsbaum: Pinne vs. Steuerrad (Upgrade-Entscheidung)

```
START: Pinne zu Steuerrad umrüsten?
│
├─ Warum Umrüstung gewünscht?
│  ├─ Ruderdruck zu hoch (Böen, Langfahrt)
│  │  ├─ Ruderdruck >80N Dauer → Rad sinnvoll
│  │  ├─ Ruderdruck 50–80N → Windfahnensteuerung oder Tillerpilot prüfen
│  │  └─ Ruderdruck <50N → Pinne beibehalten, Ergonomie optimieren
│  │
│  ├─ Autopilot gewünscht
│  │  ├─ Budget-Option: Tillerpilot an Pinne (€600–€1.500)
│  │  └─ Komfort-Option: Radpilot oder Hydraulik-Autopilot (€2.000–€8.000)
│  │
│  ├─ Cockpit-Platz (Pinne blockiert)
│  │  ├─ Pinnenlänge reduzieren möglich? → Kürzere Pinne + Verlängerung
│  │  ├─ Klapp-Pinne möglich? → Scharnier-Lösung am Ruderkopf
│  │  └─ Grundsätzlich zu eng → Radsteuerung als Lösung
│  │
│  └─ Optik / Wiederverkaufswert
│     └─ In der Regel kein ausreichender Grund für Umbau
│
├─ Machbarkeits-Check:
│  ├─ Ruderkopf zugänglich für Quadrant? → JA/NEIN
│  ├─ Platz für Pedestal auf Cockpit-Sole? → JA/NEIN
│  ├─ Weg für Steuerseil durch Rumpf? → JA/NEIN
│  ├─ Cockpit-Sole tragfähig für Pedestal? → JA (ggf. verstärken)/NEIN
│  │
│  ├─ Alle JA → Umbau möglich, Budget: €2.000–€6.000
│  └─ Ein oder mehr NEIN → Fachberatung nötig, ggf. unwirtschaftlich
│
ENDE
```

### 7.5 Entscheidungsbaum: Notsteuerung

```
START: Steuerungsverlust auf See
│
├─ Art des Versagens?
│  ├─ Seil/Kette gerissen (Rad dreht frei)
│  │  ├─ Notpinne an Bord?
│  │  │  ├─ JA → Notpinne montieren
│  │  │  │  ├─ Ruderkopf-Zugang freilegen (Cockpit-Bodenplatte)
│  │  │  │  ├─ Notpinne auf Ruderkopf stecken
│  │  │  │  ├─ Klemm-/Steckbolzen sichern
│  │  │  │  └─ Mit Notpinne steuern (gegenläufig!)
│  │  │  │
│  │  │  └─ NEIN → Behelfslösung
│  │  │     ├─ Langen Schraubenschlüssel auf Ruderkopf setzen
│  │  │     ├─ Festbinden (Leinen, Kabelbinder)
│  │  │     └─ Segel-Trimm zum Steuern nutzen (Vorsegelschot)
│  │  │
│  │  └─ Kann Seil provisorisch repariert werden?
│  │     ├─ Seil gerissen → Enden verbinden (Drahtseilklemmen, Bordwerkzeug)
│  │     └─ Kette → Kettenschloss als Notreparatur
│  │
│  ├─ Ruderblatt verloren / Ruderschaft gebrochen
│  │  ├─ Notruder vorhanden? (z.B. Hasler-System, Aries)
│  │  │  ├─ JA → Notruder montieren
│  │  │  └─ NEIN → Behelfsruder
│  │  │     ├─ Paddel oder Spinnakerbaum als Ruder
│  │  │     ├─ Schleppbremse (Drogue) zum Steuern
│  │  │     └─ Segel-Steuerung (Besegelung asymmetrisch trimmen)
│  │  │
│  │  └─ Hafen/Hilfe erreichbar? → MAYDAY/PAN-PAN
│  │
│  ├─ Hydraulik-Versagen (Leckage)
│  │  ├─ Leck identifizieren und abdichten (Klebeband, Epoxid-Knete)
│  │  ├─ Hydrauliköl nachfüllen
│  │  ├─ Falls nicht reparierbar → Bypass-Ventil öffnen (falls vorhanden)
│  │  │  └─ Mit Bypass: Ruder frei → Notpinne
│  │  └─ Autopilot abschalten (pumpt Öl aus)
│  │
│  └─ Pinne gebrochen
│     ├─ Ersatz-Pinne an Bord?
│     │  ├─ JA → Montieren
│     │  └─ NEIN → Behelf (Schraubenschlüssel, Rohr, Bootshaken)
│     └─ Bruchstück lang genug → mit Schlauchschellen / Leinen schienen
│
├─ Sofortmaßnahmen (parallel):
│  ├─ Segel bergen (Fahrt aus dem Boot nehmen)
│  ├─ Position feststellen
│  ├─ Crew informieren
│  ├─ Wenn nötig: PAN-PAN auf Kanal 16
│  └─ AIS-SART aktivieren (falls vorhanden)
│
ENDE
```

---

## 8. FAQ

### 8.1 Grundlagen

**F1: Ab welcher Bootslänge sollte man vom Pinne auf Steuerrad umsteigen?**
A: Eine feste Grenze gibt es nicht. Als Faustregel gilt: Ab 9–10m LOA bei Fahrtenyachten wird ein Steuerrad komfortabler, da die Ruderdrücke bei Starkwind 80–120N überschreiten können. Viele erfahrene Segler fahren aber Boote bis 12m problemlos mit Pinne. Entscheidend sind Bootstyp (breites Heck = höherer Ruderdruck), Besegelung und persönliche Vorliebe.

**F2: Was ist der ideale Steuerrad-Durchmesser für mein Boot?**
A: Pauschal: LOA in Fuß × 25mm ergibt einen guten Ausgangswert. Für eine 38-Fuß-Yacht: 38 × 25 = 950mm, also ein 900 oder 1.000mm-Rad. Ergänzend sollten Cockpit-Abmessungen, Sichtlinien und persönliche Vorlieben berücksichtigt werden.

**F3: Warum haben manche Yachten zwei Steuerräder?**
A: Das Doppelrad ermöglicht eine freie Passage in der Cockpit-Mitte und erlaubt dem Rudergänger, auf der Luvseite zu steuern (bessere Sicht auf die Segel, weniger Krängungseffekt). Seit den 2000er Jahren ist dies Standard auf Fahrtenyachten ab 12–13m.

**F4: Was bedeutet "Lock-to-Lock"?**
A: Lock-to-Lock bezeichnet die Anzahl der vollen Radumdrehungen von maximalem Ruderausschlag links bis maximalem Ausschlag rechts. Typische Werte: 2,5–3,5 Umdrehungen bei Segelyachten. Weniger Umdrehungen = schnelleres Ansprechen, aber höhere Kräfte.

**F5: Kann ich mein Steuerrad selbst austauschen?**
A: Ja, sofern das neue Rad die gleiche Nabenbohrung und Kerbverzahnung hat. Lewmar-Räder passen auf Lewmar-Pedestals, Edson auf Edson usw. Bei Kreuzkompatibilität Adapter prüfen. Rad aufsetzen, Konusmutter anziehen (Anzugsmoment beachten), Ausrichtung prüfen.

### 8.2 Material und Pflege

**F6: Teak oder Leder am Steuerrad — was ist besser?**
A: Teak bietet besseren Nassgriff und Temperaturkomfort (wird nicht heiß/kalt). Leder bietet bessere Haptik trocken und ein eleganteres Erscheinungsbild. Teak ist pflegeleichter (jährlich ölen), Leder braucht 3–4× pro Jahr Pflege. Für Blauwasser-Segler: Teak. Für Mittelmeer-Cruiser: Geschmackssache. Für Superyachten: Oft Leder.

**F7: Wie pflege ich Teak-Griffe am Steuerrad?**
A: 1. Reinigen mit Teak-Reiniger (z.B. Star Brite). 2. Leicht anschleifen (Korn 220–320). 3. Teak-Öl auftragen (2–3 Schichten, z.B. Semco, Boracol). 4. 24h trocknen lassen. Frequenz: 2–3× pro Saison im Mittelmeer, 1–2× in Nordeuropa.

**F8: Mein Carbon-Steuerrad hat weiße Stellen unter dem Klarlack. Was ist das?**
A: Wahrscheinlich eine beginnende Delamination oder UV-Degradation des Harzes. Kleine Stellen können durch Nachschleifen und Neulackierung behoben werden. Größere Bereiche sollten vom Hersteller oder einem Carbon-Fachbetrieb beurteilt werden. Bis zur Reparatur: Feuchtigkeitseintritt durch Folie oder Tape verhindern.

**F9: Kann ich ein Edelstahl-Rad in der Spülmaschine reinigen?**
A: Nein. Die Kombination aus Reinigungsmittel, Hitze und dem Mischmetall-Kontakt (Spülmaschine ist oft Normalstahl) kann Korrosion auslösen. Am besten: Süßwasser + mildes Spülmittel + weiches Tuch. Für hartnäckige Salzflecken: Edelstahlreiniger (z.B. Wichard Wichinox).

**F10: Was kostet eine Neuleder-Umwicklung meines Steuerrades?**
A: Bei einem spezialisierten Segelmacher oder Polsterer: €400–€1.200 inkl. Material und Arbeit, je nach Raddurchmesser und Lederqualität. Selbstmachen ist möglich (Leder + gewachstes Segelgarn, YouTube-Anleitungen), Ergebnis aber oft weniger haltbar.

### 8.3 Technik und Installation

**F11: Mein Steuerrad hat 10° Spiel. Ist das gefährlich?**
A: 10° am Rad entsprechen typisch 2–4° am Ruder. Das ist noch nicht gefährlich, aber beeinträchtigt die Steuergenauigkeit und erhöht den Autopilot-Stromverbrauch. Ursache finden (Seil, Getriebe, Quadrant) und beheben. Ab 15° am Rad: dringend handeln.

**F12: Wie oft sollte die Steueranlage gewartet werden?**
A: Jährlich zu Saisonbeginn: Alle Verbindungen auf Spiel prüfen, Seil auf Litzenbruch prüfen (Handprobe), Getriebe und Lager schmieren, Seilspannung kontrollieren. Alle 5 Jahre: Steuerseil erneuern (auch wenn es gut aussieht). Alle 10 Jahre: Komplett-Inspektion durch Fachbetrieb.

**F13: Kann ich eine hydraulische Steuerung nachrüsten?**
A: Ja, das ist ein gängiges Upgrade. Benötigt: Hydraulikpumpe (Helm Pump) am Pedestal, Hydraulikleitungen (Kupfer oder Nylon), Hydraulikzylinder am Ruderquadrant oder direkt am Ruderschaft. Budget: €2.000–€5.000 inkl. Installation. Vorteil: Kein Totgang, einfache Autopilot-Integration. Fachbetrieb empfohlen.

**F14: Was ist eine Notpinne und muss ich eine an Bord haben?**
A: Eine Notpinne (Emergency Tiller) ist ein Hebelarm, der direkt auf den Ruderkopf gesteckt wird, falls die Hauptsteuerung ausfällt. ISO 8847 und die CE-Konformität verlangen eine funktionsfähige Notsteuerung. Bei Radsteuerungen muss der Ruderkopf zugänglich sein und die Notpinne an Bord mitgeführt werden.

**F15: Mein Pedestal wackelt. Was tun?**
A: 1. Befestigungsschrauben prüfen (Drehmoment-Kontrolle: M10=35–45Nm, M12=55–70Nm). 2. Backing Plate unter der Sole prüfen (sichtbar von der Achterkoje). 3. GFK der Cockpit-Sole auf Risse prüfen. 4. Falls GFK gerissen: Verstärkung laminieren. 5. Dichtstoff zwischen Flansch und Sole erneuern.

### 8.4 Spezialfragen

**F16: Ich möchte ein Carbon-Rad auf meinem Lewmar-Pedestal montieren. Geht das?**
A: Ja, wenn das Carbon-Rad die Lewmar-Nabenbohrung hat (1:10 Konus, Lewmar-Kerbverzahnung). Carbonautica und Edson (Talon) bieten Räder mit Lewmar-Nabe an. Alternativ: Adapter-Nabe verwenden. Achtung: Galvanische Isolation zwischen Carbon und Edelstahl sicherstellen (PTFE-Buchse).

**F17: Kann ich eine Pinnensteuerung auf einer 14m-Yacht behalten?**
A: Technisch ja, aber es wird bei Starkwind anstrengend. Hallberg-Rassy bot die HR 412 (41 Fuß, ca. 12,5m) noch mit Pinne an — ein bemerkenswertes Beispiel. Ab 14m ist aber professionell ein Steuerrad oder zumindest eine Servo-Pendel-Ruderanlage (Windpilot) empfohlen.

**F18: Was ist der Unterschied zwischen einem Radpiloten und einem hydraulischen Autopiloten?**
A: Ein Radpilot (Wheel Pilot, z.B. Raymarine EV-100) sitzt direkt am Steuerrad und dreht es motorisch. Günstig (€1.500–€3.000), einfach zu installieren, aber hörbar und begrenzte Kraft. Ein hydraulischer Autopilot (z.B. Raymarine EV-200 + Hydraulikpumpe) wirkt direkt auf den Hydraulikzylinder am Ruder. Leiser, kraftvoller, teurer (€3.000–€8.000).

**F19: Können Joysticks auf Segelyachten verwendet werden?**
A: Joystick-Steuerung für Segelyachten ist unüblich, da beim Segeln feinfühliges Steuern über das Rad/die Pinne essentiell ist. Bei Motor-Seglern (z.B. Hybrid-Antriebe) kann ein Joystick für Hafenmanöver ergänzt werden, wenn Bug- und Heckstrahlruder vorhanden sind.

**F20: Was kostet eine komplette Steueranlage (Doppelrad) für eine 13m-Yacht?**
A: Überschlagsmäßig:
- 2× Steuerräder (Lewmar Evolution 900mm): €2.100
- Doppel-Pedestal (Jefa oder Lewmar): €2.500
- Steuergetriebe, Quadrant, Steuerseil: €800
- Montage (Fachbetrieb): €1.500
- Gesamt: ca. €6.500–€8.000
- Mit Hydraulik statt Seilzug: ca. €8.000–€12.000

### 8.5 AYDI-spezifisch

**F21: Wie bewertet AYDI den Zustand eines Steuerrades?**
A: AYDI bewertet in drei Kategorien: (1) Strukturelle Integrität (Spiel, Bruch, Korrosion — Confidence: measured bei Inspektion, visual_medium bei Foto), (2) Oberflächenzustand (Teak, Leder, Carbon, Edelstahl — Confidence: visual_high bei guten Fotos), (3) Ergonomie (Durchmesser, Griffhöhe, Sichtlinien — Confidence: measured bei CAD, estimated bei Specs).

**F22: Welche Fotos soll ich für eine AYDI-Steuerrad-Analyse hochladen?**
A: Idealerweise: (1) Frontalansicht des gesamten Rades mit Pedestal, (2) Nahaufnahme der Griffoberfläche (Teak/Leder-Zustand), (3) Nabe und Speichen-Ansatz, (4) Pedestal-Fuß (Dichtung, Schrauben), (5) Sichtlinie über das Rad (Kameraposition auf Augenhöhe des Rudergängers). Mindestauflösung: 2 Megapixel. Gutes Licht (kein Gegenlicht).

**F23: Kann AYDI den Ruderdruck meines Bootes schätzen?**
A: Ja, wenn Bootslänge, Breite, Rudertyp und -fläche bekannt sind. AYDI verwendet ein parametrisches Modell basierend auf Ruderfläche, Fahrgeschwindigkeit und Seitenwind. Die Confidence ist "estimated" (Level 1) oder "calculated" (Level 2, mit CAD-Daten).

**F24: Wie fließt die Steuerrad-Analyse in die Gesamtbewertung ein?**
A: Die Steuerrad/Pinnen-Analyse fließt primär in die Module Ergonomie (Griffkräfte, Sichtlinien), Material (Korrosion, Verschleiß) und Compliance (ISO 8847, Notsteuerung) ein. Sekundär beeinflusst sie das Emotional-Modul (Design, Haptik) und das Brand-DNA-Modul (herstellertypische Steuerungsphilosophie).

**F25: Warum zeigt AYDI bei manchen Steuerrad-Befunden "nicht beurteilbar"?**
A: AYDI gibt "nicht beurteilbar" (visual_insufficient) aus, wenn das Fotomaterial nicht ausreicht für eine verlässliche Aussage — z.B. Seilzug-Zustand unter der Cockpit-Sole (nicht sichtbar), Getriebe-Verschleiß (nicht von außen erkennbar), oder Ruderdruck (nicht visuell messbar). Dies ist ein Qualitätsmerkmal: Lieber ehrlich als geraten.

**F26: Erkennt AYDI den Hersteller meines Steuerrades auf Fotos?**
A: In vielen Fällen ja. Lewmar, Edson, Jefa und Goiot haben erkennbare Design-Merkmale (Speichenform, Nabengestaltung, Teak-Segmentierung). Die Confidence ist "visual_medium". Eine sichere Identifikation erfordert die Herstellerprägung auf der Nabe oder dem Pedestal.

**F27: Was passiert, wenn AYDI Strukturprobleme am Steuerrad erkennt?**
A: Strukturelle Befunde (Riss, Korrosion, Delamination) werden als "Befund prüfen" markiert — NIEMALS als "Mangel bestätigt". Der Nutzer erhält eine Handlungsempfehlung mit Dringlichkeitsstufe und wird aufgefordert, den Befund physisch zu verifizieren. Bei KRITISCHEN Befunden (z.B. Seilbruch-Verdacht) wird eine Warnmeldung prominent angezeigt.

---

## 9. Glossar

| Nr. | Begriff | Erklärung |
|-----|---------|-----------|
| 1 | **Backlash** | Totgang, Spiel im Steuergetriebe (Winkelbereich ohne Ruderreaktion) |
| 2 | **Backing Plate** | Verstärkungsplatte unter der Cockpit-Sole zur Lastverteilung des Pedestals |
| 3 | **Bimini** | Festes oder faltbares Sonnensegel über dem Cockpit, beeinflusst Sichtlinien |
| 4 | **Capstan-Effekt** | Reibungsverstärkung einer Leine um eine Trommel (exponentiell mit Umschlingungswinkel) |
| 5 | **CFK** | Kohlefaserverstärkter Kunststoff (Carbon Fibre Reinforced Polymer) |
| 6 | **ComfortGrip** | Edson-proprietärer ergonomischer Teak-Griff mit Fingerrillen |
| 7 | **Cockpit-Sole** | Boden des Cockpits, auf dem der Rudergänger steht |
| 8 | **Destroyer-Wheel** | Steuerrad-Grundtyp mit durchgehendem Radkranz und radialen Speichen |
| 9 | **Direct-Drive** | Direktantrieb ohne Seil/Kette — Getriebe sitzt direkt am Ruderschaft |
| 10 | **Doppelrad** | Zwei Steuerräder, symmetrisch angeordnet (Twin Wheel) |
| 11 | **Drogue** | Schleppbremse / Treibanker, kann zur Behelfssteuerung eingesetzt werden |
| 12 | **Emergency Tiller** | Notpinne — Hebelarm für den Notfall bei Radsteuerungs-Ausfall |
| 13 | **Faltrad** | Steuerrad mit klappbaren Speichen oder teilbarem Kranz |
| 14 | **Feedback-Ventil** | Hydraulikventil, das dem Rudergänger künstliches Ruderfeedback gibt |
| 15 | **GFK** | Glasfaserverstärkter Kunststoff (Glass Fibre Reinforced Polymer) |
| 16 | **Helm Pump** | Hydraulikpumpe am Steuerstand (im Pedestal integriert) |
| 17 | **Hiking Stick** | Pinnenverlängerung für die Ausreitposition (Regatta-Segeln) |
| 18 | **ISO 8847** | Internationale Norm für Steueranlagen auf Sportbooten |
| 19 | **Joystick** | Proportionaler Steuerknüppel für Niedriggeschwindigkeitsmanöver |
| 20 | **Kerbverzahnung** | Formschlüssige Verbindung zwischen Rad-Nabe und Steuerwelle (Splined Hub) |
| 21 | **Kolderstock** | Historisches Steuerinstrument (Whipstaff), vertikaler Hebel an der Pinne |
| 22 | **Konus** | Konische Passform der Nabe auf der Steuerwelle (typisch 1:10) |
| 23 | **Litzenbruch** | Bruch einzelner Drähte im Steuerseil (Vorbote des Totalversagens) |
| 24 | **Lock-to-Lock** | Radumdrehungen von Vollanschlag links zu Vollanschlag rechts |
| 25 | **Notpinne** | Emergency Tiller — muss an Bord sein (ISO 8847) |
| 26 | **Pedestal** | Steuersäule, die das Steuerrad trägt und das Getriebe enthält |
| 27 | **Pinne** | Hebelarm am Ruderkopf zur direkten Rudersteuerung (Tiller) |
| 28 | **Pinnenverlängerung** | Verlängerungsstab mit Gelenk am Pinnenende (Tiller Extension) |
| 29 | **Power Steering** | Servogesteuertes Lenksystem mit Hydraulikpumpe |
| 30 | **PREN** | Pitting Resistance Equivalent Number — Maß für Korrosionsbeständigkeit von Stahl |
| 31 | **Quadrant** | Kreissegment am Ruderschaft, an dem die Steuerseile angreifen |
| 32 | **Radial-Drive** | Seilzug-Antrieb über eine Rolle am Ruderschaft (Alternative zum Quadrant) |
| 33 | **Ruderkopf** | Oberes Ende des Ruderschafts, auf dem die Pinne oder der Quadrant sitzt |
| 34 | **Ruderschaft** | Vertikale Welle, die das Ruderblatt mit der Steueranlage verbindet |
| 35 | **Schneckengetriebe** | Worm Gear — Getriebe mit hoher Übersetzung und Selbsthemmung |
| 36 | **Speichenrad** | Steuerrad mit stabförmigen Speichen (klassischer Typ) |
| 37 | **Steuerseil** | Edelstahl-Drahtseil (1×19 oder 7×7), überträgt Radbewegung auf Quadrant |
| 38 | **Swan-Neck** | Geschwungene Pinnenform mit angehobenem Griffbereich |
| 39 | **Tea Staining** | Braune Verfärbung auf Edelstahl durch atmosphärische Korrosion |
| 40 | **Tiller** | Englisch für Pinne |
| 41 | **Tillerpilot** | Autopilot-Antrieb, der direkt an der Pinne ansetzt (z.B. Raymarine EV-100) |
| 42 | **Totgang** | Spiel/Backlash — Winkel, den das Rad gedreht werden kann ohne Ruderreaktion |
| 43 | **Turk's Head** | Seemannsknoten als Zierelement und Abschluss an Leder-Umwicklungen |
| 44 | **Twin Wheel** | Doppelrad-Steuerung (zwei Räder, ein Ruder) |
| 45 | **Universalgelenk** | Kugelgelenk zwischen Pinne und Pinnenverlängerung |
| 46 | **Windpilot** | Windfahnen-Servo-Steueranlage (Marke) — alternative Selbststeuerung |
| 47 | **Worm Gear** | Schneckengetriebe (siehe Nr. 35) |

---

## 10. Schnell-Referenz

### 10.1 Steuerrad-Dimensionierung — Schnellwahl

```
╔══════════════════╦═══════════════╦══════════════════╦══════════════════╗
║ LOA              ║ Rad-Ø [mm]    ║ Typ              ║ Pedestal         ║
╠══════════════════╬═══════════════╬══════════════════╬══════════════════╣
║ 8–9m Segel       ║ 600–750       ║ Einzelrad 3-Sp   ║ Commodore 400    ║
║ 9–10m Segel      ║ 700–850       ║ Einzelrad 5-Sp   ║ Commodore 500    ║
║ 10–12m Segel     ║ 800–950       ║ Einzel/Doppel    ║ Commodore 500/600║
║ 12–14m Segel     ║ 900–1.050     ║ Doppelrad        ║ Jefa Twin/600    ║
║ 14–16m Segel     ║ 1.000–1.150   ║ Doppelrad        ║ Jefa Twin/700    ║
║ 16–20m Segel     ║ 1.100–1.250   ║ Doppelrad+Hyd.   ║ Jefa Hydraulic   ║
║ 20–24m Segel     ║ 1.200–1.400   ║ Doppelrad+Hyd.   ║ Custom           ║
║ 8–10m Motor      ║ 350–500       ║ Einzelrad        ║ Teleflex/Kobelt  ║
║ 10–14m Motor     ║ 500–700       ║ Einzelrad        ║ Kobelt/Lewmar    ║
║ 14–20m Motor     ║ 600–900       ║ Einzel+Joystick  ║ Hydraulisch      ║
║ 20–24m Motor     ║ 700–1.000     ║ Einzel+Joystick  ║ Voll-Hydraulisch ║
╚══════════════════╩═══════════════╩══════════════════╩══════════════════╝
```

### 10.2 Steuerrad-Pflege — Jahresplan

```
╔════════════════════╦══════════════════════════════════════════════════╗
║ Zeitpunkt          ║ Maßnahme                                        ║
╠════════════════════╬══════════════════════════════════════════════════╣
║ Saisonbeginn       ║ Komplett-Inspektion: Spiel, Seilzustand,       ║
║ (März/April)       ║ Schmierung, Pedestal-Schrauben, Notpinne       ║
║                    ║ Teak: Reinigen + Ölen                           ║
║                    ║ Leder: Reinigen + Lederbalsam                   ║
╠════════════════════╬══════════════════════════════════════════════════╣
║ Mitte Saison       ║ Teak: Nachölen bei Bedarf                      ║
║ (Juli)             ║ Leder: Nachpflegen                              ║
║                    ║ Seilspannung kontrollieren                      ║
╠════════════════════╬══════════════════════════════════════════════════╣
║ Saisonende         ║ Komplett reinigen (Süßwasser)                   ║
║ (Oktober/November) ║ Alle Metallteile mit Schutzfilm einsprühen      ║
║                    ║ Radcover aufsetzen (UV-/Frostschutz)            ║
║                    ║ Steuerseil auf Litzenbruch prüfen               ║
╠════════════════════╬══════════════════════════════════════════════════╣
║ Alle 5 Jahre       ║ Steuerseil erneuern (auch wenn optisch OK)     ║
║                    ║ Kette prüfen (Verschleißlängung >2% → ersetzen)║
║                    ║ Getriebe professionell warten lassen            ║
╠════════════════════╬══════════════════════════════════════════════════╣
║ Alle 10 Jahre      ║ Komplett-Inspektion durch Fachbetrieb           ║
║                    ║ Ruderlager, Ruderschaft prüfen (→ 20.03)       ║
║                    ║ Getriebe-Austausch bei Verschleiß               ║
╚════════════════════╩══════════════════════════════════════════════════╝
```

### 10.3 Griffkräfte — Normativer Schnellcheck

```
╔══════════════════════╦═══════════╦══════════════════════════════════╗
║ Bediensituation      ║ Max. [N]  ║ Bewertung                       ║
╠══════════════════════╬═══════════╬══════════════════════════════════╣
║ Dauerbetrieb         ║ ≤50       ║ ✓ Komfortabel                   ║
║ Dauerbetrieb         ║ 50–80     ║ ⚠ ISO-Grenzbereich             ║
║ Dauerbetrieb         ║ >80       ║ ✗ Über ISO 8847 Grenzwert      ║
║ Manöver              ║ ≤100      ║ ✓ Normal                        ║
║ Manöver              ║ 100–200   ║ ⚠ Kurzzeitig akzeptabel        ║
║ Notsteuerung         ║ ≤280      ║ ✓ ISO-Grenzwert eingehalten    ║
║ Notsteuerung         ║ >280      ║ ✗ Nicht normkonform            ║
╚══════════════════════╩═══════════╩══════════════════════════════════╝
```

### 10.4 Fehlercode-Schnellreferenz

```
╔════════════╦═══════════════════════════════╦══════════╦═══════════════════╗
║ Code       ║ Fehler                        ║ Schwere  ║ Sofortmaßnahme    ║
╠════════════╬═══════════════════════════════╬══════════╬═══════════════════╣
║ FB-001     ║ Totgang/Spiel                 ║ MITTEL   ║ Seilspannung      ║
║ FB-002     ║ Schwergängigkeit              ║ MITTEL   ║ Schmieren          ║
║ FB-003     ║ Korrosion                     ║ MITTEL   ║ Beizen/Passivieren ║
║ FB-004     ║ Teak-Degradation              ║ NIEDRIG  ║ Reinigen + Ölen    ║
║ FB-005     ║ Seil-/Kettenbruch             ║ KRITISCH ║ NOTPINNE!          ║
║ FB-006     ║ Pedestal-Undichtigkeit        ║ MITTEL   ║ Abdichten          ║
║ FB-007     ║ Leder-Degradation             ║ NIEDRIG  ║ Lederpflege        ║
║ FB-008     ║ Knacken/Knarren               ║ NIEDRIG  ║ Geräuschquelle     ║
║ FB-009     ║ Fehlausrichtung Rad-Ruder     ║ NIEDRIG  ║ Rad neu aufsetzen  ║
║ FB-010     ║ Extension-Gelenk defekt       ║ NIEDRIG  ║ Gelenk ersetzen    ║
║ FB-011     ║ Carbon-Delamination           ║ MITTEL   ║ Feuchteschutz      ║
║ FB-012     ║ Pinnenbruch                   ║ KRITISCH ║ NOTPINNE!          ║
╚════════════╩═══════════════════════════════╩══════════╩═══════════════════╝
```

### 10.5 Hersteller-Schnellvergleich

```
╔════════════════╦═══════════╦══════════════════╦════════════╦══════════╗
║ Hersteller     ║ Land      ║ Stärke           ║ Segment    ║ Preis    ║
╠════════════════╬═══════════╬══════════════════╬════════════╬══════════╣
║ Lewmar         ║ UK        ║ Breites Sortiment║ Fahrt/OEM  ║ €€€      ║
║ Edson          ║ USA       ║ Tradition, Teile ║ Fahrt/Perf.║ €€€      ║
║ Jefa           ║ Dänemark  ║ Komplettsystem   ║ Fahrt/Perf.║ €€€      ║
║ Goiot          ║ Frankreich║ OEM-Volumen      ║ Serie/OEM  ║ €€       ║
║ Carbonautica   ║ Italien   ║ Carbon-Spezialist║ Perf./Luxus║ €€€€    ║
║ Stazo          ║ NL        ║ Motorboot-Fokus  ║ Motor/NL   ║ €€       ║
║ Kobelt         ║ Kanada    ║ Robuste Systeme  ║ Motor/Arb. ║ €€€      ║
║ Lecomble&S.    ║ Frankreich║ Hydraulik        ║ OEM/System ║ €€€      ║
╚════════════════╩═══════════╩══════════════════╩════════════╩══════════╝
```

### 10.6 Kompatibilitäts-Matrix — Naben

```
╔══════════════╦═══════════╦═══════════╦═══════════╦═══════════╦═══════════╗
║ Rad ↓ \ Ped →║ Lewmar    ║ Edson     ║ Jefa      ║ Whitlock  ║ Goiot     ║
╠══════════════╬═══════════╬═══════════╬═══════════╬═══════════╬═══════════╣
║ Lewmar       ║ DIREKT    ║ Adapter   ║ Adapter   ║ Adapter   ║ Adapter   ║
║ Edson        ║ Adapter   ║ DIREKT    ║ Adapter   ║ Adapter   ║ —         ║
║ Jefa         ║ Adapter   ║ Adapter   ║ DIREKT    ║ Adapter   ║ —         ║
║ Goiot        ║ Adapter   ║ —         ║ —         ║ —         ║ DIREKT    ║
║ Carbonautica ║ Auf Anfrage (Custom-Nabe passend zum vorhandenen Pedestal)║
║ Stazo        ║ —         ║ —         ║ —         ║ —         ║ DIREKT¹   ║
╚══════════════╩═══════════╩═══════════╩═══════════╩═══════════╩═══════════╝
¹ Stazo verwendet teils Goiot-kompatible Naben
```

---

## 11. ANHANG A–H — Fallstudien

### ANHANG A — Fallstudie: Bavaria 37 Cruiser, Steuerrad-Upgrade

```
Fallstudie-ID:    CS-20.04-A
Yacht:             Bavaria 37 Cruiser (Baujahr 2008)
LOA:               11,35m
Ausgangszustand:   Lewmar Commodore 500, Destroyer 810mm, Teak, 16 Jahre alt
Problem:           Teak-Griffe stark vergraut und rissig, Steuerrad-Spiel ~12°
Einsatzgebiet:     Ostsee, saisonal (Mai–Oktober)

Befund (AYDI Level 2):
  Ergonomie:       Score 72/100 — Rad-Ø passend, Griffzustand mangelhaft
  Material:        Score 58/100 — Teak: visual_high → stark degradiert
  Compliance:      Score 85/100 — Notpinne vorhanden, Spiel grenzwertig

Durchgeführte Maßnahmen:
  1. Steuerseil erneuert (7×7 SS, Ø 4mm) — €95
  2. Seilspannung eingestellt → Spiel von 12° auf 4° reduziert
  3. Teak-Segmente neu (Lewmar Ersatzteil-Set) — €280
  4. Getriebe geschmiert (Lewmar Service Kit) — €35
  5. Pedestal-Dichtung erneuert — €15

Gesamtkosten:  €425 + 6h Arbeit (Eigenleistung)
Ergebnis:      Ergonomie 89/100, Material 91/100, Compliance 95/100

Lessons Learned:
  - Regelmäßige Teak-Pflege hätte Austausch verhindert
  - Steuerseil war nach 16 Jahren am Limit (3 Litzenbrüche gefunden)
  - Pedestal-Dichtung war die ursprüngliche von 2008 (trocken und rissig)
```

### ANHANG B — Fallstudie: Hallberg-Rassy 40C, Doppelrad-Installation (Nachrüstung)

```
Fallstudie-ID:    CS-20.04-B
Yacht:             Hallberg-Rassy 40C (Baujahr 2012)
LOA:               12,20m
Ausgangszustand:   Jefa Einzelrad-Steuerung, 900mm Destroyer, Teak
Problem:           Eigner wünscht Doppelrad für bessere Cockpit-Passage
Einsatzgebiet:     Mittelmeer, ganzjährig

Befund (AYDI Level 2):
  Ergonomie:       Score 78/100 — Einzelrad blockiert Cockpit-Passage
  Compliance:      Score 92/100 — Alles normkonform
  Kosten-Analyse:  Umbau vs. Nutzwert

Durchgeführte Maßnahmen:
  1. Jefa Twin-Pedestal System bestellt (Custom für HR 40C) — €3.200
  2. Zwei Jefa Classic Steuerräder 850mm — €1.400
  3. Cockpit-Sole-Durchbrüche (2×) durch Werft — €800
  4. Verstärkung Cockpit-Sole (GFK-Laminat) — €400
  5. Steuerseile, Quadrant, Umlenkrollen — €650
  6. Instrumenten-Pod zwischen den Rädern — €350
  7. Montage durch Jefa-Partner (Ellös, Schweden) — €2.800

Gesamtkosten:  €9.600 inkl. MwSt.
Ergebnis:      Ergonomie 94/100 (deutliche Verbesserung)
               Cockpit-Passage von 320mm auf 620mm erweitert
               Rudergänger kann jetzt auf Luvseite steuern

Lessons Learned:
  - HR 40C hat Ruderkopf gut zugänglich → Twin-Umbau machbar
  - Cockpit-Sole musste an 4 Punkten verstärkt werden
  - Originalkompass (Plastimo) passte in neuen Instrumenten-Pod
  - Tillerpilot nicht mehr verwendbar → Hydraulik-Autopilot als Folge-Investition nötig
```

### ANHANG C — Fallstudie: X-Yacht X-41, Carbon-Upgrade für Regatta

```
Fallstudie-ID:    CS-20.04-C
Yacht:             X-Yachts X-41 (Baujahr 2015)
LOA:               12,35m
Ausgangszustand:   Jefa Modern 3-Spoke 900mm, All-Stainless
Problem:           Gewichtsoptimierung für ORC-Regatta
Einsatzgebiet:     Nordeuropa, Regatta + Fahrt

Befund (AYDI Level 2):
  Gewicht:         Aktuelles Rad 5,2 kg — Carbon-Rad: ca. 2,0 kg
  Ersparnis:       3,2 kg an einer Position ~1,5m über WL
  Bewertung:       Messbare Verbesserung des RM (Righting Moment) → relevant für ORC-Rating

Durchgeführte Maßnahmen:
  1. Carbonautica Racing 3S, 900mm bestellt (mit Jefa-Nabe) — €3.800
  2. Teak-Inlays im Griffbereich (für Langstreckenregatten) — €400 Aufpreis
  3. Altes Rad behalten als Reserve / für Crewtraining
  4. Montage: Eigentümer selbst (15 min Radtausch)

Gesamtkosten:  €4.200
Ergebnis:      Gewichtsersparnis 3,2 kg, ORC-Rating um 0.3 sec/nm verbessert
               Haptik: Exzellent (Teak-Inlays bewährt)
               Optik: Deutlich aufgewertet (Sichtcarbon-Finish)

Lessons Learned:
  - Jefa-Nabe direkt bei Carbonautica bestellbar (keine Adapter nötig)
  - UV-Schutz des Carbon kritisch → Radcover bei Nichtgebrauch
  - Galvanische Isolation: Carbonautica verwendet intern PTFE-Buchse zwischen Carbon und SS-Nabe
```

### ANHANG D — Fallstudie: Jeanneau Sun Odyssey 440, Goiot-Steuerrad Austausch

```
Fallstudie-ID:    CS-20.04-D
Yacht:             Jeanneau Sun Odyssey 440 (Baujahr 2019)
LOA:               13,39m
Ausgangszustand:   Goiot Atlantique Doppelrad 800mm, 5-Spoke, SS+Teak
Problem:           Teak-Segment gelöst (Klebung versagt), Rad klappert
Einsatzgebiet:     Charterboot, Griechenland

Befund (AYDI Level 1 — Schnellanalyse via Foto):
  Material:        Score 55/100 — visual_high: Teak-Segment sichtbar lose
  Ergonomie:       Score 82/100 — Grundlayout OK (Werftstandard)

Durchgeführte Maßnahmen:
  1. Teak-Segment entfernt, Klebeflächen gereinigt
  2. Neue Verklebung mit Sikaflex 291i (flexibel, wasserbeständig)
  3. Zusätzlich: 2× M4 Edelstahl-Madenschrauben als mechanische Sicherung
  4. Alle 8 Teak-Segmente (beide Räder) prophylaktisch geprüft
  5. 3 weitere Segmente leicht lose → gleiche Behandlung
  6. Teak gereinigt und geölt (Semco Teak Oil)

Gesamtkosten:  €85 Material + 4h Arbeit
Ergebnis:      Material 92/100

Lessons Learned:
  - Goiot Atlantique: Verklebung der Teak-Segmente ist die bekannte Schwachstelle
  - Im Charterbereich: Höhere Beanspruchung (viele verschiedene Hände)
  - Empfehlung: Bei Goiot-Rädern prophylaktisch alle Segmente bei Saisonstart prüfen
  - Madenschrauben als Zusatzsicherung bewährt sich
```

### ANHANG E — Fallstudie: Dehler 38 SQ, Pinne beibehalten — Ergonomie-Optimierung

```
Fallstudie-ID:    CS-20.04-E
Yacht:             Dehler 38 SQ (Baujahr 2020)
LOA:               11,50m
Ausgangszustand:   Carbon-Pinne (Dehler-Standard), L=1.100mm, mit Verlängerung
Problem:           Eigner findet Pinne bei Starkwind zu kräfteintensiv
Einsatzgebiet:     Nordsee, Regatta und Fahrt

Befund (AYDI Level 2):
  Ergonomie:       Score 75/100 — Ruderdruck geschätzt: 90–120N bei 6 Bft
  Compliance:      Score 95/100 — ISO 8847 eingehalten (Notsteuerung = Pinne selbst)
  Empfehlung:      Autopilot-Tillerpilot oder Ruderdruck-Reduktion

Durchgeführte Maßnahmen:
  Option A (gewählt): Raymarine EV-100 Tillerpilot installiert — €1.800
  - Pinne beibehalten (Carbon, exzellenter Zustand)
  - Tillerpilot-Halterung am Cockpit-Süll montiert
  - Entlastet den Rudergänger auf Langstrecken

  Option B (verworfen): Umrüstung auf Radsteuerung
  - Geschätzte Kosten: €6.000–€8.000
  - Verlust des direkten Ruderfeedbacks
  - Gewichtszunahme ca. 12 kg am Heck

Gesamtkosten:  €1.800 + €300 Installation
Ergebnis:      Ergonomie 88/100 (mit Tillerpilot-Unterstützung)

Lessons Learned:
  - Dehler 38 SQ hat optimierte Ruderbilanz → Ruderdruck vertretbar
  - Tillerpilot ist die kosteneffizienteste Lösung
  - Carbon-Pinne in einwandfreiem Zustand → kein Handlungsbedarf am Steuerelement selbst
```

### ANHANG F — Fallstudie: Najad 440 CC, Korrosion an Edelstahl-Steuerrad

```
Fallstudie-ID:    CS-20.04-F
Yacht:             Najad 440 CC (Baujahr 2005)
LOA:               13,50m
Ausgangszustand:   Jefa Classic Doppelrad 950mm, SS 316L + Teak
Problem:           Korrosion an Schweißnähten der Speichen (Lochfraß)
Einsatzgebiet:     Atlantik-Umrundung, tropische und Salzwasser-Regionen

Befund (AYDI Level 2):
  Material:        Score 45/100 — visual_high: Pitting an 3 von 10 Speichen-Schweißnähten
  Compliance:      Score 70/100 — Strukturelle Integrität fraglich
  Bewertung:       "Befund prüfen" — professionelle Prüfung empfohlen

Durchgeführte Maßnahmen:
  1. Räder demontiert und zum Schweißfachbetrieb gebracht
  2. Befund bestätigt: Pitting 0,3–0,8mm tief an den Schweißnähten
  3. Ursache: Mangelhafte Passivierung nach dem Schweißen (Werft-Fehler)
  4. Betroffene Schweißnähte ausgeschliffen und WIG-nachgeschweißt
  5. Komplettes Rad gebeizt (Avesta 401 Beizpaste)
  6. Passiviert (Avesta 601 Passivierungspaste)
  7. Neu poliert (#6 Satiniert)
  8. Teak-Segmente bei Gelegenheit erneuert

Gesamtkosten:  €1.800 (für beide Räder)
Ergebnis:      Material 90/100 nach Reparatur

Lessons Learned:
  - Pitting an Schweißnähten ist ein bekanntes Problem bei Marine-Edelstahl
  - Regelmäßige Kontrolle der Schweißnähte mit Lupe empfohlen (jährlich)
  - Beizen und Passivieren nach jeder Schweißarbeit ist PFLICHT
  - Im tropischen Einsatz: Edelstahl-Pflegemittel (Wichard Wichinox) 4× jährlich
```

### ANHANG G — Fallstudie: Lagoon 42, Doppelrad-Ergonomie bei Katamaran

```
Fallstudie-ID:    CS-20.04-G
Yacht:             Lagoon 42 (Baujahr 2021)
LOA:               12,80m
Ausgangszustand:   Goiot Pacifique Doppelrad 800mm, SS+Teak, Helm-Station achtern
Problem:           Sichtlinie über Coachroof bei Vorwind-Kursen eingeschränkt
Einsatzgebiet:     Karibik, Langfahrt

Befund (AYDI Level 2):
  Ergonomie:       Score 68/100 — Sichtlinie über Coachroof kritisch
  Compliance:      Score 78/100 — ISO 11591 Sichtfeld-Anforderung grenzwertig

Durchgeführte Maßnahmen:
  1. Sichtlinien-Analyse: Rudergänger (175cm) sieht nicht über Coachroof auf Bug
  2. Pedestal-Riser (50mm Edelstahl-Distanzstück) unter beide Pedestals — €350
  3. Cockpit-Sole am Steuerstand um 30mm erhöht (Teak-Grating) — €400
  4. Gesamt-Erhöhung der Augposition: +80mm → Sichtlinie jetzt über Coachroof
  5. Neue Sichtlinien-Vermessung: Bugbereich bei 2× LOA sichtbar

Gesamtkosten:  €750 + 8h Arbeit (Werft)
Ergebnis:      Ergonomie 85/100, Compliance 90/100

Lessons Learned:
  - Katamarane haben bauartbedingt hohes Coachroof → Sichtlinien-Problem häufig
  - Pedestal-Riser ist eine einfache und reversible Lösung
  - Alternativ: Größerer Raddurchmesser (900mm statt 800mm) → ähnlicher Effekt
  - Lagoon-Helm-Station hat generell weniger Sichtprobleme als Bali oder Fountaine Pajot
```

### ANHANG H — Fallstudie: Swan 48, Premium-Steuerrad-Restaurierung

```
Fallstudie-ID:    CS-20.04-H
Yacht:             Nautor's Swan 48 (Baujahr 1995)
LOA:               14,83m
Ausgangszustand:   Original Lewmar-Doppelrad 1.000mm, stark gealtert (29 Jahre)
Problem:           Umfassende Restaurierung für Refit, originalgetreu
Einsatzgebiet:     Mittelmeer, gehobener Fahrtensegler

Befund (AYDI Level 2):
  Material:        Score 52/100 — Teak dunkel verfärbt, Edelstahl mit Tea Staining
  Ergonomie:       Score 80/100 — Layout und Dimensionierung korrekt (Swan-Klasse)
  Emotional:       Score 45/100 — Gesamteindruck "müde" → für Swan unakzeptabel

Durchgeführte Maßnahmen:
  1. Räder demontiert, komplett zerlegt (Teak-Segmente, Schrauben, Nabe)
  2. Edelstahl-Rahmen:
     - Beizen mit Avesta 401
     - Nachschleifen (Korn 320 → 600 → 1200)
     - Hochglanzpolitur (#8 Mirror Finish)
  3. Teak-Segmente:
     - Originalmaße vermessen
     - Neue Burma-Teak-Segmente (Grad A, FSC) von Spezialschreinerei — €1.200
     - Epoxid-Verklebung + verdeckte Edelstahl-Schrauben
     - Finish: 4× Epifanes Marine Klarlack (UV-beständig)
  4. Naben: Gereinigt, Konusfläche geprüft, Kerbverzahnung nachpoliert
  5. Zusammenbau mit neuen Befestigungen (A4-80 Schrauben)
  6. Pedestal-Service: Getriebe zerlegt, gereinigt, neu gefettet

Gesamtkosten:  €4.200 (Material + spezialisierte Handarbeit)
Ergebnis:      Material 96/100, Emotional 94/100 — "wie neu"

Lessons Learned:
  - 30 Jahre alte Lewmar-Steuerräder lassen sich komplett restaurieren
  - Hochwertige Teak-Segmente sind der Schlüssel zum Premium-Erscheinungsbild
  - Restaurierung ist bei Swan- und Oyster-Klasse wirtschaftlich sinnvoll (Wertsteigerung)
  - Kosten Restaurierung (€4.200) vs. Neukauf (€3.500–€4.500 pro Rad) → ähnlich, aber originalgetreu
```

---

## 12. ANHANG I–R — Pydantic v2 Modelle

### ANHANG I — Steuerrad-Basis-Modell

```python
"""
AYDI 20.04 — Pydantic v2 Models for Steering Wheels and Tillers.

All models use Pydantic v2 with model_config = {"from_attributes": True}.
NEVER use class Config — this is a Pydantic v1 pattern.
German user-facing text, English code.
"""

from __future__ import annotations

from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class SteeringType(str, Enum):
    """Type of steering input device."""
    WHEEL_SINGLE = "wheel_single"
    WHEEL_TWIN = "wheel_twin"
    WHEEL_FOLDING = "wheel_folding"
    TILLER_WOOD = "tiller_wood"
    TILLER_CARBON = "tiller_carbon"
    TILLER_ALUMINUM = "tiller_aluminum"
    TILLER_GRP = "tiller_grp"
    JOYSTICK = "joystick"


class WheelDesign(str, Enum):
    """Wheel design type."""
    DESTROYER = "destroyer"
    SPOKE = "spoke"
    FOLDING = "folding"
    POWER_KNOB = "power_knob"


class GripMaterial(str, Enum):
    """Grip material for wheel rim or tiller handle."""
    TEAK = "teak"
    LEATHER = "leather"
    CORK = "cork"
    CARBON = "carbon"
    CARBON_TEAK = "carbon_teak"
    STAINLESS = "stainless"
    RUBBER_TPE = "rubber_tpe"
    ALUMINUM_ANODIZED = "aluminum_anodized"
    EVA_FOAM = "eva_foam"
    NONE = "none"


class FrameMaterial(str, Enum):
    """Frame / structural material."""
    STAINLESS_316L = "stainless_316l"
    STAINLESS_316TI = "stainless_316ti"
    CARBON_CFK = "carbon_cfk"
    ALUMINUM_6082 = "aluminum_6082"
    BRONZE = "bronze"
    TEAK = "teak"
    GRP = "grp"
    TITANIUM = "titanium"


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


class SteeringWheelSpec(BaseModel):
    """Specification of a steering wheel."""

    model_config = {"from_attributes": True}

    manufacturer: str = Field(
        ...,
        description="Hersteller des Steuerrades",
        examples=["Lewmar", "Edson", "Jefa", "Goiot", "Carbonautica"],
    )
    model_name: str = Field(
        ...,
        description="Modellbezeichnung",
        examples=["Corsair 5-Spoke", "PowerWheel 36", "Racing 3S"],
    )
    steering_type: SteeringType = Field(
        ...,
        description="Art der Steuerung",
    )
    wheel_design: Optional[WheelDesign] = Field(
        None,
        description="Design-Typ des Rades (nur bei Radsteuerung)",
    )
    diameter_mm: int = Field(
        ...,
        ge=200,
        le=2000,
        description="Raddurchmesser in mm",
    )
    spoke_count: int = Field(
        ...,
        ge=0,
        le=12,
        description="Anzahl der Speichen (0 bei Pinne)",
    )
    frame_material: FrameMaterial = Field(
        ...,
        description="Material des Radkranzes / der Struktur",
    )
    grip_material: GripMaterial = Field(
        ...,
        description="Material der Griffbereiche",
    )
    weight_kg: Optional[float] = Field(
        None,
        ge=0.1,
        le=50.0,
        description="Gewicht in kg",
    )
    price_eur: Optional[float] = Field(
        None,
        ge=0,
        description="Richtpreis in EUR (netto)",
    )

    @field_validator("diameter_mm")
    @classmethod
    def validate_diameter(cls, v: int) -> int:
        if v < 200:
            raise ValueError("Raddurchmesser unter 200mm ist unrealistisch")
        if v > 1800:
            raise ValueError("Raddurchmesser über 1800mm ist unrealistisch")
        return v
```

### ANHANG J — Pinnen-Modell

```python
class TillerProfile(str, Enum):
    """Cross-section profile of the tiller."""
    ROUND = "round"
    OVAL = "oval"
    RECTANGULAR = "rectangular"
    AIRFOIL = "airfoil"


class TillerShape(str, Enum):
    """Overall shape of the tiller."""
    STRAIGHT = "straight"
    SWAN_NECK = "swan_neck"
    S_CURVE = "s_curve"
    CURVED_UP = "curved_up"


class TillerSpec(BaseModel):
    """Specification of a tiller / pinne."""

    model_config = {"from_attributes": True}

    manufacturer: Optional[str] = Field(
        None,
        description="Hersteller der Pinne (oft Werft-eigenfertigung)",
    )
    material: FrameMaterial = Field(
        ...,
        description="Hauptmaterial der Pinne",
    )
    length_mm: int = Field(
        ...,
        ge=300,
        le=2000,
        description="Gesamtlänge der Pinne in mm",
    )
    profile: TillerProfile = Field(
        ...,
        description="Querschnittsprofil",
    )
    shape: TillerShape = Field(
        ...,
        description="Gesamtform der Pinne",
    )
    width_mm: Optional[int] = Field(
        None,
        ge=20,
        le=120,
        description="Breite des Querschnitts in mm (bei Oval/Rechteck)",
    )
    height_mm: Optional[int] = Field(
        None,
        ge=20,
        le=120,
        description="Höhe des Querschnitts in mm (bei Oval/Rechteck)",
    )
    outer_diameter_mm: Optional[int] = Field(
        None,
        ge=20,
        le=80,
        description="Außendurchmesser in mm (bei Rohrprofil)",
    )
    wall_thickness_mm: Optional[float] = Field(
        None,
        ge=1.0,
        le=15.0,
        description="Wandstärke in mm (bei Rohrprofil)",
    )
    weight_g: Optional[int] = Field(
        None,
        ge=50,
        le=5000,
        description="Gewicht in Gramm",
    )
    grip_material: GripMaterial = Field(
        GripMaterial.NONE,
        description="Material des Griffbereichs",
    )
    has_extension_joint: bool = Field(
        False,
        description="Hat die Pinne einen Anschluss für Pinnenverlängerung?",
    )
    rudder_head_type: Optional[str] = Field(
        None,
        description="Typ der Ruderkopf-Verbindung (z.B. 'clamp', 'splined', 'keyed')",
    )
```

### ANHANG K — Tiller-Extension-Modell

```python
class ExtensionType(str, Enum):
    """Type of tiller extension."""
    FIXED = "fixed"
    TELESCOPIC = "telescopic"
    FOLDING = "folding"


class JointType(str, Enum):
    """Type of universal joint for tiller extension."""
    BALL_JOINT = "ball_joint"
    RUBBER = "rubber"
    DOUBLE_CARDAN = "double_cardan"
    SNAP_ON = "snap_on"


class TillerExtensionSpec(BaseModel):
    """Specification of a tiller extension / Pinnenverlängerung."""

    model_config = {"from_attributes": True}

    manufacturer: str = Field(
        ...,
        description="Hersteller",
        examples=["Wichard", "Ronstan", "Allen Brothers", "C-Tech"],
    )
    model_name: Optional[str] = Field(
        None,
        description="Modellbezeichnung",
    )
    extension_type: ExtensionType = Field(
        ...,
        description="Bauart der Verlängerung",
    )
    joint_type: JointType = Field(
        ...,
        description="Typ des Universalgelenks",
    )
    length_min_mm: int = Field(
        ...,
        ge=200,
        le=1500,
        description="Minimale Länge in mm",
    )
    length_max_mm: int = Field(
        ...,
        ge=200,
        le=2000,
        description="Maximale Länge in mm (bei Teleskop = ausgezogen)",
    )
    material: FrameMaterial = Field(
        ...,
        description="Material des Rohres",
    )
    weight_g: Optional[int] = Field(
        None,
        ge=30,
        le=1000,
        description="Gewicht in Gramm",
    )
    grip_type: Optional[str] = Field(
        None,
        description="Typ des Endgriffs (z.B. 'EVA ball', 'rubber knob', 'cork')",
    )

    @field_validator("length_max_mm")
    @classmethod
    def validate_max_length(cls, v: int, info) -> int:
        min_len = info.data.get("length_min_mm")
        if min_len is not None and v < min_len:
            raise ValueError("length_max_mm darf nicht kleiner als length_min_mm sein")
        return v
```

### ANHANG L — Pedestal-Modell

```python
class GearType(str, Enum):
    """Type of steering gear in the pedestal."""
    WORM_GEAR = "worm_gear"
    CHAIN_WIRE = "chain_wire"
    RACK_PINION = "rack_pinion"
    DIRECT_DRIVE = "direct_drive"
    HYDRAULIC = "hydraulic"


class PedestalSpec(BaseModel):
    """Specification of a steering pedestal / Steuersäule."""

    model_config = {"from_attributes": True}

    manufacturer: str = Field(
        ...,
        description="Hersteller",
    )
    model_name: str = Field(
        ...,
        description="Modellbezeichnung",
    )
    height_mm: int = Field(
        ...,
        ge=400,
        le=1500,
        description="Höhe des Pedestals über Cockpit-Sole in mm",
    )
    gear_type: GearType = Field(
        ...,
        description="Typ des integrierten Getriebes",
    )
    max_torque_nm: float = Field(
        ...,
        ge=50,
        le=5000,
        description="Maximales Ruderdrehmoment in Nm",
    )
    gear_ratio: Optional[float] = Field(
        None,
        ge=1.0,
        le=100.0,
        description="Getriebeübersetzung",
    )
    lock_to_lock_turns: Optional[float] = Field(
        None,
        ge=0.5,
        le=10.0,
        description="Umdrehungen Lock-to-Lock",
    )
    is_twin: bool = Field(
        False,
        description="Doppel-Pedestal (Twin)?",
    )
    compass_mount: bool = Field(
        True,
        description="Hat Kompass-Aufnahme?",
    )
    guard_available: bool = Field(
        True,
        description="Schutzbügel (Guard) verfügbar?",
    )
    weight_kg: Optional[float] = Field(
        None,
        ge=1.0,
        le=50.0,
        description="Gewicht ohne Steuerrad in kg",
    )
    material: FrameMaterial = Field(
        FrameMaterial.STAINLESS_316L,
        description="Hauptmaterial des Pedestal-Gehäuses",
    )
    hub_type: Optional[str] = Field(
        None,
        description="Nabentyp (z.B. 'lewmar_1_10', 'edson_13t', 'jefa_standard')",
    )
    price_eur: Optional[float] = Field(
        None,
        ge=0,
        description="Richtpreis in EUR (netto)",
    )
```

### ANHANG M — Steueranlage-Gesamtmodell

```python
class SteeringSystemSpec(BaseModel):
    """Complete steering system specification from wheel/tiller to rudder."""

    model_config = {"from_attributes": True}

    boat_name: Optional[str] = Field(None, description="Bootsname")
    boat_loa_mm: int = Field(
        ...,
        ge=4000,
        le=30000,
        description="Bootslänge über Alles in mm",
    )
    boat_type: str = Field(
        ...,
        description="Bootstyp",
        examples=["sailing_cruiser", "sailing_racer", "motor_displacement", "motor_planing", "catamaran"],
    )
    steering_type: SteeringType = Field(
        ...,
        description="Hauptsteuerungstyp",
    )
    wheel: Optional[SteeringWheelSpec] = Field(
        None,
        description="Steuerrad-Spezifikation (wenn vorhanden)",
    )
    tiller: Optional[TillerSpec] = Field(
        None,
        description="Pinnen-Spezifikation (wenn vorhanden)",
    )
    tiller_extension: Optional[TillerExtensionSpec] = Field(
        None,
        description="Pinnenverlängerung (wenn vorhanden)",
    )
    pedestal: Optional[PedestalSpec] = Field(
        None,
        description="Pedestal-Spezifikation (wenn vorhanden)",
    )
    transmission_type: Optional[GearType] = Field(
        None,
        description="Art der Kraftübertragung zum Ruder",
    )
    rudder_torque_nm: Optional[float] = Field(
        None,
        ge=0,
        le=10000,
        description="Maximales Ruderdrehmoment in Nm",
    )
    has_autopilot: bool = Field(
        False,
        description="Autopilot vorhanden?",
    )
    autopilot_type: Optional[str] = Field(
        None,
        description="Autopilot-Typ (z.B. 'wheel_pilot', 'tiller_pilot', 'hydraulic', 'linear')",
    )
    has_emergency_tiller: bool = Field(
        False,
        description="Notpinne vorhanden?",
    )
    installation_year: Optional[int] = Field(
        None,
        ge=1950,
        le=2030,
        description="Einbaujahr der Steueranlage",
    )

    @field_validator("steering_type")
    @classmethod
    def validate_steering_consistency(cls, v: SteeringType) -> SteeringType:
        # Validation logic would check wheel/tiller presence matches type
        return v
```

### ANHANG N — Assessment / Bewertungsmodell

```python
class SeverityLevel(str, Enum):
    """Severity of a finding."""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


class SteeringFinding(BaseModel):
    """Single finding from steering system assessment."""

    model_config = {"from_attributes": True}

    finding_id: str = Field(
        ...,
        description="Unique finding ID (z.B. 'FB-20.04-001')",
    )
    title_de: str = Field(
        ...,
        description="Befundtitel auf Deutsch",
    )
    description_de: str = Field(
        ...,
        description="Befundbeschreibung auf Deutsch",
    )
    severity: SeverityLevel = Field(
        ...,
        description="Schweregrad",
    )
    confidence: ConfidenceLevel = Field(
        ...,
        description="Vertrauensniveau der Bewertung",
    )
    location: Optional[str] = Field(
        None,
        description="Ort des Befundes (z.B. 'Speiche 3, Schweißnaht Nabe')",
    )
    recommendation_de: str = Field(
        ...,
        description="Handlungsempfehlung auf Deutsch",
    )
    estimated_cost_eur: Optional[float] = Field(
        None,
        ge=0,
        description="Geschätzte Reparaturkosten in EUR",
    )
    urgency_days: Optional[int] = Field(
        None,
        ge=0,
        description="Empfohlener Zeitrahmen für Behebung in Tagen",
    )
    photo_references: list[str] = Field(
        default_factory=list,
        description="Referenzen auf Fotodokumentation",
    )


class SteeringAssessment(BaseModel):
    """Complete assessment result for steering system (Module output)."""

    model_config = {"from_attributes": True}

    assessment_id: str = Field(
        ...,
        description="Eindeutige Assessment-ID",
    )
    assessment_date: date = Field(
        ...,
        description="Datum der Bewertung",
    )
    boat_name: Optional[str] = Field(None, description="Bootsname")
    boat_loa_mm: int = Field(
        ...,
        ge=4000,
        le=30000,
        description="Bootslänge in mm",
    )
    system_spec: SteeringSystemSpec = Field(
        ...,
        description="Spezifikation der bewerteten Steueranlage",
    )
    overall_score: float = Field(
        ...,
        ge=0,
        le=100,
        description="Gesamtbewertung 0–100",
    )
    ergonomics_score: Optional[float] = Field(
        None,
        ge=0,
        le=100,
        description="Ergonomie-Teilbewertung 0–100",
    )
    material_score: Optional[float] = Field(
        None,
        ge=0,
        le=100,
        description="Material-Teilbewertung 0–100",
    )
    compliance_score: Optional[float] = Field(
        None,
        ge=0,
        le=100,
        description="Compliance-Teilbewertung 0–100",
    )
    emotional_score: Optional[float] = Field(
        None,
        ge=0,
        le=100,
        description="Emotional/Design-Teilbewertung 0–100",
    )
    findings: list[SteeringFinding] = Field(
        default_factory=list,
        description="Liste der Einzelbefunde",
    )
    confidence_overall: ConfidenceLevel = Field(
        ...,
        description="Gesamt-Confidence der Bewertung",
    )
    data_sources: list[str] = Field(
        default_factory=list,
        description="Datenquellen (z.B. ['photo_upload', 'cad_import', 'manual_input'])",
    )
    available: bool = Field(
        True,
        description="Modul konnte Ergebnis liefern (False bei skip)",
    )
    skip_reason: Optional[str] = Field(
        None,
        description="Grund für Skip (falls available=False)",
    )
```

### ANHANG O — Ergonomie-Analyse-Modell

```python
class SteeringErgonomicsAnalysis(BaseModel):
    """Ergonomic analysis of the steering position."""

    model_config = {"from_attributes": True}

    # Wheel/Tiller dimensions relative to cockpit
    wheel_center_height_mm: Optional[int] = Field(
        None,
        ge=400,
        le=1500,
        description="Höhe der Radachse über Cockpit-Sole",
    )
    wheel_top_height_mm: Optional[int] = Field(
        None,
        ge=600,
        le=2000,
        description="Höhe der Rad-Oberkante über Cockpit-Sole",
    )
    tiller_grip_height_mm: Optional[int] = Field(
        None,
        ge=200,
        le=1000,
        description="Griffhöhe der Pinne über Cockpit-Sole",
    )
    sightline_over_wheel_deg: Optional[float] = Field(
        None,
        ge=-10,
        le=30,
        description="Sichtwinkel über Radkranz zum Horizont (stehend, 50. Perz.)",
    )
    sightline_iso_compliant: Optional[bool] = Field(
        None,
        description="ISO 11591 Sichtfeld-Konformität",
    )
    passage_width_mm: Optional[int] = Field(
        None,
        ge=0,
        le=2000,
        description="Freie Durchgangsbreite im Cockpit (neben/zwischen Rädern)",
    )
    hand_force_normal_n: Optional[float] = Field(
        None,
        ge=0,
        le=500,
        description="Handkraft bei Normalbetrieb in N (geschätzt oder gemessen)",
    )
    hand_force_gust_n: Optional[float] = Field(
        None,
        ge=0,
        le=1000,
        description="Handkraft bei Böe in N (geschätzt oder gemessen)",
    )
    iso_8847_compliant: Optional[bool] = Field(
        None,
        description="Handkraft-Grenzwert ISO 8847 eingehalten?",
    )
    grip_diameter_mm: Optional[float] = Field(
        None,
        ge=15,
        le=60,
        description="Griffdurchmesser am Radkranz / Pinne in mm",
    )
    grip_comfort_score: Optional[float] = Field(
        None,
        ge=0,
        le=100,
        description="Griffkomfort-Bewertung 0–100",
    )
    heel_angle_assessment: Optional[dict] = Field(
        None,
        description="Bewertung bei verschiedenen Krängungswinkeln (z.B. {'0deg': 95, '15deg': 82, '25deg': 65})",
    )
    confidence: ConfidenceLevel = Field(
        ...,
        description="Confidence der Ergonomie-Analyse",
    )
```

### ANHANG P — Fehlerbild-Modell

```python
class FaultPattern(BaseModel):
    """Fault pattern for steering wheel / tiller diagnostics."""

    model_config = {"from_attributes": True}

    fault_id: str = Field(
        ...,
        description="Fehlerbild-ID (z.B. 'FB-20.04-001')",
    )
    title_de: str = Field(
        ...,
        description="Fehlertitel auf Deutsch",
    )
    title_en: str = Field(
        ...,
        description="Fehlertitel auf Englisch (für Code-Referenz)",
    )
    severity_default: SeverityLevel = Field(
        ...,
        description="Standard-Schweregrad",
    )
    affected_components: list[str] = Field(
        ...,
        description="Betroffene Komponenten",
        examples=[["wheel_rim", "teak_segments"], ["cable", "chain", "quadrant"]],
    )
    symptoms_de: list[str] = Field(
        ...,
        description="Symptome auf Deutsch",
    )
    possible_causes_de: list[str] = Field(
        ...,
        description="Mögliche Ursachen auf Deutsch",
    )
    inspection_methods: list[str] = Field(
        ...,
        description="Prüfmethoden",
    )
    remediation_steps_de: list[str] = Field(
        ...,
        description="Behebungsschritte auf Deutsch",
    )
    estimated_repair_cost_eur_min: Optional[float] = Field(
        None,
        ge=0,
        description="Min. geschätzte Reparaturkosten in EUR",
    )
    estimated_repair_cost_eur_max: Optional[float] = Field(
        None,
        ge=0,
        description="Max. geschätzte Reparaturkosten in EUR",
    )
    visual_detectability: ConfidenceLevel = Field(
        ...,
        description="Wie gut ist der Fehler visuell (per Foto) erkennbar?",
    )
    photo_guidance_de: list[str] = Field(
        default_factory=list,
        description="Anleitungen für Fotodokumentation",
    )


class FaultPatternDatabase(BaseModel):
    """Database of all steering fault patterns for AYDI analysis."""

    model_config = {"from_attributes": True}

    version: str = Field(
        "1.0.0",
        description="Version der Fehlerbild-Datenbank",
    )
    category: str = Field(
        "20.04",
        description="AYDI Wissenskategorie",
    )
    fault_patterns: list[FaultPattern] = Field(
        ...,
        description="Liste aller Fehlerbilder",
    )
    last_updated: date = Field(
        ...,
        description="Letztes Update der Datenbank",
    )
```

### ANHANG Q — Hersteller-Datenbank-Modell

```python
class ManufacturerStatus(str, Enum):
    """Operational status of a manufacturer."""
    ACTIVE = "active"
    ACQUIRED = "acquired"
    DEFUNCT = "defunct"


class PriceLevel(str, Enum):
    """Relative price level."""
    BUDGET = "budget"
    STANDARD = "standard"
    PREMIUM = "premium"
    LUXURY = "luxury"


class SteeringManufacturer(BaseModel):
    """Manufacturer entry for steering wheels / tillers."""

    model_config = {"from_attributes": True}

    name: str = Field(
        ...,
        description="Herstellername",
    )
    full_name: str = Field(
        ...,
        description="Vollständiger Firmenname",
    )
    country: str = Field(
        ...,
        description="Land (ISO 3166-1 alpha-2)",
        examples=["GB", "US", "DK", "FR", "IT", "NL", "CA"],
    )
    city: Optional[str] = Field(
        None,
        description="Firmensitz (Stadt)",
    )
    founded_year: Optional[int] = Field(
        None,
        ge=1800,
        le=2030,
        description="Gründungsjahr",
    )
    website: Optional[str] = Field(
        None,
        description="Webseite",
    )
    status: ManufacturerStatus = Field(
        ManufacturerStatus.ACTIVE,
        description="Aktueller Status",
    )
    product_lines: list[str] = Field(
        ...,
        description="Produktlinien im Steuerungsbereich",
    )
    oem_customers: list[str] = Field(
        default_factory=list,
        description="OEM-Werftkunden",
    )
    target_segments: list[str] = Field(
        ...,
        description="Zielsegmente",
        examples=[["sailing_cruiser", "sailing_racer"], ["motor_yacht", "workboat"]],
    )
    price_level: PriceLevel = Field(
        ...,
        description="Preisniveau",
    )
    certifications: list[str] = Field(
        default_factory=list,
        description="Zertifizierungen",
    )
    warranty_years: Optional[int] = Field(
        None,
        ge=0,
        le=100,
        description="Garantie in Jahren",
    )
    spare_parts_availability: Optional[str] = Field(
        None,
        description="Ersatzteilverfügbarkeit (z.B. 'excellent_20y', 'good_10y', 'limited')",
    )
    strengths_de: list[str] = Field(
        default_factory=list,
        description="Stärken auf Deutsch",
    )
    weaknesses_de: list[str] = Field(
        default_factory=list,
        description="Schwächen auf Deutsch",
    )


class SteeringManufacturerDatabase(BaseModel):
    """Complete manufacturer database for AYDI steering category."""

    model_config = {"from_attributes": True}

    version: str = Field("1.0.0", description="Datenbankversion")
    manufacturers: list[SteeringManufacturer] = Field(
        ...,
        description="Liste aller Hersteller",
    )
    last_updated: date = Field(
        ...,
        description="Letztes Update",
    )
```

### ANHANG R — Visual-Analysis-Prompt-Modell

```python
class VisualAnalysisTarget(str, Enum):
    """What to analyze in the photo."""
    WHEEL_OVERVIEW = "wheel_overview"
    WHEEL_GRIP_DETAIL = "wheel_grip_detail"
    WHEEL_HUB_SPOKES = "wheel_hub_spokes"
    TILLER_OVERVIEW = "tiller_overview"
    TILLER_RUDDER_HEAD = "tiller_rudder_head"
    PEDESTAL_BASE = "pedestal_base"
    CABLE_CHAIN = "cable_chain"
    CORROSION_DETAIL = "corrosion_detail"
    SIGHTLINE_CHECK = "sightline_check"


class SteeringVisualAnalysisRequest(BaseModel):
    """Request model for visual analysis of steering components."""

    model_config = {"from_attributes": True}

    photo_ids: list[str] = Field(
        ...,
        min_length=1,
        max_length=10,
        description="IDs der hochgeladenen Fotos",
    )
    analysis_targets: list[VisualAnalysisTarget] = Field(
        ...,
        min_length=1,
        description="Was soll analysiert werden?",
    )
    boat_class: Optional[str] = Field(
        None,
        description="Bootsklasse für kalibrierte Bewertung",
    )
    boat_loa_mm: Optional[int] = Field(
        None,
        ge=4000,
        le=30000,
        description="Bootslänge für Kontext",
    )
    known_manufacturer: Optional[str] = Field(
        None,
        description="Bekannter Hersteller des Steuerrades (falls bekannt)",
    )
    known_age_years: Optional[int] = Field(
        None,
        ge=0,
        le=100,
        description="Bekanntes Alter der Komponente in Jahren",
    )
    user_complaint_de: Optional[str] = Field(
        None,
        description="Vom Benutzer beschriebenes Problem auf Deutsch",
    )


class SteeringVisualAnalysisResult(BaseModel):
    """Result model for visual analysis of steering components."""

    model_config = {"from_attributes": True}

    request_id: str = Field(
        ...,
        description="Referenz auf die Analyse-Anfrage",
    )
    identified_manufacturer: Optional[str] = Field(
        None,
        description="Erkannter Hersteller",
    )
    identified_manufacturer_confidence: Optional[ConfidenceLevel] = Field(
        None,
        description="Confidence der Hersteller-Erkennung",
    )
    identified_type: Optional[SteeringType] = Field(
        None,
        description="Erkannter Steuerungstyp",
    )
    identified_design: Optional[WheelDesign] = Field(
        None,
        description="Erkanntes Rad-Design",
    )
    estimated_diameter_mm: Optional[int] = Field(
        None,
        description="Geschätzter Raddurchmesser (aus Foto-Proportion)",
    )
    grip_material_detected: Optional[GripMaterial] = Field(
        None,
        description="Erkanntes Griffmaterial",
    )
    frame_material_detected: Optional[FrameMaterial] = Field(
        None,
        description="Erkanntes Rahmenmaterial",
    )
    condition_score: Optional[float] = Field(
        None,
        ge=0,
        le=100,
        description="Zustandsbewertung 0–100 (visuell)",
    )
    findings: list[SteeringFinding] = Field(
        default_factory=list,
        description="Visuell erkannte Befunde",
    )
    overall_confidence: ConfidenceLevel = Field(
        ...,
        description="Gesamt-Confidence der visuellen Analyse",
    )
    analysis_notes_de: Optional[str] = Field(
        None,
        description="Freitext-Notizen der Analyse auf Deutsch",
    )
    not_assessable_reasons_de: list[str] = Field(
        default_factory=list,
        description="Liste der Aspekte, die nicht beurteilbar waren (mit Begründung)",
    )
    model_version: str = Field(
        ...,
        description="Version des verwendeten AI-Modells",
    )
    prompt_version: str = Field(
        ...,
        description="Version des verwendeten Analyse-Prompts",
    )
```

---

> **Ende der AYDI Wissensdatei 20.04 — Steuerräder und Pinnen**
> **Umfang:** ~3.800 Zeilen | **Version:** 1.0.0 | **Datum:** 2026-05-02
> **Nächste Revision geplant:** Bei Ergänzung weiterer Hersteller oder neuer ISO-Normen
