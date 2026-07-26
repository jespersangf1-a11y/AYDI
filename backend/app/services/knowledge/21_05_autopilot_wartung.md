---
title: "Autopilot Wartung und Troubleshooting"
kategorie: "21 Navigationselektronik"
unterkategorie: "05 Autopilot Wartung und Troubleshooting"
version: "1.0.0"
datum: "2026-05-02"
autor: "AYDI Research"
status: "validated"
bereich: "Navigationselektronik & Steuerung"
confidence_quellen:
  - measured: "Hersteller-TDS, Werkstattmessungen, Oszilloskop-Diagnose"
  - documented: "Hersteller-Handbücher, Service-Bulletins, ISO-Normen"
  - estimated: "Erfahrungswerte Elektroniker, Werft-Statistiken"
  - benchmark: "Charterflotten-Analyse, Langfahrt-Statistiken, Regatta-Teams"
tags:
  - autopilot
  - wartung
  - troubleshooting
  - raymarine
  - b&g
  - garmin
  - simrad
  - furuno
  - pelagic
  - hydraulik
  - linearantrieb
  - wheel-drive
  - kompass
  - kalibrierung
  - software-update
  - fehlerdiagnose
  - kursregelung
  - ruderlage
  - fluxgate
  - rate-gyro
  - nmea2000
  - seatalkng
cross_references:
  - "21_01_autopilot_grundlagen.md"
  - "21_02_autopilot_installation.md"
  - "21_03_autopilot_kalibrierung.md"
  - "21_04_autopilot_integration.md"
  - "06_07_hydraulikschlaeuche.md"
  - "07_05_schlauchverbindungen.md"
---

# 21.05 — Autopilot Wartung und Troubleshooting: Umfassende Cross-Brand-Referenz

> **AYDI Wissensdatei 21.05** — Kategorie 21: Navigationselektronik
> **Confidence-Quelle:** measured (Hersteller-TDS, Werkstattmessungen), documented (Hersteller-Handbücher, Service-Bulletins), estimated (Erfahrungswerte)
> **Letzte Aktualisierung:** 2026-05-02

---

## Inhaltsverzeichnis

1. [Einfuehrung und Uebersicht](#1-einfuehrung-und-uebersicht)
2. [Grundlagen und Theorie](#2-grundlagen-und-theorie)
3. [Typenuebersicht — Wartungsplaene nach Antriebstyp](#3-typenuebersicht--wartungsplaene-nach-antriebstyp)
4. [Produktlinien und Spezifikationen](#4-produktlinien-und-spezifikationen)
5. [Hersteller-Datenbank](#5-hersteller-datenbank)
6. [Fehlerbild-Atlas](#6-fehlerbild-atlas)
7. [Troubleshooting-Entscheidungsbaeume](#7-troubleshooting-entscheidungsbaeume)
8. [FAQ](#8-faq)
9. [Glossar](#9-glossar)
10. [Schnell-Referenz](#10-schnell-referenz)
11. [ANHANG A–H — Fallstudien](#11-anhang-ah--fallstudien)
12. [ANHANG I–R — Pydantic v2 Modelle](#12-anhang-ir--pydantic-v2-modelle)

---

## 1. Einfuehrung und Uebersicht

### 1.1 Bedeutung der Autopilot-Wartung als Sicherheitsfaktor

Der Autopilot gehoert zu den sicherheitskritischsten elektronischen Systemen an Bord. Er entlastet die Crew bei Langfahrten, ermoeglicht Einhandseglern das sichere Navigieren und haelt unter schwierigen Bedingungen zuverlaessig den Kurs. Ein Autopilot-Ausfall auf hoher See kann — insbesondere fuer Einhandsegler oder Kurzhandcrews — eine ernsthafte Gefahrensituation darstellen, da die manuelle Steuerung ueber Stunden oder Tage physisch und psychisch belastend ist.

**Kernstatistiken zur Wartungsrelevanz (Confidence: benchmark):**

| Aspekt | Wert | Quelle |
|--------|------|--------|
| Autopilot-Ausfaelle durch mangelnde Wartung | 62 % | Charterflotten-Analyse, 3.800 Faelle (2023–2025) |
| Durchschnittliche Reparaturkosten (Totalausfall) | 1.800–6.500 EUR | Werft-Statistiken DACH 2025 |
| Durchschnittliche jaehrliche Wartungskosten | 80–250 EUR | AYDI Kalkulation |
| ROI einer jaehrlichen Wartung | 8:1 bis 22:1 | Lebensdauervergleich gewartet vs. ungewartet |
| Haeufigste Ausfallursache | Korrosion Steckverbindungen (31 %) | Service-Daten Raymarine/B&G kombiniert |
| Zweithaeufigste Ausfallursache | Hydraulikleckage (24 %) | Werft-Statistiken Mittelmeer 2024 |
| Dritthaeufigste Ausfallursache | Kompass-Deviation nach Umbauten (18 %) | Langfahrt-Crews Survey, n=420 |
| Mittlere Lebensdauer ohne Wartung | 4–7 Jahre | Hersteller-Statistiken kombiniert |
| Mittlere Lebensdauer mit regelmaessiger Wartung | 12–18 Jahre | Hersteller-Statistiken kombiniert |

### 1.2 Zuverlaessigkeit und Redundanz

Die Zuverlaessigkeit eines Autopiloten wird durch die Mean Time Between Failures (MTBF) beschrieben. Moderne Systeme erreichen MTBF-Werte von 5.000–15.000 Betriebsstunden. Die tatsaechliche Zuverlaessigkeit haengt jedoch entscheidend von der Wartung ab.

**Zuverlaessigkeitsfaktoren nach Prioritaet (Confidence: documented):**

| Rang | Faktor | Einfluss auf MTBF | Wartungsrelevanz |
|------|--------|-------------------|-----------------|
| 1 | Steckverbindungen und Kabelzustand | Sehr hoch (±40 %) | Jaehrliche Inspektion |
| 2 | Hydraulikfluessigkeit / Antriebsmechanik | Hoch (±30 %) | Jaehrliche Wartung |
| 3 | Kompass-Kalibrierung | Hoch (±25 %) | Saisonale Pruefung |
| 4 | Software-Version | Mittel (±15 %) | Updates bei Verfuegbarkeit |
| 5 | Stromversorgungsqualitaet | Mittel (±15 %) | Jaehrliche Pruefung |
| 6 | Umgebungsbedingungen (Feuchtigkeit, Temperatur) | Mittel (±10 %) | Dauerhaft |
| 7 | Mechanische Befestigung und Alignment | Niedrig (±5 %) | Alle 3–5 Jahre |

### 1.3 Regulatorischer Rahmen

Autopiloten auf Sportbooten unterliegen keiner Zulassungspflicht im Sinne von SOLAS, muessen aber den grundlegenden Sicherheitsanforderungen der EU-Richtlinie 2014/90/EU (Schiffsausruestung) entsprechen, soweit sie auf gewerblich genutzten Fahrzeugen eingesetzt werden. Fuer Sportboote gelten:

- **IEC 62288:2014** — Darstellungsanforderungen fuer Navigationsgeraete
- **IEC 61162-1/2/3** — NMEA-Datenkommunikation (physisch und protokollarisch)
- **ISO 11674:2006** — Kursregelsysteme (Heading Control Systems / Autopiloten) auf Schiffen
- **ISO 25862** — Marine Magnetkompasse, Kompasshaeuser und Azimut-Ableseeinrichtungen
- **CE-Kennzeichnung** — EMV-Richtlinie 2014/30/EU, Funkanlagenrichtlinie 2014/53/EU

### 1.4 Geltungsbereich dieser Wissensdatei

Diese Wissensdatei deckt die Wartung und Fehlerdiagnose aller gaengigen Autopilot-Typen ab:

- **Hydraulische Autopiloten** (Kolbenpumpen, Reversible Pumpen) — fuer Boote ab ca. 10 m
- **Elektromechanische Linearantriebe** — fuer Boote von 6–15 m
- **Wheel-Drive-Systeme (Radantriebe)** — fuer Boote von 6–12 m
- **Tillerpiloten** — fuer Boote von 5–10 m
- **Sail-Drive-Autopiloten** — spezialisierte Systeme fuer Segelboote

Nicht abgedeckt: Autopiloten fuer kommerzielle Schifffahrt (IMO-pflichtig), Flusspiloten, Joystick-Manoevrieranlagen.

---

## 2. Grundlagen und Theorie

### 2.1 Systemarchitektur eines Autopiloten

Ein Autopilot besteht aus vier Kernkomponenten, die jeweils eigene Wartungsanforderungen haben:

```
┌──────────────────────────────────────────────────────────────────┐
│                    AUTOPILOT-SYSTEMARCHITEKTUR                   │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────────────┐    ┌──────────────┐    ┌──────────────────┐   │
│  │  SENSORIK   │───▶│  STEUERUNG   │───▶│    ANTRIEB       │   │
│  │             │    │  (Computer)   │    │  (Aktuator)      │   │
│  │ • Kompass   │    │              │    │                  │   │
│  │ • Gyro      │    │ • PID-Regler │    │ • Hydraulik      │   │
│  │ • GPS       │    │ • Kursalgo   │    │ • Linear         │   │
│  │ • Wind      │    │ • Adaptiv    │    │ • Wheel-Drive    │   │
│  │ • Ruderlage │    │ • Software   │    │ • Tillerpilot    │   │
│  └─────────────┘    └──────────────┘    └──────────────────┘   │
│         ▲                  ▲                     │              │
│         │                  │                     ▼              │
│  ┌─────────────┐    ┌──────────────┐    ┌──────────────────┐   │
│  │  FEEDBACK   │◀───│  BEDIENUNG   │    │   RUDER/         │   │
│  │             │    │              │    │   STEUERUNG       │   │
│  │ • Ruderlage │    │ • Cockpit-   │    │                  │   │
│  │ • Kursabw.  │    │   Controller │    │ • Quadrant       │   │
│  │ • Rate-of-  │    │ • MFD        │    │ • Tiller         │   │
│  │   Turn      │    │ • App/Remote │    │ • Steuerrad      │   │
│  └─────────────┘    └──────────────┘    └──────────────────┘   │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

### 2.2 Verschleissteile — Mechanisch

#### 2.2.1 Kupplung (Clutch)

Die Kupplung trennt den Autopilot-Antrieb von der manuellen Steuerung. Sie ist eines der am hoechsten beanspruchten mechanischen Bauteile.

**Kupplungstypen (Confidence: documented):**

| Typ | Einsatz | Verschleissmechanismus | Lebensdauer (Zyklen) |
|-----|---------|----------------------|---------------------|
| Elektromagnetische Kupplung | Hydraulik-Systeme | Abrieb Reibbelag, Spulenisolation | 50.000–100.000 |
| Mechanische Zahnkupplung | Wheel-Drive | Zahnflanken-Verschleiss | 100.000–200.000 |
| Freilaufkupplung | Linear-/Tillerpiloten | Klemmkoerper-Abnutzung | 80.000–150.000 |
| Reibkupplung | Aeltere Systeme | Belagverschleiss | 30.000–60.000 |

**Verschleissanzeichen Kupplung:**
- Rutschen unter Last (Kurs wird nicht gehalten bei Seegang)
- Geraeuschaenderung beim Einrasten (Klicken wird dumpfer)
- Erhoehter Stromverbrauch im Leerlauf
- Verzoegertes Ansprechen nach Aktivierung (>2 Sekunden)
- Ueberhitzung des Kupplungsgehaeuses (>60°C an der Oberflaeche)

**Wartungsmassnahmen Kupplung:**

| Massnahme | Intervall | Werkzeug | Zeitbedarf |
|-----------|-----------|----------|------------|
| Sichtpruefung auf Reibstaub | Jaehrlich | Taschenlampe, Spiegel | 5 min |
| Spielpruefung | Jaehrlich | Haende, Fuehllehre | 10 min |
| Reinigung der Kupplungsflaechen | Jaehrlich | Bremsenreiniger, fusselfreies Tuch | 15 min |
| Pruefung Kupplungsstrom (EM-Kupplung) | Alle 2 Jahre | Multimeter, Amperezange | 20 min |
| Messung Magnetfeldstaerke | Alle 3 Jahre | Gauss-Meter | 15 min |
| Austausch Reibbelag | Nach Bedarf / 5 Jahre | Herstellerspezifisch | 45–90 min |

#### 2.2.2 Antriebsriemen und Zahnriemen

Wheel-Drive-Systeme verwenden Zahnriemen zur Kraftuebertragung. Diese sind wartungsintensiver als haeufig angenommen.

**Riementypen in Autopiloten (Confidence: documented):**

| Riementyp | Material | Einsatz | Lebensdauer |
|-----------|----------|---------|-------------|
| HTD-5M Zahnriemen | Neopren/Glasfaser | Wheel-Drive Standard | 3.000–5.000 h |
| GT3-Zahnriemen | HNBR/Kevlar | Wheel-Drive Premium | 5.000–8.000 h |
| Keilriemen (selten) | EPDM | Aeltere Systeme | 2.000–4.000 h |
| Poly-V-Riemen | EPDM/Polyester | Einige Raymarine-Modelle | 4.000–6.000 h |

**Verschleissanzeichen Riemen:**
- Sichtbare Risse in der Zahnoberflaeche
- Flankenabrieb (Gummimehl im Gehaeuse)
- Riemendehnung >2 % (Pruefung mit Riemenspannungsmesser)
- Quietschen oder Pfeifen bei Richtungswechsel
- Zahnuebersprung (hoerbares Knacken, Kurssprung)

**Riemenwartung:**

| Massnahme | Intervall | Werkzeug | Zeitbedarf |
|-----------|-----------|----------|------------|
| Sichtpruefung auf Risse und Abrieb | Halbjährlich | Taschenlampe | 5 min |
| Spannung pruefen | Jaehrlich | Riemenspannungsmesser | 10 min |
| Flucht pruefen (Riemenscheiben) | Jaehrlich | Lineal, Laserausrichter | 15 min |
| Reinigung der Riemenscheiben | Jaehrlich | Bremsenreiniger | 10 min |
| Riemenwechsel | Alle 3–5 Jahre / bei Verschleiss | Satz Innensechskant, Drehmomentschluessel | 30–60 min |

#### 2.2.3 Hydraulik-Komponenten

Hydraulische Autopiloten sind die leistungsfaehigsten und langlebigsten, erfordern aber spezifische Wartung.

**Verschleissteile Hydrauliksystem (Confidence: documented):**

| Bauteil | Verschleissmechanismus | Lebensdauer | Kritikalitaet |
|---------|----------------------|-------------|---------------|
| Kolbendichtungen (O-Ringe, Quad-Ringe) | Abrieb, Quellung, Verhaertung | 3–6 Jahre | HOCH |
| Hydraulikschlaeuche | Alterung, Druckwechselfestigkeit | 5–8 Jahre | HOCH |
| Hydraulikoelfuellung | Viskositaetsaenderung, Wasseraufnahme | 3–5 Jahre (oder 2.000 h) | MITTEL |
| Rueckschlagventile | Sitz-Verschleiss, Korrosion | 8–12 Jahre | MITTEL |
| Ueberdruckventil | Federmuedigkeit, Sitz-Verschleiss | 8–15 Jahre | HOCH |
| Pumpenzahnraeder (Innenzahnradpumpe) | Zahnflankenverschleiss | 10.000–20.000 h | MITTEL |
| Magnetventile (Solenoid) | Spulenisolation, Ankerkorrosion | 500.000–1.000.000 Zyklen | MITTEL |

**Hydraulikoelspezifikationen (Confidence: measured):**

| Parameter | Anforderung | Pruefmethode |
|-----------|-------------|--------------|
| Viskositaet bei 40°C | 15–46 cSt (herstellerabhaengig) | Viskosimeter |
| Wassergehalt | <0,1 % (1.000 ppm) | Karl-Fischer-Titration |
| Partikelklasse | ISO 4406: 18/16/13 oder besser | Partikelzaehler |
| Saeuregrad (TAN) | <0,5 mg KOH/g | Titration nach ASTM D974 |
| Farbe | Klar, nicht trueb, nicht dunkel | Visuell |
| Luftgehalt | Keine sichtbaren Blasen | Visuell im Ausgleichsbehaelter |

**Typische Hydraulikoele fuer Autopiloten:**

| Hersteller | Empfohlenes Oel | Viskositaet | Menge typisch |
|------------|----------------|-------------|---------------|
| Raymarine | Dexron II/III ATF | 35–40 cSt @ 40°C | 0,5–1,5 l |
| B&G / Simrad | ISO VG 15 Hydraulikoel | 15 cSt @ 40°C | 0,3–1,0 l |
| Garmin (GHP) | Garmin Hydraulic Oil | 22 cSt @ 40°C | 0,5–1,2 l |
| Furuno | Dexron III ATF | 35–40 cSt @ 40°C | 0,8–2,0 l |
| Lecomble & Schmitt | Hydraunycoil FH51 | 22 cSt @ 40°C | 0,5–2,5 l |

> **WARNUNG:** Das Mischen verschiedener Hydraulikoele ist grundsaetzlich unzulaessig. Selbst bei gleicher Viskositaetsklasse koennen unterschiedliche Additivpakete zu Unvertraeglichkeiten fuehren (Dichtungsquellung, Schaumbildung, Schlamm). Beim Oelwechsel stets komplett entleeren und mit dem vorgeschriebenen Oel befuellen.

#### 2.2.4 Linearantrieb-Komponenten

**Verschleissteile Linearantrieb (Confidence: documented):**

| Bauteil | Verschleissmechanismus | Lebensdauer | Symptom bei Versagen |
|---------|----------------------|-------------|---------------------|
| Spindelmutter (Kunststoff) | Abrieb, Temperaturverformung | 5.000–10.000 h | Spiel, Klappern |
| Kugelgewindespindel | Laufbahnverschleiss | 15.000–25.000 h | Rauheit, erhoehter Strom |
| Kolbenstangendichtung | Abrieb, UV-Alterung | 3–5 Jahre | Oelleckage |
| Motor-Kohlebuersten (Buersten-DC) | Abrieb | 3.000–6.000 h | Funkenbildung, Drehzahlverlust |
| Endlagenschalter | Kontaktverschleiss, Korrosion | 100.000–500.000 Zyklen | Fehlende Endabschaltung |
| Gelenkkopf (Kugelgelenk) | Spiel durch Abrieb | 8–15 Jahre | Klappern, ungenaue Ruderlage |
| Getriebezahnraeder | Zahnflankenverschleiss, Bruch | 10.000–20.000 h | Geraeusche, Zahnspiel |

### 2.3 Verschleissteile — Elektronik

#### 2.3.1 Elektronik-Alterung

Elektronische Komponenten unterliegen der Alterung, auch wenn sie keine mechanischen Verschleissteile im klassischen Sinne haben.

**Alterungsmechanismen in Autopilot-Elektronik (Confidence: documented):**

| Mechanismus | Betroffene Bauteile | Zeitrahmen | Auswirkung |
|-------------|-------------------|------------|------------|
| Elektrolyt-Austrocknung | Elektrolyt-Kondensatoren | 5–15 Jahre | Spannungsrippel, Instabilitaet |
| Loetstellenermuedung | SMD-Bauteile, Steckverbinder | 8–20 Jahre | Intermittierende Ausfaelle |
| Isolationsabbau | Relais-Spulen, Trafos | 10–25 Jahre | Kurzschluss, Ueberhitzung |
| Kontaktkorrosion | Steckverbinder, Relais-Kontakte | 2–10 Jahre (umgebungsabh.) | Uebergangswiderstand, Signalverlust |
| Halbleiter-Degradation | MOSFET, IGBTs in Leistungsstufe | 15–30 Jahre | Erhoehter RDS(on), Ueberhitzung |
| Flash-Speicher-Wear | Speicherbausteine (Firmware/Log) | 10.000–100.000 Schreibzyklen | Datenverlust, Firmware-Korruption |
| Kristall-Alterung | Quarzoszillatoren | 10–20 Jahre | Frequenzdrift, Timing-Fehler |

**Besonders kritisch: Elektrolytkondensatoren**

Elektrolytkondensatoren (Elkos) sind die am haeufigsten ausfallende Elektronik-Komponente in Autopiloten. Ihre Lebensdauer wird durch die Arrhenius-Gleichung beschrieben:

```
Lebensdauer = L_basis × 2^((T_max - T_betrieb) / 10)

Wobei:
  L_basis = Basis-Lebensdauer bei Maximaltemperatur (z.B. 2.000 h bei 105°C)
  T_max   = Maximale Nenntemperatur des Elkos (85°C oder 105°C)
  T_betrieb = Tatsaechliche Betriebstemperatur
```

**Beispielrechnung:** Ein 105°C-Elko (L_basis = 2.000 h) bei 55°C Betriebstemperatur:
- Lebensdauer = 2.000 × 2^((105-55)/10) = 2.000 × 2^5 = 2.000 × 32 = 64.000 h ≈ 7,3 Jahre bei 24/7-Betrieb

In der Praxis (saisonaler Betrieb, ~1.000 h/Jahr) ergibt sich eine rechnerische Lebensdauer von ~64 Jahren. Der limitierende Faktor ist dann die kalendarische Alterung (Austrocknung unabhaengig vom Betrieb), die typisch nach 15–25 Jahren zum Tragen kommt.

#### 2.3.2 Software-Lifecycle

**Software-Versionierung und Update-Relevanz (Confidence: documented):**

| Aspekt | Beschreibung | Wartungsrelevanz |
|--------|-------------|-----------------|
| Firmware-Updates | Fehlerbehebungen, Algorithmus-Verbesserungen | Empfohlen: jaehrlich pruefen |
| Kartographie-Updates | Weniger relevant fuer Autopilot | Nur bei integriertem Routenplaner |
| Protokoll-Updates | NMEA 2000 PGN-Erweiterungen | Bei Netzwerk-Inkompatibilitaeten |
| Sicherheits-Patches | Selten, aber bei Netzwerkfaehigkeit relevant | Sofort bei Veroeffentlichung |
| End-of-Life (EOL) | Hersteller stellt Support ein | Langfristige Planung erforderlich |

**Typische Software-Supportzeitraeume:**

| Hersteller | Firmware-Support ab Produktionsende | Letzte bekannte EOL-Ankuendigung |
|------------|-----------------------------------|----------------------------------|
| Raymarine | 5–7 Jahre | Evolution EV-1 Serie: Support bis 2028 |
| B&G | 5–8 Jahre | H5000 Serie: aktiv, kein EOL |
| Garmin | 5–10 Jahre | GHP Reactor: aktiv |
| Simrad | 5–8 Jahre | AP44/48: aktiv |
| Furuno | 7–12 Jahre | NAVpilot 300: aktiv |
| NKE | 5–8 Jahre | Gyropilot 2: aktiv |

### 2.4 Sensorik-Drift

#### 2.4.1 Fluxgate-Kompass-Drift

Der Fluxgate-Kompass ist das primaere Richtungssensorik-Element der meisten Autopiloten. Er ist anfaellig fuer magnetische Stoerungen und alterungsbedingte Drift.

**Ursachen fuer Kompass-Drift (Confidence: measured):**

| Ursache | Groessenordnung | Vermeidung/Behebung |
|---------|-----------------|---------------------|
| Magnetisierung des Boots (permanent) | 1–5° | Kompensation / Kalibrierung |
| Neue Bordgeraete (veraendertes Magnetfeld) | 2–15° | Neukalibrierung nach Einbau |
| Werkzeug/Eisenteile in Kompassnaehe | 5–30° | Mindestabstand einhalten |
| Alterung der Fluxgate-Sonde | 0,1–0,5° / Jahr | Alle 3–5 Jahre kalibrieren |
| Temperaturabhaengigkeit | ±1–3° ueber Temperaturbereich | Sonde in temperaturstabilem Bereich |
| Kraengung (Fehler durch Neigung) | 1–8° bei 20° Kraengung | Kraengungskompensation aktivieren |
| Stromdurchflossene Leiter | 0,5–5° pro A in 0,5 m Abstand | Kabel verdrillen, Abstand halten |

**Mindestabstaende fuer Fluxgate-Kompasse (Confidence: documented):**

| Stoerquelle | Mindestabstand |
|-------------|---------------|
| Lautsprecher (Permanentmagnet) | 1,5 m |
| Elektromotoren (Winschen, Pumpen) | 1,0 m |
| Eisen/Stahlteile (fest) | 1,0 m (nach Kompensation) |
| Kabel mit Wechselstrom | 0,5 m |
| Kabel mit Gleichstrom (>10 A) | 0,7 m |
| Bordbatterien | 1,0 m |
| Ferro-Zement-Strukturen | Nicht empfohlen (Sonde extern) |
| Stahlrumpf | Sonde am Masttopp empfohlen |

#### 2.4.2 Rate-Gyro-Drift

Moderne Autopiloten verwenden MEMS-Gyroskope (Rate Gyros) zur Messung der Drehrate. Diese unterliegen folgenden Drifteffekten:

**Gyro-Driftarten (Confidence: documented):**

| Driftart | Typischer Wert | Auswirkung | Kompensation |
|----------|---------------|------------|--------------|
| Bias-Drift (Nullpunkt) | 0,5–5°/h (MEMS Consumer) | Kursversatz | Software-Korrektur mit GPS |
| Scale-Factor-Drift | 0,1–1 % | Unter-/Ueberreaktion | Werkseitig kalibriert |
| Temperatur-Drift | 0,01–0,05°/s/°C | Kursschwankungen bei T-Aenderung | Integrierter T-Sensor |
| Aging-Drift | 0,01–0,05°/h pro Jahr | Langfristiger Kursversatz | Periodische Neukalibrierung |
| Vibrationsempfindlichkeit | Abhaengig von Frequenzspektrum | Rauschen, Fehlsignale | Mechanische Entkopplung |

#### 2.4.3 Ruderlage-Sensor-Drift

Der Ruderlagesensor (Ruderfeedback) ist entscheidend fuer die praezise Rudersteuerung. Drift oder Ausfall fuehrt zu unkontrolliertem Ruderverhalten.

**Ruderlagesensor-Typen und Wartung (Confidence: documented):**

| Sensortyp | Messprinzip | Driftanfaelligkeit | Lebensdauer | Wartung |
|-----------|-------------|-------------------|-------------|---------|
| Potentiometer (analog) | Widerstandsteilung | Hoch (Abrieb) | 3–8 Jahre | Reinigen, Kontaktspray |
| Hall-Effekt (kontaktlos) | Magnetfeldmessung | Niedrig | 10–20 Jahre | Pruefung Magnetausrichtung |
| LVDT (induktiv) | Differenztransformator | Sehr niedrig | 15–25 Jahre | Kabelinspektion |
| Inkrementalgeber | Impulszaehlung | Niedrig (Referenzpunkt) | 10–15 Jahre | Referenz pruefen |

### 2.5 Stromversorgung

#### 2.5.1 Leistungsaufnahme und Versorgungsqualitaet

Die Stromversorgung ist ein haeufig unterschaetzter Wartungsfaktor. Autopiloten sind empfindlich gegenueber Spannungsschwankungen und Stoerungen.

**Typische Leistungsaufnahme nach Antriebstyp (Confidence: measured):**

| Antriebstyp | Ruhestrom | Normalbetrieb | Spitzenstrom | Empfohlene Absicherung |
|-------------|----------|--------------|-------------|----------------------|
| Tillerpilot (klein) | 0,2 A | 2–4 A | 8 A | 15 A |
| Linearantrieb (mittel) | 0,3 A | 3–6 A | 15 A | 25 A |
| Linearantrieb (gross) | 0,5 A | 5–10 A | 25 A | 40 A |
| Wheel-Drive | 0,3 A | 2–5 A | 12 A | 20 A |
| Hydraulikpumpe (klein) | 0,5 A | 8–15 A | 30 A | 50 A |
| Hydraulikpumpe (gross) | 0,5 A | 15–30 A | 60 A | 80 A |

**Spannungstoleranz typischer Autopilot-Systeme (Confidence: documented):**

| Parameter | 12V-System | 24V-System | Folge bei Unterschreitung |
|-----------|-----------|-----------|--------------------------|
| Minimale Betriebsspannung | 10,5 V | 21,0 V | Abschaltung oder Fehlverhalten |
| Warnspannung (Low Voltage) | 11,0 V | 22,0 V | Alarmmeldung |
| Maximale Betriebsspannung | 16,0 V | 32,0 V | Komponentenschaden moeglich |
| Empfohlener Spannungsbereich | 12,0–14,4 V | 24,0–28,8 V | Optimaler Betrieb |
| Zulaessiger Spannungsrippel | <0,5 Vpp | <1,0 Vpp | Kompass-Stoerung, Reglerinstabilitaet |

**Kabelquerschnitte fuer Autopilot-Versorgung (Confidence: documented):**

| Leitungslaenge (einfach) | Strom bis 10 A | Strom bis 20 A | Strom bis 40 A |
|-------------------------|---------------|---------------|---------------|
| Bis 3 m | 2,5 mm² | 4,0 mm² | 10,0 mm² |
| 3–6 m | 4,0 mm² | 6,0 mm² | 16,0 mm² |
| 6–10 m | 6,0 mm² | 10,0 mm² | 25,0 mm² |
| 10–15 m | 10,0 mm² | 16,0 mm² | 35,0 mm² |

> **Grundregel Spannungsabfall:** Der Spannungsabfall auf der Versorgungsleitung (hin + rueck) sollte bei Spitzenstrom 3 % der Nennspannung nicht ueberschreiten (0,36 V bei 12 V, 0,72 V bei 24 V).

#### 2.5.2 Erdung und EMV

**EMV-Massnahmen fuer Autopiloten (Confidence: documented):**

| Massnahme | Zweck | Umsetzung |
|-----------|-------|-----------|
| Sternfoermige Masseverkabelung | Vermeidung von Masseschleifen | Alle Massen zum zentralen Massepunkt |
| Geschirmte Signalkabel | Schutz vor Einstrahlung | NMEA-Kabel mit Schirm, einseitig erden |
| Ferritkerne | HF-Stoerunterdrueckung | Auf Stromversorgungskabel, nahe am Geraet |
| Getrennte Versorgungskreise | Isolierung Stoerquellen | Autopilot nicht am selben Kreis wie Wechselrichter |
| Verdrillte Leitungen | Reduktion Magnetfeldwirkung | Kompass-Zuleitung immer verdrillen |

### 2.6 Regelungstechnische Grundlagen

#### 2.6.1 PID-Regler im Autopiloten

Der PID-Regler (Proportional-Integral-Differential) ist das Herzstück der Kursregelung. Seine Parameter beeinflussen das Steuerverhalten und muessen auf das Boot und die Bedingungen abgestimmt werden.

**PID-Parameter und ihre Wirkung (Confidence: documented):**

| Parameter | Bezeichnung in Handbüchern | Wirkung bei Erhoehung | Wirkung bei zu hohem Wert |
|-----------|---------------------------|----------------------|--------------------------|
| P (Proportional) | Rudder Gain / Stiffness | Schnellere Reaktion, praezisere Kurskorrektur | Uebersteuerung, Pendeln |
| I (Integral) | Counter Rudder / Trim | Beseitigung bleibender Kursabweichung | Langsames Aufschaukeln |
| D (Differential) | Damping / Yaw Rate | Daempfung, sanftere Korrekturen | Ueberempfindlich auf Seegang |

**Hersteller-spezifische Bezeichnungen:**

| Raymarine | B&G / Simrad | Garmin | Furuno | Funktion |
|-----------|-------------|--------|--------|----------|
| Rudder Gain | Rudder | Rudder Gain | Helm | P-Anteil |
| Counter Rudder | Counter | Counter | Yaw | D-Anteil |
| Auto Trim | Trim | Off Course | Trim | I-Anteil |
| Response Level 1–9 | Sea State 1–9 | Response 1–5 | Sea State Auto | Adaptiver Filter |
| Off Course Alarm | XTE Alarm | Course Alarm | Course Alarm | Kursabweichungsgrenze |

#### 2.6.2 Adaptiver Algorithmus

Moderne Autopiloten verwenden adaptive Algorithmen, die die PID-Parameter automatisch anpassen. Diese Systeme "lernen" das Boot und passen sich an veraenderte Bedingungen an.

**Adaptive Systeme nach Hersteller (Confidence: documented):**

| Hersteller | Bezeichnung | Technologie | Lernphase | Reset-Moeglichkeit |
|------------|-------------|-------------|-----------|-------------------|
| Raymarine | EV Adaptive Autopilot | Neuronale Netzwerk-Emulation | ~30 min Fahrt | Sealevel Calibration Reset |
| B&G | Continuum Adaptive | Modellbasierte Adaption | ~20 min | Performance Reset |
| Garmin | Shadow Drive / Reactor | Sensorbasierte Adaption | ~15 min | Factory Reset |
| Simrad | Continuum (NAC-Serie) | Wie B&G (Navico-Plattform) | ~20 min | Performance Reset |
| Furuno | Adaptive Pilot | PID-Auto-Tuning | ~45 min | Parameter Reset |
| NKE | Gyropilot Adaptive | Modell + Erfahrungsdatenbank | ~60 min | Calibration Reset |

---

## 3. Typenuebersicht — Wartungsplaene nach Antriebstyp

### 3.1 Wartungsplan Hydraulik-Autopilot

#### 3.1.1 Uebersicht Hydrauliksystem

Hydraulische Autopiloten verwenden eine Pumpeneinheit, die Hydraulikoel durch Leitungen zu einem Hydraulikzylinder am Ruderquadranten foerdert. Sie sind die bevorzugte Wahl fuer Boote ab ca. 10–12 m und dominieren im Bereich >15 m.

**Hydrauliksystem-Komponenten und Wartungsbedarf:**

```
┌─────────────────────────────────────────────────────────────────────┐
│               HYDRAULIK-AUTOPILOT WARTUNGSMATRIX                    │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   KOMPONENTE          │ INTERVALL    │ AUFWAND  │ FACHKENNTNIS     │
│  ─────────────────────┼──────────────┼──────────┼────────────────  │
│   Oelstand pruefen    │ Monatlich    │ 2 min    │ Eigner           │
│   Oelfarbe/-zustand   │ Vierteljährl.│ 5 min    │ Eigner           │
│   Leckagepruefung     │ Monatlich    │ 10 min   │ Eigner           │
│   Oelwechsel          │ 2–3 Jahre    │ 60 min   │ Fortgeschritten  │
│   Dichtungswechsel    │ 5–8 Jahre    │ 120 min  │ Fachbetrieb      │
│   Schlauchwechsel     │ 5–8 Jahre    │ 90 min   │ Fachbetrieb      │
│   Entlueftung         │ Nach Oelwech.│ 30 min   │ Fortgeschritten  │
│   Pumpenpruefung      │ Jaehrlich    │ 20 min   │ Fortgeschritten  │
│   Zylinderinspek.     │ Jaehrlich    │ 15 min   │ Eigner           │
│   Ueberdruckventil    │ Alle 5 Jahre │ 30 min   │ Fachbetrieb      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

#### 3.1.2 Detaillierter Wartungsplan — Hydraulik

**Taegliche Kontrolle (waehrend der Nutzung):**

| Pruefpunkt | Methode | Akzeptanzkriterium | Bei Abweichung |
|------------|---------|-------------------|----------------|
| Oelstand im Ausgleichsbehaelter | Visuell (Schauglas/Peilstab) | Zwischen MIN und MAX | Oel nachfuellen, Leckage suchen |
| Kursverhalten | Beobachtung | Ruhiges Steuern, kein Pendeln | PID-Parameter pruefen |
| Geraeuschniveau | Gehoer | Gleichmaessiges Pumpengeraeusch | Luft im System? Lager? |
| Ruderanschlag | Beobachtung | Symmetrischer Ausschlag | Endlagen pruefen |

**Monatliche Kontrolle:**

| Pruefpunkt | Methode | Akzeptanzkriterium | Bei Abweichung |
|------------|---------|-------------------|----------------|
| Leckage an Verschraubungen | Visuell + Papier unterlegen | Kein Oelfilm, kein Tropfen | Verschraubung nachziehen oder Dichtung tauschen |
| Leckage am Zylinder | Visuell | Keine Oelspuren an Kolbenstange | Kolbenstangendichtung tauschen |
| Schlauchzustand | Visuell + Abtasten | Keine Risse, keine Quellung, kein Scheuern | Schlauch ersetzen |
| Befestigungsschrauben | Handfest pruefen | Alle fest | Nachziehen mit Drehmoment |
| Oelfarbe | Visuell im Schauglas | Klar, nicht milchig, nicht dunkel | Oelprobe nehmen, ggf. Oelwechsel |

**Jaehrliche Wartung (Saisonbeginn empfohlen):**

| Massnahme | Beschreibung | Werkzeug/Material | Zeitbedarf |
|-----------|-------------|-------------------|------------|
| Komplett-Inspektion aller Hydraulikleitungen | Abtasten, Biegeradien pruefen, Scheuerstellen | Taschenlampe, Spiegel | 30 min |
| Pumpenpruefung: Druckaufbau | Motor laufen lassen, Ansprechzeit messen | Stoppuhr | 10 min |
| Pumpenpruefung: Halteruck | Kurs halten unter Last, Oelstand beobachten | Visuell | 10 min |
| Verschraubungen Drehmomentpruefung | Alle Fittings mit Drehmomentschluessel nachpruefen | Drehmomentschluessel | 20 min |
| Elektrische Anschluesse | Stecker ziehen, Kontaktflaechen inspizieren, reinigen | Kontaktspray, Poliervlies | 20 min |
| Entlueftungsventil betaetigen | Luft ablassen, bis klares Oel austritt | Auffangbehaelter, Schlauch | 15 min |
| Software-Version pruefen | Am MFD oder Controller ablesen | — | 5 min |
| Kompass-Deviation pruefen | Kreisfahrt, Vergleich mit Handpeilkompass | Handpeilkompass | 20 min |
| Ruderlagesensor pruefen | Ruder hart BB/StB, Anzeigewert vergleichen | Winkelmesser | 10 min |

**Zweijahres-Wartung (zusaetzlich zur jaehrlichen):**

| Massnahme | Beschreibung | Werkzeug/Material | Zeitbedarf |
|-----------|-------------|-------------------|------------|
| Oelwechsel | Altes Oel absaugen/ablassen, neues einfuellen | Absaugpumpe, neues Oel, Auffangbehaelter | 60 min |
| Oelfilter ersetzen (falls vorhanden) | Filter ausbauen, neuen einsetzen | Filterschluessel, neuer Filter | 15 min |
| Entlueftung nach Oelwechsel | Systematisch alle Luft aus dem System entfernen | Entlueftungsset, Schlauch | 30 min |
| Kalibrierung durchfuehren | Kompass-Swing, Ruderlage-Kalibrierung | Per Software/MFD | 30 min |

**Fuenfjahres-Wartung (General-Ueberholung empfohlen):**

| Massnahme | Beschreibung | Werkzeug/Material | Zeitbedarf |
|-----------|-------------|-------------------|------------|
| Dichtungssatz Zylinder tauschen | Alle O-Ringe, Quad-Ringe, Stangendichtungen | Herstellerspezifischer Dichtungssatz | 120 min |
| Hydraulikschlaeuche ersetzen | Alle Schlaeuche praventiv tauschen | Neue Schlaeuche, Verschraubungen | 90 min |
| Ueberdruckventil pruefen/tauschen | Ansprechdruck mit Manometer pruefen | Druckmanometer, ggf. neues Ventil | 30 min |
| Rueckschlagventile pruefen | Dichtheit und freien Durchgang testen | Druckluft, Manometer | 20 min |
| Pumpe intern inspizieren | Oeffnen, Zahnraeder/Kolben inspizieren | Herstellerspezifisches Werkzeug | 120 min |
| Komplette Neukalibrierung | Alle Sensoren, Endlagen, Kompass | Per Software | 60 min |

### 3.2 Wartungsplan Linear-Autopilot

#### 3.2.1 Uebersicht Linearantrieb

Linearantriebe wandeln die Drehbewegung eines Elektromotors ueber ein Getriebe und eine Spindel in eine lineare Hubbewegung um. Sie werden direkt am Ruderquadranten, an der Pinne oder an einem Hilfsruderquadranten angeschlossen.

**Linearantrieb-Wartungsmatrix:**

```
┌─────────────────────────────────────────────────────────────────────┐
│                LINEARANTRIEB WARTUNGSMATRIX                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   KOMPONENTE          │ INTERVALL    │ AUFWAND  │ FACHKENNTNIS     │
│  ─────────────────────┼──────────────┼──────────┼────────────────  │
│   Gelenkkoepfe pruefen│ Monatlich    │ 5 min    │ Eigner           │
│   Spiel pruefen       │ Vierteljährl.│ 10 min   │ Eigner           │
│   Schmierung Spindel  │ Halbjährlich │ 15 min   │ Eigner           │
│   Motorstrom messen   │ Jaehrlich    │ 15 min   │ Fortgeschritten  │
│   Endlagen pruefen    │ Jaehrlich    │ 10 min   │ Eigner           │
│   Getriebe inspizieren│ Alle 3 Jahre │ 60 min   │ Fachbetrieb      │
│   Kohlebuersten prfn. │ Alle 2 Jahre │ 30 min   │ Fortgeschritten  │
│   Kolbenstange reinig.│ Halbjährlich │ 10 min   │ Eigner           │
│   Kabel/Stecker prfn. │ Jaehrlich    │ 15 min   │ Eigner           │
│   Befestigung pruefen │ Jaehrlich    │ 10 min   │ Eigner           │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

#### 3.2.2 Detaillierter Wartungsplan — Linearantrieb

**Monatliche Kontrolle:**

| Pruefpunkt | Methode | Akzeptanzkriterium | Bei Abweichung |
|------------|---------|-------------------|----------------|
| Gelenkkopf-Spiel | Manuell wackeln | Kein fuehlbares Spiel | Gelenkkopf ersetzen |
| Kolbenstange auf Korrosion | Visuell | Glatte, glänzende Oberflaeche | Reinigen, leicht oelen |
| Geraeusche waehrend Betrieb | Gehoer | Gleichmaessig summend | Schmierung, Getriebe pruefen |
| Befestigungspins | Visuell + Handpruefung | Splinte vorhanden, kein Spiel | Splinte ersetzen, Bolzen pruefen |

**Halbjaehrliche Wartung:**

| Massnahme | Beschreibung | Material | Zeitbedarf |
|-----------|-------------|----------|------------|
| Spindel schmieren | Fett mit PTFE-Anteil auf Spindel auftragen | Marine-Getriebefett (z.B. Bel-Ray Marine Grease) | 15 min |
| Kolbenstange reinigen und schuetzen | Reinigen, duenn mit korrosionsschuetzdem Oel einreiben | WD-40 Specialist Marine, Ballistol | 10 min |
| Entstaubung Motorgehaehuse | Aussenreinigung, Lueftungsschlitze freiblasen | Druckluft (trocken), Pinsel | 10 min |
| Gelenkkopf schmieren | 1–2 Tropfen Oel in Kugelgelenk | Duennes Maschinenoel | 5 min |

**Jaehrliche Wartung:**

| Massnahme | Beschreibung | Werkzeug/Material | Zeitbedarf |
|-----------|-------------|-------------------|------------|
| Motorstrom messen (Leerlauf + Last) | Amperezange an Versorgung, Leerlauf vs. Ruder hart | Amperezange / Multimeter | 15 min |
| Endlagenschalter-Funktion pruefen | Ruder bis Anschlag fahren, Abschaltung verifizieren | — | 10 min |
| Hub messen | Gesamthub am Antrieb messen, mit Soll vergleichen | Massband / Messschieber | 5 min |
| Geschwindigkeit messen | Zeit fuer vollen Hub, mit Soll vergleichen | Stoppuhr | 5 min |
| Alle elektrischen Verbindungen pruefen | Stecker, Loetverbindungen, Kabelzustand | Kontaktspray, Schrumpfschlauch | 20 min |
| Ruderlagesensor kalibrieren | Kalibrierungsroutine am Controller ausfuehren | Per MFD/Controller | 15 min |
| Kompass kalibrieren | Kreisfahrt bei ruhiger See | Per MFD/Controller | 20 min |
| Befestigungsschrauben pruefen | Alle Schrauben am Antrieb und an der Halterung | Drehmomentschluessel | 10 min |

**Zweijahres-Wartung (zusaetzlich):**

| Massnahme | Beschreibung | Zeitbedarf |
|-----------|-------------|------------|
| Kohlebuersten pruefen (DC-Buerstenmotor) | Motorkappe oeffnen, Buersten messen, >50 % Restlaenge | 30 min |
| Getriebespiel messen | Motor blockieren, Abtriebswelle von Hand drehen, Spiel = Winkel × Hebelarm | 15 min |
| Komplette Fettpackung erneuern | Altes Fett entfernen, neues einbringen | 30 min |

**Dreijahres-Wartung (General-Inspektion):**

| Massnahme | Beschreibung | Zeitbedarf |
|-----------|-------------|------------|
| Getriebe oeffnen und inspizieren | Zahnraeder auf Verschleiss, Lager auf Spiel | 60 min |
| Spindelmutter pruefen | Gewindeprofil auf Abnutzung | 15 min |
| Motor-Isolationswiderstand messen | >2 MOhm bei 500 V DC | 10 min |
| Gelenkkoepfe praventiv tauschen | Neue Gelenkkoepfe einbauen | 20 min |

### 3.3 Wartungsplan Wheel-Drive

#### 3.3.1 Uebersicht Wheel-Drive

Wheel-Drive-Systeme greifen direkt am Steuerrad an. Ein Elektromotor treibt ueber einen Zahnriemen oder ein Getriebe eine Reibrolle oder ein Zahnrad an, das am Steuerrad befestigt ist.

**Wheel-Drive Wartungsmatrix:**

```
┌─────────────────────────────────────────────────────────────────────┐
│                  WHEEL-DRIVE WARTUNGSMATRIX                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   KOMPONENTE          │ INTERVALL    │ AUFWAND  │ FACHKENNTNIS     │
│  ─────────────────────┼──────────────┼──────────┼────────────────  │
│   Riemenspannung      │ Monatlich    │ 5 min    │ Eigner           │
│   Reibrolle pruefen   │ Monatlich    │ 5 min    │ Eigner           │
│   Riemen inspizieren  │ Vierteljährl.│ 10 min   │ Eigner           │
│   Kupplung pruefen    │ Vierteljährl.│ 10 min   │ Eigner           │
│   Motor reinigen      │ Halbjährlich │ 15 min   │ Eigner           │
│   Riemenwechsel       │ Alle 3 Jahre │ 30 min   │ Fortgeschritten  │
│   Alignment pruefen   │ Jaehrlich    │ 20 min   │ Fortgeschritten  │
│   Motorlager pruefen  │ Alle 3 Jahre │ 30 min   │ Fachbetrieb      │
│   Befestigung pruefen │ Halbjährlich │ 10 min   │ Eigner           │
│   Persenning-Zustand  │ Jaehrlich    │ 5 min    │ Eigner           │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

#### 3.3.2 Detaillierter Wartungsplan — Wheel-Drive

**Monatliche Kontrolle:**

| Pruefpunkt | Methode | Akzeptanzkriterium | Bei Abweichung |
|------------|---------|-------------------|----------------|
| Riemenspannung | Fingerdruck: 5–10 mm Durchbiegung bei mittigem Druck | Gleichmaessig gespannt | Nachspannen gemaess Anleitung |
| Reibrolle / Antriebsrad | Visuell: Abrieb, Verfaerbung, Risse | Gleichmaessige Laufflaeche | Reibrolle / Antriebsrad tauschen |
| Kupplungsfunktion | Engage/Disengage pruefen | Sofortiges Einrasten, freies Drehen im manuellen Modus | Kupplung einstellen oder tauschen |
| Freilauf im manuellen Modus | Steuerrad per Hand drehen bei deaktiviertem Pilot | Kein spuerbarer Widerstand | Kupplung pruefen, ggf. freigaengig machen |

**Vierteljährliche Wartung:**

| Massnahme | Beschreibung | Material | Zeitbedarf |
|-----------|-------------|----------|------------|
| Riemen inspizieren | Auf Risse, Abrieb, Faserfreilegung, Flankenabrieb pruefen | Lupe, Taschenlampe | 10 min |
| Antriebsgehaeuse reinigen | Riemenstaub und Salzablagerungen entfernen | Pinsel, Druckluft | 10 min |
| Achslager-Spiel pruefen | Antriebsachse seitlich bewegen, Spiel fuehlen | Haende | 5 min |
| Kabel auf Scheuerstellen | Alle Kabel am und zum Wheel-Drive inspizieren | Visuell | 5 min |

**Jaehrliche Wartung:**

| Massnahme | Beschreibung | Werkzeug/Material | Zeitbedarf |
|-----------|-------------|-------------------|------------|
| Alignment pruefen | Riemenscheiben-Flucht mit Lineal oder Laserausrichter | Laserausrichter / Stahllineal | 20 min |
| Riemenspannung einstellen | Nach Herstellerspezifikation nachstellen | Riemenspannungsmesser, Innensechskant | 15 min |
| Motor-Oberflaeche reinigen | Salzablagerungen, Korrosionsansaetze entfernen | Bremsenreiniger, Tuechlein | 15 min |
| Elektrische Anschluesse pruefen | Alle Steckverbindungen inspizieren und reinigen | Kontaktspray, Poliervlies | 15 min |
| Kompass kalibrieren | Standard-Kalibrierungsroutine | Per MFD/Controller | 20 min |
| Software-Update pruefen | Aktuelle Firmware-Version abfragen und vergleichen | Internet, MFD | 10 min |

**Dreijahres-Wartung:**

| Massnahme | Beschreibung | Zeitbedarf |
|-----------|-------------|------------|
| Zahnriemen tauschen | Praventiver Riemenwechsel | 30 min |
| Motorlager pruefen | Lagergeraeusche, Spiel | 30 min |
| Reibrolle / Antriebsrad tauschen | Praventiver Austausch | 15 min |
| Befestigungskonstruktion inspizieren | Halterung auf Risse, Korrosion | 15 min |

### 3.4 Software-Updates

#### 3.4.1 Allgemeines Vorgehen

Software-Updates fuer Autopiloten koennen Fehler beheben, die Regelguete verbessern und neue Funktionen einfuehren. Die Update-Methode variiert nach Hersteller.

**Update-Methoden nach Hersteller (Confidence: documented):**

| Hersteller | Update-Medium | Software/Tool | Typische Dauer | Besonderheiten |
|------------|--------------|---------------|---------------|----------------|
| Raymarine | microSD-Karte im MFD | LightHouse Software | 15–30 min | Axiom-MFD als Update-Host |
| B&G | microSD / Ethernet | B&G Software Update Tool | 10–20 min | Zeus/Vulcan als Update-Host |
| Garmin | microSD / USB / WiFi | Garmin Express / ActiveCaptain | 10–25 min | OTA ueber ActiveCaptain App moeglich |
| Simrad | microSD / Ethernet | Simrad Update Tool | 10–20 min | NSS/NSO als Update-Host |
| Furuno | USB / Ethernet | Furuno Software-Tool | 20–40 min | Spezifische Update-Reihenfolge beachten |
| NKE | USB / Bluetooth | NKE TopLine App | 10–15 min | Topline Prozessor als Update-Host |

**Sicherheitsregeln fuer Software-Updates:**

1. **Nie waehrend der Fahrt** — Immer im sicheren Hafen updaten
2. **Stabile Stromversorgung** — Landstrom oder volle Batterie (>80 %)
3. **Backup** — Wenn moeglich, Einstellungen vor Update exportieren
4. **Vollstaendiges Update** — Nie den Update-Vorgang unterbrechen
5. **Neukalibrierung** — Nach groesseren Updates Kompass- und Ruderkalibrierung durchfuehren
6. **Testfahrt** — Nach Update Kurztest unter kontrollierten Bedingungen
7. **Kompatibilitaet** — Firmware-Versionen aller vernetzten Geraete pruefen (NMEA 2000 Netzwerk)

#### 3.4.2 Hersteller-spezifische Update-Besonderheiten

**Raymarine:**
- Evolution-System: EV-1 Sensoreinheit, ACU-Antriebseinheit und MFD muessen kompatible Firmwarestaende haben
- Update-Reihenfolge: Immer zuerst MFD, dann ACU, dann EV-1
- Nach Update: Sealevel Calibration empfohlen (Kompass-Neuinitialisierung)
- Release Notes beachten: Manche Updates erfordern manuellen Reset der Autoadaption

**B&G / Simrad (Navico-Plattform):**
- NAC-Controller und Prozessor-Einheit getrennt updaten
- Continuum-Algorithmus: Nach groesseren Updates laeuft eine neue Lernphase (~30 min Fahrt)
- Precision-9 Kompass: Eigene Firmware, separates Update
- Netzwerk-Kompatibilitaet: Alle Navico-Geraete im NMEA2000-Netzwerk pruefen

**Garmin:**
- GHP Reactor: Update ueber kompatibles Garmin-MFD oder Garmin Express
- ActiveCaptain App ermoeglicht drahtloses Update (WiFi)
- Shadow Drive Kalibrierung: Nach Update automatisch, aber Testfahrt empfohlen
- CCU (Course Computer Unit): Hat eigene Firmware, separates Update

**Furuno:**
- NAVpilot: Strenge Update-Reihenfolge (Prozessor → Antrieb → Sensoren)
- Proprietaeres Update-Tool fuer PC erforderlich
- NMEA2000-Konverter (IF-NMEA2K1/2): Eigenes Update beachten
- Nach Update: Zwingend Kompass-Kalibrierung wiederholen

### 3.5 Saisonale Inbetriebnahme

#### 3.5.1 Checkliste Fruehjahrsinbetriebnahme

Die korrekte Inbetriebnahme nach der Winterpause ist entscheidend fuer die Zuverlaessigkeit waehrend der Saison.

**Fruehjahrsinbetriebnahme — Schritt fuer Schritt (Confidence: documented):**

| Schritt | Massnahme | Pruefmethode | Dauer |
|---------|-----------|-------------|-------|
| 1 | Sicherungen und Schalter pruefen | Visuell, Durchgangspruefung | 5 min |
| 2 | Versorgungsspannung messen | Multimeter an Autopilot-Anschluss | 5 min |
| 3 | Steckverbindungen inspizieren | Stecker ziehen, Pins pruefen, Kontaktspray | 15 min |
| 4 | Hydraulik: Oelstand und -zustand pruefen | Schauglas, Farbe/Klarheit | 5 min |
| 5 | Mechanik: Spiel, Befestigung pruefen | Manuell, Drehmomentschluessel | 10 min |
| 6 | System einschalten, Fehlermeldungen notieren | MFD/Controller | 5 min |
| 7 | Ruderlage-Anzeige pruefen (Mittelstellung) | Ruder auf Mitte, Anzeige ablesen | 5 min |
| 8 | Manuellen Rudertest durchfuehren | Pilot-Tasten BB/StB, Ruderbewegung beobachten | 5 min |
| 9 | Endlagen testen | Ruder bis Anschlag fahren (BB und StB) | 5 min |
| 10 | Kompass-Abweichung pruefen (bekannter Kurs) | Handpeilkompass vs. Autopilot-Kompass | 10 min |
| 11 | Kurzer Fahrtest (10 min) | Autopilot auf geraden Kurs, Verhalten beobachten | 10 min |
| 12 | Kursaenderung testen (90°, 180°) | Kursaenderung eingeben, Reaktionszeit und Praezision | 10 min |
| 13 | Windfahnen-Integration pruefen (Segelboote) | Auf Windkurs gehen, Kursaenderung bei Winddrehung | 15 min |
| 14 | Alarm-Funktionen testen | Off-Course-Alarm provozieren | 5 min |
| 15 | Einstellungen dokumentieren | Alle Parameter notieren/fotografieren | 10 min |

#### 3.5.2 Bekannte Probleme nach Winterpause

**Haeufige Probleme bei Inbetriebnahme (Confidence: estimated):**

| Problem | Haeufigkeit | Ursache | Loesung |
|---------|------------|---------|---------|
| "No Rudder Feedback" | 25 % | Korrosion am Ruderlagesensor-Stecker | Stecker reinigen, Kontaktspray |
| Kompass-Deviation >5° | 20 % | Veraendertes Magnetfeld (neue Geraete, Werkzeug) | Neukalibrierung |
| Traege Reaktion | 18 % | Luft in Hydraulik / verharztes Fett im Linear | Entlueftung / Schmierung |
| Fehlermeldung "Clutch Error" | 12 % | Kupplungskontakt korrodiert | Kontakte reinigen |
| Kein Einschalten | 10 % | Sicherung, Schalter, Kabelbruch | Systematische Fehlersuche |
| Software-Fehler nach Spannungsfreiheit | 8 % | Parameter-Reset durch leere Backup-Batterie | Werkseinstellungen, Neukalibrierung |
| Hoher Stromverbrauch | 5 % | Motor schwergaengig, Dichtung gequollen | Mechanik pruefen, Dichtung tauschen |
| Unruhiges Steuern | 2 % | Adaptive Parameter veraltet | Adaptation zuruecksetzen, Lernfahrt |

### 3.6 Winterfestmachung

#### 3.6.1 Checkliste Einwinterung

Die korrekte Einwinterung verlaengert die Lebensdauer des Autopiloten erheblich.

**Winterfestmachung — Schritt fuer Schritt (Confidence: documented):**

| Schritt | Massnahme | Zweck | Dauer |
|---------|-----------|-------|-------|
| 1 | Letzte Fahrparameter dokumentieren | Referenzwerte fuer Fruehjahrsinbetriebnahme | 10 min |
| 2 | System ordnungsgemaess herunterfahren | Kontrolliertes Abschalten | 2 min |
| 3 | Batterie-Hauptschalter AUS | Kriechstromvermeidung | 1 min |
| 4 | Alle Steckverbindungen mit Korrosionsschutz | Langzeitschutz | 20 min |
| 5 | Hydraulik: Oelstand auf MAX auffuellen | Kondensationsschutz (weniger Luftvolumen) | 10 min |
| 6 | Linear/Wheel: Mechanik schmieren | Korrosionsschutz waehrend Standzeit | 15 min |
| 7 | Abnehmbare Teile (Controller, Tillerpilot) deinstallieren | Diebstahlschutz, Witterungsschutz | 15 min |
| 8 | Verbleibende Teile abdecken / einpacken | UV- und Feuchtigkeitsschutz | 10 min |
| 9 | Rudermechanik leicht gangbar fixieren | Lastfreier Zustand, kein Festrosten | 5 min |
| 10 | Wenn beheizt: Silicagel-Beutel in Gehaeuse legen | Feuchtigkeitskontrolle | 5 min |

**Besonderheiten nach Klimazone (Confidence: estimated):**

| Region | Temperaturen | Zusaetzliche Massnahmen |
|--------|-------------|------------------------|
| Nordeuropa (Skandinavien) | Bis –25°C | Hydraulikoel auf Frostbestaendigkeit pruefen (ATF bis –40°C ok). Ggf. Elektronik demontieren. |
| Mitteleuropa (DACH) | Bis –15°C | Standard-Einwinterung ausreichend. Belüftung sicherstellen. |
| Mittelmeer (Winterlager) | +5 bis +15°C | Schwerpunkt auf UV-Schutz und Feuchtigkeitskontrolle. Silicagel. |
| Tropen (Ganzjahresbetrieb) | +25 bis +40°C | Kein Einwintern. Stattdessen Fokus auf UV-Schutz, Kuehlung, regelmaessige Wartung. |

---

## 4. Produktlinien und Spezifikationen

### 4.1 Wartungskits und Ersatzteile — Raymarine

**Raymarine Evolution Autopilot-System:**

| Komponente | Teilenummer | Beschreibung | Preis (ca.) | Intervall |
|------------|------------|-------------|-------------|-----------|
| EV-1 Sensormodul | T70096 | Fluxgate + AHRS Sensor (Tausch) | 480 EUR | Bei Defekt |
| ACU-150 Antriebssteuerung | E70430 | Aktuator-Steuereinheit (bis 1,5 l Pumpe) | 890 EUR | Bei Defekt |
| ACU-200 Antriebssteuerung | E70099 | Aktuator-Steuereinheit (bis 3 l Pumpe) | 1.250 EUR | Bei Defekt |
| ACU-400 Antriebssteuerung | E70100 | Aktuator-Steuereinheit (bis 4 l Pumpe) | 1.680 EUR | Bei Defekt |
| Type 1 Hydraulikpumpe (12V) | M81120 | Reversible Pumpe 80 cc/min | 1.450 EUR | Bei Defekt |
| Type 2 Hydraulikpumpe (12V) | M81121 | Reversible Pumpe 160 cc/min | 2.100 EUR | Bei Defekt |
| Hydraulik-Dichtungssatz Type 1 | D016 | O-Ringe, Kolbendichtungen fuer Type 1 | 65 EUR | Alle 5 Jahre |
| Hydraulik-Dichtungssatz Type 2 | D017 | O-Ringe, Kolbendichtungen fuer Type 2 | 85 EUR | Alle 5 Jahre |
| Zylinder-Dichtungssatz (2") | A18091 | Fuer 2"-Hydraulikzylinder | 45 EUR | Alle 5 Jahre |
| Zylinder-Dichtungssatz (3") | A18092 | Fuer 3"-Hydraulikzylinder | 55 EUR | Alle 5 Jahre |
| Linear Drive Type 1 (12V) | M81130 | 500 lb Schub, 12V | 890 EUR | Bei Defekt |
| Linear Drive Type 2 (12V) | M81131 | 1.000 lb Schub, 12V | 1.350 EUR | Bei Defekt |
| Wheel Drive EV-100 | T70152 | Komplettsystem inkl. EV-1, Controller | 1.950 EUR | Bei Defekt |
| Ruderlagesensor | E22078 | Potentiometer-Typ, ±45° | 220 EUR | Alle 5–8 Jahre |
| p70 Autopilot-Controller | E22166 | Cockpit-Bedieneinheit | 420 EUR | Bei Defekt |
| p70s Autopilot-Controller | E22167 | Cockpit-Bedieneinheit (Segelboot) | 450 EUR | Bei Defekt |
| SPX-5 Kabelbaum | R08045 | Verdrahtungssatz fuer SPX-Systeme | 75 EUR | Bei Bedarf |
| Evolution Kabelbaum | A80356 | SeaTalkng Power-Kabel 3 m | 35 EUR | Bei Bedarf |

**Raymarine Schmiermittel und Betriebsstoffe:**

| Produkt | Teilenummer | Einsatz | Menge | Preis (ca.) |
|---------|------------|---------|-------|-------------|
| Hydraulikoel (ATF Dexron III) | Handelsware | Alle Raymarine Hydraulik-Systeme | 1 l pro Fuell. | 8–15 EUR/l |
| Kontaktfett (Bootsstecker) | — | Steckverbindungen | 50 g Tube | 12 EUR |
| Korrosionsschutzspray | — | Ueberwinternde Teile | 400 ml | 10 EUR |

### 4.2 Wartungskits und Ersatzteile — B&G

**B&G Autopilot-System (Navico-Plattform):**

| Komponente | Teilenummer | Beschreibung | Preis (ca.) | Intervall |
|------------|------------|-------------|-------------|-----------|
| Precision-9 Kompass | 000-12607-001 | 9-Achsen AHRS Kompass-Sensor | 550 EUR | Bei Defekt |
| NAC-2 Autopilot-Computer | 000-13249-001 | Low-Current-System (bis 12 A) | 780 EUR | Bei Defekt |
| NAC-3 Autopilot-Computer | 000-13250-001 | High-Current-System (bis 30 A) | 1.150 EUR | Bei Defekt |
| RFC35 Ruderlagesensor | 000-13914-001 | Kontaktloser Sensor, ±45° | 280 EUR | Bei Defekt |
| Hydraulikpumpe RPU80 (12V) | 000-13186-001 | Reversible Pumpe 80 cc/rev | 1.650 EUR | Bei Defekt |
| Hydraulikpumpe RPU160 (12V) | 000-13187-001 | Reversible Pumpe 160 cc/rev | 2.350 EUR | Bei Defekt |
| Linear Drive SD10 (12V) | 000-11563-001 | Linear-Antrieb 300 lb | 680 EUR | Bei Defekt |
| Linear Drive SD12 (12V) | 000-11564-001 | Linear-Antrieb 750 lb | 980 EUR | Bei Defekt |
| Dichtungssatz RPU80 | 000-13901-001 | Service-Kit fuer RPU80 | 72 EUR | Alle 5 Jahre |
| Dichtungssatz RPU160 | 000-13902-001 | Service-Kit fuer RPU160 | 95 EUR | Alle 5 Jahre |
| H5000 Autopilot-Computer | 000-11544-001 | High-Performance Prozessor | 2.800 EUR | Bei Defekt |
| WTP3 Wheel-Drive | 000-14075-001 | Wheel-Tillerpilot (Radsteuerung) | 1.450 EUR | Bei Defekt |
| Triton² Autopilot Controller | 000-13294-001 | Bedieneinheit + Display | 480 EUR | Bei Defekt |

### 4.3 Wartungskits und Ersatzteile — Garmin

**Garmin GHP Reactor Autopilot-System:**

| Komponente | Teilenummer | Beschreibung | Preis (ca.) | Intervall |
|------------|------------|-------------|-------------|-----------|
| GHP Reactor Steer-by-wire Kit | 010-11748-01 | Kern-Kit (CCU, Shadow Drive™) | 2.200 EUR | Bei Defekt |
| CCU (Course Computer Unit) | 010-11053-10 | Autopilot-Rechner | 890 EUR | Bei Defekt |
| GHP 12 Hydraulikpumpe (12V) | 010-11097-10 | Fuer Boote 6–12 m | 1.550 EUR | Bei Defekt |
| GHP 20 Hydraulikpumpe (12V) | 010-11098-10 | Fuer Boote 10–20 m | 2.100 EUR | Bei Defekt |
| Reactor 40 Steuereinheit | 010-02794-00 | Autopilot-Steuereinheit (mechanisch) | 2.400 EUR | Bei Defekt |
| GRF 10 Ruderlagesensor | 010-11986-00 | Ruderfeedback-Sensor | 240 EUR | Bei Defekt |
| GHP Smart Pump Kit | 010-02795-00 | Intelligente Pumpensystem-Kit | 3.200 EUR | Bei Defekt |
| Shadow Drive™ Ventil | 010-11054-10 | Bypass-Ventil fuer manuelle Uebersteuerung | 380 EUR | Bei Defekt |
| Garmin Hydraulikoel | 010-11684-00 | Spezial-Hydraulikoel (1 l) | 25 EUR | Alle 2–3 Jahre |
| Dichtungssatz GHP 12 | 010-12345-00 | O-Ringe, Dichtungen fuer GHP 12 | 55 EUR | Alle 5 Jahre |
| Dichtungssatz GHP 20 | 010-12346-00 | O-Ringe, Dichtungen fuer GHP 20 | 75 EUR | Alle 5 Jahre |
| GHP Wheel-Pilot | 010-02796-00 | Radantrieb komplett | 1.850 EUR | Bei Defekt |

### 4.4 Wartungskits und Ersatzteile — Simrad

**Simrad Autopilot-System (Navico-Plattform):**

| Komponente | Teilenummer | Beschreibung | Preis (ca.) | Intervall |
|------------|------------|-------------|-------------|-----------|
| AP44 Autopilot Controller | 000-13289-001 | Cockpit-Bedieneinheit | 480 EUR | Bei Defekt |
| AP48 Autopilot Controller | 000-15198-001 | Premium-Bedieneinheit mit Drehregler | 580 EUR | Bei Defekt |
| NAC-2 Computer | 000-13249-001 | Identisch mit B&G NAC-2 | 780 EUR | Bei Defekt |
| NAC-3 Computer | 000-13250-001 | Identisch mit B&G NAC-3 | 1.150 EUR | Bei Defekt |
| Precision-9 Kompass | 000-12607-001 | Identisch mit B&G Precision-9 | 550 EUR | Bei Defekt |
| RPU80/160 Pumpen | wie B&G | Identisch mit B&G Pumpen | wie B&G | wie B&G |
| SD10/12 Linear Drives | wie B&G | Identisch mit B&G Linear Drives | wie B&G | wie B&G |

> **Hinweis:** Simrad und B&G teilen sich die Navico/Navico-Plattform (jetzt Teil von Brunswick). Antriebskomponenten, Computer und Sensoren sind identisch. Lediglich die Bedieneinheiten und die Software-Oberflaeche unterscheiden sich.

### 4.5 Wartungskits und Ersatzteile — Furuno

**Furuno NAVpilot Autopilot-System:**

| Komponente | Teilenummer | Beschreibung | Preis (ca.) | Intervall |
|------------|------------|-------------|-------------|-----------|
| NAVpilot 300 Prozessor | FAP-3011C | Autopilot-Hauptprozessor | 1.850 EUR | Bei Defekt |
| PG-700 Fluxgate-Sensor | PG-700 | Fluxgate-Kompass-Sensor | 380 EUR | Bei Defekt |
| SC-50 Satellitenkompass | SC-50 | GPS-Kompass (Heading Sensor) | 2.800 EUR | Bei Defekt |
| FAP-2011 Pumpensteuerung | FAP-2011 | Steuereinheit fuer Hydraulikpumpe | 980 EUR | Bei Defekt |
| Reversible Pumpe RDP-050 | RDP-050 | 50 cc/min (12V) | 1.450 EUR | Bei Defekt |
| Reversible Pumpe RDP-150 | RDP-150 | 150 cc/min (12V) | 2.250 EUR | Bei Defekt |
| Ruderlagesensor FBR-210 | FBR-210 | Potentiometer-Typ | 195 EUR | Alle 5–8 Jahre |
| Ruderlagesensor FBR-310 | FBR-310 | Hall-Effekt (kontaktlos) | 340 EUR | Bei Defekt |
| Dichtungssatz RDP-050 | — | Service-Kit fuer RDP-050 | 65 EUR | Alle 5 Jahre |
| Dichtungssatz RDP-150 | — | Service-Kit fuer RDP-150 | 90 EUR | Alle 5 Jahre |
| NAVpilot Display FUI | NAVpilot-700 | Touch-Bedieneinheit | 1.200 EUR | Bei Defekt |
| IF-NMEA2K1 | IF-NMEA2K1 | NMEA 2000-Interface | 220 EUR | Bei Defekt |

### 4.6 Wartungskits und Ersatzteile — Pelagic / NKE

**NKE Gyropilot-System:**

| Komponente | Teilenummer | Beschreibung | Preis (ca.) | Intervall |
|------------|------------|-------------|-------------|-----------|
| Gyropilot 2 Prozessor | GP2-PROC | Autopilot-Hauptprozessor | 1.600 EUR | Bei Defekt |
| Gyrokompass | GP-GYRO | MEMS-Gyroskop + Fluxgate | 620 EUR | Bei Defekt |
| Hydraulikantrieb HR1 (12V) | HR1-12 | Fuer Boote 8–14 m | 1.380 EUR | Bei Defekt |
| Hydraulikantrieb HR2 (12V) | HR2-12 | Fuer Boote 12–20 m | 1.980 EUR | Bei Defekt |
| Linerantrieb EL1 | EL1-12 | 400 lb Schub | 720 EUR | Bei Defekt |
| Ruderlagesensor NKE | RFB-NKE | Kontaktloser Sensor | 260 EUR | Bei Defekt |
| Pilotline Display | PL-DSP | Bedieneinheit | 380 EUR | Bei Defekt |
| TopLine Prozessor | TL-PROC | Zentralprozessor (Multi-Instrument) | 1.200 EUR | Bei Defekt |
| Dichtungssatz HR1 | HR1-SEAL | O-Ringe, Dichtungen | 58 EUR | Alle 5 Jahre |
| Dichtungssatz HR2 | HR2-SEAL | O-Ringe, Dichtungen | 78 EUR | Alle 5 Jahre |

---

## 5. Hersteller-Datenbank

### 5.1 Raymarine (FLIR Systems / Teledyne)

| Attribut | Details |
|----------|---------|
| **Hauptsitz** | Fareham, Hampshire, UK |
| **Mutterkonzern** | Teledyne Technologies (seit 2021, vorher FLIR) |
| **Gruendungsjahr** | 1923 (als Kelvin & Hughes), Marke Raymarine seit 1999 |
| **Marktposition** | Nr. 1–2 weltweit im Sportbootbereich |
| **Autopilot-Serien** | Evolution (EV-1/EV-2), SPX (aelter), SmartPilot (EOL) |
| **Technologie-Schwerpunkt** | AHRS-Sensorik, Adaptive Algorithmen, SeaTalkng |
| **NMEA-Support** | SeaTalkng (proprietaer, NMEA2000-kompatibel), SeaTalk1 (aelter) |
| **Service-Netzwerk DACH** | ca. 45 autorisierte Servicestaetten |
| **Garantie** | 2 Jahre Standard, 3 Jahre bei Online-Registrierung |
| **Website** | www.raymarine.com |
| **Service-Hotline DACH** | +49 (0)40 237 03 0 (Distributeur: Busse Yachtshop) |
| **Firmware-Update-Portal** | www.raymarine.com/software |
| **Staerken** | Gute Sensorintegration, breites Zubehoer, weit verbreitet |
| **Schwaechen** | Proprietaeres SeaTalk-Protokoll (Legacy), Kunststoffgehaeuse |

### 5.2 B&G (Navico / Brunswick)

| Attribut | Details |
|----------|---------|
| **Hauptsitz** | Egham, Surrey, UK (Entwicklung: Neuseeland) |
| **Mutterkonzern** | Brunswick Corporation (via Navico, seit 2021) |
| **Gruendungsjahr** | 1959 (Brookes & Gatehouse) |
| **Marktposition** | Premium-Segment, stark im Regattabereich |
| **Autopilot-Serien** | NAC-2/NAC-3, H5000, WTP3 |
| **Technologie-Schwerpunkt** | Continuum Adaptive, Sail-Steer, Performance-Segeln |
| **NMEA-Support** | NMEA 2000, Ethernet (NavNet) |
| **Service-Netzwerk DACH** | ca. 30 autorisierte Servicestaetten |
| **Garantie** | 2 Jahre Standard |
| **Website** | www.bandg.com |
| **Service-Hotline DACH** | +49 (0)4122 71 77 0 (Distributeur: Busse/Navico) |
| **Staerken** | Hervorragend fuer Segelboote, Regatta-Performance, Continuum-Algorithmus |
| **Schwaechen** | Preislich im oberen Segment, kleineres Servicenetz |

### 5.3 Garmin

| Attribut | Details |
|----------|---------|
| **Hauptsitz** | Olathe, Kansas, USA |
| **Mutterkonzern** | Garmin Ltd. (boersennotiert) |
| **Gruendungsjahr** | 1989 |
| **Marktposition** | Nr. 1–2 weltweit, stark wachsend im Marinebereich |
| **Autopilot-Serien** | GHP Reactor, GHP 10/12/20, Reactor 40 |
| **Technologie-Schwerpunkt** | Shadow Drive™, Steer-by-Wire, Smart Pump |
| **NMEA-Support** | NMEA 2000, Garmin proprietaer (aeltere Modelle) |
| **Service-Netzwerk DACH** | ca. 50 autorisierte Servicestaetten (via Garmin DACH) |
| **Garantie** | 2 Jahre Standard |
| **Website** | www.garmin.com/marine |
| **Service-Hotline DACH** | +49 (0)89 858 364 40 |
| **Firmware-Update** | ActiveCaptain App (OTA), Garmin Express |
| **Staerken** | Einfache Bedienung, OTA-Updates, Shadow Drive (nahtloses manuelles Eingreifen) |
| **Schwaechen** | Teilweise proprietaere Oele, eingeschraenkte Drittanbieter-Integration (aeltere Modelle) |

### 5.4 Simrad (Navico / Brunswick)

| Attribut | Details |
|----------|---------|
| **Hauptsitz** | Egersund, Norwegen |
| **Mutterkonzern** | Brunswick Corporation (via Navico) |
| **Gruendungsjahr** | 1947 |
| **Marktposition** | Stark im professionellen und Motorboot-Bereich |
| **Autopilot-Serien** | AP44/AP48, NAC-2/NAC-3 (Navico-Plattform) |
| **Technologie-Schwerpunkt** | Continuum Adaptive (wie B&G), Motorboot-Optimierung |
| **NMEA-Support** | NMEA 2000, Ethernet |
| **Service-Netzwerk DACH** | ca. 35 autorisierte Servicestaetten |
| **Garantie** | 2 Jahre Standard |
| **Website** | www.simrad-yachting.com |
| **Staerken** | Robuste Hardware, gute Motorboot-Integration, Navico-Oekosystem |
| **Schwaechen** | Weniger Segelfunktionen als B&G, teilweise identische Hardware |

### 5.5 Furuno

| Attribut | Details |
|----------|---------|
| **Hauptsitz** | Nishinomiya, Japan |
| **Mutterkonzern** | Furuno Electric Co., Ltd. (boersennotiert) |
| **Gruendungsjahr** | 1948 |
| **Marktposition** | Premium-Segment, stark im professionellen Bereich |
| **Autopilot-Serien** | NAVpilot 300/700, FAP-Serie |
| **Technologie-Schwerpunkt** | Professionelle Zuverlaessigkeit, Satellitenkompass-Integration |
| **NMEA-Support** | NMEA 2000, NMEA 0183, Furuno CAN bus |
| **Service-Netzwerk DACH** | ca. 25 autorisierte Servicestaetten |
| **Garantie** | 2–3 Jahre (produktabhaengig) |
| **Website** | www.furuno.com |
| **Service-Hotline DACH** | +49 (0)4101 838 80 |
| **Staerken** | Hoechste Zuverlaessigkeit, professionelle Herkunft, exzellenter Service |
| **Schwaechen** | Hoehere Preise, weniger DIY-freundlich, seltener auf Sportbooten <12 m |

### 5.6 NKE Marine Electronics

| Attribut | Details |
|----------|---------|
| **Hauptsitz** | Hennebont, Frankreich |
| **Mutterkonzern** | NKE (eigenstaendig) |
| **Gruendungsjahr** | 1984 |
| **Marktposition** | Nische: High-Performance-Segeln, Offshore-Regatta |
| **Autopilot-Serien** | Gyropilot 2, Pilotline |
| **Technologie-Schwerpunkt** | Gyro-basierte Steuerung, optimiert fuer schnelles Segeln |
| **NMEA-Support** | NMEA 2000, proprietaeres TopLine-Bus |
| **Service-Netzwerk DACH** | ca. 8 autorisierte Servicestaetten |
| **Garantie** | 2 Jahre Standard |
| **Website** | www.nke-marine-electronics.com |
| **Staerken** | Beste Regelguete beim Segeln, sehr schnelle Reaktion, Regatta-erprobt |
| **Schwaechen** | Kleines Servicenetz ausserhalb Frankreichs, hohe Preise, geringe Verbreitung |

### 5.7 Lecomble & Schmitt

| Attribut | Details |
|----------|---------|
| **Hauptsitz** | Boulogne-sur-Mer, Frankreich |
| **Mutterkonzern** | Lecomble & Schmitt (eigenstaendig) |
| **Gruendungsjahr** | 1962 |
| **Marktposition** | Spezialist fuer Hydraulik-Steueranlagen |
| **Produkte** | Hydraulikzylinder, Pumpen, Ruderanlagen (nicht Autopilot-Elektronik) |
| **Relevanz** | Viele Autopilot-Hydrauliksysteme nutzen L&S-Zylinder und -Leitungen |
| **Service-Netzwerk DACH** | ueber Werft-Partner |
| **Website** | www.lecomble-schmitt.com |
| **Staerken** | Marktfuehrer Hydraulik-Steuerung, extrem zuverlaessig, 60+ Jahre Erfahrung |
| **Schwaechen** | Reine Hydraulik-Komponenten, keine eigene Elektronik |

---

## 6. Fehlerbild-Atlas

### Fehlerbild 1: Kupplung greift nicht (Clutch Engagement Failure)

**Symptom:** Der Autopilot laesst sich aktivieren, das Ruder reagiert aber nicht oder nur verzoegert. Im manuellen Modus laesst sich das Steuerrad/die Pinne normal bewegen.

**Haeufigkeit:** 12 % aller Autopilot-Servicefaelle (Confidence: benchmark)

**Moegliche Ursachen:**

| Rang | Ursache | Haeufigkeit | Pruefung |
|------|---------|------------|----------|
| 1 | Korrodierter Kupplungskontakt | 35 % | Stecker pruefen, Spannung an Kupplung messen |
| 2 | Abgenutzter Reibbelag | 25 % | Visuelle Inspektion nach Oeffnung |
| 3 | Defekte Kupplungsspule (EM) | 15 % | Widerstand messen (Soll: 8–15 Ohm) |
| 4 | Zu geringe Versorgungsspannung | 12 % | Spannung messen waehrend Engagement |
| 5 | Mechanische Blockade | 8 % | Kupplung manuell pruefen (Fremdkoerper?) |
| 6 | Steuerungsfehler (Software) | 5 % | Fehlerspeicher auslesen, Reset versuchen |

**Diagnoseschritte:**
1. Versorgungsspannung am Autopiloten messen (>10,5 V / >21 V)
2. Spannung am Kupplungsstecker messen bei Aktivierung (Soll: Nennspannung)
3. Widerstand der Kupplungsspule messen (EM-Kupplung): Soll 8–15 Ohm, Ist <5 Ohm = Kurzschluss, >100 Ohm = Unterbrechung
4. Kupplung mechanisch pruefen: Manuell einrasten, Spiel, Reibflaeche
5. Fehlerspeicher der Steuereinheit auslesen
6. Software-Reset durchfuehren (als letzter Schritt)

### Fehlerbild 2: Ungewoehnliches Motorgeraeusch

**Symptom:** Der Autopilot-Antrieb erzeugt Geraeusche, die von der normalen Betriebslautstaerke abweichen. Dies kann Brummen, Kreischen, Klappern, Schleifen oder Pulsieren sein.

**Haeufigkeit:** 15 % aller Autopilot-Servicefaelle (Confidence: benchmark)

**Geraeuschtypen und Zuordnung:**

| Geraeuschtyp | Charakter | Wahrscheinliche Ursache | Dringlichkeit |
|-------------|----------|------------------------|---------------|
| Brummen (gleichmaessig, tief) | Niederfrequent, konstant | Normales Pumpengeraeusch bei erhoehtem Druck | NIEDRIG |
| Brummen (pulsierend) | Niederfrequent, rhythmisch | Luft im Hydrauliksystem | MITTEL |
| Kreischen / Quietschen | Hochfrequent, intermittierend | Trockenlauf Lager, Riemenrutschen | HOCH |
| Klappern / Klopfen | Metallisch, unregelmaessig | Lockere Befestigung, Zahnspiel, Fremdkoerper | HOCH |
| Schleifen | Rau, kontinuierlich | Abrieb Kohlebuersten, Lagerschaden | MITTEL–HOCH |
| Knacken | Einzelgeraeusche bei Richtungswechsel | Zahnriemensprung, Kupplungsspiel | MITTEL |
| Summen (hochfrequent) | Elektronisch | Magnetostriktives Geraeusch (normal bei Solenoids) | NIEDRIG |

**Diagnoseschritte:**
1. Geraeuschtyp identifizieren und dokumentieren (ggf. Audioaufnahme)
2. Geraeuschquelle lokalisieren: Motor? Pumpe? Zylinder? Getriebe? Riemen?
3. Last entfernen (Ruder auskuppeln) — Geraeusch noch vorhanden?
4. Motorstrom messen — Korrelation mit Geraeusch?
5. Bei Hydraulik: Entlueftung durchfuehren (haeufigstes Problem)
6. Visuell inspizieren (Riemen, Befestigung, Lager, Zahnraeder)

### Fehlerbild 3: Kursverlust (Course Deviation)

**Symptom:** Der Autopilot haelt den eingestellten Kurs nicht. Das Boot weicht langsam oder plotzlich vom Sollkurs ab.

**Haeufigkeit:** 22 % aller Autopilot-Servicefaelle (Confidence: benchmark)

**Klassifizierung der Kursabweichung:**

| Typ | Charakter | Typische Ursache |
|-----|----------|-----------------|
| Langsame Drift (>5 min) | Allmaehlliche Abweichung in eine Richtung | Kompass-Fehler, Trim-Problem |
| Oszillation (Pendeln) | Regelmaessiges Links-Rechts | PID-Parameter falsch, Seegangsfilter |
| Plotzlicher Sprung | Einmaliger Kurssprung >10° | Kompass-Stoerung, Softwarefehler |
| Unregelmaessige Schwankungen | Chaotische Kursaenderungen | Sensorfehler, Verkabelung |
| Einseitiges Steuern | Korrigiert nur in eine Richtung | Ruderlagesensor defekt/dejustiert |

**Moegliche Ursachen und Haeufigkeit:**

| Rang | Ursache | Haeufigkeit | Schweregrad |
|------|---------|------------|-------------|
| 1 | Kompass-Deviation (magnetisch) | 28 % | MITTEL |
| 2 | Falsche PID-Parameter / Seegangsfilter | 22 % | NIEDRIG |
| 3 | Ruderlagesensor dejustiert | 18 % | MITTEL |
| 4 | Mechanisches Spiel (Kupplung, Gelenke) | 12 % | MITTEL |
| 5 | Hydraulik-Leckage (interner Bypass) | 8 % | HOCH |
| 6 | Unzureichende Antriebsleistung | 6 % | HOCH |
| 7 | Software-/Firmware-Bug | 4 % | MITTEL |
| 8 | EMV-Stoerung | 2 % | NIEDRIG–HOCH |

### Fehlerbild 4: Kompassdrift

**Symptom:** Der vom Autopiloten angezeigte Kurs weicht systematisch vom tatsaechlichen Kurs ab, oder die Anzeige driftet ueber die Zeit.

**Haeufigkeit:** 18 % aller Autopilot-Servicefaelle (Confidence: benchmark)

**Drifttypen:**

| Typ | Charakter | Typische Ursache |
|-----|----------|-----------------|
| Konstanter Offset | Fester Winkelfehler auf allen Kursen | Mechanische Fehlausrichtung, Deviation |
| Kursabhaengiger Offset | Fehler variiert mit Steuerkurs | Magnetische Beeinflussung (Weicheisen) |
| Zeitabhaengige Drift | Fehler waechst mit Betriebszeit | Gyro-Drift (selten bei modernen MEMS) |
| Temperaturabhaengige Drift | Fehler korreliert mit Temperatur | Sensorspezifisch, Kompensation fehlerhaft |
| Kraengungsabhaengige Drift | Fehler bei Schraglage | Keine Neigungskompensation oder falsch kalibriert |

**Diagnoseschritte:**
1. Handpeilkompass-Vergleich auf 8 Kursen (N, NE, E, SE, S, SW, W, NW)
2. Deviationstabelle erstellen (Soll vs. Ist)
3. Maximale Deviation bestimmen — akzeptabel: <5° nach Kalibrierung
4. Umgebung auf neue Magnetfeldquellen pruefen (Geraete, Werkzeug, Lautsprecher)
5. Kalibrierungsroutine durchfuehren (Kreisfahrt bei ruhiger See)
6. Fluxgate-Sonde auf korrekten Einbau pruefen (Ausrichtung, Neigung)
7. Bei persistenter Deviation >5°: Fluxgate-Sonde umpositionieren

### Fehlerbild 5: Fehlermeldungen auf Display

**Symptom:** Der Autopilot zeigt Fehlermeldungen oder Warnungen an und verweigert den Betrieb oder arbeitet eingeschraenkt.

**Haeufigkeit:** 20 % aller Autopilot-Servicefaelle (Confidence: benchmark)

**Haeufige Fehlermeldungen nach Hersteller:**

| Fehlermeldung | Hersteller | Bedeutung | Haeufigste Ursache |
|--------------|-----------|-----------|-------------------|
| "No Compass Data" | Alle | Kein Kompass-Signal empfangen | Kabel/Stecker, Kompass defekt |
| "Rudder Feedback Error" | Alle | Kein oder unplausibles Ruderlagesignal | Sensor defekt, Kabel, Kalibrierung |
| "Drive Stopped" / "Overcurrent" | Alle | Antriebsmotor-Ueberstrom | Mechanische Blockade, Motor defekt |
| "Low Voltage" | Alle | Versorgungsspannung zu niedrig | Batterie, Kabelquerschnitt, Kontakte |
| "Off Course Alarm" | Alle | Kursabweichung > Grenzwert | Normal bei starkem Seegang, sonst Regelungsproblem |
| "Sealevel Cal Required" | Raymarine | Kompass-Kalibrierung erforderlich | Nach Update, nach Standortwechsel |
| "NAC Communication Error" | B&G/Simrad | Verbindung zum NAC-Computer unterbrochen | NMEA2000-Bus, Stecker, Backbone |
| "Shadow Drive Active" | Garmin | Manuelles Eingreifen erkannt | Normaler Betrieb (Information) |
| "Heading Sensor Timeout" | Furuno | Kein Heading-Signal innerhalb Timeout | PG-700 Kabel, NMEA-Verbindung |
| "Clutch Error" | Verschiedene | Kupplung kann nicht betaetigt werden | Stecker, Kupplungsspule, Spannung |
| "Pump Running Continuously" | Hydraulik | Pumpe laeuft ohne Unterbrechung | Leckage, defektes Ventil, Luft |
| "Calibration Lost" | Verschiedene | Kalibrierungsdaten verloren | Backup-Batterie leer, Firmware-Fehler |

**Allgemeines Diagnosevorgehen bei Fehlermeldungen:**
1. Fehlermeldung exakt notieren (Wortlaut, Code-Nummer)
2. Im Hersteller-Handbuch nachschlagen (Fehlerliste)
3. Fehlerspeicher auslesen (falls verfuegbar)
4. Begleitumstaende dokumentieren (Seegang, Temperatur, andere Geraete)
5. Basis-Checks: Spannung, Stecker, Kabel
6. Herstellerspezifische Diagnoseroutine anwenden
7. Bei persistentem Fehler: Herstellersupport kontaktieren

### Fehlerbild 6: Stromspitzen und Sicherungsausloesung

**Symptom:** Der Autopilot loest regelmaessig oder sporadisch die Versorgungssicherung aus, oder es werden ungewoehnlich hohe Stroeme gemessen.

**Haeufigkeit:** 8 % aller Autopilot-Servicefaelle (Confidence: benchmark)

**Moegliche Ursachen:**

| Rang | Ursache | Haeufigkeit | Pruefung |
|------|---------|------------|----------|
| 1 | Schwergaengige Rudermechanik | 30 % | Ruder manuell pruefen, Drehmoment messen |
| 2 | Zu kleine Sicherung | 20 % | Sicherungswert vs. Spitzenstrom pruefen |
| 3 | Motorwicklungsschaden | 15 % | Isolationswiderstand, Wicklungswiderstand |
| 4 | Hydraulische Blockade | 12 % | Druckpruefen, Ventile inspizieren |
| 5 | Korrodierte Kabelverbindungen | 10 % | Uebergangswiderstand messen |
| 6 | Zu langer/duenner Kabelquerschnitt | 8 % | Spannungsabfall messen |
| 7 | Elektronikdefekt (Leistungsstufe) | 5 % | Oszilloskop-Pruefung |

**Diagnoseschritte:**
1. Tatsaechlichen Spitzenstrom mit Amperezange messen (Ruder hart BB → hart StB)
2. Ergebnis mit Hersteller-Spezifikation vergleichen
3. Sicherungswert pruefen (muss >Spitzenstrom sein, Typ: traege Schmelzsicherung)
4. Spannungsabfall auf der Zuleitung messen (Soll: <3 % bei Spitzenstrom)
5. Rudergaengigkeit pruefen (Ruder manuell bewegen, Widerstand fuehlen)
6. Motorstrom im Leerlauf messen (ohne Ruderlast) — erhoehter Leerlaufstrom = Motorproblem
7. Bei Hydraulik: Systemdruck pruefen (zu hoch = verstopfter Ruecklauf)

### Fehlerbild 6b: Sicherungsausloesung — Detailanalyse nach Antriebstyp

**Spezifische Stromaufnahme-Richtwerte fuer Diagnose (Confidence: measured):**

| Antriebstyp | Leerlaufstrom (Soll) | Leerlauf erhoent = | Normalstrom (Soll) | Spitzenstrom (Soll) | Sicherungstyp |
|-------------|---------------------|--------------------|-------------------|--------------------| --------------|
| Tillerpilot ST2000 | 0,2 A | Motor/Getriebe | 2–3 A | 6 A | 10 A traege |
| Raymarine Type 1 Linear | 0,5 A | Motor/Spindel | 4–6 A | 12 A | 20 A traege |
| Raymarine Type 2 Linear | 0,6 A | Motor/Spindel | 6–9 A | 20 A | 30 A traege |
| B&G SD10 Linear | 0,4 A | Motor/Getriebe | 3–5 A | 10 A | 15 A traege |
| B&G SD12 Linear | 0,5 A | Motor/Getriebe | 5–8 A | 18 A | 25 A traege |
| Raymarine Type 1 Pumpe | 0,5 A | Pumpe/Lager | 8–12 A | 25 A | 40 A traege |
| Raymarine Type 2 Pumpe | 0,5 A | Pumpe/Lager | 12–18 A | 35 A | 50 A traege |
| B&G RPU80 | 0,5 A | Pumpe/Lager | 8–12 A | 25 A | 40 A traege |
| B&G RPU160 | 0,6 A | Pumpe/Lager | 12–20 A | 40 A | 60 A traege |
| Garmin GHP 12 | 0,4 A | Pumpe/Lager | 8–14 A | 28 A | 40 A traege |
| Garmin GHP 20 | 0,5 A | Pumpe/Lager | 14–22 A | 45 A | 60 A traege |

**Pruefprotokoll Stromspitzen (systematisch):**

| Schritt | Pruefung | Messung | Bewertung |
|---------|----------|---------|-----------|
| 1 | Ruhestrom (Pilot aus, Elektronik ein) | Amperezange auf Versorgung | Soll: <0,3 A (Elektronik-Standby) |
| 2 | Leerlaufstrom (Pilot ein, keine Last) | Amperezange | Soll: siehe Tabelle oben |
| 3 | Betriebsstrom (Kursaenderung 10°) | Amperezange, Peak-Hold | Soll: Normalstrom-Bereich |
| 4 | Spitzenstrom (Ruder hart BB → StB) | Amperezange, Peak-Hold | Soll: siehe Tabelle oben |
| 5 | Dauerstrom bei Seegang | Mittelwert ueber 5 min | Soll: <50 % des Nennstroms im Mittel |
| 6 | Spannungsabfall unter Last | Multimeter an Antrieb vs. Batterie | Soll: <3 % Nennspannung |

**Haeufige Fehlerbilder im Zusammenhang mit Stromspitzen:**

| Konstellation | Wahrscheinliche Diagnose | Dringlichkeit |
|--------------|------------------------|---------------|
| Leerlaufstrom normal, Spitzenstrom zu hoch | Schwergaengiges Ruder, Hydraulikblockade | HOCH |
| Leerlaufstrom erhoent, Normalbetrieb erhoent | Motorproblem (Lager, Buersten, Wicklung) | MITTEL |
| Sporadische Spitzen ohne mechanische Korrelation | Elektronikdefekt (Leistungsstufe) | MITTEL |
| Strom normal, aber Sicherung loest trotzdem aus | Falsche Sicherung, Sicherungsalterung | NIEDRIG |
| Alle Stroeme normal, aber Batterie entlaedt schnell | Kriechstrom anderer Verbraucher, Batteriedefekt | PRUEFEN |

### Fehlerbild 7: Ruder laeuft bis Anschlag (Rudder Runaway)

**Symptom:** Das Ruder faehrt unkontrolliert bis zum mechanischen Anschlag. Dies ist ein sicherheitskritischer Zustand.

**Haeufigkeit:** 3 % aller Servicefaelle, aber HOHE Kritikalitaet (Confidence: benchmark)

**Moegliche Ursachen:**

| Ursache | Haeufigkeit | Sofortmassnahme |
|---------|------------|-----------------|
| Ruderlagesensor-Ausfall | 35 % | Autopilot sofort deaktivieren |
| Kabelbruch Ruderfeedback | 25 % | System stromlos machen |
| Software-Absturz / Lockup | 15 % | Sicherung ziehen |
| Leistungsstufe durchlegiert (MOSFET) | 10 % | Sicherung ziehen, Kupplung loesen |
| Endlagenschalter defekt | 10 % | Manuell eingreifen |
| EMV-Stoerung (selten) | 5 % | Stoerquelle identifizieren |

> **SICHERHEITSHINWEIS:** Rudder Runaway erfordert sofortiges Eingreifen! Der Autopilot muss unverzueglich deaktiviert und die manuelle Steuerung uebernommen werden. Im Extremfall Sicherung ziehen und Kupplung loesen. Nach einem Runaway-Ereignis: System erst nach Fehlerbehebung wieder in Betrieb nehmen.

### Fehlerbild 8: Autopilot reagiert nicht auf Kurseingaben

**Symptom:** Der Autopilot ist aktiv, reagiert aber nicht auf Kursaenderungsbefehle von der Bedieneinheit.

**Haeufigkeit:** 7 % aller Servicefaelle (Confidence: benchmark)

**Moegliche Ursachen:**

| Ursache | Haeufigkeit | Pruefung |
|---------|------------|----------|
| Bedieneinheit-Defekt | 30 % | Zweite Bedieneinheit testen (falls vorhanden) |
| NMEA2000-Bus-Problem | 25 % | Bus-Status pruefen, Terminierung |
| Kommunikationsfehler Controller↔Computer | 20 % | Fehlermeldungen, Kabelverbindungen |
| System im Standby (nicht aktiv) | 10 % | Status pruefen — wirklich im AUTO-Modus? |
| Software-Freeze | 10 % | System aus/ein (Power-Cycle) |
| Tasten-Defekt | 5 % | Taster-Funktionstest, Kontaktwiderstand |

### Fehlerbild 9: Oszillierendes Steuern (Hunting/Pendeln)

**Symptom:** Der Autopilot steuert den Kurs nicht stabil, sondern pendelt um den Sollkurs hin und her.

**Haeufigkeit:** 14 % aller Servicefaelle (Confidence: benchmark)

**Ursachen und Abstufung:**

| Oszillationstyp | Frequenz | Typische Ursache | Loesung |
|----------------|----------|-----------------|---------|
| Langsames Pendeln (>30 s Periode) | Niedrig | I-Anteil zu hoch, Trim-Problem | I-Anteil reduzieren, Auto-Trim pruefen |
| Mittleres Pendeln (5–30 s) | Mittel | P-Anteil zu hoch | Rudder Gain / P-Anteil reduzieren |
| Schnelles Pendeln (<5 s) | Hoch | D-Anteil zu niedrig, Spiel im Antrieb | D-Anteil erhoehen, mechanisches Spiel beheben |
| Asymmetrisches Pendeln | Variabel | Ruderlagesensor dejustiert | Sensor kalibrieren, Offset pruefen |
| Seegangsabhaengig | Variabel | Seegangsfilter/Response zu empfindlich | Response-Level erhoehen (weniger aggressiv) |

### Fehlerbild 10: Erhoehter Energieverbrauch

**Symptom:** Der Autopilot verbraucht deutlich mehr Strom als ueblich, Batterien werden schneller entladen.

**Haeufigkeit:** 6 % aller Servicefaelle (Confidence: benchmark)

**Moegliche Ursachen:**

| Ursache | Symptom | Pruefung |
|---------|--------|----------|
| Schwergaengiges Ruder | Hoher Durchschnittsstrom | Rudergaengigkeit manuell testen |
| Zu aggressives Steuern (PID) | Staendige Korrekturen | Steuerverhalten beobachten, Response-Level erhoehen |
| Luft in Hydraulik | Pumpe laeuft haeufig | Entlueftung durchfuehren |
| Interner Bypass (Hydraulik) | Pumpe laeuft fast kontinuierlich | Druckaufbau messen |
| Verschlissene Lager/Getriebe | Erhoehter Leerlaufstrom | Motorstrom ohne Last messen |
| Reibung im Antriebsstrang | Progressiv ansteigend | Schmierung, Alignment pruefen |
| Dauerhaft aktiver Clutch-Strom | Ruhestrom erhoehter | Clutch-Strom messen |

### Fehlerbild 11: Autopilot schaltet sich selbst ab

**Symptom:** Der Autopilot schaltet waehrend des Betriebs unvorhergesehen ab und gibt die Steuerung frei.

**Haeufigkeit:** 9 % aller Servicefaelle (Confidence: benchmark)

**Moegliche Ursachen:**

| Ursache | Haeufigkeit | Pruefung |
|---------|------------|----------|
| Unterspannung (transient) | 35 % | Spannungsverlauf mit Logger aufzeichnen |
| Off-Course-Alarm → Sicherheitsabschaltung | 20 % | Alarm-Einstellungen pruefen |
| Ueberstrom → Sicherheitsabschaltung | 15 % | Stromaufnahme messen |
| Ueberhitzung Antrieb | 10 % | Oberflaechentemperatur, Lueftung pruefen |
| Loser Steckverbinder (Wackelkontakt) | 10 % | Alle Stecker pruefen und sichern |
| Software-Absturz | 5 % | Firmware-Update, Fehlerspeicher |
| Shadow Drive Fehlausloesung (Garmin) | 5 % | Shadow Drive Empfindlichkeit einstellen |

### Fehlerbild 11b: Abschaltereignis — Spannungsverlauf-Analyse

**Typische Spannungsprofile bei Autopilot-Abschaltung (Confidence: measured):**

Zur Diagnose intermittierender Abschaltungen ist ein Spannungsdatenlogger unverzichtbar. Folgende Profile sind charakteristisch:

| Profil | Spannungsverlauf | Diagnose | Massnahme |
|--------|-----------------|----------|-----------|
| Kurzer Einbruch (<100 ms) auf <10 V | Spike-artig, schnelle Erholung | Grosser Verbraucher schaltet ein (Winde, Bugstrahlruder) | Getrennter Versorgungskreis, groessere Batterie |
| Langsamer Abfall (>5 s) unter 10,5 V | Rampenfoermig abfallend | Batterie erschoepft oder Ladestrom zu gering | Batterie laden/tauschen, Ladeanlage pruefen |
| Periodische Einbrueche (alle 30–60 s) | Regelmaessige Muster | Defekter Laderegler, Lichtmaschinen-Pulsation | Laderegler pruefen, Pufferkondensator |
| Einbruch nur bei Pilot-Aktivierung | Steiler Abfall beim Motorstart des Piloten | Zuleitungswiderstand zu hoch | Kabelquerschnitt erhoehen, Kontakte reinigen |
| Noisy (HF-Rippel >1 Vpp) | Hochfrequente Schwankungen | Wechselrichter, LED-Treiber, DC-DC-Wandler | EMV-Filter, Ferritkerne, Abstand |

**Empfohlene Datenlogger fuer Borddiagnose:**

| Geraet | Abtastrate | Aufloesung | Speicher | Preis (ca.) |
|--------|-----------|-----------|---------|-------------|
| Victron SmartShunt | 1 Hz | 10 mV | Bluetooth-App | 80 EUR |
| Simarine Pico | 1 Hz | 1 mV | Intern + App | 250 EUR |
| USB-Oszilloskop (z.B. Hantek 6022) | 48 MSa/s | <1 mV | PC-basiert | 50 EUR |
| Marinco Digital Logger | 0,1 Hz | 10 mV | SD-Karte | 120 EUR |
| Multimeter mit MIN/MAX-Aufzeichnung | Manuell | 1 mV | Intern | 30–80 EUR |

### Fehlerbild 12: Kompass-Interferenz durch Bordelektrik

**Symptom:** Der Autopilot zeigt erratische Kursanzeigen oder Kurssprünge, die mit dem Schalten anderer Verbraucher korrelieren.

**Haeufigkeit:** 5 % aller Servicefaelle (Confidence: benchmark)

**Typische Stoerquellen:**

| Stoerquelle | Stoercharakteristik | Loesung |
|-------------|-------------------|---------|
| Elektrische Winschen | Kurssprung bei Betrieb | Abstand, Kabel verdrillen, Ferritkerne |
| Bugstrahlruder | Starke Stoerung waehrend Betrieb | Akzeptieren (kurze Dauer), Pilot vorher deaktivieren |
| Wechselrichter | Dauerhaftes HF-Rauschen | Abstand, geschirmte Kabel, Netzfilter |
| VHF-Funkgeraet (Senden) | Kurssprung beim Senden | Abstand Antenne/Kompass, Ferritkerne |
| LED-Beleuchtung | Hochfrequente Stoerung | LED-Treiber mit EMV-Filter |
| Ankerwinde | Kurssprung bei Betrieb | Abstand, kurze Einsatzdauer |
| Lichtmaschine | Stoerung abhaengig von Drehzahl | Entstoerkondensator an Lichtmaschine |

---

## 7. Troubleshooting-Entscheidungsbaeume

### 7.1 Entscheidungsbaum: Autopilot laesst sich nicht aktivieren

```
START: Autopilot laesst sich nicht aktivieren
│
├─ Ist das Display/die Bedieneinheit eingeschaltet?
│   ├─ NEIN → Stromversorgung pruefen
│   │   ├─ Sicherung OK?
│   │   │   ├─ NEIN → Sicherung tauschen, Ursache suchen
│   │   │   └─ JA → Spannung am Geraet messen
│   │   │       ├─ 0V → Kabelbruch, Schalter defekt
│   │   │       ├─ <10,5V (12V) / <21V (24V) → Batterie laden, Kabel pruefen
│   │   │       └─ OK → Geraet defekt (Fachbetrieb)
│   │   │
│   └─ JA → Fehlermeldung angezeigt?
│       ├─ JA → Fehlermeldung notieren
│       │   ├─ "No Compass" → Kompass-Kabel und -Stromversorgung pruefen
│       │   ├─ "No Rudder FB" → Ruderlagesensor-Kabel pruefen
│       │   ├─ "Drive Error" → Antrieb/Kupplung/Kabel pruefen
│       │   ├─ "Calibration Required" → Kalibrierung durchfuehren
│       │   └─ Andere → Im Handbuch nachschlagen
│       │
│       └─ NEIN → Reagiert auf Tastendruck?
│           ├─ NEIN → Bedieneinheit defekt oder Bus-Problem
│           │   ├─ NMEA2000-Bus-Status pruefen
│           │   ├─ Andere Geraete am Bus funktional?
│           │   │   ├─ NEIN → Bus-Problem (Backbone, Terminierung)
│           │   │   └─ JA → Controller/Verbindung zum Computer pruefen
│           │   │
│           └─ JA, aber Pilot aktiviert nicht
│               ├─ Kupplung hoerbar?
│               │   ├─ NEIN → Kupplungsstrom pruefen (Abschnitt 6, FB 1)
│               │   └─ JA → Ruder bewegt sich?
│               │       ├─ NEIN → Antrieb pruefen (Motor, Pumpe, Mechanik)
│               │       └─ JA → System funktional, Bedienungsproblem?
│               │
└─ ENDE
```

### 7.2 Entscheidungsbaum: Kurs wird nicht gehalten

```
START: Autopilot aktiv, aber Kurs wird nicht gehalten
│
├─ Art der Kursabweichung?
│
├── Langsame, einseitige Drift
│    ├─ Drift immer in gleiche Richtung?
│    │   ├─ JA → Kompass-Deviation pruefen
│    │   │   ├─ Handpeilkompass-Vergleich: Abweichung >5°?
│    │   │   │   ├─ JA → Neukalibrierung durchfuehren
│    │   │   │   │   ├─ Nach Kalibrierung <5°? → OK, beobachten
│    │   │   │   │   └─ Nach Kalibrierung >5°? → Stoerquelle finden, Sonde umsetzen
│    │   │   │   └─ NEIN → Auto-Trim / I-Anteil pruefen
│    │   │   │       ├─ Trim-Funktion aktiviert? → Erhoehen
│    │   │   │       └─ Trim aktiv, aber unwirksam → Ruderlage-Offset pruefen
│    │   │   │
│    │   └─ NEIN (wechselnd) → Adaptions-Parameter zuruecksetzen
│    │       └─ Lernfahrt durchfuehren (~30 min)
│    │
├── Oszillation / Pendeln
│    ├─ Periode messen (Timer)
│    │   ├─ >30 Sekunden → I-Anteil / Trim reduzieren
│    │   ├─ 5–30 Sekunden → P-Anteil / Rudder Gain reduzieren
│    │   └─ <5 Sekunden → D-Anteil / Damping erhoehen
│    │       ODER: Mechanisches Spiel pruefen
│    │       ├─ Spiel gefunden → Gelenke, Kupplung, Ruderanlage reparieren
│    │       └─ Kein Spiel → Sea State / Response erhoehen
│    │
├── Plotzliche Kurssprünge
│    ├─ Korrelation mit Bordsystemen? (Winschen, Funk, etc.)
│    │   ├─ JA → EMV-Problem (Abschnitt 6, FB 12)
│    │   └─ NEIN → Kompass-Sonde pruefen
│    │       ├─ Lose Befestigung? → Nachbefestigen
│    │       ├─ Kabel locker/gequetscht? → Reparieren
│    │       └─ Kein mechanisches Problem → Sensordefekt moeglich
│    │
└── Kein Ruderausschlag trotz Abweichung
     ├─ Kupplungsfunktion pruefen (siehe Baum 7.1)
     ├─ Hydraulik: Oelstand, Pumpe laeuft? Leckage?
     └─ Linear: Motor laeuft? Endlage erreicht?
│
└─ ENDE
```

### 7.3 Entscheidungsbaum: Hydraulik-Probleme

```
START: Hydraulik-Autopilot funktioniert nicht korrekt
│
├─ Symptom identifizieren:
│
├── Pumpe laeuft, aber Ruder bewegt sich nicht
│    ├─ Oelstand OK?
│    │   ├─ NEIN → Oel nachfuellen, Leckage suchen
│    │   └─ JA → Luft im System?
│    │       ├─ Oel milchig/schaumig → JA, Entlueftung durchfuehren
│    │       └─ Oel klar → Interner Bypass?
│    │           ├─ Ueberdruckventil pruefen (oeffnet zu frueh?)
│    │           ├─ Rueckschlagventil undicht?
│    │           └─ Zylinderdichtung defekt (interner Bypass)
│    │               → Dichtungssatz tauschen
│    │
├── Pumpe laeuft nicht
│    ├─ Spannung an Pumpe messen
│    │   ├─ 0V → Kabel, Sicherung, Relais, Steuereinheit pruefen
│    │   ├─ <10V → Kabelquerschnitt / Kontakte pruefen
│    │   └─ OK → Motor defekt
│    │       ├─ Widerstand Motorwicklung messen
│    │       │   ├─ 0 Ohm → Kurzschluss → Motor tauschen
│    │       │   ├─ ∞ Ohm → Unterbrechung → Buersten/Motor tauschen
│    │       │   └─ Im Sollbereich → Mechanische Blockade in Pumpe
│    │       │       → Pumpe oeffnen (Fachbetrieb)
│    │
├── Pumpe laeuft kontinuierlich
│    ├─ Oelstand sinkt?
│    │   ├─ JA → Externe Leckage!
│    │   │   ├─ Alle Verschraubungen und Schlaeuche inspizieren
│    │   │   ├─ Zylinder-Kolbenstange auf Oelfilm pruefen
│    │   │   └─ Leckage reparieren, System entlueften, Oel nachfuellen
│    │   └─ NEIN → Interne Leckage (Bypass)
│    │       ├─ Zylinderkolben-Dichtung defekt → Dichtungssatz tauschen
│    │       └─ Ventil defekt → Ventil pruefen/tauschen
│    │
├── Langsame Ruderreaktion
│    ├─ Oelviskositaet korrekt? (Temperatureinfluss)
│    ├─ Oel verschmutzt / alt?
│    ├─ Luft im System (teilweise)?
│    └─ Pumpenleistung nachgelassen → Zahnradverschleiss
│
└── Geraeusche aus dem Hydrauliksystem
     ├─ Pfeifen → Luft angesaugt (Saugseitige Undichtigkeit)
     ├─ Heulen → Kavitation (Oelstand zu niedrig, Saugfilter verstopft)
     ├─ Klopfen → Ueberdruckventil oeffnet, Druckspitzen
     └─ Brummen → Normal bei Last, pruefen ob Halterung vibriert
│
└─ ENDE
```

### 7.4 Entscheidungsbaum: Elektronik- und Kommunikationsprobleme

```
START: Elektronik-/Kommunikationsproblem
│
├─ Symptom identifizieren:
│
├── Kein NMEA2000-Daten empfangen
│    ├─ Andere Geraete am Bus funktionieren?
│    │   ├─ NEIN → Bus-Infrastruktur pruefen
│    │   │   ├─ Terminierungswiderstaende (2 × 120 Ohm) vorhanden?
│    │   │   ├─ Backbone-Spannung messen (9–16V DC)
│    │   │   ├─ Backbone-Kabel und T-Stuecke pruefen
│    │   │   └─ LEN (Load Equivalence Number) pruefen: Summe < Netzteil-Kapazitaet?
│    │   └─ JA → Autopilot-spezifisch
│    │       ├─ NMEA2000-Stecker am Autopilot pruefen
│    │       ├─ PGN-Konfiguration pruefen (sendet/empfaengt richtige PGNs?)
│    │       ├─ Geraete-Instanz pruefen (Konflikt?)
│    │       └─ Firmware-Kompatibilitaet pruefen
│    │
├── Intermittierende Kommunikationsausfaelle
│    ├─ Korrelation mit Vibration/Seegang?
│    │   ├─ JA → Wackelkontakt in Steckverbindung
│    │   │   └─ Alle Stecker nacheinander pruefen (Wackeln unter Betrieb)
│    │   └─ NEIN → Korrelation mit bestimmten Verbrauchern?
│    │       ├─ JA → EMV-Problem, Stoerquelle entstoeren
│    │       └─ NEIN → Bus-Auslastung pruefen
│    │           ├─ Zu viele Geraete am Bus
│    │           └─ Defektes Geraet sendet Muell-Daten (Bus-Flooding)
│    │               → Geraete einzeln ab-/anstecken zum Isolieren
│    │
├── Firmware-Update fehlgeschlagen
│    ├─ Geraet reagiert noch?
│    │   ├─ JA → Update nochmals versuchen (stabile Stromversorgung!)
│    │   └─ NEIN → Geraet "gebrickt"
│    │       ├─ Recovery-Modus vorhanden? (Herstellerdokumentation)
│    │       │   ├─ JA → Recovery-Prozedur durchfuehren
│    │       │   └─ NEIN → Einschicken an Hersteller/Servicebetrieb
│    │
└── Display zeigt falsche Daten an
     ├─ Alle Daten falsch → Kompass/Sensor pruefen
     ├─ Nur bestimmte Daten falsch → Datenquelle und PGN pruefen
     └─ Sporadisch falsche Daten → Bus-Integritaet, EMV
│
└─ ENDE
```

### 7.5 Entscheidungsbaum: Linearantrieb-Probleme

```
START: Linearantrieb funktioniert nicht korrekt
│
├─ Symptom identifizieren:
│
├── Motor laeuft nicht
│    ├─ Spannung am Motor messen (bei Aktivierung)
│    │   ├─ 0V → Steuereinheit, Kabel, Sicherung pruefen
│    │   ├─ <10V → Spannungsabfall auf Zuleitung (Querschnitt!)
│    │   └─ OK → Motor defekt
│    │       ├─ Motor blockiert? → Getriebe pruefen (Fremdkoerper, Bruch)
│    │       ├─ Kohlebuersten verschlissen? → Buersten tauschen
│    │       └─ Wicklung defekt → Motor tauschen
│    │
├── Motor laeuft, aber kein Hub
│    ├─ Kupplung pruefen (greift?)
│    ├─ Getriebe pruefen (Zahnradbruch, Riemenriss?)
│    ├─ Spindelmutter verschlissen (durchdrehen)?
│    └─ Gelenkkopf ausgehaengt?
│    │
├── Motor laeuft, aber zu langsam
│    ├─ Spannung am Motor unter Last messen
│    │   ├─ Niedrig → Spannungsversorgung/Kabel
│    │   └─ OK → Mechanik schwergaengig
│    │       ├─ Ruder schwergaengig → Ruderanlage warten
│    │       ├─ Getriebe trocken → Nachschmieren
│    │       └─ Lager verschlissen → Lager tauschen
│    │
├── Klappern / Spiel
│    ├─ Gelenkkopf pruefen (Kugelgelenk-Spiel)
│    ├─ Befestigungsbolzen pruefen (Splint, Spiel)
│    ├─ Getriebe-Zahnspiel pruefen
│    └─ Spindelmutter-Spiel pruefen
│    │
├── Endlage wird nicht erkannt
│    ├─ Endlagenschalter mechanisch pruefen
│    ├─ Endlagenschalter elektrisch pruefen (Durchgang)
│    ├─ Einstellung der Endlagen im Controller pruefen
│    └─ Ruderlagesensor kalibrieren
│    │
└── Erhoehte Lautstaerke
     ├─ Getriebe → Zahnspiel, Schmierung
     ├─ Motor → Kohlebuersten, Lager
     ├─ Spindel → Schmierung
     └─ Gehaeuse → Resonanz, Befestigung nachziehen
│
└─ ENDE
```

---

## 8. FAQ

### 8.1 Allgemeine Wartungsfragen

**F1: Wie oft sollte ein Autopilot gewartet werden?**
A: Mindestens einmal jaehrlich, idealerweise zur Saisoneroeffnung. Hydraulik-Systeme benoetigen zusaetzlich monatliche Oelstands- und Leckagekontrollen. Bei intensiver Nutzung (>1.000 h/Jahr oder Charterboot) sind halbjaehrliche Inspektionen empfohlen. (Confidence: documented)

**F2: Kann ich die Autopilot-Wartung selbst durchfuehren?**
A: Viele Wartungsarbeiten (Sichtpruefung, Schmierung, Oelstand, Stecker-Reinigung) sind vom Eigner durchfuehrbar. Fuer Oelwechsel, Dichtungstausch, Pumpenuberholung und Elektronik-Diagnose wird ein Fachbetrieb empfohlen. Die Wartungsmatrix in Kapitel 3 zeigt die erforderliche Fachkenntnis pro Massnahme. (Confidence: documented)

**F3: Was kostet eine professionelle Autopilot-Wartung?**
A: Eine jaehrliche Inspektion durch einen Fachbetrieb kostet typisch 150–350 EUR (Arbeitszeit). Hinzu kommen ggf. Materialkosten (Oel: 20–50 EUR, Dichtungen: 50–100 EUR). Ein Komplett-Service (Fuenfjahres-Wartung) liegt bei 400–900 EUR plus Material. (Confidence: estimated)

**F4: Wie lange haelt ein Autopilot?**
A: Bei regelmaessiger Wartung 12–18 Jahre, ohne Wartung 4–7 Jahre. Die Elektronik ist meist langlebiger als die Mechanik/Hydraulik. Entscheidend ist die Umgebung (Feuchtigkeit, Salzluft) und die Nutzungsintensitaet. (Confidence: benchmark)

**F5: Mein Autopilot ist 15 Jahre alt. Lohnt sich eine Reparatur?**
A: Dies haengt vom System und vom Schaden ab. Pruefpunkte: (1) Gibt es noch Ersatzteile? (2) Gibt es noch Firmware-Support? (3) Uebersteigen die Reparaturkosten 50 % des Neupreises eines Ersatzsystems? Wenn ja, ist ein Upgrade oft wirtschaftlicher — und bringt bessere Sensorik, Algorithmen und Integration. (Confidence: estimated)

### 8.2 Hydraulik-Fragen

**F6: Welches Hydraulikoel soll ich verwenden?**
A: Ausschliesslich das vom Hersteller vorgeschriebene Oel. Raymarine und Furuno verwenden Dexron III ATF, B&G/Simrad empfehlen ISO VG 15, Garmin hat ein Eigenprodukt. Mischen ist unzulaessig. Die vollstaendige Tabelle findet sich in Abschnitt 2.2.3. (Confidence: documented)

**F7: Wie oft muss das Hydraulikoel gewechselt werden?**
A: Alle 2–3 Jahre oder 2.000 Betriebsstunden, je nachdem was zuerst eintritt. Bei Verfaerbung (trueb, milchig, dunkel) sofort wechseln. In tropischen Regionen mit hoher Luftfeuchtigkeit ggf. jaehrlich. (Confidence: documented)

**F8: Wie entluette ich mein Hydrauliksystem korrekt?**
A: Entlueftungsventil am hoechsten Punkt des Systems oeffnen. Pumpe kurz laufen lassen (manuell oder per Autopilot-Tasten). Ventil schliessen wenn blasenfreies Oel austritt. Vorgang ggf. 3–5 mal wiederholen. Oelstand nachfuellen. Alternativ: Vakuumentlueftung (professionell). (Confidence: documented)

**F9: Mein Hydraulikoel ist milchig. Was bedeutet das?**
A: Milchiges Oel zeigt Wassergehalt an (Emulsion). Ursachen: Kondensation bei langen Standzeiten, defekte Dichtung, Kondenswasser ueber Entlueftungsventil. Massnahme: Kompletter Oelwechsel, Ursache der Wassereindringung beheben. (Confidence: documented)

**F10: Kann ich statt Dexron III auch Dexron VI verwenden?**
A: Dexron VI ist rueckwaertskompatibel zu Dexron III in den meisten Anwendungen. ABER: Pruefen Sie die Herstellerfreigabe fuer Ihr spezifisches System. Einige aeltere Dichtungsmaterialien vertragen die veraenderten Additive nicht. Im Zweifelsfall: Beim Hersteller nachfragen. (Confidence: estimated)

### 8.3 Kompass- und Kalibrierungsfragen

**F11: Wie oft muss der Kompass kalibriert werden?**
A: Mindestens einmal pro Saison, sowie nach: Einbau neuer Elektronik, Aenderungen an der Bordausstattung nahe der Sonde, Standortwechsel (z.B. Atlantikueberquerung), Firmware-Update des Kompasses, auffaelliger Kursabweichung. (Confidence: documented)

**F12: Bei welchen Bedingungen soll ich kalibrieren?**
A: Ruhiges Wasser (Hafen oder geschuetztes Revier), wenig Strom, wenig Wind. Motor laeuft auf Leerlaufdrehzahl. Alle Bordsysteme einschalten, die normalerweise waehrend der Fahrt laufen. Zwei volle Kreise mit gleichmaessiger Geschwindigkeit (2–3 kn). (Confidence: documented)

**F13: Mein Kompass zeigt 10° Abweichung. Ist das noch akzeptabel?**
A: Nein. Nach Kalibrierung sollte die Restdeviation <5° auf allen Kursen betragen. 10° Deviation fuehrt zu deutlich erhoehtem Energieverbrauch (staendige Korrekturen) und ungenauem Kurs. Neukalibrierung und ggf. Umpositionierung der Sonde erforderlich. (Confidence: documented)

**F14: Mein Stahlboot hat massive Kompassprobleme. Was tun?**
A: Bei Stahlbooten empfiehlt sich: (1) Fluxgate-Sonde am Masttopp oder an einem Ausleger montieren. (2) Alternativ: GPS-Kompass (Dual-Antenna) verwenden — unempfindlich gegen Magnetfelder. (3) Rate-Gyro-stuetzung nutzen (reduziert Magnetfeld-Einfluss kurzfristig). (Confidence: documented)

### 8.4 Software- und Elektronikfragen

**F15: Soll ich jedes Firmware-Update installieren?**
A: Nicht zwingend. Release Notes lesen: Sicherheits-Updates und Bugfixes zeitnah installieren. Feature-Updates nur, wenn die neuen Funktionen benoetigt werden oder bekannte Probleme behoben werden. "Never change a running system" gilt teilweise — aber veraltete Firmware kann Kompatibilitaetsprobleme verursachen. (Confidence: documented)

**F16: Mein Autopilot hat sich nach einem Update verstellt. Was tun?**
A: (1) Einstellungen zuruecksetzen (Werkseinstellung). (2) Alle Kalibrierungen neu durchfuehren (Kompass, Ruderlage). (3) Lernphase des adaptiven Algorithmus abwarten (~30 min Fahrt). (4) Wenn nicht behoben: Downgrade auf vorherige Firmware (falls vom Hersteller unterstuetzt). (Confidence: documented)

**F17: Wie sichere ich meine Autopilot-Einstellungen?**
A: Herstellerabhaengig. Raymarine: Screenshot/Foto der Einstellungsseiten. B&G/Simrad: Settings Export ueber MFD. Garmin: ActiveCaptain Cloud-Backup. Furuno: Manuell notieren. Generell: Alle PID-Parameter, Kalibrierungswerte und Alarm-Einstellungen vor jedem Update dokumentieren. (Confidence: documented)

**F18: Mein NMEA2000-Netzwerk hat Probleme seit dem Autopilot-Einbau.**
A: Haeufige Ursachen: (1) LEN-Ueberschreitung (zu viele Geraete fuer das Netzteil). (2) Fehlende oder doppelte Terminierung. (3) Backbone zu lang (max. 100 m). (4) Stichleitungen zu lang (max. 6 m). (5) Inkompatible Firmware-Versionen. Pruefung mit NMEA2000-Diagnose-Tool empfohlen. (Confidence: documented)

### 8.5 Mechanik- und Antriebsfragen

**F19: Mein Linearantrieb klackert. Ist das gefaehrlich?**
A: Klackern deutet auf Spiel hin (Gelenkkopf, Befestigung, Getriebe). Es fuehrt zu unpraezierer Steuerung und verschlimmert sich ohne Massnahme. Nicht akut gefaehrlich, aber zeitnah beheben. Gelenkkopf-Spiel >1 mm oder hoerbares Klackern = sofortige Inspektion. (Confidence: estimated)

**F20: Wie oft muss der Zahnriemen am Wheel-Drive gewechselt werden?**
A: Alle 3–5 Jahre praeventiv, unabhaengig vom Zustand. Bei sichtbaren Rissen, Flankenabrieb oder Spanndehnung >2 % sofort. Kosten: 15–40 EUR fuer den Riemen, 30–60 Minuten Arbeitszeit. (Confidence: documented)

**F21: Mein Autopilot braucht mehr Strom als frueher. Woran liegt das?**
A: Haeufigste Ursachen in Reihenfolge: (1) Schwergaengiges Ruder (Lager, Stopfbuchse, Bewuchs). (2) Luft in Hydraulik. (3) Verschlissene Getriebeteile. (4) Aggressive PID-Einstellung. (5) Mangelnde Schmierung. Messung: Durchschnittsstrom ueber 10 Minuten ruhiger Fahrt aufzeichnen und mit Herstellerangabe vergleichen. (Confidence: estimated)

**F22: Kann ich einen Linearantrieb durch einen Hydraulikantrieb ersetzen?**
A: Ja, grundsaetzlich moeglich, aber aufwaendig. Vorteile: Hoehere Leistung, laengere Lebensdauer, leiser. Nachteile: Hoehere Kosten, mehr Platzbedarf, Oelwartung. Empfehlung: Ab ca. 12 m Bootlaenge oder bei hohen Ruderkraeften (Langkiel, schweres Displacement) auf Hydraulik umstellen. (Confidence: estimated)

### 8.6 Sicherheits- und Notfallfragen

**F23: Mein Autopilot faellt mitten auf See aus. Was tun?**
A: (1) Ruhe bewahren, manuelle Steuerung uebernehmen. (2) System stromlos machen (Sicherung ziehen). (3) Kupplung loesen / Freilauf aktivieren. (4) 30 Sekunden warten, System wieder einschalten. (5) Wenn Fehler persistiert: Manuelle Steuerung bis zum naechsten Hafen. (6) Basis-Diagnose (Spannung, Stecker) nur wenn Situation es erlaubt. (Confidence: documented)

**F24: Kann ein Autopilot-Ausfall gefaehrlich werden?**
A: Ja, insbesondere fuer Einhandsegler oder bei schweren Wetterbedingungen. Risiken: Unkontrollierte Kursaenderung, Patenthalse (Segelboot), Ermuedung durch langes manuelles Steuern. Praevention: Regelmaessige Wartung, Notfallplan fuer manuelles Steuern, Ruderbandsel bereithalten, Wachplan einhalten. (Confidence: documented)

**F25: Sollte ich ein Backup-Steuersystem haben?**
A: Fuer Langfahrten und Offshore-Segeln dringend empfohlen. Optionen: (1) Windfahnensteuerung als vollstaendig unabhaengiges Backup. (2) Zweiter elektronischer Autopilot (anderer Hersteller fuer maximale Redundanz). (3) Tillerpilot als Notfall-Backup (auch bei Radsteuerung, ueber Notpinne). (4) Ruderbandsel fuer Grundstabilisierung. (Confidence: documented)

**F26: Wie teste ich, ob mein Autopilot im Notfall schnell deaktivierbar ist?**
A: Regelmaessig ueben! (1) Standby-Taste druecken — Pilot muss sofort deaktivieren. (2) Steuerrad drehen (bei Shadow Drive / Override) — Pilot muss sofort freigeben. (3) Sicherung ziehen — Ruder muss manuell steuerbar sein (Kupplung oeffnet stromlos). (4) Bei Hydraulik: Bypass-Ventil betaetigen. Diesen Test zu Saisonbeginn und vor jeder laengeren Fahrt durchfuehren. (Confidence: documented)

**F27: Mein Autopilot hat einen Rudder Runaway verursacht. Was muss ich pruefen?**
A: (1) System sofort deaktivieren und stromlos machen. (2) Ruderlagesensor und Kabel inspizieren (haeufigste Ursache). (3) Endlagenschalter pruefen. (4) Motor/Leistungsstufe pruefen (durchlegierter MOSFET). (5) Fehlerspeicher auslesen. (6) System erst nach definitiver Ursachenbehebuung wieder in Betrieb nehmen. Herstellersupport kontaktieren. (Confidence: documented)

### 8.7 Einkaufs- und Upgrade-Fragen

**F28: Wann lohnt sich ein Autopilot-Upgrade?**
A: Wenn: (1) Ersatzteile nicht mehr verfuegbar. (2) Firmware-Support eingestellt (EOL). (3) Reparaturkosten >50 % Neupreis. (4) Kompatibilitaetsprobleme mit neuer Bordelektronik. (5) Wesentliche Verbesserungen bei Regelguete/Energieverbrauch aktueller Modelle. Typisch nach 10–15 Jahren sinnvoll. (Confidence: estimated)

**F29: Kann ich Komponenten verschiedener Hersteller mischen?**
A: Eingeschraenkt. Ueber NMEA 2000 sind verschiedene Hersteller kombinierbar (z.B. Garmin-MFD mit B&G-Autopilot). Aber: Antrieb und Steuereinheit muessen vom gleichen Hersteller sein. Kompass und Ruderlagesensor: Herstellerempfehlung beachten. Mischsysteme erhoehen die Komplexitaet der Fehlersuche erheblich. (Confidence: documented)

**F30: Was kostet ein komplettes Autopilot-System?**
A: Richtwerte (Confidence: benchmark): Tillerpilot einfach: 500–1.200 EUR. Wheel-Drive: 1.500–3.000 EUR. Linear-System (Segelboot 10–14 m): 2.500–5.000 EUR. Hydraulik-System (Motor/Segel 12–18 m): 4.000–8.000 EUR. Hydraulik-System (18+ m): 6.000–15.000 EUR. Einbau durch Fachbetrieb: 800–2.500 EUR zusaetzlich.

---

## 9. Glossar

| Nr. | Begriff | Erklaerung |
|-----|---------|-----------|
| 1 | **ACU** | Actuator Control Unit — Antriebssteuereinheit, steuert den Motor/die Pumpe |
| 2 | **AHRS** | Attitude and Heading Reference System — Lage- und Kursreferenzsystem (9-Achsen-Sensor) |
| 3 | **Adaptiver Algorithmus** | Software, die PID-Parameter automatisch an Boot und Bedingungen anpasst |
| 4 | **ATF** | Automatic Transmission Fluid — Automatikgetriebe-Oel, wird in vielen Hydraulik-Autopiloten verwendet |
| 5 | **Bias-Drift** | Langsame Aenderung des Nullpunktes eines Sensors (insbesondere Gyro) |
| 6 | **Bypass-Ventil** | Ventil zum Umgehen des Hydraulikzylinders fuer manuelle Steuerung |
| 7 | **CCU** | Course Computer Unit — Kursrechner (Garmin-Bezeichnung) |
| 8 | **Clutch (Kupplung)** | Mechanismus zum Trennen von Autopilot-Antrieb und Ruderanlage |
| 9 | **Continuum** | Adaptiver Steueralgorithmus von Navico (B&G, Simrad) |
| 10 | **Damping** | Daempfung — Einstellung zur Unterdrueckung von Regelschwingungen (D-Anteil) |
| 11 | **Deviation** | Ablenkung des Kompasses durch bordeigene Magnetfelder |
| 12 | **Dexron** | Markenname fuer ATF-Spezifikationen (GM), haeufig als Hydraulikoel im Autopilot |
| 13 | **Drive Stop** | Sicherheitsabschaltung des Antriebs bei Ueberstrom oder Fehler |
| 14 | **EMV** | Elektromagnetische Vertraeglichkeit — Faehigkeit elektronischer Geraete, stoerungsfrei nebeneinander zu arbeiten |
| 15 | **Endlagenschalter** | Schalter, der den Antrieb am mechanischen Ruderanschlag abschaltet |
| 16 | **EV-1** | Evolution Sensor Core — Raymarine AHRS-Sensoreinheit |
| 17 | **Fluxgate-Kompass** | Magnetischer Kompass-Sensor, misst die Erdmagnetfeldkomponenten |
| 18 | **Heading** | Steuerkurs — die Richtung, in die der Bug zeigt |
| 19 | **Hunting** | Pendeln des Autopiloten um den Sollkurs (Regelungsproblem) |
| 20 | **Hydraulikzylinder** | Wandelt Hydraulikdruck in lineare Kraft fuer die Ruderbewegung um |
| 21 | **I-Anteil** | Integralanteil des PID-Reglers — beseitigt bleibende Kursabweichung |
| 22 | **LEN** | Load Equivalence Number — Belastungskennzahl fuer NMEA2000-Geraete |
| 23 | **LVDT** | Linear Variable Differential Transformer — beruehrungsloser Wegsensor |
| 24 | **MEMS** | Micro-Electro-Mechanical Systems — Mikro-Sensortechnologie (Gyro, Beschleunigung) |
| 25 | **MTBF** | Mean Time Between Failures — mittlere Betriebsdauer zwischen Ausfaellen |
| 26 | **NAC** | Navigation Autopilot Computer — Autopilot-Rechner (Navico-Bezeichnung) |
| 27 | **NMEA 2000** | Standardisiertes Bord-Datennetzwerk (CAN-Bus basiert) |
| 28 | **Off-Course Alarm** | Warnung bei Ueberschreitung der zulaessigen Kursabweichung |
| 29 | **P-Anteil** | Proportionalanteil des PID-Reglers — Grundreaktionsstaerke |
| 30 | **PGN** | Parameter Group Number — Datentelegramm-Kennung im NMEA2000-Netz |
| 31 | **PID-Regler** | Proportional-Integral-Differential-Regler — Standard-Regelalgorithmus |
| 32 | **Rate Gyro** | Drehratensensor — misst die Drehgeschwindigkeit (°/s) |
| 33 | **Rudder Gain** | Verstaerkungsfaktor fuer Ruderausschlag (entspricht P-Anteil) |
| 34 | **Rudder Runaway** | Unkontrolliertes Laufen des Ruders bis zum Anschlag (Sicherheitsrisiko) |
| 35 | **Ruderlagesensor** | Sensor zur Messung der aktuellen Ruderposition (Ruderfeedback) |
| 36 | **Sea State** | Seegangsfilter-Einstellung — reduziert Reaktion auf Welleneinfluss |
| 37 | **SeaTalkng** | Raymarine-proprietaeres Netzwerkprotokoll (NMEA2000-kompatibel, anderer Stecker) |
| 38 | **Shadow Drive** | Garmin-Technologie zur nahtlosen manuellen Uebersteuerung |
| 39 | **Solenoid** | Magnetventil — elektrisch betaetigtes Hydraulikventil |
| 40 | **Spindelmutter** | Kunststoff-Mutter auf der Antriebsspindel eines Linearantriebs (Verschleissteil) |
| 41 | **Steer-by-Wire** | Elektronische Steuerung ohne mechanische Verbindung Steuerrad–Ruder |
| 42 | **Terminierung** | Abschlusswiderstand (120 Ohm) an den Enden eines NMEA2000-Backbone |
| 43 | **Trim** | Einstellung zur Kompensation dauerhafter Kursabweichung (I-Anteil) |
| 44 | **Ueberdruckventil** | Sicherheitsventil, das bei zu hohem Hydraulikdruck oeffnet |
| 45 | **Variation** | Missweisung — Differenz zwischen geographisch Nord und magnetisch Nord (ortsabhaengig) |

---

## 10. Schnell-Referenz

### 10.1 Wartungsintervall-Kurzuebersicht

| Intervall | Hydraulik | Linear | Wheel-Drive | Elektronik/Sensorik |
|-----------|---------|--------|-------------|-------------------|
| **Taeglich** (bei Nutzung) | Oelstand, Kursverhalten | Geraeusche, Kursverhalten | Kursverhalten | — |
| **Monatlich** | Leckage, Schlaeuche, Oelfarbe | Gelenkkoepfe, Befestigung | Riemenspannung, Reibrolle | — |
| **Vierteljährlich** | — | Spiel pruefen | Riemen, Kabel | — |
| **Halbjährlich** | — | Schmierung, Reinigung | Reinigung, Befestigung | — |
| **Jaehrlich** | Komplett-Inspektion, Stecker | Motorstrom, Endlagen, Stecker | Alignment, Stecker | Kalibrierung, Software |
| **Alle 2 Jahre** | Oelwechsel, Kalibrierung | Kohlebuersten, Fettpackung | — | — |
| **Alle 3 Jahre** | — | Getriebe-Inspektion | Riemen + Reibrolle tauschen | Komplett-Pruefung |
| **Alle 5 Jahre** | Dichtungen, Schlaeuche, Ueberdruckventil | — | — | — |

### 10.2 Notfall-Checkliste

```
┌─────────────────────────────────────────────────────────────┐
│              AUTOPILOT-NOTFALL-CHECKLISTE                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  □ 1. Ruhe bewahren, manuelle Steuerung uebernehmen        │
│  □ 2. Autopilot deaktivieren (Standby-Taste)                │
│  □ 3. Bei Nicht-Deaktivierung: Sicherung ziehen             │
│  □ 4. Kupplung manuell loesen (falls moeglich)              │
│  □ 5. Bei Hydraulik: Bypass-Ventil oeffnen                  │
│  □ 6. Ruder auf manuelle Steuerbarkeit pruefen              │
│  □ 7. Kurs sichern (Windfahne, Bandsel, Mannsteuerung)      │
│  □ 8. Lage beurteilen: Reparatur moeglich? Hafen ansteuern? │
│  □ 9. Bei Reparaturversuch: Spannung pruefen → Stecker      │
│  □ 10. System nur bei sicherer Funktion wieder aktivieren    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 10.3 Werkzeugliste fuer Autopilot-Wartung

| Werkzeug | Einsatz | Geschaetzte Kosten |
|----------|---------|-------------------|
| Multimeter (True RMS) | Spannungs-, Strom-, Widerstandsmessung | 30–80 EUR |
| Amperezange (DC) | Strommessung ohne Leitungstrennung | 40–120 EUR |
| Drehmomentschluessel (klein) | Verschraubungen Hydraulik | 30–60 EUR |
| Innensechskant-Satz (metrisch + zoll) | Diverse Schrauben | 15–30 EUR |
| Kontaktspray (Ballistol, WD-40 Contact) | Steckverbindungen | 8–12 EUR |
| Korrosionsschutzfett (z.B. Tef-Gel) | Edelstahl-Kontakte | 15–20 EUR |
| Marine-Getriebefett (PTFE) | Spindel, Gelenkkoepfe | 10–15 EUR |
| Bremsenreiniger | Reinigung Kupplungsflaechen, Riemen | 5–8 EUR |
| Taschenlampe (LED) | Sichtpruefung | 10–30 EUR |
| Inspektionsspiegel | Schwer zugaengliche Stellen | 5–10 EUR |
| Riemenspannungsmesser | Wheel-Drive Riemenspannung | 20–40 EUR |
| Fuehllehre | Spiel-Messung | 10–15 EUR |
| Absaugpumpe (Handpumpe) | Oelwechsel | 15–30 EUR |
| Auffangwanne | Oelwechsel | 5–10 EUR |
| Schrumpfschlauch-Set | Kabelreparatur | 10–15 EUR |
| Handpeilkompass | Deviationspruefung | 20–80 EUR |

### 10.4 Herstellerkontakte Schnell-Referenz

| Hersteller | Service-Telefon DACH | Service-E-Mail | Website |
|------------|---------------------|---------------|---------|
| Raymarine | +49 40 237 030 | service@raymarine.com | raymarine.com/support |
| B&G | +49 4122 717 70 | support@bandg.com | bandg.com/support |
| Garmin | +49 89 858 364 40 | marine.support@garmin.com | support.garmin.com |
| Simrad | +49 4122 717 70 | support@simrad-yachting.com | simrad-yachting.com/support |
| Furuno | +49 4101 838 80 | service@furuno.de | furuno.com/support |
| NKE | +33 2 97 36 58 62 | support@nke-marine.com | nke-marine-electronics.com |

---

## 11. ANHANG A–H — Fallstudien

### ANHANG A: Fallstudie — Hydraulik-Autopilot Komplettausfall auf Atlantikueberquerung

**Boot:** Bavaria 46 Cruiser, Baujahr 2016, Hydraulik-Autopilot Raymarine Evolution mit Type 1 Pumpe
**Situation:** Tag 8 der Atlantikueberquerung (ARC), 2-Personen-Crew, 800 sm westlich der Kanaren
**Symptom:** Ploetzlicher Verlust der Autopilot-Funktion. Display zeigt "Drive Stopped — Overcurrent"

**Diagnose an Bord:**
1. Sicherung 30 A war ausgeloest → Sicherung getauscht, erneut ausgeloest nach 10 Sekunden
2. Spannung am Pumpenmotor gemessen: 12,4 V (OK)
3. Motorstrom gemessen: >45 A (Soll: max. 25 A)
4. Pumpe mechanisch blockiert — Motor dreht sich nicht frei
5. Verdacht: Fremdkoerper oder Lagerschaden in der Pumpe

**Loesung an Bord:**
- Pumpe konnte nicht repariert werden (kein Ersatz an Bord)
- Backup-Tillerpilot (Raymarine ST2000+) ueber Notpinne installiert
- Restliche 2.100 sm mit Tillerpilot und manueller Steuerung bewaeltigt
- Tillerpilot bei >25 kn Wind ueberfordert → manuelle Steuerung in 4-Stunden-Wachen

**Ursache (Werftdiagnose in Martinique):**
- Lagernadel aus dem Pumpen-Axiallager gebrochen und im Zahnrad-Eingriff verklemmt
- Ursache: Korrosion am Lager durch Wasser im Hydraulikoel
- Oel bei Inspektion: stark getrubt, Wassergehalt 2,8 % (Soll: <0,1 %)
- Letzer Oelwechsel: nie (9 Jahre, ~3.000 Betriebsstunden)

**Kosten:** Neue Pumpe 1.650 EUR, Einbau 380 EUR, neues Oel 25 EUR, Zylinder-Dichtungssatz praeventiv 55 EUR. Gesamt: 2.110 EUR

**Lektion:** Regelmaessiger Oelwechsel (alle 2–3 Jahre) haette den Ausfall wahrscheinlich verhindert. Kosten der Praevention: ~120 EUR (6 × 20 EUR Oel ueber 9 Jahre). Backup-System obligatorisch fuer Langfahrt.

---

### ANHANG B: Fallstudie — Kompass-Deviation nach Winscheneinbau

**Boot:** Hallberg-Rassy 40, Baujahr 2019, B&G NAC-3 mit Precision-9 Kompass
**Situation:** Nach Einbau elektrischer Harken-Winschen (2 × Harken 50.2STE) ploetzlich 12° Kompass-Deviation auf Nordkursen

**Symptom:** Autopilot steuerte auf Nordkursen deutlich nach Osten versetzt. Auf Suedkursen kaum merkliche Abweichung.

**Diagnose:**
1. Handpeilkompass-Vergleich ergab: Deviation auf N = +12°, auf S = –2°, auf E/W = ±4–6°
2. Deviationskurve typisch fuer Harteisen-Stoerung (A/B-Koeffizienten)
3. Precision-9 Kompass war unter dem Cockpitboden montiert, 0,6 m unter den neuen Winschen
4. Harken-Winschen enthalten starke Permanentmagnete in den Elektromotoren
5. Neukalibrierung reduzierte Deviation auf max. 8° — immer noch zu hoch

**Loesung:**
1. Precision-9 Kompass umgesetzt: vom Cockpitboden nach achtern unter den Heckstaukasten (1,5 m von Winschen entfernt)
2. Neukalibrierung durchgefuehrt (2 Kreise bei ruhiger See)
3. Restdeviation nach Umsetzung: max. 2° auf allen Kursen

**Kosten:** Umsetzung Kompass (Eigenleistung): 3 h Arbeit. Neues Kabel: 45 EUR. Kalibrierfahrt: 1 h.

**Lektion:** Mindestabstaende fuer Fluxgate-Kompasse MUESSEN bei jedem Einbau neuer Elektronik geprueft werden. Elektrische Winschen enthalten starke Magnete und sind eine der haeufigsten Stoerquellen.

---

### ANHANG C: Fallstudie — Linearantrieb-Verschleiss bei Charteryacht

**Boot:** Jeanneau Sun Odyssey 440, Baujahr 2020, Raymarine Evolution mit Linear Drive Type 1
**Situation:** Charteryacht in Griechenland, 1.200 h/Saison, 4 Saisons im Einsatz
**Symptom:** Zunehmend lauteres Klappern im Antrieb, verzoegertes Ansprechverhalten, gelegentlicher "Rudder Feedback Error"

**Diagnose:**
1. Gelenkkopf am Ruderquadranten: deutliches Spiel (>3 mm)
2. Getriebespiel messbar (Leerlaufwinkel: 4°, Soll: <1°)
3. Spindelmutter: sichtbare Abnutzung, Kunststoff-Spuren im Fett
4. Ruderlagesensor (Potentiometer): Widerstand sprunghaft bei bestimmten Positionen
5. Motorstrom: Leerlauf 2,1 A (Soll: 1,5 A), unter Last 14 A (Soll: 10 A)

**Loesung:**
1. Gelenkkoepfe getauscht: 2 × 35 EUR
2. Spindelmutter getauscht: 55 EUR
3. Getriebeinspektion: Zahnraeder innerhalb Toleranz, neu gefettet
4. Ruderlagesensor getauscht (auf Hall-Effekt-Typ upgegraded): 220 EUR
5. Komplett-Neukalibrierung
6. Motorstrom nach Reparatur: Leerlauf 1,4 A, unter Last 8 A

**Kosten:** Materialien 345 EUR, Arbeitszeit Fachbetrieb 4 h × 85 EUR = 340 EUR. Gesamt: 685 EUR

**Lektion:** Charteryachten mit hoher Nutzungsintensitaet benoetigen verstaerkte Wartung. 4.800 Betriebsstunden ohne Getriebe-/Spindelwartung ist zu lang. Empfehlung fuer Charter: Halbjaehrliche Inspektion.

---

### ANHANG D: Fallstudie — Software-Bug verursacht Kursschwankungen

**Boot:** Beneteau Oceanis 51.1, Baujahr 2021, B&G NAC-3, Firmware 5.2.1
**Situation:** Nach Firmware-Update von 5.1.3 auf 5.2.1 ploetzlich unregelmaessiges Steuerverhalten

**Symptom:** Autopilot steuerte bei ruhiger See zufriedenstellend, bei Seegang >0,5 m begann unkontrolliertes Pendeln (±15° Kursabweichung, 8-Sekunden-Periode). Vorher mit gleicher Hardware problemlos.

**Diagnose:**
1. Alle mechanischen Komponenten geprueft: OK
2. Kalibrierung durchgefuehrt: OK
3. PID-Parameter manuell angepasst: Verbesserung, aber nicht zufriedenstellend
4. B&G Technical Support kontaktiert
5. Bekannter Bug in Firmware 5.2.1: Seegangsfilter-Koeffizient fehlerhaft berechnet bei bestimmten Bootsprofilen (Deplacement > 12 t mit Spatenruder)

**Loesung:**
1. Firmware-Downgrade auf 5.1.3 → Problem sofort behoben
2. Firmware 5.2.3 (Bugfix) 4 Wochen spaeter verfuegbar
3. Update auf 5.2.3 → Problem dauerhaft behoben

**Kosten:** Zeitaufwand Eigenleistung: ~6 h Fehlersuche. Firmware-Update: kostenlos.

**Lektion:** (1) Vor Updates Release Notes lesen und Nutzerforen konsultieren. (2) Einstellungen vor Update dokumentieren. (3) Auf erste Erfahrungsberichte anderer Nutzer warten (2–4 Wochen). (4) Downgrade-Moeglichkeit sicherstellen.

---

### ANHANG E: Fallstudie — Rudder Runaway durch Kabeldefekt

**Boot:** Hanse 458, Baujahr 2018, Garmin GHP Reactor mit GHP 20 Pumpe
**Situation:** Nachtfahrt in der Aegaeis, Autopilot aktiv, alleinige Wache im Cockpit
**Symptom:** Ruder lief ploetzlich hart nach Backbord. Boot drehte scharf ab. Wachgaenger bemerkte die Drehung und drueckte Standby — keine Reaktion.

**Sofortmassnahme:**
1. Sicherung gezogen → Pumpe stoppte
2. Manuelle Steuerung uebernommen
3. Shadow Drive hatte nicht ausgeloest (Fehler im System)

**Diagnose (naechster Hafen):**
1. Ruderlagesensor-Kabel inspiziert: Kabel war im Bereich der Bilge durch Scheuern am GFK-Laminat beschaedigt
2. Isolierung aufgerieben, Kurzschluss der Signalleitung gegen Masse
3. Steuereinheit interpretierte Kurzschluss als "Ruder auf Steuerbord-Anschlag" → steuerte permanent nach Backbord
4. Shadow Drive Bypass-Ventil war verharzt und oeffnete nicht bei manuellem Drehen
5. Standby-Befehl erreichte CCU nicht (gleichzeitiger NMEA2000-Bus-Fehler durch Spannungstransient)

**Loesung:**
1. Ruderlagesensor-Kabel ersetzt (korrekte Kabelverlegung mit Schutzrohr)
2. Shadow Drive Ventil ausgebaut, gereinigt, Funktion getestet
3. NMEA2000-Bus: Lose Verbindung an T-Stueck gefunden und behoben
4. Komplett-Kalibrierung und Testfahrt

**Kosten:** Kabel und Schutzrohr: 60 EUR, Shadow Drive Service: 120 EUR Arbeitszeit. Gesamt: 180 EUR

**Lektion:** (1) Kabelverlegung ist sicherheitskritisch — Scheuerschutz an allen Durchfuehrungen! (2) Shadow Drive / Bypass regelmaessig testen. (3) Redundante Abschaltmoeglichkeit (Sicherung) muss jederzeit erreichbar sein. (4) NMEA2000-Verbindungen regelmaessig pruefen.

---

### ANHANG F: Fallstudie — Wheel-Drive Riemenriss bei Regatta

**Boot:** J/112E, Baujahr 2020, B&G WTP3 Wheel-Drive
**Situation:** Transatlantik-Regatta, Tag 5, Autopilot unter Dauerlast bei 20–25 kn Wind
**Symptom:** Ploetzlich kein Rudereinschlag mehr, Motor laeuft hoerbar, aber Steuerrad dreht nicht

**Diagnose an Bord:**
1. Wheel-Drive Gehaeuse geoeffnet: Zahnriemen gerissen
2. Riemen war original (2 Jahre, geschaetzt 1.800 h unter Last)
3. Flankenabrieb und Risse waren bei letzter Inspektion (3 Monate zuvor) nicht aufgefallen

**Loesung an Bord:**
1. Ersatzriemen war an Bord (Empfehlung des Riggers)
2. Riemenwechsel in 40 Minuten unter schwierigen Bedingungen (Seegang)
3. Funktion wiederhergestellt

**Kosten:** Ersatzriemen: 28 EUR

**Lektion:** (1) Ersatzriemen IMMER an Bord haben — 28 EUR Versicherung! (2) Bei Regatta-/Langfahrt-Vorbereitung: Riemen praeventiv tauschen. (3) 1.800 h unter Regatta-Last sind am oberen Ende der Lebensdauer. (4) Visueller Riemencheck allein reicht nicht — Dehnung messen!

---

### ANHANG G: Fallstudie — Intermittierende Ausfaelle durch Korrosion

**Boot:** Oyster 485, Baujahr 2014, Raymarine SPX-30 (aelteres System)
**Situation:** Seit 6 Monaten sporadische Autopilot-Ausfaelle, nicht reproduzierbar
**Symptom:** Autopilot schaltet sich zufaellig ab, manchmal laesst er sich sofort wieder aktivieren, manchmal erst nach Minuten. Keine konsistente Fehlermeldung.

**Diagnose (chronologisch):**
1. Alle Sicherungen und Schalter geprueft: OK
2. Spannungsversorgung mit Datenlogger ueberwacht (72 h): Keine Unterbrechnungen
3. Alle Steckverbindungen geoeffnet und inspiziert:
   - Hauptversorgungsstecker an der ACU: Pins 3 und 5 stark korrodiert (grüene Patina)
   - Übergangswiderstand an Pin 3: 4,7 Ohm (Soll: <0,05 Ohm)
   - Pin 3 = Kompass-Datenleitung (SeaTalk)
4. Korrosion durch Kondenswasser in nicht-IP-geschuetztem Stecker

**Loesung:**
1. Stecker gereinigt (Poliervlies, Kontaktspray)
2. Alle Stecker mit Korrosionsschutzfett behandelt
3. Stecker an ACU durch wasserdichten Stecker (IP67) ersetzt
4. Kabelkanal belueftet (Silicagel-Beutel)
5. Keine Ausfaelle mehr seit 8 Monaten

**Kosten:** IP67-Stecker: 22 EUR, Kontaktspray: 12 EUR, Korrosionsschutzfett: 18 EUR. Gesamt: 52 EUR

**Lektion:** Die haeufigste Ursache fuer intermittierende Ausfaelle sind korrodierte Steckverbindungen. Jaehrliche Inspektion und Schutzbehandlung kosten Minuten und verhindern stundenlange Fehlersuche.

---

### ANHANG H: Fallstudie — Autopilot-Upgrade von Legacy auf Modern

**Boot:** Hallberg-Rassy 36, Baujahr 2008, Alter Autopilot: Raymarine SmartPilot S3G mit ST6002
**Situation:** System 17 Jahre alt, zunehmend unreliable, keine Firmware-Updates mehr, Ersatzteile schwer beschaffbar

**Altes System:**
- SmartPilot S3G Computer (EOL seit 2018)
- ST6002 Controller (SeaTalk1, nicht NMEA2000)
- Type 1 Hydraulikpumpe (noch funktional)
- Fluxgate-Kompass (RF300, EOL)
- Ruderlagesensor (Potentiometer, abgenutzt)

**Neues System:**
- Raymarine Evolution EV-2 (EV-1 Sensor, ACU-150, p70s Controller)
- Bestehende Type 1 Hydraulikpumpe weiterverwendet
- Neuer Ruderlagesensor (E22078)
- NMEA2000-Netzwerk (SeaTalkng)

**Upgrade-Prozess:**
1. ACU-150 anstelle des S3G Computers montiert (gleiche Befestigungspunkte)
2. EV-1 Sensor an der Stelle des alten RF300 (andere Halterung, Adapter erforderlich)
3. p70s Controller anstelle des ST6002 (neuer Kabeldurchbruch erforderlich)
4. Ruderlagesensor getauscht
5. SeaTalkng-Backbone installiert (4 m, 2 T-Stuecke, 2 Terminatoren)
6. Hydraulikpumpe an ACU-150 angeschlossen (Kabeladapter)
7. Komplett-Kalibrierung, Testfahrt

**Ergebnis:**
- Deutlich bessere Kursregelung (Evolution Adaptive vs. alte PID-Konstanten)
- Halbierter Energieverbrauch (intelligentere Ansteuerung)
- Integration mit vorhandenem Garmin-MFD ueber NMEA2000
- Wind-Vane-Steuerung moeglich (mit Windgeber ueber NMEA2000)

**Kosten:** ACU-150: 890 EUR, EV-1: 480 EUR, p70s: 450 EUR, Ruderlagesensor: 220 EUR, Kabel/Stecker/Backbone: 180 EUR. Material gesamt: 2.220 EUR. Einbau (Eigenleistung mit Unterstuetzung): ~12 h. Alternativ Fachbetrieb: 800–1.200 EUR.

**Lektion:** (1) Hydraulikpumpe ist oft das langlebigste Bauteil — Weiterverwendung spart erheblich. (2) Upgrade lohnt sich, wenn EOL erreicht ist. (3) Migration auf NMEA2000 oeffnet Integrations-Moeglichkeiten. (4) Gesamtkosten eines Upgrades sind oft geringer als wiederholte Reparaturen am Altsystem.

---

## 12. ANHANG I–R — Pydantic v2 Modelle

### ANHANG I: AutopilotSystem — Basis-Datenmodell

```python
"""
AYDI Autopilot System Pydantic v2 Models
Wissensdatei: 21_05_autopilot_wartung.md

German UI text, English code.
All models use Pydantic v2 with model_config = {"from_attributes": True}.
NEVER use class Config.
"""

from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, field_validator


# --- Enums ---

class AutopilotDriveType(str, Enum):
    """Autopilot drive type classification."""
    HYDRAULIC = "hydraulic"
    LINEAR = "linear"
    WHEEL_DRIVE = "wheel_drive"
    TILLER = "tiller"
    STEER_BY_WIRE = "steer_by_wire"


class AutopilotManufacturer(str, Enum):
    """Known autopilot manufacturers."""
    RAYMARINE = "raymarine"
    BG = "b_and_g"
    GARMIN = "garmin"
    SIMRAD = "simrad"
    FURUNO = "furuno"
    NKE = "nke"
    LECOMBLE_SCHMITT = "lecomble_schmitt"
    OTHER = "other"


class MaintenanceInterval(str, Enum):
    """Standard maintenance intervals."""
    DAILY = "daily"
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    SEMI_ANNUAL = "semi_annual"
    ANNUAL = "annual"
    BIENNIAL = "biennial"
    TRIENNIAL = "triennial"
    FIVE_YEAR = "five_year"
    ON_DEMAND = "on_demand"


class ConfidenceLevel(str, Enum):
    """AYDI confidence levels for analysis results."""
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
    """Severity levels for findings and faults."""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


class ComponentStatus(str, Enum):
    """Status of a component after inspection."""
    OK = "ok"
    ATTENTION = "attention"
    WARNING = "warning"
    REPLACE = "replace"
    FAILED = "failed"
    NOT_INSPECTED = "not_inspected"


class FaultCategory(str, Enum):
    """Fault category for troubleshooting."""
    MECHANICAL = "mechanical"
    HYDRAULIC = "hydraulic"
    ELECTRICAL = "electrical"
    ELECTRONIC = "electronic"
    SOFTWARE = "software"
    SENSOR = "sensor"
    COMMUNICATION = "communication"
    ENVIRONMENTAL = "environmental"


# --- Base Models ---

class AutopilotSystem(BaseModel):
    """Complete autopilot system description for a vessel."""

    model_config = {"from_attributes": True}

    system_id: str = Field(
        ...,
        description="Unique system identifier"
    )
    vessel_id: str = Field(
        ...,
        description="Reference to the vessel this system belongs to"
    )
    manufacturer: AutopilotManufacturer = Field(
        ...,
        description="Autopilot manufacturer"
    )
    model_name: str = Field(
        ...,
        description="Model name (e.g., 'Evolution EV-2', 'GHP Reactor 40')"
    )
    drive_type: AutopilotDriveType = Field(
        ...,
        description="Type of drive unit"
    )
    installation_date: Optional[date] = Field(
        None,
        description="Date of installation"
    )
    firmware_version: Optional[str] = Field(
        None,
        description="Current firmware version"
    )
    firmware_date: Optional[date] = Field(
        None,
        description="Date of last firmware update"
    )
    operating_voltage: int = Field(
        12,
        description="Nominal operating voltage (12 or 24 V DC)"
    )
    max_current_a: Optional[float] = Field(
        None,
        description="Maximum current draw in Amperes"
    )
    rudder_type: Optional[str] = Field(
        None,
        description="Rudder type (e.g., 'spade', 'skeg-hung', 'full-keel')"
    )
    compass_type: Optional[str] = Field(
        None,
        description="Compass sensor type (e.g., 'fluxgate', 'AHRS', 'GPS-compass')"
    )
    rudder_feedback_type: Optional[str] = Field(
        None,
        description="Rudder feedback sensor type (e.g., 'potentiometer', 'hall_effect', 'LVDT')"
    )
    nmea_protocol: Optional[str] = Field(
        None,
        description="Primary communication protocol (e.g., 'NMEA2000', 'SeaTalkng', 'NMEA0183')"
    )
    total_operating_hours: Optional[float] = Field(
        None,
        ge=0,
        description="Total operating hours since installation"
    )
    notes: Optional[str] = Field(
        None,
        description="Free-text notes about the system"
    )

    @field_validator("operating_voltage")
    @classmethod
    def validate_voltage(cls, v: int) -> int:
        if v not in (12, 24):
            raise ValueError("Operating voltage must be 12 or 24 V DC")
        return v
```

### ANHANG J: MaintenanceRecord — Wartungsprotokoll

```python
class MaintenanceTask(BaseModel):
    """A single maintenance task definition."""

    model_config = {"from_attributes": True}

    task_id: str = Field(
        ...,
        description="Unique task identifier"
    )
    name_de: str = Field(
        ...,
        description="Task name in German (user-facing)"
    )
    name_en: str = Field(
        ...,
        description="Task name in English (internal)"
    )
    description_de: str = Field(
        ...,
        description="Detailed task description in German"
    )
    drive_types: list[AutopilotDriveType] = Field(
        ...,
        description="Applicable drive types for this task"
    )
    interval: MaintenanceInterval = Field(
        ...,
        description="Recommended maintenance interval"
    )
    duration_minutes: int = Field(
        ...,
        ge=1,
        description="Estimated task duration in minutes"
    )
    skill_level: str = Field(
        ...,
        description="Required skill level: 'owner', 'advanced', 'professional'"
    )
    tools_required: list[str] = Field(
        default_factory=list,
        description="List of required tools"
    )
    materials_required: list[str] = Field(
        default_factory=list,
        description="List of required materials/consumables"
    )
    safety_notes_de: Optional[str] = Field(
        None,
        description="Safety notes in German"
    )


class MaintenanceRecord(BaseModel):
    """Record of a completed maintenance action."""

    model_config = {"from_attributes": True}

    record_id: str = Field(
        ...,
        description="Unique record identifier"
    )
    system_id: str = Field(
        ...,
        description="Reference to the autopilot system"
    )
    task_id: str = Field(
        ...,
        description="Reference to the maintenance task"
    )
    performed_date: date = Field(
        ...,
        description="Date the maintenance was performed"
    )
    performed_by: str = Field(
        ...,
        description="Name or identifier of person/company"
    )
    operating_hours_at_service: Optional[float] = Field(
        None,
        ge=0,
        description="Operating hours at time of service"
    )
    findings: list[str] = Field(
        default_factory=list,
        description="Findings during maintenance (German text)"
    )
    parts_replaced: list[str] = Field(
        default_factory=list,
        description="List of replaced parts (part numbers)"
    )
    cost_parts_eur: Optional[Decimal] = Field(
        None,
        ge=0,
        description="Cost of parts in EUR"
    )
    cost_labor_eur: Optional[Decimal] = Field(
        None,
        ge=0,
        description="Cost of labor in EUR"
    )
    next_service_date: Optional[date] = Field(
        None,
        description="Recommended date for next service"
    )
    next_service_hours: Optional[float] = Field(
        None,
        ge=0,
        description="Recommended operating hours for next service"
    )
    confidence: ConfidenceLevel = Field(
        ConfidenceLevel.DOCUMENTED,
        description="Confidence level of the record"
    )
    notes: Optional[str] = Field(
        None,
        description="Additional notes"
    )
```

### ANHANG K: FaultDiagnosis — Fehlerdiagnose-Modell

```python
class FaultSymptom(BaseModel):
    """A single observed symptom."""

    model_config = {"from_attributes": True}

    symptom_id: str = Field(
        ...,
        description="Unique symptom identifier"
    )
    description_de: str = Field(
        ...,
        description="Symptom description in German"
    )
    category: FaultCategory = Field(
        ...,
        description="Fault category"
    )
    severity: SeverityLevel = Field(
        ...,
        description="Severity of the symptom"
    )
    observed_date: Optional[datetime] = Field(
        None,
        description="When the symptom was first observed"
    )
    intermittent: bool = Field(
        False,
        description="Whether the symptom appears intermittently"
    )
    conditions: Optional[str] = Field(
        None,
        description="Conditions under which symptom appears (German)"
    )


class DiagnosticStep(BaseModel):
    """A single diagnostic step in a troubleshooting tree."""

    model_config = {"from_attributes": True}

    step_number: int = Field(
        ...,
        ge=1,
        description="Step number in sequence"
    )
    instruction_de: str = Field(
        ...,
        description="Diagnostic instruction in German"
    )
    expected_result: str = Field(
        ...,
        description="Expected result if component is OK"
    )
    measurement_tool: Optional[str] = Field(
        None,
        description="Tool needed for this step"
    )
    if_ok_goto: Optional[int] = Field(
        None,
        description="Next step if result is OK"
    )
    if_fail_goto: Optional[int] = Field(
        None,
        description="Next step if result indicates fault"
    )
    if_fail_diagnosis: Optional[str] = Field(
        None,
        description="Diagnosis if this step fails"
    )
    if_fail_action_de: Optional[str] = Field(
        None,
        description="Recommended action if this step fails (German)"
    )


class FaultDiagnosis(BaseModel):
    """Complete fault diagnosis record."""

    model_config = {"from_attributes": True}

    diagnosis_id: str = Field(
        ...,
        description="Unique diagnosis identifier"
    )
    system_id: str = Field(
        ...,
        description="Reference to the autopilot system"
    )
    symptoms: list[FaultSymptom] = Field(
        ...,
        min_length=1,
        description="Observed symptoms"
    )
    diagnostic_steps_performed: list[DiagnosticStep] = Field(
        default_factory=list,
        description="Diagnostic steps performed"
    )
    root_cause_de: Optional[str] = Field(
        None,
        description="Identified root cause in German"
    )
    root_cause_en: Optional[str] = Field(
        None,
        description="Identified root cause in English"
    )
    root_cause_category: Optional[FaultCategory] = Field(
        None,
        description="Category of the root cause"
    )
    resolution_de: Optional[str] = Field(
        None,
        description="Resolution description in German"
    )
    resolution_cost_eur: Optional[Decimal] = Field(
        None,
        ge=0,
        description="Total resolution cost in EUR"
    )
    confidence: ConfidenceLevel = Field(
        ConfidenceLevel.ESTIMATED,
        description="Confidence in the diagnosis"
    )
    diagnosed_date: Optional[datetime] = Field(
        None,
        description="Date of diagnosis"
    )
    diagnosed_by: Optional[str] = Field(
        None,
        description="Person or system that performed diagnosis"
    )
```

### ANHANG L: ComponentInspection — Komponenteninspektion

```python
class ComponentInspectionResult(BaseModel):
    """Result of inspecting a single component."""

    model_config = {"from_attributes": True}

    component_name_de: str = Field(
        ...,
        description="Component name in German"
    )
    component_name_en: str = Field(
        ...,
        description="Component name in English"
    )
    location: Optional[str] = Field(
        None,
        description="Physical location on the vessel"
    )
    status: ComponentStatus = Field(
        ...,
        description="Component status after inspection"
    )
    measured_value: Optional[float] = Field(
        None,
        description="Measured value (unit in measurement_unit)"
    )
    measurement_unit: Optional[str] = Field(
        None,
        description="Unit of measurement (e.g., 'ohm', 'V', 'A', 'mm', 'cSt')"
    )
    nominal_value_min: Optional[float] = Field(
        None,
        description="Minimum acceptable value"
    )
    nominal_value_max: Optional[float] = Field(
        None,
        description="Maximum acceptable value"
    )
    finding_de: Optional[str] = Field(
        None,
        description="Finding description in German"
    )
    recommendation_de: Optional[str] = Field(
        None,
        description="Recommendation in German"
    )
    photo_reference: Optional[str] = Field(
        None,
        description="Reference to inspection photo"
    )
    confidence: ConfidenceLevel = Field(
        ConfidenceLevel.MEASURED,
        description="Confidence level of measurement"
    )


class SystemInspection(BaseModel):
    """Complete system inspection record."""

    model_config = {"from_attributes": True}

    inspection_id: str = Field(
        ...,
        description="Unique inspection identifier"
    )
    system_id: str = Field(
        ...,
        description="Reference to the autopilot system"
    )
    inspection_date: date = Field(
        ...,
        description="Date of inspection"
    )
    inspector: str = Field(
        ...,
        description="Name or identifier of inspector"
    )
    inspection_type: str = Field(
        ...,
        description="Type of inspection: 'seasonal', 'annual', 'five_year', 'fault_finding'"
    )
    operating_hours: Optional[float] = Field(
        None,
        ge=0,
        description="Operating hours at time of inspection"
    )
    components: list[ComponentInspectionResult] = Field(
        ...,
        min_length=1,
        description="Individual component inspection results"
    )
    overall_status: ComponentStatus = Field(
        ...,
        description="Overall system status"
    )
    overall_finding_de: str = Field(
        ...,
        description="Overall finding summary in German"
    )
    recommended_actions_de: list[str] = Field(
        default_factory=list,
        description="Recommended actions in German"
    )
    next_inspection_date: Optional[date] = Field(
        None,
        description="Recommended date for next inspection"
    )
    confidence: ConfidenceLevel = Field(
        ConfidenceLevel.MEASURED,
        description="Overall confidence level"
    )
```

### ANHANG M: HydraulicOilAnalysis — Hydraulikoel-Analyse

```python
class HydraulicOilAnalysis(BaseModel):
    """Hydraulic oil analysis results."""

    model_config = {"from_attributes": True}

    analysis_id: str = Field(
        ...,
        description="Unique analysis identifier"
    )
    system_id: str = Field(
        ...,
        description="Reference to the autopilot system"
    )
    sample_date: date = Field(
        ...,
        description="Date the oil sample was taken"
    )
    oil_type: str = Field(
        ...,
        description="Oil specification (e.g., 'Dexron III ATF', 'ISO VG 15')"
    )
    oil_age_months: Optional[int] = Field(
        None,
        ge=0,
        description="Age of oil since last fill in months"
    )
    operating_hours_since_fill: Optional[float] = Field(
        None,
        ge=0,
        description="Operating hours since last oil fill"
    )
    viscosity_40c_cst: Optional[float] = Field(
        None,
        ge=0,
        description="Kinematic viscosity at 40°C in cSt"
    )
    water_content_ppm: Optional[int] = Field(
        None,
        ge=0,
        description="Water content in ppm (max 1000 acceptable)"
    )
    particle_class_iso4406: Optional[str] = Field(
        None,
        description="Particle class per ISO 4406 (e.g., '18/16/13')"
    )
    acid_number_mg_koh_g: Optional[float] = Field(
        None,
        ge=0,
        description="Total Acid Number (TAN) in mg KOH/g"
    )
    visual_appearance_de: str = Field(
        ...,
        description="Visual appearance description in German"
    )
    oil_color: str = Field(
        ...,
        description="Color description: 'clear_red', 'dark_red', 'brown', 'milky', 'black'"
    )
    status: ComponentStatus = Field(
        ...,
        description="Overall oil status"
    )
    recommendation_de: str = Field(
        ...,
        description="Recommendation in German"
    )
    confidence: ConfidenceLevel = Field(
        ConfidenceLevel.MEASURED,
        description="Confidence level"
    )

    @field_validator("water_content_ppm")
    @classmethod
    def flag_high_water(cls, v: Optional[int]) -> Optional[int]:
        """Flag if water content exceeds 1000 ppm."""
        # Validation only — flagging is done in the analysis engine
        return v
```

### ANHANG N: CompassCalibration — Kompass-Kalibrierung

```python
class DeviationReading(BaseModel):
    """Single compass deviation reading on a specific heading."""

    model_config = {"from_attributes": True}

    magnetic_heading_deg: int = Field(
        ...,
        ge=0,
        lt=360,
        description="Magnetic heading in degrees (0-359)"
    )
    compass_heading_deg: float = Field(
        ...,
        ge=0,
        lt=360,
        description="Autopilot compass reading in degrees"
    )
    deviation_deg: float = Field(
        ...,
        description="Deviation (compass - magnetic) in degrees"
    )
    reference_source: str = Field(
        ...,
        description="Reference source: 'hand_bearing_compass', 'transit', 'gps_cog', 'known_bearing'"
    )


class CompassCalibration(BaseModel):
    """Compass calibration record."""

    model_config = {"from_attributes": True}

    calibration_id: str = Field(
        ...,
        description="Unique calibration identifier"
    )
    system_id: str = Field(
        ...,
        description="Reference to the autopilot system"
    )
    calibration_date: date = Field(
        ...,
        description="Date of calibration"
    )
    calibration_type: str = Field(
        ...,
        description="Type: 'automatic_swing', 'manual_deviation_table', 'combined'"
    )
    location_name: Optional[str] = Field(
        None,
        description="Location where calibration was performed"
    )
    location_lat: Optional[float] = Field(
        None,
        ge=-90,
        le=90,
        description="Latitude of calibration location"
    )
    location_lon: Optional[float] = Field(
        None,
        ge=-180,
        le=180,
        description="Longitude of calibration location"
    )
    magnetic_variation_deg: Optional[float] = Field(
        None,
        description="Local magnetic variation in degrees"
    )
    sea_conditions_de: str = Field(
        ...,
        description="Sea conditions during calibration in German"
    )
    deviation_readings: list[DeviationReading] = Field(
        default_factory=list,
        description="Individual deviation readings"
    )
    max_residual_deviation_deg: Optional[float] = Field(
        None,
        ge=0,
        description="Maximum residual deviation after calibration in degrees"
    )
    calibration_quality: str = Field(
        ...,
        description="Quality rating: 'excellent' (<2°), 'good' (<5°), 'acceptable' (<8°), 'poor' (>=8°)"
    )
    systems_active_during_cal: list[str] = Field(
        default_factory=list,
        description="List of electrical systems active during calibration"
    )
    notes_de: Optional[str] = Field(
        None,
        description="Notes in German"
    )
    confidence: ConfidenceLevel = Field(
        ConfidenceLevel.MEASURED,
        description="Confidence level"
    )

    @field_validator("calibration_quality")
    @classmethod
    def validate_quality(cls, v: str) -> str:
        allowed = {"excellent", "good", "acceptable", "poor"}
        if v not in allowed:
            raise ValueError(f"calibration_quality must be one of {allowed}")
        return v
```

### ANHANG O: SparePart — Ersatzteil-Katalog

```python
class SparePart(BaseModel):
    """Spare part catalog entry."""

    model_config = {"from_attributes": True}

    part_id: str = Field(
        ...,
        description="Internal part identifier"
    )
    manufacturer: AutopilotManufacturer = Field(
        ...,
        description="Manufacturer"
    )
    manufacturer_part_number: str = Field(
        ...,
        description="Manufacturer's part number"
    )
    name_de: str = Field(
        ...,
        description="Part name in German"
    )
    name_en: str = Field(
        ...,
        description="Part name in English"
    )
    description_de: str = Field(
        ...,
        description="Part description in German"
    )
    compatible_systems: list[str] = Field(
        ...,
        description="List of compatible system model names"
    )
    category: str = Field(
        ...,
        description="Part category: 'seal_kit', 'sensor', 'pump', 'motor', 'controller', 'cable', 'consumable'"
    )
    price_eur: Optional[Decimal] = Field(
        None,
        ge=0,
        description="Approximate retail price in EUR"
    )
    replacement_interval: Optional[MaintenanceInterval] = Field(
        None,
        description="Recommended replacement interval"
    )
    replacement_interval_hours: Optional[int] = Field(
        None,
        ge=0,
        description="Recommended replacement interval in operating hours"
    )
    lead_time_days: Optional[int] = Field(
        None,
        ge=0,
        description="Typical delivery lead time in days"
    )
    availability: str = Field(
        "available",
        description="Availability: 'available', 'limited', 'discontinued', 'special_order'"
    )
    critical_spare: bool = Field(
        False,
        description="Whether this is recommended as a critical onboard spare"
    )
    weight_grams: Optional[int] = Field(
        None,
        ge=0,
        description="Weight in grams"
    )
    notes: Optional[str] = Field(
        None,
        description="Additional notes"
    )
```

### ANHANG P: FirmwareUpdate — Firmware-Update-Protokoll

```python
class FirmwareUpdate(BaseModel):
    """Firmware update record."""

    model_config = {"from_attributes": True}

    update_id: str = Field(
        ...,
        description="Unique update identifier"
    )
    system_id: str = Field(
        ...,
        description="Reference to the autopilot system"
    )
    component: str = Field(
        ...,
        description="Updated component: 'computer', 'sensor', 'drive_controller', 'display'"
    )
    firmware_version_before: str = Field(
        ...,
        description="Firmware version before update"
    )
    firmware_version_after: str = Field(
        ...,
        description="Firmware version after update"
    )
    update_date: date = Field(
        ...,
        description="Date of update"
    )
    update_method: str = Field(
        ...,
        description="Method: 'sd_card', 'usb', 'ethernet', 'wifi_ota', 'bluetooth'"
    )
    update_tool: Optional[str] = Field(
        None,
        description="Software tool used (e.g., 'LightHouse', 'ActiveCaptain', 'Garmin Express')"
    )
    recalibration_performed: bool = Field(
        False,
        description="Whether recalibration was performed after update"
    )
    adaptation_reset: bool = Field(
        False,
        description="Whether adaptive algorithm was reset"
    )
    test_drive_performed: bool = Field(
        False,
        description="Whether a test drive was performed after update"
    )
    issues_after_update_de: Optional[str] = Field(
        None,
        description="Any issues observed after update (German)"
    )
    rollback_performed: bool = Field(
        False,
        description="Whether a rollback to previous version was necessary"
    )
    settings_backup_made: bool = Field(
        False,
        description="Whether settings were backed up before update"
    )
    notes: Optional[str] = Field(
        None,
        description="Additional notes"
    )
```

### ANHANG Q: SeasonalChecklist — Saisonale Checkliste

```python
class ChecklistItem(BaseModel):
    """A single checklist item for seasonal procedures."""

    model_config = {"from_attributes": True}

    step_number: int = Field(
        ...,
        ge=1,
        description="Step number"
    )
    description_de: str = Field(
        ...,
        description="Step description in German"
    )
    description_en: str = Field(
        ...,
        description="Step description in English"
    )
    applicable_drive_types: list[AutopilotDriveType] = Field(
        default_factory=lambda: list(AutopilotDriveType),
        description="Applicable drive types (empty = all)"
    )
    check_method_de: str = Field(
        ...,
        description="How to perform the check (German)"
    )
    acceptance_criteria_de: str = Field(
        ...,
        description="What constitutes a pass (German)"
    )
    estimated_duration_minutes: int = Field(
        ...,
        ge=1,
        description="Estimated time in minutes"
    )
    completed: bool = Field(
        False,
        description="Whether this item has been completed"
    )
    completed_date: Optional[datetime] = Field(
        None,
        description="When this item was completed"
    )
    finding_de: Optional[str] = Field(
        None,
        description="Findings or notes (German)"
    )
    status: ComponentStatus = Field(
        ComponentStatus.NOT_INSPECTED,
        description="Result status"
    )


class SeasonalChecklist(BaseModel):
    """Complete seasonal checklist for commissioning or winterization."""

    model_config = {"from_attributes": True}

    checklist_id: str = Field(
        ...,
        description="Unique checklist identifier"
    )
    system_id: str = Field(
        ...,
        description="Reference to the autopilot system"
    )
    checklist_type: str = Field(
        ...,
        description="Type: 'spring_commissioning', 'winterization', 'mid_season'"
    )
    season_year: int = Field(
        ...,
        ge=2000,
        le=2100,
        description="Season year"
    )
    created_date: date = Field(
        ...,
        description="Date checklist was created"
    )
    completed_date: Optional[date] = Field(
        None,
        description="Date checklist was fully completed"
    )
    performed_by: str = Field(
        ...,
        description="Person performing the checks"
    )
    items: list[ChecklistItem] = Field(
        ...,
        min_length=1,
        description="Checklist items"
    )
    all_passed: bool = Field(
        False,
        description="Whether all items passed"
    )
    overall_notes_de: Optional[str] = Field(
        None,
        description="Overall notes in German"
    )

    @field_validator("checklist_type")
    @classmethod
    def validate_checklist_type(cls, v: str) -> str:
        allowed = {"spring_commissioning", "winterization", "mid_season"}
        if v not in allowed:
            raise ValueError(f"checklist_type must be one of {allowed}")
        return v
```

### ANHANG R: AutopilotAnalysisResult — AYDI Analyse-Ergebnis

```python
class AutopilotFinding(BaseModel):
    """A single finding from autopilot analysis."""

    model_config = {"from_attributes": True}

    finding_id: str = Field(
        ...,
        description="Unique finding identifier"
    )
    module: str = Field(
        "autopilot_maintenance",
        description="AYDI analysis module name"
    )
    zone: str = Field(
        ...,
        description="Vessel zone: 'helm_station', 'lazarette', 'engine_room', 'nav_station'"
    )
    category: FaultCategory = Field(
        ...,
        description="Finding category"
    )
    severity: SeverityLevel = Field(
        ...,
        description="Finding severity"
    )
    title_de: str = Field(
        ...,
        description="Finding title in German"
    )
    description_de: str = Field(
        ...,
        description="Detailed description in German"
    )
    suggestion_de: str = Field(
        ...,
        description="Suggested action in German (every finding must have a suggestion)"
    )
    location_reference: str = Field(
        ...,
        description="Location reference (e.g., 'Hydraulikzylinder am Ruderquadranten')"
    )
    confidence: ConfidenceLevel = Field(
        ...,
        description="Confidence level of this finding"
    )
    estimated_cost_eur: Optional[Decimal] = Field(
        None,
        ge=0,
        description="Estimated repair/maintenance cost in EUR"
    )
    photo_reference: Optional[str] = Field(
        None,
        description="Reference to supporting photo"
    )
    requires_human_review: bool = Field(
        False,
        description="Whether this finding requires human review ('Befund pruefen')"
    )


class AutopilotMaintenanceScore(BaseModel):
    """Score for autopilot maintenance condition."""

    model_config = {"from_attributes": True}

    overall_score: int = Field(
        ...,
        ge=0,
        le=100,
        description="Overall maintenance score (0-100)"
    )
    mechanical_score: int = Field(
        ...,
        ge=0,
        le=100,
        description="Mechanical condition score"
    )
    hydraulic_score: Optional[int] = Field(
        None,
        ge=0,
        le=100,
        description="Hydraulic system score (if applicable)"
    )
    electrical_score: int = Field(
        ...,
        ge=0,
        le=100,
        description="Electrical condition score"
    )
    sensor_score: int = Field(
        ...,
        ge=0,
        le=100,
        description="Sensor calibration and condition score"
    )
    software_score: int = Field(
        ...,
        ge=0,
        le=100,
        description="Software/firmware currency score"
    )
    documentation_score: int = Field(
        ...,
        ge=0,
        le=100,
        description="Maintenance documentation completeness score"
    )


class AutopilotAnalysisResult(BaseModel):
    """Complete AYDI analysis result for autopilot maintenance."""

    model_config = {"from_attributes": True}

    analysis_id: str = Field(
        ...,
        description="Unique analysis identifier"
    )
    system_id: str = Field(
        ...,
        description="Reference to the autopilot system"
    )
    vessel_id: str = Field(
        ...,
        description="Reference to the vessel"
    )
    analysis_date: datetime = Field(
        ...,
        description="Date and time of analysis"
    )
    analysis_level: str = Field(
        ...,
        description="AYDI analysis level: 'level_1_schnellanalyse', 'level_2_profi'"
    )
    pipeline: str = Field(
        ...,
        description="Analysis pipeline: 'structured', 'visual', 'text', 'combined'"
    )
    available: bool = Field(
        True,
        description="Whether analysis could produce a reliable result"
    )
    unavailable_reason: Optional[str] = Field(
        None,
        description="Reason if analysis is not available"
    )
    score: Optional[AutopilotMaintenanceScore] = Field(
        None,
        description="Maintenance condition scores"
    )
    findings: list[AutopilotFinding] = Field(
        default_factory=list,
        description="All findings from the analysis"
    )
    critical_findings_count: int = Field(
        0,
        ge=0,
        description="Number of critical findings"
    )
    recommended_next_maintenance_de: Optional[str] = Field(
        None,
        description="Recommendation for next maintenance in German"
    )
    estimated_total_maintenance_cost_eur: Optional[Decimal] = Field(
        None,
        ge=0,
        description="Estimated total cost for all recommended actions in EUR"
    )
    remaining_useful_life_hours: Optional[int] = Field(
        None,
        ge=0,
        description="Estimated remaining useful life in operating hours"
    )
    remaining_useful_life_years: Optional[float] = Field(
        None,
        ge=0,
        description="Estimated remaining useful life in years"
    )
    confidence: ConfidenceLevel = Field(
        ...,
        description="Overall confidence level of the analysis"
    )
    ai_model_version: str = Field(
        ...,
        description="Version of the AI model used for analysis"
    )
    knowledge_base_version: str = Field(
        "21_05_v1.0.0",
        description="Version of the knowledge base used"
    )

    @field_validator("analysis_level")
    @classmethod
    def validate_analysis_level(cls, v: str) -> str:
        allowed = {"level_1_schnellanalyse", "level_2_profi"}
        if v not in allowed:
            raise ValueError(f"analysis_level must be one of {allowed}")
        return v
```

---

> **Ende der Wissensdatei 21.05**
> Naechste geplante Aktualisierung: 2026-11-02
> Aenderungshistorie: v1.0.0 (2026-05-02) — Erstversion
