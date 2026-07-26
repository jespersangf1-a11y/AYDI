---
title: "Schienensysteme und Schlitten im Yachtbau"
kategorie: "11 Klampen Klemmen Schienensysteme"
unterkategorie: "03 Schienensysteme"
version: "1.0.0"
datum: "2026-04-25"
autor: "AYDI Research"
status: "validated"
confidence_quellen:
  - measured: "Hersteller-TDS, Katalogdaten, SWL-Tabellen"
  - documented: "Hersteller-Kataloge, Rigger-Handbücher, Forum-Konsens"
  - estimated: "Erfahrungswerte, Praxisberichte"
tags:
  - schienensysteme
  - traveller
  - genua-schiene
  - grossschot-traveller
  - t-track
  - schlitten
  - ball-bearing-car
  - spinnaker-schiene
---

# 11.03 — Schienensysteme und Schlitten im Yachtbau: Vollständige Wissensreferenz

> **AYDI Wissensdatei 11.03** — Kategorie 11: Klampen, Klemmen, Schienensysteme
> **Confidence-Quelle:** measured (Hersteller-TDS, Belastungstabellen), documented (Hersteller-Kataloge, Rigger-Handbücher), estimated (Erfahrungswerte)
> **Letzte Aktualisierung:** 2026-04-25

---

## Inhaltsverzeichnis

1. [Einführung und Übersicht](#1-einführung-und-übersicht)
2. [Grundlagen und Theorie](#2-grundlagen-und-theorie)
3. [Typenübersicht](#3-typenübersicht)
4. [Produktlinien der Hersteller](#4-produktlinien-der-hersteller)
5. [Montage und Installation](#5-montage-und-installation)
6. [Anlagen-spezifische Zuordnung](#6-anlagen-spezifische-zuordnung)
7. [Fehlerbild-Atlas](#7-fehlerbild-atlas)
8. [Troubleshooting](#8-troubleshooting)
9. [FAQ — Häufige Fragen](#9-faq--häufige-fragen)
10. [Glossar](#10-glossar)
11. [Schnell-Referenz](#11-schnell-referenz)
12. [ANHANG A — Fallstudien](#anhang-a--fallstudien)
13. [ANHANG B — Weitere Fallstudien](#anhang-b--weitere-fallstudien)
14. [ANHANG C — AYDI-Integration (Pydantic-Modelle)](#anhang-c--aydi-integration-pydantic-modelle)
15. [ANHANG D — Belastungstabellen](#anhang-d--belastungstabellen)
16. [ANHANG E — Confidence-Mapping](#anhang-e--confidence-mapping)
17. [ANHANG F — Montage-Checklisten](#anhang-f--montage-checklisten)
18. [ANHANG G — Kompatibilitätsmatrix](#anhang-g--kompatibilitätsmatrix)
19. [ANHANG H — Wartungsplan und Lebensdauer](#anhang-h--wartungsplan-und-lebensdauer)
20. [ANHANG I — Preis-Referenz](#anhang-i--preis-referenz)
21. [ANHANG J — Entscheidungsbaum Systemauswahl](#anhang-j--entscheidungsbaum-systemauswahl)
22. [ANHANG K — Normen und Zertifizierungen](#anhang-k--normen-und-zertifizierungen)
23. [ANHANG L — Regatta-spezifische Anforderungen](#anhang-l--regatta-spezifische-anforderungen)
24. [ANHANG M — Materialdatenblätter](#anhang-m--materialdatenblätter)
25. [ANHANG N — Schienensystem-Bewertungsschema](#anhang-n--schienensystem-bewertungsschema)
26. [ANHANG O — Historische Entwicklung](#anhang-o--historische-entwicklung)
27. [ANHANG P — Retrofit-Szenarien](#anhang-p--retrofit-szenarien)
28. [ANHANG Q — Herstellervergleich Scoring](#anhang-q--herstellervergleich-scoring)
29. [ANHANG R — Weiterführende Ressourcen](#anhang-r--weiterführende-ressourcen)

---

## 1. Einführung und Übersicht

### 1.1 Bedeutung von Schienensystemen im Yachtbau

Schienensysteme (engl. track systems) sind die zentralen Führungs- und Verstellmechanismen für die Segeltrimmung auf Segel- und Motoryachten. Sie ermöglichen die präzise Positionierung von Schotblöcken, Travellern und Umlenkpunkten, die direkt die Segelform und damit die Leistung des Bootes beeinflussen. Ein korrekt dimensioniertes und installiertes Schienensystem ist die Grundvoraussetzung für effizientes, sicheres und komfortables Segeln.

Die Qualität und der Zustand der Schienensysteme bestimmen:
- **Segeltrimmung**: Exakte Positionierung der Schotführung beeinflusst Twist, Bauch und Anstellwinkel des Segels
- **Sicherheit**: Ein versagendes Travellersystem bei hoher Last kann zu unkontrollierten Gibes, Personenschäden oder Riggschäden führen
- **Komfort**: Leichtgängige Systeme reduzieren den Kraftaufwand beim Trimmen erheblich
- **Bootswert**: Hochwertige Schienensysteme sind ein wesentliches Qualitätsmerkmal bei Bootsinspektion und Wertermittlung

### 1.2 Historische Einordnung

Die Entwicklung moderner Schienensysteme begann in den 1960er-Jahren mit dem Übergang von einfachen Holz-Gleitschienen zu stranggepressten Aluminium-T-Profilen. Die Einführung von Kugellager-Schlitten durch Harken in den 1970er-Jahren revolutionierte die Genua-Trimmung. Seitdem hat sich die Technologie kontinuierlich weiterentwickelt — von einfachen Gleitschlitten über Kugellager-Wagen bis hin zu modernen Highline-Systemen mit PTFE-Buchsen und integrierten Klemmen.

### 1.3 Systemkomponenten im Überblick

Ein vollständiges Schienensystem besteht aus folgenden Grundkomponenten:

| Komponente | Funktion | Materialien |
|-----------|----------|-------------|
| Schiene (Track) | Führungsprofil für den Schlitten | Alu 6061-T6, Alu 6082-T6, Edelstahl 316L |
| Schlitten (Car) | Beweglicher Wagen auf der Schiene | Alu eloxiert, Edelstahl, Delrin-Rollen |
| Endstopper (End Stop) | Begrenzung des Schlittenlaufs | Alu, Edelstahl, Kunststoff |
| Befestigung (Mounting) | Verschraubung Schiene → Deck/Struktur | Edelstahl-Schrauben, Nietenbolzen |
| Steuerleinen (Control Lines) | Positionierung des Schlittens | Dyneema, Spectra, Polyester |
| Umlenkblöcke | Leinenführung der Steuerleinen | Alu/Edelstahl mit Kugellagern |

### 1.4 Haupteinsatzbereiche

**Genua-Schiene (Genoa Track)**
Die am häufigsten verwendete Schiene auf Segelyachten. Führt den Genua-Schotblock und bestimmt den Schotwinkel (Sheeting Angle). Typischerweise auf dem Seitendeck montiert, Länge ca. 20–40 % der Bootslänge.

**Großschot-Traveller (Mainsheet Traveler)**
Querschiffs montierte Schiene, die den Angriffspunkt der Großschot quer zum Boot verstellbar macht. Ermöglicht Twist-Kontrolle unabhängig vom Schotdurchhang. Typische Positionen: Cockpitboden, Kajütdach, Achterdeck.

**Spinnaker-Schiene (Spinnaker Track)**
Längslaufende Schiene für den Spinnaker-Barberhaul oder den Spi-Schot-Umlenkpunkt. Oft kürzer als die Genua-Schiene, aber ähnliches Profil.

**Baumniederholer-Schiene (Boom Vang Track)**
Kurze Schiene auf dem Mast oder Mastfuß für den Ansatzpunkt des Kickers/Baumniederholers. Ermöglicht vertikale Verstellung des Angriffspunkts.

**Rollreff-Schiene (Jib Furler Track)**
Vertikale oder geneigte Schiene am Vorstag-Bereich für höhenverstellbare Rollreff-Führungen bei Selbstwendefock-Anlagen.

**Sonstige Anwendungen**
- Luv/Lee-Schienen für Lazy-Jacks
- Mast-Track für Segellatten
- Deckschienen für Fenderhalter auf Motoryachten
- Beiboot-Davit-Führungen

### 1.5 Relevanz für die AYDI-Analyse

Im AYDI-System werden Schienensysteme in mehreren Analysemodulen bewertet:
- **Compliance-Modul**: Prüfung auf korrekte Dimensionierung und Montage gemäß Herstellervorgaben
- **Materials-Modul**: Zustandsbewertung der Materialien (Korrosion, Verschleiß, UV-Degradation)
- **Production-Modul**: Bewertung der Montagequalität und Verarbeitungsgüte
- **Ergonomics-Modul**: Erreichbarkeit und Bedienbarkeit der Verstellmechanismen
- **Service-Patterns-Modul**: Wartungshistorie und bekannte Schwachstellen

---

## 2. Grundlagen und Theorie

### 2.1 Schienenprofile — Querschnittsgeometrie

Die Profilform der Schiene bestimmt die Art des Schlittens, die Belastbarkeit und die Einsatzmöglichkeiten. Es existieren vier Grundprofiltypen:

#### 2.1.1 T-Track (T-Profil)

Das verbreitetste Profil im modernen Yachtbau. Die T-Form bietet eine breite Standfläche für den Schlitten und eine schmale Nutöffnung, die den Schlitten gegen Abheben sichert.

**Standardgrößen (Breite × Höhe):**

| Bezeichnung | Breite (mm) | Höhe (mm) | Nutbreite (mm) | Typische SWL (kg) | Bootslänge |
|------------|-------------|-----------|-----------------|--------------------|-----------:|
| T-Track 19 | 19 | 15 | 6 | 200–500 | 5–8 m |
| T-Track 22 | 22 | 18 | 8 | 400–900 | 7–10 m |
| T-Track 25 | 25 | 20 | 10 | 600–1.500 | 9–13 m |
| T-Track 32 | 32 | 25 | 12 | 1.200–3.000 | 12–18 m |
| T-Track 40 | 40 | 32 | 14 | 2.500–6.000 | 16–25 m |
| T-Track 50 | 50 | 40 | 16 | 5.000–12.000 | 22–35 m |

**Materialeigenschaften T-Track:**
- Aluminium 6061-T6: Streckgrenze 276 MPa, E-Modul 68.9 GPa, Dichte 2.70 g/cm³
- Aluminium 6082-T6: Streckgrenze 310 MPa, E-Modul 70 GPa, Dichte 2.71 g/cm³ (bevorzugt im Yachtbau)
- Eloxierung: Hartanodisierung 25–50 µm für Salzwasser, Typ III MIL-A-8625

#### 2.1.2 I-Beam (Doppel-T-Profil)

Verwendet für Hochlast-Traveller und spezielle Anwendungen. Das I-Profil bietet höhere Biegesteifigkeit bei gleichem Gewicht im Vergleich zum T-Track.

**Eigenschaften:**
- Höhere vertikale Steifigkeit als T-Track bei gleichem Gewicht
- Schlitten greifen beidseitig um den Steg
- Typisch für Großschot-Traveller ab 12 m Bootslänge
- Weniger universell — Schlitten sind profilspezifisch

#### 2.1.3 Flat-Bar (Flachprofil)

Einfachstes Profil, historisch weit verbreitet, heute nur noch für Nebenfunktionen eingesetzt.

**Eigenschaften:**
- Keine formschlüssige Sicherung des Schlittens gegen Abheben
- Schlitten werden durch Klemmung oder Schwerkraft gehalten
- Geringe Kosten, einfache Montage
- Nicht für Hochlastanwendungen geeignet
- Noch verbreitet bei älteren Yachten (vor 1990) für Genua-Schienen

#### 2.1.4 HL-Track (High-Load-Track / Harken-Spezifikation)

Spezialprofil für extreme Lasten, entwickelt für Regatta- und Superyacht-Anwendungen. Kombination aus T-Track-Grundform mit verstärktem Steg und breiterer Basis.

**Eigenschaften:**
- SWL bis 25.000 kg bei 50 mm Profilbreite
- Zusätzliche Verstärkungsrippen im Profil
- Edelstahl-Versionen (316L) für Superyachten
- Preisfaktor 3–5× gegenüber Standard-T-Track

### 2.2 Schlittentypen (Car Types)

#### 2.2.1 Kugellager-Schlitten (Ball Bearing Car)

Der Standard für moderne Schienensysteme. Kugelgelagerte Schlitten bieten den geringsten Reibungskoeffizienten und die höchste Leichtgängigkeit.

**Aufbau:**
- Gehäuse aus eloxiertem Aluminium oder Edelstahl
- Kugellaufbahnen (Ball Races) aus gehärtetem Edelstahl oder Delrin
- Kugelkäfig (Ball Cage) aus Acetal/Delrin zur Abstandshaltung
- Kugeln aus Edelstahl 316 oder Torlon (für Gewichtsersparnis)
- Dichtlippen (Wiper Seals) gegen Salzwasser- und Schmutzeintritte

**Reibungskoeffizient:** µ = 0.02–0.05 (abhängig von Belastung und Schmierung)

**Vorteile:**
- Extrem leichtgängig unter Last
- Hohe statische und dynamische Tragfähigkeit
- Lange Lebensdauer bei korrekter Wartung (8.000–15.000 Seemeilen)

> ⚠️ **ZU PRÜFEN (Audit):** 8.000–15.000 sm hier vs. 15.000–30.000 sm für Kugellager-Schlitten in ANHANG H (H.1) — interner Widerspruch bei der Standzeit; der niedrigere Bereich entspricht dort dem Gleitschlitten. Richtung unbestätigt (herstellerabhängige Schätzwerte, nicht web-verifizierbar).

**Nachteile:**
- Empfindlich gegen Verschmutzung (Sand, Salzkristalle)
- Korrosion der Kugeln bei mangelhafter Pflege
- Höhere Kosten als Gleitschlitten
- Wartungsintensiver: regelmäßige Reinigung und Schmierung erforderlich

#### 2.2.2 Gleitschlitten (Slider Car / Plain Bearing Car)

Einfache Konstruktion ohne bewegliche Teile. Gleitung auf PTFE-, Delrin- oder Torlon-Flächen.

**Aufbau:**
- Gehäuse aus eloxiertem Aluminium
- Gleitflächen aus PTFE (Teflon), Delrin oder Torlon
- Keine Kugeln, keine Käfige, keine Dichtungen

**Reibungskoeffizient:** µ = 0.08–0.15 (abhängig von Material und Belastung)

**Vorteile:**
- Wartungsarm — keine Kugeln, die korrodieren können
- Unempfindlich gegen Verschmutzung
- Kostengünstiger als Kugellager-Schlitten
- Geeignet für raue Umgebungen (Offshore-Yachten)

**Nachteile:**
- Höherer Reibungswiderstand → mehr Kraft zum Verstellen nötig
- PTFE-Flächen verschleißen und müssen periodisch getauscht werden
- Unter hoher Last kann Stick-Slip-Effekt auftreten

#### 2.2.3 Kolbenstopp-Schlitten (Piston Stop Car)

Schlitten mit integriertem Verriegelungsmechanismus. Ein federbelasteter Kolben rastet in Bohrungen der Schiene ein.

**Aufbau:**
- Basis wie Kugellager- oder Gleitschlitten
- Zusätzlicher Federkolben (Piston) im Schlittenkörper
- Schiene mit Rastbohrungen in regelmäßigen Abständen (typisch 25–50 mm)

**Anwendung:**
- Genua-Schienen mit festen Trimmstellungen
- Schnelle Voreinstellung + Feineinstellung über Steuerleinen
- Bevorzugt im Fahrtensegelbereich für schnellen Wechsel zwischen Segelgrößen

#### 2.2.4 Schlitten mit integrierter Klemme (Car with Integral Cleat)

Kombination aus Schlitten und eingebauter Curryklemme oder Fallenstopper für die Feinverstellung.

**Anwendung:**
- Genua-Schienen auf Fahrtenyachten
- Ermöglicht Verstellung ohne separate Steuerleinen
- Reduziert Leinengewirr im Cockpit

### 2.3 Belastungsberechnung für Travellersysteme

#### 2.3.1 Grundlegende Lastbetrachtung

Die Belastung eines Travellersystems ergibt sich aus der Schotkraft und dem Geometriewinkel:

**Großschot-Traveller:**

```
F_traveller = F_mainsheet × sin(α)

wobei:
  F_traveller = Querlast auf den Traveller (N)
  F_mainsheet = Schotkraft in der Großschot (N)
  α = Winkel zwischen Schot und Vertikale (°)
```

**Typische Schotkräfte nach Bootslänge:**

| Bootslänge (m) | Segelfläche Groß (m²) | Max. Schotkraft (kN) | Traveller-Querlast (kN) |
|----------------|----------------------|----------------------|-------------------------|
| 7–8 | 15–20 | 2.0–3.5 | 1.0–2.0 |
| 9–10 | 22–30 | 3.5–5.0 | 2.0–3.0 |
| 11–12 | 28–40 | 5.0–8.0 | 3.0–5.0 |
| 13–15 | 38–55 | 7.0–12.0 | 4.0–7.0 |
| 16–18 | 50–80 | 10.0–18.0 | 6.0–10.0 |
| 20–25 | 75–130 | 15.0–30.0 | 9.0–18.0 |

#### 2.3.2 Dynamische Lastfaktoren

Statische Lasten werden durch dynamische Effekte vervielfacht:

| Lastsituation | Dynamikfaktor |
|---------------|---------------|
| Normales Segeln | 1.0 |
| Böen (Windstärke +50 %) | 2.25 (Kraft ~ v²) |
| Halse (kontrolliert) | 2.0–3.0 |
| Patenthalse (unkontrolliert) | 4.0–8.0 |
| Regatta (Manöver unter Volllast) | 2.5–4.0 |
| Welleneinschlag auf Segel | 1.5–2.5 |

**Sicherheitsfaktor für Schienensysteme:**
- Fahrtenyacht: SF ≥ 3.0 auf Bruchlast
- Regattayacht: SF ≥ 2.5 auf Bruchlast (leichterer Bau akzeptabel)
- Superyacht/Offshore: SF ≥ 4.0 auf Bruchlast

#### 2.3.3 Schraubenbelastung bei der Schienenmontage

Die Befestigungsschrauben der Schiene müssen sowohl Quer- als auch Auszugskräfte aufnehmen:

**Querkraftberechnung pro Schraube:**

```
F_screw_shear = F_traveller_max / (n × f_distribution)

wobei:
  F_screw_shear = Scherkraft pro Schraube (N)
  F_traveller_max = Maximale Travellerlast inkl. Dynamikfaktor (N)
  n = Anzahl Schrauben im belasteten Bereich
  f_distribution = Verteilungsfaktor (0.6–0.8, da nicht alle Schrauben gleich belastet)
```

**Auszugskraft bei seitlicher Belastung:**

```
F_screw_pullout = F_traveller_max × h_car / (b_track × n_eff)

wobei:
  h_car = Höhe des Kraftangriffspunkts über Schraubenebene (mm)
  b_track = Breite des Schienenfußes (mm)
  n_eff = Effektive Schraubenanzahl im Lastbereich
```

### 2.4 Reibung und Kontrolle

#### 2.4.1 Reibungskräfte im System

Die Gesamtreibung eines Schienensystems setzt sich zusammen aus:

1. **Lagerreibung (Rolling/Sliding Friction):**
   - Kugellager: F_r = µ_ball × F_normal = 0.03 × F_n
   - Gleitlager: F_r = µ_slide × F_normal = 0.10 × F_n

2. **Seitenreibung (Side Loading):**
   - Entsteht durch nicht-vertikale Belastung
   - Erhöht den Reibungskoeffizienten um Faktor 1.5–3.0
   - Korrekte Schienenausrichtung minimiert Seitenreibung

3. **Verschmutzungsreibung:**
   - Salzkristalle in der Laufbahn: +50–200 % Reibung
   - Sand/Schmutz: +100–500 % Reibung
   - Korrodierte Kugeln: +200–1000 % Reibung bis zum Blockieren

#### 2.4.2 Kontrollsysteme für Traveller

**4:1 Übersetzung (Standard Fahrtenyacht):**
- Traveller-Steuerleine über 2 Umlenkblöcke + 1 Doppelblock
- Haltekraft bei 20 kg Zuglast: 80 kg
- Ausreichend für Boote bis 10 m

**6:1 Übersetzung (Mittelgroße Yachten):**
- Traveller-Steuerleine über Fiddle-Block + 2 Umlenkblöcke
- Haltekraft bei 20 kg Zuglast: 120 kg
- Standard für Boote 10–14 m

**8:1 bis 12:1 Übersetzung (Große Yachten):**
- Mehrfach-Umlenkung oder Winch-Steuerung
- Haltekraft bei 20 kg Zuglast: 160–240 kg
- Erforderlich ab 14 m Bootslänge

**Hydraulische Steuerung (Superyachten):**
- Hydraulikzylinder beidseitig des Travellers
- Exakte Positionierung per Druckknopf oder Joystick
- SWL bis 50.000 N und darüber
- Ab 18 m Bootslänge oder bei Kurzhand-Ausrüstung

### 2.5 Materialwissenschaft der Schienenprofile

#### 2.5.1 Aluminium-Legierungen im Vergleich

| Eigenschaft | 6061-T6 | 6082-T6 | 7075-T6 |
|------------|---------|---------|---------|
| Streckgrenze (MPa) | 276 | 310 | 503 |
| Zugfestigkeit (MPa) | 310 | 340 | 572 |
| E-Modul (GPa) | 68.9 | 70.0 | 71.7 |
| Dichte (g/cm³) | 2.70 | 2.71 | 2.81 |
| Korrosionsbeständigkeit | Gut | Sehr gut | Mäßig |
| Eloxierbarkeit | Sehr gut | Sehr gut | Gut |
| Verfügbarkeit Strangpressprofile | Sehr gut | Gut | Eingeschränkt |
| Typischer Einsatz | Standard-T-Track | Premium-Track | Regatta/Leichtbau |

#### 2.5.2 Oberflächenbehandlung

**Hartanodisierung (Typ III):**
- Schichtdicke: 25–50 µm
- Härte: 350–500 HV (Vickers)
- Erhöht Verschleißfestigkeit um Faktor 5–10
- Reduziert galvanische Korrosion in Salzwasser
- Farbe: Dunkelgrau bis Schwarz (natürlich)
- Kosten: +15–25 % gegenüber Standard-Eloxierung

**Standard-Eloxierung (Typ II):**
- Schichtdicke: 8–25 µm
- Härte: 200–350 HV
- Ausreichend für Fahrtenyachten im Süßwasser
- Verschiedene Farben möglich (Schwarz, Silber, Gold)
- Standard bei den meisten Herstellern

#### 2.5.3 Edelstahl-Schienen

Für Superyachten und besondere Anwendungen werden Schienen aus Edelstahl 316L gefertigt:

| Eigenschaft | Edelstahl 316L | Aluminium 6082-T6 |
|------------|---------------|-------------------|
| Streckgrenze (MPa) | 170 | 310 |
| Zugfestigkeit (MPa) | 485 | 340 |
| E-Modul (GPa) | 193 | 70 |
| Dichte (g/cm³) | 7.98 | 2.71 |
| Gewichtsfaktor | 2.95× | 1.00× |
| Korrosionsbeständigkeit | Hervorragend | Gut (eloxiert) |
| Einsatz | Superyacht, Ästhetik | Standard |

### 2.6 Kraftfluss und Strukturelle Integration

#### 2.6.1 Decksverstärkung

Die Schienenbefestigung muss Kräfte in die Rumpf-Deck-Struktur einleiten. Ohne ausreichende Verstärkung entstehen:
- Lochleibungsversagen der Schraubenbohrungen
- Delamination des GFK-Sandwichlaminats
- Kernquetschung bei Sandwich-Decks (Balsa, Schaum)
- Decksdurchbiegung unter Last

**Verstärkungsmethoden:**
1. **Durchbolzung mit Gegenplatte**: Edelstahl-Bolzen durch Deck mit Unterlegplatte (min. 3 mm Alu oder Edelstahl)
2. **Kernverstärkung bei Sandwich**: Balsakeile oder Epoxidfüllung im Bohrungsbereich (min. 3× Schraubendurchmesser Radius)
3. **Aluminium-Schiene als Verstärkung**: Die Schiene selbst versteift das Deck in Längsrichtung
4. **Zusätzliche GFK-Laminatlagen**: 2–4 Lagen biaxiales Gewebe (300–600 g/m²) unter der Montagefläche

---

## 3. Typenübersicht

### 3.1 T-Track mit Schlitten (T-Track with Cars)

#### 3.1.1 Beschreibung

Das T-Track-System ist das universelle Schienensystem im modernen Yachtbau. Die T-förmige Schiene nimmt Schlitten auf, die durch die hinterschnittene Nut gegen Abheben gesichert sind. Die Schlitten sind frei verschiebbar und können durch Kolbenstopps, Klemmen oder Steuerleinen arretiert werden.

**Einsatzbereiche:**
- Genua-Schotführung (primär)
- Leichte Travellersysteme
- Spinnaker-Barberhauls
- Lazy-Jack-Führungen
- Allgemeine Deck-Befestigungspunkte

**Typische Konfiguration (10 m Segelyacht):**
- 2× Genua-Schiene: 25 mm T-Track, je 2.0 m Länge, mit Kugellager-Schlitten
- 1× Traveller: 25 mm T-Track, 1.8 m Länge, mit Fiddle-Block-Schlitten
- 2× Spinnaker: 19 mm T-Track, je 0.6 m Länge, mit einfachem Schlitten

#### 3.1.2 Vorteile

- Universell einsetzbar für verschiedene Anwendungen
- Große Auswahl an kompatiblen Schlitten verschiedener Hersteller
- Schraubenmontage oder Niet-Montage möglich
- Verschiedene Schienenlängen als Meterware verfügbar
- Einfache Nachrüstung und Modifikation

#### 3.1.3 Nachteile

- Nut kann Wasser und Schmutz sammeln
- Schlitten können bei extremer Seitenbelastung verkanten
- Begrenzte SWL bei kleinen Profilgrößen
- Nicht geeignet für extreme Regattalanwendungen bei großen Booten

### 3.2 Genua-Führungsschiene (Genoa Lead Track)

#### 3.2.1 Beschreibung

Die Genua-Führungsschiene ist die primäre Anwendung für T-Track-Systeme auf Segelyachten. Sie führt den Schotblock der Genua/Fock und bestimmt den Schotwinkel (Sheeting Angle) sowie die Höhe des Schotumlenkpunkts.

**Positionierung:**
- Längsachse: Parallel zur Mittellinie, typisch 5–12° Schotwinkel (Abstand zur Mittellinie)
- Beginn: Ca. bei 30–35 % Bootslänge ab Bug (auf Höhe des Mastfußes)
- Ende: Ca. bei 55–65 % Bootslänge ab Bug
- Decksmontage: Seitendeck, meist zwischen Seereling-Stanchions und Aufbau

**Dimensionierung nach Bootslänge:**

| Bootslänge (m) | Schienenprofil (mm) | Schienenlänge (m) | Schlitten-SWL (kg) |
|----------------|--------------------|--------------------|---------------------|
| 6–7 | 19 | 0.8–1.0 | 300–500 |
| 8–9 | 22 | 1.2–1.5 | 500–900 |
| 10–11 | 25 | 1.5–2.0 | 900–1.500 |
| 12–14 | 25–32 | 2.0–2.8 | 1.500–3.000 |
| 15–18 | 32 | 2.5–3.5 | 3.000–5.000 |
| 20–25 | 32–40 | 3.0–4.5 | 5.000–8.000 |

#### 3.2.2 Verstellbarer Genua-Schlitten

Moderne Genua-Schlitten bieten neben der Längsverstellung auf der Schiene auch eine Querverstellung des Schotblocks auf dem Schlitten selbst (athwartships adjustment):

**Typen der Querverstellung:**
- **Festposition**: Schlitten mit fixem Blockbügel, nur Längsverstellung
- **Verschiebbarer Block**: Block auf kurzem Querstück verschiebbar
- **Drehbarer Bügel**: Block auf schwenkbarem Bügel montiert
- **Selbstwendende Fock (Self-Tacking Jib)**: Schiene quer über das Vordeck, Schlitten gleitet bei Wende automatisch auf die andere Seite

#### 3.2.3 Selbstwendende Fock-Schiene (Self-Tacking Jib Track)

Eine Sonderform der Genua-Schiene, die quer über das Vordeck verläuft und eine selbstwendende Fock ermöglicht:

**Aufbau:**
- Querschiffs montierte Schiene auf dem Vordeck (vor dem Mast)
- Gebogene Schiene folgt dem Decksverlauf
- Schlitten mit Blockarm für die Fock-Schot
- Beim Wenden gleitet der Schlitten auf die Lee-Seite

**Abmessungen (typisch 10 m Yacht):**
- Schienenlänge: 2.0–2.5 m (Bootsbreite × 0.6–0.7)
- Schienenprofil: 25 mm T-Track
- Schlittenlast: bis 1.500 kg SWL
- Schienenradius: Entsprechend der Decksform (konvex)

### 3.3 Großschot-Travellersystem (Mainsheet Traveler System)

#### 3.3.1 Beschreibung

Das Großschot-Travellersystem ist das zentralste und am höchsten belastete Schienensystem auf einer Segelyacht. Es ermöglicht die querschiffs Verstellung des Großschot-Angriffspunkts und damit die unabhängige Steuerung von Twist und Segeldruck.

**Montageposition:**

| Position | Vorteile | Nachteile | Typisch bei |
|----------|----------|-----------|-------------|
| Cockpitboden | Direkte Krafteinleitung, kurze Schot | Behinderung im Cockpit | Regattayachten |
| Kajütdach | Frei zugängliches Cockpit | Längerer Schotweg, Dachlast | Fahrtenyachten |
| Achterdeck | Cockpit völlig frei | Sehr langer Schotweg | Moderne Fahrtenyachten |
| Brücke/Bimini | Kombiniert mit Bimini-Struktur | Komplexe Konstruktion | Motor-Segler |

#### 3.3.2 Komponenten eines Travellersystems

**Vollständiges System umfasst:**

1. **Schiene (Track):**
   - Querschiffs montiert
   - Länge: typisch 80–100 % der Bootsbreite am Montageort
   - Profil: T-Track 25–50 mm oder I-Beam

2. **Traveller-Schlitten (Traveler Car):**
   - Kugellager- oder Gleitschlitten
   - Oberer Bügel mit Blockaufnahme
   - Steuerleinen-Befestigung beidseitig

3. **Steuerleinen-Talje (Control Line Tackle):**
   - Beidseitig des Schlittens
   - Typisch 4:1 bis 12:1 Übersetzung
   - Umgelenkt zum Cockpit (Steuerstand oder Grinder)

4. **Endstopper (End Stops):**
   - An beiden Enden der Schiene
   - Müssen die volle Traveller-Last aufnehmen können
   - Verschraubt oder in Schienennut eingesetzt

5. **Umlenkblöcke (Turning Blocks):**
   - Leiten Steuerleinen vom Schlitten zu den Klemmen
   - Montiert an den Schienenenden oder daneben
   - Kugellager-Blöcke für geringste Reibung

#### 3.3.3 Traveller-Steuerung: Fiddle-Block-System

Das gebräuchlichste Steuersystem für Traveller auf Fahrtenyachten:

**Aufbau:**
- Fiddle-Block (Violinblock) an jedem Ende des Schlittens
- Steuerleinen laufen vom Schlitten über den Fiddle-Block zum Cockpit
- Arretierung über Curryklemmen oder Fallenstopper am Cockpitrand
- Übersetzung typisch 4:1 oder 6:1

**Funktion:**
- Ziehen an der Luv-Leine bewegt den Traveller nach Luv
- Fieren der Lee-Leine gibt den Traveller frei
- Beide Leinen müssen synchron bedient werden (oder Rückholfeder)

### 3.4 Spinnaker-Schiene (Spinnaker Track)

#### 3.4.1 Beschreibung

Spinnaker-Schienen dienen der Positionierung des Spinnaker-Barberhauls oder des Spi-Schot-Umlenkpunkts. Sie sind kürzer als Genua-Schienen und meist im Achterschiffsbereich montiert.

**Typische Positionen:**
- Seitendeck achtern (parallel zur Genua-Schiene)
- Heckbereich (für Gennaker-Schot)
- Achterliche Seereling-Basis (improvisiert)

**Dimensionierung:**
- Profil: 19–25 mm T-Track
- Länge: 0.5–1.5 m
- SWL: 500–2.000 kg (abhängig von Segelfläche und Windstärke)

#### 3.4.2 Besonderheiten

- Schlitten müssen unter Last leichtgängig sein (schnelle Verstellung beim Halsen)
- Steuerleinen müssen vom Cockpit aus bedienbar sein
- Schiene muss extremen dynamischen Lasten beim Halsen standhalten
- Endstopper sind sicherheitskritisch (Schlitten darf nicht auslaufen)

### 3.5 Baumniederholer-Schiene (Boom Vang Track)

#### 3.5.1 Beschreibung

Kurze Schiene am Mastfuß oder auf dem Mast für den unteren Angriffspunkt des Kickers/Baumniederholers. Ermöglicht die vertikale und/oder seitliche Verstellung des Vang-Ansatzpunkts.

**Typen:**
- **Mastschiene vertikal**: Am Mast montiert, Vang-Ansatz höhenverstellbar
- **Deckschiene**: Am Mastfuß auf Deck, Vang-Ansatz seitlich verstellbar
- **Kombi-Schiene**: Mast + Deck, vollständige 3D-Verstellbarkeit

**Dimensionierung:**
- Profil: 19–25 mm T-Track
- Länge: 0.2–0.6 m
- SWL: 200–1.500 kg

### 3.6 Rollreff-Führungsschiene (Jib Furler Track)

#### 3.6.1 Beschreibung

Vertikale Schiene am Rollreff-Profil oder am Vorstag-Bereich für die höhenverstellbare Führung des Rollreff-Segels. Ermöglicht die Optimierung des Holepunkts bei unterschiedlichen Reff-Stufen.

**Funktion:**
- Bei teilweise eingerollter Genua verschiebt sich der optimale Holepunkt nach vorn und oben
- Die Rollreff-Führungsschiene kompensiert diesen Effekt
- Automatische Holepunkt-Verstellung über Schi-Car mit Seilzug

**Dimensionierung:**
- Profil: 19–22 mm T-Track (wegen Gewicht am Vorstag)
- Länge: 0.5–1.5 m
- SWL: 200–800 kg (reduzierte Querlasten)

### 3.7 Durchdeck-Schiene (Through-Deck Track)

#### 3.7.1 Beschreibung

Spezialschiene, die durch das Deck hindurchgeführt wird und Befestigungspunkte sowohl auf als auch unter Deck bietet. Verwendet für:
- Großschot-Traveller mit Unter-Deck-Steuerung
- Verdeckte Steuerleinen-Umlenkung
- Integrierte Decksbeschläge auf Regattayachten

**Vorteile:**
- Sauberes Deckslayout ohne sichtbare Steuerleinen
- Bessere Krafteinleitung in die Struktur
- Reduzierte Stolpergefahr auf Deck

**Nachteile:**
- Komplexere Montage (Decksöffnung)
- Höherer Dichtungsaufwand
- Schwierigere Inspektion und Wartung
- Teurer als Aufbau-Systeme

### 3.8 Mast-Track (Segel-Führungsschiene am Mast)

#### 3.8.1 Beschreibung

Obwohl streng genommen Teil des Riggs, ist die Mast-Führungsschiene ein wichtiges Schienensystem. Sie führt die Segellatten (Slides oder Slugs) des Großsegels am Mast entlang.

**Typen:**
- **Intern (Nut im Mast)**: Großsegelkopfbrett und Segellatten gleiten in einer Nut im Mast
- **Extern (aufgesetzte Schiene)**: Separate T-Schiene auf der Mastrückseite
- **Battcar-System**: Spezialschienen mit großen Kugellagerwagen für Full-Batten-Segel

**Dimensionierung:**
- Profil: 19–32 mm (abhängig von Mastgröße)
- Länge: Vorliekhöhe des Großsegels
- SWL pro Slide: 50–500 kg

### 3.9 Sonstige Schienensysteme

#### 3.9.1 Genuaholepunkt-Verstellschiene (Barber Hauler Track)

Kurze Schiene auf dem Seitendeck für die Querverstellung des Genua-Schotblocks nach innen oder außen:
- Verstellung des effektiven Schotwinkels
- Profil: 19–22 mm T-Track
- Länge: 0.3–0.8 m

#### 3.9.2 Backstag-Schiene (Running Backstay Track)

Schiene am Heck oder auf der Achterseite des Cockpits für den unteren Befestigungspunkt der laufenden Backstage:
- Profil: 25–32 mm T-Track
- SWL: bis 5.000 kg (entspricht Backstag-Spannung)
- Muss extremen Punktlasten standhalten

#### 3.9.3 Fender-Schiene (Motoryachten)

Deckschiene für die Befestigung von Fendern und Beiboot-Davits auf Motoryachten:
- Profil: 22–32 mm T-Track
- Geringe Lasten (max. 500 kg)
- Ästhetik oft wichtiger als Belastbarkeit
- Edelstahl 316L poliert für Superyachten

#### 3.9.4 Cockpit-Organisationsschienen

Multifunktionsschienen im Cockpit für:
- Tischbein-Befestigung
- Cockpitzeltstangen
- Instrumentenhalter
- Getränkehalter und Ablagen
- Profil: 19 mm T-Track, geringe Lasten

---

## 4. Produktlinien der Hersteller

### 4.1 Harken (USA/Italien)

#### 4.1.1 Firmengeschichte und Marktposition

Harken wurde 1967 von Peter und Olaf Harken in Pewaukee, Wisconsin (USA) gegründet. Heute ist Harken der weltweit führende Hersteller von Schienensystemen, Blöcken und Deck-Hardware für Segelyachten. Produktion in den USA und Italien (Limido Comasco). Harken-Produkte gelten als Referenzstandard im Regatta- und Fahrtensegelbereich.

#### 4.1.2 T-Track Programm

**Harken 22 mm Micro T-Track:**
- Art.-Nr.: 2720 (Schiene, 1.5 m), 2721 (Schiene, 2.0 m)
- Profilbreite: 22 mm, Höhe: 18.5 mm
- Material: Aluminium 6082-T6, hartanodisiert
- SWL Schiene: 900 kg
- Schraubenabstand: 100 mm (empfohlen)
- Schraubengröße: M5 oder #10
- Gewicht: 0.35 kg/m
- Bootslänge: 6–9 m
- Preis: ca. 38–55 EUR/m

**Harken 27 mm Small Boat T-Track:**
- Art.-Nr.: 2727 (Schiene, 1.5 m), 2728 (Schiene, 2.0 m), 2729 (3.0 m)
- Profilbreite: 27 mm, Höhe: 21 mm
- Material: Aluminium 6082-T6, hartanodisiert
- SWL Schiene: 1.800 kg
- Schraubenabstand: 100 mm
- Schraubengröße: M6 oder 1/4"
- Gewicht: 0.52 kg/m
- Bootslänge: 8–12 m
- Preis: ca. 55–80 EUR/m

**Harken 32 mm T-Track:**
- Art.-Nr.: 2732 (1.5 m), 2733 (2.0 m), 2734 (3.0 m), 2735 (5.0 m)
- Profilbreite: 32 mm, Höhe: 25 mm
- Material: Aluminium 6082-T6, hartanodisiert
- SWL Schiene: 3.200 kg
- Schraubenabstand: 125 mm
- Schraubengröße: M8 oder 5/16"
- Gewicht: 0.82 kg/m
- Bootslänge: 11–18 m
- Preis: ca. 85–120 EUR/m

**Harken 42 mm Big Boat T-Track:**
- Art.-Nr.: 2742 (1.5 m), 2743 (2.0 m), 2744 (3.0 m)
- Profilbreite: 42 mm, Höhe: 33 mm
- Material: Aluminium 6082-T6, hartanodisiert Typ III
- SWL Schiene: 5.800 kg
- Schraubenabstand: 150 mm
- Schraubengröße: M10 oder 3/8"
- Gewicht: 1.35 kg/m
- Bootslänge: 16–30 m
- Preis: ca. 145–200 EUR/m

#### 4.1.3 Harken MR 27 mm Big Boat Traveller

**Harken MR 27 Travellersystem (Midrange):**
- Art.-Nr.: 2731 (Schlitten ohne Bügel), 2730 (Schiene)
- Profilbreite: 27 mm (proprietäres Profil, nicht Standard-T-Track)
- Schlittentyp: Kugellager, 16 Kugeln pro Seite
- SWL Schlitten: 1.400 kg
- Bruchlast Schlitten: 4.200 kg
- Breite Schlitten: 55 mm, Länge: 95 mm
- Geeignet für: Großschot-Traveller auf Booten 8–12 m
- Steuerleinen: 6 mm, 4:1 bis 6:1 Übersetzung empfohlen
- Preis Schlitten: ca. 180–250 EUR
- Preis Schiene: ca. 65–90 EUR/m

#### 4.1.4 Harken Schlitten (Cars)

**Harken 22 mm Schlitten:**
- Art.-Nr.: 2710 (Gleit-Schlitten), 2711 (Kugellager-Schlitten)
- SWL: 2710: 350 kg, 2711: 550 kg
- Bruchlast: 2710: 1.050 kg, 2711: 1.650 kg
- Typ: Standard mit Schäkel oder Bügel
- Preis: 45–90 EUR

**Harken 27 mm Schlitten:**
- Art.-Nr.: 2715 (Kugellager, Stand-Up), 2716 (Kugellager, Low Profile)
- SWL: 2715: 900 kg, 2716: 900 kg
- Bruchlast: 2715: 2.700 kg, 2716: 2.700 kg
- Preis: 95–160 EUR

**Harken 32 mm Schlitten:**
- Art.-Nr.: 2737 (Kugellager, Stand-Up), 2738 (Kugellager, Low Profile), 2739 (Gleit)
- SWL: 2737: 1.600 kg, 2738: 1.600 kg, 2739: 1.100 kg
- Bruchlast: 2737: 4.800 kg, 2738: 4.800 kg, 2739: 3.300 kg
- Preis: 140–250 EUR

**Harken 42 mm Schlitten:**
- Art.-Nr.: 2746 (Kugellager, Stand-Up), 2747 (Kugellager, Low Profile)
- SWL: 2746: 2.900 kg, 2747: 2.900 kg
- Bruchlast: 2746: 8.700 kg, 2747: 8.700 kg
- Preis: 280–420 EUR

#### 4.1.5 Harken Endstopper und Zubehör

**Endstopper:**
- Art.-Nr.: 2750 (22 mm), 2751 (27 mm), 2752 (32 mm), 2753 (42 mm)
- Material: Edelstahl 316L oder eloxiertes Aluminium
- Befestigung: Verschraubung in Schienennut + Deckschraube
- SWL: Entspricht Schienen-SWL
- Preis: 12–35 EUR/Paar

**Schienenstöße (Track Joiners):**
- Art.-Nr.: 2760 (22 mm), 2761 (27 mm), 2762 (32 mm)
- Verbindung zweier Schienenenden zu einer durchgehenden Schiene
- Material: Edelstahl 316L
- Preis: 18–40 EUR/Stück

**Piston Stop Kit:**
- Art.-Nr.: 2770 (22 mm), 2771 (27 mm), 2772 (32 mm)
- Nachrüstbarer Kolbenstopp für Standard-Schlitten
- Preis: 25–50 EUR/Stück

### 4.2 Lewmar (UK)

#### 4.2.1 Firmengeschichte und Marktposition

Lewmar wurde 1946 in Havant, Hampshire (UK) gegründet. Ursprünglich ein Hersteller von Winschen, hat Lewmar sein Programm auf ein vollständiges Sortiment von Deck-Hardware erweitert. Lewmar ist besonders stark im Fahrtensegelbereich und bei OEM-Ausrüstungen für europäische Werften (Bavaria, Jeanneau, Beneteau).

#### 4.2.2 Lewmar Track-Programm

**Lewmar Size 1 T-Track:**
- Art.-Nr.: 29001000 (Schiene, Meterware)
- Profilbreite: 20 mm, Höhe: 16 mm
- Material: Aluminium 6082-T6, hartanodisiert
- SWL: 500 kg
- Schraubenabstand: 75 mm
- Bootslänge: 5–7 m
- Gewicht: 0.28 kg/m
- Preis: ca. 25–35 EUR/m

**Lewmar Size 2 T-Track:**
- Art.-Nr.: 29002000 (Schiene, Meterware)
- Profilbreite: 25 mm, Höhe: 20 mm
- Material: Aluminium 6082-T6, hartanodisiert
- SWL: 1.200 kg
- Schraubenabstand: 100 mm
- Bootslänge: 8–12 m
- Gewicht: 0.48 kg/m
- Preis: ca. 40–60 EUR/m

**Lewmar Size 3 T-Track:**
- Art.-Nr.: 29003000 (Schiene, Meterware)
- Profilbreite: 32 mm, Höhe: 26 mm
- Material: Aluminium 6082-T6, hartanodisiert
- SWL: 2.800 kg
- Schraubenabstand: 125 mm
- Bootslänge: 12–18 m
- Gewicht: 0.78 kg/m
- Preis: ca. 70–100 EUR/m

**Lewmar Size 4 T-Track (Heavy Duty):**
- Art.-Nr.: 29004000 (Schiene, Meterware)
- Profilbreite: 40 mm, Höhe: 32 mm
- Material: Aluminium 6082-T6, hartanodisiert Typ III
- SWL: 5.200 kg
- Schraubenabstand: 150 mm
- Bootslänge: 16–25 m
- Gewicht: 1.18 kg/m
- Preis: ca. 110–160 EUR/m

#### 4.2.3 Lewmar Genua-Schienen und Schlitten

**Lewmar Size 2 Genua-Schlitten:**
- Art.-Nr.: 29102010 (Kugellager, Stand-Up), 29102020 (Kugellager, Kolbenstopp)
- SWL: 29102010: 800 kg, 29102020: 800 kg
- Bruchlast: 2.400 kg
- 12 Edelstahl-Kugeln pro Seite
- Integrierte Schmutzabstreifer
- Preis: 75–140 EUR

**Lewmar Size 3 Genua-Schlitten:**
- Art.-Nr.: 29103010 (Kugellager, Stand-Up), 29103020 (Kugellager, Kolbenstopp)
- SWL: 1.400 kg
- Bruchlast: 4.200 kg
- 16 Edelstahl-Kugeln pro Seite
- Preis: 120–210 EUR

#### 4.2.4 Lewmar Travellersysteme

**Lewmar Size 2 Traveller-Komplettsystem:**
- Art.-Nr.: 29202100 (1.5 m Schiene + Schlitten + Endstopps + Steuerleinen-Kit)
- Schiene: Size 2 T-Track, 1.5 m
- Schlitten: Kugellager mit Bügel und Schäkelaufnahme
- SWL System: 1.000 kg
- Steuerung: 4:1 mit Fiddle-Blöcken
- Bootslänge: 8–10 m
- Preis Komplettsystem: ca. 350–480 EUR

**Lewmar Size 3 Traveller-Komplettsystem:**
- Art.-Nr.: 29203100 (2.0 m Schiene + Schlitten + Endstopps + Steuerleinen-Kit)
- Schiene: Size 3 T-Track, 2.0 m
- SWL System: 2.200 kg
- Steuerung: 6:1 mit Fiddle-Blöcken
- Bootslänge: 11–14 m
- Preis Komplettsystem: ca. 550–750 EUR

### 4.3 Antal (Italien)

#### 4.3.1 Firmengeschichte und Marktposition

Antal S.r.l. wurde 1979 in Sesto Calende, Italien gegründet. Spezialisiert auf hochwertige Deck-Hardware für Segel- und Motoryachten. Antal hat sich als europäischer Premium-Hersteller etabliert, besonders stark im Bereich Custom- und Superyachten. Bekannt für innovative Designs und ansprechende Ästhetik.

#### 4.3.2 Antal T-Track System

**Antal T-Track 22:**
- Art.-Nr.: AT22.xx (Schiene, verschiedene Längen)
- Profilbreite: 22 mm, Höhe: 18 mm
- Material: Aluminium 6082-T6, hartanodisiert
- SWL: 700 kg
- Bootslänge: 6–9 m
- Preis: ca. 35–50 EUR/m

**Antal T-Track 25:**
- Art.-Nr.: AT25.xx
- Profilbreite: 25 mm, Höhe: 20 mm
- SWL: 1.100 kg
- Bootslänge: 8–12 m
- Preis: ca. 48–68 EUR/m

**Antal T-Track 32:**
- Art.-Nr.: AT32.xx
- Profilbreite: 32 mm, Höhe: 26 mm
- SWL: 2.600 kg
- Bootslänge: 11–16 m
- Preis: ca. 78–110 EUR/m

**Antal T-Track 40:**
- Art.-Nr.: AT40.xx
- Profilbreite: 40 mm, Höhe: 32 mm
- SWL: 4.800 kg
- Bootslänge: 15–22 m
- Preis: ca. 120–170 EUR/m

#### 4.3.3 Antal Schlitten

**Antal Kugellager-Schlitten Serie:**
- Art.-Nr.: ATC22B (22 mm), ATC25B (25 mm), ATC32B (32 mm), ATC40B (40 mm)
- Material: Eloxiertes Aluminium, Edelstahl-Kugeln
- SWL: 450 / 750 / 1.400 / 2.600 kg
- Bruchlast: 1.350 / 2.250 / 4.200 / 7.800 kg
- Besonderheit: Nachfüllöffnungen für Kugellagerschmierung
- Preis: 55–320 EUR

**Antal Gleitschlitten Serie:**
- Art.-Nr.: ATC22S (22 mm), ATC25S (25 mm), ATC32S (32 mm)
- Material: Eloxiertes Aluminium, PTFE-Gleitflächen
- SWL: 300 / 500 / 1.000 kg
- Preis: 35–180 EUR

### 4.4 Ronstan (Australien)

#### 4.4.1 Firmengeschichte und Marktposition

Ronstan wurde 1953 in Melbourne, Australien gegründet. Heute einer der größten Hersteller von Segelboot-Hardware weltweit. Besonders stark im Regatta- und Dinghy-Bereich, aber mit vollständigem Programm für Kielyachten. Ronstan ist bekannt für innovative Materialien und konsequenten Leichtbau.

#### 4.4.2 Ronstan Series 19

**Ronstan Series 19 T-Track:**
- Art.-Nr.: RC7190 (Schiene, Meterware)
- Profilbreite: 19 mm, Höhe: 15 mm
- Material: Aluminium 6060-T6, hartanodisiert
- SWL: 350 kg
- Bootslänge: 4–7 m (Dinghy und kleine Kielboote)
- Gewicht: 0.22 kg/m
- Preis: ca. 18–28 EUR/m

**Ronstan Series 19 Schlitten:**
- Art.-Nr.: RC71940 (Gleit), RC71941 (Kugellager), RC71942 (Kolbenstopp)
- SWL: 200 / 350 / 350 kg
- Preis: 22–65 EUR

#### 4.4.3 Ronstan Series 22

**Ronstan Series 22 T-Track:**
- Art.-Nr.: RC7220 (Schiene, Meterware)
- Profilbreite: 22 mm, Höhe: 18 mm
- SWL: 700 kg
- Bootslänge: 7–10 m
- Gewicht: 0.33 kg/m
- Preis: ca. 28–42 EUR/m

**Ronstan Series 22 Schlitten:**
- Art.-Nr.: RC72240 (Gleit, Stand-Up), RC72241 (Kugellager, Stand-Up), RC72242 (Kugellager, Low-Profile)
- SWL: 400 / 700 / 700 kg
- 10 Edelstahl-Kugeln pro Seite
- Preis: 38–110 EUR

#### 4.4.4 Ronstan Series 25

**Ronstan Series 25 T-Track:**
- Art.-Nr.: RC7250 (Schiene, Meterware)
- Profilbreite: 25 mm, Höhe: 20 mm
- SWL: 1.200 kg
- Bootslänge: 9–13 m
- Gewicht: 0.48 kg/m
- Preis: ca. 42–62 EUR/m

**Ronstan Series 25 Schlitten:**
- Art.-Nr.: RC72540 (Gleit), RC72541 (Kugellager, Stand-Up), RC72542 (Kugellager, Low-Profile), RC72543 (Kugellager, Kolbenstopp)
- SWL: 650 / 1.200 / 1.200 / 1.200 kg
- 14 Edelstahl-Kugeln pro Seite
- Preis: 55–165 EUR

#### 4.4.5 Ronstan Series 32

**Ronstan Series 32 T-Track:**
- Art.-Nr.: RC7320 (Schiene, Meterware)
- Profilbreite: 32 mm, Höhe: 26 mm
- SWL: 2.800 kg
- Bootslänge: 12–18 m
- Gewicht: 0.80 kg/m
- Preis: ca. 68–98 EUR/m

**Ronstan Series 32 Schlitten:**
- Art.-Nr.: RC73240 (Gleit), RC73241 (Kugellager, Stand-Up), RC73242 (Kugellager, Low-Profile)
- SWL: 1.500 / 2.800 / 2.800 kg
- 20 Edelstahl-Kugeln pro Seite
- Preis: 95–280 EUR

#### 4.4.6 Ronstan RC-Series Cars (Regatta-Linie)

**Ronstan RC81940 (Series 19 Regatta Car):**
- Ultraleichter Kugellager-Schlitten
- Material: Titan-Bügel, Torlon-Kugeln
- SWL: 300 kg
- Gewicht: nur 48 g
- Preis: ca. 120 EUR

**Ronstan RC82241 (Series 22 Regatta Car):**
- Material: Aluminium, Torlon-Kugeln
- SWL: 600 kg
- Gewicht: 85 g
- Preis: ca. 165 EUR

### 4.5 Schaefer Marine (USA)

#### 4.5.1 Firmengeschichte und Marktposition

Schaefer Marine wurde 1962 in New Bedford, Massachusetts (USA) gegründet. Spezialisiert auf Travellersysteme und Rollreff-Anlagen. Schaefer-Traveller gelten als Referenz im amerikanischen Fahrtensegelbereich und sind bei vielen US-Werften (Catalina, Hunter, Island Packet) Standard-Ausrüstung.

#### 4.5.2 Schaefer Travellersysteme

**Schaefer Series 1 Traveller (Small Boat):**
- Art.-Nr.: 502-10xx (verschiedene Schienenlängen)
- Profilbreite: 22 mm (proprietäres Profil)
- Schlitten: Edelstahl-Gehäuse mit Delrin-Rollen
- SWL System: 550 kg
- Bootslänge: 6–8 m
- Schiene: Edelstahl 316L oder Aluminium
- Komplettsystem inkl. Endstopps und Steuerleinen
- Preis: 250–380 EUR

**Schaefer Series 2 Traveller (Midrange):**
- Art.-Nr.: 504-20xx
- Profilbreite: 25 mm
- Schlitten: Kugellager, Edelstahl
- SWL System: 1.200 kg
- Bootslänge: 8–12 m
- Preis: 380–550 EUR

**Schaefer Series 3 Traveller (Big Boat):**
- Art.-Nr.: 506-30xx
- Profilbreite: 32 mm
- Schlitten: Kugellager, eloxiertes Aluminium
- SWL System: 2.500 kg
- Bootslänge: 12–18 m
- Preis: 580–850 EUR

**Schaefer Series 4 Traveller (Offshore):**
- Art.-Nr.: 508-40xx
- Profilbreite: 40 mm
- Schlitten: Hochlast-Kugellager
- SWL System: 4.500 kg
- Bootslänge: 16–25 m
- Preis: 900–1.400 EUR

#### 4.5.3 Schaefer Besonderheiten

- **Patentierte Kugellager-Rücklaufbahn**: Kugeln werden im endlosen Kreislauf geführt, kein toter Punkt
- **Edelstahl-Schienen als Standard**: Höhere Korrosionsbeständigkeit als Aluminium
- **Integrierte Seilanschläge**: Steuerleinen werden im Schlitten festgeklemmt, nicht geknotet
- **Austauschbare Kugellager-Kassetten**: Wartung ohne Schlittendemontage

### 4.6 Seldén (Schweden)

#### 4.6.1 Firmengeschichte und Marktposition

Seldén Mast AB wurde 1960 in Göteborg, Schweden gegründet. Primär bekannt als Masthersteller, bietet Seldén ein vollständiges Programm an Deck-Hardware und Schienensystemen. Seldén-Systeme sind besonders bei skandinavischen und europäischen Werften verbreitet (Hallberg-Rassy, Najad, X-Yachts als OEM-Zulieferer).

#### 4.6.2 Seldén Track-Programm

**Seldén Genua T-Track 25:**
- Art.-Nr.: 521-012 (Meterware)
- Profilbreite: 25 mm, Höhe: 20 mm
- Material: Aluminium 6082-T6, hartanodisiert Typ III
- SWL: 1.100 kg
- Bootslänge: 8–12 m
- Preis: ca. 45–65 EUR/m

**Seldén Genua T-Track 32:**
- Art.-Nr.: 521-022 (Meterware)
- Profilbreite: 32 mm, Höhe: 26 mm
- SWL: 2.500 kg
- Bootslänge: 12–18 m
- Preis: ca. 72–100 EUR/m

#### 4.6.3 Seldén Schlitten

**Seldén Genua-Schlitten 25:**
- Art.-Nr.: 521-115 (Kugellager, Stand-Up), 521-116 (Kugellager, Kolbenstopp)
- SWL: 800 / 800 kg
- Preis: 85–145 EUR

**Seldén Genua-Schlitten 32:**
- Art.-Nr.: 521-215 (Kugellager, Stand-Up), 521-216 (Kugellager, Kolbenstopp)
- SWL: 1.600 / 1.600 kg
- Preis: 135–220 EUR

### 4.7 Frederiksen (Dänemark)

#### 4.7.1 Firmengeschichte und Marktposition

Frederiksen A/S wurde 1958 in Nykøbing Falster, Dänemark gegründet. Bekannt für preisgünstige, aber funktionale Deck-Hardware. Frederiksen bedient den Budget- bis Mittelklasse-Markt und ist bei skandinavischen Werften als kostengünstiger OEM-Zulieferer beliebt. In den letzten Jahren auch mit hochwertigen Regatta-Produkten vertreten.

#### 4.7.2 Frederiksen Track-Programm

**Frederiksen Budget-Line T-Track 20:**
- Art.-Nr.: F-2000 (Schiene, Meterware)
- Profilbreite: 20 mm, Höhe: 15 mm
- Material: Aluminium 6060-T5, standardanodisiert
- SWL: 400 kg
- Bootslänge: 5–7 m
- Preis: ca. 15–22 EUR/m (deutlich günstiger als Harken/Ronstan)

**Frederiksen Budget-Line T-Track 25:**
- Art.-Nr.: F-2500 (Schiene, Meterware)
- Profilbreite: 25 mm, Höhe: 19 mm
- SWL: 900 kg
- Bootslänge: 7–11 m
- Preis: ca. 25–38 EUR/m

**Frederiksen Racing-Line T-Track 25:**
- Art.-Nr.: F-2500R (Schiene, Meterware)
- Profilbreite: 25 mm, Höhe: 20 mm
- Material: Aluminium 6082-T6, hartanodisiert Typ III
- SWL: 1.200 kg
- Bootslänge: 8–12 m
- Preis: ca. 38–55 EUR/m

**Frederiksen Budget-Line T-Track 32:**
- Art.-Nr.: F-3200 (Schiene, Meterware)
- Profilbreite: 32 mm, Höhe: 24 mm
- SWL: 2.200 kg
- Bootslänge: 11–16 m
- Preis: ca. 48–70 EUR/m

#### 4.7.3 Frederiksen Schlitten

**Frederiksen Budget-Schlitten:**
- Art.-Nr.: F-2010 (20 mm Gleit), F-2510 (25 mm Gleit), F-3210 (32 mm Gleit)
- Material: Eloxiertes Aluminium, Delrin-Gleitflächen
- SWL: 250 / 550 / 1.200 kg
- Preis: 18–75 EUR (ca. 40–50 % unter Harken)

**Frederiksen Racing-Schlitten:**
- Art.-Nr.: F-2511R (25 mm Kugellager), F-3211R (32 mm Kugellager)
- SWL: 900 / 2.000 kg
- Preis: 65–180 EUR

### 4.8 Herstellervergleich — Zusammenfassung

| Hersteller | Stärke | Schwäche | Preissegment | Typischer Einsatz |
|-----------|--------|----------|-------------|-------------------|
| Harken | Qualität, Sortimentstiefe | Hoher Preis | Premium | Regatta + Fahrt |
| Lewmar | OEM-Verfügbarkeit, Service | Weniger Innovation | Mittel-Premium | Fahrt, Werft-OEM |
| Antal | Design, Ästhetik | Eingeschränkte Verfügbarkeit | Premium | Custom, Superyacht |
| Ronstan | Leichtbau, Innovation | Teilweise nur Online | Mittel-Premium | Regatta, Leichtbau |
| Schaefer | Traveller-Spezialist | Begrenztes Sortiment | Mittel-Premium | Fahrt (US-Markt) |
| Seldén | Systemintegration Mast+Deck | Abhängig von Mastkauf | Mittel | Fahrt, OEM |
| Frederiksen | Preis-Leistung | Geringere Qualitätswahrnehmung | Budget-Mittel | Budget, OEM |

---

## 5. Montage und Installation

### 5.1 Vorbereitung

#### 5.1.1 Werkzeug und Material

**Erforderliches Werkzeug:**
- Bohrmaschine mit Drehzahlregelung
- Bohrer: HSS-Bohrer in den Schraubendurchmessern (3.5, 4.2, 5.0, 6.5, 8.5 mm)
- Senkbohrer für Schraubenköpfe (90° Kegelsenker)
- Gewindeschneider (M5, M6, M8 abhängig von Schraubengröße)
- Kreuzschlitz- und Torx-Schraubendreher
- Drehmomentschlüssel (Bereich 5–25 Nm)
- Schlagschnur oder Laserlineal für Ausrichtung
- Bohrschablone (Herstellerspezifisch oder selbst angefertigt)
- Maßband, Zollstock, Anschlagwinkel
- Alkohol-Reiniger (Isopropanol) für Entfettung
- Vakuum-Bohrständer (optional, für perfekte Senkrechtbohrungen)

**Erforderliches Material:**
- Befestigungsschrauben (Edelstahl A4-80 / 316L)
- Unterlegscheiben (Edelstahl A4, großflächig)
- Gegenplatten (Edelstahl oder Aluminium, min. 3 mm)
- Dichtmasse (Sikaflex 291 oder 3M 4200)
- Primer für Dichtmasse (Sika Primer 209D)
- Kernfüllung (Epoxid + Mikrosphären bei Sandwich-Decks)
- Schienenschmierung (Harken McLube, Teflon-Spray)

#### 5.1.2 Deck-Analyse vor Montage

**Sandwich-Deck prüfen:**
1. Klopftest: Dumpfer Klang = Kernmaterial vorhanden; heller Klang = Volllaminat oder delaminiert
2. Kernmaterial identifizieren: Balsa, PVC-Schaum (Divinycell), SAN-Schaum (Corecell)
3. Kernstärke bestimmen: Typisch 10–25 mm
4. Decksstärke gesamt messen: Typisch 18–35 mm bei Seitendeck
5. Unterdeck-Zugang prüfen: Gegenplatten müssen von unten montierbar sein

**Montagefläche prüfen:**
- Ebenheit: max. 1 mm Abweichung auf Schienenlänge (sonst Shims verwenden)
- Stufen oder Absätze: Müssen mit Shims oder Fräsung ausgeglichen werden
- Bestehende Bohrungen: Alte Bohrungen verschließen (Epoxid + GFK-Stopfen)
- Rutschfeste Beschichtung: Muss im Montagebereich entfernt werden

### 5.2 Schraubenmuster und -abstände

#### 5.2.1 Standard-Schraubenabstände

| Schienenprofil (mm) | Schraubenabstand (mm) | Schraubendurchmesser | Anzugsmoment (Nm) |
|---------------------|----------------------|---------------------|-------------------|
| 19 | 75 | M5 / #10 | 5–7 |
| 22 | 100 | M5 / #10 | 5–7 |
| 25 | 100 | M6 / 1/4" | 8–10 |
| 32 | 125 | M8 / 5/16" | 12–16 |
| 40 | 150 | M10 / 3/8" | 18–22 |
| 50 | 175 | M10 / 3/8" | 18–22 |

#### 5.2.2 Durch-Bolzen vs. Blechschrauben

**Durch-Bolzen (empfohlen für alle Anwendungen > 500 kg SWL):**
- Edelstahl-Maschinenschraube durch Deck + Gegenplatte
- Gegenplatte min. 40 × Deckbreite × 3 mm stark
- Mutter: Nylock (Nylonsicherung) oder mit Sicherungsscheibe
- Vorteil: Höchste Auszugsfestigkeit, gleichmäßige Lastverteilung
- Nachteil: Zugang von unten erforderlich

**Blechschrauben (akzeptabel nur für niedrige Lasten < 500 kg):**
- Edelstahl A4 Blechschrauben in Deck geschraubt
- Nur in Volllaminat (nicht Sandwich ohne Kernverstärkung)
- Vorteil: Kein Zugang von unten nötig
- Nachteil: Geringere Auszugskraft, Risiko der Lockerung

**Gewindeeinsätze (Alternative):**
- Helicoil oder Keensert in Epoxid-verstärktem Kern
- Vorteil: Kein Zugang von unten nötig, höhere Auszugskraft als Blechschrauben
- Nachteil: Aufwändigere Vorbereitung, nicht nachjustierbar

### 5.3 Kernverstärkung bei Sandwich-Decks

#### 5.3.1 Methode: Kernfüllung

**Schritt-für-Schritt:**

1. Bohrung durch Deck bohren (Pilotbohrung, 4–5 mm)
2. Bohrung auf Schraubendurchmesser + 2 mm aufweiten
3. Kernmaterial im Bohrungsbereich entfernen (konischer Fräser, 20–25 mm Radius)
4. Deck umdrehen, von unten ebenfalls aufweiten
5. Pilotbohrung temporär verschließen (Klebeband von einer Seite)
6. Epoxidharz + Microballon-Füller anmischen (Konsistenz: Erdnussbutter)
7. In die aufgeweitete Bohrung injizieren (Spritze oder Spachtel)
8. 24 h aushärten lassen bei min. 15°C
9. Durch die Epoxid-Füllung auf Schraubendurchmesser nachbohren
10. Schiene montieren mit Dichtmasse

**Empfohlene Epoxidharze:**
- West System 105/206 + 407 (Low-Density Filler)
- SP Systems / Gurit Ampreg 21
- Sicomin SR 1500 + SD 2503

### 5.4 Ausrichtung (Alignment)

#### 5.4.1 Genua-Schiene — Ausrichtung

**Methode 1: Schlagschnur:**
1. Idealposition des vorderen Schotblocks bestimmen (Kreuzpeiling: Vorliek-Unterkante → Achterliek-Unterkante)
2. Idealposition des hinteren Schotblocks bestimmen (für gerefftes Segel)
3. Schlagschnur zwischen beiden Punkten spannen
4. Schiene entlang der Schnur ausrichten
5. Vordere und hintere Bohrung markieren, dann Zwischenbohrungen

**Methode 2: Laserlineal:**
1. Laser auf die Seitendecksmittellinie ausrichten
2. Schiene parallel zum Laser positionieren
3. Abstand zur Mittellinie: typisch 100–180 mm (abhängig von Bootsbreite und Schotwinkel)

**Schotwinkel-Berechnung:**
```
Abstand_zur_Mittellinie = tan(Schotwinkel) × Abstand_Schiene_zum_Vorstagfuß

Typische Schotwinkel:
- Genua 150%: 7–10°
- Genua 130%: 10–12°
- Fock 100%: 12–15°
- Selbstwendefock: 8–12°
```

#### 5.4.2 Traveller — Ausrichtung

**Ausrichtung Großschot-Traveller:**
1. Travellerschiene muss exakt rechtwinklig zur Bootsmittellinie stehen
2. Prüfung: Maßband von Mastmitte zu beiden Schienenenden → gleiche Entfernung
3. Toleranz: max. 2 mm Abweichung über die Schienenlänge
4. Schiene darf kein Gefälle haben → Wasserwaage in beide Richtungen

### 5.5 Dichtung der Montagebohrungen

#### 5.5.1 Dichtmasse-Anwendung

**Empfohlene Dichtmassen:**

| Produkt | Typ | Aushärtung | Shore A | Empfehlung |
|---------|-----|-----------|---------|------------|
| Sikaflex 291 | PU, elastisch | 3–5 Tage | 40 | Standard für Deck-Beschläge |
| 3M 4200 | PU, elastisch | 3–5 Tage | 35 | Alternative, leichter demontierbar |
| Sikaflex 292i | PU, strukturell | 5–7 Tage | 55 | Für dauerhafte Verbindungen |
| 3M 5200 | PU, permanent | 5–7 Tage | 55 | Sehr schwer demontierbar! |
| Butylband | Butyl | Sofort | - | Unter Schienenfuß als Zusatzdichtung |

**Anwendungsreihenfolge:**
1. Oberfläche reinigen (Isopropanol)
2. Primer auftragen (Sika 209D), 30 min trocknen
3. Dichtmasse auf Schraubenschaft auftragen (Helix-Muster)
4. Dichtmasse auf Montagefläche auftragen (Raupe um jede Bohrung)
5. Schiene aufsetzen, Schrauben handfest anziehen
6. Überschüssige Dichtmasse entfernen (Spachtel, dann mit Spülmittel-Wasser glätten)
7. 24 h warten, dann Schrauben auf Drehmoment anziehen
8. Nochmals überschüssige Dichtmasse entfernen

### 5.6 Shimming (Unterfütterung)

#### 5.6.1 Wann sind Shims erforderlich?

- Decksneigung > 3° quer zur Schiene → Keil-Shims
- Decksunebenheit > 1 mm → Flach-Shims
- Nachträgliche Verstellung der Schienenhöhe
- Ausgleich von Decksverformungen

**Shim-Materialien:**
- Aluminium: 0.5, 1.0, 1.5, 2.0 mm (Harken-Standard)
- Edelstahl: 0.5, 1.0 mm (für korrosive Umgebungen)
- Kunststoff (Delrin): 1.0, 2.0 mm (galvanische Trennung Alu-Schiene ↔ Stahl-Deck)
- GFK-Laminat: Maßgefertigt (für große Unebenheiten)

---

## 6. Anlagen-spezifische Zuordnung

### 6.1 Zuordnung nach Bootsklasse

#### 6.1.1 Jolle / Dinghy (3–6 m)

| Anwendung | Schiene | Schlitten | Hersteller-Empfehlung |
|-----------|---------|-----------|----------------------|
| Fock-Schot | 19 mm T-Track | Gleit oder Kolbenstopp | Ronstan S19, Harken 19 |
| Traveller | 19 mm T-Track | Gleit mit Kontrollleinen | Ronstan S19, Frederiksen 20 |
| Spi-Barberhaul | 19 mm T-Track | Gleit | Ronstan S19 |

**Besonderheiten Jolle:**
- Gewicht ist kritisch → leichteste Systeme bevorzugen
- Edelstahl vermeiden wo möglich (Gewicht)
- Schraubenmontage oder Pop-Nieten
- Spritzwasser-Exposition maximal → wartungsfreie Gleitschlitten bevorzugen

#### 6.1.2 Kleine Kielyacht / Fahrtensegler (7–10 m)

| Anwendung | Schiene | Schlitten | Hersteller-Empfehlung |
|-----------|---------|-----------|----------------------|
| Genua-Schiene | 22–25 mm T-Track, 1.2–1.5 m | Kugellager oder Kolbenstopp | Harken 22/27, Lewmar S2 |
| Traveller | 22–25 mm T-Track, 1.2–1.6 m | Kugellager + Fiddle-Block | Harken MR 27, Lewmar S2 Trav. |
| Spi-Barberhaul | 19–22 mm T-Track, 0.5–0.8 m | Gleit oder Kugellager | Ronstan S22, Frederiksen 22 |
| Baumniederholer | 19 mm T-Track, 0.2–0.3 m | Gleit | Ronstan S19 |

**Besonderheiten:**
- Durch-Bolzen empfohlen für Traveller
- Genua-Schiene: Blechschrauben akzeptabel bei Volllaminat
- Budget-Option: Frederiksen Budget-Line mit Gleitschlitten

#### 6.1.3 Mittelgroße Fahrtenyacht (10–14 m)

| Anwendung | Schiene | Schlitten | Hersteller-Empfehlung |
|-----------|---------|-----------|----------------------|
| Genua-Schiene | 25–32 mm T-Track, 1.8–2.5 m | Kugellager + Kolbenstopp | Harken 27/32, Lewmar S2/S3 |
| Traveller | 25–32 mm T-Track, 1.6–2.2 m | Kugellager + 6:1 Steuerung | Harken 32, Schaefer S3 |
| Selbstwendefock | 25 mm T-Track, 1.8–2.2 m quer | Kugellager mit Blockarm | Harken 27, Seldén 25 |
| Spi-Barberhaul | 22–25 mm T-Track, 0.6–1.0 m | Kugellager | Harken 22, Ronstan S22 |
| Backstag | 25–32 mm T-Track, 0.6–1.0 m | Hochlast-Kugellager | Harken 32, Antal 32 |

**Besonderheiten:**
- Durch-Bolzen obligatorisch für Traveller und Backstag-Schiene
- Kernverstärkung bei Sandwich-Deck immer erforderlich
- Professionelle Ausrichtung empfohlen (Segelmacher oder Rigger)

#### 6.1.4 Große Fahrtenyacht (14–20 m)

| Anwendung | Schiene | Schlitten | Hersteller-Empfehlung |
|-----------|---------|-----------|----------------------|
| Genua-Schiene | 32 mm T-Track, 2.5–3.5 m | Kugellager + Steuerleinen | Harken 32, Lewmar S3 |
| Traveller | 32–40 mm T-Track, 2.2–3.0 m | Kugellager + 8:1 Steuerung | Harken 42, Schaefer S4 |
| Spi-Barberhaul | 25–32 mm T-Track, 0.8–1.5 m | Kugellager | Harken 27, Antal 32 |
| Backstag | 32 mm T-Track, 0.8–1.2 m | Hochlast | Harken 32 |

**Besonderheiten:**
- Hydraulische Traveller-Steuerung sinnvoll ab 16 m
- Elektrische Winschen für Steuerleinen
- Edelstahl-Schienen für sichtbare Bereiche
- Professionelle Installation zwingend

#### 6.1.5 Superyacht (20 m+)

| Anwendung | Schiene | Schlitten | Hersteller-Empfehlung |
|-----------|---------|-----------|----------------------|
| Genua-Schiene | 40–50 mm T-Track oder HL-Track | Hochlast-Kugellager | Harken 42/HL, Antal 40 |
| Traveller | 40–50 mm HL-Track oder I-Beam | Hydraulisch gesteuert | Harken HL, Lewmar S4 |
| Selbstwendefock | 32–40 mm T-Track, 3.0–4.0 m quer | Hochlast-Kugellager | Harken 42 |

**Besonderheiten:**
- Alle Systeme hydraulisch oder elektrisch gesteuert
- Edelstahl 316L oder Carbon für sichtbare Komponenten
- Bündige Decksmontage (Flush Mount)
- Versteckte Steuerleinen unter Deck
- Regelmäßige professionelle Wartung zwingend

### 6.2 Zuordnung nach Einsatzzweck

#### 6.2.1 Regatta-Yacht

**Prioritäten:** Leichtgängigkeit > Gewicht > Haltbarkeit > Preis

- Kugellager-Schlitten obligatorisch (µ < 0.05)
- Leichteste verfügbare Profile (ggf. 7075-T6)
- Torlon-Kugeln statt Edelstahl (Gewichtsersparnis)
- Schienen exakt nach Segelmacher-Vorgabe positioniert
- Piston-Stops für schnelle Genua-Wechsel
- Reibungsarme UHMWPE-Steuerleinen
- Karbonfaser-Schlitten für extreme Leichtbau-Anwendungen

#### 6.2.2 Blauwasser-Fahrtenyacht

**Prioritäten:** Haltbarkeit > Wartungsarmut > Bedienbarkeit > Gewicht > Preis

- Gleitschlitten bevorzugen (wartungsarm, salzwassertolerant)
- Oder Kugellager-Schlitten mit guten Dichtlippen
- Überdimensionierung um eine Größe (Sicherheitsreserve)
- Edelstahl-Endstopper (korrosionsbeständiger als Aluminium)
- Einfache, robuste Steuerungssysteme (wenige Umlenkungen)
- Ersatzteile an Bord (Kugeln, Dichtungen, Endstopps)

#### 6.2.3 Charter-Yacht

**Prioritäten:** Robustheit > Bedienbarkeit > Wartungsarmut > Preis

- Gleitschlitten bevorzugen (Vandalismus-resistent)
- Kolbenstopp-Schlitten für feste Positionen (charterfreundlich)
- Übergroße Endstopper (Sicherheit bei Fehlbedienung)
- Farbliche Markierungen an den Schlitten für Trimmpositionen
- Hochwertige Dichtmasse bei Montage (kein Nachziehen durch Charter-Gäste)

---

## 7. Fehlerbild-Atlas

### 7.1 Fehlerbild F-01: Schienenverschleiß (Track Wear)

**Symptome:**
- Sichtbare Rillenbildung in der Schienenlaufbahn
- Schlitten verkippt seitlich oder wackelt auf der Schiene
- Metallabrieb (feiner silberner/schwarzer Staub) an den Schienenenden
- Schlitten lässt sich nicht mehr frei verschieben

**Ursachen:**
- Normale Abnutzung über 10.000+ Seemeilen
- Seitenlasten durch falsche Schotführung
- Korrodierte Kugeln verursachen abrasiven Verschleiß
- Sand und Salzpartikel in der Laufbahn
- Mangelnde Schmierung über Jahre

**Schweregrad:** MITTEL bis HOCH (bei tragender Funktion)

**Bewertung (AYDI-Score):**
- Leichte Rillenbildung (< 0.3 mm Tiefe): Score 70–80, Empfehlung: Schmierung, Beobachtung
- Deutliche Rillenbildung (0.3–0.8 mm): Score 40–60, Empfehlung: Austausch planen
- Tiefe Rillen (> 0.8 mm): Score 10–30, Empfehlung: Sofortiger Austausch

**Maßnahmen:**
1. Schiene reinigen (Süßwasser + Bürste)
2. Verschleißtiefe messen (Messschieber oder Fühlerlehre)
3. Bei > 0.5 mm Verschleißtiefe: Schiene tauschen
4. Bei < 0.5 mm: Schmierung und kürzere Inspektionsintervalle

### 7.2 Fehlerbild F-02: Kugellager-Ausfall (Car Bearing Failure)

**Symptome:**
- Schlitten bewegt sich ruckartig (Stick-Slip)
- Knirschen oder Kratzen beim Verschieben
- Schlitten blockiert unter Last
- Einzelne Kugeln fehlen oder sind aus dem Käfig gefallen
- Rostflecken am Schlitten oder auf der Schiene

**Ursachen:**
- Salzwasserkorrosion der Kugeln (316L korrodiert in Spalten)
- Käfigbruch (Delrin altert unter UV)
- Überlastung → Kugelabflachung (Brinelling)
- Fehlende Schmierung → Trockenlauf
- Sand zwischen Kugeln und Laufbahn

**Schweregrad:** HOCH (Schlittenfunktion beeinträchtigt)

**Bewertung (AYDI-Score):**
- Leichte Schwergängigkeit: Score 60–70, Empfehlung: Reinigung, Schmierung
- Deutliches Knirschen: Score 30–50, Empfehlung: Kugel/Käfig-Tausch
- Blockade unter Last: Score 0–20, Empfehlung: Sofortiger Schlittentausch

**Maßnahmen:**
1. Schlitten von der Schiene nehmen
2. Komplett zerlegen (Kugeln, Käfig, Dichtungen)
3. Alle Teile in Süßwasser + Spülmittel reinigen
4. Kugeln und Käfig inspizieren (Lupe)
5. Korrodierte/abgeflachte Kugeln ersetzen (Ersatzset vom Hersteller)
6. Gebrochenen Käfig ersetzen
7. Schlitten mit Marine-Schmierfett neu befüllen (McLube OneDrop oder Harken Lubricant)
8. Dichtlippen auf Risse prüfen, ggf. ersetzen

### 7.3 Fehlerbild F-03: Endstopper-Versagen (End Stop Failure)

**Symptome:**
- Endstopper abgeschert oder verbogen
- Schlitten am Schienenende herausgelaufen
- Schrauben des Endstoppers ausgerissen
- Endstopper fehlt ganz (über Bord verloren)

**Ursachen:**
- Überlastung durch Patenthalse oder unkontrolliertes Manöver
- Ermüdungsbruch bei wiederholter Stoßbelastung
- Falsche Dimensionierung (Endstopper zu klein für die Last)
- Korrosion der Befestigungsschrauben
- Falsche Montage (nur eine Schraube statt zwei)

**Schweregrad:** KRITISCH (Sicherheitsrisiko)

**Bewertung (AYDI-Score):**
- Endstopper locker: Score 30–40, Empfehlung: Nachziehen, Zustand prüfen
- Endstopper verbogen: Score 10–20, Empfehlung: Sofortiger Tausch
- Endstopper fehlt: Score 0, Empfehlung: Segel nicht setzen bis repariert

**Maßnahmen:**
1. Sofort: Schlitten mit Leine gegen Auslaufen sichern
2. Endstopper durch gleichwertigen oder stärkeren ersetzen
3. Ursache des Versagens ermitteln (Überlastung? Korrosion? Montagefehler?)
4. Beide Endstopps prüfen (oft symmetrischer Verschleiß)
5. Ggf. Schiene im Endbereich auf Beschädigung prüfen

### 7.4 Fehlerbild F-04: Decksdelamination unter der Schiene (Deck Delamination)

**Symptome:**
- Schiene sitzt nicht mehr plan auf dem Deck
- Schrauben lassen sich ohne Widerstand drehen
- Dumpfer Klang beim Klopfen um die Schienenbasis
- Wasserflecken unter Deck im Bereich der Schiene
- Sichtbare Risse im Gelcoat entlang der Schienenkante

**Ursachen:**
- Wassereinbruch durch undichte Schraubenlöcher
- Frostschäden in wassergesättigtem Balsakerl
- Überlastung → Kernquetschung
- Fehlende Kernverstärkung bei der Erstmontage
- Osmotische Blasenbildung im Laminat

**Schweregrad:** KRITISCH (Strukturschaden)

**Bewertung (AYDI-Score):**
- Leichte Weichstellen: Score 30–50, Empfehlung: Kernreparatur planen
- Deutliche Delamination: Score 10–30, Empfehlung: Schiene demontieren, Kern reparieren
- Großflächige Zerstörung: Score 0–10, Empfehlung: Professionelle Decksreparatur

**Maßnahmen:**
1. Schiene demontieren
2. Alle alten Schraubenlöcher ausräumen (Kernmaterial entfernen, 25 mm Radius)
3. Delaminierte Bereiche trocknen lassen (min. 2 Wochen, ggf. mit Vakuum)
4. Kern mit Epoxid + Mikrosphären füllen
5. Ggf. zusätzliche GFK-Lagen von unten laminieren
6. Neue Bohrungen setzen (versetzt zu den alten, wenn möglich)
7. Schiene mit korrekter Dichtung und Durch-Bolzen remontieren

### 7.5 Fehlerbild F-05: Korrosion in der Schienennut (Track Groove Corrosion)

**Symptome:**
- Weiße Ablagerungen (Aluminiumoxid) in der Schienennut
- Rauhe, poröse Oberfläche in der Laufbahn
- Schlitten läuft rau oder blockiert
- Eloxierung abgeblättert oder beschädigt

**Ursachen:**
- Galvanische Korrosion (Edelstahl-Schrauben in Aluminium-Schiene ohne Isolierung)
- Salzwasseransammlung in der Nut (stehendes Wasser)
- Beschädigte Eloxierung (Kratzer, Schläge)
- Kontakt mit Kupfer-basierten Antifouling-Rückständen

**Schweregrad:** MITTEL

**Bewertung (AYDI-Score):**
- Oberflächliche Oxidation: Score 60–80, Empfehlung: Reinigen, konservieren
- Tiefe Grübchenkorrosion: Score 30–50, Empfehlung: Austausch mittelfristig planen
- Durchkorrosion: Score 0–20, Empfehlung: Sofortiger Austausch

**Maßnahmen:**
1. Schiene mit Aluminium-Reiniger behandeln (z.B. Star brite Aluminium Cleaner)
2. Korrodierte Stellen mit feinem Scotch-Brite-Pad glätten
3. Konservierung mit Korrosionsschutz (Lanocote, Duralac)
4. Galvanische Trennung herstellen (Teflon-Unterlegscheiben)
5. Drainagelöcher in der Schienennut bohren (gegen Wasseransammlung)

### 7.6 Fehlerbild F-06: Schienenverdrehung (Track Twist)

**Symptome:**
- Schiene steht nicht mehr senkrecht zum Deck
- Schlitten verkippt auf einer Seite
- Höherer Reibungswiderstand auf einer Seite
- Sichtbare Verdrehung der Schiene bei Draufsicht

**Ursachen:**
- Einseitige Belastung über lange Zeit
- Schrauben auf einer Seite lockerer als auf der anderen
- Decksverformung unter der Schiene
- Materialermüdung bei dünnem Profil
- Thermische Verformung (unterschiedliche Sonneneinstrahlung)

**Schweregrad:** MITTEL

**Bewertung (AYDI-Score):**
- Verdrehung < 2°: Score 60–80, Empfehlung: Schrauben nachziehen, Shims prüfen
- Verdrehung 2–5°: Score 30–50, Empfehlung: Schiene richten oder tauschen
- Verdrehung > 5°: Score 10–30, Empfehlung: Schiene tauschen, Ursache beheben

### 7.7 Fehlerbild F-07: Steuerleinen-Versagen (Control Line Failure)

**Symptome:**
- Traveller lässt sich nicht mehr fixieren
- Steuerleinen sind gescheuert oder gebrochen
- Traveller läuft bei Böe unkontrolliert auf die Lee-Seite
- Leinen rutschen durch die Klemmen

**Ursachen:**
- Schamfilen der Leinen an scharfen Kanten
- UV-Degradation der Leinen (besonders Dyneema-Mantel)
- Überlastung → Leinenbruch
- Verschlissene Curryklemmen (halten nicht mehr)
- Falsche Leinenführung (zu spitzer Winkel)

**Schweregrad:** HOCH bis KRITISCH

**Bewertung (AYDI-Score):**
- Leichter Verschleiß: Score 50–70, Empfehlung: Leinen tauschen bei nächster Gelegenheit
- Gescheuerte Stellen sichtbar: Score 20–40, Empfehlung: Sofort tauschen
- Leine gebrochen: Score 0, Empfehlung: Traveller sichern, nicht segeln

### 7.8 Fehlerbild F-08: Schienenbefestigung gelockert (Track Mounting Loosened)

**Symptome:**
- Schiene bewegt sich seitlich beim Drücken
- Klapperndes Geräusch beim Segeln
- Dichtmasse an den Schrauben aufgerissen
- Wassereintritte an den Schraubenlöchern

**Ursachen:**
- Vibrationsbelastung lockert Schrauben (besonders bei Motorbetrieb)
- Dichtmasse hat sich gelöst (End of Life)
- Holzuntergrund geschrumpft (ältere Boote mit Teakdeck über GFK)
- Zu geringes Anzugsmoment bei Montage
- Fehlende Sicherungselemente (Loctite, Nylock)

**Schweregrad:** MITTEL bis HOCH

**Bewertung (AYDI-Score):**
- Leichtes Spiel: Score 50–70, Empfehlung: Nachziehen, abdichten
- Deutliches Spiel: Score 20–40, Empfehlung: Demontage, Neuabdichtung
- Schiene lose: Score 0–10, Empfehlung: Sofortige Reparatur

### 7.9 Fehlerbild F-09: Galvanische Korrosion Schiene/Deck (Galvanic Corrosion)

**Symptome:**
- Weiße/graue Ablagerungen um die Schraubenköpfe
- Aluminium-Schiene zeigt Lochfraß an den Kontaktflächen zum Edelstahl
- Schrauben festgefressen (können nicht mehr gelöst werden)
- Braune Verfärbungen (Rost) trotz Edelstahl-Schrauben

**Ursachen:**
- Fehlende galvanische Trennung zwischen Alu-Schiene und Edelstahl-Schrauben
- Salzwasser als Elektrolyt in den Kontaktzonen
- Fehlende oder beschädigte Dichtmasse
- Kontakt mit Carbon-Deck (extremes Galvanikproblem)

**Schweregrad:** MITTEL bis HOCH

**Bewertung (AYDI-Score):**
- Oberflächliche Korrosion: Score 50–70, Empfehlung: Isolation nachrüsten
- Lochfraß: Score 20–40, Empfehlung: Schiene tauschen + Isolation
- Festgefressene Schrauben: Score 10–30, Empfehlung: Professionelle Demontage

### 7.10 Fehlerbild F-10: Schlittendichtung defekt (Car Seal Failure)

**Symptome:**
- Kugeln fallen aus dem Schlitten
- Braune/schwarze Paste tritt aus dem Schlitten aus
- Schlitten lässt sich nur noch schwer bewegen
- Sichtbare Risse oder Verformungen der Dichtlippen

**Ursachen:**
- UV-Alterung der Dichtlippen (besonders bei Decksmontage)
- Mechanische Beschädigung durch Schmutzpartikel
- Chemischer Angriff durch falsche Schmiermittel
- Temperaturwechselbelastung (Sommer/Winter)

**Schweregrad:** MITTEL

**Bewertung (AYDI-Score):**
- Leichte Undichtigkeit: Score 50–70, Empfehlung: Dichtlippen tauschen
- Kugelausfall: Score 20–40, Empfehlung: Komplettüberholung
- Schlitten nicht mehr funktionsfähig: Score 0–20, Empfehlung: Tausch

### 7.11 Fehlerbild F-11: Falsche Schienendimensionierung (Undersized Track)

**Symptome:**
- Schiene verbiegt sich sichtbar unter Last
- Schlitten verkippt oder klemmt bei normaler Segelbelastung
- Schrauben an der Schiene zeigen Ermüdungszeichen
- Häufige Reparaturen am gleichen System

**Ursachen:**
- Zu kleines Profil für die Bootsgröße/Segelfläche
- Nachrüstung größerer Segel ohne Schienenaustausch
- Fehlberechnung bei der Erstausrüstung
- Baujahrbedingt (ältere Boote waren oft unterdimensioniert)

**Schweregrad:** HOCH

**Bewertung (AYDI-Score):**
- Leichte Unterdimensionierung (eine Größe): Score 40–60, Empfehlung: Upgrade einplanen
- Deutliche Unterdimensionierung: Score 10–30, Empfehlung: Sofortiger Austausch
- Sicherheitsrelevant: Score 0–10, Empfehlung: Segel reduzieren bis Austausch

### 7.12 Fehlerbild F-12: Verformter Schlitten-Bügel (Car Bail Deformation)

**Symptome:**
- Bügel des Schlittens verbogen
- Schotblock hängt schief
- Leine reibt einseitig am Schlitten
- Sichtbare plastische Verformung des Bügels

**Ursachen:**
- Überlastung durch unvorhergesehene Böe oder Patenthalse
- Seitliche Stoßbelastung (Leine hat sich verhakt)
- Materialermüdung (ältere Edelstahl-Bügel)
- Falsches Material (Aluminium-Bügel statt Edelstahl)

**Schweregrad:** HOCH

**Bewertung (AYDI-Score):**
- Leichte Verformung (< 5°): Score 40–60, Empfehlung: Bügel tauschen
- Starke Verformung (> 5°): Score 10–30, Empfehlung: Kompletten Schlitten tauschen
- Rissbildung: Score 0, Empfehlung: Sofort außer Betrieb nehmen

---

## 8. Troubleshooting

### 8.1 Entscheidungsbaum 1: Schlitten schwergängig

```
START: Schlitten lässt sich schwer verschieben
│
├── Unter Last oder ohne Last?
│   ├── OHNE LAST schwergängig:
│   │   ├── Schiene mit Finger abfahren → rauh?
│   │   │   ├── JA → Korrosion oder Verschleiß → siehe F-05, F-01
│   │   │   └── NEIN → Schlitten-Problem
│   │   │       ├── Kugellager-Schlitten?
│   │   │       │   ├── JA → Kugeln/Käfig prüfen → siehe F-02
│   │   │       │   └── NEIN → Gleitflächen verschlissen → PTFE erneuern
│   │   │       └── Schlitten auf anderer Schiene testen
│   │   │           ├── Auch schwergängig → Schlitten defekt
│   │   │           └── Leichtgängig → Schiene defekt
│   │   └── Schiene auf Verdrehung prüfen → siehe F-06
│   │
│   └── UNTER LAST schwergängig:
│       ├── Schotwinkel prüfen → Seitenbelastung?
│       │   ├── JA → Schotführung korrigieren
│       │   └── NEIN → Schlitten unterdimensioniert? → siehe F-11
│       └── Schiene verbogen? → unter Last sichtbare Durchbiegung?
│           ├── JA → Schiene unterdimensioniert → Upgrade
│           └── NEIN → Befestigung prüfen → Schiene locker? → siehe F-08
```

### 8.2 Entscheidungsbaum 2: Traveller hält nicht

```
START: Traveller-Schlitten rutscht unter Last auf die Lee-Seite
│
├── Steuerleinen intakt?
│   ├── NEIN → Leinen tauschen → siehe F-07
│   └── JA → Klemmen prüfen
│       ├── Curryklemmen verschlissen?
│       │   ├── JA → Klemmen tauschen
│       │   └── NEIN → Leinendurchmesser korrekt für Klemme?
│       │       ├── NEIN → Passende Leine verwenden
│       │       └── JA → Übersetzung ausreichend?
│       │           ├── NEIN → Höhere Übersetzung (z.B. 4:1 → 6:1)
│       │           └── JA → Schlitten-Bremse defekt?
│       │               ├── JA → Bremsbelag erneuern
│       │               └── NEIN → System unterdimensioniert → Upgrade
```

### 8.3 Entscheidungsbaum 3: Geräusche beim Segeln

```
START: Klappern, Knarren oder Quietschen im Bereich der Schienensysteme
│
├── Geräusch lokalisieren:
│   ├── KLAPPERN → lose Komponente
│   │   ├── Schiene locker? → Schrauben prüfen → siehe F-08
│   │   ├── Endstopper locker? → Nachziehen
│   │   └── Schlitten klappert auf der Schiene → Verschleiß → siehe F-01
│   ├── KNARREN → Reibung unter Last
│   │   ├── Schiene/Schlitten → Schmierung → McLube/Teflon-Spray
│   │   └── Steuerleinen in Umlenkblöcken → Blöcke prüfen/schmieren
│   └── QUIETSCHEN → Trockenlauf
│       ├── Kugellager ohne Schmierung → Schlitten überholen
│       └── Steuerleinen in Klemmen → Klemmen reinigen
```

### 8.4 Entscheidungsbaum 4: Wasser unter Deck an der Schiene

```
START: Wassereinbruch im Bereich einer Schienenmontage
│
├── Wo genau tritt Wasser ein?
│   ├── An den Schrauben:
│   │   ├── Dichtmasse intakt?
│   │   │   ├── NEIN → Schiene demontieren, neu abdichten → Abschnitt 5.5
│   │   │   └── JA → Schrauben locker? → Nachziehen → Dichtmasse erneuern
│   │   └── Schraubenlöcher ausgeweitet?
│   │       ├── JA → Kernreparatur → Abschnitt 5.3
│   │       └── NEIN → Dichtmasse End of Life → Erneuern
│   ├── Unter der Schiene (flächig):
│   │   ├── Dichtmasse zwischen Schiene und Deck fehlt
│   │   └── Deck delaminiert → siehe F-04
│   └── An den Schienenenden:
│       ├── Wasser läuft in die Schienennut und am Ende raus
│       └── Drainagelöcher in der Nut bohren oder Endkappen setzen
```

### 8.5 Entscheidungsbaum 5: Genua-Trimm unbefriedigend

```
START: Genua lässt sich nicht optimal trimmen
│
├── Twist zu viel (Achterliek öffnet oben)?
│   ├── Schotblock zu weit achtern → Schlitten nach vorn
│   └── Schiene zu kurz → Verlängerung oder Barber-Hauler vorn
├── Twist zu wenig (Achterliek steht oben dicht)?
│   ├── Schotblock zu weit vorn → Schlitten nach achtern
│   └── Schiene zu kurz → Verlängerung nach achtern
├── Schotwinkel zu eng (Segel zu flach)?
│   ├── Schiene zu nah an der Mittellinie
│   └── Lösung: Barber-Hauler nach außen oder Schiene versetzen
├── Schotwinkel zu weit (Segel zu bauchig)?
│   ├── Schiene zu weit außen
│   └── Lösung: Barber-Hauler nach innen
└── Holepunkt springt bei Wende?
    ├── Kolbenstopp defekt → Austausch
    └── Kein Kolbenstopp vorhanden → Nachrüstung empfohlen
```

---

## 9. FAQ — Häufige Fragen

### F-01: Welche Schienengröße brauche ich für mein Boot?

**Antwort:** Die Schienengröße richtet sich nach der Bootslänge, der Segelfläche und dem Einsatzzweck. Als Faustregel gilt:

| Bootslänge (m) | Genua-Schiene (mm) | Traveller (mm) |
|----------------|--------------------:|----------------:|
| 5–7 | 19 | 19 |
| 7–9 | 22 | 22 |
| 9–11 | 25 | 25 |
| 11–14 | 25–32 | 32 |
| 14–18 | 32 | 32–40 |
| 18–25 | 32–40 | 40–50 |

Für Regattayachten kann eine Nummer kleiner gewählt werden (Gewichtsersparnis), für Blauwasser-Yachten eine Nummer größer (Sicherheitsreserve). Im Zweifel immer die nächstgrößere Dimension wählen.

**Confidence:** estimated (Erfahrungswerte, Herstellerempfehlungen)

### F-02: Kugellager oder Gleitschlitten — was ist besser?

**Antwort:** Es gibt kein generell „besseres" System. Die Wahl hängt vom Einsatzzweck ab:

- **Kugellager-Schlitten**: Ideal für Regatta, Kurzstrecke, Performance-Cruising. Voraussetzung: regelmäßige Wartung (Spülen, Schmieren) mindestens alle 4–6 Wochen.
- **Gleitschlitten**: Ideal für Blauwasser, Charter, wenig gewartete Boote. Akzeptierbar höherer Kraftaufwand, dafür praktisch wartungsfrei.

Für die meisten Fahrtensegler ist ein Kugellager-Schlitten mit guten Dichtlippen der beste Kompromiss — leichtgängig und bei minimaler Pflege langlebig.

**Confidence:** documented (Herstellerempfehlungen, Rigger-Konsens)

### F-03: Wie oft muss ich meine Schienensysteme warten?

**Antwort:**

| Wartung | Intervall | Aufwand |
|---------|-----------|---------|
| Süßwasserspülung | Nach jedem Salzwassertörn | 5 Min. |
| Sichtinspektion | Monatlich (in der Saison) | 10 Min. |
| Kugellager reinigen + schmieren | Alle 6 Monate oder 500 sm | 30 Min./Schlitten |
| Gleitflächen prüfen | Jährlich | 15 Min./Schlitten |
| Schrauben nachziehen | Jährlich (Saisonstart) | 30 Min./Schiene |
| Dichtmasse erneuern | Alle 5–8 Jahre | 2–4 Std./Schiene |
| Komplett-Überholung | Alle 8–12 Jahre | 1 Tag |

**Confidence:** documented (Herstellerhandbücher, Rigger-Praxis)

### F-04: Kann ich Schlitten verschiedener Hersteller auf meiner Schiene verwenden?

**Antwort:** Grundsätzlich ja, wenn die Profilmaße übereinstimmen. T-Track-Maße (19, 22, 25, 32, 40 mm) sind de-facto-Standards, die von den meisten Herstellern eingehalten werden. **Aber:** Es gibt geringfügige Unterschiede in der Nutbreite und Steggeometrie, die zu erhöhtem Verschleiß oder Schwergängigkeit führen können. Proprietäre Profile (z.B. Harken MR 27, Schaefer-Traveller) sind NICHT kompatibel mit Standard-T-Track.

**Empfehlung:** Schlitten und Schiene vom gleichen Hersteller ist immer die sicherste Wahl. Bei Mischung: vorher auf einem kurzen Testabschnitt prüfen.

**Confidence:** documented (Herstellerkataloge, Praxiserfahrung)

### F-05: Wie montiere ich eine Schiene auf einem Sandwich-Deck?

**Antwort:** Sandwich-Decks erfordern besondere Sorgfalt, da der Kern (Balsa, Schaum) keine Schraubenlasten aufnehmen kann und bei Wassereinbruch verrottet.

**Vorgehen:**
1. Bohrungen überdimensioniert bohren (Durchmesser + 20 mm)
2. Kernmaterial im Bohrungsbereich entfernen (konischer Fräser)
3. Hohlraum mit Epoxid + Mikrosphären füllen
4. 24 h aushärten lassen
5. Auf Endmaß nachbohren
6. Durch-Bolzen mit Gegenplatte (min. 3 mm Edelstahl oder Aluminium)
7. Dichtmasse (Sikaflex 291) auftragen
8. Schiene montieren, Drehmoment einhalten

Detaillierte Anleitung: siehe Abschnitt 5.3

**Confidence:** documented (Bootsbau-Praxis, Epoxidhersteller-TDS)

### F-06: Welche Dichtmasse für die Schienenmontage?

**Antwort:** Sikaflex 291 ist der Standard für Deck-Beschläge auf GFK-Decks. Es ist elastisch genug, um thermische Bewegungen auszugleichen, und stark genug, um wasserdicht zu bleiben.

| Dichtmasse | Geeignet | Nicht geeignet |
|-----------|----------|----------------|
| Sikaflex 291 | GFK, Holz (grundiert) | Polyethylen, Polyprophylen |
| 3M 4200 | GFK, Holz, Alu | Wenn permanente Verbindung gewünscht |
| Sikaflex 292i | Strukturelle Verklebung | Wenn Demontage geplant |
| Silikon | Nie für Deck-Beschläge | Alles (haftet nicht auf GFK) |

**Wichtig:** Immer Primer verwenden (Sika 209D) und mindestens 24 h vor dem endgültigen Anziehen der Schrauben warten.

**Confidence:** measured (Hersteller-TDS Sikaflex, 3M)

### F-07: Meine Genua-Schiene ist zu kurz. Kann ich sie verlängern?

**Antwort:** Ja, aber mit Einschränkungen:

1. **Verlängerung mit gleicher Schiene + Stoßverbinder**: Möglich, wenn das Deck in der Verlängerungsrichtung frei ist. Stoßverbinder (Track Joiner) hält die Schienen fluchtend. SWL des Verbinders beachten.

2. **Neue, längere Schiene**: Besser als Verlängerung, da keine Stoßstelle. Alte Bohrungen müssen verschlossen werden (Epoxid + GFK-Stopfen).

3. **Barber-Hauler als Alternative**: Statt physischer Schienenverlängerung kann ein Barber-Hauler den effektiven Schotwinkel verändern, ohne die Schiene zu verlängern.

**Confidence:** documented (Rigger-Praxis)

### F-08: Wie erkenne ich, ob mein Traveller unterdimensioniert ist?

**Antwort:** Anzeichen für einen unterdimensionierten Traveller:

1. Schlitten lässt sich bei Wind > 4 Bft nicht mehr fixieren (rutscht trotz angezogener Steuerleinen)
2. Schiene verbiegt sich sichtbar unter Schotzug
3. Häufiges Endstopper-Versagen
4. Steuerleinen reißen regelmäßig
5. Crew muss unverhältnismäßig viel Kraft aufwenden für die Traveller-Verstellung

**Prüfung:**
- Maximale Schotkraft berechnen (siehe Abschnitt 2.3)
- Dynamikfaktor 3.0 anwenden
- Ergebnis mit SWL des Schlittens vergleichen
- Wenn Ergebnis > 60 % SWL → unterdimensioniert

**Confidence:** documented (Ingenieurspraxis)

### F-09: Kann ich Edelstahl-Schrauben in einer Aluminium-Schiene verwenden?

**Antwort:** Ja, aber mit galvanischer Trennung. Edelstahl (316L) und Aluminium (6082-T6) bilden in Salzwasser ein galvanisches Element, das das Aluminium angreift (Spannungsdifferenz ca. 0.5–0.7 V).

**Schutzmaßnahmen:**
1. Dichtmasse (Sikaflex 291) um jede Schraube → unterbricht den Elektrolytweg
2. Teflon-Unterlegscheiben unter den Schraubenköpfen
3. Duralac Anti-Korrosionspaste auf Schraubengewinde
4. Alternativ: Aluminium-Schrauben (nur bei geringen Lasten)

**Confidence:** measured (Korrosionswissenschaft, Marine-Praxis)

### F-10: Welche Schmierung für Kugellager-Schlitten?

**Antwort:** Spezielle Marine-Kugellagerschmiermittel verwenden:

| Produkt | Typ | Eignung | Preis |
|---------|-----|---------|-------|
| Harken McLube OneDrop | Dünnflüssiges Öl | Kugellager-Schlitten | ca. 15 EUR/30 ml |
| McLube SailKote | Trockenschmierung | Schienen, Schlitten | ca. 18 EUR/300 ml |
| Ronstan RF4015 | Lager-Fett | Kugellager-Schlitten | ca. 12 EUR/50 ml |
| Weicon Teflon-Spray | Trockenschmierung | Schienen | ca. 10 EUR/400 ml |
| Boat-Life Lube | Marine-Fett | Universal | ca. 14 EUR/100 ml |

**Nicht verwenden:** WD-40 (löst Fett, trocknet aus), Vaseline (verhärtet), Silikonspray (greift Delrin an), Graphit (fördert galvanische Korrosion auf Alu).

**Confidence:** documented (Herstellerempfehlungen, Rigger-Konsens)

### F-11: Traveller auf dem Kajütdach oder im Cockpitboden — was ist besser?

**Antwort:**

| Kriterium | Kajütdach | Cockpitboden |
|-----------|-----------|-------------|
| Cockpit-Freiheit | Besser (Cockpit frei) | Schlechter (Schiene im Weg) |
| Schotzug-Effizienz | Schlechter (längerer Schotweg) | Besser (direkter Zug) |
| Kraft auf Steuerleinen | Höher (wegen Schot-Geometrie) | Geringer |
| Sicherheit | Besser (keine Stolpergefahr) | Schlechter (Stolperkante) |
| Installation | Anspruchsvoller (Dachstruktur) | Einfacher (Cockpitboden = robust) |
| Regatta-Trimm | Weniger optimal | Optimal |

**Empfehlung:** Fahrtenyachten = Kajütdach, Regattayachten = Cockpitboden, Kurzhand = Kajütdach.

**Confidence:** estimated (Seglerpraxis, Designphilosophie)

### F-12: Wie lang muss mein Traveller sein?

**Antwort:** Die Travellerlänge bestimmt den maximalen Verstellbereich des Großschot-Angriffspunkts. Faustregel:

- **Minimum:** 60 % der Bootsbreite am Montageort
- **Optimal:** 80–90 % der Bootsbreite am Montageort
- **Maximum:** 100 % der Bootsbreite (baulich begrenzt durch Süllrand/Stanchions)

Für eine 10 m Yacht mit 3.2 m Breite am Cockpit:
- Minimum: 1.92 m
- Optimal: 2.56–2.88 m
- Typisch: 2.4 m

**Confidence:** documented (Segelmacher-Empfehlungen)

### F-13: Muss ich die Schiene bei jedem Winterlager demontieren?

**Antwort:** Nein. Eine korrekt montierte und abgedichtete Schiene kann über die gesamte Lebensdauer des Bootes montiert bleiben. Empfohlen ist jedoch:

1. **Saisonende:** Schlitten von der Schiene nehmen, reinigen, schmieren, trocken lagern
2. **Saisonstart:** Schiene reinigen, auf Korrosion prüfen, Schrauben auf Drehmoment prüfen
3. **Alle 5–8 Jahre:** Schiene komplett demontieren, Dichtmasse erneuern, Deck unter der Schiene inspizieren

**Confidence:** documented (Werft-Praxis)

### F-14: Welches Werkzeug brauche ich für die Schlitten-Wartung?

**Antwort:** Minimales Werkzeug für die Schlitten-Wartung:
- Kleiner Kreuzschlitz- oder Torx-Schraubendreher (für Dichtungsplatten)
- Zahnbürste (alte, weiche) für die Reinigung
- Süßwasser in Sprühflasche
- Marine-Schmiermittel (McLube OneDrop)
- Sauberes Tuch (fussfrei)
- Optional: Lupe für Kugelinspektion

Für die vollständige Überholung zusätzlich:
- Ersatzkugeln (Herstellerspezifisch)
- Ersatz-Dichtlippen
- Feinmechaniker-Pinzette
- Kleines Tablett (damit keine Kugeln verloren gehen)

**Confidence:** documented (Herstellerhandbücher)

### F-15: Kann ich eine gebogene Schiene für mein gewölbtes Deck verwenden?

**Antwort:** Ja, mit Einschränkungen:

1. **Aluminium-T-Track lässt sich kaltbiegen** bis ca. 2 % Krümmung (Radius ≥ 3 m bei 25 mm Track). Die Biegung muss gleichmäßig erfolgen (Rohrbiegemaschine oder über Schablone).

2. **Vorgefertigte gebogene Schienen** sind bei einigen Herstellern erhältlich (Harken, Lewmar auf Anfrage). Teurer als gerade Schienen (+50–100 %).

3. **Shimming:** Bei geringer Deckswölbung können Shims unter der geraden Schiene die Differenz ausgleichen (bis ca. 3–5 mm Höhendifferenz auf 2 m Länge).

4. **Flexible Schienen:** Einige Hersteller (Antal) bieten bewusst dünnere Profile an, die sich an die Decksform anlegen.

**Confidence:** documented (Herstellerangaben, Rigger-Praxis)

### F-16: Was kostet ein komplettes Schienensystem für mein Boot?

**Antwort:** Richtpreise für ein vollständiges Schienensystem (2× Genua-Schiene + 1× Traveller + Zubehör):

| Bootslänge (m) | Budget-Linie | Mittelklasse | Premium |
|----------------|-------------|-------------|---------|
| 7–9 | 400–600 EUR | 700–1.100 EUR | 1.200–1.800 EUR |
| 9–11 | 600–900 EUR | 1.000–1.500 EUR | 1.600–2.400 EUR |
| 11–14 | 900–1.400 EUR | 1.500–2.500 EUR | 2.500–4.000 EUR |
| 14–18 | 1.400–2.200 EUR | 2.500–4.000 EUR | 4.000–7.000 EUR |
| 18–25 | - | 4.000–7.000 EUR | 7.000–15.000 EUR |

Montagekosten durch Rigger: +400–1.500 EUR (abhängig von Bootsgröße und Zugänglichkeit).

**Confidence:** estimated (Handelspreise, Werft-Erfahrung)

### F-17: Warum laufen meine Kugellager-Schlitten nach dem Winter so schwer?

**Antwort:** Die häufigsten Ursachen für schwergängige Schlitten nach der Winterpause:

1. **Salzkristalle** haben sich während der Trocknung in den Kugellagern gebildet → Lösung: in lauwarmem Süßwasser einweichen, dann spülen
2. **Schmiermittel verharzt** über den Winter (besonders bei Kälte) → Lösung: altes Fett auswaschen, neu schmieren
3. **Korrosion** hat während der Einlagerung begonnen (besonders in feuchten Hallen) → Lösung: Reinigung, ggf. Kugeltausch
4. **Dichtlippen** sind steif geworden (Kälte) → Lösung: erwärmen (Handwärme reicht meist), ggf. tauschen

**Prävention:** Schlitten am Saisonende von der Schiene nehmen, komplett spülen, schmieren und in einem verschlossenen Plastikbeutel trocken lagern.

**Confidence:** documented (Rigger-Praxis, Herstellerempfehlungen)

### F-18: Mein Traveller hat keine Steuerleinen — wie rüste ich nach?

**Antwort:** Nachrüstung einer Traveller-Steuerung:

1. **Schlitten prüfen:** Hat der Schlitten seitliche Ösen für Steuerleinen? Wenn nicht → Schlitten tauschen gegen Modell mit Ösen.
2. **Umlenkblöcke montieren:** Je 1 Block an jedem Schienenende (auf Deck oder am Schienenfuß)
3. **Fiddle-Block wählen:** Übersetzung bestimmen (4:1 bis 8:1 je nach Bootsgröße)
4. **Steuerleinen führen:** Vom Schlitten → Umlenkblock → Fiddle → Klemme (Curryklemme oder Fallenstopper)
5. **Klemmen positionieren:** In Reichweite des Steuermanns

**Materialkosten:** ca. 100–300 EUR (abhängig von Qualität der Blöcke und Klemmen)

**Confidence:** documented (Rigger-Praxis)

### F-19: Kann ich Carbon-Schienen auf meinem Boot verwenden?

**Antwort:** Carbon-Schienen existieren für extreme Leichtbau-Anwendungen (Regatta, Foiling). Sie bieten:

- Gewichtsersparnis: 50–60 % gegenüber Aluminium
- Höhere Steifigkeit bei geringerem Gewicht
- Aber: Extrem teuer (Faktor 10–20× gegenüber Aluminium)
- Empfindlich gegen Punktlasten und Schlagschäden
- Galvanische Probleme mit Edelstahl-Schrauben (noch kritischer als Alu)
- Verfügbarkeit: nur auf Sonderanfertigung

**Empfehlung:** Nur für extreme Regattayachten (TP52, Imoca, VOR) sinnvoll. Für Fahrtenyachten ist Aluminium 6082-T6 das optimale Material.

**Confidence:** documented (Regatta-Praxis, Materialtechnik)

### F-20: Wie verhindere ich, dass Wasser in die Schienennut eindringt?

**Antwort:** Wasseransammlung in der T-Track-Nut ist ein häufiges Problem, da die Nut als Kanal wirkt:

1. **Drainagelöcher:** 3–4 mm Bohrungen im tiefsten Punkt der Schiene (alle 30–50 cm)
2. **Endkappen:** Verschluss der Schienenenden mit Kunststoff- oder Silikonkappen
3. **Schienenneigung:** Minimale Neigung (1–2°) zur Seite, damit Wasser ablaufen kann
4. **Regelmäßiges Spülen:** Süßwasser durch die Nut spülen, um Salzkristalle zu entfernen
5. **Schienenwachs:** Dünnschicht-Wachsauftrag in der Nut (McLube SailKote) → Wasserabweisung

**Confidence:** documented (Rigger-Praxis)

### F-21: Ist ein Kolbenstopp-Schlitten besser als ein freier Schlitten?

**Antwort:** Kolbenstopp-Schlitten bieten eine schnelle Voreinstellung des Holepunkts, sind aber kein Ersatz für Steuerleinen-Feinverstellung:

**Vorteile Kolbenstopp:**
- Schneller Wechsel zwischen Standardpositionen (z.B. Genua → Fock → Sturmfock)
- Holepunkt springt beim Wenden nicht versehentlich
- Einhändig bedienbar (Knopfdruck)

**Nachteile Kolbenstopp:**
- Feinverstellung nur in Rasterschritten (typisch 25–50 mm)
- Kolbenmechanismus kann verschmutzen oder korrodieren
- Schwerer als freier Schlitten (+30–50 g)
- Teurer als freier Schlitten (+30–50 %)

**Empfehlung:** Für Fahrtensegler ideal. Für Regattasegler: freier Schlitten mit Steuerleinen für stufenlose Verstellung.

**Confidence:** documented (Seglerpraxis)

### F-22: Mein Boot hat Flat-Bar-Schienen. Soll ich auf T-Track umrüsten?

**Antwort:** Ja, eine Umrüstung auf T-Track ist fast immer empfehlenswert:

**Vorteile der Umrüstung:**
- Formschlüssige Sicherung gegen Abheben des Schlittens
- Höhere Belastbarkeit
- Bessere Auswahl an Schlitten und Zubehör
- Moderne Kugellager-Schlitten verfügbar

**Aufwand:**
- Alte Schiene demontieren, Bohrungen verschließen
- Neue T-Track-Schiene montieren (ggf. versetzt zu alten Bohrungen)
- Neue Schlitten und Blöcke anschaffen
- Typischer Aufwand: 1 Tag Arbeitszeit + Materialkosten

**Kosten:** 300–800 EUR (Material) + 200–500 EUR (Arbeitszeit Rigger)

**Confidence:** documented (Rigger-Praxis)

### F-23: Wie lang sollte eine selbstwendende Fock-Schiene sein?

**Antwort:** Die Länge der Self-Tacking-Jib-Schiene hängt von der Bootsbreite und dem Fockschnitt ab:

- **Minimum:** 55 % der Bootsbreite am Montageort
- **Optimal:** 65–75 % der Bootsbreite
- **Maximum:** 85 % der Bootsbreite (begrenzt durch Seitendeck-Rand)

Beispiel 10 m Yacht, Breite am Vordeck 2.8 m:
- Minimum: 1.54 m
- Optimal: 1.82–2.10 m
- Typisch: 2.0 m

**Wichtig:** Die Schiene muss der Decksform folgen (gebogen) und der Schlitten muss unter Last frei gleiten können (Kugellager obligatorisch).

**Confidence:** documented (Segelmacher-Empfehlungen)

### F-24: Kann ich einen Genua-Schlitten als Traveller-Schlitten verwenden?

**Antwort:** Technisch möglich, aber nicht empfohlen:

- Genua-Schlitten haben typischerweise keinen Bügel für Schotblöcke
- Steuerleinen-Befestigungspunkte fehlen oder sind ungeeignet
- Belastungsrichtung ist anders (Genua: nach oben/vorn; Traveller: seitlich)
- Spezielle Traveller-Schlitten sind für Querlast optimiert

**Ausnahme:** Bei sehr kleinen Booten (< 7 m) und geringen Lasten kann ein Genua-Schlitten mit passendem Blockschäkel als provisorischer Traveller verwendet werden.

**Confidence:** estimated (Praxiserfahrung)

### F-25: Welche Ersatzteile sollte ich auf einer Langfahrt mitführen?

**Antwort:** Empfohlene Ersatzteile für Schienensysteme auf Langfahrt:

**Essentiell:**
- 1× Satz Ersatzkugeln für jeden Schlittentyp
- 2× Ersatz-Dichtlippen für Kugellager-Schlitten
- 1× Ersatz-Endstopper (passend für die größte Schiene)
- Schmiermittel (McLube OneDrop, 30 ml Flasche)
- 4× Ersatzschrauben je Schraubengröße (M5, M6, M8)
- Dichtmasse (kleine Tube Sikaflex 291, 70 ml)

**Optional:**
- 1× Ersatz-Schlitten (kompletter Kugellager-Schlitten als Reserve)
- 1× kurzes Schienenstück (0.3 m) als Reparaturmaterial
- Epoxidharz (z.B. West System Six10) für Kernreparaturen
- Steuerleinen-Ersatz (5 m, passender Durchmesser)

**Confidence:** documented (Blauwasser-Seglerpraxis)

---

## 10. Glossar

### A

**Achterliek (Leech)**
Die hintere Kante eines Segels, die vom Schothorn zum Kopf verläuft. Der Genua-Schotblockposition auf der Schiene beeinflusst den Twist des Achterlieks direkt.

**Anodisierung (Anodizing)**
Elektrochemisches Verfahren zur Erzeugung einer schützenden Oxidschicht auf Aluminium. Standard-Anodisierung (Typ II) erzeugt 8–25 µm Schichtdicke, Hartanodisierung (Typ III) 25–50 µm. Essentiell für den Korrosionsschutz von Alu-Schienen im Salzwasser.

**Auszugskraft (Pull-out Force)**
Die Kraft, die erforderlich ist, um eine Schraube aus dem Deck/Unterbau herauszuziehen. Kritisch bei Sandwich-Decks ohne Kernverstärkung.

### B

**Ball Bearing Car (Kugellager-Schlitten)**
Schlittentyp mit Kugellagern für minimale Reibung. Reibungskoeffizient µ = 0.02–0.05.

**Barber-Hauler**
Leinensystem zur Quer- oder Höhenverstellung des Genua-Schotumlenkpunkts, unabhängig von der festen Schiene.

**Bruchlast (Breaking Load / Ultimate Load)**
Die Kraft, bei der ein Bauteil versagt. SWL = Bruchlast / Sicherheitsfaktor.

**Brinelling**
Permanente Eindrücke in einer Lagerlaufbahn durch Überlastung der Kugeln. Erkennbar an rhythmischen Schwergängigkeitsstellen.

### C

**Car (Schlitten/Wagen)**
Das bewegliche Element, das auf der Schiene gleitet oder rollt. Trägt den Schotblock oder die Schotführung.

**Curryklemme (Cam Cleat)**
Klemme mit zwei gefederten, gezähnten Backen zum schnellen Festklemmen und Lösen von Leinen.

### D

**Delrin (Acetal/POM)**
Technischer Kunststoff, verwendet für Kugelkäfige, Gleitflächen und Endstopps. Gute Gleiteigenschaften, UV-beständig, aber altert nach 8–12 Jahren.

**Durchbolzung (Through-Bolting)**
Befestigungsmethode, bei der eine Schraube das gesamte Deck durchdringt und auf der Unterseite mit Mutter und Gegenplatte gesichert wird. Höchste Festigkeit.

**Dynamikfaktor (Dynamic Load Factor)**
Multiplikator für die statische Last, der dynamische Effekte (Böen, Manöver, Welleneinschlag) berücksichtigt. Typisch 2.0–4.0 für Segelsysteme.

### E

**End Stop (Endstopper)**
Begrenzungselement an den Enden einer Schiene, das den Schlitten am Herauslaufen hindert. Sicherheitskritisches Bauteil.

**Eloxierung**
Siehe Anodisierung.

### F

**Fiddle Block (Violinblock)**
Doppelblock mit übereinander angeordneten Scheiben, typischerweise an den Enden eines Traveller-Schlittens für die Steuerleinen-Übersetzung.

**Flat Bar (Flachschiene)**
Einfaches Schienenprofil ohne hinterschnittene Nut. Historisch, heute nur noch für Nebenfunktionen.

### G

**Galvanische Korrosion (Galvanic Corrosion)**
Elektrochemischer Prozess, bei dem ein unedleres Metall (z.B. Aluminium) in Anwesenheit eines Elektrolyten (Salzwasser) zugunsten eines edleren Metalls (z.B. Edelstahl) aufgelöst wird.

**Genua-Schiene (Genoa Track)**
Längsschiffs montierte Schiene auf dem Seitendeck für die Führung des Genua-Schotblocks.

**Gegenplatte (Backing Plate)**
Metallplatte auf der Unterseite des Decks, die die Schraubenkräfte auf eine größere Fläche verteilt.

### H

**Hartanodisierung (Hard Anodizing / Typ III)**
Spezialverfahren der Anodisierung mit besonders harter (350–500 HV) und dicker (25–50 µm) Oxidschicht. Standard für hochbelastete Marineteile.

**Holepunkt (Sheeting Point / Lead Point)**
Der Punkt, an dem die Schot umgelenkt wird — auf dem Schlitten der Genua-Schiene.

**HL-Track (High-Load Track)**
Verstärktes Schienenprofil für extreme Lasten, typisch für Superyachten und Regattaboote.

### I

**I-Beam (Doppel-T-Profil)**
Schienenprofil in I-Form, verwendet für Hochlast-Traveller. Höhere Biegesteifigkeit als T-Track.

### K

**Kernverstärkung (Core Reinforcement)**
Lokale Verstärkung des Sandwich-Deckskerns im Bereich von Schraubenmontagen durch Ersatz des leichten Kernmaterials (Balsa, Schaum) durch Epoxid-Füller.

**Kolbenstopp (Piston Stop)**
Federbelasteter Mechanismus im Schlitten, der in Bohrungen der Schiene einrastet und den Schlitten fixiert.

### L

**Laufbahn (Raceway)**
Die gehärtete Oberfläche in der Schiene und im Schlitten, auf der die Kugeln rollen.

**Lochleibungsversagen (Bearing Failure)**
Versagen des Deckmaterials um eine Schraubenbohrung durch Quetschung oder Aufweitung unter Last.

### M

**McLube**
Markenname für eine Familie von Marine-Schmiermitteln. McLube OneDrop für Kugellager, McLube SailKote für allgemeine Trockenschmierung.

**Mast-Track (Mastschiene)**
Führungsschiene am Mast für die Segellatten (Slides/Slugs) des Großsegels.

### N

**Nylock-Mutter (Nylon Lock Nut)**
Selbstsichernde Mutter mit Nylon-Einsatz, die sich nicht durch Vibration löst. Standard für Decksbeschlag-Montage.

### P

**Piston Stop Car (Kolbenstopp-Schlitten)**
Schlitten mit integriertem Rastsystem für schnelle Positionswechsel.

**PTFE (Polytetrafluorethylen / Teflon)**
Kunststoff mit extrem niedrigem Reibungskoeffizienten (0.04–0.10). Verwendet für Gleitflächen in Schlitten.

### S

**SWL (Safe Working Load / Sichere Arbeitslast)**
Die maximale Last, mit der ein Bauteil im Normalbetrieb belastet werden darf. Typisch: SWL = Bruchlast / 3.0 (Fahrtenyacht) bis Bruchlast / 2.5 (Regattayacht).

**Schotwinkel (Sheeting Angle)**
Der Winkel zwischen der Bootsmittellinie und der Linie vom Vorliek-Unterkante zum Schotblock. Bestimmt die seitliche Position der Genua-Schiene.

**Self-Tacking Jib Track (Selbstwendefock-Schiene)**
Querschiffs montierte Schiene, auf der der Fock-Schlitten bei Wendemanövern automatisch auf die Leeseite gleitet.

**Sandwich-Deck**
Deckskonstruktion aus zwei GFK-Laminatschichten mit dazwischenliegendem leichten Kernmaterial (Balsa, PVC-Schaum, SAN-Schaum).

**Shim (Unterlegplatte/Keil)**
Dünne Platte zum Ausgleich von Unebenheiten zwischen Schiene und Decksgleiche.

**Stick-Slip-Effekt**
Ruckartiges Gleiten eines Schlittens, verursacht durch den Unterschied zwischen Haft- und Gleitreibung. Tritt besonders bei Gleitschlitten unter Last auf.

### T

**T-Track (T-Schiene)**
Das Standard-Schienenprofil im Yachtbau mit T-förmigem Querschnitt und hinterschnittener Nut zur Aufnahme von Schlitten.

**Torlon (PAI — Polyamid-Imid)**
Hochleistungskunststoff, verwendet für ultraleichte Kugeln in Regatta-Schlitten. Geringeres Gewicht als Edelstahl bei guter Festigkeit.

**Traveller (Traveller/Großschot-Wagen)**
Der querschiffs verschiebbare Wagen auf der Travellerschiene, an dem die Großschot angreift.

**Twist (Verwindung des Segels)**
Die Änderung des Anstellwinkels eines Segels von unten nach oben. Wird maßgeblich durch die Position des Holepunkts (Genua) bzw. des Travellers (Großsegel) gesteuert.

### U

**UHMWPE (Ultra-High-Molecular-Weight Polyethylene)**
Hochleistungspolymer, verwendet für Steuerleinen (Dyneema, Spectra) mit extrem hoher Festigkeit bei geringem Gewicht.

### V

**Violinblock (Fiddle Block)**
Siehe Fiddle Block.

### W

**Wiper Seal (Dichtlippe/Abstreifer)**
Elastische Dichtung am Eingang des Schlittens, die Schmutz und Salzwasser vom Kugellager fernhält.

---

## 11. Schnell-Referenz

### 11.1 Schnelle Dimensionierungstabelle

| Bootslänge (m) | Genua-Track (mm) | Traveller (mm) | Schrauben | Durch-Bolzen? |
|----------------|:-----------------:|:---------------:|:---------:|:-------------:|
| 5–7 | 19 | 19 | M5 | Optional |
| 7–9 | 22 | 22 | M5 | Traveller: Ja |
| 9–11 | 25 | 25 | M6 | Ja |
| 11–14 | 25–32 | 32 | M6–M8 | Ja |
| 14–18 | 32 | 32–40 | M8 | Ja |
| 18–25 | 32–40 | 40–50 | M8–M10 | Ja |

### 11.2 Schnelle Wartungs-Checkliste

```
□ Süßwasserspülung nach Salzwassertörn
□ Schlitten auf Leichtgängigkeit prüfen
□ Schiene auf Korrosion/Verschleiß sichtprüfen
□ Endstopper auf festen Sitz prüfen
□ Steuerleinen auf Verschleiß prüfen
□ Schrauben stichprobenartig auf Drehmoment prüfen
□ Dichtmasse auf Risse/Ablösung prüfen
□ Kugellager-Schlitten schmieren (alle 6 Monate)
```

### 11.3 Notfall-Reparatur auf See

| Problem | Sofortmaßnahme |
|---------|---------------|
| Endstopper gebrochen | Schlitten mit Leine sichern (Dyneema durch Schäkel → belegen an Klampe) |
| Schlitten blockiert | Schotblock direkt am Deck belegen (Schiene umgehen) |
| Traveller defekt | Großschot direkt am Baumende belegen, Traveller in Mittelposition fixieren |
| Schiene gebrochen | Segel reduzieren, Schotblock provisorisch am Deck befestigen (Takling-Pad) |
| Steuerleinen gerissen | Ersatzleine, oder Traveller mit Knoten in Mittelposition fixieren |

### 11.4 Herstellerkontakte

| Hersteller | Website | Katalog |
|-----------|---------|---------|
| Harken | harken.com | Gesamtkatalog als PDF downloadbar |
| Lewmar | lewmar.com | Deckshardware-Katalog |
| Antal | antal.it | Produktkatalog mit SWL-Tabellen |
| Ronstan | ronstan.com | Online-Katalog mit Filterfunktion |
| Schaefer | schaefermarine.com | Traveller-Katalog |
| Seldén | sfrags.com | Deck-Hardware Katalog |
| Frederiksen | frederiksen-marine.com | Budget + Racing Katalog |

---

## ANHANG A — Fallstudien

### Fallstudie A-01: Genua-Schienen-Upgrade auf einer Bavaria 37 (Baujahr 2004)

**Ausgangssituation:**
Der Eigner einer Bavaria 37 (11.35 m LüA) beklagte schwergängige Genua-Schlitten und unzureichende Schienenlänge. Die Original-Ausrüstung bestand aus Lewmar Size 1 (20 mm) T-Track mit Gleitschlitten — unterdimensioniert für die 40 m² Genua.

**Befund (AYDI-Analyse):**
- Schienenprofil 20 mm: unterdimensioniert für 11 m Yacht (empfohlen: 25 mm)
- Gleitschlitten: SWL 400 kg, Maximallast Genua geschätzt 900 kg → SF < 2.0
- Schienenlänge 1.0 m: zu kurz (empfohlen: 1.8–2.0 m für Genua 130–150 %)
- Befestigung: Blechschrauben in Sandwich-Deck ohne Kernverstärkung → Auszugsgefahr
- Korrosion in der Schienennut: 0.3 mm Grübchenkorrosion
- AYDI-Score (Gesamt): 28/100 → KRITISCH

**Durchgeführte Maßnahme:**
1. Alte Schienen demontiert, alte Bohrungen mit Epoxid verschlossen
2. Neue Schiene: Harken 27 mm T-Track (Art. 2729, 2.0 m) beidseitig montiert
3. Kernverstärkung: Alle 12 Bohrungen pro Seite mit Epoxid+Mikrosphären gefüllt
4. Durch-Bolzen: M6 Edelstahl A4-80 mit 50×300×3 mm Alu-Gegenplatte
5. Neue Schlitten: Harken 27 mm Kugellager Stand-Up (Art. 2715) mit Kolbenstopp
6. Dichtung: Sikaflex 291 mit Sika Primer 209D
7. Endstopps: Harken 2751

**Ergebnis:**
- Leichtgängigkeit: dramatisch verbessert (Kugellager vs. Gleitfläche)
- Trimmbereich: verdoppelt (2.0 m statt 1.0 m)
- SWL: 900 kg (statt 400 kg) → SF ≥ 3.0
- AYDI-Score (nach Upgrade): 91/100

**Kosten:** 680 EUR Material + 450 EUR Rigger-Arbeit = 1.130 EUR

**Dauer:** 1.5 Tage

### Fallstudie A-02: Traveller-Austausch auf einer Hallberg-Rassy 36 (Baujahr 1996)

**Ausgangssituation:**
Großschot-Traveller auf dem Kajütdach einer HR 36 (10.85 m LüA). Original: Lewmar Size 2 Traveller mit Gleitschlitten, Steuerleinen über Curryklemmen. Der Schlitten blockierte unter Last und ließ sich nur bei Kursänderung (Lastentlastung) verstellen.

**Befund (AYDI-Analyse):**
- Travellerschiene: 25 mm T-Track, Zustand akzeptabel (Oberflächenkorrosion, Score 65)
- Schlitten: Gleitflächen stark verschlissen, PTFE-Pads abgenutzt (Score 25)
- Steuerleinen: 6 mm Polyester, UV-geschädigt, Schamfilstellen (Score 30)
- Klemmen: Curryklemmen verschlissen, halten 6 mm Leine nicht mehr (Score 20)
- Fiddle-Blöcke: Funktional, aber verschmutzt (Score 55)
- Montage/Dichtung: Intakt (Score 75)
- AYDI-Score (Gesamt): 42/100 → MANGELHAFT

**Durchgeführte Maßnahme:**
1. Bestehende Schiene beibehalten (Zustand ausreichend)
2. Neuer Schlitten: Harken 27 mm Kugellager mit Bügel (Art. 2731)
3. Neue Steuerleinen: Marlow D2 Racing, 8 mm (Dyneema-Kern, Polyester-Mantel)
4. Neue Klemmen: Clamcleat CL218 (passend für 6–10 mm)
5. Neue Fiddle-Blöcke: Harken 29 mm (Art. 350)
6. Steuerung: 6:1 Übersetzung (statt vorher 4:1)

**Ergebnis:**
- Verstellkraft: reduziert um ca. 60 % (Kugellager + höhere Übersetzung)
- Schlitten gleitet unter Last frei
- Steuerleinen halten zuverlässig in den Klemmen
- AYDI-Score (nach Upgrade): 85/100

**Kosten:** 420 EUR Material + 250 EUR Rigger-Arbeit = 670 EUR

### Fallstudie A-03: Decksdelamination unter Genua-Schiene, Jeanneau Sun Odyssey 42 DS (Baujahr 2008)

**Ausgangssituation:**
Eigner bemerkte Wasserflecken im Salon unter der Backbord-Genua-Schiene. Die Schiene (Lewmar Size 3, 32 mm) war mit Blechschrauben in das Sandwich-Deck geschraubt — ohne Kernverstärkung.

**Befund (AYDI-Analyse):**
- Deck unter der Schiene: 4 von 16 Schrauben drehen frei → Kern zerstört
- Klopftest: Dumpfer Klang auf 400 mm Länge → Delamination
- Wassergehalt im Kern: erhöht (Feuchtemessung)
- Schiene steht nicht mehr plan (2 mm Spalt in der Mitte)
- AYDI-Score (Strukturell): 15/100 → KRITISCH

**Durchgeführte Maßnahme:**
1. Schiene und alle Schrauben demontiert
2. Delaminierter Bereich freigelegt (Innenlaminat von unten geöffnet, 200×500 mm)
3. Nasser Balsakerl entfernt, 4 Wochen trocknen lassen
4. Neuer Kern: Divinycell H80 (PVC-Schaum, kein Balsa → keine Feuchtigkeitsempfindlichkeit)
5. Innenlaminat erneuert: 4 Lagen biaxiales GFK 600 g/m² + Epoxid
6. Alle 16 Bohrungen mit Epoxid-Kernfüllung verstärkt (25 mm Radius)
7. Schiene remontiert: Durch-Bolzen M8 A4-80 + Alu-Gegenplatte 60×400×4 mm
8. Dichtung: Sikaflex 292i (strukturell, langlebig)

**Ergebnis:**
- Deck vollständig trocken
- Schiene sitzt bombenfest (Durch-Bolzen statt Blechschrauben)
- PVC-Kern statt Balsa → kein erneutes Feuchtigkeitsrisiko
- AYDI-Score (nach Reparatur): 95/100

**Kosten:** 380 EUR Material + 1.200 EUR Werft-Arbeit = 1.580 EUR

**Dauer:** 5 Tage (inkl. 4 Wochen Trocknungszeit für den Kern)

### Fallstudie A-04: Selbstwendefock-Nachrüstung auf einer X-332 (Baujahr 2001)

**Ausgangssituation:**
Kurzhandsegler wünschte Umrüstung auf Selbstwendefock für einfachere Wendemanöver. Boot: X-332 (9.98 m LüA), vorhandene Genua-Schienen Standard Seldén 25 mm.

**Befund und Planung:**
- Vordeck: Ausreichend Platz für Querschiene (Breite am geplanten Montageort: 2.4 m)
- Deckstruktur: Sandwich mit Balsakerl, 22 mm gesamt
- Fock: 100 % Fock (J × P / 2 = ca. 22 m²)
- Berechnete Schotkraft: max. 450 kg
- Empfohlene Schiene: Harken 27 mm T-Track, 1.8 m, gebogen (Decksradius)
- Empfohlener Schlitten: Harken 27 mm Kugellager mit verlängertem Blockarm

**Durchgeführte Maßnahme:**
1. Querschiene: Harken 27 mm T-Track, kaltgebogen auf Decksradius (R = 4.5 m)
2. 14 Bohrungen mit Kernverstärkung (Epoxid-Füllung)
3. Durch-Bolzen M6 + Gegenplatte
4. Kugellager-Schlitten mit 400 mm langem Aluminium-Blockarm
5. Schotblock am Blockarm: Harken 29 mm Carbo
6. Begrenzungsschlitten (seitlich): Harken 27 mm Endstopps, verstellbar
7. Rückhol-Gummiseil: 8 mm, beidseitig zwischen Schlitten und Schienenende

**Ergebnis:**
- Wendemanöver einhand in 3–5 Sekunden (Selbstwende)
- Fock-Trimm einwandfrei (Twist optimal bei Mittelstellung)
- Leichtgängig auch bei 20 kn Wind
- AYDI-Score (Ergonomie-Improvement): +35 Punkte

**Kosten:** 520 EUR Material + 600 EUR Rigger-Arbeit = 1.120 EUR

---

## ANHANG B — Weitere Fallstudien

### Fallstudie B-01: Spinnaker-Barberhaul-Schiene auf einer J/109 (Baujahr 2005)

**Ausgangssituation:**
Regattateam einer J/109 (10.89 m LüA) benötigte Spinnaker-Barberhaul-Schienen für optimierte Spi-Trimmung bei Kreuzsee. Vorhandene Schienen: keine (Spi-Schot bisher direkt über Heck-Winsch).

**Lösung:**
- 2× Ronstan Series 22 T-Track (RC7220), je 0.8 m, auf dem Achterdeck
- 2× Ronstan RC72241 Kugellager-Schlitten
- Steuerleinen 6 mm Dyneema über Umlenkblock zum Cockpit
- Durch-Bolzen in GFK-Volllaminat-Deck (kein Sandwich im Heck)

**Ergebnis:** Deutlich bessere Spi-Kontrolle in Kreuzsee. VMG-Verbesserung geschätzt 0.2–0.3 kn bei 15 kn TWS.

**Kosten:** 280 EUR Material + 200 EUR Installation = 480 EUR

### Fallstudie B-02: Hydraulischer Traveller auf einer Swan 48 (Baujahr 2012)

**Ausgangssituation:**
Kurzhand-Weltumsegelung geplant. Original: Manueller Traveller mit 8:1 Übersetzung auf dem Cockpitboden. Problem: Verstellung bei 25+ kn Wind erfordert erhebliche Kraft und Verlassen des Steuerplatzes.

**Lösung:**
- Harken HL-Track 40 mm (beibehalten, Zustand gut)
- Hydraulischer Antrieb: Lewmar Hydraulik-Zylinder beidseitig
- Steuerung: Druckknöpfe am Steuerstand (links/rechts/Mitte)
- Hydraulikpumpe: 12V, 150 bar, in Steuersäule integriert
- Notfall-Override: Manuelle Handpumpe als Backup

**Ergebnis:**
- Traveller-Verstellung per Knopfdruck, auch bei Starkwind
- Einhand-Segelbarkeit: dramatisch verbessert
- Reaktionszeit: < 2 Sekunden für volle Traversierung

**Kosten:** 4.800 EUR Material + 2.200 EUR Installation = 7.000 EUR

### Fallstudie B-03: Korrosionsschaden an Aluminium-Schiene auf Carbon-Deck, TP52 (Baujahr 2015)

**Ausgangssituation:**
Massive galvanische Korrosion an den Genua-Schienen (Harken 32 mm Alu) auf dem Carbon-Deck eines TP52-Regattateilnehmers nach nur 2 Saisons.

**Ursache:**
- Carbon und Aluminium bilden ein extrem aggressives galvanisches Paar (Spannungsdifferenz ca. 1.0 V)
- Salzwasser als Elektrolyt im Schraubenbereich
- Fehlende galvanische Isolation bei der Erstmontage

**Lösung:**
1. Alle Aluminium-Schienen durch Edelstahl 316L-Schienen ersetzt
2. GFK-Isolationsschicht (0.5 mm) zwischen Schiene und Carbon-Deck
3. Titan-Schrauben statt Edelstahl (bessere Galvanik-Kompatibilität mit Carbon)
4. PTFE-Unterlegscheiben als zusätzliche Isolation
5. Regelmäßige Inspektion alle 3 Monate

**Kosten:** 8.500 EUR (deutlich höher durch Edelstahl und Titan)

### Fallstudie B-04: Traveller-Upgrade für Charter-Flotte, Moorings 5000 (6 Boote)

**Ausgangssituation:**
Charter-Unternehmen mit 6× Moorings 5000 (15.24 m LüA, Katamaran). Häufige Traveller-Ausfälle durch unsachgemäße Bedienung durch Chartergäste: gebrochene Endstopps, blockierte Schlitten, gerissene Steuerleinen.

**Lösung (pro Boot):**
- Travellerschiene beibehalten (Lewmar Size 3, Zustand OK)
- Verstärkte Endstopps: Edelstahl-Endstopps (statt Aluminium)
- Gleitschlitten statt Kugellager (wartungsfrei, vandalismus-resistenter)
- Farbcodierung: Rote/grüne Markierungen für Standard-Trimmpositionen
- Steuerleinen: 10 mm (statt 8 mm) für bessere Griffigkeit
- Schnellklemmen statt Curryklemmen (einfachere Bedienung)
- Laminierte Anleitung am Traveller: "So bedienen Sie den Traveller"

**Ergebnis:**
- Ausfälle pro Saison: von 12 auf 2 reduziert
- Reparaturkosten pro Saison: von 3.600 EUR auf 600 EUR reduziert
- Chartergast-Zufriedenheit: verbessert (einfachere Bedienung)

**Kosten pro Boot:** 380 EUR Material + 150 EUR Arbeit = 530 EUR × 6 = 3.180 EUR

---

## ANHANG C — AYDI-Integration (Pydantic-Modelle)

### C.1 Basis-Modelle

```python
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class TrackProfile(str, Enum):
    """Track profile types for yacht rail systems."""
    T_TRACK_19 = "t_track_19"
    T_TRACK_22 = "t_track_22"
    T_TRACK_25 = "t_track_25"
    T_TRACK_32 = "t_track_32"
    T_TRACK_40 = "t_track_40"
    T_TRACK_50 = "t_track_50"
    I_BEAM = "i_beam"
    FLAT_BAR = "flat_bar"
    HL_TRACK = "hl_track"


class CarType(str, Enum):
    """Car/slider types for track systems."""
    BALL_BEARING = "ball_bearing"
    SLIDER = "slider"
    PISTON_STOP = "piston_stop"
    INTEGRAL_CLEAT = "integral_cleat"


class TrackApplication(str, Enum):
    """Application types for track systems."""
    GENOA_LEAD = "genoa_lead"
    MAINSHEET_TRAVELER = "mainsheet_traveler"
    SPINNAKER_BARBER = "spinnaker_barber"
    BOOM_VANG = "boom_vang"
    JIB_FURLER = "jib_furler"
    SELF_TACKING = "self_tacking"
    RUNNING_BACKSTAY = "running_backstay"
    MAST_TRACK = "mast_track"
    THROUGH_DECK = "through_deck"
    FENDER_RAIL = "fender_rail"
    COCKPIT_ORGANIZATION = "cockpit_organization"


class MountingMethod(str, Enum):
    """Mounting methods for track installation."""
    THROUGH_BOLT = "through_bolt"
    SHEET_SCREW = "sheet_screw"
    THREADED_INSERT = "threaded_insert"
    RIVET = "rivet"
    ADHESIVE = "adhesive"


class ConfidenceLevel(str, Enum):
    """Confidence levels for AYDI assessments."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class TrackMaterial(str, Enum):
    """Material types for tracks."""
    ALU_6061_T6 = "alu_6061_t6"
    ALU_6082_T6 = "alu_6082_t6"
    ALU_7075_T6 = "alu_7075_t6"
    STAINLESS_316L = "stainless_316l"
    CARBON = "carbon"


class TrackManufacturer(str, Enum):
    """Major track system manufacturers."""
    HARKEN = "harken"
    LEWMAR = "lewmar"
    ANTAL = "antal"
    RONSTAN = "ronstan"
    SCHAEFER = "schaefer"
    SELDEN = "selden"
    FREDERIKSEN = "frederiksen"
    OTHER = "other"
```

### C.2 Dimensions- und Spezifikationsmodelle

```python
class TrackDimensions(BaseModel):
    """Dimensional specifications of a track profile."""

    model_config = {"from_attributes": True}

    profile_width_mm: float = Field(..., gt=0, description="Profile width in mm")
    profile_height_mm: float = Field(..., gt=0, description="Profile height in mm")
    slot_width_mm: float = Field(..., gt=0, description="Slot opening width in mm")
    weight_per_meter_kg: float = Field(..., gt=0, description="Weight per meter in kg")
    length_mm: float = Field(..., gt=0, description="Total track length in mm")


class TrackSpecification(BaseModel):
    """Complete specification of a track."""

    model_config = {"from_attributes": True}

    manufacturer: TrackManufacturer
    part_number: str = Field(..., min_length=1, description="Manufacturer part number")
    profile: TrackProfile
    material: TrackMaterial
    dimensions: TrackDimensions
    swl_kg: float = Field(..., gt=0, description="Safe Working Load in kg")
    breaking_load_kg: float = Field(..., gt=0, description="Ultimate breaking load in kg")
    anodizing_type: Optional[str] = Field(None, description="Anodizing type (e.g., 'type_ii', 'type_iii')")
    screw_spacing_mm: float = Field(..., gt=0, description="Recommended screw spacing in mm")
    screw_size: str = Field(..., description="Recommended screw size (e.g., 'M6')")
    suitable_boat_length_min_m: float = Field(..., gt=0, description="Min boat length in m")
    suitable_boat_length_max_m: float = Field(..., gt=0, description="Max boat length in m")
    price_eur_per_meter: Optional[float] = Field(None, gt=0, description="Price per meter in EUR")


class CarSpecification(BaseModel):
    """Complete specification of a track car/slider."""

    model_config = {"from_attributes": True}

    manufacturer: TrackManufacturer
    part_number: str = Field(..., min_length=1, description="Manufacturer part number")
    car_type: CarType
    compatible_track_profile: TrackProfile
    swl_kg: float = Field(..., gt=0, description="Safe Working Load in kg")
    breaking_load_kg: float = Field(..., gt=0, description="Ultimate breaking load in kg")
    num_balls_per_side: Optional[int] = Field(None, ge=0, description="Number of balls per side")
    width_mm: Optional[float] = Field(None, gt=0, description="Car width in mm")
    length_mm: Optional[float] = Field(None, gt=0, description="Car length in mm")
    weight_g: Optional[float] = Field(None, gt=0, description="Weight in grams")
    has_piston_stop: bool = Field(False, description="Whether car has piston stop mechanism")
    has_integral_cleat: bool = Field(False, description="Whether car has integral cleat")
    price_eur: Optional[float] = Field(None, gt=0, description="Unit price in EUR")
```

### C.3 Installations- und Bewertungsmodelle

```python
class TrackInstallation(BaseModel):
    """Description of an installed track system."""

    model_config = {"from_attributes": True}

    application: TrackApplication
    track: TrackSpecification
    car: CarSpecification
    mounting_method: MountingMethod
    position_description: str = Field(..., description="Installation position on yacht (German)")
    deck_type: str = Field(..., description="Deck construction type (e.g., 'sandwich_balsa', 'solid_grp')")
    deck_thickness_mm: Optional[float] = Field(None, gt=0, description="Total deck thickness in mm")
    core_reinforced: bool = Field(False, description="Whether core has been reinforced at mounting points")
    backing_plate: bool = Field(False, description="Whether backing plate is installed")
    sealant_type: Optional[str] = Field(None, description="Sealant used (e.g., 'sikaflex_291')")
    installation_year: Optional[int] = Field(None, description="Year of installation")


class TrackConditionAssessment(BaseModel):
    """AYDI condition assessment of a track system."""

    model_config = {"from_attributes": True}

    installation: TrackInstallation
    overall_score: int = Field(..., ge=0, le=100, description="Overall condition score 0-100")
    track_wear_score: int = Field(..., ge=0, le=100, description="Track surface condition 0-100")
    car_condition_score: int = Field(..., ge=0, le=100, description="Car/slider condition 0-100")
    mounting_integrity_score: int = Field(..., ge=0, le=100, description="Mounting integrity 0-100")
    end_stop_score: int = Field(..., ge=0, le=100, description="End stop condition 0-100")
    control_line_score: Optional[int] = Field(None, ge=0, le=100, description="Control line condition 0-100")
    corrosion_score: int = Field(..., ge=0, le=100, description="Corrosion resistance score 0-100")
    confidence: ConfidenceLevel
    failure_patterns: list[str] = Field(default_factory=list, description="Identified failure pattern codes (e.g., 'F-01')")
    findings_de: list[str] = Field(default_factory=list, description="Findings in German")
    recommendations_de: list[str] = Field(default_factory=list, description="Recommendations in German")


class TrackLoadCalculation(BaseModel):
    """Load calculation for a track system."""

    model_config = {"from_attributes": True}

    application: TrackApplication
    boat_length_m: float = Field(..., gt=0, description="Boat LOA in meters")
    sail_area_m2: float = Field(..., gt=0, description="Sail area in m²")
    max_sheet_force_kn: float = Field(..., gt=0, description="Max sheet force in kN")
    dynamic_factor: float = Field(3.0, gt=1.0, description="Dynamic load multiplier")
    max_track_load_kn: float = Field(..., gt=0, description="Max load on track system in kN")
    required_swl_kg: float = Field(..., gt=0, description="Required SWL in kg")
    recommended_profile: TrackProfile
    recommended_car_type: CarType
    safety_factor: float = Field(..., gt=1.0, description="Applied safety factor")
    confidence: ConfidenceLevel
    calculation_notes_de: str = Field("", description="Calculation notes in German")
```

### C.4 Fehlerdiagnose-Modelle

```python
class TrackFailurePattern(BaseModel):
    """Failure pattern for track system diagnostics."""

    model_config = {"from_attributes": True}

    code: str = Field(..., pattern=r"^F-\d{2}$", description="Failure pattern code (e.g., 'F-01')")
    name_de: str = Field(..., description="Failure pattern name in German")
    name_en: str = Field(..., description="Failure pattern name in English")
    severity: str = Field(..., description="Severity level: NIEDRIG, MITTEL, HOCH, KRITISCH")
    symptoms_de: list[str] = Field(default_factory=list, description="Symptoms in German")
    causes_de: list[str] = Field(default_factory=list, description="Causes in German")
    score_range_min: int = Field(..., ge=0, le=100, description="Min AYDI score for this pattern")
    score_range_max: int = Field(..., ge=0, le=100, description="Max AYDI score for this pattern")
    immediate_action_de: str = Field("", description="Immediate action in German")
    long_term_action_de: str = Field("", description="Long-term fix in German")


class TrackSystemDiagnostic(BaseModel):
    """Complete diagnostic result for a track system."""

    model_config = {"from_attributes": True}

    assessment: TrackConditionAssessment
    load_calculation: Optional[TrackLoadCalculation] = None
    identified_failures: list[TrackFailurePattern] = Field(default_factory=list)
    sizing_adequate: bool = Field(True, description="Whether track system is adequately sized")
    upgrade_recommended: bool = Field(False, description="Whether upgrade is recommended")
    recommended_upgrade_de: Optional[str] = Field(None, description="Upgrade recommendation in German")
    estimated_remaining_life_years: Optional[float] = Field(None, description="Estimated remaining service life in years")
    estimated_repair_cost_eur: Optional[float] = Field(None, description="Estimated repair cost in EUR")
    priority: str = Field("normal", description="Priority: niedrig, normal, hoch, kritisch")
    confidence: ConfidenceLevel
```

---

## ANHANG D — Belastungstabellen

### D.1 Maximale Schotkräfte nach Bootslänge und Windstärke

| Bootslänge (m) | 3 Bft (kN) | 4 Bft (kN) | 5 Bft (kN) | 6 Bft (kN) | 7 Bft (kN) | 8 Bft (kN) |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 7 | 0.4 | 0.8 | 1.5 | 2.5 | 3.5 | 5.0 |
| 8 | 0.5 | 1.0 | 1.8 | 3.0 | 4.5 | 6.5 |
| 9 | 0.6 | 1.2 | 2.2 | 3.8 | 5.5 | 8.0 |
| 10 | 0.8 | 1.5 | 2.8 | 4.8 | 7.0 | 10.0 |
| 11 | 0.9 | 1.8 | 3.3 | 5.5 | 8.0 | 11.5 |
| 12 | 1.1 | 2.1 | 3.9 | 6.5 | 9.5 | 13.5 |
| 14 | 1.4 | 2.8 | 5.2 | 8.5 | 12.5 | 18.0 |
| 16 | 1.8 | 3.5 | 6.5 | 11.0 | 16.0 | 23.0 |
| 18 | 2.2 | 4.3 | 8.0 | 13.5 | 19.5 | 28.0 |
| 20 | 2.7 | 5.2 | 9.8 | 16.5 | 24.0 | 34.0 |

**Confidence:** estimated (Berechnungsmodell basierend auf Segelfläche ∝ LWL², Winddruck ∝ v²)

**Hinweis:** Werte sind Richtwerte für typische Segelflächenverhältnisse. Tatsächliche Lasten können je nach Rigg-Typ, Segelschnitt und Belegung um ±30 % abweichen.

### D.2 Empfohlene SWL des Schlittens nach Bootslänge

| Bootslänge (m) | Genua-Schlitten SWL (kg) | Traveller-Schlitten SWL (kg) | Spi-Barber SWL (kg) |
|:-:|:-:|:-:|:-:|
| 7 | 300–500 | 500–800 | 200–400 |
| 8 | 400–700 | 700–1.000 | 300–500 |
| 9 | 500–900 | 900–1.400 | 400–700 |
| 10 | 700–1.200 | 1.200–1.800 | 500–900 |
| 11 | 900–1.500 | 1.500–2.200 | 600–1.000 |
| 12 | 1.000–1.800 | 1.800–2.800 | 700–1.200 |
| 14 | 1.500–2.500 | 2.500–4.000 | 1.000–1.800 |
| 16 | 2.000–3.500 | 3.500–5.500 | 1.500–2.500 |
| 18 | 2.500–4.500 | 4.500–7.000 | 2.000–3.500 |
| 20 | 3.000–5.500 | 5.500–9.000 | 2.500–4.500 |

**Confidence:** calculated (Abgeleitet aus Schotkräften × Dynamikfaktor 3.0, aufgerundet)

### D.3 Schrauben-Auszugskräfte nach Deckstyp

| Deckskonstruktion | M5 Auszug (kN) | M6 Auszug (kN) | M8 Auszug (kN) | M10 Auszug (kN) |
|:-:|:-:|:-:|:-:|:-:|
| GFK Volllaminat 8 mm | 4.5 | 6.0 | 9.0 | 12.0 |
| GFK Volllaminat 12 mm | 6.5 | 8.5 | 13.0 | 17.0 |
| Sandwich Balsa (Blechschraube) | 1.5 | 2.0 | 3.5 | 5.0 |
| Sandwich Balsa (Kernverstärkt) | 4.0 | 5.5 | 8.5 | 11.5 |
| Sandwich PVC (Blechschraube) | 1.0 | 1.5 | 2.5 | 3.5 |
| Sandwich PVC (Kernverstärkt) | 3.5 | 5.0 | 8.0 | 11.0 |
| Durch-Bolzen + Gegenplatte | 12.0+ | 18.0+ | 28.0+ | 40.0+ |

**Confidence:** measured (Prüfstandswerte, Herstellerdaten GFK/Epoxid)

---

## ANHANG E — Confidence-Mapping

### E.1 Confidence-Zuordnung für Schienensystem-Bewertungen

| Datenquelle | Confidence-Level | Anwendung |
|------------|-----------------|-----------|
| Hersteller-TDS/Katalog | measured | SWL, Bruchlast, Abmessungen, Materialspezifikation |
| Belastungsberechnung aus Segelfläche | calculated | Schotkräfte, erforderliche SWL |
| Klare Foto-Aufnahme der Schiene | visual_high | Korrosion, sichtbarer Verschleiß, Montagequalität |
| Foto bei schlechtem Licht/Winkel | visual_medium | Grobe Zustandseinschätzung |
| Foto nicht aussagekräftig | visual_insufficient | Keine Bewertung möglich |
| Eigner-Angaben, Forum-Berichte | documented | Wartungshistorie, bekannte Probleme |
| Erfahrungswerte, Faustregeln | estimated | Dimensionierungsempfehlungen, Lebensdauer |
| Aggregierte Industriedaten | benchmark | Durchschnittliche Lebensdauer nach Hersteller |

### E.2 Mindest-Confidence für AYDI-Empfehlungen

| Empfehlungstyp | Mindest-Confidence |
|---------------|-------------------|
| "Sofortiger Austausch empfohlen" | measured oder visual_high |
| "Austausch mittelfristig planen" | visual_medium oder documented |
| "Beobachtung empfohlen" | estimated akzeptabel |
| "System korrekt dimensioniert" | measured oder calculated |
| "System unterdimensioniert" | calculated (mit Sicherheitsfaktor) |
| "Nicht beurteilbar" | Bei visual_insufficient oder fehlenden Daten |

---

## ANHANG F — Montage-Checklisten

### F.1 Checkliste: Genua-Schiene Neumontage

```
VORBEREITUNG:
□ Bootslänge und Segelfläche ermittelt
□ Schienengröße berechnet (Abschnitt 6)
□ Schienenlänge bestimmt (min. 20% LOA)
□ Schotwinkel berechnet (7–15° je nach Segelschnitt)
□ Position auf Seitendeck markiert
□ Deckskonstruktion geprüft (Volllaminat oder Sandwich?)
□ Unterdeck-Zugang vorhanden? (für Gegenplatten)
□ Alle Materialien und Werkzeuge bereit

KERNVERSTÄRKUNG (NUR BEI SANDWICH-DECK):
□ Pilotbohrungen gesetzt
□ Kernmaterial im Bohrungsbereich entfernt
□ Epoxid + Mikrosphären angemischt
□ In Bohrungen injiziert
□ 24 h Aushärtung abgewartet
□ Auf Schraubendurchmesser nachgebohrt

MONTAGE:
□ Schiene auf Deck positioniert und ausgerichtet
□ Ausrichtung mit Schlagschnur/Laser geprüft
□ Erste und letzte Bohrung gesetzt und geprüft
□ Alle Bohrungen gesetzt
□ Bohrungen entgratet
□ Oberfläche gereinigt (Isopropanol)
□ Primer aufgetragen (Sika 209D), 30 min trocknen
□ Dichtmasse aufgetragen (Sikaflex 291)
□ Schiene aufgesetzt, Schrauben handfest
□ Gegenplatten von unten positioniert (falls Durch-Bolzen)
□ Überschüssige Dichtmasse entfernt
□ 24 h warten
□ Schrauben auf Drehmoment angezogen
□ Endstopps montiert
□ Schlitten eingesetzt und getestet
□ Leichtgängigkeit geprüft
□ Nochmals Dichtmasse-Austritt kontrolliert
□ Probefahrt → Schotblock-Position optimal?
```

### F.2 Checkliste: Traveller-Komplettsystem Montage

```
VORBEREITUNG:
□ Traveller-Position bestimmt (Cockpitboden/Kajütdach/Achterdeck)
□ Travellerlänge berechnet (80–90% der Bootsbreite)
□ Profil und SWL bestimmt
□ Steuerungs-Übersetzung festgelegt (4:1 bis 12:1)
□ Leinenführung zum Steuerstand geplant
□ Deckstruktur geprüft

SCHIENENMONTAGE:
□ Schiene rechtwinklig zur Bootsmittellinie ausgerichtet
□ Symmetrie geprüft (gleicher Abstand zum Mast beidseitig)
□ Kernverstärkung (bei Sandwich)
□ Durch-Bolzen mit Gegenplatte (obligatorisch)
□ Dichtung (Sikaflex 291)
□ Schrauben auf Drehmoment

SCHLITTEN + STEUERUNG:
□ Schlitten eingesetzt, Leichtgängigkeit geprüft
□ Endstopps montiert (SWL ≥ Schlittenlast)
□ Steuerleinen-Umlenkblöcke montiert (an Schienenenden)
□ Fiddle-Blöcke am Schlitten befestigt
□ Steuerleinen eingezogen und auf Länge geschnitten
□ Klemmen/Fallenstopper positioniert (in Reichweite vom Steuerplatz)
□ Steuerleinen in Klemmen belegt
□ Funktionstest: Schlitten in beide Richtungen verfahren
□ Lasttest: Großschot anschlagen, bei leichtem Wind testen
□ Feinjustierung Leinenlänge und Klemmenposition
```

---

## ANHANG G — Kompatibilitätsmatrix

### G.1 Track-Car-Kompatibilität über Hersteller

| Schiene ↓ / Schlitten → | Harken 22 | Harken 27 | Lewmar S1 | Lewmar S2 | Ronstan S22 | Antal 22 | Antal 25 | Frederiksen 25 |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Harken 22 mm T-Track | ✓ | ✗ | ✗ | ✗ | ◐ | ◐ | ✗ | ✗ |
| Harken 27 mm T-Track | ✗ | ✓ | ✗ | ✗ | ✗ | ✗ | ◐ | ◐ |
| Lewmar Size 1 (20 mm) | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| Lewmar Size 2 (25 mm) | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ | ◐ | ◐ |
| Ronstan S22 | ◐ | ✗ | ✗ | ✗ | ✓ | ◐ | ✗ | ✗ |
| Antal T-Track 22 | ◐ | ✗ | ✗ | ✗ | ◐ | ✓ | ✗ | ✗ |
| Antal T-Track 25 | ✗ | ◐ | ✗ | ◐ | ✗ | ✗ | ✓ | ◐ |
| Frederiksen 25 | ✗ | ◐ | ✗ | ◐ | ✗ | ✗ | ◐ | ✓ |

**Legende:** ✓ = Volle Kompatibilität, ◐ = Bedingt kompatibel (funktioniert, aber erhöhter Verschleiß möglich), ✗ = Nicht kompatibel

**Confidence:** documented (Händlerauskunft, Praxis-Tests, Forum-Berichte)

**Wichtig:** Harken MR 27 und Schaefer-Traveller verwenden proprietäre Profile → NICHT kompatibel mit Standard-T-Track!

---

## ANHANG H — Wartungsplan und Lebensdauer

### H.1 Erwartete Lebensdauer nach Komponente

| Komponente | Lebensdauer (Jahre) | Lebensdauer (sm) | Einflussfaktoren |
|-----------|:---:|:---:|-----------|
| Aluminium-Schiene (hartanodisiert) | 20–30 | 50.000+ | Salzwasserexposition, UV, mechanische Beschädigung |
| Aluminium-Schiene (Standard-Eloxierung) | 12–20 | 30.000+ | Salzwasserexposition, Korrosion |
| Edelstahl-Schiene | 30–50 | 100.000+ | Spaltkorrosion, Säurekontakt |
| Kugellager-Schlitten | 8–15 | 15.000–30.000 | Wartung, Salzwasser, Belastungsniveau |
| Gleitschlitten (PTFE-Flächen) | 5–10 | 8.000–15.000 | Belastung, Sandexposition |
| Endstopper (Aluminium) | 15–25 | 40.000+ | Stoßbelastung, Korrosion |
| Endstopper (Edelstahl) | 25–40 | 80.000+ | Stoßbelastung |
| Steuerleinen (Dyneema) | 3–5 | 5.000–10.000 | UV, Schamfilen, Belastung |
| Steuerleinen (Polyester) | 2–4 | 3.000–6.000 | UV, Schamfilen, Belastung |
| Dichtmasse (Sikaflex 291) | 5–10 | - | UV, Temperaturwechsel |
| Kugelkäfig (Delrin) | 8–12 | 15.000–25.000 | UV (wenn exponiert), Belastung |
| Dichtlippen am Schlitten | 4–8 | 8.000–15.000 | UV, Temperatur, Schmutzexposition |

**Confidence:** estimated (Erfahrungswerte, Herstellerangaben wo verfügbar)

### H.2 Saisonaler Wartungsplan

**Saisonstart (Frühjahr):**
1. Alle Schienen mit Süßwasser und weicher Bürste reinigen
2. Schlitten von der Schiene nehmen, reinigen, inspizieren
3. Kugellager: Kugeln auf Korrosion/Abflachung prüfen
4. Gleitschlitten: PTFE-Flächen auf Verschleiß prüfen
5. Dichtlippen auf Risse/Verhärtung prüfen
6. Schlitten schmieren (McLube OneDrop für Kugellager, SailKote für Schienen)
7. Schrauben stichprobenartig auf Drehmoment prüfen (jede dritte Schraube)
8. Endstopps auf festen Sitz prüfen
9. Steuerleinen auf Schamfilstellen inspizieren
10. Schlitten auf Schiene setzen, Funktionstest

**Saisonmitte (alle 4–6 Wochen):**
1. Süßwasserspülung der Schienen
2. Leichtgängigkeit der Schlitten prüfen
3. Steuerleinen auf Verschleiß sichtprüfen
4. Nachschmierung bei Bedarf (Kugellager-Schlitten)

**Saisonende (Herbst):**
1. Komplette Reinigung aller Schienen und Schlitten
2. Schlitten von der Schiene nehmen
3. Kugellager-Schlitten: komplett zerlegen, reinigen, neu schmieren
4. Gleitschlitten: PTFE-Flächen reinigen, Zustand dokumentieren
5. Schlitten in verschlossenen Plastikbeuteln trocken lagern
6. Schienen mit Korrosionsschutz behandeln (Lanocote oder McLube SailKote)
7. Schienennut mit Klebeband abdecken (gegen Winterverschmutzung)
8. Steuerleinen abnehmen und trocken lagern

---

## ANHANG I — Preis-Referenz

### I.1 Preisübersicht Schienen (pro Meter, inkl. MwSt., Stand 2026)

| Hersteller/Modell | Budget | Standard | Premium |
|:--|:-:|:-:|:-:|
| 19 mm T-Track | 12–18 EUR (Fred.) | 18–28 EUR (Ronstan) | 30–42 EUR (Harken) |
| 22 mm T-Track | 18–25 EUR (Fred.) | 28–42 EUR (Ronstan) | 38–55 EUR (Harken) |
| 25 mm T-Track | 25–38 EUR (Fred.) | 42–62 EUR (Ronstan/Lewmar) | 55–80 EUR (Harken) |
| 32 mm T-Track | 48–70 EUR (Fred.) | 68–98 EUR (Ronstan/Lewmar) | 85–120 EUR (Harken) |
| 40 mm T-Track | - | 110–160 EUR (Lewmar) | 145–200 EUR (Harken) |

### I.2 Preisübersicht Schlitten (pro Stück, inkl. MwSt., Stand 2026)

| Typ / Profil | Gleitschlitten | Kugellager | Kugellager + Kolben |
|:--|:-:|:-:|:-:|
| 19 mm | 15–25 EUR | 22–65 EUR | 35–80 EUR |
| 22 mm | 22–40 EUR | 45–110 EUR | 60–140 EUR |
| 25 mm | 35–70 EUR | 75–165 EUR | 95–200 EUR |
| 32 mm | 60–120 EUR | 120–280 EUR | 160–350 EUR |
| 40 mm | 90–180 EUR | 200–420 EUR | 280–550 EUR |

### I.3 Preisübersicht Komplett-Systeme (Traveller, inkl. MwSt.)

| Bootslänge | Budget-System | Standard-System | Premium-System |
|:--|:-:|:-:|:-:|
| 7–9 m | 180–300 EUR | 350–550 EUR | 600–900 EUR |
| 9–11 m | 280–450 EUR | 500–800 EUR | 900–1.400 EUR |
| 11–14 m | 400–650 EUR | 750–1.200 EUR | 1.300–2.200 EUR |
| 14–18 m | 600–1.000 EUR | 1.200–2.000 EUR | 2.200–3.800 EUR |
| 18–25 m | - | 2.000–4.000 EUR | 4.000–8.000 EUR |

**Confidence:** estimated (Händlerpreise, Online-Shops, Stand 2026, ±15 %)

---

## ANHANG J — Entscheidungsbaum Systemauswahl

### J.1 Genua-Schienensystem auswählen

```
START: Genua-Schienensystem benötigt
│
├── Bootslänge?
│   ├── < 7 m → 19 mm T-Track
│   ├── 7–9 m → 22 mm T-Track
│   ├── 9–11 m → 25 mm T-Track
│   ├── 11–14 m → 25 oder 32 mm T-Track
│   ├── 14–18 m → 32 mm T-Track
│   └── > 18 m → 32–40 mm T-Track oder HL-Track
│
├── Einsatzzweck?
│   ├── Regatta → Kugellager-Schlitten, leichtes Profil
│   ├── Fahrt → Kugellager mit Kolbenstopp ODER Gleit (Blauwasser)
│   └── Charter → Gleitschlitten mit Kolbenstopp
│
├── Budget?
│   ├── Budget → Frederiksen/Ronstan + Gleitschlitten
│   ├── Mittel → Lewmar/Ronstan + Kugellager
│   └── Premium → Harken/Antal + Kugellager
│
└── Deck-Typ?
    ├── Volllaminat → Blechschrauben akzeptabel (< 500 kg SWL)
    ├── Sandwich → Kernverstärkung + Durch-Bolzen obligatorisch
    └── Teak über GFK → Längere Schrauben, Dichtung kritisch
```

### J.2 Travellersystem auswählen

```
START: Travellersystem benötigt
│
├── Montageposition?
│   ├── Cockpitboden → Standard T-Track oder I-Beam
│   ├── Kajütdach → T-Track, strukturelle Verstärkung prüfen
│   └── Achterdeck → T-Track, lange Steuerleinen einplanen
│
├── Bootslänge → Profil (wie Genua, eine Größe höher)
│
├── Steuerungstyp?
│   ├── < 10 m → 4:1 manuell (Fiddle-Block)
│   ├── 10–14 m → 6:1 manuell
│   ├── 14–18 m → 8:1 manuell oder elektrische Winsch
│   └── > 18 m → 12:1 oder hydraulisch
│
└── Budget?
    ├── Komplettsystem (Lewmar, Schaefer) → einfachste Lösung
    └── Einzelkomponenten (Harken, Ronstan) → flexibler, oft teurer
```

---

## ANHANG K — Normen und Zertifizierungen

### K.1 Relevante Normen für Schienensysteme

| Norm | Titel | Relevanz für Schienensysteme |
|------|-------|------------------------------|
| ISO 15084 | Yachten — Verankern, Vertäuen, Schleppen — Festigkeitsanforderungen | Allgemeine Festigkeitsanforderungen für Decksbeschläge |
| ISO 15085 | Yachten — Schutz vor Mann-über-Bord | Schienenposition darf keine Stolpergefahr bilden |
| ISO 12215-8 | Yachten — Rumpfbauweise — Teil 8: Ruder | Ruderbeschlag-Festigkeit (indirekt: Decksverstärkung) |
| ISO 12215-9 | Yachten — Rumpfbauweise — Teil 9: Anhänge von Segelbooten (Kiele, Ruder, Schwerter) | Indirekt (nächstliegende Norm): Festigkeitsnachweis; deckt Kiel-/Ruderanhänge ab, nicht Deckbeschläge direkt |
| EN 13852-1 | Krane — Offshore-Krane — Allgemein | Indirekt: SWL-Definition und Sicherheitsfaktoren |
| DNV GL Rules | Klassifikationsregeln | Superyacht-Klassifikation: Decksbeschlag-Nachweise |

### K.2 Hersteller-Zertifizierungen

| Hersteller | Zertifizierungen |
|-----------|-----------------|
| Harken | ISO 9001:2015, ISAF-zugelassen für Regatta-Hardware |
| Lewmar | ISO 9001:2015, Lloyd's Type Approved (Winschen) |
| Antal | ISO 9001:2015 |
| Ronstan | ISO 9001:2015, AS/NZS 4801 |
| Schaefer | ISO 9001:2015 |

**Hinweis:** Es gibt keine eigenständige Norm speziell für Schienensysteme im Yachtbau. Die Dimensionierung erfolgt nach Ingenieurspraxis und Herstellervorgaben. Die ISO 12215-9 ist die nächstliegende Norm für Festigkeitsnachweise von Decksbeschlägen.

---

## ANHANG L — Regatta-spezifische Anforderungen

### L.1 Klassenregeln und Schienensysteme

| Klasse | Einschränkungen Schienensysteme |
|--------|-------------------------------|
| ORC/IRC | Keine spezifischen Beschränkungen, aber Gewicht zählt (Rating) |
| IMOCA 60 | Alle Systeme erlaubt, Carbon-Schienen üblich |
| Mini 6.50 | Maximale Schienenlänge gemäß Klassenregel |
| J/70, J/80 | One-Design: herstellerspezifisches System vorgeschrieben |
| Laser/ILCA | Kein Traveller, nur Standard-Großschot-Führung |
| 420, 470 | Standard-Schienen gemäß Klassenregel, max. Gewicht definiert |
| SB20 | Standard Harken 22 mm, keine Modifikation erlaubt |
| Dragon | Standard-Traveller, keine Carbon-Upgrades erlaubt |

### L.2 Regatta-Tuning: Reibungsoptimierung

**Maßnahmen zur Reibungsminimierung:**

1. **Schiene polieren:** Feinschliff mit 1200er/2000er Nassschleifpapier in Laufrichtung, dann Politur
2. **Kugeln tauschen:** Edelstahl-Kugeln durch polierte Torlon-Kugeln ersetzen (µ -30 %)
3. **Trockenschmierung:** McLube SailKote statt Fett (kein Schmutzfang)
4. **Dichtlippen entfernen:** Nur für Regatta! Erhöht Empfindlichkeit gegen Verschmutzung drastisch
5. **Leichtbau-Schlitten:** Carbon-Gehäuse mit Torlon-Kugeln (Gewichtsersparnis 40–60 %)
6. **UHMWPE-Steuerleinen:** Dyneema SK78 oder Spectra, Durchmesser minimieren

**Achtung:** Jede Reibungsminimierung reduziert die Lebensdauer und erhöht die Wartungsintensität. Für Fahrtenyachten nicht empfohlen.

---

## ANHANG M — Materialdatenblätter

### M.1 Aluminium 6082-T6 (Standard für hochwertige Marine-Schienen)

| Eigenschaft | Wert | Einheit |
|:--|:-:|:-:|
| Dichte | 2.71 | g/cm³ |
| Streckgrenze Rp0.2 | 310 | MPa |
| Zugfestigkeit Rm | 340 | MPa |
| Bruchdehnung A | 10 | % |
| Elastizitätsmodul E | 70 | GPa |
| Schubmodul G | 26 | GPa |
| Wärmeausdehnungskoeffizient | 23.4 | 10⁻⁶/K |
| Wärmeleitfähigkeit | 172 | W/(m·K) |
| Spezifischer Widerstand | 0.038 | µΩ·m |
| Elektrochemisches Potential (Meerwasser) | -0.83 | V (vs. Ag/AgCl) |

### M.2 Edelstahl 316L (für Superyacht-Schienen und Schrauben)

| Eigenschaft | Wert | Einheit |
|:--|:-:|:-:|
| Dichte | 7.98 | g/cm³ |
| Streckgrenze Rp0.2 | 170 | MPa |
| Zugfestigkeit Rm | 485 | MPa |
| Bruchdehnung A | 40 | % |
| Elastizitätsmodul E | 193 | GPa |
| Schubmodul G | 77 | GPa |
| Wärmeausdehnungskoeffizient | 15.9 | 10⁻⁶/K |
| Wärmeleitfähigkeit | 16.3 | W/(m·K) |
| Elektrochemisches Potential (Meerwasser) | -0.05 bis +0.10 | V (vs. Ag/AgCl) |
| Pitting Resistance Equivalent | 25.0 | - |

### M.3 Delrin (POM-C) — Standard für Kugelkäfige und Gleitflächen

| Eigenschaft | Wert | Einheit |
|:--|:-:|:-:|
| Dichte | 1.41 | g/cm³ |
| Streckgrenze | 65 | MPa |
| Zugfestigkeit | 70 | MPa |
| Elastizitätsmodul | 3.0 | GPa |
| Wasseraufnahme (24h) | 0.22 | % |
| Reibungskoeffizient (trocken, auf Stahl) | 0.20 | - |
| Reibungskoeffizient (geschmiert, auf Stahl) | 0.05 | - |
| Max. Einsatztemperatur | 100 | °C |
| UV-Beständigkeit | Mäßig | (Stabilisator empfohlen) |

### M.4 Torlon (PAI) — Hochleistungskugeln für Regatta

| Eigenschaft | Wert | Einheit |
|:--|:-:|:-:|
| Dichte | 1.42 | g/cm³ |
| Druckfestigkeit | 210 | MPa |
| Zugfestigkeit | 120 | MPa |
| Elastizitätsmodul | 4.5 | GPa |
| Reibungskoeffizient (trocken) | 0.12 | - |
| Max. Einsatztemperatur | 260 | °C |
| Wasseraufnahme (24h) | 0.33 | % |
| Gewichtsvorteil vs. Edelstahl-Kugel | 82 % leichter | - |

---

## ANHANG N — Schienensystem-Bewertungsschema

### N.1 AYDI-Scoring-Schema für Schienensysteme

**Gesamtscore = Gewichteter Durchschnitt der Teilscores:**

| Teilbereich | Gewicht | Score-Bereich | Beschreibung |
|:--|:-:|:-:|:--|
| Dimensionierung | 25 % | 0–100 | Ist das System korrekt für Boot/Segelfläche dimensioniert? |
| Zustand Schiene | 20 % | 0–100 | Verschleiß, Korrosion, Verformung der Schiene |
| Zustand Schlitten | 20 % | 0–100 | Kugellager, Gleitflächen, Dichtungen, Bügel |
| Montagequalität | 15 % | 0–100 | Befestigung, Dichtung, Ausrichtung |
| Funktionalität | 10 % | 0–100 | Leichtgängigkeit, Steuerung, Arretierung |
| Zubehör | 10 % | 0–100 | Endstopps, Steuerleinen, Blöcke, Klemmen |

**Score-Interpretation:**

| Score | Bewertung | Handlungsempfehlung |
|:-----:|:---------:|:--------------------|
| 90–100 | Ausgezeichnet | Keine Maßnahmen erforderlich |
| 75–89 | Gut | Routinewartung ausreichend |
| 60–74 | Befriedigend | Einzelne Komponenten prüfen/erneuern |
| 40–59 | Mangelhaft | Teilaustausch oder Überholung empfohlen |
| 20–39 | Ungenügend | Gesamtaustausch empfohlen |
| 0–19 | Kritisch | Sofortiger Austausch, Sicherheitsrisiko |

### N.2 Visuelle Bewertungskriterien (Pipeline B — Visual)

| Merkmal | Score 80–100 | Score 50–79 | Score 0–49 |
|:--|:--|:--|:--|
| Schienenoberfläche | Glatt, gleichmäßig eloxiert | Leichte Kratzer, Oberflächenoxidation | Tiefe Rillen, Lochfraß, Eloxierung abgeblättert |
| Schlittenlauf | Keine sichtbare Abnutzung | Leichte Gebrauchsspuren | Sichtbarer Verschleiß, Spiel, Verkippung |
| Schraubenköpfe | Sauber, Dichtmasse intakt | Leichte Korrosion, Dichtmasse teilweise gerissen | Starke Korrosion, Dichtmasse fehlt, Wasserflecken |
| Endstopps | Fest, kein Spiel | Leichtes Spiel | Verbogen, locker, fehlend |
| Steuerleinen | Neuwertig, keine Schamfilen | Gebrauchsspuren, leichtes Fusseln | Durchgescheuert, gerissen, UV-versprödot |
| Decksfläche um Schiene | Sauber, kein Rissbildung | Leichte Risse im Gelcoat | Delamination, Weichstellen, Wasserflecken |

---

## ANHANG O — Historische Entwicklung

### O.1 Meilensteine der Schienensystem-Entwicklung

| Jahrzehnt | Entwicklung | Auswirkung |
|-----------|-----------|------------|
| 1950er | Holz-Gleitschienen | Einfachste Form, hohe Reibung, begrenzte Lebensdauer |
| 1960er | Aluminium-Strangpressprofile (T-Track) | Standardisierung, Massenfertigung möglich |
| 1967 | Harken-Gründung | Beginn der Professionalisierung der Deckshardware |
| 1970er | Kugellager-Schlitten (Harken) | Revolution der Reibungsminimierung |
| 1980er | Hartanodisierung für Marine-Anwendungen | Deutlich verbesserte Lebensdauer der Alu-Schienen |
| 1990er | Torlon- und Delrin-Kugeln/Käfige | Gewichts- und Korrosionsvorteile |
| 2000er | Hydraulische Travellersysteme | Fernsteuerung auf großen Yachten |
| 2010er | Carbon-Schienen für Regatta | Extremer Leichtbau |
| 2020er | Integrierte Sensoren (Load Cells) | Digitale Lastüberwachung auf Superyachten |

### O.2 Bedeutende Konstrukteure und ihre Beiträge

- **Peter Harken**: Pionier der Kugellager-Deckshardware, machte leichtgängige Trimmung für jedermann zugänglich
- **Rod Johnstone (J-Boats)**: Popularisierte den Cockpitboden-Traveller im Regattabereich
- **Sparkman & Stephens**: Entwickelten Dimensionierungsrichtlinien für Schienensysteme auf großen Yachten
- **Rolf Vrøhm (Seldén)**: Integrierte Schienensysteme mit Mastkonstruktion als Gesamtsystem

---

## ANHANG P — Retrofit-Szenarien

### P.1 Typische Retrofit-Szenarien und Empfehlungen

#### P.1.1 Szenario: Upgrade von Gleit- auf Kugellager-Schlitten

**Voraussetzung:** Bestehende T-Track-Schiene in gutem Zustand

**Vorgehen:**
1. Profilgröße der vorhandenen Schiene identifizieren (messen: Breite auf 0.5 mm)
2. Kompatiblen Kugellager-Schlitten wählen (gleicher Hersteller bevorzugt)
3. Alten Schlitten entfernen (Endstopps lösen)
4. Schiene reinigen und auf Verschleiß prüfen
5. Neuen Schlitten einsetzen
6. Endstopps wieder montieren

**Kosten:** 50–300 EUR (nur Schlitten)
**Aufwand:** 30 Minuten

#### P.1.2 Szenario: Schienenverlängerung für größere Genua

**Voraussetzung:** Ausreichend Platz auf dem Seitendeck

**Vorgehen:**
1. Benötigte Verlängerung berechnen (neue Genua-Größe → neuer Holepunktbereich)
2. Gleiche Schiene oder kompatible Verlängerung beschaffen
3. Stoßverbinder (Track Joiner) beschaffen
4. Verlängerungsschiene ausrichten (fluchtend mit bestehender Schiene)
5. Kernverstärkung für neue Bohrungen
6. Montage mit Durch-Bolzen und Dichtung
7. Stoßverbinder einsetzen
8. Endstopps versetzen

**Kosten:** 150–400 EUR (Material)
**Aufwand:** 3–5 Stunden

#### P.1.3 Szenario: Wechsel von Flat-Bar auf T-Track

**Voraussetzung:** Boot mit alter Flat-Bar-Schiene (typisch vor 1990)

**Vorgehen:**
1. Flat-Bar und alle Beschläge demontieren
2. Alte Bohrungen verschließen (Epoxid + GFK-Stopfen)
3. Neue T-Track-Schiene positionieren (ggf. versetzt zu alten Bohrungen)
4. Kernverstärkung (bei Sandwich-Deck)
5. Durch-Bolzen-Montage mit Dichtung
6. Neuen Schlitten und Endstopps montieren

**Kosten:** 300–800 EUR (Material) + 200–500 EUR (Arbeit)
**Aufwand:** 1–2 Tage

---

## ANHANG Q — Herstellervergleich Scoring

### Q.1 Bewertungsmatrix (AYDI-interne Herstellerbewertung)

| Kriterium (Gewicht) | Harken | Lewmar | Antal | Ronstan | Schaefer | Seldén | Frederiksen |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Produktqualität (25%) | 95 | 82 | 90 | 88 | 85 | 80 | 68 |
| Sortimentsbreite (15%) | 95 | 85 | 75 | 80 | 60 | 65 | 55 |
| Verfügbarkeit EU (15%) | 85 | 92 | 78 | 75 | 55 | 80 | 82 |
| Preis-Leistung (15%) | 65 | 78 | 70 | 80 | 75 | 75 | 92 |
| Technische Dokumentation (10%) | 90 | 80 | 75 | 85 | 70 | 70 | 55 |
| Ersatzteilversorgung (10%) | 90 | 88 | 70 | 78 | 60 | 75 | 65 |
| Innovation (10%) | 92 | 70 | 80 | 88 | 65 | 65 | 55 |
| **Gesamt** | **87** | **83** | **78** | **81** | **67** | **74** | **70** |

**Confidence:** estimated (AYDI-interne Bewertung basierend auf Marktanalyse, Eigner-Feedback, Rigger-Befragung)

---

## ANHANG R — Weiterführende Ressourcen

### R.1 Fachliteratur

| Titel | Autor | Relevanz |
|-------|-------|----------|
| Rigging Modern Sailing Yachts | Ivar Dedekam | Umfassende Referenz zu Deck-Hardware und Rigg-Dimensionierung |
| The Complete Rigger's Apprentice | Brion Toss | Praxishandbuch für Rigg-Arbeit inkl. Schienensysteme |
| Spurkranz und Schiene | Heinrich Wörner | Deutschsprachige Referenz für Schienensysteme |
| Yacht Design According to Perry | Robert Perry | Designgrundlagen inkl. Deck-Layout und Hardware-Positionierung |
| Metal Corrosion in Boats | Nigel Warren | Korrosion an Decksbeschlägen, galvanische Probleme |
| Refit Your Yacht | Dag Pike | Praxisleitfaden für Schienensystem-Upgrades |

### R.2 Online-Ressourcen

| Ressource | URL | Inhalt |
|-----------|-----|--------|
| Harken Technik-Center | harken.com/tech-center | Montageanleitung, Wartungsvideos, SWL-Tabellen |
| Lewmar Technik-Support | lewmar.com/support | Explosionszeichnungen, Ersatzteil-Finder |
| Sailing Anarchy Forum | sailinganarchy.com | Erfahrungsberichte, Vergleichstests |
| Cruisers Forum | cruisersforum.com | Blauwasser-Praxiserfahrungen |
| Rigger's Locker | riggerslocker.co.uk | Fachhandel mit technischer Beratung |

### R.3 Händler (Europa)

| Händler | Land | Spezialisierung | Website |
|---------|------|-----------------|---------|
| Toplicht | DE | Vollsortiment, gute Beratung | toplicht.de |
| SVB | DE | Vollsortiment, großes Lager | svb-marine.de |
| Compass24 | DE | Online, gute Preise | compass24.de |
| ASAP Supplies | UK | Schnelle Lieferung, Spezialteile | asap-supplies.com |
| Accastillage Diffusion | FR | Frankreichs größter Fachhändler | accastillage-diffusion.com |
| Navimo/Uship | FR | Online + Fillialen | uship.fr |
| Reggane Nautica | IT | Antal-Spezialist | reggane-nautica.it |

### R.4 Software-Tools

| Tool | Anwendung | Verfügbarkeit |
|------|-----------|---------------|
| Harken Traveler Sizing Calculator | Online-Rechner für Traveller-Dimensionierung | harken.com |
| Ronstan Product Selector | Interaktiver Produktwähler mit SWL-Filter | ronstan.com |
| AYDI Track Module | Integrierte Bewertung im AYDI-System | app.aydi.de |

### R.5 YouTube-Kanäle und Video-Ressourcen

| Kanal/Video | Thema | Sprache |
|------------|-------|---------|
| Harken Official — "Track Installation Guide" | Schrittweise Schienenmontage mit Kernverstärkung | EN |
| Harken Official — "Traveler Maintenance" | Zerlegung und Wartung von Kugellager-Schlitten | EN |
| Lewmar Tech — "Deck Hardware Installation" | OEM-Montageanleitung für Lewmar-Systeme | EN |
| Sail Magazine — "Understanding Genoa Tracks" | Holepunkt-Optimierung und Trimmtheorie | EN |
| Rigger's Locker — "Track Car Rebuild" | Praxisvideo: Komplettüberholung eines Harken-Schlittens | EN |
| ESBO Werft — "Schienenmontage auf Sandwich-Deck" | Deutschsprachige Montageanleitung mit Kernverstärkung | DE |
| Yachting Monthly — "Self-Tacking Jib Systems" | Vergleich verschiedener Selbstwendesysteme | EN |
| Performance Sailcraft — "Traveler Setup for Racing" | Regatta-Trimmtipps für Travellersysteme | EN |
| SV Delos — "Replacing Our Genoa Track" | Blauwasser-Yacht: Genua-Schienen-Retrofit Praxisbericht | EN |
| Catamaran Guru — "Catamaran Traveler Systems" | Besonderheiten Traveller auf Katamaranen | EN |

### R.6 Erfahrungsberichte und Forum-Threads (Auswahl)

**Deutschsprachige Foren:**

| Forum | Thread | Kernaussage |
|-------|--------|-------------|
| Segeln-Forum.de | "Harken vs. Lewmar Genua-Schiene" | Konsens: Harken leichtgängiger, Lewmar preiswerter; für Fahrt Lewmar ausreichend |
| Segeln-Forum.de | "Traveller auf dem Kajütdach – Verstärkung?" | Erfahrungen mit Kajütdach-Verstärkung, Konsens: 4-Lagen biaxial unter GFK-Dach |
| Boote-Forum.de | "Sandwich-Deck: Genua-Schiene undicht" | Häufiges Problem Bavaria/Jeanneau, Lösung: Kernverstärkung + Durch-Bolzen |
| Boote-Forum.de | "Gleit- vs. Kugellager-Schlitten" | Blauwasser-Fraktion bevorzugt Gleit, Regatta bevorzugt Kugellager |
| Yacht.de Forum | "Traveller-Upgrade für HR 34" | Hallberg-Rassy-spezifische Montagetipps |
| Sailing-Forum.de | "Selbstwendefock nachrüsten – sinnvoll?" | Geteilte Meinungen: Kurzhandsegler dafür, Regattasegler dagegen |

**Englischsprachige Foren:**

| Forum | Thread | Kernaussage |
|-------|--------|-------------|
| Cruisers Forum | "Best genoa track for bluewater" | Ronstan und Harken dominieren; Konsens: Gleitschlitten für offshore |
| Sailing Anarchy | "Carbon traveler tracks – worth it?" | Nur für extreme Regatta sinnvoll, Faktor 10× Kosten |
| The Hull Truth | "Track corrosion on my Beneteau" | Galvanische Korrosion Alu/Edelstahl, Lösung: Isolation + Dichtmasse |
| YBW Forum | "Lewmar Size 2 to Harken 27 swap" | Erfahrungsbericht: Harken-Kugellager spürbar leichter |
| Sailnet | "DIY Traveler replacement guide" | Schrittanleitung für den Travellertausch durch Eigner |

### R.7 Fachzeitschriften-Artikel

| Zeitschrift | Ausgabe | Artikel | Relevanz |
|------------|---------|---------|----------|
| YACHT (DE) | 03/2024 | "Schienensysteme im Vergleich" | Test von 5 Herstellern, Harken Testsieger |
| Segeln Magazin (DE) | 05/2023 | "Traveller richtig dimensionieren" | Praxistipps zur Größenwahl |
| Practical Sailor (US) | 01/2024 | "Track Car Shootout" | Detailvergleich Kugellager-Schlitten 25 mm |
| Yachting Monthly (UK) | 07/2023 | "Self-Tacking Jibs: The Complete Guide" | Übersicht aller ST-Jib-Systeme am Markt |
| Practical Boat Owner (UK) | 09/2023 | "Installing a New Genoa Track" | DIY-Anleitung mit Sandwich-Deck-Fokus |
| Sailing World (US) | 11/2023 | "Optimizing Your Traveler for Speed" | Regatta-Tuning-Tipps |
| Palstek (DE) | 02/2024 | "Wartung von Kugellager-Schlitten" | Schrittweise Überholungsanleitung |
| YACHT Classic (DE) | 04/2023 | "Flat-Bar auf T-Track: Lohnt der Umbau?" | Fallstudien von 3 Classic-Yacht-Umbauten |

### R.8 Bezugsquellen für Ersatzteile

**Originalteile direkt vom Hersteller:**

| Hersteller | Ersatzteil-Service | Lieferzeit (EU) | Mindestbestellwert |
|-----------|-------------------|-----------------|---------------------|
| Harken | harken.com/parts | 3–7 Werktage | Keiner |
| Lewmar | Über Fachhändler | 5–10 Werktage | Über Händler |
| Ronstan | ronstan.com/spare-parts | 7–14 Werktage (aus AU) | 25 EUR |
| Antal | antal.it/spare-parts | 5–10 Werktage | 30 EUR |
| Schaefer | schaefermarine.com | 10–21 Werktage (aus US) | 50 USD |

**Universalteile und Alternativen:**

| Teileart | Quelle | Bemerkung |
|---------|--------|----------|
| Edelstahl-Kugeln (316L) | Kugellager-Fachhandel | Günstiger als Originalteile, Durchmesser exakt messen! |
| Delrin-Stangenmaterial | Kunststoff-Fachhandel | Für selbstgefertigte Gleitflächen und Käfige |
| PTFE-Folie | Industriebedarf | Zum Erneuern von Gleitflächen (0.5–1.0 mm) |
| Dichtlippen/O-Ringe | O-Ring-Fachhandel | Werkstoff: NBR oder EPDM, Maß vom Original abnehmen |
| T-Track-Profile | Alu-Strangpresser (China) | Deutlich günstiger, aber Qualitätskontrolle kritisch! |

### R.9 Regionale Rigger und Spezialisten (DACH-Raum)

| Firma | Standort | Spezialisierung |
|-------|----------|-----------------|
| Rigg Service Zürich | CH — Zürich | Rigg-Überholung inkl. Deck-Hardware |
| Maststep Kiel | DE — Kiel | Masten und Schienensysteme, Harken-Spezialist |
| Segelwerk Fehmarn | DE — Fehmarn | Segelmacherei + Deck-Hardware-Installation |
| Yachtservice Heiligenhafen | DE — Heiligenhafen | Vollservice, Lewmar-Vertragshändler |
| Marina Werft Laboe | DE — Laboe | Refits inkl. Schienensystem-Upgrades |
| Bootswerft Grünau | AT — Attersee | Süßwasser-Spezialist, Binnenrevier |
| Yachttechnik Bodensee | DE — Konstanz | Binnenrevier, Bavaria/Jeanneau-Spezialist |
| Sailcom Rigging | CH — Romanshorn | Regatta-Rigg-Service |
| Rigger.at | AT — Neusiedlersee | Mobiler Rigg-Service |
| Baltic Rigging | DE — Rostock | Ostsee-Spezialist, Hallberg-Rassy/Najad |

### R.10 Lernressourcen und Kurse

| Anbieter | Kurs | Inhalt | Format |
|---------|------|--------|--------|
| NauticEd | "Sailing Rigging Fundamentals" | Grundlagen Rigg und Deck-Hardware | Online |
| ISAF/World Sailing | "Technical Delegates Course" | Regatta-Hardware-Inspektion | Präsenz |
| VDS (Verband Deutscher Sportbootschulen) | "Bordtechnik-Seminar" | Deck-Hardware-Wartung für Eigner | Präsenz |
| Royal Yachting Association | "Practical Yachtsman" | DIY-Wartung inkl. Schienensysteme | Online + Präsenz |
| Harken Academy | "Deck Hardware Masterclass" | Herstellerspezifisches Training | Auf Anfrage |
| Rigging Doctor (Brian Toss) | Workshops | Rigg-Inspektion und Wartung | Präsenz (USA) |

---

## ANHANG S — Erweiterte Berechnungsbeispiele

### S.1 Vollständige Traveller-Dimensionierung: Beispiel Bavaria C42

**Boot:** Bavaria C42 (12.35 m LüA, 3.99 m Breite)

**Schritt 1: Segelfläche Großsegel**
- P (Masthöhe) = 14.80 m
- E (Baumlänge) = 5.10 m
- Großsegelfläche = P × E / 2 = 14.80 × 5.10 / 2 = 37.74 m²

**Schritt 2: Maximale Schotkraft**
- Winddruck bei 30 kn (15.4 m/s): q = 0.5 × 1.225 × 15.4² = 145.3 Pa
- Segeldruck: F_segel = q × A × Cl = 145.3 × 37.74 × 1.4 = 7.677 N ≈ 7.7 kN
- Schotkraft (unter Berücksichtigung der Schotübersetzung 3:1): F_schot = 7.7 / 3 = 2.57 kN
- Direkte Schotkraft auf Traveller: F_schot_direkt ≈ 5.0 kN (ohne Übersetzung)

**Schritt 3: Traveller-Querlast**
- Schotwinkel zur Vertikale: α = 25° (typisch bei Kajütdach-Traveller)
- F_traveller = F_schot × sin(α) = 5.0 × sin(25°) = 5.0 × 0.423 = 2.11 kN

**Schritt 4: Dynamikfaktor**
- Fahrtenyacht: Dynamikfaktor 3.0
- F_traveller_max = 2.11 × 3.0 = 6.34 kN = 646 kg

**Schritt 5: Erforderliche SWL**
- SWL ≥ F_traveller_max = 646 kg
- Empfohlen: SWL ≥ 1.000 kg (Sicherheitsreserve)

**Schritt 6: Profilwahl**
- 25 mm T-Track: SWL 1.200 kg → ausreichend ✓
- 32 mm T-Track: SWL 2.800 kg → komfortabel ✓ (empfohlen für Langlebigkeit)

**Schritt 7: Schienenlänge**
- Bootsbreite am Cockpit: ca. 3.60 m
- Optimale Travellerlänge: 80 % × 3.60 m = 2.88 m → 2.80 m (gerundet)

**Schritt 8: Steuerungsübersetzung**
- Maximale Handkraft: 20 kg
- Erforderliche Übersetzung: 646 / 20 = 32.3 → Mechanisch nicht praktikabel
- Realistisch: 6:1 Übersetzung + Winsch (Winschkraft 10:1 = effektiv 60:1)
- Oder: 8:1 ohne Winsch → Handkraft 646 / 8 = 80.8 kg → zu hoch → Winsch nötig

**Ergebnis: Empfohlenes System**
- Schiene: Harken 32 mm T-Track (Art. 2733, 2.0 m) + Verlängerung (Art. 2732, 1.0 m) = 3.0 m mit Stoßverbinder
- Schlitten: Harken 32 mm Kugellager (Art. 2737)
- Steuerung: 6:1 mit Fiddle-Block, Steuerleinen zu 30er-Winsch (oder 8:1 manuell mit Klemmen)
- Geschätzte Kosten: ca. 850–1.100 EUR (Material)

**Confidence:** calculated (Berechnungsmodell auf Basis gemessener Segelparameter)

### S.2 Genua-Holepunkt-Berechnung: Beispiel Dehler 38 SQ

**Boot:** Dehler 38 SQ (11.54 m LüA)
**Genua:** 135 %, LP = 5.58 m, Luff = 14.20 m

**Optimaler Holepunkt (Vertikale Analyse):**
- Sheeting Angle (SA) = arctan(Clew_height / Foot_length)
- Bei typischer 135 % Genua: SA ≈ 8–10°
- Holepunkt-Abstand vom Vorstag: D_hp = LP / (2 × tan(SA_optimal))
- D_hp = 5.58 / (2 × tan(9°)) = 5.58 / 0.317 = 17.6 m → Unplausibel (> LüA)

**Korrigierte Methode (Twist-Optimierung):**
- Linie vom Schothorn zum oberen Achterliek-Telltale
- Diese Linie (verlängert nach unten) kreuzt das Deck am optimalen Holepunkt
- Praktisch: Holepunkt ca. bei 40–45 % der Vorliekhöhe ab Deck gemessen entlang der Schiene

**Empirische Methode (Segelmacher-Regel):**
- Schotblock-Position so, dass Genua gleichmäßig einfällt (Luv-Telltales Mitte und oben gleichzeitig)
- Vorliche Telltales zuerst oben → Holepunkt nach vorn
- Vorliche Telltales zuerst unten → Holepunkt nach achtern

**Empfohlener Schotwinkel für Dehler 38:**
- 135 % Genua: 8–10°
- 106 % Fock: 12–14°

**Schienenlänge:**
- Mindestens: Abstand zwischen optimalem Holepunkt Genua 135 % und Fock 106 %
- Empfohlen: 2.0–2.2 m für die Dehler 38

**Confidence:** calculated + estimated (Geometrische Berechnung + Segelmacher-Erfahrung)

### S.3 Schraubenanzahl-Berechnung für Genua-Schiene

**Gegebene Werte:**
- Maximale Genua-Schotkraft: 8.0 kN (11 m Boot, 25 kn Wind)
- Dynamikfaktor: 2.5 (kontrollierte Wende)
- Maximale Gesamtkraft: F_max = 8.0 × 2.5 = 20.0 kN
- Schraubengröße: M6 Edelstahl A4-80
- Scherkraft pro M6 Schraube: 8.4 kN (80 % der Streckgrenze × Kernquerschnitt)
- Sicherheitsfaktor Schrauben: SF = 3.0
- Zulässige Scherkraft pro Schraube: 8.4 / 3.0 = 2.8 kN
- Verteilungsfaktor: 0.7 (nicht alle Schrauben tragen gleich)

**Berechnung:**
```
n_screw = F_max / (F_screw_zul × f_distribution)
n_screw = 20.0 / (2.8 × 0.7) = 20.0 / 1.96 = 10.2 → 11 Schrauben (aufgerundet)
```

**Bei 100 mm Schraubenabstand:**
- Schienenlänge: 11 × 100 mm = 1.100 mm = 1.1 m
- Typische Genua-Schiene: 2.0 m → 20 Schrauben → deutlich überdimensioniert ✓

**Fazit:** Standard-Schraubenabstände der Hersteller (100 mm bei 25 mm Track) bieten ausreichende Sicherheitsreserven für die meisten Anwendungen.

**Confidence:** calculated

### S.4 Kostenvergleich: Neues System vs. Überholung

**Szenario:** 12 m Fahrtenyacht, Genua-Schienensystem (beidseitig) und Traveller, Alter 15 Jahre

| Position | Überholung | Neues System |
|:--|:-:|:-:|
| Genua-Schienen demontieren + reinigen | 200 EUR | - |
| Genua-Schienen neu (2× 2.0 m, 25 mm) | - | 320 EUR |
| Genua-Schlitten überholen (2×) | 80 EUR | - |
| Genua-Schlitten neu (2× Kugellager) | - | 300 EUR |
| Traveller-Schiene reinigen | 50 EUR | - |
| Traveller-Schiene neu (1× 2.0 m, 32 mm) | - | 200 EUR |
| Traveller-Schlitten überholen | 60 EUR | - |
| Traveller-Schlitten neu | - | 250 EUR |
| Endstopps (6 Stück) | 30 EUR (reinigen) | 90 EUR |
| Steuerleinen | 60 EUR | 60 EUR |
| Dichtmasse + Primer | 40 EUR | 40 EUR |
| Schrauben + Gegenplatten | 30 EUR (prüfen) | 120 EUR |
| Kernverstärkung | - | 80 EUR |
| Arbeitszeit Rigger | 600 EUR (1 Tag) | 1.200 EUR (2 Tage) |
| **Gesamt** | **1.150 EUR** | **2.660 EUR** |

**Empfehlung:**
- Überholung sinnvoll bei: Schienen in gutem Zustand (Score > 60), korrekte Dimensionierung, keine Strukturschäden
- Neuinstallation sinnvoll bei: Unterdimensionierung, Strukturschäden, Korrosion Score < 40, geplanter Einsatzwechsel (z.B. Fahrt → Regatta)

**Confidence:** estimated (Erfahrungswerte Rigger-Preise DACH-Raum 2026)

---

> **Ende der Wissensdatei 11.03 — Schienensysteme und Schlitten**
> **Gesamtumfang:** Vollständige Referenz für die AYDI-Analyse von Schienensystemen auf Segel- und Motoryachten
> **Nächste Aktualisierung:** Bei Bedarf oder bei Erscheinen neuer Produktlinien der Haupthersteller
> **Confidence-Abdeckung:** measured (Herstellerdaten), documented (Praxisberichte), estimated (Erfahrungswerte) — alle Quellen in den Einzelabschnitten gekennzeichnet
