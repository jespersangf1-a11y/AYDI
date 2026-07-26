---
title: "Elektrik Wartung und Troubleshooting"
kategorie: "22 Elektrik"
unterkategorie: "12 Wartung und Troubleshooting"
version: "1.0.0"
datum: "2026-05-08"
autor: "AYDI Research"
status: "validated"
bereich: "Elektrik & Elektronik"
confidence_quellen:
  - measured: "Hersteller-TDS, Werkstattmessungen, Labordaten"
  - documented: "Hersteller-Kataloge, Service-Bulletins, ABYC E-11, ISO 13297"
  - estimated: "Erfahrungswerte Elektriker, Forum-Konsens, Werft-Statistiken"
  - benchmark: "Charterflotten-Analysen, Versicherungsdaten, Surveyor-Berichte"
tags:
  - elektrik
  - wartung
  - troubleshooting
  - multimeter
  - isolationsmessung
  - megger
  - thermografie
  - streustrom
  - batterietest
  - winterfestmachung
  - inbetriebnahme
  - fehlerdiagnose
  - spannungsabfall
  - korrosion
  - fluke
  - victron
  - marinco
cross_references:
  - "22_01_bordnetz_grundlagen.md"
  - "22_02_batterien.md"
  - "22_03_ladegeraete.md"
  - "22_04_wechselrichter.md"
  - "22_05_solarsysteme.md"
  - "22_06_kabel_und_leitungen.md"
  - "22_07_schalttafeln.md"
  - "22_08_beleuchtung.md"
  - "22_09_landstrom.md"
  - "22_10_galvanische_isolation.md"
  - "22_11_blitzschutz.md"
  - "07_06_opferanoden.md"
---

# 22.12 — Elektrik Wartung und Troubleshooting: Gesamtsystem-Inspektion, Messgeräte, Fehlersuche, Winterfestmachung

> **AYDI Wissensdatei 22.12** — Kategorie 22: Elektrik
> **Confidence-Quelle:** measured (Hersteller-TDS, Labordaten), documented (ABYC E-11, ISO 13297, Service-Bulletins), estimated (Erfahrungswerte)
> **Letzte Aktualisierung:** 2026-05-08

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
11. [Anhänge A–H — Fallstudien](#11-anhänge-ah--fallstudien)
12. [Anhänge I–R — Pydantic v2 Modelle](#12-anhänge-ir--pydantic-v2-modelle)

---

## 1. Einführung und Übersicht

### 1.1 Elektrik-Wartung als Sicherheitsmaßnahme

Die elektrische Anlage einer Yacht ist das zentrale Nervensystem des gesamten Schiffes. Sie versorgt Navigation, Kommunikation, Antrieb, Beleuchtung, Komfortsysteme und Sicherheitseinrichtungen. Ein Ausfall der Elektrik kann im schlimmsten Fall lebensbedrohlich sein — vom Verlust der Navigationsbeleuchtung bei Nacht über den Ausfall der Bilgenpumpe bei Wassereinbruch bis hin zu Kabelbränden durch Überhitzung.

Marine-Elektrik operiert unter extrem widrigen Bedingungen: permanente Salzluft-Exposition, hohe Luftfeuchtigkeit (oft >80 % rH), Vibrationen durch Motor und Seegang, Temperaturzyklen von -5 °C bis +65 °C im Motorraum, UV-Strahlung an Deck und galvanische Wechselwirkungen zwischen unterschiedlichen Metallen im Seewasser.

**Kernstatistiken zur Wartungsrelevanz (Confidence: benchmark):**

| Aspekt | Wert | Quelle |
|--------|------|--------|
| Anteil Elektrik an allen Yachtbränden | 55 % | BoatUS Marine Insurance Claim Report 2024 |
| Häufigste Brandursache | Überhitzte Kabelverbindungen (34 %) | NFPA Marine Fire Statistics |
| Streustrom-Schäden pro Jahr (Durchschnitt) | 3.200–8.500 EUR | Pantaenius Versicherungsdaten DACH |
| Anteil Elektrik-Ausfälle bei Seenotfällen | 22 % | BSH Seeunfall-Datenbank 2020–2024 |
| Durchschnittliche Lebensdauer Marinekabel (gut gewartet) | 20–30 Jahre | ABYC Technical Information Report |
| Durchschnittliche Lebensdauer Marinekabel (vernachlässigt) | 5–10 Jahre | Surveyor-Erfahrungswerte |
| Kosten einer vollständigen Neuverkabelung (12m SY) | 8.000–18.000 EUR | Werft-Kalkulationen DACH 2024/2025 |
| ROI einer jährlichen Elektrik-Inspektion | 15:1 bis 35:1 | Lebensdauervergleich |

### 1.2 Regulatorischer Rahmen

Die Elektrik-Wartung auf Yachten unterliegt einem umfassenden Regelwerk:

**Internationale und europäische Normen:**

| Norm | Titel | Relevanz für Wartung |
|------|-------|---------------------|
| ISO 13297:2021 | Elektrische Systeme — Gleichstrom | Kabelquerschnitte, Sicherungen, Installationsstandards |
| ISO 10133:2012 | Elektrische Systeme — Niederspannung DC | Extra-Niederspannung bis 50 V DC |
| ISO 13297:2021 | Elektrische Systeme — Wechselstrom | AC-Installation, Erdung, FI-Schutz |
| IEC 60092 | Elektrische Anlagen auf Schiffen | Professionelle Schifffahrt, teilw. anwendbar |
| EN 60529 | IP-Schutzarten | Mindestschutzklassen nach Zone |
| ABYC E-11 | AC & DC Electrical Systems | US-Standard, international anerkannt |
| ABYC E-2 | Cathodic Protection | Kathodischer Korrosionsschutz, Opferanoden, Referenzelektroden-Potentiale |
| ABYC TE-4 | Lightning Protection | Erweiterte Blitzschutz-Richtlinien |

**CE-Kategorie-spezifische Anforderungen:**

| Anforderung | Kat. A (Ocean) | Kat. B (Offshore) | Kat. C (Inshore) | Kat. D (Sheltered) |
|-------------|---------------|-------------------|-------------------|---------------------|
| Redundante Bilgenpumpen-Stromversorgung | Pflicht | Pflicht | Empfohlen | Optional |
| Wasserdichte Schalttafel | IP 66 | IP 56 | IP 44 | IP 22 |
| Batterie-Trennschalter zugänglich | < 1 m vom Steuerstand | < 2 m | < 3 m | Empfohlen |
| Navigationsbeleuchtung Backup | Pflicht (separate Batterie) | Pflicht | Empfohlen | Optional |
| Kabelführung Mindesth. über Bilge | 200 mm | 150 mm | 100 mm | 50 mm |

### 1.3 Kosten der Vernachlässigung

Die elektrische Anlage durchläuft bei Vernachlässigung typische Degradationsstufen:

**Stufe 1 — Schleichende Degradation (0–12 Monate ohne Inspektion):**
- Kontaktwiderstände an Klemmen steigen um 10–30 %
- Erste Grünspan-Bildung an ungeschützten Kupferkontakten
- Batterie-Innenwiderstand steigt um 5–15 %
- Spannungsabfall unter Last an schwachen Verbindungen messbar
- Geschätzter Wertverlust der Elektrik: 3–8 %

**Stufe 2 — Funktionseinschränkung (12–36 Monate ohne Inspektion):**
- Sicherungen lösen sporadisch aus (Übergangswiderstände)
- Korrosion an Masseverbindungen → Erdschleifen, Instrumentenstörungen
- Batterie-Kapazität auf 60–80 % gesunken
- Isolationswiderstände kritisch gesunken
- Erste Streustrom-Probleme messbar
- Geschätzter Wertverlust der Elektrik: 15–30 %

**Stufe 3 — Sicherheitsrelevante Defekte (36–60 Monate ohne Inspektion):**
- Kabelisolierungen spröde, Rissbildung
- Terminalkorrosion verursacht intermittierende Ausfälle
- Batterien können Startstrom nicht mehr zuverlässig liefern
- FI-Schutzschalter funktionsuntüchtig (nicht getestet)
- Brandgefahr durch überhitzte Verbindungen
- Geschätzter Wertverlust der Elektrik: 40–65 %

**Stufe 4 — Systemversagen (>60 Monate ohne Inspektion):**
- Kabelbäume müssen komplett erneuert werden
- Batterien tiefentladen, sulfatiert, irreversibel geschädigt
- Schalttafeln korrodiert, Kontaktflächen zerstört
- Brandrisiko akut — Versicherungsschutz gefährdet
- Geschätzter Wertverlust der Elektrik: 75–100 %

### 1.4 Wartungsphilosophie

Die AYDI-Elektrik-Wartungsphilosophie basiert auf vier Grundprinzipien:

1. **Messen statt Vermuten:** Jede Diagnose beginnt mit einer Messung. Sichtprüfung allein reicht nicht — ein Kabel kann äußerlich intakt erscheinen und innen gebrochen sein.
2. **Systematisch statt punktuell:** Die Gesamtanlage wird als System betrachtet. Ein Fehler in der Masseverbindung kann sich als Instrumentenstörung manifestieren.
3. **Dokumentiert und reproduzierbar:** Jede Messung wird mit Datum, Messwert, Messbedingung und Gerät protokolliert. Trendanalysen erkennen Degradation, bevor Ausfälle auftreten.
4. **Normkonform und herstellerspezifisch:** ABYC E-11 und ISO 13297 definieren die Mindeststandards. Herstellerangaben für spezifische Geräte haben Vorrang.

**Confidence-Bewertung dieses Abschnitts:**
- Statistiken: `benchmark` — aggregierte Branchendaten, Versicherungsstatistiken
- Degradationsstufen: `documented` — Surveyor-Berichte, Werft-Erfahrung
- Kostenangaben: `estimated` — AYDI-Kalkulation auf Basis von Marktpreisen 2024/2025
- Normentabelle: `measured` — offizielle Normtexte

---

## 2. Grundlagen und Theorie

### 2.1 Multimeter — Das universelle Diagnosewerkzeug

#### 2.1.1 Funktionsprinzip und Aufbau

Das digitale Multimeter (DMM) ist das grundlegende Messinstrument für die Elektrik-Diagnose an Bord. Es vereint mindestens drei Messfunktionen: Spannungsmessung (Voltmeter), Strommessung (Amperemeter) und Widerstandsmessung (Ohmmeter).

**Messprinzip Spannungsmessung (DC):**
Das DMM schaltet einen hochohmigen Eingangswiderstand (typisch 10 MΩ) parallel zur Messstrecke. Der durch den Eingangswiderstand fließende Strom ist proportional zur anliegenden Spannung. Ein Analog-Digital-Wandler (ADC) konvertiert das Signal in einen angezeigten Zahlenwert. Die hohe Eingangsimpedanz stellt sicher, dass die Messung den Stromkreis praktisch nicht belastet.

**Messprinzip Strommessung (DC):**
Das DMM wird in Reihe geschaltet und misst den Spannungsabfall über einen präzisen Shunt-Widerstand (Bürde). Der Spannungsabfall ist proportional zum durchfließenden Strom (Ohmsches Gesetz: U = I × R). Marine-Multimeter haben typische Messbereiche bis 10 A DC; für höhere Ströme wird ein Zangenamperemeter verwendet.

**Messprinzip Widerstandsmessung:**
Das DMM speist einen bekannten Strom durch die Messstrecke und misst den resultierenden Spannungsabfall. Der Widerstand ergibt sich aus R = U/I. Wichtig: Die Messung darf nur an spannungsfreien Leitungen durchgeführt werden — andernfalls verfälscht die externe Spannung das Ergebnis oder beschädigt das Gerät.

**Messprinzip Durchgangsprüfung:**
Sonderfall der Widerstandsmessung mit akustischem Signal bei Widerstand < 20–50 Ω. Die schnellste Methode zur Prüfung von Kabelverbindungen und Sicherungen. Der Summer reagiert typisch innerhalb von 100–250 ms — schnell genug, um beim Bewegen einer Leitung intermittierende Unterbrechungen zu erkennen.

#### 2.1.2 Kenngrößen und Genauigkeit

**Genauigkeitsspezifikation eines DMM:**

Die Genauigkeit wird typisch als ±(% vom Messwert + Digits) angegeben:

| Parameter | Einsteigergerät | Profigerät (z.B. Fluke 87V) | Laborgerät |
|-----------|-----------------|-------------------------------|------------|
| DC Spannung | ±0,5 % + 3 dgt | ±0,05 % + 1 dgt | ±0,005 % + 1 dgt |
| AC Spannung | ±1,0 % + 5 dgt | ±0,7 % + 2 dgt | ±0,06 % + 3 dgt |
| DC Strom | ±1,0 % + 3 dgt | ±0,2 % + 2 dgt | ±0,05 % + 2 dgt |
| Widerstand | ±0,8 % + 3 dgt | ±0,2 % + 1 dgt | ±0,01 % + 1 dgt |
| Auflösung | 2.000 Counts | 20.000 Counts | 120.000 Counts |
| True RMS | Nein | Ja | Ja |
| CAT-Rating | CAT II 300V | CAT III 1000V / CAT IV 600V | CAT II 300V |
| Preis (ca.) | 25–80 EUR | 350–500 EUR | 800–2.500 EUR |

**True RMS vs. Average-Responding:**
An Bord ist True-RMS-Fähigkeit essenziell. Wechselrichter erzeugen oft modifizierte Sinuswellen (Modified Sine Wave, MSW), deren Effektivwert von einem Average-Responding-Gerät bis zu 40 % falsch angezeigt wird. Nur ein True-RMS-Gerät misst den tatsächlichen Effektivwert unabhängig von der Kurvenform.

**CAT-Rating (Messkategorie):**
Das CAT-Rating definiert die Stoßfestigkeit des Multimeters gegenüber transienten Überspannungen:
- **CAT I:** Elektronik, geschützte Stromkreise (nicht für Bordnetz)
- **CAT II:** Einphasige Steckdosen-Stromkreise (Landstrom-Verbraucher)
- **CAT III:** Verteilung, Fest verdrahtete Verbraucher (Schalttafel, Landstrom-Einspeisung)
- **CAT IV:** Netzeinspeisung (Landstrom-Stecker, Steg-Steckdose)

Für die Bordnetz-Diagnose wird mindestens CAT III 600V empfohlen.

#### 2.1.3 Messpraxis an Bord

**Spannungsmessung am DC-Bordnetz:**

Referenzwerte für 12V-Systeme (Confidence: measured):

| Zustand | Spannung (Blei-Säure) | Spannung (LiFePO4) | Bewertung |
|---------|----------------------|---------------------|-----------|
| Voll geladen (Ruhe, >12h) | 12,73–12,80 V | 13,30–13,40 V | Optimal |
| 75 % SoC | 12,40–12,50 V | 13,20–13,30 V | Gut |
| 50 % SoC | 12,10–12,20 V | 13,10–13,20 V | Ladung empfohlen |
| 25 % SoC | 11,80–11,90 V | 12,80–13,00 V | Kritisch — sofort laden |
| Entladen | < 11,80 V | < 12,80 V | Tiefentladung droht |
| Während Ladung (Bulk) | 14,20–14,80 V | 14,20–14,60 V | Normal |
| Während Ladung (Float) | 13,20–13,60 V | 13,40–13,60 V | Normal |
| Motorstart (Cranking) | > 9,60 V | > 10,00 V | Akzeptabel |

Referenzwerte für 24V-Systeme: Alle Werte × 2.

**Spannungsabfall-Messung — Die wichtigste Marine-Messung:**

Der Spannungsabfall über eine belastete Verbindung ist der empfindlichste Indikator für Korrosion und lose Kontakte. Methode:

1. Verbraucher einschalten (Last anlegen)
2. Multimeter auf DC-Volt, Messbereich mV
3. Rote Messleitung an der Versorgungsseite der Verbindung
4. Schwarze Messleitung an der Verbraucherseite derselben Verbindung
5. Spannungsabfall ablesen

Grenzwerte (Confidence: documented — ABYC E-11):

| Verbindungstyp | Max. Spannungsabfall | Bewertung bei Überschreitung |
|----------------|---------------------|------------------------------|
| Einzelne Crimpverbindung | < 50 mV | Verbindung erneuern |
| Schraubklemme | < 50 mV | Klemme reinigen und nachziehen |
| Sicherungshalter | < 100 mV | Kontakte reinigen oder Halter tauschen |
| Batterieschalter | < 50 mV | Kontakte prüfen, ggf. tauschen |
| Gesamter positiver Leiter (Batterie→Verbraucher) | < 3 % der Nennspannung | Schwächste Verbindung identifizieren |
| Gesamter negativer Leiter (Verbraucher→Batterie) | < 3 % der Nennspannung | Masseverbindung prüfen |
| Kritische Systeme (Navigation, Bilgenpumpe) | < 1,5 % der Nennspannung | Sofort beheben |

Berechnungsbeispiel 12V-System, Ankerwinde 80 A:
- Max. 3 % Spannungsabfall = 12 V × 0,03 = 0,36 V (gesamt hin und zurück)
- Max. pro Verbindung: 50 mV = 0,05 V
- Bei 7 Verbindungen im Stromkreis: 7 × 0,05 V = 0,35 V → gerade noch akzeptabel
- Jede einzelne Verbindung mit > 100 mV ist verdächtig

### 2.2 Zangenamperemeter — Berührungslose Strommessung

#### 2.2.1 Funktionsprinzip

Das Zangenamperemeter (Clamp Meter) misst den Strom durch einen Leiter, ohne den Stromkreis aufzutrennen. Es nutzt das elektromagnetische Feld, das jeden stromdurchflossenen Leiter umgibt.

**AC-Messung (Stromwandler-Prinzip):**
Der aufklappbare Ferritkern umschließt den Leiter und bildet einen Transformator-Sekundärkreis. Der Wechselstrom im Leiter (Primärseite) induziert einen proportionalen Strom in der Sekundärwicklung des Kerns. Vorteil: Rein passives Messprinzip, hohe Genauigkeit. Nachteil: Nur für AC geeignet.

**DC-Messung (Hall-Sensor-Prinzip):**
Für Gleichstrommessung — an Bord die primäre Anforderung — wird ein Hall-Sensor im Luftspalt des Ferritkerns platziert. Das magnetische Feld des Gleichstroms erzeugt eine Hall-Spannung proportional zur Feldstärke und damit zum Strom. Nachteil: Hall-Sensoren haben einen Offset-Drift und müssen regelmäßig genullt werden.

**Wichtige Regel:** Immer nur EINEN Leiter umfassen. Werden Plus und Minus gemeinsam umfasst, heben sich die Magnetfelder auf und die Anzeige ist null — unabhängig vom tatsächlichen Strom.

#### 2.2.2 Typische Messungen an Bord

**Ruhestromaufnahme (Parasitic Draw):**

Die Ruhestromaufnahme ist der Strom, den das Bordnetz zieht, wenn alle Verbraucher ausgeschaltet sind. Typische Werte (Confidence: documented):

| Bootsgröße / Typ | Akzeptabler Ruhestrom | Typische Quellen |
|-------------------|----------------------|------------------|
| Segelyacht 8–10 m (einfach) | < 0,5 A | Bilgenpumpen-Automatik, CO-Melder |
| Segelyacht 10–14 m (Standard) | 0,5–1,5 A | + Kühlschrank-Thermostat, GPS-Backup |
| Segelyacht 14–18 m (Komfort) | 1,5–3,0 A | + Alarmanlage, AIS-Standby, Router |
| Motoryacht 10–14 m | 1,0–3,0 A | + Ladegerät-Standby, Klimavorheizung |
| Motoryacht 14–20 m | 3,0–8,0 A | + mehrere Kühlschränke, Überwachung |
| Superyacht 20 m+ | 8,0–25,0 A | + Server, CCTV, Klimaregelung |

Bei Überschreitung: Sicherungen einzeln ziehen und Ruhestrom nach jeder Sicherung erneut messen → Stromkreis mit dem Leckstrom identifizieren.

**Ladestrommessung:**

| Ladequelle | Typischer Strom (12V, 100Ah-Bank) | Typischer Strom (12V, 400Ah-Bank) |
|------------|-----------------------------------|-----------------------------------|
| Lichtmaschine (Standard) | 30–55 A | 30–55 A (Regler-limitiert) |
| Lichtmaschine (Hochleistung) | 80–120 A | 80–150 A |
| Landladegerät 30A | 25–30 A | 25–30 A |
| Solarpanel 100 Wp | 5–7 A (Spitze) | 5–7 A (Spitze) |
| Windgenerator | 2–15 A (windabh.) | 2–15 A (windabh.) |

### 2.3 Isolationsmessung (Megger-Test)

#### 2.3.1 Funktionsprinzip

Die Isolationsmessung prüft den Widerstand zwischen einem aktiven Leiter und der Erde (Schiffsmasse/Wasser). Ein Megger (Markenname, generisch: Isolationsmessgerät) legt eine definierte Prüfspannung an — typisch 250 V, 500 V oder 1.000 V DC — und misst den resultierenden Leckstrom. Der Isolationswiderstand ergibt sich aus R_iso = U_prüf / I_leck und wird in Megaohm (MΩ) angegeben.

**Warum hohe Prüfspannung?**
Bei der normalen Betriebsspannung (12 V oder 24 V DC) ist der Leckstrom durch beschädigte Isolation oft so gering, dass er nicht messbar ist. Die erhöhte Prüfspannung "stresst" die Isolation und macht Schwachstellen sichtbar, bevor sie bei Betriebsspannung zum Ausfall führen.

#### 2.3.2 Grenzwerte und Interpretation

**Isolationswiderstands-Grenzwerte (Confidence: documented — IEC 60092, ABYC E-11):**

| Prüfspannung | Neuzustand (Mindest.) | Bestand (Mindest.) | Kritisch | Alarm |
|--------------|----------------------|--------------------|-----------| ------|
| 500 V DC (Standard) | > 100 MΩ | > 2 MΩ | < 1 MΩ | < 0,5 MΩ |
| 250 V DC (empfindl. Geräte) | > 50 MΩ | > 1 MΩ | < 0,5 MΩ | < 0,25 MΩ |
| 1.000 V DC (Hochspannung) | > 200 MΩ | > 5 MΩ | < 2 MΩ | < 1 MΩ |

**Temperatur- und Feuchtigkeitskorrektur:**
Der Isolationswiderstand sinkt mit steigender Temperatur und Feuchtigkeit. Faustregel: Pro 10 °C Temperaturanstieg halbiert sich der Isolationswiderstand. Messungen sollten daher immer mit Angabe der Umgebungsbedingungen dokumentiert werden.

Korrekturformel (vereinfacht):
```
R_korrigiert = R_gemessen × K_temp × K_feuchte

K_temp = 2^((T_gemessen - 20) / 10)  → bezogen auf 20 °C Referenz
K_feuchte ≈ 1,0 bei < 60 % rH
K_feuchte ≈ 0,75 bei 60–80 % rH
K_feuchte ≈ 0,5 bei > 80 % rH
```

#### 2.3.3 Durchführung an Bord

**Vorbereitungsschritte (zwingend):**

1. **Alle Verbraucher abschalten** — Sicherungsautomaten AUS, Batterieschalter AUS
2. **Empfindliche Elektronik abklemmen** — Chartplotter, UKW-Funkgerät, AIS, Autopilot-Computer. Die Prüfspannung von 500 V kann Halbleiter zerstören!
3. **Batterien abtrennen** — Beide Pole abklemmen
4. **Landstrom trennen** — Stecker ziehen
5. **Kapazitive Verbraucher entladen** — Entstörfilter, Motorkondensatoren
6. **Wartezeit 60 Sekunden** nach Abtrennung (Entladung von Kapazitäten)

**Messablauf:**

1. Megger-Prüfspannung wählen (500 V DC für Standard-Bordnetz)
2. Prüfleitung an den zu testenden Leiter (z.B. Hauptstromschiene Plus)
3. Erdleitung an Schiffsmasse (Motorblock oder Kiel-Bolzen)
4. Messung starten — Minimum 60 Sekunden anlegen
5. Wert nach 60 s ablesen und dokumentieren (R_60s)
6. Polarisierungsindex PI = R_600s / R_60s berechnen (bei Verdacht auf Feuchtigkeit)
7. Leiter sicher entladen (Megger hat Entladefunktion)

**Polarisierungsindex (PI):**

| PI-Wert | Bewertung |
|---------|-----------|
| > 4,0 | Exzellent — trockene, intakte Isolation |
| 2,0–4,0 | Gut — normale Alterung |
| 1,0–2,0 | Verdächtig — Feuchtigkeit oder Degradation möglich |
| < 1,0 | Kritisch — Isolation feucht oder beschädigt |

### 2.4 Thermografie — Wärmebilddiagnose

#### 2.4.1 Funktionsprinzip

Infrarot-Thermografie erfasst die von Oberflächen emittierte Wärmestrahlung und visualisiert sie als Temperaturbild. In der Elektrik-Diagnose ist Thermografie ein mächtiges Werkzeug, da jede übermäßige Erwärmung auf einen erhöhten Widerstand hinweist — sei es durch Korrosion, lose Verbindungen, überlastete Kabel oder defekte Bauteile.

**Physikalischer Hintergrund:**
Jeder Körper mit Temperatur > 0 K emittiert elektromagnetische Strahlung. Die emittierte Leistung ist proportional zu T⁴ (Stefan-Boltzmann-Gesetz). Der Emissionsgrad ε (0 bis 1) beschreibt, wie effizient die Oberfläche im Vergleich zu einem idealen Schwarzkörper strahlt.

Typische Emissionsgrade an Bord:

| Material | Emissionsgrad ε | Anmerkung |
|----------|----------------|-----------|
| Isolierter Kabel (PVC, XLPE) | 0,92–0,95 | Ideale Messoberfläche |
| Kupfer (blank, oxidiert) | 0,60–0,80 | Stark variabel |
| Kupfer (blank, poliert) | 0,02–0,07 | Nicht direkt messbar |
| Edelstahl (gebürstet) | 0,50–0,70 | Korrektur nötig |
| Kunststoff-Schalttafel | 0,90–0,95 | Gut messbar |
| Aluminium (eloxiert) | 0,70–0,85 | Abhängig von Eloxalschicht |
| Aluminium (blank) | 0,03–0,10 | Nicht direkt messbar |

#### 2.4.2 Grenzwerte und Bewertungskriterien

**Temperaturdifferenz (ΔT) als Bewertungskriterium (Confidence: documented — NETA MTS):**

| ΔT (gegenüber Referenz) | Bewertung | Maßnahme | Dringlichkeit |
|--------------------------|-----------|----------|---------------|
| < 5 °C | Normal | Keine | — |
| 5–15 °C | Auffällig | Nächste geplante Wartung | Monate |
| 15–35 °C | Ernsthaft | Wartung so bald wie möglich | Wochen |
| 35–75 °C | Kritisch | Sofortige Reparatur | Tage |
| > 75 °C | Notfall | Sofort abschalten! | Sofort |

Die Referenz ist immer eine gleichartige, gleichbelastete Verbindung. Bei asymmetrischer Erwärmung einer von drei Phasen (AC-Landstrom) liegt der Fehler auf der warmen Phase.

#### 2.4.3 Einsatz an Bord

**Optimale Bedingungen:**
- Anlage mindestens 30 Minuten unter Last (Verbraucher eingeschaltet)
- Schalttafelabdeckungen geöffnet
- Keine direkte Sonneneinstrahlung auf Messobjekt
- Keine Zugluft (verfälscht Oberflächentemperatur)
- Kamera mindestens 15 Minuten akklimatisieren lassen

**Typische Befunde an Bord:**
1. Überhitzte Sicherungshalter (schlechter Kontakt Sicherung ↔ Halter)
2. Warme Crimpverbindungen (unzureichende Verpressung)
3. Heiße Batteriepole (Korrosion unter Polklemme)
4. Überlastete Kabelquerschnitte (zu dünne Leitung für den Strom)
5. Defekte Relais (Kontaktabbrand, erhöhter Innenwiderstand)
6. Asymmetrische Erwärmung an Landstrom-Steckern (lose Kontaktfeder)

### 2.5 Streustrom-Diagnose

#### 2.5.1 Grundlagen und Gefahren

Streustrom (Stray Current, Galvanic Corrosion Current) ist der ungewollte Fluss von elektrischem Strom durch das Seewasser oder den Rumpf. Er ist eine der zerstörerischsten und heimtückischsten Erscheinungen in der Marine-Elektrik, da er massive Korrosion an metallischen Unterwasser-Bauteilen verursacht — Propeller, Welle, Stevenrohr, Seeventile, Kiel-Bolzen.

**Zwei Haupttypen:**

**Galvanische Streustrom (Galvanic Corrosion):**
Entsteht durch die galvanische Spannungsreihe verschiedener Metalle im Elektrolyten Seewasser. Beispiel: Bronze-Seeventil in Kontakt mit Edelstahl-Kielbolzen → das unedlere Metall wird anodisch aufgelöst. Schutz: Opferanoden (Zink oder Aluminium) und galvanische Isolation.

**Elektrolytischer Streustrom (Stray Current Corrosion):**
Verursacht durch Fehler in der elektrischen Anlage — ein Isolationsfehler lässt Gleichstrom über das Seewasser fließen. Korrosionsrate bis zu 1.000-fach höher als galvanische Korrosion! Ein Strom von nur 1 A kann innerhalb eines Jahres ca. 10 kg Aluminium oder 20 kg Stahl auflösen.

#### 2.5.2 Diagnose-Methoden

**Methode 1 — Referenzelektrodenmessung (Silber/Silberchlorid):**

Die genaueste Methode. Eine Ag/AgCl-Referenzelektrode wird ins Wasser neben dem Rumpf getaucht. Die Potentialdifferenz zwischen Rumpf (Schiffsmasse) und Referenzelektrode wird mit einem hochohmigen Voltmeter gemessen.

Bewertung (Confidence: documented — ABYC E-2):

| Potential (vs. Ag/AgCl) | Bewertung | Maßnahme |
|--------------------------|-----------|----------|
| -800 bis -1.050 mV | Ausreichend geschützt | Anoden kontrollieren |
| -1.050 bis -1.100 mV | Überschutz möglich | Anodenmenge reduzieren |
| < -1.100 mV | Überschutz — Blasenbildung | Sofort Anoden reduzieren |
| > -800 mV | Unzureichend geschützt | Anoden erneuern, Streustrom suchen |
| > -500 mV | Aktive Korrosion! | Sofort Fehler suchen |

**Methode 2 — DC-Leckstrommessung an Landstromkabel:**

Zangenamperemeter um alle Leiter des Landstromkabels (L, N, PE) gemeinsam legen. Bei einem fehlerfreien System ist die Summe der Ströme null. Jede Anzeige > 0 bedeutet, dass Strom über einen alternativen Pfad (z.B. Seewasser) zurückfließt.

| Messwert | Bewertung |
|----------|-----------|
| < 30 mA | Normal (Ableitströme der Entstörfilter) |
| 30–100 mA | Erhöht — Isolationsmessung durchführen |
| 100–500 mA | Kritisch — Streustrom, Fehler suchen |
| > 500 mA | Gefahr — Sofort Landstrom trennen! |

**Methode 3 — Spannungsmessung Schiffsmasse vs. Nachbarboot:**

Einfachste Vor-Ort-Methode: Voltmeter zwischen der Schiffsmasse des eigenen Bootes und der eines benachbarten Bootes am selben Steg.

| Messwert | Bewertung |
|----------|-----------|
| < 50 mV | Normal |
| 50–200 mV | Erhöht — Isolationsprüfung beider Boote |
| > 200 mV | Aktiver Streustrom — eines der Boote hat einen Fehler |

### 2.6 Batterietest — Kapazitäts- und Zustandsdiagnose

#### 2.6.1 Ruhespannungsmessung (OCV — Open Circuit Voltage)

Die einfachste Methode zur Bestimmung des Ladezustands (SoC — State of Charge). Voraussetzung: Batterie mindestens 4 Stunden (besser 12–24 h) ohne Last und ohne Ladung (Ruhephase), damit sich die Oberflächenladung abgebaut hat.

**Ruhespannungstabelle Blei-Säure (12V, flooded) (Confidence: measured):**

| SoC | Spannung | Säuredichte (20 °C) |
|-----|----------|---------------------|
| 100 % | 12,73 V | 1,265 g/cm³ |
| 90 % | 12,58 V | 1,249 g/cm³ |
| 80 % | 12,42 V | 1,233 g/cm³ |
| 70 % | 12,32 V | 1,218 g/cm³ |
| 60 % | 12,20 V | 1,204 g/cm³ |
| 50 % | 12,06 V | 1,190 g/cm³ |
| 40 % | 11,98 V | 1,176 g/cm³ |
| 30 % | 11,88 V | 1,162 g/cm³ |
| 20 % | 11,76 V | 1,148 g/cm³ |
| 10 % | 11,64 V | 1,134 g/cm³ |
| 0 % | 11,50 V | 1,120 g/cm³ |

**Ruhespannungstabelle AGM (12V) (Confidence: measured):**

| SoC | Spannung |
|-----|----------|
| 100 % | 12,85 V |
| 90 % | 12,65 V |
| 80 % | 12,50 V |
| 70 % | 12,37 V |
| 60 % | 12,24 V |
| 50 % | 12,10 V |
| 40 % | 12,00 V |
| 30 % | 11,90 V |
| 20 % | 11,80 V |
| 10 % | 11,70 V |
| 0 % | 11,60 V |

**Ruhespannungstabelle LiFePO4 (12V / 4S) (Confidence: measured):**

| SoC | Spannung | Bemerkung |
|-----|----------|-----------|
| 100 % | 14,40–14,60 V | Direkt nach Ladung, sinkt auf 13,4 V |
| 90 % | 13,35 V | |
| 80 % | 13,28 V | |
| 70 % | 13,24 V | Flaches Plateau — Unterscheidung schwierig |
| 60 % | 13,22 V | |
| 50 % | 13,20 V | |
| 40 % | 13,18 V | |
| 30 % | 13,14 V | |
| 20 % | 13,00 V | Untere Grenze für Dauernutzung |
| 10 % | 12,80 V | BMS sollte abschalten |
| 0 % | 10,00 V | Tiefentladung — BMS muss getrennt haben |

Hinweis: LiFePO4 hat ein extrem flaches Spannungsplateau zwischen 20 % und 80 % SoC. Die Ruhespannung ist daher kein zuverlässiger SoC-Indikator. Coulomb-Counting (z.B. Victron SmartShunt) ist die bevorzugte Methode.

#### 2.6.2 Belastungstest (Load Test)

**Methode:** Eine definierte Last wird für 15 Sekunden angelegt. Die Starterbatterie muss unter Last > 9,6 V (12V-System) halten.

Faustregel für Lastgröße:
- Blei-Säure: 50 % der CCA (Cold Cranking Amps) bei -18 °C
- AGM: 50 % der CCA
- Starterbatterie 12V/70 Ah ≈ CCA 640 A → Testlast 320 A

| Spannung unter Last (15s) | Bewertung |
|---------------------------|-----------|
| > 10,2 V | Exzellent |
| 9,6–10,2 V | Gut |
| 9,0–9,6 V | Schwach — Austausch planen |
| < 9,0 V | Defekt — sofort tauschen |

#### 2.6.3 Innenwiderstandsmessung

Moderne Batterietester messen den Innenwiderstand mit einem AC-Impuls (typisch 1 kHz). Der Innenwiderstand steigt mit Alterung und gibt Aufschluss über den SoH (State of Health).

| Batterietyp (12V, 100 Ah) | Neuzustand | 80 % SoH | 60 % SoH | Austausch |
|----------------------------|-----------|----------|----------|-----------|
| Blei-Säure (Flooded) | 4–6 mΩ | 7–9 mΩ | 10–14 mΩ | > 15 mΩ |
| AGM | 3–5 mΩ | 6–8 mΩ | 9–12 mΩ | > 13 mΩ |
| Gel | 5–8 mΩ | 9–12 mΩ | 13–18 mΩ | > 20 mΩ |
| LiFePO4 | 1–3 mΩ | 3–5 mΩ | 5–8 mΩ | > 10 mΩ |

### 2.7 Zusätzliche Messtechniken

#### 2.7.1 Oszilloskop-Diagnose

Für die Diagnose von Ladereglerfehlern, Wechselrichter-Störungen und EMV-Problemen ist ein tragbares Oszilloskop (z.B. Fluke ScopeMeter 120B) unentbehrlich. Es zeigt den zeitlichen Verlauf von Spannung und Strom und macht Störungen sichtbar, die ein DMM nicht erfasst.

**Typische Oszilloskop-Diagnosen an Bord:**

| Anwendung | Einstellung | Normalbefund | Fehlerbefund |
|-----------|-------------|--------------|--------------|
| Lichtmaschinen-Ripple | AC-Kopplung, 20 mV/div | < 100 mV pp | > 500 mV pp → Diode defekt |
| Wechselrichter-Ausgangssignal | AC, 100 V/div, 5 ms/div | Sauberer Sinus | Verzerrung, Aussetzer |
| PWM-Solarregler | DC, 5 V/div, 100 μs/div | Sauberes PWM-Signal | Fehlende Pulse, Jitter |
| Starter-Spannungsverlauf | DC, 5 V/div, 500 ms/div | Dip auf >9,6V, schnelle Erholung | Dip <9V, langsame Erholung |
| Tachosignal (Motor) | AC, 5 V/div, 10 ms/div | Gleichmäßige Pulse | Fehlende/doppelte Pulse |

#### 2.7.2 Erdungskontinuitätsmessung

Prüfung, ob alle metallischen Teile (Motorblock, Tanks, Stevenrohr, Seeventile, Reling-Stützen) ordnungsgemäß mit der gemeinsamen Masse verbunden sind.

**Methode:** Widerstandsmessung mit Kelvin-Klemmen (Vierleitermessung) oder niederohmiges Ohmmeter.

| Verbindung | Max. Widerstand |
|------------|----------------|
| Motorblock → Hauptmasse-Sammelschiene | < 0,5 mΩ |
| Batterie Minus → Hauptmasse | < 1,0 mΩ |
| Seeventil → Erdungsband | < 10 mΩ |
| Tank → Erdungsband | < 10 mΩ |
| Bugkorb/Heckkorb → Erdungsband | < 50 mΩ |
| Mast-Fuß → Erdungsband | < 10 mΩ |

#### 2.7.3 Kabelquerschnitt-Bestimmung (nachträglich)

In der Praxis muss häufig der Querschnitt eines bereits verlegten Kabels bestimmt werden — insbesondere bei nachträglichen Verbraucher-Ergänzungen oder beim Kauf einer Gebrauchtyacht.

**Methode 1 — Kabelbeschriftung ablesen:**
Marinekabel tragen Aufdrucke wie "16 AWG", "1,5 mm²" oder "TINNED COPPER 2,5 mm²". Vorsicht: AWG (American Wire Gauge) ist NICHT identisch mit mm²!

AWG ↔ mm² Umrechnungstabelle (Confidence: measured):

| AWG | mm² (exakt) | mm² (Handelsbezeichnung) | Max. Strom (30°C, offen) |
|-----|-------------|--------------------------|--------------------------|
| 18 | 0,82 | 0,75 | 7 A |
| 16 | 1,31 | 1,5 | 10 A |
| 14 | 2,08 | 2,5 | 15 A |
| 12 | 3,31 | 4,0 | 20 A |
| 10 | 5,26 | 6,0 | 30 A |
| 8 | 8,37 | 10,0 | 40 A |
| 6 | 13,30 | 16,0 | 55 A |
| 4 | 21,15 | 25,0 | 70 A |
| 2 | 33,62 | 35,0 | 95 A |
| 1 | 42,41 | 50,0 | 110 A |
| 1/0 (0) | 53,49 | 50,0 | 125 A |
| 2/0 (00) | 67,43 | 70,0 | 145 A |
| 4/0 (0000) | 107,22 | 95,0 | 195 A |

**Methode 2 — Durchmesser messen:**
Einzelader freilegen, Durchmesser mit Messschieber messen. Querschnitt = π × (d/2)². Bei Litze: Eine Einzelader messen und mit Aderzahl multiplizieren.

**Methode 3 — Widerstandsmessung (genaueste Methode):**
Kabelwiderstand über bekannte Länge messen und mit Kupfer-Leitwert vergleichen:
```
Querschnitt [mm²] = (ρ × L) / R
  ρ = 0,0178 Ω·mm²/m (Kupfer bei 20°C)
  L = Kabellänge in Metern (hin und zurück!)
  R = gemessener Widerstand in Ohm
```

Beispiel: 10 m Kabel (5 m hin, 5 m zurück), gemessener Widerstand 0,071 Ω:
Querschnitt = (0,0178 × 10) / 0,071 = 2,51 mm² → 2,5 mm² Kabel

#### 2.7.4 Kabelfarben-Codierung im Marine-Bereich

Die Kabelfarben an Bord folgen unterschiedlichen Standards je nach Herstellerland und Alter der Yacht:

**ABYC-Standard (amerikanische Yachten) (Confidence: documented):**

| Farbe | Funktion |
|-------|----------|
| Rot | DC Positiv (Hauptversorgung) |
| Gelb mit rotem Streifen | Starterkabel Positiv |
| Braun mit gelbem Streifen | Bilgenpumpe (Automatik) |
| Dunkelgrau | Navigation (Tachometer) |
| Grün | DC Erdung / Bonding |
| Schwarz | DC Negativ (Rückleiter) |
| Weiß | AC Negativ (Neutralleiter) |
| Schwarz (AC) | AC Phase (L) |
| Grün (AC) | AC Schutzleiter (PE) |
| Blau | Kabinenlicht |
| Gelb | Generatorstart |
| Orange | Zubehör-Schalter |

**Europäischer Standard (DIN/ISO) (Confidence: documented):**

| Farbe | Funktion |
|-------|----------|
| Rot | DC Positiv |
| Blau oder Schwarz | DC Negativ |
| Braun | AC Phase (L) |
| Blau (hell) | AC Neutralleiter (N) |
| Grün-Gelb | AC Schutzleiter (PE) |
| Grün | DC Erdung / Bonding |

**Achtung:** Auf älteren und selbstgebauten Yachten weicht die Farbcodierung häufig ab! Vor jeder Arbeit: Kabel mit Multimeter identifizieren, nicht nach Farbe urteilen. Jeden Stromkreis mit dem Schaltplan abgleichen. Fehlende Beschriftung bei der Wartung nachtragen.

#### 2.7.5 Sicherungstypen im Marine-Bereich

Übersicht der gebräuchlichen Sicherungstypen an Bord:

| Sicherungstyp | Nennstrom | Einsatz | Abmessungen | Unterbrechungsvermögen |
|---------------|-----------|---------|-------------|------------------------|
| ATO / ATC (Flach-Steck) | 1–40 A | Standard-DC-Verbraucher | 19,1 × 18,5 × 5,1 mm | 1.000 A |
| MINI (Flach-Steck) | 2–30 A | Kompakte Schalttafeln | 10,9 × 16,3 × 3,8 mm | 1.000 A |
| MAXI (Flach-Steck) | 20–80 A | Mittlere Verbraucher | 29,2 × 34,0 × 8,5 mm | 1.500 A |
| MEGA / AMG | 100–300 A | Hauptsicherung, Wechselrichter | 57 × 19 × 9 mm | 2.000 A |
| ANL | 35–750 A | Hauptsicherung, Ankerwinde, Bugstrahlruder | 82 × 22 × 11 mm | 6.000 A |
| Streifensicherung (MRBF) | 30–300 A | Direkt am Batteriepol | 42 × 25 × 13 mm | 2.500 A |
| Schmelzsicherung (Glas) | 0,5–30 A | Ältere Anlagen, Instrumente | 6,3 × 32 mm | 200 A |
| NH-Sicherung | 25–1.250 A | Professionelle Anlagen, Superyachten | Verschiedene Baugrößen | 50.000 A |
| Sicherungsautomat (MCB) | 1–63 A | AC-Verteilung, moderne DC-Anlagen | DIN-Hutschiene | 6.000–10.000 A |

**Kritische Regeln:**
1. Niemals eine Sicherung durch eine mit höherem Nennstrom ersetzen!
2. Sicherung schützt das KABEL, nicht den Verbraucher. Der Sicherungswert muss ≤ der Strombelastbarkeit des dünnsten Kabels im Stromkreis sein.
3. An der Batterie: Hauptsicherung innerhalb von 180 mm (7 Zoll) vom Batteriepol (ABYC E-11). Viele Yachten haben diese Sicherung NICHT — gravierender Mangel!
4. Sicherungshalter-Kontakte korrodieren → regelmäßig prüfen und reinigen.

#### 2.7.6 Crimpverbindungen — Technik und Qualitätskontrolle

Die Crimpverbindung ist die bevorzugte Verbindungstechnik in der Marine-Elektrik (NICHT Löten — Lötstellen werden durch Vibration spröde und brechen).

**Marine-Grade-Crimpverbinder vs. Standard:**

| Merkmal | Standard (KFZ) | Marine-Grade |
|---------|----------------|--------------|
| Material Hülse | Kupfer, verzinnt | Kupfer, doppelt verzinnt |
| Isolierung | PVC (schrumpft nicht) | Polyolefin mit Heißkleber (schmelzdicht) |
| Korrosionsschutz | Keiner | Integrierter Kleber dichtet ab |
| Farbcodierung | Rot (0,5–1,5mm²), Blau (1,5–2,5mm²), Gelb (4–6mm²) | Gleiche Farben, oft transparent |
| Preis (100 Stk.) | 5–10 EUR | 15–30 EUR |
| Lebensdauer Marine | 2–5 Jahre | 15–25 Jahre |

**Crimpwerkzeug-Typen:**

| Werkzeugtyp | Eignung | Preis | Qualität |
|-------------|---------|-------|----------|
| Einfache Zange (Baumarkt) | Ungeeignet für Marine! | 5–15 EUR | Mangelhaft — inkonsistente Pressung |
| Ratsche-Crimpzange (z.B. Knipex 97 21 215) | Gut | 50–80 EUR | Gut — definierte Presskraft |
| Professionelle Ratsche mit Wechseleinsätzen | Sehr gut | 120–250 EUR | Sehr gut — passend für jeden Verbinder |
| Hydraulische Crimpzange (>25 mm²) | Pflicht für große Querschnitte | 200–500 EUR | Exzellent |

**Qualitätskontrolle einer Crimpverbindung:**

| Prüfkriterium | Akzeptabel | Nicht akzeptabel |
|---------------|-----------|------------------|
| Zugfestigkeit | Kabel reißt vor Crimp | Kabel lässt sich aus Crimp ziehen |
| Verformung der Hülse | Gleichmäßig, keine Risse | Einseitig, Risse, zu flach |
| Isolierungsbeschädigung | Keine sichtbare Beschädigung | Einschnitte, Quetschungen |
| Aderfreilegung | 0–1 mm Kupfer sichtbar | > 3 mm Kupfer sichtbar |
| Alle Adern erfasst | 100 % der Einzeladern im Verbinder | Einzelne Adern stehen heraus |

Nach dem Crimpen: Doppelwand-Schrumpfschlauch mit Kleber über die gesamte Verbindung — auch bei Marine-Grade-Verbindern als zusätzlichen Schutz.

**Confidence-Bewertung dieses Abschnitts:**
- Messprinzipien: `measured` — physikalische Grundlagen
- Grenzwerte: `documented` — ABYC E-11, IEC 60092, NETA MTS
- Praxishinweise: `estimated` — Erfahrungswerte Marine-Elektriker
- Referenzspannungstabellen: `measured` — Hersteller-Datenblätter (Victron, Mastervolt, Trojan)
- AWG-Tabelle: `measured` — ASTM B258, IEC 60228
- Sicherungsdaten: `measured` — Hersteller-Datenblätter (Littelfuse, Blue Sea, Bussmann)

---

## 3. Typenübersicht

### 3.0 Vergleichsmatrix der Wartungstypen

| Kriterium | Jährliche Inspektion | Saisonale Wartung | 5-Jahres-Revision | Winterfestmachung | Inbetriebnahme | Notfallreparatur |
|-----------|---------------------|-------------------|--------------------|--------------------|----------------|------------------|
| **Häufigkeit** | 1×/Jahr | 2–3×/Jahr | 1×/5 Jahre | 1×/Jahr (Herbst) | 1×/Jahr (Frühjahr) | Nach Bedarf |
| **Wer** | Eigner oder Fachbetrieb | Eigner | Fachbetrieb empfohlen | Eigner | Eigner | Eigner (Erste Hilfe) + Fachbetrieb |
| **Dauer (12m SY)** | 4–8 h | 1–2 h | 8–16 h | 3–6 h | 4–8 h | Variabel |
| **Kosten** | 250–1.000 EUR | Eigenleistung | 1.200–2.500 EUR | Eigenleistung | Eigenleistung | 200–5.000+ EUR |
| **Schwerpunkt** | Gesamtanlage, Dokumentation | Funktionskontrolle | Tiefendiagnose | Schutz im Winterlager | Wiederherstellung | Fehlerbehebung |
| **Messtechnik** | DMM, Zangenamperemeter | DMM (Basistest) | DMM + Megger + Thermografie | DMM | DMM | DMM, Improvisation |
| **Isolationsmessung** | Optional | Nein | Pflicht | Nein | Nein | Nur bei Verdacht |
| **Thermografie** | Empfohlen | Nein | Pflicht | Nein | Nein | Nein |
| **Batterie-Kapazitätstest** | Empfohlen | Nein | Pflicht | Nein | Empfohlen | Nein |
| **Dokumentationsumfang** | Vollständig | Kurznotiz | Vollständig + Trenddaten | Checkliste | Checkliste | Schadensbericht |

### 3.1 Jährliche Inspektion

#### 3.1.1 Umfang und Ziele

Die jährliche Elektrik-Inspektion ist die Basismaßnahme zur Aufrechterhaltung der Betriebssicherheit und des Anlagenwerts. Sie sollte idealerweise im Frühjahr vor der Saison durchgeführt werden.

**Zeitaufwand nach Bootsgröße (Confidence: estimated):**

| Bootsgröße | Zeitaufwand (Fachmann) | Zeitaufwand (Eigner, erfahren) | Kosten (Fachbetrieb) |
|------------|------------------------|-------------------------------|---------------------|
| 8–10 m SY | 2–4 Stunden | 4–8 Stunden | 250–500 EUR |
| 10–14 m SY | 4–8 Stunden | 8–16 Stunden | 500–1.000 EUR |
| 14–18 m SY/MY | 8–16 Stunden | 16–32 Stunden | 1.000–2.000 EUR |
| 18–24 m MY | 16–32 Stunden | Fachbetrieb empfohlen | 2.000–4.500 EUR |
| 24 m+ | 32–80 Stunden | Fachbetrieb Pflicht | 4.500–12.000 EUR |

#### 3.1.2 Checkliste Jährliche Inspektion

**A — Batterien und Ladung:**
- [ ] Ruhespannung aller Batterien messen und dokumentieren
- [ ] Polklemmen auf Korrosion prüfen, ggf. reinigen und fetten
- [ ] Batteriehalterungen auf festen Sitz prüfen (Vibrationssicherung)
- [ ] Elektrolytstand prüfen (bei Flooded-Batterien)
- [ ] Batterieraum-Belüftung prüfen (Wasserstoff-Gefahr)
- [ ] Ladegerät-Funktion prüfen (Bulk, Absorption, Float)
- [ ] Solarpanel-Ertrag messen und mit Vorjahr vergleichen
- [ ] Lichtmaschinen-Ladestrom messen

**B — Schalttafeln und Sicherungen:**
- [ ] Sichtprüfung Schalttafel auf Korrosion, Verfärbungen, Schmorspuren
- [ ] Alle Sicherungen auf korrekten Wert prüfen
- [ ] Sicherungshalter-Kontakte auf Korrosion prüfen
- [ ] Schalter-Funktion testen (Haptik, Kontakt, Beleuchtung)
- [ ] Thermografie der Schalttafel unter Last (empfohlen)
- [ ] Beschriftung vollständig und lesbar?

**C — Kabel und Verbindungen:**
- [ ] Sichtprüfung aller zugänglichen Kabelführungen
- [ ] Crimpverbindungen auf Korrosion prüfen (Grünspan?)
- [ ] Kabelisolierung auf Sprödigkeit, Risse, Verfärbung prüfen
- [ ] Kabeldurchführungen durch Schotten auf Scheuerschutz prüfen
- [ ] Spannungsabfall-Messung an kritischen Verbrauchern (Ankerwinde, Bugstrahlruder, Bilgenpumpe)

**D — Masseverbindungen:**
- [ ] Hauptmasseband auf Korrosion und festen Sitz prüfen
- [ ] Masseverbindung Motorblock → Hauptmasse messen (< 1 mΩ)
- [ ] Erdungsband zu Seeventilen, Tanks, Kiel-Bolzen prüfen
- [ ] Massesammelschiene auf Korrosion prüfen

**E — Schutzeinrichtungen:**
- [ ] FI-Schutzschalter (RCD) testen (Prüftaste und mit Messgerät)
- [ ] Batterie-Hauptschalter funktionsfähig?
- [ ] Galvanischer Isolator (sofern vorhanden) testen
- [ ] Überspannungsschutz (sofern vorhanden) prüfen

**F — Beleuchtung und Signale:**
- [ ] Alle Navigationsleuchten funktionsfähig?
- [ ] Sichtweite der Navlichter prüfen (Leuchtmittel-Alterung)
- [ ] Ankerlicht, Dampferlicht, Hecklicht testen
- [ ] Innenbeleuchtung komplett testen
- [ ] Unterwasserbeleuchtung (sofern vorhanden) testen

**G — Landstrom:**
- [ ] Landstromkabel auf Beschädigung prüfen
- [ ] Landstrom-Einlass auf Korrosion und Dichtigkeit prüfen
- [ ] Trenntrafo/Galvanischer Isolator testen
- [ ] FI-Schutzschalter im Landstromkreis testen

**H — Streustrom-Prüfung:**
- [ ] Leckstrom am Landstromkabel messen (Zangenamperemeter)
- [ ] Potentialmessung Rumpf vs. Referenzelektrode (bei Wasserlieger)
- [ ] Opferanoden auf Verbrauch prüfen

### 3.2 Saisonale Wartung

#### 3.2.1 Frühjahrs-Inbetriebnahme (nach Winterlager)

**Umfang:** Wiederherstellung der vollen Betriebsfähigkeit nach der Winterpause. Aufbauend auf der jährlichen Inspektion (3.1), die idealerweise zeitgleich erfolgt.

**Zusätzliche Punkte zur jährlichen Inspektion:**

- [ ] Batterie-Kapazitätstest nach Winterladung
- [ ] Alle während der Winterfestmachung abgeklemmten Systeme wieder anschließen
- [ ] Reihenfolge der Inbetriebnahme: Batterien → Hauptschalter → DC-Verbraucher → Landstrom → AC-Verbraucher
- [ ] Kühlschrank/Tiefkühler-Kompressor: Anlaufstrom messen
- [ ] Autopilot: Funktionstest, Ruder-Endlagen
- [ ] Winschen (elektrisch): Funktionstest unter Last, Strommessung
- [ ] Bugstrahlruder: Funktionstest, Strommessung, Kabelerwärmung prüfen
- [ ] Ankerwinde: Funktionstest unter Last, Spannungsabfall messen
- [ ] UKW-Funk: Sendetest, Strom messen (ca. 5–6 A bei 25 W)
- [ ] AIS-Transponder: Funktionstest
- [ ] Alle Pumpen testen (Bilge, Frischwasser, Salzwasser, Dusche, WC)

#### 3.2.2 Mitte-Saison-Check (Juli/August)

Kurze Kontrolle nach intensiver Nutzung:

- [ ] Batterie-Ruhespannung
- [ ] Sichtprüfung Schalttafel
- [ ] Landstrom-Stecker und -Kabel visuell
- [ ] Bilgenpumpen-Funktion (manuell und automatisch)
- [ ] Navigationsbeleuchtung

#### 3.2.3 Herbst-Vorbereitung (vor Winterlager)

Siehe detailliert unter 3.4 Winterfestmachung.

### 3.3 5-Jahres-Revision

#### 3.3.1 Umfang und Ziele

Alle fünf Jahre wird eine umfassende Revision der gesamten Elektrik empfohlen. Diese geht weit über die jährliche Inspektion hinaus und umfasst auch versteckte Bereiche und systematische Tests.

**Zusätzlich zur jährlichen Inspektion:**

- [ ] Komplette Isolationsmessung aller Stromkreise (Megger-Test, 500 V DC)
- [ ] Innenwiderstandsmessung aller Batterien
- [ ] Thermografie der gesamten Schalttafel unter Volllast
- [ ] Alle Crimpverbindungen in kritischen Stromkreisen nachprüfen oder erneuern
- [ ] Alle Sicherungshalter reinigen oder ersetzen
- [ ] Landstrom-Stecker und -Dose: Kontakte prüfen, ggf. ersetzen
- [ ] Alle Dichtungen an Kabeldurchführungen erneuern
- [ ] Erdungskontinuität aller Metalteile messen
- [ ] Kabelführung im Motorraum auf Hitze- und Vibrationsschäden prüfen
- [ ] Zugänglichkeit aller Verbindungen sicherstellen (oft zugebaut!)
- [ ] Schaltplan-Aktualität prüfen — stimmen die Sicherungsbezeichnungen noch?
- [ ] Alle Relais unter Last prüfen (Kontaktspannung messen)
- [ ] Alle Pumpen-Motorströme messen und mit Sollwerten vergleichen
- [ ] Windgenerator/Solarpanel-Kabel auf UV-Schäden prüfen
- [ ] VHF-Antennenkabel: SWR messen (Stehwellenverhältnis)

**Zeitaufwand:** 2–5× der jährlichen Inspektion.

**Kosten (Confidence: estimated):**

| Bootsgröße | Kosten (Fachbetrieb) |
|------------|---------------------|
| 8–10 m SY | 500–1.200 EUR |
| 10–14 m SY | 1.200–2.500 EUR |
| 14–18 m SY/MY | 2.500–5.500 EUR |
| 18–24 m MY | 5.500–12.000 EUR |
| 24 m+ | 12.000–30.000 EUR |

### 3.4 Winterfestmachung

#### 3.4.1 Ziele

Die Winterfestmachung schützt die elektrische Anlage vor den Gefahren der Winterpause: Frostschäden, Kondensation, Tiefentladung, Nagetier-Fraß an Kabeln, Korrosion durch stehende Feuchtigkeit.

#### 3.4.2 Checkliste Winterfestmachung Elektrik

**Phase 1 — Vorbereitung (an Bord, Wasser):**

- [ ] Alle Verbraucher ausschalten
- [ ] Alle Systeme dokumentieren (Fotos der Schalttafel-Stellungen, Notiz welche Sicherungen normalerweise ein sind)
- [ ] Solarpanel-Regler auf Winterprogramm umstellen (Float-Erhaltungsladung)
- [ ] Windgenerator arretieren und abklemmen (oder kurzschließen!)

**Phase 2 — Stromversorgung:**

- [ ] Batterien voll laden (100 % SoC) — kritisch!
- [ ] Optionen für Winterlager:
  - **Option A (empfohlen):** Batterien an Bord belassen, Erhaltungsladegerät (Float/Maintenance) anschließen. Voraussetzung: Landstrom im Winterlager.
  - **Option B:** Batterien ausbauen, an Land trocken und frostfrei lagern, monatlich nachladen.
  - **Option C (nur LiFePO4):** Batterie-Trennschalter AUS, BMS schaltet in Sleep-Mode. LiFePO4 hat <3 % Selbstentladung/Monat.
- [ ] Blei-Säure-Batterien: Elektrolytstand auffüllen (bei Flooded)
- [ ] Batteriepole mit Polfett (z.B. Shell Retinax HD2) konservieren

**Phase 3 — Abklemmen und Konservieren:**

- [ ] Empfindliche Elektronik ausbauen oder luftdicht verpacken (Chartplotter, tragbares UKW, Fernglas mit Kompass)
- [ ] Antennenstecker mit Schutzkappen versehen oder Denso-Band umwickeln
- [ ] VHF-Antenne: Stecker mit Kontaktspray behandeln und abdichten
- [ ] GPS-Antenne: Stecker schützen
- [ ] Alle offenen Kabelenden mit Schrumpfschlauch oder Isolierband verschließen
- [ ] Kabeldurchführungen an Deck auf Dichtigkeit prüfen

**Phase 4 — Feuchtigkeitsschutz:**

- [ ] Entfeuchter an Bord installieren (elektrisch bei Landstrom, sonst Granulat-Entfeuchter)
- [ ] Schalttafeln leicht geöffnet lassen (Luftzirkulation)
- [ ] Silikagelpackungen in Schalttafeln und Elektronikfächer legen
- [ ] Bilge trocken saugen

**Phase 5 — Schutz gegen Nagetiere:**

- [ ] Kabelschächte auf Zugangsmöglichkeiten für Mäuse prüfen
- [ ] Landstromkabel am Steg-Anschluss mit Mäuseschutz versehen
- [ ] Ultraschall-Mäuseabwehr (batteriebetrieben) in Betracht ziehen

#### 3.4.3 Sonderfälle

**Winterlager im Wasser (Dauerlieger):**
- Landstrom dauerhaft angeschlossen → Trenntrafo oder galvanischer Isolator zwingend erforderlich
- Streustrom-Kontrolle monatlich
- Opferanoden vor dem Winter erneuern
- Bilgenpumpen-Automatik muss aktiv bleiben
- Frostschutz für Motorkühlung und Frischwasser beachten

**LiFePO4-Batterien im Winter:**
- NIEMALS unter 0 °C laden! BMS muss Low-Temperature-Cutoff haben.
- Lagertemperatur ideal: 10–25 °C, akzeptabel: -20 bis +45 °C
- SoC für Lagerung: 50–60 % (nicht voll, nicht leer)
- Kein Erhaltungsladegerät notwendig — BMS-Sleep-Mode genügt

### 3.4.4 Winterfestmachung — Detaillierte Protokolle nach Batterietyp

**Protokoll Blei-Säure (Flooded / Wet Cell):**
1. Alle Zellen auf korrekten Elektrolytstand auffüllen (destilliertes Wasser)
2. Batterie voll laden (Bulk → Absorption → Float, mindestens 4 h im Float)
3. Ruhespannung nach 4 h dokumentieren (Soll: > 12,65 V)
4. Säuredichte jeder Zelle messen und dokumentieren (Soll: 1,265 ±0,010 g/cm³)
5. Zellenabweichung > 0,015 g/cm³ → Ausgleichsladung (Equalization) durchführen
6. Polklemmen reinigen, Polfett auftragen
7. Erhaltungsladegerät anschließen (Soll: 13,2–13,4 V Float)
8. Batterieraum belüften (Gasung während Erhaltungsladung minimal, aber vorhanden)

**Protokoll AGM / Gel:**
1. Batterie voll laden (14,4 V Absorption bei AGM, 14,1 V bei Gel)
2. Ruhespannung nach 4 h dokumentieren (Soll: > 12,80 V AGM, > 12,85 V Gel)
3. KEINE Equalization bei AGM/Gel! (zerstört die Vlies-/Gel-Struktur)
4. Polklemmen reinigen, Polfett auftragen
5. Erhaltungsladegerät anschließen (13,5–13,8 V Float bei AGM, 13,5–13,6 V bei Gel)
6. Ladegerät MUSS korrektes Profil für AGM/Gel haben — Flooded-Profil zerstört AGM/Gel!

**Protokoll LiFePO4:**
1. Batterie auf 50–60 % SoC entladen/laden (NICHT voll für Langzeitlagerung)
2. Spannung dokumentieren (Soll: ca. 13,15–13,25 V bei 4S-Konfiguration)
3. BMS-Status prüfen: Low-Temperature-Cutoff aktiv? (Pflicht unter 5 °C)
4. Batterie-Trennschalter AUS — BMS geht in Sleep-Mode
5. KEIN Erhaltungsladegerät anschließen! (nicht nötig, kann BMS stören)
6. Selbstentladung: < 3 %/Monat → nach 6 Monaten noch > 35 % SoC
7. Wenn Boot in Region mit Temperaturen < -20 °C: Batterie ausbauen und frostfrei lagern (BMS-Elektronik hat Temperaturgrenzen)
8. NIEMALS eine LiFePO4-Batterie unter 0 °C laden! Lithium-Plating zerstört die Zellen irreversibel.

**Protokoll Starterbatterie (unabhängig vom Typ):**
1. Voll laden
2. Starterkabel abklemmen (Minus zuerst, dann Plus)
3. Batterie isoliert lagern (kein Kontakt zu Metallteilen)
4. Monatlich Ruhespannung prüfen und bei < 12,4 V nachladen
5. Alternative: Separates Erhaltungsladegerät nur für Starterbatterie

### 3.5 Inbetriebnahme

#### 3.5.1 Ablauf der Inbetriebnahme nach Winterlager

Die Inbetriebnahme ist das Gegenstück zur Winterfestmachung. Sie muss in definierter Reihenfolge erfolgen:

**Schritt 1 — Visueller Check (alle Systeme noch AUS):**
- Sichtprüfung aller Kabel, Anschlüsse, Schalttafeln
- Bilge trocken? Kein Wassereinbruch über Winter?
- Nagetier-Spuren? (Kotrückstände, angefressene Isolation)
- Kondensation/Schimmel an Elektronik?

**Schritt 2 — Batterien vorbereiten:**
- Batterie-Ruhespannung messen (vor Anschluss an Bordnetz)
- Blei-Säure: Elektrolytstand prüfen
- Polklemmen reinigen und anschließen (Plus zuerst, Minus zuletzt)
- Batterie-Hauptschalter EIN

**Schritt 3 — DC-Basisversorgung:**
- Bilgenpumpe testen (Handschalter und Automatik)
- Bordspannung an Schalttafel prüfen
- Instrumentenbeleuchtung testen

**Schritt 4 — DC-Verbraucher einzeln einschalten:**
- Navigation (Chartplotter, GPS, AIS)
- Beleuchtung (Innen, Navigationslichter)
- Kühlschrank/Tiefkühler (Anlaufstrom beobachten)
- Pumpen (Frischwasser, Bilge, WC)
- UKW-Funk (Sendetest mit Frequenz 16 — kurze Testmeldung)
- Autopilot (Funktionstest am Steg)
- Instrumente (Log, Lot, Wind)

**Schritt 5 — Landstrom/AC-Versorgung:**
- Landstromkabel anschließen
- FI-Schutzschalter testen
- Bordspannung AC messen (230 V ±10 %)
- Ladegerät prüfen (Bulk/Absorption/Float)
- Warmwasserboiler, Heizung, Klimaanlage

**Schritt 6 — Motor-Elektrik:**
- Motorstart (Cranking-Spannung > 9,6 V?)
- Ladestrom Lichtmaschine messen
- Motorinstrumente (Öldruck, Temperatur, Drehzahl)
- Tankgeber (Kraftstoff, Frischwasser)

**Schritt 7 — Großverbraucher:**
- Ankerwinde (unter Last, Spannungsabfall messen)
- Bugstrahlruder (kurzer Test, Spannungsabfall und Kabelerwärmung)
- Elektrische Winschen

**Schritt 8 — Dokumentation:**
- Alle Messwerte protokollieren
- Vergleich mit Vorjahreswerten
- Auffälligkeiten notieren und planen

### 3.6 Notfallreparatur

#### 3.6.1 Notfallkit Elektrik

**Mindestausstattung Notfallkit (Confidence: documented):**

| Gegenstand | Menge | Zweck |
|------------|-------|-------|
| Multimeter (True RMS, wasserdicht) | 1 | Diagnose |
| Crimpzange (isolierte Verbinder) | 1 | Reparatur |
| Kabelsortiment (1 mm² – 6 mm²) | je 5 m | Ersatzkabel |
| Crimpverbinder-Sortiment (isoliert) | je 20 | Verbindungen |
| Schrumpfschlauch mit Kleber (sortiert) | je 10 | Isolation |
| Isolierband (Scotch Super 88+) | 2 Rollen | Provisorien |
| Sicherungssortiment (Flach + ATO) | je 5 | Sicherungsersatz |
| Kabelschere / Seitenschneider | 1 | Schneiden |
| Abisolierwerkzeug | 1 | Abisolieren |
| Kontaktspray (z.B. Ballistol Kontakt-Chemie) | 1 Dose | Kontaktpflege |
| Stirnlampe (unabhängig vom Bordnetz!) | 1 | Licht |
| Batterieklemmen (Not-) | 2 | Notanschluss |
| Kabelbinder (sortiert) | 50 | Befestigung |
| Spannungsprüfer (berührungslos) | 1 | Schnelltest |
| Schaltplan des Bootes (laminiert) | 1 | Referenz |

#### 3.6.2 Notfallszenarien und Sofortmaßnahmen

**Szenario 1 — Totalausfall DC-Bordnetz:**
1. Ruhe bewahren — Stirnlampe anschalten
2. Batterie-Hauptschalter prüfen (versehentlich AUS?)
3. Batteriepole prüfen (lose Klemme?)
4. Hauptsicherung prüfen (ANL-Sicherung oder Streifensicherung am Batteriepol)
5. Spannung direkt an Batterie messen
6. Falls Batterie OK: Kabel Batterie → Hauptschalter → Schalttafel durchmessen

**Szenario 2 — Totaler Startausfall Motor:**
1. Batteriespannung messen (> 12,4 V?)
2. Anlasser-Magnetschalter: Klicken hörbar?
   - Ja → Batterie zu schwach oder Kabel korrodiert (Spannungsabfall messen)
   - Nein → Zündschloss, Kabelsicherung oder Magnetschalter defekt
3. Notstart: Direkt am Magnetschalter brücken (30 → 50, Vorsicht!)
4. Alternativ: Starterbatterie mit Starthilfekabel von Verbraucherbatterie überbrücken

**Szenario 3 — Kabelbrand:**
1. SOFORT Batterie-Hauptschalter AUS
2. SOFORT Landstrom trennen (wenn möglich)
3. Brand mit CO₂- oder Pulverlöscher bekämpfen — KEIN Wasser auf Elektrik!
4. Brandstelle lokalisieren und isolieren
5. Ursache: Überlastung, Kurzschluss oder Kontakterwärmung
6. Beschädigten Kabelabschnitt komplett ersetzen, NICHT reparieren
7. Ursache beheben, bevor Wiederinbetriebnahme

**Szenario 4 — Navigationsbeleuchtung fällt aus (nachts auf See):**
1. Sofort: Taschenlampe / Stirnlampe als Ersatz (COLREG Regel 37)
2. Sicherung prüfen und ggf. ersetzen
3. Leuchtmittel prüfen (Ersatz-Navlichter immer an Bord)
4. Falls Kabel defekt: Provisorische Verkabelung legen
5. Falls alles erfolglos: Weißes Rundumlicht improvisieren (Regel 37)

**Szenario 5 — Bilgenpumpe fällt aus bei Wassereinbruch:**
1. Manuelle Bilgenpumpe nutzen (muss an Bord sein, CE-Vorschrift Kat. A/B)
2. Elektrische Pumpe: Sicherung prüfen
3. Schwimmerschalter prüfen (festgeklemmt? Schmutz?)
4. Pumpe direkt an Batterie anschließen (Notverkabelung, Sicherung nicht vergessen)
5. Zweite Bilgenpumpe (Backup) aktivieren

#### 3.6.3 Provisorische Reparaturen auf See

**Grundsatz:** Provisorische Reparaturen dienen ausschließlich dazu, die sichere Rückkehr in den Hafen zu ermöglichen. Sie müssen so schnell wie möglich durch eine fachgerechte Reparatur ersetzt werden. Jede provisorische Reparatur ist im Bordbuch zu dokumentieren.

**Provisorische Kabelverbindung:**
1. Beschädigtes Kabelende sauber abschneiden (kein Quetschen!)
2. 15 mm Isolierung abisolieren (sauberer Schnitt, keine Adern beschädigen)
3. Aderenden verdrillen
4. Wenn Crimpzange vorhanden: Marine-Crimpverbinder verwenden → beste Notlösung
5. Ohne Crimpzange: Western Union Splice (Adern ineinander verdrillen, mind. 5 Windungen)
6. Mit Isolierband (Scotch Super 88+) mindestens 3 Lagen übereinander wickeln
7. Bei Nässe: Zusätzlich selbstverschweißendes Silikonband (z.B. Rescue Tape) darüber
8. KEINE Lüsterklemmen in der Marine-Elektrik! Vibration löst sie, Kontakte korrodieren

**Provisorischer Sicherungsersatz:**
NIEMALS eine durchgebrannte Sicherung mit Draht, Alufolie oder anderen Überbrückungen ersetzen! Stattdessen:
- Sicherung aus einem weniger kritischen Stromkreis umstecken (z.B. Kabinenlicht → Bilgenpumpe)
- Universalsicherungs-Sortiment aus dem Notfallkit verwenden
- Wenn gar keine passende Sicherung verfügbar: NÄCHST KLEINERE Sicherung verwenden, nicht die nächst größere

**Provisorische Verkabelung (Bypass):**
Bei unterbrochenem Kabel, das nicht repariert werden kann (z.B. im Mast, unter Verkleidung):
1. Provisorisches Kabel von der Schalttafel direkt zum Verbraucher legen (außen)
2. Kabelquerschnitt: Mindestens gleich oder größer als Original
3. Sicherung nicht vergessen! Nächste passende Sicherung an der Schalttafel-Seite
4. Kabel mit Kabelbindern sichern, keine losen Enden
5. Markierung "PROVISORIUM" anbringen

**Wasserdichte Notverbindung (bei Decksdurchführung):**
1. Verbindung herstellen (Crimp oder Splice)
2. Schrumpfschlauch mit Kleber (wenn Heißluftfön vorhanden)
3. Alternativ: Selbstverschweißendes Silikonband → wasserdicht nach 24 h Aushärtung
4. Zusätzlich Denso-Band (Petrolatum-Band) als äußere Schutzschicht

#### 3.6.4 Häufigkeit von Notfallszenarien (Confidence: benchmark)

| Notfall-Szenario | Häufigkeit pro 1.000 Yachten/Jahr | Typische Kosten |
|------------------|-----------------------------------|-----------------|
| Batterie-Ausfall auf See | 45–80 | 200–1.500 EUR |
| Sicherungsproblem (Ausfall einzelner Stromkreis) | 120–200 | 10–50 EUR |
| Navigationslicht-Ausfall | 30–60 | 20–150 EUR |
| Bilgenpumpen-Ausfall | 15–30 | 50–300 EUR |
| Motor-Startversagen (elektrisch) | 25–50 | 50–500 EUR |
| Landstrom-Ausfall (Stecker/Kabel) | 80–150 | 30–200 EUR |
| Kabelbrand/Schmorschaden | 3–8 | 500–10.000+ EUR |
| Totaler DC-Ausfall | 5–12 | 200–5.000 EUR |
| Streustrom-Schaden (entdeckt) | 10–25 | 1.000–10.000+ EUR |
| Blitzschlag (Elektrik-Schaden) | 1–3 | 5.000–50.000+ EUR |

**Confidence-Bewertung dieses Abschnitts:**
- Checklisten: `documented` — ABYC E-11, Hersteller-Wartungsanleitungen
- Zeitaufwand/Kosten: `estimated` — Werft-Erfahrungswerte DACH
- Notfallmaßnahmen: `documented` — BSH, COLREG, Sicherheitshandbücher
- Häufigkeitsdaten: `benchmark` — Versicherungsstatistiken, Charterflotten-Analyse

---

## 4. Produktlinien und Spezifikationen

### 4.1 Fluke — Industriestandard-Messgeräte

#### 4.1.1 Fluke 87V Industrial Multimeter

**Hersteller:** Fluke Corporation, Everett, WA, USA
**Kategorie:** Digitales Multimeter (True RMS)
**Marine-Eignung:** Hervorragend — CAT III 1000V / CAT IV 600V, robustes Gehäuse

**Technische Daten (Confidence: measured — Hersteller-Datenblatt):**

| Parameter | Wert |
|-----------|------|
| DC Spannung | 0,1 mV – 1.000 V (±0,05 % + 1 dgt) |
| AC Spannung (True RMS) | 0,1 mV – 1.000 V (±0,7 % + 2 dgt) |
| DC Strom | 0,01 mA – 10 A (±0,2 % + 2 dgt) |
| AC Strom (True RMS) | 0,01 mA – 10 A (±1,0 % + 2 dgt) |
| Widerstand | 0,1 Ω – 50 MΩ (±0,2 % + 1 dgt) |
| Kapazität | 0,01 nF – 9.999 μF |
| Frequenz | 0,01 Hz – 200 kHz |
| Temperatur | -200 °C bis +1.090 °C (Typ K) |
| Auflösung | 20.000 Counts |
| Eingangsimpedanz | 10 MΩ (>10 GΩ bei Low-Z) |
| Durchgangsprüfer | Summer < 25 Ω, Reaktionszeit < 250 ms |
| Display | Dual-Display mit Bargraph |
| Schutzart | IP 42 (mit Holster IP 52) |
| Batterie | 9V (6LR61), ca. 400 h |
| Gewicht | 355 g |
| Preis (UVP) | ca. 450 EUR |

**Besondere Marine-Vorteile:**
- Low-Z-Funktion: Eliminiert Geisteranzeigen durch kapazitive Kopplung (häufig in dichten Kabelbäumen an Bord)
- Min/Max/Average-Aufzeichnung: Erkennt intermittierende Spannungseinbrüche (z.B. beim Anlasserstart)
- Gleitender Mittelwert: Stabilisiert Anzeige bei schwankenden Spannungen (typisch Bordnetz unter Last)
- Temperaturmessung: Ermöglicht Überwachung von Kabeltemperaturen direkt mit dem DMM

#### 4.1.2 Fluke 376 FC True-RMS AC/DC Clamp Meter

**Hersteller:** Fluke Corporation
**Kategorie:** Zangenamperemeter mit Flexsensor
**Marine-Eignung:** Exzellent — misst DC bis 999 A, ideal für Batterie-Ladeströme

**Technische Daten (Confidence: measured):**

| Parameter | Wert |
|-----------|------|
| AC Strom (Zange) | 0,1 A – 999 A (±2,0 %) |
| DC Strom (Zange) | 0,1 A – 999 A (±2,0 %) |
| AC Strom (iFlex Sensor) | 0,5 A – 2.500 A (±3,0 %) |
| AC Spannung | 0,1 V – 1.000 V |
| DC Spannung | 0,1 V – 1.000 V |
| Widerstand | 0,1 Ω – 60 kΩ |
| Zangenöffnung | 34 mm (feste Zange) |
| iFlex-Sensor | Bis 178 mm Leiterdurchmesser |
| CAT-Rating | CAT III 1000V / CAT IV 600V |
| Bluetooth (Fluke Connect) | Ja — Fernablesung per Smartphone |
| Gewicht | 380 g |
| Preis (UVP) | ca. 650 EUR |

**Besondere Marine-Vorteile:**
- DC-Messung bis 999 A: Erfasst selbst Anlasserströme und Bugstrahlruder-Spitzenströme
- iFlex-Sensor: Flexibler Rogowski-Sensor für Kabel, die nicht in die Zange passen (dicke Batteriekabel)
- Fluke Connect Bluetooth: Werte können per Smartphone aus der Ferne abgelesen werden — ideal, wenn der Messort schlecht einsehbar ist (Motorraum, hinter Schalttafel)
- Inrush-Funktion: Erfasst den Einschaltstromstoß von Kompressoren und Motoren

### 4.2 Megger — Isolationsmessgeräte

#### 4.2.1 Megger MIT420/2 Isolationsmessgerät

**Hersteller:** Megger Group Ltd., Dover, UK
**Kategorie:** Isolationsmessgerät (Megger)
**Marine-Eignung:** Exzellent — speziell für Marine und industrielle Anwendungen konzipiert

**Technische Daten (Confidence: measured):**

| Parameter | Wert |
|-----------|------|
| Prüfspannungen | 10 V, 25 V, 50 V, 100 V, 250 V, 500 V, 1.000 V DC |
| Isolationswiderstand | 0,01 MΩ – 200 GΩ |
| Genauigkeit | ±3 % bei Nennbedingungen |
| Durchgangsprüfung | 0,01 Ω – 100 kΩ (200 mA Prüfstrom) |
| Polarisierungsindex (PI) | Automatische Berechnung R_10min / R_1min |
| DAR (Dielectric Absorption Ratio) | Automatische Berechnung R_60s / R_15s |
| Timer-Test | 1–10 Minuten (Trendmessung) |
| CAT-Rating | CAT IV 600V |
| Schutzart | IP 54 |
| Bluetooth | Ja (Datentransfer) |
| Batterie | 8× AA, ca. 1.500 Tests |
| Gewicht | 850 g |
| Preis (UVP) | ca. 750 EUR |

**Marine-relevante Funktionen:**
- Stufenlose Prüfspannung 10–1.000 V: Niedrige Spannung (50 V) für empfindliche Elektronik-Stromkreise, 500 V Standard für Bordnetz
- Automatischer Entladevorgang nach Messung: Sicherheit bei kapazitiven Lasten
- Live-Schaltkreis-Warnung: Warnt, wenn der Stromkreis noch unter Spannung steht
- Trendanzeige: Visualisiert den Isolationswiderstand über die Messzeit (Feuchtigkeit vs. echte Beschädigung)

### 4.3 Hioki — Präzisionsmessgeräte

#### 4.3.1 Hioki DT4282 Digital Multimeter

**Hersteller:** Hioki E.E. Corporation, Ueda, Japan
**Kategorie:** Digitales Multimeter (True RMS), Premium-Klasse
**Marine-Eignung:** Gut — sehr hohe Genauigkeit, robustes Gehäuse

**Technische Daten (Confidence: measured):**

| Parameter | Wert |
|-----------|------|
| DC Spannung | 60,000 mV – 1.000 V (±0,025 % + 3 dgt) |
| AC Spannung (True RMS) | 6,0000 V – 1.000 V (±0,3 % + 10 dgt) |
| DC Strom | 600,00 μA – 10 A (±0,15 % + 3 dgt) |
| Widerstand | 60,000 Ω – 600 MΩ (±0,3 % + 3 dgt) |
| Kapazität | 1,000 nF – 100,0 mF |
| Auflösung | 60.000 Counts |
| Eingangsimpedanz | 10 MΩ |
| CAT-Rating | CAT III 1000V / CAT IV 600V |
| Durchgangsprüfer | < 25 Ω, Reaktionszeit < 50 ms |
| Schutzart | IP 40 (mit Tasche IP 50) |
| Gewicht | 360 g |
| Preis (UVP) | ca. 380 EUR |

**Marine-Vorteile:**
- Extrem schneller Durchgangsprüfer (< 50 ms): Erkennt intermittierende Kabelbrüche, die andere Geräte verpassen
- Hohe Auflösung (60.000 Counts): Exakte Spannungsabfall-Messungen im mV-Bereich
- Temperaturmessung integriert

#### 4.3.2 Hioki CM4376 AC/DC Clamp Meter

**Hersteller:** Hioki E.E. Corporation
**Kategorie:** Zangenamperemeter, True RMS
**Marine-Eignung:** Hervorragend für DC-Diagnose

**Technische Daten (Confidence: measured):**

| Parameter | Wert |
|-----------|------|
| DC Strom | 0,01 A – 1.000 A (±0,9 % + 5 dgt) |
| AC Strom | 0,01 A – 1.000 A (±1,3 % + 5 dgt) |
| DC Spannung | 0,1 mV – 1.500 V |
| AC Spannung | 0,1 mV – 1.000 V |
| Widerstand | 0,1 Ω – 60 MΩ |
| Zangenöffnung | 33 mm |
| Inrush-Messung | Ja (Halbwellen-RMS) |
| Bluetooth | Ja (GATT) |
| CAT-Rating | CAT III 1000V / CAT IV 600V |
| Gewicht | 310 g |
| Preis (UVP) | ca. 520 EUR |

### 4.4 Victron Energy — Batterie-Monitoring

#### 4.4.1 Victron SmartShunt 500A

**Hersteller:** Victron Energy BV, Almere, Niederlande
**Kategorie:** Batteriemonitor (Shunt-basiert)
**Marine-Eignung:** Exzellent — De-facto-Standard auf modernen Yachten

**Technische Daten (Confidence: measured):**

| Parameter | Wert |
|-----------|------|
| Messbereich Strom | -500 A bis +500 A |
| Auflösung Strom | 0,01 A |
| Genauigkeit Strom | ±0,4 % |
| Messbereich Spannung | 6,5–70 V DC |
| Auflösung Spannung | 0,01 V |
| Midpoint-Spannungsmessung | Optional (zweiter Eingang) |
| Temperaturmessung | Ja (externer Sensor beiliegend) |
| Kommunikation | Bluetooth Low Energy (BLE) |
| App | VictronConnect (iOS, Android) |
| VE.Direct-Port | Ja (für GX-Geräte, Cerbo GX) |
| Eigenverbrauch | < 1 mA |
| Shunt-Widerstand | 0,2 mΩ (500 A = 0,1 V Abfall) |
| Schutzart | IP 21 (Shunt) |
| Gewicht | 85 g (nur Shunt) |
| Preis (UVP) | ca. 80 EUR |

**Funktionen:**
- SoC-Berechnung: Coulomb-Counting + synchronization bei Volladung
- Verlaufshistorie: Min/Max-Spannung, tiefste Entladung, Zyklenanzahl, Ah-Verbrauch
- Trend: Restlaufzeit bei aktuellem Verbrauch
- Alarme: Konfigurierbare Spannungs-, Strom- und SoC-Alarme via App
- NMEA 2000-kompatibel (über VE.Direct-to-NMEA-2000-Interface)

#### 4.4.2 Victron BMV-712 Smart

**Hersteller:** Victron Energy BV
**Kategorie:** Batteriemonitor mit Display
**Marine-Eignung:** Exzellent — gleiche Funktion wie SmartShunt, zusätzlich Panelmeter

**Technische Daten (Confidence: measured):**

| Parameter | Wert |
|-----------|------|
| Messbereich Strom | -500 A bis +500 A |
| Display | LCD, hintergrundbeleuchtet |
| Anzeigen | Spannung, Strom, SoC, Leistung, Restlaufzeit |
| Relay-Ausgang | 1× programmierbar (60 V / 1 A) |
| Zweiter Batterie-Eingang | Ja (Starterbank-Überwachung) |
| Bluetooth | Ja |
| VE.Direct | Ja |
| Einbaumaß | 69 × 69 mm |
| Preis (UVP) | ca. 155 EUR |

**Unterschied SmartShunt vs. BMV-712:**
- SmartShunt: Kein eigenes Display — Ablesung nur über App. Ideal für vernetzte Systeme (GX-Display).
- BMV-712: Einbau-Display am Navigationsplatz. Ideal, wenn kein GX-Gerät vorhanden.

### 4.5 Marinco — Steckverbinder und Landstrom

#### 4.5.1 Marinco Landstrom-Steckverbinder

**Hersteller:** Marinco (BEP Marine / Actuant), Menomonee Falls, WI, USA
**Kategorie:** Landstrom-Einspeisung, Steckverbinder
**Marine-Eignung:** Industriestandard für Landstrom-Systeme

**Produktlinie 16A (Europa, CEE-kompatibel):**

| Modell | Typ | Nennstrom | Spannung | IP | Preis (ca.) |
|--------|-----|-----------|----------|----|-------------|
| 16A Inlet (303SSEL) | Einlass (Boot) | 16 A | 230 V AC | IP 66 | 75–110 EUR |
| 16A Cord Set (15 m) | Anschlusskabel | 16 A | 230 V AC | IP 44 | 120–180 EUR |
| 16A Adapter Y | Verteiler | 2× 16 A | 230 V AC | IP 44 | 85–130 EUR |

**Produktlinie 32A (Europa):**

| Modell | Typ | Nennstrom | Spannung | IP | Preis (ca.) |
|--------|-----|-----------|----------|----|-------------|
| 32A Inlet (6373EL) | Einlass (Boot) | 32 A | 230 V AC | IP 66 | 110–160 EUR |
| 32A Cord Set (25 m) | Anschlusskabel | 32 A | 230 V AC | IP 44 | 200–320 EUR |
| 32A Adapter 32→16 | Reduzierung | 16 A (limitiert) | 230 V AC | IP 44 | 45–70 EUR |

**Wartungshinweise Marinco-Stecker:**
- Kontaktstifte halbjährlich mit Kontaktfett (z.B. Marinco Moisture Guard) behandeln
- Dichtungsringe jährlich auf Elastizität prüfen, ggf. ersetzen
- Bajonettverschluss auf korrekten Sitz prüfen (häufige Fehlerquelle!)
- UV-exponierte Kabel alle 5 Jahre auf Sprödigkeit prüfen
- Brandmarken an Kontakten = sofort ersetzen

### 4.6 Weitere relevante Messgeräte

#### 4.6.1 Fluke 1587 FC Insulation Multimeter

Kombination aus Isolationsmessgerät und True-RMS-Multimeter in einem Gerät. Ideal für die Marine-Wartung, da nur ein Gerät mitgeführt werden muss.

**Technische Daten (Confidence: measured):**

| Parameter | Wert |
|-----------|------|
| Isolations-Prüfspannungen | 50, 100, 250, 500, 1.000 V DC |
| Isolationswiderstand | 0,01 MΩ – 2 GΩ |
| DC Spannung | 0,1 mV – 1.000 V |
| AC Spannung (True RMS) | 0,1 mV – 1.000 V |
| Widerstand | 0,1 Ω – 50 MΩ |
| PI (Polarisierungsindex) | Ja |
| DAR | Ja |
| Fluke Connect (Bluetooth) | Ja |
| CAT-Rating | CAT III 1000V / CAT IV 600V |
| Preis (UVP) | ca. 900 EUR |

#### 4.6.2 FLIR C5 Kompakt-Wärmebildkamera

**Hersteller:** Teledyne FLIR, Wilsonville, OR, USA
**Kategorie:** Kompakte Infrarot-Kamera
**Marine-Eignung:** Gut — klein genug für die Bordwerkzeugkiste

**Technische Daten (Confidence: measured):**

| Parameter | Wert |
|-----------|------|
| IR-Auflösung | 160 × 120 Pixel |
| Thermische Empfindlichkeit (NETD) | < 70 mK |
| Temperaturbereich | -20 °C bis +400 °C |
| Genauigkeit | ±3 °C oder ±3 % |
| Sichtfeld | 54° × 42° |
| Visuelles Bild | 5 Mpx |
| MSX-Bildverbesserung | Ja (überlagert Konturen) |
| WiFi | Ja (Cloud-Upload) |
| Display | 3,5" Touchscreen |
| Akku | Ca. 4 h |
| Schutzart | IP 54 |
| Abmessungen | 133 × 81 × 28 mm |
| Preis (UVP) | ca. 550 EUR |

**Confidence-Bewertung dieses Abschnitts:**
- Technische Daten: `measured` — Hersteller-Datenblätter
- Preise: `estimated` — Marktpreise DACH 2024/2025, Stand Mai 2026
- Marine-Eignung: `documented` — Anwendungsberichte, Fachliteratur

---

## 5. Hersteller-Datenbank

### 5.1 Fluke Corporation

| Feld | Information |
|------|------------|
| **Firmenname** | Fluke Corporation |
| **Hauptsitz** | 6920 Seaway Blvd, Everett, WA 98203, USA |
| **Gründung** | 1948 |
| **Muttergesellschaft** | Fortive Corporation |
| **Umsatz (geschätzt)** | > 1 Mrd. USD |
| **Mitarbeiter** | > 3.000 |
| **Website** | www.fluke.com |
| **Marine-Relevanz** | Industriestandard für DMM und Zangenamperemeter, weit verbreitet auf Werften und bei Marine-Elektrikern |
| **Support DACH** | Fluke Deutschland GmbH, Glottertal |
| **Garantie** | 3 Jahre (DMM), 2 Jahre (Zangen) |
| **Kalibrierservice** | Ja, weltweit, auch DAkkS-akkreditiert über Partner |
| **Relevante Produkte** | 87V, 117, 179, 376 FC, 1587 FC, ScopeMeter 120B/190 |
| **Preissegment** | Premium (200–2.500 EUR) |

### 5.2 Megger Group

| Feld | Information |
|------|------------|
| **Firmenname** | Megger Group Limited |
| **Hauptsitz** | Archcliffe Road, Dover, Kent CT17 9EN, UK |
| **Gründung** | 1889 (als "Evershed & Vignoles") |
| **Markenname** | "Megger" ist zum Gattungsbegriff für Isolationsmessgeräte geworden |
| **Website** | www.megger.com |
| **Marine-Relevanz** | Standard für Isolationsmessungen, von Surveyors und Versicherungen anerkannt |
| **Support DACH** | Megger GmbH, Baunach (Bayern) |
| **Garantie** | 3 Jahre |
| **Relevante Produkte** | MIT420/2, MIT430/2, MIT480/2, MFT1741 |
| **Preissegment** | Premium (400–3.000 EUR) |

### 5.3 Hioki E.E. Corporation

| Feld | Information |
|------|------------|
| **Firmenname** | Hioki E.E. Corporation |
| **Hauptsitz** | 81 Koizumi, Ueda, Nagano 386-1192, Japan |
| **Gründung** | 1935 |
| **Börsennotierung** | Tokyo Stock Exchange (6866) |
| **Website** | www.hioki.com |
| **Marine-Relevanz** | Hochpräzise Messgeräte, besonders schneller Durchgangsprüfer, in Asien und Europa wachsend |
| **Support DACH** | Hioki Europe GmbH, Eschborn |
| **Garantie** | 3 Jahre |
| **Relevante Produkte** | DT4282, CM4376, IR4057, BT3554 (Batterietester) |
| **Preissegment** | Mittel bis Premium (200–1.500 EUR) |

### 5.4 Victron Energy

| Feld | Information |
|------|------------|
| **Firmenname** | Victron Energy B.V. |
| **Hauptsitz** | De Paal 35, 1351 JG Almere, Niederlande |
| **Gründung** | 1975 |
| **Inhaber** | Familienunternehmen (Reinout Vader) |
| **Website** | www.victronenergy.com |
| **Marine-Relevanz** | Marktführer für Batteriemonitoring, Ladegeräte, Wechselrichter auf Yachten im europäischen Markt |
| **Support DACH** | Direkt + umfangreiches Händlernetzwerk, Victron Professional Portal |
| **Garantie** | 5 Jahre |
| **Open Source** | VRM-Portal kostenlos, VE.Direct-Protokoll dokumentiert |
| **Relevante Produkte** | SmartShunt, BMV-712, SmartSolar MPPT, MultiPlus, Cerbo GX |
| **Preissegment** | Mittel (60–3.000 EUR) |

### 5.5 Marinco / BEP Marine

| Feld | Information |
|------|------------|
| **Firmenname** | Marinco (Marke von BEP Marine) |
| **Hauptsitz** | Menomonee Falls, WI, USA / BEP: Auckland, NZ |
| **Muttergesellschaft** | Actuant Corporation → Enerpac Tool Group |
| **Website** | www.marinco.com / www.bepmarine.com |
| **Marine-Relevanz** | Standard für Landstrom-Steckverbinder, Batterieschalter, Verteilerpanele weltweit |
| **Support DACH** | Über Fachhändler (SVB, Toplicht, Compass, AWN) |
| **Garantie** | 2 Jahre (Steckverbinder), 5 Jahre (Schalter) |
| **Relevante Produkte** | Landstrom-Inlets, Power Cord Sets, Batterieschalter, CruiseGard Galvanischer Isolator |
| **Preissegment** | Mittel (30–350 EUR) |

### 5.6 Teledyne FLIR

| Feld | Information |
|------|------------|
| **Firmenname** | Teledyne FLIR LLC |
| **Hauptsitz** | 27700 SW Parkway Ave, Wilsonville, OR 97070, USA |
| **Muttergesellschaft** | Teledyne Technologies |
| **Gründung** | 1978 (als FLIR Systems) |
| **Website** | www.flir.com |
| **Marine-Relevanz** | Marktführer Wärmebildkameras; Modelle C3/C5 ideal für Elektrik-Diagnose an Bord |
| **Support DACH** | Teledyne FLIR, Frankfurt am Main |
| **Garantie** | 2 Jahre (Kamera), 10 Jahre (Sensor) |
| **Relevante Produkte** | C5, ONE Pro, E54, maritime Kameras (M-Serie) |
| **Preissegment** | Mittel bis Premium (300–15.000 EUR) |

### 5.7 CTEK Sweden AB

| Feld | Information |
|------|------------|
| **Firmenname** | CTEK Sweden AB |
| **Hauptsitz** | Rostugnsvägen 3, 776 30 Vikmanshyttan, Schweden |
| **Gründung** | 1997 |
| **Website** | www.ctek.com |
| **Marine-Relevanz** | Marktführer für kompakte Erhaltungsladegeräte und Batterieladegeräte, ideal für Winterlager |
| **Support DACH** | CTEK GmbH, Kornwestheim |
| **Garantie** | 5 Jahre |
| **Relevante Produkte** | MXS 5.0, MXS 10, D250SE (DC-DC), Smartpass 120S |
| **Preissegment** | Mittel (80–400 EUR) |
| **Besonderheit Marine** | MXS 5.0 hat "Recond"-Modus für Desulfatierung, wasserdicht IP 65, ideal für Winterlager-Erhaltungsladung |

### 5.8 Kastar / Blue Sea Systems

| Feld | Information |
|------|------------|
| **Firmenname** | Blue Sea Systems |
| **Hauptsitz** | Bellingham, WA, USA |
| **Muttergesellschaft** | Actuant → Enerpac |
| **Website** | www.bluesea.com |
| **Marine-Relevanz** | Führend bei Marine-Schalttafeln, Sicherungsblöcken, Batterieschaltern und Diagnosezubehör |
| **Support DACH** | Über Fachhändler |
| **Garantie** | 5 Jahre |
| **Relevante Produkte** | ST Blade Sicherungsblöcke, ML-ACR Laderelais, m-LVD Unterspannungsschutz, Digital Multimeter 8015 |
| **Preissegment** | Mittel (20–400 EUR) |

### 5.9 Knipex / Weidmüller — Crimpwerkzeuge

| Feld | Information |
|------|------------|
| **Firmenname (Crimpen)** | Knipex-Werk C. Gustav Putsch KG |
| **Hauptsitz** | Oberkamper Str. 13, 42349 Wuppertal, Deutschland |
| **Gründung** | 1882 |
| **Website** | www.knipex.de |
| **Marine-Relevanz** | Professionelle Crimpzangen (97er-Serie), Kabelschere, Abisolierwerkzeug — Industriestandard in DACH-Werften |
| **Relevante Produkte** | 97 21 215 (isolierte Kabelverbinder), 97 22 240 (unisoliert), 97 49 xx (Wechseleinsätze), 95 12 200 (Kabelschere) |
| **Preissegment** | Premium (50–250 EUR) |
| **Garantie** | Lebenslang (bei bestimmungsgemäßem Gebrauch) |

### 5.10 Ancor / Marinco — Marine-Kabel und Verbinder

| Feld | Information |
|------|------------|
| **Firmenname** | Ancor Marine Grade (Marke von Actuant/BEP) |
| **Hauptsitz** | Menomonee Falls, WI, USA |
| **Website** | www.ancorproducts.com |
| **Marine-Relevanz** | Führend bei Marine-Grade-Kabeln (tinned copper), Crimpverbindern, Schrumpfschläuchen mit Kleber |
| **Support DACH** | Über Fachhändler (SVB, Toplicht, Compass) |
| **Relevante Produkte** | Marine-Grade-Kabel (alle Querschnitte), Heat Shrink Connectors, Battery Cable, Butt Splices |
| **Preissegment** | Mittel (Marine-Kabel ca. 2–8 EUR/m je Querschnitt) |
| **Besonderheit** | Alle Kabel UL 1426 Marine-zertifiziert, verzinntes Kupfer (Korrosionsschutz), SAE J1127/J1128 konform |

**Confidence-Bewertung dieses Abschnitts:**
- Firmendaten: `documented` — öffentliche Quellen, Handelsregister
- Produktdaten: `measured` — Hersteller-Datenblätter
- Preise: `estimated` — DACH-Marktpreise Stand 2024/2025

---

## 6. Fehlerbild-Atlas

### 6.1 Fehlerbild: Grünspan an Kupfer-Crimpverbindungen

| Feld | Beschreibung |
|------|-------------|
| **Fehlerbild-ID** | EW-FB-001 |
| **Bezeichnung** | Grünspan (Kupfer(II)-carbonat) an Crimpverbindungen |
| **Visuelles Erscheinungsbild** | Grün-türkise, pulvrige bis krustige Ablagerungen auf Kupferoberflächen, insbesondere an der Übergangsstelle Crimpverbinder ↔ Kabel |
| **Ort / Häufigkeit** | Motorraum (70 %), Bilge-Bereich (20 %), Decksdurchführungen (10 %) |
| **Ursache** | Feuchtigkeit + Salz + Kupfer → Oxidation → Cu₂(OH)₂CO₃. Verstärkt durch unzureichende Isolierung der Crimpstelle, fehlenden Schrumpfschlauch, Vibration |
| **Auswirkung** | Erhöhter Übergangswiderstand (50–500 mΩ statt < 5 mΩ), Erwärmung, intermittierende Ausfälle, Spannungsabfall |
| **Messwert** | Spannungsabfall über Verbindung > 100 mV unter Last |
| **Schweregrad** | Mittel (B) — bei Ausbreitung: Hoch (C) |
| **Sofortmaßnahme** | Verbindung trennen, reinigen (Messingbürste), neu crimpen mit Marine-Grade-Verbinder + Doppelwand-Schrumpfschlauch mit Kleber |
| **Langfristmaßnahme** | Alle Crimpverbindungen im betroffenen Bereich auf Marine-Grade umstellen, Belüftung verbessern |
| **AYDI Visual Detection** | `visual_high` — charakteristische Grünfärbung eindeutig erkennbar |

### 6.2 Fehlerbild: Geschmorte Sicherungshalter

| Feld | Beschreibung |
|------|-------------|
| **Fehlerbild-ID** | EW-FB-002 |
| **Bezeichnung** | Thermische Schädigung eines Sicherungshalters |
| **Visuelles Erscheinungsbild** | Bräunlich-schwarze Verfärbung des Kunststoffs um die Sicherungskontakte, geschmolzene oder verformte Kontaktfedern, Brandgeruch |
| **Ort / Häufigkeit** | Schalttafel (60 %), Motorraum-Sicherungsbox (30 %), dezentrale Sicherungen (10 %) |
| **Ursache** | Korrodierte oder lose Kontaktfedern → erhöhter Übergangswiderstand → I²R-Erwärmung → Kunststoff schmilzt → noch schlechterer Kontakt → Eskalation. Oft durch falsche Sicherungsgröße oder Billig-Sicherungen verstärkt |
| **Auswirkung** | Brandgefahr (Stufe: Kritisch), Sicherung löst nicht korrekt aus, Spannungsabfall am Verbraucher |
| **Messwert** | Thermografie: ΔT > 35 °C zum Nachbar-Halter. Spannungsabfall > 500 mV |
| **Schweregrad** | Hoch (C) bis Kritisch (D) |
| **Sofortmaßnahme** | Sicherung ziehen, Stromkreis außer Betrieb nehmen. Kompletten Sicherungshalter ersetzen (nicht nur Sicherung!). Kabelenden neu abisolieren und crimpen |
| **Langfristmaßnahme** | Hochwertigen Sicherungsblock (z.B. Blue Sea ST Blade) installieren, alle Sicherungswerte verifizieren |
| **AYDI Visual Detection** | `visual_high` — Verfärbung und Verformung visuell eindeutig |

### 6.3 Fehlerbild: Korrodierte Batteriepole

| Feld | Beschreibung |
|------|-------------|
| **Fehlerbild-ID** | EW-FB-003 |
| **Bezeichnung** | Sulfat-Korrosion an Batteriepolen |
| **Visuelles Erscheinungsbild** | Weiße bis bläulich-grüne, kristalline Ablagerungen an Batteriepolen und Polklemmen. Bei Blei-Säure: weiße Bleisulfat-Kristalle. Bei Kupferklemmen: grün-blaues Kupfersulfat |
| **Ort / Häufigkeit** | Batteriebank (90 %), Starterbatterie (10 %) |
| **Ursache** | Ausgasung der Blei-Säure-Batterie (Schwefelsäure-Dämpfe) + Feuchtigkeit + Metall → Sulfatbildung. Verstärkt durch Überladung, undichte Zellenstopfen, mangelnde Belüftung |
| **Auswirkung** | Erhöhter Übergangswiderstand (bis zu mehrere Ohm!), Ladestörungen, Startprobleme, Spannungsabfall unter Last. Im Extremfall Kontaktverlust |
| **Messwert** | Spannungsabfall Batteriepol → Kabelende > 200 mV bei 50 A |
| **Schweregrad** | Mittel (B) bis Hoch (C) |
| **Sofortmaßnahme** | Polklemmen abschrauben, Korrosion mit Natronlauge (Backpulver + Wasser) neutralisieren, Messingbürste reinigen, Polfett auftragen |
| **Langfristmaßnahme** | Polklemmen auf Marine-Grade (vergoldet oder verzinnt) umstellen, Batterieraum-Belüftung optimieren, Ladeparameter prüfen (Überladung?) |
| **AYDI Visual Detection** | `visual_high` — weiß-bläuliche Kristallbildung eindeutig |

### 6.4 Fehlerbild: Spröde Kabelisolierung

| Feld | Beschreibung |
|------|-------------|
| **Fehlerbild-ID** | EW-FB-004 |
| **Bezeichnung** | UV- und thermische Degradation der Kabelisolierung |
| **Visuelles Erscheinungsbild** | PVC-Isolierung ist verhärtet, brüchig, zeigt Risse oder bricht beim Biegen. Farbe ist ausgeblichen (UV) oder dunkel verfärbt (thermisch). Kupferleiter teilweise sichtbar |
| **Ort / Häufigkeit** | Motorraum (40 %), Decksdurchführungen (30 %), Mastfuß (15 %), Achterkajüte über Maschine (15 %) |
| **Ursache** | UV-Strahlung (Deck), Hitze >80 °C (Motorraum), Ozon (Motorabgase), chemische Einwirkung (Diesel, Öl). PVC-Weichmacher verdampft über Zeit, Isolierung wird spröde |
| **Auswirkung** | Isolationsfehler → Kurzschluss- und Brandgefahr. Streustrom bei Seewasserkontakt. Isolationswiderstand < 1 MΩ |
| **Messwert** | Megger-Test: Isolationswiderstand < 2 MΩ (kritisch < 0,5 MΩ) |
| **Schweregrad** | Hoch (C) — Brandgefahr |
| **Sofortmaßnahme** | Betroffenen Kabelabschnitt sofort ersetzen (nicht flicken!). Bis zum Austausch: Sicherung reduzieren oder Stromkreis abschalten |
| **Langfristmaßnahme** | Kabel im Motorraum auf hitzebeständiges XLPE oder Silikon-Kabel (180 °C) umstellen. Kabel an Deck mit UV-beständiger Ummantelung versehen |
| **AYDI Visual Detection** | `visual_medium` — Sprödigkeit nicht immer visuell erkennbar, Rissbildung erst bei genauem Hinsehen |

### 6.5 Fehlerbild: Streustrom-Korrosion am Propeller

| Feld | Beschreibung |
|------|-------------|
| **Fehlerbild-ID** | EW-FB-005 |
| **Bezeichnung** | Elektrolytische Streustrom-Korrosion an Bronze-/Alu-Propeller |
| **Visuelles Erscheinungsbild** | Rapider Materialverlust, "angefressene" Oberfläche, pitting, scharfe Kanten an Angriffsstellen. Bei Aluminium: weiße Pulverablagerungen. Bei Bronze: grüne Patina + Materialabtrag |
| **Ort / Häufigkeit** | Propeller (50 %), Welle (20 %), Seeventile (15 %), Kiel-Bolzen (15 %) |
| **Ursache** | Fehler in der Bordnetz-Isolation → DC-Leckstrom fließt über Seewasser. Häufig: defekter Landstrom-Isolator, fehlende AC-Erdung, Nachbarboot mit Elektrik-Fehler |
| **Auswirkung** | Materialabtrag bis zu 10 kg/Jahr bei 1 A Streustrom. Propeller-Unwucht, Wellenvibration, Seeventil-Versagen (Durchbruchgefahr!) |
| **Messwert** | Referenzelektroden-Messung: Potential > -500 mV vs. Ag/AgCl = aktive Korrosion. Leckstrom am Landstromkabel > 100 mA |
| **Schweregrad** | Kritisch (D) — Sicherheitsrelevant (Seeventil-Versagen → Untergang) |
| **Sofortmaßnahme** | Landstrom sofort trennen. Streustromquelle identifizieren (eigenes Boot? Nachbar?). Alle Massen messen |
| **Langfristmaßnahme** | Galvanischen Isolator installieren (Marinco CruiseGard, ProSafe). Bordnetz-Isolationsmessung. Opferanoden-System überprüfen |
| **AYDI Visual Detection** | `visual_medium` — Unterwasserbefund, Foto bei Kranen/Taucher erforderlich |

### 6.6 Fehlerbild: Defekter Laderegler (Überladung)

| Feld | Beschreibung |
|------|-------------|
| **Fehlerbild-ID** | EW-FB-006 |
| **Bezeichnung** | Lichtmaschinen-Laderegler defekt — Überladung |
| **Visuelles Erscheinungsbild** | Batterien gasen übermäßig (Schwefelgeruch), Elektrolytstand sinkt rapide, Batterie-Gehäuse aufgebläht, Batteriepole stark korrodiert, Ladespannung > 15,5 V (12V-System) |
| **Ort / Häufigkeit** | Motorraum / Lichtmaschine (100 %) |
| **Ursache** | Laderegler-Defekt (Thyristor kurzgeschlossen), lose Regler-Masseverbindung, falscher Regler-Typ für Batteriechemie |
| **Auswirkung** | Batterie-Überladung → übermäßige Gasung → Wasserverlust → Plattenfreilegung → Zerstörung. Bei AGM/Gel: Irreversibel! Bei LiFePO4: BMS schaltet ab (Schutzmechanismus) |
| **Messwert** | Ladespannung > 14,8 V (Flooded), > 14,4 V (AGM/Gel), > 14,6 V (LiFePO4) bei laufendem Motor = Überladung |
| **Schweregrad** | Hoch (C) — Batteriezerstörung, Gasung = Explosionsgefahr (Knallgas) |
| **Sofortmaßnahme** | Motor abstellen. Ladespannung messen. Batterie-Temperatur fühlen (> 50 °C = Gefahr). Batterieraum belüften (Knallgas!) |
| **Langfristmaßnahme** | Laderegler tauschen. Externen Hochleistungs-Regler (z.B. Balmar MC-614, Mastervolt Alpha Pro III) mit korrekte Batterie-Kennlinie installieren |
| **AYDI Visual Detection** | `visual_low` — Überladung visuell erst bei massiven Schäden erkennbar |

### 6.7 Fehlerbild: FI-Schutzschalter löst nicht aus

| Feld | Beschreibung |
|------|-------------|
| **Fehlerbild-ID** | EW-FB-007 |
| **Bezeichnung** | Fehlstromschutzschalter (RCD/FI) funktionsunfähig |
| **Visuelles Erscheinungsbild** | Prüftaste bewirkt keine Auslösung. Äußerlich unauffällig. Kontakte innen korrodiert oder Magnetauslöser festgesetzt |
| **Ort / Häufigkeit** | AC-Schalttafel (100 %) |
| **Ursache** | Korrosion durch Marine-Umgebung, mangelnde Betätigung (Mechanismus verharzt), Alterung der Auslösespule, Feuchtigkeit im Gehäuse |
| **Auswirkung** | Kein Personenschutz bei Erdschluss im AC-Netz! Lebensgefahr bei Berührung spannungsführender Teile. Kein Schutz gegen Streustrom über Landstrom |
| **Messwert** | FI-Testgerät: Auslösezeit > 300 ms (soll < 40 ms bei Typ A 30 mA) oder keine Auslösung |
| **Schweregrad** | Kritisch (D) — Lebensgefahr |
| **Sofortmaßnahme** | FI-Schutzschalter sofort ersetzen. Bis dahin: Landstrom-Nutzung minimieren, Erdkontakt vermeiden |
| **Langfristmaßnahme** | FI-Schutzschalter monatlich mit Prüftaste testen. Alle 5 Jahre durch Fachbetrieb mit Messgerät testen. Marine-Grade FI verwenden |
| **AYDI Visual Detection** | `visual_insufficient` — Fehler nur durch elektrische Prüfung erkennbar |

### 6.8 Fehlerbild: Elektromagnetische Störungen (EMV)

| Feld | Beschreibung |
|------|-------------|
| **Fehlerbild-ID** | EW-FB-008 |
| **Bezeichnung** | EMV-Störungen durch mangelhafte Verkabelung |
| **Visuelles Erscheinungsbild** | Keine direkt sichtbaren Schäden. Symptome: Kompassabweichung, GPS-Positionssprünge, Rauschen im UKW-Funk, Tachometer-Schwankungen, AIS-Aussetzer, Autopilot-Fehlsteuerung |
| **Ort / Häufigkeit** | Navigationsbereich (40 %), Motorraum (30 %), Mastfuß/Antennenkabel (30 %) |
| **Ursache** | Parallel verlegte Starkstrom- und Signalkabel, fehlende Abschirmung, unzureichende Verdrillung, defekte Entstörfilter, LED-Treiber ohne EMV-Filter |
| **Auswirkung** | Navigationsfehler, Kommunikationsstörungen, Fehlalarme, Autopilot-Aussetzer (sicherheitsrelevant!) |
| **Messwert** | Oszilloskop: Störspannungen > 50 mV pp auf Signalleitungen. SDR/Spektrumanalysator: Erhöhtes Rauschmaß |
| **Schweregrad** | Mittel (B) bis Hoch (C) — sicherheitsrelevant bei Navigation |
| **Sofortmaßnahme** | Störquelle identifizieren (Verbraucher einzeln ein/ausschalten). LED-Beleuchtung als häufigste Ursache prüfen |
| **Langfristmaßnahme** | Kabel nach ABYC-Vorgaben trennen (Signal ≥ 30 cm Abstand zu Starkstrom), Signalkabel abschirmen, Ferritkerne auf Störer-Kabel, entstörte LED-Treiber |
| **AYDI Visual Detection** | `visual_insufficient` — Nur durch elektrische Messung diagnostizierbar |

### 6.9 Fehlerbild: Galvanische Korrosion an Steckverbindern

| Feld | Beschreibung |
|------|-------------|
| **Fehlerbild-ID** | EW-FB-009 |
| **Bezeichnung** | Kontaktkorrosion durch Materialpaarung verschiedener Metalle |
| **Visuelles Erscheinungsbild** | Weißliche bis grünliche Ablagerungen an Kontaktflächen, Stecker lassen sich schwer lösen, Kontaktoberflächen pitting, unterschiedliche Verfärbung der beiden Kontaktpartner |
| **Ort / Häufigkeit** | Decksdurchführungen (35 %), Mastfuß-Steckverbinder (25 %), Ankerwinden-Anschlüsse (20 %), Heck-Steckdosen (20 %) |
| **Ursache** | Ungeeignete Materialpaarung (z.B. Aluminium-Stecker in Kupfer-Buchse) + Feuchtigkeit + Salz → galvanisches Element. Spannungsdifferenz > 0,25 V in der galvanischen Reihe ist kritisch |
| **Auswirkung** | Wachsender Übergangswiderstand, intermittierende Kontaktprobleme, letztendlich Kontaktverlust |
| **Messwert** | Übergangswiderstand > 100 mΩ (soll < 10 mΩ) |
| **Schweregrad** | Mittel (B) |
| **Sofortmaßnahme** | Steckverbindung trennen, Kontakte reinigen (Kontaktspray), mit Kontaktfett (z.B. Tef-Gel, Duralac) wieder zusammenstecken |
| **Langfristmaßnahme** | Steckverbinder durch galvanisch kompatible Marine-Grade-Verbinder ersetzen. Deutsch DT-Steckverbinder (vergoldete Kontakte) für DC-Anwendungen |
| **AYDI Visual Detection** | `visual_medium` — Korrosion an Kontaktflächen oft nur nach Demontage sichtbar |

### 6.10 Fehlerbild: Batterie-Sulfatierung

| Feld | Beschreibung |
|------|-------------|
| **Fehlerbild-ID** | EW-FB-010 |
| **Bezeichnung** | Irreversible Sulfatierung von Blei-Säure-Batterien |
| **Visuelles Erscheinungsbild** | Batterie nimmt kaum Ladestrom an (< 2 A bei 100 Ah-Batterie im Bulk), Ruhespannung nach Ladung fällt schnell ab, Kapazität drastisch reduziert. Bei geöffneten Zellen: weiße, harte Kristalle auf Bleiplatten |
| **Ort / Häufigkeit** | Verbraucher-Batteriebank (60 %), Starterbatterie Langzeitlager (25 %), Bug-Batterie (15 %) |
| **Ursache** | Langfristige Teilentladung ohne vollständige Aufladung. Blei-Sulfat kristallisiert und wird hart. Besonders im Winterlager ohne Erhaltungsladung |
| **Auswirkung** | Kapazitätsverlust 30–80 %, erhöhter Innenwiderstand, Startprobleme, kurze Autonomie |
| **Messwert** | Innenwiderstand > 150 % des Neuwerts. Kapazitätstest: < 60 % der Nennkapazität |
| **Schweregrad** | Mittel (B) — bei Starterbatterie: Hoch (C) |
| **Sofortmaßnahme** | Desulfatierungs-Ladezyklus versuchen (Ladegerät mit Reconditioning-Programm, z.B. CTEK MXS 5.0). Erfolgsquote: ca. 30–50 % bei leichter Sulfatierung |
| **Langfristmaßnahme** | Batterie ersetzen. Zukünftig: Erhaltungsladung im Winterlager, Tiefentladeschutz installieren (z.B. Blue Sea m-LVD) |
| **AYDI Visual Detection** | `visual_insufficient` — äußerlich nicht erkennbar |

### 6.11 Fehlerbild: Wassereinbruch in Kabelkanäle

| Feld | Beschreibung |
|------|-------------|
| **Fehlerbild-ID** | EW-FB-011 |
| **Bezeichnung** | Wasser in Kabelführungen und Verteilerdosen |
| **Visuelles Erscheinungsbild** | Kondenswasser-Tropfen auf Kabeln, Wasseransammlungen in Verteilerdosen, Grünspan an allen Kontakten im betroffenen Bereich, Feuchtigkeit auf Schalttafel-Rückseite |
| **Ort / Häufigkeit** | Kabeldurchführungen Deck→Innenraum (40 %), Mastfuß (25 %), Motorraum (20 %), Heck-Plicht (15 %) |
| **Ursache** | Undichte Decksdurchführungen, Kapillareffekt an Kabelmantel, Kondensation (kaltes Kabel, warme feuchte Luft), undichte Luken über Kabelführungen |
| **Auswirkung** | Flächenkorrosion aller Kontakte im betroffenen Bereich, Isolationsversagen, Kurzschlüsse, Streustrom |
| **Messwert** | Isolationswiderstand im betroffenen Stromkreis < 0,5 MΩ |
| **Schweregrad** | Hoch (C) — Brandgefahr und Streustrom-Korrosion |
| **Sofortmaßnahme** | Betroffene Stromkreise abschalten. Wasser entfernen, Trocknung. Alle Verbindungen im betroffenen Bereich prüfen |
| **Langfristmaßnahme** | Decksdurchführungen mit geeignetem Dichtstoff (Sikaflex 291i) abdichten. Kabeldurchführungen mit Kabeldurchgängen (Roxtec, Hawke) ausführen. Entwässerungsschleifen (Drip Loops) installieren |
| **AYDI Visual Detection** | `visual_high` — Wasseransammlungen und Korrosion visuell eindeutig |

### 6.12 Fehlerbild: LED-Beleuchtung flackert / stört

| Feld | Beschreibung |
|------|-------------|
| **Fehlerbild-ID** | EW-FB-012 |
| **Bezeichnung** | LED-Beleuchtungsstörungen — Flackern, EMV, Frühausfall |
| **Visuelles Erscheinungsbild** | LED-Lampen flackern, dimmen unregelmäßig, oder fallen komplett aus. Begleitend: Störungen an UKW-Funk, AIS, Kompass wenn LEDs eingeschaltet |
| **Ort / Häufigkeit** | Innenbeleuchtung (45 %), Navigationsbeleuchtung (25 %), Cockpit-Beleuchtung (20 %), Unterwasserbeleuchtung (10 %) |
| **Ursache** | Billige LED-Treiber ohne EMV-Filterung, Bordspannungsschwankungen (11,5–14,8 V), ungeeignete LED-Retrofit-Leuchtmittel (für 230 V AC konzipiert, nicht für marine DC), Korrosion an Lampensockeln |
| **Auswirkung** | EMV-Störungen (kritisch bei Navigation), Kompassabweichung durch LED-Magnete, reduzierte Lebensdauer, Brandgefahr bei überhitzten Treibern |
| **Messwert** | Oszilloskop: Hochfrequente Störspannungen > 200 mV pp auf DC-Bus. SDR: Breitbandstörungen im UKW-Bereich |
| **Schweregrad** | Mittel (B) — bei Navigationslichtern: Hoch (C) |
| **Sofortmaßnahme** | Betroffene LED-Leuchtmittel durch qualifizierte Marine-LED ersetzen (z.B. Hella Marine, Lopolight, Dr. LED) |
| **Langfristmaßnahme** | Alle LED-Leuchtmittel auf Marine-Grade umstellen (EMV-geprüft, CE). Ferritkerne auf Zuleitungen. Separate Stromkreise für Beleuchtung und Navigation |
| **AYDI Visual Detection** | `visual_medium` — Flackern per Video dokumentierbar, EMV nur messbar |

**Confidence-Bewertung dieses Abschnitts:**
- Fehlerbilder: `documented` — Surveyor-Berichte, Werft-Dokumentation, Versicherungsgutachten
- Messwerte: `measured` — Labormessungen, Hersteller-Grenzwerte
- Häufigkeitsangaben: `benchmark` — Charterflotten-Analysen, Versicherungsstatistiken

---

## 7. Troubleshooting-Entscheidungsbäume

### 7.1 Entscheidungsbaum: Totalausfall DC-Bordnetz

```
START: Kein Strom an Bord (alle DC-Verbraucher tot)
│
├─ [1] Batterie-Hauptschalter auf ON?
│   ├─ Nein → Hauptschalter einschalten → PROBLEM GELÖST?
│   │   ├─ Ja → Ursache: Versehentliche Abschaltung ✓
│   │   └─ Nein → Weiter zu [2]
│   └─ Ja → Weiter zu [2]
│
├─ [2] Spannung direkt an Batteriepolen messen (DMM DC)
│   ├─ > 12,0 V → Batterie OK → Weiter zu [3]
│   ├─ 10,0–12,0 V → Batterie stark entladen → Laden → PROBLEM GELÖST?
│   │   ├─ Ja → Ursache: Tiefentladung (Ruhestrom zu hoch? Ladung defekt?) ✓
│   │   └─ Nein → Batterie defekt → Austausch
│   └─ < 10,0 V → Batterie tiefentladen oder defekt
│       ├─ Laden versuchen (max. 2h mit reduziertem Strom)
│       ├─ Nimmt Ladestrom an? Ja → Langsam laden → Kapazitätstest
│       └─ Nimmt keinen Ladestrom an? → Batterie defekt → Austausch
│
├─ [3] Spannung am Batterie-Hauptschalter AUSGANG messen
│   ├─ Spannung vorhanden (≈ Batteriespannung) → Weiter zu [4]
│   └─ Keine Spannung → Hauptschalter defekt oder Kabel unterbrochen
│       ├─ Spannungsabfall über Hauptschalter messen
│       ├─ > 0,5 V → Kontakte verschmort → Schalter tauschen
│       └─ Keine Verbindung → Kabel Batterie→Schalter durchmessen
│
├─ [4] Spannung an Schalttafel-Eingang messen
│   ├─ Spannung vorhanden → Weiter zu [5]
│   └─ Keine Spannung → Zuleitung Hauptschalter→Schalttafel unterbrochen
│       ├─ Hauptsicherung (ANL/MEGA) prüfen → Durchgebrannt?
│       │   ├─ Ja → KURZSCHLUSS suchen bevor neue Sicherung!
│       │   └─ Nein → Kabel prüfen (Durchgang, Spannungsabfall)
│       └─ Kabel gebrochen oder korrodiert → Ersetzen
│
├─ [5] Einzelne Sicherungsautomaten einschalten
│   ├─ Alle Stromkreise tot → Sammelschiene/Busbar korrodiert oder Masseband unterbrochen
│   │   ├─ Masseverbindung Schalttafel → Batterie Minus prüfen
│   │   └─ Busbar-Verbindungen auf Korrosion prüfen
│   ├─ Einzelne Stromkreise funktionieren → Defekte Sicherungen/Automaten identifizieren
│   └─ Alle funktionieren → Intermittierender Fehler → Spannungsabfall-Messung aller Verbindungen unter Last
│
└─ [6] ENDE: Fehlerquelle identifiziert → Reparatur → Test unter Last → Dokumentation
```

### 7.2 Entscheidungsbaum: Batterie lädt nicht (Landstrom)

```
START: Batterie lädt nicht trotz angeschlossenem Landstrom
│
├─ [1] Landstrom-Anzeige an Schalttafel leuchtet?
│   ├─ Nein → Kein AC an Bord → Weiter zu [1a]
│   └─ Ja → AC vorhanden, Ladegerät-Problem → Weiter zu [2]
│
├─ [1a] AC-Spannung am Landstrom-Einlass messen
│   ├─ 230 V vorhanden → Problem im AC-Verteilungssystem
│   │   ├─ FI-Schutzschalter ausgelöst? → Reset → Löst erneut aus? → Erdschluss suchen
│   │   ├─ AC-Hauptsicherung? → Prüfen
│   │   └─ Kabelbruch Einlass → Schalttafel → Durchgangsprüfung
│   └─ Keine Spannung → Problem am Steg/Kabel
│       ├─ Sicherung am Steg prüfen
│       ├─ Landstromkabel tauschen (Test)
│       └─ Stecker-Kontakte prüfen (Korrosion, Schmorspuren)
│
├─ [2] Ladegerät-Status-LED / Display prüfen
│   ├─ Keine Anzeige → Ladegerät erhält keinen Strom oder Geräte-Defekt
│   │   ├─ AC-Spannung am Ladegerät-Eingang messen
│   │   ├─ Interne Sicherung des Ladegeräts prüfen
│   │   └─ Ladegerät defekt → Austausch
│   ├─ Fehlermeldung → Herstellerhandbuch konsultieren
│   │   ├─ "High Temp" → Belüftung prüfen, Umgebungstemperatur > 40 °C?
│   │   ├─ "Battery Error" → Batterie-Spannung zu niedrig/hoch? Verkabelung prüfen
│   │   ├─ "No Battery" → Sicherung zwischen Ladegerät und Batterie prüfen
│   │   └─ "Overload" → Batterie-Innenwiderstand zu hoch → Batterie defekt?
│   └─ Status: "Bulk" / "Absorption" → Ladegerät arbeitet → Weiter zu [3]
│
├─ [3] Ladestrom messen (Zangenamperemeter am DC-Ausgang)
│   ├─ > 5 A → Ladegerät arbeitet, Problem eventuell nur Anzeige/Monitoring
│   ├─ 0,1–5 A → Ladegerät im Float oder reduziert
│   │   ├─ Batterie-Spannung prüfen: Schon voll (> 13,2 V)? → Float ist korrekt
│   │   ├─ Batterie nicht voll aber wenig Strom → Temperatur-Reduktion? (> 40 °C)
│   │   └─ Batterie sulfatiert → Innenwiderstand zu hoch → Batterie tauschen
│   └─ 0 A → Kein Ladestrom
│       ├─ DC-Sicherung Ladegerät → Batterie prüfen
│       ├─ Kabel-Durchgang Ladegerät → Batterie prüfen
│       └─ Ladegerät DC-Ausgang defekt → Austausch
│
└─ [4] ENDE: Fehlerquelle identifiziert → Reparatur → Ladezyklus überwachen → Dokumentation
```

### 7.3 Entscheidungsbaum: Streustrom-Korrosion

```
START: Verdacht auf Streustrom (schneller Anodenverbrauch, Propeller-Korrosion)
│
├─ [1] Liegt das Boot im Wasser mit Landstrom?
│   ├─ Ja → Weiter zu [2]
│   └─ Nein → Galvanische Korrosion (nicht elektrolytisch)
│       ├─ Anoden prüfen (Zustand, Material, Menge)
│       ├─ Materialpaarungen prüfen (galvanische Reihe)
│       └─ Erdungsband prüfen
│
├─ [2] Zangenamperemeter um ALLE Landstromkabel-Leiter
│   ├─ < 30 mA → Kein DC-Leckstrom über Landstrom → Weiter zu [4]
│   ├─ 30–100 mA → Leichter Leckstrom → Weiter zu [3]
│   └─ > 100 mA → Signifikanter Leckstrom! → Weiter zu [3]
│
├─ [3] Landstrom trennen — Leckstrom verschwunden?
│   ├─ Ja → Problem im eigenen AC-Netz oder Nachbarboot
│   │   ├─ Galvanischen Isolator prüfen (sofern vorhanden)
│   │   ├─ AC-Erdung prüfen (PE ↔ Schiffsmasse)
│   │   ├─ Trenntrafo empfehlen (beste Lösung)
│   │   └─ Nachbarboote bitten, Landstrom zu trennen (Ausschlussverfahren)
│   └─ Nein → DC-Leckstrom aus eigenem Bordnetz → Weiter zu [4]
│
├─ [4] Alle DC-Sicherungen/Automaten AUS — Ruhestrom messen
│   ├─ Ruhestrom = 0 A → Sicherungen einzeln einschalten
│   │   ├─ Stromkreis mit erhöhtem Leckstrom identifizieren
│   │   ├─ In diesem Stromkreis: Isolationsmessung (Megger 500 V)
│   │   └─ Defekte Isolation/feuchtes Kabel ersetzen
│   └─ Ruhestrom > 0 A trotz aller Sicherungen AUS
│       ├─ Direkt an Batterie angeschlossene Geräte suchen (Bilgenpumpe, Alarme)
│       ├─ Masseverbindungen prüfen
│       └─ Batteriekabel auf Isolationsschaden prüfen
│
├─ [5] Referenzelektrode-Messung (Ag/AgCl)
│   ├─ -800 bis -1.050 mV → Ausreichend geschützt → Monitoring fortsetzen
│   ├─ > -800 mV → Unzureichend geschützt → Anoden erneuern oder vergrößern
│   └─ > -500 mV → Aktive Korrosion! → Sofortmaßnahmen (Boot krantzen, Fehler beheben)
│
└─ [6] ENDE: Streustromquelle identifiziert → Reparatur → Nachmessung → Langzeit-Monitoring
```

### 7.4 Entscheidungsbaum: Motor startet nicht (elektrisch)

```
START: Motor startet nicht — Zündschlüssel/Startknopf ohne Reaktion oder nur Klicken
│
├─ [1] Was passiert beim Drehen des Zündschlüssels?
│   ├─ Gar nichts (kein Klicken, kein Geräusch) → Weiter zu [2]
│   ├─ Nur Klicken (Magnetschalter) → Weiter zu [3]
│   ├─ Anlasser dreht langsam → Weiter zu [4]
│   └─ Anlasser dreht normal, Motor zündet nicht → KEIN Elektrik-Problem → Kraftstoff/Kompression
│
├─ [2] Keine Reaktion
│   ├─ Batteriespannung an Starterbatterie messen
│   │   ├─ < 10,5 V → Batterie entladen → Laden oder Starthilfe
│   │   ├─ > 12,0 V → Batterie OK → Weiter zu [2a]
│   │   └─ 0 V → Batterie-Anschluss unterbrochen → Polklemmen prüfen
│   ├─ [2a] Spannung am Zündschloss prüfen
│   │   ├─ Keine Spannung → Sicherung Zündung oder Kabel prüfen
│   │   └─ Spannung vorhanden → Zündschloss-Ausgang in Stellung START messen
│   │       ├─ Keine Spannung → Zündschloss defekt
│   │       └─ Spannung vorhanden → Kabel Zündschloss → Magnetschalter prüfen
│   └─ Notstart: Magnetschalter direkt brücken (Klemme 30 → 50)
│       ⚠ VORSICHT: Gang muss raus sein, Not-Stopp bereit!
│
├─ [3] Nur Klicken
│   ├─ Spannung an Batteriepolen messen WÄHREND Startversuch
│   │   ├─ Spannung bricht unter 9,6 V ein → Batterie zu schwach oder defekt
│   │   │   ├─ Batterie-Innenwiderstand messen
│   │   │   ├─ Starthilfe von Verbraucherbatterie
│   │   │   └─ Batterie tauschen wenn Innenwiderstand zu hoch
│   │   └─ Spannung bleibt > 10 V → Spannungsabfall im Starterstromkreis
│   │       ├─ Spannungsabfall Batteriepol Plus → Anlasser-Klemme 30
│   │       ├─ Spannungsabfall Motorblock → Batterie Minus
│   │       ├─ Grenzwert: Jede Verbindung < 100 mV bei Startversuch
│   │       └─ Auffällige Verbindung reinigen / ersetzen
│   └─ Magnetschalter-Kontakte verschmort → Magnetschalter tauschen
│
├─ [4] Anlasser dreht langsam
│   ├─ Batteriespannung unter Last messen
│   │   ├─ < 9,6 V → Batterie → Laden oder Tauschen
│   │   └─ > 9,6 V → Kabelquerschnitt zu klein oder Verbindungen korrodiert
│   ├─ Kabelquerschnitt Starterkabel prüfen (mind. 50 mm² bei Diesel bis 3L)
│   ├─ Masseband Motor → Batterie Minus prüfen (Querschnitt, Korrosion)
│   └─ Anlasser-Kohlen verschlissen? → Anlasser überholen oder tauschen
│
└─ [5] ENDE: Fehlerquelle identifiziert → Reparatur → Starttest → Lade-/Spannungskontrolle
```

### 7.5 Entscheidungsbaum: Instrumentenstörungen

```
START: Einzelne oder mehrere Instrumente zeigen falsche Werte oder fallen aus
│
├─ [1] Wie viele Instrumente betroffen?
│   ├─ Eines → Weiter zu [2]
│   ├─ Mehrere am selben Stromkreis → Weiter zu [3]
│   └─ Alle → Weiter zu [4]
│
├─ [2] Einzelnes Instrument gestört
│   ├─ Versorgungsspannung am Instrument messen
│   │   ├─ Korrekt (11,5–14,5 V) → Instrument oder Sensor-Problem
│   │   │   ├─ Sensor/Geber prüfen (Widerstand messen, Kabel prüfen)
│   │   │   ├─ NMEA-2000/Signal-Bus: Terminatoren vorhanden?
│   │   │   └─ Instrument defekt → Austausch
│   │   └─ Schwankend oder zu niedrig → Spannungsversorgung prüfen
│   │       ├─ Sicherung, Kabelverbindung, Stecker
│   │       └─ Spannungsabfall-Messung unter Last
│   └─ Intermittierender Ausfall → Kabel bewegen (Vibrations-Simulation) → Wackelkontakt?
│       ├─ Ja → Betroffene Verbindung erneuern
│       └─ Nein → Temperaturabhängig? (Kalte Lötstelle im Gerät → Reparatur)
│
├─ [3] Mehrere Instrumente am selben Stromkreis
│   ├─ Gemeinsame Masseverbindung prüfen!
│   │   ├─ Widerstand Instrumenten-Masse → Batterie Minus: < 100 mΩ?
│   │   ├─ Nein → Masseverbindung korrodiert → Reinigen und neu anschließen
│   │   └─ Ja → Versorgungsspannung am gemeinsamen Verteiler prüfen
│   ├─ NMEA-2000-Bus: Backbone-Spannung 9–16 V? Terminatoren?
│   │   ├─ Spannung < 9 V → Versorgungsproblem
│   │   ├─ Keine Terminatoren → Reflexionen → einsetzen (120 Ω an jedem Ende)
│   │   └─ Drop-Kabel zu lang? (max. 6 m) → Verkürzen
│   └─ EMV-Störungen → Verbraucher einzeln einschalten → Störer identifizieren
│
├─ [4] Alle Instrumente betroffen
│   ├─ Bordspannung prüfen
│   │   ├─ < 10 V → Batterie / Ladung → Basisversorgung sicherstellen
│   │   └─ > 10 V → Masseband Hauptmasse → Schalttafel prüfen
│   ├─ Hauptmasseverbindung gelöst? (häufig nach Winterlager!)
│   ├─ Batteriewechsel mit falsch angeschlossenen Kabeln? (Plus/Minus vertauscht)
│   └─ Überspannung durch defekten Laderegler? (> 16 V)
│
└─ [5] ENDE: Ursache identifiziert → Reparatur → Funktionstest aller Instrumente → Dokumentation
```

**Confidence-Bewertung dieses Abschnitts:**
- Entscheidungsbäume: `documented` — ABYC Troubleshooting Guides, Hersteller-Service-Manuals
- Grenzwerte: `measured` — Normen und Hersteller-Spezifikationen
- Reihenfolge: `estimated` — Erfahrungswerte Marine-Elektriker (häufigste Ursache zuerst)

---

## 8. FAQ

### 8.1 Grundlagen und Werkzeuge

**F1: Welches Multimeter brauche ich für die Boots-Elektrik?**
A: Mindestens ein True-RMS-Multimeter mit CAT III 600V-Rating, DC-Spannungsmessung bis 60 V und Millivolt-Auflösung für Spannungsabfall-Messungen. Das Fluke 87V ist der Gold-Standard. Als Budget-Alternative kommt das Fluke 117 oder UNI-T UT61E+ in Frage. Finger weg von Geräten unter 50 EUR — mangelnde Genauigkeit führt zu Fehldiagnosen.

**F2: Brauche ich ein Zangenamperemeter an Bord?**
A: Dringend empfohlen. Die berührungslose Strommessung ist die einzige praktikable Methode, um Ströme > 10 A zu messen, ohne das Kabel aufzutrennen. Unverzichtbar für Ruhestrom-Diagnose, Ladestrom-Kontrolle und Fehlersuche. Ein DC-fähiges Modell (z.B. Fluke 376 FC) ist Pflicht — reine AC-Zangen sind an Bord fast nutzlos.

**F3: Was kostet eine professionelle Elektrik-Inspektion?**
A: Je nach Bootsgröße und Umfang: 250–1.000 EUR für eine Jahresinspektion (8–14 m), 1.000–5.000 EUR für eine 5-Jahres-Revision. Eigenleistung spart 60–70 % der Kosten, setzt aber Fachkenntnis und geeignete Messgeräte voraus.

**F4: Wie oft sollte ich die Elektrik inspizieren?**
A: Jährlich vor der Saison (Pflicht). Zusätzlich nach jedem Gewitter (Blitzeinschlag?), nach längerer Nichtbenutzung, und bei jedem Kauf/Verkauf (Zustandsbericht). Alle 5 Jahre eine Vollrevision mit Isolationsmessung.

**F5: Kann ich Elektrik-Arbeiten selbst machen oder brauche ich einen Fachbetrieb?**
A: Einfache Wartungsarbeiten (Sicherungswechsel, Kontaktreinigung, Batteriepflege, Beleuchtungstausch) sind für technisch versierte Eigner machbar. Arbeiten am AC-Netz (230 V Landstrom), Änderungen an der Hauptverkabelung und Arbeiten am Laderegler/Wechselrichter sollten von einem zugelassenen Marine-Elektriker durchgeführt werden. In vielen Ländern ist dies auch versicherungsrechtlich vorgeschrieben.

### 8.2 Batterien und Ladung

**F6: Wie erkenne ich, ob meine Batterie noch gut ist?**
A: Drei Tests: (1) Ruhespannung nach 12h Ruhe (12V Blei: 12,73 V = 100 %, < 12,06 V = < 50 %). (2) Belastungstest: Spannung unter Last 15s > 9,6 V. (3) Innenwiderstandsmessung: > 150 % des Neuwerts = Austausch. Ein Victron SmartShunt oder BMV-712 erleichtert das Monitoring erheblich.

**F7: Muss ich die Batterien im Winter ausbauen?**
A: Nicht zwingend. Ideal: An Bord belassen mit Erhaltungsladegerät (z.B. CTEK MXS 5.0 oder Victron Blue Smart IP65) bei Landstrom. Ohne Landstrom: Ausbauen, an Land trocken und frostfrei lagern, monatlich nachladen. LiFePO4: BMS in Sleep-Mode, kein Laden unter 0 °C!

**F8: Kann ich AGM- und Blei-Säure-Batterien mischen?**
A: Dringend abgeraten. Verschiedene Batterietypen haben unterschiedliche Ladekennlinien. Wenn gemischt, wird mindestens eine Batterie nicht optimal geladen. Ausnahme: Getrennte Batteriebanken mit separaten Ladegeräten (z.B. AGM als Starter, Flooded als Verbraucher) — aber Ladespannung muss individuell eingestellt sein.

**F9: Warum ist meine Batterie nach dem Winter immer leer?**
A: Selbstentladung + Ruhestrom. Blei-Säure verliert 3–5 % Kapazität pro Monat durch Selbstentladung (bei 20 °C). Dazu kommt der Ruhestrom der Bordgeräte (0,5–3 A). Ohne Erhaltungsladung ist nach 3–4 Monaten Tiefentladung erreicht. Lösung: Erhaltungsladegerät oder Batterie-Trennschalter OFF + monatliches Nachladen.

**F10: LiFePO4 oder Blei-Säure — was ist besser für Yachten?**
A: LiFePO4 bietet 3–4× mehr nutzbare Kapazität pro kg, 3.000–5.000 Zyklen vs. 300–500, flache Entladekurve, schnelleres Laden. Nachteile: 3–4× teurer in der Anschaffung, BMS erforderlich, keine Ladung unter 0 °C, Kompatibilität mit Lichtmaschine muss sichergestellt sein. Für Langfahrer und Vielnutzer: LiFePO4. Für Wochenendsegler mit Landstrom: AGM reicht oft.

### 8.3 Landstrom und AC-System

**F11: Warum löst mein FI-Schutzschalter ständig aus?**
A: Häufigste Ursachen: (1) Feuchtigkeit in einem AC-Verbraucher (Warmwasserboiler, Heizung). (2) Defekte Isolierung eines AC-Kabels. (3) Falsche Verdrahtung (N und PE vertauscht). (4) Zu empfindlicher FI (30 mA) bei langen Kabeln mit hohem Ableitstrom. (5) Nachbar am selben Steg mit Erdschluss (über Seewasser gekoppelt).

**F12: Brauche ich einen Trenntrafo?**
A: Für optimalen Schutz gegen Streustrom: Ja. Ein Trenntrafo (galvanische Trennung, z.B. Victron Isolation Transformer) eliminiert die galvanische Verbindung zwischen Steg-Erdung und Schiffsmasse vollständig. Alternative: Galvanischer Isolator (z.B. Marinco CruiseGard), der nur DC blockiert, AC-Erdung aber erhält. Für Dauerlieger im Salzwasser: Trenntrafo dringend empfohlen.

**F13: Was ist der Unterschied zwischen PE, N und L beim Landstrom?**
A: L (Phase) = stromführender Leiter (230 V gegen Erde). N (Neutralleiter) = Rückleiter (0 V gegen Erde am Einspeisepunkt). PE (Schutzleiter) = Schutzerdung, führt im Normalfall keinen Strom, leitet im Fehlerfall den Fehlerstrom ab und löst den FI aus. ACHTUNG: Auf Yachten darf der Schutzleiter (PE) NICHT mit der Schiffsmasse verbunden werden (Streustromgefahr!) — es sei denn, ein Trenntrafo oder galvanischer Isolator ist installiert.

**F14: Mein Landstromkabel wird warm — ist das normal?**
A: Leichte Erwärmung bei hoher Last (z.B. Klimaanlage + Ladegerät + Warmwasserboiler) ist akzeptabel, solange die Kabeltemperatur 60 °C nicht überschreitet. Starke Erwärmung (Kabel zu heiß zum Anfassen) deutet auf zu kleinen Querschnitt, korrodierte Steckerkontakte oder Überlastung hin. Sofort: Last reduzieren, Steckerkontakte prüfen. Thermografie durchführen.

### 8.4 Sicherheit und Schutz

**F15: Wie schütze ich mein Boot vor Blitzschlag?**
A: Ein Blitzschutzsystem nach ABYC E-4 / ISO 10134 leitet den Blitzstrom vom höchsten Punkt (Mastspitze) über einen niederohmigen Pfad ins Wasser. Kernkomponenten: Blitzableiter an Mastspitze, Kupfer-Erdungsband (mind. 30 mm² Querschnitt), Verbindung zum Kiel-Bolzen oder großflächiger Erdungsplatte (mind. 0,1 m²). Überspannungsschutz (SPD) an allen Elektronik-Zuleitungen installieren.

**F16: Was tun bei Kabelbrand an Bord?**
A: (1) SOFORT Batterie-Hauptschalter AUS. (2) Landstrom trennen. (3) CO₂- oder Pulverlöscher verwenden — KEIN Wasser auf brennende Elektrik! (4) Brand lokalisieren und isolieren. (5) Danach: Brandstelle komplett freilegen, beschädigte Kabel restlos ersetzen, Brandursache ermitteln und beheben.

**F17: Wie erkenne ich Streustrom-Probleme?**
A: Warnsignale: (1) Opferanoden verbrauchen sich ungewöhnlich schnell (< 6 Monate). (2) Propeller zeigt "angefressene" Oberfläche (Pitting). (3) Seeventile haben weißliche Ablagerungen. (4) Nachbarboote haben ebenfalls Korrosionsprobleme. Diagnose: Referenzelektrode-Messung und Leckstrommessung am Landstromkabel.

**F18: Wie teste ich meinen FI-Schutzschalter?**
A: (1) Monatlich: Prüftaste am FI drücken — muss sofort auslösen. (2) Jährlich: Mit FI-Testgerät Auslösezeit messen (soll < 40 ms bei 30 mA, Typ A). (3) Alle 5 Jahre: Professionelle Prüfung mit Rampen-Test (Auslösestrom bestimmen). Wenn der FI bei Prüftaste nicht auslöst: SOFORT ersetzen!

### 8.5 Wartung und Winterlager

**F19: Wie schütze ich die Elektrik im Winterlager?**
A: Siehe detaillierte Checkliste in Abschnitt 3.4. Kernpunkte: Batterien voll laden und Erhaltungsladung sicherstellen, empfindliche Elektronik ausbauen oder luftdicht verpacken, Schalttafeln belüften (Silikagel), Entfeuchter installieren, Landstromkabel gegen Nagetiere sichern.

**F20: Wann muss ich Kabel ersetzen?**
A: Sofort bei: Rissiger oder spröder Isolierung, sichtbarem Kupfer, Verfärbung durch Hitze, Isolationswiderstand < 1 MΩ, Querschnitt für aktuelle Last zu klein (nachträgliche Verbraucher). Planmäßig: Kabel im Motorraum alle 15–20 Jahre, Kabel an Deck alle 10–15 Jahre, Landstromkabel alle 10 Jahre.

**F21: Wie reinige ich korrodierte Kontakte?**
A: (1) Stromkreis spannungsfrei schalten. (2) Kontakt demontieren. (3) Leichte Korrosion: Kontaktspray (z.B. WD-40 Specialist Kontaktspray) + Mikrofaser-Tuch. (4) Mittlere Korrosion: Messingbürste + Isopropanol. (5) Starke Korrosion: Verbindung erneuern (neu crimpen, neuen Stecker). (6) Kontaktfett (z.B. NO-OX-ID, Tef-Gel) auftragen. (7) Schrumpfschlauch mit Kleber zur Versiegelung.

**F22: Wie oft müssen Opferanoden gewechselt werden?**
A: Wenn > 50 % des Materials verbraucht ist. Typischer Wechselintervall: 12–18 Monate im Salzwasser, 24–36 Monate im Brackwasser, 36–60 Monate im Süßwasser. Bei schnellerem Verbrauch: Streustrom-Diagnose durchführen!

### 8.6 Spezialthemen

**F23: Was ist eine Millivolt-Drop-Analyse und warum ist sie so wichtig?**
A: Die Millivolt-Drop-Analyse (Spannungsabfall-Messung) ist die aussagekräftigste Einzelmessung in der Marine-Elektrik. Sie misst den Spannungsabfall über jede einzelne Verbindung im Stromkreis unter Last. Jede Verbindung sollte < 50 mV abfallen. Die Summe aller Abfälle sollte < 3 % der Nennspannung sein. Ein erhöhter Spannungsabfall zeigt Korrosion oder lose Kontakte an, BEVOR sie zu Ausfällen führen.

**F24: Wie diagnostiziere ich EMV-Störungen an Bord?**
A: Systematisch: (1) Alle Verbraucher aus. (2) Einzeln einschalten und auf Störung am betroffenen Instrument achten. (3) Störer identifiziert? Ferritkern auf Zuleitung des Störers. (4) LED-Beleuchtung ist die häufigste Ursache — durch Marine-Grade-LEDs ersetzen. (5) Kabelführung prüfen: Signal- und Starkstromkabel mindestens 30 cm Abstand. (6) Abschirmung der Signalkabel prüfen.

**F25: Kann ich eine 12V-Anlage auf 24V umstellen?**
A: Technisch möglich, aber umfangreich und teuer. ALLE Verbraucher müssen 24V-kompatibel sein (Pumpen, Leuchten, Instrumente, Winschen, Ankerwinde). Alle Sicherungen und Schalter müssen neu dimensioniert werden. Kabelquerschnitte können bei 24V kleiner sein (halber Strom bei gleicher Leistung). Sinnvoll bei Neuinstallation auf Yachten > 15 m oder bei hohem Leistungsbedarf. Auf bestehenden Booten < 14 m meist unwirtschaftlich.

**F26: Wie integriere ich ein Batterie-Monitoring in mein NMEA-2000-Netzwerk?**
A: Victron SmartShunt oder BMV-712 + VE.Direct-to-NMEA-2000-Interface. Alternativ: Victron Cerbo GX als Gateway (VE.Direct → NMEA 2000, WiFi, VRM Cloud). Auf NMEA 2000 werden die PGNs 127506 (DC Detailed Status), 127508 (Battery Status) und 127513 (Battery Configuration) gesendet.

**F27: Was ist der Unterschied zwischen Schiffsmasse und Erdung?**
A: Schiffsmasse (DC Ground / DC Negative) ist der gemeinsame Rückleiter des DC-Bordnetzes — typisch der Batterie-Minuspol. Erdung (AC Ground / PE) ist der Schutzleiter des AC-Netzes (Landstrom). Auf Yachten OHNE Trenntrafo/Isolator: PE und Schiffsmasse sind NICHT verbunden (um Streustrom zu vermeiden). Mit Trenntrafo: PE wird bordseitig mit Schiffsmasse verbunden (Trenntrafo trennt galvanisch vom Steg).

### 8.7 AYDI-spezifische Fragen

**F28: Wie erkennt AYDI Elektrik-Probleme auf Fotos?**
A: Die AYDI Visual Analysis Pipeline B analysiert Fotos der Elektrik-Installation auf: (1) Korrosionserscheinungen (Grünspan, Sulfatierung). (2) Thermische Schäden (Verfärbungen, geschmorte Kontakte). (3) Installationsqualität (Kabelführung, Crimpqualität, Beschriftung). (4) Normkonformität (Kabelfarben, Sicherungsgrößen). Confidence Level variiert: `visual_high` für deutliche Korrosion, `visual_medium` für Installationsqualität, `visual_insufficient` für verdeckte Fehler.

**F29: Welche Daten braucht AYDI für eine Elektrik-Analyse Level 2?**
A: Optimal: Schaltplan (digital), Batteriedaten (Typ, Kapazität, Alter), Ladegerät-Spezifikationen, Verbraucherliste mit Stromaufnahme, Kabelquerschnitte, Sicherungswerte, letzte Messprotokolle (Isolationsmessung, Spannungsabfall). Fotos: Schalttafel (offen), Batterieraum, Motorraum-Verkabelung, Landstrom-Einspeisung, Massesammelschiene.

**F30: Wie bewertet AYDI die Elektrik-Qualität einer gebrauchten Yacht?**
A: AYDI verwendet einen gewichteten Score aus: Installationsqualität (30 %), Zustand der Komponenten (25 %), Normkonformität (20 %), Dokumentation (15 %), Alter und Wartungshistorie (10 %). Jeder Aspekt wird separat bewertet mit Confidence-Level. Das Ergebnis fließt in den Gesamt-Zustandsscore der Yacht ein.

### 8.8 Weiterführende Fragen

**F31: Wie berechne ich die Autonomie meiner Batteriebank?**
A: Autonomie [h] = (Batteriekapazität [Ah] × nutzbare DoD × Systemspannung [V]) / (Gesamtverbrauch [W]). Beispiel: 400 Ah AGM, 50 % DoD, 12 V, 60 W Durchschnittsverbrauch → (400 × 0,5 × 12) / 60 = 40 Stunden. Für LiFePO4 mit 80 % DoD: (400 × 0,8 × 12) / 60 = 64 Stunden. AYDI berechnet dies automatisch basierend auf dem Verbraucherprofil.

**F32: Mein Wechselrichter brummt — ist das normal?**
A: Ein leises Summen (< 40 dB) bei Belastung ist bei transformatorbasierten Wechselrichtern normal (Magnetostriktion im Trafo-Kern). Lautes Brummen oder Vibrationen deuten auf: (1) Lose Befestigungsschrauben. (2) Überlastung (Last > 80 % der Nennleistung). (3) Niedrige Batteriespannung (< 11,5 V bei 12V-System). (4) Defekten Lüfter. (5) Modifizierter Sinus (MSW) — manche Verbraucher brummen mit MSW-Wechselrichtern.

**F33: Welche Verbraucher brauchen einen reinen Sinus-Wechselrichter?**
A: Zwingend: Mikrowelle (Drehteller dreht nicht bei MSW), empfindliche Ladegeräte (Laptop, Drohne), Medizinische Geräte (CPAP), Laserdrücker, Induktionsherd. Empfohlen: Klimaanlage (läuft effizienter), Waschmaschine (Timer-Probleme bei MSW), Audio-Equipment (Brummen bei MSW). Unkritisch: Heizlüfter, Kaffeemaschine (Heizelement), einfache Wasserkocher, LED-Beleuchtung.

**F34: Wie verkable ich ein NMEA-2000-Netzwerk korrekt?**
A: Kernregeln: (1) Backbone als durchgehende Linie, nicht sternförmig. (2) Zwei 120-Ω-Terminatoren, je einer an jedem Ende des Backbone. (3) Drop-Kabel max. 6 m, bei > 6 m: Repeater verwenden. (4) Backbone max. 100 m (Micro-C) oder 200 m (Mini-C). (5) Spannungsversorgung über Power-T-Stück, 9–16 V DC. (6) Max. 50 Geräte am Bus. (7) Backbone-Kabel nicht knicken (Mindestbiegeradius beachten).

**F35: Was kostet eine komplett neue Elektrik-Installation auf einer 12-m-Segelyacht?**
A: Richtwerte (Confidence: estimated): Material: 8.000–15.000 EUR (Kabel, Schalttafel, Sicherungen, Stecker, Batterien nicht enthalten). Arbeitskosten (Fachbetrieb): 15.000–30.000 EUR (200–400 Arbeitsstunden). Gesamt ohne Batterien und Elektronik: 25.000–45.000 EUR. Mit neuer Batteriebank (LiFePO4 400 Ah): + 4.000–6.000 EUR. Mit neuer Navigations-Elektronik: + 5.000–15.000 EUR. Deshalb: Gute Wartung ist erheblich günstiger als Neuinstallation.

**Confidence-Bewertung dieses Abschnitts:**
- Antworten: `documented` — Normen, Hersteller-Empfehlungen, Fachliteratur
- Kostenangaben: `estimated` — DACH-Marktpreise 2024/2025
- AYDI-spezifisch: `measured` — Systemspezifikation

---

## 9. Glossar

| Nr. | Begriff | Erklärung |
|-----|---------|-----------|
| 1 | **ABYC** | American Boat and Yacht Council — US-Organisation für Boots-Standards, international anerkannt |
| 2 | **AC** | Alternating Current (Wechselstrom) — an Bord typisch 230 V / 50 Hz über Landstrom |
| 3 | **AGM** | Absorbent Glass Mat — wartungsfreie Blei-Säure-Batterie, Elektrolyt in Glasfaservlies gebunden |
| 4 | **Ampere (A)** | SI-Einheit der elektrischen Stromstärke |
| 5 | **BMS** | Battery Management System — elektronische Schutzschaltung für LiFePO4-Batterien |
| 6 | **Bulk-Ladung** | Erste Ladephase mit maximalem Ladestrom bis ca. 80 % SoC |
| 7 | **CAT-Rating** | Messkategorie für die Stoßfestigkeit von Messgeräten (CAT I–IV) |
| 8 | **CCA** | Cold Cranking Amps — Kaltstartstrom einer Batterie (bei -18 °C, 30 s, > 7,2 V) |
| 9 | **CE-Kategorie** | Designkategorie nach EU-Richtlinie 2013/53/EU (A/B/C/D) |
| 10 | **Coulomb-Counting** | Methode zur SoC-Bestimmung durch Integration des Stroms über die Zeit |
| 11 | **Crimpverbindung** | Mechanische Kabelverbindung durch plastische Verformung eines Verbinders |
| 12 | **DAR** | Dielectric Absorption Ratio — Verhältnis R_60s / R_15s bei Isolationsmessung |
| 13 | **DC** | Direct Current (Gleichstrom) — an Bord typisch 12 V oder 24 V |
| 14 | **DMM** | Digital Multimeter — digitales Vielfachmessgerät |
| 15 | **Emissionsgrad (ε)** | Maß für die Infrarot-Abstrahleffizienz einer Oberfläche (0–1) |
| 16 | **EMV** | Elektromagnetische Verträglichkeit — Störfestigkeit und Störaussendung |
| 17 | **Erdschluss** | Unerwünschte Verbindung eines aktiven Leiters mit der Erde/Masse |
| 18 | **FI (RCD)** | Fehlerstromschutzschalter — Schutzeinrichtung gegen Personengefährdung durch Fehlerstrom |
| 19 | **Float-Ladung** | Erhaltungsladung — konstante Spannung (z.B. 13,4 V) hält Batterie bei 100 % SoC |
| 20 | **Galvanische Korrosion** | Korrosion durch elektrochemische Potentialdifferenz verschiedener Metalle im Elektrolyten |
| 21 | **Galvanischer Isolator** | Bauteil, das DC-Leckströme über den PE-Leiter blockiert, AC-Erdung erhält |
| 22 | **Hall-Sensor** | Halbleiter-Sensor zur berührungslosen Gleichstrommessung über magnetisches Feld |
| 23 | **IP-Schutzart** | International Protection Rating — Schutzgrad gegen Fremdkörper und Wasser (z.B. IP 67) |
| 24 | **Isolationswiderstand** | Widerstand zwischen aktivem Leiter und Erde, gemessen in MΩ mit Prüfspannung |
| 25 | **LiFePO4** | Lithium-Eisenphosphat — sichere Lithium-Batterie-Chemie für Marine-Anwendungen |
| 26 | **Megger** | Markenname (Megger Group), generisch: Isolationsmessgerät |
| 27 | **mΩ (Milliohm)** | 0,001 Ohm — Einheit für Kontaktwiderstände und Batterie-Innenwiderstand |
| 28 | **NMEA 2000** | Marinbus-Standard für die Vernetzung von Bordelektronik (CAN-basiert) |
| 29 | **OCV** | Open Circuit Voltage — Ruhespannung (ohne Last und Ladung) |
| 30 | **Opferanode** | Weniger edles Metall (Zink, Aluminium), das sich anstelle der zu schützenden Bauteile auflöst |
| 31 | **PE** | Protective Earth (Schutzleiter) — Schutzerdung im AC-System |
| 32 | **PI (Polarisierungsindex)** | Verhältnis R_10min / R_1min bei Isolationsmessung — Indikator für Feuchtigkeit |
| 33 | **Ripple** | Wechselstrom-Anteil auf einer Gleichspannung (z.B. Lichtmaschinen-Ripple) |
| 34 | **Shunt** | Präzisionswiderstand zur Strommessung über Spannungsabfall |
| 35 | **SoC** | State of Charge — Ladezustand einer Batterie in Prozent |
| 36 | **SoH** | State of Health — Gesundheitszustand einer Batterie (Restkapazität vs. Neuzustand) |
| 37 | **Spannungsabfall** | Spannungsverlust über eine Verbindung oder Leitung unter Last (V-Drop) |
| 38 | **Streustrom** | Unerwünschter elektrischer Strom, der über Seewasser oder Rumpf fließt |
| 39 | **Sulfatierung** | Irreversible Kristallbildung von Bleisulfat auf Batterieplatten bei Tiefentladung |
| 40 | **SWR** | Standing Wave Ratio (Stehwellenverhältnis) — Maß für die Antennenanpassung |
| 41 | **Thermografie** | Berührungslose Temperaturmessung mittels Infrarotkamera |
| 42 | **Trenntrafo** | Transformator zur galvanischen Trennung von Landstrom und Bordnetz |
| 43 | **True RMS** | Echte Effektivwertmessung — misst korrekt bei nicht-sinusförmigen Signalen |
| 44 | **Übergangswiderstand** | Widerstand an einer Kontaktstelle (Stecker, Klemme, Crimpverbindung) |
| 45 | **VE.Direct** | Proprietäres Kommunikationsprotokoll von Victron Energy |
| 46 | **VRM** | Victron Remote Management — Cloud-Portal zur Fernüberwachung |
| 47 | **XLPE** | Cross-Linked Polyethylene — vernetztes Polyethylen, hitzebeständige Kabelisolierung |
| 48 | **Absorption** | Zweite Ladephase nach Bulk — konstante Spannung, sinkender Strom bis Batterie voll |
| 49 | **ANL-Sicherung** | Große Streifensicherung (35–750 A) für Hauptstromkreise und Hochstromverbraucher |
| 50 | **Bonding** | Elektrische Verbindung aller metallischen Teile im Unterwasserbereich zum Korrosionsschutz |
| 51 | **Buck-Converter** | Abwärts-Schaltregler, z.B. in LED-Treibern — häufige EMV-Störquelle |
| 52 | **Busbar** | Sammelschiene (Kupfer/Messing) zur Verteilung von Plus oder Minus an mehrere Stromkreise |
| 53 | **CAN-Bus** | Controller Area Network — Basis von NMEA 2000, serielles Datenbussystem |
| 54 | **COLREG** | Convention on the International Regulations for Preventing Collisions at Sea — Kollisionsverhütungsregeln |
| 55 | **Cranking** | Startvorgang — Anlasser dreht Motor durch, hoher Stromimpuls (200–600 A) |
| 56 | **Desulfatierung** | Versuch, Sulfatkristalle auf Batterieplatten durch spezielle Ladepulse aufzulösen |
| 57 | **Diode** | Halbleiterbauelement, das Strom nur in einer Richtung durchlässt — in Ladeverteilern und Gleichrichtern |
| 58 | **DoD** | Depth of Discharge — Entladetiefe. AGM: max. 50 %, LiFePO4: max. 80 % |
| 59 | **Drip-Loop** | Entwässerungsschleife — U-förmige Kabelführung, die verhindert, dass Wasser am Kabel entlang in Geräte läuft |
| 60 | **Equalization** | Ausgleichsladung — kurzzeitig erhöhte Ladespannung (15,5–16 V) bei Flooded-Batterien zum Ausgleich der Zellenspannungen |
| 61 | **Ferritkern** | Ringförmiger Kern aus Ferrit-Material, als EMV-Filter auf Kabel aufgesteckt |
| 62 | **Fluxgate-Kompass** | Elektronischer Kompass mit magnetfeldempfindlichen Spulen — empfindlich gegenüber magnetischen Störfeldern |
| 63 | **GFI** | Ground Fault Interrupter — US-Bezeichnung für FI/RCD-Schutzschalter |
| 64 | **Inrush Current** | Einschaltstromstoß — kurzzeitig hoher Strom beim Einschalten von Motoren, Kompressoren, Transformatoren |
| 65 | **Kelvin-Messung** | Vierleitermessung — eliminiert den Widerstand der Messleitungen für präzise Niedrigstwiderstandsmessungen |
| 66 | **Knallgas** | Explosives Gemisch aus Wasserstoff und Sauerstoff, entsteht bei Überladung von Blei-Säure-Batterien |
| 67 | **Leitfähigkeit** | Kehrwert des spezifischen Widerstands — Kupfer: 58 MS/m, Aluminium: 37 MS/m |
| 68 | **MCB** | Miniature Circuit Breaker — Leitungsschutzschalter / Sicherungsautomat |
| 69 | **MPPT** | Maximum Power Point Tracking — Algorithmus in Solarreglern zur optimalen Energieausbeute |
| 70 | **NETD** | Noise Equivalent Temperature Difference — thermische Empfindlichkeit einer IR-Kamera (kleiner = besser) |
| 71 | **Peukert-Effekt** | Kapazitätsverlust von Blei-Säure-Batterien bei hohen Entladeströmen — LiFePO4 nahezu frei davon |
| 72 | **Rogowski-Spule** | Flexible Strommesspule ohne Eisenkern — misst AC über induzierte Spannung |
| 73 | **Selbstentladung** | Kapazitätsverlust ohne externe Last. Blei-Säure: 3–5 %/Monat, LiFePO4: 1–3 %/Monat |
| 74 | **Transiente** | Kurzzeitige Überspannung (μs bis ms) — verursacht durch Blitzeinschlag, Schalthandlungen, Lichtmaschinendefekte |
| 75 | **VE.Smart Networking** | Victron-Funktion: Bluetooth-Vernetzung von Ladegeräten, Solarreglern und Batteriemonitoren für synchronisierte Ladung |

---

## 10. Schnell-Referenz

### 10.1 Sofort-Checkliste: Jährliche Elektrik-Inspektion (Kurzform)

```
□ Batterie-Ruhespannung messen (12V: > 12,5 V ✓)
□ Polklemmen visuell prüfen (kein Grünspan ✓)
□ Schalttafel auf Verfärbungen / Schmorspuren prüfen
□ Alle Sicherungen korrekt? (Wert + Typ)
□ Navigationsbeleuchtung testen (alle Laternen)
□ Bilgenpumpe testen (Handschalter + Automatik)
□ FI-Schutzschalter Prüftaste drücken (löst aus? ✓)
□ Landstromkabel visuell prüfen (keine Schäden ✓)
□ Spannungsabfall kritischer Verbraucher (< 3 % ✓)
□ Masseband Motorblock visuell prüfen
□ Ergebnisse dokumentieren!
```

### 10.2 Grenzwert-Referenzkarte

```
╔══════════════════════════════════════════════════════════════╗
║              ELEKTRIK GRENZWERTE — SCHNELLREFERENZ          ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  BATTERIE (12V Blei-Säure, Ruhe):                           ║
║    100 % SoC = 12,73 V  │  50 % SoC = 12,06 V              ║
║    Startfähig > 9,60 V   │  Tiefentladung < 11,50 V         ║
║                                                              ║
║  BATTERIE (12V LiFePO4, Ruhe):                              ║
║    100 % SoC = 13,40 V  │  50 % SoC = 13,20 V              ║
║    BMS-Cutoff < 12,80 V │  Tiefentladung < 10,00 V          ║
║                                                              ║
║  SPANNUNGSABFALL (unter Last):                               ║
║    Einzelverbindung: < 50 mV                                 ║
║    Sicherungshalter: < 100 mV                                ║
║    Gesamtstromkreis: < 3 % (< 360 mV bei 12V)               ║
║    Kritische Systeme: < 1,5 % (< 180 mV bei 12V)            ║
║                                                              ║
║  ISOLATION (Megger 500V DC):                                 ║
║    Neuzustand: > 100 MΩ │  Bestand: > 2 MΩ                 ║
║    Kritisch: < 1 MΩ     │  Alarm: < 0,5 MΩ                 ║
║                                                              ║
║  RUHESTROM (alle Verbraucher aus):                           ║
║    8–10 m SY: < 0,5 A   │  10–14 m SY: < 1,5 A             ║
║    14–18 m SY: < 3,0 A  │  Motoryacht: 1,0–8,0 A           ║
║                                                              ║
║  STREUSTROM:                                                 ║
║    Leckstrom Landstromkabel: < 30 mA (Normal)               ║
║    Referenzelektrode: -800...-1050 mV = geschützt            ║
║    Spannung vs. Nachbarboot: < 50 mV                         ║
║                                                              ║
║  THERMOGRAFIE (ΔT vs. Referenz):                             ║
║    < 5 °C Normal │ 5–15 °C Auffällig │ 15–35 °C Ernsthaft  ║
║    35–75 °C Kritisch │ > 75 °C NOTFALL — ABSCHALTEN!        ║
║                                                              ║
║  FI-SCHUTZSCHALTER:                                          ║
║    Auslösezeit Typ A 30 mA: < 40 ms                         ║
║    Prüftaste: MONATLICH betätigen!                           ║
║                                                              ║
║  ERDUNG (Widerstand):                                        ║
║    Motor → Hauptmasse: < 0,5 mΩ                             ║
║    Seeventil → Erdungsband: < 10 mΩ                         ║
║    Batterie Minus → Hauptmasse: < 1 mΩ                      ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

### 10.3 Werkzeug-Empfehlung nach Anwendertyp

| Anwender | Minimum | Empfohlen | Optimal |
|----------|---------|-----------|---------|
| **Eigner (Wochenende)** | Multimeter (Fluke 117, ~250 EUR) | + Zangenamperemeter (Fluke 323, ~180 EUR) | + Victron SmartShunt (~80 EUR) |
| **Eigner (Langfahrt)** | Multimeter (Fluke 87V, ~450 EUR) + Zangenamperemeter (Fluke 376 FC, ~650 EUR) | + Megger MIT420 (~750 EUR) | + FLIR C5 (~550 EUR) + Oszilloskop |
| **Werft / Elektriker** | Fluke 87V + 376 FC + Megger MIT420 | + FLIR E54 (~3.500 EUR) + Batterietester | + Netzanalysator + Streustrom-Equipment |
| **AYDI Level 2** | Wie "Werft / Elektriker" | + Datenlogger + Referenzelektrode | + Thermografie-Jahresabo + Trenddatenbank |

### 10.4 Sicherungszuordnung — Typische Kabelquerschnitte

| Sicherung (A) | Min. Kabelquerschnitt (mm²) bei < 3 m | Min. bei 3–6 m | Min. bei 6–12 m |
|----------------|----------------------------------------|-----------------|------------------|
| 5 A | 0,75 mm² | 1,0 mm² | 1,5 mm² |
| 10 A | 1,0 mm² | 1,5 mm² | 2,5 mm² |
| 15 A | 1,5 mm² | 2,5 mm² | 4,0 mm² |
| 20 A | 2,5 mm² | 4,0 mm² | 6,0 mm² |
| 30 A | 4,0 mm² | 6,0 mm² | 10,0 mm² |
| 50 A | 10,0 mm² | 16,0 mm² | 25,0 mm² |
| 80 A | 16,0 mm² | 25,0 mm² | 35,0 mm² |
| 100 A | 25,0 mm² | 35,0 mm² | 50,0 mm² |
| 150 A | 35,0 mm² | 50,0 mm² | 70,0 mm² |
| 200 A | 50,0 mm² | 70,0 mm² | 95,0 mm² |

Basierend auf 3 % Spannungsabfall, 12V DC, Kupfer, 30 °C Umgebungstemperatur. Für 24V-Systeme: halber Querschnitt bei gleicher Leistung. Für Motorraum (> 50 °C): eine Stufe größer wählen.

### 10.5 Jährlicher Wartungskalender Elektrik

```
╔══════════════════════════════════════════════════════════════╗
║            JÄHRLICHER WARTUNGSKALENDER ELEKTRIK              ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  JANUAR / FEBRUAR (Winterlager):                             ║
║    □ Monatliche Batteriespannungskontrolle                   ║
║    □ Erhaltungsladegerät-Funktion prüfen                     ║
║    □ Entfeuchter nachfüllen (Granulat)                       ║
║    □ Boot auf Nagetier-Aktivität prüfen                      ║
║                                                              ║
║  MÄRZ / APRIL (Inbetriebnahme):                              ║
║    □ Jährliche Inspektion (Checkliste 3.1)                   ║
║    □ Batterie-Kapazitätstest                                 ║
║    □ FI-Schutzschalter testen                                ║
║    □ Alle Systeme einzeln in Betrieb nehmen (Reihenfolge!)   ║
║    □ Spannungsabfall-Messung kritischer Verbraucher          ║
║    □ Navigationsbeleuchtung komplett testen                  ║
║                                                              ║
║  MAI / JUNI (Saisonstart):                                   ║
║    □ Motor-Elektrik nach erstem Einsatz kontrollieren        ║
║    □ Ladestrom Lichtmaschine bei Betriebstemperatur messen   ║
║    □ Solarpanel-Ertrag dokumentieren (Referenzwert)          ║
║                                                              ║
║  JULI / AUGUST (Mitte-Saison):                               ║
║    □ Mitte-Saison-Check (Kurzinspektion 3.2.2)              ║
║    □ FI-Schutzschalter Prüftaste monatlich betätigen         ║
║    □ Bilgenpumpen-Funktion bei jedem Törn prüfen             ║
║    □ Landstrom-Kabel visuell bei jedem Anschluss prüfen      ║
║                                                              ║
║  SEPTEMBER / OKTOBER (Saisonende):                           ║
║    □ Letzte umfassende Funktionsprüfung aller Systeme        ║
║    □ Batterien voll laden vor Winterlager                    ║
║    □ Winterfestmachung (Checkliste 3.4)                      ║
║    □ Solarpanel-Ertrag dokumentieren (Vergleich Saisonstart) ║
║                                                              ║
║  NOVEMBER / DEZEMBER (Winterlager):                          ║
║    □ Monatliche Batteriespannungskontrolle                   ║
║    □ Erhaltungsladegerät-Funktion prüfen                     ║
║    □ Boot auf Feuchtigkeit/Kondensation prüfen               ║
║                                                              ║
║  ALLE 5 JAHRE (zusätzlich):                                  ║
║    □ 5-Jahres-Revision (Abschnitt 3.3)                       ║
║    □ Isolationsmessung aller Stromkreise (Megger)            ║
║    □ Thermografie der Schalttafel unter Volllast              ║
║    □ Alle Crimpverbindungen in kritischen Stromkreisen       ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

### 10.6 Notfall-Kontakte und Ressourcen

| Ressource | Kontakt / Link |
|-----------|---------------|
| Seenotrettung (DE) | DGzRS: Bremen MRCC, Tel. 0421-536870, UKW Kanal 16/70 |
| Seenotrettung (AT/CH) | Über nächste Küstenwache oder Revierzentrale |
| Technische Hilfe (DE) | ADAC Sportschifffahrt: 089-76 76 77 |
| ABYC Standards | www.abycinc.org |
| ISO-Normen | www.iso.org |
| Victron Support | community.victronenergy.com |
| Fluke Support DACH | www.fluke.com/de-de |
| Marine-Elektriker finden | www.nmma.org (international), www.bvww.de (DE) |
| Versicherung (Schadenmeldung) | Pantaenius, Yacht-Pool, Allianz — Police-Nr. bereithalten |

### 10.7 Typische Stromaufnahmen von Bordverbrauchern

Referenztabelle zur Dimensionierung von Sicherungen und Kabeln (Confidence: documented):

| Verbraucher | Typischer Strom (12V) | Typischer Strom (24V) | Bemerkung |
|-------------|----------------------|----------------------|-----------|
| Ankerlicht LED | 0,15 A | 0,08 A | Dauerbetrieb nachts vor Anker |
| Navigationslichter LED (komplett) | 0,8–1,5 A | 0,4–0,8 A | Topplicht + Seitenlichter + Heck |
| Innenbeleuchtung LED (pro Leuchte) | 0,2–0,5 A | 0,1–0,25 A | 2–6 W pro Leuchte |
| Kühlschrank (Kompressor) | 3–6 A | 1,5–3 A | Anlaufstrom 3× Nennstrom |
| Tiefkühler | 4–8 A | 2–4 A | Anlaufstrom 3× Nennstrom |
| Frischwasserpumpe | 4–8 A | 2–4 A | Kurzzeitig, druckgesteuert |
| Bilgenpumpe (Standard) | 2–5 A | 1–2,5 A | 500–2000 GPH |
| Bilgenpumpe (Hochleistung) | 8–15 A | 4–7,5 A | 3000–4000 GPH |
| WC-Pumpe (elektrisch) | 10–20 A | 5–10 A | Kurzzeitig |
| UKW-Funk (Standby) | 0,3–0,5 A | 0,15–0,25 A | Dauerbetrieb |
| UKW-Funk (Senden 25W) | 5–6 A | 2,5–3 A | Kurzzeitig |
| AIS-Transponder | 0,3–1,0 A | 0,15–0,5 A | Dauerbetrieb, Sendeimpulse höher |
| Chartplotter (7") | 1–2 A | 0,5–1 A | Dauerbetrieb |
| Chartplotter (12"+) | 2–4 A | 1–2 A | Dauerbetrieb |
| Autopilot (Hydraulik) | 3–15 A | 1,5–7,5 A | Stark variabel je nach Seegang |
| Radar (4 kW) | 3–5 A | 1,5–2,5 A | Dauerbetrieb im Scanmodus |
| Ankerwinde | 60–150 A | 30–75 A | Kurzzeitig, max. 3 Minuten |
| Bugstrahlruder | 80–300 A | 40–150 A | Max. 5 Sekunden, dann Pause! |
| Elektrische Winsch (Harken 46.2) | 40–80 A | 20–40 A | Unter Last |
| Warmwasserboiler (230V AC) | — | — | 750–1500 W über Landstrom |
| Heizung (Diesel, Eberspächer) | 1–8 A | 0,5–4 A | Anlaufphase: 8 A, dann 1–2 A |
| Kompressor-Klimaanlage | — | — | 3.000–12.000 BTU, über 230V AC |
| Windmessanlage | 0,05–0,2 A | 0,025–0,1 A | Dauerbetrieb |
| Echolot | 0,1–0,3 A | 0,05–0,15 A | Dauerbetrieb |
| Log (Geschwindigkeit) | 0,05–0,1 A | 0,025–0,05 A | Dauerbetrieb |

---

## 11. Anhänge A–H — Fallstudien

### ANHANG A — Fallstudie: Totalausfall nach Winterlager (Bavaria 40 Cruiser, Bj. 2015)

**Ausgangssituation:**
Eine Bavaria 40 Cruiser (12,35 m) wurde nach 5 Monaten Winterlager ohne Landstrom in Betrieb genommen. Alle DC-Systeme tot. Eigner hatte die Batterien nicht abgeklemmt und kein Erhaltungsladegerät angeschlossen.

**Befund:**
- Verbraucher-Batteriebank (3× 110 Ah AGM, 5 Jahre alt): Ruhespannung 8,4 V → Tiefentladung
- Starterbatterie (80 Ah AGM, 5 Jahre alt): Ruhespannung 10,2 V → stark entladen
- Ruhestrom im Winterlager: 1,8 A (Kühlschrank-Thermostat vergessen, AIS-Transponder im Standby, CO-Melder)
- 1,8 A × 24 h × 150 Tage = 6.480 Ah entnommen → Batterien seit Monaten tiefentladen

**Diagnose:**
- Verbraucherbank: Innenwiderstand 18 mΩ (Neuwert: 5 mΩ) → irreversibel sulfatiert
- Starterbatterie: Innenwiderstand 11 mΩ (Neuwert: 4 mΩ) → stark sulfatiert, aber regenerierbar
- Desulfatierungsversuch Starterbatterie: CTEK MXS 5.0 "Recond"-Modus → nach 48 h: 9 mΩ → teilweise erholt
- Ladegerät Mastervolt ChargeMaster 25-3: Funktionstest OK, kein Defekt

**Maßnahmen:**
- Verbraucherbank: Komplett ersetzt durch 2× Victron LiFePO4 Smart 200 Ah (4.200 EUR)
- Starterbatterie: Im Betrieb belassen, engmaschiges Monitoring (Victron SmartShunt installiert)
- Sicherheitsmaßnahme: Blue Sea m-LVD (Low Voltage Disconnect) installiert — trennt Verbraucher bei < 12,0 V
- Winterlager-Prozedur dokumentiert: Batterie-Trennschalter OFF, Erhaltungsladegerät Pflicht

**Kosten:**
| Position | Betrag |
|----------|--------|
| 2× Victron LiFePO4 Smart 200 Ah | 4.200 EUR |
| Victron SmartShunt 500A | 80 EUR |
| Blue Sea m-LVD | 65 EUR |
| Einbau + Verkabelung (Fachbetrieb) | 850 EUR |
| **Gesamt** | **5.195 EUR** |

**Lehre:** 5 Monate Vernachlässigung → 5.195 EUR Schaden. Ein Erhaltungsladegerät (100 EUR) hätte alles verhindert.

### ANHANG B — Fallstudie: Streustrom-Schaden im Hafenliegeplatz (Hallberg-Rassy 43 Mk II, Bj. 2008)

**Ausgangssituation:**
HR 43 Dauerlieger in einer Marina an der Ostsee. Propeller (3-Blatt Bronze Gori, 1.800 EUR) nach nur 14 Monaten massiv korrodiert. Opferanoden (Zink) nach 6 Monaten aufgelöst. Eigner hat galvanischen Isolator installiert (Marinco CruiseGard).

**Befund:**
- Propeller: Tiefes Pitting, Materialverlust ca. 3 mm an Blattspitzen, Unwucht spürbar
- Wellenanlage: Anfängliches Pitting am Wellenende
- Seeventile: Leichtes Pitting an Bronze-Seeventilen
- Referenzelektrode-Messung: -420 mV vs. Ag/AgCl → massiver Unterschutz!
- Leckstrom am Landstromkabel: 380 mA (!!!)
- Galvanischer Isolator: Defekt — Dioden durchlegiert, kein Blockiereffekt mehr

**Diagnose (systematisch):**
1. Landstrom getrennt → Leckstrom verschwunden → Problem im AC-Netz
2. Eigenes Boot isoliert → Leckstrom immer noch 350 mA → Nachbarboot!
3. Nachbarboot (Jeanneau 44DS) untersucht: Warmwasserboiler mit Erdschluss, 4,5 A Leckstrom ins Wasser
4. Eigener galvanischer Isolator: Defekt durch Überspannung (Blitz am Steg vermutet)

**Maßnahmen:**
- Nachbareigner informiert → Boiler repariert → Leckstrom eliminiert
- Galvanischer Isolator durch Victron Isolation Transformer 3600W (Trenntrafo) ersetzt → vollständige galvanische Trennung
- Propeller ausgetauscht (Materialermüdung durch Pitting)
- Alle Opferanoden erneuert (Aluminium statt Zink für besseren Schutz)
- Halbjährliche Referenzelektroden-Messung vereinbart

**Kosten:**
| Position | Betrag |
|----------|--------|
| Gori 3-Blatt Faltpropeller (Neuteil) | 3.800 EUR |
| Victron Isolation Transformer 3600W | 1.200 EUR |
| Opferanoden-Set (Aluminium) | 180 EUR |
| Kranen + Propellertausch + Einbau Trenntrafo | 1.800 EUR |
| **Gesamt** | **6.980 EUR** |

**Lehre:** Galvanische Isolatoren bieten keinen vollständigen Schutz und können ausfallen. Ein Trenntrafo ist die sicherste Lösung für Dauerlieger. Nachbarboote mit Elektrik-Fehlern können das eigene Boot zerstören.

### ANHANG C — Fallstudie: Kabelbrand durch überlastete Crimpverbindung (Hanse 415, Bj. 2016)

**Ausgangssituation:**
Während einer Nachtfahrt Rauchentwicklung aus der Schalttafel. Eigner hat Batterie-Hauptschalter rechtzeitig ausgeschaltet. Kein offener Brand, aber Schmorschaden.

**Befund:**
- Geschmorte Crimpverbindung am Pluskabel der elektrischen Ankerwinde (35 mm²)
- Crimpverbinder: Standard-PVC-Verbinder (nicht Marine-Grade), offensichtlich nachrüstlich montiert
- Kabel-Querschnitt am Crimpverbinder: Nur 18 der 35 mm² Einzeldrähte vom Crimpverbinder erfasst → effektiver Querschnitt 18 mm²
- Ankerwinde zieht 80 A Spitzenstrom → 80 A durch 18 mm² = 4,4 A/mm² → massive Überlastung

**Ursache-Analyse:**
- Bei einer früheren Reparatur wurde das Kabel gekürzt und mit einer handelsüblichen (nicht-marine) Crimpzange verpresst
- Unzureichende Crimpkraft → nur halber Querschnitt kontaktiert
- Kein Schrumpfschlauch → Feuchtigkeit konnte in die Crimpstelle eindringen
- Korrosion an den nicht verpressten Adern → Übergangswiderstand stieg über Monate
- I²R-Verlustleistung: 80² × 0,002 Ω = 12,8 W an einer einzelnen Crimpstelle!

**Maßnahmen:**
- Gesamtes Ankerwinden-Kabel ersetzt (Batterie → Schalter → Sicherung → Winde)
- Marine-Grade-Crimpverbinder (Ancor) mit Ratchet-Crimpzange verpresst
- Doppelwand-Schrumpfschlauch mit Kleber über jeder Verbindung
- Thermografie der gesamten Schalttafel durchgeführt → 2 weitere auffällige Verbindungen präventiv erneuert
- 150 A ANL-Sicherung direkt am Batteriepol nachgerüstet (fehlte!)

**Kosten:**
| Position | Betrag |
|----------|--------|
| Kabel 35 mm² tinned (8 m) | 120 EUR |
| Marine-Crimpverbinder + Schrumpfschlauch | 45 EUR |
| ANL-Sicherungshalter + 150 A Sicherung | 35 EUR |
| Fachbetrieb (Einbau + Thermografie) | 650 EUR |
| Schalttafel-Reinigung (Ruß) | 180 EUR |
| **Gesamt** | **1.030 EUR** |

**Lehre:** EINE schlechte Crimpverbindung kann einen Brand verursachen. Marine-Grade-Crimpwerkzeug und -verbinder sind keine Luxusausgabe, sondern Sicherheitsnotwendigkeit. Fehlende Hauptsicherung am Batteriepol ist ein häufiger und gefährlicher Mangel.

### ANHANG D — Fallstudie: EMV-Störungen nach LED-Umrüstung (X-Yachts X-43, Bj. 2006)

**Ausgangssituation:**
Nach Umrüstung der gesamten Innenbeleuchtung auf LED-Leuchtmittel (G4-Bi-Pin, 12V) massive Störungen am UKW-Funk (Rauschen, eingeschränkte Reichweite), GPS-Positionssprünge bis 200 m und Kompassabweichung von 8°.

**Befund:**
- 22 LED-Leuchtmittel No-Name (China-Import, ca. 2 EUR/Stück) eingebaut
- Keine EMV-Prüfung, keine CE-Kennzeichnung (oder gefälschte)
- Oszilloskop-Messung: 150–250 mV pp Breitbandstörung (500 kHz – 30 MHz) auf DC-Bus bei eingeschalteter Beleuchtung
- SDR-Analyse: Erhöhtes Rauschmaß im VHF-Band (156–162 MHz) um 15 dB
- Fluxgate-Kompass (B&G): Ablenkung durch ungeschirmte LED-Treiber in Deckenkonsolen direkt über Kompass

**Ursache:**
- Billig-LEDs verwenden ungeschirmte Buck-Converter als Treiber
- Hochfrequente Schaltstörungen (PWM > 500 kHz) strahlen über die Kabel als Antenne ab
- Magnetfeld der ungeschirmten Induktivitäten im LED-Treiber beeinflusst Fluxgate-Kompass

**Maßnahmen:**
- Alle 22 LED-Leuchtmittel gegen Marine-Grade LEDs (Hella Marine) getauscht → 380 EUR
- 4 LEDs in der Nähe des Kompass: Zusätzlich Ferritkerne (Fair-Rite 0431164181) auf Zuleitungen
- Kabelführung: Beleuchtungs-Stromkreise von Instrumenten-Stromkreisen getrennt
- Nachmessung: Störpegel < 20 mV pp auf DC-Bus, VHF-Rauschmaß wieder auf Normalwert, Kompassabweichung < 1°

**Kosten:**
| Position | Betrag |
|----------|--------|
| 22× Hella Marine LED G4 (je 17 EUR) | 374 EUR |
| 8× Ferritkerne | 24 EUR |
| Einbau (Eigenleistung) | 0 EUR |
| Weggeworfene Billig-LEDs | 44 EUR (Verlust) |
| **Gesamt** | **442 EUR** |

**Lehre:** Bei LED-Umrüstung auf Booten NUR Marine-Grade-LEDs mit nachgewiesener EMV-Konformität verwenden. Die Ersparnis von 330 EUR (Billig vs. Marine-Grade) steht einem potenziellen Sicherheitsrisiko und Funktionsverlust der Navigation gegenüber.

### ANHANG E — Fallstudie: Isolationsfehler durch Kondenswasser (Beneteau Oceanis 46.1, Bj. 2019)

**Ausgangssituation:**
FI-Schutzschalter löst bei Landstrom-Anschluss nach 10–30 Minuten aus. Problem tritt nur in der Übergangszeit (Frühjahr/Herbst) auf, im Sommer nicht.

**Befund:**
- FI-Schutzschalter selbst in Ordnung (Auslösetest: 28 ms bei 30 mA → einwandfrei)
- Isolationsmessung aller AC-Stromkreise: Warmwasserboiler-Zuleitung nur 0,8 MΩ (soll > 2 MΩ)
- Kabel zum Warmwasserboiler verläuft durch einen unbelüfteten Hohlraum unter der Achterkajüte
- In diesem Hohlraum: Massive Kondensation auf allen Oberflächen (Temperaturunterschied Seewasser↔Innenraum)
- Kabeldurchführung durch Schott ohne Dichtung → Kondenswasser läuft am Kabel entlang in die Verteilerdose

**Ursache:**
- Temperaturwechsel Frühjahr/Herbst → Kondenswasser auf kaltem Kabel
- Wasser sammelt sich in Verteilerdose → Isolation sinkt → FI löst aus
- Im Sommer: Boot durchgewärmt, keine Kondensation → kein Problem

**Maßnahmen:**
- Verteilerdose durch IP 67-Version (Wiska COMBI 308) ersetzt
- Kabeldurchführung durch Schott mit Kabeldichtung (Roxtec) abgedichtet
- Drip-Loop (Entwässerungsschleife) im Kabel vor der Verteilerdose
- Belüftung des Hohlraums durch zwei Dorade-Ventilatoren verbessert
- Isolationsmessung nach Maßnahmen: 85 MΩ → Problem gelöst

**Kosten:**
| Position | Betrag |
|----------|--------|
| IP 67 Verteilerdose (Wiska COMBI 308) | 35 EUR |
| Roxtec Kabeldurchführung | 45 EUR |
| 2× Dorade-Ventilator (klein) | 120 EUR |
| Einbau (Eigenleistung, ca. 6 h) | 0 EUR |
| **Gesamt** | **200 EUR** |

**Lehre:** Kondensation ist ein häufiges und unterschätztes Problem in der Marine-Elektrik. Jede Kabeldurchführung durch ein Schott muss abgedichtet sein. Drip-Loops verhindern, dass Wasser am Kabel entlang in Verteilerdosen läuft.

### ANHANG F — Fallstudie: Lichtmaschinen-Überladung zerstört AGM-Batterien (Jeanneau Sun Odyssey 440, Bj. 2020)

**Ausgangssituation:**
Eigner bemerkt Gasgeruch (Schwefel) aus dem Batteriekasten. Batterien (2× Victron AGM 220 Ah, 1,5 Jahre alt) heiß, Gehäuse leicht aufgebläht.

**Befund:**
- Ladespannung bei laufendem Motor (2.000 RPM): 15,8 V (!!!)
- Sollwert AGM: max. 14,4 V Absorption, 13,8 V Float
- Laderegler (integriert in Lichtmaschine): Defekt — Regelung ausgefallen, volle Lichtmaschinenspannung an Batterie
- Batterien: Innenwiderstand 22 mΩ (Neuwert: 5 mΩ) → irreversibel geschädigt durch Überladung
- Elektrolyt teilweise ausgetrocknet (AGM-Vlies nicht mehr vollständig gesättigt)

**Ursache:**
- Lichtmaschinen-Regler (Valeo-Typ) hat nach 18 Monaten im Marine-Einsatz versagt
- Standard-Kfz-Regler sind für Marine-Bedingungen oft nicht ausgelegt (Feuchtigkeit, Vibrationen)
- Kein externer Laderegler, kein Spannungswächter installiert

**Maßnahmen:**
- Beide AGM-Batterien ersetzt → 2× Victron AGM 220 Ah
- Externer Hochleistungs-Laderegler Balmar MC-614 installiert
- Ladeprofil korrekt für AGM programmiert (14,4 V Absorption, 13,8 V Float, 30 min Absorption-Timer)
- Victron SmartShunt mit High-Voltage-Alarm (> 14,5 V) installiert → App-Benachrichtigung auf Handy

**Kosten:**
| Position | Betrag |
|----------|--------|
| 2× Victron AGM 220 Ah | 980 EUR |
| Balmar MC-614 Laderegler | 420 EUR |
| Victron SmartShunt 500A | 80 EUR |
| Einbau + Programmierung (Fachbetrieb) | 550 EUR |
| **Gesamt** | **2.030 EUR** |

**Lehre:** Ein externer Hochleistungs-Laderegler mit korrektem Batterie-Profil ist die wichtigste Schutzmaßnahme für die Batteriebank. Spannungswächter mit Alarm sind kostengünstig und verhindern teure Folgeschäden.

### ANHANG G — Fallstudie: Nagetier-Schaden im Winterlager (Dehler 38 SQ, Bj. 2017)

**Ausgangssituation:**
Bei der Inbetriebnahme nach dem Winterlager (an Land, Plane abgedeckt, kein Landstrom): Mehrere Stromkreise funktionslos, Sicherungsautomaten lassen sich nicht einschalten.

**Befund:**
- Mäusenest im Bereich der Schalttafel (hinter dem Navigationsplatz)
- 6 Kabel mit angefressener Isolierung, davon 2 mit blankliegenden Kupferleitern
- Kurzschluss zwischen zwei beschädigten Kabeln → Sicherungsautomat ausgelöst und blockiert
- Kotspuren und Urin auf Schalttafel-Platine → Korrosion der Leiterbahnen
- Mäuse sind über das Landstromkabel am Steg an Bord gelangt (Kabel lag auf dem Boden)

**Maßnahmen:**
- Alle 6 beschädigten Kabel komplett ersetzt (nicht nur repariert — Bissspuren schwächen die Isolation dauerhaft)
- Schalttafel-Platine gereinigt (Isopropanol), getrocknet und mit Plastik-70-Schutzlack versiegelt
- Kabelschächte mit Stahlwolle verschlossen (Mäuse können Stahlwolle nicht durchbeißen)
- Ultraschall-Mäuseabwehr installiert (batteriebetrieben, 4× AA, hält eine Saison)
- Landstromkabel im nächsten Winter: Aufgehängt, nicht auf dem Boden. Zusätzlich Mäuseschutz-Manschette

**Kosten:**
| Position | Betrag |
|----------|--------|
| Kabel + Crimpverbinder + Schrumpfschlauch | 85 EUR |
| Plastik-70 Schutzlack | 18 EUR |
| Ultraschall-Mäuseabwehr | 35 EUR |
| Stahlwolle + Dichtmasse | 12 EUR |
| Fachbetrieb (Kabel erneuern, 6 h) | 480 EUR |
| **Gesamt** | **630 EUR** |

**Lehre:** Mäuse sind eine reale und unterschätzte Gefahr für die Bordelektrik im Winterlager. Zugangswege konsequent verschließen, Landstromkabel aufhängen, Ultraschall-Abwehr als zusätzliche Maßnahme.

### ANHANG H — Fallstudie: NMEA-2000-Netzwerk instabil (Contest 42CS, Bj. 2012)

**Ausgangssituation:**
Intermittierende Ausfälle einzelner NMEA-2000-Geräte (Windmesser, AIS, Autopilot-Kompass). Ausfälle treten zufällig auf, manchmal minutenlang, manchmal tagelang stabil.

**Befund:**
- NMEA-2000-Backbone: Micro-C-Kabel, 14 Geräte angeschlossen
- Backbone-Spannung: 11,2 V (soll 9–16 V) → knapp OK
- Backbone-Spannung unter Last (alle Geräte aktiv): Schwankt zwischen 8,5 V und 11,5 V → Unterspannung!
- Ein Terminator fehlte (nur an einem Ende vorhanden, am anderen Ende: offenes T-Stück)
- Oszilloskop am CAN-Bus: Reflexionen und Signalverzerrungen sichtbar
- Drop-Kabel zum Windmesser am Masttopp: 9 m lang (Spezifikation: max. 6 m)

**Ursache:**
1. Fehlender Terminator → Signalreflexionen → Datenkorruption
2. Zu langes Drop-Kabel → zusätzliche Signaldämpfung
3. Backbone-Versorgung über zu dünnes Kabel → Spannungseinbrüche bei hoher Bus-Last

**Maßnahmen:**
- Fehlenden 120-Ω-Terminator eingesetzt
- Drop-Kabel zum Windmesser: Micro-C durch CAN-Bus-Repeater (Actisense A2K-RSP-1) am Mastfuß verlängert
- Backbone-Versorgung: Separates 2,5 mm²-Kabel direkt von Schalttafel zum Power-T-Stück
- Nachmessung: Backbone-Spannung stabil 12,1 V, Oszilloskop zeigt saubere CAN-Signale

**Kosten:**
| Position | Betrag |
|----------|--------|
| NMEA-2000-Terminator (Micro-C) | 12 EUR |
| Actisense A2K-RSP-1 Repeater | 180 EUR |
| Kabel 2,5 mm² (5 m) | 8 EUR |
| Einbau (Eigenleistung, 4 h) | 0 EUR |
| **Gesamt** | **200 EUR** |

**Lehre:** NMEA-2000-Netzwerke benötigen IMMER zwei Terminatoren (120 Ω an jedem Backbone-Ende). Drop-Kabel > 6 m erfordern einen Repeater. Die Backbone-Spannungsversorgung wird oft vernachlässigt und verursacht intermittierende Ausfälle, die schwer zu diagnostizieren sind.

### Zusammenfassung der Fallstudien — Lessons Learned

| Nr. | Fallstudie | Kernursache | Kosten | Prävention (Kosten) | Faktor |
|-----|-----------|-------------|--------|---------------------|--------|
| A | Totalausfall nach Winter | Keine Erhaltungsladung | 5.195 EUR | Erhaltungsladegerät (100 EUR) | 52× |
| B | Streustrom-Korrosion | Defekter galv. Isolator + Nachbar | 6.980 EUR | Trenntrafo (1.200 EUR) | 6× |
| C | Kabelbrand | Schlechte Crimpverbindung | 1.030 EUR | Marine-Crimpwerkzeug (120 EUR) | 9× |
| D | EMV nach LED-Umbau | Billige LEDs ohne EMV | 442 EUR | Marine-Grade LEDs von Anfang an (+330 EUR) | 1,3× |
| E | FI löst aus (Kondens.) | Undichte Kabeldurchführung | 200 EUR | Dichtung bei Installation (20 EUR) | 10× |
| F | Überladung zerstört AGM | Defekter Laderegler | 2.030 EUR | Externer Laderegler + Alarm (500 EUR) | 4× |
| G | Nagetier-Schaden | Offene Zugänge im Winterlager | 630 EUR | Mäuseschutz (47 EUR) | 13× |
| H | NMEA-2000 instabil | Fehlender Terminator | 200 EUR | Korrekte Installation (12 EUR) | 17× |

**Durchschnittlicher Präventionsfaktor: 14×** — Für jeden Euro in Prävention investiert, werden durchschnittlich 14 Euro Reparaturkosten vermieden.

**Häufigste Grundursachen über alle Fallstudien:**
1. Vernachlässigte Wartung / fehlende regelmäßige Inspektion (3 von 8 Fällen)
2. Falsche oder unzureichende Materialien/Komponenten (3 von 8 Fällen)
3. Fehlende Schutzmaßnahmen (2 von 8 Fällen)

**AYDI-Empfehlung:** Jede Yacht sollte mindestens die jährliche Elektrik-Inspektion (Abschnitt 3.1) durchlaufen. Die Investition in hochwertige Komponenten (Marine-Grade) und regelmäßige Dokumentation amortisiert sich vielfach. Ein Victron SmartShunt (80 EUR) als permanentes Monitoring-System erkennt Batterieprobleme, bevor sie zu Ausfällen führen.

**Statistische Verteilung der Schadensursachen (Confidence: benchmark — Pantaenius Versicherungsdaten DACH 2020–2024):**

| Schadensursache | Anteil an Elektrik-Schäden | Durchschn. Schadenshöhe |
|----------------|---------------------------|------------------------|
| Batterie-/Ladedefekt | 28 % | 1.800 EUR |
| Korrosion/Kontaktprobleme | 22 % | 2.400 EUR |
| Streustrom-Korrosion | 15 % | 5.200 EUR |
| Kabelbrand/Überhitzung | 12 % | 6.800 EUR |
| Blitzschlag | 8 % | 18.500 EUR |
| Wassereintritt in Elektrik | 7 % | 3.100 EUR |
| Fehlbedienung/falscher Einbau | 5 % | 2.200 EUR |
| Sonstige | 3 % | 1.500 EUR |

---

## 12. Anhänge I–R — Pydantic v2 Modelle

### ANHANG I — Basismodelle

```python
"""
AYDI Electrical Maintenance — Base Models
Pydantic v2 with model_config = {"from_attributes": True}
NEVER use class Config — always model_config dict.
German UI, English code.
"""

from __future__ import annotations

from datetime import date, datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, field_validator


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------

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


class Severity(str, Enum):
    """Schweregrad / Severity classification."""
    INFO = "info"           # Hinweis
    LOW = "low"             # Gering (A)
    MEDIUM = "medium"       # Mittel (B)
    HIGH = "high"           # Hoch (C)
    CRITICAL = "critical"   # Kritisch (D)


class InspectionType(str, Enum):
    ANNUAL = "annual"                   # Jährliche Inspektion
    SEASONAL = "seasonal"               # Saisonale Wartung
    FIVE_YEAR = "five_year"             # 5-Jahres-Revision
    WINTERIZATION = "winterization"     # Winterfestmachung
    COMMISSIONING = "commissioning"     # Inbetriebnahme
    EMERGENCY = "emergency"             # Notfallreparatur


class BatteryChemistry(str, Enum):
    FLOODED = "flooded"     # Blei-Säure offen
    AGM = "agm"             # Absorbent Glass Mat
    GEL = "gel"             # Gel-Batterie
    LIFEPO4 = "lifepo4"     # Lithium-Eisenphosphat


class ElectricalSystem(str, Enum):
    DC_12V = "dc_12v"
    DC_24V = "dc_24v"
    DC_48V = "dc_48v"
    AC_230V = "ac_230v"
    AC_120V = "ac_120v"


class FaultCategory(str, Enum):
    CORROSION = "corrosion"
    OVERHEATING = "overheating"
    INSULATION = "insulation"
    STRAY_CURRENT = "stray_current"
    OVERCHARGE = "overcharge"
    UNDERCHARGE = "undercharge"
    EMI = "emi"
    MECHANICAL = "mechanical"
    WATER_INGRESS = "water_ingress"
    RODENT_DAMAGE = "rodent_damage"


# ---------------------------------------------------------------------------
# Base Models
# ---------------------------------------------------------------------------

class ConfidenceAnnotation(BaseModel):
    """Confidence annotation for any measurement or assessment."""
    model_config = {"from_attributes": True}

    level: ConfidenceLevel
    source: str = Field(
        ...,
        description="Source of the confidence (e.g., 'ABYC E-11', 'Fluke 87V measurement')"
    )
    notes: Optional[str] = None


class MeasurementValue(BaseModel):
    """A single measurement with value, unit, and confidence."""
    model_config = {"from_attributes": True}

    value: float
    unit: str = Field(..., description="SI unit (V, A, Ω, MΩ, mV, mA, °C, %)")
    confidence: ConfidenceAnnotation
    measured_at: Optional[datetime] = None
    instrument: Optional[str] = Field(
        None, description="Instrument used (e.g., 'Fluke 87V SN:12345')"
    )
    conditions: Optional[str] = Field(
        None, description="Measurement conditions (e.g., '25°C, 55% rH, under load 80A')"
    )


class ThresholdRange(BaseModel):
    """Defines acceptable, warning, and critical ranges for a measurement."""
    model_config = {"from_attributes": True}

    parameter: str
    unit: str
    optimal_min: Optional[float] = None
    optimal_max: Optional[float] = None
    warning_min: Optional[float] = None
    warning_max: Optional[float] = None
    critical_min: Optional[float] = None
    critical_max: Optional[float] = None
    source: str = Field(..., description="Norm or standard (e.g., 'ABYC E-11')")
```

### ANHANG J — Inspektionsmodelle

```python
"""
AYDI Electrical Maintenance — Inspection Models
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, Field

from .base_models import (
    ConfidenceAnnotation,
    ConfidenceLevel,
    InspectionType,
    MeasurementValue,
    Severity,
)


class InspectionCheckItem(BaseModel):
    """Single item in an inspection checklist."""
    model_config = {"from_attributes": True}

    item_id: str = Field(..., description="Unique ID (e.g., 'BAT-001')")
    category: str = Field(..., description="Category (e.g., 'Batterien', 'Schalttafel')")
    description_de: str = Field(..., description="German description of check item")
    passed: Optional[bool] = None
    measurement: Optional[MeasurementValue] = None
    finding: Optional[str] = Field(None, description="Finding description if not passed")
    severity: Optional[Severity] = None
    photo_refs: list[str] = Field(default_factory=list)
    recommendation_de: Optional[str] = None


class InspectionReport(BaseModel):
    """Complete electrical inspection report."""
    model_config = {"from_attributes": True}

    report_id: str
    yacht_id: str
    inspection_type: InspectionType
    inspector: str
    date_performed: date
    date_report: date
    yacht_name: Optional[str] = None
    yacht_type: Optional[str] = None
    yacht_loa_m: Optional[float] = None
    electrical_system: str = Field(
        ..., description="Primary system voltage (e.g., '12V DC / 230V AC')"
    )
    battery_bank_info: Optional[str] = None
    hours_spent: Optional[float] = None
    check_items: list[InspectionCheckItem] = Field(default_factory=list)
    summary_de: str = Field(..., description="German executive summary")
    critical_findings: list[InspectionCheckItem] = Field(default_factory=list)
    recommendations_de: list[str] = Field(default_factory=list)
    next_inspection_date: Optional[date] = None
    overall_score: Optional[float] = Field(
        None, ge=0, le=100, description="Overall electrical condition score 0-100"
    )
    confidence: ConfidenceAnnotation

    @property
    def pass_rate(self) -> float:
        """Percentage of passed check items."""
        if not self.check_items:
            return 0.0
        passed = sum(1 for item in self.check_items if item.passed is True)
        return round(passed / len(self.check_items) * 100, 1)
```

### ANHANG K — Batterie-Diagnosemodelle

```python
"""
AYDI Electrical Maintenance — Battery Diagnostic Models
"""

from __future__ import annotations

from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, Field, field_validator

from .base_models import (
    BatteryChemistry,
    ConfidenceAnnotation,
    MeasurementValue,
    Severity,
)


class BatteryCondition(BaseModel):
    """Detailed condition assessment of a single battery."""
    model_config = {"from_attributes": True}

    battery_id: str
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    chemistry: BatteryChemistry
    nominal_voltage: float = Field(..., description="Nominal voltage in V (12, 24, 48)")
    nominal_capacity_ah: float = Field(..., description="Nominal capacity in Ah")
    manufacture_date: Optional[date] = None
    install_date: Optional[date] = None
    age_months: Optional[int] = None

    # Measurements
    open_circuit_voltage: Optional[MeasurementValue] = None
    voltage_under_load: Optional[MeasurementValue] = None
    internal_resistance: Optional[MeasurementValue] = None
    state_of_charge_pct: Optional[float] = Field(None, ge=0, le=100)
    state_of_health_pct: Optional[float] = Field(None, ge=0, le=100)
    electrolyte_level: Optional[str] = Field(
        None, description="OK / Low / Critical (flooded only)"
    )
    temperature: Optional[MeasurementValue] = None

    # Assessment
    severity: Severity = Severity.INFO
    finding_de: Optional[str] = None
    recommendation_de: Optional[str] = None
    estimated_remaining_life_months: Optional[int] = None
    confidence: ConfidenceAnnotation = ConfidenceAnnotation(
        level=ConfidenceLevel.ESTIMATED,
        source="AYDI battery assessment algorithm",
    )

    @field_validator("nominal_voltage")
    @classmethod
    def validate_nominal_voltage(cls, v: float) -> float:
        if v not in (6, 12, 24, 36, 48):
            raise ValueError("Nominal voltage must be 6, 12, 24, 36, or 48 V")
        return v


class BatteryBankAssessment(BaseModel):
    """Assessment of a complete battery bank."""
    model_config = {"from_attributes": True}

    bank_id: str
    bank_name_de: str = Field(..., description="e.g., 'Verbraucherbank', 'Starterbank'")
    batteries: list[BatteryCondition] = Field(default_factory=list)
    configuration: str = Field(
        ..., description="e.g., '3S1P', '2S2P', '1S1P'"
    )
    total_capacity_ah: float
    usable_capacity_ah: float = Field(
        ..., description="Usable capacity considering DoD limits"
    )
    bank_voltage: Optional[MeasurementValue] = None
    bank_current: Optional[MeasurementValue] = None
    imbalance_mv: Optional[float] = Field(
        None, description="Voltage imbalance between cells/batteries in mV"
    )
    max_acceptable_imbalance_mv: float = Field(
        default=500.0,
        description="Max acceptable imbalance in mV (500 mV for lead-acid, 50 mV for LiFePO4)"
    )
    estimated_autonomy_hours: Optional[float] = None
    severity: Severity = Severity.INFO
    finding_de: Optional[str] = None
    recommendation_de: Optional[str] = None
    confidence: ConfidenceAnnotation
```

### ANHANG L — Isolationsmessmodelle

```python
"""
AYDI Electrical Maintenance — Insulation Test Models
"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, field_validator

from .base_models import ConfidenceAnnotation, MeasurementValue, Severity


class InsulationTestResult(BaseModel):
    """Single insulation resistance measurement."""
    model_config = {"from_attributes": True}

    circuit_id: str = Field(..., description="Circuit identifier (e.g., 'AC-Main-L1')")
    circuit_name_de: str = Field(..., description="German name (e.g., 'Landstrom Phase')")
    test_voltage_v: float = Field(..., description="Applied test voltage in V DC")
    r_15s: Optional[MeasurementValue] = Field(
        None, description="Insulation resistance at 15 seconds"
    )
    r_60s: Optional[MeasurementValue] = Field(
        None, description="Insulation resistance at 60 seconds"
    )
    r_600s: Optional[MeasurementValue] = Field(
        None, description="Insulation resistance at 10 minutes"
    )
    dar: Optional[float] = Field(
        None, description="Dielectric Absorption Ratio (R_60s / R_15s)"
    )
    pi: Optional[float] = Field(
        None, description="Polarisation Index (R_600s / R_60s)"
    )
    ambient_temp_c: Optional[float] = None
    ambient_humidity_pct: Optional[float] = None
    corrected_r_60s: Optional[MeasurementValue] = Field(
        None, description="Temperature-corrected insulation resistance"
    )
    instrument: str = Field(..., description="e.g., 'Megger MIT420/2 SN:2024-xxxxx'")
    measured_at: datetime
    severity: Severity = Severity.INFO
    finding_de: Optional[str] = None
    recommendation_de: Optional[str] = None
    confidence: ConfidenceAnnotation

    @field_validator("test_voltage_v")
    @classmethod
    def validate_test_voltage(cls, v: float) -> float:
        allowed = [10, 25, 50, 100, 250, 500, 1000, 2500, 5000]
        if v not in allowed:
            raise ValueError(f"Test voltage must be one of {allowed}")
        return v


class InsulationTestReport(BaseModel):
    """Complete insulation test report for a yacht."""
    model_config = {"from_attributes": True}

    report_id: str
    yacht_id: str
    date_tested: datetime
    tester: str
    instrument: str
    results: list[InsulationTestResult] = Field(default_factory=list)
    overall_assessment_de: str
    overall_severity: Severity
    lowest_reading: Optional[MeasurementValue] = None
    worst_circuit: Optional[str] = None
    confidence: ConfidenceAnnotation

    @property
    def circuits_below_minimum(self) -> list[InsulationTestResult]:
        """Return circuits with insulation resistance below 2 MΩ."""
        below = []
        for r in self.results:
            if r.r_60s and r.r_60s.value < 2.0:
                below.append(r)
        return below
```

### ANHANG M — Streustrom-Diagnosemodelle

```python
"""
AYDI Electrical Maintenance — Stray Current Diagnostic Models
"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from .base_models import ConfidenceAnnotation, MeasurementValue, Severity


class ReferenceElectrodeMeasurement(BaseModel):
    """Single reference electrode (Ag/AgCl) measurement."""
    model_config = {"from_attributes": True}

    measurement_id: str
    location_de: str = Field(
        ..., description="Measurement location (e.g., 'Steuerbord Mitte')"
    )
    potential_mv: float = Field(
        ..., description="Potential vs Ag/AgCl in mV (negative = cathodic)"
    )
    shore_power_connected: bool
    measured_at: datetime
    water_type: str = Field(
        ..., description="'saltwater' | 'brackish' | 'freshwater'"
    )
    water_temp_c: Optional[float] = None
    assessment_de: str = Field(
        ...,
        description="German assessment (e.g., 'Ausreichend geschützt')"
    )
    severity: Severity
    confidence: ConfidenceAnnotation


class LeakageCurrentMeasurement(BaseModel):
    """DC leakage current measurement on shore power cable."""
    model_config = {"from_attributes": True}

    measurement_id: str
    current_ma: float = Field(
        ..., description="Measured leakage current in mA"
    )
    instrument: str
    shore_power_voltage: Optional[float] = None
    measured_at: datetime
    all_consumers_off: bool = Field(
        default=False, description="Whether all consumers were off during measurement"
    )
    assessment_de: str
    severity: Severity
    confidence: ConfidenceAnnotation


class StrayCurrentReport(BaseModel):
    """Complete stray current diagnostic report."""
    model_config = {"from_attributes": True}

    report_id: str
    yacht_id: str
    date_tested: datetime
    tester: str
    electrode_measurements: list[ReferenceElectrodeMeasurement] = Field(
        default_factory=list
    )
    leakage_measurements: list[LeakageCurrentMeasurement] = Field(
        default_factory=list
    )
    galvanic_isolator_installed: bool = False
    galvanic_isolator_functional: Optional[bool] = None
    isolation_transformer_installed: bool = False
    anode_condition_de: Optional[str] = None
    anode_material: Optional[str] = Field(
        None, description="'zinc' | 'aluminum' | 'magnesium'"
    )
    overall_assessment_de: str
    overall_severity: Severity
    recommendations_de: list[str] = Field(default_factory=list)
    confidence: ConfidenceAnnotation
```

### ANHANG N — Thermografie-Modelle

```python
"""
AYDI Electrical Maintenance — Thermography Models
"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from .base_models import ConfidenceAnnotation, MeasurementValue, Severity


class ThermalAnomaly(BaseModel):
    """A single thermal anomaly detected during thermographic inspection."""
    model_config = {"from_attributes": True}

    anomaly_id: str
    location_de: str = Field(
        ..., description="Location (e.g., 'Schalttafel, Sicherung #7')"
    )
    component_de: str = Field(
        ..., description="Component (e.g., 'ATO-Sicherungshalter 15A')"
    )
    measured_temp_c: float
    reference_temp_c: float = Field(
        ..., description="Temperature of equivalent unaffected component"
    )
    delta_t_c: float = Field(
        ..., description="Temperature difference (measured - reference)"
    )
    ambient_temp_c: float
    load_current_a: Optional[float] = Field(
        None, description="Current at time of measurement"
    )
    load_percentage: Optional[float] = Field(
        None, ge=0, le=100, description="Load as percentage of rated capacity"
    )
    emissivity: float = Field(
        default=0.95, ge=0.01, le=1.0,
        description="Emissivity setting used for measurement"
    )
    image_ref: Optional[str] = Field(
        None, description="Reference to thermal image file"
    )
    severity: Severity
    assessment_de: str
    recommendation_de: str
    urgency_de: str = Field(
        ..., description="e.g., 'Sofort', 'Wochen', 'Monate', 'Nächste planmäßige Wartung'"
    )
    confidence: ConfidenceAnnotation


class ThermographyReport(BaseModel):
    """Complete thermographic inspection report."""
    model_config = {"from_attributes": True}

    report_id: str
    yacht_id: str
    date_inspected: datetime
    inspector: str
    camera_model: str = Field(
        ..., description="e.g., 'FLIR C5 SN:xxx'"
    )
    ambient_temp_c: float
    humidity_pct: Optional[float] = None
    load_condition_de: str = Field(
        ..., description="e.g., 'Volle Bordlast, Landstrom + Motor'"
    )
    anomalies: list[ThermalAnomaly] = Field(default_factory=list)
    areas_inspected_de: list[str] = Field(
        default_factory=list,
        description="e.g., ['DC-Schalttafel', 'AC-Schalttafel', 'Batteriepole']"
    )
    overall_assessment_de: str
    overall_severity: Severity
    confidence: ConfidenceAnnotation

    @property
    def critical_anomalies(self) -> list[ThermalAnomaly]:
        return [a for a in self.anomalies if a.severity in (Severity.HIGH, Severity.CRITICAL)]
```

### ANHANG O — Fehlerbild-Modelle

```python
"""
AYDI Electrical Maintenance — Fault Pattern Models
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from .base_models import (
    ConfidenceAnnotation,
    ConfidenceLevel,
    FaultCategory,
    Severity,
)


class FaultPattern(BaseModel):
    """A single fault pattern entry for the Fehlerbild-Atlas."""
    model_config = {"from_attributes": True}

    fault_id: str = Field(..., description="e.g., 'EW-FB-001'")
    name_de: str = Field(..., description="German fault name")
    category: FaultCategory
    visual_description_de: str = Field(
        ..., description="Visual appearance description in German"
    )
    typical_locations_de: list[str] = Field(
        default_factory=list,
        description="Typical locations on a yacht"
    )
    location_frequency: Optional[dict[str, float]] = Field(
        None, description="Location → frequency percentage mapping"
    )
    causes_de: list[str] = Field(default_factory=list)
    effects_de: list[str] = Field(default_factory=list)
    measurement_indicators: list[str] = Field(
        default_factory=list,
        description="Measurable indicators (e.g., 'Voltage drop > 100 mV')"
    )
    severity: Severity
    immediate_action_de: str
    long_term_action_de: str
    visual_detectability: ConfidenceLevel = Field(
        ..., description="How well AYDI Vision can detect this fault"
    )
    reference_images: list[str] = Field(default_factory=list)
    related_faults: list[str] = Field(
        default_factory=list,
        description="Related fault IDs"
    )
    confidence: ConfidenceAnnotation


class FaultDiagnosis(BaseModel):
    """A diagnosed fault instance on a specific yacht."""
    model_config = {"from_attributes": True}

    diagnosis_id: str
    yacht_id: str
    fault_pattern_id: str = Field(
        ..., description="Reference to FaultPattern.fault_id"
    )
    location_de: str
    description_de: str
    measurements: list[dict] = Field(
        default_factory=list,
        description="List of measurement results supporting the diagnosis"
    )
    photo_refs: list[str] = Field(default_factory=list)
    severity: Severity
    status: str = Field(
        default="open",
        description="'open' | 'in_progress' | 'resolved' | 'monitoring'"
    )
    recommendation_de: str
    estimated_repair_cost_eur: Optional[float] = None
    confidence: ConfidenceAnnotation
```

### ANHANG P — Winterfestmachung und Inbetriebnahme

```python
"""
AYDI Electrical Maintenance — Winterization & Commissioning Models
"""

from __future__ import annotations

from datetime import date
from typing import Optional

from pydantic import BaseModel, Field

from .base_models import ConfidenceAnnotation, MeasurementValue, Severity


class WinterizationCheckItem(BaseModel):
    """Single winterization checklist item."""
    model_config = {"from_attributes": True}

    item_id: str
    phase: str = Field(
        ..., description="Phase (e.g., 'preparation', 'power', 'disconnect', 'moisture', 'rodent')"
    )
    description_de: str
    completed: bool = False
    completed_date: Optional[date] = None
    notes: Optional[str] = None


class WinterizationReport(BaseModel):
    """Complete winterization report for electrical systems."""
    model_config = {"from_attributes": True}

    report_id: str
    yacht_id: str
    date_winterized: date
    performed_by: str
    winter_storage_type: str = Field(
        ..., description="'ashore_covered' | 'ashore_open' | 'afloat_marina' | 'afloat_mooring'"
    )
    shore_power_available: bool
    battery_strategy: str = Field(
        ..., description="'onboard_trickle' | 'removed_stored' | 'bms_sleep'"
    )
    battery_soc_at_winterization: Optional[float] = Field(None, ge=0, le=100)
    battery_voltage_at_winterization: Optional[MeasurementValue] = None
    dehumidifier_installed: bool = False
    dehumidifier_type: Optional[str] = Field(
        None, description="'electric' | 'granulate' | 'none'"
    )
    rodent_protection_installed: bool = False
    check_items: list[WinterizationCheckItem] = Field(default_factory=list)
    summary_de: str
    confidence: ConfidenceAnnotation

    @property
    def completion_rate(self) -> float:
        if not self.check_items:
            return 0.0
        done = sum(1 for item in self.check_items if item.completed)
        return round(done / len(self.check_items) * 100, 1)


class CommissioningStep(BaseModel):
    """Single commissioning step."""
    model_config = {"from_attributes": True}

    step_id: str
    step_number: int
    phase_de: str = Field(
        ..., description="Phase (e.g., 'Visueller Check', 'Batterien', 'DC-Basis')"
    )
    description_de: str
    measurement: Optional[MeasurementValue] = None
    expected_value_de: Optional[str] = Field(
        None, description="Expected value (e.g., '> 12,5 V')"
    )
    passed: Optional[bool] = None
    finding_de: Optional[str] = None
    severity: Optional[Severity] = None


class CommissioningReport(BaseModel):
    """Complete commissioning report after winter storage."""
    model_config = {"from_attributes": True}

    report_id: str
    yacht_id: str
    date_commissioned: date
    performed_by: str
    previous_winterization_id: Optional[str] = None
    steps: list[CommissioningStep] = Field(default_factory=list)
    battery_voltage_after_winter: Optional[MeasurementValue] = None
    battery_voltage_after_charge: Optional[MeasurementValue] = None
    all_systems_operational: bool = False
    issues_found_de: list[str] = Field(default_factory=list)
    summary_de: str
    confidence: ConfidenceAnnotation
```

### ANHANG Q — Messgeräte-Datenbank

```python
"""
AYDI Electrical Maintenance — Instrument Database Models
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class InstrumentSpec(BaseModel):
    """Specification of a measurement instrument."""
    model_config = {"from_attributes": True}

    instrument_id: str
    manufacturer: str
    model: str
    category: str = Field(
        ..., description="'multimeter' | 'clamp_meter' | 'insulation_tester' | "
                         "'thermal_camera' | 'battery_monitor' | 'oscilloscope'"
    )
    marine_suitability: str = Field(
        ..., description="'excellent' | 'good' | 'adequate' | 'poor'"
    )
    ip_rating: Optional[str] = None
    cat_rating: Optional[str] = Field(
        None, description="e.g., 'CAT III 1000V / CAT IV 600V'"
    )
    dc_voltage_range: Optional[str] = None
    ac_voltage_range: Optional[str] = None
    dc_current_range: Optional[str] = None
    ac_current_range: Optional[str] = None
    resistance_range: Optional[str] = None
    insulation_test_voltages: Optional[list[int]] = None
    true_rms: Optional[bool] = None
    bluetooth: Optional[bool] = None
    weight_g: Optional[int] = None
    price_eur_approx: Optional[float] = None
    key_marine_features_de: list[str] = Field(default_factory=list)
    limitations_de: list[str] = Field(default_factory=list)


class ManufacturerInfo(BaseModel):
    """Manufacturer information for the Hersteller-Datenbank."""
    model_config = {"from_attributes": True}

    manufacturer_id: str
    name: str
    headquarters: str
    country: str
    founded: Optional[int] = None
    website: Optional[str] = None
    marine_relevance_de: str
    support_dach: Optional[str] = None
    warranty_years: Optional[int] = None
    price_segment: str = Field(
        ..., description="'budget' | 'mid_range' | 'premium'"
    )
    key_products: list[str] = Field(default_factory=list)
```

### ANHANG R — Scoring und Gesamtbewertung

```python
"""
AYDI Electrical Maintenance — Scoring & Overall Assessment Models
"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from .base_models import ConfidenceAnnotation, Severity


class ElectricalSubScore(BaseModel):
    """Score for a single aspect of the electrical system."""
    model_config = {"from_attributes": True}

    aspect: str = Field(
        ...,
        description="Aspect being scored: 'batteries', 'wiring', 'connections', "
                    "'protection', 'insulation', 'grounding', 'shore_power', "
                    "'lighting', 'instruments', 'documentation'"
    )
    score: float = Field(..., ge=0, le=100)
    weight: float = Field(
        ..., ge=0, le=1.0,
        description="Weight of this aspect in overall score"
    )
    weighted_score: float = Field(..., ge=0, le=100)
    severity: Severity
    findings_de: list[str] = Field(default_factory=list)
    recommendations_de: list[str] = Field(default_factory=list)
    confidence: ConfidenceAnnotation


class ElectricalSystemScore(BaseModel):
    """Overall electrical system assessment score."""
    model_config = {"from_attributes": True}

    yacht_id: str
    assessment_date: datetime
    assessor: str
    assessment_level: str = Field(
        ..., description="'level_1_quick' | 'level_2_professional'"
    )
    sub_scores: list[ElectricalSubScore] = Field(default_factory=list)
    overall_score: float = Field(..., ge=0, le=100)
    overall_severity: Severity
    summary_de: str
    critical_issues_count: int = 0
    high_issues_count: int = 0
    medium_issues_count: int = 0
    estimated_remediation_cost_eur: Optional[float] = None
    confidence: ConfidenceAnnotation

    # Score fusion weights (structured vs. visual)
    structured_weight: float = Field(
        default=0.85,
        description="Weight of structured analysis (measurements, data)"
    )
    visual_weight: float = Field(
        default=0.15,
        description="Weight of visual analysis (photos)"
    )

    @property
    def score_category_de(self) -> str:
        """German category based on overall score."""
        if self.overall_score >= 90:
            return "Ausgezeichnet"
        elif self.overall_score >= 75:
            return "Gut"
        elif self.overall_score >= 60:
            return "Befriedigend"
        elif self.overall_score >= 40:
            return "Mangelhaft"
        else:
            return "Ungenügend"

    @property
    def insurance_risk_de(self) -> str:
        """Insurance risk classification in German."""
        if self.overall_score >= 80 and self.critical_issues_count == 0:
            return "Geringes Risiko"
        elif self.overall_score >= 60 and self.critical_issues_count == 0:
            return "Normales Risiko"
        elif self.overall_score >= 40:
            return "Erhöhtes Risiko"
        else:
            return "Hohes Risiko — Auflagen wahrscheinlich"


class ElectricalMaintenancePlan(BaseModel):
    """Generated maintenance plan based on assessment."""
    model_config = {"from_attributes": True}

    plan_id: str
    yacht_id: str
    generated_date: datetime
    based_on_assessment_id: Optional[str] = None
    immediate_actions_de: list[str] = Field(
        default_factory=list,
        description="Actions to take immediately (critical/high severity)"
    )
    short_term_actions_de: list[str] = Field(
        default_factory=list,
        description="Actions within 1-3 months"
    )
    seasonal_actions_de: list[str] = Field(
        default_factory=list,
        description="Actions for next seasonal maintenance"
    )
    annual_actions_de: list[str] = Field(
        default_factory=list,
        description="Actions for next annual inspection"
    )
    five_year_actions_de: list[str] = Field(
        default_factory=list,
        description="Actions for next 5-year revision"
    )
    estimated_total_cost_eur: Optional[float] = None
    priority_order: list[str] = Field(
        default_factory=list,
        description="Ordered list of action IDs by priority"
    )
    confidence: ConfidenceAnnotation
```

**Confidence-Bewertung der Pydantic-Modelle:**
- Modellstruktur: `measured` — direkt aus AYDI-Systemspezifikation abgeleitet
- Grenzwerte in Modellen: `documented` — aus ABYC E-11, ISO 13297
- Pydantic v2 Syntax: `measured` — offizielle Pydantic v2 Dokumentation, model_config = {"from_attributes": True}

---

## Quellen- und Normenverzeichnis

### Primärnormen

| Norm | Titel | Ausgabe | Relevanz |
|------|-------|---------|----------|
| ABYC E-11 | AC & DC Electrical Systems on Boats | 2018 (am. 2023) | Hauptreferenz für alle Elektrik-Grenzwerte |
| ABYC E-2 | Cathodic Protection | 2018 | Kathodischer Korrosionsschutz, Opferanoden, Referenzelektroden-Potentiale |
| ABYC TE-4 | Lightning Protection for Boats | 2016 | Erweiterte Blitzschutz-Richtlinien |
| ISO 13297 | Small craft — Electrical systems — AC installations | 2021 | EU-Standard AC-Installation |
| ISO 10133 | Small craft — Electrical systems — Extra-low-voltage DC | 2012 | EU-Standard DC-Installation |
| IEC 60092 | Electrical installations in ships | 2022 | Professionelle Schifffahrt |
| IEC 60529 | Degrees of protection provided by enclosures (IP Code) | 2013 | IP-Schutzarten |
| ISO 12217 | Small craft — Stability and buoyancy | 2022 | Gewichtsverteilung Batterien |
| ISO 9094 | Small craft — Fire protection | 2015 | Brandschutz Elektrik |

### Sekundärquellen

| Quelle | Typ | Verwendung |
|--------|-----|------------|
| BoatUS Marine Insurance Claim Report 2024 | Statistik | Brandursachen, Schadensverteilung |
| NFPA Marine Fire Statistics | Statistik | Brandursachen-Analyse |
| Pantaenius Versicherungsdaten DACH 2020–2024 | Statistik | Streustrom-Schäden, Elektrik-Ausfälle |
| BSH Seeunfall-Datenbank 2020–2024 | Statistik | Elektrik-bezogene Seenotfälle |
| NETA Maintenance Testing Specifications (MTS) | Richtlinie | Thermografie-Bewertungskriterien |
| Nigel Calder: Boatowner's Mechanical and Electrical Manual | Fachbuch | Praxisreferenz |
| Ed Sherman: Advanced Marine Electrics and Electronics | Fachbuch | Theorie und Praxis |
| Victron Energy Blue Paper | Technische Dokumentation | Batterie-Monitoring, Ladeparameter |
| Fluke Application Notes (Marine) | Anwendungsdokumentation | Messtechnik-Praxis |
| Megger Guide to Insulation Testing | Anwendungsdokumentation | Isolationsmessung-Methodik |

### Hersteller-Datenblätter (direkt referenziert)

| Hersteller | Produkt | Dokument-ID |
|------------|---------|-------------|
| Fluke | 87V Industrial Multimeter | DS-87V-2024-EN |
| Fluke | 376 FC Clamp Meter | DS-376FC-2024-EN |
| Fluke | 1587 FC Insulation Multimeter | DS-1587FC-2023-EN |
| Megger | MIT420/2 | DS-MIT420-2-2023-EN |
| Hioki | DT4282 | DS-DT4282-2024-EN |
| Hioki | CM4376 | DS-CM4376-2024-EN |
| Victron | SmartShunt 500A | VE-DS-SmartShunt-2024 |
| Victron | BMV-712 Smart | VE-DS-BMV712-2024 |
| Marinco | 303SSEL 16A Inlet | DS-303SSEL-2023 |
| Teledyne FLIR | C5 | DS-FLIR-C5-2024-EN |
| Blue Sea | ST Blade Fuse Block | DS-BSS-5025-2024 |
| CTEK | MXS 5.0 | DS-MXS5-2024-EN |
| Ancor | Marine Grade Wire | DS-ANCOR-UL1426-2024 |

---

## Dokumentenhistorie

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0.0 | 2026-05-08 | AYDI Research | Initiale Erstellung |

---

> **Ende der AYDI Wissensdatei 22.12 — Elektrik Wartung und Troubleshooting**
> Letzte Aktualisierung: 2026-05-08
> Nächste geplante Revision: 2026-11-08
