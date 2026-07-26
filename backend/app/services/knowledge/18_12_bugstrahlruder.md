---
titel: "Bug- und Heckstrahlruder"
kategorie: "Motoren und Antrieb"
unterkategorie: "Bugstrahlruder"
version: "2.0"
letzte_aktualisierung: "2026-04"
autor: "AYDI Maritime Knowledge Base"
---

# 18_12 — Bug- und Heckstrahlruder

---

## Inhaltsverzeichnis

1. [Einführung](#1-einführung)
2. [Grundlagen und Funktionsprinzip](#2-grundlagen-und-funktionsprinzip)
3. [Typen von Strahlrudern](#3-typen-von-strahlrudern)
4. [Tunnel-Thruster im Detail](#4-tunnel-thruster-im-detail)
5. [Einziehbare (Retractable) Thruster](#5-einziehbare-retractable-thruster)
6. [Externe Thruster](#6-externe-thruster)
7. [Heckstrahlruder](#7-heckstrahlruder)
8. [Elektrischer vs. hydraulischer Antrieb](#8-elektrischer-vs-hydraulischer-antrieb)
9. [Dimensionierung und Auslegung](#9-dimensionierung-und-auslegung)
10. [Tunnelrohr — Einbau und Spezifikation](#10-tunnelrohr--einbau-und-spezifikation)
11. [Elektrische Installation](#11-elektrische-installation)
12. [Steuerung und Bedienung](#12-steuerung-und-bedienung)
13. [Anoden und Korrosionsschutz](#13-anoden-und-korrosionsschutz)
14. [Hersteller: Vetus (Niederlande)](#14-hersteller-vetus-niederlande)
15. [Hersteller: Side-Power / Sleipner (Norwegen)](#15-hersteller-side-power--sleipner-norwegen)
16. [Hersteller: Lewmar (UK)](#16-hersteller-lewmar-uk)
17. [Hersteller: Max Power (Italien)](#17-hersteller-max-power-italien)
18. [Hersteller: Quick (Italien)](#18-hersteller-quick-italien)
19. [Hersteller: Imtra / Anchorlift (USA)](#19-hersteller-imtra--anchorlift-usa)
20. [Herstellervergleich und Cross-Referenz](#20-herstellervergleich-und-cross-referenz)
21. [Fehlerbild-Atlas](#21-fehlerbild-atlas)
22. [Troubleshooting-Entscheidungsbaum](#22-troubleshooting-entscheidungsbaum)
23. [Wartung und Inspektion](#23-wartung-und-inspektion)
24. [FAQ — Häufige Fragen](#24-faq--häufige-fragen)
25. [Glossar](#25-glossar)
26. [Fallstudien](#26-fallstudien)
27. [ANHANG A: Normen und Vorschriften](#27-anhang-a-normen-und-vorschriften)
28. [ANHANG B: Confidence-Mapping](#28-anhang-b-confidence-mapping)
29. [ANHANG C: Pydantic v2 Datenmodelle](#29-anhang-c-pydantic-v2-datenmodelle)
30. [ANHANG D: AYDI Bewertungsschema](#30-anhang-d-aydi-bewertungsschema)

---

## 1. Einführung

### 1.1 Bedeutung von Strahlrudern im modernen Yachtbau

Bug- und Heckstrahlruder (englisch: bow and stern thrusters) gehören heute zur Standardausrüstung moderner Motor- und Segelyachten ab ca. 9 Metern Länge. Sie ermöglichen Querbewegungen des Boots bei niedrigen Geschwindigkeiten und sind damit unverzichtbar für sichere Hafenmanöver, Anlegemanöver in Seitenwind und das Navigieren in engen Marinas.

Die steigende Bootsgröße im Freizeitbereich, kombiniert mit immer engeren Liegeplatzverhältnissen in europäischen Marinas, hat Bugstrahlruder von einer Luxusoption zu einer praktischen Notwendigkeit gemacht. Während in den 1990er-Jahren nur ca. 15% der Neuboote über 10m mit Bugstrahlruder ausgeliefert wurden, liegt die Quote 2025 bei über 80%.

### 1.2 Grundbegriffe

| Begriff | Erklärung |
|---------|-----------|
| Bugstrahlruder (BSR) | Querschub-Antrieb im Vorschiffsbereich |
| Heckstrahlruder (HSR) | Querschub-Antrieb im Heckbereich |
| Thruster | Englischer Oberbegriff für alle Strahlruder |
| Tunnel-Thruster | Im Rumpf eingebautes Rohr mit Propeller |
| Retractable Thruster | Einziehbarer Thruster ohne permanentes Tunnelrohr |
| External Thruster | Außen montierter Thruster (z.B. Vetus BOW PRO GO) |
| kgf | Kilogramm-Force — Maßeinheit für Schub (1 kgf ≈ 9,81 N) |
| lbf | Pound-Force — Schubeinheit im angloamerikanischen Raum |
| Duty Cycle | Einschaltdauer — maximale Betriebszeit vor Abkühlpause |

### 1.3 Abgrenzung

Dieses Kapitel behandelt ausschließlich dedizierte Querschub-Anlagen (Thruster). Nicht behandelt werden:
- Joystick-Manöversysteme (z.B. Volvo Penta IPS, Mercury Joystick Piloting) — diese nutzen die Hauptantriebe
- Podantriebe (Azipod, Saildrive mit Strahlruder-Funktion)
- Wasserstrahlantriebe (Jet Drives)
- Seitenstrahlruder großer Schiffe (>24m, gewerbliche Schifffahrt)

---

## 2. Grundlagen und Funktionsprinzip

### 2.1 Physikalisches Prinzip

Ein Strahlruder erzeugt eine Querkraft (Seitenschub) durch Beschleunigung von Wasser quer zur Längsachse des Bootes. Der Propeller im Tunnelrohr saugt Wasser auf einer Seite an und drückt es auf der anderen Seite heraus. Nach Newtons drittem Gesetz (Actio = Reactio) bewegt sich das Boot in die entgegengesetzte Richtung.

**Schubkraft-Formel (vereinfacht):**
```
F = ṁ × Δv
F = Schubkraft [N]
ṁ = Massenstrom [kg/s]
Δv = Geschwindigkeitsänderung des Wassers [m/s]
```

**Praktische Dimensionierung:**
```
F_erforderlich [kgf] = Verdrängung [t] × Windangriffsfläche_faktor × Sicherheitsfaktor
```

### 2.2 Wirksamkeitsbereich

Strahlruder sind nur bei niedrigen Bootsgeschwindigkeiten effektiv:
- **0–3 kn:** Volle Wirksamkeit
- **3–5 kn:** Abnehmende Wirksamkeit (Wasserstrom am Rumpf überdeckt den Querstrahl)
- **>5 kn:** Praktisch unwirksam, Wasserströmung am Tunnel erzeugt Widerstand

### 2.3 Drehpunkt des Bootes

Der Drehpunkt eines Bootes liegt bei Fahrt voraus ca. 1/3 der Wasserlinie von vorn. Bei Rückwärtsfahrt verschiebt er sich nach achtern. Das Bugstrahlruder wirkt damit mit einem langen Hebelarm — daher ist der Bugstrahlruder effektiver als ein Heckstrahlruder gleicher Leistung.

**Hebelarm-Berechnung:**
```
Drehmoment_Bug = F_BSR × (2/3 × LWL)
Drehmoment_Heck = F_HSR × (1/3 × LWL)
```

Bei gleichem Drehmoment benötigt ein Heckstrahlruder daher die doppelte Schubkraft.

> ⚠️ **ZU PRÜFEN (Audit):** Drehpunkt 1/3 LWL von vorn (§2.3) vs. Bug-Hebelarm 2/3 LWL (obige Formel + §9.1/§9.5) — nicht vereinbar. Liegt der Drehpunkt 1/3 von vorn, beträgt der Bug-Hebelarm nur 1/3 LWL (dann wäre das HSR effektiver, nicht das BSR); bei Manövriergeschwindigkeit (~0 kn) liegt der Drehpunkt zudem nahe mittschiffs (Hebelarme annähernd gleich). Richtung nicht zweifelsfrei — Dimensionierungsannahme (Faktor 2/3 bzw. "doppelte Schubkraft HSR") unverifiziert.

### 2.4 Einfluss von Wind und Strömung

Die Effektivität eines Strahlruders wird maßgeblich durch externe Kräfte beeinflusst:

| Bedingung | Auswirkung | Empfehlung |
|-----------|------------|------------|
| Seitenwind 10 kn | +30% Schubkraft nötig | Standard-BSR ausreichend |
| Seitenwind 15 kn | +60% Schubkraft nötig | Überdimensionierung empfohlen |
| Seitenwind 20 kn | +100% Schubkraft nötig | Kombination BSR + HSR |
| Seitenwind 25+ kn | BSR allein oft unzureichend | Zusätzlich Hauptantrieb nutzen |
| Querstrom 0,5 kn | Wie 10 kn Seitenwind | BSR + vorausschauendes Manövrieren |
| Querstrom 1,0 kn | Wie 20 kn Seitenwind | BSR + HSR + Hauptantrieb |

### 2.5 Windangriffsfläche

Die Windangriffsfläche variiert stark je nach Bootstyp:

| Bootstyp | Lateralfläche über WL | Windempfindlichkeit |
|----------|----------------------|---------------------|
| Segelyacht 10m | 8–12 m² | Mittel (Mast als Windfahne) |
| Segelyacht 14m | 14–20 m² | Mittel–Hoch |
| Motoryacht 10m | 10–15 m² | Mittel |
| Motoryacht 14m (Flybridge) | 20–30 m² | Hoch |
| Motoryacht 18m (Flybridge) | 35–50 m² | Sehr hoch |
| Katamaran 12m | 15–25 m² | Hoch (breites Profil) |

---

## 3. Typen von Strahlrudern

### 3.1 Übersicht

```
Strahlruder
├── Tunnel-Thruster (fest eingebaut)
│   ├── Elektrisch
│   │   ├── 12V DC
│   │   ├── 24V DC
│   │   └── AC (Wechselstrom, hydraulisch-elektrisch)
│   └── Hydraulisch
│       ├── Vom Hauptmotor angetrieben
│       └── Separates Hydraulikaggregat
├── Einziehbar (Retractable)
│   ├── Elektrisch
│   └── Hydraulisch
├── Extern (External / Bolt-On)
│   ├── Bug-montiert
│   └── Heck-montiert
└── Heckstrahlruder
    ├── Tunnel (wie Bugstrahlruder)
    └── Extern
```

### 3.2 Vergleich der Typen

| Merkmal | Tunnel | Retractable | External |
|---------|--------|-------------|----------|
| **Schubkraft** | 30–300+ kgf | 30–150 kgf | 20–80 kgf |
| **Widerstand bei Fahrt** | Gering (Tunnel-Effekt) | Null (eingezogen) | Mittel–Hoch |
| **Einbauaufwand** | Hoch (Rumpf-Durchbruch) | Sehr hoch | Gering |
| **Nachrüstbarkeit** | Schwierig (Slipanlage nötig) | Schwierig | Einfach |
| **Wartungszugang** | Nur im Wasser oder auf Slip | Komplex | Einfach |
| **Geräusch** | Mittel–Laut | Leise–Mittel | Mittel |
| **Typische Bootsgröße** | 8–30m+ | 10–25m | 6–14m |
| **Preisspanne** | 800–15.000 EUR | 3.000–25.000 EUR | 500–3.000 EUR |

### 3.3 Entscheidungsmatrix für Bootstyp

| Bootstyp/Situation | Empfehlung | Begründung |
|---------------------|-----------|------------|
| Segelyacht 8–12m, Nachrüstung | External oder kleiner Tunnel | Minimaler Eingriff, Budget |
| Segelyacht 12–16m, Neubau | Tunnel 125–150mm Ø | Standard bei Herstellern |
| Segelyacht 16m+, Performance | Retractable | Kein Widerstand unter Segeln |
| Motoryacht 8–12m | Tunnel 150mm Ø | Standardlösung |
| Motoryacht 12–18m | Tunnel 185–250mm Ø | Ausreichend Schub für Windangriffsfläche |
| Motoryacht 18m+, Flybridge | Tunnel 250–300mm Ø + HSR | Große Windangriffsfläche |
| Katamaran 10–14m | 2× Tunnel oder 1× starker Tunnel | Breites Boot, hohe Windangriffsfläche |

---

## 4. Tunnel-Thruster im Detail

### 4.1 Aufbau

Ein Tunnel-Thruster besteht aus folgenden Komponenten:

1. **Tunnelrohr** (GFK, Aluminium oder Edelstahl)
   - Durchmesser: 110–300mm (Standard-Reihe: 125, 150, 160, 185, 200, 250, 300mm)
   - Wandstärke: 3–8mm je nach Material
   - Einlaminiert oder verschraubt im Rumpf
2. **Propeller** (Kunststoff oder Bronze)
   - 2–4 Blätter
   - Durchmesser passend zum Tunnelrohr (z.B. 145mm Propeller in 150mm Tunnel)
   - Austauschbar als Verschleißteil
3. **Motor** (DC-Elektromotor oder Hydraulikmotor)
   - Eingebaut im Tunnelrohr (Unterwasser) oder im Boot oberhalb der Wasserlinie
   - Gekapselt gegen Wassereintritt (IP68)
4. **Getriebestufe** (bei den meisten Modellen)
   - Kegelrad- oder Schneckengetriebe
   - Umlenkung der Motorachse um 90° zum Propeller
5. **Dichtungen und Lager**
   - Wellendichtring (Simmerring) oder Gleitringdichtung
   - Kugellagersatz für Propellerwelle
6. **Gitter / Schutzgitter**
   - Beidseitig am Tunnelrohr
   - Schützt vor Fremdkörpern (Leinen, Seetang, Plastik)
   - Reduziert Schub um ca. 5–10%

### 4.2 Tunnelrohr-Durchmesser und Schubkraft

| Tunnel-Ø [mm] | Typische Schubkraft [kgf] | Typische Bootsgröße [m] |
|----------------|---------------------------|-------------------------|
| 110 | 20–35 | 6–8 |
| 125 | 30–55 | 8–10 |
| 150 | 45–80 | 10–13 |
| 160 | 55–95 | 11–14 |
| 185 | 70–120 | 13–17 |
| 200 | 90–150 | 15–20 |
| 250 | 130–230 | 18–25 |
| 300 | 200–340 | 22–30+ |

### 4.3 Tunnelposition im Rumpf

**Optimale Position:**
- So weit vorne wie möglich (maximaler Hebelarm)
- Mindestens 1× Tunnel-Ø unter der Wasserlinie (bei leichtester Beladung)
- Mindestens 0,5× Tunnel-Ø über dem Kiel (Strömung muss frei ein-/austreten)
- Tunnel-Achse horizontal (±2° Toleranz)

**Typische Einbauposition:**
- Segelyacht: Station 10–15% der LWL von vorn
- Motoryacht: Station 5–12% der LWL von vorn (breiterer Bug erlaubt weiter vorn)
- Mindestabstand zur Bugverkleidung: 300mm

**Problematische Positionen:**
- Zu nah an der Wasserlinie: Luft wird angesaugt, Schubverlust
- Zu tief: erhöhter Strömungswiderstand bei Fahrt
- Zu weit achtern: reduzierter Hebelarm, weniger effektiv
- Schräg eingebaut: asymmetrischer Schub, erhöhter Verschleiß

### 4.4 Tunnelrohr-Materialien

| Material | Vorteile | Nachteile | Typisch für |
|----------|---------|-----------|-------------|
| GFK (glasfaserverstärkter Kunststoff) | Leicht, keine Korrosion, einfach laminierbar | Kann delaminieren bei schlechtem Einbau | Serien-Einbau, GFK-Rümpfe |
| Aluminium (5083/5086) | Leicht, korrosionsbeständig | Galvanische Korrosion bei Kontakt mit Bronze | Alu-Rümpfe |
| Edelstahl 316L | Sehr stabil, korrosionsbeständig | Schwer, teuer | Superyachten, Stahlrümpfe |
| Kunststoff (PE/PVC) | Leicht, keine Korrosion, günstig | Begrenzte Festigkeit | Kleinere Boote, Nachrüstung |

### 4.5 Propeller-Materialien und -Typen

**Kunststoff-Propeller (Standard):**
- Material: glasfaserverstärktes Polyamid (PA6-GF30)
- Vorteile: günstig, austauschbar, keine galvanische Korrosion
- Nachteile: geringere Effizienz, Verschleiß bei Sand/Schmutz
- Lebensdauer: 3–8 Jahre
- Preis: 40–120 EUR

**Bronze-Propeller (Premium):**
- Material: Manganbronze oder Nickelaluminiumbronze (NAB)
- Vorteile: höhere Effizienz (+5–10%), langlebiger, reparierbar
- Nachteile: teuer, galvanische Korrosion möglich, schwerer
- Lebensdauer: 10–20+ Jahre
- Preis: 150–450 EUR

**Edelstahl-Propeller:**
- Material: Edelstahl 316L
- Vorteile: sehr langlebig, hohe Festigkeit
- Nachteile: galvanische Korrosion mit Alu-Tunnelrohr, teuer
- Einsatz: selten, nur bei Spezialanwendungen

### 4.6 Doppel-Propeller-Systeme

Einige Hersteller (insbesondere Side-Power und Vetus) bieten Systeme mit zwei gegenläufigen Propellern im selben Tunnelrohr:

- **Vorteil:** Höherer Schub bei gleichem Tunnel-Ø, weniger Drall-Verluste
- **Nachteil:** Komplexer, teurer, mehr Wartung
- **Schubgewinn:** ca. 20–30% gegenüber Einzelpropeller
- **Typischer Einsatz:** Große Motoryachten 18m+

---

## 5. Einziehbare (Retractable) Thruster

### 5.1 Funktionsprinzip

Retractable Thruster werden im Rumpfinneren verstaut und nur bei Bedarf durch eine Öffnung im Rumpf nach unten ausgefahren. Sie haben kein permanentes Tunnelrohr und erzeugen daher bei Fahrt keinen zusätzlichen Widerstand.

**Aufbau:**
1. Thruster-Einheit mit Propeller (horizontal oder vertikal)
2. Hubmechanismus (elektrisch oder hydraulisch)
3. Rumpföffnung mit Dichtungsklappe
4. Steuereinheit

**Ausfahrvorgang:**
1. Steuerbefehl → Dichtungsklappe öffnet
2. Thruster fährt nach unten aus (ca. 15–30 Sekunden)
3. Endposition → Verriegelung → Betriebsbereit
4. Nach Gebrauch: Einfahren → Klappe schließt → bündig mit Rumpf

### 5.2 Vorteile und Nachteile

**Vorteile:**
- Kein Strömungswiderstand bei eingefahrenem Thruster
- Ideal für Performance-Segelyachten und schnelle Motoryachten
- Kein Tunnel im Bug → keine Strömungsgeräusche
- Kann nachgerüstet werden (kein Tunnelrohr-Einbau)

**Nachteile:**
- Hohe Kosten (3–10× teurer als Tunnel-Thruster)
- Komplexe Mechanik → höherer Wartungsaufwand
- Langsamere Einsatzbereitschaft (15–30s Ausfahrzeit)
- Mehr Einbauraum im Boot nötig
- Dichtungsklappe als potenzielle Undichtigkeitsstelle
- Weniger Schubkraft als vergleichbarer Tunnel-Thruster

### 5.3 Hersteller und Modelle

| Hersteller | Modell | Schub [kgf] | Antrieb | Preis [EUR] |
|------------|--------|-------------|---------|-------------|
| Side-Power | EX Series | 40–95 | Elektrisch 24V | 5.500–12.000 |
| Lewmar | RT Series | 55–120 | Hydraulisch | 6.000–15.000 |
| Max Power | Retract | 40–100 | Elektrisch 24V | 4.500–11.000 |
| Quick | TCRB Series | 60–140 | Hydraulisch | 7.000–18.000 |
| Vetus | RETRACT | 50–110 | Elektrisch 24V | 5.000–13.000 |
| ABT (American Bow Thruster) | TRAC | 50–160 | Hydraulisch | 8.000–25.000 |

### 5.4 Einbauraum-Anforderungen

| Schubklasse [kgf] | Min. Einbauhöhe [mm] | Min. Breite [mm] | Min. Tiefe [mm] |
|--------------------|---------------------|-------------------|-----------------|
| 40–60 | 500 | 350 | 400 |
| 60–100 | 650 | 400 | 500 |
| 100–150 | 800 | 500 | 600 |

---

## 6. Externe Thruster

### 6.1 Funktionsprinzip

Externe Thruster werden außen am Rumpf montiert — entweder unterhalb der Wasserlinie am Bug oder am Heck. Sie erfordern keinen Rumpfdurchbruch (nur Kabeldurchführung) und sind daher ideal für die Nachrüstung.

### 6.2 Typen externer Thruster

**Feststehend extern:**
- Permanent am Rumpf montiert (Flansch/Konsole)
- Einfacher Aufbau, geringe Kosten
- Erhöhter Widerstand bei Fahrt
- Beispiel: Vetus BOW PRO, Side-Power EX

**Klappbar extern:**
- Einklappbar bei Fahrt
- Reduzierter Widerstand
- Mechanisch komplexer
- Beispiel: Vetus BOW PRO GO (klappbar)

**Trailer-Boot extern:**
- Temporär montierbar (Saugnapf, Klemme)
- Für Boote ohne feste Installation
- Begrenzte Schubkraft (10–30 kgf)
- Beispiel: Docksafe, EasyDock Thruster

### 6.3 Vor- und Nachteile

**Vorteile:**
- Kein Rumpfdurchbruch nötig
- Einfache Nachrüstung (oft an einem Tag)
- Geringere Kosten als Tunnel-Thruster
- Einfache Wartung (Boot muss nicht geslippt werden)

**Nachteile:**
- Geringere Schubkraft (max. ca. 80 kgf)
- Erhöhter Strömungswiderstand bei Fahrt
- Optisch weniger ansprechend
- Beschädigungsrisiko bei Grundberührung
- Bewuchsgefahr an freiliegenden Komponenten

### 6.4 Vetus BOW PRO Serie

| Modell | Schub [kgf] | Spannung | Leistung [W] | Tunnel-Ø [mm] | Preis [EUR] |
|--------|-------------|----------|-------------|----------------|-------------|
| BOW PRO 36 | 36 | 12V | 1.000 | Extern | 1.250 |
| BOW PRO 46 | 46 | 12V | 1.500 | Extern | 1.550 |
| BOW PRO 57 | 57 | 12V | 2.000 | Extern | 1.850 |
| BOW PRO 76 | 76 | 24V | 2.500 | Extern | 2.350 |
| BOW PRO GO 36 | 36 | 12V | 1.000 | Extern, klappbar | 1.650 |
| BOW PRO GO 46 | 46 | 12V | 1.500 | Extern, klappbar | 1.950 |

---

## 7. Heckstrahlruder

### 7.1 Wann ein Heckstrahlruder sinnvoll ist

Ein Heckstrahlruder ergänzt das Bugstrahlruder und ermöglicht echte Seitwärtsfahrt (Crabbing). Es ist besonders sinnvoll bei:

- **Große Motoryachten (>14m):** Hohe Windangriffsfläche, Bug- und Heckversatz gleichzeitig steuern
- **Flybridge-Yachten:** Extreme Windangriffsfläche durch Aufbauten
- **Einschrauber mit hohem Heck:** Hauptantrieb kann Heck nicht effektiv seitlich bewegen
- **Engen Marinas:** Seitwärts in die Box fahren (Crabbing-Manöver)
- **Charter- und Ausbildungsboote:** Vereinfachte Manöver für weniger erfahrene Skipper

### 7.2 Besonderheiten beim Einbau am Heck

Im Gegensatz zum Bug ist das Heck eines Bootes konstruktiv anders aufgebaut:

- **Motoryacht:** Breites Heck, Badeplattform, oft Transom-Stern → Tunnel-Einbau seitlich möglich
- **Segelyacht:** Schmales Heck, Ruderblatt, Antriebswelle → begrenzter Platz für Tunnel
- **Katamaran:** Tunnel in jedem Rumpf oder zentraler Tunnel im Brückendeck

**Einbauherausforderungen:**
- Nähe zu Hauptantrieb und Ruder → Vibrationsübertragung
- Abgassystem und Tanks im Heckbereich → Platzkonflikt
- Badeplattform/Garage → eingeschränkter Zugang
- Bei Segelyachten: Ruderblatt und Kiel im Weg

### 7.3 Dimensionierung Heckstrahlruder

Da der Hebelarm am Heck kürzer ist (ca. 1/3 LWL vom Drehpunkt), muss ein Heckstrahlruder stärker sein als das Bugstrahlruder, um denselben Dreheffekt zu erzielen:

**Faustregel:**
```
Schub_HSR = Schub_BSR × 1,3 bis 1,5
```

Für echte Seitwärtsfahrt (Crabbing) sollten BSR und HSR zusammen mindestens die Verdrängung × 0,015 als Schubkraft aufbringen:

```
Schub_gesamt [kgf] ≥ Verdrängung [kg] × 0,015
```

### 7.4 Kombinierte Systeme (BSR + HSR)

| Bootsgröße [m] | BSR [kgf] | HSR [kgf] | Gesamt [kgf] | Typische Kombination |
|----------------|-----------|-----------|-------------|----------------------|
| 12–14 | 55–80 | 70–100 | 125–180 | Vetus 55/80 + Vetus 80/100 |
| 14–18 | 80–120 | 100–160 | 180–280 | Side-Power SE80/SP100 |
| 18–22 | 120–185 | 160–240 | 280–425 | Hydraulisch empfohlen |
| 22–30 | 185–300 | 240–400 | 425–700 | Hydraulisch zwingend |

---

## 8. Elektrischer vs. hydraulischer Antrieb

### 8.1 Elektrischer Antrieb

**Funktionsprinzip:**
Ein DC-Elektromotor (12V oder 24V) treibt den Propeller direkt oder über ein Getriebe an. Der Motor wird über ein Leistungsrelais (Solenoid) geschaltet und zieht Strom direkt aus der Bordbatterie.

**12V-Systeme:**
- Typisch für Boote 8–14m
- Schubkraft: 30–100 kgf
- Stromaufnahme: 80–400A
- Einfache Installation (vorhandenes 12V-Bordnetz)
- Batterie: mindestens 100Ah dedizierte Thruster-Batterie empfohlen

**24V-Systeme:**
- Typisch für Boote 12–22m
- Schubkraft: 50–200 kgf
- Stromaufnahme: 60–250A (halbe Stromstärke bei gleicher Leistung)
- Dünnere Kabel möglich, geringere Verluste
- Separate 24V-Bank oder 2× 12V in Reihe

**Vorteile elektrisch:**
- Einfache Installation
- Geringere Kosten (System + Einbau)
- Kein laufender Hauptmotor nötig
- Sofort einsatzbereit (kein Aufwärmen)
- Geringerer Wartungsaufwand

**Nachteile elektrisch:**
- Begrenzte Einschaltdauer (Duty Cycle)
- Hohe Stromaufnahme → dicke Kabel, große Batterien
- Batterie-Abhängigkeit
- Geringere Schubkraft bei gleicher Baugröße

### 8.2 Hydraulischer Antrieb

**Funktionsprinzip:**
Eine Hydraulikpumpe (angetrieben vom Hauptmotor oder einem separaten Elektromotor) erzeugt Öldruck, der einen Hydraulikmotor am Propeller antreibt.

**Vom Hauptmotor angetrieben:**
- Hydraulikpumpe am Motor (z.B. über Keilriemen)
- Hauptmotor muss laufen
- Typisch für Boote >16m
- Unbegrenzte Einschaltdauer (solange Motor läuft)

**Separates Hydraulikaggregat:**
- Eigener Elektromotor treibt Hydraulikpumpe
- Unabhängig vom Hauptmotor
- Höhere Kosten, mehr Platz
- Typisch bei Nachrüstung auf großen Yachten

**Vorteile hydraulisch:**
- Unbegrenzte Einschaltdauer (kein Duty Cycle)
- Höhere Schubkraft möglich (bis 500+ kgf)
- Kein hoher Gleichstrom → keine dicken DC-Kabel
- Leiser Betrieb (Hydraulikmotor am Propeller ist klein und leise)
- Kann mehrere Verbraucher bedienen (BSR + HSR + Ankerwinde + Stabilisatoren)

**Nachteile hydraulisch:**
- Höhere Kosten (System + Installation)
- Komplexer (Leitungen, Filter, Öl, Pumpe)
- Hauptmotor muss laufen (bei PTO-System)
- Ölverlust als Umweltrisiko
- Mehr Wartung (Öl, Filter, Schläuche, Dichtungen)

### 8.3 Vergleichstabelle

| Kriterium | Elektrisch 12V | Elektrisch 24V | Hydraulisch |
|-----------|---------------|---------------|-------------|
| Typische Bootsgröße | 8–14m | 12–22m | 16–30m+ |
| Max. Schub | ~100 kgf | ~200 kgf | 500+ kgf |
| Duty Cycle | 2–4 min on, 8–15 min off | 3–5 min on, 8–15 min off | Unbegrenzt |
| Stromaufnahme | 80–400A | 60–250A | 5–20A (Ventil) |
| Kabelquerschnitt | 50–95 mm² | 35–70 mm² | Hydraulikschläuche |
| Systemkosten | 800–4.000 EUR | 1.200–7.000 EUR | 3.000–18.000 EUR |
| Einbaukosten | 500–1.500 EUR | 800–2.500 EUR | 2.000–6.000 EUR |
| Wartungskosten/Jahr | 50–150 EUR | 50–150 EUR | 200–500 EUR |
| Geräusch | Mittel–Laut | Mittel | Leise–Mittel |
| Reaktionszeit | Sofort | Sofort | 1–3 Sekunden |

### 8.4 Duty Cycle — Details

Der Duty Cycle (Einschaltdauer) ist die kritischste Betriebseinschränkung elektrischer Thruster. Er wird durch die thermische Belastung des Motors bestimmt.

**Typische Duty Cycles:**

| Klasse | Betrieb | Pause | Zyklen/Stunde | Bemerkung |
|--------|---------|-------|---------------|-----------|
| Intermittierend (S2) | 2 min | 8 min | 6 | Preiswertes Segment |
| Semi-Dauerbetrieb (S3) | 4 min | 6 min | 6 | Mittleres Segment |
| Quasi-Dauerbetrieb (S4) | 5 min | 5 min | 6 | Premium-Segment |
| Schwerlast | 3 min | 15 min | 3–4 | Überdimensioniert |

**Warnung:** Überschreitung des Duty Cycle führt zu:
1. Überhitzung der Motorwicklungen
2. Schmelzen der Isolation → Kurzschluss
3. Verformung der Kohlebürsten (bei Bürstenmotoren)
4. Dauerhafte Beschädigung des Motors
5. Im Extremfall: Brand an Bord

**Thermoschutz:**
- Hochwertige Thruster haben einen eingebauten Thermoschutz
- Abschalttemperatur: typisch 120–140°C am Motor
- Automatische Wiedereinschaltung nach Abkühlung
- Vetus, Side-Power, Quick: Thermoschutz bei allen Modellen ab mittlerer Preisklasse

---

## 9. Dimensionierung und Auslegung

### 9.1 Grundformel

Die erforderliche Schubkraft hängt von mehreren Faktoren ab:

```
F_erforderlich [kgf] = A_lateral × p_wind × C_d × L_faktor / L_hebelarm
```

Wobei:
- A_lateral = Lateralfläche über Wasser [m²]
- p_wind = Winddruck [kgf/m²] (bei 15 kn ≈ 3,5 kgf/m²)
- C_d = Widerstandsbeiwert (0,8–1,2 je nach Aufbauform)
- L_faktor = Sicherheitsfaktor (1,3–1,5)
- L_hebelarm = Hebelarm des Thrusters [m] (typisch 2/3 × LWL für BSR)

### 9.2 Vereinfachte Dimensionierung nach Bootslänge

Für die schnelle Auslegung wird in der Praxis oft eine vereinfachte Tabelle verwendet:

**Segelyachten:**

| Bootslänge [m] | Verdrängung [t] | Min. Schub [kgf] | Empfohlen [kgf] | Tunnel-Ø [mm] |
|----------------|-----------------|-------------------|------------------|----------------|
| 8–9 | 3–5 | 25 | 35 | 110–125 |
| 9–10 | 4–7 | 30 | 45 | 125 |
| 10–11 | 6–9 | 40 | 55 | 125–150 |
| 11–12 | 8–12 | 50 | 65 | 150 |
| 12–13 | 10–15 | 60 | 80 | 150–160 |
| 13–14 | 12–18 | 70 | 95 | 160–185 |
| 14–16 | 15–25 | 85 | 120 | 185–200 |
| 16–18 | 20–35 | 110 | 150 | 200–250 |
| 18–20 | 30–50 | 140 | 185 | 250 |
| 20–25 | 45–80 | 180 | 240 | 250–300 |

**Motoryachten (höhere Windangriffsfläche):**

| Bootslänge [m] | Verdrängung [t] | Min. Schub [kgf] | Empfohlen [kgf] | Tunnel-Ø [mm] |
|----------------|-----------------|-------------------|------------------|----------------|
| 8–9 | 3–6 | 30 | 45 | 125 |
| 9–10 | 5–8 | 40 | 55 | 125–150 |
| 10–11 | 7–11 | 50 | 70 | 150 |
| 11–12 | 9–14 | 60 | 85 | 150–160 |
| 12–13 | 12–18 | 75 | 100 | 160–185 |
| 13–14 | 15–22 | 90 | 120 | 185 |
| 14–16 | 18–30 | 110 | 150 | 185–200 |
| 16–18 | 25–40 | 140 | 185 | 200–250 |
| 18–20 | 35–55 | 175 | 230 | 250 |
| 20–25 | 50–90 | 220 | 300 | 250–300 |
| 25–30 | 80–150 | 300 | 400 | 300+ |

### 9.3 Katamarane

Katamarane haben eine überproportional große Windangriffsfläche bei relativ geringer Verdrängung. Die Dimensionierung sollte 20–40% über den Werten für Einrumpf-Motoryachten liegen.

| Katamaran-Länge [m] | Empfohlen [kgf] | Konfiguration |
|---------------------|-----------------|---------------|
| 10–12 | 65–90 | 1× zentraler Tunnel |
| 12–14 | 90–130 | 1× stark oder 2× mittel |
| 14–16 | 130–180 | 2× Tunnel (je Rumpf) |
| 16–18 | 180–250 | 2× Tunnel (je Rumpf) |

### 9.4 Überdimensionierung vs. Unterdimensionierung

**Überdimensionierung (+20–30% über Empfehlung):**
- Vorteile: Reserve bei Starkwind, kürzere Betriebszeit → weniger Duty-Cycle-Probleme
- Nachteile: Höhere Kosten, größerer Tunnel → mehr Widerstand
- Empfehlung: In Starkwind-Revieren (Nordsee, Mistral-Zone) sinnvoll

**Unterdimensionierung:**
- Häufigste Fehlerquelle bei Eignerbeschwerden
- „Der Thruster bringt nichts" → fast immer unterdimensioniert
- Kosten der Nachrüstung eines größeren Thrusters: 3–5× der Differenz zum richtigen Modell

### 9.5 Beispielrechnung

**Boot:** Motoryacht 14m, Flybridge, Verdrängung 15t
- Lateralfläche über WL: ca. 25 m²
- Windangriffsfläche Flybridge: ca. 8 m² zusätzlich
- Gesamt-Lateralfläche: ca. 33 m²
- Winddruck bei 15 kn Seitenwind: 3,5 kgf/m²
- Widerstandsbeiwert Flybridge: C_d = 1,1
- Windkraft: 33 × 3,5 × 1,1 = 127 kgf
- Hebelarm BSR: 2/3 × 12,5m (LWL) = 8,3m
- Erforderliches Drehmoment: 127 × 8,3 = 1.054 kgf·m
- Schub BSR: 1.054 / 8,3 = 127 kgf → Empfehlung: 150 kgf BSR
- Sicherheitsfaktor ×1,3: 165 kgf → Tunnel 200mm Ø

---

## 10. Tunnelrohr — Einbau und Spezifikation

### 10.1 Tunnelrohr-Durchmesser (Industriestandard)

| Außen-Ø [mm] | Innen-Ø [mm] | Wandstärke [mm] | Hersteller-Kompatibilität |
|-------------|-------------|-----------------|--------------------------|
| 110 | 104 | 3 | Vetus BOW25/30, Max Power CT25 |
| 125 | 119 | 3 | Vetus BOW35/45, Side-Power SE30/40, Max Power CT35 |
| 150 | 143 | 3,5 | Vetus BOW55/75, Side-Power SE60/80, Lewmar 140TT |
| 160 | 152 | 4 | Side-Power SE100, Max Power CT60/80 |
| 185 | 176 | 4,5 | Vetus BOW95/125, Side-Power SP100/125, Lewmar 185TT |
| 200 | 190 | 5 | Quick BTDC, Max Power CT100/125 |
| 250 | 238 | 6 | Vetus BOW160/230, Side-Power SP155/190 |
| 300 | 286 | 7 | Vetus BOW285/340, Side-Power SP240/300 |

### 10.2 Einbau des Tunnelrohrs in GFK-Rümpfe

**Werkzeuge und Material:**
- Lochsäge oder Stichsäge (beidseitig)
- Schleifmaschine mit 80er/120er Schleifscheiben
- Epoxidharz + Härter (z.B. West System 105/206)
- Glasfasermatten (300g/m² und 600g/m² Biaxial)
- Thixotropiermittel (Silica, Baumwollflocken)
- Abklebeband, Trennmittel
- Wasserwaage, Winkelmesser
- Schutzausrüstung (Handschuhe, Atemschutz, Brille)

**Einbau-Schritte:**

**Schritt 1: Positionsbestimmung**
- Boot aufrecht und waagerecht ausrichten
- Wasserlinie markieren (bei leichtester und schwerster Beladung)
- Tunnel-Mittelachse: min. 1,5× Tunnel-Ø unter leichtester WL
- Position von innen und außen markieren
- Innenraum prüfen: keine Tanks, Leitungen, Schotten im Weg?

**Schritt 2: Rumpfdurchbruch**
- Kernmaterial identifizieren (wenn Sandwich-Laminat)
- Bei Sandwich-Laminat: Kern im Bereich 50mm um das Loch entfernen und mit Epoxid-Laminat auffüllen (Kernverstärkung)
- Loch beidseitig bohren (Pilotbohrung mittig, Lochsäge beidseitig)
- Schnitt sauber entgraten
- GFK-Schnittkanten mit Epoxid versiegeln (Feuchtigkeit!)

**Schritt 3: Tunnelrohr anpassen**
- Tunnelrohr auf Länge kürken (Rumpfbreite + 2× 5mm Überstand)
- Rohr-Enden beidseitig anfasen (45°, 10mm)
- Passprobe: Rohr muss spaltfrei sitzen
- Bei asymmetrischem Rumpf: Rohr entsprechend anschrägen

**Schritt 4: Einlaminieren**
- Tunnelrohr und Rumpf-Innenflächen anschleifen (80er Korn)
- Epoxid-Laminat (mindestens 3 Lagen Biaxial 600g/m²) innen und außen
- Kehle mit Epoxid-Spachtel (Thixotropiermittel) an Übergängen
- Mindestens 50mm Überlappung auf den Rumpf
- Aushärtezeit: 24h bei 20°C, dann mindestens 7 Tage vor Wasserlassen

**Schritt 5: Nachbearbeitung**
- Laminat schleifen und mit Gelcoat versiegeln
- Antifouling auf Tunnelrohr und Umgebung
- Gitter beidseitig montieren

### 10.3 Einbau in Aluminium-Rümpfe

- Tunnelrohr: Aluminium 5083 (seewasserfest)
- Verbindung: WIG-Schweißung (nicht MIG wegen Spaltkorrosion)
- Isolation zwischen Tunnelrohr und Thruster-Motor (galvanische Trennung!)
- Keine Bronzepropeller in Aluminium-Tunnel (galvanische Korrosion!)

### 10.4 Einbau in Stahlrümpfe

- Tunnelrohr: Stahl (gleiche Legierung wie Rumpf) oder Edelstahl 316L
- Verbindung: Schweißnaht (durchgehend, nicht punktgeheftet)
- Schweißnaht röntgen lassen bei professionellem Einsatz
- Korrosionsschutz: Grundierung + Antifouling innen und außen

### 10.5 Tunnelrohr-Geometrie

**Ideale Tunnelform:**
- Gerade, zylindrisch
- Keine Einengungen oder Erweiterungen im Durchflussbereich
- Einlaufkante leicht abgerundet (Radius ≥ 5mm) → weniger Strömungsverluste
- Auslaufkante gerade oder leicht trompetenförmig

**Tunnellänge:**
- Optimale Länge: 1,5–2,5× Tunnel-Ø
- Zu kurz (<1,2× Ø): Rezirkulation, Schubverlust
- Zu lang (>3× Ø): Strömungsverluste durch Reibung
- Bei breiten Booten: ggf. Leitbleche (Stator Vanes) einbauen

### 10.6 Gitter und Schutz

| Gitter-Typ | Material | Schubverlust | Schutzwirkung | Preis [EUR] |
|-------------|----------|-------------|---------------|-------------|
| Drahtgitter (Standard) | Edelstahl 316L | 5–8% | Mittel | 40–80 |
| Strömungsoptimiertes Gitter | Edelstahl 316L | 3–5% | Mittel | 80–150 |
| Lochblech | Edelstahl/Alu | 8–12% | Hoch | 50–100 |
| Fingerbreaker | Kunststoff | 2–4% | Gering (nur Personenschutz) | 20–40 |
| Ohne Gitter | — | 0% | Keine | 0 |

---

## 11. Elektrische Installation

### 11.1 Kabelquerschnitte und Stromaufnahme

Die elektrische Installation eines Thrusters ist eine der anspruchsvollsten Aufgaben im Bordnetz. Die extrem hohen Ströme erfordern sorgfältige Dimensionierung.

**12V-Systeme:**

| Schub [kgf] | Leistung [W] | Strom [A] | Kabelquerschnitt [mm²] | Max. Kabellänge [m] (3% Verlust) |
|-------------|-------------|-----------|------------------------|----------------------------------|
| 25–35 | 750–1.000 | 80–110 | 35 | 4 |
| 35–45 | 1.000–1.500 | 110–160 | 50 | 4 |
| 45–55 | 1.500–2.000 | 160–220 | 70 | 3 |
| 55–75 | 2.000–2.800 | 220–300 | 95 | 3 |
| 75–100 | 2.800–4.000 | 300–420 | 2×70 oder 120 | 2 |

**24V-Systeme:**

| Schub [kgf] | Leistung [W] | Strom [A] | Kabelquerschnitt [mm²] | Max. Kabellänge [m] (3% Verlust) |
|-------------|-------------|-----------|------------------------|----------------------------------|
| 45–65 | 1.500–2.500 | 65–110 | 35 | 6 |
| 65–95 | 2.500–4.000 | 110–175 | 50 | 5 |
| 95–130 | 4.000–5.500 | 175–240 | 70 | 4 |
| 130–180 | 5.500–8.000 | 240–350 | 95 | 4 |
| 180–250 | 8.000–12.000 | 350–500 | 120 oder 2×70 | 3 |

### 11.2 Batterie-Anforderungen

**Dedizierte Thruster-Batterie (empfohlen):**

| Thruster-Klasse | Min. Batteriekapazität | Empfohlen | Batterietyp |
|-----------------|----------------------|-----------|-------------|
| 25–55 kgf (12V) | 80 Ah | 120 Ah | AGM Deep Cycle |
| 55–100 kgf (12V) | 120 Ah | 200 Ah | AGM oder Lithium |
| 45–95 kgf (24V) | 60 Ah | 100 Ah | AGM Deep Cycle |
| 95–180 kgf (24V) | 100 Ah | 150 Ah | AGM oder Lithium |
| 180–300 kgf (24V) | 150 Ah | 250 Ah | Lithium empfohlen |

**Lithium (LiFePO4) vs. AGM:**
- Lithium liefert konstante Spannung bis 90% Entladung → konstante Schubkraft
- AGM verliert ab 50% Entladung merklich Spannung → Schubverlust
- Lithium: 3× Zyklenlebensdauer, 50% Gewichtseinsparung
- AGM: günstiger, kein spezielles Ladegerät nötig, bewährt
- Preis: Lithium ca. 2,5–3× AGM bei gleicher nutzbarer Kapazität

### 11.3 Solenoid (Leistungsrelais)

Das Solenoid schaltet den hohen Motorstrom und wird über den Bedienpanel mit niedrigem Steuerstrom angesteuert.

**Spezifikation:**
- Dauerstrom: ≥ maximaler Motorstrom + 20% Reserve
- Einschaltspitzen: bis 3× Nennstrom für 0,5s (Motoranlauf)
- Spannung: passend zum System (12V oder 24V Steuerspule)
- Ausführung: zweipolig (für Rechts-/Linkslauf) oder einzeln (2 Stück)
- Kontaktmaterial: Kupfer oder Silber (kein Zinn!)
- Befestigung: vibrationsfest, trocken, belüftet

**Typische Solenoid-Daten:**

| Hersteller | Modell | Dauerstrom [A] | Spannung | Preis [EUR] |
|------------|--------|---------------|----------|-------------|
| Vetus |?"SET0012" | 150A | 12V | 85 |
| Vetus | SET0024 | 150A | 24V | 90 |
| Side-Power | S-link Solenoid | 200A | 12/24V | 120 |
| Blue Sea | ML-RBS | 300A | 12V | 140 |
| Blue Sea | ML-RBS | 300A | 24V | 150 |
| Lewmar | Standard-Solenoid | 250A | 12/24V | 110 |

### 11.4 Sicherungen und Schutz

**Hauptsicherung:**
- Typ: ANL-Sicherung, Mega-Fuse oder Class-T-Sicherung
- Nennwert: 125–150% des maximalen Dauerstroms
- Position: innerhalb 200mm von der Batterie (ABYC-Standard)
- Keine Automaten-Sicherungen (zu langsam bei diesen Strömen)

**Sicherungsdimensionierung:**

| Motor-Nennstrom [A] | Sicherung [A] | Typ |
|---------------------|---------------|-----|
| 80–110 | 150 | ANL |
| 110–160 | 200 | ANL oder Mega |
| 160–220 | 300 | Mega oder Class-T |
| 220–300 | 400 | Class-T |
| 300–420 | 500 | Class-T |
| 420–500 | 600 | Class-T |

### 11.5 Kabelverlegung

**Grundregeln:**
- So kurz wie möglich (jeder Meter zählt bei 300A+)
- Plus- und Minuskabel zusammen verlegen (EMV)
- Keine scharfen Biegungen (min. Biegeradius = 6× Kabeldurchmesser)
- Kabeldurchführungen durch Schotten mit Gummitüllen
- Kabelschuhe: Ringkabelschuhe, hydraulisch verpresst (nicht gelötet!)
- Alle Verbindungen mit Schrumpfschlauch und Kontaktfett
- Kabel beschriften (Ampere-Rating, Quelle, Ziel)

**Häufige Installationsfehler:**
1. Zu dünner Kabelquerschnitt → Spannungsabfall → Motor dreht langsam → überhitzt
2. Kabel zu lang → gleicher Effekt
3. Schlechte Crimpungen → Übergangswiderstand → Erhitzung → Brand
4. Kabel durch Bilge verlegt → Korrosion der Kabelschuhe
5. Sicherung zu weit von Batterie → ungeschützter Kabelabschnitt
6. Massekabel an Rumpf statt an Batterie-Minuspol → Streustrom → Korrosion

### 11.6 Verdrahtungsschema

```
[Batterie +] ──► [Hauptsicherung 200mm] ──► [Kabel 70mm² rot] ──► [Solenoid] ──► [Motor +]
[Batterie -] ──► [Kabel 70mm² schwarz] ──► [Motor -]
[Solenoid Steuerung] ──► [Bedienpanel] (1,5mm² Steuerkabel)
[Batterie +] ──► [Ladegerät / Trennrelais] ──► [Hauptbatterie]
```

### 11.7 Ladeerhaltung der Thruster-Batterie

Da die Thruster-Batterie separat ist, muss sie geladen werden:
- **Trennrelais (Cyrix, VSR):** Verbindet Thruster-Batterie mit Lichtmaschine bei laufendem Motor
- **DC-DC-Ladegerät:** Lädt Thruster-Batterie gezielt (besser für Lithium)
- **Separates Ladegerät am Landstrom:** Eigenes Ladegerät für Thruster-Batterie
- **Solaranlage:** Bei ausreichender Kapazität direkt auf Thruster-Batterie

---

## 12. Steuerung und Bedienung

### 12.1 Bedienelemente

**Joystick-Panel (Standard):**
- Links/Rechts-Joystick oder Kippschalter
- Proportionalsteuerung (stufenlos) oder Ein/Aus
- LED-Anzeige: Betrieb, Überhitzung, Störung
- Spritzwassergeschützt (IP66 mindestens für Cockpit-Montage)

**Touchpanel (Premium):**
- Digitale Anzeige mit Schubkraft-Indikator
- Timer für Duty Cycle
- Batteriestand-Anzeige
- Fehlermeldungen im Klartext
- CAN-Bus-Anbindung

**Funk-Fernbedienung:**
- Kabellos, tragbar (z.B. beim Anlegen auf dem Vorschiff)
- Reichweite: 30–100m
- Batteriebetrieben (AAA oder Li-Ion Akku)
- Vorsicht: Funkstörungen möglich in dichten Marinas
- Hersteller: Side-Power, Vetus, Quick bieten passende Fernbedienungen

### 12.2 Proportionalsteuerung vs. Ein/Aus

| Merkmal | Proportional | Ein/Aus |
|---------|-------------|---------|
| Feinfühligkeit | Hoch (stufenloser Schub) | Gering (nur voller Schub) |
| Kosten | +200–600 EUR | Basis |
| Komplexität | Höher (Controller nötig) | Einfach (Solenoid) |
| Batteriebelastung | Geringer (oft weniger als max.) | Immer Maximum |
| Manövrierpräzision | Sehr gut | Akzeptabel |
| Empfehlung | Ab 12m Bootslänge | Unter 10m, Budget |

### 12.3 Integration in Gesamtsystem

Moderne Thruster können in das Boots-Managementsystem integriert werden:
- **NMEA 2000:** Schubstatus, Batteriespannung, Temperatur
- **CAN-Bus:** Herstellerspezifische Protokolle (Vetus V-CAN, Side-Power S-Link)
- **Joystick-Manöversystem:** BSR + HSR + Hauptantrieb(e) zentral gesteuert
- **Autopilot-Integration:** Automatische Querkorrektur bei GPS-Ankerung

---

## 13. Anoden und Korrosionsschutz

### 13.1 Galvanische Korrosion bei Thrustern

Ein im Seewasser arbeitender Thruster ist ein Brennpunkt galvanischer Korrosion:
- Motor (Stahl/Kupfer), Propeller (Bronze/Kunststoff), Tunnelrohr (GFK/Alu/Stahl)
- Verschiedene Metalle + Elektrolyt (Seewasser) = galvanische Zelle
- Ohne Schutz: das unedelste Metall wird aufgelöst (typisch: Aluminium-Tunnelrohr oder Stahlrumpf)

### 13.2 Anoden-Typen

| Material | Einsatz | Spannung [V vs. Ag/AgCl] | Lebensdauer |
|----------|---------|--------------------------|-------------|
| Zink (Zn) | Salzwasser | -1,05 | 12–18 Monate |
| Aluminium (Al) | Salzwasser + Brackwasser | -1,10 | 18–24 Monate |
| Magnesium (Mg) | Süßwasser | -1,70 | 6–12 Monate |

**Empfehlung:**
- Mittelmeer, Nordsee, Atlantik: Zink oder Aluminium
- Brackwasser (Ostsee, Flüsse): Aluminium
- Süßwasser (Binnenseen): Magnesium

### 13.3 Anoden am Thruster

Jeder Tunnel-Thruster hat mindestens eine Opferanode:
- **Propelleranode:** Ring- oder Scheibenform auf der Propellerwelle
- **Tunnelrohr-Anode:** Zinkanode innen im Tunnelrohr (bei Aluminium-Rohr)
- **Gehäuse-Anode:** Am Motorgehäuse (bei Bronzegehäuse)

**Wechselintervall:**
- Prüfung: jedes Antifouling (jährlich)
- Wechsel: wenn >50% verbraucht
- Sofortiger Wechsel: wenn >70% verbraucht
- Niemals ohne Anode betreiben!

### 13.4 Anoden der gängigen Hersteller

| Hersteller | Modell | Anoden-Typ | Teilenummer | Preis [EUR] |
|------------|--------|-----------|-------------|-------------|
| Vetus | BOW55–125 | Zink-Ring | SET0150 | 25–45 |
| Vetus | BOW160–340 | Zink-Ring | SET0151 | 35–65 |
| Side-Power | SE30–SE100 | Zink-Scheibe | 61180 | 20–40 |
| Side-Power | SP100–SP300 | Zink-Ring | 71190 | 30–55 |
| Lewmar | 140TT–250TT | Zink-Ring | 589011 | 25–50 |
| Max Power | CT35–CT125 | Zink-Scheibe | MPZ-XXX | 20–40 |
| Quick | BTDC Serie | Zink-Ring | QAN-XXX | 25–45 |

### 13.5 Streustrom-Korrosion

Neben galvanischer Korrosion ist Streustrom-Korrosion das größte Risiko:
- Ursache: DC-Leckstrom vom Thruster-Schaltkreis in den Rumpf/Wasser
- Effekt: 100× aggressiver als galvanische Korrosion
- Symptome: schneller Anodenverbrauch, Lochfraß an Metallen
- Prüfung: Strommessung zwischen Rumpf und Wasser (>30mA = Problem)
- Abhilfe: Galvanischer Isolator, korrekte Masseführung, keine Rumpf-Rückleiter

---

## 14. Hersteller: Vetus (Niederlande)

### 14.1 Firmenporträt

Vetus (Fokker) ist einer der weltweit größten Hersteller von Bootsausrüstung mit Sitz in Schiedam, Niederlande. Gegründet 1951, seit 2020 Teil der Yanmar-Gruppe. Vetus bietet das breiteste Sortiment an Bugstrahlrudern und hat einen geschätzten Marktanteil von 35% in Europa.

### 14.2 Tunnel-Thruster — BOW-Serie

**12V-Modelle:**

| Modell | Schub [kgf] | Tunnel-Ø [mm] | Leistung [W] | Strom [A] | Duty Cycle | Preis [EUR] |
|--------|-------------|----------------|-------------|-----------|------------|-------------|
| BOW25 | 25 | 110 | 750 | 80 | 2 min on / 8 min off | 890 |
| BOW35 | 35 | 125 | 1.000 | 110 | 2 min on / 8 min off | 1.150 |
| BOW45 | 45 | 125 | 1.500 | 150 | 3 min on / 8 min off | 1.450 |
| BOW55 | 55 | 150 | 1.750 | 180 | 3 min on / 8 min off | 1.750 |
| BOW75 | 75 | 150 | 2.500 | 260 | 3 min on / 10 min off | 2.250 |
| BOW95 | 95 | 185 | 3.500 | 350 | 4 min on / 10 min off | 2.850 |

**24V-Modelle:**

| Modell | Schub [kgf] | Tunnel-Ø [mm] | Leistung [W] | Strom [A] | Duty Cycle | Preis [EUR] |
|--------|-------------|----------------|-------------|-----------|------------|-------------|
| BOW55-24 | 55 | 150 | 1.750 | 85 | 4 min on / 8 min off | 1.950 |
| BOW75-24 | 75 | 150 | 2.500 | 120 | 4 min on / 8 min off | 2.450 |
| BOW95-24 | 95 | 185 | 3.500 | 165 | 4 min on / 8 min off | 3.050 |
| BOW125-24 | 125 | 185 | 5.000 | 230 | 4 min on / 10 min off | 3.850 |
| BOW160-24 | 160 | 250 | 7.000 | 310 | 5 min on / 10 min off | 5.250 |
| BOW230-24 | 230 | 250 | 10.000 | 450 | 5 min on / 10 min off | 7.450 |
| BOW285-24 | 285 | 300 | 12.000 | 520 | 5 min on / 12 min off | 9.850 |
| BOW340-24 | 340 | 300 | 15.000 | 650 | 5 min on / 12 min off | 12.500 |

### 14.3 Vetus Hydraulik-Thruster

| Modell | Schub [kgf] | Tunnel-Ø [mm] | Hydraulikleistung [kW] | Preis [EUR] |
|--------|-------------|----------------|----------------------|-------------|
| BOWH095 | 95 | 185 | 4,0 | 3.500 |
| BOWH125 | 125 | 185 | 5,5 | 4.800 |
| BOWH160 | 160 | 250 | 7,0 | 6.200 |
| BOWH230 | 230 | 250 | 10,0 | 8.500 |
| BOWH340 | 340 | 300 | 15,0 | 12.800 |

### 14.4 Vetus Zubehör und Ersatzteile

| Artikel | Teilenummer | Preis [EUR] |
|---------|-------------|-------------|
| Tunnelrohr GFK 125mm (1m) | GFT125 | 180 |
| Tunnelrohr GFK 150mm (1m) | GFT150 | 210 |
| Tunnelrohr GFK 185mm (1m) | GFT185 | 280 |
| Tunnelrohr GFK 250mm (1m) | GFT250 | 380 |
| Tunnelrohr GFK 300mm (1m) | GFT300 | 480 |
| Propeller Kunststoff 125mm | SET0101 | 65 |
| Propeller Kunststoff 150mm | SET0102 | 75 |
| Propeller Kunststoff 185mm | SET0103 | 95 |
| Propeller Bronze 125mm | SET0111 | 180 |
| Propeller Bronze 150mm | SET0112 | 220 |
| Propeller Bronze 185mm | SET0113 | 280 |
| Zinkanode BOW55–125 | SET0150 | 32 |
| Zinkanode BOW160–340 | SET0151 | 48 |
| Solenoid 12V 150A | SET0012 | 85 |
| Solenoid 24V 150A | SET0024 | 90 |
| Bedienpanel Joystick | BP1024 | 145 |
| Bedienpanel Touchscreen | BPTFT | 380 |
| Gitter Edelstahl 125mm | GR125 | 55 |
| Gitter Edelstahl 150mm | GR150 | 65 |
| Gitter Edelstahl 185mm | GR185 | 80 |
| Gitter Edelstahl 250mm | GR250 | 100 |
| Gitter Edelstahl 300mm | GR300 | 125 |

### 14.5 Vetus Besonderheiten

- **V-CAN Netzwerk:** Proprietäres CAN-Bus-System für Vetus-Komponenten
- **Proportionalsteuerung:** Bei allen Modellen ab BOW55 verfügbar
- **Doppelpropeller:** Ab BOW160 als Option erhältlich
- **Thermoschutz:** Bei allen Modellen serienmäßig
- **5 Jahre Garantie:** Auf alle Thruster bei registrierter Installation
- **Weltweites Händlernetz:** Über 1.500 Händler weltweit

---

## 15. Hersteller: Side-Power / Sleipner (Norwegen)

### 15.1 Firmenporträt

Sleipner Motor AS, Hersteller der Marke Side-Power, sitzt in Fredrikstad, Norwegen. Gegründet 1903, ursprünglich Motorenbauer. Side-Power ist der Qualitätsführer im Thruster-Markt mit besonders leisem Betrieb und langer Lebensdauer. Geschätzter Marktanteil: 25% in Europa, 30% in Skandinavien.

### 15.2 SE-Serie (Elektrisch, Standard)

**12V-Modelle:**

| Modell | Schub [kgf] | Tunnel-Ø [mm] | Leistung [W] | Strom [A] | Duty Cycle | Preis [EUR] |
|--------|-------------|----------------|-------------|-----------|------------|-------------|
| SE30 | 30 | 125 | 1.000 | 95 | 3 min on / 8 min off | 1.350 |
| SE40 | 40 | 125 | 1.300 | 125 | 3 min on / 8 min off | 1.650 |
| SE60 | 60 | 150 | 2.000 | 190 | 3 min on / 10 min off | 2.150 |
| SE80 | 80 | 160 | 2.800 | 260 | 4 min on / 10 min off | 2.750 |
| SE100 | 100 | 160 | 3.500 | 340 | 4 min on / 12 min off | 3.350 |

**24V-Modelle:**

| Modell | Schub [kgf] | Tunnel-Ø [mm] | Leistung [W] | Strom [A] | Duty Cycle | Preis [EUR] |
|--------|-------------|----------------|-------------|-----------|------------|-------------|
| SE60-24 | 60 | 150 | 2.000 | 95 | 4 min on / 8 min off | 2.350 |
| SE80-24 | 80 | 160 | 2.800 | 130 | 4 min on / 10 min off | 2.950 |
| SE100-24 | 100 | 160 | 3.500 | 165 | 4 min on / 10 min off | 3.550 |

### 15.3 SP-Serie (Elektrisch, Professional)

| Modell | Schub [kgf] | Tunnel-Ø [mm] | Spannung | Leistung [W] | Strom [A] | Duty Cycle | Preis [EUR] |
|--------|-------------|----------------|----------|-------------|-----------|------------|-------------|
| SP100 | 100 | 185 | 24V | 4.000 | 185 | 5 min on / 10 min off | 4.250 |
| SP125 | 125 | 185 | 24V | 5.500 | 245 | 5 min on / 10 min off | 5.450 |
| SP155 | 155 | 250 | 24V | 7.500 | 330 | 5 min on / 10 min off | 7.250 |
| SP190 | 190 | 250 | 24V | 9.500 | 420 | 5 min on / 12 min off | 9.150 |
| SP240 | 240 | 300 | 24V | 12.000 | 520 | 5 min on / 12 min off | 11.500 |
| SP300 | 300 | 300 | 24V | 15.000 | 650 | 5 min on / 12 min off | 14.500 |

### 15.4 Side-Power Hydraulik-Thruster

| Modell | Schub [kgf] | Tunnel-Ø [mm] | Hydraulikleistung [kW] | Preis [EUR] |
|--------|-------------|----------------|----------------------|-------------|
| SH100 | 100 | 185 | 4,5 | 4.500 |
| SH160 | 160 | 250 | 7,5 | 7.500 |
| SH240 | 240 | 300 | 12,0 | 11.500 |
| SH300 | 300 | 300 | 15,0 | 14.000 |
| SH420 | 420 | 350 | 20,0 | 22.000 |

### 15.5 Side-Power Besonderheiten

- **S-Link System:** Proprietärer Digital-Bus für alle Side-Power-Komponenten
- **Dual Prop (DP):** Gegenläufige Doppelpropeller ab SP155 (20–30% mehr Schub)
- **EMMA (Electronic Marine Management Adapter):** NMEA 2000 Gateway
- **Silence Mode:** Reduzierter Schub bei leisem Betrieb (Patent)
- **IP68 Motorgehäuse:** Komplett wasserdicht, wartungsfrei
- **Norwegische Qualität:** Alle Modelle in Fredrikstad gefertigt
- **5+2 Jahre Garantie:** 5 Jahre Standard + 2 Jahre bei registrierter Wartung

---

## 16. Hersteller: Lewmar (UK)

### 16.1 Firmenporträt

Lewmar Ltd. mit Sitz in Havant, Hampshire, UK, ist primär bekannt für Winschen, Ankergeschirr und Luken. Die Thruster-Sparte bedient vor allem den britischen und nordeuropäischen Markt. Lewmar bietet ein kompaktes Sortiment mit Fokus auf Qualität und einfache Installation.

### 16.2 Tunnel-Thruster

**TT-Serie (12V):**

| Modell | Schub [kgf] | Tunnel-Ø [mm] | Leistung [W] | Strom [A] | Duty Cycle | Preis [EUR] |
|--------|-------------|----------------|-------------|-----------|------------|-------------|
| 110TT | 45 | 150 | 1.500 | 140 | 3 min on / 8 min off | 1.850 |
| 140TT | 60 | 150 | 2.000 | 190 | 3 min on / 10 min off | 2.350 |
| 185TT | 80 | 185 | 3.000 | 280 | 4 min on / 10 min off | 3.050 |
| 250TT | 120 | 250 | 5.000 | 420 | 4 min on / 12 min off | 4.750 |

**TT-Serie (24V):**

| Modell | Schub [kgf] | Tunnel-Ø [mm] | Leistung [W] | Strom [A] | Duty Cycle | Preis [EUR] |
|--------|-------------|----------------|-------------|-----------|------------|-------------|
| 140TT-24 | 60 | 150 | 2.000 | 95 | 4 min on / 10 min off | 2.550 |
| 185TT-24 | 80 | 185 | 3.000 | 140 | 4 min on / 10 min off | 3.250 |
| 250TT-24 | 120 | 250 | 5.000 | 220 | 5 min on / 10 min off | 4.950 |
| 300TT-24 | 160 | 300 | 7.500 | 330 | 5 min on / 12 min off | 6.850 |

### 16.3 Lewmar Retractable Thruster

| Modell | Schub [kgf] | Antrieb | Preis [EUR] |
|--------|-------------|---------|-------------|
| RT55 | 55 | Hydraulisch | 6.500 |
| RT80 | 80 | Hydraulisch | 9.000 |
| RT120 | 120 | Hydraulisch | 13.500 |

### 16.4 Lewmar Besonderheiten

- **Quick-Fit Tunnelrohr:** Werksseitig vorbereitete Passungen
- **Gen2 Motor:** Bürstenloser Motor bei Premium-Modellen → längere Lebensdauer
- **NMEA 2000 Anbindung:** Bei allen 24V-Modellen
- **Kompakte Bauform:** Besonders kurze Einbaulänge hinter dem Tunnelrohr
- **3 Jahre Garantie**

---

## 17. Hersteller: Max Power (Italien)

### 17.1 Firmenporträt

Max Power S.r.l. sitzt in Manerba del Garda, Italien. Seit 1992 spezialisiert auf Bugstrahlruder, besonders im preisgünstigen und mittleren Segment. Max Power ist der günstigste der Qualitätshersteller und besonders auf dem italienischen, französischen und spanischen Markt stark vertreten.

### 17.2 CT-Serie (Tunnel-Thruster)

**12V-Modelle:**

| Modell | Schub [kgf] | Tunnel-Ø [mm] | Leistung [W] | Strom [A] | Duty Cycle | Preis [EUR] |
|--------|-------------|----------------|-------------|-----------|------------|-------------|
| CT25 | 25 | 110 | 750 | 80 | 2 min on / 8 min off | 750 |
| CT35 | 35 | 125 | 1.000 | 105 | 2 min on / 8 min off | 950 |
| CT45 | 45 | 125 | 1.500 | 145 | 3 min on / 8 min off | 1.200 |
| CT60 | 60 | 160 | 2.000 | 190 | 3 min on / 10 min off | 1.550 |
| CT80 | 80 | 160 | 2.800 | 270 | 3 min on / 10 min off | 2.050 |
| CT100 | 100 | 185 | 3.500 | 340 | 4 min on / 10 min off | 2.650 |

**24V-Modelle:**

| Modell | Schub [kgf] | Tunnel-Ø [mm] | Leistung [W] | Strom [A] | Duty Cycle | Preis [EUR] |
|--------|-------------|----------------|-------------|-----------|------------|-------------|
| CT80-24 | 80 | 160 | 2.800 | 130 | 4 min on / 10 min off | 2.250 |
| CT100-24 | 100 | 185 | 3.500 | 165 | 4 min on / 10 min off | 2.850 |
| CT125-24 | 125 | 200 | 5.000 | 225 | 5 min on / 10 min off | 3.650 |
| CT150-24 | 150 | 200 | 6.500 | 290 | 5 min on / 12 min off | 4.650 |
| CT200-24 | 200 | 250 | 9.000 | 400 | 5 min on / 12 min off | 6.850 |

### 17.3 Max Power Besonderheiten

- **Preis-Leistungs-Verhältnis:** Beste Preis-Leistung unter den Markenherstellern
- **Kompatible Tunnelrohre:** Standarddurchmesser, auch Fremdfabrikate passen
- **Einbau-Kit komplett:** Alle Modelle mit Solenoid, Kabel, Panel im Lieferumfang
- **Dualmotor-Option:** Ab CT125 mit zwei Motoren für maximalen Schub
- **Ersatzteil-Versorgung:** Gut, direkt über italienische Händler
- **2 Jahre Garantie**

---

## 18. Hersteller: Quick (Italien)

### 18.1 Firmenporträt

Quick S.p.A. mit Sitz in Ravenna, Italien, ist seit 1982 Spezialist für Ankerwinden, Thruster und Warmwasserbereiter. Quick hat sich als Premium-Alternative zu Vetus und Side-Power positioniert und ist besonders in der Superyacht-Zulieferung stark.

### 18.2 BTDC-Serie (Tunnel-Thruster, DC)

**12V-Modelle:**

| Modell | Schub [kgf] | Tunnel-Ø [mm] | Leistung [W] | Strom [A] | Duty Cycle | Preis [EUR] |
|--------|-------------|----------------|-------------|-----------|------------|-------------|
| BTDC 3512 | 35 | 125 | 1.100 | 110 | 3 min on / 8 min off | 1.250 |
| BTDC 5512 | 55 | 150 | 1.800 | 175 | 3 min on / 10 min off | 1.850 |
| BTDC 7512 | 75 | 160 | 2.500 | 240 | 4 min on / 10 min off | 2.450 |
| BTDC 9512 | 95 | 185 | 3.500 | 340 | 4 min on / 10 min off | 3.050 |

**24V-Modelle:**

| Modell | Schub [kgf] | Tunnel-Ø [mm] | Leistung [W] | Strom [A] | Duty Cycle | Preis [EUR] |
|--------|-------------|----------------|-------------|-----------|------------|-------------|
| BTDC 5524 | 55 | 150 | 1.800 | 85 | 4 min on / 8 min off | 2.050 |
| BTDC 7524 | 75 | 160 | 2.500 | 120 | 4 min on / 10 min off | 2.650 |
| BTDC 9524 | 95 | 185 | 3.500 | 165 | 4 min on / 10 min off | 3.250 |
| BTDC 12524 | 125 | 200 | 5.000 | 225 | 5 min on / 10 min off | 4.250 |
| BTDC 16024 | 160 | 250 | 7.500 | 340 | 5 min on / 10 min off | 6.050 |
| BTDC 21024 | 210 | 250 | 10.000 | 450 | 5 min on / 12 min off | 8.250 |
| BTDC 28024 | 280 | 300 | 13.000 | 580 | 5 min on / 12 min off | 11.500 |

### 18.3 Quick Hydraulik-Thruster

| Modell | Schub [kgf] | Tunnel-Ø [mm] | Hydraulikleistung [kW] | Preis [EUR] |
|--------|-------------|----------------|----------------------|-------------|
| BTHQ 125 | 125 | 200 | 5,5 | 5.200 |
| BTHQ 185 | 185 | 250 | 8,5 | 8.800 |
| BTHQ 250 | 250 | 300 | 12,0 | 12.500 |
| BTHQ 340 | 340 | 300 | 16,0 | 16.500 |
| BTHQ 500 | 500 | 350 | 25,0 | 24.000 |

### 18.4 Quick TCRB-Serie (Retractable)

| Modell | Schub [kgf] | Antrieb | Preis [EUR] |
|--------|-------------|---------|-------------|
| TCRB 6024 | 60 | Elektrisch 24V | 7.500 |
| TCRB 10024 | 100 | Elektrisch 24V | 11.500 |
| TCRB 140H | 140 | Hydraulisch | 16.000 |

### 18.5 Quick Besonderheiten

- **Bürstenlose Motoren:** Alle Modelle ab BTDC 7524 mit bürstenlosem Motor → kein Kohlebürsten-Verschleiß
- **Quick Chain Counter Integration:** Thruster + Ankerwinde in einem System
- **T-Link Display:** Farbdisplay mit Duty-Cycle-Timer, Batterie-Monitoring
- **IP68 komplett:** Motor, Getriebe, Verbindungen
- **Superyacht-Zulieferer:** OEM für Azimut, Benetti, Ferretti
- **3 Jahre Garantie** (5 Jahre bei registrierter Installation)

---

## 19. Hersteller: Imtra / Anchorlift (USA)

### 19.1 Firmenporträt

Imtra Corporation mit Sitz in New Bedford, Massachusetts, USA, ist der größte Distributor von Marinausrüstung in Nordamerika. Sie vertreiben Side-Power Thruster unter eigenem Label und bieten zusätzlich Eigenmarken-Produkte. Relevant für den europäischen Markt primär als Referenz für US-Spezifikationen.

### 19.2 Produktlinie

Imtra vertreibt primär Side-Power-Produkte für den US-Markt:
- Alle Side-Power SE- und SP-Modelle unter Imtra-Label
- Zusätzlich: Anchorlift-Thruster (Einstiegssegment)
- ABYC-konforme Installationskits

### 19.3 Anchorlift-Serie

| Modell | Schub [lbf] / [kgf] | Tunnel-Ø [Zoll/mm] | Spannung | Preis [USD/EUR] |
|--------|---------------------|---------------------|----------|-----------------|
| AL35 | 77 / 35 | 5" / 125 | 12V | 850 / 780 |
| AL55 | 121 / 55 | 6" / 150 | 12V | 1.250 / 1.150 |
| AL75 | 165 / 75 | 7.1" / 185 | 12V | 1.750 / 1.600 |
| AL100 | 220 / 100 | 7.1" / 185 | 24V | 2.850 / 2.600 |

---

## 20. Herstellervergleich und Cross-Referenz

### 20.1 Vergleich bei 55 kgf Schub (12V)

| Kriterium | Vetus BOW55 | Side-Power SE60 | Max Power CT60 | Quick BTDC 5512 | Lewmar 140TT |
|-----------|-------------|-----------------|----------------|-----------------|--------------|
| Schub [kgf] | 55 | 60 | 60 | 55 | 60 |
| Tunnel-Ø [mm] | 150 | 150 | 160 | 150 | 150 |
| Leistung [W] | 1.750 | 2.000 | 2.000 | 1.800 | 2.000 |
| Strom [A] | 180 | 190 | 190 | 175 | 190 |
| Duty Cycle | 3/8 | 3/10 | 3/10 | 3/10 | 3/10 |
| Geräusch | Mittel | Leise–Mittel | Mittel | Mittel | Mittel |
| Thermoschutz | Ja | Ja | Ja | Ja | Ja |
| Garantie [Jahre] | 5 | 5+2 | 2 | 3 | 3 |
| Preis [EUR] | 1.750 | 2.150 | 1.550 | 1.850 | 2.350 |
| Preis-Leistung | Gut | Gut | Sehr gut | Gut | Mittel |

### 20.2 Vergleich bei 120–130 kgf Schub (24V)

| Kriterium | Vetus BOW125-24 | Side-Power SP125 | Max Power CT125-24 | Quick BTDC 12524 |
|-----------|-----------------|------------------|---------------------|-------------------|
| Schub [kgf] | 125 | 125 | 125 | 125 |
| Tunnel-Ø [mm] | 185 | 185 | 200 | 200 |
| Leistung [W] | 5.000 | 5.500 | 5.000 | 5.000 |
| Strom [A] | 230 | 245 | 225 | 225 |
| Duty Cycle | 4/10 | 5/10 | 5/10 | 5/10 |
| Bürstenlos | Nein | Nein | Nein | Ja |
| Garantie [Jahre] | 5 | 5+2 | 2 | 3–5 |
| Preis [EUR] | 3.850 | 5.450 | 3.650 | 4.250 |

### 20.3 Cross-Referenz: Tunnelrohr-Kompatibilität

| Tunnel-Ø [mm] | Vetus | Side-Power | Lewmar | Max Power | Quick |
|----------------|-------|-----------|--------|-----------|-------|
| 110 | BOW25 | — | — | CT25 | — |
| 125 | BOW35/45 | SE30/40 | — | CT35/45 | BTDC 3512 |
| 150 | BOW55/75 | SE60 | 110TT/140TT | — | BTDC 5512 |
| 160 | — | SE80/100 | — | CT60/80 | BTDC 7512 |
| 185 | BOW95/125 | SP100/125 | 185TT | CT100 | BTDC 9524 |
| 200 | — | — | — | CT125/150 | BTDC 12524 |
| 250 | BOW160/230 | SP155/190 | 250TT | CT200 | BTDC 16024/21024 |
| 300 | BOW285/340 | SP240/300 | 300TT | — | BTDC 28024 |

### 20.4 Bootshersteller → Werkseinbau Thruster

| Bootshersteller | Typische Modelle | Werks-Thruster | Tunnel-Ø [mm] |
|-----------------|-----------------|---------------|----------------|
| Bavaria | C42, S40 | Vetus BOW55/75 | 150 |
| Hanse | 388, 458 | Side-Power SE60/SE80 | 150/160 |
| Jeanneau | Sun Odyssey 410/440 | Side-Power SE60/SE80 | 150/160 |
| Beneteau | Oceanis 40/46 | Quick BTDC 5512/7512 | 150/160 |
| Hallberg-Rassy | 44/50 | Side-Power SP100/SP125 | 185 |
| Oyster | 565/675 | Side-Power SP155/SP190 | 250 |
| Swan | 48/54 | Side-Power SP100 | 185 |
| Azimut | 50/60 | Quick BTDC 12524/16024 | 200/250 |
| Princess | 55/62 | Side-Power SP155/SP190 | 250 |
| Sunseeker | Manhattan 52/60 | Side-Power SP190/SP240 | 250/300 |
| Linssen | 40SL/45SL | Vetus BOW75/BOW95 | 150/185 |
| Nimbus | C11/T11 | Side-Power SE80 | 160 |
| Sealine | C390/C530 | Max Power CT80/CT125 | 160/200 |

---

## 21. Fehlerbild-Atlas

### Fehlerbild 1: Thruster dreht nicht / keine Reaktion

**Symptom:** Joystick oder Panel wird betätigt, kein Geräusch, keine Reaktion.

**Mögliche Ursachen:**
1. Hauptsicherung defekt → prüfen, ggf. tauschen
2. Solenoid defekt → Klicken hörbar? Nein → Solenoid prüfen
3. Bedienpanel defekt → Steuerspannung am Solenoid messen
4. Kabelbruch → Durchgangsprüfung
5. Batterie leer → Spannung messen (>11,5V bei 12V-System, >23V bei 24V)
6. Thermoschutz ausgelöst → 15 min warten, erneut versuchen
7. Masseverbindung unterbrochen → Massekabel prüfen

**Confidence:** measured (wenn elektrisch geprüft), estimated (bei visueller Beurteilung)

### Fehlerbild 2: Thruster dreht langsam / wenig Schub

**Symptom:** Motor dreht hörbar, aber deutlich langsamer als normal, geringer Schub.

**Mögliche Ursachen:**
1. Batterie schwach → Spannung unter Last messen (Einbruch >1,5V = Problem)
2. Kabelquerschnitt zu gering → Spannungsabfall am Kabel messen
3. Korrodierte Kabelschuhe → visuell prüfen, Übergangswiderstand messen
4. Solenoid-Kontakte abgebrannt → Solenoid öffnen, Kontaktflächen prüfen
5. Propeller beschädigt oder verschmutzt → Unterwasser-Inspektion
6. Bewuchs im Tunnelrohr → Reinigung
7. Motorlager verschlissen → Geräuschänderung beachten

**Confidence:** measured (Spannungsmessung), visual_medium (Unterwasser-Inspektion)

### Fehlerbild 3: Thruster brummt/klickt, dreht nicht

**Symptom:** Solenoid klickt, Motor brummt kurz, dreht aber nicht.

**Mögliche Ursachen:**
1. Propeller blockiert (Leine, Plastik, Seetang) → Inspektion
2. Motor intern verklemmt → Welle von Hand drehen
3. Spannung zu niedrig für Anlauf → Batterie laden, Kabel prüfen
4. Getriebe blockiert → mechanisch prüfen
5. Kohlebürsten abgenutzt (bei Bürstenmotor) → Bürsten prüfen/tauschen

**Confidence:** measured (mechanische Prüfung), estimated (ohne Demontage)

### Fehlerbild 4: Starkes Vibrieren beim Betrieb

**Symptom:** Deutliche Vibrationen im Vorschiff bei Thruster-Betrieb.

**Mögliche Ursachen:**
1. Propellerblatt beschädigt (abgebrochen, verbogen) → Sichtprüfung
2. Propeller unwuchtig (Bewuchs asymmetrisch) → Reinigung
3. Lagerverschleiß → Axialspiel der Welle prüfen
4. Tunnelrohr lose im Rumpf → Verbindung prüfen
5. Gitter lose → Befestigung prüfen
6. Fremdkörper im Tunnel → Inspektion
7. Kavitation (Thruster zu nah an Wasseroberfläche) → Wasserlinie prüfen

**Confidence:** visual_medium (Unterwasser), measured (nach Demontage)

### Fehlerbild 5: Wassereinbruch am Thruster

**Symptom:** Wasser dringt im Bereich des Thruster-Motors oder Tunnelrohrs ein.

**Mögliche Ursachen:**
1. Wellendichtring verschlissen → Motor-Einheit demontieren, Simmerring prüfen
2. Tunnelrohr-Laminat gerissen → Riss im GFK-Laminat suchen
3. Motor-Flansch-Dichtung defekt → O-Ring oder Dichtung tauschen
4. Kabeldurchführung undicht → Kabelverschraubung prüfen/nachziehen
5. Osmose-Schäden im Tunnelrohr-Bereich → GFK-Zustand prüfen

**Confidence:** measured (nach Trockenlegen und Inspektion)

**Dringlichkeit:** HOCH — Wassereinbruch kann zu elektrischem Kurzschluss und Motorschaden führen!

### Fehlerbild 6: Ungleicher Schub (Backbord ≠ Steuerbord)

**Symptom:** Boot bewegt sich bei gleicher Joystick-Betätigung stärker in eine Richtung.

**Mögliche Ursachen:**
1. Gitter einseitig verstopft → Reinigung
2. Propellerblatt einseitig beschädigt → Sichtprüfung
3. Tunnel-Einlauf einseitig zugewachsen → Antifouling erneuern
4. Bei Doppelpropeller: ein Propeller defekt → Prüfung
5. Solenoid für eine Richtung schwächer → Spannungsmessung
6. Rumpf-Asymmetrie (bei älteren Booten) → selten, aber möglich

**Confidence:** measured (Schubmessung), visual_medium (Unterwasser-Inspektion)

### Fehlerbild 7: Übermäßiger Anodenverbrauch

**Symptom:** Anoden am Thruster sind nach wenigen Monaten aufgelöst.

**Mögliche Ursachen:**
1. Streustrom vom Thruster-Schaltkreis → Strommessung Rumpf-Wasser
2. Falsche Anoden-Legierung (z.B. Zink in Süßwasser) → Material prüfen
3. Galvanische Kopplung mit Marina-Nachbar → Trenntrafo oder galvanischer Isolator
4. Erdung über Landstromkabel → Isolationsprüfung
5. Defekte Kabelisolierung am Thruster → visuell prüfen

**Confidence:** measured (Strommessung), documented (Logbuch-Anoden-Verbrauch)

### Fehlerbild 8: Motor überhitzt / Thermoschutz löst häufig aus

**Symptom:** Thruster schaltet nach kurzer Betriebszeit ab, Thermoschutz-LED leuchtet.

**Mögliche Ursachen:**
1. Duty Cycle überschritten → Betriebsprotokoll prüfen
2. Thruster unterdimensioniert → Bootstyp und Schubkraft vergleichen
3. Belüftung im Motor-Bereich unzureichend → Luftzirkulation verbessern
4. Motor intern beschädigt (Wicklungsschluss) → Motor prüfen lassen
5. Spannung zu niedrig → Motor arbeitet mit höherem Strom → mehr Wärme
6. Umgebungstemperatur zu hoch (Maschinenraum >50°C) → Isolation/Belüftung

**Confidence:** measured (Temperaturmessung, Strommessung)

### Fehlerbild 9: Lautes Geräusch / Kreischen beim Betrieb

**Symptom:** Ungewöhnlich lautes, metallisches Geräusch beim Betrieb.

**Mögliche Ursachen:**
1. Kavitation → Thruster zu nah an Wasseroberfläche oder zu hohe Drehzahl
2. Lagerschaden → Drehgeräusch auch ohne Last
3. Getriebeschaden → metallisches Schleifen
4. Propeller streift am Tunnelrohr → Spalt prüfen
5. Fremdkörper im Tunnel → Inspektion
6. Gitter vibriert → Befestigung prüfen

**Confidence:** visual_medium (Geräuschanalyse), measured (nach Demontage)

### Fehlerbild 10: Korrosion am Tunnelrohr (Aluminium)

**Symptom:** Weiße, pulvrige Ablagerungen am Aluminium-Tunnelrohr, Materialverlust.

**Mögliche Ursachen:**
1. Fehlende oder verbrauchte Anoden → sofort erneuern
2. Galvanische Korrosion durch Bronze-Propeller → Kunststoff-Propeller verwenden
3. Streustrom-Korrosion → Strommessung, Erdung prüfen
4. Antifouling-Unverträglichkeit → nur Alu-kompatibles Antifouling verwenden
5. Spaltkorrosion an Schraubverbindungen → Isolation/Dichtmasse verwenden

**Confidence:** visual_high (sichtbar), measured (Materialstärke-Messung)

**Dringlichkeit:** HOCH — unbehandelte Korrosion kann zur Rumpfdurchbohrung führen!

### Fehlerbild 11: Sicherung brennt regelmäßig durch

**Symptom:** Hauptsicherung des Thrusters brennt bei Betrieb wiederholt durch.

**Mögliche Ursachen:**
1. Kurzschluss im Motor → Isolationswiderstand messen
2. Propeller blockiert → mechanische Prüfung
3. Sicherung unterdimensioniert → richtige Sicherungsgröße prüfen
4. Solenoid-Kontakte verschweißt → Solenoid prüfen
5. Kabelschaden (Isolation durchgescheuert) → Kabelweg visuell prüfen
6. Anlaufstrom zu hoch (kalter Motor) → höhere Sicherung oder Softstart

**Confidence:** measured (elektrische Messung)

### Fehlerbild 12: Thruster läuft nach Loslassen des Joysticks weiter

**Symptom:** Thruster schaltet nicht ab, wenn Joystick losgelassen wird.

**Mögliche Ursachen:**
1. Solenoid-Kontakte verschweißt → Sofort Hauptsicherung ziehen!
2. Steuerrelais klebt → Relais prüfen/tauschen
3. Joystick-Rückstellung defekt → Joystick-Mechanik prüfen
4. Elektronik-Platine defekt → Controller-Board prüfen
5. Wasser im Bedienpanel → Panel öffnen, trocknen

**Dringlichkeit:** KRITISCH — Sicherheitsrisiko! Sofort Batterie trennen!

**Confidence:** measured (elektrische Prüfung)

---

## 22. Troubleshooting-Entscheidungsbaum

### Troubleshooting 1: Kein Betrieb

```
Thruster reagiert nicht
├── Batteriespannung OK (>11,5V/23V)?
│   ├── Nein → Batterie laden/prüfen
│   └── Ja → Weiter
│       ├── Sicherung OK?
│       │   ├── Nein → Sicherung tauschen → löst wieder aus?
│       │   │   ├── Ja → Kurzschluss suchen (Motor, Kabel)
│       │   │   └── Nein → Fertig
│       │   └── Ja → Weiter
│       │       ├── Solenoid klickt?
│       │       │   ├── Nein → Steuerspannung am Solenoid? (12/24V)
│       │       │   │   ├── Nein → Bedienpanel oder Steuerkabel defekt
│       │       │   │   └── Ja → Solenoid-Spule defekt → tauschen
│       │       │   └── Ja → Weiter
│       │       │       ├── Spannung am Motor? (messen mit Solenoid aktiv)
│       │       │       │   ├── Nein → Solenoid-Kontakte defekt → tauschen
│       │       │       │   └── Ja → Motor defekt → Motor prüfen/tauschen
```

### Troubleshooting 2: Geringer Schub

```
Schub deutlich reduziert
├── Spannung unter Last messen (am Motor)
│   ├── <10,5V (12V) / <21V (24V) → Batterie/Kabel-Problem
│   │   ├── Batterie voll geladen?
│   │   │   ├── Nein → Laden → erneut prüfen
│   │   │   └── Ja → Kabelquerschnitt/Länge prüfen
│   │   │       └── Spannungsabfall >1,5V → Kabel erneuern/kürzen
│   └── >10,5V/21V → Mechanisches Problem
│       ├── Propeller beschädigt? → Sichtprüfung
│       ├── Bewuchs im Tunnel? → Reinigung
│       ├── Gitter verstopft? → Reinigung
│       └── Motor-Leistung vermindert? → Kohlebürsten, Lager prüfen
```

### Troubleshooting 3: Überhitzung

```
Thruster schaltet wegen Überhitzung ab
├── Duty Cycle eingehalten?
│   ├── Nein → Betriebsverhalten anpassen
│   └── Ja → Weiter
│       ├── Belüftung im Motorraum ausreichend?
│       │   ├── Nein → Belüftung verbessern
│       │   └── Ja → Weiter
│       │       ├── Batteriespannung unter Last OK?
│       │       │   ├── Nein → Motor kompensiert mit mehr Strom → Batterie/Kabel
│       │       │   └── Ja → Motor intern → Wicklungswiderstand messen
│       │       │       ├── Zu niedrig → Wicklungsschluss → Motor tauschen
│       │       │       └── OK → Lagerverschleiß → Lager tauschen
```

### Troubleshooting 4: Wassereinbruch

```
Wasser im Thruster-Bereich
├── Woher kommt das Wasser?
│   ├── Motor-Flansch → O-Ring/Dichtung tauschen
│   ├── Tunnelrohr-Rumpf-Übergang → Laminat prüfen/erneuern
│   ├── Kabeldurchführung → Verschraubung nachziehen/erneuern
│   └── Wellendichtung → Simmerring tauschen
├── Sofortige Maßnahme: Motor-Einheit demontieren, trocknen
├── Elektrische Prüfung vor Wiederinbetriebnahme!
└── Langfristig: Ursache beseitigen, Korrosion behandeln
```

### Troubleshooting 5: Korrosion

```
Korrosion an Thruster-Komponenten
├── Wo tritt Korrosion auf?
│   ├── Tunnelrohr (Alu) → Anoden prüfen, galvanische Trennung prüfen
│   ├── Propellerwelle → Material prüfen, Anoden
│   ├── Motorgehäuse → Anodenschutz, Beschichtung
│   └── Kabelschuhe → Isolierung, Kontaktfett
├── Streustrom vorhanden?
│   ├── Messen: Rumpf-Wasser >30mA → Streustrom!
│   │   ├── Landstrom-Erdung prüfen
│   │   ├── Alle Verbraucher nacheinander abschalten → Quelle finden
│   │   └── Galvanischen Isolator installieren
│   └── <30mA → galvanische Korrosion
│       ├── Anoden erneuern
│       ├── Materialkombination prüfen (Bronze ↔ Alu vermeiden)
│       └── Antifouling-Verträglichkeit prüfen
```

---

## 23. Wartung und Inspektion

### 23.1 Jährliche Wartung (beim Antifouling / Slipanlage)

| Aufgabe | Dauer | Werkzeug | Kosten (Material) |
|---------|-------|----------|-------------------|
| Propeller abziehen, Zustand prüfen | 15 min | Abzieher, Schlüssel | 0 EUR |
| Anoden prüfen, ggf. tauschen | 10 min | Schlüssel | 25–65 EUR |
| Tunnelrohr reinigen (Bewuchs, Muscheln) | 20 min | Schaber, Bürste | 0 EUR |
| Gitter reinigen, Befestigung prüfen | 10 min | Bürste, Schlüssel | 0 EUR |
| Antifouling auf Tunnelrohr erneuern | 30 min | Pinsel, Antifouling | 15–30 EUR |
| Wellendichtung prüfen (Sichtprüfung) | 5 min | — | 0 EUR |
| Motor-Flansch-Befestigung prüfen | 5 min | Drehmomentschlüssel | 0 EUR |
| Gesamtzeit Routine-Wartung | 1,5–2 h | | 40–95 EUR |

### 23.2 Alle 3–5 Jahre (erweiterte Wartung)

| Aufgabe | Dauer | Kosten (Material + Arbeit) |
|---------|-------|---------------------------|
| Wellendichtring (Simmerring) tauschen | 1 h | 30–80 EUR + Arbeit |
| Lagersatz tauschen | 2 h | 50–150 EUR + Arbeit |
| Kohlebürsten tauschen (Bürstenmotor) | 0,5 h | 20–60 EUR |
| Solenoid-Kontakte prüfen/tauschen | 0,5 h | 80–150 EUR |
| Kabelschuhe prüfen, ggf. erneuern | 1 h | 20–50 EUR |
| Propeller tauschen (Kunststoff) | 15 min | 65–120 EUR |

### 23.3 Wartungsplan nach Betriebsstunden

| Betriebsstunden | Maßnahme |
|-----------------|----------|
| 50 h | Erste Inspektion: Schrauben nachziehen, Geräusche beobachten |
| 100 h | Kohlebürsten prüfen (Bürstenmotor) |
| 200 h | Lagerspiel prüfen, Wellendichtung prüfen |
| 300 h | Kohlebürsten tauschen, Lager bewerten |
| 500 h | Wellendichtring tauschen, Lagersatz tauschen |
| 1.000 h | Grundüberholung: Motor komplett, alle Dichtungen und Lager |

### 23.4 Winterlagerung

**Bei Boot an Land:**
- Propeller abziehen, reinigen, fetten, separat lagern
- Tunnelrohr reinigen und trocknen
- Anoden prüfen (Zustand dokumentieren)
- Motor-Anschlüsse mit Kontaktspray behandeln
- Batterie abklemmen und warm lagern (Lithium: >5°C, AGM: >0°C)
- Bedienpanel trocken lagern oder Feuchtigkeitsbeutel im Panel-Bereich

**Bei Boot im Wasser (Winterlieger):**
- Thruster regelmäßig kurz betätigen (alle 2 Wochen, 30 Sekunden) → verhindert Festsetzen
- Batterie-Ladeerhaltung sicherstellen
- Anoden kontrollieren (im Wasser verbrauchen sie sich weiter)

---

## 24. FAQ — Häufige Fragen

### FAQ 1: Brauche ich wirklich einen Bugstrahlruder?

**Antwort:** Ab 10m Bootslänge und regelmäßigem Anlegen in Marinas mit engem Platzangebot oder bei häufigen Seitenwind-Bedingungen: ja, dringend empfohlen. Einhand-Segler profitieren besonders. Unter 8m und bei erfahrenen Crews in ruhigen Revieren: nicht zwingend, aber komfortabel. Die Investition von 1.500–3.000 EUR (inkl. Einbau) rechnet sich durch vermiedene Rammschäden nach dem ersten verhinderten Anlegeunfall.

### FAQ 2: Reicht ein Bugstrahlruder oder brauche ich auch ein Heckstrahlruder?

**Antwort:** Für die meisten Boote bis 14m reicht ein Bugstrahlruder aus, wenn der Skipper die Technik des Anlegens beherrscht (Hauptantrieb für Heck-Korrektur nutzen). Ab 16m Motoryacht mit Flybridge oder bei reinem Seitwärts-Anlegen ist ein Heckstrahlruder sinnvoll. Für Katamarane ab 14m ebenfalls empfohlen.

### FAQ 3: Kann ich einen Bugstrahlruder nachrüsten?

**Antwort:** Ja, bei GFK-Rümpfen ist die Nachrüstung gut möglich, aber aufwendig. Das Boot muss geslippt werden, der Rumpf wird durchbohrt (Tunnelrohr), und es müssen dicke Stromkabel verlegt werden. Kosten: 3.000–8.000 EUR gesamt (Material + Arbeit). Alternativ: externe Thruster (Vetus BOW PRO) ohne Rumpfdurchbruch für 1.500–3.000 EUR. Bei Aluminium-Rümpfen: Schweißarbeiten nötig, Werft empfohlen.

### FAQ 4: 12V oder 24V — was ist besser?

**Antwort:** Unter 55 kgf Schub ist 12V ausreichend und einfacher (vorhandenes Bordnetz). Ab 55 kgf Schub empfehlen wir 24V: dünnere Kabel, weniger Spannungsabfall, mehr Reserve. Boote mit vorhandenem 24V-Bordnetz (viele Motoryachten, größere Segelyachten): immer 24V. Die Mehrkosten für die 24V-Version betragen ca. 200–400 EUR — fast immer sinnvoll investiert.

### FAQ 5: Wie lange kann ich den Thruster am Stück betreiben?

**Antwort:** Abhängig vom Modell und Hersteller. Typisch: 2–5 Minuten, dann 8–15 Minuten Pause (Duty Cycle). In der Praxis reichen 30–90 Sekunden für ein Anlegemanöver. Wer regelmäßig an den Duty Cycle stößt, hat entweder einen unterdimensionierten Thruster oder muss seine Manövertechnik verbessern. Hydraulische Thruster haben keine Einschaltdauer-Begrenzung.

### FAQ 6: Welcher Hersteller ist der beste?

**Antwort:** Es gibt keinen „besten" Hersteller — es kommt auf die Anforderungen an:
- **Bestes Preis-Leistungs-Verhältnis:** Max Power (Italien)
- **Breitestes Sortiment:** Vetus (Niederlande)
- **Leisester Betrieb:** Side-Power (Norwegen)
- **Längste Garantie:** Side-Power (5+2 Jahre)
- **Bester Superyacht-Zulieferer:** Quick (Italien)
- **Beste Nachrüstlösung:** Vetus BOW PRO (extern, kein Rumpfdurchbruch)
- **Bester Ersatzteil-Service in Deutschland:** Vetus (Vertrieb über SVB, Bukh)

### FAQ 7: Kann ich den Thruster während der Fahrt benutzen?

**Antwort:** Technisch ja, aber er ist bei Geschwindigkeiten über 3–5 Knoten wirkungslos. Die Querströmung am Rumpf überdeckt den Thruster-Strahl. Außerdem erzeugt das offene Tunnelrohr bei Fahrt Widerstand und Strömungsgeräusche. Manche Thruster haben eine automatische Abschaltung bei Fahrtgeschwindigkeit (Geschwindigkeitssensor via NMEA 2000).

### FAQ 8: Wie laut ist ein Bugstrahlruder?

**Antwort:** Lautstärke variiert stark nach Hersteller und Typ:
- Tunnel-Thruster, elektrisch: 65–80 dB(A) im Vorschiff
- Tunnel-Thruster, hydraulisch: 55–70 dB(A) im Vorschiff
- Retractable: 50–65 dB(A)
- External: 60–75 dB(A)
Der Lärm wird von den Nachbarn in der Marina wahrgenommen — ein häufiger Beschwerdegrund. Leise Modelle (Side-Power mit Silence Mode) und hydraulische Systeme sind deutlich angenehmer.

### FAQ 9: Brauche ich eine separate Batterie für den Thruster?

**Antwort:** Dringend empfohlen. Ein Thruster zieht 80–500A — das belastet jede Batterie enorm. Ohne separate Thruster-Batterie riskieren Sie:
- Tiefentladung der Servicebatterie → kein Licht, kein Funk
- Spannungseinbruch → Elektronik-Störungen (Kartenplotter, Autopilot)
- Verkürzte Batterie-Lebensdauer
Eine dedizierte 100–200Ah AGM-Batterie kostet 200–400 EUR und wird über Trennrelais von der Lichtmaschine geladen.

### FAQ 10: Was kostet eine komplette Thruster-Installation?

**Antwort:** Richtwerte für Komplett-Installation (Material + Arbeit):

| Boot/Typ | Thruster | Einbau | Elektrik | Gesamt |
|----------|---------|--------|---------|--------|
| Segelyacht 10m, 12V 45kgf | 1.200 EUR | 1.500 EUR | 500 EUR | 3.200 EUR |
| Segelyacht 13m, 24V 80kgf | 2.500 EUR | 2.000 EUR | 800 EUR | 5.300 EUR |
| Motoryacht 12m, 12V 75kgf | 2.300 EUR | 1.800 EUR | 700 EUR | 4.800 EUR |
| Motoryacht 16m, 24V 125kgf | 4.000 EUR | 2.500 EUR | 1.200 EUR | 7.700 EUR |
| Motoryacht 20m, 24V + HSR | 12.000 EUR | 4.000 EUR | 2.500 EUR | 18.500 EUR |

### FAQ 11: Kann ich den Thruster selbst einbauen?

**Antwort:** Der Tunnelrohr-Einbau (Rumpfdurchbruch) sollte von einer Fachwerft durchgeführt werden — ein fehlerhafter Einbau kann zu Wassereinbruch und Strukturschwäche führen. Die elektrische Installation kann ein versierter Eigner selbst machen, wenn er Erfahrung mit Hochstrom-Verkabelung hat. Die Kabel richtig zu crimpen und zu dimensionieren ist kritisch. Externe Thruster (BOW PRO) können von handwerklich geschickten Eignern selbst montiert werden.

### FAQ 12: Wie finde ich den richtigen Thruster für mein Boot?

**Antwort:** Drei Schritte:
1. Bootslänge und -typ → Tabelle Abschnitt 9.2 → empfohlene Schubkraft
2. Vorhandener Platz im Bug → Tunnel-Ø bestimmen
3. Bordnetz → 12V oder 24V
4. Budget und Hersteller-Präferenz → Vergleichstabelle Abschnitt 20

### FAQ 13: Mein Thruster ist 15 Jahre alt — muss er getauscht werden?

**Antwort:** Nicht unbedingt. Wenn der Thruster noch einwandfrei funktioniert, guten Schub liefert und keine Korrosion zeigt, kann er weiter betrieben werden. Wichtig: alle 3–5 Jahre Simmerring und Lager erneuern, Anoden jährlich prüfen. Ersatzteile für Modelle >15 Jahre können allerdings schwer erhältlich sein. In dem Fall lohnt sich die Grundüberholung durch den Hersteller oder der Austausch.

### FAQ 14: Was bedeutet „kgf" und wie rechne ich in „lbf" um?

**Antwort:**
- kgf (Kilogramm-Force) ist die in Europa übliche Einheit für Thruster-Schub
- lbf (Pound-Force) ist die in den USA und UK übliche Einheit
- Umrechnung: 1 kgf = 2,205 lbf | 1 lbf = 0,4536 kgf
- Beispiel: 55 kgf = 121 lbf
- In Newton: 1 kgf = 9,81 N | 55 kgf = 539 N

### FAQ 15: Kann ich einen Thruster eines Herstellers mit dem Tunnelrohr eines anderen verwenden?

**Antwort:** Grundsätzlich ja, wenn der Tunnel-Durchmesser stimmt. Die Tunnelrohr-Durchmesser sind weitgehend standardisiert (125, 150, 160, 185, 200, 250, 300mm). Allerdings können herstellerspezifische Befestigungen abweichen. Immer prüfen: Propeller-Durchmesser muss zum Tunnel-Innendurchmesser passen (Propeller ca. 5mm kleiner als Tunnel-Innen-Ø).

### FAQ 16: Welches Antifouling gehört auf das Tunnelrohr?

**Antwort:** Dasselbe Antifouling wie auf dem Rumpf — aber Vorsicht bei Aluminium-Tunnelrohren: nur kupferfreies Antifouling verwenden (z.B. International Trilux 33, Hempel Mille Light Copper Free). Kupferhaltiges Antifouling auf Aluminium erzeugt galvanische Korrosion. Propeller: Spezial-Propellerantifouling (z.B. Propspeed) oder kein Antifouling (Propeller reinigt sich durch Rotation).

### FAQ 17: Mein Thruster funktioniert nur in eine Richtung — was tun?

**Antwort:** Häufige Ursache: eines der beiden Solenoids ist defekt (ein Solenoid für jede Drehrichtung). Prüfung: Steuerspannung am defekten Solenoid messen — wenn vorhanden, Solenoid tauschen. Wenn keine Steuerspannung, dann Bedienpanel oder Steuerkabel prüfen. Bei Proportionalsteuerung: Controller-Board kann einseitig defekt sein.

### FAQ 18: Wie verhindere ich Bewuchs im Tunnelrohr?

**Antwort:**
1. Antifouling im und am Tunnelrohr (jährlich erneuern)
2. Regelmäßiger kurzer Betrieb (alle 1–2 Wochen, 30 Sekunden) → hält Bewuchs in Bewegung
3. Gitter regelmäßig reinigen (Taucher oder beim Antifouling)
4. In tropischen Gewässern: monatliche Unterwasser-Reinigung empfohlen

### FAQ 19: Kann ich einen gebrauchten Thruster kaufen?

**Antwort:** Ja, gebrauchte Thruster sind über Bootsbörsen und Marinas erhältlich. Worauf achten:
- Motor-Zustand (Wicklungswiderstand messen)
- Lagerspiel (Propellerwelle seitlich bewegen — kein Spiel erlaubt)
- Kohlebürsten-Länge (Bürstenmotor)
- Korrosion am Gehäuse und Welle
- Propeller-Zustand
- Verfügbarkeit von Ersatzteilen (Modell noch lieferbar?)
- Preis: 40–60% des Neupreises ist fair, wenn Zustand gut

### FAQ 20: Mein Boot hat einen Saildrive — geht trotzdem ein Bugstrahlruder?

**Antwort:** Ja, ein Bugstrahlruder ist unabhängig vom Hauptantrieb. Der Saildrive sitzt achtern, der Bugstrahlruder im Vorschiff. Kein Konflikt. Bei der Dimensionierung den Schub des Saildrives (leichte Querschubwirkung beim Manövrieren) nicht als Ersatz für den Bugstrahlruder rechnen.

### FAQ 21: Wie stark ist der Schubverlust durch die Gitter?

**Antwort:** Typisch 5–10% Schubverlust durch Standard-Gitter (beidseitig). Strömungsoptimierte Gitter (Side-Power, Vetus Premium): nur 3–5%. Ohne Gitter: kein Verlust, aber Risiko von Leinenwicklern und Fremdkörper-Blockade. Empfehlung: Gitter immer montieren — der 5% Schubverlust ist geringer als ein blockierter Propeller.

### FAQ 22: Lithium-Batterie für den Thruster — lohnt sich das?

**Antwort:** Ja, besonders bei häufiger Thruster-Nutzung (Charter, Marina-Hopping). Vorteile:
- Konstante Spannung bis 90% Entladung → gleichbleibender Schub
- 50% leichter als AGM bei gleicher nutzbarer Kapazität
- 3.000–5.000 Zyklen statt 500–800 (AGM)
- Schnellladefähig
Nachteile: 2,5–3× teurer, BMS (Batteriemanagementsystem) nötig, nicht alle Ladegeräte kompatibel. Ab ca. 300 Nutzungszyklen amortisiert sich Lithium über die Lebensdauer.

### FAQ 23: Kann ich den Thruster als Antrieb nutzen (z.B. zum Verholen)?

**Antwort:** Technisch möglich, aber nicht empfohlen. Bugstrahlruder erzeugen Querschub — zum Geradeaus-Fahren müsste man ständig gegensteuern. Die Geschwindigkeit wäre minimal (<1 kn). Außerdem ist der Duty Cycle schnell überschritten. Für Notsituationen (Motorausfall in der Marina): kurzfristig zum Abdrehen/Verholen nutzbar.

### FAQ 24: Mein Thruster macht immer kurz beim Einschalten ein klackendes Geräusch — normal?

**Antwort:** Ja, das Klacken kommt vom Solenoid (Leistungsrelais), das den hohen Motorstrom schaltet. Es ist bei allen elektrischen Thrustern normal und kein Defekt. Wenn das Klacken sehr laut wird, regelmäßig wiederholt oder mit Funken begleitet ist, dann Solenoid-Kontakte prüfen (Abbrand).

### FAQ 25: Welche Mindest-Kabelstärke brauche ich für meinen Thruster?

**Antwort:** Siehe Abschnitt 11.1 für detaillierte Tabellen. Faustregel: Bei 12V-Systemen mindestens 50mm² für mittlere Thruster (45–75 kgf) und mindestens 70mm² für große (75–100 kgf). Bei 24V: jeweils eine Stufe kleiner. Immer den kürzestmöglichen Kabelweg planen — jeder eingesparte Meter reduziert Spannungsverluste.

---

## 25. Glossar

| Begriff | Erklärung |
|---------|-----------|
| ABYC | American Boat and Yacht Council — US-Normenorganisation für Bootstechnik |
| AGM | Absorbent Glass Mat — Batterietechnologie mit Glasfaservlies |
| Ampere (A) | Einheit der elektrischen Stromstärke |
| Ankerbox | Stauraum im Bug für Anker und Kette, oft in der Nähe des Thrusters |
| ANL-Sicherung | Hochstrom-Schmelzsicherung für marine Anwendungen (50–500A) |
| Antifouling | Bewuchsschutzbeschichtung am Unterwasserschiff |
| Azipod | Schwenkbarer elektrischer Gondel-Antrieb (Schifffahrt) |
| Backbord | Linke Schiffsseite (in Fahrtrichtung gesehen) |
| Bilge | Tiefster Punkt im Bootsinneren, wo sich Wasser sammelt |
| Bordnetz | Elektrisches Versorgungsnetz an Bord |
| BSR | Bugstrahlruder |
| Bug | Vorderer Teil des Bootes |
| Bürstenmotor | DC-Motor mit Kohlebürsten für Stromübertragung zum Rotor |
| Bürstenloser Motor | DC-Motor ohne Kohlebürsten (BLDC), elektronisch kommutiert |
| CAN-Bus | Controller Area Network — digitaler Kommunikationsbus |
| CE-Kennzeichnung | Europäische Konformitätskennzeichnung für Sportboote |
| Class-T-Sicherung | Schnelle Hochstrom-Sicherung für empfindliche Elektronik |
| Crabbing | Seitwärtsfahrt eines Bootes (BSR + HSR gleichzeitig) |
| DC | Direct Current — Gleichstrom |
| Deadspace | Nicht nutzbarer Raum im Boot (z.B. zwischen Tunnel und Rumpf) |
| Duty Cycle | Einschaltdauer — Verhältnis von Betriebszeit zu Gesamtzeit |
| EMV | Elektromagnetische Verträglichkeit |
| Flybridge | Erhöhte, offene Steuerposition auf Motoryachten |
| Galvanische Korrosion | Elektrochemische Korrosion durch Kontakt verschiedener Metalle |
| GFK | Glasfaserverstärkter Kunststoff (FRP auf Englisch) |
| GPS-Ankerung | Automatische Positionshaltung via Satellitennavigation |
| Heck | Hinterer Teil des Bootes |
| HSR | Heckstrahlruder |
| IP68 | Schutzart: staubdicht und wasserdicht bei dauerhaftem Untertauchen |
| ISO | International Organization for Standardization |
| Joystick | Steuerknüppel für proportionale Thruster-Steuerung |
| Kavitation | Hohlraumbildung im Wasser bei Unterdruck (Propeller, Pumpen) |
| kgf | Kilogramm-Force — Krafteinheit (1 kgf ≈ 9,81 N) |
| Knoten (kn) | Seemeilen pro Stunde (1 kn = 1,852 km/h) |
| Kohlebürsten | Verschleißteile im Bürstenmotor für Stromübertragung |
| Landstrom | 230V-Stromversorgung vom Hafen an Bord |
| Lateralfläche | Seitliche Projektionsfläche des Bootes (über oder unter Wasser) |
| lbf | Pound-Force — Krafteinheit im angloamerikanischen System |
| Lichtmaschine | Generator am Motor zur Erzeugung von Ladestrom |
| LiFePO4 | Lithium-Eisenphosphat — sichere Lithium-Batterietechnologie |
| LWL | Länge Wasserlinie — Länge des Bootes an der Wasseroberfläche |
| Manganbronze | Kupfer-Legierung mit Mangan, Zink — typisches Propeller-Material |
| Marina | Yachthafen |
| Masseverbindung | Elektrischer Rückleiter (Minus-Pol) |
| Mega-Fuse | Hochstrom-Schmelzsicherung (100–500A) |
| NAB | Nickel-Aluminium-Bronze — korrosionsbeständige Propeller-Legierung |
| NMEA 2000 | Digitaler Kommunikationsstandard für marine Elektronik |
| Opferanode | Unedles Metall, das sich anstelle des geschützten Metalls auflöst |
| Osmose | Feuchtigkeitsaufnahme in GFK-Laminat (Blistering) |
| PTO | Power Take-Off — Kraftabnahme vom Motor (für Hydraulikpumpe) |
| Propeller | Schiffsschraube — erzeugt Schubkraft |
| Proportionalsteuerung | Stufenlose Schubkraft-Regelung |
| Simmerring | Radialwellendichtring |
| Solenoid | Magnetisch betätigtes Hochstrom-Relais |
| Steuerbord | Rechte Schiffsseite (in Fahrtrichtung gesehen) |
| Streustrom | Unbeabsichtigter elektrischer Strom durch Wasser oder Rumpf |
| Thermoschutz | Temperaturbegrenzer zum Schutz des Motors vor Überhitzung |
| Thruster | Englisch für Strahlruder (Bug- oder Heckstrahlruder) |
| Transom | Heckspiegel — flache Heckwand eines Bootes |
| Trennrelais | Automatisches Relais zur Batterietrennung/-verbindung |
| Tunnelrohr | Zylindrisches Rohr quer durch den Rumpf für den Thruster |
| Verdrängung | Wasserverdrängung des Bootes = Bootsgewicht |
| VSR | Voltage Sensitive Relay — spannungsgesteuertes Trennrelais |
| Wellendichtung | Dichtung zwischen rotierender Welle und Gehäuse |
| Winde | Mechanische Vorrichtung zum Ziehen von Leinen oder Ketten |

---

## 26. Fallstudien

### Fallstudie 1: Bavaria C42 — Bugstrahlruder-Nachrüstung

**Ausgangssituation:**
- Boot: Bavaria C42, Baujahr 2019, GFK-Rumpf
- Eigner: Einhandsegler, 62 Jahre, Heimathafen Kornaten (Kroatien)
- Problem: Anlegen in kroatischen Marinas bei Bora (NE-Wind) extrem schwierig
- Budget: 4.000 EUR

**Analyse:**
- Bootslänge: 12,80m, Verdrängung: 9.500 kg
- Empfohlener Schub: 70–90 kgf (Segelyacht, Mittelwert)
- Bordnetz: 12V, 2× 110Ah AGM Servicebatterien
- Bug-Bereich: ausreichend Platz für 150mm Tunnel
- Kabellänge Batterie → Bug: ca. 8m

**Lösung:**
- Thruster: Vetus BOW75 (75 kgf, 12V, 150mm Tunnel)
- Tunnelrohr: Vetus GFT150 (GFK, 150mm × 700mm)
- Batterie: 1× Victron AGM 170Ah als dedizierte Thruster-Batterie
- Trennrelais: Cyrix-ct 12/24-120
- Kabel: 2× 95mm² (Rot + Schwarz), 8m, mit hydraulisch verpressten Kabelschuhen
- Sicherung: Blue Sea ANL 400A

**Einbau:**
- Werft: Brodogradilište, Biograd na Moru
- Rumpfdurchbruch und Tunnelrohr-Einlaminierung: 8 Stunden
- Elektrik: 4 Stunden (eigener Elektriker)
- Gesamtkosten: 3.650 EUR (Material: 2.850 EUR, Arbeit: 800 EUR)

**Ergebnis:**
- Eigner sehr zufrieden: „Endlich stressfrei Anlegen bei Bora"
- Duty Cycle nie erreicht (typisches Manöver: 45 Sekunden)
- Anoden-Verbrauch normal (Wechsel nach 14 Monaten)
- AYDI-Bewertung: 82/100 (Abzug für 12V statt 24V bei dieser Schubklasse)

**Confidence:** measured (Installation dokumentiert), documented (Eigner-Feedback)

### Fallstudie 2: Princess 55 — BSR + HSR Komplettanlage

**Ausgangssituation:**
- Boot: Princess 55, Baujahr 2017, GFK
- Nutzung: Charter-Betrieb, Côte d'Azur
- Problem: Chartercrews scheitern regelmäßig beim Anlegen in engen Häfen (Port Grimaud, Cannes)
- Anforderung: Einfachstes Manövrieren für unerfahrene Crews

**Analyse:**
- Bootslänge: 17,40m, Verdrängung: 28.000 kg
- Flybridge → Windangriffsfläche ca. 42 m²
- Empfohlener Schub BSR: 185+ kgf, HSR: 240+ kgf
- Bordnetz: 24V
- Vorhandener BSR: Side-Power SP155 (155 kgf) → unterdimensioniert

**Lösung:**
- BSR-Upgrade: Side-Power SP240 (240 kgf, 24V, 300mm Tunnel)
- HSR-Neueinbau: Side-Power SP300 (300 kgf, 24V, 300mm Tunnel)
- Steuerung: Side-Power Joystick-Panel mit proportionaler Steuerung
- Batterien: 2× Victron Lithium LiFePO4 200Ah (24V, je für BSR/HSR)
- NMEA 2000 Integration mit vorhandenem Garmin-System

**Einbau:**
- Werft: Chantier Naval, Antibes
- Dauer: 3 Wochen (inkl. alten BSR-Ausbau, neuer Tunnel, HSR-Tunnel)
- Gesamtkosten: 38.000 EUR (Material: 28.000 EUR, Arbeit: 10.000 EUR)

**Ergebnis:**
- Chartercrews berichten „Seitwärts in die Box — wie ein Auto einparken"
- Kein Rammschaden seit Installation (vorher 2–3 pro Saison)
- ROI durch vermiedene Reparaturen: Amortisation nach 2 Saisons
- AYDI-Bewertung: 95/100

**Confidence:** measured (professionelle Installation), documented (Charter-Feedback über 2 Saisons)

### Fallstudie 3: Hallberg-Rassy 44 — Retractable Thruster

**Ausgangssituation:**
- Boot: Hallberg-Rassy 44, Baujahr 2021
- Eigner: Performance-orientierter Blauwasser-Segler
- Problem: Bugstrahlruder gewünscht, aber kein Tunnelrohr (Widerstand unter Segeln)
- Budget: 15.000 EUR

**Analyse:**
- Bootslänge: 13,50m, Verdrängung: 13.500 kg
- Empfohlener Schub: 75–95 kgf
- Performance-Anforderung: kein Widerstand bei Segeln (Regatta-Teilnahme)
- Bordnetz: 24V

**Lösung:**
- Thruster: Side-Power EX95 (Retractable, 95 kgf, 24V)
- Batterie: Victron Lithium LiFePO4 100Ah (24V)
- Fernbedienung: Side-Power Funk-Fernbedienung

**Einbau:**
- Werft: Hallberg-Rassy Varv, Ellös (Schweden)
- Dauer: 5 Tage
- Gesamtkosten: 14.200 EUR (Material: 12.000 EUR, Arbeit: 2.200 EUR)

**Ergebnis:**
- Unter Segeln: null Widerstand, kein Tunnelgeräusch
- Ausfahrzeit: 22 Sekunden (Eigner muss vorausplanen)
- Schub ausreichend für Hafenmanöver
- Einziger Nachteil: komplexere Wartung bei Hallberg-Rassy Werft
- AYDI-Bewertung: 89/100

**Confidence:** measured (Werft-Dokumentation), documented (Eigner-Feedback)

### Fallstudie 4: Linssen Grand Sturdy 40.0 — Hydraulischer Thruster

**Ausgangssituation:**
- Boot: Linssen Grand Sturdy 40.0 AC, Baujahr 2020, Stahlverdränger
- Nutzung: Binnengewässer (Niederlande, Frankreich), Dauerleben an Bord
- Problem: Schleusenmanöver erfordern langen Thruster-Betrieb
- Budget: 10.000 EUR

**Analyse:**
- Bootslänge: 12,85m, Verdrängung: 14.500 kg
- Anforderung: Dauerbetrieb in Schleusen (bis 10 Minuten am Stück)
- Vorhandener BSR: Vetus BOW75 (elektrisch, 12V) → Duty Cycle Problem
- Elektrischer Thruster nicht ausreichend für Dauerbetrieb

**Lösung:**
- BSR: Vetus BOWH125 (hydraulisch, 125 kgf)
- Hydraulikpumpe: Vetus HT1010 (vom Hauptmotor angetrieben, PTO)
- Kein Duty Cycle: unbegrenzter Betrieb bei laufendem Motor

**Einbau:**
- Werft: Linssen Yachts Service, Maasbracht
- Dauer: 2 Wochen (hydraulische Leitungen, Pumpe, alter BSR Demontage)
- Gesamtkosten: 9.800 EUR (Material: 7.200 EUR, Arbeit: 2.600 EUR)

**Ergebnis:**
- Schleusenmanöver jetzt stressfrei — Thruster läuft so lange wie nötig
- Deutlich leiser als der alte elektrische Thruster
- Wartung: jährlich Hydrauliköl und Filter (150 EUR)
- AYDI-Bewertung: 91/100

**Confidence:** measured (Werft-Installation), documented (Eigner nach 2 Jahren Betrieb)

### Fallstudie 5: Fountaine Pajot Elba 45 — Katamaran BSR

**Ausgangssituation:**
- Boot: Fountaine Pajot Elba 45, Baujahr 2022, GFK-Katamaran
- Problem: Kein werkseitiger Bugstrahlruder, Anlegen bei Seitenwind mit 14m Breite schwierig
- Eigner: Ehepaar, 2-Personen-Crew

**Analyse:**
- Bootslänge: 13,40m, Breite: 7,42m
- Verdrängung: 11.500 kg, aber große Windangriffsfläche (Brücke + Salon)
- Kein zentrales Tunnelrohr möglich (zwei Rümpfe)
- Empfohlener Schub: 120–160 kgf gesamt

**Lösung:**
- 2× Vetus BOW55-24 (je 55 kgf, 24V, 150mm Tunnel) — einer pro Rumpf
- Gemeinsame Steuerung: beide BSR gleichzeitig angesteuert
- Batterie: 1× Victron Lithium 200Ah (24V) für beide BSR

**Einbau:**
- Werft: Multi Marine, La Rochelle
- Dauer: 10 Tage (2× Rumpfdurchbruch, 2× Tunnelrohr)
- Gesamtkosten: 8.500 EUR (Material: 6.200 EUR, Arbeit: 2.300 EUR)

**Ergebnis:**
- 110 kgf Gesamtschub — ausreichend für Manöver bis 15 kn Seitenwind
- Ehefrau: „Ich lege jetzt auch alleine an — das war vorher undenkbar"
- Synchron-Steuerung funktioniert einwandfrei
- AYDI-Bewertung: 85/100 (Abzug: knapp dimensioniert für 20+ kn Wind)

**Confidence:** measured (Installation), documented (Eigner-Feedback)

### Fallstudie 6: Azimut 50 — Quick BTDC Erstausstattung

**Ausgangssituation:**
- Boot: Azimut 50, Baujahr 2024, GFK (Neubau)
- Eigner: Erstbesitzer, Heimathafen Mallorca (Port Adriano)
- Konfiguration bei Bestellung: BSR + HSR als Werkspaket

**Analyse:**
- Bootslänge: 15,24m, Verdrängung: 21.000 kg
- Flybridge-Version → hohe Windangriffsfläche
- Bordnetz: 24V
- Werkseitig vorgesehen: Quick BTDC 12524 (BSR) + Quick BTDC 9524 (HSR)

**Werksinstallation:**
- BSR: Quick BTDC 12524 (125 kgf, 24V, 200mm Tunnel)
- HSR: Quick BTDC 9524 (95 kgf, 24V, 185mm Tunnel)
- Steuerung: Quick T-Link Farbdisplay + proportionaler Joystick
- Batterie: 2× Quick FLPR 200Ah AGM (dediziert für Thruster)

**Preis (im Werkspaket):**
- BSR + HSR + Steuerung + Batterien: 14.500 EUR (Aufpreis über Basispreis)
- Deutlich günstiger als Nachrüstung (geschätzt: 22.000 EUR)

**Ergebnis:**
- Perfekte Integration in Azimut-Bordsystem
- T-Link Display zeigt Schub, Batterie, Duty Cycle in Echtzeit
- Seitwärtsfahrt in die Box — kein Problem
- AYDI-Bewertung: 93/100 (Abzug: HSR leicht unterdimensioniert für Starkwind)

**Confidence:** measured (Werks-Dokumentation), documented (Eigner nach 1 Saison)

### Fallstudie 7: Vetus BOW PRO GO Nachrüstung auf Segelyacht 9m

**Ausgangssituation:**
- Boot: Dufour 382 Grand Large, Baujahr 2016, GFK
- Eigner: Wochenend-Segler, Budget-bewusst
- Problem: Anlegen in Heimatmarina bei Seitenwind mühsam
- Budget: max. 2.000 EUR

**Analyse:**
- Bootslänge: 11,25m (Rumpf), Verdrängung: 7.800 kg
- Empfohlener Schub: 45–65 kgf
- Kein Rumpfdurchbruch gewünscht → externer Thruster
- Bordnetz: 12V, 2× 95Ah AGM

**Lösung:**
- Thruster: Vetus BOW PRO GO 46 (46 kgf, 12V, klappbar extern)
- Keine zusätzliche Batterie (vorhandene 95Ah ausreichend für gelegentliche Nutzung)
- Eigeneinbau

**Einbau:**
- Montage: Eigner selbst (Samstagnachmittag, 4 Stunden)
- Kabeldurchführung: bestehende Ankerketten-Luke genutzt
- Kabel: 50mm², 5m
- Gesamtkosten: 1.950 EUR (nur Material)

**Ergebnis:**
- 46 kgf reichen für Manöver bis 10–12 kn Seitenwind
- Klappbar: bei Segeln eingeklappt, kaum Widerstand
- Eigeneinbau hat funktioniert (Eigner ist Elektroingenieur)
- Schwachpunkt: unter 46 kgf bei stärkerem Wind an der Grenze
- AYDI-Bewertung: 72/100 (Abzug: knapp dimensioniert, extern, keine eigene Batterie)

**Confidence:** documented (Eigner-Bericht), estimated (Schub-Bewertung)

### Fallstudie 8: Sunseeker Manhattan 60 — Hydraulik-Komplettanlage mit Stabilisatoren

**Ausgangssituation:**
- Boot: Sunseeker Manhattan 60, Baujahr 2018
- Nutzung: Privatyacht, Mittelmeer, mit Crew
- Problem: Bestehende elektrische Thruster zu schwach, Duty-Cycle-Probleme beim Anlegen in Starkwind-Häfen (Mistral)
- Budget: 50.000 EUR (Thruster + Stabilisatoren zusammen)

**Analyse:**
- Bootslänge: 18,56m, Verdrängung: 35.000 kg
- Flybridge → Windangriffsfläche ca. 55 m²
- Mistral: regelmäßig 25–35 kn Seitenwind in südfranzösischen Häfen
- Empfohlener Schub: BSR 300+ kgf, HSR 400+ kgf
- Vorhandenes Hydrauliksystem für Stabilisatoren nutzbar

**Lösung:**
- BSR: Side-Power SH300 (300 kgf, hydraulisch, 300mm Tunnel)
- HSR: Side-Power SH420 (420 kgf, hydraulisch, 350mm Tunnel)
- Hydraulikpumpe: Twin-Disc PTO am Hauptmotor (beide Motoren)
- Zentrales Hydrauliksystem auch für Seakeeper-Stabilisatoren
- Steuerung: Side-Power Joystick + Garmin Helm-Integration

**Einbau:**
- Werft: MB92, Barcelona
- Dauer: 6 Wochen (komplettes Hydrauliksystem, Rumpfarbeiten)
- Gesamtkosten: 48.000 EUR (Material: 33.000 EUR, Arbeit: 15.000 EUR)

**Ergebnis:**
- Unbegrenzter Betrieb — kein Duty Cycle mehr
- 720 kgf Gesamtschub — Anlegen auch bei 30 kn Mistral sicher
- Hydrauliksystem versorgt zusätzlich Stabilisatoren und Passerelle
- Crew: „Das Boot ist eine andere Welt — absolut souverän"
- AYDI-Bewertung: 97/100

**Confidence:** measured (Werft-Dokumentation, Schub-Messprotokoll), documented (Crew-Feedback über 3 Saisons)

---

## 27. ANHANG A: Normen und Vorschriften

### 27.1 Relevante ISO-Normen

| Norm | Titel | Relevanz für Thruster |
|------|-------|----------------------|
| ISO 12217 | Stabilitätsbewertung | Gewicht des Thrusters in Stabilitätsberechnung |
| ISO 13297 | Elektrische Systeme — Wechselstrom | Hydraulik-Aggregate mit AC-Motor |
| ISO 10133 | Elektrische Systeme — Gleichstrom | DC-Thruster-Installation, Kabelquerschnitte |
| ISO 9094 | Brandschutz | Kabel-Führung, Sicherungen, Batterie-Belüftung |
| ISO 8846 | Elektrische Geräte — Zündschutz | Thruster in Umgebung von Gas/Kraftstoff |
| ISO 15085 | Mann-über-Bord-Prävention | Gitter am Thruster, Kennzeichnung |

### 27.2 ABYC-Standards (USA)

| Standard | Relevanz |
|----------|----------|
| ABYC E-11 | AC & DC Electrical Systems — Kabelquerschnitte, Sicherungen |
| ABYC E-2 | Cathodic Protection — Anoden, Streustrom |
| ABYC H-2 | Ventilation of Boats Using Gasoline — Benzin-/Kraftstoff-Entlüftung; relevant nur für Thruster in Benzin-Motorräumen. Batterie-Belüftung dagegen unter ABYC E-11 (siehe erste Zeile) |

> ✅ Aufgeloest (Audit): ABYC H-2 = "Ventilation of Boats Using Gasoline" (Benzin-Entlüftung), NICHT Batterie-Belüftung; die Belüftung von Thruster-Batterien fällt unter ABYC E-11. Zeile korrigiert (Titel richtiggestellt, auf 2 Spalten gebracht). — Quelle: ABYC H-2 (ANSI webstore preview_H-2.pdf; law.resource.org/pub/us/cfr/ibr/001/abyc.H-02.1989.pdf), ABYC E-11 (AC and DC Electrical Systems on Boats).

### 27.3 CE-Konformität

Bug- und Heckstrahlruder als Schiffsausrüstung unterliegen der Maschinenrichtlinie 2006/42/EG und der Niederspannungsrichtlinie 2014/35/EU (für >50V AC / >75V DC). Für 12V/24V-DC-Thruster gilt:
- CE-Kennzeichnung durch Hersteller
- Konformitätserklärung muss vorliegen
- EMV-Richtlinie 2014/30/EU für alle Steuerungskomponenten

---

## 28. ANHANG B: Confidence-Mapping

### 28.1 Confidence-Levels für Thruster-Bewertungen

| Datenquelle | Confidence | Beispiel |
|-------------|-----------|----------|
| Hersteller-Datenblatt | measured | Schubkraft, Stromaufnahme, Tunnel-Ø |
| Herstellerübergreifender Test | measured | Vergleichstests in Fachzeitschriften |
| CAD/Messung am Boot | measured | Tunnelposition, Kabellänge, Batteriespannung |
| Berechnung aus Messdaten | calculated | Erforderliche Schubkraft aus Lateralfläche |
| Foto Tunnelrohr/Propeller | visual_high | Korrosion, Bewuchs, sichtbare Schäden |
| Foto von außen (Gitter) | visual_medium | Gitter-Zustand, Tunnelposition |
| Foto Innere Installation | visual_medium | Kabelverlauf, Batterieposition |
| Unscharfes / dunkles Foto | visual_low | Kaum verwertbar |
| Servicebericht | documented | Anodenverbrauch, Reparaturhistorie |
| Eigner-Aussage ohne Beleg | estimated | „Der Thruster hat 75 kgf" ohne Typenschild |
| Klassen-Durchschnitt | benchmark | Typischer Schub für 12m-Segelyacht |
| Nicht beurteilbar | visual_insufficient | Thruster unter Wasser, kein Zugang |

### 28.2 Modulzuordnung

Im AYDI-Analysesystem wird die Thruster-Bewertung dem Modul **structural** (Antriebstechnik) zugeordnet mit Score-Fusion-Gewichtung:
- Strukturiert (CAD/Messdaten): 0,95
- Visuell (Fotos): 0,05

Für den Zustand (Korrosion, Bewuchs) wird das Modul **materials** herangezogen:
- Strukturiert: 0,35
- Visuell: 0,65

---

## 29. ANHANG C: Pydantic v2 Datenmodelle

```python
"""
AYDI Pydantic v2 Modelle für Bug- und Heckstrahlruder.
Alle Modelle verwenden model_config statt class Config (Pydantic v2).
"""

from pydantic import BaseModel, Field
from typing import Optional, Literal
from enum import Enum
from datetime import date


# --- Enums ---

class ThrusterType(str, Enum):
    TUNNEL = "tunnel"
    RETRACTABLE = "retractable"
    EXTERNAL = "external"


class ThrusterPosition(str, Enum):
    BOW = "bow"
    STERN = "stern"


class DriveType(str, Enum):
    ELECTRIC_12V = "electric_12v"
    ELECTRIC_24V = "electric_24v"
    HYDRAULIC_PTO = "hydraulic_pto"
    HYDRAULIC_SEPARATE = "hydraulic_separate"


class PropellerMaterial(str, Enum):
    PLASTIC = "plastic"
    BRONZE = "bronze"
    STAINLESS_STEEL = "stainless_steel"


class TunnelMaterial(str, Enum):
    GFK = "gfk"
    ALUMINUM = "aluminum"
    STAINLESS_STEEL = "stainless_steel"
    PLASTIC = "plastic"


class AnodeMaterial(str, Enum):
    ZINC = "zinc"
    ALUMINUM = "aluminum"
    MAGNESIUM = "magnesium"


class ConfidenceLevel(str, Enum):
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class ConditionRating(str, Enum):
    EXCELLENT = "excellent"
    GOOD = "good"
    FAIR = "fair"
    POOR = "poor"
    CRITICAL = "critical"
    NOT_ASSESSABLE = "nicht_beurteilbar"


class BatteryType(str, Enum):
    AGM = "agm"
    GEL = "gel"
    LITHIUM_LIFEPO4 = "lithium_lifepo4"
    LEAD_ACID = "lead_acid"


# --- Core Models ---

class ThrusterSpec(BaseModel):
    """Spezifikation eines Bug- oder Heckstrahlruders."""

    model_config = {"from_attributes": True}

    manufacturer: str = Field(..., description="Hersteller (z.B. Vetus, Side-Power)")
    model: str = Field(..., description="Modellbezeichnung (z.B. BOW75, SE80)")
    thruster_type: ThrusterType = Field(..., description="Typ des Thrusters")
    position: ThrusterPosition = Field(..., description="Bug oder Heck")
    drive_type: DriveType = Field(..., description="Antriebsart")
    thrust_kgf: float = Field(..., ge=10, le=600, description="Schubkraft in kgf")
    thrust_lbf: Optional[float] = Field(None, description="Schubkraft in lbf")
    tunnel_diameter_mm: Optional[int] = Field(None, ge=100, le=400, description="Tunnel-Ø in mm")
    power_watts: Optional[int] = Field(None, description="Elektrische Leistung in Watt")
    current_amps: Optional[float] = Field(None, description="Stromaufnahme in Ampere")
    voltage: Optional[int] = Field(None, description="Betriebsspannung in Volt")
    duty_cycle_on_min: Optional[float] = Field(None, description="Einschaltdauer in Minuten")
    duty_cycle_off_min: Optional[float] = Field(None, description="Pausenzeit in Minuten")
    hydraulic_power_kw: Optional[float] = Field(None, description="Hydraulikleistung in kW")
    propeller_material: Optional[PropellerMaterial] = Field(None, description="Propeller-Material")
    propeller_blades: Optional[int] = Field(None, ge=2, le=4, description="Anzahl Propellerblätter")
    tunnel_material: Optional[TunnelMaterial] = Field(None, description="Tunnelrohr-Material")
    has_proportional_control: bool = Field(False, description="Proportionalsteuerung vorhanden")
    has_thermal_protection: bool = Field(True, description="Thermoschutz vorhanden")
    brushless_motor: bool = Field(False, description="Bürstenloser Motor")
    weight_kg: Optional[float] = Field(None, description="Gewicht der Einheit in kg")
    price_eur: Optional[float] = Field(None, description="Listenpreis in EUR")
    year_of_manufacture: Optional[int] = Field(None, description="Baujahr")
    serial_number: Optional[str] = Field(None, description="Seriennummer")


class ThrusterInstallation(BaseModel):
    """Einbau-Dokumentation eines Thrusters."""

    model_config = {"from_attributes": True}

    thruster_spec: ThrusterSpec = Field(..., description="Thruster-Spezifikation")
    installation_date: Optional[date] = Field(None, description="Einbaudatum")
    installer: Optional[str] = Field(None, description="Einbau-Werft oder Person")
    tunnel_position_from_bow_pct: Optional[float] = Field(
        None, ge=0, le=30,
        description="Tunnelposition in % der LWL vom Bug"
    )
    tunnel_depth_below_wl_mm: Optional[int] = Field(
        None, description="Tunnelmitte unter Wasserlinie in mm"
    )
    cable_length_m: Optional[float] = Field(None, description="Kabellänge Batterie→Motor in m")
    cable_cross_section_mm2: Optional[float] = Field(None, description="Kabelquerschnitt in mm²")
    fuse_rating_amps: Optional[int] = Field(None, description="Hauptsicherung in Ampere")
    dedicated_battery: bool = Field(False, description="Dedizierte Thruster-Batterie vorhanden")
    battery_type: Optional[BatteryType] = Field(None, description="Batterietyp")
    battery_capacity_ah: Optional[float] = Field(None, description="Batteriekapazität in Ah")
    has_grids: bool = Field(True, description="Schutzgitter montiert")
    installation_cost_eur: Optional[float] = Field(None, description="Einbaukosten gesamt in EUR")
    confidence: ConfidenceLevel = Field(
        ConfidenceLevel.ESTIMATED,
        description="Datenqualität der Installation"
    )


class ThrusterConditionAssessment(BaseModel):
    """Zustandsbewertung eines installierten Thrusters."""

    model_config = {"from_attributes": True}

    overall_condition: ConditionRating = Field(..., description="Gesamtzustand")
    propeller_condition: ConditionRating = Field(
        ConditionRating.NOT_ASSESSABLE,
        description="Propellerzustand"
    )
    tunnel_condition: ConditionRating = Field(
        ConditionRating.NOT_ASSESSABLE,
        description="Tunnelrohr-Zustand"
    )
    anode_condition: ConditionRating = Field(
        ConditionRating.NOT_ASSESSABLE,
        description="Anoden-Zustand"
    )
    anode_material: Optional[AnodeMaterial] = Field(None, description="Anoden-Material")
    anode_remaining_pct: Optional[float] = Field(
        None, ge=0, le=100,
        description="Geschätzter Anoden-Rest in %"
    )
    motor_condition: ConditionRating = Field(
        ConditionRating.NOT_ASSESSABLE,
        description="Motor-Zustand"
    )
    electrical_condition: ConditionRating = Field(
        ConditionRating.NOT_ASSESSABLE,
        description="Zustand der elektrischen Installation"
    )
    corrosion_found: bool = Field(False, description="Korrosion festgestellt")
    corrosion_type: Optional[str] = Field(None, description="Art der Korrosion")
    corrosion_severity: Optional[Literal["gering", "mittel", "stark", "kritisch"]] = Field(
        None, description="Schwere der Korrosion"
    )
    biofouling_level: Optional[Literal["kein", "leicht", "mittel", "stark"]] = Field(
        None, description="Bewuchsgrad"
    )
    water_ingress: bool = Field(False, description="Wassereinbruch festgestellt")
    last_anode_change: Optional[date] = Field(None, description="Letzter Anodenwechsel")
    last_service: Optional[date] = Field(None, description="Letzte Wartung")
    operating_hours: Optional[float] = Field(None, description="Betriebsstunden (geschätzt)")
    findings: list[str] = Field(default_factory=list, description="Befunde (einzeln)")
    recommendations: list[str] = Field(default_factory=list, description="Empfehlungen")
    confidence: ConfidenceLevel = Field(..., description="Datenqualität der Bewertung")
    score: Optional[float] = Field(None, ge=0, le=100, description="AYDI-Score 0–100")


class ThrusterDimensioningInput(BaseModel):
    """Eingabedaten für die Thruster-Dimensionierung."""

    model_config = {"from_attributes": True}

    boat_length_m: float = Field(..., ge=5, le=40, description="Bootslänge in m")
    lwl_m: Optional[float] = Field(None, description="Länge Wasserlinie in m")
    beam_m: Optional[float] = Field(None, description="Breite in m")
    displacement_kg: float = Field(..., ge=500, le=200000, description="Verdrängung in kg")
    boat_type: Literal["sailboat", "motorboat", "catamaran"] = Field(
        ..., description="Bootstyp"
    )
    has_flybridge: bool = Field(False, description="Flybridge vorhanden")
    lateral_area_m2: Optional[float] = Field(
        None, description="Lateralfläche über WL in m²"
    )
    typical_wind_kn: float = Field(
        15.0, ge=5, le=40,
        description="Typischer Seitenwind bei Manöver in Knoten"
    )
    voltage: Optional[int] = Field(None, description="Vorhandenes Bordnetz in Volt")
    budget_eur: Optional[float] = Field(None, description="Budget in EUR")
    prefers_retractable: bool = Field(False, description="Einziehbarer Thruster bevorzugt")
    needs_stern_thruster: bool = Field(False, description="Heckstrahlruder gewünscht")


class ThrusterDimensioningResult(BaseModel):
    """Ergebnis der Thruster-Dimensionierung."""

    model_config = {"from_attributes": True}

    recommended_thrust_kgf: float = Field(..., description="Empfohlene Schubkraft in kgf")
    minimum_thrust_kgf: float = Field(..., description="Mindest-Schubkraft in kgf")
    recommended_tunnel_mm: int = Field(..., description="Empfohlener Tunnel-Ø in mm")
    recommended_voltage: int = Field(..., description="Empfohlene Spannung in Volt")
    recommended_type: ThrusterType = Field(..., description="Empfohlener Thruster-Typ")
    recommended_drive: DriveType = Field(..., description="Empfohlene Antriebsart")
    stern_thruster_recommended: bool = Field(False, description="Heckstrahlruder empfohlen")
    stern_thrust_kgf: Optional[float] = Field(
        None, description="Empfohlener Heckschub in kgf"
    )
    estimated_wind_force_kgf: float = Field(
        ..., description="Berechnete Windkraft in kgf"
    )
    lateral_area_used_m2: float = Field(
        ..., description="Verwendete Lateralfläche in m²"
    )
    matching_models: list[str] = Field(
        default_factory=list,
        description="Passende Modelle (Herst. + Modell)"
    )
    estimated_total_cost_eur: Optional[float] = Field(
        None, description="Geschätzte Gesamtkosten in EUR"
    )
    notes: list[str] = Field(default_factory=list, description="Hinweise zur Dimensionierung")
    confidence: ConfidenceLevel = Field(..., description="Datenqualität")


class ThrusterElectricalCheck(BaseModel):
    """Elektrische Prüfung der Thruster-Installation."""

    model_config = {"from_attributes": True}

    battery_voltage_no_load: Optional[float] = Field(
        None, description="Batteriespannung ohne Last in V"
    )
    battery_voltage_under_load: Optional[float] = Field(
        None, description="Batteriespannung unter Last in V"
    )
    voltage_drop_v: Optional[float] = Field(
        None, description="Spannungsabfall am Kabel in V"
    )
    motor_current_amps: Optional[float] = Field(
        None, description="Gemessener Motorstrom in A"
    )
    cable_cross_section_mm2: Optional[float] = Field(
        None, description="Kabelquerschnitt in mm²"
    )
    cable_length_m: Optional[float] = Field(
        None, description="Kabellänge in m"
    )
    fuse_rating_amps: Optional[int] = Field(
        None, description="Sicherungswert in A"
    )
    fuse_condition: Optional[Literal["ok", "defekt", "nicht_geprüft"]] = Field(
        None, description="Sicherungszustand"
    )
    solenoid_condition: Optional[Literal["ok", "verschlissen", "defekt", "nicht_geprüft"]] = Field(
        None, description="Solenoid-Zustand"
    )
    stray_current_ma: Optional[float] = Field(
        None, description="Streustrom Rumpf-Wasser in mA"
    )
    insulation_resistance_mohm: Optional[float] = Field(
        None, description="Isolationswiderstand in MΩ"
    )
    cable_condition: Optional[Literal["ok", "korrodiert", "beschädigt"]] = Field(
        None, description="Kabelzustand"
    )
    findings: list[str] = Field(default_factory=list, description="Elektrische Befunde")
    pass_fail: Optional[Literal["bestanden", "nicht_bestanden", "teilweise"]] = Field(
        None, description="Prüfergebnis"
    )
    confidence: ConfidenceLevel = Field(..., description="Datenqualität")


class ThrusterMaintenanceAction(BaseModel):
    """Einzelne Wartungsmaßnahme."""

    model_config = {"from_attributes": True}

    action: str = Field(..., description="Beschreibung der Maßnahme")
    category: Literal[
        "routine", "verschleiss", "korrosion", "elektrisch", "mechanisch", "notfall"
    ] = Field(..., description="Kategorie der Maßnahme")
    interval_months: Optional[int] = Field(None, description="Empfohlenes Intervall in Monaten")
    interval_hours: Optional[int] = Field(None, description="Empfohlenes Intervall in Betriebsstunden")
    estimated_duration_hours: Optional[float] = Field(None, description="Geschätzte Dauer in Stunden")
    estimated_cost_eur: Optional[float] = Field(None, description="Geschätzte Kosten in EUR")
    requires_slipway: bool = Field(False, description="Slipanlage erforderlich")
    diy_possible: bool = Field(True, description="Selbstdurchführung möglich")
    priority: Literal["niedrig", "mittel", "hoch", "kritisch"] = Field(
        "mittel", description="Priorität"
    )


class ThrusterMaintenanceSchedule(BaseModel):
    """Wartungsplan für einen Thruster."""

    model_config = {"from_attributes": True}

    thruster_model: str = Field(..., description="Thruster-Modell")
    installation_date: Optional[date] = Field(None, description="Einbaudatum")
    operating_hours: Optional[float] = Field(None, description="Aktuelle Betriebsstunden")
    actions: list[ThrusterMaintenanceAction] = Field(
        default_factory=list,
        description="Wartungsmaßnahmen"
    )
    next_anode_check: Optional[date] = Field(None, description="Nächste Anodenprüfung")
    next_full_service: Optional[date] = Field(None, description="Nächste Vollwartung")
    estimated_annual_cost_eur: Optional[float] = Field(
        None, description="Geschätzte jährliche Wartungskosten in EUR"
    )
    confidence: ConfidenceLevel = Field(..., description="Datenqualität")


class ThrusterAnalysis(BaseModel):
    """Gesamtanalyse Bug-/Heckstrahlruder — AYDI Hauptmodell."""

    model_config = {"from_attributes": True}

    boat_id: Optional[str] = Field(None, description="AYDI Boot-ID")
    zone: str = Field("thruster", description="Analysezone")
    spec: Optional[ThrusterSpec] = Field(None, description="Thruster-Spezifikation")
    installation: Optional[ThrusterInstallation] = Field(None, description="Einbau-Details")
    condition: Optional[ThrusterConditionAssessment] = Field(None, description="Zustandsbewertung")
    dimensioning: Optional[ThrusterDimensioningResult] = Field(
        None, description="Dimensionierungs-Ergebnis"
    )
    electrical_check: Optional[ThrusterElectricalCheck] = Field(
        None, description="Elektrische Prüfung"
    )
    maintenance: Optional[ThrusterMaintenanceSchedule] = Field(
        None, description="Wartungsplan"
    )
    overall_score: Optional[float] = Field(None, ge=0, le=100, description="Gesamtscore 0–100")
    findings: list[str] = Field(default_factory=list, description="Gesamtbefunde")
    recommendations: list[str] = Field(default_factory=list, description="Gesamtempfehlungen")
    data_completeness_pct: Optional[float] = Field(
        None, ge=0, le=100,
        description="Datenvollständigkeit in %"
    )
    confidence: ConfidenceLevel = Field(..., description="Gesamt-Confidence")
    analysis_version: str = Field("2.0", description="AYDI Analyseversion")
    available: bool = Field(True, description="Analyse verfügbar")
    unavailable_reason: Optional[str] = Field(
        None, description="Grund falls nicht verfügbar"
    )
```

---

## 30. ANHANG D: AYDI Bewertungsschema

### 30.1 Scoring-Kriterien für Thruster-Anlagen

| Kriterium | Gewicht | 100 Punkte | 50 Punkte | 0 Punkte |
|-----------|---------|-----------|-----------|----------|
| Dimensionierung | 25% | ≥120% der Empfehlung | 80–100% der Empfehlung | <60% der Empfehlung |
| Einbauqualität | 20% | Professionell, dokumentiert | Solide, kleine Mängel | Fehlerhaft, nicht dokumentiert |
| Elektrische Installation | 15% | Korrekt dimensioniert, sauber | Funktional, kleine Mängel | Unterdimensioniert, gefährlich |
| Korrosionsschutz | 15% | Anoden frisch, kein Streustrom | Anoden 30–50%, kein Streustrom | Keine Anoden, Streustrom |
| Tunnelrohr-Zustand | 10% | Einwandfrei, kein Bewuchs | Leichter Bewuchs, intakt | Korrodiert, beschädigt |
| Propeller-Zustand | 5% | Wie neu, keine Beschädigungen | Leichte Gebrauchsspuren | Beschädigt, unwuchtig |
| Wartungszustand | 5% | Regelmäßig gewartet, dokumentiert | Gelegentlich gewartet | Keine Wartung |
| Steuerung/Bedienung | 5% | Proportional, Panel einwandfrei | Ein/Aus, funktional | Defekt, unsicher |

### 30.2 Bewertungsstufen

| Score | Bewertung | Handlungsbedarf |
|-------|-----------|-----------------|
| 90–100 | Hervorragend | Kein Handlungsbedarf |
| 75–89 | Gut | Optionale Verbesserungen |
| 60–74 | Befriedigend | Wartung empfohlen |
| 40–59 | Mangelhaft | Reparatur/Upgrade erforderlich |
| 20–39 | Schlecht | Dringender Handlungsbedarf |
| 0–19 | Kritisch | Sicherheitsrelevant — sofortige Maßnahme |

### 30.3 Automatische Flags

| Befund | Flag | Priorität |
|--------|------|-----------|
| Kein Bugstrahlruder bei Boot >12m | INFO | Niedrig |
| Thruster unterdimensioniert (<70% Empfehlung) | WARNUNG | Mittel |
| Anoden >70% verbraucht | WARNUNG | Hoch |
| Streustrom >30mA | ALARM | Kritisch |
| Wassereinbruch am Thruster | ALARM | Kritisch |
| Sicherung fehlt oder unterdimensioniert | ALARM | Kritisch |
| Kabel ohne Kabelschuhe (gelötet in Hochstrom) | WARNUNG | Hoch |
| Thruster ohne Schutzgitter | INFO | Niedrig |
| Duty Cycle regelmäßig überschritten | WARNUNG | Mittel |
| Motor >500 Betriebsstunden ohne Wartung | WARNUNG | Mittel |
| Aluminium-Tunnel + Bronze-Propeller | ALARM | Hoch |
| Keine dedizierte Thruster-Batterie bei >75kgf | WARNUNG | Mittel |

---

## 31. ANHANG E: Erweiterte Herstellerdaten und Modellvergleiche

### 31.1 Vetus BOW-Serie — Technische Detaildaten

**Motorspezifikationen:**

| Modell | Motortyp | Drehzahl [U/min] | Bürsten | Kohlebürsten-Ø [mm] | Gewicht Motor [kg] |
|--------|----------|-------------------|---------|---------------------|-------------------|
| BOW25 | DC Bürstenmotor | 2.800 | 2 | 8×12 | 3,2 |
| BOW35 | DC Bürstenmotor | 2.800 | 2 | 10×14 | 4,1 |
| BOW45 | DC Bürstenmotor | 2.600 | 2 | 10×14 | 5,3 |
| BOW55 | DC Bürstenmotor | 2.400 | 4 | 10×16 | 6,8 |
| BOW75 | DC Bürstenmotor | 2.200 | 4 | 12×18 | 8,5 |
| BOW95 | DC Bürstenmotor | 2.000 | 4 | 12×18 | 11,2 |
| BOW125-24 | DC Bürstenmotor | 2.200 | 4 | 12×20 | 13,5 |
| BOW160-24 | DC Bürstenmotor | 2.000 | 4 | 14×22 | 18,0 |
| BOW230-24 | DC Bürstenmotor | 1.800 | 4 | 14×22 | 24,5 |
| BOW285-24 | DC Bürstenmotor | 1.600 | 4 | 16×24 | 32,0 |
| BOW340-24 | DC Bürstenmotor | 1.500 | 4 | 16×24 | 38,0 |

**Getriebe-Spezifikationen:**

| Modell | Getriebetyp | Untersetzung | Getriebeöl | Ölmenge [ml] |
|--------|-------------|-------------|-----------|-------------|
| BOW25–45 | Schneckengetriebe | 4,5:1 | SAE 80W-90 GL4 | 80 |
| BOW55–75 | Kegelradgetriebe | 3,8:1 | SAE 80W-90 GL4 | 120 |
| BOW95–125 | Kegelradgetriebe | 3,5:1 | SAE 80W-90 GL5 | 180 |
| BOW160–230 | Kegelradgetriebe | 3,2:1 | SAE 80W-90 GL5 | 250 |
| BOW285–340 | Planetengetriebe | 3,0:1 | Synthetic 75W-90 | 350 |

**Einbaumaße (Motor-Einheit hinter Tunnelrohr):**

| Modell | Länge [mm] | Breite [mm] | Höhe [mm] | Abstand Tunnel→Schott min. [mm] |
|--------|-----------|-----------|---------|-------------------------------|
| BOW25 | 280 | 140 | 160 | 320 |
| BOW35 | 310 | 155 | 175 | 350 |
| BOW45 | 340 | 165 | 185 | 380 |
| BOW55 | 365 | 180 | 200 | 420 |
| BOW75 | 395 | 195 | 220 | 450 |
| BOW95 | 430 | 215 | 245 | 490 |
| BOW125-24 | 470 | 235 | 270 | 530 |
| BOW160-24 | 520 | 260 | 300 | 590 |
| BOW230-24 | 580 | 290 | 340 | 660 |
| BOW285-24 | 640 | 320 | 380 | 730 |
| BOW340-24 | 700 | 350 | 420 | 800 |

### 31.2 Side-Power — Erweiterte Daten

**Geräuschemission (gemessen nach ISO 14509):**

| Modell | Geräusch an Deck [dB(A)] | Geräusch Vorschiffskabine [dB(A)] | Geräusch extern 10m [dB(A)] |
|--------|-------------------------|----------------------------------|----------------------------|
| SE30 | 58 | 68 | 52 |
| SE60 | 62 | 72 | 56 |
| SE80 | 64 | 74 | 58 |
| SE100 | 66 | 76 | 60 |
| SP125 | 64 | 72 | 58 |
| SP155 | 66 | 74 | 60 |
| SP240 | 68 | 76 | 62 |
| SP300 | 70 | 78 | 64 |
| SH160 (hydr.) | 54 | 62 | 48 |
| SH300 (hydr.) | 58 | 66 | 52 |

**Side-Power Silence Mode — Messwerte:**

| Modell | Standard [dB(A)] | Silence Mode [dB(A)] | Schub-Reduktion |
|--------|-----------------|---------------------|-----------------|
| SP125 | 72 | 64 | -25% |
| SP155 | 74 | 66 | -25% |
| SP190 | 76 | 68 | -30% |
| SP240 | 78 | 70 | -30% |
| SP300 | 80 | 72 | -30% |

### 31.3 Lebensdauer-Erwartung nach Hersteller

| Komponente | Vetus | Side-Power | Max Power | Quick | Lewmar |
|------------|-------|-----------|-----------|-------|--------|
| Motor (gesamt) | 1.500 h | 2.000 h | 1.200 h | 1.800 h | 1.500 h |
| Kohlebürsten | 300–500 h | 400–600 h | 250–400 h | Bürstenlos ab 75kgf | 300–500 h |
| Kegelradgetriebe | 2.000 h | 2.500 h | 1.500 h | 2.000 h | 2.000 h |
| Wellendichtring | 500 h | 600 h | 400 h | 500 h | 500 h |
| Kugellager | 1.000 h | 1.200 h | 800 h | 1.000 h | 1.000 h |
| Kunststoff-Propeller | 1.000 h | 1.200 h | 800 h | 1.000 h | 1.000 h |
| Bronze-Propeller | 3.000+ h | 3.000+ h | 2.500+ h | 3.000+ h | 3.000+ h |

### 31.4 Ersatzteil-Preisvergleich

**Kohlebürsten-Satz (4 Stück):**

| Hersteller | Modellreihe | Preis [EUR] | Verfügbarkeit |
|------------|------------|-------------|---------------|
| Vetus | BOW25–45 | 28 | Sofort (SVB, Bukh Bremen) |
| Vetus | BOW55–95 | 38 | Sofort |
| Vetus | BOW125–340 | 48 | 1–3 Werktage |
| Side-Power | SE30–SE100 | 35 | 1–2 Wochen (Norwegen) |
| Side-Power | SP100–SP300 | 52 | 1–2 Wochen |
| Max Power | CT25–CT100 | 22 | 1–3 Werktage (Italien) |
| Quick | BTDC (Bürstenmodelle) | 30 | 1–2 Wochen |
| Lewmar | TT-Serie | 32 | 1–2 Wochen (UK) |

**Wellendichtring (Simmerring):**

| Hersteller | Modellreihe | Preis [EUR] | OEM-Nummer |
|------------|------------|-------------|-----------|
| Vetus | BOW25–75 | 18 | SET0088 |
| Vetus | BOW95–340 | 24 | SET0089 |
| Side-Power | SE/SP alle | 22 | 61054 |
| Max Power | CT alle | 15 | MPW-SL |
| Quick | BTDC alle | 20 | QSR-xxx |
| Lewmar | TT alle | 22 | 589055 |

**Lagersatz (Kugellager komplett):**

| Hersteller | Modellreihe | Preis [EUR] | Anzahl Lager |
|------------|------------|-------------|-------------|
| Vetus | BOW25–75 | 45 | 2 |
| Vetus | BOW95–340 | 65 | 3 |
| Side-Power | SE30–100 | 55 | 2 |
| Side-Power | SP100–300 | 80 | 3 |
| Max Power | CT25–125 | 35 | 2 |
| Quick | BTDC alle | 50 | 2–3 |
| Lewmar | TT alle | 50 | 2 |

---

## 32. ANHANG F: Bezugsquellen und Händler in Europa

### 32.1 Online-Händler

| Händler | Land | Schwerpunkt | URL | Besonderheit |
|---------|------|-----------|-----|-------------|
| SVB (Sailing & Vintage Boats) | DE | Alle Hersteller | svb-marine.de | Größter dt. Onlineshop, Vetus-Haupthändler |
| Compass24 | DE | Vetus, Max Power | compass24.de | Schnelle Lieferung, gute Preise |
| Bukh Bremen | DE | Vetus | bukh-bremen.de | Vetus-Importeur Deutschland |
| Toplicht | DE | Vetus, Side-Power | toplicht.de | Hamburg, auch Ladengeschäft |
| Bootsbedarf Lippstadt | DE | Alle Hersteller | bootsbedarf.de | Gute Beratung |
| Nautic-Markt | DE | Max Power, Quick | nautic-markt.de | Spezialist für ital. Hersteller |
| Maritimus | AT | Alle Hersteller | maritimus.at | Österreich, gute Lagerbestände |
| Boatoon | NL | Vetus, Side-Power | boatoon.com | Niederlande, direkt ab Lager |
| Force4 | UK | Lewmar, Side-Power | force4.co.uk | UK-Marktführer |
| Accastillage Diffusion | FR | Quick, Max Power | ad-france.com | Frankreich |
| Osculati | IT | Max Power, Quick | osculati.com | Italien, Großhandel |

### 32.2 Service-Werkstätten (Deutschland)

| Werkstatt | Ort | Spezialisierung | Kontakt |
|-----------|-----|-----------------|---------|
| Bukh Bremen | Bremen | Vetus Authorized Service | +49-421-xxx |
| Yachtservice Rostock | Rostock | Alle Hersteller, Ostsee | yachtservice-rostock.de |
| Bootstechnik Bodensee | Konstanz | Vetus, Side-Power | bootstechnik-bodensee.de |
| Marine Elektrik Hamburg | Hamburg | Elektrische Installation | marine-elektrik-hh.de |
| Werft Rathje | Kiel | Tunnel-Einbau, Stahl/Alu | werft-rathje.de |
| Yacht-Technik Fehmarn | Fehmarn | Nachrüstung, alle Marken | yacht-technik-fehmarn.de |
| Marina Werft Greifswald | Greifswald | Side-Power Authorized | marina-werft.de |
| Baltic Yachtservice | Travemünde | Vetus, Side-Power | baltic-yachtservice.de |

---

## 33. ANHANG G: Erweiterte Dimensionierungsformeln

### 33.1 Exakte Windkraft-Berechnung

```
F_wind = 0,5 × ρ × v² × A × C_d

F_wind = Windkraft auf das Boot [N]
ρ = Luftdichte (1,225 kg/m³ bei 15°C, Meeresniveau)
v = Windgeschwindigkeit [m/s] (1 kn = 0,5144 m/s)
A = Lateralfläche über Wasser [m²]
C_d = Widerstandsbeiwert
```

**Widerstandsbeiwerte (C_d) nach Aufbautyp:**

| Aufbautyp | C_d | Bemerkung |
|-----------|-----|-----------|
| Segelyacht, Decksalon | 0,85 | Relativ strömungsgünstig |
| Segelyacht, Doghouse | 0,90 | Leicht höher durch Aufbau |
| Motoryacht, Sedan | 0,95 | Glatte Aufbauten |
| Motoryacht, Flybridge | 1,10 | Zusätzliche Windangriffsfläche |
| Motoryacht, Trawler | 1,05 | Hohe Aufbauten |
| Katamaran | 1,15 | Breites Profil, Brückendeck |
| Motoryacht, Sportbridge | 1,00 | Niedrige Aufbauten |

**Windgeschwindigkeit und Winddruck:**

| Wind [kn] | Wind [m/s] | Winddruck [Pa] | Winddruck [kgf/m²] | Beaufort |
|-----------|-----------|----------------|---------------------|----------|
| 5 | 2,57 | 4,1 | 0,42 | 2 |
| 10 | 5,14 | 16,2 | 1,65 | 3 |
| 15 | 7,72 | 36,5 | 3,72 | 4–5 |
| 20 | 10,29 | 64,9 | 6,62 | 5 |
| 25 | 12,86 | 101,4 | 10,34 | 6 |
| 30 | 15,43 | 145,9 | 14,88 | 7 |
| 35 | 18,01 | 198,7 | 20,26 | 8 |

### 33.2 Lateralflächen-Abschätzung (wenn keine Zeichnung vorhanden)

**Segelyachten:**
```
A_lateral ≈ LOA × (Freibord_mittel + Aufbauhöhe × 0,7)
Freibord_mittel ≈ 0,08 × LOA + 0,3 [m]
Aufbauhöhe ≈ 0,07 × LOA + 0,5 [m]
```

**Motoryachten:**
```
A_lateral ≈ LOA × (Freibord_mittel + Aufbauhöhe × 0,85)
Freibord_mittel ≈ 0,10 × LOA + 0,4 [m]
Aufbauhöhe:
  - Sedan: 0,08 × LOA + 0,6 [m]
  - Flybridge: 0,12 × LOA + 1,0 [m]
  - Trawler: 0,10 × LOA + 0,8 [m]
```

**Katamarane:**
```
A_lateral ≈ LOA × (Freibord_mittel + Brückendeckhöhe × 0,9 + Aufbauhöhe × 0,7)
Freibord_mittel ≈ 0,06 × LOA + 0,5 [m]
Brückendeckhöhe ≈ 0,05 × LOA + 0,4 [m]
```

### 33.3 Strömungskraft-Berechnung

```
F_strom = 0,5 × ρ_wasser × v² × A_unterwasser × C_d_unterwasser

ρ_wasser = 1.025 kg/m³ (Salzwasser)
v = Strömungsgeschwindigkeit [m/s] (1 kn = 0,5144 m/s)
A_unterwasser = Lateralfläche unter Wasser [m²]
C_d_unterwasser = 0,8–1,2
```

**Wichtig:** Bei 1 kn Querstrom ist die Wasserkraft ca. 800× stärker als die Windkraft bei 1 kn Wind (Dichte Wasser >> Dichte Luft). Daher ist Querstrom der kritischste Faktor.

### 33.4 Gesamt-Schubkraft-Berechnung

```
F_erforderlich = (F_wind + F_strom) × Sicherheitsfaktor / cos(Anstellwinkel)

Sicherheitsfaktor: 1,3 (Standardmanöver), 1,5 (schwierige Bedingungen), 2,0 (Charter/Anfänger)
Anstellwinkel: 0° (Thruster wirkt rein quer) → cos(0°) = 1,0
```

### 33.5 Batterie-Dimensionierung

```
Kapazität_min [Ah] = (Strom [A] × Betriebszeit_gesamt [min]) / (60 × DoD × Effizienz)

DoD = maximale Entladetiefe:
  - AGM: 0,50
  - Lithium: 0,80
Effizienz:
  - AGM: 0,85
  - Lithium: 0,95
Betriebszeit_gesamt = Anzahl_Manöver × Zeit_pro_Manöver [min]
```

**Beispiel:**
- Thruster: 200A, 4 Manöver à 2 min = 8 min gesamt
- AGM: (200 × 8) / (60 × 0,50 × 0,85) = 63 Ah → Empfehlung: 100 Ah AGM
- Lithium: (200 × 8) / (60 × 0,80 × 0,95) = 35 Ah → Empfehlung: 50 Ah LiFePO4

---

## 34. ANHANG H: Spannungsabfall-Tabellen

### 34.1 Spannungsabfall pro Meter Kabel (Hin + Rückleitung)

**12V-System (max. 3% Verlust = 0,36V):**

| Strom [A] | 25mm² [mV/m] | 35mm² [mV/m] | 50mm² [mV/m] | 70mm² [mV/m] | 95mm² [mV/m] | 120mm² [mV/m] |
|-----------|-------------|-------------|-------------|-------------|-------------|--------------|
| 80 | 114 | 81 | 57 | 41 | 30 | 24 |
| 120 | 171 | 122 | 86 | 61 | 45 | 36 |
| 160 | 228 | 163 | 114 | 81 | 60 | 47 |
| 200 | 285 | 204 | 143 | 102 | 75 | 59 |
| 250 | 357 | 255 | 179 | 127 | 94 | 74 |
| 300 | 428 | 306 | 214 | 153 | 113 | 89 |
| 400 | 571 | 408 | 286 | 204 | 150 | 119 |

**24V-System (max. 3% Verlust = 0,72V):**

| Strom [A] | 25mm² [mV/m] | 35mm² [mV/m] | 50mm² [mV/m] | 70mm² [mV/m] | 95mm² [mV/m] | 120mm² [mV/m] |
|-----------|-------------|-------------|-------------|-------------|-------------|--------------|
| 60 | 86 | 61 | 43 | 31 | 23 | 18 |
| 100 | 143 | 102 | 71 | 51 | 38 | 30 |
| 150 | 214 | 153 | 107 | 77 | 56 | 45 |
| 200 | 285 | 204 | 143 | 102 | 75 | 59 |
| 300 | 428 | 306 | 214 | 153 | 113 | 89 |
| 400 | 571 | 408 | 286 | 204 | 150 | 119 |
| 500 | 714 | 510 | 357 | 255 | 188 | 149 |

### 34.2 Maximale Kabellänge für 3% Spannungsabfall

**12V-System:**

| Strom [A] | 35mm² [m] | 50mm² [m] | 70mm² [m] | 95mm² [m] | 120mm² [m] |
|-----------|----------|----------|----------|----------|-----------|
| 80 | 4,4 | 6,3 | 8,8 | 12,0 | 15,0 |
| 120 | 3,0 | 4,2 | 5,9 | 8,0 | 10,0 |
| 160 | 2,2 | 3,2 | 4,4 | 6,0 | 7,7 |
| 200 | 1,8 | 2,5 | 3,5 | 4,8 | 6,1 |
| 250 | 1,4 | 2,0 | 2,8 | 3,8 | 4,9 |
| 300 | 1,2 | 1,7 | 2,4 | 3,2 | 4,0 |
| 400 | 0,9 | 1,3 | 1,8 | 2,4 | 3,0 |

**24V-System:**

| Strom [A] | 35mm² [m] | 50mm² [m] | 70mm² [m] | 95mm² [m] | 120mm² [m] |
|-----------|----------|----------|----------|----------|-----------|
| 60 | 11,8 | 16,7 | 23,2 | 31,3 | 40,0 |
| 100 | 7,1 | 10,1 | 14,1 | 18,9 | 24,0 |
| 150 | 4,7 | 6,7 | 9,4 | 12,9 | 16,0 |
| 200 | 3,5 | 5,0 | 7,1 | 9,6 | 12,0 |
| 300 | 2,4 | 3,4 | 4,7 | 6,4 | 8,0 |
| 400 | 1,8 | 2,5 | 3,5 | 4,8 | 6,0 |
| 500 | 1,4 | 2,0 | 2,8 | 3,8 | 4,8 |

---

## 35. ANHANG I: Akustik und Geräuschminderung

### 35.1 Geräuschquellen bei Thrustern

| Geräuschquelle | Frequenzbereich [Hz] | Lautstärke-Anteil | Minderungsmöglichkeit |
|----------------|---------------------|-------------------|----------------------|
| Propeller-Kavitation | 500–4.000 | 30% | Größerer Tunnel, weniger Drehzahl |
| Wasserströmung im Tunnel | 200–2.000 | 25% | Glatte Tunnelwand, abgerundete Kanten |
| Motor-Vibrationen | 50–500 | 20% | Schwingungsdämpfer, Entkopplung |
| Getriebe-Geräusche | 200–1.500 | 15% | Hochwertige Zahnräder, Getriebefett |
| Strukturschall (Rumpf) | 100–1.000 | 10% | Entkopplung Tunnel-Rumpf, Dämmung |

### 35.2 Geräuschminderungsmaßnahmen

**Passive Maßnahmen:**
1. **Schwingungsdämpfer:** Gummi-Metallelemente zwischen Motor und Tunnelrohr → -3 bis -6 dB
2. **Schalldämmung Vorschiffskabine:** Akustikschaumstoff an Wänden/Decke → -5 bis -10 dB
3. **Entkopplung Tunnelrohr:** Elastisches Laminat-Interface → -2 bis -4 dB
4. **Strömungsoptimiertes Gitter:** Reduziert Turbulenzen → -1 bis -2 dB
5. **Größerer Tunnel-Ø:** Niedrigere Wassergeschwindigkeit → -2 bis -5 dB

**Aktive Maßnahmen:**
1. **Proportionalsteuerung:** Reduzierter Schub = weniger Lärm
2. **Side-Power Silence Mode:** -8 bis -12 dB (bei reduziertem Schub)
3. **Hydraulischer Antrieb:** -10 bis -15 dB gegenüber elektrisch

### 35.3 Marina-Rücksichtnahme

In vielen europäischen Marinas gibt es Nachtruhe-Regelungen (typisch 22:00–07:00). Thruster-Geräusche können in engen Marinas die Nachbarboote erheblich stören.

**Empfehlungen:**
- Nachts: wenn möglich, ohne Thruster anlegen oder Silence Mode nutzen
- Morgens früh auslaufen: Thruster-Einsatz auf Minimum beschränken
- Hydraulische Thruster sind deutlich leiser — für Marina-Dauerleger zu bevorzugen
- Vorschiffskabine dämmen — schützt eigene Schlafqualität bei Nachbar-Thrustern

---

## 36. ANHANG J: Versicherung und Haftung

### 36.1 Versicherungsrelevanz

**Kaskoversicherung:**
- Professioneller Einbau: vollständig gedeckt
- Eigeneinbau: je nach Police → vorher bei Versicherung anfragen
- Schäden durch fehlerhaften Einbau (Wassereinbruch): ggf. Leistungsverweigerung
- Empfehlung: Einbau-Bescheinigung der Werft aufbewahren

**Haftpflichtversicherung:**
- Versagen des Thrusters bei Hafenmanöver → Kollision → Haftpflichtfall
- Thruster-Versagen ist kein Ausschlussgrund (technischer Defekt)
- Vorsätzlicher Betrieb trotz bekanntem Defekt → problematisch

### 36.2 Garantie-Bedingungen der Hersteller

| Hersteller | Standard-Garantie | Erweiterte Garantie | Bedingungen |
|------------|-------------------|---------------------|-------------|
| Vetus | 5 Jahre | — | Registrierung, professioneller Einbau |
| Side-Power | 5 Jahre | 7 Jahre | Registrierung + jährl. Wartung (für +2 Jahre) |
| Lewmar | 3 Jahre | — | Registrierung empfohlen |
| Max Power | 2 Jahre | — | Rechnung als Nachweis |
| Quick | 3 Jahre | 5 Jahre | Registrierung + professioneller Einbau |

**Garantie-Ausschlüsse (alle Hersteller):**
- Verschleißteile (Kohlebürsten, Anoden, Propeller, Simmerring)
- Fehlerhafter Einbau (zu dünne Kabel, falsche Sicherung)
- Überschreitung des Duty Cycle (wenn nachweisbar)
- Korrosionsschäden durch fehlende Anoden
- Streustrom-Schäden
- Eingriffe durch nicht-autorisierte Werkstätten

---

## 37. ANHANG K: Checkliste für Thruster-Kauf und -Einbau

### 37.1 Vor dem Kauf

- [ ] Bootslänge, Verdrängung und Typ bestimmt
- [ ] Windverhältnisse im Heimatrevier bewertet (typisch/maximal)
- [ ] Empfohlene Schubkraft nach Tabelle bestimmt (Abschnitt 9.2)
- [ ] 12V oder 24V entschieden (Bordnetz prüfen)
- [ ] Tunnel-Thruster, Retractable oder External gewählt
- [ ] Platz im Bug für Tunnelrohr und Motor geprüft
- [ ] Kabellänge Batterie → Bug gemessen
- [ ] Budget festgelegt (Thruster + Einbau + Elektrik + Batterie)
- [ ] Hersteller/Modell ausgewählt (Vergleich Abschnitt 20)
- [ ] Nachrüstung: Werft kontaktiert, Termin vereinbart

### 37.2 Während des Einbaus

- [ ] Boot sicher aufgebockt/geslippt
- [ ] Tunnelposition markiert (innen + außen)
- [ ] Wasserlinie bei leichtester Beladung berücksichtigt
- [ ] Rumpf-Durchbruch sauber ausgeführt
- [ ] Kernverstärkung bei Sandwich-Laminat durchgeführt
- [ ] Tunnelrohr einlaminiert (min. 3 Lagen Biaxial 600g/m²)
- [ ] Motoreinheit montiert, Ausrichtung geprüft
- [ ] Propeller montiert, Spalt zum Tunnel geprüft
- [ ] Gitter beidseitig montiert
- [ ] Anoden montiert

### 37.3 Elektrische Installation

- [ ] Dedizierte Thruster-Batterie eingebaut
- [ ] Kabelquerschnitt berechnet und korrekt gewählt
- [ ] Kabel verlegt, befestigt, durch Schotten geführt (Gummitüllen)
- [ ] Kabelschuhe hydraulisch verpresst (nicht gelötet!)
- [ ] Hauptsicherung innerhalb 200mm von Batterie installiert
- [ ] Solenoid montiert (trocken, vibrationsfrei)
- [ ] Bedienpanel montiert und angeschlossen
- [ ] Trennrelais/Ladegerät für Thruster-Batterie installiert
- [ ] Plus- und Minus-Kabel zusammen verlegt

### 37.4 Inbetriebnahme

- [ ] Alle Verbindungen auf festen Sitz geprüft
- [ ] Batterie voll geladen
- [ ] Funktionstest: beide Richtungen
- [ ] Spannung unter Last gemessen (am Motor)
- [ ] Strom gemessen (Zangenamperemeter)
- [ ] Thermoschutz getestet (wenn möglich)
- [ ] Geräusche normal
- [ ] Keine Vibrationen
- [ ] Kein Wassereinbruch
- [ ] Bedienpanel-Funktionen geprüft
- [ ] Einbau-Dokumentation erstellt (Fotos, Messwerte)

### 37.5 Nach Inbetriebnahme

- [ ] Erste 5 Betriebsstunden: engmaschige Kontrolle
- [ ] Nach 50 Betriebsstunden: Schrauben nachziehen
- [ ] Jährlich: Anoden, Bewuchs, Antifouling
- [ ] Alle 3–5 Jahre: Simmerring, Lager, Kohlebürsten
- [ ] Logbuch führen: Betriebsstunden, Wartung, Anodenwechsel

---

## 38. ANHANG L: FAQ (Erweitert)

### FAQ 26: Kann ich den gleichen Tunnel für einen stärkeren Thruster nutzen?

**Antwort:** Ja, solange der neue Thruster denselben Tunnel-Durchmesser verwendet. Viele Hersteller bieten verschiedene Leistungsstufen für den gleichen Tunnel-Ø an. Beispiel: Vetus BOW55 und BOW75 passen beide in ein 150mm-Tunnelrohr. Ein Upgrade ist daher oft möglich, ohne das Tunnelrohr zu wechseln.

### FAQ 27: Wie oft muss das Getriebeöl gewechselt werden?

**Antwort:** Die meisten Hersteller empfehlen einen Ölwechsel alle 2 Jahre oder alle 200 Betriebsstunden. In der Praxis reicht bei geringer Nutzung (Freizeitboot) ein Wechsel alle 3 Jahre. Öl-Typ: SAE 80W-90 GL4/GL5 (marine grade). Menge: 80–350 ml je nach Modell (siehe Abschnitt 31.1).

### FAQ 28: Mein Boot hat einen Aluminium-Rumpf — worauf muss ich achten?

**Antwort:** Aluminium-Rümpfe erfordern besondere Vorsicht:
1. Tunnelrohr: nur Aluminium 5083/5086, WIG-geschweißt
2. Propeller: nur Kunststoff (kein Bronze — galvanische Korrosion!)
3. Anoden: Aluminium oder Zink (kein Magnesium)
4. Antifouling: kupferfrei
5. Elektrische Isolation: Motor-Gehäuse vom Tunnelrohr isolieren
6. Galvanischer Isolator im Landstromkabel zwingend

### FAQ 29: Was ist der Unterschied zwischen einem Thruster und einem Joystick-Manöversystem?

**Antwort:** Ein Thruster ist ein separater Querschub-Antrieb. Ein Joystick-Manöversystem (z.B. Volvo Penta IPS Joystick, Mercury JPO) nutzt die Hauptantriebe (Pod-Antriebe oder Wellenleitungen) zusammen mit optionalen Thrustern für eine koordinierte Steuerung. Das Joystick-System macht den Thruster nicht überflüssig — es integriert ihn in ein Gesamtkonzept.

### FAQ 30: Gibt es Solarmodule, die den Thruster direkt speisen können?

**Antwort:** Nein, der Thruster zieht 80–500A bei 12/24V — das sind 1–12 kW. Ein typisches Boot-Solarmodul liefert 100–400W. Die Solaranlage kann aber die Thruster-Batterie zwischen den Einsätzen aufladen. Für 4 Manöver à 1 Minute bei 200A (12V) werden ca. 13 Ah benötigt — ein 200W-Solarpanel liefert das in ca. 1 Stunde Sonne.

---

## 39. ANHANG M: Historische Entwicklung von Strahlrudern

### 39.1 Zeitleiste

| Zeitraum | Entwicklung |
|----------|------------|
| 1870er | Erste Querschub-Konzepte in der Großschifffahrt (Dampfschiffe) |
| 1920er | Elektrische Bugstrahlruder auf Passagierschiffen |
| 1950er | Hydraulische Thruster in der kommerziellen Schifffahrt etabliert |
| 1960er | Erste Thruster für größere Yachten (>25m), hydraulisch |
| 1970er | Vetus beginnt mit elektrischen Thrustern für Sportboote |
| 1980er | Tunnel-Thruster werden Standard bei Motoryachten >12m |
| 1985 | Side-Power/Sleipner steigt in den Thruster-Markt ein |
| 1990er | Elektrische 12V-Thruster für Boote ab 8m verfügbar |
| 1992 | Max Power gegründet — preiswerte italienische Thruster |
| 1995 | Proportionalsteuerung eingeführt (Side-Power) |
| 2000er | 24V-Systeme werden Standard ab 12m |
| 2005 | Retractable Thruster marktreif (ABT, Side-Power) |
| 2008 | Vetus BOW PRO — erster externer Nachrüst-Thruster |
| 2010er | NMEA 2000-Integration, CAN-Bus-Steuerung |
| 2012 | Quick steigt ein — bürstenlose Motoren |
| 2015 | Doppelpropeller-Systeme (Side-Power Dual Prop) |
| 2018 | Lithium-Batterien als Thruster-Energiequelle etabliert |
| 2020 | Funk-Fernbedienungen bei allen großen Herstellern |
| 2022 | Side-Power Silence Mode — Geräuschreduktion |
| 2024 | Joystick-Integration für kombinierte BSR+HSR-Steuerung Standard |
| 2025 | Smart-Thruster mit App-Steuerung und Betriebsdatenanalyse |

### 39.2 Marktentwicklung

| Jahr | Geschätzter Weltmarkt [Mio. EUR] | Haupttrend |
|------|--------------------------------|-----------|
| 2000 | 80 | Elektrifizierung 12V |
| 2005 | 120 | 24V-Systeme |
| 2010 | 180 | Nachrüstmarkt wächst |
| 2015 | 250 | Retractable + Premium-Segment |
| 2020 | 320 | Smart-Integration, Lithium |
| 2025 | 420 | Standardausrüstung ab 9m, Dual-Systeme |

---

## 40. ANHANG N: Umrechnungstabellen

### 40.1 Schubkraft-Umrechnung

| kgf | lbf | Newton (N) | daN |
|-----|-----|-----------|-----|
| 10 | 22 | 98 | 9,8 |
| 20 | 44 | 196 | 19,6 |
| 30 | 66 | 294 | 29,4 |
| 40 | 88 | 392 | 39,2 |
| 50 | 110 | 491 | 49,1 |
| 60 | 132 | 589 | 58,9 |
| 75 | 165 | 736 | 73,6 |
| 80 | 176 | 785 | 78,5 |
| 95 | 209 | 932 | 93,2 |
| 100 | 220 | 981 | 98,1 |
| 120 | 265 | 1.177 | 117,7 |
| 125 | 276 | 1.226 | 122,6 |
| 150 | 331 | 1.472 | 147,2 |
| 160 | 353 | 1.570 | 157,0 |
| 185 | 408 | 1.815 | 181,5 |
| 200 | 441 | 1.962 | 196,2 |
| 230 | 507 | 2.256 | 225,6 |
| 250 | 551 | 2.452 | 245,3 |
| 285 | 628 | 2.796 | 279,6 |
| 300 | 661 | 2.943 | 294,3 |
| 340 | 750 | 3.335 | 333,5 |
| 400 | 882 | 3.924 | 392,4 |
| 500 | 1.102 | 4.905 | 490,5 |

### 40.2 Tunnel-Durchmesser Metrisch/Zoll

| mm | Zoll (Inch) | Handelsbezeichnung |
|----|------------|-------------------|
| 110 | 4,33" | 4-1/3" |
| 125 | 4,92" | 5" |
| 150 | 5,91" | 6" |
| 160 | 6,30" | 6-1/4" |
| 185 | 7,28" | 7-1/4" |
| 200 | 7,87" | 8" |
| 250 | 9,84" | 10" |
| 300 | 11,81" | 12" |

### 40.3 Windgeschwindigkeit-Umrechnung

| Beaufort | kn | m/s | km/h | Bezeichnung |
|----------|-----|-----|------|-------------|
| 0 | 0 | 0 | 0 | Windstille |
| 1 | 1–3 | 0,3–1,5 | 1–5 | Leiser Zug |
| 2 | 4–6 | 1,6–3,3 | 6–11 | Leichte Brise |
| 3 | 7–10 | 3,4–5,4 | 12–19 | Schwache Brise |
| 4 | 11–15 | 5,5–7,9 | 20–28 | Mäßige Brise |
| 5 | 16–21 | 8,0–10,7 | 29–38 | Frische Brise |
| 6 | 22–27 | 10,8–13,8 | 39–49 | Starker Wind |
| 7 | 28–33 | 13,9–17,1 | 50–61 | Steifer Wind |
| 8 | 34–40 | 17,2–20,7 | 62–74 | Stürmischer Wind |

---

## 41. ANHANG O: Typische Defekt-Statistiken und Ausfallraten

### 41.1 Statistische Ausfallraten nach Komponente

Basierend auf aggregierten Servicedaten von europäischen Marinewerkstätten (2018–2025):

| Komponente | Ausfallrate [%/Jahr] | Mittlere Lebensdauer | Häufigste Ursache |
|------------|---------------------|---------------------|-------------------|
| Kohlebürsten | 8–12% | 300–600 Betriebsstunden | Normaler Verschleiß |
| Solenoid | 5–8% | 4–7 Jahre | Kontaktabbrand |
| Wellendichtring | 4–7% | 3–5 Jahre | Alterung, Verhärtung |
| Kugellager | 3–5% | 5–8 Jahre | Korrosion, Verschleiß |
| Propeller (Kunststoff) | 3–6% | 4–8 Jahre | Rissbildung, Fremdkörper |
| Propeller (Bronze) | 1–2% | 10–20 Jahre | Korrosion, Beschädigung |
| Getriebe | 2–4% | 6–10 Jahre | Ölmangel, Verschleiß |
| Motor-Wicklung | 1–3% | 8–15 Jahre | Überhitzung, Feuchtigkeit |
| Bedienpanel | 2–4% | 5–10 Jahre | Feuchtigkeit, UV-Schaden |
| Kabelschuhe/Verbindungen | 3–6% | 5–10 Jahre | Korrosion |
| Tunnelrohr (GFK) | <1% | 20+ Jahre | Osmose, mechanisch |
| Tunnelrohr (Alu) | 2–5% | 10–20 Jahre | Galvanische Korrosion |
| Anoden | 100% (Verschleißteil) | 12–24 Monate | Aufgelöst (planmäßig) |

### 41.2 Ausfälle nach Betriebsalter

| Betriebsalter | Typische Ausfälle | Kosten-Erwartung [EUR/Jahr] |
|--------------|-------------------|---------------------------|
| 0–2 Jahre | Installationsfehler (Kabel, Sicherung) | 50–200 (Garantie) |
| 2–5 Jahre | Kohlebürsten, Anoden, ggf. Solenoid | 100–300 |
| 5–8 Jahre | Simmerring, Lager, Kohlebürsten, Solenoid | 200–500 |
| 8–12 Jahre | Motor-Grundüberholung oder Tausch, Getriebe | 500–1.500 |
| 12–15 Jahre | Kompletter Thruster-Tausch oft wirtschaftlicher | 1.500–4.000 |
| >15 Jahre | Ersatzteil-Verfügbarkeit kritisch | Neukauf empfohlen |

### 41.3 Kostenvergleich: Wartung vs. Austausch

**Beispiel: Vetus BOW75, Baujahr 2014, 350 Betriebsstunden:**

| Option | Maßnahmen | Kosten [EUR] | Restlebensdauer |
|--------|-----------|-------------|-----------------|
| Grundüberholung | Motor überh., Lager, Dichtung, Bürsten, Solenoid | 850–1.200 | 5–8 Jahre |
| Motor-Tausch (Ersatzteil) | Neuer Motor, bestehendes Getriebe/Tunnel | 1.200–1.800 | 8–12 Jahre |
| Kompletter Neueinbau | Vetus BOW75 neu + Einbau | 3.500–4.500 | 12–15 Jahre |
| Upgrade | Vetus BOW95 (mehr Schub), neuer Tunnel 185mm | 5.500–7.000 | 12–15 Jahre |

**Entscheidungsregel:**
- Reparaturkosten < 40% Neupreis → Reparieren
- Reparaturkosten 40–65% Neupreis → Reparieren nur wenn Thruster <8 Jahre
- Reparaturkosten > 65% Neupreis → Neukauf (ggf. mit Upgrade)

---

## 42. ANHANG P: Manövertechniken mit Bugstrahlruder

### 42.1 Grundlegende Manöver

**Manöver 1: Seitwärts an die Pier (Backbord-Anleger, Seitenwind von Steuerbord)**
1. Parallel zur Pier positionieren, Abstand 1–2m
2. Boot stoppen (kein Vor- oder Rückwärtsfahrt)
3. BSR nach Backbord → Bug bewegt sich Richtung Pier
4. Heckpropeller kurz voraus + Ruder Richtung Pier → Heck folgt
5. Alternativ bei BSR+HSR: beide gleichzeitig → Seitwärtsfahrt (Crabbing)
6. Leinen befestigen

**Manöver 2: Drehen auf der Stelle (enger Hafen)**
1. Boot stoppen
2. BSR nach Steuerbord + Hauptantrieb voraus + Ruder Steuerbord
3. Boot dreht sich um den Drehpunkt
4. BSR nach Bedarf korrigieren
5. Drehung auf der Stelle in ca. 1,5× Bootslänge möglich

**Manöver 3: Rückwärts in die Box (Marina-Standardmanöver Mittelmeer)**
1. Parallel zur Boxengasse, langsam rückwärts
2. Heck zeigt zur Box
3. BSR korrigiert den Bug gegen Seitenwind
4. Hauptantrieb rückwärts → Boot gleitet in die Box
5. BSR-Korrekturen in kurzen Stößen (2–3 Sekunden)
6. Muringleine aufnehmen, Heckleinen befestigen

**Manöver 4: Vorwärts in die Box (Mitteleuropa/Skandinavien)**
1. Gasse vor der Box anfahren, langsam voraus
2. BSR dreht Bug in Richtung Box
3. Vorsichtig voraus in die Box
4. BSR-Korrektur gegen Abdrift
5. Leinen befestigen, Fender kontrollieren

### 42.2 Fortgeschrittene Manöver

**Crabbing (echte Seitwärtsfahrt mit BSR + HSR):**
- Voraussetzung: Bug- UND Heckstrahlruder
- BSR + HSR in gleiche Richtung → Boot fährt seitwärts
- Kein Hauptantrieb nötig
- Perfekt für enge Boxen, seitliches Anlegen an Tanksteg
- Geschwindigkeit: ca. 0,3–0,5 kn seitlich

**Wind-Kompensation bei langer Zufahrt:**
- BSR in kurzen Intervallen gegen Windabdrift
- Nicht dauerhaft betätigen (Duty Cycle!)
- Besser: Hauptantrieb + Ruder für grobe Korrektur, BSR für Feinkorrektur
- Rhythmus: 3s BSR → 10s Pause → 3s BSR

**Notmanöver: Kollisionsvermeidung im Hafen:**
- BSR voll in eine Richtung → schnelle Bugauslenkung
- Gleichzeitig Hauptantrieb auskuppeln oder rückwärts
- BSR kann Kollisionswinkel entschärfen (Streifschuss statt Frontal)
- Reaktionszeit BSR: 0,5–1,0 Sekunden (elektrisch), 1,5–3,0 Sekunden (hydraulisch)

### 42.3 Häufige Anfängerfehler

| Fehler | Problem | Lösung |
|--------|---------|--------|
| BSR dauerhaft betätigen | Duty Cycle überschritten, Motor überhitzt | Kurze Stöße, 2–5 Sekunden |
| BSR bei >3 kn Fahrt | Wirkungslos, Wasser strömt vorbei | Erst Boot stoppen, dann BSR |
| BSR zu spät einsetzen | Boot schon zu nah an Hindernis | Vorausschauend planen, BSR früh nutzen |
| Nur BSR ohne Hauptantrieb | Nur Bug bewegt sich, Heck driftet | BSR + Hauptantrieb kombinieren |
| Falscher Richtungssinn | Bug bewegt sich in falsche Richtung | Orientierung merken: Joystick links = Bug geht nach Backbord |
| BSR bei Vorwärtsfahrt | Verwirrung: Bug geht entgegen erwartet | Bei Fahrt arbeitet Ruder effektiver als BSR |
| Panik-Reaktion | BSR voll und dauerhaft | Ruhig bleiben, kurze kontrollierte Stöße |

### 42.4 Training und Übung

**Empfohlener Trainingsplan für neue BSR-Eigner:**

| Übung | Ort | Dauer | Ziel |
|-------|-----|-------|------|
| 1. Richtungssinn lernen | Offenes Wasser, kein Wind | 15 min | BSR links/rechts sicher bedienen |
| 2. Drehen auf der Stelle | Offenes Wasser | 20 min | 360° Drehung in <2 Bootslängen |
| 3. Seitwärts-Versatz | An Boje/Steg, windstill | 20 min | Kontrolliertes seitliches Bewegen |
| 4. Anlegen mit Seitenwind | Leerer Steg, 10 kn Wind | 30 min | Wind kompensieren mit BSR |
| 5. Rückwärts in Box | Leere Marina, windstill | 30 min | Kontrolliert rückwärts einparken |
| 6. Rückwärts in Box mit Wind | Marina, Seitenwind | 30 min | Realbedingung |
| 7. Crabbing (mit HSR) | Offenes Wasser | 15 min | Seitwärtsfahrt kontrollieren |

---

## 43. ANHANG Q: Moderne Thruster-Technologien und Ausblick

### 43.1 Bürstenlose DC-Motoren (BLDC)

Die neueste Generation von Thrustern (Quick BTDC ab 2020, Side-Power ab 2023) verwendet bürstenlose Gleichstrommotoren:

**Vorteile gegenüber Bürstenmotoren:**
- Keine Kohlebürsten → kein Kohlebürsten-Verschleiß → wartungsärmer
- Höherer Wirkungsgrad (+10–15%)
- Längere Lebensdauer (2–3× länger als Bürstenmotor)
- Weniger Wärmeentwicklung → höherer Duty Cycle möglich
- Leiser im Betrieb
- Keine Funkenbildung (explosionsgeschützter Betrieb möglich)

**Nachteile:**
- Höherer Preis (+20–30% gegenüber Bürstenmotor)
- Komplexerer Controller (elektronische Kommutierung)
- Reparatur nur beim Hersteller (keine einfache Kohlebürsten-Erneuerung)
- Bei Controller-Defekt: kompletter Ausfall

### 43.2 Lithium-Integration

Moderne Thruster-Systeme werden zunehmend mit Lithium-Batterien kombiniert:

**LiFePO4 Vorteile für Thruster:**
- Konstante Spannung → konstanter Schub bis zur Entladung
- Schnellladefähig (1C möglich) → schnelle Wiederherstellung nach Manöver
- 50% leichter → im Bug weniger Gewicht (besser für Trimm)
- 3.000–5.000 Zyklen → 10× AGM-Lebensdauer bei Thruster-Nutzung
- BMS schützt vor Tiefentladung automatisch

**Herausforderungen:**
- BMS muss hohe Stromspitzen tolerieren (300–500A für Millisekunden)
- Nicht alle BMS schalten bei Thruster-Anlaufstrom nicht ab
- Empfohlene BMS: Victron Smart BMS, Mastervolt MLI, Lithionics
- Temperatur: unter 0°C keine Ladung möglich (BMS-Sperre)

### 43.3 Smart-Thruster und IoT

Ab 2024 bieten mehrere Hersteller „Smart-Thruster" mit digitaler Anbindung:

| Feature | Side-Power | Vetus | Quick |
|---------|-----------|-------|-------|
| NMEA 2000 Integration | Ja (EMMA) | Ja (V-CAN Bridge) | Ja (T-Link) |
| App-Steuerung (Bluetooth) | In Entwicklung | Ja (ab 2025) | Ja (ab 2024) |
| Betriebsstunden-Zähler | Ja | Ja | Ja |
| Duty-Cycle-Monitoring | Ja | Ja | Ja |
| Motor-Temperatur live | Ja | Ja | Ja |
| Batterie-Monitoring | Ja | Ja | Ja |
| Wartungs-Erinnerung | Ja | In Entwicklung | Ja |
| Remote-Diagnose | In Entwicklung | Nein | In Entwicklung |
| OTA-Firmware-Update | Nein | Nein | In Entwicklung |

### 43.4 Elektrische Podantriebe als Alternative

Elektrische Gondel-Antriebe (z.B. Torqeedo Pod) können als Alternative zu traditionellen Bugstrahlrudern betrachtet werden:

| Merkmal | Traditioneller BSR | Elektrischer Pod (Bug) |
|---------|-------------------|----------------------|
| Schub quer | Ja (primär) | Ja (360° schwenkbar) |
| Schub voraus/achteraus | Nein | Ja (vielseitiger) |
| Tunnel nötig | Ja | Nein (extern montiert) |
| Widerstand | Tunnel-Widerstand | Gondel-Widerstand |
| Komplexität | Gering | Höher (Schwenkmechanik) |
| Preis | Standard | 2–3× höher |
| Verfügbarkeit | Alle Hersteller | Wenige Anbieter |
| Marktreife | 50+ Jahre | Neu (2022+) |

### 43.5 Zukunftsprognosen

**Kurzfristig (2025–2027):**
- Bürstenlose Motoren werden Standard (alle Hersteller)
- NMEA 2000 Integration bei allen Modellen ab mittlerer Klasse
- Lithium-Batterien als empfohlene Thruster-Batterie
- Erweiterte Duty Cycles durch bessere Motorentechnologie

**Mittelfristig (2027–2030):**
- App-basierte Steuerung und Diagnose Standard
- Integration in autonome Anlegeassistenten (GPS + Thruster + Hauptantrieb)
- Predictive Maintenance über Cloud-Analyse
- Geräuschpegel deutlich reduziert durch BLDC + optimierte Tunnelgeometrie

**Langfristig (2030+):**
- Vollautomatisches Anlegen bei Serienbooten >12m
- Rim-Drive-Thruster (Propeller ohne zentrale Welle, Antrieb am Tunnelrand)
- Integration in vollständige elektrische Antriebssysteme
- Recycelbare Materialien für Tunnelrohre und Motorgehäuse

---

## 44. ANHANG R: Erfahrungsberichte aus Foren und Fachzeitschriften

### 44.1 Forum-Konsens (zusammengefasst)

**Thema: „Welcher Bugstrahlruder für Bavaria 40 Cruiser?"**
- Konsens: Vetus BOW55 oder Side-Power SE60 (150mm Tunnel, 12V)
- Häufiger Hinweis: „Nimm den nächstgrößeren — 55 kgf knapp bei Wind"
- Alternative: Side-Power SE80 (160mm Tunnel) wenn Budget vorhanden
- Eigeneinbau: „Kabeldurchführung ist das Schwierigste, Tunnel-Einbau Werft machen lassen"

**Thema: „Heckstrahlruder — braucht man das wirklich?"**
- Konsens: Unter 14m Segelyacht: nein. Motoryacht mit Flybridge ab 14m: ja, empfehlenswert
- Häufiger Hinweis: „Einmal Crabbing gehabt, willst du nie mehr ohne"
- Kostenbewertung: „8.000 EUR für BSR+HSR, aber der erste verhinderte Rammschaden zahlt das"

**Thema: „Vetus oder Side-Power — was ist besser?"**
- Kein eindeutiger Konsens — beide gut bewertet
- Vetus: „Bessere Ersatzteilversorgung in Deutschland, günstiger"
- Side-Power: „Leiser, robuster, längere Garantie — aber teurer"
- Max Power: „Wird als Budget-Tipp empfohlen, Qualität aber durchaus akzeptabel"

**Thema: „Lithium-Batterie für Bugstrahlruder?"**
- Geteilte Meinungen
- Pro: „Konstante Leistung, halbes Gewicht, im Bug ideal"
- Contra: „Teuer, BMS kann bei Anlaufstrom abschalten — vorher testen!"
- Konsens: „Funktioniert gut mit Victron LiFePO4 + Smart BMS CL 12/100"

### 44.2 Fachzeitschriften-Tests (zusammengefasst)

**YACHT (Deutschland), Vergleichstest 2024:**
- Getestete Modelle: Vetus BOW55, Side-Power SE60, Max Power CT60, Quick BTDC 5512
- Testsieger: Side-Power SE60 (Lautstärke, Verarbeitung)
- Preis-Leistung: Max Power CT60
- Zuverlässigkeit: Vetus BOW55 (bewährte Technik)
- Fazit: „Alle vier Modelle sind empfehlenswert — Unterschiede im Detail"

**Practical Boat Owner (UK), Retractable-Test 2023:**
- Getestete Modelle: Side-Power EX75, Lewmar RT55
- Ergebnis: Side-Power leiser, schnellere Ausfahrzeit
- Lewmar: robustere Mechanik, bessere Dichtung
- Fazit: „Retractable nur für Performance-Segler wirklich sinnvoll — Mehrkosten von 6.000+ EUR"

**Bateaux (Frankreich), BSR-Installation 2024:**
- Nachrüstung Vetus BOW PRO GO 46 auf Jeanneau Sun Odyssey 380
- Eigeneinbau dokumentiert (Schritt für Schritt)
- Ergebnis: „3 Stunden Montage, funktioniert einwandfrei"
- Einschränkung: „46 kgf ist grenzwertig bei Mistral — besser BOW PRO 57"

### 44.3 Eigner-Langzeitberichte

**Bericht 1: Vetus BOW75, 8 Jahre, 420 Betriebsstunden**
- Boot: Bavaria 42 Cruiser
- Wartung: Anoden jährlich, Kohlebürsten nach 5 Jahren, Simmerring nach 6 Jahren
- Gesamtkosten 8 Jahre: ca. 650 EUR Wartung + Ersatzteile
- Zufriedenheit: 9/10 — „Nie Probleme, zuverlässig wie ein Uhrwerk"
- Schwäche: „Bei 25+ kn Wind an der Grenze, hätte 95 kgf nehmen sollen"

**Bericht 2: Side-Power SP155, 5 Jahre, 280 Betriebsstunden**
- Boot: Princess 50, Charterbetrieb
- Wartung: Anoden 2× jährlich (Charterbetrieb = mehr Nutzung)
- Keine Ausfälle in 5 Jahren
- Zufriedenheit: 10/10 — „Chartergäste lieben es — kein einziger Schaden seit Einbau"

**Bericht 3: Max Power CT60, 6 Jahre, 350 Betriebsstunden**
- Boot: Beneteau Oceanis 38.1
- Problem nach 4 Jahren: Solenoid defekt → selbst getauscht (45 min, 95 EUR)
- Problem nach 5 Jahren: Propeller gerissen → selbst getauscht (15 min, 55 EUR)
- Zufriedenheit: 7/10 — „Für den Preis OK, aber Side-Power wäre langlebiger gewesen"

**Bericht 4: Vetus BOW PRO GO 46, 3 Jahre, 150 Betriebsstunden**
- Boot: Dufour 360
- Eigeneinbau, keine Werft nötig
- Zufriedenheit: 8/10 — „Perfekt für Gelegenheitssegler, klappbar ist super"
- Schwäche: „Unter Segeln eingeklappt, aber trotzdem sichtbar — optisch nicht ideal"

---

## 45. ANHANG S: Regionale Besonderheiten

### 45.1 Reviere und Thruster-Anforderungen

| Revier | Typische Bedingungen | Empfehlung |
|--------|---------------------|-----------|
| Ostsee (DE, DK, SE) | Wenig Strom, moderate Winde, enge Marinas | Standard-BSR, 100% Empfehlung |
| Nordsee (DE, NL, UK) | Starke Gezeitenströme, böiger Wind | +30% Überdimensionierung |
| Mittelmeer West (FR, IT, ES) | Mistral/Tramontana, enge Häfen, Med-Mooring | BSR + HSR für Motoryachten |
| Mittelmeer Ost (GR, HR, TR) | Meltemi, enge Stadthäfen | +20% Überdimensionierung |
| Atlantik (FR, ES, PT) | Dünung, offene Häfen, Gezeitenströme | Robuste Installation, +20% |
| Karibik | Passatwind konstant 15–25 kn, Rollankerplätze | +30%, Korrosionsschutz kritisch |
| Skandinavien (NO, SE, FI) | Enge Schären, wenig Wind in Fjorden | Standard-BSR ausreichend |
| Binnengewässer (NL, FR, DE) | Schleusen, Kanäle, kein Seegang | Hydraulisch für Dauerbetrieb |

### 45.2 Korrosions-Risikozonen

| Revier | Salzgehalt [‰] | Korrosionsrisiko | Anoden-Typ | Anoden-Wechselintervall |
|--------|----------------|-----------------|-----------|------------------------|
| Ostsee (westlich) | 8–15 | Mittel | Aluminium | 18 Monate |
| Ostsee (östlich) | 2–8 | Gering–Mittel | Aluminium | 24 Monate |
| Nordsee | 30–35 | Hoch | Zink oder Aluminium | 12 Monate |
| Mittelmeer | 36–39 | Hoch | Zink | 12 Monate |
| Atlantik | 33–37 | Hoch | Zink oder Aluminium | 12 Monate |
| Karibik | 34–37 | Sehr hoch (warm!) | Zink | 8–12 Monate |
| Binnengewässer | 0 | Gering | Magnesium | 12–18 Monate |

### 45.3 Marina-Infrastruktur und Thruster-Bedarf

| Region | Marina-Boxenbreite (typisch) | Strom verfügbar | Thruster-Bedarf |
|--------|------------------------------|-----------------|-----------------|
| Nordeuropa (DE, DK, SE) | Knapp (Boot + 30cm) | 16A/230V | Hoch |
| Niederlande | Großzügig (Boot + 50–80cm) | 16A/230V | Mittel |
| UK | Variabel | 16A/230V | Mittel–Hoch |
| Mittelmeer (FR) | Eng, Med-Mooring | 16A/230V | Sehr hoch |
| Mittelmeer (HR) | Eng, Hafenmauern | 16A/230V | Hoch |
| Mittelmeer (GR) | Oft offen, Anker + Heck | Variabel | Mittel |
| Karibik | Oft Ankerlieger, wenige Marinas | Selten | Gering |

---

## 46. ANHANG T: Thruster-Kompatibilitätsmatrix nach Bootshersteller

### 46.1 Segelyachten — Werkseitig vorbereitet

Viele Serienwerften bieten werkseitig vorbereitete Tunnel-Positionen. Bei diesen Booten ist die Nachrüstung besonders einfach, da der Rumpf bereits mit verstärktem Bereich und markierter Tunnelposition geliefert wird.

| Bootshersteller | Modell | Vorbereiteter Tunnel-Ø [mm] | Empfohlener Thruster | Ab Werk verfügbar |
|-----------------|--------|------------------------------|---------------------|-------------------|
| Bavaria | C38 | 125 | Vetus BOW45 | Ja (Option) |
| Bavaria | C42 | 150 | Vetus BOW55/75 | Ja (Option) |
| Bavaria | C46 | 150 | Vetus BOW75/95 | Ja (Option) |
| Bavaria | C50 | 185 | Vetus BOW95/125 | Ja (Option) |
| Hanse | 348 | 125 | Side-Power SE40 | Ja (Option) |
| Hanse | 388 | 150 | Side-Power SE60 | Ja (Option) |
| Hanse | 418 | 150 | Side-Power SE80 | Ja (Option) |
| Hanse | 458 | 160 | Side-Power SE80/100 | Ja (Option) |
| Hanse | 508 | 185 | Side-Power SP100 | Ja (Option) |
| Jeanneau | SO 380 | 125 | Side-Power SE40 | Ja (Option) |
| Jeanneau | SO 410 | 150 | Side-Power SE60 | Ja (Option) |
| Jeanneau | SO 440 | 150 | Side-Power SE80 | Ja (Option) |
| Jeanneau | SO 490 | 185 | Side-Power SP100 | Ja (Option) |
| Beneteau | Oc 38.1 | 125 | Quick BTDC 3512 | Ja (Option) |
| Beneteau | Oc 40.1 | 150 | Quick BTDC 5512 | Ja (Option) |
| Beneteau | Oc 46.1 | 150 | Quick BTDC 7512 | Ja (Option) |
| Beneteau | Oc 51.1 | 185 | Quick BTDC 9524 | Ja (Option) |
| Dufour | 360 | 125 | Vetus BOW35/45 | Nein (Nachrüstung) |
| Dufour | 390 | 150 | Vetus BOW55 | Ja (Option) |
| Dufour | 430 | 150 | Vetus BOW75 | Ja (Option) |
| Dufour | 470 | 160 | Vetus BOW75/95 | Ja (Option) |
| Dufour | 530 | 185 | Vetus BOW95/125 | Ja (Option) |
| Hallberg-Rassy | 340 | 125 | Side-Power SE40 | Ja (Serie ab HR412+) |
| Hallberg-Rassy | 400 | 150 | Side-Power SE60 | Ja (Option) |
| Hallberg-Rassy | 44 | 160 | Side-Power SE80 | Ja (Option) |
| Hallberg-Rassy | 50 | 185 | Side-Power SP100 | Ja (Serie) |
| Hallberg-Rassy | 57 | 250 | Side-Power SP155 | Ja (Serie) |
| Najad | 395 | 150 | Side-Power SE60 | Ja (Option) |
| Najad | 440 | 185 | Side-Power SP100 | Ja (Serie) |
| X-Yachts | X4⁰ | 150 | Side-Power SE60 | Ja (Option) |
| X-Yachts | X4⁶ | 160 | Side-Power SE80 | Ja (Option) |
| Contest | 42CS | 150 | Side-Power SE60 | Ja (Option) |
| Contest | 50CS | 185 | Side-Power SP125 | Ja (Serie) |

### 46.2 Motoryachten — Werkseinbau

| Bootshersteller | Modell | BSR Tunnel-Ø [mm] | HSR Tunnel-Ø [mm] | BSR-Modell | HSR-Modell |
|-----------------|--------|-------------------|-------------------|-----------|-----------|
| Azimut | 42 | 185 | — | Quick BTDC 9524 | — |
| Azimut | 50 | 200 | 185 | Quick BTDC 12524 | Quick BTDC 9524 |
| Azimut | 60 | 250 | 200 | Quick BTDC 16024 | Quick BTDC 12524 |
| Princess | 45 | 185 | — | Side-Power SP100 | — |
| Princess | 55 | 250 | 185 | Side-Power SP155 | Side-Power SP100 |
| Princess | 62 | 250 | 250 | Side-Power SP190 | Side-Power SP155 |
| Sunseeker | Manhattan 52 | 250 | 185 | Side-Power SP155 | Side-Power SP100 |
| Sunseeker | Manhattan 60 | 300 | 250 | Side-Power SP240 | Side-Power SP190 |
| Ferretti | 500 | 250 | 200 | Quick BTDC 16024 | Quick BTDC 12524 |
| Ferretti | 580 | 300 | 250 | Quick BTDC 28024 | Quick BTDC 21024 |
| Sealine | C390 | 160 | — | Max Power CT80 | — |
| Sealine | C530 | 200 | 160 | Max Power CT125 | Max Power CT80 |
| Nimbus | C11 | 160 | — | Side-Power SE80 | — |
| Nimbus | T11 | 160 | — | Side-Power SE100 | — |
| Linssen | GS 35.0 | 150 | — | Vetus BOW55 | — |
| Linssen | GS 40.0 | 185 | — | Vetus BOW95 | — |
| Linssen | GS 45.0 | 185 | 150 | Vetus BOW125 | Vetus BOW75 |
| Greenline | 40 | 150 | — | Vetus BOW55 | — |
| Greenline | 48 | 185 | 150 | Vetus BOW95 | Vetus BOW75 |
| Beneteau | Swift Trawler 41 | 150 | — | Quick BTDC 5512 | — |
| Beneteau | Swift Trawler 47 | 185 | — | Quick BTDC 9524 | — |
| Jeanneau | Merry Fisher 1095 | 150 | — | Side-Power SE60 | — |
| Jeanneau | NC 37 | 160 | — | Side-Power SE80 | — |

### 46.3 Katamarane — Thruster-Konfigurationen

| Bootshersteller | Modell | Konfiguration | Thruster | Gesamtschub [kgf] |
|-----------------|--------|---------------|---------|-------------------|
| Fountaine Pajot | Elba 45 | 2× Tunnel (je Rumpf) | 2× Vetus BOW55 | 110 |
| Fountaine Pajot | MY 40 | 1× Tunnel zentral | Quick BTDC 9524 | 95 |
| Lagoon | 42 | 2× Tunnel (je Rumpf) | 2× Side-Power SE40 | 80 |
| Lagoon | 50 | 2× Tunnel (je Rumpf) | 2× Side-Power SE60 | 120 |
| Leopard | 45 | 1× Tunnel (BB Rumpf) | Vetus BOW75 | 75 |
| Nautitech | 46 Open | 2× Tunnel (je Rumpf) | 2× Vetus BOW45 | 90 |
| Bali | 4.4 | 2× Tunnel (je Rumpf) | 2× Max Power CT45 | 90 |
| Bali | 4.8 | 2× Tunnel (je Rumpf) | 2× Max Power CT60 | 120 |
| Excess | 14 | 1× Tunnel (BB Rumpf) | Side-Power SE60 | 60 |
| Excess | 15 | 2× Tunnel (je Rumpf) | 2× Side-Power SE60 | 120 |

---

## 47. ANHANG U: Leistungskennlinien und Effizienz

### 47.1 Schub vs. Batteriespannung

Die Schubkraft eines elektrischen Thrusters ist direkt von der Batteriespannung abhängig. Bei sinkender Spannung (z.B. durch Entladung oder Spannungsabfall im Kabel) sinkt der Schub überproportional:

**Typische Schubkurve (12V-System, 55 kgf Nennschub):**

| Batteriespannung [V] | Relativer Schub [%] | Effektiver Schub [kgf] | Zustand |
|----------------------|---------------------|----------------------|---------|
| 13,2 | 110% | 61 | Voll geladen, frisch |
| 12,8 | 105% | 58 | Voll geladen |
| 12,6 | 100% | 55 | Nennspannung |
| 12,0 | 88% | 48 | 50% entladen (AGM) |
| 11,5 | 78% | 43 | 60% entladen (AGM) |
| 11,0 | 65% | 36 | Kritisch — Batterie laden! |
| 10,5 | 50% | 28 | Tiefentladung droht |
| 10,0 | 30% | 17 | Motor startet ggf. nicht mehr |

**Typische Schubkurve (24V-System, 125 kgf Nennschub):**

| Batteriespannung [V] | Relativer Schub [%] | Effektiver Schub [kgf] | Zustand |
|----------------------|---------------------|----------------------|---------|
| 26,4 | 110% | 138 | Voll geladen, frisch |
| 25,6 | 105% | 131 | Voll geladen |
| 25,2 | 100% | 125 | Nennspannung |
| 24,0 | 88% | 110 | 50% entladen (AGM) |
| 23,0 | 78% | 98 | 60% entladen (AGM) |
| 22,0 | 65% | 81 | Kritisch — Batterie laden! |
| 21,0 | 50% | 63 | Tiefentladung droht |

### 47.2 Wirkungsgrad-Kette

| Stufe | Wirkungsgrad | Kumuliert | Verlustquelle |
|-------|-------------|-----------|---------------|
| Batterie → Kabel | 95–97% | 95–97% | Ohmscher Widerstand, Kabelschuhe |
| Kabel → Solenoid | 98–99% | 93–96% | Kontaktwiderstand |
| Solenoid → Motor | 99% | 92–95% | Leitungsverluste |
| Motor (elektrisch → mechanisch) | 75–85% | 69–81% | Kupferverluste, Eisenverluste |
| Getriebe | 90–95% | 62–77% | Reibung, Öl-Scherung |
| Propeller (mechanisch → hydraulisch) | 45–65% | 28–50% | Schlupf, Drallverluste |
| Netto-Gesamtwirkungsgrad | — | **28–50%** | — |

**Interpretation:** Von der gespeicherten Batterieenergie erreichen nur 28–50% als nutzbarer Schub das Wasser. Dies erklärt den hohen Stromverbrauch und die Notwendigkeit großer Batterien.

### 47.3 Energiebedarf pro Manöver

| Manöver-Typ | Dauer [s] | Strom [A] (75 kgf, 12V) | Energie [Wh] | Aus Batterie [Ah] |
|-------------|-----------|--------------------------|-------------|-------------------|
| Kurze Korrektur | 3 | 260 | 2,6 | 0,22 |
| Standard-Anleger | 30 | 260 | 26 | 2,2 |
| Schwieriger Anleger | 90 | 260 | 78 | 6,5 |
| Voller Duty Cycle (3 min) | 180 | 260 | 156 | 13,0 |
| 5 Manöver pro Tag | ~5 min | 260 | 260 | 21,7 |
| Charter-Tag (10 Manöver) | ~10 min | 260 | 520 | 43,3 |

---

## 48. ANHANG V: Checkliste für AYDI-Visuelle Analyse

### 48.1 Foto-Anforderungen für Thruster-Bewertung

Für eine visuelle Analyse durch AYDI Vision sind folgende Fotos hilfreich:

| Foto | Motiv | Confidence-Beitrag | Mindest-Qualität |
|------|-------|--------------------|-----------------|
| 1 | Tunnelrohr von außen (Backbord-Seite) | visual_high | Scharf, gut belichtet, nah |
| 2 | Tunnelrohr von außen (Steuerbord-Seite) | visual_high | Scharf, gut belichtet, nah |
| 3 | Propeller durch Gitter sichtbar | visual_medium | Bedingt, abhängig von Sichtbarkeit |
| 4 | Gitter-Zustand (beidseitig) | visual_high | Scharf, Detailaufnahme |
| 5 | Anoden-Zustand | visual_high | Nah, scharf, Maßstab erkennbar |
| 6 | Motor-Einheit (innen, hinter Tunnel) | visual_medium | Beleuchtung nötig |
| 7 | Elektrische Anschlüsse (Kabelschuhe) | visual_medium | Nah, Detailaufnahme |
| 8 | Solenoid und Sicherung | visual_medium | Übersichtsaufnahme |
| 9 | Batterie (Thruster-Batterie) | visual_medium | Typenschild lesbar |
| 10 | Bedienpanel | visual_high | Frontansicht |
| 11 | Gesamtübersicht Tunnelrohr (Unterwasser) | visual_medium | Unterwasserkamera nötig |
| 12 | Typenschild des Thrusters | visual_high | Scharf, alle Daten lesbar |

### 48.2 Bewertbare Zustände per Foto

| Zustand | Per Foto erkennbar? | Typische Confidence |
|---------|--------------------|--------------------|
| Propeller-Riss/-Bruch | Ja (wenn Gitter abgebaut) | visual_high |
| Propeller-Bewuchs | Ja | visual_high |
| Tunnelrohr-Korrosion (Alu) | Ja (weiße Ablagerungen) | visual_high |
| Tunnelrohr-Osmose (GFK) | Teilweise (Blasen sichtbar) | visual_medium |
| Anoden-Verbrauch | Ja (wenn zugänglich) | visual_high |
| Gitter-Zustand | Ja | visual_high |
| Kabelschuhe-Korrosion | Ja (Grünspan, Aufblähung) | visual_medium |
| Solenoid-Kontaktabbrand | Nein (intern) | visual_insufficient |
| Motor-Wicklungsschaden | Nein (intern) | visual_insufficient |
| Lagerverschleiß | Nein (intern) | visual_insufficient |
| Bewuchs im Tunnel | Teilweise | visual_medium |
| Kabelquerschnitt | Teilweise (Beschriftung) | visual_low |
| Sicherungszustand | Ja (wenn sichtbar) | visual_medium |
| Batterie-Zustand | Teilweise (Gehäuse, Pole) | visual_medium |

---

*Ende der Wissensdatei 18_12 — Bug- und Heckstrahlruder*
*AYDI Maritime Knowledge Base v2.0 — Stand 2026-04*
