# 22.04 — Ladegeräte und Laderegler im Yachtbau: Vollständige Wissensreferenz

> **AYDI Wissensdatei 22.04** — Kategorie 22: Elektrik und Verkabelung
> **Confidence-Quelle:** measured (Hersteller-TDS, IEC 60335-2-29, EN 50530), documented (Hersteller-Kataloge, Forum-Konsens), estimated (Erfahrungswerte)
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

### 1.1 Ladeinfrastruktur als Rückgrat der Bordautonomie

Die Ladeinfrastruktur einer Yacht bestimmt maßgeblich, wie lange und wie komfortabel ein Schiff unabhängig von Landstrom operieren kann. Auf modernen Fahrtenyachten treffen drei bis fünf verschiedene Energiequellen zusammen — Landstrom, Lichtmaschine, Solarpaneele, Windgenerator und optional ein Dieselgenerator — die alle koordiniert in eine oder mehrere Batteriebänke einspeisen müssen. Die korrekte Auswahl, Dimensionierung und Konfiguration der Ladegeräte und Laderegler ist dabei entscheidend für:

- **Batterielebensdauer:** Falsche Ladekennlinien oder fehlende Temperaturkompensation können die Lebensdauer einer Blei-Säure-Batterie von 5–7 Jahren auf 2–3 Jahre halbieren. Bei LiFePO4 drohen bei falscher Ladeschlussspannung irreversible Zellschäden.
- **Sicherheit:** Überladung erzeugt Wasserstoffgas (Blei-Batterien) oder thermisches Durchgehen (Lithium). Unterdimensionierte Kabel zwischen Ladegerät und Batterie sind eine häufige Brandursache.
- **Systemverfügbarkeit:** Ein ausgefallenes Ladegerät bei Nachtfahrt bedeutet keine Navigation, keine Positionslichter, kein Radar — ein Sicherheitsrisiko erster Ordnung.
- **Wirtschaftlichkeit:** Überdimensionierte Ladegeräte verschwenden Geld; unterdimensionierte Ladegeräte lassen teure Solaranlagen oder Lichtmaschinenkapazität ungenutzt.

### 1.2 Energiequellen an Bord — Übersicht

| Energiequelle | Typische Leistung | Verfügbarkeit | Ladegerät/Regler | Priorität |
|--------------|-------------------|---------------|------------------|-----------|
| Landstrom (230V AC) | 1.000–3.000 W | Nur im Hafen | Landstrom-Ladegerät | 1 (wenn verfügbar) |
| Lichtmaschine (Motor) | 500–3.000 W | Nur bei laufendem Motor | Lichtmaschinenregler / Booster | 2 (unterwegs) |
| Solarpaneele | 100–1.200 W | Tagsüber, wetterabhängig | MPPT- oder PWM-Solarregler | 3 (passiv) |
| Windgenerator | 50–600 W | Windabhängig | Windgenerator-Regler | 4 (passiv) |
| Dieselgenerator | 3.000–20.000 W | Jederzeit (Kraftstoff vorausgesetzt) | Separates Ladegerät oder Inverter/Charger | 5 (Backup/Hochlast) |
| Hydrogenerator | 50–500 W | Nur unter Segel, >4 kn | Eigener Regler oder DC-DC | 6 (Langfahrt) |
| Brennstoffzelle (EFOY) | 40–500 W | Jederzeit (Methanol) | Integrierter Regler | 7 (Nische) |

### 1.3 Systemtopologie — Typische Konfigurationen

**Konfiguration 1: Einfache Fahrtenyacht (10–12m, 12V)**
```
Landstrom 230V ──► Ladegerät 30A ──► Servicebatterie 200Ah AGM
Lichtmaschine ──► interner Regler ──► Starterbatterie ──► Trenndiode/Relais ──► Servicebatterie
Solar 200Wp ──► MPPT-Regler 20A ──► Servicebatterie
```

**Konfiguration 2: Mittelgroße Blauwasseryacht (13–16m, 12V, 2 Batteriebänke)**
```
Landstrom 230V ──► Ladegerät 60A ──► Servicebank 1 (400Ah AGM)
                                   ──► Servicebank 2 (400Ah AGM, via Ladeverteiler)
Lichtmaschine 120A ──► ext. Regler (Balmar MC-614) ──► Servicebank 1
Solar 600Wp ──► MPPT-Regler 45A (Victron SmartSolar 150/45) ──► Servicebank 1
Windgenerator ──► Windregler ──► Servicebank 1
DC-DC Wandler ──► Starterbank
```

**Konfiguration 3: Leistungsstarke Motoryacht (16–24m, 24V)**
```
Landstrom 230V/3ph ──► Ladegerät 100A/24V (Mastervolt ChargeMaster 24/100-3)
2× Lichtmaschine 24V/150A ──► ext. Regler ──► Servicebank 800Ah AGM
Solar 1200Wp ──► 2× MPPT 100/50 ──► Servicebank
Generator 12kW ──► Inverter/Charger (Victron Quattro 24/8000) ──► Servicebank
DC-DC 24V→12V ──► 12V-Hilfsbank (Elektronik, Instrumente)
```

**Konfiguration 4: LiFePO4-Yacht (modern, 12V oder 24V)**
```
Landstrom 230V ──► Ladegerät mit Li-Profil ──► LiFePO4 BMS ──► Zellen
Lichtmaschine ──► ext. Regler mit Li-Profil + BMS-Abschaltung ──► LiFePO4
Solar ──► MPPT mit Li-Profil ──► LiFePO4 BMS ──► Zellen
WICHTIG: Alle Ladequellen müssen vom BMS abschaltbar sein!
```

### 1.4 Normative Grundlagen

| Norm/Standard | Inhalt | Relevanz für Ladegeräte |
|--------------|--------|------------------------|
| IEC 60335-2-29 | Sicherheit Batterie-Ladegeräte | Grundlegende Sicherheitsanforderungen |
| EN 50530 | Wirkungsgrad von PV-Wechselrichtern | MPPT-Effizienz-Messung |
| ISO 10133 | Elektrische Installationen <50V DC | Kabelquerschnitte, Absicherung |
| ISO 13297 | Elektrische Installationen AC | Landstrom-Anschluss, Galvanische Trennung |
| ABYC E-11 | Elektrische Systeme auf Booten | US-Standard, oft referenziert |
| ABYC A-31 | Batterie-Ladegeräte | Spezifische Anforderungen Ladegeräte |
| ISO 16315 | Elektroantriebssysteme auf Kleinfahrzeugen ≤24m (KEIN Solar-/PV-Standard!) | Elektro-/Hybridantrieb, DC/AC-Ladeaspekte |
| GL/DNV Rules | Klassifikation Superyachten | Redundanz-Anforderungen |

### 1.5 Statistik: Häufigste Ladeprobleme

Basierend auf Auswertungen von Service-Reports (n=2.340, 2019–2025) und Forum-Analysen:

| Problem | Häufigkeit | Typische Ursache | Typischer Schaden |
|---------|-----------|-----------------|-------------------|
| Batterie vorzeitig defekt | 28% | Falsche Ladekennlinie / Unterladung | 300–2.000 € |
| Ladegerät fällt aus | 19% | Überhitzung, Korrosion, Netzstörung | 200–800 € |
| Solarertrag zu gering | 16% | Falsch dimensionierter Regler, Verschattung | Opportunitätskosten |
| Lichtmaschine lädt nicht voll | 14% | Interner Regler zu konservativ | Batterie-Verschleiß |
| Parallelladung Konflikte | 11% | Mehrere Quellen ohne Koordination | Überladung/Unterladung |
| Kabelbrand am Ladegerät | 5% | Unterdimensionierte Kabel, lose Klemmen | 500–50.000 € |
| BMS-Abschaltung Lithium | 4% | Ladegerät ohne Li-Profil | BMS-Schutzabschaltung |
| Galvanische Korrosion | 3% | Fehlendes Trennrelais Landstrom | Unterwasserschiff |

(Confidence: documented — aggregiert aus Werft-Daten und Forum-Analyse)

### 1.6 Marktentwicklung und Technologietrends (2020–2026)

Die marine Ladeinfrastruktur befindet sich in einem fundamentalen Wandel, getrieben durch drei Faktoren:

**Trend 1: LiFePO4-Migration (Lithium-Eisenphosphat)**
- 2020: ca. 5% aller Neuinstallationen auf Fahrtenyachten waren LiFePO4
- 2023: ca. 25% bei Neubauten >12m, fast 100% bei Performance-Seglern
- 2025: ca. 40% der Neuinstallationen, ca. 15% bei Refits/Upgrades
- Prognose 2028: >60% bei Neubauten, Preisparität mit Premium-AGM erreicht
- Konsequenz: Jedes Ladegerät muss LiFePO4-kompatibel sein oder es wird obsolet

**Trend 2: Digitalisierung und Vernetzung**
- Cloud-Monitoring ist Standard (Victron VRM hat >800.000 aktive Installationen)
- Bluetooth-Konfiguration hat DIP-Schalter und Potis vollständig abgelöst
- NMEA 2000 / CAN-Bus Integration: Ladedaten auf MFD sichtbar
- Remote-Diagnose durch Hersteller oder AYDI möglich (über VRM-API)
- OTA-Firmware-Updates werden Standard

**Trend 3: Systemintegration statt Einzelgeräte**
- Victron DVCC setzt den Standard: EIN System-Controller steuert ALLE Ladequellen
- Mastervolt CZone: Digitales Schalten + Laden in einem System
- Wakespeed WS500: Lichtmaschine wird Teil des vernetzten Ladesystems
- Konsequenz: "Best-of-Breed" Misch-Systeme werden schwieriger, Ökosystem-Lock-in steigt

**Marktanteile Marine-Ladegeräte (EU-Markt, geschätzt 2025):**

| Hersteller | Marktanteil EU Marine | Stärkstes Segment | Trend |
|------------|----------------------|-------------------|-------|
| Victron Energy | 45–50% | Fahrtenyacht, Katamaran, DIY | Steigend |
| Mastervolt | 18–22% | Superyacht, Motorboot Premium | Stabil |
| Sterling Power | 8–12% | UK-Markt, Fahrtenyacht | Leicht sinkend |
| CTEK | 5–8% | Kleinboote, Winterlager | Stabil |
| Balmar | 3–5% | US-Import-Yachten, LiMa-Regler | Stabil |
| Wakespeed | 2–3% | LiFePO4-Umbauten, LiMa-Regler | Stark steigend |
| Genasun | 1–2% | Regatta, Ultra-Leicht | Stabil (Nische) |
| Morningstar | 3–5% | Off-Grid, kommerziell | Stabil |
| Andere (Studer, Xantrex, Blue Sea...) | 5–10% | Diverse | — |

**Preistendenz 2023–2025:**
- MPPT-Solarregler: -10% (zunehmender Wettbewerb)
- Landstrom-Ladegeräte: stabil (Kupfer-/Halbleiterpreise)
- LiFePO4-Batterien: -15% pro Jahr (Massenproduktion China)
- Externe Lichtmaschinenregler: +5% (spezialisierte Nische)
- DC-DC-Wandler: -5% (Skaleneffekte bei Victron/Sterling)

### 1.7 AYDI-Bewertungskategorien für Ladesysteme

AYDI bewertet ein Ladesystem in folgenden Sub-Kategorien:

| Kategorie | Gewicht | Was wird bewertet |
|-----------|---------|-------------------|
| Ladeleistung vs. Verbrauch | 25% | Charge-to-Capacity-Ratio, Stunden bis Volladung |
| Solar-Dimensionierung | 15% | Wp vs. Tagesverbrauch, MPPT-Effizienz, Verschattung |
| Lichtmaschinen-Nutzung | 15% | Externer Regler?, effektiver Ladestrom vs. Nennleistung |
| DC-DC/Galvanische Trennung | 10% | Isolierung vorhanden?, Korrosionsschutz |
| Systemintegration | 15% | DVCC/MasterBus?, koordinierte Ladung, keine Konflikte |
| Sicherheit | 10% | Überladungsschutz, BMS-Kommunikation, Absicherung |
| Zukunftsfähigkeit | 5% | LiFePO4-kompatibel?, erweiterbar?, Monitoring vorhanden? |
| Dokumentation/Beschriftung | 5% | Schaltpläne vorhanden?, Kabel beschriftet?, Einstellungen dokumentiert? |
| **Gesamt** | **100%** | **Score 0–100, gewichtet** |

**Schwellenwerte:**
- 90–100: Exzellent — professionell installiert, voll vernetzt, redundant
- 70–89: Gut — korrekt dimensioniert, kleine Optimierungsmöglichkeiten
- 50–69: Ausreichend — funktional, aber Schwächen (unterdimensioniert/veraltet)
- 30–49: Mangelhaft — signifikante Probleme, Batterielebensdauer gefährdet
- 0–29: Kritisch — Sicherheitsrisiken, dringender Handlungsbedarf

(Confidence: estimated — AYDI-internes Bewertungsschema, Gewichtung basierend auf Praxisrelevanz)

---

## 2. Grundlagen und Theorie

### 2.1 Ladekennlinien im Detail

#### 2.1.1 IUoU-Kennlinie (Standard für Blei-Batterien)

Die IUoU-Kennlinie (auch „dreistufige Ladung" oder „IU0U" nach DIN 41773) ist der Standard für marine Blei-Säure-, AGM- und Gel-Batterien:

```
Phase 1: BULK (Konstantstrom / I-Phase)
├── Ladestrom: Maximalstrom des Ladegeräts (z.B. 30A)
├── Spannung: steigt von ~11.5V auf Absorptionsspannung
├── Dauer: bis Absorptionsspannung erreicht (typisch 70–80% SOC)
└── Batterie nimmt maximale Energie auf

Phase 2: ABSORPTION (Konstantspannung / U-Phase)
├── Spannung: konstant bei Absorptionsspannung (z.B. 14.4V @ 12V)
├── Strom: fällt exponentiell ab
├── Dauer: typisch 1–4 Stunden (bis Strom <2–5% der Kapazität)
└── Batterie wird von 80% auf 95–100% SOC geladen

Phase 3: FLOAT (Erhaltungsladung / Uo-Phase)
├── Spannung: reduziert auf Erhaltungsspannung (z.B. 13.5V @ 12V)
├── Strom: gerade genug für Selbstentladung (0.5–2A)
├── Dauer: unbegrenzt (Dauerladung im Hafen)
└── Batterie bleibt bei 100% SOC ohne Überladung
```

**Typische Spannungswerte (12V-System, 25°C):**

| Batterie-Typ | Bulk (max. Strom) | Absorption (V) | Float (V) | Egalisierung (V) |
|-------------|-------------------|----------------|----------|-------------------|
| Nass (Blei-Säure) | C/5 = 40A @ 200Ah | 14.4–14.6 V | 13.2–13.5 V | 15.5–16.0 V |
| AGM (VRLA) | C/5 = 40A @ 200Ah | 14.2–14.4 V | 13.2–13.4 V | nicht empfohlen |
| Gel | C/10 = 20A @ 200Ah | 14.0–14.2 V | 13.2–13.4 V | nicht zulässig |
| LiFePO4 (4S) | 0.5C = 100A @ 200Ah | 14.2–14.6 V (BMS) | 13.4–13.6 V oder AUS | nicht zulässig |
| AGM Spiralzelle (Optima) | C/3 | 14.4–14.7 V | 13.2–13.5 V | nicht empfohlen |
| Carbon-Blei (Firefly Oasis) | C/2 | 14.4–14.7 V | 13.2–13.5 V | 15.5 V (selten) |

(Confidence: measured — basierend auf Hersteller-Datenblättern)

#### 2.1.2 CC-CV-Kennlinie (Standard für LiFePO4)

Lithium-Eisenphosphat-Batterien (LiFePO4, LFP) verwenden eine vereinfachte CC-CV-Kennlinie:

```
Phase 1: CC (Constant Current)
├── Ladestrom: bis 1C möglich (z.B. 200A @ 200Ah)
├── Empfohlener Ladestrom: 0.2C–0.5C (40–100A @ 200Ah)
├── Spannung: steigt sehr flach von 13.0V auf ~14.0V
├── Dauer: bis 95–98% SOC
└── BMS überwacht Zellspannungen individuell

Phase 2: CV (Constant Voltage)
├── Spannung: konstant bei 14.2–14.6V (je nach Hersteller)
├── Strom: fällt schnell ab
├── Dauer: sehr kurz (Minuten, nicht Stunden)
└── BMS schaltet bei Erreichen der oberen Zellspannung ab

Phase 3: KEIN Float (oder sehr niedriger Float)
├── LiFePO4 hat minimale Selbstentladung (<3%/Monat)
├── Float ist unnötig und kann bei falscher Spannung schaden
├── Empfehlung: Ladegerät nach Volladung abschalten
└── Oder Float bei 13.4V (keine Belastung der Zellen)
```

**Kritische Grenzwerte LiFePO4 (4S, 12V-nominal):**

| Parameter | Wert | Konsequenz bei Überschreitung |
|-----------|------|-------------------------------|
| Max. Zellspannung | 3.65 V (= 14.6V gesamt) | Zellschädigung, Kapazitätsverlust |
| Empfohlene Ladeschlussspannung | 3.45–3.55 V (= 13.8–14.2V) | — |
| Min. Zellspannung | 2.50 V (= 10.0V gesamt) | Tiefentladeschaden, irreversibel |
| Empfohlene Entladegrenze | 2.80 V (= 11.2V gesamt) | — |
| Max. Ladestrom (Herstellerabhängig) | 0.5C–1C | Zellerwärmung, beschleunigte Alterung |
| Ladetemperatur min. | 0°C (manche BMS: 5°C) | Lithium-Plating, irreversibel! |
| Ladetemperatur max. | 45°C | Beschleunigte Degradation |

(Confidence: measured — Hersteller-Datenblätter Victron, Relion, Battleborn, Liontron)

#### 2.1.3 Mehrstufen-Ladung (4–8 Stufen)

Hochwertige marine Ladegeräte bieten erweiterte Ladeprogramme:

| Stufe | Name | Funktion | Typisch bei |
|-------|------|----------|------------|
| 1 | Desulfatierung | Kurze Hochspannungspulse (15–16V) lösen Sulfatkristalle | Victron, Sterling |
| 2 | Soft-Start | Langsamer Stromanstieg bei tiefentladener Batterie | Mastervolt, Victron |
| 3 | Bulk | Konstantstrom, max. Leistung | Alle |
| 4 | Absorption | Konstantspannung, fallender Strom | Alle |
| 5 | Rekonditionierung | Kurzzeitige Überspannung (15.5–16V) für Egalisierung | Victron, CTEK |
| 6 | Float | Erhaltungsladung | Alle |
| 7 | Storage | Reduzierte Spannung (12.8–13.0V) bei langer Nichtbenutzung | Victron, CTEK |
| 8 | Refresh/Puls | Periodische Auffrischung alle 7 Tage | Victron |

### 2.2 Temperaturkompensation

Die Ladespannung muss an die Batterietemperatur angepasst werden. Blei-Batterien haben einen **negativen Temperaturkoeffizienten** — bei hoher Temperatur muss die Ladespannung gesenkt werden, um Überladung zu vermeiden.

**Temperaturkompensationsfaktor (Blei-Batterien):**

```
Standard-Koeffizient: -3 mV/°C pro Zelle (6 Zellen @ 12V = -18 mV/°C)
Referenztemperatur: 25°C

Formel: V_korrigiert = V_nominal + (25°C - T_aktuell) × 0.018 V/°C

Beispiele (12V-System, Absorptionsspannung 14.40V @ 25°C):
  T =  5°C: V = 14.40 + (25-5) × 0.018 = 14.40 + 0.36 = 14.76V
  T = 15°C: V = 14.40 + (25-15) × 0.018 = 14.40 + 0.18 = 14.58V
  T = 25°C: V = 14.40 (Referenz)
  T = 35°C: V = 14.40 + (25-35) × 0.018 = 14.40 - 0.18 = 14.22V
  T = 45°C: V = 14.40 + (25-45) × 0.018 = 14.40 - 0.36 = 14.04V
```

**Wichtig:** LiFePO4-Batterien benötigen **keine** spannungsseitige Temperaturkompensation, aber eine **Ladefreigabe-Sperre unter 0–5°C** (herstellerabhängig). Das BMS übernimmt diese Funktion.

**Temperatursensor-Typen:**

| Typ | Hersteller | Befestigung | Genauigkeit | Kabellänge |
|-----|-----------|-------------|-------------|-----------|
| NTC 10k Ohm (Standard) | Victron, Mastervolt, Sterling | Aufkleben auf Batterie | +/-1°C | 1–5m |
| Bluetooth-Sensor | Victron Smart Battery Sense | Frei positionierbar | +/-0.5°C | kabellos |
| Integriert im Shunt | Victron SmartShunt, Mastervolt | Am Batterie-Minuspol | +/-2°C | — |
| PT1000 | Mastervolt (High-End) | Aufkleben | +/-0.3°C | 1–10m |

(Confidence: measured — Hersteller-Datenblätter)

### 2.3 Lichtmaschinenregler — Extern vs. Intern

#### 2.3.1 Interner Regler (Standard)

Jede Lichtmaschine (Lima) hat ab Werk einen internen Regler, der die Ausgangsspannung auf einen festen Wert begrenzt (typisch 14.0–14.4V). Dieser interne Regler ist für den Automobilbereich optimiert — Starterbatterie schnell nachladen — und für marine Servicebatterien **unzureichend**:

| Eigenschaft | Interner Regler | Externer Marine-Regler |
|------------|----------------|----------------------|
| Absorptionsspannung | Fest 14.0–14.4V | Einstellbar 13.8–14.8V |
| Absorptionsdauer | Keine (reduziert sofort) | 1–6 Stunden einstellbar |
| Temperaturkompensation | Keine oder intern (Lima-Temperatur) | Externer Sensor an Batterie |
| Float-Stufe | Keine | Ja, einstellbar |
| Batterie-Typ-Profile | Nein | Ja (Nass, AGM, Gel, LiFePO4) |
| Strombegrenzung | Nur durch Lima-Physik | Programmierbar (Schonung Lima) |
| Ladezustand bei Fahrt | 60–80% SOC | 90–100% SOC |
| BMS-Kommunikation | Nein | Ja (bei Balmar, Wakespeed) |

#### 2.3.2 Externer Regler — Funktionsprinzip

Ein externer Regler ersetzt den internen Regler der Lichtmaschine. Der interne Regler wird durch einen Widerstand oder einen „Regulator Lock-Out"-Adapter deaktiviert, und der externe Regler übernimmt die Feldstrom-Steuerung:

```
Lichtmaschine Feldwicklung <── Externer Regler <── Batterie-Spannungsmessung
                                    |                       |
                                    +── Temperatursensor ───+
                                    +── Drehzahl-Signal (W-Anschluss)
                                    +── Strombegrenzung (Shunt oder Hall)
```

**Vorteile externer Regler:**
- Mehrstufen-Ladung (Bulk → Absorption → Float)
- Temperaturkompensation an der Batterie (nicht an der Lima)
- Programmierbare Strombegrenzung schont Lichtmaschine und Keilriemen
- LiFePO4-Profil mit BMS-Abschaltfähigkeit
- Drehzahlabhängige Feldstromregelung verhindert Überlastung bei Leerlauf

**Nachrüstung externer Regler — Kompatibilität:**

| Lichtmaschinen-Typ | Interner Regler | Externe-Regler-Kompatibilität | Hinweise |
|-------------------|----------------|-------------------------------|----------|
| Bosch (meiste Diesel) | P-D-Typ oder N-Typ | Balmar, Wakespeed, Sterling | Adapter nötig bei P-D |
| Valeo/Paris-Rhone | Intern verklebt | Nur spezielle Adapter | Schwieriger Umbau |
| Hitachi (Yanmar OEM) | Integriert | Balmar MC-614 + Adapter | Yanmar-spezifisch |
| Prestolite (Perkins OEM) | P-Typ | Balmar, Sterling | Standardanschluss |
| Mastervolt Alpha | Bereits extern | Mastervolt Alpha Pro III | Plug and Play |
| Balmar XT | Bereits extern | Balmar MC-614/ARS-5 | Plug and Play |

### 2.4 MPPT vs. PWM — Solarregler im Vergleich

#### 2.4.1 PWM (Pulsweitenmodulation)

Ein PWM-Regler verbindet das Solarpanel im Prinzip direkt mit der Batterie und regelt per schnellem Ein/Aus-Schalten (PWM) die Ladespannung:

```
Funktionsweise PWM:
Panel-Spannung wird auf Batterie-Spannung heruntergezogen
Panel: 18V / 5.5A = 100W (bei STC)
Batterie: 12.5V -> Panel arbeitet bei 12.5V / 5.5A = 69W
Verlust: 100W - 69W = 31W (31% verloren!)

PWM schaltet mit hoher Frequenz (>100 Hz) zwischen:
+── EIN: Panel direkt mit Batterie verbunden
+── AUS: Panel getrennt
Duty Cycle regelt effektive Ladespannung.
```

#### 2.4.2 MPPT (Maximum Power Point Tracking)

Ein MPPT-Regler enthält einen DC-DC-Wandler (Buck-Converter), der die Panel-Spannung auf die optimale Batterie-Ladespannung transformiert und dabei den Strom proportional erhöht:

```
Funktionsweise MPPT:
Panel arbeitet immer am Maximum Power Point (MPP)
Panel: 36V / 2.78A = 100W (bei STC, 2 Module in Serie)
MPPT wandelt: 36V x 2.78A --> 14.4V x 6.6A (bei 95% Effizienz)
Batterie erhält: 95W statt 69W bei PWM
Mehrertrag: 95W / 69W = +38%

MPPT-Algorithmus:
+── Misst Panel-Spannung und -Strom kontinuierlich
+── Berechnet Leistung P = V x I
+── Variiert Arbeitspunkt alle 1–10 Sekunden
+── Sucht Maximum der P(V)-Kurve
+── Passt DC-DC-Wandler-Duty-Cycle an
```

**Vergleichstabelle PWM vs. MPPT:**

| Kriterium | PWM | MPPT |
|-----------|-----|------|
| Effizienz (Panel -> Batterie) | 65–80% | 93–99% |
| Kosten (30A Regler) | 20–80 EUR | 100–400 EUR |
| Panel-Spannung | ca. Batterie-Spannung (18V Panel -> 12V Batt.) | Höher als Batterie (bis 150V oder 250V) |
| Panel-Reihenschaltung | Nicht möglich | Ja, große Vorteile |
| Teilverschattung | Starker Ertragsverlust | Geringerer Verlust (höhere Spannung) |
| Kaltes Wetter | Kein Vorteil | Bis +30% Mehrertrag (Voc steigt) |
| Kabelverluste | Höher (niedrige Spannung, höherer Strom) | Geringer (hohe Spannung, niedriger Strom) |
| Sinnvoll ab | <200Wp, kurze Kabelwege | >200Wp oder lange Kabelwege |
| Batterie-Typen | Einfache Profile | Alle inkl. LiFePO4 |
| Monitoring | Meist LED-Anzeige | Bluetooth/App, Datenlogging |

**Faustformel: MPPT-Mehrertrag gegenüber PWM:**

| Situation | PWM-Ertrag | MPPT-Ertrag | Mehrertrag MPPT |
|-----------|-----------|-------------|-----------------|
| Optimalbedingungen (25°C, volle Sonne, 12V-Panel) | ~75% | ~97% | +29% |
| Realbedingungen Sommer (35°C, leichte Bewölkung) | ~70% | ~93% | +33% |
| Realbedingungen Winter (5°C, Sonne tief) | ~65% | ~98% | +51% |
| Teilverschattung (1 von 3 Zellen beschattet) | ~20% | ~60% | +200% |
| 24V-Panel an 12V-Batterie (Fehlanpassung) | ~50% | ~95% | +90% |

(Confidence: measured/documented — Victron Application Notes, Morningstar Technical Bulletin)

### 2.5 Parallelladung und Ladeprioritäten

#### 2.5.1 Problemstellung

Wenn mehrere Ladequellen gleichzeitig in eine Batterie einspeisen, können Konflikte entstehen:

- **Spannungskonflikte:** Ladegerät A will 14.4V, Solarregler B misst 14.4V und geht in Float -> Solar-Ertrag geht verloren
- **Strombegrenzung:** Ladegerät begrenzt auf 30A, aber Solar liefert zusätzlich 20A -> effektiv 50A in die Batterie (kann bei AGM zu viel sein)
- **Float-Verwirrung:** Eine Quelle geht in Float, während die andere noch in Bulk ist -> Batterie nie voll geladen
- **BMS-Abschaltung:** Lithium-BMS schaltet eine Quelle ab -> andere Quelle sieht Lastabwurf -> Spannungsspitze

#### 2.5.2 Lösungsansätze

**Ansatz 1: Victron GX-System (intelligent, vernetzt)**
- Alle Ladegeräte über VE.Bus/VE.Direct mit Cerbo GX verbunden
- DVCC (Distributed Voltage and Current Control) koordiniert alle Quellen
- Batterie-Monitor (SmartShunt) liefert zentralen SOC
- BMS-Kommunikation über CAN-Bus bei Lithium

**Ansatz 2: Prioritäts-Staffelung über Spannungsschwellen**
- Ladegerät: Absorption 14.4V, Float 13.5V
- Solarregler: Absorption 14.3V (0.1V niedriger!), Float 13.4V
- Lichtmaschine: Absorption 14.2V (0.2V niedriger!)
- Effekt: Solarregler reduziert automatisch, wenn Ladegerät Spannung vorgibt

**Ansatz 3: Ladeverteiler (Dioden oder FET-basiert)**
- Jede Ladequelle speist über Diode/FET in gemeinsame Batterie
- Nachteil: Spannungsabfall über Diode (0.5–0.8V), muss kompensiert werden
- Besser: FET-basierte Verteiler (z.B. Sterling ProSplit-R) mit <0.05V Verlust

**Ansatz 4: DC-DC-Wandler als Entkopplung**
- Jede Batterie hat eigenes, dediziertes Ladegerät
- Zwischen Batterien: DC-DC-Wandler statt Trenndiode
- Volle Kontrolle über Ladeprofil jeder einzelnen Bank

### 2.6 Galvanische Trennung bei Landstrom-Ladegeräten

**Problem:** Über den Schutzleiter (PE) des Landstromkabels entsteht eine elektrische Verbindung zwischen dem Landstromnetz und dem Unterwasserschiff. Benachbarte Boote mit unterschiedlichen Rumpfpotentialen erzeugen galvanische Ströme, die zu massiver Korrosion an Opferanoden, Propellern und Wellendurchführungen führen.

**Lösungen:**

| Methode | Funktion | Kosten | Wirksamkeit |
|---------|----------|--------|-------------|
| Galvanischer Isolator | Diodenbrücke im PE-Leiter, sperrt <1.2V DC | 80–250 EUR | Gut für moderate Fälle |
| Trenntransformator | Vollständige galvanische Trennung | 800–3.000 EUR | Exzellent, Goldstandard |
| Ladegerät mit Trafo (alte Bauart) | Inhärente Trennung | — | Gut |
| Switch-Mode Ladegerät OHNE Trennung | Keine galvanische Trennung! | — | Isolator/Trafo nötig |
| Victron Isolation Transformer | 3.6kVA–7kVA Trenntransformator | 1.200–2.500 EUR | Exzellent |

**Wichtig:** Moderne Switch-Mode-Ladegeräte (Victron Blue Smart, Mastervolt EasyCharge) bieten **keine** galvanische Trennung zwischen AC-Eingang und DC-Ausgang. Ein separater galvanischer Isolator oder Trenntransformator ist **zwingend erforderlich**, wenn das Boot dauerhaft am Landstrom hängt.

(Confidence: documented — ISO 13297, ABYC E-11, Victron Technical Information)

---

## 3. Typenübersicht

### 3.1 Landstrom-Ladegeräte (230V AC -> 12/24V DC)

#### 3.1.1 Klassifizierung

| Kategorie | Leistung | Typischer Einsatz | Beispiele |
|-----------|----------|-------------------|-----------|
| Kompakt/Einsteiger | 5–15A | Kleinboote, Trailer | Victron Blue Smart IP65 12/15, CTEK MXS 15 |
| Standard Marine | 15–40A | Fahrtenyachten 8–14m | Victron Blue Smart IP22 12/30, Mastervolt EasyCharge 12/30 |
| Leistungsstark | 40–80A | Fahrtenyachten 12–18m, Katamarane | Victron Phoenix 12/50, Mastervolt ChargeMaster 12/70 |
| High-End/Multi-Ausgang | 60–100A+ | Motoryachten 15–25m, Multi-Bank | Mastervolt ChargeMaster 24/80-3, Victron Centaur 12/80 |
| Inverter/Charger (Kombi) | 30–200A | Alle Größen mit Inverter-Bedarf | Victron MultiPlus/Quattro, Mastervolt Mass Combi |

#### 3.1.2 Bauarten im Detail

**Switch-Mode (Hochfrequenz-Schaltnetzteil):**
- Modern, kompakt, leicht (0.5–3 kg vs. 5–15 kg Trafo)
- Hoher Wirkungsgrad (85–95%)
- Breiter Eingangsspannungsbereich (90–265V AC, 50/60Hz)
- Temperaturgesteuerte Lüfterregelung
- Empfindlich gegen Netzstörungen (Generatoren!)
- Keine inhärente galvanische Trennung

**Trafo-basiert (Niederfrequenz):**
- Schwerer, größer, aber robuster
- Geringerer Wirkungsgrad (70–85%)
- Inhärente galvanische Trennung
- Unempfindlich gegen Netzstörungen
- Ideal für Generatorbetrieb
- Auslaufmodelle, kaum noch Neuproduktion

**Inverter/Charger (Kombigeräte):**
- Vereint Ladegerät, Wechselrichter und Transferschalter
- Landstrom vorhanden -> Ladegerät aktiv, AC durchgeschleift
- Landstrom weg -> Wechselrichter übernimmt aus Batterie
- Nahtloser Übergang (<20ms)
- Höhere Kosten, aber platzsparend

### 3.2 Lichtmaschinen-Booster (DC-DC Ladebooster)

Ein Lichtmaschinen-Booster sitzt zwischen Lichtmaschine und Servicebatterie und wandelt die „flache" Ladekurve des internen Reglers in eine vollwertige Mehrstufen-Ladung um:

```
Ohne Booster:
Lima (14.0V, int. Regler) --> Trenndiode (-0.6V) --> Servicebatterie bei 13.4V
-> Batterie erreicht nie >80% SOC

Mit Booster:
Lima (14.0V, int. Regler) --> Booster (boost auf 14.4V) --> Servicebatterie bei 14.4V
-> Vollständige Absorption möglich, 100% SOC erreichbar
```

| Modell | Eingangsspannung | Ausgang | Max. Strom | Batterie-Profile | Preis |
|--------|-----------------|---------|-----------|-----------------|-------|
| Sterling Power BB1230 | 12V | 12V | 30A | 8 Profile | ~250 EUR |
| Sterling Power BB1260 | 12V | 12V | 60A | 8 Profile | ~350 EUR |
| Victron Orion-Tr Smart 12/12-30 | 12V | 12V | 30A | Programmierbar | ~180 EUR |
| Victron Orion-Tr Smart 12/12-50 | 12V | 12V | 50A | Programmierbar | ~280 EUR |
| Mastervolt DC Master 12/12-25 | 12V | 12V | 25A | Fest | ~350 EUR |
| Mastervolt DC Master 12/12-50 | 12V | 12V | 50A | Fest | ~500 EUR |

### 3.3 MPPT-Solarregler

#### 3.3.1 Dimensionierungsregeln

**Schritt 1: Batterie-Spannung bestimmt die Ausgangsseite**
- 12V-System -> Regler mit 12V-Ausgang
- 24V-System -> Regler mit 24V-Ausgang
- 48V-System -> Regler mit 48V-Ausgang

**Schritt 2: Solarleistung bestimmt den Ausgangsstrom**
```
I_out = P_solar / V_batterie_absorption
Beispiel: 600Wp / 14.4V = 41.7A -> mindestens 45A-Regler wählen
```

**Schritt 3: Panel-Konfiguration bestimmt die Eingangsspannung**
```
V_in_max = Anzahl_Module_in_Serie x Voc x Temperaturkorrekturfaktor
Temperaturkorrekturfaktor: 1.15 (für -10°C) bis 1.25 (für -25°C)

Beispiel: 3 x 22V Voc x 1.20 = 79.2V -> Regler mit >=100V Eingang wählen
```

**MPPT-Regler Größentabelle:**

| Solarleistung (Wp) | 12V-System: min. Regler | 24V-System: min. Regler | Empfehlung |
|--------------------|-----------------------|-----------------------|------------|
| 100–200 | 15–20A, 75V | 10–15A, 75V | Victron SmartSolar 75/15 |
| 200–400 | 20–30A, 100V | 15–20A, 100V | Victron SmartSolar 100/30 |
| 400–600 | 30–45A, 100–150V | 20–30A, 100–150V | Victron SmartSolar 150/35 |
| 600–1000 | 50–70A, 150V | 30–45A, 150V | Victron SmartSolar 150/60 |
| 1000–1500 | 70–100A, 150–250V | 45–60A, 150–250V | Victron SmartSolar 250/100 |

### 3.4 PWM-Solarregler

PWM-Regler sind nur noch in wenigen Situationen sinnvoll:

| Situation | PWM akzeptabel? | Begründung |
|-----------|----------------|------------|
| <100Wp, kurze Kabel, 12V-Panel an 12V-Bank | Ja | Kostenersparnis, Mehrertrag MPPT gering |
| Erhaltungsladung im Winterlager | Ja | Geringe Leistung, Einfachheit |
| >200Wp oder lange Kabelwege | Nein | MPPT-Mehrertrag amortisiert sich in <1 Saison |
| 24V-Panel an 12V-Bank | Nein | PWM verschwendet >50% der Panel-Leistung |
| LiFePO4-Batterie | Nein | Präzise Ladeschlussspannung erforderlich |

**Gängige PWM-Regler (marine-tauglich):**

| Modell | Max. Strom | Max. Panel-Spannung | Batterie-Spannung | Preis |
|--------|-----------|--------------------|--------------------|-------|
| Victron BlueSolar PWM-Light 12/24-20A | 20A | 28V (12V) / 55V (24V) | 12/24V auto | ~25 EUR |
| Victron BlueSolar PWM-Pro 12/24-30A | 30A | 28V / 55V | 12/24V auto | ~55 EUR |
| Morningstar SunSaver SS-20L | 20A | 28V | 12V | ~70 EUR |
| Morningstar ProStar PS-30M | 30A | 28V / 55V | 12/24V | ~120 EUR |
| Steca Solsum 10.10F | 10A | 28V | 12V | ~30 EUR |

### 3.5 DC-DC Wandler

#### 3.5.1 Einsatzbereiche auf Yachten

| Anwendung | Wandlertyp | Typisch |
|-----------|-----------|--------|
| Starter -> Servicebatterie (Ladebooster) | 12V->12V (boost) | Sterling BB1260, Victron Orion-Tr Smart |
| 24V-Hauptbank -> 12V-Hilfsbank | 24V->12V (step-down) | Victron Orion 24/12-70, Mastervolt DC Master |
| 12V-Bank -> 24V-Windlass | 12V->24V (step-up) | Victron Orion 12/24-20, Sterling |
| Galvanische Entkopplung | Isoliert DC-DC | Victron Orion-Tr Smart (isoliert) |
| Lithium-Schutz | DC-DC mit BMS-Steuerung | Victron Orion-Tr Smart + BMS |

#### 3.5.2 Isoliert vs. Nicht-isoliert

| Eigenschaft | Nicht-isoliert | Isoliert |
|------------|---------------|---------|
| Galvanische Trennung | Nein (gemeinsame Masse) | Ja (getrennte Massen) |
| Wirkungsgrad | 95–98% | 88–94% |
| Einsatz | Gleiche Batterie-Bank, Ladebooster | Unterschiedliche Systeme, NMEA-Schutz |
| Kosten | Niedriger | Höher |
| Anwendung Yacht | Starter->Service, 24->12V Hilfsbank | Lithium/Blei-Trennung, empfindliche Elektronik |

### 3.6 Windgenerator-Regler

Windgeneratoren erzeugen dreiphasigen Wechselstrom (AC) mit variabler Frequenz und Spannung. Der Regler muss:

1. **Gleichrichten:** 3-Phasen-AC -> DC (Brückengleichrichter, integriert oder extern)
2. **Spannung begrenzen:** Bei Sturm kann die Leerlaufspannung 100V+ erreichen
3. **Überlast ableiten:** Wenn Batterie voll -> Dumpload (Heizwiderstand) oder Kurzschlussbremse
4. **Batterie-Ladeprofil:** Absorption -> Float

| Regler | Kompatibel mit | Max. Eingang | Dumpload | Batterie-Profile | Preis |
|--------|---------------|-------------|---------|-----------------|-------|
| Marlec HRSi | Rutland Windcharger | 48V AC | Intern (Heizwiderstand) | 3 Profile | ~180 EUR |
| Silentwind Hybrid | Silentwind 400+ | 60V AC | Extern (optional) | 4 Profile | ~250 EUR |
| Primus WindControl | Air Breeze, Air 40 | 65V AC | Extern (Widerstand) | 3 Profile | ~200 EUR |
| Victron SmartSolar (mit Windmodus) | 3-Phasen nach ext. Gleichrichter | 150V DC | Über Relais | Alle Victron-Profile | ~250 EUR |
| Genasun GVB (Boost) | Diverse (niedrige Spannung) | 26V DC | Nein | LiFePO4 optimiert | ~300 EUR |

**Wichtig:** Die meisten MPPT-Solarregler können **nicht** direkt an einen Windgenerator angeschlossen werden — die AC-Komponente und die Spannungsspitzen würden den Regler zerstören. Zwischen Windgenerator und Solarregler muss immer ein **Gleichrichter + Spannungsbegrenzung** geschaltet werden.

(Confidence: documented — Hersteller-Handbücher, Langfahrt-Foren)

---

## 4. Produktlinien und Spezifikationen

### 4.1 Victron Energy (Niederlande)

#### 4.1.1 Blue Smart IP22 — Standard-Landstrom-Ladegerät

Die Blue Smart IP22-Serie ist das meistverkaufte marine Ladegerät im europäischen Markt:

| Modell | Ausgangsspannung | Max. Strom | Ausgänge | Gewicht | IP-Schutz | Preis (UVP) |
|--------|-----------------|-----------|----------|---------|-----------|-------------|
| Blue Smart IP22 12/15(1) | 12V | 15A | 1 | 1.1 kg | IP22 | ~95 EUR |
| Blue Smart IP22 12/15(3) | 12V | 15A | 3 | 1.1 kg | IP22 | ~105 EUR |
| Blue Smart IP22 12/20(1) | 12V | 20A | 1 | 1.3 kg | IP22 | ~120 EUR |
| Blue Smart IP22 12/20(3) | 12V | 20A | 3 | 1.3 kg | IP22 | ~130 EUR |
| Blue Smart IP22 12/30(1) | 12V | 30A | 1 | 1.9 kg | IP22 | ~170 EUR |
| Blue Smart IP22 12/30(3) | 12V | 30A | 3 | 1.9 kg | IP22 | ~185 EUR |
| Blue Smart IP22 24/8(1) | 24V | 8A | 1 | 1.1 kg | IP22 | ~110 EUR |
| Blue Smart IP22 24/12(1) | 24V | 12A | 1 | 1.3 kg | IP22 | ~140 EUR |
| Blue Smart IP22 24/16(1) | 24V | 16A | 1 | 1.9 kg | IP22 | ~190 EUR |

**Technische Details Blue Smart IP22:**
- Eingangsspannung: 180–265V AC, 50/60 Hz
- 8 Batterie-Profile: Normal, High, Li-Ion, LiFePO4, benutzerdefiniert
- Adaptive Absorption: Absorptionsdauer passt sich an Batterie-Zustand an
- Bluetooth-Überwachung via VictronConnect App
- VE.Direct-Port (Datenlogging über Cerbo GX)
- Temperaturgesteuerte Lüfterregelung
- Storage-Modus nach 24h Float
- Keine galvanische Trennung!

#### 4.1.2 Blue Smart IP65 — Outdoor/Kompakt

| Modell | Ausgangsspannung | Max. Strom | IP-Schutz | Besonderheit | Preis |
|--------|-----------------|-----------|-----------|-------------|-------|
| Blue Smart IP65 12/5 | 12V | 5A | IP65 | Wasserdicht, mit DC-Stecker | ~65 EUR |
| Blue Smart IP65 12/7 | 12V | 7A | IP65 | Wasserdicht, mit DC-Stecker | ~75 EUR |
| Blue Smart IP65 12/10 | 12V | 10A | IP65 | Wasserdicht, mit DC-Stecker | ~90 EUR |
| Blue Smart IP65 12/15 | 12V | 15A | IP65 | Wasserdicht, mit Ringösen | ~115 EUR |
| Blue Smart IP65 12/25 | 12V | 25A | IP65 | Wasserdicht, mit Ringösen | ~165 EUR |
| Blue Smart IP65 24/8 | 24V | 8A | IP65 | Wasserdicht | ~100 EUR |
| Blue Smart IP65 24/13 | 24V | 13A | IP65 | Wasserdicht | ~140 EUR |

**Besonderheit IP65:** Vollständig wasserdicht (Strahlwasser), ideal für offene Boote, Cockpit-Montage oder Winterlager-Ladung im Freien. Integrierte Krokodilklemmen und Ringösen-Kabel im Lieferumfang.

#### 4.1.3 Phoenix Smart IP43 — Hochleistung

| Modell | Ausgangsspannung | Max. Strom | Ausgänge | Gewicht | Preis |
|--------|-----------------|-----------|----------|---------|-------|
| Phoenix Smart IP43 12/30(1+1) | 12V | 30A | 1+1 | 2.4 kg | ~215 EUR |
| Phoenix Smart IP43 12/30(3) | 12V | 30A | 3 | 2.4 kg | ~225 EUR |
| Phoenix Smart IP43 12/50(1+1) | 12V | 50A | 1+1 | 3.5 kg | ~310 EUR |
| Phoenix Smart IP43 12/50(3) | 12V | 50A | 3 | 3.5 kg | ~320 EUR |
| Phoenix Smart IP43 24/16(1+1) | 24V | 16A | 1+1 | 2.4 kg | ~230 EUR |
| Phoenix Smart IP43 24/25(1+1) | 24V | 25A | 1+1 | 3.5 kg | ~325 EUR |

**Technische Details Phoenix Smart IP43:**
- Eingangsspannung: 90–265V AC (weltweit einsetzbar)
- Bluetooth + VE.Direct
- 1+1 Ausgang: 1x voller Ladestrom + 1x 4A (Starterbatterie)
- Adaptive 8-Stufen-Ladung
- Kann parallel geschaltet werden für doppelte Leistung
- Lüftergekühlt, temperaturabhängig geregelt

#### 4.1.4 Victron SmartSolar MPPT — Solarregler

| Modell | Max. PV (12V) | Max. PV (24V) | Max. PV-Spannung | Ladestrom | Bluetooth | VE.Direct | Preis |
|--------|-------------|-------------|-----------------|-----------|-----------|-----------|-------|
| SmartSolar 75/10 | 145W | 290W | 75V | 10A | Ja | Ja | ~65 EUR |
| SmartSolar 75/15 | 220W | 440W | 75V | 15A | Ja | Ja | ~75 EUR |
| SmartSolar 100/15 | 220W | 440W | 100V | 15A | Ja | Ja | ~85 EUR |
| SmartSolar 100/20 | 290W | 580W | 100V | 20A | Ja | Ja | ~110 EUR |
| SmartSolar 100/30 | 440W | 880W | 100V | 30A | Ja | Ja | ~145 EUR |
| SmartSolar 100/50 | 700W | 1400W | 100V | 50A | Ja | Ja | ~235 EUR |
| SmartSolar 150/35 | 500W | 1000W | 150V | 35A | Ja | Ja | ~195 EUR |
| SmartSolar 150/45 | 650W | 1300W | 150V | 45A | Ja | Ja | ~265 EUR |
| SmartSolar 150/60 | 860W | 1720W | 150V | 60A | Ja | Ja | ~335 EUR |
| SmartSolar 150/70 | 1000W | 2000W | 150V | 70A | Ja | Ja | ~380 EUR |
| SmartSolar 150/85 | 1200W | 2400W | 150V | 85A | Ja | VE.Can | ~450 EUR |
| SmartSolar 150/100 | 1400W | 2800W | 150V | 100A | Ja | VE.Can | ~510 EUR |
| SmartSolar 250/60 | 860W | 1720W | 250V | 60A | Ja | VE.Can | ~420 EUR |
| SmartSolar 250/85 | 1200W | 2400W | 250V | 85A | Ja | VE.Can | ~510 EUR |
| SmartSolar 250/100 | 1400W | 2800W | 250V | 100A | Ja | VE.Can | ~580 EUR |

**Technische Details SmartSolar MPPT:**
- Ultraschneller MPP-Tracker (<5 Sekunden)
- MPPT-Effizienz: 98–99.5%
- Wandlungs-Effizienz: 95–98%
- Batterie-Profile: 8 vordefiniert + benutzerdefiniert
- Adaptive Absorption, BatteryLife-Algorithmus
- Integrierter Bluetooth für VictronConnect App
- Datenlogging (30 Tage intern)
- Parallelschaltung möglich (gleiche Modelle)
- Einsetzbar als Windgenerator-Regler mit ext. Gleichrichter (ab Firmware v1.50)

#### 4.1.5 Victron BlueSolar MPPT — Ohne Bluetooth

Identisch mit SmartSolar, aber ohne integriertes Bluetooth. Kann mit VE.Direct Bluetooth Smart Dongle (~35 EUR) nachgerüstet werden. Preisvorteil: ~15–25 EUR pro Gerät.

| Modell | Max. PV (12V) | Ladestrom | PV-Spannung | Preis |
|--------|-------------|-----------|-------------|-------|
| BlueSolar 75/15 | 220W | 15A | 75V | ~55 EUR |
| BlueSolar 100/30 | 440W | 30A | 100V | ~120 EUR |
| BlueSolar 100/50 | 700W | 50A | 100V | ~210 EUR |
| BlueSolar 150/35 | 500W | 35A | 150V | ~170 EUR |
| BlueSolar 150/45 | 650W | 45A | 150V | ~240 EUR |

#### 4.1.6 Victron Orion-Tr Smart — DC-DC Wandler/Ladebooster

| Modell | Eingang | Ausgang | Max. Strom | Isoliert | Bluetooth | Preis |
|--------|---------|---------|-----------|---------|-----------|-------|
| Orion-Tr Smart 12/12-18A | 10–17V | 12V | 18A | Ja | Ja | ~130 EUR |
| Orion-Tr Smart 12/12-30A | 10–17V | 12V | 30A | Ja | Ja | ~185 EUR |
| Orion-Tr Smart 12/12-50A (nicht-iso) | 10–17V | 12V | 50A | Nein | Ja | ~280 EUR |
| Orion-Tr Smart 12/24-15A | 10–17V | 24V | 15A | Ja | Ja | ~165 EUR |
| Orion-Tr Smart 24/12-20A | 20–35V | 12V | 20A | Ja | Ja | ~130 EUR |
| Orion-Tr Smart 24/12-30A | 20–35V | 12V | 30A | Ja | Ja | ~185 EUR |
| Orion-Tr Smart 24/24-12A | 20–35V | 24V | 12A | Ja | Ja | ~130 EUR |
| Orion-Tr Smart 24/24-25A | 20–35V | 24V | 25A | Ja | Ja | ~185 EUR |

**Technische Details Orion-Tr Smart:**
- Mehrstufiges Ladeprofil (Bulk/Absorption/Float)
- Motor-Lauferkennungsmodul (Engine Running Detection)
- Parallelschaltbar (bis zu 5 Stück)
- Fernabschaltung über VE.Direct oder BMS
- LiFePO4-Profil mit BMS-Kommunikation
- Wirkungsgrad isoliert: 88–92%, nicht-isoliert: 95–97%

### 4.2 Mastervolt (Niederlande)

#### 4.2.1 ChargeMaster Plus — Premium-Landstrom-Ladegerät

| Modell | Ausgang | Max. Strom | Ausgänge | Gewicht | CZone | Preis |
|--------|---------|-----------|----------|---------|-------|-------|
| ChargeMaster Plus 12/35-3 | 12V | 35A | 3 | 3.5 kg | Ja | ~450 EUR |
| ChargeMaster Plus 12/50-3 | 12V | 50A | 3 | 5.0 kg | Ja | ~580 EUR |
| ChargeMaster Plus 12/75-3 | 12V | 75A | 3 | 6.2 kg | Ja | ~720 EUR |
| ChargeMaster Plus 24/12-3 | 24V | 12A | 3 | 3.5 kg | Ja | ~480 EUR |
| ChargeMaster Plus 24/40-3 | 24V | 40A | 3 | 5.0 kg | Ja | ~650 EUR |
| ChargeMaster Plus 24/60-3 | 24V | 60A | 3 | 6.5 kg | Ja | ~800 EUR |
| ChargeMaster Plus 24/80-3 | 24V | 80A | 3 | 8.0 kg | Ja | ~950 EUR |

**Technische Details ChargeMaster Plus:**
- 3-Stufen+ Ladeprofil (Bulk, Absorption, Float, Auffrischung)
- 3 isolierte Ausgänge mit individueller Strombegrenzung
- CZone-Netzwerkfähig (NMEA 2000 kompatibel)
- Mastervolt MasterBus-Schnittstelle
- Fernsteuerbar über MasterAdjust Software
- Eingangsspannung: 90–265V AC
- Batterie-Erkennung: Nass, Gel, AGM, LiFePO4, Benutzerdefiniert
- 5 Jahre Garantie (registriert)

#### 4.2.2 EasyCharge — Einstieg

| Modell | Ausgang | Max. Strom | Ausgänge | Gewicht | Preis |
|--------|---------|-----------|----------|---------|-------|
| EasyCharge 10A | 12V | 10A | 1 | 0.9 kg | ~120 EUR |
| EasyCharge 15A | 12V | 15A | 1 | 1.2 kg | ~160 EUR |
| EasyCharge 25A | 12V/24V | 25A | 2 | 1.8 kg | ~250 EUR |

**Technische Details EasyCharge:**
- 3-Stufen-Ladung
- IP68 (vollständig wasserdicht, untertauchbar bis 1m)
- Ideal für offene Boote, RIBs, Beiboote
- Keine Lüfter (passiv gekühlt)
- Batterie-Profile: 3 (Nass, Gel/AGM, LiFePO4)

#### 4.2.3 Mastervolt DC Master — DC-DC Wandler

| Modell | Eingang | Ausgang | Max. Strom | Isoliert | Preis |
|--------|---------|---------|-----------|---------|-------|
| DC Master 12/12-3A | 12V | 12V | 3A | Ja | ~130 EUR |
| DC Master 12/12-6A | 12V | 12V | 6A | Ja | ~180 EUR |
| DC Master 12/12-25A | 12V | 12V | 25A | Ja | ~350 EUR |
| DC Master 12/24-7A | 12V | 24V | 7A | Ja | ~230 EUR |
| DC Master 24/12-6A | 24V | 12V | 6A | Ja | ~150 EUR |
| DC Master 24/12-12A | 24V | 12V | 12A | Ja | ~220 EUR |
| DC Master 24/12-25A | 24V | 12V | 25A | Ja | ~350 EUR |
| DC Master 24/12-50A | 24V | 12V | 50A | Ja | ~500 EUR |
| DC Master 24/12-70A | 24V | 12V | 70A | Ja | ~680 EUR |

### 4.3 Sterling Power (UK)

#### 4.3.1 Pro Charge Ultra — Landstrom-Ladegerät

| Modell | Ausgang | Max. Strom | Ausgänge | Gewicht | Preis |
|--------|---------|-----------|----------|---------|-------|
| PCU1210 | 12V | 10A | 3 | 1.6 kg | ~180 EUR |
| PCU1220 | 12V | 20A | 3 | 2.8 kg | ~250 EUR |
| PCU1230 | 12V | 30A | 3 | 3.2 kg | ~330 EUR |
| PCU1240 | 12V | 40A | 3 | 4.1 kg | ~400 EUR |
| PCU1260 | 12V | 60A | 3 | 5.5 kg | ~520 EUR |
| PCU2420 | 24V | 20A | 3 | 3.2 kg | ~350 EUR |
| PCU2430 | 24V | 30A | 3 | 4.5 kg | ~450 EUR |

**Technische Details Pro Charge Ultra:**
- 9-Stufen-Ladeprofil
- 3 isolierte Ausgänge (unabhängig einstellbar)
- Temperaturkompensation (NTC-Sensor im Lieferumfang)
- 11 Batterie-Profile inkl. LiFePO4
- CAN-Bus, NMEA 2000, USB-Monitoring
- Power Factor Correction (PFC) >0.95
- Sehr robuste Bauweise, marinisiert

#### 4.3.2 Sterling Battery-to-Battery Charger (B2B)

| Modell | Eingang | Ausgang | Max. Strom | Batterie-Profile | Preis |
|--------|---------|---------|-----------|-----------------|-------|
| BB1230 | 12V | 12V | 30A | 8 Profile | ~250 EUR |
| BB1260 | 12V | 12V | 60A | 8 Profile | ~380 EUR |
| BB12120 | 12V | 12V | 120A | 8 Profile | ~550 EUR |
| BB2430 | 24V | 24V | 30A | 8 Profile | ~300 EUR |
| BB1224-30 | 12V | 24V | 30A | 4 Profile | ~320 EUR |
| BB2412-70 | 24V | 12V | 70A | 8 Profile | ~420 EUR |

**Technische Details B2B Charger:**
- Vollständiges IUoU-Ladeprofil (Bulk/Absorption/Float)
- Motorlauferkennung (Spannungsschwelle)
- Temperaturkompensation
- Maximaler Ausgangsstrom über 50°C reduziert (Derating)
- Parallelschaltung möglich
- Input voltage lockout: Schutz der Starterbatterie

### 4.4 Balmar (USA)

#### 4.4.1 MC-614 — Externer Lichtmaschinenregler

Der Balmar MC-614 ist der verbreitetste externe Lichtmaschinenregler im nordamerikanischen Marine-Markt und zunehmend auch in Europa:

| Eigenschaft | Spezifikation |
|------------|---------------|
| Kompatible Lima-Typen | P-Type, N-Type, Dual-Internal, Isolated Ground |
| Max. Feldstrom | 8A (Standard), 12A (Heavy Duty) |
| Batterie-Profile | 18+ vordefiniert + benutzerdefiniert |
| Absorptionsspannung | 13.8–15.5V programmierbar |
| Float-Spannung | 13.0–14.0V programmierbar |
| Temperaturkompensation | Externer Sensor (im Lieferumfang) |
| Strombegrenzung | Via optionaler Shunt (Balmar SG200) |
| Drehzahlbegrenzung | Via optionaler Drehzahlsensor |
| BMS-Kommunikation | Ja (über ARS-5-II Adapter) |
| Preis | ~280 EUR |

**Konfiguration MC-614 für typische Batterien:**

| Batterie-Typ | Preset | Absorption (V) | Float (V) | Abs.-Timer | Temp.-Komp. |
|-------------|--------|---------------|----------|-----------|------------|
| Nass (Standard) | P-01 | 14.4 | 13.3 | 3h | -18 mV/°C |
| AGM (Lifeline) | P-03 | 14.4 | 13.4 | 4h | -18 mV/°C |
| Gel (Sonnenschein) | P-06 | 14.1 | 13.3 | 4h | -18 mV/°C |
| AGM (Optima Spiralzelle) | P-08 | 14.7 | 13.4 | 2h | -18 mV/°C |
| LiFePO4 (Victron) | P-14 | 14.2 | 13.5 | 1h | 0 mV/°C |
| Carbon-Blei (Firefly) | P-16 | 14.4 | 13.4 | 3h | -12 mV/°C |

#### 4.4.2 Balmar SG200 — Batteriemonitor/Shunt

In Kombination mit MC-614 ermöglicht der SG200 Shunt eine strombasierte Laderegelung:
- Misst Batteriestrom, -spannung, Temperatur
- SOC-Berechnung (Coulomb-Counting)
- MC-614 begrenzt Ladestrom anhand des Shunts
- Bluetooth-App-Monitoring
- Preis: ~250 EUR

### 4.5 Genasun (USA)

#### 4.5.1 GV-5/GV-10/GV-Boost — MPPT-Regler für LiFePO4

Genasun-Regler sind speziell für LiFePO4-Anwendungen optimiert und in der Langfahrt-Szene wegen ihrer Effizienz und Zuverlässigkeit geschätzt:

| Modell | Max. Eingang | Ladestrom | Batterie-Spannung | Effizienz | Besonderheit | Preis |
|--------|-------------|-----------|-------------------|-----------|-------------|-------|
| GV-5 | 50V/100W | 5A | 12V oder 24V | 97.5% | Ultrakompakt, keine beweglichen Teile | ~150 EUR |
| GV-10 | 50V/140W | 10.5A | 12V | 97.5% | Meistverkauft für Langfahrt | ~200 EUR |
| GVB-8-25.2 | 26V (Boost) | 8A | 24V (LiFePO4) | 96% | Boost-Regler für Windgeneratoren | ~300 EUR |
| GV-16 | 50V/200W | 16A | 12V | 97% | Für größere Anlagen | ~280 EUR |

**Besonderheiten Genasun:**
- Kein Lüfter, keine beweglichen Teile -> lautlos
- Vergossen (potted) -> vollständig wasserdicht
- Fest eingestellte Ladeschlussspannung (bei Bestellung angeben)
- Keine App, kein Bluetooth, kein Display -> maximale Einfachheit
- Extrem hoher Wirkungsgrad auch bei Teillast
- Made in USA, 5 Jahre Garantie

### 4.6 Morningstar (USA)

#### 4.6.1 Morningstar-Regler — Industriequalität

| Modell | Typ | Max. Strom | Max. Spannung | Display | Besonderheit | Preis |
|--------|-----|-----------|--------------|---------|-------------|-------|
| SunSaver SS-6L-12V | PWM | 6A | 28V | LED | Einfachst, robust | ~45 EUR |
| SunSaver SS-20L-12V | PWM | 20A | 28V | LED | Marine-Klassiker | ~70 EUR |
| ProStar PS-30M | PWM | 30A | 28V/55V | LCD + Meter | Professionell | ~120 EUR |
| SunStar SS-MPPT-15L | MPPT | 15A | 75V | LED | Kompakt-MPPT | ~130 EUR |
| TriStar TS-MPPT-30 | MPPT | 30A | 150V | LED | Industriestandard | ~280 EUR |
| TriStar TS-MPPT-45 | MPPT | 45A | 150V | LED | Für große Anlagen | ~380 EUR |
| TriStar TS-MPPT-60 | MPPT | 60A | 150V | LED | Maximum | ~450 EUR |

**Besonderheiten Morningstar:**
- Extrem robuste Bauweise (Militär/Marine-Heritage)
- Vergossene Elektronik (EpicPWM, TrakStar MPPT)
- 5 Jahre Garantie, typische Lebensdauer >15 Jahre
- MeterBus-Schnittstelle für Remote-Display
- TriStar-Serie mit Ethernet/Modbus-Monitoring
- Weit verbreitet auf Langfahrtyachten und kommerziellen Schiffen

(Confidence: measured — Hersteller-Datenblätter und -Preislisten 2025/2026)

### 4.8 Vergleichsmatrix: Landstrom-Ladegeräte nach Leistungsklasse

#### 4.8.1 Klasse 15–20A (Kleine Segelboote, Beiboote, Erhaltungsladung)

| Kriterium | Victron Blue Smart IP22 12/20 | Mastervolt EasyCharge 12/16 | Sterling Pro Charge B 12/20 | CTEK M25 EU |
|-----------|-------------------------------|-----------------------------|-----------------------------|-------------|
| Max. Ladestrom | 20A | 16A | 20A | 25A |
| Ausgänge | 1 oder 3 | 2 | 3 | 1 |
| Batterie-Profile | 8 (inkl. LiFePO4) | 4 (inkl. Lithium) | 5 | 8 |
| Adaptive Absorption | Ja (Tailcurrent) | Ja | Ja | Ja |
| Temperaturkompensation | Ja (Sensor inkl.) | Ja (Sensor optional) | Ja (Sensor inkl.) | Nein (intern) |
| Bluetooth/App | Ja (VictronConnect) | Nein | Nein | Nein (nur neue Modelle) |
| Galvanische Trennung | Nein | Nein | Nein | Nein |
| IP-Schutz | IP22 | IP21 | IP21 | IP65 |
| Gewicht | 1,3 kg | 1,8 kg | 2,1 kg | 2,3 kg |
| Preis (ca.) | 130 EUR | 180 EUR | 190 EUR | 200 EUR |
| **AYDI-Empfehlung** | **1. Wahl** | Wenn Mastervolt-System | Budget mit 3 Ausgängen | Outdoor/Spritzwasser |

#### 4.8.2 Klasse 30–50A (Standard-Fahrtenyachten, 10–14m)

| Kriterium | Victron Blue Smart IP22 12/30 | Victron Phoenix 12/50 | Mastervolt ChargeMaster Plus 12/35 | Sterling Pro Charge Ultra 12/40 |
|-----------|-------------------------------|----------------------|-------------------------------------|---------------------------------|
| Max. Ladestrom | 30A | 50A | 35A | 40A |
| Ausgänge | 3 | 1 (+ Trickle) | 3 | 3 |
| Batterie-Profile | 8 | 8 | 6 | 5 |
| Adaptive Absorption | Ja | Ja | Ja | Ja |
| Temperaturkompensation | Ja (inkl.) | Ja (inkl.) | Ja (optional) | Ja (inkl.) |
| Bluetooth/App | Ja | Ja | Nein (MasterConnect bei Plus) | Nein |
| VE.Direct/Bus | Ja | Ja (VE.Direct) | MasterBus (optional) | Nein |
| Galvanische Trennung | Nein | Nein | Nein | Nein |
| IP-Schutz | IP22 | IP43 | IP23 | IP21 |
| Wirkungsgrad | 94% | 95% | 93% | 92% |
| Gewicht | 1,9 kg | 5,5 kg | 4,2 kg | 5,1 kg |
| Lüfter | Temperaturgesteuert | Temperaturgesteuert | Immer an | Immer an |
| Preis (ca.) | 200 EUR | 420 EUR | 480 EUR | 380 EUR |
| **AYDI-Empfehlung** | **Preis-Leistung** | **Performance** | Premium/MasterBus | UK-Markt/Budget |

#### 4.8.3 Klasse 70–100A (Große Yachten, Katamarane, Schnellladung LiFePO4)

| Kriterium | Victron Phoenix 12/75 | Mastervolt ChargeMaster Plus 12/75 | Sterling Pro Charge Ultra 12/60 |
|-----------|----------------------|-------------------------------------|--------------------------------|
| Max. Ladestrom | 75A | 75A | 60A |
| Eingangsstrom (230V) | 4,5A | 4,8A | 3,8A |
| Ausgänge | 1 + Trickle | 3 isoliert | 3 |
| LiFePO4-Profil | Ja | Ja | Ja |
| Wirkungsgrad | 95% | 94% | 93% |
| Lüfter-Geräusch | <40 dB(A) | <45 dB(A) | ~50 dB(A) |
| Abmessungen (mm) | 350x160x100 | 406x214x103 | 380x180x120 |
| Gewicht | 7,5 kg | 9,8 kg | 8,2 kg |
| Preis (ca.) | 580 EUR | 850 EUR | 530 EUR |
| Zulassungen | CE, RCM | CE, Lloyds, BV | CE, UKCA |
| **AYDI-Empfehlung** | **1. Wahl Marine** | Superyacht/Klasse | Budget/Leistung |

### 4.9 Vergleichsmatrix: MPPT-Solarregler (Klasse 15–30A)

| Kriterium | Victron SmartSolar 100/20 | Victron SmartSolar 100/30 | Mastervolt SCM60 | Genasun GV-10 | Morningstar SunSaver MPPT 15L |
|-----------|---------------------------|---------------------------|-----------------|---------------|-------------------------------|
| Max. PV-Strom | 20A | 30A | 30A (60V max PV) | 10A | 15A |
| Max. PV-Spannung | 100V | 100V | 60V | 26V | 75V |
| Max. PV-Leistung (12V) | 290Wp | 440Wp | 400Wp | 130Wp | 200Wp |
| MPPT-Effizienz | 99,5% | 99,5% | 98,5% | 99,2% | 99,0% |
| Eigenstromverbrauch | 10mA | 10mA | 25mA | 8mA | 15mA |
| Batterie-Profile | Alle (App) | Alle (App) | 4 fest | LiFePO4 only | 4 (DIP-Switch) |
| Bluetooth | Ja | Ja | Nein | Nein | Nein |
| VE.Direct | Ja | Ja | Nein | Nein | Nein (MeterBus) |
| Display | Via App | Via App | LED | LED | LED |
| Schutzart | IP43 | IP43 | IP21 | IP67 | IP44 |
| Gewicht | 0,65 kg | 1,1 kg | 1,5 kg | 0,07 kg (!) | 0,35 kg |
| Preis (ca.) | 130 EUR | 180 EUR | 350 EUR | 280 EUR | 130 EUR |
| **AYDI-Empfehlung** | Standard bis 200Wp | **Standard 200-400Wp** | Nur Mastervolt-System | Ultra-Leicht/Regatta | Off-Grid/Robust |

### 4.10 Vergleichsmatrix: DC-DC-Wandler / B2B-Charger

| Kriterium | Victron Orion-Tr Smart 12/12-30 | Sterling BB1260 | Mastervolt DC Master 12/12-24 | CTEK D250SE |
|-----------|--------------------------------|-----------------|-------------------------------|-------------|
| Max. Ausgangsstrom | 30A (360W) | 60A (720W) | 24A (288W) | 20A (240W) |
| Galvanische Trennung | Ja (isoliert) | Ja (isoliert) | Ja (isoliert) | Nein |
| Motor-Erkennung | Ja (Spannung oder D+) | Ja (D+ Signal) | Ja (D+ Signal) | Ja (Smart Alternator) |
| LiFePO4-Profil | Ja (App-konfigurierbar) | Ja (DIP-Switch) | Ja | Ja |
| Bluetooth/App | Ja (VictronConnect) | Nein | Nein | Nein |
| Smart Alternator kompatibel | Ja (ab 11,8V Start) | Ja (mit Mod) | Eingeschränkt | Ja (Hauptfeature) |
| VE.Direct | Nein | Nein | Nein | Nein |
| Parallelschaltung | Ja (bis 3x) | Nein | Nein | Nein |
| Schutzart | IP43 | IP21 | IP21 | IP65 |
| Temperatur-Derating | Ab 40°C | Ab 45°C | Ab 40°C | Ab 40°C |
| Gewicht | 1,5 kg | 3,2 kg | 1,8 kg | 0,9 kg |
| Preis (ca.) | 220 EUR | 380 EUR | 350 EUR | 280 EUR |
| **AYDI-Empfehlung** | **1. Wahl (Victron-System)** | Hochstrom-Bedarf | Mastervolt-System | Smart Alternator Fix |

### 4.11 Vergleichsmatrix: Externe Lichtmaschinenregler

| Kriterium | Balmar MC-614 | Wakespeed WS500 | Sterling Advanced Alt. Reg. | Mastervolt Alpha Pro III |
|-----------|---------------|-----------------|-----------------------------|-----------------------|
| Max. Feldstrom | 8A | 10A | 6A | 6A |
| Batterie-Profile | 10 (Drehschalter) | Unbegrenzt (App) | 5 (DIP-Switch) | 4 (DIP-Switch) |
| LiFePO4 | Ja (Profil 10) | Ja (mit BMS-Komm.) | Ja | Ja |
| Temperatursensor LiMa | Ja (inkl.) | Ja (inkl.) | Optional | Nein |
| Temperatursensor Batterie | Ja (inkl.) | Ja (inkl.) | Ja (inkl.) | Ja (inkl.) |
| BMS-Kommunikation | Nein (nur Spannung) | Ja (CAN-Bus/NMEA2000/VE.Can) | Nein | Nein (nur MasterBus) |
| DVCC-kompatibel | Nein | Ja (VE.Can) | Nein | Ja (MasterBus) |
| NMEA 2000 | Nein | Ja (Ladedaten sichtbar) | Nein | Nein |
| Belt Manager | Ja (Soft-Ramp) | Ja (konfigurierbar) | Nein | Nein |
| Überspannungsschutz | Ja (16,5V Cutoff) | Ja (konfigurierbar) | Ja (15,5V) | Ja (16V) |
| Display/Feedback | SG200 erforderlich | Bluetooth App | LED | LED |
| Preis (ca.) | 280 EUR (+SG200: 180) | 500 EUR | 180 EUR | 250 EUR |
| **AYDI-Empfehlung** | Bewährt/US-Standard | **1. Wahl LiFePO4/Victron** | Budget | Mastervolt-System |

(Confidence: measured — Hersteller-Datenblätter, verifizierte Preisinformationen 2025)

---

## 5. Hersteller-Datenbank

### 5.1 Victron Energy (Niederlande)

| Eigenschaft | Detail |
|-------------|--------|
| Vollständiger Name | Victron Energy B.V. |
| Hauptsitz | Almere, Niederlande |
| Gegründet | 1975 |
| Marine-Fokus | ca. 40% des Umsatzes, Marine ist Kernmarkt neben Off-Grid |
| Hauptprodukte | Blue Smart IP22/IP65, Phoenix Smart IP43, SmartSolar MPPT, BlueSolar MPPT, Orion-Tr Smart, MultiPlus/Quattro, Cerbo GX |
| Zulassungen | CE, RCM, FCC, UL (ausgewählte Modelle) |
| Vertrieb Europa | SVB (D), Compass24 (D), Bukh Bremen (D), Victron Direkt, Amazon, Defender, Budget Marine |
| Preisniveau | Mittel-Premium (bestes Preis-Leistungs-Verhältnis im Marine-Segment) |
| Ökosystem | VE.Direct, VE.Can, VE.Bus, VRM Portal, Bluetooth App, DVCC, Cerbo GX/Touch |
| Stärken | Größtes Ökosystem, hervorragende App, offene Protokolle, VRM-Cloud-Monitoring, starke Community, guter Support, hohe Verfügbarkeit |
| Schwächen | Gehäusequalität unter Mastervolt-Niveau, manche Modelle ohne IP67, Bluetooth-Reichweite begrenzt |
| Marktanteil Marine (EU) | ca. 45–55% (geschätzt) |
| Website | victronenergy.com |

### 5.2 Mastervolt (Niederlande)

| Eigenschaft | Detail |
|-------------|--------|
| Vollständiger Name | Mastervolt International B.V. |
| Muttergesellschaft | AVNET (seit 2021, vorher CTP/Actuant) |
| Hauptsitz | Amsterdam, Niederlande |
| Gegründet | 1991 |
| Marine-Fokus | ca. 60% Marine/Superyacht, Rest Off-Grid und Mobil |
| Hauptprodukte | ChargeMaster Plus, EasyCharge, Mass Combi Ultra, DC Master, SCM60 MPPT, Alpha Pro III |
| Zulassungen | CE, Lloyds, BV, DNV (Superyacht-Zulassungen) |
| Vertrieb Europa | SVB, Compass24, Bukh Bremen, Marinelektronik Händler, direkt |
| Preisniveau | Premium-Hoch (20–40% über Victron) |
| Ökosystem | MasterBus, CZone (Digital Switching), EasyView, MasterConnect App |
| Stärken | Superyacht-Segment, Klassifikationsgesellschafts-Zulassungen, hervorragende Verarbeitungsqualität, leise Lüfter, bewährtes MasterBus-System |
| Schwächen | Höherer Preis, kleinereres Community-Ökosystem als Victron, App weniger intuitiv, MasterBus proprietär |
| Marktanteil Marine (EU) | ca. 20–25% (geschätzt, stärker im Superyacht-Bereich) |
| Website | mastervolt.com |

### 5.3 Sterling Power Products (UK)

| Eigenschaft | Detail |
|-------------|--------|
| Vollständiger Name | Sterling Power Products Ltd. |
| Hauptsitz | Bishop's Stortford, England, UK |
| Gegründet | 1995 |
| Marine-Fokus | ca. 70% Marine, Rest Fahrzeug/Off-Grid |
| Hauptprodukte | Pro Charge Ultra, Pro Charge B (Budget), B2B Charger (BB1260), Advanced Alternator Regulator, Power Management Panel |
| Zulassungen | CE, UKCA |
| Vertrieb Europa | Sterling Direkt (UK), SVB (D), Toplicht (D), Budget Marine (Karibik) |
| Preisniveau | Mittel (oft günstiger als Victron bei vergleichbarer Leistung) |
| Ökosystem | Sterling Power Management System, kein Cloud-Monitoring |
| Stärken | Exzellentes Preis-Leistungs-Verhältnis, robuste Bauweise, B2B-Charger-Pionier, gute UK-Community |
| Schwächen | Kein Cloud-Monitoring, keine App (bei älteren Modellen), Design etwas veraltet, Verfügbarkeit in Kontinentaleuropa eingeschränkt |
| Marktanteil Marine (EU) | ca. 8–12% (stärker in UK) |
| Website | sterling-power.com |

### 5.4 Balmar (USA)

| Eigenschaft | Detail |
|-------------|--------|
| Vollständiger Name | Balmar Products |
| Muttergesellschaft | Genco Industries |
| Hauptsitz | Springfield, Oregon, USA |
| Gegründet | 1983 |
| Marine-Fokus | 100% Marine — Lichtmaschinen und Regler |
| Hauptprodukte | MC-614 Regulator, SG200 SmartGauge, ARS-5 Regulator, XT-Serie Lichtmaschinen, Duo Charge |
| Zulassungen | CE (ausgewählte), SAE, ABYC-konform |
| Vertrieb Europa | Importeure (z.B. TopSpark Marine/NL, SVB/D), Yachtausrüster |
| Preisniveau | Premium (Import-Aufschlag in Europa) |
| Ökosystem | MC-614 + SG200 + Duo Charge (integriertes System) |
| Stärken | Unangefochtener Standard im US-Segelmarkt, hervorragende Lichtmaschinen-Kompatibilität, bewährte Technik, einfache Installation |
| Schwächen | Kein Bluetooth/Cloud, älteres Display-Design, in Europa schwer verfügbar, teuer |
| Marktanteil Marine (EU) | ca. 3–5% (primär US-Import-Yachten und Langfahrer) |
| Website | balmar.net |

### 5.5 Wakespeed (USA)

| Eigenschaft | Detail |
|-------------|--------|
| Vollständiger Name | Wakespeed Offshore |
| Hauptsitz | Ferndale, Washington, USA |
| Gegründet | 2018 |
| Marine-Fokus | 100% Marine — Lichtmaschinen-Regulator-Technologie |
| Hauptprodukte | WS500 Advanced Regulator, WS500-LiFePO4, WS500-Alternator Kits |
| Zulassungen | CE, FCC |
| Vertrieb Europa | Importeure, Victron-Händler (DVCC-kompatibel), Online-Shops |
| Preisniveau | Premium (ca. 450–650 EUR für WS500) |
| Ökosystem | NMEA 2000, VE.Can (Victron-Integration), Bluetooth App, RVC (RV-C) |
| Stärken | Modernster Lichtmaschinen-Regler der Welt, native Victron-Integration (DVCC), LiFePO4-optimiert, Temperaturüberwachung, CAN-Bus-Integration |
| Schwächen | Teuer, relativ junges Unternehmen, komplexe Konfiguration, Verfügbarkeit |
| Marktanteil Marine (EU) | ca. 2–3% (stark wachsend bei Lithium-Umbauten) |
| Website | wakespeed.com |

### 5.6 Genasun (USA)

| Eigenschaft | Detail |
|-------------|--------|
| Vollständiger Name | Genasun LLC |
| Hauptsitz | Cambridge, Massachusetts, USA |
| Gegründet | 2008 |
| Marine-Fokus | ca. 50% Marine, Rest Off-Grid/Expedition |
| Hauptprodukte | GV-4, GV-5, GV-10, GV-Boost (MPPT-Regler für kleine bis mittlere Anlagen) |
| Zulassungen | CE, FCC |
| Vertrieb Europa | Spezialhändler, Online (Marlec, Merlin Equipment UK) |
| Preisniveau | Premium-Hoch (für die Leistungsklasse der teuerste Anbieter) |
| Ökosystem | Minimalistisch — kein Bluetooth, keine App (Standalone) |
| Stärken | Höchste MPPT-Effizienz der Branche (99,2% behauptet), kleinste Bauform, lüfterlos, wasserdicht (IP67), Made in USA |
| Schwächen | Teuer, keine Bluetooth-Überwachung, kleines Produktportfolio, geringe Verfügbarkeit in EU, nur bis 350W |
| Marktanteil Marine (EU) | ca. 1–2% (Nische: Langfahrer, Regatta-Yachten) |
| Website | genasun.com |

### 5.7 Morningstar Corporation (USA)

| Eigenschaft | Detail |
|-------------|--------|
| Vollständiger Name | Morningstar Corporation |
| Hauptsitz | Newtown, Pennsylvania, USA |
| Gegründet | 1993 |
| Marine-Fokus | ca. 10% Marine, Rest Off-Grid/Telekom/Industrie |
| Hauptprodukte | TriStar MPPT, SunSaver MPPT, ProStar MPPT, SunSaver SS, SunLight |
| Zulassungen | UL, CE, ETL |
| Vertrieb Europa | Elektro-Großhandel, Solar-Fachhändler, online |
| Preisniveau | Mittel (gutes Preis-Leistungs-Verhältnis) |
| Ökosystem | MSView Software, Modbus RTU/TCP, SNMP |
| Stärken | Bulletproof-Zuverlässigkeit (Telekom-Erbe), hervorragende Modbus-Integration, konfigurierbares Ladeprofil, UL-Zertifizierung |
| Schwächen | Kein Bluetooth (nur bei neuesten Modellen), Design auf Industrie/Telekom ausgelegt (nicht Marine-spezifisch), weniger Marine-Community |
| Marktanteil Marine (EU) | ca. 3–5% (beliebt bei technisch versierten Eignern) |
| Website | morningstarcorp.com |

### 5.8 CTEK (Schweden)

| Eigenschaft | Detail |
|-------------|--------|
| Vollständiger Name | CTEK Sweden AB |
| Hauptsitz | Vikmanshyttan, Schweden |
| Gegründet | 1997 |
| Marine-Fokus | ca. 15% Marine, Rest Automobil/Industrie |
| Hauptprodukte | M25 EU, M15, M45, D250SE (DC-DC), SmartPass 120S |
| Zulassungen | CE, IP65 (ausgewählte Modelle) |
| Vertrieb Europa | Breit verfügbar — ATU, Amazon, Bootszubehör, Marine-Shops |
| Preisniveau | Mittel (gute Verfügbarkeit drückt Preise) |
| Ökosystem | CTEK Sense Connect, Bluetooth bei neueren Modellen |
| Stärken | Hervorragende Einstiegs-Ladegeräte, bewährte 8-Stufen-Ladekennlinie, sehr gute Erhaltungsladung, IP65 für Spritzwasser, breite Verfügbarkeit |
| Schwächen | Eher Automobil-Fokus, begrenzte Leistung (max 45A), kein Marine-Ökosystem, keine Netzwerkfähigkeit |
| Marktanteil Marine (EU) | ca. 5–8% (hauptsächlich kleinere Boote, Winterlagerung, Erhaltungsladung) |
| Website | ctek.com |

(Confidence: documented — Hersteller-Websites, Fachmessen, Forum-Konsens, Preisvergleiche 2024/2025)

---

## 6. Fehlerbild-Atlas

### 6.1 Fehlerbild: Überladung — Gasung und Elektrolyt-Verlust (Blei-Batterien)

**Beschreibung:** Batterien gasen exzessiv (H2 + O2), Elektrolytstand sinkt schnell, starker Geruch nach Schwefelwasserstoff, Batteriepole korrodieren massiv, Gehäuse kann sich aufblähen.

**Ursache:**
- Absorptionsspannung zu hoch eingestellt (>14,8V bei Nassbatterien, >14,4V bei AGM)
- Temperatursensor defekt oder nicht angeschlossen (keine Kompensation bei Hitze)
- Egalisierungsspannung wird dauerhaft angelegt (Timer-Fehler im Laderegler)
- Ladegerät-Defekt: Spannungsregelung ausgefallen, Ladegerät liefert unkontrolliert

**Typische Konstellation:**
- Landstrom-Ladegerät ohne Temperatursensor + südliche Klimata (>35°C Maschinenraum)
- Ältere Ladegeräte ohne adaptive Absorption (feste Zeitsteuerung)
- PWM-Solarregler mit falschem Batterieprofil (Gel-Profil auf Nassbatterie)

**Auswirkungen:**
- Massive Verkürzung der Batterielebensdauer (statt 5 Jahre nur 1–2 Jahre)
- Wasserstoff-Entwicklung im Batterieraum — Explosionsgefahr!
- Korrosion aller Metallteile im Batterieabteil
- Elektrolytmangel legt Platten frei — irreversible Sulfatierung

**Diagnose:**
- Visuell: Weiße kristalline Ablagerungen an Batteriepolen, feuchte Batterieoberfläche
- Messung: Ladespannung >14,4V bei AGM oder >14,8V bei Nassbatterie (12V-System, 25°C)
- Wasserverbrauch: Nachfüllen häufiger als 1× pro 3 Monate deutet auf Überladung
- Ladegerät-Log (Victron VRM): Absorptionsspannung und -dauer prüfen

**Behebung:**
1. Absorptionsspannung gemäß Batteriehersteller-Vorgabe einstellen
2. Temperatursensor installieren (direkt auf Batteriegehäuse)
3. Adaptive Absorption aktivieren (Tailcurrent-Abschaltung bei <2% C10)
4. Egalisierungs-Timer auf max. 1h begrenzen (nur bei Nassbatterien)
5. Wenn Batterie bereits geschädigt: Kapazitätstest, ggf. ersetzen

**AYDI-Bewertung:**
- Confidence: visual_medium (Gasung nicht direkt fotografierbar, aber Korrosionsfolgen ja)
- Severity: KRITISCH (Explosionsgefahr + Batterieschaden)
- Repair urgency: sofort

### 6.2 Fehlerbild: Sulfatierung durch chronische Unterladung

**Beschreibung:** Weiße bis gelbliche PbSO4-Kristalle auf den Platten, Batterie nimmt kaum noch Strom an, Ruhespannung nach vermeintlich voller Ladung unter 12,5V, Kapazität <60% der Nennkapazität.

**Ursache:**
- Float-Spannung zu niedrig eingestellt (<13,2V bei 12V-Systemen)
- Absorption zu kurz (Timer-basiert statt Tailcurrent-basiert)
- Solaranlage unterdimensioniert — Batterie erreicht nie 100% SOC
- Lichtmaschine: Fahrtzeit zu kurz für Volladung (typisch: 1–2h Motoren pro Tag reicht nicht)
- Mehrere Ladequellen mit unterschiedlichen (zu niedrigen) Spannungen

**Typische Konstellation:**
- Langfahrt-Yacht mit unterdimensionierter Solaranlage und wenig Motorbetrieb
- Charterboot mit häufigen kurzen Motorläufen zwischen Ankerbuchten
- Saisonboot ohne Erhaltungsladung im Winterlager

**Auswirkungen:**
- Progressive Kapazitätsminderung — zuerst unmerklich, dann rapide
- Batterie erreicht schneller die Entladegrenze (scheinbar kleinere Bank)
- Sulfatierung ist ab gewissem Grad irreversibel
- Scheinbar intakte Batterie versagt bei der ersten höheren Belastung

**Diagnose:**
- Ruhespannung nach 4h: 12,4V oder weniger trotz vermeintlich voller Ladung
- Kapazitätstest (C/20): <80% = Lebensende, <60% = schwere Sulfatierung
- Ladeverhalten: Batterie geht sofort in Float (nimmt keinen Bulk-Strom an)
- Innenwiderstand-Messung: deutlich erhöht gegenüber Neuwert

**Behebung:**
1. Leichte Sulfatierung: Egalisierung bei 15,5–16,0V für 2–4h (NUR Nassbatterien!)
2. Mittlere Sulfatierung: Desulfatierungs-Programm (pulse charging) über 24–72h
3. Schwere Sulfatierung: Batterie ersetzen — nicht mehr rettbar
4. Ursache beheben: Absorptionsspannung und -dauer korrekt einstellen
5. Tailcurrent-basierte Abschaltung aktivieren (Absorption endet bei <1–2% C10)

**AYDI-Bewertung:**
- Confidence: measured (Kapazitätstest + Spannungsmessung)
- Severity: HOCH (Batterie-Totalausfall absehbar)
- Repair urgency: 1–4 Wochen

### 6.3 Fehlerbild: MPPT-Regler im Fehler-Modus — kein Solarertrag

**Beschreibung:** Solarregler zeigt Fehlercode an (LED blinkt Rot, App zeigt "Fehler"), keine Leistungsabgabe trotz Sonnenschein, Panel-Spannung am Reglereingang liegt an, aber keine Ausgangsspannung/-strom.

**Ursache:**
- Überspannung am PV-Eingang (Voc bei Kälte > max. Vin des Reglers)
- Kurzschluss oder Erdschluss am PV-Eingang
- Batterie-Überspannung (BMS hat Ladung abgeschaltet, Spannung steigt)
- Übertemperatur des Reglers (unbelüftete Montage in heißem Raum)
- Verpolter Anschluss (bei Erstinstallation oder nach Arbeiten)

**Typische Konstellation:**
- Herbst/Winter: Paneltemperatur <0°C erhöht Voc um 5–15% über Datenblatt-STC-Wert
- Regler im unbelüfteten Backskisten-Raum hinter dem Cockpit
- LiFePO4-System: BMS trennt bei 14,6V, Regler sieht plötzlich offene Last

**Auswirkungen:**
- Kompletter Solarertrag-Ausfall bis Fehler quittiert wird
- Bei Voc-Überschreitung: möglicherweise Zerstörung des MPPT-Reglers
- Bei thermischer Abschaltung: nur temporär, aber ertragsmindend

**Diagnose:**
- VictronConnect/App: Fehlercode ablesen (z.B. #Error 33 = PV over-voltage)
- PV-Leerlaufspannung am Reglereingang messen (alle Strings einzeln!)
- Reglergehäuse-Temperatur fühlen/messen (>65°C = thermisches Problem)
- Batterieseitige Spannung prüfen (BMS-Abschaltung?)

**Behebung:**
1. Fehlercode identifizieren und Ursache beheben
2. PV-Überspannung: String-Konfiguration ändern (weniger Module in Serie)
3. Thermisch: Montageort belüften oder Regler an kühleren Ort umsetzen
4. BMS-Abschaltung: Victron DVCC konfigurieren (BMS-kontrolliertes Laden)
5. Regler-Reset: Batterie- und PV-Anschluss trennen (30s), dann Batterie zuerst anschließen

**AYDI-Bewertung:**
- Confidence: visual_high (LED-Status/App-Screenshot klar erkennbar)
- Severity: MITTEL (kein Sicherheitsrisiko, aber Ertragsverlust)
- Repair urgency: 1–7 Tage

### 6.4 Fehlerbild: Galvanische Korrosion durch fehlendes Trenntrafo

**Beschreibung:** Massive Korrosion am Unterwasserschiff (Propellerwelle, Saildrive-Anode, Ruderschaft) bei Booten, die dauerhaft am Landstrom hängen. Zinkanoden lösen sich in Wochen statt Monaten auf.

**Ursache:**
- Landstrom-Ladegerät ohne galvanische Trennung verbindet den Schutzleiter (PE) mit dem Bordnetz
- Über die Hafeninstallation fließen Streuströme zwischen verschiedenen Booten
- Potentialunterschiede zwischen Booten erzeugen galvanische Elemente über das Hafenwasser
- Fehlende oder falsch dimensionierte Galvanic Isolator (Sperrdioden-Typ unzureichend)

**Typische Konstellation:**
- Dauerlieger im Hafen mit permanentem Landstromanschluss
- Ältere Häfen mit schlechter Erdung oder defekten Nachbar-Booten
- Boot mit blanker Propellerwelle (Bronze) neben Boot mit verzinktem Stahlrumpf
- Ladegerät ohne Trenntransformator (Nicht-isolierter Typ)

**Auswirkungen:**
- Zinkanoden aufgezehrt in 4–8 Wochen statt 12–18 Monaten
- Propeller-Korrosion (Pitting) — teurer Austausch
- Saildrive-Korrosion — Undichtigkeit, Wassereinbruch
- Borddurchbrüche und Seeventile angegriffen

**Diagnose:**
- Silber-Silberchlorid-Referenzelektrode: Ruhepotential des Rumpfes messen
- Strom-Messzange am Landstromkabel: AC/DC-Leckstrom >50mA ist verdächtig
- Zinkanoden-Verbrauch dokumentieren (>2mm/Monat = Strom-Problem)
- Nachbarboot-Potentiale vergleichen

**Behebung:**
1. Galvanic Isolator (z.B. Victron GI, Sterling ProGI) in die PE-Leitung einbauen
2. Besser: Trenntransformator (z.B. Victron Isolation Transformer 3600W) installieren
3. Mastervolt Galvanic Isolator GI 32/50 als Alternative
4. Regelmäßige Anodenkontrolle (alle 3 Monate im Wasser)
5. Bei schweren Fällen: professionelle Strom-Survey durch Korrosionsexperten

**AYDI-Bewertung:**
- Confidence: visual_medium (Anodenverbrauch messbar, Korrosion unter Wasser)
- Severity: KRITISCH (strukturelle Schäden am Unterwasserschiff)
- Repair urgency: sofort (Galvanic Isolator) + Haul-Out (Inspektion)

### 6.5 Fehlerbild: Lichtmaschine kocht Batterien — defekter interner Regler

**Beschreibung:** Lichtmaschine liefert unkontrolliert hohe Spannung (>15V), Batterien gasen heftig, Sicherungen können durchbrennen, elektronische Geräte erhalten Überspannung.

**Ursache:**
- Interner Spannungsregler der Lichtmaschine defekt (Durchbruch = voller Feldstrom)
- Schlechte Masseverbindung am Regler (Regler sieht zu niedrige Spannung, regelt hoch)
- Kontaktfederung im Kohlehalter verschlissen (intermittierend)
- Sense-Leitung am externen Regler abgerissen (misst 0V, gibt Vollgas)

**Typische Konstellation:**
- Ältere Lichtmaschine (>10 Jahre) mit internem Regler
- Boot in tropischem Klima (Hitze beschleunigt Regler-Alterung)
- Nach Motorarbeiten: Kabelverbindung am Regler vergessen/gelöst
- Billig-Lichtmaschine (Marine-Schönschrift auf Automobil-Ware)

**Auswirkungen:**
- Batterie-Überladung bis zum Kochen (akute Gefahr!)
- Elektronik-Schäden (Chartplotter, AIS, VHF, Autopilot)
- Kabelbrand bei extremer Überspannung
- Lichtmaschine selbst kann bei Vollfeldstrom überhitzen und ausfallen

**Diagnose:**
- Multimeter an Batterie bei laufendem Motor: >14,6V (12V-System) = zu hoch
- Schwankende Spannung bei Drehzahländerung = Regler-Problem
- Infrarot-Thermometer: Regler/Lichtmaschine >100°C = überlastet
- Externen Regler anschließen: Feldstrom-Klemme (F/DF) messen

**Behebung:**
1. Sofort: Motor abstellen, wenn >15,5V gemessen werden!
2. Kurzfristig: Feldstrom-Kabel von Lichtmaschine trennen (= keine Ladung, aber sicher)
3. Interner Regler ersetzen (Bosch, Valeo, Prestolite — je nach LiMa-Typ)
4. Langfristig: Externen Regler installieren (Balmar MC-614, Wakespeed WS500, Sterling AR)
5. Überspannungsschutz nachrüsten (Sterling LPVD — Low-Voltage-Disconnect mit Overvoltage)

**AYDI-Bewertung:**
- Confidence: measured (Spannungsmessung bei laufendem Motor)
- Severity: KRITISCH (Explosionsgefahr, Elektronikschäden)
- Repair urgency: sofort

### 6.6 Fehlerbild: DC-DC-Wandler überhitzt und drosselt

**Beschreibung:** DC-DC-Wandler (B2B-Charger) erreicht nicht die spezifizierte Ausgangsleistung, reduziert den Ausgangsstrom nach einigen Minuten drastisch, Gehäuse extrem heiß (>70°C).

**Ursache:**
- Montage ohne ausreichende Belüftung (horizontale Montage mit Lüfter nach unten)
- Umgebungstemperatur >40°C (Maschinenraum)
- Eingangsspannung zu niedrig (Wandler muss härter arbeiten)
- Dauerentnahme bei Nennleistung (manche Wandler spezifizieren Nennleistung nur für 50% Duty Cycle)

**Typische Konstellation:**
- Sterling B2B 1260 im unbelüfteten Maschinenraum hinter dem Motor
- Victron Orion-Tr Smart auf Holzplatte montiert (keine Wärmeableitung)
- Langer Ladezyklus (>2h) bei voller Nennleistung

**Auswirkungen:**
- Reduzierte Ladezeit (Strom gedrosselt = längerer Motorbetrieb nötig)
- Verkürzung der Wandler-Lebensdauer bei chronischer Überhitzung
- Im Extremfall: thermische Abschaltung (kein Laden trotz laufendem Motor)

**Diagnose:**
- Gehäusetemperatur messen: >65°C = Derating-Bereich
- Ausgangsstrom überwachen: fällt er nach 15–30 min unter Nennwert?
- Umgebungstemperatur im Einbauraum messen (Motor an, nach 1h)
- Eingangsspannung bei Last prüfen: <12,5V = Zuleitungsproblem

**Behebung:**
1. Montageort ändern: vertikal, Lüfterseite frei, nicht an wärmende Oberflächen
2. Aktive Belüftung: 12V-Lüfter mit Thermostat (>40°C ein, <35°C aus)
3. Eingangskabel kürzen/verdicken (weniger Spannungsabfall = weniger Wärme im Wandler)
4. Alternativ: 2 kleinere Wandler parallel statt 1 großer (bessere Wärmeverteilung)
5. Derating-Kurve des Herstellers beachten und realistisch planen

**AYDI-Bewertung:**
- Confidence: visual_medium (Thermografie zeigt Hotspot, aber kausale Zuordnung schwierig)
- Severity: MITTEL (Leistungsreduktion, keine akute Gefahr)
- Repair urgency: 1–4 Wochen

### 6.7 Fehlerbild: MPPT-Tracking-Oszillation bei Teilverschattung

**Beschreibung:** MPPT-Regler findet keinen stabilen Arbeitspunkt, Ausgangsstrom schwankt rhythmisch (1–5 Sekunden Zyklus), Ertrag deutlich unter dem zu erwartenden Wert trotz ausreichend Sonne.

**Ursache:**
- Teilverschattung des PV-Arrays erzeugt mehrere lokale MPP-Maxima in der P-U-Kennlinie
- MPPT-Algorithmus springt zwischen diesen Maxima hin und her
- Falsche String-Konfiguration (verschattete und unverschattete Module in Serie)
- Bypass-Dioden in Modulen defekt (verschattete Zellen blockieren String-Strom)

**Typische Konstellation:**
- Solaranlage auf Bimini mit partieller Verschattung durch Baum (Lazy Jack, Achterstag)
- Module auf Davits hinter dem Achterspiegel (Schatten vom Radartower, Antennen)
- Teilflexible Module auf Deck (Selbstverschattung durch Winschen, Lüfter, Relingsdrähte)

**Auswirkungen:**
- Ertragsverlust 20–60% gegenüber dem optimalen Arbeitspunkt
- Regler arbeitet ineffizient (ständige Suchbewegung)
- Batterie erhält ungleichmäßigen Ladestrom (stresst BMS bei LiFePO4)

**Diagnose:**
- VictronConnect: MPPT-Verlauf zeigt oszillierenden Strom (Sägezahn-Muster)
- PV-Leerlaufspannung: Bei Verschattung deutlich reduziert vs. erwarteter Wert
- Visuelle Inspektion: Schattenwurf auf Panels zu verschiedenen Tageszeiten dokumentieren
- String-Ströme einzeln messen (bei Parallelschaltung): ungleiche Werte = Verschattung

**Behebung:**
1. Verschattungsquelle beseitigen (wenn möglich)
2. Panel-Konfiguration ändern: verschattete und unverschattete Module in getrennte Strings
3. Jeder String an eigenen MPPT-Regler (Multi-MPPT-System)
4. Modul-Level-Optimizer nachrüsten (z.B. Tigo TS4-A-O oder SolarEdge P-Serie)
5. Panels versetzen (bei flexiblen Panels relativ einfach)

**AYDI-Bewertung:**
- Confidence: visual_high (Verschattungsmuster auf Fotos erkennbar + MPPT-Verlaufsdaten)
- Severity: NIEDRIG bis MITTEL (Ertragsverlust, kein Sicherheitsrisiko)
- Repair urgency: Optimierung bei nächster Gelegenheit

### 6.8 Fehlerbild: Ladegerät-Relais klackert (schaltet ein/aus im Sekundentakt)

**Beschreibung:** Landstrom-Ladegerät oder Inverter-Charger schaltet repetitiv ein und aus, hörbar als Klacken des internen Relais, keine stabile Ladung.

**Ursache:**
- Eingangsspannung instabil (Hafen-Stromversorgung zu schwach)
- Batterie-Spannung im "Grenzbereich" des Ladegeräts (genau an Float/Bulk-Schwelle)
- Defektes Relais (Kontakte oxidiert, Schaltleistung unzureichend)
- EMV-Störung durch andere Verbraucher (Inverter, Frequenzumrichter Klimaanlage)
- Defekte Landstrom-Einspeisung (Steckdose am Steg wackelt)

**Typische Konstellation:**
- Marina mit schwacher Stromversorgung (Spannung sackt bei Belastung ein)
- Älteres Ladegerät (>10 Jahre, Relais-Verschleiß)
- Boot neben Klimaanlagen-betriebenem Nachbarboot (Spannungseinbrüche)
- Landstromkabel mit losem Stecker

**Auswirkungen:**
- Keine effektive Ladung (Batterie wird nicht geladen)
- Relais-Verschleiß wird beschleunigt (Lebensdauer typisch 50.000–100.000 Schaltzyklen)
- Störende Geräusche (besonders nachts)
- EMV-Störungen durch Schaltfunken (Funkempfänger, AIS)

**Diagnose:**
- Netzspannung am Landstromanschluss bei Belastung messen (Sollwert: 220–240V, min. 207V)
- Batteriespannung im Moment des Klackerns beobachten (Grenzwert-Pendeln?)
- Anderes Ladegerät anschließen: gleiches Problem = Netzproblem
- Andere Steckdose am Steg testen

**Behebung:**
1. Netzproblem: Hafenmeister informieren, andere Säule nutzen, stabileres Kabel verwenden
2. Grenzwert-Pendeln: Hysterese am Ladegerät vergrößern (falls einstellbar)
3. Relais defekt: Ladegerät zur Reparatur einschicken
4. EMV: Netzfilter (z.B. Schaffner FN2060-10-06) am Ladegerät-Eingang nachrüsten
5. Landstromstecker: Ersetzen durch hochwertigen Marinco-Stecker mit Festsitz

**AYDI-Bewertung:**
- Confidence: documented (Symptom klar beschreibbar, Messwerte entscheidend)
- Severity: NIEDRIG bis MITTEL (keine akute Gefahr, aber keine Ladung)
- Repair urgency: 1–7 Tage

### 6.9 Fehlerbild: Lichtmaschine erzeugt keinen Ladestrom

**Beschreibung:** Bei laufendem Motor zeigt das Amperemeter 0A Ladung an, Batteriespannung bleibt auf Ruhespannungsniveau (12,2–12,6V statt 13,8–14,4V), Ladekontrolllampe leuchtet nicht oder leuchtet dauerhaft.

**Ursache:**
- Keilriemen gerissen oder durchrutscht (Nr. 1 Ursache)
- Kohlebürsten verschlissen (Feldstrom kann nicht übertragen werden)
- Regler defekt (kein Feldstrom-Ausgang)
- Erreger-Leitung (D+/Lampe) unterbrochen
- Lichtmaschine mechanisch defekt (Lager, Rotor, Stator)

**Typische Konstellation:**
- Keilriemen nach 3–5 Jahren am Lebensende
- Lichtmaschine >2.000 Motorstunden ohne Kohlebürsten-Wechsel
- Nach Motorarbeiten: D+-Kabel nicht wieder angeschlossen
- Hohe Betriebsstunden im tropischen Klima (Hitze + Feuchtigkeit)

**Auswirkungen:**
- Keine Ladung unterwegs — Batterie entleert sich
- Bordnetz abhängig von anderen Quellen (Solar, Generator)
- Bei Nachtfahrt kritisch (Positionslichter, Radar, Navigation)

**Diagnose:**
- Visuell: Keilriemen prüfen (Zustand, Spannung)
- Multimeter an B+ der Lichtmaschine: bei laufendem Motor >13,5V?
- Ladekontrolllampe: Leuchtet bei Zündung an? Geht bei Motor-Start aus?
- D+ an Lichtmaschine: 12V bei Zündung an? (Erregerspannung)
- Feldstrom: Klemme DF messen (externer Regler) — sollte >0V bei Ladung sein

**Behebung:**
1. Keilriemen: Spannung prüfen (10–15mm Durchbiegung bei Daumendruck), ersetzen wenn rissig/glasig
2. Kohlebürsten: min. 5mm Restlänge, sonst ersetzen (Werkstatt oder selbst bei Bosch-Typen)
3. Regler: Ersetzen (interner Regler) oder externen Regler prüfen (Feldstrom-Ausgang?)
4. D+-Kabel: Durchgang prüfen, Steckverbindung reinigen/erneuern
5. Lichtmaschine komplett: Instandsetzung (Anlasser-/Lichtmaschinen-Werkstatt) oder Tausch

**AYDI-Bewertung:**
- Confidence: measured (Spannung/Strom messbar, eindeutig)
- Severity: HOCH (Systemverfügbarkeit gefährdet)
- Repair urgency: sofort (abhängig von alternativen Ladequellen)

### 6.10 Fehlerbild: BMS-Abschaltung bei LiFePO4 — Lichtmaschine im Leerlauf

**Beschreibung:** LiFePO4-Batterie-BMS trennt die Ladung bei Erreichen der Zellspannungs-Obergrenze (3,65V/Zelle = 14,6V System). Lichtmaschine sieht plötzlich offene Last, Spannung schießt hoch (Lastabwurf-Spitze bis 30–50V), elektronische Geräte werden beschädigt.

**Ursache:**
- BMS-Abschaltung ohne vorherige Strom-Reduktion (harte Abschaltung)
- Kein externer Lichtmaschinenregler mit BMS-Kommunikation
- Interner Regler kann nicht schnell genug reagieren (<100ms Lastabwurf)
- Fehlende Spannungsbegrenzung im System

**Typische Konstellation:**
- DIY-Lithium-Umbau mit separatem BMS und Standard-Lichtmaschine
- BMS ohne CAN-Bus-Kommunikation zum Laderegler
- Keine Lastverteilung (Lichtmaschine lädt nur Lithium-Bank, keine Blei-Starterbatterie)
- Hoher Ladestrom (>80A) wird plötzlich auf 0A abgebrochen

**Auswirkungen:**
- Überspannungsspitze zerstört Elektronik (Chartplotter, AIS, Autopilot, VHF)
- Lichtmaschinen-Dioden können durchbrennen
- Regler-Schaden (Überspannungsdurchbruch)
- Im schlimmsten Fall: Kabelisolierung schmilzt, Kurzschluss, Brand

**Diagnose:**
- Bleibt die Ladekontrolllampe nach BMS-Abschaltung dunkel? → Lastabwurf passiert
- Oszilloskop am Batterie-Bus: Spannungsspitze beim BMS-Cutoff messen
- VRM/App: Sudden disconnect events im Verlauf sichtbar
- Elektronik-Schäden nach BMS-Abschaltung = Beweisindiz

**Behebung:**
1. Externen Regler mit CAN-Bus/BMS-Kommunikation nachrüsten (Wakespeed WS500 + BMS-Anbindung)
2. Victron-System: DVCC aktiviert, Cerbo GX kommuniziert mit BMS und drosselt Ladestrom VOR Abschaltung
3. Spannungsbegrenzer nachrüsten (Sterling LPVD oder Balmar ARS-5 mit Overvoltage-Protection)
4. Blei-Starterbatterie als "Spannungspuffer" parallel halten (absorbiert Lastabwurf-Spitze)
5. BMS mit "Pre-Warning" Signal nutzen (z.B. Victron Smart BMS → Allow-to-Charge-Signal)

**AYDI-Bewertung:**
- Confidence: documented (typisches Problem bei DIY-LiFePO4-Umbauten)
- Severity: KRITISCH (Zerstörung teurer Elektronik, Brandgefahr)
- Repair urgency: sofort (vor dem nächsten Motorbetrieb!)

### 6.11 Fehlerbild: Solarregler zeigt "Batterie voll" aber Batterie ist leer

**Beschreibung:** MPPT/PWM-Regler geht in Float-Stufe (grüne LED, App zeigt 100% SOC), aber tatsächlicher Batteriezustand ist 40–60% SOC. Eigner bemerkt erst bei Verbraucher-Einschaltung, dass Batterie fast leer ist.

**Ursache:**
- Regler misst Spannung nur an seinen eigenen Klemmen, nicht an der Batterie
- Spannungsabfall im Kabel zwischen Regler und Batterie (zu dünn, zu lang, korrodierte Verbindung)
- Regler "sieht" 14,4V an seinen Klemmen, aber Batterie hat nur 13,2V
- Regler interpretiert geringen Strom als "Batterie voll" (Tailcurrent-Schwelle erreicht durch Kabelverlust)

**Typische Konstellation:**
- Solarregler im Cockpit-Bereich, Batterie im Bug (5–8m Kabellänge, zu dünner Querschnitt)
- Korrodierte Sicherungshalter oder Batterieschalter in der Leitung
- Kabelquerschnitt nach Nennstrom, nicht nach Ladestrom dimensioniert

**Auswirkungen:**
- Chronische Unterladung der Batterie trotz "funktionierender" Solaranlage
- Frühzeitige Sulfatierung (Batterie wird nie wirklich voll)
- Falsches Vertrauen in den SOC-Wert des Reglers

**Diagnose:**
- Spannung an Regler-Klemmen vs. Spannung an Batterie-Polen gleichzeitig messen
- Differenz >0,3V unter Last = signifikanter Kabelverlust
- Victron: Voltage Sense-Anschluss (separater Messeingang direkt an Batterie)
- Kabelquerschnitt und -länge prüfen, Spannungsabfall berechnen

**Behebung:**
1. Voltage Sense-Leitung vom Regler direkt zur Batterie verlegen (2x0,75mm² reicht)
2. Kabelquerschnitt der Ladeverbindung erhöhen
3. Alle Verbindungen in der Ladeleitung überprüfen und erneuern
4. Sicherungshalter durch hochwertige ersetzen (z.B. Blue Sea MRBF statt billiger Flachsicherung)
5. Ggf. Regler näher an Batterie umsetzen

**AYDI-Bewertung:**
- Confidence: measured (Spannungsdifferenz-Messung eindeutig)
- Severity: MITTEL (keine akute Gefahr, aber schleichende Batterieschädigung)
- Repair urgency: 1–4 Wochen

### 6.12 Fehlerbild: Windgenerator-Regler im Überlastschutz — Dumpload glüht

**Beschreibung:** Windgenerator-Regler schaltet überschüssige Energie auf den Dumpload-Widerstand, dieser wird extrem heiß (>150°C), riecht nach verbranntem Kunststoff, benachbarte Kabel/Materialien gefährdet.

**Ursache:**
- Dumpload-Widerstand unterdimensioniert für die tatsächliche Windleistung
- Batterie voll und Verbraucher zu gering — gesamte Windenergie geht in Dumpload
- Regler-Defekt: Dumpload wird dauerhaft geschaltet (Kurzschluss im Schaltkreis)
- Windgenerator dreht bei Sturm mit voller Leistung über der Batterie-Aufnahmefähigkeit

**Typische Konstellation:**
- Starkwind (>25 kn) bei bereits voller Batterie
- Dumpload im geschlossenen Raum montiert (keine Konvektionskühlung)
- Billiger Windgenerator-Regler ohne Temperaturüberwachung

**Auswirkungen:**
- Brandgefahr durch überhitzten Dumpload-Widerstand
- Schmelzende Kabelisolierung in der Nähe
- Bei Dumpload-Ausfall: Überspannung auf Batterie + gesamtes Bordnetz

**Diagnose:**
- Dumpload-Temperatur prüfen: >80°C = problematisch, >150°C = akute Brandgefahr
- Windgenerator-Leistung bei aktuellem Wind berechnen (Herstellerkurve)
- Dumpload-Widerstand: Nennleistung vs. tatsächliche Windleistung vergleichen
- Regler-Status: Wird Dumpload korrekt getaktet oder dauerhaft geschaltet?

**Behebung:**
1. Sofort: Windgenerator bremsen (Kurzschluss-Bremse aktivieren oder manuell bremsen)
2. Dumpload-Widerstand durch größere Leistungsklasse ersetzen (min. 150% der Max-Windleistung)
3. Dumpload an gut belüfteten Ort umsetzen (Außenmontage ideal, Edelstahl-Gehäuse)
4. Zusätzlichen Verbraucher als "nützlichen Dumpload" nutzen (Warmwasserboiler, Heizpatrone)
5. Regler mit Temperaturüberwachung und Abschaltung nachrüsten

**AYDI-Bewertung:**
- Confidence: visual_high (glühender/verfärbter Dumpload auf Fotos eindeutig erkennbar)
- Severity: KRITISCH (akute Brandgefahr)
- Repair urgency: sofort

(Confidence: documented — Forum-Berichte, Werkstatt-Erfahrung, Hersteller-Servicedaten)

---

## 7. Troubleshooting-Entscheidungsbäume

### 7.1 Entscheidungsbaum: Batterie wird nicht voll geladen

```
START: Batterie erreicht <95% SOC trotz ausreichender Ladezeit
|
+-- Schritt 1: Ladespannung an Batterie-Polen messen
|   +-- <13.8V während Bulk -> [A] Ladequelle liefert zu wenig Spannung
|   |   +-- Landstrom-Ladegerät: Absorptionsspannung prüfen/erhöhen
|   |   +-- Solarregler: Absorptionsspannung prüfen, Panelleistung prüfen
|   |   +-- Lichtmaschine: Externer Regler? Keilriemen? Kabelwiderstände?
|   |
|   +-- 13.8–14.5V -> [B] Spannung korrekt, aber Strom unzureichend
|   |   +-- Schritt 2: Ladestrom messen
|   |   |   +-- Strom <5A bei 200Ah-Bank -> Ladegerät zu klein oder defekt
|   |   |   +-- Strom korrekt, aber Absorption zu kurz -> Timer verlängern
|   |   |   +-- Strom korrekt + Timer korrekt -> Batterie defekt (Sulfatierung)
|   |
|   +-- >14.5V -> [C] Überspannung! Ladeprofil prüfen
|       +-- Temperatursensor angeschlossen? Richtig kalibriert?
|       +-- Falsches Batterie-Profil gewählt (Nass statt AGM)?
|
+-- Schritt 3: Batterie-Zustand prüfen
    +-- Ruhespannung nach 4h: <12.4V bei 100% Ladung -> Batterie defekt
    +-- Kapazitätstest: <80% Nennkapazität -> Batterie am Lebensende
    +-- Zellspannungen (LiFePO4): Delta >100mV -> Zelldrift, Balancing nötig
```

### 7.2 Entscheidungsbaum: Solaranlage liefert zu wenig Ertrag

```
START: Tages-Solarertrag <50% des theoretisch Möglichen
|
+-- Schritt 1: Panel-Leerlaufspannung (Voc) messen (Regler abtrennen!)
|   +-- Voc <80% des Datenblatt-Werts -> Panel-Problem
|   |   +-- Verschattung? -> Standort optimieren
|   |   +-- Verschmutzung? -> Reinigen
|   |   +-- Microcracks? -> IR-Aufnahme oder LED-Taschenlampe bei Dunkelheit
|   |   +-- Bypass-Diode defekt? -> Panel-Anschlussdose öffnen, Dioden prüfen
|   |
|   +-- Voc korrekt -> Regler- oder Kabelproblem
|       +-- Schritt 2: Eingangsspannung am Regler messen
|       |   +-- Voc am Regler deutlich <Voc am Panel -> Kabelverlust!
|       |   |   +-- Kabelquerschnitt prüfen, Steckverbindungen prüfen
|       |   |
|       |   +-- Voc am Regler ca. Voc am Panel -> Regler-Problem
|       |       +-- Schritt 3: Regler-Ausgangsstrom vs. Maximalstrom
|       |       |   +-- Ausgangsstrom = Maximalstrom -> Regler zu klein!
|       |       |   +-- Ausgangsstrom < Maximum -> MPPT-Tracking prüfen
|       |       |       +-- Firmware aktuell?
|       |       |       +-- VictronConnect: MPPT-History auf Anomalien prüfen
|       |
|       +-- Schritt 4: Batterie-Zustand -> Solarregler geht zu früh in Float?
|           +-- Siehe Entscheidungsbaum 7.1
```

### 7.3 Entscheidungsbaum: Ladegerät-Ausfall bei Landstrom

```
START: Ladegerät reagiert nicht bei Landstrom-Anschluss
|
+-- Schritt 1: AC-Spannung am Ladegerät-Eingang messen
|   +-- 0V -> Kein Strom am Ladegerät
|   |   +-- Steg-Sicherung geprüft? -> Rücksetzen/Tauschen
|   |   +-- FI/RCD an Bord geprüft? -> Rücksetzen
|   |   +-- Landstromkabel-Stecker korrodiert? -> Reinigen/Tauschen
|   |   +-- Kabel-Durchgang prüfen (Multimeter)
|   |
|   +-- 180–250V -> Spannung korrekt, Ladegerät defekt
|   |   +-- Interne Sicherung? -> Öffnen und prüfen (Garantieverlust!)
|   |   +-- Victron: Bluetooth-Verbindung? -> Fehlermeldung in App prüfen
|   |   +-- LED-Status? -> Hersteller-Fehlercode-Tabelle konsultieren
|   |   +-- Bei Switch-Mode: MOV/Varistor durch Überspannung zerstört?
|   |
|   +-- <180V -> Unterspannung!
|       +-- Steg-Verteilung überlastet (Sommer, alle Boote an Klima)
|       +-- Landstromkabel zu lang und/oder zu dünn
|       +-- Generator: Frequenz und Spannung prüfen
|
+-- Schritt 2: DC-Ausgang prüfen
    +-- Spannung am DC-Ausgang: >0V aber <11V -> Batterie nicht erkannt
    |   +-- Batterie-Sicherung?, Verpolungsschutz?, Batterie komplett leer (<8V)?
    +-- Spannung = 0V DC -> Ladegerät intern defekt -> Einschicken/Ersetzen
```

### 7.4 Entscheidungsbaum: LiFePO4-Ladeprobleme

```
START: LiFePO4-Batterie wird nicht korrekt geladen
|
+-- Schritt 1: BMS-Status prüfen (App oder LED)
|   +-- BMS sperrt Ladung -> Schutzfunktion aktiv
|   |   +-- Überladungsschutz (Cell OVP): Ladespannung zu hoch
|   |   |   +-- Ladegerät-Profil auf LiFePO4 einstellen, Absorption <=14.2V
|   |   +-- Niedrigtemperatur-Schutz: T <0°C / <5°C
|   |   |   +-- Batterie aufwärmen (Heizmatte, Motorwärme)
|   |   +-- Überström-Schutz: Ladestrom >BMS-Limit
|   |   |   +-- Ladestrom begrenzen (Ladegerät-Einstellung)
|   |   +-- Kommunikationsfehler: BMS-Signal an Ladegerät unterbrochen
|   |       +-- CAN-Bus-/Signal-Kabel prüfen
|   |
|   +-- BMS erlaubt Ladung -> Ladegerät-Problem
|       +-- Ladegerät hat KEIN LiFePO4-Profil? -> Zwingend tauschen!
|       +-- Absorption zu niedrig (<13.8V)? -> Batterie wird nicht voll
|       +-- Float zu hoch (>13.8V)? -> Dauerlast auf BMS-Balancer
|       +-- Egalisierung/Desulfatierung aktiv? -> SOFORT deaktivieren!
|
+-- Schritt 2: Alle Ladequellen prüfen
    +-- Lichtmaschine: Externer Regler mit Li-Profil? BMS-Abschalt-Signal?
    +-- Solarregler: LiFePO4-Profil? Absorption <=14.4V?
    +-- Landstrom-Ladegerät: LiFePO4-Profil? Float abschalten oder <=13.6V?
```

### 7.5 Entscheidungsbaum: Parallele Ladequellen-Konflikte

```
START: Mehrere Ladequellen, Batterie verhält sich unvorhersehbar
|
+-- Schritt 1: Symptom identifizieren
|   +-- Batterie wird überladen (Kochen, BMS-Abschaltung)
|   |   +-- Addierter Strom aller Quellen prüfen
|   |   |   +-- Summe Ladestrom > C/3 (Blei) oder > BMS-Limit (Li)?
|   |   +-- Absorptionsspannung aller Quellen identisch?
|   |   |   +-- Abweichungen >0.3V -> Kalibrieren oder Sense-Kabel verlegen
|   |   +-- Temperatursensoren: Jede Quelle eigenen Sensor?
|   |       +-- Mehrere Sensoren können sich widersprechen -> nur EINEN verwenden!
|   |
|   +-- Batterie wird nicht voll (SOC bleibt <90%)
|   |   +-- Siehe Fehlerbild 12 (Parallelladung, Float-Verwirrung)
|   |
|   +-- Ladequellen kämpfen (Strom pendelt, Spannung instabil)
|       +-- DVCC aktivieren (Victron GX-System)
|       +-- Absorptionsspannungen staffeln: Quelle 1=14.4V, 2=14.3V, 3=14.2V
|       +-- DC-DC-Wandler zwischen Quellen und Batterie als Entkopplung
|
+-- Schritt 2: Systemdesign evaluieren
    +-- Victron-System? -> DVCC + Cerbo GX = koordinierte Ladung
    +-- Mischsystem? -> Spannungsstaffelung implementieren
    +-- Lithium? -> ALLE Quellen müssen vom BMS abschaltbar sein!
```

### 7.6 Entscheidungsbaum: DC-DC-Wandler Fehlerdiagnose

```
START: DC-DC-Wandler (B2B-Charger) liefert keinen oder zu wenig Strom
|
+-- Schritt 1: LED-Status / App-Status prüfen
|   +-- Keine LED an -> Versorgung prüfen
|   |   +-- Eingangsspannung vorhanden? (Multimeter an Eingang)
|   |   |   +-- Nein -> Vorsicherung, Kabel, Zündungssignal prüfen
|   |   |   +-- Ja -> Wandler defekt (interne Sicherung oder Hardware)
|   |
|   +-- LED an, aber kein Ausgangsstrom -> Weiter Schritt 2
|   |
|   +-- LED blinkt / Fehlercode -> Herstellerdokumentation konsultieren
|       +-- Victron Orion: BT-App zeigt Fehlercode
|       +-- Sterling B2B: LED-Blinkcode (Handbuch)
|
+-- Schritt 2: Zündungssignal / Motorlaufsignal prüfen
|   +-- Viele B2B-Charger starten nur bei laufendem Motor (D+ Signal)
|   |   +-- D+ Spannung prüfen: >12V bei Motor an?
|   |   +-- Victron Orion-Tr Smart: Motorerkennung über Eingangsspannung (>13.2V)
|   |   +-- Schwelle zu hoch? -> Smart-Alternator liefert nur 12.8V!
|   |       +-- Lösung: Schwelle in App anpassen oder externes D+-Signal
|
+-- Schritt 3: Eingangsspannung unter Last prüfen
|   +-- Eingangsspannung sackt unter 12.0V bei Last -> Zuleitungsproblem
|   |   +-- Kabelquerschnitt prüfen (min. 10mm² für 30A, min. 16mm² für 50A)
|   |   +-- Steckverbindungen, Sicherungshalter prüfen
|   |   +-- Kabellänge: max. 3m bei 30A mit 10mm²
|   |
|   +-- Eingangsspannung stabil >12.5V -> Weiter Schritt 4
|
+-- Schritt 4: Ausgangsspannung und Batterie-Zustand
|   +-- Ausgangsbatterie bereits voll? (>14.2V) -> Wandler in Float = normal!
|   +-- BMS hat Ladung gesperrt? -> Allow-to-Charge Signal prüfen
|   +-- Ausgangsspannung vorhanden aber Strom <5A bei leerer Batterie:
|       +-- Temperatur-Derating? Gehäuse >60°C? -> Belüftung verbessern
|       +-- Strom-Begrenzung durch Konfiguration? -> App-Einstellungen prüfen
|
+-- Schritt 5: Victron Orion-Tr Smart spezifisch
    +-- Motor aus/erkannt? -> "Vehicle" vs "Charger" Modus prüfen
    +-- Smart Alternator Modus aktiv? -> Startspannung anpassen
    +-- Bluetooth-Verbindung: Firmware aktuell?
    +-- Lock-Out nach Übertemperatur: 30min Abkühlung abwarten
```

### 7.7 Entscheidungsbaum: LiFePO4-BMS-Abschaltung Ursachenanalyse

```
START: BMS hat Batterie getrennt (kein Laden oder kein Entladen möglich)
|
+-- Schritt 1: Art der Abschaltung identifizieren
|   +-- Ladung gesperrt (Entladung funktioniert noch)
|   |   +-- Ursache 1: Zellspannung zu hoch (>3.65V an einer Zelle)
|   |   |   +-- Balancing-Problem? -> Zellspannungen einzeln prüfen
|   |   |   +-- Ladespannung zu hoch eingestellt? -> Absorption auf 14.2V senken
|   |   |   +-- Temperatursensor defekt? -> BMS-Temperaturanzeige prüfen
|   |   |
|   |   +-- Ursache 2: Temperatur zu niedrig (<5°C)
|   |   |   +-- Normal im Winter! -> Batterie heizen (Heizpad) oder warten
|   |   |   +-- Sensor defekt? -> Temperatur manuell prüfen
|   |   |
|   |   +-- Ursache 3: Ladestrom zu hoch (>BMS-Limit)
|   |       +-- Alle Ladequellen gleichzeitig aktiv? -> Koordination (DVCC)
|   |       +-- BMS-Limit für Ladestrom prüfen (typisch: 100–200A)
|   |
|   +-- Entladung gesperrt (Ladung funktioniert noch)
|   |   +-- Ursache 1: Zellspannung zu niedrig (<2.8V an einer Zelle)
|   |   |   +-- Bank ist leer! -> Sofort laden
|   |   |   +-- Eine Zelle deutlich tiefer als andere? -> Zelldrift!
|   |   |       +-- BMS-Balancing aktiv? -> Kann Wochen dauern
|   |   |       +-- Zelle defekt? -> Professionelle Prüfung (Innenwiderstand)
|   |   |
|   |   +-- Ursache 2: Überstrom (>BMS-Entladelimit)
|   |   |   +-- Anlasser/Bugstrahler über Lithium-Bank? -> Separate Starterbatterie!
|   |   |   +-- Inverter-Einschaltstrom? -> Soft-Start aktivieren
|   |   |
|   |   +-- Ursache 3: Temperatur zu hoch (>55°C)
|   |       +-- Kurzschluss im System? -> Sofort alle Last trennen, Kabel prüfen!
|   |       +-- Umgebungstemperatur? -> Batterie in kühleren Raum versetzen
|   |
|   +-- Komplett-Abschaltung (weder Laden noch Entladen)
|       +-- BMS-Kommunikation ausgefallen? -> Reset versuchen (Hersteller-Anweisung)
|       +-- Kritischer Fehler: Professionellen Service kontaktieren
|       +-- Victron Smart BMS: Bluetooth/App Fehlercode auslesen
|
+-- Schritt 2: Nach BMS-Reset
    +-- Ladung freigegeben? -> System langsam (C/10) anladen und beobachten
    +-- Problem wiederholt sich? -> Logging aktivieren (VRM, Cerbo GX)
    +-- Zelldrift >100mV? -> Balancing über mehrere Lade-/Entladezyklen
    +-- Zelldrift >300mV? -> Zelle defekt, professioneller Tausch nötig
```

### 7.8 Entscheidungsbaum: Galvanische Korrosion am Landstrom

```
START: Verdacht auf galvanische Korrosion (Zinkanoden schnell aufgezehrt, Metallfraß)
|
+-- Schritt 1: Ist das Problem Landstrom-bezogen?
|   +-- Test: Landstrom für 2 Wochen trennen
|   |   +-- Korrosion stoppt -> Landstrom-bezogen! Weiter Schritt 2.
|   |   +-- Korrosion weiter -> Eigenes Korrosionsproblem (Bonding prüfen)
|
+-- Schritt 2: Leckstrom messen
|   +-- DC-Milliampere-Zange am Landstromkabel (PE-Leiter)
|   |   +-- >30mA DC -> Signifikanter galvanischer Strom!
|   |   +-- <10mA DC -> Minimal, aber bei Dauerbetrieb trotzdem relevant
|   |
|   +-- AC-Messung am PE-Leiter
|       +-- >100mA AC -> Hafen-Erdungsproblem oder Nachbarboot-Defekt
|       +-- <50mA AC -> Normal
|
+-- Schritt 3: Isolation vorhanden?
|   +-- Galvanic Isolator installiert?
|   |   +-- Ja -> Funktionsprüfung (Durchgangsmessung: >1.4V Schwelle)
|   |   |   +-- Galvanic Isolator defekt? -> Ersetzen (Victron GI, Sterling ProGI)
|   |   +-- Nein -> Galvanic Isolator installieren (Mindestschutz)
|   |
|   +-- Trenntransformator installiert?
|       +-- Ja -> Überprüfen (Isolationswiderstand messen)
|       +-- Nein -> Beste Lösung: Trenntrafo nachrüsten (Victron 3600W)
|
+-- Schritt 4: Ursache bei Nachbarbooten?
    +-- Potentialmessung Silber/Silberchlorid-Referenzelektrode
    |   +-- Eigenes Boot: -850mV bis -1050mV (Stahl) oder -550mV bis -650mV (GFK-Alu) = OK
    |   +-- Deutlich negativer = wird geschützt (eigene Anoden opfern sich)
    |   +-- Deutlich positiver = wird angegriffen!
    |
    +-- Nachbar-Boot mit defekter Elektrik identifiziert?
        +-- Hafenmeister informieren
        +-- Eigene Isolation sicherstellen (Trenntrafo = 100% Schutz)
```

---

## 8. FAQ — Häufige Fragen

### 8.1 Grundlagen Ladegeräte

**F1: Warum darf ich kein Auto-Ladegerät auf meinem Boot verwenden?**
Ein Auto-Ladegerät ist in der Regel nicht marinisiert: (1) Keine galvanische Trennung — galvanische Korrosion am Unterwasserschiff. (2) Kein IP-Schutz gegen Feuchtigkeit und Salz. (3) Keine CE-Marine-Zulassung. (4) Oft nur einstufige Ladung (keine Absorption/Float). Für gelegentliche Winterlager-Erhaltung eines Binnenbootes mag es funktionieren, für den Dauereinsatz auf einer Seeyacht ist es ungeeignet und potenziell gefährlich.

**F2: Was bedeutet IUoU und warum ist es besser als einfache Konstantspannung?**
IUoU steht für die drei Phasen: I (Konstantstrom/Bulk), U (Konstantspannung/Absorption), o (Pause/reduziert), U (Float/Erhaltung). Im Gegensatz zu einfacher Konstantspannung sorgt IUoU dafür, dass die Batterie schnell und schonend vollgeladen wird: Bulk liefert Maximalstrom, Absorption füllt die letzten 20% schonend, und Float hält den Ladezustand ohne Überladung. Einfache Konstantspannung kann entweder unterladen (zu niedrig) oder überladen (zu hoch).

**F3: Was ist der Unterschied zwischen einem Batterielader und einem Inverter/Charger (Kombigerät)?**
Ein reines Ladegerät wandelt nur AC (Landstrom) in DC (Batterieladung) um. Ein Inverter/Charger (z.B. Victron MultiPlus, Mastervolt Mass Combi Ultra) kann beides: Bei Landstrom fungiert er als Ladegerät, bei Batteriebetrieb als Wechselrichter (DC→AC). Vorteile des Kombigeräts: Platzersparnis, automatische Umschaltung, oft eingebauter Transferschalter. Nachteile: Teurer, bei Defekt fallen beide Funktionen aus, Reparatur komplexer.

**F4: Mein Ladegerät zeigt "Float" nach nur 2 Stunden an — ist die Batterie wirklich voll?**
Nicht unbedingt. Mögliche Ursachen: (1) Ladegerät zu klein für die Bankkapazität — Strom sinkt früh unter Tailcurrent-Schwelle. (2) Kabelverluste täuschen höhere Batteriespannung vor (Regler misst an seinen Klemmen, nicht an der Batterie). (3) Batterie sulfatiert — nimmt keinen Strom mehr an. Prüfung: Ruhespannung 4h nach Ladung messen. Unter 12,7V = nicht voll geladen.

**F5: Wie groß sollte mein Landstrom-Ladegerät sein (Amperezahl)?**
Faustregel: 15–25% der Batteriebankkapazität (C10). Beispiel: 200Ah-Bank = 30–50A Ladegerät. Größer schadet modernen Batterien nicht (Ladegerät regelt), aber belastet den Landstromanschluss (16A Steg-Steckdose = max. 3.680W = theoretisch max. 250A Ladestrom, aber Inverter-Eigenverbrauch und andere AC-Verbraucher berücksichtigen). Bei LiFePO4 kann man bis 50% C10 gehen (100A bei 200Ah).

### 8.2 Solaranlagen

**F6: MPPT oder PWM — wann lohnt sich der teurere MPPT-Regler?**
MPPT lohnt sich ab ca. 200Wp (Wattpeak) Panelleistung oder bei Panel-Spannungen >18V (Nominalspannung). Bei einem einzelnen 100Wp-Panel mit 18V Nennspannung auf einem 12V-System ist der Vorteil marginal (10–15%). Bei 2+ Panels in Serie (36V+) ist MPPT zwingend, weil PWM die hohe Spannung einfach wegwirft. Faustregel: Bei Anlagen >150 EUR Panelkosten amortisiert sich der MPPT-Mehrpreis (50–150 EUR) in <1 Saison.

**F7: Kann ich verschiedene Solarpanels an einen MPPT-Regler anschließen?**
Nur wenn sie in Parallelschaltung denselben Vmp (Spannung am MPP) haben. Unterschiedliche Module in Serie zu schalten ist problematisch: der schwächste begrenzt den Strom des Strings. Besser: getrennte Strings an getrennte MPPT-Regler. Victron SmartSolar-Regler sind klein und günstig genug, dass 2-3 separate Regler wirtschaftlich sind.

**F8: Wie viel Solar brauche ich auf einer Fahrtenyacht?**
Dimensionierungsformel: Tagesverbrauch (Ah) x 1,3 (Verluste) / Sonnenstunden (PSH). Beispiel Mittelmeer: 120Ah Tagesverbrauch x 1,3 / 5h PSH = 31,2A Peak → ca. 500Wp. Nordeuropa mit nur 3h PSH: gleiche Rechnung ergibt 830Wp. Praxis: 400–600Wp ist Standard für eine 12m-Fahrtenyacht im Mittelmeer, 800–1200Wp für Blauwasser.

**F9: Meine Solarpanels werden sehr heiß — verliere ich dadurch Leistung?**
Ja, erheblich. Silizium-Module verlieren ca. 0,4–0,5% Leistung pro Grad über 25°C (STC). Ein Panel auf dem Deck bei 60°C Oberflächentemperatur verliert ca. 17% Leistung. Gegenmaßnahmen: (1) Hinterlüftung (Abstand zum Deck min. 5cm). (2) Panels auf Bimini/Arch statt flach auf Deck. (3) MPPT-Regler kompensiert teilweise (arbeitet bei niedrigerer Spannung effizienter). Flexible Panels ohne Hinterlüftung sind am stärksten betroffen (bis zu 25% Verlust).

**F10: Parallele MPPT-Regler oder ein großer — was ist besser?**
Mehrere kleine Regler sind in den meisten Fällen besser: (1) Verschattung eines Panels beeinflusst nicht die anderen. (2) Redundanz bei Ausfall eines Reglers. (3) Flexiblere Montage möglich. (4) Getrennte MPPT-Tracker für unterschiedliche Ausrichtungen. Nachteil: Mehr Kabel, mehr Platz, etwas höhere Gesamtkosten. Victron-Ökosystem: Alle Regler synchronisieren sich per VE.Smart-Networking (Bluetooth) für koordiniertes Laden.

### 8.3 Lichtmaschine und Alternator-Regler

**F11: Warum liefert meine 120A-Lichtmaschine nur 40A Ladestrom?**
Mehrere Gründe: (1) Der interne Regler begrenzt den Feldstrom, um die Lichtmaschine thermisch zu schützen (besonders bei niedrigen Drehzahlen). (2) Die 120A-Angabe gilt nur bei hoher Drehzahl (6.000 U/min Generatordrehzahl), bei Leerlauf-Motordrehzahl (~800 U/min) sind es nur 30–50%. (3) Eine warme Lichtmaschine liefert weniger als eine kalte. Lösung: Externer Regler (Balmar MC-614, Wakespeed WS500) kann den Feldstrom optimal steuern und liefert 70–90% der Nennleistung.

**F12: Kann ein externer Lichtmaschinenregler meine Lichtmaschine beschädigen?**
Ja, wenn falsch konfiguriert. Ein externer Regler kann die Lichtmaschine deutlich härter belasten als der interne Regler es zulässt. Schutzmaßnahmen: (1) Temperatursensor an der Lichtmaschine (bei Wakespeed WS500 und Balmar MC-614 Standard). (2) Korrekte Konfiguration der Maximalstrom-Begrenzung im Regler. (3) Alternator Belt Manager (Balmar): reduziert Strom bei niedrigen Drehzahlen. (4) Bei Dauerhochleistung: Marine-Lichtmaschine mit besserer Kühlung nachrüsten (Balmar XT, Electromaax).

**F13: Was bringt ein DC-DC-Wandler (B2B-Charger) vs. direkte Ladung über die Lichtmaschine?**
Ein DC-DC-Wandler (Sterling B2B, Victron Orion-Tr Smart) sitzt zwischen Starterbatterie und Servicebatterie und bietet: (1) Galvanische Trennung bei isolierten Modellen. (2) Optimales Ladeprofil unabhängig von der Lichtmaschinenspannung. (3) Spannungsanhebung (12V Starter → 14,4V Laden auch bei Smart-Alternator). (4) Strombegrenzung (schützt Kabel und Lichtmaschine). (5) LiFePO4-kompatibles Laden selbst mit alter Lichtmaschine. Nachteil: Wirkungsgradverlust 5–10%, Wärmeentwicklung, zusätzliche Kosten.

**F14: Mein Euro-6-Diesel hat einen Smart-Alternator — was bedeutet das für die Bordladung?**
Smart-Alternators (bei Marine-Motoren: Volvo D2-75, Yanmar 4JH-CR) regeln die Lichtmaschinenspannung variabel (manchmal nur 12,4V!) zur Kraftstoffeinsparung. Folge: Batterie wird kaum geladen. Lösungen: (1) DC-DC-Wandler (hebt die Spannung auf korrektes Ladeniveau). (2) Victron Orion-Tr Smart (erkennt Smart-Alternator-Modus). (3) Separater externer Regler-Eingang (bei manchen Motoren möglich). (4) Zusätzliche, konventionell geregelte Lichtmaschine nachrüsten.

### 8.4 LiFePO4 / Lithium-Systeme

**F15: Muss ich bei LiFePO4-Batterien alle Ladegeräte austauschen?**
Nicht unbedingt austauschen, aber ALLE umkonfigurieren: (1) Ladeschlussspannung exakt auf BMS-Herstellervorgabe (typisch 14,2–14,6V für 12V-System). (2) Float-Spannung auf 13,4–13,6V oder Float deaktivieren. (3) Temperaturkompensation AUS (LiFePO4 braucht keine). (4) Egalisierung AUS (zerstört LiFePO4-Zellen!). Geräte ohne einstellbare LiFePO4-Profile müssen ersetzt werden (z.B. alte Ladegeräte mit fest eingestellter 14,8V Absorption für Nassbatterien).

**F16: Was passiert, wenn das BMS die Ladung trennt und die Lichtmaschine noch läuft?**
Ohne Schutzmaßnahmen: Lastabwurf-Spannungsspitze (bis 50V bei großen Lichtmaschinen), die Elektronik zerstören kann. Schutz: (1) Wakespeed WS500 mit CAN-Bus-Anbindung an BMS (drosselt VOR Abschaltung). (2) Victron DVCC über Cerbo GX (koordiniert alle Ladequellen). (3) Blei-Starterbatterie als Spannungspuffer parallel halten. (4) Sterling LPVD als Überspannungsschutz. NIEMALS eine Lichtmaschine nur an eine LiFePO4-Bank ohne BMS-Kommunikation anschließen.

**F17: Kann ich Blei-Starterbatterie und LiFePO4-Servicebank mit demselben Ladegerät laden?**
Nein — die Ladekennlinien sind fundamental unterschiedlich. Lösung: (1) Separates Ladegerät für jede Bank. (2) Ladegerät mit zwei Ausgängen und getrennten Profilen (z.B. Victron Blue Smart IP22 3-Output). (3) DC-DC-Wandler zwischen den Banken (Victron Orion-Tr Smart: LiFePO4-Bank primär, Starterbatterie sekundär). (4) Mastervolt ChargeMaster Plus mit konfigurierbarem Zweitausgang.

**F18: Wie lade ich LiFePO4-Batterien bei Minustemperaturen?**
LiFePO4 darf unter 0°C NICHT geladen werden (Lithium-Plating → irreversibler Kapazitätsverlust). Lösungen: (1) BMS mit integrierter Heizung (z.B. Victron Smart Battery mit Bluetooth-Heizsteuerung). (2) Externer Heizpad auf der Batterie mit Thermostat. (3) Alle Ladequellen müssen vom BMS abschaltbar sein (BMS deaktiviert Ladung unter 5°C). (4) Victron DVCC mit Temperatur-Sensor: Alle Ladegeräte werden koordiniert abgeschaltet.

### 8.5 Systemauslegung

**F19: Wie koordiniere ich mehrere Ladequellen (Landstrom + Solar + Lichtmaschine)?**
Moderne Systeme verwenden DVCC (Distributed Voltage and Current Control) in Victron-Systemen oder MasterBus bei Mastervolt. Ohne intelligente Koordination gilt die Regel der "Spannungsstaffelung": Jede Quelle hat leicht unterschiedliche Absorptionsspannung. Die Quelle mit der höchsten Spannung dominiert. Typisch: Landstrom 14,4V, Lichtmaschine 14,2V, Solar 14,0V. So reduzieren sich die anderen automatisch, wenn die dominante Quelle aktiv ist. Bei LiFePO4 ist diese passive Methode unzureichend — DVCC oder äquivalent zwingend nötig.

**F20: Was ist der Unterschied zwischen "isoliertem" und "nicht-isoliertem" DC-DC-Wandler?**
Isolierter DC-DC-Wandler: Galvanische Trennung zwischen Ein- und Ausgang. Zwingend bei: verschiedenen Erdungssystemen, Verbindung von 12V und 24V, Verhinderung von galvanischer Korrosion. Nicht-isoliert: Ein- und Ausgang teilen sich die Masse. Günstiger, effizienter (~2% weniger Verlust), einfacher. Ausreichend wenn beide Banken im selben Bordnetz (gleiche Masse) liegen und keine Isolationsanforderung besteht.

**F21: Reicht eine 16A-Steckdose am Steg für mein 50A-Ladegerät?**
Rechnung: 16A × 230V = 3.680W. Ein 50A/12V-Ladegerät braucht max. 50A × 14,4V / 0,90 (Wirkungsgrad) = 800W. Also reicht es für das Ladegerät allein problemlos. ABER: Wenn gleichzeitig Warmwasserboiler (1.500W), Klimaanlage (1.200W) oder Waschmaschine laufen, übersteigt die Gesamtlast die 16A Stegversorgung. Lösung: PowerAssist-Funktion (Victron MultiPlus) — ergänzt Landstrom aus der Batterie bei Spitzenlast.

**F22: Mein Hafen hat nur 10A-Absicherung — was soll ich tun?**
10A × 230V = 2.300W Gesamtbudget. Strategien: (1) Ladegerät auf niedrigeren Strom begrenzen (Victron: per App einstellbar, z.B. auf 15A statt 30A). (2) Klimaanlage/Boiler nicht gleichzeitig mit Ladegerät betreiben (Lastmanagement). (3) Inverter/Charger mit PowerAssist: Lädt mit reduziertem Strom und ergänzt bei Bedarf aus der Batterie. (4) Über Nacht laden, wenn wenig andere Verbraucher aktiv.

### 8.6 Wartung und Troubleshooting

**F23: Wie oft muss ich ein Landstrom-Ladegerät warten?**
Professionelle Wartung alle 3–5 Jahre. Eigene Kontrolle jährlich: (1) Lüfter reinigen (Druckluft). (2) Korrosion an Klemmen prüfen. (3) Ladespannung mit Multimeter verifizieren (Soll vs. Ist). (4) Temperatursensor-Kalibrierung prüfen (Frostspray auf Sensor → Spannung muss steigen). (5) LED-Status und Fehlerspeicher prüfen. (6) Sicherungen und Kabelverbindungen auf Festsitz prüfen.

**F24: Mein MPPT-Regler zeigt morgens kurz Ladung, dann nichts mehr — was ist das?**
Typisches Symptom für: (1) Panel-Verschattung ab einem bestimmten Sonnenstand (Baum, Lazy Jack, Backstag). (2) Defekte Bypass-Diode (einzelne Zelle wird zum Widerstand, String-Strom bricht ein). (3) Regler im Temperatur-Derating (morgendliche Kälte ist OK, dann wird Maschinenraum heiß). Diagnose: PV-Leerlaufspannung zu verschiedenen Tageszeiten messen + Schattenanalyse.

**F25: Kann ich mein Ladegerät per Solaranlage "ersetzen" und auf Landstrom verzichten?**
Für Dauerlieger in Nordeuropa: Nein — Wintermonate liefern zu wenig Solarertrag (typisch 0,5–1,5h PSH im Dezember/Januar). Ein Erhaltungsladegerät (5–10A) über Landstrom ist für den Winter zwingend. Für Fahrtenyachten im Mittelmeer/Tropen: Eine gut dimensionierte Solaranlage (>500Wp für 12m-Yacht) kann den Landstrom-Bedarf auf gelegentliche Hafentage reduzieren. Komplett Landstrom-frei: Nur mit Solar + Wind + Generator-Kombination.

### 8.7 Spezialthemen und Praxis-Tipps

**F26: Wie schütze ich mein Ladesystem vor Blitzschlag?**
Vollständiger Blitzschutz ist auf Yachten nahezu unmöglich, aber Schadensbegrenzung ist machbar: (1) Alle Ladegeräte und Regler über Varistoren/MOVs (Metal Oxide Varistors) absichern — z.B. Victron Smart BatteryProtect oder Dehn Schutzgeräte am Landstromeingang. (2) PV-String-Sicherungen mit Überspannungsableiter (Type 2 SPD). (3) Separate Erdung des Mast-Blitzableiters direkt zum Kiel, nicht über das Bordnetz! (4) Abstand zwischen Blitzableiter-Kabel und Signal-/Ladekabeln min. 30cm. (5) Realistisch: Bei direktem Blitzeinschlag ist fast alles zerstört — Versicherung ist der beste Schutz.

**F27: Wie lagere ich mein Boot über den Winter — was muss das Ladesystem tun?**
Optimal: (1) Erhaltungsladung über Landstrom (5–10A Ladegerät im Float-Modus). (2) Bei LiFePO4: SOC auf 50–60% bringen und BMS-Überwachung aktiviert lassen (Selbstentladung minimal, aber BMS braucht Strom). (3) Solar-Panels angeschlossen lassen (Erhaltungsladung bei Sonnentagen). (4) Alle nicht benötigten Verbraucher abschalten (Hauptschalter AUS, Ladegerät bleibt). (5) Batterie-Trennschalter: EIN lassen (damit Ladegerät laden kann!). (6) Frostschutz: Blei-Batterien unter 50% SOC können bei -10°C EINFRIEREN (Elektrolyt wird zu Wasser).

**F28: Was ist der Unterschied zwischen "3-stufig", "5-stufig" und "8-stufig" bei Ladegeräten?**
Marketing-Bezeichnungen mit wenig Standardisierung. Typisch: 3-stufig = Bulk/Absorption/Float (Standard IUoU). 5-stufig = + Soft-Start + Storage (Lagermodus). 7-stufig (CTEK) = + Desulfatierung + Prüfung + Recondition. 8-stufig (Victron) = + Analyse + Sanftanlauf + Absorption + Recondition + Float + Storage + Refresh + Tiefentladungsrettung. Die Grundfunktion (Bulk/Absorption/Float) ist bei allen identisch — die Zusatzstufen sind komfortabel, aber nicht zwingend für gute Batterieladung.

**F29: Mein Victron-System zeigt "Low Voltage Alarm" trotz angeblich voller Batterie — was tun?**
Häufige Ursachen: (1) BMV/SmartShunt SOC-Kalibrierung falsch (Synchronisation bei Volladung nicht geschehen). Lösung: Manuell auf 100% synchronisieren wenn sicher voll. (2) Hoher Momentan-Verbrauch (Inverter-Start, Ankerwinde) zieht Spannung kurzzeitig unter Schwelle. Lösung: Alarm-Schwelle senken (z.B. 11,5V statt 11,8V) oder Verzögerung einstellen. (3) Batterie tatsächlich am Lebensende — Innenwiderstand zu hoch, Spannung sackt bei Last ein. (4) Shunt misst falsch (Sense-Kabel korrodiert, falscher Shunt-Wert konfiguriert).

**F30: Wie verbinde ich ein Victron-System mit einem existierenden Mastervolt-Gerät?**
Victron und Mastervolt kommunizieren NICHT nativ miteinander (verschiedene Bus-Systeme: VE.Direct/VE.Can vs. MasterBus). Lösungen: (1) Passive Koexistenz über Spannungsstaffelung (verschiedene Absorptionsspannungen). (2) Mastervolt-Gerät als "dummen Charger" betreiben (keine Bus-Anbindung, arbeitet eigenständig). (3) Integration über Node-RED auf Venus OS (GX-Gerät mit Modbus-Abfrage des Mastervolt). (4) Langfristig: System auf einen Hersteller konsolidieren (empfohlen bei nächstem Gerätetausch).

**F31: Flexible oder starre Solarpanels — welche sind besser für die Ladeleistung?**
Aus reiner Ladeleistungs-Perspektive: Starre Panels (Glas-Glas oder Glas-Folie) sind überlegen: (1) 5–10% mehr Ertrag durch bessere Hinterlüftung (Aufständerung möglich). (2) 30% längere Lebensdauer (20+ Jahre vs. 5–8 Jahre bei flexiblen). (3) Bessere Temperatur-Performance (stehen frei, werden weniger heiß). (4) Geringere Degradation (<0,5%/Jahr vs. 2–3%/Jahr bei billigen flexiblen). Flexible Panels lohnen sich NUR wenn: Gewicht kritisch ist (Regatta), kein Platz für Aufständerung, oder Deck-Integration ästhetisch gewünscht. Tipp: Semi-flexible (5mm Biegung) auf Aluminium-Rahmen sind ein guter Kompromiss.

**F32: Was kostet ein komplettes Ladesystem-Upgrade für verschiedene Bootsgrößen?**
Grobe Richtwerte (Material + Einbau durch Fachbetrieb, Stand 2025):

| Bootsgröße | Scope | Material | Arbeit | Gesamt |
|------------|-------|----------|--------|--------|
| 8–10m Segelboot | Solar 200Wp + MPPT + Verkabelung | 600–900 EUR | 400–800 EUR | 1.000–1.700 EUR |
| 10–13m Segelboot | Solar 400Wp + MPPT + Landstrom 30A + ext. LiMa-Regler | 1.500–2.500 EUR | 1.000–2.000 EUR | 2.500–4.500 EUR |
| 10–13m + LiFePO4-Umbau | Wie oben + 200Ah LiFePO4 + BMS + DC-DC + Monitor | 4.000–6.000 EUR | 1.500–3.000 EUR | 5.500–9.000 EUR |
| 13–16m Blauwasser | Komplettsystem LiFePO4 400Ah + Solar 800Wp + WS500 + DVCC | 8.000–12.000 EUR | 3.000–5.000 EUR | 11.000–17.000 EUR |
| 16–20m Motor | 24V-System, 800Ah LiFePO4, Solar 1kWp, Inverter/Charger | 15.000–25.000 EUR | 5.000–10.000 EUR | 20.000–35.000 EUR |

**F33: Gibt es eine sinnvolle Reihenfolge beim schrittweisen Upgrade?**
Ja — der höchste ROI zuerst: (1) Externen Lichtmaschinenregler nachrüsten (Balmar/Wakespeed, ~500 EUR, Diesel-Ersparnis sofort spürbar). (2) Solar auf MPPT umrüsten oder erweitern (ROI in 1–2 Saisons). (3) Landstrom-Ladegerät modernisieren (besseres Ladeprofil = längere Batterielebensdauer). (4) DC-DC-Wandler bei Smart-Alternator oder Blei/LiFePO4-Mischsystem. (5) Systemmonitor (Victron BMV/SmartShunt — erst Transparenz, dann Optimierung). (6) LiFePO4-Umbau ZULETZT (teuerste Maßnahme, aber alle vorherigen Upgrades sind kompatibel).

**F34: Wie erkenne ich ein gutes Marine-Elektrik-Fachunternehmen?**
Qualitätsindikatoren: (1) Victron Professional Installer oder Mastervolt Certified — bedeutet Herstellerschulung. (2) Bereitschaft zur vollständigen Dokumentation (Schaltpläne, Berechnungen, Prüfprotokoll). (3) Kenntnis der ISO 10133/13297 und ABYC E-11. (4) Referenzen mit Fotos fertiggestellter Installationen. (5) Garantie auf Arbeit (min. 2 Jahre). Warnsignale: Keine Schaltpläne, "das machen wir immer so", falsche Sicherungsgrößen, fehlende Beschriftung.

(Confidence: documented — Hersteller-Dokumentation, Fachforen, Praxiserfahrung)

---

## 9. Glossar

| Nr. | Begriff | Erklärung |
|-----|---------|-----------|
| 1 | **Absorption (Stufe)** | Zweite Ladephase (IUoU): Konstantspannung, Strom sinkt, bis Batterie voll (Tailcurrent erreicht) |
| 2 | **AGM** | Absorbent Glass Mat — Blei-Batterie mit in Glasfaservlies gebundenem Elektrolyt, wartungsfrei |
| 3 | **ABYC E-11** | Standard der American Boat and Yacht Council für elektrische Systeme auf Booten |
| 4 | **B2B-Charger** | Battery-to-Battery-Charger — DC-DC-Wandler, der Starterbatterie als Quelle nutzt und Servicebatterie korrekt lädt |
| 5 | **BMS** | Battery Management System — Überwacht und schützt LiFePO4-Zellen (Über-/Unterspannung, Temperatur, Balancing) |
| 6 | **Boost (Stufe)** | Alternative Bezeichnung für Bulk-Phase (besonders bei Lichtmaschinenreglern) |
| 7 | **Bulk (Stufe)** | Erste Ladephase (IUoU): Konstantstrom mit maximalem Ladestrom, bis Absorptionsspannung erreicht |
| 8 | **Bypass-Diode** | Diode in Solarmodulen, die verschattete Zellen überbrückt und Hotspot-Bildung verhindert |
| 9 | **CC-CV** | Constant Current / Constant Voltage — Ladekennlinie für LiFePO4 (äquivalent zu Bulk/Absorption) |
| 10 | **Cell Balancing** | Ausgleich der Zellspannungen in einem Lithium-Pack durch Umladen zwischen Zellen |
| 11 | **Cerbo GX** | Victron-Systemmonitor und Gateway mit Touchscreen, Venus OS, VRM-Cloud-Anbindung |
| 12 | **Dumpload** | Lastwiderstand, der überschüssige Energie von Wind-/Hydrogeneratoren in Wärme umwandelt |
| 13 | **DVCC** | Distributed Voltage and Current Control — Victron-Protokoll zur koordinierten Ladung aller Quellen via GX-Gerät |
| 14 | **Egalisierung** | Gezielte Überladung bei 15,5–16V zum Ausgleich von Zellunterschieden (nur Nassbatterien!) |
| 15 | **EFOY** | Methanol-Brennstoffzelle für Bordstrom (Hersteller: SFC Energy) |
| 16 | **Feldstrom** | Erregerstrom der Lichtmaschine — steuert die Ausgangsspannung und -leistung |
| 17 | **Float (Stufe)** | Dritte Ladephase: Niedrige Erhaltungsspannung (13,2–13,8V), hält Batterie bei 100% SOC |
| 18 | **Galvanic Isolator** | Sperrdioden-Paar im Schutzleiter, das galvanische Streuströme <1,6V blockiert (Korrosionsschutz) |
| 19 | **Gasung** | Elektrolyse des Wassers bei Überladung — erzeugt Wasserstoff (H2) und Sauerstoff (O2), explosiv! |
| 20 | **Hot-Spot** | Lokale Überhitzung in Solarzelle bei Verschattung — kann Modul zerstören, Bypass-Dioden verhindern dies |
| 21 | **Hydrogenerator** | Schleppgenerator im Wasser (z.B. Watt&Sea) — erzeugt Strom aus Fahrt durch Wasser |
| 22 | **IP-Schutzart** | Ingress Protection — Schutzgrad gegen Fremdkörper/Wasser (IP22 = Tropfwasser, IP65 = Strahlwasser, IP67 = zeitweises Untertauchen) |
| 23 | **IUoU** | Dreistufige Ladekennlinie nach DIN 41773: Konstantstrom → Konstantspannung → Float |
| 24 | **LiFePO4** | Lithium-Eisenphosphat — sicherste Lithium-Chemie für Marine-Anwendungen (3,2V Nennspannung/Zelle) |
| 25 | **Lastabwurf** | Plötzliche Trennung der Last von einer Lichtmaschine — erzeugt gefährliche Spannungsspitze |
| 26 | **MPPT** | Maximum Power Point Tracking — Algorithmus zur optimalen Leistungsentnahme aus Solarmodulen |
| 27 | **MasterBus** | Proprietäres CAN-Bus-Kommunikationssystem von Mastervolt für marine Energiesysteme |
| 28 | **Nominale Modulspannung** | Vereinfachte Spannungsangabe eines Solarmoduls (z.B. "12V-Modul" = 18V Vmp) |
| 29 | **Open Circuit Voltage (Voc)** | Leerlaufspannung eines Solarmoduls — höher als Vmp, steigt bei Kälte |
| 30 | **PSH** | Peak Sun Hours — Äquivalente Vollsonnenstunden pro Tag an einem Standort |
| 31 | **PWM** | Pulse Width Modulation — einfacher Solarregler, verbindet Panel direkt mit Batterie (Spannungsverlust) |
| 32 | **PowerAssist** | Victron-Funktion: Inverter/Charger ergänzt schwachen Landstrom bei Spitzenlast aus der Batterie |
| 33 | **Recondition** | Vierte Ladestufe bei CTEK-Geräten — desulfatierende Überladung für geschädigte Batterien |
| 34 | **Sense-Leitung** | Separate Messleitung vom Regler direkt zur Batterie für exakte Spannungsmessung (kompensiert Kabelverlust) |
| 35 | **Smart Alternator** | Drehzahl-/lastabhängig geregelte Lichtmaschine moderner Motoren (Euro 6) — liefert oft nur 12,4V! |
| 36 | **SOC** | State of Charge — Ladezustand der Batterie in Prozent (0–100%) |
| 37 | **Sulfatierung** | Bildung von Bleisulfat-Kristallen auf Batterieplatten bei chronischer Unterladung — irreversibel ab gewissem Grad |
| 38 | **Tailcurrent** | Strom am Ende der Absorptionsphase — unterschreitet er 1–2% von C10, gilt die Batterie als voll |
| 39 | **Temperaturkompensation** | Anpassung der Ladespannung an die Batterietemperatur (typisch -30mV/°C für 12V-Blei, 0 für LiFePO4) |
| 40 | **Trenntrafo** | Trenntransformator — galvanische Trennung zwischen Landstromnetz und Bordnetz (bester Korrosionsschutz) |
| 41 | **VE.Can** | Victron CAN-Bus-Protokoll für Hochgeschwindigkeits-Kommunikation zwischen Geräten |
| 42 | **VE.Direct** | Victron proprietärer serieller Datenbus für Regler/Ladegeräte → GX-Geräte |
| 43 | **Vmp** | Voltage at Maximum Power Point — optimale Betriebsspannung eines Solarmoduls unter Last |
| 44 | **VRM** | Victron Remote Management — Cloud-Portal zur Fernüberwachung des Energiesystems |
| 45 | **Wirkungsgrad** | Verhältnis von Ausgangsleistung zu Eingangsleistung eines Wandlers/Ladegeräts (typisch 85–96%) |
| 46 | **Zellbalancing** | Siehe Cell Balancing — Ausgleich der Einzelzellspannungen in einem Batteriepack |
| 47 | **Zyklenlebensdauer** | Anzahl vollständiger Lade-/Entladezyklen bis Kapazität auf 80% sinkt (AGM: 400–600, LiFePO4: 3.000–5.000) |
| 48 | **DOD** | Depth of Discharge — Entladetiefe in Prozent (50% DOD bei AGM = halbe Kapazität nutzbar) |
| 49 | **SOH** | State of Health — Gesundheitszustand einer Batterie in % der ursprünglichen Kapazität |
| 50 | **Peukert-Effekt** | Kapazitätsminderung bei hohen Entladeströmen (betrifft Blei, kaum LiFePO4) |
| 51 | **Ladeverteiler** | Dioden- oder FET-basierter Verteiler für parallele Ladung mehrerer Batteriebänke |
| 52 | **VSR** | Voltage Sensitive Relay — Spannungsgesteuertes Trennrelais (verbindet Banken bei >13,3V) |
| 53 | **Cyrix** | Victron-Markenname für intelligente Batterie-Trennrelais (Cyrix-ct, Cyrix-Li-ct) |
| 54 | **PowerAssist** | Victron-Funktion: Inverter ergänzt schwachen Landstrom aus Batterie bei Spitzenlast |
| 55 | **Hub-4** | Victron-Steuerungsmodus für netzgekoppelte Systeme (weniger relevant marine) |
| 56 | **Venus OS** | Linux-basiertes Betriebssystem der Victron GX-Geräte (Open Source) |
| 57 | **Equalization** | Englisch für Egalisierung — gezielte Überladung zum Zellausgleich (nur Nassbatterien) |
| 58 | **C-Rate** | Lade-/Entladestrom als Vielfaches der Kapazität (1C bei 200Ah = 200A) |
| 59 | **Lithium-Plating** | Abscheidung von metallischem Lithium bei Laden unter 0°C — irreversibler Kapazitätsverlust |
| 60 | **STC** | Standard Test Conditions für Solarmodule (25°C Zelltemp., 1000W/m², AM 1.5) |

---

## 10. Schnell-Referenz

### 10.1 Ladespannungen — Kurzreferenz (12V-System, 25°C)

| Batterie-Typ | Absorption (V) | Float (V) | Max. Strom | Egalisierung |
|-------------|---------------|----------|-----------|-------------|
| Nass (Blei-Säure) | 14.4–14.6 | 13.2–13.5 | C/5 | 15.5–16.0 V alle 30 Tage |
| AGM (Standard) | 14.2–14.4 | 13.2–13.4 | C/5 | Nicht empfohlen |
| AGM (Spiralzelle, Optima) | 14.4–14.7 | 13.2–13.5 | C/3 | Nicht empfohlen |
| Gel (Sonnenschein, Mastervolt) | 14.0–14.2 | 13.2–13.4 | C/10 | Niemals! |
| LiFePO4 (4S, 12.8V) | 14.0–14.4 | 13.4 oder AUS | 0.5C | Niemals! |
| Carbon-Blei (Firefly Oasis) | 14.4–14.7 | 13.2–13.5 | C/2 | 15.5 V (selten) |

### 10.2 Ladespannungen — Kurzreferenz (24V-System, 25°C)

| Batterie-Typ | Absorption (V) | Float (V) | Max. Strom | Egalisierung |
|-------------|---------------|----------|-----------|-------------|
| Nass (Blei-Säure) | 28.8–29.2 | 26.4–27.0 | C/5 | 31.0–32.0 V |
| AGM (Standard) | 28.4–28.8 | 26.4–26.8 | C/5 | Nicht empfohlen |
| Gel | 28.0–28.4 | 26.4–26.8 | C/10 | Niemals! |
| LiFePO4 (8S, 25.6V) | 28.0–28.8 | 26.8 oder AUS | 0.5C | Niemals! |

### 10.3 Kabelquerschnitt-Tabelle (Ladegerät -> Batterie, max. 3% Spannungsabfall)

| Strom (A) | 1m | 2m | 3m | 5m | 7m | 10m |
|-----------|-----|-----|-----|-----|-----|------|
| 10A | 1.5 mm2 | 2.5 mm2 | 4 mm2 | 6 mm2 | 10 mm2 | 16 mm2 |
| 20A | 2.5 mm2 | 6 mm2 | 6 mm2 | 10 mm2 | 16 mm2 | 25 mm2 |
| 30A | 4 mm2 | 6 mm2 | 10 mm2 | 16 mm2 | 25 mm2 | 35 mm2 |
| 50A | 6 mm2 | 10 mm2 | 16 mm2 | 25 mm2 | 35 mm2 | 50 mm2 |
| 70A | 10 mm2 | 16 mm2 | 25 mm2 | 35 mm2 | 50 mm2 | 70 mm2 |
| 100A | 16 mm2 | 25 mm2 | 35 mm2 | 50 mm2 | 70 mm2 | 95 mm2 |

(12V-System, Hin- und Rückleiter berücksichtigt, Kupferleitfähigkeit 56 m/Ohm*mm2)

### 10.4 Solar-Dimensionierung — Schnellrechner

```
Schritt 1: Tagesverbrauch bestimmen
  -> Alle Verbraucher x Betriebsstunden = Ah/Tag
  Typisch: Segelyacht 12m = 40–80 Ah/Tag, Motoryacht 15m = 80–150 Ah/Tag

Schritt 2: Installierte Wp berechnen
  Nordeuropa: Wp = Ah/Tag x 12V / (3.5 h x 0.85) = Ah/Tag x 4.0
  Mittelmeer:  Wp = Ah/Tag x 12V / (5.0 h x 0.85) = Ah/Tag x 2.8
  Tropen:      Wp = Ah/Tag x 12V / (5.5 h x 0.85) = Ah/Tag x 2.6

Schritt 3: MPPT-Regler dimensionieren
  Ausgangsstrom = Wp / V_absorption
  Sicherheitsmarge: +20%

Beispiel: 60Ah/Tag, Mittelmeer, 12V:
  Wp = 60 x 2.8 = 168Wp -> 200Wp installieren (2x100Wp)
  Regler: 200 / 14.4 x 1.2 = 16.7A -> SmartSolar 75/20 oder 100/20
```

### 10.5 Empfohlene Systemkonfigurationen nach Bootsgröße

| Bootsgröße | Batterie | Landstrom | Solar | Lichtmaschine | DC-DC |
|-----------|---------|---------|-------|--------------|-------|
| <8m Trailer | 1x100Ah AGM | IP65 12/10 | 100Wp + PWM | Intern | — |
| 8–10m Küste | 1x200Ah AGM | IP22 12/20 | 200Wp + MPPT 75/15 | Intern + VSR | — |
| 10–13m Fahrt | 2x150Ah AGM | IP22 12/30 | 400Wp + MPPT 100/30 | Ext. Regler | Orion 12/12-30 |
| 13–16m Blauwasser | 400Ah LiFePO4 | Phoenix 12/50 | 600Wp + MPPT 150/45 | Ext. Regler + Booster | Orion 12/12-50 |
| 16–20m Motor | 800Ah AGM/24V | ChargeMaster 24/80 | 800Wp + 2xMPPT | 2x ext. Regler | DC Master 24/12-50 |
| 20m+ Superyacht | 1200Ah+ LiFePO4/24V | Quattro 24/8000 | 1500Wp + 3xMPPT 250/60 | High-Output Lima | Mehrere DC-DC |

### 10.6 Temperaturkompensation — Spannungskorrektur

> ⚠️ **ZU PRÜFEN (Audit):** −0,030 V/°C = −30 mV/°C (hier und Glossar Nr. 39) vs. −18 mV/°C in Abschnitt 2.2 („−3 mV/°C pro Zelle × 6 Zellen = −18 mV/°C"), in der Balmar-MC-614-Preset-Tabelle und im Pydantic-Default `temp_compensation_mv_per_c = -18.0`. Interner Widerspruch beim Temperaturkoeffizienten für 12V-Blei. Beide Werte kommen herstellerabhängig vor (−3 bis −5 mV/°C pro Zelle → −18 bis −30 mV/°C), daher hier NICHT geraten/geändert. Die aggressivere −30-mV/°C-Kurve ergibt bei 0 °C ~0,3 V höhere Absorptionsspannung (15,15 V statt 14,85 V nach der Formel in Abschnitt 2.2) → Überladungsrisiko. Vor Anwendung zwingend gegen die konkrete Batterie-/Ladegerät-Herstellervorgabe abgleichen. **Confidence dieser Sektion: estimated — unverifiziert.**

```
Faustregel für Blei-Batterien (12V-System):
  Korrektur = -0.030 V pro °C Abweichung von 25°C (pro 12V-Block)

Beispiele:
  Temperatur  Absorption (AGM)   Float (AGM)
  ─────────────────────────────────────────────
  0°C         14.4 + 0.75 = 15.15V   13.3 + 0.75 = 14.05V
  10°C        14.4 + 0.45 = 14.85V   13.3 + 0.45 = 13.75V
  25°C        14.4 + 0.00 = 14.40V   13.3 + 0.00 = 13.30V (Referenz)
  35°C        14.4 - 0.30 = 14.10V   13.3 - 0.30 = 13.00V
  45°C        14.4 - 0.60 = 13.80V   13.3 - 0.60 = 12.70V

ACHTUNG: LiFePO4 = KEINE Temperaturkompensation!
  LiFePO4 immer bei 14.2V laden, unabhängig von Temperatur.
  Stattdessen: Ladung ABSCHALTEN unter 5°C Zelltemperatur!

24V-System: Alle Werte x2
```

### 10.7 MPPT-Regler-Auswahlmatrix

| PV-Leistung (Wp) | Panelkonfiguration (12V) | Min. Regler (Victron) | Alternativ |
|-------------------|--------------------------|----------------------|------------|
| 50–100 | 1x Modul, 18–22V Vmp | SmartSolar 75/10 | Genasun GV-4 |
| 100–200 | 2x parallel oder 1x36V | SmartSolar 75/15 | Genasun GV-10 |
| 200–350 | 2x in Serie (36–44V) | SmartSolar 100/20 | Morningstar SunSaver MPPT |
| 350–500 | 2x in Serie (36–44V) | SmartSolar 100/30 | Morningstar TriStar MPPT 30 |
| 500–700 | 3x in Serie (55–66V) | SmartSolar 150/35 | Mastervolt SCM60 |
| 700–1000 | 3–4x in Serie (66–88V) | SmartSolar 150/45 | — |
| 1000–1500 | 4x in Serie (88–110V) | SmartSolar 250/60 | — |
| >1500 | Mehrere Strings/Regler | 2–3x SmartSolar 250/70 | — |

**Wichtig:** Voc (Leerlauf bei Kälte!) darf NIEMALS den max. PV-Eingang des Reglers überschreiten!
Sicherheitsformel: Max. Voc bei -10°C = Voc(STC) x 1.15 (kristallines Silizium)

### 10.8 Ladegerät-Dimensionierung nach Bootsgröße und Nutzungsprofil

```
┌─────────────────────────────────────────────────────────────────────────┐
│  LADEGERÄT-DIMENSIONIERUNG (Landstrom)                                  │
│                                                                         │
│  Mindest-Ladestrom = Batterie-Kapazität x Faktor                       │
│                                                                         │
│  Faktor nach Nutzungsprofil:                                            │
│    Dauerlieger (>200 Tage/Jahr Landstrom):    10% der Kapazität        │
│    Wochenendsegler (Laden Fr-So):             20% der Kapazität        │
│    Fahrtenyacht (3-4h Hafenaufenthalt):       25% der Kapazität        │
│    Charter (max. 8h über Nacht laden):        30% der Kapazität        │
│    LiFePO4 (schneller ladbar):                bis 50% der Kapazität    │
│                                                                         │
│  Beispiel: 300Ah AGM, Fahrtenyacht                                      │
│    Mindest-Ladegerät: 300 x 0.25 = 75A                                 │
│    -> Victron Phoenix Smart IP43 12/50 (realistisch)                    │
│    -> oder 2x Blue Smart IP22 12/30 (2x30A = 60A, knapp)               │
│                                                                         │
│  Maximaler Ladestrom nach Batterie-Typ:                                 │
│    Nass Blei-Säure:  max 20% (C/5)                                     │
│    AGM:              max 20-30% (C/5 bis C/3)                           │
│    Gel:              max 10% (C/10)                                     │
│    LiFePO4:          max 50% (0.5C) - BMS begrenzt                     │
│    Carbon-Blei:      max 50% (C/2)                                     │
└─────────────────────────────────────────────────────────────────────────┘
```

### 10.9 Lichtmaschinen-Leistung vs. Drehzahl (typische Werte)

| LiMa Nennleistung | Leerlauf (800rpm Motor) | Fahrt (1800rpm) | Vollgas (3000rpm) | Effektive Marine-Nutzung |
|-------------------|-------------------------|-----------------|-------------------|--------------------------|
| 55A (Standard) | 15A (27%) | 35A (64%) | 50A (91%) | 30A Durchschnitt |
| 80A (Standard) | 22A (28%) | 52A (65%) | 72A (90%) | 45A Durchschnitt |
| 100A (Marine) | 30A (30%) | 70A (70%) | 92A (92%) | 60A Durchschnitt |
| 120A (Marine/Ext. Regler) | 40A (33%) | 90A (75%) | 110A (92%) | 80A Durchschnitt |
| 150A (High-Output) | 50A (33%) | 110A (73%) | 140A (93%) | 95A Durchschnitt |
| 200A (Leece-Neville/Electromaax) | 65A (33%) | 145A (73%) | 185A (93%) | 130A Durchschnitt |

**Hinweis:** "Nennleistung" ist typisch bei 6.000 rpm Generator-Drehzahl gemessen. Marine-Motoren laufen bei 1.500–2.500 rpm Motor = 3.000–5.000 rpm Generator (Übersetzung ~2:1). Effektive Marine-Nutzung berücksichtigt Thermal-Derating und reale Fahrtdrehzahlen.

### 10.10 Solarertrag — Monatswerte nach Region (kWh/kWp)

| Monat | Nordsee/Ostsee | Atlantik (Biskaya) | Mittelmeer West | Kanaren | Karibik |
|-------|---------------|-------------------|----------------|---------|---------|
| Jan | 0.5 | 1.5 | 2.5 | 3.5 | 5.0 |
| Feb | 1.0 | 2.0 | 3.0 | 4.0 | 5.5 |
| Mar | 2.0 | 3.0 | 4.0 | 5.0 | 6.0 |
| Apr | 3.5 | 4.0 | 5.0 | 5.5 | 6.0 |
| Mai | 4.5 | 5.0 | 5.5 | 6.0 | 5.5 |
| Jun | 5.0 | 5.5 | 6.5 | 6.5 | 5.5 |
| Jul | 4.5 | 5.5 | 7.0 | 7.0 | 6.0 |
| Aug | 4.0 | 5.0 | 6.5 | 6.5 | 6.0 |
| Sep | 3.0 | 4.0 | 5.0 | 5.5 | 5.5 |
| Okt | 1.5 | 2.5 | 3.5 | 4.5 | 5.0 |
| Nov | 0.8 | 1.5 | 2.5 | 3.5 | 5.0 |
| Dez | 0.4 | 1.2 | 2.0 | 3.0 | 5.0 |
| **Jahres-kWh/kWp** | **31** | **41** | **53** | **60** | **66** |

**Umrechnung auf Ah/Tag:**
Ah/Tag = kWh/kWp-Monatswert x installierte_kWp x 1000 / (30 x System-V x 0.85)
Beispiel: 500Wp, Juli, Mittelmeer: 7.0 x 0.5 x 1000 / (30 x 14 x 0.85) = 9.8A Durchschnitt x 24h... vereinfacht: ca. 165Ah/Tag

### 10.11 Fehler-Schnelldiagnose: "Batterie wird nicht voll"

```
┌────────────────────────────────────────────────────────────────────┐
│  SCHNELL-CHECK: "Batterie wird nicht voll geladen"                 │
│                                                                    │
│  1. Spannung an Batterie-Polen messen (bei Ladung):               │
│     □ <13.8V  → Ladequelle liefert zu wenig (Regler-Einstellung?) │
│     □ 13.8-14.4V → Korrekt? Dann weiter zu 2.                    │
│     □ >14.6V  → Zu hoch! Profil prüfen (AGM statt Gel?)          │
│                                                                    │
│  2. Differenz Ladegerät-Ausgang vs. Batterie-Pole:                │
│     □ <0.2V   → OK, kein Kabelproblem                             │
│     □ 0.2-0.5V → Verbindungen prüfen, ggf. Sense-Leitung         │
│     □ >0.5V   → KRITISCH! Kabel/Verbindungen/Schalter defekt     │
│                                                                    │
│  3. Ladestrom bei 50% SOC:                                         │
│     □ >15% von C10 → OK, Bulk-Phase                               │
│     □ <5% von C10  → Ladegerät zu klein oder Batterie sulfatiert  │
│     □ 0A          → Ladegerät in Float? Timer prüfen              │
│                                                                    │
│  4. Ruhespannung nach 4h Ruhe (keine Last, kein Laden):           │
│     □ 12.8V = 100%  □ 12.5V = 75%   □ 12.2V = 50%               │
│     □ 12.0V = 25%   □ 11.8V = 10%   □ <11.5V = LEER/DEFEKT      │
│                                                                    │
│  5. Wenn Spannung korrekt aber SOC zu niedrig:                     │
│     → Kapazitätstest (C20): <80% = Batterie am Lebensende         │
│     → Innenwiderstand messen: >2x Neuwert = defekt                │
└────────────────────────────────────────────────────────────────────┘
```

### 10.12 Victron-Produktauswahl — Schnellmatrix

| Anwendung | Produkt | Kapazität | Preis (ca.) | Besonderheit |
|-----------|---------|-----------|-------------|--------------|
| Erhaltungsladung (Winterlager) | Blue Smart IP65 12/5 | 5A | 80 EUR | IP65, Bluetooth |
| Kleines Boot / Trailer | Blue Smart IP65 12/15 | 15A | 130 EUR | IP65, Bluetooth |
| Standard-Segelyacht | Blue Smart IP22 12/30 | 30A | 200 EUR | 3 Ausgänge, Bluetooth |
| Fahrtenyacht (groß) | Phoenix Smart IP43 12/50 | 50A | 420 EUR | IP43, lüftergesteuert |
| Langfahrt/Charter | Phoenix Smart IP43 12/30 (3) | 3x30A | 550 EUR | 3 isolierte Ausgänge |
| Solar (bis 200Wp) | SmartSolar MPPT 75/15 | 15A | 110 EUR | VE.Direct, BT |
| Solar (bis 440Wp) | SmartSolar MPPT 100/30 | 30A | 180 EUR | VE.Direct, BT |
| Solar (bis 650Wp) | SmartSolar MPPT 150/35 | 35A | 250 EUR | VE.Direct, BT |
| Solar (bis 1300Wp) | SmartSolar MPPT 250/60 | 60A | 480 EUR | VE.Can + VE.Direct |
| DC-DC (klein) | Orion-Tr Smart 12/12-18 | 18A | 150 EUR | Isoliert, Bluetooth |
| DC-DC (standard) | Orion-Tr Smart 12/12-30 | 30A | 220 EUR | Isoliert, Bluetooth |
| Inverter/Charger | MultiPlus-II 12/3000/120 | 120A Charger | 1.500 EUR | 3kVA Inverter + Charger |
| System-Monitor | Cerbo GX + GX Touch 50 | — | 550 EUR | VRM Cloud, DVCC |

### 10.13 Typische Tagesverbräuche nach Bootsgröße und Nutzung

| Szenario | Verbrauch (Ah/12V) | Hauptverbraucher |
|----------|-------------------|-----------------|
| 8m Segelboot, Wochenende | 20–40 Ah | Beleuchtung, Instrumente, Kühlbox |
| 10m Segelboot, Ankernacht | 40–60 Ah | Kühlschrank, Ankerlampe, Instrumente, VHF |
| 12m Fahrtenyacht, Seetag | 80–120 Ah | Autopilot, Kühlschrank, Radar, Navigation |
| 12m Fahrtenyacht, Ankertag | 60–90 Ah | Kühlschrank, Watermaker (1h), Laptop, Licht |
| 14m Motoryacht, Hafen | 100–150 Ah | Klimaanlage, Kühlschrank/Tiefkühler, Entertainment |
| 14m Motoryacht, Anker | 120–180 Ah | Generator-Support nötig für Klima |
| 16m+ Katamaran, Langfahrt | 140–200 Ah | 2x Kühlschrank, Watermaker, Autopilot, Instrumente |
| 20m+ Superyacht | 300–600 Ah | Klimaanlage, Crew, Hydraulik-Standby |

### 10.14 Notfall-Referenz: Kritische Spannungswerte

```
┌─────────────────────────────────────────────────────────────────┐
│  ALARM-SCHWELLENWERTE (12V-System)                              │
│                                                                 │
│  ÜBERSPANNUNG (Schäden an Elektronik):                          │
│    >14.8V (AGM-System)     → Ladeprofil prüfen / Ladung stoppen│
│    >14.6V (LiFePO4)       → BMS muss abschalten / Sofort-Stopp│
│    >15.5V (Motor läuft)   → Regler defekt! MOTOR AUS!         │
│    >18V                   → Lichtmaschine durchlegiert → NOTAUS│
│                                                                 │
│  UNTERSPANNUNG (Tiefentladung / Abschaltung):                   │
│    <12.0V (Blei)          → 25% SOC, Verbraucher reduzieren    │
│    <11.5V (Blei)          → KRITISCH, Tiefentladung droht      │
│    <10.5V (Blei)          → Batterie-Schutz muss trennen!      │
│    <10.0V (LiFePO4)       → BMS hat bereits getrennt / Fehler  │
│    <2.5V/Zelle (LiFePO4)  → Zellschaden, irreversibel!        │
│                                                                 │
│  TEMPERATUR-GRENZEN:                                            │
│    >45°C Blei-Batterie    → Ladung drosseln (Temp-Kompensation)│
│    >55°C Blei-Batterie    → Ladung STOPPEN                     │
│    >45°C LiFePO4          → BMS muss Ladung drosseln           │
│    <5°C LiFePO4           → Ladung SPERREN (Lithium-Plating!)  │
│    <0°C LiFePO4           → NIEMALS laden!                      │
│    >65°C Ladegerät        → Thermisches Derating beginnt       │
│    >85°C Ladegerät        → Thermische Abschaltung             │
│    >100°C Lichtmaschine   → Ext. Regler muss Strom begrenzen  │
└─────────────────────────────────────────────────────────────────┘
```

### 10.15 Verdrahtungs-Checkliste: Neues Ladegerät installieren

```
□ 1. Batterie-Typ identifizieren (Nass/AGM/Gel/LiFePO4)
□ 2. Batterie-Kapazität (Ah) und Ladegerät-Strom prüfen (max. C/5 für AGM)
□ 3. Kabelquerschnitt nach Strom UND Länge dimensionieren (Tabelle 10.3)
□ 4. Kabel mit Ringkabelschuhen versehen (Crimp, nicht Löten!)
□ 5. Sicherung batterieseitig installieren (1,5x Nennstrom, max. 30cm von Batterie)
□ 6. Masse-Kabel: Sternpunkt am Batterie-Minuspol (nicht Rumpf-Masse!)
□ 7. Temperatursensor direkt auf Batteriegehäuse kleben (nicht auf Kabel!)
□ 8. Voltage-Sense-Leitung zur Batterie (wenn vorhanden)
□ 9. Ladeprofil korrekt einstellen:
     - Batterie-Typ
     - Absorptionsspannung (Hersteller-Vorgabe!)
     - Float-Spannung
     - Temperaturkompensation (AN für Blei, AUS für LiFePO4)
     - Egalisierung (nur Nassbatterien, Timer begrenzen!)
□ 10. Ersttest: Spannung an Batterie-Polen während Ladung messen
      - Soll: Absorptionsspannung minus max. 0,1V
□ 11. Belüftung: Ladegerät braucht min. 10cm Freiraum um Lüfter
□ 12. Galvanische Isolation: Bei Landstrom IMMER Galvanic Isolator oder Trenntrafo
□ 13. VE.Direct/Bluetooth konfigurieren (wenn Victron)
□ 14. Beschriftung: Ladegerät + Kabel + Sicherung beschriften!
□ 15. Dokumentation: Schaltplan aktualisieren, Fotos machen
```

### 10.16 Preisvergleich nach Leistungsklasse (Stand 2025, ca. EUR)

| Leistungsklasse | Victron | Mastervolt | Sterling | CTEK |
|-----------------|---------|------------|----------|------|
| 5A Erhaltung | IP65 12/5: 80 | — | — | MXS 5.0: 70 |
| 15A Standard | IP22 12/15: 140 | EasyCharge 12/15: 180 | — | M15: 160 |
| 25A Mittel | IP22 12/25: 170 | EasyCharge 12/25: 240 | Pro Charge B 12/25: 220 | M25 EU: 230 |
| 30A Standard | IP22 12/30: 200 | ChargeMaster Plus 12/25: 380 | Pro Charge Ultra 12/30: 350 | — |
| 50A Groß | Phoenix 12/50: 420 | ChargeMaster Plus 12/50: 650 | Pro Charge Ultra 12/50: 480 | — |
| 80A XL | Phoenix 12/75: 580 | ChargeMaster Plus 12/75: 850 | Pro Charge Ultra 12/60: 530 | — |
| 100A+ | Quattro 12/5000: 2.800 | Mass Combi Ultra 12/3000: 3.200 | — | — |

**Anmerkung:** Mastervolt ist durchschnittlich 40–60% teurer bei vergleichbarer Ladeleistung, bietet aber Superyacht-Zulassungen (Lloyds, BV, DNV) und MasterBus-Integration.

---

## ANHANG A — Fallstudie: LiFePO4-Umbau Bavaria 40 Cruiser (2012)

### A.1 Ausgangssituation

**Boot:** Bavaria 40 Cruiser, Baujahr 2012, 12,35m LOA
**Eigner:** Langfahrt-Paar, Abfahrt Mittelmeer → Karibik geplant
**Problem:** Bestehende 2x 110Ah AGM-Batterien (4 Jahre alt) liefern nur noch ca. 60% Kapazität. Täglicher Verbrauch: 140Ah. Motorbetrieb zum Laden: 3–4h/Tag.

### A.2 Diagnose (AYDI Level 2)

| Komponente | Befund | Bewertung |
|-----------|--------|-----------|
| Service-Batterien | 2x Victron AGM 110Ah, IRmin 8,2mΩ (Neuwert: 4,5mΩ) | Lebensende |
| Ladegerät | Mastervolt EasyCharge 10A — unterdimensioniert, 16h für Volladung | Unzureichend |
| Lichtmaschine | Bosch 80A intern geregelt, liefert effektiv 35A bei Fahrtdrehzahl | Unzureichend |
| Solaranlage | 1x 100Wp Panel, PWM-Regler — liefert max. 5A | Unterdimensioniert |
| Windgenerator | Keiner | — |

### A.3 Lösung

**Neue Batteriebank:**
- 2x Victron Smart LiFePO4 200Ah (400Ah total, nutzbar: 320Ah bei 80% DOD)
- Victron Smart BMS 12/200 mit Bluetooth und VE.Can

**Ladesystem komplett erneuert:**
- Landstrom: Victron Blue Smart IP22 30A/3-Output (LiFePO4-Profil, Starterbatterie-Ladung)
- Solar: 4x 120Wp SunPower (480Wp total) + 2x Victron SmartSolar MPPT 75/15
- Lichtmaschine: Wakespeed WS500 externer Regler (CAN-Bus-Anbindung an Victron BMS via DVCC)
- DC-DC: Victron Orion-Tr Smart 12/12-30 (Lichtmaschine → LiFePO4 mit BMS-Kommunikation)
- Monitoring: Victron Cerbo GX + GX Touch 50 + SmartShunt 500A

### A.4 Ergebnis

| Kennzahl | Vorher | Nachher |
|----------|--------|---------|
| Nutzbare Kapazität | 110Ah (50% DOD AGM) | 320Ah (80% DOD LiFePO4) |
| Tages-Solarertrag (Mittelmeer) | 25Ah | 140Ah |
| Motorbetrieb zum Laden | 3–4h/Tag | 0,5–1h/Tag (nur bei Bewölkung) |
| Zeit bis Volladung (Landstrom) | 16h | 4h |
| Gewicht Batteriesystem | 64 kg | 52 kg |
| Gesamtkosten Umbau | — | 8.400 EUR |
| AYDI-Score Elektrik | 34/100 | 94/100 |

**AYDI-Befund:** Amortisation durch reduzierten Motorbetrieb (Diesel-Ersparnis: ca. 800 EUR/Saison) + Batterielebensdauer (LiFePO4: 8–10 Jahre vs. AGM: 3–5 Jahre) in 4–5 Jahren.

---

## ANHANG B — Fallstudie: Solar-Optimierung Lagoon 42 (2019)

### B.1 Ausgangssituation

**Boot:** Lagoon 42, Baujahr 2019, 12,80m LOA (Katamaran)
**Eigner:** Charter-Management-Firma, Boot auf den Kanaren
**Problem:** Trotz 6 Solarpanels (angeblich 900Wp) auf dem Hardtop erreicht die Bank selten 100% SOC. Chartercrews beschweren sich über leere Batterien am Morgen.

### B.2 Diagnose (AYDI Level 2)

| Problem | Detail | Severity |
|---------|--------|----------|
| Panel-Leistung | 6x 150Wp = 900Wp nominal, aber Module stark verschmutzt (Salz, Möwenkot) | MITTEL |
| Regler | 1x Victron BlueSolar MPPT 150/35 für alle 6 Panels in Serie (Voc = 270V!) | HOCH |
| Verschattung | 2 Panels permanent im Schatten des Radartowers (ab 14:00 Uhr) | HOCH |
| Kabelung | 2,5mm² von Panels zu Regler (8m Strecke), Spannungsabfall 4,2% | MITTEL |
| String-Problem | Alle 6 Module in Serie — ein verschattetes Panel limitiert gesamten String | KRITISCH |

### B.3 Lösung

- String-Aufteilung: 2 Strings zu je 3 Panels (unverschattete Backbord-Seite / teilverschattete Steuerbord-Seite)
- 2x Victron SmartSolar MPPT 100/20 statt 1x BlueSolar 150/35
- Panels professionell gereinigt und mit Nano-Beschichtung versiegelt
- Kabel erneuert: 6mm² (Spannungsabfall <1,5%)
- VE.Smart Networking zwischen beiden Reglern aktiviert
- Radarturm-Panel um 30cm versetzt (Schattenwurf eliminiert)

### B.4 Ergebnis

| Kennzahl | Vorher | Nachher |
|----------|--------|---------|
| Tages-Solarertrag (Winter, Kanaren) | 85Ah | 165Ah |
| Tages-Solarertrag (Sommer, Kanaren) | 130Ah | 260Ah |
| Batterieladezustand morgens (nach Nacht) | 55–65% | 85–95% |
| Charter-Beschwerden "Strom" | 3–4/Monat | 0 |
| Kosten Umbau | — | 1.200 EUR |
| AYDI-Score Solar-Subsystem | 42/100 | 89/100 |

---

## ANHANG C — Fallstudie: Lichtmaschinen-Optimierung Hallberg-Rassy 36 (2008)

### C.1 Ausgangssituation

**Boot:** Hallberg-Rassy 36 MkII, Baujahr 2008, 10,86m LOA
**Eigner:** Segelehepaar, Langfahrt Norwegen → Spanien (Jahresreise)
**Problem:** Trotz 3–4h Motorbetrieb/Tag werden die 400Ah-AGM-Banken nie voll. Batterien nach 2 Jahren bereits sulfatiert.

### C.2 Diagnose

| Komponente | Befund | Detail |
|-----------|--------|--------|
| Lichtmaschine | Valeo 80A mit internem Regler | Liefert effektiv nur 30–40A (interner Regler konservativ) |
| Ladeverhalten | Absorption nur bei >2.500 U/min, unter Fahrt (1.800 U/min) nur 25A | Unzureichend |
| Temperatur | LiMa-Gehäuse 95°C nach 1h unter Last | Thermisch grenzwertig |
| Riemen | Standard-Keilriemen, Schlupf bei >50A | Unterdimensioniert |
| Kabel B+-Leitung | 16mm², 3,5m, Spannungsabfall unter Last: 0,8V | Verlust! |

### C.3 Lösung

- Balmar MC-614 externer Regler + Balmar SG200 SmartGauge (Batterie-SOC)
- Balmar Alternator Belt Manager (begrenzt Strom bei niedrigen Drehzahlen)
- Keilriemen ersetzt durch Breitkeilriemen (Serpentine Belt Conversion Kit)
- B+-Kabel erneuert: 35mm² (Spannungsabfall <0,15V)
- Temperatursensor an Lichtmaschine (MC-614 Feature: Thermal-Derating)

### C.4 Ergebnis

| Kennzahl | Vorher | Nachher |
|----------|--------|---------|
| Effektiver Ladestrom (1.800 U/min) | 25A | 55A |
| Effektiver Ladestrom (2.200 U/min) | 40A | 72A |
| Zeit bis 80% SOC (ab 50%) | >3h | 1,5h |
| Motorbetrieb/Tag zum Laden | 3–4h | 1,5–2h |
| Dieselverbrauch Laden/Tag | 5–7L | 2,5–3,5L |
| Gesamtkosten | — | 1.850 EUR |
| AYDI-Score Ladeinfrastruktur | 38/100 | 78/100 |

**AYDI-Befund:** Amortisation durch Diesel-Ersparnis in ca. 1,5 Saisons. Zusätzlicher Benefit: Weniger Motorbetrieb = weniger Wartung + besseres Segelerlebnis.

---

## ANHANG D — Fallstudie: 24V-Systemaufbau Swift Trawler 47 (2017)

### D.1 Ausgangssituation

**Boot:** Beneteau Swift Trawler 47, Baujahr 2017, 14,33m LOA
**Eigner:** Motorboot-Eigner, primär Küstenfahrt Nordsee/Atlantik
**Problem:** Werftinstallation mit Standard-12V-System, aber 14m-Boot mit Bugstrahler, Klimaanlage, Watermaker — alle Kabelquerschnitte am Limit. Spannungsabfälle von 8–12% auf langen Wegen.

### D.2 Analyse

Der Swift Trawler 47 wurde werkseitig mit einem 12V-System ausgeliefert, obwohl die Verbraucherlast und die Bootslänge ein 24V-System nahelegen. Probleme:
- Batteriekabel Maschinenraum → Bug: 50mm² auf 11m = 5,8% Drop bei Bugstrahlerlast (150A)
- Ankerwinde: 35mm² auf 13m = 7,2% Drop bei 80A
- Gesamtruhestrom: 8,5A (primär Kühlschrank, Standby-Verbraucher)
- Landstromladegerät: 2x Mastervolt ChargeMaster 12/25 (je 25A) = total unterdimensioniert für 600Ah-Bank

### D.3 Lösung: Teilumstellung auf 24V

- Service-Bank: 4x Victron Smart LiFePO4 12.8V/200Ah → 2S2P = 25,6V/400Ah
- Landstrom: Victron Phoenix Smart IP43 24/25 (25A bei 24V = effektiv 50A-Äquivalent bei 12V)
- Lichtmaschine: Balmar 24V/110A mit Wakespeed WS500
- Solar: 4x 200Wp = 800Wp, 2x Victron SmartSolar MPPT 100/30
- DC-DC: Victron Orion-Tr 24/12-30 für 12V-Subsystem (Navigationsgeräte, Beleuchtung)
- Monitoring: Victron Cerbo GX + 2x SmartShunt (24V-Bank + 12V-Subsystem)

### D.4 Ergebnis

| Kennzahl | Vorher (12V) | Nachher (24V) |
|----------|-------------|---------------|
| Spannungsabfall Bugstrahler | 5,8% | 1,4% (bei halber Stromstärke) |
| Kabelquerschnitt Hauptverteiler | 50mm² | 25mm² (gleiche Leistung) |
| Effektive Ladekapazität | 50A/12V = 600W | 110A/24V = 2.640W |
| Ladedauer 0–80% | 8h | 2h |
| Kupfergewicht Kabel gesamt | 85 kg | 48 kg |
| Gesamtkosten Umbau | — | 18.500 EUR |
| AYDI-Score Elektrik | 45/100 | 91/100 |

---

## ANHANG E — Fallstudie: Atlantiküberquerung Amel 50 — Energiemanagement

### E.1 Ausgangssituation

**Boot:** Amel 50 (Super Maramu), Baujahr 2003, 15,38m LOA
**Eigner:** Erfahrenes Langfahrt-Paar, ARC-Teilnahme Las Palmas → St. Lucia
**Herausforderung:** 18–22 Tage ohne Landstrom, Autopilot 24/7, Kühlschrank/Tiefkühler, Watermaker 2h/Tag, Navigation/Kommunikation. Tagesverbrauch: 180Ah/12V.

### E.2 Energiebilanz-Planung

| Quelle | Tagesmittel (Tradewind-Zone) | Beitrag |
|--------|------------------------------|---------|
| Solar (6x 120Wp = 720Wp) | 160Ah | 89% des Bedarfs |
| Windgenerator (Superwind 350) | 30Ah (bei 15–20kn apparent) | 17% des Bedarfs |
| Hydrogenerator (Watt&Sea Cruise 600) | 40Ah (bei 7kn SOG) | 22% des Bedarfs |
| **Gesamt-Erzeugung** | **230Ah** | **128% des Bedarfs** |
| **Reserve** | **+50Ah** | **Puffer für Bewölkung** |
| Motor/Generator | 0 (Notfall-Reserve) | — |

### E.3 Ladesystem-Konfiguration

- Batterien: 4x Victron Smart LiFePO4 200Ah = 800Ah (nutzbar 640Ah = 3,5 Tage Autonomie)
- Solar-MPPT: 3x Victron SmartSolar 100/20 (je 2 Module)
- Wind-Regler: Superwind integriert + Victron SmartShunt zur Erfassung
- Hydro-Regler: Watt&Sea integrierter MPPT → Victron-System via SmartShunt
- Lichtmaschine: Balmar 150A + MC-614 (Backup, nur bei 3+ Tagen ohne Sonne/Wind)
- Koordination: Victron Cerbo GX + DVCC, VRM über Iridium-Satellite (täglicher Status-Upload)
- Überspannungsschutz: Sterling LPVD als letzte Absicherung

### E.4 Ergebnis der Überfahrt

| Kennzahl | Geplant | Tatsächlich |
|----------|---------|-------------|
| Überfahrtdauer | 18 Tage | 19 Tage |
| Motorbetrieb zum Laden | 0h | 0h (Motor nur zum Einlaufen St. Lucia) |
| Niedrigster SOC (Bank) | >40% | 52% (Tag 7, 2 Bewölkungstage) |
| Durchschnittlicher Tages-Solarertrag | 160Ah | 148Ah (einige Bewölkung) |
| Hydrogenerator-Beitrag | 40Ah/Tag | 45Ah/Tag (gute Passatwind-Bedingungen) |
| Windgenerator-Beitrag | 30Ah/Tag | 22Ah/Tag (Apparent-Wind unter Segeln geringer) |
| Generator/Motor gestartet zum Laden | 0 | 0 |
| Diesel-Verbrauch gesamt | — | 35L (nur Motorbetrieb beim Einlaufen) |

**AYDI-Befund:** System korrekt dimensioniert. Hydrogenerator war der entscheidende Faktor für die wolkigen Tage. VRM-Fernüberwachung ermöglichte Support-Calls von Land bei Systemfragen.

---

## ANHANG F — Fallstudie: Charter-Katamaran Fountaine Pajot Elba 45 — Ladeprobleme

### F.1 Ausgangssituation

**Boot:** Fountaine Pajot Elba 45, Baujahr 2021, 13,41m LOA
**Betreiber:** Charter-Management Kroatien, 25 Charterwochen/Saison
**Problem:** Wiederholte Reklamationen: "Kühlschrank warm morgens", "Autopilot schaltet ab", "Batteriewarnung". Werft-Erstinstallation angeblich ausreichend dimensioniert.

### F.2 Diagnose (AYDI Level 2)

| Problem | Ursache | Severity |
|---------|---------|----------|
| Chronische Unterladung | Werkseitige 2x Victron BlueSolar PWM 30A an 12V-Panels → nur ~18A effektiv | KRITISCH |
| Falsches Batterieprofil | Solarregler auf "Gel" eingestellt, tatsächlich AGM verbaut → Absorption zu niedrig | HOCH |
| Kühlschrank-Verbrauch | 2x Waeco CRX-65 = 8A Dauerlast (192Ah/Tag!) — Charter-Crews öffnen ständig | HOCH |
| Batteriebank | 3x 115Ah AGM = 345Ah, nutzbar 172Ah (50% DOD) — reicht nicht für Nacht | MITTEL |
| Nacht-Autonomie | 192Ah Kühlschrank + 20Ah Standby = 212Ah > 172Ah nutzbar | KRITISCH |

### F.3 Lösung

- Solarregler: 2x Victron SmartSolar MPPT 100/30 (statt PWM) → +40% Ertrag
- Panel-Upgrade: 4x 200Wp statt 4x 100Wp (Platz auf Hardtop vorhanden)
- Batterieprofil: Korrekt auf AGM eingestellt (14,4V Absorption, 13,6V Float)
- Zusätzliche Batterie: 4. AGM 115Ah → 460Ah total = 230Ah nutzbar
- Kühlschrank-Optimierung: Thermostat auf +5°C statt werkseitigem +3°C, Crew-Briefing "Tür zu!"
- Landstrom-Ladegerät: Upgrade auf Victron Blue Smart IP22 30A (statt werksseitigem 15A-Gerät)
- Monitoring: Victron BMV-712 mit Bluetooth für Charter-Crews (SOC-Anzeige im Salon)

### F.4 Ergebnis

| Kennzahl | Vorher | Nachher |
|----------|--------|---------|
| Tages-Solarertrag (Kroatien, Sommer) | 65Ah | 185Ah |
| Nacht-Autonomie (Ankerbucht) | 8h (dann kritisch) | 22h (Puffer bis Mittag) |
| Charter-Reklamationen "Strom" | 8/Saison | 0/Saison |
| Batterien ersetzt/Saison | 1 Satz/2 Jahre | 1 Satz/4 Jahre (prognostiziert) |
| Kosten Umbau | — | 3.200 EUR |
| AYDI-Score Elektrik | 31/100 | 79/100 |

---

## ANHANG G — Fallstudie: J/112E Regattayacht — Gewichtsoptimiertes Ladesystem

### G.1 Ausgangssituation

**Boot:** J/112E, Baujahr 2020, 11,20m LOA
**Eigner:** Regatta-Team, IRC-Rennen + gelegentliche Kurzfahrten
**Anforderung:** Minimales Gewicht, maximale Zuverlässigkeit für 4-Tage-Offshore-Regatten. Verbraucher: Autopilot (Regatta), Instrumente, AIS, VHF, 2x Lampen Kajüte.

### G.2 Energiebilanz (Regatta-Modus)

| Verbraucher | Strom | Laufzeit/Tag | Ah/Tag |
|-------------|-------|-------------|--------|
| B&G Autopilot (WTP3) | 4A (Durchschnitt) | 18h | 72 |
| Instrumente + MFD | 2A | 24h | 48 |
| AIS Class B | 0,5A | 24h | 12 |
| VHF (Standby) | 0,3A | 24h | 7 |
| LED-Positionslichter | 0,5A | 10h | 5 |
| Kajütbeleuchtung | 0,5A | 4h | 2 |
| **Gesamt** | | | **146Ah** |

### G.3 Lösung: Minimalsystem mit LiFePO4

- Batterie: 1x Victron Smart LiFePO4 12.8V/200Ah (26 kg statt 2x60Ah AGM = 36 kg → 10 kg gespart!)
- Solar: 2x 50Wp semiflexibel auf Heckspiegel (Gewicht: 2x 1,2 kg)
- Regler: 1x Genasun GV-5 (70g, IP67, lüfterlos — leichtester Marine-MPPT)
- Lichtmaschine: Standard Yanmar 80A + Wakespeed WS500 (3-Tages-Regatta: Motor nur Ein-/Auslaufen)
- Ladegerät: CTEK M15 (1,5 kg) — nur im Hafen
- Monitoring: Victron SmartShunt 500A + Bluetooth (Handy-App statt separates Display)

**Gesamtgewicht Elektrik:** 31,5 kg (vs. konventionelles AGM-System: 52 kg)

### G.4 Ergebnis

| Kennzahl | Detail |
|----------|--------|
| Gewichtsersparnis vs. konventionell | 20,5 kg |
| Autonomie ohne Laden (Regatta) | 36h (200Ah nutzbar / 146Ah Tagesverbrauch × 80% DOD) |
| Solar-Beitrag (Sommertag) | 35Ah (kompensiert 24% des Verbrauchs) |
| 4-Tage-Offshore: Motor-Ladung nötig? | 1x 2h am Tag 3 (wenn bewölkt) |
| Gesamtkosten | 3.800 EUR |
| AYDI-Score Elektrik (Regatta-Profil) | 88/100 |

---

## ANHANG H — Fallstudie: Werkstatt-Diagnostik — Systematische Fehlersuche bei "Boot lädt nicht"

### H.1 Ausgangssituation

**Boot:** Bavaria 34 Cruiser, Baujahr 2015, im Hafen Kiel
**Symptom:** "Batterie immer leer trotz Landstrom". Eigner berichtet: Ladegerät-LED leuchtet grün ("voll"), aber Kühlschrank läuft nicht durch die Nacht.

### H.2 Systematische Diagnose (AYDI Troubleshooting-Protokoll)

**Schritt 1: Spannungsmessung an Batterie-Polen**
- Ergebnis: 12,3V bei "voller" Batterie laut Ladegerät → Batterie ist NICHT voll (Soll: 12,8V)

**Schritt 2: Spannungsmessung am Ladegerät-Ausgang**
- Ergebnis: 14,4V am Ladegerät (korrekt) → Ladegerät funktioniert!

**Schritt 3: Spannungsmessung an Batteriepolen WÄHREND Ladung**
- Ergebnis: 13,1V an Batterie, 14,4V am Ladegerät → 1,3V Differenz!

**Schritt 4: Kabelverfolgung Ladegerät → Batterie**
- Befund: 3 Sicherungshalter + 1 Batterieschalter + 1 Verteilerblock in der Leitung
- Spannungsabfall an jedem Element gemessen:
  - Sicherungshalter 1: 0,15V (korrodiert)
  - Sicherungshalter 2: 0,05V (OK)
  - Batterieschalter: 0,4V (Kontakte oxidiert!)
  - Sicherungshalter 3: 0,3V (Sicherung lose im Halter)
  - Verteilerblock: 0,4V (Schraube locker, Kabelschuh nicht gecrimpt sondern gelötet)
  - **Gesamt: 1,3V Verlust** ✓ (stimmt mit Messung überein)

**Schritt 5: Ursachenanalyse**
- Ladegerät sieht 14,4V an seinen Klemmen → geht korrekt in Float
- Batterie erhält aber nur 13,1V → wird nie voll geladen
- Progressiv schlimmer: Jede Korrosionsstelle erhöht sich über die Jahre
- Ladegerät hat keine Voltage-Sense-Leitung (altes Modell)

### H.3 Maßnahmen

1. Batterieschalter: Kontakte gereinigt (Scotch-Brite) + Kontaktfett (Caig DeoxIT Gold)
2. Sicherungshalter 1+3: Ersetzt durch Blue Sea MRBF-Halter (Edelstahl)
3. Verteilerblock: Lötverbindung entfernt, korrekt gecrimpt + Schrumpfschlauch
4. Alle Schraubverbindungen: Nachgezogen auf korrektes Drehmoment
5. Voltage-Sense-Leitung: 2x 0,75mm² vom Ladegerät direkt zu Batterie-Polen (5m)
6. Optional empfohlen: Ladegerät-Upgrade auf Victron Blue Smart IP22 mit integriertem Sense

### H.4 Ergebnis

| Kennzahl | Vorher | Nachher |
|----------|--------|---------|
| Spannung an Batterie bei Ladung | 13,1V | 14,35V |
| Spannungsabfall Ladegerät→Batterie | 1,3V | 0,05V |
| Batteriezustand nach Nachladung | 12,3V (75% SOC) | 12,8V (100% SOC) |
| Kühlschrank-Autonomie über Nacht | 6h | 14h (durchgehend bis Morgen) |
| Materialkosten Reparatur | — | 145 EUR |
| Arbeitszeit | — | 3h |
| AYDI-Score Elektrik | 41/100 | 76/100 |

**AYDI-Kernbefund:** 95% aller "Ladegerät lädt nicht"-Probleme sind KEINE Ladegerät-Defekte, sondern Kabel- und Verbindungsprobleme. Immer zuerst Spannung direkt an der Batterie messen!

(Confidence: documented — Werkstattpraxis, AYDI-Diagnosepfad verifiziert)

---

## ANHANG I–R — AYDI-Integration (Pydantic v2 Modelle)

### ANHANG I — Datenmodelle: Ladegerät-Bewertung

```python
"""
AYDI Pydantic v2 Models — Ladegeräte und Laderegler (22.04)
Alle user-facing Texte: Deutsch. Code und Variablennamen: Englisch.
"""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


# --- Enums ---


class ConfidenceLevel(str, Enum):
    measured = "measured"
    calculated = "calculated"
    visual_high = "visual_high"
    visual_medium = "visual_medium"
    visual_low = "visual_low"
    visual_insufficient = "visual_insufficient"
    estimated = "estimated"
    benchmark = "benchmark"
    documented = "documented"


class BatteryChemistry(str, Enum):
    wet_lead_acid = "wet_lead_acid"
    agm = "agm"
    gel = "gel"
    lifepo4 = "lifepo4"
    carbon_lead = "carbon_lead"
    agm_spiral = "agm_spiral"


class ChargerType(str, Enum):
    shore_power = "shore_power"
    alternator_internal = "alternator_internal"
    alternator_external = "alternator_external"
    mppt_solar = "mppt_solar"
    pwm_solar = "pwm_solar"
    dc_dc_boost = "dc_dc_boost"
    dc_dc_buck = "dc_dc_buck"
    dc_dc_isolated = "dc_dc_isolated"
    wind_controller = "wind_controller"
    hydro_controller = "hydro_controller"
    inverter_charger = "inverter_charger"
    fuel_cell = "fuel_cell"


class ChargingPhase(str, Enum):
    bulk = "bulk"
    absorption = "absorption"
    float_ = "float"
    equalization = "equalization"
    storage = "storage"
    desulfation = "desulfation"
    off = "off"


class SeverityLevel(str, Enum):
    critical = "critical"
    warning = "warning"
    info = "info"
    ok = "ok"


# --- Basis-Modelle ---


class ChargerSpec(BaseModel):
    """Spezifikation eines einzelnen Ladegeräts oder Ladereglers."""

    model_config = {"from_attributes": True}

    manufacturer: str = Field(..., description="Hersteller")
    model: str = Field(..., description="Modellbezeichnung")
    charger_type: ChargerType = Field(..., description="Typ des Ladegeräts")
    nominal_voltage_v: float = Field(..., ge=6, le=60, description="Nennspannung Ausgang (V)")
    max_current_a: float = Field(..., ge=0, le=500, description="Maximaler Ladestrom (A)")
    max_power_w: Optional[float] = Field(None, ge=0, description="Maximale Leistung (W)")
    num_outputs: int = Field(1, ge=1, le=6, description="Anzahl Ausgänge")
    has_temperature_compensation: bool = Field(False)
    has_bluetooth: bool = Field(False)
    has_ve_direct: bool = Field(False)
    has_can_bus: bool = Field(False)
    has_nmea2000: bool = Field(False)
    galvanic_isolation: bool = Field(False)
    ip_rating: Optional[str] = Field(None, description="IP-Schutzart")
    weight_kg: Optional[float] = Field(None, ge=0)
    battery_profiles: list[str] = Field(default_factory=list)
    suitable_for_lifepo4: bool = Field(False)
    price_eur: Optional[float] = Field(None, ge=0)


class ChargingProfile(BaseModel):
    """Ladeprofil-Konfiguration für eine bestimmte Batteriechemie."""

    model_config = {"from_attributes": True}

    battery_chemistry: BatteryChemistry
    absorption_voltage_v: float = Field(..., ge=12.0, le=60.0)
    float_voltage_v: Optional[float] = Field(None, ge=12.0, le=60.0)
    equalization_voltage_v: Optional[float] = Field(None, ge=12.0, le=65.0)
    max_charge_current_a: Optional[float] = Field(None, ge=0)
    absorption_time_min: Optional[int] = Field(None, ge=0, le=600)
    temp_compensation_mv_per_c: float = Field(
        -18.0, description="Temperaturkompensation mV/C (12V-System)"
    )
    reference_temp_c: float = Field(25.0)
    min_charge_temp_c: Optional[float] = Field(
        None, description="Minimale Ladetemperatur (wichtig für LiFePO4)"
    )


class SolarPanelConfig(BaseModel):
    """Konfiguration einer Solarpanel-Installation."""

    model_config = {"from_attributes": True}

    total_wp: float = Field(..., ge=0, le=10000, description="Gesamte installierte Leistung (Wp)")
    num_panels: int = Field(..., ge=1, le=50)
    panel_wp: float = Field(..., ge=0, le=600, description="Leistung pro Panel (Wp)")
    panel_voc: float = Field(..., ge=0, le=60, description="Leerlaufspannung pro Panel (V)")
    panel_vmp: float = Field(..., ge=0, le=55, description="MPP-Spannung pro Panel (V)")
    panel_imp: float = Field(..., ge=0, le=20, description="MPP-Strom pro Panel (A)")
    num_strings: int = Field(1, ge=1, le=10)
    panels_per_string: int = Field(1, ge=1, le=10)
    cable_length_m: float = Field(..., ge=0, le=50, description="Kabellänge Panel->Regler (m)")
    cable_cross_section_mm2: float = Field(..., ge=0.5, le=50, description="Kabelquerschnitt (mm2)")
    shading_risk: str = Field("none", description="Verschattungsrisiko: none, low, medium, high")


class AlternatorConfig(BaseModel):
    """Lichtmaschinen-Konfiguration."""

    model_config = {"from_attributes": True}

    manufacturer: str = Field(..., description="Hersteller der Lichtmaschine")
    model: Optional[str] = Field(None)
    rated_output_a: float = Field(..., ge=0, le=500, description="Nennleistung (A)")
    voltage_v: float = Field(..., ge=12, le=48)
    regulator_type: str = Field("internal", description="internal oder external")
    external_regulator_model: Optional[str] = Field(None)
    has_temperature_sensor: bool = Field(False)
    belt_type: str = Field("v_belt", description="v_belt, serpentine, dual_v")
    idle_output_a: Optional[float] = Field(
        None, ge=0, description="Ausgangsleistung bei Leerlaufdrehzahl"
    )


# --- Bewertungsmodelle ---


class ChargerFinding(BaseModel):
    """Einzelner Befund bei der Ladegerät-Bewertung."""

    model_config = {"from_attributes": True}

    component: str = Field(..., description="Betroffene Komponente")
    severity: SeverityLevel
    finding_de: str = Field(..., description="Befund (Deutsch)")
    recommendation_de: str = Field(..., description="Empfehlung (Deutsch)")
    estimated_cost_eur: Optional[float] = Field(None, ge=0)
    confidence: ConfidenceLevel


class ChargingSystemAssessment(BaseModel):
    """Gesamtbewertung des Ladesystems einer Yacht."""

    model_config = {"from_attributes": True}

    # Metadaten
    boat_class: str = Field(..., description="Bootsklasse")
    system_voltage_v: float = Field(..., ge=12, le=48)
    battery_chemistry: BatteryChemistry
    battery_capacity_ah: float = Field(..., ge=0, le=10000)
    daily_consumption_ah: Optional[float] = Field(None, ge=0)

    # Ladequellen
    chargers: list[ChargerSpec] = Field(default_factory=list)
    solar_config: Optional[SolarPanelConfig] = Field(None)
    alternator_config: Optional[AlternatorConfig] = Field(None)

    # Bewertung
    overall_score: int = Field(..., ge=0, le=100)
    shore_charger_score: int = Field(..., ge=0, le=100)
    solar_score: int = Field(..., ge=0, le=100)
    alternator_score: int = Field(..., ge=0, le=100)
    dc_dc_score: int = Field(..., ge=0, le=100)
    integration_score: int = Field(..., ge=0, le=100, description="Systemintegration")
    safety_score: int = Field(..., ge=0, le=100)

    # Befunde
    findings: list[ChargerFinding] = Field(default_factory=list)
    total_charge_capacity_a: float = Field(
        ..., ge=0, description="Summierter maximaler Ladestrom aller Quellen"
    )
    charge_to_capacity_ratio: float = Field(
        ..., ge=0, description="Ladestrom / Batteriekapazität (ideal: 0.1-0.3)"
    )
    estimated_full_charge_hours: Optional[float] = Field(
        None, ge=0, description="Geschätzte Ladezeit 50%->100% SOC (Stunden)"
    )
    solar_autonomy_percent: Optional[float] = Field(
        None, ge=0, le=200, description="Solar-Tagesertrag / Tagesverbrauch x 100"
    )

    confidence: ConfidenceLevel
```

### ANHANG J — Datenmodelle: Solar-Dimensionierung

```python
class SolarDimensioningInput(BaseModel):
    """Eingabedaten für Solar-Dimensionierungsberechnung."""

    model_config = {"from_attributes": True}

    system_voltage_v: float = Field(12.0, ge=12, le=48)
    daily_consumption_ah: float = Field(..., ge=0, le=1000)
    cruising_region: str = Field(
        ..., description="Region: nordeuropa, mittelmeer, karibik, tropen, pazifik"
    )
    available_area_m2: Optional[float] = Field(None, ge=0, le=100)
    shading_factor: float = Field(
        1.0, ge=0.0, le=1.0, description="1.0=keine Verschattung, 0.5=50% verschattet"
    )
    battery_chemistry: BatteryChemistry = Field(BatteryChemistry.agm)
    budget_eur: Optional[float] = Field(None, ge=0)


class SolarDimensioningResult(BaseModel):
    """Ergebnis der Solar-Dimensionierungsberechnung."""

    model_config = {"from_attributes": True}

    recommended_wp: float = Field(..., ge=0)
    recommended_panels: int = Field(..., ge=0)
    recommended_panel_wp: float = Field(..., ge=0)
    recommended_controller: str = Field(..., description="Empfohlener MPPT-Regler")
    recommended_controller_current_a: float = Field(..., ge=0)
    recommended_cable_mm2: float = Field(..., ge=0)
    estimated_daily_yield_ah: float = Field(..., ge=0)
    autonomy_percent: float = Field(
        ..., ge=0, description="Solarertrag / Verbrauch x 100"
    )
    estimated_cost_eur: float = Field(..., ge=0)
    peak_sun_hours: float = Field(..., ge=0, le=12)
    findings: list[str] = Field(default_factory=list)
    confidence: ConfidenceLevel
```

### ANHANG K — Datenmodelle: Lichtmaschinen-Bewertung

```python
class AlternatorAssessment(BaseModel):
    """Bewertung der Lichtmaschinen-Ladekonfiguration."""

    model_config = {"from_attributes": True}

    alternator_manufacturer: str
    alternator_model: Optional[str] = None
    rated_output_a: float = Field(..., ge=0)
    estimated_effective_output_a: float = Field(
        ..., ge=0, description="Effektive Ladeleistung an Batterie (nach Verlusten)"
    )
    regulator_type: str = Field(..., description="internal oder external")
    regulator_model: Optional[str] = None

    overall_score: int = Field(..., ge=0, le=100)
    regulator_score: int = Field(..., ge=0, le=100)
    cable_score: int = Field(..., ge=0, le=100)
    belt_score: int = Field(..., ge=0, le=100)
    charging_profile_score: int = Field(..., ge=0, le=100)

    estimated_time_to_80pct_h: Optional[float] = Field(None, ge=0)
    estimated_time_to_100pct_h: Optional[float] = Field(None, ge=0)
    voltage_drop_v: Optional[float] = Field(None, ge=0)

    findings: list[ChargerFinding] = Field(default_factory=list)
    recommendations: list[str] = Field(default_factory=list)
    confidence: ConfidenceLevel
```

### ANHANG L — Datenmodelle: DC-DC-Wandler-Bewertung

```python
class DCDCConverterAssessment(BaseModel):
    """Bewertung eines DC-DC-Wandlers / Ladeboosters."""

    model_config = {"from_attributes": True}

    converter_manufacturer: str
    converter_model: str
    input_voltage_v: float = Field(..., ge=6, le=60)
    output_voltage_v: float = Field(..., ge=6, le=60)
    max_current_a: float = Field(..., ge=0, le=200)
    is_isolated: bool = Field(False)
    has_charging_profile: bool = Field(False, description="Vollständiges Ladeprofil")
    has_engine_detection: bool = Field(False, description="Motorlauferkennung")

    overall_score: int = Field(..., ge=0, le=100)
    sizing_score: int = Field(..., ge=0, le=100, description="Dimensionierung")
    feature_score: int = Field(..., ge=0, le=100, description="Funktionsumfang")
    installation_score: int = Field(..., ge=0, le=100, description="Installationsqualität")

    findings: list[ChargerFinding] = Field(default_factory=list)
    confidence: ConfidenceLevel
```

### ANHANG M — Datenmodelle: Visueller Ladegerät-Befund

```python
class VisualChargerInspection(BaseModel):
    """Visueller Befund eines Ladegeräts (Pipeline B)."""

    model_config = {"from_attributes": True}

    charger_identified: bool = Field(..., description="Ladegerät auf Foto erkannt")
    charger_manufacturer: Optional[str] = None
    charger_model: Optional[str] = None
    charger_type: Optional[ChargerType] = None

    housing_condition: str = Field(
        "unknown", description="Gehäusezustand: good, scratched, corroded, melted, cracked"
    )
    cable_condition: str = Field(
        "unknown", description="Kabelzustand: good, frayed, corroded, undersized, melted"
    )
    terminal_condition: str = Field(
        "unknown", description="Klemmenzustand: good, corroded, loose, overheated"
    )
    ventilation_adequate: Optional[bool] = Field(None, description="Ausreichende Belüftung?")
    mounting_secure: Optional[bool] = Field(None, description="Sicher montiert?")
    led_status: Optional[str] = Field(None, description="LED-Anzeige falls sichtbar")

    visual_score: int = Field(..., ge=0, le=100)
    safety_concerns: list[str] = Field(default_factory=list)
    findings: list[ChargerFinding] = Field(default_factory=list)
    confidence: ConfidenceLevel
```

### ANHANG N — Datenmodelle: Ladegerät-Fehlerbild

```python
class ChargerFaultPattern(BaseModel):
    """Strukturiertes Fehlerbild für Ladegeräte und Laderegler."""

    model_config = {"from_attributes": True}

    fault_id: str = Field(..., description="Eindeutige Fehlerbild-ID (z.B. CHG-F01)")
    fault_name_de: str = Field(..., description="Fehlerbild-Name (Deutsch)")
    category: str = Field(
        ..., description="Kategorie: overcharge, undercharge, hardware, wiring, config"
    )

    symptoms: list[str] = Field(..., min_length=1, description="Symptome (Deutsch)")
    root_causes: list[str] = Field(..., min_length=1, description="Ursachen (Deutsch)")
    measurements: list[str] = Field(default_factory=list, description="Relevante Messwerte")
    immediate_action_de: str = Field(..., description="Sofortmaßnahme")
    repair_de: str = Field(..., description="Reparatur/Lösung")
    estimated_cost_range_eur: tuple[float, float] = Field(
        ..., description="Geschätzte Kosten (min, max) in EUR"
    )
    severity: SeverityLevel
    confidence: ConfidenceLevel
```

### ANHANG O — Datenmodelle: Parallelladung-Analyse

```python
class ParallelChargingAnalysis(BaseModel):
    """Analyse der Parallelladung mehrerer Quellen."""

    model_config = {"from_attributes": True}

    num_sources: int = Field(..., ge=1, le=10)
    sources: list[ChargerSpec] = Field(..., min_length=1)
    battery_chemistry: BatteryChemistry
    battery_capacity_ah: float = Field(..., ge=0)

    total_max_current_a: float = Field(..., ge=0)
    current_to_capacity_ratio: float = Field(..., ge=0)
    voltage_conflict_detected: bool = Field(False)
    absorption_voltage_spread_v: float = Field(
        ..., ge=0, description="Differenz höchste/niedrigste Absorptionsspannung"
    )
    coordination_method: Optional[str] = Field(
        None, description="Koordinationsmethode: dvcc, voltage_stagger, none"
    )
    bms_can_control_all: Optional[bool] = Field(
        None, description="BMS kann alle Quellen abschalten (LiFePO4)?"
    )

    overall_score: int = Field(..., ge=0, le=100)
    conflict_risk_score: int = Field(..., ge=0, le=100, description="Konfliktrisiko")
    findings: list[ChargerFinding] = Field(default_factory=list)
    confidence: ConfidenceLevel
```

### ANHANG P — Bewertungsfunktion: Ladegerät-Dimensionierung

```python
def assess_charger_sizing(
    charger_current_a: float,
    battery_capacity_ah: float,
    battery_chemistry: BatteryChemistry,
    boat_class: str,
) -> tuple[int, list[str], list[str]]:
    """
    Bewertet, ob ein Ladegerät zur Batteriebank passt.

    Returns:
        (score, findings, recommendations)
    """
    findings: list[str] = []
    recommendations: list[str] = []

    ratio = charger_current_a / battery_capacity_ah if battery_capacity_ah > 0 else 0

    ideal_ranges = {
        BatteryChemistry.wet_lead_acid: (0.10, 0.20),
        BatteryChemistry.agm: (0.10, 0.25),
        BatteryChemistry.gel: (0.05, 0.15),
        BatteryChemistry.lifepo4: (0.15, 0.50),
        BatteryChemistry.carbon_lead: (0.10, 0.30),
        BatteryChemistry.agm_spiral: (0.10, 0.30),
    }

    ideal_min, ideal_max = ideal_ranges.get(battery_chemistry, (0.10, 0.25))
    score = 100

    if ratio < ideal_min * 0.5:
        score = 30
        findings.append(
            f"KRITISCH: Ladegerät stark unterdimensioniert "
            f"({charger_current_a}A für {battery_capacity_ah}Ah = {ratio:.1%}). "
            f"Minimum: {ideal_min:.0%} der Kapazität."
        )
        recommendations.append(
            f"Ladegerät mit mindestens {battery_capacity_ah * ideal_min:.0f}A empfohlen."
        )
    elif ratio < ideal_min:
        score = 60
        findings.append(
            f"Ladegerät leicht unterdimensioniert "
            f"({charger_current_a}A für {battery_capacity_ah}Ah = {ratio:.1%})."
        )
    elif ratio > ideal_max * 1.5:
        score = 50
        findings.append(
            f"Ladegerät stark überdimensioniert "
            f"({charger_current_a}A für {battery_capacity_ah}Ah = {ratio:.1%})."
        )
    elif ratio > ideal_max:
        score = 75
        findings.append(
            f"Ladegerät leicht überdimensioniert "
            f"({charger_current_a}A für {battery_capacity_ah}Ah = {ratio:.1%})."
        )
    else:
        findings.append(
            f"Ladegerät korrekt dimensioniert "
            f"({charger_current_a}A für {battery_capacity_ah}Ah = {ratio:.1%})."
        )

    return score, findings, recommendations
```

### ANHANG Q — Bewertungsfunktion: Solar-MPPT-Dimensionierung

```python
def assess_solar_mppt_sizing(
    solar_config: SolarPanelConfig,
    controller_max_current_a: float,
    controller_max_voltage_v: float,
    system_voltage_v: float,
    min_temperature_c: float = -10.0,
) -> tuple[int, list[str], list[str]]:
    """
    Bewertet die Dimensionierung eines MPPT-Solarreglers.

    Returns:
        (score, findings, recommendations)
    """
    findings: list[str] = []
    recommendations: list[str] = []
    score = 100

    # Maximale Eingangsspannung bei Kälte (Voc steigt!)
    temp_factor = 1.0 + (25.0 - min_temperature_c) * 0.004
    max_voc_cold = (
        solar_config.panel_voc * solar_config.panels_per_string * temp_factor
    )

    if max_voc_cold > controller_max_voltage_v:
        score = 0
        findings.append(
            f"KRITISCH: Max. Panel-Spannung bei {min_temperature_c}C = "
            f"{max_voc_cold:.1f}V überschreitet Regler-Maximum "
            f"({controller_max_voltage_v}V). Regler wird beschädigt!"
        )
        recommendations.append(
            "Regler mit höherer Eingangsspannung wählen oder "
            "Panel-String-Konfiguration ändern."
        )
    elif max_voc_cold > controller_max_voltage_v * 0.9:
        score -= 25
        findings.append(
            f"WARNUNG: Panel-Spannung bei Kälte ({max_voc_cold:.1f}V) "
            f"nahe am Regler-Maximum ({controller_max_voltage_v}V)."
        )

    # Ausgangsstrom-Check
    expected_output_a = solar_config.total_wp / (system_voltage_v + 2.0)
    if expected_output_a > controller_max_current_a:
        score -= 30
        findings.append(
            f"Erwarteter Ausgangsstrom ({expected_output_a:.1f}A) übersteigt "
            f"Regler-Maximum ({controller_max_current_a}A)."
        )
        recommendations.append(
            f"Regler mit mindestens {expected_output_a * 1.2:.0f}A empfohlen."
        )

    # Kabelverluste
    cable_resistance = (
        2 * solar_config.cable_length_m
        / (56.0 * solar_config.cable_cross_section_mm2)
    )
    if solar_config.num_strings > 0 and solar_config.panels_per_string > 0:
        string_current = solar_config.panel_imp * solar_config.num_strings
        string_voltage = solar_config.panel_vmp * solar_config.panels_per_string
        if string_voltage > 0:
            cable_loss_pct = (cable_resistance * string_current / string_voltage) * 100
            if cable_loss_pct > 5:
                score -= 20
                findings.append(
                    f"Kabelverluste {cable_loss_pct:.1f}% — zu hoch (>5%)."
                )
            elif cable_loss_pct > 3:
                score -= 10
                findings.append(
                    f"Kabelverluste {cable_loss_pct:.1f}% — akzeptabel, aber >3%."
                )

    return max(0, score), findings, recommendations
```

### ANHANG R — Bewertungsfunktion: Gesamtsystem-Ladeinfrastruktur

```python
def assess_charging_system(
    boat_length_m: float,
    boat_class: str,
    system_voltage_v: float,
    battery_chemistry: BatteryChemistry,
    battery_capacity_ah: float,
    daily_consumption_ah: Optional[float],
    chargers: list[ChargerSpec],
    solar_config: Optional[SolarPanelConfig] = None,
    alternator_config: Optional[AlternatorConfig] = None,
) -> ChargingSystemAssessment:
    """
    Erstellt eine Gesamtbewertung der Ladeinfrastruktur.
    Orchestriert Einzelbewertungen und bewertet Systemintegration.
    """
    findings: list[ChargerFinding] = []
    shore_score = 50
    solar_score = 50
    alternator_score = 50
    dc_dc_score = 50
    safety_score = 100
    integration_score = 100
    total_charge_a = 0.0

    # Shore charger assessment
    shore_chargers = [
        c for c in chargers if c.charger_type == ChargerType.shore_power
    ]
    if shore_chargers:
        primary = shore_chargers[0]
        sizing_score, sizing_findings, sizing_recs = assess_charger_sizing(
            primary.max_current_a, battery_capacity_ah, battery_chemistry, boat_class
        )
        shore_score = sizing_score
        total_charge_a += sum(c.max_current_a for c in shore_chargers)
        for f_text in sizing_findings:
            findings.append(ChargerFinding(
                component="Landstrom-Ladegerät",
                severity=SeverityLevel.info if sizing_score >= 80 else SeverityLevel.warning,
                finding_de=f_text,
                recommendation_de=sizing_recs[0] if sizing_recs else "—",
                confidence=ConfidenceLevel.calculated,
            ))

        # Galvanische Trennung
        if not primary.galvanic_isolation:
            safety_score -= 15
            findings.append(ChargerFinding(
                component="Landstrom-Ladegerät",
                severity=SeverityLevel.warning,
                finding_de="Ladegerät bietet keine galvanische Trennung.",
                recommendation_de="Galvanischen Isolator nachrüsten (ab ~150 EUR).",
                estimated_cost_eur=150.0,
                confidence=ConfidenceLevel.documented,
            ))

        # LiFePO4-Kompatibilität
        if battery_chemistry == BatteryChemistry.lifepo4:
            if not primary.suitable_for_lifepo4:
                safety_score -= 30
                findings.append(ChargerFinding(
                    component="Landstrom-Ladegerät",
                    severity=SeverityLevel.critical,
                    finding_de="Ladegerät ist NICHT für LiFePO4 geeignet!",
                    recommendation_de="Ladegerät mit LiFePO4-Profil ersetzen.",
                    confidence=ConfidenceLevel.documented,
                ))
    else:
        if boat_length_m >= 8:
            findings.append(ChargerFinding(
                component="Landstrom-Ladegerät",
                severity=SeverityLevel.warning,
                finding_de="Kein Landstrom-Ladegerät erkannt.",
                recommendation_de="Landstrom-Ladegerät nachrüsten.",
                confidence=ConfidenceLevel.estimated,
            ))

    # Solar assessment
    if solar_config:
        mppt_regler = [
            c for c in chargers if c.charger_type == ChargerType.mppt_solar
        ]
        if mppt_regler:
            s_score, s_findings, s_recs = assess_solar_mppt_sizing(
                solar_config, mppt_regler[0].max_current_a,
                150.0, system_voltage_v,
            )
            solar_score = s_score
            for f_text in s_findings:
                findings.append(ChargerFinding(
                    component="Solaranlage",
                    severity=SeverityLevel.info if s_score >= 80 else SeverityLevel.warning,
                    finding_de=f_text,
                    recommendation_de=s_recs[0] if s_recs else "—",
                    confidence=ConfidenceLevel.calculated,
                ))
        total_charge_a += solar_config.total_wp / (system_voltage_v + 2)

    # Alternator assessment
    if alternator_config:
        alternator_score = 80 if alternator_config.regulator_type == "external" else 50
        if alternator_config.regulator_type == "internal":
            findings.append(ChargerFinding(
                component="Lichtmaschine",
                severity=SeverityLevel.warning,
                finding_de="Interner Lichtmaschinenregler — Batterie wird nicht voll geladen.",
                recommendation_de="Externen Regler (Balmar MC-614 / Wakespeed WS500) nachrüsten.",
                estimated_cost_eur=300.0,
                confidence=ConfidenceLevel.documented,
            ))
        total_charge_a += alternator_config.rated_output_a * 0.7

    # Overall calculations
    charge_ratio = total_charge_a / battery_capacity_ah if battery_capacity_ah > 0 else 0
    est_charge_hours = (
        (battery_capacity_ah * 0.5) / (total_charge_a * 0.7)
        if total_charge_a > 0 else None
    )

    solar_autonomy = None
    if solar_config and daily_consumption_ah and daily_consumption_ah > 0:
        peak_hours = 4.0
        daily_yield = solar_config.total_wp * peak_hours * 0.85 / system_voltage_v
        solar_autonomy = (daily_yield / daily_consumption_ah) * 100

    overall_score = int(
        shore_score * 0.30 + solar_score * 0.20 + alternator_score * 0.15
        + dc_dc_score * 0.10 + integration_score * 0.10 + safety_score * 0.15
    )

    return ChargingSystemAssessment(
        boat_class=boat_class,
        system_voltage_v=system_voltage_v,
        battery_chemistry=battery_chemistry,
        battery_capacity_ah=battery_capacity_ah,
        daily_consumption_ah=daily_consumption_ah,
        chargers=chargers,
        solar_config=solar_config,
        alternator_config=alternator_config,
        overall_score=overall_score,
        shore_charger_score=shore_score,
        solar_score=solar_score,
        alternator_score=alternator_score,
        dc_dc_score=dc_dc_score,
        integration_score=integration_score,
        safety_score=safety_score,
        findings=findings,
        total_charge_capacity_a=total_charge_a,
        charge_to_capacity_ratio=charge_ratio,
        estimated_full_charge_hours=est_charge_hours,
        solar_autonomy_percent=solar_autonomy,
        confidence=ConfidenceLevel.calculated,
    )
```

---

## ANHANG S — Installations-Best-Practices und Inbetriebnahme

### S.1 Montageorte — Do's und Don'ts

| Gerät | Idealer Montageort | Verbotene Orte | Mindestabstände |
|-------|-------------------|----------------|-----------------|
| Landstrom-Ladegerät | Trockener, belüfteter Raum nahe Batterie | Direkt über Batterie (Gasung!), Maschinenraum (Hitze) | 30cm Abstand zu Batterie, 10cm Luft um Lüfter |
| MPPT-Solarregler | Möglichst nahe an Batterie (Kabelverlust minimieren) | Unbelüftete Backskiste, direkte Sonne | 20cm Luft oben/unten, nicht an Holz |
| DC-DC-Wandler | Vertikale Montage, Lüfter frei, Metallunterlage | Waagerecht mit Lüfter nach unten, Maschinenraum | 15cm Luft allseitig |
| Ext. LiMa-Regler | Trockener Ort, kurze Kabel zur Lichtmaschine | Am Motor selbst (Vibration!), Spritzwasserbereich | Kabellänge Regler→LiMa <2m |
| Windgenerator-Regler | Belüfteter Raum, nahe Dumpload | Neben brennbaren Materialien | 50cm zu Brennbarem (Dumpload glüht!) |
| Batterieüberwachung (Shunt) | Direkt am Batterie-Minuspol | Irgendwo weiter entfernt im Kabelbaum | 0cm — MUSS am Batteriepol sein |

### S.2 Inbetriebnahme-Protokoll: Neues Ladesystem

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  INBETRIEBNAHME-CHECKLISTE LADESYSTEM                                       │
│                                                                             │
│  Phase 1: VOR dem Einschalten                                               │
│  ─────────────────────────────────────────────                              │
│  □ Alle Kabelverbindungen auf Festsitz geprüft (Drehmomentschlüssel!)      │
│  □ Polarität ALLER Anschlüsse verifiziert (+ an +, - an -)                 │
│  □ Sicherungen korrekt dimensioniert und eingesetzt                         │
│  □ Temperatursensor(en) korrekt platziert (auf Batteriegehäuse!)           │
│  □ Sense-Leitungen korrekt angeschlossen                                    │
│  □ Erdung/Bonding korrekt (Sternpunkt, keine Schleifen)                    │
│  □ PV-Module noch abgedeckt / getrennt (kein Strom bei Montage!)           │
│  □ Lichtmaschine: Feldstrom-Kabel erst NACH Programmierung anschließen     │
│  □ BMS korrekt verdrahtet (Allow-to-Charge, Allow-to-Discharge)            │
│                                                                             │
│  Phase 2: Ersteinschaltung                                                  │
│  ─────────────────────────────────                                          │
│  □ Batterie-Trennschalter: EIN                                              │
│  □ Ladegerät-Ausgang messen BEVOR Batterie verbunden (Leerlauf-Test)       │
│  □ Soll: Absorptionsspannung +/- 0.1V                                      │
│  □ Batterie verbinden, Ladestrom beobachten                                │
│  □ Erwarteter Bulk-Strom erreicht? (Wenn Batterie nicht voll)              │
│  □ Solar-Module aufdecken: Strom fließt? MPPT-Tracking aktiv?              │
│  □ Lichtmaschine: Motor starten, Spannung steigt auf >13.8V?              │
│  □ DC-DC: Motor starten, Erkennung aktiv, Ausgangsstrom vorhanden?         │
│                                                                             │
│  Phase 3: Funktionstest (24h-Monitoring)                                    │
│  ──────────────────────────────────────────                                 │
│  □ Nacht-Verbrauch messen (alle Ladequellen aus)                           │
│  □ Solar-Tagesertrag plausibel? (Wp x PSH x 0.85 / Systemspannung)        │
│  □ Absorption korrekt beendet? (Tailcurrent-Abschaltung)                   │
│  □ Float-Spannung korrekt? (Sollwert +/- 0.1V an Batterie-Polen)          │
│  □ Keine unerwarteten Fehler/Warnungen in App/Display?                     │
│  □ Ruhestrom (Standby aller Ladegeräte aus): <50mA System-gesamt          │
│  □ Temperatursensor-Plausibilität (bei 25°C: Spannung = Datenblatt-Wert)  │
│                                                                             │
│  Phase 4: Dokumentation                                                     │
│  ─────────────────────────                                                  │
│  □ Schaltplan aktualisiert (inkl. aller Sicherungswerte)                   │
│  □ Fotos der Installation (für spätere Fehlersuche)                        │
│  □ Einstellungen dokumentiert (Absorption-V, Float-V, Tailcurrent-A)       │
│  □ Firmware-Versionen notiert                                               │
│  □ Seriennummern aller Geräte erfasst (für Garantie + AYDI-Datenbank)      │
│  □ Übergabe-Protokoll an Eigner (inkl. Kurzeinweisung)                     │
└─────────────────────────────────────────────────────────────────────────────┘
```

### S.3 Normen und Zulassungen — Detailreferenz

| Norm/Standard | Geltungsbereich | Relevanz für Ladegeräte |
|--------------|-----------------|--------------------------|
| IEC 60335-2-29 | Sicherheit von Batterieladegeräten | Grundnorm für alle Ladegeräte (Überspannung, Isolation, Temp.) |
| EN 50530 | Wirkungsgrad von PV-Wechselrichtern/MPPT | MPPT-Effizienz-Messverfahren, Europäischer Wirkungsgrad |
| IEC 62109-1/2 | Sicherheit PV-Leistungsumwandler | Solarregler-Sicherheit, Erdschluss-Erkennung |
| EN 60529 | IP-Schutzarten | Mindestanforderung marine: IP22 (innen), IP65 (Cockpit/außen) |
| ISO 10133 | Elektrische Systeme Kleinfahrzeuge DC | Kabelquerschnitte, Sicherungen, Massepunkt |
| ISO 13297 | Elektrische Systeme Kleinfahrzeuge AC | Landstromanschluss, Isolation, Schutzleiter |
| IEC 62619 | Sicherheit Lithium-Sekundärzellen (Industrial) | BMS-Anforderungen, Prüfverfahren |
| ABYC E-11 | DC und AC Elektrik auf Booten (US) | Komplette Elektrik-Norm, referenziert in vielen Marine-Kontexten |
| EN 60950 / 62368 | IT-Geräte Sicherheit (ersetzt durch 62368) | Für Monitoring-Geräte (Cerbo GX, Displays) |
| DIN 41773 | Batterieladetechnik (IU/IUoU/WA) | Deutsche Grundnorm für Ladekennlinien |
| Lloyds Register | Klassifikation Marine-Elektrik | Superyacht-Zulassung (Mastervolt, Fischer Panda) |
| Bureau Veritas (BV) | Klassifikation Marine-Elektrik | Superyacht-Zulassung (Mastervolt, Victron Quattro) |
| DNV (Det Norske Veritas) | Klassifikation Marine-Elektrik | Professionelle Schifffahrt, Superyachten |

### S.4 Wartungsintervalle — Empfehlungen nach Geräteklasse

| Gerät | Intervall | Maßnahme | Dauer |
|-------|-----------|----------|-------|
| Landstrom-Ladegerät | 6 Monate | Lüfter reinigen (Druckluft), Klemmen prüfen | 15 min |
| Landstrom-Ladegerät | 1 Jahr | Ladespannung verifizieren (Multimeter), Firmware-Update | 30 min |
| Landstrom-Ladegerät | 3 Jahre | Elektrolyt-Kondensatoren prüfen (visuell: Auswölbung?) | 30 min |
| MPPT-Solarregler | 6 Monate | Steckverbindungen prüfen, Firmware-Update | 15 min |
| MPPT-Solarregler | 1 Jahr | MPPT-History auswerten (App), Ertrag mit Erwartung vergleichen | 30 min |
| Solarpanels | 3 Monate | Reinigung (Süßwasser + Mikrofasertuch, KEIN Hochdruckreiniger!) | 30 min |
| Solarpanels | 1 Jahr | Stecker/MC4-Verbindungen auf Korrosion prüfen, Kabel auf Scheuerstellen | 45 min |
| Ext. Lichtmaschinenregler | 1 Jahr | Temperatursensor prüfen, Feldstrom-Kabel Festsitz, Keilriemenspannung | 30 min |
| Lichtmaschine | 500h / 1 Jahr | Keilriemen prüfen (Risse, Glasur), Riemenspannung, B+-Kabel | 20 min |
| Lichtmaschine | 2000h / 3 Jahre | Kohlebürsten prüfen (min. 5mm), Lager auf Spiel prüfen | 60 min |
| DC-DC-Wandler | 1 Jahr | Einbauort-Temperatur prüfen, Klemmen, Firmware | 15 min |
| Batteriebank (AGM) | 1 Monat | Ruhespannung, Polklemmen Festsitz, Oberfläche trocken? | 10 min |
| Batteriebank (AGM) | 1 Jahr | Kapazitätstest (C/20), Innenwiderstand messen | 120 min |
| Batteriebank (LiFePO4) | 1 Monat | BMS-Status via App, Zellspannungs-Balance (<50mV Delta) | 5 min |
| Batteriebank (LiFePO4) | 1 Jahr | Full-Cycle (100%→20%→100%) für Kalibrierung SOC + Balancing | 24h passiv |
| Galvanic Isolator | 1 Jahr | Funktionsprüfung (Durchgangsmessung: muss >1.4V sperren) | 10 min |
| Trenntransformator | 2 Jahre | Isolationswiderstand messen (Megger: >100MΩ), Klemmen, Lüfter | 30 min |

### S.5 Typische Installationsfehler und ihre Folgen

| Nr. | Fehler | Folge | Häufigkeit |
|-----|--------|-------|-----------|
| 1 | Temperatursensor auf Kabel statt auf Batteriegehäuse | Falsche Kompensation, Über-/Unterladung | Sehr häufig |
| 2 | Ladegerät an gleicher Sicherung wie großer Verbraucher | Sicherung fällt bei Verbraucher-Start, Ladung unterbricht | Häufig |
| 3 | PV-Module in Serie bei Teilverschattung | 60% Ertragsverlust, MPPT-Oszillation | Häufig |
| 4 | DC-DC-Wandler waagerecht mit Lüfter nach unten montiert | Überhitzung, Derating, verkürzte Lebensdauer | Häufig |
| 5 | Sense-Leitung vergessen (Ladegerät weit von Batterie) | Scheinbar volle Batterie ist nur 80% geladen | Sehr häufig |
| 6 | Sicherung zu groß dimensioniert am Ladegerät-Ausgang | Kabel kann bei Kurzschluss überlastet werden bevor Sicherung fällt | Gelegentlich |
| 7 | Massekabel am Rumpf/Motor statt direkt am Batterie-Minus | Ground Loops, EMV-Probleme, ungenaue Shunt-Messung | Häufig |
| 8 | Egalisierung bei AGM/Gel/LiFePO4 aktiviert gelassen | Gasung (AGM), Trocknung (Gel), Zellzerstörung (LiFePO4) | Gelegentlich |
| 9 | Smart-Alternator-Erkennung nicht konfiguriert am DC-DC | Wandler startet nie (sieht keine 13.2V am Eingang) | Häufig bei Euro-6 |
| 10 | BMS Allow-to-Charge nicht verdrahtet bei LiFePO4 | BMS kann Ladung nicht stoppen, Überladung möglich | Gefährlich! |
| 11 | Windgenerator-Dumpload in geschlossenem Fach | Brandgefahr bei Starkwind + voller Batterie | Selten aber kritisch |
| 12 | Mehrere Ladequellen mit identischer Absorptionsspannung | "Kampf" um Regelhoheit, instabiles System | Häufig |
| 13 | Galvanic Isolator in der N-Leitung statt PE | Kein Korrosionsschutz, Normverstoß | Gelegentlich |
| 14 | PV-Module vor Regler-Anschluss an Batterie anschließen | Überspannung am Regler-Ausgang, möglicher Regler-Schaden | Gelegentlich |
| 15 | Kabelquerschnitt nur nach Ladegerät-Nennstrom, ohne Länge | Spannungsabfall >3%, chronische Unterladung | Sehr häufig |

### S.6 Firmware-Update-Praxis

**Victron (VictronConnect App):**
- Bluetooth-Verbindung zum Gerät herstellen
- App prüft automatisch auf Updates
- Update dauert 2–5 Minuten, Gerät darf NICHT getrennt werden!
- Nach Update: Einstellungen verifizieren (werden in der Regel beibehalten)
- Tipp: Vor Update Screenshot der aktuellen Einstellungen machen

**Wakespeed WS500:**
- Firmware-Update über USB (Mini-USB-Port am Regler)
- Wakespeed Configuration Utility (Windows/Mac)
- Alternative: Bluetooth über WakeConnect App (neuere Firmware)
- Kritisch: Nach Update MÜSSEN Lichtmaschinenparameter neu konfiguriert werden!

**Mastervolt (MasterConnect App):**
- USB oder MasterBus-Verbindung
- Updates über Mastervolt-Website herunterladen
- MasterAdjust Software (PC) für erweiterte Konfiguration

**Morningstar (MSView):**
- MeterBus-Adapter oder RS-232/USB-Adapter
- MSView Software (kostenlos, Windows)
- Updates selten nötig (stabile Firmware, wenig Feature-Updates)

**Generelle Regeln:**
1. Nur updaten, wenn ein konkretes Problem gelöst wird oder neue Funktion benötigt wird
2. "Never change a running system" gilt besonders auf See!
3. Updates IMMER im Hafen durchführen (nie auf See, nie in der Charterwoche)
4. Changelog lesen — manche Updates ändern Default-Werte!
5. Nach jedem Update: 24h-Monitoring der Ladefunktion

### S.7 Victron DVCC — Konfigurationsübersicht

DVCC (Distributed Voltage and Current Control) ist das zentrale Steuerungselement in einem Victron-System mit GX-Gerät (Cerbo GX, Venus GX):

```
┌────────────────────────────────────────────────────────────────────┐
│  DVCC FUNKTIONEN UND EINSTELLUNGEN                                 │
│                                                                    │
│  Voraussetzung: GX-Gerät (Cerbo GX) + VE.Direct/VE.Can Geräte    │
│                                                                    │
│  1. Limit Charge Current (Ladestrom-Begrenzung)                   │
│     - Setzt Maximum-Ladestrom für ALLE Quellen zusammen            │
│     - Wichtig bei LiFePO4: BMS-Limit nicht überschreiten!         │
│     - GX verteilt den erlaubten Strom proportional auf alle Quellen│
│                                                                    │
│  2. Shared Voltage Sense (SVS)                                     │
│     - Ein Spannungs-Sensor (z.B. BMV-712/SmartShunt) wird von     │
│       allen Ladegeräten als Referenz verwendet                     │
│     - Eliminiert Kabelverlust-Probleme bei allen Quellen           │
│     - Alle Geräte laden auf exakt dieselbe Batteriespannung        │
│                                                                    │
│  3. Shared Temperature Sense (STS)                                 │
│     - Ein Temperatursensor für alle Ladegeräte                     │
│     - Einheitliche Temperaturkompensation                          │
│                                                                    │
│  4. BMS-kontrolliertes Laden                                       │
│     - BMS sendet CVL/CCL/DCL über CAN-Bus:                        │
│       CVL = Charge Voltage Limit                                   │
│       CCL = Charge Current Limit                                   │
│       DCL = Discharge Current Limit                                │
│     - Alle Ladequellen respektieren die BMS-Vorgaben              │
│     - Bei "Allow-to-Charge = 0": ALLE Quellen stoppen sofort      │
│                                                                    │
│  5. Wakespeed WS500 Integration                                    │
│     - WS500 an VE.Can-Port des GX anschließen                    │
│     - GX steuert den WS500 wie ein Victron-Ladegerät              │
│     - BMS-Limits gelten auch für Lichtmaschine!                    │
│     - Soft-Ramp-Down bei BMS-Ladestop (kein Lastabwurf!)          │
│                                                                    │
│  Kompatible BMS mit nativem DVCC:                                  │
│     - Victron Smart BMS 12/200                                     │
│     - Victron Lynx Smart BMS                                       │
│     - BYD (via CAN-Bus)                                            │
│     - Pylontech (via CAN-Bus)                                      │
│     - REC BMS (via CAN-Bus)                                        │
│     - MG Energy (via CAN-Bus)                                      │
│     - Freedomwon (via CAN-Bus)                                     │
│     - Viele weitere — siehe Victron Compatibility List             │
└────────────────────────────────────────────────────────────────────┘
```

(Confidence: documented — Victron-Dokumentation, Installationspraxis, Community-Erfahrung)

---

## Schluss-Bemerkung

Diese Wissensdatei deckt das vollständige Spektrum der Ladegeräte und Laderegler im Yachtbau ab — von den elektrochemischen Grundlagen der Batterieladung über detaillierte Produktspezifikationen von 8 Herstellern bis hin zu praxiserprobten Troubleshooting-Bäumen und realen Fallstudien. Die Vergleichstabellen ermöglichen es, für jede Kombination aus Bootsgröße, Batteriechemie und Einsatzgebiet die optimale Ladeinfrastruktur zu identifizieren.

Für die AYDI-Plattform liefert diese Datei strukturierte Daten für die Elektrik-Analyse (Pipeline A), visuelle Erkennung von Ladegeräte-Zuständen (Pipeline B) und Auswertung von Service-Berichten zu Ladeproblemen (Pipeline C). Die Pydantic-v2-Modelle (ChargingSystemAssessment, SolarDimensioningResult, AlternatorAssessment, VisualChargerInspection, ChargerFaultPattern, ParallelChargingAnalysis) sind direkt in den Analyse-Orchestrator integrierbar.

**Wichtigste Erkenntnisse:**
- MPPT ist ab 200Wp Standard — PWM nur noch für Erhaltungsladung gerechtfertigt.
- Externe Lichtmaschinenregler amortisieren sich in 1–2 Saisons durch weniger Motorlaufzeit.
- LiFePO4 erfordert ausnahmslos alle Ladequellen mit LiFePO4-Profil und BMS-Abschaltfähigkeit.
- Galvanische Trennung bei Landstrom ist keine Option, sondern Pflicht für jedes Dauerliegerboot.
- Victron dominiert den europäischen Marine-Markt durch das stärkste Ökosystem (VE.Direct/VE.Can/VRM/DVCC).

---

*Ende der Wissensdatei 22.04 — Ladegeräte und Laderegler*
