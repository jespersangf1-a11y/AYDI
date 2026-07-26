# 22.02 — Batteriesysteme im Yachtbau: Vollständige Wissensreferenz

> **AYDI Wissensdatei 22.02** — Kategorie 22: Elektrik und Verkabelung
> **Confidence-Quelle:** measured (Hersteller-TDS, ABYC E-11, ISO 10133), documented (Hersteller-Kataloge, Praxisberichte), estimated (Erfahrungswerte)
> **Letzte Aktualisierung:** 2026-05-04

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

### 1.1 Die Batterie als Herzstück der Bordelektrik

Die Batteriebank einer Yacht ist das zentrale Energiespeichersystem, von dem sämtliche elektrischen Verbraucher an Bord abhängen — von der Navigationsbeleuchtung über Autopilot und Funkgeräte bis zu Kühlschrank, Ankerwinde und Bug-/Heckstrahlruder. Ohne eine zuverlässige, korrekt dimensionierte und sachgerecht gewartete Batterieanlage ist ein Schiff weder seetüchtig noch bewohnbar.

**Statistische Relevanz:**
- Laut Pantaenius Schadensstatistik 2024 sind **18% aller Bordelektrik-Ausfälle** direkt auf Batteriefehler zurückzuführen
- BoatUS meldet, dass **fehlerhafte Batterieladung** die zweithäufigste Ursache für Brände auf Sportbooten ist
- Die durchschnittliche Lebensdauer einer Nassbatterie an Bord beträgt nur **2,8 Jahre** (vs. 5+ Jahre bei korrekter Behandlung)
- **73% aller Blei-Säure-Batterien** auf Gebrauchtbooten zeigen bei der Überprüfung bereits Sulfatierungsschäden

**Confidence:** documented — basierend auf Pantaenius Claims Data 2024, BoatUS Schadensberichte, Mastervolt Servicedaten.

### 1.2 Technologie-Entwicklung im Überblick

| Dekade | Dominante Technologie | Energiedichte | Zyklen (50% DoD) | Kosten/kWh |
|--------|----------------------|---------------|-------------------|------------|
| 1970er | Nass-Blei (offene Zellen) | 30–35 Wh/kg | 200–400 | ~€80 |
| 1980er | Geschlossene Blei-Säure | 33–38 Wh/kg | 300–500 | ~€100 |
| 1990er | AGM / Gel | 35–45 Wh/kg | 400–800 | ~€180 |
| 2000er | AGM Deep Cycle | 38–48 Wh/kg | 500–1.000 | ~€200 |
| 2010er | LiFePO4 (1. Generation) | 90–120 Wh/kg | 2.000–3.000 | ~€800 |
| 2020er | LiFePO4 (3. Generation + BMS) | 130–160 Wh/kg | 3.500–6.000 | ~€400 |
| 2025+ | LiFePO4/LTO/Na-Ion | 140–180 Wh/kg | 5.000–15.000 | ~€300 |

### 1.3 Kosten-Nutzen-Analyse nach Yachtklasse

**Produktionssegelboot (8–14m, Weekender/Coastal Cruiser):**
- Typischer Energiebedarf: 80–200 Ah/Tag bei 12V
- Empfehlung: 2× AGM 100 Ah (Versorgung) + 1× AGM 70 Ah (Starter)
- Investition: €600–€1.200
- Lithium-Upgrade lohnt ab >100 Seetagen/Jahr oder bei Gewichtsproblemen

**Semi-Custom Fahrtenyacht (12–20m, Blauwasser):**
- Typischer Energiebedarf: 200–500 Ah/Tag bei 12V oder 24V
- Empfehlung: LiFePO4 400–800 Ah (Versorgung) + 1× AGM (Starter)
- Investition: €3.000–€8.000
- Amortisation über 5–8 Jahre durch Zyklenlebensdauer

**Custom/Superyacht (18m+):**
- Typischer Energiebedarf: 500–3.000 Ah/Tag bei 24V oder 48V
- Empfehlung: LiFePO4-Systeme mit redundantem BMS, 24V oder 48V
- Investition: €15.000–€80.000+
- Immer professionelle Systemplanung erforderlich

**Motoryacht (8–15m, Küste/Binnengewässer):**
- Typischer Energiebedarf: 150–400 Ah/Tag bei 12V
- Empfehlung: AGM Dual Purpose oder LiFePO4 je nach Nutzungsprofil
- Investition: €800–€4.000
- Lichtmaschine als primäre Ladequelle, daher Ladeprofil-Kompatibilität kritisch

### 1.4 Relevante Normen und Standards

| Standard | Thema | Relevanz für Batterien |
|----------|-------|----------------------|
| ISO 10133:2012 | DC-Systeme auf kleinen Wasserfahrzeugen | Batterieinstallation, Belüftung, Absicherung |
| ISO 13297:2014 | AC-Systeme auf Booten | Ladegeräte, Shore-Power-Integration |
| ABYC E-11 | AC/DC Electrical Systems | Batterieraum, Belüftung, Kabelquerschnitte |
| ABYC E-10 | Storage Batteries | Spezifisch für Batterieinstallation |
| IEC 62619:2022 | Lithium-Sekundärzellen — Sicherheit | LiFePO4-Zertifizierung |
| IEC 62281 | Transport von Lithium-Zellen | Versand- und Lageranforderungen |
| UN 38.3 | Transportprüfung Lithiumbatterien | Pflichttest für alle Li-Batterien |
| EN 50342 | Blei-Säure-Starterbatterien | Automobilnorm, teils anwendbar |
| GL/DNV Rules | Klassifikation | Yachten >24m, Superyachten |

### 1.5 Typische Fehler und deren Vermeidung

Die häufigsten Batteriefehler auf Yachten sind nahezu immer vermeidbar. Die folgende Tabelle zeigt die **Top-10-Fehler** aus über 500 analysierten Schadensfällen:

| Rang | Fehler | Häufigkeit | Vermeidung |
|------|--------|-----------|------------|
| 1 | Chronische Unterladung (nie 100% SoC) | 34% | Regelmäßig Absorptionsphase abwarten |
| 2 | Falsches Ladeprofil für Batteriechemie | 22% | Bei Batterietausch Ladegerät prüfen |
| 3 | Batterie steht monatelang entladen | 18% | Winterlager-Protokoll einhalten |
| 4 | Überladung durch defekten Regler | 8% | Jährliche Ladespannungs-Kontrolle |
| 5 | Mischung alter/neuer Batterien parallel | 6% | Immer kompletten Satz tauschen |
| 6 | Zu kleine Bankkapazität für Verbrauch | 4% | Energiebilanz VOR Installation |
| 7 | Fehlende Absicherung am Batteriepol | 3% | ISO 10133 / ABYC E-10 einhalten |
| 8 | LiFePO4 an ungeregelte Lichtmaschine | 2% | DC-DC-Wandler / B2B-Lader verwenden |
| 9 | Batterie im Maschinenraum (Hitze) | 2% | Separaten belüfteten Standort wählen |
| 10 | LiFePO4 bei Frost geladen | 1% | BMS mit Temperaturüberwachung |

**Kostenmäßige Auswirkung:**
- Top-10-Fehler verursachen durchschnittlich **€800–€2.500** Folgekosten pro Vorfall
- 80% der Fehler sind durch korrekte Erstinstallation und Eigner-Schulung vermeidbar
- AYDI-Empfehlung: Systematische Prüfung bei Übernahme und jährlich

### 1.6 Batterie im Kontext der Yacht-Systemarchitektur

Die Batterie steht im Zentrum eines komplexen Energiesystems:

```
┌─────────────────────────────────────────────────────┐
│                  LADEQUELLEN                         │
│  ┌───────────┐ ┌──────────┐ ┌────────┐ ┌────────┐  │
│  │Landstrom  │ │Licht-    │ │Solar   │ │Wind-   │  │
│  │Ladegerät  │ │maschine  │ │MPPT    │ │generator│  │
│  └─────┬─────┘ └────┬─────┘ └───┬────┘ └───┬────┘  │
│        │             │           │           │       │
│        └──────┬──────┘───────────┘───────────┘       │
│               │                                      │
│        ┌──────▼──────┐                               │
│        │    BMS      │← Überwacht & schützt          │
│        └──────┬──────┘                               │
│               │                                      │
│        ┌──────▼──────┐                               │
│        │ BATTERIE-   │                               │
│        │   BANK      │                               │
│        └──────┬──────┘                               │
│               │                                      │
│        ┌──────▼──────┐                               │
│        │Batterie-    │                               │
│        │schalter     │                               │
│        └──────┬──────┘                               │
│               │                                      │
│  ┌────────────┼────────────────────────────────┐     │
│  │            │        VERBRAUCHER             │     │
│  │  ┌────────▼──────┐  ┌──────────┐  ┌─────┐  │     │
│  │  │Wechselrichter │  │DC-Panel  │  │Motor│  │     │
│  │  │(230V AC)      │  │(12/24V)  │  │Start│  │     │
│  │  └───────────────┘  └──────────┘  └─────┘  │     │
│  └─────────────────────────────────────────────┘     │
│                                                      │
│        ┌─────────────┐                               │
│        │ MONITORING  │← Batteriemonitor/Shunt        │
│        │ (App/VRM)   │                               │
│        └─────────────┘                               │
└─────────────────────────────────────────────────────┘
```

### 1.7 Systemspannung — 12V vs. 24V vs. 48V

| Kriterium | 12V | 24V | 48V |
|-----------|-----|-----|-----|
| Typische Bootsgröße | <12m | 12–20m | >18m / E-Antrieb |
| Strom bei 3 kW Last | 250 A | 125 A | 62,5 A |
| Kabelquerschnitt (bei 3% Vdrop, 5m) | 70 mm² | 35 mm² | 16 mm² |
| Verfügbarkeit Verbraucher | Sehr gut | Gut | Begrenzt |
| Sicherheit (Berührspannung) | Unkritisch | Unkritisch | Bedingt kritisch |
| Wechselrichter-Effizienz | 90–93% | 93–96% | 95–98% |
| Kosten Peripherie | Niedrig | Mittel | Hoch |

### 1.8 Batterie-Lebensdauer: Einflussfaktoren

Die Lebensdauer einer Bootsbatterie wird von folgenden Faktoren bestimmt (absteigend nach Einfluss):

| Faktor | Einfluss | Erläuterung |
|--------|---------|-------------|
| Ladeprofil-Korrektheit | ★★★★★ | Falsche Absorptionsspannung = #1 Killer |
| Entladetiefe (DoD) | ★★★★★ | Tiefer = kürzer. Exponentieller Zusammenhang |
| Temperatur (Betrieb) | ★★★★☆ | Pro 10°C über 25°C: halbe Lebensdauer (Blei) |
| Lagerung im Winterlager | ★★★★☆ | Entladen stehen = Sulfatierung innerhalb Wochen |
| Vollständige Ladung (regelmäßig) | ★★★☆☆ | Mindestens alle 2 Wochen 100% SoC erreichen |
| Vibrationsbelastung | ★★☆☆☆ | Marine-Grade vs. Automobil-Qualität |
| Ladestrom-Höhe | ★★☆☆☆ | Zu schnelles Laden stresst Blei-Platten |
| Parallelschaltungs-Qualität | ★☆☆☆☆ | Nur identische Batterien parallel |

### 1.9 Abgrenzung: Starter- vs. Versorgungsbank

| Aspekt | Starterbatterie | Versorgungsbank |
|--------|----------------|-----------------|
| Hauptaufgabe | Hoher Strom für 5–30 Sekunden | Moderate Ströme über Stunden |
| Plattendesign | Viele dünne Platten (Oberfläche) | Wenige dicke Platten (Masse) |
| CCA-Wert | Hoch (500–1.200 A) | Irrelevant |
| Zyklenlebensdauer | Gering (50–150 bei 80% DoD) | Hoch (500–5.000+) |
| Typische Entladung | <5% DoD pro Startvorgang | 20–80% DoD täglich |
| Laden | Schnell nach Start (Lichtmaschine) | Komplex (mehrstufig) |
| Trennung | Separater Kreis, Trennrelais | Separater Kreis, Trennrelais |
| Redundanz | 1 Batterie reicht | 2+ Batterien empfohlen |
| Konsequenz bei Ausfall | Motor startet nicht | Bordnetz tot (Navigation, Funk!) |

**Goldene Regel:** Starter und Versorgung IMMER getrennt! Die einzige Verbindung = Notfall-Paralleling über Batteriewahlschalter (Position „Beide").

**Confidence:** measured — ISO 10133, ABYC E-10/E-11 Normtexte; estimated — Kostenangaben.

---

## 2. Grundlagen und Theorie

### 2.1 Elektrochemie der Blei-Säure-Batterie

**Entladereaktion:**
```
Anode:    Pb + SO₄²⁻ → PbSO₄ + 2e⁻
Kathode:  PbO₂ + SO₄²⁻ + 4H⁺ + 2e⁻ → PbSO₄ + 2H₂O
Gesamt:   Pb + PbO₂ + 2H₂SO₄ → 2PbSO₄ + 2H₂O
```

**Zellspannung:** 2,05–2,15 V (Leerlauf, vollgeladen)
**Nennspannung:** 2,0 V pro Zelle → 6 Zellen = 12V-Batterie
**Elektrolyt:** Schwefelsäure (H₂SO₄), Dichte 1,265 kg/l bei Vollladung (25°C)

**Säuredichte als Ladezustandsindikator:**

| Ladezustand (SoC) | Säuredichte (kg/l) | Ruhespannung (12V) |
|-------------------|-------------------|-------------------|
| 100% | 1,265 | 12,73 V |
| 90% | 1,249 | 12,62 V |
| 80% | 1,233 | 12,50 V |
| 70% | 1,218 | 12,37 V |
| 60% | 1,204 | 12,24 V |
| 50% | 1,190 | 12,10 V |
| 40% | 1,176 | 11,96 V |
| 30% | 1,163 | 11,81 V |
| 20% | 1,149 | 11,66 V |
| 10% | 1,135 | 11,51 V |
| 0% | 1,120 | 11,36 V |

### 2.2 Elektrochemie der LiFePO4-Batterie

**Entladereaktion:**
```
Anode:    LiFePO₄ → FePO₄ + Li⁺ + e⁻
Kathode:  C₆ + Li⁺ + e⁻ → LiC₆
Gesamt:   LiFePO₄ + C₆ ↔ FePO₄ + LiC₆
```

**Zellspannung:** 3,2–3,3 V (nominal)
**Betriebsbereich:** 2,5 V (leer) bis 3,65 V (voll)
**4 Zellen in Serie:** 12,8 V nominal (= „12V LiFePO4")
**8 Zellen in Serie:** 25,6 V nominal (= „24V LiFePO4")

**LiFePO4 Spannungskurve (pro Zelle):**

| Ladezustand (SoC) | Zellspannung | 4S-Pack (12V) | 8S-Pack (24V) |
|-------------------|-------------|---------------|---------------|
| 100% | 3,60 V | 14,40 V | 28,80 V |
| 90% | 3,35 V | 13,40 V | 26,80 V |
| 80% | 3,32 V | 13,28 V | 26,56 V |
| 70% | 3,30 V | 13,20 V | 26,40 V |
| 60% | 3,28 V | 13,12 V | 26,24 V |
| 50% | 3,27 V | 13,08 V | 26,16 V |
| 40% | 3,26 V | 13,04 V | 26,08 V |
| 30% | 3,25 V | 13,00 V | 26,00 V |
| 20% | 3,20 V | 12,80 V | 25,60 V |
| 10% | 3,05 V | 12,20 V | 24,40 V |
| 0% | 2,50 V | 10,00 V | 20,00 V |

**Besonderheit:** Die extrem flache Spannungskurve zwischen 20% und 80% SoC macht eine spannungsbasierte Ladezustandsermittlung bei LiFePO4 nahezu unmöglich. Coulomb-Counting oder impedanzbasierte Methoden sind erforderlich.

### 2.3 Kapazität — Ah und Wh

**Amperestunden (Ah):**
Die nominelle Kapazität einer Batterie in Ah gibt an, wie viele Stunden ein bestimmter Strom entnommen werden kann. Standardmäßig wird die Kapazität bei **C/20** (20-Stunden-Entladerate) angegeben.

- Beispiel: 100 Ah (C/20) = 5 A über 20 Stunden
- Bei höherer Entladerate sinkt die nutzbare Kapazität (Peukert-Effekt bei Blei)

**Wattstunden (Wh):**
Die tatsächlich nutzbare Energie ergibt sich aus:
```
Wh = Ah × Nennspannung
```

- 100 Ah × 12,0 V = 1.200 Wh = 1,2 kWh (Blei-Säure)
- 100 Ah × 12,8 V = 1.280 Wh = 1,28 kWh (LiFePO4)

**Nutzbare Kapazität:**
- Blei-Säure: maximal 50% DoD empfohlen → 100 Ah nutzbar = 600 Wh
- AGM Deep Cycle: maximal 60% DoD → 100 Ah nutzbar = 720 Wh
- LiFePO4: bis 80–90% DoD → 100 Ah nutzbar = 1.024–1.152 Wh

→ Eine 100-Ah-LiFePO4 liefert die gleiche nutzbare Energie wie eine **200-Ah-Blei-Säure**

### 2.4 C-Rate

Die C-Rate beschreibt den Lade-/Entladestrom relativ zur Nennkapazität:

| C-Rate | Bei 100 Ah | Bei 200 Ah | Typische Anwendung |
|--------|-----------|-----------|-------------------|
| C/20 | 5 A | 10 A | Nennkapazitäts-Messung |
| C/10 | 10 A | 20 A | Normale Entladung |
| C/5 | 20 A | 40 A | Hohe Entladung |
| C/2 | 50 A | 100 A | Sehr hohe Entladung |
| 1C | 100 A | 200 A | Startvorgang / Wechselrichter-Spitze |
| 2C | 200 A | 400 A | Nur LiFePO4, Strahlruder |

**Maximale Lade-/Entladeraten nach Technologie:**

| Technologie | Max. Entladerate | Max. Laderate | Pulsbelastung (30s) |
|-------------|-----------------|---------------|---------------------|
| Nass-Blei (Starter) | 5C (CCA) | C/5 | 10C |
| Nass-Blei (Versorgung) | C/3 | C/10 | 2C |
| AGM | C/2 | C/5 (Schnellladung C/3) | 3C |
| Gel | C/3 | C/10 | 2C |
| LiFePO4 | 1–2C (kontinuierlich) | 1C (optimal 0,5C) | 5C |
| LTO | 5C (kontinuierlich) | 5C | 10C |

### 2.5 Peukert-Effekt

Der Peukert-Effekt beschreibt den überproportionalen Kapazitätsverlust bei höheren Entladeraten bei Blei-Säure-Batterien. Er ist bei Lithium-Batterien praktisch vernachlässigbar.

**Peukert-Gleichung:**
```
t = H × (C / (I × H))^k

Wobei:
  t = tatsächliche Entladezeit (Stunden)
  H = Nennentladezeit (z.B. 20h für C/20)
  C = Nennkapazität (Ah bei C/20)
  I = tatsächlicher Entladestrom (A)
  k = Peukert-Exponent (dimensionslos)
```

**Typische Peukert-Exponenten:**

| Batterietyp | Peukert-Exponent (k) | Bedeutung |
|-------------|---------------------|-----------|
| LiFePO4 | 1,02–1,05 | Nahezu ideal, kein relevanter Verlust |
| AGM (hochwertig) | 1,08–1,12 | Geringer Verlust bei hohen Strömen |
| AGM (Standard) | 1,12–1,18 | Moderater Verlust |
| Gel | 1,10–1,15 | Moderater Verlust |
| Nass-Blei (Deep Cycle) | 1,15–1,25 | Deutlicher Verlust |
| Nass-Blei (Starter) | 1,25–1,40 | Starker Verlust bei Dauerentladung |

**Praxisbeispiel:**
100 Ah Nass-Blei-Batterie (k=1,25), Entladung mit 50 A (= C/2):
```
t = 20 × (100 / (50 × 20))^1,25 = 20 × (0,1)^1,25 = 20 × 0,0562 = 1,12 h
Nutzbare Kapazität: 50 A × 1,12 h = 56 Ah (statt nominell 100 Ah)
```

→ Bei C/2-Entladung stehen nur noch **56% der Nennkapazität** zur Verfügung!

### 2.6 Entladetiefe (DoD) und Zyklenlebensdauer

**DoD (Depth of Discharge)** = der Anteil der Kapazität, der entnommen wird.
**SoC (State of Charge)** = 100% − DoD

**Zyklenlebensdauer in Abhängigkeit der DoD:**

| Technologie | 20% DoD | 30% DoD | 50% DoD | 80% DoD | 100% DoD |
|-------------|---------|---------|---------|---------|----------|
| Nass-Blei (Versorgung) | 1.800 | 1.200 | 500 | 200 | 80 |
| AGM (Deep Cycle) | 2.500 | 1.800 | 800 | 400 | 200 |
| AGM (Dual Purpose) | 1.500 | 1.000 | 500 | 250 | 120 |
| Gel (Deep Cycle) | 3.500 | 2.500 | 1.200 | 600 | 300 |
| LiFePO4 (Grade A) | >10.000 | 6.000 | 3.500 | 2.500 | 2.000 |
| LiFePO4 (Grade B) | >5.000 | 3.500 | 2.000 | 1.200 | 800 |
| LTO | >20.000 | >15.000 | >10.000 | 7.000 | 5.000 |

**Empfohlene maximale DoD im Dauerbetrieb:**

| Technologie | Empfohlene Max-DoD | Begründung |
|-------------|-------------------|------------|
| Nass-Blei | 50% | Sulfatierungsgefahr unter 12,0 V |
| AGM | 50–60% | Optimale Zyklen-/Kosten-Balance |
| Gel | 60–70% | Gel-Struktur toleriert tiefere Entladung |
| LiFePO4 | 80% (BMS-begrenzt) | BMS schaltet bei 10–20% SoC ab |
| LTO | 90–95% | Extrem robuste Chemie |

### 2.7 Ladekurven und Ladeprofile

#### 2.7.1 IUoU-Ladeprofil (Blei-Säure/AGM/Gel)

Das Standard-Ladeverfahren für Blei-Säure-Batterien ist das **IUoU-Verfahren** (auch IUIa oder 3-Stufen-Ladung):

**Stufe 1 — Bulk (I-Phase / Konstantstrom):**
- Ladestrom: maximal C/5 (AGM: C/3 möglich)
- Dauer: bis Absorptionsspannung erreicht
- Lädt ca. 80% der Kapazität
- Batterie „zieht" den vollen verfügbaren Strom

**Stufe 2 — Absorption (U-Phase / Konstantspannung):**
- Spannung wird konstant auf Absorptionsniveau gehalten
- Strom sinkt exponentiell ab
- Endet wenn Strom < C/100 (= Tail Current)
- Dauer: 1–4 Stunden je nach Zustand
- Kritisch für Vollladung und Anti-Sulfatierung

**Stufe 3 — Float (Uo-Phase / Erhaltungsladung):**
- Reduzierte Konstantspannung
- Kompensiert Selbstentladung
- Nur bei Dauerlandstrom-Versorgung (Hafen)
- Nicht nötig wenn Batterie abgeklemmt wird

**Ladespannungen (12V-System, 25°C):**

| Parameter | Nass-Blei | AGM | Gel |
|-----------|----------|-----|-----|
| Absorptionsspannung | 14,4 V | 14,4–14,7 V | 14,1–14,4 V |
| Absorptionszeit | 2–4 h | 1–3 h | 3–5 h |
| Float-Spannung | 13,3–13,5 V | 13,5–13,8 V | 13,5–13,8 V |
| Temperaturkompensation | −3 mV/°C/Zelle | −3 mV/°C/Zelle | −4 mV/°C/Zelle |
| Max. Ladestrom | C/5 | C/3 | C/10 |
| Tail Current (Ende Absorption) | C/100 | C/100 | C/100 |
| Equalization | 15,5 V (30 min) | NICHT ERLAUBT | NICHT ERLAUBT |

**WARNUNG:** Gel-Batterien dürfen NIEMALS mit >14,4 V geladen werden. Überspannung zerstört irreversibel die Gel-Struktur (Gasbildung → Hohlräume → Kapazitätsverlust). Viele „Standard-Blei"-Ladegeräte laden mit bis zu 14,8 V und sind daher für Gel UNGEEIGNET.

#### 2.7.2 CC-CV-Ladeprofil (LiFePO4)

**Stufe 1 — CC (Constant Current):**
- Ladestrom: typisch 0,5C, maximal 1C
- Dauer: bis Abschaltspannung des BMS erreicht (14,4–14,6 V bei 4S)
- Lädt ca. 90–95% der Kapazität
- Sehr kurze Phase bei LiFePO4 wegen flacher Kurve

**Stufe 2 — CV (Constant Voltage):**
- Optional und kurz (oft nur 15–30 min)
- Viele BMS schalten direkt nach CC ab
- Endet bei Tail Current < C/50

**Kein Float nötig!** LiFePO4 hat nur 1–3% Selbstentladung/Monat. Dauer-Float schadet sogar (Überladung einzelner Zellen möglich).

**LiFePO4-Ladeparameter (12V = 4S-Pack):**

| Parameter | Wert | Anmerkung |
|-----------|------|-----------|
| CC-Ladestrom (empfohlen) | 0,5C | 50 A bei 100 Ah |
| CC-Ladestrom (maximal) | 1C | BMS-Limit beachten |
| CV-Spannung | 14,2–14,6 V | Herstellerabhängig |
| Abschaltspannung (BMS) | 14,4–14,8 V | Zellenspezifisch |
| Unterspannungs-Abschaltung | 10,0–11,0 V | BMS schützt vor Tiefentladung |
| Float-Spannung | 13,5 V (wenn nötig) | Nur zur Kompensation von Bordverbrauch |
| Temperaturbereich Laden | 0–45°C | NIEMALS unter 0°C laden! |
| Temperaturbereich Entladen | −20 bis +60°C | Kapazitätsreduktion bei Kälte |

**KRITISCHE WARNUNG:** LiFePO4-Zellen dürfen **NIEMALS unter 0°C geladen** werden! Lithium-Plating (metallisches Lithium lagert sich an der Anode ab) ist irreversibel, reduziert die Kapazität drastisch und kann zu internen Kurzschlüssen führen. Hochwertige BMS mit Temperaturüberwachung sperren den Ladeeingang automatisch bei <0°C.

### 2.8 Temperatureinfluss

**Kapazität vs. Temperatur:**

| Temperatur | Blei-Säure (% Nennkapazität) | LiFePO4 (% Nennkapazität) |
|------------|------------------------------|---------------------------|
| −20°C | 50% | 70% |
| −10°C | 65% | 80% |
| 0°C | 80% | 90% |
| 10°C | 90% | 95% |
| 20°C | 95% | 98% |
| 25°C | 100% (Referenz) | 100% (Referenz) |
| 30°C | 102% | 100% |
| 40°C | 105% | 98% |
| 50°C | 107% (Lebensdauer ↓↓) | 95% (Alterung ↑) |

**Temperatur und Lebensdauer (Blei-Säure):**
Faustregel: Pro **10°C über 25°C** halbiert sich die Lebensdauer.
- 25°C: 100% Lebensdauer (Referenz)
- 35°C: 50% Lebensdauer
- 45°C: 25% Lebensdauer
- 55°C: 12,5% Lebensdauer

**Marine-Relevanz:** Im Maschinenraum herrschen oft 40–60°C. Batterien sollten NIEMALS im Maschinenraum installiert werden (Ausnahme: Starterbatterie mit entsprechender Wärmeabschirmung). Idealer Standort: belüfteter, aber isolierter Batteriekasten unter der Salon-Sitzbank oder in einer separaten Batterieboxe mit Entlüftung.

### 2.9 Selbstentladung

| Technologie | Selbstentladung/Monat (25°C) | Selbstentladung/Monat (40°C) |
|-------------|------------------------------|------------------------------|
| Nass-Blei | 5–15% | 15–30% |
| AGM | 1–3% | 5–10% |
| Gel | 1–3% | 4–8% |
| LiFePO4 | 1–3% | 2–5% |
| LTO | <1% | 1–2% |

**Konsequenz für Winterlager:**
- Nass-Blei: monatliche Nachladung oder Erhaltungsladegerät zwingend
- AGM/Gel: alle 2–3 Monate nachlade, oder Erhaltungsladegerät empfohlen
- LiFePO4: auf 50–60% SoC lagern, kein Ladegerät nötig (BMS-Ruhestrom beachten!)
- BMS-Ruhestrom: 5–50 mA → kann bei 6 Monaten 2–15 Ah verbrauchen

### 2.10 Innenwiderstand

Der Innenwiderstand (Ri) einer Batterie bestimmt:
- Maximal möglichen Strom (Kurzschlussstrom = U/Ri)
- Spannungsabfall unter Last (ΔU = I × Ri)
- Wärmeentwicklung bei hohen Strömen (P = I² × Ri)
- Ladeeffizienz (höherer Ri = mehr Wärmeverluste)

**Typische Innenwiderstandswerte (12V, 100 Ah, neu):**

| Technologie | Ri (mΩ) | Kurzschlussstrom | Spannungsabfall bei 100 A |
|-------------|---------|-----------------|--------------------------|
| Nass-Blei (Starter) | 4–6 | >2.000 A | 0,4–0,6 V |
| Nass-Blei (Deep Cycle) | 8–15 | 800–1.500 A | 0,8–1,5 V |
| AGM | 5–8 | 1.500–2.400 A | 0,5–0,8 V |
| Gel | 10–15 | 800–1.200 A | 1,0–1,5 V |
| LiFePO4 | 2–5 | >2.500 A | 0,2–0,5 V |
| LTO | 1–3 | >4.000 A | 0,1–0,3 V |

**Innenwiderstand als Zustandsindikator:**
- Neuwert: Herstellerangabe (Datenblatt)
- Ende der Lebensdauer: Ri = 2× Neuwert (Blei) bzw. 1,5× Neuwert (LiFePO4)
- Stark sulfatierte Batterie: Ri > 3× Neuwert → Batterie irreversibel geschädigt

### 2.11 Energiebilanz-Berechnung

Die korrekte Dimensionierung der Batteriebank beginnt mit der **Energiebilanz**:

**Schritt 1: Verbraucherliste erstellen**
```
Verbraucher × Leistung (W) × Betriebsstunden/Tag = Energiebedarf (Wh/Tag)
```

**Schritt 2: Gesamtbedarf berechnen**
```
Σ aller Verbraucher = Tagesbedarf (Wh)
Tagesbedarf / Systemspannung = Tagesbedarf (Ah)
```

**Schritt 3: Batteriebank dimensionieren**
```
Bankkapazität = Tagesbedarf (Ah) × Autonomie-Tage / max. DoD

Blei-Säure:  Bankkapazität = Tagesbedarf × 3 / 0,50 = 6 × Tagesbedarf
LiFePO4:     Bankkapazität = Tagesbedarf × 3 / 0,80 = 3,75 × Tagesbedarf
```

**Beispiel: 12m Fahrtenyacht, 2 Personen, Überfahrt ohne Landstrom:**

| Verbraucher | Leistung (W) | Stunden/Tag | Wh/Tag |
|-------------|-------------|-------------|--------|
| Kühlschrank | 50 | 12 (Kompressor-Takt) | 600 |
| Navigationsbeleuchtung | 25 | 10 | 250 |
| Autopilot | 60 | 20 | 1.200 |
| Instrumentierung/GPS | 15 | 24 | 360 |
| Funk (Standby) | 5 | 24 | 120 |
| LED-Innenbeleuchtung | 20 | 5 | 100 |
| Wasserpumpe | 60 | 0,5 | 30 |
| Laptop/Laden | 60 | 3 | 180 |
| **Gesamt** | | | **2.840 Wh** |

→ 2.840 Wh / 12 V = **237 Ah/Tag**
→ 3 Tage Autonomie, 50% DoD (Blei): 237 × 3 / 0,5 = **1.422 Ah Blei-Säure**
→ 3 Tage Autonomie, 80% DoD (LiFePO4): 237 × 3 / 0,8 = **889 Ah LiFePO4**

**Confidence:** calculated — Berechnung nach ABYC E-11 Methodik.

### 2.12 Parallelschaltung — Elektrisches Verhalten

Bei parallel geschalteten Batterien teilt sich der Strom nach dem Verhältnis der Innenwiderstände auf:

```
I₁ = I_total × (Ri_gesamt / Ri₁)
Ri_gesamt = 1 / (1/Ri₁ + 1/Ri₂ + ... + 1/Ri_n)
```

**Problem: Ungleiche Innenwiderstände**
- Neue Batterie (Ri = 5 mΩ) parallel mit alter Batterie (Ri = 12 mΩ)
- Bei 100 A Gesamtentladung:
  - Neue Batterie: 100 × 12/(5+12) = 70,6 A (71% der Last!)
  - Alte Batterie: 100 × 5/(5+12) = 29,4 A (29% der Last)
- → Neue Batterie wird überproportional belastet und altert schneller

**Cross-Diagonal-Verkabelung:**
Bei 2+ parallelen Batterien IMMER cross-diagonal verkabeln:
```
[Batt 1]+──┐    ┌──[Batt 2]+
            │    │
      Verbraucher (+)
            │    │
[Batt 1]−──┘    └──[Batt 2]−
        ↑                    ↑
  MINUS hier          PLUS hier
  nehmen              nehmen
```
→ Plus-Kabel an der letzten Batterie, Minus-Kabel an der ersten → identische Kabellängen → gleichmäßige Stromverteilung.

### 2.13 Ladeprioritäts-Management

Auf modernen Yachten existieren oft 3–5 Ladequellen gleichzeitig. Ohne Koordination kann es zu Konflikten kommen:

**Typische Ladequellen-Hierarchie:**

| Priorität | Quelle | Typischer Output | Verfügbarkeit |
|-----------|--------|-----------------|---------------|
| 1 (höchste) | Landstrom-Ladegerät | 30–120 A | Im Hafen |
| 2 | Dieselgenerator | 50–200 A | Auf See (Kraftstoff) |
| 3 | Lichtmaschine (Motor) | 50–120 A | Motor läuft |
| 4 | Solar (MPPT) | 5–40 A | Tagsüber |
| 5 | Windgenerator | 3–25 A | Bei Wind |
| 6 | Hydrogenerator | 3–15 A | Bei Fahrt >5 kn |

**Koordinations-Strategien:**

1. **Unkoordiniert (Budget):** Jede Quelle lädt unabhängig. Problem: Überlagerung der Absorptionsspannungen, BMS-Verwirrung.
2. **Dioden-Trennung:** Ladeströme über Dioden zusammengeführt. Problem: 0,6V Spannungsabfall pro Diode → Unterladung.
3. **Smart-Relais (Cyrix):** Victron Cyrix verbindet/trennt Bänke spannungsgesteuert. Besser, aber nicht intelligent.
4. **BMS-gesteuert (optimal):** VE.Bus BMS v2 oder MasterBus kommuniziert mit allen Ladequellen → koordinierte Abschaltung bei Voll/Fehler.
5. **DC-DC-Wandler (B2B):** Isolierte Ladequelle (z.B. Orion-Tr Smart). Vollständige Entkopplung. Optimal für LiFePO4 + Lichtmaschine.

### 2.14 Wechselrichter-Dimensionierung und Batteriebezug

Die Batterie muss den Wechselrichter-Spitzenstrom liefern können:

```
I_batterie = P_wechselrichter / (η × U_batterie)

Wobei:
  P_wechselrichter = AC-Ausgangsleistung in Watt
  η = Wechselrichter-Wirkungsgrad (0,85–0,95)
  U_batterie = Batterie-Nominalspannung unter Last
```

**Beispiele:**

| Wechselrichter | AC-Leistung | Spitze | Batteriestrom (12V) | Min. Bankkapazität |
|----------------|-------------|--------|--------------------|--------------------|
| 800 W | 800 W | 1.600 W | 75 A (Spitze: 150 A) | 150 Ah AGM |
| 2.000 W | 2.000 W | 4.000 W | 190 A (Spitze: 380 A) | 400 Ah AGM / 200 Ah LiFePO4 |
| 3.000 W | 3.000 W | 6.000 W | 285 A (Spitze: 570 A) | 600 Ah AGM / 300 Ah LiFePO4 |
| 5.000 W | 5.000 W | 10.000 W | 475 A (Spitze: 950 A) | Nur 24V/48V System |

**Faustregel:** Batteriebank-Kapazität (Ah) ≥ 2× maximaler Dauerstrom des Wechselrichters (A) bei Blei-Säure, 1× bei LiFePO4.

---

## 3. Typenübersicht

### 3.1 Nass-Blei-Säure (Flooded Lead-Acid)

#### 3.1.1 Starterbatterie (SLI — Starting, Lighting, Ignition)

**Bauweise:** Viele dünne Platten für maximale Oberfläche → hoher Kurzzeitstrom (CCA)
**Anwendung:** Ausschließlich für Motorstart (Diesel/Benzin)
**Nicht geeignet für:** Zyklische Versorgung (zerstört Platten in wenigen Monaten)

| Eigenschaft | Wert |
|-------------|------|
| Zellenbauart | Dünne Gitterplatten, offene Zellen |
| Elektrolyt | Flüssige H₂SO₄, nachfüllbar |
| CCA (Cold Cranking Amps) | 400–1.000 A (je nach Größe) |
| Zyklenlebensdauer (80% DoD) | 50–150 |
| Empfohlene DoD | <5% (nur Startvorgang) |
| Wartung | Destilliertes Wasser nachfüllen, Pole fetten |
| Aufstellung | Aufrecht, belüftet (Gasung!) |
| Gasung | Ja (Knallgas H₂ + O₂ bei Überladung) |
| Temperaturbereich | −30 bis +60°C |
| Gewicht (je 100 Ah) | 25–30 kg |
| Preis (je 100 Ah) | €80–€150 |

**Marine-Starterbatterien vs. Automobil:**
- Marine: dickere Platten, vibrationsfeste Gitter, korrosionsbeständige Pole
- Automobil: dünnere Platten (höhere CCA), weniger vibrationsfest
- Empfehlung: IMMER dedizierte Marine-Starterbatterie verwenden

#### 3.1.2 Versorgungsbatterie (Deep Cycle Flooded)

**Bauweise:** Dickere Platten, robustere Gitter → höhere Zyklenlebensdauer
**Anwendung:** Bordnetz-Versorgung (Beleuchtung, Kühlschrank, Elektronik)
**Einschränkungen:** Gasung erfordert Belüftung, Wartung nötig, lageabhängig

| Eigenschaft | Wert |
|-------------|------|
| Zellenbauart | Dicke Panzerplatten oder Röhrchenplatten |
| Elektrolyt | Flüssige H₂SO₄, nachfüllbar |
| Zyklenlebensdauer (50% DoD) | 400–800 |
| Empfohlene DoD | 50% |
| Wartung | Destilliertes Wasser alle 4–8 Wochen |
| Aufstellung | Aufrecht, belüftet, säurefester Kasten |
| Gasung | Ja (weniger als Starter bei korrekter Ladung) |
| Gewicht (je 100 Ah) | 28–35 kg |
| Preis (je 100 Ah) | €120–€250 |

**Tropische Nassbatterien / Panzerplatten:**
- OPzS-Typ (Ortsfeste Panzerplatte, Spezial)
- 1.500–2.500 Zyklen bei 50% DoD
- Extrem langlebig, aber schwer (40+ kg/100 Ah) und teuer
- Einsatz: Langfahrt-Blauwasseryachten mit beschränktem Budget

### 3.2 AGM (Absorbent Glass Mat)

#### 3.2.1 AGM Deep Cycle

**Bauweise:** Glasfasermatten-Separator absorbiert Elektrolyt → kein freies Säure
**Vorteile:** Wartungsfrei, lageunabhängig (bis 90°), keine Gasung bei normalem Betrieb, höhere Lade-/Entladeströme als Nass-Blei

| Eigenschaft | Wert |
|-------------|------|
| Zellenbauart | Flache oder spiralförmige Platten mit AGM-Separator |
| Elektrolyt | In Glasfasermatten gebunden |
| Zyklenlebensdauer (50% DoD) | 600–1.200 |
| Empfohlene DoD | 50–60% |
| Max. Ladestrom | C/3 (manche Hersteller C/2,5) |
| Wartung | Keine (verschlossen) |
| Aufstellung | Lageunabhängig (nicht über Kopf) |
| Gasung | Nur bei Überladung (Sicherheitsventil) |
| Innenwiderstand | Niedrig (gut für hohe Ströme) |
| Gewicht (je 100 Ah) | 26–32 kg |
| Preis (je 100 Ah) | €200–€400 |

**Marine-AGM-Qualitätsmerkmale:**
- 99,99% reines Blei (Pure Lead AGM) → noch längere Lebensdauer
- Kupfer-legierte Gitter → niedrigerer Innenwiderstand
- Flammenrückschlag-Schutz am Ventil → Sicherheit bei Gasung
- Vibrationsfeste Zellverbindung → Hochsee-Einsatz

#### 3.2.2 AGM Dual Purpose

**Bauweise:** Kompromiss zwischen dünnen (Starter) und dicken (Deep Cycle) Platten
**Anwendung:** Kombinierte Starter-/Versorgungsbatterie für kleinere Boote
**Einschränkung:** Weder optimaler Starter noch optimaler Deep Cycle

| Eigenschaft | Wert |
|-------------|------|
| CCA | 600–800 A (bei 100 Ah) |
| Zyklenlebensdauer (50% DoD) | 300–600 |
| Empfohlene DoD | 40–50% |
| Einsatz | Motorboote <10m mit wenig Verbrauchern |
| Gewicht (je 100 Ah) | 25–30 kg |
| Preis (je 100 Ah) | €180–€350 |

**Empfehlung:** Dual-Purpose-Batterien sind nur für Boote mit geringem Energiebedarf sinnvoll, wo das Gewicht und der Platz für zwei getrennte Batterien fehlt. Ab 10m Bootslänge immer getrennte Starter- und Versorgungsbatterien verwenden.

### 3.3 Gel-Batterien

**Bauweise:** Elektrolyt durch Kieselsäure (SiO₂) zu Gel eingedickt
**Vorteile:** Extrem zyklenfest, unempfindlich gegen Tiefentladung, niedrige Selbstentladung
**Nachteile:** Empfindlich gegen Überladung, niedriger maximaler Ladestrom, höherer Innenwiderstand

| Eigenschaft | Wert |
|-------------|------|
| Zellenbauart | Platten mit Gel-Elektrolyt |
| Zyklenlebensdauer (50% DoD) | 1.000–1.800 |
| Zyklenlebensdauer (80% DoD) | 500–800 |
| Empfohlene DoD | 60–70% |
| Max. Ladestrom | C/10 (manche bis C/5) |
| Max. Ladespannung (12V) | 14,1–14,4 V (KRITISCH!) |
| Wartung | Keine |
| Aufstellung | Lageunabhängig |
| Gasung | Minimal (Rekombination >99%) |
| Temperaturempfindlichkeit | Höher als AGM |
| Gewicht (je 100 Ah) | 30–36 kg |
| Preis (je 100 Ah) | €280–€500 |

**Typischer Einsatz Marine:**
- Langfahrt-Yachten mit Solar-/Windladung (niedrige, konstante Ströme)
- Notbatterien in Sicherheitssystemen (geringe Selbstentladung)
- Charter-Yachten (robust gegen Bedienfehler bei Tiefentladung)

### 3.4 LiFePO4 (Lithium-Eisenphosphat)

#### 3.4.1 Prismatische Zellen

**Bauweise:** Großformatige rechteckige Zellen (typisch 100–280 Ah pro Zelle)
**Standard im Marinebereich:** 4 Zellen in Serie (4S) = 12,8V, 8S = 25,6V

| Eigenschaft | Wert |
|-------------|------|
| Zellformat | Prismatisch (CATL, EVE, BYD-Zellen) |
| Zellspannung | 3,2 V nominal |
| Zyklenlebensdauer (80% DoD) | 2.500–6.000 |
| Empfohlene DoD | 80% (BMS-gesteuert) |
| Max. Ladestrom | 0,5–1C (BMS-abhängig) |
| Max. Entladestrom | 1–3C (BMS-abhängig) |
| BMS erforderlich | JA — IMMER |
| Gewicht (je 100 Ah, 12V) | 12–15 kg |
| Energiedichte | 130–160 Wh/kg |
| Ladetemperatur | 0–45°C (UNTER 0°C VERBOTEN) |
| Selbstentladung | 1–3%/Monat |
| Preis (je 100 Ah, 12V, mit BMS) | €500–€1.200 |

**Grade-A vs. Grade-B Zellen:**
- Grade A: Direkt aus Erstproduktion, volle Kapazität, perfekte Qualitätskontrolle
- Grade B: Ausschuss mit leicht reduzierter Kapazität (95–98%), kosmetischen Mängeln
- Grade B gebraucht: Aus EV-Batterien ausgebaut, unbekannte Historie → NICHT EMPFOHLEN für Marine

#### 3.4.2 Zylindrische Zellen (21700/32700)

**Bauweise:** Viele kleine zylindrische Zellen in Serie/Parallel-Konfiguration
**Einsatz:** Kompakte Batterien, E-Außenborder, tragbare Powerstations

| Eigenschaft | Wert |
|-------------|------|
| Zellformat | 21700 (5 Ah) oder 32700 (6 Ah) |
| Konfiguration (100 Ah, 12V) | 4S20P (80 Zellen) |
| Vorteile | Flexibles Formdesign, Redundanz |
| Nachteile | Mehr Verbindungsstellen, komplexeres BMS |
| Typischer Einsatz | E-Antriebe, Powerstations, Retrofit |
| Preis (je 100 Ah, 12V) | €400–€800 |

### 3.5 LTO (Lithium-Titanat, Li₄Ti₅O₁₂)

**Bauweise:** Titanat-Anode statt Graphit → extrem schnellladefähig und langlebig
**Nachteil:** Niedrigere Energiedichte (nur 60–80 Wh/kg), höherer Preis

| Eigenschaft | Wert |
|-------------|------|
| Zellspannung | 2,4 V nominal |
| Zyklenlebensdauer (80% DoD) | 7.000–15.000+ |
| Max. Ladestrom | 5C (!) |
| Max. Entladestrom | 10C (!) |
| Temperaturbereich Laden | −30 bis +55°C |
| Gewicht (je 100 Ah, 12V) | 25–30 kg |
| Energiedichte | 60–80 Wh/kg |
| Sicherheit | Höchste aller Li-Technologien |
| Preis (je 100 Ah, 12V) | €1.500–€3.000 |

**Marine-Einsatz:**
- Hybrid-Antriebe mit schnellem Lade-/Entladezyklus
- Manövrierstrahlruder (hohe Pulsbelastung)
- Superyachten mit Lade-/Entladezyklen während Manöver
- Rennsegler (Gewicht sekundär, Leistung primär)

### 3.6 Natrium-Ionen (Na-Ion)

**Status 2025/2026:** Erste marine-taugliche Produkte in Markteinführung
**Vorteile:** Kein Lithium/Kobalt nötig, günstiger, kälteverträglicher
**Nachteile:** Noch geringere Energiedichte als LiFePO4, begrenzte Verfügbarkeit

| Eigenschaft | Wert (Stand 2025) |
|-------------|-------------------|
| Zellspannung | 3,1 V nominal |
| Energiedichte | 100–140 Wh/kg |
| Zyklenlebensdauer | 3.000–5.000 |
| Temperaturbereich | −20 bis +60°C (laden bei −20°C möglich!) |
| Sicherheit | Sehr hoch (kein Thermal Runaway) |
| Preis (Zielwert) | €150–€250/kWh |
| Marine-Eignung | Vielversprechend, aber noch früh |

**Confidence:** estimated — Na-Ion-Daten basieren auf Herstellerankündigungen (CATL, HiNa), noch keine langfristige Marine-Erfahrung.

### 3.7 BMS-Varianten für Marine-LiFePO4

#### 3.7.1 Internes BMS (All-in-One)

Das BMS ist im Batteriegehäuse integriert. Standard bei Consumer-Produkten (Battle Born, RELiON, Liontron).

| Eigenschaft | Wert |
|-------------|------|
| Standort | Im Batteriegehäuse |
| Kommunikation | Bluetooth (App), teils CAN |
| Balancer | Passiv (50–100 mA) |
| Schutzfunktionen | Überspannung, Unterspannung, Überstrom, Kurzschluss, Temperatur |
| Konfigurierbar | Meist nicht (feste Parameter) |
| Systemintegration | Begrenzt (keine Ladequellen-Steuerung) |
| Vorteil | Einfach, Plug-and-Play |
| Nachteil | Keine zentrale Steuerung aller Ladequellen |
| Empfehlung | Einfache Systeme, Retrofit, 1–2 Batterien |

#### 3.7.2 Externes BMS (Systemintegration)

Separates BMS kommuniziert mit Ladegeräten und Wechselrichter. Standard bei Victron (VE.Bus BMS) und Mastervolt (MasterBus).

| Eigenschaft | Wert |
|-------------|------|
| Standort | Separate Einheit + Zell-Überwachungsmodul |
| Kommunikation | VE.Bus, CAN, Modbus |
| Balancer | Passiv oder aktiv (je nach Modell) |
| Schutzfunktionen | Wie intern + Ladequellen-Abschaltung, Pre-Alarm |
| Konfigurierbar | Ja (Parameter über Software/App) |
| Systemintegration | Vollständig (steuert Ladegerät, Wechselrichter, Solar) |
| Vorteil | Maximale Sicherheit und Kontrolle |
| Nachteil | Komplexer, teurer, mehr Verkabelung |
| Empfehlung | Professionelle Systeme, >2 Batterien, Langfahrt |

#### 3.7.3 BMS-Vergleichsmatrix Marine-Markt

| BMS | Hersteller | Typ | Zellen | Max. Strom | Balancer | Protokoll | Preis |
|-----|-----------|-----|--------|-----------|----------|-----------|-------|
| VE.Bus BMS v2 | Victron | Extern | 4–48 | Unbegrenzt (Relais) | Intern | VE.Bus, Bluetooth | €200 |
| smallBMS | Victron | Extern (minimal) | 4–16 | Relais-gesteuert | Extern | Signal/Relais | €65 |
| Lynx Smart BMS | Victron | Extern (Lynx-System) | 4–48 | 500 A | Intern | VE.Can, Bluetooth | €550 |
| MasterBus BMS | Mastervolt | Extern | 4–16 | Relais-gesteuert | Intern | MasterBus (CAN) | €400 |
| REC Q BMS | REC | Extern | 4–16 | 800 A (MOSFET) | Aktiv (2A) | CAN, RS485 | €350 |
| Batrium WatchMon | Batrium | Extern | 4–48 | Unbegrenzt (Relais) | Aktiv (1A) | WiFi, CAN | €450 |
| JBD/Daly BMS | China | Intern | 4–16 | 100–200 A | Passiv | Bluetooth | €30–€80 |
| 123SmartBMS | 123Electric | Modular | 4–32 | MOSFET-basiert | Aktiv | CAN, Bluetooth | €250 |

**Empfehlung nach Anwendungsfall:**
- Budget-Retrofit (1 Batterie): JBD/Daly (ACHTUNG: Qualität variiert stark!)
- Standard-Marine: Victron VE.Bus BMS v2 oder SmallBMS
- Premium-Langfahrt: Victron Lynx Smart BMS oder REC Q BMS
- Superyacht/Profi: Mastervolt MasterBus oder Custom-Lösung

### 3.8 Zellhersteller und Qualitätsstufen (LiFePO4)

Unabhängig vom Batterie-Markenname werden die eigentlichen Zellen von wenigen Großherstellern produziert:

| Zellhersteller | Herkunft | Typische Modelle | Qualität | Verwendet von |
|---------------|---------|-----------------|----------|---------------|
| CATL | China | 3,2V/280Ah prismatisch | Grade A+++ | Victron, Mastervolt |
| EVE Energy | China | LF280K, LF304 | Grade A+ | Battle Born, RELiON |
| BYD | China | Blade Battery | Grade A+ | BYD Marine (Eigenmarke) |
| CALB | China | CA180, CA200 | Grade A | Diverse Assembler |
| Gotion High-Tech | China | 3,2V/100-200Ah | Grade A | Torqeedo (teilweise) |
| Lishen | China | 3,2V/100-272Ah | Grade A bis B | Budget-Marken |
| REPT | China | 3,2V/280Ah | Grade A | Neuere Marken |

**Qualitätskriterien bei Zellen:**
- Kapazitätsabweichung: Grade A <2%, Grade B 2–5%, Grade C >5%
- Innenwiderstandsstreuung: Grade A <5%, Grade B 5–15%
- Selbstentladung: Grade A <3%/Monat, Grade B 3–8%
- Zyklentests: Grade A = Hersteller-Spezifikation erfüllt, Grade B = leicht unter Spec
- Optische Qualität: Grade A = makellos, Grade B = Kratzer/Dellen (funktional OK)

**WARNUNG:** „Grade B gebraucht aus EV" = NIEMALS für Marine-Anwendung! Unbekannte Zyklenzahl, thermische Historie, mögliche interne Schäden. Sicherheitsrisiko!

---

## 4. Produktlinien und Spezifikationen

### 4.1 Victron Energy

**Hauptsitz:** Almere, Niederlande
**Marktsegment:** Premium Marine/Off-Grid
**Stärke:** Vollständiges Ökosystem (Batterie + Ladegerät + Wechselrichter + Monitoring)

#### 4.1.1 Victron Lithium Smart (LiFePO4)

| Modell | Spannung | Kapazität | Gewicht | BMS | Max. Entlade | Max. Lade | Preis (ca.) |
|--------|----------|-----------|---------|-----|-------------|-----------|-------------|
| Smart 12,8V/100Ah | 12,8 V | 100 Ah | 16 kg | Intern + VE.Bus BMS | 200 A | 100 A | €1.400 |
| Smart 12,8V/150Ah | 12,8 V | 150 Ah | 20 kg | Intern + VE.Bus BMS | 300 A | 150 A | €1.900 |
| Smart 12,8V/200Ah | 12,8 V | 200 Ah | 26 kg | Intern + VE.Bus BMS | 400 A | 200 A | €2.500 |
| Smart 12,8V/330Ah | 12,8 V | 330 Ah | 45 kg | Intern + VE.Bus BMS | 500 A | 200 A | €3.800 |
| Smart 25,6V/100Ah | 25,6 V | 100 Ah | 30 kg | Intern + VE.Bus BMS | 200 A | 100 A | €2.600 |
| Smart 25,6V/200Ah | 25,6 V | 200 Ah | 50 kg | Intern + VE.Bus BMS | 400 A | 200 A | €4.800 |

**Besonderheiten:**
- Bluetooth-Monitoring über VictronConnect App
- Parallelschaltung bis 5 Einheiten (mit VE.Bus BMS v2)
- Integrierter Zell-Balancer
- Lebensdauer: 2.500 Zyklen bei 80% DoD (Herstellergarantie: 5 Jahre)
- Kommunikation: VE.Bus, CAN-Bus, Bluetooth LE
- Heizmatte optional (für Betrieb in kalten Gewässern)

#### 4.1.2 Victron Lithium SuperPack

| Modell | Spannung | Kapazität | Gewicht | BMS | Max. Entlade | Preis (ca.) |
|--------|----------|-----------|---------|-----|-------------|-------------|
| SuperPack 12,8V/60Ah | 12,8 V | 60 Ah | 7,5 kg | Intern (einfach) | 60 A | €650 |
| SuperPack 12,8V/100Ah | 12,8 V | 100 Ah | 12 kg | Intern (einfach) | 100 A | €950 |
| SuperPack 12,8V/200Ah | 12,8 V | 200 Ah | 22 kg | Intern (einfach) | 200 A | €1.700 |

**Besonderheiten:**
- Integriertes BMS ohne externe Komponenten
- Einfacherer Aufbau als Lithium Smart (kein VE.Bus BMS nötig)
- Parallelschaltung bis 4 Einheiten
- Ideal für Retrofit von Blei auf Lithium

#### 4.1.3 Victron AGM

| Modell | Spannung | Kapazität | Gewicht | Zyklen (50% DoD) | Preis (ca.) |
|--------|----------|-----------|---------|-------------------|-------------|
| AGM Deep Cycle 12V/60Ah | 12 V | 60 Ah | 18 kg | 500 | €160 |
| AGM Deep Cycle 12V/90Ah | 12 V | 90 Ah | 26 kg | 500 | €220 |
| AGM Deep Cycle 12V/110Ah | 12 V | 110 Ah | 32 kg | 500 | €270 |
| AGM Deep Cycle 12V/130Ah | 12 V | 130 Ah | 38 kg | 500 | €310 |
| AGM Deep Cycle 12V/165Ah | 12 V | 165 Ah | 47 kg | 500 | €380 |
| AGM Deep Cycle 12V/220Ah | 12 V | 220 Ah | 65 kg | 500 | €490 |
| AGM Super Cycle 12V/100Ah | 12 V | 100 Ah | 29 kg | 1.000 (60% DoD) | €350 |
| AGM Super Cycle 12V/170Ah | 12 V | 170 Ah | 47 kg | 1.000 (60% DoD) | €520 |
| AGM Super Cycle 12V/230Ah | 12 V | 230 Ah | 63 kg | 1.000 (60% DoD) | €680 |

### 4.2 Mastervolt

**Hauptsitz:** Amsterdam, Niederlande
**Marktsegment:** Premium Marine (OEM bei vielen Werften)
**Stärke:** Integrierte Systeme, werftfertige Lösungen

#### 4.2.1 Mastervolt MLI Ultra (LiFePO4)

| Modell | Spannung | Kapazität | Gewicht | BMS | Max. Entlade | Preis (ca.) |
|--------|----------|-----------|---------|-----|-------------|-------------|
| MLI Ultra 12/1250 | 12 V | 100 Ah | 13 kg | MasterBus integriert | 250 A | €1.800 |
| MLI Ultra 12/2750 | 12 V | 220 Ah | 26 kg | MasterBus integriert | 500 A | €3.500 |
| MLI Ultra 12/5000 | 12 V | 400 Ah | 47 kg | MasterBus integriert | 750 A | €5.900 |
| MLI Ultra 24/1250 | 24 V | 50 Ah | 13 kg | MasterBus integriert | 250 A | €1.900 |
| MLI Ultra 24/2750 | 24 V | 110 Ah | 26 kg | MasterBus integriert | 500 A | €3.700 |
| MLI Ultra 24/5500 | 24 V | 220 Ah | 50 kg | MasterBus integriert | 750 A | €6.500 |

**Besonderheiten:**
- MasterBus CAN-Bus Integration (proprietär, aber sehr ausgereift)
- Serienschaltung möglich (24V aus 2× 12V)
- IP65-Schutzklasse
- Integrierte Heizung für Laden bei niedrigen Temperaturen
- 5.000+ Zyklen bei 80% DoD
- Garantie: 5 Jahre / 7.500 Betriebsstunden

#### 4.2.2 Mastervolt MVG (Gel)

| Modell | Spannung | Kapazität | Gewicht | Zyklen (50% DoD) | Preis (ca.) |
|--------|----------|-----------|---------|-------------------|-------------|
| MVG 12/55 | 12 V | 55 Ah | 18 kg | 1.500 | €220 |
| MVG 12/85 | 12 V | 85 Ah | 26 kg | 1.500 | €310 |
| MVG 12/120 | 12 V | 120 Ah | 37 kg | 1.500 | €420 |
| MVG 12/200 | 12 V | 200 Ah | 60 kg | 1.500 | €650 |
| MVG 12/270 | 12 V | 270 Ah | 78 kg | 1.500 | €850 |

**Besonderheiten:**
- Extrem zyklenfest (Sonnenschein-Technologie)
- OEM bei Hallberg-Rassy, Najad, Oyster (historisch)
- Ideal für Solar-/Windladeprofile
- Absorptionsspannung: 14,25 V (strikt einzuhalten)

### 4.3 Exide / Sonnenschein

**Hauptsitz:** Büdingen, Deutschland (Sonnenschein = Marke von Exide)
**Marktsegment:** Industrielle Gel-Technologie, auch Marine

#### 4.3.1 Sonnenschein A500 / A600 (dryfit Gel)

| Modell | Spannung | Kapazität | Gewicht | Zyklen (60% DoD) | Preis (ca.) |
|--------|----------|-----------|---------|-------------------|-------------|
| A512/55 G6 | 12 V | 55 Ah | 18,5 kg | 700 | €240 |
| A512/85 A | 12 V | 85 Ah | 28 kg | 700 | €360 |
| A512/115 A | 12 V | 115 Ah | 38 kg | 700 | €480 |
| A512/140 A | 12 V | 140 Ah | 44 kg | 700 | €560 |
| A512/200 A | 12 V | 200 Ah | 62 kg | 700 | €780 |
| A600 Bloc (6V) | 6 V | 180–520 Ah | 29–80 kg | 1.800 | €350–€900 |

**Besonderheiten:**
- Deutsche Industriequalität
- A600-Serie: 1.800 Zyklen bei 60% DoD (Panzerplatten-Gel)
- Bewährt in Telekommunikation, Medizin, Marine
- 10-Jahres-Standby-Lebensdauer
- Temperaturkompensation: −4 mV/°C/Zelle

### 4.4 Optima (Johnson Controls / Clarios)

**Hauptsitz:** Milwaukee, USA
**Marktsegment:** Premium AGM, Spiralzellen-Technologie

#### 4.4.1 Optima BlueTop (Marine)

| Modell | Spannung | Kapazität | CCA | Gewicht | Typ | Preis (ca.) |
|--------|----------|-----------|-----|---------|-----|-------------|
| BlueTop D31M (Starter) | 12 V | 75 Ah | 900 A | 24 kg | Starter | €280 |
| BlueTop D27M (Dual) | 12 V | 66 Ah | 800 A | 23 kg | Dual Purpose | €260 |
| BlueTop D34M (Dual) | 12 V | 55 Ah | 750 A | 20 kg | Dual Purpose | €240 |
| BlueTop D31M (Deep Cycle) | 12 V | 75 Ah | — | 24 kg | Deep Cycle | €290 |

**Besonderheiten:**
- Spiralzellen-Technologie (SpiralCell™) → extrem vibrationsfest
- 15× vibrationsresistenter als konventionelle AGM
- Ideal für Hochgeschwindigkeits-Motorboote (Planing Hulls)
- ABER: nur moderate Zyklenlebensdauer (300–500 bei 50% DoD)
- Eher Starter/Dual-Purpose als echte Deep-Cycle

### 4.5 Battle Born Batteries

**Hauptsitz:** Reno, Nevada, USA
**Marktsegment:** Consumer-LiFePO4, Retrofit-Markt

#### 4.5.1 Battle Born BB10012 / BB10024

| Modell | Spannung | Kapazität | Gewicht | BMS | Max. Entlade | Preis (ca.) |
|--------|----------|-----------|---------|-----|-------------|-------------|
| BB10012 | 12 V | 100 Ah | 13 kg | Intern | 100 A | €850 |
| BB10024 | 24 V | 50 Ah | 11 kg | Intern | 50 A | €900 |
| BB20012 (GC3) | 12 V | 200 Ah | 28 kg | Intern | 200 A | €1.500 |
| BB5024 (GC2) | 24 V | 50 Ah | 10 kg | Intern | 100 A | €950 |

**Besonderheiten:**
- 3.000–5.000 Zyklen bei 100% DoD
- Internes BMS mit Low-Temperature-Cutoff (0°C)
- Parallelschaltung bis 4 Einheiten (ohne externes BMS)
- 10-Jahre-Garantie
- Populär im US-Marine-Retrofit-Markt
- Bluetooth-Monitoring optional (BB100-BT)

### 4.6 RELiON Batteries

**Hauptsitz:** Charlotte, North Carolina, USA
**Marktsegment:** Premium-LiFePO4, professionelle Marine-Anwendungen

#### 4.6.1 RELiON RB-Serie / Insight-Serie

| Modell | Spannung | Kapazität | Gewicht | BMS | Max. Entlade | Preis (ca.) |
|--------|----------|-----------|---------|-----|-------------|-------------|
| RB100 | 12 V | 100 Ah | 13 kg | Intern | 100 A | €900 |
| RB100-LT (Low Temp) | 12 V | 100 Ah | 14 kg | Intern + Heizung | 100 A | €1.200 |
| RB200 | 12 V | 200 Ah | 24 kg | Intern | 200 A | €1.700 |
| RB300 | 12 V | 300 Ah | 36 kg | Intern | 300 A | €2.500 |
| InSight 48V/30 | 48 V | 30 Ah | 16 kg | Intern (CAN) | 100 A | €1.800 |
| InSight 48V/60 | 48 V | 60 Ah | 30 kg | Intern (CAN) | 200 A | €3.200 |

**Besonderheiten:**
- LT-Serie: Integrierte Heizung, laden ab −20°C möglich
- InSight-Serie: CAN-Bus mit Victron/Mastervolt-Kompatibilität
- 5.000 Zyklen bei 80% DoD
- UL-zertifiziert (UL 1973, UL 9540A)
- IP67-Optionen für Deck-Montage

---

## 5. Hersteller-Datenbank

### 5.1 Victron Energy

| Feld | Information |
|------|-------------|
| Firma | Victron Energy B.V. |
| Hauptsitz | Almere, Niederlande |
| Gründung | 1975 |
| Schwerpunkt | Marine/Off-Grid Energiesysteme |
| Produktpalette | Batterien, Ladegeräte, Wechselrichter, MPPT, Monitoring |
| Marine-Relevanz | ★★★★★ (Industriestandard) |
| Vertrieb DACH | Über Fachhändler und Distributoren |
| Support | Hervorragend (Community + offizieller Support) |
| Garantie | 5 Jahre (Lithium), 2 Jahre (AGM) |
| Monitoring | VictronConnect App, VRM Portal (Cloud), GX-Geräte |
| Kommunikation | VE.Bus, VE.Direct, VE.Can, Bluetooth LE, NMEA 2000 |
| Zertifizierungen | CE, UL, FCC, DNV GL (ausgewählte Produkte) |
| Website | victronenergy.com |

### 5.2 Mastervolt (WHISPER Power Group)

| Feld | Information |
|------|-------------|
| Firma | Mastervolt International B.V. |
| Hauptsitz | Amsterdam, Niederlande |
| Gründung | 1991 |
| Schwerpunkt | Integrierte Marine-Energiesysteme |
| Produktpalette | Batterien, Ladegeräte, Wechselrichter, Generatoren |
| Marine-Relevanz | ★★★★★ (OEM bei Premium-Werften) |
| Vertrieb DACH | Direkt + autorisierte Servicepartner |
| Support | Gut (professionell, aber weniger Community) |
| Garantie | 5 Jahre (MLI Ultra), 2 Jahre (Gel) |
| Monitoring | MasterBus, EasyView Display, SmartRemote App |
| Kommunikation | MasterBus (CAN), NMEA 2000, Modbus |
| Zertifizierungen | CE, Lloyd's, DNV GL, GL |
| Website | mastervolt.com |

### 5.3 Exide Technologies (Sonnenschein)

| Feld | Information |
|------|-------------|
| Firma | Exide Technologies GmbH |
| Hauptsitz | Büdingen, Deutschland |
| Gründung | 1888 (Sonnenschein: 1910) |
| Schwerpunkt | Industrielle Blei-Säure und Gel-Technologie |
| Produktpalette | Gel-Batterien (dryfit), AGM, Nass-Blei |
| Marine-Relevanz | ★★★★☆ (Industriequalität, bewährt) |
| Vertrieb DACH | Großhandel + Fachhandel |
| Support | Gut (technische Dokumentation umfangreich) |
| Garantie | 2 Jahre (Standard), projektspezifisch bis 5 Jahre |
| Kommunikation | Keine eigene Bus-Integration |
| Zertifizierungen | VDE, CE, IEC, DNV GL |
| Website | exide.com |

### 5.4 Optima Batteries (Clarios)

| Feld | Information |
|------|-------------|
| Firma | Clarios (ehem. Johnson Controls) |
| Hauptsitz | Milwaukee, Wisconsin, USA |
| Gründung | Optima seit 1972 |
| Schwerpunkt | Premium AGM, Spiralzellen |
| Produktpalette | BlueTop (Marine), YellowTop (Deep Cycle), RedTop (Starter) |
| Marine-Relevanz | ★★★☆☆ (Nische: Vibrationsbelastung) |
| Vertrieb DACH | Importeure, Online-Handel |
| Support | Begrenzt in Europa |
| Garantie | 3 Jahre (BlueTop) |
| Zertifizierungen | SAE, BCI, CE |
| Website | optimabatteries.com |

### 5.5 Battle Born Batteries

| Feld | Information |
|------|-------------|
| Firma | Dragonfly Energy Holdings (Battle Born Batteries) |
| Hauptsitz | Reno, Nevada, USA |
| Gründung | 2011 |
| Schwerpunkt | Consumer LiFePO4, Retrofit |
| Produktpalette | LiFePO4 12V/24V/48V, Zubehör |
| Marine-Relevanz | ★★★☆☆ (Consumer-Grade, populär in USA) |
| Vertrieb DACH | Online-Importeure, Amazon |
| Support | Gut (US-basiert, Live-Chat) |
| Garantie | 10 Jahre |
| Kommunikation | Bluetooth (optional) |
| Zertifizierungen | UL, FCC, DOT |
| Website | battlebornantteries.com |

### 5.6 RELiON Batteries

| Feld | Information |
|------|-------------|
| Firma | RELiON Battery LLC |
| Hauptsitz | Charlotte, North Carolina, USA |
| Gründung | 2014 |
| Schwerpunkt | Premium LiFePO4 für professionellen Einsatz |
| Produktpalette | LiFePO4 12V/24V/48V, InSight-Serie (CAN-Bus) |
| Marine-Relevanz | ★★★★☆ (Professionell, UL-zertifiziert) |
| Vertrieb DACH | Distributoren, Mastervolt-Händler (teilweise kompatibel) |
| Support | Gut (technischer Telefon-Support, umfangreiche Docs) |
| Garantie | 10 Jahre |
| Kommunikation | CAN-Bus (InSight), Bluetooth (RB-Serie) |
| Zertifizierungen | UL 1973, UL 9540A, UN 38.3, CE |
| Website | relionbattery.com |

### 5.7 Lithium Battery Power (LBP) / Liontron

| Feld | Information |
|------|-------------|
| Firma | Liontron GmbH |
| Hauptsitz | Braunschweig, Deutschland |
| Gründung | 2018 |
| Schwerpunkt | Preis-Leistung LiFePO4 für Marine/Wohnmobil |
| Produktpalette | LiFePO4 12V/24V, Arctic-Serie (Heizung) |
| Marine-Relevanz | ★★★☆☆ (Preis-Leistung, DACH-Support) |
| Vertrieb DACH | Direkt + SVB, Compass24, AWN |
| Support | Deutsch, gut erreichbar |
| Garantie | 5 Jahre |
| Kommunikation | Bluetooth |
| Zertifizierungen | CE, UN 38.3 |
| Website | liontron.com |

### 5.8 Torqeedo / BMW i (Hochvolt-Marine)

| Feld | Information |
|------|-------------|
| Firma | Torqeedo GmbH (DEUTZ AG) |
| Hauptsitz | Gilching bei München, Deutschland |
| Gründung | 2005 |
| Schwerpunkt | Elektrische Bootsantriebe + Hochvolt-Batterien |
| Produktpalette | Power 48-5000 (5 kWh, 48V), Power 24-3500 |
| Marine-Relevanz | ★★★★☆ (Elektroantrieb-Spezialist) |
| Vertrieb DACH | Direkt + Händlernetzwerk |
| Support | Gut (deutscher Hersteller) |
| Garantie | 2 Jahre (erweiterbar) |
| Kommunikation | CAN-Bus, Torqeedo TorqLink |
| Zertifizierungen | CE, DNV GL (Power 48-5000) |
| Website | torqeedo.com |

---

## 6. Fehlerbild-Atlas

### 6.1 Sulfatierung (Blei-Säure/AGM/Gel)

| Feld | Details |
|------|---------|
| **Beschreibung** | Bleisulfat-Kristalle (PbSO₄) lagern sich permanent an den Platten ab und werden irreversibel hart. Die aktive Oberfläche der Platten wird reduziert. |
| **Ursache** | Langfristige Teilladung (<80% SoC), zu langes Stehen im entladenen Zustand, fehlende Absorptionsphase beim Laden, zu niedrige Ladespannung |
| **Symptome** | Schneller Spannungsabfall unter Last, reduzierte Kapazität (nur noch 50–70% der Nennkapazität), erhöhter Innenwiderstand, Ladegerät geht schnell in Float (geringe Stromaufnahme in Absorption) |
| **Visuelle Erkennung** | Bei Nass-Blei: weiße kristalline Ablagerungen auf Platten sichtbar (wenn Zellen geöffnet), Elektrolyt-Verfärbung; AGM/Gel: nur über Messwerte erkennbar |
| **Confidence** | visual_medium (Nass-Blei mit offenen Zellen), measured (Innenwiderstandsmessung) |
| **Schweregrad** | MITTEL bis KRITISCH (je nach Ausmaß) |
| **Reversibilität** | Leichte Sulfatierung: Desulfatierungsladung (Equalization 15,5V, 30 min) bei Nass-Blei möglich. Starke Sulfatierung: irreversibel |
| **Prävention** | Vollständige Ladung mindestens alle 2 Wochen, Absorptionsphase nie abbrechen, Winterlager mit Erhaltungsladegerät |
| **AYDI-Score-Impact** | −20 bis −50 Punkte im Batterie-Modul |

### 6.2 Thermal Runaway (LiFePO4 / alle Lithium)

| Feld | Details |
|------|---------|
| **Beschreibung** | Unkontrollierte exotherme Kettenreaktion im Zellinneren. Temperatur steigt über 150°C, Elektrolyt zersetzt sich, Zelle bläht auf, kann Feuer fangen oder explodieren. |
| **Ursache** | BMS-Versagen bei Überladung, externer Kurzschluss, mechanische Beschädigung (Punktion), Laden unter 0°C (Lithium-Plating → interner Kurzschluss) |
| **Symptome** | Rapider Temperaturanstieg (>60°C Gehäusetemperatur), Aufblähen des Gehäuses, Rauchentwicklung, stechender Geruch (Elektrolyt-Zersetzung), Spannungseinbruch |
| **Visuelle Erkennung** | Aufgeblähtes Gehäuse, Verfärbung (braun/schwarz), Austritt von Elektrolyt/Gas, Schmelzspuren an Anschlüssen |
| **Confidence** | visual_high (eindeutige visuelle Merkmale) |
| **Schweregrad** | KRITISCH — LEBENSGEFAHR |
| **Reversibilität** | KEINE — Zelle/Pack ist zerstört |
| **Prävention** | Hochwertiges BMS mit Temperaturüberwachung, keine mechanische Beschädigung, NIEMALS unter 0°C laden, Absicherung nach Herstellervorgabe, keine Grade-B-Zellen aus unbekannter Quelle |
| **Sofortmaßnahmen** | Raum verlassen, Belüftung maximieren, KEIN Wasser auf Lithium-Brand, CO₂-Löscher oder Löschsand, Feuerwehr (Marine-Brand melden) |
| **AYDI-Score-Impact** | Sofortige Abwertung auf 0. Befund: „Akute Brandgefahr — sofortige Außerbetriebnahme" |

### 6.3 BMS-Abschaltung (LiFePO4)

| Feld | Details |
|------|---------|
| **Beschreibung** | Das Battery Management System trennt die Batterie vom Bordnetz (Lade- und/oder Entladerichtung) aufgrund eines erkannten Schutzparameter-Überschreitens. |
| **Ursache** | Überstrom (>BMS-Limit), Überspannung (>3,65 V/Zelle), Unterspannung (<2,5 V/Zelle), Übertemperatur (>55°C), Untertemperatur beim Laden (<0°C), Zellungleichgewicht (>100 mV Differenz) |
| **Symptome** | Plötzlicher Totalausfall der Bordelektrik, kein Strom messbar an den Klemmen, BMS-LED zeigt Fehler (rot/blinkend), App zeigt Fehlermeldung |
| **Visuelle Erkennung** | Keine äußeren Schäden sichtbar, LED-Status am BMS/Batterie, Display-Fehlermeldung |
| **Confidence** | measured (via BMS-Fehlerspeicher/App) |
| **Schweregrad** | HOCH (Funktionsverlust, aber Schutzmechanismus arbeitet korrekt) |
| **Reversibilität** | Meist selbstreversibel nach Behebung der Ursache (Abkühlen, Entlastung, Nachladen). Manche BMS erfordern manuellen Reset. |
| **Prävention** | Korrekte Systemdimensionierung, Strombegrenzung vor BMS-Limit, Temperaturmanagement, regelmäßige Balancierung, redundantes System (2. Batteriebank) |
| **AYDI-Score-Impact** | −15 Punkte (Schutzfunktion korrekt), −30 wenn wiederholt |

### 6.4 Zellungleichgewicht (Cell Imbalance)

| Feld | Details |
|------|---------|
| **Beschreibung** | Die einzelnen Zellen in einem Serien-Pack driften auseinander — unterschiedliche Spannungen, Kapazitäten oder Innenwiderstände. |
| **Ursache** | Unzureichende Balancierung, unterschiedliche Temperaturverteilung, eine schwache Zelle im Pack, BMS-Balancer zu langsam (passiver Balancer: 50–100 mA), Mischung von alten/neuen Zellen |
| **Symptome** | BMS-Abschaltung bei scheinbar halbvoller Batterie (eine Zelle erreicht Limit zuerst), reduzierte nutzbare Kapazität, ungleiche Zellenspannungen (>30 mV Differenz) |
| **Visuelle Erkennung** | Nicht sichtbar — nur über BMS-Zelldaten oder Einzelzellmessung |
| **Confidence** | measured (BMS-Zellenspannungs-Log) |
| **Schweregrad** | MITTEL (reduzierte Leistung) bis HOCH (BMS-Abschaltung) |
| **Reversibilität** | Leichtes Ungleichgewicht: Top-Balancing (Vollladung + lange Absorptionsphase). Starkes Ungleichgewicht: Einzelzellen-Ladung nötig. Defekte Zelle: Austausch. |
| **Prävention** | Regelmäßige Vollladung (alle 2–4 Wochen) für Balancierung, aktives BMS (>1A Balancerstrom), gleiche Temperatur für alle Zellen, keine gemischten Zellen |
| **AYDI-Score-Impact** | −10 bis −25 Punkte je nach Schwere |

### 6.5 Gehäuse-Aufblähen (Swelling)

| Feld | Details |
|------|---------|
| **Beschreibung** | Das Batteriegehäuse verformt sich sichtbar nach außen durch internen Gasdruckaufbau. |
| **Ursache** | Blei-Säure: Überladung → Elektrolyse → Wasserstoff/Sauerstoff-Entwicklung bei geschlossener Batterie. LiFePO4: Zellinterner Defekt, Überladung, Elektrolyt-Zersetzung, beginnender Thermal Runaway |
| **Symptome** | Sichtbare Gehäusedeformation, Batterie „wackelt" auf ebenem Untergrund, bei Blei: Säureaustritt möglich, bei LiFePO4: Elektrolytgeruch |
| **Visuelle Erkennung** | Deutlich sichtbar — Gehäuse gewölbt, Ecken aufgespreizt, Deckel hebt sich |
| **Confidence** | visual_high (eindeutig erkennbar auf Fotos) |
| **Schweregrad** | KRITISCH (Blei: Kurzschlussgefahr, Säure; LiFePO4: Thermal Runaway Vorstufe) |
| **Reversibilität** | KEINE — Batterie sofort außer Betrieb nehmen |
| **Prävention** | Korrekte Ladeparameter, Temperaturüberwachung, ventilierter Einbauort, BMS mit Überladeschutz, keine billigen No-Name-Produkte |
| **AYDI-Score-Impact** | Sofortige Abwertung auf 0. Befund: „Batterie sofort ersetzen — Gefahrenpotential" |

### 6.6 Kapazitätsverlust (Capacity Fade)

| Feld | Details |
|------|---------|
| **Beschreibung** | Schleichende, permanente Reduktion der nutzbaren Kapazität über die Lebensdauer. Bei Blei-Säure typisch 5–10% pro Jahr, bei LiFePO4 1–3% pro Jahr. |
| **Ursache** | Normaler Alterungsprozess (kalendarisch + zyklisch), beschleunigt durch: hohe Temperaturen, hohe DoD, hohe Lade-/Entladeströme, Sulfatierung (Blei), SEI-Schichtwachstum (Lithium) |
| **Symptome** | Kürzere Betriebszeiten bei gleicher Nutzung, Ladezyklus wird kürzer (schneller „voll"), Spannung fällt schneller unter Last, SoC-Anzeige ungenau |
| **Visuelle Erkennung** | Nicht sichtbar — nur über Kapazitätstest messbar |
| **Confidence** | measured (Kapazitätstest mit definiertem Entladestrom) |
| **Schweregrad** | NIEDRIG bis MITTEL (schleichend, planbar) |
| **Reversibilität** | KEINE — irreversibler chemischer Alterungsprozess |
| **Prävention** | Temperaturmanagement, moderate DoD (<50% Blei, <80% LiFePO4), regelmäßige Vollladung, korrekte Ladeparameter |
| **End-of-Life-Kriterium** | Batterie bei <80% der Nennkapazität als „verbraucht" klassifizieren (ISO-Standard-Definition) |
| **AYDI-Score-Impact** | Proportional zum Kapazitätsverlust: −2 Punkte pro 5% unter 100% |

### 6.7 Korrosion an Batteriepolen

| Feld | Details |
|------|---------|
| **Beschreibung** | Weiß-grüne Ablagerungen an Batteriepolen und Kabelschuhen durch elektrochemische Korrosion im Salzwassermilieu. |
| **Ursache** | Salzwasseraerosol, fehlender Korrosionsschutz, bimetallische Kontakte (Kupfer auf Blei), Säuredämpfe (Nass-Blei), undichte Polabdichtung |
| **Symptome** | Erhöhter Übergangswiderstand, Spannungsabfall an den Klemmen, intermittierender Kontaktverlust, Erwärmung der Polverbindung |
| **Visuelle Erkennung** | Weiße (Bleisulfat), grüne (Kupferoxid) oder blaue (Kupfersulfat) Ablagerungen |
| **Confidence** | visual_high (eindeutig sichtbar) |
| **Schweregrad** | NIEDRIG bis MITTEL |
| **Reversibilität** | Ja — mechanische Reinigung, Polfett/Kontaktspray, neue Kabelschuhe wenn stark korrodiert |
| **Prävention** | Polfett (Vaseline oder technisches Polfett), Kabelschuhe mit Schrumpfschlauch abdichten, Batterieraum trocken halten |
| **AYDI-Score-Impact** | −5 bis −15 Punkte |

### 6.8 Elektrolytverlust (Nass-Blei)

| Feld | Details |
|------|---------|
| **Beschreibung** | Elektrolytstand sinkt unter die Plattenoberkante, freiliegende Platten sulfatieren irreversibel und werden mechanisch beschädigt. |
| **Ursache** | Normaler Wasserverbrauch durch Gasung (Überladung), fehlende Wartung (kein Wasser nachgefüllt), gekippte Aufstellung, Gehäuseriss |
| **Symptome** | Kapazitätsverlust, einzelne Zellen „kochen" beim Laden, ungleichmäßige Zellenspannungen, Säurespritzer am Gehäuse |
| **Visuelle Erkennung** | Platten oberhalb des Elektrolytspiegels sichtbar (bei transparentem Gehäuse oder offenen Zellen), Säurespuren am Gehäuse |
| **Confidence** | visual_medium bis visual_high |
| **Schweregrad** | HOCH wenn Platten freiliegen |
| **Reversibilität** | Teilweise — Wasser nachfüllen, wenn Platten noch nicht dauerhaft geschädigt. Bei sichtbarer Plattenkorrosion: irreversibel |
| **Prävention** | Regelmäßige Kontrolle alle 4–8 Wochen, nur destilliertes Wasser verwenden, Ladeparameter prüfen (Überladung vermeiden) |
| **AYDI-Score-Impact** | −15 bis −35 Punkte |

### 6.9 Kurzschluss (intern)

| Feld | Details |
|------|---------|
| **Beschreibung** | Interner Kontakt zwischen positiver und negativer Platte durch Separator-Versagen, Dendritenbildung oder mechanische Verformung. |
| **Ursache** | Vibrationsschäden (Separator-Abrieb), Überladung (Dendritenwachstum bei Blei), Tiefentladung (Kupfer-Auflösung bei LiFePO4), Fertigungsfehler, mechanischer Schock |
| **Symptome** | Einzelne Zelle mit 0V, Batterie wird heiß ohne Last, Gesamtspannung um 2V reduziert (Blei) bzw. 3,2V (LiFePO4), extrem hoher Selbstentladestrom |
| **Visuelle Erkennung** | Nicht direkt sichtbar, aber: Gehäuseverfärbung (Hitze), geschmolzene Polanschlüsse |
| **Confidence** | measured (Zellenspannungsmessung) |
| **Schweregrad** | KRITISCH — Brandgefahr |
| **Reversibilität** | KEINE — Batterie sofort ersetzen |
| **Prävention** | Vibrationsdämpfung, korrekte Ladeparameter, keine Tiefentladung, hochwertige Zellen |
| **AYDI-Score-Impact** | Sofortige Abwertung auf 0. Sicherheitsbefund. |

### 6.10 BMS-Kommunikationsfehler

| Feld | Details |
|------|---------|
| **Beschreibung** | BMS meldet keine Daten mehr an das Monitoring-System (VRM, MasterBus, etc.) oder zeigt fehlerhafte Werte. |
| **Ursache** | Kabelbruch (CAN-Bus/VE.Bus), EMV-Störung (Motorstart, Radar), BMS-Firmware-Fehler, Feuchtigkeit an Steckern, Terminierung fehlt |
| **Symptome** | Keine Batterie-Daten auf Display/App, „Lost Communication" Alarm, Ladegerät wechselt in Safe-Mode (niedrige Spannung), inkonsistente Anzeigen |
| **Visuelle Erkennung** | Nicht direkt sichtbar (Kabel und Stecker prüfen) |
| **Confidence** | measured (Systemlog, Alarm-Historie) |
| **Schweregrad** | MITTEL (Monitoring-Verlust) bis HOCH (Ladegerät im Safe-Mode = Unterladung) |
| **Reversibilität** | Ja — Kabel prüfen, Stecker reinigen/tauschen, Firmware-Update, CAN-Terminierung prüfen |
| **Prävention** | Wasserdichte Stecker (IP67), geschirmte Kabel für CAN-Bus, korrekte Terminierung (120Ω), EMV-Ferrite, regelmäßige Firmware-Updates |
| **AYDI-Score-Impact** | −10 bis −20 Punkte |

### 6.11 Überladung (Blei-Säure)

| Feld | Details |
|------|---------|
| **Beschreibung** | Batterie wird dauerhaft mit zu hoher Spannung oder zu langem Ladestrom beaufschlagt, was zur Elektrolyse und Gasbildung führt. |
| **Ursache** | Defekter Laderegler, falsch eingestellte Absorptionsspannung, fehlende Temperaturkompensation bei Hitze, Gleichzeitiger Betrieb mehrerer Ladequellen ohne Koordination |
| **Symptome** | Starke Gasung (Blubbern), Wärmeentwicklung, Wasserverbrauch (Nass-Blei), Aufblähen (AGM/Gel), Säuregeruch, Korrosion an Gittern (positives Gitterwachstum) |
| **Visuelle Erkennung** | Säure-/Wasserflecken um Batterie, Gehäuseverformung (AGM/Gel), Korrosion an positiven Polen verstärkt |
| **Confidence** | visual_medium, measured (Ladelog-Analyse) |
| **Schweregrad** | HOCH — verkürzt Lebensdauer drastisch, Knallgasgefahr |
| **Reversibilität** | Teilweise — Wasserverlust nachfüllbar (Nass-Blei), aber Gitterkorrosion irreversibel |
| **Prävention** | Ladegerät mit Temperaturkompensation, korrekte Parameter pro Batterietyp, regelmäßige Spannungskontrolle, Ladeprioritäts-Management bei mehreren Quellen |
| **AYDI-Score-Impact** | −20 bis −40 Punkte |

### 6.12 Tiefentladung (Deep Discharge)

| Feld | Details |
|------|---------|
| **Beschreibung** | Batterie wird unter die empfohlene Mindestspannung entladen (Blei: <11,5V/12V-System; LiFePO4: <10V/12V-Pack). |
| **Ursache** | Vergessene Verbraucher (Bilgenpumpe, Kühlschrank), fehlendes Low-Voltage-Disconnect, defekter Batteriemonitor, Leckstrom (Kriechstrom über feuchte Verteilung) |
| **Symptome** | Blei: massive Sulfatierung, irreversibler Kapazitätsverlust, einzelne Zellen können umpolen. LiFePO4: BMS-Abschaltung (Schutz), bei <2V/Zelle: Kupfer-Auflösung (irreversibel) |
| **Visuelle Erkennung** | Nicht direkt sichtbar |
| **Confidence** | measured (Spannungslog, BMS-Fehlerspeicher) |
| **Schweregrad** | HOCH (Blei: oft irreversibel) bis MITTEL (LiFePO4: BMS schützt meist rechtzeitig) |
| **Reversibilität** | Blei: Leichte Fälle mit Desulfatierungsladen, schwere Fälle irreversibel. LiFePO4: Wenn BMS rechtzeitig abschaltet, kein Schaden. |
| **Prävention** | Low-Voltage-Disconnect (LVD) bei 11,8V (Blei) bzw. BMS-intern (LiFePO4), Batteriemonitor mit Alarm, automatische Verbraucherabschaltung |
| **AYDI-Score-Impact** | −15 bis −40 Punkte je nach Schaden |

### 6.13 Verpolung (Reverse Polarity)

| Feld | Details |
|------|---------|
| **Beschreibung** | Batterie wird mit vertauschter Polarität angeschlossen (+/− verwechselt). |
| **Ursache** | Installationsfehler, unmarkierte Kabel, fehlende Farbcodierung, Arbeit bei schlechtem Licht |
| **Symptome** | Sofortiger Kurzschluss über angeschlossene Elektronik, Sicherung löst aus (hoffentlich!), Elektronik-Zerstörung (Ladegerät, Wechselrichter, BMS), Funkenbildung bei Anschluss |
| **Visuelle Erkennung** | Geschmolzene Sicherungen, verbrannte Kabelenden, beschädigte Stecker |
| **Confidence** | measured (Spannungsmessung zeigt negative Spannung am Verbraucher) |
| **Schweregrad** | KRITISCH — kann gesamte Bordelektronik zerstören |
| **Reversibilität** | Batterie: meist unbeschädigt. Elektronik: oft irreversibel zerstört |
| **Prävention** | Farbcodierung (Rot = Plus, Schwarz = Minus), Polklemmen mit unterschiedlichen Durchmessern, Verpolungsschutz-Diode an empfindlicher Elektronik, bei Arbeiten immer Multimeter zur Kontrolle |
| **AYDI-Score-Impact** | −30 Punkte (Installationsqualität) |

### 6.14 Ladegerät-Fehlanpassung (Charging Mismatch)

| Feld | Details |
|------|---------|
| **Beschreibung** | Ladeprofil des Ladegeräts passt nicht zur Batteriechemie (z.B. Blei-Profil für Gel, Standard-Profil für LiFePO4). |
| **Ursache** | Falsches Profil am Ladegerät eingestellt, Ladegerät ohne Profilwahl (nur feste Spannung), Batterietausch ohne Ladegerät-Anpassung |
| **Symptome** | Gel: Gasung bei >14,4V, Kapazitätsverlust. AGM: Unterladung bei zu niedriger Absorptionsspannung. LiFePO4: Equalization zerstört Zellen. |
| **Visuelle Erkennung** | Indirekt: Batteriegehäuse-Verformung (Gel bei Überladung), Säurespuren |
| **Confidence** | measured (Ladespannungs-Monitoring) |
| **Schweregrad** | HOCH — häufigste vermeidbare Schadensursache |
| **Reversibilität** | Frühzeitig erkannt: ja (Ladeprofil korrigieren). Spät erkannt: irreversible Batterieschädigung |
| **Prävention** | Ladeprofil bei jedem Batterietausch verifizieren, Ladegerät-Einstellung dokumentieren, Aufkleber am Batteriekasten „Typ: ___" |
| **AYDI-Score-Impact** | −25 bis −40 Punkte |

### 6.15 Kriechstrom (Parasitic Drain)

| Feld | Details |
|------|---------|
| **Beschreibung** | Unerwarteter Stromverbrauch bei scheinbar ausgeschaltetem System. Entlädt Batterie im Hafen/Winterlager. |
| **Ursache** | Standby-Verbrauch von Elektronik (CO-Melder, AIS, Stereo, Bilgenpumpen-Controller), feuchte Verteilung (Leckstrom über PCB), defekte Isolierung, BMS-Ruhestrom |
| **Symptome** | Batterie nach wenigen Tagen/Wochen leer, obwohl keine Verbraucher aktiv |
| **Visuelle Erkennung** | Nicht sichtbar — Amperemeter in Hauptleitung erforderlich |
| **Confidence** | measured (Strommessung im Aus-Zustand) |
| **Schweregrad** | NIEDRIG bis MITTEL (je nach Strom und Batteriealter) |
| **Reversibilität** | Ja — Ursache identifizieren und beheben |
| **Messmethode** | Amperemeter (Bereich mA!) in Serie mit Batterie-Minus. Normal: <30 mA (12V-System). Problem: >50 mA. Kritisch: >200 mA. |
| **Prävention** | Master-Trennschalter, Standby-Verbrauch jedes Geräts kennen, bei Winterlager: alle Sicherungen ziehen |
| **AYDI-Score-Impact** | −10 bis −20 Punkte |

### 6.16 Vibrationsschaden

| Feld | Details |
|------|---------|
| **Beschreibung** | Mechanische Beschädigung durch dauerhafte Vibration im Boots-Betrieb (Motor, Seegang, Wellenanlage). |
| **Ursache** | Unzureichende Befestigung, kein vibrationsdämpfendes Material, Hochgeschwindigkeits-Motorboote (Planing Hulls), Batterieposition nahe Motor/Antrieb |
| **Symptome** | Blei: Plattenmaterial bröckelt, interner Kurzschluss. AGM: Separator löst sich. LiFePO4: Zellenverbindungen lockern sich, BMS-Stecker lösen sich. |
| **Visuelle Erkennung** | Lose Batterie im Kasten, verschobene Halterungen, lockere Pole, Risse am Gehäuse |
| **Confidence** | visual_medium (Befestigung beurteilbar), measured (Innenwiderstand) |
| **Schweregrad** | MITTEL bis HOCH (interner Kurzschluss möglich) |
| **Reversibilität** | Äußere Befestigung: ja. Innere Schäden: nein |
| **Prävention** | Vibrationsfeste Montage (Spanngurte + Gummilager), Marine-Grade-Batterien (vibrationstested), Optima SpiralCell für extreme Vibrationen |
| **AYDI-Score-Impact** | −10 bis −25 Punkte |

---

## 7. Troubleshooting-Entscheidungsbäume

### 7.1 Batterie lädt nicht (Ladestrom = 0)

```
START: Ladestrom = 0, Batterie wird nicht geladen
│
├─ Ladegerät eingeschaltet und mit Landstrom verbunden?
│   ├─ NEIN → Landstrom prüfen, Sicherung, Fehlerstromschutzschalter
│   └─ JA →
│       ├─ LED/Display am Ladegerät zeigt Fehler?
│       │   ├─ JA → Fehlermeldung notieren, Handbuch konsultieren
│       │   │   ├─ "Reverse Polarity" → Verkabelung prüfen (+/− vertauscht?)
│       │   │   ├─ "Battery Voltage High" → Batterie ist bereits voll ODER
│       │   │   │   defektes BMS meldet falsche Spannung → Ruhespannung messen
│       │   │   ├─ "Battery Voltage Low" → Tiefentladung, manche Ladegeräte
│       │   │   │   laden nicht unter 8V → Boost/Recovery-Modus aktivieren
│       │   │   └─ "Temperature" → Batterie oder Ladegerät zu heiß/kalt
│       │   └─ NEIN (Ladegerät scheint normal, aber kein Strom) →
│       │       ├─ Spannung an Batteriepolen messen (mit Multimeter)
│       │       │   ├─ >14,4V → Batterie ist voll, Float-Modus korrekt
│       │       │   ├─ 12,0–14,4V → Kabelverbindung prüfen (Widerstand,
│       │       │   │   lose Klemmen, Sicherung zwischen Ladegerät und Batterie)
│       │       │   └─ <12,0V → Batterie tiefentladen
│       │       │       ├─ LiFePO4: BMS hat abgeschaltet → 
│       │       │       │   Ladespannung kurz anlegen (BMS „aufwecken")
│       │       │       └─ Blei-Säure: Recovery-Laden versuchen,
│       │       │           wenn <10,5V → Batterie wahrscheinlich defekt
│       │       └─ Victron/Mastervolt-System: 
│       │           VE.Bus BMS hat Lade-Eingang gesperrt?
│       │           → BMS-Fehlerlog prüfen (App/Display)
│       └─ LiFePO4-spezifisch:
│           ├─ Temperatur <0°C? → BMS sperrt Laden korrekt. Heizung aktivieren.
│           ├─ Zellspannungs-Differenz >100mV? → BMS sperrt. Balancierung nötig.
│           └─ BMS-LED aus/nicht erreichbar? → BMS defekt, Servicepartner.
│
ERGEBNIS: Ursache identifiziert → Maßnahme einleiten
```

### 7.2 Batterie entlädt sich schnell (hohe Selbstentladung)

```
START: Batterie verliert deutlich Ladung ohne offensichtlichen Verbrauch
│
├─ Alle Verbraucher tatsächlich ausgeschaltet?
│   ├─ NEIN → Kriechstrommessung: Amperemeter in Hauptleitung
│   │   ├─ >50 mA (12V-System) → Verbraucher identifizieren
│   │   │   ├─ Sicherungen einzeln ziehen → Stromreduktion bei welcher?
│   │   │   ├─ Häufige Übeltäter: CO-Melder, Bilgenpumpen-Controller,
│   │   │   │   Stereoanlage (Standby), AIS-Transponder, GPS
│   │   │   └─ Feuchtigkeit auf Verteilung? → Kriechstrom über PCB
│   │   └─ <50 mA → Normal für BMS + Monitoring
│   └─ JA →
│       ├─ Batterie >3 Jahre alt (Blei) oder >8 Jahre (LiFePO4)?
│       │   ├─ JA → Kapazitätstest durchführen
│       │   │   ├─ <80% Nennkapazität → End-of-Life, Austausch empfohlen
│       │   │   └─ >80% → Anderes Problem
│       │   └─ NEIN →
│       │       ├─ Blei-Säure:
│       │       │   ├─ Zellenspannungen messen (einzeln oder Gesamtspannung/6)
│       │       │   ├─ Deutlich unterschiedlich? → Defekte Zelle (interner KS)
│       │       │   └─ Gleichmäßig niedrig? → Sulfatierung (Desulfatierung versuchen)
│       │       └─ LiFePO4:
│       │           ├─ BMS-Ruhestrom messen: 5–20 mA = normal, >50 mA = BMS-Defekt
│       │           ├─ Zellenspannungen gleich? 
│       │           │   ├─ JA + alle niedrig → Externer Verbraucher nicht gefunden
│       │           │   └─ NEIN → Zellungleichgewicht → Balancierung
│       │           └─ Wurde Batterie kürzlich unter 0°C geladen?
│       │               → Lithium-Plating möglich (irreversibel)
│
ERGEBNIS: Verbraucher gefunden / Batterie-EOL / Defekt identifiziert
```

### 7.3 BMS schaltet ab (LiFePO4-Totalausfall)

```
START: LiFePO4-Batterie hat abgeschaltet, keine Ausgangsspannung
│
├─ BMS-Status-LED vorhanden?
│   ├─ LED rot blinkend → Fehlerzustand
│   │   ├─ Bluetooth/App verfügbar?
│   │   │   ├─ JA → Fehlermeldung auslesen
│   │   │   │   ├─ "Over Current" → Zu hoher Verbraucherstrom
│   │   │   │   │   → Verbraucher reduzieren, Absicherung prüfen
│   │   │   │   ├─ "Under Voltage" → Tiefentladung
│   │   │   │   │   → Ladegerät anschließen, ggf. BMS-Aufweck-Prozedur
│   │   │   │   ├─ "Over Voltage" → Ladespannung zu hoch
│   │   │   │   │   → Ladegerät-Einstellung prüfen (max. 14,4–14,6V)
│   │   │   │   ├─ "Over Temperature" → >55°C
│   │   │   │   │   → Kühlung verbessern, Last reduzieren
│   │   │   │   ├─ "Under Temperature" → Ladeversuch bei <0°C
│   │   │   │   │   → Batterie aufwärmen (>5°C), dann erneut laden
│   │   │   │   └─ "Cell Imbalance" → Δ >100–200 mV
│   │   │   │       → Top-Balancing: Vollladung mit reduziertem Strom (C/10)
│   │   │   └─ NEIN →
│   │   │       ├─ Gehäuse heiß (>50°C)?
│   │   │       │   ├─ JA → SOFORT isolieren! Thermal Runaway möglich!
│   │   │       │   │   → Raum verlassen, Lüftung auf, KEIN Wasser
│   │   │       │   └─ NEIN → Standard-Schutzabschaltung
│   │   │       └─ Reset versuchen: Ladegerät anschließen (Aufweck-Puls)
│   │   │           ├─ BMS reagiert → Problem war temporär, Ursache suchen
│   │   │           └─ BMS reagiert nicht → BMS defekt, Servicepartner
│   ├─ LED grün/aus → BMS kommuniziert nicht
│   │   └─ Spannung direkt an Zellen messen (VORSICHT, Fachperson!)
│   │       ├─ Zellspannungen normal (3,0–3,4V) → BMS-Elektronik defekt
│   │       └─ Eine oder mehrere Zellen <2,5V → Tiefentladung oder Zelldefekt
│   └─ Keine LED vorhanden → Externe Diagnose erforderlich
│
ERGEBNIS: Temporärer Schutz / BMS-Defekt / Zelldefekt / Thermal Event
```

### 7.4 Reduzierte Kapazität (Batterie „hält nicht mehr")

```
START: Nutzer bemerkt kürzere Betriebszeiten als gewohnt
│
├─ Schritt 1: Verbrauch gestiegen?
│   ├─ Neue Verbraucher installiert? → Energiebilanz neu berechnen
│   ├─ Saison gewechselt? → Kälte reduziert Kapazität (s. Temperaturkurve)
│   └─ Nutzungsmuster geändert? → Mehr Verbraucher gleichzeitig?
│
├─ Schritt 2: Wird Batterie noch vollständig geladen?
│   ├─ Absorptionsphase wird erreicht? (Ladegerät-Anzeige)
│   │   ├─ NEIN → Ladezeit zu kurz, Landstrom-Unterbrechung, Solar zu wenig
│   │   └─ JA → Absorptionszeit ausreichend? (mind. 1h bei Blei, 15min LiFePO4)
│   ├─ Ladespannung korrekt? (Multimeter an Batterie beim Laden)
│   │   ├─ Zu niedrig (<14,2V Blei) → Ladegerät-Einstellung prüfen
│   │   └─ Korrekt → Weiter
│   └─ Bei mehreren Ladequellen: Alle koordiniert?
│
├─ Schritt 3: Kapazitätstest durchführen
│   ├─ Batterie vollständig laden (24h Ruhe danach)
│   ├─ Definierte Last anschließen (z.B. 5A = C/20)
│   ├─ Zeit messen bis Entladeschlussspannung (10,5V Blei, 10,0V LiFePO4)
│   ├─ Kapazität = Strom × Zeit
│   │   ├─ >90% Nennkapazität → Batterie in Ordnung, Problem liegt anderswo
│   │   ├─ 80–90% → Beginnende Alterung, noch im Toleranzbereich
│   │   ├─ 60–80% → Deutliche Alterung, Austausch planen
│   │   └─ <60% → Batterie am End-of-Life, Austausch erforderlich
│   └─ Ergebnis dokumentieren für Trend-Analyse
│
├─ Schritt 4: Innenwiderstandsmessung
│   ├─ Mit Batterietester (z.B. Midtronics, Hioki)
│   ├─ Vergleich mit Neuwert (Datenblatt)
│   │   ├─ <150% Neuwert → Normal
│   │   ├─ 150–200% → Deutliche Alterung
│   │   └─ >200% → Batterie defekt/sulfatiert
│   └─ LiFePO4: Auch Einzelzellen-Ri prüfen (Ungleichgewicht?)
│
ERGEBNIS: Verbrauch zu hoch / Ladung unvollständig / Batterie-EOL / Defekt
```

### 7.5 Batterie wird heiß (Übertemperatur)

```
START: Batterie fühlt sich ungewöhnlich warm/heiß an (>45°C Gehäuse)
│
├─ SOFORT: Wie heiß?
│   ├─ >60°C (Hand kann nicht >3s auflegen) → GEFAHR!
│   │   ├─ LiFePO4: Thermal Runaway möglich!
│   │   │   → Last sofort trennen (Hauptschalter)
│   │   │   → Raum belüften
│   │   │   → Beobachten: Rauch/Geruch/Aufblähen?
│   │   │       ├─ JA → Raum verlassen, Feuerlöscher bereithalten,
│   │   │       │   ggf. Feuerwehr/Küstenwache
│   │   │       └─ NEIN → Abkühlen lassen (ohne Wasser!), dann Diagnose
│   │   └─ Blei-Säure: Interner Kurzschluss oder Überladung
│   │       → Ladegerät sofort trennen
│   │       → Belüftung sicherstellen (Knallgas-Gefahr!)
│   │       → Batterie nach Abkühlung prüfen/ersetzen
│   └─ 45–60°C (warm, aber noch anfassbar) →
│       ├─ Wird gerade geladen?
│       │   ├─ JA → Ladestrom prüfen
│       │   │   ├─ Ladestrom zu hoch? (>C/5 Blei, >C/3 AGM, >1C LiFePO4)
│       │   │   │   → Ladestrom reduzieren
│       │   │   ├─ Absorptionsspannung zu hoch? → Ladegerät-Einstellung
│       │   │   └─ Normal → Umgebungstemperatur? (Maschinenraum >40°C?)
│       │   │       → Batterie-Standort verlegen oder Belüftung verbessern
│       │   └─ NEIN (Entladung) →
│       │       ├─ Sehr hoher Entladestrom? (Wechselrichter, Ankerwinde)
│       │       │   ├─ Erwärmung nur während Hochlast = normal
│       │       │   └─ Erwärmung bei Niedriglast = Problem
│       │       ├─ Innenwiderstand gestiegen? → Batterie gealtert
│       │       │   → Erwärmung P = I² × Ri
│       │       └─ Einzelne Zelle deutlich heißer?
│       │           → Interner Defekt in dieser Zelle → Batterie ersetzen
│       │
│       └─ Umgebungstemperatur berücksichtigen:
│           ├─ Maschinenraum >50°C → Batterie umplatzieren!
│           ├─ Sonneneinstrahlung auf Batteriekasten → Isolation/Beschattung
│           └─ Keine Belüftung → Lüftungsschlitze/Ventilator nachrüsten
│
ERGEBNIS: Normalbetrieb / Standort-Problem / Konfigurationsfehler / Defekt / GEFAHR
```

---

## 8. FAQ — Häufige Fragen

### 8.1 Allgemeine Fragen

**F1: Kann ich eine Starterbatterie als Versorgungsbatterie verwenden?**
Nein. Starterbatterien haben dünne Platten für hohe Kurzzeit-Ströme. Zyklische Entladung (auch nur 30% DoD) zerstört die Platten innerhalb weniger Monate. Immer dedizierte Deep-Cycle-Batterie für die Versorgung verwenden.

**F2: Wie viele Jahre hält eine Bootsbatterie?**
- Nass-Blei (Versorgung): 3–5 Jahre bei guter Wartung
- AGM Deep Cycle: 4–7 Jahre
- Gel: 6–10 Jahre
- LiFePO4: 8–15 Jahre (zyklenabhängig, nicht kalendarisch limitiert)
- Entscheidend: korrekte Ladung und Vermeidung von Tiefentladung

**F3: Lohnt sich der Umstieg von Blei auf Lithium?**
Kosten-Nutzen-Analyse:
- Blei 200 Ah (nutzbar 100 Ah): ~€400, Lebensdauer 4 Jahre → €100/Jahr
- LiFePO4 100 Ah (nutzbar 80 Ah): ~€900, Lebensdauer 10 Jahre → €90/Jahr
- Plus: 50% Gewichtsersparnis, schnelleres Laden, kein Peukert-Effekt
- Fazit: Lohnt ab >50 Seetagen/Jahr oder wenn Gewicht/Platz kritisch

**F4: Darf ich verschiedene Batterietypen mischen?**
Grundregel: NEIN. Niemals AGM mit Gel, Blei mit Lithium oder neue mit alten Batterien parallel schalten. Unterschiedliche Innenwiderstände und Ladekurven führen zu ungleichmäßiger Strom-/Spannungsverteilung und vorzeitigem Ausfall.
Ausnahme: Getrennte Batteriekreise (z.B. Starter = AGM, Versorgung = LiFePO4) mit Trenndiode/Trennrelais.

**F5: Was bedeutet „Deep Cycle" wirklich?**
Deep Cycle = konstruiert für regelmäßige Entladung auf 50%+ DoD mit nachfolgender Vollladung. Konstruktionsmerkmale: dickere Platten, robustere Gitter, höhere aktive Masse. Nicht jede als „Deep Cycle" vermarktete Batterie erfüllt diesen Anspruch — Zyklenlebensdauer im Datenblatt prüfen (>500 bei 50% DoD = echte Deep Cycle).

### 8.2 Laden und Ladegeräte

**F6: Kann mein altes Blei-Ladegerät LiFePO4 laden?**
Kommt drauf an: Wenn das Ladegerät eine fixe Absorptionsspannung von 14,2–14,4V hat und keinen „Equalization"-Modus automatisch startet, ist es bedingt nutzbar. ABER: Kein Float nötig (schadet langfristig), kein Temperaturkompensations-Sensor anschließen (verfälscht Spannung), und das BMS muss die Batterie schützen. Empfehlung: Immer ein Lithium-kompatibles Ladegerät verwenden.

**F7: Warum lädt meine Batterie im Hafen nicht auf 100%?**
Häufigste Ursachen:
1. Absorptionszeit zu kurz eingestellt (mind. 2h bei Blei, 30 min bei LiFePO4)
2. Ladestrom zu gering (Ladegerät zu klein dimensioniert)
3. Verbraucher laufen während des Ladens (Kühlschrank, Standby-Geräte)
4. Spannungsabfall im Kabel zwischen Ladegerät und Batterie (>0,3V = zu viel)
5. Defekter Temperatursensor meldet zu hohe Temperatur → Ladegerät reduziert

**F8: Wie stelle ich die Lichtmaschine auf LiFePO4 ein?**
Eine Standard-Lichtmaschine (14,2–14,4V, interner Regler) kann LiFePO4 laden, ABER:
- Problem: LiFePO4 hat extrem niedrigen Innenwiderstand → Lichtmaschine liefert Volllast bis die Batterie fast voll ist → Überhitzung der Lichtmaschine möglich
- Lösung 1: Externer Laderegler (z.B. Victron Buck-Boost, Sterling B2B)
- Lösung 2: Strombegrenzender DC-DC-Ladebooster
- Lösung 3: Victron Orion-Tr Smart (begrenzt Strom und Spannung)
- NIEMALS direkt ohne Absicherung/Begrenzung anschließen

**F9: Was ist „Equalization" und brauche ich das?**
Equalization (Ausgleichsladung) = kontrollierte Überladung bei 15,5V für 30–60 Minuten. Nur für Nass-Blei-Batterien! Zweck: Sulfatierung reduzieren, Elektrolyt durchmischen.
- AGM: NIEMALS Equalization (zerstört Separator)
- Gel: NIEMALS Equalization (zerstört Gel-Struktur)
- LiFePO4: NIEMALS (BMS schaltet ab oder Zellschaden)

**F10: Wie schnell kann ich LiFePO4 laden?**
- Empfohlen: 0,5C (= 50A bei 100 Ah) → 80% in ca. 1,5h
- Maximal: 1C (= 100A bei 100 Ah) → 80% in ca. 50 min
- Begrenzender Faktor: BMS-Limit, nicht die Zellchemie
- Praxistipp: Mit 0,5C laden schont die Zellen und erreicht >5.000 Zyklen

### 8.3 Installation und Sicherheit

**F11: Welche Belüftung braucht ein Batterieraum?**
- Nass-Blei: ZWINGEND belüftet (Knallgas H₂ bei >4% explosiv!)
  - Berechnung: Q = 0,52 × n × I × 10⁻⁴ m³/h (n=Zellen, I=Ladestrom)
  - Mindestens 2 Lüftungsöffnungen (oben und unten)
- AGM/Gel: Geringe Belüftung empfohlen (Sicherheitsventil kann Gas ablassen)
- LiFePO4: Keine spezielle Belüftung für normalen Betrieb nötig
  - ABER: Notbelüftung für Thermal-Runaway-Fall empfohlen

**F12: Wie befestige ich Batterien seeklar?**
- Batterie muss gegen Verrutschen in ALLE Richtungen gesichert sein
- Spanngurte (Edelstahl oder Nylon) mit max. 1cm Spiel
- Säurefester Batteriekasten (Blei) mit Deckel
- ISO 10133: Batterie muss bei 30° Krängung + 1g Beschleunigung sicher bleiben
- LiFePO4: Leichter, aber gleiche Sicherungsanforderungen
- NIEMALS Batterien gestapelt ohne Zwischenplatte (Kurzschlussgefahr)

**F13: Brauche ich einen Batterieschalter?**
Ja, IMMER:
- Hauptschalter für Versorgungskreis (trennt alle Verbraucher)
- Separater Schalter für Starter (oder kombinierter 1-2-Beide-Aus-Schalter)
- Empfehlung: Blue Sea m-Serie oder BEP Marine (700A+ Dauerlast)
- LiFePO4: BMS hat eingebauten Schalter, aber externer Hauptschalter trotzdem empfohlen (Service/Notfall)

**F14: Wie dimensioniere ich die Batteriesicherung?**
- Sicherung schützt das KABEL, nicht die Batterie
- Sicherung ≤ Kabel-Ampacity (Belastbarkeit des Kabels)
- Sicherung > maximaler Dauerstrom der angeschlossenen Verbraucher
- Sicherung am Batterie-Pluspol (max. 20 cm Kabelweg vor Sicherung)
- Beispiel: 35mm² Kabel (Ampacity 170A) → Sicherung 150A
- LiFePO4-Zusatz: BMS-Limit ist NICHT die Absicherung! Externe Sicherung zwingend.

**F15: Kann LiFePO4 in ein bestehendes Bleisystem eingebaut werden?**
Retrofit-Checkliste:
1. Ladegerät: LiFePO4-Profil vorhanden oder einstellbar? (14,2–14,6V, kein Equalization)
2. Lichtmaschine: Strombegrenzung nötig (DC-DC-Wandler oder B2B-Lader)
3. Kabelquerschnitte: Prüfen ob für höhere Lade-/Entladeströme ausreichend
4. Sicherungen: Anpassen an neue maximale Ströme
5. Batteriemonitor: Auf LiFePO4-Profil umstellen (andere SoC-Berechnung)
6. Solarregler: LiFePO4-Profil einstellen (Victron MPPT: vorprogrammiert)
7. Platz: LiFePO4 ist ~50% kleiner/leichter → Ballast-Ausgleich nötig? (Segelyachten!)

### 8.4 BMS und Monitoring

**F16: Was macht ein BMS genau?**
Battery Management System — überwacht und schützt LiFePO4-Zellen:
- Überspannungsschutz (pro Zelle >3,65V → Laden abschalten)
- Unterspannungsschutz (pro Zelle <2,5V → Entladen abschalten)
- Überstromschutz (>BMS-Limit → Abschaltung)
- Kurzschlussschutz (<1ms Reaktionszeit)
- Übertemperaturschutz (>55°C → Abschaltung)
- Untertemperaturschutz beim Laden (<0°C → Laden sperren)
- Zell-Balancierung (passiv: 30–100mA oder aktiv: 1–5A)
- Kommunikation (Bluetooth, CAN-Bus, VE.Bus)
- Datenlogging (Zyklen, Min/Max-Werte, Fehler)

**F17: Aktives vs. passives Balancing — was ist besser?**
- Passives Balancing: Überschüssige Energie der vollsten Zelle wird als Wärme abgeleitet (Widerstand). Einfach, günstig, aber langsam (50–100 mA). Funktioniert nur am oberen Spannungsende.
- Aktives Balancing: Energie wird von volleren zu leereren Zellen transferiert. Schneller (1–5A), effizienter, aber teurer und komplexer. Funktioniert über den gesamten SoC-Bereich.
- Empfehlung: Passives Balancing reicht für die meisten Anwendungen, wenn die Batterie regelmäßig (alle 2–4 Wochen) vollständig geladen wird.

**F18: Welchen Batteriemonitor soll ich kaufen?**
- Budget: Victron SmartShunt (€80) — Bluetooth, Coulomb-Counting, App
- Mittelklasse: Victron BMV-712 (€170) — Display + Bluetooth + Relais
- Premium: Victron Cerbo GX + Touchdisplay (€450+) — Gesamtsystem-Monitoring
- Alternative: Mastervolt MasterShunt 500 (€250) — MasterBus-Integration
- DIY: Simarine Pico (€350) — Schickes Display, NMEA 2000

**F19: Muss ich die Zellenspannungen einzeln überwachen?**
- Bei LiFePO4: JA — das BMS tut dies intern, aber der Nutzer sollte Zugriff auf die Daten haben (App/Display). Differenz >50 mV bei Ruhe = Balancierung prüfen. Differenz >100 mV = Problem.
- Bei Blei-Säure: NEIN (keine Einzelzellen-Messung möglich ohne Öffnen). Gesamtspannung und Säuredichte (bei Nass-Blei) genügen.

**F20: Was ist ein „Smart BMS" und brauche ich das?**
Smart BMS = BMS mit Bluetooth/App-Kommunikation für Remote-Monitoring. Vorteile: Zellenspannungen am Handy ablesen, Fehlerhistorie, SoC-Anzeige, OTA-Updates. Für Fahrtenyachten dringend empfohlen — ermöglicht Fernüberwachung und frühzeitige Problemerkennung.

### 8.5 Spezifische Situationen

**F21: Batterie im Winterlager — was beachten?**
- Blei-Säure: Vollständig laden, dann Erhaltungsladegerät anschließen ODER alle 4 Wochen nachladen. Niemals entladen stehen lassen (Sulfatierung!). Bei Frost: Vollgeladene Batterie friert erst bei −40°C, entladene bei −10°C!
- LiFePO4: Auf 50–60% SoC laden, BMS-Trennschalter AUS (verhindert BMS-Ruhestromverbrauch), trocken und frostfrei lagern. Kein Ladegerät nötig.

**F22: Batterie für Langfahrt (Blauwasser) — worauf kommt es an?**
- Redundanz: Mindestens 2 unabhängige Batteriebänke
- Autonomie: 3–5 Tage ohne Nachladen
- Ladequellen: Solar + Wind + Lichtmaschine + optional Generator
- LiFePO4 vorteilhaft: schnelleres Laden, mehr nutzbare Kapazität
- Ersatzteile: BMS-Sicherungen, Kabelschuhe, Multimeter mitnehmen
- Monitoring: Fernzugriff (Iridium/Starlink + VRM Portal)

**F23: Darf ich Batterien parallel schalten?**
- Gleicher Typ, gleiches Alter, gleicher Hersteller: JA
- Verbindungskabel: Gleiche Länge und Querschnitt (symmetrische Impedanz)
- Blei-Säure: Bis 4 Batterien parallel, darüber Umverteilungsprobleme
- LiFePO4: Herstellervorgabe beachten (typisch 2–5 parallel, BMS-abhängig)
- Cross-Diagonal-Verkabelung: + von Batterie 1, − von Batterie 4 → gleichmäßige Stromverteilung

**F24: Was bedeutet „Marine-Grade" bei Batterien?**
Kein geschützter Begriff! Seriöse Marine-Batterien bieten:
- Vibrationsfeste Konstruktion (ABYC-Test: 4g, 20 min)
- Flammenrückschlagschutz am Ventil
- Korrosionsbeständige Polbuchsen (verzinnt/verbleit)
- Spritzwassergeschützt (min. IP22, besser IP56+)
- Lageunabhängig (AGM/Gel/LiFePO4)
- Zertifizierung: CE, ggf. GL/DNV, UL

**F25: Wie entsorge ich alte Bootsbatterien?**
- Blei-Säure: Rückgabe an Händler (gesetzliche Rücknahmepflicht, Pfand €7,50)
- LiFePO4: Elektro-Altgeräte-Sammlung oder Hersteller-Rücknahme
- NIEMALS im Hausmüll oder über Bord! (Straftat, Umweltschaden)
- Recycling-Quote Blei: >99% (wirtschaftlich attraktiv)
- Recycling LiFePO4: Im Aufbau (Lithium, Eisen, Phosphat rückgewinnbar)

**F26: Wie teste ich den Zustand meiner Batterie selbst?**
Einfacher Belastungstest für Laien:
1. Batterie vollständig laden (über Nacht am Ladegerät)
2. 4 Stunden ruhen lassen (kein Verbraucher)
3. Ruhespannung messen: >12,6V (Blei) bzw. >13,2V (LiFePO4) = gut
4. Definierten Verbraucher einschalten (z.B. 5A-Glühlampe)
5. Spannung nach 30 Sekunden messen: Einbruch >0,5V = Problem
6. Alternativ: Batterie-Analysator verwenden (z.B. Midtronics, CTEK Analyzer)

Professioneller Test: Kapazitätsmessung bei C/20 (5A bei 100 Ah) bis 10,5V. Ergebnis in Ah = aktuelle Kapazität. Vergleich mit Nennkapazität = SoH.

**F27: Was ist der Unterschied zwischen Serien- und Parallelschaltung?**
- **Serienschaltung:** Spannung addiert sich, Kapazität bleibt gleich.
  Beispiel: 4× 3,2V/100Ah in Serie = 12,8V/100Ah
  Anwendung: LiFePO4-Zellen zu 12V-Pack, 12V-Batterien zu 24V-System
- **Parallelschaltung:** Kapazität addiert sich, Spannung bleibt gleich.
  Beispiel: 3× 12V/100Ah parallel = 12V/300Ah
  Anwendung: Erhöhung der Bankkapazität
- **Kombination:** Serie-Parallel (z.B. 2S3P für 24V/300Ah)
  WICHTIG: Nur identische Batterien (Typ, Alter, Kapazität) parallel!

**F28: Wie schütze ich meine Batterie vor Blitzschlag?**
- Direkte Blitzableitung: Über Mast-Erdung (Kiel oder Grundplatte)
- Induktive Überspannungen können Batterieelektronik (BMS) zerstören
- Schutzmaßnahmen: Überspannungsableiter (MOV) an Batteriepolen, geschirmte Kabel für BMS-Kommunikation, redundantes BMS
- Nach Blitzeinschlag: Alle Elektronik prüfen, BMS-Reset, Zellenspannungen kontrollieren

**F29: Wie lagere ich Ersatzbatterien an Bord?**
- Blei-Säure: Voll geladen, aufrecht, belüftet, alle 3 Monate nachladen
- LiFePO4: Bei 50–60% SoC, BMS-Trennschalter AUS, trocken, raumtemperiert
- NIEMALS lose Batterien ungesichert an Bord! (Kurzschlussgefahr bei Kontakt)
- Pole abdecken (Gummikappe) oder mit Isolierband schützen
- Temperatur: 10–25°C ideal, NICHT im Maschinenraum lagern

**F30: Was passiert bei einem Wassereinbruch im Batterieraum?**
- Blei-Säure: Kurzschlussgefahr wenn Salzwasser Pole überbrückt, Säureaustritt kontaminiert Bilge → SOFORT Strom trennen
- LiFePO4: BMS kann bei Wasserkontakt Fehlfunktion zeigen, Korrosion an Elektronik → SOFORT isolieren
- Maßnahmen: Batterieschalter AUS, Wasser absaugen, Batterie trocknen/ersetzen
- Prävention: Batteriekasten wasserdicht (IP56+), Drainageöffnung nach unten, Montage über Bilgenwasserlinie

**F31: Kann ich einen Wechselrichter direkt an die Starterbatterie anschließen?**
NEIN — niemals:
- Wechselrichter-Spitzenstrom (z.B. 150A bei 2000W) überfordert Starterbatterien bei zyklischer Nutzung
- Starterbatterie wird tiefentladen → Motor startet nicht mehr
- IMMER separaten Versorgungskreis für Wechselrichter verwenden
- Ausnahme: Notfallbetrieb mit Batterie-Umschalter (1-2-Beide-Aus)

**F32: Meine AGM-Batterie „kocht" beim Laden — was tun?**
AGM-Batterien dürfen NICHT „kochen" (= hörbare Gasung). Mögliche Ursachen:
1. Ladespannung zu hoch (>14,7V) → Ladegerät prüfen/austauschen
2. Temperaturkompensation defekt → Sensor prüfen
3. Batterie intern kurzgeschlossen (defekte Zelle) → Batterie ersetzen
4. Equalization-Modus versehentlich aktiv → Sofort deaktivieren!
→ Bei aktiver Gasung: Sofort Ladestrom unterbrechen, belüften!

**F27: Kann ich Solarpanels direkt an die Batterie anschließen?**
NEIN — immer über einen Laderegler (MPPT oder PWM):
- Ohne Regler: Batterie wird bei Sonnenschein permanent überladen → Zerstörung
- MPPT-Regler: Optimiert Solarertrag (bis 30% mehr als PWM)
- LiFePO4-kompatibel: Victron SmartSolar MPPT (alle Modelle)
- Einstellung: LiFePO4-Profil wählen (14,2V Absorption, kein Float oder 13,5V)

### 8.6 Kostenfragen

**F28: Was kostet ein komplettes 12V-Lithium-System für eine 12m Yacht?**
Typische Kalkulation:
- 2× LiFePO4 200 Ah (Victron Smart): €5.000
- 1× Victron MultiPlus 12/3000: €1.800
- 1× Victron SmartSolar MPPT 150/35: €350
- 1× Orion-Tr Smart 12/12-30 (B2B): €200
- 1× Cerbo GX + Touch 50: €550
- Verkabelung + Sicherungen + Installation: €800–€1.500
- **Gesamt: ca. €8.700–€9.400**

**F29: Wann amortisiert sich Lithium gegenüber AGM?**
Vergleichsrechnung (200 Ah nutzbare Kapazität):
- AGM-Lösung: 2× 200 Ah AGM = €800, alle 5 Jahre ersetzen → €160/Jahr
- LiFePO4-Lösung: 1× 250 Ah LiFePO4 = €1.500, hält 12 Jahre → €125/Jahr
- Break-Even: nach ca. 6 Jahren (ohne Berücksichtigung Gewichtsvorteil/Platz)

**F30: Welche Batterien verwenden Yachthersteller ab Werft?**
Typische OEM-Ausstattung (Stand 2025):
- Bavaria/Hanse/Bénéteau (Produktion): AGM Deep Cycle (Exide, Varta)
- Hallberg-Rassy/Najad: Mastervolt MVG Gel (traditionell) oder MLI Ultra (seit 2023)
- Oyster/Swan: LiFePO4 (Victron oder Mastervolt, je nach Konfigurator)
- Lagoon/Fountaine Pajot: AGM Standard, LiFePO4 als Option (+€5.000–€12.000)
- Sunreef/HH Catamarans: LiFePO4 serienmäßig (Premium-Segment)

**F31: Wie funktioniert ein Batterie-Trennrelais (VSR/Cyrix)?**
Ein Voltage Sensitive Relay (VSR) oder Victron Cyrix verbindet automatisch zwei Batteriebänke (z.B. Starter + Versorgung) wenn die Ladespannung einen Schwellwert überschreitet (typisch 13,7V). Sobald die Spannung unter 13,0V fällt, trennt das Relais die Bänke.
- Vorteil: Starterbatterie wird über Lichtmaschine mitgeladen
- Nachteil: Keine Strombegrenzung, keine separate Ladekurve
- Für LiFePO4: Cyrix-Li-Serie verwenden (spezielle Schwellwerte)
- Alternative: DC-DC-Wandler (Orion-Tr Smart) = besser für LiFePO4

**F32: Was ist ein „Drop-In-Replacement" bei LiFePO4?**
Drop-In = LiFePO4-Batterie mit gleichen Abmessungen und Anschlüssen wie eine Standard-Blei-AGM. Beispiele: Battle Born BB10012, RELiON RB100, Liontron LiFePO4 100Ah.
- ABER: „Drop-In" bedeutet NICHT, dass keine Systemanpassungen nötig sind!
- Ladegerät MUSS LiFePO4-kompatibel sein
- Lichtmaschine MUSS strombegrenzt werden
- Batteriemonitor MUSS auf LiFePO4-Profil umgestellt werden
- Der Begriff ist Marketing — immer Gesamtsystem prüfen!

**F33: Wie schütze ich Batterien vor Diebstahl im Hafen?**
- Batteriekasten abschließbar (Vorhängeschloss)
- Hauptschalter mit Schlüssel
- GPS-Tracker in der Batteriebox (GSM-basiert)
- Alarmsystem mit Stromüberwachung (plötzliche Unterbrechung = Alarm)
- Versicherung: Batterien in Yacht-Inventarliste aufnehmen (Seriennummern!)

**F34: Was bedeutet „Calendar Aging" vs. „Cycle Aging"?**
- **Calendar Aging (kalendarische Alterung):** Batterie verliert Kapazität allein durch Zeitablauf, auch ohne Nutzung. Getrieben durch Temperatur und SoC-Niveau. LiFePO4 bei 50% SoC und 25°C: ca. 1–2%/Jahr.
- **Cycle Aging (zyklische Alterung):** Kapazitätsverlust durch Lade-/Entladezyklen. Getrieben durch DoD, C-Rate, Temperatur. Dominanter Effekt bei aktiver Nutzung.
- Marine-Relevanz: Wochenend-Segler (wenig Zyklen) verlieren primär durch Calendar Aging; Vollzeit-Liveaboards durch Cycle Aging.

**F35: Kann ich meine Batterie mit einem PKW überbrücken?**
- Blei → Blei: JA (gleiche Chemie, kurzzeitig akzeptabel)
- LiFePO4: NEIN — PKW-Lichtmaschine liefert unkontrolliert 80+ A direkt in die Batterie. BMS kann abschalten oder Zellschaden bei Kälte.
- Empfehlung: Mobiles Starthilfegerät (LiFePO4-Booster, z.B. NOCO GB40) an Bord mitführen

---

## 9. Glossar

| Begriff | Erklärung |
|---------|-----------|
| **Ah (Amperestunde)** | Einheit der elektrischen Ladung/Kapazität. 1 Ah = 1 Ampere Strom über 1 Stunde. |
| **AGM (Absorbent Glass Mat)** | Blei-Säure-Technologie mit Glasfasermatten-Separator, der den Elektrolyt bindet. Wartungsfrei und lageunabhängig. |
| **Absorptionsspannung** | Konstantspannungsphase beim Laden. Batterie wird bei fester Spannung (z.B. 14,4V) geladen, Strom sinkt bis Batterie voll. |
| **Balancing / Balancierung** | Ausgleich der Zellenspannungen in einem Serien-Pack. Passiv (Widerstand) oder aktiv (Energietransfer). |
| **BMS (Battery Management System)** | Elektronische Überwachung und Schutzschaltung für Lithium-Batterien. Überwacht Spannung, Strom, Temperatur pro Zelle. |
| **Bulk-Phase** | Erste Ladephase mit konstantem Maximalstrom bis zur Absorptionsspannung. |
| **C-Rate** | Verhältnis von Strom zu Nennkapazität. 1C bei 100 Ah = 100 A. C/10 = 10 A. |
| **CCA (Cold Cranking Amps)** | Kaltstartleistung: Strom, den eine Starterbatterie bei −18°C für 30s über 7,2V halten kann. |
| **CC-CV (Constant Current – Constant Voltage)** | Standard-Ladeverfahren für Lithium. Erst Konstantstrom, dann Konstantspannung. |
| **Coulomb-Counting** | SoC-Bestimmung durch Integration des Stroms über die Zeit (Ah-Zähler). |
| **Deep Cycle** | Batterie, die für regelmäßige tiefe Entladung (50%+) und Wiederaufladung konstruiert ist. |
| **DoD (Depth of Discharge)** | Entladetiefe in Prozent der Nennkapazität. 50% DoD = 50% der Kapazität entnommen. |
| **Energiedichte** | Speicherbare Energie pro Gewicht (Wh/kg) oder Volumen (Wh/l). |
| **Equalization** | Kontrollierte Überladung (15,5V) bei Nass-Blei zur Desulfatierung. NUR für Nass-Blei! |
| **Float-Ladung** | Erhaltungsladung bei reduzierter Spannung (13,3–13,8V), kompensiert Selbstentladung. |
| **Grade A / Grade B** | Qualitätseinstufung von LiFePO4-Zellen. Grade A = Erstqualität, Grade B = leicht reduziert. |
| **IUoU** | Dreistu-Ladeverfahren für Blei-Säure: Konstantstrom → Konstantspannung → Erhaltungsspannung. |
| **Innenwiderstand (Ri)** | Ohmscher Widerstand innerhalb der Batterie. Bestimmt max. Strom und Wärmeverluste. |
| **Knallgas** | Explosives Gemisch aus Wasserstoff und Sauerstoff, entsteht bei Überladung von Blei-Säure-Batterien (>4% H₂ in Luft explosiv). |
| **LFP / LiFePO4** | Lithium-Eisenphosphat. Sichere Lithium-Chemie mit 3,2V/Zelle, keine Thermal-Runaway-Neigung bei korrektem BMS. |
| **Lithium-Plating** | Abscheidung metallischen Lithiums an der Anode bei Laden unter 0°C. Irreversibel, gefährlich. |
| **LTO (Lithium-Titanat)** | Lithium-Chemie mit Titanat-Anode. Extrem schnellladefähig (5C) und langlebig (>15.000 Zyklen). |
| **LVD (Low Voltage Disconnect)** | Automatische Lastabschaltung bei Unterschreitung einer Mindestspannung. Schützt vor Tiefentladung. |
| **MCA (Marine Cranking Amps)** | Kaltstartleistung bei 0°C (statt −18°C wie CCA). MCA ≈ 1,25 × CCA. |
| **MPPT** | Maximum Power Point Tracker. Solarladeregler, der den optimalen Arbeitspunkt des Solarpanels findet. |
| **Peukert-Effekt** | Überproportionaler Kapazitätsverlust bei höheren Entladeraten (nur Blei-Säure relevant). |
| **Peukert-Exponent (k)** | Dimensionsloser Faktor, der die Stärke des Peukert-Effekts beschreibt. Ideal = 1,00; Blei = 1,15–1,40. |
| **Prismatische Zelle** | Rechteckiges Zellformat für LiFePO4 (z.B. CATL 280 Ah). Standard im Marine-Bereich. |
| **Ruhespannung (OCV)** | Spannung einer Batterie ohne Last nach >4h Ruhe. Korreliert mit SoC. |
| **SEI (Solid Electrolyte Interface)** | Passivierungsschicht auf der Anode von Lithium-Zellen. Wächst mit der Zeit und reduziert Kapazität. |
| **SoC (State of Charge)** | Ladezustand in Prozent. SoC = 100% − DoD. |
| **SoH (State of Health)** | Gesundheitszustand als Verhältnis aktuelle Kapazität / Nennkapazität. SoH <80% = End-of-Life. |
| **Sulfatierung** | Bildung harter PbSO₄-Kristalle auf Blei-Platten durch unvollständiges Laden. Häufigste Ausfallursache. |
| **Tail Current** | Ladestrom am Ende der Absorptionsphase. Typisch C/100. Signal für „Batterie voll". |
| **Thermal Runaway** | Unkontrollierte exotherme Reaktion in Lithium-Zellen. Kann zu Brand/Explosion führen. |
| **Top-Balancing** | Balancierung durch gemeinsame Vollladung aller Zellen. Standard-Methode für LiFePO4-Packs. |
| **Wh (Wattstunde)** | Einheit der elektrischen Energie. Wh = Ah × V. Besser als Ah für Vergleiche verschiedener Spannungen. |
| **Zyklenlebensdauer** | Anzahl der Lade-/Entladezyklen bis SoH <80%. Stark DoD-abhängig. |
| **Ampacity** | Maximale Strombelastbarkeit eines Kabels in Ampere (abhängig von Querschnitt, Temperatur, Verlegeart). |
| **B2B-Lader (Battery-to-Battery)** | DC-DC-Wandler der eine Batterie (z.B. Starter via Lichtmaschine) als Quelle nutzt und eine zweite (Versorgung) isoliert und geregelt lädt. |
| **Calendar Aging** | Alterung einer Batterie allein durch Zeitablauf (ohne Nutzung), getrieben durch Temperatur und Ladezustand. |
| **CAN-Bus** | Controller Area Network — serieller Datenbus für Kommunikation zwischen BMS, Ladegeräten und Monitoring. Standard im Marine-Bereich. |
| **Cycle Aging** | Alterung einer Batterie durch wiederholte Lade-/Entladezyklen. Abhängig von DoD, C-Rate und Temperatur. |
| **Dendrit** | Nadelförmige kristalline Ablagerung (Blei oder Lithium), die im Batterie-Inneren wachsen und Kurzschlüsse verursachen kann. |
| **Drop-In-Replacement** | LiFePO4-Batterie mit identischen Abmessungen wie Standard-AGM, aber NICHT ohne Systemanpassung einsetzbar. |
| **Gasung** | Bildung von Wasserstoff und Sauerstoff durch Elektrolyse des Wassers im Elektrolyt bei Überladung. Bei >4% H₂ in Luft explosiv. |
| **IP-Schutzklasse** | International Protection Rating. IP56 = staubgeschützt + Schutz gegen starkes Strahlwasser. IP67 = staubdicht + Untertauchen. |
| **Na-Ion** | Natrium-Ionen-Batterie. Neuere Technologie ohne Lithium/Kobalt, kältetoleranter, aber geringere Energiedichte. |
| **OCV (Open Circuit Voltage)** | Leerlaufspannung = Ruhespannung einer Batterie ohne Last. |
| **OPzS** | Ortsfest Panzerplatte Spezial — besonders langlebiger Blei-Säure-Zelltyp mit Röhrchenplatten. |
| **Rekombination** | Chemische Rückführung von Gasen (H₂ + O₂) zu Wasser innerhalb der Batterie. Bei AGM/Gel >99% Effizienz. |
| **Smart Shunt** | Stromsensor (Hall-Effekt oder Shunt-Widerstand) mit integrierter Elektronik und Bluetooth für SoC-Berechnung. |
| **VE.Bus / VE.Direct** | Proprietary Victron-Kommunikationsprotokolle für Systemintegration (BMS, Ladegeräte, Wechselrichter). |
| **VSR (Voltage Sensitive Relay)** | Spannungsgesteuertes Trennrelais, verbindet Batteriebänke automatisch bei Ladespannung. |

---

## 10. Schnell-Referenz

### 9.2 Vergleichstabelle: Alle Technologien auf einen Blick

| Eigenschaft | Nass-Blei | AGM | Gel | LiFePO4 | LTO | Na-Ion |
|-------------|----------|-----|-----|---------|-----|--------|
| Energiedichte (Wh/kg) | 30–35 | 35–48 | 35–45 | 130–160 | 60–80 | 100–140 |
| Zellspannung (V) | 2,0 | 2,0 | 2,0 | 3,2 | 2,4 | 3,1 |
| Nennspannung 12V-Pack | 12,0 | 12,0 | 12,0 | 12,8 | 12,0 (5S) | 12,4 (4S) |
| Zyklen (50% DoD) | 300–800 | 500–1.200 | 1.000–1.800 | 3.500–6.000 | >10.000 | 3.000–5.000 |
| Empfohlene DoD | 50% | 50–60% | 60–70% | 80% | 90–95% | 80% |
| Nutzbar (% Nennkapazität) | 50% | 55% | 65% | 80% | 90% | 80% |
| Max. Ladestrom | C/5 | C/3 | C/10 | 1C | 5C | 1C |
| Max. Entladestrom | C/2 | 1C | C/3 | 2C | 10C | 2C |
| Ladetemperatur min. | −10°C | −10°C | −10°C | 0°C | −30°C | −20°C |
| Selbstentladung/Monat | 5–15% | 1–3% | 1–3% | 1–3% | <1% | 2–4% |
| Wartung | Hoch | Keine | Keine | Keine | Keine | Keine |
| Lageunabhängig | Nein | Ja | Ja | Ja | Ja | Ja |
| BMS erforderlich | Nein | Nein | Nein | JA | JA | JA |
| Gasung/Explosionsrisiko | JA | Minimal | Minimal | Nein | Nein | Nein |
| Thermal Runaway Risiko | Nein | Nein | Nein | Sehr gering | Nein | Nein |
| Gewicht (100Ah, 12V) | 28–35 kg | 26–32 kg | 30–36 kg | 12–15 kg | 25–30 kg | 18–22 kg |
| Preis (100Ah, 12V) | €120–250 | €200–400 | €280–500 | €500–1.200 | €1.500–3.000 | €300–500 |
| Marine-Verfügbarkeit | Überall | Überall | Gut | Sehr gut | Begrenzt | Sehr begrenzt |
| Recycling-Rate | >99% | >99% | >99% | ~50% (im Aufbau) | ~50% | Neu |
| Typischer Einsatz Marine | Starter | Deep Cycle | Langfahrt | Universell | Hybrid/E-Antrieb | Kälte-Anw. |

### 9.3 Entscheidungsmatrix: Welche Technologie wählen?

**Scoring-Tabelle (1=schlecht, 5=exzellent):**

| Kriterium (Gewicht) | Nass-Blei | AGM | Gel | LiFePO4 | LTO |
|---------------------|----------|-----|-----|---------|-----|
| Anschaffungskosten (15%) | 5 | 4 | 3 | 2 | 1 |
| Lebensdauer/Zyklen (25%) | 2 | 3 | 4 | 5 | 5 |
| Gewicht/Volumen (15%) | 1 | 2 | 2 | 5 | 3 |
| Ladegeschwindigkeit (10%) | 2 | 3 | 2 | 5 | 5 |
| Wartungsaufwand (10%) | 1 | 5 | 5 | 4 | 4 |
| Sicherheit (10%) | 2 | 4 | 4 | 4 | 5 |
| Systemkomplexität (5%) | 5 | 5 | 5 | 3 | 2 |
| Kältetauglichkeit (5%) | 3 | 3 | 3 | 2 | 5 |
| Verfügbarkeit (5%) | 5 | 5 | 4 | 4 | 2 |
| **Gewichteter Score** | **2,55** | **3,40** | **3,35** | **4,05** | **3,55** |

→ **LiFePO4 gewinnt** in der Gesamtbewertung für die meisten Marine-Anwendungen (2025+)
→ **AGM bleibt sinnvoll** für budgetbewusste Eigner mit <50 Seetagen/Jahr
→ **Gel für Langfahrt** mit Solar-Ladung (niedrige, konstante Ströme)
→ **LTO für Spezialanwendungen** (E-Antrieb, Hybrid, Extremkälte)

### 9.4 Kompatibilitätsmatrix: Ladegeräte und Batterien

| Ladegerät-Einstellung | Nass-Blei | AGM | Gel | LiFePO4 |
|----------------------|----------|-----|-----|---------|
| Blei-Standard (14,4V/13,5V Float) | ✓ Optimal | ✓ OK | ⚠️ Grenzwertig | ⚠️ Suboptimal |
| AGM (14,7V/13,8V Float) | ⚠️ Leicht hoch | ✓ Optimal | ✗ ZU HOCH! | ⚠️ Suboptimal |
| Gel (14,1V/13,8V Float) | ⚠️ Unterladung | ⚠️ Unterladung | ✓ Optimal | ⚠️ Suboptimal |
| LiFePO4 (14,2V/kein Float) | ⚠️ Unterladung | ⚠️ Unterladung | ⚠️ Unterladung | ✓ Optimal |
| Universal/Auto (14,8V) | ✓ OK | ⚠️ Leicht hoch | ✗ ZERSTÖREND! | ✗ BMS schaltet ab |
| Equalization (15,5V) | ✓ Periodisch | ✗ VERBOTEN! | ✗ VERBOTEN! | ✗ VERBOTEN! |

Legende: ✓ = kompatibel, ⚠️ = funktioniert aber nicht optimal, ✗ = schädlich/verboten

### 10.0 Checkliste: Batterieinstallation Neuboot / Refit

**Vor der Installation:**
- [ ] Energiebilanz erstellt (alle Verbraucher erfasst)
- [ ] Systemspannung festgelegt (12V/24V/48V)
- [ ] Batteriechemie gewählt (AGM/Gel/LiFePO4)
- [ ] Bankkapazität berechnet (mit Autonomie-Reserve)
- [ ] Standort festgelegt (nicht Maschinenraum, belüftet, zugänglich)
- [ ] Kabelquerschnitte berechnet (max. 3% Spannungsabfall)
- [ ] Sicherungen dimensioniert (≤ Kabel-Ampacity)
- [ ] Ladequellen identifiziert (Landstrom, Lichtmaschine, Solar, Wind)
- [ ] Ladeprofil-Kompatibilität geprüft
- [ ] BMS-Anforderungen definiert (LiFePO4)
- [ ] Monitoring-System gewählt

**Während der Installation:**
- [ ] Batteriekasten säurefest (Blei) / vibrationsfest
- [ ] Spanngurte / Halterungen montiert (30°-Krängungstest)
- [ ] Hauptschalter installiert (zugänglich, nicht im Batterieraum)
- [ ] Sicherung direkt am Pluspol (<20 cm Kabel)
- [ ] Kabel verzinnt, mit Schrumpfschlauch und Kabelschuh
- [ ] Pol-Reihenfolge: erst Plus, dann Minus anschließen (Abklemmen umgekehrt: erst Minus, dann Plus)
- [ ] Drehmoment an Polklemmen nach Herstellervorgabe
- [ ] Belüftung geprüft (Blei-Säure: Berechnung!)
- [ ] Temperatursensor platziert (am Batteriegehäuse, mittlere Zelle)
- [ ] BMS-Kommunikation getestet (CAN/VE.Bus/Bluetooth)
- [ ] Ladeprofil am Ladegerät korrekt eingestellt

**Nach der Installation:**
- [ ] Ruhespannung gemessen und dokumentiert
- [ ] Erste Vollladung durchgeführt
- [ ] Alle Verbraucher getestet (kein unerwarteter Spannungsabfall)
- [ ] Monitoring-System zeigt korrekte Werte
- [ ] Batteriemonitor kalibriert (Shunt-Nullpunkt)
- [ ] Dokumentation: Typ, Seriennummer, Installationsdatum
- [ ] Alarmgrenzen gesetzt (Unterspannung, Übertemperatur)
- [ ] Eigner in Bedienung und Wartung eingewiesen

### 10.0b Wartungsintervalle nach Technologie

| Wartungsarbeit | Nass-Blei | AGM | Gel | LiFePO4 |
|---------------|----------|-----|-----|---------|
| Polklemmen prüfen/reinigen | Monatlich | 3 Monate | 3 Monate | 6 Monate |
| Elektrolytstand prüfen | 4–8 Wochen | — | — | — |
| Wasser nachfüllen | Nach Bedarf | — | — | — |
| Ruhespannung messen | Monatlich | 3 Monate | 3 Monate | 3 Monate |
| Kapazitätstest (C/20) | Jährlich | Jährlich | Jährlich | 2 Jahre |
| Innenwiderstand messen | Jährlich | Jährlich | Jährlich | 2 Jahre |
| Ladeprofil verifizieren | 6 Monate | 6 Monate | 6 Monate | 6 Monate |
| BMS-Firmware-Update | — | — | — | Wenn verfügbar |
| Zellenspannungen prüfen | — | — | — | 3 Monate |
| Equalization | 3 Monate | NICHT | NICHT | NICHT |
| Batterieschalter-Funktion | 6 Monate | 6 Monate | 6 Monate | 6 Monate |
| Befestigung prüfen | Vor Saison | Vor Saison | Vor Saison | Vor Saison |
| Säure-Auffangwanne prüfen | 6 Monate | — | — | — |
| Belüftung prüfen/reinigen | 6 Monate | Jährlich | Jährlich | Jährlich |

### 10.0c Notfall-Referenzkarte

**Batterie-Notfälle — Sofortmaßnahmen:**

| Situation | Sofortmaßnahme | NICHT tun |
|-----------|---------------|-----------|
| Rauch aus Batterie | Raum verlassen, belüften, Feuerwehr | Kein Wasser auf LiFePO4! |
| Aufgeblähtes Gehäuse | Sofort isolieren, nicht berühren | Nicht versuchen zu laden |
| Säureaustritt | Handschuhe, mit Natron neutralisieren | Nicht mit bloßen Händen |
| Funkenbildung an Polen | Batterieschalter AUS, Kontakt herstellen | Kein offenes Feuer! |
| Totalausfall Bordnetz | Batterieschalter prüfen, BMS-LED prüfen | Nicht „Kabel brücken" |
| Frostschaden (Blei) | Langsam auftauen (>0°C), dann prüfen | Nicht laden wenn gefroren |
| Salzwasser an Batterie | Strom trennen, Süßwasser spülen, trocknen | Nicht ignorieren |

### 10.1 Ladespannungen auf einen Blick (12V-System, 25°C)

| Parameter | Nass-Blei | AGM | Gel | LiFePO4 |
|-----------|----------|-----|-----|---------|
| Absorption | 14,4 V | 14,4–14,7 V | 14,1–14,4 V | 14,2–14,6 V |
| Float | 13,3–13,5 V | 13,5–13,8 V | 13,5–13,8 V | 13,5 V (optional) |
| Equalization | 15,5 V | VERBOTEN | VERBOTEN | VERBOTEN |
| Max. Ladestrom | C/5 | C/3 | C/10 | 0,5–1C |
| Temp.-Kompensation | −18 mV/°C | −18 mV/°C | −24 mV/°C | Keine |

### 10.2 Entscheidungshilfe: Welche Batterie für welches Boot?

| Bootstyp | Empfehlung | Begründung |
|----------|------------|------------|
| Motorboot <8m (Trailer) | AGM Dual Purpose | Einfach, wartungsfrei, Starter+Versorgung |
| Segelboot 8–10m (Weekender) | 2× AGM Deep Cycle + AGM Starter | Kosten-Nutzen optimal |
| Motoryacht 10–14m | AGM oder LiFePO4 | Je nach Nutzungsintensität |
| Fahrtenyacht 12–16m | LiFePO4 + AGM Starter | Gewicht, Kapazität, Zyklen |
| Blauwasser-Yacht 14–20m | LiFePO4 (redundant) | Autonomie, schnelles Laden |
| Superyacht >20m | LiFePO4 24V/48V, professionell | Individuell geplant |
| Regatta-Yacht | LiFePO4 oder LTO | Minimales Gewicht |
| Elektrisch angetrieben | LiFePO4 48V / Hochvolt | Torqeedo, Oceanvolt, etc. |

### 10.3 Kapazitätsplanung: Faustregel

```
Blei-Säure:    Batteriebank = Tagesbedarf (Ah) × 4 (bei 50% DoD, 2 Tage Autonomie)
LiFePO4:       Batteriebank = Tagesbedarf (Ah) × 2,5 (bei 80% DoD, 2 Tage Autonomie)
```

### 10.4 Gewichtsvergleich (200 Ah nutzbare Kapazität)

| Technologie | Nötige Nennkapazität | Gewicht | Volumen (ca.) |
|-------------|---------------------|---------|---------------|
| Nass-Blei | 400 Ah | 120 kg | 80 l |
| AGM | 400 Ah | 110 kg | 75 l |
| Gel | 330 Ah | 100 kg | 70 l |
| LiFePO4 | 250 Ah | 35 kg | 30 l |
| LTO | 220 Ah | 55 kg | 45 l |

### 10.5 Formeln und Berechnungen — Kurzreferenz

**Kapazitätsberechnung:**
```
Bankkapazität (Ah) = Tagesbedarf (Ah) × Autonomie-Tage / max_DoD
```

**Peukert-Korrektur (nur Blei):**
```
C_effektiv = C_nominal × (I_nominal / I_tatsächlich)^(k−1)
```

**Energieinhalt:**
```
Wh = Ah × V_mittel
kWh = Wh / 1000
```

**Spannungsabfall in Zuleitung:**
```
ΔU = (2 × L × I × ρ) / A
Wobei: L=Kabellänge(m), I=Strom(A), ρ=0,0175 Ω·mm²/m (Kupfer), A=Querschnitt(mm²)
```

**Ladezeit-Schätzung (Bulk-Phase bis 80%):**
```
t_bulk = (C_bank × 0,8) / I_lade  [Stunden]
```

**Temperaturkompensation Ladespannung:**
```
U_korrigiert = U_25°C + (T − 25) × Komp_Faktor × Zellen
Blei: Komp_Faktor = −3 mV/°C/Zelle × 6 Zellen = −18 mV/°C
```

**Belüftungsberechnung (Blei-Säure, ISO 10133):**
```
Q = 0,52 × n × I × 10⁻⁴  [m³/h]
Wobei: n=Zellenanzahl, I=max. Ladestrom(A)
```

**Wechselrichter-Batteriestrom:**
```
I_DC = P_AC / (η × U_batt)
η ≈ 0,90 (typischer Wirkungsgrad)
```

**Break-Even Lithium vs. Blei:**
```
Jahre = (Kosten_LiFePO4 − Kosten_Blei) / (Kosten_Blei/Lebensdauer_Blei − Kosten_LiFePO4/Lebensdauer_LiFePO4)
```

**Solar-Ertrag (vereinfacht):**
```
E_tag = P_peak × PSH × η_system
PSH = Peak Sun Hours (2–7 je nach Breitengrad/Jahreszeit)
η_system ≈ 0,65–0,75 (Panel + MPPT + Kabel + Temperatur)
```

**Parallelschaltung — Stromaufteilung:**
```
I_n = I_gesamt × (Ri_gesamt / Ri_n)
Ri_gesamt = 1 / Σ(1/Ri_n)
```

### 10.6 Gewichtsbudget und Schwerpunkt

**Relevanz für Segelyachten:**
Batterien sind oft die schwerste einzelne Ausrüstungskomponente. Ihre Position beeinflusst den Gewichtsschwerpunkt (CG) signifikant.

| Yacht-Größe | Typisches Batteriegewicht (Blei) | Nach LiFePO4-Upgrade | Gewichtsersparnis |
|-------------|--------------------------------|---------------------|------------------|
| 8m Segler | 50–80 kg | 20–30 kg | 30–50 kg |
| 12m Segler | 100–160 kg | 35–55 kg | 65–105 kg |
| 14m Segler | 150–250 kg | 50–80 kg | 100–170 kg |
| 18m Segler | 250–400 kg | 80–130 kg | 170–270 kg |

**Auswirkung auf Trimm:**
- Batterien typisch unter Salon/Pantry (nahe Schwerpunkt)
- Bei LiFePO4-Upgrade: Gewicht fällt weg → Boot wird leichter → weniger Tiefgang
- Bei Regatta-Yachten: Gewichtsersparnis = Geschwindigkeitsvorteil
- Bei Fahrtenyachten: Gewichtsersparnis = mehr Zuladung möglich
- ACHTUNG: Bei starker Gewichtsreduktion → Stabilität prüfen (ISO 12217)
- Ggf. Ausgleichsballast im unteren Bereich erforderlich

**Optimale Platzierung:**
- Möglichst tief und mittig (niedriger Schwerpunkt)
- Nicht im Maschinenraum (Hitze!)
- Nicht in der Bilge (Feuchtigkeit, Überflutungsrisiko)
- Ideal: Unter Salon-Sitzbänken, unter Kojen (mittschiffs)
- Zugänglich für Wartung und Monitoring

### 10.7 Kritische Grenzwerte — Sofortige Warnung

| Zustand | Grenzwert | Aktion |
|---------|-----------|--------|
| Blei-Spannung <11,5V (12V) | Tiefentladung | Sofort laden, LVD prüfen |
| Blei-Spannung >15,0V (12V) | Überladung | Ladegerät sofort trennen |
| LiFePO4 Zelle >3,65V | Überladung | BMS muss abschalten |
| LiFePO4 Zelle <2,5V | Tiefentladung | Irreversibler Schaden möglich |
| Zell-Differenz >100 mV | Imbalance | Balancierung erforderlich |
| Batterietemperatur >55°C | Überhitzung | Last reduzieren, Kühlung |
| LiFePO4 Laden bei <0°C | Lithium-Plating | SOFORT stoppen! |
| Innenwiderstand >2× Neuwert | End-of-Life | Batterie ersetzen |
| Kapazität <80% Nennwert | End-of-Life | Batterie ersetzen |
| Gasung bei AGM/Gel | Überladung | Ladegerät sofort trennen |
| Gehäuse aufgebläht | Interner Defekt | Batterie sofort ersetzen, GEFAHR |

---

## ANHANG A–H — Fallstudien

### ANHANG A — Fallstudie: Sulfatierte AGM-Batterien auf einer 38ft Segelyacht

**Yacht:** Bavaria 38 Cruiser (2015), 12V-System
**Problem:** Batteriebank (2× Victron AGM 220 Ah) nach nur 2 Jahren am End-of-Life
**Symptome:** Nur noch 3h Kühlschrankbetrieb statt 18h, Autopilot-Ausfälle bei Nachtfahrt

**Analyse:**
- Ruhespannung: 12,15V (≈55% SoC) — nach angeblicher Vollladung
- Innenwiderstand: 12 mΩ (Neuwert: 5 mΩ) → 240% des Neuwerts
- Ladeprofil-Aufzeichnung: Absorption nur 20 Minuten (statt 2–4h)
- Ursache: Landstrom-Ladegerät (Sterling Pro Charge Ultra) war auf „Gel" programmiert → Absorptionsspannung nur 14,1V statt 14,4V für AGM → chronische Unterladung → Sulfatierung

**Maßnahmen:**
1. Ladegerät auf AGM-Profil umgestellt (14,4V Absorption)
2. Desulfatierungsversuch: 48h bei 14,7V mit C/20 Strom → erfolglos (Ri blieb >10 mΩ)
3. Batterien ersetzt durch Victron AGM Super Cycle 230 Ah
4. Ladeprofil verifiziert und dokumentiert

**Kosten:** €1.360 (2× Batterie) + €150 (Arbeit) = €1.510
**Lernpunkt:** Falsches Ladeprofil ist der #1-Killer für AGM-Batterien. IMMER prüfen ob Ladegerät zum Batterietyp passt.

**AYDI-Bewertung:**
- Batteriezustand (vor Maßnahme): 18/100
- Systemkonfiguration: 35/100 (falsches Ladeprofil)
- Nach Maßnahme: 92/100

---

### ANHANG B — Fallstudie: LiFePO4-Upgrade auf einer Hallberg-Rassy 40

**Yacht:** Hallberg-Rassy 40 MkII (2018), 12V-System, Blauwasser-Ausrüstung
**Ausgangslage:** 4× Mastervolt MVG 200 Ah Gel (800 Ah total, 400 Ah nutzbar), 112 kg Batteriegewicht
**Ziel:** Höhere nutzbare Kapazität bei geringerem Gewicht für Transatlantik

**Neues System:**
- 2× Victron Lithium Smart 12,8V/330 Ah (660 Ah total, 528 Ah nutzbar)
- 1× Victron VE.Bus BMS v2
- 1× Victron Cerbo GX + GX Touch 50
- 1× Victron Orion-Tr Smart 12/12-30 (Lichtmaschinen-Ladung)
- 3× Victron SmartSolar MPPT 100/30 (Solar 3× 175W)
- 1× AGM 70 Ah Starterbatterie (separater Kreis)

**Vergleich:**

| Parameter | Gel (vorher) | LiFePO4 (nachher) |
|-----------|-------------|-------------------|
| Nutzbare Kapazität | 400 Ah | 528 Ah (+32%) |
| Gewicht (Versorgung) | 112 kg | 42 kg (−63%) |
| Ladezeit 0–80% (Solar) | 6–8h | 3–4h (−50%) |
| Autonomie (237 Ah/Tag) | 1,7 Tage | 2,2 Tage (+30%) |
| Zyklen bei täglichem 50% DoD | 1.500 | 5.000+ |
| Investition | €2.600 (bereits bezahlt) | €9.200 |

**Herausforderungen beim Retrofit:**
1. Lichtmaschinen-Strombegrenzung: 90A Bosch-Lichtmaschine lieferte Volllast → Orion-Tr auf 30A begrenzt
2. Temperaturmanagement: Batteriefach im Salon (kein Problem), aber CAN-Bus-Kabel musste neu verlegt werden
3. Gewichtsverteilung: 70 kg weniger tief im Schiff → 15 kg Bleiballast im Kiel-Bereich nachgerüstet
4. Alarmsystem: VE.Bus BMS steuert Relais für Ladequellen-Abschaltung → Verkabelung angepasst

**Ergebnis nach 2 Jahren / 18.000 nm:**
- Keine Ausfälle, Kapazität bei 97% SoH
- Energieautonomie: 2,5 Tage ohne Nachladen (Solar allein reicht für Tagesbedarf)
- Investition amortisiert sich über Lebensdauer gegenüber 2× Gel-Satz

**AYDI-Bewertung:** 94/100 (Gesamtsystem)

---

### ANHANG C — Fallstudie: Thermal Runaway auf einer Motoryacht (Beinahe-Unfall)

**Yacht:** Princess V48 (2020), 24V-System
**Vorfall:** Rauchentwicklung aus Batteriekasten während Hafenliegezeit

**Hergang:**
1. Eigner installierte „günstiges" 24V/200Ah LiFePO4-Pack (chinesische Marke, €600) als Versorgungsbatterie
2. BMS des Packs: Einfachst-Ausführung ohne Temperaturüberwachung
3. Landstrom-Ladegerät: Alte Mastervolt-Einstellung für Gel (14,1V × 2 = 28,2V für 24V)
4. Problem: Eine Zelle im Pack war von Anfang an schwächer (Grade-B-Zelle, unbekannte Herkunft)
5. Nach 8 Monaten: Schwache Zelle wird bei jedem Zyklus tiefer entladen → Kupfer-Dendritenbildung
6. Dendrit verursacht internen Mikro-Kurzschluss → lokale Erwärmung → Elektrolyt-Zersetzung

**Entdeckung:**
- Hafennachbar bemerkte Rauch aus Lüftungsöffnung
- Feuerwehr gerufen, Batterie mit Sand abgedeckt (kein Wasser!)
- Eine Zelle vollständig ausgebrannt, Nachbarzellen durch Hitze beschädigt

**Schadensumme:** €12.000 (Batterie, Kabelbaum, Batteriekasten, Reparatur)
**Kein Personenschaden** (Glück: Boot war unbewohnt)

**Analyse — Was lief falsch:**
1. Grade-B-Zellen unbekannter Herkunft (keine QC-Daten)
2. BMS ohne Temperaturüberwachung (hätte bei >60°C abschalten müssen)
3. Kein aktives Balancing → schwache Zelle wurde systematisch geschädigt
4. Keine redundante Überwachung (kein externer Batteriemonitor)

**Lernpunkte:**
- NIEMALS Billig-LiFePO4 ohne verifiziertes BMS + Temperaturschutz
- Grade-A-Zellen von bekannten Herstellern (EVE, CATL, BYD)
- BMS mit Temperaturüberwachung UND Kommunikation (Remote-Alarm)
- Feuerlöschdecke + CO₂-Löscher im Batterieraum

**AYDI-Bewertung (vor Vorfall):** Hätte bei visueller Analyse auf 25/100 gewartet (No-Name, kein Datenblatt, keine Zertifizierung)

---

### ANHANG D — Fallstudie: Optimale Solar-/Batterieanlage für eine 14m Katamaran-Langfahrtyacht

**Yacht:** Lagoon 42 (2021), 12V-System, Weltumsegelung geplant
**Anforderung:** Energieautarkie (kein Generator, kein Landstrom) für 5+ Tage

**Energiebilanz:**

| Verbraucher | Leistung | h/Tag | Wh/Tag |
|-------------|----------|-------|--------|
| 2× Kühlschrank/Freezer | 80W | 14 | 1.120 |
| Autopilot | 50W | 18 | 900 |
| Instrumentierung | 20W | 24 | 480 |
| Wassermacher (30 l/h) | 120W | 2 | 240 |
| LED-Beleuchtung | 30W | 5 | 150 |
| Laptops + Kommunikation | 80W | 4 | 320 |
| Diverses (Pumpen, Lüfter) | 30W | 6 | 180 |
| **Gesamt** | | | **3.390 Wh** |

→ 3.390 Wh / 12V = **283 Ah/Tag**

**Dimensionierung Batteriebank:**
- 5 Tage Autonomie bei 80% DoD: 283 × 5 / 0,8 = **1.769 Ah LiFePO4**
- Gewählt: 4× Victron Lithium Smart 12,8V/330 Ah = **1.320 Ah** (+ Solarertrag)
- Begründung: Mit 1.400 Wp Solar wird Autonomie auf >7 Tage erweitert

**Solaranlage:**
- 8× 175 Wp Solarpanels (Hardtop + Bimini) = 1.400 Wp
- 4× Victron SmartSolar MPPT 100/30
- Erwarteter Ertrag: 4.500–6.500 Wh/Tag (tropisch) → Überschuss!

**Systemkosten:**
- Batterien (4× 330 Ah): €15.200
- BMS + Cerbo GX + Monitoring: €1.200
- Solar (8× Panel + 4× MPPT): €3.200
- Wechselrichter (Victron MultiPlus 12/3000): €1.800
- Orion-Tr (2×): €400
- Installation + Kabel + Sicherungen: €3.000
- **Gesamt: ca. €24.800**

**Ergebnis nach 12 Monaten / 8.000 nm (Mittelmeer → Karibik):**
- Generator: 0 Betriebsstunden (nie gebraucht)
- Durchschnittlicher SoC bei Ankerlieger: 75–95%
- Durchschnittlicher SoC bei 5-Tages-Überfahrt: nie unter 40%
- SoH aller Batterien: 99%

**AYDI-Bewertung:** 97/100

---

### ANHANG E — Fallstudie: Batteriealterung und Kapazitätsmonitoring über 5 Jahre

**Yacht:** Jeanneau Sun Odyssey 440 (2019), 12V
**Batterie:** 2× Victron AGM Deep Cycle 165 Ah (installiert Mai 2019)
**Monitoring:** Victron BMV-712 mit VRM-Cloud-Logging

**Jährliche Kapazitätsmessung (C/20-Entladung):**

| Jahr | Kapazität (Ah) | SoH (%) | Innenwiderstand | Nutzung (Zyklen/Jahr) |
|------|---------------|---------|-----------------|----------------------|
| 2019 (neu) | 168 Ah | 102% | 5,5 mΩ | — |
| 2020 | 162 Ah | 98% | 5,8 mΩ | 180 |
| 2021 | 155 Ah | 94% | 6,2 mΩ | 200 |
| 2022 | 143 Ah | 87% | 7,1 mΩ | 220 |
| 2023 | 128 Ah | 78% | 8,5 mΩ | 190 |
| 2024 | 115 Ah | 70% | 10,2 mΩ | 150 (reduziert) |

**Analyse:**
- SoH fiel unter 80% in Jahr 4,5 → offizielles End-of-Life nach ISO-Definition
- Degradation beschleunigte sich ab Jahr 3 (typisch für AGM bei 50% DoD-Nutzung)
- Innenwiderstand-Verdoppelung korreliert mit 50% Kapazitätsverlust
- Eigner fuhr weiter bis 70% SoH (akzeptabel bei reduziertem Energiebedarf)

**Austausch 2024:** Upgrade auf Victron Lithium Smart 200 Ah (statt 2× AGM 165 Ah)
- Nutzbare Kapazität: 160 Ah (LiFePO4 bei 80% DoD) vs. vorher 165 Ah (AGM bei 50% DoD, aber nur noch 70% SoH → real 58 Ah nutzbar!)
- Gewichtsersparnis: 94 kg → 26 kg (−68 kg)

**AYDI-Lernpunkt:** Automatisierte SoH-Trendanalyse mit prädiktiver Warnung „Austausch in X Monaten empfohlen"

---

### ANHANG F — Fallstudie: Falsche Parallelschaltung — Ungleiche Alterung

**Yacht:** Bavaria Cruiser 46 (2016), 12V
**Problem:** 3× AGM 100 Ah parallel (= 300 Ah Bank), eine Batterie erst 2023 getauscht (andere 2016)

**Symptome:**
- Neue Batterie wird überproportional belastet (niedrigerer Innenwiderstand zieht mehr Strom)
- Alte Batterien „verstecken" sich hinter der neuen
- Neue Batterie altert beschleunigt
- Gesamtkapazität: nicht 300 Ah, sondern effektiv ca. 180 Ah

**Messung:**
- Batterie 1 (2016): Ri = 12 mΩ, Kapazität 62 Ah (62%)
- Batterie 2 (2016): Ri = 14 mΩ, Kapazität 55 Ah (55%)
- Batterie 3 (2023): Ri = 5 mΩ, Kapazität 98 Ah (98%)

**Problem:** Beim Entladen liefert Batterie 3 den Großteil des Stroms (niedrigster Ri), beim Laden nimmt sie den meisten Strom auf. Die alten Batterien werden nur marginal ge-/entladen → Sulfatierung schreitet fort.

**Lösung:**
- ALLE drei Batterien gleichzeitig ersetzt durch 2× Victron AGM Super Cycle 170 Ah
- Alternativ-Empfehlung: 1× LiFePO4 200 Ah (gleiche nutzbare Kapazität, weniger Gewicht)

**Lernpunkt:** Niemals eine einzelne Batterie in einem Parallel-Verbund austauschen. Immer alle gleichzeitig ersetzen.

---

### ANHANG G — Fallstudie: BMS-Kommunikationsproblem Victron-System

**Yacht:** Hanse 548 (2022), 12V Victron-Vollsystem
**Problem:** Cerbo GX zeigt sporadisch „Battery Communication Lost", Ladegerät fällt in Safe-Mode (niedrige Ladespannung → chronische Unterladung)

**Systemaufbau:**
- 2× Victron Lithium Smart 200 Ah (parallel)
- VE.Bus BMS v2
- Cerbo GX + Touch 50
- MultiPlus-II 12/3000/120
- 2× SmartSolar MPPT 150/35

**Diagnose:**
1. VE.Bus-Kabel zwischen BMS und Cerbo: OK (Widerstand <0,1 Ω)
2. RJ45-Stecker am BMS: Sichtbar oxidiert (Salzwassernebel im Elektrikschrank)
3. CAN-Bus Terminierung: Fehlte am letzten Gerät (120 Ω)
4. EMV: Radar-Pulser neben Elektrikschrank → sporadische Störungen

**Maßnahmen:**
1. Alle RJ45-Stecker ersetzt (vergoldete Stecker, IP67-Verschraubungen)
2. 120 Ω Terminierungswiderstand am CAN-Bus-Ende installiert
3. Geschirmtes CAN-Bus-Kabel verlegt (statt Standard-UTP)
4. EMV-Ferrite auf VE.Bus-Leitung am Radar-Näherungsbereich
5. Firmware-Update aller Geräte auf aktuelle Version

**Ergebnis:** Seit 14 Monaten kein Kommunikationsfehler mehr.

**AYDI-Bewertung (Elektrik-Modul):**
- Vor Maßnahme: 55/100 (Kommunikation instabil, Ladung beeinträchtigt)
- Nach Maßnahme: 93/100

---

### ANHANG H — Fallstudie: Natrium-Ionen-Pilotinstallation auf einem Forschungskatamaran

**Yacht:** Custom Research Catamaran „Polarwind" (2024), 22m, 48V-System
**Einsatzgebiet:** Arktische Gewässer (Spitzbergen, Grönland), Forschungsreisen

**Herausforderung:** Standardmäßige LiFePO4 kann nicht unter 0°C geladen werden → problematisch in arktischen Gewässern mit Temperaturen bis −25°C

**Lösung: Natrium-Ionen-Pilotinstallation**
- Hersteller: HiNa Battery (China), 48V/100 Ah Module
- 4× 48V/100 Ah = 19,2 kWh Speicherkapazität
- Ladebar ab −20°C (Hauptvorteil gegenüber LiFePO4!)
- BMS: Custom-Entwicklung mit CAN-Bus

**Vergleich mit LiFePO4-Alternative:**

| Parameter | Na-Ion (installiert) | LiFePO4 (Alternative) |
|-----------|---------------------|----------------------|
| Kapazität | 19,2 kWh | 19,2 kWh |
| Gewicht | 240 kg | 140 kg |
| Volumen | 200 l | 130 l |
| Ladetemperatur min. | −20°C | 0°C (mit Heizung: −10°C) |
| Zyklen (80% DoD) | 3.500 | 5.000 |
| Kosten | €8.500 | €12.000 |

**Ergebnis nach 1 Saison (Juni–Oktober 2025):**
- 85 Ladezyklen bei <0°C Außentemperatur ohne Heizung (!)
- Keine Degradation messbar
- Energiedichte: akzeptabel für Forschungs-Katamaran (Gewicht unkritisch)
- BMS-Integration: Stabil nach anfänglichen Firmware-Problemen

**Bewertung:**
- Na-Ion ist vielversprechend für Kälte-Anwendungen
- Noch nicht Mainstream (begrenzte Verfügbarkeit, kurze Track Record)
- Für Standard-Marine-Anwendungen in gemäßigten Breiten: LiFePO4 bleibt überlegen

**Confidence:** estimated — Pilotprojekt, keine Langzeitdaten (>3 Jahre) verfügbar.

### ANHANG H.2 — Berechnungsbeispiele für die Praxis

#### Beispiel 1: Peukert-Effekt bei Ankerwinden-Betrieb

**Situation:** 12V AGM-Batterie 100 Ah (k=1,15), Ankerwinde zieht 80 A für 5 Minuten.
```
Nominaler Strom (C/20): I_nom = 100/20 = 5 A
Peukert-Zeit: t = 20 × (5/80)^1,15 = 20 × 0,0625^1,15 = 20 × 0,0428 = 0,856 h
Effektive Kapazität bei 80 A: C_eff = 80 × 0,856 = 68,5 Ah
Kapazitätsverlust: (100 − 68,5) / 100 = 31,5%
Tatsächlich entnommen in 5 min: 80 × (5/60) = 6,67 Ah
SoC-Reduktion: 6,67 / 68,5 = 9,7% (nicht 6,67% wie naiv berechnet!)
```

→ Bei hohen Strömen ist der effektive DoD deutlich höher als der nominelle!

#### Beispiel 2: Temperaturkorrektur der Ladespannung

**Situation:** AGM-Batterie im Maschinenraum, Temperatur 45°C (statt 25°C Referenz).
```
Temperaturkompensation: −3 mV/°C pro Zelle × 6 Zellen = −18 mV/°C (Gesamt)
ΔT = 45°C − 25°C = +20°C
Spannungskorrektur: −18 mV/°C × 20°C = −360 mV = −0,36 V

Absorption (25°C): 14,40 V
Absorption (45°C): 14,40 − 0,36 = 14,04 V

Float (25°C): 13,60 V
Float (45°C): 13,60 − 0,36 = 13,24 V
```

→ Ohne Temperaturkompensation wird die Batterie bei 45°C mit 0,36V zu viel geladen = Überladung!

#### Beispiel 3: Bankdimensionierung für 24V-Motoryacht

**Situation:** 14m Motoryacht, 24V-System, 3 Tage Ankerlieger ohne Generator.
```
Tagesverbrauch: 4.200 Wh = 175 Ah bei 24V
Autonomie: 3 Tage = 525 Ah Entnahme
Technologie: LiFePO4, max. DoD 80%
Erforderlich: 525 / 0,80 = 656 Ah bei 24V

Empfehlung: 2× Mastervolt MLI Ultra 24/2750 (je 110 Ah) = 220 Ah
... zu wenig! → 4× MLI Ultra 24/2750 parallel = 440 Ah
... immer noch zu wenig! → 3× MLI Ultra 24/5500 (je 220 Ah) = 660 Ah ✓

Gewicht: 3 × 50 kg = 150 kg
Kosten: 3 × €6.500 = €19.500

Alternative (günstiger): 4× Victron Smart 25,6V/200Ah = 800 Ah
Gewicht: 4 × 50 kg = 200 kg
Kosten: 4 × €4.800 = €19.200
```

#### Beispiel 4: Solar-Lade-Berechnung für Ankerlieger

**Situation:** 12V-System, 400 Wp Solar (MPPT), LiFePO4 400 Ah, Mallorca (Juli).
```
Solar-Einstrahlung Mallorca Juli: 6,5 kWh/m²/Tag (Peak Sun Hours)
Panel-Effizienz (Temperatur, Winkel, Verschmutzung): 75%
MPPT-Effizienz: 95%
Kabel-/Systemverluste: 95%

Erwarteter Ertrag: 400 Wp × 6,5 h × 0,75 × 0,95 × 0,95 = 1.762 Wh/Tag
In Ah (12V): 1.762 / 13,0 V (durchschnittliche Ladespannung) = 135 Ah/Tag

Tagesverbrauch (Ankerlieger): 180 Ah/Tag
Defizit: 180 − 135 = 45 Ah/Tag

→ Bei 400 Ah Bank und 80% DoD: 320 Ah nutzbar
→ Autonomie ohne Nachladen: 320 / 45 = 7,1 Tage
→ Danach: Motor/Generator 1h = ca. 80 Ah über Lichtmaschine + Orion-Tr
```

#### Beispiel 5: Kosten pro kWh über Lebenszyklus

**Vergleich: AGM vs. LiFePO4 für identischen Nutzen (200 Ah nutzbar, 12V)**

| Parameter | AGM (2× 200 Ah) | LiFePO4 (1× 250 Ah) |
|-----------|-----------------|---------------------|
| Anschaffung | €800 | €1.500 |
| Nutzbar (50% vs. 80% DoD) | 200 Ah | 200 Ah |
| Energie nutzbar | 2.400 Wh | 2.560 Wh |
| Zyklen (50%/80% DoD) | 800 | 3.500 |
| Gesamt-Energie über Lebenszeit | 800 × 2,4 kWh = 1.920 kWh | 3.500 × 2,56 kWh = 8.960 kWh |
| Kosten/kWh | €800 / 1.920 = **€0,42/kWh** | €1.500 / 8.960 = **€0,17/kWh** |
| 20 Jahre (200 Zyklen/Jahr) | 5 Sätze = €4.000 | 1,1 Sätze = €1.700 |

→ LiFePO4 ist über die Lebensdauer **2,5× günstiger** pro gelieferter kWh!

---

## ANHANG I–R — AYDI-Integration (Pydantic v2 Modelle)

### ANHANG I — Basis-Modelle

```python
"""
AYDI Battery Module — Base Models
Grundlegende Datenstrukturen für das Batterie-Analyse-Modul.
"""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class ConfidenceLevel(str, Enum):
    """Confidence levels for AYDI analysis results."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class BatteryChemistry(str, Enum):
    """Batteriechemie-Typen."""
    FLOODED_LEAD_ACID = "flooded_lead_acid"
    AGM = "agm"
    GEL = "gel"
    LIFEPO4 = "lifepo4"
    LTO = "lto"
    SODIUM_ION = "sodium_ion"
    UNKNOWN = "unknown"


class BatteryPurpose(str, Enum):
    """Verwendungszweck der Batterie."""
    STARTER = "starter"
    HOUSE_SUPPLY = "house_supply"
    DUAL_PURPOSE = "dual_purpose"
    BOW_THRUSTER = "bow_thruster"
    ELECTRIC_PROPULSION = "electric_propulsion"
    EMERGENCY = "emergency"


class BatteryCondition(str, Enum):
    """Zustandsbewertung einer Batterie."""
    EXCELLENT = "excellent"        # SoH >95%
    GOOD = "good"                  # SoH 85-95%
    FAIR = "fair"                  # SoH 75-85%
    POOR = "poor"                  # SoH 60-75%
    END_OF_LIFE = "end_of_life"    # SoH <60%
    DEFECTIVE = "defective"        # Akuter Defekt
    DANGEROUS = "dangerous"        # Sicherheitsrisiko


class Severity(str, Enum):
    """Schweregrad eines Befundes."""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


class SystemVoltage(str, Enum):
    """Bordnetz-Systemspannung."""
    V12 = "12V"
    V24 = "24V"
    V48 = "48V"


class BatterySpecification(BaseModel):
    """Spezifikation einer einzelnen Batterie."""
    model_config = {"from_attributes": True}

    manufacturer: str = Field(..., description="Hersteller")
    model: str = Field(..., description="Modellbezeichnung")
    chemistry: BatteryChemistry
    purpose: BatteryPurpose
    nominal_voltage: float = Field(..., gt=0, description="Nennspannung in Volt")
    nominal_capacity_ah: float = Field(..., gt=0, description="Nennkapazität in Ah (C/20)")
    weight_kg: Optional[float] = Field(None, gt=0, description="Gewicht in kg")
    dimensions_mm: Optional[tuple[float, float, float]] = Field(
        None, description="Abmessungen L×B×H in mm"
    )
    max_discharge_current_a: Optional[float] = Field(None, gt=0)
    max_charge_current_a: Optional[float] = Field(None, gt=0)
    cycle_life_50_dod: Optional[int] = Field(None, gt=0, description="Zyklen bei 50% DoD")
    cycle_life_80_dod: Optional[int] = Field(None, gt=0, description="Zyklen bei 80% DoD")
    has_bms: bool = Field(False, description="Integriertes BMS vorhanden")
    bms_communication: Optional[str] = Field(None, description="BMS-Kommunikationsprotokoll")
    ip_rating: Optional[str] = Field(None, description="IP-Schutzklasse")
    operating_temp_min_c: float = Field(-20, description="Min. Betriebstemperatur °C")
    operating_temp_max_c: float = Field(60, description="Max. Betriebstemperatur °C")
    charge_temp_min_c: float = Field(0, description="Min. Ladetemperatur °C")
    charge_temp_max_c: float = Field(45, description="Max. Ladetemperatur °C")
    price_eur: Optional[float] = Field(None, ge=0, description="Preis in EUR (ca.)")
    confidence: ConfidenceLevel = Field(
        default=ConfidenceLevel.DOCUMENTED,
        description="Konfidenz der Spezifikationsdaten"
    )


class BatteryBankConfiguration(BaseModel):
    """Konfiguration einer Batteriebank (mehrere Batterien)."""
    model_config = {"from_attributes": True}

    bank_id: str = Field(..., description="Eindeutige ID der Batteriebank")
    purpose: BatteryPurpose
    system_voltage: SystemVoltage
    batteries: list[BatterySpecification] = Field(..., min_length=1)
    series_count: int = Field(1, ge=1, description="Anzahl in Serie")
    parallel_count: int = Field(1, ge=1, description="Anzahl parallel")
    total_capacity_ah: float = Field(..., gt=0, description="Gesamtkapazität in Ah")
    usable_capacity_ah: float = Field(..., gt=0, description="Nutzbare Kapazität in Ah")
    total_energy_wh: float = Field(..., gt=0, description="Gesamtenergie in Wh")
    total_weight_kg: Optional[float] = Field(None, gt=0)
    max_dod_percent: float = Field(..., gt=0, le=100, description="Max. empfohlene DoD in %")
    installation_year: Optional[int] = Field(None, ge=1990, le=2030)
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.ESTIMATED)
```

### ANHANG J — Befund-Modelle

```python
"""
AYDI Battery Module — Finding Models
Befund- und Fehlerbild-Modelle für die Batterie-Analyse.
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from .battery_base_models import (
    BatteryChemistry,
    ConfidenceLevel,
    Severity,
)


class BatteryFinding(BaseModel):
    """Ein einzelner Befund aus der Batterie-Analyse."""
    model_config = {"from_attributes": True}

    finding_id: str = Field(..., description="Eindeutige Befund-ID")
    title_de: str = Field(..., description="Befund-Titel auf Deutsch")
    description_de: str = Field(..., description="Beschreibung auf Deutsch")
    severity: Severity
    category: str = Field(..., description="Fehlerbild-Kategorie (z.B. 'sulfatierung')")
    affected_chemistry: list[BatteryChemistry] = Field(
        default_factory=list, description="Betroffene Batteriechemien"
    )
    location_reference: Optional[str] = Field(
        None, description="Ort des Befundes (z.B. 'Steuerbord-Batteriebank')"
    )
    measured_value: Optional[str] = Field(None, description="Gemessener Wert")
    expected_value: Optional[str] = Field(None, description="Erwarteter/Sollwert")
    recommendation_de: str = Field(..., description="Empfehlung auf Deutsch")
    estimated_cost_eur: Optional[float] = Field(None, ge=0, description="Geschätzte Kosten")
    urgency_days: Optional[int] = Field(
        None, ge=0, description="Empfohlene Behebung innerhalb X Tagen"
    )
    confidence: ConfidenceLevel
    visual_evidence: bool = Field(False, description="Visueller Nachweis vorhanden")
    requires_professional: bool = Field(False, description="Fachperson erforderlich")


class BatterySafetyFinding(BaseModel):
    """Sicherheitsrelevanter Befund — erfordert sofortige Aufmerksamkeit."""
    model_config = {"from_attributes": True}

    finding_id: str = Field(..., description="Eindeutige Befund-ID")
    title_de: str = Field(..., description="Sicherheitsbefund-Titel")
    description_de: str = Field(..., description="Beschreibung der Gefährdung")
    severity: Severity = Field(Severity.CRITICAL, description="Immer CRITICAL")
    risk_type: str = Field(..., description="Risikotyp: brand, explosion, vergiftung, stromschlag")
    immediate_action_de: str = Field(
        ..., description="Sofortmaßnahme auf Deutsch"
    )
    affected_bank_id: Optional[str] = Field(None)
    confidence: ConfidenceLevel
    human_verification_required: bool = Field(
        True, description="'Befund prüfen' — Human-in-the-Loop"
    )


class BatteryFindingCollection(BaseModel):
    """Sammlung aller Befunde einer Batterie-Analyse."""
    model_config = {"from_attributes": True}

    findings: list[BatteryFinding] = Field(default_factory=list)
    safety_findings: list[BatterySafetyFinding] = Field(default_factory=list)
    total_findings: int = Field(0, ge=0)
    critical_count: int = Field(0, ge=0)
    high_count: int = Field(0, ge=0)
    medium_count: int = Field(0, ge=0)
    low_count: int = Field(0, ge=0)
    info_count: int = Field(0, ge=0)
```

### ANHANG K — Scoring-Modelle

```python
"""
AYDI Battery Module — Scoring Models
Score-Berechnung und Fusion für das Batterie-Modul.
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from .battery_base_models import ConfidenceLevel


class BatteryStructuredScore(BaseModel):
    """Strukturelle Bewertung (Pipeline A) des Batterie-Moduls."""
    model_config = {"from_attributes": True}

    capacity_adequacy_score: int = Field(
        ..., ge=0, le=100, description="Kapazität ausreichend für Nutzungsprofil"
    )
    chemistry_appropriateness_score: int = Field(
        ..., ge=0, le=100, description="Batteriechemie passend zum Einsatzprofil"
    )
    charging_profile_score: int = Field(
        ..., ge=0, le=100, description="Ladeprofil korrekt konfiguriert"
    )
    state_of_health_score: int = Field(
        ..., ge=0, le=100, description="Gesundheitszustand (SoH)"
    )
    installation_compliance_score: int = Field(
        ..., ge=0, le=100, description="Installation normkonform (ISO 10133, ABYC E-10)"
    )
    bms_functionality_score: Optional[int] = Field(
        None, ge=0, le=100, description="BMS-Funktionalität (nur LiFePO4)"
    )
    monitoring_score: int = Field(
        ..., ge=0, le=100, description="Überwachung und Monitoring"
    )
    safety_score: int = Field(
        ..., ge=0, le=100, description="Sicherheit (Absicherung, Belüftung, Befestigung)"
    )
    redundancy_score: int = Field(
        ..., ge=0, le=100, description="Redundanz und Ausfallsicherheit"
    )

    overall_structured_score: int = Field(..., ge=0, le=100)
    confidence: ConfidenceLevel


class BatteryVisualScore(BaseModel):
    """Visuelle Bewertung (Pipeline B) des Batterie-Moduls."""
    model_config = {"from_attributes": True}

    physical_condition_score: int = Field(
        ..., ge=0, le=100, description="Äußerer Zustand (Gehäuse, Pole, Korrosion)"
    )
    installation_quality_score: int = Field(
        ..., ge=0, le=100, description="Installationsqualität visuell"
    )
    cable_connection_score: int = Field(
        ..., ge=0, le=100, description="Kabelanschlüsse (Ordnung, Korrosion)"
    )
    labeling_score: int = Field(
        ..., ge=0, le=100, description="Beschriftung und Kennzeichnung"
    )
    ventilation_score: int = Field(
        ..., ge=0, le=100, description="Belüftung visuell beurteilbar"
    )
    safety_visual_score: int = Field(
        ..., ge=0, le=100, description="Sicherheitsmerkmale visuell (Sicherungen, Schalter)"
    )

    overall_visual_score: int = Field(..., ge=0, le=100)
    confidence: ConfidenceLevel


class BatteryModuleFusedScore(BaseModel):
    """Fusionierter Score für das Batterie-Modul."""
    model_config = {"from_attributes": True}

    structured_score: Optional[BatteryStructuredScore] = None
    visual_score: Optional[BatteryVisualScore] = None

    # Fusionsgewichte — Batterien sind primär strukturell bewertbar
    structured_weight: float = Field(default=0.75)
    visual_weight: float = Field(default=0.25)

    fused_score: int = Field(..., ge=0, le=100)
    confidence: ConfidenceLevel

    critical_findings_count: int = Field(0, ge=0)
    high_findings_count: int = Field(0, ge=0)
    medium_findings_count: int = Field(0, ge=0)

    summary_de: str = Field(..., description="Zusammenfassung auf Deutsch")
    top_recommendations: list[str] = Field(
        default_factory=list, description="Top-3 Empfehlungen, priorisiert"
    )
    estimated_remaining_life_years: Optional[float] = Field(
        None, ge=0, description="Geschätzte Restlebensdauer in Jahren"
    )
    estimated_replacement_cost_eur: Optional[float] = Field(
        None, ge=0, description="Geschätzte Austauschkosten in EUR"
    )
```

### ANHANG L — Kapazitätsberechnung

```python
"""
AYDI Battery Module — Capacity Calculation
Kapazitätsberechnung und Dimensionierung der Batteriebank.
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from .battery_base_models import (
    BatteryChemistry,
    ConfidenceLevel,
    SystemVoltage,
)


class EnergyConsumer(BaseModel):
    """Ein einzelner Verbraucher in der Energiebilanz."""
    model_config = {"from_attributes": True}

    name_de: str = Field(..., description="Verbraucher-Bezeichnung auf Deutsch")
    power_watts: float = Field(..., gt=0, description="Leistungsaufnahme in Watt")
    hours_per_day: float = Field(..., ge=0, le=24, description="Betriebsstunden pro Tag")
    quantity: int = Field(1, ge=1, description="Anzahl identischer Verbraucher")
    is_critical: bool = Field(False, description="Sicherheitskritischer Verbraucher")
    daily_energy_wh: float = Field(
        ..., gt=0, description="Täglicher Energiebedarf in Wh (berechnet)"
    )


class EnergyBudget(BaseModel):
    """Vollständige Energiebilanz einer Yacht."""
    model_config = {"from_attributes": True}

    consumers: list[EnergyConsumer] = Field(..., min_length=1)
    total_daily_wh: float = Field(..., gt=0, description="Tagesverbrauch gesamt in Wh")
    total_daily_ah: float = Field(..., gt=0, description="Tagesverbrauch in Ah")
    system_voltage: SystemVoltage
    safety_margin_percent: float = Field(
        20.0, ge=0, le=100, description="Sicherheitszuschlag in %"
    )
    total_with_margin_wh: float = Field(..., gt=0, description="Mit Sicherheitszuschlag")
    confidence: ConfidenceLevel


class BatteryBankSizing(BaseModel):
    """Ergebnis der Bankdimensionierung."""
    model_config = {"from_attributes": True}

    energy_budget: EnergyBudget
    autonomy_days: float = Field(..., gt=0, description="Gewünschte Autonomie in Tagen")
    target_chemistry: BatteryChemistry
    max_dod_percent: float = Field(..., gt=0, le=100)
    required_capacity_ah: float = Field(
        ..., gt=0, description="Erforderliche Bankkapazität in Ah"
    )
    required_energy_wh: float = Field(
        ..., gt=0, description="Erforderliche Bankenergie in Wh"
    )
    recommended_products: list[str] = Field(
        default_factory=list, description="Empfohlene Produkte"
    )
    estimated_weight_kg: Optional[float] = Field(None, gt=0)
    estimated_cost_eur: Optional[float] = Field(None, gt=0)
    confidence: ConfidenceLevel


class PeukertCalculation(BaseModel):
    """Peukert-Effekt-Berechnung für Blei-Säure."""
    model_config = {"from_attributes": True}

    nominal_capacity_ah: float = Field(..., gt=0, description="Nennkapazität (C/20)")
    peukert_exponent: float = Field(
        ..., gt=1.0, le=2.0, description="Peukert-Exponent k"
    )
    discharge_current_a: float = Field(..., gt=0, description="Tatsächlicher Entladestrom")
    effective_capacity_ah: float = Field(
        ..., gt=0, description="Effektive Kapazität bei gegebenem Strom"
    )
    capacity_loss_percent: float = Field(
        ..., ge=0, le=100, description="Kapazitätsverlust durch Peukert in %"
    )
    runtime_hours: float = Field(..., gt=0, description="Tatsächliche Laufzeit in Stunden")
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.CALCULATED)
```

### ANHANG M — Ladeprofil-Modelle

```python
"""
AYDI Battery Module — Charging Profile Models
Ladeprofil-Konfiguration und -Analyse.
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from .battery_base_models import BatteryChemistry, ConfidenceLevel, Severity


class ChargingProfile(BaseModel):
    """Ladeprofil-Konfiguration eines Ladegeräts."""
    model_config = {"from_attributes": True}

    profile_name: str = Field(..., description="Profilbezeichnung")
    target_chemistry: BatteryChemistry
    system_voltage_v: float = Field(..., gt=0, description="Systemspannung (12/24/48)")
    bulk_current_a: float = Field(..., gt=0, description="Bulk-Ladestrom in A")
    absorption_voltage_v: float = Field(..., gt=0, description="Absorptionsspannung in V")
    absorption_time_min: int = Field(
        ..., gt=0, description="Max. Absorptionszeit in Minuten"
    )
    float_voltage_v: Optional[float] = Field(
        None, gt=0, description="Float-Spannung in V (None = kein Float)"
    )
    equalization_voltage_v: Optional[float] = Field(
        None, gt=0, description="Equalization-Spannung (nur Nass-Blei)"
    )
    equalization_time_min: Optional[int] = Field(
        None, gt=0, description="Equalization-Dauer in Minuten"
    )
    tail_current_a: float = Field(
        ..., gt=0, description="Tail Current (Ende Absorption) in A"
    )
    temperature_compensation_mv_per_c: Optional[float] = Field(
        None, description="Temperaturkompensation mV/°C (pro Zelle)"
    )
    low_temp_cutoff_c: Optional[float] = Field(
        None, description="Lade-Abschaltung unter dieser Temperatur"
    )


class ChargingProfileAnalysis(BaseModel):
    """Analyse eines bestehenden Ladeprofils vs. Batteriechemie."""
    model_config = {"from_attributes": True}

    profile: ChargingProfile
    actual_battery_chemistry: BatteryChemistry
    is_compatible: bool = Field(
        ..., description="Profil kompatibel mit installierter Batterie?"
    )
    compatibility_issues: list[str] = Field(
        default_factory=list, description="Gefundene Kompatibilitätsprobleme"
    )
    severity: Severity = Field(
        Severity.INFO, description="Schweregrad der Inkompatibilität"
    )
    recommendation_de: str = Field(..., description="Empfehlung auf Deutsch")
    optimal_absorption_v: float = Field(..., gt=0, description="Optimale Absorptionsspannung")
    optimal_float_v: Optional[float] = Field(None, gt=0, description="Optimale Float-Spannung")
    confidence: ConfidenceLevel


class ChargingSourceInventory(BaseModel):
    """Inventar aller Ladequellen an Bord."""
    model_config = {"from_attributes": True}

    shore_charger: Optional[ChargingProfile] = Field(
        None, description="Landstrom-Ladegerät"
    )
    alternator_output_a: Optional[float] = Field(
        None, gt=0, description="Lichtmaschinen-Ladestrom"
    )
    alternator_regulator: Optional[str] = Field(
        None, description="Typ des Ladereglers (intern/extern/smart)"
    )
    solar_wp: Optional[float] = Field(None, ge=0, description="Solar-Leistung in Wp")
    solar_controller_type: Optional[str] = Field(
        None, description="MPPT oder PWM"
    )
    solar_controller_profile: Optional[ChargingProfile] = None
    wind_generator_w: Optional[float] = Field(
        None, ge=0, description="Windgenerator-Leistung in W"
    )
    hydro_generator_w: Optional[float] = Field(
        None, ge=0, description="Hydrogenerator-Leistung in W"
    )
    diesel_generator_kw: Optional[float] = Field(
        None, gt=0, description="Dieselgenerator-Leistung in kW"
    )
    dc_dc_charger: Optional[ChargingProfile] = Field(
        None, description="DC-DC-Ladebooster (B2B)"
    )
    total_max_charge_current_a: float = Field(
        ..., gt=0, description="Max. Gesamtladestrom aller Quellen"
    )
    charge_coordination: Optional[str] = Field(
        None, description="Art der Ladekoordination (BMS, Prioritäts-Relais, unkoordiniert)"
    )
    confidence: ConfidenceLevel
```

### ANHANG N — BMS-Analyse-Modelle

```python
"""
AYDI Battery Module — BMS Analysis Models
BMS-Bewertung und Kommunikations-Analyse.
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from .battery_base_models import ConfidenceLevel, Severity


class BMSSpecification(BaseModel):
    """Spezifikation eines Battery Management Systems."""
    model_config = {"from_attributes": True}

    manufacturer: str = Field(..., description="BMS-Hersteller")
    model: str = Field(..., description="BMS-Modell")
    cell_count: int = Field(..., ge=1, le=32, description="Überwachte Zellenanzahl")
    max_continuous_current_a: float = Field(..., gt=0)
    max_peak_current_a: Optional[float] = Field(None, gt=0)
    overvoltage_cutoff_v: float = Field(..., gt=0, description="Überspannungs-Abschaltung pro Zelle")
    undervoltage_cutoff_v: float = Field(..., gt=0, description="Unterspannungs-Abschaltung pro Zelle")
    overtemp_cutoff_c: float = Field(..., description="Übertemperatur-Abschaltung °C")
    undertemp_charge_cutoff_c: float = Field(..., description="Lade-Sperre unter °C")
    balancing_type: str = Field(..., description="passive oder active")
    balancing_current_ma: float = Field(..., gt=0, description="Balancer-Strom in mA")
    communication_protocols: list[str] = Field(
        default_factory=list, description="Kommunikationsprotokolle (Bluetooth, CAN, VE.Bus...)"
    )
    has_temperature_sensors: bool = Field(True)
    temperature_sensor_count: int = Field(1, ge=0)
    has_precharge: bool = Field(False, description="Vorlade-Schaltung für kapazitive Lasten")
    firmware_version: Optional[str] = Field(None)
    confidence: ConfidenceLevel


class BMSHealthCheck(BaseModel):
    """Ergebnis einer BMS-Gesundheitsprüfung."""
    model_config = {"from_attributes": True}

    bms_spec: BMSSpecification
    cell_voltages_v: list[float] = Field(
        ..., min_length=1, description="Aktuelle Zellenspannungen"
    )
    cell_voltage_delta_mv: float = Field(
        ..., ge=0, description="Max. Spannungsdifferenz zwischen Zellen in mV"
    )
    cell_balance_status: str = Field(
        ..., description="'balanced' (<30mV), 'slight_imbalance' (30-100mV), 'imbalanced' (>100mV)"
    )
    temperature_readings_c: list[float] = Field(
        default_factory=list, description="Temperatursensor-Werte"
    )
    total_cycles: Optional[int] = Field(None, ge=0)
    error_history_count: int = Field(0, ge=0, description="Gespeicherte Fehlerereignisse")
    last_error_type: Optional[str] = Field(None)
    communication_stable: bool = Field(True)
    firmware_up_to_date: bool = Field(True)
    overall_bms_health: int = Field(..., ge=0, le=100, description="BMS-Gesundheits-Score")
    findings: list[str] = Field(default_factory=list, description="Befunde auf Deutsch")
    confidence: ConfidenceLevel
```

### ANHANG O — Visuelle Analyse (Pipeline B)

```python
"""
AYDI Battery Module — Visual Analysis Models
Modelle für die visuelle Analyse (Claude Vision Pipeline B).
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from .battery_base_models import (
    BatteryChemistry,
    BatteryCondition,
    ConfidenceLevel,
    Severity,
)


class BatteryVisualObservation(BaseModel):
    """Einzelne visuelle Beobachtung aus einem Foto."""
    model_config = {"from_attributes": True}

    observation_id: str = Field(..., description="Eindeutige Beobachtungs-ID")
    description_de: str = Field(..., description="Beschreibung auf Deutsch")
    category: str = Field(
        ..., description="Kategorie: gehaeuse, pole, kabel, installation, label, umgebung"
    )
    severity: Severity
    indicator_of: Optional[str] = Field(
        None, description="Fehlerbild, auf das diese Beobachtung hinweist"
    )
    confidence: ConfidenceLevel
    bounding_box: Optional[tuple[float, float, float, float]] = Field(
        None, description="Relative Position im Bild (x1, y1, x2, y2) 0-1"
    )


class BatteryVisualAnalysisResult(BaseModel):
    """Gesamtergebnis der visuellen Batterie-Analyse."""
    model_config = {"from_attributes": True}

    image_quality: str = Field(
        ..., description="Bildqualität: excellent, good, fair, poor, insufficient"
    )
    detected_chemistry: Optional[BatteryChemistry] = Field(
        None, description="Erkannte Batteriechemie (aus Label/Gehäuse)"
    )
    detected_manufacturer: Optional[str] = Field(None, description="Erkannter Hersteller")
    detected_model: Optional[str] = Field(None, description="Erkanntes Modell")
    estimated_age_years: Optional[float] = Field(
        None, ge=0, description="Geschätztes Alter in Jahren"
    )
    overall_visual_condition: BatteryCondition
    observations: list[BatteryVisualObservation] = Field(default_factory=list)
    swelling_detected: bool = Field(False, description="Aufblähen erkannt (KRITISCH)")
    corrosion_detected: bool = Field(False, description="Korrosion an Polen/Klemmen")
    leakage_detected: bool = Field(False, description="Elektrolytaustritt erkannt")
    installation_issues: list[str] = Field(
        default_factory=list, description="Installationsmängel"
    )
    overall_visual_score: int = Field(..., ge=0, le=100)
    confidence: ConfidenceLevel
    nicht_beurteilbar_reasons: list[str] = Field(
        default_factory=list,
        description="Gründe warum Aspekte nicht beurteilt werden können"
    )


# Vision Prompt Template (für Claude Vision API)
BATTERY_VISUAL_ANALYSIS_PROMPT = """
Analysiere dieses Foto einer Bootsbatterie / Batterieinstallation.

Beurteile folgende Aspekte:
1. GEHÄUSE: Verformung, Aufblähen, Risse, Verfärbungen
2. POLE/KLEMMEN: Korrosion (weiß/grün/blau), lockere Verbindungen, fehlender Schutz
3. KABEL: Querschnitt angemessen, Zustand, Anschlussqualität
4. INSTALLATION: Befestigung, Belüftung, Säureschutz, Zugänglichkeit
5. BESCHRIFTUNG: Hersteller, Typ, Baujahr erkennbar
6. UMGEBUNG: Feuchtigkeit, Temperatur (Standort), Ordnung

Bei Unklarheit: 'nicht beurteilbar' mit Begründung angeben.
Schweregrad-Einschätzung für jeden Befund.
Antwort auf Deutsch, strukturiert nach den 6 Kategorien.
"""
```

### ANHANG P — Lebenszyklus-Modelle

```python
"""
AYDI Battery Module — Lifecycle Models
Lebenszyklus-Analyse, Alterungsprognose, Kostenberechnung.
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from .battery_base_models import BatteryChemistry, ConfidenceLevel


class BatteryAgingModel(BaseModel):
    """Modell für die Alterungsprognose einer Batterie."""
    model_config = {"from_attributes": True}

    chemistry: BatteryChemistry
    initial_capacity_ah: float = Field(..., gt=0)
    current_capacity_ah: float = Field(..., gt=0)
    current_soh_percent: float = Field(..., ge=0, le=100)
    age_months: int = Field(..., ge=0)
    total_cycles: Optional[int] = Field(None, ge=0)
    average_dod_percent: float = Field(..., gt=0, le=100)
    average_temperature_c: float = Field(25.0)
    estimated_remaining_cycles: int = Field(..., ge=0)
    estimated_remaining_months: int = Field(..., ge=0)
    estimated_eol_date: Optional[str] = Field(
        None, description="Geschätztes End-of-Life Datum (YYYY-MM)"
    )
    degradation_rate_percent_per_year: float = Field(
        ..., ge=0, description="Jährliche Degradationsrate in %"
    )
    confidence: ConfidenceLevel


class BatteryLifecycleCost(BaseModel):
    """20-Jahres-Lebenszykluskosten-Analyse."""
    model_config = {"from_attributes": True}

    chemistry: BatteryChemistry
    initial_purchase_eur: float = Field(..., ge=0)
    installation_cost_eur: float = Field(0, ge=0)
    annual_maintenance_cost_eur: float = Field(0, ge=0)
    expected_lifetime_years: float = Field(..., gt=0)
    replacements_in_20_years: int = Field(..., ge=0)
    total_replacement_cost_eur: float = Field(0, ge=0)
    total_20_year_cost_eur: float = Field(..., ge=0)
    cost_per_kwh_delivered_eur: float = Field(
        ..., ge=0, description="Kosten pro gelieferter kWh über Lebensdauer"
    )
    cost_per_cycle_eur: float = Field(
        ..., ge=0, description="Kosten pro Zyklus"
    )
    weight_penalty_factor: float = Field(
        1.0, ge=0, description="Gewichts-Mehrkosten-Faktor (Segelyachten)"
    )
    confidence: ConfidenceLevel


class LifecycleComparison(BaseModel):
    """Vergleich der Lebenszykluskosten verschiedener Technologien."""
    model_config = {"from_attributes": True}

    target_usable_capacity_ah: float = Field(..., gt=0)
    system_voltage_v: float = Field(..., gt=0)
    annual_cycles: int = Field(..., gt=0)
    average_dod_percent: float = Field(..., gt=0, le=100)
    options: list[BatteryLifecycleCost] = Field(..., min_length=2)
    recommended_option: str = Field(
        ..., description="Empfohlene Technologie mit Begründung"
    )
    break_even_years: Optional[float] = Field(
        None, ge=0, description="Break-Even Lithium vs. Blei in Jahren"
    )
    confidence: ConfidenceLevel
```

### ANHANG Q — Temperatur- und Sicherheitsmodelle

```python
"""
AYDI Battery Module — Temperature and Safety Models
Temperaturmanagement und Sicherheitsanalyse.
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from .battery_base_models import BatteryChemistry, ConfidenceLevel, Severity


class TemperatureAssessment(BaseModel):
    """Temperatur-Bewertung des Batterie-Standorts."""
    model_config = {"from_attributes": True}

    location_description: str = Field(
        ..., description="Standort-Beschreibung (z.B. 'Maschinenraum Steuerbord')"
    )
    ambient_temp_min_c: float = Field(..., description="Min. Umgebungstemperatur °C")
    ambient_temp_max_c: float = Field(..., description="Max. Umgebungstemperatur °C")
    ambient_temp_avg_c: float = Field(..., description="Durchschn. Umgebungstemperatur °C")
    near_engine: bool = Field(False, description="In der Nähe des Motors")
    direct_sun_exposure: bool = Field(False, description="Direkte Sonneneinstrahlung")
    ventilation_adequate: bool = Field(True, description="Belüftung ausreichend")
    battery_chemistry: BatteryChemistry
    temperature_risk_level: Severity = Field(
        ..., description="Temperaturrisiko-Stufe"
    )
    lifetime_reduction_factor: float = Field(
        1.0, ge=0, le=1.0, description="Lebensdauer-Faktor (1.0 = kein Einfluss, 0.5 = halbiert)"
    )
    recommendations_de: list[str] = Field(
        default_factory=list, description="Empfehlungen auf Deutsch"
    )
    confidence: ConfidenceLevel


class VentilationRequirement(BaseModel):
    """Belüftungsberechnung für Blei-Säure-Batterien."""
    model_config = {"from_attributes": True}

    battery_chemistry: BatteryChemistry
    cell_count: int = Field(..., ge=1)
    max_charge_current_a: float = Field(..., gt=0)
    required_ventilation_m3_per_h: float = Field(
        ..., ge=0, description="Erforderliche Belüftung in m³/h"
    )
    min_opening_area_cm2: float = Field(
        ..., ge=0, description="Min. Lüftungsöffnung in cm²"
    )
    forced_ventilation_required: bool = Field(
        False, description="Mechanische Belüftung erforderlich"
    )
    hydrogen_explosion_risk: bool = Field(
        False, description="Knallgas-Explosionsrisiko vorhanden"
    )
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.CALCULATED)


class SafetyCompliance(BaseModel):
    """Sicherheits-Compliance-Check nach ISO 10133 / ABYC E-10."""
    model_config = {"from_attributes": True}

    battery_secured: Optional[bool] = Field(
        None, description="Batterie gegen Verrutschen gesichert (30° + 1g)"
    )
    main_switch_present: Optional[bool] = Field(
        None, description="Batterie-Hauptschalter vorhanden"
    )
    fuse_at_battery: Optional[bool] = Field(
        None, description="Sicherung am Batteriepol (max. 20cm)"
    )
    ventilation_adequate: Optional[bool] = Field(
        None, description="Belüftung ausreichend (Blei-Säure)"
    )
    acid_containment: Optional[bool] = Field(
        None, description="Säure-Auffangwanne vorhanden (Blei)"
    )
    spark_protection: Optional[bool] = Field(
        None, description="Zündschutz im Batterieraum"
    )
    cable_protection: Optional[bool] = Field(
        None, description="Kabelschutz gegen Kurzschluss"
    )
    polarity_marking: Optional[bool] = Field(
        None, description="Polaritätskennzeichnung vorhanden"
    )
    emergency_disconnect: Optional[bool] = Field(
        None, description="Not-Aus erreichbar"
    )
    bms_functional: Optional[bool] = Field(
        None, description="BMS funktionsfähig (LiFePO4)"
    )
    compliance_score: int = Field(..., ge=0, le=100)
    non_compliant_items: list[str] = Field(
        default_factory=list, description="Nicht-konforme Punkte"
    )
    confidence: ConfidenceLevel
```

### ANHANG R — Score-Fusion und Orchestrierung

```python
"""
AYDI Battery Module — Score Fusion
Kombiniert strukturelle und visuelle Analyse.
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from .battery_base_models import ConfidenceLevel


class BatteryModuleStructuredScore(BaseModel):
    """Strukturelle Bewertung (Pipeline A) des Batteriemoduls."""
    model_config = {"from_attributes": True}

    capacity_adequacy_score: int = Field(..., ge=0, le=100)
    chemistry_appropriateness_score: int = Field(..., ge=0, le=100)
    charging_profile_score: int = Field(..., ge=0, le=100)
    state_of_health_score: int = Field(..., ge=0, le=100)
    installation_compliance_score: int = Field(..., ge=0, le=100)
    bms_score: Optional[int] = Field(None, ge=0, le=100)
    monitoring_score: int = Field(..., ge=0, le=100)
    safety_score: int = Field(..., ge=0, le=100)
    redundancy_score: int = Field(..., ge=0, le=100)

    overall_structured_score: int = Field(..., ge=0, le=100)
    confidence: ConfidenceLevel


class BatteryModuleVisualScore(BaseModel):
    """Visuelle Bewertung (Pipeline B) des Batteriemoduls."""
    model_config = {"from_attributes": True}

    physical_condition_score: int = Field(..., ge=0, le=100)
    installation_quality_score: int = Field(..., ge=0, le=100)
    cable_connection_score: int = Field(..., ge=0, le=100)
    labeling_score: int = Field(..., ge=0, le=100)
    ventilation_score: int = Field(..., ge=0, le=100)
    safety_visual_score: int = Field(..., ge=0, le=100)

    overall_visual_score: int = Field(..., ge=0, le=100)
    confidence: ConfidenceLevel


class BatteryModuleFusedResult(BaseModel):
    """Fusionierter Score für das Batteriemodul."""
    model_config = {"from_attributes": True}

    structured_score: Optional[BatteryModuleStructuredScore] = None
    visual_score: Optional[BatteryModuleVisualScore] = None

    # Fusionsgewichte (Batterien sind primär strukturell bewertbar)
    structured_weight: float = Field(default=0.75)
    visual_weight: float = Field(default=0.25)

    fused_score: int = Field(..., ge=0, le=100)
    confidence: ConfidenceLevel

    critical_findings_count: int = Field(0, ge=0)
    high_findings_count: int = Field(0, ge=0)
    medium_findings_count: int = Field(0, ge=0)

    summary_de: str = Field(..., description="Zusammenfassung auf Deutsch")
    top_recommendations: list[str] = Field(
        default_factory=list, description="Top-3 Empfehlungen, priorisiert"
    )


def fuse_battery_scores(
    structured: Optional[BatteryModuleStructuredScore],
    visual: Optional[BatteryModuleVisualScore],
    structured_weight: float = 0.75,
    visual_weight: float = 0.25,
) -> BatteryModuleFusedResult:
    """
    Fusioniert strukturelle und visuelle Bewertung des Batteriemoduls.

    Wenn nur eine Quelle vorliegt, wird diese mit 100% gewichtet.
    Wenn keine vorliegt, wird Score 0 mit visual_insufficient zurückgegeben.
    """
    if structured is None and visual is None:
        return BatteryModuleFusedResult(
            structured_score=None,
            visual_score=None,
            structured_weight=structured_weight,
            visual_weight=visual_weight,
            fused_score=0,
            confidence=ConfidenceLevel.VISUAL_INSUFFICIENT,
            summary_de="Keine Daten für Batteriebewertung vorhanden.",
            top_recommendations=[
                "Batterieinspektion durchführen (strukturell und/oder visuell)."
            ],
        )

    if structured is not None and visual is not None:
        fused = int(
            structured.overall_structured_score * structured_weight
            + visual.overall_visual_score * visual_weight
        )
        conf = _lower_confidence(structured.confidence, visual.confidence)
    elif structured is not None:
        fused = structured.overall_structured_score
        conf = structured.confidence
    else:
        assert visual is not None
        fused = visual.overall_visual_score
        conf = visual.confidence

    # Zusammenfassung generieren
    if fused >= 85:
        summary = "Batteriesystem in sehr gutem Zustand. Keine Maßnahmen erforderlich."
    elif fused >= 70:
        summary = "Batteriesystem in gutem Zustand. Geringfügige Optimierungen möglich."
    elif fused >= 55:
        summary = "Batteriesystem akzeptabel, einige Verbesserungen empfohlen."
    elif fused >= 40:
        summary = "Batteriesystem weist erhebliche Mängel auf. Maßnahmen empfohlen."
    else:
        summary = "Batteriesystem in schlechtem Zustand. Dringende Maßnahmen erforderlich."

    return BatteryModuleFusedResult(
        structured_score=structured,
        visual_score=visual,
        structured_weight=structured_weight,
        visual_weight=visual_weight,
        fused_score=max(0, min(100, fused)),
        confidence=conf,
        summary_de=summary,
        top_recommendations=[],
    )


def _lower_confidence(a: ConfidenceLevel, b: ConfidenceLevel) -> ConfidenceLevel:
    """Gibt das niedrigere Confidence-Level zurück."""
    order = [
        ConfidenceLevel.MEASURED,
        ConfidenceLevel.CALCULATED,
        ConfidenceLevel.DOCUMENTED,
        ConfidenceLevel.VISUAL_HIGH,
        ConfidenceLevel.VISUAL_MEDIUM,
        ConfidenceLevel.ESTIMATED,
        ConfidenceLevel.BENCHMARK,
        ConfidenceLevel.VISUAL_LOW,
        ConfidenceLevel.VISUAL_INSUFFICIENT,
    ]
    idx_a = order.index(a) if a in order else len(order) - 1
    idx_b = order.index(b) if b in order else len(order) - 1
    return order[max(idx_a, idx_b)]


def calculate_peukert_capacity(
    nominal_capacity_ah: float,
    peukert_exponent: float,
    discharge_current_a: float,
    nominal_hours: float = 20.0,
) -> tuple[float, float]:
    """
    Berechnet die effektive Kapazität unter Berücksichtigung des Peukert-Effekts.

    Returns:
        (effective_capacity_ah, runtime_hours)
    """
    # Peukert-Gleichung: t = H × (C / (I × H))^k
    i_nominal = nominal_capacity_ah / nominal_hours
    runtime_h = nominal_hours * (i_nominal / discharge_current_a) ** peukert_exponent
    effective_ah = discharge_current_a * runtime_h
    return effective_ah, runtime_h


def calculate_ventilation_requirement(
    cell_count: int,
    max_charge_current_a: float,
) -> tuple[float, float]:
    """
    Berechnet die erforderliche Belüftung für Blei-Säure-Batterien.

    Nach ABYC E-10 / ISO 10133:
    Q = 0.52 × n × I × 10^-4 m³/h

    Returns:
        (required_m3_per_h, min_opening_area_cm2)
    """
    q_m3_per_h = 0.52 * cell_count * max_charge_current_a * 1e-4
    # Min. Öffnungsfläche: Q / 0.5 m/s Luftgeschwindigkeit
    min_area_m2 = q_m3_per_h / (0.5 * 3600)
    min_area_cm2 = min_area_m2 * 10000
    return q_m3_per_h, max(min_area_cm2, 28.0)  # Min. 28 cm² nach ISO
```

---

### ANHANG R.2 — AYDI-Analyse-Konstanten

```python
"""
AYDI Battery Module — Analysis Constants
Referenzwerte und Schwellwerte für die automatisierte Analyse.
"""

# Ladespannungs-Referenzwerte (12V-System, 25°C)
CHARGE_VOLTAGES = {
    "flooded_lead_acid": {
        "absorption_v": 14.4,
        "float_v": 13.4,
        "equalization_v": 15.5,
        "max_charge_rate": 0.2,  # C/5
        "temp_comp_mv_per_c": -18,
    },
    "agm": {
        "absorption_v": 14.5,
        "float_v": 13.6,
        "equalization_v": None,  # VERBOTEN
        "max_charge_rate": 0.33,  # C/3
        "temp_comp_mv_per_c": -18,
    },
    "gel": {
        "absorption_v": 14.2,
        "float_v": 13.6,
        "equalization_v": None,  # VERBOTEN
        "max_charge_rate": 0.1,  # C/10
        "temp_comp_mv_per_c": -24,
    },
    "lifepo4": {
        "absorption_v": 14.4,
        "float_v": 13.5,  # Optional, nur bei Dauerlandstrom
        "equalization_v": None,  # VERBOTEN
        "max_charge_rate": 1.0,  # 1C
        "temp_comp_mv_per_c": 0,  # Keine Kompensation
    },
}

# Kritische Schwellwerte für Alarme
CRITICAL_THRESHOLDS = {
    "lead_acid_12v": {
        "low_voltage_warning_v": 12.0,
        "low_voltage_critical_v": 11.5,
        "high_voltage_warning_v": 14.8,
        "high_voltage_critical_v": 15.0,
        "max_temperature_c": 50,
    },
    "lifepo4_12v": {
        "cell_overvoltage_v": 3.65,
        "cell_undervoltage_v": 2.5,
        "cell_imbalance_warning_mv": 50,
        "cell_imbalance_critical_mv": 100,
        "charge_temp_min_c": 0,
        "max_temperature_c": 55,
    },
}

# SoH-Bewertungsgrenzen
SOH_THRESHOLDS = {
    "excellent": 95,  # >95% = excellent
    "good": 85,       # 85-95% = good
    "fair": 75,       # 75-85% = fair
    "poor": 60,       # 60-75% = poor
    "end_of_life": 60,  # <60% = end_of_life
}

# Score-Fusion-Gewichte für Batteriemodul
BATTERY_MODULE_FUSION_WEIGHTS = {
    "structured_weight": 0.75,
    "visual_weight": 0.25,
}
```

---

> **Ende der AYDI Wissensdatei 22.02 — Batteriesysteme**
> **Confidence-Mapping:** Alle Herstellerangaben basieren auf öffentlich verfügbaren Datenblättern (documented). Berechnungsformeln sind nach ABYC E-10 / ISO 10133 (measured). Erfahrungswerte und Preise sind estimated. Pydantic-Modelle sind als calculated markiert, da sie aus den Wissensinhalten algorithmisch abgeleitet werden.
