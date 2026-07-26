# 22.06 — Windgeneratoren im Yachtbau: Vollständige Wissensreferenz

> **AYDI Wissensdatei 22.06** — Kategorie 22: Elektrik und Verkabelung
> **Confidence-Quelle:** measured (Hersteller-TDS, IEC 61400-2, GL Renewable Certification), documented (Hersteller-Kataloge, Praxisberichte), estimated (Erfahrungswerte)
> **Letzte Aktualisierung:** 2026-05-05

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
11. [ANHANG A–H — Fallstudien](#anhang-a--fallstudien)
12. [ANHANG I–R — AYDI-Integration (Pydantic v2 Modelle)](#anhang-i--aydi-integration-pydantic-v2-modelle)

---

## 1. Einführung und Übersicht

### 1.1 Wind als Ergänzung zur Solarenergie an Bord

Windgeneratoren sind nach Solarpanelen die zweitwichtigste erneuerbare Energiequelle auf Fahrtenyachten. Während Solarpanele tagsüber bei Sonnenschein optimale Erträge liefern, produzieren Windgeneratoren Tag und Nacht, bei bewölktem Himmel und insbesondere in den Übergangszeiten und Wintermonaten, wenn die Sonneneinstrahlung minimal ist. Die Kombination beider Systeme ergibt eine deutlich höhere Versorgungssicherheit als jede Einzellösung.

**Statistische Relevanz:**
- Laut Pantaenius Fahrtenyacht-Studie 2024 nutzen **42% aller Blauwassersegler** einen Windgenerator als Ergänzung zur Solaranlage
- Die durchschnittliche Betriebsdauer bis zum ersten relevanten Defekt beträgt **4,2 Jahre** bei Horizontalachsern und **5,8 Jahre** bei Vertikalachsern
- **67% aller Windgenerator-Beschwerden** beziehen sich auf Geräusch- und Vibrationsprobleme, nicht auf mangelnde Leistung
- Ein korrekt dimensionierter Windgenerator kann **30–60% des täglichen Energiebedarfs** einer Fahrtenyacht im Passat decken
- Die Kombination Solar + Wind reduziert den Generatorbetrieb um **70–85%** gegenüber Solar allein

**Confidence:** documented — basierend auf Pantaenius Blauwasser-Survey 2024, Superwind Servicedaten, OCC (Ocean Cruising Club) Crew Reports.

### 1.2 Einsatzprofile

#### 1.2.1 Blauwassersegler (Langfahrt)

| Parameter | Typisch | Optimal |
|-----------|---------|---------|
| Fahrtgebiet | Passatroute, Tropen, gemäßigte Breiten | Konsistente Winde 12–25 kn |
| Windverfügbarkeit | 60–80% der Zeit >8 kn | >70% der Zeit >10 kn |
| Täglicher Energiebedarf | 150–400 Ah/12V | — |
| Windgenerator-Beitrag | 30–80 Ah/Tag | 50–120 Ah/Tag |
| Typische Generatorgröße | 350–500 W nominal | 400 W |
| Montageort | Heckkorb, Arch, Mast | Heckarch 2,5m+ Höhe |
| Lärm-Toleranz | Mittel (kein Hafenbetrieb) | — |
| Budget | €1.500–€4.000 inkl. Montage | — |

#### 1.2.2 Küstensegler (Wochenend-/Urlaubsnutzung)

| Parameter | Typisch | Optimal |
|-----------|---------|---------|
| Fahrtgebiet | Nordsee, Ostsee, Mittelmeer Küste | Reviere mit zuverlässiger Thermik |
| Windverfügbarkeit | 50–70% der Zeit >8 kn | — |
| Täglicher Energiebedarf | 80–200 Ah/12V | — |
| Windgenerator-Beitrag | 15–50 Ah/Tag | — |
| Typische Generatorgröße | 200–400 W nominal | — |
| Montageort | Heckkorb, Geländer | — |
| Lärm-Toleranz | Gering (Hafennächte) | — |
| Budget | €800–€2.500 inkl. Montage | — |

#### 1.2.3 Ankerlieger / Liveaboard

| Parameter | Typisch | Optimal |
|-----------|---------|---------|
| Fahrtgebiet | Karibik, Mittelmeer Ankerbucht | Exponierte Ankerplätze mit Trade Winds |
| Windverfügbarkeit | Variable, abhängig vom Ankerplatz | — |
| Täglicher Energiebedarf | 200–500 Ah/12V | — |
| Windgenerator-Beitrag | 40–100 Ah/Tag | — |
| Typische Generatorgröße | 400–500 W nominal | — |
| Montageort | Heckarch, dedizierter Mast | — |
| Lärm-Toleranz | Sehr gering (24/7 an Bord) | — |
| Budget | €2.000–€5.000 inkl. Montage | — |

#### 1.2.4 Motoryacht (Ergänzung)

| Parameter | Typisch | Optimal |
|-----------|---------|---------|
| Fahrtgebiet | Küste, Binnengewässer | — |
| Windverfügbarkeit | 40–60% der Zeit >8 kn | — |
| Täglicher Energiebedarf | 200–600 Ah/12V | — |
| Windgenerator-Beitrag | 10–40 Ah/Tag | — |
| Typische Generatorgröße | 200–400 W nominal | — |
| Montageort | Flybridge-Arch, Antennenhalter | — |
| Lärm-Toleranz | Mittel | — |
| Budget | €1.000–€3.000 inkl. Montage | — |

### 1.3 Vor- und Nachteile gegenüber anderen Energiequellen

#### Vorteile

| Vorteil | Erläuterung |
|---------|-------------|
| 24/7 Produktion | Unabhängig von Tageszeit, produziert auch nachts |
| Komplementär zu Solar | Hoher Ertrag bei bedecktem Himmel und in Wintermonaten |
| Passatoptimal | In Passatregionen zuverlässigste erneuerbare Quelle |
| Geringer Platzbedarf | Rotorfläche <1 m², nutzt vertikalen Raum |
| Keine Verschattungsprobleme | Unabhängig von Segelstellung, Bimini, Dinghy |
| Automatischer Betrieb | Keine Bedienung nötig (bei korrektem Regler) |
| Psychologischer Effekt | Sichtbare, hörbare Produktion gibt Sicherheitsgefühl |

#### Nachteile

| Nachteil | Erläuterung |
|----------|-------------|
| Geräuschemission | 45–75 dB(A) je nach Modell und Windstärke |
| Vibration | Übertragung auf Rumpf/Mast, besonders bei Resonanz |
| Wartungsintensiver als Solar | Bewegliche Teile: Lager, Bürsten, Schleifkontakte |
| Verletzungsgefahr | Rotierender Rotor, Sicherheitsabstand erforderlich |
| Windabhängigkeit | Unter 8 kn praktisch kein Ertrag |
| Sturmsicherung | Bremsvorrichtung oder Kurzschluss-Bremse erforderlich |
| Mastbelastung | Zusätzliche Kräfte auf Heckkorb/Arch/Mast |
| Blitzrisiko | Höchster Punkt der Yacht (bei Mastmontage) |

### 1.4 Kosten-Nutzen-Analyse nach Yachtklasse

**Produktionssegelboot (8–14m):**
- Typischer Beitrag: 15–50 Ah/Tag (Durchschnitt, nicht Peak)
- Investition: €800–€2.500 (Generator + Regler + Montage)
- Amortisation vs. Generator-Diesel: 2–4 Jahre bei >80 Seetagen/Jahr
- Empfehlung: Sinnvoll ab 60+ Seetagen/Jahr oder bei eingeschränktem Solar

**Semi-Custom Fahrtenyacht (12–20m, Blauwasser):**
- Typischer Beitrag: 50–120 Ah/Tag in Passatregionen
- Investition: €2.000–€5.000 (Generator + Regler + Arch-Montage)
- Amortisation vs. Generator-Diesel: 1,5–3 Jahre bei Dauerfahrt
- Empfehlung: Quasi-Standard für Blauwasserausrüstung

**Custom/Superyacht (18m+):**
- Typischer Beitrag: Marginal im Verhältnis zum Gesamtverbrauch
- Investition: €3.000–€8.000
- Empfehlung: Nur als Statement oder für spezifische Subsysteme

### 1.5 Relevante Normen und Standards

| Standard | Thema | Relevanz für Windgeneratoren |
|----------|-------|------------------------------|
| IEC 61400-2 | Kleine Windenergieanlagen | Grundnorm für Anlagen <50 kW, Sicherheitsanforderungen |
| ISO 10133 | Elektrische Installationen (DC) | Kabelquerschnitte, Absicherung, Erdung |
| ISO 13297 | Elektrische Installationen (AC) | Falls Wechselrichter integriert |
| ISO 15085 | Man-Overboard-Prävention | Montage darf Bewegungsfreiheit nicht einschränken |
| IEC 61400-12-1 | Energieertragsberechnung | Methodik zur Ertragsberechnung (Leistungskurve + AEP) |
| ABYC E-11 | AC/DC Electrical Systems | US-Standard für Bordinstallation |
| GL Rules | Renewable Energy Certification | Germanischer Lloyd Typzertifizierung |
| MCA LY3 | Large Yacht Code | Anforderungen für >24m Yachten |

### 1.6 Historische Entwicklung

| Zeitraum | Meilenstein |
|----------|-------------|
| 1975–1980 | Erste improvisierte Windgeneratoren auf Langfahrtyachten (umgebaute Auto-Lichtmaschinen) |
| 1980–1985 | Ampair 100 als erster kommerzieller Marine-Windgenerator, 50 W |
| 1985–1990 | Rutland WG913, Fourwinds — Permanent-Magnet-Generatoren |
| 1990–1995 | D400, Air Marine (später Air-X) — kompakte Hochleistungsgeräte |
| 1995–2000 | Air-X dominant am Markt, aber berüchtigt für Lärm |
| 2000–2005 | Superwind 350, Silentwind — Fokus auf Geräuschreduzierung |
| 2005–2010 | Vertikalachser (Leading Edge) kommen auf den Markt |
| 2010–2015 | MPPT-Regler, verbesserte Bremssysteme, Carbon-Blätter |
| 2015–2020 | Hybrid Solar-Wind-Regler, integrierte Monitoring-Systeme |
| 2020–2025 | Helicale Vertikalachser, Lithium-optimierte Ladeprofile |
| 2025+ | KI-gesteuerte Ausrichtung, integrierte Wettervorhersage |

---

## 2. Grundlagen und Theorie

### 2.1 Physik der Windenergie

#### 2.1.1 Grundgleichung der Windleistung

Die theoretisch verfügbare Leistung im Wind berechnet sich nach:

```
P_wind = ½ × ρ × A × v³
```

Wobei:
- **P_wind** = verfügbare Windleistung [W]
- **ρ** = Luftdichte [kg/m³] (Standard: 1,225 kg/m³ auf Meereshöhe bei 15°C)
- **A** = Rotorfläche [m²] (= π × r²)
- **v** = Windgeschwindigkeit [m/s]

**Praxisbeispiel:**

| Rotordurchmesser | Fläche | 10 kn (5,1 m/s) | 15 kn (7,7 m/s) | 20 kn (10,3 m/s) | 25 kn (12,9 m/s) |
|------------------|--------|-----------------|-----------------|------------------|------------------|
| 0,8 m | 0,50 m² | 41 W | 140 W | 333 W | 651 W |
| 1,0 m | 0,79 m² | 64 W | 220 W | 525 W | 1.027 W |
| 1,17 m (Superwind) | 1,07 m² | 87 W | 299 W | 713 W | 1.394 W |
| 1,2 m | 1,13 m² | 92 W | 316 W | 753 W | 1.472 W |
| 1,5 m | 1,77 m² | 144 W | 494 W | 1.178 W | 2.303 W |

**Hinweis:** Dies sind theoretische Maximalwerte. Der tatsächliche Ertrag ist durch den Betz-Faktor und Wirkungsgrade begrenzt.

#### 2.1.2 Das Betz-Limit

Albert Betz bewies 1919, dass maximal **59,3%** (16/27) der kinetischen Windenergie in mechanische Energie umgewandelt werden können. Dies ist ein physikalisches Grundgesetz, unabhängig von der Konstruktion.

```
P_max = ½ × ρ × A × v³ × Cp_max
Cp_max = 16/27 ≈ 0,593
```

**Reale Leistungsbeiwerte (Cp) für Marine-Windgeneratoren:**

| Generatortyp | Cp typisch | Cp maximal | Erreicht bei TSR |
|-------------|-----------|-----------|-----------------|
| 3-Blatt HAWT (optimiert) | 0,25–0,35 | 0,38–0,42 | 5–7 |
| 5-Blatt HAWT | 0,20–0,28 | 0,30–0,35 | 3–5 |
| 6-Blatt HAWT | 0,18–0,25 | 0,28–0,32 | 2–4 |
| Savonius VAWT | 0,10–0,15 | 0,18 | 0,8–1,2 |
| Darrieus VAWT | 0,20–0,30 | 0,35 | 4–6 |
| Helical VAWT | 0,18–0,25 | 0,30 | 3–5 |

**Systemwirkungsgrad:**
Der Gesamtwirkungsgrad η_system berücksichtigt alle Verluste:

```
η_system = Cp × η_generator × η_regler × η_kabel × η_batterie

Typisch:
η_system = 0,32 × 0,85 × 0,92 × 0,97 × 0,90 = 0,22 (22%)
```

Das bedeutet: Nur etwa **20–25%** der Windenergie landen tatsächlich als nutzbare Energie in der Batterie.

#### 2.1.3 Kubische Windabhängigkeit — Die entscheidende Erkenntnis

Die Leistung steigt mit der **dritten Potenz** der Windgeschwindigkeit. Dies hat fundamentale Konsequenzen:

| Windgeschwindigkeit | Relative Leistung | Faktor vs. 10 kn |
|--------------------|--------------------|-------------------|
| 5 kn (2,6 m/s) | 1× | 0,125 |
| 8 kn (4,1 m/s) | 4,1× | 0,512 |
| 10 kn (5,1 m/s) | 8× | 1,000 |
| 12 kn (6,2 m/s) | 13,8× | 1,728 |
| 15 kn (7,7 m/s) | 27,5× | 3,375 |
| 20 kn (10,3 m/s) | 65,5× | 8,000 |
| 25 kn (12,9 m/s) | 128× | 15,625 |
| 30 kn (15,4 m/s) | 220× | 27,000 |

**Praxis-Implikation:** Eine Verdopplung der Windgeschwindigkeit bringt die **8-fache** Leistung. Deshalb ist die Montagehöhe (höhere Windgeschwindigkeit) wichtiger als ein etwas größerer Rotor.

### 2.2 Schnelllaufzahl (Tip Speed Ratio — TSR)

Die Schnelllaufzahl λ ist das Verhältnis der Blattspitzengeschwindigkeit zur Windgeschwindigkeit:

```
λ = (ω × R) / v = (2π × n × R) / v
```

Wobei:
- **ω** = Winkelgeschwindigkeit [rad/s]
- **R** = Rotorradius [m]
- **n** = Drehzahl [1/s]
- **v** = Windgeschwindigkeit [m/s]

**Optimale TSR nach Generatortyp:**

| Typ | Optimale TSR | Drehzahl bei 15 kn (R=0,5m) | Geräuschcharakteristik |
|-----|-------------|------------------------------|------------------------|
| 2-Blatt | 7–10 | 1.050–1.500 U/min | Sehr hohe Blattspitzengeschwindigkeit, laut |
| 3-Blatt | 5–7 | 750–1.050 U/min | Kompromiss Effizienz/Geräusch |
| 5-Blatt | 3–5 | 450–750 U/min | Leiser, niedrigere Effizienz |
| 6-Blatt | 2–4 | 300–600 U/min | Am leisesten unter HAWT |
| Savonius | 0,8–1,2 | 120–180 U/min | Sehr leise, brummendes Geräusch |
| Darrieus | 4–6 | 600–900 U/min | Pulsierend |
| Helical | 3–5 | 450–750 U/min | Gleichmäßig, leise |

**Blattspitzengeschwindigkeit und Geräusch:**

```
v_tip = λ × v_wind
```

Die Geräuschemission steigt ab v_tip > 40 m/s exponentiell an. Für akzeptablen Komfort auf einer Yacht sollte v_tip < 50 m/s bleiben.

| Modell | TSR | v_tip bei 20 kn | v_tip bei 30 kn | Komfort-Grenze |
|--------|-----|-----------------|-----------------|----------------|
| Superwind 350 | 5,5 | 56 m/s | 85 m/s | Überschritten ab ~18 kn |
| Silentwind 400 | 4,0 | 41 m/s | 62 m/s | Überschritten ab ~25 kn |
| D400 | 6,0 | 62 m/s | 93 m/s | Überschritten ab ~16 kn |
| Rutland 1200 | 3,5 | 36 m/s | 54 m/s | Überschritten ab ~28 kn |
| Leading Edge (VAWT) | 3,0 | 31 m/s | 46 m/s | Selten überschritten |

### 2.3 Leistungskurven

#### 2.3.1 Typische Leistungskurve eines Marine-Windgenerators

Eine ideale Leistungskurve hat vier Phasen:

```
Phase 1: Anlauf (0–6 kn)
  - Generator dreht, aber keine nennenswerte Leistung
  - Reibung und Generatorwiderstand dominieren
  - Typisch: 0–5 W

Phase 2: Kubischer Anstieg (6–20 kn)
  - Leistung steigt mit v³
  - Arbeitsbreich des Generators
  - Typisch: 5–350 W (bei 400W-Generator)

Phase 3: Nennleistung (20–30 kn)
  - Generator erreicht Nennleistung
  - Regler begrenzt Ladestrom oder Blätter stallen
  - Typisch: 350–420 W (bei 400W-Generator)

Phase 4: Sturmregelung (>30 kn)
  - Überdrehzahlschutz aktiv
  - Furling, Stall oder Bremse
  - Leistung konstant oder fallend
  - Typisch: 300–400 W oder 0 W (bei Bremsung)
```

#### 2.3.2 Vergleich realer Leistungskurven

| Wind (kn) | Superwind 350 | Silentwind 400 | Rutland 1200 | D400 | Leading Edge LE-v150 |
|-----------|--------------|----------------|-------------|------|---------------------|
| 5 | 0 W | 0 W | 2 W | 0 W | 0 W |
| 8 | 15 W | 12 W | 18 W | 10 W | 5 W |
| 10 | 35 W | 30 W | 40 W | 28 W | 15 W |
| 12 | 65 W | 55 W | 72 W | 55 W | 30 W |
| 15 | 130 W | 110 W | 145 W | 120 W | 65 W |
| 18 | 210 W | 185 W | 240 W | 200 W | 105 W |
| 20 | 280 W | 250 W | 320 W | 270 W | 140 W |
| 22 | 330 W | 310 W | 380 W | 340 W | 170 W |
| 25 | 350 W | 380 W | 420 W | 400 W | 200 W |
| 28 | 350 W | 400 W | 420 W | 420 W | 220 W |
| 30 | 350 W | 400 W | 380 W* | 400 W | 230 W |
| 35 | 350 W | 400 W | 300 W* | 380 W* | 240 W |
| 40 | 320 W** | 350 W** | 200 W* | 300 W* | 245 W |

*Stall/Furling aktiv  **Elektronische Bremse aktiv

### 2.4 Beaufort-Korrelation und Ertragserwartung

#### 2.4.1 Beaufort-Skala mit Windgenerator-Relevanz

| Bft | Bezeichnung | Knoten | m/s | Ertrag 400W-Gen | Ladestrom (12V) | Praxiskommentar |
|-----|-------------|--------|-----|-----------------|-----------------|-----------------|
| 0 | Windstille | 0–1 | 0–0,2 | 0 W | 0 A | Kein Ertrag |
| 1 | Leiser Zug | 1–3 | 0,3–1,5 | 0 W | 0 A | Rotor steht oder dreht frei |
| 2 | Leichte Brise | 4–6 | 1,6–3,3 | 0–5 W | 0–0,4 A | Minimal, Eigenverbrauch Regler |
| 3 | Schwache Brise | 7–10 | 3,4–5,4 | 5–40 W | 0,4–3,3 A | Erster nutzbarer Ertrag |
| 4 | Mäßige Brise | 11–16 | 5,5–7,9 | 40–160 W | 3,3–13,3 A | Guter Arbeitsbreich |
| 5 | Frische Brise | 17–21 | 8,0–10,7 | 160–320 W | 13,3–26,7 A | Optimaler Ertrag |
| 6 | Starker Wind | 22–27 | 10,8–13,8 | 320–400 W | 26,7–33,3 A | Nennleistung, Geräusch steigt |
| 7 | Steifer Wind | 28–33 | 13,9–17,1 | 350–400 W | 29–33 A | Regler begrenzt, laut |
| 8 | Stürmischer Wind | 34–40 | 17,2–20,7 | 300–400 W | 25–33 A | Bremse empfohlen |
| 9+ | Sturm | >40 | >20,8 | 0–200 W | 0–17 A | Bremse zwingend, Sicherheit |

#### 2.4.2 Ertragsberechnung nach Region und Saison

**Methodik:**
Der Tagesertrag berechnet sich aus der Windverteilung (Weibull) und der Leistungskurve:

```
E_tag = Σ(P(v_i) × h(v_i)) für alle v_i

Wobei:
- P(v_i) = Leistung bei Windgeschwindigkeit v_i [W]
- h(v_i) = Stunden pro Tag mit Windgeschwindigkeit v_i [h]
```

**Vereinfachte Ertragsschätzung (AYDI-Methode):**

```
E_tag_Wh = P_nenn × CF × 24

CF = Capacity Factor (anteilige Nutzung der Nennleistung)
```

**Capacity Factors nach Region und Saison:**

| Region | Sommer CF | Winter CF | Jahresmittel CF | Bemerkung |
|--------|-----------|-----------|-----------------|-----------|
| Nordsee | 0,18 | 0,32 | 0,25 | Stark saisonal, Starkwind Winter |
| Ostsee | 0,14 | 0,26 | 0,20 | Eisproblematik im Winter |
| Atlantik (Biskaya) | 0,20 | 0,35 | 0,27 | Gut ganzjährig |
| Mittelmeer West | 0,12 | 0,18 | 0,15 | Mistral-Phasen dominant |
| Mittelmeer Ost | 0,15 | 0,20 | 0,17 | Meltemi im Sommer |
| Karibik (Passatgürtel) | 0,25 | 0,22 | 0,24 | Konstant gut, Hurrikansaison beachten |
| Passatroute (Atlantik) | 0,28 | — | 0,28 | Idealbedingungen Nov–Feb |
| Südpazifik (Tropen) | 0,12 | 0,15 | 0,13 | Wenig Wind in Lagunen |
| Patagonien/Südatlantik | 0,30 | 0,38 | 0,34 | Extrem windreich, Sturmsicherung kritisch |
| Skandinavien | 0,16 | 0,28 | 0,22 | Lange Sommertage → Solar bevorzugt |

**Tageserträge bei 400 W Nennleistung (Beispiele):**

| Region | Sommer Wh/Tag | Winter Wh/Tag | Ah/Tag (12V, Sommer) |
|--------|---------------|---------------|---------------------|
| Nordsee | 1.728 | 3.072 | 144 |
| Ostsee | 1.344 | 2.496 | 112 |
| Mittelmeer West | 1.152 | 1.728 | 96 |
| Karibik | 2.400 | 2.112 | 200 |
| Passatroute | 2.688 | — | 224 |
| Patagonien | 2.880 | 3.648 | 240 |

### 2.5 Vibration und Resonanz

#### 2.5.1 Grundlagen der Vibrationsproblematik

Windgeneratoren erzeugen Vibrationen durch:

1. **Massenunwucht** — Ungleichmäßige Blattmasse (Fertigungstoleranzen, Regen/Eis)
2. **Aerodynamische Unwucht** — Unterschiedlicher Anstellwinkel der Blätter
3. **Turm-/Mastschwingung** — Eigenfrequenz des Montagemastes
4. **Blatt-Turmpassage** — Periodische Windabschattung (bei HAWT hinter Mast)
5. **Generator-Cogging** — Rastmomente bei Permanentmagnet-Generatoren

**Anregungsfrequenzen:**

```
f_rotor = n / 60 [Hz]  (Grundfrequenz)
f_blatt = f_rotor × Z [Hz]  (Blattpassierfrequenz, Z = Blattzahl)
f_cogging = f_rotor × p [Hz]  (Polzahl p)
```

**Beispielrechnung Superwind 350 bei 20 kn:**
- Drehzahl: ~800 U/min
- f_rotor = 800/60 = 13,3 Hz
- f_blatt = 13,3 × 3 = 40 Hz (3 Blätter)
- Spürbar als Brummen und Vibration am Montagehalter

#### 2.5.2 Resonanz am Montagesystem

Die Eigenfrequenz des Montagesystems (Rohr/Mast + Generator) muss die Anregungsfrequenzen meiden:

```
f_eigen = (1 / 2π) × √(3EI / (m × L³))

Wobei:
- E = E-Modul des Rohrmaterials [N/m²]
- I = Flächenträgheitsmoment [m⁴]
- m = Masse am Rohrende (Generator) [kg]
- L = freie Rohrlänge [m]
```

**Campbell-Diagramm-Analyse:**

Die Montage ist problematisch, wenn:
- f_eigen liegt im Bereich 0,8–1,2 × f_rotor (bei irgendeiner Betriebsdrehzahl)
- f_eigen liegt im Bereich 0,8–1,2 × f_blatt

**Abhilfe bei Resonanzproblemen:**

| Maßnahme | Effekt | Aufwand |
|----------|--------|---------|
| Rohr kürzen | f_eigen steigt | Gering |
| Rohr verstärken (dickwandiger) | f_eigen steigt | Mittel |
| Masse reduzieren (leichterer Generator) | f_eigen steigt | Hoch (neues Gerät) |
| Dämpfer am Rohrfuß | Amplitude sinkt | Mittel |
| Abspannung (Stage) | f_eigen steigt drastisch | Mittel |
| Schwingungstilger (TMD) | Resonanzamplitude sinkt | Hoch |

#### 2.5.3 Vibrationsmessung und Grenzwerte

| Kriterium | Grenzwert | Messstelle | Methode |
|-----------|-----------|------------|---------|
| ISO 10816-1 Zone A (gut) | < 2,8 mm/s RMS | Montagehalter-Fuß | Schwingungsmesser |
| ISO 10816-1 Zone B (akzeptabel) | 2,8–7,1 mm/s RMS | Montagehalter-Fuß | Schwingungsmesser |
| Komfort an Bord | < 0,5 mm/s RMS | Innenrumpf nächste Koje | Smartphone-App (Orientierung) |
| Strukturelle Sicherheit | < 15 mm/s Peak | Montagehalter-Basis | Professionell |

### 2.6 Geräuschemission

#### 2.6.1 Schallquellen

| Quelle | Frequenzbereich | Charakter | Dominiert bei |
|--------|-----------------|-----------|---------------|
| Blattspitzenrauschen | 500–4.000 Hz | Zischen, Rauschen | Hoher TSR, >20 kn |
| Aerodynamisches Breitband | 100–2.000 Hz | Rauschen | Immer |
| Blatt-Stallgeräusch | 200–800 Hz | Dröhnen, Pulsieren | Stall-Bereich |
| Generatorgeräusch | 100–1.000 Hz (Oberwellen) | Summen | Niedrige Drehzahl |
| Cogging/Rasten | Diskrete Frequenzen | Ticken | Niedrige Drehzahl |
| Mechanisches Schlagen | < 50 Hz | Dumpfes Klopfen | Lagerverschleiß |
| Mastübertragung | 50–500 Hz | Brummen im Schiff | Resonanz |

#### 2.6.2 Schalldruckpegel nach Modell und Windstärke

| Modell | 10 kn | 15 kn | 20 kn | 25 kn | 30 kn | Messabstand |
|--------|-------|-------|-------|-------|-------|-------------|
| Superwind 350 | 32 dB(A) | 42 dB(A) | 52 dB(A) | 58 dB(A) | 62 dB(A) | 7 m |
| Silentwind 400 | 28 dB(A) | 38 dB(A) | 48 dB(A) | 54 dB(A) | 58 dB(A) | 7 m |
| Rutland 1200 | 30 dB(A) | 40 dB(A) | 50 dB(A) | 56 dB(A) | 60 dB(A) | 7 m |
| D400 | 35 dB(A) | 45 dB(A) | 56 dB(A) | 63 dB(A) | 68 dB(A) | 7 m |
| Air Breeze | 38 dB(A) | 50 dB(A) | 60 dB(A) | 68 dB(A) | 72 dB(A) | 7 m |
| Leading Edge LE-v150 | 25 dB(A) | 32 dB(A) | 40 dB(A) | 45 dB(A) | 48 dB(A) | 7 m |

**Referenzwerte zum Vergleich:**
- Ruhiges Ankerfeld, Nacht: 25–30 dB(A)
- Hafen, leise Nacht: 35–40 dB(A)
- Normale Unterhaltung: 60 dB(A)
- Dinghy-Außenborder: 75–85 dB(A)

#### 2.6.3 Lärmminderungsmaßnahmen

| Maßnahme | Reduktion | Kosten | Anmerkung |
|----------|-----------|--------|-----------|
| Modellwechsel (leiser Typ) | 5–15 dB(A) | €1.000–€3.000 | Effektivste Maßnahme |
| Blattmodifikation (Winglets) | 2–4 dB(A) | €100–€300 | Nicht bei allen Modellen möglich |
| Gummipuffer Montage | 1–3 dB(A) (Körperschall) | €50–€150 | Reduziert Übertragung auf Rumpf |
| Höhere Montage | 2–5 dB(A) (am Ohr) | €200–€500 | Abstandsgesetz |
| Nacht-Bremse (Windstärke-abhängig) | Vollständig | €0 (Regler-Einstellung) | Verlust Nachtproduktion |
| Drehzahlbegrenzung per Regler | 3–8 dB(A) | €0 (Software) | Leistungsverlust 10–30% |

### 2.7 Windgradient und Montagehöhe

Der Wind nimmt mit der Höhe über dem Boden/Wasser zu (logarithmisches Windprofil):

```
v(h) = v_ref × (ln(h/z0) / ln(h_ref/z0))

Wobei:
- v(h) = Windgeschwindigkeit in Höhe h
- v_ref = Referenz-Windgeschwindigkeit in Höhe h_ref
- z0 = Rauigkeitslänge (offenes Wasser: 0,0002 m)
- h_ref = Referenzhöhe (typisch 10 m für meteorologische Daten)
```

**Praktische Höhenfaktoren (Wasser):**

| Höhe über Wasser | Faktor vs. 10m | Leistungsfaktor (v³) |
|------------------|----------------|---------------------|
| 2 m (Deck) | 0,82 | 0,55 |
| 3 m (Heckkorb) | 0,86 | 0,64 |
| 4 m (Arch) | 0,89 | 0,71 |
| 5 m (hohe Arch) | 0,92 | 0,78 |
| 6 m (Mast niedrig) | 0,94 | 0,83 |
| 8 m (Mast mittel) | 0,97 | 0,91 |
| 10 m (Masttop) | 1,00 | 1,00 |
| 12 m (Masttop groß) | 1,02 | 1,06 |
| 15 m (Mastspitze) | 1,04 | 1,13 |

**Schlussfolgerung:** Die Montage auf einer 3m-Heckstange liefert nur **64%** der Leistung einer Masttop-Montage bei 10m. Die Montage auf einer 5m-Arch liefert **78%**.

### 2.8 Apparent Wind auf fahrendem Schiff

Auf einem segelnden oder motorenden Schiff wirkt der **scheinbare Wind** (Apparent Wind), nicht der wahre Wind:

```
Vor dem Wind:
v_apparent = v_true - v_boat
→ Windgenerator-Ertrag SINKT auf Vorwindkursen

Am Wind / Halbwind:
v_apparent > v_true (vektoriell)
→ Windgenerator-Ertrag STEIGT auf Am-Wind-Kursen
```

**Ertragsvariation nach Kurs (15 kn wahrer Wind, 6 kn Bootsgeschwindigkeit):**

| Kurs zum wahren Wind | Apparent Wind | Relative Leistung | Kommentar |
|---------------------|---------------|-------------------|-----------|
| Am Wind (45°) | 19,5 kn | 220% | Hervorragend |
| Halbwind (90°) | 16,2 kn | 125% | Gut |
| Raumer Wind (135°) | 12,0 kn | 60% | Mäßig |
| Vor dem Wind (180°) | 9,0 kn | 27% | Schwach |

**Praxis-Implikation für Blauwassersegler:** Auf der typischen Passatroute (Vorwindkurs) ist der Apparent-Wind-Effekt negativ. Tatsächlicher Ertrag ist geringer als stationäre Ankerbedingungen vermuten lassen.

---

## 3. Typenübersicht

### 3.1 Horizontalachser (HAWT — Horizontal Axis Wind Turbine)

#### 3.1.1 Drei-Blatt-Rotor

**Beschreibung:** Der Standard im Marine-Bereich. Drei aerodynamisch profilierte Blätter, horizontal rotierende Achse, passive Windnachführung (Fahne oder Rotor-Nachlauf).

**Funktionsprinzip:**
- Auftriebsbasiert: Blätter erzeugen wie ein Flugzeugflügel Auftrieb
- Hohe TSR (5–7): Blattspitzen laufen deutlich schneller als der Wind
- Anlauf bei 6–10 kn (modellabhängig)
- Passive Windnachführung durch Heckflosse oder aerodynamische Gestaltung

**Technische Merkmale:**

| Parameter | Typisch | Bereich |
|-----------|---------|---------|
| Rotordurchmesser | 1,0–1,3 m | 0,8–1,5 m |
| Nennleistung | 300–500 W | 200–700 W |
| Anlaufgeschwindigkeit | 7–10 kn | 5–12 kn |
| Nennwindgeschwindigkeit | 25–30 kn | 22–35 kn |
| Gewicht | 6–15 kg | 4–20 kg |
| TSR (optimal) | 5–7 | — |
| Cp (maximal) | 0,35–0,42 | — |
| Geräusch (20 kn) | 48–56 dB(A) | — |
| Lebensdauer Lager | 5–10 Jahre | — |

**Vor-/Nachteile:**

| Vorteile | Nachteile |
|----------|-----------|
| Höchster Wirkungsgrad aller Typen | Laut bei >20 kn |
| Bewährte Technologie, große Auswahl | Vibration bei hoher Drehzahl |
| Guter Anlauf bei moderatem Wind | Verletzungsgefahr (Rotorteller) |
| Einfache Wartung | Sturmregelung erforderlich |
| Viele Ersatzteile verfügbar | Windrichtung muss nachgeführt werden |

**Modelle:** Superwind 350, D400, Air Breeze, Primus Air 40, Rutland FM1803

#### 3.1.2 Fünf-Blatt-Rotor

**Beschreibung:** Mehr Blätter bei kleinerem Durchmesser. Niedrigere TSR, damit geringere Blattspitzengeschwindigkeit und weniger Geräusch. Guter Kompromiss für lärmsensible Anwendungen.

**Funktionsprinzip:**
- Wie 3-Blatt, aber niedrigere Schnelllaufzahl
- Mehr Blattfläche → höheres Anlaufmoment → besserer Schwachwindstart
- Etwas niedrigerer maximaler Cp als 3-Blatt

**Technische Merkmale:**

| Parameter | Typisch | Bereich |
|-----------|---------|---------|
| Rotordurchmesser | 1,0–1,2 m | 0,9–1,4 m |
| Nennleistung | 200–400 W | 150–500 W |
| Anlaufgeschwindigkeit | 5–8 kn | 4–10 kn |
| Nennwindgeschwindigkeit | 25–30 kn | — |
| Gewicht | 7–14 kg | — |
| TSR (optimal) | 3–5 | — |
| Cp (maximal) | 0,30–0,35 | — |
| Geräusch (20 kn) | 42–50 dB(A) | — |

**Vor-/Nachteile:**

| Vorteile | Nachteile |
|----------|-----------|
| Leiser als 3-Blatt | Niedrigerer max. Wirkungsgrad |
| Besserer Schwachwindstart | Größerer Rotordurchmesser für gleiche Leistung |
| Gleichmäßigeres Drehmoment | Mehr Blätter = mehr Wartungspotential |
| Geringere Vibration | Weniger Modellauswahl am Markt |

**Modelle:** Silentwind 400, Rutland 1200, Marlec Rutland 504

#### 3.1.3 Sechs-Blatt-Rotor

**Beschreibung:** Maximum an Blättern für den leisesten HAWT-Betrieb. Sehr niedriger TSR, hochanlaufstark, aber mit dem niedrigsten Wirkungsgrad der HAWT-Kategorie.

**Technische Merkmale:**

| Parameter | Typisch | Bereich |
|-----------|---------|---------|
| Rotordurchmesser | 1,0–1,4 m | — |
| Nennleistung | 150–350 W | — |
| Anlaufgeschwindigkeit | 4–7 kn | — |
| TSR (optimal) | 2–4 | — |
| Cp (maximal) | 0,25–0,32 | — |
| Geräusch (20 kn) | 38–46 dB(A) | — |

**Modelle:** Rutland 1200 (6 Blätter), einige chinesische Hersteller

### 3.2 Vertikalachser (VAWT — Vertical Axis Wind Turbine)

#### 3.2.1 Savonius-Rotor

**Beschreibung:** Widerstandsbasierter Rotor mit S-förmigem Querschnitt. Sehr einfache, robuste Konstruktion. Niedrigster Wirkungsgrad, aber unempfindlich gegen Windrichtung und sehr leise.

**Funktionsprinzip:**
- Widerstandsprinzip: Eine Schale fängt den Wind, die andere weicht aus
- TSR immer <1 (Blattspitze langsamer als Wind)
- Omnidirektional: keine Windnachführung nötig
- Selbstanlaufend auch bei sehr geringem Wind

**Technische Merkmale:**

| Parameter | Typisch | Bereich |
|-----------|---------|---------|
| Rotordurchmesser | 0,3–0,6 m | — |
| Rotorhöhe | 0,5–1,0 m | — |
| Nennleistung | 50–150 W | 30–200 W |
| Anlaufgeschwindigkeit | 3–5 kn | — |
| TSR (optimal) | 0,8–1,2 | — |
| Cp (maximal) | 0,15–0,18 | — |
| Geräusch (20 kn) | 25–35 dB(A) | — |
| Gewicht | 5–12 kg | — |

**Vor-/Nachteile:**

| Vorteile | Nachteile |
|----------|-----------|
| Sehr leise | Sehr niedriger Wirkungsgrad |
| Omnidirektional | Große Baufläche für wenig Leistung |
| Selbstanlaufend | Schwere Vibrationen bei Unwucht |
| Keine Sturmregelung nötig (selbstbegrenzend) | Begrenzte Leistung |
| Robust, wenig Wartung | Selten als Marinegerät verfügbar |
| Keine Verletzungsgefahr | — |

**Einsatzbereich:** Nischenanwendung für ultra-leise Anforderungen, z.B. Naturschutzgebiete, Liveaboards mit Geräuschsensibilität.

#### 3.2.2 Darrieus-Rotor

**Beschreibung:** Auftriebsbasierter Vertikalachser mit geraden oder gekrümmten Blättern. Höherer Wirkungsgrad als Savonius, aber nicht selbstanlaufend und anfällig für Vibrationen.

**Funktionsprinzip:**
- Auftriebsbasiert wie HAWT, aber vertikale Achse
- Blätter erzeugen Auftrieb durch Anströmung unter wechselndem Anstellwinkel
- Hohe TSR möglich (4–6)
- NICHT selbstanlaufend (benötigt Starthilfe oder Savonius-Kombination)

**Technische Merkmale:**

| Parameter | Typisch | Bereich |
|-----------|---------|---------|
| Rotordurchmesser | 0,5–1,0 m | — |
| Rotorhöhe | 0,8–1,5 m | — |
| Nennleistung | 100–300 W | 50–500 W |
| Anlaufgeschwindigkeit | 8–12 kn (benötigt oft Hilfsstart) | — |
| TSR (optimal) | 4–6 | — |
| Cp (maximal) | 0,30–0,35 | — |
| Geräusch (20 kn) | 35–48 dB(A) | — |
| Gewicht | 8–20 kg | — |

**Vor-/Nachteile:**

| Vorteile | Nachteile |
|----------|-----------|
| Guter Wirkungsgrad für VAWT | Nicht selbstanlaufend |
| Omnidirektional | Pulsierende Drehmomentbelastung |
| Kompakte Bauform | Ermüdungsbelastung Blätter |
| Keine Heckflosse nötig | Komplexe Lagerung |

#### 3.2.3 Helicaler Rotor (Twisted Savonius / Gorlov)

**Beschreibung:** Moderne Weiterentwicklung des Savonius/Darrieus-Prinzips mit helikal (schraubenförmig) verdrehten Blättern. Kombiniert Vorteile beider Konzepte: Selbstanlauf, gleichmäßiges Drehmoment, akzeptabler Wirkungsgrad.

**Funktionsprinzip:**
- Hybridprinzip: Widerstand + Auftrieb
- Helicale Verdrehung (typisch 60°) sorgt für gleichmäßige Drehmomentabgabe
- Selbstanlaufend durch Widerstandskomponente
- Keine toten Punkte wie beim geraden Darrieus

**Technische Merkmale:**

| Parameter | Typisch | Bereich |
|-----------|---------|---------|
| Rotordurchmesser | 0,4–0,8 m | 0,3–1,0 m |
| Rotorhöhe | 0,6–1,2 m | 0,5–1,5 m |
| Nennleistung | 100–300 W | 50–500 W |
| Anlaufgeschwindigkeit | 5–8 kn | — |
| TSR (optimal) | 3–5 | — |
| Cp (maximal) | 0,25–0,30 | — |
| Geräusch (20 kn) | 30–42 dB(A) | — |
| Gewicht | 8–18 kg | — |

**Vor-/Nachteile:**

| Vorteile | Nachteile |
|----------|-----------|
| Sehr leise | Niedrigerer Wirkungsgrad als HAWT |
| Omnidirektional | Höherer Preis pro Watt |
| Selbstanlaufend | Wenig Marine-spezifische Modelle |
| Gleichmäßiges Drehmoment | Größer/schwerer für gleiche Leistung |
| Optisch ansprechend | Weniger Langzeiterfahrung auf See |
| Keine Verletzungsgefahr | Komplexere Blattfertigung |
| Keine Sturmregelung nötig | — |

**Modelle:** Leading Edge LE-v150, Hi-Q Windpower, Pacific Sky Power

### 3.3 Hybrid Solar-Wind-Systeme

#### 3.3.1 Integrierte Hybrid-Einheiten

Einige Hersteller bieten Kompaktgeräte, die Windgenerator und Solarpanel in einer Einheit kombinieren.

**Konzeptansätze:**

| Ansatz | Beschreibung | Beispiel |
|--------|-------------|---------|
| VAWT mit Solar-Ring | Vertikalachser umgeben von PV-Zellen | Diverse China-Produkte |
| HAWT mit Nacelle-PV | Solarzellen auf der Generatorgondel | Prototypen |
| Gemeinsamer Regler | Separater Wind + Solar, ein MPPT-Regler | Victron SmartSolar + Wind |
| Integriertes Monitoring | Gemeinsame Ertragsüberwachung | Superwind + NMEA2000 |

**Bewertung für den Marineeinsatz:**

- Integrierte Kompaktgeräte: **Nicht empfohlen.** Meist minderwertige Qualität, schlecht gewartbar, Kompromisse in beiden Funktionen.
- Separater Wind + Solar mit Hybrid-Regler: **Empfohlen.** Beste Einzelkomponenten, optimale Regelung, einfache Wartung.
- Monitoring-Integration: **Empfohlen.** Gemeinsames Display/App für beide Quellen.

#### 3.3.2 Hybrid-Regler (Dual-Input MPPT)

Moderne Laderegler können sowohl Solar- als auch Wind-Input verarbeiten:

| Regler | Solar-Input | Wind-Input | Batterie | Features |
|--------|-------------|------------|----------|----------|
| Victron SmartSolar MPPT + Wind | bis 75V/450W | — (separater Windregler) | 12/24V | Bluetooth, VRM |
| Genasun GVB-8 | — | bis 40V/350W | 12V | MPPT für Wind |
| Morningstar TriStar MPPT | bis 150V/600W | Diversion mode | 12/24/48V | Dual-Use |
| EPever Tracer AN (Hybrid) | bis 100V/400W | bis 400W | 12/24V | Budget-Option |
| Silentwind Hybrid | bis 400W Solar | bis 500W Wind | 12/24V | Integriert |

### 3.4 Vergleichsmatrix aller Typen

| Kriterium | 3-Blatt HAWT | 5-Blatt HAWT | Savonius | Darrieus | Helical VAWT |
|-----------|-------------|-------------|----------|----------|-------------|
| Wirkungsgrad (Cp) | ★★★★★ | ★★★★ | ★★ | ★★★★ | ★★★ |
| Geräusch | ★★ | ★★★ | ★★★★★ | ★★★ | ★★★★ |
| Vibration | ★★ | ★★★ | ★★★★ | ★★ | ★★★★ |
| Anlaufverhalten | ★★★ | ★★★★ | ★★★★★ | ★ | ★★★★ |
| Sturmfestigkeit | ★★★ | ★★★ | ★★★★★ | ★★★ | ★★★★ |
| Wartungsaufwand | ★★★ | ★★★ | ★★★★ | ★★ | ★★★★ |
| Sicherheit (Verletzung) | ★★ | ★★ | ★★★★★ | ★★★★ | ★★★★★ |
| Preis/Leistung | ★★★★★ | ★★★★ | ★★ | ★★★ | ★★★ |
| Modellauswahl Markt | ★★★★★ | ★★★ | ★ | ★★ | ★★ |
| Langzeiterfahrung | ★★★★★ | ★★★★ | ★★★ | ★★★ | ★★ |

(★★★★★ = hervorragend, ★ = schlecht)

---

## 4. Produktlinien und Spezifikationen

### 4.1 Superwind 350

**Hersteller:** Superwind GmbH, Brühl, Deutschland
**Typ:** 3-Blatt Horizontalachser
**Marktposition:** Premium-Segment, Referenzgerät für Blauwassersegler

#### Technische Daten

| Parameter | Wert |
|-----------|------|
| Nennleistung | 350 W (bei 28 kn) |
| Rotordurchmesser | 1,17 m |
| Blattmaterial | Glasfaserverstärkter Kunststoff (GFK) |
| Blattzahl | 3 |
| Generator | Bürstenloser Permanentmagnet (NdFeB) |
| Anlaufgeschwindigkeit | 7 kn (3,6 m/s) |
| Nennwindgeschwindigkeit | 28 kn (14,4 m/s) |
| Überlebenswindgeschwindigkeit | 120 kn (62 m/s) |
| Gewicht | 7,5 kg |
| Durchmesser Montagesockel | 48,3 mm Rohr |
| Schutzart | IP68 |
| Spannung | 12V oder 24V (Modellvariante) |
| Max. Ladestrom | 25 A (12V), 12 A (24V) |
| Sturmregelung | Passives Pitch-System (Blätter stallen) |
| Bremse | Elektronische Kurzschlussbremse |
| Lebensdauer Lager | >80.000 Betriebsstunden |
| Garantie | 5 Jahre |
| Preis (UVP 2025) | ca. €2.200 (ohne Regler) |

#### Leistungskurve (Herstellerangabe, unabhängig verifiziert)

| Wind (kn) | Leistung (W) | Ladestrom 12V (A) | Ladestrom 24V (A) |
|-----------|-------------|-------------------|-------------------|
| 7 | 5 | 0,4 | 0,2 |
| 10 | 35 | 2,9 | 1,5 |
| 12 | 65 | 5,4 | 2,7 |
| 15 | 130 | 10,8 | 5,4 |
| 18 | 210 | 17,5 | 8,8 |
| 20 | 280 | 23,3 | 11,7 |
| 22 | 330 | 27,5 | 13,8 |
| 25 | 350 | 29,2 | 14,6 |
| 28 | 350 | 29,2 | 14,6 |
| 30 | 350 | 29,2 | 14,6 |
| 35 | 350 | 29,2 | 14,6 |
| 40 | 320 | 26,7 | 13,3 |

#### Besondere Merkmale

- **Passive Pitch-Regelung:** Blätter verändern bei hoher Drehzahl selbstständig den Anstellwinkel (Zentrifugalkraft-gesteuert). Keine Elektronik, kein Verschleiß.
- **Wartungsfreie Lager:** Doppelt abgedichtete Hochleistungskugellager, >80.000 h.
- **Marine-Grade Korrosionsschutz:** Alle Metallteile Edelstahl 316L oder eloxiertes Aluminium.
- **Integrierte Kurzschlussbremse:** Schalter am Regler oder manuell.
- **Made in Germany:** Fertigung in Brühl bei Köln.

#### Erfahrungswerte aus der Praxis

- Sehr zuverlässig, kaum Ausfälle dokumentiert
- Geräusch ab 18–20 kn deutlich wahrnehmbar (Zischen)
- Passive Pitch-Regelung funktioniert ab ~25 kn, nicht schlagartig
- Lager zeigen nach 6–8 Jahren erste Geräusche (Austausch-Kit verfügbar, ~€180)
- Bei Dauer-Starkwind (Patagonien, Kap Hoorn) bevorzugtes Modell
- Schwäche: Schwachwindertrag unter 10 kn marginal

### 4.2 Rutland 1200 (FM1803)

**Hersteller:** Marlec Engineering Co Ltd, Corby, England
**Typ:** 6-Blatt Horizontalachser
**Marktposition:** Mittelklasse, populär bei Küstenseglern und Motorbooten

#### Technische Daten

| Parameter | Wert |
|-----------|------|
| Nennleistung | 420 W (bei 30 kn) |
| Rotordurchmesser | 1,14 m |
| Blattmaterial | Glasfaserverstärkter Nylon |
| Blattzahl | 6 |
| Generator | Permanentmagnet, bürstenlos |
| Anlaufgeschwindigkeit | 5 kn (2,6 m/s) |
| Nennwindgeschwindigkeit | 30 kn (15,4 m/s) |
| Überlebenswindgeschwindigkeit | 90 kn (46 m/s) |
| Gewicht | 9,5 kg |
| Durchmesser Montagesockel | 48,3 mm Rohr |
| Schutzart | IP55 |
| Spannung | 12V oder 24V |
| Max. Ladestrom | 30 A (12V) |
| Sturmregelung | Elektronische Drehzahlbegrenzung (Regler) |
| Bremse | Elektronisch über Regler |
| Garantie | 3 Jahre |
| Preis (UVP 2025) | ca. €1.400 (inkl. Regler) |

#### Leistungskurve

| Wind (kn) | Leistung (W) | Ladestrom 12V (A) |
|-----------|-------------|-------------------|
| 5 | 2 | 0,2 |
| 8 | 18 | 1,5 |
| 10 | 40 | 3,3 |
| 12 | 72 | 6,0 |
| 15 | 145 | 12,1 |
| 18 | 240 | 20,0 |
| 20 | 320 | 26,7 |
| 22 | 380 | 31,7 |
| 25 | 420 | 35,0 |
| 28 | 420 | 35,0 |
| 30 | 420 | 35,0 |
| 35 | 300 | 25,0 |

#### Besondere Merkmale

- **6 Blätter:** Sehr guter Schwachwindstart, leiser als 3-Blatt
- **Elektronische Sturmregelung:** Regler begrenzt Drehzahl über Brems-Widerstand
- **Preis-Leistung:** Gutes Verhältnis, inkl. Regler im Lieferumfang
- **Blätter austauschbar:** Einzelne Blätter nachbestellbar (~€35/Stück)
- **Hoher Anlaufmoment:** Startet bereits bei 5 kn nutzbar

#### Erfahrungswerte aus der Praxis

- Schwachwindspezialist: merkbar mehr Ertrag unter 10 kn als 3-Blatt-Typen
- Blätter aus Nylon weniger UV-beständig als GFK (Versprödung nach 4–6 Jahren)
- Elektronische Bremse hat bekannte Ausfälle bei Überspannung
- Geräusch bei Starkwind: typisches Heulen ab 25 kn
- Beliebtes Budget-Modell für Nordsee/Ostsee-Segler
- Windnachführung etwas träge bei böigem Wind

### 4.3 Silentwind 400

**Hersteller:** Silentwind GmbH, Jülich, Deutschland
**Typ:** 5-Blatt Horizontalachser
**Marktposition:** Premium-Segment, Fokus auf Geräuschreduzierung

#### Technische Daten

| Parameter | Wert |
|-----------|------|
| Nennleistung | 400 W (bei 26 kn) |
| Rotordurchmesser | 1,13 m |
| Blattmaterial | Carbon-GFK-Hybrid |
| Blattzahl | 5 |
| Generator | Bürstenloser Permanentmagnet, Coreless Design |
| Anlaufgeschwindigkeit | 6 kn (3,1 m/s) |
| Nennwindgeschwindigkeit | 26 kn (13,4 m/s) |
| Überlebenswindgeschwindigkeit | 110 kn (57 m/s) |
| Gewicht | 8,2 kg |
| Durchmesser Montagesockel | 48,3 mm Rohr |
| Schutzart | IP67 |
| Spannung | 12V oder 24V |
| Max. Ladestrom | 28 A (12V), 14 A (24V) |
| Sturmregelung | Elektronisch + aerodynamisches Stall |
| Bremse | Elektronische Kurzschlussbremse + manueller Schalter |
| Lebensdauer Lager | >60.000 Betriebsstunden |
| Garantie | 5 Jahre |
| Preis (UVP 2025) | ca. €2.600 (inkl. Hybrid-Regler) |

#### Leistungskurve

| Wind (kn) | Leistung (W) | Ladestrom 12V (A) |
|-----------|-------------|-------------------|
| 6 | 3 | 0,3 |
| 8 | 12 | 1,0 |
| 10 | 30 | 2,5 |
| 12 | 55 | 4,6 |
| 15 | 110 | 9,2 |
| 18 | 185 | 15,4 |
| 20 | 250 | 20,8 |
| 22 | 310 | 25,8 |
| 25 | 380 | 31,7 |
| 26 | 400 | 33,3 |
| 28 | 400 | 33,3 |
| 30 | 400 | 33,3 |
| 35 | 380 | 31,7 |
| 40 | 350 | 29,2 |

#### Besondere Merkmale

- **Coreless Generator:** Kein Cogging (Rastmoment), extrem leiser Lauf auch bei niedriger Drehzahl
- **5 Carbon-GFK-Blätter:** Sehr leicht, UV-beständig, leiser durch höhere Steifigkeit
- **Integrierter Hybrid-Regler:** Kann gleichzeitig Solar- und Windladung managen
- **NMEA 2000 Schnittstelle:** Optional, Ertragsanzeige auf Plotter
- **Stummschaltmodus:** Per App Drehzahl auf 60% begrenzen (Nachtmodus)

#### Erfahrungswerte aus der Praxis

- Gilt als leisester HAWT am Markt (messbar 5–8 dB leiser als D400)
- Coreless-Design eliminiert das typische Cogging-Geräusch
- Hybrid-Regler zuverlässig, gute App-Integration
- Carbon-Blätter empfindlich gegen Steinschlag (Dinghy-Kran!)
- In der Karibik sehr beliebt bei Liveaboards
- Etwas geringerer Peak-Ertrag als Superwind, aber besserer Schwachwindertrag

### 4.4 D400

**Hersteller:** Eclectic Energy Ltd, Southwell, England
**Typ:** 5-Blatt Horizontalachser
**Marktposition:** Obere Mittelklasse, Langfahrt-Klassiker

#### Technische Daten

| Parameter | Wert |
|-----------|------|
| Nennleistung | 400 W (bei 30 kn) |
| Rotordurchmesser | 1,10 m |
| Blattmaterial | GFK |
| Blattzahl | 5 |
| Generator | Permanentmagnet, eisenlos (Coreless) |
| Anlaufgeschwindigkeit | 7 kn (3,6 m/s) |
| Nennwindgeschwindigkeit | 30 kn (15,4 m/s) |
| Überlebenswindgeschwindigkeit | 100+ kn |
| Gewicht | 8,0 kg |
| Durchmesser Montagesockel | 48,3 mm |
| Schutzart | IP66 |
| Spannung | 12V, 24V oder 48V |
| Max. Ladestrom | 27 A (12V) |
| Sturmregelung | Elektronische Bremse (Regler), aerodynamischer Stall |
| Garantie | 3 Jahre |
| Preis (UVP 2025) | ca. €1.800 (ohne Regler) |

#### Leistungskurve

| Wind (kn) | Leistung (W) | Ladestrom 12V (A) |
|-----------|-------------|-------------------|
| 7 | 4 | 0,3 |
| 10 | 28 | 2,3 |
| 12 | 55 | 4,6 |
| 15 | 120 | 10,0 |
| 18 | 200 | 16,7 |
| 20 | 270 | 22,5 |
| 22 | 340 | 28,3 |
| 25 | 400 | 33,3 |
| 28 | 420 | 35,0 |
| 30 | 400 | 33,3 |
| 35 | 380 | 31,7 |

#### Besondere Merkmale

- **Coreless Design:** Wie Silentwind, kein Cogging, leiser Anlauf
- **Sehr leicht:** 8,0 kg ist konkurrenzfähig mit der Superwind
- **48V-Variante:** Für größere Yachten mit 48V-System
- **Bewährt auf Weltumseglungen:** Seit >20 Jahren auf dem Markt

#### Erfahrungswerte aus der Praxis

- Etwas lauter als Silentwind bei >20 kn (Blattdesign älter)
- Lager langlebig, aber schwerer zu wechseln als bei Superwind
- Coreless-Generator effizient im Teillastbereich
- Guter Allrounder, nicht in jeder Disziplin Spitze
- Ersatzteilversorgung zuverlässig

### 4.5 Leading Edge LE-v150

**Hersteller:** Leading Edge Power Ltd, (aufgelöst/übernommen)
**Typ:** Helicaler Vertikalachser (VAWT)
**Marktposition:** Nische, Premium-VAWT für lärmsensible Installationen

#### Technische Daten

| Parameter | Wert |
|-----------|------|
| Nennleistung | 150 W (bei 28 kn) |
| Rotordurchmesser | 0,58 m |
| Rotorhöhe | 0,73 m |
| Blattmaterial | GFK, UV-stabilisiert |
| Blattzahl | 3 (helikal verdreht) |
| Generator | Permanentmagnet, Axialflux |
| Anlaufgeschwindigkeit | 6 kn (3,1 m/s) |
| Nennwindgeschwindigkeit | 28 kn (14,4 m/s) |
| Überlebenswindgeschwindigkeit | 100+ kn |
| Gewicht | 12 kg |
| Schutzart | IP65 |
| Spannung | 12V oder 24V |
| Max. Ladestrom | 10 A (12V) |
| Sturmregelung | Selbstbegrenzend (aerodynamisch) |
| Garantie | 2 Jahre |
| Preis (UVP, historisch) | ca. €1.800 |

#### Leistungskurve

| Wind (kn) | Leistung (W) | Ladestrom 12V (A) |
|-----------|-------------|-------------------|
| 6 | 2 | 0,2 |
| 8 | 5 | 0,4 |
| 10 | 15 | 1,3 |
| 12 | 30 | 2,5 |
| 15 | 65 | 5,4 |
| 18 | 105 | 8,8 |
| 20 | 140 | 11,7 |
| 22 | 170 | 14,2 |
| 25 | 200 | 16,7 |
| 28 | 150 | 12,5 |
| 30 | 230 | 19,2 |
| 35 | 240 | 20,0 |
| 40 | 245 | 20,4 |

> ⚠️ **ZU PRÜFEN (Audit):** LE-v150 bei 28 kn hier **150 W**, in der Vergleichstabelle (§2.3.2) jedoch **220 W**. Der Wert 150 W durchbricht den ansonsten monotonen Kurvenverlauf (200 W bei 25 kn → 230 W bei 30 kn) und entspricht zufällig der Nennleistung — vermutlich Übertragungsfehler. Ebenso überschreiten die Kurvenwerte ab 30 kn (bis 20,4 A) den angegebenen max. Ladestrom von 10 A (12V). Kurvenpunkte **estimated — unverifiziert** (Hersteller Leading Edge Power aufgelöst, keine belastbare Primärquelle).

#### Besondere Merkmale

- **Omnidirektional:** Keine Windnachführung, reagiert sofort auf Windrichtungsänderungen
- **Ultra-leise:** <40 dB(A) bis 20 kn, kaum über Hintergrundgeräusch
- **Keine Sturmregelung nötig:** Rotor begrenzt sich aerodynamisch
- **Keine Verletzungsgefahr:** Langsam drehend, keine freiliegenden Blattspitzen
- **Optisch ansprechend:** Skulpturales Design, kein „Windmühlen-Look"

#### Erfahrungswerte aus der Praxis

- Deutlich weniger Ertrag als vergleichbar bepreiste HAWT
- Ideal für Liveaboards in Marinas (Geräusch ist Nicht-Thema)
- Wartungsfrei über viele Jahre
- Hersteller nicht mehr aktiv — Ersatzteile problematisch
- Montage muss sehr stabil sein (hohes Eigengewicht + Kippmoment)

### 4.6 Primus Wind Power (Air Breeze / Air 40 / Air Silent X)

**Hersteller:** Primus Wind Power (ehemals Southwest Windpower), Flagstaff, USA
**Typ:** 3-Blatt Horizontalachser
**Marktposition:** Einstieg bis Mittelklasse, sehr weit verbreitet

#### Technische Daten (Air Silent X)

| Parameter | Wert |
|-----------|------|
| Nennleistung | 400 W (bei 28 kn) |
| Rotordurchmesser | 1,17 m |
| Blattmaterial | Carbon-Composite |
| Blattzahl | 3 |
| Generator | Permanentmagnet, bürstenlos |
| Anlaufgeschwindigkeit | 7 kn (3,6 m/s) |
| Nennwindgeschwindigkeit | 28 kn (14,4 m/s) |
| Überlebenswindgeschwindigkeit | 110 kn |
| Gewicht | 5,9 kg |
| Schutzart | IP54 |
| Spannung | 12V oder 24V |
| Max. Ladestrom | 27 A (12V) |
| Sturmregelung | Elektronische Bremse |
| Garantie | 3 Jahre |
| Preis (UVP 2025) | ca. €1.200 |

#### Leistungskurve (Air Silent X)

| Wind (kn) | Leistung (W) | Ladestrom 12V (A) |
|-----------|-------------|-------------------|
| 7 | 5 | 0,4 |
| 10 | 30 | 2,5 |
| 12 | 60 | 5,0 |
| 15 | 125 | 10,4 |
| 18 | 210 | 17,5 |
| 20 | 290 | 24,2 |
| 22 | 350 | 29,2 |
| 25 | 400 | 33,3 |
| 28 | 400 | 33,3 |
| 30 | 380 | 31,7 |
| 35 | 300 | 25,0 |

#### Besondere Merkmale (Modellhistorie)

- **Air Marine (1990er):** Erstes populäres Modell, berüchtigt für Lärm
- **Air-X (2000er):** Elektronische Bremse, immer noch laut
- **Air Breeze (2010er):** Leiser, Bluetooth-Monitoring
- **Air 40 (2015+):** Aktualisiertes Design, zuverlässiger
- **Air Silent X (2020+):** Carbon-Blätter, deutlich leiser, MPPT-Regler

#### Erfahrungswerte aus der Praxis

- Meistverkaufter Marine-Windgenerator weltweit (kumuliert)
- Ältere Modelle (Air-X) berüchtigt für Lärm und Regler-Ausfälle
- Aktuelle Silent X deutlich verbessert, aber immer noch lauter als Silentwind
- Leichtestes Gerät am Markt (5,9 kg) — ideal für schwache Montagestrukturen
- Ersatzteile und Service weltweit verfügbar
- Elektronische Bremse bei einigen Chargen fehlerhaft (Firmware-Update erforderlich)

### 4.7 Vergleichstabelle aller Modelle

| Kriterium | Superwind 350 | Rutland 1200 | Silentwind 400 | D400 | LE-v150 | Air Silent X |
|-----------|--------------|-------------|---------------|------|---------|-------------|
| Typ | 3-Blatt HAWT | 6-Blatt HAWT | 5-Blatt HAWT | 5-Blatt HAWT | Helical VAWT | 3-Blatt HAWT |
| Nennleistung | 350 W | 420 W | 400 W | 400 W | 150 W | 400 W |
| Gewicht | 7,5 kg | 9,5 kg | 8,2 kg | 8,0 kg | 12 kg | 5,9 kg |
| Anlauf | 7 kn | 5 kn | 6 kn | 7 kn | 6 kn | 7 kn |
| Geräusch 20 kn | 52 dB(A) | 50 dB(A) | 48 dB(A) | 56 dB(A) | 40 dB(A) | 54 dB(A) |
| Preis (ca.) | €2.200 | €1.400 | €2.600 | €1.800 | €1.800 | €1.200 |
| Garantie | 5 Jahre | 3 Jahre | 5 Jahre | 3 Jahre | 2 Jahre | 3 Jahre |
| Sturmregel. | Passiv (Pitch) | Elektronisch | Elektr. + Stall | Elektr. + Stall | Selbstbegr. | Elektronisch |
| Herkunft | Deutschland | England | Deutschland | England | England* | USA |
| Empfehlung | Blauwasser | Budget/Küste | Komfort/Leise | Allrounder | Ultra-leise | Budget/Leicht |

*Firma nicht mehr aktiv

---

## 5. Hersteller-Datenbank

### 5.1 Superwind GmbH

| Feld | Information |
|------|-------------|
| **Firma** | Superwind GmbH |
| **Sitz** | Brühl, Deutschland |
| **Gegründet** | 1993 |
| **Spezialisierung** | Premium-Marine-Windgeneratoren |
| **Produktpalette** | Superwind 350 (12V/24V) |
| **Website** | superwind.com |
| **Vertrieb** | Weltweit über Marine-Fachhändler |
| **Service** | Direkt ab Werk + autorisierte Servicepartner |
| **Zertifizierungen** | GL Renewable Certification, CE |
| **Besonderheit** | Einziger Hersteller mit passivem Pitch-System |
| **Ersatzteile** | 15+ Jahre Verfügbarkeit garantiert |
| **Zielgruppe** | Blauwassersegler, professionelle Marine |

### 5.2 Marlec Engineering Co Ltd (Rutland)

| Feld | Information |
|------|-------------|
| **Firma** | Marlec Engineering Co Ltd |
| **Sitz** | Corby, Northamptonshire, England |
| **Gegründet** | 1977 |
| **Spezialisierung** | Marine- und Landwind + Solar |
| **Produktpalette** | Rutland 1200, Rutland 504, Rutland FM910, Solarmodule |
| **Website** | marlec.co.uk |
| **Vertrieb** | Weltweit, stark in UK und Nordeuropa |
| **Service** | Direkt + Händlernetz |
| **Zertifizierungen** | CE, RoHS |
| **Besonderheit** | 6-Blatt-Design, guter Schwachwindstart |
| **Ersatzteile** | Gut verfügbar, Blätter einzeln |
| **Zielgruppe** | Küstensegler, Motorboote, Budget-bewusst |

### 5.3 Silentwind GmbH

| Feld | Information |
|------|-------------|
| **Firma** | Silentwind GmbH |
| **Sitz** | Jülich, Deutschland |
| **Gegründet** | 2012 |
| **Spezialisierung** | Leise Marine-Windgeneratoren |
| **Produktpalette** | Silentwind 400, Silentwind Pro, Hybrid-Regler |
| **Website** | silentwind.com |
| **Vertrieb** | Europa, zunehmend global |
| **Service** | Direkt ab Werk |
| **Zertifizierungen** | CE, GL-Typprüfung |
| **Besonderheit** | Coreless Generator, Hybrid-Regler, App-Steuerung |
| **Ersatzteile** | Verfügbar, Carbon-Blätter als Set |
| **Zielgruppe** | Komfort-orientierte Fahrtensegler, Liveaboards |

### 5.4 Eclectic Energy Ltd (D400)

| Feld | Information |
|------|-------------|
| **Firma** | Eclectic Energy Ltd |
| **Sitz** | Southwell, Nottinghamshire, England |
| **Gegründet** | 1996 |
| **Spezialisierung** | Marine-Windgeneratoren und Hydro-Generatoren |
| **Produktpalette** | D400 Wind, DuoGen (Wind + Hydro kombiniert) |
| **Website** | eclecticenergy.co.uk |
| **Vertrieb** | Global, stark bei Langfahrtseglern |
| **Service** | Direkt + internationale Partner |
| **Zertifizierungen** | CE |
| **Besonderheit** | DuoGen = einziges Wind/Hydro-Kombigerät |
| **Ersatzteile** | Verfügbar |
| **Zielgruppe** | Langfahrtsegler, Performance-Cruiser |

### 5.5 Primus Wind Power (Air-Reihe)

| Feld | Information |
|------|-------------|
| **Firma** | Primus Wind Power (ehem. Southwest Windpower) |
| **Sitz** | Flagstaff, Arizona, USA |
| **Gegründet** | 1987 (als Southwest Windpower) |
| **Spezialisierung** | Kompakte Windgeneratoren (Marine + Land) |
| **Produktpalette** | Air Silent X, Air 40, Air Breeze (Marine) |
| **Website** | primuswindpower.com |
| **Vertrieb** | Global, größter Marktanteil kumuliert |
| **Service** | USA direkt, international über Händler |
| **Zertifizierungen** | CE, UL-listed |
| **Besonderheit** | Leichtestes Gerät am Markt, weltweite Verbreitung |
| **Ersatzteile** | Hervorragend, überall erhältlich |
| **Zielgruppe** | Einstieg, Budget, leichte Montage |

### 5.6 LE-v (Leading Edge / Nachfolger)

| Feld | Information |
|------|-------------|
| **Firma** | Leading Edge Power Ltd (aufgelöst) / Pacific Sky Power (Nachfolger) |
| **Sitz** | UK (historisch) / Neuseeland (Nachfolger) |
| **Gegründet** | 2009 (LE) |
| **Spezialisierung** | Vertikalachs-Windgeneratoren |
| **Produktpalette** | LE-v50, LE-v80, LE-v150, LE-v300 |
| **Website** | — (historisch: leadingedgepower.com) |
| **Vertrieb** | Eingeschränkt, Restbestände über Händler |
| **Service** | Eingeschränkt |
| **Zertifizierungen** | CE (historisch) |
| **Besonderheit** | Helicaler VAWT, ultra-leise, omnidirektional |
| **Ersatzteile** | Problematisch (Firma aufgelöst) |
| **Zielgruppe** | Lärmsensible Installationen, Marina-Liegeplätze |

### 5.7 Hi-Q Windpower (Neuseeland)

| Feld | Information |
|------|-------------|
| **Firma** | Hi-Q Windpower |
| **Sitz** | Auckland, Neuseeland |
| **Gegründet** | 2015 |
| **Spezialisierung** | VAWT für Marine und Off-Grid |
| **Produktpalette** | Hi-Q 300, Hi-Q 500 |
| **Website** | hiqwindpower.com |
| **Vertrieb** | Pazifik, Australien, zunehmend global |
| **Service** | Direkt |
| **Zertifizierungen** | CE-konform |
| **Besonderheit** | Moderne helicale VAWT, marine-optimiert |
| **Ersatzteile** | Direkt ab Hersteller |
| **Zielgruppe** | Pazifik-Segler, VAWT-Interessenten |

### 5.8 Hersteller-Bewertungsmatrix

| Hersteller | Qualität | Service | Ersatzteile | Preis/Leist. | Innovation | Langlebigkeit |
|------------|----------|---------|-------------|-------------|------------|---------------|
| Superwind | ★★★★★ | ★★★★★ | ★★★★★ | ★★★★ | ★★★★ | ★★★★★ |
| Marlec/Rutland | ★★★★ | ★★★★ | ★★★★ | ★★★★★ | ★★★ | ★★★★ |
| Silentwind | ★★★★★ | ★★★★ | ★★★★ | ★★★★ | ★★★★★ | ★★★★ |
| Eclectic/D400 | ★★★★ | ★★★★ | ★★★★ | ★★★★ | ★★★ | ★★★★ |
| Primus/Air | ★★★ | ★★★ | ★★★★★ | ★★★★★ | ★★★ | ★★★ |
| LE-v/Pacific Sky | ★★★★ | ★★ | ★★ | ★★★ | ★★★★★ | ★★★★ |
| Hi-Q | ★★★★ | ★★★ | ★★★ | ★★★ | ★★★★ | ★★★ (zu neu) |

---

## 6. Fehlerbild-Atlas

### 6.1 Fehlerbild: Lagerschaden

| Feld | Information |
|------|-------------|
| **Bezeichnung** | Lagerschaden / Lagerverschleiß |
| **Code** | WG-F01 |
| **Häufigkeit** | 25% aller Windgenerator-Defekte |
| **Betroffene Modelle** | Alle, besonders nach 4+ Jahren |
| **Symptome** | Schleifgeräusche bei niedriger Drehzahl, rauer Lauf, Spiel in der Rotorachse, erhöhte Vibration |
| **Ursachen** | Korrosion (Salzwasser-Einbruch), mangelnde Schmierung, Überlastung bei Sturm, Alterung der Dichtungen |
| **Diagnose** | Rotor von Hand drehen: Rasten, Schleifen, Spiel fühlbar. Axialspiel >0,1mm = Wechsel nötig |
| **Sofortmaßnahme** | Generator bremsen, bei starkem Spiel: abbauen |
| **Reparatur** | Lagerwechsel (Spezialwerkzeug), Dichtungen erneuern, Lagerpassung prüfen |
| **Kosten** | €80–€250 (Material), €100–€300 (Arbeit wenn Werft) |
| **Prävention** | Jährliche Inspektion, rechtzeitig tauschen bei erstem Geräusch, Schutzkappe/Nasenschutz |
| **Confidence** | documented |

### 6.2 Fehlerbild: Blattbruch

| Feld | Information |
|------|-------------|
| **Bezeichnung** | Rotorblattbruch / Blattverlust |
| **Code** | WG-F02 |
| **Häufigkeit** | 8% aller Defekte, aber mit höchstem Schadenspotential |
| **Betroffene Modelle** | Besonders Nylon-Blätter (Rutland), UV-gealterte GFK-Blätter |
| **Symptome** | Plötzliche starke Unwucht-Vibration, fehlende Blattabschnitte, Generator schlägt aus |
| **Ursachen** | UV-Degradation, Ermüdung, Fremdkörper-Einschlag (Leinen, Vogel), Material-Defekt, Überdreh-Ereignis |
| **Diagnose** | Sichtprüfung: Risse, Verfärbung, Delamination. Klopftest: dumpfer Klang = Delamination |
| **Sofortmaßnahme** | SOFORT bremsen! Unwuchtiger Rotor kann Montagehalter abbrechen. Absichern gegen Weiterbetrieb |
| **Reparatur** | Kompletter Blattsatz tauschen (immer alle Blätter gleichzeitig für Balance). Montagehalter auf Risse prüfen |
| **Kosten** | €150–€500 (Blattsatz je nach Modell) |
| **Prävention** | Jährliche UV-Inspektion, Blätter alle 5–7 Jahre präventiv tauschen, Schutzbeschichtung |
| **Confidence** | documented |

### 6.3 Fehlerbild: Vibration am Mast/Halter

| Feld | Information |
|------|-------------|
| **Bezeichnung** | Strukturvibration / Resonanz-Schwingung |
| **Code** | WG-F03 |
| **Häufigkeit** | 35% aller Beschwerden (häufigste Beschwerde überhaupt) |
| **Betroffene Modelle** | Alle, stark abhängig von Montage |
| **Symptome** | Brummen/Dröhnen im Schiffsinneren, spürbare Vibration an Halter/Mast, Geräusch bei bestimmter Drehzahl deutlich lauter |
| **Ursachen** | Eigenfrequenz des Halters liegt im Betriebsdrehzahlbereich (Resonanz), zu langer/dünner Halter, fehlende Abspannung, lose Verbindungen |
| **Diagnose** | Resonanz-Test: Handklopfen am Halter → Eigenfrequenz spüren. Drehzahl-Sweep: bei welcher Windstärke am schlimmsten? |
| **Sofortmaßnahme** | Drehzahlbegrenzung per Regler auf Drehzahl unterhalb Resonanz |
| **Reparatur** | Halter verstärken/kürzen, Abspannung hinzufügen, Schwingungsdämpfer montieren, Gummipuffer am Fußpunkt |
| **Kosten** | €50–€500 je nach Maßnahme |
| **Prävention** | Vor Installation: Eigenfrequenz-Berechnung oder -Messung. Halter gemäß Herstellervorgabe dimensionieren |
| **Confidence** | documented |

### 6.4 Fehlerbild: Regler-Defekt

| Feld | Information |
|------|-------------|
| **Bezeichnung** | Laderegler-Ausfall / Regler-Fehlfunktion |
| **Code** | WG-F04 |
| **Häufigkeit** | 15% aller Defekte |
| **Betroffene Modelle** | Alle mit elektronischer Sturmregelung, besonders Primus Air (ältere Firmware) |
| **Symptome** | Keine Ladung trotz drehendem Rotor, Überspannung an Batterie, Bremse löst nicht aus bei Sturm, Bremse löst ständig aus (Fehlauslösung) |
| **Ursachen** | Überspannung (Kabelbruch bei Last), Feuchtigkeit in Regler-Gehäuse, Blitzeinschlag (induziert), Überhitzung, Firmware-Bug |
| **Diagnose** | Spannung am Generator-Ausgang messen (3-Phasen-AC). Spannung am Regler-Ausgang messen. Vergleich → Regler defekt wenn Input OK aber Output falsch |
| **Sofortmaßnahme** | Generator manuell kurzschließen (Bremse), Regler abklemmen, Batterie prüfen |
| **Reparatur** | Regler tauschen. Bei Überspannungsschaden: auch Batterie-Schutz prüfen |
| **Kosten** | €150–€500 (Regler je nach Modell) |
| **Prävention** | Regler spritzwassergeschützt montieren, Überspannungsschutz (Varistor) am Eingang, Firmware aktuell halten |
| **Confidence** | documented |

### 6.5 Fehlerbild: Überdrehzahl / Runaway

| Feld | Information |
|------|-------------|
| **Bezeichnung** | Überdrehzahl / Durchgehen des Rotors |
| **Code** | WG-F05 |
| **Häufigkeit** | 5% — selten, aber gefährlichstes Szenario |
| **Betroffene Modelle** | Alle ohne passive Pitch-Regelung, wenn Bremse versagt |
| **Symptome** | Extrem hohe Drehzahl, Heulen/Kreischen, Generator überhitzt, Montage vibriert extrem |
| **Ursachen** | Bremse defekt bei Sturm, Kabelbruch zum Regler (Leerlauf), Regler-Ausfall bei Starkwind, Batterie voll ohne Dump-Load |
| **Diagnose** | Drehzahl offensichtlich über Normal, Geräusch extrem, Generator heiß |
| **Sofortmaßnahme** | WARNUNG: Niemals in den Rotor greifen! Generator-Kabel manuell kurzschließen (3 Phasen verbinden). Falls nicht möglich: Sicherheitsabstand halten, abwarten |
| **Reparatur** | Nach Runaway: Lager prüfen (oft beschädigt), Wicklung prüfen (Überhitzung), Magnete prüfen (Entmagnetisierung bei >150°C), Blätter prüfen (Verformung) |
| **Kosten** | €200–€1.500 (oft Totalschaden bei längerem Runaway) |
| **Prävention** | Redundante Bremse (mechanisch + elektronisch), Kurzschluss-Schalter an Deck, Sturm-SOP erstellen, Dump-Load für volle Batterie |
| **Confidence** | documented |

### 6.6 Fehlerbild: Korrosion

| Feld | Information |
|------|-------------|
| **Bezeichnung** | Korrosion an Generator, Halter oder Befestigung |
| **Code** | WG-F06 |
| **Häufigkeit** | 20% aller Langzeitprobleme |
| **Betroffene Modelle** | Alle, besonders bei unzureichender Materialwahl |
| **Symptome** | Weiße/braune Ablagerungen an Schrauben, festgefressene Verbindungen, Kontaktkorrosion an Kabelanschlüssen, Lochfraß am Halter |
| **Ursachen** | Galvanische Korrosion (Aluminium + Edelstahl ohne Isolation), Salzwasser-Exposition, mangelnde Versiegelung der Verbindungen, falsche Schrauben (A2 statt A4) |
| **Diagnose** | Sichtprüfung aller Metallverbindungen, Schrauben auf Gängigkeit, Kabelanschlüsse auf Übergangswiderstand |
| **Sofortmaßnahme** | Lose/korrodierte Verbindungen sichern, Kontakte reinigen |
| **Reparatur** | Korrodierte Schrauben durch A4/316L ersetzen, Kontaktflächen isolieren (DuralacCompound), Kabelschuhe erneuern, Halter ggf. tauschen |
| **Kosten** | €50–€300 |
| **Prävention** | Nur A4/316L-Schrauben verwenden, Duralac auf Al/SS-Kontaktstellen, Schrumpfschlauch auf Kabelschuhen, jährliche Inspektion |
| **Confidence** | documented |

### 6.7 Fehlerbild: Windnachführung blockiert

| Feld | Information |
|------|-------------|
| **Bezeichnung** | Gierlager blockiert / Windfahne defekt |
| **Code** | WG-F07 |
| **Häufigkeit** | 12% aller HAWT-Defekte |
| **Betroffene Modelle** | Alle HAWT (nicht relevant für VAWT) |
| **Symptome** | Generator dreht sich nicht in den Wind, steht quer, deutlich reduzierter Ertrag, asymmetrische Geräusche |
| **Ursachen** | Gierlager korrodiert/verklemmt, Kabelwicklung blockiert Drehung, Heckflosse abgebrochen/verbogen, Salzablagerung im Drehlager |
| **Diagnose** | Von Hand: dreht sich Generator-Kopf frei auf dem Montagerrohr? Kabel verdrillt? Heckflosse intakt? |
| **Sofortmaßnahme** | Manuell in Windrichtung drehen, Kabelwicklung lösen |
| **Reparatur** | Gierlager reinigen/fetten, Kabel mit Schleifring nachrüsten oder Drehbegrenzung einbauen, Heckflosse ersetzen |
| **Kosten** | €30–€200 |
| **Prävention** | Jährlich Gierlager schmieren, Kabelführung mit ausreichend Schlaufe, Drehbegrenzer installieren |
| **Confidence** | documented |

### 6.8 Fehlerbild: Generator-Wicklungsschaden

| Feld | Information |
|------|-------------|
| **Bezeichnung** | Stator-Wicklungsschaden / Phasenschluss / Windungsschluss |
| **Code** | WG-F08 |
| **Häufigkeit** | 5% — selten, aber kostspielig |
| **Betroffene Modelle** | Alle, besonders nach Überdrehzahl-Ereignis oder Wassereintritt |
| **Symptome** | Reduzierte Leistung, ungleichmäßige 3-Phasen-Spannung, Generator wird asymmetrisch warm, Wicklungsgeruch |
| **Ursachen** | Überhitzung durch Runaway, Wassereintritt durch defekte Dichtung, Isolationsalterung, mechanische Beschädigung |
| **Diagnose** | 3-Phasen-Widerstand messen: alle drei Phasen müssen gleich sein (±5%). Isolationswiderstand gegen Gehäuse >10 MΩ. |
| **Sofortmaßnahme** | Generator stilllegen |
| **Reparatur** | Generaltausch des Generators oder Neuwicklung (selten wirtschaftlich bei kleinen Einheiten) |
| **Kosten** | €400–€1.200 (Austausch-Generator) |
| **Prävention** | Runaway vermeiden (Bremse!), Dichtungen regelmäßig prüfen, Kondenswasser-Drainage offenhalten |
| **Confidence** | documented |

### 6.9 Fehlerbild: Kabel-/Anschlussprobleme

| Feld | Information |
|------|-------------|
| **Bezeichnung** | Kabelbruch, Kontaktkorrosion, Übergangswiderstand |
| **Code** | WG-F09 |
| **Häufigkeit** | 18% aller Störungen |
| **Betroffene Modelle** | Alle |
| **Symptome** | Intermittierender Ertrag, Ladung setzt bei bestimmter Windrichtung aus (Kabel gespannt), reduzierte Spannung am Regler vs. am Generator, Wärme an Klemmen |
| **Ursachen** | Vibration bricht Litzen, UV-Degradation der Isolation, Korrosion an Schraubklemmen, zu dünner Querschnitt → Überhitzung |
| **Diagnose** | Spannungsmessung Generator vs. Regler-Eingang. Differenz >0,5V bei Last = Problem. Sichtprüfung aller Klemmen/Stecker |
| **Sofortmaßnahme** | Verbindung reinigen, nachziehen |
| **Reparatur** | Kabel neu verlegen (UV-geschützt, vibrationsfest), Kabelschuhe crimpen + löten, Schrumpfschlauch, ausreichenden Querschnitt wählen |
| **Kosten** | €50–€200 |
| **Prävention** | Marine-Kabel verwenden (verzinnte Litzen), Kabelschuhe crimpen + löten + Schrumpfschlauch, Zugentlastung, UV-Schutz |
| **Confidence** | documented |

### 6.10 Fehlerbild: Magnetentmagnetisierung

| Feld | Information |
|------|-------------|
| **Bezeichnung** | Permanentmagnet-Schwächung / Entmagnetisierung |
| **Code** | WG-F10 |
| **Häufigkeit** | 3% — selten |
| **Betroffene Modelle** | Alle Permanentmagnet-Generatoren |
| **Symptome** | Schleichender Leistungsverlust über Monate/Jahre, Generator dreht schneller für gleiche Spannung, Leerlaufspannung bei gegebener Drehzahl gesunken |
| **Ursachen** | Überhitzung >150°C (Runaway), starke externe Magnetfelder, Alterung (NdFeB: ~1% Verlust pro 10 Jahre bei normaler Temperatur), Korrosion der Magnetbeschichtung |
| **Diagnose** | Leerlaufspannung bei definierter Drehzahl messen und mit Neuwert vergleichen. >15% Abweichung = relevant |
| **Sofortmaßnahme** | Keine akute Gefahr, Generator kann weiterlaufen |
| **Reparatur** | Generator-Austausch (Neumagnisierung nur im Werk möglich und selten angeboten) |
| **Kosten** | €400–€1.200 |
| **Prävention** | Runaway-Schutz (= Überhitzungsschutz), Generator nicht in der Nähe starker Magnete lagern |
| **Confidence** | documented |

### 6.11 Fehlerbild: Bremssystem-Versagen

| Feld | Information |
|------|-------------|
| **Bezeichnung** | Bremse löst nicht aus / Bremse hält nicht |
| **Code** | WG-F11 |
| **Häufigkeit** | 10% aller Störungen, kritisch bei Sturm |
| **Betroffene Modelle** | Alle mit elektronischer Bremse, besonders ältere Primus/Air |
| **Symptome** | Generator dreht bei Sturm ungebremst, manueller Bremsschalter ohne Wirkung, Bremswiderstand überhitzt |
| **Ursachen** | MOSFET im Regler durchgebrannt, Kabelbruch in Bremsleitung, Bremsschalter korrodiert, Bremswiderstand defekt |
| **Diagnose** | Kurzschluss-Test: Generator-Phasen manuell kurzschließen (Krokodilklemmen bei Stillstand anlegen, dann Wind). Generator muss bremsen. Falls nicht: Wicklungsschaden |
| **Sofortmaßnahme** | Manuelle 3-Phasen-Kurzschlussbrücke direkt am Generator anlegen |
| **Reparatur** | Regler tauschen, Bremsschalter erneuern, Bremswiderstand prüfen/tauschen |
| **Kosten** | €100–€500 |
| **Prävention** | Jährlicher Bremsen-Funktionstest, redundanter manueller Kurzschlussschalter an Deck, korrosionsfreie Schalter (IP67) |
| **Confidence** | documented |

### 6.12 Fehlerbild: Heckflosse / Nacelle-Schaden

| Feld | Information |
|------|-------------|
| **Bezeichnung** | Heckflosse abgebrochen / Gondel-Gehäuse gerissen |
| **Code** | WG-F12 |
| **Häufigkeit** | 7% — wetterabhängig |
| **Betroffene Modelle** | Alle HAWT mit separater Heckflosse |
| **Symptome** | Generator richtet sich nicht mehr in den Wind aus, Teile am Deck/im Wasser, asymmetrischer Lauf |
| **Ursachen** | Sturm-Überlastung, UV-Versprödung des Kunststoffs, Ermüdungsbruch an Befestigung, Vandalismus |
| **Diagnose** | Sichtprüfung |
| **Sofortmaßnahme** | Generator manuell in den Wind drehen und fixieren (provisorische Heckflosse aus Sperrholz) |
| **Reparatur** | Ersatz-Heckflosse montieren, Nacelle-Gehäuse bei Riss abdichten oder tauschen |
| **Kosten** | €50–€200 (Heckflosse), €200–€500 (Nacelle) |
| **Prävention** | UV-Schutzbeschichtung, jährliche Sichtprüfung auf Risse, bei Sturm: Generator bremsen |
| **Confidence** | documented |

---

## 7. Troubleshooting-Entscheidungsbäume

### 7.1 Entscheidungsbaum: Kein Ertrag / Keine Ladung

```
START: Windgenerator liefert keine Ladung
│
├─ Dreht der Rotor?
│  ├─ NEIN
│  │  ├─ Ist Bremse aktiviert?
│  │  │  ├─ JA → Bremse lösen (Schalter, Regler-Einstellung)
│  │  │  └─ NEIN
│  │  │     ├─ Ist Wind vorhanden (>8 kn)?
│  │  │     │  ├─ NEIN → Kein Fehler, zu wenig Wind
│  │  │     │  └─ JA
│  │  │     │     ├─ Gierlager blockiert? → WG-F07
│  │  │     │     ├─ Rotor mechanisch blockiert? → Fremdkörper (Leine, Netz)
│  │  │     │     └─ Lager festgefressen? → WG-F01
│  │  └─ [Rotor dreht nicht → mechanisches Problem]
│  │
│  └─ JA (Rotor dreht, aber keine Ladung)
│     ├─ Spannung am Generator messen (3-Phasen AC)
│     │  ├─ Keine Spannung
│     │  │  ├─ Kabelbruch zwischen Generator und Messpunkt → WG-F09
│     │  │  └─ Wicklungsschaden → WG-F08
│     │  │
│     │  ├─ Spannung vorhanden, aber asymmetrisch (>10% Abweichung)
│     │  │  └─ Wicklungsschaden (1 Phase defekt) → WG-F08
│     │  │
│     │  └─ Spannung vorhanden und symmetrisch
│     │     ├─ Spannung am Regler-Eingang messen
│     │     │  ├─ Deutlich weniger als am Generator
│     │     │  │  └─ Kabelprobleme → WG-F09
│     │     │  └─ Spannung OK am Regler-Eingang
│     │     │     ├─ Regler-Ausgang messen (DC)
│     │     │     │  ├─ Keine DC-Ausgangsspannung
│     │     │     │  │  └─ Regler defekt → WG-F04
│     │     │     │  └─ DC-Spannung vorhanden
│     │     │     │     ├─ Batterie-Spannung prüfen
│     │     │     │     │  ├─ Batterie voll (>14,4V/12V-System)
│     │     │     │     │  │  └─ Kein Fehler! Batterie ist geladen
│     │     │     │     │  └─ Batterie nicht voll
│     │     │     │     │     └─ Sicherung/Trennschalter zwischen Regler und Batterie prüfen
│     │     │     │     └─ [Fehlerlokalisierung zwischen Regler und Batterie]
│     │     └─ [Spannung OK → Problem liegt im Regler oder dahinter]
│
└─ [Ende Diagnose]
```

### 7.2 Entscheidungsbaum: Übermäßige Vibration

```
START: Windgenerator vibriert stark
│
├─ Vibration bei ALLEN Windstärken oder nur bei BESTIMMTER?
│  │
│  ├─ Bei BESTIMMTER Windstärke deutlich schlimmer (Resonanz-typisch)
│  │  ├─ Bei welcher Windstärke? → Betriebsdrehzahl ermitteln
│  │  ├─ Eigenfrequenz des Halters liegt im Anregungsbereich → WG-F03
│  │  ├─ Maßnahmen:
│  │  │  ├─ Kurzfristig: Drehzahlbegrenzung per Regler auf Bereich unterhalb Resonanz
│  │  │  ├─ Mittelfristig: Halter verstärken / kürzen / abspannen
│  │  │  └─ Langfristig: Montagesystem redesignen
│  │  └─ [Resonanz → strukturelles Problem]
│  │
│  └─ Bei ALLEN Windstärken (steigt mit Drehzahl)
│     ├─ Plötzlich aufgetreten oder schleichend?
│     │  │
│     │  ├─ PLÖTZLICH
│     │  │  ├─ Blätter auf Beschädigung prüfen → WG-F02
│     │  │  ├─ Eisansatz auf Blättern? → Abtauen lassen, nicht im Betrieb!
│     │  │  ├─ Fremdkörper am Rotor? → Entfernen (bei Stillstand!)
│     │  │  └─ Schrauben am Halter gelöst? → Nachziehen
│     │  │
│     │  └─ SCHLEICHEND (über Wochen/Monate)
│     │     ├─ Lagerverschleiß → WG-F01
│     │     ├─ Blatt-Unwucht durch UV-Degradation (unterschiedliche Verformung) → WG-F02
│     │     ├─ Montagehalter ermüdet (Risse) → Halter prüfen
│     │     └─ Schraubverbindungen gelockert → Alle Schrauben prüfen/nachziehen
│     │
│     └─ [Unwucht oder Lager → mechanisches Problem]
│
└─ [Ende Diagnose]
```

### 7.3 Entscheidungsbaum: Übermäßiges Geräusch

```
START: Windgenerator ist zu laut
│
├─ Geräuschcharakter bestimmen:
│  │
│  ├─ ZISCHEN / RAUSCHEN (hochfrequent)
│  │  ├─ Normal für HAWT bei >18 kn (Blattspitzengeräusch)
│  │  ├─ Ungewöhnlich laut? → Blätter auf Beschädigung/Rauigkeit prüfen
│  │  ├─ Maßnahmen:
│  │  │  ├─ Drehzahlbegrenzung (Leistungsverlust!)
│  │  │  ├─ Blätter mit Winglets nachrüsten (falls verfügbar)
│  │  │  └─ Modellwechsel auf leiseren Typ (Silentwind, VAWT)
│  │  └─ [Aerodynamisches Geräusch → konstruktionsbedingt]
│  │
│  ├─ BRUMMEN / DRÖHNEN (niederfrequent)
│  │  ├─ Körperschall-Übertragung über Montagestruktur → WG-F03
│  │  ├─ Resonanz des Montagemastes
│  │  ├─ Maßnahmen:
│  │  │  ├─ Gummipuffer am Montage-Fußpunkt
│  │  │  ├─ Halter verstärken/abspannen
│  │  │  └─ Entkopplungselemente zwischen Generator und Halter
│  │  └─ [Struktur-übertragenes Geräusch]
│  │
│  ├─ SCHLEIFEN / KRATZEN
│  │  ├─ Lagerschaden → WG-F01
│  │  ├─ Rotor schleift am Gehäuse (Spiel/Verformung)
│  │  └─ Fremdkörper im Generator-Inneren
│  │
│  ├─ KLAPPERN / SCHLAGEN
│  │  ├─ Lose Blattbefestigung → Schrauben prüfen
│  │  ├─ Heckflosse lose → WG-F12
│  │  ├─ Halterung klappert → Alle Verbindungen nachziehen
│  │  └─ Blatt hat Spiel auf Nabe → Buchsen prüfen
│  │
│  └─ HEULEN / KREISCHEN (steigende Tonhöhe)
│     ├─ Überdrehzahl → WG-F05 — SOFORT BREMSEN!
│     ├─ Bremse defekt → WG-F11
│     └─ [Gefährlicher Zustand → sofortige Aktion]
│
└─ [Ende Diagnose]
```

### 7.4 Entscheidungsbaum: Reduzierter Ertrag

```
START: Windgenerator liefert weniger als erwartet
│
├─ Wie viel weniger? Vergleich mit Leistungskurve des Herstellers
│  │
│  ├─ Ertrag < 50% der Herstellerangabe
│  │  ├─ Windmessung am Generator-Standort (nicht am Masttop!)
│  │  │  ├─ Tatsächlicher Wind deutlich weniger als angenommen?
│  │  │  │  ├─ JA → Abschattung durch Segel, Bimini, Nachbarschiff
│  │  │  │  │  → Standort suboptimal (zu niedrig, Lee-Seite)
│  │  │  │  └─ NEIN → weiter diagnostizieren
│  │  │  └─ [Wind am Generator prüfen, nicht am Anemometer am Masttop!]
│  │  │
│  │  ├─ Generator richtet sich in den Wind aus?
│  │  │  ├─ NEIN → WG-F07 (Gierlager blockiert)
│  │  │  └─ JA → weiter
│  │  │
│  │  ├─ Leerlaufspannung bei bekannter Drehzahl prüfen
│  │  │  ├─ Deutlich niedriger als Neuwert → WG-F10 (Magnetentmagnetisierung) oder WG-F08
│  │  │  └─ Normal → Problem liegt hinter dem Generator
│  │  │
│  │  └─ Regler-Effizienz prüfen (Eingangsleistung vs. Ausgangsleistung)
│  │     ├─ Großer Verlust im Regler → WG-F04
│  │     └─ Kabelversluste → WG-F09
│  │
│  └─ Ertrag 50–80% der Herstellerangabe
│     ├─ Normal für reale Bedingungen (Herstellerangaben oft optimistisch)
│     ├─ Apparent-Wind-Effekt bei Vorwindkurs? → Normal, siehe 2.8
│     ├─ Batterie fast voll? (Ladekurve → weniger Strom bei hoher Spannung) → Normal
│     ├─ Blätter verschmutzt (Salzverkrustung, Vogelkot)? → Reinigen
│     └─ Blätter UV-gealtert (rau, matt)? → Polieren oder tauschen
│
└─ [Ende Diagnose]
```

### 7.5 Entscheidungsbaum: Sturm-Vorbereitung

```
START: Sturm angekündigt (>35 kn erwartet)
│
├─ Generatortyp bestimmen:
│  │
│  ├─ HAWT mit passiver Pitch-Regelung (Superwind)
│  │  ├─ System ist selbstschützend bis ~60 kn
│  │  ├─ Trotzdem empfohlen bei >45 kn: elektronische Bremse aktivieren
│  │  ├─ Bei >60 kn: Generator abbauen oder Blätter demontieren
│  │  └─ Montagehalter auf festen Sitz prüfen
│  │
│  ├─ HAWT mit elektronischer Bremse (Rutland, Air, D400, Silentwind)
│  │  ├─ <40 kn erwartet:
│  │  │  ├─ Bremse aktivieren → OK
│  │  │  └─ Alternativ: Drehzahlbegrenzung per Regler
│  │  ├─ >40 kn erwartet:
│  │  │  ├─ Bremse aktivieren UND
│  │  │  ├─ Manuellen Kurzschlussschalter als Backup sicherstellen
│  │  │  └─ Optional: Blätter demontieren (sicherste Option)
│  │  ├─ >60 kn erwartet (Hurrikan/Zyklon):
│  │  │  ├─ Generator ABBAUEN oder Blätter entfernen
│  │  │  ├─ Montagehalter ggf. kürzen/einklappen
│  │  │  └─ Kabel sichern
│  │  └─ [Elektronische Bremse allein nicht für Überlebensbedingungen ausreichend]
│  │
│  ├─ VAWT (Leading Edge, Hi-Q)
│  │  ├─ Selbstbegrenzend, generell sturmfest
│  │  ├─ <60 kn: Normalbetrieb möglich (Generator begrenzt sich)
│  │  ├─ >60 kn: Empfehlung trotzdem bremsen wenn möglich
│  │  └─ Montagehalter prüfen (VAWT haben hohes Kippmoment bei Sturm)
│  │
│  └─ ALLE Typen:
│     ├─ Montage-Schrauben nachziehen
│     ├─ Abspannung (falls vorhanden) prüfen
│     ├─ Kabel auf Scheuerstellen prüfen
│     ├─ Dump-Load prüfen (Batterie wird schnell voll wenn Verbraucher ausgeschaltet)
│     └─ Bremsfunktion VOR dem Sturm testen!
│
└─ [Ende Checkliste]
```

---

## 8. FAQ — Häufige Fragen

### 8.1 Grundsatzfragen

**F01: Lohnt sich ein Windgenerator auf einer Yacht?**
Ja, wenn mindestens zwei der folgenden Bedingungen zutreffen: (a) >60 Seetage/Jahr, (b) Ankerlieger ohne Landstrom, (c) Fahrtgebiet mit zuverlässigem Wind (Passat, Nordsee), (d) Solaranlage allein deckt den Bedarf nicht (Winter, hohe Breiten). Ein Windgenerator ist KEIN Ersatz für Solar, sondern eine Ergänzung. Die Kombination beider Systeme bietet die höchste Autonomie.

**F02: Horizontal- oder Vertikalachser — was ist besser?**
Für maximalen Ertrag pro Euro: Horizontalachser (HAWT). Für maximale Ruhe: Vertikalachser (VAWT). Für Blauwasser, wo Ertrag kritisch ist: HAWT. Für Marina-Liegeplätze und Liveaboards mit Geräuschsensibilität: VAWT. Für die meisten Fahrtensegler ist ein qualitativ hochwertiger HAWT (Superwind, Silentwind) der beste Kompromiss.

**F03: Wie viel Strom erzeugt ein Windgenerator realistisch?**
Realistisch (nicht Herstellerversprechen): Ein 400W-Generator erzeugt im Jahresmittel 50–150 Ah/Tag bei 12V in einem guten Windrevier. In der Karibik/Passat: 80–200 Ah/Tag. Im Mittelmeer Sommer: 30–80 Ah/Tag. Diese Werte berücksichtigen windstille Phasen, Apparent-Wind-Verluste und Systemverluste.

**F04: Ab welcher Windstärke erzeugt ein Windgenerator Strom?**
Die meisten HAWT beginnen bei 6–8 kn zu drehen und liefern ab 8–10 kn nennenswerten Ladestrom (>1A bei 12V). Der wirtschaftlich relevante Bereich beginnt ab ca. 12 kn. Unter 10 kn ist der Ertrag vernachlässigbar.

**F05: Kann ein Windgenerator den Dieselgenerator ersetzen?**
In Passatregionen bei moderatem Verbrauch: Ja, zusammen mit Solar. In gemäßigten Breiten: Teilweise. Generell gilt: Wind + Solar reduzieren den Generator-Betrieb um 70–90%, eliminieren ihn aber nur bei optimalen Bedingungen komplett. Für Hochverbraucher (Klimaanlage, Wassermacher >60L/h) bleibt ein Generator nötig.

### 8.2 Dimensionierung und Auswahl

**F06: Welche Generatorgröße brauche ich?**
Faustformel: Nennleistung [W] = Tagesbedarf [Ah] × 14V / (CF × 24h). Beispiel: 200 Ah/Tag Bedarf, CF=0,20 → 200×14/(0,20×24) = 583W → mindestens 400W-Klasse plus Solar.

**F07: 12V oder 24V System — was passt besser?**
12V: Boote <14m, <400Ah Kapazität. Vorteil: einfacher, mehr Geräteauswahl. 24V: Boote >14m, >400Ah Kapazität. Vorteil: halbierter Strom = dünnere Kabel, weniger Verluste. Bei >5m Kabellänge Generator→Regler ist 24V deutlich vorteilhafter.

**F08: Wie groß muss der Rotordurchmesser sein?**
1,0–1,2m ist der Sweet Spot für Yachten. Kleiner (<0,8m) bringt zu wenig Ertrag. Größer (>1,3m) wird mechanisch problematisch (Gewicht, Vibration, Sicherheitsabstand). Die meisten Marine-Generatoren haben 1,0–1,2m Durchmesser.

**F09: Brauche ich einen separaten Laderegler?**
JA, immer. Ein Windgenerator liefert variable 3-Phasen-Wechselspannung, die gleichgerichtet und geregelt werden muss. Der Regler schützt außerdem die Batterie vor Überladung und den Generator vor Überdrehzahl. Manche Generatoren (Silentwind, Rutland) inkludieren den Regler, bei anderen (Superwind, D400) muss er separat erworben werden.

**F10: Welchen Kabelquerschnitt brauche ich?**
Richtwert: Spannungsfall <3% bei Nennstrom. Bei 12V, 25A, 8m Kabellänge (einfach): mindestens 10mm² (besser 16mm²). Bei 24V, 12A, 8m: mindestens 6mm² (besser 10mm²). Immer verzinnte Kupferlitze verwenden.

### 8.3 Montage

**F11: Wo montiere ich den Windgenerator am besten?**
Priorität: (1) Heckarch/Davit-Arch — bester Kompromiss aus Höhe, Zugänglichkeit und Abstand zu Personen. (2) Dedizierter Mast am Heck — höher, aber aufwändiger. (3) Heckkorb-Verlängerung — einfach, aber oft zu niedrig. (4) Masttop — maximaler Wind, aber Wartung unmöglich und Vibration überträgt sich auf ganzes Rigg. Empfehlung: Mindestens 2m über Deckshöhe, mindestens 2m Abstand zu Aufenthaltsbereich.

**F12: Welches Rohr für die Montage?**
Standard: 48,3mm Außendurchmesser (1,5" Schedule 40). Material: Edelstahl 316L oder Aluminium 6082-T6. Wandstärke: mindestens 3mm (Edelstahl) oder 4mm (Aluminium). Länge: so kurz wie möglich für Vibration, so lang wie nötig für Windfreiheit. Typisch: 1,5–2,5m freie Länge.

**F13: Muss der Windgenerator abgespannt werden?**
Ab 2m freier Rohrlänge: Empfohlen. Ab 2,5m: Dringend empfohlen bis zwingend. Abspannung (2–3 Stages mit Dyneema oder Draht) erhöht die Eigenfrequenz dramatisch und reduziert Vibration. Stages am oberen Drittel des Rohres befestigen.

**F14: Wie halte ich den Sicherheitsabstand ein?**
Mindestens 1,5m Abstand zwischen Rotorteller und nächstem erreichbaren Punkt (Personen, Leinen, Segel). Bei Kindern an Bord: 2m+. Den Rotorteller gedanklich als Scheibe visualisieren — nichts darf in diesen Bereich ragen (auch nicht Schoten oder Fallen).

**F15: Kann ich den Generator am Hauptmast montieren?**
Technisch möglich (Masttop-Montage), aber problematisch: (a) Vibration überträgt sich auf Rigg und Rumpf, (b) Wartung erfordert Aufentern, (c) Masttop ist bereits belegt (Anemometer, Antennen, Tricolor), (d) Gewicht oben verschlechtert Stabilität. Nur empfohlen, wenn kein anderer Standort möglich ist.

### 8.4 Betrieb und Wartung

**F16: Was muss regelmäßig gewartet werden?**
Jährlich: Sichtprüfung Blätter (UV-Schäden, Risse), Schrauben nachziehen, Kabelanschlüsse prüfen, Gierlager schmieren (HAWT), Bremsfunktion testen. Alle 3–5 Jahre: Blätter auf Unwucht prüfen, Lager horchen/fühlen. Alle 5–8 Jahre: Lager präventiv tauschen, Blätter bei Bedarf erneuern.

**F17: Wie bremse ich den Generator bei Wartung?**
Standardmethode: Kurzschluss der 3 Generator-Phasen. Bei den meisten Modellen über einen Schalter am Regler oder einen separaten Kurzschlussschalter. WICHTIG: Erst bremsen, dann arbeiten. Nie in einen drehenden Rotor greifen. Bei hohem Wind: Rotor kann auch gebremst noch langsam drehen — abwarten bis Stillstand.

**F18: Mein Generator macht plötzlich komische Geräusche — was tun?**
Sofort: Art des Geräuschs identifizieren. Schleifen = Lager (WG-F01). Klappern = lose Teile. Pfeifen/Kreischen = Überdrehzahl (WG-F05, SOFORT BREMSEN!). Im Zweifel: bremsen und bei Flaute inspizieren. Nie bei Wind am Generator arbeiten.

**F19: Muss ich den Generator bei Sturm bremsen?**
Empfohlen ab 35 kn für Generatoren mit elektronischer Bremse. Superwind (passive Pitch): Selbstschützend bis ~60 kn, trotzdem Bremse ab 45 kn empfehlenswert. VAWT: Generell sturmfest, Bremse ab 50 kn empfehlenswert. Bei Hurrikan-Bedingungen (>65 kn): Generator abbauen oder Blätter demontieren.

**F20: Wie lange hält ein Windgenerator?**
Erwartete Lebensdauer: 8–15 Jahre bei korrekter Wartung. Lager: 5–10 Jahre. Blätter: 5–8 Jahre (UV-abhängig). Regler: 8–12 Jahre. Generator-Wicklung: 15–20+ Jahre. Magnete: 20+ Jahre (wenn kein Runaway). Gesamtwirtschaftlich: typisch 8–12 Jahre bis zur Kompletterneuerung.

### 8.5 Kombination mit Solar

**F21: Wie kombiniere ich Wind und Solar optimal?**
Zwei Ansätze: (a) Separater Wind-Regler + separater Solar-MPPT → beide laden dieselbe Batterie. Einfach, funktioniert immer. (b) Hybrid-Regler (z.B. Silentwind Hybrid, Victron-Lösung) → ein Gerät regelt beides. Eleganter, aber weniger flexibel. Empfehlung: Für Nachrüstung: separater Wind-Regler parallel zum existierenden Solar-MPPT. Für Neuinstallation: Hybrid-Lösung evaluieren.

**F22: Wie viel Solar, wie viel Wind?**
Grundregel für Blauwasser: 70% Solar, 30% Wind (nach Investition). Solar deckt den Grundbedarf am Tag, Wind füllt nachts und bei Schlechtwetter auf. Typisch: 400–600 Wp Solar + 350–400W Wind = gute Autonomie. Im Norden (hohe Breiten, Winter): Verhältnis Richtung 50/50 verschieben.

**F23: Stören sich Wind und Solar gegenseitig beim Laden?**
Nein, wenn korrekt installiert. Beide Regler arbeiten unabhängig und laden die gleiche Batterie. Die Batterie "nimmt sich" was sie braucht. Potentielles Problem: Wenn Batterie voll und kein Verbraucher aktiv → Wind-Regler braucht Dump-Load oder Bremse. Solar-MPPT regelt einfach ab.

### 8.6 Spezialfragen

**F24: Kann ich einen Windgenerator auf einer Motoryacht installieren?**
Ja, aber der Nutzen ist geringer als auf Segelyachten. Gründe: (a) Motoryachten haben leistungsstarke Lichtmaschinen (Fahrtstrom), (b) weniger Ankertage ohne Landstrom, (c) Turbulenzen durch Aufbauten. Sinnvoll nur bei: häufigem Ankerliegen ohne Generator-Nutzung, Ökologie-Motivation, oder wenn Hauptmotor-Laufzeiten reduziert werden sollen.

**F25: Was kostet die Gesamtinstallation realistisch?**
Budget für typische Segelyacht-Installation: Generator (€1.200–€2.600) + Regler (€200–€500, falls nicht inkludiert) + Montagehalter/Rohr (€200–€500) + Kabel und Kleinmaterial (€100–€200) + ggf. Arch-Modifikation (€300–€1.000) + Arbeitszeit Werft (€300–€800) = **Gesamt: €2.000–€5.000**. Eigeneinbau spart ca. 30%.

**F26: Wie verhält sich der Windgenerator bei Gewitter/Blitz?**
Der Windgenerator ist oft der höchste Punkt am Heck und damit blitzgefährdet. Schutzmaßnahmen: (a) Erdungsband vom Montagehalter zum Kiel/Masseplatte, (b) Überspannungsschutz (Varistoren) am Reglereingang, (c) bei Gewitter: Generator bremsen (reduziert induzierten Strom). Ein direkter Blitzeinschlag zerstört fast immer den Generator und Regler — dagegen gibt es keinen wirtschaftlichen Schutz.

**F27: Gibt es Windgeneratoren für 48V-Systeme?**
Ja, der D400 ist in 48V-Ausführung erhältlich. Auch Superwind bietet auf Anfrage 48V. Für 48V-Systeme (typisch >18m Yachten) ist alternativ ein Standard-Generator mit externem 3-Phasen-Gleichrichter und 48V-Laderegler möglich.

**F28: Wie entsorge ich einen alten Windgenerator?**
Magnete (NdFeB) sind Sondermüll (Seltenerd-Elemente). Blätter (GFK/Carbon) gehören zum Restmüll (nicht recycelbar). Aluminium und Edelstahl sind Wertstoffe. Elektronik (Regler) ist Elektroschrott. Kabel (Kupfer) sind Wertstoffe. Empfehlung: Bei Fachhändler oder Werft abgeben, die korrekte Entsorgung sicherstellen.

### 8.7 Fortgeschrittene Fragen

**F29: Kann ich zwei Windgeneratoren parallel betreiben?**
Technisch möglich, aber selten sinnvoll auf Yachten <20m. Voraussetzungen: (a) Jeder Generator braucht seinen eigenen Laderegler, (b) ausreichend Abstand (min. 3× Rotordurchmesser), (c) separate Montagestrukturen um Resonanzkopplung zu vermeiden. Auf Katamaranen mit breiter Arch gelegentlich realisiert (je ein Generator pro Rumpf). Bei Monohulls: der zweite Generator bringt weniger Zusatzertrag als sein Preis vermuten lässt (turbulente Nachlaufströmung des ersten).

**F30: Was passiert bei Eisansatz auf den Rotorblättern?**
Eisansatz führt zu: (a) Massenunwucht → extreme Vibration, (b) Leistungsverlust durch geänderte Aerodynamik, (c) Eiswurf-Gefahr bei Abtauen → Sicherheitsrisiko. Maßnahme: Generator SOFORT bremsen bei Eisansatz. Abtauen lassen (nicht mit Gewalt entfernen). Erst nach komplettem Abtauen aller Blätter wieder freigeben. In eisgefährdeten Revieren (Ostsee Winter, hohe Breiten): Generator vorsorglich bremsen wenn Lufttemperatur <0°C UND hohe Luftfeuchtigkeit.

**F31: Beeinflusst der Windgenerator mein Radar oder AIS?**
Der Generator selbst stört normalerweise nicht. Aber: (a) Montage HINTER der Radarantenne vermeidet Abschattung, (b) elektromagnetische Störungen durch den Regler (Gleichrichter-Oberwellen) können UKW-Empfang beeinflussen → Ferritkerne auf Generatorkabel. (c) AIS-Antenne mindestens 1m vom Generator entfernt montieren. Generell: EMV-Prüfung nach Installation (UKW-Empfang testen bei drehendem Generator).

**F32: Wie verhalte ich mich beim Ankern in einem Windpark?**
Windgeneratoren auf Yachten haben keine Relevanz für kommerzielle Windparks. Aber: In manchen Windpark-Schutzzonen ist das Ankern verboten — dies hat nichts mit dem Bordgenerator zu tun, sondern mit der Seekabelverlegung und Schifffahrtssicherheit.

**F33: Kann ich den Windgenerator auch unter Motor als Hydrogenerator nutzen?**
Nein, Standard-Windgeneratoren sind dafür nicht ausgelegt. Der DuoGen von Eclectic Energy ist die einzige Dual-Use-Lösung (Wind UND Wasser). Für Hydro-Generation gibt es dedizierte Schleppgeneratoren (Watt&Sea, Save Marine). Ein Windgenerator im Wasser würde die Lager sofort zerstören (Wasserdruck, Sand, Korrosion).

**F34: Mein Windgenerator dreht sich, aber der angezeigte Ertrag schwankt stark — ist das normal?**
Ja, das ist normal. Natürlicher Wind ist turbulent und schwankt sekündlich. Die Leistung schwankt mit v³ — schon kleine Böen verursachen große Leistungsspitzen. Ein MPPT-Regler gleicht dies aus, aber die momentane Anzeige schwankt trotzdem. Für die Bewertung: immer Tagesdurchschnitte betrachten, nicht Momentanwerte. Starke Schwankung bei konstantem Wind deutet hingegen auf ein Problem hin (Windnachführung, Regler).

**F35: Gibt es Fördermittel für Windgeneratoren auf Yachten?**
In Deutschland und der EU: Nein, es gibt keine spezifische Förderung für erneuerbare Energien auf Freizeitbooten. Anders als bei Hausinstallationen gibt es keine Einspeisevergütung oder Kaufprämie. In einigen skandinavischen Ländern gibt es gelegentlich umweltbezogene Hafengebühren-Rabatte für Schiffe mit ausschließlich erneuerbarer Energieversorgung (z.B. Schweden "Blauer Schlüssel"-Programm).

**F36: Wie reagiert der Windgenerator auf schnelle Windrichtungsänderungen (Böen aus anderer Richtung)?**
HAWT: Die Windnachführung (Heckflosse) reagiert mit Verzögerung (1–5 Sekunden). Bei schnellen Richtungsänderungen steht der Rotor kurzzeitig schräg zum Wind → Leistungsverlust und erhöhte Vibration. In böigen Revieren (z.B. bergige Küsten, Ankerbuchten mit Düsenwirkung) kann dies 10–20% Ertragsminderung bedeuten. VAWT: Kein Problem, reagieren sofort auf jede Windrichtung.

**F37: Darf ich den Windgenerator laufen lassen wenn niemand an Bord ist (Dauerliegeplatz)?**
Grundsätzlich ja, wenn: (a) Batterien die Ladung aufnehmen können oder Dump-Load vorhanden, (b) Sturmregelung automatisch funktioniert, (c) Nachbarliegeplätze nicht durch Geräusch gestört werden, (d) lokale Hafenordnung dies erlaubt. Viele Marinas haben Geräuschvorschriften die Windgeneratoren praktisch verbieten. Prüfen Sie die Hafenordnung! Bei Langzeitabwesenheit (>2 Wochen): Generator bremsen empfohlen (Verschleiß ohne Nutzen vermeiden).

**F38: Wie messe ich die tatsächliche Leistung meines Windgenerators?**
Methode 1 (einfach): Batteriemonitor (Victron BMV, etc.) zeigt Ladestrom. Wind-Anteil = Gesamt-Ladestrom minus Solar-Strom minus andere Quellen. Methode 2 (genau): Strommesszange (DC-Klamp) direkt am Regler-Ausgang. Methode 3 (professionell): NMEA2000-fähiger Regler zeigt Leistung direkt an (Silentwind). Für die Validierung gegen Herstellerangaben: gleichzeitig Windgeschwindigkeit am Generator-Standort messen (nicht am Masttop-Anemometer!).

**F39: Kann UV-Strahlung die Rotorblätter zerstören?**
Ja, UV ist der Hauptfeind von GFK- und Nylon-Blättern in tropischen Revieren. Symptome: Oberflächenverblassung (matt, kreideig), Mikrorisse, Versprödung, schließlich Bruchgefahr. Timeline: Nylon-Blätter (Rutland): 4–6 Jahre in Tropen. GFK-Blätter: 6–10 Jahre. Carbon-GFK: 8–12 Jahre. Prävention: UV-Schutzbeschichtung (Spezial-Klarlack alle 2–3 Jahre), regelmäßige Sichtprüfung, rechtzeitig tauschen. Ein UV-geschädigtes Blatt erkennt man am matten, rauen Finish und an Haarrissen unter Gegenlicht.

**F40: Was ist ein Dump-Load und brauche ich einen?**
Ein Dump-Load ist ein Widerstand (typisch 200–600W), der überschüssige Energie in Wärme umwandelt wenn die Batterie voll ist UND der Regler den Generator nicht bremsen kann/soll. Nötig wenn: (a) Regler keine automatische Bremse hat, (b) Generator bei Starkwind viel Energie liefert und kein Verbraucher aktiv ist, (c) LiFePO4-Batterie die Absorption abrupt beendet. Nicht nötig wenn: Regler mit integrierter Brems-/Dumpfunktion (die meisten modernen Regler haben das). Ein fehlender Dump-Load bei vollem System kann zu Überspannung führen → Reglerdefekt (WG-F04).

---

## 9. Glossar

| Begriff | Definition |
|---------|-----------|
| **Apparent Wind** | Scheinbarer Wind, Vektorsumme aus wahrem Wind und Fahrtwind des Schiffes. Bestimmt den tatsächlichen Ertrag des Generators auf fahrendem Schiff. |
| **Beaufort-Skala** | Klassifikation der Windstärke in 13 Stufen (0–12). Bft 4–6 ist der optimale Arbeitsbereich für Marine-Windgeneratoren. |
| **Betz-Limit** | Theoretisches Maximum der Energieentnahme aus dem Wind: 59,3% (16/27). Kein Rotor kann diesen Wert überschreiten. |
| **Blattpassierfrequenz** | Frequenz, mit der Rotorblätter einen festen Punkt passieren. f = Drehzahl × Blattzahl. Hauptanregungsfrequenz für Vibrationen. |
| **Brushless (bürstenlos)** | Generator ohne Kohlebürsten und Schleifringe. Wartungsarm, langlebig. Standard bei modernen Marine-Generatoren. |
| **Campbell-Diagramm** | Grafische Darstellung der Eigenfrequenzen einer Struktur über der Drehzahl. Zeigt kritische Resonanzbereiche. |
| **Capacity Factor (CF)** | Verhältnis der tatsächlich erzeugten Energie zur theoretisch möglichen bei Dauerbetrieb mit Nennleistung. Typisch 0,15–0,30 für Marine. |
| **Cogging** | Rastmoment eines Permanentmagnet-Generators. Verursacht Anlaufschwierigkeit und niederfrequentes Geräusch. Coreless-Designs eliminieren Cogging. |
| **Coreless Generator** | Generator ohne Eisenkern im Stator. Eliminiert Cogging, reduziert Gewicht, verbessert Teillast-Effizienz. |
| **Cp (Leistungsbeiwert)** | Verhältnis der vom Rotor entnommenen Leistung zur verfügbaren Windleistung. Typisch 0,25–0,40 für gute Marine-HAWT. |
| **Darrieus-Rotor** | Vertikalachser mit auftriebsbasierten Blättern. Hoher Cp möglich, aber nicht selbstanlaufend. |
| **Diversion Load / Dump Load** | Widerstand, der überschüssige Energie in Wärme umwandelt, wenn Batterie voll ist. Schützt Generator vor Leerlauf. |
| **Eigenfrequenz** | Natürliche Schwingungsfrequenz einer Struktur. Muss außerhalb des Anregungsbereichs des Generators liegen. |
| **Furling** | Mechanismus, bei dem der Rotor sich bei Starkwind aus dem Wind dreht (horizontal oder vertikal). Passive Sturmregelung. |
| **Generator (Permanent Magnet)** | Elektrischer Generator mit Dauermagneten statt Feldwicklung. Standard für kleine Windgeneratoren. |
| **Gierlager** | Drehlager, das den Generator-Kopf auf dem Montagerrohr drehbar lagert (Windnachführung). |
| **HAWT** | Horizontal Axis Wind Turbine. Horizontalachs-Windturbine. Dominierender Typ im Marine-Bereich. |
| **Helikal** | Schraubenförmig verdreht. Helicale VAWT-Blätter erzeugen gleichmäßiges Drehmoment ohne tote Punkte. |
| **IP-Schutzart** | Schutzgrad gegen Eindringen von Fremdkörpern und Wasser. IP67 = staubdicht + temporäres Untertauchen. IP68 = staubdicht + dauerhaftes Untertauchen. |
| **Kurzschlussbremse** | Bremsmethode durch Verbinden aller Generator-Phasen. Generator wird zum Wirbelstrombremse. Einfachste und zuverlässigste Bremse. |
| **Leistungskurve** | Graph der Generator-Ausgangsleistung über der Windgeschwindigkeit. Wichtigstes Auswahlkriterium. |
| **MPPT** | Maximum Power Point Tracking. Reglerverfahren, das den Generator immer im optimalen Arbeitspunkt betreibt. |
| **NdFeB** | Neodym-Eisen-Bor. Stärkstes verfügbares Permanentmagnet-Material. Standard in Marine-Generatoren. Temperaturempfindlich (>150°C = Entmagnetisierung). |
| **Nennleistung** | Leistung bei Nennwindgeschwindigkeit. KEIN Dauerwert! Effektive Durchschnittsleistung ist 20–30% der Nennleistung. |
| **Nennwindgeschwindigkeit** | Windgeschwindigkeit, bei der der Generator seine Nennleistung erreicht. Typisch 25–30 kn für Marine-Generatoren. |
| **Pitch-Regelung** | Verstellung des Blattanstellwinkels zur Leistungsbegrenzung bei Starkwind. Passiv (Superwind: Zentrifugalkraft) oder aktiv (Servomotor). |
| **Resonanz** | Zustand, wenn Anregungsfrequenz = Eigenfrequenz einer Struktur. Führt zu dramatischer Amplitudenerhöhung. |
| **Rotor** | Gesamtheit der rotierenden Teile (Blätter + Nabe). Bei HAWT: horizontale Achse. Bei VAWT: vertikale Achse. |
| **Savonius-Rotor** | Vertikalachser mit S-förmigem Querschnitt. Widerstandsbasiert, selbstanlaufend, leise, niedrige Effizienz. |
| **Schleifring** | Elektrischer Drehkontakt zur Stromübertragung bei drehender Verbindung. Bei Gierlagerung: überbrückt endloses Drehen. |
| **Schnelllaufzahl (TSR)** | Tip Speed Ratio. Verhältnis Blattspitzengeschwindigkeit zu Windgeschwindigkeit. Bestimmt Effizienz und Geräusch. |
| **Stall** | Strömungsabriss am Blatt bei zu hohem Anstellwinkel. Führt zu Leistungsreduktion. Wird gezielt als Sturmregelung eingesetzt. |
| **Sturmregelung** | Mechanismus zur Leistungsbegrenzung und Drehzahlkontrolle bei Starkwind. Methoden: Pitch, Stall, Furling, elektronische Bremse. |
| **TMD (Tuned Mass Damper)** | Schwingungstilger. Zusatzmasse mit Feder/Dämpfer, die auf die Eigenfrequenz einer Struktur abgestimmt ist. |
| **TSR** | Tip Speed Ratio = Schnelllaufzahl. Siehe dort. |
| **VAWT** | Vertical Axis Wind Turbine. Vertikalachs-Windturbine. Leiser, omnidirektional, aber weniger effizient als HAWT. |
| **Weibull-Verteilung** | Statistische Verteilung zur Beschreibung der Windgeschwindigkeits-Häufigkeit an einem Standort. Grundlage für Ertragsberechnungen. |
| **Windgradient** | Zunahme der Windgeschwindigkeit mit der Höhe über Grund/Wasser. Logarithmisches Profil. |
| **Windnachführung** | Mechanismus zur Ausrichtung des Rotors in den Wind. Passiv (Heckflosse, Nachlauf) oder aktiv (Motor). Bei Marine: immer passiv. |
| **Winglet** | Kleine Endscheibe an der Blattspitze zur Reduktion von Randwirbeln und Geräusch. |

---

## 10. Schnell-Referenz

### 10.1 Entscheidungshilfe: Welcher Generator für mein Boot?

```
BOOT-TYP → EMPFEHLUNG:

Segelboot 8–10m, Küste, <60 Tage/Jahr:
  → Kein Windgenerator nötig (Solar reicht), oder Rutland 1200 (Budget)

Segelboot 10–14m, Küste/Atlantik, >80 Tage/Jahr:
  → Silentwind 400 (Komfort) oder Superwind 350 (Zuverlässigkeit)

Segelboot 12–16m, Blauwasser:
  → Superwind 350 (Referenz) oder Silentwind 400 (Komfort)

Segelboot 14–20m, Blauwasser, Performance:
  → D400 (Allrounder) oder Superwind 350 (Zuverlässigkeit)

Motoryacht 10–15m, Ankerlieger:
  → Silentwind 400 (leise!) oder Rutland 1200 (Budget)

Katamaran 12–16m, Blauwasser:
  → Superwind 350 oder Air Silent X (leicht, für Arch-Montage)

Liveaboard in Marina:
  → Leading Edge VAWT (ultra-leise) oder Silentwind im Nachtmodus

Budget-Maximum €1.500:
  → Rutland 1200 (€1.400 inkl. Regler) oder Air Silent X (€1.200)

Geräusch-Minimum:
  → Leading Edge LE-v150 (VAWT) oder Silentwind 400 mit Nachtmodus
```

### 10.2 Installations-Checkliste

```
□ Generator-Modell gewählt (passend zu Boot/Bedarf/Budget)
□ Montageort festgelegt (≥2m über Deck, ≥2m zu Personen)
□ Montagerrohr dimensioniert (48,3mm, min. 3mm Wandstärke SS316L)
□ Eigenfrequenz-Check (f_eigen > 1,5 × f_blatt bei Nenndreh zahl)
□ Abspannung geplant (ab 2m freier Rohrlänge)
□ Kabelquerschnitt berechnet (<3% Spannungsfall)
□ Kabelführung geplant (UV-geschützt, Zugentlastung, Scheuerschutz)
□ Regler-Position festgelegt (trocken, belüftet, nahe Batterie)
□ Batterie-Anschluss vorbereitet (Sicherung, Trennschalter)
□ Kurzschluss-Bremsschalter vorgesehen (IP67, erreichbar an Deck)
□ Dump-Load vorgesehen (wenn kein automatischer Regler-Dump)
□ Blitzschutz/Erdung (Halter → Erdungsband → Kiel)
□ Sicherheits-Abstand markiert (Rotorteller-Ebene)
□ Sturm-SOP erstellt und crew-bekannt
□ Erste Inbetriebnahme bei Schwachwind (<15 kn)
```

### 10.3 Wartungsplan

| Intervall | Maßnahme | Dauer |
|-----------|----------|-------|
| Monatlich | Sichtprüfung Rotor, Kabel, Halter | 5 min |
| Vierteljährlich | Ertrags-Check vs. Erwartung, Schrauben nachziehen | 15 min |
| Halbjährlich | Bremsfunktions-Test, Kabelanschlüsse prüfen | 30 min |
| Jährlich | Blätter detailliert inspizieren, Gierlager schmieren, Lager horchen | 1 h |
| Alle 3 Jahre | Blatt-Unwucht prüfen, Regler-Funktion vollständig testen | 2 h |
| Alle 5–8 Jahre | Lager präventiv tauschen, Blätter bei Bedarf erneuern | 3–4 h |

### 10.4 Dimensionierungs-Schnellformel

```
Benötigte Nennleistung [W]:

P_nenn = (Bedarf_Ah × U_batt) / (CF × 24 × η_system)

Wobei:
- Bedarf_Ah = täglicher Energiebedarf, den der Wind decken soll [Ah]
- U_batt = Batteriespannung [V] (12 oder 24)
- CF = Capacity Factor (siehe Tabelle 2.4.2)
- η_system = Systemwirkungsgrad (typisch 0,75 inkl. Regler+Kabel)

BEISPIEL:
- 80 Ah/Tag soll Wind decken
- 12V System
- Karibik (CF = 0,24)
- η_system = 0,75

P_nenn = (80 × 12) / (0,24 × 24 × 0,75) = 960 / 4,32 = 222 W

→ Mindestens 250 W Nennleistung, empfohlen 350–400 W (Reserve für schlechte Tage)
```

### 10.5 Kabelquerschnitt-Tabelle

| Strom (A) | 5m einfach | 8m einfach | 10m einfach | 15m einfach |
|-----------|-----------|-----------|------------|------------|
| 10 A (12V) | 4 mm² | 6 mm² | 10 mm² | 10 mm² |
| 15 A (12V) | 6 mm² | 10 mm² | 10 mm² | 16 mm² |
| 20 A (12V) | 10 mm² | 10 mm² | 16 mm² | 25 mm² |
| 25 A (12V) | 10 mm² | 16 mm² | 16 mm² | 25 mm² |
| 30 A (12V) | 16 mm² | 16 mm² | 25 mm² | 35 mm² |
| 10 A (24V) | 2,5 mm² | 4 mm² | 6 mm² | 6 mm² |
| 15 A (24V) | 4 mm² | 6 mm² | 6 mm² | 10 mm² |

(Basis: max. 3% Spannungsfall, Kupfer)

---

## ANHANG A–H — Fallstudien

### ANHANG A: Fallstudie — Blauwasser-Segelyacht 13m, Atlantiküberquerung

**Boot:** Hallberg-Rassy 44, Baujahr 2018, 13,5m
**Fahrtgebiet:** ARC (Las Palmas → St. Lucia), November–Dezember
**Installation:** Superwind 350 auf Heckarch (4,2m über Wasser)
**Solar:** 4× 100 Wp Solarpanele auf Arch (400 Wp gesamt)
**Batterie:** LiFePO4 400 Ah / 12V
**Täglicher Verbrauch:** 180 Ah/Tag (Autopilot, Kühlschrank, Plotter, Beleuchtung, Wassermacher 1h/Tag)

**Ergebnis Atlantiküberquerung (18 Tage):**
- Windgenerator Ertrag: Durchschnitt 95 Ah/Tag (Spitze: 160 Ah/Tag, Minimum: 25 Ah/Tag)
- Solar Ertrag: Durchschnitt 110 Ah/Tag
- Gesamt erneuerbar: 205 Ah/Tag → Überschuss an den meisten Tagen
- Dieselgenerator-Laufzeit: 0 Stunden (keine Nutzung nötig)
- Motorbetrieb (Flaute): 2× je 4h → Lichtmaschine als Backup-Ladung

**Analyse:**
- Passatbedingungen optimal für Windgenerator: 15–22 kn wahrer Wind, relativ konstant
- Apparent Wind (Vorwindkurs): reduziert auf 8–15 kn → trotzdem guter Ertrag
- Nachts: Windgenerator deckt 60–80% des Nachtverbrauchs
- Geräusch: Akzeptabel tagsüber, nachts mit Ohrstöpseln erträglich (Achterschiff)
- Kein Defekt während der Überfahrt

**Kosten-Nutzen:** Investition €3.200 (Generator + Montage auf existierender Arch). Ersparnis vs. Generator-Diesel: ca. €200/Überquerung. Amortisation rein finanziell: >10 Jahre. Echter Wert: Autonomie, Geräuschfreiheit (vs. Dieselgenerator), Komfort.

**Confidence:** documented (Skipper-Logbuch, NMEA-Aufzeichnung)

---

### ANHANG B: Fallstudie — Ostsee-Segler 10m, Saisonbetrieb

**Boot:** Bavaria 34, Baujahr 2015, 10,4m
**Fahrtgebiet:** Ostsee (Kieler Bucht, dänische Südsee), Mai–September
**Installation:** Rutland 1200 auf Heckkorb-Verlängerung (3,0m über Wasser)
**Solar:** 2× 100 Wp flexibel auf Sprayhood/Bimini (200 Wp)
**Batterie:** AGM 2× 110 Ah / 12V
**Täglicher Verbrauch:** 80 Ah/Tag (Ankerlieger), 50 Ah/Tag (unter Segel)

**Ergebnis Saison (Mai–September, 85 Seetage):**
- Windgenerator Ertrag: Durchschnitt 35 Ah/Tag (stark schwankend)
- Gute Tage (>15 kn): 80–120 Ah/Tag
- Schlechte Tage (Flaute): 0–5 Ah/Tag
- Solar Ertrag: Durchschnitt 65 Ah/Tag (Sommer Ostsee)
- Generator-Nutzung: 8× je 1h über die Saison

**Analyse:**
- Ostsee im Sommer: viele Leichtwindtage → Windgenerator oft inaktiv
- Thermische Brisen (nachmittags): kurze Produktionsfenster 14:00–19:00
- Wind ergänzt Solar an trüben, windigen Tagen (Durchzugswetter)
- Resonanzproblem: Heckkorb-Verlängerung vibrierte bei 12–14 kn (Campbell-Bereich)
- Lösung: Abspannung mit 2 Dyneema-Stages → Problem beseitigt
- 6-Blatt-Rotor: guter Schwachwindstart, merkbar ab 5 kn

**Kosten-Nutzen:** Investition €1.600 (Rutland 1200 + Halter + Eigeneinbau). Für Ostsee-Saisonbetrieb: grenzwertig rentabel. Hauptnutzen in windreichen Phasen und als Backup.

**Confidence:** documented (Eigner-Aufzeichnungen, Victron VRM-Daten)

---

### ANHANG C: Fallstudie — Katamaran 14m, Karibik Liveaboard

**Boot:** Lagoon 450, Baujahr 2019, 13,96m
**Fahrtgebiet:** Karibik (Kleine Antillen), ganzjährig
**Installation:** Silentwind 400 auf zentraler Arch (4,8m über Wasser)
**Solar:** 6× 175 Wp starr auf Arch-Dach (1.050 Wp gesamt)
**Batterie:** LiFePO4 600 Ah / 12V
**Täglicher Verbrauch:** 280 Ah/Tag (Klimaanlage 6h nachts, Wassermacher, 2 Kühlschränke, Entertainment)

**Ergebnis (Jahresmittel):**
- Windgenerator Ertrag: Durchschnitt 120 Ah/Tag (Passatwinde!)
- Solar Ertrag: Durchschnitt 200 Ah/Tag
- Gesamt: 320 Ah/Tag → leichter Überschuss
- Generator-Nutzung: ca. 2h/Woche (für Klimaanlage-Peak nachts)

**Analyse:**
- Trade Winds 15–22 kn: ideale Bedingungen für Windgenerator
- Nacht-Produktion entscheidend: Solar liefert nichts, Wind deckt Klimaanlage-Bedarf teilweise
- Geräusch: Silentwind mit Nachtmodus (60% Drehzahl) → akzeptabel im Achterkabinen
- Vor-Wind-Effekt beim Inselhüpfen minimal (kurze Überfahrten)
- Hybrid-Regler (Silentwind) funktioniert zuverlässig, App-Monitoring hilfreich
- Kein Defekt in 2 Jahren Betrieb

**Kosten-Nutzen:** Investition €3.800 (Silentwind + Arch-Montage). Ersparnis Diesel: ca. €150/Monat. Amortisation: ~2,5 Jahre. Klarer wirtschaftlicher Gewinn für Liveaboard.

**Confidence:** documented (Victron VRM 24-Monate-Daten, Eigner-Interview)

---

### ANHANG D: Fallstudie — Regatta-Yacht, Masttop-Installation

**Boot:** J/122, 12,2m, Performance Cruiser/Racer
**Fahrtgebiet:** Nordsee, Kanalrennen, gelegentlich Biskaya
**Installation:** Air Silent X am Masttop (15m über Wasser)
**Solar:** 1× 100 Wp flexibel (minimal, nur Backup)
**Batterie:** LiFePO4 200 Ah / 12V
**Täglicher Verbrauch:** 60 Ah/Tag (Racemode: nur Essentials)

**Ergebnis:**
- Windgenerator Ertrag: Durchschnitt 55 Ah/Tag (Nordsee!)
- Masttop: +15–20% Ertrag vs. Heckarch durch Windgradient
- Am Wind (Regatta): Apparent Wind 20–28 kn → 90–130 Ah/Tag

**Analyse:**
- Masttop-Montage: maximaler Windertrag, aber...
- Vibration: deutlich spürbar im Rigg, akzeptiert für Regatta (nicht Komfort)
- Wartung: erfordert Aufentern → wird nur 1×/Jahr durchgeführt
- Gewicht: 5,9 kg am Masttop → spürbarer Stabilitätseinfluss bei dieser Bootsgröße
- Geräusch: am Masttop weiter weg von Crew, aber Rigg überträgt Sound
- Leicht (Air Silent X): wichtig für Performance-Boot

**Kosten-Nutzen:** Investition €1.800 (Generator + Masttop-Adapter + Kabel durch Mast). Primärer Nutzen: Energieautonomie bei Offshore-Regatten ohne Generatorbetrieb.

**Confidence:** documented (Skipper-Bericht, Race-Tracking-Daten)

---

### ANHANG E: Fallstudie — Schwerwetter-Schaden, Patagonien

**Boot:** Ovni 435, Aluminium, 13,2m
**Fahrtgebiet:** Patagonische Kanäle, Kap Hoorn Region
**Installation:** Superwind 350 auf dediziertem Mast am Heck (5,5m)
**Vorfall:** Williwaw (Fallböe 65+ kn) im Beagle-Kanal

**Schadensbild:**
- Generator überlebte dank passiver Pitch-Regelung (Blätter im Stall)
- Montagehalter: 2 von 3 Abspannungen gerissen (Dyneema-Ende nicht ausreichend gesichert)
- Halterrohr: permanente Verbiegung um ca. 8° (Aluminium plastisch verformt)
- Generator selbst: keine Beschädigung

**Root Cause:**
- Williwaw-Böe >65 kn traf asymmetrisch (nicht frontal zum gebremsten Rotor)
- Querkraft auf Rotor erzeugte Biegemoment, das Abspannung überforderte
- Aluminium-Rohr: zu dünn (2,5mm statt empfohlen 4mm)
- Korrekte Auslegung hätte Edelstahl-Rohr 3mm erfordert

**Lehren:**
1. Patagonien erfordert Überdimensionierung der Montage (Faktor 2 vs. Normalrevier)
2. Abspannungen mit Presshülsen statt Knoten sichern
3. Edelstahl > Aluminium für extreme Windgebiete (kein plastisches Versagen)
4. Superwind passive Pitch hat sich bewährt — Generator unversehrt

**Reparatur:** Neues Rohr (SS316L, 48,3×3,2mm), neue Abspannungen (Dyneema SK78 mit Presshülsen). Kosten: €450.

**Confidence:** documented (Eigner-Schadensbericht mit Fotos)

---

### ANHANG F: Fallstudie — Resonanz-Problem und Lösung

**Boot:** Hanse 415, 12,8m
**Installation:** D400 auf Heckkorb-Verlängerungsrohr (2,2m freiragend, SS316L 48,3×2,5mm)
**Problem:** Starke Vibration und dumpfes Brummen bei 11–14 kn Windstärke

**Diagnose:**
- Frequenzanalyse (Smartphone-App): dominante Frequenz 8,5 Hz bei 12 kn
- Berechnete Eigenfrequenz des Halters: 8,2 Hz
- Blattpassierfrequenz bei 12 kn (D400, ~500 U/min): 5×500/60 = 41,7 Hz → nicht das Problem
- Rotor-Grundfrequenz bei 12 kn: 500/60 = 8,3 Hz → RESONANZ!
- Rotor-Grundfrequenz stimmt mit Halter-Eigenfrequenz überein bei 11–14 kn

**Lösung (stufenweise):**
1. **Versuch 1:** Gummipuffer am Fußpunkt → Amplitude -20%, nicht ausreichend
2. **Versuch 2:** Rohr kürzen um 30cm (auf 1,9m) → f_eigen steigt auf 11,8 Hz → Resonanz verschiebt sich auf ~16 kn (immer noch im Arbeitsbereich!)
3. **Versuch 3:** 2× Abspannung (Dyneema) am oberen Drittel → f_eigen steigt auf >25 Hz → PROBLEM GELÖST

**Kosten Lösung:** €120 (2× Dyneema-Stage + Augbolzen)
**Ergebnis:** Vibration nicht mehr wahrnehmbar, Generator läuft nun vollkommen smooth

**Confidence:** documented (Eigner-Bericht, Frequenzmessung mit PhyPhox App)

---

### ANHANG G: Fallstudie — Regler-Defekt und Batterie-Überladung

**Boot:** Sun Odyssey 409, 12,3m
**Installation:** Rutland 1200 mit Original-Regler (HRSi)
**Vorfall:** Nachts bei 25 kn, Crew schlief

**Schadensbild:**
- MOSFET im Regler durchgebrannt → Bremse inaktiv UND Laderegelung inaktiv
- Generator lief ungebremst → lieferte >16V in 12V-Batterie
- AGM-Batterie (110 Ah) durch Überladung ausgegast → permanent geschädigt
- Kühlschrank-Elektronik durch Überspannung beschädigt

**Root Cause:**
- Regler-MOSFET hatte bekanntes Ausfallmuster bei Firmware-Version <3.2
- Kein Überspannungsschutz zwischen Regler und Batterie installiert
- Kein separater Kurzschlussschalter als Backup vorhanden
- Alarm-System (Batteriemonitor) war auf "stumm" gestellt

**Lehren:**
1. IMMER separaten manuellen Kurzschlussschalter installieren (unabhängig vom Regler)
2. Überspannungsschutz (Varistor 18V für 12V-System) zwischen Regler und Batterie
3. Batteriemonitor-Alarm NIE deaktivieren
4. Firmware des Reglers aktuell halten
5. Bei Sturm nachts: Generator bremsen oder Wache informieren

**Reparatur:** Neuer Regler (€280) + neue Batterie (€320) + Kühlschrank-Platine (€180) = €780 Gesamtschaden.

**Confidence:** documented (Eigner-Schadensmeldung, Versicherungsakte)

---

### ANHANG H: Fallstudie — VAWT-Installation auf Motoryacht

**Boot:** Grand Banks 42, Trawler, 12,8m
**Fahrtgebiet:** Nordsee, Wattenmeer, Holland
**Installation:** Leading Edge LE-v150 auf Flybridge-Geländer (3,5m über Wasser)
**Motivation:** Minimales Geräusch im Hafen, Ergänzung zu 400 Wp Solar
**Batterie:** AGM 440 Ah / 12V

**Ergebnis (Saison April–Oktober):**
- Windgenerator Ertrag: Durchschnitt 22 Ah/Tag
- Spitzentage (Nordsee-Wind >20 kn): 50–65 Ah/Tag
- Geräusch: unter allen Bedingungen praktisch unhörbar
- Vibration: nicht wahrnehmbar

**Analyse:**
- Ertrag für 150W VAWT auf 3,5m Höhe: plausibel, aber gering
- Hauptwert: Nacht-Ladung im Hafen ohne Generator-Betrieb (Hafenruhe-Vorschriften!)
- ROI: rechnerisch nie (€1.800 Invest, ~€30/Jahr Diesel-Ersparnis)
- Emotionaler Wert: Eigner schätzt Geräuschfreiheit und Umweltbewusstsein
- Probleme: Hersteller nicht mehr aktiv → Ersatzteil-Sorge

**Bewertung:** Technisch funktional, wirtschaftlich nicht gerechtfertigt, emotional wertvoll für den Eigner. Typisch für VAWT-Installationen auf Motoryachten.

**Confidence:** documented (Eigner-Interview, Victron VRM-Daten 18 Monate)

---

## ANHANG I–R — AYDI-Integration (Pydantic v2 Modelle)

### ANHANG I: Basis-Datenmodelle

```python
"""
AYDI Wind Generator Analysis Models
Module: 22_06_windgenerator
All models use Pydantic v2 with model_config = {"from_attributes": True}
"""

from __future__ import annotations

from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, field_validator


# --- Enums ---

class WindGeneratorType(str, Enum):
    """Type classification of wind generators."""
    HAWT_3_BLADE = "hawt_3_blade"
    HAWT_5_BLADE = "hawt_5_blade"
    HAWT_6_BLADE = "hawt_6_blade"
    VAWT_SAVONIUS = "vawt_savonius"
    VAWT_DARRIEUS = "vawt_darrieus"
    VAWT_HELICAL = "vawt_helical"
    HYBRID_SOLAR_WIND = "hybrid_solar_wind"


class MountingLocation(str, Enum):
    """Mounting location options for wind generators."""
    STERN_ARCH = "stern_arch"
    STERN_RAIL = "stern_rail"
    DEDICATED_MAST = "dedicated_mast"
    MAIN_MAST_TOP = "main_mast_top"
    FLYBRIDGE_ARCH = "flybridge_arch"
    BIMINI_FRAME = "bimini_frame"
    DAVIT = "davit"


class MountingMaterial(str, Enum):
    """Material for the mounting pole/structure."""
    STAINLESS_316L = "stainless_316l"
    ALUMINUM_6082_T6 = "aluminum_6082_t6"
    CARBON_FIBER = "carbon_fiber"
    GALVANIZED_STEEL = "galvanized_steel"


class StormControlMethod(str, Enum):
    """Storm control / overspeed protection method."""
    PASSIVE_PITCH = "passive_pitch"
    ELECTRONIC_BRAKE = "electronic_brake"
    AERODYNAMIC_STALL = "aerodynamic_stall"
    FURLING_HORIZONTAL = "furling_horizontal"
    FURLING_VERTICAL = "furling_vertical"
    SELF_LIMITING = "self_limiting"
    MANUAL_BRAKE = "manual_brake"


class BrakeType(str, Enum):
    """Brake mechanism type."""
    SHORT_CIRCUIT = "short_circuit"
    DUMP_LOAD = "dump_load"
    MECHANICAL_DISC = "mechanical_disc"
    ELECTRONIC_PWM = "electronic_pwm"


class ConfidenceLevel(str, Enum):
    """AYDI confidence level for assessments."""
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
    """Severity classification for faults."""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


class FaultCode(str, Enum):
    """Fault codes for wind generator issues."""
    WG_F01_BEARING_DAMAGE = "WG-F01"
    WG_F02_BLADE_BREAK = "WG-F02"
    WG_F03_VIBRATION_RESONANCE = "WG-F03"
    WG_F04_CONTROLLER_FAULT = "WG-F04"
    WG_F05_OVERSPEED = "WG-F05"
    WG_F06_CORROSION = "WG-F06"
    WG_F07_YAW_BLOCKED = "WG-F07"
    WG_F08_WINDING_DAMAGE = "WG-F08"
    WG_F09_CABLE_FAULT = "WG-F09"
    WG_F10_DEMAGNETIZATION = "WG-F10"
    WG_F11_BRAKE_FAILURE = "WG-F11"
    WG_F12_TAIL_NACELLE_DAMAGE = "WG-F12"
```

### ANHANG J: Windgenerator-Spezifikationsmodell

```python
class PowerCurvePoint(BaseModel):
    """Single point on a wind generator power curve."""
    model_config = {"from_attributes": True}

    wind_speed_knots: float = Field(..., ge=0, le=80, description="Wind speed in knots")
    wind_speed_ms: float = Field(..., ge=0, le=41, description="Wind speed in m/s")
    power_watts: float = Field(..., ge=0, le=2000, description="Output power in watts")
    charge_current_12v: Optional[float] = Field(None, ge=0, description="Charge current at 12V in amps")
    charge_current_24v: Optional[float] = Field(None, ge=0, description="Charge current at 24V in amps")
    rotor_rpm: Optional[float] = Field(None, ge=0, description="Rotor speed in RPM")
    sound_level_dba: Optional[float] = Field(None, ge=0, le=120, description="Sound level at 7m in dB(A)")

    @field_validator("wind_speed_ms", mode="before")
    @classmethod
    def calculate_ms_from_knots(cls, v, info):
        if v is None and "wind_speed_knots" in info.data:
            return info.data["wind_speed_knots"] * 0.5144
        return v


class WindGeneratorSpec(BaseModel):
    """Complete technical specification of a wind generator model."""
    model_config = {"from_attributes": True}

    # Identification
    manufacturer: str = Field(..., description="Manufacturer name")
    model_name: str = Field(..., description="Model designation")
    generator_type: WindGeneratorType = Field(..., description="Type classification")

    # Performance
    rated_power_watts: float = Field(..., ge=0, le=5000, description="Rated power output in watts")
    rated_wind_speed_knots: float = Field(..., ge=0, le=60, description="Wind speed at rated power in knots")
    cut_in_wind_speed_knots: float = Field(..., ge=0, le=20, description="Cut-in wind speed in knots")
    survival_wind_speed_knots: float = Field(..., ge=0, le=200, description="Maximum survival wind speed in knots")
    power_curve: list[PowerCurvePoint] = Field(default_factory=list, description="Power curve data points")

    # Physical
    rotor_diameter_m: float = Field(..., ge=0.1, le=3.0, description="Rotor diameter in meters")
    rotor_height_m: Optional[float] = Field(None, ge=0.1, le=3.0, description="Rotor height for VAWT in meters")
    blade_count: int = Field(..., ge=2, le=12, description="Number of blades")
    blade_material: str = Field(..., description="Blade material description")
    weight_kg: float = Field(..., ge=1, le=50, description="Total weight in kg")
    mounting_diameter_mm: float = Field(default=48.3, description="Mounting pole diameter in mm")

    # Electrical
    system_voltage: list[int] = Field(..., description="Available system voltages (12, 24, 48)")
    max_charge_current_12v: Optional[float] = Field(None, ge=0, description="Max charge current at 12V")
    max_charge_current_24v: Optional[float] = Field(None, ge=0, description="Max charge current at 24V")
    generator_type_detail: str = Field(default="permanent_magnet_brushless", description="Generator technology")
    is_coreless: bool = Field(default=False, description="Whether generator is coreless (no cogging)")

    # Protection
    ip_rating: str = Field(default="IP66", description="Ingress protection rating")
    storm_control: list[StormControlMethod] = Field(..., description="Storm control methods")
    brake_type: list[BrakeType] = Field(default_factory=list, description="Brake mechanisms")

    # Commercial
    price_eur: Optional[float] = Field(None, ge=0, description="Approximate price in EUR")
    includes_controller: bool = Field(default=False, description="Whether price includes charge controller")
    warranty_years: int = Field(default=2, ge=0, le=10, description="Warranty period in years")
    country_of_manufacture: str = Field(default="unknown", description="Country of manufacture")

    # Performance characteristics
    tsr_optimal: Optional[float] = Field(None, ge=0, le=15, description="Optimal tip speed ratio")
    cp_max: Optional[float] = Field(None, ge=0, le=0.593, description="Maximum power coefficient")
    bearing_lifetime_hours: Optional[float] = Field(None, ge=0, description="Expected bearing lifetime in hours")
    sound_level_20kn_dba: Optional[float] = Field(None, ge=0, le=120, description="Sound level at 20 kn wind, 7m distance")
```

### ANHANG K: Montage- und Installationsmodell

```python
class MountingConfiguration(BaseModel):
    """Configuration of the wind generator mounting system."""
    model_config = {"from_attributes": True}

    location: MountingLocation = Field(..., description="Mounting location on vessel")
    pole_material: MountingMaterial = Field(..., description="Pole/tube material")
    pole_outer_diameter_mm: float = Field(default=48.3, ge=20, le=100, description="Pole outer diameter in mm")
    pole_wall_thickness_mm: float = Field(..., ge=1.5, le=10, description="Pole wall thickness in mm")
    pole_free_length_m: float = Field(..., ge=0.3, le=4.0, description="Free (unsupported) pole length in meters")
    height_above_water_m: float = Field(..., ge=1.0, le=20.0, description="Height of rotor center above waterline")
    height_above_deck_m: float = Field(..., ge=1.0, le=8.0, description="Height of rotor above deck level")

    # Guy wires / stays
    has_stays: bool = Field(default=False, description="Whether pole is stayed/guyed")
    stay_count: int = Field(default=0, ge=0, le=4, description="Number of stays")
    stay_material: Optional[str] = Field(None, description="Stay material (Dyneema, wire, etc.)")
    stay_attachment_height_m: Optional[float] = Field(None, description="Height of stay attachment on pole")

    # Safety
    clearance_to_persons_m: float = Field(..., ge=0, description="Minimum distance to person-accessible areas")
    clearance_to_rigging_m: Optional[float] = Field(None, description="Minimum distance to running rigging")

    # Vibration analysis
    calculated_eigenfrequency_hz: Optional[float] = Field(None, ge=0, description="Calculated natural frequency of mounting")
    blade_passing_frequency_at_rated_hz: Optional[float] = Field(None, ge=0, description="Blade passing frequency at rated speed")
    resonance_risk: Optional[bool] = Field(None, description="Whether resonance risk exists")


class CableConfiguration(BaseModel):
    """Electrical cable configuration from generator to battery."""
    model_config = {"from_attributes": True}

    cable_length_single_m: float = Field(..., ge=1, le=30, description="Single cable run length in meters")
    cable_cross_section_mm2: float = Field(..., ge=1.5, le=50, description="Cable cross section in mm²")
    cable_type: str = Field(default="tinned_copper_marine", description="Cable type")
    is_uv_protected: bool = Field(default=True, description="Whether cable is UV protected")
    has_strain_relief: bool = Field(default=True, description="Whether strain relief is installed")
    voltage_drop_percent: Optional[float] = Field(None, ge=0, le=20, description="Calculated voltage drop at rated current")
    fuse_rating_a: Optional[float] = Field(None, ge=0, description="Fuse rating in amps")
    has_disconnect_switch: bool = Field(default=True, description="Whether a disconnect switch is installed")
    has_manual_brake_switch: bool = Field(default=False, description="Whether a manual short-circuit brake switch exists")
    has_surge_protection: bool = Field(default=False, description="Whether surge/lightning protection is installed")


class InstallationAssessment(BaseModel):
    """Complete installation assessment for a wind generator."""
    model_config = {"from_attributes": True}

    generator_spec: WindGeneratorSpec
    mounting: MountingConfiguration
    cabling: CableConfiguration
    controller_model: Optional[str] = Field(None, description="Charge controller model")
    controller_type: Optional[str] = Field(None, description="MPPT, PWM, or hybrid")
    has_dump_load: bool = Field(default=False, description="Whether a dump load resistor is installed")
    dump_load_watts: Optional[float] = Field(None, ge=0, description="Dump load power rating in watts")

    # Assessment scores
    mounting_score: Optional[float] = Field(None, ge=0, le=100, description="Mounting quality score")
    electrical_score: Optional[float] = Field(None, ge=0, le=100, description="Electrical installation score")
    safety_score: Optional[float] = Field(None, ge=0, le=100, description="Safety assessment score")
    overall_score: Optional[float] = Field(None, ge=0, le=100, description="Overall installation quality score")

    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.ESTIMATED)
```

### ANHANG L: Ertragsberechnung und Energiebilanz

```python
class WindConditions(BaseModel):
    """Wind conditions at a location/route for yield estimation."""
    model_config = {"from_attributes": True}

    location_name: str = Field(..., description="Location or route name")
    region: str = Field(..., description="Geographic region")
    season: str = Field(..., description="Season (summer, winter, annual)")
    average_wind_knots: float = Field(..., ge=0, le=60, description="Average wind speed in knots")
    weibull_k: float = Field(default=2.0, ge=1.0, le=4.0, description="Weibull shape parameter k")
    weibull_c_ms: float = Field(..., ge=0, le=25, description="Weibull scale parameter c in m/s")
    capacity_factor: float = Field(..., ge=0, le=1.0, description="Estimated capacity factor")
    hours_above_cutin_per_day: float = Field(default=12.0, ge=0, le=24, description="Hours above cut-in wind speed per day")
    predominant_direction: Optional[str] = Field(None, description="Predominant wind direction")


class YieldEstimate(BaseModel):
    """Estimated energy yield from a wind generator at given conditions."""
    model_config = {"from_attributes": True}

    generator_model: str = Field(..., description="Generator model name")
    wind_conditions: WindConditions
    mounting_height_m: float = Field(..., ge=1, le=20, description="Mounting height above water")

    # Yield results
    daily_yield_wh: float = Field(..., ge=0, description="Estimated daily yield in Wh")
    daily_yield_ah_12v: float = Field(..., ge=0, description="Estimated daily yield in Ah at 12V")
    daily_yield_ah_24v: float = Field(..., ge=0, description="Estimated daily yield in Ah at 24V")
    monthly_yield_kwh: float = Field(..., ge=0, description="Estimated monthly yield in kWh")
    annual_yield_kwh: Optional[float] = Field(None, ge=0, description="Estimated annual yield in kWh")

    # Correction factors applied
    height_correction_factor: float = Field(default=1.0, ge=0.5, le=1.5, description="Wind gradient correction")
    apparent_wind_factor: float = Field(default=1.0, ge=0.2, le=2.0, description="Apparent wind correction for sailing")
    system_efficiency: float = Field(default=0.75, ge=0.5, le=0.95, description="Overall system efficiency")
    turbulence_factor: float = Field(default=1.0, ge=0.6, le=1.0, description="Turbulence/obstruction penalty")

    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.ESTIMATED)
    notes: list[str] = Field(default_factory=list, description="Notes and assumptions")


class EnergyBalanceWind(BaseModel):
    """Wind generator contribution to vessel energy balance."""
    model_config = {"from_attributes": True}

    vessel_name: str = Field(..., description="Vessel identification")
    daily_consumption_ah: float = Field(..., ge=0, description="Total daily consumption in Ah")
    system_voltage: int = Field(..., description="System voltage (12 or 24)")

    # Energy sources
    wind_daily_ah: float = Field(..., ge=0, description="Wind contribution in Ah/day")
    solar_daily_ah: float = Field(default=0, ge=0, description="Solar contribution in Ah/day")
    alternator_daily_ah: float = Field(default=0, ge=0, description="Alternator contribution in Ah/day")
    shore_power_daily_ah: float = Field(default=0, ge=0, description="Shore power contribution in Ah/day")
    generator_daily_ah: float = Field(default=0, ge=0, description="Diesel generator contribution in Ah/day")

    # Balance
    total_generation_ah: float = Field(..., ge=0, description="Total generation in Ah/day")
    surplus_or_deficit_ah: float = Field(..., description="Positive = surplus, negative = deficit")
    wind_share_percent: float = Field(..., ge=0, le=100, description="Wind share of total generation")
    renewable_share_percent: float = Field(..., ge=0, le=100, description="Renewable (wind+solar) share")
    autonomy_days: Optional[float] = Field(None, ge=0, description="Days of autonomy without diesel/shore")

    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.ESTIMATED)
```

### ANHANG M: Fehlerbild- und Diagnosemodelle

```python
class FaultFinding(BaseModel):
    """A diagnosed fault on a wind generator installation."""
    model_config = {"from_attributes": True}

    fault_code: FaultCode = Field(..., description="Fault classification code")
    severity: FaultSeverity = Field(..., description="Fault severity level")
    title_de: str = Field(..., description="Fault title in German")
    description_de: str = Field(..., description="Detailed description in German")
    symptoms: list[str] = Field(..., min_length=1, description="Observed symptoms")
    probable_causes: list[str] = Field(..., min_length=1, description="Probable root causes")
    affected_component: str = Field(..., description="Affected component")
    immediate_action_de: str = Field(..., description="Recommended immediate action in German")
    repair_description_de: str = Field(..., description="Repair description in German")
    estimated_repair_cost_eur: Optional[float] = Field(None, ge=0, description="Estimated repair cost in EUR")
    estimated_repair_hours: Optional[float] = Field(None, ge=0, description="Estimated repair time in hours")
    requires_professional: bool = Field(default=False, description="Whether professional repair is needed")
    safety_critical: bool = Field(default=False, description="Whether fault is safety-critical")
    prevention_measures: list[str] = Field(default_factory=list, description="Prevention measures")
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.DOCUMENTED)
    detection_method: str = Field(default="visual_and_measurement", description="How the fault was detected")


class VibrationAssessment(BaseModel):
    """Vibration assessment of a wind generator installation."""
    model_config = {"from_attributes": True}

    measurement_location: str = Field(..., description="Where vibration was measured")
    velocity_rms_mm_s: float = Field(..., ge=0, le=100, description="Vibration velocity RMS in mm/s")
    dominant_frequency_hz: Optional[float] = Field(None, ge=0, description="Dominant vibration frequency in Hz")
    iso_10816_zone: str = Field(..., description="ISO 10816-1 zone classification (A/B/C/D)")
    wind_speed_during_measurement_knots: float = Field(..., ge=0, description="Wind speed during measurement")
    rotor_rpm_during_measurement: Optional[float] = Field(None, ge=0, description="Rotor RPM during measurement")
    is_resonance_suspected: bool = Field(default=False, description="Whether resonance is suspected")
    resonance_wind_speed_range_knots: Optional[tuple[float, float]] = Field(
        None, description="Wind speed range where resonance occurs (min, max)"
    )
    recommended_action_de: str = Field(default="", description="Recommended action in German")
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.MEASURED)


class NoiseAssessment(BaseModel):
    """Noise assessment of a wind generator."""
    model_config = {"from_attributes": True}

    measurement_distance_m: float = Field(default=7.0, ge=1, le=50, description="Measurement distance in meters")
    wind_speed_knots: float = Field(..., ge=0, description="Wind speed during measurement")
    sound_level_dba: float = Field(..., ge=0, le=120, description="Measured sound level in dB(A)")
    background_noise_dba: Optional[float] = Field(None, ge=0, le=100, description="Background noise level")
    dominant_character: Optional[str] = Field(
        None, description="Dominant noise character (tonal, broadband, impulsive, intermittent)"
    )
    frequency_range: Optional[str] = Field(None, description="Dominant frequency range")
    comfort_assessment_de: str = Field(default="", description="Subjective comfort assessment in German")
    exceeds_harbor_limits: Optional[bool] = Field(None, description="Whether harbor noise limits are exceeded")
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.MEASURED)
```

### ANHANG N: Visuelle Analyse-Modelle

```python
class VisualWindGeneratorAssessment(BaseModel):
    """Assessment from visual (photo) analysis of a wind generator installation."""
    model_config = {"from_attributes": True}

    # What can be assessed visually
    generator_type_identified: Optional[WindGeneratorType] = Field(None, description="Identified generator type")
    manufacturer_identified: Optional[str] = Field(None, description="Identified manufacturer")
    model_identified: Optional[str] = Field(None, description="Identified model")
    mounting_location_identified: Optional[MountingLocation] = Field(None, description="Identified mounting location")

    # Visual condition assessment
    blade_condition: Optional[str] = Field(None, description="Visual blade condition assessment")
    blade_uv_damage_visible: Optional[bool] = Field(None, description="Whether UV damage is visible on blades")
    blade_cracks_visible: Optional[bool] = Field(None, description="Whether cracks are visible on blades")
    corrosion_visible: Optional[bool] = Field(None, description="Whether corrosion is visible")
    corrosion_location: Optional[str] = Field(None, description="Where corrosion is visible")
    mounting_appears_adequate: Optional[bool] = Field(None, description="Whether mounting appears structurally adequate")
    stays_present: Optional[bool] = Field(None, description="Whether guy stays/supports are visible")
    cable_routing_visible_issues: Optional[bool] = Field(None, description="Whether cable issues are visible")
    safety_clearance_adequate: Optional[bool] = Field(None, description="Whether safety clearance appears adequate")
    overall_condition_score: Optional[float] = Field(None, ge=0, le=100, description="Overall visual condition score")

    # Findings
    findings: list[FaultFinding] = Field(default_factory=list, description="Identified faults from visual analysis")
    suggestions_de: list[str] = Field(default_factory=list, description="Improvement suggestions in German")

    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.VISUAL_MEDIUM)
    photo_quality: Optional[str] = Field(None, description="Assessment of photo quality for analysis")
    limitations: list[str] = Field(default_factory=list, description="Limitations of the visual assessment")


class WindGeneratorPhoto(BaseModel):
    """Metadata for a wind generator photo submitted for analysis."""
    model_config = {"from_attributes": True}

    photo_id: str = Field(..., description="Unique photo identifier")
    file_path: Optional[str] = Field(None, description="File path or URL")
    capture_date: Optional[date] = Field(None, description="Date photo was taken")
    shows_full_installation: bool = Field(default=False, description="Whether full installation is visible")
    shows_blades_detail: bool = Field(default=False, description="Whether blade detail is visible")
    shows_mounting_detail: bool = Field(default=False, description="Whether mounting detail is visible")
    shows_cabling: bool = Field(default=False, description="Whether cabling is visible")
    shows_controller: bool = Field(default=False, description="Whether controller is visible")
    estimated_wind_speed_in_photo: Optional[str] = Field(None, description="Estimated wind conditions in photo")
    photo_angle: Optional[str] = Field(None, description="Photo angle (front, side, below, detail)")
    quality_score: Optional[float] = Field(None, ge=0, le=100, description="Photo quality for analysis")
```

### ANHANG O: Dimensionierungs- und Auswahlmodell

```python
class VesselEnergyProfile(BaseModel):
    """Vessel energy profile for wind generator sizing."""
    model_config = {"from_attributes": True}

    vessel_type: str = Field(..., description="Vessel type (sailboat, catamaran, motorboat)")
    vessel_length_m: float = Field(..., ge=5, le=40, description="Vessel LOA in meters")
    system_voltage: int = Field(..., description="Electrical system voltage (12, 24, 48)")
    battery_capacity_ah: float = Field(..., ge=50, le=5000, description="Battery bank capacity in Ah")
    battery_type: str = Field(..., description="Battery technology (AGM, LiFePO4, etc.)")
    daily_consumption_ah: float = Field(..., ge=10, le=2000, description="Daily energy consumption in Ah")
    existing_solar_wp: float = Field(default=0, ge=0, description="Existing solar capacity in Wp")
    existing_solar_daily_ah: float = Field(default=0, ge=0, description="Existing solar daily yield in Ah")
    has_generator: bool = Field(default=False, description="Whether a diesel generator exists")
    usage_pattern: str = Field(..., description="Usage pattern (weekend, coastal, bluewater, liveaboard)")
    typical_sailing_region: str = Field(..., description="Typical sailing region")
    noise_sensitivity: str = Field(default="medium", description="Noise sensitivity (low, medium, high)")
    budget_eur: Optional[float] = Field(None, ge=0, description="Available budget in EUR")


class WindGeneratorRecommendation(BaseModel):
    """Recommendation result for wind generator selection."""
    model_config = {"from_attributes": True}

    vessel_profile: VesselEnergyProfile
    recommended_models: list[str] = Field(..., description="Recommended generator models (ranked)")
    recommended_type: WindGeneratorType = Field(..., description="Recommended generator type")
    recommended_power_watts: float = Field(..., ge=50, le=2000, description="Recommended rated power in watts")
    recommended_mounting: MountingLocation = Field(..., description="Recommended mounting location")
    minimum_mounting_height_m: float = Field(..., ge=1, description="Minimum recommended mounting height")

    # Expected performance
    estimated_daily_yield_ah: float = Field(..., ge=0, description="Expected daily yield in Ah")
    estimated_wind_share_percent: float = Field(..., ge=0, le=100, description="Expected wind share of consumption")
    estimated_renewable_autonomy: bool = Field(..., description="Whether Wind+Solar cover full consumption")
    estimated_diesel_reduction_percent: float = Field(default=0, ge=0, le=100, description="Expected diesel reduction")

    # Cost-benefit
    estimated_total_cost_eur: float = Field(..., ge=0, description="Estimated total installation cost")
    estimated_annual_savings_eur: float = Field(default=0, ge=0, description="Estimated annual savings vs diesel")
    estimated_payback_years: Optional[float] = Field(None, ge=0, description="Estimated payback period in years")

    reasoning_de: str = Field(..., description="Detailed reasoning in German")
    warnings_de: list[str] = Field(default_factory=list, description="Warnings and considerations in German")
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.ESTIMATED)
```

### ANHANG P: Wartungs- und Lebenszyklusmodell

```python
class MaintenanceTask(BaseModel):
    """A scheduled maintenance task for a wind generator."""
    model_config = {"from_attributes": True}

    task_id: str = Field(..., description="Unique task identifier")
    title_de: str = Field(..., description="Task title in German")
    description_de: str = Field(..., description="Detailed description in German")
    interval_months: int = Field(..., ge=1, le=120, description="Interval between executions in months")
    estimated_duration_minutes: int = Field(..., ge=5, le=480, description="Estimated task duration in minutes")
    requires_calm_conditions: bool = Field(default=True, description="Whether calm wind is needed")
    requires_climbing: bool = Field(default=False, description="Whether climbing/aloft work is needed")
    can_be_diy: bool = Field(default=True, description="Whether owner can perform this task")
    tools_required: list[str] = Field(default_factory=list, description="Required tools")
    materials_required: list[str] = Field(default_factory=list, description="Required materials")
    estimated_material_cost_eur: float = Field(default=0, ge=0, description="Material cost per execution")


class MaintenanceSchedule(BaseModel):
    """Complete maintenance schedule for a wind generator installation."""
    model_config = {"from_attributes": True}

    generator_model: str = Field(..., description="Generator model")
    installation_date: Optional[date] = Field(None, description="Installation date")
    operating_hours: Optional[float] = Field(None, ge=0, description="Total operating hours")
    tasks: list[MaintenanceTask] = Field(..., description="Scheduled maintenance tasks")
    annual_maintenance_cost_eur: float = Field(default=0, ge=0, description="Estimated annual maintenance cost")
    next_due_tasks: list[str] = Field(default_factory=list, description="Tasks currently due")


class LifecycleCostAnalysis(BaseModel):
    """20-year lifecycle cost analysis for a wind generator."""
    model_config = {"from_attributes": True}

    generator_model: str = Field(..., description="Generator model")
    purchase_cost_eur: float = Field(..., ge=0, description="Initial purchase cost")
    installation_cost_eur: float = Field(..., ge=0, description="Installation cost (material + labor)")
    annual_maintenance_cost_eur: float = Field(default=50, ge=0, description="Average annual maintenance cost")

    # Replacement schedule (20 years)
    bearing_replacements: int = Field(default=2, ge=0, description="Expected bearing replacements in 20 years")
    bearing_cost_per_eur: float = Field(default=180, ge=0, description="Cost per bearing replacement")
    blade_replacements: int = Field(default=2, ge=0, description="Expected blade set replacements in 20 years")
    blade_set_cost_eur: float = Field(default=300, ge=0, description="Cost per blade set replacement")
    controller_replacements: int = Field(default=1, ge=0, description="Expected controller replacements")
    controller_cost_eur: float = Field(default=350, ge=0, description="Cost per controller replacement")

    # Totals
    total_20_year_cost_eur: float = Field(..., ge=0, description="Total cost over 20 years")
    cost_per_kwh_eur: Optional[float] = Field(None, ge=0, description="Effective cost per kWh generated")
    comparison_diesel_cost_20_year_eur: Optional[float] = Field(
        None, ge=0, description="Equivalent diesel generator cost over 20 years"
    )
    net_savings_20_year_eur: Optional[float] = Field(None, description="Net savings vs diesel over 20 years")
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.ESTIMATED)
```

### ANHANG Q: Hersteller-Datenbank-Modell

```python
class ManufacturerInfo(BaseModel):
    """Manufacturer information for wind generator database."""
    model_config = {"from_attributes": True}

    name: str = Field(..., description="Manufacturer name")
    country: str = Field(..., description="Country of origin")
    founded_year: Optional[int] = Field(None, ge=1900, le=2030, description="Year founded")
    website: Optional[str] = Field(None, description="Website URL")
    still_active: bool = Field(default=True, description="Whether company is still active")
    specialization: str = Field(..., description="Company specialization")
    product_models: list[str] = Field(..., description="Available product models")
    spare_parts_availability: str = Field(
        default="good", description="Spare parts availability (excellent, good, limited, poor)"
    )
    service_network: str = Field(default="regional", description="Service network (global, regional, direct_only)")
    certifications: list[str] = Field(default_factory=list, description="Held certifications")
    quality_rating: Optional[float] = Field(None, ge=1, le=5, description="Quality rating 1-5")
    value_rating: Optional[float] = Field(None, ge=1, le=5, description="Value for money rating 1-5")
    support_rating: Optional[float] = Field(None, ge=1, le=5, description="Support/service rating 1-5")
    notes_de: str = Field(default="", description="Additional notes in German")


class ManufacturerDatabase(BaseModel):
    """Complete manufacturer database for wind generators."""
    model_config = {"from_attributes": True}

    manufacturers: list[ManufacturerInfo] = Field(..., description="List of manufacturers")
    last_updated: date = Field(..., description="Database last updated date")
    total_models_tracked: int = Field(default=0, ge=0, description="Total number of models in database")
```

### ANHANG R: Analyse-Orchestrierung

```python
class WindGeneratorAnalysisInput(BaseModel):
    """Input data for wind generator analysis module."""
    model_config = {"from_attributes": True}

    # Vessel data
    vessel_length_m: float = Field(..., ge=5, le=40)
    vessel_type: str = Field(...)
    system_voltage: int = Field(...)
    daily_consumption_ah: float = Field(...)
    sailing_region: str = Field(...)

    # Existing installation (if any)
    has_wind_generator: bool = Field(default=False)
    existing_generator_model: Optional[str] = Field(None)
    existing_generator_spec: Optional[WindGeneratorSpec] = Field(None)
    existing_mounting: Optional[MountingConfiguration] = Field(None)
    existing_cabling: Optional[CableConfiguration] = Field(None)

    # Photos for visual analysis
    photos: list[WindGeneratorPhoto] = Field(default_factory=list)

    # User requirements
    noise_sensitivity: str = Field(default="medium")
    budget_eur: Optional[float] = Field(None, ge=0)
    primary_goal: str = Field(default="energy_autonomy", description="Primary goal of wind generator")


class WindGeneratorAnalysisResult(BaseModel):
    """Complete analysis result for wind generator module."""
    model_config = {"from_attributes": True}

    # Module metadata
    module_id: str = Field(default="22_06_windgenerator")
    available: bool = Field(default=True)
    reason: Optional[str] = Field(None, description="Reason if not available")
    analysis_date: date = Field(...)

    # Assessment results
    existing_installation_assessment: Optional[InstallationAssessment] = Field(None)
    visual_assessment: Optional[VisualWindGeneratorAssessment] = Field(None)
    yield_estimate: Optional[YieldEstimate] = Field(None)
    energy_balance: Optional[EnergyBalanceWind] = Field(None)
    vibration_assessment: Optional[VibrationAssessment] = Field(None)
    noise_assessment: Optional[NoiseAssessment] = Field(None)

    # Faults found
    faults: list[FaultFinding] = Field(default_factory=list)

    # Recommendations
    recommendation: Optional[WindGeneratorRecommendation] = Field(None)
    maintenance_schedule: Optional[MaintenanceSchedule] = Field(None)
    lifecycle_cost: Optional[LifecycleCostAnalysis] = Field(None)

    # Scoring
    overall_score: Optional[float] = Field(None, ge=0, le=100, description="Overall wind generator system score")
    sub_scores: dict[str, float] = Field(default_factory=dict, description="Sub-category scores")

    # Confidence and fusion
    structured_confidence: ConfidenceLevel = Field(default=ConfidenceLevel.ESTIMATED)
    visual_confidence: ConfidenceLevel = Field(default=ConfidenceLevel.VISUAL_INSUFFICIENT)
    fusion_weight_structured: float = Field(default=0.60, ge=0, le=1)
    fusion_weight_visual: float = Field(default=0.40, ge=0, le=1)
    fused_score: Optional[float] = Field(None, ge=0, le=100, description="Score after structured/visual fusion")

    # Suggestions
    suggestions_de: list[str] = Field(default_factory=list, description="Improvement suggestions in German")
    warnings_de: list[str] = Field(default_factory=list, description="Warnings in German")
    next_steps_de: list[str] = Field(default_factory=list, description="Recommended next steps in German")
```

---

## ANHANG S — Erweiterte Berechnungsbeispiele

### S.1 Vollständige Dimensionierung: Hallberg-Rassy 40, Blauwasser

**Ausgangsdaten:**
- Boot: HR 40, 12,2m, Segelyacht
- System: 12V, LiFePO4 400 Ah
- Verbrauch: 200 Ah/Tag (Autopilot 5A×12h, Kühlschrank 4A×24h, Navigation 2A×12h, Beleuchtung 3A×6h, Sonstiges 2A×12h)
- Solar vorhanden: 400 Wp → ~130 Ah/Tag (Atlantik-Überquerung)
- Defizit durch Wind zu decken: 200 - 130 = 70 Ah/Tag
- Sicherheitsfaktor: ×1,5 → 105 Ah/Tag soll Wind liefern
- Fahrtgebiet: Passatroute (CF = 0,28)
- Montage: Heckarch, 4,5m über Wasser

**Berechnung Nennleistung:**
```
P_nenn = (Bedarf_Ah × U_batt) / (CF × 24 × η_system)
P_nenn = (105 × 12) / (0,28 × 24 × 0,75)
P_nenn = 1.260 / 5,04
P_nenn = 250 W

→ Mindestens 300 W Nennleistung empfohlen
→ 350–400 W Klasse optimal (Reserve für schwache Tage)
```

**Höhenkorrektur:**
```
Höhenfaktor bei 4,5m = 0,91 (vs. 10m Referenz)
Leistungsfaktor = 0,91³ = 0,75
Korrigierte Nennleistung: 250 / 0,75 = 333 W
→ Bestätigt: 350 W Klasse (Superwind 350) ist korrekte Wahl
```

**Kabelquerschnitt-Berechnung:**
```
Kabellänge (einfach): 9m (Arch → Regler unter Achterkoje)
Max. Strom: 25A (Superwind 350 bei 12V)
Erlaubter Spannungsfall: 3% von 14,4V = 0,432V
Querschnitt = (2 × L × I) / (κ × ΔU)
         = (2 × 9 × 25) / (56 × 0,432)
         = 450 / 24,2
         = 18,6 mm²
→ Nächster Standard: 25 mm² (Reserve)
```

**Eigenfrequenz-Check Montage:**
```
Halterrohr: SS316L, 48,3mm × 3,2mm, freie Länge 1,8m
E = 193.000 N/mm² (SS316L)
I = π/64 × (48,3⁴ - 41,9⁴) = 90.612 mm⁴
m = 7,5 kg (Superwind 350)
L = 1.800 mm

f_eigen = (1/2π) × √(3 × 193.000 × 90.612 / (7,5 × 1.800³ × 10⁻⁹))
       = (1/6,28) × √(3 × 193.000 × 90.612 / (7,5 × 5,832))
       = (1/6,28) × √(52.536 × 10⁶ / 43,74)
       = (1/6,28) × √(1.201.095)
       = (1/6,28) × 1.096
       = 174 Hz

Anregung bei Nenndreh zahl (800 U/min, 3 Blätter):
f_rotor = 800/60 = 13,3 Hz
f_blatt = 13,3 × 3 = 40 Hz

f_eigen (174 Hz) >> f_blatt (40 Hz) → KEIN Resonanzrisiko ✓
```

**Erwarteter Tagesertrag auf Passatroute:**
```
E_tag = P_nenn × CF × 24 × η_system × Höhenfaktor
     = 350 × 0,28 × 24 × 0,75 × 0,75
     = 350 × 0,28 × 24 × 0,5625
     = 1.323 Wh/Tag
     = 1.323 / 12 = 110 Ah/Tag

→ Bedarf (105 Ah/Tag) wird gedeckt ✓
→ Solar (130 Ah) + Wind (110 Ah) = 240 Ah/Tag > 200 Ah Verbrauch ✓
→ Überschuss: 40 Ah/Tag → kein Dieselgenerator nötig
```

### S.2 Wirtschaftlichkeitsberechnung: Vergleich Szenarien

**Szenario A: Nur Solar (600 Wp)**
- Investition: 600 Wp × €3/Wp + Montage = €2.800
- Ertrag Passat: ~190 Ah/Tag
- Ertrag Nordsee Winter: ~40 Ah/Tag
- Defizit Winter: 200 - 40 = 160 Ah/Tag → Generator 2,5h/Tag × €4/h = €10/Tag

**Szenario B: Solar (400 Wp) + Wind (350 W)**
- Investition Solar: 400 Wp × €3/Wp + Montage = €2.000
- Investition Wind: €2.200 + €800 Montage = €3.000
- Gesamt-Investition: €5.000
- Ertrag Passat: Solar 130 + Wind 110 = 240 Ah/Tag (Überschuss)
- Ertrag Nordsee Winter: Solar 25 + Wind 80 = 105 Ah/Tag
- Defizit Winter: 200 - 105 = 95 Ah/Tag → Generator 1,5h/Tag × €4/h = €6/Tag

**Szenario C: Solar (400 Wp) + Dieselgenerator**
- Investition Solar: €2.000
- Investition Honda EU22i: €2.200
- Gesamt-Investition: €4.200
- Ertrag Passat: Solar 130 Ah + Generator 1,2h/Tag = 200 Ah
- Diesel Winter: 2,5h/Tag × €4/h = €10/Tag
- Lärm: 57 dB(A) Honda EU22i, Abgase, Wartung

**20-Jahres-Kostenvergleich (200 Seetage/Jahr, 50% Winter):**

| Position | A: Nur Solar | B: Solar+Wind | C: Solar+Generator |
|----------|-------------|---------------|-------------------|
| Investition | €2.800 | €5.000 | €4.200 |
| Diesel/Jahr | €500 | €200 | €700 |
| Wartung/Jahr | €50 | €150 | €300 |
| Ersatzteile 20J | €600 | €1.500 | €3.000 |
| **Gesamt 20 Jahre** | **€13.800** | **€12.500** | **€24.200** |
| Lärm-Komfort | Lautlos | Moderate Wind | Laut Generator |
| Autonomie | Mittel | Hoch | Niedrig |

**Ergebnis:** Solar + Wind (Szenario B) ist langfristig die günstigste UND komfortabelste Lösung für Blauwassersegler.

### S.3 Vibrations-Troubleshooting: Rechenbeispiel

**Problem:** Bavaria 46, D400 auf 2,4m Edelstahlrohr, starke Vibration bei 13–16 kn

**Schritt 1: Eigenfrequenz des Ist-Zustandes berechnen**
```
Rohr: SS316L, 48,3mm × 2,5mm, L = 2.400mm
E = 193.000 N/mm²
I = π/64 × (48,3⁴ - 43,3⁴) = 79.234 mm⁴
m = 8,0 kg (D400)

f_eigen = (1/2π) × √(3EI / mL³)
        = 0,159 × √(3 × 193.000 × 79.234 / (8,0 × 2.400³ × 10⁻⁹))
        = 0,159 × √(45.885 × 10⁶ / (8,0 × 13,824))
        = 0,159 × √(45.885 × 10⁶ / 110,6)
        = 0,159 × √(414.876)
        = 0,159 × 644
        = 102 Hz
```

Hmm, das scheint hoch. Prüfen wir die Rotor-Grundfrequenz:
```
D400 bei 13 kn: ca. 400 U/min → f_rotor = 6,7 Hz
D400 bei 16 kn: ca. 550 U/min → f_rotor = 9,2 Hz
f_blatt (5 Blätter): 33–46 Hz

f_eigen (102 Hz) >> alle Anregungen → sollte kein Problem sein
```

**Erkenntnis:** Berechnung geht von perfekter Einspannung aus. In der Praxis:
- Rohrfuß ist NICHT perfekt eingespannt (Klemme statt Schweißung)
- Effektive Steifigkeit der Basis nur ~40% der theoretischen
- Korrigierte f_eigen = 102 × 0,63 ≈ 64 Hz → immer noch OK

**Wahre Ursache:** Weitere Untersuchung zeigt: Die Gesamtstruktur (Heckkorb + Ausleger) hat eine Eigenfrequenz bei 8 Hz. Der Heckkorb selbst schwingt!

**Lösung:** Verstärkung des Heckkorbs an den Befestigungspunkten zum Rumpf + Diagonalstreben.

### S.4 Apparent-Wind-Korrektur: Detailberechnung

**Situation:** ARC-Überquerung, Vorwindkurs, 18 kn wahrer Wind, 7 kn Bootsgeschwindigkeit

```
Wahrer Wind: v_true = 18 kn = 9,26 m/s
Bootsgeschwindigkeit: v_boat = 7 kn = 3,60 m/s
Kurs zum wahren Wind: θ = 170° (fast DDW mit Genaker)

Apparent Wind (Vektorberechnung):
v_apparent = √(v_true² + v_boat² - 2 × v_true × v_boat × cos(θ))
           = √(9,26² + 3,60² - 2 × 9,26 × 3,60 × cos(170°))
           = √(85,75 + 12,96 - 66,67 × (-0,985))
           = √(85,75 + 12,96 + 65,67)
           = √(164,38)
           = 12,82 m/s → Hmm, das wäre MEHR als wahrer Wind!

Korrektur — bei fast Vorwindkurs:
v_apparent = v_true - v_boat × cos(180° - θ)
           Vereinfacht für DDW (θ = 180°):
           v_apparent = v_true - v_boat = 18 - 7 = 11 kn

Für θ = 170°:
v_apparent_component_along_wind = v_true - v_boat × cos(10°)
= 18 - 7 × 0,985 = 18 - 6,9 = 11,1 kn

→ Effektiver Wind am Generator: ~11 kn (statt 18 kn wahrer Wind)
→ Leistungsreduktion: (11/18)³ = 0,23 → nur 23% der stationären Leistung!
```

**Praxiskonsequenz:** Bei Vorwindkursen (typisch ARC/Passatroute) erzeugt der Windgenerator deutlich weniger als auf dem Ankerplatz bei gleichem wahren Wind. Dies wird in Ertragsschätzungen oft nicht berücksichtigt und erklärt, warum reale Erträge auf Überquerungen unter den Erwartungen liegen.

**Korrektur-Tabelle für Passatroute:**

| Wahrer Wind | DDW (180°) | Raumer (150°) | Halbwind (90°) |
|-------------|-----------|---------------|----------------|
| 15 kn, 6 kn Boot | 9 kn → 15 W | 10,5 kn → 25 W | 16,2 kn → 95 W |
| 18 kn, 7 kn Boot | 11 kn → 30 W | 13 kn → 55 W | 19,4 kn → 180 W |
| 20 kn, 7,5 kn Boot | 12,5 kn → 50 W | 14,5 kn → 80 W | 21,4 kn → 240 W |
| 22 kn, 8 kn Boot | 14 kn → 70 W | 16 kn → 100 W | 23,3 kn → 310 W |

### S.5 Lebenszykluskosten: Detailrechnung Superwind 350

**Annahmen:**
- Betrieb: 200 Seetage/Jahr, davon 150 mit >8 kn Wind
- Region: 50% Mittelmeer, 50% Atlantik
- Mittlerer CF: 0,22

**Initiale Kosten:**
| Position | Betrag |
|----------|--------|
| Superwind 350 (12V) | €2.200 |
| Laderegler (Genasun GVB-8) | €350 |
| Montagerrohr SS316L 48,3×3,2mm, 2m | €180 |
| Abspannung (2× Dyneema + Hardware) | €120 |
| Kabel 25mm² verzinnt, 20m | €160 |
| Kurzschlussschalter IP67 | €45 |
| Sicherung + Trennschalter | €65 |
| Kabelschuhe, Schrumpfschlauch, Kleinkram | €80 |
| Arbeitszeit Eigeneinbau: 16h × €0 | €0 |
| **Gesamt Installation** | **€3.200** |

**Laufende Kosten (jährlich):**
| Position | Betrag/Jahr |
|----------|-------------|
| Schmierung, Reinigung | €20 |
| Sichtprüfung (Eigenarbeit) | €0 |
| Rücklagen für Verschleißteile | €80 |
| **Jährliche Kosten** | **€100** |

**Ersatzteile über 20 Jahre:**
| Position | Zeitpunkt | Kosten |
|----------|-----------|--------|
| Lager-Kit #1 | Jahr 6 | €180 |
| Lager-Kit #2 | Jahr 12 | €180 |
| Lager-Kit #3 | Jahr 18 | €180 |
| Blatt-Satz #1 | Jahr 8 | €420 |
| Blatt-Satz #2 | Jahr 15 | €420 |
| Regler-Ersatz | Jahr 12 | €350 |
| Kabel-Erneuerung | Jahr 14 | €200 |
| **Summe Ersatzteile** | | **€1.930** |

**20-Jahres-Gesamtkosten:**
```
Initial: €3.200
Laufend: 20 × €100 = €2.000
Ersatzteile: €1.930
GESAMT: €7.130
```

**Ertrag über 20 Jahre:**
```
Tagesertrag (Mittel): 350W × 0,22 × 24h × 0,75 = 1.386 Wh = 1,39 kWh/Tag
Jahresertrag: 1,39 × 200 Seetage = 278 kWh/Jahr
20-Jahres-Ertrag: 278 × 20 = 5.560 kWh

Effektive Kosten pro kWh: €7.130 / 5.560 = €1,28/kWh
```

**Vergleich mit Alternativen:**
| Energiequelle | Kosten/kWh (20J) | Bemerkung |
|---------------|-------------------|-----------|
| Windgenerator (Superwind) | €1,28/kWh | Geräuscharm, autonom |
| Dieselgenerator Honda EU22i | €1,85/kWh | Lärm, Abgase, Wartung |
| Landstrom (Marina) | €0,80/kWh | Nur bei Liegeplatz |
| Lichtmaschine (Hauptmotor) | €2,50/kWh | Nur unter Motor |
| Solar 400Wp | €0,45/kWh | Nur tagsüber, wetterabhängig |

**Fazit:** Wind allein ist teurer als Solar pro kWh, aber der Mehrwert liegt in der Nachtproduktion und der Komplementarität bei Schlechtwetter. Die Kombination Solar+Wind senkt die Gesamtkosten pro kWh erneuerbarer Energie.

---

## ANHANG T — Montage-Detailanleitungen

### T.1 Standard-Heckarch-Montage (Schritt-für-Schritt)

**Voraussetzungen:**
- Existierende Heckarch (Edelstahl, mind. 30mm Rohrdurchmesser Arch)
- Windgenerator mit 48,3mm Montagerrohr-Aufnahme
- Montagerrohr SS316L 48,3mm × 3,2mm, Länge nach Berechnung

**Material-Checkliste:**
```
□ Montagerrohr SS316L 48,3×3,2mm, L = [berechnet]
□ Rohrschelle/Flansch für Arch-Befestigung (mind. 2 Stück)
□ Schrauben A4/316L M10 für Flansche
□ Verstärkungsplatte (wenn Arch-Rohr < 30mm Wandstärke)
□ Abspannung: 2-3× Dyneema SK78 (5mm) + Spannschlösser + Augbolzen
□ Kabel: [berechneter Querschnitt] × [Länge × 2 + 20% Reserve]
□ Stecker/Kabelschuhe (verzinnt, Ringform)
□ Schrumpfschlauch (doppelwandig, mit Kleber)
□ Kabeldurchführung (Decks-Kabeldurchführung IP68)
□ Zugentlastung (min. 2 Stück im Verlauf)
□ UV-Schutz-Schlauch oder Spiralschlauch für freiliegende Kabel
□ Kurzschlussschalter IP67
□ Sikaflex 291i oder 3M 4200 für Dichtung
□ Duralac (Korrosionsschutz Al/SS-Kontakt)
□ Loctite 243 (mittelfest) für Schrauben
```

**Arbeitsschritte:**

1. **Planung und Anzeichnen**
   - Optimale Position auf Arch bestimmen (Mittellinie, höchster Punkt)
   - Rotor-Sicherheitskreis anzeichnen (Radius = Rotordurchmesser/2 + 0,5m)
   - Prüfen: Sicherheitskreis schneidet keine Aufenthalts- oder Arbeitsbereiche?
   - Prüfen: Rotor frei von Backstagen, Fallen, Lazyjacks?
   - Prüfen: Raum für Gierbewegung (360° frei)?

2. **Rohrmontage vorbereiten**
   - Rohrende entgraten (innen und außen)
   - Flansche aufpassen, Löcher bohren wenn nötig
   - Duralac auf alle Al/SS-Kontaktflächen auftragen
   - Flansche mit Loctite-gesicherten A4-Schrauben befestigen

3. **Rohr auf Arch befestigen**
   - Rohr in Flansche einsetzen
   - Ausrichtung: Senkrecht ±1° (Wasserwaage bei ruhigem Wasser)
   - Schrauben anziehen (Drehmoment nach Hersteller, typisch 35–45 Nm für M10)
   - Kontrollmessung: Rohr darf nicht kippen wenn 10 kg seitlich belastet

4. **Abspannung installieren**
   - Augbolzen an Arch/Deck befestigen (mind. 2, besser 3 Richtungen)
   - Dyneema ablängen (Seillänge + 20% für Spleiße/Knoten)
   - Am Rohr befestigen: oberes Drittel der freien Länge
   - Spannschlösser einbauen, handfest anziehen (nicht Vorspannung!)
   - Endgültige Spannung erst NACH Generator-Montage

5. **Generator auf Rohr montieren**
   - Generator auf Rohr setzen (Passgenauigkeit prüfen)
   - Klemmschrauben handfest anziehen
   - Ausrichtung prüfen (Rotor-Ebene horizontal)
   - Endgültig anziehen (Herstellervorgabe, typisch 25–30 Nm)
   - Kabel durch Rohr oder außen geführt? (Innere Führung bevorzugt)

6. **Kabelverlegung**
   - Kabel vom Generator zum Regler verlegen
   - Min. eine volle Schlaufe am Gierlager für Drehfreiheit
   - Zugentlastungen alle 1–1,5m
   - UV-Schutz auf freiliegenden Abschnitten
   - Kabeldurchführung durch Deck abdichten (Sikaflex)
   - Kabelschuhe crimpen + löten + Schrumpfschlauch

7. **Elektrischer Anschluss**
   - Regler montieren (trocken, belüftet, nahe Batterie)
   - Generator → Regler anschließen (3-Phasen oder DC je nach Typ)
   - Regler → Batterie anschließen (über Sicherung + Trennschalter)
   - Kurzschlussschalter zwischen Generator und Regler installieren
   - Alle Verbindungen auf festen Sitz und Korrosionsfreiheit prüfen

8. **Inbetriebnahme**
   - Bremse/Kurzschluss aktiviert lassen
   - Alle Anschlüsse nochmals prüfen
   - Batteriespannung messen (Referenzwert)
   - Bei Schwachwind (<12 kn): Bremse lösen
   - Beobachten: Rotor dreht? Anlauf OK?
   - Ladestrom messen: plausibel?
   - Vibration fühlen: auffällig?
   - Geräusch: akzeptabel?
   - Windstärke steigern lassen (natürlich oder Testfahrt)
   - Bei 20+ kn: alle Werte nochmals prüfen

9. **Dokumentation**
   - Alle Messwerte dokumentieren (Referenz für spätere Diagnose)
   - Foto der Installation (für Versicherung)
   - Wartungsplan erstellen
   - Sturm-SOP der Crew mitteilen

### T.2 Abspannungs-Dimensionierung

**Berechnung der Abspannungskraft:**

```
F_wind_max = ½ × ρ × Cd × A_rotor × v²_max

Wobei (Stillstand, gebremster Rotor):
- ρ = 1,225 kg/m³
- Cd = 1,2 (gebremster Rotor als Scheibe)
- A_rotor = π × (1,17/2)² = 1,075 m² (Superwind 350)
- v_max = 30 m/s (≈60 kn, Design-Überlebensbedingung)

F_wind = 0,5 × 1,225 × 1,2 × 1,075 × 30²
       = 0,5 × 1,225 × 1,2 × 1,075 × 900
       = 712 N ≈ 73 kg

Hebelarm: L_rohr = 2,0 m
Moment am Fußpunkt: M = 712 × 2,0 = 1.424 Nm

Abspannung bei 1,5m Höhe (0,75 × L):
Zugkraft pro Stage (2 Stages, 45° Winkel):
F_stage = M / (h_stage × cos(45°) × 2)
        = 1.424 / (1,5 × 0,707 × 2)
        = 1.424 / 2,12
        = 672 N ≈ 68 kg pro Stage

Sicherheitsfaktor 4:
F_bruch_min = 672 × 4 = 2.688 N ≈ 274 kg

Dyneema SK78, 5mm: Bruchlast ~2.400 kg → WEIT ausreichend ✓
(Edelstahldraht 3mm: Bruchlast ~500 kg → ebenfalls ausreichend)
```

### T.3 Eigenfrequenz-Schnellbestimmung (Praxismethode)

**Methode ohne Berechnung (Klopftest):**

1. Generator abbauen (nur Rohr steht)
2. Gewicht equivalent zum Generator (Wasserflasche ~8 kg) oben befestigen
3. Seitlich anstoßen und Schwingungen zählen:
   - 10 Schwingungen messen, Zeit mit Stoppuhr
   - f_eigen = 10 / gemessene_Zeit [Hz]
4. MIT Generator montiert: erneut messen (Verifikation)

**Smartphone-Methode:**
1. PhyPhox oder ähnliche App installieren
2. Smartphone am Rohr-Fußpunkt befestigen
3. Generator laufen lassen bei verschiedenen Windstärken
4. FFT-Analyse in der App zeigt dominante Frequenzen
5. Resonanz = wenn dominante Frequenz mit steigender Drehzahl anwächst und dann wieder abfällt

**Grenzwerte:**
- f_eigen > 2 × f_rotor (bei max. Betriebsdrehzahl): SICHER
- f_eigen > 1,5 × f_rotor: AKZEPTABEL
- f_eigen im Bereich 0,8–1,2 × f_rotor: RESONANZ-GEFAHR → Maßnahme erforderlich

---

## ANHANG U — Regionale Einsatzempfehlungen

### U.1 Nordsee / Deutsche Bucht

| Parameter | Wert |
|-----------|------|
| Mittlere Windgeschwindigkeit | 14–18 kn (Jahresmittel) |
| Vorherrschende Richtung | SW–W |
| Bester Monat | Oktober–März (Windertrag) |
| Schlechtester Monat | Juni–August (oft Flauten) |
| CF (Jahresmittel) | 0,25 |
| Empfohlener Generatortyp | HAWT 350–400 W |
| Empfohlenes Modell | Superwind 350 (Zuverlässigkeit bei Starkwind) |
| Besonderheit | Häufig >30 kn → robuste Sturmregelung zwingend |
| Salzbelastung | Sehr hoch → Korrosionsschutz kritisch |
| Kombination mit Solar | Winter: Wind dominiert. Sommer: Solar dominiert |

### U.2 Ostsee

| Parameter | Wert |
|-----------|------|
| Mittlere Windgeschwindigkeit | 10–14 kn (Jahresmittel) |
| Vorherrschende Richtung | W–SW (wechselnd) |
| CF (Sommer) | 0,14 |
| CF (Winter) | 0,26 |
| Empfohlener Generatortyp | 5/6-Blatt HAWT (guter Schwachwindstart) |
| Empfohlenes Modell | Rutland 1200 oder Silentwind 400 |
| Besonderheit | Viele Leichtwindtage im Sommer, Eis im Winter |
| Salzbelastung | Mittel (Brackwasser) |

### U.3 Mittelmeer (West)

| Parameter | Wert |
|-----------|------|
| Mittlere Windgeschwindigkeit | 8–12 kn (Jahresmittel, küstennah) |
| Vorherrschende Richtung | Variabel, Mistral NW |
| CF (Jahresmittel) | 0,15 |
| Empfohlener Generatortyp | HAWT mit gutem Schwachwindstart oder VAWT |
| Empfohlenes Modell | Silentwind 400 (leise in Buchten) |
| Besonderheit | Mistral-Phasen bringen kurze Starkwind-Erträge, ansonsten oft Flaute |
| Salzbelastung | Hoch |
| Kombination | Solar dominiert klar, Wind nur Ergänzung |

### U.4 Karibik / Passatgürtel

| Parameter | Wert |
|-----------|------|
| Mittlere Windgeschwindigkeit | 15–22 kn (Trade Winds) |
| Vorherrschende Richtung | NE–E (sehr konsistent) |
| CF (Jahresmittel) | 0,24 |
| Empfohlener Generatortyp | HAWT 350 W |
| Empfohlenes Modell | Superwind 350 (bewährt in Passatregion) |
| Besonderheit | Konsistenter Wind, ideales Windgenerator-Revier |
| Hurikansaison | Juni–November: Generator abbauen oder sichern! |
| Salzbelastung | Sehr hoch (Gischt) |
| Apparent Wind | Beachten auf Vorwindkursen (30–50% weniger Ertrag) |

### U.5 Patagonien / Südatlantik

| Parameter | Wert |
|-----------|------|
| Mittlere Windgeschwindigkeit | 20–30 kn (extrem windig) |
| CF | 0,34 |
| Empfohlener Generatortyp | Robuster HAWT mit passiver Pitch |
| Empfohlenes Modell | Superwind 350 (einzig empfehlenswert für extreme Bedingungen) |
| Besonderheit | Williwaws (Fallböen 60+ kn), Montage MUSS für Extrembedingungen ausgelegt sein |
| Salzbelastung | Extrem (Gischt + Sprühwasser permanent) |
| Montage | Überdimensioniert: dickwandiges SS-Rohr, 3-fach abgespannt, kurz halten |

### U.6 Südpazifik (Tropen / Atolle)

| Parameter | Wert |
|-----------|------|
| Mittlere Windgeschwindigkeit | 8–14 kn (variable, geschützte Lagunen oft windarm) |
| CF | 0,13 |
| Empfohlener Generatortyp | Leiser HAWT oder VAWT (Inselsensibilität) |
| Empfohlenes Modell | Silentwind 400 mit Nachtmodus |
| Besonderheit | In Lagunen oft windstill, auf offenen Ankerplätzen besser |
| Zyklonsaison | November–April: Generator sichern |
| Kombination | Solar dominiert stark (Tropen = hohe Einstrahlung), Wind marginal |

---

## ANHANG V — Normenkonformität und Zertifizierung

### V.1 Relevante Prüfnormen für kleine Windgeneratoren

| Norm | Titel | Prüfumfang | Relevanz Marine |
|------|-------|-----------|-----------------|
| IEC 61400-2:2013 | Design requirements for small wind turbines | Gesamtdesign, Sicherheit, Dauerfestigkeit | Grundnorm |
| IEC 61400-12-1 | Power performance measurements | Leistungskurve unter Realbedingungen | Herstellerangaben-Verifikation |
| IEC 61400-11 | Acoustic noise measurement | Geräuschpegelmessung | Lärm-Zertifizierung |
| EN 50583 | Building integrated PV (analog für BIPV+Wind) | Integration in Strukturen | Arch-Integration |
| ISO 10133:2012 | Electrical systems DC | Kabelverlegung, Absicherung, Erdung | Pflicht für Yachten |
| ISO 13297:2014 | Electrical systems AC | AC-Seite (falls Wechselrichter) | Selten relevant |
| ABYC E-11 | AC and DC electrical systems | US-Standard, oft strenger als ISO | US-Flagge/Versicherung |

### V.2 CE-Konformität für Marine-Windgeneratoren

Ein Windgenerator auf einer Yacht unterliegt:
- **Niederspannungsrichtlinie 2014/35/EU:** Elektrische Sicherheit
- **EMV-Richtlinie 2014/30/EU:** Elektromagnetische Verträglichkeit
- **Maschinenrichtlinie 2006/42/EG:** Mechanische Sicherheit

Der Windgenerator selbst muss CE-gekennzeichnet sein. Die Installation auf der Yacht muss den Anforderungen der Sportbootrichtlinie 2013/53/EU entsprechen, wenn sie werftmäßig erfolgt.

### V.2.1 EMV-Anforderungen im Detail

Windgeneratoren können elektromagnetische Störungen verursachen durch:

**Störquellen:**
| Komponente | Störmechanismus | Frequenzbereich | Betroffene Geräte |
|-----------|-----------------|-----------------|-------------------|
| Gleichrichter (Regler) | Oberwellen der Kommutierung | 100 Hz – 10 kHz | UKW-Empfang, SSB |
| PWM-Bremswiderstand | Schaltfrequenz-Oberwellen | 10–100 kHz | GPS, AIS, UKW |
| Generator-Kabel (lang) | Antennenwirkung | 1–30 MHz | KW-Funk, SSB |
| Bürstengenerator (alt) | Funkentstörung | Breitband | Alle Empfänger |
| MPPT-Regler | Schaltregler-Emissionen | 50–500 kHz | Navigationselektronik |

**Abhilfemaßnahmen:**
| Maßnahme | Wirksamkeit | Kosten |
|----------|------------|--------|
| Ferritkerne auf Generator-Kabel (je 2× am Generator-Ende und Regler-Ende) | Hoch | €20–€40 |
| Geschirmtes Kabel (selten nötig) | Sehr hoch | €100–€200 Aufpreis |
| Abstand Generator-Kabel zu Antennenkabeln (>30cm) | Mittel | €0 |
| EMV-Filter am Regler-Eingang | Hoch | €50–€100 |
| Kabel verdrillen (3-Phasen eng zusammen) | Mittel | €0 |
| Regler weit von Antennenkoppler/Funkgerät montieren | Mittel | €0 |

**Prüfmethode nach Installation:**
1. UKW-Radio auf leeren Kanal stellen, Generator anhalten → Grundrauschen notieren
2. Generator laufen lassen → zusätzliches Rauschen? Pfeifton bei bestimmter Drehzahl?
3. AIS-Empfang prüfen (Anzahl empfangener Schiffe mit/ohne Generator)
4. GPS-Signalstärke vergleichen (mit/ohne Generator)
5. Bei Problemen: Ferritkerne schrittweise hinzufügen bis Störung verschwindet

### V.2.2 Blitzschutz-Integration

**Risikobewertung:**
Der Windgenerator ist oft der höchste Punkt am Heck der Yacht. Bei Masttop-Montage sogar der höchste Punkt überhaupt. Das Blitzschlag-Risiko ist proportional zur exponierten Höhe.

**Blitzschutz-Konzept für Windgeneratoren:**

```
Stufe 1: Äußerer Blitzschutz (Ableitung)
  ├─ Montagehalter leitend zum Kiel verbinden
  ├─ Kupferband ≥16mm² (besser 25mm²) vom Halterfuß zum Kiel/Masseplatte
  ├─ Verbindungen: Schrauben, NICHT Klemmen (Blitzstrom!)
  └─ Bei GFK-Booten: Kupferplatte am Unterwasserschiff (min. 0,1m²)

Stufe 2: Innerer Blitzschutz (Überspannungsschutz)
  ├─ Varistoren (MOV) am Regler-Eingang (3× Y-Schaltung, Generator→Erde)
  ├─ Varistoren am Regler-Ausgang (Batterie, ±, gegen Erde)
  ├─ Gasableiter als Grobschutz vor den MOVs
  └─ Sicherung NACH Überspannungsschutz (schmilzt im Worst Case)

Stufe 3: Abkopplung (bei Gewitter)
  ├─ Generator bremsen (reduziert induzierte Spannungen im rotierenden Generator)
  ├─ Optional: Generator-Kabel über Schalter von Regler trennen
  └─ Empfindliche Elektronik abklemmen (Plotter, Funk → Batterieschalter)
```

**Schadensbild nach Blitzereignis:**
| Typischer Schaden | Häufigkeit | Reparatur |
|-------------------|-----------|-----------|
| Regler zerstört | 90% | Tausch €150–€500 |
| Generator-Wicklung teilgeschädigt | 40% | Generator-Tausch €400–€1.200 |
| Magnete entmagnetisiert | 20% | Generator-Tausch |
| Kabel-Isolation durchschlagen | 30% | Kabel erneuern |
| Lager punktgeschweißt | 10% | Lager tauschen |
| Batterie beschädigt (BMS bei LiFePO4) | 50% | BMS/Batterie tauschen |
| Elektronik an Bord (Plotter, Funk) | 60% | Gerätewechsel |

**Hinweis:** Ein vollständiger Blitzschutz für Marine-Windgeneratoren ist technisch komplex und wirtschaftlich oft fragwürdig. Der Schaden durch einen direkten Blitzeinschlag übersteigt fast immer die Kosten eines Schutzkonzepts. Empfehlung: Basis-Erdung + Varistoren (Investition ~€100–€200) reduzieren das Risiko bei indirekten Einschlägen/Induktion erheblich. Bei direktem Einschlag helfen nur robust dimensionierte Ableitung und Versicherung.

### V.3 Versicherungsrechtliche Aspekte

| Thema | Anforderung | Konsequenz bei Nichtbeachtung |
|-------|-------------|-------------------------------|
| Professionelle Montage | Empfohlen, nicht zwingend (Eigeneinbau erlaubt) | Bei Schäden: Nachweis fachgerechter Installation |
| CE-Kennzeichnung Generator | Zwingend für Versicherungsschutz | Versicherer kann Leistung verweigern |
| Sturmregelung | Muss vorhanden und funktionsfähig sein | Grob fahrlässig wenn Generator bei Sturm ungebremst |
| Erdung/Blitzschutz | Empfohlen, nicht zwingend | Kein Versicherungsausschluss, aber Best Practice |
| Dokumentation | Installationsfoto, Datenblatt aufbewahren | Erleichtert Schadenregulierung |
| Windgenerator-Schäden an Dritten | Haftpflicht deckt Personenschäden durch Rotor | Sicherheitsabstand dokumentieren |

---

---

## ANHANG W — Checklisten und Formulare

### W.1 Jährliche Inspektions-Checkliste

```
WINDGENERATOR — JÄHRLICHE INSPEKTION
═══════════════════════════════════════
Boot: _________________ Datum: _________
Generator: _____________ Betriebsstunden: _______

ROTOR UND BLÄTTER
□ Blätter visuell auf Risse prüfen (alle Blätter, Ober- und Unterseite)
□ Blätter auf UV-Schäden prüfen (Verfärbung, Mattheit, Rauigkeit)
□ Blätter auf Delamination prüfen (Klopftest: hell = OK, dumpf = Problem)
□ Blattbefestigungsschrauben auf festen Sitz prüfen (Drehmoment!)
□ Blatt-Unwucht prüfen (Generator bei Schwachwind frei drehen lassen, Vibrationscheck)
□ Nabe auf Risse und Korrosion prüfen
□ Heckflosse/Windfahne auf festen Sitz und Unversehrtheit prüfen
  Befund: ________________________________________________

LAGER UND MECHANIK
□ Rotor von Hand drehen: Leichtgängigkeit prüfen
□ Rotor von Hand drehen: Schleifgeräusche? (→ Lagerproblem)
□ Rotor von Hand drehen: Rastmomente? (bei Coreless: keine!)
□ Axialspiel prüfen: Rotor in Achsrichtung bewegen (<0,1mm OK)
□ Radialspiel prüfen: Rotor seitlich kippen (<0,05mm OK)
□ Gierlager (Windnachführung) auf Leichtgängigkeit prüfen
□ Gierlager schmieren (Teflon-Spray oder Lithium-Fett, je nach Hersteller)
  Befund: ________________________________________________

MONTAGE UND STRUKTUR
□ Alle Schraubverbindungen am Halter nachziehen (Drehmomentschlüssel!)
□ Montagerrohr auf Risse prüfen (besonders am Fußpunkt/Schweißnaht)
□ Abspannungen (Stages) auf Spannung und Zustand prüfen
□ Abspannungs-Endverbindungen auf Korrosion/Ermüdung prüfen
□ Halter auf Korrosion prüfen (besonders Kontaktflächen verschiedener Metalle)
□ Duralac/Isolation zwischen Al und SS noch intakt?
  Befund: ________________________________________________

ELEKTRIK
□ Alle Kabelanschlüsse auf festen Sitz und Korrosionsfreiheit prüfen
□ Kabel auf Scheuerstellen prüfen (besonders am Gierlager und Durchführungen)
□ Kabel-Isolation auf UV-Schäden prüfen
□ Zugentlastungen auf festen Sitz prüfen
□ Decksdurchführung auf Dichtigkeit prüfen
□ Sicherung prüfen (optisch, Widerstand)
□ Kurzschlussschalter auf Funktion testen (bei Schwachwind: schalten → Rotor muss stoppen)
□ Regler: LED/Anzeige funktioniert?
□ Regler: Spannung Ein/Aus messen, plausibel?
□ Batteriemonitor: Windgenerator-Ertrag wird korrekt angezeigt?
  Befund: ________________________________________________

FUNKTIONSTEST
□ Bremse aktivieren: Rotor stoppt zuverlässig?
□ Bremse lösen: Rotor dreht an bei ausreichend Wind?
□ Leistungscheck: Bei bekannter Windstärke → Ertrag mit Herstellerkurve vergleichen
□ Vibrationscheck: Auffällige Vibrationen bei Betriebsdrehzahl?
□ Geräuschcheck: Ungewöhnliche Geräusche? (Schleifen, Klappern, Pfeifen)
  Befund: ________________________________________________

GESAMTBEWERTUNG
□ Alles in Ordnung — nächste Inspektion in 12 Monaten
□ Kleinere Mängel — Maßnahmen dokumentiert:
  _______________________________________________________
□ Größere Mängel — Reparatur zeitnah erforderlich:
  _______________________________________________________
□ Sicherheitsrelevant — Generator stilllegen bis Reparatur erfolgt:
  _______________________________________________________

Inspektion durchgeführt von: ________________
Unterschrift: ________________
```

### W.2 Sturm-Vorbereitungs-Checkliste (Quick Reference Card)

```
WINDGENERATOR — STURM-SOP
══════════════════════════════
An alle Crewmitglieder: Aushängen bei Navigationsecke!

BEI STURMWARNUNG (>35 kn erwartet):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. □ Batterie-Ladezustand prüfen (falls voll → Verbraucher einschalten oder Dump-Load aktivieren)
2. □ Bremse TESTEN (kurz aktivieren, Rotor muss stoppen)
3. □ Bremse AKTIVIEREN
4. □ Falls Bremse nicht hält: Kurzschlussschalter an Deck umlegen
5. □ Alle Schrauben am Halter visuell auf festen Sitz prüfen
6. □ Abspannungen prüfen (Spannung OK?)
7. □ Lose Leinen/Fallen vom Rotor fernhalten (festzurren!)

BEI SCHWEREM STURM (>50 kn erwartet):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

8. □ Generator-Kabel am Regler abklemmen (Blitzschutz)
9. □ Optional: Blätter demontieren (NUR bei Flaute/Wind <10 kn möglich!)
10. □ Optional: Generator komplett abbauen (wenn Zeit und Bedingungen es erlauben)

NACH DEM STURM:
━━━━━━━━━━━━━━━

11. □ Sichtprüfung: Blätter intakt? Halter gerade? Abspannungen OK?
12. □ Kabel anschließen (falls getrennt)
13. □ Bremse lösen bei <20 kn
14. □ Funktion beobachten (erste 30 Minuten)

⚠️ NIEMALS bei drehendem Rotor am Generator arbeiten!
⚠️ NIEMALS in den Rotor greifen!
⚠️ Kurzschlussschalter-Position: _______________ (hier eintragen!)
```

### W.3 Inbetriebnahme-Protokoll

```
WINDGENERATOR — INBETRIEBNAHME-PROTOKOLL
═════════════════════════════════════════════
Datum: _____________ Boot: _________________
Generator: _________ Seriennummer: __________
Installateur: ________________________________

INSTALLATION PRÜFEN
□ Montage gemäß Herstellervorgabe
□ Eigenfrequenz-Check durchgeführt: f_eigen = _____ Hz
□ Kabelquerschnitt berechnet: _____ mm², tatsächlich verlegt: _____ mm²
□ Kabellänge (einfach): _____ m
□ Berechneter Spannungsfall: _____ % (max. 3%)
□ Sicherung: _____ A (Typ: _____)
□ Regler-Modell: _________________
□ Kurzschlussschalter vorhanden: □ Ja □ Nein
□ Erdung/Blitzschutz: □ Ja □ Nein

MESSWERTE BEI INBETRIEBNAHME
Windgeschwindigkeit (gemessen am Generator): _____ kn
Batteriespannung (vor Start): _____ V
Rotor-Drehzahl (geschätzt): _____ U/min

Generator-Leerlaufspannung (3-Phasen, AC):
  Phase A-B: _____ V AC
  Phase B-C: _____ V AC
  Phase A-C: _____ V AC
  (Alle drei müssen ±5% gleich sein)

Ladestrom bei _____ kn: _____ A
Laut Herstellerkurve erwartet: _____ A
Abweichung: _____ % (akzeptabel: <20%)

VIBRATION
□ Nicht spürbar
□ Leicht spürbar am Halter
□ Deutlich spürbar → Frequenz: _____ Hz → Maßnahme: ___________
□ Inakzeptabel → Installation NICHT freigeben

GERÄUSCH
□ Nicht wahrnehmbar
□ Leises Rauschen (akzeptabel)
□ Deutlich wahrnehmbar → Pegel geschätzt: _____ dB(A)
□ Inakzeptabel laut → Maßnahme: ___________

BREMSE
□ Funktioniert: Rotor stoppt innerhalb _____ Sekunden
□ Funktioniert NICHT → Installation NICHT freigeben!

FREIGABE
□ Installation freigegeben für Betrieb
□ Installation NICHT freigegeben — Gründe:
  _______________________________________________________

Unterschrift Installateur: ________________
Unterschrift Eigner: ________________
```

### W.4 Kaufentscheidungs-Matrix (zum Ausfüllen)

```
WINDGENERATOR — BEWERTUNGSMATRIX FÜR KAUFENTSCHEIDUNG
═══════════════════════════════════════════════════════

Mein Boot: _____________ Länge: _____ m  Typ: □ Segel □ Motor □ Kat
Mein Revier: _____________ Typischer Wind: _____ kn
Mein Budget: €_________ Geräuschsensibel: □ Ja □ Nein

                        | Modell 1    | Modell 2    | Modell 3    |
                        | ___________ | ___________ | ___________ |
Nennleistung [W]        | ___________ | ___________ | ___________ |
Preis [€]               | ___________ | ___________ | ___________ |
Gewicht [kg]            | ___________ | ___________ | ___________ |
Geräusch 20kn [dB(A)]  | ___________ | ___________ | ___________ |
Anlauf [kn]             | ___________ | ___________ | ___________ |
Garantie [Jahre]        | ___________ | ___________ | ___________ |
Sturmregelung           | ___________ | ___________ | ___________ |
Ersatzteile Verfügbar   | ___________ | ___________ | ___________ |
Erfahrungsberichte pos. | ___________ | ___________ | ___________ |

BEWERTUNG (1-5 Punkte):
Ertrag pro Euro          | ___/5       | ___/5       | ___/5       |
Geräusch-Komfort         | ___/5       | ___/5       | ___/5       |
Zuverlässigkeit (Ruf)    | ___/5       | ___/5       | ___/5       |
Eignung für mein Revier  | ___/5       | ___/5       | ___/5       |
Service/Ersatzteile      | ___/5       | ___/5       | ___/5       |
─────────────────────────────────────────────────────────────────────
SUMME                    | ___/25      | ___/25      | ___/25      |

Meine Wahl: ___________________
Begründung: ___________________
```

---

## Ende der Wissensdatei 22.06 — Windgeneratoren

> **Gesamtumfang:** ~3.800 Zeilen
> **Confidence-Quellen:** Herstellerdatenblätter, IEC 61400-2, GL Renewable Certification, Pantaenius Schadensstatistik, OCC Crew Reports, Praxisberichte Blauwassersegler
> **Nächste Aktualisierung fällig:** 2026-11-05
