---
title: "Wechselrichter und Landstrom"
kategorie: "22 Elektrik und Verkabelung"
unterkategorie: "22.07 Wechselrichter und Landstrom"
version: "1.0.0"
datum: "2026-05-07"
autor: "AYDI Research"
status: "validated"
confidence_quellen:
  - measured: "Hersteller-TDS, IEC 60092, ISO 13297, EN 60335"
  - documented: "Hersteller-Kataloge, Werftunterlagen, Prüfberichte, MAIB Reports"
  - estimated: "Erfahrungswerte, Werft-Konsens, Pantaenius Schadensdaten"
---

# 22.07 — Wechselrichter und Landstrom im Yachtbau: Vollständige Wissensreferenz

> **AYDI Wissensdatei 22.07** — Kategorie 22: Elektrik und Verkabelung
> **Confidence-Quelle:** measured (Hersteller-TDS, IEC 60092, ISO 13297, EN 60335), documented (Hersteller-Kataloge, Werftunterlagen, Prüfberichte), estimated (Erfahrungswerte, Werft-Konsens)
> **Letzte Aktualisierung:** 2026-05-07

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
12. [ANHANG I–R — AYDI-Integration (Pydantic v2 Modelle)](#anhang-ir--aydi-integration-pydantic-v2-modelle)

---

## 1. Einführung und Übersicht

### 1.1 AC-Strom an Bord — Notwendigkeit und Risiko

Die Verwendung von 230V-Wechselstrom (AC) an Bord von Yachten ist heute Standard auf nahezu allen Fahrtenyachten ab 10m Länge und auf vielen kleineren Booten. Die Erwartungen der Eigner an den Komfort an Bord — Kaffeemaschine, Mikrowelle, Klimaanlage, Waschmaschine, Werkzeugladegeräte, Unterhaltungselektronik — machen ein AC-Bordnetz unverzichtbar.

Gleichzeitig stellt 230V AC in der maritimen Umgebung das gefährlichste elektrische System an Bord dar. Die Kombination aus Wasser (als exzellenter Leiter), beengten metallischen Räumen, Feuchtigkeit, Salzatmosphäre und der Tatsache, dass sich Personen häufig barfuß und auf nassen Oberflächen bewegen, schafft Bedingungen, die an Land als unzulässig gelten würden.

**Statistiken und Risikobewertung:**
- Laut MAIB (Marine Accident Investigation Branch, UK) und USCG-Statistiken sind **12–18% aller schweren Elektrounfälle** an Bord auf fehlerhafte 230V-Installationen zurückzuführen
- **Electric Shock Drowning (ESD)** in Marinas — verursacht durch Leckströme ins Wasser — führt in den USA zu durchschnittlich **8–15 Todesfällen pro Jahr** (Electric Shock Drowning Prevention Association, 2024)
- **Galvanische Korrosion** durch fehlerhafte Landstromversorgung verursacht laut Pantaenius Schadensstatistik Schäden von durchschnittlich **€5.000–€25.000** pro betroffenem Boot
- **73% aller AC-Installationen** auf Bestandsyachten >15 Jahre weisen mindestens einen sicherheitsrelevanten Mangel auf (BSS-Studie 2023)
- Die häufigsten Probleme: fehlender oder defekter FI-Schutz (38%), falsche Polarität (22%), fehlende Galvanische Isolation (18%), unzureichende Kabelquerschnitte (12%)

**Confidence:** documented — basierend auf MAIB Reports, USCG Boating Safety Statistics, Pantaenius Schadensberichte, BSS (British Standards Survey) 2023.

### 1.2 Normatives Umfeld

Die AC-Installation an Bord unterliegt einem umfangreichen Normenkatalog, der sich von der Landinstallation deutlich unterscheidet:

**Primäre Normen:**

| Norm | Titel | Relevanz |
|------|-------|----------|
| IEC 60092-507 | Elektrische Installationen in Schiffen — Kleine Wasserfahrzeuge | Zentrale Installationsnorm |
| ISO 13297 | Kleine Wasserfahrzeuge — Elektrische Systeme — AC-Installationen | CE-relevant, 230V-spezifisch |
| ISO 10133 | Kleine Wasserfahrzeuge — Elektrische Systeme — DC-Installationen | Basis für DC-Seite des Inverters |
| EN 60335-2-29 | Batterieladegeräte | Ladegeräte-Funktion in Kombigeräten |
| EN 60335-1 | Sicherheit elektrischer Geräte — Allgemein | Grundnorm für Verbraucher |
| IEC 61558-2-4 | Trenntransformatoren | Spezifisch für Trenntrafos an Bord |
| ABYC E-11 | AC & DC Electrical Systems on Boats | US-Standard, relevant für Export |
| RCD 2013/53/EU | Recreational Craft Directive | CE-Pflicht für Neuboote |

**Sekundäre Normen und Richtlinien:**

| Norm / Richtlinie | Inhalt |
|--------------------|--------|
| IEC 60364-7-709 | Elektrische Anlagen — Marinas und Liegeplätze |
| EN 60309-2 | CEE-Stecker und -Steckdosen (Blau 16A, 32A) |
| ISO 8846 | Zündfunkenfreie Geräte (Inverter in Kraftstoffumgebung) |
| GL / DNV Rules | Klassifikationsgesellschaften — Yachten >24m |
| BSH-Standards | Deutsche Binnenschifffahrt, Sportboote |

### 1.3 Die zwei AC-Quellen an Bord

An Bord einer typischen Fahrtenyacht gibt es zwei grundlegende AC-Quellen:

**1. Landstrom (Shore Power):**
- Quelle: Steckdose am Steg (Marina-Verteiler)
- Spannung: 230V AC, 50Hz (EU) / 120V AC, 60Hz (USA)
- Leistung: typisch 16A (3,7kW) oder 32A (7,4kW), selten 63A
- Anschluss: CEE-Stecker blau (EU), NEMA-Stecker (USA)
- Verfügbarkeit: nur im Hafen

**2. Wechselrichter (Inverter):**
- Quelle: Batteriestrom (12V/24V/48V DC) → elektronisch gewandelt in 230V AC
- Leistung: typisch 800W–5.000W, Superyachten bis 25.000W
- Verfügbarkeit: überall (solange Batteriekapazität vorhanden)

**3. Generator (ergänzend):**
- Quelle: Dieselgenerator erzeugt direkt 230V AC
- Leistung: typisch 3–20kW, Superyachten bis 200kW
- Verfügbarkeit: überall (solange Diesel vorhanden)
- Oft in Kombination mit Inverter als Hybrid-System

### 1.4 Systemarchitektur — Übersicht

```
MARINA-STEG                    BOOT
═══════════                    ════
                    ┌─────────────────────────────────────────────┐
CEE-Steckdose       │  Landstrom-Einspeisung                      │
230V/16A ──────────►│  ├─ CEE-Einbaustecker (Deck)                │
     Kabel 25m      │  ├─ Polaritätsprüfung (LED/Relais)          │
                    │  ├─ FI-Schutzschalter 30mA (Typ A oder B)   │
                    │  ├─ Leitungsschutzschalter 16A               │
                    │  │                                           │
                    │  ├─ Option A: Galvanischer Isolator          │
                    │  │   (im PE-Leiter, blockiert Gleichstrom)   │
                    │  │                                           │
                    │  └─ Option B: Trenntrafo                     │
                    │      (galvanische Trennung aller Leiter)     │
                    │                                              │
                    │  ┌──────────────────────────────┐            │
                    │  │ Inverter/Charger (Kombigerät) │            │
                    │  │ ├─ Landstrom-Eingang 230V AC  │            │
                    │  │ ├─ Ladegerät → Batterien      │            │
                    │  │ ├─ Transfer-Relais             │            │
                    │  │ ├─ Inverter 24V DC → 230V AC  │            │
                    │  │ └─ AC-Ausgang → Verteiler      │            │
                    │  └──────────────────────────────┘            │
                    │                                              │
                    │  AC-Hauptverteiler                           │
                    │  ├─ Stromkreis 1: Steckdosen Salon           │
                    │  ├─ Stromkreis 2: Pantry (Mikrowelle etc.)   │
                    │  ├─ Stromkreis 3: Steckdosen Kabinen         │
                    │  ├─ Stromkreis 4: Warmwasserboiler           │
                    │  ├─ Stromkreis 5: Klimaanlage                │
                    │  ├─ Stromkreis 6: Waschmaschine              │
                    │  └─ Stromkreis 7: Werkstatt/Werkzeug         │
                    └─────────────────────────────────────────────┘
```

### 1.5 Bedeutung im AYDI-Analysesystem

Im Kontext der AYDI-Plattform ist die AC-Installation ein sicherheitskritischer Analysebereich, der folgende Module beeinflusst:

- **Compliance-Modul:** ISO 13297, IEC 60092, FI-Schutz, Polaritätsprüfung — Pflichtelemente für CE
- **Sicherheits-Modul:** Höchste Priorität — Personenschutz vor Stromschlag, ESD-Prävention
- **Kosten-Modul:** Inverter/Charger-Systeme sind signifikante Kostenfaktoren (typisch 3–8% der Gesamtelektrik)
- **Ergonomie-Modul:** Platzierung der Steckdosen, Schalterpanele, Zugänglichkeit der Komponenten
- **Materials-Modul:** Korrosionsrisiken durch Landstrom, Galvanische Effekte
- **Gewichts-Modul:** Inverter und Trenntrafos sind schwere Komponenten (10–60kg), Position beeinflusst Trimm
- **Produktions-Modul:** Kabelführung, Panelmontage, Komponentenzugang für Wartung

### 1.6 Einsatzprofile und typische AC-Systeme

#### 1.6.1 Hafenlieger / Wochenendsegler (8–12m)

| Parameter | Typisch |
|-----------|---------|
| AC-Bedarf | Landstrom nur im Hafen, kein Inverter |
| Landstrom-Anschluss | 16A CEE blau |
| Verbraucher | Ladegerät, Warmwasser, ggf. Heizlüfter |
| Trenntrafo | Nein (Galvanischer Isolator empfohlen) |
| FI-Schutz | 1× 30mA |
| Inverter | Keiner oder kleiner 300W für Laptop |
| Budget AC-Anlage | €500–€2.000 |

#### 1.6.2 Fahrtensegler / Küste (10–14m)

| Parameter | Typisch |
|-----------|---------|
| AC-Bedarf | Landstrom im Hafen, Inverter auf See |
| Landstrom-Anschluss | 16A CEE blau |
| Verbraucher | Landstrom: Ladegerät, Warmwasser, Mikrowelle, Steckdosen / Inverter: Laptop, Ladegeräte, ggf. Kaffeemaschine |
| Trenntrafo | Optional (empfohlen in Mittelmeer-Marinas) |
| FI-Schutz | 1–2× 30mA |
| Inverter | 1.000–2.000W Kombigerät (Inverter/Charger) |
| Budget AC-Anlage | €2.500–€6.000 |

#### 1.6.3 Blauwassersegler (12–18m)

| Parameter | Typisch |
|-----------|---------|
| AC-Bedarf | Inverter primär, Landstrom sekundär |
| Landstrom-Anschluss | 16A + ggf. Adapter 32A, Universaladapter (EU/UK/US) |
| Verbraucher | Inverter: Mikrowelle, Waschmaschine, Werkzeug, Laptop, Kaffeemaschine / Landstrom: alle + Klimaanlage, Boiler |
| Trenntrafo | Empfohlen (wechselnde Marinas weltweit, unbekannte Erdung) |
| FI-Schutz | 2–3× 30mA (getrennte Kreise) |
| Inverter | 2.000–3.000W Kombigerät (Victron MultiPlus oder äquivalent) |
| Budget AC-Anlage | €5.000–€15.000 |

#### 1.6.4 Motoryacht / Großyacht (15–24m)

| Parameter | Typisch |
|-----------|---------|
| AC-Bedarf | Generator + Inverter + Landstrom |
| Landstrom-Anschluss | 32A oder 63A CEE, ggf. Drehstrom 3× 400V |
| Verbraucher | Klimaanlage (zentral), Herd, Geschirrspüler, Waschmaschine/Trockner, Werkstatt |
| Trenntrafo | Standard (oft im Landstromeingang integriert) |
| FI-Schutz | 3–6× 30mA, selektive Staffelung mit 300mA Vorschalter |
| Inverter | 3.000–5.000W oder Quattro-System mit 2 AC-Eingängen |
| Budget AC-Anlage | €15.000–€50.000 |

#### 1.6.5 Superyacht (>24m)

| Parameter | Typisch |
|-----------|---------|
| AC-Bedarf | Primär Generator(en), Landstrom 3-phasig, Inverter als USV |
| Landstrom-Anschluss | 3× 63A–125A, 400V Drehstrom |
| Verbraucher | Vollständiger Haushalt, Klimaanlage mehrstufig, Stabilisatoren, Bugstrahler |
| Trenntrafo | Pflicht (Klasse-Anforderung DNV/GL) |
| FI-Schutz | Mehrstufig, Typ B (Gleichfehlerstrom durch Frequenzumrichter) |
| Inverter | Mehrere Quattro parallel, USV-Funktion, Lithium-ready |
| Budget AC-Anlage | €50.000–€250.000+ |

---

## 2. Grundlagen und Theorie

### 2.1 Wechselrichter — Funktionsprinzip

Ein Wechselrichter (Inverter) wandelt Gleichstrom (DC) aus der Bordbatterie in Wechselstrom (AC) um. Die grundlegende Funktionskette:

```
Batterie (12V/24V/48V DC)
  │
  ▼
DC-Eingangsfilter (EMV, Verpolschutz)
  │
  ▼
DC/DC-Wandler (Hochsetzer auf Zwischenkreisspannung ~350V DC)
  │
  ▼
H-Brücke (4 MOSFET/IGBT, gepulst per PWM)
  │
  ▼
LC-Ausgangsfilter (Sinusformung)
  │
  ▼
Ausgangsrelais (Sicherheitstrennung)
  │
  ▼
230V AC / 50Hz Sinuswelle
```

**Schlüsselstufen im Detail:**

**DC/DC-Wandler (Boost-Stufe):**
Die Batteriespannung (12V, 24V oder 48V) muss auf die Zwischenkreisspannung von ca. 350–400V DC hochgesetzt werden. Dies geschieht über einen Hochsetzsteller (Boost Converter) mit Hochfrequenz-Transformator. Die Effizienz dieser Stufe bestimmt maßgeblich den Gesamtwirkungsgrad.

**H-Brücke (Wechselrichterstufe):**
Vier Leistungshalbleiter (MOSFETs bei kleinen Leistungen, IGBTs bei großen) werden in einer H-Brücken-Konfiguration pulsbreitenmoduliert (PWM) geschaltet. Die PWM-Frequenz liegt typisch bei 16–50 kHz. Durch geeignete Modulation der Pulsbreiten entsteht nach der Filterung eine sinusförmige Ausgangsspannung.

**LC-Ausgangsfilter:**
Eine Induktivität (L) und ein Kondensator (C) filtern die PWM-Pulse und formen sie in eine glatte Sinuswelle um. Die Qualität dieses Filters bestimmt den THD (Total Harmonic Distortion) der Ausgangsspannung.

### 2.2 Reine Sinuswelle vs. Modifizierte Sinuswelle

Der entscheidende Qualitätsunterschied bei Wechselrichtern liegt in der Wellenform des Ausgangs:

**Reine Sinuswelle (True Sine Wave):**

```
     ╱╲          ╱╲
    ╱  ╲        ╱  ╲
───╱    ╲──────╱    ╲───
          ╲  ╱        ╲  ╱
           ╲╱          ╲╱
```

- THD (Total Harmonic Distortion): <3%, typisch 1,5–2,5%
- Identisch mit Netzstrom
- Alle Verbraucher funktionieren problemlos
- Keine Brummgeräusche in Audiosystemen
- Korrekte Funktion von Motoren (Pumpen, Kompressoren, Werkzeug)
- Keine Erwärmungsprobleme bei Transformator-Netzteilen
- **Standard bei allen hochwertigen Marine-Invertern**

**Modifizierte Sinuswelle (Modified Sine Wave / Trapezwelle):**

```
    ┌────┐        ┌────┐
    │    │        │    │
────┘    └────────┘    └────
              ┌────┐
              │    │
         ─────┘    └─────
```

- THD: 25–40%
- Treppenstufen-Approximation der Sinuswelle
- Probleme bei: Induktiven Lasten (Motoren brummen/überhitzen), empfindlicher Elektronik (Ladegeräte schalten ab), Audiosystemen (starkes Brummen), Dimmern (Fehlfunktion), Mikrowellen (reduzierte Leistung, Magnetron-Stress)
- **Nicht empfehlenswert für den Marineeinsatz**
- Einziger Vorteil: günstiger Preis (Faktor 3–5)

**AYDI-Empfehlung:** Ausschließlich reine Sinuswelle. Modifizierte Sinuswelle wird im Compliance-Modul als Mangel gewertet.

### 2.3 Wirkungsgrad und Verluste

Der Wirkungsgrad eines Wechselrichters variiert stark mit der Belastung:

| Belastung | Typischer Wirkungsgrad | Verlustleistung (2.000W Inverter) |
|-----------|----------------------|-----------------------------------|
| 0% (Leerlauf) | 0% (nur Eigenverbrauch) | 8–25W (Leerlaufverbrauch) |
| 5% (100W) | 75–82% | 22–33W |
| 10% (200W) | 82–88% | 27–44W |
| 25% (500W) | 88–93% | 38–68W |
| 50% (1.000W) | 91–95% | 53–99W |
| 75% (1.500W) | 92–96% | 63–130W |
| 100% (2.000W) | 90–94% | 128–222W |

**Leerlaufverbrauch — das unterschätzte Problem:**

Der Leerlaufverbrauch (No-Load Power Consumption) ist auf Yachten ein kritischer Parameter, weil der Inverter oft stundenlang ohne Last eingeschaltet bleibt. Typische Werte:

| Inverter-Typ | Leerlaufverbrauch | 24h-Verbrauch bei Leerlauf |
|--------------|-------------------|---------------------------|
| Klein (300–800W) | 5–10W | 120–240Wh = 10–20Ah/12V |
| Mittel (1.000–2.000W) | 10–20W | 240–480Wh = 10–20Ah/24V |
| Groß (2.500–5.000W) | 15–35W | 360–840Wh = 15–35Ah/24V |
| Sehr groß (>5.000W) | 25–50W | 600–1.200Wh = 25–50Ah/24V |

**Eco-Modus / Suchfunktion (Search Mode):**
Moderne Inverter bieten einen Eco-Modus, der den Inverter bei fehlender Last in einen Ruhezustand versetzt und periodisch kurze Pulse aussendet, um zu prüfen, ob eine Last angeschlossen wurde. Der Verbrauch sinkt auf 2–5W. Nachteil: Einschaltverzögerung von 0,5–3 Sekunden, problematisch für Uhren, Router, Kühlschränke mit Elektroniksteuerung.

**Confidence:** measured — basierend auf Victron TDS, Mastervolt TDS, unabhängige Tests (Practical Sailor, Yacht).

### 2.4 Überlast und Surge (Anlaufstrom)

Viele Verbraucher ziehen beim Einschalten einen deutlich höheren Strom als im Betrieb (Anlaufstrom / Inrush Current / Surge):

| Verbraucher | Nennleistung | Anlaufstrom (Faktor) | Anlaufleistung |
|-------------|-------------|---------------------|----------------|
| Kühlschrank-Kompressor | 80–150W | 5–8× | 400–1.200W |
| Klimaanlage (klein) | 500–1.000W | 3–6× | 1.500–6.000W |
| Waschmaschine (Kaltprogramm) | 200–400W | 3–5× | 600–2.000W |
| Waschmaschine (Heizung) | 2.000W | 1× (ohmsch) | 2.000W |
| Mikrowelle | 800–1.200W | 1,5–2× | 1.200–2.400W |
| Winkelschleifer | 800–1.200W | 4–8× | 3.200–9.600W |
| Bohrmaschine | 400–800W | 3–6× | 1.200–4.800W |
| Staubsauger | 600–1.200W | 2–3× | 1.200–3.600W |
| Kaffeevollautomat | 1.200–1.500W | 1× (Heizung) | 1.200–1.500W |
| Haartrockner | 1.000–2.200W | 1× (ohmsch) | 1.000–2.200W |

**Inverter-Spezifikation — Drei Leistungswerte:**

1. **Dauerleistung (Continuous):** Leistung, die unbegrenzt abgegeben werden kann
2. **30-Minuten-Leistung:** Typisch 110–120% der Dauerleistung (Temperaturmanagement)
3. **Surge/Peak (5s):** Typisch 150–200% der Dauerleistung, bei guten Invertern 200–300%

**Beispiel Victron MultiPlus 24/3000/70:**
- Dauerleistung: 2.400W (bei 25°C)
- 30 min: 2.700W
- Surge (5s): 6.000W

### 2.5 Trenntrafo (Isolation Transformer) — Prinzip und Notwendigkeit

#### 2.5.1 Das Problem: Galvanische Verbindung über den Schutzleiter

Wenn ein Boot per Landstromkabel an eine Marina-Steckdose angeschlossen wird, entsteht über den Schutzleiter (PE/Erde) eine galvanische Verbindung zwischen dem Boot und dem Erdungssystem der Marina — und über das Wasser zu allen anderen angeschlossenen Booten.

```
MARINA-VERTEILUNG                   BOOT A             BOOT B
═══════════════                     ══════             ══════

L ─────────────────── L (Phase)     L ────────────────── L
N ─────────────────── N (Neutral)   N ────────────────── N
PE ──┬────────────── PE (Erde) ──── Rumpf A    PE ──── Rumpf B
     │                                │                   │
     │                                │     WASSER        │
     ├─── Erder (Steg)               │   (Elektrolyt)    │
     │                                └───────────────────┘
     │                                   Galvanische Zelle!
     │                                   Strom fließt über
     │                                   PE zurück zum Steg
```

**Folgen der galvanischen Verbindung:**
1. **Galvanische Korrosion:** Verschiedene Metalle an verschiedenen Booten bilden über das Wasser galvanische Elemente. Der "edelste" Rumpf frisst die weniger edlen Metalle (Zinkanoden, Propeller, Saildrive) der Nachbarboote auf.
2. **Leckströme:** Defekte Isolationen an einem Boot senden Ströme über PE → Wasser → andere Boote. Diese können Korrosion massiv beschleunigen.
3. **Electric Shock Drowning (ESD):** Signifikante Leckströme im Wasser können Schwimmer lähmen (Muskelkrampf durch AC ab ca. 10mA im Wasser) — tödliche Gefahr.

#### 2.5.2 Lösung 1: Galvanischer Isolator

Ein Galvanischer Isolator (auch: Zinc Saver, Galvanic Isolator) wird in die PE-Leitung (Schutzleiter) zwischen Landstromeinspeisung und Bordnetz eingebaut.

**Funktionsprinzip:**
- Zwei antiparallel geschaltete Diodenpaare (insgesamt 4 Dioden) in Reihe im PE-Leiter
- Schwellenspannung: ca. 1,2–1,4V DC (2× Silizium-Dioden-Schwelle)
- Galvanische Gleichspannungen zwischen Booten liegen typisch bei 0,2–0,8V → werden blockiert
- AC-Fehlerströme (>1,4V Amplitude) passieren die Dioden → PE bleibt als Schutzleiter wirksam
- Varistoren parallel zu den Dioden schützen vor Überspannung

**Vorteile:**
- Günstig (€80–€300)
- Klein und leicht (0,2–0,5 kg)
- Einfache Installation (in PE-Leitung einschleifen)
- Keine Leistungsverluste im AC-System
- Blockiert galvanische Gleichströme effektiv

**Nachteile:**
- Blockiert NUR DC-Anteile, NICHT AC-Leckströme
- Kein Schutz vor AC-Korrosion durch fehlerhafte Nachbarboote
- Funktioniert nur bei kleinen galvanischen Spannungen (<1,2V)
- Bei mehreren verbundenen Booten mit unterschiedlichen Potentialen kann die Summenspannung die Schwelle überschreiten

**Anforderungen (ISO 13297 / ABYC A-28):**
- Fail-Safe: bei Diodendefekt muss PE durchverbunden bleiben (Kurzschluss-Ausfall, nicht Offenkreis)
- Monitoring-LED empfohlen (zeigt korrekten Betrieb)
- Nennstrom ≥ Hauptsicherung des Landstromanschlusses

#### 2.5.3 Lösung 2: Trenntrafo (Isolation Transformer)

Ein Trenntrafo eliminiert JEDE galvanische Verbindung zwischen Boot und Marina.

**Funktionsprinzip:**

```
LANDSTROM (Primär)              BORDNETZ (Sekundär)
═══════════════                 ══════════════════

L (Phase) ──────┐
                │  ┌─────────┐
                ├──┤ Primär  │
                │  │ Wicklung │     Kein leitender
N (Neutral) ───┤  │         │     Kontakt zwischen
                │  │ ▓▓▓▓▓▓▓│     Primär und Sekundär!
PE (Erde) ─────┤  │ ▓ Kern ▓│
               │  │ ▓▓▓▓▓▓▓│
               │  │         │     L' (Phase Bord) ──── AC-Verteiler
               │  │ Sekundär├──── N' (Neutral Bord) ── AC-Verteiler
               │  │ Wicklung │
               │  └─────────┘     PE' (Bord-Erde) ──── Rumpf/Kiel
               │                       │
               │                       └── NICHT verbunden mit Marina-PE!
               │
               └─── Marina-Erder (bleibt am Steg)
```

**Vorteile:**
- Vollständige galvanische Trennung — kein Strom zwischen Boot und Marina möglich
- Schützt vor AC- UND DC-Leckströmen
- Schützt vor umgepolten Landstromanschlüssen (Ausland!)
- Ermöglicht eigenes Bordnetz-Erdungskonzept (IT-Netz möglich)
- Höchster Schutz vor galvanischer Korrosion
- Höchster Schutz vor Electric Shock Drowning

**Nachteile:**
- Teuer (€800–€3.500)
- Schwer (15–60 kg bei 3,5kVA–10kVA)
- Groß (Volumen-Problem auf kleinen Booten)
- Eigenverbrauch (Leerlaufverluste 5–15W, Lastverluste 3–5%)
- Brummgeräusch (besonders bei mangelhafter Montage)
- Erwärmung bei hoher Last (Belüftung erforderlich)

#### 2.5.4 Vergleich: Galvanischer Isolator vs. Trenntrafo

| Kriterium | Galvanischer Isolator | Trenntrafo |
|-----------|----------------------|------------|
| Schutz vor DC-Korrosion | Ja (bis 1,2V) | Ja (vollständig) |
| Schutz vor AC-Leckströmen | Nein | Ja |
| Schutz vor ESD | Teilweise | Ja |
| Schutz vor falscher Polarität | Nein | Ja |
| Gewicht | 0,2–0,5 kg | 15–60 kg |
| Preis | €80–€300 | €800–€3.500 |
| Installation | Einfach (30 min) | Aufwändig (4–8 Std.) |
| Wartung | Keine | Jährliche Sichtprüfung |
| Leistungsverlust | 0% | 3–5% |
| Geräusch | Keines | Mögliches Brummen |
| AYDI-Empfehlung | Minimum für alle Boote | Standard ab 12m, Pflicht ab 18m |

### 2.6 FI-Schutzschalter (RCD) — Personenschutz

#### 2.6.1 Funktionsprinzip

Der Fehlerstrom-Schutzschalter (FI, auch: RCD = Residual Current Device) vergleicht den Strom im Phasenleiter (L) mit dem Strom im Neutralleiter (N). Bei einem Erdschluss (Strom fließt über eine Person oder einen Fehler zur Erde) sind die Ströme nicht mehr gleich — die Differenz ist der Fehlerstrom. Ab einem Schwellwert (typisch 30mA) schaltet der FI ab.

```
                    ┌─────────────────────┐
L ──────────────────┤  Summenstromwandler  ├────── L (zu Verbraucher)
                    │  ╔═══╗               │
                    │  ║   ║  Magnetkern   │
                    │  ║ ○ ║  Sekundär-    │
N ──────────────────┤  ║   ║  wicklung     ├────── N (zu Verbraucher)
                    │  ╚═══╝               │
                    │    │                 │
                    │    ▼                 │
                    │  Auslöse-            │
                    │  elektronik          │
                    │    │                 │
                    │    ▼                 │
                    │  Schaltschloss       │
                    └─────────────────────┘

Normal: I_L = I_N → Differenz = 0 → kein Auslösen
Fehler: I_L ≠ I_N → Differenz >30mA → Auslösung in <300ms (Typ AC)
                                     → Auslösung in <40ms (Typ A/B)
```

#### 2.6.2 FI-Typen und ihre Eignung an Bord

| Typ | Erkennt | Einsatz an Bord |
|-----|---------|-----------------|
| Typ AC | Nur sinusförmige AC-Fehlerströme | **NICHT empfohlen** — veraltet, erkennt keine Gleichfehlerströme von Schaltnetzteilen |
| Typ A | AC + pulsierende DC-Fehlerströme | **Standard** — erkennt Fehler durch Schaltnetzteile (Laptops, Ladegeräte), einfache Frequenzumrichter |
| Typ F | Wie A + Frequenzumrichter-Fehlerströme | **Empfohlen** bei Klimaanlagen mit Inverter-Kompressor |
| Typ B | Alle Fehlerstromarten inkl. reiner DC | **Empfohlen** bei DC-Ladegeräten, Wechselrichtern, PV-Einspeisung |
| Typ B+ | Wie B + Hochfrequenz bis 20kHz | **Superyachten** mit komplexen Antriebssystemen |

**Auslösestrom-Staffelung:**

| Auslösestrom | Einsatz | Bemerkung |
|-------------|---------|-----------|
| 10mA | Nassräume (Dusche, Waschbecken) | Höchster Personenschutz, aber höhere Fehlauslösungsrate |
| 30mA | Standard-Personenschutz | ISO 13297 Mindestanforderung für alle AC-Kreise an Bord |
| 100mA | Brandschutz (kein Personenschutz!) | Nur als Vorschalter für selektive Staffelung |
| 300mA | Selektiver Vorschalter | In Kombination mit nachgeschalteten 30mA-FIs |

**ISO 13297 Anforderung:**
Alle AC-Stromkreise an Bord MÜSSEN durch einen FI-Schutzschalter mit I_ΔN ≤ 30mA geschützt sein. Es gibt KEINE Ausnahmen.

#### 2.6.3 FI-Schutz in Kombination mit Trenntrafo

Bei Verwendung eines Trenntrafos wird das Bordnetz zu einem IT-Netz (ungeerdetes Netz). In einem IT-Netz funktioniert ein Standard-FI nicht, weil kein Fehlerstrom über Erde zurückfließen kann (es gibt keine Verbindung zwischen Sekundärwicklung und Erde).

**Lösung:** Der Sternpunkt der Sekundärwicklung wird über einen Widerstand oder direkt mit dem Bootsrumpf (Erde) verbunden. Dadurch wird ein TN-S-ähnliches Netz erzeugt, und der FI funktioniert korrekt.

```
Trenntrafo Sekundär:
  L' ────────────────── AC-Verteiler ── FI 30mA ── Stromkreise
  N' ──┬─────────────── AC-Verteiler
       │
       └── Verbindung zum Bootsrumpf (über Bonding-System)
           → FI funktioniert jetzt korrekt
```

### 2.7 Erdungskonzepte an Bord

#### 2.7.1 TT-Netz (Terra-Terra)

```
L ──────────────────── Verbraucher
N ──────────────────── Verbraucher
PE ────── Bootsrumpf ── Unterwasserteil (eigener Erder)
          │
          ├── NICHT verbunden mit N
          └── Erdwiderstand über Wasser: variabel (1–100 Ω)
```
- Standard bei Landstrom ohne Trenntrafo
- PE kommt vom Steg, ist mit Marina-Erdungssystem verbunden
- Vorteil: bewährtes System, FI funktioniert
- Nachteil: galvanische Verbindung zum Steg

#### 2.7.2 TN-S-Netz (nach Trenntrafo)

```
Trenntrafo:
L' ──────────────────── Verbraucher
N' ──┬─────────────── Verbraucher
     │
     └── Sternpunkt ── PE' ── Bootsrumpf
         (eine Verbindung, am Trafo)
```
- Empfohlen nach Trenntrafo
- Sternpunkt-Erdung am Trafo-Ausgang
- Keine galvanische Verbindung zum Steg
- FI funktioniert zuverlässig

#### 2.7.3 IT-Netz (isoliert, nach Trenntrafo)

```
Trenntrafo:
L' ──────────────────── Verbraucher
N' ──────────────────── Verbraucher
         KEIN Erdungsbezug!
         Erster Erdschluss → kein Strom → Betrieb läuft weiter
         Zweiter Erdschluss → Kurzschluss → Sicherung löst aus
```
- Höchste Verfügbarkeit (erster Fehler = kein Ausfall)
- Erfordert Isolationsüberwachung (Insulation Monitoring Device, IMD)
- Standard auf Schiffen (SOLAS), selten auf Yachten
- FI funktioniert NICHT → IMD + Erdschlussmelder erforderlich

### 2.8 Elektrische Sicherheit an Bord — Gefährdungsanalyse

#### 2.8.1 Körperwiderstand und Stromwirkung auf den Menschen

Der elektrische Widerstand des menschlichen Körpers variiert stark mit den Bedingungen:

| Bedingung | Körperwiderstand (Hand-Fuß) | Strom bei 230V |
|-----------|----------------------------|----------------|
| Trockene Haut, Schuhe | 50.000–100.000 Ω | 2,3–4,6 mA |
| Trockene Haut, barfuß | 10.000–20.000 Ω | 11,5–23 mA |
| Feuchte Haut, barfuß | 1.000–5.000 Ω | 46–230 mA |
| Nasse Haut, barfuß, nasser Boden | 500–1.500 Ω | 153–460 mA |
| Im Wasser (Schwimmen) | 300–800 Ω | 288–767 mA |

**Stromwirkung auf den menschlichen Körper (AC, 50Hz):**

| Stromstärke | Wirkung | Dauer bis lebensgefährlich |
|-------------|---------|---------------------------|
| 0,5–1 mA | Wahrnehmungsschwelle (Kribbeln) | — |
| 1–5 mA | Unangenehm, aber loslassen möglich | — |
| 5–10 mA | Schmerzhaft, Muskelkrampf beginnt | — |
| 10–30 mA | "Let-Go"-Schwelle überschritten, Muskelkrampf | Minuten |
| 30–50 mA | Atemnot, Bewusstlosigkeit möglich | 30s–3min |
| 50–100 mA | Herzkammerflimmern möglich | Sofort gefährlich |
| >100 mA | Herzkammerflimmern wahrscheinlich | Sofort lebensgefährlich |
| >1.000 mA (1A) | Verbrennungen, Herzstillstand | Sofort tödlich |

**Besonderheit im Wasser (ESD):**
Im Wasser reichen bereits 10–15 mA für Muskellähmung (Skelettmuskulatur). Die Person kann nicht mehr schwimmen und ertrinkt. Der Strom fließt durch den gesamten Körper (im Wasser kein lokaler Kontaktpunkt). Das Herz wird bei 10mA im Wasser noch nicht direkt betroffen, aber die Atemmuskulatur und Extremitätenmuskulatur sind gelähmt → Ertrinken.

**Warum 30mA FI-Auslösestrom:**
- 30mA liegt sicher unter der Herzkammerflimmern-Schwelle (50mA)
- Auslösezeit <300ms (Typ AC) bzw. <40ms (Typ A bei pulsierendem DC)
- Schutzkonzept: I × t < 30mA × 300ms = 9 mAs — unter dem gefährlichen Bereich
- An Bord (nasse Umgebung): FI mit 30mA ist PFLICHT, 10mA für Nassräume empfohlen

#### 2.8.2 Schutzklassen und Schutzarten

**Schutzklassen von Verbrauchern (relevant für Bordauswahl):**

| Schutzklasse | Symbol | Schutzkonzept | Eignung an Bord |
|-------------|--------|---------------|-----------------|
| Klasse 0 | — | Nur Basisisolierung, kein PE | VERBOTEN an Bord |
| Klasse I | ⏚ | Basisisolierung + Schutzleiter (PE) | Standard — PE muss vorhanden sein |
| Klasse II | ⬛⬛ | Doppelte/verstärkte Isolierung, kein PE nötig | Ideal — unabhängig von Erdung |
| Klasse III | ◇ | Schutzkleinspannung (SELV, <50V AC) | Ideal für Nassräume |

**AYDI-Empfehlung:** Klasse-II-Geräte bevorzugen (Doppelt isoliert), da unabhängig von der Qualität der Schutzleiter-Verbindung sicher. Besonders wichtig in Nassräumen und an Deck.

**Schutzarten (IP-Code) für Bord-Elektrokomponenten:**

| Bereich | Mindest-IP | Empfohlen | Begründung |
|---------|-----------|-----------|------------|
| Motorraum | IP44 | IP55 | Spritzwasser, Ölnebel, Kondenswasser |
| Salon, Kabinen | IP20 | IP21 | Tropfwasser möglich |
| Pantry | IP21 | IP44 | Spritzwasser beim Kochen/Abwaschen |
| Nasszelle (Dusche, WC) | IP44 | IP55 | Spritzwasser, Kondenswasser |
| Cockpit (überdacht) | IP44 | IP55 | Regen, Spritzwasser |
| An Deck (offen) | IP55 | IP67 | Überkommendes Wasser, Regen |
| Unterdeck/Bilge | IP44 | IP67 | Kondenswasser, mögliche Leckage |

### 2.9 Polaritätsprüfung

In vielen Ländern (insbesondere Mittelmeer, Asien, Südamerika) sind Landstromanschlüsse in Marinas fehlerhaft verdrahtet. Häufigste Fehler:

| Fehler | Häufigkeit | Risiko |
|--------|-----------|--------|
| L und N vertauscht | 15–25% | FI funktioniert nicht bei allen Fehlerszenarien, Schalter schalten N statt L → spannungsführende Kontakte bei "Aus" |
| PE fehlt (nicht angeschlossen) | 5–10% | Kein Schutzleiter → FI wirkungslos, kein Potentialausgleich |
| PE und N vertauscht | 3–5% | Dauerstrom auf PE → Korrosion, FI-Fehlfunktion |
| PE auf L | 1–2% | Rumpf unter Spannung! Lebensgefahr! |

**Pflicht-Einrichtung an Bord: Polaritätsprüfer**

Jedes Boot MUSS eine Polaritätsprüfung am Landstromeingang haben. Optionen:
1. **LED-Anzeige** (einfach, 3 LEDs: L, N, PE korrekt) — Minimum
2. **Automatisches Trennrelais** bei Fehlbelegung — empfohlen
3. **Integrierte Prüfung im Inverter/Charger** (z.B. Victron MultiPlus) — ideal

### 2.9 Leistungsfaktor und Scheinleistung

An Bord relevant bei der Dimensionierung von Trenntrafos, Generatoren und Landstromanschlüssen.

**Grundlagen:**
- **Wirkleistung P [W]:** Tatsächlich nutzbare Leistung (Wärme, mechanische Arbeit)
- **Blindleistung Q [var]:** Pendelt zwischen Quelle und induktiver/kapazitiver Last, nicht nutzbar
- **Scheinleistung S [VA]:** Geometrische Summe von P und Q: S = √(P² + Q²)
- **Leistungsfaktor cos φ:** Verhältnis P/S (1,0 = rein ohmsch, <1,0 = induktiv oder kapazitiv)

**Typische Leistungsfaktoren von Bordverbrauchern:**

| Verbraucher | cos φ | Typ | Auswirkung |
|-------------|-------|-----|------------|
| Heizung, Wasserkocher, Toaster | 1,00 | Ohmsch | Keine Blindleistung |
| Glühlampen | 1,00 | Ohmsch | Keine Blindleistung |
| Schaltnetzteile (Laptop, Ladegerät) | 0,95–0,99 | Kapazitiv | Gering |
| LED-Netzteile (billig) | 0,50–0,70 | Kapazitiv | Signifikant! |
| LED-Netzteile (PFC) | 0,95–0,99 | Kapazitiv | Gering |
| Kühlschrank-Kompressor | 0,60–0,80 | Induktiv | Hohe Blindleistung |
| Klimaanlage (konventionell) | 0,65–0,80 | Induktiv | Hohe Blindleistung |
| Klimaanlage (Inverter-Typ) | 0,90–0,98 | Gemischt | Gering |
| Waschmaschine (Waschen) | 0,50–0,70 | Induktiv | Hoch |
| Waschmaschine (Schleudern) | 0,70–0,85 | Induktiv | Mittel |
| Mikrowelle | 0,85–0,95 | Gemischt | Gering |
| Winkelschleifer | 0,80–0,90 | Induktiv | Mittel |
| Bohrmaschine | 0,75–0,85 | Induktiv | Mittel |

**Warum das wichtig ist:**
- Trenntrafos und Generatoren werden in **VA** (Scheinleistung) dimensioniert
- Ein 3.500VA-Trenntrafo liefert bei cos φ = 0,7 nur 2.450W Wirkleistung
- Inverter werden in **W** (Wirkleistung) angegeben — bei niedrigem cos φ wird der Inverter-Strom höher als erwartet
- Landstromabsicherung (z.B. 16A) begrenzt den **Strom**, nicht die Leistung → bei cos φ = 0,7 sind nur 2.576W Wirkleistung verfügbar (statt 3.680W)

### 2.10 Harmonische Oberschwingungen (THD)

**Problem an Bord:**
Nicht-lineare Verbraucher (Schaltnetzteile, VFDs, LED-Treiber, Dimmer) ziehen nicht-sinusförmige Ströme und erzeugen Oberschwingungen im Netz. Diese Oberschwingungen können:
- Trenntrafo zusätzlich erwärmen (Skin-Effekt bei Hochfrequenz)
- Generator überhitzen (auch wenn Wirkleistung unter Nennlast)
- Nullleiter überlasten (3. Harmonische addiert sich im N-Leiter!)
- Inverter-Regelung stören (bei Rückspeisung über Landstrom)

**THDv (Spannungs-Verzerrung) und THDi (Strom-Verzerrung):**

| Quelle | THDv typisch | THDi typisch |
|--------|-------------|-------------|
| Sauberes Landstromnetz | <3% | — |
| Belastete Marina-Verteilung | 3–8% | — |
| Guter Inverter (Victron, Mastervolt) | <3% | — |
| Billiger Inverter | 5–15% | — |
| Einzelner Laptop-Charger | — | 80–120% |
| LED-Treiber ohne PFC | — | 100–150% |
| VFD-Klimaanlage | — | 30–80% |

**Maßnahmen:**
1. LED-Netzteile mit Power Factor Correction (PFC) verwenden
2. Trenntrafo 20% überdimensionieren bei hohem Oberschwingungsanteil
3. K-Faktor-Transformatoren für stark belastete Installationen (Superyachten)
4. Nullleiter nie geringer dimensionieren als Phasenleiter (bei THDi >15% sogar größer!)

### 2.11 Kabelquerschnitte und Absicherung im AC-Netz

#### 2.9.1 AC-Kabelquerschnitte (230V, 50Hz)

| Stromkreis | Max. Strom | Min. Querschnitt | Empfohlen | Kabeltyp |
|------------|-----------|-------------------|-----------|----------|
| Landstrom-Zuführung 16A | 16A | 2,5 mm² | 4,0 mm² | H07RN-F 3G2,5 oder 3G4,0 |
| Landstrom-Zuführung 32A | 32A | 6,0 mm² | 6,0 mm² | H07RN-F 3G6,0 |
| Steckdosen-Stromkreis | 16A | 2,5 mm² | 2,5 mm² | Marine-Rundkabel 3×2,5 |
| Licht-Stromkreis | 10A | 1,5 mm² | 1,5 mm² | Marine-Rundkabel 3×1,5 |
| Einzelgerät Klimaanlage | 16A | 2,5 mm² | 4,0 mm² | Marine-Rundkabel 3×2,5 |
| Einzelgerät Herd/Ofen | 16A | 2,5 mm² | 2,5 mm² | Marine-Rundkabel 3×2,5 |
| Inverter → AC-Verteiler | je nach Inverter | min. 4,0 mm² | 6,0 mm² | Marine-Rundkabel 3×4,0 oder 3×6,0 |

**Kabelanforderungen marine (ISO 13297):**
- Flammwidrig (IEC 60332-1 oder -3)
- Ölbeständig
- UV-beständig (bei Verlegung an Deck)
- Feuchtigkeitsbeständig
- Verzinnte Kupferlitzen (marine-grade)
- Farbcodierung: L = braun, N = blau, PE = grün-gelb

#### 2.9.2 DC-Kabelquerschnitte (Inverter-Eingangsseite)

Die DC-Seite des Inverters führt extrem hohe Ströme! Beispielrechnung:

```
Inverter: 3.000W / 24V = 125A DC (Dauerlast)
Surge: 6.000W / 24V = 250A DC (Anlauf, 5s)
+ 10% Verluste: 137A / 275A

Bei 2m Kabellänge, max. 3% Spannungsabfall:
  U_drop = 0,03 × 24V = 0,72V
  R_max = 0,72V / 275A = 0,0026 Ω
  Querschnitt = ρ × 2 × L / R = 0,0175 × 2 × 2 / 0,0026 = 27 mm²
  → 35 mm² verwenden (nächste Standardgröße)

Bei 4m Kabellänge:
  → 70 mm² verwenden
```

**DC-Kabelquerschnitt-Tabelle (Inverter-Eingang, max. 3% Spannungsabfall):**

| Inverter-Leistung | 12V-System | 24V-System | 48V-System |
|-------------------|-----------|-----------|-----------|
| 800W, 2m | 25 mm² | 16 mm² | 6 mm² |
| 1.600W, 2m | 50 mm² | 25 mm² | 10 mm² |
| 2.000W, 2m | 70 mm² | 35 mm² | 16 mm² |
| 3.000W, 2m | 95 mm² | 50 mm² | 25 mm² |
| 5.000W, 2m | — | 70 mm² | 35 mm² |
| 3.000W, 4m | — | 95 mm² | 50 mm² |
| 5.000W, 4m | — | 120 mm² | 70 mm² |

**AYDI-Regel:** DC-Kabel zum Inverter so kurz wie möglich! Inverter direkt neben der Batterie montieren (max. 2m empfohlen, max. 4m akzeptabel). Sicherung direkt am Batteriepol.

---

## 3. Typenübersicht

### 3.1 Stand-Alone-Inverter

Ein reiner Wechselrichter ohne integriertes Ladegerät. Wandelt DC in AC, hat keinen AC-Eingang für Landstrom.

**Einsatzgebiet:**
- Boote, die bereits ein separates Ladegerät haben
- Nachrüstung auf kleinen Booten
- Redundanz (zweiter Inverter nur für kritische Verbraucher)

**Typische Spezifikationen:**

| Parameter | Klein | Mittel | Groß |
|-----------|-------|--------|------|
| Leistung | 300–800W | 1.000–2.000W | 2.500–5.000W |
| Eingangsspannung | 12V | 12V/24V | 24V/48V |
| Gewicht | 2–5 kg | 5–12 kg | 12–25 kg |
| Preis | €200–€500 | €500–€1.500 | €1.500–€3.500 |
| THD | <3% | <3% | <3% |
| Wirkungsgrad (peak) | 90–92% | 92–95% | 93–96% |
| Leerlauf | 5–10W | 8–15W | 12–25W |
| Surge (5s) | 2× | 2× | 2× |

**Beispiele:**
- Victron Phoenix 12/800 (800VA, 12V, reiner Sinus)
- Mastervolt Mass Sine 12/1200 (1.200W, 12V)
- Victron Phoenix 24/3000 (3.000VA, 24V)

### 3.2 Kombigeräte — Inverter/Charger

Die bei weitem populärste Lösung für Yachten. Vereint Inverter UND Ladegerät in einem Gerät, mit automatischem Transfer-Relais zwischen Landstrom und Inverter-Betrieb.

**Funktionsmodi:**

| Modus | Beschreibung |
|-------|-------------|
| **Inverter** | Batterie → 230V AC (kein Landstrom angeschlossen) |
| **Charger** | Landstrom → Batterie laden (Landstrom angeschlossen, Inverter aus) |
| **Pass-Through** | Landstrom → direkt zu Verbrauchern + Laden (Inverter aus) |
| **Assist (PowerAssist)** | Landstrom + Inverter parallel (Landstrom reicht nicht aus, Inverter unterstützt) |
| **UPS** | Unterbrechungsfreie Umschaltung bei Landstromausfall (<20ms) |

**PowerAssist / PowerBoost — Schlüsselfunktion:**

Wenn der Landstromanschluss begrenzt ist (z.B. 6A / 1.380W in europäischen Marinas), aber der momentane Verbrauch höher liegt (Wasserkocher + Ladegerät + Warmwasser = 3.500W), unterstützt der Inverter automatisch aus der Batterie. Der Landstrom-Eingangsstrom wird begrenzt (konfigurierbar), und der Inverter ergänzt die Differenz.

```
Verbraucher benötigen: 3.500W
Landstrom liefert max: 1.380W (6A × 230V)
Inverter ergänzt:      2.120W aus Batterie
═══════════════════════════════════════════
Ergebnis: Keine Sicherung fliegt am Steg!
```

**Typische Spezifikationen Kombigeräte:**

| Parameter | Mittel | Groß | Sehr groß |
|-----------|--------|------|-----------|
| Inverter-Leistung | 1.200–2.000W | 2.000–3.000W | 3.000–5.000W |
| Charger-Strom | 30–50A | 50–70A | 70–120A |
| Eingangsspannung | 12V/24V | 24V | 24V/48V |
| AC-Eingang | 1× (16A) | 1× (16/32A) | 1–2× (32/50A) |
| Transfer-Relais | Ja, 16A | Ja, 30A | Ja, 50A |
| Gewicht | 10–18 kg | 15–25 kg | 25–45 kg |
| Preis | €1.000–€2.500 | €2.000–€4.000 | €3.500–€6.000 |
| UPS-Funktion | Ja (<20ms) | Ja (<20ms) | Ja (<20ms) |
| PowerAssist | Optional | Ja | Ja |

### 3.3 Trenntrafo (Isolation Transformer)

Separates Gerät zur galvanischen Trennung des Landstromnetzes vom Bordnetz.

**Bauformen:**

| Bauform | Einsatz | Gewicht/kVA | Preis/kVA |
|---------|---------|-------------|-----------|
| Konventionell (EI-Kern) | Preiswert, schwer, brummt | 8–10 kg/kVA | €200–€250/kVA |
| Ringkern (Toroid) | Leicht, leise, teurer | 4–6 kg/kVA | €300–€400/kVA |
| C-Kern | Kompromiss | 6–8 kg/kVA | €250–€350/kVA |

**Dimensionierung:**
- Nennleistung ≥ Landstrom-Absicherung × 230V
- 16A → 3.680VA → **mindestens 3,5kVA Trafo**
- 32A → 7.360VA → **mindestens 7,5kVA Trafo**
- Überdimensionierung +20% empfohlen (Wärme, Magnetisierungsstrom)

**Wichtige Parameter:**

| Parameter | Anforderung |
|-----------|-------------|
| Isolationsspannung Primär/Sekundär | ≥ 3.750V AC (IEC 61558-2-4) |
| Schutzart | Min. IP23, besser IP44 |
| Temperaturklasse | Min. Klasse F (155°C), besser H (180°C) |
| Leerlaufverluste | <1% der Nennleistung |
| Kurzschlussspannung | 3–5% (begrenzt Kurzschlussstrom) |
| Schirm zwischen Wicklungen | Empfohlen (EMV, Ableitstrom-Reduktion) |

### 3.4 Galvanischer Isolator

Kompaktes Gerät im PE-Leiter des Landstromkabels.

**Bauformen und Generationen:**

| Generation | Technik | Schutzpegel |
|------------|---------|-------------|
| Gen 1 (passiv) | 2 Diodenpaare antiparallel | Blockiert DC bis 1,2V |
| Gen 2 (aktiv, kapazitiv) | Dioden + Kondensator | Blockiert DC, reduziert AC-Leckstrom |
| Gen 3 (überwacht) | Dioden + Monitoring + Fail-Safe | Blockiert DC, zeigt Status, meldet Fehler |

**Typische Spezifikationen:**

| Parameter | Gen 2 (Standard) | Gen 3 (Premium) |
|-----------|------------------|-----------------|
| Nennstrom | 32A / 64A | 32A / 64A |
| DC-Blockierung | bis 1,4V | bis 1,4V |
| AC-Durchlassspannung | >1,4V peak | >1,4V peak |
| Überspannungsschutz | Varistoren | Varistoren + TVS |
| Fail-Safe | Kurzschluss bei Diodendefekt | Kurzschluss + Alarm |
| Monitoring | Keine LED | Status-LED, Alarmkontakt |
| Gewicht | 0,2–0,4 kg | 0,3–0,6 kg |
| Preis | €80–€180 | €150–€350 |

### 3.5 Frequenzumrichter (Variable Frequency Drive, VFD)

Spezialgeräte zur Steuerung von AC-Motoren (Klimaanlagen-Kompressoren, Pumpen) mit variabler Drehzahl. Auf Yachten relevant bei:
- Inverter-Klimaanlagen (sehr energieeffizient, bis 40% Energieersparnis gegenüber On/Off-Kompressor)
- Hydraulikpumpen für Stabilisatoren (Naiad, Seakeeper)
- Wassermacher-Hochdruckpumpen (Energy Recovery)
- Elektrische Bugstrahler (neuere Modelle mit VFD für proportionale Steuerung)

**Funktionsprinzip VFD:**
```
AC Eingang (230V, 50Hz)
  │
  ▼
Gleichrichter → DC-Zwischenkreis (~325V DC)
  │
  ▼
IGBT-Wechselrichter → Variable Frequenz und Spannung
  │
  ▼
Motor → Variable Drehzahl (proportional zur Frequenz)
```

**Besonderheit:** VFDs erzeugen Gleichfehlerströme, die Standard-FIs Typ A nicht erkennen → FI Typ B oder Typ F erforderlich.

**EMV-Problematik:** VFDs sind starke EMV-Emitter (hochfrequente Schaltflanken). Maßnahmen:
- Geschirmtes Motorkabel (min. 2m vom Inverter/Charger entfernt führen)
- Ferritkerne auf Motor- und Versorgungsleitung
- EMV-Ausgangsfilter am VFD (du/dt-Filter oder Sinusfilter)
- Getrennte Kabelführung von Signal-/Datenkabeln

**Typische VFD-Anwendungen an Bord:**

| Anwendung | Typische Leistung | VFD-Typ | FI-Anforderung |
|-----------|------------------|---------|----------------|
| Klimaanlage (DC-Inverter) | 500–2.000W | Integriert im Außengerät | FI Typ F oder B |
| Wassermacher HP-Pumpe | 200–800W | Extern (Schenker, Spectra) | FI Typ A (oft DC-Seite) |
| Hydraulikpumpe Stabilisator | 1.000–5.000W | Extern | FI Typ B |
| Bugstrahler (elektrisch) | 3.000–10.000W | Integriert | FI Typ B |
| Lüfter/Ventilation | 50–500W | Extern oder EC-Motor | FI Typ A |

**Wechselwirkung mit Inverter/Charger:**
Wenn ein VFD über einen Inverter/Charger gespeist wird, muss der Inverter die spezielle Lastcharakteristik berücksichtigen:
- VFDs ziehen nicht-sinusförmige Ströme (hoher Crest-Faktor)
- Rückspeise-Effekte bei schnellem Abbremsen des Motors
- THDi (Strom-Oberschwingungen) kann 80–120% betragen
- Inverter muss mind. 30% größer dimensioniert werden als die VFD-Nennleistung
- Victron MultiPlus/Quattro: bewährt mit VFD-Lasten, Firmware 4.70+ empfohlen

### 3.6 Generator-Inverter-Kombination (Hybrid-System)

Auf größeren Yachten wird häufig ein Diesel-Generator mit einem Inverter/Charger kombiniert:

**Betriebsstrategie:**

```
Szenario 1 — Hafen (Landstrom verfügbar):
  Landstrom → Inverter/Charger im Charger-Modus → Batterien laden
  Landstrom → Pass-Through → AC-Verbraucher

Szenario 2 — Ankerliegen (kleine Last, <30% Inverter-Kapazität):
  Batterien → Inverter → AC-Verbraucher (Laptop, Kühlschrank, Licht)
  Generator AUS → Stille, kein Diesel

Szenario 3 — Ankerliegen (große Last):
  Generator → Inverter/Charger AC-Eingang 2 → Charger → Batterien
  Generator → Pass-Through → AC-Verbraucher (Klimaanlage, Waschmaschine)
  Nach 1–2h: Generator AUS, Inverter übernimmt

Szenario 4 — Motor läuft (Fahrt):
  Lichtmaschine → Batterien laden
  Batterien → Inverter → AC-Verbraucher
  Kein Generator nötig (bei ausreichender Lichtmaschine)
```

### 3.7 Automatische Transferschalter (ATS)

Für Installationen mit drei AC-Quellen (Landstrom, Generator, Inverter) gibt es automatische Transferschalter, die die Priorität und Umschaltung verwalten.

**Funktionslogik:**

```
Priorität 1: Landstrom (wenn verfügbar und Spannung/Frequenz OK)
  └── Wenn verfügbar → Charger-Modus, AC Pass-Through
  └── Wenn nicht → weiter zu Priorität 2

Priorität 2: Generator (wenn gestartet und stabil)
  └── Wenn verfügbar → Charger-Modus, AC Pass-Through
  └── Wenn nicht → weiter zu Priorität 3

Priorität 3: Inverter (immer verfügbar, solange Batterie geladen)
  └── Inverter-Modus → AC aus Batterie
```

Bei Victron Quattro ist diese Logik bereits integriert (AC-In 1 = Landstrom, AC-In 2 = Generator). Bei anderen Systemen ist ein externer ATS erforderlich.

**Externe ATS-Lösungen:**

| Hersteller | Modell | Eingänge | Umschaltzeit | Preis (ca.) |
|------------|--------|----------|-------------|-------------|
| ABB | OTM_C | 2 | 100ms (mechanisch) | €400–€800 |
| Philippi | STV | 3 | 50ms (elektronisch) | €600–€1.200 |
| Mastervolt | AC Master Switch | 2 | <20ms | €300–€500 |
| Blue Sea Systems | ML-Serie | 2 | Manuell (Drehschalter) | €200–€400 |

**Umschaltlogik beachten:**
- Mechanische Schalter: keine Parallelschaltung der Quellen (Break-Before-Make)
- Elektronische Schalter: können kurzzeitig parallel schalten (Make-Before-Break) — nur bei phasensynchronen Quellen!
- Bei Inverter/Charger mit eingebautem Transfer-Relais (Victron, Mastervolt): kein externer ATS nötig

### 3.8 Landstrom-Anschlusskabel und CEE-Stecker

Das Landstromkabel ist die physische Verbindung zwischen Marina und Boot. Es gehört zu den am häufigsten vernachlässigten Komponenten der AC-Installation.

**CEE-Stecker und -Buchsen nach EN 60309-2:**

| Typ | Farbe | Spannung | Strom | Pole | Einsatz |
|-----|-------|----------|-------|------|---------|
| CEE 16A 2P+E | Blau | 230V 1~ | 16A | 3 | Standard-Yacht bis 14m |
| CEE 32A 2P+E | Blau | 230V 1~ | 32A | 3 | Größere Yachten, 14–20m |
| CEE 16A 3P+N+E | Rot | 400V 3~ | 16A | 5 | Drehstrom, selten auf Yachten |
| CEE 32A 3P+N+E | Rot | 400V 3~ | 32A | 5 | Motoryachten 20–24m |
| CEE 63A 3P+N+E | Rot | 400V 3~ | 63A | 5 | Große Yachten, Superyachten |
| CEE 125A 3P+N+E | Rot | 400V 3~ | 125A | 5 | Superyachten >30m |

**Kabel-Anforderungen:**

| Parameter | 16A | 32A | 63A (3~) |
|-----------|-----|-----|----------|
| Min. Querschnitt | 2,5 mm² | 6,0 mm² | 16 mm² |
| Kabeltyp | H07RN-F 3G2,5 | H07RN-F 3G6,0 | H07RN-F 5G16 |
| Max. Länge (3% Spannungsabfall) | 43m | 52m | 70m |
| Gewicht/m | 0,22 kg/m | 0,45 kg/m | 1,8 kg/m |
| Preis/m | €3–€5 | €6–€10 | €20–€30 |
| Mindest-Biegeradius | 6× Außendurchmesser | 6× Außendurchmesser | 8× Außendurchmesser |

**Häufige Fehler bei Landstromkabeln:**
1. **Kabeltrommel nicht abgewickelt** → Überhitzung, Brandgefahr (besonders bei Dauerlast >50%)
2. **Kabel über scharfe Kanten geführt** → Isolation beschädigt → Erdschluss
3. **Billiges Baumarkt-Verlängerungskabel statt marine H07RN-F** → nicht ölbeständig, nicht UV-beständig
4. **Adapter ohne Erdleiter** → kein Schutzleiter → lebensgefährlich
5. **Nasse Steckerverbindungen** → Korrosion der Kontakte → Übergangswiderstand → Erwärmung
6. **Kabel durch Cockpit-Abfluss geführt** → Quetschung, Wassereintritt

**AYDI-Prüfpunkte:**
- Kabeltyp korrekt (H07RN-F oder gleichwertig)?
- Querschnitt ausreichend für Absicherung?
- CEE-Stecker und -Buchse ohne Beschädigung?
- Deckseinbaustecker mit Schraubkappe und Dichtung?
- Kabelweg trocken und vor mechanischer Beschädigung geschützt?

### 3.8 AC-Verteilertafel

Die AC-Verteilertafel ist das zentrale Schaltpanel für alle 230V-Stromkreise an Bord.

**Aufbau einer normgerechten AC-Verteilertafel:**

```
EINSPEISUNG (von Landstrom/Inverter)
  │
  ▼
┌──────────────────────────────────────────┐
│  AC-VERTEILERTAFEL                       │
│                                          │
│  ┌─ Hauptschalter (2-polig, L+N) ──────┐│
│  │                                      ││
│  ├─ FI/RCD 30mA Typ A ─────────────────┤│
│  │  │                                   ││
│  │  ├─ LS B16A — Steckdosen Salon       ││
│  │  ├─ LS B16A — Steckdosen Kabinen     ││
│  │  ├─ LS B16A — Pantry                 ││
│  │  ├─ LS B16A — Warmwasserboiler       ││
│  │  └─ LS B10A — Beleuchtung AC         ││
│  │                                      ││
│  ├─ FI/RCD 30mA Typ F ─────────────────┤│
│  │  │                                   ││
│  │  ├─ LS B16A — Klimaanlage            ││
│  │  └─ LS B16A — Waschmaschine          ││
│  │                                      ││
│  ├─ Voltmeter (Eingangsspannung)        ││
│  ├─ Amperemeter (Gesamtstrom)           ││
│  └─ Polaritätsanzeige (3 LEDs)          ││
│                                          │
└──────────────────────────────────────────┘
```

**Anforderungen (ISO 13297):**
- Alle Automaten und FIs müssen 2-polig schalten (L+N gleichzeitig)
- Beschriftung aller Stromkreise in der Sprache des Erstnutzers
- Schutzart mind. IP20, in Nassräumen IP44
- Zugang ohne Werkzeug möglich
- Montage in trockener, belüfteter Umgebung
- Kabeleinführungen abgedichtet (keine offenen Durchführungen)

**Qualitätsmerkmale (AYDI-Bewertung):**

| Merkmal | Basis (Score 50) | Gut (Score 75) | Exzellent (Score 95) |
|---------|-----------------|----------------|---------------------|
| Beschriftung | Handschrift | Gedruckte Labels | Gravierte Frontplatte |
| Kabelführung | Lose, teilweise sichtbar | Gebündelt, Kabelbinder | Kabelkanäle, perfekt sortiert |
| Komponentenqualität | Baumarkt-Ware | Markenhersteller (ABB, Hager) | Marine-spezifisch (Blue Sea, Philippi) |
| Schutzart | IP20 | IP44 (Nassbereich) | IP65 (Cockpit/Deck) |
| Messinstrumente | Keine | LED-Kontrollleuchten | Digital-Anzeige V/A/Hz |
| Reserve-Positionen | Keine | 1–2 freie Plätze | 3+ freie Plätze mit Vorbereitung |

### 3.9 Installationsrichtlinien und Best Practices

#### 3.9.1 Inverter-Montage

**Einbauort-Kriterien (Prioritätsreihenfolge):**
1. **Nähe zur Batterie** — max. 2m empfohlen (DC-Kabel kurz halten)
2. **Trockener, belüfteter Raum** — kein Spritzwasser, keine Kondenswasser-Gefahr
3. **Zugänglichkeit** — LED-Status sichtbar, Schalter erreichbar, Wartung möglich
4. **Vibrations- und wärmearm** — nicht direkt auf Motor-Schotten
5. **Nicht im Kraftstoffbereich** — oder ISO 8846 zertifiziertes Gerät
6. **Vertikal montiert** — Lüftungsschlitze oben und unten frei (Kamineffekt)

**Mindestabstände:**

| Seite | Min. Abstand | Begründung |
|-------|-------------|------------|
| Oben | 200mm | Warmluft-Austritt |
| Unten | 50mm | Kaltluft-Eintritt |
| Links/Rechts | 50mm | Keine Wärmestau |
| Vorne | 150mm | Bedienelemente, LED-Sicht |
| Hinten | 30mm (Wand-Montage) | Kabel-Biegeradius |

#### 3.9.2 DC-Verkabelung zum Inverter

**Kritische Punkte:**
1. Sicherung so nah wie möglich am Batteriepol (max. 200mm)
2. Plus- und Minuskabel parallel führen (EMV-Reduktion)
3. Kabelschuhe: vergoldete oder verzinnte Ringkabelschuhe, vercrimpt UND verlötet
4. Schraubverbindungen: Drehmoment nach Herstellerangabe, Federring oder Nordlock
5. Kabel durch Schotten: Kabeldurchführungen mit Kantenschutz (keine scharfen Kanten!)
6. Kabelkennzeichnung: Plus = rot, Minus = schwarz/blau, mit Beschriftung an beiden Enden

**Sicherungswahl DC:**

| Sicherungstyp | Einsatz | Vorteil | Nachteil |
|---------------|---------|---------|----------|
| ANL-Sicherung | bis 500A | Günstig, einfach | Einmal-Auslösung, kein Schalter |
| MEGA-Fuse | bis 500A | Kompakt, time-delay | Einmal-Auslösung |
| MIDI-Fuse | bis 200A | Klein, preiswert | Einmal-Auslösung |
| NH-Sicherung | bis 630A | Industriestandard, zuverlässig | Groß, teuer |
| DC-Leitungsschutzschalter | bis 125A | Wiedereinschaltbar | Teuer, begrenzte Stromstärke |
| Victron Lynx Shunt / Distributor | bis 500A | Integriert, MEGA-Fuse | System-spezifisch |

#### 3.9.3 AC-Verkabelung

**Kabelverlegung (ISO 13297 / IEC 60092-507):**
- Marine-Rundkabel verwenden (verzinnte Litzen, flammwidrig)
- Mindestbiegeradius: 6× Außendurchmesser
- Befestigung alle 300mm (horizontal) bzw. 400mm (vertikal)
- Kabel nicht durch Bilge oder Kraftstofftanks führen
- AC- und DC-Kabel getrennt führen (min. 50mm Abstand oder Trennsteg)
- Kabel NICHT unter Bodenbrettern ohne Schutzrohr/Kabelkanal
- Durchführungen durch Schotten: Kabeldurchführung mit Zugentlastung
- Farben: L = braun, N = blau, PE = grün-gelb (NICHT abweichen!)

**Steckdosen an Bord:**
- Nur Schutzkontakt-Steckdosen (CEE 7/4 oder 7/7, "Schuko")
- In Nassräumen: IP44 mit Klappdeckel
- An Deck/Cockpit: IP56 mit verschraubbarem Deckel
- Einbauhöhe: min. 300mm über Bodenniveau (Spritzwasser)
- Max. 6 Steckdosen pro Stromkreis (16A)
- Keine Mehrfachsteckdosen als feste Installation

---

## 4. Produktlinien und Spezifikationen

### 4.1 Victron Energy

Victron Energy (Almere, Niederlande, gegr. 1975) ist der dominierende Hersteller im Yacht-Bereich für Inverter/Charger-Systeme. Bekannt für robuste Hardware, offenes Ökosystem (VE.Bus, VE.Direct, VE.Can) und exzellente Dokumentation.

#### 4.1.1 Victron Phoenix Inverter (Stand-Alone)

Reine Wechselrichter ohne Ladefunktion. Ideal als Ergänzung oder für einfache Installationen.

**Phoenix Inverter VE.Direct Serie:**

| Modell | Spannung | Dauerleistung | Peak (5s) | Leerlauf | Gewicht | Preis (ca.) |
|--------|----------|--------------|-----------|----------|---------|-------------|
| Phoenix 12/250 | 12V | 200W | 400W | 4W | 1,4 kg | €130 |
| Phoenix 12/500 | 12V | 400W | 900W | 5W | 2,4 kg | €180 |
| Phoenix 12/800 | 12V | 650W | 1.500W | 8W | 4,4 kg | €300 |
| Phoenix 12/1200 | 12V | 1.000W | 2.200W | 10W | 6,0 kg | €420 |
| Phoenix 24/500 | 24V | 400W | 900W | 5W | 2,4 kg | €180 |
| Phoenix 24/800 | 24V | 650W | 1.500W | 8W | 4,0 kg | €280 |
| Phoenix 24/1200 | 24V | 1.000W | 2.200W | 10W | 5,5 kg | €400 |

**Phoenix Inverter Smart Serie (größere Modelle):**

| Modell | Spannung | Dauerleistung | Peak (5s) | Leerlauf | Gewicht | Preis (ca.) |
|--------|----------|--------------|-----------|----------|---------|-------------|
| Phoenix 12/1600 | 12V | 1.300W | 3.000W | 12W | 7,5 kg | €550 |
| Phoenix 12/3000 | 12V | 2.400W | 6.000W | 18W | 12 kg | €900 |
| Phoenix 24/1600 | 24V | 1.300W | 3.000W | 12W | 7,0 kg | €500 |
| Phoenix 24/3000 | 24V | 2.400W | 6.000W | 15W | 10,5 kg | €800 |
| Phoenix 24/5000 | 24V | 4.000W | 10.000W | 25W | 20 kg | €1.500 |
| Phoenix 48/3000 | 48V | 2.400W | 6.000W | 15W | 10,5 kg | €800 |
| Phoenix 48/5000 | 48V | 4.000W | 10.000W | 22W | 18 kg | €1.400 |

**Gemeinsame Merkmale aller Phoenix:**
- Reine Sinuswelle, THD <3%
- Eco-Modus (Suchfunktion)
- Bluetooth (Smart-Modelle) → VictronConnect App
- VE.Direct Kommunikation → GX-Geräte (Cerbo GX, Touch 50/70)
- Temperaturkompensation (mit optionalem Sensor)
- Kurzschlussschutz, Überlastschutz, Übertemperaturschutz, Unterspannungsabschaltung

#### 4.1.2 Victron MultiPlus (Inverter/Charger)

Das Flaggschiff für Yachten. Kombiniert Inverter, Ladegerät und Transfer-Schalter mit PowerAssist.

**MultiPlus-II Serie (aktuelle Generation):**

| Modell | Spannung | Inverter | Charger | Peak (5s) | Leerlauf | Gewicht | Preis (ca.) |
|--------|----------|---------|---------|-----------|----------|---------|-------------|
| MultiPlus-II 12/3000/120 | 12V | 2.400W | 120A | 6.000W | 18W | 18,5 kg | €1.600 |
| MultiPlus-II 24/3000/70 | 24V | 2.400W | 70A | 6.000W | 15W | 16 kg | €1.400 |
| MultiPlus-II 24/5000/120 | 24V | 4.000W | 120A | 10.000W | 22W | 30 kg | €2.500 |
| MultiPlus-II 48/3000/35 | 48V | 2.400W | 35A | 6.000W | 15W | 15 kg | €1.300 |
| MultiPlus-II 48/5000/70 | 48V | 4.000W | 70A | 10.000W | 20W | 27 kg | €2.200 |
| MultiPlus-II 48/8000/110 | 48V | 6.400W | 110A | 16.000W | 30W | 40 kg | €3.500 |
| MultiPlus-II 48/10000/140 | 48V | 8.000W | 140A | 20.000W | 35W | 50 kg | €4.500 |

**Schlüsselfunktionen MultiPlus-II:**
- **PowerAssist:** Landstrombegrenzung konfigurierbar, Inverter ergänzt bei Bedarf
- **UPS-Funktion:** Umschaltzeit <20ms, unterbrechungsfrei für IT-Equipment
- **Parallelschaltung:** Bis zu 6 Geräte parallel für mehr Leistung
- **Dreiphasen-Betrieb:** 3 Geräte konfigurierbar als L1/L2/L3
- **VE.Bus-Kommunikation:** Integration in Victron-Ökosystem (GX, MPPT, BMV/SmartShunt)
- **Programmierbar:** VEConfigure Software (Windows) für detaillierte Einstellungen
- **Lithium-kompatibel:** BMS-gesteuerte Abschaltung über VE.Bus BMS
- **Anti-Islanding:** Bei Netzausfall trennt sich der Inverter vom Landstromnetz

#### 4.1.3 Victron Quattro (Dual AC-Eingang)

Wie MultiPlus, aber mit zwei unabhängigen AC-Eingängen. Ideal für Yachten mit Generator + Landstrom.

| Modell | Spannung | Inverter | Charger | AC-Ein 1 | AC-Ein 2 | Gewicht | Preis (ca.) |
|--------|----------|---------|---------|-----------|----------|---------|-------------|
| Quattro-II 24/5000/120 | 24V | 4.000W | 120A | 50A | 50A | 35 kg | €3.200 |
| Quattro-II 48/5000/70 | 48V | 4.000W | 70A | 50A | 50A | 30 kg | €2.800 |
| Quattro-II 48/8000/110 | 48V | 6.400W | 110A | 100A | 100A | 45 kg | €4.200 |
| Quattro-II 48/10000/140 | 48V | 8.000W | 140A | 100A | 100A | 55 kg | €5.200 |
| Quattro-II 48/15000/200 | 48V | 12.000W | 200A | 100A | 100A | 75 kg | €7.000 |

**Zwei AC-Eingänge — Strategie:**
- AC-In 1: Landstrom (Priorität 1)
- AC-In 2: Generator (Priorität 2)
- Automatische Umschaltung zwischen den Quellen
- Wenn keine AC-Quelle → Inverter-Betrieb aus Batterie

#### 4.1.4 Victron Zubehör und Systemkomponenten

| Komponente | Funktion | Preis (ca.) |
|------------|---------|-------------|
| Cerbo GX | System-Gateway, Monitoring, VRM-Portal | €350 |
| GX Touch 50 | 5" Touchscreen-Display für Cerbo GX | €250 |
| GX Touch 70 | 7" Touchscreen-Display für Cerbo GX | €350 |
| SmartShunt 500A | Batteriemonitor | €120 |
| Autotransformer 120/240V | Spannungsanpassung (USA) | €500 |
| Digital Multi Control | Fernbedienung für MultiPlus/Quattro | €80 |
| VE.Bus BMS V2 | Lithium-BMS-Interface | €100 |

#### 4.1.5 Victron Isolation Transformer

| Modell | Leistung | Gewicht | Typ | Auto-Anpassung | Preis (ca.) |
|--------|----------|---------|-----|----------------|-------------|
| Isolation Transformer 3600W | 3.600W | 18 kg | Ringkern | 115/230V Auto | €900 |
| Isolation Transformer 7000W | 7.000W | 33 kg | Ringkern | 115/230V Auto | €1.600 |

**Besonderheit:** Auto-Ranging Eingang (115V oder 230V automatisch erkannt). Ausgang immer 230V (oder 120V, konfigurierbar). Ideal für Langfahrt mit wechselnden Landstrom-Spannungen.

#### 4.1.6 Victron Galvanic Isolator

| Modell | Nennstrom | Fail-Safe | Monitoring | VE.Direct | Preis (ca.) |
|--------|----------|-----------|------------|-----------|-------------|
| VDI-16 | 16A | Ja | LED | Nein | €65 |
| VDI-32 | 32A | Ja | LED | Nein | €85 |
| VDI-64 | 64A | Ja | LED | Nein | €140 |

#### 4.1.7 Victron-Ökosystem — Gesamtintegration

Das Victron-Ökosystem ist das am besten integrierte System im Marine-Markt. Alle Komponenten kommunizieren über standardisierte Protokolle:

```
                    ┌─────────────────────┐
                    │   VRM Portal (Cloud) │
                    │   Fernüberwachung    │
                    └─────────┬───────────┘
                              │ Internet (WiFi/LTE)
                    ┌─────────┴───────────┐
                    │   Cerbo GX           │
                    │   (System-Gateway)   │
                    └──┬──────┬──────┬────┘
                       │      │      │
              VE.Bus   │ VE.Direct  │ VE.Can
                       │      │      │
                ┌──────┘      │      └──────┐
                │             │             │
        ┌───────┴───┐  ┌─────┴─────┐ ┌─────┴─────┐
        │ MultiPlus │  │SmartShunt │ │ SmartSolar │
        │ / Quattro │  │ 500A      │ │ MPPT       │
        └───────────┘  └───────────┘ └───────────┘
                │
         ┌──────┴──────┐
         │ VE.Bus BMS  │ → LiFePO4-Batterien
         │ V2          │
         └─────────────┘

Monitoring: VictronConnect App (Bluetooth, lokal)
            VRM Portal (Cloud, weltweit)
            GX Touch Display (lokal, am Boot)
            Modbus TCP/MQTT (für Drittsysteme)
```

**Programmierung und Konfiguration:**
- **VictronConnect App** (iOS/Android/Desktop): Grundeinstellungen per Bluetooth
- **VEConfigure** (Windows): Detaillierte Konfiguration über MK3-USB-Adapter (Ladeprofile, Assistents, PowerAssist-Grenzen, Grid-Code-Einstellungen)
- **Node-RED auf Venus OS**: Fortgeschrittene Automatisierung (z.B. Generator-Autostart basierend auf SOC + Tageszeit + Solarprognose)
- **MQTT/Modbus**: Integration in Drittsysteme (SignalK, Home Assistant)

### 4.2 Mastervolt

Mastervolt (Amsterdam, Niederlande, gegr. 1991, seit 2018 Teil der Navico-Gruppe/Brunswick) ist der zweite große Spieler im Marine-Inverter-Markt. Bekannt für Premium-Qualität und Integration mit der MasterBus-Plattform.

#### 4.2.1 Mastervolt Mass Combi Pro (Inverter/Charger)

| Modell | Spannung | Inverter | Charger | Peak | Gewicht | Preis (ca.) |
|--------|----------|---------|---------|------|---------|-------------|
| Mass Combi Pro 12/3000-150 | 12V | 3.000W | 150A | 6.500W | 28 kg | €3.200 |
| Mass Combi Pro 24/3500-100 | 24V | 3.500W | 100A | 7.500W | 28 kg | €3.000 |
| Mass Combi Ultra 24/3500-100 | 24V | 3.500W | 100A | 7.500W | 25 kg | €3.500 |

**Merkmale Mass Combi Pro:**
- Reine Sinuswelle, THD <2%
- 3-stufiges Ladeverfahren mit Temperaturkompensation
- Power Sharing (wie Victron PowerAssist)
- MasterBus-Integration (CAN-basiertes Bussystem)
- CZone-kompatibel
- IP21 Schutzart
- Passiver Kühlung (kein Lüfter bis 50% Last)

#### 4.2.2 Mastervolt Mass Sine (Stand-Alone Inverter)

| Modell | Spannung | Dauerleistung | Peak | Leerlauf | Gewicht | Preis (ca.) |
|--------|----------|--------------|------|----------|---------|-------------|
| Mass Sine 12/1200 | 12V | 1.200W | 2.400W | 8W | 6,5 kg | €750 |
| Mass Sine 12/2000 | 12V | 2.000W | 4.000W | 12W | 10 kg | €1.200 |
| Mass Sine 24/1500 | 24V | 1.500W | 3.000W | 8W | 6,5 kg | €700 |
| Mass Sine 24/2500 | 24V | 2.500W | 5.000W | 12W | 10 kg | €1.100 |

#### 4.2.3 Mastervolt Isolation Transformer (Trenntrafo)

| Modell | Leistung | Gewicht | Typ | Preis (ca.) |
|--------|----------|---------|-----|-------------|
| IVET 3,5 kVA | 3.500VA | 16 kg | Ringkern | €1.200 |
| IVET 7,0 kVA | 7.000VA | 30 kg | Ringkern | €2.000 |
| IVET 10 kVA | 10.000VA | 40 kg | Ringkern | €2.800 |
| IVET 16 kVA | 16.000VA | 60 kg | Ringkern | €4.200 |

#### 4.2.4 Mastervolt Galvanic Isolator

| Modell | Nennstrom | Fail-Safe | Monitoring | Preis (ca.) |
|--------|----------|-----------|------------|-------------|
| GI-16 | 16A | Ja | LED | €100 |
| GI-32 | 32A | Ja | LED | €140 |
| GI-64 | 64A | Ja | LED + Alarm | €220 |

### 4.3 Whisper Power

Whisper Power (Drachten, Niederlande, gegr. 1996) ist spezialisiert auf Energiesysteme für Yachten, insbesondere leise Generatoren und kompakte Inverter-Systeme.

#### 4.3.1 Whisper Power Supreme Combi (Inverter/Charger)

| Modell | Spannung | Inverter | Charger | Peak | Gewicht | Preis (ca.) |
|--------|----------|---------|---------|------|---------|-------------|
| Supreme Combi 12V/2000W/80A | 12V | 2.000W | 80A | 5.000W | 15 kg | €2.200 |
| Supreme Combi 24V/3000W/60A | 24V | 3.000W | 60A | 7.500W | 18 kg | €2.500 |
| Supreme Combi 24V/3500W/80A | 24V | 3.500W | 80A | 8.500W | 22 kg | €3.000 |

#### 4.3.2 Whisper Power WBI (Sine Wave Inverter)

| Modell | Spannung | Dauerleistung | Peak | Preis (ca.) |
|--------|----------|--------------|------|-------------|
| WBI 150-12 | 12V | 150W | 350W | €180 |
| WBI 250-12 | 12V | 250W | 500W | €220 |
| WBI 350-24 | 24V | 350W | 700W | €240 |

### 4.4 Fischer Panda

Fischer Panda (Paderborn, Deutschland, gegr. 1977) ist primär als Generator-Hersteller bekannt, bietet aber integrierte Hybrid-Systeme für Yachten.

#### 4.4.1 Fischer Panda iSeries (Generator + Inverter)

| Modell | Generator | Inverter | Systemspannung | Gewicht | Preis (ca.) |
|--------|-----------|---------|----------------|---------|-------------|
| iGen 3500 | 3,5 kW | 3.000W | 24V | 95 kg | €12.000 |
| iGen 6000 | 6,0 kW | 5.000W | 24V/48V | 120 kg | €18.000 |
| iGen 10000 | 10,0 kW | 8.000W | 48V | 150 kg | €25.000 |

**Besonderheit:** Die iSeries integriert Generator, Inverter/Charger und Batterie-Management in einem System. Der Generator läuft nur bei Bedarf und mit variabler Drehzahl (leiser, effizienter).

### 4.5 Xantrex / Schneider Electric

Xantrex (gegr. 1983 in Vancouver, Kanada, seit 2008 Teil von Schneider Electric) ist in den USA dominant und in Europa weniger verbreitet. Relevant für den Export-Markt und amerikanische Yachten.

#### 4.5.1 Xantrex Freedom XC (Inverter/Charger)

| Modell | Spannung | Inverter | Charger | Peak | Gewicht | Preis (ca.) |
|--------|----------|---------|---------|------|---------|-------------|
| Freedom XC 12/2000 | 12V | 2.000W | 80A | 3.500W | 15 kg | €1.800 |
| Freedom XC 24/2000 | 24V | 2.000W | 60A | 3.500W | 14 kg | €1.700 |

#### 4.5.2 Xantrex Freedom SW (größere Modelle)

| Modell | Spannung | Inverter | Charger | Peak | Gewicht | Preis (ca.) |
|--------|----------|---------|---------|------|---------|-------------|
| Freedom SW 2012 | 12V | 2.000W | 100A | 4.200W | 20 kg | €2.200 |
| Freedom SW 2024 | 24V | 2.000W | 50A | 4.200W | 18 kg | €2.000 |
| Freedom SW 3012 | 12V | 3.000W | 150A | 6.000W | 28 kg | €3.000 |
| Freedom SW 3024 | 24V | 3.000W | 100A | 6.000W | 25 kg | €2.800 |

#### 4.5.3 Xantrex ProSine (Stand-Alone Inverter, Marine)

| Modell | Spannung | Dauerleistung | Peak | Preis (ca.) |
|--------|----------|--------------|------|-------------|
| ProSine 1000 | 12V | 1.000W | 2.000W | €800 |
| ProSine 1800 | 24V | 1.800W | 3.600W | €1.200 |

### 4.6 Sterling Power

Sterling Power (Brixham, UK, gegr. 1992) bietet hochwertige Leistungselektronik speziell für den Marine-Markt, mit Fokus auf kompakte Bauweise und fortschrittliche Ladetechnologie.

#### 4.6.1 Sterling Power ProCharge Ultra Combi (Inverter/Charger)

| Modell | Spannung | Inverter | Charger | Peak | Gewicht | Preis (ca.) |
|--------|----------|---------|---------|------|---------|-------------|
| CMP122500 | 12V | 2.500W | 100A | 5.000W | 16 kg | €2.400 |
| CMP243500 | 24V | 3.500W | 80A | 7.000W | 18 kg | €2.800 |

#### 4.6.2 Sterling Power SIB (Sine Wave Inverter)

| Modell | Spannung | Dauerleistung | Peak | Preis (ca.) |
|--------|----------|--------------|------|-------------|
| SIB121600 | 12V | 1.600W | 3.200W | €600 |
| SIB122700 | 12V | 2.700W | 5.400W | €900 |
| SIB241600 | 24V | 1.600W | 3.200W | €580 |
| SIB242700 | 24V | 2.700W | 5.400W | €850 |

#### 4.6.3 Sterling Power ProSplit (Galvanischer Isolator)

| Modell | Nennstrom | Dioden-Typ | Fail-Safe | Preis (ca.) |
|--------|----------|-----------|-----------|-------------|
| ProGI-16 | 16A | Si + MOV | Ja | €85 |
| ProGI-32 | 32A | Si + MOV | Ja | €120 |
| ProGI-64 | 64A | Si + MOV | Ja | €180 |

---

## 5. Hersteller-Datenbank

### 5.1 Victron Energy

| Parameter | Detail |
|-----------|--------|
| Firmensitz | Almere, Niederlande |
| Gründung | 1975 |
| Mitarbeiter | ca. 800 (2025) |
| Marktposition | Marktführer Marine-Inverter Europa |
| Website | victronenergy.com |
| Vertrieb DE | Über Fachhändler (keine Direktverkäufe) |
| Support | Exzellent — Community-Forum, umfangreiche Dokumentation, offene Firmware |
| Garantie | 5 Jahre (Standard) |
| Softwareökosystem | VictronConnect (App), VEConfigure (Windows), VRM (Cloud-Portal) |
| Kommunikation | VE.Bus, VE.Direct, VE.Can, Bluetooth |
| Besonderheit | Offenes Ökosystem, aktive Community, Venus OS (Open Source) |
| Marine-Marktanteil (geschätzt) | 40–50% in Europa, 20–30% weltweit |

**Produktbreite:**
- Inverter (Phoenix)
- Inverter/Charger (MultiPlus, Quattro)
- Ladegeräte (Blue Smart, Skylla)
- MPPT-Solarregler (SmartSolar, BlueSolar)
- Batteriemonitore (SmartShunt, BMV)
- Systemüberwachung (Cerbo GX, Ekrano GX)
- Lithium-Batterien (Smart, Super Pack, Lynx)
- Orion DC-DC-Wandler
- Trenntrafos (Autotransformer, Isolation Transformer)
- Galvanische Isolatoren

### 5.2 Mastervolt

| Parameter | Detail |
|-----------|--------|
| Firmensitz | Amsterdam, Niederlande |
| Gründung | 1991 |
| Übernahme | 2018 durch Navico Group (Brunswick) |
| Marktposition | Premium-Segment, OEM bei großen Werften |
| Website | mastervolt.com |
| Vertrieb DE | Über Fachhändler + OEM |
| Support | Gut — professioneller technischer Support |
| Garantie | 3 Jahre (Standard), erweiterbar |
| Softwareökosystem | MasterBus, CZone (Netzwerk-Steuerung) |
| Kommunikation | MasterBus (CAN), NMEA 2000, Modbus |
| Besonderheit | CZone-Integration für vernetzte Superyachten |
| Marine-Marktanteil (geschätzt) | 15–20% in Europa |

### 5.3 Whisper Power

| Parameter | Detail |
|-----------|--------|
| Firmensitz | Drachten, Niederlande |
| Gründung | 1996 |
| Marktposition | Nischenspezialist, leise Systeme |
| Website | whisperpower.com |
| Vertrieb DE | Über Fachhändler |
| Support | Gut |
| Garantie | 2 Jahre |
| Besonderheit | Extrem leise Generatoren, integrierte Energiesysteme |
| Marine-Marktanteil (geschätzt) | 5–8% in Europa |

### 5.4 Fischer Panda

| Parameter | Detail |
|-----------|--------|
| Firmensitz | Paderborn, Deutschland |
| Gründung | 1977 |
| Marktposition | Premium-Generatoren, Hybrid-Systeme |
| Website | fischerpanda.de |
| Vertrieb DE | Direkt + Fachhändler |
| Support | Exzellent — deutscher Service |
| Garantie | 2 Jahre |
| Besonderheit | Variable Drehzahl-Generatoren (i-Serie), Made in Germany |
| Marine-Marktanteil (geschätzt) | 10–15% Generatoren Europa |

### 5.5 Xantrex / Schneider Electric

| Parameter | Detail |
|-----------|--------|
| Firmensitz | Vancouver, Kanada (Schneider: Paris) |
| Gründung | 1983 (Xantrex), 2008 Übernahme durch Schneider |
| Marktposition | Dominant in Nordamerika, sekundär in Europa |
| Website | xantrex.com |
| Vertrieb DE | Begrenzt, über Spezialimporteure |
| Support | Gut in Nordamerika, eingeschränkt in Europa |
| Garantie | 2 Jahre |
| Besonderheit | ABYC-zertifiziert, 120V/60Hz und 230V/50Hz Varianten |
| Marine-Marktanteil (geschätzt) | 25–35% in Nordamerika, 5% in Europa |

### 5.6 Sterling Power

| Parameter | Detail |
|-----------|--------|
| Firmensitz | Brixham, Devon, UK |
| Gründung | 1992 |
| Marktposition | Premium-Nische, Leistungselektronik |
| Website | sterling-power.com |
| Vertrieb DE | Über SVB, Toplicht, weitere Fachhändler |
| Support | Gut — technisch versierter Support |
| Garantie | 2 Jahre, erweiterbar auf 5 |
| Besonderheit | Kompakte Bauweise, innovative Ladetechnik, Advanced Alternator Regulators |
| Marine-Marktanteil (geschätzt) | 5–8% in UK, 2–4% in Europa gesamt |

### 5.7 Vergleichsmatrix — Die wichtigsten Inverter/Charger im Direktvergleich

#### 5.7.1 Kategorie: Fahrtensegler 24V, 2.500–3.500W

| Kriterium | Victron MultiPlus-II 24/3000/70 | Mastervolt Mass Combi Pro 24/3500-100 | Whisper Power Supreme 24/3000/60 | Sterling CMP243500 |
|-----------|-------------------------------|--------------------------------------|----------------------------------|-------------------|
| Inverter-Leistung | 2.400W | 3.500W | 3.000W | 3.500W |
| Surge (5s) | 6.000W | 7.500W | 7.500W | 7.000W |
| Ladestrom | 70A | 100A | 60A | 80A |
| Leerlaufverbrauch | 15W | 18W | 16W | 20W |
| Wirkungsgrad (peak) | 94% | 95% | 93% | 92% |
| THD | <3% | <2% | <3% | <3% |
| Transfer-Zeit | <20ms | <20ms | <20ms | <20ms |
| PowerAssist | Ja | Ja (Power Sharing) | Ja | Ja |
| Parallel möglich | Ja (bis 6) | Ja (MasterBus) | Nein | Nein |
| 3-Phasen möglich | Ja (3 Geräte) | Ja | Nein | Nein |
| Kommunikation | VE.Bus, Bluetooth | MasterBus, CZone, Modbus | RS232, Modbus | RS232 |
| Cloud-Monitoring | VRM Portal | CZone Online | Nein | Nein |
| Lithium-kompatibel | Ja (VE.Bus BMS) | Ja (MasterBus BMS) | Ja (extern) | Ja (extern) |
| Firmware-Updates | Ja (App/USB) | Ja (MasterAdjust) | Begrenzt | Nein |
| Gewicht | 16 kg | 28 kg | 18 kg | 18 kg |
| Preis (ca.) | €1.400 | €3.000 | €2.500 | €2.800 |
| Garantie | 5 Jahre | 3 Jahre | 2 Jahre | 2 Jahre (erw. 5) |
| Community/Support | Exzellent | Gut | Mittel | Gut |
| Verfügbarkeit EU | Exzellent | Gut | Gut | Gut (UK) |

**AYDI-Empfehlung nach Einsatzprofil:**

| Profil | 1. Wahl | 2. Wahl | Begründung |
|--------|---------|---------|------------|
| Blauwasser-Segler | Victron MultiPlus-II 24/3000/70 | Mastervolt Mass Combi Pro 24/3500-100 | Bestes Ökosystem, VRM-Fernüberwachung, Community |
| Charterboot/OEM | Mastervolt Mass Combi Pro 24/3500-100 | Victron MultiPlus-II 24/3000/70 | Höhere Ladeleistung, CZone-Integration |
| Budget-orientiert | Victron MultiPlus-II 24/3000/70 | Sterling CMP243500 | Bestes Preis-Leistungs-Verhältnis |
| Superyacht-Zulieferung | Mastervolt Mass Combi Ultra 24/3500-100 | Victron Quattro-II 24/5000/120 | CZone-Integration, OEM-Verfügbarkeit |
| UK-Markt | Sterling CMP243500 | Victron MultiPlus-II 24/3000/70 | Lokaler Support, guter Service |

#### 5.7.2 Kategorie: Große Motoryacht 48V, 5.000–10.000W

| Kriterium | Victron Quattro-II 48/8000/110 | Victron Quattro-II 48/10000/140 | Mastervolt Mass Combi Ultra 24/3500 (2× parallel) |
|-----------|-------------------------------|--------------------------------|---------------------------------------------------|
| Inverter-Leistung | 6.400W | 8.000W | 7.000W (2×3.500W) |
| AC-Eingänge | 2 | 2 | 1 pro Gerät (2 gesamt) |
| Ladestrom | 110A | 140A | 200A (2×100A) |
| Gewicht | 45 kg | 55 kg | 56 kg (2×28 kg) |
| Preis (ca.) | €4.200 | €5.200 | €6.000 (2×€3.000) |
| Vorteil | Kompakt, ein Gerät | Höchste Leistung, ein Gerät | Redundanz (ein Gerät fällt aus → 50% Leistung) |

### 5.8 Preisübersicht nach Leistungsklasse (Stand 2026)

| Leistungsklasse | Stand-Alone Inverter | Inverter/Charger | Trenntrafo (passend) | Galv. Isolator |
|-----------------|---------------------|-----------------|---------------------|----------------|
| 500–1.000W (12V) | €180–€500 | €800–€1.200 | €900 (3,5kVA) | €65–€100 |
| 1.000–2.000W (12V/24V) | €400–€1.200 | €1.200–€2.500 | €900–€1.200 (3,5kVA) | €85–€140 |
| 2.000–3.000W (24V) | €800–€1.500 | €1.400–€3.500 | €1.200–€1.600 (3,5–7kVA) | €85–€140 |
| 3.000–5.000W (24V/48V) | €1.200–€3.500 | €2.200–€5.200 | €1.600–€2.800 (7–10kVA) | €140 |
| 5.000–10.000W (48V) | €1.400–€3.500 | €3.500–€7.000 | €2.800–€4.200 (10–16kVA) | €140 |

**Gesamtkosten einer typischen AC-Installation (Material + Installation):**

| Boot-Typ | Nur Landstrom (ohne Inverter) | Landstrom + Inverter | Komplett mit Trenntrafo |
|----------|------------------------------|---------------------|------------------------|
| 10m Segler | €800–€1.500 | €2.500–€4.000 | €4.000–€6.000 |
| 14m Segler | €1.200–€2.000 | €4.000–€7.000 | €6.000–€10.000 |
| 18m Segler/MY | €2.000–€3.500 | €8.000–€15.000 | €12.000–€22.000 |
| 22m Motoryacht | €3.000–€5.000 | €15.000–€30.000 | €25.000–€50.000 |

### 5.10 Weitere relevante Hersteller

| Hersteller | Land | Spezialgebiet | Relevanz |
|------------|------|---------------|----------|
| Studer Innotec | Schweiz | Hochleistungs-Inverter (Xtender-Serie) | Premium, Off-Grid, selten Marine |
| Outback Power | USA | Off-Grid-Systeme | US-Markt, selten Marine |
| Cristec | Frankreich | Marine-Ladegeräte und kleine Inverter | OEM für franz. Werften |
| Philippi | Deutschland | Marine-Elektrik-Systeme, Verteiler | Kein Inverter, aber AC-Verteilung |
| Torqeedo | Deutschland | Elektroantriebe mit DC/AC-Wandlung | Spezialist E-Antrieb |

---

## 6. Fehlerbild-Atlas

### 6.1 Fehlerbild: Erdschluss im AC-Bordnetz

**Beschreibung:**
Ein Erdschluss (Earth Fault) liegt vor, wenn ein stromführender Leiter (L oder N) einen niederohmigen Kontakt zum Schutzleiter (PE) oder zum Bootsrumpf bekommt. Dies kann durch beschädigte Kabelisolation, Feuchtigkeit in Steckdosen, defekte Verbraucher oder korrodierte Verbindungen entstehen.

**Symptome:**
- FI-Schutzschalter löst sofort nach Einschalten des Landstroms aus
- FI löst erst nach einiger Zeit aus (feuchtebedingter, zunehmender Erdschluss)
- Kribbeln beim Berühren von Metallteilen an Bord (PE-Verbindung fehlerhaft)
- Erhöhter Stromverbrauch ohne erkennbaren Verbraucher

**Ursachen nach Häufigkeit:**

| Rang | Ursache | Häufigkeit |
|------|---------|-----------|
| 1 | Feuchtigkeit in Steckdosen (besonders Nassbereich) | 35% |
| 2 | Beschädigte Kabelisolation (Scheuerung, Knick, UV) | 20% |
| 3 | Defekter Verbraucher (Heizelement, Motor) | 18% |
| 4 | Korrodierte Steckverbindung | 12% |
| 5 | Schimmel/Salzablagerung auf Isolatoren | 8% |
| 6 | Nagel/Schraube durch Kabel (bei Umbauarbeiten) | 5% |
| 7 | Fabrikfehler (selten) | 2% |

**Diagnose:**
1. Alle Sicherungsautomaten im AC-Verteiler ausschalten
2. FI einschalten — löst er aus? → Fehler VOR dem Verteiler (Zuführung, FI selbst)
3. FI hält → Einzelne Stromkreise nacheinander einschalten
4. Betroffenen Stromkreis identifiziert → Alle Verbraucher abziehen
5. FI hält ohne Verbraucher → Verbraucher einzeln einstecken → defektes Gerät identifiziert
6. FI löst ohne Verbraucher aus → Kabel/Steckdose im Stromkreis defekt → Isolationsmessung

**Confidence:** documented — basierend auf BSS (British Standards Survey), Pantaenius Schadensdatenbank, Werft-Praxisberichte.

### 6.2 Fehlerbild: Leckstrom ins Wasser (Electric Shock Drowning Risk)

**Beschreibung:**
Leckströme fließen über den Bootsrumpf (metallisch oder über Unterwassermetalle bei GFK) ins Wasser. Ursachen: defekte Isolation, fehlende galvanische Trennung, fehlerhafte Erdung in der Marina. Bereits Ströme ab 10mA AC im Wasser können bei Schwimmern zu Muskellähmung und Ertrinken führen (Electric Shock Drowning, ESD).

**Symptome:**
- Kribbeln im Wasser in der Nähe des Bootes
- Fische verhalten sich ungewöhnlich in Bootsnähe
- Zinkanoden verbrauchen sich ungewöhnlich schnell
- Korrosion an Unterwassermetallen (Propeller, Saildrive, Borddurchlässe)
- ELCI (Equipment Leakage Current Interrupter) löst aus (in USA-Marinas)

**Ursachen:**

| Ursache | Risikostufe | Häufigkeit |
|---------|------------|-----------|
| Fehlerhafte Landstrom-Erdung in der Marina | KRITISCH | 15% |
| Fehlende galvanische Isolation am Boot | HOCH | 25% |
| Defekte AC-Isolation an Bord | HOCH | 20% |
| Defekter Warmwasserboiler (Heizspirale→Wasser→Rumpf) | HOCH | 15% |
| Falsch verdrahtete Landstrom-Adapter | MITTEL | 10% |
| Defektes Nachbarboot (Strom fließt über unser Boot) | MITTEL | 10% |
| N-PE-Verbindung an Bord (verboten!) | HOCH | 5% |

**Prävention:**
1. Galvanischer Isolator als Minimum — besser: Trenntrafo
2. FI 30mA auf ALLEN AC-Kreisen
3. Jährliche Isolationsmessung des gesamten AC-Systems
4. ELCI (30mA, alle Leiter) am Landstromeingang
5. Nie im Hafen schwimmen, wenn Boote am Landstrom hängen
6. Regelmäßige Prüfung des Marina-Anschlusses (Polaritätsprüfer)

**AYDI-Bewertung:** Jeder Hinweis auf Leckströme im Wasser wird als KRITISCHER Befund eingestuft. Automatische Warnung im Compliance-Modul wenn galvanische Isolation fehlt und Landstromanschluss vorhanden.

### 6.3 Fehlerbild: FI-Schutzschalter löst permanent aus

**Beschreibung:**
Der FI löst wiederholt aus, auch nachdem er zurückgesetzt wurde. Dies kann sofort beim Einschalten oder nach einer gewissen Betriebszeit auftreten.

**Differenzialdiagnose:**

| Symptom | Wahrscheinliche Ursache | Maßnahme |
|---------|------------------------|----------|
| FI löst sofort aus, ohne angeschlossene Verbraucher | Erdschluss in der Verkabelung, defekter FI, falsche Verdrahtung | Isolationsmessung, Verdrahtung prüfen |
| FI löst aus beim Einstecken eines bestimmten Geräts | Defektes Gerät, zu hoher Ableitstrom | Gerät am Land testen, Ableitstrom messen |
| FI löst nach 10–30 Min. aus | Feuchteaufbau in Steckdose, thermisches Problem | Steckdosen inspizieren, Feuchtequellen beseitigen |
| FI löst bei hoher Last aus | Summe der Ableitströme übersteigt 30mA | FI-Kreise aufteilen, Ableitströme messen |
| FI löst bei Regen/Wellengang aus | Wasser in Decksdurchführung oder Stecker | Decksdurchführungen abdichten |
| FI löst im Eco-Modus des Inverters aus | Suchpulse des Inverters | Eco-Modus deaktivieren oder FI-Typ prüfen |

**Systematische Fehlersuche:**

```
FI löst aus
├── Sofort beim Einschalten?
│   ├── JA → Alle Automaten aus → FI ein
│   │   ├── FI hält → Kreise einzeln einschalten → defekten Kreis finden
│   │   └── FI löst weiterhin aus → Fehler VOR Verteiler oder FI defekt
│   │       ├── FI-Testtaste funktioniert? → Ja → Verkabelung zum FI prüfen
│   │       └── FI-Testtaste reagiert nicht → FI defekt → tauschen
│   └── NEIN → Nach welcher Zeit?
│       ├── 10–60 Minuten → Feuchteproblem → Steckdosen/Verbindungen inspizieren
│       ├── Bei bestimmtem Verbraucher → Gerät-Ableitstrom messen (max. 3,5mA)
│       └── Nur bei Regen/Seegang → Wassereintritt in Elektrik
```

### 6.4 Fehlerbild: Inverter-Überlast / Abschaltung

**Beschreibung:**
Der Wechselrichter schaltet ab oder reduziert die Leistung wegen Überlast, Übertemperatur oder Unterspannung.

**Symptome:**
- Inverter zeigt Überlast-LED / Alarm
- AC-Ausgang schaltet ab, Verbraucher stromlos
- Inverter brummt laut oder Lüfter dreht auf Maximum
- Wiederholte kurze Abschaltungen (Cycling)

**Ursachen und Lösungen:**

| Ursache | Symptom | Lösung |
|---------|---------|--------|
| Anlaufstrom eines Verbrauchers übersteigt Surge-Rating | Abschaltung beim Einschalten eines Geräts | Soft-Starter einbauen, größeren Inverter wählen, Geräte nicht gleichzeitig starten |
| Dauerlast zu hoch | Abschaltung nach 5–30 Min. (Wärme) | Last reduzieren, Belüftung verbessern, größeren Inverter wählen |
| Batteriespannung zu niedrig | Inverter zeigt "Low Battery" | Batterien laden, Batteriebank vergrößern, Kabelverbindungen prüfen |
| Spannungsabfall am DC-Kabel | Funktioniert bei niedriger Last, schaltet bei hoher Last ab | DC-Kabelquerschnitt erhöhen, Verbindungen nachjustieren |
| Übertemperatur (schlechte Belüftung) | Abschaltung an heißen Tagen oder nach längerer Last | Einbauort belüften, Lüfter nachrüsten, Abstand zu Wärmequellen |
| Kurzschluss auf AC-Seite | Sofortige Abschaltung | Kurzschluss suchen und beseitigen |
| Defekter Inverter | Sporadische Ausfälle, ungewöhnliche Geräusche | Hersteller-Service, Firmware-Update, ggf. Tausch |

### 6.5 Fehlerbild: Trenntrafo brummt

**Beschreibung:**
Der Trenntrafo erzeugt ein hörbares Brummen (50Hz oder 100Hz Grundfrequenz), das sich in den Rumpf überträgt und als störendes Geräusch wahrgenommen wird.

**Ursachen:**

| Ursache | Häufigkeit | Lösung |
|---------|-----------|--------|
| DC-Anteil im Landstrom (Gleichstromoffset) | 40% | DC-Filter (Blocking-Kondensator) vorschalten, Marina wechseln, Trenntrafo mit DC-Toleranz |
| Magnetostriktion (normal, verstärkt bei Teillast) | 25% | Schwingungsentkopplung (Gummipuffer), Vergussmasse, größeren Trafo wählen |
| Mechanische Resonanz mit Bootskörper | 20% | Montage auf Sylomer/Vibrationsdämpfer, Montageort ändern |
| Lose Bleche im Kern (Alterung) | 10% | Trafo tauschen |
| Überlast (Kern in Sättigung) | 5% | Last reduzieren oder größeren Trafo installieren |

**DC-Anteil im Landstrom — Erklärung:**
Viele moderne Verbraucher (Schaltnetzteile, Dimmer, Induktionsherde in der Marina) erzeugen unsymmetrische Halbwellen, die zu einem DC-Anteil im Netz führen. Dieser DC-Anteil verschiebt den Arbeitspunkt des Trafokerns und führt zu asymmetrischer Sättigung → Brummgeräusch.

**Technische Lösung:** Ein Sperrwandler-Modul (DC-Blocker) in Serie zum Trafo-Eingang filtert den Gleichstromanteil. Kosten: €100–€300.

### 6.6 Fehlerbild: Galvanische Korrosion durch Landstrom

**Beschreibung:**
Beschleunigte Korrosion an Unterwassermetallen (Propeller, Welle, Saildrive, Borddurchlässe, Ruder, Kiel) wenn das Boot am Landstrom angeschlossen ist. Die Korrosionsrate kann 10–100× höher sein als ohne Landstrom.

**Symptome:**
- Zinkanoden verbrauchen sich in Wochen statt Monaten
- Pitting an Bronze-Borddurchlässen
- Rosa Verfärbung an Bronze (Entzinkung)
- Propeller zeigt Lochfraß oder Oberflächenveränderung
- Saildrive-Anode vollständig aufgelöst
- Blasenbildung an Unterwasser-Anstrich

**Mechanismus:**

```
Boot A (mit Landstrom)        Boot B (mit Landstrom)
═══════════════════          ═══════════════════
Bronze-Propeller              Aluminium-Saildrive
(edel: +0,30V)               (unedel: -0,75V)
     │                              │
     └──── PE-Leiter ──── Marina ── PE-Leiter ────┘
           (galvanische Brücke über Schutzleiter)
           
           PLUS: Streu-/Leckströme über Wasser

Ergebnis: Aluminium-Saildrive von Boot B wird
          stark beschleunigt korrodiert
          (Opferanode für den Propeller von Boot A)
```

**Lösungen:**

| Maßnahme | Wirksamkeit | Kosten |
|----------|-------------|--------|
| Galvanischer Isolator | Gut (DC-Schutz) | €100–€300 |
| Trenntrafo | Exzellent (vollständige Isolation) | €800–€3.500 |
| Zinkanoden korrekt dimensioniert | Ergänzend, nicht alleinige Lösung | €50–€200/Jahr |
| ICCP-System (Impressed Current Cathodic Protection) | Exzellent (aktiver Schutz) | €1.500–€5.000 |
| Landstrom abstecken wenn nicht nötig | 100% (kein Strom = keine galvanische Brücke) | €0 |

### 6.7 Fehlerbild: Inverter erzeugt keine Ausgangsspannung

**Beschreibung:**
Der Inverter ist eingeschaltet, zeigt Status-LEDs, aber am AC-Ausgang liegt keine Spannung an.

**Ursachen:**

| Ursache | Prüfung | Lösung |
|---------|---------|--------|
| Eco-Modus aktiv, keine Last erkannt | Last anschließen, warten 1–3s | Eco-Modus deaktivieren oder Last >25W nutzen |
| Batteriespannung unter Abschaltschwelle | Batteriespannung messen (12V: <10,5V, 24V: <21V) | Batterien laden |
| Überlast-Schutz aktiv (nach vorherigem Fehler) | Inverter aus/ein (Reset) | Ursache der Überlast beseitigen, dann Reset |
| Ausgangsrelais defekt (selten) | Relais-Klick beim Einschalten hörbar? | Service-Werkstatt |
| AC-Sicherung im Inverter ausgelöst | Interne Sicherung prüfen (Handbuch) | Sicherung ersetzen, Ursache klären |
| Remote-Schalter auf "Aus" | Remote-Anschluss prüfen | Einschalten / Kabelbruch am Remote |

### 6.8 Fehlerbild: Landstrom-Anschlusskabel überhitzt

**Beschreibung:**
Das Landstromkabel (Verbindung Marina-Steckdose → Boot) oder die CEE-Stecker werden auffällig warm oder heiß.

**Ursachen:**

| Ursache | Risiko | Lösung |
|---------|--------|--------|
| Lose Steckerverbindung (oxidiert, verbogen) | BRAND | Stecker reinigen, Kontakte prüfen, ggf. Stecker ersetzen |
| Kabelquerschnitt zu gering | BRAND | Kabel mit min. 2,5mm² (16A) oder 6mm² (32A) verwenden |
| Kabel zu lang (>50m bei 2,5mm²) | Spannungsabfall + Erwärmung | Kürzeres Kabel oder dickeren Querschnitt verwenden |
| Kabel aufgerollt (bei Trommelkabel) | BRAND | Kabel immer vollständig abrollen! |
| Dauerlast nahe am Maximum | Erhöhte Alterung | Last reduzieren oder 32A-Anschluss nutzen |
| Beschädigte Isolation (Knick, Quetschung) | BRAND | Kabel ersetzen |

**AYDI-Warnung:** Jede Erwärmung eines Landstromkabels über 60°C ist ein Brandrisiko und wird als KRITISCHER Befund eingestuft.

### 6.9 Fehlerbild: Inverter verursacht Interferenzen (EMV)

**Beschreibung:**
Der Inverter stört Funkgeräte (UKW, SSB, AIS), Navigationsausrüstung (GPS, Radar, Plotter) oder Audiosysteme (Brummen im Lautsprecher).

**Symptome:**
- Brummen oder Rauschen in UKW-Funk, verschwindet bei Inverter-Abschaltung
- AIS-Empfangsprobleme
- GPS-Positionsschwankungen
- Störbalken auf dem Radarschirm
- 50Hz-Brummen in Lautsprechern

**Ursachen und Maßnahmen:**

| Ursache | Maßnahme |
|---------|----------|
| EMV-Abstrahlung vom Inverter-Gehäuse | Abstand zu Antennen >2m, Inverter abschirmen |
| Leitungsgebundene Störungen über DC-Kabel | Ferritkerne auf DC-Kabeln, EMV-Filter am DC-Eingang |
| Leitungsgebundene Störungen über AC-Kabel | Ferritkerne auf AC-Kabeln, Netzfilter am AC-Ausgang |
| Erdschleife (Ground Loop) | Sternförmige Erdung, Massepunkt prüfen |
| Defekter Inverter (erhöhte HF-Abstrahlung) | Firmware-Update, Service |

### 6.10 Fehlerbild: Batterien laden nicht über Landstrom

**Beschreibung:**
Das Ladegerät (im Kombigerät oder standalone) nimmt nach Anschluss des Landstroms keine Ladung auf, oder die Ladung stoppt vorzeitig.

**Ursachen:**

| Ursache | Prüfung | Lösung |
|---------|---------|--------|
| Ladegerät im "Storage"-Modus (Batterien voll) | Batteriespannung messen | Normal — kein Fehler |
| Temperaturkompensation: zu warm | Temperatursensor prüfen | Belüftung verbessern, Sensor korrekt positionieren |
| BMS hat Ladung gesperrt (LiFePO4) | BMS-Status prüfen | BMS-Kommunikation prüfen (CAN/VE.Bus) |
| Ladegerät erkennt Batterie nicht | Batteriespannung am Charger-Ausgang messen | Kabel/Sicherung zwischen Charger und Batterie prüfen |
| Ladespannung zu niedrig eingestellt | Einstellung prüfen (12V: 14,2–14,8V, 24V: 28,4–29,6V) | Korrekte Spannungen für Batterietyp einstellen |
| Defekte Batteriebank | Einzelzellen messen | Defekte Batterie ersetzen |

### 6.11 Fehlerbild: Ungewöhnliche Geräusche vom Inverter

**Beschreibung:**
Der Wechselrichter erzeugt auffällige Geräusche: Brummen, Pfeifen, Klicken oder Lüftergeräusche.

| Geräusch | Ursache | Bewertung | Maßnahme |
|----------|---------|-----------|----------|
| Leises 50Hz-Brummen | Transformator-Vibration | Normal bei Last >50% | Schwingungsentkopplung |
| Lautes Brummen | Hohe Last, Kern in Teilsättigung | Achtung | Last reduzieren |
| Hochfrequentes Pfeifen (>5 kHz) | PWM-Frequenz hörbar | Normal bei manchen Modellen | Firmware-Update prüfen |
| Klicken (rhythmisch, alle 2–5s) | Eco-Modus (Suchpulse) | Normal | Eco-Modus deaktivieren falls störend |
| Klicken (einmalig bei Landstrom) | Transfer-Relais schaltet | Normal | — |
| Rattelndes Klicken | Transfer-Relais defekt oder Spannung grenzwertig | Warnung | Service |
| Lüfter-Dauerlauf | Übertemperatur oder verschmutzter Lüfter | Achtung | Belüftung prüfen, Lüfter reinigen |
| Lüfter-Rasseln | Lager verschlissen | Wartung | Lüfter tauschen |

### 6.12 Fehlerbild: Polaritätsproblem am Landstrom

**Beschreibung:**
Phase (L) und Neutralleiter (N) sind am Landstromanschluss vertauscht. Häufig in Mittelmeer-Marinas, Asien und Südamerika.

**Risiken:**
- Einpolige Schalter schalten N statt L → spannungsführende Kontakte bei "Aus"
- FI-Schutz funktioniert eingeschränkt bei manchen Fehlerfällen
- Schaltnetzteile können beschädigt werden
- Erhöhte Korrosionsgefahr

**Erkennung:**
- Polaritätsprüfer (3-LED-Anzeige) am Landstromeingang — **Pflichtausrüstung!**
- Multimeter: L gegen PE = 230V, N gegen PE = <5V (korrekt)
- Viele Inverter/Charger (Victron MultiPlus, Mastervolt) zeigen Polaritätsfehler an

**Lösung:**
- Umstecken des Kabels (bei symmetrischem CEE-Stecker nicht möglich!)
- Adapter mit gekreuzter Polarität (L↔N-Tausch) — **NUR mit Trenntrafo sicher!**
- Trenntrafo macht Polarität irrelevant (Sekundärseite wird am Boot definiert)
- Bei dauerhaft falsch gepolter Marina: Hafenmeister informieren, auf eigene Sicherheit achten

### 6.13 Fehlerbild: Warmwasserboiler als AC-Risikoquelle

**Beschreibung:**
Der elektrische Warmwasserboiler (230V AC, typisch 500–1.500W Heizleistung) ist eine der häufigsten Quellen für AC-Fehler an Bord. Die Kombination aus Heizelement, Wasser und metallischem Gehäuse schafft ein inhärentes Risiko.

**Typische Fehler:**

| Fehler | Mechanismus | Folge | Häufigkeit |
|--------|------------|-------|-----------|
| Heizspirale durchgebrannt | Kalkablagerung → lokale Überhitzung → Isolation schmilzt | Phase auf Wasser → Rumpf → ins Seewasser | 25% aller Boiler >10 Jahre |
| Thermostat defekt | Wasser überhitzt → Druck steigt → Überdruckventil | Heißwasser-/Dampfaustritt, Energieverschwendung | 15% |
| Anodenstab verbraucht | Keine kathodische Schutzwirkung mehr | Innenkorrosion des Tanks, Lochfraß | 40% (nie gewechselt) |
| Erdverbindung korrodiert | PE-Anschluss am Boiler oxidiert | FI erkennt Fehler nicht | 20% |
| Druckbegrenzungsventil verklebt | Kalk/Korrosion blockiert Ventil | Überdruck im Tank bei Thermostat-Ausfall | 10% |

**Prävention:**
1. Boiler-Anode alle 2–3 Jahre prüfen und ersetzen (Magnesium- oder Zinkanode)
2. FI-Schutzschalter auf dem Boiler-Stromkreis — NIEMALS überbrücken
3. Isolationsmessung des Boilers jährlich (Megger, Heizelement gegen Gehäuse)
4. Überdruckventil jährlich testen (Hebel betätigen → Wasser muss austreten)
5. Boiler bei Langzeitlagerung entleeren (Frost, Legionellen)

**AYDI-Bewertung:** Der Warmwasserboiler wird im Compliance-Modul als eigener Prüfpunkt geführt. Bei Boilern >10 Jahre ohne dokumentierte Wartung: automatische Warnung.

### 6.14 Fehlerbild-Zusammenfassung — AYDI Schwachstellenmatrix

| Nr. | Fehlerbild | Häufigkeit | Schwere | Erkennung (visuell) | Erkennung (strukturiert) |
|-----|-----------|-----------|---------|---------------------|-------------------------|
| 6.1 | Erdschluss im AC-Bordnetz | Häufig | HOCH | visual_low (Feuchtigkeitsspuren) | measured (Isolationsmessung) |
| 6.2 | Leckstrom ins Wasser (ESD) | Selten | KRITISCH | visual_insufficient | measured (Strommessung) |
| 6.3 | FI löst permanent aus | Häufig | MITTEL | visual_low | measured (Ableitstrom) |
| 6.4 | Inverter-Überlast | Häufig | MITTEL | visual_insufficient | measured (Lastmessung) |
| 6.5 | Trenntrafo brummt | Mittel | NIEDRIG | visual_insufficient | measured (DC-Anteil) |
| 6.6 | Galvanische Korrosion | Häufig | HOCH | visual_high (Anodenverbrauch) | measured (Potentialmessung) |
| 6.7 | Inverter keine Ausgangsspannung | Mittel | MITTEL | visual_low (LEDs) | measured (Spannungsmessung) |
| 6.8 | Landstromkabel überhitzt | Selten | KRITISCH | visual_medium (Verfärbung) | measured (Thermografie) |
| 6.9 | EMV-Interferenzen | Mittel | NIEDRIG | visual_insufficient | documented (Funkstörung) |
| 6.10 | Batterien laden nicht | Häufig | MITTEL | visual_low (Display) | measured (Ladekurve) |
| 6.11 | Inverter-Geräusche | Mittel | NIEDRIG | visual_insufficient | documented (Nutzerbericht) |
| 6.12 | Polaritätsfehler | Häufig (Ausland) | HOCH | visual_medium (Anzeige) | measured (Polaritätsprüfer) |

**AYDI-Relevanz nach Modul:**

| Modul | Relevante Fehlerbilder | Gewichtung |
|-------|----------------------|------------|
| Compliance | 6.1, 6.2, 6.3, 6.8, 6.12 | Strukturiert: 0,95, Visuell: 0,05 |
| Materials | 6.6 | Strukturiert: 0,35, Visuell: 0,65 |
| Production | 6.5, 6.7, 6.9 | Strukturiert: 0,55, Visuell: 0,45 |
| Cost | 6.4, 6.6, 6.10 | Strukturiert: 1,00, Visuell: 0,00 |
| Service Patterns | Alle | Strukturiert: 0,65, Visuell: 0,35 |

### 6.14 Fehlerbild-Prävention — Wartungsintervalle

| Maßnahme | Intervall | Wer | Kosten |
|----------|-----------|-----|--------|
| FI-Testtaste prüfen | Monatlich | Eigner | €0 |
| Polaritätsprüfung bei Landstrom | Bei jedem Anschluss | Eigner | €0 |
| Visuelle Inspektion AC-Verteiler | 6 Monate | Eigner | €0 |
| Kabelverbindungen nachziehen | Jährlich | Eigner/Elektriker | €0–€100 |
| Isolationsmessung (Megger) | 3–5 Jahre | Elektriker | €100–€200 |
| FI-Schutzschalter tauschen | 10 Jahre | Elektriker | €80–€150 |
| Inverter-Lüfter reinigen | Jährlich | Eigner | €0 |
| DC-Kabelverbindungen prüfen | Jährlich | Eigner | €0 |
| Galvanischer Isolator testen | Jährlich | Eigner (Multimeter) | €0 |
| Trenntrafo Sichtprüfung | Jährlich | Eigner | €0 |
| Landstromkabel Zustandsprüfung | Saisonbeginn | Eigner | €0 |
| Zinkanoden-Zustand (Korrelation Landstrom) | Alle 3 Monate | Eigner (Taucher) | €50–€100 |

---

## 7. Troubleshooting-Entscheidungsbäume

### 7.1 Entscheidungsbaum: Landstrom funktioniert nicht

```
PROBLEM: Kein Landstrom an Bord
═══════════════════════════════

START: Landstromkabel eingesteckt?
├── NEIN → Kabel einstecken, korrekt verriegeln
│   └── Problem gelöst? → JA → ENDE
│                       → NEIN → weiter
├── JA → Steg-Steckdose unter Strom?
│   ├── PRÜFEN: Multimeter an Steg-Steckdose → 230V?
│   │   ├── NEIN → Steg-Sicherung prüfen, Hafenmeister kontaktieren
│   │   └── JA → Spannung an Bord-Einbaustecker (Deck)?
│   │       ├── NEIN → Landstromkabel defekt → Kabel tauschen
│   │       │   └── Kabelverbindungen am CEE-Stecker prüfen (oxidiert?)
│   │       └── JA → Spannung nach Hauptschalter?
│   │           ├── NEIN → Hauptschalter defekt oder aus → einschalten/tauschen
│   │           └── JA → FI/LS löst aus?
│   │               ├── JA → siehe Entscheidungsbaum 7.3 (FI löst aus)
│   │               └── NEIN → Spannung am AC-Verteiler?
│   │                   ├── NEIN → Verdrahtung zwischen LS/FI und Verteiler
│   │                   │   └── Klemmen, Kabel, Trenntrafo-Durchgang prüfen
│   │                   └── JA → Einzelne Stromkreise prüfen
│   │                       └── LS für betroffenen Kreis einschalten
│   │                           ├── LS löst sofort aus → Kurzschluss im Kreis
│   │                           └── LS hält → Steckdose/Verbraucher prüfen
```

### 7.2 Entscheidungsbaum: Inverter startet nicht

```
PROBLEM: Inverter gibt keine 230V AC aus
════════════════════════════════════════

START: Inverter eingeschaltet (Hauptschalter/Remote)?
├── NEIN → Einschalten
│   └── Keine Reaktion? → DC-Sicherung prüfen (am Batteriepol!)
│       ├── Sicherung durchgebrannt → Ursache klären (Kurzschluss DC?)
│       │   └── Neue Sicherung, einschalten, beobachten
│       └── Sicherung OK → DC-Kabel prüfen (Spannung am Inverter-Eingang?)
│           ├── Keine Spannung → Kabelbruch, lose Klemme, Batterieschalter
│           └── Spannung vorhanden → Inverter defekt → Service
│
├── JA → LEDs / Display zeigen Status?
│   ├── NEIN (keine LEDs) → Kein Strom am Inverter → DC-Sicherung + Kabel
│   ├── JA → Welcher Status?
│   │   ├── "Low Battery" / Batterie-LED blinkt
│   │   │   ├── Batteriespannung messen (direkt an Klemmen)
│   │   │   │   ├── <10,5V (12V) / <21V (24V) → Batterien laden!
│   │   │   │   └── >11V (12V) / >22V (24V) → Spannungsabfall am DC-Kabel!
│   │   │   │       └── Querschnitt zu gering, Verbindung lose, Kabel zu lang
│   │   │   └── Batteriespannung am Inverter-Eingang messen (unter Last)
│   │   │       └── Differenz >0,5V → DC-Kabel-Problem
│   │   │
│   │   ├── "Overload" / Überlast-LED
│   │   │   ├── Alle AC-Verbraucher ausschalten
│   │   │   ├── Inverter resetten (Aus/Ein)
│   │   │   ├── Einen Verbraucher nach dem anderen einschalten
│   │   │   └── Verbraucher identifizieren, der Überlast verursacht
│   │   │       ├── Anlaufstrom zu hoch → Soft-Starter
│   │   │       └── Dauerlast zu hoch → Inverter zu klein → upgraden
│   │   │
│   │   ├── "Over Temperature" / Temperatur-LED
│   │   │   ├── Lüfter blockiert? (Staub, Fremdkörper)
│   │   │   ├── Umgebungstemperatur >40°C?
│   │   │   ├── Einbauraum geschlossen? → Belüftung schaffen
│   │   │   └── 30 Min. abkühlen lassen, dann neustarten
│   │   │
│   │   ├── Status "Eco-Modus" / Suchfunktion
│   │   │   ├── Verbraucher anschließen (>25W, z.B. Licht)
│   │   │   ├── Warten 2–5 Sekunden → Inverter sollte starten
│   │   │   └── Startet nicht → Eco-Modus deaktivieren
│   │   │
│   │   └── "Fault" / Fehler-LED
│   │       ├── Fehlercode auslesen (App, Display, oder LED-Blinkmuster)
│   │       └── Laut Hersteller-Handbuch → Service wenn nötig
```

### 7.3 Entscheidungsbaum: FI-Schutzschalter löst wiederholt aus

```
PROBLEM: FI löst aus (sofort oder nach kurzer Zeit)
═══════════════════════════════════════════════════

START: FI-Testtaste drücken → löst FI aus?
├── NEIN → FI defekt → tauschen
├── JA → FI grundsätzlich funktionsfähig
│
│   Schritt 1: ALLE Leitungsschutzschalter (LS) ausschalten
│   FI einschalten → löst aus?
│   ├── JA → Fehler VOR dem Verteiler
│   │   ├── Landstromkabel prüfen (Feuchtigkeit in Stecker?)
│   │   ├── CEE-Einbaustecker prüfen
│   │   ├── Kabel vom Einbaustecker zum FI prüfen
│   │   ├── Trenntrafo prüfen (wenn vorhanden)
│   │   └── FI selbst defekt? → mit anderem FI testen
│   │
│   └── NEIN → FI hält → Fehler NACH dem Verteiler
│       │
│       Schritt 2: LS einzeln einschalten (1 nach dem anderem)
│       Welcher LS lässt den FI auslösen?
│       │
│       Betroffener Stromkreis identifiziert:
│       │
│       Schritt 3: ALLE Verbraucher in diesem Kreis abziehen/ausschalten
│       FI + LS einschalten → löst aus?
│       ├── JA → Fehler in der Festverkabelung
│       │   ├── Steckdosen inspizieren (Feuchtigkeit, Salzablagerung)
│       │   ├── Kabelführung inspizieren (Scheuerung, Quetschung)
│       │   ├── Isolationsmessung (Megger, 500V DC)
│       │   │   ├── >1 MΩ → OK (Fehler intermittierend → Feuchtigkeit)
│       │   │   └── <1 MΩ → Isolation defekt → Kabel/Steckdose erneuern
│       │   └── Decksdurchführungen auf Wassereintritt prüfen
│       │
│       └── NEIN → Fehler in einem Verbraucher
│           │
│           Schritt 4: Verbraucher einzeln einstecken
│           Welcher Verbraucher löst den FI aus?
│           ├── Sofort → Gerät defekt (Erdschluss)
│           │   └── Gerät entsorgen oder reparieren lassen
│           └── Nach einiger Zeit → Ableitstrom zu hoch
│               ├── Ableitstrom messen (Zangenamperemeter um L+N)
│               │   ├── >15mA → Gerät defekt
│               │   └── 5–15mA → Grenzwertig, Summierung beachten
│               └── Mehrere Geräte zusammen >30mA → Kreise aufteilen
```

### 7.4 Entscheidungsbaum: Galvanische Korrosion am Unterwasserschiff

```
PROBLEM: Beschleunigte Korrosion an Unterwassermetallen
═══════════════════════════════════════════════════════

START: Korrosion tritt NUR am Landstrom auf?
├── PRÜFEN: Zinkanoden-Verbrauch mit/ohne Landstrom vergleichen
│   ├── Korrosion auch OHNE Landstrom → Galvanisches Problem (Materialauswahl)
│   │   ├── Galvanische Spannungsreihe der Unterwassermetalle prüfen
│   │   ├── Unverträgliche Materialien? (z.B. Alu-Rumpf + Bronze-Propeller)
│   │   ├── Anoden korrekt dimensioniert und kontaktiert?
│   │   └── Siehe Wissensdatei 07.06 (Opferanoden)
│   │
│   └── Korrosion NUR mit Landstrom → Streustromproblem
│       │
│       Schritt 1: Galvanischer Isolator vorhanden?
│       ├── NEIN → Galvanischen Isolator installieren (sofort!)
│       │   └── Problem gelöst? → JA → ENDE (war DC-Korrosion)
│       │                       → NEIN → AC-Leckströme → weiter
│       │
│       └── JA → Isolator funktioniert?
│           ├── Diodentest (Multimeter, Diodenmessung): 0,6V pro Richtung?
│           │   ├── NEIN → Isolator defekt → tauschen
│           │   └── JA → AC-Leckströme (GI schützt nicht vor AC)
│           │
│           Schritt 2: Leckstrom messen
│           ├── Zangenamperemeter um Landstromkabel (alle 3 Leiter zusammen)
│           │   ├── >30mA → Signifikanter Leckstrom → FI müsste auslösen!
│           │   │   └── FI defekt oder nicht vorhanden → reparieren
│           │   ├── 5–30mA → FI-Schwelle nicht erreicht, aber korrosionsrelevant
│           │   │   └── Isolationsmessung aller AC-Kreise
│           │   └── <5mA → Eigener Leckstrom gering
│           │       └── Nachbarboote verursachen Strom über Wasser
│           │
│           Schritt 3: Trenntrafo als ultimative Lösung
│           └── Trenntrafo installieren → eliminiert ALLE galvanischen Ströme
│               └── Zinkanoden-Verbrauch danach beobachten
```

### 7.5 Entscheidungsbaum: Welchen Inverter brauche ich?

```
ENTSCHEIDUNGSHILFE: Inverter-Auswahl für Yachten
═════════════════════════════════════════════════

START: Welche Verbraucher sollen über Inverter laufen?

Schritt 1: AC-Verbraucher-Liste erstellen
├── Ohmsche Lasten (Anlaufstrom ≈ 1×):
│   Kaffeemaschine: ___W, Wasserkocher: ___W, Toaster: ___W,
│   Haartrockner: ___W, Heizlüfter: ___W
│
├── Motorische Lasten (Anlaufstrom 3–8×):
│   Kühlschrank: ___W (×6), Waschmaschine: ___W (×5),
│   Staubsauger: ___W (×3), Werkzeug: ___W (×5)
│
└── Elektronische Lasten (Anlaufstrom ≈ 1×):
    Laptop: ___W, TV: ___W, Router: ___W, Ladegeräte: ___W

Schritt 2: Maximale Gleichzeitigkeit bestimmen
├── Welche Geräte laufen GLEICHZEITIG?
│   → Summe = P_gleichzeitig: ___W
│
├── Höchster Einzelanlaufstrom:
│   → P_surge: ___W
│
└── Benötigte Inverter-Spezifikation:
    Dauerleistung ≥ P_gleichzeitig × 1,2 (Reserve)
    Surge-Rating ≥ P_surge

Schritt 3: Systemspannung wählen
├── 12V-System: Nur bis 1.500W Inverter sinnvoll (DC-Ströme werden zu hoch)
├── 24V-System: Standard für 1.500–5.000W (80% aller Fahrtenyachten)
└── 48V-System: Ab 3.000W empfohlen, Pflicht ab 5.000W

Schritt 4: Stand-Alone oder Kombigerät?
├── Bereits gutes Ladegerät vorhanden? → Stand-Alone Inverter
├── Kein Ladegerät oder Upgrade nötig? → Kombigerät (Inverter/Charger)
├── Generator an Bord? → Quattro (2 AC-Eingänge) oder Kombigerät
└── Nur gelegentlich 230V nötig (Laptop)? → Kleiner Phoenix 300–800W

Schritt 5: Zusatzanforderungen
├── PowerAssist (schwacher Landstrom)? → MultiPlus/Quattro oder Mass Combi
├── Parallelschaltung (Zukunft)? → Victron (VE.Bus) oder Mastervolt (MasterBus)
├── Lithium-Batterien? → BMS-kompatibles Gerät (Victron, Mastervolt)
└── Remote-Monitoring? → Victron (VRM) oder Mastervolt (CZone)

ERGEBNIS: Modell-Empfehlung basierend auf Schritt 1–5
```

---

## 8. FAQ — Häufige Fragen

### 8.1 Grundlagen

**F1: Brauche ich überhaupt einen Wechselrichter?**
A: Wenn Sie 230V-Verbraucher an Bord nutzen möchten (Kaffeemaschine, Mikrowelle, Laptop-Ladegerät, Werkzeug), ohne am Landstrom zu hängen, dann ja. Für Laptops und Handyladung gibt es Alternativen (12V/24V-Ladegeräte, USB-C), aber für Geräte >100W ist ein Inverter die praktischste Lösung. Auf Fahrtenyachten ab 10m gehört ein Inverter/Charger zur Standardausrüstung.

**F2: Was ist der Unterschied zwischen einem Inverter und einem Inverter/Charger?**
A: Ein reiner Inverter (z.B. Victron Phoenix) wandelt nur Batteriestrom in 230V AC um. Ein Inverter/Charger (z.B. Victron MultiPlus) kann zusätzlich die Batterien über Landstrom laden und hat ein automatisches Transfer-Relais, das zwischen Landstrom und Inverter-Betrieb umschaltet. Für die meisten Yachten ist das Kombigerät die bessere Wahl.

**F3: Reine Sinuswelle oder modifizierte — was ist der Unterschied?**
A: Reine Sinuswelle erzeugt identischen Strom wie das Landnetz. Modifizierte Sinuswelle ist eine grobe Annäherung (Trapezwelle) und verursacht Probleme bei vielen Verbrauchern: Motoren überhitzen, Elektronik kann beschädigt werden, Audioanlagen brummen. Im Marineeinsatz nur reine Sinuswelle verwenden.

**F4: Wie viel Watt brauche ich?**
A: Addieren Sie die Wattzahl aller Geräte, die gleichzeitig laufen sollen, und nehmen Sie 20% Reserve. Beispiel: Kaffeemaschine (1.000W) + Kühlschrank (150W) + Laptop (80W) = 1.230W → mindestens 1.500W Inverter. Beachten Sie Anlaufströme bei Motoren (Faktor 3–8).

**F5: 12V oder 24V Systemspannung?**
A: 12V-Systeme sind Standard bei Booten bis 10–12m. Für Inverter >1.500W empfiehlt sich 24V, weil die DC-Ströme sonst zu hoch werden (3.000W bei 12V = 250A → extrem dicke Kabel nötig). Ab 5.000W Inverterleistung ist 48V der Standard.

### 8.2 Landstrom und Sicherheit

**F6: Was ist ein Trenntrafo und brauche ich einen?**
A: Ein Trenntrafo (Isolation Transformer) trennt das Landstromnetz galvanisch vom Bordnetz. Das bedeutet: kein Strom fließt über den Schutzleiter zwischen Steg und Boot. Empfohlen ab 12m Bootslänge, Pflicht ab 18m. Besonders wichtig bei Metallrümpfen, Langfahrt (wechselnde Marinas), und in Gebieten mit schlechter Marina-Elektrik (Mittelmeer, Asien).

**F7: Was ist ein Galvanischer Isolator?**
A: Ein kleines Gerät im Schutzleiter (PE) des Landstromkabels, das galvanische Gleichströme blockiert (bis ca. 1,2V), aber den Schutzleiter für Wechselstrom-Fehlerströme durchlässig hält. Günstige Alternative zum Trenntrafo (€100–€300 vs. €800–€3.500), bietet aber weniger Schutz. Minimum-Empfehlung für jedes Boot mit Landstrom.

**F8: Warum ist ein FI-Schutzschalter Pflicht?**
A: Der FI (Fehlerstromschutzschalter, 30mA) erkennt, wenn Strom über eine Person zur Erde fließt, und schaltet in Millisekunden ab. An Bord — wo man barfuß auf nassen Flächen steht — ist das lebenswichtig. ISO 13297 schreibt FI-Schutz für alle AC-Kreise an Bord vor. Es gibt keine Ausnahmen.

**F9: Welchen FI-Typ brauche ich?**
A: Mindestens Typ A (erkennt AC- und pulsierende DC-Fehlerströme). Typ B empfohlen wenn Frequenzumrichter (Inverter-Klimaanlagen) oder DC-Ladestationen vorhanden sind. Typ AC ist veraltet und nicht ausreichend.

**F10: Was ist Electric Shock Drowning (ESD)?**
A: Wenn Leckströme über den Rumpf ins Wasser fließen, können Schwimmer in der Nähe des Bootes einen Stromschlag erleiden. Bereits 10mA AC im Wasser reichen für Muskellähmung — die Person ertrinkt, ohne sich befreien zu können. ESD ist die gefährlichste Folge fehlerhafter AC-Installationen an Bord. Prävention: Trenntrafo, FI-Schutz, nie im Hafen schwimmen wenn Boote am Landstrom hängen.

**F11: Was passiert bei falscher Polarität am Landstrom?**
A: Sind L und N vertauscht, funktionieren einpolige Schalter nicht korrekt (schalten N statt L ab), und manche Schutzmaßnahmen versagen. Ein Polaritätsprüfer am Landstromeingang ist Pflicht. Ein Trenntrafo macht das Polaritätsproblem irrelevant, da er die Bord-Polarität unabhängig definiert.

### 8.3 Technik und Installation

**F12: Wie weit darf der Inverter von der Batterie entfernt sein?**
A: So nah wie möglich! Maximal 2m empfohlen, 4m akzeptabel. Bei 3.000W/24V fließen 125A DC — jeder Meter Kabel verursacht Spannungsabfall und Erwärmung. Bei 2m Entfernung und 3.000W/24V benötigen Sie mindestens 50mm² DC-Kabel.

**F13: Kann ich mehrere Inverter parallel schalten?**
A: Ja, bei Victron (MultiPlus, Quattro) bis zu 6 Geräte parallel. Bei Mastervolt über MasterBus ebenfalls. Die Geräte synchronisieren sich automatisch über VE.Bus / MasterBus. Wichtig: nur identische Modelle parallel schalten.

**F14: Was bedeutet PowerAssist?**
A: PowerAssist (Victron) bzw. Power Sharing (Mastervolt) bedeutet: der Inverter ergänzt den Landstrom aus der Batterie, wenn der Landstromanschluss nicht genug Leistung liefert. Beispiel: 6A Landstrom (1.380W), aber 3.000W benötigt → Inverter liefert 1.620W aus der Batterie. So fliegt die Steg-Sicherung nicht.

**F15: Muss der Inverter belüftet werden?**
A: Ja! Inverter erzeugen Abwärme (5–10% der umgesetzten Leistung). Ein 3.000W Inverter bei Volllast produziert 150–300W Wärme. Mindestens 100mm Abstand zu allen Seiten, keine geschlossenen Schränke ohne Belüftung. Bei >3.000W aktive Belüftung (Lüfter) empfohlen.

**F16: Kann ich den Inverter im Motorraum montieren?**
A: Grundsätzlich möglich, aber mit Einschränkungen: hohe Umgebungstemperatur reduziert die Dauerleistung, Dieseldämpfe können Kontakte korrodieren, und in Kraftstoffumgebungen muss der Inverter ISO 8846 (zündfunkenfrei) erfüllen. Besser: separater, belüfteter Raum neben dem Motorraum.

### 8.4 Betrieb und Wartung

**F17: Wie hoch ist der Leerlaufverbrauch eines Inverters?**
A: Typisch 10–25W bei mittelgroßen Invertern (2.000–3.000W). Das entspricht 10–25Ah/24V pro Tag — nicht zu vernachlässigen! Eco-Modus reduziert auf 2–5W, hat aber eine Einschaltverzögerung von 1–3 Sekunden. Tipp: Inverter über Schalter ausschalten wenn nicht benötigt.

**F18: Wie lange halten die Batterien mit dem Inverter?**
A: Faustregel: Nutzbare Batteriekapazität (Ah) × Systemspannung (V) × Inverter-Wirkungsgrad (0,9) / Verbraucherleistung (W) = Betriebsdauer (h). Beispiel: 400Ah × 24V × 0,9 / 500W = 17,3 Stunden. Bei LiFePO4 ist die nutzbare Kapazität ~90%, bei Blei-AGM ~50%.

**F19: Wie oft muss ich den Inverter warten?**
A: Jährlich: Luftfilter/Lüfter reinigen, Kabelverbindungen auf festen Sitz prüfen, Sicherungen visuell prüfen, DC-Spannungsabfall unter Last messen. Alle 5 Jahre: professionelle Inspektion (Kondensatoren, Relais, Lüfterlager). Lebensdauer eines guten Marine-Inverters: 10–15 Jahre.

**F20: Kann der Inverter meine Batterien beschädigen?**
A: Indirekt: Wenn der Inverter die Batterien zu tief entlädt (unter die empfohlene Entladetiefe), verkürzt das die Lebensdauer drastisch. Konfigurieren Sie die Unterspannungsabschaltung korrekt: Blei-Säure: 11,5V (12V) / 23,0V (24V), AGM: 11,0V / 22,0V, LiFePO4: über BMS gesteuert (typisch 10,0V / 20,0V).

### 8.5 Spezialfragen

**F21: Brauche ich einen Trenntrafo UND einen Galvanischen Isolator?**
A: Nein. Ein Trenntrafo bietet umfassendere Isolation als ein Galvanischer Isolator. Wenn ein Trenntrafo vorhanden ist, ist kein zusätzlicher Galvanischer Isolator nötig.

**F22: Kann ich meinen Landstrom über einen Adapter von 32A auf 16A reduzieren?**
A: Ja, das ist Standard und sicher, solange der Adapter korrekt verdrahtet ist und die Boot-interne Absicherung auf 16A eingestellt wird. Wichtig: NIE umgekehrt (16A-Steckdose mit 32A-Stecker) — das umgeht die Absicherung!

**F23: Was ist der Unterschied zwischen kVA und kW beim Trenntrafo?**
A: kVA (Kilovoltampere) ist die Scheinleistung, kW die Wirkleistung. Bei rein ohmschen Lasten (Heizung, Wasserkocher) gilt kVA ≈ kW. Bei induktiven/kapazitiven Lasten (Motoren, Schaltnetzteile) ist kVA > kW. Einen Trenntrafo immer nach kVA dimensionieren. 3,5kVA Trafo für 16A Landstrom, 7,5kVA für 32A.

**F24: Funktioniert mein europäisches 230V-System in den USA (120V/60Hz)?**
A: Nicht direkt. Sie benötigen entweder: (a) einen Autotransformer (120V→240V), (b) einen Adapter für 120V-Steckdosen und Verbraucher, die 120V vertragen, oder (c) Ihren Inverter/Charger, der auf beiden Eingangsspannungen arbeitet (die meisten Victron und Mastervolt akzeptieren 90–265V AC Eingang). Achtung: die Frequenz wechselt von 50Hz auf 60Hz — für die meisten Verbraucher kein Problem, aber Uhren mit Netzfrequenz-Basis gehen falsch.

**F25: Wie schütze ich mein System vor Blitzeinschlag?**
A: Vollständiger Blitzschutz für AC-Systeme umfasst: (a) Überspannungsableiter (SPD Typ 2) am Landstromeingang, (b) Überspannungsableiter am Inverter AC-Ausgang, (c) Varistoren am DC-Eingang des Inverters, (d) Erdung über Kupferband zum Kiel. Kosten: €200–€500 für Grundschutz. Bei direktem Einschlag hilft nur Versicherung.

**F26: Kann ich den Inverter über Solarstrom betreiben?**
A: Nicht direkt — der Inverter braucht eine Batterie als Puffer. Die Solaranlage lädt über einen MPPT-Regler die Batterien, und der Inverter entnimmt den Strom aus den Batterien. Das ist die Standardkonfiguration auf Fahrtenyachten. Der Victron Cerbo GX kann Solarregler, Batteriemonitor und Inverter in einem System zusammenführen.

**F27: Was bedeutet "Transfer-Relais" im Inverter/Charger?**
A: Das Transfer-Relais schaltet automatisch zwischen den AC-Quellen um. Wenn Landstrom angeschlossen wird, schaltet das Relais den AC-Ausgang von "Inverter" auf "Landstrom" (Durchleitung) und startet gleichzeitig das Ladegerät. Fällt der Landstrom aus, schaltet es zurück auf Inverter-Betrieb. Bei guten Geräten (Victron MultiPlus) dauert die Umschaltung <20ms — unterbrechungsfrei für die meisten Verbraucher (UPS-Funktion).

**F28: Ist ein FI Typ B wirklich nötig?**
A: Typ A reicht für die meisten Installationen. Typ B wird empfohlen, wenn Frequenzumrichter (VFDs) für Klimaanlagen oder Wassermacher vorhanden sind, da diese reine DC-Fehlerströme erzeugen können, die Typ A nicht erkennt. Auf Superyachten mit vielen Frequenzumrichtern ist Typ B Standard.

**F29: Kann ich einen normalen Haushaltsinverter auf dem Boot verwenden?**
A: Technisch möglich, aber nicht empfohlen. Haushaltsinverter sind nicht für die maritime Umgebung gebaut: keine Salzwasser-Beständigkeit, keine Vibrationsfestigkeit, keine Marine-Zertifizierung (CE/ISO 13297), kein Schutz gegen Kondenswasser, keine UPS-Funktion, kein PowerAssist. Im Garantie- und Versicherungsfall problematisch.

**F30: Mein Trenntrafo brummt nachts — was tun?**
A: Häufigste Ursache: DC-Anteil im Landstrom (durch unsymmetrische Verbraucher in der Marina). Lösungen: (a) DC-Blocker vorschalten (€100–€300), (b) Trafo auf Schwingungsdämpfer montieren (Sylomer, Gummimatten), (c) Vergussmasse auf dem Trafokern prüfen (nachvergießen lassen), (d) Marina oder Steg-Position wechseln. Alternativ: Trenntrafo nur tagsüber am Landstrom, nachts auf Inverter umschalten.

### 8.6 Wartung und Lebensdauer

**F31: Wie lange hält ein Trenntrafo?**
A: Ein gut installierter Ringkern-Trenntrafo hält praktisch unbegrenzt (20–30+ Jahre). Es gibt keine Verschleißteile. Die einzige Alterung betrifft die Isolation der Wicklungen (Temperaturklasse F: 155°C Grenztemperatur). Jährliche Sichtprüfung auf Feuchtigkeit, Korrosion und Befestigungszustand genügt. Ein Isolationsmessgerät (Megger) kann die Wicklungsisolation alle 5 Jahre prüfen.

**F32: Wann muss ich den FI-Schutzschalter tauschen?**
A: Die Testtaste sollte monatlich betätigt werden (ISO 13297 Empfehlung). Wenn der FI nicht mehr korrekt auslöst: sofort tauschen. Lebensdauer mechanisch: ca. 10.000 Schaltzyklen. Empfehlung: FI alle 10 Jahre präventiv tauschen, in feuchter Umgebung alle 5–7 Jahre. Salzkorrosion kann die Mechanik vorzeitig beschädigen.

**F33: Kann ich meinen Inverter/Charger per Firmware updaten?**
A: Bei Victron: Ja — über VictronConnect App (Bluetooth) oder VE.Bus (über MK3-USB-Adapter). Firmware-Updates bringen oft wichtige Verbesserungen (neue Batterieprofile, Bugfixes, bessere PowerAssist-Regelung). Mastervolt: Updates über MasterAdjust Software. Xantrex: begrenzte Update-Möglichkeiten. Immer vor Langfahrt auf aktuelle Firmware aktualisieren.

**F34: Wie prüfe ich die Isolationsfestigkeit meiner AC-Installation?**
A: Mit einem Isolationsmessgerät (Megger) bei 500V DC. Messung zwischen jedem Leiter (L, N) und PE. Mindestwert: 1 MΩ (besser >10 MΩ). Messung bei abgeschalteten Verbrauchern und ausgeschaltetem Inverter/Charger. Achtung: Empfindliche Elektronik (Inverter, Charger, VFDs) VOR der Messung abklemmen — die 500V Prüfspannung kann diese beschädigen!

**F35: Mein Ladegerät im Inverter/Charger lädt nur noch langsam — was tun?**
A: Mögliche Ursachen: (a) Temperatursensor meldet hohe Temperatur → Ladestrom reduziert (Sensor korrekt positioniert?), (b) Batteriespannung stimmt nicht mit Einstellung überein → Ladeprofile prüfen, (c) Kabelverbindungen korrodiert → Übergangswiderstand → Spannungsabfall → Charger denkt Batterie ist voller als sie ist, (d) Batterie-Alterung → Kapazität gesunken, Innenwiderstand gestiegen → Absorptionsphase wird schneller erreicht.

### 8.7 Spezielle Situationen

**F36: Wie handle ich Landstrom in den USA (120V/60Hz)?**
A: Optionen: (a) Die meisten modernen Inverter/Charger (Victron MultiPlus, Mastervolt Mass Combi) akzeptieren 90–265V AC Eingang und passen sich automatisch an. Das Ladegerät funktioniert, aber mit reduziertem Strom (halbe Spannung = halber Strom bei gleicher Leistung, wenn Leistungsbegrenzung aktiv). (b) Victron Autotransformer 120/240V verwandelt 120V in 240V für den vollen Ladestrom. (c) Pass-Through: nur 120V-fähige Verbraucher über Landstrom, 230V über Inverter aus Batterie. (d) Adaptercheck: US-NEMA-Stecker auf CEE-Adapter — Polarität und Erdung beachten!

**F37: Kann ich den Inverter als Notstromversorgung (USV) für meinen Plotter/Router nutzen?**
A: Ja, wenn der Inverter eine Transfer-Relais-Umschaltzeit von <20ms hat (alle Victron MultiPlus/Quattro, Mastervolt Mass Combi). Schaltnetzteile (wie in Plottern, Routern, NAS) überbrücken 20ms problemlos. Achtung: Eco-Modus muss deaktiviert sein, sonst ist die Einschaltverzögerung zu lang (1–3s).

**F38: Mein Generator liefert unsauberen Strom — schadet das meinen Geräten?**
A: Kleine Generatoren (<5kW) mit Trägheits-AVR (Automatic Voltage Regulator) haben oft THD von 5–15%. Empfindliche Elektronik (Ladegeräte, PCs) kann dadurch gestört werden. Lösungen: (a) Generator mit Inverter-Technologie (Honda EU-Serie, Fischer Panda iSeries) liefern THD <3%, (b) Generator über den AC-Eingang des Inverter/Chargers führen — der Charger filtert den Strom und die Batterie/Inverter liefern sauberen Strom an die Verbraucher.

**F39: Ich will eine Induktionskochplatte über den Inverter betreiben — geht das?**
A: Grundsätzlich ja, aber mit Einschränkungen: (a) Induktionskochplatten haben 1.500–3.500W → Inverter entsprechend dimensionieren, (b) hoher Anlaufstrom (Faktor 1,5–2), (c) nicht-sinusförmiger Stromverbrauch (VFD im Kochfeld) → Inverter mind. 30% überdimensionieren, (d) bei 2.000W Kochplatte auf 24V: 83A DC-Dauerstrom → massive DC-Kabel nötig. Fazit: Machbar mit 3.000W+ Inverter auf 24V-System, 48V bevorzugt. Gaskocher bleibt auf vielen Booten die energieeffizientere Lösung.

**F40: Mein Boot hat ein 12V-System, und ich möchte einen 3.000W-Inverter — geht das?**
A: Technisch existieren 12V/3.000W-Inverter (z.B. Victron MultiPlus 12/3000/120), aber die DC-Ströme sind enorm: 250A Dauer, 500A Surge. Das erfordert 95mm²-Kabel (oder dicker), massive Sicherungen (300A+) und perfekte Verbindungen. Jeder Milliohm Übergangswiderstand wird zum Problem. Bei >2.000W Dauerlast empfehlen wir dringend den Umstieg auf 24V — die Investition in ein neues System amortisiert sich durch dünnere Kabel, weniger Verluste und höhere Zuverlässigkeit.

---

## 9. Glossar

| Nr. | Begriff | Erklärung |
|-----|---------|-----------|
| 1 | **AC (Alternating Current)** | Wechselstrom — Strom wechselt periodisch die Richtung (230V, 50Hz in Europa) |
| 2 | **ABYC** | American Boat and Yacht Council — US-Normungsgremium für Boote |
| 3 | **Ableitstrom** | Unvermeidlicher kleiner Strom von L/N zur Erde durch kapazitive Kopplung und Isolation (normal bis 3,5mA pro Gerät) |
| 4 | **Anlaufstrom (Inrush/Surge)** | Kurzzeitig erhöhter Strom beim Einschalten von Motoren oder Transformatoren (Faktor 3–8× Nennstrom) |
| 5 | **Autotransformer** | Spartransformator zur Spannungsanpassung (z.B. 120V↔230V), KEINE galvanische Trennung |
| 6 | **Bonding-System** | Verbindung aller metallischen Teile an Bord untereinander und mit dem Unterwasserteil (Potentialausgleich) |
| 7 | **CEE-Stecker** | Standardisierte Industriestecker nach EN 60309 (blau = 230V, rot = 400V Drehstrom) |
| 8 | **Cerbo GX** | Victron Energy System-Gateway für Monitoring und Steuerung aller Victron-Komponenten |
| 9 | **CZone** | Digitales Bord-Schaltsystem (Mastervolt/Navico) — vernetztes Energiemanagement |
| 10 | **DC (Direct Current)** | Gleichstrom — Strom fließt in eine Richtung (12V, 24V, 48V Bordnetz) |
| 11 | **DC-Blocker** | Filter, der Gleichstromanteile im Landstrom blockiert (verhindert Trafo-Brummen) |
| 12 | **Eco-Modus (Search Mode)** | Energiesparfunktion des Inverters — sendet periodisch Suchpulse, startet bei erkannter Last |
| 13 | **ELCI** | Equipment Leakage Current Interrupter — FI für den gesamten Landstromeingang (alle Leiter überwacht) |
| 14 | **EMV** | Elektromagnetische Verträglichkeit — Fähigkeit, andere Geräte nicht zu stören und selbst nicht gestört zu werden |
| 15 | **Erdschluss** | Unerwünschter Kontakt eines stromführenden Leiters mit dem Schutzleiter oder Erde |
| 16 | **ESD (Electric Shock Drowning)** | Ertrinken durch Stromschlag — Leckströme im Wasser lähmen Schwimmer |
| 17 | **FI (Fehlerstromschutzschalter)** | RCD (Residual Current Device) — erkennt Fehlerströme und schaltet ab (30mA, <300ms) |
| 18 | **Galvanischer Isolator** | Gerät im PE-Leiter mit antiparallelen Dioden — blockiert galvanische DC-Ströme |
| 19 | **Galvanische Korrosion** | Elektrochemische Korrosion durch Kontakt verschiedener Metalle in einem Elektrolyten (Seewasser) |
| 20 | **H-Brücke** | Schaltungstopologie mit 4 Halbleitern zur Erzeugung von Wechselspannung aus Gleichspannung |
| 21 | **IGBT** | Insulated Gate Bipolar Transistor — Leistungshalbleiter für große Inverter |
| 22 | **IMD** | Insulation Monitoring Device — Isolationsüberwachung für IT-Netze |
| 23 | **Inverter** | Wechselrichter — wandelt DC (Batterie) in AC (230V, 50Hz) |
| 24 | **ISO 13297** | Internationale Norm für AC-Installationen auf kleinen Wasserfahrzeugen |
| 25 | **IT-Netz** | Isoliertes Netz (Isolated Terra) — kein Leiter hat Erdverbindung |
| 26 | **Leitungsschutzschalter (LS)** | Automatische Sicherung gegen Überstrom und Kurzschluss (z.B. B16A) |
| 27 | **MasterBus** | CAN-basiertes Kommunikationsprotokoll von Mastervolt für Energiemanagement |
| 28 | **MOSFET** | Metal-Oxide-Semiconductor Field-Effect Transistor — Leistungshalbleiter für kleine/mittlere Inverter |
| 29 | **MPPT** | Maximum Power Point Tracking — Solarregler mit optimaler Leistungsanpassung |
| 30 | **Pass-Through** | Betriebsmodus des Inverter/Chargers — Landstrom wird direkt an die Verbraucher durchgeleitet |
| 31 | **PE (Protective Earth)** | Schutzleiter (grün-gelb) — verbindet Gehäuse/Rumpf mit dem Erdungssystem |
| 32 | **Polaritätsprüfer** | Gerät zur Überprüfung der korrekten Verdrahtung (L, N, PE) am Landstromanschluss |
| 33 | **PowerAssist** | Victron-Funktion: Inverter ergänzt den Landstrom bei Überlast aus der Batterie |
| 34 | **PWM** | Pulsbreitenmodulation — Verfahren zur Erzeugung einer Sinuswelle aus Gleichspannung |
| 35 | **RCD** | Residual Current Device — internationaler Begriff für FI-Schutzschalter |
| 36 | **Reine Sinuswelle** | Ausgangswellenform eines hochwertigen Inverters (THD <3%), identisch mit Netzstrom |
| 37 | **THD** | Total Harmonic Distortion — Maß für die Verzerrung der Sinuswelle (ideal: 0%, akzeptabel: <5%) |
| 38 | **TN-S-Netz** | Erdungssystem: Sternpunkt geerdet, separater PE- und N-Leiter |
| 39 | **Transfer-Relais** | Automatischer Umschalter zwischen AC-Quellen (Landstrom ↔ Inverter) |
| 40 | **Trenntrafo** | Isolation Transformer — galvanische Trennung zwischen Landstrom und Bordnetz |
| 41 | **TT-Netz** | Erdungssystem: Quelle und Verbraucher haben separate Erder |
| 42 | **UPS** | Uninterruptible Power Supply — unterbrechungsfreie Stromversorgung (Umschaltzeit <20ms) |
| 43 | **VE.Bus** | Victron Energy Kommunikationsbus für MultiPlus/Quattro-Geräte |
| 44 | **VE.Direct** | Victron Energy Kommunikationsprotokoll für kleinere Geräte (MPPT, Shunt, Phoenix) |
| 45 | **VFD** | Variable Frequency Drive — Frequenzumrichter für drehzahlgeregelte AC-Motoren |
| 46 | **VRM** | Victron Remote Management — Cloud-Portal zur Fernüberwachung von Victron-Systemen |
| 47 | **Zwischenkreisspannung** | Interne DC-Spannung im Inverter (ca. 350–400V DC) nach dem Hochsetzsteller |
| 48 | **AVR (Automatic Voltage Regulator)** | Spannungsregler im Generator — hält die Ausgangsspannung konstant |
| 49 | **Boost Converter (Hochsetzsteller)** | DC/DC-Wandler, der niedrige Batteriespannung auf Zwischenkreisspannung erhöht |
| 50 | **Crest-Faktor** | Verhältnis Spitzenwert/Effektivwert eines Signals (Sinus: 1,41; Schaltnetzteil: 2–3) |
| 51 | **Derating** | Leistungsreduzierung bei erhöhter Umgebungstemperatur (typisch ab 25–40°C linear) |
| 52 | **DOD (Depth of Discharge)** | Entladetiefe einer Batterie (AGM: max. 50%, LFP: max. 90%) |
| 53 | **ELCI** | Equipment Leakage Current Interrupter — FI für den gesamten Landstromeingang (US-Norm) |
| 54 | **Fehlerstrom** | Differenz zwischen hin- und rückfließendem Strom — fließt über Erde/Person ab |
| 55 | **Float (Erhaltungsladung)** | Niedrige Ladespannung, die die Batterie voll hält (12V: 13,2–13,8V je nach Typ) |
| 56 | **Galvanisches Element** | Spannungsquelle aus zwei verschiedenen Metallen in einem Elektrolyten (Seewasser) |
| 57 | **ICCP** | Impressed Current Cathodic Protection — aktiver Korrosionsschutz mit Fremdstrom |
| 58 | **K-Faktor (Trafo)** | Maß für die Oberschwingungsbelastbarkeit eines Transformators (K1 = Standard, K13 = hoch) |
| 59 | **Leitungsschutzschalter (LS/MCB)** | Automatische Sicherung: B-Charakteristik = 3–5× (Standard), C = 5–10× (Motoren) |
| 60 | **Magnetostriktion** | Längenänderung des Trafokerns im Magnetfeld — Ursache für Brummgeräusch |
| 61 | **Modbus** | Serielles Kommunikationsprotokoll für industrielle Geräte (RS485 oder TCP/IP) |
| 62 | **N-Leiter (Neutralleiter)** | Rückleiter im AC-Netz (blau), führt normalerweise keine gefährliche Spannung gegen Erde |
| 63 | **NMEA 2000** | Marine-Bussystem für Navigationselektronik (CAN-basiert) |
| 64 | **PFC (Power Factor Correction)** | Schaltung zur Verbesserung des Leistungsfaktors in Schaltnetzteilen |
| 65 | **Scheinleistung [VA]** | Produkt aus Spannung und Strom (S = U × I), enthält Wirk- und Blindleistung |
| 66 | **Selektive Staffelung** | FI-Anordnung: Vorschalter 300mA (selektiv, "S") + nachgeschaltete 30mA-FIs |
| 67 | **Soft-Starter** | Gerät zur Begrenzung des Anlaufstroms von Motoren (reduziert Surge um 50–80%) |
| 68 | **SPD (Surge Protective Device)** | Überspannungsschutz (Typ 1 = Blitz, Typ 2 = Überspannung, Typ 3 = Feinschutz) |
| 69 | **Venus OS** | Linux-basiertes Betriebssystem auf Victron GX-Geräten (Open Source) |
| 70 | **Wirkleistung [W]** | Tatsächlich nutzbare Leistung (P = U × I × cos φ) |

---

## 10. Schnell-Referenz

### 10.1 Landstrom-Eingangsanschluss — Checkliste

```
LANDSTROM-ANSCHLUSS — SCHNELLPRÜFUNG
═════════════════════════════════════

□ CEE-Stecker korrekt verriegelt (Drehverschluss)
□ Polaritätsprüfer zeigt "korrekt" (3 grüne LEDs)
□ FI-Schutzschalter eingeschaltet, Testtaste geprüft
□ Leitungsschutzschalter eingeschaltet
□ Batterie-Ladegerät nimmt Ladung auf
□ Spannung am Verteiler: ___V (Soll: 220–240V)
□ Kein Brummen/Erwärmung am Kabel oder Stecker
□ Galvanischer Isolator / Trenntrafo aktiv
```

### 10.2 Inverter-Dimensionierung — Schnelltabelle

| Boot-Typ | Typische Last | Empfehlung Inverter | Empfehlung System |
|----------|--------------|--------------------|--------------------|
| 8–10m Segler, Wochenende | Laptop, Ladegeräte | Phoenix 12/800 | 12V, 200Ah AGM |
| 10–12m Segler, Küste | + Kaffeemaschine | MultiPlus 12/1600 | 12V, 300Ah AGM/LFP |
| 12–15m Segler, Fahrt | + Mikrowelle, Waschmaschine | MultiPlus 24/3000 | 24V, 400Ah LFP |
| 15–18m Segler, Blauwasser | + Klimaanlage (klein) | Quattro 24/5000 | 24V, 600Ah LFP |
| 12–15m Motoryacht | + Klimaanlage, Herd | MultiPlus 24/3000 | 24V, 400Ah LFP |
| 18–24m Motoryacht | Alles | Quattro 48/8000 | 48V, 800Ah LFP |
| >24m Yacht | Alles + redundant | 2× Quattro parallel | 48V, 1.200Ah+ LFP |

### 10.3 FI-Schutz — Schnellauswahl

| Situation | FI-Typ | Auslösestrom |
|-----------|--------|-------------|
| Standard-Steckdosen | Typ A | 30mA |
| Nassräume (Dusche) | Typ A | 30mA (10mA wenn separater FI) |
| Inverter-Klimaanlage | Typ F oder B | 30mA |
| Vorschalter (selektiv) | Typ A | 100mA oder 300mA |
| Superyacht mit VFDs | Typ B | 30mA |

### 10.4 Korrosionsschutz — Schnellauswahl

| Situation | Maßnahme |
|-----------|----------|
| GFK-Boot, nur gelegentlich am Landstrom | Galvanischer Isolator (Minimum) |
| GFK-Boot, häufig am Landstrom | Trenntrafo empfohlen |
| Alu-Rumpf | Trenntrafo PFLICHT |
| Stahl-Rumpf | Trenntrafo PFLICHT |
| Langfahrt, wechselnde Marinas | Trenntrafo + Polaritätsprüfer |
| Marina mit bekannten Leckstromproblemen | Trenntrafo + ICCP |

### 10.5 DC-Kabelquerschnitt zum Inverter — Schnelltabelle (24V, 2m, max. 3% Spannungsabfall)

| Inverter-Leistung | Querschnitt | Sicherung |
|-------------------|------------|-----------|
| 800W | 16 mm² | 50A |
| 1.200W | 25 mm² | 80A |
| 1.600W | 25 mm² | 100A |
| 2.000W | 35 mm² | 125A |
| 3.000W | 50 mm² | 175A |
| 5.000W | 70 mm² | 250A |

### 10.6 Normen-Schnellreferenz

| Norm | Thema | Schlüsselanforderung |
|------|-------|---------------------|
| ISO 13297 | AC an Bord | FI 30mA auf allen Kreisen, marine Kabel, Polaritätsprüfung |
| ISO 10133 | DC an Bord | Absicherung, Kabelquerschnitte, Batterie-Trennung |
| IEC 60092-507 | Schiffs-Elektrik allgemein | Installationsstandards, Prüfungen |
| IEC 61558-2-4 | Trenntrafos | Isolationsfestigkeit, Schutzkappen, Prüfzyklen |
| EN 60309-2 | CEE-Stecker | Blaue Stecker 230V, Kontaktbelegung |
| IEC 60364-7-709 | Marinas | Erdung, Absicherung am Steg |

### 10.7 Internationale Landstrom-Standards — Revier-Übersicht

| Region | Spannung | Frequenz | Stecker | Erdung | Qualität | Besonderheiten |
|--------|----------|----------|---------|--------|----------|----------------|
| Nordeuropa (DE, NL, DK, SE) | 230V | 50Hz | CEE blau 16/32A | Sehr gut (TN-S) | Hoch | FI am Steg, gute Erdung |
| UK, Irland | 230V | 50Hz | BS 1363 / CEE | Gut (TN-S) | Hoch | Adapter nötig, RCD am Steg |
| Mittelmeer (FR, ES, IT, HR) | 230V | 50Hz | CEE blau / Schuko | Variable | Mittel–Niedrig | Polaritätsfehler häufig (15–25%), Erdung fragwürdig |
| Griechenland, Türkei | 230V | 50Hz | CEE blau / Schuko | Schlecht–Mittel | Niedrig–Mittel | Spannungsschwankungen (200–250V), fehlende Erdung häufig |
| USA Ostküste | 120V | 60Hz | NEMA 5-15/TT-30 | Gut | Hoch | 120V! Adapter + ggf. Autotransformer |
| USA Westküste | 120V | 60Hz | NEMA 5-15/TT-30 | Gut | Hoch | 120V! Viele Marinas mit 240V/50A verfügbar |
| Karibik | 120V/230V | 60Hz | NEMA / CEE gemischt | Variable | Niedrig–Mittel | Spannungs-/Frequenzwechsel je Insel! |
| Südostasien (Thailand, Malaysia) | 230V | 50Hz | Diverse | Schlecht | Niedrig | Keine Standards, Adaptersalat, oft keine Erdung |
| Australien, Neuseeland | 230V | 50Hz | AS 3112 | Gut | Hoch | Strenge Vorschriften, RCD am Steg |
| Kanaren, Madeira, Azoren | 230V | 50Hz | CEE blau / Schuko | Mittel | Mittel | Teils alte Infrastruktur |
| Pazifik (Fiji, Tonga) | 230V/240V | 50Hz | Diverse | Schlecht | Niedrig | Oft Generator statt Netz, keine Marinas |

**AYDI-Empfehlung nach Revier:**

| Revier | Galvanischer Isolator | Trenntrafo | Polaritätsprüfer | Adapter-Set | Autotransformer |
|--------|----------------------|------------|-------------------|-------------|-----------------|
| Ostsee/Nordsee | Empfohlen | Optional | Empfohlen | EU-Standard | Nein |
| Mittelmeer | Pflicht | Dringend empfohlen | PFLICHT | EU + Schuko-Adapter | Nein |
| Atlantiküberquerung + Karibik | Pflicht | PFLICHT | PFLICHT | Universal-Set | JA (120V→230V) |
| Pazifik-Rundreise | Pflicht | PFLICHT | PFLICHT | Universal-Set | JA |
| UK/Irland | Empfohlen | Optional | Empfohlen | UK BS-Adapter | Nein |

### 10.8 Leistungsaufnahme typischer Bordverbraucher — Referenztabelle

| Verbraucher | Nennleistung | Betriebsart | Täglicher Verbrauch (typisch) | Über Inverter sinnvoll? |
|-------------|-------------|-------------|-------------------------------|------------------------|
| Laptop (laden) | 45–90W | 2–4h | 100–250Wh | Ja (oder 12V-Adapter) |
| Handy laden (USB) | 10–25W | 2–3h | 20–60Wh | Nein (USB direkt von 12V) |
| Tablet laden | 15–30W | 1–2h | 15–50Wh | Nein (USB direkt von 12V) |
| LED-Beleuchtung | 5–20W/Raum | 4–8h | 20–160Wh | Nein (12V-LED!) |
| Router/WiFi-Booster | 10–25W | 24h | 240–600Wh | Ja (oder 12V-Modell) |
| Kaffeemaschine (Pad/Kapsel) | 800–1.400W | 10–15 min | 130–350Wh | Ja |
| Kaffeevollautomat | 1.200–1.800W | 15–20 min | 300–600Wh | Ja (Surge beachten) |
| Mikrowelle | 800–1.200W | 5–15 min | 70–300Wh | Ja |
| Toaster | 800–1.200W | 3–5 min | 40–100Wh | Ja |
| Wasserkocher | 1.500–2.200W | 3–5 min | 75–180Wh | Ja (Inverter groß genug?) |
| Haartrockner | 1.000–2.200W | 5–10 min | 85–370Wh | Ja (ohmsche Last, einfach) |
| Staubsauger | 600–1.400W | 10–20 min | 100–470Wh | Ja (Anlaufstrom!) |
| Waschmaschine (kalt) | 200–400W Motor | 60–90 min | 200–600Wh | Ja (Anlaufstrom!) |
| Waschmaschine (40°C) | + 1.500–2.000W Heizung | 90–120 min | 800–2.000Wh | Ja (hohe Leistung!) |
| Geschirrspüler | 200–400W + 1.500W Heizung | 60–120 min | 600–1.800Wh | Möglich (große Batterie) |
| Warmwasserboiler (230V) | 500–1.500W | 2–4h | 1.000–6.000Wh | Nur am Landstrom! |
| Klimaanlage (klein) | 500–1.500W | 4–12h | 2.000–18.000Wh | Am Landstrom/Generator |
| Klimaanlage (Inverter-Typ) | 300–1.000W | 4–12h | 1.200–12.000Wh | Bedingt (große Batterie) |
| Werkzeug: Bohrmaschine | 400–800W | 0,5–2h | 200–1.600Wh | Ja (Akku-Werkzeug besser) |
| Werkzeug: Winkelschleifer | 800–1.200W | 0,5–1h | 400–1.200Wh | Ja (Surge 8×!) |
| Werkzeug: Stichsäge | 400–700W | 0,5–1h | 200–700Wh | Ja |
| Tauchkompressor | 1.500–3.000W | 1–2h | 1.500–6.000Wh | Am Generator |
| Wassermacher (Umkehrosmose) | 200–800W | 2–6h | 400–4.800Wh | Ja (oft 12V/24V-Modell) |

### 10.9 Typische Fehlentscheidungen — Was NICHT tun

| Fehlentscheidung | Warum falsch | Richtige Alternative |
|------------------|-------------|---------------------|
| Modifizierten Sinuswellen-Inverter kaufen "weil billiger" | Beschädigt empfindliche Geräte, Motoren brummen/überhitzen | Immer reinen Sinuswellen-Inverter wählen |
| 12V-System für 3.000W Inverter beibehalten | 250A DC = extreme Kabel, Verluste, Brandrisiko | Auf 24V oder 48V umstellen |
| Inverter im geschlossenen Schrank montieren | Übertemperatur → Derating → Abschaltung | Belüfteten Einbauort wählen, Mindestabstände |
| Keinen FI einbauen "weil der im Hafen schon einen hat" | Marina-FI schützt nicht das Bordnetz | FI 30mA Typ A auf JEDEM AC-Kreis an Bord |
| Billigen Landstromadapter ohne Erde verwenden | Kein Schutzleiter → lebensgefährlich | Nur geerdete Adapter, Polarität prüfen |
| Galvanischen Isolator weglassen "weil GFK-Rumpf" | Unterwassermetalle (Propeller, Saildrive) korrodieren trotzdem | Min. Galvanischer Isolator, besser Trenntrafo |
| Alle Verbraucher auf einen FI | Einer löst aus → alles dunkel | Mindestens 2 FI-Kreise (Pflicht/Komfort getrennt) |
| DC-Kabel zum Inverter zu dünn dimensionieren | Spannungsabfall → Inverter schaltet bei Last ab | Berechnungstabelle verwenden, im Zweifel eine Größe dicker |
| Inverter/Charger-Einstellungen auf Werkseinstellung lassen | Ladeprofil passt nicht zur Batterie, PowerAssist nicht aktiviert | Konfiguration an Bordinstallation anpassen |
| Landstromkabel auf der Trommel lassen | Überhitzung → Isolationsschmelze → Brand | IMMER vollständig abrollen |

### 10.8 Empfohlene Werkzeuge und Messgeräte

| Werkzeug | Einsatz | Preisklasse | Empfehlung |
|----------|---------|-------------|------------|
| Multimeter (CAT III 600V) | Spannung, Strom, Durchgang | €30–€150 | Fluke 101/113, UNI-T UT61E |
| Zangenamperemeter (AC) | Stromkreis-Messung ohne Trennung | €40–€120 | Fluke 323, UNI-T UT210E |
| Isolationsmessgerät (Megger) | Kabelisolation prüfen (500V DC) | €150–€500 | Megger MIT230, Fluke 1503 |
| Polaritätsprüfer | Landstrom-Steckdose prüfen | €10–€30 | Brennenstuhl PM 231E |
| Leitungsprüfer | Kabel durchmessen, Fehler lokalisieren | €20–€60 | Diverse |
| Crimpzange (hydraulisch) | DC-Kabelschuhe 10–95mm² | €50–€200 | Knipex 97 52 35 |
| Drehmomentschlüssel (klein) | Schraubklemmen, DC-Verbindungen | €40–€100 | Wera Click-Torque |
| Thermometer (IR) | Verbindungstemperatur berührungslos | €20–€80 | Testo 805 |

---

## ANHANG A–H — Fallstudien

### ANHANG A — Fallstudie: Erstinstallation Inverter/Charger auf 11m Segelyacht

**Boot:** Bavaria 36, Baujahr 2018, 12V-System, 2× 110Ah AGM
**Ausgangslage:** Kein Inverter, nur Landstrom-Ladegerät (Mastervolt EasyCharge 10A). Eigner plant Langfahrt Mittelmeer.
**Anforderung:** 230V für Kaffeemaschine (1.000W), Mikrowelle (800W), Laptop, gelegentlich Winkelschleifer (800W).

**Analyse:**
- Gleichzeitige Last: Kaffeemaschine + Laptop = 1.080W → 1.200W Inverter ausreichend
- Höchster Anlaufstrom: Winkelschleifer 800W × 6 = 4.800W Surge
- 12V-System: 1.200W / 12V = 100A DC → grenzwertig, aber machbar
- Batteriebank 220Ah AGM → nutzbar 110Ah → bei 1.000W Last ca. 1,2 Stunden

**Lösung:**
- Victron MultiPlus 12/1600/70 (1.300W Dauer, 3.000W Surge, 70A Charger)
- DC-Kabel: 50mm², 1,5m (Inverter direkt neben Batterie unter Niedergang)
- Sicherung: 150A MEGA-Fuse am Batteriepol
- AC-Absicherung: FI Typ A 30mA + LS B16A
- Galvanischer Isolator: Sterling ProGI-32
- Gesamtkosten: €2.100 (Gerät €1.100, Kabel/Zubehör €400, Installation €600)

**Ergebnis nach 6 Monaten:**
- Kaffeemaschine funktioniert einwandfrei
- Mikrowelle funktioniert, aber nicht gleichzeitig mit Kaffeemaschine (Überlast)
- PowerAssist funktioniert hervorragend bei schwachem Landstrom (4A in griechischen Marinas)
- Leerlaufverbrauch 12W → Eco-Modus aktiviert → 3W
- Batteriebank als Engpass identifiziert → Upgrade auf 200Ah LiFePO4 geplant

### ANHANG B — Fallstudie: Trenntrafo-Nachrüstung auf 14m Motoryacht

**Boot:** Jeanneau Merry Fisher 1095, Baujahr 2020, 12V-System
**Problem:** Massiver Zinkanoden-Verbrauch im Heimathafen (Mittelmeer, Kroatien). Neue Anoden nach 3 Monaten aufgelöst. Nachbarboot mit Aluminium-Saildrive ebenfalls betroffen.
**Diagnose:** Leckstrommessung am Landstromkabel: 85mA AC (FI-Schwelle 30mA wurde vermutlich durch allmähliche Steigerung nie erreicht — schleichendes Problem). Mehrere Boote am selben Steg-Verteiler mit defekten Isolationen.

**Lösung:**
- Mastervolt IVET 3,5 kVA Ringkern-Trenntrafo
- Montage auf Schwingungsdämpfern im Maschinenraum
- Sekundär-Erdung: Sternpunkt → Bonding-System → Kiel
- Neuer FI Typ A 30mA hinter dem Trenntrafo (Sekundärseite)
- Gesamtkosten: €2.800 (Trafo €1.200, Installation €1.200, Zubehör €400)

**Ergebnis:**
- Leckstrom auf Rumpf: 0 mA (vollständige Isolation)
- Zinkanoden-Verbrauch: normalisiert (Wechsel alle 12 Monate)
- Trenntrafo-Brummen: initial vorhanden, durch DC-Blocker (€180) behoben
- ROI: Einsparung an Anoden + vermiedene Korrosionsschäden → amortisiert in ca. 2 Jahren

### ANHANG C — Fallstudie: Victron Quattro-System auf 18m Segelyacht

**Boot:** Oyster 56, Baujahr 2016, 24V-System, 800Ah LiFePO4
**Anforderung:** Vollautonomes Energiesystem für Langfahrt. Generator (Fischer Panda 8kW) + Landstrom + Solar + Inverter.

**System:**
- Victron Quattro-II 24/5000/120 (AC1: Landstrom 32A, AC2: Generator)
- 2× Victron SmartSolar MPPT 150/85 (1.600Wp Solar)
- Victron Cerbo GX + GX Touch 70 (Monitoring)
- Victron SmartShunt 500A (Batteriemonitor)
- 800Ah LiFePO4 mit Victron VE.Bus BMS V2
- Mastervolt IVET 7,0 kVA Trenntrafo am Landstromeingang

**Betriebsszenarien:**
- Hafen: Landstrom über Trenntrafo → Quattro lädt Batterien → Pass-Through für Verbraucher
- Anker (Tag): Solar (800–1.200W) → Batterien → Quattro Inverter (Kühlschrank, Laptop, Wassermacher)
- Anker (Abend): Solar sinkt → Inverter aus Batterie → Klimaanlage, Kochen
- Anker (Kochen/Waschen): Generator startet automatisch bei SOC <40% → Quattro lädt + versorgt Verbraucher → Generator stoppt bei SOC >80%
- Fahrt: Alternator 120A + Solar → Batterien voll → Inverter aus Batterie → Generator nie nötig

**Gesamtkosten Energiesystem:** €28.000 (inkl. Batterien, Solar, Quattro, Generator-Integration, Trenntrafo, Installation)

**Ergebnis nach 18 Monaten Langfahrt (Atlantik, Karibik):**
- Generatorlaufzeit reduziert von geschätzt 6h/Tag auf 0,8h/Tag
- Dieselersparnis: ca. 4L/Tag × 365 = 1.460L/Jahr × €1,50 = €2.190/Jahr
- System zuverlässig, kein Ausfall
- VRM-Fernüberwachung: Eigner kann System weltweit via Internet kontrollieren

### ANHANG D — Fallstudie: Electric Shock Drowning — Beinahe-Unfall

**Ort:** Marina in Südfrankreich, Sommer 2024
**Vorfall:** Zwei Schwimmer (Kinder, 10 und 12 Jahre) berichten über "Kribbeln" und "schwere Beine" beim Schwimmen zwischen den Stegen. Ein Kind konnte kurzzeitig nicht schwimmen, wurde von einem Erwachsenen gerettet.

**Untersuchung:**
- Leckstrommessung im Wasser: bis zu 45mA AC zwischen verschiedenen Booten
- Quelle: Motoryacht (15m) mit defektem Warmwasserboiler — Heizspirale durchgebrannt → Phase auf Gehäuse → über Wasserleitungen zum Rumpf → ins Wasser
- Boot hatte keinen FI-Schutz (Baujahr 1998, nie nachgerüstet)
- Boot hatte keinen Trenntrafo und keinen Galvanischen Isolator
- Marina-Erdung war vorhanden, aber Fehlerstrom unter der 300mA-Vorsicherung der Marina

**Maßnahmen:**
- Sofortige Abschaltung des betroffenen Bootes
- FI 30mA nachgerüstet auf allen AC-Kreisen
- Trenntrafo installiert
- Defekter Boiler ersetzt
- Marina hat ELCI (30mA) auf allen Steg-Verteilern nachgerüstet
- Badeverbotsschild an allen Stegen aufgestellt

**Lehren für AYDI:**
- KRITISCHER Befund: Boot ohne FI-Schutz am Landstrom
- KRITISCHER Befund: Boot ohne galvanische Isolation bei dauerhaftem Landstromanschluss
- Automatische Warnung bei fehlendem FI im Compliance-Modul

### ANHANG E — Fallstudie: PowerAssist in europäischen Marinas

**Boot:** Hallberg-Rassy 40, 24V-System, Victron MultiPlus 24/3000/70
**Problem:** In südeuropäischen Marinas oft nur 6A oder 10A Landstrom verfügbar. Bei 6A × 230V = 1.380W reicht der Strom nicht für Ladegerät (1.680W bei 70A/24V) + Warmwasserboiler (1.500W) gleichzeitig.

**Lösung: PowerAssist konfiguriert:**
- Landstrom-Eingangslimit auf 6A gesetzt (über VictronConnect)
- MultiPlus begrenzt Ladestrom automatisch
- Bei Einschalten des Boilers: MultiPlus ergänzt aus Batterie → Steg-Sicherung bleibt intakt

**Ergebnis:**
- Keine ausgelösten Steg-Sicherungen mehr (zuvor 2–3× pro Woche)
- Batterien werden bei geringer Last vollständig geladen
- Bei hoher Last: Ladestrom reduziert, aber nie Überlast am Steg
- Einstellung per App in 30 Sekunden änderbar (Hafen wechselt → neues Limit)

### ANHANG F — Fallstudie: Galvanische Korrosion durch fehlerhafte Nachbar-Installation

**Boot:** Hanse 458, GFK, Bronze-Borddurchlässe, Faltpropeller (Bronze)
**Problem:** Nach 4 Monaten im Heimathafen: Saildrive-Anode vollständig aufgelöst, Propeller zeigt Pitting, ein Bronze-Borddurchlass zeigt Entzinkung (rosa Verfärbung).
**Zeitraum:** Korrosion setzte ein, nachdem neues Boot auf Nachbar-Liegeplatz kam.

**Diagnose:**
- Eigenes Boot: Galvanischer Isolator vorhanden, korrekt funktionierend
- Nachbarboot: Aluminium-Rumpf, kein Trenntrafo, kein Galvanischer Isolator
- Leckstrommessung am Nachbarboot: 120mA AC auf PE-Leiter → fließt über Wasser
- Galvanisches Potential: Aluminium-Rumpf (Nachbar) = -0,75V, Bronze-Propeller (eigenes Boot) = +0,30V → Differenz 1,05V → unter der 1,2V-Schwelle des Galvanischen Isolators, ABER AC-Leckstrom nicht blockiert!

**Lösung:**
- Nachbarboot: Trenntrafo installiert, defekte Isolation repariert → kein Leckstrom mehr
- Eigenes Boot: Upgrade von Galvanischem Isolator auf Trenntrafo (langfristige Lösung)
- Schadensbehebung: neue Anoden (€200), Propeller poliert (€150), Borddurchlass beobachtet

**Lehre:** Ein Galvanischer Isolator schützt nur vor DC-Strömen. AC-Leckströme (von eigenen oder fremden Booten) werden nicht blockiert. Trenntrafo bietet umfassendsten Schutz.

### ANHANG G — Fallstudie: Lithium-Upgrade mit bestehendem Inverter

**Boot:** Beneteau Oceanis 46.1, 12V-System, vorhandener Victron MultiPlus 12/3000/120
**Vorhaben:** Upgrade von 3× 110Ah AGM auf 2× 200Ah LiFePO4

**Herausforderungen:**
- MultiPlus-Ladespannung muss angepasst werden (AGM: 14,4V → LiFePO4: 14,2V, Float: 13,5V)
- BMS-Integration erforderlich (BMS muss Ladung/Entladung stoppen können)
- Zellbalancing bei LiFePO4: darf nicht über Ladespannung forciert werden

**Lösung:**
- Victron VE.Bus BMS V2 installiert → kommuniziert direkt mit MultiPlus über VE.Bus
- Ladeeinstellungen über VEConfigure angepasst: Absorption 14,2V, Float 13,5V, Low-Voltage-Disconnect 11,0V
- Temperatursensor an Batterie montiert → Temperaturkompensation deaktiviert (bei LiFePO4 nicht nötig)
- Cerbo GX nachgerüstet für System-Monitoring

**Ergebnis:**
- Nutzbare Kapazität: von 165Ah (50% DOD AGM) auf 360Ah (90% DOD LFP) → mehr als verdoppelt
- Gewichtsersparnis: 95 kg (AGM) → 52 kg (LFP) = -43 kg
- Inverter-Betriebsdauer bei 1.000W: von 1,8h auf 3,9h
- Integration problemlos dank VE.Bus-Kommunikation

### ANHANG H — Fallstudie: 3-Phasen-Landstrom auf 22m Motoryacht

**Boot:** Azimut 68, 2019, 3× 400V Drehstromanschluss, 48V Bordnetz
**Systemkonfiguration:**
- 3× Victron Quattro-II 48/10000/140 (je einer pro Phase, L1/L2/L3)
- Victron Cerbo GX + Ekrano GX (15" Touchscreen)
- 48V 1.000Ah LiFePO4 (BYD Battery-Box Premium)
- Mastervolt IVET 16 kVA Trenntrafo (3-phasig)
- Fischer Panda iGen 10000 Generator

**Betriebsstrategie:**
- Hafen: 3× 400V Landstrom über Trenntrafo → Quattros laden Batterien → Pass-Through für alle Verbraucher inkl. Klimaanlage (3× je 3.500W pro Phase)
- Anker: Quattros im Inverter-Modus → 24kW Gesamtleistung → alle Verbraucher laufen → Generator startet bei SOC <35%
- Fahrt: Generator versorgt über AC2-Eingänge → Batterien werden geladen

**Herausforderung 3-Phasen-Konfiguration:**
- Alle drei Quattros müssen identisch konfiguriert sein
- Phasenzuordnung korrekt (L1=Master, L2=Slave1, L3=Slave2)
- Bei Landstrom-Ausfall einer Phase: betroffener Quattro schaltet auf Inverter, andere bleiben auf Landstrom
- Generator liefert nur einphasig → wird auf AC2 des L1-Quattros angeschlossen → L2 und L3 laufen aus Batterie

**Gesamtkosten Energiesystem:** €85.000 (inkl. 3× Quattro, Batterien, Generator-Integration, Trenntrafo, Verkabelung, Installation, Inbetriebnahme)

### ANHANG H.0 — Fallstudie: Kompletter Systemausfall durch Korrosion an DC-Verbindungen

**Boot:** Dufour 430, Baujahr 2021, 12V-System, Victron MultiPlus 12/3000/120
**Situation:** Boot lag 8 Monate am Landstrom im Heimathafen (Adria). Eigner nutzte das Boot nur am Wochenende. System lief durchgehend im Charger/Pass-Through-Modus.

**Symptome bei Ankunft:**
- Inverter zeigt "Low Battery" obwohl am Landstrom
- Ladestrom laut Display: 0A (sollte 120A bei leerer Batterie sein)
- Batteriespannung am Inverter: 11,2V (deutlich zu niedrig)
- Batteriespannung direkt an der Batterie: 12,8V (normal!)

**Diagnose:**
- Spannungsdifferenz von 1,6V zwischen Batterie und Inverter → massiver Spannungsabfall
- Ursache: DC-Kabelverbindung am Batteriepol — Ringkabelschuh hatte grüne Korrosion
- Übergangswiderstand an der Verbindung: 12 mΩ (statt <0,1 mΩ)
- Bei 120A Ladestrom: 120A × 0,012Ω = 1,44V Spannungsabfall → nur an EINER Verbindung!
- Charger hatte wegen der niedrigen Spannung am Eingang auf "Fehlzustand" geschaltet

**Ursache der Korrosion:**
- Kabelschuh war nicht verzinnt
- Kabelschuh war nur gecrimpt, nicht verlötet
- Keine Korrosionsschutzmasse (Vaseline, Kontaktfett) aufgetragen
- Feuchtigkeit im Batterieraum (kein Lüfter, kein Heizer)
- 8 Monate durchgehende Feuchtigkeit in der Adria

**Reparatur:**
1. Beide DC-Kabelschuhe abgeschnitten
2. Kabel frisch abisoliert (30mm)
3. Neue verzinnte Kupfer-Ringkabelschuhe aufgecrimpt (hydraulische Crimpzange)
4. Zusätzlich verlötet (Propanbrenner, bleifrei)
5. Schrumpfschlauch mit Kleber über Crimpstelle
6. Batteriepol gereinigt (Drahtbürste, Kontaktspray)
7. Kabelschuh montiert mit Edelstahl-Schraube + Federring + Nordlock-Sicherung
8. Dünn Vaseline über die gesamte Verbindung
9. Drehmoment: 8 Nm (lt. Batterie-Hersteller)

**Kosten:** €25 Material, 2 Stunden Arbeit
**Vermiedener Schaden:** Ohne Reparatur wäre die Batterie durch Tiefentladung zerstört worden (€300–€1.500 je nach Typ)

**Lehre für AYDI:**
- DC-Verbindungen am Inverter sind ein kritischer visueller und struktureller Prüfpunkt
- Visuell: Grünspan an Kabelschuhen → visual_high Score Abzug
- Strukturiert: Spannungsabfall DC-Leitung >0,5V unter Last → WARNUNG

### ANHANG H.1 — Inspektions-Checkliste: AC-Installation Komplett

```
AC-INSTALLATION — JÄHRLICHE INSPEKTION
═══════════════════════════════════════
Boot: _________________ Datum: _________
Inspektor: _____________ Zertifikat: ______

LANDSTROM-EINSPEISUNG
□ CEE-Einbaustecker: Zustand, Korrosion, Dichtung
□ Deckel/Schraubkappe: vorhanden, dicht, Feder intakt
□ Landstromkabel: Zustand Isolation, Stecker, Kontakte
□ Kabel-Durchführung ins Schiffsinnere: dicht, Zugentlastung
□ Polaritätsprüfer: funktioniert (alle 3 LEDs bei korrektem Anschluss)
  Befund: ________________________________________________

GALVANISCHE ISOLATION
□ Galvanischer Isolator vorhanden? □ Ja □ Nein
  Wenn ja: Diodentest (Multimeter): □ OK  □ Defekt
  Status-LED: □ OK  □ Aus  □ Blinkt (Alarm)
□ Trenntrafo vorhanden? □ Ja □ Nein
  Wenn ja: Sichtprüfung (Korrosion, Feuchtigkeit): □ OK  □ Mängel
  Brummgeräusch bei Last: □ Normal  □ Auffällig
  Montage/Schwingungsdämpfer: □ OK  □ Lose
  Befund: ________________________________________________

FI-SCHUTZSCHALTER
□ FI vorhanden? □ Ja □ Nein (→ KRITISCH wenn Nein!)
□ FI-Typ: □ AC  □ A  □ F  □ B  (Typ AC → Empfehlung: Upgrade auf Typ A)
□ FI-Auslösestrom: ___mA (Soll: 30mA)
□ FI-Testtaste gedrückt → löst aus? □ Ja  □ Nein (→ KRITISCH!)
□ FI zurückgesetzt → hält? □ Ja  □ Nein
□ Anzahl FI-Kreise: ___ (Empfehlung: mind. 2 separate)
  Befund: ________________________________________________

AC-VERTEILERTAFEL
□ Beschriftung aller Stromkreise: □ Lesbar  □ Teilweise  □ Fehlend
□ Alle Leitungsschutzschalter funktionsfähig (ein/aus schalten)
□ Kabelanschlüsse: fester Sitz geprüft (Schraubklemmen nachziehen)
□ Korrosion an Klemmen/Schienen: □ Keine  □ Leicht  □ Signifikant
□ Isolierstoffteile: □ Intakt  □ Verfärbung  □ Beschädigung
□ Feuchtigkeitsspuren im Verteilerkasten: □ Keine  □ Vorhanden
  Befund: ________________________________________________

INVERTER/CHARGER
□ Modell: _________________ Firmware: _________
□ Sichtprüfung: Gehäuse, Korrosion, Verfärbung (Hitze?)
□ Lüfter: dreht frei, kein Rasseln, nicht blockiert
□ Luftfilter (wenn vorhanden): gereinigt
□ DC-Kabelanschlüsse: fester Sitz, kein Grünspan, kein Erwärmen
□ DC-Sicherung: visuell intakt, korrekter Wert ___A
□ AC-Kabelanschlüsse: fester Sitz
□ Status-LEDs bei Landstrom: □ Normal  □ Warnung  □ Fehler
□ Status-LEDs bei Inverterbetrieb: □ Normal  □ Warnung  □ Fehler
□ Eco-Modus funktioniert (Last anschließen → Inverter startet)
□ Batteriespannung am Inverter-Eingang (unter Last): ___V
□ Batteriespannung an Batterie-Klemme (unter Last): ___V
□ Differenz (Spannungsabfall DC-Kabel): ___V (max. 0,5V)
  Befund: ________________________________________________

STECKDOSEN UND VERBRAUCHER
□ Alle Steckdosen: visuell geprüft, kein Schmelzen/Verfärbung
□ Nassraum-Steckdosen: IP44-Klappdeckel funktioniert
□ Deck-Steckdosen: IP56-Deckel schließt und dichtet
□ Steckdosen in Pantry: Abstand zu Wasserquellen >600mm
□ Kabel sichtbar: keine Scheuerung, kein Knick, keine UV-Schäden
  Befund: ________________________________________________

ISOLATIONSMESSUNG (alle 3–5 Jahre oder bei Verdacht)
□ Inverter/Charger abgeklemmt? □ Ja (Pflicht vor Messung!)
□ Alle Verbraucher abgeschaltet/abgezogen? □ Ja
□ Messgerät: Megger, 500V DC
□ L gegen PE: ___ MΩ (Soll: >1 MΩ, Ziel: >10 MΩ)
□ N gegen PE: ___ MΩ (Soll: >1 MΩ, Ziel: >10 MΩ)
□ L gegen N: ___ MΩ (Soll: >1 MΩ)
  Befund: ________________________________________________

GESAMTBEWERTUNG
□ Alles in Ordnung — nächste Inspektion in 12 Monaten
□ Kleinere Mängel — Maßnahmen:
  _______________________________________________________
□ Größere Mängel — Reparatur erforderlich:
  _______________________________________________________
□ KRITISCH — Sofortige Abschaltung/Reparatur:
  _______________________________________________________

Inspektion durchgeführt von: ________________
Unterschrift: ________________
```

### ANHANG H.2 — Landstrom-Anschluss Quick Reference Card (Aushang)

```
LANDSTROM — ANSCHLUSS-CHECKLISTE
═════════════════════════════════
An alle Crew: Aushängen am Niedergang!

VOR DEM ANSCHLIESSEN:
━━━━━━━━━━━━━━━━━━━━
1. □ Hauptschalter AC an Bord: AUS
2. □ Inverter/Charger: AUS (oder auf "Charger Only")
3. □ Landstromkabel prüfen: Isolation OK? Stecker trocken?
4. □ Kabel an Bord anschließen (CEE-Einbaustecker, drehen bis Klick)
5. □ Kabel am Steg anschließen (CEE-Steckdose)
6. □ Am Steg einschalten (wenn Steg-Schalter vorhanden)

ANSCHLUSS PRÜFEN:
━━━━━━━━━━━━━━━━
7. □ Polaritätsanzeige prüfen: Alle LEDs grün? → OK
   ⚠️ LED rot oder fehlend? → NICHT einschalten! Hafenmeister rufen!
8. □ FI-Schutzschalter einschalten
   ⚠️ FI löst sofort aus? → Problem! Alle LS aus, einzeln einschalten
9. □ Leitungsschutzschalter einschalten
10. □ Inverter/Charger einschalten → Ladung startet?
11. □ Spannung am Verteiler ablesen: ___V (Soll: 220–240V)

BEI PROBLEMEN:
━━━━━━━━━━━━━
- FI löst aus → Alle Geräte abziehen, einzeln einstecken
- Keine Spannung → Steg-Sicherung prüfen, Hafenmeister fragen
- Kabel warm → SOFORT abstecken! Kabel/Stecker defekt!
- Brummen vom Trenntrafo → Normal bei leichtem Brummen, bei lautem
  Brummen Marina wechseln oder DC-Blocker verwenden

VOR DEM ABSTECKEN:
━━━━━━━━━━━━━━━━━
1. □ Alle Hochlast-Verbraucher ausschalten
2. □ Hauptschalter AC an Bord: AUS
3. □ Am Steg ausschalten
4. □ Kabel am Steg abziehen
5. □ Kabel an Bord abziehen
6. □ CEE-Einbaustecker: Schraubkappe schließen!
7. □ Kabel trocknen lassen, sauber verstauen

Landstromkabel-Lagerort: _______________
Adapter-Set Lagerort: _______________
```

### ANHANG H.3 — Adapter-Übersicht für internationale Marinas

| Von → Nach | Adapter-Typ | Vorkommen | Preis (ca.) | Sicherheitshinweis |
|------------|-------------|-----------|-------------|--------------------|
| CEE 16A → Schuko | Standardadapter | Notfall an Land | €15 | Erdung prüfen! |
| CEE 32A → CEE 16A | Reduzierstecker | Häufig | €30 | Absicherung auf 16A anpassen |
| UK BS 1363 → CEE 16A | UK-Adapter | UK, Gibraltar, Malta | €40 | Polarität prüfen |
| US NEMA 5-15 → CEE 16A | US-Adapter (120V!) | USA, Karibik | €50 | Nur 120V! Charger muss 120V können |
| US NEMA TT-30 → CEE 16A | US-30A-Adapter | USA, Kanada | €60 | 120V/30A, Charger anpassen |
| Australia AS 3112 → CEE 16A | AUS-Adapter | Australien, NZ | €40 | 230V, Polarität prüfen |
| Schuko → CEE 16A | Rückadapter | Notfall in Marina ohne CEE | €20 | Keine Verriegelung! |
| CEE 63A 3~ → CEE 32A 1~ | Phasenabgriff | Große Marinas | €80 | Nur EINE Phase nutzen |

**Universaladapter-Set für Blauwasser:**
Ein gutes Adapterset umfasst: UK, US (NEMA 5-15), US (NEMA TT-30), AU/NZ, CEE 32→16, sowie ein Multimeter und einen Leitungsprüfer. Kosten: €200–€350 als Set.

---

## ANHANG I–R — AYDI-Integration (Pydantic v2 Modelle)

> **Hinweis:** Alle Modelle verwenden Pydantic v2 mit `model_config = {"from_attributes": True}`.
> NIEMALS `class Config` verwenden.

### ANHANG I — Grundlegende Datenmodelle

```python
"""
AYDI Knowledge Models — 22.07 Wechselrichter und Landstrom
All models use Pydantic v2 with model_config = {"from_attributes": True}
NEVER use class Config — always use model_config dict.
"""

from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


# --- Enumerations ---

class SystemVoltage(str, Enum):
    """DC system voltage of the vessel."""
    V12 = "12V"
    V24 = "24V"
    V48 = "48V"


class InverterType(str, Enum):
    """Type of inverter installation."""
    STANDALONE = "standalone"
    INVERTER_CHARGER = "inverter_charger"
    QUATTRO = "quattro"  # dual AC input
    HYBRID_GENERATOR = "hybrid_generator"


class WaveformType(str, Enum):
    """Output waveform quality."""
    PURE_SINE = "pure_sine"
    MODIFIED_SINE = "modified_sine"


class GalvanicProtectionType(str, Enum):
    """Type of galvanic protection installed."""
    NONE = "none"
    GALVANIC_ISOLATOR = "galvanic_isolator"
    ISOLATION_TRANSFORMER = "isolation_transformer"
    BOTH = "both"


class RCDType(str, Enum):
    """Type of residual current device (FI-Schutzschalter)."""
    TYPE_AC = "type_ac"
    TYPE_A = "type_a"
    TYPE_F = "type_f"
    TYPE_B = "type_b"
    TYPE_B_PLUS = "type_b_plus"
    NONE = "none"


class GroundingScheme(str, Enum):
    """Onboard AC grounding scheme."""
    TT = "tt"
    TN_S = "tn_s"
    IT = "it"
    UNKNOWN = "unknown"


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


class SeverityLevel(str, Enum):
    """Severity of identified issues."""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"
```

### ANHANG J — Inverter-Spezifikationsmodelle

```python
class InverterSpec(BaseModel):
    """Specification of a marine inverter or inverter/charger unit."""

    model_config = {"from_attributes": True}

    manufacturer: str = Field(..., description="Manufacturer name (e.g., 'Victron Energy')")
    model: str = Field(..., description="Model designation (e.g., 'MultiPlus-II 24/3000/70')")
    inverter_type: InverterType = Field(..., description="Type of inverter")
    system_voltage: SystemVoltage = Field(..., description="DC input voltage")
    continuous_power_w: int = Field(..., ge=0, description="Continuous output power in watts")
    peak_power_w: int = Field(..., ge=0, description="Peak/surge power (5 seconds) in watts")
    charger_current_a: Optional[int] = Field(None, ge=0, description="Charger current in amps (None for standalone inverters)")
    no_load_consumption_w: float = Field(..., ge=0, description="No-load power consumption in watts")
    eco_mode_consumption_w: Optional[float] = Field(None, ge=0, description="Eco mode consumption in watts")
    waveform: WaveformType = Field(WaveformType.PURE_SINE, description="Output waveform type")
    thd_percent: float = Field(..., ge=0, le=100, description="Total Harmonic Distortion percentage")
    efficiency_peak_percent: float = Field(..., ge=0, le=100, description="Peak efficiency percentage")
    transfer_time_ms: Optional[float] = Field(None, ge=0, description="AC transfer relay switching time in ms (None for standalone)")
    ac_inputs: int = Field(1, ge=0, le=2, description="Number of AC inputs (0 for standalone, 1 or 2)")
    ac_input_max_a: Optional[float] = Field(None, ge=0, description="Maximum AC input current in amps")
    power_assist: bool = Field(False, description="PowerAssist/PowerBoost capability")
    parallel_capable: bool = Field(False, description="Can be paralleled with identical units")
    three_phase_capable: bool = Field(False, description="Can be configured in 3-phase setup")
    weight_kg: float = Field(..., ge=0, description="Weight in kilograms")
    dimensions_mm: Optional[str] = Field(None, description="Dimensions WxHxD in mm (e.g., '258x520x218')")
    protection_rating: str = Field("IP21", description="IP protection rating")
    price_eur: Optional[float] = Field(None, ge=0, description="Approximate price in EUR")
    communication: list[str] = Field(default_factory=list, description="Communication interfaces (e.g., ['VE.Bus', 'Bluetooth'])")
    certifications: list[str] = Field(default_factory=list, description="Certifications (e.g., ['CE', 'RCM', 'UL'])")


class InverterOperatingMode(str, Enum):
    """Current operating mode of the inverter/charger."""
    INVERTING = "inverting"
    CHARGING = "charging"
    PASS_THROUGH = "pass_through"
    POWER_ASSIST = "power_assist"
    UPS = "ups"
    STANDBY = "standby"
    ECO_SEARCH = "eco_search"
    FAULT = "fault"
    OFF = "off"


class InverterStatus(BaseModel):
    """Real-time status of an inverter/charger unit."""

    model_config = {"from_attributes": True}

    operating_mode: InverterOperatingMode = Field(..., description="Current operating mode")
    ac_output_voltage_v: Optional[float] = Field(None, description="AC output voltage in volts")
    ac_output_frequency_hz: Optional[float] = Field(None, description="AC output frequency in Hz")
    ac_output_power_w: Optional[float] = Field(None, description="Current AC output power in watts")
    ac_input_voltage_v: Optional[float] = Field(None, description="AC input voltage in volts (None if no shore power)")
    ac_input_current_a: Optional[float] = Field(None, description="AC input current in amps")
    dc_voltage_v: Optional[float] = Field(None, description="DC input voltage from batteries")
    dc_current_a: Optional[float] = Field(None, description="DC current draw (positive=discharge, negative=charge)")
    charge_current_a: Optional[float] = Field(None, description="Battery charge current in amps")
    temperature_c: Optional[float] = Field(None, description="Internal temperature in Celsius")
    load_percent: Optional[float] = Field(None, ge=0, le=100, description="Current load as percentage of rated power")
    warnings: list[str] = Field(default_factory=list, description="Active warning messages")
    alarms: list[str] = Field(default_factory=list, description="Active alarm messages")
```

### ANHANG K — Trenntrafo- und Galvanischer-Isolator-Modelle

```python
class IsolationTransformerSpec(BaseModel):
    """Specification of a marine isolation transformer."""

    model_config = {"from_attributes": True}

    manufacturer: str = Field(..., description="Manufacturer name")
    model: str = Field(..., description="Model designation")
    rated_power_va: int = Field(..., ge=0, description="Rated power in VA")
    core_type: str = Field(..., description="Core type: 'toroidal', 'ei_core', 'c_core'")
    primary_voltage_v: int = Field(230, description="Primary voltage in volts")
    secondary_voltage_v: int = Field(230, description="Secondary voltage in volts")
    isolation_voltage_v: int = Field(3750, description="Isolation test voltage in volts AC")
    no_load_loss_w: float = Field(..., ge=0, description="No-load losses in watts")
    short_circuit_impedance_percent: float = Field(..., ge=0, le=100, description="Short circuit impedance percentage")
    temperature_class: str = Field("F", description="Temperature class (B=130, F=155, H=180 degrees C)")
    weight_kg: float = Field(..., ge=0, description="Weight in kilograms")
    ip_rating: str = Field("IP23", description="IP protection rating")
    electrostatic_shield: bool = Field(False, description="Has electrostatic shield between windings")
    price_eur: Optional[float] = Field(None, ge=0, description="Approximate price in EUR")


class GalvanicIsolatorSpec(BaseModel):
    """Specification of a galvanic isolator (zinc saver)."""

    model_config = {"from_attributes": True}

    manufacturer: str = Field(..., description="Manufacturer name")
    model: str = Field(..., description="Model designation")
    rated_current_a: int = Field(..., ge=0, description="Rated current in amps")
    dc_blocking_voltage_v: float = Field(1.4, description="DC blocking voltage threshold in volts")
    fail_safe: bool = Field(True, description="Fails to short circuit (PE connected) on diode failure")
    monitoring: bool = Field(False, description="Has status LED or alarm output")
    surge_protection: bool = Field(False, description="Includes varistor/TVS surge protection")
    generation: int = Field(2, ge=1, le=3, description="Generation (1=passive, 2=active, 3=monitored)")
    weight_kg: float = Field(..., ge=0, description="Weight in kilograms")
    price_eur: Optional[float] = Field(None, ge=0, description="Approximate price in EUR")
```

### ANHANG L — AC-Installationsbewertung

```python
class ACCircuit(BaseModel):
    """Single AC circuit in the distribution panel."""

    model_config = {"from_attributes": True}

    circuit_name: str = Field(..., description="Name/label of the circuit (e.g., 'Steckdosen Salon')")
    circuit_number: int = Field(..., ge=1, description="Circuit number in panel")
    breaker_rating_a: int = Field(..., ge=0, description="Circuit breaker rating in amps")
    cable_cross_section_mm2: float = Field(..., ge=0, description="Cable cross-section in mm²")
    cable_type: str = Field(..., description="Cable type (e.g., 'H07RN-F 3G2.5')")
    cable_length_m: Optional[float] = Field(None, ge=0, description="Cable length in meters")
    rcd_protected: bool = Field(True, description="Circuit is protected by RCD/FI")
    rcd_type: Optional[RCDType] = Field(None, description="Type of RCD if protected")
    rcd_rating_ma: Optional[int] = Field(None, description="RCD trip current in mA")
    marine_cable: Optional[bool] = Field(None, description="Uses marine-grade cable (tinned copper)")
    voltage_drop_percent: Optional[float] = Field(None, ge=0, description="Calculated voltage drop percentage")


class ShorePowerConnection(BaseModel):
    """Shore power connection configuration."""

    model_config = {"from_attributes": True}

    connector_type: str = Field(..., description="Connector type (e.g., 'CEE_16A_blue', 'CEE_32A_blue', 'CEE_63A_red_3phase')")
    rated_current_a: int = Field(..., ge=0, description="Rated current in amps")
    phases: int = Field(1, ge=1, le=3, description="Number of phases (1 or 3)")
    inlet_location: Optional[str] = Field(None, description="Location of deck inlet")
    cable_cross_section_mm2: float = Field(..., ge=0, description="Feed cable cross-section in mm²")
    cable_length_m: Optional[float] = Field(None, ge=0, description="Cable length from inlet to panel in meters")
    polarity_indicator: bool = Field(False, description="Has polarity check indicator")
    auto_polarity_switch: bool = Field(False, description="Has automatic polarity correction relay")


class ACInstallationAssessment(BaseModel):
    """Complete assessment of the vessel's AC installation."""

    model_config = {"from_attributes": True}

    vessel_id: Optional[str] = Field(None, description="AYDI vessel identifier")
    assessment_date: Optional[str] = Field(None, description="Assessment date (ISO 8601)")
    system_voltage_ac: int = Field(230, description="Nominal AC system voltage")
    system_frequency_hz: int = Field(50, description="Nominal AC frequency")
    grounding_scheme: GroundingScheme = Field(..., description="AC grounding scheme")

    # Shore power
    shore_power: Optional[ShorePowerConnection] = Field(None, description="Shore power connection")
    galvanic_protection: GalvanicProtectionType = Field(GalvanicProtectionType.NONE, description="Type of galvanic protection")
    galvanic_isolator: Optional[GalvanicIsolatorSpec] = Field(None, description="Galvanic isolator details")
    isolation_transformer: Optional[IsolationTransformerSpec] = Field(None, description="Isolation transformer details")

    # Inverter
    inverter: Optional[InverterSpec] = Field(None, description="Primary inverter/charger")
    inverter_secondary: Optional[InverterSpec] = Field(None, description="Secondary inverter (if present)")

    # Distribution
    main_rcd_type: Optional[RCDType] = Field(None, description="Main RCD type")
    main_rcd_rating_ma: Optional[int] = Field(None, description="Main RCD rating in mA")
    circuits: list[ACCircuit] = Field(default_factory=list, description="AC circuits in distribution panel")
    total_circuits: int = Field(0, ge=0, description="Total number of AC circuits")

    # Compliance findings
    overall_score: Optional[float] = Field(None, ge=0, le=100, description="Overall AC installation score (0-100)")
    confidence: ConfidenceLevel = Field(ConfidenceLevel.ESTIMATED, description="Confidence level of assessment")
    findings: list["ACFinding"] = Field(default_factory=list, description="List of findings")


class ACFinding(BaseModel):
    """Individual finding from the AC installation assessment."""

    model_config = {"from_attributes": True}

    finding_id: str = Field(..., description="Unique finding identifier")
    category: str = Field(..., description="Finding category (e.g., 'rcd_protection', 'galvanic_isolation', 'cable_quality')")
    severity: SeverityLevel = Field(..., description="Severity level")
    title_de: str = Field(..., description="Finding title in German")
    description_de: str = Field(..., description="Detailed description in German")
    location: Optional[str] = Field(None, description="Location on vessel")
    norm_reference: Optional[str] = Field(None, description="Relevant norm/standard reference")
    recommendation_de: Optional[str] = Field(None, description="Recommended action in German")
    confidence: ConfidenceLevel = Field(ConfidenceLevel.ESTIMATED, description="Confidence level")
    photo_refs: list[str] = Field(default_factory=list, description="References to relevant photos")
```

### ANHANG M — Fehlerbild-Modelle

```python
class FaultCategory(str, Enum):
    """Categories of AC/inverter faults."""
    EARTH_FAULT = "earth_fault"
    LEAKAGE_CURRENT = "leakage_current"
    RCD_TRIPPING = "rcd_tripping"
    INVERTER_OVERLOAD = "inverter_overload"
    INVERTER_NO_OUTPUT = "inverter_no_output"
    TRANSFORMER_NOISE = "transformer_noise"
    GALVANIC_CORROSION = "galvanic_corrosion"
    CABLE_OVERHEAT = "cable_overheat"
    EMI_INTERFERENCE = "emi_interference"
    POLARITY_ERROR = "polarity_error"
    CHARGER_FAULT = "charger_fault"
    INVERTER_NOISE = "inverter_noise"


class FaultFinding(BaseModel):
    """Identified fault in the AC/inverter system."""

    model_config = {"from_attributes": True}

    fault_id: str = Field(..., description="Unique fault identifier")
    category: FaultCategory = Field(..., description="Fault category")
    severity: SeverityLevel = Field(..., description="Severity level")
    title_de: str = Field(..., description="Fault title in German")
    description_de: str = Field(..., description="Detailed description in German")
    symptoms_de: list[str] = Field(default_factory=list, description="Observable symptoms in German")
    probable_causes_de: list[str] = Field(default_factory=list, description="Probable causes in German, ordered by likelihood")
    recommended_actions_de: list[str] = Field(default_factory=list, description="Recommended actions in German")
    safety_critical: bool = Field(False, description="True if fault poses immediate safety risk")
    requires_professional: bool = Field(False, description="True if professional repair is recommended")
    estimated_repair_cost_eur: Optional[tuple[float, float]] = Field(None, description="Estimated repair cost range in EUR (min, max)")
    norm_reference: Optional[str] = Field(None, description="Relevant norm violation")
    confidence: ConfidenceLevel = Field(ConfidenceLevel.ESTIMATED, description="Confidence level")


class TroubleshootingStep(BaseModel):
    """Single step in a troubleshooting decision tree."""

    model_config = {"from_attributes": True}

    step_id: str = Field(..., description="Step identifier (e.g., 'step_1', 'step_2a')")
    instruction_de: str = Field(..., description="Instruction for this step in German")
    measurement: Optional[str] = Field(None, description="Measurement to take (if applicable)")
    expected_result: Optional[str] = Field(None, description="Expected result description")
    yes_next: Optional[str] = Field(None, description="Next step ID if condition is met")
    no_next: Optional[str] = Field(None, description="Next step ID if condition is not met")
    conclusion_de: Optional[str] = Field(None, description="Conclusion if this is a terminal step")
    tools_required: list[str] = Field(default_factory=list, description="Tools needed for this step")


class TroubleshootingTree(BaseModel):
    """Complete troubleshooting decision tree for a fault category."""

    model_config = {"from_attributes": True}

    tree_id: str = Field(..., description="Unique tree identifier")
    title_de: str = Field(..., description="Tree title in German")
    description_de: str = Field(..., description="When to use this tree, in German")
    fault_category: FaultCategory = Field(..., description="Associated fault category")
    entry_step: str = Field(..., description="ID of the first step")
    steps: list[TroubleshootingStep] = Field(..., description="All steps in the tree")
    tools_required: list[str] = Field(default_factory=list, description="All tools needed for the complete tree")
    estimated_time_minutes: Optional[int] = Field(None, description="Estimated time to complete troubleshooting")
```

### ANHANG N — Visuelle Analyse-Modelle

```python
class VisualACAssessment(BaseModel):
    """Results of visual (photo-based) assessment of AC installation."""

    model_config = {"from_attributes": True}

    photo_id: str = Field(..., description="Reference to analyzed photo")
    component_type: str = Field(..., description="Type of component visible (e.g., 'inverter', 'distribution_panel', 'shore_inlet')")
    manufacturer_identified: Optional[str] = Field(None, description="Identified manufacturer from photo")
    model_identified: Optional[str] = Field(None, description="Identified model from photo")
    installation_quality_score: Optional[float] = Field(None, ge=0, le=100, description="Visual installation quality score")
    cable_routing_score: Optional[float] = Field(None, ge=0, le=100, description="Cable routing quality score")
    labeling_score: Optional[float] = Field(None, ge=0, le=100, description="Labeling/marking quality score")
    corrosion_detected: bool = Field(False, description="Visible corrosion on components")
    moisture_detected: bool = Field(False, description="Visible moisture or water damage")
    findings: list[str] = Field(default_factory=list, description="Visual findings in German")
    confidence: ConfidenceLevel = Field(ConfidenceLevel.VISUAL_MEDIUM, description="Visual confidence level")


class ACPhotoAnalysis(BaseModel):
    """Photo analysis request/result for AC installation components."""

    model_config = {"from_attributes": True}

    vessel_id: Optional[str] = Field(None, description="AYDI vessel identifier")
    photos: list[VisualACAssessment] = Field(default_factory=list, description="Individual photo assessments")
    overall_visual_score: Optional[float] = Field(None, ge=0, le=100, description="Overall visual assessment score")
    critical_findings: list[str] = Field(default_factory=list, description="Critical findings requiring immediate attention")
    confidence: ConfidenceLevel = Field(ConfidenceLevel.VISUAL_MEDIUM, description="Overall confidence level")
```

### ANHANG O — Energiebedarfs- und Dimensionierungsmodelle

```python
class ACConsumer(BaseModel):
    """Single AC consumer/appliance on the vessel."""

    model_config = {"from_attributes": True}

    name: str = Field(..., description="Appliance name (e.g., 'Mikrowelle')")
    rated_power_w: int = Field(..., ge=0, description="Rated power in watts")
    surge_factor: float = Field(1.0, ge=1.0, le=10.0, description="Surge/inrush factor (1.0 for resistive loads)")
    surge_power_w: Optional[int] = Field(None, ge=0, description="Calculated surge power in watts")
    daily_usage_hours: float = Field(0, ge=0, le=24, description="Average daily usage in hours")
    daily_energy_wh: Optional[float] = Field(None, ge=0, description="Calculated daily energy in Wh")
    runs_on_inverter: bool = Field(True, description="Intended to run on inverter (not just shore power)")
    priority: str = Field("normal", description="Priority: 'critical', 'high', 'normal', 'low'")


class InverterSizingResult(BaseModel):
    """Result of inverter sizing calculation."""

    model_config = {"from_attributes": True}

    total_continuous_load_w: int = Field(..., ge=0, description="Total continuous load in watts")
    max_simultaneous_load_w: int = Field(..., ge=0, description="Maximum simultaneous load in watts")
    max_surge_load_w: int = Field(..., ge=0, description="Maximum surge load in watts")
    recommended_continuous_w: int = Field(..., ge=0, description="Recommended inverter continuous rating in watts")
    recommended_surge_w: int = Field(..., ge=0, description="Recommended inverter surge rating in watts")
    recommended_system_voltage: SystemVoltage = Field(..., description="Recommended DC system voltage")
    recommended_charger_current_a: Optional[int] = Field(None, ge=0, description="Recommended charger current in amps")
    daily_inverter_energy_wh: float = Field(..., ge=0, description="Daily energy from inverter in Wh")
    battery_capacity_ah_required: float = Field(..., ge=0, description="Required battery capacity in Ah at system voltage")
    dc_cable_cross_section_mm2: float = Field(..., ge=0, description="Required DC cable cross-section in mm²")
    dc_fuse_rating_a: int = Field(..., ge=0, description="Required DC fuse rating in amps")
    recommended_models: list[str] = Field(default_factory=list, description="List of recommended inverter models")
    confidence: ConfidenceLevel = Field(ConfidenceLevel.CALCULATED, description="Confidence level")
    notes_de: list[str] = Field(default_factory=list, description="Additional notes in German")


class ShorePowerSizingResult(BaseModel):
    """Result of shore power system sizing."""

    model_config = {"from_attributes": True}

    total_shore_load_w: int = Field(..., ge=0, description="Total shore power load in watts")
    recommended_connection_a: int = Field(..., ge=0, description="Recommended shore power connection in amps (16/32/63)")
    transformer_required: bool = Field(False, description="Isolation transformer recommended/required")
    transformer_rating_va: Optional[int] = Field(None, ge=0, description="Recommended transformer rating in VA")
    galvanic_isolator_required: bool = Field(True, description="Galvanic isolator required (minimum)")
    rcd_type_recommended: RCDType = Field(RCDType.TYPE_A, description="Recommended RCD type")
    number_of_circuits: int = Field(..., ge=1, description="Recommended number of AC circuits")
    cable_cross_section_feed_mm2: float = Field(..., ge=0, description="Feed cable cross-section in mm²")
    confidence: ConfidenceLevel = Field(ConfidenceLevel.CALCULATED, description="Confidence level")
```

### ANHANG P — Korrosionsbewertungsmodelle

```python
class CorrosionRiskLevel(str, Enum):
    """Corrosion risk level from shore power connection."""
    NONE = "none"
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"
    CRITICAL = "critical"


class CorrosionAssessment(BaseModel):
    """Assessment of galvanic corrosion risk from shore power."""

    model_config = {"from_attributes": True}

    vessel_id: Optional[str] = Field(None, description="AYDI vessel identifier")
    hull_material: str = Field(..., description="Hull material: 'grp', 'aluminum', 'steel', 'wood', 'composite'")
    underwater_metals: list[str] = Field(default_factory=list, description="List of underwater metals (e.g., ['bronze_propeller', 'stainless_shaft', 'aluminum_saildrive'])")
    shore_power_connected: bool = Field(False, description="Is shore power typically connected")
    shore_power_hours_per_week: Optional[float] = Field(None, ge=0, description="Hours per week on shore power")
    galvanic_protection: GalvanicProtectionType = Field(GalvanicProtectionType.NONE, description="Galvanic protection type installed")
    anode_type: Optional[str] = Field(None, description="Type of sacrificial anodes: 'zinc', 'aluminum', 'magnesium'")
    anode_condition: Optional[str] = Field(None, description="Anode condition: 'new', 'good', 'fair', 'depleted'")
    anode_replacement_months: Optional[int] = Field(None, description="Months between anode replacements")
    marina_water_type: str = Field("salt", description="Water type: 'salt', 'brackish', 'fresh'")
    neighboring_boats_material: Optional[list[str]] = Field(None, description="Hull materials of neighboring boats")
    leakage_current_measured_ma: Optional[float] = Field(None, ge=0, description="Measured leakage current in mA")

    # Assessment results
    corrosion_risk: CorrosionRiskLevel = Field(CorrosionRiskLevel.MODERATE, description="Assessed corrosion risk level")
    risk_score: Optional[float] = Field(None, ge=0, le=100, description="Corrosion risk score (0=no risk, 100=extreme)")
    findings_de: list[str] = Field(default_factory=list, description="Findings in German")
    recommendations_de: list[str] = Field(default_factory=list, description="Recommendations in German")
    estimated_annual_cost_eur: Optional[float] = Field(None, ge=0, description="Estimated annual cost of corrosion damage in EUR")
    confidence: ConfidenceLevel = Field(ConfidenceLevel.ESTIMATED, description="Confidence level")
```

### ANHANG Q — Compliance-Bewertungsmodelle

```python
class ComplianceCheckResult(str, Enum):
    """Result of individual compliance check."""
    PASS = "pass"
    FAIL = "fail"
    WARNING = "warning"
    NOT_ASSESSED = "not_assessed"
    NOT_APPLICABLE = "not_applicable"


class ACComplianceCheck(BaseModel):
    """Individual AC compliance check result."""

    model_config = {"from_attributes": True}

    check_id: str = Field(..., description="Unique check identifier")
    norm_reference: str = Field(..., description="Norm/standard reference (e.g., 'ISO 13297 §8.3')")
    requirement_de: str = Field(..., description="Requirement description in German")
    result: ComplianceCheckResult = Field(..., description="Check result")
    finding_de: Optional[str] = Field(None, description="Finding description in German (if not pass)")
    recommendation_de: Optional[str] = Field(None, description="Recommended corrective action in German")
    severity: SeverityLevel = Field(SeverityLevel.INFO, description="Severity if not passed")
    confidence: ConfidenceLevel = Field(ConfidenceLevel.ESTIMATED, description="Confidence of this check")


class ACComplianceReport(BaseModel):
    """Complete AC installation compliance report."""

    model_config = {"from_attributes": True}

    vessel_id: Optional[str] = Field(None, description="AYDI vessel identifier")
    assessment_date: Optional[str] = Field(None, description="Assessment date (ISO 8601)")
    assessor: Optional[str] = Field(None, description="Assessor name or 'AYDI_automated'")

    # Compliance checks
    checks: list[ACComplianceCheck] = Field(default_factory=list, description="Individual compliance checks")
    total_checks: int = Field(0, ge=0, description="Total number of checks performed")
    passed: int = Field(0, ge=0, description="Number of checks passed")
    failed: int = Field(0, ge=0, description="Number of checks failed")
    warnings: int = Field(0, ge=0, description="Number of warnings")

    # Summary scores
    overall_compliance_score: Optional[float] = Field(None, ge=0, le=100, description="Overall compliance score (0-100)")
    safety_score: Optional[float] = Field(None, ge=0, le=100, description="Safety sub-score (0-100)")
    galvanic_protection_score: Optional[float] = Field(None, ge=0, le=100, description="Galvanic protection sub-score (0-100)")
    installation_quality_score: Optional[float] = Field(None, ge=0, le=100, description="Installation quality sub-score (0-100)")

    # Critical findings
    critical_findings: list[str] = Field(default_factory=list, description="Critical findings requiring immediate action")
    improvement_priority_de: list[str] = Field(default_factory=list, description="Prioritized improvements in German")

    confidence: ConfidenceLevel = Field(ConfidenceLevel.ESTIMATED, description="Overall confidence level")
```

### ANHANG R — Hersteller-Vergleichs- und Empfehlungsmodelle

```python
class ManufacturerProfile(BaseModel):
    """Profile of an inverter/shore power equipment manufacturer."""

    model_config = {"from_attributes": True}

    name: str = Field(..., description="Manufacturer name")
    country: str = Field(..., description="Country of origin")
    founded_year: Optional[int] = Field(None, description="Year founded")
    website: Optional[str] = Field(None, description="Website URL")
    product_categories: list[str] = Field(default_factory=list, description="Product categories offered")
    marine_market_share_percent: Optional[float] = Field(None, ge=0, le=100, description="Estimated marine market share in Europe")
    warranty_years: Optional[int] = Field(None, ge=0, description="Standard warranty in years")
    support_quality: Optional[str] = Field(None, description="Support quality rating: 'excellent', 'good', 'average', 'poor'")
    communication_protocols: list[str] = Field(default_factory=list, description="Supported communication protocols")
    eu_service_network: Optional[str] = Field(None, description="EU service network coverage: 'extensive', 'good', 'limited'")
    price_segment: str = Field("mid", description="Price segment: 'budget', 'mid', 'premium', 'luxury'")


class InverterRecommendation(BaseModel):
    """Inverter/charger recommendation for a specific vessel."""

    model_config = {"from_attributes": True}

    vessel_id: Optional[str] = Field(None, description="AYDI vessel identifier")
    vessel_type: str = Field(..., description="Vessel type description")
    vessel_length_m: float = Field(..., ge=0, description="Vessel length in meters")
    system_voltage: SystemVoltage = Field(..., description="DC system voltage")
    usage_profile: str = Field(..., description="Usage profile: 'harbor', 'coastal', 'offshore', 'bluewater', 'liveaboard'")

    # Recommendations
    primary_recommendation: InverterSpec = Field(..., description="Primary recommended inverter")
    alternative_recommendations: list[InverterSpec] = Field(default_factory=list, description="Alternative recommendations")
    shore_power_recommendation: ShorePowerSizingResult = Field(..., description="Shore power sizing recommendation")
    galvanic_protection_recommendation: GalvanicProtectionType = Field(..., description="Recommended galvanic protection")
    transformer_recommendation: Optional[IsolationTransformerSpec] = Field(None, description="Recommended transformer (if applicable)")

    # Cost estimate
    total_estimated_cost_eur: Optional[float] = Field(None, ge=0, description="Total estimated system cost in EUR")
    installation_cost_eur: Optional[float] = Field(None, ge=0, description="Estimated installation cost in EUR")

    reasoning_de: str = Field(..., description="Reasoning for recommendation in German")
    confidence: ConfidenceLevel = Field(ConfidenceLevel.ESTIMATED, description="Confidence level")


class ACSystemScoreFusion(BaseModel):
    """Score fusion result combining structured and visual analysis of AC system."""

    model_config = {"from_attributes": True}

    vessel_id: Optional[str] = Field(None, description="AYDI vessel identifier")

    # Structured analysis scores
    structured_compliance_score: Optional[float] = Field(None, ge=0, le=100)
    structured_safety_score: Optional[float] = Field(None, ge=0, le=100)
    structured_galvanic_score: Optional[float] = Field(None, ge=0, le=100)
    structured_installation_score: Optional[float] = Field(None, ge=0, le=100)
    structured_confidence: ConfidenceLevel = Field(ConfidenceLevel.ESTIMATED)

    # Visual analysis scores
    visual_installation_score: Optional[float] = Field(None, ge=0, le=100)
    visual_cable_routing_score: Optional[float] = Field(None, ge=0, le=100)
    visual_corrosion_score: Optional[float] = Field(None, ge=0, le=100)
    visual_confidence: ConfidenceLevel = Field(ConfidenceLevel.VISUAL_MEDIUM)

    # Fused scores (compliance module weights: structured 0.95, visual 0.05)
    fused_compliance_score: Optional[float] = Field(None, ge=0, le=100, description="Fused compliance score (95% structured, 5% visual)")
    fused_safety_score: Optional[float] = Field(None, ge=0, le=100, description="Fused safety score")

    # Materials module weights: structured 0.35, visual 0.65
    fused_materials_score: Optional[float] = Field(None, ge=0, le=100, description="Fused materials/corrosion score (35% structured, 65% visual)")

    overall_ac_score: Optional[float] = Field(None, ge=0, le=100, description="Overall AC system score")
    confidence: ConfidenceLevel = Field(ConfidenceLevel.ESTIMATED, description="Overall confidence")
    assessment_summary_de: str = Field("", description="Assessment summary in German")
```

---

### ANHANG R.1 — AYDI-Analysefunktionen: Berechnungsbeispiele

```python
"""
AYDI Calculation Functions — 22.07 Wechselrichter und Landstrom
Pure functions for analysis modules — no database access.
"""

from typing import Optional


def calculate_dc_cable_cross_section(
    power_w: float,
    system_voltage_v: float,
    cable_length_m: float,
    max_voltage_drop_percent: float = 3.0,
    copper_resistivity: float = 0.0175,
) -> float:
    """
    Calculate required DC cable cross-section for inverter feed.

    Args:
        power_w: Maximum inverter power in watts (use surge rating)
        system_voltage_v: DC system voltage (12, 24, or 48)
        cable_length_m: One-way cable length in meters
        max_voltage_drop_percent: Maximum allowed voltage drop (default 3%)
        copper_resistivity: Copper resistivity in Ohm*mm²/m (default 0.0175)

    Returns:
        Required cable cross-section in mm² (round up to standard size)
    """
    max_current_a = power_w / system_voltage_v
    max_voltage_drop_v = system_voltage_v * (max_voltage_drop_percent / 100)
    max_resistance_ohm = max_voltage_drop_v / max_current_a
    # Factor 2 for round trip (positive + negative cable)
    cross_section_mm2 = (copper_resistivity * 2 * cable_length_m) / max_resistance_ohm
    return cross_section_mm2


def calculate_inverter_runtime_hours(
    battery_capacity_ah: float,
    system_voltage_v: float,
    load_power_w: float,
    inverter_efficiency: float = 0.92,
    max_depth_of_discharge: float = 0.50,
) -> float:
    """
    Calculate inverter runtime from battery capacity.

    Args:
        battery_capacity_ah: Total battery capacity in Ah
        system_voltage_v: DC system voltage (12, 24, or 48)
        load_power_w: AC load power in watts
        inverter_efficiency: Inverter efficiency (default 0.92)
        max_depth_of_discharge: Maximum DOD (0.5 for AGM, 0.9 for LiFePO4)

    Returns:
        Runtime in hours
    """
    usable_energy_wh = battery_capacity_ah * system_voltage_v * max_depth_of_discharge
    total_draw_w = load_power_w / inverter_efficiency
    if total_draw_w <= 0:
        return float("inf")
    return usable_energy_wh / total_draw_w


def calculate_shore_power_requirement(
    consumers: list[dict],
    simultaneous_factor: float = 0.7,
) -> dict:
    """
    Calculate shore power connection requirement.

    Args:
        consumers: List of dicts with 'name', 'power_w', 'shore_only' (bool)
        simultaneous_factor: Factor for simultaneous usage (0.5-1.0)

    Returns:
        Dict with total_power_w, recommended_connection_a, transformer_va
    """
    total_power = sum(c["power_w"] for c in consumers)
    simultaneous_power = total_power * simultaneous_factor
    recommended_a = 16 if simultaneous_power <= 3680 else 32 if simultaneous_power <= 7360 else 63
    transformer_va = int(recommended_a * 230 * 1.2)  # 20% margin

    return {
        "total_power_w": total_power,
        "simultaneous_power_w": int(simultaneous_power),
        "recommended_connection_a": recommended_a,
        "transformer_va_recommended": transformer_va,
    }


def calculate_voltage_drop_ac(
    current_a: float,
    cable_length_m: float,
    cross_section_mm2: float,
    copper_resistivity: float = 0.0175,
    cos_phi: float = 1.0,
) -> dict:
    """
    Calculate AC voltage drop in a cable run.

    Args:
        current_a: Load current in amps
        cable_length_m: One-way cable length in meters
        cross_section_mm2: Cable cross-section in mm²
        copper_resistivity: Copper resistivity in Ohm*mm²/m
        cos_phi: Power factor of load

    Returns:
        Dict with voltage_drop_v, voltage_drop_percent, power_loss_w
    """
    resistance_ohm = (copper_resistivity * 2 * cable_length_m) / cross_section_mm2
    voltage_drop_v = current_a * resistance_ohm * cos_phi
    voltage_drop_percent = (voltage_drop_v / 230) * 100
    power_loss_w = current_a ** 2 * resistance_ohm

    return {
        "voltage_drop_v": round(voltage_drop_v, 2),
        "voltage_drop_percent": round(voltage_drop_percent, 2),
        "power_loss_w": round(power_loss_w, 2),
        "acceptable": voltage_drop_percent <= 5.0,
    }


def assess_corrosion_risk(
    hull_material: str,
    galvanic_protection: str,
    shore_power_hours_per_week: float,
    water_type: str = "salt",
    anode_condition: str = "good",
) -> dict:
    """
    Assess galvanic corrosion risk from shore power connection.

    Args:
        hull_material: 'grp', 'aluminum', 'steel', 'wood'
        galvanic_protection: 'none', 'galvanic_isolator', 'isolation_transformer'
        shore_power_hours_per_week: Hours per week connected to shore power
        water_type: 'salt', 'brackish', 'fresh'
        anode_condition: 'new', 'good', 'fair', 'depleted'

    Returns:
        Dict with risk_score (0-100), risk_level, recommendations_de
    """
    base_risk = 20  # baseline risk

    # Hull material factor
    hull_factors = {"grp": 1.0, "wood": 1.2, "steel": 1.8, "aluminum": 2.5}
    base_risk *= hull_factors.get(hull_material, 1.0)

    # Shore power exposure
    if shore_power_hours_per_week > 100:
        base_risk *= 1.5
    elif shore_power_hours_per_week > 40:
        base_risk *= 1.2

    # Protection
    protection_factors = {
        "none": 2.0,
        "galvanic_isolator": 0.6,
        "isolation_transformer": 0.1,
    }
    base_risk *= protection_factors.get(galvanic_protection, 1.0)

    # Water type
    water_factors = {"salt": 1.5, "brackish": 1.2, "fresh": 0.5}
    base_risk *= water_factors.get(water_type, 1.0)

    # Anode condition
    anode_factors = {"new": 0.8, "good": 1.0, "fair": 1.3, "depleted": 2.0}
    base_risk *= anode_factors.get(anode_condition, 1.0)

    risk_score = min(100, max(0, int(base_risk)))

    if risk_score >= 80:
        risk_level = "critical"
    elif risk_score >= 60:
        risk_level = "high"
    elif risk_score >= 40:
        risk_level = "moderate"
    elif risk_score >= 20:
        risk_level = "low"
    else:
        risk_level = "none"

    recommendations = []
    if galvanic_protection == "none":
        recommendations.append("Galvanischen Isolator installieren (Sofortmaßnahme)")
        if hull_material in ("aluminum", "steel"):
            recommendations.append("Trenntrafo DRINGEND empfohlen bei Metallrumpf")
    elif galvanic_protection == "galvanic_isolator":
        if risk_score >= 50:
            recommendations.append("Upgrade auf Trenntrafo empfohlen")
    if anode_condition in ("fair", "depleted"):
        recommendations.append("Opferanoden erneuern")
    if shore_power_hours_per_week > 100 and galvanic_protection != "isolation_transformer":
        recommendations.append("Bei Dauerbetrieb am Landstrom: Trenntrafo wirtschaftlich sinnvoll")

    return {
        "risk_score": risk_score,
        "risk_level": risk_level,
        "recommendations_de": recommendations,
    }


def recommend_inverter_size(
    consumers: list[dict],
    system_voltage_v: int = 24,
    safety_margin: float = 1.2,
) -> dict:
    """
    Recommend inverter size based on consumer list.

    Args:
        consumers: List of dicts with 'name', 'power_w', 'surge_factor', 'simultaneous' (bool)
        system_voltage_v: DC system voltage
        safety_margin: Safety margin factor (default 1.2 = 20%)

    Returns:
        Dict with recommended continuous/surge power, cable size, fuse size
    """
    simultaneous = [c for c in consumers if c.get("simultaneous", True)]
    total_continuous = sum(c["power_w"] for c in simultaneous)
    max_surge = max(
        (c["power_w"] * c.get("surge_factor", 1.0) for c in simultaneous),
        default=0,
    )

    recommended_continuous = int(total_continuous * safety_margin)
    recommended_surge = int(max(max_surge, total_continuous * 1.5))

    # Standard inverter sizes
    standard_sizes = [300, 500, 800, 1200, 1600, 2000, 2400, 3000, 4000, 5000, 6400, 8000, 10000]
    selected_size = next(
        (s for s in standard_sizes if s >= recommended_continuous),
        standard_sizes[-1],
    )

    # DC cable (2m assumed)
    dc_current = selected_size * 2 / system_voltage_v  # surge current
    cable_mm2 = calculate_dc_cable_cross_section(selected_size * 2, system_voltage_v, 2.0)
    standard_cables = [6, 10, 16, 25, 35, 50, 70, 95, 120]
    selected_cable = next((c for c in standard_cables if c >= cable_mm2), standard_cables[-1])

    # Fuse
    fuse_current = int(selected_size * 1.5 / system_voltage_v)
    standard_fuses = [30, 40, 50, 60, 80, 100, 125, 150, 175, 200, 250, 300, 400, 500]
    selected_fuse = next((f for f in standard_fuses if f >= fuse_current), standard_fuses[-1])

    return {
        "total_continuous_w": total_continuous,
        "recommended_continuous_w": recommended_continuous,
        "recommended_surge_w": recommended_surge,
        "selected_inverter_size_w": selected_size,
        "system_voltage_v": system_voltage_v,
        "dc_cable_mm2": selected_cable,
        "dc_fuse_a": selected_fuse,
    }
```

---

## Ende der Wissensdatei 22.07 — Wechselrichter und Landstrom

> **Gesamtumfang:** ~3.800 Zeilen
> **Confidence-Quellen:** Hersteller-TDS (Victron, Mastervolt, Whisper Power, Fischer Panda, Xantrex, Sterling), IEC 60092-507, ISO 13297, ISO 10133, EN 60335-2-29, IEC 61558-2-4, ABYC E-11, Pantaenius Schadensstatistik, MAIB Reports, BSS Survey, Praxisberichte Fahrtensegler
